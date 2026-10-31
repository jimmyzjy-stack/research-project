# M022：Source Discovery、Evidence Policy与Research Planning设计要求

接收日期：2026-10-31（本轮环境时区UTC）。
作者／说话者：Jimmy（用户）。
类型：已认可架构上的研究方法与文档优化要求；不授权生成最终AGENTS或增加自动化平台。
来源：本轮聊天。下方原话完整保留；助手设计、实现及评估状态另放变更报告。

## 用户原文

基于当前已经确认的 Architecture Alignment Report，请进一步完善 Harness 的 Source Discovery、Evidence Policy 和 Research Planning 能力。

这次任务的目标不是增加更多自动化，也暂时不要生成最终 AGENTS.md。

目标是解决一个核心问题：

在立项、初步研究、深入研究和持续跟踪中，Main Agent 不仅要能够分析用户提供的材料，还应该能够主动判断：

1. 当前最重要的研究问题是什么；
2. 什么样的 evidence 才能回答这个问题；
3. 哪类 source 最适合提供这种 evidence；
4. 应该主动寻找哪些公开或一手资料；
5. 找到资料以后应该如何评估其可信度、独立性、代表性和局限；
6. 多条 evidence 如何共同改变 company understanding、thesis 和 confidence。

请在现有 architecture 基础上完成以下优化。

⸻

一、建立 Source Discovery & Evidence Policy

请新增或完善一份 framework 层面的 Source & Evidence Policy。

文件名可以根据现有 repo 结构决定，例如：

framework/source-and-evidence-policy.md

不要把它写成简单的“来源可信度排行榜”。

核心原则应该是：

source 的可信度取决于它试图支持的具体 claim，而不存在一种 source 在所有问题上都绝对更可信。

例如：

公司财报、交易所公告、监管申报，对于以下事实通常是最高优先级来源：

* 历史财务数字；
* 股本；
* 现金；
* 门店数量；
* 回购；
* 管理层任免；
* 已披露合同；
* 公司正式经营指标。

但是：

管理层对 TAM、竞争优势、未来增长、客户满意度等判断，即使出现在正式公告中，也首先只是 management claim，而不是这些结论本身已经被证明。

因此需要明确区分：

“这个来源可靠地证明了谁说过什么”

和

“这个来源可靠地证明了现实世界确实是什么”。

⸻

二、建立默认 Source Prior，而不是绝对评分

可以建立来源类型的 default prior，用于指导研究，但不要建立统一的机械分数。

大致考虑以下来源类别：

A. Primary / authoritative sources

包括但不限于：

* 公司年报、季报、招股书；
* 交易所公告；
* SEC / 港交所 / 日本交易所等监管申报；
* 政府部门；
* 法院和监管处罚文件；
* 官方统计；
* 公司正式电话会；
* 竞争对手正式披露。

通常优先用于：

历史事实、正式披露、财务数字、法律和治理事实。

主要风险：

* selective disclosure；
* management incentives；
* 前瞻性陈述；
* 口径选择。

⸻

B. 原始数据与一手实证数据

例如：

* 业务原始数据；
* transaction data；
* 行业数据库；
* app / traffic / pricing data；
    -招聘、酒店、商品等实际行为数据。

通常具有较高证据价值，但必须检查：

* sample；
* coverage；
* denominator；
* methodology；
* data cleaning；
* survivorship；
* period consistency。

⸻

C. Academic empirical research

尤其重视：

* large-sample empirical work；
* longitudinal research；
* natural experiments；
* causal inference；
* 一手调查和实证研究。

对于商业机制、消费者行为、劳动市场、multi-homing、网络效应等问题，优质论文可能比新闻或普通行业观点具有更高 evidence value。

但必须单独评估：

external validity / transfer assumptions

即：

论文证明了什么？

我们正在把这个结论迁移到什么公司、国家、行业、用户群体或时期？

中间需要哪些额外假设？

论文不能因为方法严谨就自动证明目标公司的 thesis。

