# Real-Time Sales Data, Streamer Improvisation, and Sales Performance: Evidence From Live Stream Selling

- 作者：Yumei He; Ni Huang; Lingli Wang; Yan Sun
- 年份 / 期刊：2025 / MIS Quarterly
- DOI：10.25300/misq/2025/18627
- 源文件：15532_2025_real-time-sales-data-streamer-improvisation-and-sales-performance-evidence-from-live-stream-sell.md
- 论文主类型：field_intervention_or_platform_experiment
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.88

## 文章级论证概况

- 核心问题：在直播带货的快节奏、高不确定性和时间压力环境中，向主播提供预售商品的实时销售数据是否、如何以及在什么条件下影响主播的即兴销售策略并最终提升销售业绩。

- 制品与设计：平台侧随机现场实验：处理组主播在主播端仪表盘中可以看到预售商品的实时销售数据（如定金总额、尾款总额），控制组主播看不到这些预售数据；每个商品只在一个组内销售以避免跨组污染。

- 客观结果：处理组预售商品销量比控制组高约40.21%；机制分析显示处理组主播更多使用催促下单、情感词、加快语速并缩短单品直播时间；异质性分析显示对小型商家商品、经验品、高评分主播和高人气主播的正面效果更明显。

- 核心贡献：作者声称推进了数据驱动决策研究，证明实时数据在紧急环境中通过流式即兴（improvisation）而非历史数据的计划式分析起作用；同时将即兴理论扩展到缺乏物理观众反馈的直播带货情境，并提出实时数据仪表盘作为IT制品设计支持主播临场决策。

- 整篇论证链：文章从直播带货主播必须同时处理多项任务、面对不可预测观众反应和强时间压力这一现实问题出发，指出现有数据驱动决策研究主要关注历史数据对计划决策的作用，缺少实时数据对即兴决策的实证证据。作者用即兴理论说明，在缺乏物理观众反馈的线上直播场景中，实时销售数据可以像音乐演出的观众反应一样充当反馈信号，但也可能造成认知负荷，因此需要现场因果证据。作者借助淘宝直播平台在2020年12月1日至3日对预售商品开展的随机现场实验，将是否能看到预售实时销售数据作为处理变量，在流-商品层面估计主效应，从ASR转写文本和LIWC中提取销售战术进行中介分析，并通过产品不确定性和主播即兴能力异质性、多种反事实检验和替代机制排除进一步支持即兴解释。最后回到理论，主张实时数据在数据驱动决策中扮演不同于历史数据的角色，为平台实时数据基础设施建设提供指导。

## 类型与写作弧线判定

- 论文主类型判定：核心证据来自真实平台（淘宝直播）上的随机现场实验，平台对主播端仪表盘的实时销售数据可见性进行操纵，作者基于平台产生的流、商品、主播及语音转写数据估计因果效应，并辅以中介、异质性和反事实检验。这不是纯benchmark、纯设计科学制品或纯理论模型，而是真实平台场景中的数字信息反馈干预。

- 主导写作弧线判定：文章先提出实时直播场景下的即兴决策问题，引入即兴理论和System 1/System 2框架，将实时销售数据仪表盘视为IT制品设计，通过随机现场实验检验该设计的效果和机制，最后在讨论中回到理论。

## 研究开展程序

- study_or_phase_count：7

- 研究阶段总序列：第一阶段建立随机化有效性和总效应；第二阶段用语音文本和LIWC战术指标打开机制；第三、第四阶段分别用产品不确定性和主播即兴能力检验边界条件以强化机制推断；第五阶段通过仪表盘未使用、非预售无溢出、普通商品比例、浏览量访问量等反事实检验巩固因果解释；第六阶段排除价格调整替代机制；第七阶段比较实时数据与历史需求记录，突出实时数据的独特作用并转入讨论。

### studies_or_phases

#### 1. 随机化检查与主效应估计

- order：1

- name_cn：随机化检查与主效应估计

- question_cn：提供预售商品实时销售数据是否提高预售商品销量？

- inputs_and_setting_cn：2020年12月1-3日淘宝直播平台随机现场实验；457名主播，其中处理组192名、控制组265名；最终样本9,063个流-商品预售观测；主播层协变量用于随机化检查。

- designed_or_compared_object_cn：处理组主播仪表盘上可看到预售商品实时销售数据，控制组看不到；两类主播对常规商品都能看到实时数据。

- baseline_control_or_counterfactual_cn：控制组没有预售实时销售数据；同一商品只在一个组内销售以避免污染。

##### objective_metrics

1. Log(sales)：预售商品在单个直播流中的销售数量取对数

2. Treatment系数

- analysis_method_cn：流-商品层面的OLS回归，加入流媒体类、产品类、日期、时段固定效应，标准误在直播流层面聚类；先进行流媒体层协变量的随机化检查。

- main_result_cn：处理系数β=0.338，p<0.05，对应销量增加40.21%；随机化检查显示处理组与控制组在知名度、职业主播、网红身份、直播场次、时长和评分上无显著差异。

- argumentative_role_cn：建立实时销售数据对销售业绩的因果总效应，证明该IT反馈设计在经济上有意义。

- remaining_uncertainty_cn：总效应没有解释机制：到底是因为主播改进了销售战术，还是因为价格调整、注意力分散或跨组竞争等替代解释。

- link_to_next_phase_cn：需要检查主播实际行为是否存在策略性变化，因此转向语音脚本的销售战术中介分析。

##### evidence_pointers

1. Table 3 Randomization Checks

2. Table 4 Estimation of Main Effect

3. Research Context and Experimental Design段落

#### 2. 销售战术中介分析

- order：2

- name_cn：销售战术中介分析

- question_cn：实时销售数据是否通过主播在促销、语言和呈现节奏上的即兴战术改变而提高销量？

- inputs_and_setting_cn：直播录音经Universal ASR转写并按商品切分；LIWC提取语言特征；与主播访谈校准战术关键词；PROCESS模型5000次bootstrap。

- designed_or_compared_object_cn：比较处理组与控制组在推荐、催促、预售信息、库存信息、情感词、认知词、语速、单品时长等销售战术上的差异。

- baseline_control_or_counterfactual_cn：将控制组销售战术作为基线，处理组显著偏离基线即视为数据驱动的即兴差异。

##### objective_metrics

1. 各销售战术的间接效应

2. Direct effect和间接效应95%置信区间

- analysis_method_cn：多中介PROCESS模型，bootstrap 5000次；基于直播音频转写文本测量战术频率和速度。

- main_result_cn：催促下单、情感词、语速和单品直播时长四个战术显著中介实时销售数据对销量的作用；推荐、预售信息、库存信息、认知词不显著。

- argumentative_role_cn：把抽象即兴机制操作化为可观察的销售战术变化，说明主播确实根据实时数据调整临场行为。

- remaining_uncertainty_cn：中介战术是观察性行为差异，不能直接证明主播的认知过程就是“即兴”；需要边界条件提供额外证据。

- link_to_next_phase_cn：进一步用即兴理论要求的两个条件——不确定性和即兴能力——做异质性分析，增加机制的可信度。

##### evidence_pointers

1. Figure 3 Multiple Mediation Analyses

2. Table 5 Descriptions and Theoretical Rationale of tactics

3. Table 6 Direct and Indirect Effects in the PROCESS Model

#### 3. 产品不确定性异质性分析

- order：3

- name_cn：产品不确定性异质性分析

- question_cn：实时销售数据的正面效应是否在产品不确定性更高时更显著？

- inputs_and_setting_cn：流-商品层面的Brand-Owned变量区分品牌店和小商家；附录用经验品vs搜索品作为不确定性替代测量。

- designed_or_compared_object_cn：比较品牌店商品与小商家商品，以及经验品与搜索品。

- baseline_control_or_counterfactual_cn：品牌店/搜索品作为低不确定性基线，小商家/经验品作为高不确定性条件。

##### objective_metrics

1. Treatment × Brand-Owned交互项

2. Treatment × Experience Good交互项

3. 子样本Treatment系数

- analysis_method_cn：加入交互项的全样本回归和按不确定性拆分的子样本回归，固定效应同主分析。

- main_result_cn：品牌店交互项显著为负（β=-0.774），小商家子样本效应显著（β=0.836）；经验品交互显著为正（β=0.678），经验品子样本正向显著，搜索品子样本负向显著。

- argumentative_role_cn：不确定性是即兴的必要条件，异质性符合即兴理论预测，为机制提供非直接但一致的支持。

- remaining_uncertainty_cn：产品所有权和经验品分类是代理变量；搜索品子样本出现负效应且样本不平衡，需要谨慎解释。

- link_to_next_phase_cn：即兴能力同样是即兴理论的关键条件，因此继续检验主播评分和人气。

##### evidence_pointers

1. Table 7 Heterogeneity by Brand-Owned Products

2. Appendix D Table D1 Experience vs. Search Good

#### 4. 主播即兴能力异质性分析

- order：4

- name_cn：主播即兴能力异质性分析

- question_cn：实时销售数据的效应是否在高即兴能力主播中更显著？

- inputs_and_setting_cn：平台给定的主播评分KPI（Top-rated streamer=5/5）作为即兴能力代理；附录使用实验前粉丝数构造Popular Streamer作为替代。

