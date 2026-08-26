# Stratifying no-show patients into multiple risk groups via a holistic data analytics-based framework

- 作者：Serhat Simsek; Thomas Tiahrt; Ali Dag
- 年份 / 期刊：2020 / Decision Support Systems
- DOI：10.1016/j.dss.2020.113269
- 源文件：04588_2020_stratifying-no-show-patients-into-multiple-risk-groups-via-a-holistic-data-analytics-based-frame.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：requirements_build_evaluate_design_principles
- 置信度：0.85

## 文章级论证概况

- 核心问题：在基层门诊患者失约预测中，如何构建一个兼顾预测准确性、变量精简、处理类别不平衡并能给出患者个体化风险等级的混合数据挖掘框架？

- 制品与设计：一个四阶段混合数据挖掘框架：数据清洗与特征工程、以遗传算法和模拟退火为主的变量选择、随机欠采样/随机过采样/SMOTE类平衡、LR/RF/ANN/集成分类器比较；最终选择ANN+RUS+GA∩SA变量集构建预测模型，并用敏感性分析、信息融合、概率阈值敏感性分析和k-means聚类将患者分为五个失约风险等级，同时开发基于Web的决策支持工具。

- 客观结果：最佳模型在10折交叉验证中，ANN+RUS+GA∩SA获得最高敏感性0.792，AUC约0.838；ANN/EL+GA+RUS获得最高AUC 0.844；不进行类平衡时敏感性仅0.365–0.426。概率阈值分析显示丢弃低置信区间样本可将AUC提升至0.950、准确率0.942、敏感性0.890、特异性0.948。变量重要性中，既往失约占比28.08%、糖尿病12.03%、预约提醒11.95%、酗酒11.23%、提前期10.64%、经济援助9.48%。

- 核心贡献：作者声称贡献不在于应用已知分类模型，而在于：a）采用计算高效且不易受共线性、过拟合和局部最优影响的元启发式变量选择；b）首次在失约预测文献中系统使用数据平衡技术增强少数类检测；c）通过k-means给出五级患者失约风险；d）开发可被诊所采用的Web决策支持工具。

- 整篇论证链：文章先指出患者失约给医疗机构和患者带来成本与健康后果，并强调高质量预测模型是预约调度处方模型的前提。随后通过文献综述指出已有失约预测研究在变量选择上多采用逐步、弹性网等易受共线性/过拟合/局部最优影响的方法，且几乎没有使用类平衡技术，也没有提供个体化风险分级与可用工具。为填补这一缺口，作者在巴西Kaggle公开数据集上构建一个包含特征工程、GA/SA变量选择、RUS/ROS/SMOTE类平衡、LR/RF/ANN/EL分类器比较的完整数据挖掘流程。通过10折交叉验证和精确率/敏感性/特异性/AUC指标，证明ANN+RUS+GA∩SA在少数类检测上表现最佳，同时类平衡和精简变量能显著提升敏感性。随后通过Saltelli敏感性分析和信息融合解释黑箱变量重要性，用概率阈值敏感性分析说明低置信区间交由人工判断的合理性，并在概率之上用k-means将患者分成五个风险等级。最后部署Web工具作为实践性产出。讨论与结论部分将局部性能提升上升为可复用的方法论贡献，并承认公开数据、缺失变量和缺乏真实临床部署等限制。

## 类型与写作弧线判定

- 论文主类型判定：论文以构建一个混合数据挖掘框架和Web决策支持工具为核心，先给出四阶段方法论设计，再通过公开数据集上的性能评价和风险分层验证框架的可用性，最后提炼为设计知识和实践工具。虽然核心证据是计算实验，但整体叙述模式是“需求—构建—评价—设计知识”，而非单纯算法benchmark。

- 主导写作弧线判定：文章从失约预测的实践需求出发，逐项提出变量精简、类平衡、少数类检测、风险分层等要求，然后构建四阶段数据挖掘流程，并通过分类性能表、阈值分析、变量重要性等评价环节验证这些要求，最后以Web工具和结论中的方法论贡献收束。更接近要求—构建—评价—设计知识弧线，而非理论驱动或现场干预。

## 研究开展程序

- study_or_phase_count：8

- 研究阶段总序列：八个阶段按数据流与论证任务串接：前四个阶段完成从原始数据到最优预测模型的构建和选择；第五、六阶段对黑箱模型进行解释与概率可靠性验证；第七、八阶段将概率转化为可操作的风险类别和决策支持工具。后一阶段总是回答前一阶段留下的不确定性，例如变量选择结果进入分类比较，分类结果决定敏感性分析对象，敏感性分析结果支撑风险分层。

### studies_or_phases

#### 1. 数据获取与准备

- order：1

- name_cn：数据获取与准备

- question_cn：如何从公开原始数据得到适合预测建模的干净特征集？

- inputs_and_setting_cn：巴西Espírito Santo州的医疗预约Kaggle数据集，原始110,528条记录、14个变量。

- designed_or_compared_object_cn：清洗和特征工程后的数据集，导出提前期、预约星期/月份/呼叫时间、既往失约比例、两次预约间隔等变量，删除ID和异常值。

- baseline_control_or_counterfactual_cn：原始变量集和原始记录数；最终得到72,602条记录、17个变量。

##### objective_metrics

1. 记录数

2. 变量数

- analysis_method_cn：描述性数据处理、异常值裁剪、日期变量分解、患者历史聚合。

- main_result_cn：得到72,602条有效记录和17个预测变量，其中16个独立变量。

- argumentative_role_cn：为后续变量选择和建模提供数据基础，同时塑造“从公开数据也能构建实用框架”的定位。

- remaining_uncertainty_cn：哪些变量真正重要、如何选择精简变量集尚不清楚。

- link_to_next_phase_cn：将16个独立变量交给GA/SA进行变量选择。

##### evidence_pointers

1. Section 3.1

2. Table 2

#### 2. 变量选择：GA与SA

- order：2

- name_cn：变量选择：GA与SA

- question_cn：在避免穷举搜索的前提下，如何得到准确且精简的预测变量子集？

- inputs_and_setting_cn：上阶段产生的16个独立变量；GA和SA以随机森林为适应度函数。

- designed_or_compared_object_cn：SA选出的变量集、GA选出的变量集、两者交集和并集。

- baseline_control_or_counterfactual_cn：穷举搜索（2^16种组合）不可行；现有文献中的逐步、弹性网、似然比方法被作为潜在对比。

##### objective_metrics

1. RF交叉验证适应度

2. 后续分类性能

3. 变量子集大小

- analysis_method_cn：元启发式包装式变量选择：SA带重置策略和10次随机初始解；GA采用种群100、250代、交叉0.8、变异0.1、精英3。

- main_result_cn：SA选出9个变量，GA选出10个变量，交集为8个变量；交集在初步分析中优于并集。

- argumentative_role_cn：证明元启发式变量选择能提供精简变量集，为后文的parsimonious模型奠定基础。

- remaining_uncertainty_cn：哪个变量子集与哪种平衡方法和分类器组合效果最好尚未检验。

- link_to_next_phase_cn：将GA、SA、交集变量集与平衡技术和分类器一起纳入分类实验。

##### evidence_pointers

1. Section 3.2

2. Section 4.1

3. Table 4

#### 3. 数据平衡策略比较

- order：3

- name_cn：数据平衡策略比较

- question_cn：在约20%失约率的类别不平衡下，哪种重采样方法能改善少数类检测？

- inputs_and_setting_cn：10折交叉验证的训练折；约15,196名失约患者、57,406名履约患者。

- designed_or_compared_object_cn：随机欠采样RUS、随机过采样ROS、SMOTE与不进行平衡。

- baseline_control_or_counterfactual_cn：不使用任何类平衡方法；所有平衡只应用于训练集。

##### objective_metrics

1. AUC

2. Accuracy

3. Sensitivity

4. Specificity

- analysis_method_cn：在相同分类器和变量集下比较四种平衡条件，使用10折交叉验证。

- main_result_cn：平衡显著提升敏感性；不进行平衡时敏感性仅0.365–0.426，采用平衡后可超过0.7；RUS与ANN/交集组合达到最高敏感性0.792。

