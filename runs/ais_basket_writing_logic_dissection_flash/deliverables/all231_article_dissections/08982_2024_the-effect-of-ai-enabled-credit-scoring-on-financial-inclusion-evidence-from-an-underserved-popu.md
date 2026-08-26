# The Effect of AI-Enabled Credit Scoring on Financial Inclusion: Evidence from an Underserved Population of over One Million

- 作者：Chunxiao Li; Hongchang Wang; Songtao Jiang; Bin Gu
- 年份 / 期刊：2024 / MIS Quarterly
- DOI：10.25300/misq/2024/18340
- 源文件：08982_2024_the-effect-of-ai-enabled-credit-scoring-on-financial-inclusion-evidence-from-an-underserved-popu.md
- 论文主类型：field_intervention_or_platform_experiment
- 主导写作弧线：phenomenon_mechanism_intervention_field_test
- 置信度：0.88

## 文章级论证概况

- 核心问题：在传统银行真实部署AI信用评分模型后，AI模型如何影响未被充分服务人群的金融包容性，具体表现为贷款审批率、违约率和利用率的变化，以及这种影响通过什么机制、在什么条件下成立？

- 制品与设计：研究分析的制品是一家国有区域性银行在某个个人贷款产品中实际部署的AI信用评分模型。该模型与原有传统规则模型并行使用，主要通过整合弱信号（社保、公积金、App金融行为、App非金融行为等数据域）和先进机器学习算法（多Learner+集成LightGBM）来提高违约风险预测精度，并借助决策矩阵决定最终审批结果。

- 客观结果：采用DID策略，使用930万申请样本发现：AI模型使未被充分服务人群的审批率提高约15个百分点（相对+89.3%），违约率降低0.9个百分点（相对-19.6%），同时提高整体利用率；被拒申请人的替代结果检验表明AI同时降低第一类和第二类错误；机制分解显示弱信号和先进算法共同提升预测精度，且对未被充分服务人群的边际贡献更大；缺失弱信号会减弱效果；简化版AI模型仍能显著改善金融包容性。

- 核心贡献：作者声称在理论上揭示了以提高预测精度为目标训练的AI信用评分模型可以增强金融包容性，机制是降低银行对传统强信号的依赖并减少统计歧视；在实践上展示了一种可在大型传统银行合规部署、可扩展且不牺牲贷款绩效的AI工具，并提供了模型开发、合规、实施和异质性影响的详细知识。

- 整篇论证链：作者从金融包容性作为社会正义基础的现实问题出发，指出传统信用评分过度依赖信用历史造成“先有鸡还是先有蛋”的困境，而现有扩展金融服务的做法成本高且难以规模化。AI信用评分模型因能使用弱信号和先进算法而可能解决这一困境，但也存在历史偏见、黑箱等担忧。为回答AI模型究竟如何影响金融包容性，作者与一家国有银行合作，利用该银行在一个个人贷款产品中试点部署AI模型、另一个相似产品未部署的准自然实验，构建DID。主结果发现AI模型显著提升未被充分服务人群的审批率并降低违约率，全样本违约率下降、利用率上升。随后作者通过分数分布分析、模拟模型比较、单数据域解释性分析和相关分析，把效果归因于弱信号与先进算法共同带来的个体层面预测精度改进，并与统计歧视理论一致。异质性分析显示缺失弱信号会减弱效果，AI也缩小了城市户籍、受雇、有信用历史等传统优势特征带来的审批优势。大量稳健性检验排除了平行趋势、选择效应、人工干预和未观测行为等威胁；合规分析和简化AI模拟进一步支持可推广性。最后作者回到理论贡献，强调AI可缓解统计歧视但不能解决结构性不公正。

## 类型与写作弧线判定

- 论文主类型判定：文章不是由作者在实验室构建制品，而是利用一家大型银行真实部署AI信用评分模型的准自然实验，通过比较同一银行内采用AI模型与未采用AI模型的相似个人贷款产品来识别因果效应，属于真实组织/平台中的数字设计干预与现场因果检验。

- 主导写作弧线判定：论文从金融排斥现象和统计歧视机制出发，将AI模型视为一种真实数字干预，在银行现场用DID检验其对金融包容性的影响，再深入机制、异质性、边界条件和稳健性，最后返回理论解释与实践含义。

## 研究开展程序

- study_or_phase_count：9

- 研究阶段总序列：第一阶段建立研究现场和对照组，说明AI模型在银行一个产品上试点、另一个相似产品作为对照；第二阶段用DID估计主效应；第三阶段用被拒申请人的替换贷款结果验证筛选质量；第四阶段用分数分布分析检验预测精度机制；第五阶段用模拟模型分解弱信号与先进算法的贡献；第六阶段用单数据域解释性和相关分析证明弱信号的增量信息；第七阶段分析异质性、缺失弱信号和统计歧视；第八阶段用相对时间模型、匹配、在线子样本、分支分析和安慰剂检验等做稳健性；第九阶段通过合规分析和简化AI模型模拟讨论可推广性，最后回到理论贡献和限制。

### studies_or_phases

#### 1. 现场识别与对照组构建

- order：1

- name_cn：现场识别与对照组构建

- question_cn：能否在同一银行内找到合适的处理产品和对照组，以识别AI信用评分模型对金融包容性的影响？

- inputs_and_setting_cn：中国某国有区域性银行；处理产品在2021年2月4日部署AI模型，控制产品未部署；样本为2020年10月1日至2021年4月30日的9,300,107个申请。

- designed_or_compared_object_cn：处理产品（传统模型+AI模型）与控制产品（仅传统模型）；处理产品中未被充分服务与常规人群对比。

- baseline_control_or_counterfactual_cn：控制产品在相同时期内的变化；处理产品部署前自身作为基线。

##### objective_metrics

1. 申请数量

2. 审批率

3. 违约率

4. 利用率

5. 信用额度

6. 申请人特征分布

- analysis_method_cn：制度建设分析、描述性统计、排除政策干扰期和人工评估申请。

- main_result_cn：部署前未被充分服务人群审批率约16.83%，常规人群约49.89%；处理产品与控制产品在未被充分服务申请人特征上相似；AI部署后描述统计显示审批率提升、违约率下降。

- argumentative_role_cn：建立DID所需的反事实基础和可信度，明确未被充分服务人群的操作化定义，排除部分混淆因素。

- remaining_uncertainty_cn：描述性差异可能由时间趋势、选择效应或银行其他行动造成，尚未得到因果估计。

- link_to_next_phase_cn：引向正式DID方程估计AI模型的审批率、违约率和利用率效应。

##### evidence_pointers

1. Data and Empirical Strategy: Research Setting

2. Table 1

3. Figure 1

4. Table 2

5. Table 3

6. Table A1

#### 2. 主DID效应分析

- order：2

- name_cn：主DID效应分析

- question_cn：RQ1：AI模型对未被充分服务人群的审批率、违约率和利用率有何影响？

- inputs_and_setting_cn：930万申请，其中处理产品250万申请，控制产品680万申请；贷款层面的违约和利用率数据约437万笔。

- designed_or_compared_object_cn：AI模型采纳虚拟变量（处理产品×部署后）；全样本、常规人群子样本、未被充分服务人群子样本。

- baseline_control_or_counterfactual_cn：控制产品部署前后变化；DID中的产品固定效应和时间固定效应。

##### objective_metrics

1. 审批率（Approval 1/0）

2. 违约率（Default 1/0）

3. 利用率（Utilization Level）

- analysis_method_cn：线性概率DID，公式(1)(2)，标准误聚类到申请日，控制申请人特征、模型更新、时间固定效应和产品固定效应。

- main_result_cn：全样本审批率变化不显著（-0.008），违约率显著下降-0.008，利用率显著上升0.058；未被充分服务人群审批率显著上升0.150，违约率显著下降-0.009；常规人群审批率下降但统计不显著；相对幅度分别为+89.3%和-19.6%。

- argumentative_role_cn：确立AI模型改善金融包容性的核心因果证据，同时显示贷款绩效未受损。

- remaining_uncertainty_cn：需要确认被拒申请人是否真的更差，以及效果是否来自更好的筛选而非申请人池变化。

- link_to_next_phase_cn：引向被拒人群的替代结果分析，以说明AI同时减少错误拒绝和错误批准。

##### evidence_pointers

1. Equations (1) and (2)

2. Table 4

3. Table 5

#### 3. 筛选绩效与被拒申请人反事实分析

- order：3

- name_cn：筛选绩效与被拒申请人反事实分析

- question_cn：AI模型是否真的改善了筛选质量，即被拒绝的申请人在其他金融机构的贷款表现是否更差？

- inputs_and_setting_cn：被处理产品或控制产品拒绝、但在一周内获得其他金融机构贷款的申请人，分别有80,252个常规申请和37,229个未被充分服务申请。

- designed_or_compared_object_cn：被处理产品拒绝的申请人 vs 被控制产品拒绝的申请人；被拒后的替代贷款违约率和利用率。

- baseline_control_or_counterfactual_cn：控制产品被拒申请人在AI部署前后的表现；使用DID框架。

##### objective_metrics

1. 替代贷款违约率

2. 替代贷款利用率

- analysis_method_cn：DID分析，以替代贷款结果作为反事实代理，控制申请人特征、时间固定效应、产品固定效应。

- main_result_cn：AI模型部署后，被处理产品拒绝的常规申请人和未被充分服务申请人的替代贷款违约率显著更高，利用率显著更低。

- argumentative_role_cn：证明AI模型同时降低第一类错误（错误批准）和第二类错误（错误拒绝），与统计歧视理论预测一致。

- remaining_uncertainty_cn：替代贷款结果只是代理，一周窗口假设申请人信用状况不变；其他金融机构的审批标准可能不同。

