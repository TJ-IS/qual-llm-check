# Contextual Targeting in mHealth Apps: Harnessing Weather Information and Message Framing to Increase Physical Activity

- 作者：Nakyung Kyung; Jason Chan; Sanghee Lim; Byungtae Lee
- 年份 / 期刊：2024 / Information Systems Research
- DOI：10.1287/isre.2020.0119
- 源文件：26551_2024_contextual-targeting-in-mhealth-apps-harnessing-weather-information-and-message-framing-to-incre.md
- 论文主类型：field_intervention_or_platform_experiment
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.86

## 文章级论证概况

- 核心问题：在移动健康应用中，如何利用用户实时天气信息与消息框架的组合，最有效地促进身体活动，并识别这种天气情境定向策略的边界条件与可持续性？

- 制品与设计：与亚洲大型活动追踪应用合作，设计并推送三组消息：增益框架、损失框架和无框架中性消息；根据GPS定位获取用户所在区域的实时云量，区分晴天和阴天；通过三项现场实验测试不同天气与消息框架的最优搭配，并在第四个重复实验中检验干预的长期可重复性。

- 客观结果：研究发现，有框架的消息（增益或损失）优于无框架中性消息；在晴天，损失框架比增益框架更有效，在阴天，增益框架比损失框架更有效；该最优搭配在55天内重复使用4次仍有效；单次干预的效果可持续至少6天；机制分析表明工具性动机用户符合情绪作为资源理论的预测，而消费性动机用户符合情绪一致性的预测；低运动水平和低收入地区用户的效果更明显。

- 核心贡献：作者声称：（1）为mHealth文献提供了一种可持续、可重复使用且不扩大健康差距的情境化消息设计方案；（2）在理论上调和了情绪一致性与情绪作为资源两种对立视角，指出用户动机是决定哪种理论成立的边界条件；（3）为医疗健康企业和政策制定者提供基于天气信息与消息框架匹配的实用设计指南。

- 整篇论证链：作者从久坐不动造成的公共健康危机出发，指出现有mHealth干预效果不稳、缺乏持续性和对弱势群体效果有限，认为原因是未考虑影响运动决策的情境因素，尤其天气。虽然营销领域的天气情境定向已有效果，但健康消息面临即时成本与延迟回报、身体努力资源不足以及目标人群异质性等不同机制，不能简单移植；同时理论上情绪一致性与情绪作为资源两种视角给出了相反预测。为厘清这一问题，作者与真实活动追踪应用合作开展系列现场实验：先用组间实验证明框架消息比中性消息有效；再用组内实验让同一用户在晴、阴两种天气下接受增益或损失框架消息，发现晴天损失框架更有效、阴天增益框架更有效，支持情绪作为资源视角；随后通过稳健性检验、干预后多日DID分析以及连续四期重复实验，证明效果并非一次性或短期；机制分析利用用户使用动机调查显示工具性动机者符合情绪作为资源、消费性动机者符合情绪一致性，并通过公园可达性排除社会影响的替代解释；最后按运动水平和收入分层发现策略对低运动水平与低收入地区用户更有效。讨论部分将这些结果回接到引言中的文献缺口，提出理论调和、mHealth可持续设计以及面向弱势群体的实践启示。

## 类型与写作弧线判定

- 论文主类型判定：研究在真实活动追踪应用平台上操纵推送消息的框架设计，并利用用户所处天气作为自然变化条件，通过多个随机现场实验评估行为结果；不是实验室实验、算法benchmark、纯设计科学制品或形式模型，而是真实平台上的数字干预与现场因果检验。

- 主导写作弧线判定：写作弧线从久坐健康问题出发，引入情绪一致性与情绪作为资源两种对立理论，将其转化为增益/损失框架消息与天气搭配的可检验设计，通过三个阶段现场实验和机制分析进行检验，最后在讨论中回到理论，以用户动机调和两种理论视角并形成设计知识。

## 研究开展程序

- study_or_phase_count：9

- 研究阶段总序列：研究依次回答四个递进问题：首先证明框架消息本身能提升运动行为（Study 1组间实验）；然后在控制个体固定效应的条件下识别天气与框架的最优搭配（Study 2组内实验）；接着检验该效果的稳健性、干预后持续性以及重复使用不衰减（稳健性检验、DID、Study 3）；最后通过机制分析、替代解释排除和异质性分析刻画‘为什么有效、对谁有效’（动机机制、公园可达性、运动水平、收入分层）。

### studies_or_phases

#### 1. Study 1：组间实验，框架消息 vs 中性消息

- order：1

- name_cn：Study 1：组间实验，框架消息 vs 中性消息

- question_cn：相比无框架的中性消息，增益框架或损失框架消息是否能更有效地促使用户完成10000步挑战？

- inputs_and_setting_cn：1248名活动追踪应用用户，分布于全国；2019年春季三天内，每天上午10点发送一次推送；用户被随机分配到增益、损失或中性消息组。

- designed_or_compared_object_cn：三种推送消息：增益框架强调运动好处、损失框架强调不运动风险、中性框架仅邀请参加10000步挑战。

- baseline_control_or_counterfactual_cn：中性无框架消息作为对照组；增益和损失相互对照。

##### objective_metrics

1. 是否完成10000步挑战的二元变量

2. 总步数

- analysis_method_cn：线性概率模型（LPM）与OLS；控制性别、年龄、身高、体重、前一周步数等；进行随机化平衡检验。

- main_result_cn：增益干预比中性消息提高目标达成率约9.09个百分点（p<0.01），损失干预比中性消息提高约10.4个百分点（p<0.01）；以步数为因变量时结果一致。

- argumentative_role_cn：建立消息框架本身的因果作用，排除了‘任何框架是否有效’这一基础问题，为后续比较增益与损失在天气条件下的相对效果提供前提。

- remaining_uncertainty_cn：未涉及天气；不知道在晴天和阴天中增益与损失框架孰优孰劣，也不知道个体异质性是否会解释效果。

- link_to_next_phase_cn：既然框架消息有效，下一步需要确定在不同天气条件下应使用哪一种框架，因此进入Study 2的组内实验。

##### evidence_pointers

1. Study 1 P1

2. Table 1

3. Study 1 Results 表格A2

4. 在线附录A1平衡检验

#### 2. Study 2：组内实验，天气×消息框架的最优搭配

- order：2

- name_cn：Study 2：组内实验，天气×消息框架的最优搭配

- question_cn：在晴天和阴天条件下，增益框架与损失框架哪个更有效地促使用户完成运动目标？

- inputs_and_setting_cn：2022年9月秋季进行一个月；初始抽取7000名用户，经过两个治疗期和15天冷却期后，最终2978名用户经历了与T1相反天气并进入分析；用户所在位置由GPS识别，云量由气象局API匹配；云量0-2为晴天、8-10为阴天，排除云量3-7的模糊天气。

- designed_or_compared_object_cn：每位用户在T1随机分配到增益或损失框架消息，并在T2不同天气下收到同一种框架消息；比较同一用户在不同天气下对两种框架的响应。

- baseline_control_or_counterfactual_cn：增益框架作为参照，损失框架与之对比；每个用户作为自身对照（个体固定效应）；同时加入地区、星期固定效应。

##### objective_metrics

1. 是否完成10000步挑战

2. 对数化步数

- analysis_method_cn：线性概率模型和OLS，包含Sunny、Loss及其交互项；控制前一周步数、湿度、风速、降水；个体、地区、日固定效应；聚类稳健标准误。

- main_result_cn：晴天时损失框架相比增益框架的目标达成率显著更高（β2+β3=0.0702，p<0.01）；阴天时增益框架显著优于损失框架（β2=-0.052，p<0.05）；以步数为因变量时结果一致。

- argumentative_role_cn：直接检验了情绪作为资源与情绪一致性两种理论在mHealth场景中的竞争性预测，结果支持情绪作为资源视角：晴天损失、阴天增益。

- remaining_uncertainty_cn：结果是否受时间-地点混淆、模型设定、异常值、天气日变化影响；单次干预的效果能维持多久；重复使用是否会衰减；潜在机制是否真的是情绪资源，而非其他替代解释。

- link_to_next_phase_cn：先通过多项稳健性检验强化核心结果，再进一步考察单次干预后的持续效果，随后进入Study 3回答重复使用问题。

