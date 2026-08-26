# The effect of interactive analytical dashboard features on situation awareness and task performance

- 作者：Mario Nadj; Alexander Maedche; Christian Schieder
- 年份 / 期刊：2020 / Decision Support Systems
- DOI：10.1016/j.dss.2020.113322
- 源文件：10216_2020_the-effect-of-interactive-analytical-dashboard-features-on-situation-awareness-and-task-performa.md
- 论文主类型：theory_derived_artifact_experiment
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.75

## 文章级论证概况

- 核心问题：在运营决策支持系统中，交互式分析仪表板特征（what-if分析）如何影响运营决策者的态势感知（SA）和任务绩效？

- 制品与设计：作者构建了两款可比较的仪表板：交互式仪表板（无what-if，提供可排序表格、条形图、下钻/上卷/筛选等手工数据分析功能）与交互式分析仪表板（在交互式基础上增加what-if模拟区，可视化瓶颈组件及其关键性）。

- 客观结果：83名被试的组内实验室实验显示：交互式分析设计的SAGAT得分显著更低（0.39 vs 0.53），注视时长和次数显著更低；但规划错误显著更少（2.18 vs 2.82），心理负荷无显著差异。H1和H2得到支持；H3在SAGAT上得到支持，而眼动数据仅在交互式分析设计中支持该关联。

- 核心贡献：将what-if分析特征与SA和任务绩效联系起来，首次用SAGAT与眼动结合的大样本实验揭示“提高绩效但降低SA”的权衡，并将结果转化为缓解out-of-the-loop问题的仪表板设计启示。

- 整篇论证链：作者从运营DSS中静态仪表板难以处理复杂多维数据、交互仪表板又增加认知负荷的张力出发，指出what-if等交互式分析特征虽然被寄予厚望，却缺乏对其认知影响的实证。以Endsley的SA理论为镜头，提出三种假设：交互式分析仪表板因自动化建议和用户过度信任会降低SA（H1），但因减轻手工分析认知需求、快速指向瓶颈信息而提升任务绩效（H2），并假设SA正向关联绩效（H3）。为检验这些假设，作者在APS生产计划场景中构建两款可比较的仪表板，用83名研究生的组内实验室实验，同时以SAGAT冻结法、眼动注视时长/次数、规划错误和NASA-TLX测量。结果显示H1和H2得到支持，H3在SAGAT上得到支持而眼动测量只在交互式分析设计中支持；心理负荷无差异。讨论将这种“绩效提升但SA下降”解释为out-of-loop风险，并强调只有当底层优化模型能处理当前情境时绩效收益才成立，最后把结果转成保持人在回路、增加透明度、SA审计和训练等设计启示。

## 类型与写作弧线判定

- 论文主类型判定：文章以Endsley的SA理论为理论镜头，推导what-if分析特征对SA和任务绩效的差异化影响，然后构建两种仪表板制品并通过实验室实验检验假设；贡献主要是理论推导的因果关系证据，而非正式设计科学原则的开发。

- 主导写作弧线判定：论文从运营仪表板的问题出发，引入SA理论，将其转化为三个假设和两种仪表板设计，以组内实验检验，最后回到理论含义、边界条件和设计启示，形成完整的问题—理论—设计—检验—返回理论的弧线。

## 研究开展程序

- study_or_phase_count：5

- 研究阶段总序列：论文先进行理论建模阶段（阶段1），再进入制品构建阶段（阶段2），随后进行预测试与领域专家反馈（阶段3），然后开展核心实验室实验（阶段4），最后进行统计稳健性、测量比较和关系分析（阶段5）。各阶段依次把what-if特征从一个概念性差距转变成可操作的自变量、可测量的SA/绩效结果和可辩护的设计启示。

### studies_or_phases

#### 1. 理论与假设模型构建

- order：1

- name_cn：理论与假设模型构建

- question_cn：交互式分析特征与SA、任务绩效之间在理论上应是什么关系？

- inputs_and_setting_cn：SA理论文献、仪表板研究、交互式优化方法分类、what-if与决策绩效的冲突证据

- designed_or_compared_object_cn：研究模型与三个假设（H1、H2、H3），尚未构建制品

- baseline_control_or_counterfactual_cn：概念上将交互式仪表板（无what-if）作为比较基准

##### objective_metrics

（空）

- analysis_method_cn：文献综合与理论推理

- main_result_cn：提出假设：交互式分析设计降低SA、提升任务绩效；SA正向关联任务绩效

- argumentative_role_cn：界定研究缺口，确立SA作为理论透镜和核心结果变量

- remaining_uncertainty_cn：假设尚未得到实证检验，what-if特征的影响方向和机制只是理论预期

- link_to_next_phase_cn：需要将“有/无what-if”转成可操作、可比较的仪表板设计

##### evidence_pointers

1. Section 2

2. Section 3

3. Figure 2

#### 2. 双仪表板制品设计与领域适配

- order：2

- name_cn：双仪表板制品设计与领域适配

- question_cn：如何把what-if特征的有无具体化为两种可比较的仪表板？

- inputs_and_setting_cn：仪表板组件/类型分类、交互式优化方法分类、APS生产计划领域知识、生产计划员建议

- designed_or_compared_object_cn：交互式仪表板（无what-if）与交互式分析仪表板（有what-if模拟区）

- baseline_control_or_counterfactual_cn：交互式仪表板作为无what-if的控制条件

##### objective_metrics

（空）

- analysis_method_cn：系统构建、专家反馈

- main_result_cn：生成两款共享相同APS任务、目标和约束条件，但在分析能力上不同的仪表板

- argumentative_role_cn：将自变量从概念层面转化为可操纵的实验条件

- remaining_uncertainty_cn：尚不清楚被试能否理解任务、两款设计能否在实际实验中产生差异

- link_to_next_phase_cn：需要通过预测试和专家反馈来检验任务可理解性和设计真实性

##### evidence_pointers

1. Section 4.2

2. Section 4.3

3. Figure 3

4. Figure 4

#### 3. 预测试与领域专家反馈

- order：3

- name_cn：预测试与领域专家反馈

- question_cn：实验任务、仪表板设计和测量材料是否可理解、贴近现实？

- inputs_and_setting_cn：实验设置试测、生产计划员反馈、小规模被试训练

- designed_or_compared_object_cn：实验任务、SAGAT题目、感兴趣区域（AoI）、训练流程

- baseline_control_or_counterfactual_cn：无正式对照，以专家判断和任务可行性为准

##### objective_metrics

（空）

- analysis_method_cn：定性反馈与小规模试测

- main_result_cn：反馈循环被纳入设计；被试平均只犯2.5个使用错误，表明仪表板可理解；专家帮助确定AoI和SA/绩效评估方式

- argumentative_role_cn：提高生态效度和测量的可执行性，为正式实验做准备

- remaining_uncertainty_cn：不是正式统计证据，不能替代主实验

- link_to_next_phase_cn：进入正式实验室实验，收集可统计检验的数据

##### evidence_pointers

1. Section 4，开头段

2. Section 4.1，末尾段

#### 4. 核心实验室组内实验

- order：4

