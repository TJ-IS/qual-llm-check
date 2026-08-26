# Optional Verification and Signaling in Online Matching Markets: Evidence from a Randomized Field Experiment

- 作者：Lanfei Shi; Siva Viswanathan
- 年份 / 期刊：2023 / Information Systems Research
- DOI：10.1287/isre.2022.1194
- 源文件：28565_2023_optional-verification-and-signaling-in-online-matching-markets-evidence-from-a-randomized-field.md
- 论文主类型：field_intervention_or_platform_experiment
- 主导写作弧线：phenomenon_mechanism_intervention_field_test
- 置信度：0.79

## 文章级论证概况

- 核心问题：在缺乏声誉机制、用户信息大多自我披露的在线匹配市场中，当手机号验证由强制改为可选且对他人可见时，验证能否成为个体用户的可靠信号？谁会选择验证、为何男女选择模式不同，验证又如何影响验证者本人、潜在伴侣及平台整体匹配结果，付费与免费验证是否有不同效果？

- 制品与设计：与平台合作把手机号验证设计为一次性可选邀请，随机分入控制组、付费验证组（T1，50虚拟币≈2美元）和免费验证组（T2），验证成功后用户资料页及搜索页显示“phone verified”徽章；另用DenseNet-121深度学习模型从照片估计美貌评分。

- 客观结果：T1整体验证率8%，T2 10%；男性验证率随类型单调上升（H型最高），女性呈倒U型（M型最高）；验证使验证者收到更多且更高人气用户的消息，验证者自己也更主动联系更多/更高质量对象；H型男性和M型女性获益最大；平台匹配数量增加；免费验证效果弱于付费验证但覆盖更广。

- 核心贡献：证明在缺乏声誉机制和可信信号的匹配市场中，可选电话验证可作为个体信号；首次在同一平台两侧观察到同一信号被策略性差异化使用——男性高类型倾向验证，女性中类型倾向验证——其机制是现有主导信号（男性收入/女性美貌）的可信度不同；同时把信号研究从接收者反应扩展到发送者自身行为，并提出付费/免费验证的覆盖—强度权衡。

- 整篇论证链：作者从在线匹配平台缺乏评论/评分、信息以自我披露为主的信息不对称出发，指出把强制验证改为可选并对他人可见后，验证可能承担信号功能。他们与某美国交友平台合作，随机将2万余名用户分入对照、付费验证和免费验证三组，并用深度学习估计女性美貌。理论预测高类型用户更可能发信号；但当已有主导信号足够可信时，高类型可能不再信号化。实证发现男性验证率单调上升，女性则M型最高，且差异与收入/美貌作为主导信号的相对可信度一致。随后用ITT/TOT框架估计验证对接收消息、主动发消息和最终匹配的作用，发现验证者从更多高质量对象处收到联系，自己也更主动；收益集中在H型男性和M型女性；平台匹配改善。最后通过操纵检验、同质性排除、隐私/领英调查、LATE和多种稳健性检验支持信号机制而非替代解释，并在讨论中把结论上升为对双边市场信号理论、发送者行为及平台设计的贡献。

## 类型与写作弧线判定

- 论文主类型判定：研究路径是选择真实在线交友平台，设计并执行随机对照现场实验，把可选手机验证作为干预；核心证据来自平台用户的实际验证选择、消息和匹配行为，而非计算benchmark或纯实验室实验。

- 主导写作弧线判定：文章从在线匹配中的信息不对称现象出发，引入信号理论解释“谁验证、为什么”；通过现场干预检验机制，并在讨论部分回到既有信号理论的非单调预测和发送者行为，因此属于现象—机制—现场干预—因果检验—回到理论。

## 研究开展程序

- study_or_phase_count：8

- 研究阶段总序列：阶段顺序为：先建立现场实验设计与随机化，再用深度学习构建关键测度，随后分析事前验证选择与机制，接着依次检验验证对潜在伴侣反应、验证者自身行为、平台匹配结果的影响，最后用稳健性与调查排除替代解释。前几个阶段为后几个阶段提供外生变异和关键变量；选择分析为后果分析提供可验证的事前异质性预测；稳健性检验保护核心机制主张。

### studies_or_phases

#### 1. 现场实验设计与随机化

- order：1

- name_cn：现场实验设计与随机化

- question_cn：如何对平台用户引入可选验证并形成可识别因果效应的对照？

- inputs_and_setting_cn：美国某大型交友平台，超过100万注册用户；随机选取2万余名在线用户；平台无并行实验。

- designed_or_compared_object_cn：可选手机验证邀请：T1付费验证（50虚拟币）、T2免费验证、对照组无验证邀请；成功后显示公开徽章。

- baseline_control_or_counterfactual_cn：对照组无验证选项；T2作为免费验证对照；T1与T2互相对照。

##### objective_metrics

1. 验证率 verify_1day/verify_1week

2. 协变量平衡p值

- analysis_method_cn：按性别分层随机；t检验/线性概率模型比较处理组与对照组；随机化平衡检验。

- main_result_cn：样本在三组间各协变量无显著差异；T1整体验证率约8%，T2约10%。

- argumentative_role_cn：提供外生变异，为后续ITT/TOT识别奠定基础。

- remaining_uncertainty_cn：尚未回答哪些类型用户验证、验证如何影响结果。

- link_to_next_phase_cn：引出对用户类型、美貌测量和验证决策的分析。

##### evidence_pointers

1. Section 3.2

2. Table 3

3. Table 4

#### 2. 美貌评分深度学习测量

- order：2

- name_cn：美貌评分深度学习测量

- question_cn：如何在不手动编码和隐私风险前提下度量女性美貌这一主导信号？

- inputs_and_setting_cn：公开SCUT-FBP5500数据集；用户主照片；人脸检测算法预处理。

- designed_or_compared_object_cn：DenseNet-121回归模型，修改末层输出1-5分，用于预测女性美貌；另训练男性模型做验证性辅助。

- baseline_control_or_counterfactual_cn：与人工编码、替代模型对比；五折交叉验证与Liang等报告水平比较。

##### objective_metrics

1. MAE

2. MSE

3. 五折交叉验证表现

4. 无人脸/多人脸照片剔除比例

- analysis_method_cn：监督深度学习训练、交叉验证、人脸裁剪；用t检验比较主照片评分与多图平均评分。

- main_result_cn：平均MAE=0.24，MSE=0.10，接近原文水平；约2%照片因无人脸/多人脸被剔除。

- argumentative_role_cn：为女性美貌提供可扩展一致度量，是检验“美貌是更可信主导信号”的关键变量。

- remaining_uncertainty_cn：美貌评分来自主照片，且是模型预测而非真实伴侣感知。

- link_to_next_phase_cn：该变量进入5.1.2的机制检验和类型分割相关稳健性。

##### evidence_pointers

1. Section 4.2

2. Table 2

#### 3. 验证选择：整体与类型异质性

- order：3

- name_cn：验证选择：整体与类型异质性

- question_cn：给定可选验证，谁选择验证？不同付费/免费和性别/类型如何差异？

- inputs_and_setting_cn：处理组男女用户约1.5万；平台popularity快照；T1/T2/对照。

- designed_or_compared_object_cn：三种实验分组；按平台popularity均值±1标准差将男、女分别分割为L/M/H类型。

- baseline_control_or_counterfactual_cn：对照组无验证选项；L型为参照；T2对照T1。

##### objective_metrics

1. verify_1day

2. verify_1week

- analysis_method_cn：分别对男、女估计线性概率模型/等价t检验；按类型估计验证率。

- main_result_cn：男性验证率随类型单调上升，H型最高；女性M型验证率最高，H型显著低于M型；付费降低总验证率。

- argumentative_role_cn：确立核心经验现象：同一信号被两侧用户不同使用，是需要机制解释的起点。

- remaining_uncertainty_cn：为什么M型女性最高、H型男性最高尚未解释。

- link_to_next_phase_cn：直接进入5.1.2用主导信号可信度解释差异。

##### evidence_pointers

1. Section 5.1.1

2. Table 4

3. Table 5

4. Figure 3

#### 4. 机制：现有主导信号的可信度与验证选择

- order：4

- name_cn：机制：现有主导信号的可信度与验证选择

- question_cn：是什么导致男女性分别呈单调与倒U型验证选择？

- inputs_and_setting_cn：平台快照：美貌评分、收入、popularity、second_signal；男女类型分割；在线附录稳健性。

- designed_or_compared_object_cn：验证选择作为因变量；主导属性高/中组作为自变量；比较女性美貌H-M需求差与男性收入H-M需求差。

- baseline_control_or_counterfactual_cn：L型为参照；attribute_Medium为基准；控制second_signal。

##### objective_metrics

1. 验证率

2. popularity

3. attribute_High×female交互系数

- analysis_method_cn：相关性分析验证性别偏好；OLS/线性概率回归；在线附录用连续测量和中介做稳健性。

- main_result_cn：女性美貌与popularity相关度最高、男性收入与popularity相关度最高；女性美貌H-M需求差显著大于男性收入H-M需求差；beauty_High女性验证率低于M型，income_High男性验证率高于M型。

- argumentative_role_cn：把初始模式归因于信号可信度机制，防止“只是性别需求差异”的替代解释。

- remaining_uncertainty_cn：尚未知道验证后是否产生对应收益及对发送者/平台影响。

- link_to_next_phase_cn：由选择转入后果分析，检验事前选择是否与事后收益一致。

