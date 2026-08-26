# Ephemeral State-Dependent Recommendation for Digital Content

- 作者：Lanfei Shi; Jin Liu; Yongjun Li; Natasha Zhang Foutz
- 年份 / 期刊：2025 / Information Systems Research
- DOI：10.1287/isre.2022.664
- 源文件：28570_2025_ephemeral-state-dependent-recommendation-for-digital-content.md
- 论文主类型：field_intervention_or_platform_experiment
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.78

## 文章级论证概况

- 核心问题：数字内容消费具有瞬时性和短暂性，数字内容平台应否根据消费者当下的短暂状态（fixation vs. foraging）动态调整“同化型”还是“多样型”推荐策略？状态依赖推荐是否优于状态独立推荐？若存在优势，congruent（一致）与incongruent（不一致）这两种策略-状态配对方案分别对哪些消费者更有效？

- 制品与设计：提出一个“短暂状态依赖推荐框架”（ephemeral state-dependent recommendation framework），将推荐策略（assimilation/diversification）与消费者当下短暂状态（fixation/foraging）配对，形成核心的两种状态依赖方案：T3（incongruent scheme，foraging时assimilation、fixation时diversification）和T4（congruent scheme，fixation时assimilation、foraging时diversification）。为得到干净识别，实验刻意采用简单、基于genre的规则算法，不绑定任何特定推荐算法。

- 客观结果：在大规模随机田野实验中，状态依赖方案T3/T4显著优于状态独立方案T1/T2；总体上congruent方案T4优于incongruent方案T3，提升阅读率和阅读时间，并带来支付增加，作者外推称T4可为平台年收入带来约1973万美元、即7.3%的提升。异质性分析发现，偏好更流动、偏好广度更宽、参与度更高的用户对T3反应更好。状态依赖方案对非推荐内容产生正向需求溢出，T4同时有品类内和跨品类溢出，T3主要体现跨品类溢出。在线调查显示Schema效应偏爱congruent方案，Isolation效应偏爱incongruent方案。

- 核心贡献：作者声称将数字内容消费的“短暂性”（ephemerality in preference and consumption state）整合进推荐系统，首次通过真实平台大规模随机田野实验证明“策略-状态配对”（strategy-state pairing）的价值；引入一种新的一致性类型“策略-状态一致性”（strategy-state congruence），并用消费者异质性解释congruence文献中的混合结论；发现对非推荐内容的正向需求溢出，强调应以平台整体需求而非仅推荐内容来评估推荐系统。

- 整篇论证链：论文从数字内容平台市场体量巨大出发，指出现有推荐系统主要基于长期持久偏好或单一assimilation/diversification算法，忽略了数字内容消费的瞬时性与短暂状态。作者利用液体消费理论（liquid consumption）和选择理论将短暂性拆成瞬时偏好与短暂状态，用foraging/fixation刻画当下状态；又用congruence theory推导出congruent和incongruent两种状态依赖方案，但因文献对congruence/incongruence孰优孰劣存在混合证据，需要现场实验裁决。于是作者与大型电子书平台合作，设计2×2策略×状态矩阵，并增加两个基于enduring preference的对照组，随机分配108,158名用户到六组，比较C1/C2、T1/T2与T3/T4。结果显示状态依赖优于状态独立，T4总体优于T3；但T3在偏好流动、偏好宽、高参与用户中更优。支付与收入外推支持经济价值，非推荐内容溢出强化整体价值；在线调查用Schema/Isolation效应提供机制线索。最终作者把贡献放回推荐系统、congruence和spillover文献，并提出平台可按用户特质选择不同方案。

## 类型与写作弧线判定

- 论文主类型判定：文章的核心证据来自真实电子书平台上的大规模随机田野实验，研究者操纵六种推荐方案观察阅读、支付和溢出行为；虽然有理论推导和在线调查，但主要因果主张由平台现场实验支撑，属于平台现场干预实验的写作与研究套路。

- 主导写作弧线判定：全文遵循“问题—理论—设计—检验—回到理论”的弧线：先提出数字内容短暂性被忽视的问题，再用消费理论与一致性理论推导出状态依赖框架，接着设计与执行随机田野实验，最后用结果回填和扩展理论缺口。

## 研究开展程序

- study_or_phase_count：6

- 研究阶段总序列：第一阶段完成构念操作化与预检验，为实验定义ephemeral preference和ephemeral state；第二阶段执行大规模随机田野实验并估计主效应；第三阶段在T3/T4子样本上做异质性分析；第四阶段扩展至支付、收入外推和需求溢出；第五阶段做一系列稳健性检验；第六阶段用在线调查提供机制初探。各阶段依次解决“测量是否可信—状态依赖是否有效—哪种方案对谁有效—价值是否够大—结果是否稳健—为什么会有这种结果”的累积问题。

### studies_or_phases

#### 1. 构念操作化与预验证

- order：1

- name_cn：构念操作化与预验证

- question_cn：如何把瞬时偏好和短暂状态转化为可执行的推荐规则？

- inputs_and_setting_cn：平台管理者的领域建议、1,294名随机抽取用户的阅读行为、书籍内容embedding分析。

- designed_or_compared_object_cn：ephemeral preference用滚动7天窗口、enduring preference用3个月窗口；ephemeral state用二元状态：7天内只读一种genre为fixation，两种及以上为foraging。

- baseline_control_or_counterfactual_cn：没有严格对照，主要与平台惯用做法和学术界genre测量惯例对照。

##### objective_metrics

1. genre识别效度（同genre内容距离显著小于跨genre）

2. 7天/3个月窗口对消费周期的匹配度

- analysis_method_cn：对用户阅读行为进行描述性检视，并用内容embedding的t检验验证genre边界。

- main_result_cn：7天和3个月窗口得到平台和管理者确认，genre作为偏好测量有效，二元foraging/fixation状态可操作。

- argumentative_role_cn：为实验分组提供构念效度，避免结果无法归因到理论构念。

- remaining_uncertainty_cn：构念测量合理并不等于行为上状态依赖推荐有效。

- link_to_next_phase_cn：提供实验需要的变量定义，直接引出六组实验设计。

##### evidence_pointers

1. 第3.1节

2. Online Appendix B

3. 第4.5.3节

#### 2. 大规模随机田野实验：阅读主效应

- order：2

- name_cn：大规模随机田野实验：阅读主效应

- question_cn：状态依赖方案是否优于状态独立方案？congruent方案T4与incongruent方案T3哪个总体更好？

- inputs_and_setting_cn：108,158名在实验前一周有阅读的活跃用户；2020年9月1日至5日连续5天每天推荐；观测12天以跟踪阅读行为；电子书分20种genre。

- designed_or_compared_object_cn：六种推荐方案：C1/C2基于enduring preference，T1/T2基于ephemeral preference但状态独立，T3/T4基于ephemeral preference和ephemeral state。

- baseline_control_or_counterfactual_cn：C1（always assimilation based on enduring preference）为基准，并以T1/T2作为状态独立的中间基准。

##### objective_metrics

1. readrate（推荐书中被阅读至少一章的比例）

2. readtime（阅读推荐书的总时长）

- analysis_method_cn：随机化平衡检验（ANOVA），连续变量用OLS，占比变量用Fractional Logit，并用Wald检验比较T3/T4与T1/T2。

- main_result_cn：状态依赖方案T3/T4显著优于状态独立方案T1/T2；T4在readrate和readtime上显著优于T3。

- argumentative_role_cn：回答RQ1和RQ2的总体部分，确立“策略-状态配对”和“strategy-state congruence”的核心因果证据。

- remaining_uncertainty_cn：总体效应掩盖了消费者异质性，也未说明心理机制。

