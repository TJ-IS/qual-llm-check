# How Do Recommender Systems Lead to Consumer Purchases? A Causal Mediation Analysis of a Field Experiment

- 作者：Xitong Li; Jörn Grahl; Oliver Hinz
- 年份 / 期刊：2022 / Information Systems Research
- DOI：10.1287/isre.2021.1074
- 源文件：28279_2022_how-do-recommender-systems-lead-to-consumer-purchases-a-causal-mediation-analysis-of-a-field-exp.md
- 论文主类型：field_intervention_or_platform_experiment
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.86

## 文章级论证概况

- 核心问题：推荐系统究竟通过哪些因果路径促使消费者购买？本文特别关注考虑集的两个维度——广度（考虑集大小）和深度（每个备选项的卷入程度）——是否以及如何中介推荐系统对购买结果的正向效应。

- 制品与设计：在真实在线书店部署一个基于记忆型协同过滤（CF）的个性化推荐系统；现场实验将访问会话随机分配到展示三个推荐图书标题的处理组和不展示任何推荐的控制组；在此之前用两个实验室实验确定控制条件与推荐数量。

- 客观结果：推荐系统的使用使下单概率提高12.4%、每会话订单金额提高1.7%；同时使考虑集大小提高3.2%、平均每个备选项浏览页数提高0.9%。因果中介分析显示，考虑集大小中介25.7%的总效应，卷入深度中介9.9%–10.2%，两者合计中介39.2%。效应主要由点击并查看推荐产品的访问者驱动。

- 核心贡献：首次在真实现场实验中从因果中介视角揭示推荐系统影响购买的内在机制，证明考虑集广度与深度均起中介作用；为关于考虑集大小方向的争论提供现场证据；并将因果中介分析方法引入IS领域。

- 整篇论证链：作者先指出现有现场数据研究只证实推荐系统提高购买率，却把降低搜索成本这一机制当作未检验的假设，没有探讨因果路径上的中介因素。为填补这一缺口，作者引入营销/IS中的考虑集构念，提出推荐系统可能通过扩大考虑集（广度）和增加每个备选项的卷入（深度）两条路径影响购买。为设计现场实验，作者先用两个实验室实验证明CF推荐优于无推荐和随机推荐、并确定三条推荐为较优数量，然后用真实在线书店的随机现场实验测量结果和中介变量。在ITT和ATT分析证实总效应后，作者采用反事实因果中介方法，分别检验两个单一中介和双中介模型，并通过敏感性分析、交叉研究比较和控制另一个中介作为潜在混淆来支持稳健性。最后，作者将结果回接到考虑集争论、卷入-承诺文献和决策启发式理论，形成对机制、边界和设计知识的贡献。

## 类型与写作弧线判定

- 论文主类型判定：文章的核心证据来自真实在线书店中操纵推荐系统显示与否的随机现场实验，并辅以两个实验室试点实验来确定设计选择；主要因果推断和中介推断都基于这一真实平台上的随机干预，因此更符合平台/现场实验原型，而非纯设计科学或纯计算制品研究。

- 主导写作弧线判定：文章从研究缺口出发，引入考虑集理论构建中介模型，通过试点实验和现场实验设计测试模型，最后在讨论中返回理论争议与机制含义，形成问题—理论—设计—检验—回到理论的完整弧线。

## 研究开展程序

- study_or_phase_count：6

- 研究阶段总序列：第一、二阶段为实验室试点，分别解决现场实验的控制条件与推荐数量选择；第三阶段为现场随机实验，给出平均处理效应、合规者效应和平衡性检验；第四、五阶段分别用因果中介分析检验考虑集广度和深度作为单一中介的路径；第六阶段同时纳入两个中介、做敏感性分析和稳健性检验，并比较中介占比。六个阶段逐步从能否产生总效应推进到如何产生效应以及哪条路径更强。

### studies_or_phases

#### 1. 实验室试点研究1：推荐类型选择

- order：1

- name_cn：实验室试点研究1：推荐类型选择

- question_cn：现场实验应采用什么控制/基线条件？CF推荐相对于无推荐、随机推荐和畅销推荐的购买效果是否支持‘无推荐’作为合理基线？

- inputs_and_setting_cn：149名大学生，大学经济学实验室，实验性背包在线商店，100个产品，激励一致机制，Slope-One IBCF算法，预收集4795条评分。

- designed_or_compared_object_cn：比较CF推荐、无推荐、随机推荐、畅销推荐四种条件下购物篮金额。

- baseline_control_or_counterfactual_cn：以CF推荐作为回归基线，分别对比无推荐、随机推荐、畅销推荐。

##### objective_metrics

1. 购物篮金额（欧元）

- analysis_method_cn：OLS回归，稳健标准误。

- main_result_cn：无推荐和随机推荐的系数均显著为负且大小接近；CF推荐显著高于无推荐和随机推荐；畅销推荐的负系数不显著。结论：无推荐可作为合理控制条件，单纯展示随机产品没有提升购买。

- argumentative_role_cn：为现场实验的控制组选择提供经验依据，排除表层可见效应作为CF推荐效果的唯一解释。

- remaining_uncertainty_cn：样本量小、被试为学生、产品类别单一；CF与畅销推荐的差异不显著，无法完全确定个性化推荐的超额价值。

- link_to_next_phase_cn：既然无推荐是合理基线，下一阶段只需确定处理组应展示多少条推荐。

##### evidence_pointers

1. Section 4.1.1

2. Table 1

3. Table 2

#### 2. 实验室试点研究2：推荐数量选择

- order：2

- name_cn：实验室试点研究2：推荐数量选择

- question_cn：现场实验处理组应展示多少条推荐产品？推荐数量与购买效果之间呈何种关系？

- inputs_and_setting_cn：160名Prolific被试；三个在线商店（背包、书、办公用品），各100个产品；被试内设计，随机分配n=0、1、3、5推荐条件；激励一致机制。

- designed_or_compared_object_cn：比较无推荐、1条、3条、5条CF推荐对购物篮金额的影响。

- baseline_control_or_counterfactual_cn：以无推荐为基线；对3条与1条、5条的系数差异做t检验；控制商店固定效应的稳健性分析。

##### objective_metrics

1. 购物篮金额（欧元）

- analysis_method_cn：OLS回归，标准误在被试层面聚类，含/不含商店固定效应。

- main_result_cn：3条推荐的系数显著为正，1条和5条的系数为正但不显著；3条的系数显著大于1条和5条，呈倒U形关系。

- argumentative_role_cn：为现场实验处理组确定展示3条推荐提供实验依据。

- remaining_uncertainty_cn：3条的具体最优值可能依赖情境，作者承认该数字不一定可推广。

- link_to_next_phase_cn：确定处理条件后，进入真实在线书店的随机现场实验以测试中介模型。

##### evidence_pointers

1. Section 4.1.2

2. Table 1

3. Table 3

#### 3. 在线书店随机现场实验：设计、平衡性与总效应

- order：3

- name_cn：在线书店随机现场实验：设计、平衡性与总效应

- question_cn：在真实在线书店中，推荐系统的总体平均处理效应是什么？效应是否由实际点击推荐产品的访问者驱动？

- inputs_and_setting_cn：荷兰纯在线电子书店，24,044个会话，9,615本独特图书，1,175次购买；实验期2015年4月2日至7月1日；会话级随机分配，返回访问者保持原分组。

- designed_or_compared_object_cn：处理组展示3条CF推荐图书标题在焦点书下方；控制组不显示推荐；其余页面元素完全一致。

- baseline_control_or_counterfactual_cn：无推荐控制组；ITT效应；以随机分配为工具变量估计ATT；合规者/不合规者分离比较。

##### objective_metrics

1. 下单概率（Order）

2. 每会话订单金额对数 lnOrderVal

3. 考虑集大小对数 lnSetSize

4. 平均每个备选项页面浏览数对数 lnViewsPerItem

- analysis_method_cn：Logit估计下单概率，OLS估计连续结果；平衡性检验；2SLS估计ATT。

