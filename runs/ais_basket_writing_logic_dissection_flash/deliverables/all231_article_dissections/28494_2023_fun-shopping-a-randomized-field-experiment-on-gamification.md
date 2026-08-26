# Fun Shopping: A Randomized Field Experiment on Gamification

- 作者：Yi-Jen (Ian) Ho; Siyuan Liu; Lei Wang
- 年份 / 期刊：2023 / Information Systems Research
- DOI：10.1287/isre.2022.1147
- 源文件：28494_2023_fun-shopping-a-randomized-field-experiment-on-gamification.md
- 论文主类型：field_intervention_or_platform_experiment
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.9

## 文章级论证概况

- 核心问题：在真实线下购物场景中，徽章与排行榜两类游戏化元素能否促进消费者购物参与？与优惠券相比，其效果大小、作用差异、处理后长期持续性以及消费者异质性如何？

- 制品与设计：基于Wi-Fi定位的线下购物游戏化系统：Badge组按店类收集私密且无货币价值的徽章；Leaderboard组按步行距离和到店次数积分并公开排名；Coupon组获随机门店一次性20%折扣券；Control组仅收问候消息。采用四周处理期加四周后处理期的两阶段随机现场实验，共8000名商场访客。

- 客观结果：处理期徽章、排行榜、优惠券分别使销售额提高21.5%、22.5%和31.7%；徽章与排行榜分别使步行距离增加25%和28.4%，使到店次数增加37.9%和33.4%，均强于优惠券；后处理期游戏化组的销售额和探索行为仍显著高于基线，而优惠券效应消退；性别、年龄、收入存在显著异质效应，排行榜组内异质性最高。

- 核心贡献：首次在实体购物中心用位置技术构建在线到线下游戏化环境并开展随机现场实验，同时比较徽章、排行榜与优惠券，证明游戏化在非购买行为上的优势、处理移除后的持续效应、人口统计异质性、组内异质性和探索机制，从而将SDT/SCT扩展到线下零售游戏化领域，并提供可操作的促销与设计策略。

- 整篇论证链：文章先以游戏化市场规模和文献缺口确立其重要性，指出动机机制不明、缺少与货币激励的对照、缺少长期时间维度、缺少用户异质性四类问题，形成四个RQ；随后用自我决定理论解释徽章、用社会比较理论解释排行榜、用货币激励解释优惠券，设计出对应的三类数字干预；在亚洲大型购物中心利用Wi-Fi系统识别、追踪并推送干预，随机分配8000名访客到四组，以处理期加后处理期的两阶段设计识别因果效应与持续性；Tukey检验和ATE回归显示游戏化显著促进销售额、步行距离和到店次数，优惠券短期销售额更强但消退更快；HTE分析显示性别、年龄、收入调节效应，Levene检验和分层贝叶斯模型说明排行榜组内波动最大；新店探索比例和子样本稳健性检验支持探索机制并排除同伴与季节性解释；最后将结果升华为游戏化设计知识、商场管理和目标营销建议。

## 类型与写作弧线判定

- 论文主类型判定：文章的核心证据来自在真实大型购物中心对普通消费者进行的随机现场实验，操纵的是可实际使用的数字游戏化制品（徽章、排行榜、优惠券），并通过位置技术追踪真实行为结果，属于在真实商业环境中进行的数字干预实验。

- 主导写作弧线判定：开篇提出实践和文献问题，然后用SDT和SCT构建理论，将理论转译为三个处理设计，通过现场实验检验，最后在后处理和机制分析中回到理论讨论，并在贡献部分回应开头的四类缺口。

## 研究开展程序

- study_or_phase_count：8

- 研究阶段总序列：理论驱动的处理设计与现场实验实现→平衡检验与描述统计→模型自由证据→ATE回归→跨人口统计HTE→组内异质性→探索机制→稳健性子样本分析。前四阶段建立总体因果效应和持续性，后四阶段逐步打开异质性、机制与边界，形成从平均效应到设计知识的累积论证。

### studies_or_phases

#### 1. 理论驱动的处理设计与现场实验实现

- order：1

- name_cn：理论驱动的处理设计与现场实验实现

- question_cn：如何把SDT、SCT和货币激励转换成可检验的三种处理，并在真实线下场景实现随机化？

- inputs_and_setting_cn：SDT/SCT文献、亚洲大型购物中心、Wi-Fi基础设施、随机抽取的8000名访客

- designed_or_compared_object_cn：四组：私密徽章、公开排行榜、随机门店20%折扣券、无激励对照组

- baseline_control_or_counterfactual_cn：对照组仅接收问候信息；后处理期通过停止处理来观察无干预下的行为

##### objective_metrics

1. 随机分配是否完成

2. 各组样本量是否均衡

3. 处理是否只在处理期送达

- analysis_method_cn：基于理论的干预设计与现场实施

- main_result_cn：四组各2000人；徽章仅本人可见且无货币价值，排行榜每分钟刷新，优惠券随机指定门店；处理在前四周结束时不提前通知。

- argumentative_role_cn：为后续因果估计提供干预定义与识别策略。

- remaining_uncertainty_cn：理论机制尚未直接测量；分组是否可比待平衡检验。

- link_to_next_phase_cn：引出平衡检验以证明随机化和组间可比性。

##### evidence_pointers

1. Section 2.4

2. Section 3.1

3. Table 2

4. Figure 3

#### 2. 平衡检验与描述统计

- order：2

- name_cn：平衡检验与描述统计

- question_cn：随机分组后各组是否可比？样本总体特征如何？

- inputs_and_setting_cn：实验前两个月的个体行为记录、分配后问卷、销售代表满意度调查中的性别年龄收入数据

- designed_or_compared_object_cn：不对处理进行操纵，对四组的分配前行为和分配后人口统计进行组间比较

- baseline_control_or_counterfactual_cn：组间两两t检验和联合F检验，所有比较均以组间等价为预期

##### objective_metrics

1. Money

2. Distance

3. StoreVisits

4. Gender

5. Age

6. Income

7. iOS

- analysis_method_cn：配对t检验、联合F检验、描述统计

- main_result_cn：所有t/F统计量均不显著，说明分配前购物模式和分配后人口统计在各组间无系统差异；人口统计数据回收率达96.1%。

- argumentative_role_cn：建立随机化的可信度，使后续ATE可被解释为因果效应。

- remaining_uncertainty_cn：平衡只说明可观测变量可比，不可观测变量仍可能有差异；需回归控制协变量。

- link_to_next_phase_cn：将比较推进到不控制协变量的模型自由证据。

##### evidence_pointers

1. Section 3.2

2. Table 3

3. Table 4

#### 3. 模型自由证据

- order：3

- name_cn：模型自由证据

- question_cn：不控制协变量时，处理期和后处理期中四组均值是否存在显著差异？

- inputs_and_setting_cn：个体-时期层面的对数化Money、Distance、StoreVisits

- designed_or_compared_object_cn：四组间所有配对均值比较

- baseline_control_or_counterfactual_cn：Control组作为共同参照；处理期与后处理期分别比较

##### objective_metrics

1. log(Money)

2. log(Distance)

3. log(StoreVisits)

- analysis_method_cn：Tukey HSD多重比较

- main_result_cn：处理期三个处理组在三个结果上均高于对照组；优惠券在销售额上更强，徽章和排行榜在距离和到店次数上更强；后处理期游戏化组仍显著高于对照组，优惠券组与对照组差异不再显著。

- argumentative_role_cn：用透明、无模型假设的方式展示原始均值差异，为回归分析提供直观证据。

- remaining_uncertainty_cn：未控制协变量和个体聚类，无法给出精确效应量。

- link_to_next_phase_cn：作者明确说为了量化处理效应，进入回归分析。

##### evidence_pointers

1. Section 3.3

2. Table 5

#### 4. 平均处理效应估计

- order：4

- name_cn：平均处理效应估计

- question_cn：控制协变量后，三种处理对销售额、步行距离、到店次数的ATE是多少？处理移除后是否持续？

- inputs_and_setting_cn：8000名个体、16000条个体-时期观测，含处理组虚拟变量、Post、交互项和人口统计控制

- designed_or_compared_object_cn：Badge、Leaderboard、Coupon与Control的比较；Post交互刻画后处理期衰减

- baseline_control_or_counterfactual_cn：Control组；Post项用于识别时间趋势

##### objective_metrics

1. log(Money)

2. log(Distance)

3. log(StoreVisits)

4. 经济显著性：美元、英里、店数

- analysis_method_cn：OLS，个体层面聚类稳健标准误，系数指数化转为百分比

