# Achieving a Balance Between Privacy Protection and Data Collection: A Field Experimental Examination of a Theory-Driven Information Technology Solution

- 作者：Bailing Liu; Paul A. Pavlou; Xiufeng Cheng
- 年份 / 期刊：2022 / Information Systems Research
- DOI：10.1287/isre.2021.1045
- 源文件：28234_2022_achieving-a-balance-between-privacy-protection-and-data-collection-a-field-experimental-examinat.md
- 论文主类型：theory_derived_artifact_experiment
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.86

## 文章级论证概况

- 核心问题：在移动银行情境下，如何通过理论驱动的IT设计在隐私保护与数据收集之间取得平衡？

- 制品与设计：基于正义理论设计的三款移动银行隐私政策应用，核心是含“协商”与“主动推荐”的隐私政策应用；通过三参数区间直觉模糊集评价消费者隐私偏好，用隐私妥协值法和信息泛化设计个性化政策，并让客服代理与消费者互动协商。

- 客观结果：与仅有隐私声明及仅有协商功能的应用相比，含主动推荐的应用显著降低隐私顾虑、提高披露意愿和实际披露行为；单独协商功能对披露行为甚至有负效应，主动推荐是有效驱动。

- 核心贡献：首次将正义理论用于隐私保护设计，提出并验证了协商+主动推荐两个设计特征，证明IT设计能在提高消费者公平感的同时让企业收集更多数据；回应了IS领域“设计IT制品保护隐私”的呼吁。

- 整篇论证链：全文以“企业需要收集数据但消费者顾虑隐私”这一现实权衡开题；用正义理论指出静态隐私声明只提供程序正义，缺乏互动与分配正义；进而把两种正义分别映射为协商与主动推荐两个可设计特征；开发了三款原型应用，并以中国真实银行用户进行随机现场实验，先检验两个特征对隐私顾虑和披露意愿的主效应，再以实际披露行为与稳健性检验确认效果，最后用SEM说明公平感知与心理舒适的中介机制，从而把局部结果提升为“通过主动推荐实现隐私保护与数据收集平衡”的设计知识和理论贡献。

## 类型与写作弧线判定

- 论文主类型判定：论文从正义理论推导出两个可操作的设计特征（协商、主动推荐），据此构建三款原型应用，并通过现场实验比较特征差异和整体效果；它不是纯设计科学原则建构，也不是在既有平台上的简单操纵，而是“理论推导制品差异并通过实验检验”的典型模式。

- 主导写作弧线判定：文章从隐私保护与数据收集的现实矛盾出发，引入正义理论，将其转化为两款设计特征和具体应用，用现场实验检验，随后在讨论中返回到理论贡献和边界条件，形成了问题—理论—设计—检验—返回理论的完整弧线。

## 研究开展程序

- study_or_phase_count：7

- 研究阶段总序列：研究按“量化异质隐私偏好→设计分层隐私政策→预试验优化流程→现场实验主假设检验→实际披露行为与稳健性检验→事后机制与接受度分析→边界与理论讨论”累积；前一阶段为后一阶段提供可操作的制品组件，后一阶段又不断把前一阶段的局部结果上升为机制解释和设计知识。

### studies_or_phases

#### 1. 异质隐私偏好权重调查

- order：1

- name_cn：异质隐私偏好权重调查

- question_cn：如何将消费者的异质隐私偏好（信任倾向、一般隐私顾虑、企业声誉、激励提供）量化为可供推荐算法使用的权重？

- inputs_and_setting_cn：241名在线银行用户；四个影响因素变量；三类隐私群体（隐私原教旨主义者、务实多数派、轻微关注者）的权重评分。

- designed_or_compared_object_cn：针对三类消费者分别计算四变量权重公式F(u)。

- baseline_control_or_counterfactual_cn：无实验对照；以专家审查作为合理性校验。

##### objective_metrics

1. 重要性评分（1-7）

2. 三类消费者分别的权重向量

- analysis_method_cn：评分比例计算、四位IS专家审查

- main_result_cn：得到三组权重公式，例如务实多数派为F(u)=0.2470TP+0.2537PC+0.2532Re+0.2461Ic。

- argumentative_role_cn：为主动推荐特征提供可计算的消费者分类基础。

- remaining_uncertainty_cn：权重来自自报评分，未必代表真实披露行为；没有与其他机器学习预测方法比较。

- link_to_next_phase_cn：该权重公式被嵌入应用的第一步，用于客服代理判断消费者类别并推荐适量隐私政策。

##### evidence_pointers

1. Section 4.1.1

2. Online Appendix A Table A1/A2

3. Online Appendix C

#### 2. 隐私政策设计与基准校准

- order：2

- name_cn：隐私政策设计与基准校准

- question_cn：移动银行应请求哪些个人信息、出于什么用途，以及如何为不同隐私偏好消费者设计分层级隐私政策并设置实验基准？

- inputs_and_setting_cn：三家银行的管理者访谈；120名被试对12个信息项敏感性和数据使用担忧的评分；隐私妥协值法与信息泛化方法。

- designed_or_compared_object_cn：生成12个信息项、三类消费者的上下限隐私政策，以及三个实验应用的政策参数。

- baseline_control_or_counterfactual_cn：妥协水平设为隐私原教旨主义者85%、务实多数派50%、轻微关注者20%作为参数基准；App1采用轻微关注者下限政策作为传统静态声明。

##### objective_metrics

1. 信息敏感性评分（0-10）

2. 数据使用担忧评分（0-10）

- analysis_method_cn：隐私妥协值法、信息泛化、层次关系排序

- main_result_cn：形成S0-/S0*、S1-/S1*、S2-/S2*的有层次隐私政策集合，并据此设置App1、App2、App3的政策参数。

- argumentative_role_cn：让主动推荐和协商在真实信息条目上可操作，同时构建实验中的政策差异。

- remaining_uncertainty_cn：敏感性数据来自一次小样本调查；政策内容仅针对中国移动银行情境。

- link_to_next_phase_cn：为界面设计和现场实验提供了具体输入。

##### evidence_pointers

1. Section 4.1.2

2. Online Appendix A Table A3

#### 3. 预试验与界面流程优化

- order：3

- name_cn：预试验与界面流程优化

- question_cn：界面是否易用、说明是否清晰、现场实验流程是否可行？

- inputs_and_setting_cn：三批对象：10名IS教师与研究生、46名综合被试、以及离线银行场景中的用户和银行员工。

- designed_or_compared_object_cn：原型应用的用户界面、按钮、提示框、实验指导语、问卷布局和延迟功能。

- baseline_control_or_counterfactual_cn：三轮迭代中无正式对照，主要通过反馈前后对比。

##### objective_metrics

1. 定性反馈

2. 对界面真实感的主观评价

- analysis_method_cn：逐轮访谈和修改

- main_result_cn：界面被评价为近似真实银行应用，流程被精简，问卷被拆为必答与选答，增加延迟功能确保阅读。

