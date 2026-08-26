# Standardize or Let a Thousand Flowers Bloom? Interface Design Coordination between Software Platforms and Hosted Apps

- 作者：Cheng Zhang; Peijian Song; Kai Lim
- 年份 / 期刊：2023 / MIS Quarterly
- DOI：10.25300/misq/2022/16484
- 源文件：12600_2023_standardize-or-let-a-thousand-flowers-bloom-interface-design-coordination-between-software-platf.md
- 论文主类型：field_intervention_or_platform_experiment
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.9

## 文章级论证概况

- 核心问题：在软件平台生态系统中，app与其宿主平台之间的界面设计协调（集成界面设计）是否以及如何影响平台与app之间的衍生使用？具体而言，界面相似性、嵌入性和同步性是否通过用户的分组感知增强平台到app的前向衍生使用和app到平台的后向衍生使用？

- 制品与设计：作者开发了一个信息类笑话app，部署在微信平台上，操纵了三个界面设计属性（interface similarity, embeddedness, synchrony），形成2×2×2共8个版本。高相似性版本与微信共享字体和背景色，低相似性版本相反；高嵌入性版本在微信内浏览内容，低嵌入性版本跳到外部窗口；高同步性版本立即显示，低同步性版本有5秒等待。

- 客观结果：随机现场实验（541名参与者）显示，三个界面属性都显著增强用户的分组感知（H1-H3支持）；分组感知显著调节平台到app的前向衍生使用（H4支持），但对app到平台的后向衍生使用的调节不显著（H5不支持）。

- 核心贡献：作者声称首次基于理论论证和实证证据，表明平台生态系统中界面设计标准化的必要性；将基本Gestalt理论扩展到平台生态系统并延伸至行为后果；提出'衍生使用'概念以刻画平台与app之间的双向使用关联；为平台所有者提供通过界面设计原则平衡自主与整合的实践指导。

- 整篇论证链：论文从平台实践中'百花齐放'与产品线标准化之间的张力入手，指出平台所有者放任app界面设计可能损害跨产品界面整合价值。为了将这一矛盾转化为可研究问题，作者引入基本Gestalt理论（TBG），将界面设计分解为相似性、嵌入性和同步性三个拓扑属性，并论证它们通过影响用户对平台与app的分组感知，进而影响双向衍生使用。作者开发了一个在微信上运行的实验性app，通过随机现场实验操纵这三个属性，测量真实app使用行为和自报平台使用。结果表明三个属性均增强分组感知，而分组感知确实促进平台到app的前向衍生使用，但对app到平台的后向衍生使用没有显著作用。讨论将这一不对称结果归因于边际效用递减，并据此主张界面设计是平台治理的重要资源，同时承认研究边界为Type 1平台和单一app。

## 类型与写作弧线判定

- 论文主类型判定：文章在真实平台（微信）上部署了由研究者开发的app，随机分配参与者到8个不同界面设计条件，并通过现场观察收集真实使用行为，属于现场干预/平台实验。

- 主导写作弧线判定：全文遵循从问题张力出发→引入理论→由理论导出设计原则→现场检验→返回理论贡献并在讨论中扩展理论的弧线。

## 研究开展程序

- study_or_phase_count：6

- 研究阶段总序列：阶段1建立理论框架和假设；阶段2将理论属性操作化为实验app版本；阶段3通过两阶段现场实验收集数据；阶段4进行数据质量检验；阶段5执行假设检验（ANOVA与SEM）；阶段6对未支持假设进行补充解释并讨论边界。各阶段从理论推演逐步走向实证证据，最后回到理论扩展。

### studies_or_phases

#### 1. 理论建构与假设推导

- order：1

- name_cn：理论建构与假设推导

- question_cn：平台与app的界面设计协调如何产生衍生使用？

- inputs_and_setting_cn：文献（TBG、信任转移、协同特异性、产品线设计等）

- designed_or_compared_object_cn：概念模型中的三个界面属性及两个行为机制

- baseline_control_or_counterfactual_cn：无（文献对比）

##### objective_metrics

（空）

- analysis_method_cn：理论论证

- main_result_cn：提出H1-H5

- argumentative_role_cn：确立研究的理论框架与假设

- remaining_uncertainty_cn：假设是否在真实环境中成立

- link_to_next_phase_cn：需要实证检验，因此设计现场实验

##### evidence_pointers

1. Theory and Hypothesis Development 全文

#### 2. 实验设计与原型开发

- order：2

- name_cn：实验设计与原型开发

- question_cn：如何在微信平台上操纵三个界面属性？

- inputs_and_setting_cn：微信平台、八种实验版本app

- designed_or_compared_object_cn：操纵变量：低/高相似性、低/高嵌入性、低/高同步性

- baseline_control_or_counterfactual_cn：高条件 vs 低条件

##### objective_metrics

1. 操纵检验问题

- analysis_method_cn：软件开发与预实验

- main_result_cn：开发完成8个版本

- argumentative_role_cn：将理论属性操作化

- remaining_uncertainty_cn：参与者是否真的感知到差异

- link_to_next_phase_cn：进行随机分配和数据收集

##### evidence_pointers

1. Field Experiment 段落，Appendix E

#### 3. 现场实验数据收集（两阶段）

- order：3

- name_cn：现场实验数据收集（两阶段）

- question_cn：收集分组感知和真实使用行为

- inputs_and_setting_cn：992名招募被试，随机分配8个版本；第一阶段安装+问卷，第二阶段两周内app登录日志+平台使用问卷

- designed_or_compared_object_cn：参与者被随机分配

- baseline_control_or_counterfactual_cn：随机化控制混淆

##### objective_metrics

1. app使用次数

2. app使用时长

3. 平台使用意图量表

4. 分组感知量表

- analysis_method_cn：现场实验

- main_result_cn：541名有效受访者，完整数据

- argumentative_role_cn：提供实证数据

- remaining_uncertainty_cn：平台使用数据是自我报告，可能存在共同方法偏差

- link_to_next_phase_cn：数据质量检验

##### evidence_pointers

1. Field Experiment – Procedure 段落，Figure F1

#### 4. 数据质量检验（操纵检验与信效度）

- order：4

- name_cn：数据质量检验（操纵检验与信效度）

- question_cn：操纵是否有效，测量是否可靠？

- inputs_and_setting_cn：问卷数据

- designed_or_compared_object_cn：操纵检验t检验、Cronbach's alpha、EFA

- baseline_control_or_counterfactual_cn：无

##### objective_metrics

1. t检验值

2. p值

3. Cronbach's alpha

4. AVE

5. 因子载荷

- analysis_method_cn：t检验、探索性因子分析

- main_result_cn：操纵有效，信效度良好

- argumentative_role_cn：确保后续统计推断有效

- remaining_uncertainty_cn：无主要剩余不确定

- link_to_next_phase_cn：进入假设检验

##### evidence_pointers

1. Results 第一、二段

#### 5. 假设检验（ANOVA + SEM）

- order：5

