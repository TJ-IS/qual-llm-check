# Be Together, Run More: Enhancing Group Participation in Fitness Technology

- 作者：Zilong Liu; Xuequn Wang; Xin (Robert) Luo; Xiaolong Song; Na Liu; Yuan Zhang
- 年份 / 期刊：2023 / Journal of the Association for Information Systems
- DOI：10.17705/1jais.00779
- 源文件：13544_2023_be-together-run-more-enhancing-group-participation-in-fitness-technology.md
- 论文主类型：field_intervention_or_platform_experiment
- 主导写作弧线：phenomenon_mechanism_intervention_field_test
- 置信度：0.83

## 文章级论证概况

- 核心问题：在健身跑步应用中，一种能够促进线下群体参与的功能（Running Spot）能否以及如何提升跑步小组的整体参与度？该效果在什么边界条件下更强？

- 制品与设计：研究聚焦于中国某主流跑步应用在2017年11月上线的“Running Spot”功能：该功能在城市指定若干跑步点，并让同一跑步小组成员看到彼此是否正在相同跑步点跑步。作者将其概念化为“线下群体参与促进功能（offline group engagement facilitation）”，强调它促进的是非正式、即兴的成员间线下社交互动，而非预先计划的活动。

- 客观结果：基于151个跑步小组38周面板数据的DID估计显示，使用Running Spot的“跑步点小组”在功能上线后参与率显著高于“非跑步点小组”；匹配样本后结果稳健。群规模调节项显著为负，表明小组规模越小效果越强；距离调节项显示，距最近跑步点1.2–3.7公里的小组效果最强，距离过远或过近效果较弱，因此H3得到部分支持。

- 核心贡献：作者声称首次将关系凝聚力理论语境化到健身技术支持的自我组织跑步小组中，证明其在低任务相互依赖团队中仍有效；同时整合心理距离视角，解释IT功能如何通过缩短心理距离增加反复社交互动；并明确群规模和地理距离作为边界条件；还从群体层面丰富了健身技术文献及线下群体参与研究。

- 整篇论证链：论文先以健身应用用户规模增长与既有个体层面结果矛盾为现实背景，指出跑步常是群体性活动，但IS文献很少在群体层面研究健身技术，尤其缺乏对线下群体参与促进功能的考察；随后引入心理距离视角和关系凝聚力理论，说明Running Spot通过让成员看到彼此在相同跑步点运动，缩短客观/心理距离，促成反复的随意社交互动，进而通过社会纽带和边界界定两条路径增加小组跑步参与；为检验这一理论推理，作者利用该应用真实上线Running Spot形成的准实验，收集151个大连跑步小组38周面板数据，采用DID、时变处理DID、PSM匹配、DDD距离分箱、动态效应和一系列稳健性检验；结果支持主效应、群规模调节，以及部分支持距离调节；进一步通过检验离线活动指标发现Running Spot反而降低了计划性线下聚会，从而支持其促进的是随意线下参与而非计划性活动；讨论部分将结果上升为对关系凝聚力理论、心理距离机制、群体层面IT健身效果和线下群体参与概念的贡献，并给出对跑步应用开发者的实践建议。

## 类型与写作弧线判定

- 论文主类型判定：论文不是由作者设计并构建IT制品，也不是实验室实验或纯benchmark计算；它利用真实跑步应用平台在2017年11月上线Running Spot这一功能形成自然准实验，以151个跑步小组38周面板数据为证据，用DID/PSM做因果推断，属于真实平台上数字功能上线作为处理干预的现场平台实验。

- 主导写作弧线判定：文章从跑步常为群体活动这一现象入手，用心理距离和关系凝聚力理论建立作用机制，再将Running Spot这一平台数字功能视为干预变量，最后通过DID/PSM等现场数据因果检验，并在讨论中回到理论边界；整体符合“现象—机制—数字干预—现场因果检验”的写作弧线。

## 研究开展程序

- study_or_phase_count：9

- 研究阶段总序列：论文首先建立理论和假设框架，然后依托平台功能上线构造准实验样本；继而对预处理期进行平行趋势检验，为主体DID奠定识别基础；用基础DID和时变处理DID检验主效应；用PSM匹配样本处理自选择问题；随后分别检验群规模和距离的调节作用；再分析处理效应的动态变化；通过多样本、替代结果变量和天气控制进行稳健性检验；最后用离线活动指标检验机制替代解释。各阶段依次回应前一阶段遗留的自选择、边界条件和替代解释问题。

### studies_or_phases

#### 1. 准实验数据收集与样本构造

- order：1

- name_cn：准实验数据收集与样本构造

- question_cn：Running Spot上线能否在真实平台数据中形成可比较的处理组和对照组？

- inputs_and_setting_cn：中国大连151个跑步小组，2017年8月至2018年4月共38周，周度小组层面面板数据；功能在第15周上线，城市设有4个指定跑步点。

- designed_or_compared_object_cn：处理组为至少在某指定跑步点出现过的小组（spot groups），对照组为从未出现在任一跑步点的小组（non-spot groups）。

- baseline_control_or_counterfactual_cn：非跑步点小组及第14周前的处理前阶段。

##### objective_metrics

1. 小组活跃度（每周参与人数/小组规模，取对数）

2. SpotGroup是否曾使用跑步点

3. After是否在功能上线后

- analysis_method_cn：面板数据整理、描述性统计、处理组/对照组划分。

- main_result_cn：151个小组中76个为跑步点小组，75个为非跑步点小组；处理前两组在距跑步点距离、小组规模、离线活动图片数等变量上存在显著差异。

- argumentative_role_cn：建立后续因果推断的基本数据和分组结构。

- remaining_uncertainty_cn：小组是否使用跑步点并非随机分配，处理前组间差异可能引发选择偏差。

- link_to_next_phase_cn：组间预处理差异要求先验证平行趋势，再使用DID和PSM降低自选择影响。

##### evidence_pointers

1. Section 4.1-4.2

2. Table 2

3. Section 4.3

#### 2. 平行趋势假设验证

- order：2

- name_cn：平行趋势假设验证

- question_cn：在处理前时期，跑步点小组与非跑步点小组的活跃度变化趋势是否平行？

- inputs_and_setting_cn：2017年第1周至第15周前（即第14周）的数据，共2265个观测。

- designed_or_compared_object_cn：SpotGroup×Week交互项。

- baseline_control_or_counterfactual_cn：非跑步点小组的活跃度趋势。

##### objective_metrics

1. log(活跃度)

2. SpotGroup×Week系数显著性

- analysis_method_cn：固定效应回归、时间序列图（Figure 3）。

- main_result_cn：SpotGroup×Week在预处理期不显著，两组趋势无显著差异；图3显示第15周后两组活跃度开始分化。

- argumentative_role_cn：为DID的识别假设提供支持，使第15周后的估计可被解释为功能效果。

- remaining_uncertainty_cn：只能排除线性趋势差异，无法完全排除遗漏时变混杂因素。

- link_to_next_phase_cn：确认平行趋势后进入主DID估计。

##### evidence_pointers

1. Section 5.1

2. Figure 3

3. Table 3

#### 3. 基础DID主效应检验（H1）

- order：3

- name_cn：基础DID主效应检验（H1）

- question_cn：Running Spot是否显著提高了跑步点小组的参与度？

- inputs_and_setting_cn：全部151个小组38周数据（5738个观测），包括固定效应和聚类稳健标准误。

- designed_or_compared_object_cn：SpotGroup×After交互项。

- baseline_control_or_counterfactual_cn：非跑步点小组及功能上线前阶段。

##### objective_metrics

1. log(活跃度)

2. SpotGroup×After系数

- analysis_method_cn：DID，含小组固定效应和周固定效应；另用时变处理DID。

- main_result_cn：SpotGroup×After系数为正且显著（模型A1为0.006，A2为0.007，均p<0.01），支持H1。

- argumentative_role_cn：直接检验核心假设，确认功能上线对群体参与的正向效果。

- remaining_uncertainty_cn：处理组和对照组存在预处理观测特征差异，自选择可能干扰因果解释。

