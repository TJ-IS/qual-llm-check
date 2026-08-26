# The Fog of Warnings: How Non-Security-Related Notifications Diminish the Efficacy of Security Warnings

- 作者：Anthony Vance; Dave Eargle; C. Brock Kirwan; Bonnie Brinton Anderson; Jeffrey L. Jenkins
- 年份 / 期刊：2025 / MIS Quarterly
- DOI：10.25300/misq/2025/18531
- 源文件：27642_2025_the-fog-of-warnings-how-non-security-related-notifications-diminish-the-efficacy-of-security-war.md
- 论文主类型：theory_derived_artifact_experiment
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.88

## 文章级论证概况

- 核心问题：用户对安全警告的习惯性忽视，是否以及如何由频繁出现的非安全通知通过泛化习服机制传导至从未见过的安全警告？应该如何设计警告以减少这种泛化？

- 制品与设计：核心制品是一套浏览器中的警告/通知刺激与交互设计：高重复绩效通知；四类Firefox安全警告（两类视觉相似、两类视觉不同）；fMRI中按钮、按住滑杆、拖拽三类交互模式；Experiment 3在视觉外观基本一致的通知/警告中分别启用按钮或滑杆。

- 客观结果：实验1：经过14次通知后，警告被忽视概率为1.62倍，反应时间约22%更快；视觉相似警告有显著泛化，视觉不相似警告无显著泛化。fMRI实验：腹侧视觉流对通知产生习服；按钮式警告的激活显著低于紧邻通知，滑杆/拖拽式警告的激活显著高于通知；novel foil激活高于通知，排除疲劳。实验3：视觉外观恒定条件下，按钮警告在30次暴露后被忽视率2.77倍且反应快32%，滑杆警告无显著泛化。

- 核心贡献：作者声称首次在IS中引入泛化习服概念，证明习惯忽视通知会无意识传导到从未见过的安全警告，即使用户能意识区分；并基于习服双过程理论与图式理论开发视觉外观和交互模式两类可实施的警告设计干预，降低泛化并提高依从性；同时挑战了UI一致性原则在安全警告场景中的适用性。

- 整篇论证链：文章先指出安全警告忽视是严重安全问题，且常见通知与警告在视觉/交互上一致导致用户把警告当作通知忽视；随后引入神经生物学的泛化习服，解释为何用户即使能意识区分也会无意识忽视从未见过的相似警告。作者据此提出三个假设：通知习服泛化到视觉相似警告(H1)；视觉差异减少泛化(H2)；交互模式差异减少泛化(H3)。实验1用在线现场实验证实H1/H2并排除疲劳；补充MST证明意识区分能力存在；实验2用fMRI在神经层面证实H1并排除疲劳和认知投入，同时支持H3；实验3在保持视觉外观恒定下证明仅交互模式改变即可减少泛化(H3)。讨论把这些结果提升为对泛化习服的理论贡献和对警告设计/UI一致性原则的实践含义。

## 类型与写作弧线判定

- 论文主类型判定：文章不是单纯的多方法拼盘，而是由习服双过程理论和图式理论前瞻性地推导出警告设计差异（视觉相似性、交互模式），再通过两个现场实验和一个fMRI实验直接检验这些理论驱动的设计干预。

- 主导写作弧线判定：全文遵循：现实问题（用户忽视警告）→理论（泛化习服、双过程理论、图式理论）→设计差异（视觉外观、交互模式）→三阶段实验检验→讨论重新回到研究问题并总结理论贡献和边界条件。

## 研究开展程序

- study_or_phase_count：4

- 研究阶段总序列：实验1先在真实浏览器线上环境中建立泛化习服的行为证据，并证明视觉差异干预；随后用MST补充实验排除被试不能意识区分通知与警告的替代解释；实验2用fMRI在神经层面复现泛化、排除疲劳和认知投入，并初步支持交互模式干预；实验3再回到线上现场，通过视觉外观恒定设计把交互模式效果从视觉外观中分离出来。四个阶段依次回答：是否存在泛化→是否意识层面可区分→是否神经层面真实且非竞争解释→是否是交互模式本身导致。

### studies_or_phases

#### 1. 实验1：浏览器在线现场实验（H1、H2）

- order：1

- name_cn：实验1：浏览器在线现场实验（H1、H2）

- question_cn：在真实浏览器情境中，反复出现的非安全通知是否会让用户更快、更可能忽视从未见过的安全警告；惩罚视觉差异是否会减少这种泛化？

- inputs_and_setting_cn：609名美国MTurk参与者；Firefox浏览器；Batman图像分类掩护任务；真实浏览器HTML5通知和四类Firefox安全警告，以及novel foil；暴露位置1或15。

- designed_or_compared_object_cn：四类Firefox安全警告：两类与绩效通知视觉相似（权限请求、扩展安装）、两类视觉不同（保存可执行文件、打开宏）；另有novel foil。比较警告单独出现与在14次通知后出现。

- baseline_control_or_counterfactual_cn：同一警告在Exposure 1 vs Exposure 15；novel foil用于排除疲劳；额外第11组只有通知；事后concern和MST用于排除无法区分。

##### objective_metrics

1. warning disregard 二值

2. reaction time（取自然对数）

3. perceived concern

4. MST正确率

- analysis_method_cn：线性回归（ln RT）、logistic回归（disregard），以暴露位置/警告类型作预测变量和交互项；单尾检验；补充MST卡方检验。

- main_result_cn：通知诱发习服（14次后反应快24%）；警告在通知后出现时被忽视概率1.62倍、RT约22%更短；视觉相似警告的忽视和RT有显著泛化，视觉不同警告无显著变化；novel foil无显著疲劳效应。

- argumentative_role_cn：在自然环境中为H1和H2提供行为证据，并建立泛化习服的操作化测量；是后续神经证据的起点。

- remaining_uncertainty_cn：不能排除更快反应来自认知投入增加；不能分离交互模式与视觉外观的影响；需要证明被试不是真的分不清通知与警告。

- link_to_next_phase_cn：留下认知投入和神经机制问题，引出fMRI实验；意识区分问题由补充MST处理。

##### evidence_pointers

1. Experiment 1 section

2. Table 2

3. Table 3

4. Table 4

5. Figure 6

6. Figure 7

7. Figure 5

#### 2. 补充实验：MST记忆区分稳健性检验

- order：2

- name_cn：补充实验：MST记忆区分稳健性检验

- question_cn：被试能否形成对绩效通知的记忆表征，并将它与实验1中四类安全警告区分开来？

- inputs_and_setting_cn：31名大学社区被试（30名有效）；实验室计算机；MST范式；刺激包括绩效通知、修改版通知、novel distractors和实验1的四类警告。

- designed_or_compared_object_cn：比较对绩效通知的'旧'反应、对安全警告的'新/相似'反应；随机呈现目标、相似刺激、新异刺激。

- baseline_control_or_counterfactual_cn：MST中的精确重复(targets)与相似刺激(lures)和全新刺激(distractors)相对照；chance=33%。

##### objective_metrics

1. 平均正确率

2. 对绩效通知/'old'反应比例

3. 对安全警告/'old'反应比例

4. Chi-square

- analysis_method_cn：t检验和卡方检验描述识别/区分能力。

- main_result_cn：总体正确率61.7%（chance 33%）；76.7%将绩效通知判为'旧'，0-13%将安全警告判为'旧'；说明被试在任务要求下能意识区分。

- argumentative_role_cn：排除'被试根本没有形成区分记忆'的替代解释，支撑'泛化发生在无意识层面'的核心主张。