- name_cn：核心实验室组内实验

- question_cn：what-if分析的有无是否会导致SA和任务绩效的系统性差异？

- inputs_and_setting_cn：83名IS研究生；组内设计；两种顺序随机分配；Tobii Pro X2-30眼动仪；APS自行车生产计划任务

- designed_or_compared_object_cn：每名被试分别使用交互式仪表板和交互式分析仪表板各完成一个计划时段

- baseline_control_or_counterfactual_cn：同一被试在交互式仪表板条件下的成绩作为within-subject对照

##### objective_metrics

1. SAGAT得分（正确率百分比）

2. 注视时长（毫秒）

3. 注视次数

4. 任务绩效（计划错误数）

5. NASA-TLX心理负荷

- analysis_method_cn：Wilcoxon符号秩检验、描述统计、效应量r

- main_result_cn：H1和H2得到支持：交互式分析的SA显著更低、错误显著更少；心理负荷无显著差异

- argumentative_role_cn：提供核心因果证据，直接检验what-if特征对认知状态和结果的影响

- remaining_uncertainty_cn：SA与任务绩效之间的关联是否在不同测量方式下一致尚不清楚

- link_to_next_phase_cn：通过相关分析、正态性检验和测量对比进一步检验H3和内部有效性

##### evidence_pointers

1. Section 4.4

2. Section 4.5

3. Section 5.2

4. Section 5.3

5. Table 6

#### 5. 稳健性、相关关系与测量比较分析

- order：5

- name_cn：稳健性、相关关系与测量比较分析

- question_cn：SA与任务绩效的关联是否稳健？测量方式是否改变结论？

- inputs_and_setting_cn：同一实验数据集

- designed_or_compared_object_cn：SAGAT测量与眼动测量作为SA的两种操作化；两种仪表板条件分别分析

- baseline_control_or_counterfactual_cn：交互式条件作为比较基准；心理负荷作为潜在混淆变量

##### objective_metrics

1. Spearman相关（注视时长/注视次数/SAGAT/错误）

2. Shapiro-Wilk正态性检验

3. Wilcoxon符号秩检验

- analysis_method_cn：正态性检验、非参数相关分析、测量方法比较

- main_result_cn：SAGAT在两种设计下都与错误负相关，H3得到支持；眼动数据仅在交互式分析设计中与错误显著相关；SAGAT似乎是更强的绩效预测指标

- argumentative_role_cn：巩固内部有效性，同时把测量比较本身发展为方法论贡献

- remaining_uncertainty_cn：眼动作为SA过程指标的预测效度有限；样本为学生；未直接检验长期out-of-loop

- link_to_next_phase_cn：进入讨论，把结果与out-of-loop理论联系并形成设计启示

##### evidence_pointers

1. Section 5.1

2. Section 5.4

3. Table 7

4. Table 8

## 各部分修辞架构

### abstract_moves

1. PHENOMENON

2. GAP

3. STUDY_OVERVIEW

4. RESULT

5. CONTRIBUTION

### introduction_moves

1. CONTEXT

2. PRACTICAL_STAKES

3. PRIOR_KNOWLEDGE

4. LIMITATION

5. GAP

6. WHY_GAP_MATTERS

7. RQ_OR_OBJECTIVE

8. CONTRIBUTION

9. METHOD_JUSTIFICATION

10. TRANSITION

### theory_and_knowledge_moves

1. THEORY_INTRO

2. PRIOR_KNOWLEDGE

3. MECHANISM

4. METHOD_JUSTIFICATION

5. GAP

### artifact_design_moves

1. DESIGN_FEATURE

2. REQUIREMENT

3. METHOD_JUSTIFICATION

4. BENCHMARK_OR_CONTRAST

### evaluation_moves

1. METHOD_JUSTIFICATION

2. RESULT

3. ROBUSTNESS_OR_BOUNDARY_TEST

4. TRANSITION

### discussion_and_contribution_moves

1. CONTRIBUTION

2. MECHANISM

3. BOUNDARY_CONDITION

4. REQUIREMENT

5. LIMITATION_AND_FUTURE

## 理论/知识到设计的翻译

### 知识/理论基础

1. Endsley的态势感知理论

2. SAGAT和SA测量文献

3. 仪表板组件与类型分类（Yigitbasioglu & Velcu、Few、Eckerson）

4. 交互式优化方法分类（Meignan et al.）

5. 人机自动化与过度信任文献

6. 考虑集（consideration set）和行为决策文献

7. APS生产计划领域知识

- 理论—设计耦合：partial

- 耦合判定理由：SA理论决定了研究问题、核心结果变量、假设方向和测量选择，但具体的what-if特征和仪表板布局来自仪表板与交互式优化文献以及领域要求，并非由SA理论单独推导出来。

- 理论到设计翻译链：what-if作为交互式分析特征来自交互式优化分类（用户修改数据/约束/目标，系统提供求解结果）→ 该特征在GUI上表现为模拟区/瓶颈可视化 → 用户可快速获得反馈但无需深入检查全部数据 → SA理论预测这会降低主动信息扫描和SA、但提高当前任务绩效 → 在APS情境中把该特征实现为仿真区域 → 组内实验对比有/无what-if → 用SAGAT、眼动和错误率测量 → 得到“绩效高但SA低”的结果 → 返回理论，解释为out-of-loop问题并给出设计启示。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：Endsley指出自动化系统可能导致操作者失去SA，形成out-of-the-loop问题；过度依赖系统支持会减少主动认知加工。

- mechanism_cn：用户信任或过度信任what-if建议，减少对全部客观信息的审视，导致对情境的感知、理解和预测下降。

- design_requirement_cn：在评价交互式分析仪表板时，必须同时测量SA和任务绩效，而不仅仅看绩效。

- artifact_choice_cn：交互式分析仪表板增加what-if模拟区，以红/绿标识瓶颈组件及其关键性。

- evaluated_contrast_cn：有what-if分析与无what-if分析的交互式仪表板对比。

- objective_result_cn：SAGAT得分和注视指标显著更低，支持SA下降。

##### evidence_pointers

1. Section 2.1

2. Section 3.1

3. Section 4.3

4. Table 6

#### 2. 2

- theory_or_knowledge_claim_cn：交互仪表板的钻取、筛选等功能可让用户保持人在回路并维持SA。

- mechanism_cn：手工分析要求用户从抽象到具体地检查数据，形成更详细的情境理解。

- design_requirement_cn：控制条件应包含足以保持SA的交互功能，而不是静态只读显示。

- artifact_choice_cn：交互式仪表板包含可排序表格、条形图、下钻/上卷/筛选功能。

- evaluated_contrast_cn：同一任务下，手工交互功能加不加what-if模拟区。

- objective_result_cn：交互式设计下SA更高。

##### evidence_pointers

1. Section 2.2.2

2. Section 4.3

3. Section 5.2

#### 3. 3

- theory_or_knowledge_claim_cn：what-if分析是一种试错式交互优化特征：后台优化模型自动求解，用户通过GUI修改输入并获得反馈。

- mechanism_cn：降低完成规划任务所需的手工认知努力和时间，同时把注意力引向瓶颈组件等关键信息。

