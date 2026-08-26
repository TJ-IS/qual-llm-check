# Combining analytics and simulation methods to assess the impact of shared, autonomous electric vehicles on sustainable urban mobility

- 作者：Oliver Dlugosch; Tobias Brandt; Dirk Neumann
- 年份 / 期刊：2022 / Information & Management
- DOI：10.1016/j.im.2020.103285
- 源文件：20231_2022_combining-analytics-and-simulation-methods-to-assess-the-impact-of-shared-autonomous-electric-ve.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.87

## 文章级论证概况

- 核心问题：如何构建并运用结合数据分析和仿真方法的决策支持系统，定量评估共享、自动驾驶电动汽车（SAEV）对城市出行可持续性的影响，特别是车队规模、充电基础设施与服务水平之间的互动关系？

- 制品与设计：文章构建了一个基于Python的智能体仿真平台，配合一个预测性分析模块。仿真平台把柏林一家自由浮动式汽车共享运营商的真实出行记录转化为请求事件，将运营区离散为正六边形蜂窝区；包含请求分配、车辆重定位、充电决策三类模块；并用移动平均法基于时空特征预测各蜂窝区的空闲时间，指导车辆重定位；充电规则为低于50%电量时自动充电、行程结束后低于25%时强制充电；评价中以车辆数|V|和充电点数|P|为二维参数空间，观察错过请求率、等待时间超过10分钟比例、闲置率等指标。

- 客观结果：在纯自动驾驶燃油车情形下，600辆车即可接近零拒绝，约等于运营数据中同时使用车辆数的理论下界，意味着可将原1104辆规模缩减约48%。加入电动化后，车辆数仍是最主要约束，但充电基础设施的影响在|P|=28后饱和；在700辆车和26个充电点时可实现零拒绝，车队可减少37%；在600辆车与28个充电点场景下，车辆利用率可超过55%。敏感性分析显示，战略布局充电点、加速充电、需求扩张和高能耗在等比调整后模式类似，说明结果对参数有一定稳健性，车队规模主要受峰值需求驱动。

- 核心贡献：作者声称的主要贡献是展示一种将真实世界数据、分析技术和仿真方法结合的决策支持系统，能够帮助理解共享经济、电动化和自动驾驶三种变革如何共同影响城市出行；为政策制定者和管理者提供车队规模、充电桩数量和可维持服务水平之间权衡的定量依据，并提供一个可迁移到其他城市的开放仿真平台。

- 整篇论证链：论文从共享经济、电动化和自动驾驶正在重塑城市出行这一现实问题切入，指出这些挑战不能孤立分析，因此提出用数据驱动决策支持系统——结合分析与仿真——来系统评估SAEV的影响。作者使用柏林某自由浮动式汽车共享运营商51天的29万条真实行程数据，先描述当前车队利用率低下、峰值需求明显、理论车队下界约574辆的问题；然后构建模块化智能体仿真平台，以历史请求为事件，加入预测分析模块用于重定位，并加入充电约束。仿真分两步：先检验纯自动驾驶（内燃机）情形，发现约600辆车即可接近零拒绝，接近理论下界；随后引入电动化，在车队规模和充电点数二维网格中揭示了充电基础设施的边际效益在28个充电点后饱和，并给出可操作的车队—充电点权衡。最后通过多个敏感性分析检验战略布点、充电功率、需求扩张和能耗上升的稳健性，再在讨论部分把结果提升为对运营者、政策制定者和IS研究的一般含义。

## 类型与写作弧线判定

- 论文主类型判定：文章的核心产出是一个结合数据分析和智能体仿真的决策支持系统（Python仿真平台），并通过对真实数据驱动的参数网格实验和敏感性分析来评价该制品的有效性与边界条件；虽然没有正式的设计理论或用户实验，但整体遵循构建—评价—产生设计知识的路径。

- 主导写作弧线判定：文章先提出城市出行可持续性这一棘手问题，随后引入“数据分析+仿真”的理论动机作为设计基础，再设计与实现智能体仿真平台，通过仿真和敏感性分析检验该设计，最后在讨论中回到决策支持系统如何应对棘手问题及未来研究路径，形成了问题—理论—设计—检验—回到理论/含义的闭环。

## 研究开展程序

- study_or_phase_count：6

- 研究阶段总序列：第一阶段用真实FFCS运营数据刻画系统现状与理论下界；第二阶段构建结合预测分析和智能体仿真的仿真平台；第三阶段用纯自动驾驶（内燃机）仿真隔离自动驾驶的贡献；第四阶段用二维V×P网格仿真加入电动化约束并识别权衡；第五阶段通过多种敏感性分析检验稳健性与边界；第六阶段在讨论中把结果转化为管理、政策和研究含义。阶段之间层层递进：数据描述产生理论下界，模型构建为后续反事实实验提供工具，AV仿真奠定车队缩减效果，SAEV仿真引入充电基础设施约束，敏感性分析防止结论被局部参数绑架，讨论将局部案例结果提升为可迁移发现。

### studies_or_phases

#### 1. 真实运营数据描述与理论下界分析

- order：1

- name_cn：真实运营数据描述与理论下界分析

- question_cn：柏林当前FFCS系统的使用模式如何？在不改变出行行为的前提下，满足峰值需求所需的最低车队规模是多少？

- inputs_and_setting_cn：51天、290,000次行程、1104辆燃油车、行程起终点和时间戳、燃油量；柏林某运营商的营业区及其热力图；Fig.1、Fig.2、Table 1、Table 2。

- designed_or_compared_object_cn：无设计对象，主要是对既有运营数据的描述性分析，并推导同时使用车辆的并发数。

- baseline_control_or_counterfactual_cn：以现有1104辆燃油车及真实服务模式作为自然基线；理论下界取观察期内最大并发使用车辆数574。

##### objective_metrics

1. 每车每天行程数

2. 空闲时间

3. 行程时间

4. 并发使用车辆数及其占车队比例

5. 一周内不同日/时段的利用模式

- analysis_method_cn：描述性统计、时间序列可视化、并发使用数统计、平均日内模式比较。

- main_result_cn：平均约70%以上车队闲置，并发车辆数在130到574之间波动；工作日有两段峰值（上午约3小时，傍晚约4小时），周末下午有较高平台和傍晚小峰；相关距离在电动车单次续航范围内。

- argumentative_role_cn：建立现状基线、说明当前车队容量过度供给，并提供一个可对照的理论下限；同时为后续仿真的参数选择（车队规模、充电点下界）提供依据。

- remaining_uncertainty_cn：描述性数据无法说明自动驾驶和电动化会如何改变系统运行，也无法验证车队缩减是否可持续。

- link_to_next_phase_cn：由当前下界和需求峰值引出需要仿真模型来测试不同车队规模和充电约束下的表现。

##### evidence_pointers

1. Table 1

2. Table 2

3. Fig. 2a

4. Fig. 2b

5. Section 3 data characteristics

#### 2. 仿真平台构建：数据分析模块与智能体仿真

- order：2

- name_cn：仿真平台构建：数据分析模块与智能体仿真

- question_cn：如何将真实出行数据与自动驾驶/电动化反事实操作结合成一个可扩展、可迁移的仿真平台？

- inputs_and_setting_cn：前51天行程数据按时间切分为训练集和测试集；Open Charge Map柏林充电点位置；OSRM路由服务；业务区域离散为直径2km的蜂窝区；车辆、充电点、请求事件作为智能体/对象。

- designed_or_compared_object_cn：仿真平台本身；包括请求分配逻辑（最近空闲车先到先得）、重定位规则（先覆盖未覆盖蜂窝，再用预测空闲时间差并设定120分钟阈值）、充电规则（空闲时低于50%充电，行程结束后低于25%强制充电）、模块化Request/Task/Update结构。

- baseline_control_or_counterfactual_cn：仿真平台没有直接与其他仿真器做基准比较，而是通过不同参数设置产生反事实情境；仿真首日被排除以避免初始随机放置造成的偏差。

##### objective_metrics

1. 小时级预测空闲时间

2. 重定位距离与时间

3. 充电状态与模式分布

- analysis_method_cn：基于智能体的离散时间仿真；训练/测试切分；移动平均预测；距离加权预测；阈值决策规则。

- main_result_cn：平台可对任意|V|和|P|组合进行仿真，输出请求拒绝率、等待时间分布、利用率等指标；模块化设计使敏感性分析和未来扩展成为可能。

- argumentative_role_cn：提供评价SAEV的核心工具，是后续所有反事实实验的基础；同时通过方法合理性论证说明为什么自定义Python仿真比MATSim/SUMO等现成平台更合适。

- remaining_uncertainty_cn：模型决策规则较简单，未包含请求排队、动态路径优化、充电中断或超快速充电非线性等现实复杂性。

- link_to_next_phase_cn：构建完成后即可用该平台分别评测纯自动驾驶和自动驾驶+电动化两种情形。

##### evidence_pointers

1. Section 4.1 Model logic

2. Section 4.2 Simulation platform and setup

3. Fig. 3

4. Eq. (1)

#### 3. 纯自动驾驶燃油车仿真（分离自动驾驶效应）

- order：3

- name_cn：纯自动驾驶燃油车仿真（分离自动驾驶效应）

- question_cn：在不考虑电动化约束时，自动驾驶能使共享车队规模缩减到多少？