- link_to_next_phase_cn：需要通过PSM匹配构造更可比的控制组。

##### evidence_pointers

1. Section 5.2

2. Table 4 Models A1-A2

#### 4. PSM匹配后DID估计

- order：4

- name_cn：PSM匹配后DID估计

- question_cn：在平衡可观测预处理特征后，Running Spot的效果是否仍然成立？

- inputs_and_setting_cn：按logit模型计算倾向得分，使用最近邻一对一无放回匹配，得到39个跑步点小组和39个非跑步点小组的匹配样本。

- designed_or_compared_object_cn：匹配后的SpotGroup×After交互项。

- baseline_control_or_counterfactual_cn：匹配后的非跑步点小组。

##### objective_metrics

1. 匹配后协变量平衡t检验

2. log(活跃度)

3. SpotGroup×After系数

- analysis_method_cn：PSM + DID，聚类到小组。

- main_result_cn：匹配后t检验不显著，协变量平衡；模型A3和A4中交互项仍显著为正（0.011和0.012，均p<0.01）。

- argumentative_role_cn：缓解自选择问题，增强主效应的因果可信度。

- remaining_uncertainty_cn：只能平衡可观测变量，隐藏偏差仍可能存在。

- link_to_next_phase_cn：在匹配样本上进行调节效应分析，使结果更具可比性。

##### evidence_pointers

1. Section 5.2.1

2. Table 5

3. Table 4 Models A3-A4

#### 5. 群规模调节效应检验（H2）

- order：5

- name_cn：群规模调节效应检验（H2）

- question_cn：Running Spot的正向效果是否在小规模小组中更强？

- inputs_and_setting_cn：匹配后的78个小组、2964个观测。

- designed_or_compared_object_cn：LargeGroup二分类（大规模组 vs 小规模组），三重交互SpotGroup×After×LargeGroup。

- baseline_control_or_counterfactual_cn：小规模小组和功能上线前阶段。

##### objective_metrics

1. 三重交互项系数

- analysis_method_cn：DID扩展模型。

- main_result_cn：三重交互项显著为负（-0.011，p<0.01），说明大型小组中的正向效应更弱，H2得到支持。

- argumentative_role_cn：为关系凝聚力理论提供边界条件证据：小组成员更容易与多数成员互动，关系凝聚力更易形成。

- remaining_uncertainty_cn：大/小规模是二分化操作，未测量成员间实际互动频率。

- link_to_next_phase_cn：继续考察另一边界条件：距指定跑步点的地理距离。

##### evidence_pointers

1. Section 5.3

2. Table 6

#### 6. 距离调节效应检验（H3）

- order：6

- name_cn：距离调节效应检验（H3）

- question_cn：距最近指定跑步点的距离是否调节Running Spot的效果？

- inputs_and_setting_cn：匹配后样本，按小组注册地址到最近跑步点距离分成五分位；基线为距最近跑步点>6.2公里的小组。

- designed_or_compared_object_cn：距离分箱变量与SpotGroup×After的三重交互。

- baseline_control_or_counterfactual_cn：距离>6.2公里的跑步点小组。

##### objective_metrics

1. 各组距分箱交互项系数

- analysis_method_cn：DDD/triple-difference估计。

- main_result_cn：距最近跑步点<1.2公里和1.2–3.7公里的交互项显著为正；3.7–6.2公里不显著；其中1.2–3.7公里组系数最大，说明中等距离组效果最强，H3仅部分支持。

- argumentative_role_cn：支持距离作为物理距离引发心理距离和旅行成本的边界条件，并揭示非线性关系。

- remaining_uncertainty_cn：“中等距离最优”的阈值是基于分箱数据的事后观察，缺乏先验理论精确预测。

- link_to_next_phase_cn：进一步分析功能效果随时间演变，判断其是短期刺激还是持续性机制。

##### evidence_pointers

1. Section 5.4

2. Table 7 Model A6

#### 7. 处理效应的动态分析

- order：7

- name_cn：处理效应的动态分析

- question_cn：Running Spot的效果在功能上线后如何随时间变化？

- inputs_and_setting_cn：匹配后样本，将后处理期划分为四个六周区间。

- designed_or_compared_object_cn：SpotGroup×After^k（k=1,...,4）。

- baseline_control_or_counterfactual_cn：非跑步点小组和各区间之前阶段。

##### objective_metrics

1. 各时期交互项系数

- analysis_method_cn：动态DID。

- main_result_cn：功能上线初期效果较小且边际显著，7–18周效果最强，之后减弱但仍显著。

- argumentative_role_cn：支持学习效应和习惯形成解释，排除纯粹瞬时营销效应。

- remaining_uncertainty_cn：长期衰减原因未直接测量，可能是成员习惯化或功能新鲜感消退。

- link_to_next_phase_cn：通过稳健性检验排除排名、新用户、天气、极端规模和离线聚会等替代解释。

##### evidence_pointers

1. Section 5.5

2. Table 7 Model A7

#### 8. 稳健性检验与替代解释

- order：8

- name_cn：稳健性检验与替代解释

- question_cn：主结果是否受到城区/郊区、离线图片、初始活跃度、排名变化、新用户加入、极端规模、天气、离线聚会等因素影响？

- inputs_and_setting_cn：匹配后样本及多个子样本：城区/郊区子样本、无离线图片组、高/低活跃组、截断规模组、含天气变量的扩展模型。

- designed_or_compared_object_cn：SpotGroup×After在不同子样本和不同结果变量（排名、小组规模）上的效应。

- baseline_control_or_counterfactual_cn：各子样本内的非跑步点小组。

##### objective_metrics

1. 各模型交互项显著性

2. 对排名和小组规模的影响

- analysis_method_cn：分组DID/PSM、替代结果变量DID、天气控制模型。

- main_result_cn：主效应在全部稳健性检验中保持显著；Running Spot对小组排名和小组规模无显著影响；排除天气、极端规模等干扰后结果一致。

- argumentative_role_cn：系统排除最可能的竞争解释，将效果归因于Running Spot的成员位置可见性而非其他机制。

- remaining_uncertainty_cn：仍无法排除未观测组间差异或平台同期其他变化的混杂。

- link_to_next_phase_cn：用离线活动指标直接检验功能是否通过计划性离线聚会起作用。

##### evidence_pointers

1. Section 5.6

2. Table 8

#### 9. 离线活动机制检验

- order：9

- name_cn：离线活动机制检验

- question_cn：Running Spot带来的活跃度提升是否可归因于应用内组织的计划性线下聚会增加？

- inputs_and_setting_cn：匹配后样本，以No.OfflinePeople、No.OfflineActivities、OfflineProportion为替代因变量。

- designed_or_compared_object_cn：SpotGroup×After对三类离线活动指标的影响。

- baseline_control_or_counterfactual_cn：非跑步点小组及功能上线前阶段。

##### objective_metrics

1. 离线参与人数

2. 离线活动数量

3. 离线参与比例

- analysis_method_cn：DID/PSM，因变量替换为离线活动指标。

- main_result_cn：SpotGroup×After对三类离线活动指标均显著为负，说明Running Spot反而减少了通过应用组织的计划性离线聚会；活跃度增加不能由计划性离线聚会解释。

- argumentative_role_cn：用反向证据支持概念化：Running Spot促进的是随意的线下共同跑步参与，而非有计划的应用内线下活动。

- remaining_uncertainty_cn：没有直接测量成员间随意社交互动、心理距离或关系凝聚力，机制链条仍主要靠理论推导。

- link_to_next_phase_cn：进入讨论，将负面离线聚会结果整合进理论边界，并说明贡献与实践启示。

##### evidence_pointers

1. Section 5.6

2. Table 9

## 各部分修辞架构

### abstract_moves

1. CONTEXT: 指出个体越来越多使用跑步应用，文献集中于个体层面。

2. LIMITATION: 少有关注群体层面，更缺少线下群体参与促进功能。

3. RQ_OR_OBJECTIVE: 聚焦跑步应用的Running Spot功能，考察其是否能提升群体跑步参与。

4. THEORY_INTRO: 引入心理距离视角和关系凝聚力理论。