- designed_or_compared_object_cn：比较Top-rated vs 非Top-rated主播，以及高人气vs低人气主播。

- baseline_control_or_counterfactual_cn：非Top-rated和低人气主播作为低即兴能力基线。

##### objective_metrics

1. Treatment × Top-Rated Streamer交互项

2. Treatment × Popular Streamer交互项

3. 子样本Treatment系数

- analysis_method_cn：交互项全样本回归和按评分/人气拆分的子样本回归。

- main_result_cn：Top-rated交互项β=0.598显著；Top-rated子样本β=0.606显著，非Top-rated不显著；Popular交互项β=0.338边际显著，高人气子样本β=0.493显著，低人气子样本β=-0.157显著负。

- argumentative_role_cn：即兴能力调节效应符合System 1/即兴理论，进一步支持由主播即兴驱动的机制解释。

- remaining_uncertainty_cn：主播评分和粉丝数都不是直接测量即兴能力；低人气主播负效应提示实时数据对部分主播可能有干扰。

- link_to_next_phase_cn：在机制和边界证据之后，需要通过多种反事实检验排除替代解释和溢出。

##### evidence_pointers

1. Table 8 Heterogeneity by Streamer Rating

2. Appendix D Table D2 Heterogeneity by Streamer Popularity

#### 5. 反事实检验、溢出与竞争检验

- order：5

- name_cn：反事实检验、溢出与竞争检验

- question_cn：总效应是否确实由使用实时仪表盘驱动？是否存在对非预售商品的替代或溢出？是否存在跨组竞争混淆？

- inputs_and_setting_cn：仪表盘使用次数为零的处理组子样本；非预售商品样本；同一直播流中常规商品比例高低；浏览量和访问量的组间t检验。

- designed_or_compared_object_cn：比较未使用仪表盘的主播处理效应、非预售商品处理效应、高常规商品比例的调节效应，以及处理与控制组的浏览量和访问量。

- baseline_control_or_counterfactual_cn：未使用仪表盘的反事实、非预售商品的溢出反事实、常规商品比例作为干扰反事实、浏览量和访问量作为市场关注度反事实。

##### objective_metrics

1. 仪表盘使用=0子样本Treatment系数

2. 非预售商品Treatment系数

3. Treatment × High Non-Presale %系数

4. 浏览量、访问量组间p值

- analysis_method_cn：对子样本重估主方程；常规商品比例做调节回归；对浏览量访问量做t检验。

- main_result_cn：未使用仪表盘子样本效应不显著；非预售商品无显著差异；常规商品比例交互不显著；浏览量和访问量组间无显著差异。

- argumentative_role_cn：排除‘仅分配访问权但未使用’就有效、挤出常规商品、常规商品干扰以及实验前流量差异等替代解释，把效应锚定在主播临场行为上。

- remaining_uncertainty_cn：这些检验是排除性证据，不能正面证明主播认知过程；仍需排除价格调整等其他机制。

- link_to_next_phase_cn：价格调整是最直接的竞争性机制，因此专门用行业规则、访谈和关键词频率排除它。

##### evidence_pointers

1. Table 9 Falsification Tests

2. Additional Analyses第三段关于views和visits的t检验

#### 6. 替代机制：价格调整检验

- order：6

- name_cn：替代机制：价格调整检验

- question_cn：销量提高是否由主播在直播中临时改价或促销驱动，而不是即兴销售战术？

- inputs_and_setting_cn：主播与平台/商家访谈（Appendix B）；语音脚本中价格调整关键词频率；PROCESS模型中加入Pricing Adjustment作为替代中介。

- designed_or_compared_object_cn：比较价格调整关键词频率与推荐、催促、预售信息、库存信息等战术关键词频率；比较处理组和控制组价格调整关键词；测试价格调整的中介路径。

- baseline_control_or_counterfactual_cn：基于访谈的行业规则表明价格是预先锁定的参数；控制组作为关键词频率基线。

##### objective_metrics

1. 价格调整关键词频率

2. Treatment到Pricing Adjustment的路径系数

3. Pricing Adjustment到Sales的间接效应及其95%CI

- analysis_method_cn：描述性频率比较、组间t检验、PROCESS中介模型。

- main_result_cn：价格调整关键词频率极低（M=0.0005），远低于其他战术；组间差异不显著；价格调整的中介路径不显著。

- argumentative_role_cn：排除价格渠道，使“即兴销售战术”成为最可行的机制解释。

- remaining_uncertainty_cn：价格不可调整是基于该平台和访谈证据的行业惯例，其他直播情境可能不同。

- link_to_next_phase_cn：最后把实时数据与历史需求记录对比，说明实时数据的独特价值并引出讨论。

##### evidence_pointers

1. Table 10 Pricing Adjustment Keywords

2. Alternative Mechanism段落

3. Appendix B Expert Interviews

#### 7. 与历史需求记录的比较分析

- order：7

- name_cn：与历史需求记录的比较分析

- question_cn：实时销售数据的效果是否独立于历史需求记录？在缺乏历史记录时是否更有价值？

- inputs_and_setting_cn：预售商品是否在实验前一个月内有历史销售记录（Historical Records变量），作为是否具有历史需求知识的代理。

- designed_or_compared_object_cn：比较有历史记录与无历史记录的预售商品对处理效应的调节。

- baseline_control_or_counterfactual_cn：有历史记录商品作为低不确定性基线，无历史记录商品作为高不确定性条件。

##### objective_metrics

1. Treatment × Historical Records交互项

2. 有/无历史记录子样本Treatment系数

- analysis_method_cn：交互项回归和子样本回归。

- main_result_cn：交互项β=-0.409不显著，但子样本中无历史记录组效应显著（β=0.574），有历史记录组不显著（β=0.022），两组系数差异边际显著（p<0.1）。

- argumentative_role_cn：提供初步证据说明实时数据在缺乏历史数据时更有价值，同时作者也承认结果混合、历史记录是内生变量，因此没有作出强因果结论。

- remaining_uncertainty_cn：历史记录变量内生；交互作用未达到常规显著水平，只能作为方向性证据。

- link_to_next_phase_cn：讨论部分用这一对比强调实时数据与历史数据的不同决策功能，并把结论拉回即兴理论和System 1。

##### evidence_pointers

1. Table 11 Interaction Effect by Historical Demand Records

2. Comparing Real-Time Sales Data to Historical Demand Records段落

## 各部分修辞架构

### abstract_moves

1. 建立直播带货的快速互动与现实任务复杂性背景

2. 提出研究问题：实时销售数据对即兴决策和销售结果的影响

3. 呈现竞争性预测：可能加剧认知负荷，也可能帮助即兴

4. 交代随机现场实验设计与处理/控制对照

5. 报告主效应、机制战术、异质性结果

6. 声明对数据驱动决策文献的贡献

### introduction_moves

1. 用市场规模和行业预测说明直播带货的重要性

2. 对比直播带货与传统电商、电视购物，强调即兴必要性

3. 指出历史数据对计划决策的作用及在直播场景中的局限

4. 区分实时数据与历史数据，说明实时数据适合即兴场景

5. 构造未解决问题的Gap和竞争性预测

6. 提出RQ1-RQ3

7. 介绍平台合作随机现场实验和预售商品情境

8. 预告主效应、机制和边界条件的核心结果

9. 从数据驱动决策和直播平台两个文献声明贡献

10. 给出对平台、商家和主播的实践含义

### theory_and_knowledge_moves

1. 梳理数据驱动决策文献并限定缺口为实时数据对即兴决策的作用

2. 引入System 1/System 2区分实时数据与历史数据的认知路径

3. 分类直播带货文献并指出IT制品设计支持的空白

4. 引入即兴理论定义和两个关键要素：自发行动与直觉

5. 指出现有即兴理论多依赖物理观众反馈，直播场景缺乏这种反馈

6. 推导实时销售数据作为观众的替代反馈可以促进即兴

7. 同时提出过载与分心的反向机制，形成可检验张力

### artifact_design_moves

1. 说明仪表盘原先只对非预售商品开放，扩展到预售商品形成实验机会

2. 描述实验时间、随机化规则、处理与控制仪表盘差异

3. 强调每个商品只在一个组销售以避免污染

4. 说明数据层级：流-商品、流、主播

5. 报告随机化检查结果

### evaluation_moves

1. 用流-商品层面OLS加固定效应估计主效应

2. 以控制组战术为基准，从ASR脚本提取战术指标进行多中介分析

3. 用产品不确定性和主播评分/人气异质性提供机制佐证

4. 用未使用仪表盘、非预售商品、常规商品比例、浏览量访问量做反事实检验

5. 用价格调整关键词和行业访谈排除替代机制

6. 用历史需求记录交互比较实时数据的独特价值

### discussion_and_contribution_moves

1. 重述主发现和机制

2. 把结果提升为实时数据在紧急情境中通过System 1即兴起作用的理论贡献

3. 把IT仪表盘定位为直播平台设计研究的新现象

4. 把即兴理论扩展到无物理观众反馈的线上环境

5. 给出平台投资、分群体适配和培训建议

