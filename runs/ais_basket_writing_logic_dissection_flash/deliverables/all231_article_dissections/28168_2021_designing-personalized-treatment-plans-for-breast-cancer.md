# Designing Personalized Treatment Plans for Breast Cancer

- 作者：Wei Chen; Yixin Lu; Liangfei Qiu; Subodha Kumar
- 年份 / 期刊：2021 / Information Systems Research
- DOI：10.1287/isre.2021.1002
- 源文件：28168_2021_designing-personalized-treatment-plans-for-breast-cancer.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：requirements_build_evaluate_design_principles
- 置信度：0.87

## 文章级论证概况

- 核心问题：在早期乳腺癌放疗计划中，如何纳入患者特异性信息以预测患者对给定治疗方案的结果，并据此为个体患者定制最优的放疗剂量方案？

- 制品与设计：一个设计科学范式的个性化治疗计划决策支持框架，核心为两个部分：一是基于临床肿瘤学与放射生物学知识、以Tumor Control Probability（TCP）为核心的预测模型，使患者术前/术后残留微肿瘤细胞(MTC)体积、密度、克隆源细胞比例和放射敏感性作为随机变量纳入预测；二是以最小化乳腺平均剂量为目标的优化模型，在给定TCP目标约束（以及可选66 Gy最大剂量上限）下，通过Adam随机优化方法求解决策变量D(d)。

- 客观结果：通过系列仿真实验显示，相较标准均匀放疗计划，群组最优计划和个体剂量绘画计划均能以显著更低的平均剂量达到同样的TCP目标（如TCP 90%时，平均剂量从54 Gy降至约1.2–3.0 Gy），降低肺部/心脏辐射暴露和相关不良反应风险；同时估计可年节省超过2亿美元与放射性肺癌及心脏病相关的治疗成本。

- 核心贡献：作者声称的贡献是：(1) 为信息技术（HIT）设计研究提供一个新的临床决策支持框架，以填补现有HIT在治疗决策支持方面研究不足的缺口；(2) 回应对HIT影响进行微观层面研究的需求，量化该治疗计划框架对患者结局和治疗成本的影响；(3) 用仿真方法克服临床试验在比较个体化治疗方案时的成本和随访限制。

- 整篇论证链：论文先以乳腺癌治疗负担和现行放疗剂量均一化问题引入，指出现行标准放疗因未能考虑患者和肿瘤异质性而导致邻近器官毒副作用的风险。随后通过综述指出，现有患者级医疗预测分析大多聚焦于诊断或风险预测，很少支持治疗决策；现有放疗计划优化只关注已开处方剂量下的剂量递送优化，而没有解答如何从患者的异质性特征出发决定最优辐射剂量；同时，个性化医学文献中虽有预测建模和仿真思想，但没有结合临床工作流中的患者特异性信息做剂量个性化。作者以设计科学范式为指导，将临床肿瘤学中的TCP模型作为核心思想，用患者治疗轨迹信息（病理学、临床特征）刻画无法直接成像的MTC分布，构建预测模型并基于Bayesian-MCMC估计模型参数；随后将预测模型嵌入优化模型，用Adam算法求解在给定TCP目标下的最小平均剂量。评价分为两阶段：基准评价将标准均匀计划与群组最优计划、个体剂量绘画计划在三种误差水平下比较，展示大幅剂量下降和不良事件风险下降；附加评价将Adam与L-BFGS-B、SA、GA比较，显示其优化质量和计算效率优势；经济分析将剂量降低转换为肺癌和心脏病发病风险及成本节约。最后讨论回扣引言缺口，把贡献表述为HIT设计知识、个性化医疗分析和价值量化，并说明局限和未来方向。

## 类型与写作弧线判定

- 论文主类型判定：作者明确声明采用设计科学范式（Hevner et al. 2004, Gregor and Hevner 2013），提出的核心制品是决策支持框架（预测模型＋优化模型）。评价不是随机对照实验或单一benchmark数据集主导，而是通过仿真实验作为主要证据，并展示该制品在降低剂量、保持TCP目标、提高计算效率等方面优于现有实践。整体论证线更接近“需求—构建—评价—设计知识”的设计科学套路，而非以理论推导出制品差异并通过实验检验等其它类型。

- 主导写作弧线判定：文章以临床需求（现有放疗计划不能充分实现个性化、无法兼顾肿瘤控制与正常组织毒性）为起点，明确引入设计科学范式作为构建指导，随后构建预测模型和优化模型，再通过仿真实验和对照方法进行评价，最后在讨论中把设计经验上升为适用于其他慢病治疗决策支持的可迁移设计知识。整体结构与“需求—构建—评价—设计原则”相吻合。

## 研究开展程序

- study_or_phase_count：6

- 研究阶段总序列：论证依次包含：(1) 领域知识与问题构建（文献综述和临床问题定义）；(2) 预测模型构建与参数估计（MTC建模、Bayesian-MCMC估计）；(3) 预测模型验证（交叉验证、外部合成数据验证、敏感性/外推分析）；(4) 优化模型与最优计划求解；(5) 框架的基准评价与附加算法评价；(6) 经济效益估算。各阶段累积关系为：领域知识决定预测模型的形式；预测模型验证为后序优化提供可信的TCP预测函数；优化模型把TCP转成剂量决策；评价阶段比较两种患者粒度的最优计划；最后将剂量下降转化为经济价值。

### studies_or_phases

#### 1. 领域知识与临床问题定义/设计科学框架设定

- order：1

- name_cn：领域知识与临床问题定义/设计科学框架设定

- question_cn：放疗计划中什么样的个性化决策支持是必要且未被满足的？

- inputs_and_setting_cn：文献综述：临床乳腺癌放疗指南、现有优化放疗计划的文献、EORTC和EBCTCG临床试验背景，以及设计科学理论框架。

- designed_or_compared_object_cn：将现有“标准均匀放疗计划”和已有IMRT剂量递送优化研究与新的治疗计划设计问题相对照。

- baseline_control_or_counterfactual_cn：现有标准剂量方案（50 Gy分25次或66 Gy强化方案）作为临床实践基线；已有放疗优化文献（Romeijn等、Bortfeld等、Ungun等）作为文献基线的差异点。

##### objective_metrics

1. 肿瘤局部控制率

2. 标准治疗方案的辐射剂量

3. 邻近器官损伤风险

4. 临床试验成本与周期

- analysis_method_cn：文献综述和定性临床问题界定；对照表列出与INFORMS期刊放疗优化文章的差异。

- main_result_cn：指出现有研究聚焦于处方剂量下的递送优化，没有回答“如何首先为个体患者确定最优剂量”；患者级预测模型没有用于治疗决策；个性化放疗需要新的设计科学制品。

- argumentative_role_cn：建立需求缺口和设计目标，为后序框架提供必要和合理性。

- remaining_uncertainty_cn：如何把临床肿瘤学知识变成可估计并可优化的计算模型仍未给出。

- link_to_next_phase_cn：引出后续章节的框架构建。

##### evidence_pointers

1. Section 1 Introduction P1-P6

2. Section 2.1 最后一段

3. Section 2.2 第二、三段

4. Section 2.3 第三段

5. Table 1

#### 2. 预测模型构建与参数估计

- order：2

- name_cn：预测模型构建与参数估计

- question_cn：如何用患者和临床信息预测给定放疗方案下个体的肿瘤控制概率(TCP)？

- inputs_and_setting_cn：病理数据集（1000+张病理切片）、EORTC 22881-10882试验（1616名患者，50 Gy vs 66 Gy）、EBCTCG试验（10801名患者，50 Gy vs 0 Gy）；模拟生成10000名合成患者。

- designed_or_compared_object_cn：基于放射生物TCP模型的预测模型；将MTC体积、密度、克隆源细胞分数和放射敏感性建模为随机变量。

- baseline_control_or_counterfactual_cn：模型选择层面：对比数据驱动模型（需大数据、可解释性低），优先选择模型驱动的TCP模型；参数分布选择基于已有临床文献。

##### objective_metrics

1. 似然函数

2. MCMC估计收敛性（Heidelberger-Welch诊断）

3. 预测误差（RMSE）

4. 外部合成数据的TCP置信区间

- analysis_method_cn：模型形式化：TCP公式集成随机变量；Bayesian MCMC（Rasmussen和Ghahramani 2003）；100次重复模拟降低先验偏差。

- main_result_cn：模型被估计并验证：测试集RMSE约1.3%，外部合成数据（基于Polgar 2013）预测TCP置信区间为93.7%-94.4%，与报道的94.1%接近；敏感性分析显示在0 Gy/50 Gy和0 Gy/66 Gy子样本上训练的模型预测一致，外推风险较低。

- argumentative_role_cn：给出可工作的预测函数，该函数能嵌入优化模型，并证明预测模型可信，为后续剂量优化提供基础。

- remaining_uncertainty_cn：MTC建模基于假设性概率分布，未直接观察MTC；真实临床数据中信息集成假设可能不成立；模型中未包含辅助治疗和时间因素。

- link_to_next_phase_cn：已可信的TCP模型进入优化模型，用于在约束条件下求最小平均剂量。

##### evidence_pointers

1. Section 3.1 公式(1)-(3)

2. Section 3.1.1 Model Estimation

3. Section 3.1.2 Model Validation

4. Figure 3

#### 3. 优化模型构建与求解

- order：3

- name_cn：优化模型构建与求解

- question_cn：在给定TCP目标（以及66 Gy最大剂量约束可选）下，如何确定最优剂量分布，使其既能实现肿瘤控制又最小化平均乳腺剂量？

- inputs_and_setting_cn：10000名合成患者参数；TCP目标（90%和80%）；无约束和66 Gy上限约束；系统误差和随机误差（0、1、5 mm）。

- designed_or_compared_object_cn：群组最优计划（基于平均TCP）和个体剂量绘画计划（基于个体TCP）；优化问题为最小化AvgDose，subject to TCP=TCP目标。

- baseline_control_or_counterfactual_cn：标准均匀计划（既定的50 Gy/25次、或34 Gy/80%目标场景）作为基准；无约束/有约束优化方案作为两条件之间的比较。

##### objective_metrics

1. 平均剂量

2. 剂量分布形状

3. 最大剂量

4. 约束满足情况

- analysis_method_cn：Lagrange乘子法构造目标函数；Adam随机优化（Kingma和Ba 2014）用于解决TCP非线性、随机性；算法1给出求解步骤。

- main_result_cn：群组最优计划可达到相同TCP目标，但平均剂量大幅下降；约束方案在TCP 90%下需要较高平均剂量（因MTC高浓度区域剂量受限，需要在更大范围补量）。

- argumentative_role_cn：连接预测模型和最优计划生成，展示以TCP为目标函数时，剂量分布可以显著改变。

- remaining_uncertainty_cn：群组最优计划仍是基于平均TCP；个体计划计算成本更高且依赖更精细病理信息。

- link_to_next_phase_cn：优化模型输出用于第4节评价中与标准计划及多种误差场景比较。

##### evidence_pointers

1. Section 3.2

