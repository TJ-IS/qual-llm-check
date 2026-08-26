# Real-Effort Incentives in Online Labor Markets: Punishments and Rewards for Individuals and Groups

- 作者：Matthew J. Hashim; Jesse C. Bockstedt
- 年份 / 期刊：2024 / MIS Quarterly
- DOI：10.25300/misq/2023/15166
- 源文件：04694_2024_real-effort-incentives-in-online-labor-markets-punishments-and-rewards-for-individuals-and-group.md
- 论文主类型：theory_derived_artifact_experiment
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.85

## 文章级论证概况

- 核心问题：在线劳动力市场中，平台外生地施加奖励或惩罚，以及将干预施加于个体或群体，哪一种能更有效地提升工人的真实努力？

- 制品与设计：一个基于公共物品博弈框架改写的真实努力协作图像标注实验平台。每组四名参与者共同为复杂模糊的图片打标签，组标签与Google Cloud Vision API基准标签的GloVe词向量余弦相似度决定群体绩效；每个工人收益等于个人收益乘数（初始90）乘以组相似度。在第6轮，系统按前五轮表现外生地改变乘数：全部提高为115（全员奖励）、全部降低为65（全员惩罚）、仅提高最高贡献者（个体奖励）、仅降低最低贡献者（个体惩罚），另有对照组不变。

- 客观结果：以标签数量衡量的努力在干预后显著提升：群体应用干预优于个体应用干预；全员奖励标签数最高，全员惩罚次高且显著提升努力；个体惩罚使被惩罚者本身显著增加标签，个体奖励对被奖励者无显著影响但未受奖励的组员显著增加；对照组无显著变化。

- 核心贡献：首次在真实努力协作在线劳动力任务中，用受控实验比较由信息系统外生执行的奖励/惩罚在个体/群体两个层级上的效果，表明平台作为社会规划者可以通过外生激励机制缓解搭便车，且惩罚群体和惩罚最差个体均产生与标准经济学预测相反的非显然正面效果。

- 整篇论证链：文章以AI/ML训练数据需要高质量人工标注为现实起点，指出在线劳动力市场作为信息系统具备监控和外部干预能力，但现有文献集中研究内生对等惩罚，对奖励以及外生系统干预的个体/群体对比研究很少。作者引入公共物品博弈理论，从标准理性均衡和异质收益函数文献推导出奖励（惩罚）会提升（降低）努力这一预测。为检验该预测，作者构建真实努力协作图片标注实验：收益由组标签与Google Cloud API基准的相似度决定，同时保留搭便车空间；第6轮按前五轮表现随机并外生地改变乘数，形成全员奖励、全员惩罚、个体奖励、个体惩罚和对照组五个条件。随机化平衡检验确认基线可比；组间随机效应回归显示第6-10轮治疗效应显著，且群体干预优于个体干预；组内双固定效应回归确认各治疗组在干预后显著增加标签而对照组不显著；子样本分析进一步发现，个体惩罚中被惩罚者显著提升努力，个体奖励中被奖励者却维持原有水平。讨论中作者将违逆理论预测的负面激励结果转译为管理设计知识：惩罚最差个体既能纠正目标者又向组内其他人发出信号，成为减少价值损害行为的可选策略，并给出平台政策建议、边界条件和未来研究方向。

## 类型与写作弧线判定

- 论文主类型判定：文章从公共物品博弈和异质性收益函数理论推导出明确的干预效果预测，并将这些预测转化为实验平台的具体设计差异——收益乘数在个体或群体层面升高或降低；随后通过受控在线实验直接检验这些设计差异的效果。因此属于由理论推导出制品/设计差异并加以实验检验的典型结构。

- 主导写作弧线判定：全文围绕“现实问题—理论预测—设计转化—实验检验—返回理论与实践含义”展开：引言从AI数据标注问题切入；理论背景建立公共物品博弈预测；实验设计将理论变量投射为处理；结果部分检验假设；讨论和结论将反直觉结果重新连接回理论并产出设计知识。没有采取benchmark为主的叙事，也不是多阶段设计科学框架。

## 研究开展程序

- study_or_phase_count：6

- 研究阶段总序列：第一阶段通过公共物品理论推导奖惩影响努力的预测；第二阶段构建真实努力协作图片标注平台并将理论变量转化为可操作处理；第三阶段通过随机化平衡检验和聚合图表建立内部效度与总体模式；第四阶段用组间面板回归比较处理后各组努力差异；第五阶段用组内双固定效应回归检验干预前后的个体变化；第六阶段聚焦个体处理条件中的子样本，区分被奖励/被惩罚者与未受影响组员的行为，为讨论中的设计和政策结论提供证据。

### studies_or_phases

#### 1. 理论建模与假设推导

- order：1

- name_cn：理论建模与假设推导

- question_cn：公共物品博弈理论和异质性收益函数文献对在线劳动力市场中的外在奖惩会预测怎样的努力变化？

- inputs_and_setting_cn：公共物品博弈实验文献、异质性收益函数实验文献以及在线劳动力市场真实努力研究。

- designed_or_compared_object_cn：奖励与惩罚、个体层与群体层的理论比较。

- baseline_control_or_counterfactual_cn：标准Nash均衡预测：纯搭便车，贡献趋近于零；重复博弈中贡献随时间衰减。

##### objective_metrics

（空）

- analysis_method_cn：文献综合、理论演绎。

- main_result_cn：提出H1：惩罚（奖励）个体会降低（提高）该个体努力；H2：惩罚（奖励）群体成员会降低（提高）每个成员的努力。

- argumentative_role_cn：为实验设计提供可证伪的理论预测，建立应当被检验的经济学基线。

- remaining_uncertainty_cn：理论没有考虑平台外生施加干预和组内异质收益函数同时存在的情况，也没有考虑真实努力任务的背景效应。

- link_to_next_phase_cn：预测需要实证检验，因此推动构建一个能同时操作奖励/惩罚和个体/群体因素的真实努力实验平台。

##### evidence_pointers

1. Theoretical Background and Hypotheses section, first three paragraphs

2. Hypotheses section, Hypothesis 1 and Hypothesis 2 statements

#### 2. 实验平台设计与处理构建

- order：2

- name_cn：实验平台设计与处理构建

- question_cn：如何将理论上的奖惩×个体/群体转换成一个现实、可信且保留搭便车空间的协作在线劳动力任务？

- inputs_and_setting_cn：协作图像标注众包任务；Google Cloud Vision API生成的基准标签；Stanford GloVe词向量；四人群组；伙伴匹配；10轮实验。

- designed_or_compared_object_cn：收益函数中的乘数a_i在第一阶段为90，第二阶段按处理变为115或65；处理条件为全员奖励、全员惩罚、个体奖励、个体惩罚、控制。

- baseline_control_or_counterfactual_cn：控制组维持乘数90不变，作为无干预的对照；第1-5轮作为各处理组自身的预处理基线。

##### objective_metrics

1. 努力：每轮每人标签数量

2. 绩效：组标签与Google Vision基准的GloVe余弦相似度

- analysis_method_cn：实验设计；相似度计算用50维GloVe平均向量与余弦相似度；支付用20点兑换1美元且随机抽取两轮支付以避免财富效应。

- main_result_cn：形成了五个可操作处理条件；两阶段设计允许平台按前五轮行为决定第六轮开始的乘数变化；参与者不知晓未来会被改变乘数。

- argumentative_role_cn：将抽象理论变量翻译为信息系统可执行的干预机制，同时保持公共物品博弈的逻辑结构。

- remaining_uncertainty_cn：平台设计是否真能诱发与理论一致的搭便车和努力差异仍有待随机化检验和统计分析确认。

- link_to_next_phase_cn：实验平台和随机分配程序是后续所有因果推断的基础。

##### evidence_pointers

1. Experiment Design, Procedures, and Treatments section

2. Treatment Design subsection

3. Experiment Procedure subsection

4. Treatment Implementation subsection and Table 1, Table 2

#### 3. 随机化验证与聚合结果检验

- order：3

- name_cn：随机化验证与聚合结果检验

- question_cn：参与者是否被成功随机分配到各处理？干预前基线是否可比？是否存在值得进一步检验的总体模式？

- inputs_and_setting_cn：184名参与者，164人进入分析（各处理组人数44/44/36/40/20）；第1轮相似度和标签数；人口统计年龄和性别。

- designed_or_compared_object_cn：各处理组在Round 1标签数和相似度，以及人口统计特征。

- baseline_control_or_counterfactual_cn：处理组之间在干预前的统计不可区分性作为随机化成功证据。

##### objective_metrics

1. Kruskal-Wallis检验统计量

2. 期均标签数

3. 期均相似度

- analysis_method_cn：Kruskal-Wallis检验；描述性统计；图2每轮平均标签数趋势。

- main_result_cn：第1轮不同处理的努力和相似度无显著差异，年龄和性别也无差异，随机化成立；图2显示第1-5轮各处理标签数较为接近，第6-10轮明显分离。

- argumentative_role_cn：建立实验的内部效度，并为后续回归分析提供总体视觉证据。

- remaining_uncertainty_cn：对照组在早期轮次的路径依赖使组间直接比较不完全可比；需要更正式的统计模型和组内分析。

- link_to_next_phase_cn：总体分离模式引出处理效应显著性检验需求，进入组间回归。

##### evidence_pointers

1. Results section, Aggregate Results subsection

2. Table 3

3. Figure 2

#### 4. 组间处理效应分析

- order：4

- name_cn：组间处理效应分析

- question_cn：在干预后的Rounds 6-10中，各处理条件的平均努力是否存在显著差异？

- inputs_and_setting_cn：Rounds 6-10的个体面板数据，164名参与者，820个观测。

- designed_or_compared_object_cn：处理指示变量，以全员奖励处理为回归基线；另一个模型包含所有轮次及处理×干预后交互项。

- baseline_control_or_counterfactual_cn：回归中全员奖励作为参照；交互模型以控制组和干预前阶段为参照。