- argumentative_role_cn：直接回应文献缺口：失约预测研究中几乎没有系统使用类平衡技术。

- remaining_uncertainty_cn：什么分类器与什么变量/平衡组合总体上最好未定。

- link_to_next_phase_cn：通过四模型网格实验选择最佳分类器组合。

##### evidence_pointers

1. Section 3.3

2. Section 4.2

3. Table 6

#### 4. 预测模型构建与选择

- order：4

- name_cn：预测模型构建与选择

- question_cn：在变量集、平衡方法和分类算法组成的网格中，哪种组合最适合失约预测？

- inputs_and_setting_cn：GA、SA、GA∩SA三种变量集；SMOTE、ROS、RUS三种平衡；LR、RF、ANN、EL四种分类器；10折交叉验证。

- designed_or_compared_object_cn：36种左右的模型组合（变量集×平衡×分类器）以及全变量/无平衡的对照模型。

- baseline_control_or_counterfactual_cn：全变量且不进行类平衡的LR/RF/ANN/EL；全变量但用RUS的模型；GA∩SA但不平衡的模型。

##### objective_metrics

1. AUC

2. Accuracy

3. Sensitivity

4. Specificity

- analysis_method_cn：10折交叉验证；按均值与标准差比较；最终以敏感性为首要指标选择模型。

- main_result_cn：最高AUC 0.844出现在ANN/EL+GA+RUS；最高准确率0.786和特异性0.814在EL+GA+SMOTE；最高敏感性0.792在ANN+GA∩SA+RUS；最终选择ANN+RUS+交集变量作为理想模型。

- argumentative_role_cn：确定最终预测模型，同时用Table 5和Table 6证明类平衡和变量选择对少数类检测的增量贡献。

- remaining_uncertainty_cn：黑箱ANN无法直接解释变量作用；概率是否可靠未知。

- link_to_next_phase_cn：对选定的ANN模型进行敏感性分析和信息融合以解释变量重要性。

##### evidence_pointers

1. Section 3.4

2. Section 3.5

3. Table 5

4. Table 6

#### 5. 敏感性分析与信息融合

- order：5

- name_cn：敏感性分析与信息融合

- question_cn：在ANN这类黑箱模型中，哪些预测变量对失约结果最重要？

- inputs_and_setting_cn：10次运行选定ANN模型得到的变量重要性报告。

- designed_or_compared_object_cn：各次运行的重要性报告按AUC加权融合。

- baseline_control_or_counterfactual_cn：单一模型的敏感性排名；文献中已知的失约预测因子。

##### objective_metrics

1. 标准化敏感性占比

- analysis_method_cn：Saltelli敏感性分析测算每个变量的贡献，再利用Dag等人的信息融合公式按模型AUC加权组合。

- main_result_cn：既往失约占比28.08%，糖尿病12.03%，预约提醒11.95%，酗酒11.23%，提前期10.64%，经济援助9.48%，两次预约间隔8.62%，预约日7.65%。

- argumentative_role_cn：把模型性能结果转成可解释的临床/管理洞见，并显示与文献一致，且新增“两次预约间隔”变量。

- remaining_uncertainty_cn：概率本身是否经过良好校准、低置信区间的处理策略是否有效。

- link_to_next_phase_cn：用阈值敏感性分析检验概率分数的可靠性。

##### evidence_pointers

1. Section 3.5

2. Section 3.6

3. Fig. 2

4. Section 4.2

#### 6. 概率阈值敏感性分析

- order：6

- name_cn：概率阈值敏感性分析

- question_cn：模型给出的个体化失约概率是否可靠，低置信区间是否应交给人工判断？

- inputs_and_setting_cn：选定ANN模型在第7折测试集上的预测概率（5,757名履约、1,470名失约）。

- designed_or_compared_object_cn：阈值0.5不丢弃样本，与丢弃[0.4,0.6]、[0.3,0.7]、[0.2,0.8]、[0.1,0.9]区间的样本进行比较。

- baseline_control_or_counterfactual_cn：传统0.5概率阈值且保留所有样本。

##### objective_metrics

1. TP/FP/FN/TN

2. AUC

3. Accuracy

4. Sensitivity

5. Specificity

- analysis_method_cn：阈值敏感性分析：逐步丢弃靠近0.5的低置信样本并重算性能。

- main_result_cn：丢弃低置信样本后性能持续上升，最终AUC达到0.950、准确率0.942、敏感性0.890、特异性0.948。

- argumentative_role_cn：证明概率分数可用于风险分层，并支持“人机协作处理低置信个案”的决策逻辑。

- remaining_uncertainty_cn：如何从连续概率生成有限、可操作的风险类别。

- link_to_next_phase_cn：用k-means把概率分数聚成五个风险等级。

##### evidence_pointers

1. Table 7

2. Section 4.2

3. Fig. 3

#### 7. k-means风险分层

- order：7

- name_cn：k-means风险分层

- question_cn：如何将个体概率分数转化为“极低、低、中、高、极高”五级失约风险？

- inputs_and_setting_cn：ANN模型对每位患者估计的0到1失约概率。

- designed_or_compared_object_cn：k-means聚类得到的五级风险组，对应概率谱上不同区间。

- baseline_control_or_counterfactual_cn：二元阈值分类；概率阈值敏感性分析中“低置信丢弃”思路。

##### objective_metrics

1. 风险组数

2. 风险组在概率谱上的位置

- analysis_method_cn：k-means聚类算法对患者概率进行分组，并根据阈值分析说明可逐步丢弃中间风险组来提升模型性能。

- main_result_cn：患者被分为极低风险、低风险、中风险、高风险、极高风险五类，可作为医疗决策者评估个体失约的辅助机制。

- argumentative_role_cn：把技术性概率输出转成管理可用的风险分级，直接回应引言中的“患者个体化风险水平”目标。

- remaining_uncertainty_cn：风险分级在真实诊所流程中的成本收益和临床可接受性未被验证。

- link_to_next_phase_cn：将最优模型和风险分级封装为Web工具。

##### evidence_pointers

1. Fig. 3

2. Section 4.2

3. Section 6

#### 8. Web决策支持工具构建

- order：8

- name_cn：Web决策支持工具构建

- question_cn：如何让诊所能够便捷使用上述风险预测和分层结果？

- inputs_and_setting_cn：选定的ANN模型、GA∩SA变量集、五级风险聚类、Shiny应用环境。

- designed_or_compared_object_cn：基于Web的失约风险决策支持工具。

- baseline_control_or_counterfactual_cn：无工具的人工判断流程。

##### objective_metrics

1. 可用性（论文中未做用户评价）

2. 是否能输出风险分数和风险类别

- analysis_method_cn：开发并展示一个Shiny Web应用，输入预约和患者信息后输出个体失约风险分数与风险类别。

- main_result_cn：提供一个可运行的工具链接，能够为每位患者生成风险分数和风险类别，帮助预约决策。

- argumentative_role_cn：作为实践性贡献，使方法论能够被诊所采纳，同时强化“精简模型便于临床及时反应”的论证。

- remaining_uncertainty_cn：工具没有接受现场测试、用户满意度或部署效果评估，实际效率提升未被测量。

- link_to_next_phase_cn：结论部分将工具与限制、未来方向衔接，提出未来可加入“推荐风险最小预约日期”等功能。

##### evidence_pointers

1. Section 5

2. Section 6

## 各部分修辞架构

### abstract_moves

1. CONTEXT：失约预测对调度系统效率重要

2. RQ_OR_OBJECTIVE：提出四目标混合数据挖掘方法

3. RESULT：ANN+GA/SA变量集+RUS效果最好

4. CONTRIBUTION：阈值敏感性证明概率可用，Web工具作为实践产出

### introduction_moves

1. CONTEXT/PRACTICAL_STAKES：失约带来成本与健康损失

2. PRIOR_KNOWLEDGE：已有缓解策略包括超量预约、激励、预付、罚款

3. WHY_GAP_MATTERS：高质量预测模型是高质量调度处方的前提

4. CONTEXT：计算能力与数据驱动模型带来新机会

5. RQ_OR_OBJECTIVE：提出五级风险分类的混合数据驱动方法

6. BOUNDARY_CONDITION：只做预测，不做调度处方

