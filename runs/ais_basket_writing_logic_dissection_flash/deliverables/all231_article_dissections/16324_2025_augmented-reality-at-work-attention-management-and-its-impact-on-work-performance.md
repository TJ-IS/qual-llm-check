# Augmented Reality at Work: Attention Management and Its Impact on Work Performance

- 作者：Runge Zhu; Cheng Yi; Ting Li
- 年份 / 期刊：2025 / MIS Quarterly
- DOI：10.25300/misq/2025/18944
- 源文件：16324_2025_augmented-reality-at-work-attention-management-and-its-impact-on-work-performance.md
- 论文主类型：field_intervention_or_platform_experiment
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.87

## 文章级论证概况

- 核心问题：在真实工业维修场景中，相比传统数字渠道（手机），通过增强现实（AR）眼镜提供任务信息如何影响工人的工作绩效，其内在机制是什么，以及信息的物理情境依赖性和信息复杂度如何调节这一效应？

- 制品与设计：研究采用现场随机实验，将飞机过站安全检查的逐步指导信息部署到AR眼镜和手机上。AR眼镜为GLXSS SE，采用棱镜投影，信息位于外周视野（中心视野外10-30度），手机为6.5英寸触摸屏；两种条件下均佩戴AR眼镜录制第一视角视频，并通过手机滑动确认步骤。实验在53个检查步骤中选取9个高错误步骤，操纵三种信息类型：Type I（低依赖、低复杂度通用提醒）、Type II（高依赖、低复杂度具体部件指令）、Type III（高依赖、高复杂度多部件指令）。

- 客观结果：AR相比手机显著提高了工作专注度，但直接效应不显著；工作专注度显著中介了信息渠道对视觉绩效和动作绩效的影响。信息复杂度负向调节AR对专注度的影响（AR×Complexity显著为负），信息依赖性正向调节专注度对绩效的影响（Attentiveness×Dependency显著为正）。AR对专注度的提升还溢出到后续两个无信息步骤，但未对绩效产生溢出。

- 核心贡献：作者主张：(1) 将AR研究从信息内容特征转向AR独有的信息显示位置，用divided attention理论解释AR如何减少注意力切换并提高绩效；(2) 识别出信息依赖性和信息复杂性作为边界条件；(3) 把divided attention理论扩展到AR空间显示与外周视觉处理情境；(4) 为工业AR采纳提供多维绩效证据和实践指导。

- 整篇论证链：作者从工业检查任务中频繁切换注意力的现实问题出发，指出现有AR研究多与纸张或口头指导比较，无法分离显示位置与信息内容的作用，因此需要以手机为对照来隔离AR的显示位置效应。作者引入divided attention理论和dual-task interference文献，提出AR利用外周视觉减少中央注意力切换、降低短时记忆负担，从而通过工作专注度提升绩效；并依据任务复杂性和任务间关系推断，信息复杂度会削弱AR优势，信息依赖性会增强专注度对绩效的作用。研究在真实航空公司对61名机务人员开展三批次现场实验，用第一视角视频、第三人视角视频、问卷和多源编码构建专注度、视觉检查绩效和标准动作绩效。主分析采用双向固定效应负二项回归和fractional logit，Sobel与PROCESS bootstrap验证了被调节的中介；一系列替代测量、逐步骤子样本、认知负荷、溢出效应和工作量异质性分析增强了机制与边界结论。讨论部分将结果重新连接到AR显示位置理论，指出AR适合高依赖低复杂度信息，复杂信息下AR优势减弱甚至手机可能更优，并给出混合使用AR与手机的设计方向。

## 类型与写作弧线判定

- 论文主类型判定：研究不是在实验室构建全新系统，而是在真实航空公司运行环境中，将AR眼镜与手机两种数字信息渠道作为干预对象，通过随机分配渠道和被试内操纵信息类型，对真实飞机维护任务中的工人行为与绩效进行现场因果检验。其核心证据来自现场实验而非离线benchmark或纯理论模型。

- 主导写作弧线判定：文章从现实注意力切换问题出发，引入divided attention理论形成假设，将理论机制翻译为AR眼镜与手机的信息显示位置差异及信息类型操纵设计，通过现场实验检验中介和调节效应，最后在讨论中把结果返回理论，修正并扩展对AR显示位置、外周视觉容量和注意力边界的理解。

## 研究开展程序

- study_or_phase_count：6

- 研究阶段总序列：研究按六阶段累积推进：理论建构与假设发展 → 实验设计与信息操纵 → 现场实验执行与多源数据采集 → 视频测量构建（人工编码+YOLO）→ 主假设检验（回归、Sobel）→ 稳健性与附加机制分析（PROCESS、替代测量、认知负荷、溢出效应、工作量异质性）。前两个阶段决定对比的因果结构，第三、四阶段提供高生态效度的数据与客观测量，第五阶段给出核心证据，第六阶段巩固机制解释并界定边界。

### studies_or_phases

#### 1. 理论建构与假设发展

- order：1

- name_cn：理论建构与假设发展

- question_cn：如何从divided attention和dual-task interference推导AR相对手机影响工作绩效的机制与边界条件？

- inputs_and_setting_cn：领域文献：divided attention（Kahneman, 1973）、dual-task interference（Pashler, 1994）、外周视觉研究（Chaturvedi等，2019；Vater等，2022）、上下文依赖记忆（Smith & Vela, 2001）、任务复杂度（Wood, 1986）。

- designed_or_compared_object_cn：概念性研究模型：信息渠道（AR vs. 手机）→ 工作专注度 → 工作绩效，信息复杂度调节第一段路径，信息依赖性调节第二段路径。

- baseline_control_or_counterfactual_cn：以手机作为传统数字渠道基准，用于隔离显示位置效应。

##### objective_metrics

（空）

- analysis_method_cn：理论推导和假设陈述，无实证分析。

- main_result_cn：提出H1（AR提高绩效并由专注度中介）、H2（复杂度削弱AR对专注度的作用）、H3（依赖性增强专注度对绩效的作用）。

- argumentative_role_cn：设定研究问题、核心构念、机制路径和边界条件，为实验设计与统计模型提供理论基础。

- remaining_uncertainty_cn：理论机制是否正确需要现场行为数据检验。

- link_to_next_phase_cn：假设中的信息渠道、复杂度、依赖性和绩效维度被操作化为实验设计中的变量。

##### evidence_pointers

1. Theory and Hypotheses Development sections

2. Figure 2 research model

#### 2. 实验设计与信息操纵

- order：2

- name_cn：实验设计与信息操纵

- question_cn：如何在真实飞机维护任务中操纵信息传递渠道和三类信息，形成可检验的对比？

- inputs_and_setting_cn：中国某航空公司Boeing 737-800过站安全检查任务（53步）、传统纸质job card、公司IT部门和资深工程师、以往易错步骤问卷、AR眼镜（GLXSS SE）与手机应用。

- designed_or_compared_object_cn：信息渠道为被试间操纵（AR vs. 手机）；信息类型为被试内三水平（Type I: 低依赖低复杂度；Type II: 高依赖低复杂度；Type III: 高依赖高复杂度），每个被试三轮任务各接收一种类型。

- baseline_control_or_counterfactual_cn：手机条件作为AR条件的对照；Type I作为低依赖基准，Type II作为高依赖低复杂度基准，Type III作为高复杂度对比。

##### objective_metrics

（空）

- analysis_method_cn：预实验问卷、试点测试、与工程师协作的内容设计。

- main_result_cn：选定9个步骤，覆盖超过80%的历史错误；两步间隔2秒可读；AR与手机使用相同步骤标题、相同指令文本和相同滑动确认流程。

- argumentative_role_cn：确保因果对比的内部效度：渠道差异集中于显示位置，信息类型差异集中于依赖性和复杂度。

- remaining_uncertainty_cn：被试是否真实感知到复杂度与依赖性的操纵差异尚需操纵检验。

- link_to_next_phase_cn：该设计直接生成三轮现场实验的数据采集流程。

##### evidence_pointers

1. Methodology: Experimental Design

2. Table 1

3. Figure 3a, 4, 5

#### 3. 现场实验执行与多源数据采集

- order：3

- name_cn：现场实验执行与多源数据采集

- question_cn：如何在真实工作场景中采集可反映专注度和绩效的行为数据？

- inputs_and_setting_cn：61名机务人员（31人AR条件，30人手机条件），2021年11月21日-12月15日三轮实验；AR眼镜录制第一视角视频，研究助理录制第三人视角视频，任务后问卷测量感知复杂性、依赖性和认知负荷等。

- designed_or_compared_object_cn：被试间随机分配渠道，被试内随机安排三类信息顺序；每个被试每轮完成一次完整检查任务。

- baseline_control_or_counterfactual_cn：手机条件、信息类型轮换顺序、个人特征（年龄、工龄、AR熟悉度、IT效能、工作量）作为控制。

##### objective_metrics

（空）