- design_requirement_cn：what-if特征应能快速显示数据改动对生产计划的影响，当前输入是否构成可行计划。

- artifact_choice_cn：交互式分析仪表板的模拟区可视化瓶颈组件及其关键性，并用颜色标识有效性。

- evaluated_contrast_cn：有what-if与无what-if条件下规划错误数。

- objective_result_cn：交互式分析设计下错误更少，任务绩效更高。

##### evidence_pointers

1. Section 2.2.3

2. Section 4.3

3. Section 5.3

#### 4. 4

- theory_or_knowledge_claim_cn：SA是决策与任务绩效的重要前因，但高SA并不保证高绩效，低SA也可能由于自动化支持而得到好绩效。

- mechanism_cn：更好的情境知识能提高对系统的掌控，但绩效还取决于可用技能、优化系统是否恰当等变量。

- design_requirement_cn：分析中应区分SA、绩效和潜在调节/混淆因素。

- artifact_choice_cn：同时用SAGAT、眼动注视指标、错误数和NASA-TLX进行相关分析。

- evaluated_contrast_cn：两种仪表板设计下SA与绩效的关系是否一致。

- objective_result_cn：SAGAT在两种设计下都与错误负相关；眼动相关只在交互式分析设计中显著。

##### evidence_pointers

1. Section 3.3

2. Section 5.4

3. Table 7

## 评价逻辑

### evaluation_modes

1. 实验室组内实验

2. SAGAT冻结探针测量

3. 眼动过程指标（注视时长、注视次数）

4. 任务绩效指标（计划错误数）

5. 心理负荷控制（NASA-TLX）

6. 非参数假设检验与相关分析

- why_these_evaluations_cn：SA需要在任务执行中测量，故采用SAGAT冻结法作为直接测量，眼动作为过程指标；任务绩效用错误数衡量；NASA-TLX用于排除心理负荷差异这一竞争解释；组内设计提升统计效力并减少个体差异。

- benchmark_and_contrast_chain_cn：以不含what-if的交互式仪表板作为基线，引入what-if作为处理条件；在同一被试内两种条件比较H1和H2；再用SAGAT与错误的相关检验H3；最后用NASA-TLX证明心理负荷不构成混淆。测量对比进一步把SAGAT与眼动作为SA指标的信效度纳入论证。

### claim_evidence_ledger

#### 1. what-if分析降低SA

- claim_cn：what-if分析降低SA

- evidence_cn：SAGAT得分显著更低，注视时长和注视次数显著更低

- status_cn：支持

#### 2. what-if分析提高任务绩效

- claim_cn：what-if分析提高任务绩效

- evidence_cn：交互式分析设计下的计划错误数显著更少

- status_cn：支持

#### 3. SA正向关联任务绩效

- claim_cn：SA正向关联任务绩效

- evidence_cn：SAGAT与错误负相关；但眼动仅在交互式分析设计中显著

- status_cn：部分支持

#### 4. 心理负荷不是差异来源

- claim_cn：心理负荷不是差异来源

- evidence_cn：NASA-TLX各维度在两种条件下无显著差异

- status_cn：支持

#### 5. 眼动指标与SAGAT测量SA的相似方面

- claim_cn：眼动指标与SAGAT测量SA的相似方面

- evidence_cn：注视时长/次数与SAGAT得分显著正相关

- status_cn：支持

#### 6. SAGAT比眼动更适合预测任务绩效

- claim_cn：SAGAT比眼动更适合预测任务绩效

- evidence_cn：SAGAT在两种设计下均与错误负相关，眼动只在交互式分析设计中与错误负相关

- status_cn：有限支持

- internal_validity_strategy_cn：采用组内设计并随机分配实验顺序以控制顺序/残留效应；任务前有训练和帮助菜单；用SAGAT客观冻结测量和眼动客观记录；检验正态性后用非参数检验；用NASA-TLX排除心理负荷混淆。

- external_validity_strategy_cn：选择APS生产计划作为真实领域问题；任务包含约束、需求和最大化收入的目标；与生产计划员讨论任务、SA/绩效评估和AoI；被试经过训练且平均错误少，说明任务可执行；用学生作为被试并给出合理性论证。

- what_is_not_actually_tested_cn：没有直接中介分析证明what-if通过SA影响绩效；没有检验长期使用后技能退化；没有真实从业者样本；没有变化优化模型质量以验证边界条件；眼动作为SA代理的效度有限；out-of-loop只是理论解释而非直接测量。

## 贡献闭环

- technical_claim_cn：在相同任务和约束下，带what-if分析特征的交互式分析仪表板比不带该特征的交互式仪表板产生更少规划错误。

- artifact_claim_cn：what-if模拟区/瓶颈组件可视化是导致SA下降和绩效提升的可识别设计差异。

- mechanism_claim_cn：what-if通过自动求解和瓶颈聚焦减少用户主动信息扫描，从而降低SA；通过降低手工认知负荷和指向关键信息而提高当前任务绩效。

- boundary_claim_cn：绩效收益仅在底层优化模型和优化程序能够处理当前规划情境时成立；SA损失则可能与用户过度信任和缺少卷入有关。

- reusable_design_knowledge_cn：设计交互式分析仪表板时应同时考虑绩效和SA；可通过周期性SA审计、凝视感知反馈、系统透明度以及训练频繁视觉扫描来缓解out-of-loop风险。

- theoretical_contribution_cn：将out-of-the-loop概念从自动化系统推广到仪表板特征层面；表明SA是任务绩效的必要但不充分条件；SAGAT比眼动更适合预测绩效。

- how_discussion_closes_intro_gap_cn：引言指出what-if特征缺乏对认知能力影响的实证研究；讨论用实验结果说明其确实影响SA和绩效，并把“高绩效但低SA”解释为out-of-loop问题，回应了现有conflicting结果以及缺乏认知视角的缺口。

- overclaim_or_unsupported_leaps_cn：作者在讨论中从相关分析推出SAGAT更强预测力，但缺乏对因果预测的正式比较检验；把眼动结果解读为SA下降的一部分，但眼动本身只是注意代理；把学生样本的结果推广到实际运营决策者时证据有限；H3在两种测量间不一致，却仍概括为“SA关联绩效”。

## 句级写作动作图谱

### 1. 摘要 S1–S3

- order：1

- section：Abstract

- locator：摘要 S1–S3

- move_code：GAP

- paraphrase_cn：近年出现新的交互式分析仪表板特征；它们虽对企业有价值，但对人类认知能力的影响研究不足。

- rhetorical_function_cn：一开始就同时给出现象和缺口。

- depends_on_cn：对交互式分析特征的行业背景认识。

- sets_up_cn：引出全文要补的认知视角缺口。

- evidence_pointer：Abstract

### 2. 摘要 S4–S6

- order：2

- section：Abstract

- locator：摘要 S4–S6

- move_code：STUDY_OVERVIEW

- paraphrase_cn：作者用SA理论开发假设，通过83人的实验室实验和眼动数据检验what-if分析对SA和任务绩效的影响。

- rhetorical_function_cn：压缩式预告研究设计和证据类型。

