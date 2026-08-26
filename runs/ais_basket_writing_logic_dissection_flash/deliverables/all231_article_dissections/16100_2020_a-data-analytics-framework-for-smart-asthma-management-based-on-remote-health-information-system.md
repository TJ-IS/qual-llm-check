# A Data Analytics Framework for Smart Asthma Management Based on Remote Health Information Systems with Bluetooth-Enabled Personal Inhalers

- 作者：Junbo Son; Patricia Flatley Brennan; Shiyu Zhou
- 年份 / 期刊：2020 / MIS Quarterly
- DOI：10.25300/misq/2020/15092
- 源文件：16100_2020_a-data-analytics-framework-for-smart-asthma-management-based-on-remote-health-information-system.md
- 论文主类型：computational_artifact_benchmark
- 主导写作弧线：performance_gap_artifact_benchmark_generalize
- 置信度：0.9

## 文章级论证概况

- 核心问题：如何利用SAM系统提供的蓝牙吸入器高频使用日志，设计专门的数据分析框架来检测偏离患者正常模式的异常吸入器使用，从而改善哮喘自我管理？

- 制品与设计：制品是一个三步数据分析框架：将纵向吸入器使用事件转换为24×7网格数据；拟合GLMM-GQP模型（均值模型含患者和网格级随机效应，离散模型用环境因素刻画变异性，CAR模型刻画同小时窗口跨天相关）；基于模型预测概率构建个性化概率网格，并通过阈值判定异常。

- 客观结果：在真实SAM数据集上，以AUC为主要指标，GLMM-GQP在大多数训练数据量条件下优于GLMM-P、GLMM-NB、GLMM-GQPS、逻辑回归、SVM和CG-HMM；GLMM-GQPS次之，验证了CAR结构的贡献；CG-HMM几乎无法检测异常。

- 核心贡献：提出并验证了GLMM-GQP方法，填补了SAM数据下异常吸入器检测的方法空白；扩展了HIS定义，展示了针对新型HIS设计专属分析制品的重要性；提出可复用的设计原则（准确事件时间、相关协变量、充足目标患者数据、患者行为知识）。

- 整篇论证链：作者首先指出传统哮喘管理基于阈值和自报数据的局限，并引入新型SAM系统提供高分辨率吸入器使用日志；然后论证现有统计模型（GLMM、SVM、CG-HMM）无法同时处理患者间异质性、环境触发因素对变异性的影响以及日常例程导致的相关结构；因此提出GLMM-GQP，将网格化转换、准泊松离散模型和CAR相关结构集成起来；接着在真实数据上通过构造TP和TN场景进行离线评价，以AUC和误报/漏报率比较七个方法，证明GLMM-GQP的优越性；最后将结果上升为设计知识和实践指南，并定位为设计科学中的exaptation贡献。

## 类型与写作弧线判定

- 论文主类型判定：文章核心贡献是开发计算分析制品GLMM-GQP，主要证据来源于真实数据集上的离线性能benchmark（AUC、错误率、时间到警报），没有进行现场部署或干预实验，因此属于以计算制品和benchmark为主要证据的类型。

- 主导写作弧线判定：文章从传统数据分辨率低导致现有方法无法检测异常的性能缺口入手，提出新制品GLMM-GQP，通过系统性benchmark对比展示性能改进，最后从结果中提取适用于其他健康监测场景的通用设计知识，完全符合该写作弧线。

## 研究开展程序

- study_or_phase_count：7

- 研究阶段总序列：研究依次完成问题化、数据获取、数据转换、模型构建、检测算法、离线评价和知识提取七个阶段。问题化阶段确立SAM数据催生的新需求；数据获取揭示数据特征；数据转换将纵向数据变为网格格式；模型构建针对数据特征发展GLMM-GQP；检测算法将模型输出转化为异常标志；离线评价通过构造异常场景验证性能并量化组件贡献；最后从评价结果中提炼设计知识和适用边界。各阶段环环相扣，下一阶段解决上一阶段留下的不确定性。

### studies_or_phases

#### 1. 问题化与需求分析

- order：1

- name_cn：问题化与需求分析

- question_cn：SAM系统的高分辨率数据提出了什么现有方法无法满足的分析需求？

- inputs_and_setting_cn：哮喘管理现状、传统临床试验数据特征、SAM系统的技术能力。

- designed_or_compared_object_cn：比较阈值方法、GLMM、SVM和CG-HMM等现有方法的适用范围。

- baseline_control_or_counterfactual_cn：传统趋势检测方法作为对比参照。

##### objective_metrics

（空）

- analysis_method_cn：文献综合与推理

- main_result_cn：确认需要同时处理患者异质性、环境因素对变异性的影响和日常例程相关性的新方法。

- argumentative_role_cn：建立研究缺口并设定研究目标。

- remaining_uncertainty_cn：新方法的具体形式尚未确定。

- link_to_next_phase_cn：需要真实数据来测试和开发方法。

##### evidence_pointers

1. Introduction P2–P7

2. Literature Review

#### 2. 测试平台与数据收集

- order：2

- name_cn：测试平台与数据收集

- question_cn：SAM数据包含哪些变量、具有何种分布特征？

- inputs_and_setting_cn：Propeller Health部署的真实SAM系统，2014–2017年美国中西部城市，326名有效参与者。

- designed_or_compared_object_cn：数据变量集（人口、ACT、环境因素、事件时间戳）

- baseline_control_or_counterfactual_cn：无

##### objective_metrics

1. 均值

2. 标准差

3. 比例

- analysis_method_cn：描述性统计

- main_result_cn：样本中68%为女性、68.7%白种人、77%基线ACT控制良好；吸入器使用频率低。

- argumentative_role_cn：提供数据基础，突出数据低频、不平衡等特征以证明需要特制模型。

- remaining_uncertainty_cn：数据的时间相关结构和环境因素影响尚需建模。

- link_to_next_phase_cn：这些特征要求数据变换和统计建模。

##### evidence_pointers

1. Data Description

2. Table 2

#### 3. 数据转换（Step 1）

- order：3

- name_cn：数据转换（Step 1）

- question_cn：如何将纵向SAM数据转换成能揭示使用模式并适配建模的格式？

- inputs_and_setting_cn：每个患者的吸入器事件时间戳，以小时为单位。

- designed_or_compared_object_cn：24×7网格（168个单元格）

- baseline_control_or_counterfactual_cn：原始时间序列格式作为对比。

##### objective_metrics

1. 网格内使用次数分布

- analysis_method_cn：数据聚合与可视化

- main_result_cn：良好控制患者中超过1次使用的网格不到2%，差控制患者约25%的网格有多次使用。

- argumentative_role_cn：将时间序列转化为可直接建模的相关结构，同时提供可视化工具。

- remaining_uncertainty_cn：网格划分是否最优，模型如何运用这些网格。

- link_to_next_phase_cn：网格化数据用于GLMM-GQP建模。

##### evidence_pointers

1. Step 1: Data Transformation

2. Figure 3

3. Figure 4

#### 4. 统计模型构建（Step 2）

- order：4

- name_cn：统计模型构建（Step 2）

- question_cn：如何建模网格化的吸入器使用计数，并整合异质性、变异性和相关性？

- inputs_and_setting_cn：168个网格计数、人口变量、环境因素（温度、湿度、PM2.5等）。

