# Augmenting Password Strength Meter Design Using the Elaboration Likelihood Model: Evidence from Randomized Experiments

- 作者：Warut Khern-am-nuai; Matthew J. Hashim; Alain Pinsonneault; Weining Yang; Ninghui Li
- 年份 / 期刊：2023 / Information Systems Research
- DOI：10.1287/isre.2022.1125
- 源文件：28462_2023_augmenting-password-strength-meter-design-using-the-elaboration-likelihood-model-evidence-from-r.md
- 论文主类型：multi_method_or_multi_study_program
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.84

## 文章级论证概况

- 核心问题：在不修改密码强度算法、不依赖复杂密码策略的前提下，能否通过重新设计密码强度计的消息呈现方式，使用户生成更强的新密码并更愿意修改初始弱密码？

- 制品与设计：基于ELM设计的三类增强型密码强度计：在传统强度标签基础上分别加入恐惧诉求（预计破解时间Time）、同伴比较（弱点密码排名Rank）和共同纽带（相同密码账户数Probability）；密码强度算法、阈值和标签在所有处理中保持不变，只改变额外提示消息。

- 客观结果：Study 1显示三种消息在安全相关构念上产生与消息类型一致的显著差异；Study 2中Rank处理显著提高密码强度增长量和密码修改次数，Time和Probability不显著；Study 3现场实验中Rank仍显著，Time和Probability在强度提升上边缘显著。

- 核心贡献：首次为密码强度计如何影响用户行为建立ELM理论基础，提出并验证了可通过中心路径发挥作用的呈现设计；同时将ELM扩展到数字安全情境，发现社会比较类刺激（Rank）在数字情境中效果更强，并提供低成本、易部署的实践方案。

- 整篇论证链：论文先以密码弱密码问题持续存在且替代技术不可行来建立现实紧迫性，指出现有密码强度计研究集中在算法精度而忽视呈现组件缺乏理论指导。随后引入ELM，将传统视觉提示归为边缘路径，主张要获得更持久的行为改变应使用中心路径刺激。作者据此在保持算法固定前提下设计三类增强消息，并通过survey验证消息确实被仔细加工（proof of concept），通过随机实验室实验验证行为效果（proof of value），再通过现场随机实验验证真实环境中的外部效度（proof of use）。三级证据链一致支持Rank效果最强，最终在讨论中把这一发现上升为对ELM情境依赖性的理论贡献。

## 类型与写作弧线判定

- 论文主类型判定：论文虽然采用设计科学范式，但核心证据由三个独立互补的实证研究（survey、controlled lab experiment、field experiment）累积而成，作者明确以proof of concept、proof of value、proof of use组织贡献，并以多方法互补、印证、补偿作为评价逻辑，因此判定为多方法/多Study研究项目，而非单一制品实验或纯算法benchmark。

- 主导写作弧线判定：文章从弱密码这一现实问题切入，引入ELM解释传统强度计为何效果短暂，从理论推导出三类设计，再用三项随机实验检验，最后在讨论中把实证结果回接到ELM并提出情境依赖修正。整体是典型的'问题—理论—设计—检验—回到理论'弧线。

## 研究开展程序

- study_or_phase_count：4

- 研究阶段总序列：先进行理论驱动的概念设计与实现，形成三个可实验处理；再通过survey验证消息的中心路径加工显著性；随后通过随机实验室实验验证行为改善；最后通过真实论坛现场实验验证外部效度。每一步既回答当前未解决问题，也为下一步提供研究对象和假设基础。

### studies_or_phases

#### 1. 理论驱动设计与实现（概念构建阶段）

- order：1

- name_cn：理论驱动设计与实现（概念构建阶段）

- question_cn：如何将ELM转成可嵌入现有密码强度计的具体消息设计？在算法不变时，哪些消息最可能被用户以中心路径加工？

- inputs_and_setting_cn：ELM及恐惧诉求、同伴比较、共同纽带相关文献；backoff Markov密码强度模型；RockYou密码数据集；网页端密码输入界面；JavaScript/AJAX实现。

- designed_or_compared_object_cn：三类增强型密码强度计：Time（恐惧诉求）、Rank（同伴比较）、Probability（共同纽带），与仅显示强度标签的传统强度计对照。

- baseline_control_or_counterfactual_cn：传统密码强度计（weak/medium/strong标签）作为控制；强度计算模型与阈值在所有处理中固定。

##### objective_metrics

1. 设计可实施性

2. 消息与强度标签能否共存

3. 密码强度计算是否跨处理保持一致

- analysis_method_cn：用Gregor的Type V理论和Gregor & Hevner的设计科学原则做理论到设计的翻译；通过backoff Markov模型计算强度并以focusout事件触发消息显示。

- main_result_cn：得到Time、Rank、Probability三种可部署的增强消息设计，每条消息都保留强度标签，且只改变消息文本。

- argumentative_role_cn：确定实验处理的操作化定义，建立所有后续研究的共同对照组与处理变量，确保唯一变化是消息呈现。

- remaining_uncertainty_cn：尚不清楚用户是否真的中心加工这些消息，也不确定消息能否转化为行为改变。

- link_to_next_phase_cn：由于中心路径加工可能失败，需要先用survey验证消息显著性，因此进入Study 1。

##### evidence_pointers

1. Section 2.3

2. Section 3.1-3.4

3. Figures 2-4

4. Table 1

#### 2. Study 1：survey-based证明概念（proof of concept）

- order：2

- name_cn：Study 1：survey-based证明概念（proof of concept）

- question_cn：用户是否会仔细、全面地考虑所看到的增强提示消息？三种消息是否按ELM预期走中心路径？

- inputs_and_setting_cn：美国西南部某大学253名本科生；Qualtrics问卷；假设在线论坛注册场景；各处理随机分配截图为控制65、Time 61、Rank 64、Probability 63；使用Johnston & Warkentin（2010）和Cho等（2010）的构念。

- designed_or_compared_object_cn：四组密码强度计消息：控制（仅强度标签）、Time、Rank、Probability；统一展示weak密码下的最坏消息。

- baseline_control_or_counterfactual_cn：控制组只显示强度标签；以控制组作为比较基准，检验各处理在安全构念路径系数上的差异。

##### objective_metrics

1. PLS多组分析中处理组与控制组显著差异的路径数量

2. 显著路径的方向是否与各消息含义一致

- analysis_method_cn：PLS多组分析，使用SmartPLS 3.2.7，500次bootstrap计算标准误；先做信度、效度与内部一致性检验。

- main_result_cn：三个处理组与控制组的显著结果互不重叠，且与消息类型一致：Time影响易感和脆弱性相关路径；Rank影响响应效能与他人脆弱性路径；Probability影响自我效能相关路径。

- argumentative_role_cn：证明消息被仔细加工，即具备中心路径加工的证据，为后续行为实验奠定机制基础。

- remaining_uncertainty_cn：自我报告而非实际密码行为；学生样本；未直接测量认知加工过程，仅用构念差异推断。

- link_to_next_phase_cn：若消息确实被中心加工，应观察到行为改变，因此进入Study 2的随机实验室实验。

##### evidence_pointers

1. Section 4.1-4.3

2. Table 2

#### 3. Study 2：controlled laboratory experiment证明价值（proof of value）

- order：3

- name_cn：Study 2：controlled laboratory experiment证明价值（proof of value）

- question_cn：在控制条件下，ELM增强型密码强度计是否显著提高用户修改密码的次数并增加修改后的密码强度？

- inputs_and_setting_cn：500名Amazon Mechanical Turk美国参与者；随机分配至4个处理（控制116、Time 133、Rank 131、Probability 120）和3个假设场景（Bank 180、Restaurant 166、Forum 150）；记录完整密码输入历史及点击Tips链接行为；最终497条有效观察。

- designed_or_compared_object_cn：四类密码强度计与三个敏感度不同的注册场景（Forum、Restaurant、Bank）；密码强度计底部提供'Tips towards strong passwords'链接。

- baseline_control_or_counterfactual_cn：控制组为传统强度标签；Bank场景作为场景基准；额外控制变量包括Age、Gender、Education、initial_strength_label；后续补充learn_more、替代熵度量等稳健性检验。

##### objective_metrics

1. diff_strength：密码强度自然对数在消息前后之差

2. num_reset：看到消息后立即修改密码的次数

3. learn_more：是否点击Tips链接学习更多密码安全知识