- depends_on_cn：前面的缺口判断。

- sets_up_cn：为后续研究模型和方法部分提供预览。

- evidence_pointer：Abstract

### 3. 摘要 S7–S9

- order：3

- section：Abstract

- locator：摘要 S7–S9

- move_code：RESULT

- paraphrase_cn：what-if分析提高任务绩效但降低SA，可能造成out-of-loop问题，因此设计者需要谨慎缓解。

- rhetorical_function_cn：把核心证据性结论放在最前。

- depends_on_cn：实验证据。

- sets_up_cn：为设计启示和讨论方向铺垫。

- evidence_pointer：Abstract

### 4. 引言 P1 S1–S4

- order：4

- section：Introduction

- locator：引言 P1 S1–S4

- move_code：CONTEXT

- paraphrase_cn：以COVID-19仪表板为例，说明仪表板对公众和组织的价值，并提出让数据对运营决策者更有用是当代挑战。

- rhetorical_function_cn：用热点事件建立现实相关性和读者共鸣。

- depends_on_cn：无。

- sets_up_cn：把仪表板设计问题置于重要应用场景中。

- evidence_pointer：Introduction P1

### 5. 引言 P2 S1–S3

- order：5

- section：Introduction

- locator：引言 P2 S1–S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：作者引用既有研究，把仪表板描述为DSS中通过GUI与决策者交互的一类系统，并指出静态仪表板以视觉特征呈现信息但不与用户交互。

- rhetorical_function_cn：概括第一类已知方案。

- depends_on_cn：前一段的现实背景。

- sets_up_cn：为随后指出静态仪表板局限做铺垫。

- evidence_pointer：Introduction P2

### 6. 引言 P2 S4–S5

- order：6

- section：Introduction

- locator：引言 P2 S4–S5

- move_code：LIMITATION

- paraphrase_cn：静态仪表板被称为只读，无法满足对复杂多维数据进行分析的需求。

- rhetorical_function_cn：指出现有方案的第一类不足。

- depends_on_cn：静态仪表板的定义。

- sets_up_cn：引出第二类交互式仪表板方案。

- evidence_pointer：Introduction P2后段

### 7. 引言 P3 S1–S3

- order：7

- section：Introduction

- locator：引言 P3 S1–S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：第二类方案通过钻取、上卷、筛选和提醒等功能特征让用户参与数据分析。

- rhetorical_function_cn：介绍已有改进方向。

- depends_on_cn：静态仪表板局限。

- sets_up_cn：为讨论交互式仪表板的认知成本作准备。

- evidence_pointer：Introduction P3

### 8. 引言 P3 S4–S5

- order：8

- section：Introduction

- locator：引言 P3 S4–S5

- move_code：MECHANISM

- paraphrase_cn：这种交互支持理解复杂数据，但需要更多认知努力和手工时间，可能造成决策延迟或错误。

- rhetorical_function_cn：在利好中加入代价，制造张力。

- depends_on_cn：交互特征描述。

- sets_up_cn：引出第三类交互式分析仪表板作为平衡方案。

- evidence_pointer：Introduction P3末段

### 9. 引言 P4 S1–S3

- order：9

- section：Introduction

- locator：引言 P4 S1–S3

- move_code：CONTEXT

- paraphrase_cn：第三类交互式分析仪表板在后台用计算方法自动解决优化问题，同时通过GUI让个体参与优化过程。

- rhetorical_function_cn：介绍新的研究对象。

- depends_on_cn：前两类方案的利弊。

- sets_up_cn：定义what-if等交互式分析特征的技术基础。

- evidence_pointer：Introduction P4

### 10. 引言 P4 S4–S5

- order：10

- section：Introduction

- locator：引言 P4 S4–S5

- move_code：GAP

- paraphrase_cn：what-if分析等特征的潜力在当前运营DSS仪表板中尚未实现。

- rhetorical_function_cn：指出现有制品层面的缺位。

- depends_on_cn：交互式分析特征定义。

- sets_up_cn：说明为什么需要研究该特征。

- evidence_pointer：Introduction P4中段

### 11. 引言 P4 S6–S7

- order：11

- section：Introduction

- locator：引言 P4 S6–S7

- move_code：MECHANISM

- paraphrase_cn：用户可以在不理解优化模型的情况下使用what-if，这可能降低对当前情境的理解并导致out-of-loop问题。

- rhetorical_function_cn：引入理论风险，使问题从技术转向认知。

- depends_on_cn：交互式分析特征中的隐藏优化机制。

- sets_up_cn：为SA理论和out-of-loop概念做铺垫。

- evidence_pointer：Introduction P4末段

### 12. 引言 P5 S1–S3

- order：12

- section：Introduction

- locator：引言 P5 S1–S3

- move_code：LIMITATION

- paraphrase_cn：过去关于what-if与决策绩效的实证结果不一致，有正向、无显著和负向三种结论。

- rhetorical_function_cn：用冲突证据说明现有研究不能给出确定答案。

- depends_on_cn：相关文献的筛选。

- sets_up_cn：为认知视角的缺口增加紧迫性。

- evidence_pointer：Introduction P5前半

### 13. 引言 P5 S4–S5

- order：13

- section：Introduction

- locator：引言 P5 S4–S5

- move_code：GAP

- paraphrase_cn：学界很少关注交互式分析仪表板特征应如何设计以及它们如何影响人类认知能力。

- rhetorical_function_cn：把问题收窄为认知能力缺口。

- depends_on_cn：冲突实证结果。

- sets_up_cn：确立SA作为切入点。

- evidence_pointer：Introduction P5中段

### 14. 引言 P5 S6–S7

- order：14

- section：Introduction

- locator：引言 P5 S6–S7

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：SA是运营决策和任务绩效的关键使能因素，因此需要研究仪表板特征如何积极影响SA。

- rhetorical_function_cn：说明为什么这个认知缺口值得研究。

- depends_on_cn：前述文献缺口。

- sets_up_cn：引出研究目标和研究问题。

- evidence_pointer：Introduction P5后半

### 15. 引言 P5 S8–S9

- order：15

- section：Introduction

- locator：引言 P5 S8–S9

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：研究目标是检验交互式分析仪表板特征、SA和任务绩效之间的关系，并明确提出研究问题。

- rhetorical_function_cn：正式给出全文研究问题。

- depends_on_cn：SA缺口判断。

- sets_up_cn：为贡献声明和后续章节定位。

- evidence_pointer：Introduction P5末段

### 16. 引言 P6 S1–S3

- order：16

- section：Introduction

- locator：引言 P6 S1–S3

- move_code：CONTRIBUTION

- paraphrase_cn：主要贡献是将what-if特征与SA和任务绩效连接；次要贡献是用眼动与SAGAT的大样本实验；第三贡献是将结果转成设计启示。

- rhetorical_function_cn：预先声明贡献，让读者知道文章价值。

- depends_on_cn：研究问题。

- sets_up_cn：为讨论部分的贡献闭环设置预期。

- evidence_pointer：Introduction P6

### 17. 引言 P7 S1–S2

- order：17

- section：Introduction

