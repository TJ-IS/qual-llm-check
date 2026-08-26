# Handling the Efficiency–Personalization Trade-Off in Service Robotics: A Machine-Learning Approach

- 作者：Schahin Tofangchi; André Hanelt; David Marz; Lutz M. Kolbe
- 年份 / 期刊：2021 / Journal of Management Information Systems
- DOI：10.1080/07421222.2021.1870391
- 源文件：25398_2021_handling-the-efficiencypersonalization-trade-off-in-service-robotics-a-machine-learning-approach.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：requirements_build_evaluate_design_principles
- 置信度：0.82

## 文章级论证概况

- 核心问题：在服务机器人特别是自动驾驶汽车情境中，如何以实时、动态的方式同时建模高能效驾驶模式和用户偏好驾驶模式，并自动推断权衡权重以持续平衡效率与个性化？

- 制品与设计：一个基于分工（division-of-labor）框架的层级1设计科学制品：中央执行者维护全局能效LSTM模型和平均用户偏好LSTM模型；每位用户对应一个专家，专家持有个人偏好LSTM，并在每个时间步从预测偏好配置出发，沿能效模型梯度方向做步进，通过锁定期、权衡参数和权衡动量动态调整效率-个性化权衡；共享经济环境中的多用户数据用于加速学习和初始化用户画像。

- 客观结果：在德国carsharing数据集（约3.5万次驾驶、1856位用户）上，在线LSTM的能效预测平均绝对误差约0.01026，约为最佳baseline（均值估计器0.03842）的1/3.5；偏好估计误差约0.01557，约为最佳baseline（随机森林0.09483）的1/6。在Mafalda第二个数据集上，能效预测误差约0.00421，偏好估计误差约0.06229，均显著低于baseline。此外，作者用数学推导提出四个命题刻画权衡模块的整体行为。

- 核心贡献：第一，向BDA价值创造研究引入效率-个性化权衡概念，并将其落实到AV/服务机器人情境；第二，贡献一个用ML实现的、能够同时支持能效驾驶策略、个性化驾驶设置并实时动态平衡二者权衡的设计制品，从而弥补IS AV研究中缺乏面向实际驾驶策略的设计制品这一缺口。

- 整篇论证链：本文从BDA价值创造文献中识别出效率和个性化常被割裂或加性处理，进而在服务机器人特别是AV情境中指出二者存在动态权衡；由于现有IS设计研究既缺少能同时考虑两者的驾驶策略制品，也缺少自动推断权衡权重的方法，作者以DoL框架设计了一个三模型ML系统：中央执行者维护全局能效LSTM和平均用户偏好LSTM，专家维护个体偏好LSTM并采用从期望偏好出发向效率最优方向做梯度步进的实时决策，同时用用户手动锁定作为反馈动态调整权衡参数；在carsharing和Mafalda两个数据集上，效率LSTM和偏好LSTM的误差显著低于多种baseline；由于无法在真实自主环境中测试，作者用数学推导提出关于权衡模块收敛和边界行为的四个命题，并以补充实证显示顾客愿意为个性化驾驶支付更高价格，最终将贡献定位为向BDA价值创造引入权衡概念、提供AV驾驶策略设计制品并将研究场景扩展到日常生活服务机器人。

## 类型与写作弧线判定

- 论文主类型判定：文章明确将自己定位为设计科学研究，开发层级1的落地制品；研究路径是先通过文献界定问题与需求，再构建基于DoF/LSTM的ML应用，随后用真实数据集和baseline进行评价，最后通过数学命题和实践含义提炼可复用设计知识，符合设计科学‘构建-评价-设计知识’的范式。

- 主导写作弧线判定：文章没有以正式假设检验为主线，而是从IS BDA价值创造和AV文献中导出设计需求，构建DoL ML制品，用两个数据集和多个baseline评价其子模块，再以分析性命题和讨论提炼设计原则，符合‘要求—构建—评价—设计原则’的写作弧线。

## 研究开展程序

- study_or_phase_count：7

- 研究阶段总序列：研究分为七个阶段：前两个阶段是问题界定与需求推演以及制品架构设计；第三阶段是数据准备与实例化；第四、五阶段分别评价能效预测模块和偏好估计模块；第六阶段用数学分析刻画整体权衡模块行为；第七阶段借助在线补充附录加入顾客价值、模型适应性和更多属性的附加证据。各阶段从‘为什么需要’推进到‘如何设计’，再推进到‘模块是否准确’，最后推进到‘整体行为边界如何’和‘实践价值如何’。

### studies_or_phases

#### 1. 问题界定与需求推演（Background + Research Setting）

- order：1

- name_cn：问题界定与需求推演（Background + Research Setting）

- question_cn：为什么效率-个性化权衡在BDA价值创造和AV情境中重要，且现有IS研究缺乏相应设计制品？

- inputs_and_setting_cn：IS BDA价值创造文献、AV IS研究、运筹学权衡处理文献、服务机器人文献

- designed_or_compared_object_cn：将效率和个性化从隔离/加性视角重构为动态权衡；导出对能效模型、偏好模型和权衡机制的三类需求

- baseline_control_or_counterfactual_cn：现有IS文献将效率和个性化隔离或加性处理；运筹学权衡方法依赖决策者人工设定权重、适合长期静态规划

##### objective_metrics

（空）

- analysis_method_cn：概念论证、文献综合、gap分析

- main_result_cn：确立核心缺口：IS AV研究中缺少同时服务能效、偏好并支持动态权衡的驾驶策略设计制品；BDA价值创造研究需要纳入权衡观。

- argumentative_role_cn：为整个制品提供问题合法性和设计要求，使后续设计不是单纯技术性能改进而是回应理论和管理缺口。

- remaining_uncertainty_cn：这种动态权衡能否被ML制品实现尚未验证。

- link_to_next_phase_cn：缺口催生Research Setting中的设计需求和DoL制品架构。

##### evidence_pointers

1. Introduction全段

2. Background中BDA价值创造、贸易文献、AV IS研究三个小节

3. Figure 1

#### 2. DoL制品架构设计（Design/DoL Application）

- order：2

- name_cn：DoL制品架构设计（Design/DoL Application）

- question_cn：如何设计一个实时、分布式、模块化的ML应用来同时学习能效、偏好并进行权衡决策？

- inputs_and_setting_cn：DoL框架、LSTM网络、传感器数据流（环境变量和可配置变量）、用户手动锁定信号

- designed_or_compared_object_cn：中央执行者维护全局能效LSTM和平均用户偏好LSTM；专家维护个体偏好LSTM；权衡模块用梯度步进、锁定期、权衡参数和权衡动量更新公式（1）—（3）

- baseline_control_or_counterfactual_cn：与单模型ML应用、静态偏好学习方法（如Kuderer等）对比；与依赖人工指定权重的多目标优化方法对比

##### objective_metrics

（空）

- analysis_method_cn：架构设计与数学形式化

- main_result_cn：形成三模型组合的实时学习应用，支持用户通过手动调整提供反馈，并利用共享经济数据初始化用户画像。

- argumentative_role_cn：将需求推演转化为可实现的制品结构，是后续实例化和评价的直接对象。

- remaining_uncertainty_cn：各模型的实际预测精度、权衡模块在真实数据上的行为尚未验证。

- link_to_next_phase_cn：需要在实际数据上实例化超参数并评估各子模块。

##### evidence_pointers

1. Design/Division-of-Labor Application小节约全部内容

2. Figure 3

3. 公式(1)-(3)

#### 3. 数据准备与制品实例化

- order：3

- name_cn：数据准备与制品实例化

- question_cn：如何在真实carsharing数据和Mafalda数据集上设置LSTM超参数和权衡参数？

- inputs_and_setting_cn：德国carsharing提供商数据集（97车、1856用户、34987次驾驶、5400万个传感器数据点）；Mafalda数据集（37次驾驶、7辆个人车辆）

- designed_or_compared_object_cn：LSTM隐藏层数、隐藏层大小、激活函数、遗忘门偏置、学习率；权衡参数初始值gamma=0.01、动量=0.01、动量衰减=0.99、锁定时间=60

- baseline_control_or_counterfactual_cn：非联合优化；每次只优化一个超参数，在30%用户子集上重复5次取最低平均绝对误差

##### objective_metrics

1. 平均绝对误差

- analysis_method_cn：启发式单参数网格调优

- main_result_cn：能效预测最优为单层LSTM、3个神经元；偏好估计最优为两层LSTM、约6300个神经元；权衡参数完成初始化。

- argumentative_role_cn：确保制品从抽象架构成为一个可复现、可评价的具体实例。

- remaining_uncertainty_cn：调参只在主数据集上进行，Mafalda数据集上的表现仍需验证。

