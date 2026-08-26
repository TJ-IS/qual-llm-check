# ROLEX: A Novel Method for Interpretable Machine Learning Using Robust Local Explanations

- 作者：Buomsoo (Raymond) Kim; Karthik Srinivasan; Sung Hye Kong; Jung Hee Kim; Chan Soo Shin; Sudha Ram
- 年份 / 期刊：2023 / MIS Quarterly
- DOI：10.25300/misq/2022/17141
- 源文件：05780_2023_rolex-a-novel-method-for-interpretable-machine-learning-using-robust-local-explanations.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：performance_gap_artifact_benchmark_generalize
- 置信度：0.85

## 文章级论证概况

- 核心问题：如何为医疗预测分析中的黑箱机器学习模型生成稳健、实例级、模型无关且局部忠实的解释，并将其转化为临床可用、可建立信任的界面？

- 制品与设计：ROLEX方法包含三阶段：在合成数据生成阶段，用训练集中最近的异类点作为固定参考点，在其与目标实例之间插值得到采样中心，并直接优化采样中心位置与半径，替代LIME的全局高斯采样和LS/LEAP的随机enemy point与统一epsilon；随后用SMOTE处理局部样本不平衡；在局部模型拟合阶段，用LinSep分数判断局部决策边界是否近似线性，从而选择线性或非线性局部模型，并提出LDA评价框架来排除远离决策边界的同质样本；在患者级解释阶段，开发包含文本说明、局部系数、局部规则和可视化图形的交互式原型UI。

- 客观结果：在乳腺癌、心脏病和脆性骨折三个数据集以及RF、ADA、MLP、XGB、CB五种黑箱模型上，ROLEX的local fidelity和LDA-fidelity均一致高于LIME、LS、LEAP等基准；敏感性分析验证LDA框架比标准fidelity更可靠；消融研究表明SMOTE贡献最大，直接优化其次，非线性解释仅在决策边界非线性时重要；专家访谈显示原型UI有助于沟通、个性化护理和缓解信息不对称。

- 核心贡献：作者声称的贡献包括：提出XAI设计框架，指导真实世界HPA中可解释系统的设计；提出ROLEX方法，提升局部模型无关解释的局部忠实性与可解释性；提出LDA局部解释评价框架，处理远离决策边界的边缘情况并给出何时适合使用局部解释的启发；开发ROLEX原型UI并用医疗专家用户研究验证其满足XAI多重需求。

- 整篇论证链：文章从HPA模型因黑箱而缺乏信任、难以落地的现实问题出发，把问题收窄到现有局部解释方法在局部忠实性上的不足：LIME采样不够局部，LS的enemy point不稳定且统一半径不适用，LEAP的局部嵌入学习在真实数据上无效，同时现有方法忽视远离决策边界的同质样本和局部决策边界非线性。作者先给出一个以情境相关性、伦理安全、法规公共利益为中心的XAI框架，再据此设计ROLEX：用固定训练集异类近邻和直接优化取代启发式采样，用SMOTE处理样本不平衡，用LinSep分数决定线性/非线性局部模型，用LDA框架修正评价指标。随后在三个医疗数据集和多个黑箱预测模型上，以局部忠实性和LDA-fidelity为主线，逐步检验ROLEX相对LIME/LS/LEAP的优势，并通过敏感性分析、消融实验和复杂度实验说明优势来源与边界。最后用脆性骨折患者实例和专家访谈展示解释如何转化为患者级临床知识，再在讨论中把结果接回HPA信任、个性化医疗、信息不对称和设计科学贡献。

## 类型与写作弧线判定

- 论文主类型判定：文章的核心是构建一个新设计制品ROLEX，并在真实医疗数据和原型UI场景中评价它；同时提出XAI框架和LDA评价框架，以设计原则、原型、评价循环的方式形成设计知识，符合设计科学研究范式。

- 主导写作弧线判定：论证主线是：现有局部解释方法存在性能缺口（局部忠实性不足、评价不可靠、无可用UI）→ 构建ROLEX制品 → 用多个数据集和基准方法进行benchmark → 通过消融和边界分析把性能优势一般化为可复用设计知识。

## 研究开展程序

- study_or_phase_count：9

- 研究阶段总序列：先做概念需求分析和XAI框架构建，再进行ROLEX方法设计；然后训练黑箱预测模型，为解释评价提供被解释对象；接着在多个数据集上比较解释方法并检验LDA边缘情况；再通过敏感性分析、消融实验和复杂度实验解释优越性来源；最后用原型UI实例和专家访谈展示实际可用性与临床意义。各阶段从建立设计需求到验证技术性能，再到解释机制和外部相关性，逐级累积证据。

### studies_or_phases

#### 1. XAI框架与需求分析

- order：1

- name_cn：XAI框架与需求分析

- question_cn：设计真实世界HPA可解释系统应满足哪些一般性要求？

- inputs_and_setting_cn：XAI、HPA、设计科学、伦理与法规文献，以及医疗AI应用场景

- designed_or_compared_object_cn：XAI三要求框架和解释方法分类法

- baseline_control_or_counterfactual_cn：无，属于概念综合

##### objective_metrics

（空）

- analysis_method_cn：文献综合、概念分类、设计原则提炼

- main_result_cn：提出情境相关性、伦理安全、法规与公共利益三个核心要求；用范围与模型特异性两个维度划分解释方法

- argumentative_role_cn：建立全文设计要求和贡献定位，说明ROLEX为何需要模型无关、局部、可解释且带UI

- remaining_uncertainty_cn：没有说明这些要求如何被形式化检验

- link_to_next_phase_cn：把要求转化为ROLEX方法的具体设计目标

##### evidence_pointers

1. Theory and Motivation: XAI Framework for Practical Applications

2. Table 1

3. Figure 1

#### 2. ROLEX方法设计

- order：2

- name_cn：ROLEX方法设计

- question_cn：如何通过改进采样、局部建模和评价机制修复现有局部解释方法的缺陷？

- inputs_and_setting_cn：LIME、LS、LEAP等扰动采样方法，以及文中的合成示例图3-7

- designed_or_compared_object_cn：ROLEX的采样方案、LinSep模型选择、LDA评价框架、多模态UI

- baseline_control_or_counterfactual_cn：概念上与LIME/LS/LEAP的启发式采样和统一参数对比

##### objective_metrics

（空）

- analysis_method_cn：算法设计与形式化目标函数；利用现有方法局限进行推理

- main_result_cn：定义了直接优化采样中心和半径的鲁棒局部解释方法，加入SMOTE和线性/非线性选择，并提出LDA-fidelity评价

- argumentative_role_cn：提供待评价的核心设计制品

- remaining_uncertainty_cn：尚未证明这些设计确实提升局部忠实性

- link_to_next_phase_cn：需要真实数据和黑箱预测模型来检验方法

##### evidence_pointers

1. Proposed Method section

2. Equations (1)-(8)

3. Algorithm 1

4. Figures 3-7

#### 3. 黑箱预测模型训练

- order：3

- name_cn：黑箱预测模型训练

- question_cn：在三个医疗数据集上，哪些分类模型适合作为被解释的黑箱模型？

- inputs_and_setting_cn：乳腺癌、心脏病、脆性骨折三个数据集；DT/DRL两种可解释模型与RF/ADA/MLP/XGB/CB五种黑箱模型

- designed_or_compared_object_cn：不同预测算法的性能

- baseline_control_or_counterfactual_cn：DT和DRL作为可解释基线

##### objective_metrics

1. AUC

2. ACC

3. bACC

- analysis_method_cn：五折交叉验证调参，训练集/测试集80:20划分，报告测试性能

- main_result_cn：XGB和CB在表格数据上总体性能较好，MLP和RF也有竞争力；可解释基线明显较弱

- argumentative_role_cn：生成被解释对象，也为后续ROLEX评价提供不同决策边界形态的黑箱模型

- remaining_uncertainty_cn：这里只关心预测性能，尚未涉及解释质量

- link_to_next_phase_cn：下一阶段为这些训练好的模型生成局部解释并比较忠实性

##### evidence_pointers

1. Analysis: Evaluation of Machine Learning Algorithms

2. Table 3

3. Appendix A

#### 4. 局部解释评价与LDA边缘情况分析

- order：4

- name_cn：局部解释评价与LDA边缘情况分析

- question_cn：ROLEX是否比LIME、LS、LEAP更局部忠实？LDA框架揭示了多少现有方法会失效的边缘情况？