- locator：引言 P7 S1–S2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：选择APS生产计划作为研究情境，因为数据量大、展示分辨率挑战大、该领域仪表板研究少、计划需要持续调整和快速决策。

- rhetorical_function_cn：为研究情境的选择提供领域理由。

- depends_on_cn：研究问题对运营层的强调。

- sets_up_cn：为方法部分APS任务设计提供依据。

- evidence_pointer：Introduction P7

### 18. 引言 P8

- order：18

- section：Introduction

- locator：引言 P8

- move_code：TRANSITION

- paraphrase_cn：说明后续章节安排：背景、假设开发、方法、结果、讨论和结论。

- rhetorical_function_cn：给读者路线图。

- depends_on_cn：引言已完成的问题定位。

- sets_up_cn：为章节顺序提供组织信号。

- evidence_pointer：Introduction P8

### 19. 2.1 P1 S1–S3

- order：19

- section：Background

- locator：2.1 P1 S1–S3

- move_code：THEORY_INTRO

- paraphrase_cn：SA概念源自军事航空并扩展到复杂动态系统，采用Endsley的著名模型。

- rhetorical_function_cn：引入核心理论透镜并给出权威来源。

- depends_on_cn：引言中SA作为切入点的论述。

- sets_up_cn：为后续SA定义和测量方法提供理论根基。

- evidence_pointer：Section 2.1

### 20. 2.1 P1 S4–S7

- order：20

- section：Background

- locator：2.1 P1 S4–S7

- move_code：MECHANISM

- paraphrase_cn：SA通过个体与环境交互而产生；环境变化要求不断更新SA，这需要认知努力，且可能遇到out-of-loop等障碍。

- rhetorical_function_cn：解释SA的动态形成机制和困难来源。

- depends_on_cn：SA定义。

- sets_up_cn：为自动化导致SA损失提供理论机制。

- evidence_pointer：Section 2.1

### 21. 2.1 P2 S1–S2

- order：21

- section：Background

- locator：2.1 P2 S1–S2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：SA可以按高低程度描述，是当前知识状态在完整性和准确性上的质量判据。

- rhetorical_function_cn：将SA操作化为可测量概念。

- depends_on_cn：Endsley模型。

- sets_up_cn：为选择SAGAT和眼动测量提供概念基础。

- evidence_pointer：Section 2.1 P2

### 22. 2.1 P3 S1–S4

- order：22

- section：Background

- locator：2.1 P3 S1–S4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：SA测量很复杂，通常建议结合冻结探针、过程指标和任务绩效指标。

- rhetorical_function_cn：预告并证明研究所用的多方法测量。

- depends_on_cn：SA定义。

- sets_up_cn：为2.1.1–2.1.3三个测量小节建立框架。

- evidence_pointer：Section 2.1 P3

### 23. 2.1.1 最后一段

- order：23

- section：Background

- locator：2.1.1 最后一段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：SAGAT冻结法在任务中随机停止并遮屏提问，具有直接、客观、有效和可接受等优点。

- rhetorical_function_cn：为使用SAGAT提供方法论辩护。

- depends_on_cn：SA测量分类。

- sets_up_cn：为实验中的SAGAT操作化做铺垫。

- evidence_pointer：Section 2.1.1

### 24. 2.1.2 全部

- order：24

- section：Background

- locator：2.1.2 全部

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用眼动注视时长和次数作为SA过程指标，假设高注视意味着更多信息相关加工，但只是代理。

- rhetorical_function_cn：为眼动测量提供依据并坦承其局限。

- depends_on_cn：过程指标概念。

- sets_up_cn：为实验中AOI、注视指标的解释做准备。

- evidence_pointer：Section 2.1.2

### 25. 2.1.3 全部

- order：25

- section：Background

- locator：2.1.3 全部

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：任务绩效指标因非侵入性和易收集而被大多数SA研究采用。

- rhetorical_function_cn：为选择错误数作为绩效指标提供理由。

- depends_on_cn：SA测量分类。

- sets_up_cn：为任务绩效测量做铺垫。

- evidence_pointer：Section 2.1.3

### 26. 2.2 P1–P2

- order：26

- section：Background

- locator：2.2 P1–P2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：在BIA信息链中仪表板常被称为冰山一角，用户主要通过GUI与之交互；但目前关于仪表板特征及其用户后果的科学研究很少。

- rhetorical_function_cn：把仪表板置于大系统中，同时再次指出研究不足。

- depends_on_cn：BIA背景。

- sets_up_cn：为仪表板组件和类型分类的引入作铺垫。

- evidence_pointer：Section 2.2

### 27. 2.2.1 全部

- order：27

- section：Background

- locator：2.2.1 全部

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：视觉特征包括颜色、视觉复杂度、chart junk、数据墨水比和网格线等，影响信息呈现效率。

- rhetorical_function_cn：提供仪表板视觉维度知识。

- depends_on_cn：仪表板组件框架。

- sets_up_cn：与功能特征和交互式分析特征形成对照。

- evidence_pointer：Section 2.2.1

### 28. 2.2.2 全部

- order：28

- section：Background

- locator：2.2.2 全部

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：功能特征包括点击交互、刷选、筛选、提醒和通知，决定仪表板能做什么。

- rhetorical_function_cn：介绍交互式仪表板的能力来源。

- depends_on_cn：仪表板组件框架。

- sets_up_cn：为交互式设计条件提供依据。

- evidence_pointer：Section 2.2.2

### 29. 2.2.3 全部

- order：29

- section：Background

- locator：2.2.3 全部

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：交互式分析特征把后台优化模型和前台GUI反馈结合；what-if是用户修改数据/约束/目标后由系统求解的试错方法。

- rhetorical_function_cn：精确定义what-if特征及其技术构成。

- depends_on_cn：功能特征和优化方法分类。

- sets_up_cn：为交互式分析设计的核心特征提供概念基础。

- evidence_pointer：Section 2.2.3

### 30. 2.2.4 全部

- order：30

- section：Background

- locator：2.2.4 全部

- move_code：GAP

- paraphrase_cn：仪表板分为静态、交互和交互式分析三类；交互式分析虽有潜力，但尚未实现，用户过度信任可能损害SA。

- rhetorical_function_cn：把文献现状浓缩为三类方案并再次指向缺口。

- depends_on_cn：三种特征类型。

- sets_up_cn：自然过渡到假设开发。

- evidence_pointer：Section 2.2.4

### 31. 第3节开头

- order：31

- section：Hypotheses Development

- locator：第3节开头

- move_code：STUDY_OVERVIEW

- paraphrase_cn：作者预告研究模型包含what-if对SA和绩效的影响、交互式设计作为基线，以及心理负荷作为控制变量。

- rhetorical_function_cn：给出假设开发阶段的结构。

- depends_on_cn：背景中的理论和分类。

- sets_up_cn：为三个小节和Figure 2研究模型做组织。

- evidence_pointer：Section 3

### 32. 3.1 P1

- order：32

- section：Hypotheses Development

- locator：3.1 P1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：仪表板特征的选择应以最有效方式传递所需信息，从而可能提高SA。

