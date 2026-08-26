# Mobile health: A carrot and stick intervention to improve medication adherence

- 作者：Xinying Liu; Upkar Varshney
- 年份 / 期刊：2020 / Decision Support Systems
- DOI：10.1016/j.dss.2019.113165
- 源文件：10128_2020_mobile-health-a-carrot-and-stick-intervention-to-improve-medication-adherence.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.78

## 文章级论证概况

- 核心问题：如何设计一种基于移动健康的“胡萝卜加大棒”（Carrot & Stick, C&S）复合干预，通过正强化、负强化、目标设定与社会联接，改善慢性病患者的有意和无意用药不依从，并通过解析建模验证其有效性和经济性？

- 制品与设计：C&S移动健康干预App：用药提醒与两个安全服药时间窗；按时在第一时间窗服药获得完整PR，第二时间窗服药获得部分PR；当MAR低于期望值或连续漏服指定次数时，阻断患者最常用的手机App（NR），并可随后续服药逐步解除阻断；支持目标设定、社会信息分享、智能监测、服药记录与医护人员报告；还支持平均MAR和多药物不同权重MAR两种情况。

- 客观结果：解析模型显示：无干预时即使基础服药概率为0.8，达到期望MAR的概率仍不足60%；加入提醒和PR后可显著提升至85%以上甚至接近100%；固定PR在高第一时间窗概率、低第二时间窗概率时有效性最高（0.99）；递增PR需持续调整才能抵消边际效用递减；NR能在PR之外进一步降低达到高期望MAR所需的行为要求；即使住院率仅有小幅下降，也能产生显著的医疗费用节省。

- 核心贡献：作者声称首次在用药依从干预中利用负强化设计；首次基于理论将患者分类到十个应用场景，并提供技术与行为干预配套；以三个研究问题分别回应m-health干预文献中缺乏理论支撑、缺乏经济分析、缺乏长期可靠证据的缺口。

- 整篇论证链：文章先以慢病用药不依从的普遍性、后果与经济负担建立现实紧迫性；随后用四组因素和现有干预证据说明已有m-health干预多集中在提醒、教育、自我监测，理论根基薄弱、少有长期与经济评价，且几乎没有处理有意不依从。作者选择Social Cognitive Theory、Goal-setting Theory、Social Exchange Theory以及智能手机依赖现象作为知识基础，提出C&S：用PR奖励按时服药，用阻断常用App的NR惩罚不依从，并加入目标设定和社会连接。经过设计科学迭代得到六项系统需求与五步系统流程，再从三个场景段生成十个可配置场景并按退出概率、适用患者类型、成本效果做定性比较。然后建立概率解析模型，将无干预、提醒+PR、NR触发、固定与递增PR、社会联接、目标设定、经济节省纳入统一形式化框架，并用数值结果说明各组件及组合的贡献。最后将结果重新连接到引言缺口，宣称首次引入NR、第一项理论支撑的复合干预、十场景决策支持，同时承认缺少实证数据并给出未来方向。

## 类型与写作弧线判定

- 论文主类型判定：文章明确使用设计科学方法，先由理论和经验观察导出需求，再构建C&S制品，用场景应用和解析建模评价，最后形成关于干预设计的可复用知识；没有现场实验、benchmark或行为实验，因此不属于theory_derived_artifact_experiment或computational_artifact_benchmark。

- 主导写作弧线判定：写作主线是：先建立用药不依从问题和现有干预缺口，再引入三组理论作为设计基础，接着描述制品设计和十场景，然后用解析模型检验效果和经济性，最后在结论中把结果返回理论贡献和研究缺口，整体呈“问题—理论—设计—检验—回到理论”的循环。

## 研究开展程序

- study_or_phase_count：5

- 研究阶段总序列：第一阶段以文献综述和理论整合识别缺口；第二阶段将理论和经验观察翻译为六项需求和C&S制品；第三阶段从理论生成十个场景组件并做定性比较，以支撑患者分型；第四阶段建立概率解析模型，把干预机制形式化；第五阶段用数值算例和节省测算评价各组件与组合效果。各阶段依次回答“为什么要做—做什么—对谁做—如何证明—值不值”的问题。

### studies_or_phases

#### 1. 理论背景与文献缺口分析

- order：1

- name_cn：理论背景与文献缺口分析

- question_cn：现有移动健康用药依从干预存在哪些学术缺口？为什么需要新的理论驱动的复合干预？

- inputs_and_setting_cn：检索Web of Science、AIS电子图书馆和IEEE数字图书馆，获取2010年后24项符合标准的实证研究；同时引入SCT、Goal-setting Theory、Social Exchange Theory和行为强化文献。

- designed_or_compared_object_cn：比较现有干预类型（文本提醒、社会支持、移动应用自我管理、家庭监测）及其局限。

- baseline_control_or_counterfactual_cn：无直接对照，主要以文献综述总结的现有干预证据作为基线。

##### objective_metrics

（空）

- analysis_method_cn：系统文献筛选、叙述性综合、理论与实证证据整合。

- main_result_cn：识别出三类主要局限：干预时长不足、NR从未用于医疗干预、干预功能缺乏理论支持；同时发现PR单独使用后停药会下降，PR与NR组合未被研究，并观察到智能手机依赖可作为NR实施基础。

- argumentative_role_cn：建立论文的正当性：既证明MA问题重要，又证明现有研究在理论、经济分析和有意不依从上的缺口。

- remaining_uncertainty_cn：文献综述只是定性的；无法确定何种具体设计能真正解决有意不依从。

- link_to_next_phase_cn：识别出的三个缺口直接引出C&S的系统设计需求，尤其是将NR引入干预。

##### evidence_pointers

1. Section 1.1

2. Section 2.1–2.5

3. Fig. 1

4. Table 1

#### 2. C&S制品设计与系统流程

- order：2

- name_cn：C&S制品设计与系统流程

- question_cn：如何将理论命题和实证观察翻译为具体的移动健康干预制品？

- inputs_and_setting_cn：输入为SCT、Goal-setting Theory、Social Exchange Theory、智能手机依赖现象、已有m-health决策支持系统采纳研究及设计科学方法。

- designed_or_compared_object_cn：设计C&S干预App，包含提醒、PR、NR、目标设定、社会连接、监测、报告等功能。

- baseline_control_or_counterfactual_cn：设计层面没有对照；以“无干预”“仅提醒”“PR-only”“NR-only”作为后续解析评价的对照条件。

##### objective_metrics

（空）

- analysis_method_cn：设计科学迭代：从理论导出需求，构建制品，发现局限，修改后重新评价。

- main_result_cn：形成六项系统需求、五步系统流程、双时间窗机制、PR发放规则、NR触发与解除规则、极端阻断规则以及单药/多药MAR计算逻辑。

- argumentative_role_cn：将抽象的强化理论转化为可操作的干预机制，使后续解析建模能够用概率参数刻画设计。

- remaining_uncertainty_cn：设计呈现是纸面上的；尚未回答在何种患者条件下何种组件组合更合适。

- link_to_next_phase_cn：设计完成后需要说明如何针对不同患者类型配置组件，因而进入十场景生成与比较。

##### evidence_pointers

1. Section 3

2. Section 3.1

3. Section 3.2

4. Section 3.3

5. Figs. 2–7

#### 3. 应用场景生成与定性比较

- order：3

- name_cn：应用场景生成与定性比较

- question_cn：不同患者应如何配置C&S的强化、目标设定和社会连接组件？

- inputs_and_setting_cn：以SCT、Goal-setting Theory、个体主义/集体主义文化研究、损失厌恶文献和SPSRQ敏感性框架为输入。

- designed_or_compared_object_cn：三个场景段中的十个场景组件：PR/NR四种组合、自设/医定目标两种、社会信息分享四种方式。

- baseline_control_or_counterfactual_cn：每个场景段内以不同组件作比较，例如固定PR vs 递增PR、有无NR、分享PR vs 分享NR等。

##### objective_metrics

1. 退出概率（定性等级）

2. 适用患者类型（定性判断）

3. 成本效果（高/中/低）

- analysis_method_cn：基于理论机制进行定性场景比较，没有量化数据。

