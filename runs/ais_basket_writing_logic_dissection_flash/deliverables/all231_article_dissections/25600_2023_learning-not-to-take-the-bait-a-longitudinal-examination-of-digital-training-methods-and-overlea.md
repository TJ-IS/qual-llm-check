# Learning not to take the bait: a longitudinal examination of digital training methods and overlearning on phishing susceptibility

- 作者：Christopher Nguyen; Matthew Jensen; Eric Day
- 年份 / 期刊：2023 / European Journal of Information Systems
- DOI：10.1080/0960085x.2021.1931494
- 源文件：25600_2023_learning-not-to-take-the-bait-a-longitudinal-examination-of-digital-training-methods-and-overlea.md
- 论文主类型：theory_derived_artifact_experiment
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.9

## 文章级论证概况

- 核心问题：在两种反钓鱼数字培训（规则式与正念式）中，培训效果在2个月后如何衰减；将过度学习作为保持策略加入培训，能否显著增强技能保持并降低钓鱼易感性；过度学习与培训方式之间是否存在交互。

- 制品与设计：不是信息系统制品本身，而是三类数字培训课程（规则式、正念式、密码管理控制组）与过度学习操纵（100%过度学习=额外6封练习邮件，共12封；无过度学习=6封）。测试物料包括两版各10封邮件的邮件识别测验和两轮各5封的模拟钓鱼邮件。

- 客观结果：正念培训在辨别力（d'）和模拟钓鱼点击分数上显著优于规则式和控制组，且在2个月后仍保持优势；响应偏向（c）上正念仅在即时测验中更谨慎，2个月后与规则式/控制组无差异。过度学习显著提高响应谨慎度和模拟钓鱼得分，但未提高辨别力，且与培训方式无显著交互。

- 核心贡献：通过2个月纵向实验证明正念式反钓鱼培训比规则式更持久地降低钓鱼易感性，且不以增加误报为代价；将过度学习引入反钓鱼培训并发现其仅增强谨慎而非辨别力；使用SDT将‘能否辨别’与‘是否谨慎’分离，为反钓鱼培训评估提供了更细粒度框架。

- 整篇论证链：作者从钓鱼攻击损失巨大且技术防御可被绕过出发，指出现有反钓鱼数字培训虽然有效但效果随时间衰减，且已有研究仅覆盖1个月以内、多数只针对规则式培训。接着引入正念式培训作为系统化信息处理的替代方案，并将过度学习作为可能提升技能保持的训练策略，但指出其与正念培训可能因自动化和刻意注意的目标冲突而产生反效果。研究采用3×2×2混合设计纵向实验，在训练后立即和10周后分别用邮件识别测验测量辨别力与响应偏向，并在1周和8周时向参与者真实邮箱发送模拟钓鱼邮件测量实际点击行为。结果显示正念培训在辨别力和防钓鱼上显著且持久优于规则式和控制组，过度学习只提升谨慎和降低点击，不提升辨别力，且二者无交互。作者据此提出：反钓鱼培训应当训练人们暂停、思考、核验，而不仅仅是增加练习量；同时应使用多种测量环境评估培训迁移。

## 类型与写作弧线判定

- 论文主类型判定：训练课程是基于正念理论和规则式培训知识构建的行为干预制品，并在纵向受控实验中被检验；没有设计科学式构建评价循环，也没有现场平台自然实验，而是理论推导出的培训处理与实验对照。

- 主导写作弧线判定：以现实钓鱼损失切入，引入正念、过度学习理论和已有经验知识，设计训练与过度学习操纵，通过纵向实验检验，再在讨论中回到理论含义和边界条件。

## 研究开展程序

- study_or_phase_count：5

- 研究阶段总序列：阶段顺序为：材料开发与预测试→即时邮件识别测验→第一轮真实邮箱模拟钓鱼→第二轮模拟钓鱼与延迟邮件识别测验→补充分析。前两个阶段建立训练即时效应，第三阶段验证迁移到日常邮箱行为，第四阶段检验2个月保持与衰减，第五阶段对操作化稳健性和条件特异性做边界检验。各阶段依次累积：没有材料预测试就无法保证操纵效度；没有Time1基线就无法解释Time2衰减；没有真实邮箱测试就无法说明迁移；没有补充分析就无法处理过度学习操作化的潜在混淆。

### studies_or_phases

#### 1. 培训内容与测量材料开发及预测试

- order：1

- name_cn：培训内容与测量材料开发及预测试

- question_cn：如何将规则式、正念式与过度学习操纵化为可比、等难度的数字培训材料？

- inputs_and_setting_cn：Jensen et al. (2017) 培训材料、学术/政府/非营利/企业反钓鱼指南、IT安全经理评审、学生样本预测试。

- designed_or_compared_object_cn：三类培训网页（规则式、正念式、密码管理控制）、6/12封练习邮件、两版10封邮件识别测验、两轮5封模拟钓鱼邮件。

- baseline_control_or_counterfactual_cn：控制组接受密码管理培训；邮件难度通过预测试保证；练习条件通过预测试确定。

##### objective_metrics

1. 邮件难度相等性

2. 初始学习标准（6封中正确识别4封）

3. 过度学习量(100%)

- analysis_method_cn：预测试和基于以往研究的基准设定。

- main_result_cn：确定100%过度学习（额外6封）作为操纵；练习邮件数量为6封 vs 12封；开发出两版邮件集并做counterbalance。

- argumentative_role_cn：保证后续实验的构念效度与材料可比性，避免把材料难度混入培训效应。

- remaining_uncertainty_cn：材料在真实纵向情景下的实际效果未知。

- link_to_next_phase_cn：提供可直接施测的训练和测验工具，进入正式实验。

##### evidence_pointers

1. Section 14 Overlearning conditions

2. Section 15 Learning measures

3. Figure 1

#### 2. 即时训练效果检验（Time1邮件识别测验）

- order：2

- name_cn：即时训练效果检验（Time1邮件识别测验）

- question_cn：训练后立即，规则式与正念式是否优于不训练的密码组，且正念是否优于规则式？

- inputs_and_setting_cn：453名大学生；三类培训后立即完成的10封邮件识别测验。

- designed_or_compared_object_cn：比较三种训练条件；测量d'与c。

- baseline_control_or_counterfactual_cn：控制训练作为无反钓鱼训练基线；规则式作为既有方法参照。

##### objective_metrics

1. d' 辨别力

2. c 响应偏向

- analysis_method_cn：3×2×2混合设计ANCOVA，计划比较。

- main_result_cn：正念训练的d'显著高于控制组和规则式；规则式不显著优于控制组；响应偏向上正念在T1更谨慎，而规则式与控制组无差异。

- argumentative_role_cn：确认训练是否产生初始能力差异，支持H2a、H3a、H2b/H3b部分。

- remaining_uncertainty_cn：即时效果不等于长期保持；需要后续时点和真实邮箱行为。

- link_to_next_phase_cn：为Time2提供Time1基线，用于判断衰减。

##### evidence_pointers

1. Table 2

2. Table 4

3. Table 5

4. Results Section 18

#### 3. 第一轮模拟钓鱼攻击（训练后1周，真实邮箱迁移测试）

- order：3

- name_cn：第一轮模拟钓鱼攻击（训练后1周，真实邮箱迁移测试）

- question_cn：训练能否迁移到日常邮箱处理，减少一周后的实际点击？

- inputs_and_setting_cn：5封模拟钓鱼邮件发送至参与者真实大学邮箱；Wombat ThreatSim生成、分发和追踪。

- designed_or_compared_object_cn：在真实邮箱环境中观察点击行为；邮件来自可识别的大学来源。

- baseline_control_or_counterfactual_cn：三种训练条件之间比较；控制组为基线。

##### objective_metrics

1. 模拟钓鱼邮件点击数（反向计分）

- analysis_method_cn：混合ANCOVA中的计划比较。

