# Data misrepresentation detection for insurance underwriting fraud prevention

- 作者：Félix Vandervorst; Wouter Verbeke; Tim Verdonck
- 年份 / 期刊：2022 / Decision Support Systems
- DOI：10.1016/j.dss.2022.113798
- 源文件：19972_2022_data-misrepresentation-detection-for-insurance-underwriting-fraud-prevention.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：performance_gap_artifact_benchmark_generalize
- 置信度：0.82

## 文章级论证概况

- 核心问题：如何在不依赖历史欺诈标签、且能适应定价政策变化的情况下，在保险承保申请时检测因自我报告数据虚假陈述而产生的保费欺诈风险？

- 制品与设计：文章构建了一个基于条件密度估计（CDE）的保费欺诈风险评估方法：利用已验证合同数据 (X,Z) 估计自我报告变量 Z 在给定正确测量变量 X 下的条件密度 f(z|x)，再结合定价函数 μ 以积分形式计算条件保费欺诈风险 P(μ(Z*,X)<μ(Z,X)|X=x,Z*=z*)。方法组合使用 FlexCode（正交基投影+随机森林回归）和 RFCDE（随机森林加权核密度），引入 HDR coverage loss 作为模态诊断和异常检测指标，并通过 Shapley 值给出可解释性分解。

- 客观结果：在比利时车险真实数据集（57,000份已验证合同报价，73,000份申请）上，FlexCode 和 RFCDE 的覆盖率图均接近对角线，表明条件密度估计校准良好；在混合类型双变量场景中，CDE loss 和 HDR loss 共同选择的最优 basis size 为3；欺诈风险评分在专家标记的“高风险”子段（2500份申请）上的分布明显高于一般申请，说明分数具有区分能力。

- 核心贡献：作者声称的主要贡献是提出了一种无需历史欺诈标签、可适应外生定价政策变化、支持多变量及混合类型自我报告数据的保费欺诈检测框架；同时提出 HDR coverage loss 作为 CDE 评价的补充指标，并建立了 CDE 模型 Shapley 值分解的理论链接以增强可解释性。

- 整篇论证链：文章先指出现有保费欺诈检测受限于“不自我揭示”的标签问题，且以往统计模型仅能处理单个二元自我报告变量、假设单向误分类、无法适应定价变化。作者将保费欺诈风险定义为在给定正确测量变量和已报告自我报告值条件下，真实自我报告值导致更高保费的概率，从而将问题转化为条件密度估计。随后，文章利用 FlexCode 与 RFCDE 两种 CDE 技术估计 f(z|x)，并用 CDE loss 与新增的 HDR coverage loss 共同评价与选择参数；在真实车险数据上依次验证了单变量连续、双变量连续、混合类型和有序变量的 CDE 可行性。最后，文章将估计出的密度与 GLM 形式的定价政策 μ 结合，生成保费欺诈风险分数，在专家标记子段上展示了分布差异，并通过 Shapley 值分解说明了模型的可解释性。讨论与结论部分将贡献回扣到文献缺口，强调无需标签、适应动态定价、可扩展至其他申请欺诈场景，完成了从方法构建到应用验证的闭环。

## 类型与写作弧线判定

- 论文主类型判定：文章核心是设计并构建一个基于条件密度估计的保费欺诈检测方法（制品），在真实车险数据上进行案例研究评估，并讨论方法的适用条件与设计选择。虽然也使用了现有CDE技术，但整体遵循需求/问题—构建—评价—设计知识的模式，而非严格的理论假设检验或多研究程序。

- 主导写作弧线判定：引言建立现有方法在检测维度、标签依赖和动态适应性上的性能缺口，随后提出基于CDE的新制品，通过案例研究（而非传统benchmark）展示其在多个数据类型上的表现，最终推广为可复用的设计知识（HDR loss、Shapley解释、阶段式验证）。行文主线是‘缺口—制品—证据—一般化’。

## 研究开展程序

- study_or_phase_count：6

- 研究阶段总序列：六个阶段依次推进：1) 形式化保费欺诈风险问题；2) 引入CDE方法并补充HDR评价指标；3) 在真实单变量连续数据上验证CDE校准；4) 扩展到双变量连续与混合类型数据；5) 展示欺诈分数在真实申请样本中的判别力；6) 演示基于Shapley值的可解释性。各阶段从数学模型、方法组件、基础验证、扩展验证、应用价值到采用障碍逐步累积证据。

### studies_or_phases

#### 1. 问题形式化与条件密度建模

- order：1

- name_cn：问题形式化与条件密度建模

- question_cn：如何将承保保费欺诈检测转化为一个可由数据驱动的、合同依赖的风险评估问题？

- inputs_and_setting_cn：概念定义：真实承保信息U、报告信息U*、自我报告变量Z、正确测量变量X；定价政策μ；来自已验证合同的配对数据 (X,Z)。

- designed_or_compared_object_cn：定义了保费欺诈风险 P(μ(Z*,X)<μ(Z,X)) 及其条件版本，通过指示函数与f(z|x)积分表示。

- baseline_control_or_counterfactual_cn：无；此阶段为数学推导。

##### objective_metrics

1. 条件保费欺诈风险公式

2. CDE loss 定义

- analysis_method_cn：数学建模和概率论推导，基于测量误差文献和CDE文献。

- main_result_cn：给出条件保费欺诈风险公式，并指出需要估计f(z|x)。

- argumentative_role_cn：建立整个方法的核心理论框架，将业务问题转化为统计估计问题。

- remaining_uncertainty_cn：如何在实际中估计多变量、混合类型的条件密度，以及单一CDE loss是否足够评估。

- link_to_next_phase_cn：引出对CDE技术（FlexCode、RFCDE）的选择，并指出CDE loss不足，需要补充指标。

##### evidence_pointers

1. Section 3.1

2. Section 3.2

3. Section 3.3

4. Equation (2)

#### 2. CDE方法选型与HDR补充评价指标

- order：2

- name_cn：CDE方法选型与HDR补充评价指标

- question_cn：应采用哪些CDE技术？如何评价条件密度估计的校准质量？

- inputs_and_setting_cn：FlexCode（正交基投影+回归）、RFCDE（随机森林加权核密度）、HDR理论、GLM定价形式。

- designed_or_compared_object_cn：引入FlexCode和RFCDE；定义HDR coverage loss；提出利用定价政策简化风险计算；提出阶段式验证。

- baseline_control_or_counterfactual_cn：将CDE loss与HDR coverage loss作为互补指标比较；将vanilla random forest作为条件均值baseline（用于图2对比）。

##### objective_metrics

1. CDE loss

2. HDR coverage loss

3. Kullback-Leibler散度（用于对比先验/后验）

- analysis_method_cn：文献综合和数学推导；在案例中通过覆盖率图和KL值评价。

- main_result_cn：HDR coverage loss被提出作为CDE loss的补充，用于basis size选择；GLM乘法形式简化风险计算。

- argumentative_role_cn：完成方法工具箱，为后续实证提供评价手段和实际应用方式。

- remaining_uncertainty_cn：这些方法在真实数据上是否工作良好，尤其是多变量混合类型场景。

- link_to_next_phase_cn：进入案例研究，验证所提方法在真实车险数据上的表现。

##### evidence_pointers

1. Section 3.4

2. Section 3.5

3. Section 3.6

4. Equations (5), (6), HDR loss公式

#### 3. 真实数据单变量连续CDE验证

- order：3

- name_cn：真实数据单变量连续CDE验证

- question_cn：在真实车险数据上，用FlexCode和RFCDE估计驾驶员驾照年龄的条件密度是否校准良好？

- inputs_and_setting_cn：57,000份已验证合同报价；X为38个车辆特征（第三方提供），Z为驾照年龄（连续）；测试集为19k观测。

- designed_or_compared_object_cn：FlexCode-RF（Fourier basis, I=5）、RFCDE、vanilla random forest（作为条件均值参考）。

- baseline_control_or_counterfactual_cn：三种模型对比；先验密度f(z)作为对照；KL散度度量X的增量信息。

##### objective_metrics

1. 理论覆盖率 vs 经验覆盖率

2. KL散度

- analysis_method_cn：5折交叉验证选择参数；覆盖率图；KL散度比较。

- main_result_cn：FlexCode和RFCDE的覆盖率图均接近对角线，但FlexCode的KL散度比RFCDE更大，说明其对X更敏感。

