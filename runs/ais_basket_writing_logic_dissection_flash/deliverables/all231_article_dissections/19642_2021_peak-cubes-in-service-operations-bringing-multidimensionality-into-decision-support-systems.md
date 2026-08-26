# Peak cubes in service operations: Bringing multidimensionality into decision support systems

- 作者：Arash Barfar; Balaji Padmanabhan; Alan Hevner
- 年份 / 期刊：2021 / Decision Support Systems
- DOI：10.1016/j.dss.2020.113442
- 源文件：19642_2021_peak-cubes-in-service-operations-bringing-multidimensionality-into-decision-support-systems.md
- 论文主类型：computational_artifact_benchmark
- 主导写作弧线：performance_gap_artifact_benchmark_generalize
- 置信度：0.86

## 文章级论证概况

- 核心问题：在服务运营中，当企业拥有多维服务质量时间序列时，如何将行为经济学中的峰终规则从单维推广到多维，并构建能辅助流失预警与服务质量改进的决策支持方法？

- 制品与设计：作者提出“峰值立方（peak cube）”这一计算构造：对每位顾客的所有服务质量失败维度子空间，计算其Pareto前沿（skyline），并从中剔除属于更低维子空间的峰点，得到所有子空间上真正的多维峰值。配套给出了PeakCube算法、BCD编码、基于峰值的特征类，以及利用Shapley值做特征解释的流程。

- 客观结果：在4000个模拟客户群（共400万顾客）上，使用逻辑回归、LightGBM和SVM建立24000个流失预测模型。用多维峰值特征时平均AUROC约84%，显著高于单维峰值特征的约64%；且在多数服务场景参数变化下，多维模型的优势稳健。Shapley分析进一步给出最关键的失败组合子空间。

- 核心贡献：将峰终规则从单维服务体验扩展到多维服务体验，提出峰值立方作为可计算的DSS构件；证明多维峰值特征能显著改善顾客不满/流失预测；用Shapley值把黑箱预测转换为可操作的服务质量子空间建议；并整合行为经济学、数据库skyline、预测建模和服务科学，形成客户体验分析的新研究方向。

- 整篇论证链：论文先以“服务感知即现实”和服务体验影响忠诚为背景，引出行为经济学中的峰终规则，并指出现有研究只在单一服务质量维度上应用该规则，因而会忽略多变量同时达到峰值所形成的多维峰效应。作者用B2B物流中的损坏包裹与丢失包裹例子说明，只有同时观察两个失败维度才能发现第12次服务事件是多维峰值事件，而传统单维分析会漏掉这一点。为解决该缺口，作者借鉴数据库skyline与skycube的思想，把“多维峰值”定义为某个子空间skyline中不属于任何更低维峰值的服务事件，并给出PeakCube算法及BCD编码实现。由于真实企业数据受保密协议限制，作者设计了三模块仿真引擎，在4000个随机参数配置的客户群中嵌入已知流失模式，加入三种噪声，再对每名顾客构建峰值立方并提取端期特征。随后用三种分类器对比单维与多维峰值特征在流失预测上的AUROC，发现多维峰值特征在全部配置上显著更优，并按噪声参数、失败概率、最大幅度和模式最小维度做边界分析。最后用Shapley值解释模型，识别最应避免的服务失败子空间，把预测结果转化回服务设计知识，并讨论在医疗等领域的前景。整条线从行为理论到计算构造，再到仿真验证，最后回到设计决策支持。

## 类型与写作弧线判定

- 论文主类型判定：论文的核心证据来自计算制品（峰值立方与PeakCube算法）在模拟数据集上的benchmark：作者构造海量仿真顾客基，以流失预测AUROC为主要指标，系统对比单维与多维峰值特征。没有理论假设的受控行为实验，也没有真实平台/组织现场因果检验，而是以数据集与基准评价作为主要论证方式。

- 主导写作弧线判定：文章按“单维峰终规则性能/覆盖力不足→构造峰值立方制品→仿真benchmark检验→归纳可用于服务设计的泛化知识”展开。行为理论主要提供起点和解释语言，推进论证的主要逻辑是制品性能差距、计算基准、参数稳健性检验，最后把结论推广为设计知识与未来研究方向。

## 研究开展程序

- study_or_phase_count：6

- 研究阶段总序列：概念构建与算法设计→仿真数据生成→大规模峰值立方计算与特征提取→高层流失预测对比→服务场景稳健性与边界分析→Shapley可解释性与部署建议。前一阶段为后一阶段提供输入：概念模型决定算法，算法处理仿真数据，仿真数据支撑预测模型，预测模型结果再被参数切片和可解释性分析深化。

### studies_or_phases

#### 1. 峰值立方概念与PeakCube算法设计

- order：1

- name_cn：峰值立方概念与PeakCube算法设计

- question_cn：如何在多维服务质量时间序列中精确定义并计算“多维峰值”？

- inputs_and_setting_cn：B2B物流服务运营的动机性例子；数据库中skyline与skycube文献；服务失败时间序列的形式化表示。

- designed_or_compared_object_cn：峰值立方模型、PeakCube算法、BCD子空间编码、多类峰值特征。与全空间skyline和skycube进行概念对比。

- baseline_control_or_counterfactual_cn：全空间skyline与skycube作为未完全捕捉多维峰值的替代概念。

##### objective_metrics

（空）

- analysis_method_cn：概念分析、算法设计与形式化定义；使用rPref等偏好关系实现skyline计算。

- main_result_cn：给出peak(S)=Skyline(S)−更低维子空间峰值的定义；提出PeakCube算法，可用BCD码在运行时构造过滤集。

- argumentative_role_cn：把行为经济学中的“峰值”转化为可计算的数据库式构造，为后续仿真和预测提供制品基础。

- remaining_uncertainty_cn：概念是否有预测价值尚未验证；算法在真实规模下是否可行也未验证。

- link_to_next_phase_cn：需要构造具有已知嵌入流失模式的仿真数据，才能检验峰值立方特征是否真的能改善预测。

##### evidence_pointers

1. Section 3.1 peak cube model

2. Fig. 4 PeakCube algorithm

3. Section 3.2 BCD coding

4. Section 3.3 feature engineering

#### 2. 多维服务失败时间序列仿真系统构建

- order：2

- name_cn：多维服务失败时间序列仿真系统构建

- question_cn：如何生成大量有已知多维峰终流失模式的客户基，并覆盖不同服务运营场景？

- inputs_and_setting_cn：参数包括nCustomer=1000、nEncounter=52、calibrationWindow=8、churnRate=0.4、nPattern=100、minPatternSize=2~5、maxMagnitude、UB；三个模块为CreateEmbeddedPatterns、NonChurnServiceFailures、CreateCustomers。

- designed_or_compared_object_cn：仿真系统本身；嵌入的流失模式、失败regime、三种噪声参数。

- baseline_control_or_counterfactual_cn：参数变化形成不同服务场景；噪声水平变化作为干扰；模型并未直接与无模式仿真对照，但通过嵌入模式形成ground truth。

##### objective_metrics

1. 客户数量

2. 服务事件数量

3. 嵌入流失模式数量

4. 噪声参数取值

- analysis_method_cn：随机参数化仿真；模块化算法生成多维时间序列。

- main_result_cn：生成4000个客户基、400万顾客、约2.6亿个五维服务事件；每个客户基包含1000个嵌入流失模式，并加入churnWithPatternP、unexpectedChurnP、nonChurnerSeesPatternP三类噪声。

- argumentative_role_cn：提供有已知真值的实验场地，使研究者能判断峰值立方方法是否找回嵌入的多维峰值模式，并检验其在噪声下的稳定性。

- remaining_uncertainty_cn：仿真模式不一定对应真实管理者的决策启发；结果只证明在人为嵌入模式下有效。

- link_to_next_phase_cn：生成的客户基需要交给PeakCube算法计算峰值立方，形成特征数据。

##### evidence_pointers

1. Section 4 simulation overview

2. Fig. 5 CreateEmbeddedPatterns

3. Fig. 6 NonChurnServiceFailures

4. Fig. 7 CreateCustomers

#### 3. 大规模峰值立方计算与特征提取

- order：3

- name_cn：大规模峰值立方计算与特征提取

- question_cn：PeakCube算法能否在百万级顾客数据上运行，并导出可用于流失预测的特征？

- inputs_and_setting_cn：400万模拟顾客的五维服务失败时间序列；PeakCube算法输出<iteration ID, customer ID, event ID, subspace, subspace binary code, subspace level>。

- designed_or_compared_object_cn：峰值立方数据结构；高层特征包括unidimensional peaks、multidimensional peaks、各维度命中数、子空间最后遭遇事件。

