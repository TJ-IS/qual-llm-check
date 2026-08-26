# Industry classification with online resume big data: A design science approach

- 作者：Xiaoying Xu; Hanlin Qian; Chunmian Ge; Zhijie Lin
- 年份 / 期刊：2020 / Information & Management
- DOI：10.1016/j.im.2019.103182
- 源文件：07978_2020_industry-classification-with-online-resume-big-data-a-design-science-approach.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：performance_gap_artifact_benchmark_generalize
- 置信度：0.82

## 文章级论证概况

- 核心问题：如何利用在线简历大数据中隐含的人力资本与劳动力流动信息，构建及时且纳入人力资本维度的行业分类方法？

- 制品与设计：自动行业分类架构，包括简历爬虫（Resume Crawler）、劳动力流动网络构造器（Network Constructor）和行业分类器（Industry Classifier，基于层次化Louvain社区发现）。输入是在线专业社交网络简历，输出20个企业簇构成的行业分类。

- 客观结果：在真实数据上，LMN方法在平均调整R2上高于SIC、NAICS、GICS、HP、FDD、INM、MO；跨行业变异在销售、资产、销售增长、市场beta、资产beta上均更高；标注者一致性Fleiss' kappa为0.7396；两个案例显示Google和Microsoft的跨行业流动连接早于10-K披露。

- 核心贡献：提出基于劳动力流动网络的自动行业分类方法，扩展层次化社区发现算法，实证支持Resource-Based View中人力资本/技能关联可用于行业分析，并作为现有行业分类体系的补充而非替代。

- 整篇论证链：现有行业分类存在两处主要局限：时滞和忽略人力资本信息；10-K文本方法虽然改进但仍有滞后且仍不包含人力资本。作者以在线简历大规模数据为新数据源，基于RBV和技能关联理论认为企业进入新领域需先招聘相关人才，因此企业间劳动力流动网络可反映行业相似性。系统依次通过简历爬虫、网络构造器和层次化Louvain分类器将理论操作化为可计算制品，再用网络结构指标、人工标注、股票收益解释力、跨行业变异和案例时间前向性进行多层次评价，最终把性能结果回译为RBV的实证支持。

## 类型与写作弧线判定

- 论文主类型判定：作者明确采用设计科学研究方法，构建了由简历爬虫、网络构造器和行业分类器组成的IT制品，并按照设计科学的思路对制品进行网络分析、定性标注、基准比较和应用案例等多项评价。它不是单纯的计算制品benchmark论文，也不是现场实验，而是以制品构建加多维度评价为核心。

- 主导写作弧线判定：论证主线是：现有方案性能/能力存在缺口（时滞和缺人力资本）→ 构造新型制品（劳动力流动网络+层次化Louvain）→ 用基准比较和稳健性检验证明性能优势 → 将性能优势一般化为设计知识和方法论含义。文中没有系统提炼设计原则，也没有以现象机制现场干预为主线。

## 研究开展程序

- study_or_phase_count：8

- 研究阶段总序列：先采集在线简历数据并与上市企业匹配，再从中抽取跳槽记录构造企业间劳动力流动网络，接着设计层次化Louvain分类器；然后依次用网络结构诊断、人工标注、股票收益解释力、跨行业变异和案例时间前向性进行评价。各阶段从数据基础到制品实现再到外部有效性逐层累积。

### studies_or_phases

#### 1. 在线简历数据采集与上市企业匹配

- order：1

- name_cn：在线简历数据采集与上市企业匹配

- question_cn：能否从专业社交网络公开简历获得足量、可匹配企业层面数据的人力资本流动信息？

- inputs_and_setting_cn：大型专业社交网络公开简历；1.52M简历、5.74M工作记录、2.83M跳槽记录；Compustat匹配；S&P 1500样本

- designed_or_compared_object_cn：Resume Crawler爬虫制品；企业-年份匹配结果

- baseline_control_or_counterfactual_cn：无对照；主要检查数据规模与匹配完整性

##### objective_metrics

1. 简历数

2. 工作记录数

3. 跳槽记录数

4. 匹配企业数

- analysis_method_cn：网络爬虫、HTML解析、数据库存储与年份汇总

- main_result_cn：2011-2013年分别有4,239、4,123、4,067家S&P 1500企业与Compustat匹配

- argumentative_role_cn：为后续构网与评价提供数据基础

- remaining_uncertainty_cn：样本在行业中的分布可能不均；平台对企业名称的识别可能产生匹配偏差

- link_to_next_phase_cn：将简历工作经历转化为跳槽元组并构造网络

##### evidence_pointers

1. Sec 4.1

2. Sec 4.5

3. Table 1

#### 2. 劳动力流动网络构造

- order：2

- name_cn：劳动力流动网络构造

- question_cn：如何把个人简历中的工作经历聚合成企业级劳动力流动网络？

- inputs_and_setting_cn：已采集简历网页；JSoup解析的工作经历字段

- designed_or_compared_object_cn：Network Constructor组件；有向加权图G_year

- baseline_control_or_counterfactual_cn：无；以单条跳槽元组作为原子事实

##### objective_metrics

1. 节点数

2. 边数

3. 边权人数

- analysis_method_cn：HTML解析、元组提取、按年份聚合

- main_result_cn：可构造节点规模约19万家企业的年度有向加权劳动力流动网络

- argumentative_role_cn：将核心机制操作化为可计算的网络结构

- remaining_uncertainty_cn：简历是否完整、工作起止时间是否真实；无法验证未记录的跳槽

- link_to_next_phase_cn：网络作为行业分类器的输入

##### evidence_pointers

1. Sec 4.2.1

2. Sec 4.2.2

3. Fig 3

#### 3. 层次化Louvain行业分类器设计

- order：3

- name_cn：层次化Louvain行业分类器设计

- question_cn：如何在大规模劳动力网络中发现规模可控且可解释的行业簇？

- inputs_and_setting_cn：2011-2013年劳动力流动网络；目标社区数20

- designed_or_compared_object_cn：Industry Classifier组件；层次化Louvain算法

- baseline_control_or_counterfactual_cn：原始Louvain会生成约10,000个社区；以20个社区作为与现有方案可比的尺度

##### objective_metrics

1. 社区数量

2. 模块度

- analysis_method_cn：模块度最大化，迭代合并社区

- main_result_cn：得到20个层级化行业簇

- argumentative_role_cn：实现从网络到行业分类的核心算法；支撑多尺度结构分析

- remaining_uncertainty_cn：目标数20是否丢失更细粒度信息；层级数未系统调优

- link_to_next_phase_cn：先检验网络结构，再检验行业簇质量

##### evidence_pointers

1. Sec 4.3

2. Fig 4

3. Fig 5

#### 4. 网络结构诊断

- order：4

- name_cn：网络结构诊断

- question_cn：构建的网络是否有足够密度和社区结构以支撑行业发现？

- inputs_and_setting_cn：三年劳动力流动网络

- designed_or_compared_object_cn：网络结构指标

- baseline_control_or_counterfactual_cn：与真实社会网络最高密度0.5及模块度阈值0.3比较

##### objective_metrics

1. Density

2. Modularity

3. Clustering Coefficient

- analysis_method_cn：描述性网络指标计算