- argumentative_role_cn：减少因界面或操作造成的混淆，提高主实验的内部效度与生态效度。

- remaining_uncertainty_cn：预试验不能证明理论效应，只能优化执行条件。

- link_to_next_phase_cn：把可执行版本带入真实银行现场实验。

##### evidence_pointers

1. Section 4.2

#### 4. 现场实验主假设检验

- order：4

- name_cn：现场实验主假设检验

- question_cn：在真实移动银行场景中，协商特征和主动推荐特征如何影响消费者的隐私顾虑与披露意愿？

- inputs_and_setting_cn：中国真实银行合作招募；372名参与者，剔除无效后336人；随机分配至App1、App2、App3。

- designed_or_compared_object_cn：三个应用条件：非协商隐私声明（App1）、协商但非主动推荐（App2）、协商+主动推荐（App3）。

- baseline_control_or_counterfactual_cn：App1作为基线方法，App2作为隔离协商特征的参照，App3与App2的差异用于识别主动推荐特征。

##### objective_metrics

1. 隐私顾虑量表

2. 披露意愿量表

3. 协商成功率

4. 花费时间

5. 调整默认设置的参与者数量

- analysis_method_cn：操纵检查、t检验、Mann-Whitney检验、方差分析、多元线性回归（含/不含控制变量）

- main_result_cn：H1a/1b不支持，单独协商特征对隐私顾虑和披露意愿无显著正向作用；H2a/2b支持，主动推荐显著降低隐私顾虑并提高披露意愿。

- argumentative_role_cn：检验两个设计特征的主效应，并暴露出孤立协商的局限。

- remaining_uncertainty_cn：自报告量表和意图未必转化为真实披露行为；主效应未解释机制。

- link_to_next_phase_cn：自然转向实际披露行为和稳健性分析。

##### evidence_pointers

1. Table 3

2. Table 4

3. Table 5

4. Section 5.2

#### 5. 实际披露行为分析与稳健性检验

- order：5

- name_cn：实际披露行为分析与稳健性检验

- question_cn：两个设计特征是否影响消费者实际披露信息的行为，而不仅仅影响自我报告的意图？

- inputs_and_setting_cn：同一336人实验数据；披露行为用参与者实际填写的信息项与敏感性评分构建；补充隐私政策层级作为控制变量。

- designed_or_compared_object_cn：在三种应用条件下比较实际披露行为；另用披露数量、披露敏感性得分替换披露行为指数。

- baseline_control_or_counterfactual_cn：以App1为传统基准，App2为协商基准；替换因变量作为稳健性。

##### objective_metrics

1. 披露行为指数（0-1）

2. 披露信息数量

3. 披露信息敏感性得分

- analysis_method_cn：OLS回归、多种替代模型

- main_result_cn：主动推荐对实际披露行为有显著正向影响；单独协商对实际披露行为有显著负向影响；整体上App3仍优于App1和App2。

- argumentative_role_cn：把结论从态度层面推进到行为层面，并证明主动推荐的效应强于协商的负效应。

- remaining_uncertainty_cn：行为只在实验会话中测量，不是长期采纳；不同模型的因变量口径存在差异。

- link_to_next_phase_cn：需要解释为什么协商单独产生负面效应，从而进入事后机制分析。

##### evidence_pointers

1. Section 5.3

2. Table 6

3. Online Appendix A Table A7

#### 6. 事后SEM机制分析与可选问卷分析

- order：6

- name_cn：事后SEM机制分析与可选问卷分析

- question_cn：为什么提案能产生效果？是通过提升程序、互动、分配正义并增加心理舒适来实现吗？消费者是否认为方案有用、易用并愿意使用？

- inputs_and_setting_cn：主实验中的正义感知、隐私顾虑、披露意愿、披露行为等构念数据；可选问卷中的感知易用性、有用性、使用意愿和开放式反馈。

- designed_or_compared_object_cn：建立结构方程模型检验中介链；比较App3与App1在可选问卷指标上的差异。

- baseline_control_or_counterfactual_cn：App1作为传统隐私声明的对照；SEM模型中无操纵对照，仅检验路径。

##### objective_metrics

1. 中介路径系数

2. 感知易用性

3. 感知有用性

4. 使用意愿

5. 披露后敏感度变化

- analysis_method_cn：结构方程模型（SEM）、t检验、内容分析

- main_result_cn：设计显著提高三维正义感知，通过互动与分配正义增强心理舒适，进而降低隐私顾虑并提升披露意愿和实际披露；App3在有用性、使用意愿上显著优于App1，易用性无显著差异。

- argumentative_role_cn：提供机制证据和消费者接受度证据，把主效应与理论联系起来。

- remaining_uncertainty_cn：SEM为事后分析，非预先注册；中介链依赖横截面自报数据；附录系数细节正文未完全展开。

- link_to_next_phase_cn：促使讨论部分界定适用边界、可行性并形成理论/实践贡献。

##### evidence_pointers

1. Section 5.4

2. Online Appendix D

3. Online Appendix E

4. Online Appendix F

#### 7. 可行性与边界条件分析

- order：7

- name_cn：可行性与边界条件分析

- question_cn：消费者是否真的会协商？时间成本是否过高？方案适合哪些情境？

- inputs_and_setting_cn：App2/App3中协商轮数、调整默认设置人数、成功结果；App3与App1的时间投入；可选问卷的易用性比较。

- designed_or_compared_object_cn：比较协商行为指标和感知指标在方案与传统声明之间的差异。

- baseline_control_or_counterfactual_cn：App1（传统隐私声明）作为时间与易用性对照。

##### objective_metrics

1. 平均协商轮数

2. 调整默认设置人数

3. 成功协商结果数

4. 时间花费

5. 感知易用性/有用性/使用意愿

- analysis_method_cn：描述性统计、t检验、Elaboration Likelihood Model解释

- main_result_cn：多数被试会主动协商和调整设置；App3时间投入更高但感知易用性与App1无显著差异；方案更适合敏感信息、长期关系型应用。

- argumentative_role_cn：回应实践可行性质疑，并划定外部效度边界。

- remaining_uncertainty_cn：未检验长期使用、跨情境推广或企业成本。

- link_to_next_phase_cn：直接进入讨论部分的理论贡献、实践建议和限制。

##### evidence_pointers

1. Section 6.2

2. Online Appendix E

## 各部分修辞架构

### abstract_moves

1. CONTEXT

2. THEORY_INTRO

3. RQ_OR_OBJECTIVE

4. STUDY_OVERVIEW

5. RESULT

6. MECHANISM

7. CONTRIBUTION

### introduction_moves

1. CONTEXT

2. PRACTICAL_STAKES

3. PRIOR_KNOWLEDGE

4. THEORY_INTRO

5. LIMITATION

6. GAP

7. WHY_GAP_MATTERS

8. RQ_OR_OBJECTIVE

9. MECHANISM

10. DESIGN_FEATURE

11. METHOD_JUSTIFICATION

