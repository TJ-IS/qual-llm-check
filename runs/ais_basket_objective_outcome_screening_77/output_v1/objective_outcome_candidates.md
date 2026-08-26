# Objective-outcome screening of 77 software-design candidates

Completed: 77 / 77
Retained: 66

## A Warning Approach to Mitigating Bandwagon Bias in Online Ratings: Theoretical Analysis and Experimental Investigations

- Year/journal: 2023 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00817
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 本文的软件/内容工件是评分页面上的警告设计，包括直接风险警告和带排序任务的风险警告。该设计旨在通过改变警告内容影响用户最终提交的评分，减少向显示平均分靠拢的从众偏差，并在无偏差情况下避免不必要的评分扭曲；这些效果均以客观的DDAR（实际提交评分与显示平均分之差的绝对值）衡量。
- Decision: 两个纳入路径均成立：一是警告策略被明确设计为减少在线评分中的从众偏差，属于客观行为/结果目标；二是主要因变量DDAR由参与者实际提交的评分计算而来，是客观记录的行为结果，而非自我报告感知。因此 objective_outcome_match=true。
- Confidence: 0.98

  - Outcome: DDAR (Distance to Displayed Average Rating) (primary)
  - Measurement: 在实验中，参与者观看目标微电影后在10星量表上提交评分；系统显示的操作化平均评分（如向下调整、向上调整或未调整）与参与者最终提交评分之差的绝对值即为DDAR，即 DDAR = |个体评分 - 显示平均评分|。通过顺序回归模型和非参数检验比较不同警告组的DDAR分布。
  - Objectivity: DDAR基于参与者在实验系统中实际提交的评分计算，是可观察的行为记录，而非自我报告的态度、感知或意图；显示的平均评分由实验者操纵，具有明确的地面真值。

## Addressing Online Users’ Suspicion of Sponsored Search Results: Effects of Informational Cues

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2021.0364
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 所测试的软件/界面设计要素是在搜索结果页面上为赞助搜索结果（SSR）提供正面的信息提示（产品质量评级线索或卖家信誉评级线索）。这些线索的部署被明确设计为通过降低决策不确定性和平台恶意感知来增加用户对SSR的处理（减少回避），并以实际点击行为和眼动注意作为关键的客观行为结果加以评估。
- Decision: 文章满足两条纳入路径：(1) 明确的设计目标是通过在SSR旁呈现信息线索来增加用户对SSR的处理（减少回避），这包括实际点击行为等客观行为结果；(2) 实证测量中包含了客观测量，例如实际点击/不点击SSR的行为记录和眼动仪注视数据，而非仅依赖自我报告。自我报告变量虽然存在，但研究至少有一个实质性的客观结局指标。
- Confidence: 0.98

  - Outcome: Behavioral avoidance of the sponsored search result (click/non-click on SSR) (primary)
  - Measurement: 在三个实验室实验中，记录参与者是否实际点击了实验性赞助搜索结果（SSR）的二元行为；未点击视为行为性回避，点击视为处理SSR的行为方面。
  - Objectivity: 这是实际点击行为的系统日志/观察记录，不依赖参与者的自我报告，属于客观行为测量。
  - Outcome: Eye-tracking measures of cognitive avoidance: percentage of fixations on the SSR and percentage of time viewing the SSR (secondary)
  - Measurement: 在实验1中，使用眼动仪记录参与者在SSR区域上的注视比例和注视时间比例，作为认知回避的补充测量。
  - Objectivity: 眼动数据是生理/行为传感器记录，非自我报告，客观反映视觉注意力分配。

## Animation as a dynamic visualization technique for improving process model comprehension

- Year/journal: 2021 / Information & Management
- DOI: 10.1016/j.im.2021.103478
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 研究的软件工件是自适应动画环境（低交互视频动画与高交互分步动画），作为实验处理条件与静态过程模型可视化对比；其明确设计目标是提升过程模型理解绩效，并通过客观理解测试分数进行评价。结果支持动画对理解分数的正向效应，且受专业知识水平的U型调节。
- Decision: 两条纳入路径均成立：动画环境明确以提升过程模型理解这一实质性绩效为目标；同时，核心结果变量为客观评分的问题解决测试分数，基于专家预先确定的正确答案和研究者依据评分标准对开放题的评价，不依赖自我报告。
- Confidence: 0.98

  - Outcome: Process model comprehension test score (primary)
  - Measurement: 针对每个过程模型提出8个封闭式问题（是/否/不知道）和1个开放式问题；封闭式问题根据预先确定的正确答案计分，开放式问题由两名研究者依据专家共识的评分标准独立评分，最终汇总为0-100的总分。
  - Objectivity: 该结果是对问题回答正确性的客观计分，并非参与者自我报告；正确答案由三名专家研究者事先确定，开放式答案也依据可核查的评分标准由研究者判定，而非仅依赖参与者的主观感知。
  - Outcome: Comprehension time / overall test time (secondary)
  - Measurement: 在线实验环境记录的参与者完成整体测试所花费的时间；作者检验了动画和专业知识水平对测试时间的影响。
  - Objectivity: 时间数据由在线系统自动记录，属于系统日志类的客观行为测量，不依赖自我报告。

## Augmenting Password Strength Meter Design Using the Elaboration Likelihood Model: Evidence from Randomized Experiments

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1125
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 软件工件是ELM增强的密码强度计（Time/Rank/Probability三种说服性消息相比Control），其明确设计目标是促使用户生成更强的密码并更愿意修改初选弱密码；研究通过实验室和实地随机实验中的实际密码强度变化和修改次数来衡量该设计效果。
- Decision: 两条路径均成立：论文明确将增强密码强度计作为设计工件，目标是改善用户的密码生成行为（更可能修改密码且新密码更强），属于客观设计目标；同时，核心因变量（密码强度增加量、密码修改次数、是否点击安全提示链接）均由系统日志或算法实时计算，不依赖自我报告。
- Confidence: 0.98

  - Outcome: Increase in password strength (diff_strength) (primary)
  - Measurement: 记录用户在提交前和看到密码强度计警告后所输入密码的强度差异；强度由基于RockYou数据集训练的backoff Markov模型计算，并取自然对数。实验室和实地实验中均由系统实时计算并记录。
  - Objectivity: 基于实际输入密码的算法计算，不依赖用户自我报告；密码强度计算规则固定且可复现，属于客观行为/绩效度量。
  - Outcome: Number of password revisions after meter feedback (num_reset) (primary)
  - Measurement: 统计用户在观察到密码强度计警告后立即修改密码的次数；实验室中从系统交互日志记录，实地实验中通过API记录密码强度变化次数。
  - Objectivity: 由系统日志或运行时间计算的行为计数，非自我报告。
  - Outcome: Clicking 'Tips towards strong passwords' (learn_more) (secondary)
  - Measurement: 记录用户是否点击密码强度计下方的‘Tips towards strong passwords’链接，0/1变量；实验室实验通过系统交互日志记录。
  - Objectivity: 点击行为来自系统日志，属于客观行为测量，而非主观报告。

## Cognitive Challenges in Human–Artificial Intelligence Collaboration: Investigating the Path Toward Productive Delegation

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2021.1079
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 本文的核心软件/算法设计是允许AI根据自身置信度将图像委托给人类（inversion），以及在人类侧解释或强制执行委托策略；这些设计显式以提升分类准确率为目标，实验结果中inversion准确率显著高于AI单独运行，说明材料设计直接联系到客观绩效结果。
- Decision: 客观上，分类准确率基于ImageNet真实标签客观评分，委托率基于系统日志的实际行为，二者均为实质性客观结果；同时，AI委托机制和策略解释/强制执行条件的设计明确以提升准确率为目标，因此两条纳入路径均成立。
- Confidence: 0.98

  - Outcome: Classification accuracy (primary)
  - Measurement: 对100张来自ImageNet且具有已知类别标签的图像进行分类，将人类或AI给出的分类结果与真实标签（ground truth）比对，计算正确分类的图像百分比。
  - Objectivity: 正确性由预先存在的ImageNet人工标注真实标签客观判定，不依赖参与者自我报告；正确分类还有金钱激励。
  - Outcome: Delegation rate (secondary)
  - Measurement: 统计每个参与者或每张图像上点击“将该题委托给AI”按钮的次数占总图像数的比例；AI回答被视为参与者答案并据此支付。
  - Objectivity: 委托行为由系统交互日志直接记录，是可观察的实际选择行为，而非自我报告的意向或态度。
  - Outcome: AI inversion combined accuracy (AI delegating to humans) (artifact_performance_target)
  - Measurement: AI根据其置信度得分是否低于阈值（平均人类准确率）决定自行分类还是委托给配对的人类参与者；最终分类结果与ImageNet真实标签比对计算准确率。
  - Objectivity: 该指标是基于事先固定的委托规则和真实标签客观计算的组合性能，是显式设计目标（假设1.2）的客观验证。

## Cost-based analysis of the impact of data completeness and representational consistency

- Year/journal: 2023 / Decision Support Systems
- DOI: 10.1016/j.dss.2023.114044
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 研究比较了三个集成数据库版本（D_A原始数据、D_B和D_C依次改进完整性和表示一致性），并通过在线SQL查询平台让参与者完成任务；上述客观绩效指标用于量化数据质量改进对任务可用性的影响。
- Decision: 该研究明确以成本为基础的数据质量分析为目标，设计三种数据库版本以改进完整性和一致性，并衡量这些改进对任务解决能力的客观影响；同时，核心因变量（能否正确解决、解决时间、查询次数）均由实验平台日志和自动答案比对客观测量，符合两条纳入路径。
- Confidence: 0.98

  - Outcome: Ability to solve tasks (P_correct) (primary)
  - Measurement: 实验平台自动将参与者提交的SQL查询返回结果与模型解返回结果进行比较，判定查询是否正确；统计每个任务中能够构造出正确查询的参与者比例。
  - Objectivity: 正确性由系统依据预定义的模型解自动判定，不依赖参与者的自我报告或主观评价。
  - Outcome: Time to solve tasks (T_solved) (primary)
  - Measurement: 从平台日志中提取参与者提交正确查询的时间戳，计算其开始任务到获得正确解所需的时间（仅针对成功解出任务的参与者）。
  - Objectivity: 时间来自系统自动记录的时间戳，是客观的行为绩效测量，而非自我报告的耗时或感知负担。
  - Outcome: Number of attempts / queries needed (primary)
  - Measurement: 从查询日志中统计每位参与者在每个任务上提交的查询总数，以及其中与数据质量问题和其它问题相关的查询数量。
  - Objectivity: 查询数量由系统日志客观记录，反映实际行为；对错误原因的分类虽有研究者人工判断，但查询总数本身是客观计数。

## Could Gamification Designs Enhance Online Learning Through Personalization? Lessons from a Field Experiment

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1123
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 研究者在MOOC平台上设计并实施的四类游戏化绩效反馈（个人/社会比较 × 正向/负向框架）作为软件设计改动，明确旨在通过匹配学习者目标导向来提高SRL投入、学习效率和学习结果；SRL投入作为中介影响测试成绩。
- Decision: 两条路线均满足：游戏化反馈设计的明确目标是改善实质性的学习行为表现（SRL投入、学习效率、学习成效）；同时这些核心结果变量均通过平台日志、时间/生存分析和客观计分的知识/操作测试来测量，而非仅依赖自我报告。
- Confidence: 0.98

  - Outcome: SRL engagement (primary)
  - Measurement: 通过MOOC平台记录的学习行为数字痕迹测量，包括制定学习计划、计划完成率、计划修订次数、论坛提问/讨论数、测验尝试次数、笔记数和反思提交等，再取三个SRL阶段的主成分作为SRL投入指标（Table 1, Section 3.5）。
  - Objectivity: 数据来自系统日志和平台数字痕迹，而非参与者的自我报告或主观评分。
  - Outcome: Learning efficiency (pace of module completion with SRL) (primary)
  - Measurement: 以完成一个模块并经历三个SRL阶段所需的时间来衡量，用Cox比例风险模型分析模块完成的速率（Section 3.5, Equation 2, Table 4 Column 2）。
  - Objectivity: 时间戳和系统记录的学习事件提供了客观的完成时间和进度数据，不是自我报告。
  - Outcome: Post-experiment knowledge test score (primary)
  - Measurement: 实验后进行的知识测试，范围0-25分，测量陈述性知识和概念理解（Table 3; Table 1; Table 5）。
  - Objectivity: 测试有客观正确答案，按对错计分，不依赖参与者主观感知。
  - Outcome: Post-experiment performance test score (primary)
  - Measurement: 实验后进行的操作/技能测试，范围0-75分，测量技能习得（Table 3; Table 1; Table 5）。
  - Objectivity: 测试基于可验证的实际任务表现评分，有明确判分标准，非自我报告。

## Delays in Information Presentation Lead to Brain State Switching, Which Degrades User Performance, and There May Not Be Much We Can Do about It

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2023/17680
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: Study 1 将信息呈现延迟本身作为系统特征，考察其对决策时间的影响。Study 2 将四种软件设计干预（同时/渐进式绩效显示、倒计时器、虚拟任务）嵌入延迟期间，明确以维持任务相关脑状态、改善反应时和准确率为目标；研究发现这些干预可部分缓解但未能消除延迟对客观绩效的损害。
- Decision: 两条纳入路径均成立：第一，Study 2 的四种系统设计干预明确以改善用户客观绩效（反应时和准确率）为目标，属于客观设计目标；第二，多项核心结果变量均为客观测量，包括 Study 1 的决策时间（按钮盒记录）、脑状态切换（fMRI 算法检测），以及 Study 2 的警觉任务错误率和反应时（客观按键记录）。
- Confidence: 0.98

  - Outcome: Decision time (Study 1) (primary)
  - Measurement: 通过 fMRI 实验中的按钮盒记录参与者从看到刺激到做出满意度/不满意度评价所需的时间（秒），即“决策时间”。
  - Objectivity: 这是系统记录的客观行为反应时，不依赖参与者的自我报告。
  - Outcome: Brain state switching (during delay and during task following delay, Study 1) (primary)
  - Measurement: 利用 fMRI 数据，通过 t-SNE 降维和步长距离阈值（mean + 10×SD）检测相邻时间点之间显著的脑状态变化，分别记录延迟期间和延迟后任务期间的脑状态切换（二值变量）。
  - Objectivity: 基于神经影像 BOLD 信号和算法化阈值检测，而非参与者的主观报告。
  - Outcome: Vigilance task error rates (go errors and no-go errors, Study 2) (artifact_performance_target)
  - Measurement: 在“go/no-go”警觉任务中，依据客观刺激数字（是否为“3”）和参与者的按键反应，计算“go”试次漏按错误率和“no-go”试次误按错误率。
  - Objectivity: 错误由刺激身份与按键行为的客观匹配决定，具有明确的标准答案，不依赖自我报告。
  - Outcome: Vigilance task response time (Study 2) (artifact_performance_target)
  - Measurement: 在 go/no-go 任务中，记录参与者在“go”试次中按下空格键的反应时间（毫秒），仅对实际发生按键的试次计算平均反应时。
  - Objectivity: 反应时由系统精确记录，是客观的行为表现指标，不依赖自我报告。

## Designing Conversational Dashboards for Effective Use in Crisis Response

