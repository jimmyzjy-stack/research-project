# Harness 首次 Git 持久化说明

本文件只记录版本持久化范围，不新增或修改投资理念、研究判断、估值、公司/组合状态或行为评估结论。

目标仓库：`jimmyzjy-stack/research-project`；分支：`main`。操作前确认本地尚无提交、Git未跟踪任何文件；远端Git查询成功但无HEAD/main引用，GitHub元数据返回仓库为public、默认分支main、size为0。原有成果此前仅存在于旧task工作区，保存环境配置不等于提交到GitHub。

## 纳入范围

本次纳入147份既有文件，另外新增本说明与[persistence-manifest.json](persistence-manifest.json)两个纯版本记录文件。manifest记录既有纳入文件的逐文件SHA-256，便于核对未改写原文。

- framework中的长篇框架、主题文件、open questions、变更记录、用户直接说明的Markdown、Source & Evidence Policy、立项/主动问题生成方法等。
- investment-ontology.md；两版用户自写原始投资理念DOCX，按已有版本和路径原样保存，不用解释文本替代原件。
- architecture-alignment.md、source-and-evidence-architecture-change-report.md、initiation-and-question-generation-change-report.md及既有README。
- 全部8个Skill及skills导航。
- evals中的behavioral expectations、历史问题生成协议、输入说明、实际首次输出、纠偏、自审、GMO source plan/网络复核，以及携程护城河问题生成记录。
- casebook中的案例分析、方法/来源审阅与已有结构化归纳；companies模板、portfolio现有3份JSON及说明、scripts说明。
- 既有临时AGENTS.md与未激活的AGENTS.candidate.md原样保存。本次没有生成最终AGENTS.md，也没有改变候选稿状态。

## 未公开上传的范围

GitHub仓库当前为公开仓库。现有原件包中实际包含具名访谈、客户项目交付物，以及保密/版权标记；因此不把这些材料、全文提取件、附件副本或可能打包它们的历史ZIP提交到公开仓库。

279份现有文件留在旧task工作区：framework/history中的21份ZIP；framework/materials下M009/M010/M011/M017/M018/M019原件/对话/提取/清单目录；3份Golden Case原DOCX副本；携程测试中2份第三方年报PDF及2份同源TXT。按资料包整体排除不代表每一份文件都被判定具有法律限制，也不改变其来源地位或研究结论。

未公开文件的详细路径清单留在本地，未把具名访谈文件名再次写入公开清单。`.git`和环境凭据、task外附件/工作区备份不属于提交范围；本次纳入文件的密钥样式扫描没有发现命中。

## 新任务读取边界

新任务拉取main后可以读取上述正式成果。已启动的任务不会因本次push自动刷新，应先保存自身改动并同步远端。

历史材料索引与分析中的原始出处链接保持原样，其中被排除的原件、提取件和ZIP在公开checkout中不可用；不能因此假装已重新阅读或核实。部分完整历史回放需要用户另行提供这些资料。原有严格文件检查在原工作区通过；在不含这些原件的公开checkout中，可能报告原文/快照链接缺失，不能将其称为全量历史研究复现通过。

需要完整来源包时，应使用用户保留的备份或另行确认的非公开存储。此次未改变GitHub仓库可见性、未修改原有检查代码来掩盖缺失，也未改写原文链接。

本文件描述持久化范围，不单独证明push成功；实际提交hash和远端main核验结果在本次任务交付中报告。
