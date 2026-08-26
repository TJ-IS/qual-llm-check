# ForeSim-BI: A predictive analytics decision support tool for capacity planning

- 作者：Duarte Dinis; Ângelo Palos Teixeira; Ana Barbosa-Póvoa
- 年份 / 期刊：2020 / Decision Support Systems
- DOI：10.1016/j.dss.2020.113266
- 源文件：09376_2020_foresim-bi-a-predictive-analytics-decision-support-tool-for-capacity-planning.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：performance_gap_artifact_benchmark_generalize
- 置信度：0.8

## 文章级论证概况

- 核心问题：如何为复杂产品系统的维修组织构建一个预测性分析决策支持工具，使其能够预测未来及前所未见维修检查的工作负荷、在观测到达后更新预测，并将预测转化为可执行的容量计划？

- 制品与设计：ForeSim-BI：一个集成四个模块的决策支持工具，包括基于乘法误差状态空间Holt-Winters模型的预测模块、基于贝叶斯推断的预测更新模块、基于蒙特卡洛模拟与自助抽样的工作负荷分解模块，以及用贝叶斯网络结合历史与模拟数据并用线性规划模型自动选择工作负荷区间的决策模块。工具使用葡萄牙某飞机维修组织的171个维修项目数据开发，并针对8C检查进行验证。

- 客观结果：在三次实际观测中，ForeSim-BI对8C检查总工作负荷的百分比误差分别为13%、0%和0%；各工作负荷变量的MAE总体呈下降趋势；与模拟现行工程估计的基线相比，总工作负荷平均误差为+245人时，而工程估计为-917人时，显示前者显著更准确并具有成本节约潜力。

- 核心贡献：作者声称的主要贡献是提出并验证了一个将预测、贝叶斯更新、仿真和概率推理整合为单一决策支持工具的方案，填补了维护容量规划文献中忽视工作负荷不确定性、时间演化、信息更新以及多维度工作负荷刻画之间组合的缺口；该工具能基于历史数据和新增观测自动产生比行业现行判断性估计更准确的容量计划。

- 整篇论证链：论文从维修容量规划的实际重要性出发，指出现有行业做法主要依赖判断性估计和简单回归，而现有容量规划文献不处理工作负荷不确定性及时间演化，现有预测文献不处理信息更新和工作负荷多维刻画。为了填补这一双重缺口，作者在葡萄牙飞机维修组织的真实数据基础上构建ForeSim-BI：先检验总工作负荷服从对数正态分布，为概率建模提供基础；再用AICc选择Holt-Winters预测模型生成先验预测；随后用贝叶斯推断将先验预测更新为随观测到达而更新的预测分布；接着用蒙特卡洛与自助抽样将总工作负荷分解为工作类型、工作阶段和技能三个维度；最后用贝叶斯网络结合历史与模拟数据，并通过线性规划自动选出满足合计约束的工作负荷区间。论文用同一8C检查的三次真实观测验证工具精度，并构造模拟现行工程估计的基线模型进行对比，最终证明工具误差更低、能避免系统性的低估，并据此估算成本节约。

## 类型与写作弧线判定

- 论文主类型判定：文章按设计科学路线展开：先识别实践中的性能缺口，再构建一个由多个模块组成的决策支持工具，并在真实维修组织的数据上通过真实观测和行业基线进行评价。它不检验某个行为或组织理论，也不以benchmark竞赛为主要贡献，而是以制品构建和现场数据验证为核心的DSS研究。

- 主导写作弧线判定：论文的主线是：揭示MRO容量规划中预测不准确的性能缺口，构建ForeSim-BI制品，以真实数据与模拟现行实践的基线进行benchmark，最后将结果提升为面向复杂产品系统维修容量规划的一般性设计知识。

## 研究开展程序

- study_or_phase_count：7

- 研究阶段总序列：论文分为七个相继累积的阶段：数据与分布假设检验为概率建模提供基础；预测模型选择生成先验工作负荷预测；贝叶斯推断模块使预测能随观测更新；仿真模块将总工作负荷分解为管理相关变量；贝叶斯网络与线性规划模块将概率推断转化为可执行的容量区间；随后在同一8C检查的三次真实观测上验证工具；最后与模拟行业现行工程估计的基线比较并估算成本价值。

### studies_or_phases

#### 1. 维修数据收集与对数正态分布假设检验

- order：1

- name_cn：维修数据收集与对数正态分布假设检验

- question_cn：各类型C检查的总工作负荷是否可以用对数正态分布描述？

- inputs_and_setting_cn：葡萄牙某飞机维修组织收集的171个飞机维修项目，包含C至8C检查的总工作负荷及按工作类型、阶段、技能分类的人时数据。

- designed_or_compared_object_cn：未设计制品；检验对数正态分布这一随机变量模型。

- baseline_control_or_counterfactual_cn：零假设为样本来自对数正态分布；用Kolmogorov-Smirnov检验。

##### objective_metrics

1. K-S统计量D

2. p值

- analysis_method_cn：Kolmogorov-Smirnov拟合优度检验。

- main_result_cn：所有C至7C检查样本的p值均大于0.05，不能拒绝对数正态分布假设。

- argumentative_role_cn：为后续预测模块、贝叶斯更新和蒙特卡洛仿真提供总工作负荷的概率分布基础。

- remaining_uncertainty_cn：样本量小且来自单一维修组织；只检验了总工作负荷，未检验各分解变量。

- link_to_next_phase_cn：对数正态分布假设使预测模块可以输出均值和方差，进而形成概率分布。

##### evidence_pointers

1. Section 2.2.2

2. Table 2

#### 2. 预测模块的指数平滑模型选择

- order：2

- name_cn：预测模块的指数平滑模型选择

- question_cn：在指数平滑族中，哪个状态空间模型最适合用历史C检查样本均值预测未来C检查总工作负荷？

- inputs_and_setting_cn：从C到7C检查样本均值构成的时间序列。

- designed_or_compared_object_cn：乘法误差状态空间形式的简单指数平滑、Holt线性方法、加法Holt-Winters和乘法Holt-Winters。

- baseline_control_or_counterfactual_cn：以SES、HLM、MHW作为AHW的对照模型。

##### objective_metrics

1. AICc

2. MSE

- analysis_method_cn：通过最小化MSE估计平滑参数，再用AICc进行小样本模型选择。

- main_result_cn：AHW的AICc最低，为-4.51，因此被选为预测模块。

- argumentative_role_cn：为工具提供未来及前所未见检查的先验总工作负荷预测分布。

- remaining_uncertainty_cn：只在指数平滑族内比较，未考虑ARIMA、机器学习等替代模型。

- link_to_next_phase_cn：预测模块输出的均值和方差被转化为对数正态分布参数，供贝叶斯推断模块使用。

##### evidence_pointers

1. Section 3.1

2. Table 3

#### 3. 贝叶斯推断模块与预测更新机制

- order：3

- name_cn：贝叶斯推断模块与预测更新机制

- question_cn：当被预测维修检查的新观测到达后，如何将先验预测更新为预测性预测？

- inputs_and_setting_cn：由预测模块得到的先验均值和方差；历史数据得到的参数变异系数；被预测检查的新观测值。

- designed_or_compared_object_cn：设计贝叶斯更新规则：以对数正态分布的λ参数为待更新量，假设正态共轭先验，推导后验与预测分布。

- baseline_control_or_counterfactual_cn：与经典频率派将参数视为固定常数的做法相对照。

##### objective_metrics

1. 后验均值与标准差

2. 预测分布的均值与标准差

- analysis_method_cn：贝叶斯公式与共轭分布推导，结合五步更新程序。

- main_result_cn：预测性分布仍为对数正态分布，且其参数可通过观测值直接更新。