- analysis_method_cn：受控现场实验数据采集、问卷、视频录制。

- main_result_cn：形成183个用户-任务观测和1647个用户-步骤观测；两类条件在年龄、工龄、AR熟悉度、IT效能、工作量上无显著差异。

- argumentative_role_cn：提供高生态效度的数据基础，使结果能推广到真实工业场景。

- remaining_uncertainty_cn：原始视频需要进一步编码和识别才能转化为绩效指标。

- link_to_next_phase_cn：视频数据进入测量构建阶段。

##### evidence_pointers

1. Methodology: Experimental Procedure

2. Data and Measurement

3. Table 3

#### 4. 视频测量构建：专注度与多维绩效

- order：4

- name_cn：视频测量构建：专注度与多维绩效

- question_cn：如何用客观、可重复的方法把视频转换成工作专注度、视觉绩效和动作绩效？

- inputs_and_setting_cn：第一视角视频、第三人视角视频、维护手册、人工视频编码、YOLOv5目标识别模型（约3000张标注图像，12类关键部件，三位资深机务专家标注）。

- designed_or_compared_object_cn：专注度为每步中用于检查飞机或读取指令的时间占总时间比例；视觉绩效为在中央视野区域（20度水平×15度垂直）内出现的7个关键部件中被正确检查（至少2秒）的数量；动作绩效为6个需要下蹲步骤中执行标准下蹲动作的数量。

- baseline_control_or_counterfactual_cn：不同测量阈值作为稳健性替代：扩大中央视野至40×20度、延长时间窗至2.8秒、使用帧数而非二值、用指向动作替代下蹲。

##### objective_metrics

1. ICC = 0.81（专注度编码）

2. Inter-rater reliability = 0.83（动作编码）

3. YOLOv5 precision = 0.878, recall = 0.811, mAP = 0.842

- analysis_method_cn：人工视频编码、YOLOv5目标检测、自定义计数算法（Algorithm 1）。

- main_result_cn：成功构建3个核心因变量：工作专注度、视觉绩效、动作绩效。

- argumentative_role_cn：将理论构念落地为多维客观绩效，避免单一主观绩效造成的偏差。

- remaining_uncertainty_cn：测量阈值（2秒、中央区域大小）具有一定任意性，需要稳健性检验；部分部件因光照或遮挡无法识别。

- link_to_next_phase_cn：这些测量进入主假设检验。

##### evidence_pointers

1. Data and Measurement

2. Table 2

3. Figure 7

4. Appendix C, D

#### 5. 主假设检验：模型自由证据与回归分析

- order：5

- name_cn：主假设检验：模型自由证据与回归分析

- question_cn：H1-H3是否得到数据支持？

- inputs_and_setting_cn：183个用户-任务观测和1647个用户-步骤观测；视觉绩效用于5个有关键部件测量的步骤（N=915），动作绩效用于6个需要下蹲步骤（N=1098）。

- designed_or_compared_object_cn：比较AR与手机；高/低信息复杂度；高/低信息依赖性；以工作专注度为中介。

- baseline_control_or_counterfactual_cn：手机条件、低复杂度、低依赖性作为参照水平；逐步回归从无中介到全模型。

##### objective_metrics

1. Visual performance

2. Action performance

3. Work attentiveness

- analysis_method_cn：模型自由t检验与均值图、用户-步骤双向固定效应负二项回归（绩效）、fractional logit（专注度）、Sobel中介检验。

- main_result_cn：AR仅提高专注度而不直接提高绩效；专注度显著中介AR对两类绩效的影响（Sobel z=2.69和3.11）；AR×Complexity显著负向影响两类绩效；Attentiveness×Dependency显著正向影响两类绩效。

- argumentative_role_cn：核心因果链条和调节边界得到统计证实。

- remaining_uncertainty_cn：Sobel依赖正态假设；模型结构和固定效应选择可能存在备择解释。

- link_to_next_phase_cn：需用bootstrap和替代测量检验稳健性，并用附加分析提供机制证据。

##### evidence_pointers

1. Data Analysis and Results

2. Tables 4, 5

3. Figure 8, 9, 10

#### 6. 稳健性与附加机制分析

- order：6

- name_cn：稳健性与附加机制分析

- question_cn：主发现是否稳健？信息复杂度削弱AR优势的机制是否成立？AR效应是否具有溢出和工作量异质性？

- inputs_and_setting_cn：PROCESS Model 4/7/14、替代测量（扩大中央区域、延长窗口、帧数、指向动作）、逐步骤子样本、感知认知负荷问卷、后续无指令步骤、工作量中位数分组。

- designed_or_compared_object_cn：比较不同测量阈值、不同绩效操作化、不同步骤、不同工作量组，以及指令步骤后第一、二、三步的溢出效应。

- baseline_control_or_counterfactual_cn：PROCESS低/高调节水平下的条件间接效应；高vs低工作量组；受指令步骤vs无指令步骤。

##### objective_metrics

1. 95% bootstrap CI

2. Moderated mediation index

3. Cognitive load（问卷）

4. Workplace score/attentiveness spillover

- analysis_method_cn：PROCESS bootstrap（5000次重抽样）、重复测量ANOVA、子样本回归、分组回归。

- main_result_cn：H1-H3的调节中介指数显著且方向一致；替代测量和大多数步骤结论一致（步骤5/6因轮舱复杂而例外）；高复杂度下AR条件感知认知负荷显著高于手机；AR对专注度的提升溢出到随后两步但对绩效不溢出；高工作量组中AR优势更明显。

- argumentative_role_cn：把对主效应的依赖转化为对机制边界和设计条件的多层次证据，保护贡献不被视为一次性结果。

- remaining_uncertainty_cn：仍缺眼动或神经影像直接证据；低依赖高复杂度组合未纳入设计；步骤5/6的例外未完全解释。

- link_to_next_phase_cn：为讨论部分的理论深化和设计建议提供支持。

##### evidence_pointers

1. Robustness Checks and Additional Analysis

2. Tables 6, 7

3. Appendix E, F, G

## 各部分修辞架构

### abstract_moves

1. CONTEXT: AR是实时融合数字内容与现实环境的变革性显示技术。

2. THEORY_INTRO: 以divided attention theory研究信息渠道与信息性质对工作绩效的影响。

3. STUDY_OVERVIEW: 在飞机维护场景开展现场实验。

4. RESULT: 渠道效应由工作专注度中介；高物理情境依赖时AR更有效，高复杂度时AR优势减弱。

5. CONTRIBUTION: 加深对AR显示位置如何影响注意力管理与工作绩效的理解，并提供工业应用启示。

### introduction_moves

1. CONTEXT: 工业任务要求高度专注和精确执行。

2. PHENOMENON: 工人频繁在实体操作与纸/数字指导之间切换注意力。

3. PRACTICAL_STAKES: 企业积极寻找更无缝的信息传递方式。

4. GAP: AR相对传统数字设备的效果未知。

5. WHY_GAP_MATTERS: AR独特优势在于空间叠加，但缺乏理论理解。

6. METHOD_JUSTIFICATION: 以手机为对照隔离显示位置。

7. THEORY_INTRO: 引入divided attention和dual-task interference。

8. RQ_OR_OBJECTIVE: 提出两个研究问题。

9. STUDY_OVERVIEW: 预告航空公司现场实验。

10. RESULT: 简述核心发现与边界。

11. CONTRIBUTION: 宣告理论贡献与实践意义。

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE: 综述AR在电商、医疗、工业中的应用。

2. LIMITATION: 以往研究未分离显示位置与信息内容特征。

3. THEORY_INTRO: 解释divided attention作为有限注意资源理论。

4. MECHANISM: 注意切换依赖短时记忆，容量有限导致信息损失。

5. THEORY_INTRO: 引述dual-task interference的任务复杂度与任务间关系。

6. THEORY_INTRO: 引述外周视觉可以并行处理信息，作为外部记忆。

7. PRIOR_KNOWLEDGE: HCI中的空间连续性与外周显示设计。

8. THEORY_PROPOSITION: 综合指出AR可利用外周视觉减少切换成本，任务性质决定切换程度。

### artifact_design_moves

1. METHOD_JUSTIFICATION: 选择航空公司飞机过站检查作为高外部效度场景。

2. REQUIREMENT: 53步检查需逐步指导。

3. DESIGN_FEATURE: 描述AR眼镜棱镜投影、1.5米22英寸虚拟屏、外周10-30度显示、33.4克轻量设计。

4. METHOD_JUSTIFICATION: 两种条件均佩戴AR眼镜录制第一视角视频，且都用手机滑动切换步骤。

5. DESIGN_FEATURE: 选择9个高错误步骤并操纵信息类型。

6. DESIGN_FEATURE: 手机与AR均先显示步骤标题2秒再显示指导信息。

7. DESIGN_FEATURE: 定义三类信息：低依赖低复杂度、高依赖低复杂度、高依赖高复杂度。