- analysis_method_cn：diff_strength用线性回归；num_reset用Poisson回归；learn_more用logistic回归；补充中介、调节、替代强度计算等稳健性分析。

- main_result_cn：Rank处理显著提高diff_strength（0.089, p<0.01）和num_reset（0.993, p<0.01）；Time和Probability不显著；Forum场景比Bank场景更促进强度提升；点击Tips无显著差异；控制初始强度后Rank仍显著。

- argumentative_role_cn：在随机分配和高内部效度条件下建立设计的行为效果，尤其锁定Rank为最有效处理。

- remaining_uncertainty_cn：知情同意可能导致用户不自然；低报酬和低风险场景可能导致认知投入不足；MTurk样本偏技术熟悉；外部效度存疑。

- link_to_next_phase_cn：为缓解人工性和低风险问题，需要在真实用户、真实注册流程中验证，因此进入Study 3现场实验。

##### evidence_pointers

1. Section 5.1-5.3

2. Tables 3-4

3. Online Appendices E.1-E.4

#### 4. Study 3：现场随机实验证明使用（proof of use）

- order：4

- name_cn：Study 3：现场随机实验证明使用（proof of use）

- question_cn：在真实网站注册情境中，ELM增强型密码强度计是否能继续改善用户的密码生成行为？

- inputs_and_setting_cn：与亚洲一个在线本地折扣论坛合作；30天内310名真实新用户，排除2名忘记密码用户后308名（控制76、Time 79、Rank 78、Probability 75）；仅Forum场景；按session ID末位模4随机分配；通过Chinese wall模型只采集密码强度而非密码本身，并通过两个API过滤未登录及忘记密码用户。

- designed_or_compared_object_cn：与传统强度标签控制相比的四类密码强度计；只分析强度增量和密码修改次数两个行为指标。

- baseline_control_or_counterfactual_cn：控制组为传统强度标签；由于法律限制无法收集用户个人信息，故无人口统计控制变量；事后用Bonferroni校正做多重比较。

##### objective_metrics

1. 密码强度自然对数增量

2. 看到消息后修改密码的次数

- analysis_method_cn：ANOVA检验处理间总体差异；Bonferroni校正后的post hoc成对比较；补充控制初始密码强度的稳健性分析。

- main_result_cn：总体ANOVA对两个指标均显著；Rank在强度增量（均值差0.186, p=0.007）和修改次数（均值差0.393, p=0.004）上显著优于控制；Time和Probability在强度增量上边缘显著（p<0.10），Probability在修改次数上不显著。

- argumentative_role_cn：在真实环境、真实风险和非知情同意条件下验证设计，尤其确认Rank的稳定效果，完成proof of use。

- remaining_uncertainty_cn：无法加入控制变量；只观察到注册时刻的强度与修改次数，无法观察长期行为或密码复用；单一国家、单一论坛、Forum场景；对Time和Probability的证据强度较弱。

- link_to_next_phase_cn：将现场验证结果带回理论讨论，解释为何Rank最优，并提炼设计知识与实践含义。

##### evidence_pointers

1. Section 6

2. Tables 5-6

3. Online Appendices D, E.3, E.6

## 各部分修辞架构

### abstract_moves

#### 1. Abstract S1

- move_code：CONTEXT

- paraphrase_cn：指出密码认证是最常用的系统访问方式。

- locator：Abstract S1

#### 2. Abstract S2

- move_code：PRACTICAL_STAKES

- paraphrase_cn：强调多数密码弱，推动用户生成强密码是巨大挑战。

- locator：Abstract S2

#### 3. Abstract S3

- move_code：THEORY_INTRO

- paraphrase_cn：提出以ELM指导的增强型密码强度计设计。

- locator：Abstract S3

#### 4. Abstract S4

- move_code：STUDY_OVERVIEW

- paraphrase_cn：预告用survey、实验室实验和现场实验分别建立proof of concept、proof of value和proof of use。

- locator：Abstract S4

#### 5. Abstract S5

- move_code：RESULT

- paraphrase_cn：报告用户更可能修改密码且新密码更强。

- locator：Abstract S5

#### 6. Abstract S6

- move_code：CONTRIBUTION

- paraphrase_cn：主张该设计是促进终端用户安全密码行为的有效方法。

- locator：Abstract S6

### introduction_moves

#### 1. Introduction P1 S1

- move_code：CONTEXT

- paraphrase_cn：密码是组织访问控制的主导认证机制。

- locator：Introduction P1 S1

#### 2. Introduction P1 S2

- move_code：PRACTICAL_STAKES

- paraphrase_cn：密码安全问题对组织关键，提升用户生成密码行为的技巧有价值。

- locator：Introduction P1 S2

#### 3. Introduction P1 S3-S7

- move_code：LIMITATION

- paraphrase_cn：有专家认为密码很快过时，但现实证据相反；密码管理器存在漏洞，多因素认证成本过高。

- locator：Introduction P1 S3-S7

#### 4. Introduction P2 S1

- move_code：PHENOMENON

- paraphrase_cn：注意力重新转向密码强度计这类说服性技术。

- locator：Introduction P2 S1

#### 5. Introduction P2 S2-S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：提出设计一种由公认心理学理论驱动、不依赖密码复杂度政策、且低成本易部署的增强型强度计。

- locator：Introduction P2 S2-S3

#### 6. Introduction P3 S1

- move_code：CONTEXT

- paraphrase_cn：描述密码强度计基本功能是计算复杂度并显示强弱。

- locator：Introduction P3 S1

#### 7. Introduction P3 S2-S3

- move_code：LIMITATION

- paraphrase_cn：先前文献显示强度计在受控环境下有效，但现实中弱密码问题仍持续。

- locator：Introduction P3 S2-S3

#### 8. Introduction P3 S4-S6

- move_code：GAP

- paraphrase_cn：现有改进集中于增强算法和强度测量精度，而非呈现组件。

- locator：Introduction P3 S4-S6

#### 9. Introduction P4 S1-S2

- move_code：GAP

- paraphrase_cn：理论性的强度计界面设计指导稀缺，强度计实现像黑箱。

- locator：Introduction P4 S1-S2

#### 10. Introduction P4 S3-S4

- move_code：THEORY_INTRO

- paraphrase_cn：引入ELM并采用设计科学方法发展理论指导的强度计设计。

- locator：Introduction P4 S3-S4

#### 11. Introduction P4 S5

- move_code：RESULT

- paraphrase_cn：预告该设计能推动用户更早修改密码并选择更强密码。

- locator：Introduction P4 S5

#### 12. Introduction P5 S1-S4

- move_code：CONTRIBUTION

- paraphrase_cn：声明理论与实践贡献：为强度计影响用户建立理论基础，且实现只需客户端小改。

- locator：Introduction P5 S1-S4

#### 13. Introduction P6

- move_code：STUDY_OVERVIEW

- paraphrase_cn：预告论文结构：概念设计、实现与评价、三项实验、讨论。

- locator：Introduction P6

### theory_and_knowledge_moves

#### 1. Section 2.1 P1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：回顾视觉线索（颜色、进度条、雷达、表情符号）能吸引注意并改善密码行为。

- locator：Section 2.1 P1

#### 2. Section 2.1 P2

- move_code：LIMITATION

- paraphrase_cn：这些视觉驱动研究缺乏对行为改变背后机制和支撑理论的解释。

- locator：Section 2.1 P2

#### 3. Section 2.2 P1

- move_code：THEORY_INTRO

- paraphrase_cn：把密码强度计视为说服工具，引入ELM作为理论基础。

- locator：Section 2.2 P1

#### 4. Section 2.2 P2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：ELM是双过程理论：边缘路径低精细加工，中心路径高精细加工。

- locator：Section 2.2 P2

#### 5. Section 2.2 P3

- move_code：THEORY_PROPOSITION

- paraphrase_cn：边缘路径导致的态度行为改变肤浅短暂，中心路径导致更显著持久的改变。

- locator：Section 2.2 P3

#### 6. Section 2.2 P4

- move_code：MECHANISM

- paraphrase_cn：已有视觉刺激应走边缘路径，因此效果短暂；IS文献显示中心路径消息在技术采纳和电子病历等领域有效，但几乎无人用于强度计。

- locator：Section 2.2 P4

#### 7. Section 2.3 P1

- move_code：REQUIREMENT

