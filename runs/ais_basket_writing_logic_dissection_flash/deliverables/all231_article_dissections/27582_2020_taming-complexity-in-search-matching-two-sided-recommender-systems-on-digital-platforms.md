# Taming Complexity in Search Matching: Two-Sided Recommender Systems on Digital Platforms

- 作者：Onkar Malgonde; He Zhang; Balaji Padmanabhan; Moez Limayem
- 年份 / 期刊：2020 / MIS Quarterly
- DOI：10.25300/misq/2020/14424
- 源文件：27582_2020_taming-complexity-in-search-matching-two-sided-recommender-systems-on-digital-platforms.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.82

## 文章级论证概况

- 核心问题：数字多边平台中的复杂搜索匹配问题如何被驯服？引入一个同时考虑平台双边涌现性的两阶段推荐系统，是否比现有单边推荐系统更能降低不可约不确定性并改善参与者的表现？

- 制品与设计：提出一个two-sided recommender system框架，将推荐系统本身作为CABS中的agent，基于平台级数据学习不同侧代理的涌现性，既向学生推荐课程/同伴/讨论板，也向大学推荐课程开设/专业/开设时间；算法用简单启发式实例化。

- 客观结果：通过agent-based simulation，在MOOC教育平台情境中比较no recommender、one-sided recommender和two-sided recommender三种设置；结果显示两阶段推荐系统在降低平均fitness波动（AIC窗口分析）和提升平均fitness（参数扫描+回归）方面均优于单边推荐和无推荐。

- 核心贡献：为复杂适应商业系统提供一种以IT为基础的机制——考虑双边涌现性的推荐系统框架，能够驯服数字平台中的复杂搜索匹配问题，并推动复杂科学、信息系统和推荐系统研究。

- 整篇论证链：作者将数字多边平台概念化为复杂适应商业系统（CABS），指出平台参与者具有多样性、适应性、连接性和相互依赖性，导致非线性互动和双边涌现，进而产生不可约不确定性，使传统的收集和处理数据的方法失效。基于Tanriverdi等的理论，作者主张应对不可约不确定性的方式是驯服而非减少，即让agents coevolve and learn。现有搜索匹配方法和单边推荐系统只能处理传统不确定性，无法考虑平台另一侧的涌现性。为此，作者设计了一个将推荐系统视为CABS中adaptive agent的两阶段推荐系统框架，并在MOOC教育平台情境中用agent-based simulation实现。模拟模型经过复杂性验证后，作者通过AIC窗口比较证明两阶段推荐系统能更好地降低平均fitness的波动（即驯服复杂搜索匹配），再通过参数扫描和回归分析证明两阶段推荐系统能提升学生和大学的平均fitness。最后，讨论部分将结果返回CABS理论，主张这种IT制品为复杂系统提供了taming机制，并指出不同复杂系统可能需要不同的taming方法。

## 类型与写作弧线判定

- 论文主类型判定：文章明确采用Hevner设计科学指南（Table 6），将two-sided recommender framework作为设计制品，以agent-based simulation作为评价方法，并与现有框架进行比较，最终提炼可复用的框架性设计知识和理论贡献。

- 主导写作弧线判定：论文从CABS复杂搜索匹配问题出发，基于复杂科学理论推导设计原则并提出两阶段推荐系统，随后用模拟假设检验验证设计，最后在Discussion中返回理论，讨论对复杂科学和IS理论的贡献。

## 研究开展程序

- study_or_phase_count：6

- 研究阶段总序列：第1阶段用理论论证建立复杂搜索匹配问题；第2阶段提出两阶段推荐系统框架和假设；第3阶段构建教育平台CABS的agent-based模拟模型；第4阶段验证模拟模型确实产生复杂性；第5阶段检验推荐系统对驯服不确定性的效果（H1）；第6阶段检验推荐系统对fitness改善的效果（H2）。各阶段呈累积关系，前阶段为后阶段提供概念基础或评价工具。

### studies_or_phases

#### 1. 问题概念化：平台作为CABS与复杂搜索匹配问题

- order：1

- name_cn：问题概念化：平台作为CABS与复杂搜索匹配问题

- question_cn：为什么数字多边平台上的搜索匹配问题是一个复杂问题，且传统方法无法解决？

- inputs_and_setting_cn：理论文献：Tanriverdi et al. (2010)、Nan (2011)、Page (2009)；平台实例如Uber、Amazon、Airbnb、MOOC平台。

- designed_or_compared_object_cn：无设计对象，主要是对平台和问题进行分类和论证。

- baseline_control_or_counterfactual_cn：以传统信息收集与处理视角作为对照。

##### objective_metrics

（空）

- analysis_method_cn：概念论证、文献综合、案例分析。

- main_result_cn：平台可视为CABS，其非线性互动和涌现产生不可约不确定性，搜索匹配是复杂问题。

- argumentative_role_cn：建立研究问题的重要性和理论立场，为后续设计two-sided推荐系统提供理论根据。

- remaining_uncertainty_cn：尚不清楚何种IS方案能实际驯服该不确定性。

- link_to_next_phase_cn：引出需要设计一种考虑复杂性的推荐系统框架。

##### evidence_pointers

1. Introduction P1-P5

2. Theoretical Foundations

3. Figure 1

4. Appendix A

#### 2. 框架设计与假设提出：两阶段推荐系统

- order：2

- name_cn：框架设计与假设提出：两阶段推荐系统

- question_cn：如果要驯服复杂搜索匹配，推荐系统应该如何设计？它比现有单边推荐系统好在哪？

- inputs_and_setting_cn：基于推荐系统文献（Adomavicius、Godoy-Lorite等）和CABS理论。

- designed_or_compared_object_cn：提出two-sided recommender framework，与no recommender和one-sided recommender进行概念比较。

- baseline_control_or_counterfactual_cn：one-sided recommender作为现有方法baseline，no recommender作为无干预baseline。

##### objective_metrics

（空）

- analysis_method_cn：理论推导、框架图示（Figure 3）、假设提出。

- main_result_cn：提出H1a/H1b/H2a/H2b，认为两阶段推荐系统应比单边和无推荐更好地驯服不确定性和提升fitness。