7. CONTRIBUTION/WHY_GAP_MATTERS：提供个体风险等级并识别关键失约因素

8. STUDY_OVERVIEW：报告剩余章节结构

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE：梳理1960年代以来的失约研究三流派

2. PRIOR_KNOWLEDGE：举例Liu、Samorani、Daggy、Topuz等预测型研究

3. LIMITATION：已有变量选择方法易受共线性、过拟合、局部最优影响

4. GAP：尚无研究在失约预测中综合使用GA/SA变量选择与类平衡

5. MECHANISM：类不平衡会导致分类器偏向多数类，降低少数类敏感性

6. METHOD_JUSTIFICATION：采样方法兼容任何机器学习算法且无需已知误分类成本

### artifact_design_moves

1. REQUIREMENT：需要精简、稳健、计算可行的变量选择

2. DESIGN_FEATURE：采用GA和SA，并使用RF作为适应度函数避免共线性/过拟合

3. DESIGN_FEATURE：GA参数设计为高交叉、较高变异和精英保留

4. DESIGN_FEATURE：比较RUS、ROS、SMOTE三种平衡方法

5. DESIGN_FEATURE：构建LR/RF/ANN/EL四分类器，EL取概率均值

6. DESIGN_FEATURE：ANN通过权重衰减正则化并交叉验证调参

7. DESIGN_FEATURE：用Saltelli敏感性分析解释黑箱

8. DESIGN_FEATURE：用AUC加权的信息融合整合变量重要性

9. DESIGN_FEATURE：用k-means风险分层和Web工具实现落地产出

### evaluation_moves

1. BENCHMARK_OR_CONTRAST：Table 5覆盖变量集×平衡×分类器网格

2. BENCHMARK_OR_CONTRAST：Table 6对比无平衡/全变量/精简变量+平衡

3. RESULT：ANN+RUS+交集变量敏感性最高

4. METHOD_JUSTIFICATION：以敏感性为主要指标因为检测失约者更重要

5. ROBUSTNESS_OR_BOUNDARY_TEST：阈值敏感性分析显示丢弃低置信样本性能上升

6. RESULT：变量重要性排序与文献一致，并新增两次预约间隔变量

### discussion_and_contribution_moves

1. CONTRIBUTION：贡献是变量选择、平衡、风险分层、工具而非分类模型本身

2. RESULT/CONTRIBUTION：阈值分析证明概率分数可被临床信任

3. BOUNDARY_CONDITION：模型对低置信个案应与专家经验结合

4. LIMITATION_AND_FUTURE：公开数据集缺少预约原因、紧急程度、严重度等特征

5. LIMITATION_AND_FUTURE：未来工具不只预测风险，还应建议最低风险预约日期

## 理论/知识到设计的翻译

### 知识/理论基础

1. 失约预测文献中对预测型方法的研究（Liu、Samorani、Daggy、Alaeddini、Lenzi、Huang、Topuz等）

2. 统计学习和机器学习的变量选择理论：filter与wrapper、共线性、过拟合、穷举搜索不可行

3. 元启发式优化知识：SA跳出局部最优、GA通过交叉变异搜索

4. 类不平衡学习文献：采样方法、代价敏感学习、核方法

5. 集成学习经验：概率平均可能优于多数投票，但集成不一定总优于单模型

6. 黑箱模型解释方法：Saltelli敏感性分析与信息融合

7. 医疗失约领域经验知识：既往失约、糖尿病、提醒、提前期、经济援助、酗酒等预测因子

- 理论—设计耦合：partial

- 耦合判定理由：变量选择、类平衡、分类器组合和解释方法的设计主要来自方法论文献和工程经验，而不是来自某种组织行为理论或医生决策理论；但既有失约预测研究和领域知识确实影响了变量构造、指标选择以及结果解释，因此属于部分耦合。

- 理论到设计翻译链：领域先验（既往失约、提醒、提前期等预测因子）→ 特征工程；方法论知识（包装式变量选择缺陷、穷举不可行、采样可处理不平衡）→ 使用GA/SA选择变量、RUS/ROS/SMOTE平衡；黑箱不可解释性 → 用Saltelli敏感性和信息融合提取变量重要性；概率低置信区间影响决策可信度 → 用阈值敏感性分析验证并在低置信时转交人工；管理需要有限风险类别 → 用k-means对概率聚类形成五级风险；实践需要易用工具 → 开发Web决策支持工具。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：现有失约预测文献常用的逐步、似然比、弹性网变量选择在共线性下表现差，且弹性网易过拟合；穷举搜索成本指数增长。

- mechanism_cn：需要能在高维搜索空间中近似全局最优并避免局部最优的变量选择机制。

- design_requirement_cn：变量选择必须计算可行、稳健、产生精简模型。

- artifact_choice_cn：采用GA和SA作为wrapper变量选择方法，并用RF作为适应度函数；最后使用GA∩SA交集。

- evaluated_contrast_cn：GA、SA、交集、并集及全变量模型之间的性能比较。

- objective_result_cn：交集变量集使ANN模型达到最高敏感性0.792；交集比并集更好；全变量模型敏感性不高。

##### evidence_pointers

1. Table 4

2. Table 5

3. Table 6

#### 2. 2

- theory_or_knowledge_claim_cn：类别不平衡会导致分类器通过把样本全部判为多数类来最大化准确率，进而丢失少数类。

- mechanism_cn：训练数据中多数类主导损失函数，使少数类决策边界被压缩。

- design_requirement_cn：必须对训练集进行重采样以恢复少数类可学习性。

- artifact_choice_cn：比较RUS、ROS、SMOTE，且仅对训练折实施平衡。

- evaluated_contrast_cn：无平衡、RUS、ROS、SMOTE四类条件下的敏感性变化。

- objective_result_cn：无平衡时敏感性仅0.365–0.426；采用RUS后ANN+交集模型敏感性达0.792。

##### evidence_pointers

1. Section 3.3

2. Table 6

#### 3. 3

- theory_or_knowledge_claim_cn：ANN等黑箱模型不能直接给出变量作用，需要用敏感性分析和信息融合提取可解释信息。

- mechanism_cn：逐个排除或扰动变量并观察模型误差变化，可以估计每个变量的输出方差贡献。

- design_requirement_cn：最终模型选择后必须给出变量重要性和方向性洞见。

- artifact_choice_cn：对选定ANN进行10次敏感性分析，并使用AUC权重进行信息融合。

- evaluated_contrast_cn：变量重要性排名与已有失约文献的对照。

- objective_result_cn：既往失约、糖尿病、提醒、酗酒、提前期等变量重要性与文献一致，新增两次预约间隔变量。

##### evidence_pointers

1. Fig. 2

2. Section 4.2

#### 4. 4

- theory_or_knowledge_claim_cn：接近0.5的概率表示模型低置信，误分类风险高；人机协作可将不确定样本交给专家判断。

- mechanism_cn：把预测边界附近的样本移除或重新分配后，保留样本更易被正确分类。

- design_requirement_cn：模型概率应经可靠性验证，且区分高置信与低置信区域。

- artifact_choice_cn：阈值敏感性分析，逐步丢弃[0.4,0.6]、[0.3,0.7]、[0.2,0.8]、[0.1,0.9]区间样本。

- evaluated_contrast_cn：0.5阈值全保留与不同弃置区间的性能对比。

- objective_result_cn：丢弃低置信样本后AUC从0.846升至0.950，准确率/敏感性/特异性均提升。

##### evidence_pointers

1. Table 7

#### 5. 5

- theory_or_knowledge_claim_cn：管理决策需要离散风险等级，连续概率难以直接行动。

- mechanism_cn：聚类将接近的概率个体聚合为同质风险组，支持分层干预。

- design_requirement_cn：输出患者个体化风险分数，同时给出风险类别。

- artifact_choice_cn：对估计概率用k-means聚类成五个风险等级。

- evaluated_contrast_cn：五级风险组与二元阈值的操作差异。

- objective_result_cn：形成极低到极高五级风险，可结合医疗专家判断使用。

##### evidence_pointers

1. Fig. 3

2. Section 4.2

#### 6. 6

- theory_or_knowledge_claim_cn：若工具被诊所采用，精简模型可降低数据录入与计算时间，利于快速反应。

