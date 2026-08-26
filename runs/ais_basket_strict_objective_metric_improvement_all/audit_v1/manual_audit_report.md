# Manual stratified audit report

## Outcome

- Fixed sample: 30 articles (seed `20260806`; sampled after 8365 decisions were available)
- Model inclusions audited: 18; confirmed: 18; false positives: 0
- Model exclusions audited: 12; confirmed: 10; false negatives: 2
- Raw agreement: 28/30 (93.3%)
- Important: this is a deliberately stratified boundary audit, not a prevalence sample. Do not extrapolate its rates to the corpus.

## Corrections

### Sensing the Future: A Design Framework for Context-Aware Predictive Systems

- Model -> manual: `False` -> `True`
- Error type: `false_negative_overstrict_centrality`
- Reason: 改判纳入。CAPS 不只是抽象框架：作者按该框架连续构建 context-aware predictive artifacts，以 Croston 为显式基线，用 forecasting-error cost 证明 phase-out 版本改善 4%、sensor activity 版本改善 20%。全文把框架归为 DSR improvement contribution，客观改进是评价其能否产生更好制品的主导证据；专家/情境反思用于迭代和边界说明，不是并列的主观成功指标。

### Using “last-minute” sales for vertical differentiation on the Internet

- Model -> manual: `False` -> `True`
- Error type: `false_negative_overstrict_solution_boundary`
- Reason: 改判纳入。文章给出可实施的在线随机 last-minute sales 定价/供给决策规则，解析求解不同参数下的最优策略，并把利润同确定性销售及其他策略类别直接比较。提示词明确允许 prescriptive model、decision rule 和 digital policy，因此不应仅因它不是软件界面而判 Gate 1 失败。

## Boundary interpretation

The inclusion sample showed no obvious false positive in this audit. The two observed disagreements were both conservative exclusions:

1. A DSR process/framework paper can still be objective-improvement dominant when the framework is evaluated by building multiple artifacts and the central evidence is benchmark improvement. Qualitative reflection used to refine the framework does not automatically make the success criteria mixed.
2. A formal e-commerce policy can satisfy purposeful solution design when it yields a concrete, implementable decision rule and objective comparison. Requiring a graphical interface or deployed software would contradict the prompt's explicit allowance for prescriptive models and digital policies.

## Article-level judgments

### 01. Integrating rich and heterogeneous information to design a ranking system for multiple products

- Group: `retained_layer:algorithm_or_computational_method`
- Outcome: `confirmed_inclusion`
- Model/manual decision: `True` / `True`
- Manual reason: 确认纳入。全文提出多源 eWOM 排名算法及原型，以相对多种基线和消融版本的 Spearman 排名相关改进作为核心成功证据。

### 02. Content-based object organization for efficient image retrieval in image databases

- Group: `retained_layer:algorithm_or_computational_method`
- Outcome: `confirmed_inclusion`
- Model/manual decision: `True` / `True`
- Manual reason: 确认纳入。blob-centric 图像检索组织与索引方案是明确制品，查询响应时间和 I/O 成本相对 naive 方案的改进构成全文评价核心。

### 03. A Matter of Equality: Linear Pricing in Combinatorial Exchanges

- Group: `retained_layer:digital_platform_mechanism_or_policy`
- Outcome: `confirmed_inclusion`
- Model/manual decision: `True` / `True`
- Manual reason: 确认纳入。组合交易所定价机制及投标语言属于可实施的平台机制设计，贸易利得、效率损失和计算性能均有明确最优参照。

### 04. Mobile Time-Based Targeting: Matching Product-Value Appeal to Time of Day

- Group: `retained_layer:digital_platform_mechanism_or_policy`
- Outcome: `confirmed_inclusion`
- Model/manual decision: `True` / `True`
- Manual reason: 确认纳入。按时段匹配产品价值诉求是可实施的移动定向规则，随机实地实验以实际购买率相对行业默认策略的提升为主要结果。

### 05. Cost-Effective Quality Assurance in Crowd Labeling

- Group: `retained_layer:hybrid`
- Outcome: `confirmed_inclusion`
- Model/manual decision: `True` / `True`
- Manual reason: 确认纳入。众包标注质量保障算法围绕误分类成本与标签成本设计，并通过模拟、真实数据和现场实验与多种基准比较。

### 06. A decision support system for planning and coordination of hybrid renewable energy systems

- Group: `retained_layer:hybrid`
- Outcome: `confirmed_inclusion`
- Model/manual decision: `True` / `True`
- Manual reason: 确认纳入。混合可再生能源规划 DSS 和随机优化/启发式方法以期望总成本和最优差距作为排他性评价标准。

### 07. An empirical study of web site navigation structures' impacts on web site usability

- Group: `retained_layer:interface_or_interaction_design`
- Outcome: `confirmed_inclusion`
- Model/manual decision: `True` / `True`
- Manual reason: 确认纳入。作者构建不同导航结构的网站版本，核心问题就是哪种界面结构提高客观任务完成表现；感知测量不是成功判据。