6. 列出短期窗口、价格灵活性、engagement缺失、呈现格式等限制与未来研究

## 理论/知识到设计的翻译

### 知识/理论基础

1. 即兴理论（jazz improvisation metaphor）

2. System 1/System 2双系统理论

3. 数据驱动决策文献

4. 直播带货平台文献

5. 销售管理中的自适应销售与说服研究

- 理论—设计耦合：partial

- 耦合判定理由：即兴理论解释了为什么实时销售数据可能有效以及何时更有效，也指导了销售战术分类和边界条件选择；但实时销售数据仪表盘本身不是由理论推导出来的新制品，而是平台已经存在并扩展到预售商品的功能，作者利用这一现场设计检验理论预期。

- 理论到设计翻译链：即兴理论认为有效即兴需要观众/环境反馈，而直播主播缺乏物理观众反馈 → 实时销售数据可作为需求反馈信号 → 主播端仪表盘向处理组展示预售商品定金和尾款数据 → 主播基于数据自发调整促销、语言和节奏战术 → 处理组相对控制组销量提高40.21%；同时理论预测不确定性越高、即兴能力越强，效果越明显 → 产品类型和主播评分/人气异质性证实边界条件。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：即兴是面对不确定性和时间压力时，计划与执行同时发生的自发行动；有效即兴依赖对环境的实时反馈。

- mechanism_cn：在直播中缺少物理观众反馈，实时销售数据可模拟观众反应，让主播监控当前需求并快速调整策略。

- design_requirement_cn：需要在主播决策的同一时空提供商品维度的实时销售反馈。

- artifact_choice_cn：主播端仪表盘在预售商品下显示“总定金”和“总尾款”列，每5秒更新。

- evaluated_contrast_cn：处理组可见预售实时销售数据 vs 控制组不可见。

- objective_result_cn：处理组预售商品销量增加40.21%。

##### evidence_pointers

1. Table 4 Estimation of Main Effect

2. Experimental Design段落

#### 2. 2

- theory_or_knowledge_claim_cn：System 1决策依赖直觉和启发式，适用于快速、高压和不确定环境；即兴行为是描述性决策过程。

- mechanism_cn：实时数据被用于快速、自发地调整销售战术，而非深思熟虑分析；表现为催促下单、情感表达、语速和时长的即时改变。

- design_requirement_cn：数据需要可被快速阅读并与单个商品绑定，以便主播立即调整话术和节奏。

- artifact_choice_cn：仪表盘按商品显示实时销售数据而非复杂分析报表。

- evaluated_contrast_cn：处理组和控制组在音频转写战术指标上的差异。

- objective_result_cn：催促、情感词、语速、单品时长四类战术的间接效应显著。

##### evidence_pointers

1. Figure 3 Multiple Mediation Analyses

2. Table 6 Direct and Indirect Effects

#### 3. 3

- theory_or_knowledge_claim_cn：不确定性越高，越需要即兴；缺乏品牌或历史信息会增加产品不确定性。

- mechanism_cn：小商家商品和经验品缺少既定品牌叙事，主播无法依赖已有知识，因此更依赖实时数据判断需求并调整策略。

- design_requirement_cn：实时数据工具对高不确定产品应被优先使用或强调。

- artifact_choice_cn：无新增制品，但分析聚焦品牌店vs小商家、经验品vs搜索品。

- evaluated_contrast_cn：Treatment × Brand-Owned、Treatment × Experience Good交互。

- objective_result_cn：小商家商品效应显著为0.836，品牌店交互显著为负；经验品交互显著为正。

##### evidence_pointers

1. Table 7 Heterogeneity by Brand-Owned Products

2. Appendix D Table D1

#### 4. 4

- theory_or_knowledge_claim_cn：即兴能力是有效即兴的必要条件；专家可以通过直觉和训练快速处理信息。

- mechanism_cn：高评分或高人气主播更有经验和能力同步监控实时数据并调整话术，低技能主播可能因分心而受损。

- design_requirement_cn：平台应对主播的即兴能力进行区分，为低技能主播提供培训或适应机制。

- artifact_choice_cn：仪表盘本身不按能力差异化，但异质性分析揭示需要差异化支持。

- evaluated_contrast_cn：Treatment × Top-Rated Streamer、Treatment × Popular Streamer交互。

- objective_result_cn：高评分和高人气主播效应显著，低人气主播甚至出现负效应。

##### evidence_pointers

1. Table 8 Heterogeneity by Streamer Rating

2. Appendix D Table D2

#### 5. 5

- theory_or_knowledge_claim_cn：如果销量提升来自价格促销而非战术即兴，则机制解释无效；直播行业价格通常是预先锁定的。

- mechanism_cn：主播不能在直播中临时改价，因此价格不是实时数据作用的渠道。

- design_requirement_cn：实验分析需要排除价格调整替代解释。

- artifact_choice_cn：不涉及新设计；用关键词频率和访谈证据排除。

- evaluated_contrast_cn：价格调整关键词频率与其他战术对比；组间差异；中介路径。

- objective_result_cn：价格调整关键词极低、组间不显著、中介路径不显著。

##### evidence_pointers

1. Table 10 Pricing Adjustment Keywords

2. Alternative Mechanism段落

3. Appendix B

## 评价逻辑

### evaluation_modes

1. 平台随机现场实验

2. 流-商品层面回归加固定效应

3. 基于ASR转写和LIWC的多中介分析

4. 异质性/子样本分析

5. 多重反事实与溢出检验

6. 替代机制排除

7. 与历史需求记录的交互比较

- why_these_evaluations_cn：随机实验提供因果总效应；主效应只回答“是否有效”，需要中介分析回答“如何起作用”，需要用即兴理论要求的不确定性和能力两个边界条件回答“何时更有效”，最后用反事实检验、溢出检验和价格替代机制排除竞争性解释，从而把结果上升为理论机制。

- benchmark_and_contrast_chain_cn：控制组作为无实时预售数据的基准；销售战术以控制组为基准识别处理组即兴差异；品牌店/搜索品/有历史记录/非Top-rated作为低不确定性或低能力基准；未使用仪表盘、非预售商品和浏览量访问量作为反事实基准；价格关键词频率与其他战术对比作为替代机制基准。多组对照逐层排除替代解释。

### claim_evidence_ledger

#### 1. 实时销售数据提供使预售商品销量增加40.21%。

- claim_cn：实时销售数据提供使预售商品销量增加40.21%。

- evidence_cn：随机现场实验处理组/控制组对比，流-商品级回归，β=0.338，p<0.05。

- assessment_cn：由随机设计和固定效应支持，因果可信度较高。

#### 2. 效应由主播销售战术的即兴变化驱动。

- claim_cn：效应由主播销售战术的即兴变化驱动。

- evidence_cn：PROCESS中介分析显示催促、情感词、语速、单品时长四条间接路径显著。

- assessment_cn：中介战术来自实际直播语音文本，但“即兴”本身未被直接观测，属于行为代理。

#### 3. 产品不确定性越高，实时数据越有效。

- claim_cn：产品不确定性越高，实时数据越有效。

- evidence_cn：品牌店交互显著为负、小商家子样本显著；经验品交互显著为正。

- assessment_cn：与即兴理论一致，但产品类型是代理变量。

#### 4. 主播即兴能力越强，实时数据越有效。

- claim_cn：主播即兴能力越强，实时数据越有效。

- evidence_cn：Top-rated交互显著，高人气交互边际显著；低人气子样本负效应。

- assessment_cn：与System 1/专家直觉一致，但评分和粉丝数是间接代理。

#### 5. 效应不是来自不使用仪表盘、非预售溢出或跨组流量竞争。

- claim_cn：效应不是来自不使用仪表盘、非预售溢出或跨组流量竞争。

- evidence_cn：未使用仪表盘子样本效应不显著；非预售无差异；常规产品比例交互不显著；浏览量访问量无组间差异。

- assessment_cn：反事实检验支持行为渠道解释。

#### 6. 价格调整不是替代机制。

- claim_cn：价格调整不是替代机制。

- evidence_cn：价格调整关键词频率极低、组间无差异、中介路径不显著；访谈确认价格预先锁定。

- assessment_cn：证据充分，但依赖该平台行业惯例。

#### 7. 实时数据在无历史记录时更有价值。

- claim_cn：实时数据在无历史记录时更有价值。

- evidence_cn：无历史记录子样本显著，有历史记录子样本不显著，但交互项不显著。

- assessment_cn：作者承认证据混合，未做强烈结论，仅作方向性支持。

- internal_validity_strategy_cn：依靠平台随机分配（账号尾号），先做随机化检查；每个商品只在一个组销售防止跨组污染；用固定效应控制流媒体类、产品类、日期和时段；用未使用仪表盘、非预售、常规比例和浏览量访问量进行反事实与溢出检验；用行业访谈和关键词排除价格替代机制。

- external_validity_strategy_cn：使用真实大型直播平台和真实主播/商品；与多个平台（淘宝直播、抖音、快手）的主播和平台高管访谈确认做法；通过产品不确定性、主播能力、历史记录等异质性展示条件边界；但也承认短期实验、特定预售商品、特定平台制度可能限制推广。