- inputs_and_setting_cn：三个数据集、五个黑箱模型、测试实例、局部解释模型

- designed_or_compared_object_cn：ROLEX与LIME/LS/LEAP生成的局部解释

- baseline_control_or_counterfactual_cn：LIME、LS、LEAP，且基线经过网格搜索最优超参数

##### objective_metrics

1. Local fidelity

2. LDA-fidelity

- analysis_method_cn：固定采样数量与测试半径，用bACC计算忠实度；用网格搜索为基线选最优超参数；报告边缘情况频数

- main_result_cn：ROLEX在几乎所有数据集/模型组合上同时提高local fidelity与LDA-fidelity；LDA框架显示大量同质样本或非线性DB边缘情况，尤其XGB在脆性骨折数据上64%实例非线性DB

- argumentative_role_cn：核心性能证据，说明ROLEX优于现状且LDA评价更严格

- remaining_uncertainty_cn：未说明性能提升来自哪个具体设计成分

- link_to_next_phase_cn：用敏感性分析验证LDA框架的必要性，再用消融实验拆解ROLEX成分

##### evidence_pointers

1. Table 4

2. Table 5

3. Figure 8

#### 5. LDA框架敏感性验证

- order：5

- name_cn：LDA框架敏感性验证

- question_cn：为什么标准fidelity对远离决策边界的实例失效？LDA的排除策略是否合理？

- inputs_and_setting_cn：测试集实例彼此距离，以及局部解释在最近和最远实例上的fidelity

- designed_or_compared_object_cn：同质样本实例（Case 1）与异质样本实例（Case 2/3）

- baseline_control_or_counterfactual_cn：标准local fidelity与LDA-fidelity的对比，以及s(x_i^N)与s(x_i^F)的fidelity对比

##### objective_metrics

1. Average fidelity

2. Performance decline (%)

- analysis_method_cn：计算每个实例到最近/最远测试实例的距离，用邻近和遥远的解释分别计算fidelity并比较下降幅度

- main_result_cn：同质样本实例的近远解释fidelity几乎无差别，异质样本实例下降20%到36%；说明标准fidelity对同质实例不敏感，LDA框架更有效

- argumentative_role_cn：为LDA评价框架提供机制证据

- remaining_uncertainty_cn：仅在五个算法的组合上描述性分析，没有推断检验

- link_to_next_phase_cn：为消融实验提供动机：解释模型训练中的样本不平衡需要修复

##### evidence_pointers

1. Analysis: Evaluation of Local Explanations

2. Table 6

#### 6. 消融实验

- order：6

- name_cn：消融实验

- question_cn：ROLEX的各个设计成分分别对性能提升有多大贡献？

- inputs_and_setting_cn：脆性骨折数据集与五个黑箱模型；ROLEX完整版与三种去除版本；加SMOTE的基线版本

- designed_or_compared_object_cn：无贝叶斯优化、无SMOTE、无非线性解释三种变体；以及LIME+SMOTE、LS+SMOTE、LEAP+SMOTE

- baseline_control_or_counterfactual_cn：完整ROLEX与原始基线

##### objective_metrics

1. Average fidelity

- analysis_method_cn：逐一移除核心组件，比较fidelity下降；给基线添加SMOTE检验组件推广性

- main_result_cn：去除SMOTE导致最大下降，说明样本不平衡是关键问题；去除贝叶斯优化也明显下降；去除非线性解释只在XGB上明显下降；加SMOTE能提升LIME和LS，但ROLEX仍最好

- argumentative_role_cn：把ROLEX的总体优势归因到具体设计机制，防止整体性能被解释为偶然

- remaining_uncertainty_cn：消融只在脆性骨折数据上正式报告，其他数据集未逐一报告

- link_to_next_phase_cn：由于非线性解释只在特定情况下有用，需要进一步实验平衡复杂性与可解释性

##### evidence_pointers

1. Analysis: Evaluation of Local Explanations

2. Table 7

3. Appendix C

#### 7. 忠实性-复杂度权衡实验

- order：7

- name_cn：忠实性-复杂度权衡实验

- question_cn：局部决策树解释的复杂度应设为多少，才能在忠实性与人类可解释性之间取得平衡？

- inputs_and_setting_cn：XGB黑箱模型在脆性骨折数据上的局部解释；决策树最大叶节点数2到20

- designed_or_compared_object_cn：不同叶节点数的局部决策树

- baseline_control_or_counterfactual_cn：以叶节点数变化作为自身对照

##### objective_metrics

1. Average local fidelity

- analysis_method_cn：扫描最大叶节点数，观察fidelity曲线

- main_result_cn：fidelity随复杂度上升但约10个叶节点后进入平台，因此选择10作为默认复杂度上限

- argumentative_role_cn：说明ROLEX在追求忠实性的同时保留可解释性，回应可解释性要求

- remaining_uncertainty_cn：该阈值依赖数据集

- link_to_next_phase_cn：该复杂度设置被用于原型UI中的局部规则展示

##### evidence_pointers

1. Analysis: Evaluation of Local Explanations

2. Figure 9

#### 8. 原型UI与患者级解释演示

- order：8

- name_cn：原型UI与患者级解释演示

- question_cn：ROLEX生成的局部解释如何以患者级界面呈现，并支持医学知识发现？

- inputs_and_setting_cn：脆性骨折队列数据集、CB分类器、患者#283的局部解释

- designed_or_compared_object_cn：原型UI中的患者档案、文本说明、局部系数、局部规则、可视化和散点图

- baseline_control_or_counterfactual_cn：无直接对照；用全局平均效应与局部解释进行对比

##### objective_metrics

（空）

- analysis_method_cn：协作式案例分析：与医疗专家共同解释患者#283的局部特征和规则

- main_result_cn：患者的局部解释显示体脂、饮酒频率、泌尿症状等特征与骨折风险关联；其中体脂正相关与文献平均效应矛盾，专家认为可能源于患者亚组异质性，展示了局部解释发现新知识的能力

- argumentative_role_cn：把抽象方法转成可参与、可解释的界面，展示实践价值

- remaining_uncertainty_cn：单一患者案例，无法泛化；没有测量临床结果改进

- link_to_next_phase_cn：用专家访谈评估该UI是否满足XAI框架中的三类要求

##### evidence_pointers

1. Analysis: Patient-Level Explanations and Local Interpretations

2. Figures 10-14

3. Table 8

#### 9. 医疗专家定性评价

- order：9

- name_cn：医疗专家定性评价

- question_cn：领域专家如何看待ROLEX方法及原型的临床价值？

- inputs_and_setting_cn：四名韩国医疗保健专家（三名医生和一名移动医疗公司CEO）的30分钟非结构访谈

- designed_or_compared_object_cn：ROLEX原型界面

- baseline_control_or_counterfactual_cn：无对照组，采用归纳编码

##### objective_metrics

1. 编码频次

- analysis_method_cn：非结构访谈、录音转写、归纳法编码，并将编码映射到XAI框架三要求

- main_result_cn：专家认为ROLEX最有价值之处是帮助与公众沟通、提供个性化护理、增强信任、解决信息不对称、提升公平问责；编码频次集中在沟通和个性化护理

- argumentative_role_cn：为UI与XAI框架提供外部相关性和人工可用性的初步证据

- remaining_uncertainty_cn：样本量小、访谈非结构化、无定量结果，不能作为严格的临床有效性证据

- link_to_next_phase_cn：无需下一阶段，直接进入讨论与未来研究

##### evidence_pointers

1. Analysis: Expert Interviews

2. Table 9

## 各部分修辞架构

### abstract_moves

1. CONTEXT

2. PRACTICAL_STAKES

3. PHENOMENON

4. RQ_OR_OBJECTIVE

5. DESIGN_FEATURE

6. BENCHMARK_OR_CONTRAST

7. RESULT

8. CONTRIBUTION

### introduction_moves

1. CONTEXT

2. PRIOR_KNOWLEDGE

3. LIMITATION

4. PRACTICAL_STAKES

5. REQUIREMENT

6. RQ_OR_OBJECTIVE

7. DESIGN_FEATURE

8. MECHANISM

9. WHY_GAP_MATTERS

10. STUDY_OVERVIEW

11. RESULT

12. CONTRIBUTION

### theory_and_knowledge_moves

1. REQUIREMENT

2. PRIOR_KNOWLEDGE

3. MECHANISM

4. LIMITATION

5. GAP

6. DESIGN_FEATURE

### artifact_design_moves

1. REQUIREMENT

2. PRIOR_KNOWLEDGE

3. LIMITATION