- main_result_cn：处理期徽章、排行榜、优惠券分别使销售额提高21.5%、22.5%、31.7%；徽章和排行榜使距离提升25%和28.4%、到店次数提升37.9%和33.4%；后处理期游戏化组仍显著高于控制，优惠券基本消退。

- argumentative_role_cn：给出全篇核心因果估计，并区分货币刺激与游戏化在不同结果上的优势。

- remaining_uncertainty_cn：平均效应可能掩盖不同人群的差异。

- link_to_next_phase_cn：进入跨人口统计HTE分析，回答细分人群如何响应。

##### evidence_pointers

1. Section 4.1

2. Table 6

#### 5. 跨人口统计异质性分析

- order：5

- name_cn：跨人口统计异质性分析

- question_cn：性别、年龄、收入是否调节三种处理的效应？

- inputs_and_setting_cn：个体-时期面板，加入Gender、age、income与处理的二阶和三阶交互

- designed_or_compared_object_cn：女性/男性、平均年龄上下、收入高低对处理反应差异；处理期与后处理期分别考察

- baseline_control_or_counterfactual_cn：基准为女性、平均年龄、平均收入；交互项刻画男性、年龄偏离、收入偏离

##### objective_metrics

1. log(Money)

2. log(Distance)

3. log(StoreVisits)

- analysis_method_cn：带三方交互的OLS

- main_result_cn：女性更偏好优惠券，男性更受游戏化吸引；年轻人更积极参与游戏，优惠券近似全年龄策略；高收入人群对徽章反应更强，低收入人群对排行榜反应更强。

- argumentative_role_cn：说明游戏化不是统一效果，为定向营销和理论上的边界条件提供证据。

- remaining_uncertainty_cn：可观测人口统计仍不能解释同一人群内部反应差异。

- link_to_next_phase_cn：自然引入组内异质性分析。

##### evidence_pointers

1. Section 4.2

2. Tables 7-9

#### 6. 组内异质性分析

- order：6

- name_cn：组内异质性分析

- question_cn：各处理组内部个体反应差异有多大？排行榜是否呈现双刃剑特征？

- inputs_and_setting_cn：个体-访问次层面的支出数据，处理组虚拟变量，人口控制

- designed_or_compared_object_cn：比较Badge、Leaderboard、Coupon三组的个体斜率方差

- baseline_control_or_counterfactual_cn：组间方差比较；分层模型以个人随机系数捕捉异质性

##### objective_metrics

1. Levene/F统计量

2. 协方差矩阵对角元素

- analysis_method_cn：Levene’s方差检验与层次贝叶斯随机系数模型（Gibbs抽样）

- main_result_cn：Leaderboard组内异质性最高，Coupon最低，Badge居中；说明排行榜鼓励部分人自我强化、部分人自我放逐，徽章相对均衡。

- argumentative_role_cn：把平均效应升级为对刺激性质的理论区分：社会比较可产生两极分化，徽章更适合大众参与。

- remaining_uncertainty_cn：方差差异只是间接证据，未直接观测社会比较心理过程。

- link_to_next_phase_cn：转向探索机制，检验探索是否解释效应。

##### evidence_pointers

1. Section 4.3

2. Tables 10-11

#### 7. 探索机制分析

- order：7

- name_cn：探索机制分析

- question_cn：游戏化是否通过促使人访问新店来产生销售额、距离和到店参与？

- inputs_and_setting_cn：实验前两月已访问店作为已知店，识别整个实验窗口中的新店；构造新店结果占总结果比例

- designed_or_compared_object_cn：用RatioNewStore替换原始结果，重新估计Equation (1)

- baseline_control_or_counterfactual_cn：Control组的新店比例作为反事实

##### objective_metrics

1. 新店支出比例

2. 新店距离比例

3. 新店到访比例

- analysis_method_cn：OLS

- main_result_cn：处理期三个处理组的新店活动均显著高于控制，后处理期探索效应减小但游戏化组仍保留更多参与；探索是一种由游戏引起的即时行动机制。

- argumentative_role_cn：将观察到的销售和参与提升与理论动机机制连接起来，说明游戏化既带来临时探索也产生持久参与。

- remaining_uncertainty_cn：该分析是近似机制检验，并非正式中介分析；未排除同伴和季节因素。

- link_to_next_phase_cn：通过子样本排除伴随购物和季节性。

##### evidence_pointers

1. Section 5.1

2. Table 12

#### 8. 稳健性子样本分析

- order：8

- name_cn：稳健性子样本分析

- question_cn：排除同伴购物和暑季节性后，主结果是否依然成立？

- inputs_and_setting_cn：Wi-Fi检测到的同伴设备数据、问卷中的单独购物回答、年龄大于22岁的非学生子样本

- designed_or_compared_object_cn：在Noncompanion子样本和Nonstudent子样本上重估Equation (1)

- baseline_control_or_counterfactual_cn：原始全样本ATE作为参照

##### objective_metrics

1. log(Money)

2. log(Distance)

3. log(StoreVisits)

- analysis_method_cn：子样本OLS

- main_result_cn：非结伴购物和非学生消费者中，游戏化和优惠券的方向与显著性基本保持，说明结果不受同伴诱导和暑期学生流量驱动。

- argumentative_role_cn：保护主结果的内部与外部有效性，排除常见替代解释。

- remaining_uncertainty_cn：仍只覆盖单一商场、单一游戏参数和特定夏季窗口，未检验其他游戏元素与长期跨越。

- link_to_next_phase_cn：进入结论，将稳健经验总结为理论贡献和管理策略。

##### evidence_pointers

1. Section 5.2

2. Tables 13-14

## 各部分修辞架构

### abstract_moves

1. CONTEXT: 游戏化使用游戏元素提升参与并广泛部署

2. PRACTICAL_STAKES: 用作营销装置提升销售和忠诚

3. PHENOMENON: 聚焦徽章与排行榜两种关键游戏元素

4. STUDY_OVERVIEW: 在亚洲最大商场之一开展随机现场实验，对比优惠券

5. METHOD_JUSTIFICATION: 两期设计识别处理移除后的长期行为变化

6. RESULT: 处理期徽章、排行榜、优惠券分别提升销售21.5%、22.5%、31.7%

7. RESULT: 后处理期游戏化效应仍显著，优惠券消退

8. RESULT: 人口统计异质性和组内异质性显著不同

9. RESULT: 游戏化带来更多探索和额外销售

10. CONTRIBUTION: 结果可转化为主动利用游戏化的行动策略

### introduction_moves

1. CONTEXT: 游戏化定义及全球市场增长

2. PRACTICAL_STAKES: 企业用游戏化提升报销、训练、忠诚

3. PRIOR_KNOWLEDGE: 文献集中在badges与leaderboards并发现积极关系

4. GAP: 底层机制不清晰，营销知识尤其缺乏

5. WHY_GAP_MATTERS: 缺少因果推断、缺少与优惠券对照、缺少时间分析、缺少用户异质性

6. RQ_OR_OBJECTIVE: 提出四个研究问题

7. THEORY_INTRO: SDT与SCT作为理论基础

8. DESIGN_FEATURE: 徽章对应自决、排行榜对应社会比较、优惠券对应货币激励

9. STUDY_OVERVIEW: 大规模随机现场实验、两期设计、四组分配

10. RESULT: 两类游戏化促进销售和探索，优惠券销售更强但消退更快

11. RESULT: 异质性分析发现性别、年龄、收入和组内差异

12. MECHANISM: 探索机制和长期内在动机

13. CONTRIBUTION: 新情境、因果推断、时间范围、异质性四类贡献

14. BOUNDARY_CONDITION: 对商场管理和游戏设计给出可操作建议

15. TRANSITION: 论文结构预告

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE: 文献总结UGC、健康、教育中的游戏化结果

2. LIMITATION: 盈利相关和线下购物证据有限

3. GAP: 研究多孤立分析单一元素，未与货币激励对照

4. GAP: 缺乏随机现场实验和长期时间窗口

5. GAP: 异质性未被主动研究

6. THEORY_INTRO: SDT关于能力、自主、归属以及外在激励内化的命题

7. THEORY_PROPOSITION: 徽章通过能力反馈、自主选择和归属感激发内在动机

8. REQUIREMENT: 徽章应无货币价值、私密访问、无社会互动以对齐SDT

9. THEORY_INTRO: SCT关于上行与下行社会比较的命题

10. THEORY_PROPOSITION: 排行榜提供同时上行和下行比较，可能双刃剑

11. THEORY_PROPOSITION: 基于SDT和SCT的长期效应预测

### artifact_design_moves

1. REQUIREMENT: 用Wi-Fi识别、追踪和推送处理

