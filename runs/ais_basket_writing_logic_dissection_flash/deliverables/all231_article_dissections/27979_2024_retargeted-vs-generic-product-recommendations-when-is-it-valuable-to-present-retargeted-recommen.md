# Retargeted vs. Generic Product Recommendations: When is it Valuable to Present Retargeted Recommendations?

- 作者：Xiang (Shawn) Wan; Anuj Kumar; Xitong Li
- 年份 / 期刊：2024 / Information Systems Research
- DOI：10.1287/isre.2020.0560
- 源文件：27979_2024_retargeted-vs-generic-product-recommendations-when-is-it-valuable-to-present-retargeted-recommen.md
- 论文主类型：field_intervention_or_platform_experiment
- 主导写作弧线：phenomenon_mechanism_intervention_field_test
- 置信度：0.82

## 文章级论证概况

- 核心问题：在消费者购买漏斗的不同阶段，展示基于协同过滤的推荐商品时，重定向推荐（用户此前浏览过的推荐商品）与通用推荐（用户此前未浏览过的推荐商品）对商品曝光量和转化率及最终销售的相对价值是什么？

- 制品与设计：研究制品是两种推荐展示方式：在焦点商品页显示4个推荐商品（处理组）与隐藏推荐商品（对照组）；同时将推荐商品曝光按用户过去是否浏览过分为重定向推荐与通用推荐，并按用户在品类中是否加购过将访问阶段划分为早期与晚期购买漏斗。实验环境包括一家美国中型服装家居零售商的真实网站现场随机实验，以及一个基于Amazon MTurk的两阶段在线实验网站。

- 客观结果：现场实验中，两种推荐都显著增加推荐商品的曝光量；只有早期购买漏斗中的通用推荐显著提高推荐商品转化率，重定向推荐未显著影响转化率；早期阶段通用推荐和重定向推荐都提高推荐商品销售，但通用推荐更有效；晚期阶段只有重定向推荐显著提高推荐商品销售。总商品（焦点商品+推荐商品）销售同样呈现早期通用推荐更优、晚期重定向推荐更优的模式。在线实验表明晚期购买漏斗中重定向推荐的优势主要由重定向本身驱动，而非推荐算法亲和度。反事实模拟显示，按购买漏斗阶段替换推荐商品可使总销售提高最多3.19%。

- 核心贡献：作者将重定向广告文献中的重定向概念引入产品推荐研究，首次区分重定向推荐与通用推荐，并沿着购买漏斗分解其作用机制：两种推荐主要增加推荐商品曝光量，而非转化率；通用推荐仅在早期漏斗显著提高转化率，重定向推荐在晚期漏斗更有效。研究为在线零售商和基于商品项的协同过滤推荐系统设计提供了按漏斗阶段选择推荐类型的可操作建议。

- 整篇论证链：作者首先指出现有推荐系统文献主要考察推荐的平均效果，却没有回答推荐是否被用户此前浏览过以及用户在购买漏斗中所处阶段会如何改变推荐效果；同时重定向广告文献虽研究了重定向，但发生在第三方网站并只影响广告转化率，不能直接推广到站内商品推荐。为填补这一缺口，作者在一家真实零售网站开展随机现场实验，将推荐商品是否显示、推荐商品是否曾被浏览、以及用户处于购买漏斗早期还是晚期进行交叉比较，并把推荐商品销售分解为曝光量和转化率两个路径。研究发现两类推荐均提高曝光，但只有早期通用推荐提高转化率，晚期重定向推荐提高销售。由于现场实验中的重定向推荐同时混有协同过滤算法选择和重定向因素，作者又通过MTurk两阶段在线实验，用独立算法分别生成纯重定向推荐和通用推荐，证明晚期效果来自重定向本身。随后作者用现场数据检验焦点商品与推荐商品的总销售，排除渠道替代威胁，并通过反事实模拟显示将部分较低排名推荐替换为符合漏斗阶段类型可带来最多约3%的销售增长。全文从现象缺口出发，经机制分解、两层实验验证、稳健性检验，最终回到对推荐系统设计和重定向推荐理论的贡献。

## 类型与写作弧线判定

- 论文主类型判定：文章的核心证据来自在真实零售网站进行的随机现场实验，通过操纵焦点商品页是否显示推荐商品来比较重定向推荐与通用推荐的效果；同时辅以在线实验和反事实模拟。虽然包含在线实验和模拟，但主要论证弧线是真实平台的数字展示干预与现场因果检验，因此属于现场/平台实验类型。

- 主导写作弧线判定：文章先提出重定向推荐与通用推荐在不同购买漏斗阶段产生不同影响的现象，并用重复曝光、信号相关性和偏好收窄等机制解释；随后进行现场随机干预，并用在线实验检验机制，再以模拟量化收益。该弧线典型地符合“现象—机制—数字干预—现场因果检验”的结构。

## 研究开展程序

- study_or_phase_count：5

- 研究阶段总序列：研究先利用现场实验数据，将推荐商品销售分解为“转化率”和“曝光量”两个路径，分别检验重定向推荐与通用推荐在购买漏斗早期/晚期的不同效应；其次在同一现场数据上进行每日曝光量和销售的估计并做大量稳健性检验；接着用MTurk在线实验分离现场实验中重定向与算法推荐因素的混淆，证明重定向机制；再用现场数据估计焦点商品与推荐商品总销售，处理渠道替代问题；最后用反事实模拟估算按漏斗阶段替换推荐类型可实现的销售增益。五个阶段依次回答“效应是什么”“机制是什么”“总效应是否成立”“经济价值有多大”。

### studies_or_phases

#### 1. 现场实验：推荐商品转化率路径分解

- order：1

- name_cn：现场实验：推荐商品转化率路径分解

- question_cn：展示推荐商品（相对于隐藏）对推荐商品点击率、条件转化率和总体转化率的影响，是否取决于推荐是重定向还是通用，以及用户处于购买漏斗早期还是晚期？

- inputs_and_setting_cn：美国中型服装家居零售商网站；2015年4月起的9周随机实验；多会话访客47,697人，70,881个会话，212,657次焦点商品页浏览，846,804次推荐商品曝光；处理组半数随机显示4个推荐商品，另外半数隐藏。

- designed_or_compared_object_cn：焦点商品页是否显示推荐商品（Rec=0/1）、推荐曝光是否曾被用户浏览过（ReTar=0/1）、购买漏斗早期/晚期。

- baseline_control_or_counterfactual_cn：控制组隐藏推荐商品；以未显示的推荐商品曝光和未推荐状态为反事实基底；早期/晚期分样本；通用推荐作为重定向推荐的对照。

##### objective_metrics

1. RPView | Impression 点击率

2. RPPur | RPView 条件转化率

3. RPPur | Impression 总体转化率

4. Logit模型中的β1、β2、β3系数

- analysis_method_cn：分别对早期和晚期购买漏斗样本估计带推荐商品固定效应的Logit模型，控制推荐位次、亲和度对数、累计浏览数等变量；并用模型自由证据的均值差t检验作初步验证。

- main_result_cn：显示推荐商品在几乎所有条件下都提高点击率；显示降低了条件转化率（晚期重定向推荐除外）；只有早期购买漏斗中的通用推荐显著提高总体转化率，重定向推荐在早期和晚期总体转化率均无显著正效应。

- argumentative_role_cn：确立核心因果事实：推荐商品销售增加主要来自曝光量而非转化率；通用推荐只在早期对转化率有作用，重定向推荐对转化率无作用。为后续曝光量分析提供转化率组件。

- remaining_uncertainty_cn：现场实验中重定向推荐同时由过去浏览和协同过滤算法决定，无法判断是重定向还是算法亲和度驱动；且重定向推荐并非外生生成，可能存在内生性。

- link_to_next_phase_cn：需要将转化率与曝光量两个组件结合，估计每日推荐商品曝光量和销售，从而判断总销售效应来自哪个组件。

##### evidence_pointers

1. Section 5.1.1

2. Table 2

3. Table 4

4. Specification (1)

#### 2. 现场实验：每日推荐商品曝光量与销售分析及稳健性检验

- order：2

- name_cn：现场实验：每日推荐商品曝光量与销售分析及稳健性检验

- question_cn：重定向推荐和通用推荐对每日推荐商品曝光量和每日推荐商品销售的影响是什么？结果是否稳健？

- inputs_and_setting_cn：与前一阶段相同；将数据整理为RP-日-条件面板，共299,788个RP-日观测；每个推荐商品在63天实验中平均出现约13天。

- designed_or_compared_object_cn：每日推荐商品曝光次数和每日推荐商品销售数，按Rec、ReTar、购买漏斗阶段四个组合比较。

- baseline_control_or_counterfactual_cn：控制组（未显示推荐商品）的曝光量和销售作为基线；同一天某推荐商品在其他条件下曝光为0，以构造可比较条件面板。

##### objective_metrics

1. 每日RP曝光量

2. 每日RP销售

3. 曝光效应和销售效应点估计

4. 相对于控制组均值的销售变化百分比

- analysis_method_cn：OLS固定效应模型（Specification 2），以推荐商品固定效应控制产品层面混淆；并做系列稳健性检验：访问者与FP-RP-日固定效应、加入控制变量、纳入单次会话访客、新顾客子样本、仅出现在两个阶段访客、排除加购或与加购品高度相似的商品、两个安慰剂检验。

- main_result_cn：两种推荐在早晚期均显著增加每日推荐商品曝光量；早期两种推荐都提高推荐商品销售但通用更优；晚期只有重定向推荐显著提高销售。稳健性检验结果定性一致，且排除“重定向商品因已被加购或相似”的替代解释。