- main_result_cn：正念训练的模拟钓鱼得分显著高于规则式和控制组；规则式与控制组无差异。

- argumentative_role_cn：证明正念训练可以迁移到生态化邮件处理，而不是仅在实验任务中有效。

- remaining_uncertainty_cn：是否随时间保持仍需第二轮；仅点击数不能反映辨别力。

- link_to_next_phase_cn：引出8周后的第二轮测量以检验衰减与保持。

##### evidence_pointers

1. Figure 1

2. Section 15 Learning measures

3. Table 6

#### 4. 保持与衰减检验（8周模拟钓鱼 + 10周邮件识别测验）

- order：4

- name_cn：保持与衰减检验（8周模拟钓鱼 + 10周邮件识别测验）

- question_cn：训练和过度学习的优势能否在2个月后保持？过度学习是否提高保持？

- inputs_and_setting_cn：第二轮5封模拟钓鱼邮件（8周）；10周后在线第二版邮件识别测验。

- designed_or_compared_object_cn：重复测量Time1-Time2；比较训练×过度学习×时间交互。

- baseline_control_or_counterfactual_cn：Time1成绩作为自身对照；规则式/控制组作为正念的对照。

##### objective_metrics

1. d' Time2

2. c Time2

3. 模拟钓鱼测试2得分

- analysis_method_cn：Time×Training、Time×Overlearning、Time×Training×Overlearning交互和T2计划比较。

- main_result_cn：正念在T2的d'仍显著高于规则式和控制组，且T2模拟钓鱼得分高于规则式；H4a/H4c支持。过度学习在T2无显著优势，H6不支持；训练与过度学习无交互，H7不支持。

- argumentative_role_cn：识别哪些效果是持久的，哪些只即时存在；排除过度学习作为保持机制。

- remaining_uncertainty_cn：缺乏纯粹无训练/无练习控制；不能判断更长时期或最优过度学习量；10周测验可能受第二轮模拟钓鱼影响。

- link_to_next_phase_cn：补充分析进一步检查不达标学习者对结论的稳健性。

##### evidence_pointers

1. Tables 4-6

2. Figures 2-4

3. Results Sections 19-22

#### 5. 补充分析：学习者亚组与条件配对比较

- order：5

- name_cn：补充分析：学习者亚组与条件配对比较

- question_cn：排除未达到初始学习标准的参与者后，结果是否稳健？哪些训练条件下过度学习有实际收益？

- inputs_and_setting_cn：原453人中达到练习中6封对4封标准的300人；各条件成对比较。

- designed_or_compared_object_cn：对‘真正学习者’样本重跑主要模型；比较各训练×过度学习组合在T2的表现。

- baseline_control_or_counterfactual_cn：总体样本结果作为参照。

##### objective_metrics

1. d'、c、模拟钓鱼得分在亚组中的效应模式

2. 成对比较的显著差异

- analysis_method_cn：补充ANCOVA（附录K）和成对比较（附录L）。

- main_result_cn：总体模式在亚组中相似，但过度学习对模拟钓鱼得分和c的主效应不再显著；成对比较显示规则式+过度学习在总体表现上收益最大，正念+过度学习在T2模拟钓鱼保持上更有利。

- argumentative_role_cn：证明过度学习效应不依赖未学习者；揭示条件特异性收益，为边界条件提供证据。

- remaining_uncertainty_cn：非预注册、事后比较；控制组也接受练习和反馈；不能证明因果机制。

- link_to_next_phase_cn：为讨论中‘过度学习作用有限但并非无用’的定性结论提供支持。

##### evidence_pointers

1. Section 23 Supplemental analyses

2. Appendices J-L

## 各部分修辞架构

### abstract_moves

1. CONTEXT: phishing sophisticated and costly

2. PRIOR_KNOWLEDGE: digital training reduces susceptibility

3. LIMITATION: training effects degrade over time

4. RQ_OR_OBJECTIVE: investigate overlearning to increase retention

5. STUDY_OVERVIEW: longitudinal experiment crossing overlearning with rule-based, mindfulness, control

6. RESULT: mindfulness better retention; overlearning reduces susceptibility; no interaction

7. CONTRIBUTION: benefits of mindfulness stable over time without increasing missed legit emails

### introduction_moves

1. CONTEXT/Practical stakes: FBI losses

2. PHENOMENON: phishers mimic legitimate senders, technology not foolproof

3. PRIOR_KNOWLEDGE: training works; rule-based and mindfulness approaches

4. LIMITATION: existing retention studies <=1 month

5. GAP: no research on retention strategies in anti-phishing; overlearning not examined

6. WHY_GAP_MATTERS: severe consequences and training costs

7. RQ_OR_OBJECTIVE: extend Jensen et al. with longitudinal overlearning crossing

8. METHOD_JUSTIFICATION: student sample, real inboxes, SDT metrics

### theory_and_knowledge_moves

1. THEORY_INTRO: rule-based relies on stable cues and System1

2. THEORY_INTRO: mindfulness promotes System2 and IT mindfulness

3. MECHANISM: stop-think-check; attention allocation

4. THEORY_PROPOSITION: overlearning reinforces stimulus-response bonds and automaticity

5. PRIOR_KNOWLEDGE: overlearning meta-analysis effect

6. LIMITATION: overlearning studies lab tasks and short intervals

### artifact_design_moves

1. REQUIREMENT: need retention strategy complementing training

2. DESIGN_FEATURE: 100% overlearning = 6 extra practice emails

3. DESIGN_FEATURE: three training conditions

4. DESIGN_FEATURE: email identification tests with d' and c

5. DESIGN_FEATURE: mock phishing emails to actual inboxes

6. BENCHMARK_OR_CONTRAST: control training as no-anti-phishing baseline

7. METHOD_JUSTIFICATION: counterbalancing, pilot testing, covariates

### evaluation_moves

1. STUDY_OVERVIEW: 3x2x2 mixed ANCOVA

2. BENCHMARK_OR_CONTRAST: plan comparisons vs control and rule-based

3. RESULT: rule-based not better than control

4. RESULT: mindfulness > control and rule-based on d' and mock scores

5. RESULT: overlearning effects on c and mock scores but not d'

6. RESULT: no Time x Overlearning interactions

7. ROBUSTNESS_OR_BOUNDARY_TEST: supplemental learner subsample and pairwise comparisons

### discussion_and_contribution_moves

1. CONTRIBUTION: extends Jensen et al. to 2-month retention

2. MECHANISM: mindfulness leads to balanced caution without false positives

3. BOUNDARY_CONDITION: rule-based may desensitize; control practice with feedback may mimic rules

4. BOUNDARY_CONDITION: overlearning increases caution but not discrimination and may reduce productivity

5. BOUNDARY_CONDITION: no interaction between training and overlearning

6. THEORETICAL_CONTRIBUTION: advances IT mindfulness and overlearning to realistic task

7. LIMITATION_AND_FUTURE: no pretest, repeated mock exposure, no combined training, overlearning amount uncertainty, control also practiced, only link-click phishing

8. PRACTICAL_STAKES: minimal training resources; layered defense; caution against overcaution

## 理论/知识到设计的翻译

### 知识/理论基础

1. IT mindfulness (Langer; Thatcher et al.; Jensen et al.)

2. Rule-based training literature

3. Overlearning and skill retention (Driskell et al.; Arthur et al.)

4. Signal Detection Theory (Green & Swets)

5. Heuristic-systematic processing (Vishwanath et al.)

- 理论—设计耦合：direct

- 耦合判定理由：培训方式（规则式 vs 正念式）来自已有理论/初步研究，过度学习操纵来自技能保持理论和元分析证据；因变量采用SDT理论推导出的d'和c；假设均从理论命题直接推出并被实验结果检验。