2. STUDY_OVERVIEW: 两期各四周，处理期和后处理期

3. METHOD_JUSTIFICATION: 随机分配日期、即时推送、自动注册避免自选择

4. DESIGN_FEATURE: 徽章按店类收集且仅本人可见

5. DESIGN_FEATURE: 排行榜按距离和到店积分并公开刷新

6. DESIGN_FEATURE: 优惠券随机指定门店并一次性使用以避免选择偏差

7. BENCHMARK_OR_CONTRAST: 四组设计使游戏化与货币激励可直接比较

### evaluation_moves

1. METHOD_JUSTIFICATION: 平衡检验采用配对t和联合F

2. BENCHMARK_OR_CONTRAST: 用Tukey同时比较多组均值

3. METHOD_JUSTIFICATION: OLS聚类标准误并加入Post交互识别长期变化

4. HYPOTHESIS_OR_PROPOSITION: 协变量包括性别、年龄、收入、iOS

5. RESULT: ATE和经济显著性

6. HYPOTHESIS_OR_PROPOSITION: 人口统计交互项用于HTE

7. METHOD_JUSTIFICATION: Levene和分层贝叶斯用于组内异质性

8. MECHANISM: 用新店探索比例做机制检验

9. ROBUSTNESS_OR_BOUNDARY_TEST: 非结伴和非学生子样本

### discussion_and_contribution_moves

1. RESULT: 重新报告主结果并强调游戏化的持续效应

2. CONTRIBUTION: 新情境、随机现场实验、时间范围、异质性、位置型游戏化

3. BOUNDARY_CONDITION: 管理建议限定于游戏化与优惠券在购物场景的比较

4. LIMITATION_AND_FUTURE: 游戏设计非完全等动作、其他元素、门店特定优惠券、互补替代未研究

5. CONTRIBUTION: 结论重新连接引言中提出的四类缺口

## 理论/知识到设计的翻译

### 知识/理论基础

1. 自我决定理论（SDT）

2. 社会比较理论（SCT）

3. 货币激励/经典促销理论

4. 游戏化实证文献

5. 位置服务与移动营销文献

- 理论—设计耦合：direct

- 耦合判定理由：理论在实验设计之前就被用于选择三个处理并决定其关键属性：徽章被设计为私密无货币价值以对齐SDT内化机制，排行榜被设计为公开排名以激活SCT，优惠券被设计为随机门店折扣以代表货币激励；这些设计差异随后直接通过随机现场实验被检验。

- 理论到设计翻译链：SDT：满足能力/自主/归属并可将外部干预内化 → 设计无货币价值的私密徽章作为成就反馈 → Badge组；SCT：公开排名触发上行和下行社会比较 → 鼓励步行距离和到店次数并公开刷新分数 → Leaderboard组；货币激励：折扣降低价格、立即促成购买 → 随机门店20%折扣券 → Coupon组；长期预测：SDT/SCT文献认为内在化动机和社会比较可持久 → 两期设计观察处理移除后的行为。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：SDT认为满足能力、自主和归属需求会促进自我决定，外部奖励可被内化为内在动机。

- mechanism_cn：徽章提供完成任务的胜任反馈、给用户选择任务的自主性，并通过与环境的联结提升归属感。

- design_requirement_cn：徽章应作为成就展示但不应携带货币价值；应具有收集性和私密性，避免社会比较混淆。

- artifact_choice_cn：九个店类的Unique Badge，购买相应门店后获得，仅本人可查看。

- evaluated_contrast_cn：Badge vs Control、Badge vs Coupon；处理期与后处理期比较。

- objective_result_cn：Badge组销售额提升21.5%，距离提升25%，到店次数提升37.9%；后处理期仍显著。

##### evidence_pointers

1. Section 2.2

2. Table 2

3. Figure 3(a)

4. Table 6

#### 2. 2

- theory_or_knowledge_claim_cn：SCT认为个体通过与他人的比较评价自己，上行比较可激发努力，下行比较可带来优越感但也可能造成压力。

- mechanism_cn：公开排行榜让参与者同时看到自己与他人排名，产生自我强化或自我放逐。

- design_requirement_cn：排行榜应公开、实时更新，并以与购物相关的行为（步行距离、到店次数）作为排名依据。

- artifact_choice_cn：Leaderboard：每走100米得1分、每次到店得20分，公开排名每分钟刷新。

- evaluated_contrast_cn：Leaderboard vs Control、Leaderboard vs Coupon；组内方差比较。

- objective_result_cn：Leaderboard组销售额提升22.5%，距离提升28.4%，到店次数提升33.4%；组内异质性最高。

##### evidence_pointers

1. Section 2.3

2. Table 2

3. Figure 3(b)

4. Tables 6, 10, 11

#### 3. 3

- theory_or_knowledge_claim_cn：货币激励直接降低支付价格，是零售中最常见的短期促销工具。

- mechanism_cn：20%折扣券降低特定门店购买成本，促使立即消费但不必然改变商店探索行为。

- design_requirement_cn：优惠券应随机化门店以避免店类选择偏差；一次性使用以避免长期依赖。

- artifact_choice_cn：Coupon：在九个店类中随机抽取门店，发放一次性20%折扣QR码。

- evaluated_contrast_cn：Coupon vs Control、Coupon vs Badge/Leaderboard；处理期与后处理期比较。

- objective_result_cn：Coupon组销售额提升31.7%，但距离仅增15.6%、到店次数增10.8%；后处理期效应基本消失。

##### evidence_pointers

1. Section 3.1

2. Table 2

3. Figure 3(c)

4. Table 6

#### 4. 4

- theory_or_knowledge_claim_cn：SDT/SCT长期研究指出，自主与能力支持、社会比较可带来持续的行为改变。

- mechanism_cn：徽章内化为内在动机，排行榜通过社会比较塑造身份认同和持续动力；两者均可能产生处理移除后的持久效应。

- design_requirement_cn：实验需要包含处理停止后的观察期，才能区分短暂刺激与长期行为塑造。

- artifact_choice_cn：两期设计：前四周发送处理，后四周无处理但不提前告知。

- evaluated_contrast_cn：处理期主效应 vs 后处理期交互项；比较游戏化与优惠券的衰减速度。

- objective_result_cn：处理后游戏化组仍显著高于对照组，优惠券与对照组几乎无差异。

##### evidence_pointers

1. Section 2.4

2. Section 3.1

3. Table 6

## 评价逻辑

### evaluation_modes

1. 大型随机现场实验

2. Tukey HSD模型自由均值比较

3. 带聚类的OLS回归与处理-Post交互

4. 跨人口统计交互回归（HTE）

5. Levene方差检验与层次贝叶斯随机系数模型

6. 新店探索比例的机制检验

7. 子样本稳健性检验

- why_these_evaluations_cn：需要同时回答因果效应、与优惠券的相对大小、处理移除后的持续性、用户异质性、机制和替代解释；因此从随机化→平衡→模型自由证据→ATE→HTE→组内异质性→机制→稳健性逐层递进。

- benchmark_and_contrast_chain_cn：Control组构成零干预基准；Coupon组作为货币激励基准，使游戏化效应不只是在有无游戏间比较，还与非游戏促销比较；Post交互使后处理期成为处理停止后的反事实延续；Levene和层次模型通过方差比较区分不同刺激内部的分化程度。

### claim_evidence_ledger

#### 1. 徽章、排行榜、优惠券都能提升线下购物参与

- claim_cn：徽章、排行榜、优惠券都能提升线下购物参与

- evidence_cn：Tukey检验、Table 6的Badge/Leaderboard/Coupon系数均显著为正

- assessment_cn：因果推断可信，随机现场实验和平衡检验支持

#### 2. 游戏化在非购买行为（距离、到店）上优于优惠券

- claim_cn：游戏化在非购买行为（距离、到店）上优于优惠券

- evidence_cn：Table 5/6中Badge和Leaderboard在距离与到店上的系数大于Coupon

- assessment_cn：证据充分，差异在处理期稳定存在

#### 3. 游戏化具有处理移除后的持续效应，优惠券消退

- claim_cn：游戏化具有处理移除后的持续效应，优惠券消退

- evidence_cn：Table 6中Badge*Post和Leaderboard*Post为负但显著小于主效应，Coupon*Post几乎完全抵消主效应

- assessment_cn：由两期设计直接支持，但未跟踪更长时间窗口

#### 4. 性别、年龄、收入调节游戏化和优惠券效果

- claim_cn：性别、年龄、收入调节游戏化和优惠券效果

- evidence_cn：Tables 7-9中的两/三向交互显著

- assessment_cn：统计证据明确，但机制解释是推测性的