- rhetorical_function_cn：把仪表板设计与SA连接起来。

- depends_on_cn：SA理论中对信息加工的要求。

- sets_up_cn：为H1的比较推理提供前提。

- evidence_pointer：Section 3.1

### 33. 3.1 P2

- order：33

- section：Hypotheses Development

- locator：3.1 P2

- move_code：MECHANISM

- paraphrase_cn：交互式仪表板允许用户过滤、下钻并从抽象走向具体，从而详细审查当前情境。

- rhetorical_function_cn：解释为什么交互式设计有助于SA。

- depends_on_cn：功能特征知识。

- sets_up_cn：作为交互式分析设计的参照点。

- evidence_pointer：Section 3.1

### 34. 3.1 P3

- order：34

- section：Hypotheses Development

- locator：3.1 P3

- move_code：MECHANISM

- paraphrase_cn：what-if分析让用户无需详细查看信息或理解整体业务情境就能快速获得系统反馈。

- rhetorical_function_cn：解释为什么what-if可能绕过深度信息加工。

- depends_on_cn：what-if特征定义。

- sets_up_cn：为SA下降预测提供机制。

- evidence_pointer：Section 3.1

### 35. 3.1 P4–P5

- order：35

- section：Hypotheses Development

- locator：3.1 P4–P5

- move_code：MECHANISM

- paraphrase_cn：由于存在异常情境、模型局限和用户过度信任，依赖what-if的规划者可能不再仔细审查所有客观信息，造成SA损失和技能退化。

- rhetorical_function_cn：把自动化信任文献与out-of-loop理论结合起来。

- depends_on_cn：背景中关于过度信任的文献。

- sets_up_cn：直接支撑H1。

- evidence_pointer：Section 3.1

### 36. 3.1 末尾 H1

- order：36

- section：Hypotheses Development

- locator：3.1 末尾 H1

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：交互式分析仪表板设计比不带分析特征的交互式仪表板设计导致更低的SA。

- rhetorical_function_cn：明确给出第一个可检验假设。

- depends_on_cn：前述机制推理。

- sets_up_cn：决定实验结果的第一项检验。

- evidence_pointer：Section 3.1末

### 37. 3.2 P1–P2

- order：37

- section：Hypotheses Development

- locator：3.2 P1–P2

- move_code：MECHANISM

- paraphrase_cn：决策者无法评估所有方案，会形成考虑集；交互仪表板和what-if都能帮助调整考虑集，但what-if反馈更快。

- rhetorical_function_cn：用考虑集概念解释绩效差异。

- depends_on_cn：决策文献。

- sets_up_cn：为H2的比较推理提供认知经济性视角。

- evidence_pointer：Section 3.2

### 38. 3.2 P3

- order：38

- section：Hypotheses Development

- locator：3.2 P3

- move_code：MECHANISM

- paraphrase_cn：手工分析活动认知要求高且耗时，受工作记忆限制，即使SA更高也未必能转化为任务绩效。

- rhetorical_function_cn：解释为什么交互式设计在绩效上可能不利。

- depends_on_cn：认知负荷和工作记忆文献。

- sets_up_cn：为H2提供理论依据。

- evidence_pointer：Section 3.2

### 39. 3.2 末尾 H2

- order：39

- section：Hypotheses Development

- locator：3.2 末尾 H2

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：交互式分析仪表板设计比无分析特征的交互式仪表板设计导致更高的任务绩效。

- rhetorical_function_cn：给出第二个可检验假设。

- depends_on_cn：前述绩效机制。

- sets_up_cn：决定实验结果第二项检验。

- evidence_pointer：Section 3.2末

### 40. 3.3 P1–P2

- order：40

- section：Hypotheses Development

- locator：3.3 P1–P2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：SA是成功决策和任务绩效的重要前因；不完整或错误的情境知识会导致问题，航空事故证据支持其重要性。

- rhetorical_function_cn：SA理论的经典主张。

- depends_on_cn：SA理论。

- sets_up_cn：为H3提供理论基础。

- evidence_pointer：Section 3.3

### 41. 3.3 末尾 H3

- order：41

- section：Hypotheses Development

- locator：3.3 末尾 H3

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：SA与更高的任务绩效相关联。

- rhetorical_function_cn：给出第三个假设。

- depends_on_cn：SA理论。

- sets_up_cn：作为相关分析部分要检验的假设。

- evidence_pointer：Section 3.3末

### 42. 第4节开头 S1

- order：42

- section：Research Method

- locator：第4节开头 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：作者开发了两款仪表板：交互式设计支持手工数据分析和筛选下钻，交互式分析设计在之上增加what-if分析。

- rhetorical_function_cn：说明自变量如何被实例化为两种具体设计。

- depends_on_cn：第三节的假设。

- sets_up_cn：为实验条件和结果测量提供对象。

- evidence_pointer：Section 4

### 43. 第4节开头 S2–S4

- order：43

- section：Research Method

- locator：第4节开头 S2–S4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：采用单因素组内设计提高统计效力、减少个体差异，并通过随机分配实验顺序避免顺序和残留效应。

- rhetorical_function_cn：证明实验设计的内部有效性。

- depends_on_cn：两种处理条件。

- sets_up_cn：为被试分配和流程部分作铺垫。

- evidence_pointer：Section 4

### 44. 4.1 前两段

- order：44

- section：Research Method

- locator：4.1 前两段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：83名IS研究生被试被作为APS仪表板用户的代理，原因是学生不受实战经验偏差、成本低且具备完成复杂认知任务的能力。

- rhetorical_function_cn：为样本选择提供多重辩护。

- depends_on_cn：实验情境APS的认知复杂性。

- sets_up_cn：为外部有效性讨论做说明。

- evidence_pointer：Section 4.1

### 45. 4.1 末段

- order：45

- section：Research Method

- locator：4.1 末段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：研究还与两名生产计划员讨论了任务、SA/绩效评估和AoI设计；被试平均使用错误少，说明仪表板可理解。

- rhetorical_function_cn：用专家反馈和易用性证据增强实验材料和设计可信度。

- depends_on_cn：样本选择。

- sets_up_cn：为实验任务和测量部分做准备。

- evidence_pointer：Section 4.1末

### 46. 4.2 全部

- order：46

- section：Research Method

- locator：4.2 全部

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：APS实验任务要求被试为虚构自行车公司规划四周生产，在组件缺货约束下最大化收入。

- rhetorical_function_cn：说明任务情境、目标与约束。

- depends_on_cn：APS领域选择。

- sets_up_cn：为两种仪表板条件提供共同任务基础。

- evidence_pointer：Section 4.2

### 47. 4.3 交互式设计段

- order：47

- section：Research Method

- locator：4.3 交互式设计段

- move_code：DESIGN_FEATURE

- paraphrase_cn：交互式仪表板包含顶部工具栏、导航栏和内容区，用可排序表格和条形图结合下钻、上卷、筛选提供全面视图。

- rhetorical_function_cn：描述控制条件的界面元素。

- depends_on_cn：功能特征分类。

- sets_up_cn：与后续what-if模拟区形成对比。

- evidence_pointer：Section 4.3，Figure 3