##### objective_metrics

1. 标签数（因变量）

2. 处理回归系数

3. 交互项系数

4. Wald统计量

- analysis_method_cn：随机效应面板回归，参与者聚类稳健标准误，轮次固定效应；后估计交互项比较检验；Tobit和Poisson模型作为稳健性检验。

- main_result_cn：第6-10轮处理间差异显著，平均标签数排序为全员奖励>全员惩罚>个体惩罚≈个体奖励；个体处理的交互项显著低于全员奖励，且个体奖励与个体惩罚交互项统计上不可区分。

- argumentative_role_cn：证明干预方式本身而非随机噪声导致努力差异，确立了群体干预优于个体干预的总体结论。

- remaining_uncertainty_cn：组间分析未直接回答每个处理中个体在干预前后的变化幅度，也未区分个体处理中被标记个体与未标记个体的反应。

- link_to_next_phase_cn：需要组内分析以确认干预增量效应的大小。

##### evidence_pointers

1. Results section, Between-Subject Treatment Effects subsection

2. Table 4

#### 5. 组内处理效应分析

- order：5

- name_cn：组内处理效应分析

- question_cn：在同一处理条件下，个体在Rounds 6-10是否比Rounds 1-5显著改变标签贡献？

- inputs_and_setting_cn：每个处理的完整面板；全实验1600个观测（164人）；对照20人。

- designed_or_compared_object_cn：干预后虚拟变量（After intervention）在各自处理回归中的系数。

- baseline_control_or_counterfactual_cn：同一参与者在第1-5轮的自身标签数作为基线。

##### objective_metrics

1. After intervention系数

2. 参与者固定效应

3. 轮次固定效应

4. 调整R平方

- analysis_method_cn：双固定效应面板回归，按处理条件分列运行。

- main_result_cn：除对照组外，所有处理组的After系数均显著为正：全员奖励4.48**，全员惩罚2.82**，个体奖励1.42**，个体惩罚1.85**；对照组1.25不显著。

- argumentative_role_cn：隔离时间效应与干预效应，直接检验每个干预都提升了努力的主张，同时为后续个体层异质性分析提供必要前提。

- remaining_uncertainty_cn：个体处理中包含被标记者和未标记者两种人，需要子样本分析区分行为差异。

- link_to_next_phase_cn：子样本分析聚焦个体奖励和个体惩罚条件。

##### evidence_pointers

1. Results section, Within-Subject Treatment Effects subsection

2. Table 5

#### 6. 个体处理条件的子样本分析

- order：6

- name_cn：个体处理条件的子样本分析

- question_cn：在个体奖励和个体惩罚条件下，被系统标记的被奖励/被惩罚者与其他组员相比，努力变化有何不同？

- inputs_and_setting_cn：仅使用个体奖励和个体惩罚处理的数据；按被标记与否拆分样本；个体奖励处理36人（27未被奖励、10被奖励的进入回归），个体惩罚处理40人（30未被惩罚、10被惩罚的进入回归）。

- designed_or_compared_object_cn：被标记个体与未标记组员在干预前后的标签数变化。

- baseline_control_or_counterfactual_cn：同一子样本在Rounds 1-5的标签数；未标记组员作为对照。

##### objective_metrics

1. 子样本After intervention系数

2. 平均标签数变化值

3. 参与者和轮次固定效应

- analysis_method_cn：分样本双固定效应面板回归；表6描述性变化对比。

- main_result_cn：个体惩罚中被惩罚者After系数1.10†显著增加，且其平均标签增幅（0.94）约为未被惩罚者增幅（0.32）的三倍；个体奖励中被奖励者After系数1.11不显著，未被奖励者反而显著增加2.44**，两组平均增幅相近（0.49 vs 0.47）。

- argumentative_role_cn：揭示惩罚个体不仅能纠正被惩罚者，还向其他人传递信号；奖励个体则可能给被奖励者传递’做得太多’的信号，从而无法激励其继续提升。

- remaining_uncertainty_cn：信号解释、心理机制和群体规模等调节变量未被直接测量；需要讨论部分阐述边界条件与未来研究。

- link_to_next_phase_cn：子样本结果成为讨论和结论中设计政策建议的核心证据，并为未来机制研究提供入口。

##### evidence_pointers

1. Results section, Subsample Analysis of Individually Sanctioned/Rewarded Participants

2. Table 6

3. Table 7

## 各部分修辞架构

### abstract_moves

#### 1. 1

- move_code：CONTEXT

- description_cn：开篇指出在线劳动力市场和人工标注对AI/ML训练数据的关键作用。

#### 2. 2

- move_code：PRACTICAL_STAKES

- description_cn：强调仅依靠人力不够，关键在市场运营者如何通过干预激励人力。

#### 3. 3

- move_code：RQ_OR_OBJECTIVE

- description_cn：提出平台可在个体或群体层面施加奖励或惩罚以激励真实努力和产出。

#### 4. 4

- move_code：STUDY_OVERVIEW

- description_cn：说明采用协作图像标注实验（folksonomy）实施干预。

#### 5. 5

- move_code：RESULT

- description_cn：给出核心发现：群体干预优于个体干预；群体惩罚带来非显然的努力显著提升；个体奖励和惩罚效果相近。

#### 6. 6

- move_code：CONTRIBUTION

- description_cn：总结对在线劳动力市场运营者和带标签训练数据创建的指导意义。

### introduction_moves

#### 1. 1

- move_code：CONTEXT

- description_cn：用AI项目80%时间用于构建训练数据、数据错误破坏AI性能等证据确立人工标注重要性。

#### 2. 2

- move_code：PHENOMENON

- description_cn：在线劳动力市场天然是IS，平台可通过软件监控、测试和施加干预。

#### 3. 3

- move_code：CONTEXT

- description_cn：图像标注作为核心平台功能和folksonomy分类系统为实验提供自然依托。

#### 4. 4

- move_code：GAP

- description_cn：现有文献多研究内生惩罚，对奖励研究少，且未比较外生系统对不同市场参与者群体的奖惩效果。

#### 5. 5

- move_code：WHY_GAP_MATTERS

- description_cn：开放劳动力市场中监控并外生施加激励是IS的独特能力，因此这一缺口在IS中最值得研究。

#### 6. 6

- move_code：RQ_OR_OBJECTIVE

- description_cn：明确提出两个研究问题：谁外生奖励/惩罚更有效；应施加于个体还是群体。

#### 7. 7

- move_code：THEORY_INTRO

- description_cn：引入公共物品博弈作为建立理论预测的框架。

#### 8. 8

- move_code：STUDY_OVERVIEW

- description_cn：预告实验设计：群体图像标注、两阶段干预、随机化分配。

#### 9. 9

- move_code：RESULT

- description_cn：在引言末尾预览核心结果，包括反直觉的群体惩罚有效。

#### 10. 10

- move_code：STUDY_OVERVIEW

- description_cn：说明文章结构：文献、理论背景与假设、实验设计和程序、分析结果、讨论与政策建议。

### theory_and_knowledge_moves

#### 1. 1

- move_code：PRIOR_KNOWLEDGE

- description_cn：总结在线劳动力市场激励、众包、评论等IS文献中绩效薪酬和表扬的效果差异。

#### 2. 2

- move_code：THEORY_INTRO

- description_cn：介绍公共物品的定义和搭便车问题，并说明协作在线劳动中公共物品特征的存在。

#### 3. 3

- move_code：PRIOR_KNOWLEDGE

- description_cn：梳理Ostrom、Fehr & Gächter等关于惩罚维持合作的重要实验证据。

#### 4. 4

- move_code：MECHANISM

- description_cn：解释为何内生惩罚能维持合作而奖励通常效果较弱。

#### 5. 5

- move_code：GAP

- description_cn：指出IS中对真实努力、协作任务搭便车使用实验经济学方法的研究很少。

#### 6. 6

- move_code：WHY_GAP_MATTERS

- description_cn：在线劳动力市场的实操需要理解外生、平台执行的激励如何影响真实努力。

#### 7. 7

- move_code：THEORY_PROPOSITION

- description_cn：推导标准公共物品博弈中理性均衡预测为不做贡献，重复博弈中合作随时间衰减。

#### 8. 8

- move_code：LIMITATION

- description_cn：指出过去奖惩实验主要是内生（参与者互罚），收益函数异质性也是事先给定而非由系统对行为响应。

#### 9. 9

- move_code：HYPOTHESIS_OR_PROPOSITION

- description_cn：根据文献推导H1和H2：惩罚/奖励个体或群体分别降低/提高努力。

### artifact_design_moves

#### 1. 1

- move_code：REQUIREMENT

- description_cn：要求实验能模拟在线劳动力市场的信息系统能力：平台可以监控参与者的产出并外生施加干预。

#### 2. 2

- move_code：DESIGN_FEATURE

- description_cn：设计为四人群组、伙伴匹配、10轮真实图像标注，每轮无沟通但共享组标签列表。

#### 3. 3

- move_code：DESIGN_FEATURE

- description_cn：收益函数采用乘数乘以组相似度：u_i = a_i * Σg_j，保留搭便车空间。

#### 4. 4

- move_code：DESIGN_FEATURE

- description_cn：两阶段设计：前五轮建立基线，第六轮由系统按个体表现改变乘数，分别形成全员奖励、全员惩罚、个体奖励、个体惩罚和处理组。

#### 5. 5

- move_code：BENCHMARK_OR_CONTRAST

- description_cn：用Google Vision API生成基准标签，结合GloVe词向量相似度计算作为组绩效。

#### 6. 6

- move_code：METHOD_JUSTIFICATION

- description_cn：选择复杂模糊图像是为了使努力可观察且无法通过简单识别完成，从而保留搭便车空间。

#### 7. 7

- move_code：METHOD_JUSTIFICATION

- description_cn：随机选择两轮支付以避免财富效应，使每轮决策相互独立。

#### 8. 8