- argumentative_role_cn：证明两种CDE方法在基本单变量场景下都能提供校准的密度估计。

- remaining_uncertainty_cn：多变量和混合类型情况下是否仍然有效。

- link_to_next_phase_cn：自然扩展到双变量连续和混合类型场景。

##### evidence_pointers

1. Section 4.1

2. Section 4.2.1

3. Figures 2 and 3

#### 4. 多变量与混合类型CDE扩展

- order：4

- name_cn：多变量与混合类型CDE扩展

- question_cn：当自我报告变量为双变量连续或离散+连续混合时，所提出的CDE方法能否有效估计联合条件密度？

- inputs_and_setting_cn：同一数据集；双变量Z=(驾照年龄，驾驶员年龄)；混合类型Z=(驾照年龄，驾驶记录评分)；驾驶记录评分是有序离散变量。

- designed_or_compared_object_cn：RFCDE（多变量核，带宽矩阵约束/非约束）；FlexCode通过张量积与异质基（Fourier for连续，Haar for离散）扩展。

- baseline_control_or_counterfactual_cn：比较不同带宽矩阵参数化；不同basis size下的CDE loss和HDR loss。

##### objective_metrics

1. CDE loss

2. HDR coverage loss

3. 带宽矩阵稳定性

- analysis_method_cn：核密度估计；双变量带宽矩阵固定为先验密度估计结果；张量积基扩展；损失函数曲线选择basis size。

- main_result_cn：双变量连续示例展示了联合密度估计；混合类型中，CDE loss和HDR loss均在basis size=3时最小。

- argumentative_role_cn：表明方法可推广到更实际的多元场景，特别是混合类型，弥补了原始FlexCode/RFCDE的限制。

- remaining_uncertainty_cn：这些密度估计能否转化为有实际判别力的欺诈分数。

- link_to_next_phase_cn：在完整的欺诈分数应用中检验方法的最终目标。

##### evidence_pointers

1. Section 4.2.2

2. Section 4.2.3

3. Figures 4-8

#### 5. 欺诈评分应用与专家标记子段验证

- order：5

- name_cn：欺诈评分应用与专家标记子段验证

- question_cn：基于条件密度和定价政策计算出的保费欺诈风险分数，能否在真实申请样本上识别高风险申请？

- inputs_and_setting_cn：73,000份新合同申请（含被验证和拒绝的）；其中2500份被专家标记为“更高保费欺诈风险”但未确认欺诈；定价函数为驾照年龄的严格递减函数（附录图13），阈值5%溢价差。

- designed_or_compared_object_cn：保费欺诈风险分数；对一般申请和“风险”子段分别绘制风险分数直方图。

- baseline_control_or_counterfactual_cn：一般申请样本 vs 专家标记的风险子段样本；红色区域表示至少5%溢价差异的区域。

##### objective_metrics

1. 风险分数直方图分布差异

- analysis_method_cn：描述性统计和可视化对比；使用CDE估计f(z|x)，在风险子段上计算风险分数。

- main_result_cn：风险子段的分数分布明显高于一般申请，表明模型能够区分可疑申请。

- argumentative_role_cn：证明方法在最终应用目标上的有效性，即实际决策支持功能。

- remaining_uncertainty_cn：专家标记子段并未确认欺诈，且未与其他欺诈检测方法进行量化对比。

- link_to_next_phase_cn：转向可解释性讨论，因为实际采用需要模型解释。

##### evidence_pointers

1. Section 4.3

2. Figures 9-11

3. Figure 13 in Appendix

#### 6. 基于Shapley值的CDE可解释性

- order：6

- name_cn：基于Shapley值的CDE可解释性

- question_cn：如何解释条件密度估计中每个特征X对后验密度f(z|x)偏离先验f(z)的贡献？

- inputs_and_setting_cn：FlexCode的正交基分解；Shapley值框架；一个样本预测（图12）。

- designed_or_compared_object_cn：提出并证明两个命题：CDE模型的Shapley值可分解为各基函数回归Shapley值的加权和；条件期望模型的Shapley值也可由基函数Shapley值积分得到。

- baseline_control_or_counterfactual_cn：先验密度作为基线；后验密度CDE raw与变量贡献之和的恒等性验证。

##### objective_metrics

1. 变量贡献曲线

2. 加性性（Shapley值之和等于预测差）

- analysis_method_cn：理论证明（附录）和单样本可视化。

- main_result_cn：示例中功率、车高、车长和车龄对低驾照年龄区间的密度有正贡献；可解释性有助于验证和采用。

- argumentative_role_cn：降低黑箱顾虑，支持模型在决策流程中的使用。

- remaining_uncertainty_cn：Shapley值解释在实际业务决策中的接受度未直接评估。

- link_to_next_phase_cn：讨论和结论部分总结贡献并指出未来方向。

##### evidence_pointers

1. Section 4.4

2. Figure 12

3. Appendix A.2

4. Propositions 1 and 2

## 各部分修辞架构

### abstract_moves

1. CONTEXT

2. RQ_OR_OBJECTIVE

3. DESIGN_FEATURE

4. DESIGN_FEATURE

5. STUDY_OVERVIEW

6. RESULT

### introduction_moves

1. CONTEXT

2. PRACTICAL_STAKES

3. PRIOR_KNOWLEDGE

4. LIMITATION

5. GAP

6. RQ_OR_OBJECTIVE

7. STUDY_OVERVIEW

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE

2. PRIOR_KNOWLEDGE

3. LIMITATION

4. REQUIREMENT

5. THEORY_INTRO

6. THEORY_INTRO

7. METHOD_JUSTIFICATION

### artifact_design_moves

1. REQUIREMENT

2. MECHANISM

3. DESIGN_FEATURE

4. DESIGN_FEATURE

5. LIMITATION

6. DESIGN_FEATURE

7. DESIGN_FEATURE

### evaluation_moves

1. METHOD_JUSTIFICATION

2. STUDY_OVERVIEW

3. RESULT

4. RESULT

5. RESULT

6. RESULT

### discussion_and_contribution_moves

1. RESULT

2. BOUNDARY_CONDITION

3. LIMITATION_AND_FUTURE

4. CONTRIBUTION

5. CONTRIBUTION

6. CONTRIBUTION

7. PRACTICAL_STAKES

8. BOUNDARY_CONDITION

## 理论/知识到设计的翻译

### 知识/理论基础

1. 测量误差理论（条件密度表示误报）

2. 条件密度估计方法（FlexCode, RFCDE, 核密度）

3. 高密度区域（HDR）诊断

4. Shapley值可解释性

5. 保险定价GLM乘法形式

- 理论—设计耦合：direct

- 耦合判定理由：目标问题是直接从测量误差文献中的条件密度表示推导出的；方法选择（FlexCode、RFCDE）直接由CDE问题驱动；HDR loss来自HDR理论；定价政策乘法形式直接用于简化风险公式；Shapley值分解依赖FlexCode的正交基结构。每一步设计都源于理论或领域知识，并在案例中通过覆盖率和损失函数得到直接检验。

- 理论到设计翻译链：测量误差文献指出误报问题可用条件密度表示 → 保费欺诈风险定义为条件概率，需要估计f(z|x) → CDE理论提供FlexCode和RFCDE两种估计器 → 但CDE loss不充分，需HDR理论补充评价 → 保险定价GLM乘法形式使风险计算只需相对价格因子 → 为实际使用，用Shapley值将CDE解释分解到每个特征。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：数据误报问题可以表示为条件密度，其中Z是目标变量，f(z|x)是希望在给定X下估计的条件密度。

- mechanism_cn：自我报告值Z*可能是真实值Z的误报，正确测量变量X可作为条件信息。

- design_requirement_cn：需要估计多元、混合类型变量Z的条件密度f(z|x)，而不假设特定分布形式。

- artifact_choice_cn：采用FlexCode（正交基投影+回归）和RFCDE（随机森林加权核密度）作为CDE估计器。

- evaluated_contrast_cn：在真实车险数据上对比FlexCode与RFCDE的覆盖率图和KL散度；在混合类型中对比不同basis size。

- objective_result_cn：两种方法覆盖率图接近对角线；混合类型下basis size=3时CDE loss和HDR loss均最小。

##### evidence_pointers

1. Section 3.4

2. Figures 2, 6, 7

#### 2. 2

- theory_or_knowledge_claim_cn：CDE loss（积分平方误差）在真实数据中难以验证，且单一指标不足以评价密度估计。