5. METHOD_JUSTIFICATION: 使用151个跑步小组38周面板数据。

6. RESULT: 发现Running Spot促进小组参与，且小规模、中等距离组效果更强。

7. CONTRIBUTION: 对健身技术、群体参与和应用开发者具有启示。

### introduction_moves

1. CONTEXT: 健身应用用户与市场规模快速增长。

2. PRACTICAL_STAKES: 健身技术的终极目标是支持锻炼，但效果证据矛盾。

3. PHENOMENON: 跑步虽是个人运动，但经常以群体形式进行。

4. GAP: 现有IS研究主要关注个体层面，很少从群体层面研究。

5. WHY_GAP_MATTERS: 群体有“we-ness”、交互不可化约为个体，且应用服务商需要扩大活跃用户。

6. RQ_OR_OBJECTIVE: 研究促进随意社交互动的功能如何支持群体跑步参与。

7. STUDY_OVERVIEW: 以真实跑步应用Running Spot上线为自然实验。

8. CONTRIBUTION: 预告五项理论与实践贡献。

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE: 文献显示跑步可视为社会活动，群体跑步提供归属感和社会支持。

2. PRIOR_KNOWLEDGE: 群体参与概念包含在线/线下、计划/随意等多个维度。

3. THEORY_INTRO: 引入心理距离视角，解释客观距离如何影响心理距离并促进非正式沟通。

4. THEORY_INTRO: 引入关系凝聚力理论，解释反复社交互动如何通过社会纽带与边界界定产生承诺行为。

5. THEORY_PROPOSITION: Running Spot通过缩短物理/时间距离降低心理距离，促进反复互动。

6. HYPOTHESIS_OR_PROPOSITION: 据此形成H1、H2、H3。

### artifact_design_moves

1. DESIGN_FEATURE: Running Spot是应用内指定跑步点，并让成员看到同组其他成员是否在此跑步。

2. MECHANISM: 该功能提高成员间线下偶遇和随意社交互动的可能性。

3. BOUNDARY_CONDITION: 作者界定其促进的是“与成员相关”（relating with members）的群体参与维度，而非所有维度。

4. REQUIREMENT: 讨论部分提出应用应增加促进线下群体参与的功能，并建议建立跑步点活动排行和虚拟社区空间。

### evaluation_moves

1. METHOD_JUSTIFICATION: 使用DID控制小组和时间固定效应。

2. ROBUSTNESS_OR_BOUNDARY_TEST: 平行趋势检验和模型无关时间序列图提供识别支持。

3. METHOD_JUSTIFICATION: 使用PSM平衡处理前观测特征。

4. BENCHMARK_OR_CONTRAST: 非跑步点小组为自然控制组，距离>6.2公里组为距离基线。

5. RESULT: 主效应、群规模调节、距离调节和动态结果逐步报告。

6. ROBUSTNESS_OR_BOUNDARY_TEST: 多种子样本、替代因变量和天气控制检验稳健性。

7. RESULT: 对离线活动指标为负，作为机制/替代解释检查。

### discussion_and_contribution_moves

1. RESULT: 概括DID/PSM发现并重申主效应稳健。

2. CONTRIBUTION: 将关系凝聚力理论扩展到低任务相互依赖的自我组织小组。

3. CONTRIBUTION: 用心理距离视角补充关系凝聚力理论中“如何增加反复互动”的缺口。

4. BOUNDARY_CONDITION: 群规模与地理距离作为边界条件，并区分不同群体参与类型。

5. CONTRIBUTION: 从群体层面扩展健身技术IT效果研究。

6. CONTRIBUTION: 概念化线下群体参与促进功能，开拓线下群体参与研究。

7. PRACTICAL_STAKES: 对跑步小组成员和应用开发者提出具体建议。

8. LIMITATION_AND_FUTURE: 指出单一应用、非随机分组、未直接测量机制变量等限制。

## 理论/知识到设计的翻译

### 知识/理论基础

1. 心理距离视角（Psychological Distance）

2. 关系凝聚力理论（Relational Cohesion Theory）

3. 自我决定理论中的关系需求（Relatedness）

4. 群体参与文献（Group Engagement）

5. 跑步作为社交活动的经验研究

- 理论—设计耦合：partial

- 耦合判定理由：作者并未基于理论自行设计或开发一个新功能，而是用理论解释平台已存在的Running Spot功能为什么有效；理论影响了概念化、研究问题、假设推导和解释框架，但技术制品选择（指定跑步点与成员位置可见性）来自平台已有功能，并非由理论前瞻性决定；因此属于部分耦合。

- 理论到设计翻译链：心理距离理论指出客观距离（物理、时间、社会距离）影响心理距离，缩短心理距离促进非正式沟通；关系凝聚力理论指出反复社交互动通过社会纽带和边界界定产生承诺行为；两者结合形成命题：Running Spot通过让成员看到同组其他人在相同地点跑步，缩短客观距离→降低心理距离→增加随意社交互动→产生关系凝聚力和不确定性降低→提升小组跑步参与。群规模增大增大社会距离，削弱互动可达性；距跑步点过远增大物理距离与旅行成本，削弱效果；因此群规模和距离成为边界条件。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：心理距离由客观物理/时间/社会距离塑造，缩短心理距离能促进非正式沟通。

- mechanism_cn：看到同组成员在同一指定跑步点跑步，减少了成员之间物理和时间上的客观距离，从而降低心理距离，增加偶然社交互动。

- design_requirement_cn：若要促进线下随意群体参与，功能应提供共同地点和成员位置的可见性。

- artifact_choice_cn：Running Spot功能：指定公共跑步点并让小组内成员看到谁在同一地点跑步。

- evaluated_contrast_cn：使用跑步点的小组与未使用跑步点小组在功能上线前后的活跃度差异。

- objective_result_cn：SpotGroup×After显著为正，支持主效应（H1）。

##### evidence_pointers

1. Section 3.1

2. Section 5.2

3. Table 4

#### 2. 2

- theory_or_knowledge_claim_cn：关系凝聚力理论认为反复社交互动通过社会纽带过程和边界界定过程产生承诺行为。

- mechanism_cn：反复一起跑步使成员获得积极情绪并归因于关系，同时减少不确定性、形成群体独特性，最终表现为以小组为单位持续参与跑步。

- design_requirement_cn：功能应支撑反复、自然的共同跑步而非一次性、计划性聚会。

- artifact_choice_cn：Running Spot让成员有能力反复在同一地点遇到同组成员，形成随意但可重复的互动。

- evaluated_contrast_cn：主效应DID；同时用离线活动指标检验是否由计划性聚会引起。

- objective_result_cn：活跃度显著提升；计划性离线聚会数量反而下降，排除了计划性聚会替代解释。

##### evidence_pointers

1. Section 3.2

2. Section 5.2

3. Table 9

#### 3. 3

- theory_or_knowledge_claim_cn：关系凝聚力理论更适用于成员能与大多数其他成员互动的结构；小群体中互动可达性更高。

- mechanism_cn：小组成员更容易认识彼此、预测对方行为，关系凝聚力更容易形成；大群体成员只能与子集互动，凝聚力受限。

- design_requirement_cn：促进线下参与功能的效果会受群体结构影响，因此应关注群体规模。

- artifact_choice_cn：Running Spot本身不因规模改变，但其效果被群体规模调节。

- evaluated_contrast_cn：大规模组与小规模组的三重交互。

- objective_result_cn：三重交互显著为负，小规模组效果更强（H2支持）。

##### evidence_pointers

1. Section 3.3.2

2. Section 5.3

3. Table 6

#### 4. 4

- theory_or_knowledge_claim_cn：物理距离会影响心理距离和参与成本，因此地理邻近是线下参与功能发挥作用的边界条件。

- mechanism_cn：距跑步点越近，成员更容易到达、物理距离造成的心理距离越小；但过近时基准距离太短，新功能的边际改变较小；中等距离最受益。

- design_requirement_cn：平台指定跑步点时应考虑成员居住/工作地点的空间分布。

- artifact_choice_cn：Running Spot设定了有限数量的城市跑步点，不同小组与其距离不同。