- main_result_cn：处理组下单概率提高12.4%（OR变化）、订单金额提高1.7%、考虑集大小提高3.2%、卷入深度提高0.9%；平衡性检验通过；合规者效应显著且更大，不合规者效应不显著。

- argumentative_role_cn：先从总效应层面证明推荐系统的确影响购买和两个中介变量，并用合规定义说明效应来自真正接触推荐的人，为下一阶段机制分析铺路。

- remaining_uncertainty_cn：总效应不能说明机制；ITT可能被不合规者稀释；是否符合中介检验所需的识别条件需要专门方法。

- link_to_next_phase_cn：在确认总效应和中介变量变化后，转入因果中介分析，检验两条考虑集路径是否真的中介总效应。

##### evidence_pointers

1. Section 4.2

2. Section 5.1

3. Table 4

4. Table 5

5. Table 6

6. Table 7

#### 4. 因果中介分析：以考虑集大小为单一中介

- order：4

- name_cn：因果中介分析：以考虑集大小为单一中介

- question_cn：考虑集大小是否中介推荐系统对购买概率的影响？中介效应在敏感性分析中是否稳健？

- inputs_and_setting_cn：现场实验的24,044个会话数据；中介变量lnSetSize；结果变量Order；包含RS×lnSetSize交互项的两步回归；bootstrap偏差校正置信区间。

- designed_or_compared_object_cn：自然直接效应（NDE）与自然间接效应（NIE）分解；将lnViewsPerItem作为潜在中介-结果混淆纳入稳健性检验。

- baseline_control_or_counterfactual_cn：以无推荐为反事实状态；与Baron-Kenny/Zhao等术语比较；敏感性分析改变相关参数ρ。

##### objective_metrics

1. NIE优势比

2. NDE优势比

3. 中介百分比

4. 敏感性阈值ρ

5. 中介模型和结果模型R²乘积

- analysis_method_cn：Baron-Kenny改进的因果中介两步回归；bootstrap置信区间；敏感性分析；交叉研究比较。

- main_result_cn：NIE优势比为1.029且显著；NDE优势比为1.092但不显著，属于indirect-only/full mediation；25.7%总效应被中介；敏感性要求ρ>0.30或R²乘积>0.09才可使效应消失；控制lnViewsPerItem后结果相似。

- argumentative_role_cn：证明考虑集广度是一条真实且稳健的因果路径，并说明直接效应在统计上不显著，提示推荐系统主要通过改变考虑集起作用。

- remaining_uncertainty_cn：顺序可忽略性假定不可直接检验；考虑集大小可能与其他未观测混淆相关；深度未纳入主模型时可能是混淆。

- link_to_next_phase_cn：既然深度也可能是路径且对广度检验构成混淆，下一阶段单独检验深度并与其占比进行比较。

##### evidence_pointers

1. Section 5.3.1

2. Table 8

3. Table 9

4. Figure 3

#### 5. 因果中介分析：以卷入深度为单一中介

- order：5

- name_cn：因果中介分析：以卷入深度为单一中介

- question_cn：消费者对考虑集中每个备选项的卷入（平均页面浏览数）是否中介推荐系统对购买概率的影响？

- inputs_and_setting_cn：同一现场实验数据；中介变量lnViewsPerItem；结果变量Order；含RS×lnViewsPerItem交互项；bootstrap置信区间；敏感性分析。

- designed_or_compared_object_cn：NDE与NIE分解；将lnSetSize作为潜在中介-结果混淆纳入稳健性检验。

- baseline_control_or_counterfactual_cn：无推荐反事实状态；与Zhao等分类比较。

##### objective_metrics

1. NIE优势比

2. NDE优势比

3. 中介百分比

4. 敏感性阈值ρ

- analysis_method_cn：因果中介两步回归；bootstrap；敏感性分析；控制另一个中介的稳健性检验。

- main_result_cn：NIE优势比为1.011显著；NDE优势比为1.110显著，属于互补型中介；10.2%总效应被中介；敏感性阈值ρ≈0.20或R²乘积>0.04；控制lnSetSize后NIE仍显著但NDE变为不显著，中介类型变为indirect-only，占比9.32%。

- argumentative_role_cn：证明考虑集深度也是一条额外因果路径，但中介份额小于广度，为后续双中介比较提供基础。

- remaining_uncertainty_cn：深度的效应较脆弱：当控制广度后直接效应不显著，说明广度可能吸收较多路径；敏感性阈值也低于广度。

- link_to_next_phase_cn：分别检验完两个单一中介后，需要同时纳入两个中介估计合计中介比例，并比较两者贡献。

##### evidence_pointers

1. Section 5.3.2

2. Table 10

3. Table 11

#### 6. 双中介分析、稳健性与机制比较

- order：6

- name_cn：双中介分析、稳健性与机制比较

- question_cn：考虑集大小和卷入深度同时作为中介时，二者合计中介多少总效应？哪条路径占更大份额？结果是否稳健？

- inputs_and_setting_cn：现场实验数据；两个中介变量lnSetSize和lnViewsPerItem；结果变量Order；双中介因果中介分析。

- designed_or_compared_object_cn：将双中介模型与两个单中介模型进行比较；比较NIE、NDE、中介百分比和中介类型。

- baseline_control_or_counterfactual_cn：以无推荐为反事实；以各单一中介模型为对照。

##### objective_metrics

1. 合计中介百分比

2. NIE

3. NDE

4. 中介类型

- analysis_method_cn：多中介因果中介分析；与单中介结果对比。

- main_result_cn：两个中介合计中介39.2%的总效应，直接效应不显著，属于indirect-only full mediation；广度中介占比约25.7%，明显大于深度10.2%。

- argumentative_role_cn：为整篇文章的核心机制主张提供总体定量证据：推荐系统的购买效应大部分经由考虑集路径传递，且广度比深度更重要。

- remaining_uncertainty_cn：仍有约60%总效应未被两个中介解释；未观测中介-结果混淆仍可能影响点估计；两中介之间可能相关或顺序关系未被建模。

- link_to_next_phase_cn：随后在讨论中回应理论争议、边界条件和实践含义，同时承认未检验的局限。

##### evidence_pointers

1. Section 5.3.3

2. Section 6

## 各部分修辞架构

### abstract_moves

1. GAP

2. STUDY_OVERVIEW

3. RESULT

4. CONTRIBUTION

### introduction_moves

1. CONTEXT

2. PRACTICAL_STAKES

3. LIMITATION

4. PRIOR_KNOWLEDGE

5. GAP

6. WHY_GAP_MATTERS

7. THEORY_INTRO

8. RQ_OR_OBJECTIVE

9. STUDY_OVERVIEW

10. METHOD_JUSTIFICATION

11. DESIGN_FEATURE

12. RESULT

13. CONTRIBUTION

### theory_and_knowledge_moves

1. THEORY_INTRO

2. THEORY_PROPOSITION

3. MECHANISM

4. LIMITATION

5. BOUNDARY_CONDITION

### artifact_design_moves

1. STUDY_OVERVIEW

2. METHOD_JUSTIFICATION

3. BENCHMARK_OR_CONTRAST

4. DESIGN_FEATURE

5. REQUIREMENT

### evaluation_moves

1. METHOD_JUSTIFICATION

2. BENCHMARK_OR_CONTRAST

3. RESULT

4. ROBUSTNESS_OR_BOUNDARY_TEST

### discussion_and_contribution_moves

1. THEORY_RETURN

2. CONTRIBUTION

3. BOUNDARY_CONDITION

4. LIMITATION_AND_FUTURE

## 理论/知识到设计的翻译

### 知识/理论基础

1. 考虑集与考虑-然后-选择决策研究（Hauser & Wernerfelt; Shocker et al.; Shapiro et al.）

2. 搜索成本与电子商务搜索行为（Bakos; Brynjolfsson et al.; De et al.）

3. 卷入—承诺模型与消费者心理学（Traylor; Beatty et al.; Quester & Lim）

4. 推荐系统效果与CF算法文献（Adomavicius & Tuzhilin; Xiao & Benbasat; Lee & Hosanagar）

