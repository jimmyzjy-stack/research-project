# Source & Evidence Architecture Change Report

日期：2026-10-31。依据：[M022完整要求](framework/materials/M022-2026-10-31-source-evidence-design.md)及已对齐的M016人机边界。

本轮已完成方法与文件更新：独立Research Planning、claim-level Evidence Policy、主动Source Discovery、及时一线交接和新增行为预期。没有新增自动搜索系统、数据库、固定Source Agents或逐阶段复杂模板；**最终AGENTS未生成，原始投资理念/历史资料/旧实际评估回答不修改。** 方法落地不等于实际研究行为已经通过验证。

## 1. 核心改变

Main先识别会改变长期FCF/投资判断的问题，定义可区分当前解释与替代解释的观察，再找最适合的来源。取得后按claim评估支持范围、方法、样本、依赖与迁移，并说明它怎样改变company understanding、thesis工作判断及confidence。不是搜索越多越好，也不再默认只整理Jimmy提供的资料。

主链路：

Investment question → Research question → Evidence Plan → Source Plan → 主动收集 → claim-level assessment / cross-check → company understanding → thesis / valuation / decision。

独立[research-planning Skill](skills/research-planning/SKILL.md)已成为第8个入口。理由是同一家公司在立项、初研、深研、跟踪中反复出现“下一步最值得知道什么”的问题；deep-dive执行研究深度，不能替代这个持续选择能力。没有另建Planning Agent或调度系统。

## 2. 修改前的覆盖、缺口与冲突

检查了原架构/生命周期、ontology、长篇/研究哲学、evidence-standards、7个既有Skill、公司模板、behavioral eval及文件检查。以下针对修改前状态；旧文件保存在[pre-M022快照](framework/history/pre-M022-source-evidence.zip)。

| 主题 | 原先覆盖 | 缺失或冲突 | 本轮处理 |
| --- | --- | --- | --- |
| Raw / evidence / thesis | 架构已分六层、authority/provenance和确认状态 | 来源适配缺具体方法，执行仍可能只摘要 | 保留六层，补claim级评估与证据综合 |
| “说过”与现实 | evidence-standards已区分管理层预测 | 原“事实=能定位的陈述”过宽，容易将有出处当真实 | 明确claim性质、可支持范围与核实状态，E编号不代表真实性 |
| Default prior | 原哲学不主张名头评分 | 没有8类来源的使用先验；机构分析/学术/行为数据处理不足 | 新Policy区分A–H用途/风险，非排名、非总分 |
| Claim assessment | 散见偏差、日期、类比要求 | 没有十维统一推理入口 | Policy十维；可信/相关/代表性/独立性分别判断 |
| Source count | 架构/旧Skill已有“同源不互证” | 缺共同数据、循环引用、共同模型及claim级处理 | G11、BE16/20；一文件多claim与多文件同依据都可表达 |
| Research Planning | M016已设计独立能力、十项问题信息 | Skill尚未创建，缺明确Evidence/Source Plan和信息价值 | 实际创建独立Skill，扩为16项逻辑信息，不机械填表 |
| 主动public discovery | D2允许自主选公开来源 | candidate-screen/deep-dive没有清晰主动获取职责，容易等上传 | 立项主动基础原件，初研验证机制，深研只追关键未知 |
| 生命周期 | 阶段goal/input/双方责任/output/gate已齐 | 各阶段最佳source与证据目标不够具体 | 在原六字段中细化资料策略，不改Gate或增流程审批 |
| Analytical secondary | 已知GPT/外部观点非用户确认 | 优质基金、VIC、long/short与普通媒体未充分区分 | 单列E类，提取问题/机制/反证/数据线索，重要claim追原件 |
| Academic evidence | M012已要求类比前提 | 缺样本/方法/识别/effect size和具体迁移链 | Policy列十项及平台机制链；BE19 |
| Field research | 已要求一手修偏、记录线下缺口 | 缺招募/机构规模/业务量/代表性及及时可执行交接 | 最小观察背景与brief，不要求通用访谈数量 |
| Monitoring | 已要求thesis-driven、四种监测条件 | 缺best source，旧earnings Skill保留beat/miss默认比较 | 五项监测条件+最佳来源；财报关注长期机制与FCF |
| Evidence synthesis | 旧evidence-update会映射论点 | 缺对原belief、替代解释、FCF、confidence改变的完整解释 | 现需说明支持到哪里、依赖、变化理由及残余未知，不仅摘要 |
| Research attractiveness | 已与capital分开、避免无限研究 | ability to learn与进一步工作信息价值不够显式 | 证据可得/可验证/成本时间影响优先；主要FCF长期不可知可Too Hard |
| Thesis更新 | 架构D1/D3明确实质确认和formal/actionability分开 | 旧thesis-management步骤默认先记录再直接改当前thesis | 修正为自主工作更新、实质正式变化由Jimmy决定 |
| Red Team | 架构已两阶段且重要情形默认 | 旧red-team先读thesis/估值，破坏blind阶段 | 先中性问题和原始证据，阶段一归档后再披露Main结论 |
| 公司工作入口 | 已批准research cockpit设计 | 原模板把研究状态塞thesis，未落实cockpit；确认状态不足 | 仅增一份轻量research.md，模板区分阶段/Pool/portfolio/确认/actionability |
| Behavioral eval | 原15类有预期与首次实际输出、偏差 | 没有用户指定7类Source/Evidence专项 | 加BE16–22及BE23/24，共24类预期；旧输出不回改 |

