# Peer Effects in Competitive Environments: Field Experiments on Information Provision and Interventions

- 作者：Zhuoxin Li; Gang Wang; Harry Jiannan Wang
- 年份 / 期刊：2021 / MIS Quarterly
- DOI：10.25300/misq/2021/16085
- 源文件：01638_2021_peer-effects-in-competitive-environments-field-experiments-on-information-provision-and-interven.md
- 论文主类型：field_intervention_or_platform_experiment
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.87

## 文章级论证概况

- 核心问题：在存在竞争性评分或排名情境的在线学习管理系统中，提供描述性同伴信息能否减少拖延并提高成绩？该效应受哪些个人和情境因素调节，背后的机制是从众还是社会比较？

- 制品与设计：一个自动读取Canvas系统日志的插件程序：计算参考组中已开始作业的学生百分比，识别未开始作业的学生，随机分配纯提醒或提醒+同伴信息，并通过邮件和站内通知发送；后续通过Study III操纵排名/非排名评分，Study IV操纵21%/41%/61%的同伴行为流行度。

- 客观结果：行为上，男性在多种条件下显著提前开始作业（Study I约9小时；Study II男性占多数小组12.03小时；Study III排名条件17.73小时），女性未显著；成绩上，合并三研究的处理效应为提高4.13分，男性子样本6.54分；男性行为改善的中介效应0.92显著。

- 核心贡献：将同伴信息干预研究从非竞争情境扩展到竞争性课堂情境，发现性别响应方向发生翻转（男性更受社会比较激发），并识别出性别构成、过去行为与成绩、同伴行为流行度的调节作用；同时建立行为改善对成绩提升的中介链，为定向干预提供设计含义。

- 整篇论证链：文章以LMS日志和大学生拖延问题为起点，指出现有社会规范干预的证据几乎都来自非竞争环境，而课堂排名政策等竞争环境中的效果未知。作者开发了一个Canvas插件，自动计算未开始作业比例并向学生发送纯提醒或含同伴信息的提醒。通过四个随机现场实验，依次检验section级、group级同伴信息、竞争性评分和流行度操纵，发现同伴信息总体降低拖延并提高成绩，但效应集中体现在男性、男性占多数环境以及过去行为/成绩较差的学生身上。中介分析表明，提前开始行为解释了男性成绩提升。讨论部分用社会比较而非社会从众来解释性别翻转，并把干预定位为需要按性别、性别构成和行为轨迹进行定向设计的数字干预。

## 类型与写作弧线判定

- 论文主类型判定：论文不是在实验室构造理论制品进行单一实验，而是在真实LMS平台上部署可自动运行的Canvas插件，通过多个随机化现场实验操纵同伴信息、参照群体、竞争性评分和流行度水平，测量真实学生的行为与成绩。设计科学语言（build-evaluate）服务于现场实验证据。

- 主导写作弧线判定：文章按照‘现实问题（拖延与竞争性课堂）→文献缺口（竞争环境未知）→理论与假设→设计与部署干预→多Study现场检验→讨论返回社会比较理论’展开。每个Study是累积的理论检验，而非单纯benchmark比较。

## 研究开展程序

- study_or_phase_count：7

- 研究阶段总序列：先开发程序并验证行为度量；Study I用标准section级设计建立基线并发现性别调节；Study II引入随机小组产生外生性别构成变异；Study III在作业层面操纵竞争性评分，直接检验竞争机制；Study IV外生操纵同伴行为流行度，区分从众与社会比较；随后用中介分析把行为改善连到成绩提升；最后用随机化、串通调查和纯提醒对照等稳健性检验保护因果解释。

### studies_or_phases

#### 1. 制品构建与测量基础

- order：1

- name_cn：制品构建与测量基础

- question_cn：能否构建一个自动从LMS系统日志提取学生进度、计算参考组统计量并按条件发送提醒和同伴信息的程序，并确认行为度量有效？

- inputs_and_setting_cn：Canvas系统日志、课程学生记录；用于验证拖延度量的自报拖延问卷（主要来自Study III的约60%学生）。

- designed_or_compared_object_cn：Canvas插件/计算机程序：自动取数、计算参考组百分比、随机分组、发送邮件与站内通知；以下载数据文件作为开始作业事件。

- baseline_control_or_counterfactual_cn：无实验对照；测量效度以自报拖延量表为外部参照。

##### objective_metrics

1. 程序能否按计划运行

2. StartTime与自报拖延倾向的相关性

3. 回归中StartTime对自报拖延的预测系数

- analysis_method_cn：描述性相关与回归；主成分分析提取自报拖延因子。

- main_result_cn：程序能够自动计算并发送信息；StartTime与自报拖延倾向显著负相关（r=-0.35，p<0.001），说明该行为指标有效。

- argumentative_role_cn：为后续所有现场实验提供可操作平台和客观结果度量，使行为与成绩的因果检验成为可能。

- remaining_uncertainty_cn：程序在真实课堂中是否能引起行为变化，以及何种条件下变化最大，尚未确定。

- link_to_next_phase_cn：通过一个标准设计（Study I）启动行为效果检验。

##### evidence_pointers

1. Research Method: Experimental Setting

2. Appendix F

3. Table F1

#### 2. Study I：Section级同伴信息

- order：2

- name_cn：Study I：Section级同伴信息

- question_cn：在排名制评分的课堂中，以全班为参照的同伴信息能否减少拖延，效应是否因性别和性别构成而异？

- inputs_and_setting_cn：2门商科分析课程、6个section、446名注册学生；进入分析的样本为256人；Canvas日志记录下载与成绩。

- designed_or_compared_object_cn：在同一section内随机分配：对照组收到纯提醒，处理组收到提醒+全班开始作业百分比。

- baseline_control_or_counterfactual_cn：纯提醒消息作为对照组；不使用同伴信息。

##### objective_metrics

1. StartTime

2. Grade

3. Treatment×Male交互项

- analysis_method_cn：可视化、OLS回归、section固定效应、按性别和section男比例分组的子样本分析。

- main_result_cn：全样本主效应不显著（H1a未获支持）；男性处理效应约9小时且显著，女性为负但不显著（H2a支持）；按班级男比例三分组显示男性占主导时效应更强，为H2b提供初步证据。

- argumentative_role_cn：用文献中的标准设计建立基线效果，并首次揭示性别调节。

- remaining_uncertainty_cn：性别构成在section内没有变异，无法对性别构成进行因果识别；可能有跨section混杂因素。

- link_to_next_phase_cn：Study II用随机小组产生外生的性别构成变异，从而正式检验H2b。

##### evidence_pointers

1. Table 1

2. Table 2

3. Figure 1

4. Figure 2

5. Figure 3

6. Table 6

7. Table A1

#### 3. Study II：Group级同伴信息与性别构成

- order：3

- name_cn：Study II：Group级同伴信息与性别构成

- question_cn：用随机小组作为参照群体时，同伴信息效应是否在男性占多数的小组中更强？

- inputs_and_setting_cn：2门课程、4个section、39个4-6人随机小组、199名学生；分析样本含134名受试者。

- designed_or_compared_object_cn：学期初随机分组；在section内随机分配控制/处理；处理消息使用小组开始百分比作为同伴信息。