5. 因果中介分析与反事实框架（Imai et al.; Valeri & VanderWeele）

- 理论—设计耦合：partial

- 耦合判定理由：理论确实提前决定了中介变量选择（考虑集广度与深度）、结果测量和待检验机制，但具体制品设计——使用CF算法、展示3条推荐、控制组为无推荐——主要由实验室试点结果和行业实践驱动，而非直接从理论推导而来；因果中介方法也是独立的方法论选择。

- 理论到设计翻译链：考虑-然后-选择理论：消费者先形成考虑集再购买 → 推荐系统可能通过降低搜索成本、提高备选项质量，同时改变考虑集大小和对每个备选项的卷入 → 设计要求现场实验必须同时测量购买结果与两个中介变量 → 制品选择：在真实书店部署CF推荐系统，处理组展示3条推荐、控制组不展示 → 被比较的设计差异：展示个性化推荐 vs 不展示 → 客观结果：处理组购买概率、考虑集大小、卷入深度均显著提高，且两个中介显著传递总效应。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：消费者在购买前会先形成考虑集，并考虑加入额外备选项的边际收益与搜索成本（Hauser & Wernerfelt）。

- mechanism_cn：推荐系统降低搜索成本、提高被推荐备选项的预期效用，使消费者愿意检查和加入更多备选。

- design_requirement_cn：现场实验需要捕捉消费者在会话中考虑过的备选项，而不仅是最终购买。

- artifact_choice_cn：将考虑集操作化为会话中浏览的独特图书集合，规模为独特图书数。

- evaluated_contrast_cn：处理组（显示3条CF推荐） vs 控制组（无推荐）的考虑集规模。

- objective_result_cn：处理组考虑集规模提高3.2%（lnSetSize系数0.032，p<0.01）；中介分析NIE=1.029显著，25.7%总效应被中介。

##### evidence_pointers

1. Section 3.1

2. Section 5.1

3. Table 6

4. Table 9

#### 2. 2

- theory_or_knowledge_claim_cn：卷入与承诺模型：消费者卷入越深，越可能对产品产生情感联结并承诺购买（Traylor; Beatty et al.）。

- mechanism_cn：推荐与偏好更匹配，吸引消费者更多注意和时间，增强对每个备选项的卷入。

- design_requirement_cn：需要测量每个备选项的卷入程度，而非总卷入，以避免与考虑集规模机械相关。

- artifact_choice_cn：将卷入深度操作化为每个独特图书的平均页面浏览数。

- evaluated_contrast_cn：处理组 vs 控制组的平均每备选项页面浏览数。

- objective_result_cn：处理组卷入深度提高0.9%（系数0.010，p<0.01）；中介分析NIE=1.011显著，10.2%总效应被中介。

##### evidence_pointers

1. Section 3.2

2. Section 5.1

3. Table 6

4. Table 11

#### 3. 3

- theory_or_knowledge_claim_cn：随机/无关推荐不能提高购买，且CF推荐的购买效果高于无推荐和随机推荐（Pilot Study 1结果）。

- mechanism_cn：无推荐作为控制条件在试点中与随机推荐效果相似，因此可以用无推荐作为实际现场的合理反事实。

- design_requirement_cn：现场实验控制组应隐藏推荐，处理组应展示个性化推荐。

- artifact_choice_cn：现场实验采用控制组完全不显示推荐，处理组显示3条自定义CF推荐。

- evaluated_contrast_cn：推荐显示 vs 隐藏。

- objective_result_cn：处理组购买概率提高12.4%、订单金额提高1.7%。

##### evidence_pointers

1. Section 4.1.1

2. Table 2

3. Section 4.2

4. Table 6

#### 4. 4

- theory_or_knowledge_claim_cn：推荐数量与购买效果呈倒U形，3条推荐效果显著（Pilot Study 2结果）。

- mechanism_cn：太少推荐不足以为消费者创造足够备选；太多推荐可能造成信息过载。

- design_requirement_cn：现场实验宜展示3条推荐。

- artifact_choice_cn：处理组在焦点书下方显示3个推荐书目标题，同时允许滑动查看更多。

- evaluated_contrast_cn：3条推荐 vs 0条推荐。

- objective_result_cn：处理组效应显著且机制成立。

##### evidence_pointers

1. Section 4.1.2

2. Table 3

3. Section 4.2

## 评价逻辑

### evaluation_modes

1. 实验室随机实验（受试者间）

2. 实验室被试内实验

3. 真实平台随机现场实验（会话级随机化）

4. 意图治疗（ITT）估计

5. 工具变量2SLS估计合规定义下的平均处理效应（ATT/LATE）

6. 反事实因果中介分析（NDE/NIE分解）

7. 敏感性分析（ρ/R²乘积）

8. 交叉研究比较

9. 单一中介 + 控制另一个中介作为潜在混淆的稳健性检验

10. 多重中介分析

- why_these_evaluations_cn：先要用实验室实验解决现场实验的两个设计参数，才能让现场实验的控制条件和推荐数量可辩护；现场随机实验提供总效应的内部有效性；由于总效应不能回答‘为什么’，需要用因果中介框架把效应分解为直接与非直接路径；中介识别依赖顺序可忽略性，因此必须做敏感性分析和额外稳健性检验；最后用多重中介比较两个候选机制的解释力。

- benchmark_and_contrast_chain_cn：第一层对比是CF推荐 vs 无推荐/随机推荐/畅销推荐，证明无推荐可作为合理基线；第二层对比是推荐数量n=0/1/3/5，选出3条；第三层对比是现场实验中处理组 vs 控制组；第四层是合规者 vs 不合规者 vs 控制；第五层是中个模型中的NDE vs NIE，以及单一中介 vs 同时控制另一中介；第六层是广度与深度两条路径的中介占比比较。每次对比都建立在上一次结果之上，逐渐收窄到机制证据。

### claim_evidence_ledger

#### 1. CF推荐比无推荐和随机推荐更能提高购买（实验室）。

- claim_cn：CF推荐比无推荐和随机推荐更能提高购买（实验室）。

- evidence_cn：Pilot Study 1中，无推荐与随机推荐系数均显著为负，无推荐与随机推荐效果相近。

- status_cn：充分支持，但效应量来自实验室小样本。

#### 2. 展示三条推荐比展示一条或五条更有效。

- claim_cn：展示三条推荐比展示一条或五条更有效。

- evidence_cn：Pilot Study 2中n=3系数显著，且显著大于n=1和n=5，呈倒U形。

- status_cn：充分支持，但作者承认数字可能不普适。

#### 3. 推荐系统提高购买概率和订单金额。

- claim_cn：推荐系统提高购买概率和订单金额。

- evidence_cn：现场实验ITT：Order OR变化12.4%、lnOrderVal +1.7%，均显著。

- status_cn：充分支持。

#### 4. 推荐系统提高考虑集规模和卷入深度。

- claim_cn：推荐系统提高考虑集规模和卷入深度。

- evidence_cn：现场实验ITT：lnSetSize +3.2%、lnViewsPerItem +0.9%，均显著。

- status_cn：充分支持。

#### 5. 效应由点击查看推荐的访问者驱动。

- claim_cn：效应由点击查看推荐的访问者驱动。

- evidence_cn：合规者ATT显著且很大；不合规者所有系数不显著。

- status_cn：充分支持，但合规定义依赖是否点击推荐链接。

#### 6. 考虑集规模中介推荐系统的购买效应。

- claim_cn：考虑集规模中介推荐系统的购买效应。

- evidence_cn：NIE优势比1.029显著，NDE不显著，25.7%被中介；敏感性阈值ρ>0.30。

- status_cn：较强支持，但仍依赖顺序可忽略性假定的敏感性分析。

#### 7. 卷入深度也中介推荐系统的购买效应。

- claim_cn：卷入深度也中介推荐系统的购买效应。

- evidence_cn：NIE优势比1.011显著，单独分析NDE也显著，10.2%被中介；控制考虑集规模后NDE不再显著。

- status_cn：支持，但路径较弱、更脆弱。

#### 8. 广度比深度中介更大的效应。

- claim_cn：广度比深度中介更大的效应。