### 08. <b>Research Note</b>—Awareness Displays and Social Motivation for Coordinating Communication

- Group: `retained_layer:interface_or_interaction_design`
- Outcome: `confirmed_inclusion`
- Model/manual decision: `True` / `True`
- Manual reason: 确认纳入。awareness display 的信息粒度是被设计的界面属性，两轮实验用中断时机、任务正确率/时间和目标绩效进行客观比较。

### 09. An analytic approach to better understanding and management of coronary surgeries

- Group: `retained_layer:prediction_model`
- Outcome: `confirmed_inclusion`
- Model/manual decision: `True` / `True`
- Manual reason: 确认纳入。CABG 结局预测模型体系以测试集准确率、敏感度和特异度比较算法，客观预测表现是全文核心。

### 10. Predicting the length of hospital stay of burn patients: Comparisons of prediction accuracy among different clinical stages

- Group: `retained_layer:prediction_model`
- Outcome: `confirmed_inclusion`
- Model/manual decision: `True` / `True`
- Manual reason: 确认纳入。作者构建不同临床阶段的 LOS 预测模型并以线性回归为基准，MAE/MRE 的跨模型、跨阶段比较贯穿全文。

### 11. Optimal Policy for Software Patents: Model and Comparative Implications

- Group: `retained_layer:prescriptive_model_or_optimization`
- Outcome: `confirmed_inclusion`
- Model/manual decision: `True` / `True`
- Manual reason: 确认纳入（边界较宽）。论文给出可求解的软件专利政策决策规则，并以社会福利相对自由市场和替代政策的解析/数值比较为唯一成功标准；符合提示词对 formal prescriptive policy 的明确允许。

### 12. Hedging risks with interruptible load programs for a load serving entity

- Group: `retained_layer:prescriptive_model_or_optimization`
- Outcome: `confirmed_inclusion`
- Model/manual decision: `True` / `True`
- Manual reason: 确认纳入。可中断负荷采购随机规划以 CVaR 与期望利润为目标，并明确比较无该方案的基准情形。

### 13. Developing maintainable software: The Readable approach

- Group: `retained_layer:software_system_or_artifact`
- Outcome: `confirmed_inclusion`
- Model/manual decision: `True` / `True`
- Manual reason: 确认纳入。Readable 是实际构建的程序表示与执行环境，正确答案评分的程序理解测试相对 Java 对照构成主要评价。

### 14. A social route recommender mechanism for store shopping support

- Group: `retained_layer:software_system_or_artifact`
- Outcome: `confirmed_inclusion`
- Model/manual decision: `True` / `True`
- Manual reason: 确认纳入。社交购物路线推荐制品以推荐路线和真实访问路线的客观重叠率为核心，满意度仅为补充。

### 15. Designing Conversational Dashboards for Effective Use in Crisis Response

- Group: `retained_theory_driven`
- Outcome: `confirmed_inclusion`
- Model/manual decision: `True` / `True`
- Manual reason: 确认纳入。会话式仪表盘和 onboarding 是理论导出的界面制品；transparent interaction 用最短路径比率、效率用时间、有效性用正确任务数进行行为化测量并与六种制品条件比较。

### 16. Representing Part-Whole Relations in Conceptual Modeling: An Empirical Evaluation

- Group: `retained_theory_driven`
- Outcome: `confirmed_inclusion`
- Model/manual decision: `True` / `True`
- Manual reason: 确认纳入。概念建模中的 part-whole 表示是被设计的信息表示方式，答案正确率是主导结果，时间和感知易用性为辅助。

### 17. Designing Promotional Incentives to Embrace Social Sharing: Evidence from Field and Online Experiments

- Group: `retained_theory_driven`
- Outcome: `confirmed_inclusion`
- Model/manual decision: `True` / `True`
- Manual reason: 确认纳入。可分享性与稀缺性组合成数字促销机制，field/online experiments 以购买、成功推荐、净收入和 CLV 相对对照的改善为主。

### 18. Web-based intervention support system for health promotion

- Group: `retained_theory_driven`
- Outcome: `confirmed_inclusion`
- Model/manual decision: `True` / `True`
- Manual reason: 确认纳入。WISS 是实际 Web 干预支持制品，随机对照以药物停用率和阶段迁移等客观健康行为结果判断成效。

### 19. Online government advisory service innovation through Intelligent Support Systems

- Group: `near_miss_three_gates`
- Outcome: `confirmed_exclusion`
- Model/manual decision: `False` / `False`
- Manual reason: 确认排除。虽有三种咨询工具和客观 decision quality，但文章以 empowerment 理论及 DMS、DMT、SoC、PPR、GSPI 等感知构念形成并列核心，客观改进不占支配地位。

