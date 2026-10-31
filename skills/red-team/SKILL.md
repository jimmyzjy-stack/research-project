---
name: red-team
description: 按重要性默认触发独立两阶段审阅，寻找最强证伪路径、薄弱假设、未知与市场可能正确的原因，不为反对而反对。
---

# 独立反方审阅方法

读临时AGENTS、[架构D4及5.4](../../architecture-alignment.md)、[Source & Evidence Policy](../../framework/source-and-evidence-policy.md)。本Skill是方法，独立subagent是思考者；Main自我反驳不算独立审阅。

## 输入顺序

可能核心持仓、明显加仓、首次重要持仓、核心thesis重大改变或Jimmy/共同讨论很高conviction时，按D4默认运行；无需三位reviewer全跑。

1. Blind阶段只给中性核心research question、必要原始evidence、观察时点和资料限制；**此阶段不先读Main thesis、valuation、recommendation或conviction**，也不从标题/任务措辞泄露。查是否此前已接触结论；已接触不能口头“忘记”，应换未接触context或如实标non-blind。
2. 独立识别风险、未知、替代解释、反证观察及适合来源，先保存阶段一原始输出；不要求反方必然发现错误/红线。
3. Adversarial阶段再读Main thesis/valuation/recommendation，以Main会认可的方式复述，寻找最强falsification route、脆弱假设与市场可能正确的原因，同时保留成立部分。
4. 对正反证据都查共同来源/模型/数据、激励、样本、方法与external validity；short/contrarian thesis是高价值分析线索，重要claim仍需原件或独立验证。不给低质量负面传闻特别待遇。
5. 每个重要挑战写FCF/永久损失路径、已有支持范围、剩余未知、能够支持/驳回的观察及Source Plan；未知不伪装事实。
6. 返回独立报告，由Main原样归档后综合分歧；默认不直接改正式thesis/valuation/portfolio。实质变化交Jimmy，证据补充走evidence-update。Main综合不是投票。

若本轮没有实际独立context或工具权限，明示没有运行/仅检查方法，不能以自审声称通过blind review。Evidence Auditor按依赖/代表性/迁移/方法争议另调用，不替代反方思考。