- baseline_control_or_counterfactual_cn：单维峰值特征作为基线特征集合。

##### objective_metrics

1. 峰值数量

2. 数据规模

3. 特征维度

- analysis_method_cn：按顾客分别运行PeakCube；多线程桌面计算；特征工程。

- main_result_cn：从400万顾客构建了约7300万服务失败峰值；每名顾客可计算单维与多维峰值计数等高层特征。

- argumentative_role_cn：将概念制品转化为可直接进预测模型的独立变量，证明算法在规模化数据上可行。

- remaining_uncertainty_cn：这些特征是否真的提高预测效果，尚未在预测模型中检验。

- link_to_next_phase_cn：把峰值特征与流失标签组成4M观测数据集，进入预测模型训练与对比阶段。

##### evidence_pointers

1. Section 5 P1-P3

2. Section 3.3

#### 4. 高层流失预测模型对比实验

- order：4

- name_cn：高层流失预测模型对比实验

- question_cn：在相同条件下，使用多维峰值特征是否比单维峰值特征更准确地预测顾客流失？

- inputs_and_setting_cn：4M条观测，每条<customer base ID, customer ID, unidimensional peaks, multidimensional peaks, churn flag>；三个分类器；70%训练、30%测试。

- designed_or_compared_object_cn：单维峰值特征模型 vs 多维峰值特征模型；逻辑回归、LightGBM、SVM三种技术。

- baseline_control_or_counterfactual_cn：单维峰值特征作为直接对照。

##### objective_metrics

1. AUROC

2. Welch ANOVA显著性

- analysis_method_cn：对4000个客户基分别训练两个模型集，共24000个模型；用30%留出样本计算AUROC。

- main_result_cn：平均AUROC从单维的约64%提高到多维的约84%；Welch ANOVA显示提升显著；多维特征下三种分类器性能接近。

- argumentative_role_cn：提供峰值立方制品有效性的核心证据，说明多维视角的峰终规则确实带来可观的流失预测增益。

- remaining_uncertainty_cn：平均结果可能掩盖不同服务场景下的差异；也需要知道哪些子空间最重要。

- link_to_next_phase_cn：需要按仿真参数分解结果，检验增益在哪些场景存在、在哪些场景减弱，随后用Shapley识别关键子空间。

##### evidence_pointers

1. Section 5 P5-P6

2. Section 6 P1

3. Table 3

#### 5. 服务场景稳健性与边界分析

- order：5

- name_cn：服务场景稳健性与边界分析

- question_cn：多维峰值特征的预测优势在不同噪声、失败概率、模式幅度和模式维度下是否稳健，边界在哪里？

- inputs_and_setting_cn：4000次仿真迭代的随机参数配置；按churnWithPatternP、unexpectedChurnP、nonChurnerSeesPatternP、UB、maxMagnitude、minPatternSize分层。

- designed_or_compared_object_cn：单维与多维峰值模型在各参数切片下的平均AUROC差异；热力图展示二维交互。

- baseline_control_or_counterfactual_cn：同参数配置下的单维峰值模型。

##### objective_metrics

1. 平均AUROC

2. AUROC差

3. Welch ANOVA显著性

- analysis_method_cn：分组平均、Welch ANOVA、柱状图/折线图/热力图趋势分析。

- main_result_cn：多维模型在高失败概率、低意外流失概率、churnWithPatternP较高时优势更明显；对nonChurnerSeesPatternP不敏感；当maxMagnitude很大时单维模型提升但多维仍高约10%；minPatternSize从2升到3后单维模型下降而多维模型稳定。

- argumentative_role_cn：将“多维特征更好”从均值结论细化为“在哪些服务运营条件下更好”，同时展示方法鲁棒性。

- remaining_uncertainty_cn：这些边界只是仿真内部结论，尚未用真实顾客行为验证；也没说明具体应避免哪些失败组合。

- link_to_next_phase_cn：需要进入模型部署与可解释性阶段，用Shapley值识别关键质量子空间并给出实际使用流程。

##### evidence_pointers

1. Section 6.1-6.4

2. Figs. 8-15

#### 6. Shapley值可解释性与部署建议

- order：6

- name_cn：Shapley值可解释性与部署建议

- question_cn：流失预测模型能否同时告诉服务设计师哪些服务质量子空间最值得避免？

- inputs_and_setting_cn：一个模拟客户基；LightGBM模型；高层特征集和31维细粒度子空间特征集；测试层顾客。

- designed_or_compared_object_cn：细粒度峰值立方特征经Shapley值排序；力导向图与蜂群图展示方向和幅度。

- baseline_control_or_counterfactual_cn：文中讨论LIME作为可解释基线的不足，但未做实验对照。

##### objective_metrics

1. Shapley全局重要性I_p

2. 特征方向

- analysis_method_cn：Shapley值分解每个预测；平均绝对Shapley值作为全局特征重要性。

- main_result_cn：以<SF5,SF3>等组合为最关键的流失相关子空间；力导向图表明某顾客因经历三个二维峰值而获得高流失概率。

- argumentative_role_cn：把黑箱预测模型转成可操作的服务设计知识，回应“如何预防流失”的实践问题。

- remaining_uncertainty_cn：Shapley重要性不等同于因果重要性；没有管理人员或用户参与验证解释是否有用；部署流程只是示意。

- link_to_next_phase_cn：结论进入贡献与未来方向，把峰值立方定位为可推广到满意度设计、医疗等领域的方法。

##### evidence_pointers

1. Section 7

2. Eq. (1) and Eq. (2)

3. Figs. 16-17

## 各部分修辞架构

### abstract_moves

1. CONTEXT

2. PRIOR_KNOWLEDGE

3. LIMITATION

4. GAP

5. DESIGN_FEATURE

6. RESULT

7. CONTRIBUTION

### introduction_moves

1. CONTEXT

2. MECHANISM

3. PHENOMENON

4. PRIOR_KNOWLEDGE

5. LIMITATION

6. WHY_GAP_MATTERS

7. RQ_OR_OBJECTIVE

8. METHOD_JUSTIFICATION

9. STUDY_OVERVIEW

10. CONTRIBUTION

### theory_and_knowledge_moves

1. THEORY_INTRO

2. THEORY_PROPOSITION

3. PRIOR_KNOWLEDGE

4. MECHANISM

5. LIMITATION

6. PHENOMENON

7. BOUNDARY_CONDITION

### artifact_design_moves

1. REQUIREMENT

2. DESIGN_FEATURE

3. METHOD_JUSTIFICATION

4. LIMITATION

5. CONTRIBUTION

### evaluation_moves

1. STUDY_OVERVIEW

2. METHOD_JUSTIFICATION

3. BENCHMARK_OR_CONTRAST

4. RESULT

5. ROBUSTNESS_OR_BOUNDARY_TEST

6. MECHANISM

### discussion_and_contribution_moves

1. CONTRIBUTION

2. RESULT

3. BOUNDARY_CONDITION

4. LIMITATION_AND_FUTURE

## 理论/知识到设计的翻译

### 知识/理论基础

1. 行为经济学：峰终规则、峰值/末端效应、序列效应

2. 有界理性与满意决策（Simon）

3. 服务设计与服务科学：体验是一系列事件，结束峰点影响满意与忠诚

4. 数据库：Pareto前沿、skyline、skycube、偏好关系查询

5. 预测建模与模型可解释性：逻辑回归、LightGBM、SVM、Shapley值

6. 流失检测文献

- 理论—设计耦合：partial

- 耦合判定理由：行为经济学中的峰终规则提供了问题动机和“峰值应该重要”的核心假设，但如何把多维峰值形式化并计算，主要来自数据库skyline/skycube与偏好关系文献；预测对比来自机器学习benchmark惯例；Shapley来自博弈论解释文献。因此理论影响了目标与变量，但关键技术制品选择和实现来源是计算/数据库知识。

- 理论到设计翻译链：行为经济学命题（人类用峰/终启发式评价序列）→ 服务场景中峰值失败应导致不满/流失 → 需要捕捉多维时间序列中的峰值事件 → 用skyline定义子空间非支配事件 → 用“剔除低维峰值”语义得到真正的多维峰值 → 用PeakCube算法实现 → 提取端期特征 → 在仿真流失数据上对比单维/多维特征 → 用Shapley把模型重要性转成服务设计建议。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：人们评价一段经历时不是总加总效用，而是依赖峰值和末端（峰终规则）。

- mechanism_cn：峰值服务质量/失败会成为顾客评价的最显著线索；峰失败可能引发不满和流失。