- Year/journal: 2023 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00801
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 该文设计的会话式仪表盘（提供自然语言交互、鼠标交互以及会话式引导）被明确设计用于提高透明交互、效率和信息查找有效性。实验比较了不同设计实例（TDB、CDB-NLO、CDB-NLE，有无引导）对上述客观结果的影响，证明自然语言交互和会话式引导能显著改善透明交互，进而提升效率和有效性。
- Decision: 文章同时满足两条纳入路线：1) 设计目标明确为改善透明交互（TEU核心维度）及信息查找效率和有效性，属于客观绩效目标；2) 核心结果（透明交互、有效性、效率）均通过系统日志、任务正确性和时间等客观方式测量，NLP组件性能也基于地面真值标签客观评估。
- Confidence: 0.98

  - Outcome: Transparent interaction (behavioral measure) (primary)
  - Measurement: 基于用户与仪表盘交互的日志数据（鼠标点击、自然语言输入）计算：对于每个信息查找任务，确定完成该任务所需的最少导航步骤数，然后用该最小值除以参与者实际采取的导航步骤数（仅对正确完成的任务计算），最终取平均值。
  - Objectivity: 该测量使用系统交互日志和预定义的最短路径标准，而非参与者自我报告；论文中明确称其为行为测量，以避免自我报告的偏差。
  - Outcome: Effectiveness (number of correctly solved tasks) (secondary)
  - Measurement: 统计参与者在四个信息查找任务中正确作答的任务数量；任务答案由实验者预先设定客观正确答案（如具体州名、数字），参与者输入答案并与正确答案比对。
  - Objectivity: 任务完成正确性有明确的事实答案（如死亡人数、州名等），不是自我报告；论文将有效性定义为“用户达到任务目标的程度”，以正确解决的任务数衡量。
  - Outcome: Efficiency (time to complete correctly solved tasks) (secondary)
  - Measurement: 测量完成所有正确解决任务所需的平均时间（系统记录时间戳）。
  - Objectivity: 时间是基于系统日志的客观性能指标，不依赖参与者自我感知或报告。
  - Outcome: NLP component performance (speech-to-text accuracy, entity extraction, intent mapping) (artifact_performance_target)
  - Measurement: 使用3119条实际用户自然语言输入数据集，由人工标注地面真值（语音转录正确性、实体、意图），计算语音转写准确率、实体提取和意图映射的精确率、召回率和F1分数，以及平均响应时间。
  - Objectivity: 性能指标基于与人工标注的客观地面真值比较，属于技术系统的客观性能评估，而非用户自我报告。

## Designing Effective Mobile Health Apps: Does Combining Behavior Change Techniques Really Create Synergies?

- Year/journal: 2021 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2021.1912936
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 研究设计了四种包含社交向上比较和/或保护动机行为改变技术特征的mHealth原型（推送通知、绩效可见页面等），并以应用打开次数和训练完成次数作为客观使用结果来评估这些设计特征及组合的效果。
- Decision: 通过两条路径：1）软件设计特征明确以改善mHealth使用行为（应用打开、训练完成次数）为目标，假设H1-H3直接检验设计对客观使用的影响；2）核心因变量通过后台追踪日志客观测量，作者明确称之为objective measures of mHealth use。
- Confidence: 0.98

  - Outcome: Application opening (primary)
  - Measurement: 通过五周实地实验中移动应用原型的后台追踪数据，记录每位用户打开应用的次数。
  - Objectivity: 数据来自系统使用日志/追踪数据，而非用户自我报告。
  - Outcome: Training count (primary)
  - Measurement: 通过应用后台追踪数据统计用户完成的3分钟渐进式肌肉放松训练次数。
  - Objectivity: 训练完成次数由系统日志客观记录，不依赖受访者自报。

## How to elicit and cease herding behaviour? On the effectiveness of a warning message as a debiasing decision support system

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113652
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 本研究的软件工件包括两个DSS模拟工具以及作为去偏DSS的警告消息。警告消息被明确设计用于通过提醒用户同伴信息可能具有误导性来减少从众（herding）偏差，其效果通过用户在收到警告后是否改变对跟风选项的实际选择来衡量；同伴信息干预亦嵌入DSS界面，直接影响用户选择行为。因此，主要客观结果（选择跟风选项）正是该软件设计干预的直接行为结果。
- Decision: 两条路径均满足：(1) 目标路线：警告消息DSS被明确定位为减少从众偏差、改善决策质量的去偏干预，预期改变实际选择行为；(2) 客观测量路线：核心因变量为用户在DSS中的实际选项点击（选择跟风选项与否）以及警告后是否切换选择，均来自系统日志记录，不依赖自我报告。
- Confidence: 0.98

  - Outcome: Herding behaviour (choice of the herded option) (primary)
  - Measurement: 在随机对照试验中，通过DSS模拟工具记录被试实际点击选择的选项（Basic、Premium或Custom），将被试是否选择被标为‘Premium’的同伴信息目标选项编码为二值因变量（选中=1，未选中=0），比较实验组与对照组的选择比例及对数几率。
  - Objectivity: 该结果直接来自网站交互日志中记录的实际选择行为，而非被试自我报告的意图、态度或感知；选择行为是可独立观察和验证的。
  - Outcome: Warning message effectiveness (decision to switch from herded option after debiasing warning) (primary)
  - Measurement: 在实验组中，被试先选择初始选项，随后弹出警告信息，再允许被试修改选择；系统记录警告前后选择的选项，以警告后是否仍选择被同伴信息影响的选项（或是否改变初始选择）作为因变量，比较警告前后的选择变化。
  - Objectivity: 通过系统日志客观记录被试在收到警告消息前后的实际选项变更，不依赖自我报告；决策变更行为可直接观察。
  - Outcome: Peer information threshold for herding (percentage of peers shown and choice of herded option) (secondary)
  - Measurement: 实验组被试被随机展示10%至90%的同伴百分比，系统记录展示的百分比及其最终选择；通过将百分比分组（10-29%、30-49%、50-69%、70-89%）检验不同强度同伴信息对选择被同伴信息目标选项的影响。
  - Objectivity: 百分比由系统随机分配并记录，选择行为由系统日志记录；属客观行为数据而非自我报告。

## More Than a Bot? The Impact of Disclosing Human Involvement on Customer Interactions with Hybrid Service Agents

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2022.0152
- Objective design target: False
- Objectively measured outcome: True
- Artifact-outcome link: 研究操纵的软件设计特征是混合服务代理界面中的人工参与披露信息（欢迎消息中的前置披露和人工介入时的步骤披露）。该披露设计导致顾客在实际聊天中采用更偏向人际化的沟通风格（更长、更自然、密度更高的消息），并进而增加聊天机器人转交给员工的工作量（员工回复次数、响应时长和操作强度）。因此，软件特征（披露信息）与客观测量的顾客沟通行为和员工工作量之间存在因果关联。
- Decision: 纳入路线2成立：核心结果变量（顾客沟通风格和员工工作量）均通过系统日志、聊天文本算法分析和员工操作记录客观测量，不依赖参与者自我报告。路线1不适用，因为研究并非将披露设计为明确旨在改进某个客观结果的设计目标，而是检验其行为后果。
- Confidence: 0.98

  - Outcome: Customer communication style (human-oriented communication style) (primary)
  - Measurement: 基于真实聊天记录中的顾客消息文本计算三个指标：冗长性（每条消息平均词数）、复杂度（Coleman可读性公式）和密度（通过LIWC分类的功能词占总词数比例），并将三者作为潜变量的反映性指标。
  - Objectivity: 指标来自系统记录的聊天文本和确定性文本分析算法，不依赖顾客自我报告，是对实际沟通行为的客观测量。
  - Outcome: Employee workload (primary)
  - Measurement: 由系统日志和员工操作记录测量三个指标：频率（一次聊天中由员工而非聊天机器人发送的回复数）、时长（顾客消息与员工回复之间的响应时间总和）、强度（员工确认、编辑或全新输入回复的加权行动）。
  - Objectivity: 员工回复数量、响应时间和操作类型均来自后台系统记录，是可观察、可验证的工作行为，而非员工自我报告的工作量感知。
  - Outcome: Customer requests for human involvement (explicitly seeking an employee) (secondary)
  - Measurement: 人工复核所有聊天记录，识别顾客明确要求人工介入的消息，并比较各实验条件中这类请求的发生率。
  - Objectivity: 基于聊天文本中可观察的明确请求行为，而非顾客自报倾向；属于实际行为结果。
  - Outcome: Communication length (chat duration) (secondary)
  - Measurement: 利用聊天时间戳计算顾客与混合服务代理互动的总时长（分钟），比较不同披露条件下的差异。
  - Objectivity: 时间戳来自系统记录，属于客观的交互行为测量。

## On the Same Page? What Users Benefit from a Desktop View on Mobile Devices

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1140
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 本研究的实验平台是专门开发的酒店预订网站，其中操纵了移动端信息架构（移动IA）与桌面端信息架构（桌面IA）这一设计特征：桌面IA将所有属性呈现在单一概览页，移动IA将信息分层分布在概览页和详情页。该设计操纵直接作用于核心客观结果——决策准确性（反向编码为决策不准确性），研究发现移动IA显著降低决策准确性，从而支持了桌面视图对移动用户决策准确性的潜在益处。
- Decision: 文章满足两条纳入路径。第一，桌面视图被明确视为一种能提升移动用户决策准确性的设计选择，且这一客观绩效目标贯穿研究假设与实践建议（objective_design_target）。第二，核心因变量决策准确性通过WADD规范基准计算出的选择偏差来测量，属于客观可验证的正确性评分；信息搜索和决策时间也由系统日志客观测量（objectively_measured_outcome）。因此objective_outcome_match为真。
- Confidence: 0.98

  - Outcome: Decision accuracy (operationalized as decision inaccuracy) (primary)
  - Measurement: 在酒店预订多属性选择任务中，先引导参与者分配100分权重并选择各属性的偏好值；随后依据加权加性策略（WADD）计算每个备选方案与“理想”方案的标准化加权距离，从而对11个备选方案排序。决策不准确性被定义为参与者所选方案中比该选择更优（更接近偏好）的备选方案数量，取值0到10；决策准确性是该指标的反向。
  - Objectivity: 该测量基于明确的规范基准（WADD）和对参与者偏好权重的计算，而非参与者自我报告或主观评分；选择行为由系统记录，评分规则公开且可复现。
  - Outcome: Information search (secondary)
  - Measurement: 在做出选择前，系统记录参与者访问的详情页数量（同一详情页多次访问会重复计数）。
  - Objectivity: 该指标来自系统交互日志，是对实际信息搜索行为的客观计数，不依赖自我报告。
  - Outcome: Decision time (secondary)
  - Measurement: 从概览页呈递给参与者到参与者做出选择所经过的时间（秒），分析时通常取自然对数。
  - Objectivity: 该指标由系统时间戳客观记录，是决策过程的行为测量，不依赖主观报告。

## Peer Effects in Competitive Environments: Field Experiments on Information Provision and Interventions

- Year/journal: 2021 / MIS Quarterly
- DOI: 10.25300/misq/2021/16085
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 研究者开发的Canvas LMS插件/计算机程序会自动读取系统日志、计算同伴行为描述性信息，并向学生发送包含同伴信息的提醒消息；该干预明确以减少拖延（StartTime）和提高作业成绩（Grade）为目标，并通过随机现场实验评估其效果。
- Decision: 两条纳入路径均成立：一是干预明确设计用于改善客观行为和绩效（减少拖延、提高成绩）；二是核心因变量StartTime和Grade均基于系统日志和LMS记录进行客观测量，不依赖自我报告。
- Confidence: 0.98

  - Outcome: StartTime (procrastination behavior) (primary)
  - Measurement: 通过Canvas系统日志记录学生下载作业数据文件的时间，计算从开始作业到作业截止之间的小时数；数值越大表示开始越早、拖延越少。
  - Objectivity: 基于系统日志中的客观时间戳和可观察的下载行为，而非学生自我报告。
  - Outcome: Grade (assignment performance) (primary)
  - Measurement: 从Canvas获取学生在作业中获得的分数，并按作业总学分归一化为0-100的百分制成绩。
  - Objectivity: 成绩由教师/系统根据作业提交内容评定并记录在学习管理系统中，属于可验证的客观绩效结果，而非学生自我报告。

## Real-Effort Incentives in Online Labor Markets: Punishments and Rewards for Individuals and Groups

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2023/15166
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 研究所测试的软件/信息系统设计是实验系统（oTree）中实现的奖励与惩罚干预机制（调整收益乘数 ai），其明确设计目标是通过外部激励提高参与者的真实投入（标签数量）和输出质量（相似度）；文章使用系统日志客观测量标签数，直接评估干预对实际行为的影响。
- Decision: 该研究以在线劳动市场中可外部实施的奖励/惩罚机制为实验干预，核心因变量为系统记录的标签数量（实际投入）和基于 Google Vision API 与 GloVe 计算的相似度得分（输出质量），均属于不依赖自我报告的客观行为与结果测量；同时干预本身被明确设计用于提升真实投入和输出，因此两条纳入路径均成立。
- Confidence: 0.98

  - Outcome: Effort (tag count) (primary)
  - Measurement: 通过系统记录每位参与者每轮为图像输入的标签数量（单词数）来衡量工作投入；所有标签均由 oTree 平台自动记录。
  - Objectivity: 该测量基于实际行为的系统日志（输入的标签数量），不依赖参与者自我报告、态度或感知，可直接计数，属于客观行为测量。
  - Outcome: Tagging quality (similarity score) (secondary)
  - Measurement: 将个人或小组标签列表的 GloVe 词向量平均后，与 Google Cloud Vision API 为该图生成的标签向量计算余弦相似度，得到相似度得分（0-1）。
  - Objectivity: 该得分由预训练词向量和固定外部基准（Google Cloud Vision API 标签）自动计算，不依赖参与者自我报告或研究者主观评分，是可复现的客观算法度量。

## Retargeted vs. Generic Product Recommendations: When is it Valuable to Present Retargeted Recommendations?

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2020.0560
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 研究将网站上FP页面是否显示四个推荐产品（处理组显示、对照组隐藏）作为核心设计操纵，并将推荐区分为重定向（先前浏览过）与通用（未浏览过）两类；所有关键结局（曝光、点击/转化、销售）都直接度量该软件设计变更对实际购物行为的影响，且反事实模拟表明按购买漏斗阶段替换推荐类型可带来最高3.19%的销售提升。
- Decision: 两条纳入路径均满足：一是研究明确以提升推荐产品及总产品销售额为设计目标，并给出具体推荐替换策略；二是核心结局（RP销售额、RP曝光数、点击率/转化率、FP+RP销售额、在线实验购买）均基于系统日志和交易记录等客观行为数据测量，而非自我报告。
- Confidence: 0.98

  - Outcome: RP sales (daily recommended-product sales) (primary)
  - Measurement: 基于零售商网站交易日志，按推荐产品、日、实验条件和购买漏斗阶段汇总销售额；比较处理组（显示推荐）与对照组（隐藏推荐）的差异，并配合回归模型估计。
  - Objectivity: 购买记录来自实际交易系统，是可观察的行为结果，不依赖参与者自我报告。
  - Outcome: Number of RP impressions (daily recommended-product impressions) (primary)
  - Measurement: 由网站日志中FP页面浏览量产生每次四个RP曝光，按RP、日、实验条件和漏斗阶段计算曝光数；对照组也按隐藏RP构造曝光。
  - Objectivity: 页面曝光由服务器日志客观记录，属于系统行为数据而非自报。
  - Outcome: RP conversion rates: click-through rate (RPView | Impression), conditional conversion rate (RPPur | RPView), conversion rate (RPPur | Impression) (primary)
  - Measurement: 根据网站日志中的曝光、点击和购买行为计算：曝光后点击概率、点击后购买概率、以及曝光后购买概率；使用Logit模型和固定效应估计。
  - Objectivity: 点击、浏览和购买行为均来自客观日志记录，而非参与者的主观报告或感知。
  - Outcome: Total FP + RP sales (total focal and recommended product sales) (secondary)
  - Measurement: 汇总FP及其推荐产品的合并销售额（实际交易记录），分别估计对FP+RP转化率、每日FP曝光量和每日FP+RP销售额的影响。
  - Objectivity: 合并销售额来自交易数据，反映了实际购买行为，而非态度或意图。
  - Outcome: Online experiment product purchase and RP sales (primary)
  - Measurement: 在Amazon MTurk上搭建实验网站，参与者可真实购买商品；记录第二阶段的购买行为，比较纯重定向推荐与通用推荐在早期/晚期漏斗阶段的RP购买概率和销售额。
  - Objectivity: 购买行为在实验网站上被系统记录，且实验设计了激励对齐机制，使购买具有真实经济后果，不是问卷自报。