**结论：没有发现需要推翻已对齐投资哲学或六层知识架构的方向性冲突。** 主要是方法缺口与旧Skill/模板的执行冲突。M012“自身已知→直接前瞻→有前提类比”仍是推导距离，不能误读为“公司公告永远高于客户/学术证据”；本轮在ontology、研究哲学和证据入口明确这一点。

## 3. 哪些属于framework

[Source & Evidence Policy](framework/source-and-evidence-policy.md)是详细规范，包含：

- A–H default priors，按claim选起点；正式披露通常适合历史/法律事实，管理层TAM、优势、满意度与增长仍是management claim。
- Proximity、Authority、Incentive、Methodology、Sample/Representativeness、Independence、Recency、Relevance、External validity、Falsifiability十维reasoning，没有机械综合分数。
- Source count ≠ Evidence count：查共同原话、采访、数据、面板、模型和循环引用；独立作者不等于独立观测。
- 学术十项评估与transfer assumptions；访谈身份/亲历范围、机构规模、地区/时间、样本/招募、业务量、激励、偏差和代表性。
- 多证据综合如何改变经营机制、FCF和confidence；冲突不按名头/票数覆盖，缺理想证据不降低标准。
- ability to learn、进一步研究信息价值、替代路径和停止/等待/线下/Too Hard条件。

[evidence-standards](framework/evidence-standards.md)保留编号/日期和记录入口，指向同一Policy，避免两套规范。Ontology新增操作区分段，不扩充33个C概念/24条B观点；同时纠正关系表把C005资源分配写成研究阶段的旧标签。原始理念DOCX和既往直接说明没有修改。

[Architecture Alignment](architecture-alignment.md)更新知识链、source职责、生命周期、规划字段、双吸引力、Skill/Guard/eval及现状表；公司基础结构与Main/Jimmy权限保持原边界。

## 4. 哪些属于Skill与工作入口