- design_requirement_cn：DSS需要从服务质量时间序列中定位峰值事件，而不只是计算平均值。

- artifact_choice_cn：峰值立方包含所有子空间上的峰值事件；单维峰值只是其中一层。

- evaluated_contrast_cn：单维峰值特征 vs 多维峰值特征在流失预测中的AUROC。

- objective_result_cn：平均AUROC从约64%提升到约84%。

##### evidence_pointers

1. Section 2.1

2. Section 3.1

3. Section 6 Table 3

#### 2. 2

- theory_or_knowledge_claim_cn：Dixon和Verma的序列效应说明峰、端、趋势和扩散影响满意；服务设计应“结束强”。

- mechanism_cn：服务事件序列中的最后一段尤其重要；峰值发生在端期会影响流失决定。

- design_requirement_cn：特征必须覆盖“端期”而非整个体验的平均状态。

- artifact_choice_cn：构建HitsEnd、dimensionalHitsEnd、lastEncounter等端期峰值特征。

- evaluated_contrast_cn：模型采用最终服务事件中的单维/多维峰值计数。

- objective_result_cn：多维端期峰值特征显著提高流失预测。

##### evidence_pointers

1. Section 2.1 P3

2. Section 3.3

3. Section 5 P3

#### 3. 3

- theory_or_knowledge_claim_cn：Pareto最优对象是不被其他对象支配的对象；skyline用于多维偏好查询。

- mechanism_cn：在失败维度上，处于skyline的服务事件是“最差组合”的候选峰事件；但若它同时是单维峰值，流失不应归因于组合效应。

- design_requirement_cn：peak(S)应定义为skyline(S)中不属于任何更低维峰值的集合。

- artifact_choice_cn：PeakCube算法用BCD编码和过滤集实现peak(T,N)=Skyline(T,N)−FS。

- evaluated_contrast_cn：Full-space skyline与skycube无法区分“单维峰”和“组合峰”；峰值立方能区分。

- objective_result_cn：概念例子说明t12是组合峰而t5/t9不是；预测实验支持组合峰特征的价值。

##### evidence_pointers

1. Section 2.3

2. Section 3.1

3. Section 3.2

#### 4. 4

- theory_or_knowledge_claim_cn：Simon认为组织决策者是“满意”而非“最优”的，会用启发式评价过去经验。

- mechanism_cn：管理员/顾客用峰终启发式评估多维服务档案，多维峰特征应能预测后续流失决策。

- design_requirement_cn：多维峰特征可以作为流失预测自变量进入决策支持系统。

- artifact_choice_cn：从峰值立方生成特征并用于逻辑回归、LightGBM、SVM流失模型。

- evaluated_contrast_cn：包含与不包含多维峰值特征的模型比较。

- objective_result_cn：多维峰特征在所有仿真配置中显著优于单维模型。

##### evidence_pointers

1. Section 2.2 P2/P7

2. Section 5 P2

#### 5. 5

- theory_or_knowledge_claim_cn：Shapley值把合作博弈的收益公平分配给玩家，Lundberg和Lee用于解释模型预测。

- mechanism_cn：每个峰值特征被视为博弈玩家，其对流失概率的边际贡献被Shapley值加权平均。

- design_requirement_cn：在保持模型准确性的同时提供可操作解释：识别哪些失败组合最应避免。

- artifact_choice_cn：用Shapley公式计算每个峰值预测的解释力；用全局重要性I_p排序子空间。

- evaluated_contrast_cn：文中比较LIME的不足，但没有与LIME做实验对比。

- objective_result_cn：力导向图和蜂群图揭示例如<SF5,SF3>是最重要的失败组合。

##### evidence_pointers

1. Section 7.1

2. Eqs. (1)-(2)

3. Figs. 16-17

## 评价逻辑

### evaluation_modes

1. 仿真数据上的概念验证（proof of concept）

2. 有ground truth的嵌入模式恢复

3. 预测模型benchmark：单维 vs 多维特征，三类分类器，留出样本AUROC

4. 参数敏感性/稳健性分析：噪声、失败概率、模式幅度、模式最小维度

5. 可解释性评估：Shapley值、力导向图、蜂群图

- why_these_evaluations_cn：由于真实物流企业数据无法公开，作者需要在可控环境中验证“方法是否有效”。仿真可以嵌入已知多维流失模式并加入噪声，使得研究者能判断峰值立方是否找回这些模式、预测优势是否稳定，以及参数变化如何改变结论。AUROC提供标准化的预测性能比较，Shapley则回答“哪些失败组合应避免”的实践问题。

- benchmark_and_contrast_chain_cn：主线对照是“单维峰值特征 vs 多维峰值特征”。先以三类分类器在4000个客户基上做总体AUROC对比；随后沿仿真参数逐一切片，把总体差异分解到不同噪声水平、失败概率、模式幅度和模式维度；最后通过Shapley把模型内部特征贡献转化为子空间重要性的排序。这样，基准从“整体更好”逐步细化到“在什么条件下更好、为什么好、哪个子空间最该关注”。

### claim_evidence_ledger

#### 1. PeakCube算法能在百万级顾客上构建五维峰值立方。

- claim_cn：PeakCube算法能在百万级顾客上构建五维峰值立方。

- evidence_cn：400万顾客、7300万峰值、桌面多线程计算成功。

- warrant_cn：规模数据演示证明算法可扩展。

- status_cn：支持，但仅针对仿真数据。

#### 2. 多维峰值特征显著优于单维峰值特征。

- claim_cn：多维峰值特征显著优于单维峰值特征。

- evidence_cn：平均AUROC 64% vs 84%，Welch ANOVA显著；三种分类器一致。

- warrant_cn：多模型、多客户基、留出样本对比提高了内部效度。

- status_cn：在仿真环境下强支持。

#### 3. 优势来自捕捉单维视角遗漏的组合峰事件。

- claim_cn：优势来自捕捉单维视角遗漏的组合峰事件。

- evidence_cn：minPatternSize、maxMagnitude分析显示单维模型的失败机制与峰值立方优势相符；概念例子说明t12组合峰。

- warrant_cn：参数趋势与机制解释一致，但没有直接观察真实决策者的启发式。

- status_cn：间接支持。

#### 4. 在高失败概率、低意外流失、顾客对小幅多维失败敏感时，峰值立方尤其有价值。

- claim_cn：在高失败概率、低意外流失、顾客对小幅多维失败敏感时，峰值立方尤其有价值。

- evidence_cn：UB、unexpectedChurnP、maxMagnitude、minPatternSize的分层AUROC与热力图。

- warrant_cn：参数扫描形成了边界条件证据。

- status_cn：支持，但边界是仿真内部结论。

#### 5. 模型可以用Shapley值告诉服务设计师应避免的关键失败子空间。

- claim_cn：模型可以用Shapley值告诉服务设计师应避免的关键失败子空间。

- evidence_cn：全局重要性和蜂群图指出<SF5,SF3>等组合最相关。

- warrant_cn：Shapley值提供了与预测一致的逐特征贡献。

- status_cn：作为说明性部署示例，不等同于因果验证。

#### 6. 研究将峰终规则从单维扩展到多维并整合成一个新研究流。

- claim_cn：研究将峰终规则从单维扩展到多维并整合成一个新研究流。

- evidence_cn：概念框架、算法、仿真、预测实验和Shapley应用贯穿全文。

- warrant_cn：理论、制品与评价形成闭环。

- status_cn：强在理论整合，但需要后续真实数据检验。

- internal_validity_strategy_cn：在仿真中嵌入已知流失模式，作为ground truth；三种噪声参数随机化避免单一场景；4000次迭代覆盖宽参数空间；使用70/30训练测试划分；1000次迭代×4种minPatternSize形成重复实验；Welch ANOVA用于统计显著性检验。

- external_validity_strategy_cn：作者说明仿真参数借鉴真实物流企业的流失检测经验；将方法定位为适用于任何多维服务质量时间序列领域；通过公开代码允许其他研究者移植到新场景；讨论娱乐、电信、酒店和医疗等延伸领域。

- what_is_not_actually_tested_cn：真实顾客/管理者是否真的使用多维峰终启发式没有被直接观测；真实企业数据因保密未进入验证；Shapley解释对服务设计师的可用性没有用户研究；算法在更大维度数上的性能没有正式benchmark；部署流程只是示意，没有实际DSS原型评估。

## 贡献闭环

- technical_claim_cn：提出PeakCube算法，可从多维时间序列中计算所有子空间上的峰值事件，并能处理百万级顾客数据。

- artifact_claim_cn：峰值立方作为多维峰终规则的计算实现，在与单维峰值特征对比时带来约20个百分点的AUROC提升。

