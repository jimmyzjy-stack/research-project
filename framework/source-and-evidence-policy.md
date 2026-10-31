# Source Discovery & Evidence Policy

依据：[M022直接要求](materials/M022-2026-10-31-source-evidence-design.md)、[架构](../architecture-alignment.md)与[研究哲学](research-philosophy.md)。这是研究方法规范，不改写原始投资理念，不设来源综合分数，也不证明某家公司thesis。

## 1. 问题先于来源

Investment question → Research question → Evidence Plan → Source Plan → 主动寻找/收集 → claim-level评估与cross-check → company understanding → thesis / valuation / decision。

Main在已确认范围内主动发现公开资料，不能只处理Jimmy上传的材料。先问哪些观察能区分当前解释与最强替代解释，再决定去哪里找；意外线索可以触发重排，不因搜索结果多就改变研究重点。执行见独立[research-planning Skill](../skills/research-planning/SKILL.md)。

Source是信息载体及产生者；claim是具体命题；evidence是对某个问题有支持、削弱或中性作用的可定位观察、记录或有明确前提的推导。未经核实的陈述可登记，但编号E不等于已证事实。一份文件可包含多条claim，多个文件也可能没有增加独立证据。

**Primary sources are preferred for claims they are uniquely qualified to establish; no source is universally authoritative across all claim types.**

始终分开：可靠证明“谁在何时说了什么”，与足以证明“现实世界是什么”。年报准确记录管理层TAM预测，不证明TAM准确；亲历客户能解释自己的采购行为，但不因此代表全部客户。原始资料和正式披露也可能出错、重述或选择性呈现。

## 2. Default Source Prior，而非来源排行榜

A–H是类型代号，不是可信等级，也不是公司A/B/C/D pool。同一资料中的正式数字、预测、外部引述和作者推断分别评估。

| 类型与例子 | 通常适合回答 | 主要限制 |
| --- | --- | --- |
| A Primary / authoritative：年季报、招股书、交易所/SEC/港交所/日本交易所申报、政府/法院/处罚文件、官方统计、正式电话会、竞争对手披露 | 历史财务、股本、现金、门店及正式经营指标、回购分红、任免、已披露合同、法律与正式政策事实 | 核版本、期间、定义、法律效力、审计/重述；selective disclosure、management incentives、前瞻陈述和口径选择。对手也有激励偏差 |
| B 原始/一手实证数据：业务、transaction、行业数据库、app/traffic/pricing、招聘/酒店/商品行为 | 量价、使用、采购、供需、留存和实际行为 | sample、coverage、denominator、methodology、data cleaning、survivorship、period consistency；数据库预测不是原始观测 |
| C Academic empirical：大样本、纵向、自然实验、因果识别、一手调查 | 商业机制、消费者/劳动市场、multi-homing、网络效应 | 看识别对象、样本、方法、effect size、时期与external validity；方法严谨不自动证明公司thesis |
| D First-hand field research：客户/员工/供应商/经销商/竞争者/专家访谈、用户调查、Jimmy一线调研 | 实际采购/销售流程、switching、multi-homing、WTP、体验和运行机制 | 身份/亲历范围、规模/地区/时间、招募与样本、业务量、selection bias、incentive、代表性和异常案例；一手非天然无偏 |
| E High-quality analytical secondary：机构letters、优秀投资人、VIC、基金long/short、优质券商、咨询/行业报告 | Question discovery、competing thesis、causal mechanism、原数据/调研线索、Red Team反证 | position/selection bias、incentives、source dependency、data freshness；重要claim追原件或独立验证。研究质量可高于普通媒体，投资声誉不证明事实 |
| F Professional / mainstream media：专业记者、主流财经与行业新闻 | Event discovery、采访、近期发展、监管线索 | 区分原创调查/采访与转述，追被引报告/公告；通常不是最重要thesis的唯一依据，原始调查按具体内容判断 |
| G 行业媒体、论坛、Reddit、X、员工评论 | Leads、anomaly detection、用户情绪、员工/产品体验 | 自选择、刷帖、投诉倾向、转载/同源；重复多可提高研究优先，不证明发生率或正式thesis |
| H AI summary/explanation、旧GPT回答 | 找/整理/比较source、可复算推导、提出hypothesis | AI文本不是独立现实证据；追到实际原件、核引文计算。“用户认为”不证明Jimmy确认，多个AI引用同一数据不增加独立观测 |