- link_to_next_phase_cn：有了实例化模型即可分别评价能效预测和偏好估计。

##### evidence_pointers

1. Evaluation/Artifact Instantiation小节

2. Table 2

3. Figures 4-5

#### 4. 能效预测模块评价

- order：4

- name_cn：能效预测模块评价

- question_cn：在线LSTM能效预测模型是否显著优于常见baseline？

- inputs_and_setting_cn：carsharing数据集和Mafalda数据集

- designed_or_compared_object_cn：在线LSTM vs 随机猜测器、均值估计器、线性回归、决策树、随机森林、前馈神经网络

- baseline_control_or_counterfactual_cn：上述六类常见回归baseline

##### objective_metrics

1. 能效预测的平均绝对误差

- analysis_method_cn：离线比较预测误差；讨论低方差和相关性对baseline的影响

- main_result_cn：carsharing上LSTM误差0.01026，约为baseline均值的1/3.5；Mafalda上误差0.00421，约为baseline的1/40。

- argumentative_role_cn：证明能效模型具备高质量预测能力，为权衡模块提供可靠基础。

- remaining_uncertainty_cn：仅评价子模块，未测试整个应用在自主驾驶中的行为。

- link_to_next_phase_cn：下一个阶段评价偏好估计模块，两者共同构成权衡模块的输入。

##### evidence_pointers

1. Evaluation of the Efficiency Prediction小节

2. Tables 3-4

#### 5. 偏好估计模块评价

- order：5

- name_cn：偏好估计模块评价

- question_cn：基于LSTM的用户偏好估计是否优于多种baseline，包括密度估计方法？

- inputs_and_setting_cn：carsharing数据集和Mafalda数据集；假设用户手动选择的配置反映真实偏好

- designed_or_compared_object_cn：两层在线LSTM vs 线性回归、决策树、随机森林、前馈NN、高斯分布、KDE（Cauchy核和Gaussian核）

- baseline_control_or_counterfactual_cn：在能效baseline基础上增加密度估计baseline

##### objective_metrics

1. 可配置参数预测的平均绝对误差

- analysis_method_cn：离线比较；按配置参数平均绝对偏差计算误差

- main_result_cn：carsharing上LSTM误差0.01557，约为最佳baseline随机森林0.09483的1/6；Mafalda上误差0.06229，约为最佳baseline的1/2；KDE方法因多局部极大值而表现差。

- argumentative_role_cn：证明偏好模型能有效建模时变、情境敏感的用户偏好，弥补静态偏好学习方法的不足。

- remaining_uncertainty_cn：偏好估计复杂度高，未在完整自主系统中验证；真实用户反馈机制仅间接用锁定信号代理。

- link_to_next_phase_cn：单个模型准确之后，需要刻画两者组合后的整体权衡行为。

##### evidence_pointers

1. Evaluation of the Preference Estimation小节

2. Tables 5-6

#### 6. 整体行为数学分析与命题推导

- order：6

- name_cn：整体行为数学分析与命题推导

- question_cn：既然无法在真实自主环境中测试整体系统，权衡模块的动态行为在理论上如何刻画？

- inputs_and_setting_cn：权衡模块的数学公式（1）—（3），假设能效和偏好模型完美预测，考虑用户不干预、持续干预、偶尔干预、早期完全锁定等情形

- designed_or_compared_object_cn：抽象后的权衡模块；推导Proposition 1a、1b、2、3、4

- baseline_control_or_counterfactual_cn：极端用户行为：完全不干预 vs 总是干预；早期锁定后不干预

##### objective_metrics

（空）

- analysis_method_cn：基于公式的极限与收敛分析

- main_result_cn：完全不干预时系统收敛到能效局部最优；总干预时系统完全偏向用户偏好；权衡动量收敛到零时模块稳定；偶尔干预时最终权衡参数由初始值、动量、锁定比例和系统常数决定。

- argumentative_role_cn：在没有现场实验的情况下，为整体制品提供行为边界和理论保证，使贡献不局限于子模块性能。

- remaining_uncertainty_cn：命题基于完美预测假设，未纳入预测误差对权衡行为的影响，也没有真实用户信任/满意度数据。

- link_to_next_phase_cn：引出实践含义、边界条件和未来研究。

##### evidence_pointers

1. Discussion/Analysis of the Application’s Overall Behavior小节

2. Proposition 1a-4

3. 公式(4)-(5)

#### 7. 附加实证与适用性分析（在线补充附录）

- order：7

- name_cn：附加实证与适用性分析（在线补充附录）

- question_cn：潜在AV共享出行顾客是否重视个性化驾驶并愿意支付更高价格？模型随时间适应性和更多配置属性表现如何？

- inputs_and_setting_cn：在线补充附录A（顾客调查/选择实验）、附录D（适应性分析）、附录E（更多配置属性）；具体数据未在主文中出现

- designed_or_compared_object_cn：采用本研究个性化驾驶方案的AV服务 vs 未个性化的baseline方案；模型在不同抽象层上的适应性

- baseline_control_or_counterfactual_cn：不采用个性化方案的服务报价

##### objective_metrics

1. 顾客选择偏好

2. 支付意愿

3. 随时间的预测误差下降

- analysis_method_cn：由在线补充附录报告，主文仅转述结论

- main_result_cn：潜在AV共享出行顾客会选择并重视个性化驾驶，且对使用该方法的服务有更高支付意愿；模型能在不同层级随时间改善。

- argumentative_role_cn：将技术性能证据提升到顾客价值层面，回应AV接受度与商业可行性。

- remaining_uncertainty_cn：主文无法验证附录具体设计；不是现场部署实验，不能证明真实AV环境中的信任与接受。

- link_to_next_phase_cn：支撑讨论部分对AV开发者和共享出行商业模式的启示。

##### evidence_pointers

1. Abstract中关于Online Supplemental Appendix A的说明

2. Discussion部分引用Online Supplemental Appendices A、D、E

## 各部分修辞架构

### abstract_moves

1. CONTEXT: BDA价值创造机制在服务机器人中产生效率-个性化权衡

2. PHENOMENON: AV中个人偏好可能与效率相悖

3. GAP: 现有IS研究缺少同时处理效率、个性化和动态权衡的制品

4. DESIGN_FEATURE: 提出一个基于35,000次驾驶数据的ML方法，包含三个模型和共享经济扩展

5. RESULT: 提出制品并报告精度优势、补充实证和一般化命题

6. CONTRIBUTION: 向IS BDA价值创造引入权衡概念和AV设计制品

### introduction_moves

1. CONTEXT: BDA从企业内部走向客户面对面的服务

2. PRACTICAL_STAKES: AV领域竞争激烈，效率与个性化都影响盈利和接受

3. PHENOMENON: 服务机器人和AV成为日常生活情境中权衡的典型案例

4. PRIOR_KNOWLEDGE: IS研究分别展示了BDA的效率收益和个性化收益

5. LIMITATION: 这些机制被隔离或加性处理，忽视冲突

6. GAP: IS AV研究缺乏支持能效、偏好及动态权衡的驾驶策略设计制品

7. WHY_GAP_MATTERS: 因BDA价值创造和人的因素均关键，该问题对IS至关重要

8. RQ_OR_OBJECTIVE: 提出如何动态建模并自动推断权衡权重的研究问题

9. STUDY_OVERVIEW: 说明将开发层级1 DSR制品

10. CONTRIBUTION: 预告双重贡献和主要评价结果

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE: BDA价值创造研究的两个核心机制是效率和个性化

2. LIMITATION: 当前IS研究或单向看待或加性看待价值机制

3. THEORY_INTRO: 服务营销中的效率-个性化权衡以及组织悖论研究提供了权衡知识

4. MECHANISM: 服务机器人中系统级效率与个体级偏好天然冲突

5. GAP: 动态情境下人工设定权衡权重不可行，需要新方法

6. PRIOR_KNOWLEDGE: AV IS研究强调能效、接受度和ML潜力

7. LIMITATION: 三项要素在IS AV文献中彼此割裂

8. GAP: 相邻领域ML研究存在静态偏好、孤立模块、人工权重等局限

### artifact_design_moves

1. REQUIREMENT: 需要能效模型、偏好模型和权衡决策方法

2. METHOD_JUSTIFICATION: 采用human-centered design和DoL框架处理实时分布式学习

3. DESIGN_FEATURE: CE维护全局效率模型和平均偏好模型

4. DESIGN_FEATURE: Expert维护个体偏好模型并在每个时间步做梯度步进

5. MECHANISM: 用户手动锁定作为实时反馈，权衡参数和动量动态调整

6. DESIGN_FEATURE: 使用LSTM建模时间序列依赖

### evaluation_moves

1. METHOD_JUSTIFICATION: 因无法在真实车流中测试AV控制，评估分为独立模块评估和数学整体分析