- baseline_control_or_counterfactual_cn：纯提醒控制；非男性占多数小组作为男性占多数小组的对照。

##### objective_metrics

1. StartTime

2. Treatment×Male_majority交互项

3. 分性别分组的处理系数

- analysis_method_cn：OLS子样本回归；合并Study II和Study III的增长样本检验交互。

- main_result_cn：男生在男性占多数小组中显著提前12.03小时；女性无显著效应；合并Study II与III后，男性占多数小组的处理效应显著强于非男性占多数小组（19.70，p=0.06），H2b得到边缘支持。

- argumentative_role_cn：将性别构成变成可随机变化的实验因素，使情境调节有更强的因果解释力。

- remaining_uncertainty_cn：尚未直接操纵竞争强度；性别构成的拟制仍可能是通过其他同伴互动渠道起作用的。

- link_to_next_phase_cn：Study III通过排名与非排名评分操纵竞争环境，检验竞争机制本身。

##### evidence_pointers

1. Table 1

2. Table 3

3. Table 7

4. Table B1

5. Table B2

6. Table A2

#### 4. Study III：操纵竞争性评分

- order：4

- name_cn：Study III：操纵竞争性评分

- question_cn：在最终成绩不按排名确定的课程中，仅对实验作业设置排名评分是否会改变同伴信息效应？性别差异是否只在排名条件下出现？

- inputs_and_setting_cn：1门商科分析课程、11个section；排名条件116人，非排名条件102人。

- designed_or_compared_object_cn：随机分配排名评分和非排名评分条件；每个条件下再设置无消息、纯提醒、提醒+小组同伴信息。

- baseline_control_or_counterfactual_cn：非排名评分作为排名条件的对照；无消息和纯提醒作为同伴信息处理的对比例子。

##### objective_metrics

1. StartTime

2. Treatment×Male交互项

3. 纯提醒与无消息的StartTime差异

- analysis_method_cn：OLS回归、分性别子样本、与无消息组比较。

- main_result_cn：排名条件下男性处理效应17.73且显著、女性不显著，Treatment×Male显著；非排名条件下性别差异不显著；纯提醒与无消息相比无显著效果。

- argumentative_role_cn：直接检验竞争机制，并排除纯提醒作为替代解释。

- remaining_uncertainty_cn：消息中的百分比X仍取决于干预时机，不是完全外生；没有直接测量被试感知到的竞争强度。

- link_to_next_phase_cn：Study IV通过操纵流行度进一步检验从众与社会比较的区别。

##### evidence_pointers

1. Table 1

2. Table 4

3. Table 8

4. Table D1

5. Figure 6

6. Table A3

#### 5. Study IV：操纵同伴行为流行度

- order：5

- name_cn：Study IV：操纵同伴行为流行度

- question_cn：同伴行为流行度（低/中/高）是否调节干预效果？女性是否只在高度流行时响应，男性是否即使低度流行也响应？

- inputs_and_setting_cn：单班270名学生；消息发送时未开始作业的228人被随机分配；分析样本217人。

- designed_or_compared_object_cn：随机分为控制组（纯提醒）和三个处理组，处理消息分别显示21%、41%、61%的同学已开始。

- baseline_control_or_counterfactual_cn：纯提醒控制组；三个流行度水平互相作为对照。

##### objective_metrics

1. StartTime

2. Treatment1/2/3系数

3. 性别×流行度的差异

- analysis_method_cn：OLS回归、分性别回归、随机化检验。

- main_result_cn：男性对21%低流行度已有显著反应（9.64，p=0.09），中高流行度效应更强；女性在各流行度均不显著，低流行度呈现负趋势但不显著。

- argumentative_role_cn：支持竞争/社会比较解释：男性在低流行度时仍被激发‘抢先’，而从众机制无法解释该模式。

- remaining_uncertainty_cn：Study IV来自单一班级，样本较小，且没有检查对成绩的影响；长期效应未知。

- link_to_next_phase_cn：作为稳健性和机制补充，为讨论中的社会比较理论提供直接实验证据。

##### evidence_pointers

1. Additional Analyses: Effect of the Prevalence of Peer Behavior

2. Figure 5

3. Table C3

4. Table C4

5. Table C5

#### 6. 中介分析：行为改善与成绩提升

- order：6

- name_cn：中介分析：行为改善与成绩提升

- question_cn：同伴信息导致的提前开始作业是否中介了成绩提升？对男性和女性是否一致？

- inputs_and_setting_cn：合并Study I-III的608个观测；分为男362人、女246人。

- designed_or_compared_object_cn：使用Zhao等（2010）两步法：Treatment→StartTime，Treatment与StartTime→Grade，并用10,000次Bootstrap检验中介。

- baseline_control_or_counterfactual_cn：女性作为对照；无中介模型作为比较。

##### objective_metrics

1. Treatment对StartTime的效应

2. StartTime对Grade的效应

3. 中介效应大小及其显著性

- analysis_method_cn：两步回归、Bootstrap中介检验。

- main_result_cn：男性中Treatment对StartTime为10.23，StartTime对Grade为0.09，中介效应0.92且Bootstrap显著；女性没有显著中介。

- argumentative_role_cn：把行为结果和成绩结果连成一条因果链：干预通过减少拖延来提升成绩，从而支撑机制主张。

- remaining_uncertainty_cn：中介分析基于观测数据，仍可能遗漏其他同时影响行为和成绩的变量；没有对女性中介缺失做进一步解释。

- link_to_next_phase_cn：为讨论中的理论贡献提供明确的中介证据。

##### evidence_pointers

1. Mediating Role of Behavior Change

2. Table 10

#### 7. 稳健性与边界检验

- order：7

- name_cn：稳健性与边界检验

- question_cn：主结果是否受随机化失败、学生串通、纯提醒效应或测量效度威胁？

- inputs_and_setting_cn：Study II和III事后串通调查；Study III无消息/提醒比较；附录A、C、F中的问卷和日志数据。

- designed_or_compared_object_cn：随机化检验；排除可能串通者后重新估计；比较纯提醒与无消息；用自报拖延量表验证StartTime。

- baseline_control_or_counterfactual_cn：完整样本结果作为基准；无消息条件作为纯提醒的对照。

##### objective_metrics

1. 随机化检验p值

2. 排除串通后的系数稳定性

3. 串通比例

4. StartTime与自报拖延的相关性

- analysis_method_cn：回归、相关分析、子样本稳健性检验。

- main_result_cn：各Study随机化通过；串通概率约6%-8%，排除后结果一致；纯提醒无显著效果；StartTime有效。

- argumentative_role_cn：保护因果解释，确保效果来自同伴信息而非提醒本身或被试间污染。

- remaining_uncertainty_cn：串通调查回复率约60%，可能存在未观测的选择偏差；无法完全排除其他信息扩散渠道。

- link_to_next_phase_cn：加固了讨论部分从‘有效’到‘何时有效、为何有效’的理论结论。

##### evidence_pointers

1. Appendix A

2. Table D1

3. Figure 6

4. Appendix F

5. Table F2

6. Table F3

7. Table C2

8. Table C5

## 各部分修辞架构

### abstract_moves

1. CONTEXT

2. RQ_OR_OBJECTIVE

3. RESULT