4. DESIGN_FEATURE

5. MECHANISM

6. BOUNDARY_CONDITION

7. STUDY_OVERVIEW

8. METHOD_JUSTIFICATION

### evaluation_moves

1. BENCHMARK_OR_CONTRAST

2. METHOD_JUSTIFICATION

3. RESULT

4. ROBUSTNESS_OR_BOUNDARY_TEST

### discussion_and_contribution_moves

1. CONTRIBUTION

2. BOUNDARY_CONDITION

3. LIMITATION_AND_FUTURE

## 理论/知识到设计的翻译

### 知识/理论基础

1. XAI三要求框架（情境相关性、伦理安全、法规与公共利益）

2. 局部模型无关解释方法：LIME、LS、LEAP

3. 局部忠实性定义与局部决策边界几何

4. 设计科学中的制品、原型与逆向设计思想

5. 交互式机器学习与可解释UI原则

6. 医疗领域脆性骨折与骨密度知识

- 理论—设计耦合：partial

- 耦合判定理由：XAI框架与设计科学原则主要影响问题定位、界面设计和贡献框架，但ROLEX核心技术选择（固定训练集近邻、直接优化采样参数、SMOTE、LinSep阈值、LDA排除同质样本）来自对现有扰动采样算法局限的工程性修补和实证观察，而不是由正式理论演绎得出。

- 理论到设计翻译链：XAI三要求 → 需要模型无关、局部、可解释、带UI的解释机制；扰动采样几何知识 → 采样中心与半径需靠近局部DB且因实例而异；局部DB非线性与样本不平衡 → 用LinSep选择线性/非线性局部模型并用SMOTE纠正；同质邻域使标准fidelity失真 → 提出LDA框架排除远离DB的实例；交互式ML原则 → 将解释转化为文本、系数、规则和可视化并开发原型UI。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：XAI系统应满足情境相关性、伦理安全、法规与公共利益三类要求

- mechanism_cn：解释只有在用户可理解、能沟通系统局限、并符合利益相关者价值时才被信任和使用

- design_requirement_cn：解释必须患者级、人类可解释、能表达不确定性并面向多方利益

- artifact_choice_cn：ROLEX原型UI包含患者档案、文本说明、局部系数、局部规则和散点图

- evaluated_contrast_cn：专家访谈中不同需求维度的编码频次

- objective_result_cn：专家认为UI最有助于与公众沟通、个性化护理和解决信息不对称

##### evidence_pointers

1. Table 1

2. Table 9

3. Figures 10-14

#### 2. 2

- theory_or_knowledge_claim_cn：靠近局部决策边界采样能提高局部忠实性，但随机enemy point和共享采样半径不稳定

- mechanism_cn：采样点若远离实例或偏离局部DB，局部模型会拟合错误区域；固定参考点和按实例优化半径可减少偏差

- design_requirement_cn：每个实例应有稳定的采样中心和适当的个性化采样半径

- artifact_choice_cn：ROLEX使用训练集中最近异类点插值得到中心，并直接优化beta和epsilon

- evaluated_contrast_cn：ROLEX与LIME/LS/LEAP的fidelity和LDA-fidelity对比

- objective_result_cn：ROLEX在多数组合上显著更高

##### evidence_pointers

1. Equations (4)-(6)

2. Table 5

#### 3. 3

- theory_or_knowledge_claim_cn：局部DB可能非线性，且多数方法默认线性

- mechanism_cn：在非线性DB周围均匀采样会产生严重类别不平衡，线性解释模型无法忠实刻画局部边界

- design_requirement_cn：需要判断局部线性程度，并支持非线性可解释模型与不平衡修正

- artifact_choice_cn：引入LinSep分数；高于0.8用线性模型，否则用DT/GAM；并用SMOTE过采样少数类

- evaluated_contrast_cn：消融实验移除SMOTE、移除非线性解释、给基线加SMOTE

- objective_result_cn：SMOTE贡献最大；非线性解释只在XGB等低LinSep场景重要；加SMOTE增强基线但ROLEX仍领先

##### evidence_pointers

1. Table 7

2. Appendix C

#### 4. 4

- theory_or_knowledge_claim_cn：远离决策边界的实例邻域同质，标准fidelity会虚高

- mechanism_cn：同质测试样本使所有局部模型都能平凡地获得高准确率，从而无法区分真正局部的解释

- design_requirement_cn：评价指标应只关注对决策敏感、样本异质的实例

- artifact_choice_cn：LDA框架先检测同质/异质样本，再计算LDA-fidelity

- evaluated_contrast_cn：同质实例与异质实例的近邻/远邻解释fidelity下降比较

- objective_result_cn：同质实例几乎没有下降，异质实例下降20%-36%

##### evidence_pointers

1. Algorithm 1

2. Table 6

#### 5. 5

- theory_or_knowledge_claim_cn：忠实性与人类可解释性存在权衡

- mechanism_cn：越复杂的局部模型越能拟合非线性DB，但叶子节点或规则过多会超出人类理解能力

- design_requirement_cn：在保证可用解释性的前提下最大化忠实性

- artifact_choice_cn：限制局部决策树最大叶节点数为10

- evaluated_contrast_cn：叶节点数2到20的忠实性曲线

- objective_result_cn：约10个叶节点后忠实性进入平台

##### evidence_pointers

1. Figure 9

## 评价逻辑

### evaluation_modes

1. 多数据集多黑箱模型benchmark对比（fidelity与LDA-fidelity）

2. LDA边缘情况统计（同质样本、非线性DB）

3. 邻近/远邻解释敏感性分析

4. 消融实验与基线增强实验

5. 复杂度-忠实性权衡实验

6. 原型UI演示与医疗专家访谈的定性评价

- why_these_evaluations_cn：方法主张涉及技术性能、设计成分贡献、评价框架有效性和实践可用性，单一benchmark无法同时回答这些问题。因此先用基准比较证明ROLEX总体更好，再用敏感性分析证明评价标准本身更可靠，用消融实验把性能优势归因到具体设计，用复杂度实验说明可解释性边界，最后用专家访谈把技术性能连接到真实用户价值。

- benchmark_and_contrast_chain_cn：先训练多个预测模型建立被解释对象，再用LDA框架统计每个模型和数据集上的边缘情况，说明旧指标会失效；随后在同样的数据/模型组合上比较ROLEX与LIME/LS/LEAP，并同时报告标准fidelity和LDA-fidelity；LDA-fidelity作为更严格指标排除了同质样本的虚高。敏感性分析进一步支持LDA排除策略。消融实验在基线上添加/删除ROLEX成分，证明不是整体调参红利。复杂度实验为UI中的规则模型选择提供量化依据。最后专家访谈把评价从数值指标扩展到临床沟通与信任。

### claim_evidence_ledger

#### 1. ROLEX比现有基准更局部忠实

- claim_cn：ROLEX比现有基准更局部忠实

- evidence_cn：三个数据集、五个黑箱模型上的fidelity和LDA-fidelity均一致更高（Table 5）

- support_level：强支持

#### 2. LDA框架能处理标准指标失效问题

- claim_cn：LDA框架能处理标准指标失效问题

- evidence_cn：Table 4显示边缘情况普遍；Table 6显示同质实例近远解释fidelity几乎无差异

- support_level：强支持但描述性

#### 3. ROLEX的改进来自SMOTE、直接优化和非线性解释等组件

- claim_cn：ROLEX的改进来自SMOTE、直接优化和非线性解释等组件

- evidence_cn：Table 7消融：去除SMOTE下降最大，去除优化明显下降，去除非线性解释仅在XGB明显；Appendix C显示给基线加SMOTE后仍不如ROLEX

- support_level：中等支持，主要在脆性骨折数据上正式报告

#### 4. 原型UI满足XAI框架并能改善临床决策

- claim_cn：原型UI满足XAI框架并能改善临床决策

- evidence_cn：专家访谈归纳编码，沟通与个性化护理频次最高（Table 9）

- support_level：弱到中等支持：样本量小、非结构访谈、无临床结果指标

#### 5. 局部解释能发现全局解释看不到的医学知识

- claim_cn：局部解释能发现全局解释看不到的医学知识

- evidence_cn：患者#283的体脂与骨折风险正相关与文献平均效应矛盾，专家给出异质性解释（Figure 12-14）

- support_level：弱支持：单案例、事后方言

- internal_validity_strategy_cn：使用多个公开数据集和一个真实队列；设置固定的训练/测试划分；用五折交叉验证训练黑箱模型；基准方法经过网格搜索最优超参数；同一采样数量与测试半径；同时使用标准fidelity和LDA-fidelity；通过消融和敏感性分析排除替代解释。