2. BENCHMARK_OR_CONTRAST: 能效预测与6种baseline比较

3. BENCHMARK_OR_CONTRAST: 偏好估计增加密度估计baseline

4. RESULT: LSTM在两个数据集上均大幅优于baseline

5. ROBUSTNESS_OR_BOUNDARY_TEST: 用Mafalda数据集验证一般化

6. HYPOTHESIS_OR_PROPOSITION: 用数学命题刻画整体权衡行为

7. RESULT: 补充实证显示顾客愿意为个性化支付更高价格

### discussion_and_contribution_moves

1. RESULT: 子模块准确性和两数据集验证支持制品有效性

2. BOUNDARY_CONDITION: 权衡模块的行为在完美预测假设下由用户干预模式决定

3. CONTRIBUTION: 向BDA价值创造研究引入权衡概念和日常生活情境

4. CONTRIBUTION: 提出以人为中心、中间自动化水平的IS设计观

5. DESIGN_KNOWLEDGE: 对AV开发者、共享车队运营者提出技术和管理要求

6. LIMITATION_AND_FUTURE: 指出未在真实AV中测试、属性数量有限、未来可探索其他ML模型和更多情境

7. THEORY_RETURN: 将结果重新连接到BDA价值创造和矛盾/悖论理论

## 理论/知识到设计的翻译

### 知识/理论基础

1. BDA价值创造框架（Grover et al. 2018）

2. 服务营销中的效率-个性化权衡（Xu et al. 2014; Solomon et al. 1985）

3. IS悖论/矛盾理论（Gregory et al. 2015; Robey & Boudreau 1999）

4. DoL分布式认知专家系统框架（Tofangchi et al. 2017）

5. human-centered design（Gasson 2003）

6. LSTM/循环神经网络理论（Hochreiter & Schmidhuber 1997）

7. AV接受度研究（Bornholt & Heidt 2019; Ernst & Reinelt 2017）

8. 共享经济与共享出行商业模式（Weber 2014; Kornhauser et al. 2013）

9. 运筹学中的多目标权衡与人工权重限制（Kaliszewski 2000; White et al. 1984）

- 理论—设计耦合：partial

- 耦合判定理由：知识基础决定了问题结构、系统需求和总体模块化架构，但核心ML技术选择（LSTM、梯度步进、锁定期/动量机制）主要来自实时数据分析和工程启发；理论没有严格推导出具体算法，更多是事后解释和定位贡献，因此属于部分耦合。

- 理论到设计翻译链：BDA价值创造机制之间可能出现冲突 → 效率-个性化权衡需要被显式处理 → 系统需要同时具备能效模型、偏好模型和权衡机制 → 采用DoL框架将系统拆成CE和Expert → CE维护全局能效LSTM和平均用户偏好LSTM，Expert维护个体偏好LSTM → 决策时从预测偏好出发，沿能效梯度做步进 → 用户手动锁定作为反馈调节权衡参数和动量 → 共享经济数据用于初始化用户模型和加速学习 → 通过两个数据集评价子模块，并用数学命题刻画整体权衡行为。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：BDA价值创造中的效率和个性化机制不能总被加性处理，复杂情境下会产生权衡。

- mechanism_cn：系统级效率目标与个体级偏好目标可能冲突；忽略冲突会造成顾客不满意或效率损失。

- design_requirement_cn：需要同时优化效率和个性化，并显式处理二者权衡。

- artifact_choice_cn：设计一个三模型ML应用：能效LSTM、偏好LSTM、权衡模块。

- evaluated_contrast_cn：两个子模块分别与6-9种baseline比较；整体行为用数学命题而非现场实验检验。

- objective_result_cn：能效和偏好LSTM误差均大幅低于baseline；数学命题给出权衡模块行为边界。

##### evidence_pointers

1. Background BDA value creation部分

2. Design部分

3. Tables 3-6

4. Propositions 1-4

#### 2. 2

- theory_or_knowledge_claim_cn：运筹学多目标权衡通常需要人工指定权重，不适合动态、与个体互动紧密的实时情境。

- mechanism_cn：驾驶过程中的用户偏好随时间变化，单个决策者无法预先确定客观的权衡权重。

- design_requirement_cn：权衡权重必须从实时数据和用户反馈中自动推断。

- artifact_choice_cn：用用户手动锁定作为反馈，设计权衡参数gamma和权衡动量m，按公式(2)(3)实时更新。

- evaluated_contrast_cn：与依赖人工指定权重的多目标方法对比；通过Proposition 2-4分析收敛性。

- objective_result_cn：重力参数在有/无用户干预时分别偏向往返效率和偏好；动量收敛后系统稳定。

##### evidence_pointers

1. Background中的operations research tradeoff部分

2. Expert部分公式(1)-(3)

3. Proposition 2-4

#### 3. 3

- theory_or_knowledge_claim_cn：DoL框架通过任务分解和专家/中央执行者结构提高实时ML应用的可扩展性和有效性。

- mechanism_cn：将整体学习任务分解为系统级能效学习、个体级偏好学习和权衡决策三个低复杂度子任务。

- design_requirement_cn：系统应模块化、可实时更新并能利用分布式数据源。

- artifact_choice_cn：CE维护全局模型，每位用户由一个Expert维护；新用户用平均偏好模型初始化。

- evaluated_contrast_cn：与单模型ML应用和静态偏好学习方法对比。

- objective_result_cn：模块化LSTM在真实carsharing和Mafalda数据上均优于baseline；共享环境加速学习。

##### evidence_pointers

1. Research Setting部分

2. Central Executive/Expert部分

3. Evaluation结果

#### 4. 4

- theory_or_knowledge_claim_cn：AV接受度研究强调用户个性化驾驶体验的重要性。

- mechanism_cn：用户对驾驶体验的感知会影响其对AV的接受；忽视偏好会导致拒绝使用。

- design_requirement_cn：需要在尊重用户个性化偏好的同时不牺牲系统级能效。

- artifact_choice_cn：专家模型以用户偏好为起点，并在用户锁定时完全遵循用户设置，从而赋予用户干预权。

- evaluated_contrast_cn：偏好估计模块与baseline比较；补充实证调查顾客对个性化驾驶的支付意愿。

- objective_result_cn：偏好LSTM误差显著低于baseline；顾客愿意为个性化方案支付更高价格。

##### evidence_pointers

1. Introduction AV acceptance部分

2. Design Expert部分

3. Evaluation of Preference Estimation

4. Online Supplemental Appendix A

#### 5. 5

- theory_or_knowledge_claim_cn：用户偏好受时间序列和近期事件影响，静态偏好学习方法不足以应对动态情境。

- mechanism_cn：偏好不是固定值，而是随环境序列和最近经历变化。

- design_requirement_cn：偏好模型需要处理时间序列并实时更新。

- artifact_choice_cn：使用LSTM而非静态模型；设置两层隐藏层和大量神经元以捕捉偏好复杂性。

- evaluated_contrast_cn：与线性回归、树模型、前馈NN和密度估计法等非时序baseline比较。

- objective_result_cn：LSTM在偏好估计上显著优于baseline，Mafalda数据集上也优于全部baseline。

##### evidence_pointers

1. Background adjacent fields部分

2. Design部分

3. Evaluation of Preference Estimation

## 评价逻辑

### evaluation_modes

1. 离线预测性能评价：能效LSTM和偏好LSTM分别与多种baseline比较

2. 跨数据集验证：用carsharing主数据集调参，用Mafalda第二个数据集检验一般化

3. 数学分析：在完美预测假设下推导整体权衡模块的行为命题

4. 补证实证：通过在线补充附录A提供顾客对个性化驾驶的支付意愿证据

5. 适应性分析：在线补充附录D中评价模型随时间下降的不期望行为

- why_these_evaluations_cn：由于自动驾驶控制器难以在真实车流中测试，作者将评价拆解为可离线验证的部分：先用真实历史驾驶数据检验两个预测模块是否准确，再用第二个数据集检验可迁移性；由于整体权衡行为无法直接现场测试，作者改用数学公式推导命题以提供理论保证；最后用补充调查将技术准确性与顾客商业价值关联起来。

- benchmark_and_contrast_chain_cn：评价从两个独立维度展开：能效预测先与随机猜测、均值、线性回归、决策树、随机森林、前馈NN比较；偏好估计再增加高斯分布和KDE密度方法；两个维度都在主数据集上建立优势，再在Mafalda数据集上重复验证；最后通过极端用户干预场景和收敛分析将benchmark结果上升为整体权衡模块的行为命题。

### claim_evidence_ledger

#### 1. LSTM能效预测模型显著优于baseline

- claim_cn：LSTM能效预测模型显著优于baseline

- evidence_cn：Table 3/4中在线LSTM误差远低于所有baseline