4. MECHANISM

5. LIMITATION

6. CONTRIBUTION

### introduction_moves

1. CONTEXT

2. PRACTICAL_STAKES

3. PHENOMENON

4. PRIOR_KNOWLEDGE

5. GAP

6. RQ_OR_OBJECTIVE

7. DESIGN_FEATURE

8. MECHANISM

9. STUDY_OVERVIEW

10. METHOD_JUSTIFICATION

11. RESULT

12. THEORY_PROPOSITION

13. CONTRIBUTION

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE

2. LIMITATION

3. GAP

4. MECHANISM

5. THEORY_PROPOSITION

6. HYPOTHESIS_OR_PROPOSITION

### artifact_design_moves

1. REQUIREMENT

2. DESIGN_FEATURE

3. STUDY_OVERVIEW

4. METHOD_JUSTIFICATION

5. BENCHMARK_OR_CONTRAST

### evaluation_moves

1. RESULT

2. TRANSITION

3. METHOD_JUSTIFICATION

4. ROBUSTNESS_OR_BOUNDARY_TEST

### discussion_and_contribution_moves

1. MECHANISM

2. CONTRIBUTION

3. BOUNDARY_CONDITION

4. PRACTICAL_STAKES

5. LIMITATION_AND_FUTURE

## 理论/知识到设计的翻译

### 知识/理论基础

1. 社会规范与从众理论（Cialdini and Goldstein 2004）

2. 社会比较与竞争心理（Garcia et al. 2013）

3. 性别差异与竞争偏好（Gneezy et al. 2003）

4. 拖延行为与自我调节文献

5. LMS日志行为测量文献

- 理论—设计耦合：partial

- 耦合判定理由：理论决定了要研究的调节变量、竞争性评分操纵和流行度操纵，但核心同伴信息干预本身来自社会规范文献的成熟做法；LMS插件实现主要由系统日志可用性和工程启发式决定，因此是部分耦合。

- 理论到设计翻译链：知识命题：非竞争环境中社会规范通过从众改变行为；竞争环境可能激活社会比较与竞争偏好 → 设计选择：在LMS中嵌入描述性同伴信息，并通过实验操纵参照群体、竞争性评分和同伴行为流行度 → 检验：随机化现场实验比较有无同伴信息、排名与非排名、不同性别构成和不同流行度 → 结果：男性的行为与成绩改善，女性不显著；排名和男性多数环境增强效应；行为改善中介成绩提升。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：描述性社会规范信息在非竞争环境中通过从众改变行为。

- mechanism_cn：个体依据同伴行为调整自己的行为以符合规范。

- design_requirement_cn：向学生披露参考群体中已开始作业的比例。

- artifact_choice_cn：处理消息：“作业三天后截止。X%的同学已经开始做作业。”

- evaluated_contrast_cn：纯提醒 vs 提醒+同伴信息（Study I-II）。

- objective_result_cn：全样本主效应在Study I中不显著；性别交互显著。

##### evidence_pointers

1. Table 2

2. Table 3

3. Table 6

#### 2. 2

- theory_or_knowledge_claim_cn：竞争环境会激活社会比较，男性更偏好竞争、女性更社会定向。

- mechanism_cn：同伴信息增强环境竞争感，个体希望获得优于他人的位置。

- design_requirement_cn：需要产生竞争强度差异和性别构成差异。

- artifact_choice_cn：Study III对实验作业采用排名评分 vs 非排名评分；Study II随机分组产生不同男比例。

- evaluated_contrast_cn：排名 vs 非排名；男性占多数小组 vs 非男性占多数小组。

- objective_result_cn：排名条件下男性反应显著、女性无；非排名条件下性别差异消失；男性占多数小组显著提前。

##### evidence_pointers

1. Table 7

2. Table 8

3. Table B2

#### 3. 3

- theory_or_knowledge_claim_cn：个体与参照群体的差距会激发追赶动机。

- mechanism_cn：看到自己落后于同伴时，个体更愿意付出额外努力。

- design_requirement_cn：识别过去行为差、成绩低的学生，并检验其是否更受益。

- artifact_choice_cn：用前次作业的StartTime_Prev和Grade_Prev构造StartLate_Prev、GradeLow_Prev交互。

- evaluated_contrast_cn：过去拖延是否晚于中位数；过去成绩是否低于中位数。

- objective_result_cn：Treatment×StartLate_Prev×GradeLow_Prev显著（32.54），H3支持。

##### evidence_pointers

1. Table 11

#### 4. 4

- theory_or_knowledge_claim_cn：社会从众只在规范普遍存在时起作用；社会比较在低流行度时也能激发竞争。

- mechanism_cn：男性可能在低流行度时‘抢先’以获得优势，女性则需要高流行度才产生一致性压力。

- design_requirement_cn：外生操纵消息中披露的百分数。

- artifact_choice_cn：Study IV设置21%、41%、61%三个流行度处理。

- evaluated_contrast_cn：不同流行度水平 vs 纯提醒对照。

- objective_result_cn：男性对21%低流行度已有显著反应；女性各水平均不显著。

##### evidence_pointers

1. Table C3

2. Table C5

3. Figure 5

## 评价逻辑

### evaluation_modes

1. 随机化现场实验

2. 基于LMS日志的客观行为与成绩度量

3. 交互项与子样本回归

4. 中介分析（Zhao两步法+Bootstrap）

5. 操纵竞争性评分和同伴行为流行度

6. 随机化检验

7. 事后调查与排除串通稳健性检验

8. 纯提醒与无消息对照

- why_these_evaluations_cn：因为需要在真实课堂中建立因果效应、识别异质性调节变量，并排除纯提醒、串通和测量效度等替代解释；多个Study的设计是递进的，每个Study补足前一个的识别缺口。

- benchmark_and_contrast_chain_cn：先以纯提醒作为同伴信息的基准；再以随机小组的非男性占多数小组作为性别构成对照；再以非排名评分作为竞争条件的对照；最后以纯提醒作为流行度操纵的对照。各对照都是为了回答‘没有这种设计因素时效应是否还存在’。

### claim_evidence_ledger

#### 1. 1

- claim：同伴信息降低拖延

- evidence：Study I男性显著提前；Study III排名条件下男性显著；Study IV男性在多个流行度显著

- status：对男性支持，全样本不总是支持

#### 2. 2

- claim：同伴信息提高成绩

- evidence：Table 9合并三研究处理效应4.13，p<0.01；男性子样本6.54

- status：支持

#### 3. 3

- claim：男性比女性更受同伴信息影响

- evidence：Study I、III排名条件、合并成绩模型、Study IV中的Treatment×Male和分样本结果

- status：支持

#### 4. 4

- claim：男性占多数的环境增强效应

- evidence：Study II男性占多数小组12.03小时；合并Study II+III的交互19.70，p=0.06

- status：支持但显著性边缘

#### 5. 5

- claim：过去行为差和成绩低者更受益

- evidence：Table 11三阶交互32.54，p<0.05

- status：支持

#### 6. 6

- claim：行为改善中介成绩提升

- evidence：Table 10：男性中介效应0.92，Bootstrap p<0.05

- status：对男性支持，对女性不成立

#### 7. 7

- claim：机制是社会比较而非从众

