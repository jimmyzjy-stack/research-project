# M016：架构反馈与behavioral eval推进

接收日期：2026-10-31（Asia/Shanghai）。
作者／说话者：Jimmy（用户）。
类型：架构方向的基本认可、十项直接修订与实际评估要求。
来源位置：本轮聊天用户消息。
上下文：M014设计与M015状态命名之后；允许进入behavioral eval，明确最终AGENTS继续暂缓。确认范围不扩大为后续实现或评估结果已经认可。

## 用户原文

整体 architecture 方向基本认可，可以继续进入 behavioral eval，但暂时仍不生成最终 AGENTS.md。

以下是需要调整或进一步明确的地方：

1. Research Planning

我希望将 research-planning 明确视为一个独立的重要能力，而不是完全包含在 deep-dive 中。

我的研究方式强调先找出真正影响长期 FCF 和投资判断的少数关键问题，然后不断根据研究结果重新排序未知问题。

Research Planning 需要能够反复调用，并维护至少：

- research question
- why it matters
- impact on value / decision
- current belief
- uncertainty
- existing evidence
- evidence needed
- whether public information can answer it
- whether offline research is needed
- current research priority

可以先判断是否值得独立成为 Skill；至少在 architecture 上不要将它弱化成 deep-dive 的一次性前置步骤。

2. Research Attractiveness vs Capital Attractiveness

进一步显式区分：

Research attractiveness：一家公司是否值得持续投入认知和研究资源。

Capital attractiveness：以当前价格和信息是否值得投入资本。

两者可以明显不同。

例如优秀 compounder 当前估值很贵，可以具有很高的 research attractiveness，但很低的 capital attractiveness。

而容易理解、赔率很好的 normal value 可以具有较高 capital attractiveness，但未必值得投入大量长期研究资源。

这一点应进入 company research state / candidate comparison 的设计，而不仅是 philosophy 中的一句话。

3. D1

认可正式状态需要我确认，但不要让我确认每一个 thesis 文件版本或每一个估值假设变化。

改成 material / decision-relevant change confirmation。

Main 可以自主更新 evidence、工作模型、机械计算和非实质性假设。

只有可能改变核心 thesis、估值判断、Pool、资本配置或正式投资结论的变化才要我正式确认。

目标是减少 administrative burden。

4. D2

同意建议默认。

在我已经确认的 research questions / research scope 内，Main 应当有较高自主性，可以选择研究方法、公开资料、临时 subagent 和必要工具。

只有研究范围或关键前提发生实质变化时再回来讨论。

5. D3

认可“重大反证待审”机制，但不要让旧正式 thesis 自动失效。

更合适的状态类似：

Material Evidence Under Review

此时：

- 最后一次我确认的 formal thesis 仍然保留；
- 明确标记新的 material evidence 可能影响哪些 thesis；
- 在完成复核前，不使用旧结论自动建议新增资本；
- 不因为一条未核实反证自动修改 thesis、卖出或改变实际持仓。

旧 formal state 与 current actionability 应分开。

6. D4 / Red Team

对于可能成为核心持仓、明显加仓、首次进入重要持仓、核心 thesis 发生重大改变，或我、我们通过讨论已形成很高 conviction 的情况，Red Team 应默认运行，而不仅是可选项。

Evidence Auditor 和 Valuation Reviewer 继续按证据争议和模型复杂度调用。

Red Team 尽量使用两阶段：

第一阶段 blind review：\
先看核心 research question 和必要原始 evidence，在不知道 Main 最终 recommendation / conviction 的情况下形成自己的风险、未知和替代解释。

第二阶段 adversarial review：\
再看 Main thesis / valuation / recommendation，寻找最强 falsification route。

Red Team 的目标不是为了反对而反对。

7. research.md

同意新增 research.md，但它应该是 research cockpit，而不是另一份完整研究报告。

主要维护：

- current research stage
- current understanding
- prioritized research questions
- highest-value unknown
- resolved questions
- evidence gaps
- disagreements
- offline research needed
- next best research action
- material evidence under review

少数核心 thesis 留在 thesis.md，不在 research.md 重复维护。

8. Monitoring

进一步明确 thesis-driven monitoring，而不是 news-driven monitoring。

核心 thesis 应尽量记录：

- what strengthens it
- what weakens it
- what could falsify it
- what should be monitored

新闻、财报、访谈等只是 evidence inputs。

9. Behavioral eval

在现有8类之外增加至少三类：

A. Research priority vs capital priority\
优秀 compounder 当前估值很贵：不一定值得投入资本，但可能仍然具有很高长期研究优先级。

B. Buy hurdle vs Hold hurdle\
已持有、高 confidence compounder forward IRR 从较高水平下降到约15%，business/moat/reinvestment runway 完整，同时当前不会用新增现金以15%主动买入。系统应允许 Hold but don't add，不因“持有=买入”机械卖出。

C. Normal value vs compounder\
高 confidence、低 downside、约25% IRR 的 normal value 可以是合理资本配置机会；同时长期 compounder 可以拥有更高 research priority。不要把公司类型与当前 capital attractiveness 混为一个维度。

10. 三种状态分开

请明确区分：

Research stage\
A/B/C/D pool\
Portfolio status

三者相关但不是同一维度，不要用一个字段替代另外两个。

完成这些调整后，请更新 Architecture Alignment Report 和 behavioral eval expectations。

暂时仍不要生成最终 AGENTS.md。下一步先实际运行 behavioral eval，暴露理解和设计偏差，再决定哪些核心纪律应该进入 AGENTS.md。