### 20. Optimizing Two-Sided Promotion for Transportation Network Companies: A Structural Model with Conditional Bayesian Learning

- Group: `near_miss_three_gates`
- Outcome: `confirmed_exclusion`
- Model/manual decision: `False` / `False`
- Manual reason: 确认排除。结构模型的主要贡献是估计 TNC 功能价值、司机学习和促销效应；优化促销政策只在主分析之后作为应用，不能反向代表全文的主要成功标准。

### 21. Applying behavioral economics in predictive analytics for B2B churn: Findings from service quality data

- Group: `near_miss_three_gates`
- Outcome: `confirmed_exclusion`
- Model/manual decision: `False` / `False`
- Manual reason: 确认排除。理论特征被用于 churn prediction 且报告测试集 AUC，但没有把所提特征/模型与不含这些特征的明确基线作性能增量比较；绝对 AUC 与重复抽样不满足 Gate 3。

### 22. Sensing the Future: A Design Framework for Context-Aware Predictive Systems

- Group: `near_miss_three_gates`
- Outcome: `false_negative`
- Model/manual decision: `False` / `True`
- Manual reason: 改判纳入。CAPS 不只是抽象框架：作者按该框架连续构建 context-aware predictive artifacts，以 Croston 为显式基线，用 forecasting-error cost 证明 phase-out 版本改善 4%、sensor activity 版本改善 20%。全文把框架归为 DSR improvement contribution，客观改进是评价其能否产生更好制品的主导证据；专家/情境反思用于迭代和边界说明，不是并列的主观成功指标。

### 23. A generic framework for sentiment analysis: Leveraging opinion-bearing data to inform decision making

- Group: `near_miss_three_gates`
- Outcome: `confirmed_exclusion`
- Model/manual decision: `False` / `False`
- Manual reason: 确认排除。ECCO 同时追求可迁移的模型选择、完整分析流程和 actionable insight；准确率基准只验证其中的 sentiment-modeling 模块，后半部分洞察能力主要以案例展示，故客观改进不是整个框架的支配性成功标准。

### 24. Exploring Modes of Facilitative Support for GDSS Technology

- Group: `near_miss_three_gates`
- Outcome: `confirmed_exclusion`
- Model/manual decision: `False` / `False`
- Manual reason: 确认排除。研究操纵的是既有 GDSS 外部的人工 facilitation 角色，而非作者设计或实质修改的数字制品；客观共识结果不能弥补 Gate 1。

### 25. Integrating social networking support for dyadic knowledge exchange: A study in a virtual community of practice

- Group: `near_miss_three_gates`
- Outcome: `confirmed_exclusion`
- Model/manual decision: `False` / `False`
- Manual reason: 确认排除。平台功能是研究场景中已经发生的自然整合，作者利用准实验解释其效果，没有提出或实施该制品改造。

### 26. Using “last-minute” sales for vertical differentiation on the Internet

- Group: `near_miss_three_gates`
- Outcome: `false_negative`
- Model/manual decision: `False` / `True`
- Manual reason: 改判纳入。文章给出可实施的在线随机 last-minute sales 定价/供给决策规则，解析求解不同参数下的最优策略，并把利润同确定性销售及其他策略类别直接比较。提示词明确允许 prescriptive model、decision rule 和 digital policy，因此不应仅因它不是软件界面而判 Gate 1 失败。

### 27. Performance Outcomes of Test-Driven Development: An Experimental Investigation

- Group: `excluded_objective_without_design`
- Outcome: `confirmed_exclusion`
- Model/manual decision: `False` / `False`
- Manual reason: 确认排除。文章比较已有 TDD 与 test-last 开发实践，不设计软件制品；且软件质量与任务满意度是并列结果。

### 28. Using Self-Regulatory Learning to Enhance E-Learning-Based Information Technology Training

- Group: `excluded_objective_without_design`
- Outcome: `confirmed_exclusion`
- Model/manual decision: `False` / `False`
- Manual reason: 确认排除。干预是系统外的纸质 self-regulatory learning scripts，而非 e-learning 系统功能或数字制品改造。

### 29. <b>Research Note</b>—An Investigation of the Appropriation of Technology-Mediated Training Methods Incorporating Enactive and Collaborative Learning

- Group: `excluded_objective_without_design`
- Outcome: `confirmed_exclusion`
- Model/manual decision: `False` / `False`
- Manual reason: 确认排除。WBT 是现成商业产品，作者比较的是培训/协作教学安排；知识测试与自我效能、满意度并列，既不满足 Gate 1 也不满足 Gate 4。

### 30. Computer-Related Task Performance: A new perspective

- Group: `excluded_objective_without_design`
- Outcome: `confirmed_exclusion`
- Model/manual decision: `False` / `False`
- Manual reason: 确认排除。self-prophecy 提问是行为实验操纵，不是 IS 制品；处理相对控制也未证明任务正确率改善。
