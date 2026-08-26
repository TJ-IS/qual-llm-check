# 筛选范围：安全相关 + 算法开发（AIS Basket 全库）— v2 提示词

- 目标：从本地 AIS Basket 全文中筛出研究问题属于安全领域、且核心贡献为算法开发的文献。
- 与既往设计的关系：沿用 exclusive_objective_metric_benchmark 轮的全文逐篇裁决管道；判定模块替换为安全相关性与算法开发两个门槛；新增数据公开性记录字段（不参与纳入）。
- 安全定义（v2 收紧）：只接受「信息系统安全」意义上的安全——恶意或对抗行为者直接针对信息系统、其用户或其数据的攻击、操纵或滥用（入侵、恶意代码、钓鱼、对抗样本、提示注入、内容操纵、隐私披露攻击、未授权访问等），损害系统/用户/组织的安全属性（机密性、完整性、可用性、真实性）；或研究核心是此类威胁的检测、防御、缓解与评估。
- v2 明确排除（1.3）：传统犯罪预防与执法优化（犯罪预测、警力优化、犯罪事件关联、嫌疑人识别、身份匹配、边境车辆筛查）；金融市场监管/内幕交易监视；会计与审计欺诈（无网络攻击成分）；一般评论质量/有用性/垃圾评论分类（除非恶意操纵检测是核心）；一般信任与信誉计算（除非对抗性操纵检测是核心）；主观隐私感知研究；数据质量/清洗。
- 算法开发定义：核心贡献是提出新方法或实质性方法改进并实证评估；v2 增加排除：仅方案描述+可行性原型测试（如加密/访问控制方案），无新计算方法与基准比较。
- 数据公开性：public、private_or_nonpublic、mixed、unclear 四态，仅记录，供后续挑选公开数据研究使用。
- 判定单位：每篇完整本地全文一次独立 API 请求，不批处理、不切块。
- 模型：deepseek-v4-flash；temperature=0；不设 max_tokens（输出不限制）；response_format=json_object。
- 并发：100（config batch.max_concurrency）。
- 输入：database_fulltext_all（本地 11 刊扩展语料），年份：全部年代（1900-2100），13,910 篇。
- 输出：output_v1/decisions.jsonl（可断点续跑）、decisions.csv、summary.json、strict_matches.md、errors.jsonl。
- 判定逻辑：strict_include = security_relevance.pass AND algorithm_development.pass；脚本对每个 gate/status/pass/strict_include 做严格一致性校验，不一致按错误记录并重试。
- v2 变更记录：2026-08-23 收紧安全边界（排除执法/市场监视/审计欺诈/评论质量/信誉计算），算法开发增加方案类排除；提示词指纹变化，全量重跑。