- link_to_next_phase_cn：总体T4优势促使作者进一步考察哪些消费者更可能从incongruent T3中获益。

##### evidence_pointers

1. 第3.2节

2. 第4.2节

3. Table 4

#### 3. 异质性处理效应分析

- order：3

- name_cn：异质性处理效应分析

- question_cn：congruent方案T4对哪些消费者更有效，incongruent方案T3对哪些消费者更有效？

- inputs_and_setting_cn：仅聚焦T3和T4两组，子样本35,957个观测；使用实验前偏好稳定性、偏好广度、参与度作为调节变量。

- designed_or_compared_object_cn：在T3为基准的回归中加入T4与三个用户特质的交互项。

- baseline_control_or_counterfactual_cn：T3（incongruent）作为基准组，T4与T3的差异由交互项识别。

##### objective_metrics

1. readrate

2. readtime

- analysis_method_cn：带交互项的Fractional Logit和OLS回归，并检验各特质在组间平衡。

- main_result_cn：偏好稳定性低、偏好广度宽、参与度高的用户对T3反应更好；偏好稳定性高的用户对T4反应更好。

- argumentative_role_cn：说明“没有一刀切方案”，为个性化推荐提供依据，并部分解释congruence文献的混合发现。

- remaining_uncertainty_cn：这些特质为何导致不同反应，仍需要机制证据。

- link_to_next_phase_cn：异质性结果引向在线调查中的Schema/Isolation机制。

##### evidence_pointers

1. 第4.3.1-4.3.3节

2. Table 5

#### 4. 支付、收入外推与需求溢出分析

- order：4

- name_cn：支付、收入外推与需求溢出分析

- question_cn：状态依赖方案是否影响支付？是否能带来平台级利润提升？是否以牺牲非推荐内容为代价？

- inputs_and_setting_cn：同一田野实验数据；支付金额；非推荐书的阅读计数（同品类、跨品类、总体）。

- designed_or_compared_object_cn：比较T3/T4在支付和非推荐阅读上与C1及T1/T2的差异。

- baseline_control_or_counterfactual_cn：C1为基准；用T1/T2作为状态独立基准。

##### objective_metrics

1. payment（支付金额）

2. 非推荐书阅读数量（overall/focal_category/other_categories）

3. 年收入外推值

- analysis_method_cn：支付用回归分析，非推荐阅读计数用Negative Binomial回归，另做back-of-the-envelope年收入外推。

- main_result_cn：状态依赖方案带来更高支付；T4外推带来约1973万美元年收入提升；T3和T4均对非推荐内容有正向溢出，其中T4同时提升品类内和跨品类，T3主要提升跨品类。

- argumentative_role_cn：把阅读参与转化为平台利润，并证明只看推荐内容的评估会低估状态依赖框架的价值。

- remaining_uncertainty_cn：收入提升依赖外推假设；溢出可能部分反映推荐本身的发现效应而非纯粹策略效应。

- link_to_next_phase_cn：经济价值与溢出证据支持结论中的管理启示。

##### evidence_pointers

1. 第4.4.1节

2. 第4.4.2节

3. 第4.4.3节

4. Table 6

5. Online Appendix C Table C1

#### 5. 稳健性检验

- order：5

- name_cn：稳健性检验

- question_cn：主结果是否受时间窗、模型设定、genre测量、状态操作化、识别策略和季节性的影响？

- inputs_and_setting_cn：同一实验数据；书籍内容embedding；1,294名用户月度genre分布；不同时间窗口和子样本。

- designed_or_compared_object_cn：替换因变量观测窗口、替换模型、替换ephemeral state为连续内容相似度、排除偶尔foraging者、控制engagement depth、做首日/日度面板分析、排除开学季学生。

- baseline_control_or_counterfactual_cn：以主结果Table 4为基准，比较各替代设定下的系数方向和显著性。

##### objective_metrics

1. readrate

2. readtime

3. 支付与阅读相关指标在替代设定下的显著性

- analysis_method_cn：多种回归模型、内容embedding t检验、连续状态分位数分类、日度面板。

- main_result_cn：所有稳健性检验下结果一致。

- argumentative_role_cn：保护主效应和构念测量的内部效度，增强结论的一般性。

- remaining_uncertainty_cn：连续ephemeral state未在新实验中检验，只在现有样本中模拟。

- link_to_next_phase_cn：稳健性为后续贡献主张提供可信基础。

##### evidence_pointers

1. 第4.5节

2. Online Appendix D

3. Online Appendix E

#### 6. 在线调查：Schema与Isolation机制

- order：6

- name_cn：在线调查：Schema与Isolation机制

- question_cn：为什么有些消费者偏好congruent方案、有些偏好incongruent方案？

- inputs_and_setting_cn：281名参与者，通过Credamo平台在线调查，采用组间设计，分为congruent与incongruent方案组。

- designed_or_compared_object_cn：比较两组参与者的Schema效应和Isolation效应评分差异。

- baseline_control_or_counterfactual_cn：以congruent组为参照，对比incongruent组的心理效应评分。

##### objective_metrics

1. Schema效应评分

2. Isolation效应评分

3. 阅读意愿相关题项

- analysis_method_cn：t检验比较Likert量表评分。

- main_result_cn：更偏好congruent方案的消费者Schema效应更强；更偏好incongruent方案的消费者Isolation效应更强。

- argumentative_role_cn：为T3/T4异质性提供初步心理机制证据，并连接congruence文献的两种相反理论。

- remaining_uncertainty_cn：调查不是对田野实验参与者的真实推荐行为中介检验，机制证据是探索性的。

- link_to_next_phase_cn：进入结论部分，把机制解释与理论贡献整合。

##### evidence_pointers

1. 第4.6节

2. Online Appendix F

## 各部分修辞架构

### abstract_moves

1. CONTEXT：数字内容平台规模与推荐系统重要性

2. LIMITATION：现有推荐系统忽略短暂的消费状态

3. DESIGN_FEATURE：提出ephemeral state-dependent framework和策略-状态配对

4. STUDY_OVERVIEW：大规模随机田野实验

5. RESULT：状态依赖方案总体优于状态独立，congruent整体更优但存在异质性

6. RESULT：对非推荐内容有溢出效应

7. CONTRIBUTION：将理论驱动设计引入推荐系统并提供管理洞见

### introduction_moves

1. CONTEXT：市场体量和推荐系统价值

2. LIMITATION：数字内容消费的短暂性未被推荐系统考虑

3. THEORY_INTRO：引入瞬时偏好与短暂状态

4. PRIOR_KNOWLEDGE：消费者同时需要一致性与多样性

5. WHY_GAP_MATTERS：策略与状态的交互具有理论与实践重要性

6. GAP：状态依赖情况下同化还是多样推荐尚未解决

7. RQ_OR_OBJECTIVE：提出RQ1和RQ2

8. STUDY_OVERVIEW：预告六组随机田野实验

9. RESULT：预告主要发现与贡献

### theory_and_knowledge_moves

1. THEORY_INTRO：液体消费理论解释数字内容短暂性

2. THEORY_PROPOSITION：瞬时偏好 vs. 持久偏好

3. THEORY_PROPOSITION：foraging vs. fixation状态

4. REQUIREMENT：推荐系统应平衡一致性与多样性

5. THEORY_INTRO：congruence theory定义

6. LIMITATION：congruence/incongruence文献存在混合证据

7. MECHANISM：Schema effect与Isolation effect形成相反力量

8. PRIOR_KNOWLEDGE：推荐系统文献集中于实体消费和单一算法

9. GAP：缺少状态依赖和策略-状态配对

### artifact_design_moves