- argumentative_role_cn：赋予工具随信息到达而自动修正预测的能力，这是论文声称的重要创新之一。

- remaining_uncertainty_cn：依赖对数正态与正态共轭假设；未单独检验该模块，需结合整体工具验证。

- link_to_next_phase_cn：更新后的预测分布进入仿真模块，以生成总工作负荷和其他分解变量的随机值。

##### evidence_pointers

1. Section 3.2.1

2. Eqs. (13)-(24)

3. Fig. 2

#### 4. 仿真模块与自助抽样阈值校准

- order：4

- name_cn：仿真模块与自助抽样阈值校准

- question_cn：如何将总工作负荷分解为工作类型、阶段和技能等管理相关变量，并确定哪些变量应与总工作负荷联动？

- inputs_and_setting_cn：预测分布生成的总工作负荷随机值；历史或新观测的各项工作负荷变量样本。

- designed_or_compared_object_cn：设计蒙特卡洛仿真与自助抽样过程，并以相关系数阈值rcut决定是否按总工作负荷缩放变量。

- baseline_control_or_counterfactual_cn：比较rcut=0、0.3、0.5、0.7四种阈值，其中rcut=0等价于不缩放。

##### objective_metrics

1. MAE

2. MAPE

- analysis_method_cn：用工具对8C检查进行估计，并与实际观测比较，计算MAE和MAPE。

- main_result_cn：rcut=0.5在三次估计中获得最低或接近最低的MAE/MAPE，因此被采用。

- argumentative_role_cn：确定工作负荷分解的仿真参数，使预测不仅限于总人时，还能细化到容量规划所需的具体类别。

- remaining_uncertainty_cn：自助抽样只从相同检查类型样本中重抽样；未探索贝叶斯或参数化分解方法。

- link_to_next_phase_cn：仿真生成的大量模拟维修检查被加载到贝叶斯网络模块中，与历史数据结合。

##### evidence_pointers

1. Section 3.3.2

2. Table 4

3. Fig. 3

#### 5. 贝叶斯网络模块与线性规划区间选择

- order：5

- name_cn：贝叶斯网络模块与线性规划区间选择

- question_cn：给定总工作负荷区间后，如何自动选出各工作负荷变量的区间，使其合计等于计划总量且概率最高？

- inputs_and_setting_cn：历史数据与仿真生成的模拟维修检查；按工作类型、阶段、技能分别建立的贝叶斯网络。

- designed_or_compared_object_cn：设计100人时区间的贝叶斯网络，并构建两阶段0-1线性规划模型来选择区间。

- baseline_control_or_counterfactual_cn：与之前工作中的500人时区间及人工区间选择方式对比。

##### objective_metrics

1. 区间合计等于总工作负荷的约束满足

2. 所选区间的累计概率

3. 区间概率最大化

- analysis_method_cn：贝叶斯网络概率推断与线性规划求解。

- main_result_cn：LP模型第一阶段选择最低的总工作负荷区间并满足90%累计概率；第二阶段在总工作负荷约束下最大化各变量区间概率之和。

- argumentative_role_cn：把概率分布转化为自动化、可执行的容量计划，避免人工选择导致的繁琐与次优。

- remaining_uncertainty_cn：区间离散化会带来误差；更小区间或连续条件概率未被实现。

- link_to_next_phase_cn：该模块为验证阶段提供可直接与实际观测比较的预测区间上界。

##### evidence_pointers

1. Section 3.4.1-3.4.2

2. Eqs. (32)-(39)

3. Fig. 4

4. Fig. 5

#### 6. ForeSim-BI在8C检查三次真实观测上的精度验证

- order：6

- name_cn：ForeSim-BI在8C检查三次真实观测上的精度验证

- question_cn：ForeSim-BI在预测同一8C检查的总工作负荷及分解变量时，随观测到达其误差如何变化？

- inputs_and_setting_cn：8C检查的三次实际观测值，以及ForeSim-BI在各阶段输出的预测区间。

- designed_or_compared_object_cn：比较同一工具在第一次、第二次、第三次观测时的预测表现。

- baseline_control_or_counterfactual_cn：以真实观测值D作为金标准。

##### objective_metrics

1. PE

2. MAE

3. MAPE

- analysis_method_cn：计算预测值F与观测值D的误差、百分比误差及汇总指标。

- main_result_cn：总工作负荷PE从第一次观测的13%降至第二、三次观测的0%；所有变量的MAE总体呈下降趋势；但个别工作类型、阶段和技能变量仍有较大误差。

- argumentative_role_cn：证明贝叶斯更新和自助抽样机制在真实数据上有效，并展示工具随信息增加的改善轨迹。

- remaining_uncertainty_cn：仅针对一个8C检查；部分变量误差仍大；MAPE因极大百分比误差而不适用。

- link_to_next_phase_cn：以相同预测场景引入模拟现行工程估计的基线，比较两种方法。

##### evidence_pointers

1. Section 3.5.1

2. Table 5

#### 7. 与模拟现行工程估计的基线对比及成本估算

- order：7

- name_cn：与模拟现行工程估计的基线对比及成本估算

- question_cn：ForeSim-BI是否比MRO行业当前的预测实践更准确，并能带来成本价值？

- inputs_and_setting_cn：同一8C检查的三个观测；用简单线性回归和观测均值构成的工程估计模型；ForeSim-BI输出。

- designed_or_compared_object_cn：ForeSim-BI与模拟现行工程估计的预测模型。

- baseline_control_or_counterfactual_cn：以模拟现行行业实践作为基准。

##### objective_metrics

1. PE

2. MAE

3. MAPE

4. 三次观测平均误差

5. 成本影响百分比

- analysis_method_cn：对比两方法在同一观测上的误差，计算平均误差，并基于葡萄牙劳动法加班费率估算成本影响。

- main_result_cn：ForeSim-BI的总工作负荷误差显著更低，现行工程估计系统性地低估工作负荷；ForeSim-BI平均高估245人时，工程估计平均低估917人时；按加班费率估算可节省约6%的单项目成本。

- argumentative_role_cn：从技术精度上升到管理绩效，证明工具相对行业现状的实际优势。

- remaining_uncertainty_cn：成本估算基于假设而非实际财务数据；工程估计模型是对行业实践的简化。

- link_to_next_phase_cn：结论部分据此总结设计知识、局限和未来研究方向。

##### evidence_pointers

1. Section 3.5.2

2. Table 6

3. Table 7

4. Fig. 6

## 各部分修辞架构

### abstract_moves

1. 先提出论文核心制品与目标领域

2. 指出要解决的实践问题

3. 概述四个模块构成的制品

4. 预告真实数据与对比验证方式

5. 用准确性和成本节约主张收束

### introduction_moves

1. 从容量规划重要性进入MRO场景

2. 区分计划内与计划外维修的不确定性

3. 综述确定性/随机性容量规划方法

4. 指出现有组织仍依赖判断性预测和简单回归

5. 通过引文说明MRO数据充足但未被充分利用

6. 提出ForeSim-BI并给出动机

7. 用两条文献缺口支撑创新性

8. 预告验证策略与文章结构

### theory_and_knowledge_moves

1. 引入对数正态分布作为总工作负荷模型

2. 用K-S检验支持该假设

3. 引入乘法误差状态空间指数平滑理论

4. 用AICc进行模型选择

5. 解释贝叶斯推断相对于频率派的优势

6. 利用共轭先验简化后验推导

7. 引入蒙特卡洛与自助抽样思想

8. 引入贝叶斯网络与EM学习机制

### artifact_design_moves

1. 将预测模块设计为先验分布生成器

2. 将贝叶斯推断模块设计为预测更新器

3. 按专家输入定义三类工作负荷随机变量

4. 用互斥且完备约束保证分解变量合计为总工作负荷

5. 用相关系数阈值决定变量是否随总负荷缩放

