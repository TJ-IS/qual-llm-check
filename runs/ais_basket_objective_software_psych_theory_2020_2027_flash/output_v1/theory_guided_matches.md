# Psychology-theory-guided subset

Completed: 2475 / 2475
Retained: 110

## Designing Effective Mobile Health Apps: Does Combining Behavior Change Techniques Really Create Synergies?

- Year/journal: 2021 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2021.1912936
- Metrics: training count; application opening
- Objective evidence: 文章的核心假设和贡献围绕这两个客观使用量指标展开。在Measurement部分将应用打开和训练计数明确为因变量；在Evaluation Results中通过ANOVA和ANCOVA检验主效应和交互效应。研究发现保护动机和社会上行比较单独应用时均显著提升使用量，组合时产生负交互效应，支持H1-H3。这些客观使用结果构成文章的主要实证贡献。
- Artifact: mHealth移动健康应用（名为WORKLAX的压力缓解原型应用） — 四个原型：社会上行比较原型（SUC推送通知和性能可见性页面）、保护动机原型（恐惧诉求推送通知）、组合原型、控制原型。各原型共享基线功能（训练视图和信息视图），但在行为改变技术设计特征上存在差异。
- Theory: 社会向上比较理论（Social Upward Comparison Theory, Festinger 1954）; 保护动机理论（Protection Motivation Theory, Rogers 1975）
- Theory-to-design: 文章采用解释性设计理论方法，将两个理论的变量实例化为设计特征。社会向上比较理论：比较维度→提醒用户将mHealth使用作为比较维度；负绩效差异→推送消息和性能可见性页面显示用户使用量低于匿名其他用户的平均值；防止副作用→使用匿名平均数据避免嫉妒、自尊威胁和隐私问题。保护动机理论：威胁评估（严重性和易感性）→恐惧诉求推送消息强调威胁的严重性和用户易感性；应对评估（反应效能、自我效能、反应成本）→推送消息强调应用锻炼能有效且低成本地缓解压力。预期这些设计特征会通过各自的心理机制提升mHealth使用；但组合时会因机制冲突产生负交互。
- Decision: 基础筛选通过：文章以提高mHealth客观使用量（训练计数和应用打开次数）为核心目标，这些指标来自系统日志，独立于主观感知；文章通过设计并构建四个mHealth原型（WORKLAX）来实现，明确说明了软件制品及其被改造的特征（SUC推送/性能页面、PM恐惧推送）并用客观指标评估。理论细筛通过：社会向上比较理论和保护动机理论是心理学理论，文章在理论背景中解释了其心理机制，并前瞻性地将这些理论实例化为具体设计特征，推导出假设并进行了实证检验，形成了完整的理论-设计-指标链条。
- Confidence: 0.98

## Unlocking the Power of Voice for Financial Risk Prediction: A Theory-Driven Deep Learning Design Approach

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/17062
- Metrics: out-of-sample mean squared error (MSE); out-of-sample R² (R²_oos relative to market benchmark); long-short straddle strategy return
- Objective evidence: 文章的研究目标是提升金融风险预测能力，核心贡献是DeepVoice框架及其风险预测效果。设计评价部分以MSE和out-of-sample R²为主要指标，系统比较DeepVoice与市场基准、无语声/无文本变体、多种机器学习/深度学习方法，并用期权交易策略验证经济价值。例如Table 4显示DeepVoice在各预测区间相对市场基准的R²_oos提高2.26%-8.34%。
- Artifact: DeepVoice, a nonverbal predictive analysis system for financial risk prediction, instantiated as a software system for earnings conference call analysis — DeepVoice系统整体，包括数据采集、数据提取、机器学习预测和元学习组件；核心设计组件包括两阶段LSTM深度模型（用于学习vocal-verbal时序特征与交互）、基础vocal cues特征表示，以及与基本面/风险模型的stacking集成框架。
- Theory: Mehrabian's communication model (MCM); Nonverbal communication theory
- Theory-to-design: 文章在Table 1中明确以MCM为kernel theory。理论命题“vocal cues和vocal-verbal一致性是沟通信息的关键”被转化为meta-requirements，要求（1）同时利用vocal和verbal线索，（2）使用顺序模型学习全过程中vocal线索的时序变化及vocal-verbal交互，（3）使用基础vocal cues而非高错误率的高层vocal构念。进而推导出metadesigns：元学习集成、两阶段LSTM、基础vocal cues。设计选择不是任意的，而是由理论对心理机制的解释推出：如声音音调变化会反映紧张/自信等认知状态，因此需要用LSTM学习时序模式；声音与言语不一致会产生认知失调，因此需要两阶段融合；高层情感构念缺乏公认测量标准，因此使用基础声学特征。文章进一步以H1-H3和实验检验这些理论驱动的设计是否改善风险预测指标。
- Decision: 基础筛选通过：文章的核心贡献是DeepVoice系统，通过设计软件制品来降低金融风险预测误差，以股票波动率的out-of-sample预测MSE/R²和期权交易收益等客观指标作为最终目标和核心评价，不依赖主观感知。理论细筛通过：文章以Mehrabian沟通理论为kernel theory，从理论命题推导出meta-requirements和metadesigns，两阶段LSTM、基础vocal cues等设计选择均由理论对非言语沟通和认知/情绪机制的解释所指导，并通过与多个消融/基线的客观指标比较直接检验。
- Confidence: 0.98

## Effectiveness of Location-Based Advertising and the Impact of Interface Design

- Year/journal: 2020 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2020.1759922
- Metrics: coupon click rate; coupon choice probability; clicks
- Objective evidence: 文章核心目标是量化界面设计（距离排序、距离信息）对位置优惠券有效性的影响，有效性主要通过点击率衡量；通过随机字段实验比较四个实验组的平均点击率，发现距离排序组的点击率显著更高（如Group 3为1.53%，Group 1为1.42%，随机排序组更低），并用分层贝叶斯logit模型估计距离、显示排名及其交互对点击选择概率的影响
- Artifact: 基于位置的服务移动应用（location-based coupon pull smartphone application） — 应用内优惠券界面的两个核心设计要素：1）距离信息的提供与否；2）优惠券的排序机制（按距离排序 vs 随机排序）
- Theory: Choice architecture; Overconfidence (过度自信); Search costs and ranking effects (搜索成本与排序效应); Distance/transportation costs (距离与交通成本); Primacy effect (首因效应); Trade-off contrast (权衡对比); Context-dependent choice (情境依赖选择)
- Theory-to-design: 文章以选择架构（choice architecture）为总体框架，认为界面设计会系统影响用户选择。具体链条包括：(1) 过度自信理论：当不显示距离信息时，用户会低估到达商店的交通成本，因此距离排序且不显示距离的界面（Group 3）会比显示距离的界面（Group 1）获得更高点击率；(2) 搜索成本与排名效应：距离排序可降低用户搜索成本，同时高排位因首因效应获得更多注意，因此距离排序界面优于随机排序界面；(3) 交通成本理论：距离越远，用户感知交通成本越高，因此距离对点击有负向作用；(4) 权衡对比和情境依赖：随机排序下相邻优惠券距离差异更大，产生更强烈的对比效应，影响距离敏感度。这些理论在实验设计之前就用于推导四个实验组的界面特征，并在结果部分用于解释和验证不同设计下点击率的差异。
- Decision: 基础筛选通过：文章以点击率这一客观行为指标为最终目标和核心贡献，并通过随机字段实验修改了位置优惠券应用的两个明确界面设计要素（排序机制、距离信息），验证了客观指标改进。理论细筛通过：文章在选择架构、过度自信、搜索成本、交通成本、权衡对比等心理学相关理论的指导下，前瞻性地推导并设计了界面特征（距离排序、是否显示距离），并通过客观点击率数据和模型交互项直接检验了理论—设计链。
- Confidence: 0.97

## Interleaved Design for E-Learning: Theory, Design, and Empirical Findings

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2023/17206
- Metrics: Posttest score（实验后在线阅读理解测验分数，100分制）; Topic mastery（HMM估计的主题掌握概率）; Session accuracy（练习答题正确率）
- Objective evidence: 文章明确提出研究目标是提高 e-learning 学习表现，设计科学框架中的可检验假设 H1/H2 都以学习表现为结果；现场实验的模型自由证据和回归分析均以 posttest score 为主要因变量，结果显示 related-interleaving 相比 unrelated-interleaving 高约10分、相比 non-interleaving 高约7分，验证了核心贡献。
- Artifact: 个性化在线学习系统（personalized e-learning system / e-learning platform） — 文章设计并实例化了整个 e-learning 系统，核心可辨识部分包括：基于 hidden Markov model 的弱主题检测模块、基于专家知识和模糊关联规则的知识地图主题相关性建模模块、以及实现相关交错会话设计的调度引擎；研究团队还开发了供学习者提交练习和接收反馈的系统界面与流程。
- Theory: Cognitive Load Theory (CLT，认知负荷理论)
- Theory-to-design: 文章以 CLT 为 kernel theory：工作记忆有限，基本加工消耗过多会挤占图式建构资源；交错学习增加基本加工负荷，而提高交错主题的相关性可让学习者复用已有图式、降低基本加工负荷，同时保留对比和联系不同主题的图式建构机会。由此提出 related-interleaving 设计，并转化为元需求：动态检测弱主题、增加同一学习会话中弱主题的相关性、用调度引擎按弱主题和相关性命中安排练习。调度引擎优先选择知识地图上存在依赖关系的未掌握主题，正是 CLT 推导出的设计选择；H1/H2 也由该理论链条推出。
- Decision: 基础筛选：文章以 posttest score 等客观学习表现指标为最终目标和核心贡献，并通过设计、实例化和现场实验评价一个个性化在线学习系统及相关联的交错会话设计来实现该提升，因此通过基础筛选。理论细筛：cognitive load theory 作为 kernel theory 前瞻性地推导了 related-interleaving 的设计特征、元需求和调度引擎设计，且该理论指导的设计通过现场实验和间接机制检验得到支持，因此通过理论细筛。
- Confidence: 0.97

## The Attraction Effect in Crowdfunding

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1152
- Metrics: 选择目标高价奖励的概率; 目标奖励选择比例; backers' choice proportion
- Objective evidence: 文章核心目标是检验吸引效应在众筹情境中能否将支持者从低价选项推向高价选项，所有研究均以此为主要贡献；摘要中报告选择比例提升18.8%-28.2%，各实验和实地研究均显著。
- Artifact: 数字奖励菜单（digital reward menu），作为奖励型众筹平台（如Kickstarter）上的软件界面组件 — 在奖励菜单中插入诱饵奖励选项，具体包括价格诱饵（价格略高、质量相同）或质量诱饵（质量略低、价格相同），以形成不同的选择集。
- Theory: Salience Theory (Bordalo et al., 2012, 2013)
- Theory-to-design: 理论命题：根据显著性理论，决策者会比较各选项的属性值与参考值，属性越显著权重越高；当质量-价格比高于参考值时质量显著，低于参考值时价格显著（第3节）。心理机制：加入诱饵选项会降低参考奖励的质量-价格比，使目标奖励的质量变得显著，从而增加目标吸引力。设计选择：基于该理论，作者设计了两种诱饵（价格诱饵和质量诱饵）并将其插入数字奖励菜单。预期改善的客观指标：选择高价目标奖励的概率上升。文章通过实验比较无诱饵和有诱饵条件，验证了该理论链条。
- Decision: 基础筛选：文章以可客观测量的选择比例（选择高价奖励的比率）为最终目标和核心贡献，通过设计/修改数字奖励菜单（在菜单中加入诱饵选项）实现该提升，因此通过。理论细筛：文章明确基于显著性理论（salience theory）前瞻性推导了诱饵选项的设计（价格诱饵和质量诱饵）及预期效果，并在实验中用客观选择指标验证该理论指导的设计，因此通过。
- Confidence: 0.97

## Using Design-Science Based Gamification to Improve Organizational Security Training and Compliance

- Year/journal: 2020 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2019.1705512
- Metrics: 实际钓鱼响应行为（是否点击钓鱼邮件链接）; 钓鱼成功比例
- Objective evidence: 文章的核心目标是通过游戏化培训改善员工安全合规，尤其提升防钓鱼行为；在六个月的现场实验中，以实际钓鱼响应作为最终行为结果，结果表明游戏化组被钓鱼比例为27.3%，显著低于对照组44.7%和邮件组39.7%（Z检验显著），直接支撑了系统的核心价值主张
- Artifact: 基于Web的游戏化安全培训系统（custom Web-based gamification application） — 整个游戏化培训系统，包括用户注册与登录、头像选择、游戏大师（gamemaster）提示、积分系统、怪物奖励、青铜/白银/黄金等级、排行榜、每两周更新的分轮测验与安全知识内容
- Theory: Hedonic-Motivation System Adoption Model (HMSAM); Flow Theory; Cognitive Absorption Theory; Theory of Reasoned Action (TRA); Theory of Planned Behavior (TPB)
- Theory-to-design: 文章以HMSAM为DSR kernel theory，提出设计原则：设计原则#1要求系统通过游戏元素增强员工动机和满足感，设计原则#2要求通过有意义而有趣的学习过程提供新知识。具体而言，依据Flow理论中实现沉浸的三个条件（清晰目标、明确反馈、挑战与技能平衡），系统设计了积分、排行榜、等级、游戏大师反馈等游戏化元素，提供清晰目标和即时反馈；并根据挑战-技能平衡理论，设计了递进式挑战，且通过倒U假设和实证检验了“适当挑战”对沉浸的影响。该理论链条最终指向预期改善实际防钓鱼行为
- Decision: 基础筛选：通过。文章以实际防钓鱼行为（是否点击模拟钓鱼邮件链接）作为最终目标和核心贡献，并进行组间比较验证；同时明确设计并开发了一个自定义的Web游戏化安全培训系统，该系统是客观行为改善的直接载体。理论细筛：通过。文章以HMSAM（融合心流理论、认知吸收等）作为内核理论，前瞻性地指导系统游戏化元素的设计，并通过结构方程模型和对照实验检验了理论驱动的设计是否改善客观防钓鱼行为，形成了完整理论到设计再到客观指标的链条。
- Confidence: 0.97

## 1 + 1 > 2? Information, Humans, and Machines

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2023.0305
- Metrics: default rate; nondefault rate; equalized opportunity ratio (EOR)
- Objective evidence: 文章的核心问题是人类与机器协作能否提高最终贷款审批绩效，主要贡献在于发现同时具备大信息量和机器解释时，人机协作使默认率从5.15%降至3.13%（降低2.02%，显著），是该设计成功的核心证据；公平性EOR作为辅助客观结果，同样用于说明协作价值。
- Artifact: 人机协作贷款审批决策支持系统（包含机器学习预测模型、SHAP解释展示模块和两阶段人类决策流程） — 设计了机器建议模块（训练XGBoost模型）、机器解释模块（SHAP特征重要性及数值对比信息），以及在现有贷款审批平台中嵌入两阶段决策流程：人类先独立决策，再显示机器建议和解释，人类可调整最终决策。
- Theory: Dual-process theories of reasoning; System 1/System 2 theory (Evans 2003, Kahneman 2011)
- Theory-to-design: 理论命题指出激发System 2需要两个条件：任务复杂性和有用线索。文章据此推导：信息复杂度（大信息量）能吸引注意、激发参与；机器解释作为结构化参考线索，能促使个体重新评估决策。这一推导直接决定了软件系统中的两个设计选择——向评估者提供大信息量数据，以及展示机器建议和解释。理论预期该组合可激发人类主动反思，从而降低违约率，该预期通过组8（大信息量+解释）相对组4的违约率下降得到验证。
- Decision: 基础筛选通过：文章以客观违约率等指标提升为核心贡献，并通过设计包含机器预测、机器解释展示及两阶段人机协作流程的软件系统实现该提升。理论细筛通过：双过程理论实质指导了信息复杂度和机器解释这两项软件设计特征，并用客观违约率指标检验了理论预期。
- Confidence: 0.96

## Fun Shopping: A Randomized Field Experiment on Gamification

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1147
- Metrics: Money（购物支出）; Distance（购物距离）; StoreVisits（店铺访问次数）
- Objective evidence: 论文的核心研究问题是 gamification 能否促进消费者购物参与，并将支出、距离、店铺访问作为主要结果变量；在随机现场实验中，通过 Tukey 检验和平均处理效应回归（Table 5, Table 6）验证了 Badge、Leaderboard、Coupon 对三个指标在治疗期有显著正向影响，并评估了治疗后期的持续效应，这些指标是衡量所设计方案成功与否的主要依据。
- Artifact: 基于位置技术的游戏化购物参与信息系统（location-based gamified shopping engagement environment），由 Wi-Fi 定位、微信/购物门户推送和移动程序页面构成。 — 数字徽章收集页面（私有访问、按九大品类收集）、公开排行榜页面（按行走距离和店铺访问积分实时排名）、数字优惠券投递界面（一次性使用的 QR 码），以及相应的后台规则与推送机制。
- Theory: 自我决定理论（Self-Determination Theory, SDT）; 社会比较理论（Social Comparison Theory, SCT）
- Theory-to-design: SDT：理论命题是满足能力、自主和归属需要能促进内在动机；文章由此将徽章设计为私有的、无货币价值的数字收藏品，以提供能力反馈、自主选择和环境联结，驱动消费者购买相应品类/探索商场，预期提高客观购物指标（支出、距离、店铺访问）。SCT：理论命题是个体通过社会比较进行自我评估；文章由此将排行榜设计为公开的、实时刷新的积分排名，以激发向上/向下比较和竞争感，预期促进消费者增加行走距离、访问更多商店和增加消费。两条推导链在 Section 2.2、2.3 和 2.4 中形成，并转化为 Section 3.1 的具体实验设计。
- Decision: 基础筛选通过：论文核心目标是提升购物支出、行走距离和店铺访问次数等客观行为指标，并通过随机现场实验验证这些提升；其软件制品为基于位置技术的游戏化购物参与系统，包含徽章、排行榜和优惠券等明确功能模块，属于可运行数字系统，并通过这些客观指标评价。理论细筛通过：自我决定理论和社会比较理论被用来前瞻性地推导徽章（私有、无货币价值）和排行榜（公开、实时排名）的设计，并指导具体设计选择；通过随机实验的客观购物指标直接检验了这些理论指导的设计。
- Confidence: 0.96

## Social influence tactics in e-commerce onboarding: The role of social proof and reciprocity in affecting user registrations

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113268
- Metrics: user registration; confirmed user registration
- Objective evidence: 文章的研究问题、假设和贡献均围绕用户注册行为展开，用户注册是核心因变量。研究1的二元Logistic回归显示货币化互惠和社会认同对注册有显著主效应及交互效应；研究2的大型随机田野实验显示效用型互惠和社会认同对确认注册有显著主效应及交互效应，文章据以提出设计建议。
- Artifact: 电商平台用户引导界面（e-commerce onboarding interface） — 研究1自建的虚构电商平台Watch24中的欢迎层和注册层：欢迎层呈现货币化互惠（折扣券）提示，注册层呈现社会认同（已有100万用户注册）提示；研究2真实电商平台Chrono24的注册浮层：在浮层中增加效用型互惠（免费手表选购指南）文本和社会认同（最近30天有2万用户注册）文本。
- Theory: 社会影响理论（Social Influence Theory, Cialdini）; 互惠规范/社会交换理论（Norm of Reciprocity/Social Exchange Theory）; 社会认同与从众/乐队花车效应（Social Proof/Bandwagon Effect）; 心理抗拒理论/说服知识模型（Psychological Reactance/Persuasion Knowledge Model）
- Theory-to-design: 互惠规范→提供前置利益会引发回报义务感→设计为欢迎层中的折扣券或注册浮层中的免费指南→预期提高注册率；社会认同→不确定性下人们参照他人行为→设计为注册界面显示已有大量用户注册→预期提高注册率；心理抗拒/说服知识→货币化互惠与社会认同叠加会增强用户对操纵的警觉和审视→预期社会认同抵消货币化互惠的作用；效用型互惠因其真诚、非侵入性，社会认同作为放大信号→预期社会认同增强效用型互惠的作用。
- Decision: 基础筛选通过：文章以用户注册这一客观行为指标为最终目标和核心贡献，并通过设计/改造电商用户引导软件界面中的互惠提示和社会认同提示来实现并验证该指标提升。理论细筛通过：社会影响理论、互惠规范和社会认同等心理学相关理论在实验设计前实质性地推导了具体的界面设计元素和交互预期，并通过客观注册指标直接检验。
- Confidence: 0.96

## A Warning Approach to Mitigating Bandwagon Bias in Online Ratings: Theoretical Analysis and Experimental Investigations

- Year/journal: 2023 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00817
- Metrics: DDAR (Distance to the Displayed Average Rating); individual rating bias level
- Objective evidence: 文章的核心目标是设计警告策略以减轻bandwagon bias，DDAR是检验所有研究假设的主要因变量，用于比较不同警告组与控制组、无警告组的差异。主要实验和三个补充实验均以DDAR为依据，结果支持H1/H2/H3a/H4等预期，验证了所设计警告策略对降低评分偏差的改进。
- Artifact: 在线评分系统中的警告信息/警告弹窗（warning message/pop-up）作为软件制品的一部分 — 警告策略的内容设计，包括两种具体实现：直接警告（风险警报）和带排序任务的警告（风险警报+排序任务）。
- Theory: Flexible Correction Model (FCM); Theory of Valuation in Behavioral Economics (Coherent Arbitrariness)
- Theory-to-design: 文章用FCM预测：风险警报使个体感知偏差存在并知道方向，但缺乏程度信息，导致在无偏差时过度调整；理论推导出需要提供关于基线评价的额外信息。结合估值理论中的'coherent arbitrariness'（绝对评估易受影响，但相对评估稳定），设计出排序任务，让用户通过相对排名推断自身基线评分，从而改善对偏差存在和程度的感知。该理论链直接确定了'风险警报+排序任务'这一警告内容设计，预期改善DDAR指标。
- Decision: 基础筛选通过：文章以DDAR（个体评分与显示平均评分的绝对距离）作为核心客观指标，验证所提出的警告策略能减轻在线评分中的从众偏差；该警告策略被明确作为在线评分系统内的软件制品组成部分（警告信息/弹窗）进行设计并接受实验评价。理论细筛通过：文章基于Flexible Correction Model和行动经济学估值理论推导出'风险警报+排序任务'警告内容设计，并形成从理论到心理机制、具体制品设计和客观指标的完整链条，且用对照实验直接检验了该设计。
- Confidence: 0.95

## Achieving a Balance Between Privacy Protection and Data Collection: A Field Experimental Examination of a Theory-Driven Information Technology Solution

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2021.1045
- Metrics: Actual disclosure behavior (number and sensitivity of disclosed personal information); Quantity of disclosed information; Sensitivity score of disclosed information; Negotiation success rate
- Objective evidence: 文章的核心目标是设计一种兼顾隐私保护与数据收集的信息技术方案；摘要明确指出该方案降低隐私担忧并提高消费者信息披露意愿和实际披露行为。第5.3节的行为分析显示，active-recommendation特征显著提高实际披露行为，且App 3比传统隐私声明和仅有协商功能的App 2产生更多和更敏感的披露信息，表6也给出数量与敏感度的稳健结果，因此客观指标是文章的核心贡献验证依据。
- Artifact: Web-based mobile banking applications (prototype IT solutions) — 移动银行应用中的隐私政策功能模块：包含非协商隐私声明、协商但非主动推荐隐私政策、以及协商加主动推荐隐私政策三种应用；核心设计包括隐私偏好评估、个性化隐私政策推荐、用户界面下拉框选择、协商工作流和服务代理模块。
- Theory: Justice theory (Adams 1965; Culnan and Bies 2003); Westin's Privacy Segmentation Index
- Theory-to-design: 正义理论认为，程序正义、互动正义和分配正义会影响消费者对公平的感知，进而降低隐私担忧并促进信息披露。文章据此推导：传统隐私声明只提供程序正义，缺少互动正义和分配正义；因此设计协商功能以提供互动正义，即消费者与服务代理双向交互、表达隐私偏好并商定信息披露；同时设计主动推荐功能以提供分配正义，即根据消费者的异质隐私偏好类别主动推荐个性化隐私策略，使不同消费者按自己认为公平的投入产出比披露信息。这一理论-设计链最终指向降低隐私担忧、提高信息披露意愿和实际披露行为。
- Decision: 基础筛选通过：文章以实际信息披露行为、披露数量与敏感度等客观指标作为核心验证依据，并通过设计和开发三种移动银行隐私政策应用来实现改进。理论细筛通过：正义理论（及其中的程序、互动、分配正义）和Westin隐私偏好分类实质性地指导了协商和主动推荐两个设计特征的生成，并通过实地实验得到直接检验。
- Confidence: 0.95

## Animation as a dynamic visualization technique for improving process model comprehension

- Year/journal: 2021 / Information & Management
- DOI: 10.1016/j.im.2021.103478
- Metrics: problem-solving test score; process model comprehension performance
- Objective evidence: 文章的核心贡献是检验动画能否提升过程模型理解，因变量即问题解决测试分数；OLS 回归显示 Ananimation 系数显著为正（β=44.559, p<.001），支持 H1，并用同一分数验证了专业水平的 U 型调节作用。
- Artifact: 自适应动画环境（adaptive animation environment），一个在线过程模型可视化与实验工具 — 在静态 BPMN 过程模型上叠加的动态可视化特征（颜色转换、活动状态变化、时间顺序设计）以及两级交互功能（低交互连续视频、高交互逐步动画与用户可控切换）和自适应机制。
- Theory: Cognitive Theory of Multimedia Learning; Cognitive Load Theory; Cognitive Dimensions Framework; Expertise Reversal Effect; Signaling Principle; Attention Guidance Mechanism; Worked Example Principle; Segmentation Principle; Interactivity Principle; Congruence Principle
- Theory-to-design: 文章建立从理论到设计再到指标的链条：例如，基于认知负荷理论识别过程模型理解中的认知挑战；基于多媒体学习理论的 signaling principle 和 attention guidance mechanism，采用颜色变换逐步高亮相关元素，以降低认知负荷并引导注意力，从而提升问题解决测试分数；基于 worked example principle 和 segmentation principle，为新手提供低交互连续动画和暂停控制；基于 interactivity principle 和 expertise reversal effect，为高经验用户提供高交互逐步动画，使其能自行探索替代流程；低/高交互的适应用户在视频结束后自动切换到交互模式并可回退。这些设计选择均由特定理论命题推导，并用客观测试分数通过实验比较静态与动画组来检验。
- Decision: 基础筛选：文章以过程模型理解测试得分（0-100 的正确率）为最终目标，通过随机实验比较动画与静态展示，证明动画组得分显著提升，该指标由专家确定的正确答案和明确规则评定，不依赖主观感受；所设计的自适应动画可视化环境是明确的软件制品，其视觉与交互特征均是解决方案实质，且用该客观指标进行检验。因此 base_match=true。理论细筛：文章明确以认知负荷理论、多媒体学习认知理论、认知维度框架等多个人类认知与学习理论为设计依据，从理论命题推导出动画的颜色信号、低/高交互性等具体设计选择，并用客观测试分数通过实验验证这些理论指导的设计，满足理论实质指导软件制品设计的要求。
- Confidence: 0.95

## Attending to Customer Attention: A Novel Deep Learning Method for Leveraging Multimodal Online Reviews to Enhance Sales Prediction

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2021.0292
- Metrics: RMSE; MAE
- Objective evidence: 文章的核心目标正是提出一种更好的多模态评论销售预测方法，并以RMSE/MAE为主要成功指标。在若干实验（Experiment 1-4）中，DTV-AMI在多个时间跨度和评论类型下均优于基线与基准方法，例如在集成特征实验中最佳RMSE从7.04%降至5.32%，改进显著（见Table 5）。
- Artifact: 深度学习预测模型（DTV-AMI） — 整个DTV-AMI模型，包括四个注意力机制（时间性、语义多样性、投票意识、自适应多模态交互）、双模态GRU基础结构、以及多模态嵌入提取与融合模块。
- Theory: 双过程理论（dual-process theory，Groves & Thompson 1970）; 选择效应（selection effect，Li & Hitt 2008）; 信息处理理论（information processing theory，McGuire 1968）; 消息学习理论（message learning theory，Riley 1954）; 精心可能性模型（elaboration likelihood model，Petty & Cacioppo 1986）
- Theory-to-design: 文章在Section 3中分别用这些理论推导设计：1）双过程理论认为顾客快速自动注意新信息，从而设计时间性注意力机制，给近期评论更高权重；2）选择效应指出顾客偏好多样化的产品属性，促使关注语义多样性评论，进而设计语义多样性注意力机制；3）信息处理与消息学习理论表明顾客会注意获得投票的评论，从而设计投票意识注意力机制；4）精心可能性模型认为文本和图像通过不同说服路径影响顾客，因此设计自适应多模态交互注意力机制。这些理论直接决定了注意力权重的计算方式（如方程6、7中的时间衰减与投票加权项）。
- Decision: 基础筛选：文章以预测误差（RMSE/MAE）为客观指标，并通过设计深度学习模型DTV-AMI实现该指标的显著改善，明确属于软件制品设计与评估，故通过。理论细筛：文章使用多个心理学相关理论（如双过程理论、精心可能性模型）明确推导了模型中的注意力机制设计，并通过实验验证这些设计组件有效，故通过。
- Confidence: 0.95

## Augmenting Password Strength Meter Design Using the Elaboration Likelihood Model: Evidence from Randomized Experiments

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1125
- Metrics: diff_strength (log-transformed increase in password strength); num_reset (number of immediate password revisions after seeing the meter); learn_more (clicking the password tips link; secondary)
- Objective evidence: 论文将“促使安全密码行为”“提高密码强度”作为最终目标和核心贡献；研究2和3分别使用随机对照实验室实验和实地实验，以传统密码强度计为对照，采用回归分析和ANOVA检验，结果显示尤其Rank处理显著提高diff_strength和num_reset。
- Artifact: 增强型密码强度计，作为嵌入Web注册流程的软件界面组件；在实验室和实地系统中均实现为网页端软件功能。 — 密码强度计中的警告消息/信息呈现组件，即在原有强度标签基础上增加三种类型说服性消息（恐惧诉求/时间、同伴比较/排名、共同纽带/概率），并保持强度计算算法和生成标签完全一致。
- Theory: Elaboration Likelihood Model (ELM)
- Theory-to-design: ELM命题：经过中心路径加工的信息容易引发更显著、更持久的行为改变；而边缘路径引起的改变通常短暂且表面。论文由此推导密码强度计是说服工具，传统的视觉刺激主要走边缘路径，因而效果有限；进而提出使用恐惧诉求、同伴比较和共同纽带三类刺激来唤起用户的认知思考，使消息进入中心路径，最终提升密码行为。该链条从理论到心理机制、再到具体界面消息设计和客观密码强度指标完整清楚。
- Decision: 基础筛选通过：文章以客观可测量的密码强度提升和密码修改次数增加作为最终目标和核心贡献，不受主观感知影响；同时通过设计并实现增强型密码强度计这一明确软件界面组件来实现改进。理论细筛通过：ELM是明确的心理说服理论，并前瞻性地指导了消息呈现设计，设计链条从ELM命题、认知加工机制到密码计界面消息再到客观行为指标完整可追溯，且被随机实验客观检验。
- Confidence: 0.95