- argumentative_role_cn：将理论转化为可检验的设计差异和假设，为后续模拟提供导向。

- remaining_uncertainty_cn：尚需实证证据验证这些假设。

- link_to_next_phase_cn：需要一个可操作化复杂系统的模拟环境来检验假设。

##### evidence_pointers

1. Recommender Systems in Digital Platforms

2. Two-Sided Recommender Systems

3. Figure 2-3

4. Hypotheses

#### 3. 模拟模型构建：教育平台CABS的agent-based模型

- order：3

- name_cn：模拟模型构建：教育平台CABS的agent-based模型

- question_cn：如何将CABS概念模型实例化为可计算的agent-based模拟模型？

- inputs_and_setting_cn：基于Coursera、Udacity等MOOC平台的特征，以及学生和大学动机的文献。

- designed_or_compared_object_cn：设计agent-based模型，包含学生、大学、课程、推荐系统等agent，定义属性、行为规则、fitness更新。

- baseline_control_or_counterfactual_cn：模型包含no recommendation、one-sided、two-sided三种设置。

##### objective_metrics

1. agent fitness

2. course ratings

3. utilization rate

4. grades

5. AIC values

- analysis_method_cn：面向对象编程实现agent-based simulation，使用伪代码和行为规则。

- main_result_cn：构建了一个能复现平台动态的模拟模型，agents通过简单规则互动产生emergence。

- argumentative_role_cn：将抽象框架转化为可运行的评价工具，为假设检验提供实验平台。

- remaining_uncertainty_cn：需要验证该模拟模型确实产生复杂性（非线性），否则后续taming分析缺乏基础。

- link_to_next_phase_cn：通过AIC非线性拟合验证模型复杂度，为后续taming测量提供前提。

##### evidence_pointers

1. Conceptual Model

2. Two-Sided Recommender Systems in Educational Platforms

3. Agent-Based Model Design

4. Tables 1-5

5. Figure 4-6

6. Appendix B-E

#### 4. 复杂性验证：模拟模型中的非线性与超湍流

- order：4

- name_cn：复杂性验证：模拟模型中的非线性与超湍流

- question_cn：agent-based模拟模型是否真的表现出复杂性（非线性）而非稳定均衡？

- inputs_and_setting_cn：对每个推荐系统变体运行5,000期模拟，记录每期学生和大学平均fitness。

- designed_or_compared_object_cn：对每个变体拟合线性、二次、三次模型，比较AIC。

- baseline_control_or_counterfactual_cn：线性模型作为对照，非线性模型（二次、三次）作为候选。

##### objective_metrics

1. AIC

2. Wilcoxon signed-rank test p-value

- analysis_method_cn：拟合三次模型与线性模型比较AIC；对数据分窗口（10,25,50,75,100,150,200）用Wilcoxon检验。

- main_result_cn：三次模型对所有变体都是最佳拟合，且非线性模型AIC在窗口分析中显著更低，证明模拟模型表现出复杂性。

- argumentative_role_cn：确认模拟环境具有CABS性质，为后续将AIC差异解释为taming效果提供基础。

- remaining_uncertainty_cn：复杂性存在，但尚不清楚不同推荐系统对复杂搜索匹配的taming效果如何。

- link_to_next_phase_cn：使用同一模拟数据，通过窗口AIC比较来量化不同推荐系统的taming效果。

##### evidence_pointers

1. Complexity in the Agent-Based Simulation Model

2. Figure 7

#### 5. 假设检验H1：驯服复杂搜索匹配的窗口AIC分析

- order：5

- name_cn：假设检验H1：驯服复杂搜索匹配的窗口AIC分析

- question_cn：one-sided和two-sided推荐系统是否比no recommender更好地降低fitness波动（即taming）？two-sided是否优于one-sided？

- inputs_and_setting_cn：5,000期模拟数据，3种推荐变体，对每个变体用全局最佳模型（三次）拟合不同数据窗口（300期）。

- designed_or_compared_object_cn：比较one-sided vs no recommender，two-sided vs no recommender，two-sided vs one-sided。

- baseline_control_or_counterfactual_cn：no recommender作为baseline，one-sided作为现有方法对照。

##### objective_metrics

1. mean AIC

2. Wilcoxon signed-rank test p-value

- analysis_method_cn：将数据分16个窗口，每个窗口计算AIC；用Wilcoxon检验比较均值。窗口大小稳健性分析（100-400）。

- main_result_cn：H1a部分支持（学生侧不显著，大学侧显著）；H1b完全支持（two-sided在两侧都显著优于no和one-sided）。

- argumentative_role_cn：证明two-sided推荐系统在taming不确定性方面优于现有方案。

- remaining_uncertainty_cn：AIC差异反映波动降低，但尚未直接证明fitness的实际提升。

- link_to_next_phase_cn：通过参数扫描和回归检验fitness改善，完成第二组假设。

##### evidence_pointers

1. Results/Taming Complex Search Matching

2. Figure 8

#### 6. 假设检验H2：改善agent fitness的参数扫描与回归

- order：6

- name_cn：假设检验H2：改善agent fitness的参数扫描与回归

- question_cn：随着平台不确定性变化，推荐系统能否提升平均fitness？two-sided是否优于one-sided？

- inputs_and_setting_cn：对6个变量（Agent Types、Social Network size、Incoming students等）进行参数扫描，每个配置运行100次×1,000期。

- designed_or_compared_object_cn：比较三种推荐设置在不同参数组合下的平均fitness。

- baseline_control_or_counterfactual_cn：no recommender作为base，one-sided作为对照；回归模型中以no recommender为基准，也以one-sided为基准进行re-run。

##### objective_metrics

1. 平均学生fitness

2. 平均大学fitness

3. 回归系数

4. 调整R²

- analysis_method_cn：用线性回归模型（公式1和2）估计AlgoType和参数变量的效应。

- main_result_cn：one-sided提升学生0.31、大学0.32；two-sided提升学生0.63、大学0.45，且two-sided与one-sided相比提升学生0.31、大学0.13；H2a得到支持，H2b得到完全支持。