- paraphrase_cn：按Type V设计理论，关键处方是找出并加入可能走中心路径的刺激，例如引发认知好奇的消息。

- locator：Section 2.3 P1

#### 8. Section 2.3 P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：根据文献提出第一类消息：恐惧诉求，用于安全情境可激发认知意识。

- locator：Section 2.3 P2

#### 9. Section 2.3 P3

- move_code：DESIGN_FEATURE

- paraphrase_cn：根据文献提出第二类消息：同伴比较，尤其间接的同伴排名可诱导认知加工。

- locator：Section 2.3 P3

#### 10. Section 2.3 P4

- move_code：DESIGN_FEATURE

- paraphrase_cn：根据文献提出第三类消息：共同纽带，因常用密码更易被猜，能影响用户对风险的认知。

- locator：Section 2.3 P4

#### 11. Section 2.3 P5

- move_code：STUDY_OVERVIEW

- paraphrase_cn：将概念设计转为实际制品，并依次用survey、实验室、现场实验评价。

- locator：Section 2.3 P5

### artifact_design_moves

#### 1. Section 3.1 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：选择backoff Markov模型计算强度，并用RockYou数据集训练，以保证跨处理一致比较。

- locator：Section 3.1 P1

#### 2. Section 3.1 P2-P3

- move_code：DESIGN_FEATURE

- paraphrase_cn：基线强度计显示weak/medium/strong标签，阈值固定为最弱30万和500万。

- locator：Section 3.1 P2-P3

#### 3. Section 3.1 P4

- move_code：DESIGN_FEATURE

- paraphrase_cn：在用户离开输入框时触发强度计算与消息显示，且所有处理使用相同数据和JS逻辑。

- locator：Section 3.1 P4

#### 4. Section 3.2

- move_code：MECHANISM

- paraphrase_cn：Time处理把模型概率换算成100次/秒攻击下的破解时间，以引发恐惧诉求。

- locator：Section 3.2

#### 5. Section 3.3

- move_code：MECHANISM

- paraphrase_cn：Rank处理把密码概率映射为按最弱排名的一位数排名，形成同伴比较。

- locator：Section 3.3

#### 6. Section 3.4

- move_code：MECHANISM

- paraphrase_cn：Probability处理把密码匹配概率换算为10亿账户中相同密码账户数，形成共同纽带。

- locator：Section 3.4

#### 7. Section 3.5 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：因为密码行为动态复杂，采用多方法评价，三研究互补、印证、补偿弱点。

- locator：Section 3.5 P1

#### 8. Section 3.5 P2-P4

- move_code：STUDY_OVERVIEW

- paraphrase_cn：survey用于proof of concept，实验室用于proof of value，现场用于proof of use。

- locator：Section 3.5 P2-P4

#### 9. Section 3.5 P5

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：四项实验均采用between-subjects随机分配：控制组仅强度标签，三个处理分别加Time、Rank、Probability消息；仅要求密码长度至少6位，无其他复杂度要求。

- locator：Section 3.5 P5

### evaluation_moves

#### 1. Section 4 P1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：Study 1回答消息是否被中心路径加工，采用探索性survey。

- locator：Section 4 P1

#### 2. Section 4.1 P1-P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：借用Johnston & Warkentin和Cho等的已成熟构念并做语境化修改，以检验消息显著性。

- locator：Section 4.1 P1-P2

#### 3. Section 4.1 P3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：若处理组与控制组在安全构念关系上有差异，则说明消息被中心加工。

- locator：Section 4.1 P3

#### 4. Section 4.3 P1-P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：采用PLS多组分析并做bootstrap，以比较各处理与控制组的路径系数。

- locator：Section 4.3 P1-P2

#### 5. Section 4.3 P3-P4

- move_code：RESULT

- paraphrase_cn：三个处理组与控制组的显著差异不重叠，且与各自消息含义一致。

- locator：Section 4.3 P3-P4

#### 6. Section 4.3 P5

- move_code：TRANSITION

- paraphrase_cn：既然消息被仔细加工，下一步应测试行为改变。

- locator：Section 4.3 P5

#### 7. Section 5 P1-P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：实验室随机实验可最小化混淆和选择效应，MTurk样本具有可验证代表性。

- locator：Section 5 P1-P2

#### 8. Section 5.1 P1-P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：采用强度增量而非最终强度作为指标，避免把初始就强且未改密码的用户与由弱改强的用户混淆。

- locator：Section 5.1 P1-P2

#### 9. Section 5.1 P3-P4

- move_code：DESIGN_FEATURE

- paraphrase_cn：把密码修改次数和点击Tips链接作为另外两个行为指标，体现推动用户脱离旧习惯的作用。

- locator：Section 5.1 P3-P4

#### 10. Section 5.2.1

- move_code：DESIGN_FEATURE

- paraphrase_cn：用Forum、Restaurant、Bank三个敏感度递进的假设场景增强任务真实感并检验情境差异。

- locator：Section 5.2.1

#### 11. Section 5.3 P1-P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：采用线性、Poisson和logistic回归分别对应三个因变量，并控制人口统计和初始强度。

- locator：Section 5.3 P1-P2

#### 12. Section 5.3 P3

- move_code：RESULT

- paraphrase_cn：Rank显著提高强度增量和修改次数；Forum场景优于Bank；Tips点击无显著差异。

- locator：Section 5.3 P3

#### 13. Section 5.3 P4-P7

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：加入初始强度标签后Rank仍显著，并做learn_more控制、中介、调节和熵替代测量，结果定性一致。

- locator：Section 5.3 P4-P7

#### 14. Section 5.3 P8

- move_code：TRANSITION

- paraphrase_cn：实验室的知情同意和低风险可能导致外部效度问题，需用现场实验验证。

- locator：Section 5.3 P8

#### 15. Section 6 P1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：与亚洲在线论坛合作进行现场随机实验。

- locator：Section 6 P1

#### 16. Section 6 P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：使用Chinese wall模型只采集密码强度而非密码，并用API验证登录和忘记密码行为，既合法规又保持真实。

- locator：Section 6 P2

#### 17. Section 6 P3

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：30天共308名用户纳入分析，排除未登录和忘记密码用户。

- locator：Section 6 P3

#### 18. Section 6 P4-P5

- move_code：RESULT

- paraphrase_cn：ANOVA总体显著；Bonferroni校正后Rank在强度和修改次数上均显著，Time和Probability仅部分边缘显著。

- locator：Section 6 P4-P5

### discussion_and_contribution_moves

#### 1. Section 7.1

- move_code：RESULT

- paraphrase_cn：总结三项研究互补：survey证明消息被仔细加工，实验室与现场一致显示Rank最优。

- locator：Section 7.1

#### 2. Section 7.2 P1

- move_code：CONTRIBUTION

- paraphrase_cn：提出第一个理论贡献：为密码强度计如何影响用户行为提供ELM理论基础。

- locator：Section 7.2 P1

#### 3. Section 7.2 P2

- move_code：CONTRIBUTION

- paraphrase_cn：第二项理论贡献：将ELM扩展到数字情境，发现刺激有效性是情境依赖的，同伴比较优于其他刺激。

- locator：Section 7.2 P2

#### 4. Section 7.3

- move_code：CONTRIBUTION

- paraphrase_cn：管理含义：增强消息可显著降低暴力破解风险，且部署成本低、兼容任何现有强度计算法。

- locator：Section 7.3

#### 5. Section 7.4

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：承认survey是探索性、MTurk样本偏技术、未追踪点击Tips后行为、消息类型不穷尽、仅用RockYou训练、未与其他非传统强度计比较。

- locator：Section 7.4

## 理论/知识到设计的翻译

### 知识/理论基础

1. ELM（Petty & Cacioppo 1986）

2. 设计科学理论（Gregor 2006 Type V theory; Gregor & Hevner 2013）

3. 恐惧诉求与保护动机相关实证（Ruiter et al. 2001; Johnston & Warkentin 2010; Boss et al. 2015）

4. 社会比较理论（Festinger 1954）及同伴比较应用（Petty et al. 1991）

5. 共同纽带与风险沟通（Pinkas & Sander 2002; Slovic et al. 2000; Visschers et al. 2009）

6. 概率密码模型与密码强度测量（Ma et al. 2014; Ur et al. 2015）

7. 密码强度计视觉呈现研究（Ur et al. 2012; Golla et al. 2018; Furnell et al. 2018）