8. METHOD_JUSTIFICATION: 解释为何不用完整2×2设计（低依赖高复杂度信息可能干扰当前操作）。

### evaluation_moves

1. METHOD_JUSTIFICATION: 用第一视角视频、第三人视角视频、问卷和机器学习构建多维绩效。

2. BENCHMARK_OR_CONTRAST: 以手机作为AR的对照通道。

3. BENCHMARK_OR_CONTRAST: 用Type I/II/III对比构建依赖性和复杂度操纵。

4. RESULT: 操纵检验显示三类信息在感知复杂性和依赖性上差异方向正确。

5. RESULT: 模型自由证据显示总效应不显著但专注度显著。

6. METHOD_JUSTIFICATION: 使用负二项回归和fractional logit适配计数/比例因变量。

7. RESULT: 回归支持中介与调节。

8. ROBUSTNESS_OR_BOUNDARY_TEST: PROCESS bootstrap、替代测量、子样本、认知负荷、溢出、工作量分析。

### discussion_and_contribution_moves

1. CONTRIBUTION: 将AR价值定位于信息显示位置而非信息内容。

2. BOUNDARY_CONDITION: AR优势在高依赖、低复杂度条件下最明显。

3. THEORY_RETURN: 扩展divided attention到外周视觉信息处理边界。

4. PRACTICAL_STAKES: 建议企业精选AR信息、避免过载、考虑AR与手机混合方案。

5. LIMITATION_AND_FUTURE: 指出样本、场景、操作化限制，呼吁眼动和神经影像研究。

## 理论/知识到设计的翻译

### 知识/理论基础

1. Divided attention theory (Kahneman, 1973)

2. Dual-task interference (Pashler, 1994)

3. Peripheral vision research (Chaturvedi et al., 2019; Vater et al., 2022; Rosenholtz et al., 2012)

4. Context-dependent memory (Smith & Vela, 2001; Barsalou, 1982)

5. Task complexity construct (Wood, 1986)

6. Work performance definition (Campbell & Wiernik, 2015)

- 理论—设计耦合：direct

- 耦合判定理由：divided attention和外周视觉机制直接决定了AR与手机显示位置的选择，以及信息复杂度、依赖性如何操纵和假设如何设置。理论命题被转化为可操作的渠道对比、三类信息操纵和中介/调节模型。虽然具体操纵受AR硬件限制（如无法直接在部件上叠放信息而用图像辅助），但核心设计差异仍然由理论目标指定，因此属于direct耦合。

- 理论到设计翻译链：理论命题：注意资源有限，中央注意力在多个对象间切换会产生切换成本和短时记忆负担；外周视觉能以较低精度并行处理空间邻近信息。→ 机制：手机要求用户把中心注意力从物理任务切换到屏幕，AR把信息放在外周视野，可并行读取。→ 设计要求：(1) 信息显示位置应与物理对象邻近且不遮挡中心视野；(2) 信息量应适配外周视觉低分辨率；(3) 高物理依赖信息需要与物理解释同时加工。→ 制品选择：使用AR眼镜（棱镜投影，信息位于视野外10-30度）与手机（屏幕位于手臂上）进行对比；信息类型用具体部件+图片代表高依赖，用多个部件清单代表高复杂度。→ 被检验差异：AR vs. 手机；Type I/II/III之间的复杂度与依赖性差异。→ 客观结果：专注度中介AR对绩效的正效应；复杂度削弱AR对专注度的作用；依赖性增强专注度对绩效的作用。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：中央注意力切换会占用有限注意资源并增加短时记忆负担，降低多任务绩效。

- mechanism_cn：手机需要用户从物理任务中脱离、将信息暂存于短时记忆，再重新定向到实体，造成反复切换。

- design_requirement_cn：信息显示位置应允许用户在保持中心视野于物理任务的同时获取虚拟信息。

- artifact_choice_cn：AR眼镜将指令显示在视野外10-30度的外周区域；手机作为对照显示在独立屏幕上。

- evaluated_contrast_cn：AR条件 vs. 手机条件。

- objective_result_cn：AR显著提高工作专注度（M_mobile=0.901, M_AR=0.927, p<0.001），并通过专注度间接提高视觉和动作绩效。

##### evidence_pointers

1. Figure 8

2. Tables 4, 5 Column 2/3

3. Table 6

#### 2. 2

- theory_or_knowledge_claim_cn：外周视觉分辨率较低，处理大量信息时会过载，需要把中央注意力切换到AR屏幕才能精确加工。

- mechanism_cn：高复杂度信息超过外周视觉并行处理能力，用户被迫反复在物理任务与AR显示之间切换，削弱AR的专注优势。

- design_requirement_cn：信息复杂度应作为调节变量操纵，考察AR优势的边界。

- artifact_choice_cn：低复杂度为单一部件指令（Type II），高复杂度为多部件清单（Type III）。

- evaluated_contrast_cn：AR×Complexity交互。

- objective_result_cn：AR×Complexity对视觉绩效（β=-0.742, p<0.001）和动作绩效（β=-0.520, p<0.01）均显著为负；bootstrap调节中介指数显著为负。

##### evidence_pointers

1. Tables 4, 5 Column 4/6

2. Table 7

3. Cognitive load analysis

#### 3. 3

- theory_or_knowledge_claim_cn：当两个任务共享情境元素或认知过程时，它们更相容，同时加工更有利。

- mechanism_cn：高物理依赖信息需要与具体物理部件同时解释，专注度高时整合效率更高；AR保持对物理情境的持续关注，因此高依赖条件下优势更大。

- design_requirement_cn：信息依赖性应作为调节变量操纵，用具体部件识别与图片表示高依赖，用通用提醒表示低依赖。

- artifact_choice_cn：Type II/III为高依赖（具体部件+图像），Type I为低依赖（“请仔细检查”式通用提醒）。

- evaluated_contrast_cn：Attentiveness×Dependency交互及AR条件间接效应在高/低依赖水平上的差异。

- objective_result_cn：Attentiveness×Dependency对视觉绩效（β=8.450, p<0.01）和动作绩效（β=7.061, p<0.001）显著为正；bootstrap调节中介指数显著为正。

##### evidence_pointers

1. Tables 4, 5 Column 5/6

2. Table 7

3. Figure 10

#### 4. 4

- theory_or_knowledge_claim_cn：外周视觉可作为“外部记忆”，在中心任务执行时提供易于访问的线索，减少短时记忆压力。

- mechanism_cn：AR把指导信息置于外周视野，相当于外部记忆，用户无需大量占用短时记忆即可获取信息，从而保持对主任务的持续关注。

- design_requirement_cn：绩效测量需要捕捉专注状态和标准遵循程度，而不只是完成时间。

- artifact_choice_cn：用第一视角视频中注视飞机/信息的时间比例测专注度；用关键部件检查数量和标准动作执行数量测多维绩效。

- evaluated_contrast_cn：AR→Attentiveness→Performance中介路径。

- objective_result_cn：AR→专注度系数显著（β≈1.08-1.17, p<0.001），专注度→两类绩效系数显著，Sobel中介检验p<0.01；bootstrap CI不含0。

##### evidence_pointers

1. Tables 4, 5

2. Table 6

3. Data and Measurement

## 评价逻辑

### evaluation_modes

1. Manipulation checks（重复测量ANOVA和配对比较）

2. Model-free evidence（均值图与t检验）

3. Two-way fixed effects negative binomial regression（绩效计数）

4. Fractional logit model（专注度比例）

5. Sobel mediation test

6. PROCESS Model 4/7/14 bootstrap moderated mediation

7. Robustness checks（替代测量、逐步骤子样本、替代动作指标）

8. Additional mechanism analysis（感知认知负荷）

9. Additional boundary analysis（溢出效应、工作量异质性）

- why_these_evaluations_cn：作者需要同时完成三类任务：证明操纵确实改变了被试对复杂度/依赖性的感知；检验渠道、中介和调节构成的理论模型；排除测量选择和局部步骤造成的偶然性。因此先用操纵检验和模型自由证据建立直观模式，再用固定效应回归/Sobel完成推断，最后用PROCESS和一系列替代测量把核心主张从特定测量和特定步骤中解放出来。

- benchmark_and_contrast_chain_cn：基准从渠道开始：手机是传统数字渠道，能够传递同样准确实时信息但显示位置不同；随后信息类型在Type I/II/III之间形成依赖性和复杂度的交叉对比；回归模型中的交互项在用户-步骤层面形成AR vs手机、低vs高复杂度、低vs高依赖性的边际对照；PROCESS条件间接效应进一步量化低/高调节水平下的差异；稳健性检验通过替代中央视野、时间窗、绩效操作化来检验测量阈值是否驱动结果。最终，这些对照共同把“AR更好”的粗claim分解为“AR在何种信息条件下、通过什么机制、对什么绩效维度有效”的精细claim。

### claim_evidence_ledger

#### 1. AR相对手机提高工作专注度

- claim_cn：AR相对手机提高工作专注度