## Augmenting Social Bot Detection with Crowd-Generated Labels

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1136
- Metrics: Precision; Recall; Macro-F1; Micro-F1; AUC; 检测率（给定消息数量或众包标签数量下的检测比例）
- Objective evidence: 文章的核心贡献是提出并验证利用众包反应的bot检测框架；通过与传统方法对比（Table 6）、消融实验（Table 7）和模拟实验（Table 8、9、10）证明增强模型在F1、AUC、检测率等指标上的提升，这些指标直接支撑其核心主张。
- Artifact: 社交机器人检测系统（computational system），包含文本分类器、特征矩阵和检测流程。 — 整个检测框架：包括BERT嵌入、主题分类器、情感分类器、言语行为分类器、时序相似度特征、以及将这些特征拼接用于最终随机森林等分类器的特征矩阵。
- Theory: Speech Act Theory (Searle 1969; Austin 1962)
- Theory-to-design: 理论命题：用户的言论不仅传递内容，还执行不同的言语行为（断言、承诺、宣告、指令、表达），不同行为反映不同的确定性/意图。心理/行为机制：用户声称发现机器人时其表达的确定性和意图不同（如'我确定这是机器人' vs '能否有人验证这是否是机器人？'）。软件制品设计选择：文章基于该理论设计了言语行为分类器，将用户回复划分为五类，并将每类比例作为特征加入最终检测系统的特征矩阵（Table 5中的SA1–SA5）。预期改善的客观指标：通过加权/选择更高确定性的众包标签，增强bot检测的分类性能。消融实验（Table 7，排除speech acts）证明了该理论指导的特征带来了性能提升。
- Decision: 基础筛选通过：文章以提升社交机器人检测的客观分类性能（Precision、Recall、F1、AUC等）为最终目标和核心贡献，通过设计并实现一个融合众包反应的深度学习检测系统来实现，该系统具有明确组件（BERT分类器、特征矩阵等），并在真实Reddit数据上进行了客观评测。理论细筛通过：言语行为理论作为可识别的心理学/行为科学相关理论，被前瞻性地用于设计众包反应可信度的评估机制，形成从理论命题到心理机制、具体软件设计特征（言语行为分类）和客观检测指标的完整链条，并通过消融实验验证。
- Confidence: 0.95

## Automating in High-Expertise, Low-Label Environments: Evidence-Based Medicine by Expert-Augmented Few-Shot Learning

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2024/18573
- Metrics: Sentence classification P@N; Sentence classification R@N; Sentence classification F1@N; Precision-Recall Curve (PRC); Sequence tagging word-level F1@N; BERTScore-based F1@N; Sequence tagging PRC; SR project time / cost reduction; SR report completeness in case study
- Objective evidence: 论文的核心贡献是FastSR在低标注、高专业环境下对SR数据抽取的客观性能提升。文章以多个基线和消融实验验证了改进：WD句子分类F1@3达到73.00%，显著高于ProtoNet的65.40%和GPT-4的39.23%；序列标注F1@3为60.79%，高于ProtoNER的57.17%；COVID和EBM-NLP上也一致领先。SR案例报告显示FastSR比人工SR节省约65%的时间、约73,500美元成本，并在报告完整性上更接近专家结果。
- Artifact: 机器学习/NLP软件工具：FastSR few-shot learning framework，属于计算设计科学制品。 — FastSR的端到端可运行架构，包括BioBERT+CNN句子语义表示、全局上下文表示模块（预训练段落分类器+pointer network）、基于注意力的PICO片段表示、fragment-attended query表示、共享原型和联合学习机制；以及FastSR-augmented SR流程。
- Theory: Compositionality theory (semantic compositionality); Human sensemaking framework
- Theory-to-design: 论文从compositionality theory出发：人类可以从有限样例中组合性地建构复杂语义，因此低标注SR环境中的自动化方案应模拟该组合学习能力。具体链条为：理论命题→心理/认知机制→设计选择→预期客观指标。‘理论命题：丰富概念可由简单部分组合而成’→‘人可从少数样例高效学习’→DR1：采用FSL/ProtoNet；‘理解复杂表达的语义需要局部/全局语境’→DR2：设计上下文句子表示和全局上下文原型；‘人类语义感知强调语义对应而非词汇精确匹配’→DR3：设计注意力机制构造PICO片段表示；‘语义/语境/医学知识需协同迭代标注’→DR4：通过共享片段原型和联合损失实现句子分类与序列标注协同学习。最终用F1、PRC、BERTScore和SR时间节省检验该链条。
- Decision: 基础筛选通过：论文以FastSR为明确软件制品，以句子分类/序列标注的P@N、R@N、F1、PRC、BERTScore以及SR时间/成本节省作为最终目标和核心贡献，并在多数据集和真实SR工作流中验证，满足要求A和B。理论细筛通过：论文使用compositionality theory和sensemaking从认知角度前瞻性地推导出四项设计需求，并将其落实为FSL、上下文表示、注意力机制和联合学习等具体软件设计组件；消融和基准实验直接检验了理论指导的设计部分，因此满足要求C。
- Confidence: 0.95

## Be Together, Run More: Enhancing Group Participation in Fitness Technology

- Year/journal: 2023 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00779
- Metrics: Activeness; group participation in running; participation rate
- Objective evidence: 文章核心研究目标是检验离线群体参与促进功能（Running Spot）是否提升群体参与跑步的程度，Activeness 是主要结果变量。研究采用准实验面板数据与 DID 方法，比较引入 Running Spot 前后处理组（spot groups）与对照组（non-spot groups）的 Activeness 变化，并配合倾向得分匹配缓解自选择问题。表4、表6、表7等结果均以 Activeness 作为因变量，证明了 Running Spot 对 Activeness 的正向影响及其调节效应。因此，该客观指标是文章最终目标和核心贡献的载体。
- Artifact: 跑步移动应用（fitness running app） — 应用内新增的“Running Spot”功能：指定特定跑步地点，并允许群成员看到同一群体中其他成员是否正在同一地点跑步。
- Theory: Psychological Distance Perspective; Relational Cohesion Theory
- Theory-to-design: 文章基于心理距离理论提出：Running Spot 通过指定共享跑步地点、减少成员之间的物理和时空距离，从而降低成员之间的心理距离；心理距离缩短促进非正式社会互动（离线群体参与）。进而基于关系凝聚力理论提出：重复社会互动通过“社会纽带过程”产生积极情感和关系凝聚力，以及通过“边界定义过程”减少不确定性；这两种心理过程最终导致群体参与跑步（承诺行为）。所以，理论推导链为：心理距离与关系凝聚力理论 → 心理距离降低和社会互动增多 → Running Spot 功能设计 → 群体参与度（Activeness）上升。该设计选择并非任意，而是由理论推导出的。
- Decision: 基础筛选通过：文章以客观指标 Activeness（群体参与跑步比例）的上升为最终目标和核心贡献，该指标来自应用后台的实际跑步记录，不依赖主观感知；文章通过设计或改造明确的软件制品——跑步应用中的 Running Spot 功能——来实现该提升，并用 DID/PSM 对该功能进行客观评价。理论细筛通过：心理距离理论和关系凝聚力理论实质指导了 Running Spot 功能的设计逻辑，形成了从理论到心理机制、再到具体设计特征和客观指标的完整推导链，并通过实证检验支持了理论预测。
- Confidence: 0.95

## Can Recommender Systems Reduce Healthcare Costs? The Role of Time Pressure and Cost Transparency in Prescription Choice

- Year/journal: 2020 / MIS Quarterly
- DOI: 10.25300/misq/2020/14435
- Metrics: view（是否查看系统推荐）; adjust（是否将初始处方调整为系统推荐的等效治疗方案）; 处方费用降低（由选择更低价等效药物所导致的成本节省）
- Objective evidence: 文章的核心研究问题是推荐系统能否通过提供成本透明信息降低处方成本，最终目标是在不牺牲疗效的前提下减少医疗支出；三个研究均以查看和调整推荐作为关键因变量，统计分析（描述统计、GEE模型、Heckman模型）用于验证推荐成本框架和时间压力对处方调整行为的影响。文章在讨论中还据此估计了潜在成本节省，因此该客观行为指标是文章最终目标和核心贡献。
- Artifact: 成本敏感的医疗推荐系统原型（基于电子病历处方场景的Web实验系统，使用Qualtrics动态实现） — 推荐系统的成本信息呈现方式：低成本（low-cost）推荐列表与混合成本（mixed-cost）推荐列表；系统在处方者选择初始治疗方案后显示等效替代药物及成本信息，并允许查看推荐和调整处方。
- Theory: Adaptation Level Theory (Helson 1947); Reference Price Effect (Rajendran and Tellis 1994); Appeal to Social Norms (Goldstein et al. 2008); Time Pressure and Information Processing (e.g., Wright 1974)
- Theory-to-design: 适应水平理论/参考价格效应 → 处方者以系统显示的药物成本为情境刺激形成内部参考价格 → 据此判断原选方案是否昂贵 → 设计了“只显示更低价替代方案”的低成本推荐设计和“同时显示高价与低价替代方案”的混合成本推荐设计 → 预期低成本框架降低内部参考价格，促使更多处方者采纳更低价等效药；混合成本框架通过高价选项抬高参考价格，可能降低低价推荐的采纳 → 采用view/adjust客观行为指标在低成本和混合成本两组间比较验证。时间压力理论亦被用于推导高时间压力下处方者可能过滤成本信息或使用简化规则，从而设计高/低时间压力条件考察系统使用行为的边界条件。
- Decision: 基础筛选：文章以设计并评估一个成本透明的医疗推荐系统原型为核心，通过系统记录的实际处方查看和调整行为，验证该系统能否降低处方成本；结果指标为客观行为记录，且是文章最终目标和核心贡献，因此通过基础筛选。理论细筛：适应水平理论/参考价格效应等心理学理论在实验设计之前被明确用于推导低成本与混合成本推荐呈现方式，并直接指导了系统推荐列表的设计；这些理论指导的设计又通过客观行为指标得到检验，因此通过理论细筛。
- Confidence: 0.95

## Could Gamification Designs Enhance Online Learning Through Personalization? Lessons from a Field Experiment

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1123
- Metrics: SRL engagement (self-regulated learning engagement); Learning efficiency (pace of module completion with SRL); Learning outcomes (knowledge test score, performance test score)
- Objective evidence: 文章的核心贡献是检验游戏化反馈与目标导向匹配是否提升SRL参与度、学习效率和学习成果。他们使用回归和Cox模型验证了匹配对SRL参与度和学习效率的显著作用，并通过中介分析显示SRL对学习成果有正向影响。
- Artifact: MOOC平台（KEEP, Knowledge & Education Exchange Platform） — 游戏化性能反馈功能，包括个人/社会比较反馈、正/负目标框架消息、徽章（master/loser badges）、排行榜/失败者榜、帮助榜/吝啬榜，以及相应的邮件提醒。
- Theory: Self-Regulated Learning (SRL) theory; Goal-Orientation theory (trichotomous framework); Gamification principles (e.g., personalization principle; Liu et al. 2017); Message framing (goal framing)
- Theory-to-design: 文章基于SRL理论强调性能反馈对支持目标导向行为的重要性，并基于目标导向理论区分学习者特质（掌握、表现趋近、表现回避），再根据游戏化原则推导出特定反馈设计（社会/个人比较×正/负框架）应与特定目标导向匹配。例如，表现回避目标的学习者因害怕负面评价，应接受积极框架的个人比较反馈以减轻焦虑并促进SRL。这些推导形成了假设H1-H3，并直接转化为平台中的反馈功能设计（如排行榜、徽章、邮件），预期改善SRL参与度、学习效率和成果。
- Decision: 基础筛选：文章以提升SRL参与度、学习效率和客观学习测试成绩为最终目标和核心贡献，这些指标均从系统日志、完成时间和测试评分获得，不依赖主观感知；文章通过修改MOOC平台，设计和实现了游戏化性能反馈功能（个人/社会比较、正/负框架），并使用这些客观指标评价了该软件改造。因此基础筛选通过。理论细筛：文章使用SRL理论、目标导向理论和游戏化原则前瞻性地推导了反馈设计，理论到心理机制再到具体设计选择和客观指标形成了可追溯链条，因此理论细筛也通过。
- Confidence: 0.95

## Designing Conversational Dashboards for Effective Use in Crisis Response

- Year/journal: 2023 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00801
- Metrics: Transparent interaction (behavioral navigation-step ratio); Efficiency (time to complete correctly solved information-finding tasks); Effectiveness (number of correctly solved information-finding tasks); NLP component performance (speech-to-text accuracy, entity extraction precision/recall/F1, intent mapping accuracy/F1, response time)
- Objective evidence: 文章研究问题和贡献陈述均以提升用户的透明交互以及信息查找效率、有效性为核心目标；DSR的测试性命题直接围绕透明交互提出；用户实验比较六种仪表盘版本，统计检验支持会话式仪表盘提升透明交互，且透明交互显著正向影响效率和有效性；结果在Table 6中汇总。
- Artifact: Conversational dashboard (交互式网页数据可视化仪表盘，带会话式用户界面) — 完整的会话式COVID-19仪表盘制品，包括仪表盘与数据可视化组件、交互管理组件、自然语言处理（NLP）组件，以及会话式引导模块（conversational onboarding）；同时设计/改造了用户可用的自然语言（口头/书面）和鼠标两种交互方式。
- Theory: Theory of Effective Use (TEU; Burton-Jones & Grange, 2013); Affordance theory (Gibson, 1977; Hartson, 2003); Enactive learning (Gupta & Bostrom, 2009; Gupta et al., 2010)
- Theory-to-design: TEU提出透明交互的两个驱动因素是适应(adaptation)和学习(learning)，据此导出MR1（调整表面结构，使用自然语言）和MR2（主动支持用户学习表面结构）。基于affordance theory，作者提出DP1（提供口头/书面自然语言交互）和DP2（允许用户在自然语言与鼠标之间选择），因为自然语言使界面可供性更容易实现，且不同用户和任务需要灵活选择。基于enactive learning，作者提出DP3（会话式引导），通过分步练习、观察反馈来帮助用户熟悉自然语言交互。这三个设计原则被实例化为会话式仪表盘的关键功能，并通过测试性命题预测其会提高透明交互，最终用用户实验中的客观导航路径指标进行检验。
- Decision: 基础筛选通过：文章的最终目标和核心贡献是提升用户在危机响应仪表盘中的透明交互以及信息查找效率、有效性，这些指标由系统日志和任务结果客观计算，不依赖主观感知；同时文章明确设计并实现了会话式仪表盘制品，包括仪表盘界面、NLP组件、交互管理和会话式引导。理论细筛通过：文章在设计前基于TEU推导元需求，并借助affordance theory和enactive learning推导三个设计原则，这些原则直接指导了仪表盘的软件设计，并通过用户实验中的客观指标得到检验。
- Confidence: 0.95

## Digital Institutionalization: The Case of E-Prescribing

- Year/journal: 2024 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00845
- Metrics: 电子处方错误数; 有至少一个错误的处方集比例; 违规错误总数
- Objective evidence: 文章的核心目标是设计新交换合同以提高电子处方质量，质量通过规则合规性衡量；实施前后的错误对比（表3）是论文评价干预效果的主要依据，并据此论证数字基础设施质量和制度化成功。
- Artifact: 电子处方数字基础设施中的交换合同（exchange contract），作为API契约和系统服务接口，包含XML schema、自动验证模块、错误反馈机制。 — 新交换合同（NEF），替代旧交换合同，废除网关，引入结构、数据、动态一致性和识别规则，并实现自动验证和错误状态报告。
- Theory: 言语行为理论（Speech Act Theory, Searle, 1969）; 制度理论（Institutional Theory, Barley & Tolbert, 1997; Thornton et al., 2012）
- Theory-to-design: Author 2受言语行为理论启发，将电子处方创建视为一种高质的通信行为（speech act），由此设计了规则系统，确保电子处方在创建时就合规；该规则系统被编码到新交换合同中（表2），并通过自动验证和反馈机制改变开具处方和配药实践。制度理论用于分析宏观制度环境（法规、标准）和数字制度化过程，指导交换合同作为脚本（script）的设计和实施，以合法化和制度化电子处方。具体设计链：理论命题→高质量通信行为需明确规则→设计结构/数据/动态一致性/识别规则→编码为新交换合同并自动验证→减少错误、提高合规性（客观指标）。
- Decision: 基础筛选通过：文章以电子处方错误数下降为最终目标和核心贡献，通过设计新交换合同这一明确软件制品（数字基础设施的一部分）实现，并以客观错误数据验证改善。理论细筛通过：言语行为理论和制度理论实质指导了交换合同规则的设计，并通过错误率下降得到直接检验。
- Confidence: 0.95

## From conflicts and confusion to doubts: Examining review inconsistency for fake review detection

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113513
- Metrics: Accuracy; Precision; Recall; F-score
- Objective evidence: 论文的核心贡献在于提出并验证了三种评论不一致性特征能够显著提升虚假评论检测性能。通过将不一致性特征加入基线特征集，对比加入前后的模型性能（表6和图3），证明加入后性能显著提升，并且敏感性分析（表7）确认这些特征在模型中具有重要性。
- Artifact: 虚假评论检测系统（fake OCR detection system） — 该系统由特征提取、评论不一致性分析、模型开发和敏感性分析四个主要组件构成。在本研究中，设计/修改的核心是加入了22个新颖的不一致性特征（评定-情感不一致、内容不一致、语言不一致），并将这些特征与原有特征一起输入分类模型。
- Theory: Truth-Default Theory (TDT); Leakage Theory of Deception; Attitude-behavior Consistency Theory
- Theory-to-design: 文章基于Truth-Default Theory中的一致性/连贯性原则，将评论不一致性划分为评定-情感、内容和语言三个维度，认为虚假评论更可能违反连贯性原则；基于Leakage Theory，虚假评论者在欺骗时会泄漏出不一致线索，因此不一致性特征能暴露欺骗；基于Attitude-behavior Consistency Theory，星级（态度）与评论内容（行为）应该一致，虚假评论者因缺乏真实体验更易出现态度-行为不一致。这些理论直接指导了22个不一致性特征的内容和测量方式，并将这些特征设计为检测系统的输入部分。文章还通过假设H1和H2明确将理论预测与特征设计及检测性能关联起来。
- Decision: 基础筛选：文章以提升虚假评论检测的客观性能指标（accuracy, precision, recall, F-score）为最终目标和核心贡献，通过设计并验证一个包含特征提取、不一致性分析等组件的虚假评论检测系统来实现，因此满足要求A和B。理论细筛：文章在提出特征之前，先引用了Truth-Default Theory、Leakage Theory of Deception和Attitude-behavior Consistency Theory，并依据这些理论推导出三类不一致性特征及假设，这些理论直接指导了软件制品中特征模块的设计，且通过客观指标检验了该设计，因此满足要求C。
- Confidence: 0.95

## Impact of Incentive Mechanism in Online Referral Programs: Evidence from Randomized Field Experiments

- Year/journal: 2021 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2021.1870384
- Metrics: invitation_converted; invitation_sent; accept_invitation
- Objective evidence: 文章的核心研究问题是哪种推荐激励设计能最有效地通过口碑提高产品采用，主要结果变量是转化数（invitation_converted）。在Experiment 1和Experiment 2中，Table 2和Table 5的OLS和Poisson回归显示equal-split和generous方案显著增加转化数，Table 6显示这两种方案显著提高被邀请者的接受概率，图4展示转换率；这些客观指标直接支撑文章的核心改进主张和贡献。
- Artifact: 移动社交游戏应用程序（Experiment 1为Hearsay，Experiment 2为Muquaabla） — 应用内的推荐奖励机制（奖励分配比例：自私/平分/慷慨）、调用-行动文案、提醒通知消息、邀请消息内容、邀请归属与奖励发放逻辑。
- Theory: Andreoni and Miller's altruism preference classification (CES: selfish, perfect substitutes, Leontief); Pro-social happiness effect (Dunn and Norton); Equity theory (Walster et al.); Metaperception theory (Laing et al.; Wirtz et al.); Rational choice theory
- Theory-to-design: 文章先从Andreoni和Miller的理论中提取三种偏好类型（自私、完美替代、Leontief），据此设计三种激励方案：自私（邀请者独享奖励）、平分（双方各半）、慷慨（被邀请者独享），并将这些分配比例实现在应用内的奖励设置中。Dunn和Norton的亲社会幸福理论以及公平理论分别支持慷慨和平分可能比自私更有效；元认知理论预测只给邀请者奖励会增加内疚感、降低发送意愿，因此应用在自私组不向被邀请者透露邀请者获得奖励。这些理论推导决定了应用内的具体激励结构、通知和消息内容，并预期影响发送数、接受率和最终转化数。
- Decision: 基础筛选通过：文章以应用日志记录的成功转化数、邀请发送数和接受率等客观行为指标为最终目标和核心贡献，通过修改移动社交游戏应用内的推荐激励方案（奖励分配比例、通知与消息内容）来实现这些改进，所有指标均由系统记录且直接用于验证设计效果。理论细筛通过：实验设计由Andreoni-Miller利他偏好理论、亲社会幸福理论、公平理论、元认知理论等心理学相关理论前瞻性推导，形成了从理论命题到具体应用内设计选择再到客观指标的完整链条，并通过随机实验直接检验，因此满足理论实质指导要求。
- Confidence: 0.95

## Improving Students’ Argumentation Skills Using Dynamic Machine-Learning–Based Modeling

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2021.0615
- Metrics: 客观论证质量 (Objective Quality of Argumentation); 跨领域论证技能迁移; 主观论证质量 (Subjective Quality of Argumentation)
- Objective evidence: 摘要和结论明确将客观论证技能提升作为最终目标；研究1中动态建模组客观论证质量均值 5.08 vs 脚本建模组 3.20 (p<0.001)；研究2中动态建模在复杂任务 (4.56 vs 2.87, p<0.001) 和简单任务 (3.70 vs 2.62, p<0.05) 均显著优于自适应支持；研究3中三个月后跨领域任务中动态建模组客观论证质量显著优于静态建模 (p<0.05) 和无建模 (p<0.01)。
- Artifact: 基于 Web 的动态机器学习论证建模学习系统 ArgueLearn — 整个系统被设计，包含服务导向架构中的四个模块：论证标注方案、标注语料库、基于 SVM 的论证挖掘模型、响应式学生中心界面；界面功能包括文本输入与动态反馈、claims/premises 高亮、论证结构图、可读性/连贯性/说服力仪表盘和解释。
- Theory: 社会认知理论 (Social Cognitive Theory, Bandura 1986, 2001); 行为建模 (Behavioral Modeling); 观察学习 (Observational Learning); 论证理论 (Toulmin Model)
- Theory-to-design: 文章从社会认知理论的核心主张出发：行为是自我生成与外部影响共同作用的结果，学习者可以通过观察可获得的动态行为模型获取替代经验。基于此，ArgueLearn 被设计为动态建模系统：通过 ML 对学生的论证结构进行实时分析，以高亮 claims/premises、图可视化、仪表盘和补充解释呈现个人化行为模型，并提供反复修改反馈的机会；该设计对应观察学习和 enactive learning 机制，预期能够提高学生文本中的客观论证质量。理论命题在 Hypotheses Development 中用于推导 H1-H4，并在系统实现中落实为具体功能。
- Decision: 基础筛选：文章以提高可客观计量的论证结构质量（支持性论点数量等）为最终目标，并通过设计、构建和评估 ArgueLearn 这一 ML 驱动的动态建模 Web 系统实现该目标，因此基础筛选通过。理论细筛：系统设计明确以社会认知理论为内核，从观察学习和行为建模机制推导出动态反馈、高亮、图可视化等具体设计选择，并用客观指标在三个实验中验证，因此理论细筛通过。
- Confidence: 0.95

## Managing Congestion in a Matching Market via Demand Information Disclosure

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2022.1148
- Metrics: NumberOfRequests; NumberOfHighRequests; NumberOfLowRequests; InitialMatches; EngagedMatches; InitialMatches/Request; EngagedMatches/Request
- Objective evidence: 文章的核心目标就是通过需求信息披露缓解拥堵并提高匹配效率；摘要、引言和第5节均以匹配请求量、匹配数量和‘matches per request’作为主要结果。表7-9显示Demand+Capacity Cue条件下高需求请求显著下降、低需求请求上升，且每次请求的初始匹配与深入匹配均显著提升。
- Artifact: 移动约会应用（mobile dating application Summer）的个人主页界面 — 在用户浏览他人个人主页时显示该用户过去30天收到的匹配请求数量，并根据实验条件附加‘受欢迎’或‘空闲/忙碌’的文本框架提示；这些信息被嵌入到应用版本3.5.2的个人主页UI中。
- Theory: Observational learning (Banerjee 1992); Fear of social rejection (Huston 1973; Shanteau and Nagy 1979; Stinson et al. 2015); Capacity constraints and availability signaling (Horton 2019); Message framing / salience (Tversky and Kahneman 1981; Roggeveen et al. 2006)
- Theory-to-design: 文章在第2.2-2.3节从理论上指出，需求信息同时具有‘质量/受欢迎程度’信号和‘容量/可响应性’信号：前者经由观察性学习可能加剧拥堵，后者结合社交拒绝恐惧和机会成本会促使用户避开高需求用户。为引导用户关注容量信号而非受欢迎信号，作者设计了容量框架提示（‘busy handling requests’/‘has time to handle requests’）与受欢迎框架提示（‘very popular’/‘not picked by many others’），并通过框架/显著性文献说明这种设计可以突出某一机制。该设计预期会降低对高需求用户的请求、提高每次请求的匹配成功率。
- Decision: 基础筛选通过：文章以客观可测的请求量、匹配量和匹配效率为最终目标，并通过修改移动约会应用个人主页UI中的需求信息展示与文本框架来实现；这些指标来自平台事件日志和实际匹配行为，不依赖主观评分。理论细筛也通过：文章使用观察性学习、社交拒绝恐惧、容量约束和框架效应等心理学相关理论，前瞻性地推导了容量提示与受欢迎提示的设计选择，并用客观匹配效率指标检验了该设计。
- Confidence: 0.95

## More Than a Bot? The Impact of Disclosing Human Involvement on Customer Interactions with Hybrid Service Agents

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2022.0152
- Metrics: Customer communication style (verbosity, complexity, density); Employee workload (frequency, duration, intensity)
- Objective evidence: 文章的核心贡献是揭示人类参与披露如何影响客户沟通风格并进而影响员工工作量，这些客观指标是研究的主要结果变量，也是判断披露效果的依据；随机现场实验和受控在线实验均报告了披露对沟通风格的显著影响以及沟通风格对员工工作量的显著影响，并通过假设检验和中介分析验证了该因果链
- Artifact: Hybrid service agent (AI-based chatbot combined with human employees behind a single chat interface) — 聊天机器人的交互消息和披露逻辑：在欢迎消息中增加人类参与披露（up-front HID）以及当员工介入时发送不同的披露消息（step-in HID）
- Theory: Audience design theory; Impression management theory (impression management concerns)
- Theory-to-design: 理论命题：人们会根据受众（包括潜在听众）调整沟通风格；当人类存在时，人们会产生印象管理担忧，并采取更符合社会规范的行为。设计推导：因为揭示人类参与使客户意识到员工可能在阅读或介入，所以应该在欢迎消息或员工介入时向客户披露人类存在（HID），以激活印象管理担忧和受众设计。具体的制品设计选择：在欢迎消息中加入“If I don't know the answer... my human colleague will read your message...”语句（up-front HID）以及在员工介入时发送“I will pass it on to my human colleague...”语句（step-in HID）。预期改善的客观指标：客户将采用更人类化的沟通风格（消息更长、更复杂、更多功能词），从而增加员工工作量（响应频率、时长和强度上升）
- Decision: 基础筛选通过：文章以客户沟通风格和员工工作量等客观指标的改变为核心贡献，并通过设计或改造hybrid service agent的披露消息和交互逻辑来实现。理论细筛通过：文章使用audience design theory和impression management theory前瞻性地指导披露设计，并通过中介分析验证了该理论的实质性影响。
- Confidence: 0.95

## Nudging Private Ryan: Mobile Microgiving under Economic Incentives and Audience Effects

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/16643
- Metrics: Donation decision (0/1); Donation amount (in dollars)
- Objective evidence: 文章的核心研究问题是移动微捐赠中经济激励与数字助推如何影响捐赠行为，结果部分以捐赠决策和捐赠金额作为主要结局变量；Table 4 报告了各组的捐赠率和平均捐赠金额，Table 5-7 以及附录 D 使用 logistic 回归和 Tobit 模型验证了处理组相对控制组、以及不同处理之间的显著改善。
- Artifact: Android 移动奖励应用（lock-screen rewards app）及其中的捐赠相关功能组件 — 在与应用提供商合作中，在应用内新增了用户可将奖励积分捐赠给慈善机构的功能；具体设计或修改的部分包括捐赠页面及其激励信息展示（rebate/matching 文案）、推送通知数字助推、实验2中的社交动态（social feed）可见性组件，以及奖励积分捐赠流程。
- Theory: 数字助推与选择架构（Thaler & Sunstein; Meske & Potthoff; Schneider et al.）; 受众效应/社会促进（Zajonc 1965; Andreoni & Bernheim 2009）; 社会期望与声誉动机（Ariely et al. 2009; Ellingsen & Johannesson 2008）; 温暖光芒/不纯利他主义（Andreoni 1988, 1989, 1990; Bénabou & Tirole 2006）; 框架效应（Eckel & Grossman 2003）; 前景理论中的损失/不对称认知效应（Kahneman & Tversky 1979）
- Theory-to-design: 理论命题：智能手机是私密且个人化的媒介，弱化了外部观众和社会期望；因此 offline 中 matching 依靠合作框架和 warm glow 的优势可能在移动环境中减弱，rebate 在低可见性下更有效。据此设计并比较 rebate 与 matching 两种经济激励形式。受众效应理论进一步指出，若将捐赠行为公开，matching 的相对优势会恢复；因此实验2增加 social feed 组件，使捐赠信息对同组用户可见。数字助推理论认为 push notification 是低成本、可忽略、不改变经济选项但能提高注意和显著性的选择架构干预；因此设计为向部分用户发送推送通知。这些设计选择均通过捐赠决策和捐赠金额的客观指标进行了检验。
- Decision: 基础筛选通过：文章以捐赠决策和捐赠金额等系统日志客观指标作为最终目标和核心贡献，并通过两轮大规模田野实验验证推送通知、rebate/matching 激励和社交动态可见性设计对捐赠的显著影响；同时，文章明确与移动应用提供商合作，在 Android 奖励应用中新增并修改了捐赠功能、捐赠页面、推送通知和社会动态组件，属于对明确软件制品组成部分的设计或改造。理论细筛通过：文章使用数字助推、受众效应/社会期望、温暖光芒/不纯利他主义等心理学相关理论，前瞻性地推导了 rebate vs matching、push notification、social feed 等具体软件设计选择，并通过客观捐赠指标对理论指导的设计进行了检验。
- Confidence: 0.95

## Overcoming Breakdowns in Customer-Chatbot Interaction: Design and Impact of Collaborative Repair Strategies