- evidence_cn：广度25.7% vs 深度10.2%的中介比例；双中介总比例39.2%。

- status_cn：点估计支持，但置信区间重叠检验未正式报告。

- internal_validity_strategy_cn：使用真实平台上的随机化分配；检查pre-experimental变量平衡；保持处理组与控制组页面其他元素一致；对返回访问者稳定分配处理；用ITT避免自选择；再用工具变量估计合规者效应；因果中介采用反事实框架并做敏感性分析。

- external_validity_strategy_cn：使用真实在线书店和真实购买行为而非实验室样本；CF算法是行业常用实现；调用其他现场研究（如Lee和Hosanagar）的结果进行比较；在讨论中将结果与既有实验室证据做跨情境对照，并明确单一产品类别和单一算法对可推广性的限制。

- what_is_not_actually_tested_cn：顺序可忽略性假定无法直接检验；现场实验控制组为无推荐，因此估计的是包含表层可见效应的组合效应，没有被随机推荐控制条件在真实现场中分离；没有测试非CF推荐、畅销推荐控制条件和产品类别异质性；消费者考虑集和卷入均以浏览行为代理，未直接测量心理卷入；双中介模型中两个中介之间的顺序或相关结构未被明确建模。

## 贡献闭环

- technical_claim_cn：采用因果中介分析方法而非传统Baron-Kenny法，在随机现场实验数据中分解推荐系统的直接与间接效应，并获得可作因果解释的NIE/NDE估计。

- artifact_claim_cn：一个基于记忆型CF的推荐系统在真实书店中将购买概率提高12.4%、订单金额提高1.7%，并显著扩大考虑集与卷入深度；效应主要由点击推荐的消费者驱动。

- mechanism_claim_cn：考虑集广度与深度是推荐系统影响购买的两条并行中介路径；广度路径占比约25.7%，深度路径约10.2%，合计39.2%；直接效应在主要模型中不显著，说明推荐系统的作用很大程度经由考虑集变化传递。

- boundary_claim_cn：证据适用于CF推荐系统、电子书在线商店、会话级随机暴露、推荐置于焦点商品下方的布局；处理效应是含有表层可见效应的组合效应；当消费者不点击推荐时效应趋近于零；当使用非CF推荐或不同产品类别时结果可能不同。

- reusable_design_knowledge_cn：设计推荐系统现场实验前应先用试点实验验证控制条件和推荐数量；考虑集应分解为广度和深度以避免总卷入与规模机械相关；在真实平台评估推荐系统时，可将会话级浏览行为代理化地测量中介机制。

- theoretical_contribution_cn：将推荐系统文献中的隐含搜索成本假设置于明确的考虑集中介模型中，用现场实验解决关于推荐系统使考虑集变大还是变小的争论；把卷入-承诺机制引入推荐系统效果解释；从非补偿性与补偿性启发式角度说明推荐系统为何同时促进更多搜索和更深比较。

- how_discussion_closes_intro_gap_cn：引言说旧研究只估计总效应而未检验因果路径；讨论部分直接回应该缺口：作者用中介分析证明考虑集广度和深度确实承担路径功能，从而把‘推荐系统降低搜索成本’从假设变成可被数据支持的机制；同时针对考虑集大小方向的争论给出现场证据，并对实验室vs现场结果的差异提出解释。

- overclaim_or_unsupported_leaps_cn：文章称‘full mediation/indirect-only’但点估计显示仍有约60%总效应未解释，且NDE不显著不等于效应为零；将浏览行为视为考虑集/卷入的代理存在概念跳跃；广度与深度中介占比的比较没有报告统计推断差异；双重中介模型未处理两个中介之间的潜在顺序关系；现场控制条件无法排除表层可见效应，作者承认这一点。

## 句级写作动作图谱

### 1. P1 S1

- order：1

- section：Introduction

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：推荐系统被定义为引发或收集用户偏好并据此提供建议的软件代理。

- rhetorical_function_cn：为全文给出核心对象的技术定义。

- depends_on_cn：无，文章起点。

- sets_up_cn：限定本文聚焦个性化推荐系统。

- evidence_pointer：Introduction P1

### 2. P1 S2

- order：2

- section：Introduction

- locator：P1 S2

- move_code：CONTEXT

- paraphrase_cn：个性化推荐系统在电商中普遍存在，Amazon是代表。

- rhetorical_function_cn：说明研究对象具有现实普遍性。

- depends_on_cn：承接推荐系统的定义。

- sets_up_cn：为后续现实重要性铺垫。

- evidence_pointer：Introduction P1

### 3. P2 S1

- order：3

- section：Introduction

- locator：P2 S1

- move_code：PRACTICAL_STAKES

- paraphrase_cn：推荐系统旨在降低搜索成本、帮助找到最相关产品，并被认为对电商实践影响重大。

- rhetorical_function_cn：把研究主题与商业价值联系起来。

- depends_on_cn：推荐系统定义与普遍性。

- sets_up_cn：说明为何大量研究关注推荐系统。

- evidence_pointer：Introduction P2

### 4. P2 S2

- order：4

- section：Introduction

- locator：P2 S2

- move_code：LIMITATION

- paraphrase_cn：早期研究多在实验室进行，且所用算法不一定是现在主流的协同过滤，外推到商业实践存在疑问。

- rhetorical_function_cn：指出既有证据的第一个不足：情境和制品代表性。

- depends_on_cn：现实重要性。

- sets_up_cn：为强调现场数据研究更可取。

- evidence_pointer：Introduction P2

### 5. P3 S1

- order：5

- section：Introduction

- locator：P3 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：近期研究使用现场数据并大体一致发现推荐系统能提高购买倾向和销售额。

- rhetorical_function_cn：概括领域共识。

- depends_on_cn：早期实验室研究局限。

- sets_up_cn：随后指出共识背后的机制未检验。

- evidence_pointer：Introduction P3

### 6. P3 S2

- order：6

- section：Introduction

- locator：P3 S2

- move_code：LIMITATION

- paraphrase_cn：先前研究大多假设推荐系统降低搜索成本，但并未用现场数据检验这一假设，也不探索因果路径上的中介因素。

- rhetorical_function_cn：点出领域中的核心分析盲区。

- depends_on_cn：既有共识性发现。

- sets_up_cn：构造研究缺口。

- evidence_pointer：Introduction P3

### 7. P3 S3

- order：7

- section：Introduction

- locator：P3 S3

- move_code：GAP

- paraphrase_cn：因此，已有研究对推荐系统经济效果背后的机制理解有限。

- rhetorical_function_cn：正式声明缺口。

- depends_on_cn：前一句的未检验假设。

- sets_up_cn：引出本文目标。

- evidence_pointer：Introduction P3

### 8. P4 S1

- order：8

- section：Introduction

- locator：P4 S1

- move_code：THEORY_INTRO

- paraphrase_cn：本文提出消费者考虑集在推荐系统影响购买的因果路径中起重要作用。

- rhetorical_function_cn：引入理论透镜。

- depends_on_cn：缺口存在。

- sets_up_cn：为中介模型提供核心构念。

- evidence_pointer：Introduction P4

### 9. P4 S2

- order：9

- section：Introduction

- locator：P4 S2

- move_code：GAP

- paraphrase_cn：据作者所知，现有现场数据研究尚未考察考虑集在推荐系统购买效应中的角色。

- rhetorical_function_cn：把缺口进一步具体化到考虑集。

- depends_on_cn：考虑集构念的引入。

- sets_up_cn：说明为什么本文不同于De等人仅猜测的思路。

- evidence_pointer：Introduction P4

### 10. P5 S1

- order：10

- section：Introduction

- locator：P5 S1

- move_code：MECHANISM

- paraphrase_cn：由于推荐系统降低搜索成本，可能影响考虑集大小；因推荐更符合偏好，消费者对备选项的卷入可能不同于无推荐情境。

- rhetorical_function_cn：从机制上解释为何推荐系统会改变两个中介变量。

- depends_on_cn：考虑集模型和搜索成本文献。

- sets_up_cn：提出两个中介维度。