- argumentative_role_cn：说明推荐商品销售增加主要来自曝光量增加；早期通用推荐的销售优势来自曝光量加转化率双重作用，晚期重定向推荐的价值来自曝光量提升。

- remaining_uncertainty_cn：即使经过稳健性检验，现场实验中的重定向推荐仍非外生生成，且与算法推荐混合；需要在线实验分离机制。

- link_to_next_phase_cn：在线实验通过独立生成纯重定向推荐与通用推荐，检验重定向本身是否驱动晚期购买漏斗中的销售。

##### evidence_pointers

1. Section 5.1.2

2. Table 5

3. Table 6

4. Section 5.1.2.5

5. Online Appendices D-G

#### 3. Amazon MTurk两阶段在线实验：分离重定向效应

- order：3

- name_cn：Amazon MTurk两阶段在线实验：分离重定向效应

- question_cn：在晚期购买漏斗中，重定向推荐的优势究竟是来自“用户之前看过该商品”的重定向效应，还是来自协同过滤推荐算法的高相似度/高亲和度？

- inputs_and_setting_cn：在自建实验网站上销售女装上衣，平均价格约38美元；招募1,200名美国女性MTurk参与者，768名有效；两阶段实验，第一阶段浏览/加购，间隔3-7天后第二阶段展示推荐；另请1,000名女性MTurk工人评价产品以生成相似度数据。

- designed_or_compared_object_cn：重定向推荐是从参与者在第一阶段浏览过的产品中随机抽取；通用推荐是由Slope-One商品协同过滤算法选择的高相似度产品；随机显示或隐藏推荐。

- baseline_control_or_counterfactual_cn：30%随机分配的对照组隐藏推荐商品；重定向推荐与通用推荐相互作为对照；利用随机选择的重定向产品自身相似度高低进行额外比较。

##### objective_metrics

1. RP购买概率（转化率）

2. RP曝光量

3. RP销售

4. 重定向推荐相对通用推荐在早晚期漏斗中的销售差异

- analysis_method_cn：使用与现场实验相同的Logit Specification (1)和固定效应Specification (2)；两个先导研究优化设计；注意力检验题筛选样本；依据加购与否划分购买漏斗阶段。

- main_result_cn：只有早期购买漏斗中的通用推荐显著提高转化率；晚期重定向推荐显著提高RP销售，而通用推荐无显著效果；无论重定向推荐与焦点商品相似度高低，结果相似，说明驱动因素是重定向本身。

- argumentative_role_cn：补足现场实验的机制缺口：证明晚期重定向推荐的销售提升来自“重定向”而非协同过滤算法相似度；同时回应内生性担忧，验证现场结果稳健。

- remaining_uncertainty_cn：在线实验是人工环境，购买规模小，且仍依赖参与者自我选择的购买漏斗阶段，没有完全外生操纵漏斗阶段。

- link_to_next_phase_cn：机制确认后，回到管理者关心的总销售：使用现场数据估计焦点商品与推荐商品总销售，检验是否存在渠道替代。

##### evidence_pointers

1. Section 5.2

2. Table 7

3. Section 5.2.5

4. Online Appendix I

#### 4. 现场数据：焦点商品+推荐商品总销售分析

- order：4

- name_cn：现场数据：焦点商品+推荐商品总销售分析

- question_cn：将焦点商品与推荐商品视为同一子品类内的替代品时，展示重定向推荐或通用推荐对总销售（FP+RP）的影响是否仍遵循“早期通用推荐更优、晚期重定向推荐更优”的模式？

- inputs_and_setting_cn：复用现场实验数据；以焦点商品页为分析单元；页面是否存在至少一个重定向推荐作为Ind_ReTar指标。

- designed_or_compared_object_cn：焦点商品页是否显示推荐、页面是否存在至少一个重定向推荐、购买漏斗早期/晚期；比较总转化率、焦点商品页曝光量和FP+RP总销售。

- baseline_control_or_counterfactual_cn：隐藏推荐的对照组为基线；通用推荐状态作为重定向推荐的对照。

##### objective_metrics

1. FP+RP购买转化率

2. 每日FP页曝光量

3. 每日FP+RP总销售

4. 重定向推荐与通用推荐的销售差异

- analysis_method_cn：估计Specification (3)和(4)，分别处理页面级转化率和每日曝光/销售，并包含RP/FP固定效应及控制变量；按早期与晚期购买漏斗分样本。

- main_result_cn：结果与RP销售分析一致：早期购买漏斗中通用推荐显著提高FP+RP总销售，晚期购买漏斗中重定向推荐显著提高总销售；晚期通用推荐甚至略降低总销售。

- argumentative_role_cn：将推荐产品销售结论推广到总销售，排除“推荐只是把焦点商品销售转化为推荐商品销售”的渠道替代解释，增加管理相关性。

- remaining_uncertainty_cn：总销售分析仍基于现场观测和内生漏斗阶段；效应虽显著但未量化“按最优策略改动推荐系统”的收益。

- link_to_next_phase_cn：通过反事实模拟将各阶段效应转化为具体的推荐替换策略及其销售增益。

##### evidence_pointers

1. Section 5.3

2. Table 8

3. Specification (3) and (4)

#### 5. 反事实模拟：推荐替换策略的销售增益

- order：5

- name_cn：反事实模拟：推荐替换策略的销售增益

- question_cn：如果零售商根据购买漏斗阶段将部分推荐替换为符合阶段类型的重定向/通用推荐，总销售增益是多少？

- inputs_and_setting_cn：现场实验数据；零售商推荐系统的每个焦点商品顶部15候选推荐（实际只展示前4）；Logit模型预测的推荐购买概率和焦点商品购买概率；商品价格。

- designed_or_compared_object_cn：四种替换策略：仅替换第4位推荐、第3-4位、第2-4位、全部第1-4位；将晚期/早期的原推荐替换为第5-15位中合适类型的推荐。

- baseline_control_or_counterfactual_cn：不替换的原始销售160,072美元作为基线；预测的反事实购买概率乘以价格得到替换后销售。

##### objective_metrics

1. FP销售变化

2. RP销售变化

3. 总销售变化（美元）

4. 总销售变化百分比

- analysis_method_cn：用k折交叉验证比较Logit、固定效应Logit、线性概率和固定效应线性概率模型，选择Logit模型预测反事实购买概率；对四种替换策略分别模拟。

- main_result_cn：替换第3-4位候选推荐可获得最大总销售增益3.19%；替换全部前4位只获得0.81%增益，因为低亲和度损失抵消了类型调整收益。

- argumentative_role_cn：把统计效应转化为可操作的经济收益，展示对现有基于商品项的协同过滤推荐系统的增量价值。

- remaining_uncertainty_cn：模拟依赖模型预测，不是真实实施新策略的随机实验，可能高估或低估实际转化；没有考虑用户对推荐变化的动态反应。

- link_to_next_phase_cn：讨论部分据此提出管理建议和设计原则，同时限定结论适用于商品项协同过滤推荐系统及服装家居品类。

##### evidence_pointers

1. Section 6

2. Table 9

3. Online Appendix J

## 各部分修辞架构

### abstract_moves

1. GAP: 现有文献理解推荐对销售的平均效应，但不清楚重定向推荐与通用推荐的差异效应

2. RQ_OR_OBJECTIVE: 以现场实验比较两者在购买漏斗不同阶段的效果

3. METHOD_JUSTIFICATION: 将销售分解为推荐商品曝光量与转化率分别估计

4. RESULT: 通用推荐仅早期提高转化率；重定向推荐不提高转化率；两者均提高曝光量

5. RESULT: MTurk实验证明晚期重定向推荐的效果来自重定向本身

6. RESULT: 反事实模拟显示最多可提高约3%销售

7. CONTRIBUTION: 对在线零售商和算法推荐系统设计有启示

### introduction_moves

1. CONTEXT: 多数电商网站在焦点商品页基于共同浏览/购买展示相关商品推荐

2. PHENOMENON: 推荐中的商品有些是用户以前看过的，称为重定向推荐

3. PRACTICAL_STAKES: 判断哪类推荐更合适并展示可增加销售

4. MECHANISM: 早期漏斗用户偏好开放，通用推荐帮助发现；晚期偏好收窄，重定向推荐提醒

5. LIMITATION: 现有产品推荐研究对两类推荐在漏斗阶段的相对有效性缺乏指导

6. LIMITATION: 展示广告文献的重定向结论因发生在第三方网站且只影响广告转化率，不能直接应用

7. GAP: 没有研究考察推荐对推荐商品曝光次数和转化率的影响

8. RQ_OR_OBJECTIVE: 提出三个研究问题：何时展示哪类推荐、是否受购买漏斗阶段调节、销售增益多大

9. STUDY_OVERVIEW: 介绍现场实验设计和重定向/通用操作定义

10. RESULT: 报告核心发现——早期通用推荐提高转化率，晚期重定向推荐提高销售

11. STUDY_OVERVIEW: 介绍MTurk在线实验以梳理机制

12. RESULT: 总商品销售与推荐商品销售结果一致

13. CONTRIBUTION: 对推荐系统文献的三点贡献

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE: 综述推荐系统分类和CF系统的主导地位

2. PRIOR_KNOWLEDGE: 综述推荐系统经济价值文献的具体效应量

3. PRIOR_KNOWLEDGE: 综述共购/共现关系网络对销售的影响

4. GAP: 现有研究忽略访问者情境因素（是否看过推荐商品、漏斗阶段）

5. PRIOR_KNOWLEDGE: 推荐生成的产品网络可能同时提高曝光和条件购买概率

6. GAP: 鲜有研究同时考察曝光量与条件购买概率两个机制

7. PRIOR_KNOWLEDGE: 展示广告文献显示重定向广告对广告转化率产生影响

