# Using Digital Nudges to Enhance Collective Intelligence in Online Collaboration: Insights from Unexpected Outcomes

- 作者：Pranav Gupta; Young Ji Kim; Ella Glikson; Anita Williams Woolley
- 年份 / 期刊：2024 / MIS Quarterly
- DOI：10.25300/misq/2023/16752
- 源文件：00616_2024_using-digital-nudges-to-enhance-collective-intelligence-in-online-collaboration-insights-from-un.md
- 论文主类型：theory_derived_artifact_experiment
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.88

## 文章级论证概况

- 核心问题：数字助推能否以及如何通过改变临时在线小组中的协作过程（技能使用、任务策略、集体努力）来提升集体智慧，并在何种条件下可能失效或产生逆向效果。

- 制品与设计：四种数字助推：Skill Facilitator Bot、Strategy Facilitator Bot、ToDo List、Feedback Display。前两者为聊天机器人，分别提示成员讨论技能和任务协调；ToDo List为工作区中的任务管理小组件；Feedback Display为实时显示各成员相对参与度的动态仪表。四者分别基于“构建复杂选择”“设置默认”“即时反馈”等助推原则，嵌入Test of Collective Intelligence平台界面。

- 客观结果：Skill Facilitator Bot显著提高技能使用，并通过技能使用产生正向间接效应；Strategy Facilitator Bot对任务策略无显著效应；ToDo List显著削弱任务策略并产生负向间接效应，但总直接效应为正；Feedback Display显著降低总努力水平并产生负向间接效应。三个协作过程本身均显著正向预测集体智慧。

- 核心贡献：证明轻量数字助推可以影响在线临时团队的协作过程并改变集体智慧，但并非所有助推都有效，部分设计会产生与预期相反的结果。作者通过结构化推测系统讨论情境、剂量和人群条件，提出集体导向、协同性助推更可能成功，并强调设计者必须评估数字工具对协作过程的心理和社会影响。

- 整篇论证链：作者从临时在线小组快速普及但协作困难切入，指出这类团队缺乏传统组织中的角色和规范塑造机制，而个体决策领域的助推可能提供一种不剥夺自主性的技术干预方式。基于小群体绩效与集体智慧研究，作者锁定技能使用、任务策略和集体努力三个关键协作过程，并从助推理论中选择最匹配的界面设计原则，构建四个数字助推嵌入TCI平台。通过168个临时匿名在线小组的随机实验，作者以客观行为指标和TCI得分为依据，检验各助推对目标过程及集体智慧的独立与间接效应。结果仅部分符合预期，一个助推有效，一个无效，两个反而产生负向效应。作者随后用行为日志、用户评论和分阶段比较解释这些意外结果，再以结构化推测将结果转化为关于集体目标、剂量反应和人群特征的设计知识，最终将贡献定位为对助推理论在群体层面的扩展和对未来自适应助推系统的启示。

## 类型与写作弧线判定

- 论文主类型判定：论文从既有理论（小群体过程理论、集体智慧研究、团队干预研究、助推理论）推导出四个数字助推干预靶点和设计原则，再通过随机实验检验这些理论推导的制品对客观协作过程与集体智慧的影响，符合“理论推导制品差异并通过实验检验”的类型。不是典型的构建-评价设计科学研究，也不是真实平台上的现场实验。

- 主导写作弧线判定：写作弧线从现实问题出发，进入理论背景构建研究问题，随后描述数字助推的设计与实验检验，再处理意外结果，最后回到理论并界定边界条件，形成“问题—理论—设计—检验—回到理论”的闭环。

## 研究开展程序

- study_or_phase_count：7

- 研究阶段总序列：研究从理论映射开始，经过工程开发和pilot测试，进入正式随机实验，再进行操纵检查和主分析；主分析发现三种意外结果后，转入探索性行为与评论分析，最后通过结构化推测将局部实验证据扩展为设计原则和未来研究条件。各阶段不是独立多项研究，而是同一实验项目下的累积论证链条。

### studies_or_phases

#### 1. 理论映射与助推概念设计

- order：1

- name_cn：理论映射与助推概念设计

- question_cn：哪些协作过程是影响集体智慧的关键杠杆，哪些助推原则适合启动这些过程？

- inputs_and_setting_cn：小群体绩效研究、集体智慧研究、团队干预研究、助推与选择架构文献。

- designed_or_compared_object_cn：四个数字助推的概念设计：两个facilitator bot、ToDo List、Feedback Display。

- baseline_control_or_counterfactual_cn：无；属于设计前准备阶段。

##### objective_metrics

1. 概念-过程对应度

2. 助推原则与目标过程的匹配度

- analysis_method_cn：文献综述、概念映射、理论推导。

- main_result_cn：确定技能使用、任务策略、集体努力三个协作过程为目标；选择structure complex choices、set defaults、provide immediate feedback作为设计原则。

- argumentative_role_cn：为后续所有设计选择和实验假设提供理论基础。

- remaining_uncertainty_cn：概念设计是否能在数字界面中实现并被目标人群感知和理解尚不清楚。

- link_to_next_phase_cn：概念设计需要工程实现和预测试，进入下一阶段。

##### evidence_pointers

1. Theoretical Background小节

2. Methods Digital Nudge Treatments Table 1

#### 2. 工程测试与pilot验证

- order：2

- name_cn：工程测试与pilot验证

- question_cn：每个助推装置在POGS界面中是否功能正常，参与者能否理解和使用？

- inputs_and_setting_cn：POGS平台、四个助推原型、4-5组naive pilot测试参与者。

- designed_or_compared_object_cn：四个助推的界面实现和交互流程。

- baseline_control_or_counterfactual_cn：功能预期和设计规格。

##### objective_metrics

1. 技术bug数量

2. 参与者对助推的理解程度

3. pilot组完成任务时的可操作性

- analysis_method_cn：多轮工程调试、pilot观察和反馈。

- main_result_cn：四个助推在正式实验前均通过工程测试，pilot组表明参与者能理解和使用。

- argumentative_role_cn：通过预先打磨装置保证操纵有效性，强化实验内部效度。

- remaining_uncertainty_cn：pilot规模小，无法得知完整实验环境中的效果。

- link_to_next_phase_cn：设备就绪后进入正式随机实验。

##### evidence_pointers

1. Methods Digital Nudge Treatments最后一段

#### 3. 正式随机实验

- order：3

- name_cn：正式随机实验

- question_cn：四种数字助推相比控制条件是否影响三个协作过程和集体智慧？

- inputs_and_setting_cn：515名Amazon Mechanical Turk参与者随机组成168个三人或四人小组，通过POGS平台同步完成25分钟TCI任务电池。

- designed_or_compared_object_cn：四个助推处理条件（Skill Bot n=29；Strategy Bot n=33；ToDo List n=33；Feedback Display n=36）和“无助推”控制条件（n=37）。

- baseline_control_or_counterfactual_cn：无助推控制组；三种协作过程和CI作为客观结果。

##### objective_metrics

1. TCI collective intelligence得分

2. 按键次数作为集体努力水平

3. 任务完成比例作为任务策略质量

4. 任务维度技能-努力相关作为技能使用程度

- analysis_method_cn：随机分配实验、平台化同步数据采集。

- main_result_cn：成功采集到各组在四个处理条件上的过程与CI数据。

- argumentative_role_cn：整个研究的证据核心来源，提供因果检验所需数据。