2. Section 3.2.1 公式(9)-(15)

3. Algorithm 1

#### 4. 基准评价：标准计划 vs 最优计划的剂量比较

- order：4

- name_cn：基准评价：标准计划 vs 最优计划的剂量比较

- question_cn：相比临床现有标准均匀放疗计划，群组最优计划和个体剂量绘画计划能否在保持相同TCP目标下显著降低平均剂量？在不同setup误差条件下是否稳健？

- inputs_and_setting_cn：10000名合成患者；TCP目标90%和80%；系统误差和随机误差三种水平（0、1、5 mm）；标准均匀计划以及最优计划的代码和参数。

- designed_or_compared_object_cn：比较三种计划类型：标准均匀计划、无约束最优计划、约束最优计划；按群组粒度（平均TCP）和个体粒度（个体TCP）分别比较。

- baseline_control_or_counterfactual_cn：标准均匀计划（TCP 90%时平均剂量54 Gy；TCP 80%时平均剂量34 Gy）为基准；无约束/有约束互为条件比较；不同setup误差作为稳健性条件。

##### objective_metrics

1. 平均乳腺剂量

2. 剂量分布形状和最大剂量

3. TCP目标达成

- analysis_method_cn：仿真实验和表格/图表汇总；比较剂量分布曲线和平均剂量表。

- main_result_cn：群组最优计划在TCP 90%时，无误差条件下平均剂量从54 Gy降至约2.86 Gy（减少约94.7%），即使5 mm误差下也减少90%以上；个体剂量绘画计划在TCP 90%时平均剂量低至1.2-3.0 Gy，同样大幅低于标准计划；说明个性化计划的优势在误差存在时仍稳健。

- argumentative_role_cn：直接验证制品相对于现有实践的客观提升；说明剂量减少对正常组织毒性降低的意义。

- remaining_uncertainty_cn：只比较平均剂量，未直接度量肺/心脏剂量或患者微观副作用；未比较真实临床结局；个体计划的最优剂量分布在三个误差条件下仍有差异。

- link_to_next_phase_cn：平均剂量差异进一步被翻译成健康风险和经济成本。

##### evidence_pointers

1. Section 4.1

2. Table 2-4

3. Figure 4-5

#### 5. 附加评价：优化算法与基准优化方法比较

- order：5

- name_cn：附加评价：优化算法与基准优化方法比较

- question_cn：在群组和个体计划求解中，Adam优化方法相对L-BFGS-B、模拟退火（SA）、遗传算法（GA）是否既保证更好的患者结局（平均剂量更低）又具备更高计算效率？

- inputs_and_setting_cn：10000名合成患者；同一TCP目标90%；同一计算环境（Windows 10, Intel i7-8700, 16GB RAM）。

- designed_or_compared_object_cn：四种优化算法在相同数据、相同目标函数下的求解性能：Adam vs L-BFGS-B vs SA vs GA。

- baseline_control_or_counterfactual_cn：L-BFGS-B、SA、GA作为基准优化方法；按无约束和66 Gy约束、两种粒度（群组/个体）比较。

##### objective_metrics

1. 平均剂量

2. 收敛时间（分钟）

- analysis_method_cn：仿真实验对照表（Table 5和Table 6）。

- main_result_cn：Adam在绝大多数条件下平均剂量更低，且计算时间更短；SA和GA明显更慢且更容易陷入局部最优；L-BFGS-B结局接近但更耗时而在高误差下效果略差。

- argumentative_role_cn：强化制品的实际可用性，表明算法选择是该框架能推广的重要因素；补充“高质量的决策支持”不仅涉及预测精度，也包括优化效率。

- remaining_uncertainty_cn：只测试了论文设定的患者参数和TCP目标；没有讨论硬件对不同算法时间的影响或更大的临床数据集。

- link_to_next_phase_cn：优化算法优势转化为潜在成本节约分析的前提（可扩展到实际使用）。

##### evidence_pointers

1. Section 4.2 Additional Evaluation

2. Table 5

3. Table 6

#### 6. 经济效益估算

- order：6

- name_cn：经济效益估算

- question_cn：由个性化计划带来的平均剂量降低，经过线性剂量-风险关系，能转化为多少肺/心脏疾病风险下降和医疗成本节约？

- inputs_and_setting_cn：以TCP 90%、setup误差5 mm的保守场景；基于Table 4中剂量从54 Gy降至3 Gy；引用临床流行病学文献风险系数：肺肿瘤8.5%/Gy、心脏事件7.4%/Gy、基础发病率和治疗成本。

- designed_or_compared_object_cn：将剂量改变映射到剂量-反应线性模型；对每个患者计算肺/心脏风险绝对变化和单名患者成本节约，再按年度新增乳腺癌患者数外推。

- baseline_control_or_counterfactual_cn：标准均匀计划和最佳个性化计划的剂量差异作为暴露差异；已有文献中的风险系数作为量化基础。

##### objective_metrics

1. 肺/心脏平均剂量下降

2. 肺癌/心脏病风险下降百分比

3. 每名患者成本节约

4. 年度总成本节约

- analysis_method_cn：基于已有剂量-反应研究（Grantzau 2014; Darby 2013）的线性外推；点估计乘以外推病人数量。

- main_result_cn：平均剂量从54 Gy降至3 Gy，肺和心脏剂量分别下降约8.22 Gy和4.63 Gy；肺癌和心脏病风险分别降低69.8%和34.2%；每名患者节约约851.95美元；年度276,480名新增乳腺癌患者对应约2.355亿美元成本节约。

- argumentative_role_cn：将技术性能优势转译成实践价值和政策意义，回应引言中的经济成本和HIT价值量化缺口。

- remaining_uncertainty_cn：线性外推依赖文献平均风险系数；未计其它副作用和真实患者随访；成本估计基于2018年价格；没有真正测量个性化计划在真实人群中的实际健康收益。

- link_to_next_phase_cn：讨论部分从经济效益回到研究贡献和未来方向。

##### evidence_pointers

1. Section 4.3 Economic Benefits

## 各部分修辞架构

### abstract_moves

#### 1. Abstract P1 S1-S2

- move_code：CONTEXT

- locator：Abstract P1 S1-S2

- function_cn：建立全球乳腺癌负担和治疗复杂性背景，为问题定调。

- paraphrase_cn：乳腺癌是全世界女性癌症死亡的头号原因；现行治疗复杂且涉及多专业和大量信息处理流程。

- depends_on_cn：无

- sets_up_cn：为个性化治疗计划问题设置现实紧迫性。

#### 2. Abstract P1 S3

- move_code：RQ_OR_OBJECTIVE

- locator：Abstract P1 S3

- function_cn：提出本文研究问题：如何设计个性化治疗计划决策支持？

- paraphrase_cn：治疗复杂性和信息密集性质对个体患者的个性化与定制治疗计划提出重大挑战。

- depends_on_cn：背景的必要性

- sets_up_cn：引出设计科学制品。

#### 3. Abstract P2 S1

- move_code：DESIGN_FEATURE

- locator：Abstract P2 S1

- function_cn：描述核心制品的结构：预测模型＋优化模型。

- paraphrase_cn：框架核心由一个基于临床和患者特征预测治疗方案结局的预测模型和一个基于不同计划预测结局优化治疗方案的优化模型组成。

- depends_on_cn：研究问题

- sets_up_cn：为之后的摘要结果报告做铺垫。

#### 4. Abstract P2 S2

- move_code：RESULT

- locator：Abstract P2 S2

- function_cn：报告主要评价结果。

- paraphrase_cn：系列仿真实验表明该框架生成的计划一致优于现有实践，更好平衡局部复发和辐射副作用，并降低相关治疗成本。

- depends_on_cn：框架设计

- sets_up_cn：引出贡献声明。

#### 5. Abstract P3 S1

- move_code：CONTRIBUTION

- locator：Abstract P3 S1

- function_cn：声明研究贡献。

- paraphrase_cn：作者称研究贡献于HIT促进成本有效医疗的研究和临床实践模型工具。

- depends_on_cn：结果

- sets_up_cn：为读者提供完整摘要叙事。

### introduction_moves

#### 1. Introduction P1 S1-S2

- move_code：CONTEXT

- locator：Introduction P1 S1-S2

- function_cn：给出乳腺癌发病率和经济负担的统计背景。

- paraphrase_cn：乳腺癌是全球女性最常见癌症；美国超350万女性确诊；治疗费用预计达165亿美元。

- depends_on_cn：无

- sets_up_cn：建立现实问题的规模。

#### 2. Introduction P2 S1-S3

- move_code：PHENOMENON

- locator：Introduction P2 S1-S3

- function_cn：描述标准放疗实践中依赖医生经验、剂量均一化的现象及其风险证据。

- paraphrase_cn：多数早期乳腺癌患者术后接受放疗；尽管总体目标明确，多种因素使个体优化困难；医生依靠领域知识和经验，但已有研究显示常规放疗可能提高肺癌和心脏病风险。

- depends_on_cn：乳腺癌负担背景

- sets_up_cn：引出“知识驱动/经验式计划是否有效”的问题。

#### 3. Introduction P2 S4

- move_code：GAP

- locator：Introduction P2 S4

- function_cn：明确提出问题：知识驱动或经验式治疗计划对个体是否有效，缺乏系统回答。

- paraphrase_cn：这引发一个问题：这些基于知识和经验的治疗计划在多大程度上对个体患者有效？

- depends_on_cn：现象描述

- sets_up_cn：为研究问题提供动机。

#### 4. Introduction P3 S1

- move_code：RQ_OR_OBJECTIVE

- locator：Introduction P3 S1

- function_cn：陈述正式研究问题，并介绍设计科学方案。

- paraphrase_cn：研究问题是：如何纳入患者特异性信息预测治疗结果并调整治疗计划？作者采用设计科学范式提出预测+优化框架。

- depends_on_cn：GAP

- sets_up_cn：定义核心制品。

#### 5. Introduction P3 S2-S3

- move_code：DESIGN_FEATURE

- locator：Introduction P3 S2-S3

- function_cn：简要描述框架组成和个性化机制。

- paraphrase_cn：预测模型整合治疗轨迹中的患者和临床信息，优化模型基于临床目标和预测结果优化计划，因此可实现个体化定制。

- depends_on_cn：RQ

- sets_up_cn：为评价部分铺垫。

#### 6. Introduction P4 S1

- move_code：METHOD_JUSTIFICATION

- locator：Introduction P4 S1

- function_cn：说明用合成患者而非真实患者评价。

- paraphrase_cn：作者基于真实临床数据集创建合成患者进行框架评价。

- depends_on_cn：框架设计

- sets_up_cn：引出核心结果。

#### 7. Introduction P4 S2-S3

- move_code：RESULT

- locator：Introduction P4 S2-S3

- function_cn：报告主要量化结果。

- paraphrase_cn：仿真实验显示个性化计划可减少肺和心脏平均剂量超90%，降低肺癌和心脏病风险；按年度新发病人数，可节约超2亿美元治疗成本。

- depends_on_cn：仿真方法

- sets_up_cn：为贡献陈述提供证据。