- designed_or_compared_object_cn：GLMM-GQP模型本身（均值模型、离散模型、CAR随机效应结构）。

- baseline_control_or_counterfactual_cn：常规GLMM、无CAR结构的简化版本等作为后续基准。

##### objective_metrics

1. 参数估计

2. 标准误

3. p值

- analysis_method_cn：h-likelihood推断，迭代加权最小二乘和调整轮廓似然。

- main_result_cn：性别和ACT显著影响使用强度；温度、湿度、PM2.5和风速显著影响离散性；患者随机效应方差为2.284，网格相关ρ=0.15。

- argumentative_role_cn：建立个性化概率预测模型，为异常检测提供基础。

- remaining_uncertainty_cn：参数模型在检测任务中的实际性能尚待验证。

- link_to_next_phase_cn：模型预测用于Step 3的异常检测。

##### evidence_pointers

1. Step 2: Statistical Modeling

2. Equations (1)-(2)

3. Table 3

#### 5. 异常检测算法（Step 3）

- order：5

- name_cn：异常检测算法（Step 3）

- question_cn：如何根据GLMM-GQP的预测概率识别一次吸入器使用是否异常？

- inputs_and_setting_cn：拟合的GLMM-GQP参数、患者i在网格k的预测均值λ和离散θ。

- designed_or_compared_object_cn：个性化概率网格和阈值δ判定规则。

- baseline_control_or_counterfactual_cn：无

##### objective_metrics

1. 预测概率P(y>0)

- analysis_method_cn：用负二项分布近似准泊松概率，比较预测概率与阈值。

- main_result_cn：定义了in-pattern网格（P≥δ）和out-of-pattern网格，后者触发警报。

- argumentative_role_cn：将统计模型转化为可操作的检测工具。

- remaining_uncertainty_cn：检测性能需要系统评价。

- link_to_next_phase_cn：进入性能评价环节。

##### evidence_pointers

1. Step 3: Out-of-Pattern Inhaler Usage Detection

2. Figure 6

#### 6. 离线性能评价

- order：6

- name_cn：离线性能评价

- question_cn：GLMM-GQP是否优于现有benchmark方法？各设计组件是否有贡献？

- inputs_and_setting_cn：326名患者的SAM数据，构造异常场景（随机替换为他人数据）和正常场景。

- designed_or_compared_object_cn：GLMM-GQP对比GLMM-GQPS、GLMM-P、GLMM-NB、逻辑回归、SVM、CG-HMM，在k=1,4,8,12和近乎全部数据条件下。

- baseline_control_or_counterfactual_cn：随机猜测（AUC=0.5）及多个基准方法。

##### objective_metrics

1. AUC

2. 平均误报率

3. 平均漏报率

4. 平均时间到警报

- analysis_method_cn：重复100次的模拟实验，计算AUC和错误率。

- main_result_cn：GLMM-GQP在k≥4时AUC最高（0.81–0.85）；GLMM-GQPS次之；GLMM-P和GLMM-NB较低；逻辑回归和SVM误报高；CG-HMM AUC≈0.5。

- argumentative_role_cn：提供核心经验证据，证明制品有效性和组件必要性。

- remaining_uncertainty_cn：外部有效性（地理、人群）、实时警报效应未知。

- link_to_next_phase_cn：结果进入讨论，用于归纳设计知识和边界。

##### evidence_pointers

1. Performance Evaluation

2. Table 4

3. Figure 9

#### 7. 讨论与设计知识提取

- order：7

- name_cn：讨论与设计知识提取

- question_cn：本研究的贡献是什么？方法适用于哪些其他场景？

- inputs_and_setting_cn：性能评价结果、IS文献和设计科学框架。

- designed_or_compared_object_cn：无

- baseline_control_or_counterfactual_cn：无

##### objective_metrics

（空）

- analysis_method_cn：概念推理与文献定位

- main_result_cn：提出三项贡献（哮喘管理方法创新、GLMM-GQP模型、IS知识贡献），总结四项可复用设计要求，并指出实施中的挑战。

- argumentative_role_cn：将局部结果上升为通用设计知识，并划定适用边界。

- remaining_uncertainty_cn：临床实施和更多领域验证仍需未来研究。

- link_to_next_phase_cn：文章结束，未来方向指向EHR集成、多地区验证和COPD扩展。

##### evidence_pointers

1. Discussion and Conclusion

2. Guidelines for IS Researchers and Practitioners

## 各部分修辞架构

### abstract_moves

1. CONTEXT

2. PRACTICAL_STAKES

3. PHENOMENON

4. PRIOR_KNOWLEDGE

5. LIMITATION

6. GAP

7. RQ_OR_OBJECTIVE

8. DESIGN_FEATURE

9. RESULT

10. CONTRIBUTION

### introduction_moves

1. CONTEXT

2. PRACTICAL_STAKES

3. PHENOMENON

4. PRIOR_KNOWLEDGE

5. LIMITATION

6. PHENOMENON

7. GAP

8. WHY_GAP_MATTERS

9. RQ_OR_OBJECTIVE

10. THEORY_INTRO

11. LIMITATION

12. GAP

13. DESIGN_FEATURE

14. STUDY_OVERVIEW

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE

2. LIMITATION

3. PRIOR_KNOWLEDGE

4. LIMITATION

5. MECHANISM

6. REQUIREMENT

7. DESIGN_FEATURE

8. BENCHMARK_OR_CONTRAST

### artifact_design_moves

1. STUDY_OVERVIEW

2. CONTEXT

3. PRIOR_KNOWLEDGE

4. DESIGN_FEATURE

5. METHOD_JUSTIFICATION

6. DESIGN_FEATURE

7. THEORY_PROPOSITION

8. REQUIREMENT

9. DESIGN_FEATURE

10. METHOD_JUSTIFICATION

11. RESULT

12. DESIGN_FEATURE

### evaluation_moves

1. STUDY_OVERVIEW

2. METHOD_JUSTIFICATION

3. BENCHMARK_OR_CONTRAST

4. RESULT

5. ROBUSTNESS_OR_BOUNDARY_TEST

6. RESULT

7. ROBUSTNESS_OR_BOUNDARY_TEST

8. TRANSITION

### discussion_and_contribution_moves

1. CONTRIBUTION

2. PRACTICAL_STAKES

3. BOUNDARY_CONDITION

4. LIMITATION_AND_FUTURE

5. LIMITATION_AND_FUTURE

## 理论/知识到设计的翻译

### 知识/理论基础

1. 广义线性混合模型（GLMM）

2. 准泊松分布

3. 双广义线性模型（DGLM）

4. 条件自回归模型（CAR）

5. 哮喘临床知识（环境触发因素、日常例程、ACT分层）

6. 设计科学（exaptation）

- 理论—设计耦合：partial

- 耦合判定理由：文章没有基于行为或组织理论构建模型，而是基于统计建模文献和哮喘临床知识进行技术设计。统计理论（GLMM/DGLM/CAR）和领域知识直接影响了模型的结构选择（如离散模型、相关结构），但具体实现还受数据可用性和工程便利影响，并非由单一理论完整推导。同时，社会行为理论仅作为背景解释使用，没有实质决定设计，因此是部分耦合。