#### 5. 排行榜组内异质性最高，可能形成自我强化/自我放逐

- claim_cn：排行榜组内异质性最高，可能形成自我强化/自我放逐

- evidence_cn：Table 10的Levene F和Table 11协方差对角元素显示Leaderboard方差最大

- assessment_cn：方差证据与SCT一致，但没有直接心理测量

#### 6. 游戏化通过探索新店产生额外参与

- claim_cn：游戏化通过探索新店产生额外参与

- evidence_cn：Table 12中处理期RatioNewStore显著为正，Post交互为负

- assessment_cn：支持探索机制，但非正式中介检验

#### 7. 同伴购物和季节性不驱动主结果

- claim_cn：同伴购物和季节性不驱动主结果

- evidence_cn：Tables 13-14非结伴和非学生子样本结果仍显著

- assessment_cn：稳健性良好

- internal_validity_strategy_cn：随机分配、双期平衡检验、自动入组防自选择、不提前通知处理结束、Wi-Fi客观追踪、控制组时间趋势不显著、聚类标准误、子样本排除同伴与季节性。

- external_validity_strategy_cn：真实大型购物中心、普通消费者而非学生样本、非学生子样本、大规模8000人；但单一商场和单一商圈仍限制普适性。

- what_is_not_actually_tested_cn：SDT中的胜任感、自主性、归属感以及SCT中的上行/下行比较心理状态没有被直接测量；探索效应只是结果比例而非正式中介；未检验游戏化与优惠券的互补/替代；未涉及其他游戏元素或参数变化；未做跨商场复制。

## 贡献闭环

- technical_claim_cn：基于Wi-Fi位置技术构建线下游戏化环境，并用随机现场实验量化三种促销机制对销售和探索行为的影响；在技术上证明了位置型游戏化可用于真实零售场景。

- artifact_claim_cn：具体设计差异（私密徽章vs公开排行榜vs折扣券）导致了结果差异：徽章带来平衡参与，排行榜带来更高组内分化，优惠券带来更强短期支出。

- mechanism_claim_cn：游戏化通过临时的‘行动召唤’探索机制和更持久的内在动机重塑行为，使处理停止后仍维持参与。

- boundary_claim_cn：游戏化对男性、年轻人、不同的收入群体效果不同；排行榜对高竞争人群有效但可能放逐低动力人群；优惠券是短期、全年龄、女性偏好的工具；结果在非结伴购物和非学生样本中稳健。

- reusable_design_knowledge_cn：若目标是拉动销售额，优惠券短期最强；若目标是增加商场内探索、到店和长期客户关系，徽章适合大众、排行榜适合识别和激励高自我驱动人群；设计应将激励规则与目标行为对齐，并利用位置追踪动态配置。

- theoretical_contribution_cn：将SDT和SCT从在线、课堂、穿戴设备情境扩展到实体零售购物场景；用组内异质性刻画排行榜的双刃剑特征；用两期设计将理论上的长期内化预测操作化为可检验的处理移除效应。

- how_discussion_closes_intro_gap_cn：结论部分逐条回应引言中的四个RQ：存在因果效应、与优惠券相比有差异、后处理期持续、异质性存在；同时也对应引言中四类文献缺口（机制、对照、时间、异质性），完成了问题-理论-设计-检验-返回理论的回环。

- overclaim_or_unsupported_leaps_cn：作者在摘要和结论中使用‘重塑消费者行为’和‘长期影响’，但只有四周后处理期，严格说是中期持续效应；将方差差异解释为自我强化/自我放逐还缺乏直接心理证据；‘first’类表述依赖文献检索范围；探索机制是基于结果比例的间接证据，可能只是相关而非因果机制。

## 句级写作动作图谱

### 1. Abstract P1 S1

- order：1

- section：Abstract

- locator：Abstract P1 S1

- move_code：CONTEXT

- paraphrase_cn：游戏化通过游戏性特征吸引参与者，并在多种场景中广泛部署。

- rhetorical_function_cn：用领域常识为全文定调，说明游戏化的普遍性。

- depends_on_cn：无

- sets_up_cn：为后续指出游戏化的商业意义和研究缺口铺垫。

- evidence_pointer：Abstract开头

### 2. Abstract P1 S2

- order：2

- section：Abstract

- locator：Abstract P1 S2

- move_code：PRACTICAL_STAKES

- paraphrase_cn：这种由IT支持的参与策略被用作提高销售和客户忠诚的营销工具。

- rhetorical_function_cn：把游戏化从设计现象转化为商业营销问题。

- depends_on_cn：依赖于游戏化广泛使用的背景。

- sets_up_cn：提示本文关注营销相关结果而非一般参与。

- evidence_pointer：Abstract第1段

### 3. Abstract P2 S1

- order：3

- section：Abstract

- locator：Abstract P2 S1

- move_code：PHENOMENON

- paraphrase_cn：本研究聚焦徽章和排行榜两种重要游戏元素，它们促进消费者动机和社会比较。

- rhetorical_function_cn：将研究范围缩小到两个具体游戏元素。

- depends_on_cn：游戏化一般背景。

- sets_up_cn：暗示后面将以SDT解释徽章、SCT解释排行榜。

- evidence_pointer：Abstract第2段

### 4. Abstract P2 S2

- order：4

- section：Abstract

- locator：Abstract P2 S2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：为量化影响，在亚洲最大商场之一进行随机现场实验，并将两个元素与优惠券比较。

- rhetorical_function_cn：宣称方法贡献和比较基准。

- depends_on_cn：前一句定义了研究对象。

- sets_up_cn：说明实验设计的关键：随机、现场、多处理对照。

- evidence_pointer：Abstract第2段

### 5. Abstract P2 S3

- order：5

- section：Abstract

- locator：Abstract P2 S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：两期设计包含处理期和后处理期，用于识别处理移除后的长期行为变化。

- rhetorical_function_cn：强调两期设计对长期推断的必要性。

- depends_on_cn：随机现场实验总体设计。

- sets_up_cn：为后文持续效应结果做预告。

- evidence_pointer：Abstract第2段

### 6. Abstract P3 S1

- order：6

- section：Abstract

- locator：Abstract P3 S1

- move_code：RESULT

- paraphrase_cn：主结果显示徽章和排行榜在处理期分别促进销售21.5%和22.5%，而优惠券带来更强的31.7%提升。

- rhetorical_function_cn：给出最核心的定量结果。

- depends_on_cn：实验设计。

- sets_up_cn：让读者注意到优惠券短期更强，为后文非购买行为和持续性反转铺垫。

- evidence_pointer：Abstract第3段

### 7. Abstract P4 S1

- order：7

- section：Abstract

- locator：Abstract P4 S1

- move_code：RESULT

- paraphrase_cn：后处理期游戏化影响相对基线仍显著，但优惠券影响消退。

- rhetorical_function_cn：突出游戏化的长期/持续优势。

- depends_on_cn：两期设计。

- sets_up_cn：支撑全文对游戏化长期价值的解释。

- evidence_pointer：Abstract第4段

### 8. Abstract P5 S1

- order：8

- section：Abstract

- locator：Abstract P5 S1

- move_code：RESULT

- paraphrase_cn：额外分析显示跨人口统计的显著异质处理效应，且各处理内部异质性差异明显。

- rhetorical_function_cn：预告异质性贡献。

- depends_on_cn：前面平均效应的存在。

- sets_up_cn：引出后文HTE和组内异质性。

- evidence_pointer：Abstract第5段

### 9. Abstract P6 S1

- order：9

- section：Abstract

- locator：Abstract P6 S1

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：游戏化带来更多探索，并产生额外销售和参与；总体结果是稳健的。

- rhetorical_function_cn：给出机制和稳健性结论。

- depends_on_cn：主结果和异质性结果。

- sets_up_cn：表明研究不只是平均效应，还有机制和边界。

- evidence_pointer：Abstract第6段

### 10. Introduction P1 S1-S2

- order：10

- section：Introduction

- locator：Introduction P1 S1-S2

- move_code：CONTEXT

- paraphrase_cn：游戏化被定义为在非游戏情境中使用游戏设计元素，在教育、商业和健康中潜力巨大；2019年全球市场72亿美元，预计2024年超400亿。

- rhetorical_function_cn：用市场规模和定义为研究提供现实重要性。

- depends_on_cn：无

- sets_up_cn：支撑后面‘需要研究’的论断。

- evidence_pointer：Introduction第1段

### 11. Introduction P1 S3

- order：11

- section：Introduction

- locator：Introduction P1 S3

- move_code：PRACTICAL_STAKES