- name_cn：假设检验（ANOVA + SEM）

- question_cn：H1-H5是否成立？

- inputs_and_setting_cn：分组感知、app使用行为、平台使用意图

- designed_or_compared_object_cn：ANOVA三个主效应；SEM路径和交互

- baseline_control_or_counterfactual_cn：2×2×2因子设计

##### objective_metrics

1. F值

2. 路径系数

3. 显著性水平

- analysis_method_cn：单因素方差分析、PLS-SEM

- main_result_cn：H1-H3支持，H4支持，H5不支持

- argumentative_role_cn：检验假设

- remaining_uncertainty_cn：H5为何不支持需要解释

- link_to_next_phase_cn：补充解释

##### evidence_pointers

1. Table 1

2. Figure 2

#### 6. 未支持结果的补充解释与稳健性说明

- order：6

- name_cn：未支持结果的补充解释与稳健性说明

- question_cn：为什么分组感知不影响后向衍生使用？

- inputs_and_setting_cn：文献（边际效用递减）

- designed_or_compared_object_cn：理论解释

- baseline_control_or_counterfactual_cn：无

##### objective_metrics

（空）

- analysis_method_cn：理论推断

- main_result_cn：提出边际效用递减解释

- argumentative_role_cn：保护理论模型的完整性，提出适用边界

- remaining_uncertainty_cn：该解释未直接检验

- link_to_next_phase_cn：进入讨论贡献与局限

##### evidence_pointers

1. Results 末段

2. Discussion – Limitations

## 各部分修辞架构

### abstract_moves

1. CONTEXT

2. CONTEXT

3. PRIOR_KNOWLEDGE

4. GAP

5. RQ_OR_OBJECTIVE

6. THEORY_INTRO

7. THEORY_PROPOSITION

8. METHOD_JUSTIFICATION

9. RESULT

10. RESULT

11. CONTRIBUTION

### introduction_moves

1. CONTEXT

2. CONTEXT

3. PRACTICAL_STAKES

4. PRIOR_KNOWLEDGE

5. PRIOR_KNOWLEDGE

6. PRIOR_KNOWLEDGE

7. PHENOMENON

8. LIMITATION

9. RQ_OR_OBJECTIVE

10. THEORY_INTRO

11. DESIGN_FEATURE

12. THEORY_PROPOSITION

13. THEORY_PROPOSITION

14. THEORY_PROPOSITION

15. METHOD_JUSTIFICATION

16. CONTRIBUTION

### theory_and_knowledge_moves

1. CONTEXT

2. PHENOMENON

3. METHOD_JUSTIFICATION

4. MECHANISM

5. LIMITATION

6. GAP

7. THEORY_INTRO

8. MECHANISM

9. THEORY_PROPOSITION

10. HYPOTHESIS_OR_PROPOSITION

11. HYPOTHESIS_OR_PROPOSITION

12. HYPOTHESIS_OR_PROPOSITION

13. THEORY_INTRO

14. THEORY_INTRO

15. HYPOTHESIS_OR_PROPOSITION

16. HYPOTHESIS_OR_PROPOSITION

### artifact_design_moves

1. STUDY_OVERVIEW

2. METHOD_JUSTIFICATION

3. DESIGN_FEATURE

4. DESIGN_FEATURE

5. DESIGN_FEATURE

6. DESIGN_FEATURE

7. METHOD_JUSTIFICATION

8. METHOD_JUSTIFICATION

9. METHOD_JUSTIFICATION

### evaluation_moves

1. RESULT

2. RESULT

3. RESULT

4. RESULT

5. RESULT

6. RESULT

7. ROBUSTNESS_OR_BOUNDARY_TEST

### discussion_and_contribution_moves

1. CONTRIBUTION

2. CONTRIBUTION

3. CONTRIBUTION

4. CONTRIBUTION

5. PRACTICAL_STAKES

6. BOUNDARY_CONDITION

7. BOUNDARY_CONDITION

8. LIMITATION_AND_FUTURE

9. CONTRIBUTION

## 理论/知识到设计的翻译

### 知识/理论基础

1. theory of basic Gestalts (TBG)

2. trust transference

3. synergistic specificity

4. product line literature

5. software platform literature

- 理论—设计耦合：direct

- 耦合判定理由：三个界面设计属性直接由TBG的拓扑性质（相似性、共同区域/包围、共同命运/同步）推导而来，并通过现场实验对每个属性进行了直接操纵；行为机制（信任转移、协同特异性）用于解释分组感知到衍生使用的路径，但未被直接操纵。设计属性的选择是由理论前驱地决定的，而非数据驱动或工程启发。

- 理论到设计翻译链：TBG指出视觉元素因相似、共处同一区域、同步变化而被感知为整体 → 平台与app的界面设计可通过操纵这三个拓扑性质影响用户对二者关系的分组感知 → 设计要求：让app与平台共享视觉属性、让app在平台边界内运行、让app响应快速 → 制品选择：在微信app中设置相同字体/背景色、在微信内嵌入界面、立即显示内容 → 对照差异：高相似vs低相似、高嵌入vs低嵌入、高同步vs低同步 → 客观结果：三个主效应显著，分组感知增强 → 进一步通过信任转移和协同特异性机制预测分组感知对双向衍生使用的影响 → 结果显示分组感知只增强前向衍生使用

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：视觉上相似的物体被感知为一组（相似性原理）

- mechanism_cn：视觉分组：相似性产生突生特征，使用户将平台与app视为一体

- design_requirement_cn：app与平台在界面视觉属性上保持一致

- artifact_choice_cn：高相似版本：字体和背景色与微信相同；低相似版本：对比突出

- evaluated_contrast_cn：高相似 vs 低相似

- objective_result_cn：F=23.307, p<0.01，支持H1

##### evidence_pointers

1. Table 1

2. Field Experiment design section

#### 2. 2

- theory_or_knowledge_claim_cn：处于同一包围区域内的元素被感知为一组（共同区域/包围性）

- mechanism_cn：空间包含关系：app在平台边界内运行产生'在一起'感知

- design_requirement_cn：app在激活后保持在平台界面边界内

- artifact_choice_cn：高嵌入：在微信内浏览内容；低嵌入：跳到外部窗口

- evaluated_contrast_cn：高嵌入 vs 低嵌入

- objective_result_cn：F=14.122, p<0.01，支持H2

##### evidence_pointers

1. Table 1

#### 3. 3

- theory_or_knowledge_claim_cn：同时变化的元素被感知为一组（共同命运/同步性）

- mechanism_cn：时间同时性：用户激活平台动作与app响应在时间上紧密连接，产生因果关联感知

- design_requirement_cn：app应在用户操作后立即响应

- artifact_choice_cn：高同步：立即显示；低同步：等待5秒

- evaluated_contrast_cn：高同步 vs 低同步

- objective_result_cn：F=6.239, p<0.05，支持H3

##### evidence_pointers

1. Table 1

#### 4. 4