- main_result_cn：递增PR和只分享PR信息会降低退出概率；固定PR+固定NR退出概率最高；NR仅适合对NR敏感度低的患者；分享NR适合需要外部监督的患者；成本随PR递增、NR执行、信息分享量增加而上升。

- argumentative_role_cn：把设计从“一种干预”扩展为“一个可配置干预系统”，为决策支持和个性化提供理论依据。

- remaining_uncertainty_cn：退出概率和成本效果均为定性猜想，缺少实证校准和跨场景比较。

- link_to_next_phase_cn：场景比较给出了定性预期，但要更严格验证干预效果，需要进入解析建模将核心机制形式化。

##### evidence_pointers

1. Section 4.1

2. Section 4.2

3. Section 4.3

4. Tables 2–3

#### 4. 解析模型建立

- order：4

- name_cn：解析模型建立

- question_cn：如何用解析模型形式化表达C&S干预对达到期望MAR概率、NR触发概率和节省的影响？

- inputs_and_setting_cn：输入为概率论和组合数学；假设患者能自行服药、两个NR触发事件独立；使用Feller连续失败概率公式等工具。

- designed_or_compared_object_cn：模型比较无干预基线、提醒+PR、NR条件、固定/递增PR、社会连接、目标设定和节省公式。

- baseline_control_or_counterfactual_cn：以无干预的P_without作为基线，以P_withR表示提醒+PR。

##### objective_metrics

1. 达到期望MAR的概率

2. 第一次NR条件概率

3. 连续漏服NR概率

4. PR累积金额

5. 总节省

- analysis_method_cn：概率解析建模、组合计数、Feller连续游程概率、极值限制函数（如min(...,1)）。

- main_result_cn：得到MAR公式、双时间窗安全约束、无干预/有干预达到期望MAR概率、NR触发概率、固定与递增PR收益、社会联接和目标设定对基础概率的加性影响、节省公式。

- argumentative_role_cn：为设计提供形式化证明基础，使后续数值结果可追溯。

- remaining_uncertainty_cn：模型依赖假设和参数估计，未用真实患者数据校准；社会联接和目标设定只是简单加性函数。

- link_to_next_phase_cn：模型公式建立后，需要代入数值参数查看结果趋势，因此进入结果讨论阶段。

##### evidence_pointers

1. Section 5

2. Section 5.1

3. Section 5.2

4. Table 4

5. Appendix A

#### 5. 数值结果、经济节省与边界讨论

- order：5

- name_cn：数值结果、经济节省与边界讨论

- question_cn：在典型处方参数下，C&S各组件及其组合是否有效？节省是否显著？边界条件是什么？

- inputs_and_setting_cn：数值算例采用30天处方、每天3次、共90剂、期望MAR为80%；PR金额设为第一窗口$1、第二窗口$0.5；NR损失设为$2；递增率δ=0.08；节省测算使用假定的住院成本、系统成本和阻断费用。

- designed_or_compared_object_cn：比较无干预、提醒+固定PR、提醒+递增PR、NR触发、复合干预，以及不同P_st/P_nd/期望MAR/连续漏服阈值对结果的影响。

- baseline_control_or_counterfactual_cn：以P_base的无干预曲线为基线；NR概率计算以P_withR为反事实条件。

##### objective_metrics

1. 达到期望MAR的概率

2. PR总金额

3. NR触发概率

4. 患者/月总节省

- analysis_method_cn：数值参数扫描、表格与曲线比较、敏感性和情景分析。

- main_result_cn：提醒和PR能显著提高达到期望MAR的概率；固定PR表显示最高0.99；递增PR若不持续调整则效果下降；NR触发条件越严格，要求患者维持的P_R越高；复合干预优于任何单一组件；节省最高可达$487/患者/月。

- argumentative_role_cn：完成设计科学的评价闭环：用定量结果说明设计有效、NR有增量贡献、经济性显著且具有参数适应性。

- remaining_uncertainty_cn：所有数值基于假设参数，缺乏真实人群、真实App阻断行为、长期维持和脱落数据。

- link_to_next_phase_cn：结果讨论中的观察列表直接支持结论部分的贡献声明和未来工作。

##### evidence_pointers

1. Section 6.1–6.4

2. Figs. 9–14

3. Tables 5–6

## 各部分修辞架构

### abstract_moves

1. CONTEXT: 用药依从是促进医疗结局的关键，尤其对慢病。

2. GAP: 如何提高并维持所需依从水平仍是重大挑战。

3. DESIGN_FEATURE: 提出C&S复合干预，整合PR、NR、目标设定、社会连接和智能手机依赖。

4. CONTRIBUTION: 首次在干预设计中利用NR，并基于理论对患者分类。

### introduction_moves

1. CONTEXT: 非依从普遍复杂，是医疗实践与患者结局之间的关键中介。

2. PRACTICAL_STAKES: 约半数美国慢病患者不依从，与再住院、发病率和死亡率相关，并造成每年千亿美元负担。

3. PRIOR_KNOWLEDGE: 四组因素导致不依从；已有干预能达80%以上，但复杂且昂贵。

4. PHENOMENON: 智能手机用户对某些App高度依赖甚至接近成瘾。

5. GAP: 现有干预缺长期研究、统计与经济分析、理论检验；多依赖短期小样本。

6. RQ_OR_OBJECTIVE: 提出三个研究问题，分别关于PR/NR如何影响决策、理论基础、有效性与应用场景。

7. METHOD_JUSTIFICATION: 用设计科学方法从理论生成、评价并改进设计。

8. CONTRIBUTION: 首次将NR引入MA干预，并首次基于理论分类患者并开发十场景。

### theory_and_knowledge_moves

1. THEORY_INTRO: SCT认为学习发生于社会环境，强调控制与强化对目标导向行为的维持。

2. THEORY_PROPOSITION: SCT给出三种促进健康行为的途径：信息、外部强化、社会影响。

3. LIMITATION: 以往多数研究只关注单一干预类型，证据不稳健。

4. PRIOR_KNOWLEDGE: PR对多种疾病有效，但停止后依从显著下降；激励值与效果正相关。

5. GAP: PR和NR的组合未在医疗干预中研究，而NR在其他学科比PR更有效。

6. THEORY_INTRO: Goal-setting Theory认为具体目标加反馈优于模糊目标，目标难度与绩效正相关。

7. THEORY_INTRO: Social Exchange Theory的五命题解释行为如何被奖励和代价维持。

8. MECHANISM: 按时服药给PR会促进重复行为；为避免边际效用递减应随时间增加PR。

### artifact_design_moves

1. REQUIREMENT: 从理论和经验观察导出六项系统需求，包括个性化设置、提醒、监测、记录、医护交互、PR/NR。

2. METHOD_JUSTIFICATION: 采用设计科学迭代过程以支撑需求与验证目标。

3. DESIGN_FEATURE: 智能监测通过身上、附近、周围设备自动测量行为。

4. DESIGN_FEATURE: 双时间窗防止因补服导致过量。

5. DESIGN_FEATURE: PR按服药窗口发放，第一窗口全奖励、第二窗口部分奖励。

6. DESIGN_FEATURE: NR在MAR低于期望或连续漏服时阻断常用App，可逐步阻断并逆转。

7. DESIGN_FEATURE: 系统显示阻断信息以区分故意阻断和App故障。

8. DESIGN_FEATURE: 多药物时按平均MAR或不同权重MAR执行PR/NR。

### evaluation_moves

1. STUDY_OVERVIEW: 先描述应用场景，再用解析模型评价。

2. METHOD_JUSTIFICATION: 解析模型可表达复杂变量关系并提供形式证明和中间结果。

3. BENCHMARK_OR_CONTRAST: 以无干预概率、提醒+PR、NR触发和复合干预作为对比链。

4. RESULT: 无干预即使P_base=0.8，达到期望MAR概率仍低于60%；加入提醒和PR后显著改善。

5. RESULT: 固定PR表说明有效性与第一/第二窗口概率组合有关；递增PR需要持续调整。

6. RESULT: 期望MAR越高或连续漏服阈值越小，患者为避免NR所需维持的P_R越高。

7. RESULT: 节省即使在小幅降低住院率时也显著，并随住院成本增加而增大。

### discussion_and_contribution_moves

1. CONTRIBUTION: 创新体现在处理有意不依从、以理论指导设计、开发十场景并考虑成本效果三方面。