- evaluated_contrast_cn：按距最近跑步点距离分箱，以>6.2公里组为基线的三重交互。

- objective_result_cn：1.2–3.7公里组系数最大且显著，过近和过远组不显著或较弱，H3部分支持。

##### evidence_pointers

1. Section 3.3.3

2. Section 5.4

3. Table 7 Model A6

## 评价逻辑

### evaluation_modes

1. DID（含固定效应、聚类标准误）

2. 时变处理DID

3. 平行趋势检验与时间序列观察

4. PSM匹配后DID

5. DDD/triple-difference 距离调节

6. 动态处理效应DID

7. 多种子样本稳健性检验

8. 替代因变量DID（排名、小组规模、离线活动指标）

9. 天气变量控制

- why_these_evaluations_cn：由于小组是否使用Running Spot并非随机分配，且处理前组间存在显著差异，必须依次解决平行趋势、自选择、调节因素、时间动态和竞争解释，才能将活跃度提升归因于该功能而非其他机制。

- benchmark_and_contrast_chain_cn：非跑步点小组构成自然控制组；功能上线前14周构成处理前基线；PSM匹配后形成39对可比组；群规模检验以大规模组为对比；距离检验以>6.2公里组为基线；动态检验以后处理期四个六周区间互相参照；稳健性检验用若干子样本替换主样本。

### claim_evidence_ledger

#### 1. Running Spot提高跑步点小组的参与度。

- claim_cn：Running Spot提高跑步点小组的参与度。

- evidence_cn：DID模型A1/A2显著为正，平行趋势成立，PSM匹配后A3/A4仍显著。

- strength_cn：强：多种识别策略和稳健性检验一致。

#### 2. 小规模小组中效果更强。

- claim_cn：小规模小组中效果更强。

- evidence_cn：三重交互SpotGroup×After×LargeGroup显著为负。

- strength_cn：中等：结构性调节证据，但未直接测量互动可达性。

#### 3. 距离调节效果呈非线性，中等距离最优。

- claim_cn：距离调节效果呈非线性，中等距离最优。

- evidence_cn：距离分箱三重交互中1.2–3.7公里组最佳，>6.2公里基准不显著。

- strength_cn：中等偏弱：阈值是数据驱动的事后分组，理论未精确预测阈值。

#### 4. 活跃度提升不是来自计划性应用内离线聚会。

- claim_cn：活跃度提升不是来自计划性应用内离线聚会。

- evidence_cn：Running Spot对No.OfflinePeople、No.OfflineActivities、OfflineProportion均显著为负。

- strength_cn：中等：反向排除一种替代机制，但未直接证明随意互动增加。

#### 5. 提升是由成员位置可见性而非跑步点本身造成。

- claim_cn：提升是由成员位置可见性而非跑步点本身造成。

- evidence_cn：处理组在功能上线前可能在同一地点跑步但活跃度较低，上线后活跃度显著上升。

- strength_cn：中等：依赖观察证据和排除法，缺少随机对照。

#### 6. 心理距离和关系凝聚力是作用机制。

- claim_cn：心理距离和关系凝聚力是作用机制。

- evidence_cn：理论推导+群规模/距离调节结果与理论预测一致；但未直接测量心理距离、社交互动或关系凝聚力。

- strength_cn：弱中：机制属于推断而非直接检验。

- internal_validity_strategy_cn：采用DID吸收组间固定效应和时间固定效应；验证平行趋势；用PSM平衡可观测预处理特征；用时变处理DID处理组进入时间差异；通过动态效应观察学习过程；通过多个替代结果变量和子样本排除排名、新用户、天气、极端规模、离线聚会等竞争解释。

- external_validity_strategy_cn：选取单一城市控制天气差异，增加组间可比性；使用中国主流跑步应用提供现实外部环境；讨论部分尝试将心理距离、关系凝聚力和群体参与结果外推到虚拟团队、软件开发和线上社群；但作者同时承认单一应用、单一城市和自组织跑步群体限制了泛化。

- what_is_not_actually_tested_cn：没有直接测量成员的心理距离、随意社交互动频率、积极情绪、关系凝聚力或不确定性降低；没有随机分配处理；没有证明Running Spot功能本身是唯一变化因素（平台同期可能还有其他变化）；没有直接比较不同类型线下群体参与（随意vs计划）的机制差异；距离阈值的非线性解释部分为事后推断。

## 贡献闭环

- technical_claim_cn：在真实平台数据中，一种允许成员看到彼此在同一指定跑步点跑步的移动应用功能，能显著提高跑步小组的参与率；该技术效应在小规模和距跑步点中等距离的小组中更强。

- artifact_claim_cn：提升参与者不是跑步点位置本身，而是Running Spot让成员能够看到同组他人正在同一地点跑步的这一功能特性；处理组在功能上线前可能已在同一地点跑步但活跃度并未提升。

- mechanism_claim_cn：Running Spot通过缩短客观距离降低心理距离，促进成员间随意社交互动；基于关系凝聚力理论，反复互动通过社会纽带过程（积极情绪形成关系凝聚力）和边界界定过程（不确定性降低、群体独特性）增强小组跑步参与。

- boundary_claim_cn：组规模越小效果越强；距指定跑步点的距离并非线性：中等距离（1.2–3.7公里）最优，远距离无效，极近距离效果也较弱；效果在功能上线后7–18周达到峰值，之后减弱但仍显著；Running Spot减少计划性离线聚会，因此边界限于随意型线下群体参与。

- reusable_design_knowledge_cn：设计健身应用时，应优先加入促进线下非正式共同锻炼的功能，如指定共同地点并展示成员位置；该功能应适配小组规模与地理分布；还应提供虚拟空间或线上互动来弥补对计划性离线聚会的替代效应。

- theoretical_contribution_cn：将关系凝聚力理论扩展到低任务相互依赖、自我组织的跑步小组；用心理距离视角补充关系凝聚力理论关于“IT如何增加反复互动”的缺口；识别群体规模和地理距离作为关系凝聚力的边界条件；从群体层面扩展健身技术文献，并提出IT可促进线下群体参与的新概念。

- how_discussion_closes_intro_gap_cn：开篇指出文献缺乏群体层面健身技术研究和对线下群体参与促进功能的考察；讨论部分通过“首次将关系凝聚力理论语境化到跑步小组”“揭示IT通过减少心理距离促进反复互动”“阐明群体规模与距离边界”以及“概念化线下群体参与促进功能”等主张，直接回应了这两个缺口，并把结果提升为对理论和设计的贡献。

- overclaim_or_unsupported_leaps_cn：机制链中多个关键环节未直接测量；把Running Spot简化为“线下群体参与促进功能”可能忽略了其他功能细节；将“中等距离最优”作为理论发现存在事后解释风险；用“跑步点本身不解释效果”的排除法论证功能可见性，但未排除其他同期功能变化；将关系凝聚力理论扩展至低相互依赖任务时，文中并未直接测量关系凝聚力。

## 句级写作动作图谱

### 1. P1 S1

- order：1

- section：Abstract

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：越来越多的人使用跑步应用等新型健身技术支持锻炼。

- rhetorical_function_cn：点明研究对象与领域背景。

- depends_on_cn：不依赖前文。

- sets_up_cn：引出文献不足和本文研究问题。

- evidence_pointer：Abstract P1 S1

### 2. P1 S2-S3

- order：2

- section：Abstract

- locator：P1 S2-S3

- move_code：LIMITATION

- paraphrase_cn：现有文献集中于个体层面，很少研究健身应用如何促进群体锻炼，也缺乏如何用群体功能提高参与的信息。

- rhetorical_function_cn：直接声明学术缺口。

- depends_on_cn：承接上一句的领域背景。

- sets_up_cn：为本文以跑步小组为对象做好铺垫。

- evidence_pointer：Abstract P1 S2-S3

### 3. P2 S1-S3

- order：3

- section：Abstract

- locator：P2 S1-S3

- move_code：STUDY_OVERVIEW

- paraphrase_cn：本文以某跑步应用的Running Spot为背景，用151个跑步小组38周面板数据，结合DID与PSM检验线下群体参与促进功能。