12. STUDY_OVERVIEW

13. BOUNDARY_CONDITION

14. CONTRIBUTION

### theory_and_knowledge_moves

1. THEORY_INTRO

2. THEORY_PROPOSITION

3. MECHANISM

4. LIMITATION

5. HYPOTHESIS_OR_PROPOSITION

### artifact_design_moves

1. REQUIREMENT

2. DESIGN_FEATURE

3. METHOD_JUSTIFICATION

4. BENCHMARK_OR_CONTRAST

### evaluation_moves

1. STUDY_OVERVIEW

2. METHOD_JUSTIFICATION

3. RESULT

4. ROBUSTNESS_OR_BOUNDARY_TEST

5. MECHANISM

### discussion_and_contribution_moves

1. RESULT

2. MECHANISM

3. BOUNDARY_CONDITION

4. CONTRIBUTION

5. LIMITATION_AND_FUTURE

6. GAP

## 理论/知识到设计的翻译

### 知识/理论基础

1. 程序正义、互动正义、分配正义（justice theory）

2. Westin隐私偏好分类

3. 隐私妥协值法

4. 信息泛化

5. 三参数区间直觉模糊集

6. 社会交换与公平感知

7. Elaboration Likelihood Model（事后解释）

- 理论—设计耦合：direct

- 耦合判定理由：正义理论不仅在事后解释结果，而且直接决定了两个关键设计特征（协商对应互动正义、主动推荐对应分配正义），并被现场实验和SEM直接检验；因此是前瞻性理论到设计再到评价的闭合链条。

- 理论到设计翻译链：正义理论（互动正义→协商特征；分配正义→主动推荐特征；程序正义→可理解的隐私声明）→ 设计要求（提供双向互动、差异化个性化政策、简明可见的流程）→ 制品选择（三款应用、模糊偏好评价、妥协值法政策库、服务代理协商界面）→ 被比较的设计差异（App1/App2/App3）→ 客观结果（隐私顾虑、披露意愿、实际披露行为、机制路径）。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：程序正义要求流程可见、可理解、公平；现有隐私声明只做到这一种正义，但缺少互动与分配正义。

- mechanism_cn：如果消费者感知处理信息流程公平，隐私顾虑会下降。

- design_requirement_cn：保留并改进隐私声明的可见程序，同时增加其他两种正义。

- artifact_choice_cn：App1静态隐私声明作为基线；App3用高度可读界面显示信息用途和粒度，保持程序正义。

- evaluated_contrast_cn：App3对比App1和App2在感知程序正义上的差异。

- objective_result_cn：App3显著提高程序正义感知，且总体降低隐私顾虑、提高披露意愿/行为。

##### evidence_pointers

1. Section 3.2

2. Section 4.1.3

3. Section 5.4/Online Appendix D

#### 2. 2

- theory_or_knowledge_claim_cn：互动正义来自双向尊重性沟通；单向声明无法让消费者表达偏好。

- mechanism_cn：消费者被回应时感到被公平对待；透明协商会增加信息透明度，但也可能作为警示信号。

- design_requirement_cn：增加协商特征，让消费者能与客服代理对信息收集、使用、第三方访问达成一致。

- artifact_choice_cn：App2/App3内置协商界面，支持修改信息粒度和第三轮妥协。

- evaluated_contrast_cn：App2 vs App1，App3 vs App2。

- objective_result_cn：App2的互动正义感知更高，但H1a/1b不支持；协商单独对实际披露行为有负效应。

##### evidence_pointers

1. Section 3.3

2. Section 4.1.3

3. Section 5.1

4. Section 5.2

5. Table 6

#### 3. 3

- theory_or_knowledge_claim_cn：分配正义取决于投入与回报的公平权衡；消费者隐私偏好具有异质性。

- mechanism_cn：主动推荐个性化政策，让不同类别消费者披露不同量信息换取不同层次服务，产生公平感。

- design_requirement_cn：量化异质隐私偏好并设计差异化、分层级隐私政策，由客服代理主动推荐。

- artifact_choice_cn：三参数区间模糊集评价、隐私妥协值法、信息泛化、三类别的上下限政策。

- evaluated_contrast_cn：App3 vs App2，App3 vs App1。

- objective_result_cn：H2a/2b支持；主动推荐对实际披露行为显著正向。

##### evidence_pointers

1. Section 3.4

2. Section 4.1.1

3. Section 4.1.2

4. Section 5.2

5. Table 6

#### 4. 4

- theory_or_knowledge_claim_cn：三种正义同时满足能激发心理舒适并降低隐私顾虑。

- mechanism_cn：消费者的公平感→心理舒适→更低隐私顾虑→更多披露。

- design_requirement_cn：将协商与主动推荐同时整合在单一应用中。

- artifact_choice_cn：App3（协商+主动推荐）与客服代理交互。

- evaluated_contrast_cn：App3 vs App1/App2；事后SEM路径检验。

- objective_result_cn：描述性数据显示App3成功率高、披露信息多且敏感度高、隐私顾虑低；SEM支持中介链。

##### evidence_pointers

1. Table 3

2. Section 5.4

3. Online Appendix D

## 评价逻辑

### evaluation_modes

1. 随机现场实验

2. 操纵检查

3. 含控制变量的多元线性回归

4. 实际披露行为分析

5. 替代因变量的稳健性检验

6. 事后结构方程模型

7. 可选问卷的易用性/有用性/使用意愿分析

- why_these_evaluations_cn：主假设针对两个设计特征对隐私顾虑和披露意愿的影响，需要随机现场实验提供因果证据；因为自报意愿不一定等于行为，所以增加实际披露行为分析；又因单一主要结果可能受测度口径影响，使用替代因变量做稳健性检验；最后用SEM检验正义感知—心理舒适—披露的机制，用可选问卷评估实际采用可行性。

- benchmark_and_contrast_chain_cn：先以App1（传统静态隐私声明）为基线，建立最弱保护条件；App2增加协商特征，从而隔离出协商特征的净效果；App3再增加主动推荐，从而隔离出主动推荐特征的增量效果；随后用App3对App1的总体比较说明组合方案的有效性；之后在行为分析中把披露行为指数、数量、敏感性得分作为不同视角的因变量，完成从特征对比到机制解释的累积。

### claim_evidence_ledger

1. 协商特征降低隐私顾虑：回归系数不显著，H1a不支持——证据为Table 4 Model 1/2。

2. 协商特征提高披露意愿：回归系数不显著，H1b不支持——证据为Table 4。

3. 主动推荐特征降低隐私顾虑：系数-0.705***，H2a支持——证据为Table 4。

4. 主动推荐特征提高披露意愿：系数0.784***，H2b支持——证据为Table 4。

5. 主动推荐特征提高实际披露行为：基本模型系数0.269*，数量与敏感性得分模型亦显著——证据为Table 6。

6. 单独协商特征对实际披露行为有负效应：系数-0.174**，数量模型-2.163***，敏感性模型-9.821***——证据为Table 6。