- mechanism_cn：仅看CDE loss可能选择错误的basis size或掩盖估计问题。

- design_requirement_cn：需要补充一个能反映校准质量的指标。

- artifact_choice_cn：提出基于高密度区域（HDR）的HDR coverage loss，并作为basis size选择的互补标准。

- evaluated_contrast_cn：在混合类型双变量场景中同时绘制CDE loss和HDR loss随basis size变化的曲线。

- objective_result_cn：两个损失函数在basis size=3时同时最小，说明HDR loss与CDE loss一致且互补。

##### evidence_pointers

1. Section 3.5

2. Figures 6 and 7

#### 3. 3

- theory_or_knowledge_claim_cn：保险定价通常采用GLM乘法形式 μ(z,x)=μ0 μz(z) μx(x)。

- mechanism_cn：在乘法形式下，条件保费欺诈风险公式可约去X部分，只需相对价格因子μz。

- design_requirement_cn：在实际计算中，只需要知道μz(z)而不需要完整定价模型。

- artifact_choice_cn：在案例研究中使用简化的风险分数公式（式7），以驾照年龄作为定价递减变量。

- evaluated_contrast_cn：在实际应用中设置5%溢价差阈值，计算风险分数。

- objective_result_cn：风险分数在专家标记子段上分布更高。

##### evidence_pointers

1. Section 3.6

2. Equations (7)

3. Figure 9-10

#### 4. 4

- theory_or_knowledge_claim_cn：Shapley值提供模型预测的加性分解，可解释每个特征的贡献。

- mechanism_cn：由于FlexCode将CDE分解为正交基上的条件期望，Shapley值可在线性层面叠加。

- design_requirement_cn：需要让CDE模型对非统计学家可解释。

- artifact_choice_cn：证明两个命题：CDE的Shapley值等于基函数回归Shapley值的加权和；条件期望的Shapley值可由基函数Shapley值积分得到。

- evaluated_contrast_cn：展示一个样本预测的变量贡献曲线，并验证加和性。

- objective_result_cn：示例中功率、车高、车长、车龄等变量对低驾照年龄密度有正贡献，且Shapley值之和等于后验密度差。

##### evidence_pointers

1. Section 4.4

2. Figure 12

3. Appendix A.2

## 评价逻辑

### evaluation_modes

1. 离线统计指标评价（CDE loss, HDR coverage loss, KL散度）

2. 可视化诊断（覆盖率图、密度图）

3. 实际应用案例（欺诈分数分布对比）

4. 理论证明（Shapley值分解）

5. 专家标记子段验证（非正式对照）

- why_these_evaluations_cn：由于真实条件密度未知，需要多种互补指标来校准估计；覆盖率图直观显示校准；KL散度衡量X的增量信息；HDR loss与CDE loss共同选择超参数；欺诈分数应用直接检验决策支持目标；专家子段分布差异提供最终实用性的初步证据。可解释性通过理论证明保证数学正确性，并通过可视化演示说明可用性。

- benchmark_and_contrast_chain_cn：首先在单变量场景中，将FlexCode和RFCDE与vanilla random forest（作为条件均值参考）以及先验密度f(z)对比，通过覆盖率图和KL散度建立两种CDE方法的基本有效性。随后在混合类型场景中，利用CDE loss和HDR loss曲线共同选择basis size，作为方法选择的量化依据。最后在欺诈分数应用中，以一般申请分布为baseline，对比专家标记高风险子段的分数分布，形成从密度估计质量到应用判别力的递进证据链。

### claim_evidence_ledger

#### 1. FlexCode和RFCDE能够产生校准良好的条件密度估计。

- claim_cn：FlexCode和RFCDE能够产生校准良好的条件密度估计。

- evidence_cn：图2中两种方法的理论-经验覆盖图接近对角线。

- status：支持

#### 2. HDR coverage loss可作为CDE loss的补充评价指标。

- claim_cn：HDR coverage loss可作为CDE loss的补充评价指标。

- evidence_cn：图6-7中两种损失在basis size=3时同时最小。

- status：支持

#### 3. 所提方法能在实际中识别高风险欺诈申请。

- claim_cn：所提方法能在实际中识别高风险欺诈申请。

- evidence_cn：图9-10中专家标记的高风险子段风险分数分布显著高于一般申请。

- status：部分支持（专家标记未确认欺诈，且无正式统计检验）

#### 4. CDE模型可通过Shapley值进行可解释分解。

- claim_cn：CDE模型可通过Shapley值进行可解释分解。

- evidence_cn：附录A.2的命题证明和命题2，图12的示例验证。

- status：支持（数学证明）

#### 5. 方法无需历史欺诈标签。

- claim_cn：方法无需历史欺诈标签。

- evidence_cn：CDE仅使用已验证合同数据 (X,Z)，不涉及欺诈标签。

- status：支持

#### 6. 方法能适应定价政策变化。

- claim_cn：方法能适应定价政策变化。

- evidence_cn：风险计算仅在公式中包含定价函数μ，若μ改变只需重新计算指示函数，无需重新训练CDE。

- status：支持（理论上），但未在案例中明确测试定价变化

- internal_validity_strategy_cn：使用交叉验证选择随机森林参数；CDE loss和HDR loss在独立的测试集上计算；欺诈分数计算中使用独立于训练CDE的申请样本（虽然部分申请已在训练中，但风险分数计算不重新训练）。

- external_validity_strategy_cn：使用真实保险公司4年数据，包含第三方验证的车辆信息；强调方法在不同保险领域（车险、财险、健康险）的推广性；在结论中指出可适用于其他非保险领域的申请欺诈。

- what_is_not_actually_tested_cn：没有真实欺诈标签，专家子段只是‘疑似’高风险；没有与现有的其他欺诈检测方法在相同数据上进行性能对比；没有对定价政策变化进行模拟或实证测试；没有评估Shapley解释在实际用户决策中的有效性和采用率。

## 贡献闭环

- technical_claim_cn：提出了用CDE估计自我报告数据条件密度，并转化为保费欺诈风险分数的技术路径，支撑该路径的CDE loss和HDR loss联合评价有效。

- artifact_claim_cn：文章构建了一个可用于承保决策支持的系统：输入已验证合同数据和定价政策，输出每个申请的风险分数，并能触发进一步验证或拒绝。

- mechanism_claim_cn：欺诈风险的机制是：当自报变量Z*使得μ(Z*)低于真实变量Z对应的μ(Z)时，存在财务动机；通过f(z|x)估计自报变量的合理取值范围，从而量化这一动机的实现概率。

- boundary_claim_cn：方法有效性的边界是：条件密度估计的精度依赖于X对Z的可预测性（在车险案例中即‘根据车猜人’）；如果X无法预测Z，则方法接近先验分布，欺诈检测能力有限。

- reusable_design_knowledge_cn：可复用设计知识包括：(1) 使用HDR coverage loss作为CDE loss的补充以选择超参数；(2) 利用乘法定价模型简化风险计算；(3) 采用阶段式验证策略，用已验证变量更新条件密度；(4) 通过正交基分解将Shapley值扩展到CDE场景。

- theoretical_contribution_cn：将保费欺诈检测与条件密度估计联系起来，扩展了测量误差文献中针对单一二元变量的框架到多元混合类型；并将Shapley值的可解释性理论从条件均值模型拓展到条件密度模型。

- how_discussion_closes_intro_gap_cn：引言指出文献局限于单个二元变量、静态定价且无应用导向；文章在结论和讨论中明确指出新方法支持多变量混合类型、适应定价变化、提供合同依赖风险分数，从而直接回应这些缺口。

- overclaim_or_unsupported_leaps_cn：作者在摘要和结论中主张‘有效’检测，但实际证据仅为专家标记子段的分数分布差异，未提供真正的欺诈确认或接收者操作特征曲线等定量指标；‘自适应定价变化’仅通过公式体现，未进行实验验证；‘可以检测异常点’的证据更多是概念性的，‘traffic light’也只是提议。

## 句级写作动作图谱

### 1. 第1句

- order：1

- section：Abstract

- locator：第1句

- move_code：CONTEXT

- paraphrase_cn：保费欺诈是客户在投保时虚报信息以获取不恰当低保费的行为。

- rhetorical_function_cn：立即定义核心业务问题，为读者建立问题框架。

- depends_on_cn：无

- sets_up_cn：为后文提出检测方法做铺垫。

- evidence_pointer：Abstract 第1段第1句

### 2. 第2句