1. CONTEXT：合作平台、月活、genre结构

2. DESIGN_FEATURE：ephemeral preference与ephemeral state的操作化

3. BENCHMARK_OR_CONTRAST：C1/C2、T1/T2、T3/T4六组设计

4. METHOD_JUSTIFICATION：使用简单规则算法以保证识别

5. DESIGN_FEATURE：实时自适应选择同化或多样策略

6. METHOD_JUSTIFICATION：样本规模、重复推荐、12天观测

### evaluation_moves

1. METHOD_JUSTIFICATION：随机化平衡检验

2. METHOD_JUSTIFICATION：Fractional Logit与OLS

3. RESULT：状态依赖优于状态独立

4. RESULT：T4优于T3

5. TRANSITION：异质性分析

6. RESULT：三类用户特质调节

7. RESULT：支付与收入外推

8. RESULT：需求溢出

9. STUDY_OVERVIEW：稳健性检验

10. ROBUSTNESS_OR_BOUNDARY_TEST：连续状态模拟

11. STUDY_OVERVIEW：在线调查机制

### discussion_and_contribution_moves

1. CONTRIBUTION：总结关键发现

2. CONTRIBUTION：理论贡献（推荐、congruence、spillover三大文献）

3. CONTRIBUTION：管理含义

4. BOUNDARY_CONDITION：框架不限于电子书，可推广至视频/音频但需调整时间窗

5. LIMITATION_AND_FUTURE：算法、状态测量、机制、溢出、长期效果等方面的限制

## 理论/知识到设计的翻译

### 知识/理论基础

1. 液体消费理论（liquid consumption）

2. 选择理论与瞬时偏好（ephemeral preference）

3. variety-seeking与同化/多样化双需求文献

4. congruence theory

5. Schema effect与Isolation effect

6. 推荐系统与需求溢出文献

- 理论—设计耦合：direct

- 耦合判定理由：理论构念直接决定了核心制品的设计：短暂状态（foraging/fixation）和推荐策略（assimilation/diversification）的配对形成了T3/T4两个方案，而田野实验直接检验这一理论驱动的方案差异。具体算法实现选择简单规则是为了识别干净，非理论驱动，但策略-状态配对本身来自理论。

- 理论到设计翻译链：液体消费的短暂性 → 瞬时偏好与短暂状态 → 消费者在内容消费中有双需求（一致性与多样性） → 推荐系统需根据当下foraging/fixation状态自适应部署同化或多样策略 → congruence theory给出congruent/incongruent两种策略-状态配对 → 用简单genre规则算法实现assimilation/diversification → 六组实验比较状态依赖与状态独立 → 结果支持策略-状态配对价值，并用异质性与心理机制解释谁更适合哪种方案。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：数字内容消费是液体消费，具有短暂性，瞬时偏好和短暂状态驱动当下选择

- mechanism_cn：当下的ephemeral preference breadth表现为fixation或foraging，影响消费者对推荐内容的接受度

- design_requirement_cn：推荐系统应基于ephemeral preference和ephemeral state，而不是只基于enduring preference

- artifact_choice_cn：用7天窗口测量ephemeral preference，二元化ephemeral state，形成T1/T2/T3/T4

- evaluated_contrast_cn：T3/T4（状态依赖） vs. T1/T2（状态独立） vs. C1/C2（enduring基准）

- objective_result_cn：状态依赖方案显著提升readrate和readtime

##### evidence_pointers

1. Table 4

2. 第4.2节

#### 2. 2

- theory_or_knowledge_claim_cn：消费者需要一致性也需要多样性，同化满足熟悉舒适，多样满足刺激并减少饱足

- mechanism_cn：推荐策略应与当下状态匹配：fixation时给熟悉内容、foraging时给多样内容

- design_requirement_cn：自适应地在同化和多样化之间切换

- artifact_choice_cn：T4：fixation→assimilation，foraging→diversification；T3做相反配对

- evaluated_contrast_cn：T4（congruent） vs. T3（incongruent）

- objective_result_cn：总体T4优于T3

##### evidence_pointers

1. Table 4

2. T3=T4的Wald检验

#### 3. 3

- theory_or_knowledge_claim_cn：congruence theory主张组件间一致有效，但文献混合

- mechanism_cn：一致性降低处理难度，不一致性吸引注意；两种力量并存

- design_requirement_cn：需要识别哪些消费者从一致或非一致配对中获益

- artifact_choice_cn：在T3/T4子样本中引入偏好稳定性、偏好广度、参与度交互

- evaluated_contrast_cn：T4 vs. T3在不同用户特质水平下的差异

- objective_result_cn：流动/宽/高参与用户更偏好T3；高稳定用户更偏好T4

##### evidence_pointers

1. Table 5

2. 第4.3节

#### 4. 4

- theory_or_knowledge_claim_cn：Schema effect支持一致信息，Isolation effect支持意外信息

- mechanism_cn：消费者对congruent推荐更易加工，对incongruent推荐更易被吸引

- design_requirement_cn：机制检验应同时测两种相反心理效应

- artifact_choice_cn：在线调查中随机分配congruent/incongruent方案，测量Schema和Isolation

- evaluated_contrast_cn：两个方案组的Schema/Isolation评分差异

- objective_result_cn：偏好congruent者Schema更强，偏好incongruent者Isolation更强

##### evidence_pointers

1. 第4.6节

#### 5. 5

- theory_or_knowledge_claim_cn：需求溢出文献已识别同化策略的积极外部性

- mechanism_cn：状态依赖推荐可能改变消费者在推荐内容之外的阅读广度

- design_requirement_cn：评价新方案时应检查对非推荐内容的溢出

- artifact_choice_cn：用Negative Binomial回归分析非推荐书的阅读量（同品类/跨品类/总体）

- evaluated_contrast_cn：T3/T4 vs. C1/T1/T2对非推荐内容阅读的影响

- objective_result_cn：T3/T4均产生正向溢出，T4同时提升品类内和跨品类

##### evidence_pointers

1. Table 6

2. 第4.4.3节

## 评价逻辑

### evaluation_modes

1. 大规模随机田野实验（between-subject，六组）

2. Fractional Logit与OLS回归

3. Wald检验进行方案间两两比较

4. 异质性交互分析

5. Negative Binomial溢出回归

6. Back-of-the-envelope收入外推

7. 在线调查与t检验

8. 系列稳健性检验

- why_these_evaluations_cn：为了回答状态依赖是否优于状态独立，需要随机化分配并比较六组；为了回答congruent还是incongruent更适合谁，需要在T3/T4之间做对比并加入用户特质交互；为了把参与提升转化为平台价值，需要支付和收入外推；为了说明方案不会因推荐内容挤占其他阅读而净效应为零，需要溢出分析；为了解释为什么不同消费者偏好不同方案，需要在线调查；为了排除操作化与识别问题，需要多组稳健性检验。

- benchmark_and_contrast_chain_cn：C1/C2提供enduring preference下的现状基准；T1/T2在ephemeral preference下但状态独立，用于剥离ephemeral state本身的价值；T3/T4构成核心状态依赖对比。先由C1→T1/T2显示ephemeral preference优于enduring；再由T1/T2→T3/T4显示状态依赖优于状态独立；最后T3 vs. T4回答策略-状态配对方向。在异质性环节，以T3为基准通过交互项检验T4在不同用户群体中的相对表现。

### claim_evidence_ledger

#### 1. 状态依赖方案优于状态独立方案

- claim_cn：状态依赖方案优于状态独立方案

- evidence_cn：Wald检验显示T4 vs. T1在readrate和readtime上显著，T3/T4整体优于状态独立组

- status_cn：支持

#### 2. congruent方案T4总体优于incongruent方案T3