- theory_or_knowledge_claim_cn：信任可以从一个已知对象转移到相关的新对象（信任转移）

- mechanism_cn：用户将平台信任转给app，强化平台→app使用行为

- design_requirement_cn：通过设计增强分组感知，使app被感知为平台一部分

- artifact_choice_cn：（通过三个设计属性实现）

- evaluated_contrast_cn：分组感知的高低（由三个属性操纵产生）

- objective_result_cn：分组感知与平台使用交互项系数0.365, p<0.01，H4支持

##### evidence_pointers

1. Figure 2

2. SEM results

#### 5. 5

- theory_or_knowledge_claim_cn：当组件能够协同工作时，系统整体效用提高（协同特异性）

- mechanism_cn：用户将app的良好评价归因于平台，增强app→平台使用

- design_requirement_cn：通过设计增强分组感知，使app与平台被视为一个系统

- artifact_choice_cn：（通过三个设计属性实现）

- evaluated_contrast_cn：分组感知对后向衍生使用的调节

- objective_result_cn：交互项系数0.041, p>0.1，H5不支持

##### evidence_pointers

1. Figure 2

## 评价逻辑

### evaluation_modes

1. 随机对照现场实验（2×2×2因子设计）

2. 操纵检验（t检验）

3. 信度效度分析（Cronbach's alpha, EFA, AVE）

4. 单变量方差分析（ANOVA）检验主效应

5. PLS-SEM检验路径与调节效应

6. 无响应偏差检验

- why_these_evaluations_cn：作者需要分别验证设计属性对中间机制（分组感知）的作用，以及分组感知对行为结果（两种衍生使用）的作用。操纵检验确保参与者确实感知到了设计差异，ANOVA用来检验三个属性对分组感知的主效应，SEM用来检验分组感知对使用行为的调节和路径，同时排除无响应偏差以确保样本代表性。

- benchmark_and_contrast_chain_cn：实验通过8个版本的app在两两之间对比高/低相似、高/低嵌入、高/低同步；ANOVA主效应处理各属性独立贡献；SEM中通过交互项检验分组感知的调节作用，并通过路径系数确认前向和后向衍生使用的存在。这一链条从操纵有效性逐步渐进到假设检验。

### claim_evidence_ledger

#### 1. 三个界面属性增强分组感知

- claim_cn：三个界面属性增强分组感知

- evidence_cn：ANOVA主效应显著（表1）

#### 2. 分组感知增强平台到app前向衍生使用

- claim_cn：分组感知增强平台到app前向衍生使用

- evidence_cn：SEM交互项0.365显著（图2）

#### 3. 分组感知增强app到平台后向衍生使用

- claim_cn：分组感知增强app到平台后向衍生使用

- evidence_cn：不显著，未支持

#### 4. 平台使用显著预测app使用，app使用显著预测平台使用

- claim_cn：平台使用显著预测app使用，app使用显著预测平台使用

- evidence_cn：路径系数0.264和0.361，p<0.01（图2）

#### 5. 操纵有效

- claim_cn：操纵有效

- evidence_cn：操纵检验t值显著

#### 6. 测量有效

- claim_cn：测量有效

- evidence_cn：alpha>0.9, AVE>0.5

- internal_validity_strategy_cn：随机分配8个版本给参与者，控制个体差异；测量时间前后分离（T0平台使用→T1-T2 app使用→T2平台使用）以支持因果方向；操纵检验确保干预生效；统计检验控制人口学和平台经验等协变量。

- external_validity_strategy_cn：在真实微信平台上部署真实可用的app，参与者按正常方式安装和使用，收集真实登录行为；但平台使用为自我报告。作者同时声明边界为Type 1平台，研究范围限制在单一app，避免过度推广。

- what_is_not_actually_tested_cn：信任转移和协同特异性作为解释双向衍生使用的机制并未被直接测量或中介检验；H5的不支持被归因于边际效用递减，但未进行专门检验；平台使用行为是主观测量而非客观数据；实验只涉及一个app类型（趣味笑话），未覆盖其他类型app；研究只在微信平台、中国用户中进行，可能存在文化或平台差异。

## 贡献闭环

- technical_claim_cn：在本文的现场实验环境中，操纵三个界面属性均能显著改变用户分组感知，并且分组感知能显著改变平台→app衍生使用。

- artifact_claim_cn：高相似、高嵌入、高同步的app界面设计是提升分组感知的有效设计特征；在该机制下，前向衍生使用得到增强。

- mechanism_claim_cn：界面属性通过产生拓扑性质（突生特征）影响分组感知；分组感知通过信任转移增强前向衍生使用。

- boundary_claim_cn：该效应在Type 1平台（平台自身提供核心价值且UI可见）中成立，在Type 2平台中未必成立；对后向衍生使用未发现显著效应，可能是边际效用递减。

- reusable_design_knowledge_cn：可复用的设计原则：平台所有者可通过设置界面设计标准（视觉相似性、空间嵌入、响应同步）来促进用户对平台与app整体性的感知，进而增强平台对app的导流效应。

- theoretical_contribution_cn：将TBG引入IS平台研究并将其扩展至行为后果；提出“衍生使用”概念；将界面设计与平台治理联系起来；补充多技术使用文献。

- how_discussion_closes_intro_gap_cn：讨论通过总结三个界面设计属性实证影响分组感知并进而影响前向衍生使用，直接回应了引言中'集成界面设计能否强化平台与app之间的衍生使用'的缺口；同时以边际效用递减解释了后向路径的不显著，限定理论边界，防止简单否定。

- overclaim_or_unsupported_leaps_cn：作者声称'第一次证实界面设计标准化必要性'，但只检验了一个app类型、在单一平台、且后向衍生使用不显著；信任转移和协同特异性没有被测量，只能算理论解释；对H5的边际效用解释缺乏证据；平台使用意图测量的是使用意向而非实际平台使用。

## 句级写作动作图谱

### 1. Abstract P1 S1

- order：1

- section：Abstract

- locator：Abstract P1 S1

- move_code：CONTEXT

- paraphrase_cn：软件平台生态系统正在成为IT服务的主导模式。

- rhetorical_function_cn：开场建立研究场景的重要性。

- depends_on_cn：无

- sets_up_cn：为后续平台与app界面设计问题提供背景。

- evidence_pointer：Abstract P1

### 2. Abstract P1 S2

- order：2

- section：Abstract

- locator：Abstract P1 S2

- move_code：CONTEXT

- paraphrase_cn：平台所有者通常放弃对app用户界面的限制以加速第三方开发。

- rhetorical_function_cn：描述现实实践，引出‘百花齐放’的现状。

- depends_on_cn：平台重要性的背景。

- sets_up_cn：为后文张力（标准化 vs 自主）做铺垫。

- evidence_pointer：Abstract P1

### 3. Abstract P1 S3

- order：3

- section：Abstract

- locator：Abstract P1 S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：文献指出跨产品标准化界面设计是战略必需。

- rhetorical_function_cn：引入与平台实践相矛盾的另一套知识。