##### evidence_pointers

1. Study 2 实验流程Figure 1

2. Table 2 随机化检验

3. Figure 2 无模型证据

4. Table 3 回归结果

5. Study 2 Robustness Checks段落

#### 3. Study 2 稳健性检验

- order：3

- name_cn：Study 2 稳健性检验

- question_cn：主结果在更严格的时间-地点固定效应、其他模型设定、剔除异常值和天气突变样本后是否依然成立？

- inputs_and_setting_cn：沿用Study 2样本与变量。

- designed_or_compared_object_cn：比较主回归模型与加入时间×地点交互固定效应、Logit/Probit模型、删除前一周步数高于均值五个标准差的异常用户、删除晴阴转变日的保守样本。

- baseline_control_or_counterfactual_cn：主结果作为基准；各稳健性设定作为替代估计。

##### objective_metrics

1. 是否完成10000步挑战

2. 对数化步数

- analysis_method_cn：时间地点固定效应LPM；Logit/Probit；剔除异常值后LPM；剔除天气剧变日后LPM。

- main_result_cn：所有稳健性检验均与主结果一致，天气与框架交互效应没有消失。

- argumentative_role_cn：排除时间-地点混淆、模型误设、极端值和天气日变化等替代解释，增强晴天损失/阴天增益结论的可信度。

- remaining_uncertainty_cn：这些检验仍未回答效果持续性、可重复性和底层心理机制。

- link_to_next_phase_cn：确认核心结果稳健后，作者考察单次干预在随后数天是否仍有溢出效应，以及是否可重复使用。

##### evidence_pointers

1. Study 2 Robustness Checks 表格A3/A4/A5

#### 4. 干预后多日效果分析（DID）

- order：4

- name_cn：干预后多日效果分析（DID）

- question_cn：单次天气定向干预后，用户在未收到新消息的后续日子里是否仍会增加运动？

- inputs_and_setting_cn：将Study 2用户干预前7天和干预后7天构造成面板；分别分析晴天和阴天下损失框架相对于增益框架的差分效果。

- designed_or_compared_object_cn：损失框架作为治疗组、增益框架作为控制组的DID；晴天和阴天分别估计。

- baseline_control_or_counterfactual_cn：干预前作为基线，增益框架作为对照。

##### objective_metrics

1. 每日对数化步数

- analysis_method_cn：对干预后每一天分别做OLS DID回归，核心为Loss×After交互项。

- main_result_cn：晴天时损失框架相对增益框架在干预后连续7天都能提升步数；阴天时增益框架相对损失框架在干预后连续6天有效。

- argumentative_role_cn：说明最优搭配不只是即时效应，而是能带来至少一周的行为溢出，增强实践意义。

- remaining_uncertainty_cn：仍未说明同一策略反复推送是否会导致习惯化或效果衰减。

- link_to_next_phase_cn：由此自然引出Study 3：如果将最优天气消息重复发送四次，效果是否依然存在。

##### evidence_pointers

1. Effectiveness of Intervention on Subsequent Days After Targeting段落

2. 在线附录表A6、A7

#### 5. Study 3：重复使用效果（55天四期）

- order：5

- name_cn：Study 3：重复使用效果（55天四期）

- question_cn：最优天气消息搭配在多次重复使用后是否仍然有效，即是否存在长期可持续性？

- inputs_and_setting_cn：417名用户，55天；四个治疗期，每个治疗期之间15天冷却期；用户重复收到最优搭配（晴天损失、阴天增益）消息。

- designed_or_compared_object_cn：同一用户在四个时期分别接受最优干预；以干预前后7天平均步数构造面板。

- baseline_control_or_counterfactual_cn：各期干预前作为自身基线；无气候或时间趋势对照，但通过个体、地点、日固定效应控制部分混淆。

##### objective_metrics

1. 日均步数（对数化）

- analysis_method_cn：对每个时期分别做OLS，核心变量为AfterIntervention；跨期比较使用Z-score检验。

- main_result_cn：四个时期的干预效应均为正且显著，且第一期与后续各期效应量没有显著下降（Z-score分别为-0.447、0.199、0.746）。

- argumentative_role_cn：证明天气定向干预可以作为长期策略，回应了mHealth干预效果随干预撤除而消失的批评。

- remaining_uncertainty_cn：缺乏无干预对照组，无法完全排除同期季节性活动增加；只有417人，统计功效有限；机制仍未解释。

- link_to_next_phase_cn：在确认长期效果后，作者转向‘为什么会出现这种效应’，即机制和异质性分析。

##### evidence_pointers

1. Study 3 P1–P2

2. Table 4

#### 6. 机制分析：工具性动机与消费性动机

- order：6

- name_cn：机制分析：工具性动机与消费性动机

- question_cn：用户使用mHealth应用的动机是否决定其遵循情绪作为资源还是情绪一致性理论？

- inputs_and_setting_cn：从合作应用获取用户自报安装/使用目的；分为工具性动机（管理健康、提升自信）和消费性动机（乐趣与享受）；剔除非明确目的用户。

- designed_or_compared_object_cn：在工具性和消费性两组中分别复制Study 2的回归模型。

- baseline_control_or_counterfactual_cn：增益框架为参照；晴天与阴天相互对照；两组用户互为对照。

##### objective_metrics

1. 是否完成10000步挑战

- analysis_method_cn：分样本LPM，加入Sunny、Loss及交互项；固定效应与控制变量同Study 2。

- main_result_cn：工具性动机用户在晴天损失更有效（β2+β3=0.077，p<0.01），阴天增益更有效（β2=-0.056，p<0.05），符合情绪作为资源；消费性动机用户呈现相反模式（晴天增益更有效，阴天损失更有效），符合情绪一致性。

- argumentative_role_cn：直接验证理论机制：用户动机会决定情绪是被当作信息还是资源，从而调和两种对立理论预测。

- remaining_uncertainty_cn：动机来自用户自报，可能存在自我选择；没有直接测量情绪状态。

- link_to_next_phase_cn：在建立理论机制后，作者进一步排除社会影响的替代解释并检验异质性。

##### evidence_pointers

1. Mechanisms and Additional Analyses Mechanisms段落

2. Table 5

#### 7. 替代解释检验：公园可达性与社会影响

- order：7

- name_cn：替代解释检验：公园可达性与社会影响

- question_cn：晴天损失框架更有效是否只是因为用户在公园看到别人锻炼而产生社会比较/社会影响，而不是情绪资源机制？

- inputs_and_setting_cn：根据用户位置计算500米范围内公园数，按中位数分为高、低公园可达性两组。

- designed_or_compared_object_cn：比较高公园可达性与低公园可达性两组用户中天气×框架交互效应是否不同。

- baseline_control_or_counterfactual_cn：低公园可达性组作为参照；高可达性若诱发更多社会影响，则效应应更大。

##### objective_metrics

1. 是否完成10000步挑战

- analysis_method_cn：分样本回归，并用Z-score检验组间系数差异。

- main_result_cn：晴天与阴天中，高、低公园可达性组的核心系数均无显著差异（Z=-0.388和-0.554，p>0.1），不支持社会影响机制。

- argumentative_role_cn：排除了一个重要替代解释，强化了情绪作为资源的机制解释。

- remaining_uncertainty_cn：公园距离只是社会可见性的代理，不能完全排除其他社会比较渠道。

- link_to_next_phase_cn：随后进入异质性分析，考察策略对低运动水平和低收入用户是否更有效。

##### evidence_pointers

1. Alternative Explanation段落

2. 在线附录表A8

#### 8. 异质性分析：既往运动水平

- order：8

- name_cn：异质性分析：既往运动水平

- question_cn：天气定向策略对低运动水平和高运动水平用户是否同样有效？

- inputs_and_setting_cn：按研究前一个月步数高低分位，将用户分为低/中运动水平（75%分位以下）和高运动水平（25%分位以上）。

- designed_or_compared_object_cn：比较两组用户对Sunny×Loss交互项的响应。

- baseline_control_or_counterfactual_cn：高运动水平组作为对照。

##### objective_metrics

1. 是否完成10000步挑战

- analysis_method_cn：分样本LPM。

- main_result_cn：晴天损失更有效和阴天增益更有效的效果主要在低/中运动水平组显著；高运动水平组系数不显著。