## Roles of Feedback and Phishing Characteristics in Antiphishing Training Performance: Perspectives of Goal Setting and Skill Acquisition

- Year/journal: 2024 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00854
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 研究操纵了反钓鱼培训中的反馈材料（例如基于示例的反馈与正念反馈、反馈数量），并在随后的钓鱼邮件测验中客观测量参与者的检测准确率和决策回避，以评估这些反馈设计对培训绩效的影响。
- Decision: 纳入两个路径：其一，反馈设计明确以提升反钓鱼检测准确率和减少决策回避为目标；其二，核心因变量检测准确率和决策回避均基于有客观正确标准的测验行为编码，属于客观测量结果，而非自我报告。
- Confidence: 0.98

  - Outcome: Detection accuracy (primary)
  - Measurement: 在钓鱼邮件测验中，参与者对每封邮件判断为钓鱼邮件、合法邮件或跳过/不知道；编码为正确=1，跳过/不知道=0，错误=-1，并汇总或按消息层级分析。
  - Objectivity: 以事先设计好的邮件真实类别（钓鱼/合法）为判分标准，属于有客观正确答案的任务绩效，而非参与者自我报告。
  - Outcome: Decision avoidance (primary)
  - Measurement: 在钓鱼邮件测验中，参与者选择“跳过”或“我不知道是否为钓鱼邮件”记为1，做出判断（钓鱼或合法）记为0。
  - Objectivity: 该变量直接来自参与者在测验中的实际选择行为，而非主观态度或意图问卷，是可以观察和编码的行为结果。

## Seeker Exemplars and Quantitative Ideation Outcomes in Crowdsourcing Contests

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2021.1054
- Objective design target: False
- Objectively measured outcome: True
- Artifact-outcome link: 实验使用的自建在线竞赛平台集成了Getty Images搜索、图像短名单和提交功能，并通过系统日志记录扫描、短名单和提交数量；这些平台记录的行为计数构成了本研究的客观结果测量。干预本身是项目简报中是否展示以及展示何种寻求者范例，而非软件功能的设计变更。
- Decision: 研究的核心因变量是解题者在竞赛平台中实际扫描、短名单和提交的图像数量，均由系统日志客观记录，属于可观察的行为结果，因此满足“客观测量结果”路径。研究并非为改进某客观结果而设计软件工件，因此“客观设计目标”路径不适用。
- Confidence: 0.98

  - Outcome: Scan (number of distinct images scanned) (primary)
  - Measurement: 通过实验平台集成的 Getty Images 搜索接口，记录每位解题者在所有概念搜索中出现的去重图像数量；每次搜索返回最多30张图像，滚动“Show More”可加载更多，系统记录所见的图像。
  - Objectivity: 该结果直接来自平台系统日志中的实际搜索行为计数，而非参与者的自我报告。
  - Outcome: Shortlist (number of images shortlisted) (primary)
  - Measurement: 实验平台记录每位解题者在扫描过程中点击“shortlist”操作所保存的图像数量。
  - Objectivity: 该结果由平台系统自动记录的实际短名单操作计数构成，不依赖自我报告。
  - Outcome: Select (number of images submitted) (primary)
  - Measurement: 实验平台记录每位解题者从短名单中最终选择并提交的图像数量，上限为15张。
  - Objectivity: 提交数量是平台系统记录的实际行为结果，而非参与者自报的意图或感知。

## The Decoy Effect and Recommendation Systems

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1197
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 该软件工件是带有推荐系统的电影推荐平台，设计干预是在推荐列表中加入诱饵项（decoy）：与目标项同类型、低预测分或低平均评分、置于列表第二位。该设计特征被明确用于影响用户对目标项和“不选择”选项的实际需求，即改变推荐接受的行为结果，并在个性化和非个性化两种情境下产生相反效应。
- Decision: 两条纳入路径均满足：一是软件设计明确以改变用户实际选择行为（目标项需求、不选择概率）为目标；二是核心结果变量为实验平台记录的真实选择行为（是否选择目标项、是否选择不选择选项），并非自我报告。主观感知指标仅作为机制解释，不影响客观结果的判定。
- Confidence: 0.98

  - Outcome: Target item selection likelihood (primary)
  - Measurement: 在每种实验条件下，用户在平台提供的五个推荐电影外加一个“不选择”选项中做出实际选择；目标项为列表中第一部电影。以用户是否选择该目标电影作为二元因变量，采用固定效应logit模型分析。
  - Objectivity: 该结果是用户在实验平台上实际点击/选择行为的记录，而非自我报告的感知或意图，属于可观察的客观行为结果。
  - Outcome: No-choice (outside option) selection likelihood (primary)
  - Measurement: 用户在每次条件中可以选择不选任何推荐电影（no-choice/outside option）；以用户是否选择该选项作为二元因变量，采用固定效应logit模型分析。
  - Objectivity: 该结果直接来自用户在实验界面中的实际选择行为记录，不是问卷调查或主观评分，因此是客观行为度量。

## The Effect of Risk Representation Using Colors and Symbols in Business Process Models on Operational Risk Management Performance

- Year/journal: 2021 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00676
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 软件/设计变更体现为BPMN流程模型中风险和内部控制信息的表示方式（基线模型、彩色标注模型、符号标注模型）。客观结果（风险理解、控制理解、控制改进）正是该表示设计变更旨在提升的任务绩效；实验结果显示，彩色处理显著提高了这三项客观绩效，而符号处理未显著提高。
- Decision: 纳入路径1和路径2均成立：论文明确假设表示格式（颜色/符号）能改善风险理解、控制理解和控制改进，这些是明确的设计目标；同时，风险理解和控制理解采用有唯一正确答案的客观计分题，控制改进采用显式编码规则的独立评分，均属于客观测量的实质性结果。
- Confidence: 0.98

  - Outcome: Risk understanding (primary)
  - Measurement: 以0-5分绩效指数计分，包含五个关于BPMN模型中风险要素的开放式问题（如风险数量、损失金额、风险概率、最高总预期损失），每题只有一个正确答案。
  - Objectivity: 测量基于有明确正确答案的任务表现，而非自我报告；文中明确说明“exactly one correct answer exists”。
  - Outcome: Control understanding (primary)
  - Measurement: 以0-5分绩效指数计分，包含五个关于BPMN模型中控制要素及剩余风险的开放式问题（如控制成本、风险降低百分比、剩余总预期损失），每题只有一个正确答案。
  - Objectivity: 测量基于有明确正确答案的任务表现，而非自我报告；文中明确说明“the measure is objective, as exactly one correct answer exists”。
  - Outcome: Control improvement (primary)
  - Measurement: 参与者写出最多五个降低风险的想法；编码方案规定：适合减少特定流程环节风险的想法得1分，不够具体但适合减少风险的想法得0.5分，不适合减少风险的想法得0分；两名研究者独立编码，一致性为85.81%，分歧经讨论解决。
  - Objectivity: 虽涉及对开放性回答的评判，但采用预先定义的显式编码规则和独立双人编码，并非仅依赖参与者自我报告；该规则为可复现的行为标准。

## The Effectiveness of Social Norms in Fighting Fake News on Social Media

- Year/journal: 2021 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2021.1870389
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 实验将两种社会规范消息作为社交媒体验证性设计的界面元素：指令性规范以新闻推送顶部文本形式呈现（“举报不当内容对所有人都很重要”），描述性规范以帖子上显示“已有多少用户举报此帖”的形式呈现。该设计明确旨在提高用户对假新闻的举报行为，而核心因变量正是用户的实际举报点击行为。
- Decision: 研究通过两个在线实验检验社会规范消息对用户举报假新闻行为的影响。核心因变量为用户在模拟新闻推送中实际点击“报告”按钮的次数，属于客观行为测量，而非自我报告；同时，研究将社会规范消息作为社会媒体用户界面的设计特征，明确以改善假新闻举报行为为目标。因此，两条纳入路径均成立。
- Confidence: 0.98

  - Outcome: Amount of reported fake news (number of fake news posts reported) (primary)
  - Measurement: 在自然交互阶段，参与者面对包含15条帖子的模拟新闻推送（5条假新闻、5条真新闻、5条中性帖子），使用简化版“报告”按钮报告帖子；系统记录每位参与者实际点击报告假新闻帖子的数量。采用有序逻辑回归分析各实验组之间的差异。
  - Objectivity: 该结果来自实验系统中实际点击行为的记录，而非参与者自报的意愿、态度或感知。报告行为是可观察、可验证的操作行为。
  - Outcome: Amount of reported real news (number of real news posts incorrectly reported as fake) (secondary)
  - Measurement: 与假新闻举报数量相同，系统记录每位参与者实际点击报告真实新闻帖子的数量，用于评估社交规范信息是否导致误导性举报（将真实新闻误报为假新闻）的副作用。
  - Objectivity: 同样基于实验系统对实际点击行为的记录，而非自我报告。

## The Fog of Warnings: How Non-Security-Related Notifications Diminish the Efficacy of Security Warnings

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2025/18531
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 本文的干预措施是改变安全警告的视觉外观（Experiment 1）或交互方式（Experiment 2和3中的滑块/拖拽与按钮对比），使警告区别于常见的非安全通知；这些设计变化被明确用来减少习惯化泛化、降低警告忽略率并增加对警告的注意，直接关联到可客观测量的警告忽略行为、反应时间和神经激活。
- Decision: 两条纳入路径均满足：研究明确将减少安全警告忽略/提高警告遵从作为设计目标，且通过视觉和交互方式的软件设计干预来实现；同时，主要结局（警告忽略行为、反应时间、fMRI BOLD神经激活）均为客观测量，不依赖自我报告。因此客观结局匹配成立。
- Confidence: 0.98

  - Outcome: Security warning disregard (primary)
  - Measurement: 在浏览器实验任务中，记录参与者是否点击安全警告中较不安全的选项（例如对权限请求选择“Don’t allow”，对扩展安装警告选择“Cancel”）作为二值变量；比较警告在暴露位置1与暴露15或30时被忽略的比率。
  - Objectivity: 该指标是参与者在真实浏览器界面中的实际选择行为，由系统记录，而非自我报告。
  - Outcome: Reaction time (primary)
  - Measurement: 从通知或安全警告显示到参与者做出响应之间的时间（秒），基于浏览器或psiTurk记录的时间戳测量；分析时取自然对数。
  - Objectivity: 反应时间来自系统日志和客观时间戳，不依赖参与者的主观报告。
  - Outcome: fMRI BOLD neural activation in the ventral visual stream (primary)
  - Measurement: 在功能磁共振成像实验中测量血氧水平依赖（BOLD）信号，比较对重复性能通知、不同交互方式的安全警告以及新异刺激的腹侧视觉通路神经激活水平。
  - Objectivity: 这是客观的神经生理测量，直接反映脑部血氧信号变化，而非自我报告或主观评分。

## Will Humans-in-the-Loop Become Borgs? Merits and Pitfalls of Working with AI

- Year/journal: 2021 / MIS Quarterly
- DOI: 10.25300/misq/2021/16553
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: AI建议界面（固定建议、AI确定性显示、个性化建议）通过改变受试者的分类选择，直接影响客观分类正确率、唯一人类知识，并通过模拟影响群体智慧正确率；个性化建议被明确设计为在保持个体准确率的同时减少UHK损失并改善群体绩效。
- Decision: 两条纳入路径均成立：AI建议、确定性显示和个性化建议被明确设定为提升个体准确率、维持/增加唯一人类知识以及改善群体智慧绩效的设计目标；同时这些核心结果均基于ImageNet真实标签、AI输出和客观分类选择计算，属于客观测量而非自我报告。
- Confidence: 0.98

  - Outcome: Human accuracy (image classification accuracy) (primary)
  - Measurement: 受试者在100张ImageNet图片分类任务中正确分类的图片数除以总图片数，以官方类别标签为客观正确标准。
  - Objectivity: 正确性由ImageNet真实标签判定，不依赖自我报告。
  - Outcome: Unique human knowledge (UHK) (primary)
  - Measurement: 定义为AI分类错误而人类分类正确的图片数除以总图片数，基于同一组100张图片的客观正确标签和AI输出。
  - Objectivity: 基于AI与人类分类结果的客观比对（正确/错误），不依赖自我报告。
  - Outcome: Wisdom of crowds group accuracy (secondary)
  - Measurement: 通过蒙特卡洛模拟，从实验处理人群中随机抽取组员，以众数作为群体选择，与真实标签比较计算群体正确率；模拟1,000次迭代，群体规模1-15及99-100。
  - Objectivity: 群体选择由实验期间的客观分类选择聚合而成，并以ImageNet真实标签判定正确性，不依赖自我报告。
  - Outcome: Benefit of correct advice and harm of incorrect advice (secondary)
  - Measurement: 在前后测设计中，测量受试者在接受AI建议前后的分类正确性；收益=先前错误且建议后正确的图片数占正确AI建议图片数比例；损害=先前正确且建议后错误的图片数占错误AI建议图片数比例。
  - Objectivity: 基于前后分类的客观正确性与AI输出计算，非自我报告。