- 理论—设计耦合：direct

- 耦合判定理由：ELM在设计之前就决定了'使用中心路径刺激'这一核心设计原则，三种消息类型均从ELM相关实证文献直接推导而来，评价也围绕这些消息是否被中心加工及其行为后果展开，因此属于direct而非事后标签。

- 理论到设计翻译链：ELM中心/边缘路径区分 → 传统视觉提示被归为边缘路径且效果短暂 → 设计应使用中心路径消息 → 从ELM文献选出恐惧诉求、同伴比较、共同纽带三类消息 → 在保持密码算法和强度标签不变的前提下，将消息分别操作化为Time、Rank、Probability → 随机实验比较各处理与仅显示标签的控制组 → 结果一致支持Rank，并在讨论中将这一优势解释为数字情境中社会比较的重要性，回到并修正ELM。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：ELM指出中心路径加工产生更深刻和持久的态度与行为改变，边缘路径改变短暂。

- mechanism_cn：引发用户认知精细加工的刺激能提高对密码安全含义的理解，从而促使更持久的行为改变。

- design_requirement_cn：密码强度计不应只依赖视觉刺激，应加入能引发认知思考的消息。

- artifact_choice_cn：保留传统强度标签，在消息区叠加理论驱动的提示文本。

- evaluated_contrast_cn：增强型强度计 vs 仅标签的控制组。

- objective_result_cn：Study 1显示消息被仔细加工；Study 2/3显示增强型设计整体有效，Rank最稳。

##### evidence_pointers

1. Section 2.2-2.3

2. Tables 2, 3, 6

#### 2. 2

- theory_or_knowledge_claim_cn：恐惧诉求能激发认知意识并促进安全应对行为。

- mechanism_cn：感知威胁严重性和易感性让用户意识到弱密码可被快速破解。

- design_requirement_cn：告知用户其密码被破解所需的估计时间。

- artifact_choice_cn：Time处理：显示在100次/秒攻击下破解时间，如10秒。

- evaluated_contrast_cn：Time vs Control。

- objective_result_cn：Study 1激活易感性与脆弱性相关路径；Study 2不显著；Study 3强度提升边缘显著。

##### evidence_pointers

1. Section 3.2

2. Table 2

3. Table 3

4. Table 6

#### 3. 3

- theory_or_knowledge_claim_cn：同伴比较通过社会比较过程诱导认知加工并促进行为改变。

- mechanism_cn：排名信息让用户把自己放在与他人的比较中，产生压力和行动动机。

- design_requirement_cn：显示用户密码在所有密码中的相对强弱排名。

- artifact_choice_cn：Rank处理：把密码映射为最弱密码中的第300名等一位数排名。

- evaluated_contrast_cn：Rank vs Control。

- objective_result_cn：Study 2显著提高强度增量与修改次数；Study 3同样显著，是唯一稳定最优处理。

##### evidence_pointers

1. Section 3.3

2. Table 3

3. Table 6

#### 4. 4

- theory_or_knowledge_claim_cn：共同纽带及概率信息影响风险认知；常用密码更容易被猜中。

- mechanism_cn：相同密码账户数越多，用户感知曝光风险越高，促使其修正密码。

- design_requirement_cn：显示用户密码与其他账户的重复概率或人数。

- artifact_choice_cn：Probability处理：在10亿账户假设下显示相同密码账户数。

- evaluated_contrast_cn：Probability vs Control。

- objective_result_cn：Study 1激活自我效能路径；Study 2不显著；Study 3强度提升边缘显著但修改次数不显著。

##### evidence_pointers

1. Section 3.4

2. Table 2

3. Table 3

4. Table 6

## 评价逻辑

### evaluation_modes

1. survey-based between-subjects randomized experiment（proof of concept）

2. controlled randomized laboratory experiment on MTurk（proof of value）

3. randomized field experiment on real online forum（proof of use）

4. robustness analyses：初始强度控制、learn_more控制、中介、调节、熵替代强度、Bonferroni多重比较

- why_these_evaluations_cn：由于密码行为动态复杂，单一方法难以同时保证机制显著性、内部效度和外部效度；因此作者采用互相补充、印证、补偿的多方法链条：survey确认消息走中心路径，实验室随机实验确认因果行为效果，现场实验确认真实环境效果。

- benchmark_and_contrast_chain_cn：所有实验都以传统强度标签为控制组；密码强度计算模型和阈值跨处理固定，保证唯一差异是消息类型；实验室实验加入Bank/Restaurant/Forum场景对照，并加入初始强度标签作为稳健控制；现场实验用ANOVA加Bonferroni校正后的成对比较进一步确认控制vs处理差异。这样从'消息有意义'到'行为有改变'再到'真实环境仍有效'逐层累积证据。

### claim_evidence_ledger

#### 1. 增强型消息可被用户仔细加工，属于中心路径。

- claim_cn：增强型消息可被用户仔细加工，属于中心路径。

- evidence_cn：Survey PLS多组分析显示Time、Rank、Probability与控制组在安全构念路径上的显著差异互不重叠且与消息含义一致。

- evidence_quality_cn：自我报告测量，探索性分析，学生样本；未直接测量认知加工过程。

#### 2. Rank处理显著提高密码强度增量。

- claim_cn：Rank处理显著提高密码强度增量。

- evidence_cn：实验室回归系数0.089（p<0.01），控制初始强度后仍显著；现场成对比较均值差0.186（p=0.007）。

- evidence_quality_cn：两个随机实验证据一致，但现场实验无控制变量。

#### 3. Rank处理显著提高用户修改密码的次数。

- claim_cn：Rank处理显著提高用户修改密码的次数。

- evidence_cn：实验室Poisson系数0.993（p<0.01）；现场修改次数均值差0.393（p=0.004）。

- evidence_quality_cn：随机实验室与现场证据一致。

#### 4. Time和Probability处理也有效果。

- claim_cn：Time和Probability处理也有效果。

- evidence_cn：Study 3中两者在强度提升上边缘显著（p<0.10）；Study 2中两者不显著；Probability在修改次数上不显著。

- evidence_quality_cn：效应较弱且不稳定，作者也提示谨慎解释。

#### 5. 效果来自消息呈现而非强度算法改进。

- claim_cn：效果来自消息呈现而非强度算法改进。

- evidence_cn：所有处理使用相同算法、阈值和强度标签，唯一区别是额外消息文本。

- evidence_quality_cn：实验设计控制充分，但现场仍可能存在未观察混淆。

#### 6. 设计部署成本低、兼容现有算法。

- claim_cn：设计部署成本低、兼容现有算法。

- evidence_cn：实现描述为客户端JavaScript/AJAX计算，无需服务器新硬件。

- evidence_quality_cn：来自实现描述，不是正式成本收益分析。

- internal_validity_strategy_cn：采用随机分配、between-subjects设计；密码强度计算和阈值在所有处理间固定；实验室实验使用控制变量（年龄、性别、教育、初始强度标签），补充learn_more、中介、调节和替代强度度量；现场实验用session ID随机分配并通过API过滤未登录和忘记密码用户。

- external_validity_strategy_cn：使用三种不同样本来源（学生、MTurk、真实亚洲论坛用户）；两种以上场景（假设论坛、餐厅、银行和真实论坛）；现场实验在真实注册流程、真实风险、无需知情同意的条件下进行；通过proof of use表明结果可推广到真实环境。

- what_is_not_actually_tested_cn：未直接测量中心路径加工本身；未追踪用户点击Tips后的学习与后续密码复用；未观察长期行为持久性；现场无法控制用户特征；未与其他非传统密码强度计或更先进算法比较；只覆盖论坛类低敏感场景。

## 贡献闭环

- technical_claim_cn：在不改变密码强度算法的前提下，通过增加理论驱动的消息文本可以提高用户密码生成行为。

- artifact_claim_cn：Rank（同伴比较消息）是三种增强型设计中最稳定有效的制品设计；Time和Probability仅在部分情况下有边缘效果。

- mechanism_claim_cn：增强消息之所以有效，是因为它们比传统视觉刺激更可能被用户以ELM中心路径加工，从而产生更显著的行为改变。

- boundary_claim_cn：该效果在实验室和真实论坛场景中均存在；在低敏感（Forum）场景中，强度提升反而比高敏感（Bank）场景更明显；数字情境下社会比较类刺激更有效。