- remaining_uncertainty_cn：只证明在明确要求区分时能做到，不证明在低任务需求下不会混淆。

- link_to_next_phase_cn：为fMRI中'意识可区分而神经层面仍泛化'的解释铺路。

##### evidence_pointers

1. Experiment 1: Ruling Out a Lack of Discrimination

2. Table 5

3. MST Procedure/Results

#### 3. 实验2：fMRI神经实验（H1、H3、排除竞争解释）

- order：3

- name_cn：实验2：fMRI神经实验（H1、H3、排除竞争解释）

- question_cn：泛化是否发生在神经层面？更快的警告反应是否由认知投入或疲劳解释？改变交互模式能否减少神经层面的泛化？

- inputs_and_setting_cn：25名大学被试；fMRI；Batman图像分类任务；组内重复测量；绩效通知、三类警告（按钮、按住滑杆、拖拽）、novel foil（日常物品图片）；约23-29分钟。

- designed_or_compared_object_cn：三类权限警告的交互模式：与通知相同的按钮点击、按住按钮移动滑杆、拖拽式移动滑杆；比较首次警告与其前一通知的激活，以及各类警告与通知的平均激活。

- baseline_control_or_counterfactual_cn：图像分类任务激活作为基线；novel foil作为疲劳对照；按钮式警告作为同模式对照；滑杆/拖拽作为异模式处理。

##### objective_metrics

1. BOLD激活（腹侧视觉流簇）

2. 任务行为反应时间（辅助）

- analysis_method_cn：fMRI一般线性模型和线性对比；t检验比较首次警告与前导通知、novel foil与通知、异模式警告与通知。

- main_result_cn：性能通知在腹侧视觉流等区域呈线性习服；首次按钮式警告激活显著低于前导通知（支持H1）；novel foil激活高于通知（排除疲劳）；滑杆/拖拽警告激活显著高于通知而按钮警告与通知无差异（支持H3）。

- argumentative_role_cn：提供神经层面的泛化证据；用脑激活模式排除疲劳和认知投入；初步验证交互模式干预。

- remaining_uncertainty_cn：交互模式改变伴随视觉外观改变，不能单独归因；fMRI用按键盒代替鼠标，模式操作与真实环境不完全一致。

- link_to_next_phase_cn：引出实验3，以视觉外观恒定设计分离交互模式效果。

##### evidence_pointers

1. Experiment 2 section

2. Figure 8

3. Figure 9

4. Figure 11

5. Figure 12

6. Appendix B Table B1

#### 4. 实验3：在线现场实验隔离交互模式效果（H3）

- order：4

- name_cn：实验3：在线现场实验隔离交互模式效果（H3）

- question_cn：在视觉外观基本恒定的条件下，仅改变警告的交互模式（按钮 vs 滑杆）是否仍能减少泛化习服？

- inputs_and_setting_cn：241名MTurk参与者，剔除7个极端反应时间后234名；Firefox；图像分类任务；绩效通知和权限警告；两者的视觉外观均同时包含按钮和滑杆，但只启用其中一个。暴露位置1或30。

- designed_or_compared_object_cn：按钮启用警告 vs 滑杆启用警告；警告在1次或29/30次通知后出现。

- baseline_control_or_counterfactual_cn：Exposure 1 vs Exposure 30；按钮启用作为与通知同交互模式的对照；滑杆启用作为异模式处理；视觉外观保持一致。

##### objective_metrics

1. warning disregard 二值

2. reaction time（ln）

- analysis_method_cn：logistic回归和线性回归，预测变量为警告类型及与Exposure 30的交互。

- main_result_cn：按钮启用警告在30次暴露后被忽视率2.77倍、RT快32%；滑杆启用警告在Exposure 1和30间无显著差异，支持H3。

- argumentative_role_cn：在保持视觉外观恒定的强对照下，确证交互模式是减少泛化的独立设计杠杆。

- remaining_uncertainty_cn：仍限定在浏览器+鼠标UI；滑杆本身的新异性/新颖性可能贡献部分效果；未测试长期效果。

- link_to_next_phase_cn：结果直接进入讨论，支撑RQ2的实践干预和理论贡献。

##### evidence_pointers

1. Experiment 3 section

2. Table 6

3. Table 7

4. Figure 13

5. Figure 14

6. Figure 15

## 各部分修辞架构

### abstract_moves

1. CONTEXT

2. PHENOMENON

3. THEORY_INTRO

4. MECHANISM

5. BOUNDARY_CONDITION

6. STUDY_OVERVIEW

7. RESULT

8. CONTRIBUTION

### introduction_moves

1. CONTEXT

2. PRACTICAL_STAKES

3. PHENOMENON

4. LIMITATION

5. PRIOR_KNOWLEDGE

6. GAP

7. THEORY_INTRO

8. MECHANISM

9. RQ_OR_OBJECTIVE

10. STUDY_OVERVIEW

11. CONTRIBUTION

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE

2. LIMITATION

3. GAP

4. WHY_GAP_MATTERS

5. THEORY_INTRO

6. THEORY_PROPOSITION

7. MECHANISM

8. HYPOTHESIS_OR_PROPOSITION

9. DESIGN_FEATURE

10. REQUIREMENT

### artifact_design_moves

1. DESIGN_FEATURE

2. REQUIREMENT

3. METHOD_JUSTIFICATION

4. BENCHMARK_OR_CONTRAST

5. STUDY_OVERVIEW

### evaluation_moves

1. METHOD_JUSTIFICATION

2. BENCHMARK_OR_CONTRAST

3. RESULT

4. ROBUSTNESS_OR_BOUNDARY_TEST

5. TRANSITION

### discussion_and_contribution_moves

1. CONTRIBUTION

2. MECHANISM

3. BOUNDARY_CONDITION

4. LIMITATION_AND_FUTURE

5. CONTRIBUTION

## 理论/知识到设计的翻译

### 知识/理论基础

1. dual-process theory of habituation (Groves & Thompson, 1970)

2. generalization of habituation (Rankin et al., 2009; Thompson & Spencer, 1966)

3. schema theory / muscle memory / procedural memory (Rumelhart, 1980; Krakauer & Shadmehr, 2006)

- 理论—设计耦合：direct

- 耦合判定理由：泛化习服和双过程理论直接推导出H1/H2中视觉相似/差异的假设，图式理论/肌肉记忆直接推导出H3中改变交互模式的设计，三类假设都被实验直接检验；不是事后解释。

- 理论到设计翻译链：高频通知建立心理模型→警告与通知视觉相似时自动匹配并抑制反应（泛化）→设计应使警告在首次出现时就与通知明显不同：视觉差异或交互模式差异→用曝光位置对比、fMRI激活和视觉恒定实验检验。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：双过程习服理论：重复刺激建立心理模型，相似刺激会匹配该模型并抑制反应，因此习服可以泛化。

- mechanism_cn：频繁出现的通知形成心理模型；与警告视觉相似时，大脑无意识匹配模型，减少注意和行为反应。

- design_requirement_cn：若警告与通知在视觉上相似，则不能依赖首次出现的自动注意；必须检验相似警告是否确实产生泛化。

- artifact_choice_cn：浏览器绩效通知；权限请求和扩展安装两类视觉相似的Firefox警告。

- evaluated_contrast_cn：警告单独出现 vs 警告在14次通知后出现；fMRI中首次按钮警告 vs 其紧邻前导通知。

- objective_result_cn：警告在通知后被忽视概率1.62倍、RT约22%更短；fMRI按钮警告激活显著低于前导通知。