- main_result_cn：密度0.31-0.36，模块度0.58-0.68，聚类系数0.65-0.70，中心企业逐年变化

- argumentative_role_cn：为后续社区发现提供结构合法性

- remaining_uncertainty_cn：结构指标高不代表经济意义上的行业边界正确

- link_to_next_phase_cn：进入识别结果的可解释性检查

##### evidence_pointers

1. Sec 4.7.1

2. Table 2

#### 5. 识别行业的定性标注与一致性检验

- order：5

- name_cn：识别行业的定性标注与一致性检验

- question_cn：算法产出的20个簇是否对应可理解的行业类别？

- inputs_and_setting_cn：2012年20个企业簇；4位管理类专业博士生；30个NAICS相关标签组成的标签集

- designed_or_compared_object_cn：行业簇标签；标注者一致性

- baseline_control_or_counterfactual_cn：无对照；用Fleiss' kappa检验多标注者一致性

##### objective_metrics

1. Fleiss' kappa

2. 标签可解释性

- analysis_method_cn：多数投票与Fleiss' kappa

- main_result_cn：kappa=0.7396，substantial agreement；Top 5互联网、金融、制造、快速消费品、零售等可解释

- argumentative_role_cn：提供人工可读的构念效度

- remaining_uncertainty_cn：标签集基于NAICS，可能无法捕捉新兴行业；标注者样本小

- link_to_next_phase_cn：转向与外部金融指标比较

##### evidence_pointers

1. Sec 4.7.2

2. Table 3

#### 6. 股票收益解释力基准比较

- order：6

- name_cn：股票收益解释力基准比较

- question_cn：LMN行业分类是否比传统方案和10-K文本方法更好地解释股票收益共同变动？

- inputs_and_setting_cn：S&P 500和S&P 1500企业；2011-2013年月度收益；Compustat；Yahoo Finance市值

- designed_or_compared_object_cn：LMN分类 vs SIC/NAICS/GICS/HP/FDD/INM/MO

- baseline_control_or_counterfactual_cn：两位SIC、三位NAICS、六位GICS；HP/FDD结果直接采用原论文；Bhojraj等证明组数差异影响不显著

##### objective_metrics

1. 平均调整R2

- analysis_method_cn：每月截面回归，36次回归取平均调整R2

- main_result_cn：LMN最高；相对GICS提高8.31%/4.67%，相对FDD提高1.23%/3.97%；相对INM/MO提高7.60%/36.88%和2.11%/21.47%

- argumentative_role_cn：核心性能主张：新分类在金融指标上有增量解释力

- remaining_uncertainty_cn：HP/FDD未复现；增量幅度小；行业效应可能接近上界

- link_to_next_phase_cn：用跨行业变异做稳健性检验

##### evidence_pointers

1. Sec 4.7.3

2. Fig 6

3. Table 4

#### 7. 跨行业变异稳健性检验

- order：7

- name_cn：跨行业变异稳健性检验

- question_cn：LMN行业组是否能在财务特征上产生更高的跨行业差异？

- inputs_and_setting_cn：2011-2013分类结果与S&P样本的销售、资产、销售增长、市场beta、资产beta

- designed_or_compared_object_cn：LMN vs SIC/NAICS/INM/MO

- baseline_control_or_counterfactual_cn：未纳入HP/FDD，因为原论文未报告且难以复现

##### objective_metrics

1. 跨行业变异sigma_f

- analysis_method_cn：用既定公式计算特征变异并比较

- main_result_cn：LMN在所有特征上均更高，最低提升7.31%

- argumentative_role_cn：增强分类信息量的稳健性，排除仅单一指标偶然性

- remaining_uncertainty_cn：未与HP/FDD比较；对特征选择可能敏感

- link_to_next_phase_cn：转向实际应用案例

##### evidence_pointers

1. Sec 4.7.4

2. Fig 7

3. Table 5

#### 8. 企业新行业进入揭示案例

- order：8

- name_cn：企业新行业进入揭示案例

- question_cn：方法能否早于年报揭示企业进入新行业的行动？

- inputs_and_setting_cn：2011年部分劳动力流动网络图；Google与Microsoft两个案例；10-K披露时间线

- designed_or_compared_object_cn：网络中企业与不同行业社区之间的异常连接

- baseline_control_or_counterfactual_cn：以年报/10-K披露时间作为滞后参照，进行时间前向比较

##### objective_metrics

1. 是否存在跨行业流动连接

2. 与10-K披露的时间差

- analysis_method_cn：案例叙述与网络可视化

- main_result_cn：Google与汽车社区连接，10-K到2017才提及自动驾驶；Microsoft与电子社区连接，Surface在2012发布前3年已有招聘需求

- argumentative_role_cn：展示实际业务价值和外部效度

- remaining_uncertainty_cn：仅2个案例；未定量检验及时性；无法证明连接一定代表进入新行业

- link_to_next_phase_cn：结论中总结贡献与局限

##### evidence_pointers

1. Sec 4.7.5

2. Fig 8

## 各部分修辞架构

### abstract_moves

1. CONTEXT: 行业分类是行业分析和竞争情报的关键步骤

2. LIMITATION: 现有方案受制于业务信息滞后和缺少人力资本视角

3. RQ_OR_OBJECTIVE: 用设计科学方法开发基于在线简历大数据的新行业分类方法

4. DESIGN_FEATURE: 构建劳动力流动网络并提出层次化Louvain扩展

5. RESULT: 真实数据评估优于现有方案和最新方法，案例验证早期预警

### introduction_moves

1. CONTEXT/PRACTICAL_STAKES: 竞争情报的重要性与IBM案例

2. REQUIREMENT: 好的行业分类应及时反映企业业务变化

3. LIMITATION: SIC/NAICS存在时滞、新行业识别和人力资本缺失问题

4. LIMITATION: 10-K文本方法仍有低频更新且不关注人力资本

5. PRIOR_KNOWLEDGE: 互联网个人数据日益可得且被广泛使用

6. RQ_OR_OBJECTIVE: 提出设计科学制品并说明是补充而非替代

7. MECHANISM: 企业进入新领域必须先招聘相关人员

8. THEORY_PROPOSITION: RBV和技能关联为人力资源视角提供理论依据

9. DESIGN_FEATURE: 用在线简历跳槽记录构造劳动力流动网络

10. STUDY_OVERVIEW: 预告算法扩展和评价结果

11. CONTRIBUTION: 总结自动行业分类架构的价值

12. TRANSITION: 给出全文结构路线图

### theory_and_knowledge_moves

1. THEORY_INTRO: RBV强调企业资源异质性

2. THEORY_PROPOSITION: Farjoun和Nefke/Henning认为人力专长与技能关联可刻画行业分组

3. GAP: 现有行业分类研究忽略人力资本信息

4. PRIOR_KNOWLEDGE: 在线职业社交网络已被证明可研究人力资源问题

5. GAP: 尚无工作用在线职业社交网络做行业分析

6. PRIOR_KNOWLEDGE: 社区检测适合大规模快速变化网络

7. GAP: 未发现将社区检测用于竞争情报/行业分析

8. METHOD_JUSTIFICATION: Louvain在质量与可扩展性上最优且便于层级扩展

