# M023：立项质量、独立问题生成与历史回放测试

接收日期：2026-10-31（UTC）。作者：Jimmy。来源：本轮聊天。
范围：基于实际立项提炼方法，落实并测试Main主动发现问题；重要项目允许临时Independent Research Question Generator。最终AGENTS继续暂缓，原始理念和历史原件不改。

## 用户原文

在现有 behavioral eval 之外，我希望 Harness 明确建立并验证两个核心能力。

第一，稳定完成高质量立项报告。

第二，也是更重要的：在我尚未提出具体研究问题之前，Main Agent 能够自己识别初步研究和深度研究真正应该解决的关键问题。

1. Initiation Report

我已经提供了约4–5篇过去实际使用的立项报告。

请不要只模仿格式，而是从这些案例中提炼：

* invariant structure；
* 每个部分真正解决的问题；
* 我判断是否值得继续研究的标准；
* Reject / Too Hard / Proceed 的依据；
* 立项阶段合理的信息深度；
* 哪些内容属于基础覆盖，哪些不应该在立项阶段过度研究；
* 写作风格、证据要求和结论粒度。

请评估这些内容如何落实到现有 candidate-screen Skill，而不是为了格式单独制造复杂系统。

未来立项报告需要至少能够建立：

business model
industry / value chain
business traits
competitive advantage / moat
TAM / growth
competition / share
volume-price drivers
profit / FCF drivers
management / governance / capital allocation
valuation snapshot
key risks / unknowns
key research questions
Reject / Too Hard / Proceed

但允许根据公司的实际情况改变重点，不机械填表。

2. Research Question Generation

请将“自己发现关键研究问题”视为 Harness 的独立核心能力。

不要采用：

Search → summarize what was found → generate questions

而采用：

Business understanding
→ Value-driver map
→ What must be true?
→ What is uncertain?
→ Which uncertainty is decision-relevant?
→ Research questions
→ Evidence required
→ Best source
→ Research

对于每个重要公司，Research Planning 应首先建立业务特定的 value-driver map。

然后针对重要节点分别思考：

* What must be true for the current Base Case to hold?
* What do we currently not know?
* Which assumption has the greatest impact on long-term FCF / intrinsic value?
* Which assumption is most likely to be wrong?
* What could falsify the current understanding?
* What does the market appear to believe that we need to test?
* What evidence could realistically resolve this uncertainty?

研究问题不能只是：

“行业未来趋势是什么？”
“公司有什么竞争优势？”
“有哪些风险？”

必须尽量转化成具体、可证伪、可寻找 evidence、能够改变投资判断的问题。

3. Research Question Prioritization

不要建立统一综合评分公式，但按至少三个维度排序：

Decision sensitivity
Uncertainty
Researchability / expected value of information

重点维护当前最有价值的少数问题，而不是无限增长的 checklist。

Research Planning 是循环能力。

每完成一轮研究后，应重新判断：

* 哪些问题已经解决；
* 哪些 confidence 提高或降低；
* 新出现了什么问题；
* 当前 highest-value unknown 是什么；
* 下一单位研究时间最值得投入哪里。

4. Question → Evidence Plan

每个高优先级问题至少在逻辑上对应：

* why it matters；
* affected FCF / value driver；
* current belief；
* current uncertainty；
* evidence that would strengthen it；
* evidence that would weaken it；
* evidence that could falsify it；
* best source type；
* whether public research can answer it；
* whether offline research is required。

不要为了结构完整而强迫所有字段都写成表格。

5. Historical Question-Generation Evals

新增一类 behavioral eval：

不是测试“面对历史问题能不能回答”，而是测试：

在 Jimmy 尚未提出后来那些关键问题的时候，Harness 能不能自己问出来。

使用真实历史研究项目作为 Golden Cases。

优先选择：

* BOSS直聘；
* Timee；
* 瑞幸；
* 携程；
* PDD；
* GMO Payment Gateway。

测试方法：

只提供该公司在历史上“立项完成”或“研究早期”当时可获得的信息。

不要向模型提供我后来形成的关键研究问题、最终 thesis 或之后的研究结论。

要求 Main Agent 输出：

1. 当前 business / value-driver map；
2. 最重要的5–10个 research questions；
3. 为什么这些问题会影响长期 FCF 和投资判断；
4. 哪些问题适合初步研究，哪些只有通过初研后才值得深入；
5. 每个问题最理想的 evidence / source；
6. 当前 highest-value unknown；
7. 下一单位研究时间最应该投入哪里。

之后，再与我历史上实际形成的研究问题进行比较。

评价重点不是关键词命中率，而是：

* Decision relevance
* Causal depth
* Specificity
* Evidenceability
* Falsifiability
* Prioritization
* 是否遗漏后来证明非常重要的 crux
* 是否提出我当时没有想到、但事后看确实重要的新问题

6. 独立 Question Generation

第一版不创建常驻 Question Agent。

先以 Main Agent + research-planning Skill 实现。

但对于重要研究项目，可以按需调用一个临时 Independent Research Question Generator。

该独立角色只读取：

* initiation report；
    -必要 primary sources；
    -基础公司/行业事实；

默认不读取 Main 已经形成的 research plan 或最终 thesis。

它独立提出最重要的 research questions。

Main 对比自己的问题列表和独立列表，寻找遗漏的 decision-relevant questions。

不要通过“两个agent都问了同一个问题”自动提高事实 confidence；这里利用的是思路独立性，不是 evidence independence。

7. Research-planning Skill

基于以上要求，再次评估将 research-planning 从 deep-dive 中拆出成为独立 Skill。

我的当前倾向是应该拆出，因为：

* 它会在立项后、初研后、深研过程中、重大新证据出现后反复运行；
* 它本质上是在配置研究资源，而不是执行 deep research；
* Harness 能否自己找到关键问题，是我判断系统是否真正有价值的重要标准之一。

先落实和测试这一能力，再决定是否生成最终 AGENTS.md。