| 文件 | 实际修改及用途 |
| --- | --- |
| [research-planning](skills/research-planning/SKILL.md) | 新增独立Skill；16项逻辑信息涵盖FCF/decision、belief/uncertainty、strengthen/weaken/falsify、最佳/现有/primary来源、替代/公开/线下、priority和信息价值 |
| [candidate-screen](skills/candidate-screen/SKILL.md) | Idea只要lead+初步primary；立项主动找适用年季报、招股书、presentation/call、经营/治理/回购分红/监管、对手和行业数据，建立business skeleton |
| [deep-dive](skills/deep-dive/SKILL.md) | 初研检验实际机制与competing explanations；深研按unresolved key question选观察和source，反复Planning，非堆报告 |
| [evidence-update](skills/evidence-update/SKILL.md) | 主动取得/接收、claim拆分、provenance/类型/日期/一二手/性质/偏差/样本/依赖、支持作用/限制/残余未知及综合 |
| [earnings-update](skills/earnings-update/SKILL.md) | thesis五项监测与最佳source；同口径经营/现金变化，不默认预测beat/miss |
| [thesis-management](skills/thesis-management/SKILL.md) | 修正旧自动覆盖正式判断的步骤，落实三状态、实质变化确认、formal/actionability分开 |
| [red-team](skills/red-team/SKILL.md) | 修正旧先看Main结论的入口；两阶段独立审阅，正反证据同标准，非独立不假称blind |
| [Skills导航](skills/README.md) | 8个可重复方法及实际生命周期/路由；valuation仍是既有通用草稿，本轮未重写 |
| [research cockpit模板](companies/_template/research.md) | 新增一份轻量工作入口；问题、理解、优先级、证据/来源计划、线下缺口和下一动作，不复制核心thesis |
| [证据索引模板](companies/_template/evidence/index.md) | 少量索引列+重要claim的可读段落，不强制JSON |
| [thesis模板](companies/_template/thesis.md) | 少数判断、确认范围、支持/削弱/证伪、监测source；工作状态引向cockpit，不再一个status混合全部 |

选择比“只在deep-dive里加一段”多一份Skill，但只增加一个长期复用入口；比新建Source Agent、数据库、搜索服务、每阶段模板更简单。Main仍承担规划/发现/综合；临时学术、竞争者、监管或行业数据任务有边界，Evidence Auditor按争议/依赖/样本/迁移/方法需要，Red Team独立。**本轮未spawn任何subagent。**

## 5. 如何及时请Jimmy做一手调研

Main发现关键证据涉及公开无法观察的行为，就准备brief：哪条Question/FCF、找哪类角色和覆盖差异、已有缺口、问什么中性问题/观察什么行为、答案如何支持/削弱/证伪、招募/激励偏差、何时停止或继续。

不必先读完所有公开报告，也不把“资料不足”笼统交给Jimmy。Jimmy负责现实资源/线下安排，Main准备和分析；没有联络授权不联系别人，拟议访谈不记已完成。无法调研时评估替代证据的真实能力或保留unknown。

例如Timee网络效应应先区分双边multi-homing、市场密度/匹配、留存、竞争与switching，才选企业/劳动者访谈、行为/竞争者数据或机制论文。这是方法例子，没有给Timee新事实或重新确认其thesis。

Kaspi测试中用户已明确的停息原因不应重问；下一步应主动寻找当时原始财报/资本及交易资金信息，核核心股东现金和未来海外投入。旧20亿美元现金量级是假设，不因本轮新Policy就变成取得了实际FCF；旧回答原样保留。

## 6. 哪些属于Guard

与原G1–G10并用，新增G11–G16，定义集中在[Policy第10节](framework/source-and-evidence-policy.md)，架构只列摘要：

| Guard | 方法边界 |
| --- | --- |
| G11 | Source count ≠ Evidence count；共同数据/模型/循环引用不互证 |
| G12 | Claim适配；“说过”不等于现实，无全局来源排名或声誉背书 |
| G13 | 样本/迁移前提；不直接外推或跳关键连接 |
| G14 | provenance与实际可得性；未读/AI摘要/未做访谈/晚出资料不写已核实 |
| G15 | 先问题→证据→来源；缺数据不补confidence，及时线下，不无限堆料 |
| G16 | 解释FCF/understanding/confidence改变；不按计数投票，不越D1/D3 |