- argumentative_role_cn：识别策略的目标人群边界，并说明它恰好作用于最需要干预的高危人群。

- remaining_uncertainty_cn：运动水平按既往步数划分，且高运动组样本量较小，可能功效不足。

- link_to_next_phase_cn：最后考察收入是否也会调节效果。

##### evidence_pointers

1. Additional Analysis 第一段

2. Table 6

#### 9. 异质性分析：地区收入水平

- order：9

- name_cn：异质性分析：地区收入水平

- question_cn：天气定向策略对不同收入地区用户效果是否不同，是否会扩大或缩小健康差距？

- inputs_and_setting_cn：按用户所在地区个人收入中位数分为低收入地区和高收入地区两组。

- designed_or_compared_object_cn：比较两组用户对天气×框架交互项的响应。

- baseline_control_or_counterfactual_cn：高收入地区组作为对照。

##### objective_metrics

1. 是否完成10000步挑战

- analysis_method_cn：分样本LPM。

- main_result_cn：晴天损失更有效和阴天增益更有效的效果在低收入地区用户中显著，在高收入地区不显著。

- argumentative_role_cn：证明该策略对传统上更难触达的低收入人群更有效，不会扩大数字或健康差距，反而可能缩小健康差距。

- remaining_uncertainty_cn：收入是地区层面而非个人层面代理，存在测量误差；高收入组不显著可能受样本量影响。

- link_to_next_phase_cn：这些异质性结果被讨论部分用于说明理论调和与政策含义。

##### evidence_pointers

1. Additional Analysis 第三段

2. Table 7

## 各部分修辞架构

### abstract_moves

1. 背景与问题：现实健康威胁、mHealth干预必要性

2. 方法预告：现场实验、晴/阴天气与增益/损失框架、重复实验

3. 核心发现：晴天损失优于增益、阴天增益优于损失、可重复使用

4. 机制证据：排除替代解释、动机机制

5. 异质性：低运动水平和低收入地区更明显

6. 贡献声明：理论指导与实践意义

### introduction_moves

1. CONTEXT：久坐不动带来的健康负担

2. PRIOR_KNOWLEDGE：mHealth干预方法繁多但效果不稳定

3. LIMITATION：以往干预忽视天气等情境因素

4. CONTEXT：营销领域天气情境定向已成功

5. LIMITATION：健康消息与营销消息机制不同，不能简单移植

6. LIMITATION：健康场景需要关注低收入、低运动水平等亚群体

7. THEORY_INTRO：情绪一致性预测晴天增益/阴天损失

8. THEORY_INTRO：情绪作为资源预测晴天损失/阴天增益

9. RQ_OR_OBJECTIVE：识别最优天气-框架组合并检验异质性

10. STUDY_OVERVIEW：三项现场实验的简要顺序和主要结果

11. CONTRIBUTION：mHealth设计与理论调和贡献

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE：nudge定义与mHealth载体背景

2. PRIOR_KNOWLEDGE：天气影响情绪并通过日光/血清素/β-内啡肽解释

3. PRIOR_KNOWLEDGE：预期理论框架与健康消息的增益/损失框架

4. THEORY_INTRO：情绪一致性视角的机制

5. THEORY_INTRO：情绪作为资源视角的机制

6. MECHANISM：消费性动机使情绪成为信息输入，工具性动机使情绪成为背景资源

7. TRANSITION：mHealth用户动机未知，因此天气-框架交互是经验问题

### artifact_design_moves

1. DESIGN_FEATURE：与大型活动追踪应用合作，GPS实时位置获取气象

2. DESIGN_FEATURE：云量作为晴/阴判断依据，避免模糊天气

3. DESIGN_FEATURE：三条消息文本：增益、损失、中性

4. METHOD_JUSTIFICATION：组间设计用于建立因果作用，组内设计用于控制个体异质性

5. METHOD_JUSTIFICATION：15天冷却期减少携带效应和应用干扰

6. METHOD_JUSTIFICATION：分散取样提升天气变异并避免同区域混淆

### evaluation_moves

1. METHOD_JUSTIFICATION：随机化、平衡检验

2. BENCHMARK_OR_CONTRAST：中性消息作为Study 1基线

3. RESULT：Study 1框架优于中性

4. RESULT：Study 2模型结果支持情绪作为资源

5. ROBUSTNESS_OR_BOUNDARY_TEST：时间-地点固定效应、Logit/Probit、异常值、天气日变化

6. BENCHMARK_OR_CONTRAST：DID将增益框架作为对照

7. BENCHMARK_OR_CONTRAST：Study 3每个用户干预前作为自身基线

8. MECHANISM：动机分样本

9. ROBUSTNESS_OR_BOUNDARY_TEST：公园可达性排除社会影响

10. ROBUSTNESS_OR_BOUNDARY_TEST：运动水平和收入分样本

### discussion_and_contribution_moves

1. RESULT：重述三个现场实验和机制/异质性结果

2. CONTRIBUTION：回应mHealth可持续性缺口

3. THEORY_RETURN：用户动机调和情绪一致性/情绪作为资源两种理论

4. CONTRIBUTION：实践设计指导和营销应用注意

5. BOUNDARY_CONDITION：亚洲样本、单一运动应用、秋季

6. LIMITATION_AND_FUTURE：跨文化、其他健康应用、其他季节

## 理论/知识到设计的翻译

### 知识/理论基础

1. 预期理论（Kahneman and Tversky 1979）

2. 情绪一致性视角（Schwarz and Clore 1983; Pham 2008）

3. 情绪作为资源视角（Trope and Neter 1994; Raghunathan and Trope 2002）

4. 消费性动机与工具性动机（Pham 1998; Yeung and Wyer 2004）

5. 天气-情绪生理机制：日光、血清素、β-内啡肽（Cunningham 1979; Denissen et al. 2008）

- 理论—设计耦合：direct

- 耦合判定理由：理论前瞻性地决定了消息框架的两种实验条件（增益/损失）、天气作为调节变量以及动机作为机制维度，研究设计明确围绕情绪一致性/情绪作为资源的竞争预测展开；虽然消息的具体措辞来自现有干预范式，但检验的差异和结果解释都由理论驱动。

- 理论到设计翻译链：天气光照变化→影响血清素和β-内啡肽→引发积极或消极情绪→情绪可作为一致性信息或作为心理资源→若作为资源：积极情绪能抵御损失信息的负面情感冲击，因此晴天更适合损失框架；消极情绪缺乏资源，因此阴天更适合增益框架→将这一命题转化为推送消息的损失/增益框架→在真实应用中按用户GPS实时天气分配接受哪一种框架→通过组内设计比较晴天和阴天下的目标完成率→再用动机调查验证消费性/工具性动机决定信息/资源两种模式→最终形成‘工具性动机用户适用情绪资源匹配，消费性动机用户适用情绪一致性匹配’的条件化设计知识。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：天气通过日光影响血清素与β-内啡肽，从而影响情绪；晴天积极、阴天消极。

- mechanism_cn：生理-情绪路径：光照改变神经递质，情绪影响信息处理和运动动机。

- design_requirement_cn：需要在消息发送时获得用户实时天气，并定义可操作的晴/阴分类。

- artifact_choice_cn：通过GPS获取用户位置，与气象局API的云量匹配；云量0-2为晴天、8-10为阴天，排除3-7。

- evaluated_contrast_cn：晴天与阴天条件下的不同框架消息效果。

- objective_result_cn：天气与框架交互显著：晴天损失优于增益，阴天增益优于损失。

##### evidence_pointers

1. Study Context P2

2. Study 2 实验流程

3. Table 3

#### 2. 2

- theory_or_knowledge_claim_cn：情绪一致性视角：积极情绪促进一致的正向信息加工，消极情绪促进一致的负向信息加工。

- mechanism_cn：情绪作为信息输入，影响消息说服力；积极情绪下增益信息更易被接受，消极情绪下损失信息更易被接受。

- design_requirement_cn：若该理论成立，应给晴天用户发送增益框架、给阴天用户发送损失框架。

- artifact_choice_cn：在应用中同时准备增益和损失两种框架消息，按天气实时匹配。

- evaluated_contrast_cn：消费性动机用户中晴天/阴天对增益/损失框架的响应。