- link_to_next_phase_cn：引向预测精度的直接证据，解释为何能同时提高审批和降低违约。

##### evidence_pointers

1. Results: Main Impacts

2. Table 6

#### 4. 预测精度机制检验

- order：4

- name_cn：预测精度机制检验

- question_cn：AI模型的效果是否来自其对违约风险的预测精度提升？

- inputs_and_setting_cn：AI部署后申请人在传统模型和AI模型下的信用分数区间分布，以及各区间获批贷款的违约率。

- designed_or_compared_object_cn：传统模型分数分布 vs AI模型分数分布；常规人群 vs 未被充分服务人群。

- baseline_control_or_counterfactual_cn：传统模型的分数区间和违约率分布。

##### objective_metrics

1. 各分数区间申请人占比

2. 各分数区间违约率

3. 分数与违约率的相关性

- analysis_method_cn：描述性统计对比，观察分数区间改变和违约率单调性。

- main_result_cn：传统模型只给6.8%的未被充分服务人群620-850高分段，AI模型给到15.7%；AI模型分数与违约率的排序更一致，显著扩大各分数段差异，从而同时提高审批率和降低违约率。

- argumentative_role_cn：将审批率上升和违约率下降统一到“个体层面预测精度改善”这一机制上。

- remaining_uncertainty_cn：精度提升的来源尚未分离，需要判断是弱信号还是先进算法还是两者共同作用。

- link_to_next_phase_cn：引向数据域对比和模型分解分析。

##### evidence_pointers

1. Mechanisms: Prediction Accuracy

2. Table 7

#### 5. 弱信号与先进算法的贡献分解

- order：5

- name_cn：弱信号与先进算法的贡献分解

- question_cn：RQ2：AI模型预测精度的提升主要来自弱信号还是先进机器学习算法？

- inputs_and_setting_cn：处理产品传统模型的人工规则与特征域；AI模型的数据域（1-10）；测试期为2021年2月4日至4月30日的已批贷款。

- designed_or_compared_object_cn：真实传统模型、模拟传统模型+弱信号、真实AI模型；AI模型仅用强信号版本；AI模型用强信号+弱信号完整版本；以及模拟简化AI模型。

- baseline_control_or_counterfactual_cn：真实传统模型（仅强信号）为基线；比较加入弱信号、加入先进算法、两者同时加入的逐步贡献。

##### objective_metrics

1. AUC

2. KS

3. Top KS

4. 相对AUC改善百分比

- analysis_method_cn：模型对比模拟，分别隔离弱信号和先进算法的贡献，用AUC/KS评估排序能力。

- main_result_cn：弱信号可提高传统模型的预测精度；先进算法在相同强信号下也提高精度；两者结合提升最大；对未被充分服务人群的改善幅度大于常规人群；从强信号+AI到加入弱信号后的额外提升，未被充分服务人群为128个百分点，常规人群为43个百分点。

- argumentative_role_cn：把主效应归因于两个具体设计引擎，并解释为何未被充分服务人群受益更大。

- remaining_uncertainty_cn：需要确认弱信号是否确实包含未被强信号覆盖的增量信息，以及哪些亚组受影响。

- link_to_next_phase_cn：引向弱信号增量预测力的进一步验证。

##### evidence_pointers

1. Mechanisms: Data Domains

2. Table 8

3. Table 9

4. Table A2

5. Table A3

6. Table A4

7. Table A5

#### 6. 弱信号增量预测力验证

- order：6

- name_cn：弱信号增量预测力验证

- question_cn：弱信号是否在强信号之外提供真正有价值且不冗余的违约预测信息？

- inputs_and_setting_cn：所有10个数据域的特征；AI模型分别只用单一数据域训练；PCA主成分用于相关分析。

- designed_or_compared_object_cn：单数据域AI模型的表现：黑名单、身份信息、收入资产、逾期信贷、信贷申请、信贷使用、社保、公积金、App金融、App非金融。

- baseline_control_or_counterfactual_cn：强信号数据域（1-6）作为参照；随机/无信息基线AUC=50。

##### objective_metrics

1. K-S

2. AUC

3. 数据域间相关系数

- analysis_method_cn：单数据域可解释性方法；PCA降维后计算相关系数矩阵。

- main_result_cn：弱信号数据域的AUC在55-68之间，与强信号域接近，具有可观的预测力；弱信号与多数强信号相关性低，说明提供额外信息。

- argumentative_role_cn：进一步支持弱信号不是强信号的简单代理，而是真正增加预测精度的信息源。

- remaining_uncertainty_cn：需要检验效果是否在不同亚组间均匀，以及AI是否减少对群体特征的依赖。

- link_to_next_phase_cn：引向异质性、缺失弱信号和统计歧视分析。

##### evidence_pointers

1. Additional Predictive Power of Weak Signals

2. Table 10

3. Table 11

#### 7. 异质性、缺失弱信号与统计歧视分析

- order：7

- name_cn：异质性、缺失弱信号与统计歧视分析

- question_cn：RQ3：AI模型效果在哪些亚组中成立？缺失弱信号如何影响效果？AI是否减少了统计歧视？

- inputs_and_setting_cn：基于五条未被充分服务标准的五个子样本；缺失弱信号数据域哑变量；与自雇、城市户籍、有信用历史的交互项。

- designed_or_compared_object_cn：各子样本的DID系数；AI模型×缺失弱信号的交互；AI模型×关键强信号优势特征的交互。

- baseline_control_or_counterfactual_cn：无交互时AI模型主效应；未被充分服务人群中的基础DID；部署前这些特征的优势系数。

##### objective_metrics

1. 审批率系数

2. 违约率系数

3. 交互项系数

- analysis_method_cn：子样本DID，附加交互项的DID回归。

- main_result_cn：AI提升四个未被充分服务亚组的审批率（无永久居所除外），降低所有亚组违约率；缺失弱信号降低审批率影响但仍为正；部署后城市户籍、受雇、有信用历史的审批优势显著缩小，在未被充分服务人群中优势缩小27.3%-52.0%。

- argumentative_role_cn：建立效果的边界条件，并将结果与统计歧视理论直接连接。

- remaining_uncertainty_cn：识别威胁仍需排除；未检验其他银行或简化模型的推广性。

- link_to_next_phase_cn：引向稳健性检验和可推广性分析。

##### evidence_pointers

1. Heterogeneous Impacts and Statistical Discrimination

2. Table 12

3. Table 13

4. Table 14

#### 8. 稳健性检验与竞争解释排除

- order：8

- name_cn：稳健性检验与竞争解释排除

- question_cn：主结果是否受平行趋势、产品选择、申请人选择、人工干预、未观测行动等威胁影响？

- inputs_and_setting_cn：原样本、缩短时间窗口子样本、匹配样本、线上申请子样本、分行大小子样本、部署前伪处理日期样本。

- designed_or_compared_object_cn：相对时间哑变量；coarsened exact matching；线上渠道；分支大小；三种伪治疗日期。

- baseline_control_or_counterfactual_cn：相对时间-1作为基线；未处理控制产品；匹配后均衡样本。

##### objective_metrics

1. 审批率系数

2. 违约率系数

3. 利用率系数

4. 伪处理系数

- analysis_method_cn：相对时间（leads/lags）模型；匹配样本DID；线上子样本DID；分行子样本DID；安慰剂检验。

- main_result_cn：审批率和违约率在部署前无显著异质性趋势；匹配样本、线上样本、分行样本结果一致；安慰剂检验伪处理效应很小且对违约率为正，无法模拟AI“同时提高审批和降低违约”的组合结果。

- argumentative_role_cn：保护DID因果解释，排除产品选择、申请人池变化、人工评估和未观测政策响应等替代解释。

- remaining_uncertainty_cn：所有稳健性仍基于同一银行同一时期；外部推广需要模拟和合规分析。

- link_to_next_phase_cn：引向合规与简化AI模型的推广性分析。

##### evidence_pointers

1. Robustness Checks

2. Equation (3)

3. Table 15

4. Table 16

5. Table A6

6. Table A7

7. Table A8

8. Table A9

9. Table A10

10. Table A11

#### 9. 合规性与可推广性模拟

- order：9

- name_cn：合规性与可推广性模拟

- question_cn：在缺乏复杂IT能力或全部弱信号数据的情况下，简化AI模型是否仍能改善金融包容性？合规约束下如何可行？

- inputs_and_setting_cn：合规法律（CCPA、GDPR、ECOA、GLBA等）与银行实践；简化AI模型变体：单Learner、仅一个弱信号数据域。

- designed_or_compared_object_cn：真实AI模型 vs 简化AI模型（单Learner；仅社保；仅公积金；仅App金融；仅App非金融）；合规实践映射。

- baseline_control_or_counterfactual_cn：真实AI模型的结果；传统模型无AI时的反事实。

##### objective_metrics

1. 审批率系数

2. 违约率系数

3. 合规措施覆盖

- analysis_method_cn：模拟部署简化AI模型并重新估计DID；对照法律法规整理合规方案。

- main_result_cn：简化AI模型仍能显著提高未被充分服务人群审批率3.3%-8.6%，降低违约率0.2%-0.4%；银行在数据许可、隐私、受保护特征、结果公平、透明性等方面有明确合规做法。

- argumentative_role_cn：支持结果向能力较弱、数据较少但具有基础AI能力的金融机构推广，回应可推广性担忧。

- remaining_uncertainty_cn：模拟依赖于训练数据与真实部署相同的假设；不同法律环境下合规路径可能不同；长期效果未知。

- link_to_next_phase_cn：引向讨论中的理论贡献、结构性歧视边界和未来研究。

##### evidence_pointers

