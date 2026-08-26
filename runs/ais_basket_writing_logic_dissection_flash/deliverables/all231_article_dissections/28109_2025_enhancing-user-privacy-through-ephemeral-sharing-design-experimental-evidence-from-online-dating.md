# Enhancing User Privacy Through Ephemeral Sharing Design: Experimental Evidence from Online Dating

- 作者：Yumei He; Xingchen Xu; Ni Huang; Yili Hong; De Liu
- 年份 / 期刊：2025 / Information Systems Research
- DOI：10.1287/isre.2021.0379
- 源文件：28109_2025_enhancing-user-privacy-through-ephemeral-sharing-design-experimental-evidence-from-online-dating.md
- 论文主类型：field_intervention_or_platform_experiment
- 主导写作弧线：phenomenon_mechanism_intervention_field_test
- 置信度：0.9

## 文章级论证概况

- 核心问题：在线上约会平台中，短暂分享设计如何影响用户个人照片披露、匹配结果和匹配后互动，以及其背后的隐私机制是什么？

- 制品与设计：在匹配请求阶段提供“短暂照片”上传功能：照片对接收者短暂可见、自动消失且不可下载或截图；对照组为持久照片上传。UI包含按钮文案、阅后即焚图标和解释句等操纵元素。

- 客观结果：70,275名用户的随机现场实验显示：治疗组比对照组多发送52.1%的照片和多61.6%的含人脸照片，多获得3.3%的匹配和4.6%的接收者消息；在线实验显示短暂分享通过降低数据收集、传播和身份滥用担忧提高披露意愿；对隐私敏感者效应更强。

- 核心贡献：提出并实证检验一种鼓励披露而非限制披露的隐私增强设计，扩展短暂分享文献到陌生人匹配场景，并展示个人信息在点对点互动中的价值。

- 整篇论证链：线上约会中，隐私担忧导致用户在匹配初期不愿披露个人照片，进而引发冷启动问题。作者提出短暂分享设计，以自动消失和不可追溯来降低接收者滥用信息的风险，从而在保护隐私的同时鼓励披露。作者与平台合作开展随机现场实验，将短暂照片上传与持久照片上传对照，发现短暂分享增加了照片和含人脸照片的披露、匹配数和接收者互动消息；顺序中介表明这些下游效应由披露增加驱动。随后在线实验检验心理机制，发现短暂分享降低数据收集、传播和身份滥用担忧，并提高披露意向；异质性分析显示隐私敏感用户获益更大。讨论部分将结果回接到隐私增强设计文献，提出可复用的设计原则。

## 类型与写作弧线判定

- 论文主类型判定：核心证据来自与真实约会平台合作的用户层面随机现场实验，在实际产品中操纵短暂照片与持久照片设计，并观察真实匹配和消息行为；辅以在线机制实验。

- 主导写作弧线判定：文章沿“冷启动现象—隐私担忧机制—短暂分享干预—现场因果检验—在线机制检验”展开，通过现场实验建立因果效应，并通过在线实验解释机制。

## 研究开展程序

- study_or_phase_count：6

- 研究阶段总序列：第一阶段从文献与访谈中提炼社会隐私担忧并设计短暂分享UI；第二阶段在真实平台部署大规模随机现场实验并完成数据收集与随机化检验；第三阶段估计总效应；第四阶段用现场数据做顺序中介并排除一系列备择解释；第五阶段用在线实验测量心理构念；第六阶段做异质性与稳健性检验并进入讨论。各阶段依次回答：设计是否合理→是否在真实世界产生效应→效应是否由披露驱动→为什么披露增加→哪些用户获益更多。

### studies_or_phases

#### 1. 设计与概念化阶段

- order：1

- name_cn：设计与概念化阶段

- question_cn：如何把社会隐私担忧转译成一种既保护隐私又鼓励披露的数字设计？

- inputs_and_setting_cn：线上约会平台用户访谈、现有短暂分享文献、平台开发者与预测试。

- designed_or_compared_object_cn：短暂照片上传UI与持久照片上传UI的对照；治疗组UI包含“上传短暂照片”文案、阅后即焚图标和解释句。

- baseline_control_or_counterfactual_cn：持久照片上传作为控制条件。

##### objective_metrics

1. 用户对短暂照片概念的阅读理解程度

- analysis_method_cn：用户访谈、预测试和UI设计；确认用户理解治疗刺激。

- main_result_cn：平台用户能够理解短暂照片的自动消失和不可追溯属性；治疗刺激得以实现。

- argumentative_role_cn：建立理论到设计的翻译链，为现场实验提供可操作的操纵。

- remaining_uncertainty_cn：设计能否改变真实行为尚不清楚。

- link_to_next_phase_cn：直接引出随机现场实验来检验实际行为效应。

##### evidence_pointers

1. Section 2.3.2

2. Section 3.2

3. Online Appendices A and E

#### 2. 现场随机实验部署与数据收集

- order：2

- name_cn：现场随机实验部署与数据收集

- question_cn：在真实平台中，短暂分享相对持久分享是否影响披露、匹配和互动？

- inputs_and_setting_cn：与Summer平台合作；70,275名用户在应用更新至3.8.2时被随机分配；实验期18天；平台社区被调节以避免讨论治疗。

- designed_or_compared_object_cn：治疗组可上传短暂照片；对照组可上传持久照片；其余匹配请求流程相同。

- baseline_control_or_counterfactual_cn：对照组使用持久照片上传功能。

##### objective_metrics

1. 随机化检验的t统计量与K-S统计量

2. 协变量平衡

- analysis_method_cn：用户层面随机化分配；对数值变量做t检验，对分类变量做Kolmogorov-Smirnov检验。

- main_result_cn：ProfileFace、PhotoWallFace、性别、年龄、教育等观察协变量在两组间无显著差异。

- argumentative_role_cn：建立因果识别基础，证明实验设计的有效性。

- remaining_uncertainty_cn：具体系数效应大小和机制尚未估计。

- link_to_next_phase_cn：直接进入主分析估计总效应。

##### evidence_pointers

1. Section 3.1

2. Section 3.2

3. Section 4.1

4. Section 4.2

5. Figures 2 and 3

6. Table 4

#### 3. 总效应估计（主分析）

- order：3

- name_cn：总效应估计（主分析）

- question_cn：短暂分享对信息披露、匹配结果和接收者互动结果的总效应是什么？

- inputs_and_setting_cn：用户层面行为痕迹数据、人口统计和实验分组；70,275名用户。

- designed_or_compared_object_cn：比较治疗组与对照组在NumPhoto、NumFace、NumMatch、SumMsgFromReceiver上的差异。

- baseline_control_or_counterfactual_cn：持久照片组；OLS中控制PhotoWallFace、性别、年龄、教育、热度、任期，并加入进入日期虚拟变量。

##### objective_metrics

1. NumPhoto

2. NumFace

3. NumMatch

4. Ln(SumMsgFromReceiver)

- analysis_method_cn：OLS回归，带稳健标准误；同时报告无模型均值比较。

- main_result_cn：治疗组多发送52.1%的照片、多61.6%的含人脸照片、多3.3%的匹配、多4.6%的接收者消息。

- argumentative_role_cn：建立短暂分享设计的整体因果效应。

- remaining_uncertainty_cn：总效应不能说明为什么发生，也无法排除选择、新奇或内容变化等替代解释。

- link_to_next_phase_cn：进入中介分析与备择解释排除。

##### evidence_pointers

1. Section 5.1

2. Tables 5, 6, and 7

#### 4. 行为中介与备择解释排除