- 理论到设计翻译链：哮喘文献指出环境触发因素增加症状变异性而非仅均值，且患者日常例程导致同一小时窗口跨天正相关。统计知识提供准泊松分布和DGLM以建模离散性，提供CAR以建模相关结构。由此产生设计要求：模型必须同时包含均值模型、离散模型和结构化随机效应。这些要求转化为GLMM-GQP的具体制品选择：均值模型含患者和网格随机效应，离散模型含温度、湿度、PM2.5等环境变量，网格随机效应采用CAR相关矩阵。评价中通过GLMM-GQP vs GLMM-GQPS的对比验证CAR结构，通过GLMM-GQPS vs 常规GLMM的对比验证离散模型的价值。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：患者日常例程导致同一小时窗口跨天使用频率正相关（临床观察和反复活动模式）

- mechanism_cn：重复性日常活动会产生时间上规律性重复的吸入器使用，从而在同小时窗口跨界形成相关结构

- design_requirement_cn：模型应允许灵活指定网格之间的相关结构，而不是假设独立

- artifact_choice_cn：在网格级随机效应使用CAR模型，通过矩阵D定义同一小时窗口跨天相邻的网格为相关

- evaluated_contrast_cn：GLMM-GQP（包含CAR）对比GLMM-GQPS（无CAR，假设独立随机效应）

- objective_result_cn：GLMM-GQP在k≥4时AUC显著高于GLMM-GQPS（例如0.8543 vs 0.8257），支持CAR结构的贡献

##### evidence_pointers

1. Table 4

2. Figure 5

#### 2. 2

- theory_or_knowledge_claim_cn：环境触发因素（温度、湿度、PM2.5等）主要影响吸入器使用的变异性而非均值（Su et al. 2017）

- mechanism_cn：环境变化加剧症状波动，导致使用频率在不同时段之间的离散程度改变

- design_requirement_cn：需要建立专门的离散模型来刻画环境因素对变异性的影响

- artifact_choice_cn：使用准泊松分布并设定log(θ)与温度、PM2.5、湿度、能见度、风速的线性模型

- evaluated_contrast_cn：GLMM-GQP（含离散模型）对比GLMM-NB和GLMM-P（无离散模型）

- objective_result_cn：GLMM-GQP的AUC（0.8543）明显高于GLMM-NB（0.7409）和GLMM-P（0.6734），支持离散模型的价值

##### evidence_pointers

1. Table 3

2. Table 4

#### 3. 3

- theory_or_knowledge_claim_cn：传统临床试验数据低频，每日聚合无法反映微小时段的使用模式；因此需要保留事件时间戳

- mechanism_cn：高频数据能揭示短时模式，如一天中特定时间段的重复事件

- design_requirement_cn：模型应使用小时级时间窗口而不是每日聚合

- artifact_choice_cn：将事件转换为24×7网格，每个网格代表一个小时的窗口；检测基于小时级概率

- evaluated_contrast_cn：GLMM-GQP基于网格小时数据对比CG-HMM基于日聚合数据

- objective_result_cn：CG-HMM的AUC约0.5，几乎无法检测异常，而GLMM-GQP在数据充足时AUC>0.8

##### evidence_pointers

1. Table 4

2. Step 3

## 评价逻辑

### evaluation_modes

1. 离线历史数据模拟评估

2. 基准方法对比

3. 多数据量训练条件测试

4. 错误类型分解（误报/漏报）

5. 时间到警报分析

- why_these_evaluations_cn：需要验证检测算法在已知异常场景下有效，且要比较不同数据量条件下的表现，以说明模型对新患者的适用性和组件价值；同时区分误报和漏报以刻画实际使用风险。

- benchmark_and_contrast_chain_cn：先用GLMM-P和GLMM-NB检验基础GLMM能力；用GLMM-GQPS消融CAR结构；用逻辑回归和SVM检验非网格化、个体级分类器；用CG-HMM检验已有哮喘专用模型。AUC比较逐步累积证据：网格化+离散模型+相关结构各自贡献多少，最终显示GLMM-GQP综合优势。

### claim_evidence_ledger

#### 1. GLMM-GQP在AUC上优于所有benchmark方法

- claim_cn：GLMM-GQP在AUC上优于所有benchmark方法

- evidence_cn：Table 4中在k=4,8,12和almost all条件下GLMM-GQP的AUC最高；Figure 9显示GLMM-GQP在误报和漏报间更平衡。

#### 2. CAR相关结构对性能有贡献

- claim_cn：CAR相关结构对性能有贡献

- evidence_cn：GLMM-GQP vs GLMM-GQPS的AUC差异（如0.8543 vs 0.8257）和Figure 9中较低的漏报率。

#### 3. 离散模型（环境因素变异性）对性能有贡献

- claim_cn：离散模型（环境因素变异性）对性能有贡献

- evidence_cn：GLMM-GQP vs GLMM-NB/GLMM-P的AUC差异；环境因素在离散模型中显著（Table 3）。

#### 4. 基于阈值的方法不足以检测异常，需要模型化方法

- claim_cn：基于阈值的方法不足以检测异常，需要模型化方法

- evidence_cn：引言论证阈值法缺陷，模型方法在评价中优于逻辑回归等阈值敏感方法。

#### 5. 方法需要至少一个月目标患者数据

- claim_cn：方法需要至少一个月目标患者数据

- evidence_cn：k=4时AUC达到0.81，接近k=12和almost all的水平，而k=1时表现差。

- internal_validity_strategy_cn：通过构造TP场景（替换为其他患者数据）确保检测方法应报警，TN场景确保不报警，控制数据量k，重复100次模拟以减少随机性；使用AUC阈值无关的指标避免阈值选择偏差。

- external_validity_strategy_cn：使用真实世界SAM数据，来自696名患者中的326名，跨2014–2017三年；讨论指出地理单一局限并通过未来多地区验证计划承认外部有效性限制。

- what_is_not_actually_tested_cn：没有在实时临床环境中测试警报对患者和医生的实际影响；没有评估真实患者接受度和合规性；没有测试其他地理区域；没有检验阈值δ在实际操作中的表现。

## 贡献闭环

- technical_claim_cn：GLMM-GQP在AUC、误报/漏报均衡和时间到警报等指标上优于现有benchmark，能够检测出偏离个人模式的异常吸入器使用。

- artifact_claim_cn：模型各组件（CAR结构、离散模型、网格化）对性能有贡献，通过消融和对比验证。

- mechanism_claim_cn：环境因素通过改变吸入器使用的变异性而非均值影响行为；日常例程通过同小时窗口跨天相关性影响使用模式。

- boundary_claim_cn：当拥有至少一个月目标患者数据时性能可接受；需要准确事件时间、相关协变量、足够数据和患者行为知识；警报实施需考虑疲劳、法律和成本问题。

- reusable_design_knowledge_cn：对新型HIS数据，应先可视化事件模式，再针对数据特征（变异性、相关性）定制统计模型，并通过消融验证组件；提出了适用于其他健康事件场景的四项要求。

- theoretical_contribution_cn：将DGLM和CAR扩展到GLMM框架，为高分辨率健康数据事件建模提供新方法；在IS设计科学中作为exaptation案例，展示如何整合和改进已有设计知识。

- how_discussion_closes_intro_gap_cn：引言指出现有方法无法同时处理异质性、变异性和相关性，讨论部分明确说明GLMM-GQP通过三个特性解决这些问题，并通过benchmark证明其有效性，从而闭合缺口。