##### evidence_pointers

1. Section 5.1.2

2. Table 6

3. Table 7

4. Table 8

5. Table A2

6. Section 6.4

#### 5. 验证对潜在伴侣反应的影响

- order：5

- name_cn：验证对潜在伴侣反应的影响

- question_cn：验证是否改变潜在伴侣对验证者的反应？

- inputs_and_setting_cn：实验后一周消息记录；控制/处理组；用户类型；消息发起者popularity。

- designed_or_compared_object_cn：验证状态作为TOT对象；T1/T2作为随机干预。

- baseline_control_or_counterfactual_cn：对照组无验证；L型×处理为参照；T2对照T1。

##### objective_metrics

1. msg_received_1week

2. sender_popularity

- analysis_method_cn：ITT→TOT两阶段回归；按性别和H/M/L类型分解；Wald检验。

- main_result_cn：验证显著增加收到消息数量和发送者平均popularity；H型男性和M型女性获益最大；H型女性未受损。

- argumentative_role_cn：验证事前选择与事后收益一致性，强化信号有效性。

- remaining_uncertainty_cn：尚未回答验证者自身是否改变行为。

- link_to_next_phase_cn：转入验证者自身主动性分析。

##### evidence_pointers

1. Section 5.2.1

2. Table 9

3. Table 10

4. Table A3

#### 6. 验证对验证者自身行为的影响

- order：6

- name_cn：验证对验证者自身行为的影响

- question_cn：验证是否影响验证者自己的发消息行为？

- inputs_and_setting_cn：post-intervention msg_sent、receiver_popularity；用户类型；控制/处理组。

- designed_or_compared_object_cn：验证状态（实际验证者）；比较验证前后主动联系数量和质量。

- baseline_control_or_counterfactual_cn：未验证/对照组；L型×处理为参照。

##### objective_metrics

1. msg_sent_1week

2. receiver_popularity

- analysis_method_cn：两阶段回归；按类型分解；Wald检验。

- main_result_cn：验证者发送更多消息且联系更高popularity用户；H型男性、M型女性变化最大；女性主动性的提升对平台尤其重要。

- argumentative_role_cn：发现信号发送者的自身行为变化，扩展信号理论从接收者到发送者。

- remaining_uncertainty_cn：尚未直接转化为最终匹配和平台整体结果。

- link_to_next_phase_cn：进入平台级匹配分析。

##### evidence_pointers

1. Section 5.2.2

2. Table 11

3. Table 12

#### 7. 平台匹配结果与付费/免费比较

- order：7

- name_cn：平台匹配结果与付费/免费比较

- question_cn：可选验证是否改善平台两侧匹配，付费与免费设计有何差异？

- inputs_and_setting_cn：match_sent/match_received一周内；T1/T2/control；用户类型。

- designed_or_compared_object_cn：验证状态；付费验证与免费验证两种设计比较。

- baseline_control_or_counterfactual_cn：对照组；T1/T2互相对比。

##### objective_metrics

1. match_sent_1week

2. match_received_1week

- analysis_method_cn：两阶段回归；类型分解；Wald检验。

- main_result_cn：验证者匹配数量显著增加，H型男性和M型女性受益最大；免费验证同样有效但作用较弱；免费验证覆盖更高，付费验证带来更多主动性。

- argumentative_role_cn：把个体层面效应提升为平台层面设计知识，为实务提供成本—覆盖权衡。

- remaining_uncertainty_cn：仍未排除同质性、干扰、控制组泄气等替代解释。

- link_to_next_phase_cn：由主结果进入稳健性和机制检验。

##### evidence_pointers

1. Section 5.3.1

2. Section 5.3.2

3. Table 13

4. Table 14

#### 8. 稳健性、机制调查与替代解释排除

- order：8

- name_cn：稳健性、机制调查与替代解释排除

- question_cn：信号机制是否稳健？能否排除同质性、干扰、控制组泄气、测量问题？

- inputs_and_setting_cn：MTurk操纵检验；平台内调查（隐私原因、LinkedIn验证）；在线附录表A5–A19；社会网络连接度；备选模型。

- designed_or_compared_object_cn：再检验同质性比率、社会连接交互、LATE、负二项、连续度量/替代分割、中介。

- baseline_control_or_counterfactual_cn：控制组与处理组、验证者与未验证者、不同处理暴露水平。

##### objective_metrics

1. ratio_msg_received

2. LinkedIn_verified

3. msg_sent_pre_1week

4. p值

5. LATE估计

6. 负二项系数

- analysis_method_cn：调查描述统计、回归、LATE/IV、负二项、子样本、中介、随机化子组检验。

- main_result_cn：用户把邀请理解为差异化机会（91%/86%）；验证者更多分享自我信息（多27%），不愿验证者63%因隐私；手机验证者更可能验证LinkedIn；同质性、干扰、控制组泄气等替代解释不成立；LATE/负二项/替代分割均一致。

- argumentative_role_cn：把核心结果从一次性现场结果提升为机制稳健的知识，保护贡献。

- remaining_uncertainty_cn：仍不能直接观察接收者的认知加工；长期学习效果未考察；跨平台泛化只能推断。

- link_to_next_phase_cn：进入讨论，回扣理论并给出边界条件。

##### evidence_pointers

1. Section 6.1–6.4

2. Table 15

3. Table A5–A19

## 各部分修辞架构

### abstract_moves

1. 背景：在线匹配平台缺少评分/评论等机制，信息不对称严重（摘要首句）

2. 现象/目标：可选且可见的认证可能成为信号；与主打交友平台合作开展随机现场实验（摘要第2句）

3. 结果：男女使用相同信号方式不同，男性高类型验证、女性中类型验证最多（摘要第3-4句）

4. 机制：差异与现有主导信号（男性收入/女性美貌）可信度有关（摘要第5句）

5. 结果与贡献：验证者收到更多高质量联系、变得更主动、平台匹配改善；对研究与实务有启示（摘要末）

### introduction_moves

1. 从平台激增和信息不对称背景进入（P1 S1）

2. 指出约会同性缺乏验证信息使问题更严重（P1 S2）

3. 提出本研究关注可选、可见验证作为信号（P1 S4）

4. 对比强制验证与可选验证，制造缺口（P2 S1–S2）

5. 说明以往研究只重事后有效性，本文另看事前选择（P3 S1）

6. 提出性别差异与付费/免费问题，列出具体研究问题（P3 S2–S4）

7. 说明选择该平台的理由：理想环境、其他市场实验不可行（P4 S1–S3）

8. 预告随机实验三组设计（P5 S1）

9. 引入信号理论作指导（P6 S1）

10. 预告核心发现：男性单调、女性倒U、机制与后果（P6–P8）

11. 列举四项理论/实证贡献（P9）

12. 给出平台设计含义（P10）

### theory_and_knowledge_moves

1. 2.1确认性别偏好文献：男性重视外貌，女性重视收入；本文用数据验证这种关系

2. 2.1指出在线交友市场在匹配市场研究中相对被忽视

3. 2.2交代验证研究多在有声誉系统环境，本文移到无WOM环境

4. 2.2引入斯彭斯信号理论：高类型更可能发送昂贵信号

5. 2.2引入反信号/计分信号文献：已有信号可信时高类型可能不发送信号

6. 2.2强调新信号采用取决于相对现有信号的附加价值；此前多理论/实验，本文是双边市场现场证据

7. 2.2将信号研究从接收者扩展至发送者行为变化

8. 2.2引入深度学习美貌预测作为测量工具

### artifact_design_moves

1. 3.2随机选取用户并分三组：控制、T1付费、T2免费

2. 3.2发送一次性在线邀请，最大化阅读概率

3. 3.2按性别分层随机，保证男女比例

4. 3.2邀请文案强调减少诈骗、让人知道你是真实的；付费50虚拟币、免费验证；承诺不泄露

5. 3.2验证成功后显示徽章；一个手机号只验证一个账号；确保无并行实验

6. 4.2用公开数据集训练DenseNet-121，避免用户隐私泄露；人脸检测裁剪

### evaluation_moves

1. 5.0随机化平衡检查（Table 3）

2. 5.1.1用线性概率模型获得验证选择因果效应

3. 5.2采用ITT到TOT的识别策略，辅以LATE

4. 5.2按用户类型分解效应，检验事前预测

5. 6.1 MTurk操纵检验验证邀请被理解为差异化机会

6. 6.2用ratio_msg_received排除同质性；用隐私调查与LinkedIn验证检验机制

7. 6.3检验社会干扰、LATE、负二项模型

8. 6.4检查控制组泄气、同时性、类型分割、连续度量、中介与子组随机化

### discussion_and_contribution_moves

1. 7.1把结果重新连接到“缺少声誉机制”的起点

2. 7.1用同一信号被两方不同使用来定义核心发现

3. 7.1把差异归因于现有主导信号的可信度

4. 7.1说明验证信号传递愿意分享PII的垂直维度

5. 7.1报告发送者主动性变化并声明扩展信号理论

6. 7.1提炼付费/免费覆盖—强度权衡

7. 7.2明确三项理论贡献：双边市场信号、非单调选择、发送者行为

8. 7.3给平台设计者提出可操作的边界条件与设计原则

9. 7.4交代学习效应、多信号交互、跨平台泛化等限制

## 理论/知识到设计的翻译

### 知识/理论基础

1. 信号传递理论（Spence 1978; Riley 2001）