### 48. 4.3 交互式分析设计段

- order：48

- section：Research Method

- locator：4.3 交互式分析设计段

- move_code：DESIGN_FEATURE

- paraphrase_cn：交互式分析仪表板增加模拟区，用绿/红颜色可视化瓶颈组件及其对生产计划的关键性，立即表明当前数据是否形成有效计划。

- rhetorical_function_cn：描述处理条件的核心what-if设计。

- depends_on_cn：交互式分析特征定义。

- sets_up_cn：这是被检验的自变量操作核心。

- evidence_pointer：Section 4.3，Figure 4

### 49. 4.5 SA测量段

- order：49

- section：Research Method

- locator：4.5 SA测量段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：SA用SAGAT冻结法测量，每次任务中被试被停止四次并回答三个情境问题，答案与定格时刻的记录数据比对得到正确率。

- rhetorical_function_cn：说明SA直接测量的实际操作。

- depends_on_cn：SAGAT方法。

- sets_up_cn：为结果部分SAGAT得分的解释提供基础。

- evidence_pointer：Section 4.5，Table 1

### 50. 4.5 眼动测量段

- order：50

- section：Research Method

- locator：4.5 眼动测量段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：SA还用两个AOI的注视时长和注视次数作为过程指标，注视定义为至少60毫秒落入该区域。

- rhetorical_function_cn：说明眼动SA指标的具体操作。

- depends_on_cn：过程指标文献。

- sets_up_cn：为结果部分眼动数据的解释提供基础。

- evidence_pointer：Section 4.5

### 51. 4.5 任务绩效与负荷段

- order：51

- section：Research Method

- locator：4.5 任务绩效与负荷段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：任务绩效以保存计划中的错误数衡量；心理负荷用NASA-TLX在每种条件后测量，并用Wilcoxon检验比较。

- rhetorical_function_cn：说明绩效和混淆变量测量。

- depends_on_cn：任务设计。

- sets_up_cn：为表格3、4和结果部分提供依据。

- evidence_pointer：Section 4.5，Table 2

### 52. 5.1 全部

- order：52

- section：Data Analyses and Results

- locator：5.1 全部

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：Shapiro-Wilk检验显示数据不满足正态性，因此使用Wilcoxon符号秩检验对两个相关样本进行假设检验。

- rhetorical_function_cn：交代统计方法选择的依据。

- depends_on_cn：已有数据。

- sets_up_cn：为后续所有假设检验的统计结果做铺垫。

- evidence_pointer：Section 5.1，Table 5

### 53. 5.2 SAGAT结果段

- order：53

- section：Data Analyses and Results

- locator：5.2 SAGAT结果段

- move_code：RESULT

- paraphrase_cn：交互式设计的SAGAT得分显著高于交互式分析设计，支持H1。

- rhetorical_function_cn：报告第一个假设的直接证据。

- depends_on_cn：SAGAT测量。

- sets_up_cn：与眼动结果共同确认SA下降。

- evidence_pointer：Section 5.2，Table 6

### 54. 5.2 眼动结果段

- order：54

- section：Data Analyses and Results

- locator：5.2 眼动结果段

- move_code：RESULT

- paraphrase_cn：被试在交互式设计上的注视时长和注视次数均显著高于交互式分析设计，眼动数据进一步支持H1。

- rhetorical_function_cn：用过程指标三角验证SA结果。

- depends_on_cn：AOI眼动测量。

- sets_up_cn：为后续测量比较和讨论提供依据。

- evidence_pointer：Section 5.2，Table 6

### 55. 5.3 全部

- order：55

- section：Data Analyses and Results

- locator：5.3 全部

- move_code：RESULT

- paraphrase_cn：交互式设计下被试平均错误更多，交互式分析设计下错误更少，差异显著，支持H2。

- rhetorical_function_cn：报告第二个假设的直接证据。

- depends_on_cn：错误数测量。

- sets_up_cn：为讨论的绩效收益奠定结果基础。

- evidence_pointer：Section 5.3，Table 6

### 56. 5.4 全部

- order：56

- section：Data Analyses and Results

- locator：5.4 全部

- move_code：RESULT

- paraphrase_cn：相关分析表明注视与SAGAT正相关；SAGAT在两种设计下都与错误负相关，但眼动对错误的相关只在交互式分析设计中显著。

- rhetorical_function_cn：报告H3及测量之间的复杂关系。

- depends_on_cn：SAGAT、眼动和错误数据。

- sets_up_cn：为讨论中的测量比较和边界条件做铺垫。

- evidence_pointer：Section 5.4，Table 7

### 57. Table 8前后的总结段

- order：57

- section：Data Analyses and Results

- locator：Table 8前后的总结段

- move_code：TRANSITION

- paraphrase_cn：假设检验汇总表显示H1、H2支持，H3由SAGAT支持且眼动只在交互式分析设计中支持。

- rhetorical_function_cn：从结果部分过渡到讨论部分。

- depends_on_cn：全部统计结果。

- sets_up_cn：为讨论中的理论含义提供结构化总结。

- evidence_pointer：Section 5末，Table 8

### 58. 6.1 第一段

- order：58

- section：Discussion

- locator：6.1 第一段

- move_code：CONTRIBUTION

- paraphrase_cn：交互式分析仪表板绩效显著更高，确认其价值；但SA更低，且绩效收益依赖于优化模型能够处理当前情境。

- rhetorical_function_cn：把结果上升为第一项理论含义。

- depends_on_cn：H1/H2结果。

- sets_up_cn：界定what-if特征的收益边界。

- evidence_pointer：Section 6.1

### 59. 6.1 第二段

- order：59

- section：Discussion

- locator：6.1 第二段

- move_code：MECHANISM

- paraphrase_cn：引入交互式分析特征并非没有代价，用户会因为信任或过度信任系统结果而减少审查，导致SA下降和out-of-loop风险。

- rhetorical_function_cn：把实证结果与overtrust和out-of-loop机制接续。

- depends_on_cn：SA下降结果。

- sets_up_cn：为设计者必须缓解副作用提供依据。

- evidence_pointer：Section 6.1

### 60. 6.1 第三段

- order：60

- section：Discussion

- locator：6.1 第三段

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：SA对绩效必要但不充分，可能存在高SA却做错决定、低SA却做对决定的情况。

- rhetorical_function_cn：限定SA与绩效关系的边界。

- depends_on_cn：H3结果及文献。

- sets_up_cn：为未来研究指出其他影响变量。

- evidence_pointer：Section 6.1

### 61. 6.1 第四段

- order：61

- section：Discussion

- locator：6.1 第四段

- move_code：CONTRIBUTION

- paraphrase_cn：SAGAT在两种设计下都与绩效相关，而眼动只在交互式分析设计中与绩效相关，说明冻结探针是更强的绩效预测指标。

- rhetorical_function_cn：提升测量方法论层面的贡献。

- depends_on_cn：相关分析结果。

- sets_up_cn：为SAGAT作为SA测量推荐提供支持。

- evidence_pointer：Section 6.1

### 62. 6.2 全部

- order：62

- section：Discussion

- locator：6.2 全部