## Achieving a Balance Between Privacy Protection and Data Collection: A Field Experimental Examination of a Theory-Driven Information Technology Solution

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2021.1045
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 本文提出的软件工件是三种移动银行隐私政策应用，重点是带协商与主动推荐功能的 App 3。该应用通过服务代理主动向不同隐私偏好的消费者推荐个性化隐私政策，并允许双向协商，明确以降低隐私担忧、提高披露意愿和实际信息披露行为为设计目标。实际信息披露行为（披露数量、披露敏感度加权值及比值）是在实验应用中被系统记录的真实选择行为，直接用于检验 App 3 相对基准应用的效果。
- Decision: 两条纳入路径均成立：(1) 设计目标明确包括增加消费者的实际信息披露行为和数据收集，属于客观行为目标；(2) 研究至少有一个核心因变量——实际信息披露行为——通过实验系统记录的实际披露条目和敏感度加权来计算，不依赖自我报告。因此 objective_outcome_match 为 true。
- Confidence: 0.97

  - Outcome: Actual information disclosure behavior (disclosure behavior ratio) (primary)
  - Measurement: 以被试在实验应用（Session 3）中实际同意隐私政策或协商成功后所披露的个人信息为基础计算：披露行为 = 已披露信息项的敏感度评分之和 / 所请求的所有信息项的敏感度评分之和；备择操作化包括披露信息数量和披露信息敏感度总分。数据由系统记录被试实际选择/填写的披露内容获得。
  - Objectivity: 该结果基于被试在实验界面中的真实披露选择与所填写信息，而非自我报告的感知、态度或意图，属于可观察的实际行为数据。
  - Outcome: Quantity of disclosed information (secondary)
  - Measurement: 统计每个被试在实验应用披露流程中实际提供的信息条目数量，由实验系统记录。
  - Objectivity: 这是系统记录的实际披露行为计数，而非自我报告。
  - Outcome: Sensitivity score of disclosed information (secondary)
  - Measurement: 以被试在实验前对12项个人信息敏感度评分为权重，对被试实际披露的信息项进行加权求和，得到披露信息的敏感度总分。
  - Objectivity: 虽然敏感度评分本身是被试的主观评分，但该结果衡量的是被试实际披露了哪些信息以及披露量，是实验系统记录的真实披露行为，并非直接询问披露意愿或感知。

## Behaviorally Measuring Usability by Analyzing Users’ Mouse Movement Efficiency

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2023/17900
- Objective design target: False
- Objectively measured outcome: True
- Artifact-outcome link: 本文的软件工件是嵌入网页的JavaScript鼠标追踪脚本和相应的MME计算服务；该工件直接生成NAUC、NAD、MD等客观鼠标行为指标，并在四个研究中验证这些指标能够作为可用性的行为度量。因此，客观测量结果正是该工件输出的核心内容。
- Decision: 虽然本文的软件工件是测量工具而非改善客观状态的干预，但路线2成立：核心因变量MME（NAUC、NAD、MD及组合行为可用性分数）均由鼠标移动日志和几何算法客观测量，不依赖自我报告；眼动注视率也是客观传感器数据。文章以此作为评估系统可用性的行为代理指标，满足‘客观测量实质结果’的条件。
- Confidence: 0.97

  - Outcome: Normalized Area Under the Curve (NAUC) (primary)
  - Measurement: 通过JavaScript鼠标追踪脚本记录用户鼠标轨迹的x/y坐标，计算实际轨迹与个性化理想响应轨迹（IRT）之间的几何面积，再除以IRT线段总距离进行归一化；数值越大表示鼠标移动效率越低。
  - Objectivity: 该指标完全基于系统日志记录的鼠标移动坐标和几何计算，不依赖用户自我报告、主观评分或人工编码。
  - Outcome: Normalized Additional Distance (NAD) (primary)
  - Measurement: 用实际鼠标轨迹总距离减去IRT各线段所需最小距离，再除以IRT总距离进行归一化；数值越大表示额外移动距离越多、鼠标移动效率越低。
  - Objectivity: 该指标由鼠标坐标轨迹的欧氏距离计算得出，属于客观行为日志数据，不涉及用户自我报告。
  - Outcome: Maximum Deviation (MD) (primary)
  - Measurement: 计算实际鼠标轨迹与IRT之间最大的垂直偏离距离，通过直线方程和截点距离公式得出；数值越大表示偏离理想路径越远、鼠标移动效率越低。
  - Objectivity: 该指标是从鼠标轨迹坐标与几何计算中自动提取，属于客观行为测量。
  - Outcome: Behavioral usability composite score (Study 4) (primary)
  - Measurement: 将六种鼠标移动效率指标（NAUC、NAD、MD、鼠标移动时间、x/y轴方向切换次数、移动速度）通过线性回归模型（以感知可用性为因变量，AIC反向选择）组合成一个单一的行为可用性分数。
  - Objectivity: 该综合分数完全由鼠标行为日志指标经统计模型生成，是客观行为数据的衍生物，不依赖参与者自我报告。
  - Outcome: Eye gaze fixation rate (Study 1) (secondary)
  - Measurement: 使用Tobii Pro X2-60眼动仪以60Hz采集眼动数据，采用I-VT算法识别注视点，计算每秒注视次数（fixation rate）作为视觉搜索和注意干扰的指标。
  - Objectivity: 该指标来自眼动仪传感器记录的客观生理/行为数据，而非自我报告。

## Effects of Idea Set Partitioning on Selection Quality: An Exploratory Eye-Tracking Study of Information Processing

- Year/journal: 2025 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00958
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 研究的设计变更/软件工件是创意选择界面的分区方式：将32个创意分为每屏2个（小分区）或每屏4个（大分区）。该设计旨在通过改变信息加工策略和认知努力来影响选择质量（新颖性和可行性）。最终结果显示分区通过线索间加工和认知努力的序列中介影响了所选创意的新颖性（正向）和可行性（负向）。
- Decision: 两条路径均成立：(1) 客观设计目标：研究明确假设更大的创意子集（较少分区）会提高选择质量（H1），即提高所选创意的新颖性和可行性，这是核心设计目标。(2) 客观测量结果：选择质量基于系统客观记录的实际选择行为，并以多名领域专家的评分作为创意质量的客观基准进行计算；中介变量信息加工策略和认知努力也分别通过眼动注视转换和瞳孔扩张等客观生理/行为指标测量。因此至少存在一个实质性的客观结果。
- Confidence: 0.97

  - Outcome: Selected ideas' novelty (primary)
  - Measurement: 每位参与者在平台上实际选择的创意（系统日志追踪），将每个被选创意赋予由10位HR专家评定的平均新颖性得分（1-5分，经均值中心化，ICC=0.605），再对参与者所选创意的专家新颖性得分求平均。
  - Objectivity: 选择行为由平台客观记录，创意质量基于专家评分作为标准化的客观质量基准，而非参与者自我报告。
  - Outcome: Selected ideas' feasibility (primary)
  - Measurement: 每位参与者在平台上实际选择的创意，将每个被选创意赋予由10位HR专家评定的平均可行性得分（1-5分，经均值中心化，ICC=0.631），再对参与者所选创意的专家可行性得分求平均。
  - Objectivity: 选择行为由平台客观记录，创意质量基于专家评分的客观基准，而非参与者自我报告。
  - Outcome: Information processing strategy (strategy index) (secondary)
  - Measurement: 通过眼动追踪记录注视转换，按屏幕计算策略指数 = (选项内转换数 - 线索间转换数) / (选项内转换数 + 线索间转换数)，取值-1到+1，负值表示更多线索间（cue-wise）加工，正值表示更多选项内（option-wise）加工。
  - Objectivity: 基于眼动仪客观记录的注视行为计算，属于生理/行为测量，不依赖自我报告。
  - Outcome: Cognitive effort (pupil dilation) (secondary)
  - Measurement: 通过眼动追踪记录瞳孔直径变化，使用CEP-Web工具清理数据，用任务前最后一个介绍屏幕的瞳孔均值作为基线，计算整个选择任务期间的平均瞳孔扩张差值。
  - Objectivity: 基于眼动仪客观记录的瞳孔扩张生理信号，属于客观神经生理测量，而非自我报告。

## Expl(AI)ned: The Impact of Explainable Artificial Intelligence on Users’ Information Processing

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2023.1199
- Objective design target: False
- Objectively measured outcome: True
- Artifact-outcome link: 软件工件为叠加在预测之上的特征级XAI解释（LIME/SHAP）。研究比较了无辅助、仅不透明预测、预测加解释三种条件，发现解释改变了实际投资决策、决策准确性、挂牌价估计等可观察行为结果，并导致精神模型调整和跨域溢出效应。
- Decision: 虽然该研究的主要理论焦点是认知过程（信息处理和精神模型），但至少一个核心变量是通过客观行为表现测量的：投资决策准确性、召回率、实际投资选择和挂牌价估计均来自可观察行为或与客观基准的比较，而非仅依赖自我报告。因此满足客观测量结果路径。
- Confidence: 0.97

  - Outcome: Investment decision accuracy (share of payoff-maximizing decisions) (primary)
  - Measurement: 在实验每一阶段，将参与者的实际投资决策（投资/不投资）与预先从实地研究中获得的借款人真实还款行为进行比较，计算做出收益最大化决策的份额。
  - Objectivity: 该指标基于参与者的真实行为选择与客观基准（借款人既定的还款结果）比较，而非自我报告或主观评分。
  - Outcome: Recall (share of investments with repaying borrowers) (primary)
  - Measurement: 统计参与者投资的借款人中实际还款的比例，依据预先确定的借款人还款结果计算。
  - Objectivity: 基于实际投资行为和客观还款结果，不依赖参与者自我报告。
  - Outcome: Actual investment decisions and derived trait weighting (primary)
  - Measurement: 记录参与者在每个试次中是否投资给特定借款人的二元选择，并通过回归模型估计各借款人特征对投资概率的权重变化。
  - Objectivity: 投资决策是实验中的实际行为结果，权重变化由这些行为数据回归得出，而非自我报告的态度或意图。
  - Outcome: Listing price estimates (Study 2, including spillover prices for Chemnitz) (secondary)
  - Measurement: 专家参与者输入公寓每平方米挂牌价的欧元数值，包括实验各阶段的估计以及最后对开姆尼茨公寓的估计；这些数值被直接记录并比较分布。
  - Objectivity: 挂牌价估计是可观察的实际数值输出和行为结果，不是问卷中的主观感知或态度量表。
  - Outcome: Accuracy of listing price estimates (absolute deviation from actual prices) (secondary)
  - Measurement: 将专家估计的挂牌价与实际挂牌价的绝对偏差作为预测准确性指标。
  - Objectivity: 实际挂牌价来自在线平台数据，偏差计算基于客观数值。

## Human Behavior Mining: A Framework for Theorizing About mHealth Behavior Using Digital Trace Data

- Year/journal: 2025 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00938
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 论文中的软件制品是研究者自行开发的SCT导向mHealth应用，其设计目标是通过自我监控、反馈、目标调整、社会比较和社会支持等功能支持个体增加身体活动。该应用生成的使用行为日志与身体活动追踪数据正是HBM分析中的中心客观结果变量，用于检验SCT提出的动态交互与互惠关系。
- Decision: 至少一条纳入路径成立：(1) 客观设计目标成立——应用明确以促进身体活动这一客观健康行为为目标；(2) 客观测量结果成立——中心因变量（身体活动行为和app功能使用行为）均来自数字痕迹/系统日志和传感器客观记录，而非自我报告。因此整体 objective_outcome_match 为 true。
- Confidence: 0.97

  - Outcome: Physical activity behavior (perform physical activity) (primary)
  - Measurement: 通过自研mHealth应用与Apple Health/Google Fit的集成客观追踪用户的身体活动，记录“perform physical activity”行为事件（含开始/结束时间戳），作为情境行为纳入行为事件日志；最终日志包含1,142条身体活动踪迹（Section 5.1, 5.2.1）。
  - Objectivity: 数据来自系统/传感器自动记录的数字痕迹，而非被试自我报告的问卷或主观感知；身体活动由原生健康应用客观追踪。
  - Outcome: mHealth app feature usage behavior (self-monitoring/Add activity, feedback/Check progress, goal adjustment/Set new goals, social comparison/Query leaderboard, social support/Access social feed) (primary)
  - Measurement: 通过应用内部日志（internal app logging）记录每次用户与功能交互的时间戳事件，并映射为六个行为活动之一；例如“add activity”“check progress”“set new goals”“query leaderboard”“access social feed”均作为使用行为事件纳入日志（Section 5.1, 5.2.1, Table 4/5）。
  - Objectivity: 交互行为由系统日志自动捕获，属于实际使用行为，而非自报使用频率或感知；日志直接记录用户操作的客观痕迹。

## It's not just about accuracy: An investigation of the human factors in users' reliance on anti-phishing tools

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113846
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 该研究的反钓鱼工具原型通过邮件标记（红色警告表示钓鱼、绿色勾选表示合法）向用户提供预测；实验操纵了工具的准确性、频率和透明性，而这些设计特征的核心目标是提升用户对工具预测的依赖行为，从而减少钓鱼攻击造成的安全危害。用户依赖是本研究的首要结果变量，直接反映用户是否按照工具的设计意图采取行动。
- Decision: 两条路线均通过：首先，反钓鱼工具的设计和操纵（准确性、频率、透明度）明确以改善用户的安全相关行为（依赖工具预测）为目标；其次，核心因变量“依赖”是通过参与者在实验邮箱系统中的实际选择行为客观计算得出的，而非依赖自我报告，因此属于客观测量的实质性结果。
- Confidence: 0.97

  - Outcome: User reliance on anti-phishing tool predictions (primary)
  - Measurement: 通过计算参与者对20封实验邮件的分类选择与工具预测（红色警告/绿色勾选）一致的比例来衡量；该行为在模拟Gmail界面的实验邮箱系统中被记录。Study 1和Study 2均使用此客观行为指标，报告为平均值约91.86%-91.92%。
  - Objectivity: 该指标来源于参与者在实验任务中的实际选择行为，而非自我报告的态度或意图；文章明确称其为“observed measure”和“observed from users’ actual behaviors”。

## Skipping class: improving human-driven data exploration and querying through instances

- Year/journal: 2022 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2020.1869507
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 本文设计的实例化数据表示（instance-based representation）是核心软件/数据呈现工件，研究明确以改善内容消费者在数据探索和查询中的实际表现（识别正确模式、查询公式准确性、任务完成时间）为目标，并通过两个实验测量这些客观绩效结果。
- Decision: 两条路径均满足：一，研究明确以实例化表示提升用户数据探索和查询绩效为设计目标；二，实验一中的正确模式数和精确度以数据源为真值客观判定，实验二中的查询公式准确性依据明确答案要点和评分规则进行编码评分，且任务完成时间为客观记录。因此 objective_outcome_match=true。
- Confidence: 0.97

  - Outcome: Number of true patterns identified (primary)
  - Measurement: 参与者报告的数据模式由研究助理对照实际数据源逐条判定真伪，统计每人识别出的真实陈述数量；作者复核分歧并以数据统计为最终依据。
  - Objectivity: 以实际数据为客观真值进行验证，不依赖参与者自我报告或主观感受。
  - Outcome: Precision of identified patterns (primary)
  - Measurement: 统计每组所有报告陈述中真实陈述所占比例，即真实陈述数除以总陈述数。
  - Objectivity: 该比例基于客观判定的真实陈述计数，属于可验证的客观绩效指标。
  - Outcome: Query formulation accuracy (Experiment II) (primary)
  - Measurement: 参与者用自然语言描述完成数据检索任务的步骤；两名编码者依据预先制定的答案要点和0、0.25、0.5、0.75、1的评分规则对回答正确性打分，每个域满分4分。
  - Objectivity: 评分依据明确的答案要点和逐步评分标准，具有可验证的正确性基准（answer key），而非无约束的主观评价；两位编码者间ICC为83%和87%。
  - Outcome: Task completion time (secondary)
  - Measurement: 记录参与者完成实验任务所用的时间，实验一和实验二均报告了平均完成时间。
  - Objectivity: 时间由实验过程客观记录，不依赖参与者自我报告。