##### evidence_pointers

1. Experiment 1 Table 3

2. Figure 6/7

3. Experiment 2 Testing H1

#### 2. 2

- theory_or_knowledge_claim_cn：泛化习服程度取决于刺激相似度；足够不同的新刺激会被当作新异刺激，恢复被抑制的反应。

- mechanism_cn：视觉上不同的警告与通知的心理模型不匹配，因此不会自动触发已习服的抑制。

- design_requirement_cn：安全警告应从视觉外观上与常见通知显著区分，尤其是在首次出现时。

- artifact_choice_cn：保存可执行文件、打开宏两类视觉不相似的Firefox警告。

- evaluated_contrast_cn：视觉相似警告与视觉不相似警告在Exposure 1 vs Exposure 15的忽视率和RT差异。

- objective_result_cn：视觉相似警告有显著泛化；视觉不相似警告无显著变化。

##### evidence_pointers

1. Experiment 1 Table 4

2. Figure 6/7

#### 3. 3

- theory_or_knowledge_claim_cn：图式理论：改变互动图式会迫使意识参与，打破肌肉记忆式的自动反应。

- mechanism_cn：点击关闭是通知的主导范式；如果警告改用滑杆/拖拽，用户不能依赖既有运动图式，必须注意界面并重新加工。

- design_requirement_cn：警告的交互模式应区别于通知的常规“click-to-dismiss”，以阻断自动反应。

- artifact_choice_cn：fMRI中的按住滑杆和拖拽式警告；Experiment 3中启用滑杆的权限警告，同时保持视觉外观与按钮版一致。

- evaluated_contrast_cn：按钮启用 vs 滑杆启用的警告；fMRI中同模式按钮警告 vs 异模式滑杆/拖拽警告。

- objective_result_cn：fMRI中异模式警告激活显著高于通知；Experiment 3中滑杆警告无显著泛化，按钮警告被忽视率2.77倍并RT快32%。

##### evidence_pointers

1. Experiment 2 Figure 12

2. Experiment 3 Table 7

3. Figure 14/15

## 评价逻辑

### evaluation_modes

#### 1. 1

- mode_cn：在线现场实验 + 组间暴露位置对照

- purpose_cn：在真实浏览器环境中测量警告忽视与RT，检验H1/H2/H3的行为表现。

#### 2. 2

- mode_cn：fMRI组内实验 + BOLD激活

- purpose_cn：从神经层面测量泛化习服，并排除疲劳和认知投入等竞争解释。

#### 3. 3

- mode_cn：novel foil 对照

- purpose_cn：用视觉上全新的刺激作为恢复反应基线，区分习服与神经/感受器疲劳。

#### 4. 4

- mode_cn：MST补充实验

- purpose_cn：用认知神经科学范式的记忆区分任务证明被试能意识区分通知与警告。

#### 5. 5

- mode_cn：Experiment 3视觉恒定对照

- purpose_cn：在固定视觉外观条件下只改变交互模式，分离模式与外观的效应。

#### 6. 6

- mode_cn：logistic/linear回归

- purpose_cn：估计警告类型和暴露位置对警告忽视概率与RT的影响，并检验交互效应。

- why_these_evaluations_cn：因为泛化习服是神经层面的无意识过程，单一行为实验不足以排除疲劳、认知投入、意识区分失败和视觉/交互模式混淆等竞争解释，所以依次加入行为、神经、记忆区分和视觉恒定的多证据链。

- benchmark_and_contrast_chain_cn：Exposure 1作为未习服基线；Exposure 15/30作为习服后处理；novel foil作为疲劳重置基准；MST中精确重复/相似/新刺激提供记忆区分基准；fMRI中前导通知激活作为泛化比较基准；Experiment 3按钮启用作为同模式参照、滑杆启用作为异模式处理。

### claim_evidence_ledger

#### 1. H1：通知习服泛化到视觉相似的安全警告

- claim_cn：H1：通知习服泛化到视觉相似的安全警告

- evidence_cn：实验1：警告在14次通知后被忽视概率1.62倍、ln(RT)显著更低；实验2：首次按钮警告激活显著低于紧邻通知

- status_cn：支持

#### 2. H2：视觉不同的警告泛化更少

- claim_cn：H2：视觉不同的警告泛化更少

- evidence_cn：实验1：save executable/open macro两类视觉不相似警告在Exposure 1/15无显著差异；相似警告显著泛化

- status_cn：支持

#### 3. H3：交互模式不同的警告泛化更少

- claim_cn：H3：交互模式不同的警告泛化更少

- evidence_cn：实验2：滑杆/拖拽警告激活显著高于通知；实验3：视觉恒定下滑杆警告无显著泛化而按钮警告显著泛化

- status_cn：支持

#### 4. 泛化不是神经疲劳

- claim_cn：泛化不是神经疲劳

- evidence_cn：实验1 novel foil在通知前后无显著RT差异；实验2 novel foil激活显著高于通知

- status_cn：支持

#### 5. 泛化不是认知投入增加

- claim_cn：泛化不是认知投入增加

- evidence_cn：实验2腹侧视觉流激活线性下降，不符合认知投入增加预测

- status_cn：支持

#### 6. 被试能意识区分通知与警告

- claim_cn：被试能意识区分通知与警告

- evidence_cn：事后concern评分显示通知显著更低；MST可区分绩效通知与安全警告

- status_cn：支持

- internal_validity_strategy_cn：随机分配、组间/组内设计、掩护任务和欺骗降低需求特征、操作检查确认习服、novel foil和fMRI排除疲劳/认知投入、MST排除意识区分失败、Experiment 3视觉恒定排除混淆。

- external_validity_strategy_cn：MTurk美国样本、在参与者自己的真实浏览器/自然环境中进行、使用真实Firefox警告和通知；fMRI为人为环境但用于机制验证；作者声明外推需谨慎。

- what_is_not_actually_tested_cn：未直接测量现实世界中长时间、跨设备的通知暴露量；未验证相似度的阈值；未检验音频/AR/VR等其他交互范式；未检验更高阶认知（动机、培训、专家知识）能否覆盖泛化；未测量长期干预效果。

## 贡献闭环

- technical_claim_cn：泛化习服可以从频繁通知传导到从未见过的安全警告，并且可以通过视觉外观差异或交互模式差异加以减轻；该效应在行为和神经层面均可测量。

- artifact_claim_cn：警告的视觉外观和交互模式是两个可识别的设计维度：视觉不相似警告无显著泛化，交互模式不同的滑杆警告在视觉恒定时仍能抵抗泛化。

- mechanism_claim_cn：机制是双过程习服中的心理模型自动匹配：高频通知建立模型，相似警告在神经层面无意识匹配并抑制反应；图式理论补充解释为何改变交互模式会打断肌肉记忆并迫使意识参与。

- boundary_claim_cn：结论主要在桌面浏览器和鼠标/按钮UI中验证；作者预期可外推到其他设备和应用，但未直接测试；也未测试相似度阈值、更高阶认知过程和长期效应。

- reusable_design_knowledge_cn：安全警告应当在首次出现时就与常见非安全通知在视觉或交互模式上显著区分；不能仅依赖polymorphic设计或减少警告次数；开发者应重新审视UI一致性原则在安全警告中的适用性。

- theoretical_contribution_cn：把泛化习服概念引入IS/安全警告研究，证明习服问题比以往认识的更严重：人们可能对从未见过的警告已经深度习服；同时用双过程理论和图式理论把机制转译为可检验设计知识。