- external_validity_strategy_cn：利用两个广泛使用的公开医疗数据集和一个真实纵向前瞻性队列；覆盖多种预测模型；邀请实际医疗专家进行访谈；将XAI框架定位为可推广到其他领域的设计知识。

- what_is_not_actually_tested_cn：没有随机化用户实验或临床结果指标；没有评估解释与真实因果机制的ground truth一致性；没有检验对抗攻击和分布漂移下的鲁棒性；没有将ROLEX推广到其他领域、多分类或回归任务；LDA-fidelity的测试半径仍依赖启发式设置。

## 贡献闭环

- technical_claim_cn：ROLEX在局部忠实性和LDA-fidelity上优于LIME、LS、LEAP，且无需大量超参数调优或启发式搜索。

- artifact_claim_cn：直接优化采样中心与半径、SMOTE过采样、基于LinSep的线性/非线性模型选择共同构成ROLEX的性能优势。

- mechanism_claim_cn：现有方法失败是因为随机/次优enemy point、统一采样半径、局部样本不平衡、局部DB非线性和远离DB的同质邻域会导致局部解释模型失真；ROLEX分别针对这些机制进行修复。

- boundary_claim_cn：ROLEX的优势在局部DB非线性或样本不平衡时最明显；当局部DB高度线性时非线性解释收益有限；远离决策边界的实例即使fidelity高也可能信息量少，应谨慎使用局部解释。

- reusable_design_knowledge_cn：提供XAI三要求框架、LinSep线性可分性分数、LDA评价框架、以及关于忠实性-复杂度权衡和交互式UI的设计原则，可迁移到其他XAI系统设计。

- theoretical_contribution_cn：把局部解释重新概念化为对复杂制品的逆向设计；将XAI与HPA信任、信息不对称、个性化医疗和设计科学连接起来，扩展了医疗IS中的可解释制品研究。

- how_discussion_closes_intro_gap_cn：引言提出HPA模型因黑箱而缺乏信任和落地；讨论部分说明ROLEX通过提供局部忠实、患者级、可交互的解释，能够提升医生和患者信任，暴露系统不完备性，支持个性化护理，并缓解医患信息不对称，从而回到最初缺口。

- overclaim_or_unsupported_leaps_cn：论文多次使用“有潜力”而非实证效果；专家访谈被用作外部价值证据，但访谈是定性的、样本量小且无对照；从局部解释的数值忠实性跳跃到改善临床决策和患者安全，缺少真实决策任务中的因果证据；单案例中的医学发现也被赋予较多知识发现分量。

## 句级写作动作图谱

### 1. Abstract P1 S1

- order：1

- section：Abstract

- locator：Abstract P1 S1

- move_code：CONTEXT

- paraphrase_cn：大数据技术的近期发展正使医疗预测分析能用复杂模型研究难题。

- rhetorical_function_cn：开场建立技术背景

- depends_on_cn：无需前文

- sets_up_cn：为后续黑箱模型与信任问题做铺垫

- evidence_pointer：Abstract第一句

### 2. Abstract P1 S2

- order：2

- section：Abstract

- locator：Abstract P1 S2

- move_code：PRACTICAL_STAKES

- paraphrase_cn：但医疗从业者因黑箱结构透明度和问责不足而不愿采用这些模型。

- rhetorical_function_cn：指出现实后果

- depends_on_cn：依赖上一句的模型能力

- sets_up_cn：引出对解释的需求

- evidence_pointer：Abstract第二句

### 3. Abstract P1 S3

- order：3

- section：Abstract

- locator：Abstract P1 S3

- move_code：PHENOMENON

- paraphrase_cn：作者相信实例级局部解释能提升患者安全并促进信任，因为它允许患者层面解释和医学知识发现。

- rhetorical_function_cn：给出作者的核心信念

- depends_on_cn：由信任问题自然引出

- sets_up_cn：把局部解释立为解决方案

- evidence_pointer：Abstract第三句

### 4. Abstract P1 S4

- order：4

- section：Abstract

- locator：Abstract P1 S4

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：因此研究提出ROLEX方法，为HPA模型生成稳健的实例级解释。

- rhetorical_function_cn：点明全文目标

- depends_on_cn：前一句的信念

- sets_up_cn：引出方法名称

- evidence_pointer：Abstract第四句

### 5. Abstract P1 S5

- order：5

- section：Abstract

- locator：Abstract P1 S5

- move_code：DESIGN_FEATURE

- paraphrase_cn：ROLEX改编最新方法并改善它们在解释黑箱模型个体预测上的不足。

- rhetorical_function_cn：初步描述制品定位

- depends_on_cn：上一句目标

- sets_up_cn：暗示与LIME/LS/LEAP的比较

- evidence_pointer：Abstract第五句

### 6. Abstract P1 S6

- order：6

- section：Abstract

- locator：Abstract P1 S6

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：用脆性骨折大型真实数据和两个公开医疗数据集分析，显示ROLEX在局部忠实性上优于广泛接受的基准方法。

- rhetorical_function_cn：预告评价方法与结果

- depends_on_cn：方法提出之后

- sets_up_cn：为摘要中的结果贡献提供证据

- evidence_pointer：Abstract第六句

### 7. Abstract P1 S7

- order：7

- section：Abstract

- locator：Abstract P1 S7

- move_code：RESULT

- paraphrase_cn：ROLEX更稳健，因为不依赖大量超参数调优或启发式算法。

- rhetorical_function_cn：附加鲁棒性主张

- depends_on_cn：结果句

- sets_up_cn：区分ROLEX与基准的技术哲学

- evidence_pointer：Abstract第七句

### 8. Abstract P1 S8

- order：8

- section：Abstract

- locator：Abstract P1 S8

- move_code：CONTRIBUTION

- paraphrase_cn：ROLEX生成解释和原型UI有可能促进个性化护理和精准医学。

- rhetorical_function_cn：把技术结果转为实践贡献

- depends_on_cn：前序结果

- sets_up_cn：引向理论/设计科学含义

- evidence_pointer：Abstract第八句

### 9. Introduction P1 S1

- order：9

- section：Introduction

- locator：Introduction P1 S1

- move_code：CONTEXT

- paraphrase_cn：大数据技术和大型数据集使HPA在IS学科中受到极大关注。

- rhetorical_function_cn：建立学科背景

- depends_on_cn：摘要语境

- sets_up_cn：为已有研究回顾铺垫

- evidence_pointer：Introduction P1 S1

### 10. Introduction P1 S2

- order：10

- section：Introduction

- locator：Introduction P1 S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：已有IS研究提出预测患者再入院和异常吸入器使用等结果的方法。

- rhetorical_function_cn：展示领域已有成果

- depends_on_cn：上一句背景

- sets_up_cn：对比实践落地的不足

- evidence_pointer：Introduction P1 S2

### 11. Introduction P1 S3

- order：11

- section：Introduction

- locator：Introduction P1 S3

- move_code：LIMITATION

- paraphrase_cn：但许多HPA系统因缺乏信任而未被实际采用。

- rhetorical_function_cn：指出现状缺口

- depends_on_cn：先陈述已有预测能力

- sets_up_cn：把信任作为关键问题

- evidence_pointer：Introduction P1 S3

### 12. Introduction P1 S4

- order：12

- section：Introduction

- locator：Introduction P1 S4

- move_code：REQUIREMENT

- paraphrase_cn：获得信任的重要一步是为预测提供可靠解释，这对临床决策和患者安全至关重要。

- rhetorical_function_cn：把解释提升为核心设计要求

- depends_on_cn：信任缺口

- sets_up_cn：引入解释技术

- evidence_pointer：Introduction P1 S4

### 13. Introduction P1 S5

- order：13

- section：Introduction

- locator：Introduction P1 S5

- move_code：PRACTICAL_STAKES

- paraphrase_cn：盲目接受黑箱结果可能带来不希望甚至危及生命的后果。

- rhetorical_function_cn：强化现实风险

- depends_on_cn：信任问题

- sets_up_cn：为方法必要性提供道德权重

- evidence_pointer：Introduction P1 S5

### 14. Introduction P2 S1

- order：14

- section：Introduction

- locator：Introduction P2 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本研究提出增强HPA模型透明度和问责性的方法，即ROLEX。

- rhetorical_function_cn：首次完整陈述研究目标

- depends_on_cn：前段信任/风险论证