- move_code：DESIGN_FEATURE

- description_cn：第6轮信息只告知乘数因某成员图像标注有用性而改变，不事前透露机制，保持外生性。

### evaluation_moves

#### 1. 1

- move_code：METHOD_JUSTIFICATION

- description_cn：用Kruskal-Wallis检验确认Round 1相似度和标签数在各处理间无差异，年龄性别也无差异以支持随机化。

#### 2. 2

- move_code：METHOD_JUSTIFICATION

- description_cn：选择随机效应面板回归和双固定效应面板回归的理由：参与者随机分配、面板数据、控制时间和个体特征。

#### 3. 3

- move_code：RESULT

- description_cn：报告组间回归结果：Rounds 6-10处理间差异显著，排序为全员奖励、全员惩罚、个体惩罚、个体奖励。

#### 4. 4

- move_code：RESULT

- description_cn：报告组内回归结果：所有处理组干预后显著增加标签，对照组不显著。

#### 5. 5

- move_code：RESULT

- description_cn：报告子样本回归：被惩罚者显著增加标签，被奖励者不显著增加，未被标记组员在两种处理下都表现出一定提升。

#### 6. 6

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- description_cn：说明结果在Tobit（左截断1）和Poisson模型下一致，且对照组的路径依赖问题被单独处理。

### discussion_and_contribution_moves

#### 1. 1

- move_code：RESULT

- description_cn：总结整体结果：群体干预优于个体干预，所有干预均优于无干预。

#### 2. 2

- move_code：CONTRIBUTION

- description_cn：将全员惩罚提升努力、个体惩罚纠正被惩罚者的结果提炼为管理策略建议。

#### 3. 3

- move_code：BOUNDARY_CONDITION

- description_cn：指出并非所有激励适用于所有背景，干预不一定是成本中性的。

#### 4. 4

- move_code：CONTRIBUTION

- description_cn：提出平台可扮演社会规划者，在监控不当行为的同时动态执行奖惩。

#### 5. 5

- move_code：LIMITATION_AND_FUTURE

- description_cn：承认简化实验室设置限制外部效度，并提出群体规模、奖惩大小、信号机制、行为机制等未来问题。

#### 6. 6

- move_code：CONTRIBUTION

- description_cn：在结论中把“如何并向谁施加干预”提炼为一般设计知识。

## 理论/知识到设计的翻译

### 知识/理论基础

1. 公共物品博弈理论（Andreoni 1995; Fehr & Gächter 2000; Davis & Holt 1993 等）

2. 搭便车问题与内生惩罚实验研究（Ostrom 1992; Fehr & Gächter 2000; Sefton 2007; Andreoni 2003 等）

3. 异质性收益函数和公共物品实验（Fisher et al. 1995; Fischbacher et al. 2014）

4. 在线劳动力市场和真实努力任务文献（Charness et al. 2018; Benson et al. 2020; Fest et al. 2020）

5. 实验经济学方法论在IS研究中的应用（Gupta et al. 2018; Goes 2013）

- 理论—设计耦合：partial

- 耦合判定理由：核心设计因子（奖励/惩罚、个体/群体）和收益乘数变化直接由公共物品理论推导出来，假设检验也直接指向这些设计差异。然而，具体实验背景选择（图像标注、Google Vision API、GloVe相似度、以标签数衡量努力）主要来自在线劳动力任务的现实可行性和工程实现考虑，并非理论推导产物。因此理论决定了关键干预变量和预期，但没有完全决定整个制品的技术实现。

- 理论到设计翻译链：公共物品博弈中私人贡献的总和决定公共收益，个体搭便车可得最优 → 将贡献映射为图像标注努力、将公共收益映射为组标签相似度，将收益乘数作为平台可直接调控的政策杠杆 → 平台监控个体相似度，在第二阶段依据前五轮行为升高或降低乘数来外生施加奖励或惩罚 → 个体/群体如何被施加干预构成2×2处理设计 → 实验检验理论预测与实际行为差异。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：在公共物品博弈中，理性个体在重复互动中会减少贡献，趋向搭便车均衡。

- mechanism_cn：个人贡献属私人成本，公共收益由组共享，搭便车者的个人最优策略是不贡献或少贡献。

- design_requirement_cn：实验必须创造允许不贡献或低努力仍能获得部分收益的协作真实任务。

- artifact_choice_cn：四人群组共同标注同一图片，组收益由组标签与Google基准的相似度决定，个人收益=个人乘数×组相似度，即使少打标签也能分享组收益。

- evaluated_contrast_cn：干预条件与对照组的努力差异；重复五轮后基线是否衰减。

- objective_result_cn：对照组在Rounds 6-10无显著提升，支持搭便车/衰减预期；各干预组显著提高标签数。

##### evidence_pointers

1. Experiment Procedure section

2. Within-Subject Results Table 5 Control row

3. Discussion P1

#### 2. 2

- theory_or_knowledge_claim_cn：内生对等惩罚可有效维持公共物品合作，但奖励的效果通常较弱。

- mechanism_cn：惩罚直接降低被惩罚者的收益，促使其改变行为；奖励可能触发守规范行为但不一定持续提升贡献。

- design_requirement_cn：需要将惩罚从内生对等变为主体系统外生执行，并考察其与奖励的比较。

- artifact_choice_cn：系统在第六轮向全员降低乘数至65（全员惩罚）或提高至115（全员奖励），不依靠参与者互罚。

- evaluated_contrast_cn：全员奖励 vs 全员惩罚；外部执行机制相对于无干预的增量效应。

- objective_result_cn：全员奖励标签数最高；全员惩罚显著提升标签数（After系数2.82**），违逆理论预测。

##### evidence_pointers

1. Treatment Design subsection

2. Table 4

3. Table 5

4. Discussion P2

#### 3. 3

- theory_or_knowledge_claim_cn：异质收益函数中，收益低的个体贡献低，收益高的个体贡献高，但组内收益异质性不一定改变整体合作水平。

- mechanism_cn：个体根据自己面临的边际收益调整贡献；奖励提高收益预期，惩罚降低收益预期，因此应分别促进和抑制努力。

- design_requirement_cn：在组内对选定的个体设定不对称乘数，模拟平台对高/低贡献者的个别奖励/惩罚。

- artifact_choice_cn：个体奖励：仅将最高贡献者乘数提升至115；个体惩罚：仅将最低贡献者乘数降至65，其余人维持90。

- evaluated_contrast_cn：个体奖励 vs 个体惩罚；与被标记者 vs 未被标记者的行为差异。

- objective_result_cn：个体奖励和个体惩罚在第6-10轮平均标签数接近，统计上不可区分；子样本显示被惩罚者显著增加标签，被奖励者无显著增加。

##### evidence_pointers

1. Treatment Design subsection

2. Between-Subject Results Table 4

3. Subsample Results Table 7

4. Table 6

#### 4. 4

- theory_or_knowledge_claim_cn：在线劳动力市场中的真实努力可以被外在激励改变；不同激励类型的相对有效性存在争议。

- mechanism_cn：外在激励通过改变任务收益结构影响工人的努力投入和产出质量。

- design_requirement_cn：实验必须使用真实努力任务而非虚拟token决策，使努力成本和产出可测量。

- artifact_choice_cn：参与者实际输入标签词；努力以标签数量度量，而相似度保持为收益核心以避免单纯刷量；采用真实现金支付和实验室诚信规范。

- evaluated_contrast_cn：何种干预设计（目标层级）总能更有效地提升真实努力；干预内容是否影响个体决策。

- objective_result_cn：群体层干预显著提升努力，个体层干预也显著但幅度较小；任何干预都优于无干预。

##### evidence_pointers

1. Experiment Procedure section

2. Bottom paragraph of Between-Subject subsection

3. Discussion P1

## 评价逻辑

### evaluation_modes

1. 随机化平衡检验：使用Kruskal-Wallis检验比较Round 1标签数、相似度和人口特征在各处理间的差异。

2. 聚合趋势分析：图2和表3展示每轮平均标签数和相似度，直观呈现Rounds 1-5的不可区分和Rounds 6-10的分离。

3. 组间处理效应分析：随机效应面板回归，以处理指示变量为主要解释变量，包含轮次固定效应，并在全样本模型中引入处理×干预后交互项。

4. 组内处理效应分析：按处理条件分组的双固定效应面板回归，以After intervention虚拟变量为核心检验干预前后变化。

5. 子样本异质性分析：在个体处理条件中按被标记与否拆分样本，用双固定效应回归估计不同子群体的After系数。

6. 稳健性检验：用Tobit（左截断为1）和Poisson模型复核主要结果；对对照组早期路径依赖做单独说明。

- why_these_evaluations_cn：随机化平衡是因果推断的前提；聚合趋势提供直观模式；组间回归回答处理后处理间差异；组内回归区分时间效应与干预效应；子样本分析区分个体干预中被标记者和未标记者，解释总体平均效应背后的异质性；稳健性检验巩固结论，避免单模型偶然性。每一层评价解决下一层仍悬而未决的问题。

- benchmark_and_contrast_chain_cn：理论Nash均衡作为第一个基准：在无干预时努力应趋向搭便车；对照组作为无干预的实证基准；全员奖励作为组间回归的参照组，用于相对排序；个体处理中的未标记组员作为被惩罚/被奖励个体的对照；第1-5轮作为每个参与者自身的反事实。各基准依次被引入，使最终结论逐步从“干预是否有效”上升到“哪种层级、针对谁更有效”。

### claim_evidence_ledger

#### 1. 群体干预优于个体干预。

- claim_cn：群体干预优于个体干预。

- evidence_cn：组间回归显示以全员奖励为基准时，个体奖励交互项-1.71**、个体惩罚交互项-1.71**，两者均显著低于全员奖励；平均标签数排序也支持。

#### 2. 任何干预都比不干预好。

- claim_cn：任何干预都比不干预好。

- evidence_cn：组内双固定效应回归中所有处理组的After系数显著为正（1.42**到4.48**），对照组不显著。