- objective_result_cn：消费性动机用户呈现晴天增益、阴天损失的最优组合，与情绪一致性一致。

##### evidence_pointers

1. Theoretical Background P1

2. Table 5 column 2

#### 3. 3

- theory_or_knowledge_claim_cn：情绪作为资源视角：积极情绪缓冲负面信息的威胁，使个体能处理损失框架；消极情绪缺少这种资源，因此对损失框架产生防御，反而更接受增益框架。

- mechanism_cn：情绪作为心理资源：积极情绪促进对自我相关负面信息的加工和长期目标追求；消极情绪优先短期情绪修复。

- design_requirement_cn：若该理论成立，应给晴天用户发送损失框架、给阴天用户发送增益框架。

- artifact_choice_cn：在应用中按天气实时选择框架；在工具性动机用户中尤其应采用该匹配。

- evaluated_contrast_cn：工具性动机用户中晴天/阴天对增益/损失框架的响应；以及总体样本中的交互效应。

- objective_result_cn：总体样本和工具性动机用户中晴天损失、阴天增益更有效，支持情绪作为资源。

##### evidence_pointers

1. Theoretical Background P2

2. Table 3

3. Table 5 column 1

#### 4. 4

- theory_or_knowledge_claim_cn：消费性动机使情绪作为评价信息；工具性动机使情绪作为处理资源。

- mechanism_cn：消费性活动看重当下感受，因此采用“我感觉怎么样”启发式；工具性活动看重长期结果，因此情绪成为调节负面信息的资源。

- design_requirement_cn：消息匹配策略不能一刀切；应根据用户使用动机（而非只按天气）选择框架。

- artifact_choice_cn：收集用户安装/使用目的调查，将用户分为工具性和消费性两组，分别评估策略。

- evaluated_contrast_cn：两个动机分样本中的天气×框架交互方向是否相反。

- objective_result_cn：工具性动机样本为晴天损失/阴天增益；消费性动机样本为晴天增益/阴天损失；两组模式相反。

##### evidence_pointers

1. Mechanisms and Additional Analyses Mechanisms

2. Table 5

## 评价逻辑

### evaluation_modes

1. 随机组间现场实验（Study 1）

2. 随机组内交叉现场实验（Study 2）

3. 稳健性检验（固定效应、Logit/Probit、异常值、天气日变化）

4. 干预后多日DID分析

5. 重复治疗现场实验（Study 3）

6. 机制分样本分析（用户动机）

7. 替代解释排除（公园可达性）

8. 异质性分样本分析（运动水平、收入）

- why_these_evaluations_cn：研究需要同时回答‘是否有效、什么搭配最优、能否持续、为什么有效、对谁有效’五个层次的问题。因此先以组间设计确认框架消息的因果存在；再用组内设计利用个体固定效应消除每个人稳定特质对天气-框架交互的混淆；随后用稳健性检验和DID强化因果与持续性；用重复实验回答衰减问题；用动机分样本验证理论机制；用公园可达性排除社会影响；用运动水平和收入分层刻画边界条件和公共健康含义。

- benchmark_and_contrast_chain_cn：Study 1用中性消息作为无框架基准，证明框架本身的价值；Study 2不再设中性组，而是让增益框架和损失框架互相作为参照，并让同一用户在不同天气下比较；DID分析以增益框架和干预前作为双重对照；Study 3以每个用户干预前作为自身基线，并与第一期效应比较后续时期是否衰减；异质性分析以高运动水平和高收入组作为边界对照。

### claim_evidence_ledger

1. 框架消息优于中性消息：由Study 1的LPM和OLS结果支持，增益和损失系数均显著为正。

2. 晴天损失框架最优、阴天增益框架最优：由Study 2模型推理和无模型图支持，交互项方向与显著性与情绪作为资源预言一致。

3. 核心结果稳健：时间-地点固定效应、Logit/Probit、剔除异常值、剔除天气剧变日均保持一致。

4. 单次干预效果延续多日：晴天干预后7天、阴天干预后6天的DID交互项显著，支持溢出效应。

5. 重复使用有效：Study 3四期均为正显著，Z-score未显示显著下降，但该检验依赖无干预对照缺失和较小样本，证据强度中等。

6. 用户动机是机制：工具性动机组呈情绪资源模式，消费性动机组呈情绪一致性模式，两组方向相反，直接支持动机调节机制。

7. 排除社会影响替代解释：公园可达性高低两组系数无显著差异，不支持看到他人运动的解释。

8. 策略对低运动水平和低收入地区更有效：分样本中高运动/高收入组系数不显著，低运动/低收入组显著，支持异质性边界主张。

- internal_validity_strategy_cn：采用随机分配并进行平衡性检验；组内设计使每个用户作为自身对照，纳入个体固定效应；加入地区固定效应、日固定效应、时间×地点固定效应；设置15天冷却期以减少携带效应；排除云量3-7的模糊天气和天气剧变日；用DID处理干预前后变化；通过公园可达性排除社会影响。

- external_validity_strategy_cn：在真实应用上运行，覆盖国家多个分散地区，具有天气变异；用户是真实活动追踪用户，行为结果由应用客观追踪；通过重复四个治疗期考察长期效果；通过动机、运动水平和收入分层检验可推广边界；作者也在限制中承认样本在亚洲、单一应用、秋季，外部推广需谨慎。

- what_is_not_actually_tested_cn：没有直接测量用户情绪状态，情绪资源/信息机制是通过天气和动机间接推断；没有独立验证消息‘感知框架’是否与研究者分类一致；Study 3缺少无干预对照组，不能完全排除季节/时间趋势；动机来自自报调查，可能存在选择与测量误差；收入基于地区而非个人；高运动水平和高收入组系数不显著可能受统计功效限制，不能简单解释为‘无效’；未测试其他季节和其他健康应用类型。

## 贡献闭环

- technical_claim_cn：在mHealth推送消息中，利用实时天气信息并按天气匹配消息框架，可以显著提高用户完成10000步挑战的概率；晴天用损失框架、阴天用增益框架是统计上显著的最优搭配。

- artifact_claim_cn：天气-框架搭配干预的具体设计（损失/增益框架、云量阈值、GPS实时匹配、组内交替和冷却期）导致了行为改善，并且重复使用四次后效果仍存在；框架消息优于中性消息的结论来自Study 1的随机对比。

- mechanism_claim_cn：作者主张背后的机制是情绪作为资源：天气诱发情绪，工具性动机用户把情绪当作处理健康信息的心理资源，因此晴天能承受损失框架的负面信息、阴天更接受增益框架；消费性动机用户则把情绪当作评价信息，符合情绪一致性。

- boundary_claim_cn：该策略对工具性动机用户更有效；对低/中运动水平用户和低收入地区用户效果更明显；研究样本为亚洲单一活动追踪应用，且仅在秋季实施，边界条件包含文化和季节限制。

- reusable_design_knowledge_cn：mHealth干预应结合实时情境（天气）与消息框架；最优框架取决于用户动机类型；干预可以通过冷却期和重复推送维持长期有效；天气信息可作为低成本、可扩展的情境目标线索。

- theoretical_contribution_cn：澄清并调和了情绪一致性与情绪作为资源两种对立理论：二者分别适用于消费性动机和工具性动机情境；由此解释了为什么营销情境下情绪一致性策略有效而健康情境下相反。

- how_discussion_closes_intro_gap_cn：讨论部分将三阶段实验结果重新连接到引言提出的‘mHealth缺乏可持续性’和‘天气情境缺失’的缺口，指出该方案可重复使用、对弱势群体更有效、不会扩大健康差距；同时将天气×框架交互结果与营销文献对比，用动机条件调和理论矛盾，从而同时回应了应用缺口和理论缺口。

- overclaim_or_unsupported_leaps_cn：可能的跳跃包括：将天气作为情绪的操作化代理而没有直接测量情绪；将工具性/消费性动机分组结果作为理论机制的直接证明，但用户动机来自自报且可能存在混淆；Study 3的‘效果不衰减’结论基于无对照组的四期前后比较，Z-score不显著也可能由功效不足导致；将低收入地区效应显著解读为‘缩小健康差距’是一种较强的政策断言；高收入/高运动组不显著被解释为‘策略在优势群体中不显著’，但更稳妥的表述应是‘证据不足’。

