#!/usr/bin/env python3
"""检查本地研究文件与清单；仅使用 Python 标准库，不修改任何文件。"""

import argparse
import json
import math
import re
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlsplit


SKILLS = (
    "candidate-screen", "research-planning", "deep-dive", "thesis-management", "evidence-update",
    "earnings-update", "valuation", "red-team",
)
FRAMEWORK = (
    "investment-philosophy", "industry-analysis", "business-analysis",
    "business-quality-and-financials", "moat", "management-and-governance",
    "risk", "valuation", "position-sizing", "evidence-standards",
)
COMPANY_FILES = ("research.md", "thesis.md", "valuation.md", "updates/README.md", "evidence/index.md")
COMPANY_ID = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def read_json(path):
    def unique_keys(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"重复的 JSON 字段：{key}")
            result[key] = value
        return result

    def reject_constant(value):
        raise ValueError(f"不是标准 JSON 数值：{value}")

    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=unique_keys, parse_constant=reject_constant,
    )


def valid_date(value):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return False
    try:
        date.fromisoformat(value)
        return True
    except ValueError:
        return False


def check(root):
    errors = []

    def report(path, message):
        errors.append(f"{path.relative_to(root)}：{message}")

    def require(path):
        if not path.is_file():
            report(path, "缺少文件")

    for relative in (
        "README.md", "AGENTS.md", "framework/README.md", "portfolio/README.md",
        "companies/README.md", "skills/README.md", "scripts/README.md",
        "evals/README.md", "evals/research-quality.md", "evals/decision-consistency.md",
        "investment-ontology.md", "framework/long-form-investment-framework.md",
        "framework/materials/README.md", "framework/agents-extraction.md",
        "framework/workspace-conventions.md", "casebook/README.md", "casebook/_template.md",
        "evals/framework-fidelity.md", "framework/source-and-evidence-policy.md",
    ):
        require(root / relative)
    for name in FRAMEWORK:
        require(root / "framework" / f"{name}.md")

    companies_dir = root / "companies"
    company_dirs = [p for p in companies_dir.iterdir() if p.is_dir()] if companies_dir.is_dir() else []
    require(companies_dir / "_template" / "thesis.md")
    for company in company_dirs:
        if company.name != "_template" and not COMPANY_ID.fullmatch(company.name):
            report(company, "公司目录名应由小写英文、数字与短横线组成")
        for relative in COMPANY_FILES:
            require(company / relative)

    for name in SKILLS:
        path = root / "skills" / name / "SKILL.md"
        require(path)
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            report(path, f"无法读取：{exc}")
            continue
        header = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
        if not header or not re.search(rf"^name: {re.escape(name)}$", header[1], re.M):
            report(path, "Skill 的头部 name 与目录名称不一致")
        if not header or not re.search(r"^description: \S.+$", header[1], re.M):
            report(path, "Skill 缺少 description")

    count = 0
    for filename, key, fields in (
        ("holdings.json", "positions", ()),
        ("watchlist.json", "companies", ("reason",)),
        ("candidate-box.json", "companies", ("research_question", "next_step")),
    ):
        path = root / "portfolio" / filename
        try:
            data = read_json(path)
        except (OSError, UnicodeError, ValueError) as exc:
            report(path, f"无法读取 JSON：{exc}")
            continue
        if not isinstance(data, dict) or not isinstance(data.get(key), list):
            report(path, f"顶层必须是对象，{key} 必须是列表")
            continue
        records = data[key]
        count += len(records)
        if "as_of" not in data or (data["as_of"] is None and records):
            report(path, "非空清单需要 as_of 日期；空清单也需保留 as_of 字段")
        elif data["as_of"] is not None and not valid_date(data["as_of"]):
            report(path, "as_of 必须是 YYYY-MM-DD 格式的有效日期")
        seen = set()
        known_weight = 0.0
        for index, record in enumerate(records, 1):
            label = f"第 {index} 条"
            if not isinstance(record, dict):
                report(path, f"{label}必须是对象")
                continue
            company_id = record.get("company_id")
            if not isinstance(company_id, str) or not COMPANY_ID.fullmatch(company_id):
                report(path, f"{label}的 company_id 格式无效")
            elif company_id in seen:
                report(path, f"{label}的 company_id 重复：{company_id}")
            else:
                seen.add(company_id)
                if not (companies_dir / company_id).is_dir():
                    report(path, f"{label}引用的公司目录不存在：{company_id}")
            for field in ("name", *fields):
                if not isinstance(record.get(field), str) or not record[field].strip():
                    report(path, f"{label}需要非空文字字段 {field}")
            if filename == "holdings.json":
                weight = record.get("weight_pct")
                if "weight_pct" not in record:
                    report(path, f"{label}缺少 weight_pct，未知请使用 null")
                elif weight is not None:
                    if type(weight) not in (int, float) or not 0 <= weight <= 100 or not math.isfinite(weight):
                        report(path, f"{label}的 weight_pct 应为 0–100 的有限数字或 null")
                    else:
                        known_weight += weight
            if filename == "watchlist.json" and record.get("next_review") is not None:
                if not valid_date(record["next_review"]):
                    report(path, f"{label}的 next_review 应为有效日期或 null")
        if known_weight > 100 + 1e-8:
            report(path, "已知持仓比例之和超过 100%")

    for path in sorted(root.rglob("*.md")):
        if any(part in {".git", ".venv", "__pycache__"} for part in path.relative_to(root).parts):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            report(path, f"无法读取：{exc}")
            continue
        for link in re.findall(r"!?\[[^\]\n]*\]\(([^)\n]+)\)", text):
            target = link.strip().split(' "', 1)[0].strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            destination = (path.parent / unquote(parsed.path)).resolve()
            if not destination.is_relative_to(root) or not destination.exists():
                report(path, f"本地链接不存在或越过仓库目录：{target}")

    return errors, count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    root = parser.parse_args().root.resolve()
    errors, count = check(root)
    if errors:
        print(f"检查失败：{len(errors)} 个问题")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"文件检查通过：3 份清单，{len(SKILLS)} 个 Skill，{count} 条清单记录。")
    print("此结果仅验证文件结构与格式；研究质量和判断一致性仍需人工审阅。")
    if count == 0:
        print("清单尚未录入真实记录，不代表实际没有持仓。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