8. WHY_GAP_MATTERS: 产品推荐与第三方重定向广告不同，站内展示会影响曝光量和转化率

9. PRIOR_KNOWLEDGE: AIDA与三阶段购买漏斗模型

10. PRIOR_KNOWLEDGE: 隐马尔可夫模型刻画潜在漏斗阶段

11. PRIOR_KNOWLEDGE: 用可观察行为代理漏斗阶段的研究

12. METHOD_JUSTIFICATION: 采用加购后为晚期、加购前为早期的可观察代理定义

### artifact_design_moves

1. DESIGN_FEATURE: 现场推荐系统用IBM Coremetrics亲和度四类分加权公式

2. DESIGN_FEATURE: 仅推荐同子品类产品，保持推荐品为替代品并取前4

3. PHENOMENON: 定义推荐曝光；点击RP可使其成为新的焦点商品

4. BENCHMARK_OR_CONTRAST: 即使不显示，访客也能通过搜索或相邻展示发现RP，因此控制组可作有效反事实

5. MECHANISM: 显式展示推荐商品产生两个额外作用——被发现和帮助学习相似性

6. MECHANISM: 重定向推荐通过重复曝光、相关性信号、回忆和品类熟悉度产生效果

7. HYPOTHESIS_OR_PROPOSITION: 预期两类推荐效果随购买漏斗阶段而异，并用表1设计估计相对效果

8. DESIGN_FEATURE: 现场实验随机分配访客至展示/隐藏版本，并保持一致版本

9. METHOD_JUSTIFICATION: 用品类内加购后划分晚期购买漏斗

10. LIMITATION: 现场重定向推荐与算法推荐混淆且非外生，需要通过在线实验解决

11. DESIGN_FEATURE: 在线实验使用两个独立算法分别生成重定向和通用推荐

12. DESIGN_FEATURE: 使用Slope-One商品协同过滤算法并收集评价数据

13. DESIGN_FEATURE: 对MTurk参与者实施激励一致性机制，保证真实购买动机

### evaluation_moves

1. METHOD_JUSTIFICATION: 将每次FP页浏览组织为四条RP曝光，形成面板

2. RESULT: 模型自由证据显示显式展示提高点击率但降低条件转化率

3. METHOD_JUSTIFICATION: 用高维固定效应Logit识别交互项

4. METHOD_JUSTIFICATION: 讨论产品层面与访客层面未观测因素，说明RP固定效应与随机分配使交互系数可识别

5. RESULT: 转化率回归结果与模型自由证据一致

6. METHOD_JUSTIFICATION: RP-日面板中未出现条件记为0，以构造可比较条件

7. RESULT: 每日曝光量和销售估计显示曝光量驱动销售

8. ROBUSTNESS_OR_BOUNDARY_TEST: 多种固定效应、子样本、排除加购相似品、安慰剂检验

9. METHOD_JUSTIFICATION: 在线实验用同样的Logit和面板规范，便于与现场结果对照

10. RESULT: 在线实验结果重复了现场的核心模式

11. METHOD_JUSTIFICATION: 用k折交叉验证选择Logit用于反事实预测

12. RESULT: 模拟显示替换第3-4位推荐获得最大销售增益

### discussion_and_contribution_moves

1. CONTRIBUTION: 从重定向广告文献引入“重定向推荐”概念，并指出站内推荐会同时影响曝光量和转化率

2. CONTRIBUTION: 发现通用推荐在早期漏斗更有效，重定向推荐在晚期更有效

3. CONTRIBUTION: 指出销售增长主要来自曝光量增加，而非转化率

4. BOUNDARY_CONDITION: 结论适用于基于商品项的协同过滤推荐系统和服装家居等电商类别

5. LIMITATION_AND_FUTURE: 现场推荐非外生，建议未来设计完全随机实验

6. LIMITATION_AND_FUTURE: 用可观察行为代理漏斗阶段，未来可用潜在状态模型

7. LIMITATION_AND_FUTURE: 未来可研究不限定漏斗阶段的条件以及更多算法类别

## 理论/知识到设计的翻译

### 知识/理论基础

1. 重定向广告文献（Lambrecht and Tucker 2013; Bleier and Eisenbeiss 2015; Sahni et al. 2019）

2. 购买漏斗/AIDA模型与可观察行为代理文献（Bleier and Eisenbeiss 2015; Sahni et al. 2019）

3. 基于商品项的协同过滤推荐系统文献（Linden et al. 2003; Lee and Hosanagar 2021; Li et al. 2022）

4. 推荐系统经济价值与产品网络文献（Oestreicher-Singer and Sundararajan 2012; Kumar and Hosanagar 2019）

- 理论—设计耦合：partial

- 耦合判定理由：购买漏斗理论和重定向广告文献决定了核心变量（重定向/通用）、购买阶段操作定义（加购后为晚期）、以及结果分解（曝光量与转化率），从而塑造了实验设计；但推荐商品本身的生成算法是零售商现成的IBM Coremetrics算法和后来用于在线实验的标准Slope-One算法，并非从理论派生出来的新制品。因此理论对设计的影响是部分而非直接。

- 理论到设计翻译链：重定向广告的“重定向效应”与购买漏斗的“早期探索—晚期收窄”机制 → 推断重定向推荐与通用推荐在漏斗不同阶段应有不同价值 → 将销售分解为“推荐商品曝光量”和“条件于曝光的购买概率”两条路径 → 设计现场随机实验：随机展示/隐藏推荐，依据过去浏览区分重定向/通用，依据加购划分早/晚期 → 在线实验用独立算法生成纯重定向推荐来检验机制 → 通过反事实模拟将效应转化为“按漏斗阶段替换推荐类型”的设计原则。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：基于共同浏览/购买的协同过滤推荐反映“大众偏好”，帮助用户发现新商品；早期购买漏斗中用户偏好尚未收窄，更适合探索性推荐。

- mechanism_cn：通用推荐通过引入用户未浏览过的相关商品来扩大发现面；早期偏好可塑时，用户更可能接受这些新商品并提高购买概率。

- design_requirement_cn：必须在早期漏斗中把“用户未浏览过的推荐”与“用户以前浏览过的推荐”区分开比较。

- artifact_choice_cn：现场实验将推荐曝光按过去浏览标记为generic/retargeted；在线实验用Slope-One选出与FP最高相似且用户未看过的商品作为通用推荐。

- evaluated_contrast_cn：展示vs隐藏；通用推荐vs重定向推荐；早期vs晚期。

- objective_result_cn：只有早期购买漏斗中的通用推荐显著提高转化率；重定向推荐在早晚期均未显著提高转化率。

##### evidence_pointers

1. Table 4

2. Table 7

3. Section 5.1.1.4

4. Section 5.2.4

#### 2. 2

- theory_or_knowledge_claim_cn：重定向广告文献指出重定向广告通过提醒用户此前浏览过的品牌/产品来影响广告转化率；但站内产品推荐不同于第三方广告，会在商城内增加商品曝光机会。

- mechanism_cn：站内展示推荐直接增加推荐商品在焦点商品页的可见性；重复曝光可能提高注册、发出相关性信号、帮助回忆，并提高晚期漏斗中的购买概率。

- design_requirement_cn：不能只估计转化率，还必须估计推荐商品的曝光量变化。

- artifact_choice_cn：以每次FP页浏览生成4条RP曝光；同时在5.1.2中以RP-日面板估计每日曝光量和销售。

- evaluated_contrast_cn：处理组曝光数vs控制组曝光数；重定向推荐曝光量vs通用推荐曝光量。

- objective_result_cn：两种推荐在早晚期均显著增加每日RP曝光量；曝光量增加是销售增长的主要驱动。

##### evidence_pointers

1. Table 5

2. Table 6

3. Section 5.1.2.4

#### 3. 3

- theory_or_knowledge_claim_cn：可观察行为代理中，用户将商品加购说明偏好已经收窄并接近决策，因此加购后的会话代表晚期购买漏斗。

- mechanism_cn：晚期漏斗中用户偏好已收窄，通用推荐不再有帮助；重定向推荐能提醒用户此前探索过的选项并发送相关性信号，从而更有效。

- design_requirement_cn：必须分别估计早期和晚期漏斗中的推荐效果，并在两种情境中使用一致的操作定义。

- artifact_choice_cn：以用户在某子品类首次加购后的会话为晚期，其余为早期；现场与在线实验中均沿用该代理。

- evaluated_contrast_cn：早期漏斗中的通用/重定向推荐vs晚期漏斗中的通用/重定向推荐。

- objective_result_cn：晚期购买漏斗中重定向推荐显著提高RP销售和总销售，通用推荐无显著效应；早期则相反。

##### evidence_pointers

1. Section 3.3

2. Section 3.4

3. Table 6

4. Table 8

5. Table 7

## 评价逻辑

### evaluation_modes

1. 真实网站随机现场实验

2. 模型自由证据与t检验

3. 固定效应Logit/OLS计量模型

4. 多组固定效应与子样本稳健性检验

5. 安慰剂/伪处理检验

6. 受控在线随机实验（MTurk）

7. 反事实模拟与模型选择（k折交叉验证）

- why_these_evaluations_cn：作者需要一个能够操纵推荐是否展示并同时记录用户历史的自然场景，因此使用真实零售网站现场实验；为了把销售效应分解为机制，除转化率回归外还建立RP-日面板估计曝光量；由于现场重定向推荐非外生且与算法推荐混淆，故用在线实验分离重定向算法；最后用反事实模拟把统计效应转化为政策收益。