- evidence_cn：模型自由t检验显著；fractional logit回归中AR系数显著（β=1.165, p<0.001；β=1.077, p<0.001）；PROCESS间接效应CI不含0。

- status_cn：支持

#### 2. 工作专注度中介AR对工作绩效的影响

- claim_cn：工作专注度中介AR对工作绩效的影响

- evidence_cn：Sobel z=2.69/3.11；PROCESS Model 4间接效应视觉[0.073,0.637]、动作[0.124,0.396]；直接效应不显著。

- status_cn：支持

#### 3. 信息复杂度削弱AR对专注度/绩效的正效应

- claim_cn：信息复杂度削弱AR对专注度/绩效的正效应

- evidence_cn：AR×Complexity显著负；PROCESS调节中介指数视觉[-0.141,-0.043]、动作[-0.345,-0.098]；高复杂度下AR感知认知负荷显著更高。

- status_cn：支持

#### 4. 信息依赖性增强专注度对绩效的正效应

- claim_cn：信息依赖性增强专注度对绩效的正效应

- evidence_cn：Attentiveness×Dependency显著正；PROCESS调节中介指数视觉[0.070,0.201]、动作[0.325,0.698]；高依赖条件下AR优势显著，低依赖条件不显著。

- status_cn：支持

#### 5. AR优势在低复杂度、高依赖时最强

- claim_cn：AR优势在低复杂度、高依赖时最强

- evidence_cn：Type II条件下AR视觉/动作绩效显著优于手机；Type III和Type I条件下无显著优势或方向逆转。

- status_cn：支持

#### 6. AR对专注度的影响溢出到后续步骤

- claim_cn：AR对专注度的影响溢出到后续步骤

- evidence_cn：对指令后第一、二步专注度回归AR系数显著（β=0.194, p<0.001；β=0.105, p<0.05），第三步不显著；绩效无溢出。

- status_cn：支持

#### 7. 高工作量用户从AR获益更大

- claim_cn：高工作量用户从AR获益更大

- evidence_cn：高工作量分组中AR对专注度、视觉和动作绩效的效应更强；低工作量组视觉绩效不显著。

- status_cn：支持

#### 8. 每个检查步骤都得到一致结论

- claim_cn：每个检查步骤都得到一致结论

- evidence_cn：逐步骤回归大体一致，但步骤5和6不显著，作者用轮舱结构复杂解释。

- status_cn：部分支持（整体稳健，但存在局部例外）

#### 9. 测量阈值不影响结论

- claim_cn：测量阈值不影响结论

- evidence_cn：扩大中央视野至40×20度、延长窗口至14帧、用帧数替代二值、用指向动作替代下蹲，结果一致。

- status_cn：支持

- internal_validity_strategy_cn：随机分配渠道；被试内随机化信息类型顺序；所有被试均佩戴AR眼镜录制第一视角视频以控制设备差异；两种条件下使用相同手机滑动确认机制和相同指令文本；对信息显示增加2秒标题间隔以控制注意力引导；使用个体固定效应和步骤固定效应消除未观察的个体与步骤差异；操纵检验确认感知差异；视频编码采用双编码和ICC/信度报告；YOLO模型用行业基准精度评价。

- external_validity_strategy_cn：选择真实航空公司、真实机务人员、真实Boeing 737-800过站检查任务；在持续约一个月的多轮现场实验中采集数据；与IT部门和资深工程师合作确保信息内容符合实际维护要求；使用真实工作负荷和工龄分布。

- what_is_not_actually_tested_cn：没有直接测量实际故障漏检率或飞行安全结果；没有用眼动追踪直接测量注意力切换次数或注视落点；没有直接测量外周视觉对复杂信息的处理容量；没有纳入低依赖高复杂度组合（Type IV），因此无法在完整2×2设计中检验两个调节变量之间是否独立；没有考察长期使用AR的适应效应；样本为男性机务人员，AR经验普遍较低，限制了对专家用户的推广。

## 贡献闭环

- technical_claim_cn：在飞机维护现场中，AR眼镜相对于手机提高了工作专注度，并通过该中介提高了视觉检查绩效和标准动作绩效；该技术效果在信息高物理依赖、低复杂度条件下更强，在高复杂度条件下减弱甚至反转。

- artifact_claim_cn：AR的显示位置设计（将虚拟信息置于外周视野）是产生绩效改善的关键；当信息复杂度增加导致外周视觉过载时，该设计优势消失。

- mechanism_claim_cn：AR通过减少中央注意力切换和降低短时记忆负担来提高工作专注度，从而改善物理任务中的信息整合；高复杂度会迫使中心注意力重新切换到AR屏幕，高依赖信息则使并行整合更加关键。

- boundary_claim_cn：AR对工作绩效的正效应主要出现在信息高度依赖具体物理情境且复杂度较低的任务步骤中；在低依赖或高复杂度条件下，AR相比手机无明显优势，复杂信息下手机在标准动作方面甚至可能表现更好；AR的专注效应可溢出到后续两个无指令步骤，但绩效不溢出；高工作量用户获益更大。

- reusable_design_knowledge_cn：企业采用AR时应优先显示与当前物理对象强相关且信息量精简的操作指令；避免在AR外周视野中堆积多部件/多操作信息；可将AR用于实时关键指令，将手机用于复杂信息检索与交互；培训与渐进式引入可帮助工人适应AR。

- theoretical_contribution_cn：将divided attention theory从传统屏幕/桌面情境扩展到AR空间显示和外周视觉情境，指出AR作为外部记忆可以降低切换成本，同时揭示外周视觉的信息处理容量边界；为理解空间显示配置如何影响注意力资源分配提供新问题。

- how_discussion_closes_intro_gap_cn：引言指出现有AR研究没有分离显示位置与信息内容特征；讨论部分以“信息显示位置”为核心重新组织发现，说明AR的优势和限制都源于外周视觉显示位置，并据此提出边界条件和使用建议，从而闭合缺口。

- overclaim_or_unsupported_leaps_cn：作者从“AR提高专注度并中介绩效”推断“AR减少注意力切换”，但没有眼动证据直接测量切换次数；用感知认知负荷作为机制证据是间接的；将步骤5/6的不一致解释为轮舱复杂而缺少独立证据；绩效定义采用行为标准遵循而非实际漏检率，可能使“工作绩效”主张偏窄；溢出效应只有专注度没有绩效，但实践建议里仍把注意力溢出作为优化提醒设计的依据，存在一定跳跃。

## 句级写作动作图谱

### 1. P1 S1

- order：1

- section：Introduction

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：许多工业场景要求工人保持高度专注并达到高绩效。

- rhetorical_function_cn：开篇确立研究的现实背景。

- depends_on_cn：无。

- sets_up_cn：引出飞机维修作为典型场景。

- evidence_pointer：Introduction第一段

### 2. P1 S2-S3

- order：2

- section：Introduction

- locator：P1 S2-S3

- move_code：PHENOMENON

- paraphrase_cn：飞机维修机械师必须按精确程序检查飞机，通常要借助纸或数字指南，导致注意力频繁在物理操作和指南间切换。

- rhetorical_function_cn：把一般背景具体化为注意力切换现象。

- depends_on_cn：背景句。

- sets_up_cn：为AR减少切换的设想提供问题基础。

- evidence_pointer：Introduction第一段

### 3. P1 S4

- order：3

- section：Introduction

- locator：P1 S4

- move_code：PRACTICAL_STAKES

- paraphrase_cn：注意力频繁切换会破坏专注、妨碍信息处理并损害绩效，因此企业正寻找更无缝的信息传递方式。

- rhetorical_function_cn：说明问题的重要性和紧迫性。

- depends_on_cn：注意力切换现象。

- sets_up_cn：为AR作为解决方案铺垫。

- evidence_pointer：Introduction第一段末尾

### 4. P2 S1

- order：4

- section：Introduction

- locator：P2 S1

- move_code：CONTEXT

- paraphrase_cn：企业开始探索用AR技术在检查和维护任务中实时传递信息。

- rhetorical_function_cn：引入技术方案。

- depends_on_cn：企业寻求无缝信息传递。

- sets_up_cn：说明AR的实践来源。

- evidence_pointer：Introduction第二段

### 5. P2 S2-S3

- order：5

- section：Introduction

- locator：P2 S2-S3

- move_code：PHENOMENON

- paraphrase_cn：AR通过透明屏幕把信息显示在物理对象附近，让用户中心视觉保持在任务上，信息位于外周视野。

- rhetorical_function_cn：概括AR显示位置特征。

- depends_on_cn：AR技术出现。

- sets_up_cn：为理论机制中的外周视觉概念做准备。

- evidence_pointer：Introduction第二段

### 6. P3 S1

- order：6

- section：Introduction

- locator：P3 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：DHL仓库工人戴AR眼镜，显示产品位置和数量等实时拣选信息。

- rhetorical_function_cn：给出真实案例，增加AR应用的现实感。