- order：4

- name_cn：行为中介与备择解释排除

- question_cn：效应是否通过增加的披露行为传递？是否可归因于请求数量、对象选择、新奇效应或照片内容变化？

- inputs_and_setting_cn：现场实验数据；发送的照片图像；Baidu AI人脸检测、露骨内容分类器、面部吸引力预测模型；发送者所追求接收者的属性数据。

- designed_or_compared_object_cn：序列中介模型中的Ephemeral→NumPhoto→NumMatch→NumMsgFromReceiver路径；不同备择解释下的组间比较。

- baseline_control_or_counterfactual_cn：直接路径作为对照；持久照片组作为基线；时间窗口T2作为新奇效应的反事实。

##### objective_metrics

1. PROCESS Bootstrap间接效应置信区间

2. NumRequestPageView和NumRequest系数

3. 对象选择变量的t检验

4. Ephemeral×T2交互系数

5. 良性/毒性去抑制和面部吸引力的组间差异

- analysis_method_cn：顺序中介分析；OLS；t检验；计算机视觉内容分类。

- main_result_cn：Ephemeral→NumPhoto→NumMatch→NumMsgFromReceiver的间接效应显著；直接路径不显著；请求次数、对象选择、新奇效应、良性/毒性去抑制、面部吸引力均不显著。

- argumentative_role_cn：建立披露作为核心行为机制，同时排除一系列替代机制。

- remaining_uncertainty_cn：为什么披露增加仍需要心理构念层面证据；尚未区分具体是哪类隐私担忧被降低。

- link_to_next_phase_cn：引入在线实验，直接测量隐私担忧和其他心理机制。

##### evidence_pointers

1. Section 5.2.1

2. Figure 4

3. Section 5.2.2

4. Tables 8–15

5. Online Appendix D

#### 5. 在线实验（心理机制）

- order：5

- name_cn：在线实验（心理机制）

- question_cn：短暂分享通过降低哪些具体的隐私担忧（或通过其他心理机制）提高披露意向？

- inputs_and_setting_cn：105名中国Sojump参与者的在线实验；治疗组53人、对照组52人；视频刺激展示短暂或持久照片上传；问卷测量社会隐私担忧、机构隐私担忧、自我呈现意向和披露意向。

- designed_or_compared_object_cn：短暂照片视频vs持久照片视频；两组流程相同。

- baseline_control_or_counterfactual_cn：持久照片条件作为控制。

##### objective_metrics

1. PLS-SEM路径系数

2. Bootstrap置信区间

3. 操纵检验、注意力检验

- analysis_method_cn：PLS-SEM和中介检验。

- main_result_cn：短暂分享显著降低数据收集、数据传播和身份滥用担忧，且这些担忧完全中介披露意向；身份披露担忧、机构隐私担忧和自我呈现意向不被显著影响。

- argumentative_role_cn：用主观构念补充客观行为证据，确认隐私机制而非其他心理机制。

- remaining_uncertainty_cn：在线实验测量的是披露意向而非真实匹配行为；仍需说明哪些用户更受影响。

- link_to_next_phase_cn：进入异质性分析，用现场数据检验隐私敏感用户是否获益更多。

##### evidence_pointers

1. Section 5.3

2. Table 16

3. Figure 5

4. Online Appendix E

#### 6. 异质性与稳健性检验

- order：6

- name_cn：异质性与稳健性检验

- question_cn：短暂分享的效果是否对隐私敏感用户更强，并且对不同的隐私敏感性代理是否稳健？

- inputs_and_setting_cn：现场实验数据；PhotoWallFace作为主要隐私敏感性代理；ProfileFace作为稳健性代理。

- designed_or_compared_object_cn：在回归中加入Ephemeral×PhotoWallFace交互项；用ProfileFace重复交互分析。

- baseline_control_or_counterfactual_cn：照片墙中有人脸的发送者作为低隐私敏感参照。

##### objective_metrics

1. 交互项系数及其显著性

- analysis_method_cn：OLS交互项回归；在线性稳健性检验中用替换代理变量。

- main_result_cn：Ephemeral×PhotoWallFace在NumPhoto、NumFace、NumMatch和Ln(SumMsgFromReceiver)上均显著为负；ProfileFace结果相似。

- argumentative_role_cn：支持隐私增强机制，并界定设计的受益边界。

- remaining_uncertainty_cn：仅展示了对隐私敏感的发送者效应更强，未直接测量其实时主观担忧；对接收者行为、线下结果和跨情境推广仍未检验。

- link_to_next_phase_cn：这些边界和局限进入讨论部分，转化为贡献与未来研究。

##### evidence_pointers

1. Section 5.4

2. Table 17

3. Online Appendix F

## 各部分修辞架构

### abstract_moves

1. PHENOMENON

2. PRACTICAL_STAKES

3. DESIGN_FEATURE

4. STUDY_OVERVIEW

5. RESULT

6. MECHANISM

7. CONTRIBUTION

### introduction_moves

1. CONTEXT

2. PHENOMENON

3. PRIOR_KNOWLEDGE

4. MECHANISM

5. PRACTICAL_STAKES

6. LIMITATION

7. WHY_GAP_MATTERS

8. REQUIREMENT

9. DESIGN_FEATURE

10. RQ_OR_OBJECTIVE

11. THEORY_INTRO

12. STUDY_OVERVIEW

13. RESULT

14. BOUNDARY_CONDITION

15. CONTRIBUTION

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE

2. LIMITATION

3. GAP

4. THEORY_INTRO

5. THEORY_PROPOSITION

6. MECHANISM

7. REQUIREMENT

8. HYPOTHESIS_OR_PROPOSITION

### artifact_design_moves

1. DESIGN_FEATURE

2. REQUIREMENT

3. METHOD_JUSTIFICATION

4. BENCHMARK_OR_CONTRAST

### evaluation_moves

1. STUDY_OVERVIEW

2. METHOD_JUSTIFICATION

3. BENCHMARK_OR_CONTRAST

4. RESULT

5. ROBUSTNESS_OR_BOUNDARY_TEST

6. TRANSITION

### discussion_and_contribution_moves

1. RESULT

2. CONTRIBUTION

3. BOUNDARY_CONDITION

4. LIMITATION_AND_FUTURE

## 理论/知识到设计的翻译

### 知识/理论基础

1. 隐私管理文献（经济学、隐私控制、PETs）

2. 社会隐私边界理论（Altman、Petronio、沟通隐私管理）

3. 短暂分享与社会媒体文献（Snapchat; Xu et al.; Hofstetter et al.; Bayer et al.）

4. 线上约会冷启动与匹配市场文献（Bapna et al.; John et al.; Chen 2021）

5. 信号传递与不确定性削减理论（Berger and Calabrese; John et al. 2016）

6. 平台用户访谈和预测试提供的领域知识

- 理论—设计耦合：direct

- 耦合判定理由：作者先从社会隐私担忧机制出发推导设计需求：临时性、不可追溯性；再选择短暂照片上传作为制品，并在现场实验中直接比较短暂与持久设计；在线实验又测量了这些理论构念。理论在问题定义、设计选择和机制检验中都起到前瞻性作用。

- 理论到设计翻译链：社会隐私担忧（数据收集、传播、身份披露、身份滥用）→用户不敢附照→需要降低接收者永久占有和滥用信息的能力→短暂分享设计（自动消失、禁止下载/截图）→发送者感知隐私风险下降→更愿意附个人照片/人脸→接收者收到可信信号、不确定性下降→更可能接受匹配并互动→匹配与互动结果改善。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：社会隐私担忧会阻止用户在陌生人面前披露个人照片。