- mechanism_cn：减少预测所需变量数和模型复杂度，降低临床使用成本。

- design_requirement_cn：最终模型必须精简，且要有可直接使用的决策支持工具。

- artifact_choice_cn：使用GA∩SA得到的8个变量训练ANN，并开发Shiny Web工具。

- evaluated_contrast_cn：精简变量模型与全变量模型的敏感性对比。

- objective_result_cn：精简ANN达到最高敏感性；工具被开发并可输出风险分数和类别。

##### evidence_pointers

1. Section 5

2. Table 6

## 评价逻辑

### evaluation_modes

1. 10折交叉验证网格比较

2. 消融式对照：无平衡/有平衡、全变量/精简变量

3. 变量选择组合比较：GA、SA、交集、并集

4. 阈值敏感性分析

5. 变量重要性排序与外部文献对照

6. Web工具的示范性展示（无正式实证评价）

- why_these_evaluations_cn：每个评价对应一个具体论证缺口：网格比较确定最佳模型组合；消融对照验证类平衡和变量选择的增量贡献；变量选择组合比较说明交集优于并集；阈值敏感性分析证明概率分数可信；变量重要性对照把黑箱输出转成可解释知识；Web工具示范支撑实践应用主张。

- benchmark_and_contrast_chain_cn：先建立全变量且无平衡的基准模型，随后引入变量选择（GA/SA/交集）和平衡方法，逐项与基准对比；Table 5展示完整网格，Table 6专门拆出“无平衡”“仅平衡”“仅变量选择”“两者结合”四类，使读者看到敏感性从0.365–0.426逐步提高到0.792的因果链条；最后的阈值分析则在同一最优模型上进一步展示概率质量的边界条件。

### claim_evidence_ledger

#### 1. GA/SA变量选择能形成精简变量集。

- claim_cn：GA/SA变量选择能形成精简变量集。

- evidence_cn：SA选9个变量、GA选10个、交集8个；交集在初步分析中优于并集。

- status_cn：有直接证据；但未做统计显著性检验。

#### 2. 类平衡能显著提高少数类敏感性。

- claim_cn：类平衡能显著提高少数类敏感性。

- evidence_cn：Table 6显示无平衡时敏感性0.365–0.426，RUS后最高达0.792。

- status_cn：有直接证据。

#### 3. ANN+RUS+GA∩SA是最佳模型。

- claim_cn：ANN+RUS+GA∩SA是最佳模型。

- evidence_cn：Table 5中该组合获得最高敏感性0.792，且AUC 0.838、准确率0.730、特异性0.714。

- status_cn：有直接证据；但准确率/特异性不是最优，选择依赖“敏感性优先”的前提。

#### 4. GA+RUS能带来最高AUC 0.844。

- claim_cn：GA+RUS能带来最高AUC 0.844。

- evidence_cn：Table 5中ANN和EL均达到0.844。

- status_cn：有直接证据，但不作为最终模型选择。

#### 5. 变量重要性可经敏感性分析和信息融合获得。

- claim_cn：变量重要性可经敏感性分析和信息融合获得。

- evidence_cn：Fig. 2给出每个变量的标准化贡献百分比。

- status_cn：有计算证据，但未做变量重要性显著性检验。

#### 6. 变量重要性与现有医学文献一致。

- claim_cn：变量重要性与现有医学文献一致。

- evidence_cn：既往失约、糖尿病、提醒、酗酒、提前期、经济援助等均引用相应文献。

- status_cn：相关性支持，但非因果证据。

#### 7. 概率分数可靠，低置信区间应交给专家。

- claim_cn：概率分数可靠，低置信区间应交给专家。

- evidence_cn：Table 7显示丢弃[0.4,0.6]、[0.3,0.7]等区间后AUC/准确率/敏感性/特异性均提升。

- status_cn：有单折证据；没有校准曲线、Brier分数或外部验证。

#### 8. k-means可将患者分为五级风险。

- claim_cn：k-means可将患者分为五级风险。

- evidence_cn：Fig. 3显示五类风险组。

- status_cn：有聚类输出；但没有字段效度、临床可接受性或成本收益评价。

#### 9. Web工具可作为决策支持。

- claim_cn：Web工具可作为决策支持。

- evidence_cn：论文提供Shiny工具链接并描述输入输出。

- status_cn：仅示范，未做用户研究、部署或影响评估。

- internal_validity_strategy_cn：使用10折交叉验证并报告指标标准差；所有平衡只应用于训练折，避免信息泄漏；设置无平衡、全变量等对照组；变量选择通过RF交叉验证进行自适应度评价；对ANN参数进行交叉验证调参；最终选型以敏感性为明确优先指标并解释原因；阈值分析在同一样本上逐步放宽丢弃区间展示单调性能提升。

- external_validity_strategy_cn：使用真实世界巴西医疗预约数据；将得到的变量重要性与多个外部失约研究对齐；宣称方法可迁移到其他临床环境；开发Web工具使模型能被外部使用。但论文没有在第二地点或前瞻性队列中验证，未做时间外测试或跨机构测试。

- what_is_not_actually_tested_cn：没有检验GA/SA与逐步回归等基准变量选择方法在统计上的显著优势；没有评估k-means风险分层是否改善临床决策；没有真实临床部署；没有测量工具使用效果、患者结果或成本节省；阈值分析只来自单个折；没有报告校准曲线或Brier分数；没有验证“低置信区间交给专家”在实践中可行。

## 贡献闭环

- technical_claim_cn：在失约预测任务上，将GA/SA变量选择、RUS类平衡和ANN结合能够获得较高的少数类敏感性（0.792）和可与文献竞争或更优的AUC（0.838–0.844）。

- artifact_claim_cn：提出一个完整可复现的混合数据挖掘框架，包含变量选择、类平衡、多分类器比较、敏感性解释、概率验证、风险分层和Web工具。

- mechanism_claim_cn：元启发式变量选择可避免逐步/弹性网在共线性、过拟合、局部最优上的问题；类平衡提升少数类检测；阈值敏感性分析确认低置信区域应转交人工；信息融合使黑箱变量重要性可解释。

- boundary_claim_cn：结果基于巴西基层医疗公开数据，失约率约20%；优先使用敏感性指标意味着该方法面向“更重视捕获失约者”的运用场景；概率在0.5附近时模型不可靠，需专家判断；方法本身不提供调度处方。

- reusable_design_knowledge_cn：设计要点包括：用两种元启发式变量选择的交集作为精简变量集；仅对训练集做平衡并比较RUS/ROS/SMOTE；以敏感性为首要指标选择失约预测模型；用阈值敏感性分析定义低置信区间；用k-means把概率转成五级风险；用parsimonious模型构建Web工具以利快速数据录入和反应。

- theoretical_contribution_cn：论文没有提出新理论，主要贡献是方法论组合、经验性能证据和失约预测因子的进一步实证确认；其中“两次预约间隔”变量被视为文献中未充分探索的新预测因素。

- how_discussion_closes_intro_gap_cn：引言提出需要高精度预测、精简模型、对抗不平衡和提供个体风险等级；结论逐一回应：变量选择实现精简，RUS解决不平衡，ANN模型提供概率，五级风险分层和Web工具满足个体化决策支持。

- overclaim_or_unsupported_leaps_cn：作者声称GA/SA“最小化”共线性、过拟合和局部最优风险，但只基于算法性质而没有与传统变量选择方法做直接对比；阈值分析只用单个fold却用来普遍证明概率可靠性；k-means风险分层没有操作化验证；Web工具没有被测试就被称为可采用的决策支持工具；“首次使用数据平衡”的表1判断依赖文献边界，可能受检索范围影响。

## 句级写作动作图谱

### 1. Abstract P1 S1

- order：1

- section：Abstract

- locator：Abstract P1 S1

- move_code：CONTEXT

- paraphrase_cn：准确预测失约患者对提升调度系统效率至关重要。

- rhetorical_function_cn：一开场把预测任务放在调度效率的大背景下，点明价值。

- depends_on_cn：无。

- sets_up_cn：为后面提出预测模型目标提供动机。

- evidence_pointer：Abstract

### 2. Abstract P1 S2