- mechanism_claim_cn：多维峰值特征之所以有效，是因为它捕获了同时发生在多个失败维度上的组合峰事件，而单维峰值特征无法识别这类事件。

- boundary_claim_cn：优势在高失败概率、低意外流失、顾客对小幅多维失败敏感以及模式维度不低于三维时最大；在意外流失很高或单维失败幅度极大时优势缩小，但仍保持领先。

- reusable_design_knowledge_cn：服务DSS应把“多维峰事件”作为独立的端期特征；用skysubspace与peak cube区分单维峰与组合峰；用Shapley重要性把预测模型转化为“应避免的失败组合”清单；代码公开支持复现与扩展。

- theoretical_contribution_cn：将峰终规则从单维服务体验推广到多维服务体验，提出多维峰终启发式的可操作定义，并连接行为经济学、数据库偏好查询、预测建模和服务科学，形成客户体验分析的新研究流。

- how_discussion_closes_intro_gap_cn：引言指出现有峰终研究局限于单维；讨论部分用仿真预测结果证明多维峰值模型在各类服务运营场景中普遍优于单维模型，并用Shapley把改善转成具体子空间建议，直接回应“多维性缺失”的缺口，还延伸到满意度设计、医疗等未来应用。

- overclaim_or_unsupported_leaps_cn：把仿真中人为嵌入的模式恢复和AUROC提升直接等同于“多维峰终规则的预测价值”，可能过度推广；没有证据表明现实中顾客真按这种启发式决策；Shapley重要性被表述为“should be averted”，但这是相关性而非因果性；声称“所有配置中都显著优于”基于仿真参数范围，不能覆盖全部现实配置。

## 句级写作动作图谱

### 1. P1 S1

- order：1

- section：Abstract

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：企业投入大量分析用于改善客户服务体验。

- rhetorical_function_cn：建立现实商业背景，说明分析驱动的服务体验管理是重要议题。

- depends_on_cn：无，论文开篇背景。

- sets_up_cn：为峰终规则进入讨论铺垫。

- evidence_pointer：Abstract P1 S1

### 2. P1 S2

- order：2

- section：Abstract

- locator：P1 S2

- move_code：LIMITATION

- paraphrase_cn：现有研究只在单维服务情境中检验峰终规则。

- rhetorical_function_cn：指出已有知识的边界。

- depends_on_cn：前面的峰终规则背景。

- sets_up_cn：引出本文的多维扩展。

- evidence_pointer：Abstract P1 S2

### 3. P1 S3

- order：3

- section：Abstract

- locator：P1 S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：提出峰值立方，用于标记多维服务体验档案中的突出服务水平。

- rhetorical_function_cn：给出核心制品。

- depends_on_cn：单维限制的陈述。

- sets_up_cn：说明本文要做什么。

- evidence_pointer：Abstract P1 S3

### 4. P1 S4

- order：4

- section：Abstract

- locator：P1 S4

- move_code：RESULT

- paraphrase_cn：结果显示多维峰终模型在不同服务场景中能更好预测满意度。

- rhetorical_function_cn：提前给出主要发现。

- depends_on_cn：峰值立方制品的提出。

- sets_up_cn：让读者预期实证贡献。

- evidence_pointer：Abstract P1 S4

### 5. P1 S5

- order：5

- section：Abstract

- locator：P1 S5

- move_code：DESIGN_FEATURE

- paraphrase_cn：用Shapley值识别对多维峰终启发式和顾客满意最关键的质量维度。

- rhetorical_function_cn：介绍可解释性组件。

- depends_on_cn：预测模型的存在。

- sets_up_cn：强调从预测走向设计建议。

- evidence_pointer：Abstract P1 S5

### 6. P1 S6

- order：6

- section：Abstract

- locator：P1 S6

- move_code：CONTRIBUTION

- paraphrase_cn：研究贡献和拟议方法将给决策支持系统增加多维能力并推广到服务运营和医疗等领域。

- rhetorical_function_cn：声明贡献与适用范围。

- depends_on_cn：前面的方法与结果。

- sets_up_cn：形成摘要的贡献收束。

- evidence_pointer：Abstract P1 S6

### 7. P1 S1

- order：7

- section：1. Introduction

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：服务运营中感知即现实。

- rhetorical_function_cn：用格言式背景句确立服务体验的主观性。

- depends_on_cn：无。

- sets_up_cn：为“感知影响忠诚”的机制提供起点。

- evidence_pointer：Introduction P1 S1

### 8. P1 S2

- order：8

- section：1. Introduction

- locator：P1 S2

- move_code：MECHANISM

- paraphrase_cn：顾客对服务体验的解释决定其忠诚，忠诚进而带来盈利关系。

- rhetorical_function_cn：建立体验感知影响企业结果的因果链。

- depends_on_cn：感知即现实的背景。

- sets_up_cn：解释企业为何要投资体验分析。

- evidence_pointer：Introduction P1 S2

### 9. P1 S4

- order：9

- section：1. Introduction

- locator：P1 S4

- move_code：PHENOMENON

- paraphrase_cn：保险公司通过先处理坏消息、强调正面并良好收尾来帮助护士管理病人。

- rhetorical_function_cn：用具体例子说明行为科学已进入服务实践。

- depends_on_cn：行为科学可提升满意度的一般陈述。

- sets_up_cn：为峰终规则在现实中的应用提供具体意象。

- evidence_pointer：Introduction P1 S4

### 10. P2 S1

- order：10

- section：1. Introduction

- locator：P2 S1

- move_code：GAP

- paraphrase_cn：体验心理学被视为服务科学决策支持中缺失的一环。

- rhetorical_function_cn：点出DSS文献中的空白。

- depends_on_cn：体验感知重要性的背景。

- sets_up_cn：说明新研究流可以从行为经济学出发。

- evidence_pointer：Introduction P2 S1

### 11. P2 S2

- order：11

- section：1. Introduction

- locator：P2 S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：近期研究强调峰值和末端效用决定序列评价。

- rhetorical_function_cn：引入峰终规则作为理论资源。

- depends_on_cn：体验心理学的缺口。

- sets_up_cn：为单维—多维对比提供背景。

- evidence_pointer：Introduction P2 S2

### 12. P2 S4

- order：12

- section：1. Introduction

- locator：P2 S4

- move_code：LIMITATION

- paraphrase_cn：多数先前研究在单维服务设置中进行，只在一个变量上应用峰终规则。

- rhetorical_function_cn：定义本文要突破的限制。

- depends_on_cn：峰终规则综述。

- sets_up_cn：导出单维视角忽略组合效应的后果。

- evidence_pointer：Introduction P2 S4

### 13. P2 S6

- order：13

- section：1. Introduction

- locator：P2 S6

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：如果顾客实际从若干因素组合中获得效用，单维视角无法发现这一点。

- rhetorical_function_cn：说明单维限制不仅方法上欠完备，而且会导致实质性盲区。

- depends_on_cn：单维研究限制的陈述。

- sets_up_cn：论证多维峰终规则的必要性。

- evidence_pointer：Introduction P2 S6

### 14. P2 S8

- order：14

- section：1. Introduction

- locator：P2 S8

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文研究企业如何以多维方式应用峰终规则。

- rhetorical_function_cn：提出核心研究目标。

- depends_on_cn：多维性缺口的论述。

- sets_up_cn：引出峰值立方方法。

- evidence_pointer：Introduction P2 S8

### 15. P3 S1

- order：15

- section：1. Introduction

- locator：P3 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：提出计算“峰值立方”的方法，该构造包含不同质量变量子集对应的所有显著服务水平。

- rhetorical_function_cn：给出核心艺术品。

- depends_on_cn：多维峰终规则的目标。

- sets_up_cn：为后续算法和实验说明提供定义对象。

- evidence_pointer：Introduction P3 S1

### 16. P3 S2

- order：16

- section：1. Introduction

- locator：P3 S2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：为检验峰值立方贡献，将其特征集成到监控顾客不满的决策支持系统中，以帮助预防无合同场景下的流失。

- rhetorical_function_cn：预告评价场景。

- depends_on_cn：峰值立方制的提出。

- sets_up_cn：让读者知道本文用流失预测来体现价值。

- evidence_pointer：Introduction P3 S2

### 17. P3 S3

- order：17

- section：1. Introduction

- locator：P3 S3

- move_code：RESULT

- paraphrase_cn：结果显示在若干服务运营场景中峰值立方显著改善早期流失检测。

- rhetorical_function_cn：提前报告核心结果。

- depends_on_cn：前面预告的DSS应用。

- sets_up_cn：建立实证贡献的预期。