- evidence：Study III仅排名条件下出现性别差异；Study IV男性对低流行度仍响应

- status：由调节模式推断，未直接测量竞争偏好

- internal_validity_strategy_cn：随机分组、组内随机、随机化检验；用随机小组创造性别构成外生变异；用排名/非排名评分和流行度操纵进行机制检验；通过串通调查与排除可能串通者控制污染；用纯提醒对照排除提醒本身的效果；用自报拖延问卷验证行为度量。

- external_validity_strategy_cn：在多个课程、多个section、多学期（从2017年评分政策开始）的商科核心课程中重复实验；使用通用LMS Canvas；将结果表述为受性别构成、评分政策和过去行为调节的条件化效应，而非无条件平均效应，从而提示推广边界。

- what_is_not_actually_tested_cn：没有直接测量个体感知到的竞争强度或社会比较心理过程；‘男性更偏好竞争’是引用文献解释而非本文测量；女性在非竞争环境中的社会从众机制没有被直接实验检验；长期效果和课外场景未测试。

## 贡献闭环

- technical_claim_cn：成功开发并部署一个能自动从Canvas日志提取学生进度、计算参考组百分比并发送定向提醒和同伴信息的程序。

- artifact_claim_cn：同伴信息提醒功能可以内置于LMS；它是一个可行的行为干预，但效果高度依赖性别、性别构成、评分政策和过去行为。

- mechanism_claim_cn：在竞争性环境中，同伴信息通过社会比较和竞争动机（而非单纯社会从众）推动行为改变；提前开始作业的行为改善是成绩提升的中介。

- boundary_claim_cn：效应在男生、男性占多数的参照组、排名制评分、过去表现较差的学生中更强；对女生、非排名情境或低流行度时可能无效甚至出现反向趋势。

- reusable_design_knowledge_cn：定向干预原则：应根据收件人的性别、性别构成、过去行为/成绩和同伴行为流行度决定是否发送、如何发送同伴信息；低流行度信息也能激发男性竞争，但对女性可能需采用其他框架。

- theoretical_contribution_cn：将社会规范干预理论从非竞争情境扩展到竞争情境，提出‘情境决定从众还是社会比较主导’；并用性别差异翻转来修正先前女性更响应社会规范干预的结论。

- how_discussion_closes_intro_gap_cn：讨论回到引言提出的‘竞争环境中同伴信息效果未知’，用Study III和Study IV的结果区分社会比较与社会从众，说明为什么先前非竞争环境得到的结论不适用于排名制课堂。

- overclaim_or_unsupported_leaps_cn：把‘男性更偏好竞争’作为解释时依赖文献而非直接测量；宣称同伴信息“扩大性别差距”是从性别差异推断出的社会后果，未直接测量长期不平等；H2b的p=0.06边缘显著；Study IV样本较小且未检验成绩。

## 句级写作动作图谱

### 1. P1 S1-S2

- order：1

- section：Abstract

- locator：P1 S1-S2

- move_code：CONTEXT

- paraphrase_cn：以往社会规范干预研究主要集中在非竞争环境；本研究把这类干预放到有竞争性评分政策的课堂环境中评价。

- rhetorical_function_cn：开门见山地制造从一般到特殊的领域切换，让读者知道论文的创新点是情境转换。

- depends_on_cn：依赖社会规范干预文献的存在。

- sets_up_cn：为后续‘竞争环境中的未知效果’提供背景。

- evidence_pointer：Abstract

### 2. P1 S3

- order：2

- section：Abstract

- locator：P1 S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：在LMS上开展现场实验，检验提供描述性同伴信息能否减少拖延并提高表现。

- rhetorical_function_cn：用一句话给出研究任务，让摘要聚焦。

- depends_on_cn：前面的情境设定。

- sets_up_cn：引出后面的具体结果。

- evidence_pointer：Abstract

### 3. P1 S4-S5

- order：3

- section：Abstract

- locator：P1 S4-S5

- move_code：RESULT

- paraphrase_cn：提供同伴信息的效果是混合的，受个人特征和情境变量调节。

- rhetorical_function_cn：提前给出核心发现，并强调异质性而非平均效应。

- depends_on_cn：现场实验完成。

- sets_up_cn：随后说明具体调节变量。

- evidence_pointer：Abstract

### 4. P1 S6-S8

- order：4

- section：Abstract

- locator：P1 S6-S8

- move_code：RESULT

- paraphrase_cn：同伴信息对男性更有效，在男性占多数环境中更强；这与非竞争环境中女性更敏感的结果相反。

- rhetorical_function_cn：展示最突出的反转发现，制造理论张力。

- depends_on_cn：前面提到的混合效应。

- sets_up_cn：引出竞争偏好解释。

- evidence_pointer：Abstract

### 5. P1 S9

- order：5

- section：Abstract

- locator：P1 S9

- move_code：MECHANISM

- paraphrase_cn：性别差异可能源于男性和女性对竞争的不同偏好。

- rhetorical_function_cn：为经验反转提供理论解释，使结果不只是一堆系数。

- depends_on_cn：性别差异结果。

- sets_up_cn：为讨论中的社会比较机制埋伏笔。

- evidence_pointer：Abstract

### 6. P1 S10-S11

- order：6

- section：Abstract

- locator：P1 S10-S11

- move_code：RESULT

- paraphrase_cn：过去行为差、成绩低的人从同伴信息中获益更多。

- rhetorical_function_cn：增加第二个异质性发现，强调定向干预价值。

- depends_on_cn：整体效果存在。

- sets_up_cn：指向H3和实际干预建议。

- evidence_pointer：Abstract

### 7. P1 S12

- order：7

- section：Abstract

- locator：P1 S12

- move_code：CONTRIBUTION

- paraphrase_cn：研究强调同伴信息的异质性效应，并为定向干预提供启示。

- rhetorical_function_cn：把摘要收束到贡献。

- depends_on_cn：所有结果。

- sets_up_cn：让读者预期引言中的贡献声明。

- evidence_pointer：Abstract

### 8. P1 S1-S5

- order：8

- section：Introduction

- locator：P1 S1-S5

- move_code：CONTEXT

- paraphrase_cn：健康应用和LMS等系统记录了大量个人行为数据，使分析和干预成为可能。

- rhetorical_function_cn：建立信息系统数据可服务于行为改善的大背景。

- depends_on_cn：系统应用普遍的事实。

- sets_up_cn：为‘设计数据驱动的定向干预’提供动机。

- evidence_pointer：Introduction P1

### 9. P1 S6-S8

- order：9

- section：Introduction

- locator：P1 S6-S8

- move_code：GAP

- paraphrase_cn：现有社会规范干预大多在非竞争环境，竞争环境中的效果未知。

- rhetorical_function_cn：点明文献缺口，把一般性机会收缩到竞争情境。

- depends_on_cn：前面关于健康应用和LMS的例子。

- sets_up_cn：本研究选择LMS和排名制课堂作为竞争环境。

- evidence_pointer：Introduction P1

### 10. P2 S1-S6

- order：10

- section：Introduction

- locator：P2 S1-S6

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文在LMS情境中研究数字干预；LMS普及且日志数据细粒度，适合做定向实验。

- rhetorical_function_cn：把研究问题落地到一个可操作平台。