- mechanism_cn：担心接收者会存储、转发、滥用照片，所以不愿附照；降低这些担忧会提高披露意愿。

- design_requirement_cn：在匹配请求阶段提供一种让信息对接收者短暂可见且不可追溯的设计。

- artifact_choice_cn：治疗组可上传“短暂照片”（阅后即焚、禁止下载/截图），对照组只能上传持久照片。

- evaluated_contrast_cn：治疗组vs对照组在是否附照片、是否含人脸、匹配数和接收者消息上的差异。

- objective_result_cn：NumPhoto增加52.1%，NumFace增加61.6%，NumMatch增加3.3%，Ln(SumMsgFromReceiver)增加4.6%。

##### evidence_pointers

1. Section 3.2

2. Figures 2 and 3

3. Section 5.1

4. Tables 5–7

#### 2. 2

- theory_or_knowledge_claim_cn：披露敏感个人信息会向接收者发送可信、真诚的信号，减少不确定性。

- mechanism_cn：附有人脸的照片增加接收者信任和好感，降低继续互动门槛。

- design_requirement_cn：将照片披露放进匹配请求发送页面，使披露行为可被接收者观察到。

- artifact_choice_cn：在请求页面提供照片上传按钮；照片随匹配请求一起发送。

- evaluated_contrast_cn：有照片请求vs无照片请求（由治疗引起的差异）以及治疗对接收者回应的影响。

- objective_result_cn：顺序中介Ephemeral→NumPhoto→NumMatch→NumMsgFromReceiver的间接效应显著；直接路径不显著。

##### evidence_pointers

1. Section 5.2.1

2. Figure 4

#### 3. 3

- theory_or_knowledge_claim_cn：短暂分享在社交媒体中可能引发良性或毒性去抑制。

- mechanism_cn：如果治疗只是让对方更大胆或更失控，照片情绪、合成程度、露骨内容应有差异。

- design_requirement_cn：需要排除内容变化作为解释。

- artifact_choice_cn：对发送照片做情绪、合成、露骨内容分类；用新奇交互项和接收者特征对比。

- evaluated_contrast_cn：治疗组与对照组在良性去抑制、毒性去抑制、面部吸引力、请求数量、对象选择上的差异。

- objective_result_cn：各项t检验均不显著；Ephemeral×T2交互不显著。

##### evidence_pointers

1. Section 5.2.2

2. Tables 8–15

#### 4. 4

- theory_or_knowledge_claim_cn：机构隐私担忧和自我呈现意向是替代机制。

- mechanism_cn：如果效应因为平台数据收集担忧降低或自我表达欲提高，则在线实验中应出现这些中介。

- design_requirement_cn：在在线实验中同时测量社会隐私、机构隐私和自我呈现意向。

- artifact_choice_cn：用相同流程的短暂照片视频vs持久照片视频作为刺激。

- evaluated_contrast_cn：各构念在两组间的间接效应。

- objective_result_cn：只有数据收集、传播、身份滥用担忧显著中介；身份披露、机构隐私、自我呈现不显著。

##### evidence_pointers

1. Section 5.3

2. Table 16

3. Figure 5

#### 5. 5

- theory_or_knowledge_claim_cn：隐私敏感用户受隐私担忧限制更强，因此短暂分享对其更有效。

- mechanism_cn：没有在照片墙放人脸的用户更在意隐私，治疗降低顾虑后边际效应更大。

- design_requirement_cn：按隐私敏感性划分子组。

- artifact_choice_cn：以PhotoWallFace为代理，加入Ephemeral×PhotoWallFace交互。

- evaluated_contrast_cn：有/无照片墙人脸的发送者之间治疗效应差异。

- objective_result_cn：交互项在四个结果上均显著为负；用ProfileFace稳健。

##### evidence_pointers

1. Section 5.4

2. Table 17

3. Online Appendix F

## 评价逻辑

### evaluation_modes

1. 用户层面随机现场实验（between-subjects）

2. OLS回归加稳健标准误和进入日期虚拟变量

3. 无模型均值比较

4. 顺序中介分析（PROCESS, 5000次bootstrap）

5. 备择机制排除的t检验和交互项检验

6. 基于计算机视觉的照片内容分类与面部吸引力预测

7. 在线实验与PLS-SEM心理机制检验

- why_these_evaluations_cn：首先需要因果识别，所以采用平台中的随机现场实验；然后需要把总效应分解为行为机制，所以用顺序中介；接着需要排除常见替代解释，所以检查请求量、对象选择、新奇效应和内容变化；最后需要把行为机制追溯到心理构念，所以补充在线实验和PLS-SEM。这些评价由外到内、由行为到心理逐层递进。

- benchmark_and_contrast_chain_cn：核心反事实是持久照片上传，这让效应归因于“短暂性”而非“新增照片功能”。在机制部分，对照组不仅提供反事实，还是排除替代解释的参照：请求量无差异、接收者特征无差异、图片内容无差异、新奇交互不显著；在线实验中持久照片条件又作为心理构念层面的反事实。最终，异质性交互把“隐私敏感”作为边界对比条件。

### claim_evidence_ledger

#### 1. 短暂分享增加个人照片披露。

- claim_cn：短暂分享增加个人照片披露。

- evidence_cn：治疗组NumPhoto和NumFace显著增加，且转换为52.1%和61.6%的相对提升。

#### 2. 短暂分享增加匹配数和接收者互动。

- claim_cn：短暂分享增加匹配数和接收者互动。

- evidence_cn：NumMatch增加3.3%，Ln(SumMsgFromReceiver)增加4.6%。

#### 3. 匹配和互动效应由披露增加驱动。

- claim_cn：匹配和互动效应由披露增加驱动。

- evidence_cn：顺序中介路径Ephemeral→NumPhoto→NumMatch→NumMsgFromReceiver的95%CI不包含0；直接路径不显著。

#### 4. 短暂分享通过降低部分社会隐私担忧提高披露意向。

- claim_cn：短暂分享通过降低部分社会隐私担忧提高披露意向。

- evidence_cn：在线实验中数据收集、传播和身份滥用担忧显著下降并完全中介披露意向；身份披露、机构隐私和自我呈现不显著。

#### 5. 隐私敏感用户获益更多。

- claim_cn：隐私敏感用户获益更多。

- evidence_cn：Ephemeral×PhotoWallFace在四个结果上均显著为负；ProfileFace替代后保持一致。

#### 6. 替代解释不成立。

- claim_cn：替代解释不成立。

- evidence_cn：请求页面浏览量和请求数无差异；追求对象特征无差异；Ephemeral×T2不显著；良性/毒性去抑制和面部吸引力无差异。

- internal_validity_strategy_cn：随机化分配；随机化检查；实验期间无其他实验；平台调节社区防止讨论治疗；进入日期虚拟变量控制时间异质性；多重替代解释排除；时间窗口交互排除新奇效应；在线实验用同一视频刺激仅替换短暂/持久属性。

- external_validity_strategy_cn：在真实约会平台、超过7万名真实用户中进行，测量实际行为而非自我报告；实验场景与平台流程紧密一致；在线实验在中国进行以匹配现场平台用户背景；平台在实验后将该功能推广到全部用户；同时也承认单一平台和特定文化背景的限制。

- what_is_not_actually_tested_cn：接收者层面的感知和行为没有直接测量；短暂分享是否真的降低接收者留存/滥用照片的客观概率没有被直接追踪；身份披露担忧未被缓解；线下约会结果未检验；消息文本内容未分析；实验只覆盖18天，未观测长期效应；对社交网络或非约会情境的外推未被检验。