- benchmark_and_contrast_chain_cn：基础基准是“隐藏推荐”的控制组；随后在曝光量分析中使用“同一天其他条件曝光为0”的RP-日面板构造条件间对比；在机制层面用“通用推荐”作为重定向推荐的对照；在总销售层面用FP+RP总销售排除替代效应；在模拟层面用“不替换”的原始销售作为基线，四种替换策略形成梯度对照，展示替代范围带来的收益与损耗。

### claim_evidence_ledger

#### 1. 1

- claim：显示推荐会增加推荐商品的点击率

- evidence：Table 2/Table 4 点击率在各种条件下显著为正

- status：supported

#### 2. 2

- claim：显示推荐降低条件转化率

- evidence：Table 4 Column (2)，除晚期重定向外均为负

- status：supported

#### 3. 3

- claim：只有早期购买漏斗中的通用推荐提高推荐商品总体转化率

- evidence：Table 4 Column (3)，generic early系数0.4008***

- status：supported

#### 4. 4

- claim：两种推荐都增加推荐商品曝光量

- evidence：Table 6 每日RP曝光量效应全部显著为正

- status：supported

#### 5. 5

- claim：晚期购买漏斗中重定向推荐显著提高RP销售且优于通用推荐

- evidence：Table 6 晚期retargeted RP销售0.0005**，diff 0.0004*；Table 7在线实验重定向销售0.7320***

- status：supported

#### 6. 6

- claim：重定向推荐的效果由重定向本身驱动而非亲和度

- evidence：在线实验随机选择已浏览商品作为重定向推荐，高/低相似度子样本结果相似

- status：supported only for experimental website; field confound not fully removed

#### 7. 7

- claim：按漏斗阶段替换推荐可使总销售提高最多3.19%

- evidence：Table 9 第3-4位替换策略3.19%

- status：supported under counterfactual model; not tested by actual rollout

#### 8. 8

- claim：结果适用于基于商品项的协同过滤推荐系统并具有普遍性

- evidence：现场用IBM Coremetrics，在线用Slope-One，结果定性一致

- status：partially supported; only在线实验换算法，且品类限于服装家居

- internal_validity_strategy_cn：利用随机分配保证处理组与对照组访客统计相似；用RP固定效应吸收产品品质/人气等时间不变混淆；用RP-日/FP-RP-日固定效应控制时间变化需求冲击；用访问者固定效应控制个人浏览倾向；在识别交互项时引用Kumar and Tan (2015)说明，只要内生ReTar作为协变量，其与随机Rec的交互系数可无偏识别；用安慰剂检验排除偶然效应。

- external_validity_strategy_cn：使用真实零售网站与真实购买行为；选择服装和家居这种电商中占比很大的品类；在线实验使用不同的协同过滤算法（Slope-One）并得到相似结果；明确将结论限定在基于商品项的协同过滤推荐系统。

- what_is_not_actually_tested_cn：现场实验并未完全外生生成重定向推荐，因此重定向推荐识别仍依赖用户过去浏览；在线实验不是真实零售商平台，购买动机是激励一致的仿真购物；模拟替换策略并未真正实施到零售商网站；购买漏斗阶段始终是观察行为代理而非实验操纵。

## 贡献闭环

- technical_claim_cn：在基于商品项的协同过滤推荐系统环境中，通用推荐与重定向推荐对推荐商品曝光量和转化率具有可分离且不同的效应；将推荐商品按过去浏览状态与购买漏斗阶段细分，可以改善对推荐销售效应的估计。

- artifact_claim_cn：“按漏斗阶段替换推荐类型”这一轻量级策略（尤其是替换第3-4位推荐）可以在不改变底层协同过滤算法的前提下提高总销售约3%；该主张得到反事实模拟支持，但未被真实实施验证。

- mechanism_claim_cn：推荐商品销售增长主要来自展示带来的曝光量增加，而不是转化率提升；唯一例外是早期购买漏斗中的通用推荐，其通过提高转化率起作用；重定向推荐在晚期通过提醒、相关性信号和回忆机制提高销售，而非算法相似度。

- boundary_claim_cn：结论适用于基于商品项的协同过滤推荐系统、访客有历史浏览记录、以及服装/家居等产品类别；可能不适用于基于模型的推荐算法或其他产品类型。

- reusable_design_knowledge_cn：在线零售商应把推荐分类为用户之前看过（重定向）和未看过（通用），并将购买漏斗阶段作为推荐策略的调节变量：早期优先展示通用推荐，晚期优先展示重定向推荐；可通过观察加购行为和浏览历史低成本实现；替换中低位候选而非全部替换可避免低亲和度损失。

- theoretical_contribution_cn：将重定向广告中的“重定向”概念迁移到产品推荐情境，形成“重定向推荐”构念；指出重定向广告研究只针对转化率，而站内推荐会同时改变曝光量和转化率，从而扩展了重定向理论的适用边界；同时在推荐系统文献中引入了购买漏斗阶段作为权变因素。

- how_discussion_closes_intro_gap_cn：引言提出现有推荐系统文献不区分推荐是否被用户看过、也不考虑漏斗阶段，讨论部分明确以“首次区分重定向推荐与通用推荐”和“按漏斗阶段比较相对效果”作为核心贡献，并以“曝光量而非转化率”回应了为什么站内推荐不能沿用重定向广告的结论。

- overclaim_or_unsupported_leaps_cn：作者将现场和在线实验的定性一致解读为对现场估计内生性的“支持”，但仍在限制中承认不能完全消除；将模拟中的3%销售增益表述为零售商“可以获得”，但这是预测而非实际部署结果；将“推荐主要增加曝光量而非转化率”视为普遍机制，但曝光量指标本身与展示行为高度机械相关；把服装家居结果的相似性外推到整个item-based CF领域仍需谨慎。

## 句级写作动作图谱

### 1. Abstract P1 S1-S2

- order：1

- section：Abstract

- locator：Abstract P1 S1-S2

- move_code：GAP

- paraphrase_cn：现有研究理解算法商品推荐对销售的平均作用，但不清楚重定向推荐与通用推荐的效果差异。

- rhetorical_function_cn：开篇从已知到未知，构造知识缺口。

- depends_on_cn：无，摘要起点。

- sets_up_cn：引出全文核心问题。

- evidence_pointer：Abstract lines 1-2

### 2. Abstract P1 S3-S4

- order：2

- section：Abstract

- locator：Abstract P1 S3-S4

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：用现场实验检验两种推荐在购买漏斗不同阶段的相对效应，并将销售分解为曝光次数和转化率分别估计。

- rhetorical_function_cn：明确研究目标和识别策略。

- depends_on_cn：承接间隙。

- sets_up_cn：预告分解式分析路径。

- evidence_pointer：Abstract lines 3-4

### 3. Abstract P1 S5-S8

- order：3

- section：Abstract

- locator：Abstract P1 S5-S8

- move_code：RESULT

- paraphrase_cn：发现通用推荐只在早期提高转化率，重定向推荐不影响转化率；两种推荐都增加曝光次数；总体上重定向推荐提高晚期销售，通用推荐提高早期销售。

- rhetorical_function_cn：压缩全文核心实证结果。

- depends_on_cn：需要前面对研究设计的预告。

- sets_up_cn：引言中将对结果展开。

- evidence_pointer：Abstract lines 5-8

### 4. Abstract P1 S9-S10

- order：4

- section：Abstract

- locator：Abstract P1 S9-S10

- move_code：RESULT

- paraphrase_cn：MTurk在线实验表明重定向推荐的效果来自重定向本身；反事实模拟显示按发现调整推荐系统可提高最多约3%销售。

- rhetorical_function_cn：以机制验证和经济量化收束摘要。

- depends_on_cn：需要现场结果作为前提。

- sets_up_cn：提供摘要中的价值声明。

- evidence_pointer：Abstract lines 9-10

### 5. Introduction P1 S1

- order：5

- section：Introduction

- locator：Introduction P1 S1

- move_code：CONTEXT

- paraphrase_cn：多数电商网站根据其他用户的共同浏览和共同购买行为在焦点商品页推荐少量相关商品。

- rhetorical_function_cn：建立推荐系统广泛使用的背景。

- depends_on_cn：无。

- sets_up_cn：为定义通用推荐提供技术语境。

- evidence_pointer：Introduction P1 S1

### 6. Introduction P1 S2-S3

- order：6

- section：Introduction

- locator：Introduction P1 S2-S3

- move_code：PHENOMENON

- paraphrase_cn：将这种基于其他用户浏览行为的推荐称为通用推荐；当推荐商品被用户以前看过时，称为重定向推荐。

- rhetorical_function_cn：引入两个关键构念并给出操作定义。

- depends_on_cn：需要前句的协同过滤背景。

- sets_up_cn：后续所有比较都围绕这两个构念展开。

- evidence_pointer：Introduction P1 S2-S3

### 7. Introduction P2 S1

- order：7

- section：Introduction

- locator：Introduction P2 S1

- move_code：PRACTICAL_STAKES

- paraphrase_cn：知道哪种推荐更适合用户并提供给用户，可增加销售。

- rhetorical_function_cn：把构念差异升华为商业价值。

- depends_on_cn：需要已经定义两类推荐。

- sets_up_cn：说明研究为什么重要。

- evidence_pointer：Introduction P2 S1

### 8. Introduction P3 S1-S3

- order：8

- section：Introduction

- locator：Introduction P3 S1-S3

- move_code：MECHANISM

- paraphrase_cn：两类推荐的相对效用可能取决于用户购买阶段：早期用户偏好未定，通用推荐帮助从大量商品中发现；晚期偏好收窄，重定向推荐提醒以前看过的产品。

- rhetorical_function_cn：提出理论机制猜想。

- depends_on_cn：需要前面的构念。

- sets_up_cn：支撑购买漏斗阶段作为调节变量。