6. 用贝叶斯网络连接总工作负荷与分解变量

7. 用LP模型自动化区间选择

### evaluation_moves

1. 用K-S检验建立分布假设依据

2. 用AICc比较四个指数平滑模型

3. 用同一8C检查真实观测校准rcut

4. 用三次观测展示贝叶斯更新的动态精度

5. 用模拟工程估计建立行业基线

6. 用平均误差和加班成本将误差转化为财务影响

### discussion_and_contribution_moves

1. 在结论中重述工具模块与预测能力

2. 强调总工作负荷误差降至0%这一关键证据

3. 重申相对现行实践的优越性

4. 列出未来研究以保护贡献边界

5. 将工具定位为利用历史与新增观测改进MRO决策的预测性分析工具

## 理论/知识到设计的翻译

### 知识/理论基础

1. 指数平滑状态空间预测理论

2. 贝叶斯推断与共轭先验

3. 对数正态分布维修时间建模

4. 蒙特卡洛模拟与自助抽样

5. 贝叶斯网络概率推理

6. 线性规划

- 理论—设计耦合：partial

- 耦合判定理由：贝叶斯推断、预测分布更新和状态空间预测等知识基础确实直接塑造了部分模块，但模型中多个关键技术选择来自AICc数据驱动筛选、行业专家输入和工程启发式，而非由统一理论前瞻性决定。因此属于部分耦合。

- 理论到设计翻译链：维修工作负荷由确定性计划内任务和随机性计划外任务组成且随时间退化增长 → 需要概率型而非点值预测 → 采用对数正态分布和状态空间指数平滑输出均值与方差 → 新观测到来时应更新知识 → 用贝叶斯共轭推断形成预测分布 → 仅有总人时不足以制定容量计划 → 按专家定义的工作类型/阶段/技能三类变量进行自助抽样分解 → 分解变量需合计为总工作负荷 → 用相关系数阈值决定缩放 → 需要同时利用历史与模拟数据 → 用贝叶斯网络推断区间概率 → 区间选择需满足合计约束且概率最大 → 用LP模型自动求解。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：维修总工作负荷具有确定性+随机性成分，呈左偏且严格为正，可用对数正态分布描述

- mechanism_cn：工作负荷作为处理时间具有右偏分布，适合用对数正态随机变量建模

- design_requirement_cn：预测模块应输出概率分布而非单点值

- artifact_choice_cn：K-S检验后采用对数正态分布作为总工作负荷分布；AHW状态空间模型输出均值和方差

- evaluated_contrast_cn：对数正态假设与样本经验分布对比；AHW与SES/HLM/MHW对比

- objective_result_cn：所有C至7C检查均不能拒绝对数正态假设；AHW的AICc最低

##### evidence_pointers

1. Section 2.2.2, Table 2

2. Section 3.1, Table 3

#### 2. 2

- theory_or_knowledge_claim_cn：贝叶斯推断允许将参数视为随机变量，并用新观测更新先验分布

- mechanism_cn：随着被预测检查的实际工作负荷观测到达，λ参数的不确定性降低，预测分布被修正

- design_requirement_cn：先验预测应能转化为随观测更新的预测性预测

- artifact_choice_cn：采用正态分布作为对数正态λ参数的共轭先验，推导后验与预测分布，并设计五步更新程序

- evaluated_contrast_cn：同一8C检查在第一次、第二次、第三次观测下的预测误差

- objective_result_cn：总工作负荷PE由13%降至第二次和第三次的0%

##### evidence_pointers

1. Section 3.2, Fig. 2

2. Section 3.5.1, Table 5

#### 3. 3

- theory_or_knowledge_claim_cn：自助抽样可以从未知分布的经验样本中生成随机值；变量间相关性决定其是否随总量变化

- mechanism_cn：若分解变量与总工作负荷强相关，则应按总量缩放以维持合计约束；弱相关变量直接采用抽样值

- design_requirement_cn：总工作负荷需分解为工作类型、阶段、技能三类变量并满足合计等于总工作负荷

- artifact_choice_cn：基于自助抽样生成三类变量，用样本相关系数与阈值rcut判断是否缩放

- evaluated_contrast_cn：rcut=0,0.3,0.5,0.7的MAE/MAPE

- objective_result_cn：rcut=0.5在三次估计中获得最低或接近最低误差

##### evidence_pointers

1. Section 3.3.1-3.3.2

2. Table 4

#### 4. 4

- theory_or_knowledge_claim_cn：贝叶斯网络可通过证据进行概率推断，并可结合历史与模拟数据更新条件概率表

- mechanism_cn：当给定总工作负荷区间后，网络推出各分解变量区间的条件概率，为容量计划提供依据

- design_requirement_cn：需要将历史与模拟数据统一在一个概率推断框架中，并解决区间选择问题

- artifact_choice_cn：建立三个贝叶斯网络，总工作负荷区间采用100人时，并开发两阶段LP模型自动选区间

- evaluated_contrast_cn：100人时相对先前500人时区间的精度改进；LP求解与人工选择的对比

- objective_result_cn：LP模型保证区间合计等于总工作负荷且最大化概率；验证阶段预测区间可直接与实际观测比较

##### evidence_pointers

1. Section 3.4.1-3.4.2

2. Section 3.5.1

#### 5. 5

- theory_or_knowledge_claim_cn：行业现行工程估计采用简单回归和判断性调整，容易低估随机性较强的工作负荷

- mechanism_cn：低估导致实际执行时需用加班补偿差额，产生额外成本

- design_requirement_cn：新工具应尽量减少系统性的高估/低估偏差

- artifact_choice_cn：以工程估计模型作为baseline，比较ForeSim-BI在相同预测场景的误差

- evaluated_contrast_cn：同一8C检查三次观测下两方法的PE、MAE、平均误差

- objective_result_cn：ForeSim-BI平均高估245人时，工程估计平均低估917人时；降低成本约6%

##### evidence_pointers

1. Section 3.5.2

2. Tables 6-7

3. Fig. 6

## 评价逻辑

### evaluation_modes

1. 分布假设检验：K-S检验验证对数正态假设

2. 预测模型选择：AICc比较多个指数平滑模型

3. 参数校准：在真实观测上比较rcut阈值

4. 纵向观测验证：同一8C检查三次观测的误差变化

5. 行业基线比较：与模拟现行工程估计的模型对比

6. 财务后果量化：基于平均误差和加班费率估算成本节省

- why_these_evaluations_cn：因为论文需要同时证明工具内部各设计选择合理、整体预测精度真实可信，并证明相对于行业现状具有实践价值。单一评价不足以支撑这些不同层次的主张，因此依次完成分布假设检验、模型选择、参数校准、纵向更新验证、基线和成本对比。

- benchmark_and_contrast_chain_cn：论文先以K-S检验和AICc建立内部技术基础，再用同一8C检查的真实观测对rcut进行校准，使参数选择有据可依；随后在相同观测上报告ForeSim-BI的PE/MAE/MAPE，形成随时间变化的误差曲线；最后引入模拟现行工程估计的模型作为外部基线，并以平均误差、百分比误差和加班成本把精度差异转化为管理后果。这样benchmark从模型族内的横向比较逐步升级为面向行业实践的纵向价值对比。

### claim_evidence_ledger

#### 1. ForeSim-BI对8C总工作负荷预测误差低并能随观测大幅下降

- claim_cn：ForeSim-BI对8C总工作负荷预测误差低并能随观测大幅下降

- evidence_cn：Table 5中三次观测PE为13%、0%、0%

- assessment_cn：有直接数值证据，但只有一个检查样本，未做统计显著性检验

#### 2. 贝叶斯更新机制是误差下降的原因

- claim_cn：贝叶斯更新机制是误差下降的原因