2. BOUNDARY_CONDITION: 局限是只用解析模型、未用实证数据；MAR是单一测量；场景仅在段内比较。

3. LIMITATION_AND_FUTURE: 未来可研究多种NR类型、开发面向患者/照护者/医护的DSS、整合其他m-health干预。

## 理论/知识到设计的翻译

### 知识/理论基础

1. Social Cognitive Theory: 强化、社会影响、自我效能对健康行为的作用

2. Goal-setting Theory: 具体、有挑战性目标加反馈提升绩效

3. Social Exchange Theory: 奖励导致行为重复、边际效用递减、情绪反应

4. 智能手机依赖/成瘾现象: 用户对常用App依赖可成为行为约束杠杆

5. 行为经济学损失厌恶: 损失的心理权重约为收益两倍

6. 现有m-health实证证据: 提醒、社会支持、移动应用自我管理有效但存在缺口

- 理论—设计耦合：partial

- 耦合判定理由：理论确实前瞻性地决定了PR、NR、递增PR、目标设定和社会连接等核心设计，尤其Social Exchange Theory直接导出递增PR，SCT导出强化与社会支持的组合；但具体技术实现（Mobile App阻断、双时间窗、提醒机制）主要来自工程经验、患者安全考虑、智能手机依赖现象和已有m-health文献，而非仅由理论推导。因此属于部分耦合。

- 理论到设计翻译链：SCT与Social Exchange Theory提出强化和社会影响改变行为 → 设计需要同时包含PR和NR，并通过递增PR对抗边际效用递减 → 制品采用时间窗奖励和阻断常用App；Goal-setting Theory要求具体目标与反馈 → 制品支持自设或医定MAR目标并提供每日/周/月反馈；社会支持证据和文化差异 → 制品支持可选择的社会信息分享；智能手机依赖 → 制品用阻断常用App作为NR；患者安全考虑 → 制品用双时间窗防止补服过量；最后通过解析模型将上述机制参数化并检验。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：SCT和Social Exchange Theory认为外部强化能促使健康行为重复发生。

- mechanism_cn：按时服药后获得奖励，行为与奖励形成条件联系，重复概率增加。

- design_requirement_cn：系统必须对按时服药行为提供正强化。

- artifact_choice_cn：在第一时间窗服药给完整PR（如1颗星/奖励$1），第二时间窗给部分PR。

- evaluated_contrast_cn：无干预 vs 提醒+固定PR。

- objective_result_cn：加入提醒和PR后，达到期望MAR的概率从<60%升至>85%甚至接近100%。

##### evidence_pointers

1. Section 2.1

2. Section 3.1

3. Section 5.2.4

4. Fig. 9

5. Table 5

#### 2. 2

- theory_or_knowledge_claim_cn：Social Exchange Theory的剥夺-满足命题指出重复奖励的边际效用递减。

- mechanism_cn：如果奖励金额不变化，患者会逐渐失去动机，PR效果随时间下降。

- design_requirement_cn：PR应当随观察期递增，以维持激励强度。

- artifact_choice_cn：递增PR公式RW_I = R_st(1+δ)^(t-1)N_st + R_nd N_nd；场景2和4使用递增PR。

- evaluated_contrast_cn：固定PR vs 递增PR；不同P_st/P_nd下的PR收益曲线。

- objective_result_cn：固定PR在特定P_st/P_nd组合下最高0.99；递增PR若不提高剂量概率则有效性随时间下降，且提高P_st比提高P_nd更有利于奖励累积。

##### evidence_pointers

1. Section 2.3

2. Section 5.2.6

3. Figs. 10–12

#### 3. 3

- theory_or_knowledge_claim_cn：Smartphone依赖和损失厌恶表明，剥夺用户常用事物可比给予奖励更强地改变行为。

- mechanism_cn：当漏服导致App被阻断，患者为重新连接App而调整服药行为，形成负强化。

- design_requirement_cn：系统必须在不依从时移除患者重视的数字资源，并在依从恢复后恢复。

- artifact_choice_cn：MAR低于期望或连续漏服N_m次时阻断最常用App；阻断后服用N剂达标则解除阻断；极端情况阻断除本App外所有App但保留电话短信。

- evaluated_contrast_cn：PR-only情况下需要较高P_R避免NR；加入NR后患者必须达到更高的总体剂量概率。

- objective_result_cn：期望MAR越高、连续漏服阈值越小，患者为避免NR所需的P_R越高；复合干预优于PR-alone或NR-alone。

##### evidence_pointers

1. Section 2.5

2. Section 3.1

3. Section 5.2.5

4. Figs. 13–14

#### 4. 4

- theory_or_knowledge_claim_cn：Goal-setting Theory认为具体且有挑战性的目标配合反馈能提升表现。

- mechanism_cn：设置MAR目标并持续获得反馈，使患者有明确方向和自我激励。

- design_requirement_cn：系统必须允许设置MAR目标并提供目标反馈。

- artifact_choice_cn：参数设置中选定期望MAR；患者可自设或由医生指定；系统提供每日、每周、每月反馈。

- evaluated_contrast_cn：自设目标 vs 医定目标场景；有反馈 vs 无反馈由公式中的M_FG表达。

- objective_result_cn：定性比较认为能准确评估自身能力的患者适合自设目标，否则适合医定目标；模型将目标动机和反馈作为提高基础概率的加性因素。

##### evidence_pointers

1. Section 2.2

2. Section 3.1

3. Section 4.1.2

4. Section 5.2.8

5. Table 3

#### 5. 5

- theory_or_knowledge_claim_cn：SCT和已有实证表明社会支持与社交反馈能改善依从行为。

- mechanism_cn：患者将服药成绩或被惩罚信息分享给他人后，会受到鼓励或监督，从而改变行为。

- design_requirement_cn：系统必须提供可选择的社会连接与信息分享选项。

- artifact_choice_cn：四档社会分享：关闭分享、只分享PR、只分享NR、同时分享PR和NR。

- evaluated_contrast_cn：四种分享方式在退出概率、适用患者类型、成本上的比较。

- objective_result_cn：只分享PR时退出概率低；只分享NR时退出概率高；分享NR适合需要外部督促者；成本随信息分享量增加。

##### evidence_pointers

1. Section 2.1

2. Section 2.4

3. Section 4.1.3

4. Tables 2–3

#### 6. 6

- theory_or_knowledge_claim_cn：用药安全与提醒文献表明，提醒能减少遗忘性漏服，但补服行为可能带来过量风险。

- mechanism_cn：两个时间窗分别界定有效服药窗口和安全间隔，第一窗口提醒后未服再在第二窗口提醒，避免患者自行补服过量。

- design_requirement_cn：系统必须设置两个时间窗并遵守最大/最小剂量间隔。

- artifact_choice_cn：T_max和T_min约束；P_st第一窗口概率，P_nd第二窗口概率；未在第二窗口服药则提示不得补服。

- evaluated_contrast_cn：无提醒 vs 提醒+PR；不同P_st/P_nd组合。

- objective_result_cn：即使P_st仅与P_base相同，低P_nd也能显著提升达到期望MAR概率；P_st对奖励累积影响更大。

##### evidence_pointers

1. Section 1.1

2. Section 3.1

3. Section 5.2.2

4. Fig. 8

5. Table 5

## 评价逻辑

### evaluation_modes

1. 解析证明/形式建模

2. 数值参数扫描

3. 场景内定性比较

4. 经济节省测算

5. 敏感性/边界条件分析

- why_these_evaluations_cn：因为没有真实患者和现场数据，作者选择用解析模型作为设计科学中的形式验证工具：解析模型能同时表达干预机制、中间结果和设计变量关系，使“干预有效”这一主张可以从概率论推导中获得内部一致性；数值算例又让模型结果可读、可比，并展示不同参数条件下的边界；场景定性比较用于处理患者异质性和个性化配置；节省测算用于回应引言中“缺经济分析”的缺口。

- benchmark_and_contrast_chain_cn：评价对照链从最弱基线开始逐级增加组件：无干预P_base → 提醒+固定PR → 提醒+递增PR → NR触发条件 → 社会连接和目标设定（解析式） → 复合干预 → 节省分析。每一步新组件都在前一步基础上说明增量效果，例如NR不是在真空中评价，而是先计算P_withR，再计算NR触发概率；节省则把PR金额、NR损失和住院减少综合在一起。