#### 3. 惩罚群体能显著提高努力，与理论预测相反。

- claim_cn：惩罚群体能显著提高努力，与理论预测相反。

- evidence_cn：全员惩罚的After系数2.82**显著；在第6-10轮平均标签数高于个体处理。

#### 4. 惩罚个体能激励被惩罚者提升努力。

- claim_cn：惩罚个体能激励被惩罚者提升努力。

- evidence_cn：个体惩罚子样本中被惩罚者After系数1.10†，平均标签增幅0.94，远高于未被惩罚者的0.32。

#### 5. 奖励个体对被奖励者的激励效果不显著。

- claim_cn：奖励个体对被奖励者的激励效果不显著。

- evidence_cn：个体奖励子样本中被奖励者After系数1.11不显著；未被奖励者反而显著增加2.44**。

- internal_validity_strategy_cn：严格随机化过程（在线表单+电脑洗牌、一次实验只参加一次、oTree随机抽签）；伙伴匹配保持群体稳定；随机选择两轮支付避免财富效应；参与者不知会改变乘数，避免前摄期望效应；使用双固定效应和随机效应模型控制个体和轮次特征；Tobit和Poisson稳健性；控制组用于排除时间趋势。

- external_validity_strategy_cn：采用真实图片标注任务而非抽象token捐赠；收益与商业级Google Cloud Vision API基准挂钩；使用现金激励和标准实验室诚信协议；任务结构和报酬函数与在线劳动力市场中可监控、可干预的信息系统场景对应；结果与公共物品文献中已有的合作偏好和激励理论相连，增强可推广性。

- what_is_not_actually_tested_cn：未在真实商业在线劳动力平台上部署干预；未直接测量惩罚/奖励所触发的心理机制（报复、互惠、温暖之光、信号感知）；未操纵群体大小、奖惩绝对值或相对规模；未检验公共可见的惩罚是否真的对未受影响成员产生威慑；外部效度更多依靠实验设计与文献连接，而不是现场数据。

## 贡献闭环

- technical_claim_cn：在协作图像标注任务中，将收益乘数作为外部干预可显著改变标签数量衡量的努力水平；组间回归、组内回归和子样本分析均支持该主张。

- artifact_claim_cn：可识别的设计组成部分——乘数被提升或降低、作用于个体还是群体——是导致标签数变化的原因，而非时间、学习或回归因素。

- mechanism_claim_cn：平台干预通过收益结构变化影响参与者的行为决策：惩罚提高被惩罚者努力，奖励个体反而可能传递“做得太多”信号而抑制继续提升；未受影响组员的轻微提升被解释为信号效应。

- boundary_claim_cn：结论适用于可被信息系统监控与干预的在线劳动力市场和协作内容生产平台，尤其适用于真实努力、收益可分且存在搭便车空间的任务；不同群体规模、奖惩力度和任务类型可能改变结果。

- reusable_design_knowledge_cn：设计启示包括：应用干预总好于不干预；群体层干预通常比个体层干预更有效；若需针对个体，惩罚最差者比奖励最佳者更可能纠正行为且对群体发出警示信号；平台应尽量使激励与真实质量指标（如相似度）挂钩而非原始数量。

- theoretical_contribution_cn：将公共物品博弈的中奖励/惩罚预测从内生对等机制扩展到由信息系统外生施加的机制，填补了在线劳动力市场中真实努力协作任务下外生平台激励的实验空白，并表明在同一框架下负面激励可产生与理性均衡预测相反的结果。

- how_discussion_closes_intro_gap_cn：引言提出的缺口是惩罚已研究但奖励研究少、且未比较外生系统对个体与群体奖惩的效果。讨论和结论直接回应该缺口：用实验证明奖励和惩罚在两种层级上都有效，群体层优于个体层，并进一步指出惩罚最差个体的纠正和信号价值，从而将“向谁施加”和“如何施加”确立为核心设计维度。

- overclaim_or_unsupported_leaps_cn：讨论中“惩罚最差个体可能是最佳策略”的判断超出直接数据，因为实验只比较了四种固定条件，没有进行成本收益优化；将未受影响组员的轻微提升解释为“公众意识威慑”是推测性的，没有被直接检验；对被奖励者维持努力水平的“做得太多”信号解释也缺乏过程证据。

## 句级写作动作图谱

### 1. P1 S1

- order：1

- section：Abstract

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：在线劳动力市场和人工标注者对AI及监督式机器学习发展起到关键作用。

- rhetorical_function_cn：把研究对象置于AI大背景下，迅速确立重要性。

- depends_on_cn：无，直接开场。

- sets_up_cn：为后续提出平台干预问题铺设语境。

- evidence_pointer：Abstract first sentence

### 2. P1 S2

- order：2

- section：Abstract

- locator：P1 S2

- move_code：PRACTICAL_STAKES

- paraphrase_cn：仅有市场参与者的劳动还不够，理解市场运营者能利用哪些干预措施来激励人力是关键。

- rhetorical_function_cn：从背景升至现实痛点，说明研究动机。

- depends_on_cn：依赖前句关于在线劳动力市场重要性的设定。

- sets_up_cn：引出本文要研究的激励机制问题。

- evidence_pointer：Abstract second sentence

### 3. P1 S3

- order：3

- section：Abstract

- locator：P1 S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：提出平台可在个体或群体层面施加奖励或惩罚来激励真实努力和产出。

- rhetorical_function_cn：用一句概括研究方案并预告2×2设计。

- depends_on_cn：需要平台干预场景作为前提。

- sets_up_cn：为摘要下方研究问题做摘要式的铺垫。

- evidence_pointer：Abstract third sentence

### 4. P1 S4

- order：4

- section：Abstract

- locator：P1 S4

- move_code：STUDY_OVERVIEW

- paraphrase_cn：通过协作图像标注实验（folksonomy）应用这些干预。

- rhetorical_function_cn：预告研究方法与具体上下文。

- depends_on_cn：由奖励/惩罚、个体/群体研究方案直接过渡。

- sets_up_cn：为阅读者理解实验结果类型做铺垫。

- evidence_pointer：Abstract fourth sentence

### 5. P1 S5

- order：5

- section：Abstract

- locator：P1 S5

- move_code：RESULT

- paraphrase_cn：结果发现群体层干预优于个体层干预；惩罚群体产生非显然的努力显著提升；奖励和惩罚个体效果相近且都显著提升努力。

- rhetorical_function_cn：以高密度方式呈现核心经验发现，包括反直觉结果。

- depends_on_cn：前提是实验设计与阶段已经预告。

- sets_up_cn：呼应引言中的研究问题并吸引读者进入正文。

- evidence_pointer：Abstract fifth sentence

### 6. P1 S6

- order：6

- section：Abstract

- locator：P1 S6

- move_code：CONTRIBUTION

- paraphrase_cn：研究为在线劳动力市场运营者及带标签机器学习训练数据的激励设计提供指导。

- rhetorical_function_cn：给出实践含义，完成摘要闭环。

- depends_on_cn：以实验结果成立为前提。

- sets_up_cn：在正文中由结论部分继续展开政策启示。

- evidence_pointer：Abstract last sentence

### 7. P1 S1–S3

- order：7

- section：Introduction

- locator：P1 S1–S3

- move_code：CONTEXT

- paraphrase_cn：监督式机器学习依赖准确训练数据，人工标注占AI项目80%时间，错误数据导致AI性能受损。

- rhetorical_function_cn：用行业数据和具体危害建立研究背景。

- depends_on_cn：无。

- sets_up_cn：将在线劳动力市场的重要意义具体化，为干预需求埋线。

- evidence_pointer：Introduction first paragraph

### 8. P1 S4–S5

- order：8

- section：Introduction

- locator：P1 S4–S5

- move_code：PRACTICAL_STAKES

- paraphrase_cn：在线劳动力市场对AI关键，但核心问题在于理解市场运营者可依赖的干预措施。

- rhetorical_function_cn：从数据AI背景转向劳动力市场运营者决策。

- depends_on_cn：需要训练数据重要性作为前提。

- sets_up_cn：引出平台干预机制的研究目标。

- evidence_pointer：Introduction paragraph 1 sentences 4–5

### 9. P2 S1–S3

- order：9

- section：Introduction

- locator：P2 S1–S3

- move_code：PHENOMENON

- paraphrase_cn：在线劳动力市场本质上是信息系统，可通过软件监控、测试和管理干预。

- rhetorical_function_cn：强调IS的平台优势即将成为研究对象。

- depends_on_cn：需要前文在线劳动力市场对AI重要的前提。

- sets_up_cn：为“信息系统可监控并外生执行奖惩”这一独特贡献预埋伏笔。

- evidence_pointer：Introduction paragraph 2 sentences 1–3

### 10. P2 S4–S5

- order：10

- section：Introduction

- locator：P2 S4–S5

- move_code：MECHANISM

- paraphrase_cn：协调者或运营者可监控人类输出的努力与准确性，并外生引入干预来应对劳动力下降等问题。

- rhetorical_function_cn：具体说明平台干预可以借由监控、反馈和奖惩机制实现。

- depends_on_cn：需要信息系统可测试干预的前提。

- sets_up_cn：在理论与实验中引入外生干预概念。

- evidence_pointer：Introduction paragraph 2 last sentences

### 11. P3 S1–S3

- order：11

- section：Introduction

- locator：P3 S1–S3

- move_code：CONTEXT

- paraphrase_cn：图像标注是许多平台的核心功能，并为监督式ML及folksonomy等分类系统提供数据。

- rhetorical_function_cn：为用户劳动提供具体熟悉的应用场景。

- depends_on_cn：需要在线市场和AI训练数据的大背景。

- sets_up_cn：为实验选择协作图像标注作为研究环境提供论证。

- evidence_pointer：Introduction paragraph 3

### 12. P4 S1–S2

- order：12

- section：Introduction

- locator：P4 S1–S2

- move_code：GAP