### artifact_design_moves

1. DESIGN_FEATURE: 三层架构：简历爬虫、网络构造器、行业分类器

2. DESIGN_FEATURE: 爬虫集成Google API下载公开简历

3. DESIGN_FEATURE: 用JSoup提取工作经历并生成跳槽元组

4. DESIGN_FEATURE: 聚合为企业级有向加权图

5. METHOD_JUSTIFICATION: 模块度最大化衡量社区划分合理性

6. DESIGN_FEATURE: 层次化Louvain迭代合并社区至20个

7. REQUIREMENT: 目标社区数需与传统方案可比且易解释

### evaluation_moves

1. METHOD_JUSTIFICATION: 原型用Java、R、MySQL实现

2. BENCHMARK_OR_CONTRAST: 用密度、模块度、聚类系数做网络结构诊断

3. BENCHMARK_OR_CONTRAST: 用平均调整R2做股票收益解释力比较

4. BENCHMARK_OR_CONTRAST: 用跨行业变异做信息量稳健性检验

5. RESULT: 网络结构指标良好

6. RESULT: 标注者一致性substantial agreement

7. RESULT: LMN平均调整R2高于所有对比方法

8. RESULT: LMN跨行业变异更高

9. ROBUSTNESS_OR_BOUNDARY_TEST: Google和Microsoft案例显示时间前向性

### discussion_and_contribution_moves

1. CONTRIBUTION: 用设计科学方法解决时滞和人力资本缺失问题

2. THEORY_INTRO/THEORY_PROPOSITION: 结果回译为对RBV的实证支持

3. BOUNDARY_CONDITION: 无法识别完全依赖内部转岗的行业进入

4. LIMITATION_AND_FUTURE: 样本行业分布不均、及时性未定量检验

5. LIMITATION_AND_FUTURE: 未来研究劳动力流动与企业绩效关系

## 理论/知识到设计的翻译

### 知识/理论基础

1. Resource-Based View（Wernerfelt; Farjoun的Resource-RIGs; Nefke & Henning的skill relatedness）

2. 在线职业社交网络数据可靠性研究（Ge, Huang & Png; Antoine et al.; Wang, Li & Zhou）

3. 社区检测与模块度最大化文献（Louvain, Infomap, Modularity Optimality等）

- 理论—设计耦合：partial

- 耦合判定理由：RBV和技能关联为‘用人力资源流动识别行业’提供了方向和变量选择，但网络构造、Louvain算法选择与层次化扩展主要由数据规模、社区质量和评价可比性等工程因素决定；理论没有直接推出算法细节。

- 理论到设计翻译链：RBV/技能关联 → 人力资源流动可表征行业相似性 → 企业进入新业务会引发相关领域招聘 → 用在线简历提取跳槽记录 → 构造企业级劳动力流动网络 → 用模块度最大化的层次化Louvain发现行业簇 → 以股票收益共动和跨行业变异检验行业边界的经济意义 → 以案例显示时间前向预警。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：Farjoun和Nefke & Henning认为人力专长/技能关联可用于刻画行业分组

- mechanism_cn：具备相似技能/人力资本的企业会因劳动力流动而紧密连接

- design_requirement_cn：需要人力资本信息而非仅产品/业务描述作为分类依据

- artifact_choice_cn：从在线简历抽取跳槽记录，构造企业间有向加权劳动力流动网络

- evaluated_contrast_cn：LMN vs SIC/NAICS/GICS/HP/FDD

- objective_result_cn：LMN平均调整R2更高，跨行业变异更高

##### evidence_pointers

1. Sec 2.2

2. Sec 3

3. Sec 4.2

4. Sec 4.7.3

5. Sec 4.7.4

#### 2. 2

- theory_or_knowledge_claim_cn：企业进入新业务需要先招聘相关领域人员

- mechanism_cn：新行业进入会表现为企业与异行业社区之间的异常劳动力流动

- design_requirement_cn：分类结果应能保留或暴露跨行业异常连接，而不仅是给出静态标签

- artifact_choice_cn：层次化Louvain可观察不同尺度社区，并在案例中检查跨社区连接

- evaluated_contrast_cn：案例中的跨行业连接 vs 企业10-K披露时间

- objective_result_cn：Google/Microsoft与目标行业社区的连接早于10-K多年

##### evidence_pointers

1. Sec 4.7.5

2. Fig 8

#### 3. 3

- theory_or_knowledge_claim_cn：现有社区检测研究比较显示Louvain在质量和可扩展性上是领先算法

- mechanism_cn：大规模网络用模块度最大化可将密集流动的企业聚成簇；随机游走类算法与模块度优化可做基准

- design_requirement_cn：算法需能处理约20万节点并输出可与传统方案相比的行业组数

- artifact_choice_cn：扩展Louvain为层次版本，合并社区迭代至20个簇；选择INM/MO作为算法选择对照

- evaluated_contrast_cn：LMN vs INM/MO在同一网络上的分类结果

- objective_result_cn：LMN在R2和跨行业变异上优于INM/MO

##### evidence_pointers

1. Sec 2.4

2. Sec 4.3

3. Sec 4.7.3

4. Sec 4.7.4

## 评价逻辑

### evaluation_modes

1. 结构诊断：密度、模块度、聚类系数

2. 内容效度：4位标注者标注20个行业簇及Fleiss' kappa

3. 金融解释力基准：平均调整R2的月度截面回归

4. 信息量稳健性：跨行业变异比较

5. 案例时效性：Google和Microsoft跨行业连接早于10-K披露

- why_these_evaluations_cn：因为行业分类没有单一真值，论文先用网络结构指标确认劳动力流动网络可聚类，再用人类标注确认可解释性，然后用金融市场收益共动作为外部有效性指标，用跨行业变异作为互补的稳健性指标，最后用时间前向案例展示实践价值。

- benchmark_and_contrast_chain_cn：先以网络结构阈值（模块度>0.3、密度相对0.5）建立内部合理性；再以标注一致性建立内容效度；然后建立与传统方案SIC/NAICS/GICS、10-K文本方法HP/FDD、替代社区检测算法INM/MO的性能对比；用跨行业变异复核同一结论；最后用案例的时间前向性提升外部效度。

### claim_evidence_ledger

#### 1. LMN分类能更有效地解释股票收益共同变动

- claim_cn：LMN分类能更有效地解释股票收益共同变动

- evidence_cn：平均调整R2在S&P500和S&P1500均高于所有对比方法

- support_level_cn：较强；但HP/FDD结果未复现，增幅较小

#### 2. LMN产生更有信息量的行业分类

- claim_cn：LMN产生更有信息量的行业分类

- evidence_cn：跨行业变异在销售、资产、销售增长、市场/资产beta上均更高

- support_level_cn：较强；但未与HP/FDD比较

#### 3. 识别的行业簇具有可解释性

- claim_cn：识别的行业簇具有可解释性

- evidence_cn：4名标注者Fleiss' kappa=0.7396，Top5行业可读

- support_level_cn：中等；标签集基于NAICS，可能限制新行业

#### 4. 劳动力流动网络结构适合行业分析

- claim_cn：劳动力流动网络结构适合行业分析

- evidence_cn：密度、模块度、聚类系数高