- evidence_cn：第二次观测后PE降至0%，与更新机制的设计逻辑一致

- assessment_cn：证据与机制一致，但未做消融实验排除其他因素

#### 3. 自助抽样与rcut校准能改善工作负荷分解

- claim_cn：自助抽样与rcut校准能改善工作负荷分解

- evidence_cn：Table 4中rcut=0.5误差最低；Table 5中MAE随观测下降

- assessment_cn：基于三个观测的校准证据，样本量有限

#### 4. ForeSim-BI优于行业现行工程估计

- claim_cn：ForeSim-BI优于行业现行工程估计

- evidence_cn：Tables 6-7显示总工作负荷误差和平均误差显著更低

- assessment_cn：工程估计模型是简化模型，但作为baseline有合理性

#### 5. 工具具有成本节省潜力

- claim_cn：工具具有成本节省潜力

- evidence_cn：平均误差差值与葡萄牙加班费率计算得到约6%成本影响

- assessment_cn：属于启发性财务估算，不是实际成本核算

- internal_validity_strategy_cn：使用同一被预测维修检查的真实观测作为金标准，使预测误差可纵向追踪；用相同数据源和相同预测场景对比ForeSim-BI与工程估计，控制外部差异；通过K-S检验和AICc为模型选择提供客观依据；使用MAE、PE等标准预测误差指标。

- external_validity_strategy_cn：作者论证其数据特性（确定性+随机性成分、随时间变化、可按技能/阶段/类型刻画）普遍存在于复杂产品系统，因此工具可推广到其他行业；同时说明工具是在真实MRO与专家协作下开发的，增强生态效度。

- what_is_not_actually_tested_cn：没有进行用户实验或真实部署，未检验决策者实际使用中的行为结果；没有其他行业或机型的数据；未检验ARIMA、机器学习等替代预测模型；未对各分解变量做统计显著性检验；对工程估计的模拟只是一种简化；成本节省是推算而非财务实测。

## 贡献闭环

- technical_claim_cn：ForeSim-BI所使用的预测-更新-仿真-贝叶斯网络-LP集成方法在真实8C检查预测中取得了总工作负荷PE 13%→0%的精度，且MAE随观测下降。

- artifact_claim_cn：工具中四个模块的组合能够显著降低总工作负荷和各分解变量的预测误差，并优于行业现行工程估计。

- mechanism_claim_cn：预测误差下降的机制是贝叶斯推断在每个新观测后修正预测分布；分解变量精度改善的机制是自助抽样结合相关系数缩放，使模拟值在保持合计约束的同时随新样本调整。

- boundary_claim_cn：该工具适用于工作负荷包含确定性与随机性成分、随时间变化、且可按不同变量刻画其构成的复杂产品系统维修场景；实证范围仅限于飞机MRO的C检查族中的8C检查。

- reusable_design_knowledge_cn：可复用的设计知识包括：应采用概率分布而非点值预测应对随机工作负荷；预测模型应内置信息更新机制；总工作负荷需按管理相关维度分解并满足合计约束；概率推断结果需用优化模型转化为可执行的区间决策；误差度量需注意极端值对MAPE的扭曲。

- theoretical_contribution_cn：论文将预测、贝叶斯更新、仿真和贝叶斯网络整合进同一DSS，扩展了先前基于贝叶斯网络的维修容量规划工作，弥补了容量规划文献不讨论不确定性演化、预测文献不讨论信息更新和变量细化的缺口；为预测性分析在维护管理中的应用提供了具体实例。

- how_discussion_closes_intro_gap_cn：结论重新回到引言指出的“现有方法无法准确预测未来维修工作负荷并规划容量”这一缺口，通过重述总工作负荷误差降至0%、MAE下降以及优于工程估计的结果，直接证明ForeSim-BI填补了该缺口。

- overclaim_or_unsupported_leaps_cn：“Significantly more accurate”未经过统计显著性检验；成本节省6%基于假设性加班费率和平均误差推算，并非真实财务数据；从单一8C检查推广到更广泛复杂产品系统缺乏多场景证据；MAPE被否定后又用MAPE做rcut选择的依据，存在一致性张力。

## 句级写作动作图谱

### 1. Abstract P1 S1

- order：1

- section：Abstract

- locator：Abstract P1 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：提出用于复杂产品系统维修容量规划的决策支持工具

- rhetorical_function_cn：一句话给出论文核心制品和适用领域

- depends_on_cn：无

- sets_up_cn：后文围绕该制品的模块、数据和验证展开

- evidence_pointer：Abstract

### 2. Abstract P1 S2

- order：2

- section：Abstract

- locator：Abstract P1 S2

- move_code：PHENOMENON

- paraphrase_cn：该工具针对维修组织预测未来维修工作负荷和规划相应容量的困难

- rhetorical_function_cn：将工具置于具体实践问题之上

- depends_on_cn：前句提出工具

- sets_up_cn：为后续“现有方法不足”的缺口做铺垫

- evidence_pointer：Abstract

### 3. Abstract P1 S3-S4

- order：3

- section：Abstract

- locator：Abstract P1 S3-S4

- move_code：DESIGN_FEATURE

- paraphrase_cn：介绍四个模块：预测模块、贝叶斯推断模块、仿真模块和贝叶斯网络模块

- rhetorical_function_cn：以模块清单展示制品的整体架构

- depends_on_cn：工具提出的目标

- sets_up_cn：正文按模块顺序展开

- evidence_pointer：Abstract, Fig.1

### 4. Abstract P1 S5

- order：4

- section：Abstract

- locator：Abstract P1 S5

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：说明使用171个真实项目数据，并用真实观测和模拟行业现行做法的模型进行验证

- rhetorical_function_cn：预告证据类型与评价方式

- depends_on_cn：模块架构

- sets_up_cn：让读者预期后面的对比验证

- evidence_pointer：Abstract

### 5. Abstract P1 S6

- order：5

- section：Abstract

- locator：Abstract P1 S6

- move_code：CONTRIBUTION

- paraphrase_cn：声称工具获得更准确的预测并带来成本节省潜力

- rhetorical_function_cn：以价值主张收束摘要

- depends_on_cn：验证结果

- sets_up_cn：作为全文贡献的核心断言

- evidence_pointer：Abstract

### 6. Introduction P1 S1

- order：6

- section：Introduction

- locator：Introduction P1 S1

- move_code：CONTEXT

- paraphrase_cn：容量规划在多部门极其重要

- rhetorical_function_cn：建立研究主题的一般重要性

- depends_on_cn：无

- sets_up_cn：将维修容量规划定位为重要场景

- evidence_pointer：Introduction P1 S1

### 7. Introduction P1 S2

- order：7

- section：Introduction

- locator：Introduction P1 S2

- move_code：CONTEXT

- paraphrase_cn：在MRO中，容量规划用于预测所需资源数量和类型，尤其是按技能区分的人力

- rhetorical_function_cn：聚焦到MRO容量规划的具体内容

- depends_on_cn：容量规划重要性

- sets_up_cn：说明预测与人力技能分类是核心

- evidence_pointer：Introduction P1 S2

### 8. Introduction P1 S3

- order：8

- section：Introduction

- locator：Introduction P1 S3

- move_code：PHENOMENON

- paraphrase_cn：复杂产品系统的维修分为确定的计划内维修和随机的计划外维修，计划外可达50%以上

- rhetorical_function_cn：刻画维修工作负荷的核心不确定来源

- depends_on_cn：MRO容量规划场景

- sets_up_cn：解释为什么需要概率性预测

- evidence_pointer：Introduction P1 S3

### 9. Introduction P1 S4-S5

- order：9

- section：Introduction

- locator：Introduction P1 S4-S5

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：总结学术界已有确定性方法和随机性方法的容量规划研究