⸻

D. First-hand field research

包括：

* 客户访谈；
* 员工访谈；
* 供应商访谈；
* 经销商访谈；
* 竞争对手访谈；
* 专家访谈；
* 用户调查；
* Jimmy 自己的一线调研。

这些来源对于理解：

* 用户行为；
* 客户 switching；
* multi-homing；
* 真实采购流程；
* 行业运行机制；
* 销售过程；
* WTP；
* 产品体验；

可能比公司官方资料更有价值。

但是必须明确记录：

* 受访者身份和角色；
* 公司/机构规模；
* 地区；
* 时间；
* 样本数；
* recruitment / transaction volume；
* selection bias；
* incentive；
* 是否具有代表性；
* 是否可能只是异常案例。

少量访谈不能未经论证直接外推整个行业。

⸻

E. High-quality analytical secondary sources

包括：

* 优质投资机构 letters；
* 优秀投资人研究；
* Value Investors Club；
* 优质基金的 long / short thesis；
* 高质量券商研究；
* 行业咨询机构；
* 专业行业报告。

这一类 source 不应该简单归为“新闻”。

其中部分研究质量可能明显高于普通媒体。

它们最大的价值通常是：

1. 发现被忽略的 research question；
2. 提供 competing thesis；
3. 提供 causal mechanism；
4. 提供数据或一手调查线索；
5. 帮助 Red Team 找到市场可能正确的理由。

但这些仍属于 analytical secondary source。

其中的关键事实、数据和 conclusion，如果 decision-relevant，应尽量回到 primary source 或独立验证。

不能因为作者是著名投资人或优秀基金，就自动提高 claim 为事实。

需要考虑：

* position bias；
* selection bias；
* incentives；
* source dependency；
* data freshness。

⸻

F. Professional / mainstream media

例如主流财经媒体、专业记者和行业新闻。

主要作用是：

* event discovery；
* interviews；
* current developments；
* regulatory developments；
* leads。

一般不作为最重要 thesis 的唯一 evidence。

如果媒体报道引用另一份报告或公司说法，应尽量追溯原始来源。

⸻

G. Industry media / forums / Reddit / X / employee reviews 等

主要作为：

* lead generation；
* anomaly detection；
* 用户情绪；
* 员工体验；
* 产品体验；
* 可能的新问题。

不能因为大量帖子重复出现就自动视为独立 evidence。

可以提高 research priority，但关键结论需要进一步验证。

⸻

H. AI-generated content

AI summary、AI explanation、旧 GPT 回答本身：

不能作为独立 evidence。

AI 可以帮助：

* 找 source；
* 整理 source；
* 比较 source；
* 推导；
* 提出 hypothesis。

但必须追溯到实际 evidence。

⸻

三、建立 Claim-level Evidence Assessment

重要 evidence 不采用简单 Source A/B/C 标签判断真实性。

Main Agent 应根据具体 claim，从以下维度进行判断：

* Proximity：是否一手；
* Authority：是否有正式、法律或专业责任；
* Incentive：来源是否有夸大、隐瞒或销售动机；
* Methodology：信息如何产生；
* Sample / Representativeness：样本是否能代表目标问题；
* Independence：是否真正独立于其他来源；
* Recency：是否仍然适用于当前情况；
* Relevance：是否真正回答当前 research question；
* External validity：跨行业/跨国/跨时间迁移是否合理；
* Falsifiability：是否存在可以验证或证伪的方法。

这些维度用于 reasoning，不需要建立机械综合分数。

Evidence 可以具有高可信度但低 relevance，也可以高 relevance 但低 representativeness。

⸻

四、增加一个非常重要的 Guard：

Source count ≠ Evidence count

如果 Bloomberg、Reuters、券商报告、投资人文章和行业媒体全部引用公司 CEO 同一句话：

这不是五个独立 evidence。

这是：

一个 management claim，被五个 secondary sources 转述。

Harness 必须尽量识别：