2. 反信号/计分信号理论（Feltovich et al. 2002; Luca and Smith 2015）

3. 婚姻与约会市场中的性别偏好研究（Buss 1989; Fisman et al. 2006; Hitsch et al. 2010）

4. 信息可信度与视觉信息判断（Metzger 2007; Metzger and Flanagin 2013）

5. 隐私与个人可识别信息（PII）披露意愿（Gibbs et al. 2006; Greene et al. 2006; Jiang et al. 2013）

6. 深度学习用于图像美貌预测（Liang et al. 2018; Malik et al. 2019）

- 理论—设计耦合：partial

- 耦合判定理由：信号理论前瞻性地决定了关键研究变量、对比对象和预测方向：验证被设计为可选、可见且有成本差异，高类型/中类型的采用预测来自信号理论；但具体制品选择（手机号验证、徽章展示、一次性邀请、付费免费设计）主要来自平台实践与简单可操作性，并非从形式模型或设计原则严格推导；理论用于指导实证检验和事后解释，而非作为制品构建原则。

- 理论到设计翻译链：信号理论提出：在信息不对称下，有成本的可见信号能区分不同类型；高类型更倾向发信号，但当已有信号足够可信时高类型可能不再发新信号。作者据此把常用强制验证改为可选且可见，并设计付费与免费两种成本差异；同时依据性别偏好文献把收入识别为男性主导信号、把美貌识别为女性主导信号；又依据可验证性论证美貌比收入更可信；然后用深度学习测量美貌，把理论变量转成可估计的实证变量；最后用随机实验和调查检验从采用决策到接收者反应、发送者主动性和平台匹配的完整链条。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：高成本信号可区分高类型与低类型；高类型更可能发送昂贵信号。

- mechanism_cn：验证需要付费或暴露手机号，因此只有对自身质量有信心且愿意承担成本的用户才验证。

- design_requirement_cn：验证必须是可选的、有成本的、对他人可见的。

- artifact_choice_cn：一次性可选手机验证邀请；成功后显示“phone verified”徽章；T1收取50虚拟币，T2免费对照。

- evaluated_contrast_cn：T1 vs T2 vs 对照组；H/M/L型用户验证率比较。

- objective_result_cn：T1验证率8%，T2 10%；男性验证率单调上升，H型最高。

##### evidence_pointers

1. Section 3.2

2. Table 4

3. Table 5

#### 2. 2

- theory_or_knowledge_claim_cn：当已有信号足够可信且有效时，高类型可能不再发送新信号（计分信号）。

- mechanism_cn：已有主导信号已经能把H型与M/L型区分开，新信号的边际价值下降；M型反而更有动机验证。

- design_requirement_cn：需要识别每侧用户已有主导信号，并比较其可信度差异。

- artifact_choice_cn：按平台popularity将男女分别分为L/M/H；用收入/美貌作为主导属性变量；控制second_signal。

- evaluated_contrast_cn：beauty_High vs beauty_Medium女性验证率；income_High vs income_Medium男性验证率；女性美貌H-M需求差 vs 男性收入H-M需求差。

- objective_result_cn：女性M型验证率最高，H型显著更低；男性H型验证率最高；美貌需求差显著大于收入需求差。

##### evidence_pointers

1. Section 5.1.2

2. Table 6

3. Table 7

4. Table 8

#### 3. 3

- theory_or_knowledge_claim_cn：男性更看重外貌，女性更看重收入；这决定谁是各自的主导信号。

- mechanism_cn：popularity主要由美貌/收入驱动，导致两侧需求分布和信号替代空间不同。

- design_requirement_cn：按性别分别建模和分割；把收入/美貌作为关键协变量。

- artifact_choice_cn：分别估计男女模型；用美貌评分、收入分段、popularity作为变量。

- evaluated_contrast_cn：属性与popularity的相关性；男女性验证选择模式差异。

- objective_result_cn：美貌与女性popularity相关度最高，收入与男性popularity相关度最高。

##### evidence_pointers

1. Section 5.1.2

2. Table A2

#### 4. 4

- theory_or_knowledge_claim_cn：视觉信息比自我报告数值更容易验证，因此更可信。

- mechanism_cn：照片中的美貌可被对方直接核验，收入只是自选范围值，所以美貌作为信号的噪声更低。

- design_requirement_cn：需要可扩展、一致的美貌度量来检验其可信度优势。

- artifact_choice_cn：使用DenseNet-121深度学习模型从用户照片预测美貌分，并训练男性模型做辅助验证。

- evaluated_contrast_cn：女性beauty H-M需求差 vs 男性income H-M需求差。

- objective_result_cn：beauty_high−beauty_medium 需求差显著大于 income_high−income_medium 需求差。

##### evidence_pointers

1. Section 4.2

2. Table 6

#### 5. 5

- theory_or_knowledge_claim_cn：愿意分享个人可识别信息有助于建立亲密与信任，但在线用户通常不愿透露手机号等PII。

- mechanism_cn：可选验证让愿意分享PII的用户以较低披露风险传递可信度信号。

- design_requirement_cn：验证必须不公开手机号本身，只展示已认证状态；同时需要测度分享意愿。

- artifact_choice_cn：验证只显示徽章、不公开号码；用自我简介完整度、隐私原因调查、LinkedIn验证调查度量分享意愿。

- evaluated_contrast_cn：验证者 vs 非验证者的自我信息披露；手机验证者 vs 非手机验证者是否更愿验证LinkedIn。

- objective_result_cn：验证者平均多分享27%自我信息；63%不验证者因隐私；手机验证者更可能验证LinkedIn。

##### evidence_pointers

1. Section 6.2

2. Table 15

#### 6. 6

- theory_or_knowledge_claim_cn：获得信号后，发送者可能根据新信号调整自身行为（如教育信号后寻求更好工作）。

- mechanism_cn：验证赋予用户可信度，使其更主动、更挑剔地联系高质量对象。

- design_requirement_cn：结果分析需同时观察验证者的主动发信行为，而非只观察接收者反应。

- artifact_choice_cn：测量msg_sent、receiver_popularity、match_sent，并按类型分解。

- evaluated_contrast_cn：验证者 vs 未验证者的主动发信数量与对象质量。

- objective_result_cn：验证者发送更多消息且联系更高popularity对象；H型男性与M型女性提升最大。

##### evidence_pointers

1. Section 5.2.2

2. Table 11

3. Table 12

## 评价逻辑

### evaluation_modes

1. 随机化现场实验：控制组、付费验证T1、免费验证T2

2. 按性别分层随机与随机化平衡检验

3. ITT到TOT识别策略，辅以LATE/IV

4. 按用户类型H/M/L分解的异质性分析

5. 操纵检验：MTurk调查验证邀请被理解为差异化机会

6. 机制调查：平台内隐私原因调查与LinkedIn验证调查

7. 替代解释排除：同质性比率、社会干扰、控制组泄气、同时性

8. 备选模型与测量稳健性：负二项、连续度量、替代分割、中介、子组随机化

9. 深度学习模型交叉验证

- why_these_evaluations_cn：由于研究问题同时覆盖事前采用、事后接收者反应、发送者自身行为与平台匹配，单一回归不足以支撑；随机实验提供因果识别，TOT/LATE处理“只有部分人实际验证”的问题，类型分解用于连接事前预测与事后收益，调查与替代机制检验用于确认信号机制而非同质性或隐私混淆，最终稳健性检验保护贡献不依赖于具体分割或模型设定。

- benchmark_and_contrast_chain_cn：先以“无验证机会的对照组”为基准，对比付费和免费验证的总验证率；随后在验证组内部按L/M/H类型对比采用模式；再用收入/美貌的需求差作为“现有信号可信度”的量化对比；后果阶段仍以对照组为反事实，并通过T1/T2之间的Wald检验对比付费/免费；最后用LATE、负二项、不同类型分割和连续测量等作为替代基准，确认主结果方向不变。

### claim_evidence_ledger

#### 1. 付费验证总验证率约8%，免费验证约10%，成本抑制验证。

- claim_cn：付费验证总验证率约8%，免费验证约10%，成本抑制验证。

- evidence_cn：Table 4 t检验。

- status_cn：supported

#### 2. 男性验证率随类型单调上升，女性M型最高。

- claim_cn：男性验证率随类型单调上升，女性M型最高。

- evidence_cn：Table 5，Figure 3。

- status_cn：supported

#### 3. 验证选择由现有主导信号可信度驱动。

- claim_cn：验证选择由现有主导信号可信度驱动。

- evidence_cn：Table 6–8，Table A2，A17，A18。

- status_cn：supported_with_measured_proxies

#### 4. 验证使验证者收到更多更高质量消息。

- claim_cn：验证使验证者收到更多更高质量消息。

- evidence_cn：Table 9–10。

- status_cn：supported

#### 5. 验证使验证者更主动并联系更高类型对象。

- claim_cn：验证使验证者更主动并联系更高类型对象。

- evidence_cn：Table 11–12。

- status_cn：supported

#### 6. 平台匹配结果改善，H型男性和M型女性受益最大。

- claim_cn：平台匹配结果改善，H型男性和M型女性受益最大。

- evidence_cn：Table 13–14。

- status_cn：supported

#### 7. 免费验证覆盖更高，付费验证主动性更强。

- claim_cn：免费验证覆盖更高，付费验证主动性更强。

- evidence_cn：Table 4与Table 11中Wald检验。

- status_cn：supported