- order：2

- section：Abstract

- locator：Abstract P1 S2

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：研究目的是构建一种新的混合数据挖掘方法，实现准确预测、精简模型、处理不平衡并提供个体风险等级。

- rhetorical_function_cn：以四项任务清单概括全文贡献目标。

- depends_on_cn：失约预测的重要性。

- sets_up_cn：为摘要后续方法选择和结果预告提供框架。

- evidence_pointer：Abstract

### 3. Abstract P1 S3

- order：3

- section：Abstract

- locator：Abstract P1 S3

- move_code：RESULT

- paraphrase_cn：建议使用ANN作为分类算法，并使用GA和SA共同选出的变量集以及RUS开展预测。

- rhetorical_function_cn：在摘要中直接给出最终方法配置，使读者快速了解核心发现。

- depends_on_cn：混合方法目标。

- sets_up_cn：为正文的模型选择结果做预告。

- evidence_pointer：Abstract

### 4. Abstract P2 S1-S2

- order：4

- section：Abstract

- locator：Abstract P2 S1-S2

- move_code：CONTRIBUTION

- paraphrase_cn：通过阈值敏感性分析证明患者个体风险分数可信，并开发了可被诊所采用的Web决策支持工具。

- rhetorical_function_cn：在摘要末尾突出可操作产出和实践价值。

- depends_on_cn：最佳模型和风险分数。

- sets_up_cn：引出正文中的阈值分析和工具章节。

- evidence_pointer：Abstract

### 5. Introduction P1 S1-S2

- order：5

- section：Introduction

- locator：Introduction P1 S1-S2

- move_code：CONTEXT

- paraphrase_cn：患者错过预约被称为失约，会给医疗机构带来收入减少和成本增加，也损害患者自身健康结局。

- rhetorical_function_cn：建立现实问题的重要性和紧迫性。

- depends_on_cn：无。

- sets_up_cn：为后续文献综述和研究目标提供问题背景。

- evidence_pointer：Introduction P1

### 6. Introduction P1 S3

- order：6

- section：Introduction

- locator：Introduction P1 S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：文献尝试了超量预约、行为激励、预付、罚款等多种策略来减少失约影响。

- rhetorical_function_cn：说明失约问题已有多种对策，但预测仍是基础。

- depends_on_cn：失约问题的成本描述。

- sets_up_cn：为转向预测模型必要性铺垫。

- evidence_pointer：Introduction P1

### 7. Introduction P2 S1

- order：7

- section：Introduction

- locator：Introduction P2 S1

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：预测失约患者很关键，因为高质量预测模型是高质量调度处方模型的基础。

- rhetorical_function_cn：将预测从分类问题提升为调度优化的前置条件。

- depends_on_cn：缓解策略仍依赖预测信息。

- sets_up_cn：说明本研究聚焦预测侧的合理性。

- evidence_pointer：Introduction P2

### 8. Introduction P2 S2-S3

- order：8

- section：Introduction

- locator：Introduction P2 S2-S3

- move_code：CONTEXT

- paraphrase_cn：复杂数据集与计算能力结合，为用数据驱动模型解决困难问题创造了机会。

- rhetorical_function_cn：为采用计算密集的数据挖掘方法提供时代背景。

- depends_on_cn：预测模型的重要性。

- sets_up_cn：引出混合数据挖掘方案的可用性。

- evidence_pointer：Introduction P2

### 9. Introduction P3 S1

- order：9

- section：Introduction

- locator：Introduction P3 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：我们开发了数据驱动方法，将失约患者分为五个风险等级。

- rhetorical_function_cn：首次明确核心研究目标。

- depends_on_cn：预测模型作为调度基础的论点。

- sets_up_cn：为后文风险分层和DSS作总领。

- evidence_pointer：Introduction P3

### 10. Introduction P3 S2

- order：10

- section：Introduction

- locator：Introduction P3 S2

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：研究只处理预测侧问题，不试图提供调度处方方案。

- rhetorical_function_cn：主动限定研究范围，避免读者对调度优化产生误解。

- depends_on_cn：研究目标陈述。

- sets_up_cn：把贡献边界限定在预测、风险分层和工具。

- evidence_pointer：Introduction P3

### 11. Introduction P3 S3

- order：11

- section：Introduction

- locator：Introduction P3 S3

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：调度系统可基于这些风险洞见被设计；同时我们还想识别导致失约的关键因素及不同时间尺度模式。

- rhetorical_function_cn：说明研究不仅做预测，还提供根因理解和决策支持。

- depends_on_cn：预测模型和风险等级。

- sets_up_cn：为敏感性分析和变量重要性分析提供动机。

- evidence_pointer：Introduction P3

### 12. Introduction P4

- order：12

- section：Introduction

- locator：Introduction P4

- move_code：STUDY_OVERVIEW

- paraphrase_cn：论文其余部分按文献、方法、结果、工具、结论依次组织。

- rhetorical_function_cn：向读者提供全文导航。

- depends_on_cn：无。

- sets_up_cn：为各章节阅读预期。

- evidence_pointer：Introduction P4

### 13. Section 2 P1

- order：13

- section：Section 2 Literature review

- locator：Section 2 P1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：自1960年代以来失约研究经历“broken appointments”到“no-shows”的术语变化，形成影响、缓解、预测三个研究流。

- rhetorical_function_cn：为文献定位提供历史脉络。

- depends_on_cn：引言中的问题背景。

- sets_up_cn：将本文定位到第三个研究流。

- evidence_pointer：Section 2 P1

### 14. Section 2 Table 1讨论段

- order：14

- section：Section 2 Literature review

- locator：Section 2 Table 1讨论段

- move_code：GAP

- paraphrase_cn：Table 1总结显示，现有研究在变量选择和类平衡方面存在空白，本文的有直接影响贡献来自这两项。

- rhetorical_function_cn：用表格概括文献矩阵，并以表格本身作为缺口证据。

- depends_on_cn：前文逐项文献综述。

- sets_up_cn：为第三、四节方法设计提供必要性论证。

- evidence_pointer：Section 2, Table 1后的段落

### 15. Section 2 紧接Table 1讨论

- order：15

- section：Section 2 Literature review

- locator：Section 2 紧接Table 1讨论

- move_code：GAP

- paraphrase_cn：目前没有研究采用计算高效且能避免共线性、过拟合和局部最优的综合变量选择方法。

- rhetorical_function_cn：明确具体的变量选择缺口。

- depends_on_cn：Table 1的文献矩阵。

- sets_up_cn：为采用GA/SA提供依据。

- evidence_pointer：Section 2, 紧接Table 1

### 16. Section 2 紧接Table 1讨论

- order：16

- section：Section 2 Literature review

- locator：Section 2 紧接Table 1讨论

- move_code：LIMITATION

- paraphrase_cn：虽然文献[36,38-40]用了计算高效的变量选择，但这些方法容易受共线性、过拟合或局部最优影响。

- rhetorical_function_cn：把已有方法的弱点作为新方法设计的反衬。

- depends_on_cn：文献综述例子。

- sets_up_cn：强化GA/SA作为替代方案的必要性。

- evidence_pointer：Section 2, 紧接Table 1

### 17. Section 2 类平衡缺口句

- order：17

- section：Section 2 Literature review

- locator：Section 2 类平衡缺口句

- move_code：GAP

- paraphrase_cn：在失约预测文献中，尚未发现使用数据平衡算法来强化少数类样本检测的研究。

- rhetorical_function_cn：声明第二个文献空白。

- depends_on_cn：Table 1中Imbalance handling列均为空。

- sets_up_cn：为后面RUS/ROS/SMOTE比较提供必要性。

- evidence_pointer：Section 2, 紧接Table 1

### 18. Section 2 工具与精简模型句

- order：18

- section：Section 2 Literature review

- locator：Section 2 工具与精简模型句

- move_code：CONTRIBUTION

- paraphrase_cn：除预测性能贡献外，作者还开发了Web决策支持工具；若被医疗中心采用，精简模型能降低数据录入和计算时间。

- rhetorical_function_cn：补充实践贡献，并说明parsimony对实际部署的意义。

- depends_on_cn：文献缺口和工具开发计划。