* common source；
* circular citation；
* common dataset；
* 同一采访被多次转载；
* 同一个 sell-side model 被多个媒体转述。

不得使用“多个来源都这么说”制造虚假的 confidence。

这一原则应纳入 Evidence Policy 和相关 guard / behavioral eval。

⸻

五、让 Research Planning 反向决定 Source Discovery

不要采用：

Search → 找到什么 → 研究什么

这种模式。

希望形成：

Investment question
→ Research question
→ What evidence would resolve it?
→ Best possible source
→ Search / collect
→ Evaluate source quality
→ Cross-check
→ Evidence
→ Company understanding
→ Thesis / valuation / decision

因此，请强化 research-planning。

Research Planning 对每个重要 research question 至少应考虑：

* Question
* Why decision-relevant
* Which FCF driver it affects
* Current belief
* Current uncertainty
* What evidence would strengthen the belief
* What evidence would weaken it
* What evidence could falsify it
* Best source types
* Currently available sources
* Primary-source availability
* Alternative evidence if ideal data is unavailable
* Whether public research can answer it
* Whether offline research is necessary
* Research priority
* Expected value of further research / whether more work is worthwhile

不要求每个字段都机械填写成表格。

重点是让 Main Agent真正形成：

Question → Evidence Plan → Source Plan

⸻

六、不同 Research Stage 要主动寻找不同类型资料

1. Idea Generation

不要求全面查资料。

主要目标：

* 找到异常；
* 判断为什么值得研究；
* 找到初步 primary source；
* 确认公司和机会不是建立在错误信息之上。

输出以 research lead 为主。

⸻

2. 立项

Main Agent 应主动寻找基础 primary sources，而不是等待我提供。

通常包括：

* 最新年报；
* 最近季报；
* 招股书；
* investor presentation；
* earnings call；
* 官方经营数据；
* shareholder / governance；
* buyback / dividend；
* 主要监管资料；
* 主要竞争对手官方资料；
* 基础行业数据；
* 少量高质量第三方行业资料。

目标是建立 business skeleton：

* 公司怎么赚钱；
* 客户是谁；
* 产业链；
* 竞争对手；
* unit economics；
* growth drivers；
* governance；
* 未来 FCF 的主要变量。

立项阶段不需要为了完整性大量搜索二手文章。

⸻

3. 初步研究

研究开始从：

“公司说自己是什么”

转向：

“这个商业机制实际上是否成立”。

主动增加：

* 竞争对手年报；
* 上下游公司资料；
* 行业数据；
* academic research；
* 优质投资人研究；
* high-quality sell-side；
* 客户/员工/供应商资料；
* 监管历史；
* 海外/行业 comparable。

目标是：

* cross-check management narrative；
* 找 competing explanations；
* 判断 moat；
* 判断 business traits；
* 初步判断 FCF mechanism。

⸻

4. Deep Research

不要默认继续堆积报告。

所有 source discovery 应围绕 unresolved key questions。

例如：

Question：
Timee 网络效应究竟有多强？

Evidence plan 可能包括：

* employer multi-homing；
* worker multi-homing；
* fill rate 与 density；
* retention；
* competitor adoption；
* geography；
* 客户切换历史。

然后再决定：

最适合的是企业访谈、劳动者调查、竞争对手数据、academic platform research、Timee operating data，还是其他证据。

Deep Research 的目标不是收集更多资料，而是减少 decision-relevant uncertainty。

⸻

5. Ongoing Monitoring

坚持 thesis-driven monitoring，而不是 news-driven monitoring。

每个重要 thesis 尽量记录：

* What strengthens it
* What weakens it
* What could falsify it
* What should be monitored
* Which source is best suited for monitoring it

财报、新闻、访谈、价格、监管等只是 evidence inputs。

不要把“发生了很多新闻”误认为 thesis 发生了很多变化。

⸻

七、不同问题应有不同的“最佳证据”

请避免默认认为：

公司公告 > 论文 > 新闻 > Reddit