#### 8. Introduction P5-P7

- move_code：CONTRIBUTION

- locator：Introduction P5-P7

- function_cn：依次陈述三大贡献：HIT设计、HIT影响测量、临床试验替代。

- paraphrase_cn：第一，填补HIT治疗决策支持设计研究不足；第二，以微观层面量化HIT对结局和成本的影响；第三，以仿真克服临床试验比较替代计划的成本和时间限制。

- depends_on_cn：GAP和RESULT

- sets_up_cn：为讨论部分埋下理论贡献线索。

#### 9. Introduction P8

- move_code：STUDY_OVERVIEW

- locator：Introduction P8

- function_cn：预告论文结构。

- paraphrase_cn：第2节综述文献和临床背景；第3节描述框架；第4节评价；第5节讨论和未来。

- depends_on_cn：前面所有内容

- sets_up_cn：给读者读文章路径。

### theory_and_knowledge_moves

#### 1. Section 2.1 第一段

- move_code：PRIOR_KNOWLEDGE

- locator：Section 2.1 第一段

- function_cn：介绍医疗预测分析定义及已知应用。

- paraphrase_cn：预测分析利用多源数据预测未来事件，已在风险患者识别、急诊分诊、临床试验设计、流行病监测等领域有成效。

- depends_on_cn：

- sets_up_cn：建立该领域的基础背景。

#### 2. Section 2.1 第四段

- move_code：LIMITATION

- locator：Section 2.1 第四段

- function_cn：指出模型自由方法的限制（可解释性差、数据需求大）。

- paraphrase_cn：模型自由方法灵活性高但缺乏可解释性和透明度，可能引致不信任；且需要大量数据，临床中常缺乏。

- depends_on_cn：预测分析综述

- sets_up_cn：为选用模型驱动方法作借口。

#### 3. Section 2.1 第五段

- move_code：GAP

- locator：Section 2.1 第五段

- function_cn：指出当前患者级分析聚焦诊断/预测，不用于治疗决策。

- paraphrase_cn：现有病人级分析大多改善诊断或预测不良事件以便干预；本文不同于它们，旨在开发预测模型辅助医生治疗决策。

- depends_on_cn：预测分析综述

- sets_up_cn：给出文献缺口并对比最接近文献Meyer et al. (2014)。

#### 4. Section 2.2 第一段

- move_code：THEORY_INTRO

- locator：Section 2.2 第一段

- function_cn：引入个性化医学概念并说明其承诺。

- paraphrase_cn：个性化医学把治疗计划、策略和药物定制给个体，以改善生存、减少副作用并可能降低整体成本。

- depends_on_cn：

- sets_up_cn：为后文使用个性化计划铺路。

#### 5. Section 2.2 第二段

- move_code：LIMITATION

- locator：Section 2.2 第二段

- function_cn：说明遗传驱动的个性化目前仅限于少数疾病，且需要基础设施和分析工具。

- paraphrase_cn：基因组学进展带来可能性，但目前遗传个性化仅限于少数疾病；需要HIE等基础设施和分析工具支持。

- depends_on_cn：个性化医学概念

- sets_up_cn：引出HIT基础设施和仿真方法的需要。

#### 6. Section 2.2 第三段

- move_code：PRIOR_KNOWLEDGE

- locator：Section 2.2 第三段

- function_cn：给出已有仿真的做法和代表研究。

- paraphrase_cn：仿真可以在无真实患者的情况下比较多种治疗方案；例如HIV治疗策略和MS患者的自适应治疗策略。

- depends_on_cn：

- sets_up_cn：为本文采用仿真评价做合理性辩护。

#### 7. Section 2.3 第三段

- move_code：GAP

- locator：Section 2.3 第三段

- function_cn：指出放疗优化文献只关注处方剂量后的递送优化，缺少初始最优剂量确定。

- paraphrase_cn：现有文献限于优化处方剂量的递送，对如何首先确定个体患者最优辐射剂量的理解有限。

- depends_on_cn：放疗文献回顾

- sets_up_cn：建立本文核心缺口并引出Table 1。

#### 8. Section 2.3 第四段

- move_code：THEORY_INTRO

- locator：Section 2.3 第四段

- function_cn：引入dose-painting概念，作为本文框架的精神来源。

- paraphrase_cn：剂量绘画概念旨在通过适应患者异质性取得更好权衡；已在其他癌症中实施；乳腺癌因MTC不可直接成像尚未实现。

- depends_on_cn：放疗优化综述和缺口

- sets_up_cn：把本文框架定位为对dose-painting的乳腺癌实现。

### artifact_design_moves

#### 1. Section 3 开头两句

- move_code：REQUIREMENT

- locator：Section 3 开头两句

- function_cn：提出临床需求：放疗计划需要平衡肿瘤控制和正常组织毒性，而医生无法充分处理复杂因素。

- paraphrase_cn：放疗目标明确，但复杂生物物理过程使医生无法完全纳入个体临床档案，因此需要决策支持。

- depends_on_cn：Section 2的临床问题与缺口

- sets_up_cn：引入设计科学框架和制品。

#### 2. Section 3 第二段

- move_code：THEORY_INTRO

- locator：Section 3 第二段

- function_cn：引入设计科学范式作为开发方法。

- paraphrase_cn：作者采用IS设计科学范式，该范式为构建IT制品提供处方，并在医疗领域已有先例。

- depends_on_cn：

- sets_up_cn：为之后表述“基于kernel theory开发”建立合法性。

#### 3. Section 3 第三段

- move_code：THEORY_PROPOSITION

- locator：Section 3 第三段

- function_cn：说明临床肿瘤学作为核心理念指导建模。

- paraphrase_cn：由于缺少个性化放疗决策支持设计指南，作者用临床肿瘤学文献模拟辐射剂量与肿瘤进展关系，并采用决策理论方法优化剂量。

- depends_on_cn：设计科学范式

- sets_up_cn：引出预测模型和优化模型正式构建。

#### 4. Section 3.1 一开始

- move_code：MECHANISM

- locator：Section 3.1 一开始

- function_cn：解释TCP模型的生物机制。

- paraphrase_cn：TCP定义为治疗后无克隆源细胞存活的概率；细胞存活量随剂量指数降低；高放射敏感性和大细胞数决定所需剂量。

- depends_on_cn：临床肿瘤学知识

- sets_up_cn：为TCP公式提供生物学依据。

#### 5. Section 3.1 公式(3)

- move_code：DESIGN_FEATURE

- locator：Section 3.1 公式(3)

- function_cn：给出纳入异质性的TCP模型。

- paraphrase_cn：将残留MTC体积、密度、放射敏感性作为随机变量，基于概率密度积分计算TCP。

- depends_on_cn：TCP机制

- sets_up_cn：为后续参数估计和优化提供函数形式。

#### 6. Section 3.1 第四段

- move_code：MECHANISM

- locator：Section 3.1 第四段

- function_cn：解释MTC建模采用随机分布的依据。

- paraphrase_cn：由于MTC无法直接检测，作者依据临床肿瘤学研究，用零膨胀泊松分布建模术前MTC体积、高斯分布建模密度，并考虑术后组织变形。

- depends_on_cn：临床证据

- sets_up_cn：进入参数估计。

#### 7. Section 3.1 第五段

- move_code：METHOD_JUSTIFICATION

- locator：Section 3.1 第五段

- function_cn：解释为何选模型驱动而非数据驱动。

- paraphrase_cn：机器学习方法需要大样本高质量数据，这在放疗中罕见；模型驱动虽简化但可解释性高，在临床中重要。

- depends_on_cn：Section 2.1对数据驱动限制的讨论

- sets_up_cn：为选用Bayesian/MCMC和TCP模型辩护。

#### 8. Section 3.2 开头三段

- move_code：REQUIREMENT

- locator：Section 3.2 开头三段

- function_cn：给出优化模型的两个场景和一个中间步骤。

- paraphrase_cn：无剂量约束场景；总剂量不超过66 Gy场景；先优化患者组作为临床实践和个人化之间的中间步骤。

- depends_on_cn：预测模型

- sets_up_cn：定义优化问题。

#### 9. Section 3.2.1 公式(12)-(13)

- move_code：DESIGN_FEATURE

- locator：Section 3.2.1 公式(12)-(13)

- function_cn：形式化优化问题：最小化平均剂量，subject to TCP目标。

- paraphrase_cn：目标函数是乳腺平均剂量；约束是达到目标TCP；约束场景额外要求各距离剂量≤66 Gy。

- depends_on_cn：预测模型和临床目标

- sets_up_cn：为算法求解提供数学框架。

#### 10. Section 3.2.1 倒数第二段

- move_code：METHOD_JUSTIFICATION

- locator：Section 3.2.1 倒数第二段

- function_cn：解释为何用Adam优化算法。

- paraphrase_cn：TCP函数强非线性、随机优化问题、梯度噪声和稀疏，Adam只需一阶梯度和内存少，适合非平稳随机设置。

- depends_on_cn：优化问题复杂性

- sets_up_cn：为后文的算法对照提供方法选择依据。

#### 11. Section 3.2.2 第一段

- move_code：DESIGN_FEATURE

- locator：Section 3.2.2 第一段

- function_cn：定义个体剂量绘画计划的取舍和前提。

- paraphrase_cn：个体计划成本高且耗时；它需要细粒度组织学检查；但作者坚持个体化问题不能被技术和成本限制回避，并预测未来数字病理工具会使其可行。

- depends_on_cn：优化模型

- sets_up_cn：为个体剂量绘画计划命名并引入评价。

### evaluation_moves

#### 1. Section 4.1 第一段+Table 2

- move_code：BENCHMARK_OR_CONTRAST

- locator：Section 4.1 第一段+Table 2

- function_cn：定义评价基准：标准均匀计划；系统/随机误差作为工况。

- paraphrase_cn：评价将标准均匀计划与最优计划对比，并考虑三种setup误差：0、1、5 mm。

- depends_on_cn：临床实践和已有误差文献

- sets_up_cn：给出后续全部计划和命名。

#### 2. Section 4.1.1 第三至四段

- move_code：RESULT

- locator：Section 4.1.1 第三至四段

- function_cn：报告群组最优计划相比标准计划的剂量下降。

- paraphrase_cn：TCP 90%无误差时无约束最优计划平均剂量降低94.7%，约束降低91.4%；5 mm误差下仍降低约90%。

- depends_on_cn：Table 3

- sets_up_cn：说明群组可带来巨大改善。

#### 3. Section 4.1.2 第二至三段

- move_code：RESULT

- locator：Section 4.1.2 第二至三段

- function_cn：报告个体剂量绘画计划的剂量下降。

- paraphrase_cn：TCP 90%时剂量绘画计划平均剂量为1.2-3.0 Gy，相比54 Gy降低约94.4%。

- depends_on_cn：Table 4

- sets_up_cn：证明个体化比群组更优。

#### 4. Section 4.2 第一段

- move_code：BENCHMARK_OR_CONTRAST

- locator：Section 4.2 第一段