- depends_on_cn：AR显示位置特征。

- sets_up_cn：引出对AR有效性的疑问。

- evidence_pointer：Introduction第三段

### 7. P3 S2

- order：7

- section：Introduction

- locator：P3 S2

- move_code：GAP

- paraphrase_cn：但AR与传统数字设备相比能否促进工作仍未知。

- rhetorical_function_cn：提出核心知识缺口。

- depends_on_cn：AR现实应用与已有绩效证据。

- sets_up_cn：为研究问题提供理由。

- evidence_pointer：Introduction第三段

### 8. P3 S3

- order：8

- section：Introduction

- locator：P3 S3

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：由于AR能叠加信息在物理对象附近，而我们对并发处理物理和虚拟信息理解有限，需要评估AR相对传统渠道的绩效。

- rhetorical_function_cn：解释缺口为何重要，既有理论意义也有实践意义。

- depends_on_cn：AR显示位置的独特性。

- sets_up_cn：为采用手机对照提供依据。

- evidence_pointer：Introduction第三段

### 9. P4 S1

- order：9

- section：Introduction

- locator：P4 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本研究要考察AR相比手机如何影响工作绩效及其机制。

- rhetorical_function_cn：明确研究目标。

- depends_on_cn：前述缺口。

- sets_up_cn：引入绩效定义和文献比较。

- evidence_pointer：Introduction第四段

### 10. P4 S3

- order：10

- section：Introduction

- locator：P4 S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：已有研究表明AR相对纸质指导在操作精度、生产率和现场问题解决上有优势。

- rhetorical_function_cn：总结已有AR证据。

- depends_on_cn：研究目标。

- sets_up_cn：指出这些研究未隔离显示位置。

- evidence_pointer：Introduction第四段

### 11. P4 S4

- order：11

- section：Introduction

- locator：P4 S4

- move_code：LIMITATION

- paraphrase_cn：这些研究没有把AR独有的信息显示位置效应与一般数字信息内容的性质分离开。

- rhetorical_function_cn：定位文献局限。

- depends_on_cn：AR优势已有证据。

- sets_up_cn：确定本文切入点。

- evidence_pointer：Introduction第四段

### 12. P4 S5

- order：12

- section：Introduction

- locator：P4 S5

- move_code：GAP

- paraphrase_cn：因此缺乏对AR空间显示能力的理论理解。

- rhetorical_function_cn：进一步明确理论缺口。

- depends_on_cn：文献局限。

- sets_up_cn：引出手机对照设计。

- evidence_pointer：Introduction第四段

### 13. P4 S6

- order：13

- section：Introduction

- locator：P4 S6

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：选择手机作为另一数字渠道，因其也能提供准确实时信息但显示位置不同，从而能隔离显示位置效应。

- rhetorical_function_cn：为研究设计选择辩护。

- depends_on_cn：缺口是显示位置效应未分离。

- sets_up_cn：连接后面的现场实验。

- evidence_pointer：Introduction第四段

### 14. P4 S7

- order：14

- section：Introduction

- locator：P4 S7

- move_code：PRACTICAL_STAKES

- paraphrase_cn：手机仍是工业数字化中的主流工具，未来会与AR并存，因此比较二者有实际意义。

- rhetorical_function_cn：补充实际重要性。

- depends_on_cn：手机作为对照的合理性。

- sets_up_cn：增强研究动机。

- evidence_pointer：Introduction第四段末尾

### 15. P5 S1

- order：15

- section：Introduction

- locator：P5 S1

- move_code：THEORY_INTRO

- paraphrase_cn：作者引入divided attention（Kahneman）和dual-task interference（Pashler）作为理论透镜。

- rhetorical_function_cn：建立理论框架。

- depends_on_cn：需要解释注意力切换。

- sets_up_cn：推导AR机制和调节因素。

- evidence_pointer：Introduction第五段

### 16. P5 S2

- order：16

- section：Introduction

- locator：P5 S2

- move_code：MECHANISM

- paraphrase_cn：多任务间切换会竞争注意资源，导致绩效下降；手机会导致注意切换，AR可借助外周视野更平滑地获取信息。

- rhetorical_function_cn：用理论预测渠道效应。

- depends_on_cn：divided attention理论。

- sets_up_cn：为H1机制铺垫。

- evidence_pointer：Introduction第五段

### 17. P5 S3

- order：17

- section：Introduction

- locator：P5 S3

- move_code：MECHANISM

- paraphrase_cn：双任务干扰研究指出任务复杂性和任务间关系决定注意竞争程度。

- rhetorical_function_cn：引入两个调节因素的理论依据。

- depends_on_cn：dual-task interference文献。

- sets_up_cn：定义信息复杂度与依赖性。

- evidence_pointer：Introduction第五段

### 18. P6 S1

- order：18

- section：Introduction

- locator：P6 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：提出两个研究问题：AR与手机如何影响绩效及为什么；信息类型如何调节该效应。

- rhetorical_function_cn：正式锁定研究问题。

- depends_on_cn：理论和文献缺口。

- sets_up_cn：导入研究背景和实验摘要。

- evidence_pointer：Introduction第六段

### 19. P6 S2-S3

- order：19

- section：Introduction

- locator：P6 S2-S3

- move_code：STUDY_OVERVIEW

- paraphrase_cn：与中国某航空公司合作，在飞机维护场景进行现场实验；任务为53步的过站安全检查。

- rhetorical_function_cn：预告实证情境。

- depends_on_cn：两个研究问题。

- sets_up_cn：说明实验任务和合作方式。

- evidence_pointer：Introduction第六段

### 20. P6 S4-S5

- order：20

- section：Introduction

- locator：P6 S4-S5

- move_code：DESIGN_FEATURE

- paraphrase_cn：与IT部门和工程师合作，把步骤信息和记录功能放进AR和手机，并设计不同复杂度与依赖性的信息。

- rhetorical_function_cn：概括实验信息设计。

- depends_on_cn：现场实验背景。

- sets_up_cn：为方法论部分的具体操纵铺垫。

- evidence_pointer：Introduction第六段

### 21. P7 S1-S2

- order：21

- section：Introduction

- locator：P7 S1-S2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用AR眼镜记录第一视角视频，研究助理记录第三人视角视频，并结合人工编码和机器学习分析检查行为和动作是否符合标准。

- rhetorical_function_cn：说明绩效测量方法的选择理由。

- depends_on_cn：需要准确测量绩效。

- sets_up_cn：预告多源数据测量。

- evidence_pointer：Introduction第七段

### 22. P8 S1-S3

- order：22

- section：Introduction

- locator：P8 S1-S3

- move_code：RESULT

- paraphrase_cn：数据发现AR与手机对绩效的影响由工作专注度中介；高依赖时AR更有效，高复杂度时优势减弱；专注度提升还溢出到后两步。

- rhetorical_function_cn：提前给出主结果，设置读者预期。

- depends_on_cn：数据采集和分析。

- sets_up_cn：为贡献声明提供事实基础。

- evidence_pointer：Introduction第八段

### 23. P9

- order：23

- section：Introduction

- locator：P9

- move_code：CONTRIBUTION

- paraphrase_cn：贡献包括：推进AR空间显示能力理论、扩展divided attention到AR情境、为工业采纳提供实证依据并对显示设计提出警示。

- rhetorical_function_cn：宣告文章的理论与实践贡献。

- depends_on_cn：前面的结果。

- sets_up_cn：为全文定调。

- evidence_pointer：Introduction第九段

### 24. AR相关研究第一段

- order：24

- section：Literature Review

- locator：AR相关研究第一段

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：移动AR在电商中让消费者在真实环境中查看虚拟产品，增强产品理解和评价。

- rhetorical_function_cn：区分移动AR与穿戴式AR两种模式。

- depends_on_cn：AR应用范围。

- sets_up_cn：将焦点限定在工业穿戴式AR。

- evidence_pointer：Literature Review第一段

### 25. AR相关研究第二段

- order：25

- section：Literature Review

- locator：AR相关研究第二段

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：多数研究发现AR可提升生产率，例如Wuttke等人发现生产率提高43.8%，Vanneste等人发现错误率下降。

- rhetorical_function_cn：总结AR正效应证据。

- depends_on_cn：穿戴式AR情境。

- sets_up_cn：随后指出相反证据和局限。

- evidence_pointer：Literature Review第二段

### 26. AR相关研究第二段后半

- order：26

- section：Literature Review

- locator：AR相关研究第二段后半

- move_code：LIMITATION

- paraphrase_cn：也有研究发现AR可能分散注意、降低效率；总体未分离显示位置与信息特征。

- rhetorical_function_cn：呈现矛盾证据并识别方法论局限。

- depends_on_cn：前述AR研究。

- sets_up_cn：说明现有研究无法回答何时AR优于传统数字渠道。

- evidence_pointer：Literature Review第二段

### 27. HCI与认知科学综述段

- order：27

- section：Literature Review

- locator：HCI与认知科学综述段