- remaining_uncertainty_cn：需要确认参与者是否真正注意到或响应助推，才能解释后续结果。

- link_to_next_phase_cn：数据收集后进行操纵检查，再进入主分析。

##### evidence_pointers

1. Methods Participants

2. Methods Tasks and Procedure

#### 4. 操纵检查

- order：4

- name_cn：操纵检查

- question_cn：参与者是否达到最低限度的注意或响应门槛？

- inputs_and_setting_cn：事后问卷、ToDo List交互日志、facilitator bot条件下的聊天量。

- designed_or_compared_object_cn：各处理条件中的注意率和响应行为。

- baseline_control_or_counterfactual_cn：控制组的聊天量；ToDo List未使用的少数组。

##### objective_metrics

1. 报告注意到该nudge的参与者比例

2. ToDo List至少被使用一次的团队数

3. facilitator bot条件与控制组聊天量差异

- analysis_method_cn：描述统计、独立样本t检验、单尾检验。

- main_result_cn：ToDo List和Feedback Display分别有85.15%和87.39%参与者注意到；所有队伍至少有一名成员注意到。ToDo List中除五组外其余均使用。Skill和Strategy Bot组的聊天量显著高于控制组。

- argumentative_role_cn：证明四个助推都实现了至少最低限度的暴露，排除了“完全没注意到”的平凡解释。

- remaining_uncertainty_cn：操纵成功不等于助推会产生预期过程改变，仍需主分析检验。

- link_to_next_phase_cn：通过操纵检查后进入主分析。

##### evidence_pointers

1. Results Manipulation Check

#### 5. 多重中介主分析

- order：5

- name_cn：多重中介主分析

- question_cn：每个劝导是否通过其目标协作过程对集体智慧产生净间接效应？

- inputs_and_setting_cn：168个小组的协作过程行为指标和TCI得分。

- designed_or_compared_object_cn：四个处理哑变量vs控制组；三个协作过程作为并行中介。

- baseline_control_or_counterfactual_cn：无助推控制条件作为基线。

##### objective_metrics

1. OLS回归系数

2. bootstrap 95%置信区间的间接效应

3. 调整R²

- analysis_method_cn：PROCESS Model 4多重中介分析，pyprocessmacro，bootstrap抽样。

- main_result_cn：三个协作过程均正向预测CI。Skill Bot显著提升技能使用，间接效应显著为正；Strategy Bot无显著效应；ToDo List显著降低任务策略，间接效应显著为负；Feedback Display显著降低总努力，间接效应显著为负。

- argumentative_role_cn：正式检验理论假设，同时产生令人意外的无效和负向结果，进而推动后续探索。

- remaining_uncertainty_cn：意外结果背后的机制尚不明确。

- link_to_next_phase_cn：需要行为日志和事后评论解释为什么某些nudge失效或反向。

##### evidence_pointers

1. Results Analysis Approach

2. Results Test of Experimental Nudges

3. Table 3a

4. Table 3b

5. Figure 3

#### 6. 探索性行为与评论分析

- order：6

- name_cn：探索性行为与评论分析

- question_cn：为什么Strategy Facilitator Bot无效、ToDo List和Feedback Display反而削弱目标过程？

- inputs_and_setting_cn：按条件比较聊天量、任务阶段通信、最高与最低努力贡献者的差距、任务完成分布、开放题评论。

- designed_or_compared_object_cn：同一实验数据的细粒度行为对照和评论定性分析。

- baseline_control_or_counterfactual_cn：控制组或其余条件组合的聊天量；最高与最低努力贡献者在Feedback和Control间的比较。

##### objective_metrics

1. 最后TCI任务中聊天量对比的F值

2. 第一个任务聊天量对比

3. 高低努力贡献者差距

4. 不同阶段差距t值

- analysis_method_cn：组间比较、t检验、F检验、聊天内容查看、参与者评论的主题归纳。

- main_result_cn：Strategy Bot起初被认可但预期落空后被忽略；ToDo List让本不会协调的低绩效组提前讨论策略，但也让一些组过度规划而挤占任务执行，产生双峰效果；Feedback Display引发了极化情绪，最低贡献者贡献更少，高低差距显著扩大，被感知为公开羞辱。

- argumentative_role_cn：为三个意外结果提供机制层面的可能性解释，使结果从单纯统计效应变成可理解的行为过程。

- remaining_uncertainty_cn：这些机制是事后解释，缺乏操纵性验证，不能作为因果结论。

- link_to_next_phase_cn：探索性分析为结构化推测提供了具体素材和候选边界条件。

##### evidence_pointers

1. Results Exploring the Unexpected Results

2. Exploring Unexpected Results三个小节

#### 7. 结构化推测

- order：7

- name_cn：结构化推测

- question_cn：在Context、Scale、Population等维度上，实验结果在何种条件下可推广或改变？

- inputs_and_setting_cn：本实验证据、参与者评论、相关文献和先例（如Glikson et al. 2019）。

- designed_or_compared_object_cn：概念性对照：集体vs个体目标、剂量过低vs过高、临时匿名组vs既有组等。

- baseline_control_or_counterfactual_cn：非实证检验，而是理论条件和文献反事实。

##### objective_metrics

（空）

- analysis_method_cn：Banerjee et al. 2017提出的structured speculation框架，按情境、规模、人群三个维度系统讨论。

- main_result_cn：提出集体导向、协同性助推更可能成功；自适应剂量系统可能优于静态nudge；无既有规范、心理安全较高或声誉威胁存在的临时匿名团队中更可能观察到类似效果；个体绩效或单纯努力激励可能抵消协作收益。

- argumentative_role_cn：将局部实验证据转化为可推广的设计知识和边界条件，同时为未来研究提供可检验的假设。

- remaining_uncertainty_cn：所有推测均未被实证检验，需未来实验验证。

- link_to_next_phase_cn：作为Discussion的核心部分，连接结论中的未来研究和自适应助推展望。

##### evidence_pointers

1. Discussion: Structured Speculation

2. Table 4

3. Conclusion

## 各部分修辞架构

### abstract_moves

1. CONTEXT

2. PHENOMENON

3. PRACTICAL_STAKES

4. PRIOR_KNOWLEDGE

5. STUDY_OVERVIEW

6. RESULT

7. LIMITATION

8. CONTRIBUTION

### introduction_moves

1. CONTEXT

2. PHENOMENON

3. PRACTICAL_STAKES

4. PRIOR_KNOWLEDGE

5. RQ_OR_OBJECTIVE

6. STUDY_OVERVIEW

7. RESULT

8. CONTRIBUTION

### theory_and_knowledge_moves

1. CONTEXT

2. THEORY_INTRO

3. THEORY_PROPOSITION

4. PRIOR_KNOWLEDGE

5. LIMITATION

6. GAP

7. MECHANISM

8. TRANSITION

9. REQUIREMENT

### artifact_design_moves

1. METHOD_JUSTIFICATION

2. DESIGN_FEATURE

3. REQUIREMENT

4. BENCHMARK_OR_CONTRAST

### evaluation_moves

1. METHOD_JUSTIFICATION

2. RESULT

3. ROBUSTNESS_OR_BOUNDARY_TEST

4. MECHANISM

5. TRANSITION

### discussion_and_contribution_moves

1. RESULT

2. METHOD_JUSTIFICATION

3. BOUNDARY_CONDITION