1. Compliance and Generalizability

2. Table 17

3. Table 18

4. Table A12

## 各部分修辞架构

### abstract_moves

1. RQ_OR_OBJECTIVE

2. CONTEXT

3. GAP

4. METHOD_JUSTIFICATION

5. RESULT

6. MECHANISM

7. ROBUSTNESS_OR_BOUNDARY_TEST

8. CONTRIBUTION

### introduction_moves

1. CONTEXT

2. PRACTICAL_STAKES

3. PHENOMENON

4. WHY_GAP_MATTERS

5. LIMITATION

6. THEORY_INTRO

7. MECHANISM

8. RQ_OR_OBJECTIVE

9. STUDY_OVERVIEW

10. METHOD_JUSTIFICATION

11. RESULT

12. ROBUSTNESS_OR_BOUNDARY_TEST

13. CONTRIBUTION

14. LIMITATION_AND_FUTURE

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE

2. PHENOMENON

3. LIMITATION

4. GAP

5. THEORY_INTRO

6. MECHANISM

7. HYPOTHESIS_OR_PROPOSITION

### artifact_design_moves

1. CONTEXT

2. DESIGN_FEATURE

3. METHOD_JUSTIFICATION

4. BENCHMARK_OR_CONTRAST

5. REQUIREMENT

### evaluation_moves

1. METHOD_JUSTIFICATION

2. BENCHMARK_OR_CONTRAST

3. RESULT

4. MECHANISM

5. ROBUSTNESS_OR_BOUNDARY_TEST

6. BOUNDARY_CONDITION

### discussion_and_contribution_moves

1. CONTEXT

2. RESULT

3. MECHANISM

4. CONTRIBUTION

5. BOUNDARY_CONDITION

6. LIMITATION_AND_FUTURE

## 理论/知识到设计的翻译

### 知识/理论基础

1. 金融包容性与社会正义文献

2. AI在借贷中的应用文献

3. 弱信号/替代数据文献

4. 统计歧视理论

5. 机器学习信用评分工程实践

- 理论—设计耦合：partial

- 耦合判定理由：文章中的AI模型并非作者根据某种理论前瞻性设计出来的，而是银行在政策驱动和工程实践中开发的；作者事后用弱信号概念和统计歧视理论来概念化、归因和解释该人工制品的特征。理论影响了研究变量、数据域分类、机制解释和边界分析，但具体技术选择（如LightGBM、两层级联、决策矩阵）主要来自银行数据科学团队的工程实践。

- 理论到设计翻译链：传统模型因过度依赖信用历史等强信号而对缺少强信号的未被充分服务人群形成统计歧视；要减少这种歧视，就需要在个体层面更准确地预测违约风险。弱信号文献指出非传统、含噪的数据能提供还款意愿和能力的信息；机器学习文献指出先进算法能处理复杂非线性关系和自动生成特征。因此，AI模型的设计选择是纳入强信号+弱信号（社保、公积金、App金融和行为数据），使用LightGBM多个体学习器和集成学习器，并在部署时与传统模型形成决策矩阵；评价设计则用DID估计审批/违约/利用率，用AUC/KS分解弱信号和算法的贡献，用交互项检验统计歧视是否减弱。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：未被充分服务人群经常缺乏强信号；传统模型依赖强信号会把群体平均风险用于个体，造成统计歧视。

- mechanism_cn：传统模型无法精确评估个体信用，只能依赖群体特征，导致未被充分服务人群被系统性拒绝。

- design_requirement_cn：应使用能提供个体层面违约预测的信息和算法，减少对传统强信号的依赖。

- artifact_choice_cn：AI模型纳入弱信号数据域并使用先进机器学习算法预测个体违约风险。

- evaluated_contrast_cn：传统模型 vs AI模型的分数分布、审批率、违约率；未被充分服务 vs 常规人群。

- objective_result_cn：未被充分服务人群审批率相对+89.3%，违约率相对-19.6%；AI模型给出更合理的分数分布。

##### evidence_pointers

1. Table 5

2. Table 7

#### 2. 2

- theory_or_knowledge_claim_cn：弱信号指非传统、含噪但与还款意愿/能力有关的数据，在传统模型下因难以解释、噪声大、缺失多而被弃用。

- mechanism_cn：弱信号提供强信号之外的信息，特别是当强信号缺失时，可以更全面刻画申请人。

- design_requirement_cn：需要引入弱信号数据域，并用特征工程技术将其转化为可用的预测特征。

- artifact_choice_cn：AI模型使用社保、公积金、App金融行为、App非金融行为四个弱信号数据域，并通过NLP、时间序列、知识图谱等技术生成特征。

- evaluated_contrast_cn：传统模型仅用强信号 vs 模拟传统模型+弱信号；单数据域AI模型表现；弱信号与强信号相关性。

- objective_result_cn：加入弱信号后传统模型AUC从未被充分服务人群0.57提升到0.67；弱信号域AUC最高68，且与强信号相关低。

##### evidence_pointers

1. Table 8

2. Table 10

3. Table 11

4. Table A2

5. Table A3

#### 3. 3

- theory_or_knowledge_claim_cn：先进机器学习算法可以发现复杂特征交互和非线性关联，比人工规则更有效。

- mechanism_cn：算法能从原始数据自动生成新颖特征并连接特征与信用风险，提升个体层面精度。

- design_requirement_cn：应采用具有复杂函数逼近能力的算法，并将多个模型集成以利用不同特征组。

- artifact_choice_cn：AI模型采用四个LightGBM个体学习器+一个LightGBM集成学习器的两层结构。

- evaluated_contrast_cn：传统模型 vs AI模型仅用相同强信号；真实AI模型 vs 简化AI模型。

- objective_result_cn：相同强信号下AI模型AUC显著高于传统模型；先进算法的贡献比弱信号更大；完整AI模型效果最好。

##### evidence_pointers

1. Table 9

2. Table A4

3. Table A5

#### 4. 4

- theory_or_knowledge_claim_cn：统计歧视理论认为，当个体特征无法精确观测时，决策者会使用群体特征，导致少数群体被差别对待。

- mechanism_cn：如果AI提高个体预测精度，银行对群体特征（城市/受雇/有信用历史）的依赖会下降，从而减少统计歧视。

- design_requirement_cn：模型应避免使用受保护特征，训练样本覆盖全部人群，并且在部署后持续监测边际化亚组影响。

- artifact_choice_cn：AI模型去除与性别、残疾等受保护特征相关的变量；训练数据保留自然比例；采用决策矩阵允许AI推翻传统模型建议。

- evaluated_contrast_cn：AI部署前后，城市户籍、自雇状态、有信用历史三个特征的审批优势变化。

- objective_result_cn：这三个传统优势特征的审批优势显著缩小，在未被充分服务人群中缩小27.3%-52.0%。

##### evidence_pointers

1. Table 14

2. Development and Implementation of the AI Model

3. Figure 3

## 评价逻辑

### evaluation_modes

1. 产品级准自然实验DID

2. 被拒申请人替代结果反事实分析

3. 分数分布描述性对比

4. 模型模拟与AUC/KS机制分解

5. 单数据域可解释性分析

6. PCA相关结构分析

7. 子样本异质性DID

8. 相对时间平行趋势检验

9. 匹配样本DID

10. 线上渠道子样本DID

11. 分行规模子样本分析

12. 安慰剂检验

13. 简化AI模型模拟

- why_these_evaluations_cn：单一DID只能回答平均处理效应，无法确证机制、边界和推广性。因此作者先以DID建立总效应；接着用被拒人群替代结果确认筛选质量的提升；再通过分数分布、模型模拟和单数据域分析打开“预测精度”黑箱；用异质性分析和交互项检验统计歧视机制；用平行趋势、匹配、线上样本、安慰剂等排除竞争解释；最后用简化模型模拟和合规分析论证推广性。

- benchmark_and_contrast_chain_cn：基准始终是传统规则模型/控制产品。作者逐步叠加对照：控制产品作为DID基准；传统模型分数作为预测精度基准；传统模型仅用强信号作为机制分解基准；真实AI模型作为简化AI模型的基准；未部署AI的反事实作为稳健性基准。每一个后续分析都建立在前一个分析发现的“未解释之处”上。

### claim_evidence_ledger

#### 1. AI模型提升未被充分服务人群审批率并降低违约率

- claim_cn：AI模型提升未被充分服务人群审批率并降低违约率

- evidence_cn：Table 5 DID系数：审批率0.150***，违约率-0.009***

- status_cn：有直接统计证据支持

#### 2. AI模型同时减少第一类和第二类错误

- claim_cn：AI模型同时减少第一类和第二类错误

- evidence_cn：Table 6 被拒申请人替代贷款违约率上升、利用率下降

- status_cn：有代理证据支持，但依赖替代贷款假设

#### 3. 效果来源于AI模型预测精度提升

- claim_cn：效果来源于AI模型预测精度提升

- evidence_cn：Table 7 分数分布更合理，违约率与分数段单调性改善

- status_cn：有描述性证据支持

#### 4. 弱信号和先进算法共同驱动预测精度提升

- claim_cn：弱信号和先进算法共同驱动预测精度提升

- evidence_cn：Table 9、Table A2、Table A4的AUC/KS对比

- status_cn：有模拟对比证据支持

#### 5. 弱信号具有增量信息

- claim_cn：弱信号具有增量信息

- evidence_cn：Table 10单域AUC较高，Table 11与强信号相关低

- status_cn：有证据支持

#### 6. AI减少统计歧视

- claim_cn：AI减少统计歧视

- evidence_cn：Table 14 城市/受雇/信用历史优势缩小

- status_cn：有间接证据支持，缺少直接歧视度量

#### 7. 缺失弱信号时效果减弱