7. App3整体优于传统隐私声明：补充比较（Table A6）以及描述性统计显示更低隐私顾虑、更高披露意愿和更多披露信息——证据为Table 3、Online Appendix A Table A6。

8. 机制是正义感知→心理舒适→更低顾虑/更高披露：事后SEM支持——证据为Section 5.4、Online Appendix D。

9. 消费者接受方案：有用性和使用意愿显著高于App1，易用性无显著差异——证据为Online Appendix E。

- internal_validity_strategy_cn：随机分配、剔除过短用时和操纵检查失败样本、三维正义感知操纵检查、控制人口统计与信任/声誉/移动隐私经验、非回应偏差检验、三轮预试验优化流程、实际披露行为作为客观结果。

- external_validity_strategy_cn：使用真实银行作为情境，通过银行渠道招募客户，样本结构与中国移动银行用户画像比较；讨论部分明确限定于敏感信息和长期关系类应用，并用ELM解释时间成本为何可以被接受。

- what_is_not_actually_tested_cn：没有直接测量数据泄露率或企业实际获得的长期数据价值；没有追踪消费者的长期使用或信任变化；主动推荐算法没有与机器学习等更先进方法正式对比；SEM为事后分析；实验仅覆盖中国移动银行情境。

## 贡献闭环

- technical_claim_cn：主动推荐特征能在统计上显著降低隐私顾虑、提高披露意愿和实际披露行为；单独协商特征不能实现这些目标，甚至对实际披露有负效应。

- artifact_claim_cn：协商+主动推荐的原型应用作为一个可运行的IT方案，能够同时兼顾消费者隐私保护和公司数据收集。

- mechanism_claim_cn：效果源于三维正义感知的增强——程序、互动、分配正义共同提升消费者心理舒适，使其更愿意披露个人信息。

- boundary_claim_cn：方案更适用于需要敏感信息、依赖长期客户关系的应用，如移动银行、医疗健康信息系统；对一次性或低敏感场景不一定合适。

- reusable_design_knowledge_cn：可复用的设计知识包括：将正义类型映射为具体隐私功能（协商→互动正义、主动推荐→分配正义）；用模糊偏好评价和妥协水平生成分层政策；用服务代理推荐机制补充静态声明；以及用现场实验+行为分析+机制检验的组合评价该设计。

- theoretical_contribution_cn：把正义理论从解释/预测扩展到隐私保护的规范性设计；证明单独透明化（协商）可能触发警示效应，只有结合主动推荐才能平衡保护与数据收集；也回应了IS领域对设计型隐私研究的呼吁并推动多学科研究方法。

- how_discussion_closes_intro_gap_cn：引言指出静态声明缺乏互动与分配正义、公司缺乏主动保护动机；讨论部分用现场实验和SEM说明：只有协商特征不够，主动推荐特征才补上分配正义并提升三类正义感知；由此实现了引言所追求的“平衡”，并回应了设计IT制品保护隐私的缺口。

- overclaim_or_unsupported_leaps_cn：作者从实验推断企业可以减少隐私事件并建立长期信任，但实验只测量一次性披露行为，未追踪信任或隐私事件；主动推荐算法权重来自小样本自报，且未与机器学习预测方法正式比较；SEM为事后分析，中介链依赖自报数据；将结果推广到传统线下零售也仅是推测。

## 句级写作动作图谱

### 1. Abstract P1 S1

- order：1

- section：Abstract

- locator：Abstract P1 S1

- move_code：CONTEXT

- paraphrase_cn：企业面临加强隐私保护和更先进数据收集方式之间的两难。

- rhetorical_function_cn：在摘要一开始界定核心问题。

- depends_on_cn：无。

- sets_up_cn：引出正义驱动的隐私保护方法。

- evidence_pointer：Abstract

### 2. Abstract P1 S2

- order：2

- section：Abstract

- locator：Abstract P1 S2

- move_code：THEORY_INTRO

- paraphrase_cn：作者采用正义理论整合隐私保护特征。

- rhetorical_function_cn：说明理论出发点。

- depends_on_cn：依赖已设定的核心问题。

- sets_up_cn：为后文提出的IT方案和假设铺垫。

- evidence_pointer：Abstract

### 3. Abstract P1 S3

- order：3

- section：Abstract

- locator：Abstract P1 S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：提出用IT方案平衡隐私保护与消费者数据收集。

- rhetorical_function_cn：宣告文章目标制品。

- depends_on_cn：依赖正义理论与问题设定。

- sets_up_cn：预告后续原型设计。

- evidence_pointer：Abstract

### 4. Abstract P1 S4

- order：4

- section：Abstract

- locator：Abstract P1 S4

- move_code：STUDY_OVERVIEW

- paraphrase_cn：在现场实验中把提案与两个常规应用对照。

- rhetorical_function_cn：预告评价方式。

- depends_on_cn：需要已提出的IT方案。

- sets_up_cn：为结果报告做准备。

- evidence_pointer：Abstract

### 5. Abstract P1 S5

- order：5

- section：Abstract

- locator：Abstract P1 S5

- move_code：RESULT

- paraphrase_cn：该应用降低隐私顾虑，提升披露意愿和实际行为。

- rhetorical_function_cn：给出核心结果预告。

- depends_on_cn：依赖现场实验。

- sets_up_cn：导向机制和贡献叙述。

- evidence_pointer：Abstract

### 6. Abstract P1 S6

- order：6

- section：Abstract

- locator：Abstract P1 S6

- move_code：RESULT

- paraphrase_cn：事后分析表明正义感知提高并让消费者舒适披露。

- rhetorical_function_cn：提供机制证据。

- depends_on_cn：依赖实验数据和SEM。

- sets_up_cn：为讨论中的理论贡献埋伏笔。

- evidence_pointer：Abstract

### 7. Introduction P1 S1–S2

- order：7

- section：Introduction

- locator：Introduction P1 S1–S2

- move_code：CONTEXT

- paraphrase_cn：信息隐私是网络空间最大问题之一，企业在大量收集和使用个人信息。

- rhetorical_function_cn：建立宏观背景。

- depends_on_cn：无。

- sets_up_cn：引出数据泄露和消费者顾虑。

- evidence_pointer：Introduction P1

### 8. Introduction P1 S3–S4

- order：8

- section：Introduction

- locator：Introduction P1 S3–S4

- move_code：PRACTICAL_STAKES

- paraphrase_cn：数据泄露抬高隐私顾虑，阻碍披露，伤害公司收集和利用数据的能力。

- rhetorical_function_cn：说明权衡问题的现实后果。

- depends_on_cn：基于数据泄露背景。

- sets_up_cn：引出必须平衡隐私保护与数据收集。

- evidence_pointer：Introduction P1

### 9. Introduction P2 S1–S2

- order：9

- section：Introduction

- locator：Introduction P2 S1–S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：过往研究表明公平感知对隐私保护至关重要，公平处理信息会促使披露。