- rhetorical_function_cn：展示该领域已有知识

- depends_on_cn：前面对维修背景的描述

- sets_up_cn：在综述基础上指出缺口

- evidence_pointer：Introduction P1 S4-S5

### 10. Introduction P2 S1

- order：10

- section：Introduction

- locator：Introduction P2 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：预测被公认是容量规划的基本组成部分

- rhetorical_function_cn：将预测置于容量规划方法的中心

- depends_on_cn：容量规划综述

- sets_up_cn：转向预测方法与实践的差距

- evidence_pointer：Introduction P2 S1

### 11. Introduction P2 S2

- order：11

- section：Introduction

- locator：Introduction P2 S2

- move_code：LIMITATION

- paraphrase_cn：尽管定量预测理论有进展，多数组织仍依赖判断性预测，后者被认为不准确且有偏差

- rhetorical_function_cn：指出现实实践与理论进步之间的落差

- depends_on_cn：预测重要性

- sets_up_cn：为MRO预测实践缺陷提供一般背景

- evidence_pointer：Introduction P2 S2

### 12. Introduction P2 S3

- order：12

- section：Introduction

- locator：Introduction P2 S3

- move_code：PHENOMENON

- paraphrase_cn：常见的MRO预测是描述统计和简单线性回归，再通过过度计划等判断技巧调整

- rhetorical_function_cn：具体化MRO中的弱预测实践

- depends_on_cn：一般判断性预测实践

- sets_up_cn：为Later的工程估计baseline提供依据

- evidence_pointer：Introduction P2 S3

### 13. Introduction P2 S4

- order：13

- section：Introduction

- locator：Introduction P2 S4

- move_code：LIMITATION

- paraphrase_cn：高环境不确定性和数据变异性使MRO即使拥有大量历史数据和ERP仍采用这些方法

- rhetorical_function_cn：解释为什么技术缺口长期存在

- depends_on_cn：MRO预测实践

- sets_up_cn：说明需要更有效利用已有数据的新工具

- evidence_pointer：Introduction P2 S4

### 14. Introduction P2 S5

- order：14

- section：Introduction

- locator：Introduction P2 S5

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：列举维护环境中应用定量预测方法的已有研究

- rhetorical_function_cn：说明预测方法在维护领域的已有基础

- depends_on_cn：预测实践问题

- sets_up_cn：为论文定位与这些文献的差异

- evidence_pointer：Introduction P2 S5

### 15. Introduction P3 S1

- order：15

- section：Introduction

- locator：Introduction P3 S1

- move_code：GAP

- paraphrase_cn：提出ForeSim-BI，动机是现有方法无法准确预测未来维修工作负荷并规划容量

- rhetorical_function_cn：明确作者要填补的实践与文献缺口

- depends_on_cn：前述局限

- sets_up_cn：引出工具的模块设计和创新点

- evidence_pointer：Introduction P3 S1

### 16. Introduction P3 S2

- order：16

- section：Introduction

- locator：Introduction P3 S2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：工具在葡萄牙飞机MRO中与行业专家协作开发，基于171个项目

- rhetorical_function_cn：说明开发环境与数据来源

- depends_on_cn：工具提出

- sets_up_cn：使验证具有真实数据基础

- evidence_pointer：Introduction P3 S2

### 17. Introduction P3 S3

- order：17

- section：Introduction

- locator：Introduction P3 S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：介绍四个模块整合成的单一决策支持工具

- rhetorical_function_cn：描述制品的高层架构

- depends_on_cn：工具目标

- sets_up_cn：正文各模块详解

- evidence_pointer：Introduction P3 S3, Fig.1

### 18. Introduction P3 S4

- order：18

- section：Introduction

- locator：Introduction P3 S4

- move_code：CONTRIBUTION

- paraphrase_cn：通过模块整合，该工具比现有方法提供更准确的工作负荷预测并更有效处理容量规划的不确定性

- rhetorical_function_cn：在引言中提前声明核心贡献

- depends_on_cn：模块设计

- sets_up_cn：后文用验证支撑这一声明

- evidence_pointer：Introduction P3 S4

### 19. Introduction P3 S5-S6

- order：19

- section：Introduction

- locator：Introduction P3 S5-S6

- move_code：GAP

- paraphrase_cn：容量规划文献不处理不确定性和时间演化；预测文献不处理更新机制和变量刻画

- rhetorical_function_cn：建立双重文献缺口

- depends_on_cn：容量规划与预测综述

- sets_up_cn：为创新性定位提供依据

- evidence_pointer：Introduction P3 S5-S6

### 20. Introduction P3 S7

- order：20

- section：Introduction

- locator：Introduction P3 S7

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：综合这些方面预计能减少过度估计和不足估计资源，提升运营和财务绩效

- rhetorical_function_cn：说明缺口被填补后带来的实际后果

- depends_on_cn：双重缺口

- sets_up_cn：将技术工具与绩效价值联系起来

- evidence_pointer：Introduction P3 S7

### 21. Introduction P4

- order：21

- section：Introduction

- locator：Introduction P4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：工具通过与真实维修干预观测及模拟现行预测实践的模型进行比较来验证

- rhetorical_function_cn：预告评价方案

- depends_on_cn：工具设计

- sets_up_cn：正文第3.5节验证

- evidence_pointer：Introduction P4

### 22. Introduction P5

- order：22

- section：Introduction

- locator：Introduction P5

- move_code：STUDY_OVERVIEW

- paraphrase_cn：说明数据、模块、验证和结论的章节安排

- rhetorical_function_cn：为读者提供阅读地图

- depends_on_cn：全文结构

- sets_up_cn：正文按预测模块、更新模块、仿真模块、BN模块、验证展开

- evidence_pointer：Introduction P5

### 23. Section 2.1 P1 S1

- order：23

- section：Section 2.1

- locator：Section 2.1 P1 S1

- move_code：REQUIREMENT

- paraphrase_cn：工具适用的数据应包含确定与随机成分、随时间变化、可由不同变量刻画

- rhetorical_function_cn：从普遍适用性角度提出设计条件

- depends_on_cn：引言中的问题

- sets_up_cn：说明研究数据为何能满足这些条件

- evidence_pointer：Section 2.1 P1

### 24. Section 2.2 P1

- order：24

- section：Section 2.2

- locator：Section 2.2 P1

- move_code：CONTEXT

- paraphrase_cn：法规要求飞机MRO记录所有维修任务，因此存在大量历史数据

- rhetorical_function_cn：说明数据可得性的制度原因

- depends_on_cn：数据条件

- sets_up_cn：介绍171个项目数据

- evidence_pointer：Section 2.2 P1

### 25. Section 2.2.1 last paragraph

- order：25

- section：Section 2.2.1

- locator：Section 2.2.1 last paragraph

- move_code：STUDY_OVERVIEW

- paraphrase_cn：将数据分成两组：C至7C用于建模预测，8C用于验证

- rhetorical_function_cn：设计训练/验证数据切分

- depends_on_cn：数据介绍

- sets_up_cn：后续模块和验证的数据边界

- evidence_pointer：Section 2.2.1 last paragraph

### 26. Section 2.2.2 P1

- order：26

- section：Section 2.2.2

- locator：Section 2.2.2 P1

- move_code：THEORY_INTRO

- paraphrase_cn：总工作负荷被视为加工时间，常用对数正态分布建模，因其严格为正且右偏

- rhetorical_function_cn：从调度与维修时间文献引入分布模型

- depends_on_cn：C检查类型

- sets_up_cn：K-S检验

- evidence_pointer：Section 2.2.2 P1

### 27. Section 2.2.2 P2

- order：27

- section：Section 2.2.2

- locator：Section 2.2.2 P2

- move_code：RESULT

- paraphrase_cn：所有C至7C检查样本的K-S检验p值均大于0.05，不能拒绝对数正态假设

