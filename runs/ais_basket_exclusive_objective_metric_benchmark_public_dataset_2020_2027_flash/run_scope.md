# 筛选范围：唯一客观指标提升 + 明确 Benchmark 表述 + 公开可获取数据集（2020–2027）

- 目标：从本地 AIS Basket 全文中筛出**以提升完全客观指标为唯一核心目标**、**全文存在明确 benchmark 表述**、且**评价基于公开可查到且可获取的数据集**的文章。
- 与既往设计的关系：沿用 `ais_basket_exclusive_objective_metric_benchmark_2020_2027_flash` 的客观指标与 benchmark 两模块及执行流水线；**新增 dataset 模块**（四门槛：全文可识别数据来源、公开可查到、公开可获取、支撑核心提升主张）。
- 判定单位：每篇完整本地全文一次独立 API 请求，不批处理、不切块。
- 模型：`deepseek-v4-flash`；temperature=0；max_tokens=40000；response_format=json_object。
- 并发：`max_concurrency=20`（config 与命令行一致）。
- 输入：`database_fulltext_all`（本地 11 刊扩展语料），年份 2020–2027，2,475 篇。
- 输出：`output_v1/decisions.jsonl`（可断点续跑）、`decisions.csv`、`summary.json`、`strict_matches.md`、`errors.jsonl`。
- 判定逻辑：`strict_include = objective_metric.pass AND benchmark.pass AND dataset.pass`；脚本对每个 gate/status/pass/strict_include 做严格一致性校验，不一致按错误记录并重试。
- 提示词变更：系统提示词在旧两模块基础上新增“四、公开可查到且可获取的数据集”模块，更新输出 schema、允许状态、校准边界与排除码。