- rhetorical_function_cn：引入理论视角。

- depends_on_cn：基于已有文献。

- sets_up_cn：随后把三种正义类型融入设计。

- evidence_pointer：Introduction P2

### 10. Introduction P3 S1–S2

- order：10

- section：Introduction

- locator：Introduction P3 S1–S2

- move_code：THEORY_INTRO

- paraphrase_cn：界定程序、互动和分配三种正义。

- rhetorical_function_cn：给出理论框架。

- depends_on_cn：依赖justice理论文献。

- sets_up_cn：用于批评现有隐私声明的不足。

- evidence_pointer：Introduction P3

### 11. Introduction P3 S3–S6

- order：11

- section：Introduction

- locator：Introduction P3 S3–S6

- move_code：GAP

- paraphrase_cn：现有静态隐私声明只体现程序正义，缺乏互动与分配正义，单向、复杂、无差异化，消费者只能接受或放弃。

- rhetorical_function_cn：指出现有制品的结构性局限。

- depends_on_cn：依赖三类正义框架。

- sets_up_cn：为提出协商和主动推荐特征铺路。

- evidence_pointer：Introduction P3

### 12. Introduction P4 S1–S2

- order：12

- section：Introduction

- locator：Introduction P4 S1–S2

- move_code：LIMITATION

- paraphrase_cn：公司缺乏动力提供灵活选择，消费者行为与其陈述偏好不一致。

- rhetorical_function_cn：指出理论与实践之间的裂缝。

- depends_on_cn：基于Acquisti等关于偏好不一致的研究。

- sets_up_cn：成为设计解决方案的动机。

- evidence_pointer：Introduction P4

### 13. Introduction P5 S1

- order：13

- section：Introduction

- locator：Introduction P5 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本文目标是通过正义理论整合设计元素，使消费者行为更符合其陈述偏好并鼓励适当披露。

- rhetorical_function_cn：正式提出研究目标。

- depends_on_cn：依赖前文的缺口与理论。

- sets_up_cn：引向具体设计特征和假设。

- evidence_pointer：Introduction P5

### 14. Introduction P5 S2

- order：14

- section：Introduction

- locator：Introduction P5 S2

- move_code：MECHANISM

- paraphrase_cn：双向协商能让双方比较讨论并寻求一致，缓解隐私冲突。

- rhetorical_function_cn：解释协商特征的作用机制。

- depends_on_cn：依赖互动正义理论。

- sets_up_cn：形成关于协商特征的假设。

- evidence_pointer：Introduction P5

### 15. Introduction P5 S3

- order：15

- section：Introduction

- locator：Introduction P5 S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：主动推荐特征可根据不同消费者推荐个性化隐私政策。

- rhetorical_function_cn：引入第二个关键设计特征。

- depends_on_cn：依赖分配正义和异质偏好思想。

- sets_up_cn：形成主动推荐特征的假设。

- evidence_pointer：Introduction P5

### 16. Introduction P5 S4

- order：16

- section：Introduction

- locator：Introduction P5 S4

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：作者预期两个特征同时存在会降低隐私顾虑并提高披露。

- rhetorical_function_cn：给出总体命题。

- depends_on_cn：依赖协商与主动推荐的机制。

- sets_up_cn：为方法部分的假设检验铺垫。

- evidence_pointer：Introduction P5

### 17. Introduction P6 S1

- order：17

- section：Introduction

- locator：Introduction P6 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：在移动银行情境下设计理论驱动的IT方案，特别考虑小屏挑战。

- rhetorical_function_cn：把概念转化为制品。

- depends_on_cn：依赖前文的两个设计特征。

- sets_up_cn：引出应用架构和算法细节。

- evidence_pointer：Introduction P6

### 18. Introduction P6 S2–S3

- order：18

- section：Introduction

- locator：Introduction P6 S2–S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：通过客服代理、三参数区间模糊集和隐私妥协值法实现个性化推荐和协商。

- rhetorical_function_cn：概述实现方法，避免只停留在概念层面。

- depends_on_cn：依赖数学方法和政策设计知识。

- sets_up_cn：为方法部分详细展开提供预告。

- evidence_pointer：Introduction P6

### 19. Introduction P7 S1–S2

- order：19

- section：Introduction

- locator：Introduction P7 S1–S2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：用移动银行现场实验检验提案效果，并对照两种常规应用。

- rhetorical_function_cn：预告实证设计。

- depends_on_cn：依赖已构建的三种应用。

- sets_up_cn：为实验结果部分做铺垫。

- evidence_pointer：Introduction P7

### 20. Introduction P7 S3

- order：20

- section：Introduction

- locator：Introduction P7 S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用结构方程模型分析正义感知与心理状态以解释实验结果。

- rhetorical_function_cn：说明机制检验方式。

- depends_on_cn：依赖实验收集的构念数据。

- sets_up_cn：为事后SEM分析做铺垫。

- evidence_pointer：Introduction P7

### 21. Introduction P7 S4

- order：21

- section：Introduction

- locator：Introduction P7 S4

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：由于方案需要额外时间，更适合长期关系和敏感信息的应用。

- rhetorical_function_cn：提前划定适用边界。

- depends_on_cn：基于方案的时间成本特点。

- sets_up_cn：在讨论中进一步扩展边界条件。

- evidence_pointer：Introduction P7

### 22. Introduction P8 S1–S2

- order：22

- section：Introduction

- locator：Introduction P8 S1–S2

- move_code：CONTRIBUTION

- paraphrase_cn：贡献在于用正义理论提出和设计IT方案，填补设计型隐私研究空白。

- rhetorical_function_cn：标识贡献并点出文献缺口。

- depends_on_cn：依赖前文的理论框架和实证预告。

- sets_up_cn：为文献综述中的GAP叙述做铺垫。

- evidence_pointer：Introduction P8

### 23. Introduction P8 S3–S4

- order：23

- section：Introduction

- locator：Introduction P8 S3–S4

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：回应了设计隐私保护IT制品的呼吁；计算机科学研究多脱离真实消费者。

- rhetorical_function_cn：说明缺口为何值得IS研究。

- depends_on_cn：依赖Belanger & Crossler和Pavlou的呼吁。

- sets_up_cn：强调多学科研究的必要性。

- evidence_pointer：Introduction P8

### 24. Section 2.1, paragraph beginning 'Past studies have shown...'

- order：24

- section：Literature Review

- locator：Section 2.1, paragraph beginning 'Past studies have shown...'

- move_code：LIMITATION

- paraphrase_cn：既有研究多研究现有隐私保护方法的效果，缺乏基于正义理论设计新方法。

- rhetorical_function_cn：在文献综述中确认缺口。

- depends_on_cn：依赖对justice theory应用文献的梳理。

- sets_up_cn：把本文定位为设计型隐私研究。

- evidence_pointer：Section 2.1

### 25. Section 2.2, paragraph beginning 'For example, Liu (2014)...'

- order：25