- evidence_pointer：Introduction P3 S3

### 18. P4 S1

- order：18

- section：1. Introduction

- locator：P4 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：选择物流作为应用领域是因为这是作者实际开展工作的领域。

- rhetorical_function_cn：解释领域选择的理由。

- depends_on_cn：先前企业合作经验的暗示。

- sets_up_cn：为后面说明保密限制和仿真替代做铺垫。

- evidence_pointer：Introduction P4 S1

### 19. P4 S5

- order：19

- section：1. Introduction

- locator：P4 S5

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：由于保密协议，无法展示企业数据细节，因此用可比仿真数据展示峰值立方价值。

- rhetorical_function_cn：解释为何采用仿真作为主要证据来源。

- depends_on_cn：作者有真实企业经验但数据受限。

- sets_up_cn：为第4节仿真设计提供合法性。

- evidence_pointer：Introduction P4 S5

### 20. P5 S1-P5 S5

- order：20

- section：1. Introduction

- locator：P5 S1-P5 S5

- move_code：CONTRIBUTION

- paraphrase_cn：列出五点贡献：实现峰值立方方法、可学习峰值立方并公开代码、预测模型超越单维模型、Shapley识别关键质量维度、整合多个学科形成新研究流。

- rhetorical_function_cn：提前声明贡献清单。

- depends_on_cn：全文方法。

- sets_up_cn：给出阅读期望与评价标准。

- evidence_pointer：Introduction P5 S1-S5

### 21. P6 S1

- order：21

- section：1. Introduction

- locator：P6 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：概述后续各节安排：理论背景、模型、算法、仿真、预测模型、讨论、部署和结论。

- rhetorical_function_cn：提供论文结构路标。

- depends_on_cn：前面的贡献声明。

- sets_up_cn：引导读者按序阅读。

- evidence_pointer：Introduction P6 S1

### 22. P1 S1

- order：22

- section：2.1 Behavioral economics and service design

- locator：P1 S1

- move_code：THEORY_INTRO

- paraphrase_cn：行为经济学把人视为有界理性、使用启发式并做满意决策的个体。

- rhetorical_function_cn：引入行为经济学的底层假设。

- depends_on_cn：前面峰终规则的预告。

- sets_up_cn：解释为什么序列评价会偏离总效用。

- evidence_pointer：Section 2.1 P1 S1

### 23. P1 S2

- order：23

- section：2.1 Behavioral economics and service design

- locator：P1 S2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：与理性人加总各事件效用不同，人会用峰值和末端效用等启发式评价序列。

- rhetorical_function_cn：陈述峰终规则的核心命题。

- depends_on_cn：有界理性假设。

- sets_up_cn：为服务设计应用提供行为学基础。

- evidence_pointer：Section 2.1 P1 S2

### 24. P2 S2

- order：24

- section：2.1 Behavioral economics and service design

- locator：P2 S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：学者们开始用峰终规则和体验曲线斜率等发现指导服务设计。

- rhetorical_function_cn：展示已有研究如何转化行为理论。

- depends_on_cn：峰终规则命题。

- sets_up_cn：为本文从服务设计视角扩展做准备。

- evidence_pointer：Section 2.1 P2 S2

### 25. P3 S1

- order：25

- section：2.1 Behavioral economics and service design

- locator：P3 S1

- move_code：THEORY_INTRO

- paraphrase_cn：Dixon和Verma归纳出服务设计师应关注的四种序列效应。

- rhetorical_function_cn：引入更细的序列效应框架。

- depends_on_cn：峰终规则综述。

- sets_up_cn：用峰、扩展、趋势、末端效应补充本文“端期”特征的合理性。

- evidence_pointer：Section 2.1 P3 S1

### 26. P5 S1

- order：26

- section：2.1 Behavioral economics and service design

- locator：P5 S1

- move_code：LIMITATION

- paraphrase_cn：该研究流的关键限制是集中于单维服务水平或聚合效用。

- rhetorical_function_cn：点明文献边界。

- depends_on_cn：前面服务的峰终/序列效应综述。

- sets_up_cn：引出多维服务情境。

- evidence_pointer：Section 2.1 P5 S1

### 27. P2 S1

- order：27

- section：2.2 Motivating example

- locator：P2 S1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：作者假设满意决策的管理者会采用峰终启发式评价服务质量。

- rhetorical_function_cn：把行为理论具体化为本文的假设起点。

- depends_on_cn：Simon的满意决策观点。

- sets_up_cn：使“多维峰失败导致流失”变得可研究。

- evidence_pointer：Section 2.2 P2 S1

### 28. P2 S2

- order：28

- section：2.2 Motivating example

- locator：P2 S2

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：假设服务失败峰值会决定顾客不满，并可能在无合同情况下导致流失。

- rhetorical_function_cn：提出可检验的核心假设。

- depends_on_cn：峰终启发式假设。

- sets_up_cn：把流失预测作为评价窗口。

- evidence_pointer：Section 2.2 P2 S2

### 29. P6 S3

- order：29

- section：2.2 Motivating example

- locator：P6 S3

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：如果顾客在第12次事件后流失，可归因于多维峰终效应，而传统单维分析会忽略这一点。

- rhetorical_function_cn：用实例说明单维视角会错过流失原因。

- depends_on_cn：损坏与丢失包裹的双维时间序列例子。

- sets_up_cn：为峰值立方在服务运营中的作用提供直观理由。

- evidence_pointer：Section 2.2 P6 S3

### 30. P7 S1

- order：30

- section：2.2 Motivating example

- locator：P7 S1

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：作者明确不主张SME管理员确实使用这种决策捷径。

- rhetorical_function_cn：防止理论假设被误解为实证事实。

- depends_on_cn：组织决策中的理性/行为争论。

- sets_up_cn：为后面“如果采用启发式则特征有贡献”的条件性命题做限定。

- evidence_pointer：Section 2.2 P7 S1

### 31. P8 S1

- order：31

- section：2.2 Motivating example

- locator：P8 S1

- move_code：LIMITATION

- paraphrase_cn：顾客也可以把不同失败换算成统一单位用单维峰评价，但这不抵消多维峰特征的贡献。

- rhetorical_function_cn：处理一个常见的替代解释。

- depends_on_cn：多维峰价值的动机论述。

- sets_up_cn：用不可换算性和不可量化损失来捍卫多维视角。

- evidence_pointer：Section 2.2 P8 S1

### 32. P1 S1

- order：32

- section：2.3 Pareto frontiers in databases

- locator：P1 S1

- move_code：THEORY_INTRO

- paraphrase_cn：Pareto最优对象是指不被数据中其他对象支配的对象。

- rhetorical_function_cn：引入数据库skyline的理论基础。

- depends_on_cn：前面的多维峰值问题。

- sets_up_cn：为用skyline计算服务水平提供定义。

- evidence_pointer：Section 2.3 P1 S1

### 33. P2 S2

- order：33

- section：2.3 Pareto frontiers in databases

- locator：P2 S2

- move_code：PHENOMENON

- paraphrase_cn：用巴哈马旅行中寻找廉价且近海滩酒店的经典例子解释skyline算子。

- rhetorical_function_cn：通过日常类比降低理解成本。

- depends_on_cn：Pareto最优定义。

- sets_up_cn：引导读者理解服务水平上的skyline。

- evidence_pointer：Section 2.3 P2 S2

### 34. P3 S1

- order：34

- section：2.3 Pareto frontiers in databases

- locator：P3 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：skyline传统上用小于号定义支配，而峰效应场景改用大于号。

- rhetorical_function_cn：将数据库概念转化为服务失败峰值的适用形式。

- depends_on_cn：skyline定义。

- sets_up_cn：为service failures skyline图2b做铺垫。

- evidence_pointer：Section 2.3 P3 S1

### 35. P1 S1

- order：35

- section：3. Peak cube

- locator：P1 S1

- move_code：LIMITATION

- paraphrase_cn：全空间skyline和skycube都不足以完全捕捉多维峰效应。

- rhetorical_function_cn：指出数据库现有制品的概念不足。

- depends_on_cn：skyline/skycube介绍。

- sets_up_cn：引出峰值立方的新颖性。

- evidence_pointer：Section 3 P1 S1

### 36. P1 S2

- order：36

- section：3.1 A peak cube model

- locator：P1 S2

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：在流失场景中，顾客可能不仅因单维峰值流失，还可能因失败类型的组合峰值流失。

- rhetorical_function_cn：将多维峰终规则转化为流失预测假设。

- depends_on_cn：三维失败子空间讨论。

- sets_up_cn：定义各类子空间的峰。

- evidence_pointer：Section 3.1 P1 S2

