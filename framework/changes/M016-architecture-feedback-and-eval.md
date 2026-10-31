# M016：架构十项反馈、15类预期与首轮Main试运行

日期：2026-10-31（Asia/Shanghai）。[用户原文](../materials/M016-2026-10-31-architecture-feedback.md)完整保留；[架构报告](../../architecture-alignment.md)与[behavioral预期](../../evals/behavioral-eval-expectations.md)按其范围修订。改前7份文档保存于[快照](../history/pre-M016-architecture-and-evals.zip)。

## 本轮采用的直接反馈

1. Research Planning可反复调用，维护用户指定十项问题信息；判断值得独立成为第8个Skill，暂不创建Skill代码或常驻Agent。
2. Company cockpit和candidate comparison显式分research/capital attractiveness，不用总分或公司类型代替。
3. D1改material / decision-relevant change confirmation；自主更新证据、工作模型、机械与非实质修正，判断影响/累计变化可能实质时才正式确认。
4. D2按已确认问题/范围高自主，范围/关键前提实质变化再讨论。
5. D3标Material Evidence Under Review，保留最后formal thesis，把新增资本actionability单独限制；未核实不自动改thesis、卖出或持仓。
6. D4用户指定的重要/高conviction情形默认Red Team，尽量先blind后adversarial；审计/估值review按需，未隔离不自称blind。
7. Research.md定位轻量cockpit，维护用户指定十项研究状态；少数thesis不重复。
8. Thesis-driven monitoring，以支持、削弱、证伪和监测路径为入口；新闻等是输入。
9. BE09–11对应用户新增三题；BE12–15为助手基于上述边界增加的操作测试，不伪称用户逐条确认了这些细节。
10. Research stage、A/B/C/D pool、portfolio status分开，保留A=持有并跟踪的联系，不从一个字段推断其他事实/确认。

## 实际评估与偏差

[首轮报告](../../evals/runs/2026-10-31-main-behavioral-eval.md)关联15组实际输入/Main首次回答及定向复核。首次输出保留，没有为评分回改；发现E1无具体缺口仍追加研究任务、E2从已持有背景补出确认记录。后者也揭示BE15预期默认条件未在实际输入给出，已补边界并重答反向变体。

Main已读预期且自行审阅，故只称人工情景试运行，不是隔离盲测、独立评估或可靠性通过。未运行独立subagent、未验证执行权限和跨轮公司状态。文件检查只验证结构/链接，不验证投资理念。

## 范围与历史

导航、材料登记与open-questions同步当前阶段；D1–D4不再重复追问。原投资理念DOCX、旧材料、长篇框架、ontology、公司/组合、现有7个Skills、脚本与实际AGENTS/候选均未修改。没有创建真实公司cockpit、数据库、网页、模型库或逐阶段模板，没有提交/推送Git。

后续先核对实际偏差与未验证边界，再由Jimmy决定AGENTS应纳入的纪律；本轮明确不生成最终AGENTS。