- depends_on_cn：已有产品线文献。

- sets_up_cn：构造张力，为研究问题提供必要性。

- evidence_pointer：Abstract P1

### 4. Abstract P1 S4

- order：4

- section：Abstract

- locator：Abstract P1 S4

- move_code：GAP

- paraphrase_cn：这种张力提出了研究问题：标准化界面设计是否有利于平台和app。

- rhetorical_function_cn：将矛盾浓缩为可研究问题。

- depends_on_cn：前面的张力描述。

- sets_up_cn：引出全文要回答的问题。

- evidence_pointer：Abstract P1

### 5. Abstract P1 S5

- order：5

- section：Abstract

- locator：Abstract P1 S5

- move_code：THEORY_INTRO

- paraphrase_cn：基于基本Gestalt理论，我们理论化三个界面设计属性。

- rhetorical_function_cn：宣布理论框架和核心自变量。

- depends_on_cn：研究问题需要理论解答。

- sets_up_cn：为后续假设和实验做铺垫。

- evidence_pointer：Abstract P1

### 6. Abstract P1 S6

- order：6

- section：Abstract

- locator：Abstract P1 S6

- move_code：THEORY_PROPOSITION

- paraphrase_cn：扩展理论来调查这些属性如何帮助双方吸引彼此的用户，反映衍生使用。

- rhetorical_function_cn：将理论扩展至行为结果。

- depends_on_cn：TBG理论本身。

- sets_up_cn：提出衍生使用的概念。

- evidence_pointer：Abstract P1

### 7. Abstract P1 S7

- order：7

- section：Abstract

- locator：Abstract P1 S7

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：进行了随机现场实验来检验假设。

- rhetorical_function_cn：说明研究方法。

- depends_on_cn：需要实证检验。

- sets_up_cn：为实验结果做预告。

- evidence_pointer：Abstract P1

### 8. Abstract P1 S8

- order：8

- section：Abstract

- locator：Abstract P1 S8

- move_code：RESULT

- paraphrase_cn：结果显示三个属性增强分组感知，从而增强平台到app的前向衍生使用。

- rhetorical_function_cn：报告主要发现。

- depends_on_cn：实验的结果。

- sets_up_cn：为结论和贡献做铺垫。

- evidence_pointer：Abstract P1

### 9. Abstract P1 S9

- order：9

- section：Abstract

- locator：Abstract P1 S9

- move_code：RESULT

- paraphrase_cn：与预期相反，分组感知不改善app到平台的后向衍生使用。

- rhetorical_function_cn：报告意外结果，显示研究的细致。

- depends_on_cn：实验结果。

- sets_up_cn：为讨论中的理论解释做铺垫。

- evidence_pointer：Abstract P1

### 10. Abstract P1 S10

- order：10

- section：Abstract

- locator：Abstract P1 S10

- move_code：CONTRIBUTION

- paraphrase_cn：这些发现对界面设计在软件平台生态系统中的价值有重要启示。

- rhetorical_function_cn：点明研究意义。

- depends_on_cn：研究结果。

- sets_up_cn：收束摘要。

- evidence_pointer：Abstract P1

### 11. Introduction P1 S1

- order：11

- section：Introduction

- locator：Introduction P1 S1

- move_code：CONTEXT

- paraphrase_cn：软件平台如Chrome和Android是可扩展代码库，为第三方app提供核心功能。

- rhetorical_function_cn：定义软件平台，建立共同理解。

- depends_on_cn：无

- sets_up_cn：引入平台与app的生态关系。

- evidence_pointer：Introduction P1

### 12. Introduction P1 S2

- order：12

- section：Introduction

- locator：Introduction P1 S2

- move_code：CONTEXT

- paraphrase_cn：平台通过吸引第三方app扩展产品边界，创造互补价值。

- rhetorical_function_cn：说明平台生态的价值创造机制。

- depends_on_cn：平台定义。

- sets_up_cn：引出app的重要性。

- evidence_pointer：Introduction P1

### 13. Introduction P1 S3

- order：13

- section：Introduction

- locator：Introduction P1 S3

- move_code：PRACTICAL_STAKES

- paraphrase_cn：为加速第三方开发，平台所有者经常放弃对app UI设计的限制，赋予开发者更多自主权。

- rhetorical_function_cn：指出现实中的普遍做法。

- depends_on_cn：平台生态价值。

- sets_up_cn：为与标准化原则的张力做铺垫。

- evidence_pointer：Introduction P1

### 14. Introduction P1 S4

- order：14

- section：Introduction

- locator：Introduction P1 S4

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：产品线设计文献发现标准化UI设计提供战略优势，是产品线管理和推出的必要。

- rhetorical_function_cn：引入与之相反的知识。

- depends_on_cn：产品线文献。

- sets_up_cn：构造‘自主 vs 标准化’的张力。

- evidence_pointer：Introduction P1

### 15. Introduction P2 S1

- order：15

- section：Introduction

- locator：Introduction P2 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：集成设计特征如界面标准化和链接被偏好，因为能提供无缝用户体验并帮助新产品吸引现有产品用户。

- rhetorical_function_cn：详细说明标准化的好处。

- depends_on_cn：产品线文献。

- sets_up_cn：为理论解释提供逻辑。

- evidence_pointer：Introduction P2

### 16. Introduction P2 S3

- order：16

- section：Introduction

- locator：Introduction P2 S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：产品线研究进一步指出跨产品设计在界面和功能层面整合的作用。

- rhetorical_function_cn：强调交叉产品设计的重要性。

- depends_on_cn：产品线文献。

- sets_up_cn：提示界面设计是整合的一个层面。

- evidence_pointer：Introduction P2

### 17. Introduction P3 S1

- order：17

- section：Introduction

- locator：Introduction P3 S1

- move_code：PHENOMENON

- paraphrase_cn：这种自主与整合设计之间的张力反映了平台所有者的‘跷跷板’问题，需要在开发者自主和平台整合之间平衡。

- rhetorical_function_cn：将两种知识汇总为具体的平台管理困境。

- depends_on_cn：前两段的知识。

- sets_up_cn：指出该问题尚未解决。

- evidence_pointer：Introduction P3

### 18. Introduction P3 S2

- order：18

- section：Introduction

- locator：Introduction P3 S2

- move_code：LIMITATION

- paraphrase_cn：尽管文献讨论了架构与治理在app层面的协调，但集成/协调界面设计在平台与app关系中的作用尚未充分探索。

- rhetorical_function_cn：明确指出文献不足。

- depends_on_cn：对已有文献的回顾。

- sets_up_cn：形成研究缺口。

- evidence_pointer：Introduction P3

### 19. Introduction P3 S3

- order：19

- section：Introduction

- locator：Introduction P3 S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：研究问题是集成界面设计是否能强化平台与app之间的衍生使用，即双向受益的使用关联。

- rhetorical_function_cn：正式提出研究问题。

- depends_on_cn：前面的缺口。

- sets_up_cn：统领全文。