- move_code：REQUIREMENT

- paraphrase_cn：设计启示包括推进自动化以降低认知负荷，同时通过SA审计、凝视感知反馈、系统透明度和训练频繁视觉扫描来保持人在回路。

- rhetorical_function_cn：把结果转成实践者可用设计建议。

- depends_on_cn：理论含义和边界条件。

- sets_up_cn：为结论部分的实践贡献做总结。

- evidence_pointer：Section 6.2

### 63. 第7节前两段

- order：63

- section：Conclusion

- locator：第7节前两段

- move_code：CONTRIBUTION

- paraphrase_cn：结论重申研究目标、主要结果和三类贡献：连接what-if与SA/绩效、提供眼动与SAGAT大样本证据、指出out-of-loop在仪表板特征层面的适用性。

- rhetorical_function_cn：形成贡献闭环。

- depends_on_cn：整篇论证。

- sets_up_cn：为局限性讨论做铺垫。

- evidence_pointer：Section 7

### 64. 第7节末段

- order：64

- section：Conclusion

- locator：第7节末段

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：局限包括使用学生样本、只研究what-if一种特征；未来可研究交互式多目标优化等其他交互式分析特征。

- rhetorical_function_cn：诚实地限定适用范围并给出后续方向。

- depends_on_cn：贡献声明。

- sets_up_cn：闭合全文。

- evidence_pointer：Section 7末

## 写作技术

- gap_construction_cn：先用现实价值和COVID热点建立重要性，再通过三类仪表板方案的递进指出层层不足：静态只读不足、交互认知负荷不足、交互式分析有前景但缺乏认知效果实证；同时用what-if绩效研究结果冲突来强化缺口。

- signposting_cn：引言末给出章节路线图；第3节开头预告研究模型；4.1、4.2、4.3和4.5均用主题句说明即将描述的对象；结果部分按H1、H2、H3顺序展开；讨论按理论含义、实践含义和结论层层推进。

- transition_logic_cn：从背景中的三类仪表板自然过渡到假设开发；在假设开发中用“我们预期”“相反”“因此”等推进比较逻辑；在方法中用“为增强统计效力”“为贴近现实”等说明设计选择；在讨论中用“首先”“第二”“第三”串起含义。

- claim_evidence_rhythm_cn：每个假设都先给机制推理，再给正式假设；每个结果都先报告描述统计，再给检验统计量和效应量，再用一句话回到假设是否支持。

- benchmark_narrative_cn：交互式仪表板作为无what-if的基线不仅是一个实验条件，也是理论比较中的“人在回路”代表；结果部分不断把交互式分析设计与该基线对比，使绩效收益和SA损失都成为可解释的差异。

- theory_return_cn：讨论把绩效较高但SA较低解释为out-of-loop理论的具体表现；用‘必要但不充分’限定SA与绩效关系；用SAGAT与眼动比较来回应理论对测量方法的要求。

- contribution_positioning_cn：在引言中预先列出三项贡献，在讨论中用第一节逐条展开，在结论中再次浓缩；特别强调“不免费”的权衡和设计启示，使文章不止于一次性实验结果。

- novelty_protection_cn：通过同时报告绩效提高和SA下降，避免把结果包装成单纯正面效果；通过加入测量比较和SAGAT/眼动三角验证，使贡献不止于一个实验；通过优化模型边界条件，防止绩效收益被推广到所有what-if情境。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：建立高影响力现实背景和运营DSS中的仪表板问题。

- research_job_cn：识别一个当前被重视但研究不足的系统特征或功能类别。

- required_evidence_cn：现实实例、行业价值证据以及现有方案不足的文献。

- transition_to_next_cn：把系统特征引向人类认知后果，而不是停留在技术功能。

#### 2. 2

- step：2

- writing_job_cn：用递进式文献梳理制造缺口，并指出已有实证冲突。

- research_job_cn：系统回顾相关系统类型和特征，找出未被检验的认知变量。

- required_evidence_cn：能够说明“该特征有前景但不知认知后果”的文献。

- transition_to_next_cn：自然引出理论透镜和SA变量。

#### 3. 3

- step：3

- writing_job_cn：引入成熟理论，给出关键构念定义和测量策略。

- research_job_cn：选择与认知结果匹配的理论，并论证测量方法。

- required_evidence_cn：理论的有效性背书和已存在的测量工具（如SAGAT、眼动）。

- transition_to_next_cn：把理论命题转化为假设。

#### 4. 4

- step：4

- writing_job_cn：开发假设，并在每个假设前给机制推理。

- research_job_cn：从理论机制推演两种处理条件在结果变量上的预期差异。

- required_evidence_cn：机制文献和逻辑因果链。

- transition_to_next_cn：预告研究模型后进入制品的具体设计。

#### 5. 5

- step：5

- writing_job_cn：说明制品的特征选择、实验设计、被试和测量。

- research_job_cn：把假设中的条件实例化为可运行系统，并选择能直接测量构念的指标。

- required_evidence_cn：领域任务材料、预测试反馈、测量工具和数据收集方案。

- transition_to_next_cn：在结果部分按假设顺序报告证据。

#### 6. 6

- step：6

- writing_job_cn：在讨论中把结果返回理论，明确边界条件和设计启示。

- research_job_cn：用理论解释效应，同时限定效应的成立范围。

- required_evidence_cn：统计结果、附加的稳健性检查（如心理负荷、测量对比）。

- transition_to_next_cn：以贡献总结、局限和未来方向结束全文。

### most_transferable_moves_cn

1. 用热点现实事件作为文章开头的相关性锚点

2. 用三类方案递进制造缺口

3. 用成熟理论给出结果变量而不是只测绩效

4. 把条件设计为有/无某一关键特征

5. 用多重测量三角验证同一构念

6. 在讨论中界定绩效收益的边界，避免过度推广

### resource_intensive_or_nonstandard_parts_cn

1. 自定义APS生产计划仪表板需要较大的系统开发投入

2. 眼动仪和眼动数据处理属于专门设备和技术

3. 83人组内实验结合训练、SAGAT冻结和NASA-TLX需要较长的实验时间和场地

4. 与领域生产计划员讨论以确定AoI和任务真实性，需要领域专家配合

### what_not_to_copy_superficially_cn

1. 不能只写“what-if降低SA”而不提供SAGAT或眼动等过程证据

2. 不能在没有心理负荷或足够对照的情况下把绩效差异归因于特征

3. 不能把学生样本结论直接等同于从业者行为

4. 不能忽略“绩效收益仅在优化模型能处理当前情境时成立”的边界条件

- single_best_description_of_the_routine_cn：以成熟认知理论为镜头，把某系统特征的有无制造成两种可比较设计，用直接测量加过程测量在实验中同时揭示绩效收益和认知代价，再回到理论的边界条件与设计启示。

## 分析边界

源文件为Journal Pre-proof且部分段落存在OCR截断和合并（尤其第2.1节、第6.1节部分文本），无法逐字对齐所有句子；但章节标题、表、图和总体结构保留完整，因此分析按段落级和表格定位。缺少附录与补充材料；实验具体统计量个别表格有缺字符。