### claim_evidence_ledger

#### 1. C&S显著提高达到期望MAR的概率。

- claim_cn：C&S显著提高达到期望MAR的概率。

- evidence_cn：解析模型P_withR公式与Fig. 9数值曲线：P_base=0.8无干预时<60%，加提醒和PR后可达85%以上甚至接近100%。

- strength_cn：强形式化支持，但缺少实证数据。

#### 2. 固定PR在不同概率组合下非常有效。

- claim_cn：固定PR在不同概率组合下非常有效。

- evidence_cn：Table 5矩阵显示最高0.99，且高P_st低P_nd时效果更佳。

- strength_cn：强数值支持，但依赖假设参数。

#### 3. 递增PR能对抗边际效用递减。

- claim_cn：递增PR能对抗边际效用递减。

- evidence_cn：Fig. 10–12显示固定与递增PR金额差异，且若患者剂量概率不提升，效果仍会随时间下降。

- strength_cn：中等：直接展示奖励变化趋势，没直接测量患者动机变化。

#### 4. NR能带来额外依从收益。

- claim_cn：NR能带来额外依从收益。

- evidence_cn：Fig. 13–14显示期望MAR越高、连续漏服阈值越小，患者需维持的P_R越高；结论中据此说复合干预优于PR-alone或NR-alone。

- strength_cn：间接证据；没有行为实验证明实际阻断App能让患者改变行为。

#### 5. 干预可产生显著节省。

- claim_cn：干预可产生显著节省。

- evidence_cn：Table 6显示在假设住院成本500、系统成本100/300、月阻断损失2/20条件下，节省约211–487美元/患者/月。

- strength_cn：弱到中等：所有成本参数均为假设值，并非实际测量。

#### 6. 十场景适合不同患者类型。

- claim_cn：十场景适合不同患者类型。

- evidence_cn：Table 3基于理论与推论的定性比较给出退出概率、适用患者和成本效果等级。

- strength_cn：弱：仅为理论推导的分类框架，无实证验证。

- internal_validity_strategy_cn：通过形式化概率模型保证组件之间因果关系在数学上可推导；显式列出假设（自服药能力、NR条件独立）；采用组合计数和Feller连续游程公式减少计算歧义；用渐近表示和边界函数（min(...,1)）限制概率不越界。

- external_validity_strategy_cn：通过多个参数范围（P_st/P_nd、期望MAR、连续漏服次数、成本假设）展示系统行为；用单药/多药、平均MAR/不同MAR、十场景患者分型覆盖不同人群；以可适配性和可逆转阻断设计支撑长期使用主张。

- what_is_not_actually_tested_cn：没有真实患者实验、田野部署或纵向追踪；没有验证“阻断App确实能提高下一次服药概率”；没有测量社会分享、目标设定和医护反馈的实际效果；退出概率和成本效果均为定性或假设参数；没有测试长期新异性维持、App阻断的心理副作用或技术可行性。

## 贡献闭环

- technical_claim_cn：C&S的解析模型显示，在多种参数组合下，复合干预能显著提高达到期望MAR的概率，且经济节省可观。

- artifact_claim_cn：具体设计元素（双时间窗、PR分级、递增PR、NR阻断/解除、多药物MAR设置、社会连接选项）共同构成改进来源，其中NR是新的增量贡献。

- mechanism_claim_cn：机制是正强化增加按时服药行为、负强化通过剥夺常用App促进行为改变、目标设定与反馈提高自我调节、社会分享提供外部监督和支持。

- boundary_claim_cn：该干预主要面向慢病成人患者，适用于有意和无意不依从；依赖患者对智能手机App的依赖程度；NR只应在患者主动选择且对NR敏感度较低时使用；期望MAR越高、连续漏服限制越严时，患者需要维持的总体服药概率越高。

- reusable_design_knowledge_cn：可在m-health干预中把强化理论转化为可配置参数；用递增PR对抗激励衰减；用阻断/解除常用数字服务实现NR；用双时间窗平衡安全与提醒；用场景段支持患者分型与个性化决策。

- theoretical_contribution_cn：首次将NR引入用药依从干预设计；将Social Exchange Theory的奖励重复与边际效用递减命题操作化为PR规则；将SCT、Goal-setting Theory和Social Exchange Theory整合到同一个人机干预框架；并首次基于理论对患者进行分类。

- how_discussion_closes_intro_gap_cn：结论部分明确回顾三个研究问题：PR/NR通过影响服药决策改善MA；理论基因为SCT、GST、SET；应用场景十种且有效性与节省被解析模型支持。三点创新直接对应引言中的“缺理论检验、缺经济分析、缺长期可靠证据”缺口。

- overclaim_or_unsupported_leaps_cn：作者称“结果显示复合干预可在操作环境中维持有效性”依据的是模型适应性，而非真实操作环境；称“NR导致更好MA”来自概率模型推断，不是实际行为因果；将“首次使用NR”等同于贡献时没有充分讨论NR的伦理与可行性；成本节省和场景退出概率建立在大量假设之上，却以结论性语气表达。

## 句级写作动作图谱

### 1. 第一句

- order：1

- section：Abstract

- locator：第一句

- move_code：CONTEXT

- paraphrase_cn：用药依从是促进医疗结局的关键，尤其对慢性疾病。

- rhetorical_function_cn：一开始就把问题领域锁定在慢病用药依从。

- depends_on_cn：无

- sets_up_cn：为后续说明非依从挑战作铺垫。

- evidence_pointer：Abstract P1

### 2. 第二句

- order：2

- section：Abstract

- locator：第二句

- move_code：GAP

- paraphrase_cn：由于多种因素，如何提高并维持所需依从水平仍面临重大挑战。

- rhetorical_function_cn：提出尚未解决的核心问题。

- depends_on_cn：依从的重要性已建立。

- sets_up_cn：引出需要新干预设计。

- evidence_pointer：Abstract P1

### 3. 第三句

- order：3

- section：Abstract

- locator：第三句

- move_code：DESIGN_FEATURE

- paraphrase_cn：提出名为Carrot and Stick的移动健康干预，结合正负强化、目标设定和社会连接。

- rhetorical_function_cn：预告核心制品和设计关键词。

- depends_on_cn：挑战的具体性。

- sets_up_cn：后文的理论和设计部分展开。

- evidence_pointer：Abstract P2

### 4. 最后的贡献句

- order：4

- section：Abstract

- locator：最后的贡献句

- move_code：CONTRIBUTION

- paraphrase_cn：宣称首次在干预设计中利用NR提升MA，并按理论对患者分类。

- rhetorical_function_cn：在摘要中直接声明新颖性。

- depends_on_cn：设计已预先介绍。

- sets_up_cn：为正文贡献声明提供提纲。

- evidence_pointer：Abstract P4

### 5. Section 1.1 起始句

- order：5

- section：Introduction

- locator：Section 1.1 起始句

- move_code：CONTEXT

- paraphrase_cn：用药不依从对慢病患者是一个长期存在的复杂问题。

- rhetorical_function_cn：从临床现象进入宏观背景。

- depends_on_cn：无

- sets_up_cn：为后续数据证据提供上下文。

- evidence_pointer：Introduction P1 S1

### 6. Section 1.1 统计证据句

- order：6

- section：Introduction

- locator：Section 1.1 统计证据句

- move_code：PRACTICAL_STAKES

- paraphrase_cn：约半数美国慢病患者不依从，依从与再住院、发病和死亡密切相关，并造成每年约1000亿美元的负担。

- rhetorical_function_cn：用数量和金额把问题变成现实代价。

- depends_on_cn：非依从是重要问题的判断。

- sets_up_cn：证明解决该问题具有经济和社会意义。

- evidence_pointer：Introduction P1 S2–S4

### 7. Section 1.1 因素句

- order：7

- section：Introduction

- locator：Section 1.1 因素句

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：四组因素导致不依从：剂量频率与排程、健康素养、人口与信念动机、缺乏社会支持。

- rhetorical_function_cn：建立问题成因结构。

- depends_on_cn：非依从的现实重要性。

- sets_up_cn：为干预必须覆盖多种因素作铺垫。