### 37. P4 S1

- order：37

- section：3.1 A peak cube model

- locator：P4 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：peak(S)定义为skyline(S)中不属于任何S真子空间峰值的服务事件集合。

- rhetorical_function_cn：给出峰值立方的核心操作定义。

- depends_on_cn：对t5/t9与t7/t12语义差异的分析。

- sets_up_cn：为PeakCube算法和特征工程奠定形式基础。

- evidence_pointer：Section 3.1 P4 S1

### 38. P1 S3

- order：38

- section：3.2 Computing the peak cube of service experience

- locator：P1 S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：峰值立方定义为服务失败空间所有子空间上的完整多维失败峰值集合。

- rhetorical_function_cn：正式定义峰值立方。

- depends_on_cn：前面的peak(S)定义。

- sets_up_cn：说明算法输入输出和用途。

- evidence_pointer：Section 3.2 P1 S3

### 39. P2 S1

- order：39

- section：3.2 Computing the peak cube of service experience

- locator：P2 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：算法受skycube预计算和数据库偏好关系的代数演算启发，采用自底向上方法。

- rhetorical_function_cn：解释算法来源和设计取向。

- depends_on_cn：skycube文献。

- sets_up_cn：为Fig.4算法细节提供依据。

- evidence_pointer：Section 3.2 P2 S1

### 40. P3 S2

- order：40

- section：3.2 Computing the peak cube of service experience

- locator：P3 S2

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：Pareto优化用例中相关维度通常为2到5，因为计算成本随维度指数上升。

- rhetorical_function_cn：说明方法适用维度边界。

- depends_on_cn：维度扩展带来的计算挑战。

- sets_up_cn：解释为什么仿真使用五个失败维度。

- evidence_pointer：Section 3.2 P3 S2

### 41. P5 S1

- order：41

- section：3.3 Feature engineering with peak cubes

- locator：P5 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：所有特征类既可在端期计算，也可在整个服务期内计算。

- rhetorical_function_cn：说明特征族的可扩展性。

- depends_on_cn：前面的三类特征。

- sets_up_cn：为模型可选用不同特征窗口做铺垫。

- evidence_pointer：Section 3.3 P5 S1

### 42. P2 S2

- order：42

- section：4. Simulating customer bases and service failure time series

- locator：P2 S2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：仿真适合本目标，因为要检验多维数据比单维数据带来潜在优势，且可证明方法有效。

- rhetorical_function_cn：回应“为什么不用真实数据”的潜在质疑。

- depends_on_cn：真实物流数据保密限制。

- sets_up_cn：为仿真模块设计提供方法学正当性。

- evidence_pointer：Section 4 P2 S2

### 43. P3 bullet 3

- order：43

- section：4. Simulating customer bases and service failure time series

- locator：P3 bullet 3

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：预期使用峰值立方特征的流失模型会优于只考虑单维峰值的模型；结果还将证明算法能发现嵌入模式、能抵抗噪声、对关键输入稳健，且增益可显著。

- rhetorical_function_cn：把仿真目标陈述为可验证的命题。

- depends_on_cn：嵌入流失模式的仿真设计。

- sets_up_cn：为第5、6节的结果做预期引导。

- evidence_pointer：Section 4 P3 bullet 3

### 44. P1 S3

- order：44

- section：4.1 The CreateEmbeddedPatterns module

- locator：P1 S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：模块建立低、中、高三个失败regime，并随机分配服务质量维度到这些regime。

- rhetorical_function_cn：使仿真贴近现实中某些失败更频繁的特征。

- depends_on_cn：现实物流中late比lost常见。

- sets_up_cn：为各维度设置非零失败概率提供机制。

- evidence_pointer：Section 4.1 P1 S3

### 45. P3 S2

- order：45

- section：4.1 The CreateEmbeddedPatterns module

- locator：P3 S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：nPattern、minPatternSize和maxMagnitude共同决定嵌入的流失失败模式。

- rhetorical_function_cn：说明仿真关键参数的含义。

- depends_on_cn：需要制造有已知多维特征的模式。

- sets_up_cn：用于后续参数敏感性分析。

- evidence_pointer：Section 4.1 P3 S2

### 46. P4 S4

- order：46

- section：4.1 The CreateEmbeddedPatterns module

- locator：P4 S4

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：minPatternSize和maxMagnitude允许比较不同场景下多维与单维峰终规则的预测价值。

- rhetorical_function_cn：把仿真参数设计为后续对照条件。

- depends_on_cn：嵌入模式参数的设定。

- sets_up_cn：为第6.3和6.4的对比实验做铺垫。

- evidence_pointer：Section 4.1 P4 S4

### 47. P1 S1

- order：47

- section：4.2 The NonChurnServiceFailures module

- locator：P1 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：该模块模拟普通服务事件，并确保其失败维度小于可能致流失的模式维度。

- rhetorical_function_cn：构造无流失顾客的“非峰”对照背景。

- depends_on_cn：嵌入流失模式的定义。

- sets_up_cn：使流失信号与普通失败重叠可控。

- evidence_pointer：Section 4.2 P1 S1

### 48. P2 S1

- order：48

- section：4.3 The CreateCustomers module

- locator：P2 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：引入三种噪声：流失者按模式流失的概率、非流失者意外流失的概率、非流失者看到流失模式的概率。

- rhetorical_function_cn：让仿真更接近真实世界的模糊信号。

- depends_on_cn：基础流失生成逻辑。

- sets_up_cn：为第6.1的噪声分析提供变量。

- evidence_pointer：Section 4.3 P2 S1

### 49. P5 S3

- order：49

- section：4.3 The CreateCustomers module

- locator：P5 S3

- move_code：RESULT

- paraphrase_cn：4000次迭代产生近十亿个服务失败值，即2.6亿个五维服务事件。

- rhetorical_function_cn：用规模数据增强方法可信度。

- depends_on_cn：仿真模块参数设定。

- sets_up_cn：为第5节大规模峰值立方计算提供输入。

- evidence_pointer：Section 4.3 P5 S3

### 50. P1 S1

- order：50

- section：5. Peak cubes and defection detection models

- locator：P1 S1

- move_code：RESULT

- paraphrase_cn：对400万顾客分别运行PeakCube算法，构建400万个峰值立方，产生约7300万个服务失败峰值。

- rhetorical_function_cn：报告峰值立方在大规模仿真数据上的计算成功。

- depends_on_cn：仿真生成的顾客基。

- sets_up_cn：为特征提取和模型训练提供数据基础。

- evidence_pointer：Section 5 P1 S1

### 51. P2 S1

- order：51

- section：5. Peak cubes and defection detection models

- locator：P2 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：研究目标是预测顾客在评估多维纵向服务档案后的流失决定。

- rhetorical_function_cn：澄清本章预测任务的核心问题。

- depends_on_cn：峰值立方特征已经生成。

- sets_up_cn：连接Simon启发式假设与流失预测模型。

- evidence_pointer：Section 5 P2 S1

### 52. P3 S1

- order：52

- section：5. Peak cubes and defection detection models

- locator：P3 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：先用高层峰值立方特征建模，第7节再用更细粒度的子空间特征识别关键质量子空间。

- rhetorical_function_cn：预告本章与第7节的分工。

- depends_on_cn：特征工程与模型开始。

- sets_up_cn：为第7节可解释性分析做结构铺垫。

- evidence_pointer：Section 5 P3 S1

### 53. P4 S1

- order：53

- section：5. Peak cubes and defection detection models

- locator：P4 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：选择逻辑回归、梯度提升树和SVM是因为它们在流失检测研究和实践中被广泛使用。

- rhetorical_function_cn：说明分类器选择依据。

- depends_on_cn：流失预测文献。

- sets_up_cn：保证结果不是某个单一算法偶然造成。

- evidence_pointer：Section 5 P4 S1

### 54. P4 S5

- order：54

- section：5. Peak cubes and defection detection models

- locator：P4 S5

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：LightGBM通过GOSS和EFB显著提升梯度提升树的效率与规模。

- rhetorical_function_cn：解释为什么在多变特征场景选择LightGBM。

- depends_on_cn：峰值立方特征可能指数化增多。

- sets_up_cn：为第7节细粒度31维特征模型提供技术保障。

- evidence_pointer：Section 5 P4 S5

### 55. P5 S2

- order：55

- section：5. Peak cubes and defection detection models

- locator：P5 S2

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：第一组模型用单维峰值数预测流失，第二组模型用多维峰值数预测流失。

- rhetorical_function_cn：建立本研究的直接对照实验。

- depends_on_cn：高层特征向量。

- sets_up_cn：为AUROC比较提供基础。