- how_discussion_closes_intro_gap_cn：Discussion按RQ1/RQ2组织，直接回应引言中“泛化未研究、最佳干预未知”的缺口：RQ1说明泛化确实发生且不能用疲劳/认知投入/意识区分失败解释；RQ2提供视觉和交互模式两种理论驱动干预，并比较与过去polymorphic建议的差异。

- overclaim_or_unsupported_leaps_cn：作者在摘要和讨论中声称“人们可能已经深度习服从未见过警告”，但实验只是短时间内14/15/29次实验室诱导通知，不是真实长期暴露；“无意识”是通过能意识区分仍出现泛化间接推断；Exp2的滑杆/拖拽组整合了两类交互模式且带有视觉差异，严格上不能完全归因于模式；声称“没有可用性成本”未测量用户效率/满意度；跨设备外推是推测。

## 句级写作动作图谱

### 1. Abstract P1 S1

- order：1

- section：Abstract

- locator：Abstract P1 S1

- move_code：CONTEXT

- paraphrase_cn：安全警告被忽视是网络安全中的关键问题

- rhetorical_function_cn：开篇点明问题的重要性

- depends_on_cn：无

- sets_up_cn：引出后续“问题加剧”现象

- evidence_pointer：Abstract P1 S1

### 2. Abstract P1 S2

- order：2

- section：Abstract

- locator：Abstract P1 S2

- move_code：PHENOMENON

- paraphrase_cn：当人们把安全警告与日常无关通知混淆时，问题更严重，因为通知已被习惯性忽略

- rhetorical_function_cn：将一般问题收缩到通知与警告混淆

- depends_on_cn：依赖前句问题

- sets_up_cn：为泛化习服理论登场铺路

- evidence_pointer：Abstract P1 S2

### 3. Abstract P2 S1

- order：3

- section：Abstract

- locator：Abstract P2 S1

- move_code：THEORY_INTRO

- paraphrase_cn：以泛化习服为理论机制，习服一个刺激会转移到相似刺激

- rhetorical_function_cn：引入核心理论

- depends_on_cn：前句现象

- sets_up_cn：解释为何未见过警告也被忽视

- evidence_pointer：Abstract P2 S1

### 4. Abstract P2 S2

- order：4

- section：Abstract

- locator：Abstract P2 S2

- move_code：MECHANISM

- paraphrase_cn：因通知频繁出现，人们可能对从未见过的安全警告已经深度习服

- rhetorical_function_cn：说明理论应用到安全域的含义

- depends_on_cn：前句机制

- sets_up_cn：引出后续实验

- evidence_pointer：Abstract P2 S2

### 5. Abstract P2 S3

- order：5

- section：Abstract

- locator：Abstract P2 S3

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：即使意识上能区分，无意识神经机制仍会使泛化发生

- rhetorical_function_cn：设置关键边界/理论主张

- depends_on_cn：前句机制

- sets_up_cn：为“意识区分但忽视”的证据铺垫

- evidence_pointer：Abstract P2 S3

### 6. Abstract P3 S1

- order：6

- section：Abstract

- locator：Abstract P3 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：通过两个现场实验和一个fMRI实验检验

- rhetorical_function_cn：预告研究设计

- depends_on_cn：理论假设

- sets_up_cn：让读者知道证据形式

- evidence_pointer：Abstract P3 S1

### 7. Abstract P3 S2

- order：7

- section：Abstract

- locator：Abstract P3 S2

- move_code：RESULT

- paraphrase_cn：实验证明泛化会发生，并且可借视觉外观或交互模式差异减轻

- rhetorical_function_cn：给出核心结果

- depends_on_cn：实验设计

- sets_up_cn：支撑贡献

- evidence_pointer：Abstract P3 S2

### 8. Abstract P4 S1

- order：8

- section：Abstract

- locator：Abstract P4 S1

- move_code：CONTRIBUTION

- paraphrase_cn：为开发者提供抗泛化的警告设计指引

- rhetorical_function_cn：声明实践意义

- depends_on_cn：结果

- sets_up_cn：结束摘要

- evidence_pointer：Abstract P4 S1

### 9. Introduction P1 S1

- order：9

- section：Introduction

- locator：Introduction P1 S1

- move_code：CONTEXT

- paraphrase_cn：警告常是个人或组织被攻破前的最后防线，许多安全事件源于忽视警告打开恶意文件

- rhetorical_function_cn：用安全事件建立现实后果

- depends_on_cn：无

- sets_up_cn：说明问题严重性

- evidence_pointer：Introduction P1, Figure 1a

### 10. Introduction P2 S1

- order：10

- section：Introduction

- locator：Introduction P2 S1

- move_code：PHENOMENON

- paraphrase_cn：常见通知与安全警告外观相似，UI一致性原则和主流开发指南鼓励这种一致性

- rhetorical_function_cn：描述具体经验现象

- depends_on_cn：前段问题

- sets_up_cn：提出矛盾：一致性设计反而有害

- evidence_pointer：Introduction P2

### 11. Introduction P2 S2

- order：11

- section：Introduction

- locator：Introduction P2 S2

- move_code：LIMITATION

- paraphrase_cn：已有研究指出安全消息常像普通对话框，用户学会忽视

- rhetorical_function_cn：引用已有知识限制

- depends_on_cn：前句现象

- sets_up_cn：为GAP铺垫

- evidence_pointer：Introduction P2, West 2008 quote

### 12. Introduction P3 S1

- order：12

- section：Introduction

- locator：Introduction P3 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：习服被定义为重复刺激反应下降；IS研究已发现第二次看警告脑注意下降导致忽视

- rhetorical_function_cn：总结已有成果

- depends_on_cn：理论概念

- sets_up_cn：说明文献基础

- evidence_pointer：Introduction P3

### 13. Introduction P3 S2

- order：13

- section：Introduction

- locator：Introduction P3 S2

- move_code：LIMITATION

- paraphrase_cn：但这些研究没有处理用户将警告与通知混淆、且能意识区分的情境

- rhetorical_function_cn：指出现有研究边界

- depends_on_cn：前句成果

- sets_up_cn：形成缺口

- evidence_pointer：Introduction P3

### 14. Introduction P3 S3

- order：14

- section：Introduction

- locator：Introduction P3 S3

- move_code：GAP

- paraphrase_cn：因此问题的性质和条件未知，哪些干预有效也未知

- rhetorical_function_cn：明确尚未解决问题

- depends_on_cn：前句边界

- sets_up_cn：引出研究问题和目标

- evidence_pointer：Introduction P3

### 15. Introduction P4 S1

- order：15

- section：Introduction

- locator：Introduction P4 S1

- move_code：THEORY_INTRO

- paraphrase_cn：提出泛化习服这一IS中未探索的习服侧面

- rhetorical_function_cn：引入新理论资源

- depends_on_cn：缺口

- sets_up_cn：建立理论框架

- evidence_pointer：Introduction P4

### 16. Introduction P4 S2

- order：16

- section：Introduction

- locator：Introduction P4 S2

- move_code：MECHANISM

- paraphrase_cn：对相似刺激的习服会转移到新的相似刺激，所以人们可能对从未见过的警告已深度习服

- rhetorical_function_cn：解释因果机制

- depends_on_cn：理论概念

- sets_up_cn：预测H1/H2

- evidence_pointer：Introduction P4

### 17. Introduction P4 S3

- order：17

- section：Introduction

- locator：Introduction P4 S3

- move_code：MECHANISM

- paraphrase_cn：因为习服在神经层面无意识，即使能意识区分也会发生

