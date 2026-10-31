# 研究检查

评估分成两层：自动检查文件能否正确连接、数据能否读取；人工检查是否充分理解用户观点、研究是否可靠及判断过程是否保留。第二层需要助手审阅和你自己的判断，不能用通用模板证明已经理解用户的投资方法。

## Behavioral eval：预期、实际回答与偏差分开

[本轮29类情景预期](behavioral-eval-expectations.md)保留原24类，M023新增BE25–29立项、主动生成/三轴循环与历史/独立边界。M022的BE16–24仍未逐题实际运行，不能把M023历史回放当整套测试通过。真实材料锚与追加假设分别说明，缺持仓/结果不编成历史事实。边界与拟议Guards见[架构报告](../architecture-alignment.md)。

已进行[2026-10-31 Main人工试运行](runs/2026-10-31-main-behavioral-eval.md)，留存[完整输入/首次回答](runs/2026-10-31-main-responses.md)和[偏差后定向复核](runs/2026-10-31-targeted-recheck.md)。Main已见预期，评分为自审，不能当独立评估。首次两处偏差没有回改：未指明缺口却给normal value追加研究、从持有背景推定有确认记录。Red Team真实隔离、工具权限与跨轮状态维护尚未运行验证；不宣布整套Harness通过，最终AGENTS仍暂缓。

下列文件检查不验证这些行为，旧Timee人工纠错样例和本轮自审也不能代替真实独立执行或Jimmy对关键结果的判断。

随后开始[Kaspi 2025年收购/停息的实际Main研究测试](runs/2026-10-31-kaspi-2025-main.md)，保存[M020原始输入](../framework/materials/M020-2026-10-31-kaspi-2025-test.md)、首次回答、时点/资料边界及动态Planning工作记录。尚未外核当时公告/价格，也未运行独立Red Team；本轮不自动判定通过或提升为全局规则，后续反馈追加保留。

接续[M021澄清与价格/现金追问](../framework/materials/M021-2026-10-31-kaspi-price-and-funding.md)，保存[续轮实际分析与试算](runs/2026-10-31-kaspi-2025-capital-followup.md)。停息原因按给定事实移出优先未知；使用10月立项市值/PE样本做盈利倒算和明确假设的资金消耗敏感性，不将试算当实际FCF、情景概率或IRR。原始报价/现金与投入边界仍需核查，首轮回答不回改。

M022方法与Guard映射见[Source & Evidence变更报告](../source-and-evidence-architecture-change-report.md)和[Policy](../framework/source-and-evidence-policy.md)。旧实际回答不回改；文件检查仅补第8个Skill、Policy及cockpit存在性，不会验证Source count、迁移或研究质量。

## 两项核心能力：立项与历史问题生成

[历史能力协议](historical-question-generation.md)与原情景评估并列：不给后来问题/结论，先业务/value-driver map，生成有序5–10题及FCF/证据/阶段/下一时间动作，再对历史crux而非关键词。真实资料可用性、fresh-context输入边界、首次输出和[本轮比较](runs/2026-10-31-initiation-question-generation-review.md)单独留存；Root已知后续资料的Main对照不算盲测。没有reference的公司不伪造历史题目或新发现，重复问题不增加事实confidence。

## 文件与人工研究检查

你可以说：“请检查整个研究工作区，并分别报告文件问题、研究缺口和判断不一致的地方。”助手在仓库根目录执行：

```bash
python3 evals/check_workspace.py
```

这条命令无需安装依赖。它检查三份 JSON 的格式、日期、公司引用、已知仓位比例，必需模板与 Skill，以及 Markdown 的本地文件链接。失败会列出文件和原因，退出码为 1；通过为 0。它不访问外部网页，不检查数字真假，不验证证据编号语义、投资结论或收益率计算。

随后按任务使用[框架理解](framework-fidelity.md)、[研究质量](research-quality.md)与[判断一致性](decision-consistency.md)。每项记录“通过／缺口／不适用”与具体依据，不用总分掩盖关键缺口。空工作区可以通过文件检查，但没有真实研究可评估；不得因此称研究已经合格、哲学已稳定或用户已确认。

复盘特别重要或判断发生重大变化时，可将结果附在该公司的更新记录中。不为了填写检查表反复生成没有用途的文件。

## M024：从公开资料开始的GMO-PG立项测试

[本轮资料计划与访问记录](runs/2026-10-31-gmo-initiation-source-plan.md)保留未看公司原件前的工作假设、driver map、候选问题与Source Plan。官方IR访问被云代理403拒绝，已保存必要域名配置草稿但未证明生效；尚未取得财报/报价、未完成立项，不算Source Discovery通过，也不判公司Too Hard。网络恢复后继续同一任务，原计划留作方法评估，不回写成已核事实。

## 携程中国酒店业务：5–10年护城河问题生成

用户随后要求先尝试另一问题，见[Main实际问题输出及证据计划](runs/2026-11-01-ctrip-china-hotel-moat/README.md)。保存检索前工作稿、两份官方年报及同源提取文本，区分已有用户讨论提示、定向核查后重排、当前未验证机制和下一研究动作。本轮不是完整立项、历史盲测或正式投资判断；用户反馈尚未收到，不宣布测试通过。新增导航前版本保留于[快照](../framework/history/pre-ctrip-moat-eval-navigation-2026-11-01.zip)。