- claim_cn：缺失弱信号时效果减弱

- evidence_cn：Table 13交互项显著为负

- status_cn：有证据支持

#### 8. DID因果识别有效

- claim_cn：DID因果识别有效

- evidence_cn：Table 15平行趋势；Table 16多种稳健性，附录A6-A11

- status_cn：有较强支持，但非随机实验

#### 9. 简化AI模型也能改善金融包容性

- claim_cn：简化AI模型也能改善金融包容性

- evidence_cn：Table 18模拟系数仍显著为正

- status_cn：有模拟证据支持，非真实部署

- internal_validity_strategy_cn：使用DID并控制产品/时间固定效应；排除政策干扰期、人工评估申请；用相对时间模型检验平行趋势；用匹配样本、线上申请、短时间窗口、分行子样本排除申请人池变化和人工干预；用安慰剂检验排除未观测行动。

- external_validity_strategy_cn：大样本930万申请覆盖大规模真实银行；用机制分析解释为何在一般AI逻辑下成立；用简化AI模型模拟说明对IT能力较弱机构的可迁移性；用合规表连接不同法域；同时讨论亚组缺失弱信号和结构性歧视等边界条件。

- what_is_not_actually_tested_cn：AI模型并非随机分配，产品选择可能仍有不可观测偏差；被拒申请人的贷款结果来自其他机构，只是代理；简化AI模型是模拟而非真实部署；未检验AI对长期信用积累、福利、就业等最终社会结果的影响；统计歧视减少是通过特征权重变化间接推断的，没有直接测量歧视；未检验其他银行、其他产品、其他国家的可复制性。

## 贡献闭环

- technical_claim_cn：一个使用弱信号和先进机器学习算法的AI信用评分模型能在真实传统银行环境中提高违约预测精度，并同时提升未被充分服务人群的审批率和降低违约率。

- artifact_claim_cn：具体设计特征是关键：弱信号数据域提供了强信号之外的增量信息；LightGBM多个体+集成结构能够利用弱信号生成复杂特征并连接信用风险；AI与传统模型共同使用的决策矩阵使AI可以推翻传统决策。

- mechanism_claim_cn：AI模型通过提高个体层面预测精度，减少银行对传统强信号和群体特征的依赖，从而缓解统计歧视；弱信号和先进算法是两个独立且互补的驱动引擎。

- boundary_claim_cn：效果在未被充分服务人群中更强；缺失一个或多个弱信号数据域会减弱审批率提升；无永久居所的亚组审批率没有显著提升；简化模型效果较弱但仍显著；AI不能解决结构性社会不公正，只能缓解统计歧视。

- reusable_design_knowledge_cn：可复用的设计知识包括：应纳入弱信号数据域并针对不同数据类型采用NLP/时间序列/知识图谱等特征生成方法；应采用多个个体学习器+集成学习器提高精度和可解释性；应在训练后审查并删除受保护特征；应使用AI与传统模型共存的决策矩阵以符合监管；应对边际化亚组进行持续监测；简化的单算法或单弱信号域模型也具有经济价值。

- theoretical_contribution_cn：扩展了AI与社会正义文献，表明以提高预测精度为目标的AI模型可以增强金融包容性；将AI信用评分与统计歧视理论连接起来，说明个体预测精度提升如何降低群体特征依赖；回应了关于AI偏见和黑箱的担忧，同时指出其无法解决结构性不公正。

- how_discussion_closes_intro_gap_cn：讨论部分重新连接引言中“AI可能促进也可能损害金融包容”的开放问题，用DID证据给出明确答案，用机制分析回答“为什么有效”，用异质性和边界分析回答“对谁有效、何时失效”，并用简化模型和合规分析回应“其他机构能否复制”的推广性质疑。

- overclaim_or_unsupported_leaps_cn：可能存在以下跳跃：将被拒申请人替代贷款表现解释为真实反事实；将特征交互项变化直接等同于统计歧视减少；将单银行单产品结果推广到一般AI信用评分；将模拟简化模型的效果等同于实际部署效果；对“提高预测精度→降低群体依赖”的机制主要依赖描述性和模拟证据，而非随机操纵。

## 句级写作动作图谱

### 1. Abstract P1 S1

- order：1

- section：Abstract

- locator：Abstract P1 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：研究一家大型银行采用AI信用评分模型对未被充分服务人群金融包容性的影响，指标是审批率、违约率和利用率。

- rhetorical_function_cn：开篇给出研究目标和结果变量，让读者立即知道论文要回答什么。

- depends_on_cn：无。

- sets_up_cn：为整篇论文的核心问题定调。

- evidence_pointer：Abstract第一句

### 2. Abstract P1 S2

- order：2

- section：Abstract

- locator：Abstract P1 S2

- move_code：CONTEXT

- paraphrase_cn：银行服务超过五千万客户，过去用传统规则模型评估贷款违约风险，最近开发了更高精度的AI模型并同时用于一个个人贷款产品。

- rhetorical_function_cn：交代研究对象和制度背景，说明AI模型与传统模型并存。

- depends_on_cn：上一句的AI采用背景。

- sets_up_cn：为后文DID和机制分析提供场景。

- evidence_pointer：Abstract第二句

### 3. Abstract P1 S3

- order：3

- section：Abstract

- locator：Abstract P1 S3

- move_code：GAP

- paraphrase_cn：尽管AI模型可能更准确地估计违约风险，但关于它对金融包容性的影响知之甚少。

- rhetorical_function_cn：指出现有知识的缺口。

- depends_on_cn：前一句介绍AI优势。

- sets_up_cn：引出研究动机。

- evidence_pointer：Abstract第三句

### 4. Abstract P1 S4

- order：4

- section：Abstract

- locator：Abstract P1 S4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者用DID比较采用了AI模型的产品与未采用AI模型的相似个人贷款产品在金融包容性上的变化。

- rhetorical_function_cn：说明识别策略，让读者相信因果推断的可行性。

- depends_on_cn：研究场景中存在处理和对照产品。

- sets_up_cn：为后续实证分析作方法论预告。

- evidence_pointer：Abstract第四句

### 5. Abstract P1 S5

- order：5

- section：Abstract

- locator：Abstract P1 S5

- move_code：RESULT

- paraphrase_cn：发现AI模型同时提高未被充分服务人群的审批率并降低违约率。

- rhetorical_function_cn：给出核心发现。

- depends_on_cn：DID方法。

- sets_up_cn：为解释机制和贡献铺路。

- evidence_pointer：Abstract第五句

### 6. Abstract P1 S6

- order：6

- section：Abstract

- locator：Abstract P1 S6

- move_code：MECHANISM

- paraphrase_cn：进一步分析把金融包容性改善归因于AI模型使用弱信号和先进机器学习算法。

- rhetorical_function_cn：从结果深入机制。

- depends_on_cn：核心结果。

- sets_up_cn：预告机制分析章节。

- evidence_pointer：Abstract第六句

### 7. Abstract P1 S7

- order：7

- section：Abstract

- locator：Abstract P1 S7

- move_code：THEORY_PROPOSITION

- paraphrase_cn：结果与统计歧视理论一致：个体层面预测精度提高会减少对导致金融排斥的群体特征的依赖。

- rhetorical_function_cn：把实证结果上升到理论解释。

- depends_on_cn：机制发现。

- sets_up_cn：为讨论部分理论贡献作伏笔。

- evidence_pointer：Abstract第七句

### 8. Abstract P1 S8

- order：8

- section：Abstract

- locator：Abstract P1 S8

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：作者阐述AI模型的开发过程，并发现效果在不同亚组间有异质性，缺失弱信号的人群审批率改善较小；模拟显示简化AI模型也能提高审批率并降低违约率。

- rhetorical_function_cn：预告异质性和可推广性分析，强化贡献的边界意识。

- depends_on_cn：机制和主结果。

- sets_up_cn：为正文中的异质性、模拟和推广性章节铺垫。

- evidence_pointer：Abstract第八至九句

### 9. Abstract P1 S10

- order：9

- section：Abstract

- locator：Abstract P1 S10

- move_code：CONTRIBUTION

- paraphrase_cn：研究为AI设计如何通过提升预测精度增强金融包容性提供理论实践意义，与社会正义相关。

- rhetorical_function_cn：总结贡献。

- depends_on_cn：全文结果。

- sets_up_cn：无后续，是摘要的收束。

- evidence_pointer：Abstract最后一句

### 10. Intro P1 S1

- order：10

- section：Introduction

- locator：Intro P1 S1

- move_code：CONTEXT

- paraphrase_cn：金融包容性指个人和企业能够负责任且可持续地获得有用、可负担的金融产品和服务。

- rhetorical_function_cn：给出核心概念的定义。

- depends_on_cn：无。

- sets_up_cn：为后续讨论金融排斥问题提供概念基础。

- evidence_pointer：Introduction第一段

### 11. Intro P2 S1-S3

- order：11

- section：Introduction

- locator：Intro P2 S1-S3

- move_code：PRACTICAL_STAKES

- paraphrase_cn：金融包容性是社会正义的重要驱动力，影响就业、教育、医疗和住房等广泛结果。

- rhetorical_function_cn：强调研究问题的现实重要性。

- depends_on_cn：概念定义。

- sets_up_cn：让读者理解为什么金融包容性值得研究。

- evidence_pointer：Introduction第二段

### 12. Intro P3 S1-S3

- order：12

- section：Introduction

- locator：Intro P3 S1-S3

- move_code：PHENOMENON

- paraphrase_cn：金融包容性的主要障碍是缺乏信用历史，传统评分依赖信用历史，未被充分服务人群因此难以获得资本，形成“鸡和蛋”问题。