- function_cn：引入优化方法对照：Adam vs L-BFGS-B vs SA vs GA。

- paraphrase_cn：为展示计算有效性，作者比较三种广泛使用的随机优化方法和Adam。

- depends_on_cn：框架采用Adam

- sets_up_cn：为Table 5-6的结果做准备。

#### 5. Section 4.2 第三段

- move_code：RESULT

- locator：Section 4.2 第三段

- function_cn：报告算法对照结果。

- paraphrase_cn：Adam在两个性能维度上一致领先：SA/GA更慢且易陷入局部最优；L-BFGS-B结局接近但不高效。

- depends_on_cn：Table 5-6

- sets_up_cn：支持框架实际可用的说法。

#### 6. Section 4.3 第一段

- move_code：BENCHMARK_OR_CONTRAST

- locator：Section 4.3 第一段

- function_cn：把经济分析建立在已发表的剂量-风险线性关系上。

- paraphrase_cn：作者引用已发表的剂量-反应临床研究，把平均剂量降低映射为风险降低。

- depends_on_cn：Table 4剂量数据

- sets_up_cn：为成本节约计算提供基准。

#### 7. Section 4.3 第三段

- move_code：RESULT

- locator：Section 4.3 第三段

- function_cn：报告成本节约结果。

- paraphrase_cn：每名患者节约约852美元；按276,480年新发病例，年节约约2.355亿美元。

- depends_on_cn：风险降低和成本估计

- sets_up_cn：为讨论中的HIT价值贡献提供数据。

### discussion_and_contribution_moves

#### 1. Section 5 前奏

- move_code：CONTRIBUTION

- locator：Section 5 前奏

- function_cn：总结两项重要进展：结合治疗轨迹信息的模型驱动预测和Adam优化。

- paraphrase_cn：本文首次在乳腺癌放疗计划设计中结合患者特异性信息与放射生物模型预测，并采用Adam求解约束优化问题；据作者所知是首个研究个体放疗计划设计的文章。

- depends_on_cn：第3-4节的设计与结果

- sets_up_cn：为具体研究贡献作铺垫。

#### 2. Section 5.1 第一段

- move_code：CONTRIBUTION

- locator：Section 5.1 第一段

- function_cn：回应Agarwal et al. (2010)的HIT设计号召。

- paraphrase_cn：工作响应IS研究对HIT设计、实施和有意义使用的号召；框架统一统计建模和计算模拟以提供治疗计划优化能力。

- depends_on_cn：前言THEORY_INTRO

- sets_up_cn：把设计科学成果放入IS文献。

#### 3. Section 5.1 第二段

- move_code：CONTRIBUTION

- locator：Section 5.1 第二段

- function_cn：声称对个性化医疗分析研究的贡献。

- paraphrase_cn：当前IS研究聚焦自我健康管理，很少量化分析驱动治疗策略价值；本文通过个性化治疗计划框架填补该空缺。

- depends_on_cn：Section 2.2的个性化医学综述

- sets_up_cn：把领域知识作为IS研究的理论延伸。

#### 4. Section 5.1 第二段末尾

- move_code：BOUNDARY_CONDITION

- locator：Section 5.1 第二段末尾

- function_cn：限定框架设计原则的可推广范围。

- paraphrase_cn：尽管本研究限于乳腺癌放疗，但设计原则可应用于其他涉及并发症和合并症的慢病治疗计划个性化。

- depends_on_cn：框架设计

- sets_up_cn：为future work留出空间。

#### 5. Section 5.1 第三段

- move_code：CONTRIBUTION

- locator：Section 5.1 第三段

- function_cn：提出关于领域知识和可解释性结合的贡献。

- paraphrase_cn：医疗预测模型需要临床工作流知识和高可解释性；本文通过临床肿瘤学知识建模回应这一挑战，说明如何结合领域知识与患者数据发展临床决策工具。

- depends_on_cn：第3-4节建模选择

- sets_up_cn：将建模选择转化为方法学贡献。

#### 6. Section 5.2 第二段

- move_code：BOUNDARY_CONDITION

- locator：Section 5.2 第二段

- function_cn：指出信息共享障碍和框架落地条件。

- paraphrase_cn：个性化计划的实现需要无缝集成患者在诊断和治疗轨迹中的病历和临床信息；现实中跨部门信息摩擦是主要障碍。

- depends_on_cn：与临床工作流相关的假设

- sets_up_cn：强调实践意义的边界。

#### 7. Section 5.2 第三段

- move_code：BOUNDARY_CONDITION

- locator：Section 5.2 第三段

- function_cn：指出模型驱动方法对未见过治疗方案可预测性优势。

- paraphrase_cn：现有基于记录训练的数据驱动模型不能预测未见过疗法；本文模型基于临床领域知识TCP，可评估新的治疗方案。

- depends_on_cn：模型选择

- sets_up_cn：为筛选临床试验提供实践建议。

#### 8. Section 5.3

- move_code：LIMITATION_AND_FUTURE

- locator：Section 5.3

- function_cn：列出四项主要局限并指明未来方向。

- paraphrase_cn：模型假设简化放射生物过程；未考虑辅助治疗和时间可能偏差；平均剂量不能完全反映个体临床概况；仿真结果需临床验证。

- depends_on_cn：所有设计、数据和评价

- sets_up_cn：结束全文并给出后续研究空间。

## 理论/知识到设计的翻译

### 知识/理论基础

1. 临床肿瘤学中的肿瘤控制概率（TCP）放射生物模型

2. 剂量-反应关系（Darby等，Grantzau等文献）

3. 乳腺癌病理学和MTC分布的知识（病理数据集、Polgar试验等）

4. 随机优化方法（Adam, L-BFGS-B, SA, GA）

5. 设计科学理论（Hevner et al. 2004; Gregor and Hevner 2013）

6. 个性化医学文献（Hamburg and Collins 2010; Aspinall and Hamermesh 2007）

- 理论—设计耦合：direct

- 耦合判定理由：论文的核心设计——TCP预测模型——直接由临床肿瘤学中的放射生物知识（TCP模型）推导而来，MTC的随机建模基于临床病理学分布知识，优化模型的目标函数（最小化平均剂量、约束TCP达到目标）也由临床决策逻辑直接产生。评价实验直接检验了该TCP模型预测的准确性以及基于该模型的优化计划相对标准计划的性能，因此知识基础前瞻性并实质决定了制品。

- 理论到设计翻译链：临床肿瘤学中TCP模型（肿瘤控制概率取决于初始克隆源细胞数、辐射剂量、放射敏感性）→ 将MTC体积/密度/放射敏感性建模为随机变量以刻画患者异质性 → 预测模型采用Bayesian MCMC估计参数，用外部试验和敏感性分析验证 → 用TCP作为优化约束和最小剂量目标 → 将剂量分布D(d)作为决策变量，用Adam求解最小化平均剂量的优化问题 → 生成群组最优计划或个体剂量绘画计划 → 通过仿真对比标准均匀计划，验证剂量大幅下降 → 将剂量下降经临床文献剂量-反应率换算成健康风险和成本节约。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：TCP模型：无克隆源细胞存活概率随剂量指数下降；肿瘤控制需要足够剂量。

- mechanism_cn：辐射剂量杀伤克隆源细胞，细胞存活数N_s=N_0 exp(-αD)；TCP=exp(-N_0 exp(-αD))。

- design_requirement_cn：预测模型必须以患者特异性MTC数量和放射敏感性为输入，并能给出给定剂量下的TCP。

- artifact_choice_cn：TCP模型公式(3)，将V、ρ、α、c作为随机变量；使用病理计量和MTC概率分布。

- evaluated_contrast_cn：预测RMSE、外推一致性、外部试验TCP置信区间。

- objective_result_cn：测试集RMSE 1.3%；外部TCP 93.7%-94.4%接近94.1%；子样本模型预测一致。

##### evidence_pointers

1. Section 3.1 公式(1)-(3)

2. Section 3.1.2

3. Figure 3

#### 2. 2

- theory_or_knowledge_claim_cn：临床放疗目标是控制肿瘤并减少邻近正常组织毒性；平均剂量是毒性的关键指标。

- mechanism_cn：高平均剂量增加肺/心脏等器官吸收剂量，进而提高继发肺癌/心脏病风险。

- design_requirement_cn：优化模型应在达到TCP目标下最小化平均乳腺剂量。

- artifact_choice_cn：优化问题公式(12)-(13)：min AvgDose subject to TCP_N=TCP_target，56约束场景加D(d)≤66 Gy惩罚。

- evaluated_contrast_cn：无约束最优计划/约束最优计划 vs 标准均匀计划在不同setup误差下。

- objective_result_cn：TCP 90%时平均剂量从54 Gy降至2.86-5.15 Gy（群组）；个体计划低至1.2-3.0 Gy。

##### evidence_pointers

1. Section 3.2

2. Table 3-4

3. Figure 4-5

#### 3. 3

- theory_or_knowledge_claim_cn：剂量-反应剂量-风险线性关系：每Gy肺剂量增加8.5%肺癌风险，每Gy心脏剂量增加7.4%主要冠脉事件。

- mechanism_cn：减少平均乳腺剂量等价降低肺/心脏平均剂量，按线性无阈模型降低继发癌症和心脏事件概率。

- design_requirement_cn：个性化计划剂量降低应能转换为可估算的风险和成本收益。

- artifact_choice_cn：以TCP 90%、最大误差5mm场景计算风险差和成本差。

- evaluated_contrast_cn：标准54 Gy vs 个性化3 Gy；文献风险基线与成本数据。

- objective_result_cn：肺剂量降8.22 Gy、心脏剂量降4.63 Gy；肺癌风险降69.8%、心脏病风险降34.2%；年省约2.355亿美元。

##### evidence_pointers

1. Section 4.3

## 评价逻辑

### evaluation_modes

1. 基于真实临床试验数据的预测模型交叉验证

2. 基于外部试验的合成数据验证

3. 敏感性/外推性分析

4. 仿真实验比较标准均匀计划与最优计划

5. 多工况仿真（setup误差0/1/5mm、TCP目标80/90%、约束/无约束）

6. 优化算法基准对照（Adam vs L-BFGS-B vs SA vs GA）

7. 经济成本线性外推估算

- why_these_evaluations_cn：由于随机临床试验比较大量治疗方案在成本和随访时间上不可行，作者采用仿真作为主要评价方式。预测模型必须先经真实临床数据验证（交叉验证和外部合成验证）才能作为优化模型的可信输入；随后需要通过系统变化TCP目标、剂量上限、setup误差来检验最优计划的边界；最后将剂量差异外推为经济收益，以回扣HIT价值量化缺口。算法对照用于证明框架在实际临床计算中可用。

- benchmark_and_contrast_chain_cn：首先以“标准均匀计划”作为主流临床实践基准，建立剂量差异；接着以TCP目标下的平均剂量作为首要指标，在无约束/有约束、群组/个体两个维度构造差额；再用与基准优化方法（L-BFGS-B、SA、GA）的对照来确立Adam作为精确且高效求解器的地位；最后用已发表文献的剂量-反应率作为另一层基准，把剂量差转成风险差和成本差。这种逐步加入新基准的方法使证据从“性能差异”逐渐上升为“机制可解释的健康风险/经济收益”。