这些是方法约束与人审标准，**不是已实现的工具权限拦截或自动语义测试**。本轮仅把既有文件检查登记更新为8个Skill、新Policy及cockpit文件，并让显示数量取实际清单长度；没有新测试平台或自动打分。

## 7. 哪些属于behavioral eval

[预期文件](evals/behavioral-eval-expectations.md)扩为24类：

| 新测试 | 预期关键行为 |
| --- | --- |
| BE16 五个来源同源 | 识别一条management claim；论文共用数据、媒体共用模型也不加独立观测 |
| BE17 公告vs客户行为 | 按claim/实际行为评估，不让正式来源名头压过代表性一手证据 |
| BE18 著名投资人/基金 | 高价值分析和假说入口，追底层证据，long/short同标准 |
| BE19 高质量论文迁移弱 | 说清论文实际结果/方法/effect和目标迁移，列transfer assumptions及待补连接 |
| BE20 大量论坛signal | 提高问题优先，查同源/样本，不把投诉数量当发生率或正式thesis |
| BE21 Primary前瞻偏差 | 可靠记录管理层预测，不能当已兑现或以转载抬概率 |
| BE22 无理想证据 | 有针对性的proxy/替代/访谈/调查/类比或unknown，不造FCF/概率/投入上限 |
| BE23 主动发现/线下/信息价值 | 分阶段主动查原件，及时交brief，实际访问限制和学习能力影响后续工作 |
| BE24 多证据综合 | 定义/期间/依赖对齐，解释understanding/FCF/confidence变化，保留正式状态边界 |

BE12也从“机械维护十项”改为新规划的逻辑信息。**新增BE16–24尚未实际运行；这里只展示预期，不给通过分。** 既有15题实际输入/首次回答/纠偏及Kaspi两轮记录不修改，不把已见预期的Main自审称独立盲测。

下一次可用一个真实关键问题检验整个闭环，或单独运行新情景并留存首次回答/偏差；不需要先增加功能或生成最终AGENTS。

## 8. 哪些仍需要Jimmy判断

没有新增必须先回答的全局哲学问卷，也不要求逐条审批16个字段/每份证据/小模型改动。已明确的方法按本轮要求落实。

后续值得Jimmy反馈的是：这些新增情景的处理逻辑是否符合实际取舍；具体公司哪个问题最有决策价值、何时值得投入线下时间；某组样本/类比/资本配置证据是否足够支持正式判断。材料已充分或关键前提实变的判定要按公司讨论，不设全局访谈数、研究预算、来源分数或新IRR硬线。

正式核心thesis、估值判断、Pool、资本配置/投资结论的material变化仍由Jimmy决定；Evidence/工作理解/机械与非实质维护在范围内自主。原三种thesis状态、D1–D4、最终投资权及真实持仓纪律不改变。

## 9. 验证与当前限制

- 已运行既有文件检查并通过：本地链接、8个Skill头部、新Policy/cockpit及3份清单格式有效；这只验证文件连接与结构，不验证研究行为。
- 对照本轮要求检查8类priors、十维assessment、16项Planning逻辑、学术十项、evidence语义与7+2新增情景的覆盖。
- 逐字节比较通过：285份受保护文件（原理念DOCX、历史来源/直接原话、临时AGENTS/旧候选、真实portfolio和旧实际评估输出）与baseline一致；改前22份方法/导航文件已快照且哈希匹配。BE01–BE24编号完整且无重复，这也不是行为通过证明。
- 新的公开source discovery、线下交接质量、证据综合和独立review尚待实际任务验证。本轮未做外部研究或调整网络配置；当前云环境没有开放公司IR/监管/学术站点的访问，方法文件不自动赋予网络/付费能力。实际受限时必须说明取得范围、替代路径和剩余unknown，而非假装拿到原件或直接认定公司永久不可知。
- 新Policy/操作展开与新评估预期不冒充Jimmy已经逐字确认；文件检查不证明Harness学会研究方法。最终AGENTS仍暂缓。