- evidence_pointer：Introduction P3 S1-S3

### 9. Introduction P3 S4

- order：9

- section：Introduction

- locator：Introduction P3 S4

- move_code：GAP

- paraphrase_cn：但已有推荐系统研究几乎没有提供关于两类推荐在不同购买阶段相对有效性的指导。

- rhetorical_function_cn：指出现有产品推荐文献的缺口。

- depends_on_cn：需要前面的机制猜想。

- sets_up_cn：为研究问题作铺垫。

- evidence_pointer：Introduction P3 S4

### 10. Introduction P4 S1-S2

- order：10

- section：Introduction

- locator：Introduction P4 S1-S2

- move_code：LIMITATION

- paraphrase_cn：展示广告文献虽比较了通用和重定向广告，但结论无法直接用于产品推荐，因为广告在第三方网站只影响广告转化率，而推荐发生在商家网站且同时影响曝光和转化。

- rhetorical_function_cn：用相邻文献的边界说明现有知识不够用。

- depends_on_cn：需要前面的更广泛文献缺口。

- sets_up_cn：为曝光量+转化率分解铺垫。

- evidence_pointer：Introduction P4 S1-S2

### 11. Introduction P4 S3

- order：11

- section：Introduction

- locator：Introduction P4 S3

- move_code：GAP

- paraphrase_cn：据作者所知，没有研究考察推荐对推荐商品曝光次数及其转化率的影响。

- rhetorical_function_cn：进一步缩小并精确化缺口。

- depends_on_cn：需要前面的限制论证。

- sets_up_cn：引出研究问题。

- evidence_pointer：Introduction P4 S3

### 12. Introduction P5 S1-S3

- order：12

- section：Introduction

- locator：Introduction P5 S1-S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：提出三个问题：何时展示重定向比通用推荐更有价值、相对收益是否随购买漏斗阶段变化、选择性展示的销售增益有多大。

- rhetorical_function_cn：把缺口转化为可回答的研究问题。

- depends_on_cn：需要前面的双重缺口。

- sets_up_cn：定义后面的实证设计。

- evidence_pointer：Introduction P5 S1-S3

### 13. Introduction P6 S1-S2

- order：13

- section：Introduction

- locator：Introduction P6 S1-S2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：在中型服装家居零售商网站做现场实验，处理组页面显示四个推荐商品，控制组隐藏；按用户过去是否浏览将推荐曝光分为重定向和通用。

- rhetorical_function_cn：预告实验设计和操作定义。

- depends_on_cn：需要前面研究问题。

- sets_up_cn：为后文方法细节作索引。

- evidence_pointer：Introduction P6 S1-S2

### 14. Introduction P6 S3

- order：14

- section：Introduction

- locator：Introduction P6 S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：沿用重定向广告文献的做法，把用户在品类中加购后的会话视为购买漏斗晚期，之前为早期。

- rhetorical_function_cn：说明漏斗阶段操作定义有文献依据。

- depends_on_cn：需要实验设计。

- sets_up_cn：为阶段分样本分析提供合法性。

- evidence_pointer：Introduction P6 S3

### 15. Introduction P7 S1-S2

- order：15

- section：Introduction

- locator：Introduction P7 S1-S2

- move_code：RESULT

- paraphrase_cn：两类推荐都增加曝光；只有早期通用推荐提高转化率；重定向推荐不影响转化率；早期两类都提高RP销售但通用更优，晚期只有重定向提高RP销售。

- rhetorical_function_cn：预告核心实证结果。

- depends_on_cn：需要前面的实验概述。

- sets_up_cn：引出机制混淆和处理。

- evidence_pointer：Introduction P7 S1-S2

### 16. Introduction P8 S1-S4

- order：16

- section：Introduction

- locator：Introduction P8 S1-S4

- move_code：STUDY_OVERVIEW

- paraphrase_cn：现场重定向推荐既是被浏览商品也是算法推荐商品，因此用MTurk在线实验把两者分开，随机展示纯重定向或通用推荐，发现晚期用户更常购买重定向商品，说明是重定向效应。

- rhetorical_function_cn：预告第二个实验并解释其必要性。

- depends_on_cn：需要现场结果的机制模糊性。

- sets_up_cn：为5.2节提供逻辑位置。

- evidence_pointer：Introduction P8 S1-S4

### 17. Introduction P9 S1-S2

- order：17

- section：Introduction

- locator：Introduction P9 S1-S2

- move_code：RESULT

- paraphrase_cn：因为推荐商品与焦点商品同属子类别可能产生替代，作者转而估计焦点商品+推荐商品总销售，发现早期通用推荐优、晚期重定向推荐优。

- rhetorical_function_cn：引入管理者更关心的总销售结果。

- depends_on_cn：需要前面的RP销售结果。

- sets_up_cn：引出第5.3节。

- evidence_pointer：Introduction P9 S1-S2

### 18. Introduction P9 S3

- order：18

- section：Introduction

- locator：Introduction P9 S3

- move_code：RESULT

- paraphrase_cn：反事实模拟显示按发现替换现有推荐可使总销售增加最多约3%。

- rhetorical_function_cn：以经济量化加强实践价值。

- depends_on_cn：需要总销售估计。

- sets_up_cn：为模拟章节作预告。

- evidence_pointer：Introduction P9 S3

### 19. Introduction P10 S1-S3

- order：19

- section：Introduction

- locator：Introduction P10 S1-S3

- move_code：CONTRIBUTION

- paraphrase_cn：对IS推荐系统文献的三点贡献：考虑情境因素、比较两类推荐、可与广泛使用的协同过滤推荐系统结合提高销售。

- rhetorical_function_cn：提前声明贡献，建立评价标准。

- depends_on_cn：需要前面的结果。

- sets_up_cn：引出文献综述。

- evidence_pointer：Introduction P10 S1-S3

### 20. Section 2.1.1 P1

- order：20

- section：Literature Review 2.1.1

- locator：Section 2.1.1 P1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：推荐系统分为协同过滤、基于内容和混合三类，且协同过滤在实践中最常用。

- rhetorical_function_cn：为后文的算法选择提供知识基础。

- depends_on_cn：无。

- sets_up_cn：说明研究对象为何是item-based CF。

- evidence_pointer：Section 2.1.1

### 21. Section 2.1.2 P1

- order：21

- section：Literature Review 2.1.2

- locator：Section 2.1.2 P1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：已有研究表明推荐系统能增加产品浏览和销售，例如Lee和Hosanagar的因果实验估计。

- rhetorical_function_cn：总结推荐系统经济价值文献。

- depends_on_cn：无需依赖前文。

- sets_up_cn：显示现有文献关注平均效应。

- evidence_pointer：Section 2.1.2 P1

### 22. Section 2.1.2 P2

- order：22

- section：Literature Review 2.1.2

- locator：Section 2.1.2 P2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：部分研究考察了共览/共购网络和替代品推荐对页面浏览和销售的影响。

- rhetorical_function_cn：补充最近的相关实证。

- depends_on_cn：需要前面的经济价值综述。

- sets_up_cn：进一步说明缺乏情境因素。

- evidence_pointer：Section 2.1.2 P2

### 23. Section 2.1.2 P3

- order：23

- section：Literature Review 2.1.2

- locator：Section 2.1.2 P3

- move_code：GAP

- paraphrase_cn：但这些研究主要关注产品特征，很少考虑访问者情境因素，例如用户是否看过推荐商品以及处于购买漏斗的哪个阶段。

- rhetorical_function_cn：明确识别产品推荐文献的盲点。

- depends_on_cn：需要前面的综述。

- sets_up_cn：为本文的权变视角作铺垫。

- evidence_pointer：Section 2.1.2 P3

### 24. Section 2.1.2 P4

- order：24

- section：Literature Review 2.1.2

- locator：Section 2.1.2 P4

- move_code：MECHANISM

- paraphrase_cn：推荐系统通过在产品页面之间建立网络，可能同时增加推荐商品的曝光量和曝光条件下的购买概率。

- rhetorical_function_cn：提出两个机制维度。

- depends_on_cn：需要产品网络文献。

- sets_up_cn：为分解分析提供概念框架。

- evidence_pointer：Section 2.1.2 P4

### 25. Section 2.1.2 P5

- order：25

- section：Literature Review 2.1.2

- locator：Section 2.1.2 P5

- move_code：CONTRIBUTION

- paraphrase_cn：本文是第一项在如此细粒度上同时考察两类推荐对曝光和转化且区分漏斗阶段的研究。

- rhetorical_function_cn：宣称研究的首创性。

- depends_on_cn：需要前面的缺口。

- sets_up_cn：与后续的贡献段落呼应。

- evidence_pointer：Section 2.1.2 P5

### 26. Section 2.2 P1

- order：26

- section：Literature Review 2.2

- locator：Section 2.2 P1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：展示广告文献发现广告效果因购买漏斗阶段而变化，并采用重定向广告方法。

- rhetorical_function_cn：引入相邻文献。

- depends_on_cn：无。

- sets_up_cn：说明重定向概念来源。

- evidence_pointer：Section 2.2 P1

### 27. Section 2.2 P2

- order：27

- section：Literature Review 2.2

- locator：Section 2.2 P2

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：重定向广告在第三方网站展示并只影响广告转化率，而产品推荐在商家网站页面展示，因此需要同时研究推荐商品的曝光量和转化率。

- rhetorical_function_cn：说明为何不能直接借用重定向广告结论。

- depends_on_cn：需要前面的重定向广告综述。

- sets_up_cn：为本文曝光+转化分解提供理由。

- evidence_pointer：Section 2.2 P2

### 28. Section 2.3 P1

- order：28

- section：Literature Review 2.3