- 理论到设计翻译链：理论/经验知识→机制→设计要求→具体培训材料/操纵→被比较的条件→客观结果。具体而言：规则式培训的局限（System1、固定线索易过时）→需要替代方案→正念式培训（stop/think/check）→与规则式和控制组对比→发现正念在辨别力和防钓鱼上更好；过度学习理论（继续练习形成自动性）→为提升保持→在掌握练习后增加6封练习邮件→与无过度学习对比→发现仅提高谨慎和降低点击，不提高辨别力；技能衰减理论和深度加工→评估2个月保持→T1/T2重复测量→发现正念优势保持而过度学习不保持；SDT→将能力与偏向分开→使用d'和c→发现训练影响d'而过度学习影响c。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：规则式培训假设钓鱼邮件共享稳定线索，但攻击者可使线索过时；依赖简单规则会鼓励System1启发式处理。

- mechanism_cn：用户不加思考地响应合规技巧；固定线索占用注意力而不是促进反思。

- design_requirement_cn：需要一种不依赖固定线索、能促进System2系统化评估的培训。

- artifact_choice_cn：正念式培训：停止、思考、核验三步内容。

- evaluated_contrast_cn：正念培训 vs 规则式培训；正念培训 vs 控制培训。

- objective_result_cn：正念培训在d'和模拟钓鱼得分上显著更好，在响应偏向上T1更谨慎但T2无差异。

##### evidence_pointers

1. Section 2

2. Section 3

3. Section 8

4. Tables 4-6

#### 2. 2

- theory_or_knowledge_claim_cn：正念是对当下经验的注意与觉察，IT正念可应用于邮件评估；Jensen等已提出三步法。

- mechanism_cn：暂停、全面参与、延迟判断使个体对上下文和请求动机进行深度加工。

- design_requirement_cn：培训应引导学习者暂停行动、提问、并在不确定时向第三方核验。

- artifact_choice_cn：正念培训内容：stop/think/check。

- evaluated_contrast_cn：正念 vs 控制；正念 vs 规则式，在T1与T2。

- objective_result_cn：正念组d'显著更高、模拟钓鱼点击更少，且这些优势在2个月后保持。

##### evidence_pointers

1. Section 3

2. Section 13 Training conditions

3. Results 19

#### 3. 3

- theory_or_knowledge_claim_cn：过度学习是达到初始掌握后继续练习，通过重复和反馈强化刺激-反应联结，形成自动性并提高保持。

- mechanism_cn：自动性减少认知需求；重复反馈将技能固化为长时记忆。

- design_requirement_cn：在掌握性练习后提供额外练习机会；操作上采用100%过度学习。

- artifact_choice_cn：无过度学习=6封练习邮件；100%过度学习=额外6封共12封，均有反馈。

- evaluated_contrast_cn：过度学习 vs 无过度学习，在总体和T2。

- objective_result_cn：过度学习显著增加谨慎（更负的c）和模拟钓鱼得分，但没有显著提高d'；T2无保持优势。

##### evidence_pointers

1. Section 5

2. Section 14

3. Section 20-21

4. Tables 5-6

#### 4. 4

- theory_or_knowledge_claim_cn：技能保持随时间衰减；深度加工促进长时记忆和迁移。

- mechanism_cn：正念培训的经验导致更深加工，因此保持更好；规则式浅层加工更易遗忘。

- design_requirement_cn：评估应跨越比已有研究更长的保留间隔，并同时在测验和日常邮箱中测量。

- artifact_choice_cn：10周邮件识别测验和8周模拟钓鱼邮件；采用counterbalanced两版材料。

- evaluated_contrast_cn：Time1 vs Time2；训练×时间交互。

- objective_result_cn：正念在T2的d'和模拟钓鱼得分仍优于规则式；规则式不优于控制；响应偏向在T2差异消失。

##### evidence_pointers

1. Section 4

2. Section 6

3. Section 19

4. Figures 2-4

#### 5. 5

- theory_or_knowledge_claim_cn：Signal Detection Theory区分辨别力d'与响应偏向c，分别代表能力与谨慎倾向。

- mechanism_cn：两个用户可能有相同辨别力但不同判为钓鱼的标准；c负值表示偏好判为钓鱼。

- design_requirement_cn：评估不应只看命中率，还要看误报率；应同时报告d'和c。

- artifact_choice_cn：邮件识别测验中5钓5合法，用命中率和误报率计算d'和c。

- evaluated_contrast_cn：训练和过度学习在d' vs c上的不同效应模式。

- objective_result_cn：训练主要影响d'，过度学习主要影响c，证明二者作用于不同心理过程。

##### evidence_pointers

1. Section 6

2. Section 15

3. Tables 4-5

## 评价逻辑

### evaluation_modes

1. 实验室式邮件识别测验（即时与10周）

2. 真实邮箱模拟钓鱼攻击（1周与8周）

3. Signal Detection Theory指标（d'、c）

4. 混合设计ANCOVA与计划比较

5. 补充亚组分析（排除未达标学习者）

- why_these_evaluations_cn：因为训练研究有两类风险：能力是否习得（最大化表现）和日常是否使用（典型表现）。邮件识别测验能分离辨别力和响应偏向；模拟钓鱼邮件能测试真实环境中的点击行为；两次时点检验衰减；ANCOVA控制个体差异；补充分析解决过度学习操作化的潜在混淆。

- benchmark_and_contrast_chain_cn：先用控制培训建立‘未接受反钓鱼训练’基线；再用规则式作为已有一流方法；正念式作为新方法；每条假设都沿d'、c、模拟点击三个指标展开。结果链条为：规则式基本不优于控制→正念优于二者→过度学习只在c和点击上有效→时间交互只对训练显著而不对过度学习显著→补充分析显示规则式+过度学习总体收益最大、正念+过度学习对T2点击保持有利。

### claim_evidence_ledger

#### 1. 正念培训能提高辨别力并减少模拟钓鱼点击，且优于规则式和控制组。

- claim_cn：正念培训能提高辨别力并减少模拟钓鱼点击，且优于规则式和控制组。

- evidence_cn：d'在T1/T2显著更高；模拟钓鱼得分显著更高；Tables 4-6。

- supported：是

#### 2. 规则式培训优于不培训。

- claim_cn：规则式培训优于不培训。

- evidence_cn：规则式与控制组在d'、c、模拟得分上均无显著差异。

- supported：否

#### 3. 正念培训使人们更谨慎（响应偏向更负）。

- claim_cn：正念培训使人们更谨慎（响应偏向更负）。

- evidence_cn：T1时c显著更负；T2时与规则式/控制无差异。

- supported：否

#### 4. 过度学习能提高辨别力。

- claim_cn：过度学习能提高辨别力。

- evidence_cn：d'主效应不显著。

- supported：否

#### 5. 过度学习能提高谨慎并减少点击。

- claim_cn：过度学习能提高谨慎并减少点击。

- evidence_cn：c和模拟钓鱼得分主效应显著。

- supported：是

#### 6. 过度学习能提高2个月后的保持。

- claim_cn：过度学习能提高2个月后的保持。

- evidence_cn：Time×Overlearning交互不显著；T2计划比较无差异。

- supported：否

#### 7. 过度学习对规则式比对正念式更有保持效应。

- claim_cn：过度学习对规则式比对正念式更有保持效应。

- evidence_cn：Training×Overlearning和三维交互均不显著。

- supported：否

#### 8. 正念培训不增加误报合法邮件。

- claim_cn：正念培训不增加误报合法邮件。

- evidence_cn：d'更高且误报率未系统升高；Tables 2-3。

- supported：是

#### 9. 控制组从练习和反馈中学习了钓鱼识别。

- claim_cn：控制组从练习和反馈中学习了钓鱼识别。

- evidence_cn：控制组c随时间更负、模拟得分上升；间接支持。

- supported：否

- internal_validity_strategy_cn：随机分配、counterbalance测试版本、对邮件呈现顺序和发送时间随机化、使用协变量控制个体差异、预测试保证材料难度相等、让IT部门确保邮件不被拦截、不回应参与者询问以防泄题、补充分析排除未达标学习者。