- order：2

- section：Abstract

- locator：第2句

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：我们提出一种在申请时评估承保保费欺诈风险的新方法，特别针对可能被虚报的自我报告信息。

- rhetorical_function_cn：声明论文目标，吸引读者注意力。

- depends_on_cn：依赖问题背景。

- sets_up_cn：引出后续的方法描述。

- evidence_pointer：Abstract 第2句

### 3. 第3句

- order：3

- section：Abstract

- locator：第3句

- move_code：DESIGN_FEATURE

- paraphrase_cn：方法基于一组已验证合同的条件密度估计。

- rhetorical_function_cn：简要说明方法核心。

- depends_on_cn：目标声明。

- sets_up_cn：提示无需标签是关键卖点。

- evidence_pointer：Abstract 第3句

### 4. 第4句

- order：4

- section：Abstract

- locator：第4句

- move_code：DESIGN_FEATURE

- paraphrase_cn：该方法不需要历史欺诈标签，能适应定价政策变化，可检测异常并扩展到多元自我报告数据。

- rhetorical_function_cn：列举方法的独特优势，拉开与现有工作的距离。

- depends_on_cn：上句的方法基础。

- sets_up_cn：为摘要总结结果做铺垫。

- evidence_pointer：Abstract 第4句

### 5. 第5句

- order：5

- section：Abstract

- locator：第5句

- move_code：DESIGN_FEATURE

- paraphrase_cn：我们进一步展示了Shapley值与条件密度估计之间的联系，使方法可解释。

- rhetorical_function_cn：强调可解释性，这是实际采用的常见要求。

- depends_on_cn：方法已足够具体。

- sets_up_cn：引出可解释性章节。

- evidence_pointer：Abstract 第5句

### 6. 第6句

- order：6

- section：Abstract

- locator：第6句

- move_code：STUDY_OVERVIEW

- paraphrase_cn：我们报告了车险承保案例研究，其中可虚报驾驶员身份和驾驶记录。

- rhetorical_function_cn：预告实证证据。

- depends_on_cn：方法介绍。

- sets_up_cn：引出案例结果。

- evidence_pointer：Abstract 第6句

### 7. 第7句

- order：7

- section：Abstract

- locator：第7句

- move_code：RESULT

- paraphrase_cn：结果表明该方法能有效检测和预防承保欺诈。

- rhetorical_function_cn：给出摘要级别的结果声明。

- depends_on_cn：案例研究。

- sets_up_cn：让读者期待正文中的证据。

- evidence_pointer：Abstract 第7句

### 8. 第1段第1句

- order：8

- section：Introduction

- locator：第1段第1句

- move_code：CONTEXT

- paraphrase_cn：保费欺诈指在承保时故意虚报信息以获取低保费。

- rhetorical_function_cn：定义研究领域。

- depends_on_cn：无

- sets_up_cn：为列举具体场景提供概念基础。

- evidence_pointer：Introduction P1 S1

### 9. 第1段第2-5句

- order：9

- section：Introduction

- locator：第1段第2-5句

- move_code：PHENOMENON

- paraphrase_cn：列举人寿保险中的吸烟状态、车险中虚报驾龄、工人补偿中的薪资虚报等场景，并引用经济损失数字。

- rhetorical_function_cn：用具体现象和量化损失说明问题的普遍性和严重性。

- depends_on_cn：定义。

- sets_up_cn：后文强调检测必要性。

- evidence_pointer：Introduction P1 S2-S5

### 10. 第2段第1句

- order：10

- section：Introduction

- locator：第2段第1句

- move_code：PRACTICAL_STAKES

- paraphrase_cn：保费欺诈导致保费收入损失并最终提高所有投保人的保费，且虚报数据污染公司的决策模型。

- rhetorical_function_cn：说明现实影响，建立研究紧迫性。

- depends_on_cn：现象描述。

- sets_up_cn：强调检测能力是必需的。

- evidence_pointer：Introduction P2 S1

### 11. 第3段第1句

- order：11

- section：Introduction

- locator：第3段第1句

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：自90年代以来，研究人员已探索数据驱动的欺诈检测方法。

- rhetorical_function_cn：承认已有工作，为缺口做铺垫。

- depends_on_cn：现实问题。

- sets_up_cn：转向现有方法的局限。

- evidence_pointer：Introduction P3 S1

### 12. 第3段第2句

- order：12

- section：Introduction

- locator：第3段第2句

- move_code：LIMITATION

- paraphrase_cn：与许多欺诈不同，保险欺诈不会自我揭示，公司需要主动调查才能获知欺诈状态。

- rhetorical_function_cn：指出关键困难：无标签、无法验证。

- depends_on_cn：现有方法背景。

- sets_up_cn：进一步说明对监督学习的挑战。

- evidence_pointer：Introduction P3 S2

### 13. 第3段第3句

- order：13

- section：Introduction

- locator：第3段第3句

- move_code：LIMITATION

- paraphrase_cn：保险欺诈的非自我揭示性对识别（无标签）和预测（无监督难验证）都构成严重挑战。

- rhetorical_function_cn：深化局限，解释为什么需要新方法。

- depends_on_cn：上句。

- sets_up_cn：为提出无需标签的方法作铺垫。

- evidence_pointer：Introduction P3 S3

### 14. 第3段第4句

- order：14

- section：Introduction

- locator：第3段第4句

- move_code：GAP

- paraphrase_cn：关于承保欺诈的文献局限于单个二进制自我报告变量可能被虚报的受限场景，且不考虑定价政策变化。

- rhetorical_function_cn：明确文献缺口。

- depends_on_cn：上句的挑战。

- sets_up_cn：引出本文贡献。

- evidence_pointer：Introduction P3 S4

### 15. 第4段第1句

- order：15

- section：Introduction

- locator：第4段第1句

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文通过提出一种基于条件密度估计来评估数据虚报风险的新方法，为文献做出贡献。

- rhetorical_function_cn：提出本文目标，直接对接缺口。

- depends_on_cn：缺口陈述。

- sets_up_cn：介绍方法核心和案例。

- evidence_pointer：Introduction P4 S1

### 16. 第5段第1句

- order：16

- section：Introduction

- locator：第5段第1句

- move_code：STUDY_OVERVIEW

- paraphrase_cn：给出论文结构：文献综述、方法、案例、结论。

- rhetorical_function_cn：为读者提供阅读地图。

- depends_on_cn：论文目标。

- sets_up_cn：安排后续各节内容。

- evidence_pointer：Introduction P5 S1

### 17. 第1段第1句

- order：17

- section：Section 2 Literature review

- locator：第1段第1句

- move_code：CONTEXT

- paraphrase_cn：引用Viaene和Dedene对承保欺诈的定义，涵盖申请欺诈、保费欺诈等。

- rhetorical_function_cn：界定研究的理论概念来源。

- depends_on_cn：引言中的定义。

- sets_up_cn：为后文误报模型提供概念术语。

- evidence_pointer：Section 2 P1 S1

### 18. 第2段第1句

- order：18

- section：Section 2 Literature review

- locator：第2段第1句

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：数据虚报问题在经济学文献中有悠久历史，通常以条件密度形式建模。

- rhetorical_function_cn：将问题与计量经济学测量误差文献联系起来，为CDE方法提供理论基础。

- depends_on_cn：概念定义。

- sets_up_cn：引出现有条件密度公式。

- evidence_pointer：Section 2 P2 S1

### 19. 第2段第4-5句

- order：19

- section：Section 2 Literature review

- locator：第2段第4-5句

- move_code：THEORY_INTRO

- paraphrase_cn：描述测量误差文献中的条件密度公式：误差污染的密度是真实密度与误报条件分布的卷积。

- rhetorical_function_cn：为后文方法提供数学模型基础。

- depends_on_cn：前句背景。

- sets_up_cn：比较后续保险文献的简化。

- evidence_pointer：Section 2 P2 S4-S5

### 20. 第2段第6-7句

- order：20

- section：Section 2 Literature review

- locator：第2段第6-7句

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：引用Xia等和Akakpo等首次将统计方法引入保险承保数据虚报研究，建模一个二进制自我报告变量的误报概率，并与损失分布结合。

- rhetorical_function_cn：展示现有工作但点其局限。

- depends_on_cn：条件密度公式。

- sets_up_cn：为指出局限做铺垫。

- evidence_pointer：Section 2 P2 S6-S7

### 21. 第3段第1句

- order：21