- rhetorical_function_cn：用数据验证分布假设

- depends_on_cn：对数正态假设

- sets_up_cn：为预测模块和仿真模块的概率假设提供依据

- evidence_pointer：Section 2.2.2, Table 2

### 28. Section 3.1 P1 S1

- order：28

- section：Section 3.1

- locator：Section 3.1 P1 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：预测模块的目标是从历史数据估计未来及前所未见维修检查的工作负荷概率分布

- rhetorical_function_cn：明确模块功能

- depends_on_cn：数据切分

- sets_up_cn：选择预测模型

- evidence_pointer：Section 3.1 P1

### 29. Section 3.1 P2

- order：29

- section：Section 3.1

- locator：Section 3.1 P2

- move_code：MECHANISM

- paraphrase_cn：AHW适合具有趋势和季节性的序列，而维修工作负荷因计划内维修的周期性和计划外维修随役龄上升而具有这些特征

- rhetorical_function_cn：将模型能力与领域机制联系

- depends_on_cn：预测模块目标

- sets_up_cn：为何选择AHW

- evidence_pointer：Section 3.1 P2

### 30. Section 3.1 P3-P4

- order：30

- section：Section 3.1

- locator：Section 3.1 P3-P4

- move_code：MECHANISM

- paraphrase_cn：状态空间模型允许推出未来检查工作负荷分布的均值和方差

- rhetorical_function_cn：解释模型输出的分布内容

- depends_on_cn：AHW公式

- sets_up_cn：为贝叶斯推断提供先验均值和方差

- evidence_pointer：Section 3.1 Eqs.(1)-(9)

### 31. Section 3.1 last part

- order：31

- section：Section 3.1

- locator：Section 3.1 last part

- move_code：RESULT

- paraphrase_cn：AICc比较显示AHW在所有候选指数平滑模型中值最低

- rhetorical_function_cn：给出模型选择的客观证据

- depends_on_cn：候选模型定义

- sets_up_cn：确认预测模块采用的模型

- evidence_pointer：Section 3.1, Table 3

### 32. Section 3.2 P1 S1

- order：32

- section：Section 3.2

- locator：Section 3.2 P1 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：贝叶斯推断模块用于在关于被预测检查的新观测出现后，将先验预测转化为预测性预测

- rhetorical_function_cn：定义第二个模块的功能

- depends_on_cn：预测模块输出

- sets_up_cn：介绍贝叶斯更新方程

- evidence_pointer：Section 3.2 P1

### 33. Section 3.2 P3

- order：33

- section：Section 3.2

- locator：Section 3.2 P3

- move_code：THEORY_INTRO

- paraphrase_cn：贝叶斯方法将参数视为随机变量并用观测更新，而频率派将其视为未知常数

- rhetorical_function_cn：为采用贝叶斯更新提供方法论理由

- depends_on_cn：更新模块目标

- sets_up_cn：贝叶斯定理与后验推导

- evidence_pointer：Section 3.2 P3

### 34. Section 3.2.1 P1

- order：34

- section：Section 3.2.1

- locator：Section 3.2.1 P1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：假设λ的正态先验是共轭先验，可简化后验推导

- rhetorical_function_cn：选择便于计算的先验结构

- depends_on_cn：对数正态分布模型

- sets_up_cn：推导后验和预测分布

- evidence_pointer：Section 3.2.1, Eq.(17)

### 35. Section 3.2.1 end

- order：35

- section：Section 3.2.1

- locator：Section 3.2.1 end

- move_code：THEORY_PROPOSITION

- paraphrase_cn：预测分布仍是对数正态分布，可由更新后的参数完全确定

- rhetorical_function_cn：说明更新机制的输出形式

- depends_on_cn：共轭先验推导

- sets_up_cn：预测性预测的实用计算

- evidence_pointer：Section 3.2.1, Eqs.(22)-(24)

### 36. Section 3.2.2 Steps 1-5

- order：36

- section：Section 3.2.2

- locator：Section 3.2.2 Steps 1-5

- move_code：DESIGN_FEATURE

- paraphrase_cn：定义五步更新程序：将预测均值方差转为参数，构建先验，计算后验，生成预测分布，并重复每次新观测

- rhetorical_function_cn：将数学公式转化为可执行程序

- depends_on_cn：贝叶斯推导

- sets_up_cn：仿真模块对预测分布的调用

- evidence_pointer：Section 3.2.2, Fig.2

### 37. Section 3.3 P1

- order：37

- section：Section 3.3

- locator：Section 3.3 P1

- move_code：DESIGN_FEATURE

- paraphrase_cn：仿真模块基于蒙特卡洛模拟，生成未来检查的总工作负荷随机值并装入贝叶斯网络

- rhetorical_function_cn：引入第三个模块的输入输出

- depends_on_cn：预测性预测分布

- sets_up_cn：说明为何需要更细粒度的工作负荷变量

- evidence_pointer：Section 3.3 P1

### 38. Section 3.3 P2

- order：38

- section：Section 3.3

- locator：Section 3.3 P2

- move_code：REQUIREMENT

- paraphrase_cn：只有总工作负荷而缺少细粒度刻画，对容量规划实用价值有限，因此专家定义了工作类型、阶段和技能三类随机变量

- rhetorical_function_cn：从实践需求引入变量的必要性

- depends_on_cn：总工作负荷预测

- sets_up_cn：三类随机变量的定义

- evidence_pointer：Section 3.3 P2

### 39. Section 3.3.1 P1

- order：39

- section：Section 3.3.1

- locator：Section 3.3.1 P1

- move_code：REQUIREMENT

- paraphrase_cn：各类变量互斥且完备，合计等于总工作负荷

- rhetorical_function_cn：建立仿真分解的数学约束

- depends_on_cn：三类变量定义

- sets_up_cn：自助抽样后的归一化缩放

- evidence_pointer：Section 3.3.1, Eq.(27)

### 40. Section 3.3.1 P2

- order：40

- section：Section 3.3.1

- locator：Section 3.3.1 P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：总工作负荷从已知对数正态分布抽样，其余变量通过自助抽样从同类检查样本生成

- rhetorical_function_cn：区分总负荷与分解变量的生成机制

- depends_on_cn：分布假设

- sets_up_cn：说明自助抽样细节

- evidence_pointer：Section 3.3.1 P2

### 41. Section 3.3.2 P3

- order：41

- section：Section 3.3.2

- locator：Section 3.3.2 P3

- move_code：MECHANISM

- paraphrase_cn：并非所有分解变量都随总工作负荷变化，因此用样本相关系数判断是否需要缩放

- rhetorical_function_cn：设计自助抽样的后处理机制

- depends_on_cn：合计约束

- sets_up_cn：rcut阈值校准

- evidence_pointer：Section 3.3.2 P3

### 42. Section 3.3.2 after Eq.(29)

- order：42

- section：Section 3.3.2

- locator：Section 3.3.2 after Eq.(29)

- move_code：RESULT

- paraphrase_cn：不同rcut的测试显示rcut=0.5在三次估计中获得最低或接近最低的MAE和MAPE

- rhetorical_function_cn：用真实观测校准设计参数

- depends_on_cn：rcut定义

- sets_up_cn：最终采用0.5

- evidence_pointer：Section 3.3.2, Table 4

### 43. Section 3.3.2.1-3.3.2.2

- order：43

- section：Section 3.3.2.1-3.3.2.2

- locator：Section 3.3.2.1-3.3.2.2

- move_code：DESIGN_FEATURE

- paraphrase_cn：无观测时从最近同类检查的原样自助抽样；有观测时从新样本自助抽样

- rhetorical_function_cn：给出仿真程序的行为分支

- depends_on_cn：自助抽样机制

- sets_up_cn：仿真程序Step 3