- what_is_not_actually_tested_cn：未直接测量主播的即兴认知意图或心理过程；未操纵仪表盘的呈现格式；未测量消费者参与度/engagement；未观察长期效果；主播即兴能力只用评分、人气等代理；价格不可调整性是行业制度而非实验操纵；历史记录的调节证据较弱。

## 贡献闭环

- technical_claim_cn：实时销售数据仪表盘对预售商品开放是一种有效的平台数据分析工具，使处理组销量提高约40.21%。

- artifact_claim_cn：可识别设计部分是主播仪表盘中实时展示预售商品的定金和尾款数据；使用该仪表盘的组效果显著，未使用者无效果。

- mechanism_claim_cn：机制是主播数据驱动的即兴：更多催促下单、更多情感词、更快语速和更短单品时长，这些战术中介了销售提升。

- boundary_claim_cn：效应在产品不确定性更高（小商家、经验品）和主播即兴能力更强（高评分、高人气）时更显著；低人气主播甚至可能因实时数据受损。

- reusable_design_knowledge_cn：实时数据基础设施的价值不在于提供更多历史统计，而在于为临场决策者提供与当前行动同步的反馈信号；平台需要根据用户技能和产品不确定性差异化部署并配套培训。

- theoretical_contribution_cn：将数据驱动决策文献从历史数据/计划决策扩展到实时数据/即兴决策，用System 1说明实时数据在高速环境中的认知路径；将即兴理论从有物理观众反馈的场景扩展到无物理观众反馈的在线直播场景，提出实时数据可替代观众反馈。

- how_discussion_closes_intro_gap_cn：讨论部分直接回应引言中‘历史数据难以应对直播临场决策’的缺口，用40.21%主效应、四条中介战术和两个边界条件证明实时数据确实通过即兴而非计划决策提升绩效，并通过与历史需求记录的对比说明实时数据的独特价值。

- overclaim_or_unsupported_leaps_cn：中介分析中的战术差异被解释为即兴，但文本中没有直接测量即兴意图；产品类型和主播评分代理了不确定性和能力，但并非完美代理；历史记录交互不显著却被讨论用于强调实时数据独特价值，作者对此有保留；搜索品负效应在正文未展开，只在附录披露。

## 句级写作动作图谱

### 1. Abstract P1 S1

- order：1

- section：Abstract

- locator：Abstract P1 S1

- move_code：CONTEXT

- paraphrase_cn：直播带货已经成为高互动、快节奏和大规模观众场景下的新型电商形式。

- rhetorical_function_cn：开门见山给出研究对象和场景。

- depends_on_cn：无。

- sets_up_cn：为后文说明主播任务复杂性和实时数据价值建立场景。

- evidence_pointer：Abstract第一句

### 2. Abstract P1 S2

- order：2

- section：Abstract

- locator：Abstract P1 S2

- move_code：PHENOMENON

- paraphrase_cn：主播必须同时展示商品、与观众互动、使用销售技巧，并面对无法预知观众反应和时间压力。

- rhetorical_function_cn：指出实时直播中的核心现象性困难。

- depends_on_cn：依赖直播带货背景。

- sets_up_cn：为即兴决策和实时数据需求铺垫。

- evidence_pointer：Abstract第二句

### 3. Abstract P2 S1

- order：3

- section：Abstract

- locator：Abstract P2 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文研究实时销售数据在影响主播即兴决策和销售结果中的作用。

- rhetorical_function_cn：在摘要中直接给出研究目标。

- depends_on_cn：前两句的现实问题。

- sets_up_cn：引出后文竞争性预测和实验证据。

- evidence_pointer：Abstract P2

### 4. Abstract P2 S2-S3

- order：4

- section：Abstract

- locator：Abstract P2 S2-S3

- move_code：GAP

- paraphrase_cn：实时销售数据可能加重决策复杂性导致过载分心，也可能帮助主播即兴并高效利用时间。

- rhetorical_function_cn：呈现竞争性预测，说明研究问题尚未解决。

- depends_on_cn：研究目标。

- sets_up_cn：为随机实验的必要性做准备。

- evidence_pointer：Abstract P2

### 5. Abstract P3 S1

- order：5

- section：Abstract

- locator：Abstract P3 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：作者与领先直播平台合作，分析随机现场实验数据，处理组可看预售实时销售数据，控制组不可看。

- rhetorical_function_cn：预告实证设计。

- depends_on_cn：竞争性预测需要因果证据。

- sets_up_cn：为报告结果做铺垫。

- evidence_pointer：Abstract P3

### 6. Abstract P4 S1

- order：6

- section：Abstract

- locator：Abstract P4 S1

- move_code：RESULT

- paraphrase_cn：处理组预售商品销量比控制组增加约40.21%。

- rhetorical_function_cn：报告最重要的主效应。

- depends_on_cn：实验设计。

- sets_up_cn：后续机制和边界条件围绕该主效应展开。

- evidence_pointer：Abstract P4

### 7. Abstract P4 S2

- order：7

- section：Abstract

- locator：Abstract P4 S2

- move_code：RESULT

- paraphrase_cn：主效应可由主播在促销、语言和呈现节奏上的数据驱动即兴来解释。

- rhetorical_function_cn：预告机制答案。

- depends_on_cn：主效应。

- sets_up_cn：暗示后续销售战术中介分析。

- evidence_pointer：Abstract P4

### 8. Abstract P4 S3

- order：8

- section：Abstract

- locator：Abstract P4 S3

- move_code：RESULT

- paraphrase_cn：异质性分析显示，对即兴技巧更好的主播和不确定性更高的产品效果更强。

- rhetorical_function_cn：报告边界条件，强化机制解释。

- depends_on_cn：机制即兴。

- sets_up_cn：为理论贡献提供支撑。

- evidence_pointer：Abstract P4

### 9. Abstract P5 S1

- order：9

- section：Abstract

- locator：Abstract P5 S1

- move_code：CONTRIBUTION

- paraphrase_cn：本文对数据驱动决策文献作出贡献，强调实时数据对决策过程和结果的重要性。

- rhetorical_function_cn：在摘要中声明理论贡献。

- depends_on_cn：全部结果。

- sets_up_cn：为平台实践含义做铺垫。

- evidence_pointer：Abstract P5

### 10. Introduction P1 S1-S3

- order：10

- section：Introduction

- locator：Introduction P1 S1-S3

- move_code：PRACTICAL_STAKES

- paraphrase_cn：美国和中国直播带货市场规模预期快速增长，被视为电商革命。

- rhetorical_function_cn：用市场数据说明问题的重要性。

- depends_on_cn：无。

- sets_up_cn：把学术研究锚定在重大商业现象上。

- evidence_pointer：Introduction第一段

### 11. Introduction P2 S1-S3

- order：11

- section：Introduction

- locator：Introduction P2 S1-S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：与依赖文本图片的传统电商和预录脚本的电视购物相比，直播带货需要实时视频和主播-观众互动。

- rhetorical_function_cn：对比界定直播带货的独特性。

- depends_on_cn：市场背景。

- sets_up_cn：引出主播需要在不可预见情况下即兴表演。

- evidence_pointer：Introduction第二段

### 12. Introduction P2 S4

- order：12

- section：Introduction

- locator：Introduction P2 S4

- move_code：PHENOMENON

- paraphrase_cn：直播带货要求主播实时应对大规模观众、边走边演。

- rhetorical_function_cn：指出核心经验现象。

- depends_on_cn：直播与电视购物的对比。

- sets_up_cn：为即兴理论和实时数据价值铺垫。

- evidence_pointer：Introduction P2最后一句

### 13. Introduction P3 S1

- order：13

- section：Introduction

- locator：Introduction P3 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：已有研究表明历史数据有助于计划性决策。

- rhetorical_function_cn：概括现有数据驱动决策文献。

- depends_on_cn：无。

- sets_up_cn：随后指出历史数据在直播临场决策中的局限。

- evidence_pointer：Introduction P3 S1

### 14. Introduction P3 S2

- order：14

- section：Introduction

- locator：Introduction P3 S2

- move_code：LIMITATION

- paraphrase_cn：直播的快速、复杂和不确定性限制了历史记录在实时决策中的用处。

- rhetorical_function_cn：指出现有知识的边界。

- depends_on_cn：已有历史数据研究。

- sets_up_cn：为实时数据作为替代资源提供动机。

- evidence_pointer：Introduction P3 S2

### 15. Introduction P3 S3-S5

- order：15

- section：Introduction

- locator：Introduction P3 S3-S5

- move_code：PHENOMENON

- paraphrase_cn：主播需要同时展示商品、回应询问和完成交易，观众行为难以预测，且必须在有限时间内完成推介。

- rhetorical_function_cn：用具体任务说明直播中的多任务、不确定性和时间压力。

- depends_on_cn：历史数据局限。

- sets_up_cn：说明为什么需要针对实时数据的新研究。

- evidence_pointer：Introduction P3后三句

### 16. Introduction P4 S1

- order：16

- section：Introduction

- locator：Introduction P4 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本研究旨在理解实时销售数据在直播带货中的价值。

- rhetorical_function_cn：宣布研究目标。

- depends_on_cn：前段现象。

- sets_up_cn：定义实时销售数据并连接仪表盘设计。