- evidence_pointer：Introduction P1 S5

### 8. Section 1.1 后段

- order：8

- section：Introduction

- locator：Section 1.1 后段

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：m-health可提供不受时空限制的医疗服务，常见干预包括提醒、教育信息和自我监测。

- rhetorical_function_cn：引入研究载体与已有干预类型。

- depends_on_cn：慢病问题背景。

- sets_up_cn：对比现有干预局限。

- evidence_pointer：Introduction P2

### 9. Section 1.2 首句

- order：9

- section：Introduction

- locator：Section 1.2 首句

- move_code：GAP

- paraphrase_cn：现有干预缺少长期研究、统计与经济分析，以及理论基础的检验。

- rhetorical_function_cn：明确学术缺口。

- depends_on_cn：已有干预综述。

- sets_up_cn：为三个研究问题提供方向。

- evidence_pointer：Section 1.2 P1 S1

### 10. Section 1.2 智能手机依赖句

- order：10

- section：Introduction

- locator：Section 1.2 智能手机依赖句

- move_code：PHENOMENON

- paraphrase_cn：智能手机用户对Facebook、Twitter和游戏等App高度依赖，甚至近乎上瘾。

- rhetorical_function_cn：引入可利用的行为现象。

- depends_on_cn：已有干预局限。

- sets_up_cn：支撑用阻断App作为NR。

- evidence_pointer：Section 1.2 P1 S2

### 11. Section 1.2 研究问题句

- order：11

- section：Introduction

- locator：Section 1.2 研究问题句

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：提出研究问题：正负强化如何通过影响患者决策改善MA，理论基础是什么，干预的有效性和决策支持应用场景是什么。

- rhetorical_function_cn：把缺口转化为可回答的问题。

- depends_on_cn：缺口和现象。

- sets_up_cn：组织整篇论文结构。

- evidence_pointer：Section 1.2 P1 S4–S5

### 12. Section 1.2 设计科学句

- order：12

- section：Introduction

- locator：Section 1.2 设计科学句

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：遵循设计科学方法，用理论生成、评价和改进C&S设计。

- rhetorical_function_cn：交代研究方法范式。

- depends_on_cn：研究问题提出。

- sets_up_cn：后文的设计与评价安排。

- evidence_pointer：Section 1.2 P2 S1

### 13. Section 1.2 贡献句

- order：13

- section：Introduction

- locator：Section 1.2 贡献句

- move_code：CONTRIBUTION

- paraphrase_cn：贡献是建立理论根基，首次使用NR，并开发针对不同患者类型的十种场景。

- rhetorical_function_cn：声明两项核心贡献。

- depends_on_cn：研究问题与设计科学方法。

- sets_up_cn：为讨论和结论的贡献声明提供依据。

- evidence_pointer：Section 1.2 P2 S2–S4

### 14. Section 1.3

- order：14

- section：Introduction

- locator：Section 1.3

- move_code：STUDY_OVERVIEW

- paraphrase_cn：预告论文组织：先理论背景，再设计和操作，随后场景和解析评价，最后结论。

- rhetorical_function_cn：给读者路线图。

- depends_on_cn：研究问题和贡献。

- sets_up_cn：引导后续章节阅读。

- evidence_pointer：Section 1.3

### 15. Section 2.1 第一段

- order：15

- section：Theoretical background

- locator：Section 2.1 第一段

- move_code：THEORY_INTRO

- paraphrase_cn：社会认知理论认为学习发生在社会情境中，通过人、环境、行为动态互动，并通过控制与强化维持目标导向行为。

- rhetorical_function_cn：引入第一个理论支柱。

- depends_on_cn：研究问题需要理论支撑。

- sets_up_cn：为强化、社会支持和自我效能组件提供依据。

- evidence_pointer：Section 2.1 P1

### 16. Section 2.1 SCT健康促进方式

- order：16

- section：Theoretical background

- locator：Section 2.1 SCT健康促进方式

- move_code：THEORY_PROPOSITION

- paraphrase_cn：SCT提出通过告知健康风险与收益、用外部强化奖励健康行为、在社会影响网络中促成个人改变三种途径促进健康行为。

- rhetorical_function_cn：把抽象理论变为可操作的干预策略来源。

- depends_on_cn：SCT核心构念。

- sets_up_cn：直接支持PR、NR和社会连接三类设计功能。

- evidence_pointer：Section 2.1 P2

### 17. Section 2.1 干预分类句

- order：17

- section：Theoretical background

- locator：Section 2.1 干预分类句

- move_code：LIMITATION

- paraphrase_cn：多数研究只检验单一干预类型，且证据不够清晰稳健。

- rhetorical_function_cn：指出理论与实证结合中的缺口。

- depends_on_cn：已总结干预分类。

- sets_up_cn：说明需要复合干预。

- evidence_pointer：Section 2.1 P3

### 18. Section 2.1 PR文献综述

- order：18

- section：Theoretical background

- locator：Section 2.1 PR文献综述

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：PR对结核、HIV、阿片成瘾等患者有效，激励值越高效果越大，但停止激励后依从显著下降。

- rhetorical_function_cn：总结PR的已有证据和弱点。

- depends_on_cn：PR作为强化手段的概念。

- sets_up_cn：引出需要NR和递增PR。

- evidence_pointer：Section 2.1 P4

### 19. Section 2.1 末尾句

- order：19

- section：Theoretical background

- locator：Section 2.1 末尾句

- move_code：GAP

- paraphrase_cn：PR与NR组合在医疗干预中未被研究，而教育学和犯罪学证据显示NR比PR更能改变行为。

- rhetorical_function_cn：直接形成论文的核心缺口。

- depends_on_cn：PR证据和NR跨学科证据。

- sets_up_cn：支持C&S引入NR。

- evidence_pointer：Section 2.1 P4 S4

### 20. Section 2.2 首句

- order：20

- section：Theoretical background

- locator：Section 2.2 首句

- move_code：THEORY_INTRO

- paraphrase_cn：目标设定理论认为具体目标加绩效反馈优于没有目标或模糊目标。

- rhetorical_function_cn：引入第二个理论支柱。

- depends_on_cn：前面SCT已识别出目标因素。

- sets_up_cn：系统设计中的MAR目标设置。

- evidence_pointer：Section 2.2 P1

### 21. Section 2.2 目标来源讨论

- order：21

- section：Theoretical background

- locator：Section 2.2 目标来源讨论

- move_code：REQUIREMENT

- paraphrase_cn：自设目标和医定目标各有优劣：自设可能太易或太难，医定可能不了解患者困难；某些患者对自设目标更投入。

- rhetorical_function_cn：把目标设定理论转成设计选择依据。

- depends_on_cn：Goal-setting Theory命题。

- sets_up_cn：场景5和6的患者分型。

- evidence_pointer：Section 2.2 P2

### 22. Section 2.3 Homans命题

- order：22

- section：Theoretical background

- locator：Section 2.3 Homans命题

- move_code：THEORY_INTRO

- paraphrase_cn：社会交换理论通过成功命题、刺激命题、价值命题、剥夺-满足命题和情绪命题解释社会行为。

- rhetorical_function_cn：引入第三个理论支柱，并为奖励设计提供微观机制。

- depends_on_cn：需要解释为什么会重复服药行为。

- sets_up_cn：推导出递增PR需求。

- evidence_pointer：Section 2.3 P2

### 23. Section 2.3 PR设计推论

- order：23

- section：Theoretical background

- locator：Section 2.3 PR设计推论

- move_code：MECHANISM

- paraphrase_cn：如果每次按时服药都给PR，患者会重复该行为；为避免边际效用递减，最合适的方式是随时间提供递增PR。

- rhetorical_function_cn：把社会交换命题转成具体设计规则。

- depends_on_cn：Homans五命题。

- sets_up_cn：支撑场景1–4中的递增PR选项。

- evidence_pointer：Section 2.3 P3

### 24. Section 2.4 检索方法

- order：24

- section：Theoretical background

- locator：Section 2.4 检索方法

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：对三个电子数据库进行检索，设置成人慢病患者、移动干预、定量效果等纳入标准，排除只设计或心理/军队/住院患者。

- rhetorical_function_cn：说明文献综述的系统性，增加后续缺口判断可信度。

- depends_on_cn：需要把握现有干预全景。