- evidence_pointer：Introduction P5

### 11. P5 S2

- order：11

- section：Introduction

- locator：P5 S2

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：因此作者构建中介模型，提出考虑集规模和每个备选项卷入程度两条路径影响购买倾向。

- rhetorical_function_cn：明确提出可检验的研究模型。

- depends_on_cn：机制推理。

- sets_up_cn：为实验和中介分析设定目标。

- evidence_pointer：Introduction P5

### 12. P6 S1

- order：12

- section：Introduction

- locator：P6 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：作者与欧洲大型在线书商合作开展随机现场实验，并先用两个实验室试点实验指导现场实验设计。

- rhetorical_function_cn：预告研究项目和证据来源。

- depends_on_cn：需要实证检验中介模型。

- sets_up_cn：说明后续章节顺序。

- evidence_pointer：Introduction P6

### 13. P6 S2

- order：13

- section：Introduction

- locator：P6 S2

- move_code：RESULT

- paraphrase_cn：试点实验结果显示CF推荐提高购买、推荐数量与效果呈倒U形且三条推荐有效。

- rhetorical_function_cn：为设计选择提供证据摘要。

- depends_on_cn：试点实验的执行。

- sets_up_cn：为现场实验控制组和推荐数量辩护。

- evidence_pointer：Introduction P6

### 14. P6 S3

- order：14

- section：Introduction

- locator：P6 S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：现场实验以无推荐为控制组，处理组在焦点书下方展示三条CF推荐，其余页面完全一致。

- rhetorical_function_cn：陈述关键制品设计。

- depends_on_cn：试点实验结论。

- sets_up_cn：为结果部分的ITT估计提供设计基础。

- evidence_pointer：Introduction P6

### 15. P7 S1

- order：15

- section：Introduction

- locator：P7 S1

- move_code：RESULT

- paraphrase_cn：现场结果显示推荐系统平均使下单概率提高12.4%、每会话收入提高1.7%、考虑集规模提高3.2%、卷入深度提高0.9%。

- rhetorical_function_cn：给出总效应证据。

- depends_on_cn：现场实验数据。

- sets_up_cn：随后区分合规者并进入中介分析。

- evidence_pointer：Introduction P7

### 16. P7 S2

- order：16

- section：Introduction

- locator：P7 S2

- move_code：RESULT

- paraphrase_cn：进一步分析表明效应主要由点击并查看至少一条推荐产品的消费者驱动，只看首页暴露而不点击的消费者几乎没有效应。

- rhetorical_function_cn：增加机制可信度，排除单纯暴露效应。

- depends_on_cn：合规者/不合规者分类。

- sets_up_cn：ATT估计和后续机制解释。

- evidence_pointer：Introduction P7

### 17. P7 S3

- order：17

- section：Introduction

- locator：P7 S3

- move_code：RESULT

- paraphrase_cn：因果中介分析发现考虑集规模与卷入深度均中介推荐系统对购买的影响，直接效应不显著，表现为完全中介/间接-only中介；两个路径分别中介25.7%和9.9%，合计39.2%。

- rhetorical_function_cn：在摘要层面给出全文核心定量结论。

- depends_on_cn：因果中介方法。

- sets_up_cn：为贡献声明提供证据。

- evidence_pointer：Introduction P7

### 18. P8 S1

- order：18

- section：Introduction

- locator：P8 S1

- move_code：CONTRIBUTION

- paraphrase_cn：作者宣称首次从中介视角揭示建议呈现到购买的因果路径，贡献之一是发现广度和深度都传导推荐系统效果。

- rhetorical_function_cn：开始列举贡献。

- depends_on_cn：前面所有证据。

- sets_up_cn：为后文贡献讨论定基调。

- evidence_pointer：Introduction P8

### 19. P8 S2

- order：19

- section：Introduction

- locator：P8 S2

- move_code：CONTRIBUTION

- paraphrase_cn：作者还宣称提供第一个现场实验证据，支持推荐系统扩大考虑集并提高转化率；同时首次发现卷入深度也中介正面效应。

- rhetorical_function_cn：针对既有争论和文献空白给出贡献位置。

- depends_on_cn：现场证据和中介结果。

- sets_up_cn：摘要中的最终贡献声明。

- evidence_pointer：Introduction P8

### 20. Section 2.1 P1 S1

- order：20

- section：Related Literature

- locator：Section 2.1 P1 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：总结销售效果文献：De等人、Pathak等人、Lee和Hosanagar等均发现推荐系统提高销售或浏览。

- rhetorical_function_cn：巩固前文所说的领域共识。

- depends_on_cn：引言中的研究共识。

- sets_up_cn：随后指出共识中缺失机制。

- evidence_pointer：Section 2.1

### 21. Section 2.1 P4 S1

- order：21

- section：Related Literature

- locator：Section 2.1 P4 S1

- move_code：GAP

- paraphrase_cn：作者强调尽管大量研究确认推荐系统提升销售，但现场数据研究基本没有考察考虑集在因果中的角色。

- rhetorical_function_cn：在文献综述末尾再次声明研究缺口。

- depends_on_cn：对产品销量和网络视角的综述。

- sets_up_cn：为下一节理论发展开路。

- evidence_pointer：Section 2.1 P4

### 22. Section 3 P1 S1

- order：22

- section：Theory Development

- locator：Section 3 P1 S1

- move_code：THEORY_INTRO

- paraphrase_cn：提出考虑集是营销与IS中成熟构念，可能中介推荐系统影响购买的路径。

- rhetorical_function_cn：把考虑集正式确定为理论核心。

- depends_on_cn：文献缺口。

- sets_up_cn：引入考虑-然后-选择过程。

- evidence_pointer：Section 3 P1

### 23. Section 3 P1 S2

- order：23

- section：Theory Development

- locator：Section 3 P1 S2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：大量文献显示消费者采用考虑-然后-选择的两阶段决策，先识别考虑集再从考虑集中选择。

- rhetorical_function_cn：给出理论的决策过程基础。

- depends_on_cn：考虑集文献。

- sets_up_cn：区分形成考虑集和评估备选项两个并行过程。

- evidence_pointer：Section 3 P1

### 24. Section 3 P1 S3

- order：24

- section：Theory Development

- locator：Section 3 P1 S3

- move_code：MECHANISM

- paraphrase_cn：注意考虑集形成与备选项卷入可并行发生：消费者边搜索边评估，在购买前访问和重访考虑集中备选项。

- rhetorical_function_cn：说明广度与深度不是前后阶段而是并行维度。

- depends_on_cn：考虑-然后-选择理论。

- sets_up_cn：为模型包含两个并行中介变量提供理由。

- evidence_pointer：Section 3 P1

### 25. Section 3 P1 S4

- order：25

- section：Theory Development

- locator：Section 3 P1 S4

- move_code：THEORY_PROPOSITION

- paraphrase_cn：作者提出考虑集的两个维度——广度和深度——共同中介推荐系统对购买的影响，并以图1展示模型。

- rhetorical_function_cn：陈述正式命题。

- depends_on_cn：前面对并行过程的讨论。

- sets_up_cn：之后两小节分别推导两个维度。

- evidence_pointer：Section 3 P1, Figure 1

### 26. Section 3.1 P1 S1

- order：26

- section：Theory Development

- locator：Section 3.1 P1 S1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：已有理论对推荐系统使考虑集变小还是变大存在矛盾预测。

- rhetorical_function_cn：设置理论张力。

- depends_on_cn：考虑集规模文献。

- sets_up_cn：给出两种机制，说明是经验问题。

- evidence_pointer：Section 3.1 P1

### 27. Section 3.1 P2 S1

- order：27

- section：Theory Development

- locator：Section 3.1 P2 S1

- move_code：MECHANISM

- paraphrase_cn：一方面，推荐系统让消费者更快找到最相关产品，因此无需加入太多备选，考虑集可能变小；Haubl系列实验支持这一点。

- rhetorical_function_cn：陈述缩小机制与实验室证据。

- depends_on_cn：推荐相关性与搜索效率。

- sets_up_cn：与下段扩大机制形成对比。