- strength_cn：强，但仅限于离线日志数据，没有真实自主驾驶环境

#### 2. LSTM偏好估计模型显著优于baseline

- claim_cn：LSTM偏好估计模型显著优于baseline

- evidence_cn：Table 5/6中在线LSTM误差远低于所有baseline

- strength_cn：强，但依赖于用户手动配置等于真实偏好的假设

#### 3. 所设计的权衡模块能够在效率和个性化之间动态平衡

- claim_cn：所设计的权衡模块能够在效率和个性化之间动态平衡

- evidence_cn：公式(1)-(3)和Proposition 1-4的数学推导

- strength_cn：中，基于完美预测假设，未在真实整体系统中实证

#### 4. 该设计方法可以推广到其他数据集/其他服务机器人情境

- claim_cn：该设计方法可以推广到其他数据集/其他服务机器人情境

- evidence_cn：Mafalda数据集上的表现和低规格化数据预处理

- strength_cn：中，只验证了一个额外数据集，其他情境是推论

#### 5. 顾客愿意为采用该方法的个性化AV服务支付更高价格

- claim_cn：顾客愿意为采用该方法的个性化AV服务支付更高价格

- evidence_cn：Online Supplemental Appendix A

- strength_cn：弱至中，因主文未提供具体设计细节和统计结果

- internal_validity_strategy_cn：使用真实carsharing历史数据作为标签来源；在30%用户子集上重复5次调参；控制超参数搜索空间以近似最优配置；比较训练/未见数据误差差小于3%从而不用正则化；采用多个baseline和第二个数据集进行稳健性验证。

- external_validity_strategy_cn：使用Mafalda第二个数据集验证跨数据集表现；强调一般化数据预处理和少量规格化设置；用数学命题刻画不同用户干预模式下的行为；用补充顾客调查将结果与真实使用意愿连接。

- what_is_not_actually_tested_cn：整体DoL应用没有在真实AV或真实交通环境中运行；权衡模块的行为只在完美预测假设下以命题形式分析；用户信任、满意度、长期接受度没有直接测量；真实用户手动锁定如何影响偏好模型的效果仅从算法设计上推断；在线补充附录中的顾客调查、适应性分析和更多属性分析未在主文中详述，无法独立验证。

## 贡献闭环

- technical_claim_cn：在所用离线数据集上，LSTM能效预测和偏好估计的平均绝对误差显著低于随机猜测、均值、线性回归、决策树、随机森林、前馈NN以及密度估计等baseline，能效约3.5倍（主数据集）、偏好约6倍（主数据集）优于最佳baseline。

- artifact_claim_cn：基于DoL架构的ML制品能够同时学习能效驾驶策略和用户偏好，并通过梯度步进、锁定期和自适应权衡参数实时给出介于偏好与效率之间的车辆配置。

- mechanism_claim_cn：用户手动调整配置被解释为反馈并触发锁定；锁定比例驱动权衡参数变化：用户很少干预时系统向能效偏移，经常干预时系统向偏好偏移；权衡动量逐渐衰减使系统收敛并避免振荡。

- boundary_claim_cn：该设计适用于具备连通性、一定计算存储容量、并能提供用户反馈或手动驾驶选项的AV/共享车队；在离线logged data上有效，可迁移到其他类似时序决策情境；真实自主环境中的整体行为尚未现场验证。

- reusable_design_knowledge_cn：（1）将BDA权衡问题分解为系统级模型、个体级模型和权衡模块三个子问题；（2）用平均用户模型初始化新用户模型，借助共享经济数据加速学习；（3）以用户手动干预作为实时反馈信号，而不是要求用户显式提供偏好标签；（4）用可衰减的权衡动量实现学习初期快速适应和后期的稳定收敛。

- theoretical_contribution_cn：向IS BDA价值创造研究引入效率-个性化权衡概念，指出价值创造机制可能存在冲突而非常规加性；将BDA价值创造从组织内部扩展到日常生活与个体深度参与的自动化情境，并强调需要结合矛盾/悖论理论、以人为中心的视角来设计BDA应用。

- how_discussion_closes_intro_gap_cn：讨论段落重新回到引言识别的两个缺口：IS BDA文献将效率和个性化隔离或加性处理、IS AV文献缺少面向驾驶策略的设计制品；通过展示LSTM子模块精度、数学行为命题以及补充顾客价值证据，论证了所提出制品确实填补缺口，并将结论推广到服务机器人和其他数据驱动决策情境。

- overclaim_or_unsupported_leaps_cn：从子模块精度跳跃到‘整体系统在真实时间内处理权衡’依赖完美预测假设下的数学推导，缺少整机实验；顾客支付意愿证据只在在线补充附录中，主文无法核验；‘可一般化到其他服务机器人情境’主要基于一个额外数据集和概念论证；‘动态平衡’的实际用户体验和信任未被直接测量。

## 句级写作动作图谱

### 1. P1 S1

- order：1

- section：Introduction

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：BDA不再局限于企业内部流程优化，而越来越多地嵌入面向客户的服务中。

- rhetorical_function_cn：开头将BDA价值创造场景从组织内部转向日常生活，为后续用户体验和权衡问题铺垫。

- depends_on_cn：无

- sets_up_cn：引出客户面对面的BDA应用作为研究对象。

- evidence_pointer：Introduction第1段第1句

### 2. P1 S2-S3

- order：2

- section：Introduction

- locator：P1 S2-S3

- move_code：CONTEXT

- paraphrase_cn：诸如通用、谷歌、优步、特斯拉等企业正在竞争提供AV服务，BDA承诺带来车队级效率收益。

- rhetorical_function_cn：以经典案例建立ALV在BDA价值创造中的现实重要性。

- depends_on_cn：上一句将BDA嵌入客户服务。

- sets_up_cn：说明效率收益是竞争压力的核心目标之一。

- evidence_pointer：Introduction第1段第2-3句

### 3. P1 S4-S5

- order：3

- section：Introduction

- locator：P1 S4-S5

- move_code：PHENOMENON

- paraphrase_cn：满足个人偏好会使顾客接受和重视AV，但这可能与整体效率相悖，形成威胁盈利的张力。

- rhetorical_function_cn：首次提出效率-个性化冲突是现实问题。

- depends_on_cn：上面建立的效率收益和顾客接受两个目标。

- sets_up_cn：全文核心现象：效率-个性化权衡。

- evidence_pointer：Introduction第1段第4-5句

### 4. P2 S1-S3

- order：4

- section：Introduction

- locator：P2 S1-S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：IS研究已经展示了BDA价值创造的多种机制，例如通过优化提高效率、通过推荐系统个性化服务。

- rhetorical_function_cn：概括已有知识，承认BDA价值创造的重要性。

- depends_on_cn：现象提出后需要学术文献支撑。

- sets_up_cn：为随后指出现有研究的缺口提供对照。

- evidence_pointer：Introduction第2段第1-3句

### 5. P2 S4-S5

- order：5

- section：Introduction

- locator：P2 S4-S5

- move_code：LIMITATION

- paraphrase_cn：现有IS研究要么孤立研究单一价值机制，要么把机制当作可加总，忽略潜在冲突；随着BDA复杂性增加，这些假设不再充分。

- rhetorical_function_cn：指出现有BDA价值创造研究的核心局限。

- depends_on_cn：上一句列举的效率与个性化机制。

- sets_up_cn：为‘需要权衡观’提供理论依据。

- evidence_pointer：Introduction第2段第4-5句

### 6. P3 S1-S3

- order：6

- section：Introduction

- locator：P3 S1-S3

- move_code：PHENOMENON

- paraphrase_cn：服务机器人（定义为高自动化程度、以物理形态提供定制服务的IT）是BDA价值创造权衡凸显的具体情境；追求系统级效率时可能与个人偏好冲突。

- rhetorical_function_cn：将抽象的BDA权衡落实到服务机器人场景。

- depends_on_cn：前面指出的IS文献局限。

- sets_up_cn：为AV作为服务机器人案例铺路。

- evidence_pointer：Introduction第3段

### 7. P4 S1-S3

- order：7

- section：Introduction

- locator：P4 S1-S3

- move_code：PHENOMENON

- paraphrase_cn：AV是特别相关的服务机器人案例，未来可持续出行愿景依赖互联、协调、共享的自动驾驶电动车；车辆数据和数字基础设施使高效驾驶模式可以持续推导和应用，共享经济进一步放大潜力。

- rhetorical_function_cn：聚焦到具体研究情境AV，并解释为什么该情境适合研究效率。

- depends_on_cn：服务机器人总体背景。

- sets_up_cn：为下文同时讨论效率和个性化做背景。

- evidence_pointer：Introduction第4段第1-3句

### 8. P4 S4-S5