### claim_evidence_ledger

#### 1. 预测模型能准确预测放疗后TCP。

- claim_cn：预测模型能准确预测放疗后TCP。

- evidence_cn：EORTC+EBCTCG数据的交叉验证RMSE为1.3%；外部Polgar合成验证TCP置信区间接近报道值。

- status_cn：有直接量化证据支持，但外部验证是合成患者而非真实个体预测。

#### 2. 最优计划相对标准计划显著降低平均剂量。

- claim_cn：最优计划相对标准计划显著降低平均剂量。

- evidence_cn：Table 3/4和图4/5显示TCP 90%下平均剂量降低约90%以上。

- status_cn：有仿真证据支持；指标是平均剂量，不直接等同真实临床器官剂量或副作用。

#### 3. 剂量降低能够显著降低肺癌/心脏疾病风险。

- claim_cn：剂量降低能够显著降低肺癌/心脏疾病风险。

- evidence_cn：引用Grantzau 2014和Darby 2013的风险系数按线性外推。

- status_cn：风险降低是外推计算，不是对个性化计划直接测量。

#### 4. 框架可节约每年超2亿美元治疗成本。

- claim_cn：框架可节约每年超2亿美元治疗成本。

- evidence_cn：根据平均剂量降低、风险降低、单病种平均成本和年新发病例数计算。

- status_cn：点估计，依赖文献风险系数和成本假设，作者称未含其他副作用所以保守。

#### 5. Adam是高效且表现优良的优化方法。

- claim_cn：Adam是高效且表现优良的优化方法。

- evidence_cn：Table 5/6显示平均剂量更低且时间更短。

- status_cn：有仿真对照支持，但仅在论文实验设置和患者参数下验证。

#### 6. 模型能把临床知识结合进预测并能评价未见过治疗方案。

- claim_cn：模型能把临床知识结合进预测并能评价未见过治疗方案。

- evidence_cn：模型基于TCP机制而非纯数据驱动；敏感性分析支持外推。

- status_cn：推理和敏感性支持，未用真实未见过方案直接实验验证。

- internal_validity_strategy_cn：通过100次重复仿真减少先验带来的偏差；使用Heidelberger-Welch检验确保MCMC收敛；通过100次重复交叉验证评估预测稳定性；通过子样本训练模型比较预测一致性来检验外推问题；通过固定合成患者生成过程和误差设置来保证组间比较公平。

- external_validity_strategy_cn：使用真实EORTC/EBCTCG试验数据和病理数据集估计参数；使用外部Polgar试验数据抽样的合成患者验证预测；使用不同setup误差（0/1/5mm）和TCP目标（80/90%）以及约束/无约束场景扩展评价外部边界；经济分析使用真实年度新发病人数和治疗成本数据。

- what_is_not_actually_tested_cn：论文未在真实患者或真实放疗中心部署该框架，未进行随机对照临床验证；未测量真实的器官剂量体积直方图或长期患者随访结局；未直接观察MTC分布；未检验信息在真实临床工作流中无缝可得这一假设；未评估辅助治疗或放疗时序影响；经济收益也是线性外推，而非实际支付或保险数据分析。

## 贡献闭环

- technical_claim_cn：在给定TCP目标下，基于Adam的优化方法能生成相对现有标准均匀计划平均剂量显著更低的剂量分布，且比L-BFGS-B、SA、GA更高效；预测模型在临床数据上RMSE为1.3%，外部合成验证接近报道TCP。

- artifact_claim_cn：论文提出的个性化治疗计划框架（预测模型+优化模型）导致剂量降低和风险降低；具体可识别设计部分是模型驱动的TCP预测和Adam优化，缺一不可。

- mechanism_claim_cn：通过把患者特异性MTC分布和放射敏感性纳入TCP预测，可以使剂量集中在高风险区域，避免在无MTC区域过度照射，从而以更低平均剂量达到同样肿瘤控制目标；由此减少邻近器官辐射暴露和继发风险。

- boundary_claim_cn：在早期乳腺癌术后放疗场景、外部射线放疗、模型假设（无辅助治疗、不考虑放疗时间）下成立；在信息可无缝整合的医疗机构中适用；setup误差增加时优势仍稳健但幅度略减；适用于其他涉及合并症的慢病治疗计划设计原则可迁移。

- reusable_design_knowledge_cn：在医疗决策支持系统设计中，应优先使用基于领域知识的解释性预测模型而非纯黑箱模型；应把治疗轨迹中的患者特异性信息（病理、临床特征）转化为可计算概率分布；将预测模型嵌入优化目标可实现个性化治疗计划；选择随机优化算法时应兼顾患者指标和计算效率。

- theoretical_contribution_cn：文章声称扩展了HIT设计和有意义使用研究，把设计科学框架应用于治疗计划支持；回应Agarwal et al. (2010)对微观和细粒度HIT影响研究的呼吁；连接了个性化医学与IS分析，并提供了一个将领域知识（放射生物学）纳入预测建模的范例。

- how_discussion_closes_intro_gap_cn：讨论明确指出，本文填补的正是引言中提到的“HIT在治疗决策支持中研究不足”和“患者级分析很少用于治疗决策”的缺口；同时通过估计经济效益，回应引言提出的乳腺癌经济负担和对HIT价值微观估计的需求；通过说明“第一个研究个体放疗计划设计”来突出新颖性。

- overclaim_or_unsupported_leaps_cn：最大的跳跃是把仿真中的平均剂量降低直接外推为临床风险降低和年度2.355亿美元成本节约：风险降低基于文献平均剂量-反应率，而个性化计划的空间剂量分布与标准均匀计划的结构不同，可能不满足简单线性外推；成本节约基于风险差乘治疗费用，未考虑额外个性化检测、数字病理实施成本、住院成本、潜在不完全依从性；同时作者称“第一个研究个体放疗计划设计”是强声明，可能在放疗物理非IS文献中存在近似工作。

## 句级写作动作图谱

### 1. Abstract P1 S1-S2

- order：1

- section：Abstract

- locator：Abstract P1 S1-S2

- move_code：CONTEXT

- paraphrase_cn：乳腺癌是全球女性癌症死亡的主要原因，治疗复杂且需要多学科信息密集流程协作。

- rhetorical_function_cn：用最强疾病统计和复杂性界定现实问题。

- depends_on_cn：无

- sets_up_cn：为个性化计划难题提供规模和重要性。

- evidence_pointer：Abstract P1

### 2. Abstract P2 S1

- order：2

- section：Abstract

- locator：Abstract P2 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：核心框架由预测模型和优化模型组成：前者根据临床和患者特征预测计划结果，后者根据预测结果优化计划。

- rhetorical_function_cn：第一时间告诉读者制品结构。

- depends_on_cn：问题背景

- sets_up_cn：作为摘要中的核心方法。

- evidence_pointer：Abstract P2

### 3. Abstract P2 S2-S4

- order：3

- section：Abstract

- locator：Abstract P2 S2-S4

- move_code：RESULT

- paraphrase_cn：仿真实验显示框架生成的计划一致优于现有实践，在降低复发和辐射副作用风险以及成本方面有优势。

- rhetorical_function_cn：给出摘要层面的主要结果。

- depends_on_cn：框架设计

- sets_up_cn：支撑贡献声明。

- evidence_pointer：Abstract P2

### 4. Abstract P3 S1

- order：4

- section：Abstract

- locator：Abstract P3 S1

- move_code：CONTRIBUTION

- paraphrase_cn：作者声称研究贡献于HIT在成本有效医疗中的研究，以及向临床提供有实用价值的模型和工具。

- rhetorical_function_cn：总结研究意义，使摘要完整。

- depends_on_cn：结果

- sets_up_cn：为引言贡献段落提供模板。

- evidence_pointer：Abstract P3

### 5. Introduction P1

- order：5

- section：Introduction

- locator：Introduction P1

- move_code：CONTEXT

- paraphrase_cn：乳腺癌是最常见女性癌症，美国超350万女性确诊，治疗费用达165亿美元。

- rhetorical_function_cn：建立现实负担和成本背景。

- depends_on_cn：无

- sets_up_cn：为后文提出的成本节约做伏笔。

- evidence_pointer：Introduction P1

### 6. Introduction P2 S1-S3

- order：6

- section：Introduction

- locator：Introduction P2 S1-S3

- move_code：PHENOMENON

- paraphrase_cn：多数早期乳腺癌患者术后接受放疗；放疗目标看似简单，但多因素交互使优化困难；医生依赖知识和经验制定计划，已有研究表明传统放疗会增加肺癌和心脏病风险。

- rhetorical_function_cn：描述具体临床实践现象及其风险。

- depends_on_cn：乳腺癌负担

- sets_up_cn：推出经验式计划有效性疑问。

- evidence_pointer：Introduction P2

### 7. Introduction P2 S4

- order：7

- section：Introduction

- locator：Introduction P2 S4

- move_code：GAP

- paraphrase_cn：这引发问题：知识和经验驱动的治疗计划对个体患者在多大程度上有效？

- rhetorical_function_cn：把现象转化为可研究的问题。

- depends_on_cn：现象描述

- sets_up_cn：引出研究问题。

- evidence_pointer：Introduction P2 S4

### 8. Introduction P3 S1

- order：8

- section：Introduction

- locator：Introduction P3 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：研究问题为：如何纳入患者特异性信息预测治疗结果并适应个体患者治疗计划？

- rhetorical_function_cn：正式提出研究问题。

- depends_on_cn：GAP

- sets_up_cn：引出设计科学框架。

- evidence_pointer：Introduction P3 S1

### 9. Introduction P3 S2-S3

- order：9

- section：Introduction

- locator：Introduction P3 S2-S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：框架包含预测模型和优化模型，利用治疗轨迹中的患者和临床信息实现个性化。

- rhetorical_function_cn：先概览制品，避免读者迷失。

- depends_on_cn：RQ

- sets_up_cn：为正文第3节详细设计铺垫。

- evidence_pointer：Introduction P3 S2-S3

### 10. Introduction P4 S1-S3

- order：10

- section：Introduction

- locator：Introduction P4 S1-S3

- move_code：RESULT

- paraphrase_cn：基于真实临床数据创建合成患者进行仿真评价，发现个性化计划可减少肺/心脏平均剂量超90%，并降低继发风险，年节约超2亿美元。

- rhetorical_function_cn：在引言中给出最强量化结果，吸引读者。

- depends_on_cn：框架设计

- sets_up_cn：为贡献声明提供实证基础。

- evidence_pointer：Introduction P4

### 11. Introduction P5 S1-S2

- order：11

- section：Introduction

- locator：Introduction P5 S1-S2

- move_code：CONTRIBUTION

- paraphrase_cn：第一项贡献：为HIT设计研究提供新的个性化放疗决策支持框架，填补HIT在治疗决策支持方面研究不足。

- rhetorical_function_cn：将问题定位于IS领域，而非纯医疗AI。