- locator：Section 2.3 P1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：购买路径可分多个阶段，经典AIDA模型和广泛使用的三阶段模型（知晓、考虑、购买）是基础。

- rhetorical_function_cn：介绍购买漏斗理论。

- depends_on_cn：无。

- sets_up_cn：为选择代理变量提供理论背景。

- evidence_pointer：Section 2.3 P1

### 29. Section 2.3 P2

- order：29

- section：Literature Review 2.3

- locator：Section 2.3 P2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：一条文献用隐马尔可夫等潜在状态模型刻画漏斗阶段。

- rhetorical_function_cn：介绍潜在状态方法。

- depends_on_cn：需要前面的漏斗概念。

- sets_up_cn：对比可观察代理方法。

- evidence_pointer：Section 2.3 P2

### 30. Section 2.3 P3

- order：30

- section：Literature Review 2.3

- locator：Section 2.3 P3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：另一条文献用可观察行为代理购买阶段，如Bleier和Eisenbeiss及Sahni等人的做法。

- rhetorical_function_cn：引出与本文一致的操作方式。

- depends_on_cn：需要前面的潜在状态方法对比。

- sets_up_cn：为本文加购后为晚期作依据。

- evidence_pointer：Section 2.3 P3

### 31. Section 2.3 P4

- order：31

- section：Literature Review 2.3

- locator：Section 2.3 P4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：本文沿用该文献流，将用户在某一产品子品类加购后的会话定义为晚期，加购前为早期。

- rhetorical_function_cn：固定全文关键操作定义。

- depends_on_cn：需要前面的代理方法。

- sets_up_cn：为第三章实验设计提供规则。

- evidence_pointer：Section 2.3 P4

### 32. Section 3.2 P1

- order：32

- section：Field Setup

- locator：Section 3.2 P1

- move_code：DESIGN_FEATURE

- paraphrase_cn：零售商用IBM Coremetrics算法计算焦点商品与推荐商品之间的亲和度，公式为共同浏览、浏览后购、放弃后购、共同购买四类分值加权。

- rhetorical_function_cn：说明现场推荐系统的具体实现。

- depends_on_cn：需要第一节的CF算法背景。

- sets_up_cn：让读者知道现场推荐是标准的item-based CF。

- evidence_pointer：Section 3.2 P1

### 33. Section 3.2 P2

- order：33

- section：Field Setup

- locator：Section 3.2 P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：系统只推荐同子品类产品，使推荐品成为替代品；每天计算亲和度并保留前15个候选，页面只展示前4个。

- rhetorical_function_cn：描述推荐规则和替代品属性。

- depends_on_cn：需要亲和度算法。

- sets_up_cn：为模拟章节的可替换候选提供基础。

- evidence_pointer：Section 3.2 P2

### 34. Section 3.3 P1-P2

- order：34

- section：Field Setup

- locator：Section 3.3 P1-P2

- move_code：PHENOMENON

- paraphrase_cn：将焦点商品页浏览视为四条推荐商品曝光；若曝光商品在过去会话被用户看过，则为重定向曝光，否则为通用曝光。

- rhetorical_function_cn：给出全文核心分析单位的定义。

- depends_on_cn：需要前面的页面结构。

- sets_up_cn：为曝光量分解提供计数单位。

- evidence_pointer：Section 3.3 P1-P2

### 35. Section 3.3 P3

- order：35

- section：Field Setup

- locator：Section 3.3 P3

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：即使推荐商品没有在焦点商品页显示，访客也可能通过搜索、相邻展示或共同出现知道两者关系，因此控制组仍可看到这类商品。

- rhetorical_function_cn：确认隐藏推荐的控制组是有意义的反事实而非完全无推荐。

- depends_on_cn：需要定义推荐曝光。

- sets_up_cn：为随机实验的对照有效性辩护。

- evidence_pointer：Section 3.3 P3

### 36. Section 3.3 P4

- order：36

- section：Field Setup

- locator：Section 3.3 P4

- move_code：MECHANISM

- paraphrase_cn：在页面显式展示推荐有两个额外作用：增加被发现机会，以及帮助用户学习商品间的相似关系。

- rhetorical_function_cn：解释展示推荐为什么影响曝光和购买。

- depends_on_cn：需要前面的对照论证。

- sets_up_cn：为曝光量和转化率的双重分解提供机制。

- evidence_pointer：Section 3.3 P4

### 37. Section 3.3 P5

- order：37

- section：Field Setup

- locator：Section 3.3 P5

- move_code：MECHANISM

- paraphrase_cn：重复曝光能增加登记概率、发送相关性信号、帮助回忆并表明用户已看过该品类大部分商品，因此重定向推荐与通用推荐效果不同。

- rhetorical_function_cn：解释重定向推荐的独特心理学机制。

- depends_on_cn：需要重定向构念。

- sets_up_cn：为晚期重定向更有效提供机制预测。

- evidence_pointer：Section 3.3 P5

### 38. Section 3.3 P6

- order：38

- section：Field Setup

- locator：Section 3.3 P6

- move_code：MECHANISM

- paraphrase_cn：早期漏斗用户偏好可塑，基于他人的通用推荐更有利；晚期偏好收窄，重定向推荐因相关性信号或回忆作用更有利。

- rhetorical_function_cn：把机制与漏斗阶段连接，形成可检验预测。

- depends_on_cn：需要前面的重定向心理学机制。

- sets_up_cn：引出表1的实验设计。

- evidence_pointer：Section 3.3 P6

### 39. Section 3.3 P7

- order：39

- section：Field Setup

- locator：Section 3.3 P7

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：总结预期：两类推荐的效果取决于是否显示、是否以前看过以及购买漏斗阶段，并按表1的八格设计估计相对效率。

- rhetorical_function_cn：将机制转化为实验矩阵。

- depends_on_cn：需要前一句的机制。

- sets_up_cn：为3.4节的随机实验设计作逻辑准备。

- evidence_pointer：Table 1附近

### 40. Section 3.4 P1

- order：40

- section：Field Setup

- locator：Section 3.4 P1

- move_code：DESIGN_FEATURE

- paraphrase_cn：网站创建两个版本：处理组展示四个推荐商品，控制组隐藏；随机分配访客并在后续会话保持一致版本。

- rhetorical_function_cn：说明现场随机实验的具体操纵。

- depends_on_cn：需要前节的八格设计。

- sets_up_cn：提供数据来源和因果识别基础。

- evidence_pointer：Section 3.4 P1

### 41. Section 3.4 P2

- order：41

- section：Field Setup

- locator：Section 3.4 P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用户在某子品类开始浏览即进入该品类的购买漏斗，加购后会话进入晚期，其他会话为早期。

- rhetorical_function_cn：详细定义漏斗阶段，使分析可复制。

- depends_on_cn：需要文献综述中的代理方法。

- sets_up_cn：支撑后续早晚期分样本估计。

- evidence_pointer：Section 3.4 P2

### 42. Section 3.4 P3

- order：42

- section：Field Setup

- locator：Section 3.4 P3

- move_code：LIMITATION

- paraphrase_cn：现场设计有两个缺点：重定向推荐同时含重定向和算法推荐两个因素；且两类推荐非外生生成，可能带来偏差。

- rhetorical_function_cn：主动承认设计限制并预告补救措施。

- depends_on_cn：需要实验设计。

- sets_up_cn：引出5.2节的在线实验。

- evidence_pointer：Section 3.4 P3

### 43. Section 4 P1

- order：43

- section：Data Description

- locator：Section 4 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：要识别重定向曝光至少需要两次会话，故主要分析多会话访客，共70,881个会话、47,697位访客。

- rhetorical_function_cn：说明样本选择规则。

- depends_on_cn：需要重定向定义。

- sets_up_cn：为样本量和平衡性检验提供依据。

- evidence_pointer：Section 4 P1

### 44. Section 4 P2

- order：44

- section：Data Description

- locator：Section 4 P2

- move_code：RESULT

- paraphrase_cn：处理组里访客访问推荐商品页面的概率为25%，控制组也有17%，说明即使不显示，访客也知道焦点商品与推荐商品的关系。

- rhetorical_function_cn：用数据证明控制组不是完全无推荐状态。

- depends_on_cn：需要处理/控制会话数据。

- sets_up_cn：使处理效应解释更可信。

- evidence_pointer：Section 4 P2

### 45. Section 5.1.1.1 P1

- order：45

- section：Analysis 5.1.1.1

- locator：Section 5.1.1.1 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：将每个焦点商品页浏览组织为四条推荐曝光，共得到846,804条曝光，其中52.2%在处理组。

- rhetorical_function_cn：建立细粒度分析数据集。

- depends_on_cn：需要曝光定义。

- sets_up_cn：为模型自由证据和回归分析提供样本。

- evidence_pointer：Section 5.1.1.1

### 46. Section 5.1.1.2 P1

- order：46

- section：Analysis 5.1.1.2

- locator：Section 5.1.1.2 P1

- move_code：RESULT

- paraphrase_cn：描述性统计显示显示推荐提高点击率、降低条件转化率；总体上早期通用推荐提高转化率，重定向推荐在早晚期降低转化率。

- rhetorical_function_cn：先给模型自由证据。

- depends_on_cn：需要曝光面板数据。

- sets_up_cn：与后面的回归结果互相印证。

- evidence_pointer：Table 2

### 47. Section 5.1.1.3 P1

- order：47

- section：Analysis 5.1.1.3

- locator：Section 5.1.1.3 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：按早期和晚期购买漏斗分成两个子样本，分别估计带固定效应的Logit规范（1）。

- rhetorical_function_cn：说明统计识别策略。

- depends_on_cn：需要前面的描述性证据。