- order：8

- section：Introduction

- locator：P4 S4-S5

- move_code：PRACTICAL_STAKES

- paraphrase_cn：运营商视角下顾客吸引力与效率同样重要；研究显示满足个人偏好、提供愉悦乘坐体验对AV接受至关重要。

- rhetorical_function_cn：强调个性化并不是可选项，而是影响AV商业成败的实践后果。

- depends_on_cn：AV效率潜力背景。

- sets_up_cn：为效率和个性化冲突的重要性提供依据。

- evidence_pointer：Introduction第4段第4-5句

### 9. P4 S6-S7

- order：9

- section：Introduction

- locator：P4 S6-S7

- move_code：GAP

- paraphrase_cn：现有IS研究虽强调效率和偏好，但缺少基于BDA/ML的、能同时适应两个目标的驾驶策略制品；已有的AV权衡研究也没有提供平衡效率-个性化权衡的设计制品。

- rhetorical_function_cn：明确文献缺口：既缺设计制品，也缺针对该特定权衡的平衡方案。

- depends_on_cn：前面关于效率和偏好重要性的综述。

- sets_up_cn：直接引出本文研究问题。

- evidence_pointer：Introduction第4段第6-7句

### 10. P5 S1

- order：10

- section：Introduction

- locator：P5 S1

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：因为问题关系到BDA价值创造，并且数据驱动自动化中必须同时考虑技术和人的因素及其动态权衡，该问题对IS研究特别重要。

- rhetorical_function_cn：解释缺口为什么值得IS研究，而非单纯技术问题。

- depends_on_cn：前面的GAP。

- sets_up_cn：为研究问题的提出提供正当性。

- evidence_pointer：Introduction第5段第1句

### 11. P5 S2

- order：11

- section：Introduction

- locator：P5 S2

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：提出研究问题：如何在AV中预设和动态建模高效且用户偏好的驾驶模式，并如何自动推断权衡权重以持续平衡二者？

- rhetorical_function_cn：将gap转化为可研究的问题，是全文的核心目标句。

- depends_on_cn：整个前五段的知识积累。

- sets_up_cn：决定后续制品设计和评价方向。

- evidence_pointer：Introduction第5段第2句

### 12. P6 S1-S2

- order：12

- section：Introduction

- locator：P6 S1-S2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：作者说明将开发一个层级1设计科学制品，并定义车辆配置和驾驶模式两个基本概念。

- rhetorical_function_cn：预告研究类型和核心概念。

- depends_on_cn：研究问题。

- sets_up_cn：为后续制品描述提供术语基础。

- evidence_pointer：Introduction第6段

### 13. P7 S1-S3

- order：13

- section：Introduction

- locator：P7 S1-S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：制品由能效LSTM、偏好LSTM和权衡权重推断方法组成，并扩展使用共享经济数据加速学习、用平均用户画像初始化个体画像。

- rhetorical_function_cn：高度概括制品核心设计，让读者在导览阶段就了解解决方案。

- depends_on_cn：研究问题和概念定义。

- sets_up_cn：为正文DoL设计部分做预告。

- evidence_pointer：Introduction第7段

### 14. P8 S1-S2

- order：14

- section：Introduction

- locator：P8 S1-S2

- move_code：CONTRIBUTION

- paraphrase_cn：作者声称贡献有二：一是将效率-个性化权衡概念引入BDA价值创造和AV服务情境；二是提供一个ML设计制品解决该权衡。

- rhetorical_function_cn：在引言末尾声明贡献，建立全文价值主张。

- depends_on_cn：前面GAP和研究问题。

- sets_up_cn：为讨论部分回收贡献提供锚点。

- evidence_pointer：Introduction第8段第1-2句

### 15. P8 S3-S6

- order：15

- section：Introduction

- locator：P8 S3-S6

- move_code：RESULT

- paraphrase_cn：评价显示LSTM收敛迅速，能效预测精度约为baseline的3.5倍，偏好估计约为6倍；补充实证显示顾客会选择个性化驾驶并愿意为使用该方法的服务支付更高价格；还研究了一般化设计命题。

- rhetorical_function_cn：在导言中预告关键证据，吸引读者并展示贡献有支撑。

- depends_on_cn：制品描述。

- sets_up_cn：为Evaluation和Discussion部分做先行总结。

- evidence_pointer：Introduction第8段第3-6句

### 16. Background/BDA Value Creation P1-P2

- order：16

- section：Background

- locator：Background/BDA Value Creation P1-P2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：BDA被定义为对大数据应用统计、处理和分析技术；学者强调只有产生组织价值才算成功。

- rhetorical_function_cn：建立BDA价值创造研究的理论基础和评判标准。

- depends_on_cn：引言中的BDA价值主张。

- sets_up_cn：为后文评估BDA价值机制是否完备做铺垫。

- evidence_pointer：Background BDA value creation小节第1-2段

### 17. Background/BDA Value Creation efficiency paragraph

- order：17

- section：Background

- locator：Background/BDA Value Creation efficiency paragraph

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：效率是BDA价值创造的重要机制之一，例如制造业通过传感器和预测分析减少生产中断和运营成本。

- rhetorical_function_cn：展示效率机制在文献中的核心地位。

- depends_on_cn：BDA价值创造框架。

- sets_up_cn：为提出效率-个性化冲突提供一侧。

- evidence_pointer：Background中关于efficiency的段落

### 18. Background/BDA Value Creation personalization paragraph

- order：18

- section：Background

- locator：Background/BDA Value Creation personalization paragraph

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：个性化是另一个重要机制，例如电商BDA通过预测用户购买概率动态调整界面和产品推荐。

- rhetorical_function_cn：展示个性化机制在文献中的核心地位。

- depends_on_cn：BDA价值创造框架。

- sets_up_cn：为提出效率-个性化冲突提供另一侧。

- evidence_pointer：Background中关于personalization的段落

### 19. Background/BDA Value Creation summary paragraph

- order：19

- section：Background

- locator：Background/BDA Value Creation summary paragraph

- move_code：LIMITATION

- paraphrase_cn：现有IS BDA文献要么单向聚焦效率或个性化，要么将二者加总，忽略它们之间可能的冲突。

- rhetorical_function_cn：总结文献局限，是全文最重要的理论缺口句之一。

- depends_on_cn：上文对两种机制的综述。

- sets_up_cn：引出权衡理论视角。

- evidence_pointer：Background BDA value creation小节末段

### 20. Background/BDA Value Creation tradeoff theory paragraph

- order：20

- section：Background

- locator：Background/BDA Value Creation tradeoff theory paragraph

- move_code：THEORY_INTRO

- paraphrase_cn：权衡可以通过组织中的平衡实践来管理；运筹学虽有多种多目标优化方法，但通常要求决策者事先人工指定权重，难以应对变量多、动态变化或无法客观决策的情境。

- rhetorical_function_cn：引入权衡处理的理论视角，并说明既有方法的不足。

- depends_on_cn：前面识别出的冲突。

- sets_up_cn：为自动推断权衡权重的新方法提供必要性。

- evidence_pointer：Background BDA value creation小节中trade-off/operations research段落

### 21. Background/BDA Value Creation service robotics paragraph

- order：21

- section：Background

- locator：Background/BDA Value Creation service robotics paragraph

- move_code：MECHANISM

- paraphrase_cn：服务机器人将BDA的价值创造推向日常生活；效率收益主要落在系统层，而服务对象是个人，因此单个决策者无法预先解决权衡，必须在人机交互中动态确定偏好和权衡。

- rhetorical_function_cn：解释为什么服务机器人场景使权衡问题变得动态和难以人工管理。

- depends_on_cn：运筹学方法的局限。

- sets_up_cn：为新的实时ML方法提供问题空间。

- evidence_pointer：Background BDA value creation小节服务机器人段落

### 22. Background/BDA Value Creation final gap sentence

- order：22

- section：Background

- locator：Background/BDA Value Creation final gap sentence

- move_code：GAP

- paraphrase_cn：需要新方法来持续确定用户偏好并实时响应新环境。

- rhetorical_function_cn：从机制分析中提炼直接的方法缺口。

- depends_on_cn：服务机器人和人机交互的动态性。

- sets_up_cn：为AV案例和制品设计铺路。

- evidence_pointer：Background BDA value creation小节最后句

### 23. Background/AV section architecture and efficiency paragraph

- order：23

- section：Background

- locator：Background/AV section architecture and efficiency paragraph

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：AV架构由若干互连子模块组成；AV有潜力提高交通效率、降低排放和事故，IS研究已证明其能效优势。

- rhetorical_function_cn：将AV呈现为适合BDA效率研究的对象。

- depends_on_cn：服务机器人场景。

- sets_up_cn：为AV中的能效目标提供依据。