- sets_up_cn：详细描述方法特征

- evidence_pointer：Introduction P2 S1

### 15. Introduction P2 S2

- order：15

- section：Introduction

- locator：Introduction P2 S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：ROLEX可为任意分类模型生成模型无关的局部解释。

- rhetorical_function_cn：给出核心技术定位

- depends_on_cn：目标句

- sets_up_cn：解释模型无关与局部两个属性

- evidence_pointer：Introduction P2 S2

### 16. Introduction P2 S3

- order：16

- section：Introduction

- locator：Introduction P2 S3

- move_code：LIMITATION

- paraphrase_cn：现有HPA解释研究只针对特定模型如神经网络或树集成，不符合HPA中多样化数据集和模型的最新趋势。

- rhetorical_function_cn：构造文献缺口

- depends_on_cn：已有解释方法综述

- sets_up_cn：论证模型无关必要性

- evidence_pointer：Introduction P2 S3

### 17. Introduction P2 S4

- order：17

- section：Introduction

- locator：Introduction P2 S4

- move_code：MECHANISM

- paraphrase_cn：HPA常出现复杂非线性关系和跨观测异质效应，因此仅用全局解释不够。

- rhetorical_function_cn：解释局部解释为什么必要

- depends_on_cn：模型无关缺口

- sets_up_cn：引入局部解释概念

- evidence_pointer：Introduction P2 S4

### 18. Introduction P2 S5

- order：18

- section：Introduction

- locator：Introduction P2 S5

- move_code：REQUIREMENT

- paraphrase_cn：局部解释是患者级解释，可促进个性化护理与精准医学。

- rhetorical_function_cn：把局部解释转化为医疗价值

- depends_on_cn：异质性机制

- sets_up_cn：为ROLEX的局部分析目标铺垫

- evidence_pointer：Introduction P2 S5

### 19. Introduction P2 S6

- order：19

- section：Introduction

- locator：Introduction P2 S6

- move_code：DESIGN_FEATURE

- paraphrase_cn：ROLEX通过改进采样和新的优化方案来生成比现有方法更局部忠实的解释。

- rhetorical_function_cn：描述技术机制

- depends_on_cn：局部解释定位

- sets_up_cn：预告采样与优化是贡献重点

- evidence_pointer：Introduction P2 S6

### 20. Introduction P2 S7

- order：20

- section：Introduction

- locator：Introduction P2 S7

- move_code：DESIGN_FEATURE

- paraphrase_cn：作者还开发了包含多种人类可理解的病人级解释模式的ROLEX原型界面。

- rhetorical_function_cn：引入UI部分

- depends_on_cn：方法本身

- sets_up_cn：后续原型演示与专家研究

- evidence_pointer：Introduction P2 S7

### 21. Introduction P3 S1

- order：21

- section：Introduction

- locator：Introduction P3 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：用多个HPA数据集评估ROLEX，包括队列研究数据与两个公开数据集。

- rhetorical_function_cn：预告研究材料

- depends_on_cn：方法提出

- sets_up_cn：为评价结果铺垫

- evidence_pointer：Introduction P3 S1

### 22. Introduction P3 S2

- order：22

- section：Introduction

- locator：Introduction P3 S2

- move_code：RESULT

- paraphrase_cn：ROLEX在局部忠实性上持续优于最新解释方法。

- rhetorical_function_cn：早期预告核心结论

- depends_on_cn：研究设计

- sets_up_cn：引导读者接受贡献

- evidence_pointer：Introduction P3 S2

### 23. Introduction P3 S3

- order：23

- section：Introduction

- locator：Introduction P3 S3

- move_code：PHENOMENON

- paraphrase_cn：研究聚焦脆性骨折这一真实HPA场景。

- rhetorical_function_cn：选择具体应用领域

- depends_on_cn：方法需要真实问题

- sets_up_cn：随后描述脆性骨折为何需要局部解释

- evidence_pointer：Introduction P3 S3

### 24. Introduction P3 S4

- order：24

- section：Introduction

- locator：Introduction P3 S4

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：脆性骨折患者发病和风险因素高度异质，因此是需要局部解释的代表性HPA问题。

- rhetorical_function_cn：说明问题为何适合本文方法

- depends_on_cn：场景选择

- sets_up_cn：后续患者#283分析

- evidence_pointer：Introduction P3 S4

### 25. Introduction P3 S5

- order：25

- section：Introduction

- locator：Introduction P3 S5

- move_code：STUDY_OVERVIEW

- paraphrase_cn：作者用有经验的医疗专家用户研究展示ROLEX原型有潜力改善临床决策和解决信息不对称。

- rhetorical_function_cn：预告定性评价

- depends_on_cn：原型开发

- sets_up_cn：为贡献清单中的用户研究埋伏笔

- evidence_pointer：Introduction P3 S5

### 26. Introduction Contributions 第1条

- order：26

- section：Introduction

- locator：Introduction Contributions 第1条

- move_code：CONTRIBUTION

- paraphrase_cn：贡献之一是提出XAI框架，指导真实世界HPA可解释系统设计。

- rhetorical_function_cn：定位理论/设计贡献

- depends_on_cn：前文框架分析

- sets_up_cn：把本文绑定到设计科学知识

- evidence_pointer：Introduction Contributions (1)

### 27. Introduction Contributions 第2条

- order：27

- section：Introduction

- locator：Introduction Contributions 第2条

- move_code：CONTRIBUTION

- paraphrase_cn：贡献之二是提出解释任何黑箱模型个体预测的新方法，提升局部忠实性与可解释性。

- rhetorical_function_cn：声明方法贡献

- depends_on_cn：ROLEX设计

- sets_up_cn：后续benchmark证据

- evidence_pointer：Introduction Contributions (2)

### 28. Introduction Contributions 第3条

- order：28

- section：Introduction

- locator：Introduction Contributions 第3条

- move_code：CONTRIBUTION

- paraphrase_cn：贡献之三是提出LDA评价框架，处理局部决策边界边缘情况并提供使用局部解释的启发。

- rhetorical_function_cn：声明评价方法贡献

- depends_on_cn：LDA算法设计

- sets_up_cn：为LDA验证段落做准备

- evidence_pointer：Introduction Contributions (3)

### 29. Introduction Contributions 第4条

- order：29

- section：Introduction

- locator：Introduction Contributions 第4条

- move_code：CONTRIBUTION

- paraphrase_cn：贡献之四是展示基于XAI框架和交互式机器学习设计原则的原型UI，并以专家研究验证。

- rhetorical_function_cn：声明界面与用户研究贡献

- depends_on_cn：原型与访谈

- sets_up_cn：把文章贡献从算法扩展到系统

- evidence_pointer：Introduction Contributions (4)

### 30. Related Work P2 S1

- order：30

- section：Related Work

- locator：Related Work P2 S1

- move_code：PRACTICAL_STAKES

- paraphrase_cn：医疗领域充满需要自动化预测解释的应用，模型透明尤其关键。

- rhetorical_function_cn：连接HPA与XAI

- depends_on_cn：引言中的信任缺口

- sets_up_cn：引用多学科协作和生命风险证据

- evidence_pointer：Related Work P2 S1

### 31. Related Work P2 S2

- order：31

- section：Related Work

- locator：Related Work P2 S2

- move_code：MECHANISM

- paraphrase_cn：外科医生、住院医生和医学编码员等多学科团队常用HPA系统协作决策，因此透明和可理解性很重要。

- rhetorical_function_cn：给出透明重要的组织机制

- depends_on_cn：前一句

- sets_up_cn：强调解释是协作基础

- evidence_pointer：Related Work P2 S2

### 32. Related Work P3 S1

- order：32

- section：Related Work

- locator：Related Work P3 S1

- move_code：LIMITATION

- paraphrase_cn：已有医疗解释研究如注意力网络和可解释深度框架只针对深度模型和EHR数据。

- rhetorical_function_cn：指出现有方法适用性窄

- depends_on_cn：文献回顾

- sets_up_cn：形成模型无关缺口

- evidence_pointer：Related Work P3 S1

### 33. Related Work P3 S2

- order：33

- section：Related Work

- locator：Related Work P3 S2

- move_code：GAP

- paraphrase_cn：需要能推广到不同HPA问题和情境的可解释预测系统。

- rhetorical_function_cn：明确研究缺口

- depends_on_cn：面向深度模型的局限

- sets_up_cn：引出ROLEX的模型无关定位

- evidence_pointer：Related Work P3 S2

### 34. Theory and Motivation XAI框架 P1 S3