- evidence_pointer：Section 5 P5 S2

### 56. P6 S1

- order：56

- section：5. Peak cubes and defection detection models

- locator：P6 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：每个客户基用70%数据训练、30%留出样本计算AUROC。

- rhetorical_function_cn：说明预测性能评估协议。

- depends_on_cn：单维vs多维对照设计。

- sets_up_cn：为第6节统计结果提供可信度量。

- evidence_pointer：Section 5 P6 S1

### 57. P1 S2

- order：57

- section：6. Predictive performance in different service operations scenarios

- locator：P1 S2

- move_code：RESULT

- paraphrase_cn：Welch ANOVA显示多维峰特征带来显著性能提升，逻辑回归平均AUC从64%升至84%。

- rhetorical_function_cn：给出核心统计结论。

- depends_on_cn：24000个模型的AUROC。

- sets_up_cn：为后续参数分解提供总览。

- evidence_pointer：Section 6 P1 S2-S3

### 58. P2 S1

- order：58

- section：6. Predictive performance in different service operations scenarios

- locator：P2 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：下一步按服务运营场景分解预测性能。

- rhetorical_function_cn：预告稳健性分析。

- depends_on_cn：总体显著提升结果。

- sets_up_cn：引出噪声、UB、maxMagnitude、minPatternSize分析。

- evidence_pointer：Section 6 P2 S1

### 59. P5 S2

- order：59

- section：6.1 Predictive performance and noise parameters

- locator：P5 S2

- move_code：RESULT

- paraphrase_cn：随着意外流失概率上升，单维和多维模型都下降，但多维模型下降更多。

- rhetorical_function_cn：报告噪声对效果的影响方向。

- depends_on_cn：unexpectedChurnP的定义。

- sets_up_cn：说明多维优势在高意外流失时收缩。

- evidence_pointer：Section 6.1 Fig. 9

### 60. P2 S1

- order：60

- section：6.2 Service failures probabilities

- locator：P2 S1

- move_code：RESULT

- paraphrase_cn：多维模型AUROC保持在80%以上，而单维模型随失败概率上升而下降。

- rhetorical_function_cn：揭示失败概率是调节因素。

- depends_on_cn：UB参数定义。

- sets_up_cn：说明峰值立方在高失败概率场景尤其有价值。

- evidence_pointer：Section 6.2 Fig. 11

### 61. P2 S1

- order：61

- section：6.3 Maximum magnitude of service failures in embedded churn patterns

- locator：P2 S1

- move_code：RESULT

- paraphrase_cn：单维模型性能随maxMagnitude增大而改善，但多维模型始终高于80%，即使无幅度限制时多维仍高出约10%。

- rhetorical_function_cn：报告幅度条件对单维模型的补偿作用但不足以追平多维。

- depends_on_cn：maxMagnitude参数设置。

- sets_up_cn：论证小幅多维失败也可能触发流失。

- evidence_pointer：Section 6.3 Fig. 13

### 62. P2 S4

- order：62

- section：6.4 Minimum cardinality of embedded churn patterns

- locator：P2 S4

- move_code：RESULT

- paraphrase_cn：多维模型对流失模式最小维度不敏感，单维模型在minPatternSize大于2后性能下降。

- rhetorical_function_cn：报告模式维度边界的核心结果。

- depends_on_cn：minPatternSize参数。

- sets_up_cn：为机制解释提供现象。

- evidence_pointer：Section 6.4 Fig. 15

### 63. P3 S1

- order：63

- section：6.4 Minimum cardinality of embedded churn patterns

- locator：P3 S1

- move_code：MECHANISM

- paraphrase_cn：单维模型的下降源于维度增加后普通事件与流失模式中非零失败的重叠，使单维峰难以唯一标记流失事件。

- rhetorical_function_cn：解释参数效应背后的机制。

- depends_on_cn：minPatternSize结果。

- sets_up_cn：强化多维峰值的理论必要性。

- evidence_pointer：Section 6.4 P3 S1

### 64. P1 S1

- order：64

- section：7. Model deployment and practical implications

- locator：P1 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：服务公司可在流失检测DSS中纳入峰值立方及相应特征集。

- rhetorical_function_cn：从研究转向部署流程。

- depends_on_cn：第5节的预测模型。

- sets_up_cn：描述实际使用步骤。

- evidence_pointer：Section 7 P1 S1

### 65. P2 S1

- order：65

- section：7. Model deployment and practical implications

- locator：P2 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：流失预测模型能否同时告诉服务设计师哪些质量子空间最关键？

- rhetorical_function_cn：提出可解释性研究问题。

- depends_on_cn：部署框架已经给出。

- sets_up_cn：引入Shapley值分析。

- evidence_pointer：Section 7 P2 S1

### 66. P2 S1

- order：66

- section：7.1 Multidimensional peaks importance

- locator：P2 S1

- move_code：THEORY_INTRO

- paraphrase_cn：Shapley值方法源于合作博弈论，把模型预测视为博弈收益并公平分配给各特征。

- rhetorical_function_cn：引入解释模型的理论工具。

- depends_on_cn：需要解释黑箱模型。

- sets_up_cn：给出公式(1)和(2)的意义。

- evidence_pointer：Section 7.1 P2 S1

### 67. P4 S1

- order：67

- section：7.1 Multidimensional peaks importance

- locator：P4 S1

- move_code：CONTRIBUTION

- paraphrase_cn：Shapley贡献有两方面：解释单个顾客的流失概率，并识别重要多维峰值特征。

- rhetorical_function_cn：把可解释性分析定位为设计知识。

- depends_on_cn：Shapley值机制。

- sets_up_cn：为力导向图和全局重要性结果做铺垫。

- evidence_pointer：Section 7.1 P4 S1

### 68. P5 S5

- order：68

- section：7.1 Multidimensional peaks importance

- locator：P5 S5

- move_code：RESULT

- paraphrase_cn：力导向图表明某流失顾客因经历三个二维峰值而获得较高流失概率。

- rhetorical_function_cn：展示Shapley局部解释的实例。

- depends_on_cn：高层特征LightGBM模型。

- sets_up_cn：说明解释可用于单个顾客。

- evidence_pointer：Section 7.1 P5 S5, Fig. 16

### 69. P6 S2

- order：69

- section：7.1 Multidimensional peaks importance

- locator：P6 S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：细粒度特征集包含顾客在最后一次服务事件是否经历某个子空间峰值的31个布尔特征。

- rhetorical_function_cn：说明细粒度建模的输入。

- depends_on_cn：峰值立方子空间编码。

- sets_up_cn：为全局特征重要性排序提供输入。

- evidence_pointer：Section 7.1 P6 S2

### 70. P7 S1

- order：70

- section：7.1 Multidimensional peaks importance

- locator：P7 S1

- move_code：RESULT

- paraphrase_cn：按全局Shapley重要性排序后，<SF5,SF3>成为最重要的失败子空间。

- rhetorical_function_cn：输出可直接用于服务设计的排序结果。

- depends_on_cn：细粒度模型和Shapley值计算。

- sets_up_cn：作为“应避免哪些组合”的答案。

- evidence_pointer：Section 7.1 P7 S1, Fig. 17

### 71. P8 S5

- order：71

- section：7.1 Multidimensional peaks importance

- locator：P8 S5

- move_code：RESULT

- paraphrase_cn：蜂群图中的红色长尾表示某些顾客在特定子空间峰值上风险极高。

- rhetorical_function_cn：强调异质性：组合峰对部分顾客格外重要。

- depends_on_cn：蜂群图的可视化。

- sets_up_cn：为个性化服务设计建议提供理由。

- evidence_pointer：Section 7.1 P8 S5, Fig. 17

### 72. P1 S5

- order：72

- section：8. Research contributions and future directions

- locator：P1 S5

- move_code：RESULT

- paraphrase_cn：多维峰终模型在所有仿真服务配置中显著优于单维模型。

- rhetorical_function_cn：总结全文核心实证结论。

- depends_on_cn：第6节参数分解结果。

- sets_up_cn：支撑贡献声明。

- evidence_pointer：Section 8 P1 S5

### 73. P1 S6

- order：73

- section：8. Research contributions and future directions

- locator：P1 S6

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：峰值立方尤其在高失败概率和顾客对小幅多维失败敏感时有用。

- rhetorical_function_cn：限定核心贡献的适用条件。

- depends_on_cn：UB、maxMagnitude分析。

- sets_up_cn：避免把结论过度推广到所有服务场景。

- evidence_pointer：Section 8 P1 S6

### 74. P3 S1-S2

- order：74

- section：8. Research contributions and future directions