- evidence_pointer：Background AV section第1-2段

### 24. Background/AV section acceptance paragraph

- order：24

- section：Background

- locator：Background/AV section acceptance paragraph

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：IS技术接受研究指出，理解并回应驾驶者个人偏好（如平稳、愉悦的驾驶体验）对AV扩散至关重要。

- rhetorical_function_cn：将个性化目标引入AV情境。

- depends_on_cn：上一句效率目标。

- sets_up_cn：为效率-个性化冲突在AV中提供文献基础。

- evidence_pointer：Background AV section acceptance段落

### 25. Background/AV section second key insight limitation

- order：25

- section：Background

- locator：Background/AV section second key insight limitation

- move_code：LIMITATION

- paraphrase_cn：虽然一些IS学者同时讨论能效和便利性，但通常把它们当作加性优点，忽略了二者的潜在权衡。

- rhetorical_function_cn：直接指出AV IS研究对两个目标关系的处理不足。

- depends_on_cn：效率和接受度文献。

- sets_up_cn：提出AV中效率-个性化权衡是尚未研究的关键问题。

- evidence_pointer：Background AV section第二个key insight段

### 26. Background/AV section ML potential paragraph

- order：26

- section：Background

- locator：Background/AV section ML potential paragraph

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：IS AV研究表明ML在感知、轨迹规划等模块有潜力；例如基于卷积神经网络的场景理解。

- rhetorical_function_cn：承认ML在AV中的已有应用。

- depends_on_cn：AV架构情境。

- sets_up_cn：为指出ML尚未用于驾驶策略/偏好设计做铺垫。

- evidence_pointer：Background AV section第三个key insight段

### 27. Background/AV section ML gap sentence

- order：27

- section：Background

- locator：Background/AV section ML gap sentence

- move_code：GAP

- paraphrase_cn：现有IS的ML方案聚焦轨迹规划和物体识别，缺少同时处理能效驾驶策略和用户个性化偏好的设计研究。

- rhetorical_function_cn：将总缺口具体到ML/AI设计制品层面。

- depends_on_cn：ML应用综述。

- sets_up_cn：为本文制品设计提供直接空间。

- evidence_pointer：Background AV section第三个key insight末句

### 28. Background/AV section conclusion gap paragraph

- order：28

- section：Background

- locator：Background/AV section conclusion gap paragraph

- move_code：GAP

- paraphrase_cn：能效、个性化、BDA在AV研究中被隔离处理，既忽视了三者结合的潜力，也忽视了效率-个性化权衡；这一权衡在AV的高度动态环境中需要新的BDA方案来自动化权衡权重确定。

- rhetorical_function_cn：总结AV背景下的三重缺口，并再次强调动态权衡。

- depends_on_cn：前三部分文献综述。

- sets_up_cn：指向Figure 1和本文的Research Setting。

- evidence_pointer：Background AV section最后大段

### 29. Background/AV section adjacent fields paragraph

- order：29

- section：Background

- locator：Background/AV section adjacent fields paragraph

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：相邻领域用LSTM做能效预测、用示范学习做个性化驾驶，但存在静态、孤立训练、不考虑偏好随时间变化或依赖人工权重等问题。

- rhetorical_function_cn：说明技术侧已有起步，但都不满足动态实时权衡需求。

- depends_on_cn：IS AV gap。

- sets_up_cn：让本文的LSTM+DoL选题在相邻领域中具有增量贡献。

- evidence_pointer：Background AV section相邻领域段落

### 30. Research Setting P1-P2

- order：30

- section：Research Setting

- locator：Research Setting P1-P2

- move_code：REQUIREMENT

- paraphrase_cn：为在特定情境中解决实际驾驶策略问题，作者采用人本设计，并给出设计需求：需要能效模型、用户偏好模型和根据二者确定每时每刻配置的方法。

- rhetorical_function_cn：将文献缺口转译为具体设计要求，是需求到设计的桥梁。

- depends_on_cn：Background中的GAP。

- sets_up_cn：为DoL架构和后续三模块设计提供逻辑。

- evidence_pointer：Research Setting第1-2段

### 31. Research Setting P3-P4

- order：31

- section：Research Setting

- locator：Research Setting P3-P4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：由于是分布式、实时、大数据学习问题，作者采用DoL框架将任务分解为低复杂度子任务，由专家和中央执行者两类组件构成，并在专家中保留实时反馈能力。

- rhetorical_function_cn：解释选择DoL框架的原因，为制品架构提供方法论合法性。

- depends_on_cn：设计需求。

- sets_up_cn：为Design部分CE/Expert细节做铺垫。

- evidence_pointer：Research Setting第3-4段

### 32. Design Section first paragraph

- order：32

- section：Design Section

- locator：Design Section first paragraph

- move_code：DESIGN_FEATURE

- paraphrase_cn：应用以秒或毫秒为间隔处理输入并做高层配置决策，输入分为不可变环境变量和可修改配置变量。

- rhetorical_function_cn：确定ML应用的决策粒度和输入输出结构。

- depends_on_cn：Research Setting中的需求。

- sets_up_cn：为能效和偏好LSTM的输入输出定义做基础。

- evidence_pointer：Design Section第1段

### 33. Design Section second paragraph

- order：33

- section：Design Section

- locator：Design Section second paragraph

- move_code：DESIGN_FEATURE

- paraphrase_cn：系统包含三个ML模型：能效LSTM、偏好LSTM和权衡决策方法；用户可以通过手动设置配置来实现反馈。

- rhetorical_function_cn：总述三模型架构和用户反馈机制。

- depends_on_cn：输入输出定义。

- sets_up_cn：后续CE/Expert和公式细节都回到这一总述。

- evidence_pointer：Design Section第2段

### 34. Central Executive paragraph

- order：34

- section：Design Section

- locator：Central Executive paragraph

- move_code：DESIGN_FEATURE

- paraphrase_cn：中央执行者维护全局能效LSTM和平均用户偏好LSTM，并在每次驾驶结束后用整次驾驶能效更新能效模型，在用户锁定配置时更新偏好模型。

- rhetorical_function_cn：描述CE的职责和更新规则，体现DoL的general knowledge性质。

- depends_on_cn：DoL框架和三模型总述。

- sets_up_cn：为共享经济和跨用户学习提供机制。

- evidence_pointer：Design Section Central Executive段

### 35. Expert paragraph

- order：35

- section：Design Section

- locator：Expert paragraph

- move_code：DESIGN_FEATURE

- paraphrase_cn：专家在每步以用户偏好模型输出为起点，沿能效模型梯度方向调整配置，同时受锁定向量限制；公式(1)给出更新后的配置。

- rhetorical_function_cn：将权衡决策机制具体化为数学公式。

- depends_on_cn：能效/偏好模型输出。

- sets_up_cn：权重参数gamma、动量的引入。

- evidence_pointer：Design Section Expert段，公式(1)

### 36. Expert paragraph after formula (1)

- order：36

- section：Design Section

- locator：Expert paragraph after formula (1)

- move_code：MECHANISM

- paraphrase_cn：权衡参数根据锁定变量比例更新，锁定比例过半时向偏好方向移动，否则向能效方向移动；权衡动量随时间衰减，从而避免振荡。

- rhetorical_function_cn：解释自适应权衡算法的行为机制。

- depends_on_cn：公式(2)(3)的定义。

- sets_up_cn：为Discussion中的Proposition 1-4做理论铺垫。

- evidence_pointer：Design Section公式(2)(3)后的解释

### 37. Evaluation intro paragraph

- order：37

- section：Evaluation

- locator：Evaluation intro paragraph

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者解释评价分为能效预测模型和偏好估计模型两部分，并使用carsharing和Mafalda两个数据集；由于数据来自人驾车而非AV，需要通过转换和限制来评估自主驾驶目标。

- rhetorical_function_cn：说明评价策略和数据的合理使用方式。

- depends_on_cn：制品设计。

- sets_up_cn：后续两个子模块评价和第二个数据集验证。

- evidence_pointer：Evaluation开头段

### 38. Artifact Instantiation paragraph

- order：38

- section：Evaluation

- locator：Artifact Instantiation paragraph

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：超参数采用单变量逐个优化的近似方式，在30%用户子集上重复5次，选择平均绝对误差最低的值。

- rhetorical_function_cn：说明实例化方法的合理性，避免联合优化带来的不可行搜索空间。

- depends_on_cn：评价需要具体模型实例。

- sets_up_cn：给出Table 2中的最优超参数。

- evidence_pointer：Evaluation/Artifact Instantiation段

### 39. Artifact Instantiation tradeoff params paragraph

- order：39

- section：Evaluation

- locator：Artifact Instantiation tradeoff params paragraph

- move_code：DESIGN_FEATURE