- overclaim_or_unsupported_leaps_cn：作者将离线benchmark结果外推到临床效益改善，但未进行现场干预验证；声称“smart asthma management”但未实际测试警报系统对患者行为的影响；环境因素对变异性的机制讨论缺少直接因果证据，仅为回归关联。

## 句级写作动作图谱

### 1. P1 S1

- order：1

- section：Abstract

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：哮喘是一种影响全球大量人口的常见呼吸系统慢性病。

- rhetorical_function_cn：建立研究背景，将读者带入健康领域。

- depends_on_cn：无

- sets_up_cn：引出疾病重要性，为后续经济负担做铺垫。

- evidence_pointer：Abstract

### 2. P1 S2

- order：2

- section：Abstract

- locator：P1 S2

- move_code：PRACTICAL_STAKES

- paraphrase_cn：控制不佳会显著降低患者生活质量。

- rhetorical_function_cn：说明疾病的实际后果，强化研究必要性。

- depends_on_cn：依赖于哮喘的普遍性。

- sets_up_cn：引出自我管理的重要性。

- evidence_pointer：Abstract

### 3. P1 S3

- order：3

- section：Abstract

- locator：P1 S3

- move_code：PHENOMENON

- paraphrase_cn：为改进自我管理，专家和工程师开发了智能哮喘管理系统SAM。

- rhetorical_function_cn：引入新的信息系统现象，作为研究对象。

- depends_on_cn：基于哮喘管理的现实需求。

- sets_up_cn：为高分辨率数据出现做铺垫。

- evidence_pointer：Abstract

### 4. P1 S4

- order：4

- section：Abstract

- locator：P1 S4

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：SAM提供蓝牙吸入器并记录每次使用的时间戳，这种高频日志是传统临床试验无法获得的。

- rhetorical_function_cn：突出数据新颖性，为方法缺口做铺垫。

- depends_on_cn：引入SAM系统后解释其特征。

- sets_up_cn：对比传统数据低频，引出新分析需求。

- evidence_pointer：Abstract

### 5. P1 S5

- order：5

- section：Abstract

- locator：P1 S5

- move_code：LIMITATION

- paraphrase_cn：临床数据获取是周期性的，导致定量研究只能关注使用次数的上升趋势。

- rhetorical_function_cn：指出现有研究数据分辨率限制。

- depends_on_cn：承接传统临床数据特点。

- sets_up_cn：引出SAM数据带来的新可能性。

- evidence_pointer：Abstract

### 6. P1 S6

- order：6

- section：Abstract

- locator：P1 S6

- move_code：GAP

- paraphrase_cn：利用SAM监测能力，我们开发了检测异常吸入器使用的数据分析框架。

- rhetorical_function_cn：直接提出本文解决的新任务。

- depends_on_cn：基于SAM数据特征和传统方法不足。

- sets_up_cn：预告方法核心，并引出模型特点。

- evidence_pointer：Abstract

### 7. P1 S7

- order：7

- section：Abstract

- locator：P1 S7

- move_code：DESIGN_FEATURE

- paraphrase_cn：新统计模型能够处理SAM数据的关键特征，如环境因素的异质性影响和重复日常例程引起的相关结构。

- rhetorical_function_cn：概括模型针对的两个核心设计需求。

- depends_on_cn：基于对数据特征的识别。

- sets_up_cn：为后续结果和贡献做铺垫。

- evidence_pointer：Abstract

### 8. P1 S8

- order：8

- section：Abstract

- locator：P1 S8

- move_code：RESULT

- paraphrase_cn：通过与多种基准方法的严格比较，展示了框架的满意性能。

- rhetorical_function_cn：给出核心结果，强调严格比较。

- depends_on_cn：依赖前述模型设计。

- sets_up_cn：引向贡献陈述。

- evidence_pointer：Abstract

### 9. P1 S9

- order：9

- section：Abstract

- locator：P1 S9

- move_code：CONTRIBUTION

- paraphrase_cn：讨论对IS知识库的贡献和对数据驱动哮喘管理的实践意义。

- rhetorical_function_cn：定位贡献层次，超越技术性能。

- depends_on_cn：基于结果。

- sets_up_cn：为读者预览全文结尾。

- evidence_pointer：Abstract

### 10. P1 S1

- order：10

- section：Introduction

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：哮喘是美国最常见的慢性病之一，约2460万人受影响。

- rhetorical_function_cn：提供统计数字建立疾病重要性。

- depends_on_cn：无

- sets_up_cn：引出后续经济负担和健康后果。

- evidence_pointer：Introduction P1 S1

### 11. P1 S2

- order：11

- section：Introduction

- locator：P1 S2

- move_code：PRACTICAL_STAKES

- paraphrase_cn：哮喘症状如咳嗽和喘息若不控制会降低生活质量。

- rhetorical_function_cn：把疾病数字转化为患者的痛苦体验。

- depends_on_cn：依赖哮喘普遍性。

- sets_up_cn：为自我管理的必要性做铺垫。

- evidence_pointer：Introduction P1 S2

### 12. P1 S3

- order：12

- section：Introduction

- locator：P1 S3

- move_code：PRACTICAL_STAKES

- paraphrase_cn：未控制哮喘带来巨额经济负担，美国成本约819亿美元。

- rhetorical_function_cn：增加经济维度的现实重要性。

- depends_on_cn：基于疾病普遍性和控制不足。

- sets_up_cn：强化研究价值。

- evidence_pointer：Introduction P1 S3

### 13. P1 S4

- order：13

- section：Introduction

- locator：P1 S4

- move_code：PHENOMENON

- paraphrase_cn：哮喘自我管理需要持续监测症状和药物使用。

- rhetorical_function_cn：引入关键词“自我管理”，作为分析场景。

- depends_on_cn：基于控制哮喘的需求。

- sets_up_cn：引出当前管理方法的局限性。

- evidence_pointer：Introduction P1 S4

### 14. P2 S1

- order：14

- section：Introduction

- locator：P2 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：当前实践依赖哮喘行动计划，以吸入器使用次数阈值来评估控制。

- rhetorical_function_cn：介绍标准实践。

- depends_on_cn：基于自我管理框架。

- sets_up_cn：批判阈值方法的局限。

- evidence_pointer：Introduction P2 S1

### 15. P2 S2

- order：15

- section：Introduction

- locator：P2 S2

- move_code：LIMITATION

- paraphrase_cn：阈值法不能直接反映症状，因为有些患者会预防止咳，且个体感知差异极大。

- rhetorical_function_cn：指出现有阈值方法的主要缺陷。

- depends_on_cn：基于阈值法描述。

- sets_up_cn：为引入更精细数据和方法做铺垫。

- evidence_pointer：Introduction P2 S2

### 16. P2 S3

- order：16

- section：Introduction

- locator：P2 S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：已有健康信息系统用于改善哮喘管理，但多数依赖患者自报数据。

- rhetorical_function_cn：介绍HIS的现状及缺陷。

- depends_on_cn：承接阈值法问题。

- sets_up_cn：引出SAM系统作为解决方案。

- evidence_pointer：Introduction P2 S3

### 17. P3 S1

- order：17

- section：Introduction

- locator：P3 S1

- move_code：PHENOMENON

- paraphrase_cn：SAM系统是一种新型HIS，利用蓝牙传感器记录每个吸入器使用日期和时间。