- paraphrase_cn：已有研究一般考察使用内生惩罚纠正行为，但对奖励的研究很少，也未见比较作为外生系统的平台对不同市场主体的奖励和惩罚效果。

- rhetorical_function_cn：用对比方式暴露文献空白。

- depends_on_cn：需要前文关于内生惩罚文献的概括。

- sets_up_cn：为两个研究问题提供依据。

- evidence_pointer：Introduction paragraph 4

### 13. P4 S3–S4

- order：13

- section：Introduction

- locator：P4 S3–S4

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：监控劳动输出并外生施加激励是IS和在线劳动力市场的独特能力，在经济学文献中未得到系统研究。

- rhetorical_function_cn：使缺口不仅限于技术或经济学扩展，而是IS研究特定关切。

- depends_on_cn：需要依赖在线劳动力市场是IS这一前提。

- sets_up_cn：将论文贡献定位在IS、行为经济学和集体智慧的交汇处。

- evidence_pointer：Introduction paragraph 4 last sentences

### 14. P5 S1

- order：14

- section：Introduction

- locator：P5 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：提出研究问题：外生奖励还是外生制裁更能提升努力？为了最有效，应施加于个体还是群体？

- rhetorical_function_cn：用两个研究问题明确论文目标。

- depends_on_cn：需要前文缺口论证完整。

- sets_up_cn：直接导向实验设计。

- evidence_pointer：Introduction paragraph 5

### 15. P6 S1–S2

- order：15

- section：Introduction

- locator：P6 S1–S2

- move_code：THEORY_INTRO

- paraphrase_cn：通过实验经济学文献建立对各种奖惩的理论预测，再用协作图像标注实验检验这些干预的有效性。

- rhetorical_function_cn：说明理论预测和实验设计的先后关系。

- depends_on_cn：需要已提出两大研究问题。

- sets_up_cn：确定使用公共物品博弈框架作为理论基础。

- evidence_pointer：Introduction paragraph 6

### 16. P6 S3–S4

- order：16

- section：Introduction

- locator：P6 S3–S4

- move_code：DESIGN_FEATURE

- paraphrase_cn：实验通过修改公共物品博弈来模拟在线劳动力任务，在个体和群体层面实施奖励和惩罚（如扣发款项或发放奖金）。

- rhetorical_function_cn：概览干预在实验中的可操作化方式。

- depends_on_cn：需要以公共物品博弈框架为前提。

- sets_up_cn：预告正式实验设计的细节和两种层级干预。

- evidence_pointer：Introduction paragraph 6 last sentences

### 17. P7 S1–S3

- order：17

- section：Introduction

- locator：P7 S1–S3

- move_code：RESULT

- paraphrase_cn：结果发现群体层干预优于个体层；任何干预都比不做更好；群体惩罚显著提升平均努力，与预测相反；个体惩罚使最差者显著提升，个体奖励效果相似。

- rhetorical_function_cn：引言末尾预览重要且反直觉的结果。

- depends_on_cn：需要实验与干预设计已经预告。

- sets_up_cn：保持读者阅读兴趣，也为讨论结论提供悬念。

- evidence_pointer：Introduction paragraph 7

### 18. P8 S1–S2

- order：18

- section：Introduction

- locator：P8 S1–S2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：说明文章结构：文献综述、理论背景与假设、实验设计流程、分析结果、讨论与政策建议。

- rhetorical_function_cn：提供完整的阅读路线图。

- depends_on_cn：需要在引言中完成背景、缺口和预览。

- sets_up_cn：为正文各节顺序提供组织认知。

- evidence_pointer：Introduction last paragraph

### 19. Real-Effort Tasks and Online Labor Markets P1 S1–S4

- order：19

- section：Related Literature

- locator：Real-Effort Tasks and Online Labor Markets P1 S1–S4

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：IS中已有研究关注众包和在线评论中的激励设计，讨论工人激励和产出差异，并研究雇主声誉、训练和绩效薪酬等。

- rhetorical_function_cn：系统总结在线劳动力市场激励文献现状。

- depends_on_cn：需要引言中在线劳动力背景和干预问题。

- sets_up_cn：为指出奖励、外生干预和个人/群体层级的空白提供对比。

- evidence_pointer：Related Literature, first subsection

### 20. Real-Effort Tasks and Online Labor Markets P1 S5

- order：20

- section：Related Literature

- locator：Real-Effort Tasks and Online Labor Markets P1 S5

- move_code：LIMITATION

- paraphrase_cn：研究表明显性绩效薪酬提高产出而表扬等内在激励没有显著效果。

- rhetorical_function_cn：概括在线劳动力激励研究中一个主要结论。

- depends_on_cn：需要前面文献具体证据。

- sets_up_cn：与本文对奖励/惩罚外生干预的考察形成对照。

- evidence_pointer：Related Literature, first subsection

### 21. Public Goods and the Free-Rider Problem P1 S1–S2

- order：21

- section：Related Literature

- locator：Public Goods and the Free-Rider Problem P1 S1–S2

- move_code：THEORY_INTRO

- paraphrase_cn：当享用公共资源的人对其维护贡献不足时发生搭便车，公共物品具有非排他性和非竞争性。

- rhetorical_function_cn：引入公共物品定义和搭便车概念。

- depends_on_cn：无需依赖前面的具体文献回顾。

- sets_up_cn：将在线劳动协作中的低努力问题与公共物品文献连接。

- evidence_pointer：Related Literature, second subsection

### 22. Public Goods and the Free-Rider Problem P2 S1–S2

- order：22

- section：Related Literature

- locator：Public Goods and the Free-Rider Problem P2 S1–S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：从Ostrom、Yamagishi到Fehr和Gächter，大量实验研究考察奖励和惩罚对公共物品贡献的影响，内生对等惩罚尤其有效。

- rhetorical_function_cn：追溯奖惩实验的关键文献脉络。

- depends_on_cn：需要有公共物品和搭便车概念。

- sets_up_cn：为后面比较内生惩罚与外生平台干预提供学术背景。

- evidence_pointer：Related Literature, second subsection

### 23. Public Goods and the Free-Rider Problem P2 S3–S4

- order：23

- section：Related Literature

- locator：Public Goods and the Free-Rider Problem P2 S3–S4

- move_code：MECHANISM

- paraphrase_cn：内生化惩罚中参与者愿意承担个人成本去惩罚搭便车者；奖励在类似条件下通常不如惩罚有效。

- rhetorical_function_cn：解释内生惩罚有效的因果逻辑并评价奖励相对弱势。

- depends_on_cn：需要前面文献结论。

- sets_up_cn：为突出外生惩罚的差异和已有奖励结论奠定基础。

- evidence_pointer：Related Literature, second subsection

### 24. Public Goods and the Free-Rider Problem P3 S1–S3

- order：24

- section：Related Literature

- locator：Public Goods and the Free-Rider Problem P3 S1–S3

- move_code：MECHANISM

- paraphrase_cn：许多IS情境如维基百科、开源软件、论坛、P2P分享等具有公共物品特征；协作在线劳动同样面临搭便车。

- rhetorical_function_cn：将公共物品概念映射到IS领域。

- depends_on_cn：需要公共物品特征作为桥梁。

- sets_up_cn：为在线劳动力市场中的实验研究提供IS正当性。

- evidence_pointer：Related Literature, second subsection last paragraph

### 25. Real-Effort Tasks and the Free-Rider Problem in Experimental Economics P1 S1–S2

- order：25

- section：Related Literature

- locator：Real-Effort Tasks and the Free-Rider Problem in Experimental Economics P1 S1–S2

- move_code：GAP

- paraphrase_cn：IS研究中的真实努力和激励研究大多没有使用实验经济学方法，Gupta等人的评论呼吁在IS中采用此类方法。

- rhetorical_function_cn：点明方法论空白并引用MISQ编辑评论增强权威性。

- depends_on_cn：需要前面IS文献总结。

- sets_up_cn：使本文采用实验经济学方法成为对文献的直接回应。

- evidence_pointer：Related Literature, third subsection first paragraph

### 26. Real-Effort Tasks and the Free-Rider Problem in Experimental Economics P2 S1–S2

- order：26

- section：Related Literature

- locator：Real-Effort Tasks and the Free-Rider Problem in Experimental Economics P2 S1–S2

- move_code：GAP

- paraphrase_cn：现有IS搭便车实验多集中于数字盗版和众筹，未涉及真实努力协作平台中的奖励/惩罚。

- rhetorical_function_cn：明确具体领域空白，说明不同于前人。

- depends_on_cn：需要前面对盗版、众筹实验的介绍。

- sets_up_cn：将本文从盗版情境转向在线劳动力市场真实努力情境。

- evidence_pointer：Related Literature, third subsection second paragraph

### 27. end of Related Literature P1

- order：27

- section：Related Literature

- locator：end of Related Literature P1

- move_code：TRANSITION

- paraphrase_cn：与多数现有研究不同，本文将IS情境与实验经济学方法结合，设计受控实验，在协作任务中检验个体和群体层面的激励。

- rhetorical_function_cn：总结文献缺口并推进到理论假设部分。

- depends_on_cn：需要前文全部文献梳理。

- sets_up_cn：为理论背景和假设的正式建立提供逻辑出口。

- evidence_pointer：Final paragraph of Related Literature section

### 28. P1 S1–S2

- order：28

- section：Theoretical Background and Hypotheses

- locator：P1 S1–S2

- move_code：THEORY_INTRO

- paraphrase_cn：公共物品博弈是实证研究搭便车的主要范式，玩家选择将多少token投入公共账户，总和乘以因子后在成员间分配。

- rhetorical_function_cn：正式定义理论模型。

- depends_on_cn：需要文献中概念铺垫。

- sets_up_cn：支撑后续均衡推导和实验设计。

- evidence_pointer：Theoretical Background section first paragraph

### 29. P2 S1–S2

- order：29

- section：Theoretical Background and Hypotheses