- paraphrase_cn：设置权衡参数初始值gamma=0.01、动量=0.01、动量衰减=0.99、锁定时间=60个时间步。

- rhetorical_function_cn：将抽象参数实例化，使制品可复现。

- depends_on_cn：Design部分的参数定义。

- sets_up_cn：为后续整体行为命题提供初始条件。

- evidence_pointer：Evaluation/Artifact Instantiation第二段

### 40. Evaluation of Efficiency Prediction baseline list

- order：40

- section：Evaluation

- locator：Evaluation of Efficiency Prediction baseline list

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：能效预测与随机猜测、均值估计、线性回归、决策树、随机森林、前馈神经网络六类baseline比较。

- rhetorical_function_cn：建立评价参照，使LSTM的优势可衡量。

- depends_on_cn：评价设计。

- sets_up_cn：为展示Table 3/4的误差结果做铺垫。

- evidence_pointer：Evaluation of Efficiency Prediction段

### 41. Evaluation of Efficiency Prediction results

- order：41

- section：Evaluation

- locator：Evaluation of Efficiency Prediction results

- move_code：RESULT

- paraphrase_cn：尽管数据归一化后能效方差低导致baseline看似有效，但LSTM在两个数据集上大幅胜出，约3.5倍（主数据集）和40倍（Mafalda）于baseline。

- rhetorical_function_cn：报告能效预测核心结果，并解释baseline看起来有效的原因。

- depends_on_cn：前一句的baseline列表。

- sets_up_cn：为讨论LSTM能捕捉时间相关关系提供证据。

- evidence_pointer：Evaluation of Efficiency Prediction，Tables 3-4

### 42. Evaluation of Preference Estimation assumption

- order：42

- section：Evaluation

- locator：Evaluation of Preference Estimation assumption

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者假设用户手动选择的配置反映其真实偏好，以此作为偏好估计的ground truth。

- rhetorical_function_cn：为偏好估计评价定义可操作的标签来源。

- depends_on_cn：真实数据来自人工驾驶。

- sets_up_cn：为后续误差计算和结果解释提供假设约束。

- evidence_pointer：Evaluation of Preference Estimation第1段

### 43. Evaluation of Preference Estimation baselines

- order：43

- section：Evaluation

- locator：Evaluation of Preference Estimation baselines

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：除回归/树/森林/前馈NN外，还增加高斯概率密度和KDE（Gaussian/Cauchy核）等密度估计方法作为baseline。

- rhetorical_function_cn：扩展基准集，覆盖可能适合偏好多峰分布的密度估计。

- depends_on_cn：能效baseline列表。

- sets_up_cn：为展示偏好估计结果中KDE失效提供对照。

- evidence_pointer：Evaluation of Preference Estimation基线列表部分

### 44. Evaluation of Preference Estimation results

- order：44

- section：Evaluation

- locator：Evaluation of Preference Estimation results

- move_code：RESULT

- paraphrase_cn：LSTM偏好估计在carsharing数据集上约为最佳baseline精度的6倍，在Mafalda上约为2倍；KDE因多局部极大值偏差大。

- rhetorical_function_cn：报告偏好估计核心结果并解释KDE失败原因。

- depends_on_cn：前一句baseline设置。

- sets_up_cn：为讨论偏好建模的复杂性和LSTM优势提供证据。

- evidence_pointer：Evaluation of Preference Estimation，Tables 5-6

### 45. Discussion of Results first paragraph

- order：45

- section：Discussion

- locator：Discussion of Results first paragraph

- move_code：RESULT

- paraphrase_cn：与单模型ML应用相比，本文的多模型ML应用将问题分解为三个子问题，把决策过程隔离到由权衡参数决定；主数据集做严格评价，Mafalda数据集验证一般化。

- rhetorical_function_cn：重述设计逻辑并概括评价策略。

- depends_on_cn：整个评价部分。

- sets_up_cn：为继续解释baseline为何表现不佳和LSTM为何更好做开头。

- evidence_pointer：Discussion of Results第1段

### 46. Discussion of Results efficiency low variance paragraph

- order：46

- section：Discussion

- locator：Discussion of Results efficiency low variance paragraph

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：能效baseline看似精度高是因为归一化后目标变量方差低；LSTM通过时间关系超越静态相关性而获得更高精度。

- rhetorical_function_cn：进行边界解释，防止baseline的‘高精度’掩盖真实差异。

- depends_on_cn：评价结果。

- sets_up_cn：为LSTM在能效预测上的有效性提供机制解释。

- evidence_pointer：Discussion of Results能效低方差段

### 47. Discussion of Results preference complexity paragraph

- order：47

- section：Discussion

- locator：Discussion of Results preference complexity paragraph

- move_code：RESULT

- paraphrase_cn：偏好估计比能效预测复杂得多，因此需要两层约6300个神经元；结果仍大幅优于baseline，且增加更多隐藏层可能继续提升性能但会受计算时间限制。

- rhetorical_function_cn：解释偏好模型的更高复杂性和性能边界。

- depends_on_cn：偏好估计评价结果。

- sets_up_cn：为未来研究增加更多层/更多属性做伏笔。

- evidence_pointer：Discussion of Results偏好复杂度段

### 48. Analysis of the Application's Overall Behavior methodology

- order：48

- section：Discussion

- locator：Analysis of the Application's Overall Behavior methodology

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：由于无法在真实自主环境中评价整体系统，作者假设能效和偏好预测完美，通过数学分析对权衡模块行为提出命题。

- rhetorical_function_cn：为无法现场实验的情况提供替代性验证策略。

- depends_on_cn：前面子模块评价已完成但整体系统无法测试。

- sets_up_cn：引出Proposition 1-4。

- evidence_pointer：Analysis of Overall Behavior开头段

### 49. Analysis of Overall Behavior mechanism sentences

- order：49

- section：Discussion

- locator：Analysis of Overall Behavior mechanism sentences

- move_code：MECHANISM

- paraphrase_cn：系统总是从偏好配置出发向能效局部最优方向移动，步长由权衡参数决定；长期来看权重参数由用户干预频率决定。

- rhetorical_function_cn：在抽象层面解释权衡模块的工作原理和收敛方向。

- depends_on_cn：公式(1)-(3)。

- sets_up_cn：为Proposition 1a和1b做直接铺垫。

- evidence_pointer：Analysis of Overall Behavior第2-3段

### 50. Proposition 1a-1b sentences

- order：50

- section：Discussion

- locator：Proposition 1a-1b sentences

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：命题1a：用户完全不干预时系统选择能效局部最优；命题1b：用户总干预时系统完全偏向用户偏好。

- rhetorical_function_cn：给出权衡模块在两个极端用户行为下的行为保证。

- depends_on_cn：前面的机制分析。

- sets_up_cn：为命题2的收敛和命题3/4的中间情形铺路。

- evidence_pointer：Analysis of Overall Behavior Proposition 1a/1b

### 51. Proposition 2-4 sentences

- order：51

- section：Discussion

- locator：Proposition 2-4 sentences

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：命题2说明权衡模块在权衡动量归零时收敛；命题3给出偶尔干预下的最终权重公式；命题4给出早期完全锁定后的最终权重公式。

- rhetorical_function_cn：以数学命题刻画整体行为，使制品具有可检验的理论边界。

- depends_on_cn：公式(2)(3)和收敛概念。

- sets_up_cn：为讨论实践含义和未来研究提供条件。

- evidence_pointer：Analysis of Overall Behavior Proposition 2-4

### 52. Implications for IS Research first contribution paragraph

- order：52

- section：Discussion

- locator：Implications for IS Research first contribution paragraph

- move_code：CONTRIBUTION

- paraphrase_cn：第一项启示是向BDA价值创造研究引入权衡概念，并建议IS研究在调查和设计BDA应用时纳入矛盾/悖论理论。

- rhetorical_function_cn：将设计结果提升为IS研究的一般命题。

- depends_on_cn：背景部分的理论缺口。

- sets_up_cn：为第二项启示（日常生活情境）扩充理论贡献。

- evidence_pointer：Discussion Implications for IS Research第一段

### 53. Implications for IS Research second contribution paragraph

- order：53

- section：Discussion

- locator：Implications for IS Research second contribution paragraph

- move_code：CONTRIBUTION

- paraphrase_cn：第二项启示是将BDA价值创造从组织内部扩展到社会、日常生活情境，强调以人为中心和中间自动化水平，使用户能理解和干预ML决策。

- rhetorical_function_cn：扩展理论贡献到human-centered IS设计。

- depends_on_cn：第一项启示和制品中的用户干预机制。

- sets_up_cn：为AV开发者和共享商业模式的实践含义做铺垫。

- evidence_pointer：Discussion Implications for IS Research第二段

### 54. Implications for Developing AVs and Sharing Business Models technical requirements