- sets_up_cn：为归纳限制条件提供证据基础。

- evidence_pointer：Section 2.4 P1–P2, Fig. 1

### 25. Section 2.5 限制句

- order：25

- section：Theoretical background

- locator：Section 2.5 限制句

- move_code：LIMITATION

- paraphrase_cn：现有干预局限是：时长不够、NR从未用于医疗干预、功能缺乏理论支持。

- rhetorical_function_cn：把文献证据浓缩为三点缺口。

- depends_on_cn：文献综述结果。

- sets_up_cn：明确C&S要填补的空白。

- evidence_pointer：Section 2.5 P1

### 26. Section 2.5 依赖App句

- order：26

- section：Theoretical background

- locator：Section 2.5 依赖App句

- move_code：DESIGN_FEATURE

- paraphrase_cn：利用对特定手机App的依赖实施NR，让非依从行为与App断连之间建立因果关系。

- rhetorical_function_cn：把智能手机依赖现象转化为干预设计。

- depends_on_cn：缺口和依赖现象。

- sets_up_cn：系统设计中的阻断机制。

- evidence_pointer：Section 2.5 P2

### 27. Section 3 需求句

- order：27

- section：System design

- locator：Section 3 需求句

- move_code：REQUIREMENT

- paraphrase_cn：从理论、经验和设计科学导出六项需求：个性化目标强化与社交连接、提醒、监测、记录报告、医护交互、执行PR/NR。

- rhetorical_function_cn：把前期理论与实证工作转化为系统需求。

- depends_on_cn：SCT、GST、SET和文献缺口。

- sets_up_cn：后文系统流程逐项实现。

- evidence_pointer：Section 3 P2

### 28. Section 3 迭代方法句

- order：28

- section：System design

- locator：Section 3 迭代方法句

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：按照设计科学迭代，构建制品、评价有效性、识别局限、修改并重复，直到满足性能目标。

- rhetorical_function_cn：说明设计生成的过程具有方法论保证。

- depends_on_cn：设计科学方法。

- sets_up_cn：为后文评价与改进建立合法性。

- evidence_pointer：Section 3 P1–P2

### 29. Section 3 监测句

- order：29

- section：System design

- locator：Section 3 监测句

- move_code：DESIGN_FEATURE

- paraphrase_cn：智能监测可自动长期测量患者行为，不打扰生活，且比自报数据更准确。

- rhetorical_function_cn：为系统补充数据质量支撑。

- depends_on_cn：系统需求中的监测需求。

- sets_up_cn：为医护人员报告功能作准备。

- evidence_pointer：Section 3 P3

### 30. Section 3.1 第一至第三段

- order：30

- section：System design

- locator：Section 3.1 第一至第三段

- move_code：DESIGN_FEATURE

- paraphrase_cn：系统流程包含五步：设置MAR/PR类型/NR参数；设置两个时间窗；按MAR和连续漏服条件实施NR；极端时阻断除本App外所有App但保留通话与短信；向医护人员提供各周期依从数据。

- rhetorical_function_cn：完整勾勒系统操作流程。

- depends_on_cn：六项需求。

- sets_up_cn：解析模型中各参数定义。

- evidence_pointer：Section 3.1, Fig. 2

### 31. Section 3.1 时间窗设计句

- order：31

- section：System design

- locator：Section 3.1 时间窗设计句

- move_code：DESIGN_FEATURE

- paraphrase_cn：两个时间窗分别界定药物有效服用期间和不干扰下一剂效果的安全间隔，防止患者因补服而过量。

- rhetorical_function_cn：引入患者安全机制，回应故意/非故意补服问题。

- depends_on_cn：提醒功能和用药安全知识。

- sets_up_cn：解析模型中的Tmax/Tmin约束。

- evidence_pointer：Section 3.1 P3, Fig. 8

### 32. Section 3.1 PR规则句

- order：32

- section：System design

- locator：Section 3.1 PR规则句

- move_code：DESIGN_FEATURE

- paraphrase_cn：PR按时间窗发放：第一窗口服药给完整PR，第二窗口服药给减少的PR，未服则无PR。

- rhetorical_function_cn：把强化理论落实到可操作规则。

- depends_on_cn：SCT和Social Exchange Theory。

- sets_up_cn：解析模型中的R_st和R_nd。

- evidence_pointer：Section 3.1 P3, Fig. 3

### 33. Section 3.1 NR条件句

- order：33

- section：System design

- locator：Section 3.1 NR条件句

- move_code：DESIGN_FEATURE

- paraphrase_cn：NR只在患者选择接受后实施，触发条件为MAR低于期望或连续漏服达到阈值；从阻断最常用App开始，可逐步扩展并可逆解除。

- rhetorical_function_cn：说明负强化的实施细节和伦理边界。

- depends_on_cn：智能手机依赖和NR设计。

- sets_up_cn：解析模型中P_NR1和P_NR2。

- evidence_pointer：Section 3.1 P4, Fig. 2

### 34. Section 3.1 极端行为句

- order：34

- section：System design

- locator：Section 3.1 极端行为句

- move_code：DESIGN_FEATURE

- paraphrase_cn：如果患者行为达到极限，将阻断除本App外的所有App，但仍保留家人、朋友、警察和医护人员的电话短信。

- rhetorical_function_cn：定义NR的极限强度，保证安全连接。

- depends_on_cn：NR触发条件。

- sets_up_cn：场景中的退出概率讨论。

- evidence_pointer：Section 3.1 P5

### 35. Section 3.3 多药物句

- order：35

- section：System design

- locator：Section 3.3 多药物句

- move_code：DESIGN_FEATURE

- paraphrase_cn：多药物时可按平均MAR实施PR/NR，或按不同药物权重设置不同PR，更高MAR药物更容易触发NR。

- rhetorical_function_cn：扩展系统适应复杂用药人群。

- depends_on_cn：单药系统流程。

- sets_up_cn：场景4.3中的多药物比较。

- evidence_pointer：Section 3.3, Figs. 6–7

### 36. Section 4 开头

- order：36

- section：Scenarios

- locator：Section 4 开头

- move_code：THEORY_INTRO

- paraphrase_cn：基于SCT，强化、目标设定和社会支持是改变和维持行为的关键，因此把三功能整合进干预并讨论十个场景组件。

- rhetorical_function_cn：从理论回到设计场景，说明场景分类的理论来源。

- depends_on_cn：三组理论。

- sets_up_cn：十场景的比较。

- evidence_pointer：Section 4 P1

### 37. Section 4.1.1 PR/NR段

- order：37

- section：Scenarios

- locator：Section 4.1.1 PR/NR段

- move_code：MECHANISM

- paraphrase_cn：PR能提高依从但重复PR会出现边际效用递减；个体对PR和NR的敏感度不同；损失厌恶使人们规避损失，因此需要多种NR。

- rhetorical_function_cn：解释为什么需要递增PR和多种NR组合。

- depends_on_cn：Social Exchange Theory和损失厌恶。

- sets_up_cn：场景1–4的患者分型。

- evidence_pointer：Section 4.1.1

### 38. Section 4.1.2 目标设定段

- order：38

- section：Scenarios

- locator：Section 4.1.2 目标设定段

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：能准确评估自身能力和困难的患者适合自设目标；只能设最低目标或高估能力的患者适合医定目标。

- rhetorical_function_cn：给出目标设定适用边界。

- depends_on_cn：Goal-setting Theory和患者差异。

- sets_up_cn：场景5和6。

- evidence_pointer：Section 4.1.2

### 39. Section 4.1.3 社会连接段

- order：39

- section：Scenarios

- locator：Section 4.1.3 社会连接段

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：个体主义者和集体主义者对他人意见的敏感度不同；需要鼓励的患者应分享PR信息，需要外部约束的患者应分享NR信息。

- rhetorical_function_cn：将文化差异和个人偏好引入社会连接设计。

- depends_on_cn：社会支持证据和文化研究。

- sets_up_cn：场景7–10。

- evidence_pointer：Section 4.1.3

### 40. Section 4.2.1 退出概率

- order：40

- section：Scenarios

- locator：Section 4.2.1 退出概率

- move_code：RESULT

- paraphrase_cn：递增PR且无NR时退出概率低；固定PR且固定NR时退出概率高；只分享NR信息会增加退出概率。

