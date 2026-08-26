# 筛选范围：安全相关 + 算法开发（AIS Basket 全库）

- 目标：从本地 AIS Basket 全文中筛出研究问题属于安全领域、且核心贡献为算法开发的文献。
- 与既往设计的关系：沿用 exclusive_objective_metric_benchmark 轮的全文逐篇裁决管道；判定模块替换为安全相关性与算法开发两个门槛；新增数据公开性记录字段（不参与纳入）。
- 安全定义：存在恶意或对抗行为者，通过攻击、操纵或滥用信息系统、其用户或其所依赖的数据，对系统、用户或组织造成安全损害，或文章针对此类威胁进行检测、防御与缓解。通过与排除清单均为示例，非穷尽。
- 算法开发定义：核心贡献是提出新方法或实质性方法改进并实证评估，排除纯理论、纯行为实证、综述与仅将现成算法作工具的研究。
- 数据公开性：public、private_or_nonpublic、mixed、unclear 四态，仅记录，供后续挑选公开数据研究使用。
- 判定单位：每篇完整本地全文一次独立 API 请求，不批处理、不切块。
- 模型：deepseek-v4-flash；temperature=0；不设 max_tokens（输出不限制）；response_format=json_object。
- 并发：100（config batch.max_concurrency）。
- 输入：database_fulltext_all（本地 11 刊扩展语料），年份：全部年代（1900-2100），13,910 篇。
- 输出：output_v1/decisions.jsonl（可断点续跑）、decisions.csv、summary.json、strict_matches.md、errors.jsonl。
- 判定逻辑：strict_include = security_relevance.pass AND algorithm_development.pass；脚本对每个 gate/status/pass/strict_include 做严格一致性校验，不一致按错误记录并重试。