- section：Literature Review

- locator：Section 2.2, paragraph beginning 'For example, Liu (2014)...'

- move_code：LIMITATION

- paraphrase_cn：隐私声明在移动商务被批评为负担，没提供有意义选择。

- rhetorical_function_cn：支持现有方法无效。

- depends_on_cn：基于现有研究。

- sets_up_cn：为设计替代性隐私政策提供动机。

- evidence_pointer：Section 2.2

### 26. Section 2.2, paragraph beginning 'In sum...'

- order：26

- section：Literature Review

- locator：Section 2.2, paragraph beginning 'In sum...'

- move_code：GAP

- paraphrase_cn：以往研究偏重消费者保护，很少考虑公司视角，妨碍公司投资隐私保护。

- rhetorical_function_cn：把缺口从消费者端转向企业端。

- depends_on_cn：依赖之前对消费者中心研究的总结。

- sets_up_cn：引出主动推荐特征和平衡目标。

- evidence_pointer：Section 2.2

### 27. Section 3.2 P1 S1

- order：27

- section：Hypotheses Development

- locator：Section 3.2 P1 S1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：程序正义是可观察的公平，与隐私政策说明有关。

- rhetorical_function_cn：为基线设计提供理论背景。

- depends_on_cn：依赖justice theory。

- sets_up_cn：解释为什么App1作为传统声明基线。

- evidence_pointer：Section 3.2

### 28. Section 3.3 P1 S4

- order：28

- section：Hypotheses Development

- locator：Section 3.3 P1 S4

- move_code：MECHANISM

- paraphrase_cn：协商是双方决策过程，让消费者感到受到公平对待。

- rhetorical_function_cn：解释协商如何带来互动正义。

- depends_on_cn：依赖互动正义理论。

- sets_up_cn：形成H1a和H1b。

- evidence_pointer：Section 3.3

### 29. Section 3.3, end paragraph

- order：29

- section：Hypotheses Development

- locator：Section 3.3, end paragraph

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：假设带协商的隐私政策相比不带协商的会降低隐私顾虑并提高披露意愿。

- rhetorical_function_cn：给出可检验命题。

- depends_on_cn：依赖互动正义机制。

- sets_up_cn：让实验可以检验单一协商特征。

- evidence_pointer：Section 3.3

### 30. Section 3.4 P1 S3

- order：30

- section：Hypotheses Development

- locator：Section 3.4 P1 S3

- move_code：MECHANISM

- paraphrase_cn：消费者隐私偏好异质性导致对相同披露投入的价值判断不同。

- rhetorical_function_cn：引入分配正义需求。

- depends_on_cn：依赖隐私偏好异质性研究。

- sets_up_cn：为主动推荐特征提供理论基础。

- evidence_pointer：Section 3.4

### 31. Section 3.4 P3 S1

- order：31

- section：Hypotheses Development

- locator：Section 3.4 P3 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：主动推荐旨在提供分配正义，根据消费者偏好调整信息请求。

- rhetorical_function_cn：把理论转为设计特征。

- depends_on_cn：依赖异质偏好和分配正义。

- sets_up_cn：形成H2a和H2b。

- evidence_pointer：Section 3.4

### 32. Section 3.4, end paragraph

- order：32

- section：Hypotheses Development

- locator：Section 3.4, end paragraph

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：带主动推荐的协商相比不带主动推荐的更能降低隐私顾虑、提高披露意愿。

- rhetorical_function_cn：给出核心可检验命题。

- depends_on_cn：依赖分配正义机制。

- sets_up_cn：作为实验的主要对比。

- evidence_pointer：Section 3.4

### 33. Section 4.1 P1 S1

- order：33

- section：Research Methodology

- locator：Section 4.1 P1 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：开发三款移动银行应用作为三个实验条件。

- rhetorical_function_cn：把理论操作化为制品差异。

- depends_on_cn：依赖前文的设计特征。

- sets_up_cn：为后面的基准对照奠定基础。

- evidence_pointer：Section 4.1

### 34. Section 4.1.1 P1 S1

- order：34

- section：Research Methodology

- locator：Section 4.1.1 P1 S1

- move_code：REQUIREMENT

- paraphrase_cn：为推荐个性化政策，先量化异质隐私偏好。

- rhetorical_function_cn：说明实现主动推荐的前提条件。

- depends_on_cn：依赖主动推荐特征。

- sets_up_cn：引出权重调查和模糊集算法。

- evidence_pointer：Section 4.1.1

### 35. Section 4.1.1 P3 S1

- order：35

- section：Research Methodology

- locator：Section 4.1.1 P3 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用241名用户评分计算四类变量的相对权重。

- rhetorical_function_cn：为算法提供数据基础。

- depends_on_cn：依赖前述四变量要求。

- sets_up_cn：得到三组权重公式。

- evidence_pointer：Section 4.1.1

### 36. Section 4.1.2 P1 S1

- order：36

- section：Research Methodology

- locator：Section 4.1.2 P1 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：访谈三位银行经理确定所需信息及用途。

- rhetorical_function_cn：保证制品内容符合现实。

- depends_on_cn：依赖移动银行情境。

- sets_up_cn：生成12个信息项。

- evidence_pointer：Section 4.1.2

### 37. Section 4.1.2 P2 S1

- order：37

- section：Research Methodology

- locator：Section 4.1.2 P2 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用隐私妥协值法和信息泛化设计政策集合。

- rhetorical_function_cn：给设计提供可计算方法。

- depends_on_cn：依赖敏感性调查数据。

- sets_up_cn：产生三类消费者的上下限政策。

- evidence_pointer：Section 4.1.2

### 38. Section 4.1.2 P2 S3

- order：38

- section：Research Methodology

- locator：Section 4.1.2 P2 S3

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：为三类消费者设定85%、50%、20%妥协水平，作为政策设计参数。

- rhetorical_function_cn：建立推荐政策之间的层次对照。

- depends_on_cn：依赖Westin分类。

- sets_up_cn：使不同应用的政策差异可比较。

- evidence_pointer：Section 4.1.2

### 39. Section 4.1.3 P1 S1

- order：39

- section：Research Methodology

- locator：Section 4.1.3 P1 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：界面以简明方式展示信息粒度和用途，并提供下拉框供用户修改。

- rhetorical_function_cn：具体叙述制品界面。

- depends_on_cn：依赖政策设计和流程需求。

- sets_up_cn：使协商交互可行。

- evidence_pointer：Section 4.1.3

### 40. Section 4.1.4 P1 S2

- order：40

- section：Research Methodology

- locator：Section 4.1.4 P1 S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：把工作流程步骤对应到不同的正义感知。

- rhetorical_function_cn：明确设计特征与理论的对应。

- depends_on_cn：依赖主动推荐和协商功能。

- sets_up_cn：为实验结果的理论解释做铺垫。

- evidence_pointer：Section 4.1.4

### 41. Section 4.2 P1 S1

- order：41

- section：Research Methodology