- evidence_pointer：Introduction P4 S1

### 17. Introduction P4 S2-S4

- order：17

- section：Introduction

- locator：Introduction P4 S2-S4

- move_code：CONTEXT

- paraphrase_cn：实时销售数据指生成和处理时同步可用的交易数据，在直播中可显示在主播仪表盘上，区别于描述过去事件的历史数据。

- rhetorical_function_cn：给出核心概念的操作定义。

- depends_on_cn：研究目标。

- sets_up_cn：为实验中的仪表盘设计作铺垫。

- evidence_pointer：Introduction P4

### 18. Introduction P5 S1

- order：18

- section：Introduction

- locator：Introduction P5 S1

- move_code：GAP

- paraphrase_cn：目前尚不清楚实时销售数据是否以及如何影响主播行为和销售业绩。

- rhetorical_function_cn：明确研究缺口。

- depends_on_cn：实时数据概念界定。

- sets_up_cn：引出竞争性预测和研究问题。

- evidence_pointer：Introduction P5 S1

### 19. Introduction P5 S2

- order：19

- section：Introduction

- locator：Introduction P5 S2

- move_code：LIMITATION

- paraphrase_cn：处理实时数据可能耗尽认知资源导致过载和分心，主播可能忽略数据而沿用旧经验。

- rhetorical_function_cn：提出不利方向的机制。

- depends_on_cn：缺口。

- sets_up_cn：与有利方向形成竞争性假设。

- evidence_pointer：Introduction P5 S2

### 20. Introduction P5 S3

- order：20

- section：Introduction

- locator：Introduction P5 S3

- move_code：MECHANISM

- paraphrase_cn：实时销售数据也可能帮助主播做出知情决策、即兴调整活动并更有效利用时间。

- rhetorical_function_cn：提出有利方向的机制。

- depends_on_cn：缺口。

- sets_up_cn：引出研究问题RQ1-RQ3。

- evidence_pointer：Introduction P5 S3

### 21. Introduction P5 S4

- order：21

- section：Introduction

- locator：Introduction P5 S4

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：作者提出三个研究问题：实时数据是否影响绩效、主播使用哪些即兴战术、边界条件是什么。

- rhetorical_function_cn：将竞争性预测转化为具体研究问题。

- depends_on_cn：前句两种机制。

- sets_up_cn：统领全文实证策略。

- evidence_pointer：Introduction P5末尾

### 22. Introduction P6 S1-S2

- order：22

- section：Introduction

- locator：Introduction P6 S1-S2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：作者与淘宝直播合作，利用2020年12月1日至3日的随机现场实验评估对预售商品提供实时销售数据的效果。

- rhetorical_function_cn：介绍实证设计。

- depends_on_cn：研究问题。

- sets_up_cn：说明为什么选择预售商品。

- evidence_pointer：Introduction P6

### 23. Introduction P6 S3

- order：23

- section：Introduction

- locator：Introduction P6 S3

- move_code：CONTEXT

- paraphrase_cn：预售商品是消费者在产量确定前订购的新品，订单在未来日期履约。

- rhetorical_function_cn：界定研究对象。

- depends_on_cn：实验介绍。

- sets_up_cn：解释预售商品缺乏历史数据的特点。

- evidence_pointer：Introduction P6 S3

### 24. Introduction P6 S4

- order：24

- section：Introduction

- locator：Introduction P6 S4

- move_code：CONTEXT

- paraphrase_cn：预售商品通常缺乏历史数据和消费者评价，实时销售数据可以帮助主播测度兴趣和商家评估需求。

- rhetorical_function_cn：说明实验情境的理论和实践价值。

- depends_on_cn：预售商品定义。

- sets_up_cn：为主效应预期提供背景。

- evidence_pointer：Introduction P6最后一句

### 25. Introduction P7 S1

- order：25

- section：Introduction

- locator：Introduction P7 S1

- move_code：RESULT

- paraphrase_cn：处理组预售商品销量显著增加约40.21%。

- rhetorical_function_cn：在引言中预告总效应。

- depends_on_cn：实验设计。

- sets_up_cn：随后概述机制和边界结果。

- evidence_pointer：Introduction P7

### 26. Introduction P7 S2

- order：26

- section：Introduction

- locator：Introduction P7 S2

- move_code：RESULT

- paraphrase_cn：机制分析显示实时数据通过影响主播即兴销售战术提高销量，包括催促、情感词、语速和缩短单品时间。

- rhetorical_function_cn：预告机制结果。

- depends_on_cn：主效应。

- sets_up_cn：为中介分析章节做预告。

- evidence_pointer：Introduction P7 S2

### 27. Introduction P7 S3

- order：27

- section：Introduction

- locator：Introduction P7 S3

- move_code：RESULT

- paraphrase_cn：边界条件显示效应在高不确定性产品和更有即兴技巧的主播中更显著。

- rhetorical_function_cn：预告异质性结果。

- depends_on_cn：机制即兴。

- sets_up_cn：为异质性分析章节做预告。

- evidence_pointer：Introduction P7 S3

### 28. Introduction P8 S1-S2

- order：28

- section：Introduction

- locator：Introduction P8 S1-S2

- move_code：CONTRIBUTION

- paraphrase_cn：本文是首批实证研究实时数据如何在紧急快节奏环境中促成即兴决策的论文之一。

- rhetorical_function_cn：声明对数据驱动决策文献的贡献。

- depends_on_cn：全部结果。

- sets_up_cn：为文献综述奠定贡献定位。

- evidence_pointer：Introduction P8

### 29. Introduction P9 S1-S2

- order：29

- section：Introduction

- locator：Introduction P9 S1-S2

- move_code：CONTRIBUTION

- paraphrase_cn：本文通过主播端仪表盘提供实时数据这一IT制品设计，为直播带货平台研究作出贡献。

- rhetorical_function_cn：声明对直播平台文献的贡献。

- depends_on_cn：前一条贡献。

- sets_up_cn：为实践意义提供框架。

- evidence_pointer：Introduction P9

### 30. Data-Driven Decision-Making P1 S1-S3

- order：30

- section：Literature Review

- locator：Data-Driven Decision-Making P1 S1-S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：数据驱动决策文献主要研究各类分析工具对决策的影响，如HR评分可视化、零售描述性仪表盘和评分直方图。

- rhetorical_function_cn：系统梳理已有研究。

- depends_on_cn：引言贡献声明。

- sets_up_cn：为指出实时数据缺口提供文献基础。

- evidence_pointer：Data-Driven Decision-Making第一段

### 31. Data-Driven Decision-Making P2 S1

- order：31

- section：Literature Review

- locator：Data-Driven Decision-Making P2 S1

- move_code：GAP

- paraphrase_cn：对实时数据如何影响即兴决策及其结果的研究有限。

- rhetorical_function_cn：明确提出文献缺口。

- depends_on_cn：已有历史数据研究。

- sets_up_cn：引出实时数据区别于历史数据的论证。

- evidence_pointer：Data-Driven Decision-Making P2 S1

### 32. Data-Driven Decision-Making P2 S2-S5

- order：32

- section：Literature Review

- locator：Data-Driven Decision-Making P2 S2-S5

- move_code：THEORY_INTRO

- paraphrase_cn：历史数据适合System 2式的深思熟虑，实时数据适合System 1式的快速直觉判断。

- rhetorical_function_cn：引入双系统理论解释实时数据的不同认知路径。

- depends_on_cn：缺口。

- sets_up_cn：为即兴理论作理论铺垫。

- evidence_pointer：Data-Driven Decision-Making P2

### 33. Data-Driven Decision-Making P3 S1-S2

- order：33

- section：Literature Review

- locator：Data-Driven Decision-Making P3 S1-S2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：直播中的实时决策主要是System 1思维，强调快速自动直觉过程。

- rhetorical_function_cn：把双系统理论应用到直播场景。

- depends_on_cn：System 1/2区分。

- sets_up_cn：为实时数据促进即兴的假设埋下伏笔。

- evidence_pointer：Data-Driven Decision-Making P3

### 34. Live Stream Selling Platforms P1 S1

- order：34

- section：Literature Review

- locator：Live Stream Selling Platforms P1 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：直播带货文献可分为特征与价值、结果影响因素、卖家与主播策略三类。

- rhetorical_function_cn：建立文献分类框架。

- depends_on_cn：文献综述开始。

- sets_up_cn：定位本文在第二类文献中的位置。

- evidence_pointer：Live Stream Selling Platforms第一段

### 35. Live Stream Selling Platforms P4 S1

- order：35

- section：Literature Review

- locator：Live Stream Selling Platforms P4 S1

- move_code：GAP

- paraphrase_cn：现有研究尚未探索IT制品设计如何支持主播临场决策，本文填补该空白。

- rhetorical_function_cn：明确直播文献中的空白。

- depends_on_cn：三类文献分类。

- sets_up_cn：把贡献定位为IT制品设计研究。

- evidence_pointer：Live Stream Selling Platforms最后一段

### 36. Improvisation Theory P1 S1-S2

- order：36

- section：Literature Review

- locator：Improvisation Theory P1 S1-S2

- move_code：THEORY_INTRO