- Year/journal: 2026 / MIS Quarterly
- DOI: 10.25300/misq/2025/18742
- Metrics: Breakdown resolution rate; Immediate abandonment rate; Intent recognition score
- Objective evidence: 文章将“帮助顾客和聊天机器人解决故障”列为第一个可检验命题，并在自然主义现场实验中以 Breakdown resolution 为主要结果变量之一。该指标得到显著改善：协作式修复策略下故障解决率为38.23%，非协作式为32.41%，logistic回归系数 b=0.243, p=0.044；Immediate abandonment 从50.95%降至41.68%，b=-0.373, p=0.001。这些客观指标独立支撑了文章的核心改进主张。
- Artifact: 客户服务聊天机器人（基于意图的AI客服机器人），并包含配套的实时故障处理Web应用（Flask）。 — 在 InsurCo 客服聊天机器人中设计并实现的协作式修复策略，具体包括：故障类型分类器、自适应修复类型、自适应修复消息、实时故障处理Web应用，以及通过 webhook 和条件流程与聊天机器人后端集成的机制。
- Theory: Theory of Least Collaborative Effort (TLCE; Clark & Wilkes-Gibbs, 1986); TLCE-bot (TLCE 与 human-machine communication、customer service chatbot 文献的整合框架)
- Theory-to-design: 文章在 DSR 中明确以 TLCE 作为 kernel theory，通过概念整合提出 TLCE-bot 三原则：assisted self-repair、diagnostic transparency、proportionate effort。每条原则分别推导出元需求（如 self-repair primacy、breakdown transparency、progressive escalation），再转化为元设计的四个组件：故障类型分类、自适应修复类型、自适应修复消息、实时故障处理。例如，diagnostic transparency 原则要求修复消息包含解释元素和具体指导，而 proportionate effort 原则要求根据连续故障次数逐步升级修复方式。该理论—设计链条最终通过客观指标（Breakdown resolution、Immediate abandonment、Intent recognition score）获得检验。
- Decision: 基础筛选通过：文章以客观行为日志指标——Breakdown resolution 上升、Immediate abandonment 下降——作为核心贡献的主要证据，并在 InsurCo 客服聊天机器人中明确设计、实现了协作式修复策略的多个软件组件（故障类型分类器、自适应修复类型/消息、实时故障处理Web应用及后端集成）。理论细筛通过：TLCE/TLCE-bot 在设计前作为 kernel theory 实质指导了元需求、元设计和具体修复消息，形成了从理论命题、心理/行为机制到软件设计选择再到客观指标检验的完整可追溯链条。
- Confidence: 0.95

## Probing Digital Footprints and Reaching for Inherent Preferences: A Cause-Disentanglement Approach to Personalized Recommendations

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2023.0181
- Metrics: precision@k; MAP@k; NDCG@k; AUC
- Objective evidence: 文章的核心贡献是提出DISC推荐方法，其性能验证以这些客观排名/分类指标为主要依据；结果表明DISC在多个数据集和多种指标上显著优于基线。
- Artifact: 个性化推荐系统（recommender system）的推荐算法/推荐模块 — DISC模型：包含消费者行为（view/add-to-cart/purchase）的概率图建模、因果图、解耦表示学习、决策路径变量和EM推断的完整推荐方法
- Theory: Selective Exposure Theory; Social Influence Theory / Conformity; Behavioral Biases (nonstandard preferences, beliefs, decision making); Impulse Buying Theory
- Theory-to-design: 文章基于消费者行为理论，推导消费者在不同购物阶段的行为由内在偏好、物品显著性、从众效应共同驱动，并据此构建因果图结构和决策路径变量；该设计直接决定DISC如何从行为数据中解耦各因素，从而提供基于内在偏好的推荐，预期提升推荐准确率。
- Decision: 基础筛选：文章以DISC推荐方法为软件制品（推荐系统核心模块），以P/MAP/NDCG等客观指标为主要评估，并通过真实数据实验验证提升，因此基础筛选通过。理论细筛：文章使用消费者行为理论（如选择性暴露、社会影响、行为偏差）作为因果图设计依据，并客观验证了理论指导的组件，因此理论细筛通过。
- Confidence: 0.95

## Reciprocity or Self-Interest? Leveraging Digital Social Connections for Healthy Behavior

- Year/journal: 2022 / MIS Quarterly
- DOI: 10.25300/misq/2022/16177
- Metrics: Complete_Challenge (challenge completion rate); total running distance
- Objective evidence: 文章的核心贡献是展示互惠激励相较于自我利益激励能更有效促进健康行为，主要证据是比较Frnd-Recip组与对照组在挑战完成率和跑步距离上的显著提升（如完成率提高31.4%，匹配样本中跑步距离增加3.06公里等），这些客观指标是判断设计方案成功与否的主要依据
- Artifact: 移动社交跑步平台（RunningPlatform，为匿名而使用的代称） — 平台内的激励消息设计、金币奖励机制和挑战邀请/推送流程：包括按条件向接收者展示不同文案（Frnd-Recip/Frnd-SelfInt/Plat-SelfInt）、金币的归属（返还朋友/自己保留）、以及整个随机化配对和挑战过程
- Theory: Social Exchange Theory (SET); Reciprocity / gift exchange theory (互惠规范、感激与内疚机制)
- Theory-to-design: 基于SET，作者认为互惠激励中的收益不仅包括给朋友赢得奖励，还包括避免心理债务和表达感激，因此可能超过自我利益中的小奖励。据此设计了Frnd-Recip组：朋友作为发件人赠送金币，接收者完成挑战可获得金币返还给朋友；与Frnd-SelfInt组（金币自己保留）对照，从而操纵受益人来检验理论预期。对第二个假设，作者从SET推出社会亲近度会影响互惠获益：关系太远或太近都会降低心理债务/感激，所以设计在Frnd-Recip组中测量共同朋友数等作为亲近度指标，检验倒U型关系
- Decision: 基础筛选通过：文章以提升客观指标（挑战完成率、跑步距离）为最终目标和核心贡献，并通过设计/改造移动社交跑步平台中的激励消息和金币机制来实现。理论细筛通过：社会交换理论（及互惠、感激、内疚机制）实质性地指导了激励设计（互惠vs自我利益的对比）和社交亲近度条件的设计，且该理论指导的设计通过客观指标得到了检验。
- Confidence: 0.95

## Roles of Feedback and Phishing Characteristics in Antiphishing Training Performance: Perspectives of Goal Setting and Skill Acquisition

- Year/journal: 2024 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00854
- Metrics: Decision Avoidance; Detection Accuracy
- Objective evidence: 文章的核心目标是识别影响决策回避和检测准确率的因素，并检验不同反馈设计和钓鱼特征对这些客观绩效的影响。四个实验均以决策回避和检测准确率为主要因变量，通过ANCOVA或GEE验证假设，如实验1发现示例式反馈组检测准确率显著高于正念式反馈组（M=4.10 vs 1.28, p<0.001），决策回避更低（M=0.15 vs 0.46, p<0.05）。
- Artifact: Web-based surveys and phishing quizzes（基于网页的问卷调查与钓鱼测验系统） — 反馈材料（示例式反馈vs正念式反馈，反馈数量高/低）以及钓鱼邮件特征（钓鱼线索显著性），这些内容作为网页测验中呈现给参与者的信息元素
- Theory: Goal-Setting Theory（目标设置理论）; Skill Acquisition Theory（技能获取理论）
- Theory-to-design: 技能获取理论认为具体、可操作的反馈有助于将陈述性知识转化为程序性知识，从而减少认知负担、提高任务表现，据此设计示例式反馈（直接展示真实钓鱼邮件及如何识别假链接），并预期其比正念式反馈更能提升检测准确率；目标设置理论指出反馈特征、任务复杂性和自我效能是绩效的关键决定因素，据此设计反馈数量高/低、钓鱼线索显著性高/低以及测量感知检测效能，并推导反馈数量与线索显著性对检测准确率的交互效应。
- Decision: 基础筛选：文章核心目标是通过实验比较不同反馈设计和钓鱼特征对用户反钓鱼行为表现的影响，以决策回避（是否跳过）和检测准确率（是否正确区分钓鱼/合法邮件）这类客观可编码指标作为最终绩效衡量，这些指标不依赖主观感知；同时，文章明确创建了web-based surveys和phishing quizzes作为在线测验系统，并在其中通过反馈材料、邮件线索显著性等设计要素实现干预，且这些设计正是被客观指标评价的实质组成部分，因此满足基础筛选。理论细筛：文章基于目标设置理论和技能获取理论前瞻性地推导出反馈类型、反馈数量、线索显著性等设计特征，并形成可追溯的理论→设计→客观指标链条，且用客观指标检验了理论驱动的设计，因此满足理论细筛。
- Confidence: 0.95

## Socialize More, Pay Less: Randomized Field Experiments on Social Pricing

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2021.1089
- Metrics: 销售额 (Sales); 利润 (Profit); 购买频率 (Purchasing frequency); 订单价值 (Order value per purchase)
- Objective evidence: 文章的核心目标和贡献是评估社交定价相对常规定价和零售商折扣是否能提高零售商绩效和消费者购买行为；它报告了社交定价使销售额提高82.12%、利润提高28.73%（相对于常规定价），并使利润提高40.26%（相对于10%折扣），购买频率和订单价值也有显著正向差异；这些指标是论文的主要结果（表2、表6）。
- Artifact: 在线生鲜零售商平台/移动应用中的社交砍价（social bargaining）功能模块 — 在零售商平台中新增‘邀请朋友砍价’功能，包括邀请按钮、微信集成、朋友帮砍价链接、折扣累计规则（1%-5%每帮手，最高30%）、一小时过期机制，以及社区成员限制；实验2中还修改了社交互动规则，要求帮手为购买频率高一个标准差的用户。
- Theory: 社会美元效应 (Social Dollar Effect); 社会污名/社会成本理论 (Social Stigma / Social Cost Theory); 社会比较理论 (Social Comparison Theory); 间接互惠 (Indirect Reciprocity)
- Theory-to-design: 在实验2中，作者基于间接互惠（Nowak & Sigmund 2005）和社会比较理论（Lockwood & Kunda 1997, 1999; Lockwood 2002）推导出异质性社交定价规则：要求焦点消费者只能邀请购买频率高出至少一个标准差的帮手。他们认为这种设计会使下位者进行向上的社会比较从而自我激励，上位者进行向下比较从而避免落入下位者状态，同时通过间接互惠维持帮助行为，进而预期提高购买频率和订单价值。
- Decision: 基础筛选通过：文章以销售额、利润、购买频率和订单价值等客观指标为核心贡献，并通过在在线零售商平台设计和改造社交砍价功能来实现。理论细筛通过：实验2的异质性社交互动规则设计明确由社会比较理论和间接互惠理论推导，并受到客观指标检验。
- Confidence: 0.95

## Spoiled for Choice? Personalized Recommendation for Healthcare Decisions: A Multiarmed Bandit Approach

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1191
- Metrics: Precision@10; Recall@10; nDCG@10; MAP@10; DR@10; Simulation reward; in-period weight-loss rate; Jensen-Shannon divergence of recommendation diversity; user improvement rate
- Objective evidence: 文章在Section 2.2.1明确设计目标是最大化用户长期干预参与，并将参与作为反馈信号；第5章将Precision、Recall等作为主要评估指标，把提出的DLDE-MAB与多种benchmark对比，并通过消融实验验证各设计组件对指标的贡献，所有结果显示显著改进，因而这些客观指标是最终目标和核心贡献。
- Artifact: 个性化的在线医疗干预推荐系统（personalized healthcare recommendation system/framework） — 推荐系统的完整学习框架，核心组件包括：(1) 用户嵌入模型（wide-and-deep网络 + 增强LSTM + 注意力机制 + 健康结果辅助损失）；(2) 干预/项目嵌入模型（LSTM + FastText + SMART指标输出）；(3) 带理论驱动多样性约束的Thompson sampling多臂老虎机推荐策略。
- Theory: 社会认知理论（Social Cognitive Theory; Bandura 1991, 2004）; 健康行为动态理论（Johnson et al. 2002; King et al. 2006）; 健康行为动机和自我调节理论（Bandura 2004; Nahum-Shani et al. 2018）; 目标设定理论（Goal-Setting Theory; Locke & Latham 1990）; SMART目标指标（Doran 1981）
- Theory-to-design: 理论指导链条清晰：社会认知理论认为个体的健康自我调节同时需要管理健康结果与行为常规，因此文章据此设计多样性约束，要求推荐集至少包含一个结果导向型干预（如weight loss）和一个/多个行为导向型干预（如diet/exercise）；行为健康理论和健康行为动机理论指出健康管理由自我监控、治疗依从、社会联系和健康结果反馈塑造，因此用户嵌入模型选择多序列特征（健康轨迹、干预历史、自我监控、社交活动）并以健康结果作为辅助损失来影响表示学习；目标设定理论/SMART指标说明干预目标的明确性、可测性、可达性、相关性和时间限定会影响任务参与，因此项目嵌入模型将SMART元属性作为输出层学习目标。这些设计在实验前已由理论推导确定，最终都指向提升用户干预参与率等客观指标。
- Decision: 基础筛选通过：文章以最大化用户干预参与为目标，核心贡献是设计了一个个性化医疗干预推荐系统，并在真实数据上用Precision/Recall/nDCG/MAP/模拟奖励/减重率等客观指标验证其优于多个benchmark和消融变体，因而同时满足要求A和B。理论细筛通过：社会认知理论、行为健康理论、目标设定理论/SMART等心理学相关理论在设计确定前就实质性地推导了多样性约束、用户多序列表示、项目元属性表示等关键制品设计，并通过消融实验获得客观检验。
- Confidence: 0.95

## The Decoy Effect and Recommendation Systems

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1197
- Metrics: 目标项选择率; 无选择项选择率; 各备选项选择概率
- Objective evidence: 文章的研究问题、假设和核心贡献均围绕诱饵效应如何改变目标项需求；主要回归分析（表3、表4、表5）以目标项和无选择项选择为因变量，并通过模型无证据图（图4）和交互效应图（图5、图6）验证了不同条件下选择概率的变化。
- Artifact: 在线电影推荐系统平台 — 推荐列表的内容组成和呈现方式，包括个性化推荐（基于SVD算法）、非个性化推荐（基于平均评分）、诱饵项的选取与插入（低预测分数或低评分的同类型电影，置于目标项之后），以及推荐页面中预测分数/评分的呈现。
- Theory: 诱饵效应/吸引力效应; 说服理论; 来源可信度; 精细加工可能性模型
- Theory-to-design: 基于诱饵效应，设计一个被目标项支配的诱饵可引导选择；而基于说服理论和来源可信度，在个性化推荐中用户将系统视为可靠来源并期望高契合内容，低拟合诱饵会被视为低质量信息或操纵信号，降低系统可信度和信任，从而产生相反效果。因此，实验在个性化条件下使用低预测分数的同类型电影作为诱饵并置于目标之后，预期降低目标项选择率；在非个性化条件下使用同样的诱饵则预期提高目标项选择率。这些设计选择直接从理论推导而来。
- Decision: 基础筛选：文章的核心目标是检验推荐系统中诱饵效应如何改变用户需求，主要结果指标为目标项和无选择项选择率，由实验平台客观记录且不依赖主观感知；文章明确构建了在线电影推荐平台，并设计了诱饵插入、个性化/非个性化推荐等软件制品组成部分，并以这些指标评价了设计效果，因此同时满足要求A和B。理论细筛：文章明确使用诱饵效应和说服理论（来源可信度、ELM）前瞻性地推导不同推荐情境下诱饵设计如何影响选择，并通过行为实验和机制检验验证了理论到设计的链条，因此满足要求C。
- Confidence: 0.95

## The Effectiveness of Highlighting Different Communication Orientations in Promoting Mobile Communication Technology at Work vs. at Home: Evidence from a Field Experiment

- Year/journal: 2023 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00803
- Metrics: purchase rate; purchase adoption of 4G service
- Objective evidence: 购买率是研究的因变量和核心成功指标；文章通过随机现场实验比较不同消息框架的购买率，logit回归和卡方检验显示假设条件显著高于对照和其他条件，并报告经济显著性（如354%和278%的提升）。
- Artifact: 移动促销短信（SMS promotional message） — 短信中用于强调不同沟通导向（促进聚焦 vs. 防御聚焦）的消息框架语句，以及短信中包含的订阅链接和限时优惠信息。
- Theory: Regulatory Focus Theory (Higgins, 1997, 1998); Border Theory / Boundary Theory (Ashforth et al., 2000; Clark, 2000)
- Theory-to-design: 调节聚焦理论指出情境线索和活动会诱发不同的调节聚焦（促进/防御），边界理论指出人们会保护当前领域的心理边界；将二者结合推导：在工作域内与同事沟通时，工作环境以成就和发展为主要线索，诱发促进聚焦，故促销短信应强调加强与同事的联系（促进聚焦）；在工作域与家人跨域沟通时，沟通会侵入工作心理边界，导致防御聚焦，故应强调避免与家人失联（防御聚焦）；在家庭域内与家人沟通时，家庭活动以安全和安宁为主，诱发防御聚焦，故应强调避免与家人失联（防御聚焦）；在家庭域与同事跨域沟通时，工作沟通侵入家庭心理边界，防御聚焦主导，故应强调避免与同事失联（防御聚焦）。这些理论推导直接决定了短信中具体措辞的设计选择（例如“分享美好时刻并加强联系”vs.“避免失联和疏远”），并预期影响客观购买率。
- Decision: 基础筛选通过：文章以实际购买率（客观指标）为核心贡献，通过设计移动促销短信的消息框架（软件制品）来实现，现场实验验证了改进。理论细筛通过：调节聚焦理论和边界理论被明确用于推导不同场景下应采取的短信措辞设计，并通过购买率客观检验。
- Confidence: 0.95

## The Phishing Funnel Model: A Design Artifact to Predict User Susceptibility to Phishing Websites

- Year/journal: 2021 / Information Systems Research
- DOI: 10.1287/isre.2020.0973
- Metrics: AUC (area under the curve); 正确预测高严重性钓鱼威胁访问的比例; 钓鱼漏斗各阶段（访问、浏览、认为合法、意图交易、实际交易）的发生率; 成本节省
- Objective evidence: 文章的核心贡献是开发并验证PFM这一设计制品，以提高对用户钓鱼易感性的预测能力，并证明其驱动的干预能改善用户规避行为。研究问题RQ1和RQ2均围绕预测性能和下游干预效果；主要结果报告了PFM相比竞争模型在AUC上提升8%-52%，高严重性威胁访问预测96%正确，干预实验显示PFM显著降低各漏斗阶段发生率，并节省成本。
- Artifact: 设计制品：预测用户钓鱼易感性的实时预测模型/系统模块，可集成于企业端点安全解决方案以驱动个性化警告和访问控制。 — PFM模型，包括四个漏斗阶段（访问、浏览、认为合法、意图交易）的表示、六类预测变量、支持向量序数回归与自定义复合核（SVORCK）、累积链接混合模型（CLMM），以及由预测结果驱动的分级警告干预机制（默认、中、高严重性警告）。
- Theory: 技术接受模型 (Technology Acceptance Model, TAM); 保护动机理论 (Protection Motivation Theory, PMT); 人机回路安全框架 (Human-in-the-Loop Security Framework, HITLSF)
- Theory-to-design: TAM→用户对反钓鱼工具的有用性和易用性感知影响其依赖→PFM将工具感知因素（有用性、努力、工具错误成本）纳入预测变量→预期改善对用户是否遵从警告（进而影响漏斗行为）的预测。PMT→威胁评估（严重性、易感性）和应对评估受先前经验影响→PFM纳入威胁特征（领域、类型、严重性、情境）和威胁感知（意识、感知严重性）→预期改善对用户面对威胁时是否进入漏斗更深的预测。HITLSF→人口统计、知识经验影响警告有效性→PFM纳入性别、年龄、教育、信任、熟悉度、过往损失等用户因素→预期改善对用户应对警告的个体差异的预测。这些理论在模型构建前用于选择变量类别和具体变量，并在特征消融实验中得到验证。
- Decision: 基础筛选：通过。文章以预测用户对钓鱼网站易感性的AUC、高严重性威胁识别率、漏斗行为发生率及成本节省等客观指标为核心目标，并通过开发PFM这一设计制品（包括预测模型和由预测驱动的警告干预）来实现，且用这些客观指标评价了PFM的性能和效果。理论细筛：通过。文章明确使用TAM、PMT、HITLSF等心理学相关理论在事前推导PFM的变量选择和模型设计，并通过特征消融实验验证了理论指导的设计对客观预测指标的实际贡献。
- Confidence: 0.95

## Using Digital Nudges to Enhance Collective Intelligence in Online Collaboration: Insights from Unexpected Outcomes

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2023/16752
- Metrics: Collective Intelligence (TCI score); Level of collective effort (total keystrokes); Task strategy (percentage of task attempted/completed); Skill use (taskwise correlation between skill index and relative effort)
- Objective evidence: 文章的核心研究问题是数字助推能否提升临时在线群体的协作过程和集体智慧。结果部分用回归和多重中介模型检验每种助推对协作过程和CI的影响，CI作为最终因变量（Model 4）。例如Skill Facilitator Bot显著改善技能利用并通过该过程对CI产生显著间接效应（b=0.044），而Feedback Display通过降低努力对CI产生负间接效应。这些统计检验直接验证了设计方案的改进效果。
- Artifact: 在线协作平台POGS及其数字界面中的数字助推组件（集成于TCI测试界面） — 四个明确的软件界面组件：Skill Facilitator Bot（聊天窗口技能讨论机器人）、Strategy Facilitator Bot（聊天窗口策略讨论机器人）、ToDo List（任务清单小组件）、Feedback Display（实时相对参与度反馈显示）
- Theory: Nudge theory / Choice architecture (Thaler & Sunstein; Thaler et al.); Collaborative processes theory (Hackman; Steiner; Riedl et al.); Social loafing / free-riding theory (Latane et al.; Price et al.); Transactive memory / shared cognition (Argote & Ren; DeChurch & Mesmer-Magnus)
- Theory-to-design: 文章首先基于协作过程理论，识别出提升集体智慧需要三个心理/行为过程：技能利用、任务策略和集体努力。然后使用助推理论中的'结构化复杂选择'原则设计Skill和Strategy Facilitator Bot，通过聊天提示引发成员分享技能或讨论分工，从而改善技能利用和任务策略；使用'设置默认'原则设计ToDo List，使任务分配和进度可见，意图通过提高协调显著性来引导策略讨论；使用'提供即时反馈'原则设计Feedback Display，实时显示各成员相对贡献，意图通过社会规范和减少免费搭车感知来增强集体努力。每种设计都对应理论机制，并预期通过这些协作过程提升TCI上的客观集体智慧分数。
- Decision: 基础筛选通过：文章以提升临时在线群体的集体智慧为最终目标和核心贡献，使用TCI分数、按键数、任务完成比例等客观指标验证四种数字助推设计的效应；这些助推器是明确集成到POGS/TCI协作平台中的软件界面组件，属于对软件制品的实质性设计和改造。理论细筛通过：文章基于助推理论（选择架构/默认/即时反馈）和协作过程理论等心理学相关理论，前瞻性地推导了每种助推器的界面设计选择，并通过实验中的客观中介模型直接检验了理论驱动的设计。
- Confidence: 0.95

## When Variety Seeking Meets Unexpectedness: Incorporating Variety-Seeking Behaviors into Design of Unexpected Recommender Systems

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2021.0053
- Metrics: CTR; Video View (VV); Time Spent (TS); AUC; Hit Rate@10
- Objective evidence: 文章的核心贡献是提升推荐系统的业务表现，在线实验是最终验证手段，CTR、VV、TS被明确称为'most important business revenue indicators'，并通过A/B test证明治疗组显著高于对照组；离线实验的AUC和HR@10也被用作衡量推荐性能的主要依据，所有模型均显著优于基线。
- Artifact: 推荐系统（recommender system）中的个性化推荐模块 — 推荐系统的效用函数（utility function）：将固定系数α的推荐效用函数U=Relevance+α×Unexpectedness 改为融合用户variety-seeking水平的自适应函数U=Relevance+f(Variety_Seeking(i), Unexpectedness(i,j))，具体实现为DIN+Latent+Multiply等模型。
- Theory: Variety seeking behavior theory (McAlister and Pessemier 1982); Optimum stimulation level theory (Raju 1980); Exploratory behavior theory (Fiske and Maddi 1961); Consumer boredom and curiosity theories (Faison 1977, Bench and Lench 2019)
- Theory-to-design: 理论链：1) Variety seeking理论（McAlister and Pessemier 1982）指出消费者因厌倦和好奇心会寻求多样化产品；2) 文章以此为据，认为推荐系统应识别用户多样化倾向并据此调整推荐；3) 因此设计variety-seeking测量框架（距离、时间衰减、平稳性）来量化用户偏好；4) 将该测量嵌入推荐系统的效用函数（U=Relevance+f(Variety_Seeking, Unexpectedness)），对高variety-seeking用户提供更多意外推荐，低者反之；5) 预期提升客观业务指标（CTR、VV、TS）。具体设计选择（如乘性聚合函数）由该理论推导：高variety-seeker应从意外推荐中获得更高效用，从而在效用函数中放大unexpectedness贡献。
- Decision: 基础筛选通过：文章核心目标是提升推荐系统的业务指标，在线实验和离线实验均以客观指标（CTR、VV、TS、AUC、HR@10）作为最终验证标准，不依赖主观评价；设计并部署了推荐系统的效用函数（明确软件制品）以实现该提升。理论细筛通过：variety-seeking行为理论、最优刺激水平理论等心理学相关理论实质指导了推荐效用函数的设计，形成了从理论到心理机制、具体设计、客观指标的完整链条，并通过比较实验验证。
- Confidence: 0.95

## Words Matter! Toward a Prosocial Call-to-Action for Online Referral: Evidence from Two Field Experiments

- Year/journal: 2020 / Information Systems Research
- DOI: 10.1287/isre.2019.0873
- Metrics: referral decision (是否发起推荐); total number of referrals (推荐总数); number of recipients' purchases / conversions (接收者购买数/成功推荐转换数)
- Objective evidence: 文章的核心贡献是证明亲社会CTA能显著提升推荐行为与推荐结果；通过两个大规模随机现场实验（各10万客户），对比亲社会、利己、公平和对照CTA，用回归模型验证亲社会CTA在推荐决策、推荐数量和接收者购买数上均显著优于其他组
- Artifact: 在线推荐系统（online referral program）中的电子邮件和网页界面（CTA） — 推荐程序中的行动呼吁（CTA）的措辞和强调内容，包括电子邮件主题、CTA按钮和着陆页面的框架
- Theory: 内在-外在动机冲突理论 (Gneezy et al. 2011); 利他主义/温暖光辉利他 (Andreoni 1988, 1990); 亲社会行为理论; 内疚感减少机制 (Ryu and Feick 2007); 顾客愉悦与口碑传播理论 (Kornish and Li 2010)
- Theory-to-design: 理论命题：内在动机与外在激励混合会导致次优结果；利他/亲社会动机能提高口碑传播质量并减少内疚 → 心理机制：当CTA强调接收者受益时，发送者更倾向于将推荐视为帮助朋友的亲社会行为，降低因获利产生的内疚感 → 软件设计选择：将推荐CTA框架设计为'亲社会'类型，即强调接收者的奖励，而不是仅强调发送者奖励或双方奖励 → 预期改善客观指标：提高推荐发起率、推荐数量和接收者购买转化数
- Decision: 基础筛选通过：文章以推荐发起率、推荐总数和接收者购买数等客观行为指标为最终目标和核心贡献，并通过设计在线推荐程序中的CTA（电子邮件和网页的措辞框架）这些明确的软件制品组成部分来实现提升。理论细筛通过：设计CTA框架时明确使用了内在-外在动机混合、利他主义、内疚感等心理学理论，从理论命题推导出亲社会CTA的设计选择，并用随机现场实验的客观指标验证了该理论-设计链条。
- Confidence: 0.95

## Does Social Influence Change with Other Information Sources? A Large-Scale Randomized Experiment in Medical Crowdfunding

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1189
- Metrics: Donation; Donation Amount
- Objective evidence: 文章的核心研究问题是社会影响如何改变捐赠行为，主要因变量为Donation；随机实地实验在案例页面显示朋友捐赠信息，全样本中Treatment系数为0.148，即社会影响使捐赠可能性提高16.0%；进一步分析显示对低信息价值案例影响更强，且Informativeness Index与Treatment的交互项显著为负，验证了社会影响对捐赠可能性/金额的客观提升及其条件性。
- Artifact: 医疗众筹平台的可运行数字系统及其案例详情网页界面（medical crowdfunding platform case page） — 在案例详情页的筹款目标金额下方增加一行朋友捐赠信息，内容为“person X donated Y amount”；对照组不显示该行，其余页面信息完全相同。
- Theory: informational social influence; normative vs. informational social influence (Deutsch and Gerard 1955); signal/multiple-signal information value literature
- Theory-to-design: 信息性社会影响理论认为，个体在不确定情境下会将他人的行为视为可信信息源；医疗众筹中捐赠者难以验证案例真实性，因此朋友已捐款可被理解为朋友拥有私有信息并认可案例真实需要帮助。由此理论推导出设计选择：在案例页面显示“朋友X捐了Y金额”这一额外的信息呈现元素，预期通过信息性社会影响提高捐赠可能性（H1）。进一步，多重信号理论指出高信息价值案例属性会降低其他信号的边际价值，因此当案例属性本身信息价值高时，朋友捐赠信息的作用应减弱（H2）。该理论—设计—客观指标链条在实验前形成，并实际指导了治疗组界面信息的显示方式。
- Decision: 基础筛选：通过。文章以捐赠可能性/捐赠金额等平台日志客观行为指标作为核心结果，通过随机实地实验在医疗众筹平台案例页上添加朋友捐赠信息这一明确界面元素（软件制品组成部分），并比较治疗组与对照组，客观验证其对捐赠行为的影响。理论细筛：通过。文章以信息性社会影响理论（以及多重信号/信号价值文献）前瞻性推导出显示朋友捐赠信息应提高捐赠可能性、并在案例属性信息价值高时该效应减弱的设计假设；该理论—设计—客观指标链条清晰，且该界面改造被随机实验直接检验。
- Confidence: 0.94

## Explainable Deep Learning for False Information Identification: An Argumentation Theory Approach

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2020.0097
- Metrics: F1 score; accuracy; precision; recall; AUC; human task accuracy
- Objective evidence: 文章将自动FII系统的更强性能作为核心目标之一，并通过实验一将G-FINDER加入多种基线模型，报告F1、accuracy、AUC等指标的显著提升；该客观性能是判断设计成功与否的主要依据，且独立于信任、信心等主观结果。
- Artifact: automated false information identification (FII) system/framework，具体为G-FINDER这一可嵌入ML/DL模型的软件化检测框架 — G-FINDER的计算流程：将claim与evidence抽取为named entity-verb-noun三元组，构建带符号词网络，计算结构平衡连续分数（input 2），并与文本嵌入（input 1）拼接后训练分类器；同时基于平衡分数生成SBTX解释。
- Theory: Toulmin's model of argumentation; Structural Balance Theory (SBT); Theory of reference
- Theory-to-design: 文章提出，Toulmin模型中的claim-evidence-warrant需要建立claim与evidence之间的一致性连接；SBT提供设计隐喻：将claim和evidence表示为带符号词网络，用网络的结构平衡衡量二者的一致性；基于理论of reference进一步推出设计原则：在已知两条边真值的三元循环网络中，可由网络平衡状态推断第三条边（claim中的关系）的真假。该原则直接转化为G-FINDER中的三元组抽取、带符号词网络构建和结构平衡特征（input 2），预期能提高FII分类的F1和accuracy，并生成解释。
- Decision: 基础筛选：文章以自动FII系统的客观分类性能（F1、accuracy、AUC等）为核心目标，并通过设计G-FINDER这一软件化检测框架实现，故base_match=true。理论细筛：文章在Toulmin论证模型和SBT的指导下前瞻性推导出词网络平衡特征及SBTX解释设计，并用客观分类指标和人类任务准确率加以检验，故theory_guided_subset_match=true。
- Confidence: 0.94