- evidence_pointer：Section 3.1 P2

### 28. Section 3.1 P3 S1

- order：28

- section：Theory Development

- locator：Section 3.1 P3 S1

- move_code：MECHANISM

- paraphrase_cn：另一方面，消费者在边际收益与成本间权衡；推荐系统提高备选项预期效用并降低搜索成本，因此可能促使消费者搜索和加入更多备选，扩大考虑集。

- rhetorical_function_cn：陈述扩大机制。

- depends_on_cn：考虑集评价成本理论。

- sets_up_cn：把方向问题推给现场数据。

- evidence_pointer：Section 3.1 P3

### 29. Section 3.1 P4 S1

- order：29

- section：Theory Development

- locator：Section 3.1 P4 S1

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：更大的考虑集可能提高命中购买意图的概率，但也可能引发信息过载，因此是否促进购买仍是经验问题。

- rhetorical_function_cn：说明即使方向确定，广度到购买之间也非单调。

- depends_on_cn：信息过载文献。

- sets_up_cn：解释为何需要中介分析而不是只检验总效应。

- evidence_pointer：Section 3.1 P4

### 30. Section 3.2 P1 S1

- order：30

- section：Theory Development

- locator：Section 3.2 P1 S1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：推荐产品与偏好更匹配，可能吸引更多注意、变得更相关，也可能让比较更简单、耗时更少，所以卷入深度方向也不确定。

- rhetorical_function_cn：为深度维度设置理论两难。

- depends_on_cn：推荐匹配与注意力。

- sets_up_cn：引出卷入—承诺机制。

- evidence_pointer：Section 3.2 P1

### 31. Section 3.2 P2 S1

- order：31

- section：Theory Development

- locator：Section 3.2 P2 S1

- move_code：MECHANISM

- paraphrase_cn：消费者卷入产品会形成情感联结、提高承诺和购买意愿，既有研究和线下超市证据支持这一关系。

- rhetorical_function_cn：提供从卷入深度到购买的理论桥梁。

- depends_on_cn：消费者心理学卷入-承诺文献。

- sets_up_cn：使深度具备正向购买效应的预期。

- evidence_pointer：Section 3.2 P2

### 32. Section 4.1 P1 S1

- order：32

- section：Randomized Field Experiment

- locator：Section 4.1 P1 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：现场实验有两个关键设计选择：控制条件和推荐数量；作者用两个实验室试点实验来确定它们。

- rhetorical_function_cn：说明试点实验在整个证据链中的位置。

- depends_on_cn：理论模型需要现场检验。

- sets_up_cn：介绍表1的总体实验概览。

- evidence_pointer：Section 4.1, Table 1

### 33. Section 4.1.1 P1 S1

- order：33

- section：Randomized Field Experiment

- locator：Section 4.1.1 P1 S1

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：无推荐是自然控制选择，但估计效应可能包含单纯展示产品的表层效应；随机推荐可作为替代控制来分离表层效应。

- rhetorical_function_cn：为控制条件的选择建立方法论意识。

- depends_on_cn：现有文献常用控制设计。

- sets_up_cn：说明为何在试点实验中加入随机推荐条件。

- evidence_pointer：Section 4.1.1 P1

### 34. Section 4.1.1 P3 S1

- order：34

- section：Randomized Field Experiment

- locator：Section 4.1.1 P3 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：实验商店销售100种背包，使用Slope-One IBCF算法，并以预收集评分生成推荐。

- rhetorical_function_cn：描述试点实验的制品构建。

- depends_on_cn：需要可运行的CF推荐系统。

- sets_up_cn：使结果能够映射到现场CF推荐。

- evidence_pointer：Section 4.1.1 P3

### 35. Section 4.1.1 P5 S1

- order：35

- section：Randomized Field Experiment

- locator：Section 4.1.1 P5 S1

- move_code：RESULT

- paraphrase_cn：因为几乎所有人都购买了，转化率没有足够变异，作者用购物篮金额作为因变量。

- rhetorical_function_cn：说明分析选择受数据变异约束。

- depends_on_cn：试点实验数据。

- sets_up_cn：为表2的OLS回归作准备。

- evidence_pointer：Section 4.1.1 P5, Table 2

### 36. Section 4.1.1 P6 S1

- order：36

- section：Randomized Field Experiment

- locator：Section 4.1.1 P6 S1

- move_code：RESULT

- paraphrase_cn：无推荐和随机推荐的系数都显著为负且相似，说明随机推荐不优于无推荐，无推荐可作为合理控制组。

- rhetorical_function_cn：直接回应控制条件选择问题。

- depends_on_cn：表2结果。

- sets_up_cn：为现场实验控制条件辩护。

- evidence_pointer：Section 4.1.1 P6, Table 2

### 37. Section 4.1.2 P3 S1

- order：37

- section：Randomized Field Experiment

- locator：Section 4.1.2 P3 S1

- move_code：RESULT

- paraphrase_cn：n=3的推荐效果显著为正且明显大于n=1和n=5，呈倒U形；因此现场实验使用三条推荐。

- rhetorical_function_cn：直接决定处理组推荐数量。

- depends_on_cn：表3回归结果。

- sets_up_cn：现场实验的处理组设计。

- evidence_pointer：Section 4.1.2, Table 3

### 38. Section 4.2 P2 S1

- order：38

- section：Randomized Field Experiment

- locator：Section 4.2 P2 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：现场实验目标是在真实在线书店测试第三节提出的中介模型。

- rhetorical_function_cn：把设计与理论模型重新连接。

- depends_on_cn：理论和试点结果。

- sets_up_cn：描述实验单位和随机化。

- evidence_pointer：Section 4.2 P2

### 39. Section 4.2 P3 S1

- order：39

- section：Randomized Field Experiment

- locator：Section 4.2 P3 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：实验在会话层随机分配，处理组显示三条推荐，控制组不显示推荐，其余页面元素完全相同。

- rhetorical_function_cn：说明实验干预的具体形态。

- depends_on_cn：试点实验确定的数量和位置。

- sets_up_cn：为平衡性检验和ITT估计提供依据。

- evidence_pointer：Section 4.2, Figure 2

### 40. Section 5.1 P3 S1

- order：40

- section：Results

- locator：Section 5.1 P3 S1

- move_code：REQUIREMENT

- paraphrase_cn：遵循文献，作者将会话中浏览的独特图书集操作化为考虑集，独特图书数为广度，每个独特图书的平均浏览页数为深度。

- rhetorical_function_cn：把理论构念转成可计算变量。

- depends_on_cn：考虑集与卷入操作化文献。

- sets_up_cn：表4的描述统计和后续变量使用。

- evidence_pointer：Section 5.1 P3, Table 4

### 41. Section 5.1 P4 S1

- order：41

- section：Results

- locator：Section 5.1 P4 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：连续变量高度偏态，因此对订单金额、考虑集大小和每备选项浏览数做对数变换。

- rhetorical_function_cn：解释变量变换。

- depends_on_cn：描述统计。

- sets_up_cn：表5和表6中的估计模型。

- evidence_pointer：Section 5.1 P4

### 42. Section 5.1 P5 S1

- order：42

- section：Results

- locator：Section 5.1 P5 S1

- move_code：RESULT

- paraphrase_cn：处理组的结果和中介变量都显著高于控制组，描述统计与中介模型一致。

- rhetorical_function_cn：用描述统计先行确认模型方向。

- depends_on_cn：表5比较。

- sets_up_cn：进入正式回归。

- evidence_pointer：Section 5.1, Table 5

### 43. Section 5.2 P1 S1

- order：43

- section：Results

- locator：Section 5.2 P1 S1

- move_code：RESULT

- paraphrase_cn：推荐系统使下单概率提高12.4%、订单金额提高1.7%，同时使考虑集大小提高3.2%、卷入深度提高0.9%。

- rhetorical_function_cn：报告ITT总效应。

- depends_on_cn：表6回归。

- sets_up_cn：与Lee和Hosanagar比较效应量。

- evidence_pointer：Section 5.2, Table 6

### 44. Section 5.2 P2 S1