- paraphrase_cn：Google、Deloitte、Samsung等公司用游戏化改善报销、培训和利益相关者关系。

- rhetorical_function_cn：举例证明游戏化已是现实商业实践。

- depends_on_cn：游戏化市场背景。

- sets_up_cn：为后文面向管理者的贡献做铺垫。

- evidence_pointer：Introduction第1段

### 12. Introduction P2 S1

- order：12

- section：Introduction

- locator：Introduction P2 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：游戏化文献主要研究徽章和排行榜，并在教育、商业、健康中发现积极关系。

- rhetorical_function_cn：总结已有证据，说明领域研究现状。

- depends_on_cn：游戏化一般背景。

- sets_up_cn：为下面指出缺口提供对照。

- evidence_pointer：Introduction第2段

### 13. Introduction P3 S1

- order：13

- section：Introduction

- locator：Introduction P3 S1

- move_code：GAP

- paraphrase_cn：尽管证据增长，底层驱动用户行为的机制仍不清楚。

- rhetorical_function_cn：指出机制性缺口。

- depends_on_cn：已有积极关系文献。

- sets_up_cn：引出研究动机之一。

- evidence_pointer：Introduction第3段

### 14. Introduction P3 S2-S5

- order：14

- section：Introduction

- locator：Introduction P3 S2-S5

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：营销领域知识尤其欠缺：难以用细粒度数据做因果推断；需要与非货币激励对比货币优惠券；长期时间分析被忽略；用户特征如何影响游戏化行为没有被主动研究。

- rhetorical_function_cn：把一般机制缺口细化为四个具体的文献和理论缺口，并说明后果。

- depends_on_cn：文献总结。

- sets_up_cn：直接生成四个研究问题。

- evidence_pointer：Introduction第3段

### 15. Introduction P4 S1

- order：15

- section：Introduction

- locator：Introduction P4 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：这些缺口导致四个研究问题：游戏化能否促进购物参与？与优惠券有何不同？游戏停止后是否可持续？不同消费者如何响应不同游戏特征？

- rhetorical_function_cn：明确研究问题，作为全文指南。

- depends_on_cn：前面四个缺口。

- sets_up_cn：决定后续理论选择和实验设计。

- evidence_pointer：Introduction第4段

### 16. Introduction P5 S1

- order：16

- section：Introduction

- locator：Introduction P5 S1

- move_code：THEORY_INTRO

- paraphrase_cn：游戏化文献中以自我决定理论和社会比较理论作为理论基础。

- rhetorical_function_cn：引入解释机制的理论框架。

- depends_on_cn：四个RQ需要理论回答。

- sets_up_cn：为设计徽章与排行榜对齐机制做铺垫。

- evidence_pointer：Introduction第5段

### 17. Introduction P6 S1

- order：17

- section：Introduction

- locator：Introduction P6 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：本研究同时用可收集徽章、公开排行榜和优惠券来激发自决、社会比较和货币激励。

- rhetorical_function_cn：说明三个处理与三种理论机制的一一对应。

- depends_on_cn：SDT/SCT理论。

- sets_up_cn：后面的实验设计细节由此而来。

- evidence_pointer：Introduction第6段

### 18. Introduction P6 S2-S4

- order：18

- section：Introduction

- locator：Introduction P6 S2-S4

- move_code：MECHANISM

- paraphrase_cn：徽章无货币价值且仅本人可看，由自我满足驱动；排行榜公开排名让消费者与同伴比较；优惠券提供额外金钱激励。

- rhetorical_function_cn：用机制解释为何选择特定设计属性。

- depends_on_cn：SDT/SCT/货币激励理论。

- sets_up_cn：为实验组定义提供理论合法性。

- evidence_pointer：Introduction第6段

### 19. Introduction P7 S1-S3

- order：19

- section：Introduction

- locator：Introduction P7 S1-S3

- move_code：STUDY_OVERVIEW

- paraphrase_cn：与亚洲最大购物中心合作，用Wi-Fi系统识别访客、追踪轨迹并推送处理，随机分配到Badge、Leaderboard、Coupon、Control四组。

- rhetorical_function_cn：说明实验的规模和实施方式。

- depends_on_cn：处理设计。

- sets_up_cn：为实证结果来源提供上下文。

- evidence_pointer：Introduction第7段

### 20. Introduction P8 S1-S3

- order：20

- section：Introduction

- locator：Introduction P8 S1-S3

- move_code：RESULT

- paraphrase_cn：徽章、排行榜和优惠券都有效激励购物参与；处理期徽章和排行榜分别使收入增加21.5%和22.5%，优惠券增加31.7%；但游戏化在距离和到店上比优惠券更强。

- rhetorical_function_cn：预告第一组主要实证发现。

- depends_on_cn：现场实验。

- sets_up_cn：引导读者期待后续ATE细表。

- evidence_pointer：Introduction第8段

### 21. Introduction P9 S1-S3

- order：21

- section：Introduction

- locator：Introduction P9 S1-S3

- move_code：RESULT

- paraphrase_cn：后处理期游戏化组的参与仍然显著，优惠券效应快速消退；女性偏爱优惠券，男性偏爱游戏，年轻人更受游戏吸引，高收入者偏向徽章、低收入者偏向排行榜。

- rhetorical_function_cn：预告持续效应和异质性结果。

- depends_on_cn：两期设计和HTE分析。

- sets_up_cn：为后文贡献三和贡献四做准备。

- evidence_pointer：Introduction第9段

### 22. Introduction P10 S1-S2

- order：22

- section：Introduction

- locator：Introduction P10 S1-S2

- move_code：MECHANISM

- paraphrase_cn：扩展分析发现探索效应在处理期存在、移除后减弱，长期行为变化可能来自消费者内在动机。

- rhetorical_function_cn：提前公布机制结果。

- depends_on_cn：机制分析。

- sets_up_cn：使贡献不局限于平均效应。

- evidence_pointer：Introduction第10段

### 23. Introduction P11 S1-S4

- order：23

- section：Introduction

- locator：Introduction P11 S1-S4

- move_code：CONTRIBUTION

- paraphrase_cn：贡献包括：新情境（实体商场）、随机现场实验、考虑处理与后处理期的时间维度、全面探索人口统计异质性和组内异质性。

- rhetorical_function_cn：直接声明研究贡献，对应引言缺口。

- depends_on_cn：全部实证结果。

- sets_up_cn：为结论部分的贡献列表提供早期预告。

- evidence_pointer：Introduction第11段

### 24. Introduction P12 S1-S3

- order：24

- section：Introduction

- locator：Introduction P12 S1-S3

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：结果可以转化为商场管理、游戏设计和实时定向策略。

- rhetorical_function_cn：强调实践可操作性。

- depends_on_cn：贡献声明。

- sets_up_cn：为结论中的管理启示做准备。

- evidence_pointer：Introduction第12段

### 25. Introduction P13 S1

- order：25

- section：Introduction

- locator：Introduction P13 S1

- move_code：TRANSITION

- paraphrase_cn：论文其余部分预定：理论、实验、实证、机制、结论。

- rhetorical_function_cn：给出阅读地图。

- depends_on_cn：前面所有预告。

- sets_up_cn：组织后文结构。

- evidence_pointer：Introduction最后一段

### 26. Section 2.1 P1

- order：26

- section：Section 2.1

- locator：Section 2.1 P1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：游戏化利用游戏元素在非游戏场景中参与用户，徽章和排行榜是应用最广的两个元素。

- rhetorical_function_cn：建立文献领域并提供两个处理的理论背景。

- depends_on_cn：引言。

- sets_up_cn：后面UGC/健康/教育文献分类。

- evidence_pointer：Section 2.1第1段

### 27. Section 2.1 P2

- order：27

- section：Section 2.1

- locator：Section 2.1 P2

- move_code：LIMITATION

- paraphrase_cn：文献开始研究游戏化对盈利的影响但证据有限，线下购物场景尤其缺乏。

- rhetorical_function_cn：突出文献缺口。

- depends_on_cn：前面文献综述。

- sets_up_cn：为补缺贡献提供依据。

- evidence_pointer：Section 2.1第2段

### 28. Section 2.1 P2后

- order：28

- section：Section 2.1

- locator：Section 2.1 P2后

- move_code：GAP

- paraphrase_cn：由于线上环境技术限制，难以研究真实线下购物中游戏化与消费者行为的关系。

- rhetorical_function_cn：说明为什么线下证据缺失。

- depends_on_cn：线上文献。

- sets_up_cn：引出本研究的位置型游戏化环境。

- evidence_pointer：Section 2.1第2段末

### 29. Section 2.1 P3

- order：29

- section：Section 2.1