- depends_on_cn：前一引言的系统数据背景。

- sets_up_cn：后文Canvas插件和日志指标。

- evidence_pointer：Introduction P2

### 11. P3 S1-S4

- order：11

- section：Introduction

- locator：P3 S1-S4

- move_code：PHENOMENON

- paraphrase_cn：拖延是大学生学业不良的重要前因，调查显示大多数学生有拖延行为并希望减少拖延。

- rhetorical_function_cn：把研究对象从一般行为聚焦到拖延，并说明现实严重性。

- depends_on_cn：LMS情境。

- sets_up_cn：引出现有反拖延干预及其成本。

- evidence_pointer：Introduction P3

### 12. P4 S1-S3

- order：12

- section：Introduction

- locator：P4 S1-S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：过去常用中间期限或教师约谈来减少拖延，虽有效但实施成本高。

- rhetorical_function_cn：总结已有做法并暗示替代干预的必要性。

- depends_on_cn：拖延问题。

- sets_up_cn：引出同伴信息干预的低成本优势。

- evidence_pointer：Introduction P4

### 13. P5 S1-S4

- order：13

- section：Introduction

- locator：P5 S1-S4

- move_code：DESIGN_FEATURE

- paraphrase_cn：本研究设计通过LMS发送同伴信息，披露已开始作业的同学比例。

- rhetorical_function_cn：给出干预的核心设计。

- depends_on_cn：前面对同伴信息文献的提及。

- sets_up_cn：为后面的程序和消息模板提供蓝图。

- evidence_pointer：Introduction P5

### 14. P5 S5-S6

- order：14

- section：Introduction

- locator：P5 S5-S6

- move_code：MECHANISM

- paraphrase_cn：描述性信息可能通过从众或社会比较促使个人改变行为。

- rhetorical_function_cn：提前解释两类机制，为假设和讨论做铺垫。

- depends_on_cn：对社会规范和社会比较文献。

- sets_up_cn：H1和讨论中的机制区分。

- evidence_pointer：Introduction P5

### 15. P6 S1-S3

- order：15

- section：Introduction

- locator：P6 S1-S3

- move_code：GAP

- paraphrase_cn：现场实验中同伴信息效果好坏参半，甚至出现反弹，适用的情境和人群不清楚。

- rhetorical_function_cn：进一步说明不仅是‘没有研究’，而是已有证据矛盾。

- depends_on_cn：文献中的混合结果。

- sets_up_cn：本研究要识别调节变量。

- evidence_pointer：Introduction P6

### 16. P7 S1-S4

- order：16

- section：Introduction

- locator：P7 S1-S4

- move_code：STUDY_OVERVIEW

- paraphrase_cn：采用构建-评价方法：先开发Canvas插件，再进行多组随机现场实验。

- rhetorical_function_cn：告知研究设计和步骤。

- depends_on_cn：前面缺口和LMS数据机会。

- sets_up_cn：为研究方法和Study I-III预告。

- evidence_pointer：Introduction P7

### 17. P8 S1-S4

- order：17

- section：Introduction

- locator：P8 S1-S4

- move_code：RESULT

- paraphrase_cn：实验显示同伴信息减少拖延并提高成绩，但效应受性别、性别构成和过去表现调节。

- rhetorical_function_cn：摘要式报告主要结果，让读者提前知道贡献。

- depends_on_cn：现场实验完成。

- sets_up_cn：后文的详细结果。

- evidence_pointer：Introduction P8

### 18. P9 S1-S5

- order：18

- section：Introduction

- locator：P9 S1-S5

- move_code：THEORY_PROPOSITION

- paraphrase_cn：在竞争情境中，社会比较可能压倒从众，因此男性更可能响应而非女性。

- rhetorical_function_cn：用理论解释结果并制造与旧文献的反差。

- depends_on_cn：性别差异结果和竞争偏好文献。

- sets_up_cn：理论贡献声明。

- evidence_pointer：Introduction P9

### 19. P10 S1-S3

- order：19

- section：Introduction

- locator：P10 S1-S3

- move_code：CONTRIBUTION

- paraphrase_cn：研究对数据驱动的定向干预设计有实践含义。

- rhetorical_function_cn：把贡献从理论扩展到实践。

- depends_on_cn：全部研究结果。

- sets_up_cn：为讨论部分铺垫。

- evidence_pointer：Introduction P10

### 20. Procrastination and Measurement P1 S1-S2

- order：20

- section：Literature Review

- locator：Procrastination and Measurement P1 S1-S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：拖延被定义为延迟开始或完成既定任务，属于自我调节失败。

- rhetorical_function_cn：定义核心行为构念。

- depends_on_cn：拖延研究文献。

- sets_up_cn：后面选择拖延作为干预对象。

- evidence_pointer：Literature Review, Procrastination and Measurement

### 21. Procrastination and Measurement P2 S1-S3

- order：21

- section：Literature Review

- locator：Procrastination and Measurement P2 S1-S3

- move_code：LIMITATION

- paraphrase_cn：自我报告测量有虚报问题；LMS日志提供了客观行为指标。

- rhetorical_function_cn：论证为什么用日志数据而非问卷。

- depends_on_cn：先前测量方法。

- sets_up_cn：使用StartTime作为因变量。

- evidence_pointer：Literature Review, Procrastination and Measurement

### 22. Procrastination Interventions P1 S1-S4

- order：22

- section：Literature Review

- locator：Procrastination Interventions P1 S1-S4

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：已有反拖延干预多为治疗项目和外部期限，虽然在效果上有限，但成本较高。

- rhetorical_function_cn：总结现状并点出局限。

- depends_on_cn：拖延干预文献。

- sets_up_cn：提出替代的同伴信息干预。

- evidence_pointer：Literature Review, Procrastination Interventions

### 23. Procrastination Interventions P2 S1-S3

- order：23

- section：Literature Review

- locator：Procrastination Interventions P2 S1-S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本研究探索不干扰课程安排、可嵌入LMS的同伴信息干预。

- rhetorical_function_cn：明确本研究的替代路径。

- depends_on_cn：先前干预成本高。

- sets_up_cn：为假设和实验设计提供意图。

- evidence_pointer：Literature Review, Procrastination Interventions

### 24. Effects of Peer Information P1-P2

- order：24

- section：Literature Review

- locator：Effects of Peer Information P1-P2

- move_code：MECHANISM

- paraphrase_cn：非竞争环境中同伴信息通过从众改变行为；竞争环境中可能通过社会比较和竞争感改变行为。

- rhetorical_function_cn：建立两个竞争性机制。

- depends_on_cn：社会规范和社会比较文献。

- sets_up_cn：H1和H2背后的机制预测。

- evidence_pointer：Literature Review, Effects of Peer Information

### 25. Effects of Peer Information P3

- order：25

- section：Literature Review

- locator：Effects of Peer Information P3

- move_code：GAP

- paraphrase_cn：现场证据好坏参半甚至出现反弹，需要识别有效情境和人群。

- rhetorical_function_cn：说明为什么需要调节变量研究。

- depends_on_cn：混合证据和反弹研究。

- sets_up_cn：针对性别、性别构成和过去行为提出假设。

- evidence_pointer：Literature Review, Effects of Peer Information