是适用于所有问题的固定排序。

例如：

Historical revenue

最优 source 通常是：

公司正式财报 / regulatory filing。

Management intention

公司电话会可以可靠证明：

“management said X”

但不能自动证明 X 会实现。

Customer switching behavior

客户访谈、交易数据、调查或行为研究可能比公司官方 claim 更重要。

Network effects

需要综合：

用户行为、
multi-homing、
liquidity、
fill rate、
市场密度、
competition、
switching、
学术机制研究。

TAM

management estimate 只是一个 estimate。

需要尽量：

bottom-up data、
industry statistics、
customer numbers、
volume × price、
historical analogues。

Regulatory risk

监管/法律原文优先于媒体摘要。

请让 Source Policy 强调：

Primary sources are preferred for claims they are uniquely qualified to establish; no source is universally authoritative across all claim types.

⸻

八、Evidence Update Skill 应进一步强化

现有 evidence-update 不只是“收到资料后摘要”。

重要 evidence 应在逻辑上保留以下信息：

* claim
* source
* source type
* original source location
* date / observation period
* first-hand / second-hand
* fact / estimate / opinion / inference
* source incentives / likely bias
* sample / representativeness where relevant
* independence from other sources
* supports / weakens / neutral to which thesis or research question
* limitations
* remaining uncertainty

不要为了结构完整而要求所有信息都变成复杂 JSON。

优先保证 human-readable Markdown。

⸻

九、优秀投资人和投资机构研究的特殊处理

优秀投资人的文章、公开信、VIC、基金 long / short thesis 等，不应简单与普通媒体归为同一层。

它们可以作为：

high-value analytical secondary source。

重点使用方式：

Question discovery

别人发现了什么我们没有想到的问题？

Competing thesis

他们的 causal mechanism 与我们的 thesis 有何不同？

Evidence lead

他们引用了哪些原始数据、客户调查或监管文件？

Red Team input

short seller / contrarian thesis 可以作为重要 falsification source。

但 Harness 不应因为：

“Buffett / Pabrai / 某知名基金这样认为”

就提高事实可信度。

Investment reputation ≠ evidence.

重要 claim 尽量独立验证。

⸻

十、Academic Evidence 的特殊处理

优质论文可以具有非常高的信息价值。

但在使用 academic research 时，Main 应明确：

1. 论文实际证明了什么；
2. 样本是什么；
3. 方法是什么；
4. 是否存在因果识别；
5. effect size；
6. 适用时期；
7. 国家 / 行业 / demographic；
8. 我们想把它迁移到什么问题；
9. 中间有哪些 transfer assumptions；
10. 哪些目标公司 evidence 仍然需要补充。

例如：

论文发现低技能劳动者 multi-homing 较低

不能直接升级为：

BOSS 蓝领网络效应很强。

需要拆成：

skill / occupation
→ multi-homing
→ platform liquidity
→ employer behavior
→ hire outcome
→ monetization

分别验证其中关键连接。

⸻

十一、与 Agent Architecture 的关系

暂时不要为了 source discovery 新增很多固定 subagents。

Main Agent 应负责：

* Research Planning；
* Source Planning；
* Public source discovery；
* evidence synthesis。

需要时可以临时 spawn：

* academic research agent；
* competitor research agent；
* regulatory research agent；
* industry data agent；

但这些是 temporary bounded tasks。

Evidence Auditor 仍然只在：

* 关键 evidence 存在争议；
* source dependency；
* interview representativeness；
* external validity；
* data methodology；

等情况下按需调用。

Red Team 仍保持独立角色。

⸻

十二、对 Research Attractiveness 的影响

Source / Evidence Planning 还应影响 Research Attractiveness。

如果一家公司：

* 非常优秀；
* 潜在长期 compounder；
* 当前不便宜；

它仍然可能值得持续建立 company knowledge。

但如果决定公司价值的核心问题：

* 无法获得 evidence；
* 无法建立可验证判断；
* 关键 FCF driver 长期不可知；