## Standardize or Let a Thousand Flowers Bloom? Interface Design Coordination between Software Platforms and Hosted Apps

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/16484
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 研究操纵了App的界面相似性、嵌入性和同步性三种界面设计属性，旨在增强用户对平台与App的分组感知，进而促进平台到App的正向衍生使用（实际App使用）和App到平台的反向衍生使用。客观结果变量为App实际使用频率和时长，直接来源于后台日志，用于检验设计操纵通过分组感知对实际使用行为的影响。
- Decision: 路线1成立：界面设计操纵（相似性、嵌入性、同步性）明确以提升衍生使用行为为目标，包括实际的App使用行为。路线2成立：至少一个核心结果变量——App使用频率和时长——通过后台登录日志客观测量，而非自我报告。因此，objective_outcome_match=true。
- Confidence: 0.97

  - Outcome: App usage (frequency and duration) (primary)
  - Measurement: 在第二阶段（两周内），通过研究团队自行开发的玩笑类App的后台登录日志，自动记录每位参与者的使用频率和使用时长，并据此计算App使用强度。
  - Objectivity: 该指标来自系统日志实际记录的行为数据，而非参与者的自我报告或主观感知，因此是客观测量。

## The Impact of Animated Banner Ads on Online Consumers:  A Feature-Level Analysis Using Eye Tracking

- Year/journal: 2021 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00659
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 研究的软件/设计干预是带有运动、延迟出现和逼近等特征的动画横幅广告；这些设计特征被明确假设为能够吸引在线消费者的视觉注意（眼动注视次数和注视时长），并进而改善广告回忆。眼动数据直接客观地测量了设计特征对注意力的因果影响。
- Decision: 客观结果匹配：一方面，动画横幅广告的运动和逼近特征被明确设计并假设为增加消费者对广告的注意，注意捕捉本身是可观察的行为结果，满足客观设计目标路径；另一方面，核心因变量包括由眼动仪记录的注视次数和注视时长，属于客观生理/行为测量，且实验3的广告识别测试有明确正确答案，因此也满足客观测量路径。
- Confidence: 0.97

  - Outcome: Fixation count (total number of fixations on ads) (primary)
  - Measurement: 使用ASL 504眼动仪记录被试浏览网页时的注视点，并以100毫秒作为最小注视时长阈值，汇总为对广告区域的注视次数。
  - Objectivity: 眼动仪记录的是眼球运动的位置和时间，属于客观生理/行为指标，不依赖被试自我报告。
  - Outcome: Fixation time (total fixation time on ads) (primary)
  - Measurement: 使用同一眼动仪记录注视点，并汇总被试在广告区域内所有注视时长的总和。
  - Objectivity: 注视时长由设备直接测量，是客观的视觉注意力指标，而非主观评价。
  - Outcome: Credit card ad recall/recognition (Experiment 3) (secondary)
  - Measurement: 实验3中，被试在浏览后从五张虚拟信用卡中识别出实验中出现过的那张信用卡，答案与实验实际使用的卡片进行比对。
  - Objectivity: 该识别任务有明确正确答案（实验使用的信用卡），按是否选对进行客观计分，不是被试的主观感知或态度。

## The Role of Social Cues and Trust in Users’ Private Information Disclosure

- Year/journal: 2022 / MIS Quarterly
- DOI: 10.25300/misq/2022/16288
- Objective design target: False
- Objectively measured outcome: True
- Artifact-outcome link: 实验平台VideoBook对网站界面进行设计操纵：社交线索条件包含点赞、评分、评论等社交功能及他人活动提示，非社交条件不含这些元素。该设计变化通过社会感知间接影响参与者在网站内嵌表单中实际披露私人信息的行为；信任线索（高/低信任提示和故障）调节社交线索对社会感知的作用。
- Decision: 通过第二条路径：核心因变量——私人信息披露——并非自我报告态度，而是参与者在实验网站实际填写或拒绝填写敏感个人信息（邮编、出生日期、全名）的可观察行为，由系统记录作答与否。该行为性结果足以支持客观结果匹配。第一条设计目标路径不成立，因为研究并非旨在改进该客观结果，而是考察社交线索对其的影响。
- Confidence: 0.97

  - Outcome: Private information disclosure (willingness to disclose personal information) (primary)
  - Measurement: 在VideoBook网站内嵌的弹出式调查中，网站直接要求参与者填写年龄、性别、职业、城市、邮政编码、出生日期和全名；其中后五项自愿填写。披露分数被操作化为参与者实际填写的最后三项（邮政编码、出生日期、全名）的数量（0-3），系统仅记录是否作答，不记录回答内容。
  - Objectivity: 该指标基于参与者在网站表单中实际提交或拒绝提交个人信息的可观察行为，由系统记录，而非依赖参与者自我报告的态度、意图或感知；参与者被明确告知拒绝回答不会影响报酬，因此该行为反映了真实的披露选择。

## Why Do Data Analysts Take IT-Mediated Shortcuts? An Ego-Depletion Perspective

- Year/journal: 2022 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2022.2063558
- Objective design target: False
- Objectively measured outcome: True
- Artifact-outcome link: 实验材料是简单版与复杂版仪表盘（复杂度操纵：静态结构化数据 vs 动态结构化与非结构化数据）。复杂仪表盘通过提高自我耗竭，进而增加实际跳过图表的行为（IT介导捷径）；而跳过图表的行为又客观地与更低的决策正确率相关。
- Decision: 至少一个核心结果变量被客观测量：IT介导捷径被记为实际跳过的图表数（系统行为日志），任务表现被记为有客观正确答案的决策正确数。这两项均为实质性结果，且与所研究的IT制品（仪表盘复杂度）直接相关，因此满足客观测量路径。该研究并非旨在通过软件设计改进某一目标结果，而是检验复杂度的负面效应，因此objective_design_target未通过。
- Confidence: 0.97

  - Outcome: IT-mediated shortcuts (skipped charts) (primary)
  - Measurement: 在仪表盘任务中，参与者被明确要求逐一查看并展开所有图表以做出准确决策；系统在参与者不知情的情况下记录被跳过的图表数量（0到6），作为实际采取IT介导捷径的直接行为测量。
  - Objectivity: 该测量来自实验平台记录的实际行为（跳过的图表数），而非参与者的自我报告、感知或意图。
  - Outcome: Task performance (decision accuracy) (secondary)
  - Measurement: 参与者需要就可能的最佳产品、国家和渠道做出决策；由于每个决策维度都有正确答案，任务表现按正确答案的数量（正确决策数）进行客观评分。
  - Objectivity: 决策质量基于预先确定的客观正确答案进行编码和评分，而不是基于参与者的自我评价或研究者的主观印象。

## Designing Attentive Information Dashboards

- Year/journal: 2022 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00732
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 文章设计的是提供个体化视觉注意力反馈（VAF）的注意力信息仪表盘，基于实时眼动数据计算用户注意力分配并反馈给用户。实验比较了个体化 VAF 与一般 VAF 对用户在数据探索任务中眼动行为的影响，上述三个客观眼动指标直接用于评估该设计是否改善了用户的注意力管理。
- Decision: 该研究既满足客观设计目标路径，也满足客观测量路径。软件工件明确以改善用户的注意力分配、转移和管理为目标；同时主要因变量均为眼动仪记录的客观行为/生理传感器数据（注视时长、注视次数、转移次数、标准差），而非自我报告。
- Confidence: 0.96

  - Outcome: Attentional resource allocation (primary)
  - Measurement: 通过 Tobii 眼动仪实时记录用户在六个预定义兴趣区（AOI）上的注视时长和注视次数，计算每个 AOI 的注意力分配百分比，并与理论平均值（100/6=16.67%）比较，考察首次访问阶段与再次访问阶段的变化。
  - Objectivity: 数据来自眼动追踪设备自动记录的注视时长和注视次数，属于客观传感器测量，不依赖参与者的自我报告。
  - Outcome: Attention shift rate (primary)
  - Measurement: 通过眼动数据计算兴趣区之间的注视转移总次数（忽略同一 AOI 内的转移），以转移矩阵表示注视在不同 AOI 间的切换频率。
  - Objectivity: 由眼动追踪设备记录的注视点序列计算得出，是客观的行为测量，而非自我报告的注意力转移。
  - Outcome: Attentional resource management (primary)
  - Measurement: 在数据探索任务结束时，计算六个 AOI 注视时长和注视次数的标准差；标准差越低表示注意力在六个同等复杂度图表间分布越均匀，管理绩效越高。
  - Objectivity: 标准差由眼动追踪设备记录的注视数据计算得出，是客观的量化指标，不依赖主观评价。

## Rethinking Gamification Failure: A Model and Investigation of Gamified System Maladaptive Behaviors

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2021.0284
- Objective design target: False
- Objectively measured outcome: True
- Artifact-outcome link: Study 2构建了一个游戏化在线学习系统（GDPR合规培训模拟），通过三轮不同的游戏规则操纵（积分依据完成时间还是正确性、错误后显示正确答案、设置无法从材料回答的题目）来触发不同水平的GSMB，并使用客观的答题正确数、完成时间和搜索频率来检验GSMB对任务绩效的负面效应。这些设计操纵旨在诱发而非改善特定行为，但客观测量直接关联到该游戏化软件设计特征的评估。
- Decision: 虽然Study 1主要依赖问卷调查（主观测量），但Study 2对核心变量进行了客观测量：任务绩效通过标准答案计分，技术适应不良通过浏览器搜索记录测量，游戏化任务适应不良通过系统记录的完成时间测量。因此，至少一个实质性结果被客观测量，满足'objectively_measured_outcome'路线。不存在明确以改善客观结果为设计目标的软件设计变更，故'objective_design_target'不成立。
- Confidence: 0.96

  - Outcome: Task performance (number of correctly answered GDPR quiz questions) (primary)
  - Measurement: 在Study 2的实验中，通过统计参与者在每个回合中正确回答的题目数量来衡量任务绩效；只计入学习材料中有明确答案的题目，排除为诱导技术性适应不良而设计且无法从材料回答的题目。
  - Objectivity: 正确答题数基于客观的正确答案标准（学习材料中的内容），不是参与者的自我报告。
  - Outcome: Technology maladaptation (search frequency) (secondary)
  - Measurement: 通过记录参与者在计算机实验室活动期间的网页浏览历史，统计每个回合中在网上搜索答案的题目数量。
  - Objectivity: 该测量基于系统/浏览器日志中的客观行为记录，而非自我报告；研究者在实验中直接观察并记录了搜索行为。
  - Outcome: Gamified task maladaptation (completion time in seconds) (secondary)
  - Measurement: 通过系统记录参与者在每个回合中完成任务所花费的秒数来衡量；更快的完成时间被操作化为更明显的游戏化任务适应不良（例如为获取积分而快速作答而非认真学习）。
  - Objectivity: 完成时间来自系统自动记录的可观察行为数据，不依赖参与者的主观自我报告。

## The Attraction Effect in Crowdfunding

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1152
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 核心的数字设计干预是在数字奖励菜单中插入诱饵选项（价格诱饵或质量诱饵），其明确目标是使支持者更可能选择高价格目标奖励，从而影响实际购买/出资选择；实验和现场研究均以这一选择行为作为主要结果变量。
- Decision: 该研究明确将数字奖励菜单的设计（增加诱饵选项）作为影响选择行为的手段，并以支持者是否选择高价格目标奖励作为核心结果；该结果通过实验中的实际选择记录和真实Kickstarter支持者行为进行测量，属于客观行为结果而非自我报告。因此，客观设计目标和客观测量结果两条纳入路径均满足。
- Confidence: 0.96

  - Outcome: Choice of high-priced target reward (target vs. competitor) (primary)
  - Measurement: 在在线实验中，参与者在无诱饵、价格诱饵或质量诱饵三种奖励菜单条件下实际选择一项奖励；因变量为是否选择高价格目标奖励（相对于低价格竞争者奖励），使用逻辑回归模型估计选择概率。部分实验（如研究3、7、8）涉及真实经济后果。
  - Objectivity: 该结果基于参与者的实际选择行为记录（Qualtrics实验中的选择），而非自我报告的态度、感知或意图；在有经济后果的实验版本中，选择还与真实金钱支付挂钩。
  - Outcome: Real backer reward choice in Kickstarter field study (primary)
  - Measurement: 在与瑞士手表品牌合作的真实Kickstarter活动中，727名真实支持者在包含诱饵选项的奖励菜单中进行实际选择；记录选择竞争者（钥匙扣）、目标（手表+钥匙扣）或诱饵（仅手表）的比例，并使用多项逻辑回归和贝叶斯分析。
  - Objectivity: 这是真实平台上支持者的实际资金投入行为记录，具有真实经济后果，而非问卷调查或自我报告。

## <scp>Context‐aware</scp> user profiles to improve media synchronicity for individuals with severe motor disabilities

- Year/journal: 2022 / Information Systems Journal
- DOI: 10.1111/isj.12337
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 上下文感知用户画像作为AAC系统的设计特征，通过缩小选择空间、提供情境化短语/符号来提高信息传输速率；评估中直接对比了有/无画像条件下的实际任务完成时间和错误数，说明该软件设计特征与客观绩效结果直接相关。
- Decision: 两条路径均成立：设计需求DR1明确将提高传输速率作为客观性能目标；评估中采用系统计时的实际完成时间和可计数的交互错误作为客观测量指标。感知速度等自我报告指标不影响判定。
- Confidence: 0.95

  - Outcome: Task completion time (actual transmission rate) (primary)
  - Measurement: 系统记录每位参与者在有/无上下文感知用户画像条件下完成三项沟通任务（“I'm tired”“Adjust head to the middle”“Ears sore”）所需时间；报告平均完成时间改善率分别为26.14%、19.88%、60.33%。
  - Objectivity: 完成任务时间由系统/计时工具客观记录，而非参与者自我报告，属于可观察的任务绩效表现。
  - Outcome: Selection errors and overscan errors (secondary)
  - Measurement: 统计参与者在扫描式界面中选择过程中的两类错误：错误选择（selection errors）和错过扫描项（overscan errors）的数量。
  - Objectivity: 错误次数是从系统交互/可观察行为中计数得到的客观结果，不依赖自我报告。

## A probabilistic Bayesian inference model to investigate injury severity in automobile crashes

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113557
- Objective design target: False
- Objectively measured outcome: True
- Artifact-outcome link: 研究提出的贝叶斯网络模型及WebSimulator以受伤严重程度为预测/推断目标；评估指标直接衡量模型对客观事故严重等级的预测性能。
- Decision: 路线2通过：核心结果变量受伤严重程度来自NHTSA警方事故记录，属于客观档案数据，且通过10折交叉验证等客观指标测量。路线1不通过：文章未将软件工具或设计明确设定为改善某个客观行为或安全结果的目标，主要目标是理解和预测严重程度。
- Confidence: 0.95

  - Outcome: Injury severity (三分类：无伤害/轻伤/重伤) (primary)
  - Measurement: 基于NHTSA CRSS 2015-2017年警方报告事故数据，将受伤严重程度编码为三分类变量（无伤害=仅财产损失、轻伤=低水平非失能伤害、重伤=失能伤害和死亡），并采用10折分层交叉验证计算ROC、总体Precision、总体Reliability和严重类Precision等预测性能指标。
  - Objectivity: 受伤严重程度来自警方事故报告和NHTSA标准化编码记录，属于档案/客观记录数据，而非参与者自我报告；模型预测性能基于ground-truth分类标签和交叉验证计算，不依赖主观感知或态度。