- section：Section 2 Literature review

- locator：第3段第1句

- move_code：LIMITATION

- paraphrase_cn：这类方法虽然能估计总体误报率，但不能给出合同级别的风险，且只适用于单向误分类。

- rhetorical_function_cn：明确指出现有统计方法的局限性。

- depends_on_cn：前句模型描述。

- sets_up_cn：引出Xia等的扩展和仍存的限制。

- evidence_pointer：Section 2 P3 S1

### 22. 第3段第2句

- order：22

- section：Section 2 Literature review

- locator：第3段第2句

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：Xia等扩展了框架，加入正确报告的变量，提供依赖合同细节的误报概率，但仅适用于GLM中的二元离散因子。

- rhetorical_function_cn：承认进展，为继续指出不足做铺垫。

- depends_on_cn：前句局限。

- sets_up_cn：继续积累缺口。

- evidence_pointer：Section 2 P3 S2

### 23. 第3段第3-6句

- order：23

- section：Section 2 Literature review

- locator：第3段第3-6句

- move_code：LIMITATION

- paraphrase_cn：现有模型假设不现实且有限：实际中多个变量可能连续或离散，而且定价政策变化会改变误报方向，损失信息也有延迟。

- rhetorical_function_cn：从现实性、动态性、数据可得性三方面强化缺口。

- depends_on_cn：上句对扩展工作局限的描述。

- sets_up_cn：为CDE方法提供动机。

- evidence_pointer：Section 2 P3 S3-S6

### 24. 第4段第1句

- order：24

- section：Section 2 Literature review

- locator：第4段第1句

- move_code：REQUIREMENT

- paraphrase_cn：当存在验证数据时，误报估计可公式化为CDE问题。

- rhetorical_function_cn：引入验证数据和CDE的关联，作为方法核心依据。

- depends_on_cn：前述局限。

- sets_up_cn：引出CDE方法的具体选择。

- evidence_pointer：Section 2 P4 S1

### 25. 第4段第2-3句

- order：25

- section：Section 2 Literature review

- locator：第4段第2-3句

- move_code：THEORY_INTRO

- paraphrase_cn：对于二进制目标，后验概率等于条件均值，适用已知方法；但连续多变量Z的CDE是较少研究的统计问题。

- rhetorical_function_cn：指出CDE的技术空白。

- depends_on_cn：CDE公式。

- sets_up_cn：介绍两类CDE方法。

- evidence_pointer：Section 2 P4 S2-S3

### 26. 第4段第4句

- order：26

- section：Section 2 Literature review

- locator：第4段第4句

- move_code：THEORY_INTRO

- paraphrase_cn：FlexCode通过正交基投影将CDE转化为多个条件均值回归问题。

- rhetorical_function_cn：介绍第一种可行方法。

- depends_on_cn：技术空白。

- sets_up_cn：为后文使用FlexCode做铺垫。

- evidence_pointer：Section 2 P4 S4

### 27. 第4段第5句

- order：27

- section：Section 2 Literature review

- locator：第4段第5句

- move_code：THEORY_INTRO

- paraphrase_cn：RFCDE将CDE loss作为随机森林分裂准则，可视为加权核密度方法。

- rhetorical_function_cn：介绍第二种方法。

- depends_on_cn：技术空白。

- sets_up_cn：引出两种方法的对比。

- evidence_pointer：Section 2 P4 S5

### 28. 第4段最后一句

- order：28

- section：Section 2 Literature review

- locator：第4段最后一句

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：文章聚焦FlexCode和RFCDE，因为替代方法（如分位数回归森林、核密度估计）在可微性、多元性、规模上存在不足。

- rhetorical_function_cn：解释为什么选用这两种技术。

- depends_on_cn：前两句对方法的介绍。

- sets_up_cn：为方法章节做铺垫。

- evidence_pointer：Section 2 P4 S7

### 29. 第1句

- order：29

- section：Section 3.1

- locator：第1句

- move_code：MECHANISM

- paraphrase_cn：定义真实承保信息U、报告信息U*和保费μ(U*)，承保人的任务是判断报告是否真实且不存在因保费降低而虚报的情况。

- rhetorical_function_cn：建立模型符号和业务目标。

- depends_on_cn：文献中的定义。

- sets_up_cn：为风险定义提供表达基础。

- evidence_pointer：Section 3.1 S1

### 30. 第3句

- order：30

- section：Section 3.1

- locator：第3句

- move_code：REQUIREMENT

- paraphrase_cn：定义自报告变量Z和正确测量变量X，将保费欺诈风险正式定义为P(μ(Z*,X)<μ(Z,X))。

- rhetorical_function_cn：将业务风险转成统计概率。

- depends_on_cn：符号定义。

- sets_up_cn：为条件版本做准备。

- evidence_pointer：Section 3.1 S3

### 31. 第1句

- order：31

- section：Section 3.3

- locator：第1句

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：模型的主要目标是为给定申请提供基于自报信息的风险评分。

- rhetorical_function_cn：明确方法的应用目标。

- depends_on_cn：风险定义。

- sets_up_cn：引导出条件风险公式。

- evidence_pointer：Section 3.3 S1

### 32. 第3句

- order：32

- section：Section 3.3

- locator：第3句

- move_code：MECHANISM

- paraphrase_cn：条件保费欺诈风险等于在给定X和Z*条件下，真实Z使保费更高的概率，可表示为指示函数与f(z|x)的积分。

- rhetorical_function_cn：给出核心计算式，将风险与CDE连接。

- depends_on_cn：概率定义。

- sets_up_cn：为需要估计f(z|x)做了铺垫。

- evidence_pointer：Section 3.3 Equation (2)

### 33. 第1句

- order：33

- section：Section 3.4

- locator：第1句

- move_code：THEORY_INTRO

- paraphrase_cn：FlexCode通过正交基投影将CDE问题转化为一系列条件期望估计。

- rhetorical_function_cn：介绍方法的技术细节。

- depends_on_cn：方法选型。

- sets_up_cn：后续讨论basis size和损失。

- evidence_pointer：Section 3.4 P1 S1

### 34. 第3段第1句

- order：34

- section：Section 3.4

- locator：第3段第1句

- move_code：LIMITATION

- paraphrase_cn：FlexCode假设所有x使用相同basis size，且仅在CDE loss上选择basis可能误导。

- rhetorical_function_cn：标记方法局限，为引入补充指标埋伏笔。

- depends_on_cn：FlexCode介绍。

- sets_up_cn：引出HDR loss。

- evidence_pointer：Section 3.4 P3 S1

### 35. 第6段第1句

- order：35

- section：Section 3.4

- locator：第6段第1句

- move_code：LIMITATION

- paraphrase_cn：FlexCode和RFCDE虽然可在理论上扩展到多元响应，但不提供多变量basis size的交叉验证策略，且高维积分计算困难。

- rhetorical_function_cn：指出技术在多元场景的限制。

- depends_on_cn：前面提及张量积扩展。

- sets_up_cn：为后文展示作者的扩展做铺垫。

- evidence_pointer：Section 3.4 P6 S1

### 36. 第8段第1句

- order：36

- section：Section 3.4

- locator：第8段第1句

- move_code：LIMITATION

- paraphrase_cn：CDE loss本身没有直观解释，不足以单独评估密度估计质量。

- rhetorical_function_cn：指出评价指标缺陷。

- depends_on_cn：前段对CDE loss的公式化。

- sets_up_cn：引出下一节HDR指标。

- evidence_pointer：Section 3.4 P8 S1

### 37. 第1句

- order：37

- section：Section 3.5

- locator：第1句

- move_code：THEORY_INTRO

- paraphrase_cn：HDR在CDE文献中用于检查校准。

- rhetorical_function_cn：引入新评价工具的理论来源。

- depends_on_cn：上一节的局限。

- sets_up_cn：定义HDR coverage loss。

- evidence_pointer：Section 3.5 P1 S1

### 38. 第5段第1句

- order：38

- section：Section 3.5

- locator：第5段第1句

- move_code：DESIGN_FEATURE

- paraphrase_cn：HDR coverage loss定义为理论覆盖与实际覆盖差异的平方积分，约等于0时表示估计良好。

- rhetorical_function_cn：提出具体的补充指标。

- depends_on_cn：HDR定义。

- sets_up_cn：用于后文basis size选择。

- evidence_pointer：Section 3.5 P5

### 39. 第7段第1句

- order：39

- section：Section 3.5

- locator：第7段第1句