- paraphrase_cn：即兴理论源于爵士乐表演，解释个体在不确定和时间压力下如何适应与表现。

- rhetorical_function_cn：引入即兴理论核心定义。

- depends_on_cn：前文实时决策需要。

- sets_up_cn：为直播即兴机制提供理论基础。

- evidence_pointer：Improvisation Theory第一段

### 37. Improvisation Theory P2 S1-S3

- order：37

- section：Literature Review

- locator：Improvisation Theory P2 S1-S3

- move_code：THEORY_PROPOSITION

- paraphrase_cn：有效即兴包含两个要素：自发思考和行动，以及运用直觉；这是一个描述性决策过程。

- rhetorical_function_cn：给出即兴的行为要素。

- depends_on_cn：即兴理论定义。

- sets_up_cn：为后续销售战术测量提供理论依据。

- evidence_pointer：Improvisation Theory第二段

### 38. Improvisation Theory P3 S3

- order：38

- section：Literature Review

- locator：Improvisation Theory P3 S3

- move_code：GAP

- paraphrase_cn：直播带货缺乏物理观众存在，阻碍主播有效即兴；本文扩展即兴理论到该场景。

- rhetorical_function_cn：指出现有即兴理论的场景局限。

- depends_on_cn：即兴理论依赖观众反馈。

- sets_up_cn：引出实时数据作为观众反馈替代的核心假设。

- evidence_pointer：Improvisation Theory最后一句

### 39. Real-Time Sales Data Enables Improvisation P1 S1

- order：39

- section：Literature Review

- locator：Real-Time Sales Data Enables Improvisation P1 S1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：综合即兴理论、直播带货和销售管理，实时销售数据既可能有利于也可能损害主播即兴战术。

- rhetorical_function_cn：综合文献并建立竞争性理论主张。

- depends_on_cn：即兴理论、直播文献、销售管理。

- sets_up_cn：随后分别展开正反机制。

- evidence_pointer：Real-Time Sales Data Enables Improvisation第一段

### 40. Real-Time Sales Data Enables Improvisation P2 S2

- order：40

- section：Literature Review

- locator：Real-Time Sales Data Enables Improvisation P2 S2

- move_code：MECHANISM

- paraphrase_cn：没有实时数据时，主播可能依赖旧经验或历史记录，导致即兴时的次优或错误决策。

- rhetorical_function_cn：说明实时数据提供及时反馈的有利机制。

- depends_on_cn：即兴需要反馈。

- sets_up_cn：为处理组战术变化做铺垫。

- evidence_pointer：Real-Time Sales Data P2

### 41. Real-Time Sales Data Enables Improvisation P3 S1-S2

- order：41

- section：Literature Review

- locator：Real-Time Sales Data Enables Improvisation P3 S1-S2

- move_code：MECHANISM

- paraphrase_cn：处理实时数据可能因认知资源限制或注意力冲突造成信息过载，干扰主播。

- rhetorical_function_cn：提出反向机制。

- depends_on_cn：竞争性理论主张。

- sets_up_cn：为随机实验的必要性提供理论张力。

- evidence_pointer：Real-Time Sales Data P3

### 42. Real-Time Sales Data Enables Improvisation P3 S3

- order：42

- section：Literature Review

- locator：Real-Time Sales Data Enables Improvisation P3 S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：作者基于竞争视角提出实证检验实时数据在即兴和销售中的作用。

- rhetorical_function_cn：结束理论部分并回到实证目标。

- depends_on_cn：正反机制。

- sets_up_cn：进入随机现场实验章节。

- evidence_pointer：Real-Time Sales Data最后一句

### 43. Research Context P1 S3-S4

- order：43

- section：Randomized Field Experiment

- locator：Research Context P1 S3-S4

- move_code：CONTEXT

- paraphrase_cn：平台仪表盘原本只显示常规商品实时数据，后来扩展到预售商品，形成实验机会。

- rhetorical_function_cn：说明实验的自然平台背景。

- depends_on_cn：理论预测。

- sets_up_cn：为随机设计提供现实依据。

- evidence_pointer：Research Context

### 44. Experimental Design P1 S2-S4

- order：44

- section：Randomized Field Experiment

- locator：Experimental Design P1 S2-S4

- move_code：DESIGN_FEATURE

- paraphrase_cn：实验将预售实时数据扩展到随机分配的处理组；处理组能看到预售商品定金与尾款列，控制组不能。

- rhetorical_function_cn：描述处理的具体设计。

- depends_on_cn：平台仪表盘背景。

- sets_up_cn：为变量定义和因果识别提供依据。

- evidence_pointer：Experimental Design第一段

### 45. Experimental Design P1 S5

- order：45

- section：Randomized Field Experiment

- locator：Experimental Design P1 S5

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：每个商品只在一个组中销售，以最小化跨组污染。

- rhetorical_function_cn：说明防止污染的设计选择。

- depends_on_cn：处理组/控制组区分。

- sets_up_cn：提高因果效度。

- evidence_pointer：Experimental Design第一段最后一句

### 46. Experimental Design P2 S1-S2

- order：46

- section：Randomized Field Experiment

- locator：Experimental Design P2 S1-S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：随机化按主播账号尾号进行，处理组尾号为0、1、3、8，控制组为其余；数据每5秒更新。

- rhetorical_function_cn：给出随机分配机制。

- depends_on_cn：无。

- sets_up_cn：为随机化检查提供基础。

- evidence_pointer：Experimental Design第二段

### 47. Data and Variables P3 S2

- order：47

- section：Randomized Field Experiment

- locator：Data and Variables P3 S2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：保留至少推广一个预售商品的直播流，得到192个处理组主播和265个控制组主播。

- rhetorical_function_cn：说明样本筛选规则。

- depends_on_cn：实验设计。

- sets_up_cn：为随机化检查和主分析提供样本。

- evidence_pointer：Data and Variables最后一句

### 48. Randomization Checks P1 S1-S3

- order：48

- section：Randomized Field Experiment

- locator：Randomization Checks P1 S1-S3

- move_code：RESULT

- paraphrase_cn：处理组和控制组在知名度、职业主播比例、网红比例、直播场次、时长和评分上均无显著差异。

- rhetorical_function_cn：报告随机化检查结果。

- depends_on_cn：随机分配机制。

- sets_up_cn：支持后续因果解释。

- evidence_pointer：Randomization Checks and Table 3

### 49. Main Effect P1 S1-S2

- order：49

- section：Analyses & Results

- locator：Main Effect P1 S1-S2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：主分析在流-商品层面进行，因为处理虽然是主播级，但实际销售变化来自每场直播中单个商品的呈现，且与仪表盘显示的商品级数据对应。

- rhetorical_function_cn：解释分析单位选择的原因。

- depends_on_cn：实验设计。

- sets_up_cn：引入主效应回归方程。

- evidence_pointer：How Does the Provision of Real-Time Sales Data Affect Sales?第一段

### 50. Main Effect Equation (1)

- order：50

- section：Analyses & Results

- locator：Main Effect Equation (1)

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者用Log销售对Treatment和时间、主播类、产品类固定效应回归。

- rhetorical_function_cn：指定主效应识别模型。

- depends_on_cn：流-商品层面理由。

- sets_up_cn：为报告系数做准备。

- evidence_pointer：Equation (1)

### 51. Main Effect P2 S3

- order：51

- section：Analyses & Results

- locator：Main Effect P2 S3

- move_code：RESULT

- paraphrase_cn：固定效应模型显示Treatment系数0.338，p<0.05，对应销量增加40.21%。

- rhetorical_function_cn：报告主效应结果。

- depends_on_cn：方程(1)。

- sets_up_cn：引出机制分析。

- evidence_pointer：Table 4

### 52. Mediation Analyses P1 S1

- order：52

- section：Mechanism

- locator：Mediation Analyses P1 S1

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：将控制组销售战术作为基准，处理组若出现战术差异即视为使用实时数据进行了即兴。

- rhetorical_function_cn：建立机制识别的对照逻辑。

- depends_on_cn：主效应。

- sets_up_cn：引出文本测量和中介模型。

- evidence_pointer：Mediation Analyses on Sales Tactics第一句

### 53. Mediation Analyses P1 S2-S3

- order：53

- section：Mechanism

- locator：Mediation Analyses P1 S2-S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：音频脚本用Universal ASR转写并按商品切分，与分析单位一致。

- rhetorical_function_cn：说明语音数据处理方法。

- depends_on_cn：控制组基准。

- sets_up_cn：为战术分类提供数据来源。

- evidence_pointer：Mediation Analyses第一段

### 54. Mediation Analyses P2 S1

- order：54

- section：Mechanism

- locator：Mediation Analyses P2 S1

- move_code：THEORY_INTRO

- paraphrase_cn：基于即兴理论和销售管理，将销售战术分为促销、语言和呈现节奏三类。

- rhetorical_function_cn：引入战术分类框架。

- depends_on_cn：即兴理论。

- sets_up_cn：为表5的战术测量提供理论依据。

- evidence_pointer：Mediation Analyses第二段

### 55. Mediation Analyses P2 S2-S3

- order：55

- section：Mechanism

- locator：Mediation Analyses P2 S2-S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者访谈主播来调整战术定义，使其符合直播场景。