#### 8. 手机验证信号代表愿意分享个人可识别信息。

- claim_cn：手机验证信号代表愿意分享个人可识别信息。

- evidence_cn：自我简介多27%分享、63%隐私调查、LinkedIn验证相关（Table 15）。

- status_cn：indirect_supportive

#### 9. 效果由信号而非同质性驱动。

- claim_cn：效果由信号而非同质性驱动。

- evidence_cn：Table A6中的ratio_msg_received。

- status_cn：supported

#### 10. LATE/负二项/替代分割等稳健性下结论一致。

- claim_cn：LATE/负二项/替代分割等稳健性下结论一致。

- evidence_cn：Tables A9–A19。

- status_cn：supported

- internal_validity_strategy_cn：随机分配控制组与处理组；按性别分层；一次性邀请保证处理到达；对照组无验证可能，避免always-takers；ITT到TOT并用LATE；测试社会连接干扰；比较控制组实验前后发信以排除泄气；用unverified子样本排除同时性；主结果通过多种模型和分割方式保持一致。

- external_validity_strategy_cn：选择美国领先交友平台，平台用户规模大且无声誉机制；在正文与讨论中把结论限定于类似缺乏声誉机制、自我披露占主导的匹配市场；还指出平台早期增长阶段最适合可选验证；对平台类型和验证机制类型的推广给出边界。

- what_is_not_actually_tested_cn：接收者是否真的有意识地解读徽章并作为信号，未被直接观察；实际长期匹配、线下约会或婚姻结果未测；多个新信号同时存在时的交互未测；跨平台（招聘、早期电商等）外推只是分析性主张，不是实证；平台整体福利/帕累托改善并未用总福利指标严格检验；付费验证与免费验证效果差异可能受不同选择进入验证组的人群特征影响。

## 贡献闭环

- technical_claim_cn：使用DenseNet-121在公开美貌数据集上训练，能在本研究用户照片上达到平均MAE=0.24、MSE=0.10的预测精度，可用于大规模美貌测量。

- artifact_claim_cn：在无声誉机制的匹配平台中，把手机验证从强制改为可选且公开显示，可成为个体用户的差异化信号；付费与免费版本均有效，但付费带来更主动的验证者，免费带来更高覆盖率。

- mechanism_claim_cn：同一验证信号被两侧用户不同使用，是因为两侧现有主导信号（女性美貌 vs 男性收入）的可信度不同；验证信号还传递愿意分享个人可识别信息的意愿，并触发验证者自身更主动的联系行为。

- boundary_claim_cn：该效应主要出现在缺乏声誉机制、资料大多自我披露、用户对隐私敏感且已有主导信号可信度存在差异的匹配平台；尤其适用于平台早期或尚未强制验证的阶段；不同主导信号可信度会导致新信号帮助H型还是M型用户。

- reusable_design_knowledge_cn：设计可选验证类信息机制时，应识别每侧用户已有主导信号的可信度；若已有信号弱，新信号会帮助高类型用户脱颖而出；若已有信号强，新信号可能主要帮助中类型用户。付费与免费设计存在覆盖—强度权衡，平台可按阶段选择。

- theoretical_contribution_cn：把信号理论扩展到双边匹配市场，显示同一信号在平台两侧可产生非单调/性别差异化的采用模式；为反信号或计分信号的现场证据提供支持；并首次把信号研究从“接收者如何反应”扩展到“发送者如何因获得信号而改变自身行为”。

- how_discussion_closes_intro_gap_cn：讨论部分直接回到引言提出的“缺少评分/评论、信息自我披露、强制验证会压抑信号”等问题，重述可选验证可在无替代机制的市场中成为可信信号；随后用同一信号两侧不同使用、主导信号可信度、发送者主动性、平台匹配改善等结果回填引言中的研究问题与贡献声明。

- overclaim_or_unsupported_leaps_cn：把“更多消息/匹配”直接表述为“更好的匹配”和“平台受益”，但未测量长期匹配质量或用户福利；“验证者因信号变得主动”的因果链中，主动性也可能是验证行为本身带来的自我效能而非接收者反应；用调查和替代检验推断隐私机制，不能严格证明平台用户的真实认知过程；付费vs免费效果差异可能受不同compliers选择影响，文章依靠调查缓解但未完全排除。

## 句级写作动作图谱

### 1. Abstract P1 S1

- order：1

- section：Abstract

- locator：Abstract P1 S1

- move_code：CONTEXT

- paraphrase_cn：在线匹配平台缺少交易平台中常见的评分和评论机制，信息不对称问题突出。

- rhetorical_function_cn：开篇建立研究所在的市场类型和基本问题。

- depends_on_cn：无。

- sets_up_cn：为提出“验证可能承担信号功能”提供背景。

- evidence_pointer：Abstract

### 2. Introduction P1 S2

- order：2

- section：Introduction

- locator：Introduction P1 S2

- move_code：PRACTICAL_STAKES

- paraphrase_cn：在线约会参与者缺乏可验证信息，使信息不对称进一步恶化。

- rhetorical_function_cn：强调该问题在约会平台尤其严重。

- depends_on_cn：前一句关于匹配平台信息不对称的背景。

- sets_up_cn：为聚焦手机验证提供现实紧迫性。

- evidence_pointer：Introduction P1 S2

### 3. Introduction P1 S4

- order：3

- section：Introduction

- locator：Introduction P1 S4

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：本研究关注电话验证在可选且可见时作为可信信号的新角色。

- rhetorical_function_cn：直接宣告研究对象与角度。

- depends_on_cn：前面对信息不对称和缺乏验证信息的描述。

- sets_up_cn：为整篇论文划定核心问题。

- evidence_pointer：Introduction P1 S4

### 4. Introduction P2 S1

- order：4

- section：Introduction

- locator：Introduction P2 S1

- move_code：GAP

- paraphrase_cn：强制验证提升平台安全性，但可能抑制用户可选验证所能传达的有用信息。

- rhetorical_function_cn：制造强制与可选之间的概念缺口。

- depends_on_cn：对验证的基本功能已有理解。

- sets_up_cn：论证可选验证是未被研究的替代角色。

- evidence_pointer：Introduction P2 S1

### 5. Introduction P2 S2

- order：5

- section：Introduction

- locator：Introduction P2 S2

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：在缺少声誉机制和交易保障、依赖自我披露的市场中，简单的可选验证可能额外承担信号意义。

- rhetorical_function_cn：说明该缺口的理论价值和应用价值。

- depends_on_cn：前一句对强制验证限制的描述。

- sets_up_cn：为选择约会平台作理由。

- evidence_pointer：Introduction P2 S2

### 6. Introduction P3 S1

- order：6

- section：Introduction

- locator：Introduction P3 S1

- move_code：LIMITATION

- paraphrase_cn：以往信息机制研究多关注事后有效性，而本文还考察用户事前是否选择验证。

- rhetorical_function_cn：点出已有文献的盲点。

- depends_on_cn：前面关于验证信号角色的设定。

- sets_up_cn：为随后列出的研究问题提供定位。

- evidence_pointer：Introduction P3 S1

### 7. Introduction P3 S2

- order：7

- section：Introduction

- locator：Introduction P3 S2

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：由于在线约会中的性别差异，男女很可能在采用同一信号时方式不同。

- rhetorical_function_cn：引入性别异质性的预期。

- depends_on_cn：性别差异文献的既有知识。

- sets_up_cn：为分性别分析作铺垫。

- evidence_pointer：Introduction P3 S2

### 8. Introduction P3 S3

- order：8

- section：Introduction

- locator：Introduction P3 S3

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：研究关注付费验证与免费验证的比较。

- rhetorical_function_cn：增加一个实务层面的研究维度。

- depends_on_cn：验证对用户有潜在收益的假设。

- sets_up_cn：为T1/T2两种处理设计提供依据。

- evidence_pointer：Introduction P3 S3

### 9. Introduction P3 S4

- order：9

- section：Introduction

- locator：Introduction P3 S4

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：列出具体问题：谁验证、两侧如何不同、机制是什么、验证如何影响潜在伴侣、验证者本人和平台匹配。

- rhetorical_function_cn：将研究问题显式化，形成全文结构地图。

- depends_on_cn：前面的缺口与性别差异讨论。

- sets_up_cn：对应后文5.1、5.2、5.3各节。

- evidence_pointer：Introduction P3 S4

### 10. Introduction P4 S1

- order：10

- section：Introduction

- locator：Introduction P4 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者与美国一家领先交友平台合作。

- rhetorical_function_cn：引入实证来源。

- depends_on_cn：研究问题需真实平台数据。

- sets_up_cn：为随机现场实验出现作铺垫。

- evidence_pointer：Introduction P4 S1

### 11. Introduction P4 S2

- order：11

- section：Introduction

- locator：Introduction P4 S2

- move_code：PRACTICAL_STAKES

- paraphrase_cn：在线交友已成为主流且市场价值巨大。

- rhetorical_function_cn：说明研究该平台具有现实重要性。

- depends_on_cn：无。

- sets_up_cn：为外部有效性和实践意义提供基础。

- evidence_pointer：Introduction P4 S2

### 12. Introduction P4 S3

- order：12

- section：Introduction

- locator：Introduction P4 S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：该平台没有其他可信机制、信息全部自我报告，是理想研究环境；其他匹配市场做随机实验不可行。

- rhetorical_function_cn：论证案例选择的适宜性。

- depends_on_cn：平台特征描述。