- claim_cn：congruent方案T4总体优于incongruent方案T3

- evidence_cn：T3=T4的Wald检验：readrate p<0.0001，readtime p=0.005

- status_cn：支持

#### 3. T3对偏好更流动、广度更宽、参与度更高的消费者更有效

- claim_cn：T3对偏好更流动、广度更宽、参与度更高的消费者更有效

- evidence_cn：Table 5中T4×X交互项在偏好稳定性上为正、在偏好广度为负、在参与度为负，均显著

- status_cn：支持

#### 4. 状态依赖方案提升支付

- claim_cn：状态依赖方案提升支付

- evidence_cn：Online Appendix C Table C1显示支付结果与阅读结果一致

- status_cn：支持，但正文仅引用附录

#### 5. T4可带来约1973万美元年收入提升

- claim_cn：T4可带来约1973万美元年收入提升

- evidence_cn：back-of-the-envelope外推，基于支付回归系数、24.3百万付费用户和每天一次推荐

- status_cn：依赖外推假设

#### 6. 状态依赖方案对非推荐内容产生正向需求溢出

- claim_cn：状态依赖方案对非推荐内容产生正向需求溢出

- evidence_cn：Table 6 Negative Binomial回归显示T3和T4的总体溢出显著为正

- status_cn：支持

#### 7. Schema效应解释congruent偏好，Isolation效应解释incongruent偏好

- claim_cn：Schema效应解释congruent偏好，Isolation效应解释incongruent偏好

- evidence_cn：在线调查t检验：Schema题项T3评分高于T4，Isolation题项T3低于T4

- status_cn：探索性支持

- internal_validity_strategy_cn：使用随机化分配和随机化平衡检验；采用between-subject设计避免跨组污染；刻意使用简单规则算法以避免算法复杂度混淆；在五天中重复推荐以匹配平台实际使用；额外分析首两日、日度面板、控制前一期阅读，以处理消费依赖与时间异质性。

- external_validity_strategy_cn：样本为真实平台的108,158名活跃用户；genre作为偏好测量通过内容embedding验证；检验季节性和排除学生样本；主张框架可推广到其他数字内容类型，但建议按消费周期调整ephemeral state的时间窗口。

- what_is_not_actually_tested_cn：连续型ephemeral state没有在新实验中直接测试，只在现有样本中通过子样本模拟；在线调查不是对同一批真实用户推荐行为的中介检验，机制结论是探索性的；收入外推并非平台会计利润；对非推荐内容的溢出无法完全排除“推荐本身促进内容发现”的效应；未研究idle/inactive用户的“空闲状态”。

## 贡献闭环

- technical_claim_cn：状态依赖策略-状态配对框架比状态独立方案在阅读、支付和溢出上更有效。

- artifact_claim_cn：具体驱动改进的是“根据瞬时状态自适应切换assimilation/diversification”这一设计，尤其是congruent方案T4。

- mechanism_claim_cn：短暂状态影响消费者对同化或多样化内容的偏好；Schema effect使部分消费者偏好一致推荐，Isolation effect使另一部分消费者偏好意外推荐。

- boundary_claim_cn：congruent方案总体更优，但incongruent方案对偏好更流动、偏好广度更宽、参与度更高的消费者更有利；框架不绑定具体算法，但需根据内容消费周期调整状态测量时间窗。

- reusable_design_knowledge_cn：数字内容推荐应把推荐策略与消费者的短暂状态配对；评估推荐方案应同时考察推荐内容和非推荐内容的消费变化；不存在对所有用户都最优的单一方案，需按偏好稳定性、偏好广度和参与度做精细个性化。

- theoretical_contribution_cn：把液体消费/短暂性概念引入推荐系统研究；提出并检验“策略-状态一致性”这一新的一致性类型，解释congruence文献的混合发现；把需求溢出文献从同化策略扩展到状态依赖推荐，并区分品类内与跨品类溢出。

- how_discussion_closes_intro_gap_cn：引言提出“状态依赖是否更优”和“congruent还是incongruent适合谁”两个问题；结论用田野实验的总体效应回答第一个问题，用异质性分析和在线调查回答第二个问题，并把溢出和非推荐内容效应作为附加价值，重新接入推荐系统、congruence和spillover三个文献缺口。

- overclaim_or_unsupported_leaps_cn：从支付回归系数外推到全年1973万美元依赖“每天一次推荐、全平台付费用户、效应稳定”等强假设；在线调查的Schema/Isolation效应并非对田野实验用户的真实推荐行为做中介检验，因此机制主张是探索性而非因果；声称“更复杂的算法可能带来更大收益”属于推测；溢出效应可能部分反映推荐本身的信息价值。

## 句级写作动作图谱

### 1. Introduction P1

- order：1

- section：Introduction

- locator：Introduction P1

- move_code：CONTEXT

- paraphrase_cn：数字内容平台市场规模巨大且快速扩张，推荐系统对匹配海量内容与用户非常重要。

- rhetorical_function_cn：为研究设置经济和实践重要性。

- depends_on_cn：无。

- sets_up_cn：引出推荐系统需要被更好设计的问题。

- evidence_pointer：第1节第1段

### 2. Introduction P1

- order：2

- section：Introduction

- locator：Introduction P1

- move_code：LIMITATION

- paraphrase_cn：物理商品推荐更成熟，数字内容推荐因消费行为独特而面临挑战，尤其短暂性常被忽略。

- rhetorical_function_cn：建立现有推荐系统与数字内容特征之间的缺口。

- depends_on_cn：市场规模背景。

- sets_up_cn：引出短暂性构念。

- evidence_pointer：第1节第1段

### 3. Introduction P2

- order：3

- section：Introduction

- locator：Introduction P2

- move_code：THEORY_INTRO

- paraphrase_cn：数字内容消费的短暂性由瞬时偏好与短暂状态两个维度构成，短暂状态可用瞬时偏好广度衡量。

- rhetorical_function_cn：引入本文的核心理论概念。

- depends_on_cn：数字内容特性被忽视的缺口。

- sets_up_cn：定义fixation和foraging。

- evidence_pointer：第1节第2段

### 4. Introduction P2

- order：4

- section：Introduction

- locator：Introduction P2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：短暂状态能刻画用户当下是专注于单一内容还是跨类型觅食，并预测后续选择。

- rhetorical_function_cn：说明短暂状态具有行为预测价值。

- depends_on_cn：短暂性概念。

- sets_up_cn：为状态依赖推荐提供必要性和合法性。

- evidence_pointer：第1节第2段

### 5. Introduction P3

- order：5

- section：Introduction

- locator：Introduction P3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：行为理论指出消费者在内容消费中同时有对一致性和多样性的双重需求。

- rhetorical_function_cn：引入第二个理论支柱，解释推荐策略为何需要同化和多样化。

- depends_on_cn：短暂性概念。

- sets_up_cn：说明推荐系统应平衡这两种需求。

- evidence_pointer：第1节第3段

### 6. Introduction P3

- order：6

- section：Introduction

- locator：Introduction P3

- move_code：MECHANISM

- paraphrase_cn：消费者是否接受相似或不同推荐取决于当下的foraging或fixation状态。

- rhetorical_function_cn：建立策略-状态交互机制。

- depends_on_cn：双需求与短暂状态。

- sets_up_cn：引出策略-状态配对框架。

- evidence_pointer：第1节第3段

### 7. Introduction P3

- order：7

- section：Introduction

- locator：Introduction P3

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：因此把推荐策略与短暂状态的交互纳入推荐系统，在理论和实践上都至关重要。

- rhetorical_function_cn：提升研究缺口的重要性。