- depends_on_cn：文献缺口和设计科学背景

- sets_up_cn：为讨论部分进行贡献陈述提供模板。

- evidence_pointer：Introduction P5

### 12. Introduction P6 S1-S2

- order：12

- section：Introduction

- locator：Introduction P6 S1-S2

- move_code：CONTRIBUTION

- paraphrase_cn：第二项贡献：回应Agarwal等人的呼吁，在微观层面量化HIT框架对患者结局和治疗成本的影响。

- rhetorical_function_cn：把本文定位为HIT影响评估研究。

- depends_on_cn：HIT文献

- sets_up_cn：为经济效益分析提供理由。

- evidence_pointer：Introduction P6

### 13. Introduction P7 S1-S4

- order：13

- section：Introduction

- locator：Introduction P7 S1-S4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：临床试验虽有黄金标准地位，但昂贵且随访长，限制了对个体替代计划的比较；因此本文用仿真评价各治疗方案并揭示未被试验测试的计划。

- rhetorical_function_cn：为使用仿真而非临床实验辩护。

- depends_on_cn：个性化医学现实限制

- sets_up_cn：为第4节仿真评价提供方法论合法性。

- evidence_pointer：Introduction P7

### 14. Introduction P8

- order：14

- section：Introduction

- locator：Introduction P8

- move_code：STUDY_OVERVIEW

- paraphrase_cn：第2节文献综述和临床背景，第3节框架，第4节评价，第5节讨论。

- rhetorical_function_cn：给读者阅读地图。

- depends_on_cn：前面内容

- sets_up_cn：让读者预期后续章节。

- evidence_pointer：Introduction P8

### 15. Section 2.1 第一段

- order：15

- section：Section 2.1

- locator：Section 2.1 第一段

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：预测分析在医疗中的常见应用包括高风险患者识别、急诊分诊、临床试验设计和流行病监测。

- rhetorical_function_cn：建立医疗预测分析领域的背景和范围。

- depends_on_cn：

- sets_up_cn：随后对比诊断/预测和本文治疗决策预测。

- evidence_pointer：Section 2.1

### 16. Section 2.1 第三段

- order：16

- section：Section 2.1

- locator：Section 2.1 第三段

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：预测方法可分为模型驱动（依靠参数假设）和数据驱动（较少假设，尤其是深度学习方法广泛应用）。

- rhetorical_function_cn：给出方法论分类，为模型选择提供框架。

- depends_on_cn：领域综述

- sets_up_cn：为后续“选用模型驱动”做铺垫。

- evidence_pointer：Section 2.1 第三段

### 17. Section 2.1 第四段

- order：17

- section：Section 2.1

- locator：Section 2.1 第四段

- move_code：LIMITATION

- paraphrase_cn：模型自由方法缺乏可解释性和透明度，且通常需要大量数据，临床数据常不足。

- rhetorical_function_cn：指出数据驱动方法的关键限制。

- depends_on_cn：方法分类

- sets_up_cn：为TCP模型驱动方法提供理由。

- evidence_pointer：Section 2.1 第四段

### 18. Section 2.1 第五段

- order：18

- section：Section 2.1

- locator：Section 2.1 第五段

- move_code：GAP

- paraphrase_cn：现有患者级分析主要改善诊断或预测不良事件，很少用于辅助治疗决策；最接近文献Meyer et al. (2014)关注糖尿病治疗决策，但它采用现有患者模型，而本文聚焦个体放疗计划优化。

- rhetorical_function_cn：精确标记与现有分析的差异。

- depends_on_cn：医疗预测分析综述

- sets_up_cn：把治疗决策支持定义为本文的独特定位。

- evidence_pointer：Section 2.1 第五段

### 19. Section 2.2 第一段

- order：19

- section：Section 2.2

- locator：Section 2.2 第一段

- move_code：THEORY_INTRO

- paraphrase_cn：个性化医学将治疗计划、策略和药物定制给个体，以改善生存并降低副作用和整体成本。

- rhetorical_function_cn：引入个性化医学作为第二根知识支柱。

- depends_on_cn：

- sets_up_cn：为“个性化剂量”提供理论背景。

- evidence_pointer：Section 2.2 第一段

### 20. Section 2.2 第二段

- order：20

- section：Section 2.2

- locator：Section 2.2 第二段

- move_code：LIMITATION

- paraphrase_cn：遗传驱动的个性化仅限于少数疾病，需要基础设施和分析工具如HIE；Yaraghi和Demirezen等研究了HIE平台。

- rhetorical_function_cn：指出当前个性化医学的障碍不止基因检测，还包括信息基础设施。

- depends_on_cn：个性化医学概念

- sets_up_cn：为后文信息共享重要性的讨论预埋伏笔。

- evidence_pointer：Section 2.2 第二段

### 21. Section 2.2 第三段

- order：21

- section：Section 2.2

- locator：Section 2.2 第三段

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：由于无法对所有治疗方案做临床试验，医生常无证据地外推；仿真可避免真实患者代价地比较许多方案，例如HIV和多发性硬化治疗策略研究。

- rhetorical_function_cn：为仿真研究建立文献基础。

- depends_on_cn：临床试验成本限制

- sets_up_cn：为后文仿真评价提供正当化。

- evidence_pointer：Section 2.2 第三段

### 22. Section 2.3 第一至二段

- order：22

- section：Section 2.3

- locator：Section 2.3 第一至二段

- move_code：CONTEXT

- paraphrase_cn：放疗广泛用于乳腺癌症术后，有效降低局部复发并提高生存率，但伴随肺和心脏照射风险；平衡复发风险和正常组织损伤很关键。

- rhetorical_function_cn：提供放射治疗的临床背景。

- depends_on_cn：乳腺癌负担

- sets_up_cn：引出优化放疗的需求。

- evidence_pointer：Section 2.3 第一段

### 23. Section 2.3 第二段

- order：23

- section：Section 2.3

- locator：Section 2.3 第二段

- move_code：PHENOMENON

- paraphrase_cn：微肿瘤细胞无法被影像直接检测只能通过病理组织学识别；临床试验比较替代方案需要大量患者和长时间；标准方案未考虑肿瘤或患者异质性，可能导致次优结局。

- rhetorical_function_cn：解释放疗个性化的具体障碍。

- depends_on_cn：临床背景

- sets_up_cn：为“需要基于病理和轨迹信息建模”做准备。

- evidence_pointer：Section 2.3 第二段

### 24. Section 2.3 第三段

- order：24

- section：Section 2.3

- locator：Section 2.3 第三段

- move_code：GAP

- paraphrase_cn：现有IMRT优化文献聚焦于处方剂量后的递送优化，而对如何先确定每个患者的最优辐射剂量理解有限。

- rhetorical_function_cn：提出对放疗计划研究的核心缺口。

- depends_on_cn：放疗优化文献综述和一些代表研究

- sets_up_cn：引出Table 1和本文对最优剂量确定的贡献。

- evidence_pointer：Section 2.3 第三段

### 25. Section 2.3 第四段

- order：25

- section：Section 2.3

- locator：Section 2.3 第四段

- move_code：THEORY_INTRO

- paraphrase_cn：剂量绘画概念意图按患者异质性调整不同区域的剂量，以实现复发和副作用权衡；在乳腺癌中因MTC不可直接成像而难以实现。

- rhetorical_function_cn：把本文框架与临床前沿概念对接。

- depends_on_cn：GAP和放疗技术背景

- sets_up_cn：为“用治疗轨迹信息估计MTC分布”的创新铺垫。

- evidence_pointer：Section 2.3 第四段

### 26. Section 3 第一段

- order：26

- section：Section 3

- locator：Section 3 第一段

- move_code：REQUIREMENT

- paraphrase_cn：放疗计划需要在肿瘤控制和正常组织毒性间取得平衡，而医生无法仅凭临床知识充分整合患者具体特征，因此需要决策支持。

- rhetorical_function_cn：从需求角度引入制品。

- depends_on_cn：临床问题定义

- sets_up_cn：为采用设计科学范式和TCP建模提供目标。

- evidence_pointer：Section 3 第一段

### 27. Section 3 第二段

- order：27

- section：Section 3

- locator：Section 3 第二段

- move_code：THEORY_INTRO

- paraphrase_cn：研究采用IS设计科学范式，该范式提供解决IS设计和实现问题的规范，并在医疗领域已有Meyer、Lin、Son等例子。

- rhetorical_function_cn：为制品开发过程提供方法论标识。

- depends_on_cn：需求

- sets_up_cn：说明接下来框架是合法的设计科学制品。

- evidence_pointer：Section 3 第二段

### 28. Section 3 第三段

- order：28

- section：Section 3

- locator：Section 3 第三段

- move_code：THEORY_PROPOSITION

- paraphrase_cn：缺少设计指南时可用kernel theory：作者用临床肿瘤学文献刻画辐射剂量与肿瘤发展关系，并采用决策理论优化剂量。

- rhetorical_function_cn：把理论引入为设计基础。

- depends_on_cn：设计科学范式

- sets_up_cn：引出TCP预测模型。

- evidence_pointer：Section 3 第三段

### 29. Section 3.1 第一段

- order：29

- section：Section 3.1

- locator：Section 3.1 第一段

- move_code：MECHANISM

- paraphrase_cn：TCP定义为治疗后无克隆源细胞存活的概率；存活细胞数量依赖剂量、初始细胞数、放射敏感性。

- rhetorical_function_cn：解释TCP模型的生物学机理。

- depends_on_cn：临床肿瘤学知识

- sets_up_cn：为TCP公式提供依据。

- evidence_pointer：Section 3.1 公式(1)-(2)

### 30. Section 3.1 第二段

- order：30

- section：Section 3.1

- locator：Section 3.1 第二段

- move_code：DESIGN_FEATURE

- paraphrase_cn：为刻画患者内和患者间异质性，将残留MTC体积、密度、放射敏感性作为随机变量，用积分公式得到TCP。

- rhetorical_function_cn：给出研究所用TCP模型的具体形式。

- depends_on_cn：TCP机制和临床知识

- sets_up_cn：为参数估计和优化做数学准备。

- evidence_pointer：Section 3.1 公式(3)

### 31. Section 3.1 第四段

- order：31

- section：Section 3.1

- locator：Section 3.1 第四段

- move_code：MECHANISM

- paraphrase_cn：MTC不可直接检测，因此使用治疗轨迹中的患者和临床信息建模其分布，如零膨胀泊松分布和高斯分布，并考虑术后组织变形。

- rhetorical_function_cn：解释MTC建模的临床依据。

- depends_on_cn：临床病理知识

- sets_up_cn：为参数估计提供具体模型结构。

- evidence_pointer：Section 3.1 第四段

### 32. Section 3.1 第五段

- order：32

- section：Section 3.1

- locator：Section 3.1 第五段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：数据驱动方法需要大样本高质量数据且缺乏可解释性；本文选择模型驱动并强调可解释性在临床中的重要性。

- rhetorical_function_cn：为模型选择做方法论辩护。

- depends_on_cn：Section 2.1限制