- rhetorical_function_cn：说明测量开发结合定性访谈。

- depends_on_cn：战术分类。

- sets_up_cn：提升战术测量效度。

- evidence_pointer：Mediation Analyses第二段

### 56. Mediation Analyses P3 S1

- order：56

- section：Mechanism

- locator：Mediation Analyses P3 S1

- move_code：MECHANISM

- paraphrase_cn：如同音乐家观察观众反应，主播可查看实时销售数据并调整促销战术。

- rhetorical_function_cn：用即兴隐喻连接理论到战术。

- depends_on_cn：即兴理论。

- sets_up_cn：为促销战术指标设置理论依据。

- evidence_pointer：Mediation Analyses第三段

### 57. Mediation Analyses P4 S1

- order：57

- section：Mechanism

- locator：Mediation Analyses P4 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：使用LIWC提取每个商品的叙述脚本语言特征。

- rhetorical_function_cn：说明语言战术的测量方法。

- depends_on_cn：音频转写。

- sets_up_cn：为情感词和认知词变量提供测量。

- evidence_pointer：Mediation Analyses第四段

### 58. Mediation Analyses P5 S1-S2

- order：58

- section：Mechanism

- locator：Mediation Analyses P5 S1-S2

- move_code：MECHANISM

- paraphrase_cn：如同爵士音乐家根据观众反应调整节奏，主播可依据实时数据调整语速和单品时间。

- rhetorical_function_cn：将呈现节奏战术与即兴理论连接。

- depends_on_cn：即兴理论。

- sets_up_cn：为语速和时长指标提供依据。

- evidence_pointer：Mediation Analyses第五段

### 59. Mediation Analyses P6 S1

- order：59

- section：Mechanism

- locator：Mediation Analyses P6 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：使用PROCESS模型和5000次bootstrap进行中介分析。

- rhetorical_function_cn：说明中介检验方法。

- depends_on_cn：战术测量。

- sets_up_cn：为报告间接效应做准备。

- evidence_pointer：Mediation Analyses最后一段

### 60. Mediation Analyses P7 S1

- order：60

- section：Mechanism

- locator：Mediation Analyses P7 S1

- move_code：RESULT

- paraphrase_cn：四个关键销售战术显著中介实时数据与销售的关系：催促、情感表达、语速、单品时长。

- rhetorical_function_cn：报告中介分析主要结论。

- depends_on_cn：PROCESS模型。

- sets_up_cn：为异质性分析提供机制基础。

- evidence_pointer：Figure 3和Table 6

### 61. Heterogeneity Analyses P1 S1

- order：61

- section：Heterogeneity

- locator：Heterogeneity Analyses P1 S1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：即兴需要两个关键条件：需要即兴的决策不确定性和决策者的即兴能力。

- rhetorical_function_cn：从理论推出边界条件。

- depends_on_cn：即兴理论和中介结果。

- sets_up_cn：引领产品不确定性和主播能力两个异质性分析。

- evidence_pointer：Heterogeneity Analyses第一段

### 62. Heterogeneity by product uncertainty P1 S1

- order：62

- section：Heterogeneity

- locator：Heterogeneity by product uncertainty P1 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用产品所有权作为不确定性代理，区分品牌店与小商家。

- rhetorical_function_cn：说明不确定性如何操作化。

- depends_on_cn：不确定性条件。

- sets_up_cn：为交互模型做测量准备。

- evidence_pointer：Heterogeneity by product uncertainty第一段

### 63. Heterogeneity by product uncertainty P1 S2-S3

- order：63

- section：Heterogeneity

- locator：Heterogeneity by product uncertainty P1 S2-S3

- move_code：MECHANISM

- paraphrase_cn：品牌店有品牌认知降低不确定性，小商家缺乏品牌认知增加不确定性，因此更需要实时数据即兴。

- rhetorical_function_cn：用机制解释为什么产品所有权调节效应。

- depends_on_cn：不确定性操作化。

- sets_up_cn：预测小商家子样本效应显著。

- evidence_pointer：Heterogeneity by product uncertainty第一段

### 64. Heterogeneity by product uncertainty P2 S2

- order：64

- section：Heterogeneity

- locator：Heterogeneity by product uncertainty P2 S2

- move_code：RESULT

- paraphrase_cn：交互项显著为负，子样本显示效应主要出现在小商家商品中。

- rhetorical_function_cn：报告不确定性异质性结果。

- depends_on_cn：交互模型。

- sets_up_cn：强化即兴机制解释。

- evidence_pointer：Table 7

### 65. Heterogeneity by streamer rating P1 S1-S2

- order：65

- section：Heterogeneity

- locator：Heterogeneity by streamer rating P1 S1-S2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用平台基于KPI的主播评分作为即兴能力代理，定义Top-rated streamer。

- rhetorical_function_cn：说明即兴能力如何操作化。

- depends_on_cn：即兴能力条件。

- sets_up_cn：为评分交互模型做测量准备。

- evidence_pointer：Heterogeneity by streamer rating第一段

### 66. Heterogeneity by streamer rating P2 S1-S2

- order：66

- section：Heterogeneity

- locator：Heterogeneity by streamer rating P2 S1-S2

- move_code：RESULT

- paraphrase_cn：Top-rated交互项显著正，效应只在top-rated主播中显著，其他主播不显著。

- rhetorical_function_cn：报告即兴能力异质性结果。

- depends_on_cn：交互模型。

- sets_up_cn：支持System 1/专家直觉理论。

- evidence_pointer：Table 8

### 67. Falsification Tests P1 S4

- order：67

- section：Additional Analyses

- locator：Falsification Tests P1 S4

- move_code：RESULT

- paraphrase_cn：未浏览仪表盘的主播中，处理效应不显著。

- rhetorical_function_cn：用必要使用条件做反事实检验。

- depends_on_cn：主效应。

- sets_up_cn：证明效应由仪表盘使用驱动。

- evidence_pointer：Table 9 Column 1

### 68. Falsification Tests P2 S3

- order：68

- section：Additional Analyses

- locator：Falsification Tests P2 S3

- move_code：RESULT

- paraphrase_cn：非预售商品销量在两组间无显著差异，排除处理对非预售的溢出。

- rhetorical_function_cn：排除同一直播流中非预售商品的替代效应。

- depends_on_cn：主效应。

- sets_up_cn：说明效应不是从普通商品转移到预售。

- evidence_pointer：Table 9 Column 2

### 69. Falsification Tests P3 S3

- order：69

- section：Additional Analyses

- locator：Falsification Tests P3 S3

- move_code：RESULT

- paraphrase_cn：常规商品占比高低与处理交互不显著，说明常规商品不干扰预售商品效应。

- rhetorical_function_cn：排除混合商品组合干扰。

- depends_on_cn：溢出检验。

- sets_up_cn：进一步巩固处理效应的纯粹性。

- evidence_pointer：Table 9 Column 3

### 70. Falsification Tests P4 S1

- order：70

- section：Additional Analyses

- locator：Falsification Tests P4 S1

- move_code：RESULT

- paraphrase_cn：处理组与控制组在浏览量和访问量上无显著差异。

- rhetorical_function_cn：排除实验前流量和市场竞争混淆。

- depends_on_cn：主效应。

- sets_up_cn：说明效应发生在进入直播后的主播行为而非观众进入。

- evidence_pointer：Falsification Tests第四段

### 71. Alternative Mechanism P1 S1-S2

- order：71

- section：Additional Analyses

- locator：Alternative Mechanism P1 S1-S2

- move_code：RESULT

- paraphrase_cn：主播在直播中通常没有临时定价权，价格由事前合同锁定，因此价格调整不是合理解释。

- rhetorical_function_cn：从制度证据排除替代渠道。

- depends_on_cn：访谈和行业惯例。

- sets_up_cn：为关键词检验做铺垫。

- evidence_pointer：Alternative Mechanism第一段

### 72. Alternative Mechanism P3 S3

- order：72

- section：Additional Analyses

- locator：Alternative Mechanism P3 S3

- move_code：RESULT

- paraphrase_cn：价格调整关键词频率极低、组间无差异、中介路径不显著。

- rhetorical_function_cn：用实证排除价格替代机制。

- depends_on_cn：关键词测量和PROCESS模型。

- sets_up_cn：支持即兴战术机制。

- evidence_pointer：Alternative Mechanism第三段

### 73. Historical Demand Records P4 S1-S3

- order：73

- section：Additional Analyses

- locator：Historical Demand Records P4 S1-S3

- move_code：RESULT

- paraphrase_cn：无历史记录商品中实时数据效果显著，有历史记录商品中不显著，但交互项不显著，作者谨慎解释。

- rhetorical_function_cn：展示实时数据与历史数据的边界交互。

- depends_on_cn：历史记录变量。

- sets_up_cn：在讨论中突出实时数据不可替代的价值。

- evidence_pointer：Table 11和Historical Demand Records段落

### 74. Main Findings P1 S1-S3

- order：74

- section：Discussion

- locator：Main Findings P1 S1-S3

- move_code：RESULT

- paraphrase_cn：总结实时数据提升预售销售40.21%，通过催促、情感词、语速和时长等即兴战术起作用。