- argumentative_role_cn：证明two-sided推荐系统不仅能降低波动，还能实际提高agents的平均绩效，完成taming的价值论证。

- remaining_uncertainty_cn：模拟是简化的，未包含财务指标、真实数据校准，也未与搜索/定价机制比较。

- link_to_next_phase_cn：进入Discussion，将结果连接回理论并划清边界条件。

##### evidence_pointers

1. Results/Improving Agent Performance

2. Tables 7-10

## 各部分修辞架构

### abstract_moves

1. CONTEXT: 将数字平台定义为CABS，其特征是多种目标、偏好和约束。

2. GAP: 指出传统收集处理数据无法降低不可约不确定性。

3. RQ_OR_OBJECTIVE: 提出基于推荐系统的方法驯服复杂性。

4. DESIGN_FEATURE: 提出novel two-sided recommender system框架，考虑双边涌现。

5. STUDY_OVERVIEW: 使用agent-based simulation检验假设。

6. RESULT: 报告双面推荐系统的价值。

7. CONTRIBUTION: 讨论对IS和复杂科学的意义。

### introduction_moves

1. CONTEXT: 将平台视为市场中介流中的CABS。

2. PHENOMENON: 描述良性/恶性循环。

3. PRACTICAL_STAKES: 参与者数量增加导致匹配困难。

4. PHENOMENON: 定义复杂问题特征。

5. MECHANISM: 描述非线性、自我组织、emergence。

6. GAP: 传统方法（过滤、标签、单边推荐）有限。

7. RQ_OR_OBJECTIVE: 提出两阶段推荐系统。

8. STUDY_OVERVIEW: 在MOOC情境中研究。

9. CONTRIBUTION: 承接Tanriverdi等的命题，提供经验证据和新框架。

### theory_and_knowledge_moves

1. THEORY_INTRO: 介绍CABS四个属性。

2. THEORY_PROPOSITION: 面对不可约不确定性应转向taming。

3. MECHANISM: 非线性互动产生不可预测结果。

4. LIMITATION: 现有方法（分组、搜索、单边推荐）不能处理emergence。

5. PRIOR_KNOWLEDGE: 经济学匹配理论、互惠推荐等。

### artifact_design_moves

1. DESIGN_FEATURE: 将推荐系统建模为CABS中的agent。

2. REQUIREMENT: 需要学习双边emergence。

3. DESIGN_FEATURE: 为不同agent提供不同推荐类型。

4. BENCHMARK_OR_CONTRAST: 对比no/one/two-sided。

5. METHOD_JUSTIFICATION: 采用agent-based simulation的原因。

### evaluation_moves

1. METHOD_JUSTIFICATION: 非线性模型AIC检验复杂性。

2. BENCHMARK_OR_CONTRAST: 以无推荐和单边推荐为baseline。

3. RESULT: AIC窗口分析。

4. ROBUSTNESS_OR_BOUNDARY_TEST: 不同窗口大小。

5. RESULT: 回归分析fitness提升。

### discussion_and_contribution_moves

1. CONTRIBUTION: 提出two-sided框架作为adaptive IS solution。

2. MECHANISM: 用冷启动问题说明单边局限。

3. BOUNDARY_CONDITION: 结果限于market intermediary stream。

4. LIMITATION_AND_FUTURE: 公平性、财务指标、其他设计替代。

5. CONTRIBUTION: 对IS和推荐系统的评价方法含义。

6. CONTRIBUTION: 对复杂科学的IT制品贡献。

## 理论/知识到设计的翻译

### 知识/理论基础

1. CABS理论 (Tanriverdi et al. 2010; Page 2009; Nan 2011)

2. 推荐系统文献 (Adomavicius and Tuzhilin 2005; Godoy-Lorite et al. 2016)

3. 经济学匹配理论 (Roth 1982; Romanyuk 2016; Kanoria and Saban 2017)

4. 平台生态系统文献 (Parker et al. 2016; Tiwana 2013)

- 理论—设计耦合：partial

- 耦合判定理由：CABS理论提供了核心设计原则（应使agents coevolve and learn，而非收集数据预测），并决定了推荐系统应纳入多边emergence，但具体推荐算法是简单启发式，并非理论直接推导；设计主要来源于对现有推荐系统局限的分析和工程简化。

- 理论到设计翻译链：CABS中非线性互动和emergence导致不可约不确定性 → agents需要coevolve而非预测 → 推荐系统应作为adaptive agent服务多边 → 设计two-sided recommender framework → 在MOOC情境实例化为简单启发式算法 → 通过agent-based simulation对比no/one/two-sided → 用AIC证明taming效果、回归证明fitness提升。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：在CABS中，agents具有多样性、适应、连接和相互依赖，导致非线性互动和emergence，形成不可约不确定性。

- mechanism_cn：非线性互动使类似行为产生不同结果，agent无法精确预测系统状态。

- design_requirement_cn：解决方案应使agents coevolve and learn，而不是收集更多数据来预测未来。

- artifact_choice_cn：构建two-sided recommender framework，推荐系统作为CABS中的agent，学习不同侧的emergence。

- evaluated_contrast_cn：two-sided vs one-sided vs no recommender。

- objective_result_cn：two-sided在AIC窗口比较中显著低于one-sided和no recommender。

##### evidence_pointers

1. Theoretical Foundations

2. Two-Sided Recommender Systems

3. Figure 8

#### 2. 2

- theory_or_knowledge_claim_cn：现有one-sided recommender只服务一侧，仅学习平台级数据中的局部模式，无法考虑另一侧agents的emergence和适应。

- mechanism_cn：单侧推荐会忽略其他侧的实时涌现（如新卖家进入、买家偏好变化），导致推荐在复杂环境中失效。

- design_requirement_cn：推荐系统必须同时建模两侧的emergence，并基于平台级数据实时调整推荐。

- artifact_choice_cn：two-sided recommender同时向学生推荐课程/同伴/讨论板，向大学推荐课程开设/专业/时间。

- evaluated_contrast_cn：one-sided recommender只向学生推荐，不向大学推荐；two-sided考虑双方目标。

- objective_result_cn：two-sided相较于one-sided提升学生fitness 0.31、大学fitness 0.13。

##### evidence_pointers