- evidence_pointer：Introduction P3

### 20. Introduction P4 S1

- order：20

- section：Introduction

- locator：Introduction P4 S1

- move_code：THEORY_INTRO

- paraphrase_cn：借鉴基本Gestalt理论来研究用户如何根据界面设计对平台和app进行感知分组。

- rhetorical_function_cn：引入理论框架。

- depends_on_cn：研究问题需要理论。

- sets_up_cn：为三个设计原则提供理论来源。

- evidence_pointer：Introduction P4

### 21. Introduction P4 S2

- order：21

- section：Introduction

- locator：Introduction P4 S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：提出三个界面设计原则：界面相似性、界面嵌入性和界面同步性。

- rhetorical_function_cn：从理论中提炼可操作的设计属性。

- depends_on_cn：TBG理论。

- sets_up_cn：为后续假设和实验提供核心自变量。

- evidence_pointer：Introduction P4

### 22. Introduction P4 S4

- order：22

- section：Introduction

- locator：Introduction P4 S4

- move_code：THEORY_PROPOSITION

- paraphrase_cn：这些设计原则影响用户对app是平台一部分还是独立实体的感知，即分组感知。

- rhetorical_function_cn：建立设计属性到中间机制的关系。

- depends_on_cn：三个设计原则。

- sets_up_cn：为H1-H3做铺垫。

- evidence_pointer：Introduction P4

### 23. Introduction P5 S1

- order：23

- section：Introduction

- locator：Introduction P5 S1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：进一步扩展TBG，理解分组感知对用户使用行为的下游影响，区分两个方向的衍生使用。

- rhetorical_function_cn：扩展理论至行为后果。

- depends_on_cn：TBG理论基础。

- sets_up_cn：为H4和H5铺垫。

- evidence_pointer：Introduction P5

### 24. Introduction P5 S2

- order：24

- section：Introduction

- locator：Introduction P5 S2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：定义前向衍生使用（平台→app）和后向衍生使用（app→平台）。

- rhetorical_function_cn：明确核心因变量的定义。

- depends_on_cn：衍生使用概念。

- sets_up_cn：为使用行为测量提供概念基础。

- evidence_pointer：Introduction P5

### 25. Introduction P5 S3

- order：25

- section：Introduction

- locator：Introduction P5 S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：进行了随机现场实验，明确操纵相似性、嵌入性和同步性。

- rhetorical_function_cn：宣布研究方法。

- depends_on_cn：需要实证检验假设。

- sets_up_cn：为实验部分做预告。

- evidence_pointer：Introduction P5

### 26. Introduction P6 S1

- order：26

- section：Introduction

- locator：Introduction P6 S1

- move_code：CONTRIBUTION

- paraphrase_cn：研究贡献：补充平台文献、扩展Gestalt理论、丰富HCI、推进多技术使用文献。

- rhetorical_function_cn：预先声明理论贡献。

- depends_on_cn：研究问题和框架。

- sets_up_cn：为讨论部分的贡献详细展开做线索。

- evidence_pointer：Introduction P6

### 27. Theory – Value Creation P1 S1

- order：27

- section：Theory and Hypothesis Development

- locator：Theory – Value Creation P1 S1

- move_code：CONTEXT

- paraphrase_cn：软件平台生态系统由平台和app两个关键子系统组成，都能为用户提供价值。

- rhetorical_function_cn：建立平台生态的基本结构。

- depends_on_cn：平台定义。

- sets_up_cn：为价值创造路径的分类做铺垫。

- evidence_pointer：Theory section, Value Creation

### 28. Theory – Value Creation P2 S1

- order：28

- section：Theory and Hypothesis Development

- locator：Theory – Value Creation P2 S1

- move_code：PHENOMENON

- paraphrase_cn：存在两种典型价值创造路径：Type 1平台主要依赖平台核心功能；Type 2平台主要支持app。

- rhetorical_function_cn：区分平台类型，确定研究边界。

- depends_on_cn：平台生态结构。

- sets_up_cn：为后续聚焦Type 1平台做理由。

- evidence_pointer：Theory section, Value Creation

### 29. Theory – Value Creation P3 S2

- order：29

- section：Theory and Hypothesis Development

- locator：Theory – Value Creation P3 S2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：本研究聚焦Type 1平台，因为其UI对终端用户可见。

- rhetorical_function_cn：说明选择研究对象的理由。

- depends_on_cn：平台类型分类。

- sets_up_cn：限定研究范围。

- evidence_pointer：Theory section, Value Creation

### 30. Theory – App-Platform User Interface P1 S2

- order：30

- section：Theory and Hypothesis Development

- locator：Theory – App-Platform User Interface P1 S2

- move_code：MECHANISM

- paraphrase_cn：UI是应用的表示逻辑，管理输入和输出，帮助用户感知app价值。

- rhetorical_function_cn：解释UI在用户感知中的作用。

- depends_on_cn：功能与界面区分。

- sets_up_cn：为UI设计的重要性提供机制基础。

- evidence_pointer：Theory section, App-Platform User Interface

### 31. Theory – App-Platform User Interface P2 S1

- order：31

- section：Theory and Hypothesis Development

- locator：Theory – App-Platform User Interface P2 S1

- move_code：LIMITATION

- paraphrase_cn：平台文献主要讨论核心功能设计的相互依赖，UI设计价值在很大程度上被忽略。

- rhetorical_function_cn：指出平台文献的空白。

- depends_on_cn：对平台文献的回顾。

- sets_up_cn：为当前研究提供切入点。

- evidence_pointer：Theory section, App-Platform User Interface

### 32. Theory – App-Platform User Interface P3 S1

- order：32

- section：Theory and Hypothesis Development

- locator：Theory – App-Platform User Interface P3 S1

- move_code：GAP

- paraphrase_cn：产品线和HCI文献早就强调UI设计的重要性，但软件平台的新情境需要重新审视UI在app平台交互中的作用。

- rhetorical_function_cn：说明新情境下的知识缺口。

- depends_on_cn：产品线和HCI文献。

- sets_up_cn：引出需要新的理论视角。

- evidence_pointer：Theory section, App-Platform User Interface

### 33. Theory – App-Platform User Interface Design and Grouping P2 S1

- order：33

- section：Theory and Hypothesis Development

- locator：Theory – App-Platform User Interface Design and Grouping P2 S1

- move_code：THEORY_INTRO

- paraphrase_cn：引入TBG，将Gestalt原则作为影响分组感知的突生特征。

- rhetorical_function_cn：正式引入理论基础。

- depends_on_cn：需要解释分组感知的来源。

- sets_up_cn：为三个设计原则建立理论来源。

- evidence_pointer：Theory section, App-Platform User Interface Design and Grouping

### 34. Theory – App-Platform User Interface Design and Grouping P1 S2

- order：34

- section：Theory and Hypothesis Development

- locator：Theory – App-Platform User Interface Design and Grouping P1 S2

- move_code：MECHANISM