- sets_up_cn：为随机实验的可推广性设定条件。

- evidence_pointer：Introduction P4 S3

### 13. Introduction P5 S1

- order：13

- section：Introduction

- locator：Introduction P5 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：设计三组随机实验：控制组、付费验证组和免费验证组。

- rhetorical_function_cn：预告实验设计。

- depends_on_cn：研究问题需要因果识别。

- sets_up_cn：为数据与结果部分作结构准备。

- evidence_pointer：Introduction P5 S1

### 14. Introduction P6 S1

- order：14

- section：Introduction

- locator：Introduction P6 S1

- move_code：THEORY_INTRO

- paraphrase_cn：作者用信号相关理论指导事前采用与事后影响分析。

- rhetorical_function_cn：声明理论角色。

- depends_on_cn：可选验证作为信号的研究定位。

- sets_up_cn：引出后续信号理论的应用。

- evidence_pointer：Introduction P6 S1

### 15. Introduction P6 S2

- order：15

- section：Introduction

- locator：Introduction P6 S2

- move_code：RESULT

- paraphrase_cn：T1只有8%用户选择付费验证，T2约10%选择免费验证；作者按类型将用户分层。

- rhetorical_function_cn：报告总体验证率并预告类型分析。

- depends_on_cn：随机实验数据。

- sets_up_cn：为类型异质性结果做引子。

- evidence_pointer：Introduction P6 S2

### 16. Introduction P6 S3

- order：16

- section：Introduction

- locator：Introduction P6 S3

- move_code：RESULT

- paraphrase_cn：男性越高类型越可能验证，符合传统信号预测；女性M型最可能验证。

- rhetorical_function_cn：给出最核心的实证反差。

- depends_on_cn：类型分割和验证率估计。

- sets_up_cn：为后续机制解释提供谜题。

- evidence_pointer：Introduction P6 S3

### 17. Introduction P7 S1

- order：17

- section：Introduction

- locator：Introduction P7 S1

- move_code：MECHANISM

- paraphrase_cn：验证选择与现有主导信号的可信度有关：女性是美貌，男性是收入。

- rhetorical_function_cn：提出解释差异的机制。

- depends_on_cn：前面的性别差异模式。

- sets_up_cn：为收入/美貌的实证分析提供假设。

- evidence_pointer：Introduction P7 S1

### 18. Introduction P7 S2

- order：18

- section：Introduction

- locator：Introduction P7 S2

- move_code：MECHANISM

- paraphrase_cn：高美貌女性更少验证，中等美貌女性更多验证；高收入男性更多验证。

- rhetorical_function_cn：把机制转成具体结果预告。

- depends_on_cn：深度学习美貌评分和收入数据。

- sets_up_cn：为Table 7和Table 8作准备。

- evidence_pointer：Introduction P7 S2

### 19. Introduction P7 S3

- order：19

- section：Introduction

- locator：Introduction P7 S3

- move_code：MECHANISM

- paraphrase_cn：验证传递愿意分享个人可识别信息的信号，调查提供支持证据。

- rhetorical_function_cn：引入信号的语义内容。

- depends_on_cn：隐私与自我披露文献。

- sets_up_cn：为6.2隐私机制调查伏笔。

- evidence_pointer：Introduction P7 S3

### 20. Introduction P8 S1

- order：20

- section：Introduction

- locator：Introduction P8 S1

- move_code：RESULT

- paraphrase_cn：验证者收到更多来自更高类型用户的联系，最可能验证的群体获益最大。

- rhetorical_function_cn：报告接收者反应层面的结果。

- depends_on_cn：事后消息数据。

- sets_up_cn：为发送者行为分析过渡。

- evidence_pointer：Introduction P8 S1

### 21. Introduction P8 S2

- order：21

- section：Introduction

- locator：Introduction P8 S2

- move_code：RESULT

- paraphrase_cn：验证者变得更主动，平台匹配改善。

- rhetorical_function_cn：把效应从个体扩展到平台。

- depends_on_cn：消息与匹配结果。

- sets_up_cn：为平台层面贡献作铺垫。

- evidence_pointer：Introduction P8 S2

### 22. Introduction P8 S3

- order：22

- section：Introduction

- locator：Introduction P8 S3

- move_code：RESULT

- paraphrase_cn：免费验证效果类似但较弱，显示覆盖与主动性的权衡。

- rhetorical_function_cn：预告付费/免费比较结论。

- depends_on_cn：T1/T2对比。

- sets_up_cn：为5.3.2和实务建议提供依据。

- evidence_pointer：Introduction P8 S3

### 23. Introduction P9 S1

- order：23

- section：Introduction

- locator：Introduction P9 S1

- move_code：CONTRIBUTION

- paraphrase_cn：贡献之一：在缺乏替代机制的市场中，可选验证可成为个体信号。

- rhetorical_function_cn：开始列举贡献。

- depends_on_cn：全部实证发现。

- sets_up_cn：为后续理论贡献段作铺垫。

- evidence_pointer：Introduction P9 S1

### 24. Introduction P9 S2

- order：24

- section：Introduction

- locator：Introduction P9 S2

- move_code：CONTRIBUTION

- paraphrase_cn：贡献之二：同时考察用户的采用决策及其影响。

- rhetorical_function_cn：强调事前选择这一新视角。

- depends_on_cn：与过往仅看事后有效性对比。

- sets_up_cn：突出论文的双面分析。

- evidence_pointer：Introduction P9 S2

### 25. Introduction P9 S3

- order：25

- section：Introduction

- locator：Introduction P9 S3

- move_code：CONTRIBUTION

- paraphrase_cn：贡献之三：研究平台两侧采用同一信号的不同选择与影响。

- rhetorical_function_cn：点出双边异质性贡献。

- depends_on_cn：男女分别验证模式。

- sets_up_cn：为讨论中信号理论扩展作铺垫。

- evidence_pointer：Introduction P9 S3

### 26. Introduction P9 S4

- order：26

- section：Introduction

- locator：Introduction P9 S4

- move_code：CONTRIBUTION

- paraphrase_cn：贡献之四：用深度学习估计美貌并检验其影响。

- rhetorical_function_cn：交代方法层面贡献。

- depends_on_cn：深度学习模型。

- sets_up_cn：为该技术在其他IS研究中的应用提供示例。

- evidence_pointer：Introduction P9 S4

### 27. Introduction P10 S1

- order：27

- section：Introduction

- locator：Introduction P10 S1

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：给平台设计者的含义：早期平台可选验证能帮助验证者差异化，而不给所有用户增加成本。

- rhetorical_function_cn：把研究结果转成适用性主张。

- depends_on_cn：平台匹配改善结果。

- sets_up_cn：为讨论部分实践建议作铺垫。

- evidence_pointer：Introduction P10 S1

### 28. Section 2.1 P1

- order：28

- section：Related Work

- locator：Section 2.1 P1

- move_code：GAP

- paraphrase_cn：匹配市场研究多关注肾脏移植、医生匹配等机制的效率与稳定，在线交友研究相对不足。

- rhetorical_function_cn：指出文献空白。

- depends_on_cn：匹配市场文献。

- sets_up_cn：为本文研究场景定位。

- evidence_pointer：Section 2.1 P1

### 29. Section 2.1 P2

- order：29

- section：Related Work

- locator：Section 2.1 P2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：婚姻市场文献发现男性更重视女性外貌，女性更重视男性收入。

- rhetorical_function_cn：引入性别偏好知识。

- depends_on_cn：Buss、Fisman、Hitsch等研究。

- sets_up_cn：为后文识别收入/美貌为主导信号提供基础。

- evidence_pointer：Section 2.1 P2

### 30. Section 2.2 P1

- order：30

- section：Related Work

- locator：Section 2.2 P1

- move_code：GAP

- paraphrase_cn：验证研究多在有声誉系统的环境中，本文研究无WOM等替代信号的市场中的战略角色。

- rhetorical_function_cn：把验证文献拉入新情境。

- depends_on_cn：验证与声誉机制文献。

- sets_up_cn：为可选验证信号的主张腾出空间。

- evidence_pointer：Section 2.2 P1

### 31. Section 2.2 P2

- order：31

- section：Related Work

- locator：Section 2.2 P2

- move_code：THEORY_INTRO

- paraphrase_cn：信号理论指出信号者向接收者传递私有不可观察信息，多个信号可在多个维度上帮助区分；信号可信度影响效果。

- rhetorical_function_cn：系统引入信号理论。

- depends_on_cn：Spence、Connelly等经典文献。

- sets_up_cn：为验证作为信号提供理论语言。

- evidence_pointer：Section 2.2 P2

### 32. Section 2.2 P3

- order：32

- section：Related Work

- locator：Section 2.2 P3

- move_code：THEORY_PROPOSITION

- paraphrase_cn：传统信号模型认为高类型更可能发送昂贵信号；但新兴研究显示高类型在已有可信信号时可能不发送信号。

- rhetorical_function_cn：建立两个可竞争的预测。

- depends_on_cn：Feltovich等反信号文献。

- sets_up_cn：为女性M型最高、男性H型最高的差异提供理论基础。

- evidence_pointer：Section 2.2 P3

### 33. Section 2.2 P4

- order：33

- section：Related Work

- locator：Section 2.2 P4

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：新信号采用取决于相对现有信号的附加价值；既有非单调证据多来自理论或实验，而且信号往往只给一侧；本文研究同一信号同时在两侧可选。