- external_validity_strategy_cn：使用参与者真实大学邮箱和Wombat ThreatSim发送模拟钓鱼邮件；邮件来自可识别的大学来源；两轮模拟分布在不同时间点；识别测验与真实点击行为同时测量，能观察培训和泛化；学生样本本身是易感人群。

- what_is_not_actually_tested_cn：没有直接测量注意力分配或深度加工等机制变量；没有测量工作生产力损失；没有同时考察规则式+正念组合；只测试了链接点击这一种钓鱼请求；没有测试超出2个月的衰减；没有真正的无训练无练习控制；没有测试不同过度学习量；没有预注册。

## 贡献闭环

- technical_claim_cn：正念式反钓鱼数字培训在邮件辨别力和模拟钓鱼点击上优于规则式和控制组，且2个月后仍保持；过度学习能降低点击和增强谨慎但不能提高辨别力。

- artifact_claim_cn：是培训内容中‘停止-思考-核验’的具体设计带来了正念优势；额外6封练习邮件带来的过度学习产生了谨慎效应；由于无交互，不能主张过度学习改变了某种培训的效果。

- mechanism_claim_cn：正念培训通过促进系统化、刻意注意和延迟判断来提高深度加工和迁移；过度学习通过自动性/重复反馈增强谨慎和警觉，但未提高辨别能力；因二者机制看似竞争但实际互不影响。

- boundary_claim_cn：上述效应在2个月保留区间、100%过度学习、链接点击型钓鱼、大学生样本和大学邮箱情境中成立；正念的优势在2个月后仍存在；过度学习的收益主要体现在即时谨慎和点击降低而非长期辨别。

- reusable_design_knowledge_cn：反钓鱼培训设计应重视教授可迁移的注意与核验策略（暂停、思考、核验），而非仅固定规则清单；评估设计应采用多时点、多环境（测验+真实邮箱）和SDT双指标；增加练习可增强谨慎但应配合辨别力训练以免误报；控制组也可能通过练习学习，因此真正的无训练基线需要更严格设计。

- theoretical_contribution_cn：扩展了IT mindfulness在安全培训中的理论应用：证明正念培训可诱导并长期保持与钓鱼抵抗相关的IT正念；扩展overlearning理论：在真实世界任务和两种培训类型间比较过度学习，确认其作用边界（影响偏向而非辨别）。

- how_discussion_closes_intro_gap_cn：引言提出‘培训效果随时间衰减、缺少保持策略、过度学习在反钓鱼中未被检验’的缺口；讨论用保留数据证明正念的长期优势、规则式的非优势、过度学习仅对谨慎有效且无交互，从而将缺口闭合为‘需要针对注意力策略而不是简单重复练习’的设计知识。

- overclaim_or_unsupported_leaps_cn：作者从‘没有增加误报’推断‘不影响工作效率’略宽；控制组也接受练习和反馈，因此规则式与‘不培训’比较的效应可能被低估；未测量机制变量，却用‘系统化加工’‘自动性’解释结果，属于事后机制叙述；H4b不支持后仍把‘正念保持谨慎’写入摘要需小心；补充分析中的规则式+过度学习收益是事后比较。

## 句级写作动作图谱

### 1. Abstract S1

- order：1

- section：Abstract

- locator：Abstract S1

- move_code：CONTEXT

- paraphrase_cn：随着钓鱼攻击越来越复杂和昂贵，需要能改善并延长抵抗力的干预。

- rhetorical_function_cn：开篇建立问题重要性和紧迫性。

- depends_on_cn：无。

- sets_up_cn：为‘需要培训且培训效果要持久’提供动机。

- evidence_pointer：Abstract第一句

### 2. Abstract S2

- order：2

- section：Abstract

- locator：Abstract S2

- move_code：LIMITATION

- paraphrase_cn：已有研究支持数字培训能降低钓鱼易感性，但其效果会随时间衰减。

- rhetorical_function_cn：快速给出已有知识和关键缺口。

- depends_on_cn：依赖‘钓鱼严重’的上下文。

- sets_up_cn：引出需要研究保持策略。

- evidence_pointer：Abstract第二句

### 3. Abstract S3

- order：3

- section：Abstract

- locator：Abstract S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：因此研究过度学习作为一种通过重复和自动性提高技能保持的方法。

- rhetorical_function_cn：点明本文研究目标。

- depends_on_cn：依赖‘训练效果衰减’这一限制。

- sets_up_cn：为方法部分做预告。

- evidence_pointer：Abstract第三句

### 4. Abstract S4

- order：4

- section：Abstract

- locator：Abstract S4

- move_code：STUDY_OVERVIEW

- paraphrase_cn：开展纵向实验，将过度学习与规则式、正念式和控制培训交叉。

- rhetorical_function_cn：概括实验设计。

- depends_on_cn：需说明研究对象。

- sets_up_cn：引出结果句。

- evidence_pointer：Abstract第四句

### 5. Abstract S5

- order：5

- section：Abstract

- locator：Abstract S5

- move_code：RESULT

- paraphrase_cn：正念培训比规则式有更好保留，过度学习减少点击且提高谨慎，但并不改变培训方式效应。

- rhetorical_function_cn：给出核心结果。

- depends_on_cn：依赖实验设计句。

- sets_up_cn：支持摘要贡献句。

- evidence_pointer：Abstract第五句

### 6. Abstract S6

- order：6

- section：Abstract

- locator：Abstract S6

- move_code：CONTRIBUTION

- paraphrase_cn：整体结果表明正念培训在长期降低钓鱼易感性上稳定且不增加漏掉合法邮件的风险。

- rhetorical_function_cn：把结果提升为贡献。

- depends_on_cn：依赖结果句。

- sets_up_cn：为正文讨论埋下伏笔。

- evidence_pointer：Abstract最后一句

### 7. Introduction P1 S1-S3

- order：7

- section：Introduction

- locator：Introduction P1 S1-S3

- move_code：PRACTICAL_STAKES

- paraphrase_cn：FBI报告显示钓鱼攻击造成125亿美元损失且增长136%，还会导致信心、声誉、隐私和商业秘密损失。

- rhetorical_function_cn：用权威数据和损失类型说明现实后果。

- depends_on_cn：无。

- sets_up_cn：论证防钓鱼培训的必要性。

- evidence_pointer：Introduction第一段

### 8. Introduction P1 S4-S7

- order：8

- section：Introduction

- locator：Introduction P1 S4-S7

- move_code：PHENOMENON

- paraphrase_cn：攻击者通过模仿合法发件人，在邮件、即时消息等中窃取数据；技术过滤和警告会失效，最终要依靠个人判断。

- rhetorical_function_cn：描述具体经验现象，说明技术防御的边界。

- depends_on_cn：依赖损失数据。

- sets_up_cn：引出用户教育/培训是最后防线。

- evidence_pointer：Introduction第一段后半

### 9. Introduction P2 S1-S2

- order：9

- section：Introduction

- locator：Introduction P2 S1-S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：过去研究表明反钓鱼培训能提高识别能力和降低易感性。

- rhetorical_function_cn：总结已有知识。

- depends_on_cn：为后续限定做铺垫。

- sets_up_cn：紧接着指出‘但效果会衰减’。

- evidence_pointer：Introduction第二段开始

### 10. Introduction P2 S3-S4

- order：10

- section：Introduction

- locator：Introduction P2 S3-S4

- move_code：GAP

- paraphrase_cn：虽然有规则式和正念式培训两种方法，但很少有研究考察超过1个月的保留效果。

- rhetorical_function_cn：指出保留期不足的研究缺口。

- depends_on_cn：依赖已有培训有效的总结。

- sets_up_cn：为引入过度学习提供缺口。

- evidence_pointer：Introduction第二段后半

### 11. Introduction P3 S1

- order：11

- section：Introduction

- locator：Introduction P3 S1

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：由于钓鱼后果严重、培训成本高，必须延长培训的知识和技能保留。