4. CONTRIBUTION

5. LIMITATION_AND_FUTURE

## 理论/知识到设计的翻译

### 知识/理论基础

1. 小群体绩效与过程损失理论（Hackman 1987; Steiner 1972）

2. 集体智慧研究（Woolley et al. 2010; Riedl et al. 2021）

3. 团队教练与早期干预研究（Hackman & Wageman 2005; Mathieu & Rapp 2009）

4. 助推理论与选择架构（Thaler & Sunstein 2009; Thaler et al. 2010）

5. 数字助推研究（Weinmann et al. 2016; Mirsch et al. 2017）

6. 群组支持系统（GSS）与计算机中介协作研究

- 理论—设计耦合：partial

- 耦合判定理由：理论确实决定了助推的目标协作过程和设计原则：作者从小群体过程和CI研究选定三个过程，并从助推理论中选用三个原则。但具体制品形式（聊天机器人、ToDo小组件、动态仪表）更多来自界面工程判断和对原则的直观映射，而不是严格的从理论演绎到唯一设计；作者也承认选择的是“看起来最合适”的原则，且理论未能预测两个负向结果。因此属于部分耦合。

- 理论到设计翻译链：小群体过程理论确定三项核心协作过程 → CI研究证明这些过程驱动集体智慧 → 团队干预研究提示早期干预有效 → 助推理论说明如何不通过强制影响选择 → 数字助推研究提供界面设计原则 → 将structure complex choices映射到技能/策略bot、set defaults映射到ToDo List、provide immediate feedback映射到Feedback Display → 将设计嵌入TCI界面 → 通过实验比较目标过程与CI相对控制组的变化。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：技能使用是CI的重要驱动因素，而复杂选择需要被结构化以调用成员知识与技能。

- mechanism_cn：通过提示成员公开讨论自身技能，提升团队对可用专长的认识，强化共享认知和分工质量。

- design_requirement_cn：在任务开始阶段以轻量方式发起关于成员技能的讨论。

- artifact_choice_cn：Skill Facilitator Bot，在聊天窗口自动提问“谁擅长什么”等技能相关问题。

- evaluated_contrast_cn：Skill Bot条件vs控制条件在技能使用和CI上的差异，以技能使用为中介。

- objective_result_cn：Skill Bot显著正向影响技能使用，并通过技能使用产生正向间接效应（b=0.044，95%CI 0.002, 0.132）。

##### evidence_pointers

1. Table 3a Model 3

2. Table 3b Model 3

3. Figure 3

#### 2. 2

- theory_or_knowledge_claim_cn：任务策略协调是CI的关键过程，而复杂任务需要结构化协调选择。

- mechanism_cn：通过提示成员在任务开始和中期讨论分工、方案和调整，减少协调遗漏。

- design_requirement_cn：在每项任务开始时提示协商分工，并在中期促发过程回顾。

- artifact_choice_cn：Strategy Facilitator Bot，在聊天窗口发布“谁做什么”以及是否需要调整策略的问题。

- evaluated_contrast_cn：Strategy Bot条件vs控制条件在任务策略和CI上的差异。

- objective_result_cn：Strategy Bot对任务策略无显著效应，间接效应不显著。

##### evidence_pointers

1. Table 3a Model 2

2. Table 3b Model 2

3. Figure 3

#### 3. 3

- theory_or_knowledge_claim_cn：默认设置可诱发惯性并促使协作任务分配被显性化；缺少讨论时团队很少主动协调，因此把协调选项做成默认可见应能提升策略。

- mechanism_cn：默认呈现任务列表，引导成员早期讨论任务分配、识别缺口并追踪进度，从而提高协调。

- design_requirement_cn：在工作区提供一个默认可见且可交互的任务分配工具。

- artifact_choice_cn：ToDo List小组件，常驻工作区顶端，支持勾选完成状态和更新进度。

- evaluated_contrast_cn：ToDo List条件vs控制条件在任务策略和CI上的差异。

- objective_result_cn：ToDo List显著降低任务策略，通过任务策略的间接效应显著为负；但总直接效应为正。

##### evidence_pointers

1. Table 3a Model 2

2. Table 3b Model 2

3. Exploring ToDo List

#### 4. 4

- theory_or_knowledge_claim_cn：提供即时反馈可通过社会规范知觉减少免费搭车，使成员提高集体努力。

- mechanism_cn：实时显示每个成员的相对活动水平，唤起公平规范和比较动机，促使低贡献者增加努力。

- design_requirement_cn：在协作过程中实时呈现成员相对努力的信息。

- artifact_choice_cn：Feedback Display，界面顶部的动态显示，按活动量展示个人相对贡献水平。

- evaluated_contrast_cn：Feedback Display条件vs控制条件在集体努力水平和CI上的差异。

- objective_result_cn：Feedback Display显著降低总努力，通过努力水平的间接效应显著为负；最低贡献者贡献更少。

##### evidence_pointers

1. Table 3a Model 1

2. Table 3b Model 1

3. Exploring Feedback Display

## 评价逻辑

### evaluation_modes

1. 随机对照实验

2. 操纵检查

3. 基于客观行为数据的多重中介效应分析

4. 事后探索性行为与评论分析

5. 结构化推测

- why_these_evaluations_cn：需要首先证明助推确实被参与者注意（操纵检查），然后检验每个助推是否改变其目标协作过程并进而影响CI（多重中介）；主分析中的意外结果需要用行为日志和评论提供机制线索（探索性分析）；最后用结构化推测把局部实验证据放到更广情境中讨论外部效度。

- benchmark_and_contrast_chain_cn：所有助推均以无助推控制组为参照；三种协作过程作为并行中介，同时检验每个助推对CI的间接路径；事后分析进一步对比聊天量、努力差距和阶段变化，建立次级行为基准；结构化推测则用相关文献和Glikson et al. 2019的真实团队反馈干预作为外部对照，推理边界条件。

### claim_evidence_ledger

1. Skill Facilitator Bot通过技能使用提升CI——证据：Table 3b Model 3 bootstrap CI为0.002-0.132，且技能使用系数显著。

2. Strategy Facilitator Bot无效——证据：Table 3a Model 2无显著系数，Table 3b Model 2 CI包含0。

3. ToDo List通过任务策略产生负向间接效应——证据：Table 3a Model 2系数显著为负，Table 3b Model 2 CI为-0.540至-0.052。

4. ToDo List提高整体CI（直接效应）——证据：Table 3b Model 4 CI为0.074至0.589；探索性行为数据表明低绩效组被托底。

5. Feedback Display通过降低努力产生负向间接效应——证据：Table 3a Model 1系数显著为负，Table 3b Model 1 CI为-0.326至-0.019。

6. Feedback Display使最低贡献者进一步退却——证据：最低贡献者贡献显著少于控制组（t=3.14，p=0.005），高低努力差距增大。

7. 结构化推测中的设计原则——未直接检验，属于事后理论归纳和未来假设。

- internal_validity_strategy_cn：随机分配参与者与小组到条件，使用无绩效奖金控制激励混淆；统一平台和TCI任务电池保证刺激标准化；多轮工程测试和pilot确保助推可用；操纵检查确认曝光；回归模型控制组大小、社会知觉、沟通量和沟通方差。

