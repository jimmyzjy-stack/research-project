# M014：Architecture Alignment与行为评估设计要求

- 接收日期：2026-10-30（Asia/Shanghai）。
- 来源：用户连续两条直接消息。下面分别保留原文。
- 作用：规定本轮知识结构、研究生命周期、Copilot人机分工及评估设计；不是新增的公司事实或助手已获确认的完整架构。
- 原投资理念文件及M003/M012/M013等原文不改，12项理念反馈结果保留。本轮新的设计建议、待确认点和行为预期，与已经明确的投资原则分开。
- 用户明确暂缓AGENTS.md；上一轮候选稿保留为历史草稿，不能沿用此前单独定稿的提示。

## 用户原话一

先再对一下最新版的architecture alignment

## 用户原话二

基于当前已经提供的投资理念、历史讨论以及现有内容，先完成以下设计工作：

一、Investment Philosophy / Ontology

整理我当前明确表达的核心投资原则、定义、decision rules、
不要自行消除尚未解决的矛盾，也不要把单一公司案例泛化成普遍原则。

原始投资理念文件仍然是 source material，不要修改原文。

注意：我理解这部分应该已经完成并且对齐，核对现在是否还有open questions 和仍然存在的 tensions

二、Knowledge Architecture

设计 Harness 的知识层，并明确区分：

raw source material
processed evidence
company-specific knowledge
thesis / valuation / research state
cross-company reusable knowledge
framework / philosophy

明确不同信息的 authority 和 provenance。

历史研究、GPT conversations、管理层发言、网络资料、访谈等都属于 evidence/source，不自动成为thesis。thesis需要对evidence/source整理、分析后，由你或者我或者我们共同讨论生成，此时为初步thesis，另外为便于后续归类、推进继续研究，区分是否有我确认过的thesis（没确认的可能是没看，也可能是还在研究确认，可以根据实用角度分类）

三、Investment Research Lifecycle

按照以下生命周期设计：

Idea Generation
→ 立项
→ Research Planning
→ 初步研究
→ Human Decision Gate
→ 深度研究
→ Human Decision Gate
→ Position Management
→ Ongoing Monitoring

对每个阶段只先定义：

goal
input
AI responsibilities
Jimmy responsibilities
required output
exit / decision gate

暂时不要为每个阶段建立复杂模板。

四、Agent / Skill Architecture

设计一个以 Main Investment Research Agent 为核心的 Copilot 模式。

Main Agent 负责维护完整研究状态、协调研究、综合证据并与我互动，但最终投资判断由我完成。

请区分：

Skill = 可重复的方法和 workflow
Subagent = 需要独立 context / independent judgment 的思考者

初步评估以下角色是否值得成为独立 subagent：

Red Team / Devil’s Advocate
Evidence Auditor
Valuation Reviewer

Red Team 不应为了反对而反对，而应独立寻找最强的 falsification evidence、薄弱假设、未知风险和市场可能正确的原因。

Subagents 默认不直接修改 thesis、valuation 或 portfolio state。它们提交独立报告，由 Main Agent 综合，然后由我决定是否更新正式状态。

对于行业扫描、竞争对手研究、监管研究等任务，优先考虑由 Main Agent 按需创建临时 subagents，而不是预先创建大量固定 agents。

五、AGENTS.md 暂缓

完成以上内容后，不要立刻生成 AGENTS.md。

先给我一份 Architecture Alignment Report，包括：

1. 你如何理解这个 Harness 最终要解决的问题；
2. philosophy layer 的核心内容；
3. knowledge layer 的结构；
4. research lifecycle；
5. main agent / subagent / skill 的边界；
6. 哪些内容未来应进入 AGENTS.md；
7. 哪些应该留在 framework；
8. 哪些应该成为 Skills；
9. 哪些应该成为 Guards / tests；
10. 当前仍需我确认的设计问题。

六、在生成 AGENTS.md 前建立一套 behavioral eval。

请用若干真实投资情景测试你是否正确理解我的投资方式，包括：

高模型 IRR 但低 confidence；
高质量 compounder 当前估值不便宜；
普通 Value 但高 IRR、低 downside；
已经持有的 compounder forward IRR 下降但 thesis 完整；
现金与中等 IRR、高 confidence 机会的比较；
新访谈与旧 thesis 冲突；
股价大跌但没有 fundamental evidence；
Reject 和 Too Hard 的区分。

先展示这些测试的预期处理逻辑，由我确认。

当前目标不是让 Harness 功能更多，而是确保未来所有能力都建立在正确的理念、知识结构和人机分工之上。

## 交付定位（助手整理）

- [Architecture Alignment Report](../../architecture-alignment.md)：覆盖用户列出的10个方面；区分当前实际状态与拟议设计。
- [Behavioral eval预期](../../evals/behavioral-eval-expectations.md)：先列8类情景的预期处理逻辑，等待用户确认；不冒称已运行或通过模型行为测试。
- [变更记录](../changes/M014-architecture-alignment.md)及[原导航/候选快照](../history/pre-M014-architecture-review.zip)。

本轮不创建阶段模板、子代理实现、模型库、数据库或自动交易；不修改真实公司/组合状态。后续来源编号使用M015。