- rhetorical_function_cn：解释缺口为何重要。

- depends_on_cn：依赖先前损失和培训衰减数据。

- sets_up_cn：推出‘保持策略’研究。

- evidence_pointer：Introduction第三段开头

### 12. Introduction P3 S2-S4

- order：12

- section：Introduction

- locator：Introduction P3 S2-S4

- move_code：THEORY_INTRO

- paraphrase_cn：过度学习是在初始掌握后继续练习，通过持续练习和反馈强化长时记忆和例行化技能。

- rhetorical_function_cn：引入核心理论概念。

- depends_on_cn：由保持缺口自然引出。

- sets_up_cn：为假设和设计作理论准备。

- evidence_pointer：Introduction第三段中部

### 13. Introduction P3 S5-S6

- order：13

- section：Introduction

- locator：Introduction P3 S5-S6

- move_code：GAP

- paraphrase_cn：过度学习从未在钓鱼情境中检验，且与不同培训类型结合可能产生不同甚至相反效果。

- rhetorical_function_cn：指出具体未研究问题。

- depends_on_cn：依赖过度学习理论介绍。

- sets_up_cn：提出‘交互是否成立’的问题。

- evidence_pointer：Introduction第三段末尾

### 14. Introduction P4 S1

- order：14

- section：Introduction

- locator：Introduction P4 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：因此本研究扩展Jensen等人的初步研究，纵向考察过度学习与两种培训的差异化效应。

- rhetorical_function_cn：明确研究目标。

- depends_on_cn：依赖缺口梳理。

- sets_up_cn：预告方法。

- evidence_pointer：Introduction第四段开始

### 15. Introduction P4 S2-S4

- order：15

- section：Introduction

- locator：Introduction P4 S2-S4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：采用学生样本、两轮模拟钓鱼邮件和两次邮件识别测验，并测量辨别力和响应偏向。

- rhetorical_function_cn：解释方法选择及其作用。

- depends_on_cn：需要回应研究目标。

- sets_up_cn：为结果部分提供测量框架。

- evidence_pointer：Introduction第四段后半

### 16. Section 1 P1

- order：16

- section：Section 1 Combating phishing attacks

- locator：Section 1 P1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：通常有三种反钓鱼策略：过滤、警告、培训。

- rhetorical_function_cn：建立技术/教育应对分类。

- depends_on_cn：由引言问题自然展开。

- sets_up_cn：为说明培训仍是必要组成。

- evidence_pointer：Section 1开始

### 17. Section 1 P2 S1-S3

- order：17

- section：Section 1 Combating phishing attacks

- locator：Section 1 P2 S1-S3

- move_code：LIMITATION

- paraphrase_cn：自动工具误报率高、攻击者会持续适应，用户即使收到警告也可能进入钓鱼网站。

- rhetorical_function_cn：指出技术防御的局限。

- depends_on_cn：依赖三类策略的框架。

- sets_up_cn：为‘教育用户’的必要性增加论据。

- evidence_pointer：Section 1第二段

### 18. Section 1 P2 final sentence

- order：18

- section：Section 1 Combating phishing attacks

- locator：Section 1 P2 final sentence

- move_code：PRACTICAL_STAKES

- paraphrase_cn：引述Wright和Marett的结论：经验和培训似乎是最有效的防御工具。

- rhetorical_function_cn：用权威结论强化培训价值。

- depends_on_cn：依赖前面对技术局限的讨论。

- sets_up_cn：为规则式/正念式培训综述提供入口。

- evidence_pointer：Section 1末句

### 19. Section 2 P1 S1-S2

- order：19

- section：Section 2 Rule-based training

- locator：Section 2 P1 S1-S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：已有反钓鱼培训总体有效，且多采用规则式方法，教用户应用具体指南和线索。

- rhetorical_function_cn：总结规则式培训现状。

- depends_on_cn：衔接培训价值。

- sets_up_cn：为指出规则式局限作铺垫。

- evidence_pointer：Section 2开头

### 20. Section 2 P1 last sentences

- order：20

- section：Section 2 Rule-based training

- locator：Section 2 P1 last sentences

- move_code：MECHANISM

- paraphrase_cn：规则式培训假定钓鱼线索稳定，但攻击复杂化使规则过时；且依赖简单规则可能促进启发式处理，增加易感性。

- rhetorical_function_cn：提出规则式培训的行为机制缺陷。

- depends_on_cn：依赖规则式培训的定义。

- sets_up_cn：引出正念式培训作为替代。

- evidence_pointer：Section 2末尾

### 21. Section 3 P1

- order：21

- section：Section 3 Mindfulness training

- locator：Section 3 P1

- move_code：THEORY_INTRO

- paraphrase_cn：作为替代，可训练个体使用系统化处理（System2）评估邮件，研究者也建议探索这一方向。

- rhetorical_function_cn：介绍正念式培训的理论来源。

- depends_on_cn：由规则式缺陷自然过渡。

- sets_up_cn：为正念培训提供理由。

- evidence_pointer：Section 3第一段

### 22. Section 3 P2 S1-S3

- order：22

- section：Section 3 Mindfulness training

- locator：Section 3 P2 S1-S3

- move_code：THEORY_INTRO

- paraphrase_cn：正念是对当下经验的注意和觉察，IT正念是用户关注当下、注意细节并愿意探究IT特征和失败。

- rhetorical_function_cn：定义核心构念。

- depends_on_cn：依赖系统化处理概念。

- sets_up_cn：介绍Jensen等人的正念培训步骤。

- evidence_pointer：Section 3第二段开始

### 23. Section 3 P2 last sentences

- order：23

- section：Section 3 Mindfulness training

- locator：Section 3 P2 last sentences

- move_code：RESULT

- paraphrase_cn：Jensen等初步发现正念培训组对模拟钓鱼的响应率为7.5%，规则式组为13.4%。

- rhetorical_function_cn：引用初步证据说明正念培训潜力。

- depends_on_cn：依赖正念培训步骤介绍。

- sets_up_cn：为本文扩展保留检验做铺垫。

- evidence_pointer：Section 3末段

### 24. Section 4 P1

- order：24

- section：Section 4 Skill retention in anti-phishing training

- locator：Section 4 P1

- move_code：LIMITATION

- paraphrase_cn：已有研究只测不到1个月的保留，少数2个月研究只针对规则式，正念培训初步研究也只有10天。

- rhetorical_function_cn：系统指出保留研究缺口。

- depends_on_cn：依赖前两节的培训综述。

- sets_up_cn：引入本文2个月纵向设计。

- evidence_pointer：Section 4第一段

### 25. Section 4 P2

- order：25

- section：Section 4 Skill retention in anti-phishing training

- locator：Section 4 P2

- move_code：GAP

- paraphrase_cn：反钓鱼文献几乎没有开始研究保持策略；需要了解哪些保留策略最适合每种培训。

- rhetorical_function_cn：明确提出研究空白。

- depends_on_cn：依赖保留时间衰减的共识。

- sets_up_cn：引出过度学习。

- evidence_pointer：Section 4第二段

### 26. Section 5 P1 S1-S5

- order：26

- section：Section 5 Overlearning

- locator：Section 5 P1 S1-S5

- move_code：THEORY_PROPOSITION

- paraphrase_cn：过度学习被定义为超过设定标准后继续刻意训练，通过重复强化刺激-反应联结、减少认知需求、增强自动性，并提供更多反馈。

- rhetorical_function_cn：给出核心概念的正式定义和机制。

- depends_on_cn：为弥补保持缺口。

- sets_up_cn：为假设5-7提供理论依据。

- evidence_pointer：Section 5第一段

### 27. Section 5 P2

- order：27

- section：Section 5 Overlearning

- locator：Section 5 P2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：Driskell等人的元分析显示过度学习对保留有中等效应，50%过度学习即可带来改善。

- rhetorical_function_cn：引用实证证据支持其有效性。