## 句级写作动作图谱

### 1. Abstract P1 S1–S3

- order：1

- section：Abstract

- locator：Abstract P1 S1–S3

- move_code：CONTEXT

- paraphrase_cn：指出研究利用移动技术获取的实时天气信息来增强移动干预对健康行为的促进作用。

- rhetorical_function_cn：在摘要开头直接概括研究主题与切入点。

- depends_on_cn：依赖全文核心概念：天气情境与移动健康

- sets_up_cn：为后面的方法、结果和贡献声明做铺垫

- evidence_pointer：Abstract 第1句

### 2. Abstract P1 S4–S7

- order：2

- section：Abstract

- locator：Abstract P1 S4–S7

- move_code：RESULT

- paraphrase_cn：报告现场实验发现增益/损失干预的效果在晴天与阴天并非均匀分布：晴天损失更有效、阴天增益更有效。

- rhetorical_function_cn：用一句话浓缩核心实证发现。

- depends_on_cn：依赖Study 2的组内实验结果

- sets_up_cn：引出机制、可重复性和异质性证据

- evidence_pointer：Abstract 结果句

### 3. Abstract P1 S8–S10

- order：3

- section：Abstract

- locator：Abstract P1 S8–S10

- move_code：RESULT

- paraphrase_cn：补充机制证据、重复实验有效性以及低运动水平和低收入地区用户更明显的结果。

- rhetorical_function_cn：在摘要中展示证据广度和理论深度，防止读者把研究解读为单一实验性能结果。

- depends_on_cn：依赖Study 3、机制分析和异质性分析

- sets_up_cn：为贡献声明提供材料

- evidence_pointer：Abstract 后半部分

### 4. Introduction P1 S1–S4

- order：4

- section：Introduction

- locator：Introduction P1 S1–S4

- move_code：CONTEXT

- paraphrase_cn：描述发达国家成年人久坐比例高，身体不活动与多种疾病和死亡风险相关。

- rhetorical_function_cn：建立现实健康问题的紧迫性。

- depends_on_cn：无

- sets_up_cn：为提出mHealth干预必要性提供背景

- evidence_pointer：Introduction P1

### 5. Introduction P2 S1–S5

- order：5

- section：Introduction

- locator：Introduction P2 S1–S5

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：总结已有mHealth干预技术，如可视化、社交比较、社会支持、绩效反馈、经济激励、目标设定，但元分析显示这些应用总体效果有限且不持久。

- rhetorical_function_cn：压缩文献，为‘现有干预不足’提供证据。

- depends_on_cn：依赖引用文献和元分析

- sets_up_cn：引出需要更复杂个性化策略的呼吁

- evidence_pointer：Introduction P2

### 6. Introduction P3 S1–S4

- order：6

- section：Introduction

- locator：Introduction P3 S1–S4

- move_code：LIMITATION

- paraphrase_cn：指出现有干预忽视了影响运动决策的情境因素，天气是最基本且被充分证实的影响户外锻炼的因素，尤其对低收入群体。

- rhetorical_function_cn：从泛泛的干预不足聚焦到‘天气情境缺失’这一具体缺口。

- depends_on_cn：承接P2的mHealth有效性不足

- sets_up_cn：为将天气纳入mHealth设计提供依据

- evidence_pointer：Introduction P3

### 7. Introduction P4 S1–S3

- order：7

- section：Introduction

- locator：Introduction P4 S1–S3

- move_code：CONTEXT

- paraphrase_cn：说明营销领域已越来越多使用情境定向技术，包括天气，并能提升广告效果。

- rhetorical_function_cn：引入一个看似可借鉴的成熟技术领域。

- depends_on_cn：前面天气缺口已经建立

- sets_up_cn：随后指出该技术不能简单转移到健康领域

- evidence_pointer：Introduction P4

### 8. Introduction P5 S1–S6

- order：8

- section：Introduction

- locator：Introduction P5 S1–S6

- move_code：LIMITATION

- paraphrase_cn：说明健康消息与营销消息在即时满足、所需资源和自我控制问题上不同，运动需要付出当下成本和身体努力，所以营销的天气定向机制未必适用于健康干预。

- rhetorical_function_cn：制造‘看似可行但实际存在机制差异’的论证张力。

- depends_on_cn：依赖P4营销情境定向的成功

- sets_up_cn：论证为什么需要专门研究健康情境

- evidence_pointer：Introduction P5

### 9. Introduction P6 S1–S3

- order：9

- section：Introduction

- locator：Introduction P6 S1–S3

- move_code：LIMITATION

- paraphrase_cn：指出干预设计要考虑对低收入和低运动水平等亚群体的不同影响，而营销应用的主要目标与健康应用不同。

- rhetorical_function_cn：补充第二个维度，使研究从‘机制差异’扩展到‘异质性关注’。

- depends_on_cn：承接P5的机制差异

- sets_up_cn：为后文异质性分析做预告

- evidence_pointer：Introduction P6

### 10. Introduction P7 S1–S4

- order：10

- section：Introduction

- locator：Introduction P7 S1–S4

- move_code：THEORY_INTRO

- paraphrase_cn：介绍情绪一致性视角：积极情绪使一致信息更容易被加工，因此晴天适合增益框架，阴天适合损失框架。

- rhetorical_function_cn：引入第一种理论预测，建立理论对立的一方。

- depends_on_cn：前面已说明天气影响情绪

- sets_up_cn：为后文情绪作为资源视角的对立提供对照

- evidence_pointer：Introduction P7

### 11. Introduction P8 S1–S5

- order：11

- section：Introduction

- locator：Introduction P8 S1–S5

- move_code：THEORY_INTRO

- paraphrase_cn：介绍情绪作为资源视角：积极情绪缓冲损失框架的负面冲击，消极情绪缺乏资源而对损失框架防御，因此晴天损失更有效、阴天增益更有效。

- rhetorical_function_cn：引入第二种理论预测，形成‘理论冲突’。

- depends_on_cn：与P7的情绪一致性形成对立

- sets_up_cn：为实证检验的必要性提供理由

- evidence_pointer：Introduction P8

### 12. Introduction P9 S1–S5

- order：12

- section：Introduction

- locator：Introduction P9 S1–S5

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：提出研究目标：识别最能促进身体活动的天气与消息框架最优组合，并评估对不同用户群体的异质性效果。

- rhetorical_function_cn：将理论冲突转化为可实证的研究问题。

- depends_on_cn：P7-P8的理论冲突

- sets_up_cn：预告三项现场实验的设计

- evidence_pointer：Introduction P9

### 13. Introduction P10 S1–S6

- order：13

- section：Introduction

- locator：Introduction P10 S1–S6

- move_code：STUDY_OVERVIEW

- paraphrase_cn：概述三个实验：组间实验验证框架消息优于中性消息；组内实验发现晴天损失、阴天增益最优；第三个实验检验重复使用是否仍然有效。

- rhetorical_function_cn：给读者一张实验路线图，建立结构预期。

- depends_on_cn：研究目标已经提出

- sets_up_cn：为后面各Study的自然展开做路标

- evidence_pointer：Introduction P10

### 14. Introduction P11–P13 S1–S3

- order：14

- section：Introduction

- locator：Introduction P11–P13 S1–S3

- move_code：CONTRIBUTION

- paraphrase_cn：声明研究贡献：回应mHealth可持续性呼吁、填补情境定向在健康领域的缺口、在心理学理论上调和情绪一致性与情绪作为资源、并给出实践设计指导。

- rhetorical_function_cn：提前把贡献与缺口挂钩，使引言形成‘问题-方法-贡献’闭环。

- depends_on_cn：前面的缺口、理论冲突和实验概述

- sets_up_cn：读者会期待正文用证据兑现这些贡献

- evidence_pointer：Introduction P11-P13

### 15. Background mHealth Nudges P1 S1–S4

- order：15

- section：Background and Related Literature

- locator：Background mHealth Nudges P1 S1–S4

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：解释nudge如何通过引导注意力和设定目标来改善健康决策，并说明已被整合进健康应用。

- rhetorical_function_cn：为消息干预提供行为科学基础。

- depends_on_cn：无

- sets_up_cn：引出‘要在不同情境下找到最优消息’这一问题

- evidence_pointer：Background mHealth Nudges 第1段