- move_code：DESIGN_FEATURE

- paraphrase_cn：利用CDE和HDR可以识别条件异常值，并可映射到‘交通灯’方法促进非专家沟通。

- rhetorical_function_cn：扩展方法功能到异常检测和治理策略。

- depends_on_cn：HDR定义。

- sets_up_cn：在案例中展示交通灯解释。

- evidence_pointer：Section 3.5 P7

### 40. 第1句

- order：40

- section：Section 3.6

- locator：第1句

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：GLM是保险定价的标准，具有乘法形式。

- rhetorical_function_cn：引入领域定价知识。

- depends_on_cn：方法需要定价函数。

- sets_up_cn：简化风险公式。

- evidence_pointer：Section 3.6 P1 S1

### 41. 第2句

- order：41

- section：Section 3.6

- locator：第2句

- move_code：MECHANISM

- paraphrase_cn：乘法形式下，风险公式只依赖相对价格因子μz，无需完整GLM。

- rhetorical_function_cn：展示实际计算上的便利。

- depends_on_cn：前句GLM知识。

- sets_up_cn：指导案例中如何计算风险分数。

- evidence_pointer：Section 3.6 Equation (7)

### 42. 第3段第1句

- order：42

- section：Section 3.6

- locator：第3段第1句

- move_code：DESIGN_FEATURE

- paraphrase_cn：提出阶段式验证框架，随着自报告值逐步验证，风险分数可以更新。

- rhetorical_function_cn：增强方法的实际指导意义。

- depends_on_cn：已验证变量成为条件信息。

- sets_up_cn：为案例中的驾驶记录顺序验证做铺垫。

- evidence_pointer：Section 3.6 P3 S1

### 43. 第1句

- order：43

- section：Section 4.1

- locator：第1句

- move_code：CONTEXT

- paraphrase_cn：车险中两个自我报告维度对定价最关键：驾驶员身份（驾龄和年龄）和驾驶记录（奖金-惩罚系统）。

- rhetorical_function_cn：将方法应用于具体业务变量。

- depends_on_cn：背景知识。

- sets_up_cn：定义案例中的Z变量。

- evidence_pointer：Section 4.1 P1 S1

### 44. 第2句

- order：44

- section：Section 4.1

- locator：第2句

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：数据集包含57,000份已验证合同报价，4年历史，X为第三方认证的车辆信息，Z为自我报告信息。

- rhetorical_function_cn：描述实证数据来源和背景。

- depends_on_cn：前面方法需要验证数据。

- sets_up_cn：为后文四种场景提供数据基础。

- evidence_pointer：Section 4.1 P2 S1

### 45. 第4段第1句

- order：45

- section：Section 4.1

- locator：第4段第1句

- move_code：STUDY_OVERVIEW

- paraphrase_cn：下文展示四种自报告变量设置：单变量连续、双变量连续、混合类型、单变量有序。

- rhetorical_function_cn：预告实证部分的组织。

- depends_on_cn：数据描述。

- sets_up_cn：引导各小节。

- evidence_pointer：Section 4.1 P4 S1

### 46. 第1段第1句

- order：46

- section：Section 4.2.1

- locator：第1段第1句

- move_code：CONTEXT

- paraphrase_cn：驾照年龄的边缘分布提供基线信息。

- rhetorical_function_cn：引入先验密度作为后验对照。

- depends_on_cn：数据Z。

- sets_up_cn：说明为何边缘分布不足。

- evidence_pointer：Section 4.2.1 P1 S1

### 47. 第2段第1句

- order：47

- section：Section 4.2.1

- locator：第2段第1句

- move_code：LIMITATION

- paraphrase_cn：边缘分布的高密度区域过宽，不能有效验证单个合同。

- rhetorical_function_cn：为加入X创造条件。

- depends_on_cn：边缘分布不足。

- sets_up_cn：引出条件密度估计。

- evidence_pointer：Section 4.2.1 P2 S1

### 48. 第2段第2句

- order：48

- section：Section 4.2.1

- locator：第2段第2句

- move_code：REQUIREMENT

- paraphrase_cn：添加车辆信息X来估计条件密度f(z|x)，期望对特定车辆形成更窄的高密度区域。

- rhetorical_function_cn：说明条件密度的价值。

- depends_on_cn：边缘分布不足。

- sets_up_cn：用KL散度衡量X的增益。

- evidence_pointer：Section 4.2.1 P2 S2

### 49. 第3段第1句

- order：49

- section：Section 4.2.1

- locator：第3段第1句

- move_code：MECHANISM

- paraphrase_cn：用KL散度度量后验与先验的差异，衡量X对自报告值的预测能力。

- rhetorical_function_cn：提供量化X增益的指标。

- depends_on_cn：条件密度估计。

- sets_up_cn：用于评价模型和特征价值。

- evidence_pointer：Section 4.2.1 P3 S1

### 50. 第4段第1句

- order：50

- section：Section 4.2.1

- locator：第4段第1句

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：FlexCode需要设置基类型、基大小和回归模型参数，基类型选择Fourier基，基大小通过CDE loss交叉验证，回归用随机森林。

- rhetorical_function_cn：说明参数选择和实现细节。

- depends_on_cn：FlexCode方法。

- sets_up_cn：解释图2的结果。

- evidence_pointer：Section 4.2.1 P4

### 51. 第5段第1句

- order：51

- section：Section 4.2.1

- locator：第5段第1句

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：使用5折交叉验证确定随机森林参数，但参数最优性不保证对CDE最优，该步仅作起点。

- rhetorical_function_cn：说明参数选择策略的合理性和方法论。

- depends_on_cn：随机森林算法。

- sets_up_cn：为对比三种模型做准备。

- evidence_pointer：Section 4.2.1 P5 S1

### 52. 第6段第1句

- order：52

- section：Section 4.2.1

- locator：第6段第1句

- move_code：CONTEXT

- paraphrase_cn：在承保决策中，需要理解条件密度以评估估计合理性和解释性，仅用单一指标不够。

- rhetorical_function_cn：强调多指标评价的必要性。

- depends_on_cn：模型估计。

- sets_up_cn：引出图2的覆盖率图。

- evidence_pointer：Section 4.2.1 P6 S1

### 53. 图2描述段

- order：53

- section：Section 4.2.1

- locator：图2描述段

- move_code：RESULT

- paraphrase_cn：图2中FlexCode和RFCDE的覆盖率图接近对角线，但FlexCode的KL散度大于RFCDE，说明FlexCode对X更敏感。

- rhetorical_function_cn：报告主要实证结果。

- depends_on_cn：图2。

- sets_up_cn：解释原因并推进到多变量。

- evidence_pointer：Figure 2 及前文

### 54. 图3后段

- order：54

- section：Section 4.2.1

- locator：图3后段

- move_code：MECHANISM

- paraphrase_cn：KL差异大的样本说明车辆信息提供了更多关于驾驶员经验的信息。

- rhetorical_function_cn：解释KL结果的含义。

- depends_on_cn：图3的示例。

- sets_up_cn：为特征选择讨论铺路。

- evidence_pointer：Figure 3 后段

### 55. 第2段第1句

- order：55

- section：Section 4.2.2

- locator：第2段第1句

- move_code：STUDY_OVERVIEW

- paraphrase_cn：这里用RFCDE展示双变量连续示例。

- rhetorical_function_cn：预告本小节目的。

- depends_on_cn：前面单变量验证。

- sets_up_cn：讲带宽矩阵参数化。

- evidence_pointer：Section 4.2.2 P2 S1

### 56. 第3段第1句

- order：56

- section：Section 4.2.2

- locator：第3段第1句

- move_code：DESIGN_FEATURE

- paraphrase_cn：带宽矩阵可用约束（对角）或非约束（半正定对称）参数化，但非约束参数化可能数值不稳定，因此简单策略是用先验密度的带宽固定。

- rhetorical_function_cn：给出处理多变量核密度稳定性的实用方案。

- depends_on_cn：RFCDE多变量核。

- sets_up_cn：展示图4-5的密度估计。

- evidence_pointer：Section 4.2.2 P3

### 57. 第1段第1句

- order：57

- section：Section 4.2.3

- locator：第1段第1句

- move_code：CONTEXT

- paraphrase_cn：当自报变量为混合类型（连续+离散）时，计算风险需要联合条件密度估计。

- rhetorical_function_cn：提出更复杂场景。

- depends_on_cn：之前双变量连续。