- support_level_cn：支持结构前提；不等同经济含义

#### 5. 方法能较早揭示企业进入新行业

- claim_cn：方法能较早揭示企业进入新行业

- evidence_cn：Google与汽车社区连接早于10-K多年；Microsoft与电子社区连接早于Surface披露

- support_level_cn：案例证据，未定量检验及时性

#### 6. 选择Louvain优于其他社区检测算法

- claim_cn：选择Louvain优于其他社区检测算法

- evidence_cn：LMN在R2和跨行业变异上优于INM/MO

- support_level_cn：较强；但只比较两种替代算法

- internal_validity_strategy_cn：通过Compustat匹配限定上市企业样本；用多个评价指标交叉验证；控制行业组数差异采用两位SIC/三位NAICS/六位GICS；纳入替代算法INM/MO作为组件选择的消融对照；用月度截面回归减少时间点偶然性；在案例中建立与10-K披露的时间前向关系。

- external_validity_strategy_cn：使用1.52M真实在线简历、三年窗口、S&P500与S&P1500两个市场样本；不只报告统计提升，还展示人工可解释行业与应用案例；明确区分补充方案而非替代方案。

- what_is_not_actually_tested_cn：没有直接检验‘企业进入新行业必须外部招聘’这一机制；没有定量测量及时性；没有检验内部转岗型进入；标注者使用NAICS标签集无法充分捕获新兴行业；HP/FDD结果未复现；样本行业分布可能偏向IT；跨行业变异与HP/FDD未比较。

## 贡献闭环

- technical_claim_cn：LMN方法在股票收益解释力与跨行业变异两个指标上优于SIC/NAICS/GICS、10-K文本方法HP/FDD以及INM/MO算法。

- artifact_claim_cn：包含简历爬虫、网络构造器和层次化Louvain行业分类器的自动行业分类架构，能将在线简历数据转化为及时、可扩展的行业分类。

- mechanism_claim_cn：劳动力在企业之间的流动体现了技能关联和行业相似性，因此跨企业劳动力流动网络中的社区结构可代表潜在行业类别；异常跨行业连接可揭示新行业进入行动。

- boundary_claim_cn：方法适用于能通过外部招聘实现业务转型的企业；对完全依赖现有员工转岗的进入无法识别；样本若行业分布不均衡，结论可能偏向用户活跃行业；及时性尚未定量检验。

- reusable_design_knowledge_cn：设计知识包括：用人力资本/劳动力流动关系替代或补充产品文本作为行业相似性的证据源；用层级化社群发现获得可控粒度的行业分类；用股票收益共动和跨行业变异作为行业分类外部评价指标；用补充而非替代定位避免与既有体系冲突。

- theoretical_contribution_cn：实证检验了RBV的人力资源维度可用于行业分类，拓展了‘技能关联’概念在大规模线上数据上的操作性，但对理论本身没有修正或形式化扩展。

- how_discussion_closes_intro_gap_cn：结论直接回应引言指出的时滞与人力资本缺失，说明基于劳动力流动的方法是补充且有效；将评价结果表述为RBV的实证支持，从而把性能差异升华为理论含义。

- overclaim_or_unsupported_leaps_cn：主要风险是从两个案例推广到‘能够揭示企业进入新行业’；性能提升相对FDD较小且HP/FDD未复现；机制断言在数据中未被直接测量；‘及时性’在摘要和结论中被强调，但正文明确承认未定量检验。

## 句级写作动作图谱

### 1. Abstract P1 S1

- order：1

- section：Abstract

- locator：Abstract P1 S1

- move_code：CONTEXT

- paraphrase_cn：行业分类是行业分析和竞争情报的关键步骤。

- rhetorical_function_cn：开篇界定研究对象的重要性。

- depends_on_cn：无

- sets_up_cn：引出对现有方案局限的讨论。

- evidence_pointer：Abstract P1

### 2. Abstract P1 S2

- order：2

- section：Abstract

- locator：Abstract P1 S2

- move_code：LIMITATION

- paraphrase_cn：现有方案和方法受企业业务信息滞后以及缺少对人力资源方面的考虑所限制。

- rhetorical_function_cn：给出全文要解决的双重问题。

- depends_on_cn：步骤1

- sets_up_cn：为提出新方法做铺垫。

- evidence_pointer：Abstract P1

### 3. Abstract P1 S3

- order：3

- section：Abstract

- locator：Abstract P1 S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文采用设计科学方法，通过构建劳动力流动网络并使用在线简历大数据来开发和评价新的行业分类方法。

- rhetorical_function_cn：明确研究目标和制品。

- depends_on_cn：步骤2

- sets_up_cn：引出方法概要。

- evidence_pointer：Abstract P1

### 4. Abstract P1 S4

- order：4

- section：Abstract

- locator：Abstract P1 S4

- move_code：DESIGN_FEATURE

- paraphrase_cn：提出层次化扩展的社区检测算法，以更好地在网络上发现可扩展的企业簇。

- rhetorical_function_cn：强调关键技术设计。

- depends_on_cn：步骤3

- sets_up_cn：为评价结果提供技术对象。

- evidence_pointer：Abstract P1

### 5. Abstract P1 S5

- order：5

- section：Abstract

- locator：Abstract P1 S5

- move_code：RESULT

- paraphrase_cn：真实数据集评估显示方法优于现有行业分类方案和最新方法，两个应用案例确认其能较早揭示企业进入新产业。

- rhetorical_function_cn：以结果和案例收束摘要。

- depends_on_cn：步骤3-4

- sets_up_cn：建立全文阅读预期。

- evidence_pointer：Abstract P1

### 6. Introduction P1 S1

- order：6

- section：Introduction

- locator：Introduction P1 S1

- move_code：CONTEXT

- paraphrase_cn：竞争情报是识别竞争动态和非市场因素从而增强竞争优势的过程，已成为大企业核心能力。

- rhetorical_function_cn：建立宽泛现实背景。

- depends_on_cn：无

- sets_up_cn：为行业分类的重要性做铺垫。

- evidence_pointer：Introduction P1

### 7. Introduction P1 S3

- order：7

- section：Introduction

- locator：Introduction P1 S3

- move_code：PRACTICAL_STAKES

- paraphrase_cn：IBM在1991-1993年亏损超过140亿美元后，通过CI项目成功跟踪和分析竞争者，使其成为公司文化一部分。

- rhetorical_function_cn：用企业案例说明竞争情报的现实价值。

- depends_on_cn：步骤6

- sets_up_cn：强调行业分析工具的重要性。

- evidence_pointer：Introduction P1, IBM example

### 8. Introduction P2 S1

- order：8

- section：Introduction

- locator：Introduction P2 S1

- move_code：CONTEXT

- paraphrase_cn：CI的首要目标是提供行业和竞争者概览，行业分类是研究焦点企业竞争环境与成长机会前的重要步骤。

- rhetorical_function_cn：从CI缩小到行业分类工具。

- depends_on_cn：步骤6-7

- sets_up_cn：引出对好分类标准的要求。

- evidence_pointer：Introduction P2

### 9. Introduction P2 S2

- order：9

- section：Introduction

- locator：Introduction P2 S2

- move_code：REQUIREMENT