- locator：P2 S1–S2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：假设理性自利个体，纳什均衡预测每个人都不贡献公共品，因为个人保留私有收益更优。

- rhetorical_function_cn：给出标准理论预测。

- depends_on_cn：需要公共物品博弈模型设定。

- sets_up_cn：为后面实际行为偏离Nash提供参照。

- evidence_pointer：Theoretical Background section second paragraph

### 30. P3 S1–S2

- order：30

- section：Theoretical Background and Hypotheses

- locator：P3 S1–S2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：单轮实验中纯Nash行为罕见，贡献通常位于帕累托最优与搭便车之间；重复博弈中合作衰减，逐渐接近Nash预测；惩罚引入则提高合作。

- rhetorical_function_cn：综合重复博弈的标准经验和惩罚作用。

- depends_on_cn：需要前面Nash均衡模型。

- sets_up_cn：为实验设计提供两阶段重复博弈的依据。

- evidence_pointer：Theoretical Background section third paragraph

### 31. Hypotheses P1 S1–S2

- order：31

- section：Theoretical Background and Hypotheses

- locator：Hypotheses P1 S1–S2

- move_code：MECHANISM

- paraphrase_cn：降低玩家收益增加搭便车，提高收益减少搭便车；异质收益函数使低收益者贡献少、高收益者贡献多。

- rhetorical_function_cn：整合收益函数与贡献行为之间的经验规律。

- depends_on_cn：需要前面公共物品理论和实验结论。

- sets_up_cn：为H1/H2提供理论机制。

- evidence_pointer：Hypotheses subsection first paragraph

### 32. Hypotheses P1 S3–S4

- order：32

- section：Theoretical Background and Hypotheses

- locator：Hypotheses P1 S3–S4

- move_code：LIMITATION

- paraphrase_cn：已有异质收益函数研究通常事先设定收益，而不是由平台按参与者事后行为外生地施加。

- rhetorical_function_cn：指出文献中的设计局限，强调本文创新。

- depends_on_cn：需要前一节关于Fisher、Fischbacher等文献的讨论。

- sets_up_cn：引出本文两阶段外生奖惩设计。

- evidence_pointer：Hypotheses subsection first paragraph

### 33. Hypotheses P2 S1–S2

- order：33

- section：Theoretical Background and Hypotheses

- locator：Hypotheses P2 S1–S2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：本文依据第一阶段搭便车行为确定谁将被系统在后续阶段奖励或惩罚，模拟平台对低质量贡献进行监控并施加突然收益损失。

- rhetorical_function_cn：解释外生奖惩的操作逻辑，将其与在线劳动力市场平台能力对齐。

- depends_on_cn：需要两阶段设计作为前提。

- sets_up_cn：为实验设计和干预消息具体制定提供依据。

- evidence_pointer：Hypotheses subsection second paragraph

### 34. Hypotheses P3 S1–S3

- order：34

- section：Theoretical Background and Hypotheses

- locator：Hypotheses P3 S1–S3

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：提出H1：惩罚（奖励）个体员工会降低（提高）该员工的努力；H2：惩罚（奖励）整个群体成员会降低（提高）每个员工的努力。

- rhetorical_function_cn：将理论机制转化为可检验假设。

- depends_on_cn：需要标准公共品预测和异质收益函数文献。

- sets_up_cn：为实验中处理效果检验提供明确目标。

- evidence_pointer：Hypotheses subsection, Hypothesis 1 and 2

### 35. P1 S1–S2

- order：35

- section：Experimental Design, Procedures, and Treatments

- locator：P1 S1–S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：本文采用公共品博弈框架，通过个体或群体层级的奖励/惩罚来探索在线协作劳动中的外在激励。

- rhetorical_function_cn：介绍实验的整体理论锚点。

- depends_on_cn：需要理论与假设章节的铺垫。

- sets_up_cn：为正式实验结构铺路。

- evidence_pointer：Experiment Design section first paragraph

### 36. P2 S1–S2

- order：36

- section：Experimental Design, Procedures, and Treatments

- locator：P2 S1–S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：四人群组通过电脑随机匿名分配，并采用伙伴匹配，参与者全程同一组。

- rhetorical_function_cn：说明分组和匹配方式。

- depends_on_cn：需要以两阶段设计为前提。

- sets_up_cn：支持惩罚/奖励需要行为因果链条延续的要求。

- evidence_pointer：Experiment Design section second paragraph

### 37. P2 S3–S4

- order：37

- section：Experimental Design, Procedures, and Treatments

- locator：P2 S3–S4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：不使用陌生人随机重配是因为两阶段设计需要行为从第一轮延续到第二轮，成员更换会无法执行对低/高贡献者的奖惩。

- rhetorical_function_cn：为伙伴匹配方法提供设计理由。

- depends_on_cn：需要两阶段设计这一前提。

- sets_up_cn：解释为何固定群体重要，并进而说明为什么采用四人群组。

- evidence_pointer：Experiment Design section second paragraph

### 38. P3 S1–S3

- order：38

- section：Experimental Design, Procedures, and Treatments

- locator：P3 S1–S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：每个参与者为图片标注词语，以四人组为单位但不知道组员个体贡献；收益由组贡献相似度决定，用公式u_i = a_i * Σg_j表示。

- rhetorical_function_cn：具体化个体收益与群体绩效的函数关系。

- depends_on_cn：需要公共物品收益结构作为理论模型。

- sets_up_cn：为后续乘数操作和相似度计算提供正式基础。

- evidence_pointer：Experiment Design section third paragraph and payoff equation

### 39. P4 S1–S2

- order：39

- section：Experimental Design, Procedures, and Treatments

- locator：P4 S1–S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：收益乘数a_i在治疗中后期被有意调整以模拟在线劳动力市场干预，且这些值始终不破坏公共品均衡预测。

- rhetorical_function_cn：说明乘数变化是外层干预的核心操作变量。

- depends_on_cn：需要公共品均衡预测作为约束前提。

- sets_up_cn：为Treatment Design具体定义乘数操作做铺垫。

- evidence_pointer：Experiment Design section fourth paragraph

### 40. Treatment Design P1 S1–S2

- order：40

- section：Experimental Design, Procedures, and Treatments

- locator：Treatment Design P1 S1–S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：两个因子——干预类型（惩罚/奖励）和应用层级（个体/群体）——组合成四种处理条件，另加一个无奖惩的控制条件。

- rhetorical_function_cn：正式定义2×2+控制的实验设计矩阵。

- depends_on_cn：需要理论中的奖惩和异质收益函数概念。

- sets_up_cn：为表1处理实施和假设检验建立框架。

- evidence_pointer：Treatment Design subsection first paragraph

### 41. Treatment Design P3 S1–S2

- order：41

- section：Experimental Design, Procedures, and Treatments

- locator：Treatment Design P3 S1–S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：个体奖励只提高组内最高贡献者的乘数至115，个体惩罚只降低最低贡献者的乘数至65，其余成员保持90。

- rhetorical_function_cn：具体给出个体层处理的精确操作规则。

- depends_on_cn：需要四组处理分类。

- sets_up_cn：支撑后续关于“被标记个体vs未标记组员”的分析。

- evidence_pointer：Treatment Design subsection formal definitions

### 42. Treatment Design P4 S1–S3

- order：42

- section：Experimental Design, Procedures, and Treatments

- locator：Treatment Design P4 S1–S3

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：与已有两阶段实验（Cadigan等、Dickinson）相比，本文既在同一框架中纳入个体和群体层激励，也不设置收益锚点或竞争性焦点，因此参与者的第一阶段策略更少受试验方法诱导。

- rhetorical_function_cn：用已有方法做基准，标明本文设计的独特之处。

- depends_on_cn：需要前文两阶段设计的引入。

- sets_up_cn：强调外生执行和未知性作为方法优势。

- evidence_pointer：Treatment Design subsection comparison paragraph

### 43. Treatment Design P5 S1–S2

- order：43

- section：Experimental Design, Procedures, and Treatments

- locator：Treatment Design P5 S1–S2

- move_code：MECHANISM

- paraphrase_cn：IS系统赋予平台所有者成为虚拟社会规划者的能力，可施加外生惩罚和奖励，这与传统实验场景显著不同。

- rhetorical_function_cn：将实验设计上升到IS能力与平台社会规划者角色。

- depends_on_cn：需要前文关于外生性设计。

- sets_up_cn：在讨论与结论中重新引用这一概念。

- evidence_pointer：Treatment Design subsection last paragraph

### 44. P1 S1–S3

- order：44

- section：Experiment Procedure

- locator：P1 S1–S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：图片刻意选择复杂和模糊的城市与自然场景，使努力可通过标签数量观察，且没有唯一正确答案，因而保留搭便车空间。

- rhetorical_function_cn：解释任务刺激物的选择依据。

- depends_on_cn：需要真实努力协作任务的设计需求。

- sets_up_cn：为努力衡量和搭便车机制提供具体任务条件。

- evidence_pointer：Experiment Procedure section first paragraph

### 45. P2 S1–S3

- order：45

- section：Experiment Procedure

- locator：P2 S1–S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：每轮向参与者提供个体相似度、群体相似度和收益；结束前五轮后随机引入处理，之后继续五轮；支付通过随机抽中的两轮计算。

- rhetorical_function_cn：描述实验轮次结构、信息反馈和支付制度。

- depends_on_cn：需要两阶段设计和乘数操作概念。

- sets_up_cn：为干预的时刻选择（第六轮）和收益对个体行为的影响建立程序基础。

- evidence_pointer：Experiment Procedure section second paragraph

### 46. P3 S1–S2

- order：46

- section：Experiment Procedure

- locator：P3 S1–S2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：随机抽取支付轮次避免财富效应，鼓励每轮独立经济理性决策。

- rhetorical_function_cn：为支付制度提供经济方法论依据。

- depends_on_cn：需要收益函数结构。

- sets_up_cn：增强结果因果解释的可信度。

- evidence_pointer：Experiment Procedure section third paragraph