- rhetorical_function_cn：强化机制的无意识性

- depends_on_cn：前句

- sets_up_cn：统领后续MST/fMRI证据

- evidence_pointer：Introduction P4

### 18. Introduction P5 S1

- order：18

- section：Introduction

- locator：Introduction P5 S1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：提出两个目标和两个研究问题：泛化如何发生、如何减少

- rhetorical_function_cn：明确研究问题

- depends_on_cn：缺口

- sets_up_cn：组织全文

- evidence_pointer：Introduction P5

### 19. Introduction P6 S1

- order：19

- section：Introduction

- locator：Introduction P6 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：实验1在线现场实验证明泛化和视觉差异干预

- rhetorical_function_cn：预告第一项研究

- depends_on_cn：RQs

- sets_up_cn：为实验2铺垫

- evidence_pointer：Introduction P6

### 20. Introduction P6 S2

- order：20

- section：Introduction

- locator：Introduction P6 S2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：fMRI实验提供神经测量并排除疲劳/认知投入，检验交互模式

- rhetorical_function_cn：预告第二项研究

- depends_on_cn：RQs

- sets_up_cn：为实验3铺垫

- evidence_pointer：Introduction P6

### 21. Introduction P6 S3

- order：21

- section：Introduction

- locator：Introduction P6 S3

- move_code：STUDY_OVERVIEW

- paraphrase_cn：实验3分离交互模式与视觉外观

- rhetorical_function_cn：预告第三项研究

- depends_on_cn：前两项

- sets_up_cn：形成完整证据链

- evidence_pointer：Introduction P6

### 22. Introduction P7 S1

- order：22

- section：Introduction

- locator：Introduction P7 S1

- move_code：CONTRIBUTION

- paraphrase_cn：列出三个理论贡献和三个实践贡献

- rhetorical_function_cn：声明研究贡献

- depends_on_cn：全部工作

- sets_up_cn：引导审稿人按贡献评估

- evidence_pointer：Introduction P7

### 23. Generalization and Security Warnings P1 S1

- order：23

- section：Literature Review, Theory, and Hypotheses

- locator：Generalization and Security Warnings P1 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：已有研究观察或推断警告习服存在

- rhetorical_function_cn：回顾文献

- depends_on_cn：引言缺口

- sets_up_cn：对比本研究

- evidence_pointer：Theory section

### 24. Generalization and Security Warnings P1 S2

- order：24

- section：Literature Review, Theory, and Hypotheses

- locator：Generalization and Security Warnings P1 S2

- move_code：LIMITATION

- paraphrase_cn：但在警告情境中的泛化研究不足

- rhetorical_function_cn：指出缺口

- depends_on_cn：前句

- sets_up_cn：说明为什么需要本研究

- evidence_pointer：Theory section

### 25. Generalization and Security Warnings P1 S3

- order：25

- section：Literature Review, Theory, and Hypotheses

- locator：Generalization and Security Warnings P1 S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：Böhme和Köpsell曾观察到通知自动反应溢出到安全隐私问题，但没有经验检验或方案

- rhetorical_function_cn：引用相关但未实证的观察

- depends_on_cn：缺口

- sets_up_cn：为经验研究提供合法性

- evidence_pointer：Theory section

### 26. Generalization and Security Warnings P2 S1

- order：26

- section：Literature Review, Theory, and Hypotheses

- locator：Generalization and Security Warnings P2 S1

- move_code：GAP

- paraphrase_cn：以前的减少习服建议可能因泛化而无效

- rhetorical_function_cn：说明缺口为什么重要

- depends_on_cn：缺口

- sets_up_cn：挑战现有建议

- evidence_pointer：Theory section

### 27. Generalization and Security Warnings P2 S2

- order：27

- section：Literature Review, Theory, and Hypotheses

- locator：Generalization and Security Warnings P2 S2

- move_code：LIMITATION

- paraphrase_cn：限制警告出现次数的建议忽略了一天中大量通知

- rhetorical_function_cn：具体化现有建议的不足

- depends_on_cn：前句

- sets_up_cn：为本研究提供依据

- evidence_pointer：Theory section

### 28. Generalization and Security Warnings P3 S1

- order：28

- section：Literature Review, Theory, and Hypotheses

- locator：Generalization and Security Warnings P3 S1

- move_code：LIMITATION

- paraphrase_cn：polymorphic警告也可能无法抵抗来自通知的泛化

- rhetorical_function_cn：指出另一个建议的不足

- depends_on_cn：前句

- sets_up_cn：强化理论缺口

- evidence_pointer：Theory section

### 29. Generalization and Security Warnings P3 S2

- order：29

- section：Literature Review, Theory, and Hypotheses

- locator：Generalization and Security Warnings P3 S2

- move_code：GAP

- paraphrase_cn：泛化发生的条件和最有效干预未知

- rhetorical_function_cn：直接重申缺口

- depends_on_cn：前两句

- sets_up_cn：为H1-H3铺垫

- evidence_pointer：Theory section

### 30. Generalization Theory and Hypotheses P1 S1

- order：30

- section：Literature Review, Theory, and Hypotheses

- locator：Generalization Theory and Hypotheses P1 S1

- move_code：THEORY_PROPOSITION

- paraphrase_cn：泛化可理解为无法区分刺激；双过程理论认为首次遇到刺激建立心理模型，之后自动比较

- rhetorical_function_cn：陈述核心理论命题

- depends_on_cn：引言理论

- sets_up_cn：推出假设

- evidence_pointer：Theory section

### 31. Generalization Theory and Hypotheses P1 S2

- order：31

- section：Literature Review, Theory, and Hypotheses

- locator：Generalization Theory and Hypotheses P1 S2

- move_code：MECHANISM

- paraphrase_cn：匹配则抑制行为反应；不相配则恢复反应

- rhetorical_function_cn：解释习服机制

- depends_on_cn：前句

- sets_up_cn：说明为何相似刺激被忽视

- evidence_pointer：Theory section

### 32. Generalization Theory and Hypotheses P2 S1

- order：32

- section：Literature Review, Theory, and Hypotheses

- locator：Generalization Theory and Hypotheses P2 S1

- move_code：MECHANISM

- paraphrase_cn：习服提高效率的代价是不能区分相似刺激，抑制会泛化

- rhetorical_function_cn：引入泛化机制

- depends_on_cn：前句

- sets_up_cn：推导相似度/频率决定泛化

- evidence_pointer：Theory section

### 33. Generalization Theory and Hypotheses P3 S1

- order：33

- section：Literature Review, Theory, and Hypotheses

- locator：Generalization Theory and Hypotheses P3 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：人类研究显示即使意识区分，泛化仍发生，因为神经层面无意识

- rhetorical_function_cn：提供跨领域证据

- depends_on_cn：前句

- sets_up_cn：为“意识区分仍忽视”作依据

- evidence_pointer：Theory section

### 34. Generalization Theory and Hypotheses H1

- order：34

- section：Literature Review, Theory, and Hypotheses

- locator：Generalization Theory and Hypotheses H1

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：H1：通知习服会泛化到视觉相似警告

- rhetorical_function_cn：提出可检验假设

- depends_on_cn：理论命题

- sets_up_cn：实验1/2检验

- evidence_pointer：Theory H1

### 35. Generalization Theory and Hypotheses H2

- order：35

- section：Literature Review, Theory, and Hypotheses

- locator：Generalization Theory and Hypotheses H2

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：H2：若警告视觉外观与通知不同，泛化会减少

- rhetorical_function_cn：提出可检验假设

- depends_on_cn：理论命题