- rhetorical_function_cn：刻画核心经验现象。

- depends_on_cn：概念和重要性。

- sets_up_cn：为AI模型作为潜在解法的引入提供问题基础。

- evidence_pointer：Introduction第三段

### 13. Intro P4 S1-S3

- order：13

- section：Introduction

- locator：Intro P4 S1-S3

- move_code：LIMITATION

- paraphrase_cn：现有提高金融包容性的方法包括开分支、降低门槛、设计特定产品，但运营成本高、违约风险高且难以规模化。

- rhetorical_function_cn：指出已有解决方案的不足。

- depends_on_cn：前段描述的金融排斥问题。

- sets_up_cn：说明需要新的可扩展方案。

- evidence_pointer：Introduction第四段

### 14. Intro P4 S4

- order：14

- section：Introduction

- locator：Intro P4 S4

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：因此，寻找一种能在低成本下大规模增强金融包容性的解决方案至关重要且迫切。

- rhetorical_function_cn：说明研究缺口的重要性和紧迫性。

- depends_on_cn：前述限制。

- sets_up_cn：引入AI作为潜在答案。

- evidence_pointer：Introduction第四段最后一句

### 15. Intro P5 S1

- order：15

- section：Introduction

- locator：Intro P5 S1

- move_code：THEORY_INTRO

- paraphrase_cn：信息技术进步，特别是机器学习、大数据和AI，为解决金融包容性问题提供了新途径。

- rhetorical_function_cn：引入AI信用评分作为研究对象。

- depends_on_cn：前面的现实问题。

- sets_up_cn：引出AI模型的两个优势。

- evidence_pointer：Introduction第五段第一句

### 16. Intro P5 S2-S3

- order：16

- section：Introduction

- locator：Intro P5 S2-S3

- move_code：MECHANISM

- paraphrase_cn：相比传统规则模型，AI模型可以纳入更广泛的弱信号，并利用先进算法发现复杂关系，因此预测精度更高，对缺乏强信号的未被充分服务人群更有利。

- rhetorical_function_cn：提出AI改善金融包容性的理论机制。

- depends_on_cn：AI引入。

- sets_up_cn：为后文“弱信号+先进算法”机制分析做铺垫。

- evidence_pointer：Introduction第五段第二至三句

### 17. Intro P5 S4-S5

- order：17

- section：Introduction

- locator：Intro P5 S4-S5

- move_code：LIMITATION

- paraphrase_cn：AI模型也有数据相关和模型相关担忧，如历史偏见、新数据域带来的新歧视、黑箱问题。

- rhetorical_function_cn：平衡论证，引入不确定性。

- depends_on_cn：AI优势。

- sets_up_cn：说明为什么需要实证检验而非直接假设AI有效。

- evidence_pointer：Introduction第五段后半

### 18. Intro P6 S1-S4

- order：18

- section：Introduction

- locator：Intro P6 S1-S4

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：鉴于AI的承诺和陷阱，作者提出三个研究问题：处理效应、机制、理论边界。

- rhetorical_function_cn：正式列出研究问题。

- depends_on_cn：前段权衡。

- sets_up_cn：组织整篇文章的实证结构。

- evidence_pointer：Introduction第六段

### 19. Intro P7 S1-S4

- order：19

- section：Introduction

- locator：Intro P7 S1-S4

- move_code：STUDY_OVERVIEW

- paraphrase_cn：作者与一家国有银行合作，该银行根据政策在一个人贷产品中开发并测试AI模型，同时识别出类似的控制产品，使用DID估计影响。

- rhetorical_function_cn：说明研究设计和数据来源。

- depends_on_cn：研究问题。

- sets_up_cn：为实证部分提供场景。

- evidence_pointer：Introduction第七段

### 20. Intro P8 S1-S3

- order：20

- section：Introduction

- locator：Intro P8 S1-S3

- move_code：RESULT

- paraphrase_cn：样本包括七个月和九百万申请；AI模型提高了未被充分服务人群审批率，降低了双方违约率，并提高全体利用率。

- rhetorical_function_cn：提前给出核心结论。

- depends_on_cn：DID设计。

- sets_up_cn：吸引读者继续看证据。

- evidence_pointer：Introduction第八段前半

### 21. Intro P8 S4-S6

- order：21

- section：Introduction

- locator：Intro P8 S4-S6

- move_code：MECHANISM

- paraphrase_cn：金融包容性改善来自AI模型用弱信号和先进算法提升预测精度，组合带来最大改进，且对未被充分服务人群受益更多。

- rhetorical_function_cn：在摘要之外更详细预告机制。

- depends_on_cn：核心结果。

- sets_up_cn：为机制章节铺垫。

- evidence_pointer：Introduction第八段后半

### 22. Intro P8 S7-S8

- order：22

- section：Introduction

- locator：Intro P8 S7-S8

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：AI影响存在异质性，几乎所有未被充分服务亚组都受益；缺失弱信号时效果更小；模拟表明简化AI模型仍有效。

- rhetorical_function_cn：预告异质性和推广性。

- depends_on_cn：核心结果和机制。

- sets_up_cn：为正文相应章节作铺垫。

- evidence_pointer：Introduction第八段后半

### 23. Intro P9 S1-S4

- order：23

- section：Introduction

- locator：Intro P9 S1-S4

- move_code：CONTRIBUTION

- paraphrase_cn：作者声称对AI与社会正义文献做出理论贡献，展示以提高预测精度为目标的AI可以增强金融包容性，并减少银行对强信号的依赖。

- rhetorical_function_cn：在引言结尾声明理论贡献。

- depends_on_cn：全文结果。

- sets_up_cn：与讨论部分呼应。

- evidence_pointer：Introduction第九段前半

### 24. Intro P9 S5-S8

- order：24

- section：Introduction

- locator：Intro P9 S5-S8

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：作者也指出AI不是所有申请人都受益，不能解决结构性社会不公正，政策制定者需要更多证据和监管。

- rhetorical_function_cn：提前设定边界条件。

- depends_on_cn：贡献声明。

- sets_up_cn：为讨论部分限制做预告。

- evidence_pointer：Introduction第九段后半

### 25. Financial Inclusion and Social Justice P2 S1-S3

- order：25

- section：Literature Review

- locator：Financial Inclusion and Social Justice P2 S1-S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：已有文献指出金融包容性是社会正义的基础，但未被充分服务人群缺乏金融素养和信用历史，传统模型因依赖信用历史而将其视为高信用风险。

- rhetorical_function_cn：总结金融包容性文献并说明传统模型的失败。

- depends_on_cn：引言中的鸡和蛋问题。

- sets_up_cn：为AI作为新解法提供文献定位。

- evidence_pointer：Literature Review第一节

### 26. Financial Inclusion and Social Justice P3 S1-S2

- order：26

- section：Literature Review

- locator：Financial Inclusion and Social Justice P3 S1-S2

- move_code：GAP

- paraphrase_cn：现有举措如开分支、降低标准等只部分解决问题且成本高；研究旨在检验AI信用评分模型能否帮助银行增强金融包容性。

- rhetorical_function_cn：在文献综述中建立研究缺口。

- depends_on_cn：前段对传统模型的描述。

- sets_up_cn：把AI研究定位为对金融包容性文献的补充。

- evidence_pointer：Literature Review第一节末

### 27. AI in Lending P1 S1

- order：27

- section：Literature Review

- locator：AI in Lending P1 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：AI在金融业广泛应用于交易、身份验证、欺诈检测、风险评估等，许多替代贷款机构已使用AI信用评分。

- rhetorical_function_cn：总结AI在借贷中的应用现状。

- depends_on_cn：无。

- sets_up_cn：为讨论传统银行采用AI的缺口做铺垫。

- evidence_pointer：Literature Review第二节开头

### 28. AI in Lending P2 S1-S2

- order：28

- section：Literature Review

- locator：AI in Lending P2 S1-S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：已有研究记录了AI模型对消费贷和小企业贷的影响，如降低违约率、改变获批借款人特征，但也存在训练样本偏差和黑箱担忧。

- rhetorical_function_cn：平衡总结已有证据和担忧。

- depends_on_cn：AI应用背景。

- sets_up_cn：说明为什么作者要研究传统银行场景。

- evidence_pointer：Literature Review第二节第二段

### 29. AI in Lending P3 S1-S3

- order：29

- section：Literature Review

- locator：AI in Lending P3 S1-S3

- move_code：GAP

- paraphrase_cn：尽管传统银行采用AI信用评分被期待已久，但实际落地证据很少；为填补缺口，作者与一家传统银行合作，研究合规AI模型对未被充分服务人群的影响、机制和条件。

- rhetorical_function_cn：明确指出传统银行场景下的研究缺口。

- depends_on_cn：前面文献。

- sets_up_cn：为本文研究问题提供文献理由。

- evidence_pointer：Literature Review第二节末

### 30. Weak Signals and AI-Enabled Credit Scoring P1 S1-S2

- order：30

- section：Literature Review

- locator：Weak Signals and AI-Enabled Credit Scoring P1 S1-S2

- move_code：THEORY_INTRO

- paraphrase_cn：作者采用“弱信号”概念指与信用不直接相关或传统评分不用的含噪数据，传统模型主要依赖强信号。

- rhetorical_function_cn：正式引入关键构念。

- depends_on_cn：AI文献。

- sets_up_cn：为数据域分析和机制分解提供概念框架。

- evidence_pointer：Literature Review第三节开头

### 31. Weak Signals and AI-Enabled Credit Scoring P2 S1-S3

- order：31

- section：Literature Review

- locator：Weak Signals and AI-Enabled Credit Scoring P2 S1-S3

- move_code：LIMITATION

- paraphrase_cn：弱信号因与信用关系不直接、噪声大、难以获取和缺失而被传统模型弃用。