## 贡献闭环

- technical_claim_cn：短暂分享上传设计在真实约会平台上提升了用户的照片披露、匹配数量和接收者消息量。

- artifact_claim_cn：短暂性本身，而非“新增照片上传功能”，导致了改进；与持久照片对照组相比，治疗组效应显著。

- mechanism_claim_cn：短暂分享通过降低发送者对数据收集、数据传播和身份滥用的隐私担忧，提高披露意愿；在行为上通过披露增加推动匹配和互动。

- boundary_claim_cn：效应在隐私敏感发送者中更强；身份披露担忧未被该设计缓解；效果是在陌生人求偶匹配的线上约会情境中检验的。

- reusable_design_knowledge_cn：临时性、不可追溯性可以成为隐私增强设计的核心原则；平台可按用户隐私敏感性进行个性化；该设计可扩展到文本、音频、视频等其他私密信息。

- theoretical_contribution_cn：将隐私增强设计从限制信息流转向鼓励信息流；扩展短暂分享文献到陌生人匹配与下游结果；把个人信息价值从算法化利用延伸到用户间点对点披露。

- how_discussion_closes_intro_gap_cn：讨论重新回到冷启动和隐私担忧，说明短暂分享通过降低社会隐私担忧鼓励披露，进而缓解冷启动；强调平台已实际采用该功能，呼应引言中“需要新型设计”的缺口。

- overclaim_or_unsupported_leaps_cn：现场实验没有直接测量发送者主观隐私担忧，而在线实验只测量披露意向，两者之间存在一定推断跳跃；“完全中介”基于观察数据的中介分析，可能过于绝对；实验中多个UI元素同时变化，未能单独分离哪一个元素最重要；对“短暂性”的机制辨别依赖对照组，但没有检验其他可能的短暂性属性。

## 句级写作动作图谱

### 1. P1 S1–S2

- order：1

- section：Introduction

- locator：P1 S1–S2

- move_code：CONTEXT

- paraphrase_cn：在线约会平台如Bumble、Tinder和Coffee Meets Bagel已成为寻找约会对象的重要渠道，其基本功能是帮助用户匹配和开始沟通。

- rhetorical_function_cn：把研究对象放入大众熟悉且重要的数字市场。

- depends_on_cn：无需前置。

- sets_up_cn：为后续指出平台面临的问题作背景。

- evidence_pointer：Introduction, first paragraph

### 2. P1 S3–S4

- order：2

- section：Introduction

- locator：P1 S3–S4

- move_code：PRACTICAL_STAKES

- paraphrase_cn：线上约会趋势达到高点，约40%年轻人通过网络认识伴侣，全球用户预计超过4.4亿。

- rhetorical_function_cn：强调平台规模和社会重要性，增加研究紧迫感。

- depends_on_cn：承接在线约会的普及背景。

- sets_up_cn：让后续冷启动问题显得代价更大。

- evidence_pointer：Introduction, first paragraph

### 3. P2 S1

- order：3

- section：Introduction

- locator：P2 S1

- move_code：PHENOMENON

- paraphrase_cn：关键挑战是冷启动问题：发送方在匹配初期可能隐瞒个人信息，使双方难以连接和沟通。

- rhetorical_function_cn：引入全文要解决的核心现象。

- depends_on_cn：基于在线约会平台的匹配功能背景。

- sets_up_cn：为隐私担忧和披露缺失的讨论做铺垫。

- evidence_pointer：Introduction, second paragraph

### 4. P2 S2

- order：4

- section：Introduction

- locator：P2 S2

- move_code：PHENOMENON

- paraphrase_cn：许多用户省略自己照片、身高、职业或性取向等个人信息。

- rhetorical_function_cn：用具体行为举例说明冷启动现象。

- depends_on_cn：定义冷启动问题之后。

- sets_up_cn：说明问题在平台上有广泛表现。

- evidence_pointer：Introduction, second paragraph

### 5. P2 S3

- order：5

- section：Introduction

- locator：P2 S3

- move_code：MECHANISM

- paraphrase_cn：隐瞒信息会使匹配请求被视为不真实或不值得信任，降低匹配成功机会。

- rhetorical_function_cn：解释冷启动为什么导致坏结果。

- depends_on_cn：依赖用户隐瞒信息的现象。

- sets_up_cn：为披露行为作为关键机制作准备。

- evidence_pointer：Introduction, second paragraph

### 6. P2 S4

- order：6

- section：Introduction

- locator：P2 S4

- move_code：MECHANISM

- paraphrase_cn：缺乏个人信息披露也会使匹配后双方难以保持互动。

- rhetorical_function_cn：把冷启动的后果从匹配延伸到匹配后互动。

- depends_on_cn：承接匹配被拒的后果。

- sets_up_cn：为使用接收者消息量作为结果变量埋下伏笔。

- evidence_pointer：Introduction, second paragraph

### 7. P3 S1

- order：7

- section：Introduction

- locator：P3 S1

- move_code：PHENOMENON

- paraphrase_cn：个人信息披露不足部分源于隐私担忧，即担心数据被公司、政府或他人使用。

- rhetorical_function_cn：引入现象背后的机制。

- depends_on_cn：冷启动现象已经建立。

- sets_up_cn：为隐私增强设计提供理论靶点。

- evidence_pointer：Introduction, third paragraph

### 8. P3 S2

- order：8

- section：Introduction

- locator：P3 S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：在线约会中的隐私担忧很普遍，用户担心个人身份被传播、窃取或用于诈骗和钓鱼。

- rhetorical_function_cn：引用既有知识和平台现实支持隐私担忧的存在。

- depends_on_cn：隐私担忧定义之后。

- sets_up_cn：强化设计需要降低隐私风险的方向。

- evidence_pointer：Introduction, third paragraph

### 9. P3 S3

- order：9

- section：Introduction

- locator：P3 S3

- move_code：PRACTICAL_STAKES

- paraphrase_cn：信息泄露还可能危及用户人身安全。

- rhetorical_function_cn：把隐私担忧从效率问题提升到安全层面。

- depends_on_cn：隐私滥用的例子。

- sets_up_cn：使引入隐私保护设计更具现实必要性。

- evidence_pointer：Introduction, third paragraph

### 10. P3 S4

- order：10

- section：Introduction

- locator：P3 S4

- move_code：MECHANISM

- paraphrase_cn：隐私担忧让用户在匹配初期保留个人信息，这阻碍信任建立，压缩聊天话题，并可能阻碍互动。

- rhetorical_function_cn：把隐私担忧与冷启动后果连成一条因果链。

- depends_on_cn：前面对隐私担忧的叙述。

- sets_up_cn：明确设计需要同时解决隐私和披露。

- evidence_pointer：Introduction, third paragraph

### 11. P3 S5

- order：11

- section：Introduction

- locator：P3 S5

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：GDPR等法规不允许平台强制用户披露个人信息。

- rhetorical_function_cn：说明为什么平台单靠规则压迫解决不了问题。

- depends_on_cn：隐私担忧的因果链。

- sets_up_cn：引出设计干预的必要性。

- evidence_pointer：Introduction, third paragraph

### 12. P3 S6

- order：12

- section：Introduction

- locator：P3 S6

- move_code：REQUIREMENT

- paraphrase_cn：因此迫切需要既能鼓励自愿披露又不过度牺牲隐私保护的平台设计。

- rhetorical_function_cn：从现实需要提炼出设计要求。