类型由claim决定：基金自己的访谈有一手观察，基金投资结论仍是分析；媒体原采访有一手陈述，转发公司数字仍依赖公司；正式披露引用外部数据库也需追数据源。不能把整篇文章盖一个等级后忽略内容差异。

## 3. Claim-level Evidence Assessment

重要claim按以下维度说明理由，可用短段落；未知/不适用明示，不机械填十项分数，不合成总分。

| 维度 | 判断内容 |
| --- | --- |
| Proximity | 亲历/原记录还是听闻、转述、推导？实际能观察什么？ |
| Authority | 正式、法律、专业责任覆盖哪条claim？ |
| Incentive | 持仓、销售、募资、雇佣、声誉、付费/招募可能怎样选择或遗漏？有偏见不自动虚假 |
| Methodology | 如何采集、提问、定义、清洗、计算，能否复核？ |
| Sample / Representativeness | 覆盖谁、什么机构/地区/交易/时期，遗漏谁，能外推到哪里？ |
| Independence | 是否同原话/采访、同数据/面板、共享模型或循环引用？独立分析与独立观测分开 |
| Recency | 观察期是否适合目标期，制度/产品/竞争是否变化？新检索不等于新资料 |
| Relevance | 真正回答哪个research question/FCF driver，还是只题材相似？ |
| External validity | 从什么国家/行业/群体/时期迁移到什么目标，前提和缺的本公司证据是什么？ |
| Falsifiability | 哪种可得观察会支持、削弱或证伪？不为整齐造阈值 |

可信度高但不相关、相关性高但无代表性都可能存在。结论限定为“该地区这类大客户观察到multi-homing”，不能跳到“所有客户不忠诚”。

## 4. Source count ≠ Evidence count

Bloomberg、Reuters、券商、投资人文章和行业媒体若都引用CEO同一个TAM数字，是**一个management claim被五次转述**，不是五次独立验证。记录简短的共同来源说明即可，不建全局图数据库。

识别common source、circular citation、common dataset、同次采访转载、共同sell-side model、同一调查面板/图表。网站、作者、机构或AI不同不证明独立；依赖未查清就保留未知，不默认独立。

按claim判依赖：同篇文章可以重复CEO数字，同时包含独立客户观察；只把各部分各自有依据的贡献分开使用。共用数据的论文可有不同分析，但不是几套独立观测。一份正式股本申报也不需要凑五份转载才够可信。

例：记“原信息=某日CEO电话会TAM估计；五篇均转述；未做bottom-up核查”，再找客户数×可服务量×价格、官方分母或独立行为数据；不能用文章数抬confidence。

## 5. Question对应最佳证据

| 问题 | Evidence Plan → Source Plan |
| --- | --- |
| Historical revenue / 股本 / 回购 / 现金 | 同期财报/监管申报、附注和重述；核单位、合并范围、期间、股份类别 |
| Management intention | 电话会/正式文件证明说过/计划；预算、资本配置、里程碑和执行用于检验能否兑现 |
| Customer switching | 交易/采购/留存/切换记录，适当覆盖的客户访谈/调查；问真实经历和备选平台，不只问满意度 |
| Network effects | employer/worker multi-homing、liquidity、fill rate与density、留存、竞争采用、geography、switching history，加机制论文 |
| TAM | 自下而上客户数、可替代量/工时、频率和价格；行业统计及有前提的历史类比；避免人次/人数/工时混算和重复计数 |
| Regulatory risk | 法律/法规/监管原文、版本、施行日、适用对象与执法；区分草案、讲话、正式规则和解释，新闻用于发现后追原文 |

这不是所有公司都要搜齐的清单。找不到理想数据时，不用方便但无关的材料代替。

## 6. Academic Evidence的迁移链

关键论文保留十项：实际发现什么；样本；方法；有无因果识别/识别了什么；effect size及单位/不确定性；适用时期；国家/行业/demographic；本次迁移到什么问题；transfer assumptions；仍需补哪些目标公司证据。未报告的效应量不编。作者结论、我们推导、相关关系与因果关系分开；统计显著不自动等于商业重要。

假想例子，不是对某论文/BOSS的事实认定：美国白领平台或低技能劳动者multi-homing研究，不能直接证明中国蓝领平台网络效应。拆成skill/occupation → multi-homing → platform liquidity → employer behavior → hire outcome → monetization，验证关键连接，检查渠道、制度、用户与付费差异。严谨研究可以启发机制，不能省略本地/本公司的证据。

## 7. 一线研究与及时交接