## Ambivalence Is Better than Indifference: A Behavioral and Neurophysiological Assessment of Ambivalence in Online Environments

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/17123
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 该研究提出并检验了双变量（bivariate）评分表征作为替代传统的双极（bipolar）星形评分的设计干预，明确旨在区分矛盾态度与漠不关心，并将具有矛盾信息的产品的购买决策提升至少50%。实验2-4测量了该干预下的实际购买选择，实验3还记录了决策反应时间；实验1用EEG测量注意力以支持潜在机制。
- Decision: 两条纳入路径均满足：(1) 明确的设计目标——双变量表征干预被明确设计并宣称能提高矛盾信息产品的购买决策；(2) 客观测量结果——购买决策是强制选择行为，决策反应时间是系统记录，EEG P300振幅是神经生理测量，均不依赖自我报告。
- Confidence: 0.95

  - Outcome: Purchase decision (forced-choice product selection) (primary)
  - Measurement: 在每个场景结束时，要求参与者在四个随机排序的产品选项中必须选择一个购买；该选择被记录为场景层面的购买决策变量。
  - Objectivity: 这是可观察的强制选择行为，而非自报态度或感知；它是对模拟交易中实际选择结果的直接记录。
  - Outcome: Decision response time (secondary)
  - Measurement: 在实验3中，测量参与者对每个选择表达购买意愿所花费的时间（单位：秒）。
  - Objectivity: 由实验系统客观记录的时间度量，不依赖自我报告。
  - Outcome: Attention (P300 ERP amplitude at Pz electrode) (primary)
  - Measurement: 在EEG实验中，测量第二个属性刺激呈现后300-500ms时间窗内Pz电极处P300事件相关电位的峰值振幅，作为注意力的神经生理指标。
  - Objectivity: 这是脑电图记录的客观神经生理信号，经过标准预处理和峰值检测，不依赖参与者自我报告。

## An assisted approach to business process redesign

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113749
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: ABPR原型通过重设计模式推荐、交互式领域知识整合和仿真评估来支持流程重设计；KUKA案例中的39%时间改进和人工案例中的量化绩效结果直接展示了该软件工件对业务流程绩效的客观影响。
- Decision: 该软件工件的明确设计目标包括通过重设计模式改进业务流程绩效（DO3），并在KUKA真实案例中通过仿真客观测量了39%的时间改进；同时，仿真实验提供了关于前置时间、返工工作量等定量指标，不依赖自我报告。因此，客观设计目标路径和客观测量结果路径均满足。
- Confidence: 0.95

  - Outcome: Simulated process lead time / cycle time improvement (KUKA case study) (primary)
  - Measurement: 在KUKA仓库流程案例中，使用原型中的仿真管理器对初始流程模型和经过重设计的流程模型进行仿真实验，比较循环时间/提前期的百分比变化；最终流程模型相对于首次仿真实现了39%的时间改进（第5.3节、表5）。
  - Objectivity: 仿真实验基于过程模型、时间/成本参数和模拟配置，输出定量过程性能指标，不依赖参与者的自我报告；结果可重复计算，属于客观的量化测量。
  - Outcome: Simulated performance of redesign alternatives in artificial case studies (lead time, rework effort) (secondary)
  - Measurement: 在人工案例研究中，通过仿真比较备选流程设计；例如订单到现金流程中返工工作量减少40%导致提前期缩短10%（表3），以及软件开发流程中分诊模式的应用。仿真由原型执行并输出定量结果。
  - Objectivity: 这些是仿真实验产生的定量过程性能指标（如时间、工作量），而非用户自我报告或主观评分，符合客观测量标准。

## Bringing transparency and trustworthiness to loot boxes with blockchain and smart contracts

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113508
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 软件工件是编码为以太坊智能合约的区块链化 loot box（及演示 DApp）。其核心性能目标包括随机抽取的准确性和运行成本。准确性通过执行智能合约后的实际频次与预设概率的统计拟合来评估；成本通过区块链上的 gas 消耗和美元花费来评估。
- Decision: 该研究明确将准确性和成本作为智能合约工件的性能目标，并使用客观测量（频次统计与卡方检验、gas 与美元成本）来评估。因此满足客观设计目标路径和客观测量路径，至少有一条通过。
- Confidence: 0.95

  - Outcome: Accuracy of the smart-contract random draw (empirical vs. theoretical distribution) (artifact_performance_target)
  - Measurement: 调用智能合约的 drawItem 函数 1000 次（单一玩家）和 1000 次（多玩家），记录各物品出现频次，并与事先设定的概率（0.1, 0.2, 0.7）进行卡方拟合优度检验；还合并 2000 次抽取进行总体检验。
  - Objectivity: 结果来自区块链智能合约的实际执行记录和频数统计，而非参与者自我报告；卡方检验基于可验证的地面真值（预设概率）。
  - Outcome: Transaction cost of calling drawItem (secondary)
  - Measurement: 在以太坊测试网络上运行智能合约，记录每次调用 drawItem 函数消耗的 gas 单位，并乘以设定的 gas 价格和以太币兑换率，换算为美元成本。
  - Objectivity: 成本基于区块链网络实际产生的 gas 消耗和市场价格，是可验证的客观数据，而非主观感知。
  - Outcome: Deployment cost of the smart contract (secondary)
  - Measurement: 记录将智能合约部署到以太坊网络所需的 gas 单位，并按照不同的 gas 价格和汇率计算美元部署成本。
  - Objectivity: 部署成本根据区块链交易的固定 gas 用量和市场价格计算，是客观可验证的工程成本指标。

## How Product Display Orientation Affects Customers’ Choice Satisfaction in Online Purchase: A Choice Closure Perspective

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2022.0575
- Objective design target: False
- Objectively measured outcome: True
- Artifact-outcome link: 网页产品展示方向（水平 vs 垂直）作为界面设计变化，是研究的核心自变量；它通过影响产品比较次数和选择闭合，最终影响以实际行为（产品更换、取消机会选择）衡量的选择满意度。
- Decision: 客观测量路径通过：研究2使用实际产品更换行为作为选择满意度的行为指标，研究5使用是否购买取消机会的二元实际选择作为选择满意度的行为度量；两者均为客观、可观察的实际行为，不依赖自我报告。设计目标路径未通过：论文明确的设计目标是'选择满意度'这一主观心理状态，而非直接以客观行为或绩效作为设计目标。
- Confidence: 0.95

  - Outcome: Actual product switching behavior (Study 2) (primary)
  - Measurement: 在实验室中，参与者选择咖啡杯后，实验者告知所选咖啡杯缺货，参与者需在“接受等值现金”和“等待所选咖啡杯”之间做出真实选择；选择现金视为更换/放弃原选择，选择等待视为不更换。通过这一行为场景衡量选择满意度。
  - Objectivity: 该指标基于参与者面对实际后果时做出的真实行为选择，由实验者直接观察记录，而非自我报告态度或意图。
  - Outcome: Actual selection of cancellation opportunity (Study 5) (primary)
  - Measurement: 参与者在24个冰箱贴中做出选择后，面临是否支付名义费用以保留取消/更改选择机会的二元选择（1=保留，0=不保留），以此作为选择满意度的行为度量；使用二元逻辑回归分析。
  - Objectivity: 参与者在涉及真实金钱代价的决策中做出的实际二元选择，由实验程序记录，不依赖自我报告量表。
  - Outcome: Between-AOI eye saccades (number of product comparisons; Study 2) (secondary)
  - Measurement: 使用Gazepoint GP3眼动仪记录参与者在评估咖啡杯时的眼动，计算五个兴趣区（AOI）之间的眼跳次数（经对数转换），作为产品比较数量的客观指标。
  - Objectivity: 眼动追踪是生理/传感器测量，不依赖自我报告；实验者预先定义AOI，由设备客观记录眼跳路径并计数。

## Mitigating the Security Intention-Behavior Gap:  The Moderating Role of Required Effort on the  Intention-Behavior Relationship

- Year/journal: 2021 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00660
- Objective design target: False
- Objectively measured outcome: True
- Artifact-outcome link: 实验通过改变系统设计特征（单点登录vs多点登录、单因素vs多因素认证、即时提醒vs记忆政策）来操纵所需努力；核心因变量是这些设计条件下的实际安全行为（密码合规分数、是否披露客户信息），因此客观结果直接反映设计特征对安全行为的影响。
- Decision: 至少一项核心因变量是客观测量的实际行为：密码合规分数来自实际创建密码的自动规则计算，信息披露来自聊天日志中可观察的披露行为。因此满足'客观测量结果'路径。自报意图、PBC和努力仅为预测变量或操纵检验，不影响判定。
- Confidence: 0.95

  - Outcome: Password policy compliance score (primary)
  - Measurement: 在实验1和2中，参与者在完成组织任务时实际创建的密码被系统捕获并按5项密码策略标准自动评分（0-5分）；单点登录组使用唯一密码的分数，多点登录组使用三个密码的平均分。评分规则包括密码长度（字符数/15）、包含大小写字母、包含特殊字符、包含数字、不包含词典词。
  - Objectivity: 基于实际创建的密码进行客观算法评分，不依赖参与者的自我报告；系统自动捕获、匿名化并分析密码。
  - Outcome: Unauthorized information disclosure (information disclosure policy adherence) (primary)
  - Measurement: 在实验3中，参与者与自动聊天机器人的交互被记录；若向聊天机器人透露客户敏感信息（如姓名、联系方式等）则编码为1，否则为0；两名研究助理根据明确标准手动审核交互记录，且未出现编码分歧。
  - Objectivity: 基于交互日志的可观察行为，使用明确的二进制披露标准进行编码，而非参与者自我报告；编码标准可复现，且编码分歧为零。

## Mobile Advertising in Distracted Environments: Exploring the Impact of Distractions on Dual-Task Interference

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2024/17758
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 本研究开发的自定义App模拟移动端字谜游戏与弹窗广告的任务-中断场景，App根据NFL视频内容控制广告的弹出时机和内容一致性，并记录任务表现和广告响应。核心客观结果ad engagement（广告再认）用于评估弹窗广告的有效性，且广告时机与一致性设计是研究明确考察并旨在优化广告效果的材料设计变化。
- Decision: 客观测量路径成立：核心因变量ad engagement通过事后的品牌再认测试客观计分，有明确正确答案，不依赖自我报告，是评估广告中断有效性的实质结果。设计目标路径同时成立：研究明确假设并检验广告时机（H2）和内容一致性（H3）可提高中断有效性，即通过材料设计变化改善客观广告效果。
- Confidence: 0.95

  - Outcome: Ad engagement (interrupt effectiveness, brand recognition) (primary)
  - Measurement: 实验结束后进行 surprise memory test（意外记忆测试），参与者从12个品牌（9个实际展示品牌和3个诱饵品牌）中勾选是否记得看到该品牌广告；每个正确识别的品牌得1分，总分0-9分。按广告出现时机（action/replay/commentary）和一致性（congruent/semi-congruent/incongruent）分别计分。
  - Objectivity: 该测量基于对实际呈现品牌的客观再认成绩，存在明确正确答案和客观计分规则，不依赖参与者的主观态度、感知、满意度或自我报告回忆强度。

## Prejudiced against the Machine? Implicit Associations and the Transience of Algorithm Aversion

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/17961
- Objective design target: False
- Objectively measured outcome: True
- Artifact-outcome link: 研究中的IT人工制品是一个虚构的AI体重估计建议系统；WOA反映了参与者实际采纳该AI建议的程度，是算法厌恶/欣赏的核心行为结果。IAT则以AI作为目标类别测量对其的无意识负面联想，也与该人工制品直接相关。
- Decision: 客观测量路径成立：关键因变量WOA通过任务中的实际数值调整（行为日志）客观测量，不依赖自我报告；此外IAT d-score也基于反应时客观测量。设计目标路径不成立：该研究并非评估某个设计改进对客观结果的提升，而是解释算法厌恶现象及其随经验消减的机制。
- Confidence: 0.95

  - Outcome: Weight on Advice (WOA) (primary)
  - Measurement: 在体重估计任务中，参与者先给出初始估计，再看到AI的估计值，随后可修正自己的估计。WOA=(修正估计值−初始估计值)/(AI估计值−初始估计值)，并按Gino and Moore (2007)和Logg et al. (2019)的协议进行winsorize处理，使其落在0到1之间；Block 1和Block 2分别取两次试次的平均值。
  - Objectivity: WOA基于参与者在任务中实际提交的数值计算得出，属于系统记录的行为数据，而非自我报告的态度、意图或感知。
  - Outcome: IAT d-score (implicit prejudice against AI) (secondary)
  - Measurement: 使用内隐联想测验（IAT）测量：参与者快速将AI/me或AI/expert类别词与信任/不信任属性词进行匹配，基于正确匹配的反应时差异计算标准化d-score。
  - Objectivity: d-score由IAT任务中的按键反应时和错误率计算得出，是客观的行为计时测量，不是参与者自我报告。

## Privacy Concerns and Data Donations: Do Societal Benefits Matter?

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2024/16853
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 研究所设计的数据捐赠应用（DataDonors 和 Fight COVID-19）通过隐私控制设置、共情图片/文字或社会利益信息等界面特征，直接影响参与者实际捐赠的数据项数量；该行为结果是评估这些设计特征效应的中心因变量。
- Decision: 两个实验的核心因变量是实际数据捐赠量（所选捐赠项总数），由系统直接记录参与者的选择，属于客观行为测量；同时，应用界面中的隐私控制和公共利益信息等设计特征明确旨在促进数据捐赠行为。因此两条路径均通过。
- Confidence: 0.95

  - Outcome: Amount of data donation (total sum of donated data items) (primary)
  - Measurement: 参与者在数据捐赠应用（DataDonors 模拟界面或 Fight COVID-19 模拟应用）中逐项选择是否捐赠 23 或 27 类人口、医疗和行为数据；因变量为被选中的捐赠项目总数。
  - Objectivity: 该结果是参与者在实验系统内的实际选择行为，由系统记录并求和，而非自我报告的态度、意图或感知。

## Pushing Yourself Harder: The Effects of Mobile Touch Modes on Users’ Self-Regulation

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1155
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 该研究将移动应用中的按压与轻点两种触控模式作为软件交互设计特征，明确以提升用户自我调节（例如选择健康饮料、增加运动、减少卫生违规）为设计目标。研究通过实验操纵触控模式，考察其对客观行为结果的影响。
- Decision: 按压触控模式被明确设计为一种隐性的数字助推，用于改善用户实际的自我调节行为（饮食选择、运动锻炼、卫生遵守），因此满足客观设计目标路径；同时，研究1中的饮料选择和研究3中的个人卫生违规次数均为可验证的实际行为或独立观察测量，不依赖于自我报告，因此也满足客观测量路径。
- Confidence: 0.95

  - Outcome: Healthy beverage choice (Study 1) (primary)
  - Measurement: 参与者在移动应用中实际选择四种饮料之一；选择被编码为健康或不健康饮料，并通过二元逻辑回归分析。按压组60人中有41人选择健康饮料，轻点组60人中有26人选择健康饮料。
  - Objectivity: 这是参与者的实际选择行为，而非自我报告的偏好或意图；选择结果由实验管理员记录并按预设标准编码。
  - Outcome: Personal hygiene lapses (Study 3) (primary)
  - Measurement: 在卫生教育任务后，由两名实验管理员独立观察并记录四类违反卫生规范的行为（违反社交距离、握手、未消毒共用手机、触摸面部），每违反一项计1分，总分0-4。
  - Objectivity: 基于预先设定的明确行为准则和管理员的独立非干预性观察，而非参与者自我报告；按压组平均违规次数显著少于轻点组。