- depends_on_cn：法规限制和隐私担忧的讨论。

- sets_up_cn：为提出短暂分享设计提供逻辑入口。

- evidence_pointer：Introduction, third paragraph

### 13. P4 S1

- order：13

- section：Introduction

- locator：P4 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：作者提出短暂分享作为隐私增强的自我披露机制，并定义其内涵是分享内容在接收后很快不可见且不可追溯。

- rhetorical_function_cn：给出本文的核心设计答案。

- depends_on_cn：前面的设计要求。

- sets_up_cn：为后续现场实验定义治疗条件。

- evidence_pointer：Introduction, fourth paragraph

### 14. P4 S2

- order：14

- section：Introduction

- locator：P4 S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：与模糊、部分显示或允许用户控制可见性等设计相比，短暂分享允许不受限分享但严格限制接收者存储、传播和滥用信息。

- rhetorical_function_cn：通过与现有PETs比较来界定设计差异。

- depends_on_cn：短暂分享的定义。

- sets_up_cn：为贡献中强调“鼓励披露”的独特性埋下伏笔。

- evidence_pointer：Introduction, fourth paragraph

### 15. P4 S3

- order：15

- section：Introduction

- locator：P4 S3

- move_code：GAP

- paraphrase_cn：短暂分享虽已用于Snapchat等社交媒体，但在在线约会中是新应用，可能影响分享意愿以及匹配和互动等现实结果。

- rhetorical_function_cn：指出现有短暂分享文献未覆盖的领域。

- depends_on_cn：短暂分享设计介绍。

- sets_up_cn：为提出研究问题提供学术缺口。

- evidence_pointer：Introduction, fourth paragraph

### 16. P4 S4

- order：16

- section：Introduction

- locator：P4 S4

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：隐私担忧在不同情境有差异，隐私干预的效果也依赖情境，因此需要实证检验短暂分享能否缓解在线约会中的隐私担忧。

- rhetorical_function_cn：解释为什么不能直接照搬社交媒体的结论。

- depends_on_cn：短暂分享文献缺口。

- sets_up_cn：引出两个具体研究问题。

- evidence_pointer：Introduction, fourth paragraph

### 17. P5 S1

- order：17

- section：Introduction

- locator：P5 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：研究问题一是短暂分享如何影响个人信息披露、匹配结果和匹配后互动；研究问题二是其潜在机制。

- rhetorical_function_cn：正式宣布文章要回答的问题。

- depends_on_cn：前面的缺口论证。

- sets_up_cn：组织全文的实证结构。

- evidence_pointer：Introduction, fifth paragraph

### 18. P6 S1

- order：18

- section：Introduction

- locator：P6 S1

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：文章聚焦于陌生人寻求恋爱关系的匹配场景，因为冷启动问题在那里最明显，这与已有短暂分享研究关注已连接用户不同。

- rhetorical_function_cn：划定研究边界并突出创新点。

- depends_on_cn：研究问题提出之后。

- sets_up_cn：让理论不确定性变得明确。

- evidence_pointer：Introduction, sixth paragraph

### 19. P6 S2

- order：19

- section：Introduction

- locator：P6 S2

- move_code：THEORY_INTRO

- paraphrase_cn：理论上短暂分享对匹配结果的影响并不清楚：一方面鼓励自我披露可减少信息不对等并建立信任，另一方面也可能引发不当内容给接收者留下负面印象。

- rhetorical_function_cn：展示两种对立的理论预期，说明需要实证。

- depends_on_cn：研究边界设定。

- sets_up_cn：为现场实验和机制探讨提供理论张力。

- evidence_pointer：Introduction, sixth paragraph

### 20. P7 S1

- order：20

- section：Introduction

- locator：P7 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：作者与领先约会平台Summer合作，开展用户层级的随机现场实验，治疗组可上传短暂照片，对照组可上传持久照片。

- rhetorical_function_cn：预告核心实证设计。

- depends_on_cn：研究问题已提出。

- sets_up_cn：为数据与结果章节设定期望。

- evidence_pointer：Introduction, seventh paragraph

### 21. P8 S1

- order：21

- section：Introduction

- locator：P8 S1

- move_code：RESULT

- paraphrase_cn：治疗组发送更多个人照片和含人脸照片，并获得更多匹配和接收者消息。

- rhetorical_function_cn：在导言中给出主要结果摘要。

- depends_on_cn：实验设计预告。

- sets_up_cn：让读者知道答案已经存在。

- evidence_pointer：Introduction, eighth paragraph

### 22. P9 S1

- order：22

- section：Introduction

- locator：P9 S1

- move_code：MECHANISM

- paraphrase_cn：顺序中介显示匹配和互动效应由照片披露增加完全解释；在线实验显示短暂分享降低数据收集、传播和身份滥用担忧；还排除了良性或毒性去抑制等替代解释。

- rhetorical_function_cn：预告机制证据和替代解释排除。

- depends_on_cn：主要结果摘要。

- sets_up_cn：为结果章节的复杂分析提供地图。

- evidence_pointer：Introduction, ninth paragraph

### 23. P9 S2

- order：23

- section：Introduction

- locator：P9 S2

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：异质性测试显示短暂分享对隐私敏感发送者更有效。

- rhetorical_function_cn：在导言中预告边界条件。

- depends_on_cn：机制证据。

- sets_up_cn：为后文异质性分析做铺垫。

- evidence_pointer：Introduction, ninth paragraph

### 24. P10 S1

- order：24

- section：Introduction

- locator：P10 S1

- move_code：CONTRIBUTION

- paraphrase_cn：研究贡献于在线匹配平台隐私管理文献，提出并检验鼓励披露而非限制披露的短暂分享设计。

- rhetorical_function_cn：在导言末尾定位学术贡献。

- depends_on_cn：全部研究内容已预告。

- sets_up_cn：为讨论部分的贡献展开提供提纲。

- evidence_pointer：Introduction, tenth paragraph

### 25. Section 2.2, paragraph on PETs

- order：25

- section：Literature Review

- locator：Section 2.2, paragraph on PETs

- move_code：LIMITATION

- paraphrase_cn：多数PETs试图隐藏身份、内容和行为痕迹，但它们会减少可用个人信息，从而损害匹配市场效率。

- rhetorical_function_cn：指出现有隐私增强技术的副作用。

- depends_on_cn：隐私管理文献分类。

- sets_up_cn：为提出“鼓励披露的PETs”创造缺口。

- evidence_pointer：Section 2.2

### 26. Section 2.3.1

- order：26

- section：Literature Review

- locator：Section 2.3.1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：社交媒体的短暂分享可能促进毒性去抑制，如露骨内容、负面情绪和网络欺凌，也可能促进良性去抑制，如情绪化和非正式表达。

- rhetorical_function_cn：总结短暂分享文献中关于去抑制的知识。

- depends_on_cn：短暂分享在社交媒体的背景。

- sets_up_cn：为后来排除去抑制替代解释提供依据。

- evidence_pointer：Section 2.3.1

### 27. Section 2.3.1 and Table 1

- order：27

- section：Literature Review

- locator：Section 2.3.1 and Table 1

- move_code：MECHANISM

- paraphrase_cn：在社交媒体中短暂分享主要用于维系已有关系和缓解自我呈现担忧；在约会平台中它应作为隐私管理工具，在陌生人初始互动中降低隐私障碍。

- rhetorical_function_cn：把短暂分享的功能从社交网络迁移到约会情境。

- depends_on_cn：前面关于社交媒体短暂分享的总结。

- sets_up_cn：为理论化社会隐私担忧做铺垫。