- inputs_and_setting_cn：相同真实行程请求；车辆规模|V|从100到700；不设置充电约束；燃油补充时间设为可忽略（全车队每天约300分钟）。

- designed_or_compared_object_cn：不同车队规模下的仿真运行，自动驾驶车辆可自行移动到请求点并执行重定位。

- baseline_control_or_counterfactual_cn：对比真实车队1104辆和理论下界574辆；同时在不同车队规模之间形成梯度比较。

##### objective_metrics

1. 错过请求比例

- analysis_method_cn：参数扫描仿真；与理论下界比较。

- main_result_cn：600辆及以上车辆时错过请求率接近0或为0；600辆对应约0.2%的拒绝率，接近并略高于下界574辆；说明即使简单的重定位策略也能实现自动驾驶带来的大部分车队缩减潜力。

- argumentative_role_cn：隔离自动驾驶的贡献，证明车队缩减主要源于车辆可自行移动到客户，而不是电动化效应；也说明服务水平和车队规模之间存在可权衡空间。

- remaining_uncertainty_cn：该阶段没有考虑充电时间，也没有考虑用户行为变化（如拼车、转移峰值出行）。

- link_to_next_phase_cn：加入电动化后，充电约束会怎么改变这个结论成为下一阶段的直接问题。

##### evidence_pointers

1. Section 5.1

2. Table 3

#### 4. SAEV仿真：车队规模与充电基础设施二维参数扫描

- order：4

- name_cn：SAEV仿真：车队规模与充电基础设施二维参数扫描

- question_cn：加入电动化后，车队规模与充电点数量如何共同决定服务水平？是否存在可识别的权衡和资源门槛？

- inputs_and_setting_cn：真实行程请求；电池50kWh、效率15kWh/100km、充电功率11kW；|V|从100到700，|P|从20到30再扩展至40/50/75/100；随机选择柏林现有充电点。

- designed_or_compared_object_cn：不同|V|×|P|组合下的系统表现；同时记录错过请求、等待时间超过10分钟比例、闲置率。

- baseline_control_or_counterfactual_cn：以步骤1的真实车队和理论下界为基准；表内不同行列构成互相参照；通过与纯自动驾驶结果对比识别电动化约束。

##### objective_metrics

1. 错过请求比例

2. 等待时间超过10分钟的行程比例

3. 车辆空闲时间比例

4. 不同模式（行驶、接客、充电、重定位等）的时间分配

- analysis_method_cn：二维参数网格仿真；模式识别（何时 |V| 约束、何时 |P| 约束）；交换率计算。

- main_result_cn：小规模车队时车辆数约束主导，充电点增加无影响；约从|V|=300开始充电点形成约束；|P|=28后额外充电点不再改善服务水平；实际相关星座为500≤|V|≤700且26≤|P|≤30；|P|=26、|V|=700时零拒绝，车队可减少37%；在|P|=26、|V|=500与|P|=28、|V|=600之间观察到约50:1的车与充电点交换率；P=28,V=600时利用率超55%。

- argumentative_role_cn：论文核心证据，直接支撑“SAEV可大幅减少车队和充电点投入”的主张，同时揭示经济性（车队）与可持续性/基础设施之间的权衡。

- remaining_uncertainty_cn：结果依赖随机布点、固定充电规则、简化电池模型；对充电点位置、充电功率、需求规模敏感，因此需要敏感性分析。

- link_to_next_phase_cn：为了排除这些结果只是参数巧合，下一阶段进行多种敏感性分析。

##### evidence_pointers

1. Table 4

2. Table 5

3. Table 6

4. Fig. 4

5. Section 5.2

#### 5. 敏感性分析：战略布点、充电功率、需求扩张与能耗水平

- order：5

- name_cn：敏感性分析：战略布点、充电功率、需求扩张与能耗水平

- question_cn：基准结果对充电点布局、充电功率、需求规模和能耗水平的变化是否稳健？

- inputs_and_setting_cn：基于训练数据将充电点按各蜂窝区未满足能量需求排序放置；充电功率改为24kW；需求通过重采样扩展2.5、5、7.5、10倍；能耗改为20kWh/100km；各情形对|P|和|V|进行等比调整。

- designed_or_compared_object_cn：五种情形：基准、战略布点、加速充电、需求扩张、高能耗；与基准表相应数值比较。

- baseline_control_or_counterfactual_cn：基准情形作为对照；每种敏感情形按物理逻辑等比调整|P|或|V|后再比较。

##### objective_metrics

1. 错过请求比例（残差变化）

2. 战略布点相对随机的服务改进百分比

- analysis_method_cn：参数扫描仿真；表格对比；按比例修正后的模式比较。

- main_result_cn：战略布点总体与随机布点相似，最多减少1.5%错过请求，但在|P|=26、|V|=600时带来4.7个百分点的改进；加速充电和较高能耗在等比例调整后模式类似；需求扩张在等比例增加车队和充电点后模式与基准一致，说明车队规模主要由峰值需求决定。

- argumentative_role_cn：证明核心结论不是随机布点或特定参数的偶然产物，为把案例结果推广到政策情景提供依据；同时揭示峰值需求是车队规模的决定性机制。

- remaining_uncertainty_cn：敏感性分析仍基于同一城市数据、同一行为假设；线性外推至全柏林汽车出行只是近似。

- link_to_next_phase_cn：稳健性结果被讨论部分用于政策外推和管理建议。

##### evidence_pointers

1. Table 7

2. Table 8

3. Appendix Tables 9–14

4. Fig. 5

#### 6. 讨论与管理/政策/研究含义

- order：6

- name_cn：讨论与管理/政策/研究含义

- question_cn：仿真结果对运营者、政策制定者和IS研究者意味着什么？这些发现如何回应开头的棘手问题？

- inputs_and_setting_cn：基于前五阶段的仿真和敏感性结果；柏林人口出行统计（88.4%居民出行、3.4行程/天、32%私人机动车、1.3人/车）；租车费率约200美元/月。

- designed_or_compared_object_cn：无需设计新的仿真比较；主要是结果解释、成本估算、城市尺度外推和研究议程。

- baseline_control_or_counterfactual_cn：以柏林当前约115万辆私人汽车作为对照；以当前1000充电点为“点燃EV”的参照。

##### objective_metrics

1. 成本节省（约960,000美元/年）

2. 全柏林SAEV化所需车队与充电点估计（264,000辆车、12,320个充电点）

3. 潜在车辆减少比例（约77%）

- analysis_method_cn：反事实外推、成本换算、基于敏感性线性缩放、研究纲领阐述。

- main_result_cn：SAEV系统可用很少充电点支撑大量共享出行；运营者可通过减少约400辆车节省大量成本；全柏林机动车出行若全部SAEV化，可减少约77%车辆，充电点需求相对当前千点规模约提高一个数量级；研究上应继续扩展数据、算法、用户行为、拼车、能源系统和社会公平等视角。

- argumentative_role_cn：把仿真数字转化为行动导向的含义，并回扣开头的决策支持系统与棘手问题论述；同时标明未来研究边界，防止结果被理解为一次性案例。

- remaining_uncertainty_cn：全柏林外推依赖线性缩放和粗糙假设；实际路网、行为变化、充电非线性、社会接受度等均未直接检验。

- link_to_next_phase_cn：结束全文，将平台留作未来扩展的开放性工具。

##### evidence_pointers

1. Section 6.1 Managerial and policy implication

2. Section 6.2 Implications for research

## 各部分修辞架构

### abstract_moves

1. CONTEXT: 城市出行正经历共享经济、电动化和自动驾驶三重转变。

2. RQ_OR_OBJECTIVE: 证明结合数据分析与仿真的DSS对理解复杂城市交通系统的价值。

3. RESULT: 以柏林为案例，SAEV可大幅减少资源投入并保持服务稳定。

4. PRACTICAL_STAKES: 为利益相关者提供经济效益与可持续性权衡的信息。

### introduction_moves

1. CONTEXT: 共享经济在多个行业快速扩张并转向“使用权经济”。

2. PHENOMENON: 城市交通是使用权经济转型的典型领域，自由浮动式汽车共享快速增长。

3. PRIOR_KNOWLEDGE: 已有研究开始处理共享车辆运营问题，但电动化和自动驾驶是另外两大变革。

4. PRACTICAL_STAKES: 决策者面临充电设施投资和供需平衡等挑战，且这些挑战互相交织。

5. RQ_OR_OBJECTIVE: 探索结合真实数据、分析与仿真的信息系统如何支持SAEV整合分析。

6. METHOD_JUSTIFICATION: 分析模块预测供需模式，仿真平台分析运营决策对可持续性和经济可行性的影响。

7. RESULT: 柏林案例显示车队可减半，充电点需求极低。

8. CONTRIBUTION: 强调数据驱动DSS对可持续交通和基础设施投资的贡献。

9. STUDY_OVERVIEW: 给出全文路线图。

### theory_and_knowledge_moves

1. CONTEXT: IS研究正重新关注如何应对棘手问题。

2. PHENOMENON: 城市可持续性问题因多层复杂系统而进一步棘手。

3. PRIOR_KNOWLEDGE: 综述汽车共享、电动车、自动驾驶三条研究线的进展与局限。

