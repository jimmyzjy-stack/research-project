# 临时材料整理约定（非最终投资原则）

当前任务是充分理解用户的投资哲学，持续维护[长篇框架](framework/long-form-investment-framework.md)与[investment ontology](investment-ontology.md)。**只有框架足够稳定并经用户确认后，才提炼最终 AGENTS.md。** 当前文件不是该最终版本。

## 当前必须遵守的处理方式

- 原文先保存，再解释；重要观点保留完整理由、实际决策含义、证据与例子、反例与边界、信心、张力及未解问题，不过早压缩成投资口号。
- 区分用户原话、投资人引述、用户解释与助手推断。用户认同、理解是否准确、观点信心与框架是否稳定分别记录；不编造来源、数据、立场或确认。
- 真实案例保留当时信息和判断过程，提取有条件的暂定思维规则；不能只保存公司结论，也不能把事后结果当成当时依据。
- 张力显式记录；用户如何取舍未知时保留开放问题，不替用户消解或排序。
- 旧助手草案、通用主题清单与 Skill 模板不是用户确认的投资方法。不能把其中的默认选择写成用户的决策原则；尚未明确的偏好与持仓保持未知。
- 中文沟通，用户无需编程或先整理材料。只在关键理解确实受阻时提问，其他整理继续；除用户明确请求外，不委派子代理。

## 路由

按任务先读取完整相关文档，再开展工作：

| 用户任务 | 读取 |
| --- | --- |
| 提供哲学材料、投资人观点或零散想法 | [材料流程](framework/materials/README.md)、长篇框架与 ontology |
| 提供真实案例或复盘 | [casebook](casebook/README.md)、长篇框架与 ontology |
| 要求提炼最终 AGENTS.md | [提炼条件与方法](framework/agents-extraction.md)，先检查用户确认状态 |
| 初筛／深入研究公司 | [candidate-screen](skills/candidate-screen/SKILL.md)／[deep-dive](skills/deep-dive/SKILL.md) |
| 更新判断／证据／财报 | [thesis-management](skills/thesis-management/SKILL.md)／[evidence-update](skills/evidence-update/SKILL.md)／[earnings-update](skills/earnings-update/SKILL.md) |
| 估值／反方审阅 | [valuation](skills/valuation/SKILL.md)／[red-team](skills/red-team/SKILL.md) |

公司研究同样先阅读长篇框架和 ontology，按已明确的含义使用相关文档；理解不足时交付探索性研究与缺口，不假定已经掌握用户方法。

文件操作、来源追溯、日期与版本记录见[工作区约定](framework/workspace-conventions.md)。完成后运行 `python3 evals/check_workspace.py` 并按[框架理解检查](evals/framework-fidelity.md)及适用研究评估审阅；文件检查通过不代表框架稳定或用户已确认。