- depends_on_cn：依赖过度学习定义。

- sets_up_cn：为100%过度学习的操纵提供依据。

- evidence_pointer：Section 5第二段

### 28. Section 5 P3

- order：28

- section：Section 5 Overlearning

- locator：Section 5 P3

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：过度学习尚未在反钓鱼中检验，且多数研究间隔在4周以内、使用简单实验室任务，因此新情境能同时促进反钓鱼保持和对过度学习本身的理解。

- rhetorical_function_cn：说明在新情境中研究过度学习的理论和实践价值。

- depends_on_cn：依赖元分析结论和现有研究局限。

- sets_up_cn：为假设和设计铺垫双重贡献。

- evidence_pointer：Section 5第三段

### 29. Section 6 P1

- order：29

- section：Section 6 Hypotheses

- locator：Section 6 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：相对Jensen等人的研究，本文增加了多封模拟钓鱼邮件、SDT两个指标和2个月窗。

- rhetorical_function_cn：说明研究如何扩展现有工作。

- depends_on_cn：依赖前面对Jensen等研究的讨论。

- sets_up_cn：为假设和测量方法作铺垫。

- evidence_pointer：Section 6

### 30. Section 7 P1-H2

- order：30

- section：Section 7 Hypotheses: training vs no training

- locator：Section 7 P1-H2

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：假设1和2：接受规则式或正念式培训的人比不接受反钓鱼培训的人有更好辨别力、更谨慎、更不易受攻击。

- rhetorical_function_cn：提出总体训练效应假设。

- depends_on_cn：依赖训练有效的已有文献和机制。

- sets_up_cn：为结果中H1/H2检验做标记。

- evidence_pointer：Section 7末尾

### 31. Section 8 P1-H3

- order：31

- section：Section 8 Hypotheses: mindfulness vs rule-based

- locator：Section 8 P1-H3

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：假设3：正念培训比规则式培训带来更好辨别力、更谨慎、更少易感性。

- rhetorical_function_cn：提出训练方式之间的主要对比假设。

- depends_on_cn：依赖正念机制和Jensen初步结果。

- sets_up_cn：为结果中H3检验做准备。

- evidence_pointer：Section 8

### 32. Section 8 P2-H4

- order：32

- section：Section 8 Hypotheses: retention of training

- locator：Section 8 P2-H4

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：假设4：正念培训通过更深加工，在2个月后比规则式培训有更好辨别力、更谨慎、更少易感性。

- rhetorical_function_cn：提出保持差异假设。

- depends_on_cn：依赖加工深度理论。

- sets_up_cn：为时间2的对比做准备。

- evidence_pointer：Section 8第二段

### 33. Section 9 P1-H5

- order：33

- section：Section 9 Hypotheses: overlearning main effect

- locator：Section 9 P1-H5

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：假设5：接受过度学习的人比不接受者有更好辨别力、更谨慎、更少易感性。

- rhetorical_function_cn：提出过度学习主效应假设。

- depends_on_cn：依赖过度学习理论。

- sets_up_cn：为结果H5做准备。

- evidence_pointer：Section 9

### 34. Section 9 P2-H6

- order：34

- section：Section 9 Hypotheses: overlearning retention

- locator：Section 9 P2-H6

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：假设6：过度学习者在2个月后保持更好，表现为辨别力、谨慎和易感性上的优势。

- rhetorical_function_cn：提出过度学习的保持效应。

- depends_on_cn：依赖过度学习巩固记忆机制。

- sets_up_cn：为时间2交互检验做准备。

- evidence_pointer：Section 9第二段

### 35. Section 10 P1-H7

- order：35

- section：Section 10 Hypotheses: interaction

- locator：Section 10 P1-H7

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：假设7：规则式培训加过度学习在2个月后比正念式培训加过度学习有更好保持。

- rhetorical_function_cn：提出具体的训练×过度学习交互假设。

- depends_on_cn：依赖自动性与刻意注意目标冲突的推理。

- sets_up_cn：为结果中H7检验做准备。

- evidence_pointer：Section 10

### 36. Section 11.1 Participants

- order：36

- section：Method: Participants

- locator：Section 11.1 Participants

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：使用西南大学本科生样本，因这年龄段与钓鱼相关且易感；最终样本453人。

- rhetorical_function_cn：为样本选择提供理由。

- depends_on_cn：需要说明实验对象。

- sets_up_cn：为统计功效和外部效度讨论准备。

- evidence_pointer：Section 11.1

### 37. Section 12 P1-P2

- order：37

- section：Method: General procedures

- locator：Section 12 P1-P2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：参与者先参加1小时培训、填写协变量、接受三类培训之一、完成练习（6或12封）、填充任务、第一次邮件识别测验，之后在第1周和第8周收到模拟钓鱼邮件，并在第10周完成第二次识别测验。

- rhetorical_function_cn：完整交代实验流程。

- depends_on_cn：依赖随机分配和处理条件的设定。

- sets_up_cn：为结果分析中的时间维度提供结构。

- evidence_pointer：Figure 1和Section 12

### 38. Section 13 P1-P2

- order：38

- section：Method: Training conditions

- locator：Section 13 P1-P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：规则式培训包含六条建议，正念式培训包含停止、思考、核验三步，控制组接受密码管理培训。

- rhetorical_function_cn：具体描述培训操纵。

- depends_on_cn：依赖Jensen等材料和反钓鱼指南。

- sets_up_cn：为结果条件差异提供操作定义。

- evidence_pointer：Section 13

### 39. Section 14 P1-P2

- order：39

- section：Method: Overlearning conditions

- locator：Section 14 P1-P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：无过度学习只练习6封邮件，100%过度学习额外练习6封共12封；所有练习都有逐封反馈。

- rhetorical_function_cn：定义过度学习操纵的具体实现。

- depends_on_cn：依赖过度学习理论和先前任务经验。

- sets_up_cn：为后续补充分析中的‘是否达到初始学习’提供标准。

- evidence_pointer：Section 14

### 40. Section 15 P1-P3

- order：40

- section：Method: Learning measures

- locator：Section 15 P1-P3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：邮件识别测验用命中率和误报率计算d'和c，以区分辨别力和谨慎偏向。

- rhetorical_function_cn：说明测量工具的理论依据。

- depends_on_cn：依赖Signal Detection Theory。

- sets_up_cn：为结果中的双因变量分析做准备。

- evidence_pointer：Section 15

### 41. Section 15 P4-P5

- order：41

- section：Method: Mock phishing tests

- locator：Section 15 P4-P5

- move_code：DESIGN_FEATURE

- paraphrase_cn：模拟钓鱼测试使用Wombat ThreatSim向真实邮箱发送5封钓鱼邮件，根据点击数计分。

- rhetorical_function_cn：描述真实环境迁移测量。

- depends_on_cn：需要IT部门和IRB支持。

- sets_up_cn：为迁移到日常行为的结论提供证据基础。

- evidence_pointer：Section 15后半

### 42. Section 16

- order：42

- section：Method: Covariates

- locator：Section 16

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：纳入信任倾向、技术正念、感知网络风险、计算机自我效能、钓鱼识别专长、邮件经验、训练前动机和大五人格等协变量。

- rhetorical_function_cn：控制个体差异和先前经验。

- depends_on_cn：基于Wright和Marett的研究。

- sets_up_cn：为ANCOVA模型提供统计控制。

- evidence_pointer：Section 16

### 43. Results P1

- order：43

- section：Results

- locator：Results P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：对三个因变量分别执行3(培训)×2(过度学习)×2(时间)混合设计ANCOVA。

- rhetorical_function_cn：交代统计分析模型。

- depends_on_cn：依赖多维因变量和重复测量设计。

- sets_up_cn：统一结果报告结构。

- evidence_pointer：Results第一段

### 44. Results H1 section

- order：44

- section：Results: Main effects of training

- locator：Results H1 section

- move_code：RESULT