- order：44

- section：Results

- locator：Section 5.2 P2 S1

- move_code：MECHANISM

- paraphrase_cn：并非所有消费者对推荐同样敏感；作者区分点击过至少一条推荐的合规者和未点击的不合规者。

- rhetorical_function_cn：引入消费者异质性和合规定义。

- depends_on_cn：现场数据中的点击行为。

- sets_up_cn：ITT与ATT的区别。

- evidence_pointer：Section 5.2 P2

### 45. Section 5.2 P3 S1

- order：45

- section：Results

- locator：Section 5.2 P3 S1

- move_code：RESULT

- paraphrase_cn：用随机分配作为工具变量估计的ATT显示，合规者的购买和中介变量效应显著且远大于ITT，不合规者效应不显著。

- rhetorical_function_cn：证明效应来自真正接触推荐的消费者。

- depends_on_cn：2SLS估计。

- sets_up_cn：为中介分析提供更强的处理定义。

- evidence_pointer：Section 5.2, Table 7

### 46. Section 5.3 P1 S1

- order：46

- section：Results

- locator：Section 5.3 P1 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：中介分析在IS和营销中流行，但传统方法需要改进；最近的反事实因果中介框架允许因果解释。

- rhetorical_function_cn：引入因果中介方法并说明为何采用。

- depends_on_cn：需要检验机制。

- sets_up_cn：给出中介方程和结果方程。

- evidence_pointer：Section 5.3 P1

### 47. Section 5.3.1 P2 S1

- order：47

- section：Results

- locator：Section 5.3.1 P2 S1

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：因为不知道推荐与中介是否交互，按因果中介最佳实践在结果方程中加入暴露-中介交互项。

- rhetorical_function_cn：说明相对于经典Baron-Kenny方法的差异。

- depends_on_cn：Valeri和VanderWeele方法。

- sets_up_cn：表8回归中的交互项。

- evidence_pointer：Section 5.3.1 P2

### 48. Section 5.3.1 P3 S1

- order：48

- section：Results

- locator：Section 5.3.1 P3 S1

- move_code：RESULT

- paraphrase_cn：以考虑集大小为单一中介时，NIE优势比1.029显著，NDE优势比1.092不显著，属间接-only/full mediation，25.7%被中介。

- rhetorical_function_cn：报告核心中介结果。

- depends_on_cn：表9估计。

- sets_up_cn：为敏感性分析。

- evidence_pointer：Section 5.3.1, Table 9

### 49. Section 5.3.1 P4 S1

- order：49

- section：Results

- locator：Section 5.3.1 P4 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：因果中介需要顺序可忽略性假定，该假定不可检验，因此应进行敏感性分析，观察未观测中介-结果混淆使效应消失的阈值。

- rhetorical_function_cn：解释为何做敏感性分析。

- depends_on_cn：因果中介识别条件。

- sets_up_cn：图3的ρ曲线和R²乘积。

- evidence_pointer：Section 5.3.1 P4, Figure 3

### 50. Section 5.3.1 P5 S1

- order：50

- section：Results

- locator：Section 5.3.1 P5 S1

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：敏感性分析显示ρ需超过0.30或R²乘积超过0.09才能使中介效应消失；作者还与其他研究比较稳健性。

- rhetorical_function_cn：评估中介结论对违反假定的敏感度。

- depends_on_cn：图3和STATA mediation包。

- sets_up_cn：为加入另一中介作为混淆的稳健性检验作铺垫。

- evidence_pointer：Section 5.3.1 P5

### 51. Section 5.3.1 P6 S1

- order：51

- section：Results

- locator：Section 5.3.1 P6 S1

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：将lnViewsPerItem作为潜在中介-结果混淆纳入回归后，考虑集大小的中介结果依然相似。

- rhetorical_function_cn：增加对广度路径的稳健性信心。

- depends_on_cn：表8第3-4列。

- sets_up_cn：下节检验深度路径。

- evidence_pointer：Section 5.3.1, Table 8

### 52. Section 5.3.2 P2 S1

- order：52

- section：Results

- locator：Section 5.3.2 P2 S1

- move_code：RESULT

- paraphrase_cn：以卷入深度为单一中介时，NIE优势比1.011显著，NDE优势比1.110也显著，属于互补型中介，10.2%被中介。

- rhetorical_function_cn：报告深度路径的核心结果。

- depends_on_cn：表11第一行。

- sets_up_cn：敏感性分析及加入考虑集规模后的变化。

- evidence_pointer：Section 5.3.2, Table 11

### 53. Section 5.3.2 P4 S1

- order：53

- section：Results

- locator：Section 5.3.2 P4 S1

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：将lnSetSize作为潜在混淆后，NIE仍显著但NDE变为不显著，中介类型变为间接-only，占比9.32%。

- rhetorical_function_cn：说明深度路径在控制广度后变得更强地与完全中介一致。

- depends_on_cn：表11第二行。

- sets_up_cn：引出双中介分析。

- evidence_pointer：Section 5.3.2, Table 11

### 54. Section 5.3.3 P1 S1

- order：54

- section：Results

- locator：Section 5.3.3 P1 S1

- move_code：RESULT

- paraphrase_cn：同时纳入两个中介后，合计中介39.2%总效应，直接效应不显著，是间接-only full mediation；广度贡献显著大于深度。

- rhetorical_function_cn：给出最终机制份额。

- depends_on_cn：前面两个单中介分析。

- sets_up_cn：讨论部分的理论意义。

- evidence_pointer：Section 5.3.3

### 55. Section 6.1 P1 S1

- order：55

- section：Discussion

- locator：Section 6.1 P1 S1

- move_code：THEORY_RETURN

- paraphrase_cn：作者称研究通过验证两个考虑集维度中介购买效应，揭示了推荐系统正面效果背后的机制。

- rhetorical_function_cn：把经验结果提升为对理论问题的回答。

- depends_on_cn：中介分析结果。

- sets_up_cn：下面依次回应考虑集大小的争论和卷入深度缺口。

- evidence_pointer：Section 6.1 P1

### 56. Section 6.1 P2 S1

- order：56

- section：Discussion

- locator：Section 6.1 P2 S1

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：作者用现场证据支持CF推荐扩大考虑集；并与Haubl等实验室结果不一致，提出可能解释包括推荐算法类型、启动效应和推荐准确度。

- rhetorical_function_cn：处理与既有理论的矛盾并给出边界解释。

- depends_on_cn：之前的现场证据。

- sets_up_cn：为未来研究指明算法和情境条件。

- evidence_pointer：Section 6.1 P2

### 57. Section 6.1 P3 S1

- order：57

- section：Discussion

- locator：Section 6.1 P3 S1

- move_code：CONTRIBUTION

- paraphrase_cn：作者提出以往研究用总卷入难以区分规模与卷入；用每个备选项卷入提供更细粒度视角，并发现深度确实中介且弱于广度。

- rhetorical_function_cn：强调方法/构念层面的新贡献。

- depends_on_cn：深度操作化。

- sets_up_cn：转向启发式决策讨论。

- evidence_pointer：Section 6.1 P3

### 58. Section 6.1 P4 S1

- order：58

- section：Discussion

- locator：Section 6.1 P4 S1

- move_code：THEORY_RETURN

- paraphrase_cn：消费者使用非补偿性启发式形成考虑集、用补偿性启发式比较备选；推荐系统促使两类过程更活跃。

- rhetorical_function_cn：将结果连接到决策启发式理论。

- depends_on_cn：广度与深度同时增加的事实。

- sets_up_cn：给机制赋予认知理论意义。

- evidence_pointer：Section 6.1 P4

### 59. Section 6.2 P1 S1

- order：59

- section：Discussion

- locator：Section 6.2 P1 S1

- move_code：CONTRIBUTION

- paraphrase_cn：在线零售商可通过推荐排序、显示偏好接近度分数和比较矩阵工具来促进考虑集形成与比较。

- rhetorical_function_cn：把机制发现转化为可操作设计建议。

- depends_on_cn：考虑集中介结果。

- sets_up_cn：提出延长而非缩短顾客旅程的设计哲学。