- order：34

- section：Theory and Motivation

- locator：Theory and Motivation XAI框架 P1 S3

- move_code：REQUIREMENT

- paraphrase_cn：构建XAI系统应充分考虑三个基本要求：情境理解、全过程伦理、法规与公共利益。

- rhetorical_function_cn：给出全文设计原则

- depends_on_cn：XAI黄金时代背景

- sets_up_cn：为ROLEX和UI设计提供框架

- evidence_pointer：Theory and Motivation: XAI Framework

### 35. Theory and Motivation 分类法 P1 S1

- order：35

- section：Theory and Motivation

- locator：Theory and Motivation 分类法 P1 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：现有解释方法可按解释范围和模型特异性两个广泛接受的标准分类。

- rhetorical_function_cn：引入分类法

- depends_on_cn：前文框架

- sets_up_cn：定位局部模型无关方法

- evidence_pointer：Theory and Motivation: A Taxonomy of Existing XAI Methods

### 36. Theory and Motivation 分类法 P2 S3

- order：36

- section：Theory and Motivation

- locator：Theory and Motivation 分类法 P2 S3

- move_code：MECHANISM

- paraphrase_cn：局部解释可被理解成对复杂制品进行逆向设计，以更深入理解现象。

- rhetorical_function_cn：给出局部解释的概念框架

- depends_on_cn：Simon设计思想

- sets_up_cn：把局部解释提升为一般设计原则

- evidence_pointer：Theory and Motivation: A Taxonomy of Existing XAI Methods

### 37. Theory and Motivation 局部模型无关 P1 S1

- order：37

- section：Theory and Motivation

- locator：Theory and Motivation 局部模型无关 P1 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：研究聚焦于局部、模型无关的方法，以适用于一般HPA系统。

- rhetorical_function_cn：缩小方法选择范围

- depends_on_cn：分类法

- sets_up_cn：讨论为什么不用内在可解释模型

- evidence_pointer：Theory and Motivation: Local and Model-Agnostic Explanations

### 38. Theory and Motivation 局部模型无关 P1 S2

- order：38

- section：Theory and Motivation

- locator：Theory and Motivation 局部模型无关 P1 S2

- move_code：GAP

- paraphrase_cn：尽管有人主张直接使用内在可解释模型，但医疗数据日益多样，难以对所有数据设计可解释模型。

- rhetorical_function_cn：反驳替代方案

- depends_on_cn：Rudin观点

- sets_up_cn：强化模型无关必要性

- evidence_pointer：Theory and Motivation: Local and Model-Agnostic Explanations

### 39. Theory and Motivation 局部模型无关 P2 S1

- order：39

- section：Theory and Motivation

- locator：Theory and Motivation 局部模型无关 P2 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：在局部模型无关方法中，主要关注扰动采样方法。

- rhetorical_function_cn：确定技术家族

- depends_on_cn：方法分类

- sets_up_cn：详细介绍LIME/LS/LEAP

- evidence_pointer：Theory and Motivation: Local and Model-Agnostic Explanations

### 40. Theory and Motivation 局部模型无关 P2 S2

- order：40

- section：Theory and Motivation

- locator：Theory and Motivation 局部模型无关 P2 S2

- move_code：LIMITATION

- paraphrase_cn：LIME虽被广泛接受，但缺乏客观评价标准且局部忠实性被稀释。

- rhetorical_function_cn：指出LIME限度

- depends_on_cn：LIME介绍

- sets_up_cn：引出LS和LEAP改进

- evidence_pointer：Theory and Motivation: Local and Model-Agnostic Explanations

### 41. Theory and Motivation 局部模型无关 P3 S1

- order：41

- section：Theory and Motivation

- locator：Theory and Motivation 局部模型无关 P3 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：LS先找靠近DB的enemy point并在其周围均匀采样，以提升局部忠实性。

- rhetorical_function_cn：描述LS机制

- depends_on_cn：LIME局限

- sets_up_cn：随后指出LS仍有缺陷

- evidence_pointer：Theory and Motivation: Local and Model-Agnostic Explanations

### 42. Theory and Motivation 局部模型无关 P4 S3

- order：42

- section：Theory and Motivation

- locator：Theory and Motivation 局部模型无关 P4 S3

- move_code：LIMITATION

- paraphrase_cn：但LS和LEAP不关注不同实例与DB的距离差异，假设局部DB线性，且缺少人类可解释界面。

- rhetorical_function_cn：集中列出三方面缺陷

- depends_on_cn：LS/LEAP介绍

- sets_up_cn：为ROLEX逐条解决这些缺陷

- evidence_pointer：Theory and Motivation: Local and Model-Agnostic Explanations

### 43. Proposed Method P3 S1

- order：43

- section：Proposed Method

- locator：Proposed Method P3 S1

- move_code：MECHANISM

- paraphrase_cn：局部解释模型主要解释黑箱分类器，而不是直接描述现实现象本身。

- rhetorical_function_cn：澄清解释对象

- depends_on_cn：局部模型定义

- sets_up_cn：讨论解释模型什么时候也能代表现象

- evidence_pointer：Proposed Method段落

### 44. Proposed Method P4 S1

- order：44

- section：Proposed Method

- locator：Proposed Method P4 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：ROLEX包括三个阶段：合成数据生成、局部模型拟合、患者级解释。

- rhetorical_function_cn：给出方法路线图

- depends_on_cn：方法定位

- sets_up_cn：按三阶段组织方法说明

- evidence_pointer：Proposed Method 末段

### 45. Synthetic Data Generation P1 S1

- order：45

- section：Proposed Method: Synthetic Data Generation

- locator：Synthetic Data Generation P1 S1

- move_code：REQUIREMENT

- paraphrase_cn：合成数据生成的目标是产生反映目标实例附近DB的样本，使局部模型更忠实。

- rhetorical_function_cn：给阶段设立目标

- depends_on_cn：三阶段路线图

- sets_up_cn：评价现有采样的不足

- evidence_pointer：Proposed Method: Synthetic Data Generation

### 46. Synthetic Data Generation P2 S1

- order：46

- section：Proposed Method: Synthetic Data Generation

- locator：Synthetic Data Generation P2 S1

- move_code：LIMITATION

- paraphrase_cn：LIME的高斯扰动可能包含远离目标实例的数据点，损害局部忠实性。

- rhetorical_function_cn：指出现有采样缺陷

- depends_on_cn：LIME公式

- sets_up_cn：引入LS和LEAP的采样改进

- evidence_pointer：Synthetic Data Generation P2

### 47. Synthetic Data Generation P4 S1

- order：47

- section：Proposed Method: Synthetic Data Generation

- locator：Synthetic Data Generation P4 S1

- move_code：LIMITATION

- paraphrase_cn：LS的enemy point不一定最优且每次随机，LEAP的PCA子空间也不能保证反映局部DB，统一采样半径更不适合距离DB差异大的实例。

- rhetorical_function_cn：集中反驳LS/LEAP

- depends_on_cn：LS/LEAP机制

- sets_up_cn：引出直接优化方案

- evidence_pointer：Synthetic Data Generation P4

### 48. Synthetic Data Generation P5 S1

- order：48

- section：Proposed Method: Synthetic Data Generation

- locator：Synthetic Data Generation P5 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：ROLEX直接优化采样中心与半径，以最大化局部fidelity。

- rhetorical_function_cn：给出核心设计决策

- depends_on_cn：前一句的缺陷

- sets_up_cn：形式化目标函数

- evidence_pointer：Synthetic Data Generation P5

### 49. Synthetic Data Generation P6 S1

- order：49

- section：Proposed Method: Synthetic Data Generation

- locator：Synthetic Data Generation P6 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：用训练集中最近异类实例作为固定点，无需启发式搜索，更稳定。

- rhetorical_function_cn：解释稳定性来源

- depends_on_cn：直接优化方案

- sets_up_cn：为鲁棒性主张提供依据

- evidence_pointer：Synthetic Data Generation P6

### 50. Synthetic Data Generation P8 S1

- order：50

- section：Proposed Method: Synthetic Data Generation

- locator：Synthetic Data Generation P8 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：由于非线性DB会导致采样样本不平衡，ROLEX使用SMOTE对少数类过采样。

- rhetorical_function_cn：引入不平衡修正

- depends_on_cn：非线性DB观察

- sets_up_cn：为消融实验中的SMOTE贡献做铺垫

- evidence_pointer：Synthetic Data Generation P8

### 51. Local Model Fitting P1 S1

- order：51