- paraphrase_cn：规则式培训在辨别力、谨慎和模拟点击上与无培训控制组无显著差异，H1a/b/c均不支持。

- rhetorical_function_cn：报告第一个假设结果。

- depends_on_cn：依赖ANCOVA计划比较。

- sets_up_cn：对比正念培训效果。

- evidence_pointer：Section 18

### 45. Results H2 section

- order：45

- section：Results: Main effects of training

- locator：Results H2 section

- move_code：RESULT

- paraphrase_cn：正念培训在辨别力和模拟点击上优于控制组，但在谨慎上不显著，H2a和H2c支持、H2b不支持。

- rhetorical_function_cn：报告正念相比无培训的效果。

- depends_on_cn：依赖计划比较。

- sets_up_cn：为与规则式对比提供基础。

- evidence_pointer：Section 18

### 46. Results H3 section

- order：46

- section：Results: Main effects of training

- locator：Results H3 section

- move_code：RESULT

- paraphrase_cn：正念培训在辨别力和模拟点击上优于规则式培训，但在谨慎上无差异，H3a和H3c支持、H3b不支持。

- rhetorical_function_cn：报告正念与规则式直接比较。

- depends_on_cn：需要前述正念和控制对比。

- sets_up_cn：引出保持期对比。

- evidence_pointer：Section 18

### 47. Results H4 section

- order：47

- section：Results: Effects of training on retention

- locator：Results H4 section

- move_code：RESULT

- paraphrase_cn：2个月后，正念在辨别力上仍高于规则式和控制组，模拟点击得分高于规则式，但谨慎差异消失，H4a/H4c支持、H4b不支持。

- rhetorical_function_cn：报告训练保持效果。

- depends_on_cn：依赖Time2数据和训练×时间交互。

- sets_up_cn：说明正念优势的持久性。

- evidence_pointer：Section 19和Figures 2-4

### 48. Results H5 section

- order：48

- section：Results: Main effect of overlearning

- locator：Results H5 section

- move_code：RESULT

- paraphrase_cn：过度学习没有提高辨别力，但显著增加了谨慎并提高了模拟钓鱼得分，因此H5a不支持、H5b/H5c支持。

- rhetorical_function_cn：报告过度学习主效应。

- depends_on_cn：依赖ANCOVA主效应检验。

- sets_up_cn：引出过度学习对保持的分析。

- evidence_pointer：Section 20

### 49. Results H6 section

- order：49

- section：Results: Effect of overlearning on retention

- locator：Results H6 section

- move_code：RESULT

- paraphrase_cn：过度学习与时间的交互不显著，2个月后过度学习与无过度学习无差异，H6a/b/c均不支持。

- rhetorical_function_cn：否定过度学习作为保持策略的假设。

- depends_on_cn：依赖时间2计划比较。

- sets_up_cn：为讨论‘过度学习作用有限’提供证据。

- evidence_pointer：Section 21和Figures 5-7

### 50. Results H7 section

- order：50

- section：Results: Training method and overlearning on retention

- locator：Results H7 section

- move_code：RESULT

- paraphrase_cn：训练、过度学习与时间的交互不显著，训练和过度学习在T2也无交互，H7a/b/c均不支持。

- rhetorical_function_cn：检验训练与过度学习的组合效应。

- depends_on_cn：依赖三维交互检验。

- sets_up_cn：引出补充分析中对条件特异性收益的探索。

- evidence_pointer：Section 22

### 51. Section 23

- order：51

- section：Results: Supplemental analyses

- locator：Section 23

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：排除未达到初始学习标准的参与者后总体模式相似，但过度学习对c和模拟得分主效应不再显著；成对比较显示规则式+过度学习总体收益最大，正念+过度学习对T2保持更有利。

- rhetorical_function_cn：检验过度学习操作化的稳健性和条件特异性。

- depends_on_cn：依赖原样本结果。

- sets_up_cn：为讨论中‘过度学习并非无用但边界条件’提供证据。

- evidence_pointer：Section 23和附录J-L

### 52. Discussion P1

- order：52

- section：Discussion

- locator：Discussion P1

- move_code：CONTRIBUTION

- paraphrase_cn：本研究扩展了Jensen等人的工作，比较更长的保留间隔和两种技能保持测试。

- rhetorical_function_cn：回扣引言，声明研究的继承与增量。

- depends_on_cn：依赖整个实验结果。

- sets_up_cn：开启六点理论含义。

- evidence_pointer：Discussion第一段

### 53. Theoretical implication 1

- order：53

- section：Discussion: Theoretical implications

- locator：Theoretical implication 1

- move_code：MECHANISM

- paraphrase_cn：正念培训导致更好辨别力和更低点击率，且不增加误报，说明其帮助人们平衡地处理邮件。

- rhetorical_function_cn：用结果解释机制并提升贡献。

- depends_on_cn：依赖d'和误报率数据。

- sets_up_cn：引出‘不应只看谨慎，应看平衡’的理论观点。

- evidence_pointer：Discussion第二段

### 54. Theoretical implication 2

- order：54

- section：Discussion: Theoretical implications

- locator：Theoretical implication 2

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：规则式培训不优于控制组，可能是因为重复规则导致自满或脱敏；控制组也可能通过练习和反馈学到了相似内容。

- rhetorical_function_cn：解释规则式无效的边界和潜在混淆。

- depends_on_cn：依赖规则式结果和对照组设置。

- sets_up_cn：为未来研究组合培训提供理由。

- evidence_pointer：Discussion第三段

### 55. Theoretical implication 3

- order：55

- section：Discussion: Theoretical implications

- locator：Theoretical implication 3

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：过度学习提高了谨慎和降低了点击，但未提高辨别力，因此可能让用户过度标记邮件为钓鱼，进而影响生产力。

- rhetorical_function_cn：指出过度学习的价值与风险并存。

- depends_on_cn：依赖过度学习在d'和c上的分离结果。

- sets_up_cn：引出设计上应配合辨别力训练。

- evidence_pointer：Discussion第四段

### 56. Theoretical implication 4

- order：56

- section：Discussion: Theoretical implications

- locator：Theoretical implication 4

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：训练方法与过度学习无交互，说明过度学习并不损害正念或规则式培训，但也没有增强任何特定的保持效果。

- rhetorical_function_cn：回应H7，说明交互缺失的理论意义。

- depends_on_cn：依赖三维交互不显著的结果。

- sets_up_cn：为继续推荐正念培训提供依据。

- evidence_pointer：Discussion第五段

### 57. Theoretical implication 5

- order：57

- section：Discussion: Theoretical implications

- locator：Theoretical implication 5

- move_code：CONTRIBUTION

- paraphrase_cn：研究增进了对IT正念的理解，表明正念培训能以低成本、易实施的方式提高与钓鱼相关的IT正念并产生持续效果。

- rhetorical_function_cn：把结果上升为对IT正念理论的贡献。

- depends_on_cn：依赖正念培训长期优势结果。

- sets_up_cn：为未来反钓鱼研究提供新方向。

- evidence_pointer：Discussion第六段

### 58. Theoretical implication 6

- order：58

- section：Discussion: Theoretical implications

- locator：Theoretical implication 6

- move_code：CONTRIBUTION

- paraphrase_cn：本研究将过度学习研究扩展到真实世界任务、长保留间隔和两种培训类型，弥补了以往实验室短期间隔的局限。

- rhetorical_function_cn：声明对overlearning文献的方法论贡献。

- depends_on_cn：依赖过度学习研究综述和本实验结果。

- sets_up_cn：为实践建议做铺垫。

- evidence_pointer：Discussion第七段

### 59. Practical implications P1-P3

- order：59

- section：Discussion: Practical implications

- locator：Practical implications P1-P3

- move_code：PRACTICAL_STAKES

- paraphrase_cn：组织可用简单幻灯片和反馈练习快速实施培训，但培训不能消除所有钓鱼点击，应作为分层防御的一部分。