- sets_up_cn：为结论部分的贡献清单和第5节工具做铺垫。

- evidence_pointer：Section 2末尾

### 19. Section 3 P1

- order：19

- section：Section 3 Methodology

- locator：Section 3 P1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：为给实践者提供更好信息以开发调度系统，本文提出四步框架。

- rhetorical_function_cn：章节开头预览方法论流程。

- depends_on_cn：文献缺口声明。

- sets_up_cn：为后面四个小节安排论述顺序。

- evidence_pointer：Section 3 P1, Fig. 1

### 20. Section 3 P2

- order：20

- section：Section 3 Methodology

- locator：Section 3 P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：第一步处理巴西数据集，第二步用SA和GA选变量，第三步平衡数据并用三种分类模型与集成学习训练，第四步分析性能、变量重要性、风险分层并开发工具。

- rhetorical_function_cn：以流程化语言告知读者完整技术链。

- depends_on_cn：四步框架概述。

- sets_up_cn：为后续每个子节提供总索引。

- evidence_pointer：Section 3 P2

### 21. Section 3.1 P1

- order：21

- section：Section 3.1

- locator：Section 3.1 P1

- move_code：DESIGN_FEATURE

- paraphrase_cn：数据集来自Kaggle，原始数据有110,528条记录和14个变量，并派生出提前期、呼叫时间、日期组件、既往失约、预约间隔等变量。

- rhetorical_function_cn：说明数据来源与特征工程，使模型可复现。

- depends_on_cn：四步框架第一步。

- sets_up_cn：为变量选择提供候选特征。

- evidence_pointer：Section 3.1, Table 2

### 22. Section 3.2 P1

- order：22

- section：Section 3.2

- locator：Section 3.2 P1

- move_code：REQUIREMENT

- paraphrase_cn：变量选择是从原变量集中提取最相关子集，能帮助找到高效预测目标的简单模型；但大数据下搜索空间巨大。

- rhetorical_function_cn：设定了变量选择任务的必要性和困难。

- depends_on_cn：特征工程结果。

- sets_up_cn：引向穷举不可行和元启发式方案。

- evidence_pointer：Section 3.2 P1

### 23. Section 3.2 P2-P3

- order：23

- section：Section 3.2

- locator：Section 3.2 P2-P3

- move_code：LIMITATION

- paraphrase_cn：已有filter和wrapper方法存在局限：逐步/似然比在共线性下表现差，弹性网易过拟合，穷举搜索在16个变量下要评估2^16种组合不可行。

- rhetorical_function_cn：直接指出替代方案的问题，为GA/SA创造逻辑入口。

- depends_on_cn：变量选择的分类学。

- sets_up_cn：引出“准确、精简且不昂贵”的需求。

- evidence_pointer：Section 3.2 P2-P3

### 24. Section 3.2 P4

- order：24

- section：Section 3.2

- locator：Section 3.2 P4

- move_code：REQUIREMENT

- paraphrase_cn：因此需要一种准确、精简但没有穷举计算负担的方法，故使用SA和GA。

- rhetorical_function_cn：从方法缺陷到需求再到技术选型的桥接句。

- depends_on_cn：对逐步/弹性网/穷举的批评。

- sets_up_cn：为3.2.1和3.2.2详细算法参数提供总纲。

- evidence_pointer：Section 3.2末尾

### 25. Section 3.2 P5

- order：25

- section：Section 3.2

- locator：Section 3.2 P5

- move_code：DESIGN_FEATURE

- paraphrase_cn：作者还考虑GA和SA所得变量集的组合，因为经验结果显示组合多个变量选择算法可带来更好模型。

- rhetorical_function_cn：为后文交集/并集比较提供依据。

- depends_on_cn：GA/SA各自产生的变量集。

- sets_up_cn：为结果中交集优于并集埋下伏笔。

- evidence_pointer：Section 3.2末尾

### 26. Section 3.2.1 P1

- order：26

- section：Section 3.2.1

- locator：Section 3.2.1 P1

- move_code：MECHANISM

- paraphrase_cn：SA模仿退火过程，通过温度控制可随机接受较差解，从而跳出局部最优。

- rhetorical_function_cn：解释SA为什么适合全局搜索变量子集。

- depends_on_cn：选择SA作为变量选择方法。

- sets_up_cn：为后续SA参数的讨论提供机制基础。

- evidence_pointer：Section 3.2.1

### 27. Section 3.2.1 P2

- order：27

- section：Section 3.2.1

- locator：Section 3.2.1 P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：SA使用RF作为适应度函数，因为RF对多重共线性和过拟合不敏感；此外设置连续50次无改进便重置当前解，并运行10次不同初始解。

- rhetorical_function_cn：描述SA的工程化细节，说明为何能规避局部最优和过拟合。

- depends_on_cn：SA的机制。

- sets_up_cn：为结果中变量子集的合理性提供依据。

- evidence_pointer：Section 3.2.1

### 28. Section 3.2.2 P1

- order：28

- section：Section 3.2.2

- locator：Section 3.2.2 P1

- move_code：DESIGN_FEATURE

- paraphrase_cn：GA通过二进制染色体、交叉和变异在离散搜索空间进化出最优变量子集。

- rhetorical_function_cn：介绍GA机制并连接变量选择问题。

- depends_on_cn：GA作为变量选择工具。

- sets_up_cn：为GA参数表做准备。

- evidence_pointer：Section 3.2.2

### 29. Section 3.2.2 P2

- order：29

- section：Section 3.2.2

- locator：Section 3.2.2 P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：GA设置种群100、250代、交叉概率0.8、变异概率0.1和精英数量3，以平衡探索、多样性和收敛。

- rhetorical_function_cn：用具体参数说明GA如何被定制来避免局部最优。

- depends_on_cn：GA机制描述。

- sets_up_cn：为结果中的GA变量集提供可复现细节。

- evidence_pointer：Section 3.2.2, Table 3

### 30. Section 3.3 P1

- order：30

- section：Section 3.3

- locator：Section 3.3 P1

- move_code：MECHANISM

- paraphrase_cn：数据集中约20%失约、80%履约，分类器可能通过把全部样本判为多数类来最小化损失并最大化总体准确率。

- rhetorical_function_cn：解释类不平衡为什么会导致少数类检测失效。

- depends_on_cn：数据描述。

- sets_up_cn：为采用重采样技术提供机制理由。

- evidence_pointer：Section 3.3 P1

### 31. Section 3.3 P2

- order：31

- section：Section 3.3

- locator：Section 3.3 P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：之所以选择采样方法，是因为它们与任何机器学习算法兼容；代价敏感学习需要未知的误分类成本，故未采用。

- rhetorical_function_cn：解释方法选择边界，避免读者质疑为何不用代价敏感学习。

- depends_on_cn：类不平衡问题的类别。

- sets_up_cn：为RUS/ROS/SMOTE的具体采用建立合法性。

- evidence_pointer：Section 3.3 P2

### 32. Section 3.3 P3

- order：32

- section：Section 3.3

- locator：Section 3.3 P3

- move_code：GAP

- paraphrase_cn：已有文献中没有研究在失约预测中使用任何平衡方法，而本文使用了RUS、ROS和SMOTE。

- rhetorical_function_cn：在方法选择处再次强调与文献的差异。

- depends_on_cn：Table 1文献矩阵。

- sets_up_cn：为结果中的平衡对比提供预期。

- evidence_pointer：Section 3.3 P3

### 33. Section 3.4 P1

- order：33

- section：Section 3.4

- locator：Section 3.4 P1

- move_code：DESIGN_FEATURE

- paraphrase_cn：研究采用ANN、RF、LR三种模型，并将三者概率平均构成集成学习器EL。

- rhetorical_function_cn：列出分类模型池和集成策略。

- depends_on_cn：变量选择和平衡方法。

- sets_up_cn：为Table 5的分类结果提供方法细节。

- evidence_pointer：Section 3.4 P1

### 34. Section 3.4.1 P1-P2

- order：34

- section：Section 3.4.1

- locator：Section 3.4.1 P1-P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：ANN使用单隐层反向传播网络，通过权重衰减惩罚损失函数防止过拟合，并用交叉验证调参。