- sets_up_cn：为系数解释表3铺垫。

- evidence_pointer：Specification (1)

### 48. Section 5.1.1.3 P3

- order：48

- section：Analysis 5.1.1.3

- locator：Section 5.1.1.3 P3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：产品层面未观测特征可能同时影响曝光和购买，加入推荐商品固定效应后，Rec变量因随机分配和固定效应而外生。

- rhetorical_function_cn：处理产品层面混淆。

- depends_on_cn：需要规范(1)。

- sets_up_cn：为内生性讨论提供基础。

- evidence_pointer：Section 5.1.1.3

### 49. Section 5.1.1.3 P4

- order：49

- section：Analysis 5.1.1.3

- locator：Section 5.1.1.3 P4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：访客层面因素可能使ReTar内生，但只要ReTar作为协变量进入方程，其与随机Rec交互项的系数在RP固定效应控制后可无偏估计。

- rhetorical_function_cn：说明交互项识别的理论依据。

- depends_on_cn：需要前面的内生性讨论。

- sets_up_cn：为后续结果增加可信度。

- evidence_pointer：Section 5.1.1.3

### 50. Section 5.1.1.4 P1-P3

- order：50

- section：Analysis 5.1.1.4

- locator：Section 5.1.1.4 P1-P3

- move_code：RESULT

- paraphrase_cn：回归结果与描述证据一致：显示推荐提高点击率、降低条件转化率；只有早期通用推荐显著提高总体转化率。

- rhetorical_function_cn：给出转化率分析的核心结论。

- depends_on_cn：需要前面的识别策略。

- sets_up_cn：为曝光量和销售分析提供组件。

- evidence_pointer：Table 4

### 51. Section 5.1.2.1 P1

- order：51

- section：Analysis 5.1.2.1

- locator：Section 5.1.2.1 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：以推荐商品-日-条件为单位，某日未出现的条件记为0，构造每日曝光量和销售面板。

- rhetorical_function_cn：建立曝光量分析的数据结构。

- depends_on_cn：需要RP-日数据。

- sets_up_cn：为模型(2)提供数据。

- evidence_pointer：Section 5.1.2.1

### 52. Section 5.1.2.2 P1

- order：52

- section：Analysis 5.1.2.2

- locator：Section 5.1.2.2 P1

- move_code：RESULT

- paraphrase_cn：处理组的每日曝光和销售在几乎所有条件下高于控制组；晚期重定向销售高于早期，而晚期通用销售无提升。

- rhetorical_function_cn：提供曝光/销售的描述性证据。

- depends_on_cn：需要RP-日面板。

- sets_up_cn：引出回归估计。

- evidence_pointer：Table 5

### 53. Section 5.1.2.4 P1-P2

- order：53

- section：Analysis 5.1.2.4

- locator：Section 5.1.2.4 P1-P2

- move_code：RESULT

- paraphrase_cn：两种推荐在早晚期都显著提高每日曝光；早期通用和重定向都提高RP销售但通用更优，晚期只有重定向显著提高销售；销售增长主要由曝光量驱动。

- rhetorical_function_cn：汇总曝光量/销售估计的核心结果。

- depends_on_cn：需要前面的回归模型。

- sets_up_cn：为总销售和替代性解释提供基础。

- evidence_pointer：Table 6

### 54. Section 5.1.2.5 P1

- order：54

- section：Analysis 5.1.2.5

- locator：Section 5.1.2.5 P1

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：通过多重固定效应、单会话访客、新顾客、仅两阶段访客、排除加购/相似商品以及安慰剂检验，核心结果仍然稳健。

- rhetorical_function_cn：集中展示稳健性和排除替代解释。

- depends_on_cn：需要前面主结果。

- sets_up_cn：强化因果解释。

- evidence_pointer：Section 5.1.2.5

### 55. Section 5.2.1 P1

- order：55

- section：Online Experiment 5.2.1

- locator：Section 5.2.1 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：为弥补现场实验限制，作者在MTurk开展两阶段在线实验，第一阶段浏览或加购，第二阶段随机显示/隐藏推荐。

- rhetorical_function_cn：介绍在线实验的整体设计。

- depends_on_cn：需要现场实验的限制说明。

- sets_up_cn：为后续独立算法生成推荐作铺垫。

- evidence_pointer：Section 5.2.1

### 56. Section 5.2.2 P1-P2

- order：56

- section：Online Experiment 5.2.2

- locator：Section 5.2.2 P1-P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：用Slope-One算法识别通用推荐；重定向推荐从第一阶段查看过的产品中随机选择；两者由独立算法产生且保证用户未看过通用推荐。

- rhetorical_function_cn：实现在线实验对两种推荐算法的干净分离。

- depends_on_cn：需要前面的实验设计。

- sets_up_cn：可检验重定向效应是否独立于算法相似度。

- evidence_pointer：Section 5.2.2

### 57. Section 5.2.4 P1-P2

- order：57

- section：Online Experiment 5.2.4

- locator：Section 5.2.4 P1-P2

- move_code：RESULT

- paraphrase_cn：在线实验中，只有早期通用推荐提高转化率；两种推荐都增加曝光；早期两类都提高RP销售，晚期只有重定向推荐提高销售，与现场结果一致。

- rhetorical_function_cn：展示在线实验的核心结果并对照现场。

- depends_on_cn：需要在线实验数据。

- sets_up_cn：为机制讨论提供证据。

- evidence_pointer：Table 7

### 58. Section 5.2.5 P1-P2

- order：58

- section：Online Experiment 5.2.5

- locator：Section 5.2.5 P1-P2

- move_code：CONTRIBUTION

- paraphrase_cn：在线实验证明晚期重定向销售由重定向驱动，与算法亲和度无关；高/低相似度子样本结果相似。

- rhetorical_function_cn：把在线结果提升为机制结论。

- depends_on_cn：需要Table 7结果。

- sets_up_cn：为综合讨论提供机制部分。

- evidence_pointer：Section 5.2.5

### 59. Section 5.3 P1

- order：59

- section：Total Sales 5.3

- locator：Section 5.3 P1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：由于推荐商品可能替代焦点商品，作者进一步估计焦点商品+推荐商品的总销售，以提供管理相关结论。

- rhetorical_function_cn：引入总销售分析的重要性。

- depends_on_cn：需要RP销售结果。

- sets_up_cn：引出模型(3)和(4)。

- evidence_pointer：Section 5.3 P1

### 60. Section 5.3 P2-P4

- order：60

- section：Total Sales 5.3

- locator：Section 5.3 P2-P4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用FP页面级转化率和每日FP曝光/销售规范估计总销售效应。

- rhetorical_function_cn：说明总销售分析的估计方法。

- depends_on_cn：需要前面的总销售问题。

- sets_up_cn：为Table 8结果提供依据。

- evidence_pointer：Specification (3) and (4)

### 61. Section 5.3 P5

- order：61

- section：Total Sales 5.3

- locator：Section 5.3 P5

- move_code：RESULT

- paraphrase_cn：总销售估计与RP销售一致：早期通用推荐更优、晚期重定向推荐更优。

- rhetorical_function_cn：呈现总销售核心结果。

- depends_on_cn：需要前面的方法。

- sets_up_cn：为模拟提供政策变量。

- evidence_pointer：Table 8

### 62. Section 6 P1

- order：62

- section：Simulation 6

- locator：Section 6 P1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：通过模拟估计把晚期/早期中的通用/重定向推荐替换为另一类型所能带来的销售增益。

- rhetorical_function_cn：预告模拟目标。

- depends_on_cn：需要总销售结果。

- sets_up_cn：为进行反事实预测作准备。

- evidence_pointer：Section 6 P1

### 63. Section 6 P2-P3

- order：63

- section：Simulation 6

- locator：Section 6 P2-P3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用前15个候选推荐中的第5-15位作为替代来源，用Logit模型预测反事实购买概率，并通过交叉验证选择预测表现最佳的模型。

- rhetorical_function_cn：说明反事实模拟的具体实现。

- depends_on_cn：需要前面推荐系统的15候选规则。

- sets_up_cn：为Table 9结果提供方法基础。

- evidence_pointer：Section 6 P2-P3

### 64. Section 6 P4-P5

- order：64

- section：Simulation 6

- locator：Section 6 P4-P5

- move_code：RESULT

- paraphrase_cn：替换第3-4位推荐可使总销售提高3.19%；替换全部前4位只提高0.81%，因为低亲和度损失抵消了类型调整收益。

- rhetorical_function_cn：给出模拟的经济量化结果。

- depends_on_cn：需要反事实模型。

- sets_up_cn：为管理建议提供直接依据。

- evidence_pointer：Table 9

### 65. Section 7.1 P1

- order：65

- section：Discussion 7.1

- locator：Section 7.1 P1

- move_code：CONTRIBUTION

- paraphrase_cn：作者从重定向广告文献引入重定向推荐概念，并指出站内推荐同时影响转化率和曝光量，因此广告文献只能提供有限指导。

- rhetorical_function_cn：定义理论贡献并回应引言缺口。

- depends_on_cn：需要全文结果。

- sets_up_cn：为机制贡献做铺垫。

- evidence_pointer：Section 7.1 P1

### 66. Section 7.1 P2

- order：66

- section：Discussion 7.1

- locator：Section 7.1 P2

- move_code：CONTRIBUTION

- paraphrase_cn：核心发现是早期通用推荐更有效、晚期重定向更有效，且推荐销售增加主要由曝光量驱动，而非转化率。

- rhetorical_function_cn：把结果上升为一般贡献。

- depends_on_cn：需要前面的概念贡献。

- sets_up_cn：为管理含义和边界条件作基础。

- evidence_pointer：Section 7.1 P2