- depends_on_cn：前一句的机制。

- sets_up_cn：研究问题。

- evidence_pointer：第1节第3段

### 8. Introduction P4

- order：8

- section：Introduction

- locator：Introduction P4

- move_code：GAP

- paraphrase_cn：尽管有这些洞见，平台在用户fixation或foraging时到底应推荐同化还是多样内容仍不清楚。

- rhetorical_function_cn：明确研究缺口。

- depends_on_cn：理论重要性。

- sets_up_cn：提出状态依赖框架。

- evidence_pointer：第1节第4段

### 9. Introduction P4

- order：9

- section：Introduction

- locator：Introduction P4

- move_code：DESIGN_FEATURE

- paraphrase_cn：作者提出ephemeral state-dependent框架，把推荐策略与消费者当下短暂状态配对，称为recommendation scheme。

- rhetorical_function_cn：引入核心制品并给出命名。

- depends_on_cn：缺口。

- sets_up_cn：定义congruent/incongruent方案。

- evidence_pointer：第1节第4段

### 10. Introduction P5

- order：10

- section：Introduction

- locator：Introduction P5

- move_code：THEORY_INTRO

- paraphrase_cn：根据congruence theory，状态依赖方案存在两种配对：congruent和incongruent。

- rhetorical_function_cn：用理论界定方案空间。

- depends_on_cn：状态依赖框架。

- sets_up_cn：T3与T4的定义。

- evidence_pointer：第1节第5段

### 11. Introduction P5

- order：11

- section：Introduction

- locator：Introduction P5

- move_code：LIMITATION

- paraphrase_cn：congruence文献在不同情境中对congruent还是incongruent更好有混合实证发现。

- rhetorical_function_cn：说明理论无法先验裁决。

- depends_on_cn：congruence theory。

- sets_up_cn：需要田野实验。

- evidence_pointer：第1节第5段

### 12. Introduction P5

- order：12

- section：Introduction

- locator：Introduction P5

- move_code：GAP

- paraphrase_cn：在数字内容推荐这一新情境中，哪个方案更有利于平台或消费者仍是开放问题。

- rhetorical_function_cn：把一般理论矛盾落到具体研究情境。

- depends_on_cn：混合证据。

- sets_up_cn：研究问题。

- evidence_pointer：第1节第5段

### 13. Introduction P5

- order：13

- section：Introduction

- locator：Introduction P5

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：提出RQ1：状态依赖方案是否优于状态独立方案；RQ2：平台应部署哪个具体方案并针对哪类消费者。

- rhetorical_function_cn：正式提出研究问题。

- depends_on_cn：理论缺口。

- sets_up_cn：实验设计。

- evidence_pointer：第1节第5段

### 14. Introduction P6

- order：14

- section：Introduction

- locator：Introduction P6

- move_code：STUDY_OVERVIEW

- paraphrase_cn：与大型电子书平台合作，开展大规模随机田野实验，样本为108,158名活跃用户。

- rhetorical_function_cn：说明实证策略。

- depends_on_cn：研究问题。

- sets_up_cn：六组设计。

- evidence_pointer：第1节第6段

### 15. Introduction P6

- order：15

- section：Introduction

- locator：Introduction P6

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：实验包含两个enduring偏好控制组、两个ephemeral偏好状态独立处理组和两个状态依赖处理组，共六组。

- rhetorical_function_cn：建立多层次对照架构。

- depends_on_cn：研究问题。

- sets_up_cn：后续结果解释。

- evidence_pointer：第1节第6段，Tables 1-2

### 16. Introduction P7

- order：16

- section：Introduction

- locator：Introduction P7

- move_code：RESULT

- paraphrase_cn：状态依赖方案显著优于状态独立方案，回答RQ1。

- rhetorical_function_cn：给出第一项核心发现。

- depends_on_cn：实验数据。

- sets_up_cn：T3 vs. T4比较。

- evidence_pointer：第1节第7段，Table 4

### 17. Introduction P7

- order：17

- section：Introduction

- locator：Introduction P7

- move_code：RESULT

- paraphrase_cn：congruent方案T4总体比incongruent方案T3更能提升阅读和支付，带来7.3%年收入提升。

- rhetorical_function_cn：回答RQ2的总体层面。

- depends_on_cn：主比较。

- sets_up_cn：异质性分析。

- evidence_pointer：第1节第7段

### 18. Introduction P7

- order：18

- section：Introduction

- locator：Introduction P7

- move_code：RESULT

- paraphrase_cn：congruent并非总是最优；偏好更流动或更宽的消费者对incongruent方案更适应。

- rhetorical_function_cn：引入异质性发现。

- depends_on_cn：总体结果。

- sets_up_cn：个性化推荐建议。

- evidence_pointer：第1节第7段

### 19. Introduction P7

- order：19

- section：Introduction

- locator：Introduction P7

- move_code：STUDY_OVERVIEW

- paraphrase_cn：作者还进行了在线调查，以更好理解潜在机制。

- rhetorical_function_cn：预告机制证据。

- depends_on_cn：异质性。

- sets_up_cn：第4.6节。

- evidence_pointer：第1节第7段

### 20. Introduction P7

- order：20

- section：Introduction

- locator：Introduction P7

- move_code：RESULT

- paraphrase_cn：状态依赖方案还对非推荐内容产生正向需求溢出，且品类内和品类间都有。

- rhetorical_function_cn：扩展价值主张。

- depends_on_cn：主效应。

- sets_up_cn：溢出分析。

- evidence_pointer：第1节第7段，Table 6

### 21. Introduction P8

- order：21

- section：Introduction

- locator：Introduction P8

- move_code：CONTRIBUTION

- paraphrase_cn：总结贡献：把短暂性纳入推荐系统，展示策略-状态配对和精细个性化价值，强调整体需求视角。

- rhetorical_function_cn：在引言末尾浓缩贡献。

- depends_on_cn：全部发现。

- sets_up_cn：正文展开。

- evidence_pointer：第1节第8段

### 22. Introduction P9

- order：22

- section：Introduction

- locator：Introduction P9

- move_code：STUDY_OVERVIEW

- paraphrase_cn：预告剩余章节：理论背景、实验设计、模型与发现、结论。

- rhetorical_function_cn：提供全文路标。

- depends_on_cn：文章结构。

- sets_up_cn：读者预期。

- evidence_pointer：第1节第9段

### 23. Section 2.1 opening

- order：23

- section：Theoretical Background

- locator：Section 2.1 opening

- move_code：THEORY_INTRO

- paraphrase_cn：消费可分为液体消费和固体消费，数字内容属于液体消费，突出短暂性。

- rhetorical_function_cn：为框架提供消费理论根基。

- depends_on_cn：引言中的短暂性。

- sets_up_cn：为何推荐系统需要状态依赖。

- evidence_pointer：第2.1节首段

### 24. Section 2.1 after liquid discussion

- order：24

- section：Theoretical Background

- locator：Section 2.1 after liquid discussion

- move_code：THEORY_PROPOSITION

- paraphrase_cn：瞬时偏好与长期持久偏好不同，受即时目标和情境因素影响。

- rhetorical_function_cn：区分偏好类型。

- depends_on_cn：液体消费理论。

- sets_up_cn：ephemeral preference的测量。

- evidence_pointer：第2.1节第2段

### 25. Section 2.1 foraging/fixation paragraph

- order：25

- section：Theoretical Background

- locator：Section 2.1 foraging/fixation paragraph

- move_code：THEORY_PROPOSITION

- paraphrase_cn：用foraging和fixation刻画当下短暂状态：fixation是聚焦重复，foraging是跨类别寻求变异。

- rhetorical_function_cn：定义核心短暂状态。