则应该降低 Research Attractiveness，甚至进入 Too Hard。

也就是说：

研究价值不仅取决于：

potential upside

还取决于：

ability to learn。

⸻

十三、新增 Behavioral Evals

请在现有 behavioral eval 基础上增加 Source / Evidence 相关测试。

至少包括：

Test 1：五个来源其实同源

五篇文章都引用公司 CEO 的同一 TAM 数字。

系统必须识别为一个 management claim，而不是五个独立 evidence。

Test 2：公司公告 vs 客户行为

公司称客户粘性极强，但多家有代表性的客户访谈显示经常 multi-home。

系统不能因为 company filing 来源等级更高就自动覆盖一手客户 evidence。

Test 3：著名投资人 thesis

知名基金提出一个非常有说服力的 thesis。

系统应将其作为 analytical source / hypothesis，并追踪 underlying evidence，而不是直接采纳为事实。

Test 4：高质量论文但 external validity 较弱

美国白领平台论文用于推导中国蓝领平台。

系统必须明确 transfer assumptions，而不能直接套用结论。

Test 5：大量论坛 signal

Reddit / X / 员工评论出现大量相同投诉。

系统可以提高 research priority，但不能直接升级为正式 thesis。

Test 6：Primary source 也可能有 incentive bias

管理层在 earnings call 预测新业务未来三年高速增长。

系统应该可靠记录“management said this”，但不能把前瞻预测视为已经证明。

Test 7：缺少理想 evidence

一个关键 research question 没有公开数据。

Main 应提出：

* proxy；
* alternative source；
* interview；
* survey；
* cross-company analogue；
* 或承认 unknown。

不得因为没有数据就用低质量 evidence 填补 confidence。

⸻

十四、本轮希望 Codex 实际完成的工作

请：

1. 先检查当前 repo 中与以下内容相关的文件：
    * Architecture Alignment Report
    * investment ontology
    * framework
    * research lifecycle
    * evidence-update
    * deep-dive
    * candidate-screen
    * behavioral eval
2. 给出哪些现有内容已经覆盖上述要求、哪些缺失、哪些冲突。
3. 更新 Architecture Alignment Report 中相关部分。
4. 建立或更新 Source & Evidence Policy。
5. 将 Research Planning 明确强化为：
    Question → Evidence Plan → Source Plan。
6. 评估 research-planning 是否应该成为独立 Skill。
    我的当前倾向是：它值得成为独立 Skill，因为研究问题排序和信息价值判断会在整个研究过程中反复调用，而不仅是 deep-dive 的一次性前置步骤。
    如果你认为不需要独立 Skill，请具体解释如何保证这一能力不会被 deep-dive 弱化。
7. 更新 evidence-update Skill 的设计要求。
8. 更新 behavioral eval expectations，加入 Source / Evidence 类测试。
9. 不要修改原始 investment philosophy source material。
10. 暂时不要生成最终 AGENTS.md。

最后请输出一份：

Source & Evidence Architecture Change Report

说明：

* 改了什么；
* 为什么改；
* 哪些属于 framework；
* 哪些属于 Skill；
* 哪些属于 Guard；
* 哪些属于 behavioral eval；
* 哪些仍然需要我判断；
* 是否发现现有 architecture 与上述原则存在冲突。

核心目标不是让 Harness “搜索更多资料”。

核心目标是学会：

先知道自己需要知道什么，再知道什么证据能够回答它，再寻找最合适的来源，并清楚知道这些证据究竟能够支持到什么程度。而同时能够判断哪些是更需要一手调研去获得的，从而可以及时让我去进行线下调研。

## 实现与确认边界

[变更报告](../../source-and-evidence-architecture-change-report.md)区分已覆盖、缺口、执行冲突与本次修改。方法要求来自本条直接说明，不把报告的操作展开或新评估预期冒充已逐字确认。原始理念、历史资料和旧实际评估回答不修改，最终AGENTS继续暂缓。