- move_code：GAP

- paraphrase_cn：HCI和认知科学研究虽探讨了AR引导注意和近眼信息设计，但未提供AR如何塑造注意力管理和信息处理的理论。

- rhetorical_function_cn：将缺口扩展到相邻领域。

- depends_on_cn：文献回顾。

- sets_up_cn：引出attention理论综述。

- evidence_pointer：Literature Review第三段

### 28. 理论部分第一段

- order：28

- section：Literature Review

- locator：理论部分第一段

- move_code：THEORY_INTRO

- paraphrase_cn：divided attention理论认为注意是有限心理资源，可在不同活动间分配，切换会产生心理成本。

- rhetorical_function_cn：引入核心理论。

- depends_on_cn：需要注意力机制。

- sets_up_cn：导出短时记忆负担机制。

- evidence_pointer：Theoretical Foundation部分

### 29. 理论部分第二段

- order：29

- section：Literature Review

- locator：理论部分第二段

- move_code：MECHANISM

- paraphrase_cn：切换任务时大脑需回溯进度并保存信息，严重依赖容量有限的短时记忆，容易导致信息丢失。

- rhetorical_function_cn：解释切换成本为何损害绩效。

- depends_on_cn：divided attention理论。

- sets_up_cn：为AR减少切换的机制提供依据。

- evidence_pointer：Theoretical Foundation部分

### 30. dual-task interference段

- order：30

- section：Literature Review

- locator：dual-task interference段

- move_code：THEORY_INTRO

- paraphrase_cn：dual-task interference关注任务性质如何影响心理容量分配和干扰程度，任务复杂度与任务间关系是两个关键特征。

- rhetorical_function_cn：引入第二理论支柱。

- depends_on_cn：需要解释调节因素。

- sets_up_cn：为信息复杂度与依赖性调节提供理论来源。

- evidence_pointer：Theoretical Foundation部分

### 31. 外周视觉段

- order：31

- section：Literature Review

- locator：外周视觉段

- move_code：THEORY_INTRO

- paraphrase_cn：外周视觉可同时处理空间上接近的信息，被认为能减少中央注意切换，信息可充当外部记忆。

- rhetorical_function_cn：引入支持AR优势的认知机制。

- depends_on_cn：divided attention中并行处理。

- sets_up_cn：为AR显示位置设计奠基。

- evidence_pointer：Theoretical Foundation部分

### 32. H1前一段

- order：32

- section：Hypotheses Development

- locator：H1前一段

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：H1：使用AR（而非手机）进行指导的工人将获得更高工作绩效，且该效应由工作专注度中介。

- rhetorical_function_cn：正式提出主效应和中介假设。

- depends_on_cn：divided attention理论。

- sets_up_cn：作为后续调节假设的基础。

- evidence_pointer：Hypotheses Development, H1

### 33. 手机机制段

- order：33

- section：Hypotheses Development

- locator：手机机制段

- move_code：MECHANISM

- paraphrase_cn：使用手机时用户必须从物理任务中脱离，将关键信息存入短时记忆，再重新定向到任务，这个过程消耗大量认知资源。

- rhetorical_function_cn：细化手机条件的劣势。

- depends_on_cn：切换成本机制。

- sets_up_cn：支撑H1的第一个机制。

- evidence_pointer：H1推导部分

### 34. AR机制段

- order：34

- section：Hypotheses Development

- locator：AR机制段

- move_code：MECHANISM

- paraphrase_cn：AR把信息放在外周视野，可并行处理，用户不需要把中心注意从物理任务上移开，且信息作为外部记忆减少短时记忆压力。

- rhetorical_function_cn：细化AR条件的优势。

- depends_on_cn：外周视觉与外部记忆。

- sets_up_cn：支撑H1的第二个机制。

- evidence_pointer：H1推导部分

### 35. 调节总述段

- order：35

- section：Hypotheses Development

- locator：调节总述段

- move_code：THEORY_PROPOSITION

- paraphrase_cn：信息复杂度主要通过影响注意切换需求来调节渠道与专注度的关系，信息依赖性主要通过影响整合需求来调节专注度与绩效的关系。

- rhetorical_function_cn：指定两个调节变量的作用位点。

- depends_on_cn：dual-task interference。

- sets_up_cn：为H2/H3分别设置在模型中的不同路径。

- evidence_pointer：Hypotheses Development调节段

### 36. H2推导

- order：36

- section：Hypotheses Development

- locator：H2推导

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：H2：信息复杂度会负向调节AR通过工作专注度对绩效的间接效应，高复杂度削弱AR对专注度的影响。

- rhetorical_function_cn：正式提出第一个调节假设。

- depends_on_cn：外周视觉分辨率限制。

- sets_up_cn：为检验复杂度的实验操纵提供目标。

- evidence_pointer：Hypotheses Development, H2

### 37. H3推导

- order：37

- section：Hypotheses Development

- locator：H3推导

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：H3：信息依赖性会正向调节工作专注度对工作绩效的作用，高依赖性增强专注度对绩效的贡献。

- rhetorical_function_cn：正式提出第二个调节假设。

- depends_on_cn：上下文依赖记忆与任务相容性。

- sets_up_cn：为检验依赖性的实验操纵提供目标。

- evidence_pointer：Hypotheses Development, H3

### 38. Empirical Setting第一段

- order：38

- section：Methodology

- locator：Empirical Setting第一段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：与一家中国大型航空公司合作，在机场进行随机现场实验，以飞机维护作为高外部效度场景。

- rhetorical_function_cn：说明实证场景选择理由。

- depends_on_cn：研究问题和假设。

- sets_up_cn：引出具体检查任务。

- evidence_pointer：Methodology: Empirical Setting

### 39. Empirical Setting第二段

- order：39

- section：Methodology

- locator：Empirical Setting第二段

- move_code：REQUIREMENT

- paraphrase_cn：过站安全检查包括53步，每步要求机务在指定位置检查相关部件，传统上用厚纸版job card指导。

- rhetorical_function_cn：描述任务结构和信息需求。

- depends_on_cn：飞机维护场景。

- sets_up_cn：说明为何需要逐步数字指导。

- evidence_pointer：Methodology: Empirical Setting

### 40. Experimental Design第一段

- order：40

- section：Methodology

- locator：Experimental Design第一段

- move_code：DESIGN_FEATURE

- paraphrase_cn：使用GLXSS SE AR眼镜，棱镜投影在1.5米处形成约22英寸虚拟画面，位于焦点视线之外但始终在外周视野可用。

- rhetorical_function_cn：描述AR硬件如何实现外周显示。

- depends_on_cn：外周视觉设计要求。

- sets_up_cn：为AR与手机的显示位置差异提供物化基础。

- evidence_pointer：Methodology: Experimental Design

### 41. Experimental Design第一段后半

- order：41

- section：Methodology

- locator：Experimental Design第一段后半

- move_code：DESIGN_FEATURE

- paraphrase_cn：AR眼镜有高分辨率摄像头可记录第一视角视频，仅重33.4克，且可配近视镜片，适合工业长时间佩戴。

- rhetorical_function_cn：说明硬件同时支持数据采集和工业可用性。

- depends_on_cn：设备选择。

- sets_up_cn：为视频测量和现场实施做铺垫。

- evidence_pointer：Methodology: Experimental Design

### 42. Experimental Design第二段

- order：42

- section：Methodology

- locator：Experimental Design第二段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：所有被试都佩戴AR眼镜并连接绑在手臂上的手机，AR与手机条件都用手机滑动进入下一步，从而只改变信息显示位置。

- rhetorical_function_cn：强调跨条件保持一致的操作流程。

- depends_on_cn：需要隔离显示位置。

- sets_up_cn：提高内部效度。

- evidence_pointer：Methodology: Experimental Design

### 43. Experimental Design第三段

- order：43

- section：Methodology

- locator：Experimental Design第三段

- move_code：DESIGN_FEATURE

- paraphrase_cn：选择9个易错步骤进行信息操纵，这些步骤覆盖了80%以上的历史错误。

- rhetorical_function_cn：说明操纵步骤的选择有现场依据。

- depends_on_cn：预实验问卷和错误记录。

- sets_up_cn：保证信息操纵的任务相关性。

- evidence_pointer：Methodology: Experimental Design

### 44. Experimental Design第四段

- order：44

- section：Methodology

- locator：Experimental Design第四段

- move_code：DESIGN_FEATURE

- paraphrase_cn：手机条件中，步骤标题和指导信息在同一屏幕显示但有2秒间隔；AR条件中，指导信息在标题显示两秒后出现，两种条件指令文本相同。

- rhetorical_function_cn：说明信息时序在不同渠道中的对应设计。

- depends_on_cn：需要避免文本可读性差异。

- sets_up_cn：为渠道对比提供严格操纵。

- evidence_pointer：Methodology: Experimental Design

### 45. Experimental Design信息类型段

- order：45

- section：Methodology