- rhetorical_function_cn：把结果转化为可操作建议并提醒局限。

- depends_on_cn：依赖培训材料易实施和点击率未归零的数据。

- sets_up_cn：为限制与未来研究背景化。

- evidence_pointer：Section 26

### 60. Section 27

- order：60

- section：Discussion: Limitations and future research

- locator：Section 27

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：没有前测、两轮模拟钓鱼可能影响后续谨慎、未检验组合培训、过度学习量可能非最优、控制组也接受了练习反馈、只测链接点击。

- rhetorical_function_cn：系统列出方法限制并提出未来方向。

- depends_on_cn：依赖设计选择。

- sets_up_cn：为结论提供谦逊边界。

- evidence_pointer：Section 27

### 61. Section 28

- order：61

- section：Conclusion

- locator：Section 28

- move_code：CONTRIBUTION

- paraphrase_cn：总结：正念培训优于规则式，正念优势在2个月后仍存在；过度学习仅提高谨慎和降低点击，且不妨碍正念效果；应优先训练人们暂停、批判性评估和向第三方核验。

- rhetorical_function_cn：给出最终立场和可操作结论。

- depends_on_cn：依赖全部结果和讨论。

- sets_up_cn：结束全文，回扣标题‘Learning not to take the bait’。

- evidence_pointer：Section 28

## 写作技术

- gap_construction_cn：先承认已有培训有效，再用‘但效果随时间衰减’制造张力；随后指出已有保持研究少于1个月且只考察规则式，把缺口收窄到‘反钓鱼培训的保持策略未被研究’；最后将过度学习从未被应用于钓鱼场景和可能产生反效果两面来塑造研究问题。

- signposting_cn：摘要和引言给结论预告；方法用Figure 1完整展示流程；假设部分按H1-H7逐条给出，并在假设后附‘Thus, the following hypothesis was examined’；结果按主效应、保持、交互、补充分析分节；Table 1汇总所有假设支持情况，方便读者追踪。

- transition_logic_cn：各理论章节以‘Although... it is unclear...’为过渡；方法部分从参与者到程序到材料再到协变量逐步展开；结果部分先主效应后时间交互再到过度学习交互；讨论部分用编号的理论含义逐一解释发现。

- claim_evidence_rhythm_cn：每个假设都先陈述理论推导，再在结果中给出统计量、p值和eta²，然后用计划比较解释支持与否；对不支持的假设直接说明相等关系；最后在讨论中把‘不支持’转化为边界条件或理论教训。

- benchmark_narrative_cn：控制训练既是‘未接受反钓鱼培训’的基线，又因为练习反馈使基线变强，成为讨论中一个有意思的对照；规则式培训作为已有方法基准，正念式作为新方法；过度学习条件作为策略比较。

- theory_return_cn：讨论回到正念、规则式浅层加工、过度学习自动性和技能衰减理论，用结果修正这些理论的适用范围，如指明过度学习提升谨慎而非辨别，以及正念的优势不因过度学习而改变。

- contribution_positioning_cn：从‘扩展Jensen et al.初步研究’开始，自我定位为‘增加严格指标、更多模拟邮件、更长保留间隔’；并把自己放入overlearning研究的方法论缺口（实验室任务、短期间隔）中以提升新意。

- novelty_protection_cn：不把结果表达为‘某个训练在某个测试上更好’，而是同时报告d'、c和真实点击，说明正念影响了能力而不牺牲误报，过度学习影响偏向而非能力；通过无交互的发现排除‘加量即可’的简单解释，从而把贡献提升为设计知识和理论边界。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：用成本数据和攻击案例建立问题紧迫性；综述三类防御并指出技术防御局限。

- research_job_cn：收集权威统计和已有反钓鱼研究，说明个体判断是最后防线。

- required_evidence_cn：损失金额、攻击趋势、技术工具误报率/绕过证据。

- transition_to_next_cn：从‘技术不完美’自然导向‘需要培训’。

#### 2. 2

- step：2

- writing_job_cn：总结已有反钓鱼培训有效，但立即指出保留期短、规则式为主。

- research_job_cn：系统梳理培训保留研究，标出保留间隔和培训类型。

- required_evidence_cn：至少若干篇使用短保留期的实证研究，最好有1个月内衰减证据。

- transition_to_next_cn：引出‘需要保持策略’空白。

#### 3. 3

- step：3

- writing_job_cn：引入过度学习概念、定义和元分析证据；说明其机制和潜在反效果。

- research_job_cn：理解过度学习在技能保持中的理论；确认未被应用到钓鱼。

- required_evidence_cn：Driskell等元分析以及适用任务类型综述。

- transition_to_next_cn：提出‘过度学习×培训类型’可能交互的研究问题。

#### 4. 4

- step：4

- writing_job_cn：将研究问题转化为可检验假设，每个假设分三个依赖变量。

- research_job_cn：确定自变量（培训、过度学习）和因变量（辨别力、偏向、点击），并给出理论依据。

- required_evidence_cn：概念定义和已有初步证据。

- transition_to_next_cn：引导到‘如何测量’。

#### 5. 5

- step：5

- writing_job_cn：详述实验设计、材料、操纵和预测试；用图和表预告流程。

- research_job_cn：准备培训材料、开发邮件集、做预测试、确定过度学习量、申请IRB。

- required_evidence_cn：材料难度相等、操纵有效、样本量。

- transition_to_next_cn：进入数据收集。

#### 6. 6

- step：6

- writing_job_cn：按假设顺序报告ANCOVA主效应、时间交互和计划比较。

- research_job_cn：运行统计模型，处理协变量，检验假设。

- required_evidence_cn：F、p、eta²、校正均值。

- transition_to_next_cn：对不支持的假设要在讨论中解释。

#### 7. 7

- step：7

- writing_job_cn：用补充分析和成对比较检验操作化稳健性，并揭示条件特异性。

- research_job_cn：排除未达标学习者重跑模型；进行条件成对比较。

- required_evidence_cn：亚组模式是否一致；事后比较结果。

- transition_to_next_cn：为边界条件提供证据。

#### 8. 8

- step：8

- writing_job_cn：把结果重述为对理论和实践的意义，列出限制。

- research_job_cn：将‘不支持’结果重新解释为边界条件，与引言缺口呼应。

- required_evidence_cn：结果模式与理论机制的一致性，限制清单。

- transition_to_next_cn：结束闭环。

### most_transferable_moves_cn

1. 用现实损失数据开头

2. 用多个因变量拆解能力/偏向

3. 在实验室测验之外加入真实邮箱模拟

4. 用计划比较处理多个假设

5. 把null结果写成边界条件

6. 引入一个未在目标领域使用的成熟保留策略（overlearning）

### resource_intensive_or_nonstandard_parts_cn

1. 真实邮箱模拟钓鱼需要大学IT配合、IRB、Wombat ThreatSim或类似平台

2. 两轮8周实验周期较长

3. 材料开发与预测试耗时

4. 需购买并控制仿冒域名

### what_not_to_copy_superficially_cn

1. 不能在没有真正设计正念培训内容（stop/think/check）的情况下声称正念培训有效

2. 不能在没有纵向模拟钓鱼数据情况下宣称‘保持’

3. 不能在没有SDT指标的情况下讨论误报

4. 不能使用控制组也接受练习的设计并把‘不培训’说成纯净基线

- single_best_description_of_the_routine_cn：把‘反钓鱼训练会衰减’这一性能缺口转化为训练方法×保持策略的2×2×2纵向实验，用SDT拆开能力与倾向，再用真实邮箱点击验证迁移，最后用交互不显著和补充分析把结论从‘哪个更好’提升为‘何种机制在何时有效’。

## 分析边界

文章全文已提供，但未提供附录A-L的实际内容，只能依据正文描述推断；无精确页码，位置以章节和小节为准；部分表格OCR可能有数字缺漏，但不影响整体结构和论证动作判断。
