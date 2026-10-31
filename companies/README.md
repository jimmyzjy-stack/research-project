# 一家公司一个研究目录

当前只有[_template](_template/research.md)，没有真实公司正式研究档案。历史案例与评估不自动变成当前thesis或真实持仓。

真实公司研究需要档案时复制_template为companies/<company_id>/：

```text
research.md         cockpit：阶段、理解、优先问题、Evidence/Source Plan和下一动作
thesis.md           少数初步/已确认判断及确认范围
valuation.md        工作/正式估值的输入、假设、计算及状态
evidence/index.md   claim、原件定位、支持范围、依赖与限制
updates/            变化、独立报告、Jimmy实质决定的历史
```

company_id用稳定小写英文/数字/短横线，通常为交易所-代码。确认证券/股份类别、经营地和币种，避免同名/ADS口径混淆；多证券先在同目录说明，无需数据库。

M022新增一份轻量research.md，承接反复[research-planning](../skills/research-planning/SKILL.md)，不是逐阶段报告模板。问题只维护一处，详细分析链接证据；thesis、估值、实际portfolio仍各自是当前状态入口，cockpit只引用。

Main按[Source Policy](../framework/source-and-evidence-policy.md)主动找适合的公开原件，不把模板当等Jimmy填写资料的问卷。未知明示，不为完整编数字、观点、确认或持仓；空文件不证明研究完成。

实质性正式判断/Pool/资本变化交Jimmy确认，非实质维护自主；updates保留旧判断与原因。实际持仓只据真实事实，建议/已确认thesis不等于成交。临时subagent默认只报告，不改正式状态。文件修改也不等于已有Git提交。
