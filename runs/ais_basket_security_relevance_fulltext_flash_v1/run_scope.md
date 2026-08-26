# 筛选范围：攻防安全相关性（AIS Basket 全库，不限研究类型）

- 目标：从本地 AIS Basket 全文中筛出**研究核心属于攻防安全**的文献——恶意/对抗行为者针对信息系统、其用户或数据的攻击、操纵、滥用，或此类威胁的检测、防御、缓解、评估与建模。
- 与 99 篇筛选的关系：v2（`ais_basket_security_algorithm_development_flash_v2`）要求"安全相关 + 算法开发"双门槛；本运行**去掉算法开发门槛**，只判安全相关性（综述/行为/组织/实证均可纳入），作为 SLR 检索式（`security_fulltext_search_query.md` M1 元数据检索 2,499 条）的全库金标准对照。
- 安全边界：与 `security_fulltext_search_query.md` 第 1 节完全一致（三要素 + 纳入类型清单 + 排除清单 + 决策树），提示词由该节改写。
- 排除类型（v1 明确）：执法优化、纯金融欺诈、评论质量、信誉计算、隐私主观感知、数据质量、一般优化/鲁棒性、纯方案无攻击建模、组织治理、泛化公共安全。
- 判定单位：每篇完整本地全文一次独立 API 请求，不批处理、不切块。
- 模型：deepseek-v4-flash；temperature=0；response_format=json_object；不设 max_tokens。
- 并发：100（config batch.max_concurrency）。
- 输入：database_fulltext_all（本地 11 刊扩展语料），年份全部（1900-2100），13,910 篇 md。
- 输出：output_v1/decisions.jsonl（可断点续跑）、decisions.csv、summary.json、security_matches.md、errors.jsonl。
- 判定逻辑：security_include = security_relevance.pass（四 gates 全 true 且 status=core_security_attack_defense）；脚本对 gate/pass/status/security_include 做严格一致性校验，不一致按错误重试。
- 与检索式对照（跑完后）：金标准（本运行通过集）vs M1 元数据 2,499 / F2 head-8000 4,896 / F3 全文 10,093，计算召回与精度，输出审计文档。
