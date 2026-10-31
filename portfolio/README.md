# 组合与研究清单

这三份 JSON 记录当前状态，Git 与公司更新记录保存变化过程。初始列表为空，不代表你实际没有持仓，只表示尚未录入。

| 文件 | 用途 | 列表字段 |
| --- | --- | --- |
| [holdings.json](holdings.json) | 用户确认的实际持仓 | `positions` |
| [watchlist.json](watchlist.json) | 已研究、值得持续观察的公司 | `companies` |
| [candidate-box.json](candidate-box.json) | 等待初筛或继续研究的线索 | `companies` |

你可以说：“请把这家公司加入候选箱，注明研究问题和下一步。”或“这是我截至某日的持仓，请更新清单，并把不确定的比例留空。”助手负责检查 JSON 格式，不需要你手动编辑。

## 字段约定

- `as_of`：这份清单最后一次核实或更新的日期，格式 `YYYY-MM-DD`；初始空清单可用 `null`。
- `company_id`：对应 `companies/` 下的目录名，不能使用 `_template`；同一份清单内不重复。
- `name`：公司名称；交易所、证券代码、股份类别等身份信息写在公司 thesis。
- `weight_pct`：持仓占总投资组合市值的百分比，范围 0–100；未知用 `null`，不能填零冒充已知。已知比例之和不能超过 100%；未列出的比例含义未知。
- `notes`：持仓的补充口径或备注，未知可为空字符串。
- `reason`：进入观察名单的理由；`next_review` 是下次复查日期，可为 `null`。
- `research_question`、`next_step`：候选箱的核心问题与下一步。

以下仅展示单条记录的格式，**不是实际持仓或投资建议**；实际使用前应先建立对应公司目录。

持仓条目：

```json
{
  "company_id": "exchange-ticker",
  "name": "公司名称",
  "weight_pct": null,
  "notes": "尚未确认仓位比例"
}
```

观察名单条目：

```json
{
  "company_id": "exchange-ticker",
  "name": "公司名称",
  "reason": "需要观察的业务变量或估值条件",
  "next_review": null
}
```

候选箱条目：

```json
{
  "company_id": "exchange-ticker",
  "name": "公司名称",
  "research_question": "需要首先回答的问题",
  "next_step": "需要获取的材料或开展的分析"
}
```

各清单可以交叉出现同一家公司，例如持有的公司也在观察名单中；不要误当成重复仓位。完成初筛后决定是否移出候选箱，并记录理由。进入观察名单不代表准备买入；研究完成也不自动改变实际持仓。