- section：Proposed Method: Local Model Fitting

- locator：Local Model Fitting P1 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：作者提出LinSep分数，用平衡准确率判断局部DB是否线性，并决定使用线性还是非线性局部模型。

- rhetorical_function_cn：设计自适应模型选择

- depends_on_cn：非线性DB问题

- sets_up_cn：后续边缘情况分析

- evidence_pointer：Local Model Fitting P1

### 52. Local Model Fitting P2 S1

- order：52

- section：Proposed Method: Local Model Fitting

- locator：Local Model Fitting P2 S1

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：解释的复杂性与忠实性存在权衡，非线性模型虽可能更忠实但可能不可解释。

- rhetorical_function_cn：设定方法边界

- depends_on_cn：LinSep选择

- sets_up_cn：后续叶节点正则化实验

- evidence_pointer：Local Model Fitting P2

### 53. Local Model Fitting P4 S1

- order：53

- section：Proposed Method: Local Model Fitting

- locator：Local Model Fitting P4 S1

- move_code：MECHANISM

- paraphrase_cn：远离DB的实例邻域同质，标准fidelity会虚高，无法区分不同局部模型。

- rhetorical_function_cn：解释LDA框架的必要性

- depends_on_cn：LocalFid定义

- sets_up_cn：提出LDA决策流程

- evidence_pointer：Local Model Fitting P4

### 54. Local Model Fitting P5 图6附近

- order：54

- section：Proposed Method: Local Model Fitting

- locator：Local Model Fitting P5 图6附近

- move_code：DESIGN_FEATURE

- paraphrase_cn：因此提出LDA框架：同质样本实例被排除出fidelity评价，异质实例再按LinSep选择线性或非线性模型。

- rhetorical_function_cn：给出评价框架设计

- depends_on_cn：同质性机制

- sets_up_cn：Algorithm 1与Table 6验证

- evidence_pointer：Local Model Fitting P5

### 55. Patient-Level Explanations P1 S1

- order：55

- section：Proposed Method: Patient-Level Explanations

- locator：Patient-Level Explanations P1 S1

- move_code：REQUIREMENT

- paraphrase_cn：局部解释训练后需要转换为人类可解释的表示，探索文本理由和可视化等多种模式。

- rhetorical_function_cn：把方法从模型输出推向用户界面

- depends_on_cn：局部模型训练

- sets_up_cn：开发原型UI

- evidence_pointer：Proposed Method: Patient-Level Explanations

### 56. Patient-Level Explanations P2 S3

- order：56

- section：Proposed Method: Patient-Level Explanations

- locator：Patient-Level Explanations P2 S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：开发原型是设计科学中同时保证严谨性和相关性的基本步骤。

- rhetorical_function_cn：为UI开发提供方法论正当性

- depends_on_cn：设计科学引用

- sets_up_cn：说明专家协作必要性

- evidence_pointer：Patient-Level Explanations P2

### 57. Analysis Data P1 S1

- order：57

- section：Analysis: Data

- locator：Analysis Data P1 S1

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：使用三个医疗数据集评估ROLEX：两个公开数据集加上一个大型脆性骨折队列。

- rhetorical_function_cn：建立评价材料

- depends_on_cn：方法确定

- sets_up_cn：说明三个数据的不同作用

- evidence_pointer：Analysis: Data

### 58. Analysis Data P2 S1

- order：58

- section：Analysis: Data

- locator：Analysis Data P2 S1

- move_code：PRACTICAL_STAKES

- paraphrase_cn：脆性骨折正成为全球严重的医疗和经济问题，早期诊断和干预非常重要。

- rhetorical_function_cn：赋予应用场景现实重要性

- depends_on_cn：数据选择

- sets_up_cn：解释特征筛选和队列数据构建

- evidence_pointer：Analysis Data P2

### 59. Analysis ML P2 S1

- order：59

- section：Analysis: Evaluation of Machine Learning Algorithms

- locator：Analysis ML P2 S1

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：比较两个可解释模型与五个黑箱模型，用AUC、准确率和平衡准确率评估。

- rhetorical_function_cn：为预测模型选择提供依据

- depends_on_cn：三个数据集

- sets_up_cn：报告黑箱模型性能

- evidence_pointer：Analysis: Evaluation of Machine Learning Algorithms

### 60. Analysis LE P1 S1

- order：60

- section：Analysis: Evaluation of Local Explanations

- locator：Analysis LE P1 S1

- move_code：RESULT

- paraphrase_cn：LDA框架显示大多数场景中存在大量边缘情况，可能导致LIME和LEAP等方法产生不忠实的解释。

- rhetorical_function_cn：展示评价框架的诊断结果

- depends_on_cn：表4数据

- sets_up_cn：强调需要更严格的LDA-fidelity

- evidence_pointer：Analysis: Evaluation of Local Explanations, Table 4

### 61. Analysis LE P2 表5附近

- order：61

- section：Analysis: Evaluation of Local Explanations

- locator：Analysis LE P2 表5附近

- move_code：RESULT

- paraphrase_cn：ROLEX在局部fidelity和LDA-fidelity上均一致高于已有基准，且不需要超参数网格搜索。

- rhetorical_function_cn：给出核心性能结果

- depends_on_cn：表5结果

- sets_up_cn：为鲁棒性主张和贡献提供证据

- evidence_pointer：Analysis: Evaluation of Local Explanations, Table 5

### 62. Analysis LE P3 表6附近

- order：62

- section：Analysis: Evaluation of Local Explanations

- locator：Analysis LE P3 表6附近

- move_code：RESULT

- paraphrase_cn：敏感性分析显示同质样本实例的近邻/远邻解释fidelity几乎相同，而异质样本实例下降20%到36%，说明标准fidelity对同质实例不敏感。

- rhetorical_function_cn：验证LDA框架的有效性

- depends_on_cn：LDA设计

- sets_up_cn：支持把同质实例排除出评价

- evidence_pointer：Analysis LE Table 6

### 63. Analysis LE 表7附近

- order：63

- section：Analysis: Evaluation of Local Explanations

- locator：Analysis LE 表7附近

- move_code：RESULT

- paraphrase_cn：消融实验显示去除SMOTE造成最大fidelity下降，去除贝叶斯优化也明显下降，去除非线性解释只在XGB上明显下降。

- rhetorical_function_cn：把总体性能归因到组件

- depends_on_cn：表7结果

- sets_up_cn：为后续复杂度实验和机制讨论提供依据

- evidence_pointer：Analysis LE Table 7

### 64. Analysis LE 图9附近

- order：64

- section：Analysis: Evaluation of Local Explanations

- locator：Analysis LE 图9附近

- move_code：RESULT

- paraphrase_cn：局部决策树叶节点数增加时fidelity上升，但约10个节点后进入平台，因此设定为10。

- rhetorical_function_cn：量化可解释性与忠实性权衡

- depends_on_cn：复杂度实验

- sets_up_cn：为UI中的规则模型提供参数

- evidence_pointer：Analysis LE Figure 9

### 65. Analysis UI 患者#283部分

- order：65

- section：Analysis: Patient-Level Explanations and Local Interpretations

- locator：Analysis UI 患者#283部分

- move_code：RESULT

- paraphrase_cn：患者#283的局部解释显示体脂和体脂率与骨折风险正相关，与文献中的平均效应相反，专家认为可能是亚组异质性造成。

- rhetorical_function_cn：展示局部解释的知识发现潜力

- depends_on_cn：原型UI

- sets_up_cn：引出专家访谈对实践价值的判断

- evidence_pointer：Analysis UI, Table 8, Figures 12-14

### 66. Analysis Interviews 表9附近

- order：66

- section：Analysis: Expert Interviews

- locator：Analysis Interviews 表9附近

- move_code：RESULT

- paraphrase_cn：四名专家访谈后的归纳编码显示，ROLEX界面被认为最有助于与公众沟通、个性化护理和解决信息不对称。

- rhetorical_function_cn：提供定性外部证据

- depends_on_cn：原型UI

- sets_up_cn：支撑讨论部分关于实践影响的论述

- evidence_pointer：Analysis Expert Interviews, Table 9

### 67. Discussion Practical Implications P1 S1

- order：67

- section：Discussion

- locator：Discussion Practical Implications P1 S1

- move_code：CONTRIBUTION

- paraphrase_cn：信任强烈影响IT制品使用，可靠解释对建立信任很重要，ROLEX通过让医生和患者解释黑箱模型来建立信任。

- rhetorical_function_cn：把技术结果转化为实践贡献