- evidence_pointer：Section 2.3.1 and Table 1

### 28. Section 2.3.2, paragraph beginning with 'Building on the related literature'

- order：28

- section：Literature Review

- locator：Section 2.3.2, paragraph beginning with 'Building on the related literature'

- move_code：THEORY_INTRO

- paraphrase_cn：作者提出短暂分享可作为隐私增强设计，并将用户担忧概念化为社会隐私担忧，包含数据收集、数据传播、身份披露和身份滥用四个维度。

- rhetorical_function_cn：建立本文的理论基础。

- depends_on_cn：关于短暂分享和PETs的文献。

- sets_up_cn：为后续设计翻译和在线实验构念提供框架。

- evidence_pointer：Section 2.3.2 and Online Appendix A

### 29. Section 2.3.2, paragraph on initial interactions

- order：29

- section：Literature Review

- locator：Section 2.3.2, paragraph on initial interactions

- move_code：PHENOMENON

- paraphrase_cn：约会中的大部分关系在初始互动阶段结束；用户因隐私担忧而保留照片等个人信息，导致对方认为不可信，匹配失败并非因为不合适而是因为冷启动。

- rhetorical_function_cn：将社会隐私担忧与冷启动结果连接起来。

- depends_on_cn：社会隐私担忧四维概念。

- sets_up_cn：为短暂分享设计的作用机制提供问题场景。

- evidence_pointer：Section 2.3.2

### 30. Section 2.3.2, paragraph after the initial interaction paragraph

- order：30

- section：Literature Review

- locator：Section 2.3.2, paragraph after the initial interaction paragraph

- move_code：REQUIREMENT

- paraphrase_cn：短暂分享通过自动消失和禁止下载/截图，阻止接收者永久占有照片，从而降低传播和滥用风险，让发送者保持对信息的控制。

- rhetorical_function_cn：把理论机制转成设计属性。

- depends_on_cn：社会隐私担忧四维机制。

- sets_up_cn：为实验结果中的NumPhoto和NumFace预期提供依据。

- evidence_pointer：Section 2.3.2

### 31. Section 2.3.2, paragraph on disclosure signal

- order：31

- section：Literature Review

- locator：Section 2.3.2, paragraph on disclosure signal

- move_code：MECHANISM

- paraphrase_cn：披露个人照片向接收者发送可信和真诚的信号，减少不确定性，并降低接收者先披露的压力，所以接收者更可能接受请求并继续互动。

- rhetorical_function_cn：解释披露如何转化为匹配和互动结果。

- depends_on_cn：短暂分享降低担忧的机制。

- sets_up_cn：为匹配数和消息量作为结果变量提供理论依据。

- evidence_pointer：Section 2.3.2

### 32. End of Section 2.3.2

- order：32

- section：Literature Review

- locator：End of Section 2.3.2

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：据此预期：短暂分享通过降低社会隐私担忧促进披露，进而改善匹配结果和互动水平，缓解冷启动问题。

- rhetorical_function_cn：把整个因果链总结为可检验的主张。

- depends_on_cn：前述理论和机制。

- sets_up_cn：为实验章节设定待验证的命题。

- evidence_pointer：End of Section 2.3.2

### 33. Section 3.1

- order：33

- section：Randomized Field Experiment

- locator：Section 3.1

- move_code：CONTEXT

- paraphrase_cn：合作平台Summer使用基于问答的匹配机制：用户列出筛选问题，发送者回答并可能附照片，接收者决定是否批准。

- rhetorical_function_cn：描述实验现场的具体平台流程。

- depends_on_cn：前文实验设计与问题。

- sets_up_cn：让读者知道实验操纵发生在匹配请求阶段。

- evidence_pointer：Section 3.1 and Figure 1

### 34. Section 3.2

- order：34

- section：Randomized Field Experiment

- locator：Section 3.2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：实验采用用户层面组间设计，用户在更新应用时被随机分配到短暂或持久照片组，并一直留在该组。

- rhetorical_function_cn：说明实验设计和分配机制。

- depends_on_cn：平台背景。

- sets_up_cn：为随机化检验和因果推断设下基础。

- evidence_pointer：Section 3.2

### 35. Section 3.2, UI manipulation paragraph

- order：35

- section：Randomized Field Experiment

- locator：Section 3.2, UI manipulation paragraph

- move_code：DESIGN_FEATURE

- paraphrase_cn：治疗组在请求页和弹窗中使用“短暂照片”文案、阅后即焚图标和功能解释句；对照组只显示普通照片上传。

- rhetorical_function_cn：具体描述治疗操纵的内容。

- depends_on_cn：短暂分享设计理念。

- sets_up_cn：为读者判断操纵有效性提供细节。

- evidence_pointer：Section 3.2 and Figures 2 and 3

### 36. Section 3.2, pilot tests

- order：36

- section：Randomized Field Experiment

- locator：Section 3.2, pilot tests

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：平台通过访谈和预测试确认用户理解短暂照片概念和刺激。

- rhetorical_function_cn：为操纵有效性提供前置证据。

- depends_on_cn：UI操纵描述。

- sets_up_cn：减少对操纵不能被理解的质疑。

- evidence_pointer：Section 3.2

### 37. Section 4.1

- order：37

- section：Data

- locator：Section 4.1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：数据来自随机系统、交易数据库、云端事件日志和第三方通信仓库；人脸是否出现由面部检测API判定并人工核对。

- rhetorical_function_cn：说明结果变量的数据来源和测量方法。

- depends_on_cn：实验设计。

- sets_up_cn：为后续变量表和回归分析提供操作细节。

- evidence_pointer：Section 4.1 and Tables 2 and 3

### 38. Section 4.2

- order：38

- section：Data

- locator：Section 4.2

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：随机化检验显示所有数值和分类协变量在两组间无显著差异。

- rhetorical_function_cn：支持随机分组的有效性。

- depends_on_cn：数据收集和变量定义。

- sets_up_cn：让后续回归可被解释为因果效应。

- evidence_pointer：Section 4.2 and Table 4

### 39. Section 4.3

- order：39

- section：Data

- locator：Section 4.3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：主回归用结果变量对治疗指示变量和协变量线性回归，并加入进入日期虚拟变量控制时间异质性。

- rhetorical_function_cn：给出估计方程和识别策略。

- depends_on_cn：随机化检验。

- sets_up_cn：为结果表的解读提供框架。

- evidence_pointer：Section 4.3, Equation (1)

### 40. Section 5.1.1

- order：40

- section：Results

- locator：Section 5.1.1

- move_code：RESULT

- paraphrase_cn：治疗显著增加NumPhoto和NumFace，效应量分别为52.1%和61.6%的相对提升。

- rhetorical_function_cn：报告第一个主结果：披露增加。

- depends_on_cn：主回归方程和协变量。

- sets_up_cn：为后续匹配和互动结果提供前置环节。

- evidence_pointer：Section 5.1.1 and Table 5

### 41. Section 5.1.2

- order：41

- section：Results

- locator：Section 5.1.2

- move_code：RESULT

- paraphrase_cn：治疗组获得更多匹配，对应3.3%的匹配提升。

- rhetorical_function_cn：报告第二个主结果：匹配增加。

- depends_on_cn：披露增加的结果。

- sets_up_cn：表明设计改善了下游匹配。

- evidence_pointer：Section 5.1.2 and Table 6

### 42. Section 5.1.3

- order：42

- section：Results

- locator：Section 5.1.3

- move_code：RESULT

- paraphrase_cn：治疗组接收者消息量显著更高，相对增加约4.6%。