- external_validity_strategy_cn：使用TCI这样经过跨22个数据集、超过1300组验证的标准化任务电池，使结果不局限于单一任务；使用临时匿名陌生人团队作为基准范围；结构化推测系统讨论Context、Scale和Population，并与真实学生团队中的类似反馈干预对比以推断更广适用性。

- what_is_not_actually_tested_cn：自适应或智能助推系统未被测试；既有团队、熟悉成员、心理安全调节、绩效激励、声誉激励、参与者长期重复互动、助推剂量操纵（高低剂量比较）以及跨任务长期泛化等均未被直接检验，仅作为结构化推测提出。

## 贡献闭环

- technical_claim_cn：轻量数字助推可以在真实同步在线协作界面中改变客观协作过程并影响CI；但效果依赖具体设计，成功与失败案例并存。

- artifact_claim_cn：以集体讨论和共享认知为核心的Skill Facilitator Bot是有效的助推设计；ToDo List和Feedback Display因强化个体导向或社会比较而产生负面过程效果。

- mechanism_claim_cn：成功机制是引发关于技能和任务的集体讨论，增强共享认知；失败机制包括对静态bot预期落空后的忽略、过度规划挤占任务执行、社会比较引发心理抗拒和低贡献者退出。

- boundary_claim_cn：结果主要适用于临时、匿名、按时间计酬的陌生人团队；对既有团队、熟悉成员、不同激励结构和不同助推剂量，效果可能改变；集体目标和显性协调行动的助推更可能成功。

- reusable_design_knowledge_cn：设计数字团队助推时应优先瞄准集体层面的目标和资源，避免激发个体间比较；需要考虑剂量反应和用户适应（tolerance），开发能根据过程动态调节的干预；评价协作工具时不仅要看功能可用性，还要看其对协作过程和成员心理的影响。

- theoretical_contribution_cn：将助推理论从个体决策扩展到群体协作层面，显示个体决策助推原则不能简单平移到集体过程；支持协作过程作为集体智慧的可干预杠杆；通过结构化推测提出了团队助推设计的情境、规模、人群三个边界维度。

- how_discussion_closes_intro_gap_cn：引言提出“技术能否替代人类教练来塑造临时在线团队的协作过程”这一问题。讨论部分以实验结果回答“可以，但有条件”：Skill Bot展示了可行性，失败案例则通过结构化推测转化为具体设计条件。这直接回应了引言中关于GSS局限、传统领导者无法进入在线临时团队以及数字助推潜力的讨论。

- overclaim_or_unsupported_leaps_cn：ToDo List“抬高表现下限”和“双峰效应”的解释基于事后分数分布与评论推断，没有直接测量哪些组被托底或哪些组过度规划；Strategy Bot的“容忍/剂量过低”、Feedback Display的“公开羞辱/心理抗拒”也主要依赖参与者自述和模式比较，未操纵这些机制；结构化推测中的多数命题没有被实证检验，不能作为确定结论。

## 句级写作动作图谱

### 1. Abstract第1句

- order：1

- section：Abstract

- locator：Abstract第1句

- move_code：CONTEXT

- paraphrase_cn：互联网沟通工具的扩张使临时在线小组被广泛用于解决问题、提供服务或创造知识。

- rhetorical_function_cn：点明研究对象产生的社会技术背景。

- depends_on_cn：无

- sets_up_cn：引出协作困难和研究必要性。

- evidence_pointer：Abstract第1句

### 2. Abstract第2句

- order：2

- section：Abstract

- locator：Abstract第2句

- move_code：PRACTICAL_STAKES

- paraphrase_cn：许多这类小组难以有效协作。

- rhetorical_function_cn：指出问题严重性，为干预研究制造紧迫性。

- depends_on_cn：背景句

- sets_up_cn：需要开发和支持新型团队工作形式。

- evidence_pointer：Abstract第2句

### 3. Abstract第3-5句

- order：3

- section：Abstract

- locator：Abstract第3-5句

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：作者基于利用助推塑造行为的已有研究，报告一项对168个临时在线小组进行四种随机助推处理的实验。

- rhetorical_function_cn：说明研究的知识来源和方法选择。

- depends_on_cn：协作问题背景

- sets_up_cn：具体实验设计和结果摘要。

- evidence_pointer：Abstract第3-5句

### 4. Abstract第6-8句

- order：4

- section：Abstract

- locator：Abstract第6-8句

- move_code：RESULT

- paraphrase_cn：结果支持数字助推能改善集体智慧的基本观点，但两个助推产生了未预期的负面效果。

- rhetorical_function_cn：以简短方式报告核心发现和意外性，吸引读者。

- depends_on_cn：实验概述

- sets_up_cn：说明意外结果本身是洞察来源。

- evidence_pointer：Abstract第6-8句

### 5. Abstract最后一句

- order：5

- section：Abstract

- locator：Abstract最后一句

- move_code：CONTRIBUTION

- paraphrase_cn：作者使用结构化推测系统考虑结果成立的条件，以明确未来研究方向。

- rhetorical_function_cn：声明方法论贡献和外部效度策略。

- depends_on_cn：实验与意外结果

- sets_up_cn：读者预期讨论部分将使用structured speculation。

- evidence_pointer：Abstract最后一句

### 6. Introduction P1第1句

- order：6

- section：Introduction

- locator：Introduction P1第1句

- move_code：CONTEXT

- paraphrase_cn：临时在线小组在多种工作场景中的使用急剧增加。

- rhetorical_function_cn：建立宏观背景。

- depends_on_cn：无

- sets_up_cn：转向新型小组的协作挑战。

- evidence_pointer：Introduction P1

### 7. Introduction P1后半段

- order：7

- section：Introduction

- locator：Introduction P1后半段

- move_code：PHENOMENON

- paraphrase_cn：线上工作正从主要由独立贡献者组成的crowds演变为规模更小、互依性更强的临时在线小组，需要比标准在线工具更流畅的协调。

- rhetorical_function_cn：区分旧有任务形态和新协作形态，突出需要新的技术支持。

- depends_on_cn：背景句

- sets_up_cn：说明传统工具或方法不足。

- evidence_pointer：Introduction P1后半段

### 8. Introduction P2

- order：8

- section：Introduction

- locator：Introduction P2

- move_code：PRACTICAL_STAKES

- paraphrase_cn：在临时在线小组中鼓励高水平协作很难，因为没有既定角色或规范，协作能否形成取决于是否有成员主动影响集体过程。

- rhetorical_function_cn：说明协作困难的机制原因，强调需要通过技术方式替代传统团队领导者的设范行为。

- depends_on_cn：新型小组现象

- sets_up_cn：引入助推作为可能的解决方案。

- evidence_pointer：Introduction P2

### 9. Introduction P3

- order：9

- section：Introduction

- locator：Introduction P3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：行为经济学中的助推概念可能提供一种提示协作行为规范的途径。

- rhetorical_function_cn：引入解决方案的理论来源。

- depends_on_cn：协作困难机制

- sets_up_cn：给出研究问题和实验设计。

- evidence_pointer：Introduction P3

### 10. Introduction P4前两句

- order：10

- section：Introduction

- locator：Introduction P4前两句

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：核心研究问题是数字助推如何影响临时在线小组中协作过程的形成。

- rhetorical_function_cn：正式提出研究问题。

- depends_on_cn：助推概念引入

- sets_up_cn：描述四种数字助推和TCI实验。

- evidence_pointer：Introduction P4前两句

### 11. Introduction P4中段

- order：11

- section：Introduction