- rhetorical_function_cn：解释为什么需要现场双边证据。

- depends_on_cn：反信号文献和现有实验局限。

- sets_up_cn：为全文的差异化贡献作铺垫。

- evidence_pointer：Section 2.2 P4

### 34. Section 2.2 P5

- order：34

- section：Related Work

- locator：Section 2.2 P5

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：自愿披露文献表明，企业在非强制情况下选择审计可发出积极信号；本文把类似逻辑用于个体的可选验证。

- rhetorical_function_cn：引入自愿机制的先例。

- depends_on_cn：Lennox和Pittman等。

- sets_up_cn：为可选验证的合理性提供类比。

- evidence_pointer：Section 2.2 P5

### 35. Section 2.2 P6

- order：35

- section：Related Work

- locator：Section 2.2 P6

- move_code：THEORY_PROPOSITION

- paraphrase_cn：信号文献多关注接收者反应，但发送者获得信号后也可能改变自身行为，如投资教育后会寻求更好工作。

- rhetorical_function_cn：提出发送者自身行为变化的理论可能。

- depends_on_cn：Lazear等的理性行为观点。

- sets_up_cn：为5.2.2主动发信分析提供理论依据。

- evidence_pointer：Section 2.2 P6

### 36. Section 2.2 P7

- order：36

- section：Related Work

- locator：Section 2.2 P7

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：采用深度学习构建美貌分数。

- rhetorical_function_cn：说明测量工具的技术来源。

- depends_on_cn：计算机视觉深度学习文献。

- sets_up_cn：为4.2节模型细节作铺垫。

- evidence_pointer：Section 2.2 P7

### 37. Section 3.1

- order：37

- section：Experiment

- locator：Section 3.1

- move_code：DESIGN_FEATURE

- paraphrase_cn：平台用户资料完全由用户自我披露，电话验证是本平台第一次出现公开可验证的信息。

- rhetorical_function_cn：描述实验环境的基线状态。

- depends_on_cn：平台合作背景。

- sets_up_cn：说明实验引入的新信号是全新的。

- evidence_pointer：Section 3.1

### 38. Section 3.2 S1

- order：38

- section：Experiment

- locator：Section 3.2 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：随机选取2万多名用户并随机分配到三组；验证邀请只发送给当时在线用户并只发一次，增加被看到概率。

- rhetorical_function_cn：描述随机化与处理送达方式。

- depends_on_cn：随机实验设计目标。

- sets_up_cn：为因果识别提供操作细节。

- evidence_pointer：Section 3.2 S1

### 39. Section 3.2 S2

- order：39

- section：Experiment

- locator：Section 3.2 S2

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：按性别分层随机，以保证男女在实验组中比例均衡。

- rhetorical_function_cn：说明处理组平衡策略。

- depends_on_cn：性别差异文献。

- sets_up_cn：支持分性别分析的有效性。

- evidence_pointer：Section 3.2 S2

### 40. Section 3.2 S3

- order：40

- section：Experiment

- locator：Section 3.2 S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：邀请信息说明验证使用手机号、目的是减少诈骗并让对方知道你是真实的；T1支付50虚拟币，T2免费；承诺不泄露信息。

- rhetorical_function_cn：描述处理内容与成本操纵。

- depends_on_cn：付费/免费对比目标。

- sets_up_cn：为操纵检验和信号解释提供材料。

- evidence_pointer：Section 3.2 S3

### 41. Section 3.2 S4

- order：41

- section：Experiment

- locator：Section 3.2 S4

- move_code：DESIGN_FEATURE

- paraphrase_cn：一个手机号只能验证一个账号；成功后显示徽章；实验期间无其他并行实验。

- rhetorical_function_cn：控制验证的唯一性与干扰。

- depends_on_cn：前面对验证流程的描述。

- sets_up_cn：支持排除多账号和并行实验干扰。

- evidence_pointer：Section 3.2 S4

### 42. Section 4.1

- order：42

- section：Data

- locator：Section 4.1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：将消息按发起方向分为msg_received和msg_sent，三轮回话定义为匹配；所有协变量是分配前快照。

- rhetorical_function_cn：定义结果变量与协变量时序。

- depends_on_cn：在线约会消息数据。

- sets_up_cn：为后续回归和因果解释提供变量定义。

- evidence_pointer：Section 4.1

### 43. Section 4.2 P1

- order：43

- section：Data

- locator：Section 4.2 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用深度学习而非人工编码美貌，因为人工编码不可扩展且有隐私问题。

- rhetorical_function_cn：论证深度学习测量的必要性。

- depends_on_cn：美貌作为重要属性的理论。

- sets_up_cn：为模型训练细节作铺垫。

- evidence_pointer：Section 4.2 P1

### 44. Section 4.2 P3–P4

- order：44

- section：Data

- locator：Section 4.2 P3–P4

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：使用公开数据集训练DenseNet-121，五折交叉验证得到MAE=0.24、MSE=0.10；人脸检测裁剪，约2%照片被剔除。

- rhetorical_function_cn：建立模型精度基准。

- depends_on_cn：深度学习训练流程。

- sets_up_cn：为美貌作为可信变量的后续分析提供测量有效性。

- evidence_pointer：Section 4.2 P3–P4, Table 2

### 45. Section 4.2 end

- order：45

- section：Data

- locator：Section 4.2 end

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：还为男性训练美貌模型，用以验证既有性别排序差异。

- rhetorical_function_cn：说明辅助验证设计。

- depends_on_cn：男女都有照片数据。

- sets_up_cn：为后文女性美貌比男性收入更主导的论证提供对照。

- evidence_pointer：Section 4.2末尾

### 46. Section 5 intro, Table 3

- order：46

- section：Results

- locator：Section 5 intro, Table 3

- move_code：RESULT

- paraphrase_cn：表3显示各处理组与对照组在协变量上无显著差异，样本平衡。

- rhetorical_function_cn：报告随机化成功。

- depends_on_cn：实验设计。

- sets_up_cn：支持后续因果解释。

- evidence_pointer：Table 3

### 47. Section 5.1.1 S1

- order：47

- section：Results

- locator：Section 5.1.1 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：因处理随机分配，用线性概率模型估计验证选择的因果效应，并按性别分别估计。

- rhetorical_function_cn：交代估计方程。

- depends_on_cn：随机实验设计。

- sets_up_cn：为T1/T2验证率估计提供方法基础。

- evidence_pointer：Section 5.1.1 S1

### 48. Section 5.1.1 results

- order：48

- section：Results

- locator：Section 5.1.1 results

- move_code：RESULT

- paraphrase_cn：T1验证率约8%，T2增加约2个百分点，说明费用降低验证意愿。

- rhetorical_function_cn：报告成本效应。

- depends_on_cn：Table 4。

- sets_up_cn：为付费/免费比较提供基础。

- evidence_pointer：Section 5.1.1 results, Table 4

### 49. Section 5.1.1 type segmentation

- order：49

- section：Results

- locator：Section 5.1.1 type segmentation

- move_code：RESULT

- paraphrase_cn：按popularity均值±1标准差将男女分别分为L/M/H；男性验证率单调上升，女性M型最高、H型显著低于M型。

- rhetorical_function_cn：报告核心类型异质性。

- depends_on_cn：类型分割方法。

- sets_up_cn：为5.1.2机制检验制造谜题。

- evidence_pointer：Section 5.1.1, Table 5

### 50. Section 5.1.2 P1

- order：50

- section：Results

- locator：Section 5.1.2 P1

- move_code：TRANSITION

- paraphrase_cn：女性总体需求较高不能解释女性内部M型最高，因此需转向信号理论中已有信号强度与可信度。

- rhetorical_function_cn：从结果过渡到机制。

- depends_on_cn：Table 5中的非单调模式。

- sets_up_cn：为收入/美貌主导信号分析开路。

- evidence_pointer：Section 5.1.2 P1

### 51. Section 5.1.2 P2

- order：51

- section：Results

- locator：Section 5.1.2 P2

- move_code：MECHANISM

- paraphrase_cn：文献显示男性更看重美貌、女性更看重收入，作者用数据验证美貌/收入分别与女性/男性popularity相关性最高。

- rhetorical_function_cn：识别两侧主导信号。

- depends_on_cn：性别偏好文献。

- sets_up_cn：为后续可信度差异提供变量。

- evidence_pointer：Section 5.1.2 P2

### 52. Section 5.1.2 P3–P4

- order：52

- section：Results

- locator：Section 5.1.2 P3–P4

- move_code：MECHANISM

- paraphrase_cn：美貌来自照片容易核验，收入是自我报告的范围值更难验证，因此美貌作为主导信号更可信。

- rhetorical_function_cn：建立主导信号可信度差异的机制。

- depends_on_cn：信息可验证性文献。

- sets_up_cn：解释为何男性H型验证而女性H型不验证。

- evidence_pointer：Section 5.1.2 P3–P4

### 53. Section 5.1.2 P5

- order：53

- section：Results

- locator：Section 5.1.2 P5

- move_code：MECHANISM

- paraphrase_cn：H型男性因收入信号嘈杂而更可能采纳新信号；H型女性因美貌已足以区分而不太采纳新信号。

- rhetorical_function_cn：用信号理论连接可信度与选择。

- depends_on_cn：反信号理论。

- sets_up_cn：为Table 7和Table 8的预测提供逻辑。

- evidence_pointer：Section 5.1.2 P5

### 54. Section 5.1.2 Table 6