- rhetorical_function_cn：解释为什么传统模型不用弱信号。

- depends_on_cn：弱信号定义。

- sets_up_cn：说明AI模型引入弱信号的增量价值。

- evidence_pointer：Literature Review第三节第二段

### 32. Weak Signals and AI-Enabled Credit Scoring P3 S1-S2

- order：32

- section：Literature Review

- locator：Weak Signals and AI-Enabled Credit Scoring P3 S1-S2

- move_code：MECHANISM

- paraphrase_cn：弱信号提供还款意愿和能力的信息，机器学习算法能降低利用弱信号的难度并发现交互效应，因此AI能更好地理解缺乏信用历史的申请人。

- rhetorical_function_cn：建立弱信号+算法→理解未被充分服务人群的机制链。

- depends_on_cn：弱信号定义和AI优势。

- sets_up_cn：为实证机制分析提供预期。

- evidence_pointer：Literature Review第三节末

### 33. Research Setting P1 S1-S4

- order：33

- section：Data and Empirical Strategy

- locator：Research Setting P1 S1-S4

- move_code：CONTEXT

- paraphrase_cn：作者与区域国有银行合作，银行服务超过五千万人，受政策激励从2020年开始在一个人贷产品中试验AI信用评分。

- rhetorical_function_cn：介绍研究现场和制度背景。

- depends_on_cn：引言中的合作场景。

- sets_up_cn：为DID识别提供制度依据。

- evidence_pointer：Data: Research Setting

### 34. Research Setting P2 S1-S3

- order：34

- section：Data and Empirical Strategy

- locator：Research Setting P2 S1-S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：银行选择该产品作为试点是因为业务团队更开放；AI模型只关注违约风险，没有为优待未被充分服务人群做任何调整。

- rhetorical_function_cn：说明处理产品的选择并非直接由金融包容性目标驱动，增强DID外生性。

- depends_on_cn：研究现场。

- sets_up_cn：为“AI目标只是预测精度”的核心论证提供支持。

- evidence_pointer：Data: Research Setting第二段

### 35. Research Setting P3 S1-S5

- order：35

- section：Data and Empirical Strategy

- locator：Research Setting P3 S1-S5

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：处理产品提供小额循环贷款，利率不因人而异，信用额度由单独公式决定；控制产品类似且服务相同客户池。

- rhetorical_function_cn：描述产品特征并建立控制产品的可比性。

- depends_on_cn：银行场景。

- sets_up_cn：为DID中控制组的合理性提供证据。

- evidence_pointer：Data: Research Setting第三段

### 36. Descriptive statistics P4 S1-S3

- order：36

- section：Data and Empirical Strategy

- locator：Descriptive statistics P4 S1-S3

- move_code：RESULT

- paraphrase_cn：部署前常规人群审批率约50%，未被充分服务人群只有17%；描述统计显示AI部署后未被充分服务人群审批率大幅上升，违约率下降。

- rhetorical_function_cn：用描述统计展示初始差异和AI后的变化。

- depends_on_cn：样本数据。

- sets_up_cn：为DID回归提供直观背景。

- evidence_pointer：Data: Descriptive statistics，Table 2/3

### 37. Development and Implementation P1 S1

- order：37

- section：Data and Empirical Strategy

- locator：Development and Implementation P1 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：传统评估过程基于规则模型，主要使用强信号，依赖专家知识，只允许线性和树结构逻辑。

- rhetorical_function_cn：描述传统模型特征，作为AI模型的对比基准。

- depends_on_cn：研究背景。

- sets_up_cn：为图2开发流程和机制分析提供对比。

- evidence_pointer：Development P1

### 38. Development P2 S1-S5

- order：38

- section：Data and Empirical Strategy

- locator：Development P2 S1-S5

- move_code：DESIGN_FEATURE

- paraphrase_cn：开发团队用六个月的强、弱信号数据，通过数据清洗、特征生成、四个个体学习器训练、特征筛选、集成学习、合规审查和持续监测，最终形成两层LightGBM模型。

- rhetorical_function_cn：详细展示AI模型的构建过程，强调其工程化设计。

- depends_on_cn：前面传统模型背景。

- sets_up_cn：为机制分析中的“弱信号+先进算法”提供具体设计证据。

- evidence_pointer：Development P2，Figure 2

### 39. Development P3 S1-S2

- order：39

- section：Data and Empirical Strategy

- locator：Development P3 S1-S2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：由于金融监管，银行没有完全替换传统模型，而是并行使用并通过决策矩阵确定最终决策，AI可以推翻传统模型的审批建议。

- rhetorical_function_cn：说明AI模型如何嵌入真实业务流程，也解释为何能形成DID中的处理组。

- depends_on_cn：开发过程。

- sets_up_cn：为图3决策矩阵和后续结果解释作准备。

- evidence_pointer：Development P3，Figure 3

### 40. Identification Strategy P1 S1-S3

- order：40

- section：Data and Empirical Strategy

- locator：Identification Strategy P1 S1-S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者应用DID并把排除政策影响、产品选择效应、人工评估等作为识别前提。

- rhetorical_function_cn：说明识别策略和需要处理的混淆因素。

- depends_on_cn：研究场景。

- sets_up_cn：为之后的具体排除措施和稳健性检验做框架。

- evidence_pointer：Identification Strategy第一段

### 41. Identification Strategy P2 S1-S4

- order：41

- section：Data and Empirical Strategy

- locator：Identification Strategy P2 S1-S4

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：政府政策会影响两个产品，DID能处理；作者排除了银行主动推广和调整传统模型的时期以及人工评估申请。

- rhetorical_function_cn：具体排除政策干扰和银行其他行动。

- depends_on_cn：识别前提。

- sets_up_cn：为后续稳健性提供基础。

- evidence_pointer：Identification Strategy第二段

### 42. Identification Strategy P3 S1-S3

- order：42

- section：Data and Empirical Strategy

- locator：Identification Strategy P3 S1-S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：产品选择作为试点并非完全随机，但与金融包容性没有直接明确联系。

- rhetorical_function_cn：承认选择效应但论证其不影响结论。

- depends_on_cn：银行解释和附录数据。

- sets_up_cn：为产品选择稳健性检验作铺垫。

- evidence_pointer：Identification Strategy第三段

### 43. Equations (1) and (2)

- order：43

- section：Data and Empirical Strategy

- locator：Equations (1) and (2)

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者用申请层面的DID方程估计审批率，用贷款层面的DID方程估计违约和利用率，控制申请人特征、模型更新、时间和产品固定效应。

- rhetorical_function_cn：正式定义估计模型。

- depends_on_cn：识别策略。

- sets_up_cn：为结果表格提供模型依据。

- evidence_pointer：Identification Strategy方程

### 44. Main Impacts P1 S1-S3

- order：44

- section：Results

- locator：Main Impacts P1 S1-S3

- move_code：TRANSITION

- paraphrase_cn：全样本上总体审批率变化不大，但违约率下降、利用率上升，说明全样本分析掩盖了异质性。

- rhetorical_function_cn：从方法转向结果，并预告需要分样本。

- depends_on_cn：方程和全样本结果。

- sets_up_cn：引出分常规/未被充分服务人群的Table 5。

- evidence_pointer：Results: Main Impacts，Table 4

### 45. Main Impacts P2 S1-S4

- order：45

- section：Results

- locator：Main Impacts P2 S1-S4

- move_code：RESULT

- paraphrase_cn：AI模型使未被充分服务人群审批率提高15%、违约率降低0.9%，相对幅度+89.3%和-19.6%；常规人群审批率略降但不显著。

- rhetorical_function_cn：给出核心分样本结果。

- depends_on_cn：Table 5。

- sets_up_cn：支持AI增强金融包容性的结论。

- evidence_pointer：Results: Main Impacts，Table 5

### 46. Main Impacts P2 S5-S7

- order：46

- section：Results

- locator：Main Impacts P2 S5-S7

- move_code：MECHANISM

- paraphrase_cn：传统模型忽视了未被充分服务人群中的大量机会，AI模型通过弱信号和算法更准确地估计个体违约风险，从而选择性地向信用良好者提供资本。

- rhetorical_function_cn：解释主结果背后的机制。

- depends_on_cn：分样本结果。

- sets_up_cn：为预测精度机制分析做铺垫。

- evidence_pointer：Results: Main Impacts

### 47. Main Impacts P3 S1-S2

- order：47

- section：Results

- locator：Main Impacts P3 S1-S2

- move_code：RESULT

- paraphrase_cn：被AI拒绝的申请人在其他贷款中的违约率更高、利用率更低，说明AI同时减少第一类和第二类错误。

- rhetorical_function_cn：用替代结果验证AI筛选质量的改进。

- depends_on_cn：主效应。

- sets_up_cn：为机制分析中的“更准确区分好坏申请人”提供证据。

- evidence_pointer：Main Impacts，Table 6

### 48. Prediction Accuracy P1 S1-S2

- order：48

- section：Mechanisms

- locator：Prediction Accuracy P1 S1-S2

- move_code：MECHANISM

- paraphrase_cn：AI模型能同时提高审批率、降低违约率的关键是它提供了更准确的信用评分。

- rhetorical_function_cn：提出机制命题。

- depends_on_cn：主结果。

- sets_up_cn：引导读者看分数分布表。

- evidence_pointer：Mechanisms: Prediction Accuracy

### 49. Prediction Accuracy P2 S1-S3

- order：49

- section：Mechanisms

- locator：Prediction Accuracy P2 S1-S3

- move_code：RESULT

- paraphrase_cn：表7显示传统模型严重低估未被充分服务人群，AI模型把更多人放入高分区间，且AI分数的违约率排序更准确。