- locator：P3 S1-S2

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：研究受限于仿真数据和真实物流企业数据的保密性，但仿真数据是真实数据的近似替代。

- rhetorical_function_cn：坦诚证据来源限制。

- depends_on_cn：真实数据缺位的背景。

- sets_up_cn：为后续用其他行业真实数据验证留出空间。

- evidence_pointer：Section 8 P3 S1-S2

### 75. P4 S2

- order：75

- section：8. Research contributions and future directions

- locator：P4 S2

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：未来可将峰值立方用于最大化顾客满意度以及研究序列效应，而不只用于流失预测。

- rhetorical_function_cn：扩展理论应用范围。

- depends_on_cn：本文以流失为焦点。

- sets_up_cn：说明方法不限于不满/流失。

- evidence_pointer：Section 8 P4 S2

### 76. P5 S2

- order：76

- section：8. Research contributions and future directions

- locator：P5 S2

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：医疗领域中的多维生命体征时间序列是峰值立方的重要未来应用。

- rhetorical_function_cn：用跨领域应用增加方法的一般性。

- depends_on_cn：多维时间序列+因变量的普遍条件。

- sets_up_cn：收束全文，说明更广价值。

- evidence_pointer：Section 8 P5 S2

## 写作技术

- gap_construction_cn：先用行为经济学确立峰终规则的重要性，再指出几乎所有已有研究都只在单维服务水平上实施该规则；然后用B2B物流的双维失败例子展示单维视角会漏掉组合峰事件，从而把缺口从“没有人做”升级为“现有做法会错过真实流失原因”。

- signposting_cn：引言末尾用“论文结构如下”预告各节；第5节预告第7节会更细粒度；第6节开头说“接下来按场景分解”；第7节开头用“除了流失检测，模型能否还告诉设计师…”引导可解释性部分。

- transition_logic_cn：每阶段以“尚未解决的问题”驱动过渡：概念需仿真验证→仿真需预测模型检验→总体效果需参数分解→预测结果需可解释性转化为设计知识。段间常用“然而”“因此”“为了…”等连接。

- claim_evidence_rhythm_cn：论文遵循“先给总体AUROC显著提升，再逐参数下降解释”的节奏：每小节先说明参数含义，再报告Fig.的趋势，再做机制解释，最后用一句“说明其在某场景的重要价值”把结果提升为贡献。

- benchmark_narrative_cn：基准不是单一数据集，而是嵌入已知流失模式的仿真数据；单维峰值特征作为天然baseline，三个分类器交叉验证，holdout AUROC作为共同尺度；后续参数分层把benchmark从“有优势”细化为“在哪些条件下优势更明显”。

- theory_return_cn：结果不仅用于支持制品，还回扣Simon的满意决策假设和峰终规则：参数分析中minPatternSize的重叠解释、端点特征设计、Shapley识别关键子空间，都让实证结果回到“评价过去体验的启发式影响决策”的理论框架。

- contribution_positioning_cn：把峰值立方定位为行为经济学、数据库skyline、预测建模与服务科学的交叉，而不是单纯算法改进；同时公开代码，使贡献超越一次性结果，成为可复用的研究基础设施。

- novelty_protection_cn：通过四个策略防止贡献退化为一次性性能结果：用参数扫描证明不是单点现象；用“单维vs多维”的语义差异解释为什么改进发生；用Shapley产出可直接行动的设计清单；用医疗等跨领域应用展示概念的一般性。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：以现实服务运营中的感知-忠诚关系开篇，建立“服务体验需要被量化分析”的语境。

- research_job_cn：识别一个可观察的管理问题，如流失检测；积累一个具体行业例子。

- required_evidence_cn：能说明服务体验影响商业结果的经验证据或企业案例。

- transition_to_next_cn：引入行为经济学中的峰终规则来解释为什么体验序列会被简化评价。

#### 2. 2

- step：2

- writing_job_cn：综述既有峰终规则和序列效应文献，明确指出单维视角的限制。

- research_job_cn：系统回顾行为经济学、服务设计与DSS文献，提炼未解决缺口。

- required_evidence_cn：多篇文献表明现有研究只在单维或聚合效用上应用峰终规则。

- transition_to_next_cn：用具体业务例子说明单维视角会漏掉多维组合峰，形成WHY_GAP_MATTERS。

#### 3. 3

- step：3

- writing_job_cn：呈现一个带时间序列的动机性示例（如损坏+丢失包裹），展示多维峰值事件。

- research_job_cn：构造或找到真实/仿真的双维时间序列，指出传统方法无法识别的关键事件。

- required_evidence_cn：能清楚展示“t12是首个同时发生两个失败的峰值事件”这类图示。

- transition_to_next_cn：提出需要一种能计算所有子空间峰值的构造。

#### 4. 4

- step：4

- writing_job_cn：定义制品（峰值立方）并给出算法和特征族。

- research_job_cn：从相关计算领域（数据库skyline/skycube）借力，形式化制品的操作定义，实现算法。

- required_evidence_cn：能区分全空间skyline、skycube与峰值立方；算法可运行且有代码。

- transition_to_next_cn：说明需要用数据检验制品是否有效。

#### 5. 5

- step：5

- writing_job_cn：设计并描述仿真/实验环境，包括嵌入已知信号和噪声。

- research_job_cn：开发带ground truth的数据生成机制；确保参数覆盖多种场景；说明与真实背景的对应关系。

- required_evidence_cn：仿真能生成大规模数据，且嵌入模式可被后续算法找回。

- transition_to_next_cn：进入预测模型与基准对比。

#### 6. 6

- step：6

- writing_job_cn：报告基准结果：原有特征 vs 新特征，多个分类器、多个参数配置。

- research_job_cn：建立训练/测试协议，计算标准指标如AUROC；进行统计检验和参数分层。

- required_evidence_cn：至少一个关键指标上存在稳健且可重复的改善。

- transition_to_next_cn：从“性能更好”进入“何时更好、为什么更好”。

#### 7. 7

- step：7

- writing_job_cn：用可解释性方法（如Shapley）把模型输出转化为设计建议。

- research_job_cn：选择合适的解释框架，计算特征重要性，展示单个案例与全局排序。

- required_evidence_cn：关键特征与领域知识一致，且能指导实践。

- transition_to_next_cn：收束贡献并扩展到其他领域。

#### 8. 8

- step：8

- writing_job_cn：讨论贡献、边界、局限与未来方向；公开代码。

- research_job_cn：明确哪些结论来自仿真/条件实验，哪些尚未验证；提供后续研究路线。

- required_evidence_cn：诚实的限制说明和可复现代码。

- transition_to_next_cn：无，论文结束。

### most_transferable_moves_cn

1. 用理论确定“什么变量重要”后，从相邻计算领域借用可计算定义

2. 用简洁的双维时间序列例子展示单维方法的盲区

3. 仿真中嵌入已知模式并加噪声，使方法是否有用可被检验

4. 用“原有特征 vs 新特征”作为主干对照，而不是只报告新模型性能

5. 用参数分层回答边界条件，而不是停留于单一平均效果

6. 用可解释性组件把黑箱结果转成管理者能用的建议

### resource_intensive_or_nonstandard_parts_cn

1. 多年真实物流企业合作和对约20万SME流失建模的经验

2. 受保密协议保护的真实企业数据无法公开

3. 大规模仿真生成400万顾客、2.6亿服务事件的计算成本

4. 对400万顾客运行PeakCube算法并建立24000个预测模型

5. 需要领域知识判断哪些失败类型进入仿真维度

### what_not_to_copy_superficially_cn

1. 不能在没有嵌入已知多维流失模式或真实流失数据的情况下宣称多维峰特征有效

2. 不能把模拟数据的AUROC提升直接等同于真实管理行为中的峰终启发式

3. 不能把Shapley重要性说成因果“应避免”，除非有干预或准实验证据

4. 不能省略噪声和参数扫描，否则无法说明边界条件

5. 不能只靠概念定义而不提供算法和代码，否则失去可复现性

- single_best_description_of_the_routine_cn：先借行为经济学指出单维峰终规则的缺口，再用数据库skyline/skycube方法把多维峰值概念化为可计算的峰值立方，构造带嵌入模式与噪声的大规模仿真，用24,000个模型对比单维/多维特征，最后用Shapley值把黑箱结果转成服务设计建议。

## 分析边界

原文PDF提取中第7节编号在摘要文本显示为‘97’，但结合上下文和目录应指§7；图2-17以图片嵌入，无法从文本中读取具体数据标签，只能根据正文描述判断；附录和电子伴侣（GitHub代码）未包含在提供的全文内；没有真实企业数据细节；无页码范围。