- rhetorical_function_cn：给出场景在退出概率上的定性排序。

- depends_on_cn：理论机制。

- sets_up_cn：支持推荐哪些场景给哪些患者。

- evidence_pointer：Section 4.2.1, Table 3

### 41. Section 4.2.2 适用患者

- order：41

- section：Scenarios

- locator：Section 4.2.2 适用患者

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：NR应只用于对NR敏感度低的患者；对PR变化敏感的患者应使用递增PR；对外部评价敏感的患者不适合强制分享。

- rhetorical_function_cn：建立患者特征与场景参数匹配规则。

- depends_on_cn：SPSRQ和理论。

- sets_up_cn：个性化决策支持。

- evidence_pointer：Section 4.2.2, Table 3

### 42. Section 4.3 多药物比较

- order：42

- section：Scenarios

- locator：Section 4.3 多药物比较

- move_code：RESULT

- paraphrase_cn：多药物平均MAR与单药类似，但复杂程度可能增加退出概率；不同MAR时高MAR药物会加剧App阻断概率和阻断时长，提高退出风险和系统成本。

- rhetorical_function_cn：扩展场景比较到多药物情况。

- depends_on_cn：Section 3.3多药物设计。

- sets_up_cn：说明该方案的边界条件。

- evidence_pointer：Section 4.3, Figs. 6–7

### 43. Section 4 末尾过渡句

- order：43

- section：Scenarios

- locator：Section 4 末尾过渡句

- move_code：TRANSITION

- paraphrase_cn：本段完成了十个场景组件和单药/多药情况的定性比较，下一节用解析模型评价验证系统。

- rhetorical_function_cn：把场景定性比较连接到定量建模阶段。

- depends_on_cn：十场景比较完成。

- sets_up_cn：第五章解析模型。

- evidence_pointer：Section 4 末句

### 44. Section 5 方法合理性句

- order：44

- section：Analytical modeling

- locator：Section 5 方法合理性句

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：解析模型长期用于计算机科学、设计科学和工程中的形式证明，能表达复杂关系并提供中间和即时结果。

- rhetorical_function_cn：为用解析模型而非实证数据作辩护。

- depends_on_cn：场景定性比较完成。

- sets_up_cn：模型公式的建立。

- evidence_pointer：Section 5 P1

### 45. Section 5 结局变量选择

- order：45

- section：Analytical modeling

- locator：Section 5 结局变量选择

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：选择MAR作为核心结局变量，因为它能代表慢病长期稳定服药行为且是既往研究最常用的测量。

- rhetorical_function_cn：限定模型评价的核心指标，便于与文献可比。

- depends_on_cn：已有MA测量文献。

- sets_up_cn：式(1)和后续概率计算。

- evidence_pointer：Section 5 P2

### 46. Section 5.1 假设

- order：46

- section：Analytical modeling

- locator：Section 5.1 假设

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：模型假设患者能自行服药、两个NR触发事件互相独立，并说明这些假设可放宽。

- rhetorical_function_cn：明确模型适用范围和简化条件。

- depends_on_cn：模型需要可解性。

- sets_up_cn：后文公式推导。

- evidence_pointer：Section 5.1

### 47. Section 5.2.3 无干预概率

- order：47

- section：Analytical modeling

- locator：Section 5.2.3 无干预概率

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：无干预情况下达到期望MAR的概率是患者服用足够剂量概率的累积和。

- rhetorical_function_cn：建立评价基线。

- depends_on_cn：MAR定义和组合概率。

- sets_up_cn：与有干预概率比较。

- evidence_pointer：Section 5.2.3, Eq. (4)

### 48. Section 5.2.4 提醒+PR

- order：48

- section：Analytical modeling

- locator：Section 5.2.4 提醒+PR

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：提醒能改善遗忘性漏服；由于提醒后服药也会获得PR，所以把两者共同建模为P_withR。

- rhetorical_function_cn：把提醒和PR作为第一个对比干预包。

- depends_on_cn：遗忘是漏服主要原因的证据。

- sets_up_cn：后续NR加入的比较。

- evidence_pointer：Section 5.2.4, Eqs. (5)–(6)

### 49. Section 5.2.5 NR概率

- order：49

- section：Analytical modeling

- locator：Section 5.2.5 NR概率

- move_code：DESIGN_FEATURE

- paraphrase_cn：NR触发概率分为MAR低于期望的条件和连续漏服的条件。

- rhetorical_function_cn：把NR机制形式化。

- depends_on_cn：已有P_withR。

- sets_up_cn：Fig. 13–14的数值结果。

- evidence_pointer：Section 5.2.5, Eqs. (7)–(9)

### 50. Section 5.2.6 固定与递增PR

- order：50

- section：Analytical modeling

- locator：Section 5.2.6 固定与递增PR

- move_code：DESIGN_FEATURE

- paraphrase_cn：固定PR等于第一窗口奖励乘以第一窗口次数加第二窗口奖励乘以第二窗口次数；递增PR在此基础上乘以随时间增长的因子。

- rhetorical_function_cn：把场景中的固定/递增PR转成可计算收益。

- depends_on_cn：Social Exchange Theory。

- sets_up_cn：Fig. 10–12的奖励比较。

- evidence_pointer：Section 5.2.6, Eqs. (10)–(11)

### 51. Section 5.2.7–5.2.8

- order：51

- section：Analytical modeling

- locator：Section 5.2.7–5.2.8

- move_code：DESIGN_FEATURE

- paraphrase_cn：社会连接和目标设定分别以分享概率乘以动机因子、目标动机乘以反馈效应作为提高基础服药概率的加性项。

- rhetorical_function_cn：把社会连接和目标设定纳入统一模型。

- depends_on_cn：SCT和Goal-setting Theory。

- sets_up_cn：为复合干预效果提供形式基础。

- evidence_pointer：Section 5.2.7–5.2.8, Eqs. (12)–(13)

### 52. Section 6.1 数值发现

- order：52

- section：Results and discussion

- locator：Section 6.1 数值发现

- move_code：RESULT

- paraphrase_cn：无干预时高P_base也难达期望MAR；加提醒和PR后，即使P_nd较低也能从不足60%提升到85%以上。

- rhetorical_function_cn：证明提醒+PR的核心增益。

- depends_on_cn：无干预基线和P_withR模型。

- sets_up_cn：继续评估固定和递增PR。

- evidence_pointer：Section 6.1, Fig. 9

### 53. Section 6.2 固定PR表

- order：53

- section：Results and discussion

- locator：Section 6.2 固定PR表

- move_code：RESULT

- paraphrase_cn：固定PR在P_st高、P_nd低时达到最高有效性0.99；有效性随P_st下降和P_nd上升而下降。

- rhetorical_function_cn：展示固定PR的适用条件。

- depends_on_cn：Table 5计算结果。

- sets_up_cn：支持递增PR调整需求。

- evidence_pointer：Section 6.2, Table 5

### 54. Section 6.2 递增PR效果

- order：54

- section：Results and discussion

- locator：Section 6.2 递增PR效果

- move_code：RESULT

- paraphrase_cn：递增PR的效果会随时间下降，因为奖励必须增加才能维持同样的P_st和P_nd；且P_st比P_nd更有利于奖励累积。

- rhetorical_function_cn：说明递增PR并非一劳永逸，需要配合行为提升。

- depends_on_cn：RW_I公式和图10–12。

- sets_up_cn：为NR加入提供理由。

- evidence_pointer：Section 6.2, Figs. 10–12

### 55. Section 6.3 NR结果

- order：55

- section：Results and discussion

- locator：Section 6.3 NR结果

- move_code：RESULT

- paraphrase_cn：期望MAR越高，患者需维持的P_R越高才能避免NR；连续漏服限制越严，所需P_R越高。

- rhetorical_function_cn：证明NR在机制上对患者行为提出更高要求。

- depends_on_cn：P_NR1/P_NR2公式。

- sets_up_cn：观察列表中复合干预优于单一干预的结论。

- evidence_pointer：Section 6.3, Figs. 13–14

### 56. Section 6.4 节省表

- order：56

- section：Results and discussion

- locator：Section 6.4 节省表

- move_code：RESULT