- reusable_design_knowledge_cn：设计密码强度计时，可在保留原有算法和标签的基础上，把用户密码的排名作为轻量级消息加入；任何已部署的强度计都能以最小客户端改动复用该原则。

- theoretical_contribution_cn：为密码强度计影响用户行为提供ELM理论基础；将ELM扩展至数字安全情境，指出信息刺激的有效性依赖社会与社区情境，同伴比较可能比恐惧诉求和共同纽带更有效。

- how_discussion_closes_intro_gap_cn：引言指出强度计界面设计缺乏理论指导，讨论部分用ELM解释传统视觉刺激为何效果短暂，并用三级证据证明新的理论驱动消息有效，从而闭合缺口；同时把最强处理效应回接到ELM，提出情境依赖修正，提升理论贡献。

- overclaim_or_unsupported_leaps_cn：主要跳跃包括：由survey自我报告差异推断中心路径加工；Study 2中Time和Probability不显著，但仍以现场边缘显著和方向一致支持整体设计；把Rank最优解释为数字社会比较重要，属于事后解释而非预先假设检验；现场没有控制变量，却仍将其解释为对外部效度的确认。

## 句级写作动作图谱

### 1. Abstract S1

- order：1

- section：Abstract

- locator：Abstract S1

- move_code：CONTEXT

- paraphrase_cn：密码认证是最常用的安全系统访问方式。

- rhetorical_function_cn：建立问题领域和重要性。

- depends_on_cn：无

- sets_up_cn：为后面的密码弱点问题提供背景。

- evidence_pointer：Abstract S1

### 2. Abstract S2

- order：2

- section：Abstract

- locator：Abstract S2

- move_code：PRACTICAL_STAKES

- paraphrase_cn：经验证据表明多数密码很弱，促使用户创建更强密码是重要挑战。

- rhetorical_function_cn：说明现实后果，使研究动机重要。

- depends_on_cn：密码普遍存在

- sets_up_cn：引出需要设计干预。

- evidence_pointer：Abstract S2

### 3. Abstract S3

- order：3

- section：Abstract

- locator：Abstract S3

- move_code：THEORY_INTRO

- paraphrase_cn：提出用ELM指导增强型密码强度计设计。

- rhetorical_function_cn：预告核心理论工具。

- depends_on_cn：需要更好的密码行为干预

- sets_up_cn：形成理论到设计的主线。

- evidence_pointer：Abstract S3

### 4. Abstract S4

- order：4

- section：Abstract

- locator：Abstract S4

- move_code：STUDY_OVERVIEW

- paraphrase_cn：用survey、实验室实验和现场实验分别建立proof of concept、proof of value和proof of use。

- rhetorical_function_cn：预告三阶段证据链。

- depends_on_cn：提出设计

- sets_up_cn：组织全文结构。

- evidence_pointer：Abstract S4

### 5. Abstract S5

- order：5

- section：Abstract

- locator：Abstract S5

- move_code：RESULT

- paraphrase_cn：用户更可能修改密码，新密码显著更强。

- rhetorical_function_cn：给出核心结论。

- depends_on_cn：三项研究完成

- sets_up_cn：支持贡献声明。

- evidence_pointer：Abstract S5

### 6. Abstract S6

- order：6

- section：Abstract

- locator：Abstract S6

- move_code：CONTRIBUTION

- paraphrase_cn：增强型强度计是促进终端用户安全密码行为的有效方法。

- rhetorical_function_cn：定位总体贡献。

- depends_on_cn：核心结果

- sets_up_cn：吸引读者进入正文。

- evidence_pointer：Abstract S6

### 7. P1 S1

- order：7

- section：Introduction

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：密码是组织实施访问控制的主导认证机制。

- rhetorical_function_cn：从组织视角建立背景。

- depends_on_cn：无

- sets_up_cn：将研究定位在组织信息安全。

- evidence_pointer：Introduction P1 S1

### 8. P1 S2

- order：8

- section：Introduction

- locator：P1 S2

- move_code：PRACTICAL_STAKES

- paraphrase_cn：密码安全相关议题对组织关键，改善用户密码生成行为的技术有价值。

- rhetorical_function_cn：把密码问题转化为组织管理问题。

- depends_on_cn：密码普遍使用

- sets_up_cn：为需要更优密码行为干预提供理由。

- evidence_pointer：Introduction P1 S2

### 9. P1 S3-S7

- order：9

- section：Introduction

- locator：P1 S3-S7

- move_code：LIMITATION

- paraphrase_cn：有专家预言密码过时，但现实案例显示连国务院也难以摆脱密码；密码管理器有漏洞，多因素认证成本上升。

- rhetorical_function_cn：排除替代技术路线，强化密码强度计的重要性。

- depends_on_cn：密码问题重要

- sets_up_cn：把解决希望转移到说服性设计上。

- evidence_pointer：Introduction P1 S3-S7

### 10. P2 S1

- order：10

- section：Introduction

- locator：P2 S1

- move_code：PHENOMENON

- paraphrase_cn：注意力回到增强密码强度计这类说服性技术。

- rhetorical_function_cn：缩小研究焦点到密码强度计。

- depends_on_cn：替代技术不可行

- sets_up_cn：引出本文的具体制品。

- evidence_pointer：Introduction P2 S1

### 11. P2 S2-S3

- order：11

- section：Introduction

- locator：P2 S2-S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：提出设计一种由已知心理学理论驱动、不依赖NIST所不鼓励的复杂度政策、且可低成本广泛部署的增强型强度计。

- rhetorical_function_cn：给出文章目标与设计要求。

- depends_on_cn：焦点在密码强度计

- sets_up_cn：后面的理论选择与实现。

- evidence_pointer：Introduction P2 S2-S3

### 12. P3 S1

- order：12

- section：Introduction

- locator：P3 S1

- move_code：CONTEXT

- paraphrase_cn：解释密码强度计计算输入密码复杂度并显示强度。

- rhetorical_function_cn：为不熟悉该制品的读者提供背景。

- depends_on_cn：本文研究对象是强度计

- sets_up_cn：后续讨论强度计现有问题。

- evidence_pointer：Introduction P3 S1

### 13. P3 S2-S3

- order：13

- section：Introduction

- locator：P3 S2-S3

- move_code：LIMITATION

- paraphrase_cn：先前文献显示强度计在控制环境有效，但现实中弱密码问题持续。

- rhetorical_function_cn：揭示文献效果与现实效果之间的缺口。

- depends_on_cn：强度计基本功能

- sets_up_cn：说明需要改进现有设计。

- evidence_pointer：Introduction P3 S2-S3

### 14. P3 S4-S6

- order：14

- section：Introduction

- locator：P3 S4-S6

- move_code：GAP

- paraphrase_cn：现有改进集中在提高密码强度算法准确性，而不是检验强度计的呈现组件。

- rhetorical_function_cn：把与主流研究区别开。

- depends_on_cn：现实弱密码持续

- sets_up_cn：确定本文切入点是呈现组件。

- evidence_pointer：Introduction P3 S4-S6

### 15. P4 S1-S2

- order：15

- section：Introduction

- locator：P4 S1-S2

- move_code：GAP

- paraphrase_cn：在算法不变时研究呈现组件，并援引Furnell发现：理论上指导的强度计界面设计准则稀缺，现有实现像黑箱。

- rhetorical_function_cn：建立'理论缺口'而非单纯性能缺口。

- depends_on_cn：主流研究集中于算法

- sets_up_cn：论证引入心理学理论正当性。

- evidence_pointer：Introduction P4 S1-S2

### 16. P4 S3-S4

- order：16

- section：Introduction

- locator：P4 S3-S4

- move_code：THEORY_INTRO

- paraphrase_cn：选用ELM，并按设计科学文献发展理论指导的强度计设计。

- rhetorical_function_cn：给出理论和方法范式。

- depends_on_cn：界面设计缺少理论

- sets_up_cn：本文的理论驱动设计方法。

- evidence_pointer：Introduction P4 S3-S4

### 17. P4 S5

- order：17

- section：Introduction

- locator：P4 S5

- move_code：RESULT

- paraphrase_cn：预告该强度计能促使修改密码且新密码更强。

- rhetorical_function_cn：提前给出正面结果，吸引读者。

- depends_on_cn：提出ELM设计

- sets_up_cn：为贡献声明做铺垫。

- evidence_pointer：Introduction P4 S5