- rhetorical_function_cn：用描述性证据直接支持预测精度机制。

- depends_on_cn：分数分布数据。

- sets_up_cn：为后续对“为什么更准确”的分解提供基础。

- evidence_pointer：Table 7

### 50. Data Domains P1 S1-S3

- order：50

- section：Mechanisms

- locator：Data Domains P1 S1-S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：传统模型主要基于1-6号强信号数据域，AI模型还使用社保、公积金、App金融和非金融行为4个弱信号数据域。

- rhetorical_function_cn：说明AI和传统模型在数据基础上的区别。

- depends_on_cn：模型开发过程。

- sets_up_cn：为弱信号贡献机制提供具体对象。

- evidence_pointer：Mechanisms: Data Domains，Table 8

### 51. Data Domains P2 S1-S3

- order：51

- section：Mechanisms

- locator：Data Domains P2 S1-S3

- move_code：MECHANISM

- paraphrase_cn：弱信号不与信用直接相关，人类专家难以将它们转成规则；未被充分服务人群缺少强信号，但弱信号可得性与常规人群相似。

- rhetorical_function_cn：解释弱信号为何对传统模型困难、对AI价值大。

- depends_on_cn：数据域表。

- sets_up_cn：为机制分解和异质性分析做铺垫。

- evidence_pointer：Data Domains，Table 8

### 52. Weak Signals and Advanced Models P1 S1-S4

- order：52

- section：Mechanisms

- locator：Weak Signals and Advanced Models P1 S1-S4

- move_code：RESULT

- paraphrase_cn：表A2显示即使由传统模型使用，弱信号也能提高预测精度；AI模型结合强、弱信号效果最好。

- rhetorical_function_cn：证明弱信号的独立价值。

- depends_on_cn：数据域分析。

- sets_up_cn：为表9的相对贡献总结提供基础。

- evidence_pointer：Weak Signals and Advanced Models，Table A2

### 53. Weak Signals and Advanced Models P2 S1-S3

- order：53

- section：Mechanisms

- locator：Weak Signals and Advanced Models P2 S1-S3

- move_code：RESULT

- paraphrase_cn：表A4显示在相同强信号下，AI模型比传统模型预测精度更高，说明先进算法本身提升精度。

- rhetorical_function_cn：证明先进算法的独立价值。

- depends_on_cn：模型对比模拟。

- sets_up_cn：为表9综合比较做支撑。

- evidence_pointer：Weak Signals and Advanced Models，Table A4

### 54. Weak Signals and Advanced Models P3 S1-S4

- order：54

- section：Mechanisms

- locator：Weak Signals and Advanced Models P3 S1-S4

- move_code：RESULT

- paraphrase_cn：表9显示弱信号和先进算法都贡献精度改进，先进算法的贡献更大；两者组合对未被充分服务人群的提升尤其大，加入弱信号的额外提升为128个百分点。

- rhetorical_function_cn：给出机制分解的核心定量结果。

- depends_on_cn：A2/A4结果。

- sets_up_cn：解释未被充分服务人群为何受益更大。

- evidence_pointer：Table 9

### 55. Additional Predictive Power P1 S1-S3

- order：55

- section：Mechanisms

- locator：Additional Predictive Power P1 S1-S3

- move_code：RESULT

- paraphrase_cn：单数据域可解释性分析显示弱信号数据域的预测力与强信号接近，说明弱信号本身有预测价值。

- rhetorical_function_cn：补充弱信号增量价值的证据。

- depends_on_cn：机制分解。

- sets_up_cn：引出相关结构分析。

- evidence_pointer：Additional Predictive Power，Table 10

### 56. Additional Predictive Power P2 S1-S4

- order：56

- section：Mechanisms

- locator：Additional Predictive Power P2 S1-S4

- move_code：RESULT

- paraphrase_cn：相关分析显示弱信号与强信号多数相关性低，说明弱信号提供强信号之外的新信息。

- rhetorical_function_cn：证明弱信号并非强信号的冗余替代。

- depends_on_cn：单域预测力。

- sets_up_cn：支持弱信号作为独立驱动机制。

- evidence_pointer：Additional Predictive Power，Table 11

### 57. Heterogeneous Impacts P1 S1-S2

- order：57

- section：Heterogeneous Impacts

- locator：Heterogeneous Impacts P1 S1-S2

- move_code：RESULT

- paraphrase_cn：AI模型在5个未被充分服务亚组中提升了4个亚组的审批率，降低了所有亚组的违约率。

- rhetorical_function_cn：建立异质性边界。

- depends_on_cn：主结果。

- sets_up_cn：引向对缺失弱信号和统计歧视的分析。

- evidence_pointer：Heterogeneous Impacts，Table 12

### 58. Missing weak signals P2 S1-S3

- order：58

- section：Heterogeneous Impacts

- locator：Missing weak signals P2 S1-S3

- move_code：RESULT

- paraphrase_cn：缺失弱信号会降低AI模型对审批率的提升幅度，但总体效应仍然为正。

- rhetorical_function_cn：说明弱信号对效果的重要性及其边界。

- depends_on_cn：弱信号机制。

- sets_up_cn：为边界条件和推广性分析做铺垫。

- evidence_pointer：Heterogeneous Impacts，Table 13

### 59. Statistical Discrimination P3 S1-S4

- order：59

- section：Heterogeneous Impacts

- locator：Statistical Discrimination P3 S1-S4

- move_code：RESULT

- paraphrase_cn：交互项显示部署AI后城市户籍、受雇、有信用历史的审批优势显著缩小，在未被充分服务人群中优势缩小27.3%-52.0%。

- rhetorical_function_cn：直接连接统计歧视理论的实证检验。

- depends_on_cn：统计歧视理论。

- sets_up_cn：支持AI减少统计歧视的核心理论主张。

- evidence_pointer：Statistical Discrimination，Table 14

### 60. Robustness P1 S1-S3

- order：60

- section：Robustness Checks

- locator：Robustness P1 S1-S3

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：作者用相对时间模型检验平行趋势，发现审批率和违约率在部署前无显著差别。

- rhetorical_function_cn：为DID有效性提供关键前提检验。

- depends_on_cn：主DID。

- sets_up_cn：为后续选择效应、人工干预等稳健性做基础。

- evidence_pointer：Robustness Checks，Equation (3)

### 61. Robustness P2 S1-S2

- order：61

- section：Robustness Checks

- locator：Robustness P2 S1-S2

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：表16总结并解决了产品选择、申请人选择、人工评估、滞后人工效应和未观测行动等威胁，所有检验都支持主结果。

- rhetorical_function_cn：系统展示对替代解释的排除。

- depends_on_cn：相对时间检验。

- sets_up_cn：为外部有效性和推广性讨论做准备。

- evidence_pointer：Robustness Checks，Table 16

### 62. Compliance P1 S1-S3

- order：62

- section：Compliance and Generalizability

- locator：Compliance P1 S1-S3

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：使用AI和隐私敏感数据在监管上具有挑战性，作者整理了银行满足数据收集、隐私、受保护特征、结果公平和透明性等合规要求的做法。

- rhetorical_function_cn：说明AI模型在监管约束下如何落地，划定适用条件。

- depends_on_cn：银行开发实践。

- sets_up_cn：支持推广性论证。

- evidence_pointer：Compliance and Generalizability，Table 17

### 63. Simplified models P2 S1-S4

- order：63

- section：Compliance and Generalizability

- locator：Simplified models P2 S1-S4

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：模拟的简化AI模型（单Learner或单弱信号域）仍能显著提高未被充分服务人群审批率并降低违约率，尽管幅度更小。

- rhetorical_function_cn：验证结果对缺乏复杂能力或数据的机构仍可推广。

- depends_on_cn：主模型结果。

- sets_up_cn：为讨论中的边界条件提供证据。

- evidence_pointer：Simplified models，Table 18

### 64. Discussion P1 S1-S4

- order：64

- section：Discussion and Conclusion

- locator：Discussion P1 S1-S4

- move_code：CONTEXT

- paraphrase_cn：金融包容性对未被充分服务人群很重要，传统解决方案成本高或风险高；作者从信息技术角度研究AI信用评分的影响。

- rhetorical_function_cn：重新连接引言中的现实问题。

- depends_on_cn：全文背景。

- sets_up_cn：为总结发现和贡献提供框架。

- evidence_pointer：Discussion第一段

### 65. Discussion P2 S1-S4

- order：65

- section：Discussion and Conclusion

- locator：Discussion P2 S1-S4

- move_code：CONTRIBUTION

- paraphrase_cn：作者总结AI模型在不牺牲贷款绩效的前提下增强金融包容性，解决了金融包容性与贷款绩效之间长期存在的两难。

- rhetorical_function_cn：把结果升华为对核心问题的回答。

- depends_on_cn：主结果。

- sets_up_cn：为机制总结和理论贡献做铺垫。

- evidence_pointer：Discussion第二段

### 66. Discussion P3 S1-S3

- order：66

- section：Discussion and Conclusion

- locator：Discussion P3 S1-S3

- move_code：MECHANISM

- paraphrase_cn：直接机制是AI提高预测精度，弱信号和先进算法是两台引擎，二者结合带来最大改进，尤其对未被充分服务人群。

- rhetorical_function_cn：在讨论中复述和强化机制结论。

- depends_on_cn：机制章节。

- sets_up_cn：为理论贡献定位。

- evidence_pointer：Discussion第三段

### 67. Discussion P4 S1-S3

- order：67

- section：Discussion and Conclusion

- locator：Discussion P4 S1-S3

- move_code：CONTRIBUTION

- paraphrase_cn：作者声称研究对社会正义文献和AI消费者借贷文献都有贡献，填补了AI模型影响金融包容性研究的空白。