- locator：Experimental Design信息类型段

- move_code：DESIGN_FEATURE

- paraphrase_cn：低依赖信息是通用提醒“请仔细检查”，高依赖信息是指定当前区域的特定部件并配图像；低复杂度为一个部件，高复杂度为多个部件。

- rhetorical_function_cn：描述信息类型操纵的具体内容。

- depends_on_cn：信息依赖性和复杂度定义。

- sets_up_cn：为操纵检验和假设检验提供材料。

- evidence_pointer：Methodology: Experimental Design, Table 1

### 46. Experimental Design信息类型段后

- order：46

- section：Methodology

- locator：Experimental Design信息类型段后

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：由于低依赖高复杂度信息可能提供大量与当前部件无关的内容而分散注意力，实验采用三种信息类型而非完整2×2设计。

- rhetorical_function_cn：解释设计偏离完整因子设计的工程与注意力原因。

- depends_on_cn：真实任务中对分心的担忧。

- sets_up_cn：说明后续统计比较只能依赖Type I/II/III的部分对比。

- evidence_pointer：Methodology: Experimental Design

### 47. Data and Measurement表2前

- order：47

- section：Methodology

- locator：Data and Measurement表2前

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：定义三个因变量：专注度为步骤内检查时间占比，视觉绩效为检查到的关键部件数量，动作绩效为执行标准动作数量。

- rhetorical_function_cn：建立测量基准。

- depends_on_cn：绩效定义（Campbell & Wiernik）。

- sets_up_cn：为后续模型分析提供因变量。

- evidence_pointer：Methodology: Data and Measurement, Table 2

### 48. Data and Measurement视觉绩效段

- order：48

- section：Methodology

- locator：Data and Measurement视觉绩效段

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：用YOLO识别第一视角视频中的关键部件，只统计出现在中央视野区域且持续至少2秒的部件作为视觉绩效。

- rhetorical_function_cn：说明视觉绩效的客观计算规则。

- depends_on_cn：注意力和视觉加工理论中的中央视野概念。

- sets_up_cn：为机器学习测量提供算法基础。

- evidence_pointer：Methodology: Data and Measurement, Figure 7

### 49. Manipulation Check

- order：49

- section：Data Analysis and Results

- locator：Manipulation Check

- move_code：RESULT

- paraphrase_cn：操纵检验显示Type III被感知为比Type I和II更复杂；Type II和III被感知为比Type I更依赖物理情境，方向和设计一致。

- rhetorical_function_cn：验证实验操纵的有效性。

- depends_on_cn：三类信息操纵。

- sets_up_cn：使后续因果解释可信。

- evidence_pointer：Data Analysis and Results: Manipulation Check

### 50. Model-Free Evidence

- order：50

- section：Data Analysis and Results

- locator：Model-Free Evidence

- move_code：RESULT

- paraphrase_cn：模型自由证据显示AR显著提高专注度，但总体视觉和动作绩效差异不显著。

- rhetorical_function_cn：说明总效应不显著，为中介解释设置前提。

- depends_on_cn：数据集构造。

- sets_up_cn：引出回归分析中的中介模型。

- evidence_pointer：Data Analysis and Results: Model-Free Evidence, Figure 8

### 51. Model-Free Evidence复杂度和依赖性图

- order：51

- section：Data Analysis and Results

- locator：Model-Free Evidence复杂度和依赖性图

- move_code：RESULT

- paraphrase_cn：在低复杂度高依赖条件下AR绩效显著优于手机；高复杂度条件下AR优势消失甚至反转；低依赖条件下AR优势不显著。

- rhetorical_function_cn：用图形展示调节效应的直观模式。

- depends_on_cn：Type II/III/I对比。

- sets_up_cn：支持H2和H3。

- evidence_pointer：Figures 9, 10

### 52. Regression Analysis模型设定段

- order：52

- section：Data Analysis and Results

- locator：Regression Analysis模型设定段

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：在用户-步骤层面建立双向固定效应模型，绩效用负二项回归，专注度用fractional logit，以匹配计数和比例分布。

- rhetorical_function_cn：论证统计模型与数据结构匹配。

- depends_on_cn：用户-步骤面板数据。

- sets_up_cn：呈现Tables 4/5结果。

- evidence_pointer：Data Analysis and Results: Regression Analysis

### 53. Regression Analysis结果段

- order：53

- section：Data Analysis and Results

- locator：Regression Analysis结果段

- move_code：RESULT

- paraphrase_cn：AR不直接显著提高绩效，但显著提高专注度；专注度显著预测绩效；Sobel检验支持中介。

- rhetorical_function_cn：报告H1验证结果。

- depends_on_cn：负二项和fractional logit回归。

- sets_up_cn：为H2/H3交互结果奠定模型路径。

- evidence_pointer：Tables 4, 5 Columns 1-3

### 54. Regression Analysis H2/H3结果段

- order：54

- section：Data Analysis and Results

- locator：Regression Analysis H2/H3结果段

- move_code：RESULT

- paraphrase_cn：AR×Complexity显著负，Attentiveness×Dependency显著正，全模型结果稳定。

- rhetorical_function_cn：报告H2/H3验证结果。

- depends_on_cn：交互项设定。

- sets_up_cn：为bootstrap调节中介提供依据。

- evidence_pointer：Tables 4, 5 Columns 4-6

### 55. Bootstrapping Analysis

- order：55

- section：Robustness Checks

- locator：Bootstrapping Analysis

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：PROCESS Model 4/7/14的bootstrap结果显示中介效应和两个调节中介指数均显著，CI不含零。

- rhetorical_function_cn：用非参数推断替代Sobel，巩固中介与调节中介。

- depends_on_cn：主回归结果。

- sets_up_cn：为宣称稳健性提供证据。

- evidence_pointer：Tables 6, 7

### 56. Robustness Checks替代测量段

- order：56

- section：Robustness Checks

- locator：Robustness Checks替代测量段

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：改变中央视野范围、时间窗口、绩效编码方式、动作指标，结论保持稳定；逐步骤分析中步骤5/6例外。

- rhetorical_function_cn：检验测量选择是否驱动结果。

- depends_on_cn：主结果。

- sets_up_cn：界定结果对测量误差的敏感性。

- evidence_pointer：Appendix E

### 57. 认知负荷分析

- order：57

- section：Additional Analysis

- locator：认知负荷分析

- move_code：RESULT

- paraphrase_cn：高复杂度条件下，AR条件被试报告更高的感知认知负荷；低复杂度条件无差异。

- rhetorical_function_cn：提供与H2机制相关的额外证据。

- depends_on_cn：复杂度削弱AR的机制。

- sets_up_cn：说明AR过载来自外周视觉处理容量。

- evidence_pointer：Additional Analysis on Perceived Cognitive Load

### 58. 溢出效应分析

- order：58

- section：Additional Analysis

- locator：溢出效应分析

- move_code：RESULT

- paraphrase_cn：AR对专注度的提升溢出到指令步骤后的第一、二步，但绩效没有溢出。

- rhetorical_function_cn：拓展AR效应的动态范围。

- depends_on_cn：主结果。

- sets_up_cn：支持实践建议中减少提醒以优化显示空间。

- evidence_pointer：Additional Analysis on Spillover Effects and Workload, Appendix F

### 59. 工作量异质性分析

- order：59

- section：Additional Analysis

- locator：工作量异质性分析

- move_code：RESULT

- paraphrase_cn：高工作量组中AR显著提升专注度和绩效；低工作量组中视觉绩效优势不显著。

- rhetorical_function_cn：提供AR价值的边界异质性。

- depends_on_cn：主结果和认知资源有限性。

- sets_up_cn：强化“AR对注意资源紧张者更有利”的解释。

- evidence_pointer：Additional Analysis on Workload, Appendix G

### 60. 第一段

- order：60

- section：Discussion

- locator：第一段

- move_code：CONTRIBUTION

- paraphrase_cn：研究发现信息提供渠道对绩效的影响由专注度中介，AR降低分心并促进信息与任务整合。

- rhetorical_function_cn：重述核心发现。

- depends_on_cn：全部分析结果。

- sets_up_cn：展开理论意义。

- evidence_pointer：Discussion第一段

### 61. 第二段

- order：61

- section：Discussion

- locator：第二段

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：高依赖信息会放大AR优势，高复杂度信息会使AR优势减弱，复杂信息下手机可能在标准动作方面更有效。

- rhetorical_function_cn：明确边界条件。

- depends_on_cn：H2/H3结果。

- sets_up_cn：为理论和实践建议提供限制条件。

- evidence_pointer：Discussion第二段

### 62. 第一点

- order：62

- section：Theoretical Implications

- locator：第一点

- move_code：THEORY_RETURN

- paraphrase_cn：文章把AR价值定位为信息显示位置，基于divided attention解释其减少切换成本，为空间显示配置研究提出新问题。

- rhetorical_function_cn：将经验发现上升为理论贡献。

- depends_on_cn：讨论中的核心发现。