### 18. P5 S1-S4

- order：18

- section：Introduction

- locator：P5 S1-S4

- move_code：CONTRIBUTION

- paraphrase_cn：声明理论贡献是建立强度计与用户互动的理论根基，实践贡献是客户端简单修改即可部署。

- rhetorical_function_cn：概括文章贡献层级。

- depends_on_cn：设计、结果

- sets_up_cn：让读者预期贡献类型。

- evidence_pointer：Introduction P5 S1-S4

### 19. P6

- order：19

- section：Introduction

- locator：P6

- move_code：STUDY_OVERVIEW

- paraphrase_cn：介绍后续章节组织：概念设计、实现、三项实验和讨论。

- rhetorical_function_cn：提供阅读路线图。

- depends_on_cn：有多个研究阶段

- sets_up_cn：全文结构。

- evidence_pointer：Introduction P6

### 20. P1

- order：20

- section：Section 2.1

- locator：P1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：已有研究显示颜色、大小、雷达、计速表、跳舞兔子等视觉线索可吸引用户注意并改善密码行为。

- rhetorical_function_cn：总结与本研究最接近的已有工作。

- depends_on_cn：本文聚焦呈现组件

- sets_up_cn：接下来指出这些工作缺乏理论机制。

- evidence_pointer：Section 2.1 P1

### 21. P2

- order：21

- section：Section 2.1

- locator：P2

- move_code：LIMITATION

- paraphrase_cn：这些视觉驱动研究对行为改变的底层机制和支撑理论缺乏解释。

- rhetorical_function_cn：指出文献缺口。

- depends_on_cn：视觉线索研究

- sets_up_cn：引入ELM的必要性。

- evidence_pointer：Section 2.1 P2

### 22. P1

- order：22

- section：Section 2.2

- locator：P1

- move_code：THEORY_INTRO

- paraphrase_cn：将密码强度计定义为试图说服用户改变密码行为的工具，因此采用ELM。

- rhetorical_function_cn：从'工具功能'过渡到'说服理论'。

- depends_on_cn：需要理论解释机制

- sets_up_cn：后续双路径论述。

- evidence_pointer：Section 2.2 P1

### 23. P2-P3

- order：23

- section：Section 2.2

- locator：P2-P3

- move_code：THEORY_PROPOSITION

- paraphrase_cn：ELM是双过程理论：边缘路径低精细加工，中心路径高精细加工，二者导致的行为改变持久性不同。

- rhetorical_function_cn：陈述理论的机理性命题。

- depends_on_cn：ELM引入

- sets_up_cn：用它分类现有视觉刺激。

- evidence_pointer：Section 2.2 P2-P3

### 24. P4

- order：24

- section：Section 2.2

- locator：P4

- move_code：MECHANISM

- paraphrase_cn：已有视觉刺激应属边缘路径，因此效果短暂；IS文献中中心路径消息在技术采纳和电子病历中有效，但尚无用于强度计的尝试。

- rhetorical_function_cn：把理论用于解释现象并再次定位缺口。

- depends_on_cn：双路径命题

- sets_up_cn：为概念设计提供依据。

- evidence_pointer：Section 2.2 P4

### 25. P1

- order：25

- section：Section 2.3

- locator：P1

- move_code：REQUIREMENT

- paraphrase_cn：按设计科学Type V理论，关键处方是识别并加入可能走中心路径的刺激。

- rhetorical_function_cn：把理论转成设计原则。

- depends_on_cn：中心路径更有效

- sets_up_cn：选择具体消息类型。

- evidence_pointer：Section 2.3 P1

### 26. P2

- order：26

- section：Section 2.3

- locator：P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：提出第一类消息：恐惧诉求，在安全情境中能激发认知意识。

- rhetorical_function_cn：从文献生成具体设计候选。

- depends_on_cn：中心路径设计原则

- sets_up_cn：Time处理。

- evidence_pointer：Section 2.3 P2

### 27. P3

- order：27

- section：Section 2.3

- locator：P3

- move_code：DESIGN_FEATURE

- paraphrase_cn：提出第二类消息：同伴比较，主要通过间接的比较性压力诱导认知。

- rhetorical_function_cn：从文献生成第二个设计候选。

- depends_on_cn：中心路径设计原则

- sets_up_cn：Rank处理。

- evidence_pointer：Section 2.3 P3

### 28. P4

- order：28

- section：Section 2.3

- locator：P4

- move_code：DESIGN_FEATURE

- paraphrase_cn：提出第三类消息：共同纽带，因常用密码更易被猜，可影响用户风险认知。

- rhetorical_function_cn：从文献生成第三个设计候选。

- depends_on_cn：中心路径设计原则

- sets_up_cn：Probability处理。

- evidence_pointer：Section 2.3 P4

### 29. P5

- order：29

- section：Section 2.3

- locator：P5

- move_code：STUDY_OVERVIEW

- paraphrase_cn：将概念设计转为具体制品的situated implementation，并计划用survey、实验室、现场三阶段评价。

- rhetorical_function_cn：连接概念设计与实证安排。

- depends_on_cn：三类消息

- sets_up_cn：Section 3实现与Section 4-6实验。

- evidence_pointer：Section 2.3 P5

### 30. P1

- order：30

- section：Section 3.1

- locator：P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：采用backoff Markov模型并训练于RockYou数据集，以保持跨处理一致且接近真实。

- rhetorical_function_cn：为基线强度计的技术选择辩护。

- depends_on_cn：需要统一的强度度量

- sets_up_cn：确保后续比较公平。

- evidence_pointer：Section 3.1 P1

### 31. P2-P3

- order：31

- section：Section 3.1

- locator：P2-P3

- move_code：DESIGN_FEATURE

- paraphrase_cn：基线强度计显示weak/medium/strong标签，阈值固定在最弱30万与500万之间，所有处理相同。

- rhetorical_function_cn：给出控制条件的操作定义。

- depends_on_cn：统一强度模型

- sets_up_cn：作为后续所有比较的基准。

- evidence_pointer：Section 3.1 P2-P3

### 32. P4

- order：32

- section：Section 3.1

- locator：P4

- move_code：DESIGN_FEATURE

- paraphrase_cn：在输入框失去焦点时触发强度计算与消息显示，所有处理采用同一段JS/AJAX逻辑。

- rhetorical_function_cn：说明实现时机和统一性。

- depends_on_cn：基线强度计

- sets_up_cn：保证消息是唯一变化。

- evidence_pointer：Section 3.1 P4

### 33. P1-P3

- order：33

- section：Section 3.2

- locator：P1-P3

- move_code：MECHANISM

- paraphrase_cn：Time处理将模型概率转为100次/秒攻击下的破解时间，通过感知易感性和脆弱性触发恐惧诉求。

- rhetorical_function_cn：把恐惧诉求理论操作化为具体消息。

- depends_on_cn：恐惧诉求设计候选

- sets_up_cn：实验中Time处理的预期机制。

- evidence_pointer：Section 3.2

### 34. P1-P3

- order：34

- section：Section 3.3

- locator：P1-P3

- move_code：MECHANISM

- paraphrase_cn：Rank处理将密码概率映射为最弱密码中的一位数排名，通过比较压力促使用户改变。

- rhetorical_function_cn：把同伴比较理论操作化为排名消息。

- depends_on_cn：同伴比较设计候选

- sets_up_cn：实验中Rank处理的预测。

- evidence_pointer：Section 3.3

### 35. P1-P3

- order：35

- section：Section 3.4

- locator：P1-P3

- move_code：MECHANISM

- paraphrase_cn：Probability处理将匹配概率换算为10亿账户中相同密码账户数，通过共同纽带感知风险。

- rhetorical_function_cn：把共同纽带理论操作化为概率消息。

- depends_on_cn：共同纽带设计候选

- sets_up_cn：实验中Probability处理的预测。

- evidence_pointer：Section 3.4

### 36. P1

- order：36

- section：Section 3.5

- locator：P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：由于密码行为动态复杂，采用多方法评价，各研究互补、印证、补偿。

- rhetorical_function_cn：为三研究设计提供总体理由。

- depends_on_cn：设计已完成

- sets_up_cn：Study 1/2/3安排。

- evidence_pointer：Section 3.5 P1

### 37. P2-P4

- order：37

- section：Section 3.5

- locator：P2-P4

- move_code：STUDY_OVERVIEW