- paraphrase_cn：好的行业分类应及时反映企业业务在市场竞争中的快速变化，使管理层能够响应。

- rhetorical_function_cn：建立用于批评现有方案的规范性标准。

- depends_on_cn：步骤8

- sets_up_cn：引出SIC/NAICS的不足。

- evidence_pointer：Introduction P2

### 10. Introduction P3 S1-S2

- order：10

- section：Introduction

- locator：Introduction P3 S1-S2

- move_code：LIMITATION

- paraphrase_cn：SIC和NAICS虽然广泛使用，但存在时滞，难以识别自动驾驶等新兴行业。

- rhetorical_function_cn：指出现有分类的第一类缺陷。

- depends_on_cn：步骤9

- sets_up_cn：继续指出第二缺陷。

- evidence_pointer：Introduction P3

### 11. Introduction P3 S3-S4

- order：11

- section：Introduction

- locator：Introduction P3 S3-S4

- move_code：LIMITATION

- paraphrase_cn：现有分类主要关注业务或产品侧，缺少人力资本信息。

- rhetorical_function_cn：补充第二个研究缺口。

- depends_on_cn：步骤10

- sets_up_cn：为数据机会做铺垫。

- evidence_pointer：Introduction P3

### 12. Introduction P4 S1

- order：12

- section：Introduction

- locator：Introduction P4 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：随着IT发展，个人数据在互联网上日益可得并被研究者广泛使用。

- rhetorical_function_cn：引入新数据源机会。

- depends_on_cn：步骤11

- sets_up_cn：提出设计科学方案。

- evidence_pointer：Introduction P4

### 13. Introduction P4 S2

- order：13

- section：Introduction

- locator：Introduction P4 S2

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文使用设计科学方法构建自动行业分类架构，利用在线专业社交网络蕴含的人力资本信息并及时反映行业变化。

- rhetorical_function_cn：明确提出研究目标和制品。

- depends_on_cn：步骤11-12

- sets_up_cn：为定位说明提供基础。

- evidence_pointer：Introduction P4

### 14. Introduction P4 S3-S4

- order：14

- section：Introduction

- locator：Introduction P4 S3-S4

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：本文目的不是完全替代现有方案，而是作为补充，从劳动力流动这一全新视角出发。

- rhetorical_function_cn：主动限定贡献范围，防止被误读为替代性方案。

- depends_on_cn：步骤13

- sets_up_cn：避免后续评价中提出过强主张。

- evidence_pointer：Introduction P4

### 15. Introduction P5 S1

- order：15

- section：Introduction

- locator：Introduction P5 S1

- move_code：MECHANISM

- paraphrase_cn：企业决定进入新领域时，必须先招聘相关领域或拥有相关技能的人员。

- rhetorical_function_cn：提出支持劳动力流动网络的核心经验机制。

- depends_on_cn：步骤13

- sets_up_cn：为构网设计提供直觉。

- evidence_pointer：Introduction P5

### 16. Introduction P5 S2

- order：16

- section：Introduction

- locator：Introduction P5 S2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：Farjoun和Nefke/Henning从人力资源视角分析行业组的研究为本文提供了理论依据。

- rhetorical_function_cn：引用RBV相关研究将经验事实理论化。

- depends_on_cn：步骤15

- sets_up_cn：将理论转化为设计方向。

- evidence_pointer：Introduction P5

### 17. Introduction P5 S3

- order：17

- section：Introduction

- locator：Introduction P5 S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：具体方式是收集在线简历、提取每个个体的跳槽记录，并构建企业间劳动力流动网络。

- rhetorical_function_cn：将理论命题转化为具体数据制品设计。

- depends_on_cn：步骤15-16

- sets_up_cn：引出后面的爬虫、网络构造器。

- evidence_pointer：Introduction P5

### 18. Introduction P6 S1-S2

- order：18

- section：Introduction

- locator：Introduction P6 S1-S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：将Louvain算法扩展为层次版本以发现企业簇，并测量不同行业间异常跳转来检测进入新行业的动作。

- rhetorical_function_cn：说明技术方案与检测应用。

- depends_on_cn：步骤17

- sets_up_cn：为评价部分预告核心结果。

- evidence_pointer：Introduction P6

### 19. Introduction P6 S3

- order：19

- section：Introduction

- locator：Introduction P6 S3

- move_code：RESULT

- paraphrase_cn：基于真实数据的评价显示，提出方法在解释股票收益变异和扩大跨行业差异方面优于常用方案和10-K方法。

- rhetorical_function_cn：在引言中给出核心结论。

- depends_on_cn：步骤18

- sets_up_cn：强调案例价值。

- evidence_pointer：Introduction P6

### 20. Introduction P7

- order：20

- section：Introduction

- locator：Introduction P7

- move_code：CONTRIBUTION

- paraphrase_cn：该自动行业分类架构动态反映企业进出行业，纳入人力资本信息，并且对研究者和实践者有启示。

- rhetorical_function_cn：总结贡献，闭合引言。

- depends_on_cn：步骤13-19

- sets_up_cn：预告文章结构。

- evidence_pointer：Introduction P7

### 21. Introduction P8

- order：21

- section：Introduction

- locator：Introduction P8

- move_code：TRANSITION

- paraphrase_cn：剩余部分依次为相关研究回顾、方法直觉与概览、详细方法与评价、总结与未来研究。

- rhetorical_function_cn：作为全文路标。

- depends_on_cn：步骤20

- sets_up_cn：引导读者进入后续各节。

- evidence_pointer：Introduction P8

### 22. Section 2 intro

- order：22

- section：Section 2

- locator：Section 2 intro

- move_code：STUDY_OVERVIEW

- paraphrase_cn：本节将回顾行业分类、RBV、在线职业社交网络和社区检测四方面相关研究。

- rhetorical_function_cn：预告文献综述的结构。

- depends_on_cn：步骤21

- sets_up_cn：为四类知识基础分别说明。

- evidence_pointer：Section 2 intro

### 23. Sec 2.1 P1-P2

- order：23

- section：Section 2.1

- locator：Sec 2.1 P1-P2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：传统分类方案基于产品或市场活动定义行业，而非企业间关系。

- rhetorical_function_cn：界定传统行业分类的旧范式。

- depends_on_cn：步骤22

- sets_up_cn：为批评传统方案提供基础。

- evidence_pointer：Section 2.1

### 24. Sec 2.1 P3

- order：24

- section：Section 2.1

- locator：Sec 2.1 P3

- move_code：LIMITATION

- paraphrase_cn：类别少、更新频率低、二元归属关系无法度量企业间关联程度。

- rhetorical_function_cn：系统化传统分类的缺陷。

- depends_on_cn：步骤23

- sets_up_cn：引出新分类方法。

- evidence_pointer：Section 2.1

### 25. Sec 2.1 P4

- order：25

- section：Section 2.1

- locator：Sec 2.1 P4

- move_code：LIMITATION

- paraphrase_cn：10-K文本和XBRL财务信息聚类等新方法虽有进展，但仍因数据滞后而缺失及时性。

- rhetorical_function_cn：指出现有延伸工作的共同弱点。

- depends_on_cn：步骤24

- sets_up_cn：将本文方法定位为超越这些方法。

- evidence_pointer：Section 2.1