- rhetorical_function_cn：引入新型数据源。

- depends_on_cn：基于已有HIS的局限。

- sets_up_cn：强调高频数据优势。

- evidence_pointer：Introduction P3 S1

### 18. P3 S2

- order：18

- section：Introduction

- locator：P3 S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：SAM已被用于监测依从性和改善哮喘控制，并生成报告。

- rhetorical_function_cn：说明SAM系统的前期价值。

- depends_on_cn：SAM系统定位。

- sets_up_cn：指出已有应用集中在临床结果，缺少分析框架。

- evidence_pointer：Introduction P3 S2

### 19. P4 S1

- order：19

- section：Introduction

- locator：P4 S1

- move_code：LIMITATION

- paraphrase_cn：传统临床试验低频采集，无法揭示吸入器使用的详细模式。

- rhetorical_function_cn：再次强调传统数据短板。

- depends_on_cn：对比SAM高频数据。

- sets_up_cn：为研究目标提供背景。

- evidence_pointer：Introduction P4 S1

### 20. P4 S2

- order：20

- section：Introduction

- locator：P4 S2

- move_code：GAP

- paraphrase_cn：SAM的高频数据使我们能够建模个人使用模式，但缺乏专门针对该数据的分析方法。

- rhetorical_function_cn：明确提出方法缺口。

- depends_on_cn：区分于传统数据。

- sets_up_cn：引出研究目标。

- evidence_pointer：Introduction P4 S2

### 21. P5 S1

- order：21

- section：Introduction

- locator：P5 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：研究目标是提供可视化工具、制定针对SAM数据的统计模型、提供偏离正常模式的检测方法。

- rhetorical_function_cn：清晰列出三个具体目标。

- depends_on_cn：基于前述缺口。

- sets_up_cn：为后续模型开发提供框架。

- evidence_pointer：Introduction P5 S1

### 22. P5 S2

- order：22

- section：Introduction

- locator：P5 S2

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：传统趋势方法无法轻易发现单次异常使用，而异常可能由短期触发、突发恶化或运动诱发的症状引起。

- rhetorical_function_cn：解释为什么检测单次异常有意义。

- depends_on_cn：对比趋势方法。

- sets_up_cn：支持方法设计的目标。

- evidence_pointer：Introduction P5 S2

### 23. P6 S1

- order：23

- section：Introduction

- locator：P6 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：由于因变量是计数，可以考虑基于泊松或负二项的GLMM，或逻辑回归。

- rhetorical_function_cn：罗列可能适用的现有方法。

- depends_on_cn：基于目标识别。

- sets_up_cn：批判这些方法的局限。

- evidence_pointer：Introduction P6 S1

### 24. P6 S2

- order：24

- section：Introduction

- locator：P6 S2

- move_code：LIMITATION

- paraphrase_cn：GLMM对指定事件发生之间的相关结构灵活性有限。

- rhetorical_function_cn：指出GLMM的一个关键缺陷。

- depends_on_cn：基于SAM数据需要建模相关。

- sets_up_cn：为CAR结构引入做准备。

- evidence_pointer：Introduction P6 S2

### 25. P6 S3

- order：25

- section：Introduction

- locator：P6 S3

- move_code：LIMITATION

- paraphrase_cn：SVM个人级分类器忽略患者共享特征，且无法建模环境触发因素对变异性的影响。

- rhetorical_function_cn：指出SVM的不足。

- depends_on_cn：对比GLMM，加入分类器方法。

- sets_up_cn：强化新模型的必要性。

- evidence_pointer：Introduction P6 S3

### 26. P7 S1

- order：26

- section：Introduction

- locator：P7 S1

- move_code：GAP

- paraphrase_cn：需要一种模型，能同时处理患者随机效应、环境因子离散模型和结构化相关。

- rhetorical_function_cn：将多个局限整合为一个明确缺口。

- depends_on_cn：依赖前面所有LIMITATION。

- sets_up_cn：引出GLMM-GQP的提出。

- evidence_pointer：Introduction P7 S1

### 27. P7 S2

- order：27

- section：Introduction

- locator：P7 S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：提出GLMM-GQP，包含网格转换、患者和网格随机效应、离散子模型和CAR相关结构。

- rhetorical_function_cn：首次介绍新方法的组成。

- depends_on_cn：基于GAP。

- sets_up_cn：为后文模型开发做提纲。

- evidence_pointer：Introduction P7 S2

### 28. P7 S3

- order：28

- section：Introduction

- locator：P7 S3

- move_code：STUDY_OVERVIEW

- paraphrase_cn：论文其余部分安排为文献综述、模型开发、性能评价、结论。

- rhetorical_function_cn：预告结构，为读者导航。

- depends_on_cn：无。

- sets_up_cn：建立阅读预期。

- evidence_pointer：Introduction end

### 29. 统计模型 P1 S1

- order：29

- section：Literature Review

- locator：统计模型 P1 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：临床试验哮喘研究常用马尔可夫模型，利用临床分级量化转移概率。

- rhetorical_function_cn：概述现有统计模型。

- depends_on_cn：无。

- sets_up_cn：随后指出不适用于SAM数据。

- evidence_pointer：Literature Review, first paragraph

### 30. 统计模型 P1 S3

- order：30

- section：Literature Review

- locator：统计模型 P1 S3

- move_code：LIMITATION

- paraphrase_cn：马尔可夫模型需要临床定义的哮喘控制等级，而SAM只能远程获取数据，无法提供该输入。

- rhetorical_function_cn：排除马尔可夫模型。

- depends_on_cn：基于SAM数据来源。

- sets_up_cn：介绍CG-HMM后也会排除。

- evidence_pointer：Literature Review, statistical models paragraph 1

### 31. 统计模型 P1 S4

- order：31

- section：Literature Review

- locator：统计模型 P1 S4

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：CG-HMM被开发用于检测哮喘控制的持续逐渐恶化。

- rhetorical_function_cn：提及与本研究最接近的已有模型。

- depends_on_cn：基于处理无临床分级的替代方案。

- sets_up_cn：指出CG-HMM不适合检测突然异常。

- evidence_pointer：Literature Review, statistical models paragraph 1

### 32. 统计模型 P2 S1

- order：32

- section：Literature Review

- locator：统计模型 P2 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：GLM和GLMM是计数事件建模最自然的选择。

- rhetorical_function_cn：介绍本文的基础统计框架。

- depends_on_cn：无。

- sets_up_cn：说明GLMM-GQP是GLMM扩展。

- evidence_pointer：Literature Review, statistical models paragraph 2

### 33. 统计模型 P2 S3

- order：33

- section：Literature Review

- locator：统计模型 P2 S3

- move_code：LIMITATION

- paraphrase_cn：传统准泊松GLMM无法建模离散参数，也不具备特殊相关结构。

- rhetorical_function_cn：指出基础模型的缺陷。

- depends_on_cn：基于GLMM基础。

- sets_up_cn：为DGLM和CAR的引入做铺垫。

- evidence_pointer：Literature Review, statistical models paragraph 2

### 34. 表1之后

- order：34

- section：Literature Review

- locator：表1之后

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：表1对比GLM、GLMM、DGLM和GLMM-GQP在固定效应、随机效应、离散模型和相关结构上的差异。