- paraphrase_cn：用户更倾向于通过对象间的相互关系感知分组，而不是通过对象自身的属性。

- rhetorical_function_cn：解释分组的视觉机制。

- depends_on_cn：视觉感知文献。

- sets_up_cn：为拓扑性质的作用提供逻辑。

- evidence_pointer：Theory section, App-Platform User Interface Design and Grouping

### 35. Theory – Grouping P4 S1

- order：35

- section：Theory and Hypothesis Development

- locator：Theory – Grouping P4 S1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：UI设计中三个拓扑性质的显著性可以强烈影响用户对平台与app的分组感知。

- rhetorical_function_cn：将拓扑性质与分组感知连接。

- depends_on_cn：TBG理论。

- sets_up_cn：为H1-H3做直接铺垫。

- evidence_pointer：Theory section, Grouping

### 36. Theory – Similarity, paragraph 'We therefore posit'

- order：36

- section：Theory and Hypothesis Development

- locator：Theory – Similarity, paragraph 'We therefore posit'

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：H1：界面相似性水平增强用户对平台与app的分组感知。

- rhetorical_function_cn：正式提出第一个假设。

- depends_on_cn：相似性原理的论证。

- sets_up_cn：为实验中的相似性操纵提供预期。

- evidence_pointer：Theory section, Similarity

### 37. Theory – Embeddedness, paragraph 'We therefore propose'

- order：37

- section：Theory and Hypothesis Development

- locator：Theory – Embeddedness, paragraph 'We therefore propose'

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：H2：更高的嵌入性增强用户的分组感知。

- rhetorical_function_cn：正式提出第二个假设。

- depends_on_cn：共同区域/包围性原理。

- sets_up_cn：为实验中的嵌入性操纵提供预期。

- evidence_pointer：Theory section, Embeddedness

### 38. Theory – Synchrony, paragraph 'Consequently, we propose'

- order：38

- section：Theory and Hypothesis Development

- locator：Theory – Synchrony, paragraph 'Consequently, we propose'

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：H3：更高的同步性增强用户的分组感知。

- rhetorical_function_cn：正式提出第三个假设。

- depends_on_cn：共同命运/同步性原理。

- sets_up_cn：为实验中的同步性操纵提供预期。

- evidence_pointer：Theory section, Synchrony

### 39. Theory – Grouping and Derivative Usage, paragraph 'we propose two explanatory mechanisms'

- order：39

- section：Theory and Hypothesis Development

- locator：Theory – Grouping and Derivative Usage, paragraph 'we propose two explanatory mechanisms'

- move_code：THEORY_INTRO

- paraphrase_cn：引入信任转移机制来解释分组感知如何影响前向衍生使用。

- rhetorical_function_cn：为前向行为提供解释机制。

- depends_on_cn：信任转移文献。

- sets_up_cn：为H4的推导提供机制。

- evidence_pointer：Theory section, Grouping and Derivative Usage

### 40. Theory – Grouping and Derivative Usage, paragraph 'we propose two explanatory mechanisms'

- order：40

- section：Theory and Hypothesis Development

- locator：Theory – Grouping and Derivative Usage, paragraph 'we propose two explanatory mechanisms'

- move_code：THEORY_INTRO

- paraphrase_cn：引入协同特异性机制来解释分组感知如何影响后向衍生使用。

- rhetorical_function_cn：为后向行为提供解释机制。

- depends_on_cn：协同特异性文献。

- sets_up_cn：为H5的推导提供机制。

- evidence_pointer：Theory section, Grouping and Derivative Usage

### 41. Theory – Platform-to-App Forward Derivative Usage, paragraph 'Consequently, we posit'

- order：41

- section：Theory and Hypothesis Development

- locator：Theory – Platform-to-App Forward Derivative Usage, paragraph 'Consequently, we posit'

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：H4：分组感知增强平台到app的前向衍生使用。

- rhetorical_function_cn：正式提出第四个假设。

- depends_on_cn：信任转移机制。

- sets_up_cn：为实验结果提供预期。

- evidence_pointer：Theory section, Forward Derivative Usage

### 42. Theory – App-to-Platform Backward Derivative Usage, paragraph 'We therefore posit'

- order：42

- section：Theory and Hypothesis Development

- locator：Theory – App-to-Platform Backward Derivative Usage, paragraph 'We therefore posit'

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：H5：分组感知增强app到平台的后向衍生使用。

- rhetorical_function_cn：正式提出第五个假设。

- depends_on_cn：协同特异性机制。

- sets_up_cn：为实验结果提供预期。

- evidence_pointer：Theory section, Backward Derivative Usage

### 43. Field Experiment P1 S1

- order：43

- section：Field Experiment

- locator：Field Experiment P1 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：采用2×2×2被试间因子设计，操纵三个界面属性。

- rhetorical_function_cn：交代实验设计。

- depends_on_cn：理论假设。

- sets_up_cn：为具体操纵描述做框架。

- evidence_pointer：Field Experiment 开头段

### 44. Field Experiment P2 S1

- order：44

- section：Field Experiment

- locator：Field Experiment P2 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：开发信息类app，在微信平台收集真实使用数据，操纵独立变量。

- rhetorical_function_cn：说明实验环境的真实性。

- depends_on_cn：需要自然场景收集行为。

- sets_up_cn：为后续操纵细节提供背景。

- evidence_pointer：Field Experiment P2

### 45. Field Experiment P3 S1

- order：45

- section：Field Experiment

- locator：Field Experiment P3 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：开发八个版本app，在相似性、嵌入性、同步性上操纵。

- rhetorical_function_cn：将理论属性转化为实验条件。

- depends_on_cn：因子设计。

- sets_up_cn：为具体操纵示例提供框架。

- evidence_pointer：Field Experiment P3

### 46. Field Experiment P3 S2

- order：46

- section：Field Experiment

- locator：Field Experiment P3 S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：高相似版本使app字体和背景色与微信相同，低相似版本则对比明显。

- rhetorical_function_cn：描述相似性的具体操纵方式。

- depends_on_cn：相似性定义。

- sets_up_cn：为操纵检验提供基础。

- evidence_pointer：Field Experiment P3

### 47. Field Experiment P3 S3

- order：47

- section：Field Experiment

- locator：Field Experiment P3 S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：高嵌入版本在微信内浏览内容，低嵌入版本跳到外部窗口。

- rhetorical_function_cn：描述嵌入性的具体操纵方式。

- depends_on_cn：嵌入性定义。

- sets_up_cn：为操纵检验提供基础。

- evidence_pointer：Field Experiment P3

### 48. Field Experiment P3 S4

- order：48

- section：Field Experiment

- locator：Field Experiment P3 S4

- move_code：DESIGN_FEATURE

- paraphrase_cn：高同步版本立即显示内容，低同步版本有5秒等待。

- rhetorical_function_cn：描述同步性的具体操纵方式。

- depends_on_cn：同步性定义。

- sets_up_cn：为操纵检验提供基础。

- evidence_pointer：Field Experiment P3