- locator：Introduction P4中段

- move_code：STUDY_OVERVIEW

- paraphrase_cn：作者在TCI上测试四种分别针对三个协作过程的数字助推，并将助推整合进数字界面。

- rhetorical_function_cn：概述实验设计和平台。

- depends_on_cn：研究问题

- sets_up_cn：报告预期与非预期结果。

- evidence_pointer：Introduction P4中段

### 12. Introduction P5

- order：12

- section：Introduction

- locator：Introduction P5

- move_code：RESULT

- paraphrase_cn：结果只是部分支持总体概念，一个助推没有效果，两个产生相反和负面效果。

- rhetorical_function_cn：提前披露意外结果，形成叙事张力。

- depends_on_cn：实验概述

- sets_up_cn：贡献中把失败案例作为洞察来源。

- evidence_pointer：Introduction P5

### 13. Introduction P6

- order：13

- section：Introduction

- locator：Introduction P6

- move_code：CONTRIBUTION

- paraphrase_cn：作者声称研究扩展临时团队、GSS和计算机中介协作文献，并借助结构化推测识别未来设计原则。

- rhetorical_function_cn：提前声明贡献和理论对话目标。

- depends_on_cn：背景与结果

- sets_up_cn：理论背景和讨论部分的结构。

- evidence_pointer：Introduction P6

### 14. Collective Intelligence and Collaborative Processes小节P1

- order：14

- section：Theoretical Background

- locator：Collective Intelligence and Collaborative Processes小节P1

- move_code：CONTEXT

- paraphrase_cn：在线问题解决组已从相对独立的crowds演变为更小、更相互依赖的临时flash teams，缺乏角色和规范使互依工作更具挑战。

- rhetorical_function_cn：延续引言现象，聚焦于CI文献。

- depends_on_cn：引言中的新型小组现象

- sets_up_cn：引入小群体绩效研究。

- evidence_pointer：Theoretical Background P1

### 15. Collective Intelligence小节P2

- order：15

- section：Theoretical Background

- locator：Collective Intelligence小节P2

- move_code：THEORY_INTRO

- paraphrase_cn：小群体绩效研究识别出三项基本协作过程：协作成员知识与技能的使用、恰当任务协调策略的发展、集体努力的生成。

- rhetorical_function_cn：引入理论构念列表。

- depends_on_cn：CI研究背景

- sets_up_cn：作为后续助推干预的目标。

- evidence_pointer：Theoretical Background P2

### 16. Collective Intelligence小节P2后半段

- order：16

- section：Theoretical Background

- locator：Collective Intelligence小节P2后半段

- move_code：THEORY_PROPOSITION

- paraphrase_cn：当这些过程缺失时，会出现社会惰化、免费搭车、知识未用和协调错误等过程损失。

- rhetorical_function_cn：为三个过程的重要性提供机制依据。

- depends_on_cn：三个过程列表

- sets_up_cn：说明其影响CI的机理。

- evidence_pointer：Theoretical Background P2后半段

### 17. Collective Intelligence小节P3

- order：17

- section：Theoretical Background

- locator：Collective Intelligence小节P3

- move_code：THEORY_PROPOSITION

- paraphrase_cn：近期研究显示这三个协作过程是线上线下团队集体智慧的重要驱动因素。

- rhetorical_function_cn：把三个过程与结果变量CI挂钩。

- depends_on_cn：过程损失理论

- sets_up_cn：选择这三个过程作为干预靶点。

- evidence_pointer：Theoretical Background P3

### 18. Collective Intelligence小节P3后半段

- order：18

- section：Theoretical Background

- locator：Collective Intelligence小节P3后半段

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：干预研究显示即使简短、早期的过程干预也能改善团队运行轨迹和绩效。

- rhetorical_function_cn：为轻量、早期数字干预提供可行性依据。

- depends_on_cn：过程驱动CI

- sets_up_cn：提出技术是否可以替代人类教练的未答问题。

- evidence_pointer：Theoretical Background P3后半段

### 19. Collective Intelligence小节P4第一句

- order：19

- section：Theoretical Background

- locator：Collective Intelligence小节P4第一句

- move_code：GAP

- paraphrase_cn：一个重要未答问题是：由技术而非有经验的人类教练执行的干预是否足以改善协作过程并提升CI。

- rhetorical_function_cn：明确提出研究缺口。

- depends_on_cn：传统团队干预研究

- sets_up_cn：对比GSS研究的不足。

- evidence_pointer：Theoretical Background P4第一句

### 20. Collective Intelligence小节P4后半段

- order：20

- section：Theoretical Background

- locator：Collective Intelligence小节P4后半段

- move_code：LIMITATION

- paraphrase_cn：GSS研究曾展示电子工具在特定活动中的好处，但结果不完全一致，且这些系统多为特定任务类型优化，而更现代的协作工具又普遍缺少结构化协作过程的特性。

- rhetorical_function_cn：指出既有技术支持和现有工具的局限。

- depends_on_cn：技术干预缺口

- sets_up_cn：定位本研究的切入空间。

- evidence_pointer：Theoretical Background P4后半段

### 21. Collective Intelligence小节P4末句

- order：21

- section：Theoretical Background

- locator：Collective Intelligence小节P4末句

- move_code：GAP

- paraphrase_cn：作者因此检验轻量数字干预能否在多种任务类型中改善协作过程。

- rhetorical_function_cn：重新表述研究切入点。

- depends_on_cn：GSS的不足

- sets_up_cn：进入数字助推理论。

- evidence_pointer：Theoretical Background P4末句

### 22. The Potential for Digital Nudging小节P1

- order：22

- section：Theoretical Background

- locator：The Potential for Digital Nudging小节P1

- move_code：LIMITATION

- paraphrase_cn：完全管理在线协作的系统设计并不可行，因为用户会抵制算法控制，尤其在社会性人际情境中。

- rhetorical_function_cn：解释为什么需要低控制、保留自主性的助推。

- depends_on_cn：技术干预缺口

- sets_up_cn：正题：助推定义和原则。

- evidence_pointer：The Potential P1

### 23. The Potential P2

- order：23

- section：Theoretical Background

- locator：The Potential P2

- move_code：MECHANISM

- paraphrase_cn：助推不强制或限制决策，而是通过选择架构引导注意力，从而提高某一结果的概率，同时保留自由选择。

- rhetorical_function_cn：解释助推的行为机制。

- depends_on_cn：算法控制抵制

- sets_up_cn：引出数字界面中的助推。

- evidence_pointer：The Potential P2

### 24. The Potential P2后半段

- order：24

- section：Theoretical Background

- locator：The Potential P2后半段

- move_code：THEORY_INTRO

- paraphrase_cn：数字助推通过用户界面设计元素引导数字选择环境中的行为。

- rhetorical_function_cn：将助推概念迁移到数字环境。

- depends_on_cn：助推定义

- sets_up_cn：介绍三类助推原则。

- evidence_pointer：The Potential P2后半段

### 25. The Potential P3

- order：25

- section：Theoretical Background

- locator：The Potential P3

- move_code：THEORY_PROPOSITION

- paraphrase_cn：设置默认值利用现状偏差和社会规范影响行为。

- rhetorical_function_cn：为ToDo List设计提供原则基础。

- depends_on_cn：数字助推概念

- sets_up_cn：设计表1中的ToDo List nudge。

- evidence_pointer：The Potential P3