- sets_up_cn：为后续Bayesian/MCMC估计方法做铺垫。

- evidence_pointer：Section 3.1 第五段

### 33. Section 3.1.1 第一段

- order：33

- section：Section 3.1.1

- locator：Section 3.1.1 第一段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用病理数据集估计MTC模型参数，用EORTC和EBCTCG临床数据估计TCP中克隆源细胞分数和放射敏感性。

- rhetorical_function_cn：说明参数估计的数据来源。

- depends_on_cn：TCP模型

- sets_up_cn：为Bayesian MCMC估计提供数据准备。

- evidence_pointer：Section 3.1.1

### 34. Section 3.1.1 第二至五段

- order：34

- section：Section 3.1.1

- locator：Section 3.1.1 第二至五段

- move_code：RESULT

- paraphrase_cn：通过Bayesian MCMC和100次重复仿真的似然估计，所有估计值通过Heidelberger-Welch收敛检验。

- rhetorical_function_cn：报告估计方法的成功执行。

- depends_on_cn：数据和模型

- sets_up_cn：为验证结果铺路。

- evidence_pointer：Section 3.1.1

### 35. Section 3.1.2 第一段

- order：35

- section：Section 3.1.2

- locator：Section 3.1.2 第一段

- move_code：RESULT

- paraphrase_cn：交叉验证得到测试集TCP预测RMSE为1.3%，表明预测准确。

- rhetorical_function_cn：提供预测模型准确性的第一层证据。

- depends_on_cn：估计和临床数据

- sets_up_cn：支持框架整体可信。

- evidence_pointer：Section 3.1.2

### 36. Section 3.1.2 第二段

- order：36

- section：Section 3.1.2

- locator：Section 3.1.2 第二段

- move_code：RESULT

- paraphrase_cn：基于Polgar等试样的外部合成患者预测TCP 95%置信区间为93.7%-94.4%，接近报道的94.1%。

- rhetorical_function_cn：提供外部验证证据。

- depends_on_cn：外部试验数据和TCP模型

- sets_up_cn：加强模型泛化主张。

- evidence_pointer：Section 3.1.2

### 37. Section 3.1.2 第三段

- order：37

- section：Section 3.1.2

- locator：Section 3.1.2 第三段

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：训练于不同剂量子样本的两个模型与全样本模型预测一致，说明外推风险较低。

- rhetorical_function_cn：检验模型外推到训练剂量范围外的可信性。

- depends_on_cn：全样本模型

- sets_up_cn：为优化中使用0-66 Gy之外的剂量提供信心。

- evidence_pointer：Section 3.1.2 + Figure 3

### 38. Section 3.2 第一段

- order：38

- section：Section 3.2

- locator：Section 3.2 第一段

- move_code：REQUIREMENT

- paraphrase_cn：在预测模型基础上，需在给定临床约束下利用预测结果优化计划。

- rhetorical_function_cn：从预测转向优化。

- depends_on_cn：预测模型

- sets_up_cn：引入优化模型。

- evidence_pointer：Section 3.2

### 39. Section 3.2 第三段

- order：39

- section：Section 3.2

- locator：Section 3.2 第三段

- move_code：REQUIREMENT

- paraphrase_cn：由于风险分层可捕获部分异质性，作者先优化患者组的平均TCP，作为统一剂量和个体剂量之间的中间步骤。

- rhetorical_function_cn：为群组最优计划提供理论理由。

- depends_on_cn：个性化医学和风险分层文献

- sets_up_cn：定义群组优化问题。

- evidence_pointer：Section 3.2 第三段

### 40. Section 3.2.1 公式(9)-(15)

- order：40

- section：Section 3.2.1

- locator：Section 3.2.1 公式(9)-(15)

- move_code：DESIGN_FEATURE

- paraphrase_cn：假设MTC对称分布以将3D模型简化为一维；定义群组平均TCP和平均剂量；优化问题为最小化平均剂量并满足TCP目标，约束场景再加66 Gy上限。

- rhetorical_function_cn：给出优化的数学形式。

- depends_on_cn：预测模型

- sets_up_cn：为Lagrange和Adam求解提供目标函数。

- evidence_pointer：Section 3.2.1

### 41. Section 3.2.1 最后两段

- order：41

- section：Section 3.2.1

- locator：Section 3.2.1 最后两段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：解法采用Lagrange乘子法和Adam优化器，因为TCP强非线性、目标随机、梯度噪声大，Adam适合此类问题。

- rhetorical_function_cn：解释为何用Adam。

- depends_on_cn：优化问题性质

- sets_up_cn：为算法对照表做铺垫。

- evidence_pointer：Section 3.2.1 + Algorithm 1

### 42. Section 3.2.2 第一段

- order：42

- section：Section 3.2.2

- locator：Section 3.2.2 第一段

- move_code：REQUIREMENT

- paraphrase_cn：个体计划的成本高、耗时且需要细粒度病理检查，但作者认为个性化问题很重要，未来数字病理工具会使其可行。

- rhetorical_function_cn：讨论个体计划的取舍和前提。

- depends_on_cn：群组优化

- sets_up_cn：为个体剂量绘画计划命名。

- evidence_pointer：Section 3.2.2

### 43. Section 4.1 第一段

- order：43

- section：Section 4.1

- locator：Section 4.1 第一段

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：评价以标准均匀计划为基线，考虑系统误差和随机误差（0、1、5 mm）调整治疗体积，定义多种计划名称。

- rhetorical_function_cn：建立评价矩阵。

- depends_on_cn：优化模型

- sets_up_cn：为Table 2-4提供标签。

- evidence_pointer：Section 4.1 + Table 2

### 44. Section 4.1.1 第一至二段

- order：44

- section：Section 4.1.1

- locator：Section 4.1.1 第一至二段

- move_code：RESULT

- paraphrase_cn：图4显示最优计划的剂量分布随误差增加向右移动；约束计划有更宽分布，TCP 90%时边缘区域剂量更高。

- rhetorical_function_cn：报告剂量分布形态结果。

- depends_on_cn：仿真计算

- sets_up_cn：解释约束导致平均剂量更高的机制。

- evidence_pointer：Figure 4

### 45. Section 4.1.1 第三段

- order：45

- section：Section 4.1.1

- locator：Section 4.1.1 第三段

- move_code：RESULT

- paraphrase_cn：群组最优计划的平均剂量比标准计划降低约90%以上；TCP目标越高或误差越大，所需剂量越高。

- rhetorical_function_cn：给出群组比较的关键数字。

- depends_on_cn：Table 3

- sets_up_cn：支持“最优化剂量适应显著改善”的结论。

- evidence_pointer：Table 3

### 46. Section 4.1.2 第一至二段

- order：46

- section：Section 4.1.2

- locator：Section 4.1.2 第一至二段

- move_code：RESULT

- paraphrase_cn：在TCP 90%下剂量绘画计划的平均剂量为1.2-3.0 Gy，相比标准计划54 Gy降低约94.4%。

- rhetorical_function_cn：报告个体计划的主要优势。

- depends_on_cn：Table 4

- sets_up_cn：为经济分析提供关键剂量差。

- evidence_pointer：Section 4.1.2 + Table 4

### 47. Section 4.1.2 第三段

- order：47

- section：Section 4.1

- locator：Section 4.1.2 第三段

- move_code：MECHANISM

- paraphrase_cn：如果病人术后残留MTC很少，标准计划的高剂量不会增加肿瘤控制而只增加正常组织毒性；如果无MTC，放疗无必要。

- rhetorical_function_cn：解释为何个性化剂量能降低平均剂量而不损控制。

- depends_on_cn：Table 3-4结果

- sets_up_cn：强化剂量适应机制的知识。

- evidence_pointer：Section 4.1.2 末尾

### 48. Section 4.2 第一段

- order：48

- section：Section 4.2

- locator：Section 4.2 第一段

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：附加评价将Adam与L-BFGS-B、SA、GA三种广泛使用的随机优化方法比较，指标包括平均剂量和计算时间。

- rhetorical_function_cn：引入第二个评价基准。

- depends_on_cn：主框架采用Adam

- sets_up_cn：为算法对照结果做铺垫。

- evidence_pointer：Section 4.2

### 49. Section 4.2 第三段

- order：49

- section：Section 4.2

- locator：Section 4.2 第三段

- move_code：RESULT

- paraphrase_cn：Adam在平均剂量和计算时间两方面一致优于三种基准方法；SA和GA慢且易局部最优；L-BFGS-B结局接近但不高效。

- rhetorical_function_cn：报告优化鲁棒性和效率证明。

- depends_on_cn：Table 5-6

- sets_up_cn：支持框架实际可用性。

- evidence_pointer：Section 4.2 + Table 5-6

### 50. Section 4.3 第一至二段

- order：50

- section：Section 4.3

- locator：Section 4.3 第一至二段

- move_code：PRACTICAL_STAKES

- paraphrase_cn：因为社会面临癌症护理成本上升，作者进一步估计低平均剂量带来的潜在成本节约。

- rhetorical_function_cn：把技术结果转成经济价值问题。

- depends_on_cn：Table 4

- sets_up_cn：引入剂量-反应系数和成本数据。

- evidence_pointer：Section 4.3

### 51. Section 4.3 第三段

- order：51

- section：Section 4.3

- locator：Section 4.3 第三段

- move_code：RESULT

- paraphrase_cn：剂量降低可减少肺/心脏剂量8.22/4.63 Gy，肺癌风险降低69.8%，心脏病风险降低34.2%；年节约约2.355亿美元。

- rhetorical_function_cn：给出经济分析结果。

- depends_on_cn：剂量差和文献风险系数

- sets_up_cn：为讨论中的成本效益贡献提供论点。

- evidence_pointer：Section 4.3

### 52. Section 5 前两段

- order：52

- section：Section 5

- locator：Section 5 前两段

- move_code：CONTRIBUTION

- paraphrase_cn：作者总结两项主要进展：一是用治疗轨迹信息驱动的放射生物模型预测个体响应；二是用Adam求解个性化计划的约束优化；并声称这是首个研究个体放疗计划设计的研究。

- rhetorical_function_cn：在讨论开头重新聚合贡献。

- depends_on_cn：第3-4节

- sets_up_cn：随后分研究贡献和实践含义。

- evidence_pointer：Section 5

### 53. Section 5.1 第一段

- order：53

- section：Section 5.1

- locator：Section 5.1 第一段

- move_code：CONTRIBUTION

- paraphrase_cn：响应Agarwal等人的HIT设计、实施和有意义使用号召；框架统一统计建模和仿真支持治疗计划优化。

- rhetorical_function_cn：将贡献连接到IS文献。

- depends_on_cn：HIT研究综述

- sets_up_cn：确立该文作为HIT设计科学研究的位置。

- evidence_pointer：Section 5.1

### 54. Section 5.1 第二段

- order：54

- section：Section 5.1

- locator：Section 5.1 第二段

- move_code：CONTRIBUTION

- paraphrase_cn：工作展示预测建模和优化在个性化医疗中的潜力，填补IS在量化分析驱动治疗策略价值方面的空白。