### 16. Background Weather as a Contextual Cue P1 S1–S3

- order：16

- section：Background and Related Literature

- locator：Background Weather as a Contextual Cue P1 S1–S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：天气影响情绪和多种人类行为，但已有情境定向主要在营销领域。

- rhetorical_function_cn：巩固天气作为情境线索的重要性。

- depends_on_cn：引言中的天气缺口

- sets_up_cn：为天气-情绪机制的具体阐述做准备

- evidence_pointer：Background Weather 第1段

### 17. Background Weather P2 S1–S6

- order：17

- section：Background and Related Literature

- locator：Background Weather P2 S1–S6

- move_code：MECHANISM

- paraphrase_cn：提出日光通过促进血清素和β-内啡肽分泌来改善情绪，因此晴天使人更积极、阴天使人更消极。

- rhetorical_function_cn：用生理机制解释‘为什么天气能改变情绪’。

- depends_on_cn：前面天气影响情绪的总述

- sets_up_cn：为理论部分‘天气诱导情绪’的假设提供基础

- evidence_pointer：Background Weather 第2段

### 18. Background Intervention Framing P1 S1–S4

- order：18

- section：Background and Related Literature

- locator：Background Intervention Framing P1 S1–S4

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：消息框架基于预期理论，增益框架强调运动好处，损失框架强调不运动风险，二者会唤起不同情绪反应。

- rhetorical_function_cn：引入框架变量的理论基础，使实验刺激有据可依。

- depends_on_cn：前面的nudge讨论和天气讨论

- sets_up_cn：让两种框架消息成为理论可检验的设计

- evidence_pointer：Background Intervention Framing 第1段

### 19. Theoretical Background P1 S1–S5

- order：19

- section：Theoretical Background

- locator：Theoretical Background P1 S1–S5

- move_code：THEORY_INTRO

- paraphrase_cn：详述情绪一致性视角：情绪作为信息输入，人们更容易接受与当前情绪一致的消息，因此晴天增益、阴天损失是预测方向。

- rhetorical_function_cn：完整展开第一种理论及其机制。

- depends_on_cn：引言的简要介绍

- sets_up_cn：为与情绪资源预测对比提供充分基础

- evidence_pointer：Theoretical Background 第1段

### 20. Theoretical Background P2 S1–S6

- order：20

- section：Theoretical Background

- locator：Theoretical Background P2 S1–S6

- move_code：THEORY_INTRO

- paraphrase_cn：详述情绪作为资源视角：积极情绪是缓冲负面信息的心理资源，因此能处理损失框架；消极情绪缺乏资源，所以更接受增益框架。

- rhetorical_function_cn：完整展开第二种理论及其机制。

- depends_on_cn：情绪一致性理论已经说明

- sets_up_cn：为实证检验谁对谁错做铺垫

- evidence_pointer：Theoretical Background 第2段

### 21. Theoretical Background P3–P5 S1–S6

- order：21

- section：Theoretical Background

- locator：Theoretical Background P3–P5 S1–S6

- move_code：MECHANISM

- paraphrase_cn：消费性动机使情绪成为评价信息，工具性动机使情绪成为处理资源；mHealth用户动机未知，因此天气-框架交互是经验问题。

- rhetorical_function_cn：引入调节机制，解释为什么两种理论可能在不同人身上分别成立。

- depends_on_cn：依赖情绪信息/情绪资源的二分理论

- sets_up_cn：为后文的动机分样本机制分析做理论铺垫

- evidence_pointer：Theoretical Background 第3-5段

### 22. Study Context P1 P2 S1–S3

- order：22

- section：Study Context

- locator：Study Context P1 P2 S1–S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：描述与合作活动追踪应用的技术条件：常开后台上报GPS位置，可用于实时匹配气象；以云量0-10作为天气度量。

- rhetorical_function_cn：说明实验落地的现实条件与天气测量方法。

- depends_on_cn：前面理论需要天气信息作为前提

- sets_up_cn：为Study 1和Study 2的具体实施提供技术背景

- evidence_pointer：Study Context P1-P2

### 23. Study 1 P1 S1–S4

- order：23

- section：Study 1

- locator：Study 1 P1 S1–S4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用组间设计将1248名用户随机分配到增益、损失、中性消息组，目的在于用对照简单、清晰地证明框架消息的因果作用。

- rhetorical_function_cn：论证为什么先使用组间实验。

- depends_on_cn：研究问题需要从‘框架是否有效’开始

- sets_up_cn：为后续组内实验奠定‘框架有效’的前提

- evidence_pointer：Study 1 P1

### 24. Table 1 前一自然段与后文

- order：24

- section：Study 1

- locator：Table 1 前一自然段与后文

- move_code：DESIGN_FEATURE

- paraphrase_cn：增益消息强调运动带来的健康收益，损失消息强调不运动的疾病风险，中性消息只邀请用户参加10000步挑战。

- rhetorical_function_cn：使理论框架转化为可直接发送的消息刺激。

- depends_on_cn：预期理论与健康框架文献

- sets_up_cn：为结果解释提供刺激细节

- evidence_pointer：Table 1

### 25. Study 1 Results P1 S1–S4

- order：25

- section：Study 1

- locator：Study 1 Results P1 S1–S4

- move_code：RESULT

- paraphrase_cn：回归结果显示增益和损失干预的目标达成率都显著高于中性消息，步数结果也一致。

- rhetorical_function_cn：正式报告第一个实验结论。

- depends_on_cn：Study 1的随机设计和消息刺激

- sets_up_cn：为Study 2直接比较增益与损失提供依据

- evidence_pointer：Study 1 Results 及表A2

### 26. Study 2 P1 S1–S4

- order：26

- section：Study 2

- locator：Study 2 P1 S1–S4

- move_code：TRANSITION

- paraphrase_cn：既然框架消息已被证明有效，接下来要研究在不同天气条件下使用哪种框架最优；但组间设计无法完全控制与天气相关的地区和个人因素，因此采用组内设计。

- rhetorical_function_cn：从Study 1顺利过渡到Study 2，并解释设计变化原因。

- depends_on_cn：Study 1的结果

- sets_up_cn：为组内实验的方法细节进行论证

- evidence_pointer：Study 2 P1

### 27. Study 2 P2–P4 S1–S8

- order：27

- section：Study 2

- locator：Study 2 P2–P4 S1–S8

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：组内设计通过重复观测让个体作为自身对照，同时加入地区和星期固定效应；为解决携带效应设置15天冷却期；为增加天气变异从全国分散取样。

- rhetorical_function_cn：系统说明组内设计如何应对地点、天气、携带效应等威胁。

- depends_on_cn：前面过渡句对组间设计局限的分析

- sets_up_cn：为T1/T2流程的可信度提供保证

- evidence_pointer：Study 2 P2-P4

### 28. Study 2 experimental procedure P5 S1–S6

- order：28

- section：Study 2

- locator：Study 2 experimental procedure P5 S1–S6

- move_code：DESIGN_FEATURE

- paraphrase_cn：描述实际操作：T1随机抽取7000名用户中每天1000人，按GPS匹配云量并只在晴/阴天发送增益或损失消息；T2只给经历过相反天气的用户发送，最终分析样本2978人。

- rhetorical_function_cn：把理论对比转化为可操作、可复现的实验流程。

- depends_on_cn：组内设计原理和天气分类标准

- sets_up_cn：为Figure 1和后续结果提供样本基础

- evidence_pointer：Study 2 实验过程段落及Figure 1

### 29. Study 2 Results P1 S1–S3

- order：29

- section：Study 2

- locator：Study 2 Results P1 S1–S3

- move_code：RESULT

- paraphrase_cn：无模型证据显示：晴天损失组目标达成率21.8%高于增益组15.1%；阴天增益组11.8%高于损失组5.5%，方向与情绪作为资源一致。

- rhetorical_function_cn：先用简单图形平均值展示交互方向，便于读者直观理解。

- depends_on_cn：实验流程产生的数据

- sets_up_cn：为回归结果的显著性检验做铺垫

- evidence_pointer：Figure 2

### 30. Study 2 Results P2 S1–S5

- order：30

- section：Study 2

- locator：Study 2 Results P2 S1–S5

- move_code：RESULT