## The Fog of Warnings: How Non-Security-Related Notifications Diminish the Efficacy of Security Warnings

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2025/18531
- Metrics: security warning disregard behavior; reaction time to warning; fMRI BOLD activation in ventral visual stream
- Objective evidence: 文章的核心目标是解释和缓解安全警告被忽视问题，并以警告忽视行为、反应时间和神经激活作为主要因变量验证干预效果。例如，实验1发现视觉相似警告在通知后忽视率提高1.95-2.6倍、反应加快30%-39%；视觉不相似警告无显著变化。实验3在视觉外观恒定的情况下，滑块交互警告未表现出泛化，按钮交互警告则忽视率提高2.8倍、反应加快约32%。
- Artifact: 浏览器安全警告界面组件（Firefox浏览器中的警告对话框/通知组件） — 安全警告的视觉外观和交互模式：包括选用/设计与其他通知视觉上不同的警告，以及将标准“点击按钮”交互改为滑块或拖拽式交互，并在实验3中在保持视觉外观恒定的条件下启用滑块控件。
- Theory: dual-process theory of habituation; generalization of habituation; schema theory; procedural/muscle memory theory
- Theory-to-design: 双过程理论认为，重复的普通通知会形成心理模型，相似的安全警告会被自动匹配到该模型，从而产生习惯化泛化，导致注意和反应下降；因此设计上应使安全警告在视觉上与普通通知足够不同（H2）。图式理论和肌肉记忆理论认为，用户对“点击按钮关闭”已形成自动化动作图式；将交互改为滑块或拖拽可打破该图式，迫使有意识加工（H3）。这两条链条都从理论命题导出具体界面设计选择，并预期提高警告遵从。
- Decision: 基础筛选通过：文章以降低安全警告忽视、减少泛化习惯化为核心目标，采用实际点击行为、反应时间和fMRI BOLD激活等客观指标验证改进；其改进对象是浏览器安全警告这一软件界面组件的视觉外观和交互模式。理论细筛通过：文章用习惯化的双过程理论、泛化理论和图式理论/肌肉记忆理论前瞻性推导了视觉区分和交互模式改变两类警告设计，并用实验数据直接检验这些理论驱动的设计。
- Confidence: 0.94

## Ambivalence Is Better than Indifference: A Behavioral and Neurophysiological Assessment of Ambivalence in Online Environments

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/17123
- Metrics: Actual purchase decisions for products with ambivalent ratings; P300 ERP amplitude (attention)
- Objective evidence: 摘要和总体讨论都将“双变量干预使矛盾信息商品的购买决策至少提升50%”作为核心贡献；H7b 在实验3和实验4中得到支持，实验3中双变量相对双极和新型双极分别带来超过50%和70%的购买增加，实验4中增加超过100%；实验1的 EEG结果支持 H1 和 H3，说明矛盾信息引发更高注意力。
- Artifact: 在线平台中的商品评分信息表示组件（rating scale / product information representation），具体为一种双变量评分条，替代传统双极星级评分。 — 将传统单条双极星级评分（如1-5星）替换/扩展为同时显示正性和负性两个分量的双变量评分表示，使 ambivalence 与 indifference 能够被区分。
- Theory: Attitudinal ambivalence and bivariate structure of attitudes (Thompson et al., 1995; Snyder & Tormala, 2017); Cognitive fit perspective (Bačić & Fadlalla, 2016); Negativity bias theory (Baumeister et al., 2001; Taylor, 1991); Broaden-and-build theory (Fredrickson & Losada, 2005; Fredrickson & Branigan, 2005)
- Theory-to-design: 论文从态度的双变量结构出发：正性和负性评价是相对独立的系统，强正强负同时存在产生 ambivalence，两者都弱产生 indifference；传统双极星级评分将正负压缩为单一连续体，使 ambivalence 和 indifference 都显示为中点，造成与实际心理表征的认知不匹配。由此推导出具体设计选择：用两个独立且显著的刻度分别显示正面和负面强度，即双变量评分条。该设计被预期能提高 ambivalence 与 indifference 的可辨别性（H5）、提高决策复杂性/认知参与（H6）、提高矛盾信息商品的购买意向和实际购买决策（H7a/b），并延长决策时间（H8）。
- Decision: 基础筛选：通过。文章的核心贡献是提出并验证一种双变量评分表示，使在线平台能更好地区分 ambivalence 与 indifference，并将矛盾信息商品的实际购买决策提升至少50%；实际购买选择是客观行为计数，实验1还使用 EEG P300 幅值作为注意力的客观指标。软件制品明确为在线电商平台的评分信息呈现组件，在四个实验中作为被设计和评价的界面组件。理论细筛：通过。双变量评分设计由态度双变量/认知匹配等心理学理论前瞻性推导，并通过 H5-H8 得到实验检验，其中包含实际购买决策和决策时间等客观指标。
- Confidence: 0.92

## Assessing the Unacquainted: Inferred Reviewer Personality and Review Helpfulness

- Year/journal: 2021 / MIS Quarterly
- DOI: 10.25300/misq/2021/14375
- Metrics: helpfulness votes; recall; precision
- Objective evidence: 文章的核心贡献是预测未来评论的帮助性，其最终目标是以推断的评伦者人格提高对helpfulness的预测性能。回归部分验证人格特质与helpfulness votes的关系（Table 4），预测部分比较人格模型与基准模型的recall和precision（Table 5），显示平均recall提升28.20%、precision提升6.89%
- Artifact: 在线评论平台（Yelp）中的预测/决策支持软件组件或信息系统的设计科学IT工件 — 基于深度学习的NLP人格推断模型（CNN-based NLP model），以及与人格推断结果结合用于预测未来评论帮助性的ensemble of ensembles预测模型
- Theory: Big Five personality traits model (McCrae and Costa 1994; McCrae and John 1992); 人格与知识分享倾向、说服力、意见领袖相关理论命题（knowledge sharing propensity, reviewer persuasiveness, opinion leadership）
- Theory-to-design: 文章以Big Five为理论框架，从人格特质命题推导出五条假设（H1-H5）。这些假设选择哪些人格特质作为关键输入变量，直接指导后续预测模型的输入特征选用：Step 2用回归检验人格与helpfulness的关系并据此选择显著特质作为Step 3预测模型的输入变量。因此理论从人格特质→心理/行为机制（知识分享、说服、意见领袖）→预测模型输入设计→改善未来helpfulness预测的recall/precision形成了可追溯链条
- Decision: 基础筛选通过：文章以提高未来评论helpfulness的预测准确率（recall、precision）和helpfulness votes为目标，客观指标来自Yelp投票和程序化分类评估；文章设计并评价了‘deep learning-based NLP模型+ensemble预测模型’这一评论平台内的IT工件，属于明确软件制品组成部分。理论细筛通过：Big Five人格理论及知识分享、说服力、意见领袖等心理机制在前瞻性假设与变量选择中实质指导了预测模型设计，并通过客观指标检验。
- Confidence: 0.92

## Containing COVID-19 through physical distancing: the impact of real-time crowding information

- Year/journal: 2020 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2020.1814681
- Metrics: location selection: 用户所选医疗机构的拥挤等级（0%/33%/67%/100%）; 选择较少拥挤地点的概率/似然
- Objective evidence: 选择行为是研究问题RQ1/RQ2和三个假设的核心因变量，也是文章声称能通过CI促进physical distancing、遏制COVID-19的主要依据。模型1显示CI存在（vs.缺失）使选择较少拥挤地点的概率提高4.6倍；模型2显示实时（vs.历史平均）CI进一步增加该概率；模型3检验健康焦虑的调节作用。
- Artifact: 决策支持系统（DSS） / 实验性网站，具体为虚构的医疗服务查找网站 find-your-doctor.org — 网站地图界面中显示拥挤信息（CI）的功能组件，包括CI的存在/缺失，以及CI的即时性线索（历史平均“usual amount of patients (past 2 months)” vs. 实时“live amount of patients (updated just now)”）。
- Theory: 建构水平理论（Construal Level Theory, Trope & Liberman, 2003, 2010）; 心理距离（temporal distance, hypothetical distance）机制; 健康焦虑概念（Abramowitz et al., 2007）作为假设距离的个体差异来源
- Theory-to-design: CLT命题：高即时性（real-time）CI使时间距离更近，从而诱发低水平/具体的心理建构；同时，医疗选择的即时目标本身处于低建构水平，因此高即时性信息产生更高的建构契合（construal fit）和加工流畅性。文章据此设计DSS中的CI即时性线索（历史平均 vs. 实时）作为实验条件，并预测该设计使拥挤成本被更充分加工、更可能选择较少拥挤地点（H2）。健康焦虑通过缩小假设距离，被理论预测会与即时性产生交互（H3）。该链条最终落到选择较少拥挤地点这一客观指标。
- Decision: 基础筛选通过：文章核心因变量为用户实际选择地点的拥挤等级，属于不依赖主观评价的客观指标，并以该指标验证CI对选择行为的因果效应；文章通过构建实验性DSS网站find-your-doctor.org并设计/操纵其中的CI与即时性线索来实现该目标，满足软件制品要求。理论细筛通过：建构水平理论被用于前瞻性地推导CI即时性这一设计特征对选择行为的影响，并通过客观选择指标和加工流畅性检验加以验证。
- Confidence: 0.92

## Design Principles for Signal Detection in Modern Job Application Systems: Identifying Fabricated Qualifications

- Year/journal: 2020 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2020.1790201
- Metrics: Accuracy; Precision; Recall; F1
- Objective evidence: 文章的核心贡献是提出并验证SIGHT系统能够自动识别申请中的虚假资历；分类性能是文章评价该方案成功与否的主要依据。Table 2显示四种分类器F1达到0.84-0.95，优于人类约54%的典型准确率和55%的无信息率；在仅使用理论预测且统计显著的特征时仍得到F1 0.73-0.92，证明该目标被实际验证。
- Artifact: 基于Web的异步自动面试与求职申请筛选系统（SIGHT原型） — 在线面试界面（逐题呈现、摄像头录制、应答计时）、服务器端行为特征提取流水线（OpenSmile提取语音、IBM Watson转写文本、SPLICE提取语言线索、Intraface提取面部关键点）、信号标准化模块，以及用于识别虚假回答的分类模型模块。
- Theory: Leakage Theory; Strategic Behavior Theory / Interpersonal Deception Theory; Cognitive Load Theory; Signaling Theory
- Theory-to-design: 泄漏理论和策略行为理论预测，说慌时会出现难以掩饰的面部冻结、运动加速减缓、声音紧张以及语言复杂度、词数、副词使用等细微变化；因此SIGHT设计选择通过常用网络摄像头同时捕捉面部、声音和语言三类信号，并采用结构化提问和组内标准化来建立个体基线，从而将理论命题转化为具体软件设计选择（自动提取 facial movement、pitch、jitter、linguistic cues 等）。这些设计选择的预期目标是提高对虚假资历的自动识别准确率。
- Decision: 基础筛选通过：文章以客观分类指标（准确率、精确率、召回率、F1）为核心贡献，验证SIGHT系统能够识别申请中的虚假资历；同时通过设计并实现SIGHT原型软件制品（在线自动面试、行为信号提取和分类模块）来实现这一目标。理论细筛通过：泄漏理论、策略行为理论/人际欺骗理论、认知负荷理论等心理学相关理论实质指导了系统信号选择和面试设计，并通过分类实验直接检验了理论指导的设计特征。
- Confidence: 0.92

## Detecting Noncompliant Behavior in Organizations: How Online Survey Responses and Behaviors Reveal Risk

- Year/journal: 2021 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2021.1962600
- Metrics: logistic regression classification accuracy; area under the curve (AUC); sensitivity; specificity
- Objective evidence: 文章的目标是提供一种低成本、可扩展的工具来评估不合规风险。在Classification Accuracy部分，作者训练逻辑回归分类模型预测合规/不合规，报告总体准确率72.79%、AUC 0.718、敏感度0.644、特异度0.792，并用假设情景说明相比随机审计能多识别2.58倍的不合规案例、减少15.1%审计资源，表明该客观分类性能是核心贡献和成功验证依据。
- Artifact: 在线问卷/调查式合规风险评估工具（intelligent online questionnaire with embedded mouse-cursor tracking） — 设计并构建了问卷的合规问题模块和后果问题模块；在Qualtrics中嵌入自定义JavaScript鼠标轨迹追踪模块；利用定制链接记录是否有作弊行为；并使用逻辑回归分类模型组合回答和鼠标偏离特征以生成风险评估结果。
- Theory: Cognitive Dissonance Theory; Response Activation Model (RAM)
- Theory-to-design: 认知失调理论→非合规者面对自身违规行为与“我是诚实/合规者”信念冲突时产生认知失调→为缓解失调而潜意识地采用更宽松的合规定义和更宽松的后果评价→据此设计问卷中专门询问“什么构成不合规”和“不合规后果是否适当”两类问题；响应激活模型→回答这类问题时，非合规者脑中同时激活客观回答和更宽松回答等竞争性刺激→大脑并行编程运动反应，导致鼠标轨迹偏离理想直线→据此设计鼠标偏离测量指标。该理论链最终指向通过回答宽松度和鼠标偏离提高客观的合规风险识别效果。
- Decision: 基础筛选通过：文章以提高非合规行为识别的客观分类准确率、AUC、敏感度和特异度为最终目标和核心贡献，这些指标由客观观察到的作弊行为计算；所提出的“智能在线问卷”包含嵌入Qualtrics的鼠标追踪、专门设计的合规/后果问题模块以及逻辑回归分类模型，属于明确的软件制品设计或改造，并直接接受上述客观指标评价。理论细筛通过：认知失调理论和响应激活模型实质指导了问卷问题类型与鼠标偏离指标的选取，形成理论→心理机制→设计特征→客观指标的完整可追溯链条，并通过假设检验和分类模型得到直接检验。
- Confidence: 0.92