- locator：Section 2.1 P3

- move_code：GAP

- paraphrase_cn：以往研究通常只单独研究徽章或排行榜，而本研究在统一情境中同时研究两个元素，并以货币激励为基准。

- rhetorical_function_cn：对比文章与既有文献的差异。

- depends_on_cn：代表性文献表。

- sets_up_cn：为实验多臂设计辩护。

- evidence_pointer：Section 2.1第3段

### 30. Section 2.1 P4

- order：30

- section：Section 2.1

- locator：Section 2.1 P4

- move_code：GAP

- paraphrase_cn：文献多依赖调查、实验室和针对特定群体的档案分析，缺少随机现场实验。

- rhetorical_function_cn：指出方法缺口。

- depends_on_cn：Hamari et al. (2014)呼吁。

- sets_up_cn：支撑随机现场实验的选择。

- evidence_pointer：Section 2.1第4段

### 31. Section 2.1 P5

- order：31

- section：Section 2.1

- locator：Section 2.1 P5

- move_code：GAP

- paraphrase_cn：文献缺少更长时间范围的分析，很少关注游戏化停止后的行为变化。

- rhetorical_function_cn：指出时间维度缺口。

- depends_on_cn：Tobon et al. (2020)等。

- sets_up_cn：为两期设计提供依据。

- evidence_pointer：Section 2.1第5段

### 32. Section 2.1 P6

- order：32

- section：Section 2.1

- locator：Section 2.1 P6

- move_code：GAP

- paraphrase_cn：以往研究多把人口统计当作控制变量，较少主动研究异质性。

- rhetorical_function_cn：指出异质性缺口。

- depends_on_cn：人口统计文献。

- sets_up_cn：引出HTE分析。

- evidence_pointer：Section 2.1第6段

### 33. Section 2.2 P1

- order：33

- section：Section 2.2

- locator：Section 2.2 P1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：关于徽章的研究结果混杂，包括积极、消极和无效果。

- rhetorical_function_cn：说明徽章效果不确定性。

- depends_on_cn：UGC/教育文献。

- sets_up_cn：为用SDT解释徽章机制做铺垫。

- evidence_pointer：Section 2.2第1段

### 34. Section 2.2 P2

- order：34

- section：Section 2.2

- locator：Section 2.2 P2

- move_code：THEORY_INTRO

- paraphrase_cn：SDT将动机分为内在和外在，并认为外在干预可被内化以满足三个基本心理需要。

- rhetorical_function_cn：引入SDT核心命题。

- depends_on_cn：混合经验证据。

- sets_up_cn：为徽章内化解释奠定理论。

- evidence_pointer：Section 2.2第2段

### 35. Section 2.2 P3

- order：35

- section：Section 2.2

- locator：Section 2.2 P3

- move_code：THEORY_PROPOSITION

- paraphrase_cn：徽章提供胜任感反馈、允许自主选择并增强对环境的归属感，因此能同时推动内在外在动机。

- rhetorical_function_cn：将SDT具体应用到徽章。

- depends_on_cn：SDT概念。

- sets_up_cn：推导出徽章应被设计成私密、非货币。

- evidence_pointer：Section 2.2第3段

### 36. Section 2.2 P4

- order：36

- section：Section 2.2

- locator：Section 2.2 P4

- move_code：REQUIREMENT

- paraphrase_cn：本研究将数字徽章作为无社会互动、无货币激励的干净处理，以对齐自决动机。

- rhetorical_function_cn：从理论命题推导出实验设计要求。

- depends_on_cn：SDT内化机制。

- sets_up_cn：后面的Badge组设计细节。

- evidence_pointer：Section 2.2第4段

### 37. Section 2.3 P1

- order：37

- section：Section 2.3

- locator：Section 2.3 P1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：数字排行榜广泛研究于教育、管理和健康，但有效性和方向不一。

- rhetorical_function_cn：指出排行榜文献的矛盾。

- depends_on_cn：领导力文献。

- sets_up_cn：为SCT引入铺垫。

- evidence_pointer：Section 2.3第1段

### 38. Section 2.3 P2

- order：38

- section：Section 2.3

- locator：Section 2.3 P2

- move_code：THEORY_INTRO

- paraphrase_cn：社会比较理论认为人们通过与别人比较评估自我，排行榜同时触发上行和下行比较。

- rhetorical_function_cn：引入SCT解释排行榜效果。

- depends_on_cn：混合经验证据。

- sets_up_cn：说明排行榜可能产生相反方向的行为。

- evidence_pointer：Section 2.3第2段

### 39. Section 2.3 P3

- order：39

- section：Section 2.3

- locator：Section 2.3 P3

- move_code：THEORY_PROPOSITION

- paraphrase_cn：排行榜是双刃剑，可能激发竞争也可能抑制自主；差异可能源于个体异质性。

- rhetorical_function_cn：提出排行榜机制理论主张。

- depends_on_cn：SCT和Hydari et al. (2019)。

- sets_up_cn：为组内异质性分析做理论准备。

- evidence_pointer：Section 2.3第3段

### 40. Section 2.4 P1

- order：40

- section：Section 2.4

- locator：Section 2.4 P1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：将徽章、排行榜和优惠券作为研究框架的三个模块，在购物中心实验中提供因果证据。

- rhetorical_function_cn：将理论和实验设计连接到研究框架图。

- depends_on_cn：SDT和SCT。

- sets_up_cn：为实验部分给出总纲。

- evidence_pointer：Section 2.4第1段

### 41. Section 2.4 P2

- order：41

- section：Section 2.4

- locator：Section 2.4 P2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：基于SDT的长期研究认为感知能力和自主支持支持长期行为；因此徽章组预期有长期参与。社会比较也有长期效应，因此排行榜组也会持续参与。

- rhetorical_function_cn：给出处理期后的理论预测。

- depends_on_cn：SDT和SCT长期应用。

- sets_up_cn：为两期实验中的Post效应提供理论预期。

- evidence_pointer：Section 2.4第2段

### 42. Section 3 P1

- order：42

- section：Section 3

- locator：Section 3 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：采用随机现场实验并与亚洲大型购物中心合作；受试者完全不知道被观察，从而避免有意识偏差。

- rhetorical_function_cn：说明实验方法的选择理由。

- depends_on_cn：理论框架和RQ。

- sets_up_cn：引出场地和数据基础设施。

- evidence_pointer：Section 3第1段

### 43. Section 3 P1后

- order：43

- section：Section 3

- locator：Section 3 P1后

- move_code：CONTEXT

- paraphrase_cn：商场有超过300个品牌和多种餐饮，日均约15万访客，90%访客使用Wi-Fi和购物门户。

- rhetorical_function_cn：给出实验场所规模和信息技术条件。

- depends_on_cn：合作商场。

- sets_up_cn：说明数据追踪系统的可行性。

- evidence_pointer：Section 3第1段后

### 44. Section 3.1 P1-P2

- order：44

- section：Section 3.1

- locator：Section 3.1 P1-P2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：实验为期八周，前四周为处理期，后四周为后处理期；在第一天随机分配访客，随后发送消息和程序链接。

- rhetorical_function_cn：定义实验时间线。

- depends_on_cn：研究框架。

- sets_up_cn：强调在处理停止后继续观察。

- evidence_pointer：Section 3.1第1-2段

### 45. Section 3.1 P2后

- order：45

- section：Section 3.1

- locator：Section 3.1 P2后

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：处理停止时不提前通知，避免策略性反应；分配后自动注册，防止自选择。

- rhetorical_function_cn：说明两期设计中的识别策略。

- depends_on_cn：随机分配设计。

- sets_up_cn：使后处理期估计更干净。

- evidence_pointer：Section 3.1第2段

### 46. Section 3.1 P3

- order：46

- section：Section 3.1

- locator：Section 3.1 P3

- move_code：DESIGN_FEATURE

- paraphrase_cn：Badge组按每个店类获得独特徽章，收藏页仅本人可访问，以排除社会互动。

- rhetorical_function_cn：给出徽章处理的具体属性。

- depends_on_cn：SDT设计要求。

- sets_up_cn：使徽章处理与排行榜形成干净对比。

- evidence_pointer：Section 3.1第3段

### 47. Section 3.1 P4

- order：47

- section：Section 3.1

- locator：Section 3.1 P4

- move_code：DESIGN_FEATURE

- paraphrase_cn：Leaderboard组按距离和到店次数积分，排行榜每分钟刷新，消费者可与其他人竞争排名。

- rhetorical_function_cn：给出排行榜处理的具体属性。

- depends_on_cn：SCT设计要求。

- sets_up_cn：创造社会比较情境。