重要访谈/调查记录：身份和角色（可匿名但说明亲历范围）、机构规模、地区、访谈/观察时间、样本数、recruitment方式、相关recruitment/transaction volume、selection bias、incentive、代表性、异常案例可能性，以及提问/转写限制。不适用写明，不编业务量；Jimmy自己的亲历、转述和解释也分开。

当采购、switching、WTP或执行机制无法靠公开资料观察，**及时给Jimmy线下brief，不必等全部公开搜索结束**：问题/FCF影响、适合访问谁及覆盖差异、已有缺口、中性问题/需观察行为、支持/削弱/证伪的答案、招募/激励偏差、停止/再访条件。不设通用“访谈N人即通过”。

Jimmy决定现实资源和一线安排，Main准备和综合；没有联络授权不自行联系别人，计划不记为已完成。无法一线时，用合适proxy/类比说明能力边界或承认unknown，不靠假想访谈补confidence。

## 8. 多证据如何改变理解与判断

重要更新说明：原belief/替代解释 → 新观察及依赖 → 区分了什么解释 → 哪条经营机制/FCF金额、时间、持续性或可估计性改变 → belief/confidence变强、变弱或不变的具体原因 → 剩余未知/下一动作。

不同源但无关也不增加支持；可信反证可能比很多重复正面材料更重要。冲突先对齐样本、期间、分母、币种、合并范围、衡量对象与方法，不按名头投票，不无理由平均数字。正反同标准；无法解决的分歧保留。“没找到”不证明反命题，确认历史也不自动提高未来预测的信心，重复/中性材料可归档而不改判断。

Main自主更新evidence、company understanding和工作模型；分析后才形成初步thesis。实质改变核心thesis、估值判断、Pool、资本配置或正式结论交Jimmy决定。Material Evidence Under Review保留最后formal thesis，另列核实路径与current actionability；复核前不依旧结论自动建议新增资本，不自动卖出/改持仓，不增加第四种thesis状态。

Main负责规划、公开发现与综合；临时学术/竞争者/监管/行业任务只返回有边界报告。Evidence Auditor按关键争议、source dependency、样本、external validity、数据方法调用。Red Team仍独立，按D4默认触发和两阶段进行；审计或多个AI同意不替代它。

## 9. 缺证据、ability to learn与停止

理想数据缺失时，提出适合的proxy、alternative source、interview、survey、带前提的cross-company analogue，标明各自解决范围与剩余误差，或承认unknown。区分未找到、未披露、不可访问与客观不可知；摘要不冒充已读原件。工具/权限/付费限制需报告，但不说明现实问题永久不可知，也不默认把搜集工作全交Jimmy。

Research attractiveness同时看长期潜力/认知复利和**ability to learn**：关键证据可得、可验证、能降低决策相关不确定性，取得成本/时间合理。关键FCF driver长期不可观察/预测时降低研究优先，必要时Too Hard；贵的优秀公司若仍可学，依然可持续积累。不用潜在高收益或低质量资料填confidence。

进一步研究的信息价值用文字判断：哪些答案会改变决策？能否取得区分证据？值得花多少时间/资源？已充分回答、只会得到重复信息或关键结果目前不可知时，可结束本轮、进入资本讨论、等待节点、转线下或建议Too Hard；不是为了填报告继续搜。

## 10. Guards与验证

这些是方法边界，**尚不是代码拦截器**。与架构G1–G10并用，预期见[BE16–BE24](../evals/behavioral-eval-expectations.md)。

| Guard | 边界 | 主要测试 |
| --- | --- | --- |
| G11 Source count | 同源、共同数据/模型、循环引用不互证，独立性未知不默认独立 | BE16、BE20 |
| G12 Claim fit | “说过”不等于现实/未来成立，无通用来源排名，声誉不替代证据 | BE17、BE18、BE21 |
| G13 Transfer / sample | 严谨不等于可迁移，少数样本不直接外推，关键连接不跳过 | BE17、BE19、BE22 |
| G14 Provenance / access | 未读材料、AI摘要、未完成访谈、晚出信息不写已核事实 | BE18、BE21–BE23 |
| G15 Planning / learning | 问题→证据→来源；缺数据不降低标准，及时交线下；无具体缺口不无限研究 | BE22、BE23 |
| G16 Synthesis / state | 解释机制/FCF/confidence变化，不按计数投票；按D1/D3分正式状态与actionability | BE24、BE06、BE13 |

文件存在和链接通过不代表行为已验证。新预期与实际回答分档，不回改历史Kaspi回答来伪装当时已经主动找到了原始资料。
