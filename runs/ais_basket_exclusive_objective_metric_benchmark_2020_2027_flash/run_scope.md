# 筛选范围：唯一客观指标提升 + 明确 Benchmark 表述

- 目标：从本地 AIS Basket 全文中筛出**以提升完全客观指标为唯一核心目标**、且**全文存在明确 benchmark 表述**的文章。
- 与既往设计的关系：沿用 `ais_basket_unified_strict_artifact_class_2020_2027_flash` 的客观指标模块与执行流水线；**去掉**软件制品与类级贡献两个模块（本轮不要求）；把核心目标从 `objective_improvement_primary` 收紧为 `exclusive_objective_improvement`（唯一）；新增 benchmark 表述模块（四门槛）。
- 判定单位：每篇完整本地全文一次独立 API 请求，不批处理、不切块。
- 模型：`deepseek-v4-flash`；temperature=0；max_tokens=40000（不担心输出截断）；response_format=json_object。
- 输入：`database_fulltext_all`（本地 11 刊扩展语料），年份：全部年代（1900–2100），13,910 篇；其中 2,475 篇（2020–2027）复用上一轮判定（同提示词，仅范围扩大）。
- 输出：`output_v1/decisions.jsonl`（可断点续跑）、`decisions.csv`、`summary.json`、`strict_matches.md`、`errors.jsonl`。
- 判定逻辑：`strict_include = objective_metric.pass AND benchmark.pass`；脚本对每个 gate/status/pass/strict_include 做严格一致性校验，不一致按错误记录并重试。