### 26. The Potential P4

- order：26

- section：Theoretical Background

- locator：The Potential P4

- move_code：THEORY_PROPOSITION

- paraphrase_cn：提供即时反馈通过向用户提供比较导向的信息来改变感知和社会规范。

- rhetorical_function_cn：为Feedback Display设计提供原则基础。

- depends_on_cn：数字助推概念

- sets_up_cn：设计表1中的Feedback Display nudge。

- evidence_pointer：The Potential P4

### 27. The Potential P5

- order：27

- section：Theoretical Background

- locator：The Potential P5

- move_code：THEORY_PROPOSITION

- paraphrase_cn：结构化复杂选择通过组织选项、排序决策来引导用户依据重要标准做出更好的选择。

- rhetorical_function_cn：为两类facilitator bot设计提供原则基础。

- depends_on_cn：数字助推概念

- sets_up_cn：设计Skill和Strategy Facilitator Bot。

- evidence_pointer：The Potential P5

### 28. The Potential P6

- order：28

- section：Theoretical Background

- locator：The Potential P6

- move_code：TRANSITION

- paraphrase_cn：这些例子说明助推可能改善协作，因为多数团队在未提示时不会讨论协调，而简短讨论即可带来收益。

- rhetorical_function_cn：将助推原则从个体决策转向群体协作。

- depends_on_cn：三个原则

- sets_up_cn：同时提示复杂适应系统中的不确定性。

- evidence_pointer：The Potential P6

### 29. The Potential P7

- order：29

- section：Theoretical Background

- locator：The Potential P7

- move_code：LIMITATION

- paraphrase_cn：但团队对刺激的响应是复杂的，简单助推在协作群体这一复杂适应系统中的效果难以预测。

- rhetorical_function_cn：预先为意外结果提供理论合法性。

- depends_on_cn：群体协作复杂性

- sets_up_cn：引出研究设计的必要性。

- evidence_pointer：The Potential P7

### 30. The Potential P8

- order：30

- section：Theoretical Background

- locator：The Potential P8

- move_code：REQUIREMENT

- paraphrase_cn：为探索数字助推能否增强协作与CI，作者设计针对特定协作过程的助推并开展线上实验。

- rhetorical_function_cn：将理论转化为研究规程。

- depends_on_cn：以上理论铺垫

- sets_up_cn：方法部分。

- evidence_pointer：The Potential P8

### 31. Participants段

- order：31

- section：Methods

- locator：Participants段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者招募515名MTurk工人并随机分配到168个三人或四人小组，各组再随机分配到助推或控制条件。

- rhetorical_function_cn：描述样本和随机化策略。

- depends_on_cn：实验设计

- sets_up_cn：使因果推断成为可能。

- evidence_pointer：Methods Participants

### 32. Experimental Procedure and Platform段

- order：32

- section：Methods

- locator：Experimental Procedure and Platform段

- move_code：DESIGN_FEATURE

- paraphrase_cn：实验通过POGS浏览器平台同步协作，界面左侧为任务说明，中央为共享工作区，右侧为聊天。

- rhetorical_function_cn：描述数字环境，为读者定位助推显示位置。

- depends_on_cn：实验设计

- sets_up_cn：展示图2中的界面布局和助推位置。

- evidence_pointer：Methods Procedures

### 33. Digital Nudge Treatments + Table 1

- order：33

- section：Methods

- locator：Digital Nudge Treatments + Table 1

- move_code：DESIGN_FEATURE

- paraphrase_cn：四种助推分别为Skill Facilitator Bot、Strategy Facilitator Bot、ToDo List和Feedback Display，每种对应一个目标协作过程和助推原则。

- rhetorical_function_cn：列举干预条件的操作定义。

- depends_on_cn：助推原则介绍

- sets_up_cn：解释后文结果的对象。

- evidence_pointer：Methods Table 1

### 34. Digital Nudge Treatments第2段

- order：34

- section：Methods

- locator：Digital Nudge Treatments第2段

- move_code：REQUIREMENT

- paraphrase_cn：遵循团队干预研究，助推在团队刚开始工作时首次部署。

- rhetorical_function_cn：解释部署时机的理论依据。

- depends_on_cn：Hackman & Wageman 2005等早期干预研究

- sets_up_cn：理解为何助推出现在初始阶段。

- evidence_pointer：Methods Digital Nudge Treatments第2段

### 35. Digital Nudge Treatments末段

- order：35

- section：Methods

- locator：Digital Nudge Treatments末段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者对各助推进行多轮工程测试、调试和约4-5组pilot测试，以确保功能正常且参与者理解。

- rhetorical_function_cn：说明开发过程的严苛性，提升内部效度。

- depends_on_cn：概念设计

- sets_up_cn：使正式实验具备可信性。

- evidence_pointer：Methods Digital Nudge Treatments末段

### 36. Measures段

- order：36

- section：Methods

- locator：Measures段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：三个协作过程分别用按键总数、任务完成比例、任务技能与相对努力的组内相关来测量；CI使用TCI得分。

- rhetorical_function_cn：定义客观中介和结果变量，减少主观偏差。

- depends_on_cn：实验数据

- sets_up_cn：主分析的统计解释。

- evidence_pointer：Methods Measures

### 37. Manipulation Check段

- order：37

- section：Results

- locator：Manipulation Check段

- move_code：RESULT

- paraphrase_cn：ToDo List和Feedback Display的大多数参与者报告注意到对应工具；Skill和Strategy Bot条件下的聊天量显著高于控制组。

- rhetorical_function_cn：证明操纵暴露达到可解释的最低门槛。

- depends_on_cn：事后调查和平台日志

- sets_up_cn：使主分析结果可信。

- evidence_pointer：Results Manipulation Check

### 38. Analysis Approach段

- order：38

- section：Results

- locator：Analysis Approach段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者使用基于bootstrap的PROCESS Model 4多重中介模型，以控制条件为基线，同时估计四种nudge对三个协作过程的影响及对CI的间接效应。

- rhetorical_function_cn：说明统计方法和优势。

- depends_on_cn：数据与变量测量

- sets_up_cn：报告系数表和置信区间。

- evidence_pointer：Results Analysis Approach

### 39. Test of Experimental Nudges首段

- order：39

- section：Results

- locator：Test of Experimental Nudges首段

- move_code：RESULT

- paraphrase_cn：与既有研究一致，三个协作过程均与更高的CI相关，模型解释力较高。

- rhetorical_function_cn：复现CI与协作过程的基本关系。

- depends_on_cn：数据

- sets_up_cn：为中介解释提供基础。

- evidence_pointer：Results 首段, Table 3a Model 4

### 40. 结果(1)

- order：40

- section：Results

- locator：结果(1)

- move_code：RESULT

- paraphrase_cn：Skill Facilitator Bot按预期显著提高技能使用，并通过技能使用对CI产生显著正向间接效应。

- rhetorical_function_cn：报告预期内的成功结果。

- depends_on_cn：中介模型

- sets_up_cn：形成后期对比案例。

- evidence_pointer：Results (1), Table 3b Model 3

### 41. 结果(2)

- order：41

- section：Results

- locator：结果(2)

- move_code：RESULT

- paraphrase_cn：Strategy Facilitator Bot对任务策略没有显著影响，也没有显著间接效应。

- rhetorical_function_cn：报告空结果。

- depends_on_cn：中介模型