### 47. P4 S1–S3

- order：47

- section：Experiment Procedure

- locator：P4 S1–S3

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：组标签列表与Google Cloud Vision API生成的标签结合70%置信度阈值进行相似度计算；相似度越高收益越高，同时个人低努力可被团队掩盖。

- rhetorical_function_cn：引入外部客观基准，同时确证搭便车可能性。

- depends_on_cn：需要协作标注的任务结构。

- sets_up_cn：为GloVe相似度计算和收益公式提供技术路径。

- evidence_pointer：Experiment Procedure section fourth paragraph

### 48. P5 S1–S3

- order：48

- section：Experiment Procedure

- locator：P5 S1–S3

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：使用来自Wikipedia和Gigaword训练的GloVe词向量和gensim，将标签转换为50维向量后计算余弦相似度，作为组或个体与API标签的匹配度。

- rhetorical_function_cn：解释相似度算法的具体实现。

- depends_on_cn：需要Google Vision基准作为技术前提。

- sets_up_cn：为fig1流程和后续指标（相似度、标签数）提供测量基础。

- evidence_pointer：Experiment Procedure section fifth paragraph

### 49. P6 S1–S3

- order：49

- section：Experiment Procedure

- locator：P6 S1–S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：组相似度决定潜在收益，实际收益等于个人收益乘数乘以组相似度。

- rhetorical_function_cn：将相似度转为收益并强调乘数作用。

- depends_on_cn：需要公共品收益公式。

- sets_up_cn：为后续乘数变化成为干预杠杆提供直接基础。

- evidence_pointer：Experiment Procedure section sixth paragraph and payoff equation

### 50. P1 S1–P2 S2

- order：50

- section：Treatment Implementation

- locator：P1 S1–P2 S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：第6轮开始时系统突然显示信息，告知全员或某一成员因某组员的图像标注有用性而改变乘数，且参与者事前不知将来乘数会变。

- rhetorical_function_cn：描述干预触发点和信息内容结构。

- depends_on_cn：需要两阶段设计和处理矩阵。

- sets_up_cn：为解释干预信号如何被参与者感知提供依据，并支撑外生性主张。

- evidence_pointer：Treatment Implementation subsection and Table 2

### 51. P1 S1–P2 S2

- order：51

- section：Sample and Process for Treatment Assignment

- locator：P1 S1–P2 S2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：实验在Emory University行为实验室用oTree进行，184名学生参与，每个session仅一组四人，通过在线登记和时间随机化分配处理。

- rhetorical_function_cn：说明招募规模、实验工具和随机分配流程。

- depends_on_cn：需要实验流程设计完整。

- sets_up_cn：为样本统计分析和随机化平衡检验提供信息。

- evidence_pointer：Sample and Process for Treatment Assignment section

### 52. Aggregate Results P1 S1–S2

- order：52

- section：Results

- locator：Aggregate Results P1 S1–S2

- move_code：RESULT

- paraphrase_cn：第1轮的相似度和标签数在各处理间没有显著差异，人口特征也没有差异，说明随机化成功。

- rhetorical_function_cn：报告随机化平衡检验，建立内部效度。

- depends_on_cn：需要随机分配和样本数据。

- sets_up_cn：为后续所有因果比较提供可信前提。

- evidence_pointer：Aggregate Results subsection first paragraph and Kruskal-Wallis tests

### 53. Aggregate Results P2 S1–S3

- order：53

- section：Results

- locator：Aggregate Results P2 S1–S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用标签数量衡量努力，因为收益与相似度挂钩而非标签数，因此标签数更能反映付出且不易被刷量操纵。

- rhetorical_function_cn：解释因变量选择理由。

- depends_on_cn：需要实验激励结构。

- sets_up_cn：为后续所有回归中的因变量定义做辩护。

- evidence_pointer：Aggregate Results subsection second paragraph

### 54. Aggregate Results P3 S1–S2

- order：54

- section：Results

- locator：Aggregate Results P3 S1–S2

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：对照组的早期平均努力受路径依赖影响，因此不同处理的预处理阶段不完全直接可比，但对照组仍可作为组内分析的参照。

- rhetorical_function_cn：对对照组特殊路径依赖进行方法性说明，避免误导。

- depends_on_cn：需要图2和表3的聚合结果。

- sets_up_cn：强调组内分析的重要性，并解释为何组间直接比较需谨慎。

- evidence_pointer：Aggregate Results subsection third paragraph

### 55. Aggregate Results P4 S1–S2

- order：55

- section：Results

- locator：Aggregate Results P4 S1–S2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：选择随机效应面板回归是因为面板数据结构、随机分配以及治疗与个体固定效应共线的问题；同时纳入轮次固定效应。

- rhetorical_function_cn：说明统计分析工具选择理由。

- depends_on_cn：需要随机分配和前文数据。

- sets_up_cn：为表4回归结果提供方法论支撑。

- evidence_pointer：Aggregate Results subsection final paragraph

### 56. Between-Subject Treatment Effects P1–P3

- order：56

- section：Results

- locator：Between-Subject Treatment Effects P1–P3

- move_code：RESULT

- paraphrase_cn：第6-10轮处理后组间回归显示处理间差异显著；以全员奖励为基准，个体奖励、个体惩罚处理的交互项显著更低，全员惩罚差异较小；排序为全员奖励>全员惩罚>个体惩罚≈个体奖励。

- rhetorical_function_cn：报告组间处理效应主结果。

- depends_on_cn：需要随机效应面板模型和表4。

- sets_up_cn：支持群体干预优于个体干预的核心结论。

- evidence_pointer：Between-Subject Treatment Effects subsection and Table 4

### 57. Between-Subject Treatment Effects P4

- order：57

- section：Results

- locator：Between-Subject Treatment Effects P4

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：交互项的组间比较均显著（除个体奖励和个体惩罚之间），结果在Tobit和Poisson模型中一致。

- rhetorical_function_cn：提供补充稳健性证据。

- depends_on_cn：需要主回归模型有效。

- sets_up_cn：增强结论的模型依赖性弱化。

- evidence_pointer：Between-Subject Treatment Effects subsection and robustness sentence

### 58. Within-Subject Treatment Effects P1–P3

- order：58

- section：Results

- locator：Within-Subject Treatment Effects P1–P3

- move_code：RESULT

- paraphrase_cn：组内双固定效应回归显示各处理组在干预后显著增加标签数，对照组不显著；全员奖励增幅最大，全员惩罚其次，个体干预增幅较小。

- rhetorical_function_cn：报告干预前后对比的组内结果，区分时间效应和干预效应。

- depends_on_cn：需要前一节组间差异证据。

- sets_up_cn：确认每项干预确实对行为产生增量，为子样本异质性分析打下基础。

- evidence_pointer：Within-Subject Treatment Effects subsection and Table 5

### 59. Subsample Analysis P1–P3

- order：59

- section：Results

- locator：Subsample Analysis P1–P3

- move_code：RESULT

- paraphrase_cn：在个体处理条件下，被惩罚者平均标签增幅约为未惩罚组员的三倍；被奖励者增幅与未奖励组员相似，回归显示被惩罚者增长略显著、被奖励者不显著。

- rhetorical_function_cn：呈现异质性证据并揭示处理效果并非平均分布。

- depends_on_cn：需要组内主结果成立。

- sets_up_cn：为讨论中关于信号效应和惩罚个体正确性的论述提供核心支撑。

- evidence_pointer：Subsample Analysis subsection and Table 6, Table 7

### 60. General Implications P1 S1–S2

- order：60

- section：Discussion and Conclusion

- locator：General Implications P1 S1–S2

- move_code：CONTRIBUTION

- paraphrase_cn：全员惩罚是最具争议的激励策略，却带来非显然的努力显著提升，减少了对他人努力的搭便车。

- rhetorical_function_cn：提出反直觉结果作为核心设计知识。

- depends_on_cn：需要组内和组间分析证据。

- sets_up_cn：将实验发现转化为可供平台决策的启示。

- evidence_pointer：Discussion, General Implications first paragraph

### 61. General Implications P2 S1–S2

- order：61

- section：Discussion and Conclusion

- locator：General Implications P2 S1–S2

- move_code：CONTRIBUTION

- paraphrase_cn：只惩罚最差个体可能成为减少在线劳动力市场中价值损害行为的最佳策略，因为能纠正目标者并向群体发出信号。

- rhetorical_function_cn：将子样本分析结果推广为具体管理策略建议。

- depends_on_cn：需要子样本分析和信号解释。

- sets_up_cn：引出平台作为社会规划者的建议。

- evidence_pointer：Discussion, General Implications second paragraph

### 62. General Implications P3 S1–S2

- order：62

- section：Discussion and Conclusion

- locator：General Implications P3 S1–S2

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：全员奖励会持续提高努力，但要奖励所有成员不能只奖励个人；只奖励最佳者可能向被奖励者传达他们做得过多，从而抑制继续提升。

- rhetorical_function_cn：对奖励目标的机制给出推测性边界，限定设计启示。

- depends_on_cn：需要个体奖励子样本不显著的结果。

- sets_up_cn：提醒平台对奖励信号的权衡，避免过度泛化。

- evidence_pointer：Discussion, General Implications third paragraph

### 63. General Implications P4 S1–S2

- order：63

- section：Discussion and Conclusion

- locator：General Implications P4 S1–S2

- move_code：CONTRIBUTION

- paraphrase_cn：IS所有者可以像社会规划者一样监控行为并动态执行用户奖惩，前提是干预并非对所有组织或情境都中性或适用。

- rhetorical_function_cn：将研究提升为平台治理的一般性愿景，同时加入边界条件。

- depends_on_cn：需要实验证据和前述策略建议。

- sets_up_cn：为限制条件与未来研究方向铺垫。

- evidence_pointer：Discussion, General Implications fourth paragraph

### 64. P1 S1–S2

- order：64

- section：Limitations and Future Research