- depends_on_cn：短暂状态概念。

- sets_up_cn：操作性定义。

- evidence_pointer：第2.1节第3段

### 26. Section 2.1 final paragraph

- order：26

- section：Theoretical Background

- locator：Section 2.1 final paragraph

- move_code：REQUIREMENT

- paraphrase_cn：推荐系统应整合和平衡一致性与多样性的双需求，适应消费者动态短暂状态。

- rhetorical_function_cn：从理论推导设计要求。

- depends_on_cn：双需求与状态。

- sets_up_cn：T3/T4设计。

- evidence_pointer：第2.1节第4段

### 27. Section 2.1 summary

- order：27

- section：Theoretical Background

- locator：Section 2.1 summary

- move_code：TRANSITION

- paraphrase_cn：总结：本研究把液体消费的短暂性纳入推荐系统，是早期探讨策略-状态交互的努力。

- rhetorical_function_cn：小结并定位贡献。

- depends_on_cn：前述理论。

- sets_up_cn：下一小节。

- evidence_pointer：第2.1节第5段

### 28. Section 2.2 opening

- order：28

- section：Theoretical Background

- locator：Section 2.2 opening

- move_code：THEORY_INTRO

- paraphrase_cn：引用congruence theory定义组件一致性，强调对齐的有效性。

- rhetorical_function_cn：引入一致性理论。

- depends_on_cn：需要解释策略-状态配对。

- sets_up_cn：T4/T3比较的理论依据。

- evidence_pointer：第2.2节首段

### 29. Section 2.2 mixed findings paragraph

- order：29

- section：Theoretical Background

- locator：Section 2.2 mixed findings paragraph

- move_code：LIMITATION

- paraphrase_cn：文献对congruence和incongruence孰优孰劣存在正反两类证据。

- rhetorical_function_cn：展示理论未决状态。

- depends_on_cn：一致性理论。

- sets_up_cn：需要实证。

- evidence_pointer：第2.2节第2段

### 30. Section 2.2 schema/isolation paragraph

- order：30

- section：Theoretical Background

- locator：Section 2.2 schema/isolation paragraph

- move_code：MECHANISM

- paraphrase_cn：Schema effect偏向一致信息，Isolation effect偏向惊喜变化，两种相反力量影响消费者反应。

- rhetorical_function_cn：解释为什么有人偏好congruent、有人偏好incongruent。

- depends_on_cn：混合文献。

- sets_up_cn：异质性和调查。

- evidence_pointer：第2.2节第3段

### 31. Section 2.2 summary

- order：31

- section：Theoretical Background

- locator：Section 2.2 summary

- move_code：GAP

- paraphrase_cn：strategy-state congruence是新类型的一致性，本研究是初步探索。

- rhetorical_function_cn：定位新缺口。

- depends_on_cn：理论矛盾。

- sets_up_cn：实验意义。

- evidence_pointer：第2.2节末段

### 32. Section 2.3 first paragraph

- order：32

- section：Theoretical Background

- locator：Section 2.3 first paragraph

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：已有推荐系统研究主要在实体消费和电商中，强调用enduring preference做同化推荐。

- rhetorical_function_cn：总结现状。

- depends_on_cn：需要与文献对话。

- sets_up_cn：指出assimilation局限。

- evidence_pointer：第2.3节首段

### 33. Section 2.3 diversification algorithms paragraph

- order：33

- section：Theoretical Background

- locator：Section 2.3 diversification algorithms paragraph

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：后续算法引入多样性、意外性等目标，解决同化造成的选择窄化。

- rhetorical_function_cn：说明已有补救。

- depends_on_cn：同化局限。

- sets_up_cn：指出单一策略局限。

- evidence_pointer：第2.3节第2-3段

### 34. Section 2.3 our framework paragraph

- order：34

- section：Theoretical Background

- locator：Section 2.3 our framework paragraph

- move_code：DESIGN_FEATURE

- paraphrase_cn：本研究提出一般化状态依赖框架，可自适应部署同化或多样算法，不限制具体算法。

- rhetorical_function_cn：区分本研究与纯算法创新文献。

- depends_on_cn：文献综述。

- sets_up_cn：实验采用简单算法。

- evidence_pointer：第2.3节第4段

### 35. Section 2.3 spillover paragraph

- order：35

- section：Theoretical Background

- locator：Section 2.3 spillover paragraph

- move_code：GAP

- paraphrase_cn：现有溢出文献主要关注同化策略的类似或互补产品，未处理状态依赖推荐对品类内/跨品类溢出的影响。

- rhetorical_function_cn：开辟第二个缺口。

- depends_on_cn：推荐系统综述。

- sets_up_cn：溢出分析。

- evidence_pointer：第2.3节末段

### 36. Section 3 intro

- order：36

- section：Experimental Design

- locator：Section 3 intro

- move_code：CONTEXT

- paraphrase_cn：合作平台为年收入2.7亿美元的电子书平台，月活1.4亿，书按20种genre分类。

- rhetorical_function_cn：提供实证背景。

- depends_on_cn：研究问题。

- sets_up_cn：测量与实验细节。

- evidence_pointer：第3节首段

### 37. Section 3.1

- order：37

- section：Experimental Design

- locator：Section 3.1

- move_code：DESIGN_FEATURE

- paraphrase_cn：ephemeral preference用滚动7天阅读衡量，enduring preference用3个月阅读衡量，依据平台建议并经过预检验。

- rhetorical_function_cn：定义核心自变量测量。

- depends_on_cn：构念定义。

- sets_up_cn：ephemeral state测量。

- evidence_pointer：第3.1节第1段

### 38. Section 3.1

- order：38

- section：Experimental Design

- locator：Section 3.1

- move_code：DESIGN_FEATURE

- paraphrase_cn：ephemeral state用二元指标：7天内读一种genre为fixation，读两种及以上为foraging。

- rhetorical_function_cn：操作化状态。

- depends_on_cn：ephemeral preference。

- sets_up_cn：实验分组。

- evidence_pointer：第3.1节第2段

### 39. Section 3.2

- order：39

- section：Experimental Design

- locator：Section 3.2

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：设置C1/C2（enduring-based）、T1/T2（ephemeral-based但状态独立）、T3/T4（状态依赖）共六组。

- rhetorical_function_cn：建立完整对比链。

- depends_on_cn：操作化。

- sets_up_cn：主分析。

- evidence_pointer：第3.2节，Tables 1-2

### 40. Section 3.2 algorithm justification

- order：40

- section：Experimental Design

- locator：Section 3.2 algorithm justification

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：故意采用简单规则算法，理由是干净识别、便于测试不同配对、符合文献起点。

- rhetorical_function_cn：辩护算法选择。

- depends_on_cn：对比架构。

- sets_up_cn：结果可归因于方案而非算法。

- evidence_pointer：第3.2节第2段

### 41. Section 3.2 design advantage paragraph

- order：41

- section：Experimental Design

- locator：Section 3.2 design advantage paragraph

- move_code：DESIGN_FEATURE

- paraphrase_cn：设计把动态ephemeral state集成到推荐中，实时选择同化或多样策略，并检验T3/T4价值。

- rhetorical_function_cn：说明设计优势。

- depends_on_cn：简单算法。

- sets_up_cn：研究结论的解释边界。

- evidence_pointer：第3.2节第3段

### 42. Section 3.2 sample paragraph

- order：42

- section：Experimental Design

- locator：Section 3.2 sample paragraph

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：实验在108,158名一周内有阅读的用户中进行，连续5天每天推荐，观测12天。

- rhetorical_function_cn：说明样本与时间窗。

- depends_on_cn：平台合作。

- sets_up_cn：回归模型。