- paraphrase_cn：survey用于proof of concept，实验室用于proof of value，现场用于proof of use。

- rhetorical_function_cn：预告证据链三个环节。

- depends_on_cn：多方法理由

- sets_up_cn：Section 4-6结构。

- evidence_pointer：Section 3.5 P2-P4

### 38. P5

- order：38

- section：Section 3.5

- locator：P5

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：所有实验采用between-subjects随机分配：控制组仅强度标签，三个处理组合并添加Time/Rank/Probability消息；只要求密码长度至少6位。

- rhetorical_function_cn：明确实验对照与处理变量。

- depends_on_cn：实现好的三种消息

- sets_up_cn：保证结果可归因于消息类型。

- evidence_pointer：Section 3.5 P5

### 39. P1

- order：39

- section：Section 4

- locator：P1

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：Study 1用探索性survey检验消息是否被仔细加工，以此作为后续研究的proof of concept。

- rhetorical_function_cn：确定Study 1的功能。

- depends_on_cn：中心路径风险

- sets_up_cn：survey设计和结果。

- evidence_pointer：Section 4 P1

### 40. P1-P2

- order：40

- section：Section 4.1

- locator：P1-P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：借用Johnston & Warkentin和Cho等的安全构念，并与ELM结合，用以判断消息的加工路径。

- rhetorical_function_cn：说明为何选择这些构念。

- depends_on_cn：需要测量消息显著性

- sets_up_cn：survey问卷结构。

- evidence_pointer：Section 4.1 P1-P2

### 41. P1-P2

- order：41

- section：Section 4.2

- locator：P1-P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：学生参与者看假设论坛注册场景的强度计截图后填写1-7点Likert量表。

- rhetorical_function_cn：描述survey实施方式。

- depends_on_cn：借用的构念

- sets_up_cn：数据收集与样本量。

- evidence_pointer：Section 4.2

### 42. P1-P2

- order：42

- section：Section 4.3

- locator：P1-P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用PLS多组分析比较处理组与控制组的路径系数差异。

- rhetorical_function_cn：给出分析方法和工具。

- depends_on_cn：survey数据

- sets_up_cn：Table 2结果。

- evidence_pointer：Section 4.3 P1-P2

### 43. P3-P4

- order：43

- section：Section 4.3

- locator：P3-P4

- move_code：RESULT

- paraphrase_cn：处理组与控制组的显著差异互不重叠，且与各消息含义一致。

- rhetorical_function_cn：报告survey核心发现。

- depends_on_cn：PLS多组分析

- sets_up_cn：认为消息被中心加工。

- evidence_pointer：Section 4.3 P3-P4

### 44. P5

- order：44

- section：Section 4.3

- locator：P5

- move_code：TRANSITION

- paraphrase_cn：既然消息被仔细加工，预期用户行为会改变，因此需要行为实验。

- rhetorical_function_cn：连接survey与实验室实验。

- depends_on_cn：survey结果

- sets_up_cn：进入Study 2。

- evidence_pointer：Section 4.3 P5

### 45. P1-P2

- order：45

- section：Section 5

- locator：P1-P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：受控随机实验能最小化混淆和选择效应，MTurk样本被验证具有代表性。

- rhetorical_function_cn：为实验室方法辩护。

- depends_on_cn：需要行为证据

- sets_up_cn：Study 2设计。

- evidence_pointer：Section 5 P1-P2

### 46. P1-P2

- order：46

- section：Section 5.1

- locator：P1-P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用密码强度增量而非最终强度作为指标，避免把初始强密码和由弱改强的密码混淆。

- rhetorical_function_cn：说明核心指标的选择逻辑。

- depends_on_cn：需要客观行为指标

- sets_up_cn：diff_strength的定义。

- evidence_pointer：Section 5.1 P1-P2

### 47. P3-P4

- order：47

- section：Section 5.1

- locator：P3-P4

- move_code：DESIGN_FEATURE

- paraphrase_cn：把密码修改次数和点击Tips链接作为另外两个指标，反映强度计推动用户脱离旧习惯和增强安全意识。

- rhetorical_function_cn：扩展结果测量的维度。

- depends_on_cn：需要更全面行为测量

- sets_up_cn：num_reset和learn_more的操作化。

- evidence_pointer：Section 5.1 P3-P4

### 48. P1-P3

- order：48

- section：Section 5.2.1

- locator：P1-P3

- move_code：DESIGN_FEATURE

- paraphrase_cn：设计Forum、Restaurant、Bank三个敏感度不同的假设注册场景以增强任务真实感。

- rhetorical_function_cn：在实验室中引入情境变量。

- depends_on_cn：需要现实感

- sets_up_cn：场景对结果的稳健性检验。

- evidence_pointer：Section 5.2.1

### 49. P1-P3

- order：49

- section：Section 5.2.2

- locator：P1-P3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：先做pilot测试并记录完整密码输入历史；参与者被告知密码将被记录且不要使用现有密码。

- rhetorical_function_cn：描述数据收集和伦理约束。

- depends_on_cn：随机实验设计

- sets_up_cn：保证系统有效性和知情同意。

- evidence_pointer：Section 5.2.2

### 50. P1-P2

- order：50

- section：Section 5.3

- locator：P1-P2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用线性、Poisson和logistic回归分别处理连续、计数和二元因变量，并加入人口统计和场景控制。

- rhetorical_function_cn：给出与因变量性质匹配的统计模型。

- depends_on_cn：三类行为指标

- sets_up_cn：Table 3结果。

- evidence_pointer：Section 5.3 P1-P2

### 51. P3

- order：51

- section：Section 5.3

- locator：P3

- move_code：RESULT

- paraphrase_cn：只有Rank显著提高强度增量和修改次数；Forum场景比Bank更促进强度提升；Tips点击无显著差异。

- rhetorical_function_cn：报告实验室核心结果并识别最优处理。

- depends_on_cn：回归模型

- sets_up_cn：对场景效应的进一步稳健分析。

- evidence_pointer：Section 5.3 P3

### 52. P4-P7

- order：52

- section：Section 5.3

- locator：P4-P7

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：控制初始强度标签后Rank仍显著；补充learn_more控制、中介、调节和熵替代强度分析，结果一致。

- rhetorical_function_cn：排除初始密码强度、学习行为、度量方式等替代解释。

- depends_on_cn：主回归结果

- sets_up_cn：结论稳健性。

- evidence_pointer：Section 5.3 P4-P7

### 53. P8

- order：53

- section：Section 5.3

- locator：P8

- move_code：TRANSITION

- paraphrase_cn：实验室存在知情同意、低风险和低认知努力问题，需要用现场实验增强外部效度。

- rhetorical_function_cn：说明实验室局限并引出现场实验。

- depends_on_cn：实验室结果

- sets_up_cn：Study 3。

- evidence_pointer：Section 5.3 P8

### 54. P1

- order：54

- section：Section 6

- locator：P1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：与亚洲在线论坛合作开展现场随机实验，以建立proof of use。

- rhetorical_function_cn：引入第三个实证阶段。

- depends_on_cn：实验室局限

- sets_up_cn：实验合作与设置。

- evidence_pointer：Section 6 P1

### 55. P2

- order：55

- section：Section 6

- locator：P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：采用Chinese wall模型：网站运行时计算密码强度但不存储，研究者只收到系统生成的ID和强度，并用API验证登录和忘记密码。

- rhetorical_function_cn：说明在合规限制下保持现场真实性的实现。

- depends_on_cn：现场实验目标

- sets_up_cn：数据可用性与限制。

- evidence_pointer：Section 6 P2

### 56. P3

- order：56

- section：Section 6

- locator：P3

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：30天共310名用户创建账户，排除未登录和忘记密码用户后纳入308名。

- rhetorical_function_cn：给出样本和筛选逻辑。

- depends_on_cn：现场数据规则

- sets_up_cn：ANOVA结果。

- evidence_pointer：Section 6 P3

### 57. P4-P5

- order：57

- section：Section 6

- locator：P4-P5

- move_code：RESULT

- paraphrase_cn：总体ANOVA显著；Bonferroni校正后Rank在强度和修改次数上都显著，Time和Probability在强度上边缘显著。

- rhetorical_function_cn：报告现场验证结果。

- depends_on_cn：308名用户数据

- sets_up_cn：讨论部分对证据的综合。

- evidence_pointer：Section 6 P4-P5

### 58. P1-P2