- evidence_pointer：Section 3.3.2.1-3.3.2.2

### 44. Section 3.4 P1

- order：44

- section：Section 3.4

- locator：Section 3.4 P1

- move_code：DESIGN_FEATURE

- paraphrase_cn：贝叶斯网络模块将历史数据与仿真数据结合，使MRO在单一工具中预测已知和前所未见的检查工作负荷

- rhetorical_function_cn：引入第四模块及其集成功能

- depends_on_cn：仿真模块输出

- sets_up_cn：贝叶斯网络的结构和区间选择问题

- evidence_pointer：Section 3.4 P1

### 45. Section 3.4.1 P1

- order：45

- section：Section 3.4.1

- locator：Section 3.4.1 P1

- move_code：DESIGN_FEATURE

- paraphrase_cn：相比先前工作中的500人时区间，这里将总工作负荷离散化为100人时区间，以提高精度

- rhetorical_function_cn：说明相对先前研究的制品改进

- depends_on_cn：贝叶斯网络设计

- sets_up_cn：后文验证精度改进

- evidence_pointer：Section 3.4.1 P1

### 46. Section 3.4.1 P2

- order：46

- section：Section 3.4.1

- locator：Section 3.4.1 P2

- move_code：GAP

- paraphrase_cn：人工选择满足合计条件的区间工作繁琐且不能保证最优，因此开发LP模型

- rhetorical_function_cn：识别贝叶斯网络应用中的决策缺口

- depends_on_cn：区间推断

- sets_up_cn：LP模型的两个阶段

- evidence_pointer：Section 3.4.1 P2

### 47. Section 3.4.2 Stage 1

- order：47

- section：Section 3.4.2

- locator：Section 3.4.2 Stage 1

- move_code：DESIGN_FEATURE

- paraphrase_cn：LP模型第一阶段最小化所选总工作负荷区间上界，并满足最小累计概率约束；90%被视为合理折中

- rhetorical_function_cn：将风险态度编码进优化模型

- depends_on_cn：区间选择缺口

- sets_up_cn：第二阶段区间选择

- evidence_pointer：Section 3.4.2, Eqs.(32)-(35), Fig.4

### 48. Section 3.4.2 Stage 2

- order：48

- section：Section 3.4.2

- locator：Section 3.4.2 Stage 2

- move_code：DESIGN_FEATURE

- paraphrase_cn：LP模型第二阶段在合计等于计划总工作负荷且每个变量只选一个区间的约束下，最大化所选区间概率之和

- rhetorical_function_cn：将概率推断转为可执行区间组合

- depends_on_cn：第一阶段总区间

- sets_up_cn：验证阶段的预测值F来自区间上界

- evidence_pointer：Section 3.4.2, Eqs.(36)-(39), Fig.5

### 49. Section 3.5 P1

- order：49

- section：Section 3.5

- locator：Section 3.5 P1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：验证部分使用ForeSim-BI和模拟行业现行做法的工程估计来预测未来检查工作负荷，并比较二者误差

- rhetorical_function_cn：预告验证与对比结构

- depends_on_cn：工具完整构建

- sets_up_cn：结果表和误差解释

- evidence_pointer：Section 3.5 P1

### 50. Section 3.5.1 first conclusion

- order：50

- section：Section 3.5.1

- locator：Section 3.5.1 first conclusion

- move_code：RESULT

- paraphrase_cn：工具在预测首次8C检查时总工作负荷PE为13%，且预测跨度超过两年

- rhetorical_function_cn：报告初始预测精度

- depends_on_cn：LP模型90%累计概率

- sets_up_cn：说明后续观测改进幅度

- evidence_pointer：Section 3.5.1, Table 5

### 51. Section 3.5.1 second conclusion

- order：51

- section：Section 3.5.1

- locator：Section 3.5.1 second conclusion

- move_code：RESULT

- paraphrase_cn：第二和第三次观测时总工作负荷PE降至0%，说明贝叶斯推断机制随观测有效修正预测分布

- rhetorical_function_cn：把误差下降归因于更新机制

- depends_on_cn：表5观测序列

- sets_up_cn：支持贝叶斯模块的有效性声明

- evidence_pointer：Section 3.5.1, Table 5

### 52. Section 3.5.1 third conclusion

- order：52

- section：Section 3.5.1

- locator：Section 3.5.1 third conclusion

- move_code：RESULT

- paraphrase_cn：所有工作负荷变量的MAE总体下降，表明自助抽样随新样本改善总工作负荷在分解变量中的分配

- rhetorical_function_cn：分解变量精度改善的证据

- depends_on_cn：表5 MAE行

- sets_up_cn：说明仿真模块的有效性

- evidence_pointer：Section 3.5.1, Table 5

### 53. Section 3.5.1 fourth conclusion

- order：53

- section：Section 3.5.1

- locator：Section 3.5.1 fourth conclusion

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：MAPE因极端PE值而被认为不适合评估本文预测精度，例如个别工作阶段出现超过500%的PE

- rhetorical_function_cn：解释为何不以MAPE为主要结论

- depends_on_cn：表5结果

- sets_up_cn：避免读者误读MAPE

- evidence_pointer：Section 3.5.1, Table 5

### 54. Section 3.5.1 final conclusion

- order：54

- section：Section 3.5.1

- locator：Section 3.5.1 final conclusion

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：即使经过两次观测，部分工作类型、阶段和技能变量仍有明显误差，未来需要探索自助抽样之外的方法

- rhetorical_function_cn：诚实呈现边界与后续研究

- depends_on_cn：表5分解变量误差

- sets_up_cn：结论部分的研究展望

- evidence_pointer：Section 3.5.1

### 55. Section 3.5.2 P2

- order：55

- section：Section 3.5.2

- locator：Section 3.5.2 P2

- move_code：RESULT

- paraphrase_cn：对比显示ForeSim-BI在总工作负荷上误差显著更低，而工程估计系统性低估工作负荷

- rhetorical_function_cn：给出相对基线的核心优势证据

- depends_on_cn：表5与表6

- sets_up_cn：平均误差和成本分析

- evidence_pointer：Section 3.5.2, Table 6

### 56. Section 3.5.2 P3

- order：56

- section：Section 3.5.2

- locator：Section 3.5.2 P3

- move_code：PRACTICAL_STAKES

- paraphrase_cn：平均误差确认工程估计低估趋势；低估导致加班成本，按加班费率估算是约6%的单项目成本增加

- rhetorical_function_cn：将误差差异转化为财务影响

- depends_on_cn：表7平均误差

- sets_up_cn：强化工具实际价值

- evidence_pointer：Section 3.5.2, Table 7, Fig.6

### 57. Section 3.5.2 last paragraph

- order：57

- section：Section 3.5.2

- locator：Section 3.5.2 last paragraph

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：区间离散化总会有误差，例如WP4实际一直是41人时而预测为100人时；更小区间或连续条件概率是未来方向

- rhetorical_function_cn：界定离散化误差这一边界条件

- depends_on_cn：表6-7结果

- sets_up_cn：结论中关于连续BN的研究展望

- evidence_pointer：Section 3.5.2 last paragraph

### 58. Conclusion P1

- order：58

- section：Conclusion

- locator：Conclusion P1

- move_code：CONTRIBUTION

- paraphrase_cn：总结ForeSim-BI集成四个模块，使维修组织能够预测已知和前所未见的维修干预

- rhetorical_function_cn：重置工具模块与目标

- depends_on_cn：全文设计

- sets_up_cn：总结验证证据

- evidence_pointer：Section 4 P1

### 59. Conclusion P2

- order：59

- section：Conclusion

- locator：Conclusion P2

- move_code：CONTRIBUTION

- paraphrase_cn：强调验证结果：总工作负荷误差降至0%、MAE下降、相对现行预测实践的优越性

