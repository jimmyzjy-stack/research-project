# 个人长期投资研究工作区

这里保存你如何理解一家公司、为什么关注或持有它，以及哪些新证据会改变判断。你用自然语言提出任务，Codex/GPT 帮你研究、整理文件和检查一致性；投资决定由你作出。

## 第一次使用

整体架构方向已获基本认可。当前M023重点是两项能力：高质量立项，以及在你未提示前主动发现关键研究问题。见[变更与测试报告](initiation-and-question-generation-change-report.md)、[方法](framework/initiation-and-question-generation.md)和[历史回放评估](evals/historical-question-generation.md)。Research Planning已独立，现强化value-driver map、三轴排序及循环重排；仍是8个Skill。[Source Policy](framework/source-and-evidence-policy.md)、[Architecture Alignment](architecture-alignment.md)及原始理念继续适用。首次输出与参考/纠偏分开；有限回放不能证明长期稳定。最终AGENTS继续暂缓，真实持仓和正式公司状态未因测试改变。

你可以直接提供零散想法、长篇材料、投资人的观点与自己的解释，或真实研究案例，不必先整理。比如：

> 以下是我对【主题】的原始想法。请先完整理解，保留理由与限定条件，更新长篇框架和 ontology；将你的解释与我的原话分开，不急着提炼短原则。

真实案例可以保存在[casebook](casebook/README.md)：保留当时信息、如何判断、替代选择与后来结果，再提取有条件的思维规则，不只记录公司结论。

已保存M003完整理念、M004至M008/M010直接补充，以及M012/M013框架反馈，见[框架导航](framework/README.md)。[M016最新架构反馈](framework/materials/M016-2026-10-31-architecture-feedback.md)明确动态规划、研究/资本吸引力分开、实质性变化确认与默认两阶段Red Team；先实际评估再决定最终AGENTS内容。真实持仓未录入，后续公司研究任务可说：

> 请用 candidate-screen 初筛【公司名称及交易所/代码】，按已经明确的观点开展研究；不清楚我如何取舍的地方先保留问题，不套用默认投资风格。

Timee先收到GPT辅助稿，随后两份拆包47份原件成功接收，见[CASE002](casebook/CASE002-timee-research-process.md)、[文件索引与阅读范围](framework/materials/M010/source-index.md)及[核对记录](casebook/CASE002-timee-source-audit.md)。原件技术提取与事实核验分别记录，原聊天可按关键转折继续补充，历史项目不混成当前估值。

新增[茅台](casebook/CASE003-moutai-demand-and-pricing.md)与[Kaspi](casebook/CASE004-kaspi-initiation-and-moat.md)历史研究，已有[两家公司立项模块对照](casebook/M017-initiation-module-reference.md)。[M018三份茅台拆包](framework/materials/M018/source-index.md)已成功接收25份原件，补齐此前传输缺口；[原件核对](casebook/CASE003-M018-source-review.md)更新独立研究计划、长期需求/提价证据与模型版本边界。旧GPT聊天仍是重建，历史材料不当作当前thesis、持仓或已通过的blind eval。

[M019新增资料](framework/materials/M019/source-index.md)包括[标普全球立项](casebook/CASE005-spglobal-initiation.md)、[福寿园立项/更新与Pass](casebook/CASE006-fushouyuan-pricing-policy-pass.md)。Jimmy明确福寿园历史Pass因提价thesis与公益政策增长约束；治理独立记风险，后续事件不改写当时归因。三个原件保留，进一步提炼[模块/退出检验参考](casebook/M019-initiation-and-research-exit.md)，不自动形成当前投资状态。

这些是本仓库的研究流程。Codex 按 [AGENTS.md](AGENTS.md) 的指引读取对应的 `skills/<名称>/SKILL.md`；它们不需要额外安装插件。新对话请先让助手阅读 AGENTS.md。如果无法获取资料，助手必须说明哪些结论还没有核实。

## 文件放在哪里

| 位置 | 保存什么 | 从哪里开始 |
| --- | --- | --- |
| `AGENTS.md` | 当前的临时整理约定与导航；尚非最终投资原则 | [临时约定](AGENTS.md) |
| `architecture-alignment.md` | 知识层、研究生命周期、人机边界、设计确认点 | [最新架构报告](architecture-alignment.md) |
| `framework/` | 长篇哲学、原始材料、张力与问题，以及主题参考 | [框架导航](framework/README.md) |
| `investment-ontology.md` | 你的概念含义、区分与关系 | [概念与关系](investment-ontology.md) |
| `casebook/` | 真实判断过程和可泛化的思维规则 | [案例说明](casebook/README.md) |
| `portfolio/` | 当前持仓、观察名单、候选箱 | [清单说明](portfolio/README.md) |
| `companies/` | 每家公司的 thesis、估值、更新、证据 | [公司文件说明](companies/README.md) |
| `skills/` | 当前七份草稿；设计将research-planning独立为第八个Skill | [流程导航](skills/README.md) |
| `scripts/` | 以后确实需要的计算工具 | [计算工具说明](scripts/README.md) |
| `evals/` | 15类行为预期、首轮实际回答/偏差/复核，以及文件与人工检查 | [检查说明](evals/README.md) |

## 为什么这样选

- **Markdown**：普通文字就能读写，公司研究和流程不需要专用软件。
- **JSON**：三份清单有固定字段，便于检查和以后计算。相比 YAML，Python 自带工具就能读取 JSON；你可以让助手代为修改，无需学习语法。
- **Python 标准库**：现在只有一个文件检查工具，没有第三方依赖。等真实估值需要计算时，再添加小脚本。
- **Git/GitHub**：保存每次有意义的研究变化。一个公司一个目录即可；第一阶段无需网页、数据库、行情订阅或自动化服务。

## 日常研究与版本记录

1. 给助手公司身份、研究问题和你已有的材料。
2. 让助手按相应 Skill 工作，并先列出可核实的证据。
3. 阅读结论、反对意见和待解决问题；缺资料时允许暂缓判断。
4. thesis 的重大变化写入公司 `updates/`，保留旧判断、触发证据和新判断。
5. 让助手检查文件与研究质量，展示这次改动。需要保存到 GitHub 时，可明确说：“请把这次变化提交到 main 并推送到 GitHub。”一次提交对应一个有意义的变化，提交说明可用中文。

Git 保存历史需要实际提交；只有修改文件不会形成提交记录。GitHub 中的文件由仓库权限控制，录入个人持仓前请确认仓库可见性符合你的意愿。

你无需启动任何服务，也无需配置 API 密钥。助手可在仓库根目录运行 `python3 evals/check_workspace.py` 检查文件，但通过检查不等于研究正确，更不等于值得投资。