- rhetorical_function_cn：报告第三个主结果：互动增加。

- depends_on_cn：匹配结果。

- sets_up_cn：说明冷启动问题得到缓解。

- evidence_pointer：Section 5.1.3 and Table 7

### 43. Section 5.2.1

- order：43

- section：Results

- locator：Section 5.2.1

- move_code：RESULT

- paraphrase_cn：顺序中介显示短暂分享先增加带照片请求，再增加匹配，再增加接收者消息；直接路径不显著。

- rhetorical_function_cn：把上游披露与下游结果连成因果链。

- depends_on_cn：主效应结果。

- sets_up_cn：为“披露增加是机制”提供核心证据。

- evidence_pointer：Section 5.2.1 and Figure 4

### 44. Section 5.2.2.1

- order：44

- section：Results

- locator：Section 5.2.2.1

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：治疗组与对照组在请求页面浏览量和匹配请求数上没有显著差异。

- rhetorical_function_cn：排除“只是更活跃”的替代解释。

- depends_on_cn：披露机制的中介结果。

- sets_up_cn：加强披露行为而非活动量是驱动因素。

- evidence_pointer：Section 5.2.2.1 and Table 8

### 45. Section 5.2.2.2

- order：45

- section：Results

- locator：Section 5.2.2.2

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：追求对象在年龄、教育、任期和热度上无显著差异，亦无多样性差异。

- rhetorical_function_cn：排除“选择不同对象”导致结果变化。

- depends_on_cn：请求量排除。

- sets_up_cn：把效应锁定在请求内容而非目标选择。

- evidence_pointer：Section 5.2.2.2 and Tables 9 and 10

### 46. Section 5.2.2.3

- order：46

- section：Results

- locator：Section 5.2.2.3

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：Ephemeral×T2交互在所有结果上不显著，说明效应没有随时间衰减。

- rhetorical_function_cn：排除新奇效应。

- depends_on_cn：主效应和中介。

- sets_up_cn：帮助把短期新奇与真实设计效应区分开来。

- evidence_pointer：Section 5.2.2.3 and Table 11

### 47. Section 5.2.2.4

- order：47

- section：Results

- locator：Section 5.2.2.4

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：治疗组与对照组在照片的情感中性度、合成度和正襟危坐比例上没有显著差异，说明良性去抑制不成立。

- rhetorical_function_cn：排除良性去抑制替代机制。

- depends_on_cn：短暂分享文献中的良性去抑制概念。

- sets_up_cn：与后文在线实验的隐私机制形成对照。

- evidence_pointer：Section 5.2.2.4 and Tables 12 and 13

### 48. Section 5.2.2.5

- order：48

- section：Results

- locator：Section 5.2.2.5

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：治疗组与对照组在露骨和裸照比例上没有显著差异，在线实验中对困扰内容的披露意向也无差异。

- rhetorical_function_cn：排除毒性去抑制替代机制。

- depends_on_cn：去抑制文献。

- sets_up_cn：证明短暂分享并未促使不当内容分享。

- evidence_pointer：Section 5.2.2.5 and Tables 14 and 15

### 49. Section 5.2.2.6

- order：49

- section：Results

- locator：Section 5.2.2.6

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：治疗组与对照组发送照片的面部吸引力预测分数无显著差异。

- rhetorical_function_cn：排除“短暂分享导致发送更美照片”的解释。

- depends_on_cn：面部吸引力预测模型。

- sets_up_cn：进一步支持效应来自披露数量而非内容质量。

- evidence_pointer：Section 5.2.2.6 and Online Appendix D

### 50. Section 5.3

- order：50

- section：Results

- locator：Section 5.3

- move_code：STUDY_OVERVIEW

- paraphrase_cn：为解释披露为何增加，作者在中国开展在线实验，测量社会隐私担忧、机构隐私担忧和自我呈现意向。

- rhetorical_function_cn：从行为机制转向心理机制。

- depends_on_cn：现场实验的披露中介。

- sets_up_cn：为心理机制结果提供方法说明。

- evidence_pointer：Section 5.3

### 51. Section 5.3.4

- order：51

- section：Results

- locator：Section 5.3.4

- move_code：RESULT

- paraphrase_cn：短暂分享显著降低数据收集、数据传播和身份滥用担忧，这三个担忧完全中介披露意向；身份披露担忧、机构隐私和自我呈现意向不显著。

- rhetorical_function_cn：给出心理机制的直接证据。

- depends_on_cn：在线实验设计和PLS-SEM。

- sets_up_cn：为把机制归结为社会隐私担忧提供支撑。

- evidence_pointer：Section 5.3.4, Table 16, and Figure 5

### 52. Section 5.4

- order：52

- section：Results

- locator：Section 5.4

- move_code：RESULT

- paraphrase_cn：Ephemeral×PhotoWallFace交互在披露、匹配和互动结果上都显著为负，说明无照片墙人脸的隐私敏感发送者获益更多。

- rhetorical_function_cn：报告异质性结果并界定边界条件。

- depends_on_cn：主效应和机制。

- sets_up_cn：为讨论中的隐私敏感性个性化建议提供依据。

- evidence_pointer：Section 5.4 and Table 17

### 53. Section 6.1

- order：53

- section：Discussion

- locator：Section 6.1

- move_code：RESULT

- paraphrase_cn：总结认为，短暂照片分享相对持久照片分享改善了匹配结果和匹配后互动，效应由披露增加驱动，且通过降低部分社会隐私担忧起作用。

- rhetorical_function_cn：把全文实证发现浓缩为可引用的结论。

- depends_on_cn：所有现场和在线实验结果。

- sets_up_cn：为贡献讨论提供事实基础。

- evidence_pointer：Section 6.1

### 54. Section 6.2, first contribution

- order：54

- section：Discussion

- locator：Section 6.2, first contribution

- move_code：CONTRIBUTION

- paraphrase_cn：研究扩展了在线匹配平台的隐私管理文献，率先测试一种减少隐私担忧但不阻碍有价值信息流动的隐私增强机制。

- rhetorical_function_cn：定位对隐私管理文献的贡献。

- depends_on_cn：研究结果。

- sets_up_cn：与现有PETs的对比在讨论中展开。

- evidence_pointer：Section 6.2

### 55. Section 6.2, second contribution

- order：55

- section：Discussion

- locator：Section 6.2, second contribution

- move_code：CONTRIBUTION

- paraphrase_cn：研究扩展了短暂分享文献：从已连接用户到陌生人匹配，从内容分享行为到匹配数和互动等下游结果，从缓解自我呈现担忧到增强隐私并促进披露。

- rhetorical_function_cn：在短暂分享文献中建立本文的新颖性。

- depends_on_cn：对比社交媒体与约会情境的差异。

- sets_up_cn：强化“短暂分享可成为隐私增强设计”这一贡献。

- evidence_pointer：Section 6.2

### 56. Section 6.2, third contribution

- order：56

- section：Discussion

- locator：Section 6.2, third contribution

- move_code：CONTRIBUTION

- paraphrase_cn：研究还关联个人信息价值文献，展示用户自愿分享个人信息在点对点互动中创造价值，而非只通过算法推荐实现价值。

- rhetorical_function_cn：把隐私与披露讨论提升到信息价值层面。

- depends_on_cn：披露导致匹配和互动改善的机制。

- sets_up_cn：为平台管理者理解设计价值提供理论背景。

- evidence_pointer：Section 6.2

### 57. Section 6.3

- order：57

- section：Discussion

- locator：Section 6.3