4. GAP: 各单独研究多聚焦单项技术或运营问题，缺乏整合分析工具。

5. THEORY_INTRO: 提出“真实数据让系统交互可见，仿真让反事实操纵可行”的理论动机。

6. THEORY_PROPOSITION: 将数据分析与仿真结合可以揭示复杂系统对变革的反应。

7. CONTRIBUTION: 将基于真实数据的预测、仿真框架和互动分析作为对现有研究的扩展。

### artifact_design_moves

1. METHOD_JUSTIFICATION: 智能体建模适合分析多主体交互的交通网络。

2. DESIGN_FEATURE: 选择自建Python平台而非通用平台，以保证可扩展、可复现、可迁移。

3. REQUIREMENT: 需求不确定性要求预测分析模块支持主动重定位和充电。

4. DESIGN_FEATURE: 采用蜂窝分区、训练/测试分割、移动平均预测、距离加权空闲时间。

5. DESIGN_FEATURE: 重定位规则先覆盖未覆盖蜂窝，再用预测收益阈值120分钟。

6. DESIGN_FEATURE: 充电规则为低电量阈值与防止中途断电的强制充电。

7. BENCHMARK_OR_CONTRAST: 设置电池、效率、充电功率、车队规模范围和充电点范围。

### evaluation_moves

1. BENCHMARK_OR_CONTRAST: 以真实车队和理论下界为参照，用参数网格系统比较。

2. BENCHMARK_OR_CONTRAST: 以错过请求率和等待时间>10分钟为服务指标，引用用户容忍阈值。

3. RESULT: 纯AV结果显示600辆车接近零拒绝。

4. RESULT: SAEV网格显示充电点在28之后饱和，识别实际相关星座。

5. ROBUSTNESS_OR_BOUNDARY_TEST: 战略布点、加速充电、需求扩张、高能耗等敏感性分析。

6. MECHANISM: 总结峰值需求是车队规模的决定因素。

### discussion_and_contribution_moves

1. CONTRIBUTION: 为管理者和政策制定者提供车型、车队、充电点投资的定量论据。

2. BOUNDARY_CONDITION: 方法可迁移至其他城市，开放平台提供可复现性。

3. PRACTICAL_STAKES: 估算运营者成本节约和全柏林SAEV化潜力。

4. THEORY_RETURN: 重新连接到数据驱动DSS应对棘手问题的论题。

5. LIMITATION_AND_FUTURE: 提出数据、算法、排队、充电策略、拼车、能源系统和社会公平等未来方向。

## 理论/知识到设计的翻译

### 知识/理论基础

1. IS领域关于棘手问题与数据驱动决策支持系统的讨论（Ketter et al.）

2. 自由浮动式汽车共享中需求—供给失衡与车辆重定位的运营研究（Wagner et al.、Willing et al.、Weikl & Bogenberger等）

3. 电动车充电和续驶里程约束下的车队运营与充电基础设施文献

4. 智能体建模在复杂系统与交通网络中的方法论优势

5. FFCS用户等待时间容忍度的实证调查（Herrmann et al.）

- 理论—设计耦合：partial

- 耦合判定理由：文章提出了“数据观察+仿真操纵”的总体理论动机，并以智能体建模方法论支撑平台选择，但详细设计—如蜂窝网格尺寸、重定位阈值、充电触发规则、参数范围—主要来自领域运营知识、工程启发式和现实数据约束，而非形式化理论命题直接推导。

- 理论到设计翻译链：棘手问题（复杂社会经济技术系统） → 需要用数据观察真实交互而不显式建模所有动机 → 需要能操纵环境（电动化、自动驾驶）的仿真 → 必须把历史行程转为请求事件并加入预测分析模块 → 重定位规则依据预测空闲时间，充电规则依据电池阈值 → 车队规模与充电点数参数扫描 → 以错过请求率、等待时间和闲置率评价服务 → 再由敏感性分析将局部结果提升为关于峰值需求驱动车队规模的机制性发现。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：棘手问题中的复杂系统交互可由真实数据反映，而不必显式建模每个行为动机；仿真则可操纵系统环境。

- mechanism_cn：历史行程数据隐含通勤、娱乐等复杂动机的空间时间模式；仿真通过改变车辆操控、充电参数来产生反事实数据。

- design_requirement_cn：决策支持系统应同时包含数据分析模块与仿真模块，且仿真应能接受真实数据进行校准。

- artifact_choice_cn：搭建预测性分析模块（训练/测试切分、移动平均、距离加权空闲时间预测）和智能体仿真平台。

- evaluated_contrast_cn：纯自动驾驶燃油车 vs SAEV；不同|V|与|P|网格；敏感性案例。

- objective_result_cn：AV可缩减约48%车队；SAEV在约26–28个充电点后可满足当前需求。

##### evidence_pointers

1. Related work P6 theoretical motivation

2. Section 4.1–4.2

3. Table 3

4. Table 4

#### 2. 2

- theory_or_knowledge_claim_cn：FFCS需求高度时空异构，供需失衡需要通过车辆重定位缓解。

- mechanism_cn：有预测的空闲时间可以帮助决策者把闲置车提前移动到未来高需求区域，减少用户等待和请求拒绝。

- design_requirement_cn：重定位策略应先保证全区覆盖，再依据预测收益进行移动，且要避免无意义的长距离搬迁。

- artifact_choice_cn：重定位规则：优先覆盖未覆盖蜂窝；随后比较当前蜂窝与目标蜂窝预测空闲时间差并扣除旅行时间，仅当超过120分钟阈值时移动。

- evaluated_contrast_cn：不同车队规模下这套规则的效果，以及与理论下界的对比。

- objective_result_cn：简单规则即可使600辆车达到接近零拒绝，接近理论下界574。

##### evidence_pointers

1. Section 4.1 relocation rules

2. Eq. (1)

3. Table 3

#### 3. 3

- theory_or_knowledge_claim_cn：电动化带来的充电时间与续驶约束会占用车辆可用时间，降低车队有效供给。

- mechanism_cn：充电使车辆脱离可用车队；若充电点不足，车辆排队充电会转化为拒绝请求；但充电点超过某阈值后不再形成瓶颈。

- design_requirement_cn：仿真应能显式建模充电过程，并设置防止车辆中途断电的机制。

- artifact_choice_cn：空闲车辆电量低于50%时自动充电，行程结束后电量低于25%时仅允许充电；充电点功率设为11kW；电池50kWh，能耗15kWh/100km。

- evaluated_contrast_cn：在|V|=100到700和|P|=20到100的网格上比较错过率和等待时间。

- objective_result_cn：充电点影响在|P|=28后饱和；600辆车+28充电点利用率超55%。

##### evidence_pointers

1. Section 4.2 charging rules

2. Section 4.3 parameters

3. Table 4

4. Table 6

#### 4. 4

- theory_or_knowledge_claim_cn：FFCS用户对长时间等待高度敏感，约55%用户只接受最多15分钟等待。

- mechanism_cn：等待时间过长会损害服务可靠性和用户信心，因此服务评价不能只看拒绝率，还要看等待分布。

- design_requirement_cn：评价指标需要包含等待时间阈值，并选择保守的10分钟作为“良好服务”近似。

- artifact_choice_cn：以“超过10分钟等待的行程比例”作为第二性能指标。

- evaluated_contrast_cn：不同|V|×|P|组合下等待分布与错过率模式的一致性。

- objective_result_cn：等待时间超过10分钟比例与错过请求率呈现相似模式，充电点效果同样在28后饱和。

##### evidence_pointers

1. Section 4.3 second performance measure

2. Table 5

3. Fig. 4

## 评价逻辑

### evaluation_modes

1. 数据驱动的整体环境描述（描述性统计、理论下界）

2. 基于真实数据的智能体仿真实验（反事实参数网格）

3. 敏感性分析（战略布点、充电功率、需求规模、能耗）

4. 经济与政策反事实外推（成本节省、全城SAEV化估算）

- why_these_evaluations_cn：真实世界无法直接部署未成熟的SAEV系统，所以必须先以现有真实运营数据建立下限，再用仿真进行政策上可接受的反事实实验；二维参数网格用于同时分离车队规模与充电基础设施的影响；敏感性分析用来证明结论不是特定参数组合的偶然产物；政策和成本外推把仿真结果翻译成决策者能使用的语言。

- benchmark_and_contrast_chain_cn：原真实车队规模1104辆与理论并发下界574辆构成绝对参照；纯自动驾驶仿真把自动驾驶效应从电动化效应中剥离；SAEV仿真在V×P网格上检验电动化约束；不同敏感性案例（战略布点、加速充电、需求扩张、高能耗）再与基准表逐格对照，形成一个从现实基线→技术分离→约束引入→参数稳健性检验的累积证据链。

### claim_evidence_ledger

#### 1. 自动驾驶可使车队规模减半（约48%）。

- claim_cn：自动驾驶可使车队规模减半（约48%）。

- evidence_cn：真实数据中最大并发使用数为574；纯AV仿真中600辆车错过请求率为0.2%，700辆为0%。

- assessment_cn：该主张有较强支撑，但它是在不改变出行行为、不拼车的假设下成立的。

#### 2. 满足当前5700次/日行程仅需约30个充电点。

- claim_cn：满足当前5700次/日行程仅需约30个充电点。