- evidence_pointer：Section 6.2 P1-P3

### 60. Section 6.3 P1 S1

- order：60

- section：Discussion

- locator：Section 6.3 P1 S1

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：因现场控制组为无推荐，估计效应包含表层可见效应；虽然试点实验显示随机推荐不优于无推荐，但现场未分离表层效应。

- rhetorical_function_cn：明确外部有效性和解释边界。

- depends_on_cn：控制条件选择。

- sets_up_cn：后续局限和未来研究。

- evidence_pointer：Section 6.3 P1

### 61. Section 6.3 P2-P4

- order：61

- section：Discussion

- locator：Section 6.3 P2-P4

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：作者承认未使用畅销推荐作为控制、只测试记忆型CF、且只销售图书，限制了对其他推荐算法和产品类型的可推广性。

- rhetorical_function_cn：划定边界条件并指出未来方向。

- depends_on_cn：现场实验的单一情境。

- sets_up_cn：结束全文。

- evidence_pointer：Section 6.3 P2-P4

## 写作技术

- gap_construction_cn：先承认领域共识（推荐系统提高销售），再指出现有研究把‘降低搜索成本’当作假设而非检验对象，最后用‘没有探索因果路径/中介因素’来定义缺口；随后进一步把缺口收缩到‘考虑集’这一具体构念，并以De等人只猜测而未检验为例。

- signposting_cn：引言结尾直接宣布研究方法与结果；文献综述按‘销售效果’和‘销售多样性’两个流组织，并在每节末指出缺口；理论部分先给总体模型再分小节讨论两个维度；结果部分按‘总效应→合规定义→单一中介→双中介’层层推进。

- transition_logic_cn：从文献缺口转入理论；从理论预测的矛盾性过渡到‘需要现场实验回答’；从试点实验确定参数过渡到现场实验设计；从ITT结果过渡到合规定义，再到‘下一步检验是否被中介’；从单一中介过渡到另一个中介，最后到两个中介合计。

- claim_evidence_rhythm_cn：几乎每个主张都紧跟表或图；即使在中介这类复杂方法中，也用表格呈现两步回归和NIE/NDE，紧接着用敏感性分析处理识别风险，再在讨论中把结果回接到理论，形成‘主张-证据-稳健性-理论含义’的节奏。

- benchmark_narrative_cn：文章不把benchmark作为性能竞赛，而是作为机制推理的控制阶梯：随机推荐/无推荐/畅销推荐用于确定基线；推荐数量用于确定处理强度；ITT vs ATT用于区别暴露与使用；NDE vs NIE用于区分直接与间接路径；单中介 vs 双中介用于比较机制份额。

- theory_return_cn：讨论部分不重复结果，而是把两个中介维度放回考虑集大小争论、卷入-承诺模型和启发式决策理论中，用现场证据选择或调和已有预测，并解释与实验室结果分歧的原因。

- contribution_positioning_cn：贡献按四条排列：机制缺口、考虑集方向争论、深度维度缺口、方法论引入；每条都对应引言或文献综述中的某个具体空白，确保贡献不是泛泛而谈。

- novelty_protection_cn：通过多阶段证据链防止‘一次性性能结果’：实验室试点支持设计选择、现场随机实验保证因果总效应、合规定义增强机制解释、因果中介提供路径分解、敏感性分析处理识别风险、稳健性检验排除另一中介混淆；这样即使具体效应量只适用一个书店，机制和分类学贡献仍保持。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：在引言先承认既有研究共识，再指出共识中的未检验假设，把缺口表述为‘缺少因果路径/中介机制’。

- research_job_cn：系统梳理现场推荐系统文献，识别总效应与机制之间的缝隙。

- required_evidence_cn：需要足够多现场研究证明总效应有共识而机制未检验；最好能找到一个文献中只猜测未检验的中介线索。

- transition_to_next_cn：由缺口自然引出新的理论构念。

#### 2. 2

- step：2

- writing_job_cn：用一到两节建立理论，把构念分解为两个可操作维度，并展示每个方向都有矛盾预测或经验问题。

- research_job_cn：从营销/IS文献中提取考虑集和卷入-承诺理论，推导两条中介路径。

- required_evidence_cn：需要文献同时提供正向和反向预测，才能把方向问题留给数据。

- transition_to_next_cn：既然方向是经验问题，下一阶段说明用实验回答。

#### 3. 3

- step：3

- writing_job_cn：在实验方法前先用试点实验为关键设计选择提供依据，报告试点设计、结果和选择理由。

- research_job_cn：执行小样本实验室实验，确定控制条件、推荐数量等现场实验参数。

- required_evidence_cn：需要试点结果显示无推荐可作为合理基线、所选推荐数量显著有效。

- transition_to_next_cn：由试点参数过渡到真实现场实验。

#### 4. 4

- step：4

- writing_job_cn：详细描述现场实验的随机化、处理/控制页面、测量变量、平衡性检验，并报告ITT和合规定义下的ATT。

- research_job_cn：在真实平台部署推荐系统，随机分配会话，记录购买、浏览和点击行为。

- required_evidence_cn：需要随机化平衡、总效应显著、且效应能归因于实际接触处理的人。

- transition_to_next_cn：总效应存在后，转问‘为什么’，引入中介方法。

#### 5. 5

- step：5

- writing_job_cn：用因果中介分析分别检验每个中介，并报告NIE/NDE、中介百分比、敏感性分析和稳健性检验。

- research_job_cn：用反事实中介模型分解总效应，执行敏感性分析，用交叉检验控制另一中介。

- required_evidence_cn：需要NIE显著、敏感性阈值表明结论不是极脆弱、稳健性检验结果一致。

- transition_to_next_cn：单个中介结果出来后，合并为双中介模型并比较路径贡献。

#### 6. 6

- step：6

- writing_job_cn：在讨论中把中介份额和路径强弱回接到理论争论、边界条件和实践建议，明确列出局限。

- research_job_cn：用结果选择/调和理论争辩，提出机制解释和边界条件，承认未覆盖的算法、产品类别和控制条件。

- required_evidence_cn：需要能够把百分比差异与具体理论机制联系起来。

- transition_to_next_cn：文章以贡献和未来研究结束。

### most_transferable_moves_cn

1. 用‘文献有共识但机制未检验’构造研究缺口。

2. 用两个实验室试点为现场实验设计参数提供辩护。

3. 把ITT与合规者ATT并列报告，增强处理效应解释力。

4. 在因果中介分析中加入暴露-中介交互项并做敏感性分析。

5. 在讨论中把中介结果放在两个对立理论预测之间做调和。

6. 通过控制另一个中介作为潜在混淆来加强单一中介结论。

### resource_intensive_or_nonstandard_parts_cn

1. 与真实在线书店合作并获得会话级点击/浏览/购买数据需要大量关系和信任。

2. 部署真实推荐系统并保持随机分配稳定需要工程实现和实验平台支持。

3. 实验室试点需要招募被试、收集评分、构建实验商店。

4. 因果中介分析需要专业统计工具和充分的敏感性分析实践。

### what_not_to_copy_superficially_cn

1. 不能直接写‘效应由考虑集中介’而没有现场随机实验和中介数据。

2. 不能只报告NIE/NDE而不做敏感性分析。

3. 不能把浏览行为直接等同于心理考虑集而不讨论操作化与代理假设。

4. 不能把无推荐控制效应解释为纯个性化推荐效应而不处理表层可见效应。

- single_best_description_of_the_routine_cn：先找共识里的未检验假设，用一个理论构念把假设拆成两条并行机制，用试点实验确定现场实验参数，再用随机现场数据证明总效应、用因果中介和敏感性分析证明路径效应，最后把路径强弱变成理论贡献。

## 分析边界

分析基于OCR全文，无法看到在线附录A-D、完整图表原有版式及图3细节；因果中介的顺序可忽略性假定本身不可检验，文中以敏感性分析近似；正文只报告以Order为结果变量的中介结果，lnOrderVal等结果以脚注说明可提供但未展示；双中介中的路径顺序和相关性未被建模。