- rhetorical_function_cn：说明ANN的架构、正则化和调参。

- depends_on_cn：选择ANN作为候选模型。

- sets_up_cn：为ANN在高敏感性上胜出提供技术合理性。

- evidence_pointer：Section 3.4.1

### 35. Section 3.5 P1-P2

- order：35

- section：Section 3.5

- locator：Section 3.5 P1-P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：ANN等黑箱模型没有闭式机制可解释，因此需要敏感性分析来估计每个预测变量的影响。

- rhetorical_function_cn：建立“黑箱模型需要解释工具”的方法论逻辑。

- depends_on_cn：最终模型是ANN。

- sets_up_cn：为Saltelli敏感性和信息融合公式铺垫。

- evidence_pointer：Section 3.5

### 36. Section 3.6 P1-P2

- order：36

- section：Section 3.6

- locator：Section 3.6 P1-P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：信息融合将多个模型得到的敏感性分数按AUC加权汇总，以降低不确定性并提高信息完整性。

- rhetorical_function_cn：引入融合方法，使变量重要性更稳健。

- depends_on_cn：敏感性分析。

- sets_up_cn：为Fig. 2变量重要性结果做方法交代。

- evidence_pointer：Section 3.6

### 37. Section 4.1 P1

- order：37

- section：Section 4.1

- locator：Section 4.1 P1

- move_code：RESULT

- paraphrase_cn：GA和SA找到不同的次优变量子集：两个算法共同选择预约日、提前期、提醒、酗酒、经济援助、糖尿病、既往失约和预约间隔，但GA额外选年龄和月份，SA额外选残疾。

- rhetorical_function_cn：报告变量选择结果，并展示两种元启发式的异同。

- depends_on_cn：GA/SA变量选择过程。

- sets_up_cn：为交集变量集的合法性提供证据。

- evidence_pointer：Section 4.1, Table 4

### 38. Section 4.1 P2

- order：38

- section：Section 4.1

- locator：Section 4.1 P2

- move_code：RESULT

- paraphrase_cn：在初步分析中，交集变量集优于并集，可能因为并集导致过拟合；因此只保留交集。

- rhetorical_function_cn：用初步结果做组合决策，并强调parsimony。

- depends_on_cn：两算法子集结果。

- sets_up_cn：为后续所有交集变量模型提供前提。

- evidence_pointer：Section 4.1

### 39. Section 4.2 P1-P2

- order：39

- section：Section 4.2

- locator：Section 4.2 P1-P2

- move_code：RESULT

- paraphrase_cn：Table 5显示，最高AUC 0.844来自EL和ANN，使用GA与RUS；最高准确率和特异性来自EL+GA+SMOTE；最高敏感性0.792来自ANN+交集变量+RUS。

- rhetorical_function_cn：用网格结果给读者三条最佳配置。

- depends_on_cn：10折交叉验证实验。

- sets_up_cn：为后续“敏感性优先”选型提供数据基础。

- evidence_pointer：Section 4.2, Table 5

### 40. Section 4.2 P3

- order：40

- section：Section 4.2

- locator：Section 4.2 P3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：选择敏感性作为主要标准，因为正确检测失约者才能采取行动减少失约成本。

- rhetorical_function_cn：解释为什么最终模型不是全局最高的那个，而是敏感性最高的组合。

- depends_on_cn：Table 5中各组合的指标。

- sets_up_cn：为选择ANN+交集+RUS提供决策规则。

- evidence_pointer：Section 4.2 P3

### 41. Section 4.2 P4

- order：41

- section：Section 4.2

- locator：Section 4.2 P4

- move_code：RESULT

- paraphrase_cn：Table 6显示不使用平衡的模型敏感性很低，而全变量模型也未能超过精简变量模型的最高敏感性。

- rhetorical_function_cn：用消融式表格证明平衡与变量选择的增量贡献。

- depends_on_cn：Table 6的对照实验。

- sets_up_cn：为类不平衡和parsimony的核心贡献提供证据。

- evidence_pointer：Section 4.2, Table 6

### 42. Section 4.2 敏感性分析结果段

- order：42

- section：Section 4.2

- locator：Section 4.2 敏感性分析结果段

- move_code：RESULT

- paraphrase_cn：敏感性分析显示既往失约占比28.08%、糖尿病12.03%，两者合计占预测能力40.11%。

- rhetorical_function_cn：从模型性能转向变量重要性解释。

- depends_on_cn：信息融合结果。

- sets_up_cn：为与文献对齐的讨论提供数据。

- evidence_pointer：Section 4.2, Fig. 2

### 43. Section 4.2 文献照应段

- order：43

- section：Section 4.2

- locator：Section 4.2 文献照应段

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：所得变量重要性与现有文献一致，例如既往失约、糖尿病、提醒、酗酒、提前期、经济援助均有外部研究支持。

- rhetorical_function_cn：用外部文献支持内部发现的合理性，增加可推广性。

- depends_on_cn：变量重要性百分比。

- sets_up_cn：为“新变量”的贡献做对照。

- evidence_pointer：Section 4.2

### 44. Section 4.2 两次预约间隔段

- order：44

- section：Section 4.2

- locator：Section 4.2 两次预约间隔段

- move_code：CONTRIBUTION

- paraphrase_cn：作者没有发现文献研究“两次预约间隔”这一特征，并将其解释为患者预约频率和慢性病状态的信号。

- rhetorical_function_cn：指出本研究在变量发现上的新颖性。

- depends_on_cn：变量重要性排序。

- sets_up_cn：为结论中的知识贡献服务。

- evidence_pointer：Section 4.2

### 45. Section 4.2 阈值分析段

- order：45

- section：Section 4.2

- locator：Section 4.2 阈值分析段

- move_code：RESULT

- paraphrase_cn：Table 7显示，当丢弃概率在[0.4,0.6]、[0.3,0.7]、[0.2,0.8]、[0.1,0.9]区间内的样本后，模型各指标持续上升，最终AUC 0.950、准确率0.942。

- rhetorical_function_cn：用阈值实验证明概率分数在低置信区域之外是可靠的。

- depends_on_cn：选定ANN模型在第七折上的概率输出。

- sets_up_cn：为“人机协作处理不确定样本”提供直接依据。

- evidence_pointer：Section 4.2, Table 7

### 46. Section 4.2 概率可靠性结论段

- order：46

- section：Section 4.2

- locator：Section 4.2 概率可靠性结论段

- move_code：CONTRIBUTION

- paraphrase_cn：模型性能随不确定样本被丢弃而提升，说明概率分数可信；专家可介入概率接近0.5的个案。

- rhetorical_function_cn：把阈值分析上升为概率可靠性和人机协作主张。

- depends_on_cn：Table 7结果。

- sets_up_cn：为五级风险分层和DSS做铺垫。

- evidence_pointer：Section 4.2

### 47. Section 4.2 k-means段

- order：47

- section：Section 4.2

- locator：Section 4.2 k-means段

- move_code：DESIGN_FEATURE

- paraphrase_cn：用k-means将患者概率分成极低、低、中、高、极高五级风险。

- rhetorical_function_cn：将连续概率转成管理可用的离散风险等级。

- depends_on_cn：模型概率输出和阈值分析。

- sets_up_cn：引出Web工具的风险类别功能。

- evidence_pointer：Section 4.2, Fig. 3

### 48. Section 5 P1-P2

- order：48

- section：Section 5 Decision support tool

- locator：Section 5 P1-P2

- move_code：CONTRIBUTION

- paraphrase_cn：作者开发了一个集成最优ANN模型的Web决策支持工具，可输入预约和患者信息，输出个体失约风险分数和风险类别。

- rhetorical_function_cn：把方法成果实体化为可部署工具。

- depends_on_cn：最终模型和k-means分层。

- sets_up_cn：为结论中的实践贡献服务。

- evidence_pointer：Section 5

### 49. Section 6 P2

- order：49

- section：Section 6 Conclusions

- locator：Section 6 P2

- move_code：CONTRIBUTION

- paraphrase_cn：本文的贡献不是应用已知分类模型，而是变量选择、数据平衡、五级风险分层和Web工具。

- rhetorical_function_cn：集中声明贡献边界，避免被解读为纯算法应用。