- locator：Section 4.2 P1 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用三轮预试验修订界面和流程。

- rhetorical_function_cn：提高主实验执行质量。

- depends_on_cn：依赖初版应用界面。

- sets_up_cn：确保现场实验的内部效度。

- evidence_pointer：Section 4.2

### 42. Section 4.3 P1 S1

- order：42

- section：Research Methodology

- locator：Section 4.3 P1 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：以中国真实银行作为实验情境，通过二维码招募客户。

- rhetorical_function_cn：说明场域真实性。

- depends_on_cn：依赖三款原型应用。

- sets_up_cn：支持外部效度。

- evidence_pointer：Section 4.3

### 43. Section 4.3 P2 S1

- order：43

- section：Research Methodology

- locator：Section 4.3 P2 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：每个应用包含四阶段，先测敏感度，再读说明体验，最后填问卷并披露信息。

- rhetorical_function_cn：操作化实验流程。

- depends_on_cn：依赖实验设计。

- sets_up_cn：为后续数据收集提供结构。

- evidence_pointer：Section 4.3

### 44. Section 5.1 P1 S3

- order：44

- section：Results

- locator：Section 5.1 P1 S3

- move_code：RESULT

- paraphrase_cn：操纵检查表明三种条件在正义感知上显著不同。

- rhetorical_function_cn：证明实验条件如愿实现。

- depends_on_cn：依赖操纵检查统计。

- sets_up_cn：为假设检验提供基础。

- evidence_pointer：Section 5.1

### 45. Section 5.2 P2 S1

- order：45

- section：Results

- locator：Section 5.2 P2 S1

- move_code：RESULT

- paraphrase_cn：协商特征单独没有降低隐私顾虑或提高披露意愿，H1不支持。

- rhetorical_function_cn：报告假设检验的否定结果。

- depends_on_cn：依赖回归模型。

- sets_up_cn：强调主动推荐的必要性。

- evidence_pointer：Section 5.2

### 46. Section 5.2 P2 S2

- order：46

- section：Results

- locator：Section 5.2 P2 S2

- move_code：RESULT

- paraphrase_cn：主动推荐特征显著降低隐私顾虑并提高披露意愿，H2支持。

- rhetorical_function_cn：报告核心支持证据。

- depends_on_cn：依赖回归模型。

- sets_up_cn：引导到行为分析。

- evidence_pointer：Section 5.2

### 47. Section 5.3 P2 S2

- order：47

- section：Results

- locator：Section 5.3 P2 S2

- move_code：RESULT

- paraphrase_cn：主动推荐提高实际披露行为，协商单独对实际披露有负效应。

- rhetorical_function_cn：从意图转向实际行为。

- depends_on_cn：依赖行为指数计算。

- sets_up_cn：解释为何单独协商不可行。

- evidence_pointer：Section 5.3

### 48. Section 5.3 P3 S1

- order：48

- section：Results

- locator：Section 5.3 P3 S1

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：使用替代因变量后结果基本一致。

- rhetorical_function_cn：增强主要结论的稳健性。

- depends_on_cn：依赖基础模型。

- sets_up_cn：让结论不只依赖单一测度。

- evidence_pointer：Section 5.3

### 49. Section 5.4 P1 S1

- order：49

- section：Results

- locator：Section 5.4 P1 S1

- move_code：RESULT

- paraphrase_cn：事后分析显示设计增强三维公平感知，进而提高心理舒适，降低顾虑、促进披露。

- rhetorical_function_cn：提供机制证据。

- depends_on_cn：依赖SEM。

- sets_up_cn：为理论贡献铺路。

- evidence_pointer：Section 5.4

### 50. Section 6.1 P1 S2

- order：50

- section：Discussion

- locator：Section 6.1 P1 S2

- move_code：RESULT

- paraphrase_cn：再次总结孤立协商无益，透明可能成为警示信号。

- rhetorical_function_cn：解释主效应的理论含义。

- depends_on_cn：依赖主实验结果。

- sets_up_cn：论证必须组合主动推荐。

- evidence_pointer：Section 6.1

### 51. Section 6.1 P3 S1

- order：51

- section：Discussion

- locator：Section 6.1 P3 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：方案不仅协商信息收集，还协商信息使用和第三方访问，以缓解控制悖论。

- rhetorical_function_cn：说明设计考虑周全。

- depends_on_cn：依赖控制悖论文献。

- sets_up_cn：证明方案对消费者和企业都有益。

- evidence_pointer：Section 6.1

### 52. Section 6.2 P2 S1

- order：52

- section：Discussion

- locator：Section 6.2 P2 S1

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：App3时间投入更高但感知易用性与App1无显著差异，用户愿意为意识决策花时间。

- rhetorical_function_cn：处理可行性质疑。

- depends_on_cn：依赖时间数据与易用性比较。

- sets_up_cn：引出ELM解释和边界条件。

- evidence_pointer：Section 6.2

### 53. Section 6.2 P2 S4

- order：53

- section：Discussion

- locator：Section 6.2 P2 S4

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：方案更适用于需要长期关系和敏感信息的应用。

- rhetorical_function_cn：划定适用域。

- depends_on_cn：依赖时间成本分析。

- sets_up_cn：形成实践建议。

- evidence_pointer：Section 6.2

### 54. Section 6.3 P1 S1

- order：54

- section：Discussion

- locator：Section 6.3 P1 S1

- move_code：CONTRIBUTION

- paraphrase_cn：首次把正义理论融入隐私保护设计并验证。

- rhetorical_function_cn：声明第一项理论贡献。

- depends_on_cn：依赖全文设计与实验。

- sets_up_cn：提供未来研究方向。

- evidence_pointer：Section 6.3

### 55. Section 6.3 P2 S1

- order：55

- section：Discussion

- locator：Section 6.3 P2 S1

- move_code：CONTRIBUTION

- paraphrase_cn：实证表明IT方案能同时实现隐私保护与数据收集平衡。

- rhetorical_function_cn：声明第二项理论贡献。

- depends_on_cn：依赖主实验和行为分析。

- sets_up_cn：倡导更多设计型研究。

- evidence_pointer：Section 6.3

### 56. Section 6.4 P1 S2

- order：56

- section：Discussion

- locator：Section 6.4 P1 S2

- move_code：CONTRIBUTION

- paraphrase_cn：实践启示是从被动声明转向主动推荐个性化政策。

- rhetorical_function_cn：给出管理建议。

- depends_on_cn：依赖验证结果。

- sets_up_cn：引出公共政策建议。

- evidence_pointer：Section 6.4

### 57. Section 6.5 P1 S1

- order：57

- section：Discussion

- locator：Section 6.5 P1 S1

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：指出未充分处理协商中的隐私冲突，未来需技术与非技术解决方案。

- rhetorical_function_cn：界定局限。

- depends_on_cn：依赖整体设计范围。

- sets_up_cn：为未来研究指明方向。

- evidence_pointer：Section 6.5