- depends_on_cn：前期结果和Gregor & Benbasat

- sets_up_cn：推导个性化医疗与知识发现含义

- evidence_pointer：Discussion Practical Implications

### 68. Discussion Contributions to IS Knowledge Base P1 S1

- order：68

- section：Discussion

- locator：Discussion Contributions to IS Knowledge Base P1 S1

- move_code：CONTRIBUTION

- paraphrase_cn：ROLEX与医疗IS、大数据预测分析和设计科学等多个IS研究流相关。

- rhetorical_function_cn：定位IS学科贡献

- depends_on_cn：全文成果

- sets_up_cn：讨论理论意义与未来工作

- evidence_pointer：Discussion Contributions to IS Knowledge Base

### 69. Limitations P1 S1

- order：69

- section：Limitations

- locator：Limitations P1 S1

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：直接优化参数可能更耗时，尤其是复杂非线性数据集。

- rhetorical_function_cn：承认方法成本

- depends_on_cn：优化设计

- sets_up_cn：说明优化成本被调参成本抵消

- evidence_pointer：Discussion Limitations

### 70. Limitations P2 S1

- order：70

- section：Limitations

- locator：Limitations P2 S1

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：局部解释需要用户逐点检查，可能造成认知负担，未来可研究中层子群解释。

- rhetorical_function_cn：指出可解释性边界

- depends_on_cn：局部解释性质

- sets_up_cn：给出子群解释研究方向

- evidence_pointer：Discussion Limitations

### 71. Limitations P3 S1

- order：71

- section：Limitations

- locator：Limitations P3 S1

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：post hoc解释方法有内在局限，如易受对抗攻击，离DB远的实例仍难解释。

- rhetorical_function_cn：承认方法家族局限

- depends_on_cn：post hoc解释性质

- sets_up_cn：未来研究ground truth与防御方向

- evidence_pointer：Discussion Limitations

## 写作技术

- gap_construction_cn：不是简单说“没人研究”，而是先承认已有LIME/LS/LEAP有改进，再逐条指出它们在enemy point稳定性、采样半径统一性、DB非线性、同质邻域和UI上的具体缺陷，形成可被新方法逐项填补的缺口。

- signposting_cn：摘要即给出关键词和贡献列表；引言最后用“本文组织如下”预告；方法部分用“三阶段”组织；分析部分用数据、预测模型、局部解释、患者解释、专家访谈逐层推进；讨论用实践影响和IS知识库两部分定位贡献。

- transition_logic_cn：每节末尾常用“这些局限性由ROLEX解决”或“为检验这一点，我们进行……”连接；例如从XAI框架过渡到方法设计，从预测模型过渡到局部解释评价，从总体benchmark过渡到敏感性和消融。

- claim_evidence_rhythm_cn：先提出技术主张，随后立即给表/图；在每个表后写一小段解释性话语，把数字翻译成机制结论；例如表5后说明LS优于LIME是因为靠近enemy point采样更有效，LEAP差说明子空间学习无效。

- benchmark_narrative_cn：benchmark不是孤立堆表，而是先用表4展示边缘情况使旧指标不可信，再用表5展示ROLEX在新旧指标上都更好；随后表6解释为什么新指标更严格，表7解释优势出自哪些组件，形成“指标-结果-机制”链条。

- theory_return_cn：讨论部分不是简单重述结果，而是把局部解释重新放回XAI三要求框架，论证ROLEX提升信任、暴露不完备性、缓解信息不对称，从而回应引言中的HPA落地难题。

- contribution_positioning_cn：贡献被拆成XAI框架、方法、评价框架和UI四类，分别对应设计科学研究中的理论指导、制品、评价和系统原型，使文章不只是一次方法改进，而是一组可复用设计知识。

- novelty_protection_cn：作者用多个数据集、多个黑箱模型和一致性结果防止把优势解释为数据集特定；用消融实验把性能归因到具体机制；用LDA-fidelity说明旧指标会虚高；用专家访谈说明实践价值，从而把ROLEX从一次性技术结果抬升为设计科学与XAI知识。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：用现实问题（HPA落地难）和现象（黑箱模型不被信任）建立紧迫感

- research_job_cn：收集HPA和XAI文献，找出可信度与患者安全痛点

- required_evidence_cn：引用医疗AI风险、信任研究和IS领域HPA趋势

- transition_to_next_cn：将现实问题收窄为解释方法的技术缺口

#### 2. 2

- step：2

- writing_job_cn：用分类法或框架明确方法定位（模型无关、局部、扰动采样）

- research_job_cn：系统梳理现有方法，逐条列出限制

- required_evidence_cn：LIME/LS/LEAP的机制描述和失败案例或图示

- transition_to_next_cn：每一项限制都对应新方法的某一设计

#### 3. 3

- step：3

- writing_job_cn：描述新方法的阶段、目标函数和算法

- research_job_cn：设计算法，给出形式化目标和关键步骤

- required_evidence_cn：方程、伪代码、示意图以及为何能避免旧缺陷的推理

- transition_to_next_cn：方法提出后转向数据与评价

#### 4. 4

- step：4

- writing_job_cn：准备多个数据集和多种黑箱模型，建立评价基线

- research_job_cn：训练预测模型、划分训练/测试、调优超参数

- required_evidence_cn：预测性能表，说明黑箱模型多样性

- transition_to_next_cn：预测模型就绪后生成并比较局部解释

#### 5. 5

- step：5

- writing_job_cn：报告基准对比与评价指标，同时提出更严格指标

- research_job_cn：计算fidelity/LDA-fidelity、边缘情况统计和敏感性分析

- required_evidence_cn：对比表、敏感性表和指标合理性论证

- transition_to_next_cn：如果总体性能好，需要用消融回答为什么好

#### 6. 6

- step：6

- writing_job_cn：用消融实验和边界实验拆解性能来源，设置解释复杂度

- research_job_cn：逐一删除组件、给基线加组件、扫描复杂度参数

- required_evidence_cn：消融表、基线增强表和复杂度曲线

- transition_to_next_cn：技术评价后转向界面与用户价值

#### 7. 7

- step：7

- writing_job_cn：展示原型UI和真实案例，把局部解释转成医生能看懂的文本/规则/图

- research_job_cn：与领域专家合作解释具体患者，形成定性案例

- required_evidence_cn：界面截图、患者特征表、局部规则和医学解释

- transition_to_next_cn：用小型专家访谈补充外部有效性

#### 8. 8

- step：8

- writing_job_cn：在讨论中把结果接回引言缺口，并声明对不同IS流派的贡献

- research_job_cn：说明信任、信息不对称、个性化医疗、设计科学意义

- required_evidence_cn：专家访谈编码、与前人理论的连接、局限性承认

- transition_to_next_cn：最后给出未来工作

### most_transferable_moves_cn

1. 用分类法定位贡献，用一个框架把方法、评价和界面统一起来

2. 把旧方法缺陷逐条转化为新方法设计点

3. 在benchmark之外增加敏感性、消融和边界条件分析

4. 用具体患者案例把数值结果翻译成临床可理解故事

5. 用小型专家访谈作为设计科学的定性验证

### resource_intensive_or_nonstandard_parts_cn

1. 脆性骨折真实队列数据需要多年纵向随访和医疗专家合作，成本高

2. 医疗专家访谈虽样本小但依赖临床人脉和组织许可

3. 原型UI的开发需要交互设计和临床知识协作

4. 直接优化采样参数需要较多计算，尤其复杂数据集

### what_not_to_copy_superficially_cn

1. 不能只复制“我们提出XAI框架”而不给出可操作的框架内容

2. 不能只宣称“更稳健”而没有无调参/少调参的对比证据

3. 不能跳过LDA风格的同质边缘情况检验，否则fidelity虚高会被质疑

4. 不能把小样本定性访谈说成临床有效证据

5. 不能只用单个数据集/单模型证明通用性

- single_best_description_of_the_routine_cn：先建立现实信任缺口，再用分类和框架定位方法位置，把旧方法缺陷转化为具体设计，用多数据集benchmark和更严格指标证明改进，用消融和边界实验解释改进来源，最后用原型和专家访谈把技术性能转化为医疗价值与设计知识。

## 分析边界

文章以全文文本形式提供，但无法确认期刊编页，位置定位使用章节和段落；公式中的部分符号因OCR有缺失；图表细节依赖文字说明；专家访谈结果只有归纳表格，缺乏完整访谈协议和原始引文上下文；附录C等补充材料存在，但未提供独立附录格式。