- evidence_cn：SAEV仿真中|P|=26、|V|=700时零拒绝，|P|=28后增加充电点无改善，约28个充电点即可。

- assessment_cn：支撑充分，但仅针对该运营商和当前需求规模；全城外推依赖线性假设。

#### 3. 车队规模与充电基础设施之间存在约50:1的交换率。

- claim_cn：车队规模与充电基础设施之间存在约50:1的交换率。

- evidence_cn：Table 4中|P|=26,V=500与|P|=28,V=600均有约6%错过率，对角线模式支持该比率。

- assessment_cn：有表格支撑，但交换率只在特定服务水平和参数区间成立，不是普遍函数。

#### 4. 战略充电点布局相比随机布局改进有限。

- claim_cn：战略充电点布局相比随机布局改进有限。

- evidence_cn：Table 8相对Table 4仅最多约1.5%改进，仅|P|=26,V=600特殊组合有4.7%改进。

- assessment_cn：有直接敏感性证据；但布点算法较简单，更复杂优化可能带来更大改进。

#### 5. 需求扩张后结果按比例缩放，所需车队由峰值需求主导。

- claim_cn：需求扩张后结果按比例缩放，所需车队由峰值需求主导。

- evidence_cn：Appendix Tables 10–13显示将|V|和|P|等比放大后，错过率模式与基准类似。

- assessment_cn：支持线性缩放作为近似，但未直接模拟10倍以上需求与真实路网、充电排队等复杂交互。

#### 6. 整个柏林机动车出行若SAEV化可减少约77%车辆，需要约12,320充电点。

- claim_cn：整个柏林机动车出行若SAEV化可减少约77%车辆，需要约12,320充电点。

- evidence_cn：从28充电点/5700行程按440倍线性外推得到264,000辆车和12,320充电点；对比柏林约115万辆私家车。

- assessment_cn：这是讨论部分的外推而非仿真结果，依赖大量线性假设，属于提示性估计。

- internal_validity_strategy_cn：用训练/测试时间切分防止预测模块过拟合；用请求按真实时间顺序进入仿真，保持事件流真实性；首日仿真被排除以消除初始随机放置偏差；对同一系统使用统一指标并多参数交叉检验；通过敏感性分析观察参数变化是否改变核心模式。

- external_validity_strategy_cn：使用一座真实城市（柏林）的大规模运营商数据作为基础，而非人工生成数据；选择被调查支持的用户等待时间阈值；阐述平台模块化与开源特性，宣称可迁移至其他城市；用需求扩张敏感性测试来推断更大规模城市出行的适用性。

- what_is_not_actually_tested_cn：没有测试真实用户对SAEV的接受度、拼车意愿或目的地共享；没有测试充电非线性（超充曲线）、充电排队优化或充电中断策略；没有测试复杂路径优化与动态调度；没有真实路网微观交通效应；没有其他城市数据验证可迁移性；全城SAEV化只是线性外推，不是直接仿真。

## 贡献闭环

- technical_claim_cn：一个结合真实行程数据、预测性分析与智能体仿真的Python平台可以量化SAEV车队规模、充电点数量与服务水平的复杂关系，并给出可复现的敏感性分析。

- artifact_claim_cn：文章的可识别设计部分—特别是充电阈值规则、重定位预测规则和二维参数扫描—直接导致了“约28充电点饱和”和“车队近乎减半”的发现，而非简单宣称总体方法有效。

- mechanism_claim_cn：车队规模主要由早高峰和晚高峰的并发需求决定；充电基础设施在车少时不构成约束，在车多且充电点极少时构成约束，但该约束在约28个充电点后消失；充电点饱和后唯一改善方式仍是增加车队。

- boundary_claim_cn：发现基于柏林2016年某FFCS运营商的当前需求模式，假设用户行为不变、不拼车、车辆不主动提前接单且充电不中断；对其他城市、更大需求规模和行为变化需要进一步检验，但需求扩张敏感性提示关键机制（峰值需求驱动车队）可能具有稳定性。

- reusable_design_knowledge_cn：可复用的知识包括：数据驱动的反事实仿真平台可作为DSS核心组件；用真实历史请求作仿真输入、用预测性重定位规则代替复杂优化可接近理论性能下限；评价SAEV系统至少需要同时观察拒绝率和等待时间分布；车队规模与充电基础设施之间存在可识别的交换率，且充电点存在边际收益饱和点。

- theoretical_contribution_cn：将IS领域关于数据驱动DSS支持棘手问题的笼统论点具体化为一个可操作的“数据观察+仿真操纵”框架，并示范它如何在同一系统中同时处理共享经济、电动化、自动驾驶三种深层次变革的交互，从而扩展了关于可持续城市出行决策支持的理论叙事。

- how_discussion_closes_intro_gap_cn：引言提出决策者需要应对相互交织的充电设施、车队规模和供需平衡问题；讨论部分用仿真结果和敏感性分析直接回答了这些问题：车辆数可大幅减少、充电点需求低且有饱和点、峰值需求决定车队规模，从而把开头的“不能孤立分析”具体化为“系统整合分析”的可行性和价值。

- overclaim_or_unsupported_leaps_cn：最大跳跃是从单车企/当前需求到全柏林私人机动车出行需求的外推，其线性缩放假设未经过相同规模的仿真验证；另一个跳跃是把“简单算法”的仿真结果表述为接近理论极限，虽然与下界接近，但并未证明在其他更复杂路网条件下仍成立；此外，把充电点饱和点称为“基础设施阈值”可能被误解为对所有城市和所有运营商普适。

## 句级写作动作图谱

### 1. 摘要第一句

- order：1

- section：Abstract

- locator：摘要第一句

- move_code：CONTEXT

- paraphrase_cn：城市出行正同时经历共享经济、电动化和自动驾驶三方面根本转变。

- rhetorical_function_cn：在摘要开头建立宏观背景，让读者感到问题重要且具时代性。

- depends_on_cn：无，独立开篇。

- sets_up_cn：为提出DSS综合评估这三项变革做铺垫。

- evidence_pointer：Abstract S1

### 2. 摘要第二句

- order：2

- section：Abstract

- locator：摘要第二句

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：作者意在展示结合数据分析和仿真技术的决策支持系统在理解城市交通这类复杂系统中的价值。

- rhetorical_function_cn：明确论文目标不是单纯报告SAEV结果，而是展示方法价值。

- depends_on_cn：依赖背景句说明为什么要研究复杂系统。

- sets_up_cn：使读者预期方法—结果分离的论证结构。

- evidence_pointer：Abstract S2

### 3. 摘要第三句

- order：3

- section：Abstract

- locator：摘要第三句

- move_code：RESULT

- paraphrase_cn：以柏林为案例，共享自动驾驶电动车可在保持服务水平的同时大幅减少资源投入。

- rhetorical_function_cn：给出核心经验发现，吸引读者继续阅读。

- depends_on_cn：依赖第二句的方法目标。

- sets_up_cn：为摘要最后一句的利益相关者含义提供事实基础。

- evidence_pointer：Abstract S3

### 4. 摘要第四句

- order：4

- section：Abstract

- locator：摘要第四句

- move_code：PRACTICAL_STAKES

- paraphrase_cn：发现可帮助利益相关者权衡经济性与可持续性考虑，推动向可持续城市出行过渡。

- rhetorical_function_cn：把结果提升到实践决策层面，说明为什么值得发表。

- depends_on_cn：依赖第三句的仿真结果。

- sets_up_cn：暗示讨论部分将包含管理与政策含义。

- evidence_pointer：Abstract S4

### 5. 引言第1段前两句

- order：5

- section：Introduction

- locator：引言第1段前两句

- move_code：CONTEXT

- paraphrase_cn：过去十年共享经济深刻改变多个行业，预期收入将从2015年的150亿增长到2025年的3350亿美元。

- rhetorical_function_cn：用经济规模数据说明共享经济的重要性。

- depends_on_cn：无。

- sets_up_cn：引出后续对“共享”定义和转型方向的分析。

- evidence_pointer：Introduction P1 S1–S2

### 6. 引言第1段后半

- order：6

- section：Introduction

- locator：引言第1段后半

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：共享经济定义不清，日益被“使用权经济”概念替代，其核心是平台便利访问而非拥有资产。

- rhetorical_function_cn：引入概念框架，把共享经济聚焦到资产使用权上，为汽车共享做概念铺垫。

- depends_on_cn：建立于共享经济重要性的背景。

- sets_up_cn：让城市交通领域的汽车共享成为自然例证。

- evidence_pointer：Introduction P1 S3–S6

### 7. 引言第2段前两句

- order：7

- section：Introduction

- locator：引言第2段前两句

- move_code：PHENOMENON

- paraphrase_cn：城市交通是使用权经济转型的典型领域，并趋向共享出行；若规划得当可带来超越交通的多种好处。

- rhetorical_function_cn：从一般概念转向具体领域。

- depends_on_cn：依赖使用权经济定义。

- sets_up_cn：随后介绍Uber、Zipcar等具体现象。

- evidence_pointer：Introduction P2 S1–S2

### 8. 引言第2段后半

- order：8

- section：Introduction

- locator：引言第2段后半

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：自由浮动式汽车共享（FFCS）提供公共交通缺少的灵活性，与公共交通配合可成为私人拥车替代方案，尤其吸引年轻人。