## ROLEX: A Novel Method for Interpretable Machine Learning Using Robust Local Explanations

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/17141
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: ROLEX 方法通过直接优化采样中心与半径、SMOTE 过采样、非线性局部模型选择以及 LDA 评估框架，明确以提升局部解释的 local faithfulness（LocalFid 和 LDA-fidelity）为核心设计目标；这些指标直接度量了该软件方法相对于基准解释方法的表现。
- Decision: 两条路径均通过：1) ROLEX 明确以改进局部解释的 local faithfulness 为设计目标，属于客观性能目标；2) 该目标通过 LocalFid 和 LDA-fidelity 等基于模型输出计算得到的定量指标客观度量，而非依赖用户自报。专家访谈为主观补充证据，不影响客观结果的判定。
- Confidence: 0.95

  - Outcome: Local fidelity (LocalFid) (primary)
  - Measurement: 在待解释实例 x_i 的邻域内采样测试点，计算黑盒分类器预测 f^(z') 与局部解释模型 s_x_i(z') 的一致程度，使用 balanced accuracy 作为准确率指标（论文公式 8 与 Algorithm 1）。
  - Objectivity: 该指标完全由黑盒模型和局部解释模型的预测输出计算得出，不依赖参与者的自我报告、感知或主观评分，是可复现的客观计算指标。
  - Outcome: LDA-fidelity score (primary)
  - Measurement: 在 Local DB-Aware (LDA) 框架下，仅对具有异质样本的决策敏感实例计算局部 fidelity 的平均值；排除同质样本边界情形，使用 balanced accuracy 计算（Algorithm 1）。
  - Objectivity: 该指标基于黑盒预测标签与局部解释模型预测标签的客观比较，是可计算的算法绩效指标，不依赖用户自报或主观评分。

## That's interesting: An examination of interest theory and self‐determination in organisational cybersecurity training

- Year/journal: 2022 / Information Systems Journal
- DOI: 10.1111/isj.12374
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 该研究构建了一个基于Web的网络安全培训程序（参数篡改练习、在线演示视频、反馈和“I Give Up”自主退出按钮），明确旨在通过兴趣和自我决定动机提升学习行为与绩效。合格结果（实际学习努力和学习绩效）直接来自系统日志和任务完成情况，与培训程序的干预特征直接相关。
- Decision: 两条纳入路径均成立：(1) objective_design_target=true，研究明确以提升网络安全技能和学习行为为设计目标（RQ1、H8/H9）；(2) objectively_measured_outcome=true，实际学习努力（EFF）通过系统日志中的尝试次数和视频观看次数测量，实际学习绩效（PERF）通过成功完成练习的数量（系统判定）测量，均不依赖参与者自我报告。因此客观结果匹配。
- Confidence: 0.95

  - Outcome: Actual learning effort (EFF) (primary)
  - Measurement: 由系统日志记录参与者在全部练习中的总尝试次数和观看在线教程视频的总次数，经min-max归一化转换为1-7量表后作为形成性指标。
  - Objectivity: 基于系统自动记录的行为计数（尝试次数、视频观看次数），不依赖参与者自我报告；表4报告了每项练习的平均尝试次数和完成人数。
  - Outcome: Actual learning performance (PERF) (primary)
  - Measurement: 系统跟踪参与者成功完成的练习数量（共3个难度递增的参数篡改练习），由服务器端判定每次提交是否成功完成，成功完成数作为学习绩效。
  - Objectivity: 以任务完成的客观正确性为依据，由系统基于练习结果自动判定，而非参与者自我报告。表4和附录C展示了练习内容与完成情况。

## Trust calibration of automated security IT artifacts: A multi-domain study of phishing-website detection tools

- Year/journal: 2021 / Information & Management
- DOI: 10.1016/j.im.2020.103394
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 实验中的检测器工具界面在屏幕顶部持续显示信任校准信息（检测准确率、运行时间、错误决策后果严重性和威胁类型）；该设计特征旨在校准用户信任，进而通过提高对检测器建议的依赖来改善用户避免钓鱼网站的实际表现。H7 证实依赖对客观用户性能的正面影响。
- Decision: 两个包含路线均成立：一是检测器的校准信息显示被明确设计用于促进用户对钓鱼网站的防护表现（objective_design_target）；二是用户性能/避开钓鱼网站能力通过点击日志和客观决策计分进行测量，而非仅依赖自我报告（objectively_measured_outcome）。因此保留该文献。
- Confidence: 0.95

  - Outcome: User performance / ability to detect phishing websites (primary)
  - Measurement: 基于参与者在10个网站试次中的客观决策计分：是否避免访问钓鱼网站、是否点击后避免浏览、是否正确识别合法/钓鱼网站、是否避免与钓鱼网站交易；最终按正确决策百分比计分。访问和浏览行为通过网络分析软件跟踪点击记录测量。
  - Objectivity: 该结果不是自我报告，而是基于系统记录的点击/浏览行为和明确的客观决策分类标准进行计分，属于可独立观察的行为表现。
  - Outcome: Behavioral disagreement/agreement with detector recommendations (secondary)
  - Measurement: 在10个试次中记录参与者与检测器建议不一致的比率（参与者认为网站合法而检测器判定为钓鱼，或相反），按试次统计不同意百分比，用于检验信任校准过程。
  - Objectivity: 该指标来自参与者的实际决策与检测器输出的比较，属于系统记录的行为数据，而非自我报告的信任或意图。

## Virtual Reality, Mental Models, and Mindful Decision-Making

- Year/journal: 2025 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00933
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 研究对象为VR呈现技术（含交互式浏览和深度提示两个设计特征）。研究明确假设VR呈现能够提高用户获取的信息量（H2），并通过获取信息与感知控制提升心理模型质量，进而促进正念决策。客观的获取信息（考试得分）直接用于检验VR呈现的效果及其对心理模型质量的影响。
- Decision: 至少有一个核心结果变量（获取的信息/考试成绩）通过可客观计分的多项选择测试题测量，不依赖自我报告，满足客观测量路径；同时VR呈现的设计特征明确以提升信息获取为假设目标，也支持设计目标路径。因此objective_outcome_match=true。
- Confidence: 0.95

  - Outcome: Acquired information (exam score) (primary)
  - Measurement: 通过包含9道选择题的客观测试得分衡量（0-9分）。Study 1中测试内容为计算机硬件组件知识；Study 2中测试内容为房屋的整体理解、具体特征和相对结构（例如浴室数量、地板材质、厨房与卧室的相对位置）。答案有明确标准，按答对题数计分。
  - Objectivity: 该测量基于客观测验成绩而非参与者自我报告；答对题数可由标准答案客观判定，不依赖参与者主观感知、态度或回忆自信。作者也明确说明研究同时使用了客观和主观数据。

## Would you please like my tweet?! An artificially intelligent, generative probabilistic, and econometric based system design for popularity-driven tweet content generation

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113497
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 所设计的社交媒体内容生成与建议系统以最大化推文参与度（总转发与收藏数）为核心目标；系统通过预测模型和生成模型产生推文结构、特征和建议文本，并以实际参与度作为模型训练、模型选择和生成推文评估的客观依据。
- Decision: 设计目标明确指向提高可观察的推文参与度（转发和收藏），且该参与度由Twitter API客观记录；同时实验评估使用实际参与度计数计算预测误差，因此两条纳入路径均成立。
- Confidence: 0.95

  - Outcome: Total Engagement (retweet + favorite counts) (primary)
  - Measurement: 使用 Twitter API 返回的每条推文的转发数（reTweet）与点赞/收藏数（favorite）之和作为流行度/参与度的度量；该变量作为八个预测模型（模型1-8）的因变量，并在滚动预测实验中作为预测值的对照真值。
  - Objectivity: 该指标来自平台API记录的实际用户行为计数，而非参与者的自我报告；是可独立验证的客观行为结果。
  - Outcome: Predictive accuracy / cumulative mean absolute percentage error (CMAPE) of engagement predictions (secondary)
  - Measurement: 在按时间排序的推文数据上，用累积滚动窗口训练模型，预测下一条推文的总参与度，再将预测值与Twitter API返回的实际总参与度比较，计算绝对百分比误差及累积平均绝对百分比误差（CMAPE）。
  - Objectivity: 误差计算基于实际平台记录的参与度计数与模型预测值的客观比较，不依赖任何用户主观评价。

## Decisions for information or information for decisions? Optimizing information gathering in decision-intensive processes

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113632
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 本文提出的CMMN+MDP推荐工具明确以最大化最终决策的期望利润（最终决策收益减去信息收集成本）为设计目标；在部署阶段，工具为决策者提供每个状态下最有利的信息收集任务或最终决策建议。数值分析将该工具的MDP策略与人工决策树比较，显示期望利润从8226.0提高到15867.6，直接证明了该软件工件对客观经济结果的作用。
- Decision: 满足objective_design_target：论文明确将期望利润最大化（收益减成本）作为信息收集决策支持方法的核心设计目标，并通过数值分析展示其对决策绩效的改善。同时满足objectively_measured_outcome：中心评价指标（期望利润、期望收入、平均信息获取成本）均由明确的信息结构、奖励函数和概率分布计算得出，非自我报告性主观指标，属于客观绩效测量。因此objective_outcome_match为true。
- Confidence: 0.93

  - Outcome: Expected profit (primary)
  - Measurement: 通过MDP优化模型计算每个状态下的最优行动，并根据信息结构 Y(s,f) 和任务成本计算期望利润；Table 5给出了MDP与决策树的期望利润对比，Table 6给出9个实例的利润对比。
  - Objectivity: 期望利润是由明确的奖励函数（最终决策收益减去信息收集成本）和概率分布计算得出的数值结果，不依赖于参与者的自我报告或主观评分。
  - Outcome: Expected revenue (secondary)
  - Measurement: 根据信息结构中的收益部分（报价接受概率、维修次数、合同期限、维修成本等）计算最终决策的期望收入；Table 5给出MDP与决策树的期望收入对比。
  - Objectivity: 期望收入由明确给出的数学公式和概率分布计算，属于客观的数值绩效指标，而非自我报告的感知或态度。
  - Outcome: Average retrieval cost (secondary)
  - Measurement: 对MDP策略下执行信息获取任务所产生的成本进行平均计算；Table 5比较了MDP与决策树的平均信息获取成本。
  - Objectivity: 信息获取成本是模型中的明确数值参数，其平均值由计算得出，不依赖用户自我报告。

## A social mechanism for task-oriented crowdsourcing recommendations

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113449
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 所评估的SCT社会推荐机制通过偏好、历史绩效和社会影响力生成推荐列表；客观结果（推荐准确率、贡献接受率、请求者认可率）直接用于衡量该机制的推荐效果。
- Decision: 该研究至少有一个实质性的客观测量结果：推荐准确率基于请求者实际选择，任务接受意愿基于实际接受记录，贡献满意度实际化为请求者对完成工作的认可行为；同时论文明确以帮助请求者找到合适且愿意完成任务的高质量贡献者为设计目标，因此两条纳入路径均成立。
- Confidence: 0.9

  - Outcome: Accuracy of recommendations (primary)
  - Measurement: 以推荐列表中被请求者实际选中的贡献者人数除以推荐列表总人数计算（Accuracy = |recommend list ∩ pickup| / |recommend list|），数据来自系统记录。
  - Objectivity: 基于请求者的实际选择行为和系统记录，而非自报感知或态度。
  - Outcome: Satisfaction with contribution / approval rate (primary)
  - Measurement: 以推荐列表中实际被请求者选中并获得请求者认可（approve）的贡献者比例计算（Satisfaction = |recommended list ∩ pickup ∩ approve| / |recommended list ∩ pickup|）。
  - Objectivity: 该指标虽然名为“满意度”，但操作化为请求者对已完成贡献的实际认可/批准行为，是可观察的接受决定，而非自报态度量表。
  - Outcome: Willingness to take up task invitation (primary)
  - Measurement: 以贡献者实际接受的任务邀请数除以收到的任务邀请总数计算（Willingness = |task invited ∩ accepted| / |task invited|），基于任务邀请接受/拒绝记录。
  - Objectivity: 基于贡献者实际接受或拒绝邀请的行为记录，而非自报意愿或意向。

## Design principles for learning analytics information systems in higher education

- Year/journal: 2021 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2020.1816144
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: LAIS 原型将设计原则实例化为每周报告和可视化仪表盘，向讲师提供学生与讲座录像互动的可操作信息；讲师据此进行教学干预（如编辑录像、加入测验），服务器日志显示干预后特定录像的学生互动事件显著增加（从153增至1987），从而将软件设计特征与客观的学生投入行为结果联系起来。
- Decision: 两条纳入路径均满足：LAIS 明确以支持教师监控和改善学生投入以优化学习与教学为设计目标（客观设计目标）；同时，服务器日志中的实际互动事件计数为客观行为测量，且是评估工件效用与效能的核心证据之一。
- Confidence: 0.9

  - Outcome: Student engagement with lecture recordings (LTR), operationalized as interaction event counts (primary)
  - Measurement: 通过服务器日志追踪并统计学生与讲座录像互动的事件数量，包括 load_video、play_video、pause_video、seek_video、speed_change_video、stop_video 等事件；按视频和时间聚合，并对特定视频（如 LTR.A）进行干预前后的纵向对比。
  - Objectivity: 数据来自系统自动生成的服务器日志，直接记录学生实际观看行为，而非学生的自我报告或主观感知，属于可验证的行为观测数据。

## Disclosure decisions and the moderating effects of privacy feedback and choice

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113717
- Objective design target: False
- Objectively measured outcome: True
- Artifact-outcome link: 研究设计的隐私反馈功能及提供“选择”的功能；选择功能让用户自主决定是否查看反馈，从而客观上揭示了用户对隐私反馈的真实兴趣，是该设计特征的直接行为结果。
- Decision: 主要因变量披露意愿为自报量表，但“是否选择查看隐私反馈”是系统记录的客观实际行为（138/162选择查看），属于客观测量的实质性结果，满足客观测量出路。因此 objective_outcome_match=true；objective_design_target=false。
- Confidence: 0.9

  - Outcome: Privacy feedback access choice (secondary)
  - Measurement: 在“选择”实验条件下，系统记录参与者是否点击“FEEDBACK”按钮查看隐私反馈页面，或点击“NEXT”跳过；论文报告162名参与者中有138名选择查看隐私反馈。
  - Objectivity: 该行为由应用程序的交互日志直接记录，是可观察的实际选择行为，不依赖参与者的自我报告。