### 26. Sec 2.2 P1

- order：26

- section：Section 2.2

- locator：Sec 2.2 P1

- move_code：THEORY_INTRO

- paraphrase_cn：RBV认为每个企业因资源异质而不同。

- rhetorical_function_cn：引入理论基础。

- depends_on_cn：步骤22

- sets_up_cn：引出人力资源资源视角。

- evidence_pointer：Section 2.2

### 27. Sec 2.2 P2

- order：27

- section：Section 2.2

- locator：Sec 2.2 P2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：Farjoun和Nefke/Henning的Resource-RIGs与技能关联研究为从人力资源角度分类行业提供了理论依据。

- rhetorical_function_cn：建立理论与分类方法的直接联系。

- depends_on_cn：步骤26

- sets_up_cn：说明本文采用人力资本视角的合理性。

- evidence_pointer：Section 2.2

### 28. Sec 2.2 P2

- order：28

- section：Section 2.2

- locator：Sec 2.2 P2

- move_code：GAP

- paraphrase_cn：现有行业分类研究基本忽略了企业的人力资本信息。

- rhetorical_function_cn：在理论综述后明确指出缺口头。

- depends_on_cn：步骤27

- sets_up_cn：为本文方法提供研究空间。

- evidence_pointer：Section 2.2

### 29. Sec 2.3 P3

- order：29

- section：Section 2.3

- locator：Sec 2.3 P3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：已有研究表明在线职业社交网络是研究和解决人力资源相关问题的可靠数据源。

- rhetorical_function_cn：论证数据源可靠性。

- depends_on_cn：步骤22

- sets_up_cn：指出该数据源尚未用于行业分析。

- evidence_pointer：Section 2.3

### 30. Sec 2.3 P3

- order：30

- section：Section 2.3

- locator：Sec 2.3 P3

- move_code：GAP

- paraphrase_cn：但没有已有工作利用在线职业社交网络数据进行行业分析。

- rhetorical_function_cn：明确数据层面的文献缺口。

- depends_on_cn：步骤29

- sets_up_cn：说明本文的方法选点。

- evidence_pointer：Section 2.3

### 31. Sec 2.4 P1-P3

- order：31

- section：Section 2.4

- locator：Sec 2.4 P1-P3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：社区检测是网络科学热点，适合大规模快速变化情形，且已被广泛使用。

- rhetorical_function_cn：引入技术知识基础。

- depends_on_cn：步骤22

- sets_up_cn：说明社区检测为何适用于行业簇发现。

- evidence_pointer：Section 2.4

### 32. Sec 2.4 P3

- order：32

- section：Section 2.4

- locator：Sec 2.4 P3

- move_code：GAP

- paraphrase_cn：文献检索未发现将社区检测技术应用于竞争情报或行业分析。

- rhetorical_function_cn：指出技术层面的文献缺口。

- depends_on_cn：步骤31

- sets_up_cn：为算法扩展提供研究空间。

- evidence_pointer：Section 2.4

### 33. Sec 2.4 P5-P6

- order：33

- section：Section 2.4

- locator：Sec 2.4 P5-P6

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：Sobolevsky等和Bae等的比较结果显示Louvain在质量和可扩展性上位居前列，且过程简单便于层次化扩展。

- rhetorical_function_cn：为后续选择Louvain提供依据。

- depends_on_cn：步骤32

- sets_up_cn：引出后文的层次化Louvain。

- evidence_pointer：Section 2.4

### 34. Sec 3 P1 S1

- order：34

- section：Section 3

- locator：Sec 3 P1 S1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：方法受RBV指导，基本事实是企业开始新业务时必须招聘相关领域人员。

- rhetorical_function_cn：将理论命题落实为设计逻辑。

- depends_on_cn：步骤27

- sets_up_cn：为劳动力流动网络定义做铺垫。

- evidence_pointer：Section 3 P1

### 35. Sec 3 P1 S2

- order：35

- section：Section 3

- locator：Sec 3 P1 S2

- move_code：MECHANISM

- paraphrase_cn：拥有某领域专长的人在相关领域企业间流动概率更高，例如Google员工更可能去Apple而非McDonald's。

- rhetorical_function_cn：用类比解释网络连接为何反映行业相似性。

- depends_on_cn：步骤34

- sets_up_cn：解释劳动力流动网络为何可聚类。

- evidence_pointer：Section 3 P1

### 36. Sec 3 P1 S3

- order：36

- section：Section 3

- locator：Sec 3 P1 S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：劳动力流动网络中节点表示企业，加权有向边表示从一家企业离职加入另一家企业的人数。

- rhetorical_function_cn：定义核心网络数据制品。

- depends_on_cn：步骤35

- sets_up_cn：为网络构造和社区发现提供对象。

- evidence_pointer：Section 3 P1

### 37. Sec 3 P2

- order：37

- section：Section 3

- locator：Sec 3 P2

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：由于行业类由数据自生成而非少量预定义类别，方法能覆盖更多业务维度并快速响应市场变化。

- rhetorical_function_cn：陈述预期收益，作为评价的靶点。

- depends_on_cn：步骤36

- sets_up_cn：为后续评价设定关注点。

- evidence_pointer：Section 3 P2

### 38. Sec 4 intro

- order：38

- section：Section 4

- locator：Sec 4 intro

- move_code：DESIGN_FEATURE

- paraphrase_cn：系统架构包含简历爬虫、网络构造器和行业分类器三大组件。

- rhetorical_function_cn：从整体上描述制品结构。

- depends_on_cn：步骤36

- sets_up_cn：指导各组件细节介绍。

- evidence_pointer：Section 4 intro, Fig 1

### 39. Sec 4.1 P2

- order：39

- section：Section 4.1

- locator：Sec 4.1 P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：爬虫集成Google API自动浏览专业社交网络并下载公开简历，过滤非工作相关内容。

- rhetorical_function_cn：描述数据采集组件的设计。

- depends_on_cn：步骤38

- sets_up_cn：说明数据获取的可行路径。

- evidence_pointer：Section 4.1

### 40. Sec 4.2.1

- order：40

- section：Section 4.2.1

- locator：Sec 4.2.1

- move_code：DESIGN_FEATURE

- paraphrase_cn：使用JSoup抽取工作经历，整理成(员工ID, 原企业, 新企业, 年份)形式的跳槽元组。

- rhetorical_function_cn：说明原始简历到跳槽记录的数据转换。

- depends_on_cn：步骤39

- sets_up_cn：为按企业聚合网络提供基础。

- evidence_pointer：Section 4.2.1

### 41. Sec 4.2.2

- order：41

- section：Section 4.2.2

- locator：Sec 4.2.2

- move_code：DESIGN_FEATURE

- paraphrase_cn：将个人跳槽记录聚合成企业级有向加权图，边权表示离职并在另一企业入职的人数。

- rhetorical_function_cn：描述核心构网步骤。

- depends_on_cn：步骤40

- sets_up_cn：为行业分类器输入准备网络。

- evidence_pointer：Section 4.2.2

### 42. Sec 4.3.1

- order：42

- section：Section 4.3.1

- locator：Sec 4.3.1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：Louvain目标为最大化模块度，高模块度表示同社区企业流动紧密、跨社区流动稀疏。