- rhetorical_function_cn：建立FFCS作为研究背景，说明其已有的现实意义。

- depends_on_cn：依赖共享出行趋势的描述。

- sets_up_cn：为数据部分使用FFCS运营商数据提供合理性。

- evidence_pointer：Introduction P2 S3–S4

### 9. 引言第3段前两句

- order：9

- section：Introduction

- locator：引言第3段前两句

- move_code：PHENOMENON

- paraphrase_cn：近期研究开始关注共享车辆系统运营，但共享经济只是三大变革之一，另外两个是电动化和自动驾驶。

- rhetorical_function_cn：引入研究问题中的另外两个技术变革，并指出需要综合视角。

- depends_on_cn：建立于已介绍共享出行现象。

- sets_up_cn：为论文的整合分析目标做准备。

- evidence_pointer：Introduction P3 S1

### 10. 引言第3段后两句

- order：10

- section：Introduction

- locator：引言第3段后两句

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：电动车承诺零排放可对抗空气污染，自动驾驶则有望提高效率和安全性、减少拥堵并促进可持续。

- rhetorical_function_cn：分别说明电动化和自动驾驶的潜在价值。

- depends_on_cn：紧承三大变革的提出。

- sets_up_cn：后面讨论挑战时读者已了解其收益。

- evidence_pointer：Introduction P3 S2–S3

### 11. 引言第4段前两句

- order：11

- section：Introduction

- locator：引言第4段前两句

- move_code：PRACTICAL_STAKES

- paraphrase_cn：公共和私营决策者面临充电设施投资、共享系统供需平衡等挑战，但这些挑战不应孤立看待。

- rhetorical_function_cn：将技术发展转化为决策者现实困境，强调需要整合分析。

- depends_on_cn：依赖前面三项技术收益和挑战的并列。

- sets_up_cn：直接引出本文要探索的DSS方案。

- evidence_pointer：Introduction P4 S1–S2

### 12. 引言第4段第三句

- order：12

- section：Introduction

- locator：引言第4段第三句

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：作者探索能结合真实数据、分析技术和仿真方法的信息系统，以整合分析这些现象来支持决策。

- rhetorical_function_cn：明确研究目标：不是研究单一技术，而是研究DSS如何整合理解多个现象。

- depends_on_cn：依赖“挑战不应孤立看待”的问题定位。

- sets_up_cn：为后文的方法选择确定纲领。

- evidence_pointer：Introduction P4 S3

### 13. 引言第4段第四句

- order：13

- section：Introduction

- locator：引言第4段第四句

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：聚焦SAEV，研究自动驾驶对这些挑战的影响，以及共享和电动化约束如何反过来塑造自动驾驶对城市交通的影响。

- rhetorical_function_cn：把宽泛目标收缩为SAEV具体研究问题。

- depends_on_cn：依赖前一句“DSS整合分析”的目标。

- sets_up_cn：使后续仿真要回答“交互效应”变得明确。

- evidence_pointer：Introduction P4 S4

### 14. 引言第4段第五句

- order：14

- section：Introduction

- locator：引言第4段第五句

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：分析模块可预测未来供需模式，仿真平台可分析运营决策对可持续性和经济可行性的影响。

- rhetorical_function_cn：解释为什么选择“数据分析+仿真”的二元结构。

- depends_on_cn：依赖SAEV具体研究问题。

- sets_up_cn：为第4节模型逻辑提供高层说明。

- evidence_pointer：Introduction P4 S5

### 15. 引言第5段第一句

- order：15

- section：Introduction

- locator：引言第5段第一句

- move_code：RESULT

- paraphrase_cn：柏林结果显示自动驾驶可将汽车共享车队规模减少约一半。

- rhetorical_function_cn：在引言中给出最吸引眼球的结果。

- depends_on_cn：依赖前文提出的方法和目标。

- sets_up_cn：后面两句解释该结果的边界和扩展。

- evidence_pointer：Introduction P5 S1

### 16. 引言第5段第二句

- order：16

- section：Introduction

- locator：引言第5段第二句

- move_code：RESULT

- paraphrase_cn：该效应受早晚高峰限制，在加入电动化后仍存在；每天约5700次需求只需约30个充电点。

- rhetorical_function_cn：补充关键边界与第二个惊人结果。

- depends_on_cn：依赖第一句车队减半结果。

- sets_up_cn：为结论强调充电基础设施需求极低。

- evidence_pointer：Introduction P5 S2

### 17. 引言第5段第三句

- order：17

- section：Introduction

- locator：引言第5段第三句

- move_code：CONTRIBUTION

- paraphrase_cn：结果强调数据驱动DSS对环境可持续性的相关性，为可持续交通、充电设施投资和共享出行讨论提供见解。

- rhetorical_function_cn：把具体数据结果上升到一般贡献。

- depends_on_cn：依赖前两句结果。

- sets_up_cn：为摘要和讨论部分的贡献声明定下基调。

- evidence_pointer：Introduction P5 S3

### 18. 引言第5段第四句

- order：18

- section：Introduction

- locator：引言第5段第四句

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：对共享汽车运营商而言，结果展示了车队规模、充电点密度与服务水平之间的权衡。

- rhetorical_function_cn：限定结果面向的受众和适用维度，避免过度泛化。

- depends_on_cn：依赖第三句的一般贡献。

- sets_up_cn：为讨论部分的管理者建议做铺垫。

- evidence_pointer：Introduction P5 S4

### 19. 引言第6段

- order：19

- section：Introduction

- locator：引言第6段

- move_code：STUDY_OVERVIEW

- paraphrase_cn：预告随后章节：相关工作、数据集、方法、结果与敏感性分析、讨论和结论。

- rhetorical_function_cn：给出论文路线图，管理读者预期。

- depends_on_cn：无，通常固定出现在引言末尾。

- sets_up_cn：形成标准导航结构。

- evidence_pointer：Introduction P6

### 20. 相关文献第1段前两句

- order：20

- section：Related work

- locator：相关文献第1段前两句

- move_code：CONTEXT

- paraphrase_cn：IS社区近期重新聚焦如何通过研究应对复杂社会经济技术系统中的“棘手问题”。

- rhetorical_function_cn：把论文置于IS学科的更大学术对话中。

- depends_on_cn：无，但回应引言中的DSS目标。

- sets_up_cn：为讨论部分回扣“棘手问题”提供理论语境。

- evidence_pointer：Related work P1 S1–S2

### 21. 相关文献第1段后半

- order：21

- section：Related work

- locator：相关文献第1段后半

- move_code：PHENOMENON

- paraphrase_cn：可持续性问题本质上是棘手问题，城市环境又叠加了多层复杂社会技术系统，使其更加棘手。

- rhetorical_function_cn：把可持续城市出行归类为棘手问题，提升研究意义。

- depends_on_cn：依赖Ketter等人的定义。

- sets_up_cn：为论证DSS分析复杂系统的价值提供依据。

- evidence_pointer：Related work P1 S3–S4

### 22. 相关文献第1段末句

- order：22

- section：Related work

- locator：相关文献第1段末句

- move_code：STUDY_OVERVIEW

- paraphrase_cn：本节先概述城市交通三个根本变化，再讨论IS研究通过分析与仿真结合的数据驱动决策支持可做出的贡献。

- rhetorical_function_cn：预告相关工作的浏览路径。

- depends_on_cn：无。

- sets_up_cn：组织后续文献综述的展开。

- evidence_pointer：Related work P1 S5

### 23. 相关文献第2段前三句

- order：23

- section：Related work

- locator：相关文献第2段前三句

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：汽车共享会员数2010至2016年从120万增至1510万，车辆从3.2万增至15.7万；早期为站点式往返，后发展出单程站式。

- rhetorical_function_cn：用数字说明汽车共享规模增长和模式演变。

- depends_on_cn：无。

- sets_up_cn：为单程制运营复杂性研究做铺垫。

- evidence_pointer：Related work P2 S1–S3

### 24. 相关文献第2段后半

- order：24

- section：Related work

- locator：相关文献第2段后半

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：单程汽车共享因时空供需波动显著增加运营复杂度，已有随机混合整数规划、动态模型等研究。

- rhetorical_function_cn：梳理已有优化方法，指出FFCS领域已有运营研究。

- depends_on_cn：依赖汽车共享规模与模式演变。

- sets_up_cn：与后文FFCS重定位/充电问题连接。

- evidence_pointer：Related work P2 S4–S7

### 25. 相关文献第3段前两句

- order：25

- section：Related work

- locator：相关文献第3段前两句

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：自由浮动式汽车共享进一步加剧供需平衡挑战，需求由兴趣点驱动且随时间变化。

- rhetorical_function_cn：从站式转向自由浮动式，说明研究问题更复杂。

- depends_on_cn：依赖单程制运营复杂性的铺垫。

- sets_up_cn：为后续重定位策略文献做引子。

- evidence_pointer：Related work P3 S1–S2

### 26. 相关文献第4段前两句

- order：26

- section：Related work

- locator：相关文献第4段前两句

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：电动化是第二个重大变革，难点在于充电时间和续驶里程仍不如燃油车。

- rhetorical_function_cn：引入电动化的核心限制。

- depends_on_cn：无。

- sets_up_cn：为SAEV仿真中的充电约束提供背景。

- evidence_pointer：Related work P4 S1–S2