- rhetorical_function_cn：用表格汇总现有方法差异。

- depends_on_cn：基于文献总结。

- sets_up_cn：凸显GLMM-GQP综合能力。

- evidence_pointer：Table 1

### 35. IS Literature P1 S1

- order：35

- section：Literature Review

- locator：IS Literature P1 S1

- move_code：CONTEXT

- paraphrase_cn：IS社区在改善医疗实践方面可发挥重要作用。

- rhetorical_function_cn：将研究定位到IS领域。

- depends_on_cn：无。

- sets_up_cn：引出IS健康分析文献。

- evidence_pointer：IS Literature paragraph 1

### 36. IS Literature P1 S3

- order：36

- section：Literature Review

- locator：IS Literature P1 S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：IS学者已开展基于EHR的健康预测分析，如心力衰竭再入院和糖尿病风险建模。

- rhetorical_function_cn：展示IS健康分析先例。

- depends_on_cn：基于IS社区作用。

- sets_up_cn：将SAM研究归入同一研究流。

- evidence_pointer：IS Literature paragraph 1

### 37. IS Literature P2 S1

- order：37

- section：Literature Review

- locator：IS Literature P2 S1

- move_code：GAP

- paraphrase_cn：SAM系统是HIS定义扩展的例子，但需要新的分析方法来利用其数据。

- rhetorical_function_cn：指出SAM分析空白。

- depends_on_cn：基于已有健康分析文献。

- sets_up_cn：定位本文为exaptation。

- evidence_pointer：IS Literature paragraph 2

### 38. 开头 P1

- order：38

- section：Model Development

- locator：开头 P1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：分析框架分三步：数据转换、GLMM-GQP拟合、异常检测算法。

- rhetorical_function_cn：概述整个框架结构。

- depends_on_cn：基于研究目标。

- sets_up_cn：为后续小节提供提纲。

- evidence_pointer：Model Development, Figure 1

### 39. 数据收集 测试平台

- order：39

- section：Model Development

- locator：数据收集 测试平台

- move_code：CONTEXT

- paraphrase_cn：Propeller Health实现并管理SAM平台，其蓝牙传感器获得FDA 510(k)认证。

- rhetorical_function_cn：提供测试平台可信度。

- depends_on_cn：无。

- sets_up_cn：说明数据来源真实可靠。

- evidence_pointer：Data Collection, Description of Test Bed

### 40. 数据描述

- order：40

- section：Model Development

- locator：数据描述

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：数据包含人口统计、ACT评分和五项环境因素，均来自真实系统。

- rhetorical_function_cn：描述数据集变量。

- depends_on_cn：基于测试平台。

- sets_up_cn：为模型变量选择提供依据。

- evidence_pointer：Data Description, Table 2

### 41. 数据描述 数据不平衡

- order：41

- section：Model Development

- locator：数据描述 数据不平衡

- move_code：LIMITATION

- paraphrase_cn：数据集存在性别、种族和初始控制水平不平衡，但符合哮喘流行病学特征。

- rhetorical_function_cn：承认数据局限性，防止过度泛化。

- depends_on_cn：基于数据统计。

- sets_up_cn：讨论时说明外部有效性边界。

- evidence_pointer：Data Description final paragraph

### 42. Step 1 数据转换

- order：42

- section：Model Development

- locator：Step 1 数据转换

- move_code：DESIGN_FEATURE

- paraphrase_cn：将纵向数据按小时转换为24×7网格，并合并每个患者的多周数据。

- rhetorical_function_cn：描述核心数据变换。

- depends_on_cn：基于SAM数据时间戳。

- sets_up_cn：为可视化相关结构做铺垫。

- evidence_pointer：Step 1: Data Transformation

### 43. Step 1 图3后

- order：43

- section：Model Development

- locator：Step 1 图3后

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：网格化能揭示日常例程引起的相关结构，而在原始时间序列格式中难以处理。

- rhetorical_function_cn：解释为什么需要变换。

- depends_on_cn：基于SAM数据特性。

- sets_up_cn：为CAR模型提供数据基础。

- evidence_pointer：Step 1, Figure 3

### 44. Step 2 模型描述

- order：44

- section：Model Development

- locator：Step 2 模型描述

- move_code：THEORY_PROPOSITION

- paraphrase_cn：假设吸入器使用次数遵循准泊松分布，均值为λ，方差为θλ。

- rhetorical_function_cn：设定模型的基本统计假设。

- depends_on_cn：基于计数数据特性。

- sets_up_cn：引出均值和离散两个方程。

- evidence_pointer：Step 2, Model Description

### 45. Step 2 均值模型方程(1)后

- order：45

- section：Model Development

- locator：Step 2 均值模型方程(1)后

- move_code：DESIGN_FEATURE

- paraphrase_cn：均值模型包含人口变量、ACT、周末指示作为固定效应，并包含患者随机效应和网格随机效应。

- rhetorical_function_cn：描述均值模型完整结构。

- depends_on_cn：基于准泊松假设。

- sets_up_cn：为推断结果做铺垫。

- evidence_pointer：Equation (1)

### 46. Step 2 网格随机效应

- order：46

- section：Model Development

- locator：Step 2 网格随机效应

- move_code：DESIGN_FEATURE

- paraphrase_cn：网格随机效应采用CAR模型，通过矩阵D定义同一小时窗口跨天网格的当前相关。

- rhetorical_function_cn：介绍CAR结构作为关键创新。

- depends_on_cn：基于网格化数据。

- sets_up_cn：论证该结构符合哮喘文献和实际数据。

- evidence_pointer：Step 2, grid-level random effects paragraph

### 47. Step 2 网格相关验证

- order：47

- section：Model Development

- locator：Step 2 网格相关验证

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：该相关假设得到哮喘文献支持，并在SAM数据中观察到同一小时窗口多次使用聚集。

- rhetorical_function_cn：为CAR结构提供外部和内部证据。

- depends_on_cn：依赖CAR定义。

- sets_up_cn：增强模型可信度。

- evidence_pointer：Figure 5

### 48. Step 2 离散模型方程(2)后

- order：48

- section：Model Development

- locator：Step 2 离散模型方程(2)后

- move_code：DESIGN_FEATURE

- paraphrase_cn：离散模型将温度、湿度、PM2.5、能见度和风速作为预测变量，建模log(θ)。

- rhetorical_function_cn：描述离散模型具体内容。

- depends_on_cn：基于环境因素影响变异性的文献。

- sets_up_cn：为推断结果铺垫。

- evidence_pointer：Equation (2)

### 49. Step 2 离散模型理由

- order：49

- section：Model Development

- locator：Step 2 离散模型理由

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：文献表明环境因素主要影响变异而非均值，因此将这些因素放入离散模型。

- rhetorical_function_cn：解释为什么环境因素在离散模型而非均值模型。

- depends_on_cn：基于引用文献。

- sets_up_cn：为参数结果提供预期。

- evidence_pointer：Step 2, dispersion model paragraph

### 50. Step 2 准泊松选择

- order：50

- section：Model Development

- locator：Step 2 准泊松选择

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：选择准泊松而不是负二项，因为准泊松的均值和离散参数具有线性关系，方便DGLM式离散建模。

- rhetorical_function_cn：解释分布选择的方法学原因。

- depends_on_cn：基于DGLM文献。

- sets_up_cn：为检测概率计算做铺垫。