### 26. Effects of Peer Information P1-P4

- order：26

- section：Hypotheses Development

- locator：Effects of Peer Information P1-P4

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：同伴信息通过紧迫感、显著性、社会比较促使学生更早开始，并因更多时间和资源获得更好成绩，因此提出H1a和H1b。

- rhetorical_function_cn：给出第一个假设及其行为逻辑。

- depends_on_cn：社会比较和拖延后果文献。

- sets_up_cn：后面的性别、性别构成和过去表现调节假设。

- evidence_pointer：Hypotheses Development, Effects of Peer Information

### 27. Gender section P1-P3

- order：27

- section：Hypotheses Development

- locator：Gender section P1-P3

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：女性更社会定向、男性更竞争定向；在竞争情境中，男性更可能被同伴信息激活，因此提出H2a。

- rhetorical_function_cn：用性别竞争偏好文献推导调节方向。

- depends_on_cn：Gneezy et al. 等竞争偏好研究。

- sets_up_cn：H2a的统计检验。

- evidence_pointer：Hypotheses Development, The Moderating Role of Gender

### 28. Gender Composition section P1-P3

- order：28

- section：Hypotheses Development

- locator：Gender Composition section P1-P3

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：女性比例高的环境更合作、竞争性弱，因此男性占多数的环境中同伴信息效应更强，提出H2b。

- rhetorical_function_cn：把性别构成的情境调节形式化。

- depends_on_cn：性别构成与团队行为文献。

- sets_up_cn：Study II对性别构成的随机化检验。

- evidence_pointer：Hypotheses Development, Gender Composition

### 29. Past Behavior and Performance P1-P3

- order：29

- section：Hypotheses Development

- locator：Past Behavior and Performance P1-P3

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：与参照群体的差距会激发追赶动机，因此过去行为差、成绩低的人更受益，提出H3。

- rhetorical_function_cn：把‘最需要干预的人是否最受益’变成可检验假设。

- depends_on_cn：社会比较差距与自我调节文献。

- sets_up_cn：附加分析中的三阶交互检验。

- evidence_pointer：Hypotheses Development, Past Behavior and Performance

### 30. Experimental Setting P1

- order：30

- section：Research Method

- locator：Experimental Setting P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：选择商科分析课程是因为班级较大、不同section可比、作业有挑战。

- rhetorical_function_cn：解释实验场地选择的合理性。

- depends_on_cn：实验需要组内随机和可比section。

- sets_up_cn：后续三个Study的样本结构。

- evidence_pointer：Research Method, Experimental Setting

### 31. Experimental Setting P2

- order：31

- section：Research Method

- locator：Experimental Setting P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：开发程序自动读取Canvas日志、计算参考组统计量并随机分配干预对象。

- rhetorical_function_cn：描述核心制品的自动化流程。

- depends_on_cn：LMS日志可访问性。

- sets_up_cn：干预消息中的X%。

- evidence_pointer：Research Method, Experimental Setting

### 32. Experimental Setting P3 and Table 1

- order：32

- section：Research Method

- locator：Experimental Setting P3 and Table 1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：设计三个互补研究：Study I使用section级参照，Study II使用随机小组参照，Study III操纵竞争评分。

- rhetorical_function_cn：预告研究结构。

- depends_on_cn：每个Study在前一Study基础上补缺。

- sets_up_cn：具体实验设计细节。

- evidence_pointer：Table 1

### 33. Experimental Setting P4

- order：33

- section：Research Method

- locator：Experimental Setting P4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：Study II用随机小组产生性别构成变异，解决class/section层面学生自选择造成的识别问题。

- rhetorical_function_cn：说明为什么改变参照群体设计。

- depends_on_cn：Study I无法对性别构成做因果识别的局限。

- sets_up_cn：Study II结果。

- evidence_pointer：Research Method, Experimental Setting

### 34. Experimental Setting Study III

- order：34

- section：Research Method

- locator：Experimental Setting Study III

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：Study III在不以排名决定最终成绩的课程中，仅对实验作业操纵排名评分，从而创造竞争性环境对照。

- rhetorical_function_cn：说明竞争操纵的做法。

- depends_on_cn：需要分离最终成绩政策和实验作业的竞争性评分。

- sets_up_cn：Study III结果。

- evidence_pointer：Research Method, Experimental Setting; Table 4

### 35. Variables and Measurement P1-P2

- order：35

- section：Research Method

- locator：Variables and Measurement P1-P2

- move_code：REQUIREMENT

- paraphrase_cn：用下载数据文件到截止的小时数衡量拖延，用百分制成绩衡量表现，并记录性别、前次拖延、前次成绩和男比例。

- rhetorical_function_cn：定义因变量和调节变量。

- depends_on_cn：LMS日志和课程平台数据。

- sets_up_cn：所有回归模型。

- evidence_pointer：Research Method, Variables and Measurement; Table 5

### 36. Study I P1-P2

- order：36

- section：Results: Study I

- locator：Study I P1-P2

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：Study I沿用文献标准设计，以全班为参照，比较纯提醒与提醒+同伴信息。

- rhetorical_function_cn：建立标准的处理对照。

- depends_on_cn：文献中的标准设计。

- sets_up_cn：结果中的图和表。

- evidence_pointer：Effects of Providing Peer Information, Study I; Table 2

### 37. Gender Differences P1

- order：37

- section：Results: Study I

- locator：Gender Differences P1

- move_code：RESULT

- paraphrase_cn：回归显示同伴信息全样本主效应不显著，但Treatment×Male显著，男性边际效应约9小时提前。

- rhetorical_function_cn：报告核心性别调节。

- depends_on_cn：随机化与OLS模型。

- sets_up_cn：分性别子样本和H2a支持。

- evidence_pointer：Table 6

### 38. Gender Differences P2

- order：38

- section：Results: Study I

- locator：Gender Differences P2

- move_code：RESULT

- paraphrase_cn：分性别分析显示男性显著提前，女性为负但不显著，因此H2a得到支持。

- rhetorical_function_cn：把交互项落实到子样本方向。

- depends_on_cn：交互项显著。

- sets_up_cn：性别构成初步观察。

- evidence_pointer：Figure 2

### 39. Gender Composition Evidence P1-P2

- order：39

- section：Results: Study I

- locator：Gender Composition Evidence P1-P2

- move_code：RESULT

- paraphrase_cn：按班级男比例分组显示男性主导环境效应更强，但可能有混杂，需要更强设计。

- rhetorical_function_cn：给出初步支持并同时指出局限。

- depends_on_cn：同一section内无性别构成变异。

- sets_up_cn：Study II。

- evidence_pointer：Figure 3; Study I Gender Composition

### 40. Study II P1

- order：40

- section：Results: Study II

- locator：Study II P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：Study II用随机小组创造外在性别构成变异。

- rhetorical_function_cn：说明新的识别策略。

- depends_on_cn：Study I的识别局限。

- sets_up_cn：Study II结果和H2b检验。

- evidence_pointer：Effects of Providing Peer Information, Study II

### 41. Study II P2

- order：41

- section：Results: Study II

- locator：Study II P2

- move_code：RESULT

- paraphrase_cn：男性在男性占多数小组中显著提前12.03小时，其他个体不显著。