- locator：P1 S1–S2

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：实验是受控随机化实验，简化了真实在线劳动力协作任务；虽然并非所有干预都适用于所有情境，但简化可避免混淆因素并保证因果推断。

- rhetorical_function_cn：承认方法限制但维护其因果有效性。

- depends_on_cn：需要前面全部实验设计理由。

- sets_up_cn：为讨论未来扩展提供辩证平衡。

- evidence_pointer：Limitations and Future Research first paragraph

### 65. P2 S1–S2

- order：65

- section：Limitations and Future Research

- locator：P2 S1–S2

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：群体规模、奖惩大小相对收益、支付同步性等都可能改变行为；未来实验可操纵这些参数。

- rhetorical_function_cn：指出关键调节变量，引导未来研究。

- depends_on_cn：需要当前实验固定了群体规模、奖惩额度等。

- sets_up_cn：为后续学者扩展研究工作提供具体方向。

- evidence_pointer：Limitations and Future Research second paragraph

### 66. P3 S1

- order：66

- section：Limitations and Future Research

- locator：P3 S1

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：未来研究可进一步识别被奖惩时的行为机制，如报复、互惠、温暖之光等。

- rhetorical_function_cn：把结果背后的机制问题进一步往前推。

- depends_on_cn：需要当前结果停留在行为层而非机制层。

- sets_up_cn：勾画理论深化路径。

- evidence_pointer：Limitations and Future Research third paragraph

### 67. P1 S1–S2

- order：67

- section：Conclusion

- locator：P1 S1–S2

- move_code：CONTRIBUTION

- paraphrase_cn：研究表明干预的“如何”和“向谁”强烈影响最终行为，在线劳动力市场可利用平台监控和外生奖惩来缓解搭便车，支持AI和机器学习所需准确数据集。

- rhetorical_function_cn：将具体发现浓缩为普适性知识主张，并回扣AI数据质量开头。

- depends_on_cn：需要全部实验证据和文献背景。

- sets_up_cn：为读者留下整体结论，完成闭环。

- evidence_pointer：Conclusion first paragraph

### 68. P2 S1–S2

- order：68

- section：Conclusion

- locator：P2 S1–S2

- move_code：CONTRIBUTION

- paraphrase_cn：信息系统和在线平台具备独特能力，可以监控行为并外生实施政策，以解决在线劳动等公共贡献中的搭便车问题。

- rhetorical_function_cn：再次强调IS平台的独特角色，升华理论视角。

- depends_on_cn：需要前文实验设计和政策讨论。

- sets_up_cn：为文章整体贡献做最后定位。

- evidence_pointer：Conclusion final paragraph

## 写作技术

- gap_construction_cn：先用内生惩罚文献（Fehr & Gächter等）确立人们对惩罚影响合作的常识，接着指出外生系统执行、平台监测能力以及奖励与群体/个体层级对比都未被研究，从而构造出“文献未回答平台运营者应如何选择激励”的缺口。再通过引用Gupta等的方法论呼吁，把这一缺口归入IS领域。

- signposting_cn：在引言和讨论中反复使用“我们提出…”“我们研究问题…”“我们开展了…”，并专门列出一段说明文章结构；各小节标题和段落首句常先预告要解决什么问题，再进入方法或数据，读者容易追踪论证线。

- transition_logic_cn：理论部分以“标准预测…但本文不同”形成张力；实验结果按研究问题顺序推进：从聚合到组间到组内再到子样本，每次转向都由上一段遗留的“尚未回答的问题”触发；讨论则从实验结果逐条反向回到引言中的管理问题和理论预测。

- claim_evidence_rhythm_cn：每个主要主张后面紧跟相应表或回归系数，形成“主张—表—解释—下一主张”的节奏；回归结果先用文字解释系数幅度和显著性，再用表4/表5/表7支持。特别地，反直觉结论在摘要和引言都先以“surprisingly”形式亮相，再在结果部分用统计证据补齐。

- benchmark_narrative_cn：基准故事主要由三层构成：标准Nash均衡作为理论基准、对照组作为无干预基准、全员奖励作为相对处理基准。理论基准被用来突出全员惩罚和个体惩罚结果的非显然性；对照组作为组内反事实；全员奖励作为组间比较排序的参照，帮助读者快速看到群体层干预优于个体层干预。

- theory_return_cn：讨论部分没有止步于“干预有效”，而是将结果反向链接到公共物品博弈的预测：指出Nash均衡预测下降但我们观察到惩罚群体提高努力，并用“信号”和“做得太多”等机制解释个体奖励的非效果；结论中用“如何与向谁”重新概括理论主张，强调干预目标层级比单纯奖惩类型更重要。

- contribution_positioning_cn：通过声称“首次”将外生执行的惩罚/奖励与个体/群体层级相结合的开发劳动力市场实验、并回应MISQ方法论呼吁来定位贡献；在贡献段落中同时区分技术结果与设计启示，使贡献不被视为单一实验的一次性发现。

- novelty_protection_cn：通过强调外生执行、平台监控、真实努力任务、新颖的2×2组合以及反直觉的群体惩罚结果来避免退化为一次性性能比较；并在讨论中把发现落回公共物品理论和平台治理的一般能力，使其从具体实验条件上升为设计知识。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：用现实痛点（如AI训练数据质量、平台劳动激励）建立研究背景，并给出关键统计或案例。

- research_job_cn：识别IS情境中具有普遍性和实践影响的行为问题。

- required_evidence_cn：可靠的行业统计、新闻报道或IS领域被广泛承认的现象描述。

- transition_to_next_cn：由现实背景转向“平台可通过IS机制干预”的能力介绍。

#### 2. 2

- step：2

- writing_job_cn：系统综述相关理论文献（如公共物品、内生惩罚、异质收益），找出现有研究的共同假设和局限。

- research_job_cn：判断理论预测与真实IS情境之间的张力，确定外生平台干预这一空白。

- required_evidence_cn：若干核心文献的可泛化结论，以及这些结论未能覆盖的特定维度。

- transition_to_next_cn：由“没有研究X”过渡到“本文研究X”，并给出研究问题。

#### 3. 3

- step：3

- writing_job_cn：将理论命题转化为可操作实验设计，明确变量、处理水平、对照和因变量。

- research_job_cn：构建满足理论与实际约束的平台或任务（如协作标注、收益乘数操作），并进行预试验。

- required_evidence_cn：处理设计能对应理论构念，因变量可客观测量且不受平台设计诱导操纵。

- transition_to_next_cn：从设计描述转向程序执行和样品说明。

#### 4. 4

- step：4

- writing_job_cn：用明确程序说明随机化、样本、实验步骤和信息呈现，确保可复制。

- research_job_cn：实际运行受控实验，记录处理分配和参与者行为数据。

- required_evidence_cn：随机化流程文档、样本量、每处理样本构成、实验环境与支付机制。

- transition_to_next_cn：由实验程序进入结果部分。

#### 5. 5

- step：5

- writing_job_cn：按“随机化验证—聚合—组间—组内—子样本”层级逐层报告统计结果。

- research_job_cn：执行符合数据结构的回归模型，进行稳健性检验（如Tobit、Poisson）。

- required_evidence_cn：基线平衡检验、主回归表、稳健性说明，以及处理内/子组的对比证据。

- transition_to_next_cn：由结果转向讨论，将统计发现上升为机制和政策含义。

#### 6. 6

- step：6

- writing_job_cn：在讨论中重新连接引言中的问题与理论预测，把反直觉结果提炼为设计知识，并给出边界条件和未来研究方向。

- research_job_cn：根据证据强度和局限条件区分核心结论与推测机制，避免过度泛化。

- required_evidence_cn：对每项能够声称的设计知识点拥有至少一个相应统计结果的支撑；对未检验机制使用推测语言。

- transition_to_next_cn：以总结性结论收尾，回到开头的现实意义。

### most_transferable_moves_cn

1. 基于真实任务背景构建劳动力工具实验，使理论概念以可测量行为指标落地。

2. 把现有文献“熟悉”的结果（如内生惩罚有效）作为基准，再通过新维度（外生系统、个体/群体层级）制造增量贡献。

3. 使用“理论预测—反直觉发现”的修辞结构来吸引读者，并通过统计回归提供充分检验。

4. 结果报告遵循从聚合到组间到组内再到子样本的递进，使每一层分析服务于上一层留下的问题。

5. 在讨论中把政策或设计建议与具体表/回归结果或未来机制研究适度连接。

### resource_intensive_or_nonstandard_parts_cn

1. 受控实验平台（oTree）和真实图片标注任务的开发与调试。

2. 使用Google Cloud Vision API和GloVe词向量进行相似度计算的技术集成。

3. 行为实验室招募学生并支付现金的实验基础设施。

4. 两阶段设计需要保证伙伴匹配和远程参与中的可靠性。

### what_not_to_copy_superficially_cn

1. 若没有真实的受控实验和随机分配，不能仅靠“实验发现惩罚群体有效”一句作为贡献而被视为因果证据。

2. 不能在没有外生执行、没有收益乘数变化、也没有协作搭便车空间的情况下声称惩罚或奖励的有效性可推广。

3. 不可把“最差者惩罚是最佳策略”当作普遍设计原则照搬，因为该结论受群体规模、任务类型、奖惩大小等边界限制。

- single_best_description_of_the_routine_cn：将成熟公共品理论转译为可由信息系统外生执行的实时协作任务，通过随机对照实验在不同层级干预中检验理论预测，再用组间/组内/子样本面板回归建立因果结论，并在讨论中将反直觉结果上升为平台设计和管理知识。

## 分析边界

由于文章未提供页边编号，所有位置证据采用章节/小节名和段落顺序作为定位依据；图2、表1—表7的细节基于论文中可读文本和视觉元素推断；附录A和附录B原文完整给予了图片示例和实验说明，但未对其进行逐句代码分析。分析基于全文结构、处理定义、结果叙述和讨论部分完成，未假设任何缺失数据。