- sets_up_cn：引出FlexCode的混合基扩展。

- evidence_pointer：Section 4.2.3 P1 S1

### 58. 第3段第1句

- order：58

- section：Section 4.2.3

- locator：第3段第1句

- move_code：DESIGN_FEATURE

- paraphrase_cn：用傅里叶基处理连续变量、Haar基处理离散变量，通过张量积实现FlexCode的混合类型扩展。

- rhetorical_function_cn：描述具体扩展方法。

- depends_on_cn：原始FlexCode和离散变量性质。

- sets_up_cn：用CDE loss和HDR loss选择basis size。

- evidence_pointer：Section 4.2.3 P3

### 59. 图6-7后段

- order：59

- section：Section 4.2.3

- locator：图6-7后段

- move_code：RESULT

- paraphrase_cn：图6-7显示CDE loss和HDR coverage loss均在basis size=3时最小，且后处理仅做去负和缩放。

- rhetorical_function_cn：报告超参数选择结果，并验证互补指标一致。

- depends_on_cn：混合类型扩展。

- sets_up_cn：为欺诈分数应用提供最优模型。

- evidence_pointer：Figures 6 and 7

### 60. 第1段第1句

- order：60

- section：Section 4.3

- locator：第1段第1句

- move_code：STUDY_OVERVIEW

- paraphrase_cn：在简化的单变量设置中应用保费欺诈风险分数。

- rhetorical_function_cn：转向应用目标验证。

- depends_on_cn：前面CDE估计基础。

- sets_up_cn：描述应用设置和数据。

- evidence_pointer：Section 4.3 P1 S1

### 61. 第2段第1句

- order：61

- section：Section 4.3

- locator：第2段第1句

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用于评估的数据集包含73,000份申请（含被验证和拒绝的），其中部分已验证用于训练CDE。

- rhetorical_function_cn：说明应用数据集。

- depends_on_cn：欺诈分数需要CDE模型。

- sets_up_cn：为图9-10分布对比做铺垫。

- evidence_pointer：Section 4.3 P2 S1

### 62. 第3段第1句

- order：62

- section：Section 4.3

- locator：第3段第1句

- move_code：RESULT

- paraphrase_cn：图9给出一般申请的风险分数分布，而图10给出专家标记的高风险子段分数分布，两者差异表明模型能较好分类可疑申请。

- rhetorical_function_cn：报告应用层面的主要结果。

- depends_on_cn：图9-10。

- sets_up_cn：为可解释性讨论做过渡。

- evidence_pointer：Section 4.3 图9-10段

### 63. 第1段第1句

- order：63

- section：Section 4.4

- locator：第1段第1句

- move_code：CONTEXT

- paraphrase_cn：模型可解释性对其采用至关重要，即使对普通回归模型也具挑战。

- rhetorical_function_cn：引入可解释性问题。

- depends_on_cn：应用有效性的背景。

- sets_up_cn：为Shapley值引入做铺垫。

- evidence_pointer：Section 4.4 P1 S1

### 64. 第2段第1句

- order：64

- section：Section 4.4

- locator：第2段第1句

- move_code：THEORY_INTRO

- paraphrase_cn：Shapley值是解释黑箱模型的流行方法，给每个特征分配对预测偏差的贡献。

- rhetorical_function_cn：介绍可解释性理论工具。

- depends_on_cn：可解释性需求。

- sets_up_cn：提出将Shapley扩展到CDE。

- evidence_pointer：Section 4.4 P2 S1

### 65. 第3段第1句

- order：65

- section：Section 4.4

- locator：第3段第1句

- move_code：DESIGN_FEATURE

- paraphrase_cn：本文研究FlexCode的可解释性，提出CDE的加性分解形式。

- rhetorical_function_cn：提出具体可解释方法。

- depends_on_cn：FlexCode的正交分解。

- sets_up_cn：在附录证明命题。

- evidence_pointer：Section 4.4 P3 S1

### 66. 图12后段

- order：66

- section：Section 4.4

- locator：图12后段

- move_code：RESULT

- paraphrase_cn：示例中模型相对先验预测了更高的新手司机密度，变量贡献显示功率、车高、车长、车龄对低驾龄区间有正贡献。

- rhetorical_function_cn：展示可解释性的实际输出。

- depends_on_cn：图12。

- sets_up_cn：说明解释在治理和建模中的用途。

- evidence_pointer：Figure 12 后段

### 67. 最后一段

- order：67

- section：Section 4.4

- locator：最后一段

- move_code：PRACTICAL_STAKES

- paraphrase_cn：模型解释可作为进一步调查合同或拒绝申请的理由，也可用于特征空间约简和新变量评估。

- rhetorical_function_cn：说明可解释性的实际价值。

- depends_on_cn：可解释性结果。

- sets_up_cn：过渡到讨论。

- evidence_pointer：Section 4.4 末段

### 68. 第1段第1句

- order：68

- section：Section 4.5 Discussion

- locator：第1段第1句

- move_code：RESULT

- paraphrase_cn：我们看到CDE可以用于估计多种格式（多元、混合类型）自我报告信息的可信度。

- rhetorical_function_cn：总结实证发现。

- depends_on_cn：四个应用场景。

- sets_up_cn：讨论方法选择。

- evidence_pointer：Section 4.5 P1 S1

### 69. 第2段第1句

- order：69

- section：Section 4.5

- locator：第2段第1句

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：CDE技术的选择取决于自我报告数据的性质。

- rhetorical_function_cn：明确方法适用边界。

- depends_on_cn：实证经验。

- sets_up_cn：指出简单场景可选用更简单方法。

- evidence_pointer：Section 4.5 P2 S1

### 70. 第2段第2句

- order：70

- section：Section 4.5

- locator：第2段第2句

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：方法检测欺诈的效率取决于自我报告值能被正确测量值预测的程度。

- rhetorical_function_cn：强调外部条件对有效性的影响。

- depends_on_cn：CDE本质。

- sets_up_cn：提醒可预测性限制。

- evidence_pointer：Section 4.5 P2 S2

### 71. 第1段第1句

- order：71

- section：Section 5 Conclusions

- locator：第1段第1句

- move_code：CONTRIBUTION

- paraphrase_cn：本文将保费欺诈检测公式化为条件密度估计问题。

- rhetorical_function_cn：高度概括核心贡献。

- depends_on_cn：全文。

- sets_up_cn：扩展贡献列表。

- evidence_pointer：Section 5 P1 S1

### 72. 第2段第1句

- order：72

- section：Section 5 Conclusions

- locator：第2段第1句

- move_code：CONTRIBUTION

- paraphrase_cn：该公式使我们能够明确估计自我报告变量的分布及其与定价政策的关系，从而在机会-动机框架下产出风险评价。

- rhetorical_function_cn：将方法与既有理论框架关联。

- depends_on_cn：核心公式。

- sets_up_cn：强调理论贡献。

- evidence_pointer：Section 5 P2 S1

### 73. 第3段第1句

- order：73

- section：Section 5 Conclusions

- locator：第3段第1句

- move_code：CONTRIBUTION

- paraphrase_cn：CDE也可用于条件异常检测，通过HDR和交通灯方法识别特定维度的异常。

- rhetorical_function_cn：扩展方法应用范围。

- depends_on_cn：HDR部分。

- sets_up_cn：增加贡献维度。

- evidence_pointer：Section 5 P3 S1

### 74. 第4段第1句

- order：74

- section：Section 5 Conclusions

- locator：第4段第1句

- move_code：CONTRIBUTION

- paraphrase_cn：我们讨论了连续变量大数据集上混合类型CDE的最新技术，提出HDR loss作为互补评价，并展示了Shapley值的适配。

- rhetorical_function_cn：汇总技术贡献。

- depends_on_cn：方法部分。

- sets_up_cn：为未来工作铺垫。

- evidence_pointer：Section 5 P4 S1

### 75. 第5段第1句

- order：75

- section：Section 5 Conclusions

- locator：第5段第1句

- move_code：CONTRIBUTION

- paraphrase_cn：我们还讨论了合同的阶段式验证，并指出理解各阶段的预测性可帮助改进合同验证的稳健性。

- rhetorical_function_cn：强调设计知识贡献。

- depends_on_cn：阶段式验证部分。

- sets_up_cn：连接未来研究。

- evidence_pointer：Section 5 P5 S1

### 76. 第6段第1句

- order：76

- section：Section 5 Conclusions