- rhetorical_function_cn：解释算法目标与网络结构含义。

- depends_on_cn：步骤41

- sets_up_cn：为层次化改进做铺垫。

- evidence_pointer：Section 4.3.1

### 43. Sec 4.3.2

- order：43

- section：Section 4.3.2

- locator：Sec 4.3.2

- move_code：DESIGN_FEATURE

- paraphrase_cn：原始Louvain会产生过多小社区；扩展算法合并社区为新节点并迭代运行，直到社区数达到目标规模，本文设为20。

- rhetorical_function_cn：说明为可解释性进行的算法修改。

- depends_on_cn：步骤42

- sets_up_cn：使分类结果可与传统方案比较。

- evidence_pointer：Section 4.3.2

### 44. Sec 4.4 P2

- order：44

- section：Section 4.4

- locator：Sec 4.4 P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：原型用Java、R和MySQL实现，实验在Windows桌面环境运行。

- rhetorical_function_cn：提供可复现实证环境。

- depends_on_cn：步骤43

- sets_up_cn：为数据与评价结果做准备。

- evidence_pointer：Section 4.4

### 45. Sec 4.5 P1-P2

- order：45

- section：Section 4.5

- locator：Sec 4.5 P1-P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：收集152万简历、574万工作记录、283万跳槽记录，并选择S&P 1500作为与企业财务数据匹配的比较样本。

- rhetorical_function_cn：说明数据规模与外部样本选择依据。

- depends_on_cn：步骤44

- sets_up_cn：为后续年度网络构造和比较提供基础。

- evidence_pointer：Section 4.5, Table 1

### 46. Sec 4.6.1

- order：46

- section：Section 4.6.1

- locator：Sec 4.6.1

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：用密度、模块度、聚类系数分析网络结构，以判断是否适合进一步行业识别。

- rhetorical_function_cn：建立网络结构有效性的评价指标。

- depends_on_cn：步骤45

- sets_up_cn：为网络分析结果提供判据。

- evidence_pointer：Section 4.6.1

### 47. Sec 4.6.2

- order：47

- section：Section 4.6.2

- locator：Sec 4.6.2

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：沿用Bhojraj、Hoberg & Phillips和Fang等的做法，用平均调整R2衡量行业分类对股票收益共同变动的解释力。

- rhetorical_function_cn：建立核心外部评价指标。

- depends_on_cn：步骤46

- sets_up_cn：为后续基准比较提供方法。

- evidence_pointer：Section 4.6.2

### 48. Sec 4.6.2

- order：48

- section：Section 4.6.2

- locator：Sec 4.6.2

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：进一步采用跨行业变异指标，认为分类结果产生的跨行业差异越大，信息量越高。

- rhetorical_function_cn：建立互补评价指标。

- depends_on_cn：步骤47

- sets_up_cn：为稳健性检验提供依据。

- evidence_pointer：Section 4.6.2

### 49. Sec 4.7.1, Table 2

- order：49

- section：Section 4.7.1

- locator：Sec 4.7.1, Table 2

- move_code：RESULT

- paraphrase_cn：网络分析显示密度、模块度和聚类系数均较高，中心公司逐年变化，说明网络信息丰富且具有动态性。

- rhetorical_function_cn：提供结构前提支持。

- depends_on_cn：步骤46

- sets_up_cn：进入行业簇质量评估。

- evidence_pointer：Section 4.7.1, Table 2

### 50. Sec 4.7.2, Table 3

- order：50

- section：Section 4.7.2

- locator：Sec 4.7.2, Table 3

- move_code：RESULT

- paraphrase_cn：4位博士生对20个行业簇的标注具有substantial agreement，Fleiss' kappa为0.7396，Top 5行业可解释。

- rhetorical_function_cn：提供人工可读的内容效度。

- depends_on_cn：步骤49

- sets_up_cn：为外部基准比较建立信心。

- evidence_pointer：Section 4.7.2, Table 3

### 51. Sec 4.7.3

- order：51

- section：Section 4.7.3

- locator：Sec 4.7.3

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：与SIC/NAICS/GICS、HP/FDD、INM/MO比较；为减少行业组数差异采用两位SIC、三位NAICS、六位GICS；HP/FDD结果直接引用原论文。

- rhetorical_function_cn：说明基准设置与复制限制。

- depends_on_cn：步骤47

- sets_up_cn：为核心比较结果做铺垫。

- evidence_pointer：Section 4.7.3

### 52. Sec 4.7.3, Fig 6, Table 4

- order：52

- section：Section 4.7.3

- locator：Sec 4.7.3, Fig 6, Table 4

- move_code：RESULT

- paraphrase_cn：LMN平均调整R2高于所有对比方法；相对GICS提高8.31%/4.67%，相对FDD提高1.23%/3.97%；并解释小增幅可能是因为行业效应接近上界。

- rhetorical_function_cn：给出核心性能主张并回应增幅小。

- depends_on_cn：步骤51

- sets_up_cn：确认算法选择和分类价值。

- evidence_pointer：Section 4.7.3, Fig 6, Table 4

### 53. Sec 4.7.3 after Table 4

- order：53

- section：Section 4.7.3

- locator：Sec 4.7.3 after Table 4

- move_code：RESULT

- paraphrase_cn：LMN优于INM和MO，说明选择Louvain做社区检测是有效的。

- rhetorical_function_cn：通过替代算法对照检验设计选择。

- depends_on_cn：步骤52

- sets_up_cn：为跨行业变异检验做过渡。

- evidence_pointer：Section 4.7.3

### 54. Sec 4.7.4, Fig 7, Table 5

- order：54

- section：Section 4.7.4

- locator：Sec 4.7.4, Fig 7, Table 5

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：跨行业变异比较显示LMN在销售、资产、销售增长、市场beta和资产beta上均高于SIC/NAICS/INM/MO，最低提升7.31%。

- rhetorical_function_cn：用互补指标增加结论稳健性。

- depends_on_cn：步骤48, 步骤52

- sets_up_cn：转入应用案例讨论。

- evidence_pointer：Section 4.7.4, Fig 7, Table 5

### 55. Sec 4.7.5 P1

- order：55

- section：Section 4.7.5

- locator：Sec 4.7.5 P1

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：层级化设计能揭示不同尺度行业结构，且人力资源视角可能早于年报提供企业进入新行业的信息。

- rhetorical_function_cn：将架构特性转化为可检验的实践预期。

- depends_on_cn：步骤43, 步骤54

- sets_up_cn：为两个案例做铺垫。

- evidence_pointer：Section 4.7.5

### 56. Google case, Fig 8

- order：56

- section：Section 4.7.5

- locator：Google case, Fig 8

- move_code：RESULT

- paraphrase_cn：2011年网络中Google与汽车社区有连接，而10-K直到2017年才提及自动驾驶项目。

- rhetorical_function_cn：用具体案例展示时间前向预警。

- depends_on_cn：步骤55

- sets_up_cn：提升外部效度。

- evidence_pointer：Section 4.7.5, Fig 8

### 57. Microsoft case, Fig 8

- order：57

- section：Section 4.7.5

- locator：Microsoft case, Fig 8

- move_code：RESULT