### 58. Conclusion P1 S2

- order：58

- section：Conclusion

- locator：Conclusion P1 S2

- move_code：GAP

- paraphrase_cn：IS隐私文献多为解释预测，设计型研究少。

- rhetorical_function_cn：重申引言缺口。

- depends_on_cn：依赖文献综述。

- sets_up_cn：收束全文贡献。

- evidence_pointer：Conclusion

### 59. Conclusion P1 S3

- order：59

- section：Conclusion

- locator：Conclusion P1 S3

- move_code：CONTRIBUTION

- paraphrase_cn：总结提供平衡隐私与数据收集的IT方案并倡导主动式隐私保护。

- rhetorical_function_cn：整体收束和呼吁。

- depends_on_cn：依赖全部研究证据。

- sets_up_cn：呼吁未来在智能增强设计中加入隐私保护。

- evidence_pointer：Conclusion

## 写作技术

- gap_construction_cn：作者用两层缺口推进：一是静态隐私声明只提供程序正义，缺乏互动和分配正义；二是IS界多用正义理论做解释/预测，很少设计新制品。两层缺口都被封装在‘如何平衡保护与收集’的现实问题中。

- signposting_cn：大量使用“In this paper”“We hypothesize that”“To capture consumers’ reactions”“Post hoc analysis”等路标，让读者始终知道当前处于问题、设计、检验还是贡献环节。

- transition_logic_cn：从文献到假设：每次指出一种正义缺失后，立即提出对应特征；从方法到结果：在主实验后，先用假设检验，再转向行为分析，最后用机制分析；结果间用“not supported/supported”和“further confirms”衔接。

- claim_evidence_rhythm_cn：每个假设对应一个回归系数和表格；否定结果不被隐藏，反而被用来论证孤立协商不足；随后用主动推荐的正向结果和整体比较建立正向主张，再通过稳健性检验和SEM强化证据节奏。

- benchmark_narrative_cn：App1被视为传统基准，App2被用来隔离协商特征，App3被用来体现完整方案；benchmark不只在实验部分出现，还在讨论中反复用于解释时间成本、成功率和可行性。

- theory_return_cn：讨论部分用正义理论解释为什么单协商失败（透明成为警示），为什么主动推荐有效（补上分配正义）；并把结果升华为‘正义理论可指导隐私保护设计’的一般知识。

- contribution_positioning_cn：作者将贡献定位为理论驱动的设计研究，并强调多学科交叉，明确回应IS设计呼吁，从而把一次实验升级为学科性贡献。

- novelty_protection_cn：通过展示单一协商特征的无效和负效应，防止贡献被简化为“加了协商就有效”；通过主动推荐的主效应、行为效应和SEM机制共同锁定“组合设计”的不可替代性，并把适用边界同时声明，避免退化为一次性性能结果。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：用现实威胁和统计数字建立隐私保护与数据收集之间的张力。

- research_job_cn：识别一个具有实际后果的权衡问题，并引用权威行业报告或文献。

- required_evidence_cn：数据泄露规模、消费者隐私顾虑与企业采集需求之间冲突的证据。

- transition_to_next_cn：指出公平感知能缓解这一冲突，从而进入理论。

#### 2. 2

- step：2

- writing_job_cn：选择理论并明确把理论的子维度映射到可设计特征。

- research_job_cn：找到能解释缺口和制品功能的理论，并说明每个理论元素对应什么设计特征。

- required_evidence_cn：已有研究证明该理论元素与隐私顾虑/披露行为相关。

- transition_to_next_cn：以假设形式把预期效果写出来，并说明需要实验检验。

#### 3. 3

- step：3

- writing_job_cn：描述制品的架构、算法、界面和工作流程。

- research_job_cn：把理论映射转化为可运行的IT原型或数字设计。

- required_evidence_cn：有明确算法/参数来源、真实情境输入、可用性预试验结果。

- transition_to_next_cn：说明如何通过对照实验评估该制品。

#### 4. 4

- step：4

- writing_job_cn：描述实验设计、操纵、样本、测量和操纵检查。

- research_job_cn：开展随机现场实验或可控实验，尽量用真实组织和真实用户。

- required_evidence_cn：随机分配、有效样本、操纵检查通过、无显著组间人口差异。

- transition_to_next_cn：报告主效应和假设检验结果。

#### 5. 5

- step：5

- writing_job_cn：报告假设结果，并对否定结果给出解释。

- research_job_cn：用回归或方差分析暴露每个设计特征的独立效果。

- required_evidence_cn：回归系数、显著性、R方、是否有控制变量前后的稳定性。

- transition_to_next_cn：指出意图结果可能脱离行为，需要检查实际行为。

#### 6. 6

- step：6

- writing_job_cn：用客观行为数据或替代因变量做稳健性检验。

- research_job_cn：收集或构造实际行为指标，并用多个口径验证同一结论。

- required_evidence_cn：行为指标在不同测度下方向一致且显著。

- transition_to_next_cn：追问机制是什么，从而进入事后中介分析。

#### 7. 7

- step：7

- writing_job_cn：用SEM或路径模型检验理论机制，并用可选问题考察接受度。

- research_job_cn：收集与理论机制相关的构念，估计中介模型。

- required_evidence_cn：显著的中介路径、模型拟合指标、消费者接受度数据。

- transition_to_next_cn：回到理论贡献、边界条件、实践影响和局限。

### most_transferable_moves_cn

1. 用理论子维度对应设计特征并在流程图中标出正义类型。

2. 把单个特征和组合特征做成多个应用版本以隔离因果效应。

3. 同时报告自报意图和实际行为，并用替代因变量做稳健性。

4. 事后用SEM补上机制解释，并单独分析可行性和边界。

5. 不回避否定假设，反而用否定结果强化核心设计主张。

### resource_intensive_or_nonstandard_parts_cn

1. 与真实银行合作招募客户并通过二维码进行现场实验。

2. 开发三款可运行的原型应用，包括模糊算法、政策库和客服代理工作流。

3. 进行241人和120人的前置调查来确定权重和敏感性。

4. 三轮预试验和372人的主实验需要较大时间与组织成本。

### what_not_to_copy_superficially_cn

1. 不能只写“基于正义理论设计”，必须有真实算法和政策生成过程。

2. 不能只报告意图效应，至少要有实际行为或可观察结果。

3. 不能只依赖事后SEM宣称机制，需要有操纵检查或预注册路径。

4. 不能忽视边界条件，若情境不是敏感信息/长期关系，方案并不适用。

- single_best_description_of_the_routine_cn：从现实权衡出发，用理论映射出两个可供操纵的设计特征，用三个原型场实验隔离各特征效果，再加行为数据与机制检验把结果升华为设计知识。

## 分析边界

附录D/E/F的完整SEM系数、路径图和可选问卷统计量无法从正文核对；现场实验具体招募细节和量表题项细节部分依赖附录；对‘机制’的精确路径系数只能依据正文描述而非附录原始输出。