- rhetorical_function_cn：把贡献放在个性化医疗IS文献中。

- depends_on_cn：Section 2.2个性化医学综述

- sets_up_cn：为后续设计原则可迁移性做铺垫。

- evidence_pointer：Section 5.1

### 55. Section 5.1 第二段末尾

- order：55

- section：Section 5.1

- locator：Section 5.1 第二段末尾

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：虽然研究针对乳腺癌放疗，框架设计原则可应用于其他涉及并发症和合并症的慢性病治疗计划个性化。

- rhetorical_function_cn：将贡献从具体病种提升为一般设计知识。

- depends_on_cn：框架设计

- sets_up_cn：给未来研究留出空间。

- evidence_pointer：Section 5.1 末尾

### 56. Section 5.1 第三段

- order：56

- section：Section 5.1

- locator：Section 5.1 第三段

- move_code：CONTRIBUTION

- paraphrase_cn：本文通过临床肿瘤学知识建模平衡了预测模型的灵活性和可解释性，展示如何结合领域知识与患者数据发展临床决策支持工具。

- rhetorical_function_cn：回应对可解释性和临床工作流知识的需求。

- depends_on_cn：模型选择

- sets_up_cn：将建模选择表述为设计知识。

- evidence_pointer：Section 5.1 第三段

### 57. Section 5.2 第一段

- order：57

- section：Section 5.2

- locator：Section 5.2 第一段

- move_code：PRACTICAL_STAKES

- paraphrase_cn：基因测序、影像和数字病理等进展提高了了解疾病的机会，但临床中优化治疗仍受患者异质性和缺乏高精度生物标志物限制。

- rhetorical_function_cn：重申实际挑战，说明框架实际针对性。

- depends_on_cn：引言背景

- sets_up_cn：引出实践意义。

- evidence_pointer：Section 5.2 第一段

### 58. Section 5.2 第二段

- order：58

- section：Section 5.2

- locator：Section 5.2 第二段

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：个性化程度和经济效益依赖跨部门和跨机构的临床信息无缝共享；现实中存在严重信息摩擦。

- rhetorical_function_cn：强调框架实际落地的关键条件。

- depends_on_cn：框架假设

- sets_up_cn：为信息基础设施研究留下讨论。

- evidence_pointer：Section 5.2 第二段

### 59. Section 5.2 第三段

- order：59

- section：Section 5.2

- locator：Section 5.2 第三段

- move_code：LIMITATION

- paraphrase_cn：现有数据驱动临床模型围绕给定治疗方案和个体数据训练，不能预测未见过疗法的结局；本文基于TCP知识，可评估新计划。

- rhetorical_function_cn：通过对比数据驱动模型限制来强调本文模型优势。

- depends_on_cn：模型开发和临床预测文献

- sets_up_cn：为“框架可用于筛选临床试验”提供逻辑。

- evidence_pointer：Section 5.2 第三段

### 60. Section 5.3 第一至四段

- order：60

- section：Section 5.3

- locator：Section 5.3 第一至四段

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：局限包括放射生物过程假设简化；未考虑辅助治疗和放疗时间；平均剂量无法全面反映个体临床概况；仿真结果需临床验证。

- rhetorical_function_cn：列出限制并给出未来方向。

- depends_on_cn：全文所有内容

- sets_up_cn：结束论文。

- evidence_pointer：Section 5.3

## 写作技术

- gap_construction_cn：作者使用三层缺口叠加：一是HIT文献中治疗决策支持设计不足（区别于诊断预测）；二是放疗优化文献只解决处方剂量的递送而没解决最优剂量确定；三是个性化医学文献中缺乏结合治疗轨迹信息和仿真来定制剂量的具体框架。通过引用Agarwal et al. (2010)、Meyer et al. (2014)等文章精确标记差异和局限性，将“没有人做过”提升为“现有IS研究需要做但尚未做”。

- signposting_cn：摘要和引言开篇就用“预测模型+优化模型+仿真”概述制品；引言末尾预告第2-5节内容；第2节反复用“本文不同之处”“最接近的文献”作为路标；第3节开始先概述三步流程并配框架图；第4节点名“基线评价”“附加评价”“经济收益”等小节标题。作者在每个研究阶段前都会以一两句话说明该步骤目的和位置。

- transition_logic_cn：阶段过渡通常以“在获得可信预测模型后，下面讨论如何……”“为了展示效用……”“为了将剂量减少转成价值……”等句子实现。段落之间经常先小结上一段的结论，再引出下一问题；如在最优计划结果后，用“由表3和表4可知……”再进入机制解释。

- claim_evidence_rhythm_cn：每项大主张都先给出数学或算法定义，再报数据验证，最后在表格中放数字，并在文字中给出百分比变化。论文在引用文献数值后立即进行本地计算（如风险差和成本）。在讨论中，作者会先把第3-4节的量化和机制用两三句话总结，再分点陈述贡献。

- benchmark_narrative_cn：基准不是单一，而是层层嵌入：标准均匀计划作为临床实践基线；两种TCP目标和三种误差作为工况；优化算法比较作为第二个性能基线；已发表剂量-反应研究作为经济外推基线。作者把每个新基准都与上一结果衔接，使读者看到“性能差→算法效率→风险/成本价值”的升级。

- theory_return_cn：在讨论中，作者把设计科学和个性化医学文献重新引入，把具体剂量优化结果重新表述为“如何将领域知识嵌入预测模型”“临床工作流信息共享的重要性”“模型驱动方法可预测未见过治疗方案”等更一般的IS知识；第5.1对Agarwal et al.和Fichman et al.的引用直接回扣引言。

- contribution_positioning_cn：贡献从三方面定位：一是填补HIT治疗决策支持设计空白；二是微观粒度评估HIT影响；三是仿真作为临床试验的补充手段。每个贡献都对应引言中的一个缺口，并有对应证据段落（如技术结果对应设计贡献，经济结果对应HIT价值贡献）。

- novelty_protection_cn：作者通过强调“这是首个研究个体放疗计划设计的论文”，并将其与现有放疗优化文献的“递送优化”区分；同时声明模型驱动预测比数据驱动更适合临床小数据，强调“领域知识+机制”而不是黑箱性能；最后指出“该框架可预测未见过治疗计划”，从而避免被视为一次性仿真结果。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：建立现实背景和明确缺口：用疾病负担、经济成本、现有实践缺陷引出研究问题。

- research_job_cn：收集和综述临床实践指南、统计数据和相关文献，找出最接近的相关工作并指出其不同。

- required_evidence_cn：需要有权威统计数据或描述性证据说明问题规模，以及至少一个可对标文献缺口。

- transition_to_next_cn：“为了解决这个缺口，我们采用设计科学范式提出……”

#### 2. 2

- step：2

- writing_job_cn：构建核心制品（预测模型+优化模型），明确变量、目标函数和约束。

- research_job_cn：基于领域知识（如TCP、概率分布）建立可估计、可优化的数学模型，确定参数和求解方法。

- required_evidence_cn：需要给出可计算的模型方程式和求解算法；若使用领域知识，需引用该知识来源。

- transition_to_next_cn：“在模型构建后，我们需估计和验证参数……”

#### 3. 3

- step：3

- writing_job_cn：用真实或可追溯数据进行参数估计，并做交叉验证、外部验证和敏感性分析。

- research_job_cn：使用可获取的临床/病理数据、公开试验数据集，基于Bayesian或其他方法估计参数，并重复仿真降低偏差。

- required_evidence_cn：需要报告参数估计收敛性、预测误差（如RMSE）和外部验证或敏感性结果。

- transition_to_next_cn：“预测模型经验证后，我们可以将其用于优化……”

#### 4. 4

- step：4

- writing_job_cn：设计评价实验：定义基准、工况、指标和对比方法。

- research_job_cn：设置标准实践作为基线，定义变化条件（如误差级别、约束、目标），运行系统仿真或计算实验。

- required_evidence_cn：需要对比表格和图表：每个条件下基线vs制品的指标数值和差异百分比。

- transition_to_next_cn：“为了进一步证明效用，我们增加优化算法对照……”或“以上剂量降低可转成经济价值……”

#### 5. 5

- step：5

- writing_job_cn：增加算法基准/稳健性评价，证明制品不仅‘更好’，也在实际使用中有效。

- research_job_cn：选择主流算法作为对照，记录目标指标和资源消耗（时间/内存）。

- required_evidence_cn：需要同条件下不同算法或方法的性能对比表和结论。

- transition_to_next_cn：“最后，我们把剂量节约换算成患者风险和成本……”

#### 6. 6

- step：6

- writing_job_cn：将结果上升为更广泛的价值、机制或设计原则，并进行限制说明。

- research_job_cn：将产出与外推数据（如成本、风险系数）结合，形成实际价值评估；提炼可迁移的设计知识。

- required_evidence_cn：需要明确计算的假设、数据来源和外推方式；限制部分要指出未经临床验证的部分。

- transition_to_next_cn：结束语指向临床验证和未来改进。

### most_transferable_moves_cn

1. 以多重文献缺口叠加建立研究的必要性

2. 先用一句话预告制品结构，再分节展开

3. 在模型选择时，把数据驱动与模型驱动的利弊都交代清楚，再说明领域知识为何优先

4. 把评价拆为“性能验证—算法对照—经济价值”三个递进层次

5. 使用表格把大量工况结果集中呈现，并在正文用百分比和机制解释

6. 在讨论中把具体技术结果回接到IS文献缺口和设计原则

### resource_intensive_or_nonstandard_parts_cn

1. 需要真实临床病理数据和临床试验数据（EORTC、EBCTCG、Polgar试验），这类数据通常难以获取

2. 需要细粒度病理切片和数字病理基础设施，才能实现论文中的个体化MTC建模

3. 长期随访或临床试验验证成本极高，本文用合成患者和仿真替代，不具备可轻易复制的临床验证

4. 跨部门和跨机构的临床信息无缝整合也是现实中难以获得的条件

### what_not_to_copy_superficially_cn

1. 不能只是说‘预测+优化’而没有可验证的生物学模型和参数估计

2. 不能仅声称个体化计划更优，却缺少不同误差、约束、目标等多工况对照

3. 不能在没有剂量-反应临床文献依据的情况下把平均剂量差直接说成风险下降或成本节约

4. 不能在没有计算效率对照的情况下声称某优化算法适合临床使用

- single_best_description_of_the_routine_cn：用领域知识和临床现实定义缺口，构建可解释的预测模型与优化模型，通过真实数据和仿真完成验证与对照，再把剂量下降转化为风险、成本和可迁移设计知识。

## 分析边界

本文基于提供全文进行分析，但第3.1节和后缀引用（Online Appendix EC.1-EC.3）未给出详细内容，因此对MTC建模细节、信息流图、梯度推导等具体设计无法逐一检验。来源中表格和图像仅有部分OCR，个别图注和数字（如Table 5/6的备注）可能有限，但不影响主论证。论文声明的新颖性（“第一个研究个体放疗计划设计”）属于作者自评，未进行外部文献全面核对。