- move_code：CONTRIBUTION

- paraphrase_cn：平台可实施短暂分享设计，该模式也适用于其他私密信息；实验结束后平台已将该功能推广给所有用户。

- rhetorical_function_cn：提出可操作的管理建议并给出外部采纳证据。

- depends_on_cn：研究结果和边界。

- sets_up_cn：让贡献不只停留在理论层面。

- evidence_pointer：Section 6.3

### 58. Section 6.4

- order：58

- section：Discussion

- locator：Section 6.4

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：研究未检验接收者行为、消息内容、线下互动和跨情境推广；未来可进一步做个性化设计。

- rhetorical_function_cn：承认研究边界并指明后续方向。

- depends_on_cn：全文设计和方法局限。

- sets_up_cn：以谦虚语气保护贡献不被过度泛化。

- evidence_pointer：Section 6.4

## 写作技术

- gap_construction_cn：先描述冷启动现象和隐私担忧，再指出GDPR禁止强制披露，从而把缺口从“技术效率不足”转为“需要一种同时保护隐私与促进披露的设计”；随后用“多数PETs减少信息可用性”凸显现有制品不能解决约会匹配问题。

- signposting_cn：在引言末尾预告两个研究问题和多层证据；在每章开头用总起句说明任务；在结果部分用“First...Next...Finally...”推进，并明确“Having estimated total effects, we next...”。

- transition_logic_cn：从总效应到行为中介，再到排除替代解释，再到在线实验的心理机制，最后到异质性和稳健性；每步以“为什么还需要这一步”连接，使读者接受新增分析的合理性。

- claim_evidence_rhythm_cn：先报告主效应系数并换算百分比，建立经济显著性；再用bootstrap中介检验机制；随后每个替代解释都用专门的t检验或交互项回应；在线实验则用PLS-SEM把构念层面的路径补齐；最后用异质性交互把边界条件嵌入回归。

- benchmark_narrative_cn：持久照片上传被描述为自然反事实：不是“无照片功能”，而是常见持久设计，因此效应归因于“短暂性”；在线实验中持久照片视频成为心理构念层面的对照；在排除分析中，持久组也被反复用作t检验比较对象。

- theory_return_cn：结果部分先呈现行为链路，讨论部分再把证据回接到“社会隐私担忧”和“披露信号”；在线实验的构念测量让作者能够在讨论中明确说效应来自数据收集、传播和身份滥用担忧，而非自我呈现或机构隐私。

- contribution_positioning_cn：把贡献放到三条文献线中：隐私增强设计（从限制披露到鼓励披露）、短暂分享（从社交媒体到约会匹配）、个人信息价值（从算法提取到用户间披露），每条都用“与已有研究不同”来定位。

- novelty_protection_cn：通过时间交互排除新奇效应；通过请求量和对象选择排除活跃度和选择偏移；通过去抑制和照片内容分类排除内容变化；通过面部吸引力排除质量差异；最后用在线实验排除机构隐私和自我呈现，从而将贡献锁定在短暂性降低社会隐私担忧这一机制。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：描述平台或市场中的冷启动现象，并把原因归到某类用户担忧或机制，说明为什么现有制度或技术不能解决。

- research_job_cn：找到现实问题、文献缺口和设计需求的交集。

- required_evidence_cn：平台数据或公开报告显示问题严重；法规或文献显示强制披露不可行。

- transition_to_next_cn：由需求引出具体设计概念。

#### 2. 2

- step：2

- writing_job_cn：引入理论或知识基础，定义关键构念，并把理论命题翻译成设计要求。

- research_job_cn：明确理论机制和设计属性之间的对应关系，可通过访谈或预测试验证理解。

- required_evidence_cn：理论命题清晰；设计属性能够被用户理解。

- transition_to_next_cn：进入现场实验或受控实验来检验设计。

#### 3. 3

- step：3

- writing_job_cn：描述实验平台、随机分配、操纵界面和变量构建，报告随机化检查。

- research_job_cn：在实际产品中实施随机现场实验，收集行为痕迹和结果数据。

- required_evidence_cn：随机化平衡；治疗组和对照组流程相同；数据质量可靠。

- transition_to_next_cn：估计总效应。

#### 4. 4

- step：4

- writing_job_cn：报告总效应，并对每个结果给出经济显著性换算。

- research_job_cn：估计治疗对各层结果变量的影响。

- required_evidence_cn：显著且稳健的系数；效应量可解释。

- transition_to_next_cn：探索机制。

#### 5. 5

- step：5

- writing_job_cn：用中介分析把上游设计与下游结果连接起来，并逐项排除替代解释。

- research_job_cn：运行中介分析；利用平台日志、图像内容和时间维度排除活跃度、对象选择、新奇效应和内容变化。

- required_evidence_cn：中介路径显著；替代解释的检验不显著。

- transition_to_next_cn：补一个构念层面的机制实验。

#### 6. 6

- step：6

- writing_job_cn：用在线实验或问卷测量理论构念，验证机制并排除其他心理机制。

- research_job_cn：设计刺激与现场一致，测量多个理论机制。

- required_evidence_cn：目标构念路径显著；替代构念不显著。

- transition_to_next_cn：做异质性和稳健性检验。

#### 7. 7

- step：7

- writing_job_cn：用交互项展示边界条件，讨论贡献、管理含义和局限。

- research_job_cn：用代理变量识别受影响更大的子群；补充稳健性检验。

- required_evidence_cn：交互项方向符合理论预期；替换代理后结果一致。

- transition_to_next_cn：回到引言缺口并总结贡献。

### most_transferable_moves_cn

1. 用冷启动或初始互动失败作为现实问题入口

2. 把隐私担忧拆成多维度并转化为设计要求

3. 选择持久上传作为自然反事实，突出“短暂性”而非“新增功能”

4. 用顺序中介把上游披露与下游结果连接

5. 在排除替代解释时同时使用平台日志、计算机视觉和在线实验

6. 用交互项显示边界条件和受益人群

7. 把贡献放在多条文献线中分别定位

### resource_intensive_or_nonstandard_parts_cn

1. 与真实平台合作进行用户层面随机现场实验，需要产品开发和平台信任

2. 超过7万名用户的流量和18天实验期

3. 平台专门的UI操纵（按钮、弹窗、图标、解释句）

4. 端到端事件日志、交易数据和第三方消息数据

5. 面部检测API、露骨内容分类器和面部吸引力预测模型

6. 平台社区调节以避免用户讨论治疗

7. 在中国招聘参与者的在线实验和预测试

### what_not_to_copy_superficially_cn

1. 若没有随机控制，不能把相关披露增加说成短暂分享的因果效应

2. 若没有持久照片对照组，不能把效应归因于短暂性

3. 若没有中介检验，不能宣称披露是机制

4. 若没有排除新奇和内容变化，不能把效果归为隐私机制

5. 若在线实验没有测量替代构念，不能断言机构隐私和自我呈现不重要

6. 若没有异质性交互，不能声称对隐私敏感者更有效

- single_best_description_of_the_routine_cn：从现实冷启动出发，用理论把隐私担忧翻译成短暂分享设计，再通过平台随机现场实验建立因果主效应，用中介和排除法锁定行为机制，用在线实验补上心理机制，最后用异质性和稳健性框定边界。

## 分析边界

文章OCR中部分希腊字母和符号被替换为�，但关键系数和表格仍可辨认；图1-3的界面截图无法从文本中直接读取；多个在线附录的具体测量条目和诊断数据未包含在提供的文本中，因此对在线实验的细节判断依赖正文摘要。