- sets_up_cn：实验1检验

- evidence_pointer：Theory H2

### 36. Generalization Theory and Hypotheses H3 intro

- order：36

- section：Literature Review, Theory, and Hypotheses

- locator：Generalization Theory and Hypotheses H3 intro

- move_code：THEORY_INTRO

- paraphrase_cn：引入图式理论和肌肉记忆，解释交互模式

- rhetorical_function_cn：为H3引入第二理论资源

- depends_on_cn：前述视觉理论

- sets_up_cn：发展交互模式干预

- evidence_pointer：Theory H3 intro

### 37. Generalization Theory and Hypotheses H3

- order：37

- section：Literature Review, Theory, and Hypotheses

- locator：Generalization Theory and Hypotheses H3

- move_code：MECHANISM

- paraphrase_cn：点击关闭是主导范式，肌肉记忆让人自动回应消息

- rhetorical_function_cn：解释现状机制

- depends_on_cn：图式理论

- sets_up_cn：说明为何按钮式易泛化

- evidence_pointer：Theory H3

### 38. Generalization Theory and Hypotheses H3

- order：38

- section：Literature Review, Theory, and Hypotheses

- locator：Generalization Theory and Hypotheses H3

- move_code：THEORY_PROPOSITION

- paraphrase_cn：改变图式会迫使意识参与

- rhetorical_function_cn：陈述理论命题

- depends_on_cn：图式理论

- sets_up_cn：导出H3

- evidence_pointer：Theory H3

### 39. Generalization Theory and Hypotheses H3

- order：39

- section：Literature Review, Theory, and Hypotheses

- locator：Generalization Theory and Hypotheses H3

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：H3：交互模式不同的警告泛化更少

- rhetorical_function_cn：提出可检验假设

- depends_on_cn：前句

- sets_up_cn：实验2/3检验

- evidence_pointer：Theory H3

### 40. Methods P1 S1

- order：40

- section：Methods

- locator：Methods P1 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：遵循NeuroIS与行为实验互补的指南设计三实验

- rhetorical_function_cn：解释方法论

- depends_on_cn：研究目标

- sets_up_cn：说明为何用三种方法

- evidence_pointer：Methods, Kirwan et al. 2023

### 41. Methods P1 S2

- order：41

- section：Methods

- locator：Methods P1 S2

- move_code：STUDY_OVERVIEW

- paraphrase_cn：实验1/2/3分别检验H1-H3，Table 1概览

- rhetorical_function_cn：预告研究阶段

- depends_on_cn：设计框架

- sets_up_cn：给读者路线图

- evidence_pointer：Methods, Table 1

### 42. Experiment 1 intro P1 S1

- order：42

- section：Experiment 1

- locator：Experiment 1 intro P1 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：选择浏览器现场任务是观察自然环境下真实警告行为

- rhetorical_function_cn：方法合理性

- depends_on_cn：整体设计

- sets_up_cn：提高生态效度

- evidence_pointer：Experiment 1 intro

### 43. Experiment 1 Warning Treatments P1 S1

- order：43

- section：Experiment 1

- locator：Experiment 1 Warning Treatments P1 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：随机选择四类Firefox警告，其中两类在外观上相似/两类不同

- rhetorical_function_cn：描述材料设计

- depends_on_cn：理论H1/H2

- sets_up_cn：为对比提供操作化

- evidence_pointer：Experiment 1 Warning Treatments

### 44. Operationalizations of Habituation P1 S1

- order：44

- section：Experiment 1

- locator：Operationalizations of Habituation P1 S1

- move_code：REQUIREMENT

- paraphrase_cn：用反应时间测习服，因为习惯化后反应变快

- rhetorical_function_cn：将构念转化为指标

- depends_on_cn：习服定义

- sets_up_cn：建立DV

- evidence_pointer：Operationalizations of Habituation

### 45. Operationalizations of Habituation P2 S1

- order：45

- section：Experiment 1

- locator：Operationalizations of Habituation P2 S1

- move_code：REQUIREMENT

- paraphrase_cn：用是否点击不安全选项作为警告忽视二值

- rhetorical_function_cn：将行为结果转化为指标

- depends_on_cn：安全目标

- sets_up_cn：建立第二个DV

- evidence_pointer：Operationalizations of Habituation

### 46. Operationalizations of Generalization

- order：46

- section：Experiment 1

- locator：Operationalizations of Generalization

- move_code：REQUIREMENT

- paraphrase_cn：把泛化操作化为警告在通知后出现与单独出现之间的差异

- rhetorical_function_cn：定义泛化指标

- depends_on_cn：Rankin定义

- sets_up_cn：后续统计模型基础

- evidence_pointer：Operationalizations of Generalization

### 47. Ruling Out Fatigue

- order：47

- section：Experiment 1

- locator：Ruling Out Fatigue

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：使用视觉差异大的novel foil作基线以排除疲劳

- rhetorical_function_cn：引入竞争解释对照

- depends_on_cn：神经生物学标准

- sets_up_cn：为实验1/2排除疲劳

- evidence_pointer：Ruling Out Fatigue

### 48. Testing for Habituation and Manipulation Check

- order：48

- section：Experiment 1

- locator：Testing for Habituation and Manipulation Check

- move_code：RESULT

- paraphrase_cn：通知第14次反应比第一次快24%，习服操作成功

- rhetorical_function_cn：报告操作检查

- depends_on_cn：实验数据

- sets_up_cn：验证实验有效性

- evidence_pointer：Figure 6

### 49. Testing H1

- order：49

- section：Experiment 1

- locator：Testing H1

- move_code：RESULT

- paraphrase_cn：警告在通知后被忽视概率1.62倍，RT约22%短，支持H1

- rhetorical_function_cn：报告核心结果

- depends_on_cn：回归分析

- sets_up_cn：确立泛化行为效应

- evidence_pointer：Table 3

### 50. Testing H2

- order：50

- section：Experiment 1

- locator：Testing H2

- move_code：RESULT

- paraphrase_cn：视觉相似警告有显著泛化，视觉不相似警告无显著泛化，支持H2

- rhetorical_function_cn：报告对比结果

- depends_on_cn：Table 4模型

- sets_up_cn：证明视觉差异干预有效

- evidence_pointer：Table 4, Figure 6/7

### 51. Ruling Out Fatigue

- order：51

- section：Experiment 1

- locator：Ruling Out Fatigue

- move_code：RESULT

- paraphrase_cn：novel foil在通知前后无显著差异，不支持疲劳解释

- rhetorical_function_cn：排除竞争解释

- depends_on_cn：novel foil数据

- sets_up_cn：加强H1

- evidence_pointer：Table 4 'Foil × After notifications'

### 52. Ruling Out a Lack of Discrimination P1

- order：52

- section：Experiment 1

- locator：Ruling Out a Lack of Discrimination P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：事后concern显示通知比警告显著更低，说明能区分

- rhetorical_function_cn：用额外数据排除意识区分失败

- depends_on_cn：被试报告

- sets_up_cn：为MST铺垫

- evidence_pointer：Ruling Out a Lack of Discrimination

### 53. Ruling Out a Lack of Discrimination P2-P3

- order：53

- section：Experiment 1

- locator：Ruling Out a Lack of Discrimination P2-P3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用MST检验记忆表征和区分能力

- rhetorical_function_cn：引入认知神经范式

- depends_on_cn：concern证据

- sets_up_cn：提供更强排除证据

- evidence_pointer：MST section

### 54. MST Results

- order：54

- section：Experiment 1