- rhetorical_function_cn：用主要结果支撑贡献

- depends_on_cn：第3.5节

- sets_up_cn：引出未来研究

- evidence_pointer：Section 4 P2

### 60. Conclusion P3

- order：60

- section：Conclusion

- locator：Conclusion P3

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：列出未来方向：替代自助抽样的方法、更小或连续BN区间、更合适的误差指标

- rhetorical_function_cn：界定工具边界并保留后续贡献空间

- depends_on_cn：验证中的不足

- sets_up_cn：论文收束

- evidence_pointer：Section 4 P3

### 61. Conclusion P4

- order：61

- section：Conclusion

- locator：Conclusion P4

- move_code：CONTRIBUTION

- paraphrase_cn：最终结论是ForeSim-BI作为预测性分析定量工具，展示了历史数据和新增观测如何改进MRO容量规划决策

- rhetorical_function_cn：把具体工具结果上升为一般性预测分析价值

- depends_on_cn：全部验证

- sets_up_cn：全文结束

- evidence_pointer：Section 4 P4

## 写作技术

- gap_construction_cn：采用双重缺口构造：容量规划文献忽视工作负荷不确定性及其时间演化；预测文献忽视信息更新和工作负荷变量刻画。这样既区别于优化型DSS，又区别于纯预测研究。

- signposting_cn：摘要和引言先做模块预告；第2节说明数据条件；第3节每个模块都以功能句开头；第3.5节开头说明验证方案；结论再重述模块、结果和未来方向。

- transition_logic_cn：数据分布检验结果支撑预测模块；预测模块输出的均值和方差作为贝叶斯更新的先验；更新后的预测分布驱动仿真分解；分解后的模拟数据装入贝叶斯网络；贝叶斯网络输出再由LP决策；最终进入同一场景的纵向验证和行业基线对比。

- claim_evidence_rhythm_cn：每个设计选择后立即给出评价指标和表格，例如AICc表、rcut表、观测误差表；结果用First/Second/Third结构逐条解释，使定性结论紧贴定量证据。

- benchmark_narrative_cn：benchmark不是一次性出现的，而是先在各模块内部做模型/参数对照，最后在整体层面与“模拟现行工程估计”的baseline对照；再用平均误差和加班成本把benchmark差异升级为财务叙事。

- theory_return_cn：论文较少抽象化理论，但将工具结果明确归因于“贝叶斯推断的有效调整”和“自助抽样的改善”，使结果返回支撑这些知识基础在维护容量规划场景中的适用性。

- contribution_positioning_cn：作者将贡献定位为“首次同时考虑不确定性演化、信息更新和工作负荷多维刻画”，反复在引言、创新说明和结论中重复这一组合，以确立新颖性。

- novelty_protection_cn：通过指出现有文献分别缺少哪些能力、工具集成这四项能力、并用真实数据和行业基线证明效果，防止贡献被视为单一算法的性能报道；同时列举未来改进方向，避免一次性结果印象。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：写引言时先建立领域重要性和具体实践问题，再综述现有方法并制造双重缺口

- research_job_cn：明确目标组织、场景和现有做法；收集可用的真实数据

- required_evidence_cn：需要比现有预测/容量规划方法更差的实践证据或文献证据

- transition_to_next_cn：由缺口引出需要开发新工具

#### 2. 2

- step：2

- writing_job_cn：用专门一节描述数据特性和分布假设检验

- research_job_cn：清洗数据并检验关键随机变量的概率分布假设

- required_evidence_cn：假设检验统计量和p值

- transition_to_next_cn：分布假设为概率预测模块提供基础

#### 3. 3

- step：3

- writing_job_cn：用正式模型选择准则选择预测方法

- research_job_cn：实现候选预测模型并比较其信息准则

- required_evidence_cn：AICc或其他标准化的模型比较结果

- transition_to_next_cn：选定的预测模型输出先验分布

#### 4. 4

- step：4

- writing_job_cn：设计更新机制，使先验预测能随新观测修正

- research_job_cn：利用贝叶斯或类似更新规则推导后验和预测分布

- required_evidence_cn：数学推导与可执行程序

- transition_to_next_cn：更新后的分布进入下游仿真

#### 5. 5

- step：5

- writing_job_cn：说明总预测对实际决策不够，必须按管理维度分解

- research_job_cn：定义满足合计约束的分解变量并设计抽样过程

- required_evidence_cn：领域专家输入和数学约束

- transition_to_next_cn：需要校准分解参数

#### 6. 6

- step：6

- writing_job_cn：用真实观测校准关键设计参数

- research_job_cn：比较不同参数值的误差表现

- required_evidence_cn：至少一组真实观测和误差指标表

- transition_to_next_cn：参数确定后形成完整工具

#### 7. 7

- step：7

- writing_job_cn：将概率推断结果转化为可执行决定，说明决策规则和优化模型

- research_job_cn：构建贝叶斯网络和线性规划/决策模型

- required_evidence_cn：满足业务约束的可行解

- transition_to_next_cn：整体工具进入验证

#### 8. 8

- step：8

- writing_job_cn：在同一真实干预的多次观测上纵向验证工具

- research_job_cn：随时间收集观测并记录预测误差

- required_evidence_cn：多轮观测的PE/MAE等

- transition_to_next_cn：用基线模型建立效率对比

#### 9. 9

- step：9

- writing_job_cn：构建模拟现行实践的基准模型并进行比较

- research_job_cn：基于领域常用方法实现baseline

- required_evidence_cn：两方法在同一场景的误差对比

- transition_to_next_cn：用平均误差和成本情景把结果升级为价值

#### 10. 10

- step：10

- writing_job_cn：在结论中重述工具模块、验证结果、边界和未来研究

- research_job_cn：梳理哪些设计选择被验证、哪些未验证

- required_evidence_cn：与引言缺口对应的结果证据

- transition_to_next_cn：收束全文

### most_transferable_moves_cn

1. 双重缺口构造：容量规划文献缺不确定性演化，预测文献缺更新与分解

2. 模块化DSS：把预测、更新、仿真、决策整合为相互依赖的模块

3. 数据切分：一部分历史用于建模，另一部分新类型检查用于验证

4. 纵向观测验证：同一预测对象在不同观测时刻展示更新效果

5. 基准实践：用模拟现行工程估计作为baseline，而不是只用无意义的随机基线

6. 财务化结果：把平均误差转化为加班成本节省

### resource_intensive_or_nonstandard_parts_cn

1. 需要获得真实MRO的171个维修项目数据，涉及企业运营记录

2. 需要与行业专家深度合作以定义工作类型、阶段和技能变量

3. 需要等待同一检查类型的新观测到达，纵向验证耗时长

4. 工程估计baseline的建模依赖行业实践细节

5. 葡萄牙劳动法加班费率等财务信息具有地域特殊性

### what_not_to_copy_superficially_cn

1. 若没有真实观测和多个时点数据，不能照搬“PE降至0%”的表述

2. 若没有统计显著性检验，应避免“significantly more accurate”的措辞

3. 若只做单一案例，不宜宣称对所有复杂产品系统普遍适用

4. 若误差中存在极端值，不应继续以MAPE作为唯一精度指标

5. 成本节省不能直接从平均误差推算，需要财务实际数据或至少明确假设

- single_best_description_of_the_routine_cn：用一个集成预测、更新、仿真与概率推理的DSS填补MRO容量规划中不确定性预测与更新机制的缺口，并用同一维修干预的真实观测和行业基线证明其精度与成本价值。

## 分析边界

OCR/全文转换中图1-6及部分公式可能不可见或存在乱码（如gimel等变量名），影响对图和公式的精确描述；缺乏原文页码；未提供在线附录或补充材料；判断依据以可见文本为主。