### 49. Field Experiment – Procedure P1 S1

- order：49

- section：Field Experiment

- locator：Field Experiment – Procedure P1 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：实验分两个阶段：第一阶段安装app并完成背景问卷，第二阶段两周内使用app并记录行为。

- rhetorical_function_cn：说明纵向数据收集设计。

- depends_on_cn：需要分离感知测量与行为测量。

- sets_up_cn：为数据结构和因果推断提供基础。

- evidence_pointer：Field Experiment – Procedure

### 50. Field Experiment – Procedure P2 S2

- order：50

- section：Field Experiment

- locator：Field Experiment – Procedure P2 S2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：通过app登录日志收集客观app使用行为，平台使用数据用问卷收集。

- rhetorical_function_cn：说明两种数据来源及原因。

- depends_on_cn：平台隐私限制。

- sets_up_cn：为结果中的测量说明做铺垫。

- evidence_pointer：Field Experiment – Procedure

### 51. Field Experiment – Procedure P4 S1

- order：51

- section：Field Experiment

- locator：Field Experiment – Procedure P4 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：比较响应组和无响应组的人口特征和平台使用，无显著差异，排除无响应偏差。

- rhetorical_function_cn：检查无响应偏差，增强外部有效性。

- depends_on_cn：样本流失。

- sets_up_cn：为结果可靠性提供支持。

- evidence_pointer：Field Experiment – Procedure

### 52. Results P1 S1

- order：52

- section：Results

- locator：Results P1 S1

- move_code：RESULT

- paraphrase_cn：独立样本t检验表明三个操纵均有效。

- rhetorical_function_cn：报告操纵检验结果。

- depends_on_cn：实验设计中的操纵。

- sets_up_cn：为后续假设检验提供基础。

- evidence_pointer：Results 第一段

### 53. Results P2 S1

- order：53

- section：Results

- locator：Results P2 S1

- move_code：RESULT

- paraphrase_cn：Cronbach's alpha和EFA表明信度和效度良好。

- rhetorical_function_cn：报告测量质量。

- depends_on_cn：问卷数据。

- sets_up_cn：为SEM结果提供可信性。

- evidence_pointer：Results 第二段

### 54. Results P3 S1

- order：54

- section：Results

- locator：Results P3 S1

- move_code：RESULT

- paraphrase_cn：ANOVA显示相似性、嵌入性、同步性的主效应显著，H1-H3成立。

- rhetorical_function_cn：报告三个设计属性的直接效应。

- depends_on_cn：因子设计数据。

- sets_up_cn：支持设计属性→分组感知的路径。

- evidence_pointer：Table 1

### 55. Results P4 S1

- order：55

- section：Results

- locator：Results P4 S1

- move_code：RESULT

- paraphrase_cn：SEM显示平台使用T0显著预测app使用（T1-T2），表明前向衍生使用存在。

- rhetorical_function_cn：确认前向衍生使用的基础路径。

- depends_on_cn：纵向数据。

- sets_up_cn：为H4的调节检验做铺垫。

- evidence_pointer：Figure 2

### 56. Results P4 S2

- order：56

- section：Results

- locator：Results P4 S2

- move_code：RESULT

- paraphrase_cn：app使用显著增强T2平台使用，表明后向衍生使用存在。

- rhetorical_function_cn：确认后向衍生使用的基础路径。

- depends_on_cn：纵向数据。

- sets_up_cn：为H5的调节检验做铺垫。

- evidence_pointer：Figure 2

### 57. Results P5 S1

- order：57

- section：Results

- locator：Results P5 S1

- move_code：RESULT

- paraphrase_cn：分组感知显著调节平台到app的前向衍生使用，H4得到支持。

- rhetorical_function_cn：报告H4的检验结果。

- depends_on_cn：SEM模型。

- sets_up_cn：支持理论的核心主张。

- evidence_pointer：Figure 2

### 58. Results P6 S1

- order：58

- section：Results

- locator：Results P6 S1

- move_code：RESULT

- paraphrase_cn：分组感知对app到平台的后向衍生使用调节不显著，H5未获支持。

- rhetorical_function_cn：报告未支持假设的结果。

- depends_on_cn：SEM模型。

- sets_up_cn：为随后解释留出空间。

- evidence_pointer：Figure 2

### 59. Results P6 S3

- order：59

- section：Results

- locator：Results P6 S3

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：用边际效用递减解释H5的不支持，认为大量app时新增app的边际效用递减。

- rhetorical_function_cn：对意外结果提供理论解释，保护核心论断。

- depends_on_cn：经济学中的边际效用概念。

- sets_up_cn：为讨论中的边界条件做铺垫。

- evidence_pointer：Results 末段

### 60. Discussion – Theoretical Implications P1

- order：60

- section：Discussion

- locator：Discussion – Theoretical Implications P1

- move_code：CONTRIBUTION

- paraphrase_cn：第一个贡献：为平台生态系统提供新视角，表明界面设计标准化在生态中的必要性。

- rhetorical_function_cn：将结果上升为理论贡献。

- depends_on_cn：研究结果。

- sets_up_cn：回应引言中的缺口。

- evidence_pointer：Discussion – Theoretical Implications

### 61. Discussion – Theoretical Implications P2

- order：61

- section：Discussion

- locator：Discussion – Theoretical Implications P2

- move_code：CONTRIBUTION

- paraphrase_cn：第二个贡献：从技术设计角度推进平台生态系统管理研究。

- rhetorical_function_cn：强调技术设计层面的理论意义。

- depends_on_cn：平台治理文献。

- sets_up_cn：扩展技术设计在IS理论中的地位。

- evidence_pointer：Discussion – Theoretical Implications

### 62. Discussion – Theoretical Implications P3

- order：62

- section：Discussion

- locator：Discussion – Theoretical Implications P3

- move_code：CONTRIBUTION

- paraphrase_cn：第三个贡献：将TBG扩展至平台生态系统并连接感知与行为。

- rhetorical_function_cn：声明理论扩展。

- depends_on_cn：TBG和实验证据。

- sets_up_cn：将文章与心理学文献连接。

- evidence_pointer：Discussion – Theoretical Implications

### 63. Discussion – Theoretical Implications P4

- order：63

- section：Discussion

- locator：Discussion – Theoretical Implications P4

- move_code：CONTRIBUTION

- paraphrase_cn：第四个贡献：提出衍生使用概念，推进多技术使用文献。

- rhetorical_function_cn：将结果上升为概念贡献。

- depends_on_cn：多技术使用文献。

- sets_up_cn：为未来研究提供新构念。

- evidence_pointer：Discussion – Theoretical Implications

### 64. Discussion – Practical Implications P1

- order：64

- section：Discussion

- locator：Discussion – Practical Implications P1

- move_code：PRACTICAL_STAKES

- paraphrase_cn：对平台所有者和开发者而言，集成界面设计是支持平台增长的宝贵战略。

- rhetorical_function_cn：将结果转化为实践指导。

- depends_on_cn：实验结果。