- order：54

- section：Results

- locator：Section 5.1.2 Table 6

- move_code：RESULT

- paraphrase_cn：女性美貌H-M需求差显著大于男性收入H-M需求差。

- rhetorical_function_cn：用需求差量化主导信号可信度差异。

- depends_on_cn：主导属性分割与popularity数据。

- sets_up_cn：支持“美貌比收入更可信”的机制。

- evidence_pointer：Section 5.1.2, Table 6

### 55. Section 5.1.2 Tables 7–8

- order：55

- section：Results

- locator：Section 5.1.2 Tables 7–8

- move_code：RESULT

- paraphrase_cn：beauty_High女性验证率低于beauty_Medium女性；income_High男性验证率高于income_Medium男性。

- rhetorical_function_cn：直接检验主导信号对验证选择的影响。

- depends_on_cn：类型分割和回归模型。

- sets_up_cn：为核心机制主张提供直接证据。

- evidence_pointer：Table 7, Table 8

### 56. Section 5.2 P1

- order：56

- section：Results

- locator：Section 5.2 P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：随机化使处理接受者外生；作者估计TOT即实际验证者效应，并将LATE作为稳健性。

- rhetorical_function_cn：交代因果参数。

- depends_on_cn：随机实验设计。

- sets_up_cn：为后果分析提供识别策略。

- evidence_pointer：Section 5.2 P1

### 57. Section 5.2.1 Table 9

- order：57

- section：Results

- locator：Section 5.2.1 Table 9

- move_code：RESULT

- paraphrase_cn：验证显著增加收到消息的数量，也提高消息发起者的平均popularity。

- rhetorical_function_cn：报告接收者反应结果。

- depends_on_cn：TOT估计。

- sets_up_cn：为类型分解结果作整体判断。

- evidence_pointer：Section 5.2.1, Table 9

### 58. Section 5.2.1 Table 10

- order：58

- section：Results

- locator：Section 5.2.1 Table 10

- move_code：RESULT

- paraphrase_cn：按类型分解后，H型男性和M型女性受益最大；M型女性吸引更多关注但未伤害H型女性。

- rhetorical_function_cn：验证事前选择与事后收益对应。

- depends_on_cn：Table 9的总体效应。

- sets_up_cn：为平台层面匹配结果提供个体基础。

- evidence_pointer：Section 5.2.1, Table 10

### 59. Section 5.2.2 Table 11

- order：59

- section：Results

- locator：Section 5.2.2 Table 11

- move_code：RESULT

- paraphrase_cn：验证者更主动，发送更多消息，并联系更高popularity的对象。

- rhetorical_function_cn：报告发送者行为变化。

- depends_on_cn：主动发信变量。

- sets_up_cn：为“信号影响发送者”的理论贡献提供证据。

- evidence_pointer：Section 5.2.2, Table 11

### 60. Section 5.2.2 Table 12

- order：60

- section：Results

- locator：Section 5.2.2 Table 12

- move_code：RESULT

- paraphrase_cn：主动性提升集中在H型男性和M型女性；女性主动性的增加对平台尤其有价值。

- rhetorical_function_cn：报告异质性并强调平台价值。

- depends_on_cn：类型分解。

- sets_up_cn：为平台匹配改善提供机制通道。

- evidence_pointer：Section 5.2.2, Table 12

### 61. Section 5.3.1 Tables 13–14

- order：61

- section：Results

- locator：Section 5.3.1 Tables 13–14

- move_code：RESULT

- paraphrase_cn：验证提高最终匹配数，H型男性和M型女性获益最大；效果来自接收联系与主动联系双通道。

- rhetorical_function_cn：报告平台层面结果。

- depends_on_cn：匹配结果变量。

- sets_up_cn：为平台受益主张提供依据。

- evidence_pointer：Section 5.3.1, Table 13, Table 14

### 62. Section 5.3.2

- order：62

- section：Results

- locator：Section 5.3.2

- move_code：RESULT

- paraphrase_cn：免费验证与付费验证均有效，但免费验证覆盖更高，付费验证带来更主动的验证者。

- rhetorical_function_cn：报告付费/免费权衡。

- depends_on_cn：Wald检验。

- sets_up_cn：为实践设计建议提供直接依据。

- evidence_pointer：Section 5.3.2

### 63. Section 6.1

- order：63

- section：Robustness

- locator：Section 6.1

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：MTurk操纵检验显示91%和86%的人将付费/免费验证邀请理解为差异化机会。

- rhetorical_function_cn：验证处理被感知为信号。

- depends_on_cn：邀请文案。

- sets_up_cn：排除处理被误解的可能。

- evidence_pointer：Section 6.1

### 64. Section 6.2 P1

- order：64

- section：Robustness

- locator：Section 6.2 P1

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：用来自验证用户与未验证用户消息之比排除同质性；结果与信号机制一致。

- rhetorical_function_cn：排除替代机制。

- depends_on_cn：ratio_msg_received构造。

- sets_up_cn：强化信号解释。

- evidence_pointer：Section 6.2 P1, Table A6

### 65. Section 6.2 P2–P4

- order：65

- section：Robustness

- locator：Section 6.2 P2–P4

- move_code：MECHANISM

- paraphrase_cn：手机号属敏感PII；可选验证让愿意分享PII的用户传递可信度；验证者平均多分享27%自我信息；63%不验证者因隐私；手机验证者更可能验证LinkedIn。

- rhetorical_function_cn：用调查和替代行为证据说明信号语义。

- depends_on_cn：隐私披露文献。

- sets_up_cn：为“信号是分享意愿”的机制主张提供支撑。

- evidence_pointer：Section 6.2 P2–P4, Table 15

### 66. Section 6.3

- order：66

- section：Robustness

- locator：Section 6.3

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：社会连接与验证用户无交互作用；LATE和负二项模型结果一致。

- rhetorical_function_cn：排除干扰与模型设定问题。

- depends_on_cn：备选模型和连接度变量。

- sets_up_cn：增强因果推断可信度。

- evidence_pointer：Section 6.3, Tables A7–A11

### 67. Section 6.4

- order：67

- section：Robustness

- locator：Section 6.4

- move_code：ROBUSTNESS_OR_BOUNDARY_TEST

- paraphrase_cn：控制组未泄气；排除发送与接收同时性；替代类型分割、连续度量、中介和子组随机化均保持一致。

- rhetorical_function_cn：系统排除各种替代解释。

- depends_on_cn：多种额外检验。

- sets_up_cn：为核心结论提供广泛稳健性。

- evidence_pointer：Section 6.4, Tables A12–A19

### 68. Section 7.1 P1

- order：68

- section：Discussion

- locator：Section 7.1 P1

- move_code：CONTRIBUTION

- paraphrase_cn：本研究首次在信息不对称匹配平台中检验自愿验证作为信号。

- rhetorical_function_cn：回扣引言中的核心主张。

- depends_on_cn：全部结果。

- sets_up_cn：为后续理论贡献作统摄。

- evidence_pointer：Section 7.1 P1

### 69. Section 7.1 P2–P3

- order：69

- section：Discussion

- locator：Section 7.1 P2–P3

- move_code：CONTRIBUTION

- paraphrase_cn：虽然验证机制对所有人相同，但平台两侧却策略性不同使用；M型有时比H型更有激励发送信号。

- rhetorical_function_cn：强调双边异质性的新颖贡献。

- depends_on_cn：验证决策异质性结果。

- sets_up_cn：与反信号理论对话。

- evidence_pointer：Section 7.1 P2–P3

### 70. Section 7.1 P4

- order：70

- section：Discussion

- locator：Section 7.1 P4

- move_code：MECHANISM

- paraphrase_cn：差异采用与两侧现有主导信号的可信度有关；可选验证提升M型女性需求而不伤害H型女性，并帮H型男性区分自己。

- rhetorical_function_cn：把机制与平台匹配改善重新连接。

- depends_on_cn：Table 6–8和Table 13–14。

- sets_up_cn：为平台设计建议提供机制依据。

- evidence_pointer：Section 7.1 P4

### 71. Section 7.1 P5

- order：71

- section：Discussion

- locator：Section 7.1 P5

- move_code：MECHANISM

- paraphrase_cn：验证意愿传达愿意分享个人信息的信号，是与收入/美貌正交的属性。

- rhetorical_function_cn：界定验证信号的语义维度。

- depends_on_cn：隐私调查和LinkedIn验证。

- sets_up_cn：为推广到其他可选验证机制做铺垫。

- evidence_pointer：Section 7.1 P5

### 72. Section 7.1 P6

- order：72

- section：Discussion

- locator：Section 7.1 P6

- move_code：CONTRIBUTION

- paraphrase_cn：验证者行为更主动，研究首次揭示信号对发送者自身的影响。

- rhetorical_function_cn：把发送者行为变化上升为贡献。

- depends_on_cn：Table 11–12。

- sets_up_cn：扩展信号理论边界。

- evidence_pointer：Section 7.1 P6

### 73. Section 7.1 P7

- order：73

- section：Discussion

- locator：Section 7.1 P7

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：免费与付费验证存在覆盖与强度权衡，因此不同阶段平台可选择不同设计。

- rhetorical_function_cn：把结果转成可操作设计规则。

- depends_on_cn：T1/T2对比。

- sets_up_cn：为实践贡献提供直接建议。

- evidence_pointer：Section 7.1 P7

### 74. Section 7.2

- order：74