1. Two-Sided Recommender System

2. Table 5

3. Tables 8-9

#### 3. 3

- theory_or_knowledge_claim_cn：传统推荐系统评价用hold-out样本假设静态环境，但复杂系统中未来不像过去，agent会发展出新的行为。

- mechanism_cn：静态评价无法捕捉agent适应行为导致的性能变化。

- design_requirement_cn：评价应在部署环境中进行，考虑agents的适应性行为。

- artifact_choice_cn：采用agent-based simulation，让agents在模拟的CABS中互动并产生emergence。

- evaluated_contrast_cn：对模拟模型进行非线性验证，并对长期/短期窗口进行AIC比较。

- objective_result_cn：非线性模型在所有设置中优于线性模型，证明模拟产生复杂性。

##### evidence_pointers

1. Complexity in the Agent-Based Simulation Model

2. Figure 7

## 评价逻辑

### evaluation_modes

1. agent-based simulation

2. AIC-based non-linear model fitting and window comparison

3. parameter sweep with linear regression

4. contrast with no recommender and one-sided recommender baselines

- why_these_evaluations_cn：由于复杂系统中不可约不确定性无法用真实数据预测，作者选择agent-based simulation来生成一个具有emergence的虚拟CABS；用AIC窗口比较衡量系统波动的taming效果；用参数扫描+回归衡量agent绩效提升。这种评价策略能将设计差异转化为可量化的客观指标。

- benchmark_and_contrast_chain_cn：先用no recommender作为自然baseline，再用one-sided recommender作为现有技术baseline，最后用two-sided recommender作为新设计；在taming分析中通过AIC比较三种设置的拟合误差，在fitness分析中通过回归系数比较三种设置的平均fitness；稳健性通过改变窗口大小和参数变量实现。

### claim_evidence_ledger

#### 1. one-sided recommender比no recommender更好地tame不确定性（H1a）

- claim_cn：one-sided recommender比no recommender更好地tame不确定性（H1a）

- evidence_cn：大学侧AIC均值显著更低（p=3.327e-09），但学生侧不显著（p=0.224），因此部分支持。

#### 2. two-sided recommender比no和one-sided更好地tame不确定性（H1b）

- claim_cn：two-sided recommender比no和one-sided更好地tame不确定性（H1b）

- evidence_cn：两侧AIC均值显著更低，p值分别为0.001/0.006，完全支持。

#### 3. one-sided recommender提升fitness（H2a）

- claim_cn：one-sided recommender提升fitness（H2a）

- evidence_cn：回归系数学生0.31、大学0.32，均显著，支持。

#### 4. two-sided recommender提升fitness，优于one-sided（H2b）

- claim_cn：two-sided recommender提升fitness，优于one-sided（H2b）

- evidence_cn：回归系数学生0.63、大学0.45，对比one-sided分别为0.31和0.13，支持。

- internal_validity_strategy_cn：通过参数扫描控制6个已知变量，使用线性回归控制混杂；每种参数组合运行100次模拟以减少随机波动；使用非参数Wilcoxon检验避免分布假设；对窗口大小进行稳健性分析。

- external_validity_strategy_cn：以MOOC教育平台为实证情境，将平台特征、学生和大学目标均来自真实平台观察和文献；模拟模型经过非线性验证以保证其与CABS特征一致；作者在限制条件中将结果限定于market intermediary stream和平台提供者模型。

- what_is_not_actually_tested_cn：未使用真实平台数据校准模拟；未测试算法公平性；未与其他设计（如搜索、定价机制、非推荐系统）对比；未包含财务指标；推荐算法的具体实现被简化为启发式，未与最先进的单边推荐算法比较。

## 贡献闭环

- technical_claim_cn：两阶段推荐系统在模拟环境中比单边推荐系统和无推荐系统更好地降低fitness波动并提升fitness。

- artifact_claim_cn：two-sided recommender framework作为一个可实例化的设计制品，其核心设计差异（考虑双边emergence）导致了改进。

- mechanism_claim_cn：改进来自于two-sided推荐系统能够持续学习两侧emergence及其相互影响，从而为agents提供更适应环境变化的推荐，使其能够coevolve。

- boundary_claim_cn：结果适用于market intermediary stream中的平台提供者模型，尤其适用于像MOOC教育平台这样的双边平台；不同复杂系统可能需要不同的taming方法。

- reusable_design_knowledge_cn：为处理CABS中的不可约不确定性，IT制品应被设计为系统中的agent而非外部控制器，应学习多边emergence而非仅收集历史数据；评价此类制品应使用前瞻性agent-based simulation而非静态hold-out。

- theoretical_contribution_cn：为CABS理论提供了一种IT-based taming机制，表明自适应推荐系统能够使agents coevolve and learn；同时扩展了推荐系统理论，将其置于复杂系统中，指出单边推荐和静态评价的局限性。

- how_discussion_closes_intro_gap_cn：引言指出现有方案无法驯服不可约不确定性；讨论部分重新连接这一缺口，主张two-sided推荐系统通过考虑双边emergence提供了adaptive IS solution，并用冷启动问题说明单边推荐的失败机制，最后将结果定位为对CABS理论的一个具体实现的验证。

- overclaim_or_unsupported_leaps_cn：作者将简单启发式实例化结果推广为框架层面的结论，可能过度强调two-sided优于one-sided的一般性，而未与最先进推荐算法对比；另外，AIC降低被解释为taming，但缺乏对taming构念的直接测量；fitness提升是在模拟中，未在真实平台中验证，外部有效性有限。

## 句级写作动作图谱

### 1. Abstract P1 S1

- order：1

- section：Abstract

- locator：Abstract P1 S1

- move_code：CONTEXT

- paraphrase_cn：研究数字多边平台，将其看作具有不同且演化目标、偏好和约束的复杂适应商业系统。

- rhetorical_function_cn：文章开头即建立核心视角：平台= CABS。

- depends_on_cn：无，独立开篇。

- sets_up_cn：为后文将搜索匹配问题定义为复杂问题提供概念基础。

- evidence_pointer：Abstract, 第一句

### 2. Abstract P2 S1

- order：2

- section：Abstract