- paraphrase_cn：在假设成本参数下，患者每月节省可达211–487美元，即使住院率小幅降低也显著。

- rhetorical_function_cn：回应引言中的经济分析缺口。

- depends_on_cn：节省公式和假设参数。

- sets_up_cn：结论中关于经济价值的声明。

- evidence_pointer：Section 6.4, Table 6

### 57. Section 6 观察列表

- order：57

- section：Results and discussion

- locator：Section 6 观察列表

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：观察列表总结：提醒+PR有效，PR需调整，NR要求更高P_R，复合干预优于单组件，节省显著且随住院成本增加。

- rhetorical_function_cn：把零散数值结果提升为可迁移的设计观察。

- depends_on_cn：全部数值结果。

- sets_up_cn：为结论贡献提供证据。

- evidence_pointer：Section 6 末列表

### 58. Section 7 首段

- order：58

- section：Conclusions

- locator：Section 7 首段

- move_code：CONTRIBUTION

- paraphrase_cn：总结C&S三点创新：处理有意非依从、用理论设计提升可靠性、开发十场景并考虑成本效果。

- rhetorical_function_cn：在结论处重述贡献。

- depends_on_cn：全文设计和评价。

- sets_up_cn：后续局限和未来工作。

- evidence_pointer：Section 7 P1–P2

### 59. Section 7 局限句

- order：59

- section：Conclusions

- locator：Section 7 局限句

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：局限是仅用解析建模没有实证数据、只选MAR一个结局、场景只做段内比较。

- rhetorical_function_cn：保护贡献不被高估，同时指明外部效度边界。

- depends_on_cn：研究方法选择。

- sets_up_cn：未来数据收集和扩展研究。

- evidence_pointer：Section 7 P3

## 写作技术

- gap_construction_cn：先以现实问题铺陈，再用系统文献综述筛出现有干预的三大局限，接着通过“PR单独使用效果会回退”“NR在别的学科更有效”“智能手机依赖可被利用”三个命题把新干预的必要性收紧到“应该引入NR”。整个缺口不断从宏观转向微观，直到明确“PR与NR组合未在医疗干预中研究”。

- signposting_cn：论文在多处给出路标：引言末预告全文结构；Section 2开头声明理论将用于设计并指导场景；Section 3开头说明设计科学迭代；Section 4末尾预告下一节解析建模；Section 5开头解释解析模型的作用。

- transition_logic_cn：每个大节都用自己的末尾句连接到下一节：文献综述末尾用“从理论和文献，需要正负强化干预”过渡到设计；场景末尾用“下一节用解析模型评价”过渡到建模；结果讨论末尾用观察列表过渡到结论。

- claim_evidence_rhythm_cn：几乎每个设计主张后紧跟“为什么”和“怎么验证”：先在理论部分给出命题，再在设计部分转化为具体规则，再在建模部分用公式表达，最后在结果部分用曲线和表呈现。例如NR从理论跨学科证据到阻断App设计再到P_NR公式再到Fig. 13–14。

- benchmark_narrative_cn：没有设置传统benchmark数据集，而是把“无干预”和“仅提醒+PR”作为逐级对照：先证明提醒+PR相对无干预有显著增益，再用NR触发概率说明“要让NR不发生需要多高行为水平”，从而间接证明NR能带来额外约束收益。

- theory_return_cn：结论把数值结果重新包装为理论贡献：不是简单说“模型有效”，而是说“引入了NR、用Social Exchange Theory解释递增PR、用理论分类患者”，使结果回到引言开出的理论缺口。

- contribution_positioning_cn：贡献定位在三个层面：现象层面（首次把NR用于MA干预）、理论层面（reinforcement理论在m-health落地）、应用层面（十场景支持患者分型和成本效果）。

- novelty_protection_cn：用“首次使用NR”“第一次基于理论分类患者”“结合已被验证的提醒和社会连接元素”等措辞把新颖性嵌入设计而非仅依赖性能；同时通过多药物、多参数和场景扩展，使贡献看起来不只是一次性结果。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：用现实问题、统计负担和已有干预局限建立研究缺口。

- research_job_cn：做系统文献综述，总结现有干预类型和证据质量。

- required_evidence_cn：需要足够的流行病学数据和文献支持，证明问题重要且缺口存在。

- transition_to_next_cn：把缺口具体化为研究问题，并预告理论和设计方向。

#### 2. 2

- step：2

- writing_job_cn：引入2–3个核心理论，每个理论对应一个设计支柱。

- research_job_cn：从理论命题中提取可操作的设计启示，而不是只做理论介绍。

- required_evidence_cn：理论命题必须能被后续设计或模型映射，否则视为包装。

- transition_to_next_cn：在理论段末尾用“基于这些，我们设计……”转入系统设计。

#### 3. 3

- step：3

- writing_job_cn：把理论启示写成系统需求，再描述一个具体可操作制品。

- research_job_cn：构建设计解决方案，包括流程、界面、参数和边界情况。

- required_evidence_cn：设计特征需要与理论机制一一对应，并能被评价方案检验。

- transition_to_next_cn：设计完成后说明“为了适应不同患者，我们开发场景……”进入场景或评价。

#### 4. 4

- step：4

- writing_job_cn：设计应用场景或患者分型，使制品看起来可配置而不仅仅是一个原型。

- research_job_cn：用理论生成组件矩阵并做定性比较。

- required_evidence_cn：每个场景需要写明适用患者、推进机制和成本/退出预期。

- transition_to_next_cn：定性比较结束后，用“下面用解析/实验验证”过渡到评价。

#### 5. 5

- step：5

- writing_job_cn：用解析模型、仿真或实验把设计参数和结果变量联系起来。

- research_job_cn：定义结局指标、对照组和参数范围；最好有一个从无干预到复合干预的逐级比较。

- required_evidence_cn：模型或实验必须能区分每个组件的增量贡献。

- transition_to_next_cn：用结果列表总结观察，再进入结论。

#### 6. 6

- step：6

- writing_job_cn：在结论中重述贡献、边界和未来工作。

- research_job_cn：把结果上升到理论或设计知识，并诚实说明验证方法的局限。

- required_evidence_cn：贡献声明必须能在正文找到对应证据；若缺少实证数据则必须明确说明。

- transition_to_next_cn：结束。

### most_transferable_moves_cn

1. 将“现实问题—文献缺口—研究问题—理论支柱—设计需求—制品—场景—评价—贡献”组织成清晰链条。

2. 用“无干预—单一组件—复合干预”的逐级对照逻辑展示增量效果。

3. 在每一节末尾预告下一节，保持论证可追踪。

4. 把理论命题转化为可计算参数（如PR公式、P_NR公式），并用数值表/图支撑。

### resource_intensive_or_nonstandard_parts_cn

1. 智能手机App阻断需要真实移动平台权限、用户隐私和伦理审批，不是每篇论文都能实现。

2. 智能监测数据（身上/近身/周围传感器）需要真实硬件和患者数据采集。

3. 长时期、多场景的患者分型验证需要大规模现场实验，论文只做了解析模拟。

4. 经济节省测算依赖真实住院成本和阻断App的心理损失估计，本文使用的是假设值。

### what_not_to_copy_superficially_cn

1. 不能只在引言贴理论标签而不让理论决定具体设计参数；本文的PR/NR/目标/社会连接都能映射到需求。

2. 不能只宣称“首次使用NR”而不解释负强化的机制、触发条件和可逆性。

3. 不能在没有真实成本数据的情况下声称“节省显著”，除非限定为基于假设的估算。

4. 不能用“概率退出”这类定性等级冒充实证测量，必须注明是理论推导。

- single_best_description_of_the_routine_cn：从临床问题出发，用行为理论把“强化—目标—社会连接”转成可配置的干预制品，再用解析模型把设计参数与达到期望依从的概率、成本和适用患者类型联系起来，最后用场景与灵敏度研究兜住普适性。

## 分析边界

分析完全基于提供的论文文本、公式和图表；未复现模型数值计算，无法验证Table 5/6和Fig. 9–14的具体数值是否完全正确；原文PDF可能缺失部分附录或引用编号（如参考文献[6]、[32]、[59]未见），但不影响主要结构判断。由于论文只有解析评价，本文的“研究阶段”将数值结果与讨论合并，若按更细粒度拆分还可继续增加阶段。