- sets_up_cn：进入关于Strategy Bot的探索分析。

- evidence_pointer：Results (2), Table 3b Model 2

### 42. 结果(3)

- order：42

- section：Results

- locator：结果(3)

- move_code：RESULT

- paraphrase_cn：ToDo List意外地显著削弱任务策略，并通过任务策略对CI产生负向间接效应。

- rhetorical_function_cn：报告非预期反向结果。

- depends_on_cn：中介模型

- sets_up_cn：进入ToDo List的深入探索。

- evidence_pointer：Results (3), Table 3b Model 2

### 43. 结果(4)

- order：43

- section：Results

- locator：结果(4)

- move_code：RESULT

- paraphrase_cn：Feedback Display也意外地显著降低集体努力水平，并通过努力水平对CI产生负向间接效应。

- rhetorical_function_cn：报告第二个非预期反向结果。

- depends_on_cn：中介模型

- sets_up_cn：进入Feedback Display的深入探索。

- evidence_pointer：Results (4), Table 3b Model 1

### 44. Exploring the Unexpected Results开头

- order：44

- section：Results

- locator：Exploring the Unexpected Results开头

- move_code：TRANSITION

- paraphrase_cn：面对Strategy Bot的空结果和ToDo List、Feedback Display的负向结果，作者进一步检查行为细节和开放题评论。

- rhetorical_function_cn：转入事后机制探索。

- depends_on_cn：主分析结果

- sets_up_cn：为三个意外结果分别提供行为解释。

- evidence_pointer：Exploring Unexpected Results开头

### 45. Exploring Strategy Facilitator Bot段

- order：45

- section：Results

- locator：Exploring Strategy Facilitator Bot段

- move_code：MECHANISM

- paraphrase_cn：参与者反馈显示Strategy Bot初期被认可，但随着预期落空逐渐被忽略，最终在最后任务的规划时间中其通信量反而显著低于其他条件。

- rhetorical_function_cn：为空结果提供预期落差和行为忽略的解释。

- depends_on_cn：开放题评论和聊天量比较

- sets_up_cn：为“剂量过低/容忍”的讨论铺路。

- evidence_pointer：Exploring Strategy Facilitator Bot

### 46. Exploring ToDo List段

- order：46

- section：Results

- locator：Exploring ToDo List段

- move_code：MECHANISM

- paraphrase_cn：ToDo List让本不会协调的低绩效团队早期开始讨论策略并提高最低成绩，但也使其他团队过度规划、执行时间不足，最终表现为策略质量下降。

- rhetorical_function_cn：解释总直接效应为正与负间接效应并存的“双峰”机制。

- depends_on_cn：分数分布和通信内容

- sets_up_cn：为剂量过高的讨论提供依据。

- evidence_pointer：Exploring ToDo List

### 47. Exploring Feedback Display段

- order：47

- section：Results

- locator：Exploring Feedback Display段

- move_code：MECHANISM

- paraphrase_cn：Feedback Display引发极化评价，最高贡献者依然努力，但最低贡献者比别人更少，且高低努力差距在第一项任务后即显著扩大。

- rhetorical_function_cn：解释负向努力效应的社会比较机制。

- depends_on_cn：行为数据和评论

- sets_up_cn：为“集体vs个体”目标的边界讨论提供素材。

- evidence_pointer：Exploring Feedback Display

### 48. Discussion P1

- order：48

- section：Discussion

- locator：Discussion P1

- move_code：RESULT

- paraphrase_cn：作者总结实验发现并非所有助推都成功，部分结果与预期相反。

- rhetorical_function_cn：回归主问题并设定讨论范围。

- depends_on_cn：整个实验

- sets_up_cn：引入结构化推测。

- evidence_pointer：Discussion P1

### 49. Discussion P2

- order：49

- section：Discussion

- locator：Discussion P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者解释结构化推测能够系统考虑情境、规模和人口属性如何改变结果，从而帮助表达结论的边界条件。

- rhetorical_function_cn：说明讨论部分的论证方法。

- depends_on_cn：意外结果

- sets_up_cn：展示表4和三维度讨论。

- evidence_pointer：Discussion P2

### 50. Discussion Context段

- order：50

- section：Discussion

- locator：Discussion Context段

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：作者提出个体决策助推原则在集体层面的不适配：ToDo List引发个体任务导向，Feedback Display引发人际比较，而成功的Skill Bot引发集体讨论和共享认知。

- rhetorical_function_cn：提出第一个边界条件：集体vs个体目标。

- depends_on_cn：探索性分析和相关文献

- sets_up_cn：导出设计规则。

- evidence_pointer：Discussion Context

### 51. Discussion Context末句

- order：51

- section：Discussion

- locator：Discussion Context末句

- move_code：CONTRIBUTION

- paraphrase_cn：作者推断，指向集体目标与协调行动的助推更可能成功，并建议设计者以此作为规则。

- rhetorical_function_cn：将结果上升为可复用设计规则。

- depends_on_cn：成功与失败的对比

- sets_up_cn：转向剂量和人群边界。

- evidence_pointer：Discussion Context末 

### 52. Discussion Scalability段

- order：52

- section：Discussion

- locator：Discussion Scalability段

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：作者类比药物剂量效应，认为Strategy Bot的剂量太低会被忽略，ToDo List剂量太高会挤占任务执行，静态助推可能随使用产生耐受性。

- rhetorical_function_cn：提出第二个边界条件：剂量-反应和容忍。

- depends_on_cn：Strategy和ToDo List的探索结果

- sets_up_cn：主张自适应、智能的助推系统。

- evidence_pointer：Discussion Scalability

### 53. Discussion Population段

- order：53

- section：Discussion

- locator：Discussion Population段

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：作者推断临时、匿名、“白纸”团队最容易被助推塑造；既有团队的效果取决于心理安全；激励结构也会改变助推效应。

- rhetorical_function_cn：提出第三个边界条件：团队类型、成员关系和激励。

- depends_on_cn：实验样本特征与相关文献

- sets_up_cn：限定结果的推广范围。

- evidence_pointer：Discussion Population

### 54. Discussion Population末段

- order：54

- section：Discussion

- locator：Discussion Population末段

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：作者总结实验结果应推广到其他临时匿名团队，并可能在对熟悉度、激励或声誉压力有不同配置的样本中更强或更弱。

- rhetorical_function_cn：综合三维度推测，给出外部效度判断。

- depends_on_cn：Context/Scalability/Population讨论

- sets_up_cn：结论部分。

- evidence_pointer：Discussion Population末

### 55. Conclusion首句

- order：55

- section：Conclusion

- locator：Conclusion首句

- move_code：CONTRIBUTION

- paraphrase_cn：作者总结数字助推特别是具备更复杂社会智能的助推，可以在提升集体智慧方面发挥作用。

- rhetorical_function_cn：给出总体判断和未来方向。

- depends_on_cn：实验结果和结构化推测

- sets_up_cn：结束全文。

- evidence_pointer：Conclusion首句

### 56. Conclusion末句

- order：56

- section：Conclusion

- locator：Conclusion末句

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：作者表示若校准得当，这类干预可帮助临时在线团队快速形成重要集体认知，从而解决更复杂的问题。

- rhetorical_function_cn：展望未来价值，同时暗示当前设计仍需要谨慎校准。

- depends_on_cn：全部研究

- sets_up_cn：无

- evidence_pointer：Conclusion末句