- locator：Abstract P2 S1

- move_code：GAP

- paraphrase_cn：指出收集和处理数据的传统方法无法降低不可约不确定性。

- rhetorical_function_cn：在摘要中快速定位现有方法局限。

- depends_on_cn：CABS视角。

- sets_up_cn：引出taming的新目标。

- evidence_pointer：Abstract, 第二句

### 3. Abstract P2 S2

- order：3

- section：Abstract

- locator：Abstract P2 S2

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：提出使用推荐系统让代理共同进化和学习来驯服复杂性。

- rhetorical_function_cn：给出解决办法。

- depends_on_cn：GAP。

- sets_up_cn：引出two-sided推荐系统。

- evidence_pointer：Abstract, 第三句

### 4. Introduction P1 S1

- order：4

- section：Introduction

- locator：Introduction P1 S1

- move_code：CONTEXT

- paraphrase_cn：将数字多边平台视为CABS，重点研究平台提供者模式。

- rhetorical_function_cn：开篇明确研究对象。

- depends_on_cn：无。

- sets_up_cn：为后续复杂搜索匹配问题提供平台语境。

- evidence_pointer：Introduction 第1段第1句

### 5. Introduction P2 S1

- order：5

- section：Introduction

- locator：Introduction P2 S1

- move_code：PHENOMENON

- paraphrase_cn：平台中可能存在良性循环或恶性循环。

- rhetorical_function_cn：用熟悉的平台现象说明匹配问题的重要性。

- depends_on_cn：平台作为CABS的定义。

- sets_up_cn：引出virtuous/vicious cycles导致匹配困难。

- evidence_pointer：Introduction 第2段第1句

### 6. Introduction P2 S4

- order：6

- section：Introduction

- locator：Introduction P2 S4

- move_code：PRACTICAL_STAKES

- paraphrase_cn：当买卖双方数量增加时，参与者更难找到合适匹配，可能导致退出或活动减少。

- rhetorical_function_cn：说明匹配问题的实际后果。

- depends_on_cn：平台循环现象。

- sets_up_cn：为提出搜索匹配问题的重要性铺路。

- evidence_pointer：Introduction 第2段第4句

### 7. Introduction P3 S1

- order：7

- section：Introduction

- locator：Introduction P3 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：复杂问题由许多不同部分适应并重组，无法找到最优解。

- rhetorical_function_cn：引入复杂性问题的一般定义。

- depends_on_cn：无。

- sets_up_cn：将搜索匹配问题类比为复杂问题。

- evidence_pointer：Introduction 第3段第1句

### 8. Introduction P3 S2

- order：8

- section：Introduction

- locator：Introduction P3 S2

- move_code：PHENOMENON

- paraphrase_cn：平台上的搜索匹配问题恰好具有这些复杂特征。

- rhetorical_function_cn：建立一般复杂问题与平台搜索匹配的对应。

- depends_on_cn：复杂问题定义。

- sets_up_cn：论证平台匹配是复杂问题，不能简单优化。

- evidence_pointer：Introduction 第3段第2句

### 9. Introduction P4 S1

- order：9

- section：Introduction

- locator：Introduction P4 S1

- move_code：MECHANISM

- paraphrase_cn：平台参与者多样性、非对称依赖和演化关系导致非线性互动和不可预测结果。

- rhetorical_function_cn：解释为什么平台匹配是复杂的。

- depends_on_cn：复杂问题定义。

- sets_up_cn：引出emergence和irreducible uncertainty。

- evidence_pointer：Introduction 第4段第1句

### 10. Introduction P5 S2

- order：10

- section：Introduction

- locator：Introduction P5 S2

- move_code：MECHANISM

- paraphrase_cn：非线性互动和涌现对参与者产生不可约不确定性，形成复杂搜索匹配问题。

- rhetorical_function_cn：将非线性与涌现转化为搜索匹配问题。

- depends_on_cn：非线性互动机制。

- sets_up_cn：为taming目标提供理论基础。

- evidence_pointer：Introduction 第5段第2句

### 11. Introduction P5 S4

- order：11

- section：Introduction

- locator：Introduction P5 S4

- move_code：THEORY_PROPOSITION

- paraphrase_cn：面对不可约不确定性，重点应从减少不确定性转向驯服不确定性。

- rhetorical_function_cn：提出核心理论命题。

- depends_on_cn：不可约不确定性定义。

- sets_up_cn：定义驯服并引出新方法。

- evidence_pointer：Introduction 第5段第4句

### 12. Introduction P6 S1

- order：12

- section：Introduction

- locator：Introduction P6 S1

- move_code：LIMITATION

- paraphrase_cn：现有方法（过滤、标签、单边推荐）有一定帮助但非常有限。

- rhetorical_function_cn：指出现有方案不足。

- depends_on_cn：taming命题。

- sets_up_cn：为提出two-sided推荐系统创造缺口。

- evidence_pointer：Introduction 第6段第1句

### 13. Introduction P6 S3

- order：13

- section：Introduction

- locator：Introduction P6 S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：提出一个两阶段推荐系统框架，通过考虑平台双边涌现性来驯服不可约不确定性。

- rhetorical_function_cn：提出本文核心设计提案。

- depends_on_cn：现有方法局限。

- sets_up_cn：为后续框架设计做铺垫。

- evidence_pointer：Introduction 第6段第3句

### 14. Introduction P7 S1

- order：14

- section：Introduction

- locator：Introduction P7 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：在MOOC平台情境中研究该问题，学生和大学作为agent建模。

- rhetorical_function_cn：预告具体应用场景。

- depends_on_cn：two-sided推荐系统目标。

- sets_up_cn：为agent-based simulation设立上下文。

- evidence_pointer：Introduction 第7段第1句

### 15. Theoretical Foundations, Digital Multisided Platforms as CABS P1 S1

- order：15

- section：Theoretical Foundations

- locator：Theoretical Foundations, Digital Multisided Platforms as CABS P1 S1

- move_code：THEORY_INTRO

- paraphrase_cn：CABS元素具有多样性、适应、连接和相互依赖四个中度性质。

- rhetorical_function_cn：引入CABS理论的基本属性。