- evidence_pointer：第3.2节第4段

### 43. Section 4.1 randomization check

- order：43

- section：Empirical Results

- locator：Section 4.1 randomization check

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：先做随机化平衡检验，确保六组在用户特征和推荐书籍上无显著差异。

- rhetorical_function_cn：建立内部效度。

- depends_on_cn：实验设计。

- sets_up_cn：因果解释。

- evidence_pointer：第4.1节第2段

### 44. Section 4.1 model paragraph

- order：44

- section：Empirical Results

- locator：Section 4.1 model paragraph

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：对连续变量用OLS，对百分比用Fractional Logit，并控制书籍级协变量。

- rhetorical_function_cn：说明估计方法。

- depends_on_cn：数据结构。

- sets_up_cn：主结果。

- evidence_pointer：第4.1节第3段

### 45. Section 4.2

- order：45

- section：Empirical Results

- locator：Section 4.2

- move_code：RESULT

- paraphrase_cn：Wald检验显示状态依赖方案T3/T4显著提升readrate和readtime，对比状态独立方案。

- rhetorical_function_cn：回答RQ1。

- depends_on_cn：估计模型。

- sets_up_cn：T3/T4比较。

- evidence_pointer：第4.2节，Table 4

### 46. Section 4.2 T4 vs T3

- order：46

- section：Empirical Results

- locator：Section 4.2 T4 vs T3

- move_code：RESULT

- paraphrase_cn：T4显著优于T3，说明总体而言消费者对与状态一致的推荐反应更强。

- rhetorical_function_cn：回答RQ2总体层面。

- depends_on_cn：主分析。

- sets_up_cn：异质性。

- evidence_pointer：第4.2节，Wald检验p(T3=T4)

### 47. Section 4.3 opening

- order：47

- section：Empirical Results

- locator：Section 4.3 opening

- move_code：TRANSITION

- paraphrase_cn：进一步探索T3/T4的异质性处理效应，以T3为基准，指导个性化并解释一致性文献的混合发现。

- rhetorical_function_cn：连接主结果与后续分析。

- depends_on_cn：总体结果。

- sets_up_cn：三个用户特质。

- evidence_pointer：第4.3节首段

### 48. Section 4.3.1

- order：48

- section：Empirical Results

- locator：Section 4.3.1

- move_code：RESULT

- paraphrase_cn：偏好稳定性较低的用户对T3反应更好，稳定性高的用户对T4更好。

- rhetorical_function_cn：展示第一个异质性。

- depends_on_cn：交互模型。

- sets_up_cn：个性化建议。

- evidence_pointer：第4.3.1节，Table 5

### 49. Section 4.3.2

- order：49

- section：Empirical Results

- locator：Section 4.3.2

- move_code：RESULT

- paraphrase_cn：偏好广度更宽的用户对T3反应更好，说明T4并非总是最优。

- rhetorical_function_cn：展示第二个异质性。

- depends_on_cn：偏好测量。

- sets_up_cn：强调异质性。

- evidence_pointer：第4.3.2节，Table 5

### 50. Section 4.3.3

- order：50

- section：Empirical Results

- locator：Section 4.3.3

- move_code：RESULT

- paraphrase_cn：参与度更高的用户更偏好T3，可能因为高参与用户更易被意外内容吸引。

- rhetorical_function_cn：展示第三个异质性并给机制线索。

- depends_on_cn：参与度测量。

- sets_up_cn：机制调查。

- evidence_pointer：第4.3.3节，Table 5

### 51. Section 4.4.1

- order：51

- section：Empirical Results

- locator：Section 4.4.1

- move_code：RESULT

- paraphrase_cn：支付结果与阅读结果一致，状态依赖方案带来更高支付。

- rhetorical_function_cn：把效果扩展到货币化。

- depends_on_cn：主阅读结果。

- sets_up_cn：收入外推。

- evidence_pointer：第4.4.1节，Online Appendix C Table C1

### 52. Section 4.4.2

- order：52

- section：Empirical Results

- locator：Section 4.4.2

- move_code：RESULT

- paraphrase_cn：信封式外推显示T4可为平台年收入带来约1973万美元提升。

- rhetorical_function_cn：量化经济效益。

- depends_on_cn：支付回归。

- sets_up_cn：管理启示。

- evidence_pointer：第4.4.2节

### 53. Section 4.4.3

- order：53

- section：Empirical Results

- locator：Section 4.4.3

- move_code：RESULT

- paraphrase_cn：状态依赖方案对非推荐内容产生整体正向溢出；T3主要跨品类，T4同时提升品类内和跨品类。

- rhetorical_function_cn：扩展价值评估边界。

- depends_on_cn：主方案效果。

- sets_up_cn：贡献中的溢出主张。

- evidence_pointer：第4.4.3节，Table 6

### 54. Section 4.5 intro

- order：54

- section：Empirical Results

- locator：Section 4.5 intro

- move_code：STUDY_OVERVIEW

- paraphrase_cn：执行一系列稳健性检验，包括时间窗、模型、genre测量、状态操作化、识别、季节性。

- rhetorical_function_cn：预告稳健性。

- depends_on_cn：主结果。

- sets_up_cn：每项检验。

- evidence_pointer：第4.5节首段

### 55. Section 4.5.3

- order：55

- section：Empirical Results

- locator：Section 4.5.3

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：通过内容embedding验证同genre书籍内容距离显著小于跨genre，支持genre作为偏好测量。

- rhetorical_function_cn：强化构念效度。

- depends_on_cn：genre操作化。

- sets_up_cn：状态测量可信度。

- evidence_pointer：第4.5.3节

### 56. Section 4.5.4

- order：56

- section：Empirical Results

- locator：Section 4.5.4

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：用连续内容相似度构造ephemeral state并在现有样本中模拟，结果一致。

- rhetorical_function_cn：显示状态测量不依赖简单二分。

- depends_on_cn：主结果。

- sets_up_cn：外部效度。

- evidence_pointer：第4.5.4节，Table D4

### 57. Section 4.6 opening

- order：57

- section：Empirical Results

- locator：Section 4.6 opening

- move_code：STUDY_OVERVIEW

- paraphrase_cn：补充在线调查，从Schema/Isolation视角提供机制初探。

- rhetorical_function_cn：预告机制证据。

- depends_on_cn：异质性结果。

- sets_up_cn：调查结果。

- evidence_pointer：第4.6节首段

### 58. Section 4.6 closing

- order：58

- section：Empirical Results

- locator：Section 4.6 closing

- move_code：RESULT

- paraphrase_cn：偏好congruent方案的用户Schema效应更强，偏好incongruent方案的用户Isolation效应更强。

- rhetorical_function_cn：提供机制支持的探索性证据。

- depends_on_cn：调查数据。

- sets_up_cn：结论机制解释。

- evidence_pointer：第4.6节末段

### 59. Section 5.1

- order：59

- section：Conclusion

- locator：Section 5.1

- move_code：CONTRIBUTION

- paraphrase_cn：总结：状态依赖和策略-状态配对能提升阅读与支付，但存在消费者异质性，并对非推荐内容有正向溢出。

- rhetorical_function_cn：回顾核心发现。

- depends_on_cn：全部分析。

- sets_up_cn：理论贡献。

- evidence_pointer：第5.1节

### 60. Section 5.2

- order：60

- section：Conclusion

- locator：Section 5.2

- move_code：CONTRIBUTION

- paraphrase_cn：理论贡献包括：将短暂性纳入推荐系统、扩展congruence文献的新类型一致性、扩展spillover文献。

- rhetorical_function_cn：将结果提升为一般知识。

- depends_on_cn：发现。

- sets_up_cn：管理启示。