- rhetorical_function_cn：高度概括研究设计和识别策略。

- depends_on_cn：基于前面点明的缺口。

- sets_up_cn：预告结果和贡献。

- evidence_pointer：Abstract P2 S1-S3

### 4. P2 S4

- order：4

- section：Abstract

- locator：P2 S4

- move_code：RESULT

- paraphrase_cn：结果显示Running Spot确实促进小组跑步参与，小规模组和中等距离组效果更强。

- rhetorical_function_cn：给出核心发现。

- depends_on_cn：依赖研究方法叙述。

- sets_up_cn：引出贡献和实践意义。

- evidence_pointer：Abstract P2 S4

### 5. P1 S1-S4

- order：5

- section：Introduction

- locator：P1 S1-S4

- move_code：CONTEXT

- paraphrase_cn：健身技术快速发展，跑步类应用用户数和市场规模大幅增长。

- rhetorical_function_cn：用市场规模数据建立现实重要性。

- depends_on_cn：开篇设置领域场景。

- sets_up_cn：为后续指出“增长虽大但效果证据矛盾”提供张力。

- evidence_pointer：Introduction P1 S1-S4

### 6. P2 S1-S3

- order：6

- section：Introduction

- locator：P2 S1-S3

- move_code：LIMITATION

- paraphrase_cn：健身技术的最终目标是支持锻炼，但现有IS文献对应用是否成功提升锻炼和健康的结果并不一致。

- rhetorical_function_cn：引入学术矛盾，说明需要进一步研究功能如何发挥作用。

- depends_on_cn：依赖于上一句展示的应用增长背景。

- sets_up_cn：引出“个体单独锻炼容易放弃”的解释。

- evidence_pointer：Introduction P2 S1-S3

### 7. P3 S1-S3

- order：7

- section：Introduction

- locator：P3 S1-S3

- move_code：PHENOMENON

- paraphrase_cn：经常独自锻炼容易放弃，而人们常参与群体锻炼，借助他人社会支持改善运动习惯，跑步虽可独自完成但与他人一起可产生积极社会体验。

- rhetorical_function_cn：提出“跑步是群体现象”这一经验事实，为群体层面研究提供理由。

- depends_on_cn：回应上一段的个体锻炼矛盾。

- sets_up_cn：引出群体参与概念和群体层面研究需要。

- evidence_pointer：Introduction P3 S1-S3

### 8. P4 S1-S3

- order：8

- section：Introduction

- locator：P4 S1-S3

- move_code：GAP

- paraphrase_cn：已有研究主要关注健身技术如何促进个体活动，很少探讨其在群体锻炼中的作用。

- rhetorical_function_cn：明确点出文献缺口。

- depends_on_cn：建立在群体锻炼现象之上。

- sets_up_cn：为“为什么群体视角重要”提供展开空间。

- evidence_pointer：Introduction P4 S1-S3

### 9. P4 S4-S6

- order：9

- section：Introduction

- locator：P4 S4-S6

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：群体现象不能由个体聚合替代，成员互动是“we-ness”关键；对服务商而言，扩大活跃用户比提高少数活跃用户运动量更重要。

- rhetorical_function_cn：分别从认识论和实践角度论证缺口的重要性。

- depends_on_cn：承接上一句的缺口。

- sets_up_cn：把研究价值从理论扩充到应用服务商利益。

- evidence_pointer：Introduction P4 S4-S6

### 10. P5 S1-S3

- order：10

- section：Introduction

- locator：P5 S1-S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文目标是研究像Running Spot这类鼓励随意社交互动的功能如何支持小组成员在健身技术辅助下参与锻炼。

- rhetorical_function_cn：正式提出研究目标。

- depends_on_cn：依赖前面缺口和重要性论证。

- sets_up_cn：定义研究对象和概念：线下群体参与促进功能。

- evidence_pointer：Introduction P5 S1-S3

### 11. P5 S4-S5

- order：11

- section：Introduction

- locator：P5 S4-S5

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：选择跑步应用为背景，因为跑步常见且设备要求低，疫情下人们更倾向低强度户外运动。

- rhetorical_function_cn：证明情境选择合理。

- depends_on_cn：衔接研究目标。

- sets_up_cn：为随后介绍中国跑步应用和Running Spot提供背景。

- evidence_pointer：Introduction P5 S4-S5

### 12. P6 S1-S4

- order：12

- section：Introduction

- locator：P6 S1-S4

- move_code：STUDY_OVERVIEW

- paraphrase_cn：作者使用中国主流跑步应用在大连的151个小组38周数据，功能于2017年11月上线，形成准实验；据此研究Running Spot是否促进小组参与。

- rhetorical_function_cn：预告研究设计与数据来源。

- depends_on_cn：承接前述情境选择。

- sets_up_cn：为后文方法部分提供路线图。

- evidence_pointer：Introduction P6 S1-S4

### 13. P7 S1-S5

- order：13

- section：Introduction

- locator：P7 S1-S5

- move_code：CONTRIBUTION

- paraphrase_cn：作者预告五项贡献：语境化关系凝聚力理论、整合心理距离揭示IT如何促进随意互动、澄清边界条件、展示IT在群体层面提升健身、以及为应用留存提供实践指导。

- rhetorical_function_cn：提前声明贡献，让读者形成评价框架。

- depends_on_cn：总结前面的理论逻辑和预期结果。

- sets_up_cn：与讨论部分的理论贡献呼应。

- evidence_pointer：Introduction P7 S1-S5

### 14. Section 2.1 P1

- order：14

- section：Literature Review

- locator：Section 2.1 P1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：文献认为跑步虽然常被独自进行，但也可视为社交活动，群体跑步能创造归属感和积极体验。

- rhetorical_function_cn：提供经验知识基础，支持群体视角。

- depends_on_cn：引用既有跑步与群体研究。

- sets_up_cn：为群体参与概念作铺垫。

- evidence_pointer：Section 2.1 P1

### 15. Section 2.1 P2-P3

- order：15

- section：Literature Review

- locator：Section 2.1 P2-P3

- move_code：LIMITATION

- paraphrase_cn：现有健身技术研究多考察采纳意图和使用行为，很少在群体层面研究，也不清楚具体功能如何促进团体参与。

- rhetorical_function_cn：系统盘点文献后指出两个缺口。

- depends_on_cn：基于Table 1文献总结。

- sets_up_cn：说明本研究以Running Spot作为具体功能切入。

- evidence_pointer：Section 2.1 P2-P3; Table 1

### 16. Section 2.2 P1

- order：16

- section：Literature Review

- locator：Section 2.2 P1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：群体参与被定义为成员围绕任务互动并建立和维持共同关注焦点的过程。

- rhetorical_function_cn：引入核心构念的定义。

- depends_on_cn：来自群体研究文献。

- sets_up_cn：界定本研究关注的群体参与维度。

- evidence_pointer：Section 2.2 P1

### 17. Section 2.2 P2-P4

- order：17

- section：Literature Review

- locator：Section 2.2 P2-P4

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：群体参与可分为计划与随意、在线与线下、不同类型，文献中已有多种分类。

- rhetorical_function_cn：展示群体参与的多维性。

- depends_on_cn：引用Sessions、Metiu与Rothbard、Macgowan与Newman等研究。

- sets_up_cn：为将Running Spot概念化为促进线下随意群体参与做铺垫。

- evidence_pointer：Section 2.2 P2-P4

### 18. Section 2.2 P5

- order：18

- section：Literature Review

- locator：Section 2.2 P5

- move_code：LIMITATION

- paraphrase_cn：尽管群体参与有积极结果，但极少研究探讨IT如何促进群体参与。

- rhetorical_function_cn：再次强调缺口。

- depends_on_cn：基于前面对群体参与文献的综述。

- sets_up_cn：引出研究情境Running Spot。

- evidence_pointer：Section 2.2 P5

### 19. Section 2.3 P1-P3

- order：19

- section：Research Context

- locator：Section 2.3 P1-P3

- move_code：DESIGN_FEATURE