- rhetorical_function_cn：提供性别构成调节的直接证据。

- depends_on_cn：随机分组设计。

- sets_up_cn：合并Study II和III的正式交互检验。

- evidence_pointer：Table 7

### 42. Study II P3

- order：42

- section：Results: Study II

- locator：Study II P3

- move_code：RESULT

- paraphrase_cn：合并Study II与III后，男性占多数小组的处理效应显著强于非男性占多数小组，H2b得到支持。

- rhetorical_function_cn：增加样本量和检验力。

- depends_on_cn：两个Study的数据。

- sets_up_cn：讨论中的情境调节结论。

- evidence_pointer：Table B2

### 43. Study III P1

- order：43

- section：Results: Study III

- locator：Study III P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：Study III在实验作业层面操纵排名与非排名评分，以直接检验竞争机制。

- rhetorical_function_cn：说明如何检验机制。

- depends_on_cn：Study II无法直接操纵竞争。

- sets_up_cn：排名/非排名结果。

- evidence_pointer：Effects of Providing Peer Information, Study III; Table 4

### 44. Study III P2

- order：44

- section：Results: Study III

- locator：Study III P2

- move_code：RESULT

- paraphrase_cn：排名条件下男性显著提前、女性无，非排名条件下性别差异消失。

- rhetorical_function_cn：证明竞争环境是性别差异的条件。

- depends_on_cn：随机分配排名条件。

- sets_up_cn：讨论社会比较机制。

- evidence_pointer：Table 8

### 45. Grades P1

- order：45

- section：Performance Outcome

- locator：Grades P1

- move_code：RESULT

- paraphrase_cn：合并三研究后，同伴信息显著提高成绩4.13分，支持H1b。

- rhetorical_function_cn：从行为结果过渡到绩效结果。

- depends_on_cn：之前的行为结果。

- sets_up_cn：成绩上的性别交互。

- evidence_pointer：Table 9

### 46. Grades P2

- order：46

- section：Performance Outcome

- locator：Grades P2

- move_code：RESULT

- paraphrase_cn：成绩模型中Treatment×Male显著，男性显著改善而女性不显著。

- rhetorical_function_cn：把性别调节延伸到绩效。

- depends_on_cn：混合样本回归。

- sets_up_cn：中介分析。

- evidence_pointer：Table 9

### 47. Mediating Role of Behavior Change P1-P2

- order：47

- section：Performance Outcome

- locator：Mediating Role of Behavior Change P1-P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用Zhao两步法和Bootstrap分别对男女检验行为改善是否中介成绩提升。

- rhetorical_function_cn：说明中介分析方法和分性别原因。

- depends_on_cn：已有处理和成绩效应。

- sets_up_cn：中介结果。

- evidence_pointer：Mediating Role of Behavior Change; Table 10

### 48. Mediating Role of Behavior Change P3

- order：48

- section：Performance Outcome

- locator：Mediating Role of Behavior Change P3

- move_code：RESULT

- paraphrase_cn：男性中Treatment对StartTime为10.23，StartTime对Grade为0.09，中介0.92显著；女性无显著中介。

- rhetorical_function_cn：建立行为→成绩的因果链条。

- depends_on_cn：两步回归和Bootstrap。

- sets_up_cn：讨论中的机制主张。

- evidence_pointer：Table 10

### 49. Past Behavior and Performance P1-P2

- order：49

- section：Additional Analyses

- locator：Past Behavior and Performance P1-P2

- move_code：RESULT

- paraphrase_cn：三阶交互Treatment×StartLate_Prev×GradeLow_Prev显著，说明过去行为差且成绩低者从同伴信息中受益更多，H3支持。

- rhetorical_function_cn：报告第三个调节假设。

- depends_on_cn：合并数据回归。

- sets_up_cn：定向干预含义。

- evidence_pointer：Table 11

### 50. Prevalence section P1-P2

- order：50

- section：Additional Analyses

- locator：Prevalence section P1-P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：由于前三个Study的流行度X并非严格外生，Study IV通过操纵21%/41%/61%的流行度来解决内生性问题。

- rhetorical_function_cn：说明额外研究的必要性。

- depends_on_cn：流行度可能受干预时机影响。

- sets_up_cn：Study IV结果。

- evidence_pointer：Additional Analyses, Effect of the Prevalence of Peer Behavior; Table C3

### 51. Prevalence results Figure 5 and Table C5

- order：51

- section：Additional Analyses

- locator：Prevalence results Figure 5 and Table C5

- move_code：RESULT

- paraphrase_cn：男性对低流行度21%已有显著反应，女性在各流行度均不显著。

- rhetorical_function_cn：用外生流行度支持竞争解释。

- depends_on_cn：随机化流行度设计。

- sets_up_cn：讨论中从众与社会比较区分。

- evidence_pointer：Figure 5; Table C5

### 52. Cross-talk P1-P2

- order：52

- section：Additional Analyses

- locator：Cross-talk P1-P2

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：事后调查显示串通概率约6%-8%，排除可能串通后结果一致。

- rhetorical_function_cn：处理信息污染威胁。

- depends_on_cn：事后调查。

- sets_up_cn：保证后续结论的因果可信度。

- evidence_pointer：Additional Analyses, Cross-talk; Table F2-F3

### 53. Reminder messages alone

- order：53

- section：Additional Analyses

- locator：Reminder messages alone

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：纯提醒与无消息相比没有显著效果，说明效果来自同伴信息本身。

- rhetorical_function_cn：排除提醒功能作为替代解释。

- depends_on_cn：Study III中的无消息/提醒对照。

- sets_up_cn：把干预效应归因于同伴信息。

- evidence_pointer：Figure 6; Table D1

### 54. Social Conformity or Social Comparison? P1-P3

- order：54

- section：Discussion

- locator：Social Conformity or Social Comparison? P1-P3

- move_code：MECHANISM

- paraphrase_cn：非竞争情境从众主导，竞争情境社会比较可主导；本研究结果符合竞争偏好理论。

- rhetorical_function_cn：用理论整合所有经验结果。

- depends_on_cn：Study III和IV的机制证据。

- sets_up_cn：理论贡献声明。

- evidence_pointer：Discussion, Social Conformity or Social Comparison?

### 55. Theoretical Implications P1-P3

- order：55

- section：Discussion

- locator：Theoretical Implications P1-P3

- move_code：CONTRIBUTION

- paraphrase_cn：研究将同伴信息干预扩展到竞争环境，解释混合证据，并建立行为改善到成绩的中介链。

- rhetorical_function_cn：回应引言缺口。

- depends_on_cn：全部实验结果。

- sets_up_cn：性别差距‘暗面’讨论。

- evidence_pointer：Discussion, Theoretical Implications

### 56. Theoretical Implications P4

- order：56

- section：Discussion

- locator：Theoretical Implications P4

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：同伴信息可能扩大性别差距，因为在竞争环境中女性处于不利地位。

- rhetorical_function_cn：指出贡献的边界和潜在负面后果。

- depends_on_cn：性别差异结果。

- sets_up_cn：实践定向干预建议。

- evidence_pointer：Discussion, Theoretical Implications

### 57. Practical Implications P1-P3

- order：57

- section：Discussion