- depends_on_cn：无。

- sets_up_cn：用于映射数字平台特征。

- evidence_pointer：Theoretical Foundations 第1段

### 16. Search Matching P1 S1

- order：16

- section：Theoretical Foundations

- locator：Search Matching P1 S1

- move_code：PHENOMENON

- paraphrase_cn：平台虽促进交易，但当参与者增多时，寻找匹配变得更加困难。

- rhetorical_function_cn：描述搜索匹配问题的经验表现。

- depends_on_cn：平台作为CABS。

- sets_up_cn：为后续复杂性分析提供例证。

- evidence_pointer：Search Matching 第1段第1句

### 17. Search Matching P2 S1

- order：17

- section：Theoretical Foundations

- locator：Search Matching P2 S1

- move_code：MECHANISM

- paraphrase_cn：平台参与者目标、行为、资源和连接不同，发展非对称依赖，导致非线性互动。

- rhetorical_function_cn：解释平台复杂性来源。

- depends_on_cn：CABS属性。

- sets_up_cn：论证不可约不确定性的产生。

- evidence_pointer：Search Matching 第2段

### 18. Search Matching P5 S1

- order：18

- section：Theoretical Foundations

- locator：Search Matching P5 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：多个研究在P2P网络、在线社区等情境中发现了类似的规模增长导致参与下降的问题。

- rhetorical_function_cn：引用已有证据支持问题普遍性。

- depends_on_cn：不可约不确定性概念。

- sets_up_cn：说明搜索匹配问题的跨情境重要性。

- evidence_pointer：Search Matching 第5段

### 19. Existing Approaches P1 S1

- order：19

- section：Existing Approaches

- locator：Existing Approaches P1 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：现有平台采用人类驱动和平台驱动两类方法。

- rhetorical_function_cn：分类总结现有方案。

- depends_on_cn：问题定义。

- sets_up_cn：为critique提供对象。

- evidence_pointer：Existing Approaches 第1段第1句

### 20. Existing Approaches P2 S1

- order：20

- section：Existing Approaches

- locator：Existing Approaches P2 S1

- move_code：LIMITATION

- paraphrase_cn：这些静态策略因锁定参与者、无法捕获偏好变化等原因，无法驯服不可约不确定性。

- rhetorical_function_cn：系统说明现有方法的缺陷。

- depends_on_cn：现有方法分类。

- sets_up_cn：为推荐系统方案的引入提供动机。

- evidence_pointer：Existing Approaches 第2段

### 21. Two-Sided Recommender Systems P4 S1

- order：21

- section：Recommender Systems / Two-Sided

- locator：Two-Sided Recommender Systems P4 S1

- move_code：LIMITATION

- paraphrase_cn：传统推荐系统只服务一侧，假设未来与过去相似，因此未设计用来处理复杂系统。

- rhetorical_function_cn：指出单边推荐在复杂系统中的根本局限。

- depends_on_cn：现有推荐系统文献。

- sets_up_cn：引出two-sided框架的必要性。

- evidence_pointer：Two-Sided Recommender Systems 第4段第1句

### 22. Two-Sided Recommender Systems P7 S1

- order：22

- section：Recommender Systems / Two-Sided

- locator：Two-Sided Recommender Systems P7 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：在我们方法中，两阶段推荐系统本身是CABS中的一个agent。

- rhetorical_function_cn：描述新设计的核心特征。

- depends_on_cn：单边推荐局限。

- sets_up_cn：为agent-based模拟建模提供直接依据。

- evidence_pointer：Two-Sided Recommender Systems 第7段第1句

### 23. Hypotheses P1 S1

- order：23

- section：Hypotheses

- locator：Hypotheses P1 S1

- move_code：THEORY_INTRO

- paraphrase_cn：数字平台是CABS，agents面对随时间变化的local和global optima性能景观。

- rhetorical_function_cn：重述理论基础以推导假设。

- depends_on_cn：CABS理论。

- sets_up_cn：为coevolution优于prediction的论点提供背景。

- evidence_pointer：Hypotheses 第1段第1句

### 24. Hypotheses P2 S1

- order：24

- section：Hypotheses

- locator：Hypotheses P2 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：为评估推荐系统，考虑无推荐、单边推荐和两阶段推荐三种变体。

- rhetorical_function_cn：预告实验设计。

- depends_on_cn：推荐系统方案。

- sets_up_cn：定义baseline和对照。

- evidence_pointer：Hypotheses 第2段第1句

### 25. Hypotheses P2 S4

- order：25

- section：Hypotheses

- locator：Hypotheses P2 S4

- move_code：MECHANISM

- paraphrase_cn：单边推荐无法完全学习另一侧的涌现，因为它只处理本侧数据。

- rhetorical_function_cn：解释单边推荐的机制缺陷。

- depends_on_cn：CABS涌现性。

- sets_up_cn：支持two-sided优势假设。

- evidence_pointer：Hypotheses 第2段第4句

### 26. Hypotheses H1a/H1b

- order：26

- section：Hypotheses

- locator：Hypotheses H1a/H1b

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：提出H1a：单边推荐比无推荐更好地tame复杂搜索匹配；H1b：两阶段推荐比无推荐和单边推荐都更好。

- rhetorical_function_cn：正式提出taming效果的假设。

- depends_on_cn：机制分析。

- sets_up_cn：为结果分析提供检验对象。

- evidence_pointer：Hypotheses 假设1a/1b

### 27. Hypotheses P5 S2

- order：27

- section：Hypotheses

- locator：Hypotheses P5 S2

- move_code：CONTEXT

- paraphrase_cn：引入fitness概念，代表agent继续参与价值增强交易的总体能力。

- rhetorical_function_cn：为agent绩效定义可测量构念。

- depends_on_cn：agents的目标。

- sets_up_cn：为H2的fitness衡量奠定基础。

- evidence_pointer：Hypotheses 第5段第2句

### 28. Hypotheses H2a/H2b

- order：28

- section：Hypotheses

- locator：Hypotheses H2a/H2b

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：提出H2a和H2b：随着不确定性增加，单边/两阶段推荐系统能够提升平均fitness。

- rhetorical_function_cn：提出fitness改善假设。