- paraphrase_cn：Microsoft与电子社区连接，Surface项目在2012年发布前3年已产生电子人才需求，而10-K披露晚于2012年。

- rhetorical_function_cn：作为第二个案例重复验证时间前向性。

- depends_on_cn：步骤56

- sets_up_cn：支持结论中的实践贡献。

- evidence_pointer：Section 4.7.5, Fig 8

### 58. Sec 5 P1

- order：58

- section：Conclusion

- locator：Sec 5 P1

- move_code：CONTRIBUTION

- paraphrase_cn：总结用设计科学方法解决时滞和人力资本缺失问题，构建自动行业分类架构并通过评价确认有效性。

- rhetorical_function_cn：回扣引言的问题与目标。

- depends_on_cn：步骤52-57

- sets_up_cn：引出理论贡献。

- evidence_pointer：Conclusion P1

### 59. Sec 5 P2

- order：59

- section：Conclusion

- locator：Sec 5 P2

- move_code：CONTRIBUTION

- paraphrase_cn：本文贡献于RBV，实证检验人力资源信息用于行业分析的有效性，认为劳动力流动视角能更细粒度和更及时地捕捉行业变化。

- rhetorical_function_cn：将性能优势升华为理论贡献。

- depends_on_cn：步骤58

- sets_up_cn：过渡到局限与未来研究。

- evidence_pointer：Conclusion P2

### 60. Sec 5 P3

- order：60

- section：Conclusion

- locator：Sec 5 P3

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：局限包括无法检测只需内部转岗的行业进入、样本行业分布不均、及时性未定量检验；未来可研究劳动力流动对企业绩效的影响。

- rhetorical_function_cn：限定边界并指出后续方向。

- depends_on_cn：步骤59

- sets_up_cn：结束全文。

- evidence_pointer：Conclusion P3

## 写作技术

- gap_construction_cn：先承认现有体系设计良好，再指出两个具体且可操作的限制（时滞和缺人力资本），随后将10-K文本方法同样归入滞后阵营，三处文献缺口（传统分类、线上社交网络未用于行业分析、社区检测未用于CI）叠加，使研究空间清晰。

- signposting_cn：摘要和引言末尾都有路线图；每个子系统/评估阶段均有‘本节将...’式开场；表格/图集中呈现比较结果。

- transition_logic_cn：从‘现有方案缺陷’到‘个人数据越来越可得’再到‘本文采用设计科学’是问题-机会-方案的过渡；从理论到构网再到算法是逐步操作化；从评价指标到结果再到案例是为了把性能差异转向使用价值。

- claim_evidence_rhythm_cn：每个设计决策后都紧跟一句预期收益或评价问题；评价部分按‘指标→对比对象→结果→解释’循环；对小幅提升给出行业效应接近上界的解释，避免读者将增幅小视为失败。

- benchmark_narrative_cn：选择评价指标时以既有研究为权威依据（Bhojraj、Hoberg & Phillips、Lamponi），将stock return co-movement确立为行业分类有效性的代理；再将HP/FDD作为state-of-the-art、INM/MO作为算法选择对照，形成‘传统方案—文本方法—替代算法—本文方法’的梯度对比。

- theory_return_cn：在结论部分把‘LMN表现更好’回译为‘用人力资源信息做行业分析是有效的’，并声明贡献于RBV；但正文并没有在分析中直接测量理论构念，理论回归相对简短。

- contribution_positioning_cn：定位为补充而非替代，既回应现实采用阻力，又保留现有分类体系地位；贡献分三层：制品、方法、实证证据。

- novelty_protection_cn：通过‘人力资源视角 + 时间前向案例 + 层次化扩展 + 大规模数据’的组合防止被解读为一次性性能结果；主动列明限制，避免理论承诺过强。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：写出现有方案的两个具体缺陷，并用规范性要求定义‘好的方案应该...’

- research_job_cn：确认目标领域既有方案、数据更新频率和缺失维度

- required_evidence_cn：能举出具体新兴行业或数据滞后案例，以及现有文本方法仍不足的证据

- transition_to_next_cn：指出更及时且含人力资本的新数据源

#### 2. 2

- step：2

- writing_job_cn：介绍新型数据源并说明其可靠性

- research_job_cn：获取或论证可获取的大规模数据，并做基本规模统计

- required_evidence_cn：数据量级、可匹配外部数据库、平台识别企业能力

- transition_to_next_cn：提出把数据转化为关系网络的设计

#### 3. 3

- step：3

- writing_job_cn：将理论命题转成设计要求和组件

- research_job_cn：构造网络并选择/扩展合适算法，设置可比的参数

- required_evidence_cn：算法可扩展性依据、目标社区数合理性、模块度指标

- transition_to_next_cn：先结构检验后外部检验

#### 4. 4

- step：4

- writing_job_cn：在评估开始前说明为什么用这些指标

- research_job_cn：运行网络结构分析和人工标注

- required_evidence_cn：模块度/聚类系数数值、标注者一致性

- transition_to_next_cn：建立外部基准

#### 5. 5

- step：5

- writing_job_cn：选择与既有文献一致的benchmark并展示对比

- research_job_cn：复现或引用基准结果，运行多个指标和样本

- required_evidence_cn：平均调整R2和跨行业变异及提升率；若无法复现要说明

- transition_to_next_cn：用案例展示实践后果

#### 6. 6

- step：6

- writing_job_cn：把性能结果提升为设计知识或理论贡献，并主动写限制

- research_job_cn：收集时间前向案例，确保案例能说明机制和边界

- required_evidence_cn：案例事件与现有信息渠道的时间差；反例/边界说明

- transition_to_next_cn：结束并指未来方向

### most_transferable_moves_cn

1. 用规范性的‘好方案应该...’引出缺陷

2. 把理论转为网络/关系表示

3. 多个互补指标交叉验证同一主张

4. 将性能提升回译为理论命题

5. 主动用‘补充而非替代’限定贡献

6. 用小而清晰的案例说明时间前向价值

### resource_intensive_or_nonstandard_parts_cn

1. 1.52M真实在线简历及爬取基础设施

2. 专业社交网络公开资料获取或购买

3. 与Compustat/Yahoo Finance的企业匹配

4. S&P 1500市场收益面板

5. 4位标注者与NAICS标签体系

6. HP/FDD原论文结果的使用

### what_not_to_copy_superficially_cn

1. 没有简历大数据时不能声称‘人力资本/劳动力流动视角’已实现

2. 没有金融收益共动指标时不能将社区发现结果称为‘更有效的行业分类’

3. 没有案例时间前向证据时不能声称‘及时揭示新行业进入’

4. 没有替代算法对照时不能宣称算法选择经过检验

- single_best_description_of_the_routine_cn：先指出现有分类方案的时滞与维度缺陷，再用新型大数据构建关系网络，以算法生成分类，最后用金融市场的共动指标和案例时间线证明分类的增量价值。

## 分析边界

全文完整可读，主要图表信息（Fig.1-8, Table 1-5）可由文本描述重建。未发现附录或在线补充材料；HP/FDD结果未在本文复现，因此部分比较依赖原论文数字；本文没有提供代码或数据可用性说明。分析基于论文文本的表面论证结构，无法验证作者实际编码与实验的隐藏细节。
