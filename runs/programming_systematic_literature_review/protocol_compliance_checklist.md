# 协议执行状态

| 要求 | 来源依据 | 状态 | 证据/待办 |
|---|---|---|---|
| 冻结检索日期、字段、检索式、来源与初始数 | Cram et al. 2019 (MISQ) | 完成 | 2026-07-26；TITLE-ABS-KEY；4,981 条 |
| 一条稳定概念式与预选跨学科来源 | Diederich et al. 2022 (JAIS) | 完成 | `search_protocol_v2.md`、`source_scope_rationale.md` |
| 正向施引扩展 | Cram et al. 2019；Eisend 2019；Larsen et al. 2019 | 完成 | 20 篇种子，807 条 Scopus 施引 |
| 本地种子召回审计 | 检索完整性检查 | 完成 | 28/28 合并渠道找回 |
| 去重并保留检索渠道 | PRISMA 式流量 | 完成 | 5,816 条原始输入 → 5,642 条唯一题录 |
| 预设 eligibility criteria | 四篇实证综述 | 完成 | `search_protocol_v2.md`、提示词与校准报告 |
| 第一轮题录筛选 | corpus construction | 运行中 | DeepSeek V4 Pro，批量完整性校验、可续跑 |
| 第二次独立题录判断 | Eisend；Qahri-Saremi & Montazemi | 待第一轮完成 | 第一轮标签和理由对第二轮盲化 |
| 冲突项共识/人工裁决 | Qahri-Saremi & Montazemi 2019 | 待执行 | 不把模型当作两名人类编码者 |
| 候选全文复核与概念矩阵 | Diederich et al. 2022 | 已实现脚本，待执行 | 本地全文先跑；缺失全文单列 |
| 参考文献回溯 | Cram；Eisend；Diederich；Larsen | 待最终全文候选 | 新增记录重新走相同流程 |
| 论文数与独立研究/样本数分开 | Eisend；Qahri-Saremi & Montazemi | 待全文编码 | 复用样本不重复计入实证设置 |
| 阶段流量与排除理由 | Qahri-Saremi & Montazemi 2019 | 部分完成 | 题录流量已保存；最终 PRISMA 待全文完成 |
| 投稿前更新检索 | Cram；Diederich | 待最终写作 | 记录新增文献和更新时间 |

在“参考文献回溯、缺失全文处理和最终裁决”完成前，本项目不得被描述为已经完成的穷尽性全球 SLR。