### 27. 相关文献第5段前两句

- order：27

- section：Related work

- locator：相关文献第5段前两句

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：自动驾驶汽车对共享系统的影响正成为增长中的研究领域；Alonso-Mora等人用纽约出租车数据发现拼车可大幅减少车队。

- rhetorical_function_cn：介绍AV共享系统研究的代表性结果。

- depends_on_cn：无。

- sets_up_cn：为说明本文聚焦不拼车情形提供对照。

- evidence_pointer：Related work P5 S1–S2

### 28. 相关文献第5段第三句

- order：28

- section：Related work

- locator：相关文献第5段第三句

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：因MERGE Greenwich显示城市居民拼车意愿较低，本文选择研究不拼车情形。

- rhetorical_function_cn：明确一个重要的假设边界：不拼车。

- depends_on_cn：依赖前述拼车研究结果。

- sets_up_cn：保护后续仿真结果不被误解为包含拼车效应。

- evidence_pointer：Related work P5 S3

### 29. 相关文献第5段末句

- order：29

- section：Related work

- locator：相关文献第5段末句

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：Chen和Loeb等已用人工数据在SAEV系统中研究投资决策与运营交互。

- rhetorical_function_cn：指出已有SAEV研究的局限：使用人工数据集。

- depends_on_cn：无。

- sets_up_cn：为本文使用真实数据提供差异化空间。

- evidence_pointer：Related work P5 S4

### 30. 相关文献第6段前两句

- order：30

- section：Related work

- locator：相关文献第6段前两句

- move_code：GAP

- paraphrase_cn：上述三种发展给决策者带来车队规模、车辆重定位和充电设施投资等战略运营挑战，这些方面需要大型投资。

- rhetorical_function_cn：归纳文献和现实中的未解决问题，尤其指出充电设施投资。

- depends_on_cn：依赖前述三支文献。

- sets_up_cn：为提出DSS方案和贡献声明提供缺口。

- evidence_pointer：Related work P6 S1–S2

### 31. 相关文献第6段中间

- order：31

- section：Related work

- locator：相关文献第6段中间

- move_code：THEORY_INTRO

- paraphrase_cn：数据驱动的决策支持系统正日益成为理解这类问题的方式，作者希望进一步理解数据驱动DSS如何帮助社会应对棘手问题。

- rhetorical_function_cn：引入一个方法论/理论动机，而不只是文献缺口。

- depends_on_cn：依赖IS界棘手问题讨论。

- sets_up_cn：为“数据+仿真”的底层理论提供入口。

- evidence_pointer：Related work P6 S3

### 32. 相关文献第6段后半

- order：32

- section：Related work

- locator：相关文献第6段后半

- move_code：THEORY_PROPOSITION

- paraphrase_cn：一方面，大数据能观察复杂系统交互而不必显式建模所有方面；另一方面，仿真能操纵环境并评估真实数据揭示的动态如何响应变化。

- rhetorical_function_cn：明确提出“数据观察+仿真操纵”理论命题，这是全文方法论的支点。

- depends_on_cn：依赖数据驱动DSS的讨论。

- sets_up_cn：为第4节平台设计提供理论合法性。

- evidence_pointer：Related work P6 S4–S5

### 33. 相关文献第7段前三句

- order：33

- section：Related work

- locator：相关文献第7段前三句

- move_code：CONTRIBUTION

- paraphrase_cn：本文在SAEV经济和环境研究上的延伸是：使用大型真实共享出行数据、开发可适应仿真框架、分析服务水平—车队—充电基础设施互动。

- rhetorical_function_cn：把文献缺口转化为具体贡献列表。

- depends_on_cn：依赖前述所有文献局限。

- sets_up_cn：为方法部分和结果部分的组织提供路线。

- evidence_pointer：Related work P7 S1–S3

### 34. 相关文献第7段后两句

- order：34

- section：Related work

- locator：相关文献第7段后两句

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：具体关注电动化约束能否被历史行程容纳、自动驾驶对车队缩减的贡献、以及两者如何交互。

- rhetorical_function_cn：把贡献进一步细化为三个可回答的问题。

- depends_on_cn：依赖贡献列表。

- sets_up_cn：直接对应结果部分5.1、5.2和敏感性分析。

- evidence_pointer：Related work P7 S4–S5

### 35. 数据节第1段前半

- order：35

- section：Data set and characteristics

- locator：数据节第1段前半

- move_code：PHENOMENON

- paraphrase_cn：数据来自柏林某FFCS运营商51天290,000次行程和1,104辆车，记录起终点、时间戳、油量和车辆ID。

- rhetorical_function_cn：说明实证基础：真实世界大规模运营数据。

- depends_on_cn：无，开始实证部分。

- sets_up_cn：为后文描述性统计和仿真输入做准备。

- evidence_pointer：Section 3 P1 S1–S2

### 36. 数据节Table 1附近

- order：36

- section：Data set and characteristics

- locator：数据节Table 1附近

- move_code：RESULT

- paraphrase_cn：描述性统计显示每车每天平均5.8次行程，平均空闲时间167.6分钟，平均行程时间80.1分钟，车辆闲置波动极大。

- rhetorical_function_cn：用表格证据展示利用率的低效和需求波动。

- depends_on_cn：依赖数据描述。

- sets_up_cn：为后文“车队过度供给”和“自动驾驶潜力”提供量化基础。

- evidence_pointer：Table 1

### 37. 数据节第5段

- order：37

- section：Data set and characteristics

- locator：数据节第5段

- move_code：MECHANISM

- paraphrase_cn：由于自动驾驶车能自行去接乘客，所需部署车辆的密度可降低，因此有望进一步缩减车队。

- rhetorical_function_cn：从数据观察过渡到机制解释，为什么自动驾驶能改善利用率。

- depends_on_cn：依赖利用率过低的统计结果。

- sets_up_cn：为纯AV仿真结果做理论预期。

- evidence_pointer：Section 3 P5 S2

### 38. 数据节第6段前两句

- order：38

- section：Data set and characteristics

- locator：数据节第6段前两句

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：在不拼车且不改变用户行为前提下，最大并发行程数构成服务所有请求所需车队规模的理论下界。

- rhetorical_function_cn：给出一个可检验的理论下界，成为后续结果的重要参照。

- depends_on_cn：依赖并发使用数统计。

- sets_up_cn：为结果部分强调仿真的车队缩减接近下界。

- evidence_pointer：Section 3 P6 S1

### 39. 数据节Fig.2附近

- order：39

- section：Data set and characteristics

- locator：数据节Fig.2附近

- move_code：RESULT

- paraphrase_cn：利用热图显示工作日有上午和傍晚两个高峰，周末下午出现高平台和傍晚小峰，这可能导致SAEV充电困难。

- rhetorical_function_cn：可视化和描述日内需求模式，识别对SAEV充电系统的挑战。

- depends_on_cn：依赖并发使用数和利用率的统计。

- sets_up_cn：为后续峰值需求驱动车队规模的结论提供证据。

- evidence_pointer：Fig. 2a, Fig. 2b, Table 2

### 40. 数据节第9段

- order：40

- section：Data set and characteristics

- locator：数据节第9段

- move_code：MECHANISM

- paraphrase_cn：数据中平均行程时长80分钟，即使全速行驶也在电动车续航范围内；较长租赁可能包含停车办事阶段，因此按全程耗电估计是保守的。

- rhetorical_function_cn：说明电动化的“续航”问题在本文数据环境中的严重性有限。

- depends_on_cn：依赖Table 1中行程时长统计。

- sets_up_cn：为后面说充电约束主要由充电时间而非里程导致做铺垫。

- evidence_pointer：Section 3 P9 S1–S3

### 41. 数据节末段

- order：41

- section：Data set and characteristics

- locator：数据节末段

- move_code：TRANSITION

- paraphrase_cn：然而，车队缩小和行程安排更密会使充电需求成为约束，因此需要建立智能体模型来理解这些互动。

- rhetorical_function_cn：总结数据部分并引出仿真模型。

- depends_on_cn：依赖前面关于电动车距离充足但充电可能限制的讨论。

- sets_up_cn：自然过渡到第4节模型。

- evidence_pointer：Section 3 P10

### 42. 第4节引言段

- order：42

- section：Model

- locator：第4节引言段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：智能体方法在分析一个主体行为影响其他主体的复杂系统方面有优势，因此适合城市交通网络。

- rhetorical_function_cn：为选择智能体建模提供方法论理由。

- depends_on_cn：无，但响应第2节理论动机。

- sets_up_cn：为后文智能体规则设计提供合法性。

- evidence_pointer：Section 4 P1

### 43. 第4节第2段后半

- order：43

- section：Model

- locator：第4节第2段后半

- move_code：DESIGN_FEATURE

- paraphrase_cn：因为通用仿真平台需要大量改造，作者决定开发模块化Python智能体模型，以保证可扩展、可复现和可迁移。

- rhetorical_function_cn：解释为什么不用现成平台，并展示制品设计决策。

- depends_on_cn：依赖智能体建模方法选择。

- sets_up_cn：为后续Request/Task/Update模块结构做预告。

- evidence_pointer：Section 4 P2 S4–S5

### 44. 第4.1节第3段

- order：44

- section：Model

- locator：第4.1节第3段

- move_code：REQUIREMENT