## 写作技术

- gap_construction_cn：先用临时在线小组增长和协作困难构建现实问题，再指出传统团队领导者无法在缺乏角色和规范的在线临时环境中设范，接着揭示GSS虽有益但与任务类型绑定、现代协作工具又缺少对协作过程的结构化支持，最后把“技术能否替代人类教练”作为未答问题。随后又将助推从个体决策引入群体过程，制造理论迁移的不确定性作为研究空白。

- signposting_cn：引言在背景铺陈后直接声明中心研究问题；理论背景用两个小节分别建立协作过程和数字助推原则；方法中表1列出四个nudge与目标过程的对应；结果部分按(1)-(4)逐一报告每个nudge；探索性分析按Strategy Bot、ToDo List、Feedback Display分小节；讨论用表4给出Context/Scalability/Population三维度，并逐节展开。

- transition_logic_cn：从问题到理论用“一个可能获得洞见的领域是……”；从理论到设计用“这些例子说明……因此，为了探索……”；从主分析到探索分析用“面对空结果和意外负向结果，我们进一步检查……”；从探索到讨论用“我们提供了潜在解释，并通过结构化推测进一步讨论”；讨论内部按情境、规模、人群三段递进，并以“综上，我们推测……”收束。

- claim_evidence_rhythm_cn：先复现协作过程-CI的域内关系，再逐项报告每个nudge对过程的独立效应和对CI的间接效应；意外结果用“unexpectedly”明确标记，并紧接着给出行之有效的探索性证据：聊天量、努力差距、用户评论等。推测性解释与数据描述分开，避免把事后解释当作因果结论。

- benchmark_narrative_cn：控制组是每个nudge效果的最基本基准；使用bootstrap置信区间的间接效应提供统计基准；事后分析用不同时间阶段的通信量和最高/最低贡献者的努力差作为行为基准；结构化推测则借助相关文献和Glikson et al. 2019的真实团队反馈干预作为外部基准。

- theory_return_cn：讨论部分不是只重述结果，而是把成功与失败重新嵌套进群体复杂适应系统的理论视角：将助推原则区分为集体/个体目标、将无效结果解释为剂量和容忍、将负效应解释为心理比较，从而把实验结果升华为对助推理论在群体层面适用条件的修正。

- contribution_positioning_cn：作者将贡献定位为对临时团队、GSS和计算机中介协作文献的扩展，并把“意外结果”作为理论洞察来源；通过结构化推测把失败案例转变成边界条件和设计原则，避免被解读为一次性负面结果。

- novelty_protection_cn：通过如实报告一个成功、一个无效、两个负向结果，使研究看上去更可信；以成功的Skill Bot作为正面锚点，用它和失败案例的对比把贡献从“某个nudge有效”提升为“nudge设计必须匹配群体水平”；再用结构化推测和文献对比保护结论的普遍性，降低退化为一次性性能结果的风险。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：写作任务：建立临时在线小组增长和协作困难的现实背景。

- research_job_cn：研究任务：用文献和现象文档说明新型协作形态及其困境。

- required_evidence_cn：需要证明该现象重要且现有协作工具或方法不足。

- transition_to_next_cn：从“团队领导者无法在临时在线环境中设范”过渡到“需要技术干预”。

#### 2. 2

- step：2

- writing_job_cn：写作任务：梳理小群体绩效或相关理论，确定可干预的关键过程。

- research_job_cn：研究任务：选择并论证哪些过程是结果变量的驱动因素。

- required_evidence_cn：需要已有实证或元分析支持该过程与结果的关系。

- transition_to_next_cn：用“一个重要未答问题是……”引出技术干预缺口。

#### 3. 3

- step：3

- writing_job_cn：写作任务：对比既有技术干预（如GSS）的局限，指出新方法必要性。

- research_job_cn：研究任务：明确为什么轻量数字助推不同于以往系统。

- required_evidence_cn：需要GSS或协作工具研究中的不一致或局限证据。

- transition_to_next_cn：进入助推原则并说明如何映射到设计。

#### 4. 4

- step：4

- writing_job_cn：写作任务：把理论原则转化为明确的设计要求和制品特征。

- research_job_cn：研究任务：构建多个可比较的数字干预变体。

- required_evidence_cn：每个设计选择都需要理论或先例依据。

- transition_to_next_cn：描述工程实现和pilot测试。

#### 5. 5

- step：5

- writing_job_cn：写作任务：报告平台、任务、操纵检查、样本和随机化程序。

- research_job_cn：研究任务：进行工程迭代、pilot测试和正式实验数据采集。

- required_evidence_cn：需要操纵检查数据证明参与者确实注意到干预。

- transition_to_next_cn：进入统计模型与结果报告。

#### 6. 6

- step：6

- writing_job_cn：写作任务：向读者交代统计模型、中介路径和客观指标，按预期/非预期分类报告结果。

- research_job_cn：研究任务：运行多重中介或类似模型，并做必要的稳健性和对照分析。

- required_evidence_cn：需要回归系数、置信区间和间接效应证据。

- transition_to_next_cn：对意外结果进行探索性分析。

#### 7. 7

- step：7

- writing_job_cn：写作任务：用行为数据、评论和阶段比较解释意外结果。

- research_job_cn：研究任务：做事后机制探索，但不能宣称因果。

- required_evidence_cn：需要可量化的行为差异或定性评论佐证机制。

- transition_to_next_cn：用结构化推测等方式讨论边界。

#### 8. 8

- step：8

- writing_job_cn：写作任务：把结果提升为边界条件和设计原则，明确指出未验证命题。

- research_job_cn：研究任务：对照文献和先例，提出可检验未来假设。

- required_evidence_cn：边界条件需要有理论逻辑或文献对照支撑，而非空泛宣称。

- transition_to_next_cn：结论中概括贡献并展望自适应或智能干预。

### most_transferable_moves_cn

1. 把理论与经验知识映射到具体界面设计并用表呈现对应关系。

2. 用操纵检查先证明干预被感知，再进行效果检验。

3. 同时报告预期结果、无效结果和反向结果，并用客观行为指标支撑解释。

4. 用structured speculation或类似的边界推演把意外结果转化为设计知识。

### resource_intensive_or_nonstandard_parts_cn

1. POGS同步在线协作平台的开发和维护。

2. TCI任务电池及其多数据集效度证据。

3. 大规模MTurk同步小组实验的招募和调度。

4. 实时行为日志与开放式评论的编码分析。

5. 多轮工程调试和pilot测试。

### what_not_to_copy_superficially_cn

1. 不能只在界面放一个聊天机器人、ToDo小组件或参与度仪表就宣称“数字助推”；必须有操纵检查。

2. 不能把事后探索性解释表述为因果结论。

3. 不能把结构推测中的未来方向当作已验证的边界条件。

4. 不能在没有CI或等效群体绩效指标的情况下，把过程变化直接等同于绩效提升。

- single_best_description_of_the_routine_cn：把一个多结果、有失败的随机实验，通过“理论映射设计→操纵检查→客观中介检验→事后行为机制解释→结构化推测边界”的写作算法，转化为可复用的团队助推设计知识。

## 分析边界

分析仅基于所提供的论文全文，未获得附录、在线材料或补充文件；图2界面截图和部分表格细节只能依据文字描述推断；结构化推测是概念性写作阶段而非严格实证阶段，阶段划分带有分析者判断成分。