- paraphrase_cn：回归中，晴天损失相对增益的目标达成率增量显著为正，阴天为显著为负；以步数做因变量结果一致，因此最优搭配是晴天损失、阴天增益。

- rhetorical_function_cn：把无模型证据转化为统计学因果估计，回答核心研究问题。

- depends_on_cn：Table 3回归设定

- sets_up_cn：为后续稳健性检验和机制分析提供核心结论

- evidence_pointer：Table 3

### 31. Robustness Checks P1–P3 S1–S4

- order：31

- section：Study 2

- locator：Robustness Checks P1–P3 S1–S4

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：加入时间×地点交互固定效应、改用Logit/Probit、删除极端异常值、删除天气剧变日后，结果均保持一致。

- rhetorical_function_cn：用多种设定证明核心交互不是特定模型或样本的偶然产物。

- depends_on_cn：Study 2主结果

- sets_up_cn：提高后文DID和Study 3结果的可信度

- evidence_pointer：Study 2 Robustness Checks及表A3/A4/A5

### 32. Effectiveness of Intervention on Subsequent Days After Targeting P1–P2 S1–S4

- order：32

- section：Study 2

- locator：Effectiveness of Intervention on Subsequent Days After Targeting P1–P2 S1–S4

- move_code：RESULT

- paraphrase_cn：用DID比较干预前后7天步数，晴天损失相对增益的效果持续7天，阴天增益相对损失的效果持续6天。

- rhetorical_function_cn：把即时效应扩展到短期行为溢出，强调干预不是一次性刺激。

- depends_on_cn：Study 2样本和最优搭配结果

- sets_up_cn：为Study 3的重复使用问题铺垫

- evidence_pointer：表A6、A7

### 33. Study 3 P1 S1–S3

- order：33

- section：Study 3

- locator：Study 3 P1 S1–S3

- move_code：TRANSITION

- paraphrase_cn：虽然预期nudge效果会随时间衰减，但更实际的问题是重复使用同一最优消息是否会失效，因此设计第三个实验。

- rhetorical_function_cn：把研究推进到长期可持续性这一实践关键问题。

- depends_on_cn：Study 2结果和后续多日效果

- sets_up_cn：引出四期重复实验的设计

- evidence_pointer：Study 3 P1

### 34. Study 3 P1–P2 S1–S5

- order：34

- section：Study 3

- locator：Study 3 P1–P2 S1–S5

- move_code：DESIGN_FEATURE

- paraphrase_cn：417名用户在55天内接受四次最优天气干预，每次间隔15天冷却期，以干预前后7天平均步数构面面板。

- rhetorical_function_cn：设计一个可直接回答重复使用是否衰减的实验。

- depends_on_cn：Study 2已确定最优搭配

- sets_up_cn：为四期回归结果提供数据来源

- evidence_pointer：Study 3 实验设计段落

### 35. Study 3 Results P1–P2 S1–S4

- order：35

- section：Study 3

- locator：Study 3 Results P1–P2 S1–S4

- move_code：RESULT

- paraphrase_cn：四个时期的干预后步数都显著高于干预前，且第一期与后续时期效应没有显著下降。

- rhetorical_function_cn：支持‘天气干预可重复使用’的核心主张。

- depends_on_cn：Study 3四期实验数据

- sets_up_cn：为讨论部分的长期解决方案声明提供证据

- evidence_pointer：Table 4

### 36. Mechanisms P1 S1–S3

- order：36

- section：Mechanisms and Additional Analyses

- locator：Mechanisms P1 S1–S3

- move_code：TRANSITION

- paraphrase_cn：前面已经确立天气-框架匹配效果，本节要检验底层机制并评估异质性。

- rhetorical_function_cn：从效果转向解释，进入论文的理论深化部分。

- depends_on_cn：Study 1-3的结果

- sets_up_cn：引出动机分样本分析

- evidence_pointer：Mechanisms 第1段

### 37. Mechanisms Results P1–P2; Table 5

- order：37

- section：Mechanisms and Additional Analyses

- locator：Mechanisms Results P1–P2; Table 5

- move_code：RESULT

- paraphrase_cn：工具性动机用户在晴天损失更有效、阴天增益更有效；消费性动机用户则相反，分别支持情绪作为资源和情绪一致性。

- rhetorical_function_cn：用分样本结果直接验证理论机制，并解释核心效应为何成立。

- depends_on_cn：用户动机调查数据

- sets_up_cn：为讨论部分调和两种理论提供证据

- evidence_pointer：Table 5

### 38. Alternative Explanation P1–P2 S1–S4

- order：38

- section：Alternative Explanation

- locator：Alternative Explanation P1–P2 S1–S4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：为排除‘看到公园里别人运动导致社会比较’的替代解释，按用户500米内公园数量进行分组比较。

- rhetorical_function_cn：主动处理一个会威胁机制解释的替代假设。

- depends_on_cn：前面机制分析表明情绪资源机制

- sets_up_cn：为表A8结果做方法说明

- evidence_pointer：Alternative Explanation 第1-2段

### 39. Alternative Explanation P3 S1–S4

- order：39

- section：Alternative Explanation

- locator：Alternative Explanation P3 S1–S4

- move_code：RESULT

- paraphrase_cn：高、低公园可达性组的天气-框架交互效应无显著差异，因此社会影响不是驱动因素。

- rhetorical_function_cn：用零结果排除替代机制。

- depends_on_cn：公园可达性分组分析

- sets_up_cn：强化情绪资源机制的唯一解释地位

- evidence_pointer：表A8

### 40. Additional Analysis P1–P2; Table 6

- order：40

- section：Additional Analysis

- locator：Additional Analysis P1–P2; Table 6

- move_code：RESULT

- paraphrase_cn：按既往运动水平分组后，最优天气-框架效果在低/中运动水平组显著，在高运动水平组不显著。

- rhetorical_function_cn：识别策略的高危人群目标，说明它正好作用于更需要干预的人群。

- depends_on_cn：Study 2主模型

- sets_up_cn：为健康公平讨论提供证据

- evidence_pointer：Table 6

### 41. Additional Analysis P3–P4; Table 7

- order：41

- section：Additional Analysis

- locator：Additional Analysis P3–P4; Table 7

- move_code：RESULT

- paraphrase_cn：按地区收入中位数分组后，晴天损失、阴天增益效果在低收入地区显著，在高收入地区不显著。

- rhetorical_function_cn：证明策略对低收入地区更有效，不会扩大健康差距。

- depends_on_cn：Study 2主模型与地区收入数据

- sets_up_cn：为讨论部分‘缩小健康差距’的主张提供量化支持

- evidence_pointer：Table 7

### 42. Discussion P1 S1–S5

- order：42

- section：Discussion

- locator：Discussion P1 S1–S5

- move_code：RESULT

- paraphrase_cn：重述研究问题与全部结果：框架优于中性、晴天损失/阴天增益、可重复使用、效果随动机和人群异质。

- rhetorical_function_cn：把分散的三项实验和机制分析压缩为一段完整回答。

- depends_on_cn：全文所有实证工作

- sets_up_cn：为接下来的贡献声明提供统一梗概

- evidence_pointer：Discussion P1

### 43. Discussion P2–P3 S1–S5

- order：43

- section：Discussion

- locator：Discussion P2–P3 S1–S5

- move_code：CONTRIBUTION

- paraphrase_cn：作者主张研究回应了mHealth可持续性文献缺口，是首批将消息框架与实时天气情境结合并显示重复有效的工作，且不会加宽数字鸿沟。

- rhetorical_function_cn：将实证结果重新接入引言中提出的mHealth缺口。

- depends_on_cn：Study 3和异质性分析结果

- sets_up_cn：为理论贡献部分的更抽象表述做铺垫

- evidence_pointer：Discussion P2-P3

### 44. Discussion P4–P5 S1–S5

- order：44

- section：Discussion

- locator：Discussion P4–P5 S1–S5

- move_code：THEORY_RETURN

- paraphrase_cn：作者用用户动机条件调和情绪一致性与情绪作为资源两种理论：消费性动机时情绪一致性成立，工具性动机时情绪作为资源成立，从而解释健康与营销情境结果的分歧。

- rhetorical_function_cn：从具体应用上升为心理学的理论贡献，是全文最重要的抽象化步骤。

- depends_on_cn：表5的动机分样本结果