- evidence_pointer：Step 2, quasi-Poisson choice paragraph

### 51. Step 2 推断结果

- order：51

- section：Model Development

- locator：Step 2 推断结果

- move_code：RESULT

- paraphrase_cn：推断显示性别和ACT显著影响均值；温度负相关、湿度、PM2.5和风速正相关于离散；患者随机效应方差较大。

- rhetorical_function_cn：报告模型参数结果。

- depends_on_cn：依赖模型设计。

- sets_up_cn：为后续检测提供估计值。

- evidence_pointer：Table 3

### 52. Step 3 开头

- order：52

- section：Model Development

- locator：Step 3 开头

- move_code：DESIGN_FEATURE

- paraphrase_cn：检测基于个性化概率网格，即每位患者每个网格的吸入器使用概率。

- rhetorical_function_cn：引入异常检测的核心设计。

- depends_on_cn：依赖模型参数估计。

- sets_up_cn：说明如何判断异常。

- evidence_pointer：Step 3

### 53. Step 3 阈值

- order：53

- section：Model Development

- locator：Step 3 阈值

- move_code：REQUIREMENT

- paraphrase_cn：阈值δ由护理提供者指定，用于区分in-pattern和out-of-pattern网格。

- rhetorical_function_cn：将决策权交还给临床医生。

- depends_on_cn：基于概率网格。

- sets_up_cn：在评价中使用AUC以绕过阈值依赖。

- evidence_pointer：Step 3, threshold paragraph

### 54. 开场

- order：54

- section：Performance Evaluation

- locator：开场

- move_code：STUDY_OVERVIEW

- paraphrase_cn：我们进行系列性能评价，考虑GLMM、逻辑回归、SVM和CG-HMM等基准。

- rhetorical_function_cn：预告评价设计。

- depends_on_cn：基于方法开发。

- sets_up_cn：为评价细节做铺垫。

- evidence_pointer：Performance Evaluation, opening

### 55. 设计 两个场景

- order：55

- section：Performance Evaluation

- locator：设计 两个场景

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：构造两种场景：将待测患者一周数据替换为其他人的数据作为真阳性，不替换作为真阴性。

- rhetorical_function_cn：建立评价的ground truth。

- depends_on_cn：基于检测目标。

- sets_up_cn：为AUC计算定义TP/TN。

- evidence_pointer：Design of Evaluation Algorithm

### 56. AUC选择

- order：56

- section：Performance Evaluation

- locator：AUC选择

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：采用AUC作为主要指标，因为检测性能依赖阈值，AUC可综合衡量不同阈值下表现。

- rhetorical_function_cn：解释为何用AUC。

- depends_on_cn：基于阈值依赖问题。

- sets_up_cn：为结果表格铺垫。

- evidence_pointer：Performance Measure paragraph

### 57. Benchmark 方法清单

- order：57

- section：Performance Evaluation

- locator：Benchmark 方法清单

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：基准包括GLMM-P、GLMM-NB、无CAR的GLMM-GQPS、逻辑回归、SVM和CG-HMM，共计六种。

- rhetorical_function_cn：列出所有对比方法。

- depends_on_cn：基于现有方法分类。

- sets_up_cn：为结果解释提供了消融逻辑。

- evidence_pointer：Benchmark Methods

### 58. 结果 表4

- order：58

- section：Performance Evaluation

- locator：结果 表4

- move_code：RESULT

- paraphrase_cn：GLMM-GQP在k≥4时AUC最高，且随数据量增加而提升；GLMM-GQPS次之。

- rhetorical_function_cn：报告核心结果。

- depends_on_cn：依赖评价算法。

- sets_up_cn：为后续组件贡献分析铺垫。

- evidence_pointer：Table 4

### 59. 结果 k=1 讨论

- order：59

- section：Performance Evaluation

- locator：结果 k=1 讨论

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：在只有一周数据时，所有方法表现都差，GLMM-GQP因为模型复杂而略逊于简单方法；但这是新患者的普遍问题。

- rhetorical_function_cn：承认边界条件，防止过度声称。

- depends_on_cn：基于表4结果。

- sets_up_cn：引出数据量要求。

- evidence_pointer：Performance Evaluation Results, k=1 paragraph

### 60. 结果 GLMM-GQPS对比

- order：60

- section：Performance Evaluation

- locator：结果 GLMM-GQPS对比

- move_code：RESULT

- paraphrase_cn：GLMM-GQP优于GLMM-GQPS，说明考虑到特殊相关结构能提升性能。

- rhetorical_function_cn：用消融结果证明CAR价值。

- depends_on_cn：基于Table 4。

- sets_up_cn：为理论贡献提供证据。

- evidence_pointer：Performance Evaluation Results, GLMM family paragraph

### 61. 结果 逻辑回归SVM

- order：61

- section：Performance Evaluation

- locator：结果 逻辑回归SVM

- move_code：RESULT

- paraphrase_cn：逻辑回归和SVM误报率高，因为它们对少数吸入器事件过度敏感。

- rhetorical_function_cn：解释非网格化方法为何不好。

- depends_on_cn：基于Figure 9。

- sets_up_cn：强调网格化和模型化优势。

- evidence_pointer：Figure 9

### 62. 结果 CG-HMM

- order：62

- section：Performance Evaluation

- locator：结果 CG-HMM

- move_code：RESULT

- paraphrase_cn：CG-HMM表现最差，因为其设计用于检测逐日趋势，无法捕捉未改变日均计数的异常模式。

- rhetorical_function_cn：排除现有哮喘专用模型。

- depends_on_cn：基于CG-HMM算法。

- sets_up_cn：说明本研究任务与趋势检测不同。

- evidence_pointer：Performance Evaluation Results, CG-HMM paragraph

### 63. 贡献总结 第一点

- order：63

- section：Discussion and Conclusion

- locator：贡献总结 第一点

- move_code：CONTRIBUTION

- paraphrase_cn：首次为哮喘管理提出补充指南式自我管理的新方法，利用SAM分析从被动的护理转向数据驱动的患者中心管理。

- rhetorical_function_cn：声明对哮喘管理的贡献。

- depends_on_cn：依赖前面所有论证。

- sets_up_cn：随后列第二、第三贡献。

- evidence_pointer：Summary of Contribution

### 64. 贡献总结 第二点

- order：64

- section：Discussion and Conclusion

- locator：贡献总结 第二点

- move_code：CONTRIBUTION

- paraphrase_cn：方法角度，GLMM-GQP集成多个统计模型，提供离散子模型和灵活相关结构，并经基准验证。

- rhetorical_function_cn：声明方法论贡献。

- depends_on_cn：依赖模型结果。

- sets_up_cn：为第三点IS贡献铺垫。

- evidence_pointer：Summary of Contribution

### 65. 贡献总结 第三点

- order：65

- section：Discussion and Conclusion

- locator：贡献总结 第三点

- move_code：CONTRIBUTION

- paraphrase_cn：将SAM平台作为扩展的HIS，强调开发契合新型HIS的IT制品，并提供exaptation设计科学研究实例。

- rhetorical_function_cn：声明对IS知识库的贡献。

- depends_on_cn：基于IS文献定位。

- sets_up_cn：引出实践意义。

- evidence_pointer：Summary of Contribution

### 66. 实践意义 照护提供者

- order：66