- paraphrase_cn：FFCS需求是即时实现的，运营商不知道未来需求，因此仿真必须加入需求预测分析模块以支持主动重定位和充电。

- rhetorical_function_cn：从运营现实推导出预测模块的必要性。

- depends_on_cn：依赖数据部分关于随机需求的描述。

- sets_up_cn：说明训练/测试切分和预测规则。

- evidence_pointer：Section 4.1 P3

### 45. 第4.1节第1段

- order：45

- section：Model

- locator：第4.1节第1段

- move_code：DESIGN_FEATURE

- paraphrase_cn：运营区被离散为蜂窝状小区，任意两点间行车时间最多5分钟，直径2公里。

- rhetorical_function_cn：定义仿真空间粒度，使重定位决策可行。

- depends_on_cn：无。

- sets_up_cn：为后文预测与重定位公式提供空间单位。

- evidence_pointer：Section 4.1 P1

### 46. 第4.1节第4段

- order：46

- section：Model

- locator：第4.1节第4段

- move_code：DESIGN_FEATURE

- paraphrase_cn：重定位规则优先让每个蜂窝至少有一辆空闲车，然后按预测空闲时间差扣除行程时间，只有超过120分钟阈值才移动。

- rhetorical_function_cn：给出核心重定位设计，平衡覆盖与预测收益。

- depends_on_cn：依赖预测分析模块。

- sets_up_cn：为敏感性分析和仿真结果提供算法基础。

- evidence_pointer：Section 4.1 P4, Eq. (1)

### 47. 第4.2节第1段

- order：47

- section：Model

- locator：第4.2节第1段

- move_code：DESIGN_FEATURE

- paraphrase_cn：仿真将观测期离散为1秒时间步，每个时间步依次执行请求、任务、更新三类独立模块。

- rhetorical_function_cn：描述仿真执行架构，便于复现。

- depends_on_cn：依赖前一节模型逻辑。

- sets_up_cn：为后文详细模块说明和结果输出做框架。

- evidence_pointer：Section 4.2 P1, Fig. 3

### 48. 第4.2节充电规则段

- order：48

- section：Model

- locator：第4.2节充电规则段

- move_code：DESIGN_FEATURE

- paraphrase_cn：空闲车电量低于50%时被派往最近充电桩充电直至充满；行程结束后电量低于25%时只允许去充电，防止中途耗尽。

- rhetorical_function_cn：定义充电决策规则，将电动化约束可操作化。

- depends_on_cn：依赖EV参数和模型逻辑。

- sets_up_cn：直接影响仿真中充电点是否成为瓶颈。

- evidence_pointer：Section 4.2 Task Module charging rules

### 49. 第4.3节参数段

- order：49

- section：Model

- locator：第4.3节参数段

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：根据数据中的下界设置车队规模从100到700，并基于每日总行驶里程和单桩日最大供电里程确定充电点网格范围。

- rhetorical_function_cn：说明参数范围和公式来源，使结果有实际锚点。

- depends_on_cn：依赖数据部分的理论下界。

- sets_up_cn：为结果部分的表格结构做准备。

- evidence_pointer：Section 4.3 P2

### 50. 第4.3节指标段

- order：50

- section：Model

- locator：第4.3节指标段

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：主要指标是错过请求率，可解读为服务水平；第二个指标是等待超过10分钟的比例，依据是用户调查中多数人最多接受15分钟。

- rhetorical_function_cn：给服务评价建立明确、可辩护的指标。

- depends_on_cn：依赖运营目标与用户调查证据。

- sets_up_cn：使表4和表5的解释有标准。

- evidence_pointer：Section 4.3 P3–P4

### 51. 第5节引言段

- order：51

- section：Results

- locator：第5节引言段

- move_code：STUDY_OVERVIEW

- paraphrase_cn：结果部分先报告纯AV情形，再报告SAEV，然后做敏感性分析。

- rhetorical_function_cn：预告结果结构，强调先分离后综合。

- depends_on_cn：无。

- sets_up_cn：管理读者对表3、表4和敏感性附录的预期。

- evidence_pointer：Section 5 P1

### 52. 第5.1节末段

- order：52

- section：Results

- locator：第5.1节末段

- move_code：RESULT

- paraphrase_cn：600辆及以上车辆很少或没有错过请求，这与数据推导的理论下界574辆吻合，意味着不充电约束下即使是简单重定位也能充分利用自动驾驶潜力。

- rhetorical_function_cn：报告纯AV核心结果并对照理论下界。

- depends_on_cn：依赖数据部分理论下界和仿真结果表3。

- sets_up_cn：为下一节加入电动化后的对比做前提。

- evidence_pointer：Section 5.1, Table 3

### 53. 第5.2节前段

- order：53

- section：Results

- locator：第5.2节前段

- move_code：RESULT

- paraphrase_cn：在车队规模为100和200时，车辆可用性是唯一约束，不同充电点数不影响服务；从300辆开始充电点形成约束，但28个充电点后增加充电点不再改变服务。

- rhetorical_function_cn：报告SAEV二维网格的核心模式：两个资源依次成为瓶颈。

- depends_on_cn：依赖表4数据。

- sets_up_cn：为定义实际相关星座和交换率提供事实依据。

- evidence_pointer：Section 5.2, Table 4

### 54. 第5.2节中段

- order：54

- section：Results

- locator：第5.2节中段

- move_code：RESULT

- paraphrase_cn：面向实践的相关区间是500至700辆车和26至30个充电桩；在26个充电桩和700辆车时零拒绝，车队可减少37%且服务不降。

- rhetorical_function_cn：从矩阵中提取最可操作的数字，给出主要结论。

- depends_on_cn：依赖表4矩阵。

- sets_up_cn：为讨论部分管理建议提供明确数字。

- evidence_pointer：Table 4 bold constellations

### 55. 第5.2节中段

- order：55

- section：Results

- locator：第5.2节中段

- move_code：RESULT

- paraphrase_cn：表4中的对角线模式显示500辆车配26个充电桩与600辆车配28个充电桩服务相近，说明车辆与充电桩的交换率约为50:1。

- rhetorical_function_cn：揭示投资权衡，为经济性讨论提供关键参数。

- depends_on_cn：依赖表4。

- sets_up_cn：为讨论中车队规模增加或充电点投资的选择提供论据。

- evidence_pointer：Section 5.2 exchange rate paragraph

### 56. 第5.2节末段

- order：56

- section：Results

- locator：第5.2节末段

- move_code：RESULT

- paraphrase_cn：等待时间超过10分钟的比例与错过率呈现类似模式；闲置率数据表明SAEV可把利用率提高到55%以上，其中重定位时间占比很小。

- rhetorical_function_cn：证明多个服务指标的结论一致，并展示资源效率改进。

- depends_on_cn：依赖表5、表6和图4。

- sets_up_cn：为“可持续性资源效率”贡献提供证据。

- evidence_pointer：Section 5.2, Table 5, Table 6, Fig. 4

### 57. 第5.3节前段

- order：57

- section：Results

- locator：第5.3节前段

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：战略布点充电桩与随机布点相比总体结果相近，最多减少1.5%错过率，但在特定组合可带来4.7个百分点的改进。

- rhetorical_function_cn：用敏感性测试说明核心结论对布局方式不敏感。

- depends_on_cn：依赖基准仿真和训练数据能量需求。

- sets_up_cn：增强结果外部有效性。

- evidence_pointer：Section 5.3 Strategic positioning, Table 8

### 58. 第5.3节末段

- order：58

- section：Results

- locator：第5.3节末段

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：在等比调整后，加速充电、需求扩张和高能耗情形的模式与基准类似，说明系统需要适当车队和最低限充电设施，车队规模主要由峰值需求驱动。

- rhetorical_function_cn：总结敏感性分析，提炼跨情境稳定的机制。

- depends_on_cn：依赖附录各表。

- sets_up_cn：为讨论中的线性外推和机制陈述提供根据。

- evidence_pointer：Section 5.3, Appendix Tables 9–14

### 59. 第6.1节第一段

- order：59

- section：Discussion

- locator：第6.1节第一段

- move_code：CONTRIBUTION

- paraphrase_cn：研究结果支持政策制定者和管理者在技术、车队和充电设施投资决策中获得定量论据。

- rhetorical_function_cn：把仿真结果回接到管理者/政策制定者场景。

- depends_on_cn：依赖所有仿真和敏感性结果。

- sets_up_cn：为后续成本节省和政策外推定调。

- evidence_pointer：Section 6.1 P1

### 60. 第6.1节第二段

- order：60

- section：Discussion

- locator：第6.1节第二段

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：虽然展示的是柏林案例，但文章称仿真平台开放、可迁移到其他城市。

- rhetorical_function_cn：说明案例的可推广性边界，防止被视作唯一案例。

- depends_on_cn：依赖平台模块化的设计选择。

- sets_up_cn：为“方法贡献而非单城市结论”定位。

- evidence_pointer：Section 6.1 P2

### 61. 第6.1节第三段

- order：61

- section：Discussion

- locator：第6.1节第三段

- move_code：PRACTICAL_STAKES

- paraphrase_cn：对像柏林这样的运营商，自动驾驶让车队减少约400辆，按每月200美元租赁估算每年节省约96万美元。