- locator：MST Results

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：MST显示被试能区分绩效通知与警告，但平时仍会泛化

- rhetorical_function_cn：报告稳健性结果

- depends_on_cn：MST数据

- sets_up_cn：支撑“无意识泛化”主张

- evidence_pointer：Table 5

### 55. Experiment 1 Summary

- order：55

- section：Experiment 1

- locator：Experiment 1 Summary

- move_code：TRANSITION

- paraphrase_cn：实验1支持H1/H2并排除疲劳和意识区分失败

- rhetorical_function_cn：小结

- depends_on_cn：全部实验1结果

- sets_up_cn：引出fMRI

- evidence_pointer：Experiment 1 Summary

### 56. Experiment 2 intro P1

- order：56

- section：Experiment 2

- locator：Experiment 2 intro P1

- move_code：TRANSITION

- paraphrase_cn：快速RT仍可用认知投入解释，需要fMRI排除

- rhetorical_function_cn：识别剩余竞争解释

- depends_on_cn：实验1结果

- sets_up_cn：说明做fMRI的必要性

- evidence_pointer：Experiment 2 intro

### 57. Experiment 2 Task and Design

- order：57

- section：Experiment 2

- locator：Experiment 2 Task and Design

- move_code：DESIGN_FEATURE

- paraphrase_cn：三种警告交互模式：按钮、按住滑杆、拖拽

- rhetorical_function_cn：设计干预变化

- depends_on_cn：图式理论

- sets_up_cn：测试H3

- evidence_pointer：Figure 9

### 58. Operationalization of Habituation and Generalization

- order：58

- section：Experiment 2

- locator：Operationalization of Habituation and Generalization

- move_code：REQUIREMENT

- paraphrase_cn：将习服操作化为BOLD激活下降，若novel foil激活高则排除疲劳

- rhetorical_function_cn：神经指标

- depends_on_cn：fMRI测量

- sets_up_cn：神经检验基础

- evidence_pointer：Operationalization of Habituation and Generalization

### 59. Testing for Habituation and Manipulation Check

- order：59

- section：Experiment 2

- locator：Testing for Habituation and Manipulation Check

- move_code：RESULT

- paraphrase_cn：腹侧视觉流等多区域对通知出现线性习服

- rhetorical_function_cn：确认神经层面操作成功

- depends_on_cn：fMRI数据

- sets_up_cn：可继续检验泛化

- evidence_pointer：Figure 11

### 60. Testing H1

- order：60

- section：Experiment 2

- locator：Testing H1

- move_code：RESULT

- paraphrase_cn：首次按钮警告激活显著低于紧邻通知，支持H1

- rhetorical_function_cn：神经层面泛化证据

- depends_on_cn：GLM对比

- sets_up_cn：强化行为结果

- evidence_pointer：Exp2 Testing H1

### 61. Ruling Out Cognitive Engagement and Fatigue

- order：61

- section：Experiment 2

- locator：Ruling Out Cognitive Engagement and Fatigue

- move_code：RESULT

- paraphrase_cn：激活线性下降不支持认知投入；novel foil激活高于通知排除疲劳

- rhetorical_function_cn：排除两种竞争解释

- depends_on_cn：fMRI对照

- sets_up_cn：加强H1

- evidence_pointer：Exp2 Ruling Out

### 62. Testing H3

- order：62

- section：Experiment 2

- locator：Testing H3

- move_code：RESULT

- paraphrase_cn：滑杆/拖拽警告激活显著高于通知，按钮警告与通知无差异，支持H3

- rhetorical_function_cn：交互模式效果神经证据

- depends_on_cn：簇内平均激活

- sets_up_cn：转至实验3

- evidence_pointer：Figure 12

### 63. Experiment 3 intro P1

- order：63

- section：Experiment 3

- locator：Experiment 3 intro P1

- move_code：TRANSITION

- paraphrase_cn：实验2无法分离交互模式与视觉外观，故实验3视觉恒定

- rhetorical_function_cn：说明下一研究动机

- depends_on_cn：Exp2局限

- sets_up_cn：设计实验3

- evidence_pointer：Experiment 3 intro

### 64. Experimental Task and Treatments

- order：64

- section：Experiment 3

- locator：Experimental Task and Treatments

- move_code：DESIGN_FEATURE

- paraphrase_cn：通知和警告同时含按钮和滑杆，只启用一个，保持视觉外观恒定

- rhetorical_function_cn：材料设计关键

- depends_on_cn：前句动机

- sets_up_cn：隔离交互模式

- evidence_pointer：Figure 13

### 65. Testing H3

- order：65

- section：Experiment 3

- locator：Testing H3

- move_code：RESULT

- paraphrase_cn：按钮警告在30次后被忽视2.77倍、RT快32%；滑杆警告无显著泛化，支持H3

- rhetorical_function_cn：核心结果

- depends_on_cn：回归模型

- sets_up_cn：确证交互模式干预

- evidence_pointer：Table 7, Figure 14/15

### 66. Experiment 3 Summary

- order：66

- section：Experiment 3

- locator：Experiment 3 Summary

- move_code：RESULT

- paraphrase_cn：视觉恒定条件下交互模式差异足以减少泛化

- rhetorical_function_cn：小结

- depends_on_cn：实验3数据

- sets_up_cn：进入讨论

- evidence_pointer：Experiment 3 Summary

### 67. General Discussion P1

- order：67

- section：General Discussion

- locator：General Discussion P1

- move_code：CONTRIBUTION

- paraphrase_cn：研究扩大习服问题范围：通知习服会泛化到从未见过警告

- rhetorical_function_cn：回扣引言缺口

- depends_on_cn：三实验证据

- sets_up_cn：声明RQ1贡献

- evidence_pointer：General Discussion

### 68. Contributions Relative to RQ1 P2

- order：68

- section：General Discussion

- locator：Contributions Relative to RQ1 P2

- move_code：CONTRIBUTION

- paraphrase_cn：泛化性质说明减少警告次数不足以解决问题，应让警告与通知区分

- rhetorical_function_cn：理论含义

- depends_on_cn：机制+实验

- sets_up_cn：指导实践

- evidence_pointer：Contributions Relative to RQ1

### 69. Contributions Relative to RQ1 P4

- order：69

- section：General Discussion

- locator：Contributions Relative to RQ1 P4

- move_code：CONTRIBUTION

- paraphrase_cn：UI一致性原则在安全场景可能制造安全威胁

- rhetorical_function_cn：挑战领域原则

- depends_on_cn：泛化理论

- sets_up_cn：连接实践贡献

- evidence_pointer：Contributions Relative to RQ1

### 70. Contributions Relative to RQ2 P1/P2

- order：70

- section：General Discussion

- locator：Contributions Relative to RQ2 P1/P2

- move_code：CONTRIBUTION

- paraphrase_cn：提出视觉识别性和交互模式两类理论驱动干预，且不能从先前polymorphic工作推出

- rhetorical_function_cn：声明RQ2贡献

- depends_on_cn：H2/H3证据

- sets_up_cn：为设计原则定位

- evidence_pointer：Contributions Relative to RQ2

### 71. Limitations P1-S4

- order：71

- section：Limitations and Future Research

- locator：Limitations P1-S4

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：限制包括浏览器环境、高阶过程、传统鼠标UI、相似度阈值

- rhetorical_function_cn：为结论界定边界

- depends_on_cn：研究设计

- sets_up_cn：未来方向

- evidence_pointer：Limitations and Future Research

### 72. Conclusion P1

- order：72

- section：Conclusion

- locator：Conclusion P1