## Differential Impact of Content in Online Communication on Heterogeneous Candidates: A Field Study in Technical Recruitment

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1120
- Metrics: actual job application (Apply); minimum acceptable salary increase
- Objective evidence: 全文的核心贡献在于通过现场实验验证不同在线沟通内容对异质性技术候选人实际申请行为的影响。需求A要求最终目标和核心贡献为客观指标提升，此文中申请行为是主要因变量，所有假设（H1a、H2a等）都围绕申请概率展开；通过logistic回归显示WE内容对高绩效者申请概率显著正向（系数1.885，p<0.001），对低绩效者负向（系数-1.114，p<0.05）；PI内容对初级候选人申请概率显著正向（系数1.849，p<0.001）。最低可接受薪资涨幅作为替代因变量，结果与主分析一致（Table 13），进一步强化了客观指标的改进主张。
- Artifact: 在线招聘沟通系统（为实现招聘信息呈现而设计的社交媒体页面及电子邮件内容结构） — 电子邮件中嵌入的员工在线内容信息呈现方式，具体为：链接到公司创建的两种社交媒体页面（员工工作努力与成果WE、员工个人兴趣与信念PI）并摘录其内容到邮件正文；控制组无此类内容。
- Theory: 期望理论 (Expectancy Theory / Vroom's Motivation Theory)
- Theory-to-design: 理论链条：期望理论提出动机 = 期望 × 工具性 × 效价。→ 文章据此识别出两个对技术候选人重要的工具性：绩效薪酬（performance-based remuneration）和自我表达机会（self-expression）。→ 理论推导：高绩效者更看重绩效薪酬，所以看到员工工作努力/成果的在线内容会增强其对公司认可绩效的感知，从而更愿意申请；低绩效者则会因此感到被边缘化而不愿申请。初级候选人更看重自我表达，所以看到员工个人兴趣/信念的在线内容会增强其对公司提供自我表达机会的感知，从而更愿意申请。→ 基于该理论推导，设计了两组不同的在线内容（WE和PI）作为实验处理，并假设其通过中介变量（感知绩效薪酬和感知自我表达）影响申请行为。→ 通过实际申请行为和中介分析验证了该理论指导的设计效果。
- Decision: 基础筛选通过：文章以实际求职申请行为（客观可观察行为）为核心目标和核心贡献，通过随机现场实验设计并改造了在线招聘沟通中的内容呈现（社交媒体页面及邮件内容），并用实际申请行为客观评价了设计效果。理论细筛通过：文章使用期望理论这一心理学理论，从理论命题（工具性/效价）推导出具体设计选择（WE/PI内容），并通过中介分析验证了理论中介变量，形成了清晰的理论到设计到客观指标的链条。
- Confidence: 0.92

## Encouraging Eco-driving with Post-trip Visualized Storytelling: An Experiment Combining Eye-Tracking and a Driving Simulator

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2022.0332
- Metrics: driving smoothness; braking aggressiveness; fixation count on AOI2/AOI3; dwell time percentage on AOI2/AOI3
- Objective evidence: 文章以促进生态驾驶行为为核心目标，假设和贡献主要围绕上述客观行为指标展开；实验1和实验2通过MANCOVA、ANCOVA及简单主效应分析验证了动画插图与叙事顺序对驾驶平滑度、制动攻击性、注视次数和停留时间百分比的显著影响，客观指标独立支撑了核心改进主张
- Artifact: 后行程可视化叙事界面/系统（post-trip visualized narrative） — 由驾驶路线图、碳排放图和海平面上升图构成的三个可视化，及其呈现方式：关联插图模式（静态插图 vs 成对动画插图）和叙事顺序（前瞻叙事 vs 回顾叙事）；实验2还进一步操纵了动画形式（变化插图）和呈现并发性（交错/同时呈现）
- Theory: Construal Level Theory（解释水平理论）; Mental construal literature / processing fluency perspective
- Theory-to-design: 理论命题：心理距离较近激活具体心态，心理距离较远激活抽象心态；具体心态促进对细节信息的加工，抽象心态促进对概括信息的加工。设计推导：前瞻叙事以当前驾驶情境开头，促进具体心态，因此成对动画插图提供的具体细节信息与之形成具体-特异性一致性，从而提升对驾驶行为-环境影响关联的理解并促进生态驾驶；回顾叙事以未来后果开头，促进抽象心态，因此静态插图提供的总体概览信息形成抽象-一般性一致性，从而提升态度。据此确定和约束可视化叙事中的动画/静态与前瞻/回顾组合，预期改善驾驶平滑度、制动攻击性等客观指标
- Decision: 基础筛选通过：文章设计并实现了一个明确的后行程可视化叙事软件制品，以驾驶模拟器和眼动仪记录的客观生态驾驶行为指标（驾驶平滑度、制动攻击性、视觉注意分配）为核心目标并验证改进。理论细筛通过：文章使用解释水平理论等心理学理论，在实验前前瞻性地推导并约束了动画/静态与前瞻/回顾的软件设计组合，并通过客观行为指标和中介分析对其进行了直接检验。
- Confidence: 0.92

## Gamifying knowledge sharing in humanitarian organisations: a design science journey

- Year/journal: 2020 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2020.1718009
- Metrics: KMS访问数/访问次数; 新增条目数; 新增条目评论数; 已有条目点赞数; 已有条目评论数
- Objective evidence: 文章的研究目标是提升人道主义组织KMS中的知识共享，并通过游戏化机制改善用户对KMS的参与/贡献。H1a、H1b和H2b均围绕实际行为指标展开：H1a现场实验显示游戏化个人资料使处理组访问次数显著高于对照组（M_TG=5.04 vs M_CG=2.63, p=.001）；H1b实验室实验显示水族箱条件下新增条目数（M_TG=4.33 vs M_CG=3.02, p=.002）和新增条目评论数（M_TG=3.58 vs M_CG=1.94, p<.001）显著更高；H2b显示利他主义与游戏化条件的交互显著（b=.12, p=.046）。这些行为指标是验证设计方案成功与否的主要依据。
- Artifact: 知识管理系统（Graasp）及其扩展组件：游戏化个人资料页和虚拟水族箱反馈界面 — 在Graasp KMS中新增游戏化用户个人资料页，包括六个贡献维度（Commenter、Influencer、Contributor、Collaborator、Visitor、Sharer）、Graasper总分、相对等级和蛛网图/雷达图展示；在KMS外新增可通过专用链接访问的虚拟水族箱页面，鱼的大小代表用户相对贡献，岩石和海草代表条目与评论，并配有一个可放置于办公环境的实体展示外壳。
- Theory: 动机可供性理论（Zhang, 2008）; 社会计量地位理论（Anderson et al., 2001, 2012, 2015）; 反馈与目标设定/动机理论（Ammons, 1956; Anseel et al., 2015; Hung et al., 2011 等）; 利他主义与知识共享动机理论（Hsu & Lin, 2008; Kankanhalli et al., 2005）
- Theory-to-design: 文章以社会计量地位理论为基础，指出地位来自他人的尊重和认可并构成基本动机；以反馈理论说明反馈能帮助个体评估自身行为、促进目标实现；以利他主义理论说明反馈能帮助利他者看到自己贡献的影响。随后，作者采用Zhang（2008）的动机可供性设计原则，将上述机制转化为具体设计选择：个人资料页中的六维贡献指标和Graasper总分用于呈现社会计量地位反馈；相对等级（前1%、前5%等）强化地位比较；蛛网图/雷达图设计同时支持胜任感、关系感和积极情绪；系统外的虚拟水族箱则把贡献量化为鱼的大小和动态活动，使离线员工也能持续获得反馈。完整链条为：心理学理论→社会计量地位/反馈/利他动机等机制→具体设计特征→预期的访问和贡献行为改善。
- Decision: 基础筛选：文章以提升KMS用户的实际参与和知识共享行为（访问数、新增条目、评论、点赞等可记录行为）为最终目标和核心贡献，并实际设计、修改了明确的软件制品——Graasp KMS内的游戏化个人资料页和外部反馈水族箱——且通过现场实验和实验室实验以这些客观行为指标进行验证。因此要求A和要求B均满足。理论细筛：文章在设计中前瞻性地使用了社会计量地位、反馈、利他主义和动机可供性等心理学相关理论，从理论命题推导出个人资料维度、等级、蛛网图和水族箱反馈等具体设计选择，并用客观行为指标和针对地位感知的测量检验了该链条，因此满足要求C。
- Confidence: 0.92

## On the Same Page? What Users Benefit from a Desktop View on Mobile Devices

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1140
- Metrics: decision accuracy / decision inaccuracy (决策准确性 / 决策不准确性，即错过的更优备选数)
- Objective evidence: 文章在摘要和引言中明确将“桌面视图可能通过提高决策准确性使移动用户受益”作为核心贡献；H1正是关于移动IA降低决策准确性。实验1和实验2的主要回归模型均以决策不准确性为结果变量，Table 1和Table 2显示移动IA显著增加决策不准确性，从而支持核心主张。
- Artifact: 自建在线酒店预订实验网站（a website developed specifically for this study） — 该网站的信息架构（IA）：桌面IA将所有备选与属性信息单页呈现；移动IA采用层级结构，概览页只展示部分属性，完整属性需通过点击进入各备选详情页获取。实验2还操纵了移动IA概览页所展示属性与用户偏好的一致/不一致，作为同一网站软件的明确设计变体。
- Theory: effort-accuracy framework (努力-准确性框架；Shugan 1980; Payne et al. 等); working memory capacity (工作记忆容量；Miller 1956; Luck and Vogel 1997)
- Theory-to-design: 文章从努力-准确性框架出发推导：移动IA将同一信息分层分布于多个页面，用户若想获得与桌面IA相同的准确性，需要额外付出页面导航和工作记忆整合努力；因此用户会采用更省力的启发式策略，减少信息搜索和决策时间，以牺牲准确性为代价恢复努力-准确性平衡。该推导直接生成H1。这一理论命题被操作化为网站的设计选择：桌面IA单页呈现全部信息，移动IA用概览页+详情页分层呈现信息；实验2又依据用户偏好操纵概览页属性的一致性，进一步检验理论预测的边界条件。
- Decision: 基础筛选通过：研究以提高决策准确性这一客观指标为核心贡献，并在专门开发的酒店预订网站中设计/比较桌面IA与移动IA，使用决策不准确性作为主要因变量验证该软件设计的效果。理论细筛通过：努力-准确性框架明确指导了“信息架构跨页分层导致用户减少努力和准确性下降”的设计假设，并通过客观准确性指标和努力指标得到检验。
- Confidence: 0.92

## The Effectiveness of Social Norms in Fighting Fake News on Social Media

- Year/journal: 2021 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2021.1870389
- Metrics: reported fake news count; reported real news count
- Objective evidence: 论文的研究问题是社会规范消息能否提高社交媒体用户对假新闻的举报行为；主要因变量明确是“一个人举报了多少假新闻”。文章通过控制组、指令性规范、描述性规范和组合处理之间的有序Logistic回归检验H1–H4，发现指令性规范和组合规范显著提高假新闻举报数量，因此举报行为是论文的最终目标和核心贡献。
- Artifact: 自研的类Facebook社交新闻信息流界面（实验用在线新闻反馈系统） — 信息流界面整体；在帖子中新增和简化了举报按钮；在信息流顶部加入指令性社会规范消息；在部分新闻帖上加入描述性社会规范消息（显示已有多少人举报该帖）。
- Theory: social norms theory (injunctive vs. descriptive norms); focus theory of normative conduct
- Theory-to-design: 社会规范理论指出，指令性规范通过社会赞许/不赞许施加影响，描述性规范通过告知他人行为提供决策捷径；聚焦规范理论则强调规范只有在被注意时才会引导行为。据此，论文设计了需要用户点击确认的指令性规范消息（“举报假新闻是重要且受欢迎的行为”），以及显示其他用户举报数量的描述性规范消息；组合使用时描述性规范把注意力引向指令性规范。理论推导的预期是这些设计会提高用户点击举报假新闻按钮的数量，即客观举报指标。
- Decision: 基础筛选通过：论文以用户举报假新闻的行为次数为最终目标，该指标由实验系统日志客观记录，不依赖主观评价；同时论文设计并实质修改了一个社交新闻信息流界面，在其中加入举报按钮、指令性规范和描述性规范消息，并用该界面检验举报行为。理论细筛通过：社会规范理论与聚焦规范理论在实验设计之前推导出规范消息的具体形式、位置和组合方式，并解释其通过注意力聚焦、规范性动机影响举报行为，且用客观举报指标对该理论设计进行了检验。
- Confidence: 0.92

## The effect of interactive analytical dashboard features on situation awareness and task performance

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113322
- Metrics: Errors committed (任务绩效); SAGAT scores (态势感知); Fixation duration (注视时长); Fixation count (注视次数)
- Objective evidence: 任务绩效是文章核心因变量之一，what-if分析设计被验证能显著减少错误数，构成文章的主要贡献之一；SA虽然是认知构念，但其测量是完全客观的，也是核心结果。文章将客观指标作为验证假设的主要依据，并据此提出设计启示。
- Artifact: 决策支持系统中的交互式分析仪表板（Interactive analytical dashboard） — 在交互式仪表板基础上加入what-if分析功能，包括模拟区域、瓶颈组件可视化、红绿指示等；同时实现了交互式仪表板本身的过滤、下钻、上卷等交互功能。
- Theory: Situation Awareness Theory (Endsley, 1995); Out-of-the-loop problem (Endsley & Kiris, 1995)
- Theory-to-design: 理论命题：自动化系统支持可能使操作者减少对情境的主动加工，导致SA下降和out-of-the-loop。据此推导：what-if分析自动求解优化问题，减少用户手动审查信息的必要，因此应降低SA（H1）；同时自动建议能减少认知负荷和时间，应提升任务绩效（H2）。设计选择是在交互式仪表板上加入what-if分析功能，作为自变量进行比较，并预期改善任务绩效（错误减少）。
- Decision: 基础筛选通过：文章设计并实现了两个明确软件制品（交互式仪表板与交互式分析仪表板），核心研究目标是检验what-if分析这一功能对客观指标（错误数、SAGAT、眼动）的影响，并发现what-if分析显著提升任务绩效。理论细筛通过：Endsley的态势感知理论被用于推导假设，指导设计选择（有无what-if分析），并通过实验验证了理论—设计—客观指标之间的因果关系。
- Confidence: 0.92

## Timely, Granular, and Actionable: Designing a Social Listening Platform for Public Health 3.0

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2023/17381
- Metrics: Precision; Recall; F-measure; AUC; Collection efficiency at 5M/10M URLs; Case recall; Signal precision
- Objective evidence: 文章将HealthSense的核心贡献定义为在公共卫生3.0中实现及时、细粒度、可操作的数据采集与分析；主要结论与贡献均围绕客观性能提升展开。例如，PMDS任务在5M URL时HealthSense召回75.1%，最佳对比方法HGAN为36.7%；在10M URL时HealthSense召回99.9%，HGAN仅53%-67%。用户实验和不成比例分析也显示HealthSense数据显著提高人工和自动检测的精确率/召回率。
- Artifact: Social listening platform — HealthSense平台的完整设计，包括三个明确软件模块：Relevance Assessment Module（RAM）、Credibility Assessment Module（CAM）和Landscape Assessment Module（LAM），以及基于RAM/CAM/LAM分数的URL优先级采集队列和GNN分类模块。
- Theory: Activity Theory (Leontiev, Engeström; extended to multiplex communication activities)
- Theory-to-design: 活动理论命题：在线交流活动由主体（作者）、工具（渠道）、共同体（社区规范）和内容构成；信息不仅存在于单独交流中，还存在于跨作者、渠道、社区、内容和平台的多重关系中。由此形成设计推导：需要利用作者倾向、渠道特定模式、社区词汇/规范、内容语言、互动关系和信息传播来评估相关性与可信度，并导航渠道景观。这些设计元素体现在RAM、CAM和LAM模块以及图神经网络、多级图传播、双向关系建模中。文章预期上述理论指导的设计能改善及时采集相关健康信息的精确率和召回率这一客观指标。
- Decision: 基础筛选通过：文章以设计并构建HealthSense社交倾听平台为核心，其最终目标是提高公共卫生监听中相关数据采集和下游事件检测的客观性能，并通过精确率/召回率/F值等客观指标验证。软件制品明确，包含RAM、CAM、LAM等模块。理论细筛通过：活动理论被前瞻性地用于推导HealthSense的设计要求、模块划分和关键特征，并通过消融实验直接检验理论指导组件的贡献。
- Confidence: 0.92

## Who Is the Next “Wolf of Wall Street”? Detection of Financial Intermediary Misconduct

- Year/journal: 2020 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00633
- Metrics: accuracy; recall; precision; specificity; F1 score; AUC; average economic gain
- Objective evidence: 文章的核心贡献是提出自动检测金融中介不当行为的分类器，并在第4.2节通过十折交叉验证和自然分布样本测试，比较不同特征配置的分类器，验证了准确率、召回率、AUC等指标的提升；第4.3节通过经济评估进一步证明分类器的经济价值。这些指标是判断设计方案成功与否的主要依据
- Artifact: 自动化检测/分类系统（automated classification system / decision support system） — 用于检测金融中介不当行为的机器学习分类器，包括特征集设计（自我披露信息特征、用户确认特征、监管确认特征）、机器学习模型选择、训练与评估流程
- Theory: Information Manipulation Theory; Warranting Theory
- Theory-to-design: 信息操纵理论 → 不当行为者会操纵自我披露信息的数量、质量、相关性和明确性 → 设计特征集A：包括个人描述、网络活动、职业信息、摘要文本的篇幅、复杂程度、不确定性、情绪、措辞等（Section 3.3） → 预期能区分 misconduct 与非 misconduct 的金融中介，提高分类性能（H1）。
Warranting theory → 外部验证越强，信息越难以被本人操纵，因此信息可信度更高 → 设计特征集B/C/D：增加用户确认信息（LinkedIn推荐数、技能背书数）和监管确认信息（BrokerCheck中的执业时间、职位数、考试数、执照数，以及LinkedIn与BrokerCheck的偏差） → 预期这些更难操纵的信息能进一步提升分类性能（H2、H3）。
这些特征选择在模型训练前由理论推导而来，并构成分类器的实际输入，最终通过客观分类指标和经济收益进行检验
- Decision: 基础筛选通过：文章以检测金融中介不当行为的客观分类性能和经济收益为核心目标，通过设计、构建和评估多种机器学习分类器（明确的软件制品）来实现，并实际使用准确率、召回率、AUC和经济收益等客观指标验证了改进。理论细筛通过：文章在特征选择和分类器设计前，基于信息操纵理论和warranting理论推导研究假设，并由此设计自我披露信息、用户确认信息和监管确认信息等特征集，通过比较不同分类器配置的客观指标检验了理论指导的设计。
- Confidence: 0.92

## Bringing transparency and trustworthiness to loot boxes with blockchain and smart contracts

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113508
- Metrics: distributional accuracy (chi-square goodness-of-fit); computational complexity (O(n)); deployment gas cost; transaction gas cost; security analysis (Securify/MythX)
- Objective evidence: 文章在第六节Evaluation中明确以准确性、安全性和成本作为评价所提出解决方案的三个核心维度，并以此验证方案的有效性和可行性。准确性检验结果（p值分别为0.4888、0.9126、0.7361）表明经验分布与理论分布无显著差异，这直接支撑了方案能够实现透明且可信的随机抽取这一核心贡献；成本分析也表明方案在经济上可行。
- Artifact: 区块链上的智能合约（smart contract）以及与之交互的去中心化应用（DApp） — 智能合约的完整实现，包括items列表、probabilities列表、drawItem函数和基于哈希的RNG函数；以及一个模拟购买和打开loot box的DApp。
- Theory: 决策理论（期望效用理论）; 模糊厌恶（ambiguity aversion）
- Theory-to-design: 文章在Section 2.2运用期望效用理论说明，玩家只有在知道潜在物品和概率时才能做出理性购买决策；同时引用模糊厌恶研究表明，玩家更偏好概率已知的彩票。由此推导出loot box机制需要透明和可信，从而在设计目标中确定要公开物品和概率，并保证实际抽取按此概率执行。这一设计目标进一步落实为智能合约中公开的items和probabilities数组、可验证的drawItem函数，以及基于区块链的不可篡改记录。最终，通过卡方检验验证实际抽取频率与公布概率一致，从而证明该设计选择有效实现了透明性和可信性。
- Decision: 基础筛选通过：文章以设计并实现基于区块链的loot box智能合约为核心制品，通过统计检验、成本分析和安全分析等客观指标验证其实现了公开概率和可验证的随机抽取，从而达成透明和可信的目标。理论细筛通过：决策理论（期望效用理论和模糊厌恶）在设计前提供了理论动机，推导出公开物品和概率、可验证执行随机抽取的设计选择，并通过客观统计检验验证了这一理论指导的设计。
- Confidence: 0.9

## Contextual Targeting in mHealth Apps: Harnessing Weather Information and Message Framing to Increase Physical Activity

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2020.0119
- Metrics: Achievement of 10,000-step goal (binary); Number of steps taken; Daily average steps after intervention
- Objective evidence: 文章的核心目标是设计并检验基于天气信息的mHealth消息干预能否提升体力活动水平。三项现场实验均以是否完成10,000步、步数和日平均步数为主要结果变量，并通过中性对照组、晴/阴天气交互、重复使用检验等方式验证改进。Study 2表3显示晴天时loss干预比gain更有效（β2+β3=0.0702, p<0.01），阴天时gain比loss更有效（β2=-0.0521, p<0.05）；Study 3表4显示重复四期干预均显著提升日平均步数。
- Artifact: 移动健康/活动追踪App（mHealth activity-tracking app） — 活动追踪App中推送给用户的增益/损失框架消息内容，以及基于实时天气（晴天/阴天）的消息投放规则；该部分以推送通知和个性化干预消息的形式嵌入既有App。
- Theory: mood-as-resource perspective; mood-congruity perspective; prospect theory / message framing
- Theory-to-design: 天气（日照/云量）通过血清素和β-内啡肽影响情绪；mood-as-resource认为正性情绪可作为心理资源，使人更能处理负面信息，因此晴天时loss框架更有效；负性情绪缺乏资源，阴天时gain框架更有效。mood-congruity则给出相反预测。文章依据这些理论构建晴天/阴天×增益/损失框架的实验条件，设计具体的gain和loss消息文案，并采用实时天气匹配的推送方式，预期提高10,000步完成率。理论在实验设计之前被用于确定所比较的消息框架和天气条件，而非仅仅是事后解释。
- Decision: 基础筛选通过：文章以提高10,000步完成率和步数等客观行为指标为核心目标，并通过在活动追踪App中设计增益/损失框架推送消息及实时天气匹配规则来实现和评价该目标。理论细筛通过：mood-as-resource、mood-congruity和message framing等心理学理论在前瞻性地指导了消息框架与天气条件这一软件干预设计，并通过现场实验直接检验了理论指导的设计组合。
- Confidence: 0.9

## Digital Nudging: Numeric and Semantic Priming in E-Commerce

- Year/journal: 2020 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2019.1705505
- Metrics: willingness to pay (WTP); bid amount in single-bid auction; price of selected product in set-price condition
- Objective evidence: 文章的核心研究问题就是数字启动和语义启动能否影响消费者在电商中的愿意支付金额；七个实验均以WTP/所选产品价格为因变量，使用HLM检验启动价格或启动类型的主效应，并报告效应量。Table 8汇总了各实验的显著与不显著结果，结论和启示也围绕该指标的变化及边界条件展开。
- Artifact: 模拟在线购物网站/电商实验网站，包括类似eBay的拍卖界面和类似Amazon的固定价格界面 — 该网站中的嵌入式广告组件及其数字/语义启动设计，包括广告的价格高低、广告产品与被购产品的相关/不相关性、广告尺寸、是否显示价格、使用高级品牌或经济型品牌、是否同时显示MSRP或固定价格等。
- Theory: anchoring and adjustment heuristic; dual-process cognition / System 1 and System 2; numeric priming; semantic priming
- Theory-to-design: 文章以锚定与调整、双加工认知为基础：System 1会自动快速产生价格锚，System 2随后进行调整但往往不充分。数字启动理论认为，视觉场中任何合理数字都会影响System 1产生的锚，因此设计在商品旁广告中显示较高或较低数字价格，用于提高或降低WTP；语义启动理论认为，相关的高/低质量产品会进入工作记忆并激活对应产品特征，从而影响System 2对价格的评估，因此设计广告产品与被购产品相关，并用价格或品牌表示质量高低。随后文章进一步根据相同理论设计边界条件，如MSRP或固定价格提供更相关锚点或不需要产生数字，使启动效应减弱或消失。预期客观结果就是出价金额或所选产品价格随启动高低而升降。
- Decision: 基础筛选通过：文章以消费者出价金额/所选产品价格（WTP）这一客观行为指标为核心结果，并通过在模拟电商网站中设计、修改广告组件（价格、相关性、尺寸、有无MSRP等）来实现和检验该指标的变化。理论细筛通过：锚定与调整、双加工认知、数字启动和语义启动等心理学理论被前瞻性地用于推导广告设计特征和边界条件，并通过客观WTP指标直接检验。
- Confidence: 0.9

## Estimating the Impact of “Humanizing” Customer Service Chatbots

- Year/journal: 2021 / Information Systems Research
- DOI: 10.1287/isre.2021.1015
- Metrics: transaction conversion rate; offer sensitivity (moderation of conversion by cash offer)
- Objective evidence: 文章的核心研究问题（RQ1）是拟人化如何影响交易转化概率，主要贡献也落在转化率提升上。Table 4 的 LPM 结果显示，1 个拟人化处理使转化率提高约 6.7 个百分点，3 个拟人化处理提高约 10.8 个百分点；6.2 节复制实验再次发现社交临场感处理带来约 5 个百分点的转化率提升。报价敏感度作为次要贡献被用于解释拟人化的边界条件。
- Artifact: 基于 DialogFlow 和 Python 定制实现、集成在 Facebook Messenger 的零售商客户服务聊天机器人（AI-enabled autonomous customer service chatbot） — 聊天机器人的对话界面和交互流程被明确改造，加入了三类拟人化设计特征：社交临场感（人名称呼、非正式语言、已读回执和输入提示）、通信延迟（70 WPM 动态回复延迟）、幽默（报价前随机插入笑话）；同时通过 Python 业务逻辑实现了随机现金报价。
- Theory: CASA (Computers Are Social Actors); Social Information Processing (SIP)
- Theory-to-design: 文章先以 CASA 论证：设计者可以把人际交往中的社会线索（问候、礼貌、轮流发言等）引入人机界面，以引发信任、自我表露和说服等社会反应。然后以 SIP 进一步说明：在纯文本聊天中，用户会利用打字提示、已读回执等 chronemic 线索进行社会临场感归因，因此聊天机器人设计中应加入这些线索。由此转化为具体设计选择：社交临场感条件采用人名称呼、非正式语言、已读回执和输入提示；延迟条件按 70 WPM 动态等待；幽默条件在报价前插入笑话。预期链条是：拟人化设计提高感知社会临场感和拟人化 → 顾客更信任/更愿意参与和披露信息 → 交易转化率上升。
- Decision: 基础筛选通过：文章以交易转化率这一客观实际行为结果为核心目标，并通过随机现场实验验证聊天机器人拟人化设计对转化率的影响；软件制品明确为 Facebook Messenger 客户服务聊天机器人，设计改造部分也明确为其对话界面和交互机制。理论细筛通过：CASA 和 SIP 等心理学/传播学理论被用于推导拟人化设计特征，尤其是 chronemic 社会线索的设计选择，并形成理论—设计—客观结果的可追溯链条。
- Confidence: 0.9

## Facilitating Complex Product Choices on E-commerce Sites: An Unconscious Thought and Circadian Preference Perspective

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113365
- Metrics: Decision quality (optimal choice); Ordinal decision quality (best/mediocre/poor)
- Objective evidence: 文章的核心假设（H1、H2）均以决策质量为因变量，目标是检验无意识思维对复杂决策的改善；通过卡方检验和非参数检验，发现UT条件下选择最优的参与者比例显著高于CT（27.0% vs 14.6%），且昼夜异步组中差异更显著，因此该客观指标是文章的主要贡献验证。
- Artifact: 两个相同的在线拍卖网站（e-commerce auction websites），包含产品信息页面和可弹出的分心任务窗口 — 网站的核心界面和交互流：参与者依次浏览四部手机的产品信息页（每页15秒），在UT条件下弹出n-back任务窗口（作为分心刺激），并设置拍卖倒计时；CT条件下则提供2分钟有意识思考时间，无弹出窗口。
- Theory: Unconscious Thought Theory (UTT); Circadian preference and synchrony theory (with cognitive inhibition mechanism)
- Theory-to-design: 基于UTT，研究者认为无意识思维具有更大容量并能更全面地整合信息，因此为了在实验中引发无意识思维，设计了n-back弹出窗口干扰任务，使参与者的注意从产品信息上移开，从而诱导无意识加工；基于昼夜偏好和认知抑制理论，研究者预期在昼夜异步时无意识思维优势更明显，因此在网站中记录实验时间，并用MEQ测量昼夜偏好以分组，该设计选择直接来自对认知抑制效率和工作记忆依赖的推导。
- Decision: 基础筛选：文章以客观指标（选择最优手机的比例/有序决策质量）为最终目标和核心贡献，并通过创建具有分心弹出窗口和无分心版本的在线拍卖网站来实现该目标，因此满足要求A和B。理论细筛：Unconscious Thought Theory和昼夜偏好/认知抑制理论前瞻性地指导了网站中弹出窗口（无意识思维操纵）和实验时间记录的设计，并直接得到客观指标检验，因此满足要求C。
- Confidence: 0.9

## Feedback at scale: designing for accurate and timely practical digital skills evaluation

- Year/journal: 2020 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2019.1701955
- Metrics: grading speed (evaluation time); false positive rate; false negative rate; assignment completion rate (feedback percentage); chunk completion rate; reliability inconsistencies
- Objective evidence: 文章的核心目标是设计并评估一个可扩展、准确、及时的反馈系统，明确宣称通过proof-by-demonstration展示其实现可扩展性、有效性和可靠性、对学习者行为的积极影响。文章在第二和第三迭代中，用评分速度对比、错误率对比、完成率对比等客观指标验证了这些改进，构成了文章的主要贡献。
- Artifact: Socio-technical artifact with an IT core consisting of a custom-developed learner application (web-based MEAN stack app) and a custom-developed grading engine (Python-based XML parser) — The learner application includes chunked assignment support, structured starter files, drop-file submission, near-real-time feedback display, and AWS Lambda architecture; the grading engine includes XML parsing, key files, multiple keys, exact/flexible matching, and error detection functions.
- Theory: Intervention theory (Argyris, 1970); Feedback intervention theory (Kluger & DeNisi, 1996; Hattie & Timperley, 2007); Progress principle / small wins theory (Weick, 1984; Amabile & Kramer, 2011)
- Theory-to-design: 干预理论的三原则被用作kernel theory，推导出元需求MR1-MR5和设计原则DP1.1-DP5.3。例如，MR1要求有效信息，导致DP1.3/1.4设计可靠且有效的测量，进而实现为评分引擎和活动日志；MR3要求最大化学习者控制，导致DP3.1/3.2/3.3，实现为可选作业、反馈和资源指引；MR5要求促进进步感，基于小胜利理论，导致DP5.1-5.3，实现为现实、可管理、有限范围的作业块（chunking）。具体地，第二迭代中的分块、结构化起始文件和快速反馈明确受到progress principle启发。此外，反馈干预理论指导了系统提供任务级具体反馈而不是总体评价（DF8/DF11），以避免注意力分散到自我。所有这些设计选择都对应于软件制品的明确功能。
- Decision: 基础筛选通过：文章以评分速度、错误率、完成率等客观指标为核心贡献，并通过设计、构建和评估学习者应用和评分引擎这一明确软件制品来实现。理论细筛通过：干预理论、反馈干预理论和小胜利理论实质指导了制品设计，形成了从理论到设计原则再到具体功能以及客观评估的完整链条。
- Confidence: 0.9

## Ingredients for successful badges: evidence from a field experiment in bike commuting

- Year/journal: 2020 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2020.1808539
- Metrics: RidingDays; weekly bike-riding days
- Objective evidence: 文章的核心目标是检验不同徽章设计对目标行为（骑行天数）的促进作用，摘要、引言、研究假设、实验设计和结果分析均以此为中心。文章通过2×2×2田野实验和随机效应面板回归检验改善：withSharing显著提高骑行天数（β=0.044，p=0.022）；relative和freqRider的交互项显著（β=0.122，p=0.001），表明相对目标对频繁骑行者有正向作用；零膨胀泊松模型也得到相似结果。
- Artifact: 自行车通勤计划中的徽章成就系统及配套数字界面（周电子邮件新闻简报和Web门户仪表盘） — 对既有的自行车通勤计划周报邮件和Web门户仪表盘进行再设计，加入徽章显示并系统操纵徽章设计的三个组件：奖励（是否提供Facebook分享链接）、标识/能指（亲环境框架 vs 自利框架）、完成逻辑（固定目标 vs 相对目标）；徽章通过周报邮件和仪表盘中央面板呈现给用户。
- Theory: Expectancy-value theory; Intrinsic motivation theory / Malone & Lepper challenge-uncertainty perspective; Message framing research
- Theory-to-design: 文章在假设提出部分先引入期望价值理论：个体认为结果更有价值时会更努力，因此为徽章增加社交媒体分享选项可提高预期社会价值，进而提升骑行天数（H1）；亲环境框架通过唤起温暖感/亲社会价值提高感知价值，进而提升骑行天数（H2）。对于完成逻辑，文章引用内在动机理论中“不确定性/挑战”机制，认为相对目标对频繁骑行者更有刺激性和激励作用（H3、H4）。这些理论在实验前形成了可检验的设计假设，不是事后解释。
- Decision: 基础筛选：文章以RFID自动记录、可客观核验的每周骑行天数为最终目标和核心贡献，并通过再设计Web门户仪表盘和电子邮件新闻简报中的徽章显示及徽章组件来影响该指标，故客观指标和软件制品要求均通过。理论细筛：文章使用期望价值理论、内在动机理论和信息框架等心理学相关理论，在实验前前瞻性地推导分享选项、亲环境标识和相对目标等设计选择，并用客观骑行数据直接检验这些理论指导的设计，因此理论指导子集匹配。
- Confidence: 0.9

## Is optimal recommendation the best? A laboratory investigation under the newsvendor problem

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113251
- Metrics: Pull-to-Center (PtC) effect; actual order quantity; profit (pesos earnings); PtC asymmetry effect size d; DSS recommendation adoption rate / non-adherence percentage; regret aversion measure RA
- Objective evidence: 研究问题、摘要和假设均围绕DSS能否降低PtC偏差并提高利润。假设H1-H3通过回归检验，Table 3显示ODSS显著降低低利润条件PtC、提高利润并减小PtC不对称；Table 5-6显示激进DSS在高利润条件下将PtC效应降至0.075（与0无显著差异），即消除PtC偏差。它们构成论文的核心贡献和成功判断依据。
- Artifact: 决策支持系统（DSS） — DSS的推荐规则（最优推荐X±25、保守推荐X±20、激进推荐X±30）、决策界面中的推荐显示和自由修改功能、双向绩效反馈机制（同时反馈被试与DSS的利润和累计利润）。
- Theory: algorithm aversion; regret aversion; anchoring and insufficient adjustment; social comparison theory; prospect theory
- Theory-to-design: 算法厌恶理论（Dietvorst等）→ 用户会因算法错误而丧失信心、不愿采纳优劣建议 → 设计DSS时让推荐随轮次变化以显得更智能，同时允许用户自由修改推荐，并从文献中获得“允许修改可降低算法厌恶”的设计依据；后悔厌恶理论（Zeelenberg, Loomes & Sugden, Bell）→ 用户会根据双方绩效反馈产生体验后悔 → 设计DSS提供DSS与被试双方的利润反馈，使后悔厌恶能够推动用户后续接近推荐；锚定与调整不足理论（Schweitzer & Cachon）→ 推荐值可作为锚点 → 设计激进DSS将推荐置于最优值与需求极端之间，使被试从锚点向最优方向调整，从而消除PtC偏差。
- Decision: 基础筛选通过：论文以实验室实验中实际订单量、PtC偏差、利润等客观指标为最终目标和核心贡献，并通过设计/改进最优、保守、激进三类决策支持系统实现这些指标改善。理论细筛通过：算法厌恶、后悔厌恶、锚定与调整不足等心理学理论在DSS设计之前推导出推荐逻辑、反馈机制等设计特征，并用客观指标对这些设计进行了直接检验。
- Confidence: 0.9

## Knowledge-Aware Learning Framework Based on Schema Theory to Complement Large Learning Models

- Year/journal: 2024 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2024.2340827
- Metrics: 加权F1分数; 训练数据比例下的性能保持度; 训练时间; 模型参数量; 知识图鲁棒性（不完整/噪声下的F1）
- Objective evidence: 文章的核心研究问题是设计一种认知可信的知识感知学习框架，使其不依赖LLM也能获得满意性能并提升学习效率；这直接通过实验1、实验2和实验3来验证：其框架在多个任务上优于知识感知基线Text GCN和KIM，与SOTA LLM性能相当，并且仅用约7.6%的参数量、10%的训练数据以及近3倍更快的训练速度实现该性能，消融和鲁棒性实验确认了各组件的贡献。
- Artifact: 知识感知学习框架/深度学习文本分析模型，包含知识库、知识结构化表示、知识激活机制以及GCN与bi-LSTM融合的预测模型 — 设计了完整的四元组件学习框架：使用ConceptNet作为大规模知识库以模拟长时记忆；将知识三元组组织为结构化知识图；构建带权重的上下文知识图实现图式激活机制；采用GCN结合bi-LSTM将激活知识与原文信息融合完成文本分类和NLI任务。
- Theory: 图式理论（Schema Theory）
- Theory-to-design: 文章从图式理论出发，认为人类学习由知识获取、知识表征、知识激活和知识利用四个过程组成；据此设定ISDT元需求，并推导出四个元设计元素：使用ConceptNet模拟人类长时记忆中的知识库，使用知识三元组和知识图模拟结构化图式，使用基于TF-IDF思想的上下文知识图权重模拟任务线索对相关图式的激活，最后使用GCN+bi-LSTM将激活知识与原文信息融合；该设计意在提升文本分析的F1和学习效率。
- Decision: 基础筛选通过：文章以文本分析任务的F1、学习效率、模型规模等客观指标为最终目标和核心贡献，通过设计一个可运行的知识感知学习框架实现这些提升，该框架由知识库、知识结构、激活机制和预测模型等明确软件组件构成。理论细筛通过：图式理论作为核心理论在前瞻性指导该软件制品的设计，形成了从理论命题、心理机制、具体设计选择到客观指标评价的完整链条。
- Confidence: 0.9

## Mobile health: A carrot and stick intervention to improve medication adherence

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2019.113165
- Metrics: Medication Adherence Rate (MAR); Probability of reaching expected MAR; Healthcare savings
- Objective evidence: 文章的核心贡献是提出Carrot & Stick（C&S）干预以提高服药依从性；第5节明确将MAR作为核心因变量，第6节用解析结果说明提醒和正强化能显著提高达到预期MAR的概率，增加负强化后效果更佳，并给出显著医疗节省。这些结果构成文章的主要改进主张和贡献。
- Artifact: 移动健康手机应用（mobile health app） — 应用内的服药提醒、两个服药时间窗规则、正强化（PR奖励）机制、负强化（封锁最常用App）机制、目标设定、社会连接分享、服药记录与向医疗专业人员发送报告等模块。
- Theory: Social Cognitive Theory (SCT); Social Exchange Theory; Goal-setting Theory
- Theory-to-design: 理论→心理/行为机制→具体设计→客观指标：SCT的健康行为决定因素和强化思想指导设计中加入PR、NR、目标设定和社会连接；社会交换理论的强化命题和边际效用递减指导设计固定/递增PR，并按患者敏感性选择递增或固定奖励；目标设置理论指导设计自设目标或医生指定目标并给予反馈；这些设计选择都旨在提高按时服药概率，最终提升MAR和达到预期MAR的概率。第2.1-2.3节的理论推导在第3.1节转化为系统流程，第4节转化为十种应用场景，第5-6节用解析模型评价。
- Decision: 基础筛选通过：文章以可客观计算的MAR、达到预期MAR的概率和医疗节省为核心贡献，并通过设计移动健康应用C&S的提醒、时间窗、PR/NR、目标设定等组件来实现和验证，属于明确的软件制品设计。理论细筛通过：社会认知理论、社会交换理论和目标设置理论在系统设计中实质指导了强化、目标设定、社会连接等模块，并通过解析模型对这些理论指导的设计组件进行了客观评价。
- Confidence: 0.9

## Pushing Yourself Harder: The Effects of Mobile Touch Modes on Users’ Self-Regulation

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1155
- Metrics: healthy beverage choice (binary choice behavior); personal hygiene lapses (observed count of hygiene guideline violations); physical exercise amount and exercise goal (supporting/self-report measures in Study 2)
- Objective evidence: 文章的核心主张是触控模式可提升用户的自我调节，并将自我调节操作化为多项行为结果。Study 1 中压按组选择健康饮料的比例显著高于点按组（41/60 vs 26/60，Wald=6.20，p<0.05）；Study 3 中压按组的个人卫生违规次数显著少于点按组和长按组（F=63.25，p<0.01）。这些客观行为结果被用于直接验证设计方案的改进，而不是附属或背景指标。
- Artifact: 移动应用（mobile applications），具体包括实验用移动饮料选择应用、移动健身应用、移动个人卫生教育应用 — 应用中的触摸交互模式/手势输入：压按（pressing）与点按（tapping）两种基于力量感应技术的触摸方式，以及 Study 3 中的长按（holding）对照条件；该交互设计用于浏览饮料信息、设置运动目标、提交卫生行为承诺。
- Theory: embodied cognition theory (具身认知理论); self-regulation (自我调节理论/构念); regulatory focus theory (调节焦点理论)
- Theory-to-design: 具身认知理论认为，主动施加力量的动作会引发‘对目标的坚定趋近动机’这一身体-心理联结；因此，相比轻点屏幕的 tapping，需要更大力量按压屏幕的 pressing 被选为移动健康应用中的交互设计特征。文章从该理论推导出：在健康相关移动应用中，将信息查看、目标设定和承诺提交设计为按压动作，可以激活趋近动机，从而增强自我调节，并最终改善健康行为结果（如选择更健康饮料、提高运动量、减少卫生违规）。
- Decision: 基础筛选通过：文章以客观可测的健康自我调节行为改善为最终目标，核心贡献是验证移动触摸交互设计（压按 vs 点按）对真实选择、运动行为和个人卫生行为的影响；文章构建并实质修改了多个实验用移动应用的触摸交互部分，并用客观行为指标进行了验证。理论细筛通过：文章从具身认知理论前瞻性推导出压按应激活趋近动机，并将该理论直接落实为移动应用的交互设计选择，再通过实验中的客观行为结果和中介分析加以检验。
- Confidence: 0.9

## The Secret to Finding a Match: A Field Experiment on Choice Capacity Design in an Online Dating Platform

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2021.1028
- Metrics: number of choices; number of chats; view profile; send invite; revenue
- Objective evidence: 文章的核心目标是实证检验不同选择容量对用户参与度和匹配结果的影响，并据此提出平台设计指南。通过随机田野实验，作者比较了四个处理组与对照组的差异，如男性选择组参与度提升116%，女性选择组匹配结果提升113%，这些效果均由回归分析验证，是文章的核心贡献。
- Artifact: 在线约会平台（online dating platform） — 选择容量（choice capacity）设计，即平台每天向用户展示的候选配对数量上限（如30对、10对等）。
- Theory: choice effect; competition effect; positive same-side effect; negative cross-side effect; gender differences in risk perception; social norms in relationship initiation
- Theory-to-design: 文章在Section 3中基于choice effect和competition effect提出理论预测：增加选择容量会使用户在感知收益与成本之间权衡，男性因较低拒绝成本和风险偏好更可能变得更挑剔（选择效应），女性因更大拒绝恐惧和风险规避更可能变得更不挑剔（竞争效应）。这些理论推导直接指导了实验设计中不同选择容量处理组的设置（如仅增加女性选择容量的T1，仅增加男性选择容量的T2），并预期这些设计会通过改变用户选择行为影响匹配结果。
- Decision: 基础筛选通过：文章以在线约会平台为载体，通过随机田野实验设计不同的选择容量（choice capacity）这一平台功能，以系统记录的用户行为客观指标（如choices、chats）为核心目标，验证了设计改进的效果。理论细筛通过：文章基于选择效应、竞争效应以及性别差异的风险感知和社会规范等心理学相关理论，前瞻性地推导出不同选择容量对用户行为和匹配结果的影响，并通过实验设计直接检验了这些理论指导的设计选择。
- Confidence: 0.9

## A social mechanism for task-oriented crowdsourcing recommendations

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113449
- Metrics: Recommendation accuracy; Willingness to take up task invitation
- Objective evidence: 文章的核心目标是帮助请求者找到合适且愿意完成任务的贡献者，推荐准确率和任务邀请接受率正是对这一目标的直接度量。实验将提出的SCT机制与随机、内容型、协同型、通用平台等基准模型比较，并用配对样本t检验验证SCT在准确率和接受率上显著更优；这些客观指标是文章的主要成功证据，主观的fitness和liking仅作为辅助结果。
- Artifact: 基于Web的任务型众包社交推荐系统 — 推荐系统整体框架及其四个模块：类型树构建模块、贡献者池分析模块、社交影响分析模块、任务众包推荐模块；系统生成推荐贡献者名单并发出任务邀请。
- Theory: Social influence theory; Social affiliation and social closeness / tie strength
- Theory-to-design: 社会影响理论 → 贡献者的兴趣和参与意愿会受到朋友及请求者社会关系的影响 → 因此在社交影响分析模块中设计计算社交关联（朋友对任务的参与程度及互动强度）和社交亲近度（贡献者与请求者之间的社会路径强度），合并为SocialInfluence（Eq. 15），并纳入综合适宜性评分（Eq. 22）→ 预期提高推荐准确率和受邀者接受率。实验通过包含社交影响的SCT模型与不含社交影响的模型对比来直接验证这一链条。
- Decision: 基础筛选：文章以推荐准确率和任务邀请接受率等客观行为指标的提升为核心贡献，并设计实现了基于Web的任务众包社交推荐系统，因此通过。理论细筛：社会影响理论及其社交关联、社交亲近机制在设计阶段实质指导了社交影响分析模块，且该理论指导的模块通过SCT与基准模型的客观比较得到验证，因此通过。
- Confidence: 0.88

## Digital nudging for technical debt management at Credit Suisse

- Year/journal: 2023 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2022.2088413
- Metrics: Overall TD index; Code quality debt index; Infrastructure lifecycle debt index; Vulnerability debt index; Automation debt index
- Objective evidence: 文章将降低TD作为设计方案的核心贡献，明确表示‘nudge在一年使用后有效降低了IT应用中的TD’；第4.2节以Table 3的定量TD变化为主要评价来源，使用nudge的团队1和2整体TD下降，未实际使用nudge的团队3 TD上升，因此客观TD指标支撑了文章的核心改进主张。
- Artifact: 数字助推仪表板（digital nudge dashboard / TDM nudge），基于Tableau可视化和数据加工组件构建的可运行数字系统。 — 设计了完整的TDM nudge仪表板，包括8个设计元素（整体评级、信息来源、评级进度圈、演化趋势、单项TD指标、颜色范围、团队平均表现、阈值消息），以及数据采集、集成、聚合和日常自动化计算组件。
- Theory: Nudge theory / choice architecture (Thaler & Sunstein); Bounded rationality and heuristics-and-biases (Kahneman & Tversky); Framing effect; Social norms theory; Messenger effect; Anchoring heuristic; Availability heuristic; Loss aversion
- Theory-to-design: 理论命题：个体是有界理性的，其决策受心理偏差影响，因此可以通过选择架构设计来引导行为而不禁止选项。文章据此选择六种心理效应：框架效应→整体评级、颜色代码和单项指数简化并突出TD属性；社会规范→评级和‘CS Average’平均表现触发团队比较；损失厌恶→评级进度圈和趋势图强调避免评级下滑；锚定→颜色范围和箭头框提供TD决策参考点；可得性启发→阈值消息和提醒使TD议题保持可见；信使效应→‘i’信息源标记增强可信度。这些心理效应被前瞻性地转化为8个设计元素，构成TDM nudge的界面和信息呈现，预期目标是提升TD意识并促使软件团队采取降低TD的行动。
- Decision: 基础筛选通过：文章以降低客观技术债务指标为最终目标和核心贡献，并通过设计、实现和部署一个数字助推仪表板（TDM nudge）来实现，一年后的量化TD变化（Table 3）作为主要验证。理论细筛通过：nudge理论及多种心理效应（框架、社会规范、损失厌恶、锚定、可得性、信使）在前瞻性上指导了仪表板的8个设计元素，形成理论→心理机制→制品设计→客观TD指标的可追溯链条，并用TD水平变化进行检验。
- Confidence: 0.88

## Explainability and fairness of RegTech for regulatory enforcement: Automated monitoring of consumer complaints

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113782
- Metrics: Accuracy; Precision; Recall; F1-score; Lift (coverage of true monetary compensation cases)
- Objective evidence: 文章的核心目标是提出并评估一个能够自动识别可能获赔的消费者投诉的RegTech方案，分类性能是判断设计是否成功的主要依据。H1、H2、H3均以分类指标验证：Classifier A准确率84.03%，Classifier B准确率85.12%，Classifier C准确率85.92%，并通过McNemar检验、子组分析和实际holdout lift图证明其价值。
- Artifact: RegTech自动监测/决策支持系统，具体表现为用于自动评估金融消费者投诉的文本挖掘分类器配置。 — Classifier A（基于信息诊断性理论的语言特征）、Classifier B（基于词袋模型）、Classifier C（集成Classifier A和B）、面向older Americans的专门公平分类器，以及相应的文本预处理、特征构造和分类流程。
- Theory: Information Diagnosticity Theory
- Theory-to-design: 信息诊断性理论认为，文本的深度、情感倾向、时间焦点、主动/谨慎表达方式等影响文本对读者的诊断价值。文章据此假设，更具诊断性的消费者投诉更有说服力，进而更可能获得赔偿。该理论直接指导了Classifier A的特征设计（DF1a），例如词数、积极/消极词比例、过去时词、不确定性词、感知词、知识词等，并进一步形成“理论命题→文本诊断价值/信息处理机制→分类器特征选择→预期提升投诉获赔预测准确率”的完整链条。
- Decision: 基础筛选通过：文章核心目标是构建并评估用于自动监测消费者投诉的RegTech分类方案，以是否获得货币赔偿为客观真值，核心贡献由accuracy、precision、recall、F1和lift等客观指标支撑；同时文章明确设计Classifier A/B/C及公平分类器作为RegTech应用组件，并用这些指标评估。理论细筛通过：信息诊断性理论被前瞻性地用于推导Classifier A的文本特征设计，形成了理论→心理/行为机制→制品设计→客观指标评价的可追溯链条。
- Confidence: 0.88

## Mobile Advertising in Distracted Environments: Exploring the Impact of Distractions on Dual-Task Interference

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2024/17758
- Metrics: ad engagement; brand recognition; interrupt effectiveness
- Objective evidence: 文章的核心目标是优化移动弹窗广告在分心环境中的有效性，ad engagement是判断广告设计是否成功的核心结果变量。研究通过三项实验验证了改进：任务参与度与广告识别正相关（H1），低环境参与度时投放广告提升识别（H2），广告与环境内容一致提升识别（H3），距离削弱任务参与度对广告识别的正向作用（H4）。
- Artifact: 自定义移动/网页应用（custom app），模拟带有弹窗广告的移动端anagram游戏，并可配合分屏/多屏/投影等环境视频展示方式。 — App中的弹窗广告模块：包括广告与NFL环境的一致性内容设计（代言人和品牌组合）、广告投放时机（与NFL比赛内容的play/replay/commentary时段同步）、以及在三种空间距离条件下的屏幕布局（split-screen、multiscreen-personal、multiscreen-projector）。
- Theory: dual-task interference (DTI) theory / bottleneck model (Pashler, 1994); limited capacity model of attention (Kahneman, 1973; Lang, 2000); automaticity (Logan, 1979; Pashler, 1994); task similarity/compatibility (Duncan, 1979; Peters, 1977; Navon & Miller, 1987); relevance accessibility framework (Lynch et al., 1988); split-attention effect / cognitive load theory (Ayres & Sweller, 2005; Mayer & Fiorella, 2014; Sweller et al., 1998); two-stage model of attention (Shen & Sengupta, 2014)
- Theory-to-design: 完整的理论—设计链在Hypothesis Development中前瞻性建立：H1基于DTI和自动性，认为分心环境中任务与中断被当作单一实体处理，高任务参与度会增强中断编码，因而设计了关注任务参与度对广告识别影响的研究；H2基于有限容量注意与注意力扩散，推断环境参与度高时中断效果差，因而设计了把广告定位于环境参与度低（如NFL的replay/commentary段）而非高参与度的action段；H3基于relevance accessibility framework和任务相似性研究，推断广告与环境内容一致能提高处理效率，因而设计了广告代言人/品牌与NFL环境的一致性水平；H4基于split-attention effect和认知负荷理论，推断空间距离增大导致注意力更难分配，因而设计了split-screen、multiscreen-personal、multiscreen-projector三种距离条件。这些设计特征均是App广告模块的可操纵部分。
- Decision: 基础筛选通过：文章以提高移动弹窗广告有效性为核心目标，使用品牌识别正确率这一可客观判定的结果指标作为核心贡献，并通过自定义App对广告内容、投放时机和屏幕布局等软件设计进行实验评价。理论细筛通过：DTI、注意有限容量、相关可及性、分心注意效应等心理学理论在假设开发中前瞻性地推导并约束了App广告模块的设计特征，并用广告识别指标直接检验。
- Confidence: 0.88

## Peer Effects in Competitive Environments: Field Experiments on Information Provision and Interventions

- Year/journal: 2021 / MIS Quarterly
- DOI: 10.25300/misq/2021/16085
- Metrics: StartTime; Grade
- Objective evidence: 文章的研究问题、假设和贡献均围绕减少拖延和提升成绩；使用随机田野实验对比处理组与对照组，回归分析以 StartTime 和 Grade 为因变量，并进一步用中介分析说明行为改善带来成绩提升。
- Artifact: 学习管理系统（LMS）的自动化干预插件/附加程序（Canvas add-on） — 该插件自动读取 Canvas 系统日志，计算参考群体中已开始作业的学生比例（描述性同伴信息），识别并随机分配干预对象，并通过邮件或登录通知发送截止提醒及同伴信息；Study II/III 中还将参考群设为随机分配的四人至六人小组，并在 Study III 中操纵排名制评分条件。
- Theory: 描述性社会规范/社会从众理论（Cialdini and Goldstein 2004）; 社会比较理论（Garcia et al. 2013）; 竞争情境下的性别差异理论（Gneezy et al. 2003）
- Theory-to-design: 描述性社会规范理论认为，看到‘X%的同学已开始作业’会塑造个体对同伴行为的信念，促使个体依从规范；社会比较理论认为，在竞争情境下披露同伴进度会诱发社会比较和竞争性动机。由此，作者设计 LMS 插件在截止日前向学生发送包含描述性同伴信息（而非仅截止提醒）的消息；该信息呈现方式由理论推导而来，并预期通过上述心理机制使学生更早开始作业（StartTime 增大）并最终提高成绩（Grade）。此外，性别差异与竞争偏好理论进一步指导了在排名制/非排名制和不同同伴行为比例等实验条件下检验干预效果。
- Decision: 基础筛选通过：文章以 StartTime 和 Grade 这两个不依赖主观感知的客观指标改善为最终目标和核心贡献，并通过开发 Canvas 插件（LMS 中的软件制品）实现同伴信息干预。理论细筛通过：描述性社会规范、社会比较和竞争性别差异理论实质指导了同伴信息内容与干预情境的设计，并通过客观指标和实验设计直接检验了这一理论-设计链。
- Confidence: 0.88

## Privacy Concerns and Data Donations: Do Societal Benefits Matter?

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2024/16853
- Metrics: Amount of data donation (number of donated data items; 23 items in Experiment 1, 27 items in Experiment 2)
- Objective evidence: 数据捐赠量是研究模型的主要因变量和全部假设检验的核心结果。文章通过两个实验验证隐私关怀对捐赠量的负向影响，并检验隐私控制、隐性和显性社会效益条件如何削弱该负向影响；这些交互效应支撑了文章的理论贡献和实践启示。
- Artifact: 数据捐赠移动应用：DataDonors app mockup（实验1）和 Fight COVID-19 app simulation（实验2） — App内被设计或改造的部分包括：隐私控制界面（granular privacy settings 提供或不提供）、App首页图片与文字（诱发 empathic concern）、App内明确说明社会效益或个人效益的信息界面，以及数据捐赠选择界面。
- Theory: Privacy Calculus; Empathy-Altruism Hypothesis; Altruism/warm-glow (impure altruism) perspective
- Theory-to-design: 隐私计算理论：隐私决策是风险与收益的权衡；据此，在App中设计隐私控制来降低风险感知、设计社会效益线索来增加收益感知，理论预测这些设计会削弱隐私关怀对捐赠量的负向影响。共情-利他假说：共情关怀使人关注他人福祉而非自身隐私风险；据此，在App首页加入患者图片和perspective-taking文本，预测削弱隐私关怀的负向作用。理论链条为：理论命题 → 心理/行为机制 → App具体设计选择 → 预期改善客观捐赠量。
- Decision: 基础筛选：文章以参与者实际选择捐赠的数据项数量为核心客观指标，并通过设计/改造两款数据捐赠App（DataDonors、Fight COVID-19）中的隐私控制、社会效益呈现等组件来实现并检验该指标，因此base_match=true。理论细筛：隐私计算、共情-利他假说和亲社会动机理论在实验前推导出App设计特征，并通过客观捐赠量交互效应得到检验，因此theory_guided_subset_match=true。
- Confidence: 0.88

## Social influence-based contrast language analysis framework for clinical decision support systems

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113813
- Metrics: Accuracy; Precision; Recall; F_Score
- Objective evidence: 文章的核心贡献是提出并验证用于CDSS的对比语言分析框架，以改善早期抑郁检测能力；第4.3节的用户研究以分类性能作为主要评价标准，CART达到最高准确率69.05%、精确率76.19%、召回率66.67%、F值71.11%，并将所提特征集与LIWC、SBERT、GTF、RFE等基线比较，显示所提特征显著提升检测性能。
- Artifact: 数据驱动的临床决策支持系统（CDSS）中的分析型组件/框架，即社会影响对比语言分析框架及其数据驱动技术接口 — 在CDSS中设计并实现对比语言特征发现流程，包括术语级对比特征、主题级对比特征和网络级对比特征提取模块；这些模块可进一步与基于案例、规则、模型等其他CDSS数据驱动组件交互，用于早期抑郁检测、干预和治疗计划推荐。
- Theory: Social Influence Theory; Social Learning Theory; Mood Contagion Theory
- Theory-to-design: 社会影响理论命题：个体的态度、行为、语言会受到参照他人及社会规范的影响，越亲近的联系人影响力越强；情绪也可通过社交互动传染。由此推导心理/行为机制：在心理健康状态网络中，用户的语言和情绪倾向会受到其抑郁或非抑郁朋友的内容影响，距离越近影响越大。该机制指导了网络级对比特征（NBC_d、NBC_nd）的设计：用最短路径距离的倒数作为社会影响权重，并计算目标用户与抑郁/非抑郁邻居内容向量的余弦相似度；此外，术语级和主题级对比特征也来自群体语言规范差异。预期这些由理论推导的特征能提高早期抑郁检测的准确率、精确率、召回率和F值。
- Decision: 基础筛选通过：文章以早期抑郁检测的分类性能（准确率、精确率、召回率、F值）作为最终目标和核心贡献，指标可程序化计算；同时该框架被明确表述为数据驱动CDSS的分析组件，并通过实验验证其特征提取模块对检测性能的提升。理论细筛通过：社会影响理论等心理学相关理论从人际影响、社会规范、情绪传染等机制出发，实质推导了网络级对比特征的设计，并通过不同特征子集的对比实验直接检验了该理论指导的设计。
- Confidence: 0.88

## Standardize or Let a Thousand Flowers Bloom? Interface Design Coordination between Software Platforms and Hosted Apps

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/16484
- Metrics: App usage (frequency and duration); platform-to-app forward derivative usage path coefficient
- Objective evidence: 研究问题直接关注界面设计能否促进平台与 App 之间的使用关系；结果中平台使用对 App 客观使用有显著正向影响（0.264, p<0.01），分组感知对该正向路径有显著调节作用（0.365, p<0.01），支持 H4，从而构成界面设计价值的核心实证主张。
- Artifact: 移动社交平台微信中的第三方信息型 App（微信 Official Account 上的八种界面版本） — App 的用户界面与交互机制：界面相似性（字体/背景色）、界面嵌入性（在微信平台边界内还是外部窗口显示）、界面同步性（激活后是否立即显示，还是等待5秒）
- Theory: Theory of Basic Gestalts (TBG); 信任转移 (trust transference); 协同特异性 (synergistic specificity)
- Theory-to-design: TBG 认为人类倾向于依据对象间拓扑关系进行整体化知觉；文章据此推导出三个设计属性：界面相似性（视觉属性接近→被归为一组）、界面嵌入性（处于同一平台边界区域→被归为一组）、界面同步性（用户操作后 app 同步响应→在时间维度上被归为一组）。这些属性被操作化为八版 app 的具体设计：与微信相同/不同的字体背景、在微信内/外显示、立即/延迟5秒显示。理论进一步通过信任转移机制预测分组感知会增强平台使用到 app 使用的正向衍生使用。
- Decision: 基础筛选通过：文章开发并真实部署了一个八种界面版本的信息型 App，并在微信平台环境中操纵界面相似性、嵌入性、同步性；其核心贡献涉及平台与 App 之间的衍生使用，且关键支持证据是后台日志记录的 App 客观使用行为及平台→App正向衍生使用路径。理论细筛通过：文章以感知心理学中的基础格式塔理论（TBG）前瞻性推导出三个界面设计属性，并将其操作化为明确软件制品的设计特征，再通过现场实验和客观使用数据检验该理论—设计链。
- Confidence: 0.88

## Ephemeral State-Dependent Recommendation for Digital Content

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2022.664
- Metrics: readrate; readtime; payment; 非推荐书籍阅读量（spillover counts）
- Objective evidence: 文章的核心研究问题是状态依赖推荐方案是否优于状态无关方案、以及 congruent 与 incongruent 方案应如何选择；主要实证分析以 readrate 和 readtime 为核心结果，payment 用于经济影响分析。通过大规模随机现场实验，Wald 检验显示 T3/T4 状态依赖方案显著优于 T1/T2 状态无关方案，T4 整体优于 T3，并估计可带来约 7.3%（1973 万美元）年收入提升。
- Artifact: 电子书平台的数字内容推荐系统，具体表现为移动应用中的个人虚拟书架推荐功能 — 文章设计了状态依赖推荐方案（ephemeral state-dependent recommendation scheme / strategy-state pairing），并通过简单的、基于规则的推荐算法实现：assimilation 策略从用户近7天阅读过的类型中随机选书，diversification 策略从近7天未阅读的类型中随机选书；推荐书目显示在个人虚拟书架顶部并标注为“recommended”。
- Theory: congruence theory; liquid consumption / ephemerality theory; variety-seeking theory and dual consistency-variety needs; schema effect; isolation effect
- Theory-to-design: 文章由 liquid consumption/ephemerality 理论识别出数字内容消费的短暂性和 ephemeral state（fixation/foraging）；再由 variety-seeking/双重需求理论得出消费者同时需要一致性与多样性，因此推荐系统应依据瞬时状态在 assimilation 与 diversification 策略之间自适应切换，而不是固定使用单一策略。随后，文章依据 congruence theory 将策略-状态配对划分为 congruent scheme（T4：fixation 时 assimilation，foraging 时 diversification）和 incongruent scheme（T3：fixation 时 diversification，foraging 时 assimilation），并将这两个状态依赖方案作为核心设计进行现场实验检验。该链条在实验实施前已形成，并由客观指标 readrate/readtime/payment 评价。
- Decision: 基础筛选通过：文章以 readrate、readtime、payment 等由平台系统记录的实际行为/交易指标作为最终目标与核心贡献，并通过随机现场实验验证状态依赖推荐方案带来的提升；这些指标不依赖主观感知。文章也明确将设计方案落实为电子书平台推荐系统内的策略-状态配对和简单规则推荐算法，属于对明确软件制品及其推荐模块的设计/改造，并用上述客观指标评价。理论细筛通过：文章使用 ephemerality/liquid consumption、variety-seeking 双重需求、congruence theory 等心理学/行为科学理论，在实验前推导出状态依赖推荐框架及 congruent/incongruent 两种具体方案，并用客观阅读和支付指标对这一理论-设计链进行了直接检验；schema effect 与 isolation effect 进一步用于解释机制。
- Confidence: 0.86

## A Novel Recommendation Model for Online-to-Offline Service Based on the Customer Network and Service Location

- Year/journal: 2020 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2020.1759927
- Metrics: F-Score; Precision; Recall
- Objective evidence: 文章的核心贡献是提出新的O2O推荐方法；实验部分用F-Score、Precision和Recall作为主要评价指标，并与多种基线方法比较（见Figures 3和4），证明CNLRec和CNRec在低数据密度下明显优于其他方法；因此这些指标是判断模型成功的主要依据
- Artifact: O2O服务推荐系统/推荐模型（CNLRec） — 推荐系统的核心推荐算法，包括客户网络构建（节点、边、tie strength）、客户属性估计、位置距离计算和综合排名规则
- Theory: 行为经济学中的‘花钱谨慎’理论（如情感会计、心理账户）; 消费者知识/经验理论（customer experience as knowledge）
- Theory-to-design: （1）花钱谨慎理论 → 购买服务比评分更真实反映偏好 → 因此用共同使用服务数量（co-used behaviors）而非评分值构建客户网络和tie strength → 预期提高推荐准确率（F-Score等）；（2）消费者知识理论 → 经验丰富的客户知识更丰富、评分更可靠 → 因此用行为活动（使用数量）和偏好多样性（度中心性）估计客户属性，并在推荐影响指数中给予较高权重 → 预期提高推荐准确率
- Decision: 基础筛选通过：文章以推荐系统的F-Score、Precision、Recall等客观指标提升为核心贡献，并通过设计CNLRec推荐模型（包含客户网络和位置模块）来实现。理论细筛通过：文章使用‘花钱谨慎’这一行为经济学理论和消费者知识/经验理论，前瞻性地推导了使用共同使用行为构建网络和估计客户属性的设计决策，并通过实验验证了这些设计对推荐性能的影响。
- Confidence: 0.85

## An intelligent decision support system prototype for hinterland port logistics

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2019.113227
- Metrics: total transport costs; total travel distance; total travel time; number of vehicles; total number of trips; vehicle utilization
- Objective evidence: 文章的核心贡献是量化智能DSS作为港口社区系统增值服务对腹地集装箱运输的影响，并通过模拟实验验证该DSS带来的节省；结果图（Fig.3和Fig.4）显示合作最优计划下总运输成本和距离降低超过50%，车辆利用提高，并且该结果用于回答两个研究问题并生成对不同规模货运代理是否合作的结论。
- Artifact: 作为港口社区系统（PCS）增值服务的智能决策支持系统（DSS）原型；在多智能体仿真软件中实现，包含PCS集中服务器、Web服务、优化和强化学习模块。 — PCS中的智能决策支持工具/模块：三种行动选项（维持现状、个体最优递送/取货计划、合作最优递送/取货计划）、基于概率匹配和强化学习的智能体概率更新模块、基于DVCRPTW的车辆路径优化与订单捆绑/资源协调模块，以及集中式DSS服务器架构。
- Theory: probability matching theory; Bush-Mosteller linear reinforcement learning model; bounded rationality / adaptive heuristics in decision making
- Theory-to-design: 理论命题：人在不确定环境中通过强化学习调整行为，成功行动被再次选择的概率上升，失败行动概率下降，并伴随探索性多样化。心理机制：代理基于过去收益更新对未来行动回报的信念。设计选择：DSS中每个货运代理在每个学习回合以概率P_an(e)从维持现状、个体最优计划、合作最优计划三个行动中选择，并用公式(1)中的RL规则更新概率；概率匹配和Bush-Mosteller模型直接指导了该行动选择机制。预期客观指标：在仿真中，该RL决策模块使代理逐步收敛到成本节省更高的行动，进而降低总运输成本、距离和时间并提高车辆利用率。
- Decision: 基础筛选通过：文章以智能DSS原型对港口腹地物流的客观绩效改进为核心贡献，使用总运输成本、距离、时间、车辆利用率等客观指标验证，且该DSS原型是明确的软件制品（PCS中的决策支持模块）并通过仿真评价。理论细筛通过：概率匹配理论和Bush-Mosteller线性强化学习等心理学/行为理论实质指导了DSS中智能体行动选择机制的设计，且该理论指导的部分由客观仿真结果直接检验。
- Confidence: 0.85

## How does scarcity promotion lead to impulse purchase in the online market? A field experiment

- Year/journal: 2021 / Information & Management
- DOI: 10.1016/j.im.2020.103283
- Metrics: impulse purchase (是否下单，0/1)
- Objective evidence: 文章将实际冲动购买行为作为核心结果变量，并明确指出以往研究多采用冲动购买意愿作为替代，本文以真实订单行为为最终因变量。第5.3节表7的logistic回归显示，知觉唤醒对冲动购买有显著正向影响（β=0.289，p<0.05），从而支撑稀缺促销通过唤醒促成实际冲动购买的核心主张。
- Artifact: 淘宝平台上的真实在线商店网页（电子商务在线商店/交互界面） — 在线商店网页中的稀缺促销信息设计：限时数量（LQS）设置为20 vs 200件商品，限时时间（LTS）设置为10分钟 vs 1小时；网页上呈现商品数量提示、促销时间提示、原价折扣价以及数量和时间信息的动态更新。
- Theory: Competitive arousal model (竞争性唤醒模型, Ku et al., 2005); Scarcity model / scarcity promotion literature (Aggarwal et al., 2011)
- Theory-to-design: 竞争性唤醒模型提出感知竞争和时间压力会提高唤醒；文章据此推导：LQS通过制造买家之间的竞争感（感知竞争），LTS通过制造决策时间压力，二者共同激发消费者知觉唤醒，进而导致冲动购买。这一理论推导决定了在线商店网页上应呈现受限商品数量和有限促销时间两种信息，并设置高低水平检验其效应。
- Decision: 基础筛选通过：文章以真实交易日志记录的实际冲动购买（是否下单）为核心结果变量，该指标客观可验证；同时，作者在淘宝平台上自建在线商店网页，通过操纵限时数量/限时时间这两种网页信息呈现与系统规则，检验促销设计对实际购买的影响。理论细筛通过：竞争性唤醒模型和稀缺促销理论在实验设计前前瞻性地推导了稀缺信息→感知竞争/时间压力→知觉唤醒→冲动购买的链条，并指导了网页稀缺信息的设计与操纵，且用实际购买数据进行了检验。
- Confidence: 0.85

## Understanding Security Vulnerability Awareness, Firm Incentives, and ICT Development in Pan-Asia

- Year/journal: 2020 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2020.1790185
- Metrics: CBL外发垃圾邮件量; PSBL外发垃圾邮件量; APWG钓鱼网站托管数; OpenPhish钓鱼网站托管数; Spam_PCA / Phishing_PCA; Borda count安全排名
- Objective evidence: 文章的核心研究问题就是安全漏洞指数披露是否能使企业改善安全防护；实证检验以垃圾邮件量、钓鱼网站托管数和Borda排名作为主要结果变量。DID结果显示治疗组CBL垃圾邮件量显著下降，打开邮件的2SLS效应更大，国家层面Borda排名显著改善；钓鱼网站在部分子样本中也出现显著下降，因此客观指标是论文判断设计方案是否成功的主要依据。
- Artifact: 安全漏洞指数信息与咨询系统，包括安全数据采集/映射/指数计算模块、咨询邮件发送系统和公开咨询网站。 — 文章明确开发了一个完整信息系统：每日从CBL、PSBL、APWG、OpenPhish采集数据，映射IP到企业，用Borda count构建安全漏洞指数；再设计并发送包含企业自身数据和同行排名的咨询邮件，并搭建支持搜索其他企业安全报告的公开咨询网站。
- Theory: 社会比较理论 (social comparison); 公开效应/声誉关注 (publicity/reputation effect)
- Theory-to-design: 在Theoretical background中，文章先提出信息公开可以缓解信息不对称，且公开披露会产生公开效应并引发社会比较，从而激励企业采取安全行动；据此，在设计干预系统时，咨询邮件包含企业自身垃圾邮件/钓鱼数据和行业/地区同行排名，并建立公开咨询网站使企业能查询其他企业的安全报告。这样企业会感知到与同行的相对差距和公开暴露风险，预期推动其减少外发垃圾邮件和钓鱼网站托管，从而改善客观安全指标。
- Decision: 基础筛选通过：文章以垃圾邮件量、钓鱼网站托管数和Borda安全排名等客观指标为核心结果，并通过设计、实现和运行一个安全漏洞指数信息系统来实现披露干预。理论细筛通过：社会比较和公开效应等心理学机制在实验设计前用于推导包含同行排名和公开披露的软件系统设计，并通过客观指标进行了检验。
- Confidence: 0.85

## Choose your own training adventure: designing a gamified SETA artefact for improving information security and privacy through interactive storytelling

- Year/journal: 2020 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2020.1797546
- Metrics: OSD composite index; actual OSD score
- Objective evidence: 文章明确提出降低OSD是SETA制品的首要目标，并在纵向随机对照实验中作为核心结果检验：文本版和视觉版干预在t2-t1和t3-t1均显著优于无干预对照组（文本p<0.001，视觉p<0.01），长期中文本版还优于传统邮件干预。态度和意图等主观量表也同时报告，但OSD行为是独立的核心目标，可由上述客观化指标支撑。
- Artifact: 可运行的交互式在线安全培训系统/游戏化SETA干预工具（文中称为artefact或system，视觉版以网站www.seta.games/cyoa展示） — 完整的CYOA风格交互式安全培训故事线，包括文本版和视觉版两个形式；具体组成部分包括背景场景、13个决策点、41个决策选项、8个后果场景、5个汇报/debriefing场景、基于决策的后果反馈、重新评估机制，以及第三方披露的社交子场景。
- Theory: transformation-oriented training理论/框架（Karjalainen & Siponen, 2011）; 自我决定理论（Self-Determination Theory; Deci & Ryan, 2000）; 媒体丰富度理论（Media Richness Theory; Daft & Lengel, 1986）; 认知负荷理论（Cognitive Load Theory，通过Jenkins et al., 2012; Shaw et al., 2009等实际使用）; 学习设计原则：story-based agent 与 reflection（Sheng et al., 2007; Quinn, 2005）
- Theory-to-design: 1）转化式培训与反思原则→让学习者联系亲身经验并重新评价决策→设计为CYOA故事中先让用户做OSD决策、经历威胁后果、进行后果性debriefing并回到原决策点重新评估→预期降低OSD。2）自我决定理论（选择、明确反馈支持自主和能力）→设计为13个决策点/41个选项和不含糊的后果反馈→预期增强参与并促进态度、意图和OSD变化。3）媒体丰富度与视觉记忆理论（视觉更生动、进入长时记忆，但也可能因多通道造成认知负荷）→设计为文本版和视觉漫画版两种格式并比较，预测视觉版在记忆与体验上更好、在改变OSD上更差。
- Decision: 基础筛选：文章通过设计科学方法构建了游戏化SETA培训制品，包含文本版和视觉版交互式故事，并通过纵向随机对照实验以OSD复合指数（并由实际OSD分数验证）为核心客观指标检验其降低在线自我披露的效果；满足要求A和B。理论细筛：文章使用转化式培训、自我决定理论、媒体丰富度理论和认知负荷理论等心理学相关理论，前瞻性地推导交互式故事、选择与反馈、文本/视觉格式等具体设计选择，并用客观与相关结果检验这些设计，因此满足要求C。
- Confidence: 0.84

## Enhancing AI-Assisted Purchase Decisions: The Role of the Sense of Autonomy

- Year/journal: 2026 / MIS Quarterly
- DOI: 10.25300/misq/2025/17607
- Metrics: product sales; product return rate; actual purchase behavior
- Objective evidence: 文章在摘要和结论中把真实产品购买和退货数据作为 AI 设计有效性的关键现场证据；Study 3B 明确以产品销量和退货率为结果变量，结果显示 AI 处理产品相比基线产品销量显著上升、退货率下降，且个人手机端设计的效果更强。该客观结果独立支撑了“改善 AI 辅助购买决策”的核心改进主张。
- Artifact: AI 服装推荐系统（store AI）及配套的个人智能手机端微信小程序/App — 文章设计并构建了个人智能手机端 AI 小程序，使消费者可扫描二维码在个人手机上使用原有门店 AI；同时也在门店 AI 屏幕上设计了高/低自主性的 AI 描述/界面提示信息。
- Theory: 自我决定理论/自主感 (Self-Determination Theory; Deci & Ryan, 2000); 自我聚焦理论 (Self-Focus Theory; Gibbons, 1990; Hull et al., 1988; Song & Sela, 2023); 心理所有权与调适理论 (Psychological Ownership and Appropriation; Brasel & Gips, 2014; DeSanctis & Poole, 1994; Zamani et al., 2022)
- Theory-to-design: 自我聚焦理论认为私人自我关注会使人更关注自身内部想法、价值观和感受；Song & Sela (2023) 表明使用个人智能手机能激活私人自我关注。文章据此推导：让消费者在个人智能手机上使用门店 AI，可增强私人自我关注，进而增强自主感；自主感促使消费者将自身独特偏好和需求纳入 AI 辅助决策，弥补 AI 的 uniqueness neglect，最终提升购买决策质量（购买意愿、满意度、信心以及实际销量上升、退货率下降）。心理所有权/占有理论进一步补充：个人设备使消费者对 AI 使用过程有控制权和支配感，从而强化自主使用。这一推导链直接转化为“个人智能手机端 AI 小程序”的设计选择。
- Decision: 基础筛选：文章以真实门店产品销量上升和退货率下降作为 AI 设计有效性的客观核心结果，并通过开发个人智能手机端 AI 微信小程序这一明确软件制品来实现该改进，因此基础筛选通过。理论细筛：自我聚焦理论、心理所有权/占有理论被用来前瞻性地推导个人智能手机端设计，并通过 Study 3A 的中介分析和 Study 3B 的现场客观指标直接检验，因此理论细筛也通过。
- Confidence: 0.84

## Addressing Online Users’ Suspicion of Sponsored Search Results: Effects of Informational Cues

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2021.0364
- Metrics: SSR点击行为（是否点击/非点击）; 眼动注视次数比例和注视时间比例
- Objective evidence: 文章的核心问题是用户怀疑SSR导致低点击率，研究目标是减少用户对SSR的回避、增加处理。三个实验均以SSR点击行为作为关键因变量之一进行logistic回归检验，并报告眼动数据作为认知回避的客观补充；例如实验1中无线索组26/30未点击SSR，商品质量评分线索组16/30未点击、卖家信用评分线索组18/30未点击，实验2和实验3也报告类似显著差异。因此客观行为指标可独立支撑“信息线索提高对SSR处理”的核心改进主张。
- Artifact: 模拟淘宝网的电商搜索结果页（实验用可运行网站/软件系统） — 搜索结果页中赞助搜索结果（SSR）旁边呈现信息线索的界面元素，包括商品质量评分线索、卖家信用评分线索，以及实验3中SSR评分与自然结果评分相对高低的呈现方式。
- Theory: 状态怀疑理论（state suspicion）; 说服内部化理论（internalization; Kelman 1961）; 认知吝啬鬼视角（humans as cognitive misers）; 说服知识/说服文献相关视角（persuasion knowledge, Campbell & Kirmani）
- Theory-to-design: 状态怀疑理论将怀疑分为决策不确定性、感知平台恶意和对SSR的处理三个维度；文章论证在SSR场景中，降低前两个维度可以提高用户对SSR的处理。内部化理论认为用户只有在将信息线索内化后才会改变对SSR的评价；认知吝啬鬼视角说明用户不会无条件处理线索，因此需要线索可信或可比较。由这些理论推导出设计选择：当SSR品牌知名时，在搜索结果页上附加高质量评分或高卖家信用评分线索，预期通过降低决策不确定性增加对SSR的处理；当SSR品牌不知名时，提高线索评分使其与顶部自然结果相当，预期通过降低决策不确定性和平台恶意感知增加对SSR的处理。
- Decision: 基础筛选通过：文章以降低用户对SSR的回避、提高对SSR的点击和处理为最终目标与核心贡献，点击行为和眼动数据是独立于主观判断的客观结果，且通过三个实验室实验得到验证。软件制品明确为模拟淘宝的搜索结果页，信息线索是该页面中被设计并操纵的明确界面元素。理论细筛通过：状态怀疑理论、内部化理论和认知吝啬鬼等心理学相关理论在假设发展和实验操纵中形成了“理论命题→心理机制→具体设计特征→客观指标”的可追溯链条，并直接检验了理论指导的设计部分。
- Confidence: 0.82

## Beyond Complements and Substitutes: A Graph Neural Network Approach for Collaborative Retail Sales Forecasting

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2023.0773
- Metrics: MAE; RMSE
- Objective evidence: 文章的核心贡献是提出并验证一种更准确的协作零售销量预测方法，摘要、引言、设计与实验部分均以 MAE/RMSE 的持续降低作为主要成功标准；Table 2 和 Table 3 显示 MS2RSF 在 h=1/4/8/12 下均优于 10 个基准，Table 4-7 的替换与消融实验也以 MAE/RMSE 验证了各设计模块的作用。
- Artifact: 图神经网络预测模型/端到端深度学习架构（CL4RSF/MS2RSF），作为协作零售销量预测的计算设计制品。 — 三个核心模块：同步与异步感知时间编码器 SATE、双通道产品关系学习器 DC-PRL、方向适用与关系自适应信息交互器 DRAI，以及整合它们的端到端多源多步预测架构 MS2RSF。
- Theory: Cross-Category Choice Dependence Theory (CCCDT); cross-category consideration; product bundling; cross-category learning; dynamic product dependency concepts from Shocker et al. 2004
- Theory-to-design: CCCDT 被用于前瞻性地推导产品关系类型：产品捆绑与跨品类考虑导出正向/负向关系，考虑集和消费链条导出间接/不对称关系，跨品类学习导出异步关系，动态市场环境导出关系类型与强度的动态变化。这些理论命题转化为需求 Req1、Req2-1、Req2-2，进而指导模块设计：DC-PRL 用图鲁棒损失和图对比损失识别稳定、非偶然的正/负相关产品；DRAI 用低频/高频谱信号分别聚合正/负关系并引入磁拉普拉斯处理不对称关系；SATE 与 DC-PRL 的虚拟节点机制处理同步/异步关系，注意力机制建模动态关系。最终通过 MAE/RMSE 的改进来检验该理论-设计链条。
- Decision: 基础筛选通过：文章以降低销量预测误差 MAE/RMSE 为核心目标和贡献，且通过设计并实现 CL4RSF/MS2RSF 这一端到端图神经网络预测架构来实现该目标并完成实证验证。理论细筛通过：CCCDT 作为消费者选择相关理论，实质指导了产品关系分类和 CL4RSF 中 DC-PRL、DRAI、SATE 等模块的设计，并通过消融/替换实验以同一客观指标进行检验。
- Confidence: 0.82

## Can Positive Online Social Cues Always Reduce User Avoidance of Sponsored Search Results?

- Year/journal: 2022 / MIS Quarterly
- DOI: 10.25300/misq/2021/14962
- Metrics: 是否点击赞助搜索结果（SSR）的二元行为指标; SSR区域注视百分比; SSR区域观看时间百分比
- Objective evidence: 文章的核心研究目标是降低用户对SSR的回避，并将行为回避明确界定为不点击SSR，认知回避用眼动注视比例测量。实验1至实验3均以这些客观指标作为假设检验的关键因变量，例如实验2中匹配条件下点击人数显著高于无线索条件，实验3同样以点击和眼动数据检验社会线索的效果；摘要和讨论也明确强调提高SSR的点击率和用户关注
- Artifact: 模拟的C2C电商搜索结果页面（类似淘宝网的交互式网页界面） — 在赞助搜索结果（SSR）旁边呈现不同类型正面社会线索的信息展示设计，包括销量线索、质量评分线索和卖家信誉评分线索；线索以固定像素矩形区域的形式加入到搜索结果页面中
- Theory: 社会影响理论（Kelman 1958; Kelman 1961）; 内化机制（internalization）; 抽象参照群体理论（abstract reference group）; 消费者内隐关注/朴素理论（implicit concerns / naive theories）; 广告回避三分类框架（认知、行为、情感回避）
- Theory-to-design: 社会影响理论指出，个体只有在认为参照群体意见有价值且与其当前关注相关时才会发生内化，从而改变对目标的评价和行为。文章据此推导：在SSR界面中，如果呈现的社会线索能够匹配用户此刻活跃的内隐关注（如销量线索匹配流行度关注、质量评分线索匹配质量关注、卖家信誉线索匹配卖家信誉关注），用户会内化该线索，改善对赞助产品或卖家的感知，进而减少行为回避（提高点击）和情感回避。这一理论链直接约束了“在搜索结果页面中应呈现何种社会线索”这一界面设计选择，而非任意设计
- Decision: 基础筛选：通过。文章以降低用户对赞助搜索结果的回避为核心目标，行为回避和认知回避分别用实际点击和眼动注视等客观指标衡量，且这些客观指标在实验1-3中直接检验了主要假设。研究通过设计模拟淘宝搜索结果页面并在SSR旁呈现不同类型的社会线索来实现干预，属于对交互界面信息呈现方式的明确设计。理论细筛：通过。社会影响理论、内化机制、抽象参照群体和内隐关注等心理学理论实质推导了不同社会线索应与用户活跃关注相匹配的界面设计原则，并通过匹配/不匹配条件的实验和客观点击等指标进行了检验。
- Confidence: 0.82

## Design Principles for Robust Fraud Detection:  The Case of Stock Market Manipulations

- Year/journal: 2021 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00657
- Metrics: Accuracy; Precision; Recall; F1; Robustness accuracy under simulated attack; Robustness F1 under simulated attack
- Objective evidence: 文章的核心贡献是构建可抵御欺诈者反制措施的稳健欺诈检测分类器；摘要直接以‘robust fraud detection’为问题，评价部分专门设置朴素评价和鲁棒性评价，并提出 H1、H2a、H2b 检验不同设计特征配置；Figure 4 显示在攻击下集成学习方法优于单一模型，支持了改进主张。
- Artifact: 欺诈检测系统（FDS）的核心分类组件：一个可运行/可实例化的 IT 制品，即基于 SVM 的稳健文档分类器实现 — 文档转换与特征设计（DF1a 词袋模型、DF1b 基于信息量/可读性/情感的 linguistic features）、自动化文档分类器（DF2 SVM 分类器）、组合特征集（DF3a）、集成学习与阈值混合分类器（DF3b，包括 Classifier A/B/C/D/E）
- Theory: 营销学中的广告效果与说服传播理论（Vakratsas & Ambler, 1999; Resnik & Stern, 1977; Abruzzini, 1967; Clark, Kaminski, & Brown, 1990; Chandy et al., 2001; Sonnier, McAlister, & Rutz, 2011）; 行为金融学中关于投资者信息处理、情绪与决策影响的理论（de Bondt, 1998; Bollen & Huina, 2011; Das & Chen, 2007）
- Theory-to-design: 文章从营销学中的广告效果理论出发，认为欺诈性股票推荐本质上是一种说服性广告；要让读者购买股票，推荐需要包含充分信息、易于阅读并具有积极情绪，因此这些理论推导出应使用信息量（entropy）、可读性（ARI/Flesch/Fog）和情感（polarity/positivity/negativity）作为文档特征，即 DF1b。行为金融学则支持投资者受情感/语气影响，进一步支撑情感特征。与此同时，作者假设欺诈者为了维持广告效果不会轻易改变这些语言学特征，因此将 linguistic features 与词袋特征组合并用于集成学习，从而形成 DF3a/DF3b 的鲁棒性设计。最终，这些设计被期望在模拟攻击下提高准确率、F1 等客观指标。
- Decision: 基础筛选通过：文章以自动欺诈检测分类器的客观分类性能和攻击鲁棒性为最终目标与核心贡献，指标由混淆矩阵客观计算；其制品是 FDS 核心分类组件，以 SVM 算法实现并实际评价。理论细筛通过：营销学和行为金融学中的说服、信息处理、可读性和情感机制被前瞻性地用于选择 linguistic features 并指导分类器及集成学习设计，并通过鲁棒性仿真予以检验。
- Confidence: 0.82

## Designing Attentive Information Dashboards

- Year/journal: 2022 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00732
- Metrics: Attentional resource allocation (基于 fixation duration 和 number of fixations); Attention shift rate (基于 AOI 间 transition pairs 的转换次数); Attentional resource management (基于六个 AOI 上 fixation duration / number of fixations 的标准差)
- Objective evidence: 文章将三个眼动指标作为检验设计原则的核心因变量，提出 H1、H2、H3，并通过 92 人受控实验比较个体化 VAF 与一般 VAF；结果显示三个假设均得到支持。这些结果支撑了文章关于个性化视觉注意力反馈能提升信息处理的核心贡献。
- Artifact: Attentive information dashboard（注意力感知的信息仪表盘软件制品），包含信息仪表盘子系统、眼动追踪子系统和注意力感知子系统；实际为自开发的实验软件。 — 实时眼动追踪与注意力计算模块、attention analyzer 组件、feedback generator 组件、个性化视觉注意力反馈（VAF）展示界面，以及用于实验的静态仪表盘布局。
- Theory: Broadbent 过滤器理论 / 注意力有限容量理论; Wickens 等的人类信息加工理论; Just 和 Carpenter 的眼-心假设; Corbetta 和 Shulman 的目标导向 vs. 刺激驱动注意力理论; Kahneman 的注意力与努力理论
- Theory-to-design: 理论链：注意力是有限资源（Broadbent/Kahneman）→ 用户在信息密集的仪表盘上难以管理注意资源；人类信息加工理论说明注意在感知、记忆等阶段的关键作用；眼-心假设表明眼动可作为注意的客观近似指标 → 因此设计 DP1：实时用眼动数据计算用户的注意资源分配；目标导向注意力理论强调用户自愿分配注意的机制 → 因此设计可控仪表盘并聚焦目标导向注意；自我觉知与自我追踪机制 → 将用户自身注视时长以个体化 VAF 形式反馈给用户（DP2），预期改善后续注意分配、降低注意转换率并提升注意资源管理。
- Decision: 基础筛选通过：文章以个性化视觉注意力反馈（individualized VAF）对注意资源分配、注意转换率和注意资源管理的改善为核心贡献，这些结果均由眼动仪记录的注视时长、注视次数、AOI 间转换次数和标准差等客观指标衡量，并通过 92 人受控实验与一般 VAF 对照验证；同时，文章明确设计并实例化了作为软件制品的 attentive information dashboard，因此 base_match=true。理论细筛通过：设计原则基于注意力有限容量、人类信息加工、眼-心假设等心理学相关理论，从理论推导出实时眼动注意力计算和个体化 VAF 设计，并以客观眼动指标直接评价该理论指导的设计，因此 theory_guided_subset_match=true。
- Confidence: 0.82

## Diversity Preference-Aware Link Recommendation for Online Social Networks

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1174
- Metrics: DPMS (diversity preference matching score); Precision; Recall; F1 score
- Objective evidence: 文章的核心贡献是提出多样性偏好感知的链接推荐问题与方法，DPMS直接度量该问题目标的满足程度，是方法成功与否的主要依据；同时用Precision/Recall/F1验证推荐被接受效果。表5-9在多个k值和数据设置下比较了所提方法与MMR、MSD、DPP、DiRec以及GCN-LR等，显示DPA-LR在DPMS和准确率指标上均显著更优。
- Artifact: 在线社交网络中的链接推荐方法/模块，可嵌入社交网络的‘好友推荐’功能。 — 多样性偏好感知的推荐选择/重排模块：在已有链接预测（如GCN）产生候选好友后，通过一个非线性0-1整数优化模型（Problem (1)）和迭代求解算法（Figure 1）为每个用户从候选中选择k个好友，使推荐好友的档案分布最大化匹配该用户在各档案维度上的多样性偏好。
- Theory: 同质性/异质性（homophily/heterophily）友谊形成理论; 人格与多样性偏好差异的社会心理学理论（如开放性、对变化/权威/顺从的偏好等）
- Theory-to-design: 社会心理学理论认为，不同用户对同质性朋友和异质性朋友的重视程度不同，因而具有不同的多样性偏好；同一个人还可能在不同档案维度上有不同偏好（Rivera et al. 2010）。文章据此在问题定义前引入用户多样性偏好的概念，并以‘使推荐好友的档案分布尽量匹配用户多样性偏好’作为推荐选择目标（Problem (1)的目标函数）。这一理论到设计的链条决定了优化目标、维度级处理和最终算法，而不是事后解释。
- Decision: 基础筛选通过：文章以DPMS、Precision、Recall、F1等可由档案计数和实际好友关系记录计算的客观指标作为最终目标和核心贡献验证，并设计了一个可嵌入在线社交网络链接推荐功能的多样性偏好感知推荐方法/模块。理论细筛通过：同质性/异质性以及个体多样性偏好的社会心理学理论在研究问题定义和优化目标设计之前被使用，形成了理论→心理机制→制品设计→客观指标的链条，并通过与GCN-LR、DPA-MMR等对比/消融检验。
- Confidence: 0.82

## Enhancing User Privacy Through Ephemeral Sharing Design: Experimental Evidence from Online Dating

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2021.0379
- Metrics: NumPhoto; NumFace; NumMatch; SumMsgFromReceiver / Ln(SumMsgFromReceiver)
- Objective evidence: 文章的研究问题和核心贡献是检验短暂分享设计是否提升个人信息披露、匹配结果和配对后参与，从而缓解冷启动问题。田野实验的回归分析（表5-7）显示，处理组相比控制组在NumPhoto、NumFace、NumMatch和Ln(SumMsgFromReceiver)上显著提高，例如照片数相对提高约52.1%，含人脸照片提高约61.6%，匹配数提高约3.3%，接收者消息提高约4.6%。这些指标是验证设计有效性的主分析对象，也是中介分析和异质性分析的依据。
- Artifact: 在线交友平台（Summer）移动应用中的匹配请求功能，具体为请求页/弹窗中的照片上传功能。 — 在用户发送匹配请求时新增并改造了个人照片上传功能：处理组提供“上传短暂照片（ephemeral）”按钮，以及对应的弹窗文案、图示和解释，照片接收后短暂可见且不可持久留存；控制组提供普通持久照片上传。
- Theory: Communication Privacy Management / Communication Boundary Management (Petronio 1991, 2002); Privacy Theory (Altman 1976); Uncertainty Reduction Theory (Berger & Calabrese 1974)
- Theory-to-design: 文章依据社交隐私顾虑理论识别出在线交友中用户因数据收集、传播、身份披露和身份滥用风险而不愿披露个人信息；据此提出采用短暂分享设计，使照片自动消失并限制接收者保存/转发，从而降低发送者的社交隐私顾虑。降低隐私顾虑后，发送者更愿意在匹配请求中附带个人照片（尤其含人脸照片）；同时依据不确定性降低理论，接收者看到主动披露后感知对方可信、降低互动不确定性，进而更可能接受请求并投入对话。该链条从理论命题（隐私边界顾虑）→设计特征（短暂性/自动消失/限制存转）→行为机制（隐私顾虑下降）→客观结果（照片披露、匹配、消息数）是明确的，并且文章在实验设计前即阐述了该推理，而非事后解释。
- Decision: 基础筛选：通过。文章以客观行为计数（个人照片数、含人脸照片数、匹配数、接收者消息数）为最终目标和核心贡献，并通过在在线交友平台移动应用中设计/改造短暂照片上传功能来检验；这些指标不依赖主观评价。理论细筛：通过。文章使用隐私边界管理/社交隐私顾虑理论和不确定性降低理论，前瞻性地将“短暂性/自动消失/限制存转”作为软件设计选择，以降低隐私顾虑、促进披露和匹配；并用田野实验中介分析和在线实验对该理论—设计链进行了直接检验。
- Confidence: 0.82

## How to elicit and cease herding behaviour? On the effectiveness of a warning message as a debiasing decision support system

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113652
- Metrics: 是否选择被同伴百分比信息所指向的选项（herded option）; 收到警告信息后是否更改选择/最终是否仍选择herded option
- Objective evidence: 文章的核心研究目标即为检验同伴信息能否诱发羊群偏差以及警告信息DSS能否降低羊群偏差；结果部分用logit模型检验这两个目标，例如同伴信息的几率比为1.876，警告信息的几率比为0.969且不显著。虽然警告信息未被证明有效，但文章仍以该客观行为指标作为判定设计效果的核心依据。
- Artifact: 金融决策指导网站及其中的两个DSS仿真工具，外加作为第二个DSS的警告信息弹窗 — 仿真工具中三种保险/退休储蓄产品选项的呈现方式，实验条件下为Premium选项附加随机生成的同伴选择百分比；以及被试做出初始选择后弹出的警告信息界面，并允许其修改初始选择。
- Theory: 羊群偏差/羊群行为理论（Herding bias）; 社会影响与从众理论（Social influence/conformity）; 认知偏差去偏方法（Debiasing techniques）
- Theory-to-design: 羊群偏差理论提出，个体会根据他人行为调整自己的决策，形成社会性学习或从众行为；由此，文章在仿真DSS的产品选择界面中为Premium选项附加随机生成的同伴选择百分比，以诱发和检验羊群偏差。去偏理论进一步指出，提供警告信息可提高用户对偏差的觉察，从而降低偏差影响；据此，文章设计了第二个DSS——警告信息弹窗，在用户完成初始选择后告知羊群偏差的存在以及百分比为随机生成，并让用户重新考虑选择。该理论—设计链最终指向的客观指标是用户是否选择herded option以及警告后是否改变选择。
- Decision: 基础筛选：文章的核心目标是检验和减少羊群偏差，使用系统记录的客观选择行为作为主要结果指标；该目标通过设计两个明确的DSS软件制品（仿真工具和警告信息弹窗）来实现。理论细筛：羊群偏差/社会影响理论和去偏方法被用于推导同伴信息呈现和警告信息设计，并通过随机对照试验中的客观选择指标加以检验，形成理论到设计再到指标的可追溯链条。
- Confidence: 0.82

## Learning not to take the bait: a longitudinal examination of digital training methods and overlearning on phishing susceptibility

- Year/journal: 2023 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2021.1931494
- Metrics: Discriminability (d'); Response bias (c); Mock phishing test scores (click-based score)
- Objective evidence: 文章的核心研究问题是不同反钓鱼数字训练方法和过度学习对钓鱼易感性的长期影响，所有假设均围绕三个客观因变量展开，并通过混合设计ANCOVA、计划比较和交互效应来验证。结果是正念训练相比规则训练和控制训练显著提高辨别力、降低模拟钓鱼点击；过度学习使参与者更谨慎并减少模拟钓鱼点击。摘要、假设、结果和讨论均以这些客观指标作为判断训练有效性和保留效果的主要依据。
- Artifact: 基于网页的反钓鱼数字培训程序（digital anti-phishing training program），通过 Qualtrics 在线平台以网页形式呈现 — 培训条件的内容与结构：规则基础培训中的六条建议、正念培训中的“停-思-查”三步训练材料、控制培训中的密码创建与管理内容；电子邮件识别练习及其反馈机制；过度学习条件中的额外六封联系邮件（100%过度学习）。
- Theory: 正念理论（Mindfulness theory; Langer, 1989; Brown & Ryan, 2007）; IT正念（IT mindfulness; Thatcher et al., 2018）; 过度学习理论（Overlearning theory; Fitts, 1965; Driskell et al., 1992; Arthur et al., 1998）; 双加工理论（System 1 / System 2; Vishwanath et al., 2011）
- Theory-to-design: 正念理论认为提高对当下的注意力和意识可以减少自动、启发式的行为反应，据此设计正念培训为三步程序：停止（在收到请求时暂停）、思考（关注请求的上下文和动机）、核实（向可信第三方确认）；该设计旨在促进系统化加工（System 2），从而改善邮件辨别力并降低钓鱼易感性，并通过邮件识别测试和模拟钓鱼测试中的客观指标检验。过度学习理论认为超过初始掌握点后的重复练习可强化记忆和技能保持，通过减少认知需求和增强自动性提高长期保留；据此设计100%过度学习条件，即完成6封练习邮件后再进行6封额外练习并继续提供反馈；该设计预期改善长期辨别力、反应偏向和模拟钓鱼得分。双加工理论用于解释规则训练可能鼓励启发式加工（System 1）、正念训练鼓励系统加工（System 2），从而指导对两种训练效果差异的假设和验证。
- Decision: 基础筛选通过：文章以邮件识别测试中的辨别力、反应偏向和模拟钓鱼点击得分作为最终目标与核心贡献，这些指标均来自客观行为记录或确定性规则，不依赖主观感知；文章设计并测试了一个基于网页的反钓鱼数字培训程序，包括不同训练内容和过度学习条件，这些设计直接接受客观指标评价。理论细筛通过：正念理论、过度学习理论和双加工理论均为心理学相关理论，并在设计前实质指导了培训内容、练习次数和反馈机制的设计选择，形成了从理论到设计再到客观指标的可追溯链条，且这些设计部分被客观实验结果直接检验。
- Confidence: 0.82

## RADAR: A Framework for Developing Adversarially Robust Cyber Defense AI Agents with Deep Reinforcement Learning

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2024/17339
- Metrics: evasion rate (ER); false positive rate (FPR)
- Objective evidence: 文章的核心贡献是提出RADAR框架以提升网络防御AI代理对对抗攻击的鲁棒性。在实验2中，RL-RO使LGBM、MalConv和NonNeg三种恶意软件检测器的平均逃避率分别下降约4倍、7倍和11倍，整体平均逃避率降低约84%（等价于鲁棒性提升约7倍）；实验1用逃避率衡量r-VAC生成的对抗攻击效果；实验3用逃避率和误报率评估重复博弈的鲁棒性。这些指标是文章判断设计方案成功与否的主要依据。
- Artifact: 网络防御AI代理（cyber defense AI agents），具体实例化为恶意软件检测器；整体RADAR框架被描述为可运行的设计科学IT制品（situated IT artifact），包含对抗攻击生成器和防御鲁棒化模块。 — RADAR框架及其两个核心软件模块：(1) Phase 1的r-VAC对抗攻击生成器，以神经网络策略实现，可对恶意软件执行文件进行离散功能保持修改；(2) Phase 2的RL-RO鲁棒化模块，通过对检测器模型的再训练/优化来增强防御。同时论文将三种开源恶意软件检测器（LGBM、MalConv、NonNeg）作为被实质修改的防御AI代理。
- Theory: Robust Optimization (RO); Reinforcement Learning (RL) 理论，具体包括 VAC/Variational Actor-Critic 和 Concrete distribution 的Gumbel-Softmax重参数化变分推断思想
- Theory-to-design: RL理论将对抗性攻击建模为马尔可夫决策过程：状态为恶意输入表示，动作为对恶意文件的功能保持修改，奖励为逃避检测器时的固定正奖励；该框架直接决定Phase 1中r-VAC的网络结构、动作空间、奖励设置和交互式训练环境。RO理论通过极大极小优化（内层最大化攻击者损失、外层最小化防御者损失）推导出需要有效对抗攻击仿真；该理论指导Phase 2中RL-RO的目标函数、训练循环和鲁棒化算法，使对抗攻击生成器的输出被用于重新训练检测器。VAC/重参数化理论指导了r-VAC采用Concrete distribution重参数化离散动作空间以改进梯度估计。通过这三个理论—设计链接，RADAR的软件制品设计选择（攻击生成策略、鲁棒化目标函数、动作/奖励设置）均从理论推导而来，并用逃避率/误报率客观验证。
- Decision: 基础筛选：文章以恶意软件检测器的逃避率下降（即鲁棒性提升）和误报率保持作为核心目标和主要评价指标，这些指标由检测器输出确定，不依赖人的主观感知；RADAR框架被明确设计为包含r-VAC对抗攻击生成器和RL-RO鲁棒化模块的软件制品，并在三种开源恶意软件检测器上进行了实质修改和客观评价。因此基础筛选通过。理论细筛：文章使用强化学习（RL）和鲁棒优化（RO）理论前瞻性指导软件制品设计，形成从理论（MDP/RO极大极小博弈）到设计（r-VAC策略网络、RL-RO目标函数与训练过程）再到客观指标（逃避率与误报率）的可追溯链，并通过实验1、2、3直接检验该理论—设计链。因此理论细筛通过。
- Confidence: 0.82

## A method for resolving organisation‐enterprise system misfits: An action research study in a pluralistic organisation

- Year/journal: 2023 / Information Systems Journal
- DOI: 10.1111/isj.12433
- Metrics: newborn hearing screening data completeness rate; percentage of newborns who should have had an ORL consultation but did not; rate of newborns with an appointment before hospital discharge; rate of newborns with positive screening who had follow-up ORL consultation
- Objective evidence: 这些客观指标是验证所提方法有效性的主要证据，用于证明解决Org-ES misfit的成功程度；Section 6.3 Evaluation step报告了2年后的比较数据，显示显著改善
- Artifact: Electronic Health Record (EHR) system — EHR系统的多个配置和功能模块：结构化数据采集表单格式（下拉列表）、预约模块权限与时段、查询构建、自动文件传输以及相关工作列表和警报系统
- Theory: Affordance theory and affordance actualization; User participation theory; Change agentry
- Theory-to-design: 文章以affordance actualization概念为核心，将misfit视为affordance的实际化、部分实际化和非实际化的组合；该理论指导诊断步骤，识别出具体affordance失败（如用户缺乏对预约模块的认知），进而指导具体的EHR设计选择（如修改输入字段格式、调整预约权限、创建自动传输）和组织调整；预期改善的客观指标为数据完整性和预约率等。完整链条为：affordance理论 → 用户感知与行为（对系统可能性的认知） → 具体EHR配置修改 → 客观指标提升
- Decision: 基础筛选：通过。文章以新生儿听力筛查过程的数据完整性、随访率等客观指标作为验证所设计方法的核心结果，指标来自系统和数据库可核查记录；文章通过实际修改EHR系统（如输入字段、预约权限、自动传输等）来实现这些指标改善，因此基础筛选两项要求均满足。理论细筛：通过。文章使用affordance actualization、用户参与和change agentry理论，其中affordance理论基于生态心理学，明确指导了EHR设计修改（如修改表单、权限配置），并通过客观指标验证了该理论-设计链。
- Confidence: 0.8

## Customer-centric prioritization of process improvement projects

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113286
- Metrics: 风险调整后预期净现值 (risk-adjusted expected NPV)
- Objective evidence: 论文的研究问题是如何以客户为中心对流程改进项目排序，所提出的决策模型以风险调整预期NPV为目标函数，NPV是方案比较和最优组合选择的核心依据。在评价部分，作者用软件原型对德国保险公司的真实案例计算了最优组合（31.8 MEUR）、仅强制项目组合（-12.7 MEUR）和最差组合（-14.7 MEUR），显示模型能够选出更高NPV的组合；稳健性分析也以NPV和最优组合变化作为结果。
- Artifact: 软件原型/基于模型的流程改进项目组合选择工具 — 经济决策模型在软件原型中的实现，包括NPV目标函数、客户满意度转换函数、项目类型与效果、项目交互和约束、组合优化及稳健性分析功能。
- Theory: 卡诺模型 (Kano model / attractive quality and must-be quality)
- Theory-to-design: 卡诺理论命题：基本、绩效、兴奋三类特征对满意度有不同的方向与强度的非对称影响，且顾客期望随时间提高、特征类型会切换。文章据此在DO.2中要求过程性能涵盖客户满意度，并纳入不同特征类型和时序变化；在设计规格中，将过程特征映射为卡诺类型（B/P/E），用履行度f量化期望-感知差异，在转换函数U中规定基本、绩效、兴奋特征的必须/可选函数形态（Table 1），并加入decay和switching points。这些设计进入软件原型的组合选择逻辑，最终通过满意度-收入关系进入NPV目标函数，预期选出能维持或提升满意度并提高NPV的项目组合。
- Decision: 基础筛选：文章以风险调整预期NPV最大化为决策模型的目标函数和核心评价标准，在保险案例中通过软件原型计算并比较不同项目组合的NPV，因此满足以客观指标提升为最终目标；文章明确将所提决策模型实现为软件原型，作为流程分析人员的工具应用于项目组合选择，因此也满足设计或改造软件制品。理论细筛：卡诺模型作为与客户满意度相关的行为理论，被前瞻性地用于推导过程特征类型、转换函数、切换点/衰减等设计选择，并嵌入软件原型中得到NPV检验，因此满足理论实质指导。
- Confidence: 0.8

## From Detractors to Enhancers: Harnessing the Power of Ad Customization for User Engagement on Media Websites

- Year/journal: 2025 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00907
- Metrics: visit duration (seconds); unique pages visited; return rate
- Objective evidence: 文章的核心研究问题、假设 H1a-c 和 H2a-c 均围绕这三项用户参与指标；主要贡献是证明 AQC 能提升用户参与。模型检验显示，AQC 相比默认广告显著提高访问时长（β=0.236, p<0.001）、唯一页面数（β=0.082, p<0.001）和回访率（β=0.309, p=0.025），补充分析也显示 AQC 相比无广告网站显著提高访问时长和唯一页面数。
- Artifact: 新闻媒体网站（European music news website）中的广告数量定制（AQC）功能/界面，以及配套的广告部署脚本。 — AQC 界面：向用户提供“常规广告量”“减少广告量”“无广告”三个选项，并配有预览草图；同时包括自编程脚本，用于向所有参与者统一部署相同的静态 banner 广告。基础条件（default ads）和无广告条件（no ads）也是在真实网站上通过实验性修改实现的对照设计。
- Theory: Psychological Empowerment Theory (Spreitzer, 1995; Thomas & Velthouse, 1990)
- Theory-to-design: 心理授权理论认为，当个体体验到自主选择、胜任感和影响力时，会更加主动和富有成效（Thomas & Tymon, 1994）。文章将该理论应用到 AQC 上：AQC 界面让用户自由选择广告数量，从而增强 self-determination；用户可按需调节广告量，增强 competence；选择会立即改变广告呈现，增强 impact。由此，理论推导出应提供 AQC 这一选择功能（而非任意设计或固定广告暴露），并预期其会提高访问时长、唯一页面数和回访率（H1a-c）。理论还进一步用于推导移动设备使用场景下的调节效应（H2a-c），因为小屏幕和较高认知负荷使控制广告数量的授权体验更为重要。
- Decision: 基础筛选通过：文章以点击流日志记录的访问时长、唯一页面数和回访率为核心结果指标，这些指标无需主观感知即可计算；文章在真实新闻网站上设计并实现了 AQC 广告数量定制界面及相关广告部署脚本，并通过随机现场实验以这些客观指标验证了该软件功能的效果。理论细筛通过：文章使用心理授权理论前瞻性推导 AQC 设计及其对用户参与的影响，形成“理论→心理机制（自我决定/胜任感/影响力）→AQC 选择功能→客观参与指标”的链条，并通过 AQC 与对照条件的比较检验该理论指导的设计。
- Confidence: 0.8

## Will Humans-in-the-Loop Become Borgs? Merits and Pitfalls of Working with AI

- Year/journal: 2021 / MIS Quarterly
- DOI: 10.25300/misq/2021/16553
- Metrics: human classification accuracy; unique human knowledge (UHK); wisdom of crowds/group accuracy
- Objective evidence: 研究问题和贡献集中讨论 AI 建议对个体准确率与 UHK 的影响，以及减轻 UHK 损失的干预措施；实验以准确率和 UHK 为主要因变量，并以众数模拟检验群体准确率。例如，实验1中 AI 建议使准确率从0.681升至0.799，UHK从0.123降至0.073；实验3中个性化建议使准确率不降（0.795 vs 0.773），UHK从0.074升至0.097；群体模拟中个性化建议保持优势。因此这些客观指标是核心贡献并被实际验证。
- Artifact: AI 辅助人机决策支持系统/图像分类建议界面（实验原型） — 界面上显示的建议功能：常规 AI 建议、AI 确定性信息、个性化建议决策规则（根据个体临界比决定是否显示建议）
- Theory: mental model / error-boundary awareness
- Theory-to-design: Bansal et al. (2019b) 的命题是：人类需要理解 AI 何时会犯错（error boundary），才能实现人机互补。该命题引出“展示 AI 确定性可让人类更好地区分正确/错误建议”的机制；设计上在 AI 建议旁附加确定性并将其映射到四点尺度；理论模型中将此表示为 s_t 改变建议影响；预期结果是保持/提升人类准确率并减少 UHK 损失。
- Decision: 基础筛选通过：文章以人类准确率、UHK 和群体准确率等客观指标为核心贡献，并通过设计/改造 AI 建议界面（常规建议、确定性显示、个性化建议）实现和检验这些指标的提升或不损失。理论细筛通过：AI 确定性显示设计受到“AI error boundary / mental model”这一心理学/HCI 构念的实质指导，并有实验证据评价；但个性化建议更多来自算法化临界比而非心理学理论。
- Confidence: 0.8

## Designing scalability in required in-class introductory college courses

- Year/journal: 2020 / Information & Management
- DOI: 10.1016/j.im.2019.103263
- Metrics: 自动批改系统误评率/准确率; 自动批改单份用时; 学生出勤率; 作业提交完成率; 外部资源使用与技能考试成绩的回归系数
- Objective evidence: 文章的核心是设计可扩展的课堂课程，并将自动批改反馈系统作为规模化关键组件；在Summative evaluation中，以自动批改误评率1.62%（人工平均5.23%）和单份5.25秒（人工平均10.63分钟）等客观数据证明其优于人工操作，同时用出勤率、完成率、DDS生成能力评估整体制品的可行性和扩展性。
- Artifact: 课程交付社会技术制品的软件组成部分：自研课程Web应用（MEAN栈，AWS托管）、Python自动批改系统、PDF反馈报告生成脚本 — 登录/行为追踪模块（Google Analytics + autotrack），作业与资源访问模块，自动批改引擎，静态报告/仪表盘，外部文档链接功能，云端部署与认证系统
- Theory: 干预理论 (Intervention Theory, Argyris 1970); 说服技术 (Persuasive Technology, Fogg 2003); 数字助推 (Digital Nudging)
- Theory-to-design: 干预理论的三原则（有效且有用的信息、自由知情选择、内部承诺）分别推导出MR1/MR4/MR5（DDS记录与数据暴露反馈）、MR2/MR3（行为与成绩脱钩、自愿练习与反馈）、MR6/MR7（信号/火花/促进触发器）；这些MR进一步转化为自研应用中的登录跟踪、自动批改、PDF报告、外部链接、触发器设计等具体软件功能，并预期改善出勤、练习完成、技能掌握等客观结果。
- Decision: 基础筛选：文章设计并实质修改了明确的软件制品（自研课程Web应用和自动批改系统），且以自动批改准确率/时间、出勤率、完成率等客观指标作为可行性/规模化判断依据，因此通过A和B。理论细筛：干预理论等心理学相关理论在MR/DP阶段明确推导了软件制品设计，且该理论指导的设计通过客观评价获得检验，因此通过C。
- Confidence: 0.79

## A social recommendation approach for reward-based crowdfunding campaigns

- Year/journal: 2020 / Information & Management
- DOI: 10.1016/j.im.2019.103246
- Metrics: Like Rate; Share Rate
- Objective evidence: 文章实验评价部分的主干是 5.1 节对点赞率和分享率的比较，并以图 12、13 和表 7、8 显示所提 phase-based 推荐方法在这两个指标上显著优于其他基准；摘要和贡献部分也将推荐机制的有效性作为核心贡献。虽然文章也报告问卷结果，但点赞率/分享率作为可追踪行为指标构成独立的客观有效性证据。需注意文章声称“提高众筹成功率”，但实际未追踪真实募资结果，而是用点赞/分享行为作为代理。
- Artifact: Web-based 众筹项目支持者推荐系统（web-based phase-based backer recommendation system），整合 Facebook 社交网络数据与 FlyingV/zeczec 众筹平台数据。 — 系统的主要组成模块：TypeTree 构建模块、社交关系分析模块、用户偏好分析模块（含支持者偏好、个人偏好、经济能力）、众筹推荐引擎模块（项目阶段判定、候选支持者分组、Suitability 聚合、推荐列表生成）。
- Theory: Social network theory / social tie; social influence; social trust; social capital theory; herd behavior and word-of-mouth effects
- Theory-to-design: 理论命题：强关系者之间信任更高，且强关系对高风险选择的影响更大；早期众筹资金常来自家人和好友；羊群效应使早期支持增加后期成功率。由此推导出机制设计：社交关系分析模块按互动强度与社交接近度计算 SocialRelationship，并将潜在支持者分为强关系/一般关系/陌生人群组；众筹推荐引擎根据项目阶段和距离选择不同候选支持者组，并在阶段1给社交关系最高权重（0.461）、阶段3给个人偏好最高权重（0.499）。这些设计选择直接由上述社会影响/信任/羊群行为理论推得，而不是任意选择。
- Decision: 基础筛选通过：文章以点赞率和分享率这两个系统日志记录的实际行为指标作为主要客观结果，比较所提 phase-based 推荐机制与多个基准并证明显著提升；该机制通过开发的 web-based 推荐系统及其明确模块（社交关系分析、用户偏好分析、推荐引擎等）实现。理论细筛通过：社会网络/社会连带、社会影响、社会信任、社会资本、羊群效应等理论在系统设计之前用于推导按强弱关系分组和按众筹阶段动态选择候选支持者的设计，并通过点赞/分享率获得实证比较。
- Confidence: 0.78

## AI-Augmented Content Validation in Behavioral Research: Development and Evaluation of the RATER System

- Year/journal: 2026 / MIS Quarterly
- DOI: 10.25300/misq/2025/18946
- Metrics: ROC AUC; Macro F1; Expected Calibration Error (ECE); Accuracy against author-specified item-construct assignments; F1-score; Cohen's kappa; Pseudo-R² / significance of predicting H&T human ratings; Factor loading prediction; Softmax-based representativeness proportions
- Objective evidence: 文章的核心贡献是提出并验证 RATER 内容效度评估系统，模型评选和系统验证都以客观指标为依据：Table 2 以 AUC/mF1/ECE 比较模型；Study 1 达到 92% 准确率；Study 2 显示 RATER_C 显著预测 H&T 评分；Study 3 显示 RATER_C 优于 BRASS；Study 5 用客观分数评估 representativeness。这些客观指标是最终目标和核心贡献的直接证据。
- Artifact: Web-based software system（RATER，www.contval.org），包含 web 前端、Excel 模板上传与结果下载、模型选择与阈值设置，以及 RATER_C 和 RATER_D 两个可替换 AI 模型模块。 — RATER 系统的整体设计：General Introduction、Prepare Your Instrument、Analyze Your Instrument 三个核心界面容器；侧边栏 General Options、Model Selection、Version Details；决策阈值与可读性预警功能；RATER_C classifier 和 RATER_D distribution 模型组件。
- Theory: Psychometric measurement theory / content validity theory; MacKenzie et al. (2011) construct measurement and validation framework; Hinkin and Tracey (1999) item rating procedure; Colquitt et al. (2019) definitional correspondence and distinctiveness criteria; Kerlinger (1973) representativeness and proportional coverage argument; Haynes et al. (1995) content validity approach
- Theory-to-design: 完整链条：内容效度理论规定条目应满足 correspondence、distinctiveness、representativeness（MacKenzie et al., 2011; Colquitt et al., 2019; Haynes et al., 1995）→ 由此确定 RATER 的任务是自动判断 item 与 construct definition 的语义匹配程度 → 设计上实现为 RATER_C 概率分类器和模拟 H&T 评分的 RATER_D 分布模型，并输出逐项 correspondence 与 distinctiveness 分数；依据 Kerlinger/MacKenzie 的多维构念代表性子维度比例思想，用 softmax 将模型分数转换为 representativeness 指标；依据 MacKenzie 可读性建议加入 Flesch 可读性预警。理论不是事后解释，而是前瞻性地决定了模型任务、输出类型、界面功能和评价维度。
- Decision: 基础筛选通过：文章以可自动计算的客观指标（AUC、Macro F1、ECE、准确率、与 H&T/因子载荷一致性等）为核心贡献，验证 RATER 内容效度系统，且 RATER 是明确设计开发的 web 软件制品。理论细筛通过：心理测量/内容效度理论体系前瞻性指导了 RATER 的模型任务、输出类型、representativeness 操作化和可读性设计，并通过多项客观研究直接检验该理论-设计链。
- Confidence: 0.78

## Combining review-based collaborative filtering and matrix factorization: A solution to rating's sparsity problem

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113748
- Metrics: MAE; Precision; Recall; F1
- Objective evidence: 摘要和贡献部分均将提高推荐准确性作为核心目标；实验通过 RMF 与 UCF、ICF、MF 比较 MAE，与 RTWCB 比较 Precision/Recall/F1，并用配对 t 检验验证显著性，表明 RMF 的准确率提升是文章的主要贡献。
- Artifact: 推荐系统（Recommender System）中的推荐算法/评分预测模块（RMF） — RMF 两阶段推荐算法，包括基于评论的协同过滤、物品-主题评分矩阵构建、评分填充、矩阵分解四个核心部分。
- Theory: Multi-Attribute Utility Theory (MAUT)
- Theory-to-design: MAUT 命题：消费者对产品的效用是多个特征质量的加权函数；由此推导出软件制品设计选择：从在线评论中提取特征级情感、计算特征质量和主题评分、构建物品-主题评分矩阵，进而计算物品相似度、进行评分填充和矩阵分解；这一设计并不是任意确定，而是由多属性效用观点直接导向的。
- Decision: 基础筛选通过：文章以推荐准确性（MAE、Precision、Recall、F1）为最终目标和核心贡献，并通过设计 RMF 这一推荐系统算法/模块在真实数据上验证改进，涉及可运行的软件制品组成部分。理论细筛通过：文章在设计确定前使用多属性效用理论推导特征级评分、物品-主题评分矩阵与评分填充策略，并以客观推荐指标对理论指导的设计进行了检验。
- Confidence: 0.78

## Customer Complaint Avoidance: A Randomized Field Experiment of Platform Governance Based on Value Co-Creation and Appropriation

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/17000
- Metrics: verified renter complaints; number of information updates by host; average length of voice calls with renters
- Objective evidence: 全文研究问题、假设和主分析均以投诉数为因变量，DID模型和表3直接比较各消息组与对照组的投诉变化；稳健性检验和机制分析（表4）进一步以信息更新和通话时长验证主动努力，说明这些客观指标是最终目标和核心贡献。
- Artifact: 移动端P2P长租平台及其消息通知/提醒功能 — 平台在邻居出现已验证投诉后向其他未受影响房东发送的提醒消息内容；具体是消息中包含的价值共创陈述（房东强调/租客强调）与价值分配陈述（竞争型/合作型）的组合。
- Theory: value co-creation perspective; value appropriation perspective; agency theory; tournament/competition-based incentive theory; free-riding/social loafing theory; cross-side network effect
- Theory-to-design: 价值共创理论认为顾客满意是平台与第三方房东共创价值的关键，因此文章设计租客强调/房东强调陈述来激发不同价值共创感知；价值分配理论、锦标赛激励理论和搭便车理论指出个人回报预期与集体奖励会改变自利房东的努力动机，因而设计竞争型/合作型陈述。H1-H4由此推导，并落实到实际提醒消息文本（Table A1）。主回归检验了这些设计对已验证投诉的影响，机制分析用信息更新和通话时长验证房东实际主动努力。
- Decision: 基础筛选：客观指标通过，文章以已验证投诉数、信息更新次数和通话时长为核心结果，且这些指标不依赖主观评分；软件制品通过，平台及其消息提醒功能构成被设计/改造的制品。因此base_match=true。理论细筛：价值共创、价值分配、代理理论、锦标赛激励、社会惰化/搭便车等理论前瞻性指导了消息文本设计，并通过客观投诉与主动行为日志检验，因此theory_guided_subset_match=true。
- Confidence: 0.78

## Delays in Information Presentation Lead to Brain State Switching, Which Degrades User Performance, and There May Not Be Much We Can Do about It

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2023/17680
- Metrics: decision time (s); go-trial error rate; no-go trial error rate; response time (ms)
- Objective evidence: Study 1将决策时间作为核心行为结果检验长延迟导致表现下降，并作为脑状态切换的中介结果；Study 2专门以反应时和准确率为指标评估四种设计干预，用随机截距回归比较各干预条件与短延迟/长延迟条件，得出干预可部分缓解但不能消除延迟负面效果的结论。
- Artifact: 数字化的信息呈现与交互实验系统（Study 2中的go/no-go警觉任务界面，包含延迟/加载屏幕） — 延迟期间的信息呈现与交互组件：四种设计干预——同时呈现个人绩效统计、逐步呈现个人绩效统计、倒计时器、延迟结束时插入的虚拟任务；以及长短延迟的Loading界面。
- Theory: default-mode network (默认模式网络)理论; brain state switching (脑状态切换); task switching (任务切换)理论; priming/注意力与走神理论
- Theory-to-design: 理论链：当无外部任务时大脑进入默认模式网络，从任务相关脑状态切换到其他状态；长延迟产生任务负性环境，导致脑状态切换；切换回任务状态需要时间和努力，损害速度与准确性。据此，Study 2的设计逻辑是：用任务相关统计信息（同时/逐步）、倒计时器或主动虚拟任务填充延迟，以保持大脑处于任务相关状态或提示其重新准备，从而减少延迟后的切换代价，改善反应时和准确率。
- Decision: 基础筛选通过：文章以决策时间、错误率和反应时等客观行为指标为核心评价标准，且在Study 2中通过设计/修改计算机化任务界面中的延迟期显示与交互组件（统计信息、倒计时、虚拟任务）来实现和检验性能改善。理论细筛通过：默认模式网络、脑状态切换、任务切换等认知/神经机制理论在干预设计之前被用于推导延迟期应填充任务相关信息或提供预提醒的设计，并用客观绩效指标检验。
- Confidence: 0.78

## Guided Diverse Concept Miner (GDCM): Uncovering Relevant Constructs for Managerial Insights from Text

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2020.0494
- Metrics: AUC; accuracy; precision; recall; F1; coherence score; learned concept recallability count
- Objective evidence: 相关性（relevance）是 GDCM 的三大核心 desiderata 之一，第 5.3 节专门用预测性能和概念系数验证该目标；表 10 和图 7 显示 GDCM 的 AUC 为 0.8885，高于所有可解释基线，并接近不可解释的 CNN/XGB 黑盒模型。第 5.2.2 节表 8 显示 GDCM 仅用 5 次运行即可召回 5 个 Garvin 概念，而 LDA、HSTM、sDTM、sLDA 等在 50 甚至 150 次运行中召回数量明显更少。第 5.1.2 节显示 GDCM 平均 coherence 为 -1.86，优于 LDA 的 -2.25，且区间不重叠。
- Artifact: 可运行的文本挖掘软件工具 / 深度学习算法 GDCM；代码公开发布于 GitHub — GDCM 的完整算法实现，包括概念分配网络、词-文档-概念共享嵌入网络、线性分类层，以及稀疏、多样性和分类三个损失函数模块。
- Theory: Prototype theory of concepts; Conceptual spaces theory; cognitive science concept criteria: lexicalization, conceptual coherence, differentiation, relevance
- Theory-to-design: 文章基于原型理论将概念定义为 (A, d, p)，据此把概念、词和文档嵌入到同一语义空间 A，概念向量作为原型 p，向量相似度作为距离 d；基于 differentiation 和认知经济性思想设置概念多样性正则，使概念原型彼此远离；基于 relevance 思想设置分类损失，使概念聚焦于能预测管理结果 Y 的区域。由此形成完整链条：心理学/认知科学理论命题 → 概念表征机制 → GDCM 的共享嵌入、概念原型、多样性/相关性损失设计 → 预期提升的概念一致性、召回数和预测 AUC。
- Decision: 基础筛选通过：GDCM 的核心目标之一是提取与管理结果高度相关的概念，并通过 AUC/准确率/召回数/coherence 等客观指标验证比多个基线方法的改进；该改进通过具体实现并公开代码的软件算法 GDCM 达成，不依赖主观评分作为核心判据。理论细筛通过：原型理论、概念空间理论等认知心理学理论实质性地推导了 GDCM 的共享嵌入空间、概念原型、多样性正则和相关性分类损失等软件设计，并由第 5 节的客观实验直接检验这些设计组件。
- Confidence: 0.78

## Mitigating Exposure Bias for Recommendations in Physical Spaces: An Unbiased Pairwise Ranking Approach Using Spatial Movement

- Year/journal: 2026 / Information Systems Research
- DOI: 10.1287/isre.2023.0100
- Metrics: Recall@N（Recall@1/3/5）; DCG@N（DCG@3/5）
- Objective evidence: 文章的核心贡献主张是UMPR方法能够提供更准确、更无偏的物理空间推荐；在真实商场数据上与多个基准方法比较时，Recall@N和DCG@N是主要成功判据。Table 4显示UMPR在所有指标上优于基准，Table 5通过消融进一步验证核心组件对指标的贡献，因此这些客观指标独立支撑核心改进主张。
- Artifact: 物理空间POI推荐系统/推荐方法UMPR（unbiased movement-aware pairwise ranking），属于可运行数字系统中的推荐模块，交付渠道可为移动App、数字屏幕、AI机器人等。 — UMPR方法整体及其明确组成部分：行人移动系统（空间网络构建、路径模拟、位置/方向/视觉范围建模）、移动感知推荐模型（曝光因子AC/VS/PO、移动成本因子DS/LD/DD/IV/DT、相关性评分公式）、无偏成对学习目标和交替随机梯度上升学习算法。
- Theory: 行人运动/空间选择行为理论（最短路径假设、agent-based movement simulation）; 行人方向保持与方向改变成本的行为命题（Antonini et al. 2006; Robin et al. 2009）; 视觉注意/可视性相关行为理论（Lu and Seo 2015; Cox and Cox 2002）; 沿路可见刺激导致分心/偏离计划的行为模型（Kłeczek and Wa˛s 2014）; 多目的购物与偏好动态理论（Leszczyc et al. 2004）
- Theory-to-design: （1）行人倾向保持移动方向、方向改变产生额外努力（Antonini et al. 2006; Robin et al. 2009）→ 设计Directional Difference（DD）移动成本因子，进入相关性评分 → 改变推荐排序，预期提升Recall/DCG；（2）视觉暴露和可见性影响注意（Lu and Seo 2015; Cox and Cox 2002）→ 设计Visibility（VS）和Invisibility（IV）因子，用于估计曝光和移动成本 → 预期改善无偏推荐；（3）沿路可见POI会吸引顾客并导致偏离计划（Kłeczek and Wa˛s 2014）→ 设计Distraction（DT）因子 → 提升移动成本建模精度 → 改善推荐效果；（4）同一行程中顾客会因多目的购物切换目标（Leszczyc et al. 2004）→ 设计访问序列的stage segmentation → 减少跨阶段偏好比较噪声 → 提升下一POI预测效果；（5）空间句法agent simulation和最短路径假设（Penn and Turner 2002; Farley and Ring 1966）→ 构建空间网络、路径和视觉范围 → 为上述因子提供可计算基础。
- Decision: 基础筛选：文章以提高Recall@N和DCG@N等客观排序指标为核心贡献，并在真实商场数据上用基准和消融实验验证了改进；同时，文章明确设计了UMPR推荐方法/推荐系统组件（行人移动系统、模型因子、学习算法），因此同时满足A和B，base_match=true。理论细筛：文章虽不标榜theory-driven，但在UMPR设计过程中，行人空间选择、方向保持、视觉注意、分心行为、多目的购物等行为/心理命题被用于推导移动成本、曝光因子和阶段切分等设计特征，且这些设计成分通过消融和因子分析得到客观检验，因此theory_guided_subset_match=true。
- Confidence: 0.78

## Ruckus in the Rentals, Seeking New Arrangements: Remedying the Impact of Home-Sharing on Urban Noise

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2024/18049
- Metrics: Noise_Complaints; 预测的噪声投诉数; 平台收入
- Objective evidence: 论文提出并评价的解决方案是平台端的助推算法，其最终目标是缓解噪声外部性；在仿真实验中，算法有效性的核心判据是预测噪声投诉数的下降（如w=0.55时降9.72%，扩展到NYC后降6.6%），同时检查收入差幅（w=0.75时收入差仅0.31%），因此客观噪声指标是该方案的核心贡献和成功标准。
- Artifact: 在线短租平台（如Airbnb类平台）的房源搜索排序功能/信息推送模块 — 一个“助推算法”（nudging algorithm），通过改变房源的显示排名，将潜在客人引导至靠近既有房源聚集区、同时又满足其偏好（相似度、偏好分数）的房源。
- Theory: 视觉注意/眼动研究（eye-tracking attention studies）; 威慑理论（deterrence theory）; 助推/选择架构（nudge/choice architecture，行为机制）
- Theory-to-design: （1）基于眼动研究：用户视觉注意力集中于搜索结果顶部，因此算法将目标房源排到顶部，提升其可见性，增加被选择概率，实现助推；该设计直接依赖注意机制。（2）基于威慑理论：执法行动对噪声形成震慑，房源空间/时间聚集会增强执法可见性和威慑传播，因此算法选用靠近已有聚集的房源作为推荐对象，以提升聚集度、强化威慑，最终降低噪声投诉。该链条从理论机制推导到了具体的房源排序设计。
- Decision: 基础筛选：论文提出了平台房源排序的助推算法，以降低噪声投诉这一客观指标为核心目标，并通过仿真实验以预测噪声投诉数、收入等客观指标验证了改进，因此满足要求A和B。理论细筛：算法设计中的顶部排序依赖视觉注意研究，推荐至聚集区以增强威慑依赖威慑理论，理论到设计、再到客观指标的可追溯链条成立，因此理论细筛通过。
- Confidence: 0.78

## The Relative Effect of the Convergence of Product Recommendations from Various Online Sources

- Year/journal: 2020 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2020.1790192
- Metrics: recommendation acceptance; 是否选择被多个来源共同推荐的产品（convergent recommendation acceptance）
- Objective evidence: 推荐接受是全文的主要因变量和核心贡献：研究问题、三个假设（H1-H3）以及三个实验均围绕其展开；实验2和实验3报告了各来源收敛组合的接受率，并用二元logistic回归验证RA∩专家组合显著高于专家∩消费者和RA∩消费者，且三来源组合未显著高于RA∩专家。实践建议也直接基于这一行为结果。
- Artifact: 实验用的电子商务购物网站（可运行的网页信息系统），其中集成了推荐代理（RA）、专家推荐和消费者推荐三种来源及商品选择功能。 — 网站中被设计或实质修改的部分是三种推荐来源的呈现与交互：RA偏好采集与推荐结果生成、专家和消费者的推荐榜单展示，以及为制造“推荐收敛”而操纵的推荐产品集合，尤其是RA输出列表与专家/消费者推荐列表的重合关系。
- Theory: 产品不确定性模型 (Product Uncertainty Model, ProU); 信号理论/信息信号文献 (Signaling Theory)
- Theory-to-design: 理论命题：ProU由DeU、PerU、FitU三维构成，同时减少三个维度的不确定性比只减少一两个维度更能提升推荐接受。据此推导：RA最能减少FitU，专家最能减少DeU和PerU，因此RA∩专家能同时有效减少三个不确定性维度，优于专家∩消费者或RA∩消费者。该推导直接转化为网站设计选择：在同一网站中集成RA、专家、消费者三类推荐来源，并通过操纵RA输出和专家/消费者推荐列表制造理论规定的不同收敛组合；实验用推荐接受率检验这些来源组合的差异。
- Decision: 基础筛选通过：文章以推荐接受率（实际产品选择）为核心客观指标，在专门设计的多来源电子商务网站上通过实验比较不同来源收敛组合的效果；该指标来自真实选择行为，不依赖主观评分。理论细筛通过：产品不确定性模型和信号理论前瞻性地推导出RA∩专家应优于其他两来源组合，并将该推导转化为网站中来源组合与推荐收敛的设计操纵，且用推荐接受率直接检验。
- Confidence: 0.78

## Combining Crowd and Machine Intelligence to Detect False News on Social Media

- Year/journal: 2022 / MIS Quarterly
- DOI: 10.25300/misq/2022/16526
- Metrics: PR AUC; F1 score; recall; precision
- Objective evidence: 文章的核心贡献是提出并验证CAND框架对虚假新闻检测性能的提升；在Empirical Evaluations中，以PR AUC、F1等作为主要评价指标，并与SVM、CNN、BERT、HSA、MV、BAM等基准比较，例如CAND-123将AUC从BERT的91.62%提升至97.54%。
- Artifact: CAND（Crowd-powered fAlse News Detection）框架，一个面向社交媒体虚假新闻检测的计算框架/检测管线。 — 设计了整个CAND框架：信息提取阶段提取机器判断、回应中的混合人机判断和举报数量，随后由无监督贝叶斯聚合模型CLNAM对三类判断进行聚合，并生成最终真假新闻预测。
- Theory: online disinhibition effect; wisdom of crowds
- Theory-to-design: 在线去抑制效应说明社交媒体用户看到不认同的新闻时，可能通过回应或举报等行为诚实表达怀疑，因此CAND将回应和举报设计为两类可扩展的群体智能输入；群体智慧说明大量未必可靠的个体判断在聚合后可以区分真假新闻，因此CAND/CLNAM显式建模真假新闻具有不同辟谣回应模式和举报分布，将回应是否辟谣建模为Bernoulli、举报数建模为Poisson，并与机器判断进行贝叶斯聚合。该理论链条直接指导了CAND框架中纳入群体判断这一核心设计选择。
- Decision: 基础筛选通过：文章以PR AUC、F1等客观分类指标为最终目标和核心贡献，设计并实现了CAND虚假新闻检测框架及其CLNAM聚合模型，属于明确的计算软件框架/检测管线，并用这些指标验证其改进。理论细筛通过：在线去抑制效应和群体智慧理论前瞻性地指导了纳入回应与举报两类群体智能的设计，并通过CAND-1/12/123比较得到客观检验。
- Confidence: 0.76

## A Field Experiment in Local Personalization for Charitable Crowdfunding

- Year/journal: 2026 / MIS Quarterly
- DOI: 10.25300/misq/2025/19044
- Metrics: email open rate; email click rate; donation rate; median household income of donation zip code; donation to high-income school indicator
- Objective evidence: 研究问题、假设H1a/H1b/H2a/H2b和主要结果均以engagement（open/click）和donation为核心结果变量；随机实验通过t检验和logistic回归验证了本地个性化显著提升这些行为指标（见表4、5、6）。H3的公平性后果也是该文的重要贡献，但仍由客观收入和学校指标测量。
- Artifact: DonorsChoose慈善众筹平台的个性化邮件外联模块/邮件营销功能，包括邮件内容与对应落地页 — 本地个性化策略：在邮件主题、preheader、正文和落地页中推荐捐赠者账单所在地附近的项目，替代平台默认的“最近支持项目所在地”个性化策略。
- Theory: 双加工理论/系统1-系统2（Kahneman, 2011）; 启发式与偏差：home bias、social influence; 同质性（homophily）; 马太效应/rich-get-richer（Merton, 1968）
- Theory-to-design: 双加工理论认为捐赠者倾向使用System 1启发式决策；home bias理论指出地理邻近线索能够激活身份认同、社区义务感和道德责任感；因此平台将邮件和落地页定位到捐赠者账单所在地（本地个性化）来触发该启发式，预期提高打开、点击和捐款。social influence理论认为通过转介首次捐款的捐赠者以对推荐人的人际信任为核心驱动，地点线索可能只增加注意但不会转化为捐款，由此提出H2a/H2b。homophily和马太效应理论则预测本地个性化会把资金引向与捐赠者相似且更富裕的社区，形成H3。
- Decision: 基础筛选：文章以打开率、点击率、捐款率等客观行为指标为主要结果，并通过随机字段实验检验了DonorsChoose平台个性化邮件外联中“本地个性化策略”这一明确功能组件的效果，因此通过基础筛选。理论细筛：文章使用双加工理论、home bias、social influence、homophily和马太效应等心理学相关理论，前瞻性地推导出本地个性化设计及其异质性后果，并用客观实验和结果指标加以检验，因此通过理论细筛。
- Confidence: 0.75

## Peak cubes in service operations: Bringing multidimensionality into decision support systems

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113442
- Metrics: AUROC
- Objective evidence: 论文的核心贡献是提出Peak cube多维峰值特征，并证明其能显著改进客户不满/流失预测；表3显示逻辑回归AUROC从64.04%提升到83.83%，LightGBM和SVM也有类似提升，Welch方差分析显示改进显著。
- Artifact: 客户流失检测/决策支持系统中的预测组件（defection detection DSS），以及开源的PeakCube算法与特征计算工具 — PeakCube算法、基于峰值立方体的多维特征集（如subspaceHitsEnd、dimensionalHitsEnd等）、以及基于这些特征训练的流失预测模型。
- Theory: peak-end rule（峰值-末端法则）; bounded rationality and heuristics（有限理性与启发式判断）; sequence effects（peak/end/trend/spread effects）
- Theory-to-design: 峰值-末端法则认为个体用体验序列中的最高点和结束点进行判断；该心理机制被推广到客户服务失败场景，即多维服务失败中的峰值可能引发不满和流失。传统研究只处理单维服务时间序列，因此作者依据该理论将峰值概念扩展到多维服务失败空间，设计PeakCube算法以提取所有子空间上的峰值特征，并排除较低维峰值对较高维峰值的混淆；这些特征被用于流失预测模型，预期改善AUROC。
- Decision: 基础筛选通过：文章以客观的AUROC提升为核心贡献，并明确将该改进归因于决策支持系统中峰值立方体特征和预测模型的组件。理论细筛通过：峰值-末端法则和有限理性等心理学相关理论在模型设计之前指导了多维峰值特征与PeakCube算法设计，并通过客观预测实验得到检验。
- Confidence: 0.75

## Long-term multi-criteria improvement planning

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113606
- Metrics: Rank/level increase (I(p), I*); Bottleneck penalty (Z(p), Z*); Operational change penalty (Φ(p), Φ*)
- Objective evidence: 文章的核心贡献是生成长期多准则改进路径，并将排名/等级提升作为需要最大化的核心指标之一；案例研究通过软件生成五条ULB在ARWU20中的改进路径，逐条报告Z(p)、Φ(p)和排名步数，并使用54组惩罚权重进行敏感性分析。
- Artifact: 开源决策支持软件工具（MCDMBM，以Python脚本和可执行文件形式提供） — 多准则长期改进路径生成模块：图构建、单准则改进步骤约束、瓶颈与运营变化惩罚函数、最短路径求解、权重敏感性分析与路径可视化界面。
- Theory: Resistance to change（组织行为/心理学概念）
- Theory-to-design: 文章引用Bovey & Hede（2001）和Dent & Goldberg（1999）等关于resistance to change的研究，指出运营层面的短期变动会引发抵抗并造成资源损失；据此，在设计改进路径生成规则时要求每一步聚焦单一准则，并在图模型中引入运营变化惩罚函数Φ*（式5），使相邻两步尽量保持同一准则或同一参照备选对象，从而在生成路径时最小化可能导致抵抗的运营变化；这一设计直接影响Φ(p)这一客观指标。
- Decision: 基础筛选通过：文章以提高实体在多准则模型中的排名/等级为最终目标，并同时最小化瓶颈和运营变更指标；这些指标均通过程序和明确公式计算，不依赖主观评分。文章还构建了开源决策支持软件MCDMBM，将框架实现为可运行的路径生成与分析工具，并用案例路径客观评价该工具输出。理论细筛通过：resistance to change这一心理学/组织行为机制被用于推导运营变化惩罚函数的设计，并成为软件路径生成与评价的一部分。
- Confidence: 0.68