- sets_up_cn：为营销等替代场景的应用建议提供理论依据

- evidence_pointer：Discussion P4-P5

### 45. Discussion P6 S1–S4

- order：45

- section：Discussion

- locator：Discussion P6 S1–S4

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：承认研究局限：样本来自亚洲、单一活动追踪应用、仅秋季，未来可扩展到西方用户、其他健康应用类型和其他季节。

- rhetorical_function_cn：保护贡献不被过度一般化，同时为未来研究留出空间。

- depends_on_cn：全文的样本与实施条件

- sets_up_cn：结束全文并给出可继续探索的方向

- evidence_pointer：Discussion 最后一段

## 写作技术

- gap_construction_cn：作者先用公共卫生数据和元分析说明mHealth干预效果不足，然后将原因聚焦到‘忽视天气情境’这一具体变量，指出营销领域已有天气定向但健康情境机制不同，最后叠加两种对立理论预测造成‘理论上不知道该怎么做’的认知缺口；这种三重缺口层层收缩，使研究问题显得既重要、又可行、又有理论张力。

- signposting_cn：引言明确预告‘三个实验’的顺序和各自任务；每个Study开头用‘Having established...’‘Although...’等句子自然衔接；机制部分用‘In this section’引出；Additional Analysis用‘Next’引出收入分组；讨论部分用‘First, Second, Finally’组织贡献。

- transition_logic_cn：Study之间的过渡由逻辑缺口驱动：Study 1证明框架有效→Study 2回答哪种框架在什么天气最优→稳健性和DID回答效果是否稳健和持久→Study 3回答重复使用是否衰减→机制分析回答为什么→替代解释和异质性回答是否真是情绪资源以及对谁有效。每一步都先总结上一步结论，再指出上一步未解决的问题。

- claim_evidence_rhythm_cn：每个主要主张几乎都先呈现‘无模型’直觉（如Figure 2的平均达成率），再做回归估计，最后补稳健性；机制主张用分样本和替代解释检验；论文很少在无证据情况下直接宣称理论胜利。

- benchmark_narrative_cn：baseline不是一次性嵌入，而是随论证演进的链条：Study 1用中性消息作baseline证明框架；Study 2用增益框架作为损失框架的baseline，并用同一用户在不同天气下互为对照；DID用干预前作为baseline；Study 3用每个时期干预前作为baseline；异质性分析用高运动/高收入作为对照。

- theory_return_cn：在机制分析取得分样本结果后，讨论部分不再只谈天气与框架，而是把结果回写成‘用户动机决定情绪是信息还是资源’，并用这一条件化命题去解释营销文献与健康文献之间的表面矛盾，从而完成了从应用结果到理论知识的上升。

- contribution_positioning_cn：作者把贡献分别定位为：应用层面（可持续mHealth）、理论层面（调和两种情绪理论）、实践层面（为企业和政策提供设计指南）；每一条都明确对应引言中的一个缺口，避免出现贡献与问题脱节。

- novelty_protection_cn：为防止成果被看作‘营销天气定向的简单复制’，作者强调健康消息与营销消息机制不同、使用实时天气而非事后匹配、增加重复使用和机制检验、以及低收入/低运动人群的公平含义；这些设计使论文的贡献超越单一性能结果。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：建立现实问题及其严重性，概述已有干预和失败原因。

- research_job_cn：找到领域内公认的痛点（如mHealth干预不持久），并选择一个被忽略但理论上重要的情境变量。

- required_evidence_cn：流行病学统计、meta-analysis或系统综述证明问题规模和现有方案不足。

- transition_to_next_cn：‘尽管已有A、B、C技术，仍存在持续效果差的问题，一个可能原因是忽略了X情境因素。’

#### 2. 2

- step：2

- writing_job_cn：引入近似领域的相关成功技术，随即指出机制差异和理论冲突。

- research_job_cn：说明目标情境与已有成功情境在机制上不同，并列出两种对立的可检验理论。

- required_evidence_cn：理论文献能够形成相反预测，并指出一个调节变量（如动机）可能决定哪种理论成立。

- transition_to_next_cn：‘由于两种理论预测相反，需要通过随机现场实验识别最优设计。’

#### 3. 3

- step：3

- writing_job_cn：将理论转化为具体数字设计：刺激文本、情境分类、实验平台、测量方式。

- research_job_cn：与真实平台合作，完成消息设计、GPS/API匹配、随机化流程和结果追踪。

- required_evidence_cn：能够准确获得用户实时情境（如天气）并随机推送不同处理；有客观行为结果变量。

- transition_to_next_cn：先做一个简单实验验证基础因果，再做一个更严格的实验引入情境交互。

#### 4. 4

- step：4

- writing_job_cn：用递进实验链条回答：是否有效、什么搭配最优、是否稳健、是否持续、是否可重复。

- research_job_cn：设计组间/组内实验、交叉冷却、重复治疗、DID分析和稳健性检验。

- required_evidence_cn：每一步都至少有一个显著性结果和对应的对照/控制策略；稳健性检验覆盖主要威胁。

- transition_to_next_cn：‘在确认效果成立且稳健后，进一步检验机制和异质性。’

#### 5. 5

- step：5

- writing_job_cn：加入机制验证、替代解释排除和异质性分析，使论文从‘What works’走向‘Why and for whom’。

- research_job_cn：利用可获得的额外变量（如用户动机调查、地理数据、既往行为）做分样本分析，并设计能排除竞争机制的证据。

- required_evidence_cn：分样本中有方向可预期的结果；替代解释检验的关键系数不显著；异质性组间差异有统计依据。

- transition_to_next_cn：‘这些结果共同说明，理论机制由用户动机决定，策略对弱势群体更有效。’

#### 6. 6

- step：6

- writing_job_cn：在讨论部分把结果回写到引言缺口：重述核心发现、声明贡献、限定边界、给出实践启示。

- research_job_cn：将分样本机制结论上升为理论命题，并说明局限和未来方向。

- required_evidence_cn：所有贡献声明都能回溯到前述实验或分析；边界条件（地区、应用类型、季节）有明确依据。

- transition_to_next_cn：不要再引入新证据，而是把证据转化为设计知识和理论启示。

### most_transferable_moves_cn

1. 用‘现实问题→现有方案不足→被忽略的情境变量→两种对立理论→实验设计’五步构建引言

2. 先报告‘无模型’平均差异，再用回归给出显著性，最后用稳健性强化——这种证据节奏极易模仿

3. 以‘上一步已证明X，但还没有解决Y’作为Study之间的标准过渡句式

4. 用机制分样本把应用结果提升为理论贡献

5. 用替代解释排除检验保护主机制的解说地位

6. 用异质性分析把策略与公共健康价值联系起来

### resource_intensive_or_nonstandard_parts_cn

1. 需要与拥有大量活跃用户且能实时获取GPS位置的活动追踪应用公司建立深度合作

2. 需要气象API按用户位置实时匹配天气，并设置晴朗/阴云阈值

3. 三次现场实验涉及多批用户、多次推送和15天冷却期，时间与组织成本高

4. 用户动机调查数据并非所有研究都能获得，需要合作方支持

5. 公园可达性数据需要地理信息系统计算公园多边形与用户位置距离

### what_not_to_copy_superficially_cn

1. 不能只复制‘天气×框架’的表述而没有实际随机分配和处理组；没有真实推送与客观步数记录就无法识别因果效应

2. 不能把‘晴天损失、阴天增益’直接当作放之四海皆准的规则，作者自己也表明该结论依赖平台、季节、文化和用户动机

3. 不能在缺少无干预对照组的情况下声称‘重复使用不衰减’，需要至少有自身基线和效应量跨期比较

4. 不能忽略动机调节就直接宣称情绪一致性或情绪作为资源理论被证实；机制证据必须有可预期的方向性

- single_best_description_of_the_routine_cn：先用一个简单随机实验证明核心刺激有效，再用更严格的情境化实验找出最优搭配，然后用稳健性、溢出期、重复使用、机制和异质性分析逐层加固，最后回到理论缺口并给出设计原则。

## 分析边界

本文基于全文文本进行分析，但无法访问在线附录中的完整表格（表A1-A8），部分稳健性细节和平衡检验只能依据正文描述；对表格和图的证据定位依赖论文内的引用与说明，非逐字OCR数据。