- sets_up_cn：为治理建议做铺垫。

- evidence_pointer：Discussion – Practical Implications

### 65. Discussion – Limitations P1 S1

- order：65

- section：Discussion

- locator：Discussion – Limitations P1 S1

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：研究边界限于Type 1平台，外推到Type 2平台需谨慎。

- rhetorical_function_cn：明确研究适用的平台类型。

- depends_on_cn：平台类型分类。

- sets_up_cn：防止读者过度泛化。

- evidence_pointer：Discussion – Limitations

### 66. Discussion – Limitations P1 S2

- order：66

- section：Discussion

- locator：Discussion – Limitations P1 S2

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：实验只操纵了一个app，可能低估界面设计的价值，尤其是对后向衍生使用。

- rhetorical_function_cn：指出单一app实验的局限。

- depends_on_cn：实验设计。

- sets_up_cn：为未来研究提供方向。

- evidence_pointer：Discussion – Limitations

### 67. Discussion – Limitations P1 S3

- order：67

- section：Discussion

- locator：Discussion – Limitations P1 S3

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：未来研究可探索平台自身UI不佳等情况，以及多样化的界面设计属性。

- rhetorical_function_cn：提供未来研究建议。

- depends_on_cn：当前研究的边界。

- sets_up_cn：为后续研究留出空间。

- evidence_pointer：Discussion – Limitations

### 68. Conclusion P1 S1

- order：68

- section：Conclusion

- locator：Conclusion P1 S1

- move_code：CONTRIBUTION

- paraphrase_cn：总结：研究解决了平台生态的悖论，支持四假设，贡献于生态系统悖论辩论。

- rhetorical_function_cn：收束全文，重申贡献。

- depends_on_cn：全文论证。

- sets_up_cn：给读者留下最终印象。

- evidence_pointer：Conclusion

## 写作技术

- gap_construction_cn：作者通过对比两种文献——软件平台实践中'百花齐放'的自主权与产品线设计中标准化战略必要性——构造出'张力'，指出这一张力虽然被提及但未充分探索，形成研究缺口。

- signposting_cn：在引言末尾明确列出四个贡献；在Theory部分用'First', 'Second', 'Third'组织设计属性；在Field Experiment部分明确指出两个阶段，并在Results开头预示操纵检验等。

- transition_logic_cn：从平台价值创造到UI设计再引入TBG，逐步收窄至三个属性；每个属性从平台独特特征切入，再引入对应的Gestalt原理，然后提出假设。实验部分先给出总体设计，再逐一说明操纵方式。Results先报告操纵检验和信效度，再检验假设，最后对未支持假设做补充解释。

- claim_evidence_rhythm_cn：每个设计属性假设后都紧跟对应的实例（如GSB、PN、RCG、EW），并在实验设计和结果中给出对应操纵和统计证据，形成主张—例证—检验的节奏。

- benchmark_narrative_cn：由于是因子设计，'benchmark'就是每个属性的低水平作为对照，作者通过对高vs低条件的对比来论证每个属性的作用。在SEM中，通过平台使用路径系数确认衍生使用方向，再将分组感知作为调节项。

- theory_return_cn：在Results确认部分假设后，Discussion将结果回扣TBG，声称扩展了TBG至行为后果，并将不显著结果解释为边际效用递减，从而保护和限定理论。

- contribution_positioning_cn：在引言和讨论中反复强调'首次'、'理论驱动'、'填补空白'，并同时声明研究边界，以抵御过度概括。

- novelty_protection_cn：通过将结果与既有平台治理文献和TBG连接，强调这是理论扩展而非单纯性能；对不显著结果给出理论解释，避免被解读为一次性失败。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：建立现实张力：对比平台实践与产品线标准化文献

- research_job_cn：找到紧张关系并指出研究空白

- required_evidence_cn：两到三个来源的支持

- transition_to_next_cn：将张力转化为具体研究问题

#### 2. 2

- step：2

- writing_job_cn：引入基础理论：从相关学科引入能解释现象的理论（如TBG）

- research_job_cn：提炼理论中与情境相关的概念

- required_evidence_cn：理论的原始定义和实证基础

- transition_to_next_cn：将概念适配到新情境

#### 3. 3

- step：3

- writing_job_cn：理论到设计翻译：将理论概念转换为可操作的设计属性

- research_job_cn：定义属性并提供示例

- required_evidence_cn：理论命题的因果逻辑

- transition_to_next_cn：提出假设

#### 4. 4

- step：4

- writing_job_cn：构建实验制品并操纵：设计真实app并操纵属性，以因子设计创建多个条件

- research_job_cn：开发和部署制品，确保操纵可行

- required_evidence_cn：操纵检验

- transition_to_next_cn：收集数据

#### 5. 5

- step：5

- writing_job_cn：现场实验与多阶段数据收集：设计两阶段收集自报感知和客观行为数据

- research_job_cn：招募、随机分配、追踪使用者

- required_evidence_cn：客观日志、问卷

- transition_to_next_cn：数据质量检验

#### 6. 6

- step：6

- writing_job_cn：多层次统计检验：操纵检验→信效度→主效应→模型

- research_job_cn：执行ANOVA、SEM

- required_evidence_cn：统计显著性

- transition_to_next_cn：解释结果

#### 7. 7

- step：7

- writing_job_cn：返回理论并设置边界：将结果纳入理论扩展，对不显著结果提供理论解释，列出边界

- research_job_cn：对比假设与结果，讨论理论和实践意义

- required_evidence_cn：假设结果和文献支持

- transition_to_next_cn：贡献主张

### most_transferable_moves_cn

1. 将管理或工程文献中的'张力'作为论文起点

2. 从心理学/感知理论提取拓扑属性并适配到平台设计

3. 使用因子设计操纵多项设计属性，而非单一a/b测试

4. 在真实平台上部署实验性app来收集真实使用行为

5. 对不支持假设用现有理论给予对称解释

### resource_intensive_or_nonstandard_parts_cn

1. 需要开发完整可用的app并部署在真实平台（微信）上

2. 需要大规模招募参与者（992人）并提供经济激励

3. 需要获得平台使用许可和API集成

4. 两阶段追踪数据收集耗时长

5. 基于隐私限制，平台使用数据只能自报

### what_not_to_copy_superficially_cn

1. 如果没有实际操纵设计属性，不能仅靠测量感知来声称因果

2. 如果后向路径不显著，不能忽视而应理论解释

3. 不能将结果推广到Type 2平台或多种app

4. 如果对机制没有直接测量，不能声称检验了机制

- single_best_description_of_the_routine_cn：从实践与文献的张力出发，借用成熟理论提炼可操纵的设计属性，构建并部署真实制品，用随机现场实验提供证据，再返回理论扩展并划清边界。

## 分析边界

本文基于提供的全文文本，但图片和附录细节无法完全核对；由于原文没有页码，locator只是章节和段落描述；对于未支持结果的解释部分是作者在Results中提出的，并非额外稳健性测试。