- locator：第6段第1句

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：未来研究可探索使用每份合同的实际损失作为补充信息，桥接本文方法与[13,14]的方法。

- rhetorical_function_cn：指出当前方法未利用损失标签，并提供未来方向。

- depends_on_cn：当前方法未使用损失信息。

- sets_up_cn：结束结论。

- evidence_pointer：Section 5 P6 S1

### 77. 第7段第1句

- order：77

- section：Section 5 Conclusions

- locator：第7段第1句

- move_code：PRACTICAL_STAKES

- paraphrase_cn：保险公司可使用本方法改进承保验证决策，例如触发自动核保系统的验证。

- rhetorical_function_cn：明确实际用途。

- depends_on_cn：方法有效性。

- sets_up_cn：最后扩展到其他领域。

- evidence_pointer：Section 5 P7 S1

### 78. 第8段第1句

- order：78

- section：Section 5 Conclusions

- locator：第8段第1句

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：方法也可应用于其他非保险领域的申请欺诈，如贷款申请收入夸大或会计不当行为。

- rhetorical_function_cn：推广方法适用边界。

- depends_on_cn：方法一般性。

- sets_up_cn：结束全文。

- evidence_pointer：Section 5 P8 S1

## 写作技术

- gap_construction_cn：文章通过三层递进建立缺口：首先定义保费欺诈及其危害，其次指出保险欺诈“非自我揭示”导致标签缺失，最后聚焦到现有underwriting fraud文献的局限（单一二元变量、单向误分类、静态定价、无应用导向）。这样逐步收窄，使读者看到现有方法无法满足实际需要。

- signposting_cn：引言末段给出完整论文结构；每个实证小节开头有“In this section, we...”式预告；第4.1节末列举四种数据类型；第4.2.2和4.2.3开头也说明本节目标。路标频繁，方便读者追踪。

- transition_logic_cn：段间过渡常从“局限”转向“因此我们引入…”，如CDE loss不足→引入HDR loss；从单变量结果到多变量扩展用“类似地”“当…时”自然推进；从密度估计到欺诈分数用“本节我们应用…”承上启下。

- claim_evidence_rhythm_cn：技术性声明后紧跟公式和解释，实证声明后紧跟图表和描述。例如在提出HDR loss后立即用图6-7在案例中验证；在声称欺诈分数“有效”后立即展示图9-10的分布对比。但有时主张强度超过证据，如用“有效”描述分布差异而未做统计检验。

- benchmark_narrative_cn：本文没有传统benchmark，而是通过三种方式建立对比：1) 用先验密度作为基线展示X的增量价值；2) 用vanilla random forest作为条件均值参考，与CDE方法对比；3) 用一般申请样本作为高风险子段的对照。这些对比使得CDE的校准性和分数的判别力得以凸显。

- theory_return_cn：结论部分将风险公式与opportunity-motivation框架连接，将HDR异常检测与治理政策联系，将Shapley分解回归到可解释性理论；讨论部分强调方法效率取决于X对Z的可预测性，这是对CDE理论边界的反思。

- contribution_positioning_cn：在引言末尾和结论开头重复声明“首次提出CDE视角”“无需标签”“适应定价变化”“支持多变量混合类型”，从多个维度定位贡献，而不是仅依赖一个技术点。

- novelty_protection_cn：通过强调现有工作的受限假设（二进制、单向、静态）来凸显本文的一般性；同时提供案例和附录中的计算复杂度说明，使“通用方法”落于“可实施系统”，防止被视为一次性性能报告。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：定义业务问题并用具体现象和数据说明其严重性。

- research_job_cn：识别一个实际业务中“非自我揭示”且标签缺失的欺诈/风险问题。

- required_evidence_cn：官方统计、行业报告或具体场景描述，证明问题规模和普遍性。

- transition_to_next_cn：从业务问题转向现有技术如何不足。

#### 2. 2

- step：2

- writing_job_cn：综述现有方法并以“局限列表”方式建立缺口。

- research_job_cn：系统梳理文献，提取出若干关键假设（如单变量、二元、静态）作为缺口。

- required_evidence_cn：引文支撑每个局限，且局限之间要有递进关系。

- transition_to_next_cn：用“因此本文贡献是…”直接切入自己的方法。

#### 3. 3

- step：3

- writing_job_cn：将问题形式化为数学/统计表达式，并将核心变量和业务目标对应。

- research_job_cn：定义变量空间，推导风险或效果的概率/统计表示。

- required_evidence_cn：公式推导要能与后续案例中的操作对应。

- transition_to_next_cn：从统一定义引导到需要估计的密度，然后介绍可用技术。

#### 4. 4

- step：4

- writing_job_cn：介绍所选方法与评价指标，说明为什么这些方法适合问题。

- research_job_cn：从方法库中选择满足缺口要求的工具，并定义评价指标（尤其是补充指标）。

- required_evidence_cn：已有方法对混合类型、多元、大数据的适用性证明。

- transition_to_next_cn：宣布要用真实数据验证方法。

#### 5. 5

- step：5

- writing_job_cn：描述数据来源、变量定义、训练/测试划分。

- research_job_cn：获取或构造包含已验证真值的数据集，并清楚划分X和Z。

- required_evidence_cn：数据时间跨度、样本量、变量维度、第三方验证方式等详细信息。

- transition_to_next_cn：从数据描述进入具体应用场景。

#### 6. 6

- step：6

- writing_job_cn：按复杂度递进展示多个应用场景（单变量→多变量→混合类型）。

- research_job_cn：在每个场景中运行方法，用共同指标评价，并展示图表。

- required_evidence_cn：每个场景的评估结果（覆盖率、损失、样本预测图）。

- transition_to_next_cn：在完成密度估计后转向最终业务指标——风险分数。

#### 7. 7

- step：7

- writing_job_cn：将估计的密度与业务决策函数（如定价）结合，生成决策分数并展示判别力。

- research_job_cn：计算分数，并通过专家标记子段或其他代理标签展示区分度。

- required_evidence_cn：分布对比图或AUC等指标。

- transition_to_next_cn：分数有效后，讨论可解释性和采用障碍。

#### 8. 8

- step：8

- writing_job_cn：提供可解释性方法并给出示例，说明如何支持决策。

- research_job_cn：将解释框架（如Shapley）适配到所提模型，并给出理论保证或示例。

- required_evidence_cn：理论命题或证明，以及单样本可视化。

- transition_to_next_cn：总结贡献、边界和未来方向。

### most_transferable_moves_cn

1. 通过‘非自我揭示’或‘无标签’来凸显问题与一般预测的差异，从而合理规避监督学习。

2. 将业务风险定义为某个条件概率，再拆解为需要估计的统计量。

3. 在方法章节中不止于介绍现有工具，还指出其不足（如CDE loss无意义），从而为引入补充指标铺路。

4. 将评价指标与超参数选择直接挂钩，让模型选择有据可依。

5. 从单变量到多变量到混合类型的渐进展示，让方法能力层层递进。

### resource_intensive_or_nonstandard_parts_cn

1. 需要保险公司内部4年已验证合同报价数据（57,000份）和申请样本（73,000份），通常不易获得。

2. 需要第三方验证的车辆数据作为X，确保X确实是‘正确测量’的。

3. 专家标记风险子段需要业务专家参与，具有主观性且不可大规模复制。

4. 计算训练和验证需要训练I个回归模型，I为basis size，存在计算成本（虽然可并行）。

### what_not_to_copy_superficially_cn

1. 不能只写‘CDE可用于欺诈检测’而不展示具体的风险公式和密度估计流程。

2. 不能宣称‘无需标签’却没有验证数据如何获得和如何保证验证质量。

3. 不能只展示分数直方图差异就声称‘有效’，应补充统计检验或ROC等指标。

4. 不能只在结论中说‘适应定价变化’而不实验或模拟定价变化的情景。

- single_best_description_of_the_routine_cn：以‘非自我揭示’业务问题为入口，将检测目标形式化为条件概率，用条件密度估计作为引擎，辅以补充评价指标和可解释性，再通过真实数据上的多场景渐进验证，最终将局部结果上升为可复用设计知识。

## 分析边界

文章中的图表（图1-15）未提供数值数据，句子级位置基于文本段落推断，可能与实际分页有偏差；没有提取附录中的详细证明过程，但基于命题陈述进行了理解；未对参考文献中的细节进行验证；对方法性能的量化评估（如AUC）论文本身未提供，因此无法补充。