- locator：Practical Implications P1-P3

- move_code：PRACTICAL_STAKES

- paraphrase_cn：设计定向干预时需考虑性别、性别构成、过去表现和流行度，可针对男性占多数环境或过去表现差的学生。

- rhetorical_function_cn：把实验结果转化为设计原则。

- depends_on_cn：H2a、H2b、H3的结果。

- sets_up_cn：局限和未来研究。

- evidence_pointer：Discussion, Practical Implications

### 58. Limitations and Future Research P1

- order：58

- section：Discussion

- locator：Limitations and Future Research P1

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：低流行度对女性可能反弹；未来可改变信息框架、使用组间锦标赛或扩展到其他情境。

- rhetorical_function_cn：明确边界并给出改进方向。

- depends_on_cn：Study IV的流行度发现。

- sets_up_cn：让贡献不过度一般化。

- evidence_pointer：Discussion, Limitations and Future Research

### 59. Validation of StartTime P1-P4

- order：59

- section：Appendix F

- locator：Validation of StartTime P1-P4

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：用自报拖延问卷验证StartTime：相关显著为负，回归中StartTime负向预测拖延倾向。

- rhetorical_function_cn：给行为度量提供效度证据。

- depends_on_cn：问卷和日志数据。

- sets_up_cn：使所有以StartTime为因变量的结论可信。

- evidence_pointer：Appendix F; Table F1

### 60. Randomization Tests and Group Summaries

- order：60

- section：Appendix A-B

- locator：Randomization Tests and Group Summaries

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：各Study的随机化检验显示处理组与对照组在可观测特征上没有显著差异；Study II/III的性别构成分布有足够变异。

- rhetorical_function_cn：为因果推断提供随机化基础。

- depends_on_cn：实验设计和数据收集。

- sets_up_cn：让主结果不被归因于事前差异。

- evidence_pointer：Table A1-A3; Table B1

## 写作技术

- gap_construction_cn：先把社会规范干预的已知结论限定在非竞争场景，再指出LMS中的排名制课堂是竞争环境，现场证据有限且结果矛盾，形成未知；同时指出已有反拖延措施成本高，为新干预提供实用理由。

- signposting_cn：摘要和引言预告‘三个互补研究’；方法部分用Table 1汇总三研究目标/条件；每节说‘下一节...’，Study I/II/III之间明确‘替代设计’原因。

- transition_logic_cn：从Study I观察性别构成但无法因果识别→Study II用随机小组产生性别构成变异→Study III再操纵竞争排名→Study IV操纵流行度；每步都是填补上一步识别缺口。

- claim_evidence_rhythm_cn：先可视化展示模式，再用回归与交互项检验，再以子样本和跨Study合并增强证据；稳健性检查放在主结果之后，防止外部解释。

- benchmark_narrative_cn：以纯提醒为行为基准；以非排名政策为竞争性政策基准；以控制组为流行度操纵基准；通过附录随机化检验说明对照组可比。

- theory_return_cn：讨论部分用两个竞争性理论（从众 vs 社会比较）组织结果，再把性别差异解释为竞争偏好，最后将研究定位为对理论的边界补充。

- contribution_positioning_cn：明确说扩展文献到竞争环境、解释混合结果、建立中介链，并指出潜在‘暗面’（性别差距扩大）。

- novelty_protection_cn：将贡献从‘有效/无效’提升为‘何时有效、对谁有效、为什么有效’；用中介和机制操纵防止被看作一次性实验。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：建立背景与实用价值：说明系统日志数据、LMS普及、拖延危害。

- research_job_cn：找到可被干预的普遍行为，并确认平台上有丰富的可观测行为记录。

- required_evidence_cn：行为普遍性数据、平台日志可用性、已有干预成本证据。

- transition_to_next_cn：从一般系统数据转入‘特定行为亟待干预’。

#### 2. 2

- step：2

- writing_job_cn：指出文献局限：总结社会规范干预在非竞争场景有效/混合，竞争场景未知。

- research_job_cn：综述同伴信息、社会比较、性别差异和拖延干预文献，定位缺口。

- required_evidence_cn：现有非竞争情境证据、现场结果矛盾或反弹案例。

- transition_to_next_cn：从‘缺什么’过渡到‘本研究要问什么’。

#### 3. 3

- step：3

- writing_job_cn：开发干预制品与设计条件：描述Canvas插件、参考组百分比、随机分配、消息模板。

- research_job_cn：实现自动取数、计算、分组和发送系统。

- required_evidence_cn：系统可运行、字段可提取、随机化可行、样本量足够。

- transition_to_next_cn：用Table 1预告多个互补Study。

#### 4. 4

- step：4

- writing_job_cn：用多个Study逐级识别：每个Study解决上一个识别缺口。

- research_job_cn：依次改变参照群体、竞争政策和流行度，收集行为与成绩数据。

- required_evidence_cn：随机化检验、处理/控制差异、必要的子样本和交互项。

- transition_to_next_cn：从行为结果转向成绩结果。

#### 5. 5

- step：5

- writing_job_cn：建立行为结果到绩效结果的中介，并做稳健性检验。

- research_job_cn：构造StartTime和Grade，运行两步中介和Bootstrap；排除串通、纯提醒和测量效度威胁。

- required_evidence_cn：中介效应显著，稳健性检验结果一致。

- transition_to_next_cn：从‘有效’过渡到‘为什么有效’。

#### 6. 6

- step：6

- writing_job_cn：返回理论并声明边界：用社会比较vs从众解释结果，给出定向设计原则。

- research_job_cn：把调节模式归纳为理论机制，并说明适用条件。

- required_evidence_cn：多个Study一致的方向、机制操纵结果和中介证据。

- transition_to_next_cn：进入局限和未来研究。

### most_transferable_moves_cn

1. 用互补的多个现场实验，后一个Study专门修补前一个的识别缺陷

2. 把结果表述为条件化效应而非平均效应

3. 在讨论中用竞争性理论解释经验反转

4. 用中介分析把行为效果连到最终绩效

### resource_intensive_or_nonstandard_parts_cn

1. 需要真实课堂、LMS后台日志、教师配合和课程评分政策控制

2. 需要可编程发送消息并随机化的平台插件

3. 需要大规模学生样本和多课程/多section

4. 需要排名/非排名评分操纵以及外生流行度操纵

### what_not_to_copy_superficially_cn

1. 不要只复制‘男性效应’或‘同伴信息有效’的措辞而没有随机化证据

2. 不要在没有竞争性评分或性别构成变异时说社会比较机制

3. 不要在没有中介分析时声称行为改善导致成绩提升

4. 不要把纯粹技术演示包装成现场因果实验

- single_best_description_of_the_routine_cn：从现实行为问题出发，用可嵌入系统的同伴信息干预，通过多个环环相扣的现场实验，把‘是否有效’转变为‘对谁、何时、为何有效’，再用理论返回完成贡献定位。

## 分析边界

正文和附录齐全，但OCR/表格转换可能导致个别数字与原文存在细微差异；本文没有页码，只有节/表/图/附录位置；Study IV样本较小且只报告行为结果；H2b的检验在原文中报告为p=0.06，属于边缘显著；对中介和机制的分析主要依赖统计推断而非直接测量心理构念。