- section：Discussion

- locator：Section 7.2

- move_code：CONTRIBUTION

- paraphrase_cn：理论贡献包括：把信号研究扩展到双边匹配市场、为非单调选择提供现场证据、把信号影响从接收者扩展到发送者。

- rhetorical_function_cn：系统总结理论贡献。

- depends_on_cn：全文理论对话。

- sets_up_cn：强化论文在信号文献中的位置。

- evidence_pointer：Section 7.2

### 75. Section 7.3

- order：75

- section：Discussion

- locator：Section 7.3

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：实践启示：平台设计者应考虑每侧已有主导信号的可信度；新信号会帮助H型还是M型取决于此；自由/付费可按平台目标选择。

- rhetorical_function_cn：把结论转化为设计知识。

- depends_on_cn：机制与付费/免费结果。

- sets_up_cn：为未来平台设计提供可复用原则。

- evidence_pointer：Section 7.3

### 76. Section 7.4

- order：76

- section：Discussion

- locator：Section 7.4

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：限制包括观察期较短无法研究学习效应、只研究单一新信号未研究多信号交互、需要向其他早期匹配平台推广以验证泛化。

- rhetorical_function_cn：交代边界和未来方向。

- depends_on_cn：研究设计局限。

- sets_up_cn：防止读者过度推广。

- evidence_pointer：Section 7.4

## 写作技术

- gap_construction_cn：通过“强制验证”与“可选验证”的对比制造概念缺口；通过“以往研究只看事后有效性”和“信号只给一侧”制造文献缺口；再以“约会平台没有评分/评论、信息自我披露”制造情境缺口，最终把论文定位为首次在同一平台两侧研究可选验证的事前采用与事后影响。

- signposting_cn：引言末尾用“who chooses to verify? What mechanism? How influence partners? How influence users? Platform-level outcomes?”列成路标；正文小标题直接复述这些问题；每节开头先点明研究问题，结尾预告下一步。

- transition_logic_cn：从事前选择到事后结果用“ex ante choices should align with ex post responses”过渡；从接收者反应到发送者行为用“More interestingly, verified users become more proactive”过渡；从个体到平台用“platform as a whole”过渡；从主结果到稳健性用“additional analyses”过渡；讨论重新回到引言的缺口与贡献列表。

- claim_evidence_rhythm_cn：每个主要主张先以简洁结果句出现，再用表格和回归系数支撑；先报总体效应，再按用户类型分解；每个机制主张随后用针对性的表或调查证据跟进；稳健性表放在在线附录以保持正文简洁。

- benchmark_narrative_cn：随机实验本身以无验证机会的对照组为自然基准；付费与免费验证互为成本基准；类型分割中的L型为参照组；主导信号可信度用H-M需求差互相对比；替代模型如LATE、负二项、不同分割作为稳健基准。

- theory_return_cn：在讨论中把“男性单调、女性倒U”重新表述为信号理论中传统预测与计分信号的结合；把“验证者更主动”送回Lazear式的信号获取后行为变化；把“付费/免费权衡”送回平台设计理论，而不是停在一次性结果。

- contribution_positioning_cn：用“among the first”“hardly any studies”“in contrast to previous studies”反复标定新颖性；将贡献分理论、实证与实践三层，并通过“same signal, two sides”这一概括使文章贡献易记。

- novelty_protection_cn：通过机制检验（现有主导信号可信度）解释异质性，避免只报告一个偶然现象；通过调查和LinkedIn验证把信号语义具体化为PII披露意愿；通过同质性排除和社交干扰检验保护信号解释；通过LATE、负二项、替代分割等稳健性检验保护因果结论，使贡献不局限为某一组的性能差异。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：在平台机制中找到一个理论可用但未被实证的缺口，如强制变可选、事前采用未被研究。

- research_job_cn：选择一个信息不对称严重且缺少替代声誉机制的市场平台。

- required_evidence_cn：需要说明该平台没有评分/评论、资料自我披露、现有机制多为强制验证。

- transition_to_next_cn：从现实缺口切到信号理论。

#### 2. 2

- step：2

- writing_job_cn：引入信号理论，并同时呈现经典预测与反信号预测。

- research_job_cn：梳理性别偏好、自愿披露、隐私、发送者行为等理论线索，形成可检验的对比预测。

- required_evidence_cn：理论上有理由预测不同用户类型可能采用不同模式，同时预测可采用哪一侧主导信号解释差异。

- transition_to_next_cn：从理论预测转到实验设计。

#### 3. 3

- step：3

- writing_job_cn：报告随机现场实验设计：对照、处理、邀请方式、成本操纵、可见徽章、防干扰措施。

- research_job_cn：与平台合作实现随机分配和真实行为追踪。

- required_evidence_cn：随机化平衡检验；处理送达方式；无并行实验。

- transition_to_next_cn：从设计转向数据与测量。

#### 4. 4

- step：4

- writing_job_cn：说明关键构念如何测度；若用深度学习，给出训练数据、模型、交叉验证误差和处理隐私的方式。

- research_job_cn：训练并验证美貌预测模型，构建收入、popularity等快照变量。

- required_evidence_cn：预测误差与文献相当；对缺失或无法检测图片的剔除规则透明。

- transition_to_next_cn：从测量转向采用决策。

#### 5. 5

- step：5

- writing_job_cn：先报告总体验证率，再按性别和类型报告验证率，形成“谁选择验证”的核心现象。

- research_job_cn：估计T1/T2验证率，按popularity类型分割并检验差异。

- required_evidence_cn：总体效应显著，类型异质性显著，并显示付费成本降低验证率。

- transition_to_next_cn：“为什么不同”进入机制。

#### 6. 6

- step：6

- writing_job_cn：用主导信号可信度解释异质性；报告需求差和收入/美貌对验证选择的相关关系。

- research_job_cn：验证性别偏好与popularity的相关性；比较主导信号H-M需求差；控制second_signal。

- required_evidence_cn：需求差检验显示主导信号可信度不同；收入/美貌变量与验证选择的相关方向符合预测。

- transition_to_next_cn：从选择转向后果。

#### 7. 7

- step：7

- writing_job_cn：报告验证对收到消息、主动发信和最终匹配的影响；先用总体，再按类型分解。

- research_job_cn：用ITT/TOT或LATE估计后果；按H/M/L类型和性别分解；检验事前预测与事后收益一致。

- required_evidence_cn：接收数量与质量显著增加；主动发信显著增加；最可能验证的群体获益最大。

- transition_to_next_cn：从个体结果转向平台层面。

#### 8. 8

- step：8

- writing_job_cn：把结果提升到平台匹配与设计知识，包括付费/免费权衡。

- research_job_cn：估计匹配结果；比较T1/T2；讨论覆盖与主动性权衡。

- required_evidence_cn：匹配增加且异质性符合预期；付费/免费差异显著或边界显著。

- transition_to_next_cn：从主结果转向稳健性。

#### 9. 9

- step：9

- writing_job_cn：用操纵检验、替代机制检验、备选模型和多种稳健性检验排除替代解释。

- research_job_cn：设计调查、同质性比率、社交干扰检验、LATE、负二项、替代分割、连续测量和中介分析。

- required_evidence_cn：操纵理解正确；同质性等替代解释不成立；备选模型方向一致。

- transition_to_next_cn：进入讨论并回扣理论。

### most_transferable_moves_cn

1. 把强制机制改成可选机制并追问信号功能，是可迁移的问题建构方式

2. 同时分析事前采用与事后结果，使文章不只停留在有效性

3. 把异质性解释为“已有主导信号可信度”，而非简单人口统计差异

4. 用调查和替代行为（LinkedIn验证）支撑信号语义

5. 用“两侧使用同一信号不同”制造双边市场的理论贡献

6. 用付费/免费对比生成可操作设计知识

7. 用LATE、负二项、替代分割等系统稳健性保护结论

### resource_intensive_or_nonstandard_parts_cn

1. 与大型真实交友平台的合作关系和随机实验权限

2. 20,000+用户样本和平台内部popularity评分

3. 一次性邀请与徽章展示需要平台工程支持

4. 用于深度学习训练的公开美貌数据集和用户照片访问权限

5. 平台内调查（LinkedIn验证、隐私原因调查）需要用户触达

6. 确保实验期间无并行实验需要平台配合

### what_not_to_copy_superficially_cn

1. 不能只宣称“可选验证有价值”而没有验证用户选择与后果数据

2. 不能只报告异质性模式而缺少对现有主导信号的机制检验

3. 不能把“更多消息”直接说成“更好匹配”而不提供匹配结果或质量证据

4. 不能把“隐私意愿”当作机制而不用调查或替代行为进行至少间接验证

5. 不能在没有对照组的非随机数据中套用TOT/LATE语言

6. 不能因在线附录有稳健性检验就在正文中省略对替代解释的实质讨论

- single_best_description_of_the_routine_cn：在一个缺乏声誉机制的真实匹配平台中，把常见强制验证改为可选并随机变化成本，用信号理论解释谁选择验证，再用事后消息、主动发信和匹配结果追踪该信号的接收者与发送者双重效应，最后用机制调查和稳健性检验把一次性实验结果提升为双边市场信号设计知识。

## 分析边界

全文主体完整，但在线附录的详细表格（A5–A19）与部分子样本统计未在本文中提供，只能依据正文引用与文字总结判断；图3原始图像无法从文本中读取具体细节；因此对稳健性分析的统计量核查有限。