- sets_up_cn：把结果连接到未来研究议程。

- evidence_pointer：Theoretical Implications第一点

### 63. 第三点

- order：63

- section：Theoretical Implications

- locator：第三点

- move_code：THEORY_RETURN

- paraphrase_cn：研究揭示用户在peripheral vision中处理复杂信息的能力有限，扩展了divided attention理论对注意力边界的理解。

- rhetorical_function_cn：明确理论对原有知识的扩展。

- depends_on_cn：认知负荷分析。

- sets_up_cn：提出关于注意可塑性和混合现实的新问题。

- evidence_pointer：Theoretical Implications第三点

### 64. 第二点

- order：64

- section：Practical Implications

- locator：第二点

- move_code：PRACTICAL_STAKES

- paraphrase_cn：实施AR时应精选信息而非展示全部数据，避免信息过载，并可用混合方案让手机承担复杂信息交互。

- rhetorical_function_cn：把边界条件转化为可操作建议。

- depends_on_cn：复杂度和溢出效应结果。

- sets_up_cn：落地到企业数字化转型决策。

- evidence_pointer：Practical Implications第二点

### 65. 全文最后一段

- order：65

- section：Limitations and Future Research

- locator：全文最后一段

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：指出样本规模、单一场景、有限AR经验、单一操纵方式等限制，并呼吁眼动和神经影像提供更直接认知机制证据。

- rhetorical_function_cn：诚实界定结果适用范围并引导未来研究。

- depends_on_cn：全部结论。

- sets_up_cn：保护文章不被过度一般化。

- evidence_pointer：Limitations and Future Research

## 写作技术

- gap_construction_cn：先把AR研究归纳为“AR vs 纸张/口头指导并强调信息内容或实时性”，然后指出这些对照无法回答AR独有显示位置的价值；再以手机作为对照，把缺口精确化为“信息显示位置是否以及何时影响注意力和绩效”。同时利用AR文献中正反不一致的结果（部分提高生产率、部分分散注意）强化需要理论解释的必要性。

- signposting_cn：引言直接预告两个研究问题；假设部分说明总体研究模型并分段陈述H1/H2/H3；方法部分用独立小节标出empirical setting、experimental design、procedure、data and measurement；分析部分用manipulation check、model-free evidence、regression、robustness划清证据层次。

- transition_logic_cn：从现实问题到AR应用再到理论缺口；从divided attention到dual-task interference再到外周视觉；每个假设先给出机制后正式陈述；从主分析到bootstrap、替代测量、认知负荷、溢出、工作量，层层递进验证主结论并扩展边界。

- claim_evidence_rhythm_cn：作者坚持“先直观证据后统计推断”：先给图8-10的均值图，再给Tables 4/5的回归，再用PROCESS的CI确认，最后用感知认知负荷解释机制。每个结论都配有p值或置信区间，并且总效应不显著也如实报告，以凸显中介链条而非简单均值差异。

- benchmark_narrative_cn：benchmark不是技术数据集，而是“手机作为传统数字渠道”的现场对照。叙事中反复强调手机也能提供准确实时信息，差异只在显示位置；随后通过Type I/II/III把复杂度和依赖性做成被试内对比；最后用替代测量和逐步骤分析证明基准不影响结论。

- theory_return_cn：讨论部分把“AR提高专注度”重新表述为“显示位置通过外周视觉减少注意切换”，把“高复杂度削弱AR”表述为“peripheral vision处理精度有限”，从而把经验结果升华为divided attention在空间显示情境下的边界扩展。

- contribution_positioning_cn：作者把贡献放置在三个已知文献的交汇处：AR研究缺显示位置理论、divided attention缺空间显示应用、工业AR研究缺多维绩效证据；通过明确“不是AR整体优于手机”而是“在特定信息条件下通过专注度起作用”来避免过度宣称。

- novelty_protection_cn：通过大量稳健性检验把效应从特定测量阈值、特定步骤、特定绩效操作化中解放出来；通过认知负荷证据给复杂性调节提供独立机制支持；通过溢出效应和工作量异质性展示效应不是仅限于九个指令步骤；通过讨论明确边界，防止把一次性现场结果包装成普遍规律。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：从现实任务中提取注意力切换现象，引出企业寻求无缝信息传递，再定位AR显示位置的重要性和未知性。

- research_job_cn：选择能体现注意力切换问题的高风险真实任务，并确认该任务有明确标准步骤。

- required_evidence_cn：需要现实场景证据（如飞机检查、易错步骤、企业数字化诉求）。

- transition_to_next_cn：指出现有文献未分离显示位置与信息内容，从而转向理论透镜。

#### 2. 2

- step：2

- writing_job_cn：介绍divided attention和dual-task interference，推导渠道效应和两类信息属性调节的机制。

- research_job_cn：从理论机制中确定可操作化构念：显示位置、工作专注度、信息复杂度、信息依赖性。

- required_evidence_cn：需要理论文献支持注意切换成本、外周视觉并行加工、任务复杂度/关系影响干扰。

- transition_to_next_cn：将理论机制写成H1/H2/H3，并说明调节发生在中介路径的不同环节。

#### 3. 3

- step：3

- writing_job_cn：描述现场任务、设备选择和实验操纵，重点说明对照渠道如何隔离变量。

- research_job_cn：设计随机现场实验，确保两种渠道除显示位置外其他交互一致；设计信息类型操纵；选择高错误步骤。

- required_evidence_cn：需要合作单位、真实任务步骤、历史错误数据、可录制视频的AR设备。

- transition_to_next_cn：说明如何采集行为数据和问卷，并预告多源测量。

#### 4. 4

- step：4

- writing_job_cn：详细定义因变量和测量流程，并给出编码信度或算法精度。

- research_job_cn：用视频编码、目标检测、人工行为编码把构念转化为客观指标。

- required_evidence_cn：需要编码手册、信度系数、模型precision/recall/mAP，以及阈值的稳健性检验。

- transition_to_next_cn：数据准备好后进入假设检验。

#### 5. 5

- step：5

- writing_job_cn：先给操纵检验和模型自由证据，再给回归和被调节的中介结果。

- research_job_cn：执行与因变量分布匹配的回归模型，报告总效应、中介、交互和Sobel/bootstrap。

- required_evidence_cn：需要显著调节中介指数、置信区间、稳健性替代测量。

- transition_to_next_cn：通过机制附加分析和子样本分析说明结果的机制与边界。

#### 6. 6

- step：6

- writing_job_cn：讨论部分把结果返回理论，明确边界，给出设计和实践建议，并列出限制。

- research_job_cn：将经验模式与理论预期对照，提出可复用的设计原则。

- required_evidence_cn：需要前序分析的稳健机制证据，避免仅作事后解释。

- transition_to_next_cn：以限制和未来研究收尾，表明理论仍有开放空间。

### most_transferable_moves_cn

1. 用传统数字渠道（手机）作为对照来隔离新技术的独特机制，而不是只与纸张/无技术比较。

2. 区分总效应不显著与间接效应显著，以中介链条解释技术价值。

3. 把两个调节变量分别放在中介模型的不同路径上（一个作用于渠道→专注度，一个作用于专注度→绩效）。

4. 用第一视角视频与行为视频构建多维客观绩效，避免依赖自报绩效。

5. 用替代测量、逐步骤子样本和感知机制问卷保护结果免受测量偶然性影响。

6. 讨论中清晰区分技术主张、边界主张和设计知识。

### resource_intensive_or_nonstandard_parts_cn

1. 与真实航空公司建立长期合作并获得现场准入。

2. 在真实机场对61名机务开展三轮为期一个月以上的现场实验。

3. 部署可录制第一视角视频的AR眼镜并定制镜片；同时训练YOLOv5目标识别模型。

4. 用两名编码员对大量视频进行人工编码并检验信度。

5. 该任务（飞机过站检查）本身具有高安全标准和高错误记录基础，一般场景难以直接复制。

### what_not_to_copy_superficially_cn

1. 不要只在讨论中声称“AR减少注意力切换”而没有眼动或神经影像证据。

2. 不要直接把“AR提高专注度”说成“AR提高所有绩效”，需要报告总效应不显著和边界条件。

3. 不要在没有完整2×2设计的情况下声称两个调节变量完全独立。

4. 不要忽略低依赖高复杂度组合缺失造成的推论限制。

5. 不要把步骤级溢出到专注度而绩效不溢出当作AR全面溢出。

- single_best_description_of_the_routine_cn：以真实高风险任务为舞台，用传统数字渠道作对照隔离新技术机制，把理论机制放在中介模型的不同路径上，通过多源视频测量和层层稳健性检验，把一次现场实验升华为可复用的边界性设计知识。

## 分析边界

源文件包含正文与附录，但部分图片和表格以OCR/附件形式存在，无法完全核对图像细节；对步骤5/6的例外解释依赖作者文字；整体分析基于单篇文章，未对同主题文献做交叉验证。