- evidence_pointer：Section 3.1第4段

### 48. Section 3.1 P5

- order：48

- section：Section 3.1

- locator：Section 3.1 P5

- move_code：DESIGN_FEATURE

- paraphrase_cn：Coupon组获得九类门店中随机抽取的一张20%折扣券，一次性使用，避免门店选择偏差。

- rhetorical_function_cn：给出货币激励处理的属性。

- depends_on_cn：促销实验设计需要。

- sets_up_cn：使Coupon组成为可比的货币激励基准。

- evidence_pointer：Section 3.1第5段

### 49. Section 3.2 P1

- order：49

- section：Section 3.2

- locator：Section 3.2 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用分配前两个月的行为和分配后问卷进行平衡检验，包括配对t检验和联合F检验。

- rhetorical_function_cn：建立随机化可信度。

- depends_on_cn：随机分配。

- sets_up_cn：使后续回归可作因果解释。

- evidence_pointer：Section 3.2第1段

### 50. Section 3.2 P2

- order：50

- section：Section 3.2

- locator：Section 3.2 P2

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：数据为个体-时期层面，包含Money、Distance、StoreVisits、人口统计和iOS信息。

- rhetorical_function_cn：介绍数据结构和变量。

- depends_on_cn：Wi-Fi追踪和销售匹配。

- sets_up_cn：为后续回归变量定义提供基础。

- evidence_pointer：Section 3.2第2段

### 51. Section 3.3 P1

- order：51

- section：Section 3.3

- locator：Section 3.3 P1

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：Tukey检验同时比较多组均值，比成对t检验更适合处理组间比较。

- rhetorical_function_cn：说明为什么用Tukey而不用t检验。

- depends_on_cn：四组设计。

- sets_up_cn：给出模型自由比较结果。

- evidence_pointer：Section 3.3第1段

### 52. Section 3.3 P2

- order：52

- section：Section 3.3

- locator：Section 3.3 P2

- move_code：RESULT

- paraphrase_cn：后处理期中游戏化组与控制组差异仍显著，优惠券与控制的差异不再显著。

- rhetorical_function_cn：展示持续效应的初步证据。

- depends_on_cn：Tukey检验。

- sets_up_cn：为回归分析提供动机。

- evidence_pointer：Section 3.3第2段

### 53. Section 4.1 P1

- order：53

- section：Section 4.1

- locator：Section 4.1 P1

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：用OLS估计线性回归，加入处理组、Post及处理×Post交互，以识别ATE和后处理期变化。

- rhetorical_function_cn：给出核心识别方程。

- depends_on_cn：模型自由证据。

- sets_up_cn：为定量效应和经济显著性提供模型。

- evidence_pointer：Equation (1)

### 54. Section 4.1 P2

- order：54

- section：Section 4.1

- locator：Section 4.1 P2

- move_code：RESULT

- paraphrase_cn：处理期徽章、排行榜、优惠券分别提高销售额21.5%、22.5%、31.7%；后处理期游戏化组仍分别带来约11.64和8.54美元额外销售，优惠券只贡献0.25美元。

- rhetorical_function_cn：量化ATE和经济意义。

- depends_on_cn：Table 6回归结果。

- sets_up_cn：支持游戏化持续价值的核心主张。

- evidence_pointer：Section 4.1第2段

### 55. Section 4.1 P3

- order：55

- section：Section 4.1

- locator：Section 4.1 P3

- move_code：RESULT

- paraphrase_cn：徽章和排行榜分别让距离增加25%和28.4%、到店增加37.9%和33.4%；优惠券距离增幅较小，后处理期游戏化仍保持额外距离和到店。

- rhetorical_function_cn：说明游戏化在非购买参与上优于优惠券。

- depends_on_cn：Table 6距离和到店列。

- sets_up_cn：后面探索机制解释为什么非购买参与持续。

- evidence_pointer：Section 4.1第3段

### 56. Section 4.2 P1

- order：56

- section：Section 4.2

- locator：Section 4.2 P1

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：基于IT采用中的性别、年龄和收入异质性文献，预期这些变量调节游戏化效果。

- rhetorical_function_cn：为HTE分析提供先验预期。

- depends_on_cn：人口统计与IT采用文献。

- sets_up_cn：引入性别、年龄、收入交互模型。

- evidence_pointer：Section 4.2第1段

### 57. Section 4.2 P后

- order：57

- section：Section 4.2

- locator：Section 4.2 P后

- move_code：RESULT

- paraphrase_cn：女性在优惠券上反应更强，男性在徽章和排行榜上反应更强；游戏化重新塑造男性长期行为。

- rhetorical_function_cn：报告性别HTE。

- depends_on_cn：Table 7。

- sets_up_cn：细分目标用户。

- evidence_pointer：Section 4.2, Table 7

### 58. Section 4.2 P后

- order：58

- section：Section 4.2

- locator：Section 4.2 P后

- move_code：RESULT

- paraphrase_cn：年龄越大游戏化效应越弱，优惠券则近似对所有年龄都有效；收入对徽章和排行榜的调节方向相反。

- rhetorical_function_cn：报告年龄和收入HTE。

- depends_on_cn：Tables 8-9。

- sets_up_cn：说明游戏化并非一刀切工具。

- evidence_pointer：Section 4.2, Tables 8-9

### 59. Section 4.3 P1-P2

- order：59

- section：Section 4.3

- locator：Section 4.3 P1-P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用Levene检验比较组间方差，用层次贝叶斯随机系数模型捕捉个体层面异质性。

- rhetorical_function_cn：解释为什么要分析组内异质性。

- depends_on_cn：HTE结果不能覆盖组内差异。

- sets_up_cn：用随机斜率刻画个体异质性。

- evidence_pointer：Section 4.3第1段

### 60. Section 4.3 P后

- order：60

- section：Section 4.3

- locator：Section 4.3 P后

- move_code：RESULT

- paraphrase_cn：排行榜组方差最大，优惠券组方差最小；排行榜可能激发自我强化或自我放逐，徽章更均衡。

- rhetorical_function_cn：报告组内异质性的核心结果并给出理论解释。

- depends_on_cn：Tables 10-11。

- sets_up_cn：将方差结果提升为处理性质差异。

- evidence_pointer：Section 4.3, Tables 10-11

### 61. Section 5.1 P1

- order：61

- section：Section 5.1

- locator：Section 5.1 P1

- move_code：MECHANISM

- paraphrase_cn：将新店结果比例作为因变量重新估计，以检验处理是否促使探索新店。

- rhetorical_function_cn：把理论机制操作化为探索比例。

- depends_on_cn：ATE结果。

- sets_up_cn：为‘游戏化-探索-长期参与’故事提供证据。

- evidence_pointer：Section 5.1, Equation (5)

### 62. Section 5.1 P2

- order：62

- section：Section 5.1

- locator：Section 5.1 P2

- move_code：RESULT

- paraphrase_cn：处理期新店支出比例显著更高，后处理期探索效应减弱；作者将其解释为临时行动召唤与内在长期动机的结合。

- rhetorical_function_cn：报告机制结果并连接长期效应。

- depends_on_cn：Table 12。

- sets_up_cn：说明为什么游戏化能改变行为而不只是促销。

- evidence_pointer：Section 5.1, Table 12

### 63. Section 5.2 P1

- order：63

- section：Section 5.2

- locator：Section 5.2 P1

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：通过Wi-Fi检测排除伴随购物情况，重新估计子样本，以排除同伴效应的解释。

- rhetorical_function_cn：处理同伴干扰的可能。

- depends_on_cn：Wi-Fi追踪数据。

- sets_up_cn：为结果稳健性提供证据。

- evidence_pointer：Section 5.2第1段

### 64. Section 5.2 P2

- order：64

- section：Section 5.2

- locator：Section 5.2 P2

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：排除22岁以下的可能学生群体后，游戏化效应仍然稳定，排除季节性的替代解释。

- rhetorical_function_cn：处理季节性驱动的怀疑。

- depends_on_cn：年龄门槛子样本。

- sets_up_cn：支持外部有效性。

- evidence_pointer：Section 5.2第2段

### 65. Section 6 P1-P3

- order：65

- section：Section 6

- locator：Section 6 P1-P3

- move_code：CONTRIBUTION

- paraphrase_cn：总结游戏化对销售、距离、到店的影响，优惠券消退，异质性显著，探索机制存在。

- rhetorical_function_cn：重新陈述核心发现。

- depends_on_cn：全部实证结果。

- sets_up_cn：为理论和管理贡献做总结。

- evidence_pointer：Section 6前3段

### 66. Section 6 P4

- order：66

- section：Section 6