- paraphrase_cn：所选跑步应用2017年11月推出Running Spot，指定热门跑步地点，并允许组员看到同组其他成员的跑步位置。

- rhetorical_function_cn：具体描述研究中的IT功能。

- depends_on_cn：承接文献综述中关于群体参与的分类。

- sets_up_cn：论证该功能可概念化为线下群体参与促进功能。

- evidence_pointer：Section 2.3 P1-P3; Figure 1

### 20. Section 2.3 P4-P6

- order：20

- section：Research Context

- locator：Section 2.3 P4-P6

- move_code：MECHANISM

- paraphrase_cn：Running Spot使成员更容易发现同组其他人在同一地点跑步，从而促进随意社交互动；研究只关注“与成员相关”这一维度。

- rhetorical_function_cn：说明功能到概念的翻译，并限定概念边界。

- depends_on_cn：依赖对功能特性的描述。

- sets_up_cn：为后续理论机制提供概念基础。

- evidence_pointer：Section 2.3 P4-P6

### 21. Section 3 P1

- order：21

- section：Theory

- locator：Section 3 P1

- move_code：THEORY_INTRO

- paraphrase_cn：本研究整合心理距离视角和关系凝聚力理论作为理论框架。

- rhetorical_function_cn：预告核心理论来源及其分工。

- depends_on_cn：承接概念化Running Spot的讨论。

- sets_up_cn：分节展开两个理论。

- evidence_pointer：Section 3 P1; Figure 2

### 22. Section 3.1 P1-S2

- order：22

- section：Theory

- locator：Section 3.1 P1-S2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：心理距离是主体对客体靠近或远离自我此时此地的体验，受空间、时间、社会距离影响。

- rhetorical_function_cn：定义心理距离核心概念。

- depends_on_cn：引用Trope与Liberman。

- sets_up_cn：说明Running Spot为何可以改变成员间心理距离。

- evidence_pointer：Section 3.1 P1-S2

### 23. Section 3.1 P2-P3

- order：23

- section：Theory

- locator：Section 3.1 P2-P3

- move_code：MECHANISM

- paraphrase_cn：Running Spot使成员在同一地点跑步，降低物理和时间距离，从而降低心理距离，促进非正式沟通和社交互动。

- rhetorical_function_cn：将理论与具体功能结合，形成机制链前半段。

- depends_on_cn：心理距离定义。

- sets_up_cn：为关系凝聚力理论解释互动结果做铺垫。

- evidence_pointer：Section 3.1 P2-P3

### 24. Section 3.2 P1-P2

- order：24

- section：Theory

- locator：Section 3.2 P1-P2

- move_code：THEORY_INTRO

- paraphrase_cn：关系凝聚力理论用于理解群体内互动及其后果，核心概念是关系凝聚力和承诺行为。

- rhetorical_function_cn：引入第二个理论。

- depends_on_cn：心理距离只解释互动产生，不能解释互动后果。

- sets_up_cn：说明社会纽带和边界界定两条路径。

- evidence_pointer：Section 3.2 P1-P2

### 25. Section 3.2 P3-P5

- order：25

- section：Theory

- locator：Section 3.2 P3-P5

- move_code：THEORY_PROPOSITION

- paraphrase_cn：反复社交互动通过积极情绪形成关系凝聚力、通过减少不确定性形成群体边界，最终导致承诺行为；跑步小组的共同参与可视为一种联合生产的共同产品。

- rhetorical_function_cn：具体化关系凝聚力理论在本研究情境中的运作。

- depends_on_cn：关系凝聚力理论的一般命题。

- sets_up_cn：为H1提供理论依据。

- evidence_pointer：Section 3.2 P3-P5

### 26. Section 3.2 P6-P7

- order：26

- section：Theory

- locator：Section 3.2 P6-P7

- move_code：THEORY_PROPOSITION

- paraphrase_cn：该理论最初用于二人交换结构，但可扩展到平等权力且成员能够与多数成员互动的完整网络中。

- rhetorical_function_cn：为将理论应用到自我组织跑步小组提供合法性。

- depends_on_cn：承接关系凝聚力理论介绍。

- sets_up_cn：解释跑步小组中权力平等的基本条件。

- evidence_pointer：Section 3.2 P6-P7

### 27. Section 3.3 P1-P3

- order：27

- section：Hypotheses

- locator：Section 3.3 P1-P3

- move_code：MECHANISM

- paraphrase_cn：作者认为Running Spot通过降低客观距离降低心理距离，促进线下随意群体参与，最终提高跑步参与；群规模和距离通过影响社会距离和物理距离来调节该效应。

- rhetorical_function_cn：将两个理论合为一体，预告调节变量。

- depends_on_cn：依赖心理距离与关系凝聚力理论的结合。

- sets_up_cn：引出H1-H3。

- evidence_pointer：Section 3.3 P1-P3

### 28. Section 3.3.1 P1-P5

- order：28

- section：Hypotheses

- locator：Section 3.3.1 P1-P5

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：跑步小组是自我组织的平等权力结构；Running Spot创造共同时间地点，增加反复社交互动，因此预计提高小组参与。H1：线下群体参与促进功能增加小组跑步参与。

- rhetorical_function_cn：正式提出主假设。

- depends_on_cn：综合前两节理论。

- sets_up_cn：作为后续DID检验的对象。

- evidence_pointer：Section 3.3.1; H1

### 29. Section 3.3.2 P1-P2

- order：29

- section：Hypotheses

- locator：Section 3.3.2 P1-P2

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：小组规模增大增加成员间社会距离和心理距离，且大组成员难以与多数人互动；H2：小组规模越小，Running Spot正向效应越强。

- rhetorical_function_cn：提出群规模调节假设。

- depends_on_cn：心理距离理论和关系凝聚力理论关于互动可达性的观点。

- sets_up_cn：对应Table 6的检验。

- evidence_pointer：Section 3.3.2; H2

### 30. Section 3.3.3 P1-P2

- order：30

- section：Hypotheses

- locator：Section 3.3.3 P1-P2

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：距跑步点太远增加物理距离和旅行成本，降低心理距离减少和到达意愿；H3：距跑步点越近，正向效应越强。

- rhetorical_function_cn：提出距离调节假设。

- depends_on_cn：心理距离和成本机制。

- sets_up_cn：对应Table 7的DDD检验。

- evidence_pointer：Section 3.3.3; H3

### 31. Section 4.1 P1-P3

- order：31

- section：Methods

- locator：Section 4.1 P1-P3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：选择该应用因为它用户量大、功能变化影响广泛，Running Spot上线形成准实验，且平台支持群组社交和线下活动。

- rhetorical_function_cn：说明研究情境选择的合理性。

- depends_on_cn：与研究问题相关。

- sets_up_cn：交代数据来源和外部效度基础。

- evidence_pointer：Section 4.1 P1-P3

### 32. Section 4.2 P1-P3

- order：32

- section：Methods

- locator：Section 4.2 P1-P3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：数据来自大连151个跑步小组38周周度面板，功能在第15周上线；收集到第38周因应用改变数据报告方式而停止。

- rhetorical_function_cn：描述面板数据和时间窗口。

- depends_on_cn：前一节情境选择。

- sets_up_cn：定义处理前/处理期以及后续DID。

- evidence_pointer：Section 4.2 P1-P3

### 33. Section 4.2 P4

- order：33

- section：Methods

- locator：Section 4.2 P4

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：根据是否曾出现在指定跑步点名单，将小组分为跑步点小组（处理组）和非跑步点小组（对照组）。

- rhetorical_function_cn：建立自然实验的处理/对照结构。

- depends_on_cn：平台提供的跑步点名单。

- sets_up_cn：定义了DID的关键变量SpotGroup。

- evidence_pointer：Section 4.2 P4

### 34. Section 4.3.1

- order：34

- section：Methods

- locator：Section 4.3.1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：小组参与度以每周实际参与跑步人数除以小组规模得到的活跃度来衡量。

- rhetorical_function_cn：解释因变量操作化。

- depends_on_cn：数据中含有每周参与人数和小组规模。

- sets_up_cn：后续回归以log(活跃度)为因变量。