- evidence_pointer：第5.2节

### 61. Section 5.3

- order：61

- section：Conclusion

- locator：Section 5.3

- move_code：CONTRIBUTION

- paraphrase_cn：管理启示：用自适应状态依赖方案提升参与和利润，按偏好稳定性/广度/参与度个性化，并考虑溢出价值。

- rhetorical_function_cn：提供实践建议。

- depends_on_cn：贡献主张。

- sets_up_cn：边界条件。

- evidence_pointer：第5.3节

### 62. Section 5.3 generalizability

- order：62

- section：Conclusion

- locator：Section 5.3 generalizability

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：框架不限制算法，可推广到视频/音频等平台，但需按内容消费周期调整ephemeral state时间窗。

- rhetorical_function_cn：界定适用范围。

- depends_on_cn：研究设计。

- sets_up_cn：未来研究。

- evidence_pointer：第5.3节末段

### 63. Section 5.4

- order：63

- section：Conclusion

- locator：Section 5.4

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：限制包括简单算法、聚合效应、genre测量、active users，并提出未来方向。

- rhetorical_function_cn：诚实划界并激励后续研究。

- depends_on_cn：全部研究。

- sets_up_cn：读者对贡献边界的理解。

- evidence_pointer：第5.4节

## 写作技术

- gap_construction_cn：先用市场体量说明重要性，再用“数字内容消费的短暂性被推荐系统忽略”建立第一个缺口；接着指出已有推荐系统只做assimilation或diversification的一端而忽略两者与瞬时状态的交互；最后用congruence文献的混合证据制造需要实证裁决的开放问题。

- signposting_cn：摘要预告框架与主要发现；引言末尾给出全文结构；理论部分每小节用“总之/因此”把理论回扣到设计；实验部分用Research Question 1/2标记；稳健性小节目录化；结论分理论贡献、管理含义、局限。

- transition_logic_cn：从理论到设计：“因此我们提出/采用……”；从主结果到异质性：“进一步探索……”；从阅读到支付/溢出：“经济影响与整体价值”；从结果到机制：“为理解机制，进行在线调查”。

- claim_evidence_rhythm_cn：先给出回归表，再解释系数，用Wald检验做两两比较，最后用p值强调显著性；异质性分析中每个特质按“测量—发现—解释”三步循环；每次结果后都回到对应RQ或文献。

- benchmark_narrative_cn：C1/C2作为平台现状与enduring偏好基准，T1/T2剥离ephemeral preference影响，T3/T4作为核心对比；由此可逐步归因：enduring→ephemeral偏好改善，状态独立→状态依赖改善，T3 vs T4回答策略-状态配对方向。

- theory_return_cn：在讨论中反复把T4优于T3解释为strategy-state congruence，把异质性解释为Schema/Isolation张力，把T3对流动偏好更优解释为choice literature中的偏好异质性，从而把局部统计结果升维为理论贡献。

- contribution_positioning_cn：将贡献分层：理论框架进推荐系统文献、新型一致性进congruence文献、溢出进spillover文献；在结论中明确使用“首次”“扩展”“丰富”等定位语。

- novelty_protection_cn：强调框架不依赖特定算法，用简单算法只是识别策略；把结果从“具体算法更好”提升为“策略-状态配对更好”；用溢出效应证明只看推荐内容会低估方案价值；用异质性防止“one-size-fits-all”的过度简化。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：建立背景：说明产品市场规模、推荐系统重要性、所研究内容类别的独特挑战。

- research_job_cn：找到实践或理论现象（如数字内容短暂性）并把它与推荐系统缺口挂钩。

- required_evidence_cn：至少需要行业数据或文献支持该现象存在且未被解决。

- transition_to_next_cn：从一般现象到“已有系统忽略某构念”。

#### 2. 2

- step：2

- writing_job_cn：把现象拆成可操作构念，界定瞬时偏好、短暂状态、foraging/fixation等概念。

- research_job_cn：确定构念测量方式，并做小样本预验证或领域专家确认。

- required_evidence_cn：文献定义、平台管理者的领域知识、初步数据验证。

- transition_to_next_cn：从概念到“为推荐系统设计提出理论方案”。

#### 3. 3

- step：3

- writing_job_cn：用理论推导设计方案，说明congruent和incongruent两种策略-状态配对。

- research_job_cn：从理论命题得到可检验的对比设计。

- required_evidence_cn：理论命题与设计元素之间的清晰映射。

- transition_to_next_cn：从理论方案到“需要随机实验裁决”。

#### 4. 4

- step：4

- writing_job_cn：描述随机田野实验：样本、随机化、对照组/处理组、测量、观察窗口。

- research_job_cn：与真实平台合作执行实验，确保随机化和平台规则不污染。

- required_evidence_cn：随机化平衡检验、样本量、处理定义。

- transition_to_next_cn：从实验设计到“主效应回归”。

#### 5. 5

- step：5

- writing_job_cn：报告主效应，随后做异质性分析，分别说明对谁更有效。

- research_job_cn：用Wald检验方案间比较，用交互项检验用户特质。

- required_evidence_cn：主效应显著，异质性交互显著。

- transition_to_next_cn：从异质性到“为什么会这样”的机制探索。

#### 6. 6

- step：6

- writing_job_cn：扩展至支付、收入外推、需求溢出和在线调查机制。

- research_job_cn：用支付模型、外推计算、Negative Binomial溢出回归、调查问卷。

- required_evidence_cn：经济指标显著或至少探索性支持。

- transition_to_next_cn：从经济价值到“贡献总结”。

#### 7. 7

- step：7

- writing_job_cn：做稳健性检验，总结理论贡献、管理启示、边界和未来研究。

- research_job_cn：用替代模型、时间窗、测量方式、样本子集再检验。

- required_evidence_cn：稳健性结果一致。

- transition_to_next_cn：回到引言缺口，闭合论证。

### most_transferable_moves_cn

1. 用理论构造可检验的“配对”方案而非直接造算法

2. 把现有文献的两种对立策略统一进一个自适应框架

3. 设置多级基准（enduring/ephemeral/state-independent）以逐层归因

4. 在主效应后引入异质性以解释文献中不一致结论

5. 用溢出效应把评价从局部推荐结果扩展到平台级收益

6. 用简单算法作为刻意识别策略并明确说明理由

### resource_intensive_or_nonstandard_parts_cn

1. 需要真实平台长期用户数据和推荐位

2. 需要与平台管理者的领域知识协作确定时间窗

3. 10.8万用户的大规模随机实验成本高

4. 重复推荐和12天观测周期要求平台改动接口

5. 在线调查需要额外样本和问卷工具

### what_not_to_copy_superficially_cn

1. 如果没有理论到设计的映射，仅加几个“状态依赖”标签并不能构成贡献

2. 如果没有多级对照，只报告T3/T4差异无法说明状态依赖优于状态独立

3. 如果只用简单回归而不用Wald检验/交互，就无法支撑“总体vs异质性”的双重主张

4. 收入外推需明确假设；不能把外推当成实测利润

5. 在线调查机制不能替代实验中的中介检验；若照搬为机制结论会过度声称

- single_best_description_of_the_routine_cn：用消费理论定义短期状态，把推荐策略与状态配对成理论方案并在真实平台随机分配，再通过分层比较、异质性、支付溢出与调查逐步把结果升维为设计知识与理论贡献。

## 分析边界

本文基于正文全文进行分析，但Online Appendix A-F及多个附录表格（如B/C/D/E）未提供，部分稳健性检验、调查题项和预验证细节只能依赖正文转述；文章无页码，locator按段节标注；由于缺少附录细节，对附件内结果的核验有限。