- move_code：CONTRIBUTION

- paraphrase_cn：结论：泛化习服让用户忽视从未见过的警告；视觉或交互模式差异可减轻

- rhetorical_function_cn：最终总结

- depends_on_cn：全部证据

- sets_up_cn：结束文章

- evidence_pointer：Conclusion

## 写作技术

- gap_construction_cn：先承认已有习服研究解释了个别警告的重复忽视，再指出两个缺口：泛化本身没有被经验检验，而且旧有建议（减少警告次数、polymorphic设计）在通知密集环境中可能失效；这样把缺口定位成理论机制缺失而非单纯性能不足。

- signposting_cn：引言明确提出RQ1/RQ2；Methods用Table 1概览三个实验；每个实验前后都有导语和Summary；General Discussion按RQ1/RQ2组织贡献，并以表格对比过去研究。

- transition_logic_cn：每个实验结尾总结已解决和未解决的问题：实验1留下认知投入与交互模式混淆，MST解决意识区分，实验2解决神经机制并留下视觉/交互混淆，实验3用视觉恒定设计解决该混淆。

- claim_evidence_rhythm_cn：先给行为证据，再用神经证据强化，再用排除性检验保护；每个假设都配有正式回归模型和关键图表；报告结果时直接回连到假设编号。

- benchmark_narrative_cn：Exposure 1/15/30的对比作为基准叙事；novel foil作为“疲劳不可能”的关键反转；MST作为“意识区分”的基准；fMRI中紧邻通知激活作为泛化的神经基准；Experiment 3的按钮条件作为同模式基准，滑杆条件作为干预。

- theory_return_cn：Discussion不再重复每个实验，而是把证据归纳为RQ1/RQ2的理论贡献：泛化使“减少警告次数”失效，提示警告必须首次就与通知区分；把结果回接到双过程理论和图式理论。

- contribution_positioning_cn：用“对RQ1的贡献”“对RQ2的贡献”和“与过去研究对比表”三层定位；每个贡献直接对应一个假设或一个排除性检验。

- novelty_protection_cn：通过行为+神经双证据、排除多种竞争解释、分离单一设计维度，并把结果回接到双过程理论与图式理论，避免被视为一次性性能差异。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：建立现实问题的严重性：安全警告忽视导致失陷，并引入通知与警告相似的日常现象。

- research_job_cn：找到有现实后果但未被IS充分理论化的安全行为问题。

- required_evidence_cn：安全事件、行业报告和UI设计指南等来源证明问题存在。

- transition_to_next_cn：从现象过渡到“为什么现有习服研究不能解释”的缺口。

#### 2. 2

- step：2

- writing_job_cn：指出已有习服研究只考察个别警告，没有考察从非安全通知到警告的泛化。

- research_job_cn：系统阅读神经生物学和IS安全警告文献，定位泛化习服这一未使用概念。

- required_evidence_cn：已有研究明确未测量泛化；旧建议在通知密集场景不成立的论证。

- transition_to_next_cn：引出新的理论透镜和研究问题。

#### 3. 3

- step：3

- writing_job_cn：陈述双过程习服理论和图式理论，并把理论命题翻译成H1/H2/H3。

- research_job_cn：从心理模型匹配、刺激相似度和交互图式推出可检验预测。

- required_evidence_cn：理论命题和神经生物学文献支持；每个假设对应明确的设计差异。

- transition_to_next_cn：说明需要哪些实验来分别检验行为、神经和隔离设计维度。

#### 4. 4

- step：4

- writing_job_cn：构造浏览器掩护任务、重复通知和警告刺激，并在真实环境中操作化习服与泛化。

- research_job_cn：用既有浏览器警告、通知和novel foil建立暴露位置对比。

- required_evidence_cn：操作检查显示通知确实诱发习服；被试相信警告来自真实网站。

- transition_to_next_cn：报告泛化效应并转向排除竞争解释。

#### 5. 5

- step：5

- writing_job_cn：用Exposure 1 vs 15的对比和视觉相似/不相似警告报告行为结果，支持H1/H2。

- research_job_cn：运行logistic/线性回归，用novel foil排除疲劳。

- required_evidence_cn：显著交互项、不显著的foil效应。

- transition_to_next_cn：指出需要神经证据排除认知投入，并需要MST排除意识区分失败。

#### 6. 6

- step：6

- writing_job_cn：用MST补充实验证明用户能意识区分通知与警告。

- research_job_cn：借用认知神经科学中的MST范式，把通知和警告当作记忆区分刺激。

- required_evidence_cn：对通知的“旧”反应高，对警告的“旧”反应低。

- transition_to_next_cn：说明意识区分不等于神经层面不泛化，引出fMRI。

#### 7. 7

- step：7

- writing_job_cn：用fMRI从神经层面确认泛化并排除疲劳/认知投入，同时用交互模式变化初步测试H3。

- research_job_cn：执行组内fMRI实验，测量腹侧视觉流BOLD激活，加入novel foil和不同模式警告。

- required_evidence_cn：对通知的线性习服、首次警告激活低于前导通知、foil激活高于通知、异模式警告激活高于通知。

- transition_to_next_cn：指出现有设计无法分离交互模式与视觉外观，需要视觉恒定实验。

#### 8. 8

- step：8

- writing_job_cn：用视觉外观恒定的在线现场实验单独检验交互模式，支持H3。

- research_job_cn：在同一通知/警告上同时呈现按钮和滑杆，只启用其中一个，并比较Exposure 1 vs 30。

- required_evidence_cn：按钮条件显著泛化，滑杆条件不显著。

- transition_to_next_cn：将所有证据汇总，返回理论贡献与边界。

#### 9. 9

- step：9

- writing_job_cn：按RQ1/RQ2组织讨论，把行为+神经证据上升为理论贡献、设计知识和边界条件。

- research_job_cn：评估哪些竞争解释被排除，哪些限制仍存在。

- required_evidence_cn：每个贡献至少对应一个假设或排除性检验；限制部分明确指出未测项。

- transition_to_next_cn：结束。

### most_transferable_moves_cn

1. 把神经科学中的习服/泛化概念转译为警告设计变量并形成假设

2. 用暴露位置对比作为泛化基准，用novel foil排除疲劳

3. 行为实验、神经实验和补充记忆实验形成递增证据链

4. 最后再用视觉恒定设计分离设计维度

5. 用RQ结构组织贡献，避免贡献散落

### resource_intensive_or_nonstandard_parts_cn

1. fMRI扫描和神经数据分析

2. MST记忆区分实验

3. 在线现场实验中的真实浏览器警告和掩护任务

4. 自定义通知/警告刺激并保持视觉恒定

5. MTurk样本与奖励机制

### what_not_to_copy_superficially_cn

1. 不能只提“泛化习服”却没有行为或神经层面的操纵检查

2. 不能没有novel foil等对照就宣称排除疲劳

3. 不能在没有保持视觉恒定的情况下把效应全归于交互模式

4. 不能在没有意识区分任务的情况下断言“无意识泛化”

5. 不能把实验室短时暴露的结果直接说成现实长期影响

- single_best_description_of_the_routine_cn：用神经生物学理论把日常通知与安全警告的相似性转化为可检验的设计威胁，再通过现场实验、fMRI和隔离实验逐级证明机制并提炼反制设计知识。

## 分析边界

OCR/文本提取的表格编号有不一致（如Table 6被标为Experiment 4，Figure 13被标为Experiment 4），附录A/B未包含在提供文本中；因此具体扫描参数和部分补充分析无法核对。无页码。