- evidence_pointer：Section 4.3.1

### 35. Section 5 P1

- order：35

- section：Empirical Analysis

- locator：Section 5 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：采用DID方法，可以同时控制时间效应和组效应。

- rhetorical_function_cn：介绍总的分析策略。

- depends_on_cn：面板数据结构。

- sets_up_cn：主模型和后续检验。

- evidence_pointer：Section 5 P1

### 36. Section 5.1 P1-P4

- order：36

- section：Empirical Analysis

- locator：Section 5.1 P1-P4

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：作者验证平行趋势：时间和分组交互在处理前不显著，说明两组在功能上线前趋势相似。

- rhetorical_function_cn：为主DID提供识别有效性证据。

- depends_on_cn：DID假设。

- sets_up_cn：使后续因果解释有据。

- evidence_pointer：Section 5.1; Figure 3; Table 3

### 37. Section 5.2 P1-P4

- order：37

- section：Empirical Analysis

- locator：Section 5.2 P1-P4

- move_code：RESULT

- paraphrase_cn：DID模型显示SpotGroup×After系数显著为正，说明Running Spot确实提升跑步点小组的活跃度，H1得到支持。

- rhetorical_function_cn：报告主假设检验结果。

- depends_on_cn：平行趋势成立。

- sets_up_cn：引出PSM处理自选择问题。

- evidence_pointer：Section 5.2; Table 4 Models A1-A2

### 38. Section 5.2.1 P1-P3

- order：38

- section：Empirical Analysis

- locator：Section 5.2.1 P1-P3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：因处理/对照在预处理特征上存在差异，作者用PSM找出可观测特征相似的控制组。

- rhetorical_function_cn：阐述处理自选择问题及应对策略。

- depends_on_cn：Table 5显示的预处理差异。

- sets_up_cn：得到匹配样本后重新估计。

- evidence_pointer：Section 5.2.1; Table 5

### 39. Section 5.2.1 P4

- order：39

- section：Empirical Analysis

- locator：Section 5.2.1 P4

- move_code：RESULT

- paraphrase_cn：匹配后DID模型A3和A4中交互项仍显著为正，主效应稳健。

- rhetorical_function_cn：报告PSM后的结果。

- depends_on_cn：PSM匹配样本。

- sets_up_cn：为调节效应分析提供更可信样本。

- evidence_pointer：Section 5.2.1; Table 4 Models A3-A4

### 40. Section 5.3

- order：40

- section：Empirical Analysis

- locator：Section 5.3

- move_code：RESULT

- paraphrase_cn：三重交互SpotGroup×After×LargeGroup显著为负，说明大型小组中正向效果更弱，H2得到支持。

- rhetorical_function_cn：报告群规模调节检验。

- depends_on_cn：匹配样本。

- sets_up_cn：为理论边界讨论提供证据。

- evidence_pointer：Section 5.3; Table 6

### 41. Section 5.4

- order：41

- section：Empirical Analysis

- locator：Section 5.4

- move_code：RESULT

- paraphrase_cn：DDD结果显示，中等距离（1.2–3.7公里）的跑步点小组效果最大，过近和过远组效果弱或不显著，因此H3仅部分支持。

- rhetorical_function_cn：报告距离调节的非线性结果。

- depends_on_cn：距离分箱设定。

- sets_up_cn：为讨论边界的复杂性提供证据。

- evidence_pointer：Section 5.4; Table 7 Model A6

### 42. Section 5.5

- order：42

- section：Empirical Analysis

- locator：Section 5.5

- move_code：RESULT

- paraphrase_cn：动态DID显示效果在功能上线后先增后减，7–18周达到峰值，之后仍显著但减弱。

- rhetorical_function_cn：报告处理效应动态。

- depends_on_cn：连续处理期划分。

- sets_up_cn：为学习效应和长期衰减解释铺垫。

- evidence_pointer：Section 5.5; Table 7 Model A7

### 43. Section 5.6 P1-P5

- order：43

- section：Empirical Analysis

- locator：Section 5.6 P1-P5

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：多项稳健性检验显示：城区/郊区、无离线图片、不同初始活跃度、去除极端规模、控制天气后，主效应仍显著；排名和小组规模未受显著影响。

- rhetorical_function_cn：排除常见替代解释。

- depends_on_cn：主DID和匹配样本。

- sets_up_cn：增强因果主张的可信度。

- evidence_pointer：Section 5.6; Table 8

### 44. Section 5.6 P6-P8

- order：44

- section：Empirical Analysis

- locator：Section 5.6 P6-P8

- move_code：RESULT

- paraphrase_cn：Running Spot对计划性离线聚会人数、活动和比例的影响显著为负，说明活跃度提升不是来自应用内组织的离线聚会。

- rhetorical_function_cn：检验机制替代解释。

- depends_on_cn：匹配样本。

- sets_up_cn：支持“随意线下参与”而非“计划性聚会”的概念化。

- evidence_pointer：Section 5.6; Table 9

### 45. Section 6 P1

- order：45

- section：Discussion

- locator：Section 6 P1

- move_code：RESULT

- paraphrase_cn：作者重新概述：Running Spot通过促进反复互动提升小组活跃度，DID和PSM结果一致。

- rhetorical_function_cn：讨论开头总结核心发现。

- depends_on_cn：前述全部实证结果。

- sets_up_cn：展开理论和实践含义。

- evidence_pointer：Section 6 P1

### 46. Section 6.1 P2

- order：46

- section：Discussion

- locator：Section 6.1 P2

- move_code：CONTRIBUTION

- paraphrase_cn：本研究扩展了关系凝聚力理论，证明其在低任务相互依赖的自我组织跑步小组中仍可促进参与。

- rhetorical_function_cn：提出第一项理论贡献。

- depends_on_cn：主效应结果。

- sets_up_cn：将本文结果置于理论脉络中。

- evidence_pointer：Section 6.1 P2

### 47. Section 6.1 P3-P4

- order：47

- section：Discussion

- locator：Section 6.1 P3-P4

- move_code：CONTRIBUTION

- paraphrase_cn：本文通过整合心理距离视角补充了关系凝聚力理论中“如何增加反复互动”的未解问题。

- rhetorical_function_cn：提出第二项理论贡献。

- depends_on_cn：理论整合与实证结果。

- sets_up_cn：强调IT在促进离线互动中的独特作用。

- evidence_pointer：Section 6.1 P3-P4

### 48. Section 6.1 P5-P7

- order：48

- section：Discussion

- locator：Section 6.1 P5-P7

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：群规模和距离是重要边界条件，但这些边界主要适用于随意型线下群体参与，不同类型群体参与可能受到相反影响。

- rhetorical_function_cn：明确理论适用范围，避免过度泛化。

- depends_on_cn：群规模和距离调节结果。

- sets_up_cn：为未来研究提供边界性问题。

- evidence_pointer：Section 6.1 P5-P7

### 49. Section 6.1 P8-P9

- order：49

- section：Discussion

- locator：Section 6.1 P8-P9

- move_code：CONTRIBUTION

- paraphrase_cn：本文将健身技术研究从个体层面扩展到群体层面，并概念化线下群体参与促进功能，阐明IT如何促进线下群体参与。

- rhetorical_function_cn：总结群体层面与线下参与的贡献。

- depends_on_cn：主效应和稳健性证据。

- sets_up_cn：回应引言中的两个缺口。

- evidence_pointer：Section 6.1 P8-P9

### 50. Section 6.2

- order：50

- section：Discussion

- locator：Section 6.2

- move_code：PRACTICAL_STAKES

- paraphrase_cn：对跑步小组成员而言应利用支持反复社交互动的功能；对应用开发者应优先开发促进线下群体参与的功能，并采取措施弥补对计划性聚会的负面影响。

- rhetorical_function_cn：将研究结果转化为实践建议。

- depends_on_cn：主效应和离线活动负向结果。

- sets_up_cn：使研究对应用商具有行动指导意义。

- evidence_pointer：Section 6.2

### 51. Section 6.3

- order：51

- section：Discussion