- depends_on_cn：fitness定义。

- sets_up_cn：为后续回归分析提供目标。

- evidence_pointer：Hypotheses 假设2a/2b

### 29. Agent-Based Model Design P1 S1

- order：29

- section：Agent-Based Model Design

- locator：Agent-Based Model Design P1 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：Agent-based模拟被广泛用于CABS研究，因为它能简约建模复杂现象并研究宏观emergence。

- rhetorical_function_cn：为选择模拟方法提供依据。

- depends_on_cn：CABS研究传统。

- sets_up_cn：说明后续模拟设计的合理性。

- evidence_pointer：Agent-Based Model Design 第1段第1句

### 30. Agent-Based Model Design P2 S1

- order：30

- section：Agent-Based Model Design

- locator：Agent-Based Model Design P2 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：模拟中使用面向对象编程，用变量和数据结构表示agent属性，而非字符串。

- rhetorical_function_cn：描述模拟的技术实现选择。

- depends_on_cn：建模需求。

- sets_up_cn：为后续定义fitness和行为规则提供基础。

- evidence_pointer：Agent-Based Model Design 第2段第1句

### 31. Two-Sided Recommender System P3 S1

- order：31

- section：Two-Sided Recommender System

- locator：Two-Sided Recommender System P3 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：两阶段推荐系统向学生推荐课程、同伴和讨论板，同时向大学推荐开设课程、专业和时间。

- rhetorical_function_cn：描述推荐系统的具体操作。

- depends_on_cn：two-sided框架。

- sets_up_cn：对比one-sided的说法。

- evidence_pointer：Two-Sided Recommender System 第3段

### 32. Complexity in Simulation P1 S1

- order：32

- section：Complexity in the Agent-Based Simulation Model

- locator：Complexity in Simulation P1 S1

- move_code：RESULT

- paraphrase_cn：模拟模型表现出复杂性，并不随时间稳定。

- rhetorical_function_cn：报告模拟模型的复杂性验证结果。

- depends_on_cn：模拟运行。

- sets_up_cn：为后文将AIC作为taming指标做铺垫。

- evidence_pointer：Complexity in the Agent-Based Simulation Model 第1段

### 33. Results Taming P4 S1

- order：33

- section：Results

- locator：Results Taming P4 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：使用Wilcoxon符号秩检验比较AIC均值。

- rhetorical_function_cn：说明统计检验方法。

- depends_on_cn：AIC窗口分析。

- sets_up_cn：为假设支持与否提供统计依据。

- evidence_pointer：Results/Taming Complex Search Matching 第4段

### 34. Results Taming P5 S1

- order：34

- section：Results

- locator：Results Taming P5 S1

- move_code：RESULT

- paraphrase_cn：两阶段推荐系统的AIC均值在两侧都显著低于无推荐和单边推荐。

- rhetorical_function_cn：报告H1b检验结果。

- depends_on_cn：窗口AIC计算和检验。

- sets_up_cn：证明two-sided的taming优势。

- evidence_pointer：Results/Taming Complex Search Matching 第5段

### 35. Results Improving Agent Performance P3 S1

- order：35

- section：Results

- locator：Results Improving Agent Performance P3 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用线性回归估计各变量对平均fitness的影响。

- rhetorical_function_cn：说明参数扫描数据的分析方法。

- depends_on_cn：参数扫描实验。

- sets_up_cn：为报告回归系数建立框架。

- evidence_pointer：Results/Improving Agent Performance 第3段

### 36. Results Improving Agent Performance P6 S1

- order：36

- section：Results

- locator：Results Improving Agent Performance P6 S1

- move_code：RESULT

- paraphrase_cn：两阶段推荐系统相较无推荐，学生fitness提高0.63，大学提高0.45；相较单边推荐，分别提高0.31和0.13。

- rhetorical_function_cn：报告H2b检验的主要结果。

- depends_on_cn：线性回归模型。

- sets_up_cn：支持fitness改善主张。

- evidence_pointer：Results/Improving Agent Performance 第6段

### 37. Discussion P1 S1

- order：37

- section：Discussion

- locator：Discussion P1 S1

- move_code：CONTRIBUTION

- paraphrase_cn：两阶段推荐框架作为自适应IS解决方案能驯服CABS中的复杂问题。

- rhetorical_function_cn：开头即声明核心贡献。

- depends_on_cn：结果。

- sets_up_cn：为后续讨论理论含义铺路。

- evidence_pointer：Discussion 第1段

### 38. Discussion P3 S1

- order：38

- section：Discussion

- locator：Discussion P3 S1

- move_code：MECHANISM

- paraphrase_cn：用冷启动问题说明单边推荐只推荐成熟卖家，忽略新进入者。

- rhetorical_function_cn：用具体机制解释单边推荐为何在双边平台失败。

- depends_on_cn：单边推荐局限性。

- sets_up_cn：说明two-sided考虑双边目标的重要性。

- evidence_pointer：Discussion 第3段

### 39. Limitations P1 S1

- order：39

- section：Limitations

- locator：Limitations P1 S1

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：结果限于market intermediary stream的platform provider model。

- rhetorical_function_cn：明确研究的适用范围。

- depends_on_cn：平台分类。

- sets_up_cn：为未来推广提供边界。

- evidence_pointer：Limitations 第1段

### 40. Implications Recommender P3 S1

- order：40

- section：Implications for Recommender Systems and IS Research

- locator：Implications Recommender P3 S1

- move_code：CONTRIBUTION

- paraphrase_cn：推荐系统评价应在部署环境中进行，并考虑所有侧的适应行为，模拟是一种重要手段。

- rhetorical_function_cn：将结果推广为方法论建议。

- depends_on_cn：模拟实验经验。

- sets_up_cn：为推荐系统研究社区提供前瞻性评价思路。

- evidence_pointer：Implications for Recommender Systems 第3段

### 41. Implications Complexity P1 S1

- order：41

- section：Implications for Complexity Science

- locator：Implications Complexity P1 S1

- move_code：CONTRIBUTION

- paraphrase_cn：两阶段推荐系统作为IT制品能增强平台驯服复杂搜索匹配问题的能力。