- rhetorical_function_cn：用量化的成本节省使结果对管理者有直接吸引力。

- depends_on_cn：依赖车队减少数和服务水平结果。

- sets_up_cn：强化经济可行性叙事。

- evidence_pointer：Section 6.1 P3

### 62. 第6.1节第四段

- order：62

- section：Discussion

- locator：第6.1节第四段

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：用柏林出行统计线性外推，全城机动车出行若SAEV化需约264,000辆车和12,320个充电点，相比现有115万辆车可减少77%。

- rhetorical_function_cn：展示更宏大的政策含义，但明确承认只是粗略近似。

- depends_on_cn：依赖敏感性分析中的线性缩放假设。

- sets_up_cn：为讨论基础设施投资“鸡生蛋”问题提供定量视角。

- evidence_pointer：Section 6.1 P4

### 63. 第6.2节第一段

- order：63

- section：Discussion

- locator：第6.2节第一段

- move_code：THEORY_RETURN

- paraphrase_cn：文章重新指出，结合分析和仿真的数据驱动DSS是应对气候变化、贫困等棘手问题的有力工具。

- rhetorical_function_cn：把具体SAEV结果放回IS学科一般理论问题中。

- depends_on_cn：依赖相关文献中的理论动机。

- sets_up_cn：完成引言和理论部分的闭环。

- evidence_pointer：Section 6.2 P1

### 64. 第6.2段后续

- order：64

- section：Discussion

- locator：第6.2段后续

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：未来研究可扩展数据来源、改进预测与优化算法、引入请求排队、充电中断、拼车行为，并研究SAEV与能源系统及社会公平的交互。

- rhetorical_function_cn：交代未竟问题和边界，降低读者对简单化的批评。

- depends_on_cn：依赖论文简约模型设定。

- sets_up_cn：结束全文并展示研究纲领。

- evidence_pointer：Section 6.2 P2–P6

## 写作技术

- gap_construction_cn：先承认已有研究分别处理汽车共享运营、电动车充电和自动驾驶，然后指出这些研究大多只针对单一技术或使用人工数据，缺少在同一系统中评估三者交互的决策支持工具；最后用“挑战不应在真空中看待”来收束缺口。

- signposting_cn：引言末尾给出章节路线图；相关文献开头预告“先三变革后IS贡献”的节点；数据段末反复强调“我们将在下一节用智能体模型分析”；结果部分开头先说明从AV到SAEV再到敏感性分析的顺序；讨论部分再次回到开头的棘手问题和DSS。

- transition_logic_cn：数据部分用“充电需求可能成为新约束”过渡到模型；模型部分用“平台构建完成即可分别评测”过渡到结果；结果部分用“当加入电动化后结果变得更细致”由AV过渡到SAEV；用“为排除参数巧合”由基准过渡到敏感性；讨论部分用“对管理者与政策制定者意味着什么”由结果过渡到含义。

- claim_evidence_rhythm_cn：每个主要主张几乎紧接表格：理论下界在数据部分建立，纯AV结果立即用表3支撑；SAEV网格结论直接指向表4；交换率直接从表4对角线读取；利用率改进用表6和具体600/28示例支撑；敏感性结果用表8和附录各表支撑。

- benchmark_narrative_cn：benchmark不是与其他算法对比，而是三层对照：真实车队规模与理论下界构成绝对锚点；纯AV仿真构成“未电动化”的反事实对照；参数网格和敏感性案例构成相对对照。文章把这种对照叙述为“分离效应—综合约束—稳健性检验”的证据链。

- theory_return_cn：在讨论的研究含义中，作者回到开头的“棘手问题”框架，把SAEV案例表述为“数据驱动DSS如何帮助应对棘手问题”的实例，从而把本研究的贡献从城市交通扩展到一般IS可持续性问题。

- contribution_positioning_cn：把贡献分成数据基础、仿真框架和互动分析三块，避免只声称“我们建了个模型”；在贡献列表中反复强调“真实数据”“可适应框架”“交互分析”，分别对应文献缺口中的三个不足。

- novelty_protection_cn：通过敏感性分析把结果的稳健性展示出来，使贡献不只是特定柏林数据的偶然输出；通过开放平台和模块化宣称方法可迁移；通过讨论未来扩展把当前结果定位为持续研究的第一步，而不是一次性性能报告。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：用现实世界现象和决策者困境开场，引入三到四个宏观趋势，铺陈背景和利害关系。

- research_job_cn：找到一组相互交织的社会技术问题，并指出单个研究视角的不足。

- required_evidence_cn：至少要有文献或行业数据说明每个趋势的现实重要性，并说明它们不能孤立分析。

- transition_to_next_cn：用“挑战不应被孤立看待”过渡到需要一种DSS或综合方法。

#### 2. 2

- step：2

- writing_job_cn：综述相关文献，梳理各单线研究的成熟点，明确指出缺少综合视角或真实数据支撑。

- research_job_cn：确认具体缺口：缺真实数据、缺可操纵复杂系统的工具、缺多因素互动分析。

- required_evidence_cn：相关研究列表以及它们之间无法直接回答核心问题的缺口说明。

- transition_to_next_cn：用“因此本文在三个方向上扩展现有研究”引出贡献和问题清单。

#### 3. 3

- step：3

- writing_job_cn：描述数据来源、规模、关键统计和可视化，提炼一个可供后续仿真的理论下界或基线。

- research_job_cn：获取真实运营或平台数据，计算基本统计、时空模式、理论下限。

- required_evidence_cn：数据规模、字段说明、关键描述性统计、峰值需求或下限值。

- transition_to_next_cn：用“但这些模式无法直接回答反事实问题，因此需要仿真模型”引出方法。

#### 4. 4

- step：4

- writing_job_cn：解释建模方法选择，给出可复现的模型逻辑、规则公式和评价指标，说明为什么这些设计选择合理。

- research_job_cn：构建能使用真实数据并允许反事实参数调整的仿真或计算模型。

- required_evidence_cn：模型架构、核心公式/伪代码、参数来源、指标定义和用户/文献依据。

- transition_to_next_cn：用“平台构建完成后，先报告简单情形，再报告复杂情形”预告结果。

#### 5. 5

- step：5

- writing_job_cn：按“先简单情形后复杂情形”报告结果；用表格矩阵展示关键参数空间的交互效应，并从中提取可操作区间和交换率。

- research_job_cn：运行多组仿真/实验，至少包括基准对照、多因素网格和必要的中间隔离实验。

- required_evidence_cn：结果表格、与基线/下界对比、瓶颈转移的证据、交换率或饱和点。

- transition_to_next_cn：用“为排除参数偶然性，我们进行多种敏感性分析”引出稳健性检验。

#### 6. 6

- step：6

- writing_job_cn：用敏感性分析证明核心模式不依赖特定参数；再进入讨论，把结果翻译为运营成本、政策投资和理论含义，并明确边界和未来方向。

- research_job_cn：设计有意义的敏感性案例；估算经济和政策外推；识别哪些结果可泛化、哪些不能。

- required_evidence_cn：敏感性结果表、外推计算、对边界条件和未来研究的清晰说明。

- transition_to_next_cn：最后回到开头的宏观问题或理论框架，形成闭环。

### most_transferable_moves_cn

1. 用一个可辩护的理论下界（如最大并发需求）作为结果锚点，可大幅增强仿真/实验结果的解释力。

2. 在多因素仿真中采用二维参数网格，并识别“瓶颈转移”和“饱和点”，让结果更可操作。

3. 把多种指标（拒绝率、等待时间、利用率）并列呈现，若模式一致则主张更可信。

4. 用敏感性分析作为统计显著性的替代，因为仿真实验很难做传统假设检验。

5. 在结果里先展示“技术分离”情形（如不加新约束），再展示“综合”情形，便于读者理解交互效应。

### resource_intensive_or_nonstandard_parts_cn

1. 需要大规模真实运营数据（290,000次行程、1104辆车、51天），并非所有研究者可获得。

2. 长期仿真运行：单次运行约24小时，多参数网格和多个敏感性案例的计算资源需求很高。

3. 需要将城市运营区离散化并接入OSRM路由服务，涉及地图基础和空间计算。

4. 若没有真实充电桩位置和运营商业务区域数据，难以复现这种“真实数据驱动”的评价。

### what_not_to_copy_superficially_cn

1. 只复制“数据分析+仿真”的口号而没有真实数据输入，不能支撑任何政策结论。

2. 只做参数网格而不先建立理论下界或基线，结果会显得无锚点、难以解释重要性。

3. 只报告错过率而不用等待时间等第二指标，可能被质疑评价不足。

4. 没有敏感性分析就把案例结果推广到全城/其他城市，很容易被评审和读者视为过度外推。

- single_best_description_of_the_routine_cn：先用真实运营数据算出当前系统的瓶颈和下界，再据此构建一个模块化仿真器做多因素反事实实验，再用敏感性分析证明数字的稳健性，最后把稳健数字翻译成决策者能用的成本、投资和权衡结论。

## 分析边界

全文以PDF转换文本和表格为基础，图表中的某些图像细节（如热力图具体灰度分布）无法直接读取，但关键表格和文字说明完整；定位使用章节和段落而非精确页码；由于没有补充材料，无法核实仿真代码和完整参数输出；结论部分的外推是否过度依赖作者线性假设已做标注。