- depends_on_cn：全文方法、结果和工具。

- sets_up_cn：为后续对贡献的逐条展开提供总括。

- evidence_pointer：Section 6 P2

### 50. Section 6 P3

- order：50

- section：Section 6 Conclusions

- locator：Section 6 P3

- move_code：RESULT

- paraphrase_cn：阈值敏感性分析证明概率分数可信，低置信个案应结合医学专家直觉与激励进行最终决策。

- rhetorical_function_cn：将内部评价结果提升为临床使用建议。

- depends_on_cn：Table 7阈值分析。

- sets_up_cn：为未来工具发展方向提供逻辑。

- evidence_pointer：Section 6 P3

### 51. Section 6 P4

- order：51

- section：Section 6 Conclusions

- locator：Section 6 P4

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：主要限制是公开数据集无法收集预约原因、紧急程度、病情严重度、当日具体时段等更丰富特征；未来工具应不仅预测风险组，还建议风险最小的预约日期。

- rhetorical_function_cn：承认数据局限并给出来来自改进方向。

- depends_on_cn：公开数据和工具现状。

- sets_up_cn：结束全文，防止贡献被绝对化。

- evidence_pointer：Section 6 P4

## 写作技术

- gap_construction_cn：先用现实成本说明失约问题，再通过文献矩阵把作者想强调的两个空白集中展示：已有变量选择方法存在共线性/过拟合/局部最优问题，失约预测中没有系统使用类平衡技术；同时用“没有Web工具”“没有风险分层”补充实践缺口。

- signposting_cn：引言末尾给出完整章节地图；方法部分用“四步框架”作为总路标，并在每小节开头交代该步的功能；结果部分经常用“Table X显示”“Fig. X显示”将读者指向证据。

- transition_logic_cn：每阶段结尾留下未解决问题，下一阶段开始承接。例如变量选择结果后问“哪个组合最好”，分类实验后问“哪个变量重要”，重要性后问“概率是否可靠”，概率可靠后问“如何分层”，分层后问“如何交付工具”。

- claim_evidence_rhythm_cn：先密集铺设方法和文献知识，再以表格给出结果，每段结果后紧跟一句“这说明……”或“因此我们选择……”，并在关键处使用消融表把贡献归因到特定技术。

- benchmark_narrative_cn：不是单一基准，而是多阶段对照：Table 5网格决定最优配置；Table 6专门隔离“变量选择”和“平衡”两个因素的贡献；Table 7在同一最优模型上验证概率质量。benchmark被嵌入到每类主张的证据链中。

- theory_return_cn：没有正式理论，但讨论部分把变量重要性结果与大量医学/管理文献对齐，使计算发现获得外部知识支持；新变量“两次预约间隔”被单独提出作为对失约预测知识的小增量。

- contribution_positioning_cn：在结论中明确“贡献不是应用已知分类模型”，而是四层组合贡献，从而防止读者认为这只是机器学习练习。

- novelty_protection_cn：通过表1的文献矩阵突出GA/SA变量选择和类平衡空白；通过Table 6无平衡/无变量选择的对照证明技术增量；通过Web工具和风险分层增加不可压缩的实践附加值；通过阈值分析把性能优势与“可解释概率”绑定。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：用一个高成本现实问题开场，并说明预测是处方/调度的前置条件。

- research_job_cn：收集或使用公开数据，明确目标变量和类别不平衡情况。

- required_evidence_cn：领域问题的成本/健康后果证据，数据可用性。

- transition_to_next_cn：从“问题重要”过渡到“已有方法不足”。

#### 2. 2

- step：2

- writing_job_cn：用文献综述和表格式对比展示已有方法在某个维度上的空缺。

- research_job_cn：系统回顾相关预测/数据挖掘文献，提取可对比的方法特征。

- required_evidence_cn：能支持“尚无研究做X”的文献矩阵或引用。

- transition_to_next_cn：从“文献没做”转向“本文如何做”。

#### 3. 3

- step：3

- writing_job_cn：把需求转成一套多阶段方法论，用流程图和章节预告呈现。

- research_job_cn：设计数据清洗、变量选择、类平衡、建模、解释、落地工具等环节。

- required_evidence_cn：每一步的具体材料、参数和计算可行性。

- transition_to_next_cn：从方法描述过渡到“结果如何”。

#### 4. 4

- step：4

- writing_job_cn：用网格实验和消融对照表展示性能差异，并明确选择模型的主要指标。

- research_job_cn：运行10折交叉验证等稳健评价，记录多个指标，并做无平衡/全变量对照。

- required_evidence_cn：性能表、标准差、不同组合比较。

- transition_to_next_cn：从“哪个模型最好”过渡到“为什么好、如何解释”。

#### 5. 5

- step：5

- writing_job_cn：用敏感性分析、信息融合或SHAP等方法解释黑箱结果，并对照领域文献。

- research_job_cn：计算变量重要性，并通过文献支持或领域机制解释结果。

- required_evidence_cn：变量重要性排序，以及至少一条外部文献/领域证据。

- transition_to_next_cn：从“变量重要”过渡到“预测概率是否可靠”。

#### 6. 6

- step：6

- writing_job_cn：用阈值/校准分析验证模型概率质量，并说明低置信样本如何处理。

- research_job_cn：做阈值敏感性分析或校准曲线，考察高置信/低置信区分。

- required_evidence_cn：阈值区间与性能变化表。

- transition_to_next_cn：从“概率可靠”过渡到“可以分层使用”。

#### 7. 7

- step：7

- writing_job_cn：把连续输出转成离散风险等级，并开发可演示的决策支持工具。

- research_job_cn：聚类或规则化概率，部署Web工具或原型。

- required_evidence_cn：风险等级划分和工具链接/截图。

- transition_to_next_cn：从“工具可用”过渡到“贡献与局限”。

#### 8. 8

- step：8

- writing_job_cn：在结论中把贡献从“性能提升”升维为“方法组合+可解释风险分层+工具”，同时承认数据和方法边界。

- research_job_cn：总结技术贡献、实践贡献和限制，并给出未来方向。

- required_evidence_cn：与引言缺口一一对应的贡献清单。

- transition_to_next_cn：无。

### most_transferable_moves_cn

1. 用文献综述矩阵制造缺口

2. 以四阶段流程作为方法叙述骨架

3. 用消融式表格将性能归因到单一设计因素

4. 明确“为首要业务指标选择模型”的决策规则

5. 用敏感性/信息融合把黑箱模型转成可解释洞见

6. 用阈值分析处理低置信样本和人工介入

7. 用聚类把概率转成风险等级

8. 用Web工具把方法论沉淀为可试用产品

### resource_intensive_or_nonstandard_parts_cn

1. GA/SA变量选择本身较消耗计算资源，尤其组合大量分类器与交叉验证

2. 需要可复现的电子健康记录或公开医疗预约数据

3. 开发Shiny/Web工具需要额外前端或平台支持

4. 敏感性和信息融合需要多次运行模型，计算时间较高

5. 如果要验证实际临床收益，需要诊所现场部署和长期效果数据，本文未做

### what_not_to_copy_superficially_cn

1. 不要只声明“用了GA/SA”而没有与简单基准对比

2. 不要只报告AUC而不报告少数类敏感性，尤其在类别不平衡场景

3. 不要用“丢弃不确定样本后指标上升”直接断言模型校准良好，还需要校准曲线或外部验证

4. 不要在没有成本收益分析的情况下声称风险分层能改善决策

5. 不要仅凭Web工具链接就声称已被临床采用

6. 不要在无理论框架时硬造理论贡献，应像本文一样定位为方法论和实证知识贡献

- single_best_description_of_the_routine_cn：先以文献表制造缺口，再用多阶段数据挖掘管线构建和评价，靠消融对照把性能归因到类平衡和变量选择，最后用黑箱解释、概率阈值分析和风险聚类把纯预测结果打包成可操作的个体风险工具。

## 分析边界

本次分析基于全文文本，原文中部分图表以图片形式出现，但文字描述和表格数据已足够支撑结构判断。对Table 5/6/7的解读依赖OCR文本，个别数字可能存在识别误差；没有实际访问论文提供的Shiny工具链接，因此工具章节只按论文描述总结。