- locator：Section 6.3

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：作者承认单一应用、非随机分组、未直接测量心理距离与社交互动等限制，建议未来做随机现场实验并测量机制变量。

- rhetorical_function_cn：主动声明研究边界与未来方向。

- depends_on_cn：全文研究设计和结果。

- sets_up_cn：保护贡献同时防止过度解读。

- evidence_pointer：Section 6.3

### 52. P1

- order：52

- section：Conclusions

- locator：P1

- move_code：CONTRIBUTION

- paraphrase_cn：结论重申Running Spot提高小组活跃度，并扩展关系凝聚力理论，建议应用提供促进随意社交互动的功能。

- rhetorical_function_cn：总结全文核心结果与启示。

- depends_on_cn：所有实证与理论讨论。

- sets_up_cn：为读者留下最终信息。

- evidence_pointer：Section 7

## 写作技术

- gap_construction_cn：先以市场规模和“健身技术最终目标是支持锻炼”建立实践重要性，再用“现有文献结果矛盾”制造张力；随后把矛盾归因于个体独自锻炼的困难，引入群体锻炼现象；最后将缺口明确为“缺乏群体层面研究”和“不清楚功能如何促进线下群体参与”两个学术缺口，并以“认识论上的we-ness”和“服务商需要扩大活跃用户”两个理由证明缺口重要。

- signposting_cn：论文大量使用显式路标：在引言中预告“五个贡献”；在文献综述末尾说“为了填补两个缺口，我们选择跑步应用并研究Running Spot”；在理论部分说明“心理距离解释互动产生，关系凝聚力解释互动后果”；在实证部分用“H1得到支持”“H2得到支持”“H3部分支持”标记假设状态。

- transition_logic_cn：段落间过渡通常先总结上一理论/实证阶段的局限，再引出下一阶段：心理距离只能解释互动产生，因此转到关系凝聚力；基础DID面临自选择，因此转PSM；主效应成立后，转边界条件；主结果稳健后，转替代机制检验。

- claim_evidence_rhythm_cn：每提出一个理论假设，后续立即安排对应表格与回归模型；结果段通常先报告估计系数和显著性，再解释其理论含义；稳健性部分用“虽然...但结果一致”保持节奏；讨论部分再用概括语句回收这些证据。

- benchmark_narrative_cn：benchmark不是算法数据集，而是“非跑步点小组”这一自然对照；论文用预处理平行趋势图展示对照组合理性，用PSM匹配进一步改造对照组；距离调节采用“>6.2公里组”为基线，动态分析用四个六周区间作为参照，使对比链条明确。

- theory_return_cn：讨论部分不是直接重复结果，而是将结果上升为对关系凝聚力理论适用边界、IT如何增加反复互动、群体层面健身技术效果以及线下群体参与概念的贡献；同时用“边界条件只适用于随意型线下参与”来细化理论适用范围。

- contribution_positioning_cn：作者反复使用“首次”“扩展”“补充”“揭示”等措辞，将贡献定位为理论语境化而非新造理论；通过整合两个已有理论，使研究在解释力上显得既有基础又有创新。

- novelty_protection_cn：用多重稳健性检验排除排名、新用户、天气、极端规模等机械解释；用负向离线活动结果证明效果不是计划性聚会所致；用“处理组可能在功能前已在同一地点跑步但活跃度未提升”来区分跑步点本身与功能可见性；承认效果随时间衰减但保持显著，避免一次性效果印象。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：用市场规模或现实现象建立背景，同时点出文献中的矛盾或不足。

- research_job_cn：确认领域内确实存在尚未解决且具有实践意义的问题，并将问题从个体层面扩展到群体/组织层面。

- required_evidence_cn：需要可靠的市场数据或行业报告，以及引用代表性研究之间的冲突结果。

- transition_to_next_cn：用“这一问题可通过群体视角获得独特理解”过渡到研究目标。

#### 2. 2

- step：2

- writing_job_cn：综述关键构念与相关文献，提出具体学术缺口，并说明缺口为什么重要。

- research_job_cn：精确界定要研究的概念（如线下群体参与促进功能），并区分其与已有概念（如在线参与、计划性聚会）的差异。

- required_evidence_cn：需要有可引用的文献分类、概念定义，以及一项足以证明“少有人做”的文献盘点表。

- transition_to_next_cn：用“为填补上述两个缺口”引出本文研究情境与具体功能。

#### 3. 3

- step：3

- writing_job_cn：选择一到两个理论，说明它们各自解释机制链的哪一段，并形成可检验假设。

- research_job_cn：建立从功能特性到心理机制再到群体行为结果的完整链条，必要时增加调节变量。

- required_evidence_cn：需要在理论命题基础上推导出可观察差异，并为每个假设铺垫实证对照。

- transition_to_next_cn：用“我们采用面板数据和准实验检验”进入方法。

#### 4. 4

- step：4

- writing_job_cn：详细描述数据来源、处理组/对照组构造、变量操作化与识别策略。

- research_job_cn：选择一个自然实验或准实验场景，收集面板或纵向数据；实施DID/PSM等因果推断方法。

- required_evidence_cn：需要预处理期数据、处理/对照分组信息，以及平行趋势和自选择检验。

- transition_to_next_cn：用“既然存在自选择，我们用PSM生成匹配样本”进入更稳健的估计。

#### 5. 5

- step：5

- writing_job_cn：报告主效应、调节效应、动态效应和稳健性；讨论部分回收理论缺口，并转化为理论和实践贡献。

- research_job_cn：针对每个主结果安排一种检验；通过替代因变量、子样本和机制变量排除竞争解释。

- required_evidence_cn：需要至少一种因果识别策略和多种稳健性检验；若声称机制，应尽量直接测量机制变量或至少提供排除性证据。

- transition_to_next_cn：从“结果稳健”过渡到“对理论和实践的启示”，并在结尾列明限制。

### most_transferable_moves_cn

1. 把已有文献的矛盾或缺口作为研究起点，并用“群体/组织层面不可化约为个体”增加新意

2. 将实际平台功能概念化为理论构念，明确限定其对应的概念维度

3. 用两种理论分别解释机制链的上下游，再合成为假设

4. 用自然实验加DID/PSM处理自选择，使二手平台数据具有因果解释力

5. 用替代因变量和负向结果排除替代机制

6. 在讨论中明确提出边界条件，并区分边界仅适用于某一类参与形式

### resource_intensive_or_nonstandard_parts_cn

1. 访问某大型跑步应用的内部/API面板数据，涵盖151个小组38周

2. 依赖平台在数据收集期间正式上线新功能形成的自然实验，研究者无法控制处理分配

3. 需要记录每个小组是否出现在指定跑步点名单，以及注册地址计算距离

4. 需要对城市内天气、季节、平台报告规则变化等外部条件有较长观测期

5. 平台后续改变数据报告方式迫使数据收集停止，这类权限和数据窗口并非可普遍获得

### what_not_to_copy_superficially_cn

1. 不能只写“我们用了DID”却没有平行趋势检验和PSM平衡检验

2. 不能直接把功能称为“线下群体参与促进功能”却不界定其维度和边界

3. 不能声称心理距离或关系凝聚力被验证，如果没有直接测量中间变量

4. 不能套用“中等距离最优”的非线性结论，除非有理论或数据进行支撑

5. 不能用“跑步点本身不解释效果”的排除法作为唯一证据，而不处理其他同期变化

6. 不能只做回归而不说明处理组/对照组定义、数据周期间隔和固定效应设置

- single_best_description_of_the_routine_cn：以群体现象和文献缺口为入口，用双理论构建从IT功能到心理机制再到行为结果的链条，借助平台真实功能上线作为准实验，用DID/PSM和边界调节做因果推断，最后通过稳健性检验和排除性证据把局部功能效果提升为可复用的理论贡献与设计启示。

## 分析边界

OCR文本中部分数学符号、变量名和个别句子以问号占位符呈现（如因变量操作化中的“??????????????????”），但主要章节、表格、图、假设和结果均可辨识，不影响分析结构和理论判断；本分析根据论文现有文本重建，未获得附录中完整理论机制图的细节。