- rhetorical_function_cn：对复杂科学领域声明贡献。

- depends_on_cn：结果和CABS理论。

- sets_up_cn：指出多种复杂系统可能需要不同taming方法。

- evidence_pointer：Implications for Complexity Science 第1段

## 写作技术

- gap_construction_cn：先建立CABS视角，说明不可约不确定性无法由数据减少；再逐一否定现有方案（人类分组、平台搜索、单边推荐、静态评价），指出它们忽视了双边emergence，从而留下'需要一种考虑双边涌现性的推荐系统'的缺口。

- signposting_cn：引言末尾明确列出论文后续各节内容；每个主要部分有标题和小结；Table 6用设计科学指南映射论文结构，给读者清晰的路线图。

- transition_logic_cn：每个阶段结束时用总结句将理论缺口引向下一阶段，例如从现有方法局限过渡到推荐系统方案，从框架设计过渡到模拟实现，从复杂性验证过渡到taming分析，从taming分析过渡到fitness分析。

- claim_evidence_rhythm_cn：每个假设先陈述理论机制，再描述实验操作，最后报告统计检验结果；H1和H2分别用AIC窗口分析和回归分析，形成'降低波动+提升水平'的双重证据。

- benchmark_narrative_cn：将no recommender定义为base case，将one-sided定义为existing framework，将two-sided定义为proposed framework，从而形成清晰的阶梯式比较；AIC和回归系数均以相对差异呈现。

- theory_return_cn：在Discussion和Implications中，将two-sided推荐系统的成功归因于CABS理论中的coevolution和emergence概念，强调这是对Tanriverdi等命题的具体例证，并将结果抽象为'IT制品可作为taming机制'。

- contribution_positioning_cn：将贡献分层：技术贡献为模拟证据，设计贡献为two-sided框架，理论贡献为CABS理论提供了adaptive IT机制，方法论贡献为agent-based simulation作为推荐系统评价手段。

- novelty_protection_cn：通过反复对比one-sided与two-sided的机制差异（是否学习另一侧emergence），将two-sided的优势归因于框架级设计而非算法细节，避免被视为特定参数调优；同时承认算法是简单启发式，强调框架可扩展，从而保护贡献的一般性。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：建立现实问题（平台匹配困难）并引入理论视角（CABS）。

- research_job_cn：完成文献综合，论证该问题具有复杂性和不可约不确定性。

- required_evidence_cn：平台实例或文献证据表明传统方法无法解决。

- transition_to_next_cn：指出需要新的IS方案来驯服不确定性。

#### 2. 2

- step：2

- writing_job_cn：定义现有解决方案的类别并逐类批评。

- research_job_cn：综述人类驱动和平台驱动方法，以及单边推荐系统的局限。

- required_evidence_cn：文献或逻辑论证证明这些方法不考虑双边emergence。

- transition_to_next_cn：推荐系统是最自然方案，但需要改变为两阶段。

#### 3. 3

- step：3

- writing_job_cn：提出新的制品/框架并说明其设计特征。

- research_job_cn：将理论命题转化为具体设计（two-sided）。

- required_evidence_cn：机制逻辑说明新设计如何解决前文缺口。

- transition_to_next_cn：提出可检验假设。

#### 4. 4

- step：4

- writing_job_cn：选择一个能生成复杂动态的评价环境。

- research_job_cn：建立agent-based simulation模型，并验证模型产生非线性。

- required_evidence_cn：非线性模型AIC优于线性模型，证明复杂性存在。

- transition_to_next_cn：在已建立的复杂环境中比较不同设计。

#### 5. 5

- step：5

- writing_job_cn：检验taming效果（波动降低）。

- research_job_cn：用AIC窗口比较新框架与baseline。

- required_evidence_cn：统计显著且稳健的AIC差异。

- transition_to_next_cn：证明taming后，还需要验证实际fitness改善。

#### 6. 6

- step：6

- writing_job_cn：检验agent绩效改善。

- research_job_cn：参数扫描+回归分析比较不同条件下的平均fitness。

- required_evidence_cn：回归系数支持假设，并控制其他变量。

- transition_to_next_cn：用结果讨论理论含义和边界。

#### 7. 7

- step：7

- writing_job_cn：把结果抽象为一般设计知识和理论贡献。

- research_job_cn：从机制层面解释成功原因，明确边界和未来方向。

- required_evidence_cn：证据链与理论机制的对应。

- transition_to_next_cn：结束文章。

### most_transferable_moves_cn

1. 从理论概念（CABS）推导问题类型（不可约不确定性）并据此设计IT制品的思路

2. 将现有方案分类后逐一批评，并指出共同缺陷（忽视另一侧）

3. 引入三档比较：无干预、现有技术、新技术

4. 用AIC模型拟合检验模拟模型是否产生复杂性

5. 将'驯服'操作化为性能波动的降低，并用窗口分析测量

6. 用参数扫描+回归控制混杂，估计设计差异的效应

### resource_intensive_or_nonstandard_parts_cn

1. agent-based simulation模型需要大量设计工作，包括建模agent属性、行为规则、fitness更新逻辑

2. 模拟运行需要计算资源（多参数×100次×1000期）

3. MOOC平台具体情境和文献基础不可随意复制

4. AIC窗口分析和非线性验证需要统计知识

### what_not_to_copy_superficially_cn

1. 如果没有真正构建agent-based模型并验证复杂性，就不能宣称taming效果

2. 如果没有与one-sided baseline对比，就不能将贡献归功于two-sided框架

3. 如果只用模拟数据而未结合理论机制解释，AIC差异只是一次性结果

4. 不应忽视文章列明的边界（market intermediary stream、MOOC情境）而过度一般化

- single_best_description_of_the_routine_cn：先以理论把问题抬高为复杂系统问题，再指出现有方案的理论缺陷，然后提出一个理论驱动的框架级设计，用一个能产生复杂性的模拟环境做阶梯式比较，最后把结果上升为对理论的印证。

## 分析边界

分析基于提供的全文，包含附录A-E；由于没有真实页码，句子定位使用段落和句数近似；对于部分图表（如Figure 7、8）仅能依据引用位置，无法逐像素分析。