- order：58

- section：Section 7.1

- locator：P1-P2

- move_code：RESULT

- paraphrase_cn：三项研究互补：survey证明消息被仔细加工，实验室和现场一致显示Rank最优。

- rhetorical_function_cn：总结整套证据链。

- depends_on_cn：三个研究结果

- sets_up_cn：理论贡献讨论。

- evidence_pointer：Section 7.1

### 59. P1

- order：59

- section：Section 7.2

- locator：P1

- move_code：CONTRIBUTION

- paraphrase_cn：第一项理论贡献是为密码强度计如何影响用户行为建立ELM基础。

- rhetorical_function_cn：声明对IS文献的贡献。

- depends_on_cn：三项研究

- sets_up_cn：支持文章不是一次性性能结果。

- evidence_pointer：Section 7.2 P1

### 60. P2

- order：60

- section：Section 7.2

- locator：P2

- move_code：CONTRIBUTION

- paraphrase_cn：第二项贡献是扩展ELM到数字情境，提出刺激有效性受情境影响，同伴比较在数字环境中更有效。

- rhetorical_function_cn：把实证结果反哺理论。

- depends_on_cn：Rank最优的结果

- sets_up_cn：ELM研究未来方向。

- evidence_pointer：Section 7.2 P2

### 61. P1-P3

- order：61

- section：Section 7.3

- locator：P1-P3

- move_code：CONTRIBUTION

- paraphrase_cn：管理含义是强度增加可显著推迟暴力破解，部署成本低，且在低敏感网站也有用。

- rhetorical_function_cn：给出实践贡献。

- depends_on_cn：现场和实验室结果

- sets_up_cn：实践者应用依据。

- evidence_pointer：Section 7.3

### 62. P1

- order：62

- section：Section 7.4

- locator：P1

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：承认survey探索性、MTurk样本偏技术、未追踪Tips点击后行为、消息类型不穷尽、密码训练集单一、未比较其他强度计。

- rhetorical_function_cn：保护贡献不被过度一般化。

- depends_on_cn：全文证据

- sets_up_cn：未来研究议程。

- evidence_pointer：Section 7.4

## 写作技术

- gap_construction_cn：先构造实践缺口（弱密码持续、替代技术不可行），再构造理论缺口（强度计呈现组件没有理论指导、视觉刺激只走边缘路径），最后把缺口定位在'中心路径消息缺位'，使ELM成为自然解决方案。

- signposting_cn：摘要和引言反复使用proof of concept、proof of value、proof of use三个路标；每章开头说明本阶段任务，章节末说明为何还需要下一实验；Table 1在实验开始前就给出处理到消息的映射。

- transition_logic_cn：从视觉刺激有效但缺理论→ELM；从理论命题→设计原则；从概念设计→具体实现；从survey的自我报告差异→行为实验；从实验室的人工性和低风险→现场实验；从现场结果→理论和实践含义。

- claim_evidence_rhythm_cn：先陈述理论期望，再报告统计系数和p值；对显著结果强调重复证据，对不显著结果不回避，而用现场边缘显著和方向一致性补充；讨论时把最强的Rank结果作为核心结论。

- benchmark_narrative_cn：控制组不是空处理，而是保留标准强度标签的传统强度计；通过强调算法、阈值、标签在所有处理中固定，使消息成为唯一差异；现场实验又用Bonferroni校正保证保守性。

- theory_return_cn：在讨论中把Rank最优解释为数字情境中社会比较的重要性，从而将实证结果从'哪个消息最好'上升为'ELM刺激有效性依赖情境'的理论命题。

- contribution_positioning_cn：用'第一批建立密码强度计理论基础'和'last research mile'提升贡献层级；把简单消息修改定位为低成本、可兼容任意算法的设计科学成果。

- novelty_protection_cn：通过算法不变、理论先导、三方法互补、现场验证、Rank稳定性，防止贡献被解读为一次性性能改进或偶然结果。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：从现实系统中找持续失败的问题，并说明替代技术成本或副作用。

- research_job_cn：收集行业案例、安全报告和既有技术缺陷证据。

- required_evidence_cn：至少一个现实持续问题和一个或多个替代方案失败的证据。

- transition_to_next_cn：把问题收窄到某个可修改的IT制品组件。

#### 2. 2

- step：2

- writing_job_cn：选择能解释现有制品为何不充分的理论，并展示该理论能生成新设计原则。

- research_job_cn：做领域内的理论文献综述，指出既有设计缺少理论机制。

- required_evidence_cn：已有制品的机制缺口，而非简单的性能不足。

- transition_to_next_cn：把理论命题翻译为设计处方。

#### 3. 3

- step：3

- writing_job_cn：把理论处方转成多个可独立操作的设计变体，并保留只改变一个维度的控制条件。

- research_job_cn：实现制品，明确算法、界面、阈值和对照条件。

- required_evidence_cn：可部署的实现和明确的处理-控制差异。

- transition_to_next_cn：先验证设计是否激活了理论预期机制。

#### 4. 4

- step：4

- writing_job_cn：用survey或小样本研究检验用户是否按理论预期的机制加工设计。

- research_job_cn：借用成熟构念自我报告，比较处理组与控制组的构念关系。

- required_evidence_cn：处理组与控制组在理论相关构念上出现与设计含义一致的差异。

- transition_to_next_cn：机制成立后，才进入行为结果检验。

#### 5. 5

- step：5

- writing_job_cn：用受控随机实验检验客观行为效果，并定义能反映改善过程而非最终状态的指标。

- research_job_cn：设计注册任务、记录行为日志、使用与因变量性质匹配的回归模型。

- required_evidence_cn：至少一种设计变体在行为指标上显著优于控制，且稳健性分析成立。

- transition_to_next_cn：为应对外部效度质疑，进入现场实验。

#### 6. 6

- step：6

- writing_job_cn：在真实平台或真实用户中进行随机现场验证，并说明伦理合规措施。

- research_job_cn：与平台合作，在合规前提下保留随机分配和行为测量。

- required_evidence_cn：最优设计在现场环境中重复显著效果，且有筛选和多重比较校正。

- transition_to_next_cn：把现场结果带回理论讨论。

#### 7. 7

- step：7

- writing_job_cn：在讨论中把结果反哺理论，明确边界条件、设计知识和实践成本。

- research_job_cn：识别效应最强和最弱的设计，解释情境依赖，列出未检验假设。

- required_evidence_cn：跨研究一致的模式和至少一项对理论的修正或细化。

- transition_to_next_cn：结束文章并留给未来研究。

### most_transferable_moves_cn

1. 用理论重新解释现有制品为什么实际效果有限，而不是单纯宣称技术更好。

2. 把同一个理论翻译成多个可操作消息，并保持算法和基准条件不变。

3. 使用强度增量而非最终强度，避免把不同初始状态用户混为一谈。

4. 按proof of concept、proof of value、proof of use组织证据链，每阶段回答前一阶段留下的问题。

5. 在讨论中用最优处理的结果反哺理论，提出情境依赖命题。

### resource_intensive_or_nonstandard_parts_cn

1. 需要真实网站伙伴开展现场实验并处理法律合规（Chinese wall模型、不收集密码、API验证）。

2. 需要大规模真实密码数据集（RockYou）训练概率模型。

3. 需要MTurk样本、Qualtrics survey、PLS软件和浏览器端事件日志系统。

4. 需要多轮补充分析（中介、调节、替代强度测量）才能支撑结论稳健性。

### what_not_to_copy_superficially_cn

1. 不要只给消息贴ELM标签而不做survey证明它被中心加工。

2. 不要直接宣称所有处理都有效；Time和Probability在实验室不显著，需要如实报道。

3. 不要在field实验没有控制变量时过度解释效应大小。

4. 不要只报告最终密码强度而忽略初始状态。

5. 不要在没有真实平台合作时声称完成proof of use。

- single_best_description_of_the_routine_cn：用一个心理学理论重新解释既有安全提示为何效果有限，把理论命题转成三种可落地的消息设计，再用从问卷到现场的三阶段因果证据链证明设计有效，最后把现场结果反哺为对理论情境依赖性的修正。

## 分析边界

文章正文完整，但图1-4为占位符，附录A-F未纳入全文，无法核实部分测量题目、稳健性分析细节和在线附录结果；Table 2的OCR可能不完整。以上判断基于正文、表格和作者描述。