## How AI-Based Systems Can Induce Reflections: The Case of AI-Augmented Diagnostic Work

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/16773
- Objective design target: False
- Objectively measured outcome: True
- Artifact-outcome link: 该研究开发的ML-C DSS在第二阶段向医生提供各诊断标签的概率分数，作为反思伙伴刺激反思；同时，研究比较了有无该系统时的诊断错误率，显示AI辅助后错误率从80.2%降至58.2%，即该软件设计间接与客观诊断准确性的改善相关。
- Decision: 研究中包含客观测量的实质性结果：医生诊断与NIH数据集ground truth的比对得出诊断错误率（Stage 1 vs Stage 2），这是客观可验证的行为/绩效结果，且作为补充数据用于评估ML-C DSS的影响，满足'客观测量结果'路径；但系统明确的设计目标是激发反思而非直接优化诊断绩效，故'客观设计目标'路径不成立。
- Confidence: 0.9

  - Outcome: Diagnostic error rate (Stage 1 vs. Stage 2) (secondary)
  - Measurement: 将医生在第一轮（无AI辅助）和第二轮（有ML-C DSS辅助）中做出的诊断选择与NIH ChestX-ray数据集的真实标签进行比较，计算错误分类的百分比。
  - Objectivity: 该结果基于与外部ground truth标签的客观比对，而非参与者的自我报告或主观评分。

## Push It Cross the Finish Line—Designing Online Interfaces to Induce Choice Closure at the Postdecision Prepurchase Stage

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2021.0085
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 研究操纵的是购物车页面上的界面设计（直接强化：优惠券/口头表扬；社会强化：信息型/规范型社会背书）。该界面设计旨在通过减少认知失调、增强感知选择闭合，进而提高决策满意度和购买意愿，并最终对抗购物车放弃/推动购买完成。客观按钮点击（Proceed to Checkout）是在这些界面线索展示后测得的实际行为代理，直接对应论文所关注的购物车放弃/购买完成问题；但论文未报告界面条件对该客观点击行为的主效应，仅将其作为满意度影响购买意愿的下游行为回归结果。
- Decision: 两条路径均判定匹配：（1）客观设计目标：界面强化线索明确以推动消费者完成购买、减少购物车放弃为实践目标；（2）客观测量结果：研究使用“Proceed to Checkout”与“Save for Later”按钮点击作为购买意愿的客观代理指标，这是可观察的实际行为而非自我报告。主要理论变量（认知失调、选择闭合、满意度）虽为自我报告，但不影响至少一个实质性客观结果的存在。
- Confidence: 0.9

  - Outcome: Proceed to Checkout vs. Save for Later button click (objective proxy of purchase intention) (secondary)
  - Measurement: 在模拟电商网站购物车页面，参与者查看购物车信息（含实验设计的强化线索）后，实际点击“Proceed to Checkout”或“Save for Later”按钮；该点击行为被用作购买意愿的客观代理指标，并用于回归分析（满意度→该行为）。
  - Objectivity: 按钮点击是可观察的实际行为/系统交互记录，而非参与者自我报告的态度、意愿或感知量表。
  - Outcome: Purchase completion / shopping cart abandonment reduction (explicit design target, not directly measured) (artifact_performance_target)
  - Measurement: 论文以购物车放弃率（约70%）和相关经济损失为动机，将界面设计的目标表述为“推动消费者越过终点线（完成购买）”和“对抗购物车放弃”；但实验中未追踪真实支付或购买完成，仅以按钮点击作为代理。
  - Objectivity: 完成购买是客观结果，但本文未直接测量真实购买完成率；作为明确的设计目标，不单独作为经验性客观测量。

## Visual analytics of set data for knowledge discovery and member selection support

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113635
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 所提出的基于流形网络模型（MNM）的可视分析系统，通过前向映射预测阵容的比赛结果（胜负准确率），并通过逆向映射从团队潜在变量重构成员组成（JS重构误差）；这些客观指标直接用于评估系统支持知识发现与成员选择的核心功能。
- Decision: 文章明确将胜负预测准确率和阵容重构误差作为系统前向与逆向任务的评估标准，两者均为基于真实数据或量化公式的客观测量，因此满足‘客观测量结果’路线；同时，系统设计目标明确包括预测阵容输出和重构满足条件的阵容，因此也满足‘客观设计目标’路线。
- Confidence: 0.9

  - Outcome: Game result (winning/losing) prediction accuracy (primary)
  - Measurement: 使用NBA真实比赛数据评估前向问题，将模型预测的比赛胜负结果与真实比赛结果比较，计算准确率；提案方法63%，基准系统56%，随机水平50%。
  - Objectivity: 以实际比赛胜负记录为客观真值，通过预测结果与真实结果的一致率计算，不依赖用户自我报告或主观评分。
  - Outcome: Lineup reconstruction error via Jensen–Shannon divergence (primary)
  - Measurement: 使用Jensen–Shannon（JS）散度计算测试阵容成员组成与模型重构的成员组成之间的差异；提案方法重构误差0.012，均匀分布基线0.24，平均成员组成比较0.14。
  - Objectivity: 该指标是从数据派生的成员组成分布与模型生成分布之间的数值散度，有明确的计算公式和可复现的量化标准，而非主观评价。

## Proper and improper uses of MCDA methods in energy systems analysis

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113848
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 本文开发/升级的MCDA-MSS软件（http://mcdamss.com）内嵌规则与六条指南，其设计目标就是帮助决策者和分析师选择最适合的MCDA方法，避免不当使用并改善实际决策方法选择。该软件被回溯应用于56个案例研究，产出的匹配/不匹配和指南违规结果直接用于检验软件功能，因此上述客观结局直接衡量该软件设计变更的效果。
- Decision: 两条纳入路径均成立：1) MCDA-MSS明确以改善MCDA方法选择（实际选择/行为）为设计目标，并声称能保证MCDA方法的适当使用；2) 核心结局（使用的MCDA方法与推荐方法是否匹配、是否违反指南）通过软件规则库和特征矩阵客观判定，而不是依赖参与者自我报告。因此objective_outcome_match为true。
- Confidence: 0.82

  - Outcome: Proper/improper use of MCDA methods (MCDA-MSS match status) (primary)
  - Measurement: 将56个能源系统案例研究按MCDA-MSS的156个特征进行编码，运行基于规则的MCDA-MSS软件，将案例实际使用的MCDA方法与软件推荐的方法进行匹配；软件输出匹配/不匹配、未覆盖特征、违反的指南及推荐替代方法（见表3），并据此统计匹配率（37.5%）和不当使用频率（约60%）。
  - Objectivity: 该结局不是参与者的自我报告，而是基于明确特征体系和规则库由软件算法判定的方法选择正确性；它反映案例作者实际选择的MCDA方法这一可观察行为与规范性推荐之间的客观比对。尽管特征编码包含少量作者的推断/假设（3.18%推断、7.92%假设），判定规则透明且可复现。
  - Outcome: Guideline violations and reasons for improper MCDA method use (secondary)
  - Measurement: 对每个不匹配案例，MCDA-MSS识别未满足的特征及其对应的指南，并统计各指南未得到遵循的频率（Fig. 2）；针对六条指南分别给出典型案例（Tables 4-7）。
  - Objectivity: 违规判断由MCDA-MSS的规则库基于案例特征自动生成，非自我报告；每条指南有明确的操作性定义（如权重含义、问题陈述类型、测量尺度、归一化步骤、标准间交互），因此是可复现的规则化评估。

## Reach Out and Touch: Eliciting the Sense of Touch Through Gesture-Based Interaction

- Year/journal: 2021 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00704
- Objective design target: False
- Objectively measured outcome: True
- Artifact-outcome link: 所比较的软件交互方式（触摸屏交互 vs. 空中手势交互）是研究的核心设计变更；通过内容分析客观测量参与者在选择理由中提及触觉属性的行为，发现触摸屏交互（尤其在高触觉重要性产品条件下）显著增加了触觉属性提及，从而为交互方式对感知触摸感的影响提供了客观行为层面的佐证。
- Decision: 客观设计目标路线未通过：软件交互方式的预期改善目标是感知触摸感，属于主观感受而非实质性客观状态或行为。客观测量路线通过：虽然主要构念均通过自报量表测量，但研究中对选择理由的内容分析采用了明确的编码规则和评分者间信度检验，客观测量了参与者实际提及触觉属性的行为，属于实质性次要结果，满足至少一个客观结局的标准。
- Confidence: 0.8

  - Outcome: Mention of haptic information in product choice justifications (content analysis of decision attributes) (secondary)
  - Measurement: 参与者在购物任务后书面说明选择理由，两名对研究假设不知情的研究助理独立编码其理由中是否提及产品触觉属性（如材质、重量、质地、温暖感、光滑度等），提及记为1，否则记为0；使用卡方检验比较不同交互条件下提及触觉属性的参与者比例。
  - Objectivity: 该测量基于对开放式文本的明确编码规则，而非参与者的自报量表或主观感受；编码标准可复现，且报告了较高的评分者间信度（alpha > 0.70），因此属于对实际行为（选择理由内容）的客观化测量。

## An Activity Theory Approach to Leak Detection and Mitigation in Patient Health Information (PHI)

- Year/journal: 2021 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00687
- Objective design target: True
- Objectively measured outcome: False
- Artifact-outcome link: 文章提出的活动理论访问控制模型及Java原型通过将每次访问请求与privilege set匹配来检测PHI泄漏；不匹配时生成缓解策略（如deny restriction、联系管理员/患者），因此软件设计明确以PHI泄漏检测和缓解这一客观安全结果为目标。
- Decision: 路线1成立：软件原型和访问控制模型明确以检测和缓解PHI泄漏这一客观安全状态/行为为目标，摘要、设计目标和评价部分均有明确表述。路线2不成立：评价主要依赖专家主观确认、场景演示和原型示例，没有对泄漏检测/缓解效果的客观测量指标。
- Confidence: 0.78

  - Outcome: PHI leak detection and mitigation (unauthorized access prevention) (artifact_performance_target)
  - Measurement: 未进行实证测量；论文通过四个PHI泄漏场景的示例映射、交易测试（privilege set匹配）以及Java原型截图（Figure 7e显示mismatch触发管理员/患者联系）说明模型和原型能够检测和缓解泄漏。
  - Objectivity: 该目标本身是客观的安全结果（是否存在未授权披露或非法信息流），但论文仅给出概念性演示和界面示例，没有系统日志、事件计数、正确率等客观测量数据，因此属于未测量的设计目标而非客观测量的结果。

## Long-term multi-criteria improvement planning

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113606
- Objective design target: True
- Objectively measured outcome: True
- Artifact-outcome link: 本文提出的软件（MCDMBM.py / MCDMBM.exe）实现了基于图的改进规划框架；其生成的路径通过排名增量、瓶颈风险、运营变化和最优性占比等客观指标进行评估，直接将软件与客观绩效目标联系起来。
- Decision: 路径1通过：软件框架明确旨在生成提高排名/等级的改进场景，排名增加是核心设计目标。路径2通过：论文报告了基于真实数据计算得出的客观评价指标（排名增量、Z(p)、Φ(p)、最优性占比），并非仅依赖自我报告。
- Confidence: 0.75

  - Outcome: Rank/level increase (I(p)) (artifact_performance_target)
  - Measurement: 沿着改进路径，每一步的排名/等级增量通过差值函数τ(ν'_k, ν''_h)计算并累加（公式6,10），在案例研究中基于ARWU20真实排名数据计算，表4列出各步的排名增量。
  - Objectivity: 该指标由形式化图模型和官方排名数据计算得到，不依赖任何自我报告或主观评价。
  - Outcome: Bottleneck risk indicator (Z(p)) (secondary)
  - Measurement: 根据公式(4)，若当前改进方向不是argmax#Λ_k(ν'_k)则记τ(ν'_k, ν''_h)为瓶颈风险，沿路径累加（公式8），表4报告每条的Z(p)值。
  - Objectivity: 该指标由观测替代方案数据与既定规则计算得到，属于可复现的形式化计算结果，非自我报告。
  - Outcome: Operational change indicator (Φ(p)) (secondary)
  - Measurement: 根据公式(5)，若连续两步改进的是不同准则或参照不同观测对象则记τ为运营变化，沿路径累加（公式9），表4报告每条的Φ(p)值。
  - Objectivity: 该指标由图结构和基准选择规则直接计算，非主观评分或自我报告。
  - Outcome: Optimality percentage over penalty-weight pairs (secondary)
  - Measurement: 生成54对罚权(α_Φ, α_Z)，对每条生成路径计算其在聚合单目标最短路径问题中为最优解的罚权对占比（如p1在56%的权对下最优）。
  - Objectivity: 该比例通过对图进行确定性Dijkstra求解得到，属于客观的算法输出，不依赖参与者主观报告。

## Showcase: A Data-Driven Dashboard for Federal Criminal Sentencing

- Year/journal: 2023 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00796
- Objective design target: True
- Objectively measured outcome: False
- Artifact-outcome link: ShowCase仪表盘通过整合多种量刑建议区间（指南、同行法官、公众意见）、类似案例、额外因素、被告风险评分和需求，旨在为法官提供更全面的信息，从而改进实际量刑决策的公平性和客观性；但这一目标仅得到专家主观评价支持，未通过真实判决结果进行实证验证。
- Decision: 纳入路线1成立：论文明确将提升量刑决策的公平性和客观性作为软件制品的设计目标，量刑决策属于实际行为和选择，是实质性客观结果；尽管该目标未被客观测量，但路线1不要求测量。路线2不成立：所有评价证据均来自访谈参与者的自我报告和主观评价，没有系统日志、客观评分、实际判决记录或其他非自我报告测量。
- Confidence: 0.72

  - Outcome: Fairness and objectivity of federal criminal sentencing decisions (artifact_performance_target)
  - Measurement: 未进行实证测量；论文仅通过11次法律专家半结构化访谈收集对仪表盘能否促进更公平、更客观判决的主观评价（第4.3节）。
  - Objectivity: 该结果是明确的设计目标——影响法官的实际量刑决策（真实行为和选择），而不仅仅是感知；但论文没有用实际判决记录、评分标准或行为日志等客观方式测量该结果。

## An interface between natural language and abstract argumentation frameworks for real-time debate analysis

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113694
- Objective design target: True
- Objectively measured outcome: False
- Artifact-outcome link: AIPA/WebAIPA的人工制品设计目标是通过将自然语言论证转化为抽象论证框架，实时计算并可视化可接受论证、冲突结论和论证状态，从而支持实时辩论的结构化与可追溯性。该目标被明确陈述并通过两个应用案例演示，但没有通过受控实验或客观测量验证其实际效果。
- Decision: objective_design_target（真）：论文明确将实时论证推理、辩论状态计算和可追溯图结构作为AIPA的设计目标，这些属于可观察的性能/功能属性。objective_measured_outcome（假）：没有对任何实质性结果进行客观测量；两个案例是说明性的，结论基于定性描述和参与者反馈，而非系统日志、任务绩效、正确性评分等客观指标。因此总判定为真。
- Confidence: 0.65

  - Outcome: Real-time computation of argumentation extensions and debate status (artifact_performance_target)
  - Measurement: 未进行系统测量；论文将其作为设计目标和系统能力来描述，例如在第二个应用中声称173个论点仍可即时获得结果，但没有提供计时数据或性能基准。
  - Objectivity: 实时性属于可观察的系统性能属性，而不是用户自我报告；但本文只是定性说明‘即时’完成，未用日志或客观计时指标加以验证。
  - Outcome: Traceable and structured representation of debate arguments (artifact_performance_target)
  - Measurement: 工具记录论点、参与者、时间以及攻击/支持关系并生成图结构；论文展示了该功能，但没有用客观外部标准衡量其质量或效果。
  - Objectivity: 可追溯性是一种可观察的工件属性（图结构、记录的存在），但本文没有系统评估该属性是否真正改善了真实辩论的客观结果。
