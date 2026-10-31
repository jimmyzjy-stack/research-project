# M014：架构设计与行为预期，AGENTS继续暂缓

日期：2026-10-30。直接要求见[M014原话](../materials/M014-2026-10-30-architecture-design-request.md)。本轮完整交付为[Architecture Alignment Report](../../architecture-alignment.md)与[behavioral eval预期](../../evals/behavioral-eval-expectations.md)。

## 已完成的设计

- 核对已有哲学/ontology和T/U状态：保留12项反馈成果、33个C/24个B；未发现阻塞本次设计的新核心理念问题。列明已解释的差异与仍须个案取舍的张力，不伪称张力全消失。
- 设计六类知识及其authority/provenance，区分作者、证据可信度、研究阶段、A/B/C/D和Jimmy版本确认；不将source/evidence自动升级为thesis。
- 定义9个生命周期节点，各含goal/input/AI responsibilities/Jimmy responsibilities/required output/exit或gate；不创建逐阶段模板。
- 设计Main Copilot、Skills及独立subagents边界，评估Red Team/Evidence Auditor/Valuation Reviewer的按需价值；不启动subagents或建立执行系统。
- 给出未来AGENTS/framework/Skills/Guards的内容去向及D1–D4操作设计确认点。
- 设计用户指定的8类行为预期，明确真实材料锚与测试假设，不编历史持仓、交易、当前价格或结果；尚未运行、没有通过结论。

## 当前实现与建议分开

研究仍只有公司模板，7个Skills仍为通用草稿，3份portfolio清单为空。research.md与knowledge主题笔记属于未来最小建议，本轮不创建。现有文件检查不是behavioral eval，不以其通过证明理念或人机边界已被验证。

本地Git尚无提交；已有原件与快照不是Git/GitHub提交历史。本轮不提交/推送，不扩代码、数据库、服务或计算库。

## 现有文件处理

AGENTS.candidate.md和来源对照改为“前轮草稿暂停采用”，保留原17条及映射；不覆盖AGENTS.md。导航指向新报告和预期文件，取消此前直接确认旧候选即可定稿的当前路径。更新前7份文件保留于[快照](../history/pre-M014-architecture-review.zip)。

open-questions的T006旧标题易误读为三层治理处理，按已经明确的M012修正为红线与合并风险/警惕。原始M005/M012等材料、投资理念DOCX、长篇框架、ontology和真实公司/组合状态均保持原样。

下一步由Jimmy先核对架构设计与8类预期逻辑；不把未回复当确认。AGENTS定稿及Skills落实留待之后，不能凭旧候选或文件检查跳过这一步。