- rhetorical_function_cn：明确理论贡献并回应文献缺口。

- depends_on_cn：文献综述和结果。

- sets_up_cn：引出限制和未来方向。

- evidence_pointer：Discussion第四段

### 68. Discussion P5 S1-S4

- order：68

- section：Discussion and Conclusion

- locator：Discussion P5 S1-S4

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：作者承认AI不能解决结构性歧视，对缺失弱信号的亚组效果较弱，黑箱和隐私问题仍需政策干预和未来研究。

- rhetorical_function_cn：设置边界条件，避免过度泛化。

- depends_on_cn：异质性和合规分析。

- sets_up_cn：文章以此收束。

- evidence_pointer：Discussion第五段

## 写作技术

- gap_construction_cn：作者先用“鸡和蛋”现象展示金融包容性的结构性困境，再指出传统扩展方案成本高、风险高，接着说明AI模型具有理论上的优势但也存在偏见和黑箱担忧，最后指出“传统银行实际采用AI模型的影响尚未被研究”，从而在现实重要性和文献空白之间建立清晰的GAP。

- signposting_cn：在摘要、引言和文献综述中反复预告三个研究问题；每个实证小节开头都会说明“要回答什么问题”，结尾会总结“该发现支持什么机制”；大量使用“To answer these research questions”“We first investigated…”“To further understand…”等过渡路标。

- transition_logic_cn：从主效应到筛选绩效，再到预测精度、弱信号、先进算法、异质性和稳健性，每一步都建立在前一步留下的未解问题上；用“直接原因”“数据域”“另一渠道”“进一步”“为理解…”等连接词；结果后紧跟机制，机制后紧跟边界，边界后紧跟稳健性。

- claim_evidence_rhythm_cn：先给结论性表述，再指向表/图作为证据，然后解释相对幅度和理论含义；在关键主张（如同时降低两类错误）后，立即用替代结果分析确认；在机制主张后，用模拟模型分解和单域分析提供多重证据。

- benchmark_narrative_cn：几乎所有对比都围绕“传统规则模型”这一自然基准展开：DID中用控制产品作为基准；预测精度中用传统模型分数作为基准；机制分解中用传统模型AUC作为基准；简化模型模拟中用真实AI模型作为基准；这样使每一个性能或效果数字都嵌在可解释的对照中。

- theory_return_cn：作者没有只在引言引用统计歧视理论，而是在机制、异质性、统计歧视交互项和讨论部分反复回到该理论；用“减少依赖群体特征”作为统一解释，把审批率提升、违约率下降、特征优势缩小都纳入同一个理论框架。

- contribution_positioning_cn：作者把贡献定位在AI与社会正义、AI与消费者借贷的交叉处，特别强调“以提高预测精度为目标训练的AI也能增强金融包容性”，这一表述既回应AI偏见担忧，又区别于已有技术准确性研究。

- novelty_protection_cn：作者通过展示机制（弱信号+算法）、边界（缺失弱信号、结构性歧视）、可推广性（简化模型模拟）和合规性（监管映射），把结果从“一个银行的一次AI部署”提升为可复用的设计知识和理论命题，避免被看作一次性性能结果。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：用现实世界的社会问题（金融排斥）和“鸡和蛋”现象建立重要性；给出定义和现实后果。

- research_job_cn：选择具有重大社会后果的领域，找到制度性障碍和现有解决方案的高成本/低扩展性限制。

- required_evidence_cn：文献中关于该问题影响和现有方案不足的证据。

- transition_to_next_cn：指出需要新的可扩展方案，引入信息技术/AI作为潜在答案。

#### 2. 2

- step：2

- writing_job_cn：在文献综述中建立三条线索：领域文献、技术应用文献、关键构念文献；指出传统金融机构采用AI尚未被研究。

- research_job_cn：找到可进入的真实组织/平台现场，确认存在罕见的AI采用事件和适当的对照组。

- required_evidence_cn：获得组织合作、明确的采用时间、处理产品/控制产品、以及“AI目标不是直接偏向弱势群体”的事实。

- transition_to_next_cn：描述研究现场和数据，说明DID识别策略。

#### 3. 3

- step：3

- writing_job_cn：详细描述AI制品的发展流程和实际部署方式，强调设计特征（数据域、算法、决策矩阵）和与传统模型的差异。

- research_job_cn：与开发团队合作获取模型开发步骤、数据域列表、特征工程方法和最终模型结构。

- required_evidence_cn：可验证的模型开发流程图、数据域表、模型部署时间线和决策规则。

- transition_to_next_cn：说明这些设计如何构成DID中的处理，并引出方程。

#### 4. 4

- step：4

- writing_job_cn：用DID方程和表格报告处理效应，先全样本再分样本，给出相对幅度。

- research_job_cn：运行审批率、违约率、利用率的DID回归；处理产品选择、时间趋势、固定效应和聚类标准误。

- required_evidence_cn：主结果的显著性和稳健性，分样本显示弱势群体受益更大。

- transition_to_next_cn：指出全样本掩盖异质性，需要用更细的反事实和机制分析解释。

#### 5. 5

- step：5

- writing_job_cn：用被拒申请人的替代贷款结果验证筛选质量，说明同时减少两类错误。

- research_job_cn：匹配被处理产品/控制产品拒绝但在其他金融机构获得贷款的申请人，构建反事实贷款表现。

- required_evidence_cn：替代贷款违约率和利用率在DID下的显著变化。

- transition_to_next_cn：从“更好筛选”进入“为什么更好预测”的机制分析。

#### 6. 6

- step：6

- writing_job_cn：用分数分布、模型模拟、单数据域可解释性和相关分析打开预测精度黑箱，把效果归因于弱信号和先进算法。

- research_job_cn：比较传统模型与AI模型的分数分布；隔离弱信号和算法的影响；计算AUC/KS；检验弱信号增量信息。

- required_evidence_cn：AUC/KS对比、相对改进百分比、单域预测力和相关性矩阵。

- transition_to_next_cn：说明效果并非平均分布，需要研究异质性和边界。

#### 7. 7

- step：7

- writing_job_cn：用子样本DID、缺失数据交互项和关键特征交互项展示异质性、边界和统计歧视减少。

- research_job_cn：按未被充分服务标准划分子样本；构造缺失弱信号哑变量；检验传统优势特征审批优势的缩小。

- required_evidence_cn：各亚组系数、交互项方向和显著性、优势缩小的百分比。

- transition_to_next_cn：在因果解释之前必须先排除识别威胁。

#### 8. 8

- step：8

- writing_job_cn：用平行趋势、匹配样本、线上样本、分行分析、安慰剂检验等系统排除竞争解释。

- research_job_cn：构建相对时间模型、匹配样本、特定子样本和伪处理日期回归。

- required_evidence_cn：部署前无显著差异，各稳健性检验方向一致，安慰剂效应远小于主效应。

- transition_to_next_cn：说明结果可信后，讨论推广性和合规性。

#### 9. 9

- step：9

- writing_job_cn：用合规表、简化模型模拟和行业实例讨论可推广性，最后讨论理论贡献、限制和未来方向。

- research_job_cn：整理监管合规措施；训练简化模型并模拟部署；对照其他实践。

- required_evidence_cn：简化模型仍显著有效，合规实践可复制，边界条件清晰。

- transition_to_next_cn：回到引言中的社会正义和AI文献，总结贡献和局限。

### most_transferable_moves_cn

1. 把现实问题凝练为“鸡和蛋”式结构性困境，增加研究必要性

2. 利用真实组织部署中的处理/对照产品构建准自然实验

3. 在AI制品描述中突出“目标仅提高预测精度”这一洁净性设计

4. 用DID主效应→筛选反事实→机制分解→异质性→稳健性→推广性的递进结构

5. 用AUC/KS相对改进而非单一准确率来分解机制贡献

6. 用“传统优势特征审批优势缩小”作为统计歧视减少的可观察代理

7. 用简化模型模拟把单点结果推广为一般设计知识

### resource_intensive_or_nonstandard_parts_cn

1. 与大型银行六年的深度合作和内部数据访问

2. 银行内部的AI模型开发团队和详细开发日志

3. 处理产品和控制产品同时存在的罕见试点安排

4. 覆盖930万申请的大规模行政和贷款表现数据

5. 对人工评估申请进行标记和排除的数据库能力

6. 跨机构和跨产品的替代贷款匹配数据

7. 一个包含数据科学家和合规专家的长期项目团队

### what_not_to_copy_superficially_cn

1. 不能只套用“AI+普惠金融”叙事而没有真实银行部署和处理/对照产品

2. 不能只报告DID系数而没有平行趋势和多种竞争解释排除

3. 不能把机制归因于弱信号/算法而不提供AUC/KS分解或单域证据

4. 不能声称AI减少统计歧视而只用主效应推测，需要有特征优势缩小等交互证据

5. 不能直接宣称推广到其他银行或国家，除非有模拟或合规分析支持

6. 不能忽略结构性不公正、缺失数据亚组和黑箱等边界条件

- single_best_description_of_the_routine_cn：用一个真实银行罕见但干净的AI部署作为准自然实验，先用DID证明“AI能同时提升弱势群体审批和降低违约”，再用分数分布、模型分解、交互项和模拟把这一结果上升为“弱信号+先进算法减少统计歧视”的可迁移设计知识。

## 分析边界

文章全文和附录基本完整，但OCR后部分表格内公式字符和个别附图（图1、图2、图3、图A1）仅能依赖文字说明；没有精确页码，位置证据主要使用章节、表号、图号和段落位置；部分附录内容（如A12行业实践表）依赖原文表格，分析中不补充未提供的细节。