### 67. Section 7.2 P1-P2

- order：67

- section：Discussion 7.2

- locator：Section 7.2 P1-P2

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：零售商可根据浏览历史分类推荐类型和漏斗阶段，在晚期替换低排名的通用推荐为重定向推荐，在早期做相反替换。

- rhetorical_function_cn：将发现转化为操作原则。

- depends_on_cn：需要模拟结果。

- sets_up_cn：为可复用设计知识提供具体形式。

- evidence_pointer：Section 7.2

### 68. Section 7.3 P1

- order：68

- section：Discussion 7.3

- locator：Section 7.3 P1

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：结论适用于最常用的基于商品项的协同过滤推荐系统，并适用于服装、配饰和家居等电商大品类。

- rhetorical_function_cn：明确结论边界，避免过度推广。

- depends_on_cn：需要在线实验的算法变化验证。

- sets_up_cn：引出限制与未来研究。

- evidence_pointer：Section 7.3

### 69. Section 7.4 P1

- order：69

- section：Discussion 7.4

- locator：Section 7.4 P1

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：现场中重定向推荐非外生生成，虽然做了大量固定效应和在线实验验证，但仍建议未来设计完全随机的推荐实验。

- rhetorical_function_cn：诚实承认因果识别局限。

- depends_on_cn：需要现场结果。

- sets_up_cn：限制贡献强度。

- evidence_pointer：Section 7.4 P1

### 70. Section 7.4 P2

- order：70

- section：Discussion 7.4

- locator：Section 7.4 P2

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：用可观察行为代理漏斗阶段有局限性，未来可用更精确的潜在状态建模。

- rhetorical_function_cn：补充方法和理论上的未来方向。

- depends_on_cn：需要前面的代理定义。

- sets_up_cn：结束全文。

- evidence_pointer：Section 7.4 P2

## 写作技术

- gap_construction_cn：作者先承认推荐系统平均效应已知，再在主文献中发现“是否看过推荐商品”和“购买阶段”两个维度未被考虑；随后用展示广告文献作对照，指出重定向广告发生在第三方网站且只影响转化率，而站内推荐会影响曝光量和转化率，由此形成双重缺口：概念缺口（没有重定向推荐构念）和机制缺口（没有分解曝光与转化）。

- signposting_cn：引言用三个显式研究问题预告全文；摘要用“field experiment”“MTurk experiment”“counterfactual simulations”形成路线；正文在每个小节开头先说明要做什么，例如5.1先说明把RP销售分解为转化率和曝光量；5.2开头回顾现场设计的两点局限并预告在线实验；5.3开头提出管理相关性问题。

- transition_logic_cn：各阶段通过“尚未解决的不确定性”衔接：转化率分析留下“重定向与算法混淆”，故接在线实验；RP销售分析留下“未考虑替代”，故接FP+RP总销售；总销售效应留下“经济价值未量化”，故接反事实模拟；每个阶段最后常以“与现场结果一致”或“管理相关性”收束。

- claim_evidence_rhythm_cn：每类分析都采用“数据描述—模型自由证据—计量规范—结果—稳健性”的顺序；模型自由证据先给直观差异，回归结果再给统计显著性，最后稳健性检验排除替代解释；总销售和模拟则分别放在主因果分析之后作为管理拓展。

- benchmark_narrative_cn：基准叙事不是单一benchmark，而是多层反事实：控制组（隐藏推荐）→ 条件间零曝光填充 → 通用推荐作为重定向推荐的对照 → 不替换的原销售作为模拟基线；通过反复强调“即使控制组也有17%概率看到RP”来说明隐藏推荐的合理前提。

- theory_return_cn：结果不直接建模理论变量，但在讨论中用“曝光量而非转化率”回应站内推荐与重定向广告的差异，用“晚期购买偏好收窄、重定向信号相关”解释重定向推荐在晚期的优势，使实证发现回到文献综述中的机制猜想。

- contribution_positioning_cn：贡献定位有三个层次：概念层（引入重定向推荐构念）、机制层（曝光量vs转化率分解）、实践层（可嵌入现有CF系统并量化收益）；与引言中的缺口一一对应，并以“首次”“现有文献未记录”等措辞保护新颖性。

- novelty_protection_cn：作者始终把研究放在现有商品项协同过滤推荐算法之上，强调只修改“向谁显示什么类型推荐”而不改变算法；通过在线实验更换算法（Slope-One）证明结果不是某一算法特有；通过模拟显示对现有系统增量收益可达3%，避免贡献沦为单点性能结果。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：撰写引言：从推荐系统普遍现象出发，引入重定向推荐与通用推荐的构念，并指出现有文献忽略的情境因素。

- research_job_cn：界定构念、操作化“重定向”和“购买漏斗阶段”，找到真实平台或能模拟该情境的场域。

- required_evidence_cn：需要能够随机操纵推荐展示并追踪访客历史浏览的真实网站数据；否则需准备在线实验环境。

- transition_to_next_cn：用“现有重定向广告结论不能直接迁移”引出研究问题。

#### 2. 2

- step：2

- writing_job_cn：文献综述：分产品推荐、重定向广告、购买漏斗三个阶段分别综述，并在每一段末尾指出与本文的缺口。

- research_job_cn：梳理已有推荐效果研究和购买漏斗的操作化方法。

- required_evidence_cn：需要足够的实证文献支撑平均效应与重定向广告效果差异。

- transition_to_next_cn：最后确定本文采用“加购后为晚期”的代理定义，并进入现场设计。

#### 3. 3

- step：3

- writing_job_cn：现场设置与实验设计：说明推荐算法、页面结构、随机分配、曝光定义和漏斗阶段定义，并主动列出局限。

- research_job_cn：与平台合作实现处理/控制版本，记录曝光级数据，明确处理、重定向、阶段三类变量。

- required_evidence_cn：需要随机分配验证（平衡检验）、处理组和对照组均可观察到推荐商品的近似反事实。

- transition_to_next_cn：以“现场数据存在混淆和非外生性”引出在线实验和计量识别。

#### 4. 4

- step：4

- writing_job_cn：主分析：先分解结果变量（如转化率与曝光量），用模型自由证据和固定效应回归呈现核心效应。

- research_job_cn：分别估计不同条件下点击率、条件转化率、总体转化率、每日曝光量和销售，并作固定效应识别。

- required_evidence_cn：需要曝光级面板和有助于识别交互项的随机分配，以及控制产品固定效应后的显著性结果。

- transition_to_next_cn：以“重定向与算法混淆”或“替代效应”等未解决问题引出下一步。

#### 5. 5

- step：5

- writing_job_cn：机制实验：设计一个干净实验把混淆因素分开，并说明结果与主实验一致。

- research_job_cn：在线实验中使用独立算法生成重定向推荐与通用推荐，并加入激励一致性机制保证真实购买。

- required_evidence_cn：需要参与者足够多、两阶段设计能够形成购买漏斗、以及注意力检验保证数据质量。

- transition_to_next_cn：机制确认后，转向管理者关心的总销售口径。

#### 6. 6

- step：6

- writing_job_cn：总销售与模拟：用总结果排除替代效应，用反事实模拟量化政策收益。

- research_job_cn：在总销售口径上重复主估计；基于现有推荐算法候选集设计替换策略并预测反事实。

- required_evidence_cn：需要总商品层面的销售数据和模型预测验证（如交叉验证）。

- transition_to_next_cn：在讨论中将模拟收益转化为可操作原则。

#### 7. 7

- step：7

- writing_job_cn：讨论与结论：分贡献、管理含义、普遍性、限制与未来四部分收束，明确边界条件。

- research_job_cn：把实证发现回接到理论和文献，诚实交代未检验环节。

- required_evidence_cn：需要能够支撑所有贡献点的证据映射；没有证据的贡献只能在限制中说明。

- transition_to_next_cn：结束全文。

### most_transferable_moves_cn

1. 引入新构念时从相邻领域（重定向广告）借词并说明差异

2. 用“结果分解”打开黑箱，例如把销售分解为曝光量×转化率

3. 在每个阶段末尾主动声明“尚未解决的不确定性”以引出下一实验

4. 用模型自由证据和回归结果互证

5. 通过更换算法或平台来证明结果不依赖特定实现

6. 用反事实模拟把统计效应翻译成政策收益

### resource_intensive_or_nonstandard_parts_cn

1. 真实零售网站9周随机现场实验需要零售平台配合和工程改动

2. IBM Coremetrics推荐算法和每日候选集属于企业私有数据

3. MTurk 1,200名参与者两阶段实验和先导实验需要资金和时间

4. 商品评价数据收集（1,000名MTurk工人）用于生成相似度

5. 反事实模拟需要推荐候选排名（前15）和价格数据

### what_not_to_copy_superficially_cn

1. 不能只写“首次区分重定向推荐和通用推荐”而没有真实历史浏览数据

2. 不能把依赖模拟的3%销售增益说成已实施政策的效果

3. 不能在没有随机分配的情况下复制固定效应模型并声称因果

4. 不能把现场推荐与在线实验的一致性当作完全外生实验的证据

5. 不能忽略控制组也可能通过搜索看到推荐商品，否则反事实无效

- single_best_description_of_the_routine_cn：把现有推荐算法之外的一个简单情境标签（用户是否看过、处于漏斗哪一阶段）变成随机实验的处理维度，先分解结果变量找机制，再用第二个实验拆掉混淆，最后用模拟把效应换成钱。

## 分析边界

本分析基于用户提供的全文文本，在线附录D-J只在正文中被引用而未在文本中展开，因此涉及附录的稳健性细节和具体估计系数只能依据正文描述推断；正文未提供PDF页码，位置证据以章节和段落标识。