- order：54

- section：Discussion

- locator：Implications for Developing AVs and Sharing Business Models technical requirements

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：实际部署需要车辆在驾驶开始和结束时能联网、具备一定计算和存储能力、并提供反馈或手动驾驶模块。

- rhetorical_function_cn：界定制品落地的技术边界条件。

- depends_on_cn：DoL架构假设。

- sets_up_cn：为实践可操作性提供清单。

- evidence_pointer：Implications for Developing AVs and Sharing Business Models段

### 55. Implications for Developing AVs and Sharing Business Models sharing economy paragraph

- order：55

- section：Discussion

- locator：Implications for Developing AVs and Sharing Business Models sharing economy paragraph

- move_code：DESIGN_KNOWLEDGE

- paraphrase_cn：共享经济环境让模型可以更快训练、用平均用户偏好作为新用户初始值，并减少对用户人口统计与偏好关系的昂贵研究。

- rhetorical_function_cn：提炼共享商业模式下的可复用设计知识。

- depends_on_cn：CE平均偏好模型的机制。

- sets_up_cn：为未来共享出行系统可以替代人工评分/偏好询问提供论点。

- evidence_pointer：Discussion共享经济段

### 56. Limitations and Future Research

- order：56

- section：Discussion

- locator：Limitations and Future Research

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：受制于无法在真实车流中测试AV控制器，作者承认数据属性有限、只考虑两三个可配置属性、未与其他AV模块交互，未来需要真实世界测试、探索其他ML模型和医疗等其他情境。

- rhetorical_function_cn：明确研究边界并开放未来研究方向。

- depends_on_cn：整个评价和讨论。

- sets_up_cn：文章在谦逊收束中结束，保护贡献不过度声明。

- evidence_pointer：Discussion Limitations and Future Research段

## 写作技术

- gap_construction_cn：文章先承认BDA价值创造研究和AV IS研究分别已经展示效率和个性化的重要性，然后反复指出两个文献流都把二者视为可加总或孤立处理；再通过运筹学方法需要人工指定权重、ML偏好方法静态/孤立等相邻领域证据，逐步把缺口收缩到‘缺少能动态自动平衡效率-个性化的设计制品’。

- signposting_cn：引言明确预告层级1设计制品和三个组成部分；Background以‘三个关键洞见’组织AV文献；Evaluation开头说明评价分为两个部分；Discussion开头总结DoL模块化设计；命题以数字编号显式给出，形成清晰路标。

- transition_logic_cn：每个章节末尾都指向下一节：Background从BDA价值创造到服务机器人再到AV和ML现状，最终推出Figure 1；Research Setting从缺口转向需求；Design从总体架构到CE/Expert细则；Evaluation从实例化转向两个子模型评价，再被Discussion的整体行为分析接续。

- claim_evidence_rhythm_cn：文章采用‘先声明后证据’的节奏：几乎每个设计选择后都紧跟公式或伪代码；每个比较性声明都紧跟baseline列表和误差表；讨论部分先复述结果，再做低方差/复杂度解释，最后以命题和启示提升抽象层次。

- benchmark_narrative_cn：Benchmark不是简单指标对比，而是被叙述为两个维度：能效预测与标准回归/ML基线比较，偏好估计再增加密度估计基线；在报告精度优势后，还解释baseline为何失效（低方差、静态相关性、KDE局部极大值），使LSTM优势具有机制解释而非偶然。

- theory_return_cn：讨论部分将评价结果回接到BDA价值创造理论和AV接受度理论：用能效和偏好模型的高精度说明BDA确实可以同时服务两个价值机制；用数学命题说明权衡模块在人机互动中的行为边界；再提出IS研究应引入矛盾/悖论视角和以人为中心的设计，从而完成从具体制品到理论贡的上升。

- contribution_positioning_cn：贡献被定位为双重：一是在概念层面引入效率-个性化权衡到BDA价值创造，二是在制品层面提供ML设计解决方案；这种定位使文章既不只是一个技术报告，也不只是一个理论评论，而是设计与理论的结合。

- novelty_protection_cn：作者通过三类策略防止贡献退化为一次性性能结果：一是强调与baseline相比的差距并解释差距来源；二是在第二个数据集上验证可迁移性；三是用数学命题刻画出系统行为的理论边界，使结果具有可检验、可扩展的设计知识属性。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：从目标领域文献中识别一个被隔离或加性处理的双目标问题；将问题落脚到读者关心的现实情境。

- research_job_cn：做窄而深的文献回顾，找到效率和个性化（或其他价值机制）在现有可能被忽略的冲突。

- required_evidence_cn：至少两类文献分别支持两个目标，且现有解决方案不能同时处理二者。

- transition_to_next_cn：用‘这种权衡在动态/人本场景下无法人工解决’过渡到新方法必要性。

#### 2. 2

- step：2

- writing_job_cn：把问题转化为一组明确的设计需求：系统需要哪些模型、需要何种实时决策机制。

- research_job_cn：选择一个可支撑分布式/模块化计算的方法论框架（如DoL），说明其与问题特征匹配。

- required_evidence_cn：每个需求都能追溯到前面的文献缺口或者场景特征。

- transition_to_next_cn：用‘我们据此开发制品’进入架构描述。

#### 3. 3

- step：3

- writing_job_cn：详细描述制品架构：模块划分、每个模块的输入输出、更新规则，以及模块之间如何交互。

- research_job_cn：把理论/框架翻译为可实现的组件选择（如LSTM、梯度更新、用户锁定信号）。

- required_evidence_cn：公式或伪代码可以表达决策过程；每个模块对应一个已提出的需求。

- transition_to_next_cn：用‘现在需要实例化并评价’进入评估部分。

#### 4. 4

- step：4

- writing_job_cn：在真实或仿真数据上实例化超参数，并建立明确的baseline列表。

- research_job_cn：准备至少一个主数据集和可选的第二数据集；确定与目标匹配的误差指标。

- required_evidence_cn：展示调参过程和baseline设置，使读者相信评价是公平的。

- transition_to_next_cn：分别报告两个子模型的误差表。

#### 5. 5

- step：5

- writing_job_cn：报告评价结果时先给表格，再解释baseline的局限和LSTM的优势机制。

- research_job_cn：对每个子模型进行系统比较，并在第二个数据集上重复验证。

- required_evidence_cn：误差表显示显著改善；并且最好有对改善机制的解释。

- transition_to_next_cn：说明整体系统无法直接测试，因此用数学命题替代。

#### 6. 6

- step：6

- writing_job_cn：在讨论中把子模型结果升级为整体行为命题，并连接理论贡献。

- research_job_cn：对无法实测的整体行为做数学或仿真分析，给出极端和中间情形的行为保证。

- required_evidence_cn：命题需要从公式或模型机制可推导；边界条件要明确。

- transition_to_next_cn：从命题转向IS研究和实践启示。

### most_transferable_moves_cn

1. 将gap从‘没人研究’升级为‘现有方法把目标隔离/加总，忽视冲突’

2. 用模块化框架把大型实时ML问题分解为系统级和个体级子问题

3. 在决策点设计用户反馈通道（手动覆盖/锁定）

4. 用公式表达决策规则和自适应权重更新

5. 在无法现场实验时用数学命题补足整体系统验证

6. 用第二个数据集和补充用户研究增强外部效度

### resource_intensive_or_nonstandard_parts_cn

1. 需要长期、大规模、包含用户行为的单车共享出行数据（约3.5万次驾驶）

2. 需要德国联邦经济部资助的carsharing项目数据作为主数据集

3. 需要额外获取Mafalda数据集进行验证

4. 在线补充附录中涉及用户调查/选择实验，需要额外研究资源和被试

5. LSTM超参数优化即使采用单变量搜索，仍需要重复训练大量模型

### what_not_to_copy_superficially_cn

1. 如果只有普通小型数据集，不能简单声称LSTM自动优于baseline，需要在相似数据规模下验证

2. ‘权衡模块有效’不能只靠命题推导，必须有评价或者至少仿真支持

3. 不能只引用DoL而忽视每个模块的具体数据流和更新公式

4. 不能把顾客WTP结果作为核心贡献而无详细样本和统计证据

- single_best_description_of_the_routine_cn：先指出文献把一个双目标问题当作可加总，再用模块化ML系统把两个目标分开建模并用自适应权重动态平衡，然后用双数据集benchmark和数学命题把性能差异提升为设计知识。

## 分析边界

本分析只能基于主文内容；Online Supplemental Appendices A、D、E未提供，顾客WTP、适应性分析和更多配置属性只能根据正文转述识别，无法核验具体统计结果；表格中的某些数值因OCR或排版可能有微小误差；数学公式中的OCR文本可能与原始公式存在格式不一致。