- locator：Section 6 P4

- move_code：CONTRIBUTION

- paraphrase_cn：贡献被概括为五个方面：新线下情境、随机现场实验、长期时间范围、全面HTE、位置型游戏化技术。

- rhetorical_function_cn：给被审稿人容易引用的贡献列表。

- depends_on_cn：所有结果。

- sets_up_cn：支撑后面的研究定位。

- evidence_pointer：Section 6贡献段

### 67. Section 6 P5-P6

- order：67

- section：Section 6

- locator：Section 6 P5-P6

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：对商场管理者：优惠券短期促进销售但游戏化能重塑长期行为；徽章适合大众，排行榜适合高竞争人群。对设计者：应把激励设计与目标结果对齐并使用位置技术动态配置。

- rhetorical_function_cn：将研究发现转化为行动建议。

- depends_on_cn：实证结果和理论解释。

- sets_up_cn：体现研究的实践相关性。

- evidence_pointer：Section 6管理启示段

### 68. Section 6最后段

- order：68

- section：Section 6

- locator：Section 6最后段

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：限制包括游戏设计不能完全等动作、未研究其他游戏元素、优惠券是门店特定而非全场、未检验两种激励的互补替代。

- rhetorical_function_cn：限定贡献范围并给出未来方向。

- depends_on_cn：本研究设计和局限。

- sets_up_cn：保护结论不过度扩大。

- evidence_pointer：Section 6最后一段

## 写作技术

- gap_construction_cn：不是简单说‘没人做过’，而是将机制不清、营销知识不足、缺少与非货币/货币激励对照、缺少时间分析、缺少异质性这五类问题并置，并用四个RQ把这些缺口转成可检验问题，使每个后来的贡献都能直接对应一个缺口。

- signposting_cn：摘要末尾预告结果类型；引言用四个RQ作路标；每一节开头用‘We first... Then...’式预告；过渡句如‘To quantify the effects, we are motivated to...’连接原始证据和回归分析。

- transition_logic_cn：每阶段结果都保留‘uncertainty’：平衡检验证明可比后进入均值比较；Tukey显示差异后进入回归；ATE表明平均效应后问是否异质；人口统计HTE后问是否还存在组内异质；机制检验后问是否被情境因素驱动，从而逐层推进。

- claim_evidence_rhythm_cn：先给模型自由证据，再给回归证据，再给经济显著性；每个数值都通过指数化系数算出百分比和美元/英里/店数，使结果可理解；在重要主张后立即给出表格证据。

- benchmark_narrative_cn：优惠券不是附加品而是基准：作者让读者从‘游戏化是否有效’升级为‘游戏化相对于货币激励有什么用’，再用距离、到店、后处理期三个维度证明游戏化在非销售和长期行为上的独特价值。

- theory_return_cn：后处理期之前用SDT/SCT文献做长期预测；结果出来后，在组内异质性一节用‘双刃剑’回扣SCT；在探索机制一节用SDT的‘内化’解释长期行为；这样理论不只是引言包装，而是贯穿解释。

- contribution_positioning_cn：贡献段在引言和结论各出现一次，引言预告、结论细述；每个贡献都绑定一个文献缺口或方法呼吁（如Hamari et al. 2014的因果呼吁，Tobon et al. 2020的时间呼吁）。

- novelty_protection_cn：通过多维比较防止退化为一次性性能结果：与优惠券对照、两期设计、组内异质性、机制检验、子样本稳健性，使游戏化被刻画为具有不同性质（短期vs长期、大众vs分化）的促销策略，而不仅是‘又一种有效工具’。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：用市场规模和真实企业例子建立实践重要性，然后压缩到两个具体游戏元素。

- research_job_cn：找到与所选情境相关的游戏化要素，并确认这些要素在实践中被广泛部署。

- required_evidence_cn：能引用的行业数据和至少两到三个企业案例。

- transition_to_next_cn：用‘文献有积极证据但机制不明’过渡到缺口。

#### 2. 2

- step：2

- writing_job_cn：把文献缺口拆成机制、对照、时间、异质性等具体维度，并生成RQ。

- research_job_cn：系统阅读目标领域最新综述，定位未被回答的问题。

- required_evidence_cn：每类缺口至少有一篇近年的综述或评论作为依据。

- transition_to_next_cn：用‘这些缺口共同需要严格研究’引出RQ。

#### 3. 3

- step：3

- writing_job_cn：选择和RQ匹配的理论，并说明理论命题如何指导每个处理的属性。

- research_job_cn：从理论中推导每个设计变量应当有何种属性（如私密、公开、货币价值）。

- required_evidence_cn：理论文献明确提到哪些刺激满足哪种心理需要或比较机制。

- transition_to_next_cn：用研究框架图把三个刺激与机制放到同一张图中。

#### 4. 4

- step：4

- writing_job_cn：详细描述实验场地、随机分配、处理内容、时间线，使研究可复制。

- research_job_cn：在实际组织中实现随机分配并确保处理只能按计划送达。

- required_evidence_cn：随机化流程、处理停止规则、防自选择机制和样本量。

- transition_to_next_cn：用平衡检验证明随机化成功。

#### 5. 5

- step：5

- writing_job_cn：先展示无模型证据，再报告ATE回归和经济显著性。

- research_job_cn：用多重比较和回归同时估计平均效应及处理-时间交互。

- required_evidence_cn：组间均值差异、聚类回归系数和可解释的百分比换算。

- transition_to_next_cn：从‘平均效应是否不同’过渡到‘对谁更有效’。

#### 6. 6

- step：6

- writing_job_cn：报告人口统计HTE和组内异质性，把异质性从偶然现象变成理论特征。

- research_job_cn：用两/三向交互和方差或层次模型刻画异质性。

- required_evidence_cn：交互项显著性和方差比较的统计检验。

- transition_to_next_cn：用‘为什么会有这些效应’进入机制分析。

#### 7. 7

- step：7

- writing_job_cn：用可观察中介变量近似机制，并用子样本排除替代解释。

- research_job_cn：构造机制变量（如探索比例）并检验其随时间变化；用子样本检验边界。

- required_evidence_cn：机制变量对处理的响应及稳健性不变量。

- transition_to_next_cn：汇总主要发现并升华为理论和实践贡献。

#### 8. 8

- step：8

- writing_job_cn：结论逐条回应引言缺口，同时明确限制和未来方向。

- research_job_cn：将经验规律映射为设计知识、管理策略和理论边界。

- required_evidence_cn：每个贡献至少对应一个已报告的结果。

- transition_to_next_cn：用‘尽管有限制，本研究是第一批...’收尾。

### most_transferable_moves_cn

1. 把文献缺口拆成多个正交维度，使每个贡献都能对号入座

2. 让理论直接决定处理设计属性，而不是只在讨论中事后解释

3. 在实验设计中包含‘停止处理后的观察期’来回答持续性

4. 用货币激励作为基准，避免只说‘游戏化有效’

5. 用多个结果变量（销售、距离、到店）揭示不同刺激的优势维度

6. 用组内方差/随机系数刻画处理属性的本质差异

7. 先用无模型证据再回归，使结果透明且可逐步叠加

### resource_intensive_or_nonstandard_parts_cn

1. 与大型商场合作并获得免费Wi-Fi和服务入口的数据权限

2. 精确匹配销售记录与设备标识，需要收银系统配合

3. 对数千访客进行随机分配和消息推送，需要商场的会员/微信/门禁体系

4. 两月预分配数据用于平衡检验，需要持续追踪

5. 同伴检测需要Wi-Fi设备间邻近识别和问卷验证

### what_not_to_copy_superficially_cn

1. 如果只写‘我们开展随机现场实验’而没有随机化流程、平衡检验和防自选择措施，因果声明会失败

2. 如果只用理论命名处理而没有让理论决定具体设计属性，三组比较只是标签替换

3. 如果只报告AT而不给后处理期、HTE、机制和子样本，结论容易退化为一次性促销比较

4. 如果把组内方差解释为心理机制而没有任何心理测量或中介证据，会被审稿人视为过度解释

- single_best_description_of_the_routine_cn：用理论把两个游戏化元素和一个货币激励转成可对照的数字处理，在真实场景中随机分配，先用无模型证据后回归，再通过持续期、异质性、机制和子样本把‘有没有效’升级为‘何时、对谁、为什么有效以及如何设计’。

## 分析边界

分析基于文章完整文本而非重新获取原始数据；部分表格值和图细节可能因OCR产生细微误差，但不影响主要结构判断。文章本身未提供直接心理量表测量SDT/SCT机制，因此对机制部分的解读需与作者一样保持间接性。