- section：Discussion and Conclusion

- locator：实践意义 照护提供者

- move_code：PRACTICAL_STAKES

- paraphrase_cn：对护理提供者，自动检测可优化资源利用，减少人工监测的昂贵时间投入。

- rhetorical_function_cn：强调对临床实践的直接益处。

- depends_on_cn：基于制品功能。

- sets_up_cn：导致面向患者的意义。

- evidence_pointer：Practical Implications

### 67. 实践意义 患者

- order：67

- section：Discussion and Conclusion

- locator：实践意义 患者

- move_code：PRACTICAL_STAKES

- paraphrase_cn：对哮喘患者，工具可作为自我管理辅助，HIS与分析结合才能发挥质量改善潜力。

- rhetorical_function_cn：说明患者层面的价值。

- depends_on_cn：基于信息系统和分析结合论点。

- sets_up_cn：导向指南部分。

- evidence_pointer：Practical Implications

### 68. 指南 四项条件

- order：68

- section：Discussion and Conclusion

- locator：指南 四项条件

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：方法适用于满足四项条件的任何健康事件检测：准确事件时间、相关协变量、充足目标患者数据、患者行为知识。

- rhetorical_function_cn：限定方法的适用边界。

- depends_on_cn：基于本研究经验。

- sets_up_cn：为未来扩展提供方向。

- evidence_pointer：Guidelines for IS Researchers and Practitioners

### 69. 实施注意

- order：69

- section：Discussion and Conclusion

- locator：实施注意

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：实施时需考虑警报疲劳、法律风险、患者服从性和成本分担等问题。

- rhetorical_function_cn：承认实际部署的挑战。

- depends_on_cn：基于制品到临床的转化问题。

- sets_up_cn：引出局限与未来研究。

- evidence_pointer：Implementation caveats

### 70. 主要局限

- order：70

- section：Discussion and Conclusion

- locator：主要局限

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：数据源于单一地理区域，变量列表不完整，未与EHR整合；计划跨区域验证并扩展至COPD。

- rhetorical_function_cn：坦诚外部有效性局限。

- depends_on_cn：基于研究环境。

- sets_up_cn：为未来研究铺路。

- evidence_pointer：Limitations and Future Research

## 写作技术

- gap_construction_cn：通过对比传统临床试验数据低分辨率与SAM高分辨率，指出现有方法只能捕捉趋势不能检测单次异常，从而制造方法缺口；同时批判依赖自报数据的现有HIS，强化新系统的必要性。

- signposting_cn：摘要末尾预告贡献；引言末尾列出研究目标和论文结构；模型开发开头用图1预告三个步骤；评价前用图7预告流程；表1总结方法差异；每部分结尾设有小总结。

- transition_logic_cn：从方法局限到问题提出，从数据描述到数据转换（图3），从转换到模型设计（方程1/2），从模型到检测算法（图6），从检测到性能评价（图7），从结果到设计知识（讨论）。每个新部分都以简短的综述段落重新连接前文目标。

- claim_evidence_rhythm_cn：先提出设计特征，然后用参数估计（Table 3）支持模型合理性，然后用AUC对比（Table 4）展示整体性能，再用消融（GLMM-GQPS vs GLMM-GQP）和错误率细节（Figure 9）支持组件价值。主张逐步由弱到强，每个主张后紧接证据。

- benchmark_narrative_cn：benchmark不是简单列数字，而是按逻辑分组：GLMM家族（有无CAR、有无离散）、非网格化方法（逻辑回归、SVM）、已有哮喘专用模型（CG-HMM）。通过解释每个基准为何表现好或坏，将benchmark嵌入论证链中。

- theory_return_cn：结果回到统计文献中的DGLM和CAR，验证这些方法可以集成到GLMM并有效；回到IS设计科学的exaptation概念，说明整合已有设计知识可解决新问题。

- contribution_positioning_cn：强调贡献是专门针对新型HIS数据的方法，而非通用算法，呼吁IS学者研究新HIS带来的数据分析需求，避免被误解为纯统计学论文。

- novelty_protection_cn：通过消融实验证明每个设计组件都有贡献，通过阈值无关的AUC和多种错误指标避免单点性能，通过多k值测试说明方法的数据需求，从而防止贡献退化为一次性性能结果。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：建立现实问题背景和新技术数据源，说明传统数据分辨率不足。

- research_job_cn：识别新型HIS数据带来的新分析可能性。

- required_evidence_cn：疾病流行数据、传统方法局限的文献、新系统技术描述。

- transition_to_next_cn：引入新数据源后指出现有方法不能充分利用，将缺口具体化。

#### 2. 2

- step：2

- writing_job_cn：系统评述可能适用的统计模型和IS文献，指出每个现有方法的适用边界。

- research_job_cn：将数据特征（相关性、变异性）映射到具体方法缺陷。

- required_evidence_cn：相关统计模型文献、IS健康分析先例。

- transition_to_next_cn：从多个局限综合出一个新方法的需求。

#### 3. 3

- step：3

- writing_job_cn：描述新制品的完整设计，包括数据变换、模型方程和算法步骤。

- research_job_cn：集成多种技术构建分析框架，并说明每个设计选择的理由。

- required_evidence_cn：数据说明、模型公式、图表可视化。

- transition_to_next_cn：说明模型输出如何用于检测异常。

#### 4. 4

- step：4

- writing_job_cn：设计严谨的离线评价，构造正反场景，选择合理指标，列出适当的benchmark。

- research_job_cn：实现评价流程并计算性能指标。

- required_evidence_cn：TP/TN定义、AUC和其他指标、多数据量条件。

- transition_to_next_cn：从性能结果提取组件贡献和边界。

#### 5. 5

- step：5

- writing_job_cn：在讨论中回到引言缺口，声明贡献，提炼适用条件和设计原则。

- research_job_cn：将局部结果一般化，识别方法和领域局限性。

- required_evidence_cn：性能结果、文献定位、明确的适用条件。

- transition_to_next_cn：文章收束，提出未来研究方向。

### most_transferable_moves_cn

1. 使用表格对比方法特征差异

2. 用消融模型验证每个组件的贡献

3. 使用多个数据量k测试数据敏感性

4. 用AUC等阈值无关指标避免主观阈值

5. 通过构造替换场景生成真阳性和真阴性

6. 将方法适用条件分解为可检查的四个方面

### resource_intensive_or_nonstandard_parts_cn

1. 需要与真实SAM平台合作获得蓝牙吸入器传感器数据和环境数据

2. 需要跨多年、多区域的患者级数据

3. 需要临床知识来设定相关结构和确定环境变量

4. 评价算法中的替换场景模拟需要计算资源

### what_not_to_copy_superficially_cn

1. 不要只提出新模型名称而不做消融验证

2. 不要在没有真实患者数据时声称临床改善

3. 不要忽略事件时间戳和协变量的准确性

4. 不要将AUChigh直接等同于临床价值，需讨论实际部署壁垒

- single_best_description_of_the_routine_cn：针对新数据源的特征，构建一个集成现有统计技术的分析制品，通过消融和benchmark证明每个组件必要，再提炼为可复用的设计知识。

## 分析边界

基于提供的完整全文进行解剖，可能受OCR影响公式呈现略有歧义，但结构和文字清晰；未接触附录或补充材料；外部有效性讨论仅基于作者自述。