- rhetorical_function_cn：在讨论开篇重述核心结果。

- depends_on_cn：全部实证结果。

- sets_up_cn：为理论贡献作基础。

- evidence_pointer：Discussion Main Findings

### 75. Implications for Research P1 S1-S5

- order：75

- section：Discussion

- locator：Implications for Research P1 S1-S5

- move_code：CONTRIBUTION

- paraphrase_cn：对数据驱动决策文献的贡献在于证明实时数据在紧急环境中通过即兴和System 1思维起作用，不同于历史数据。

- rhetorical_function_cn：将结果提升为理论贡献。

- depends_on_cn：主效应和机制结果。

- sets_up_cn：为后文直播平台和即兴理论贡献铺垫。

- evidence_pointer：Implications for Research第一段

### 76. Implications for Research P3 S1-S3

- order：76

- section：Discussion

- locator：Implications for Research P3 S1-S3

- move_code：CONTRIBUTION

- paraphrase_cn：对直播带货平台文献的贡献是提出实时IT制品设计以支持主播临场决策。

- rhetorical_function_cn：定位在直播平台设计研究。

- depends_on_cn：IT制品实验。

- sets_up_cn：为实践含义提供理论支撑。

- evidence_pointer：Implications for Research第二段

### 77. Implications for Research P4 S1-S3

- order：77

- section：Discussion

- locator：Implications for Research P4 S1-S3

- move_code：CONTRIBUTION

- paraphrase_cn：对即兴理论的贡献是将其扩展到无物理观众反馈的在线直播环境，实时数据可模拟观众反馈。

- rhetorical_function_cn：把边界条件转化为理论推广。

- depends_on_cn：异质性结果和机制。

- sets_up_cn：说明技术可以弥补即兴反馈缺失。

- evidence_pointer：Implications for Research第三段

### 78. Implications for Practice P1 S1-S3

- order：78

- section：Discussion

- locator：Implications for Practice P1 S1-S3

- move_code：PRACTICAL_STAKES

- paraphrase_cn：建议平台投资实时数据基础设施，并根据主播能力和产品不确定性定制仪表盘和培训。

- rhetorical_function_cn：把研究结果转化为管理建议。

- depends_on_cn：边界条件结果。

- sets_up_cn：为限制与未来研究收尾。

- evidence_pointer：Implications for Practice

### 79. Limitations P1 S1-S4

- order：79

- section：Discussion

- locator：Limitations P1 S1-S4

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：指出短期窗口、价格灵活性的情境依赖、缺少engagement指标和未操纵呈现格式等限制。

- rhetorical_function_cn：界定适用边界并给出未来方向。

- depends_on_cn：全部研究设计。

- sets_up_cn：为读者提供对结果范围的理解。

- evidence_pointer：Limitations and Future Research

## 写作技术

- gap_construction_cn：先承认历史数据对计划决策的价值，然后指出直播场景的快节奏、不确定性和无物理观众反馈使历史记录失效，从而把缺口精确锁定在“实时数据对即兴决策的作用”。

- signposting_cn：在引言就列出RQ1-RQ3；在正文用“How Does...”、“What Are the Plausible Underlying Mechanisms?”、“Heterogeneity Analyses”、“Additional Analyses”等标题对研究阶段进行路标式预告。

- transition_logic_cn：每个阶段结尾留下尚未解决的具体问题，例如主效应后问“机制是什么”，中介后问“边界条件是否支持即兴”，机制后用“反事实检验排除替代解释”，最后用历史数据对比把讨论引向理论。

- claim_evidence_rhythm_cn：先报告主效应系数，随后立即用战术中介分解效应，再用异质性结果加强机制，最后用反事实和替代机制排除竞争解释；每类主张都紧跟对应表格或检验。

- benchmark_narrative_cn：benchmark不是技术基线，而是控制组和低不确定性/低能力子样本；中介分析把控制组战术作为默认脚本，处理组偏离即被视为即兴，使得对照概念与理论高度一致。

- theory_return_cn：讨论部分把40.21%的销量提升、四条战术中介和两个边界条件重新编码为System 1思维和即兴理论在无物理观众环境中的延伸，并用历史数据对比说明实时数据的独特决策功能。

- contribution_positioning_cn：作者同时面向数据驱动决策、直播平台设计和即兴理论三个文献，分别强调“实时数据非计划决策”“IT制品设计支持临场决策”“在线环境可借助技术实现即兴”。

- novelty_protection_cn：通过把结果绑定到即兴理论和System 1，使单平台、单商品类别、三天窗口的结果看起来具有理论普遍性；同时用未使用仪表盘、非预售溢出、价格替代和多平台访谈等证据防止贡献被简化为一次性平台实验结果。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：把真实商业现象压缩为需要临场决策的具体任务，并用市场规模说明重要性。

- research_job_cn：选择或识别一个决策者在不确定、时间压力和复杂任务下行动的真实场景。

- required_evidence_cn：场景中的任务复杂度、不确定来源和时间压力需要有文本或访谈支持。

- transition_to_next_cn：说明历史数据/已有决策支持工具在该场景中的局限，引出新的实时反馈设计。

#### 2. 2

- step：2

- writing_job_cn：建立文献缺口：现有研究关注计划决策或历史数据，未关注实时数据对即兴决策的作用。

- research_job_cn：系统梳理相关文献并找出具有理论张力的竞争预测。

- required_evidence_cn：引用代表性文献说明已有研究范围。

- transition_to_next_cn：把张力转化为研究问题和可检验的机制。

#### 3. 3

- step：3

- writing_job_cn：引入理论透镜（如即兴理论、System 1/2）并推导机制、边界条件和可能的相反机制。

- research_job_cn：用理论确定关键调节变量和中介行为类别。

- required_evidence_cn：理论命题与场景存在可操作映射。

- transition_to_next_cn：说明需要随机/准实验来检验竞争预测。

#### 4. 4

- step：4

- writing_job_cn：描述平台或组织中的随机现场实验设计、处理/控制差异、随机化规则和数据层级。

- research_job_cn：获取或参与真实平台实验，保证随机化和避免污染。

- required_evidence_cn：处理分配规则、仪表盘界面、随机化检查和样本描述。

- transition_to_next_cn：报告主效应后立即转向机制证据。

#### 5. 5

- step：5

- writing_job_cn：用过程数据（如文本、语音、行为日志）测量中介变量，报告主效应和中介路径。

- research_job_cn：从音频/文本/日志中构造与理论构念对齐的行为指标，并做bootstrap中介。

- required_evidence_cn：中介路径显著且方向符合理论。

- transition_to_next_cn：用理论预期的调节变量检验机制边界。

#### 6. 6

- step：6

- writing_job_cn：报告产品不确定性和决策者能力异质性，并加入反事实、溢出和替代机制检验。

- research_job_cn：用子样本、交互项和反事实分析排除竞争解释。

- required_evidence_cn：调节方向符合理论，反事实检验不显著或符合预期。

- transition_to_next_cn：在讨论中把结果回收到理论。

#### 7. 7

- step：7

- writing_job_cn：讨论部分重新连接引言缺口，明确技术、制品、机制、边界和理论贡献，给出实践建议和限制。

- research_job_cn：总结哪些结果具有一般性，哪些依赖平台制度，哪些未直接检验。

- required_evidence_cn：全部结果能闭合引言缺口。

- transition_to_next_cn：限制与未来研究自然结束。

### most_transferable_moves_cn

1. 用竞争性预测而非单一假设构造研究问题

2. 把抽象机制（即兴）操作化为可观察的行为战术并从中介分析入手

3. 用理论必要条件（不确定性、能力）设计异质性分析

4. 用反事实检验和替代机制排除竞争解释

5. 在讨论中用System 1/即兴理论把平台实验结果提升为一般决策知识

### resource_intensive_or_nonstandard_parts_cn

1. 与大型平台合作取得随机现场实验机会

2. 平台对仪表盘功能进行实际干预并控制商品分组销售

3. 需要直播音频转写系统（Universal ASR）、LIWC和按商品切分的脚本数据

4. 需要主播和平台高管访谈来校准战术关键词和确认行业制度

5. 平台数据脱敏和数据使用许可

### what_not_to_copy_superficially_cn

1. 不能只抄“40.21%”而忽略随机化检查和固定效应模型

2. 不能把任意文本词频直接称为即兴，必须有理论映射和访谈校准

3. 不能只做中介就宣称机制，需要异质性和反事实逻辑

4. 不能忽略价格、产品类型、主播能力等制度性和情境性边界

5. 不能在没有平台随机干预时声称随机现场实验

- single_best_description_of_the_routine_cn：找到一个亟需临场决策的真实平台环境，用随机现场实验改变一个实时数据反馈设计，从主效应、中介战术、异质性边界到反事实和替代机制逐层打开，最后把结果回收到即兴理论与System 1，形成理论驱动的现场因果研究。

## 分析边界

分析基于提供的全文文本，图表和附录基本完整，但部分具体数字和表格细节依赖文中报告；由于没有原始页码，位置标识以章节和段落级别为准；文章为MIS Quarterly格式，作者对结果有较强因果主张，本解剖在机制和外部效度方面保留了必要谨慎。
