# Base matches

Completed: 2475 / 2475
Retained: 231

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

## A novel decision support system for optimizing aircraft maintenance check schedule and task allocation

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113545
- Metrics: 未使用飞行小时 (unused FH); 平均FH/FC; A检/C检总次数; 维护成本与收益（美元）; 额外维护槽数量; 飞机可用运营天数; 计算时间; 任务分配最优性差距（与商业求解器比较）
- Objective evidence: 论文的核心贡献是提出并验证一个集成化的飞机维修计划DSS，以客观KPI的改善作为成功依据：第4.1节显示与航司现行计划相比，DSS少1次C检和3次A检，同时提高平均FH；计算时间约10分钟；AMPO-2与商业求解器的最优性差距仅0.028%。第4.2节还用DSS评估不同维修策略，以总收益/损失、检查次数、额外槽位等客观指标比较情景。
- Artifact: 决策支持系统（DSS），一个独立的Python软件原型，已转换为Windows可执行文件 — 完整的DSS，包括数据库层、模型层和图形用户界面（GUI）；模型层包含AMPO-1维护检查排程模块、AMPO-2任务分配模块和AMPO-3班次计划模块。
- Theory: 
- Theory-to-design: 
- Decision: 基础筛选通过：文章构建了一个明确的DSS软件制品，其三个模型组件分别处理检查排程、任务分配和班次计划，并用未使用飞行小时、检查次数、成本收益、计算时间和最优性差距等客观指标验证了改进。理论细筛不通过：全文未以任何心理学相关理论指导DSS设计，设计依据是动态规划和装箱优化思想，因此不满足理论指导子集要求。
- Confidence: 0.96

## An interactive decision support system for real-time ambulance relocation with priority guidelines

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113712
- Metrics: average coverage rate (ACR); average response time (ART); average number of ambulances available to cover calls (ANAA); average workload of each ambulance in one shift (AWA); total working time of all ambulances in one shift (TWAA)
- Objective evidence: 论文将提高需求覆盖率、降低响应时间并减少总体工作量作为所设计 DSS 的核心目标与贡献；Section 5 的 Tables 8-11 将 DSS 推荐策略与静态政策对比，显示 ACR 从 73% 提高到 89%，ART 从 12.6 分钟降低到 8.2 分钟，TWAA 降低 9%，这些结果被用作系统有效性的主要结论。
- Artifact: model-driven decision support system (DSS) for real-time ambulance relocation — DSS 中的实时搬迁数学模型、过程模型、数据库、图形用户界面，以及实时搬迁风险评估（RRARR）指南模块。
- Theory: 
- Theory-to-design: 未形成从心理学理论命题到心理/行为机制、再到具体软件制品设计选择及客观指标的完整链条；DSS 设计主要由运筹学数学模型、覆盖率约束、响应时间目标和搬迁成本最小化驱动。
- Decision: 基础筛选通过：文章以覆盖率、响应时间、总工时等客观指标为最终目标和核心贡献，并明确设计、实现和评价了一个模型驱动的 DSS 软件制品（数学模型、过程模型、数据库和用户界面）。理论细筛不通过：全文未使用心理学理论实质指导软件制品设计，设计依据是运筹优化和风险评估方法。
- Confidence: 0.96

## Automated discovery of business process simulation models from event logs

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113284
- Metrics: BPTD (Business Process Trace Distance); ELS (Event Log Similarity)
- Objective evidence: 文章核心主张是自动化发现并优化BPS模型准确度：提出BPTD/ELS准确度度量，并用TPE搜索使准确度最大化的配置。实验以ELS为主要结果，比较基线与优化配置在三个日志上的表现，并用Mann-Whitney U检验证明优化显著提高准确度（P2P、ACR、MP），因此该客观指标是最终目标和核心贡献。
- Artifact: 自动化业务流程仿真模型发现软件工具（Simod，Python Jupyter Notebook开源工具） — 完整的Simod工具及其内部各阶段模块：控制流发现（Split Miner）、日志修复、日志重放、到达间隔/分支概率/处理时间/资源池等参数提取、仿真模型组装、BIMP仿真、BPTD/ELS准确度评估和TPE超参数优化。
- Theory: 
- Theory-to-design: 不存在可追溯的链条：没有心理学理论命题→被解释的心理/行为机制→Simod的具体设计选择→预期改善的客观准确度指标。文章没有用任何心理理论来推导或约束软件制品的设计。
- Decision: 基础筛选通过：文章以BPTD/ELS这一可自动计算的日志相似度作为核心目标，通过设计并实现Simod软件工具，从事件日志自动发现并优化BPS模型，且在三个日志上以客观指标验证。理论细筛不通过：全文未使用心理学相关理论指导Simod的设计，只依赖过程挖掘和超参数优化方法。
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

## Human Identification for Activities of Daily Living: A Deep Transfer Learning Approach

- Year/journal: 2020 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2020.1759961
- Metrics: Accuracy; Precision; Recall; F-1 Score; AUC; ROC
- Objective evidence: 研究的核心研究问题是设计DTL-HID框架，在物体运动传感器数据稀缺的情况下进行ADL执行者身份识别。摘要、研究缺口与贡献陈述均将身份识别准确率作为框架的核心目标和贡献。论文通过实验1-4系统验证改进：在HANDY上CNN-HID优于经典机器学习和替代CNN；在OPPO四个目标数据集上DTL-HID的micro-averaged accuracy（0.707）显著高于非迁移学习基准（0.407-0.570）和仅迁移单一依赖类型的DTL-HID/T（0.655）、DTL-HID/CA（0.667）。
- Artifact: DTL-HID deep transfer learning framework，作为面向物体运动传感器家庭ADL监测系统设计的软件/计算制品（IT artifact instantiation），用Python/Keras实现。 — 文章设计并实现了DTL-HID框架，包括：(1) CNN-HID模型，含新颖的三层卷积网络，使用1D卷积核提取单轴时间依赖、2D交互卷积核提取跨轴依赖；(2) DTL-HID算法，用于从可穿戴传感器源域到物体传感器目标域的知识迁移；(3) 数据预处理流程，包括PCHIP重采样、8秒滑动窗口分段和标准化。
- Theory: 
- Theory-to-design: 无。文章未建立“心理学理论命题→心理/行为机制→具体软件制品设计选择→预期客观指标”的可追溯链条。CNN-HID的卷积核设计、DTL-HID的迁移层选择、数据预处理和评估设计均由深度学习架构和信号处理考虑驱动，没有使用心理学理论来推导或约束设计。
- Decision: 基础筛选通过：文章以人类身份识别准确率、精确率、召回率、F-1和AUC等客观指标作为最终目标和核心贡献，并设计实现了DTL-HID深度学习框架这一明确的软件制品，通过多个实验验证其改进。理论细筛不通过：全文未使用任何心理学相关理论来指导DTL-HID或CNN-HID的设计；设计理由源于传感器信号特性、深度学习和迁移学习原理，而非心理或行为机制。
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

## A Deep Learning Approach for Recognizing Activity of Daily Living (ADL) for Senior Care: Exploiting Interaction Dependency and Temporal Patterns

- Year/journal: 2021 / MIS Quarterly
- DOI: 10.25300/misq/2021/15574
- Metrics: macro-averaged F1 score; precision; recall; Accuracy @1; Accuracy @2; Accuracy; average block Levenshtein distance (ABLD)
- Objective evidence: 文章以计算设计科学范式开发ADL识别框架，核心贡献是更准确的ADL识别，并通过四个实验（交互提取、手势识别、活动识别、端到端识别）对比多个基线模型，统计检验证明所提方法在F1、Accuracy和ABLD上显著更优。
- Artifact: ADL识别软件框架（IT artifact），包含I-CNN、启发式手势识别模块和S2S_GRU活动识别模块 — 设计了层级化多阶段ADL识别框架的全部组成部分：2D interaction kernel的I-CNN、启发式手势识别流程、GRU-based Seq2Seq活动识别模型
- Theory: 
- Theory-to-design: 不存在理论到设计选择的可追溯链条；设计主要受数据依赖模式（单轴、跨轴、跨传感器轴）和ADL层次分解启发，没有心理学理论指导具体的模块设计。
- Decision: 基础筛选通过：文章以ADL识别精度等客观指标为核心目标，并通过设计多层ADL识别框架（包含I-CNN、启发式手势识别、S2S_GRU）这一明确软件制品实现指标提升，相关实验验证了有效性。理论细筛不通过：全文未使用心理学相关理论指导软件制品设计，设计动机来自ADL层级和传感器依赖，而非人的心理或行为机制。
- Confidence: 0.95

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

## A decision support system for home dialysis visit scheduling and nurse routing

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2019.113224
- Metrics: total distance travelled (km); total travel time (min); number of required nurses; workload balance / maximum workload across nurses; travel and overtime cost
- Objective evidence: 论文的核心贡献是开发HDSS以优化家庭透析日巡访排程和护士路线，并以总行驶距离、行驶时间、所需护士数等作为最终目标和成功验证指标。第6节将HDSS结果与手工方案比较，典型周总距离降低27%，八周数据降低38%，并显示所需护士数降低11%–16%；表4、表5和表6用于验证改进。
- Artifact: 决策支持系统（DSS），命名为Home Dialysis Scheduler System（HDSS），是一个独立安装的可运行系统 — HDSS整体系统及其组成模块：优化模块（MILP模型）、地图模块、用户界面模块、可视化模块、报告生成模块和数据模块；其中核心是自动生成护士路线和患者访问时间表的MILP优化引擎。
- Theory: 
- Theory-to-design: 不存在从心理学理论命题到心理机制、具体软件制品设计选择和预期客观指标的可追溯链条。文章没有说明某个心理学理论如何推导出某个界面元素、交互机制或优化模型特征，也没有解释为什么该理论导致特定设计而不是其他设计。
- Decision: 基础筛选通过：文章核心目标是提升客观排程和路线指标（总距离、行驶时间、所需护士数、工作量平衡、成本），并设计了一个具体可运行的决策支持系统HDSS，其优化模块和界面模块构成软件制品，且用真实数据与手工方案比较验证了改进。理论细筛不通过：文章虽然声称采用以用户为中心的界面设计原则，但未引用或应用任何可识别的心理学理论，也没有建立从理论到具体设计特征再到客观指标的理论指导链，因此不满足心理学相关理论实质指导软件制品设计的要求。
- Confidence: 0.95

## A dynamic shipment matching problem in hinterland synchromodal transportation

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113289
- Metrics: total cost; computation time
- Objective evidence: 文章核心贡献是提出滚动时域方法和启发式算法以降低总成本，摘要和结论均以总成本为判断标准；实验对比滚动时域方法与贪心方法的总成本，以及启发式算法与精确算法的总成本和计算时间
- Artifact: 在线同步协调运输匹配平台（online synchromodal matching platform） — 平台的滚动时域决策模块和启发式求解算法
- Theory: 
- Theory-to-design: 
- Decision: 基础筛选通过：文章以降低总成本这一客观指标为最终目标，并设计了在线匹配平台中的滚动时域方法和启发式算法来实现该目标。理论细筛不通过：全文未引入任何心理学相关理论指导软件制品设计，仅使用优化和算法方法。
- Confidence: 0.95

## A dynamic simulation approach to support the evaluation of cyber risks and security investments in SMEs

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113580
- Metrics: 经济损失（欧元）; 收入损失百分比; 年度总成本（投资+损害，欧元）; 防御能力水平（Prevention/Detection/Mitigation）
- Objective evidence: 文章的核心贡献是支持SME评估网络风险并规划投资，其最终目标是通过模拟客观经济指标验证不同投资策略的效果；通过三个场景（Alpha中危、Alpha高危、Beta高危）对比损失百分比、总成本（表6）和成本-效益（表7），并使用配对t检验验证差异的统计显著性
- Artifact: 基于系统动力学的决策支持与模拟工具（SMECRA，SME Cyber Risk Assessment） — 整个SMECRA工具，包括Snapshot Survey问卷、系统动力学存量-流量模型、因果回路图、变量方程、投资分配的战略重点参数和动态仿真界面
- Theory: 
- Theory-to-design: 不存在从心理学理论到设计特征的推导链；系统动力学本身是建模方法论，而非心理学相关理论，没有理论命题指导具体设计选择（如变量选择、反馈回路结构、战略重点参数等），因此不满足要求C
- Decision: 基础筛选通过：文章以SMECRA系统动力学工具为核心，通过客观模拟指标（经济损失、总成本、防御能力）验证了该工具有效支持SME网络风险评价和投资决策，满足客观指标提升和软件制品设计两个要求。理论细筛未通过：文章没有使用可识别的心理学相关理论指导软件制品设计，系统动力学不属于心理学范畴，因此theory_guided_subset_match为false。
- Confidence: 0.95

## A prescriptive analytics framework for efficient E-commerce order delivery

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113584
- Metrics: delivery success rate; number of delivery attempts; total delivery cost; total distance traveled; number of vehicles
- Objective evidence: 文章核心贡献是提出并验证能提高配送成功率、降低配送成本的决策支持框架；通过对比基线和数据驱动策略，报告在Hub A和Hub B分别实现7.2%和10.2%的成本节省，并减少配送尝试次数和车辆数。
- Artifact: 决策支持框架（Decision Support Framework） — 框架整体由多个明确组件构成：配送成功预测模型、订单成功画像生成模块、配送时间窗推断模块、VRPTW调度模块（含基于插入启发式的调度算法与局部搜索改进）。
- Theory: 
- Theory-to-design: 无。全文未形成'心理学理论→心理机制→软件制品设计选择→预期客观指标改进'的推导链。
- Decision: 基础筛选通过：文章以配送成功率、配送尝试次数、配送成本等客观指标提升为核心目标，通过设计并实现一个决策支持框架（包含预测模型、订单成功画像、时间窗推断和VRPTW调度模块）来实现，并用模拟实验验证改进。理论细筛不通过：全文未使用心理学相关理论实质指导软件制品设计，设计由数据驱动和运筹优化方法决定。
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

## Algorithms to the Rescue: Market Mechanisms for Consensual Trading of Unbiased Individual Data

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2024.1115
- Metrics: Sample bias (B); Total compensation (TC); Total cost (Φ = TC + ω|B|); Exclusion (Z); Gini index of selection probabilities (G); Variance of selection probabilities (Vp)
- Objective evidence: 文章的核心贡献是设计一种市场机制，使平台能够以低成本和低偏差获取个体数据样本。理论命题（Proposition 2、3、5）和模拟结果均以偏差、总补偿、总成本等作为主要绩效比较指标，并证明RSP优于固定补偿和集中优化等基准。
- Artifact: 数据市场交易平台（data marketplace / intermediary platform） — 平台内的市场机制模块：第二补偿拍卖（second compensation auction）与随机滚动配对抽样算法（Random Sampling of Rolling Pairs, RSP），以及算法中涉及的数据排序、匿名化和补偿计算逻辑。
- Theory: 
- Theory-to-design: 不存在从心理学理论命题到设计选择的推导链。拍卖机制和抽样算法的设计源于经济学激励相容和成本最小化，而非任何心理学理论；文中提及的“隐私关心”是经济效用模型中的成本参数，并非心理学理论指导。
- Decision: 基础筛选通过：文章以客观指标（无偏性、总补偿、总成本等）为最终目标，通过设计数据交易平台中的RSP算法和补偿机制实现，并用理论分析和模拟验证。理论细筛失败：全文使用机制设计等经济学理论，未使用可识别的心理学理论实质指导软件制品设计，因此不属于理论指导子集。
- Confidence: 0.95

## An explainable lesion detection transformer model for medical imaging diagnosis decision support: Design science research

- Year/journal: 2025 / Decision Support Systems
- DOI: 10.1016/j.dss.2025.114492
- Metrics: MAP@0.50:0.95; MAP@0.50; MAP@0.75; MAR@0.50:0.95
- Objective evidence: 文章的核心贡献是提出EL-DETR以提高病灶检测的准确性和可解释性，并在四个真实数据集上通过与多种基线模型的比较实验验证了MAP和MAR指标的提升，这些指标是评价模型成功的主要依据。
- Artifact: 人工智能软件制品（AI artifact），具体为基于Transformer的病灶检测模型EL-DETR，并进一步实现为医疗影像决策支持系统。 — EL-DETR模型的完整架构，包括DCNN骨干网络、Transformer编码器-解码器、可解释分离注意力机制、混合匹配查询策略、高效复合损失函数；以及基于该模型构建的医疗影像决策支持系统。
- Theory: 
- Theory-to-design: 
- Decision: 基础筛选通过：文章以MAP、MAR等客观检测指标为最终目标和核心贡献，并通过设计AI软件制品EL-DETR（一种基于Transformer的病灶检测模型）来实现这些指标提升。理论细筛不通过：未发现心理学相关理论实质指导该软件制品设计。
- Confidence: 0.95

## Analytics with digital-twinning: A decision support system for maintaining a resilient port

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113496
- Metrics: Berth-on-Arrival (BoA) rate; Resilience level R(s)
- Objective evidence: 文章的核心贡献是提出并评价一个用于港口韧性计算与恢复行动选择的 DSS。案例研究以 BoA rate 作为关键绩效指标（KPI），通过比较默认行动与 DSS 推荐行动（Table 2），以及随机数字孪生与确定性数字孪生的 BoA rate（Table B.5 和 Fig. 5），验证了 DSS 的有效性。例如 Scenario 1 中 DSS 行动使 BoA rate 从 79.39% 提高到 91.90%。
- Artifact: 决策支持系统（DSS），可作为数字化码头操作系统（TOS）的规划级模块 — DSS 包含两个关键模块：恢复分析模块（由数字孪生模型和 OCBA 模拟优化算法构成）和韧性分析模块；数字孪生模型基于开源 O2DES.Net 框架构建，包含终端模块、船舶生成器、外部卡车生成器，以及岸桥、场桥、AGV 等资源子模型。
- Theory: 
- Theory-to-design: 
- Decision: 基础筛选通过：文章以客观指标 BoA rate 和韧性水平 R(s) 为核心目标与贡献，并设计、构建了 DSS（含数字孪生与 OCBA 模块）这一明确软件制品，且用该客观指标检验了系统效果。理论细筛失败：全文没有使用任何心理学相关理论指导软件制品设计，OCBA 是数学优化方法，数字孪生是工程仿真方法，均不属于心理学理论。
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

## Applied machine learning for a zero defect tolerance system in the automated assembly of pharmaceutical devices

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113540
- Metrics: False Negative Rate (FNR); False Positive Rate (FPR); Overall accuracy; Execution time / latency
- Objective evidence: 文章的核心贡献是提出并验证一种零缺陷容忍的ML质量控制系统；摘要和结论均以“检测100%缺陷产品”和“限制误拒数量”为主要成功主张。第6节在UC1和UC2中报告FNR=0，FPR分别为9.04%和2.32%，并验证执行时间远低于实时限制，直接支撑核心贡献。
- Artifact: 数据驱动的智能质量控制软件系统（ML-based QC system / decision support system），以Python软件原型实现 — 完整的多阶段软件算法流水线，包括k-means异常检测模块、由决策树/SVM/CNN组成的集成分类器、投票/元分类器决策方案、Grad-CAM解释可视化模块，以及Python实现中的信号预处理和重采样步骤。
- Theory: 
- Theory-to-design: 不存在“心理学理论→心理/行为机制→具体软件设计选择→预期客观指标改善”的完整链条。Grad-CAM和决策树的可解释设计源于工程可理解性需求，而非某心理学理论推导出的设计约束。
- Decision: 基础筛选通过：文章以零缺陷质量控制为最终目标，核心贡献是数据驱动的ML QC系统；该系统是明确设计并实现的Python软件制品；文章用FNR、FPR、运行时间等客观指标在真实工业数据上验证了改进。理论细筛不通过：文章没有使用心理学相关理论实质指导软件制品设计，仅提及可解释性和辅助决策等一般性设计目标。
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

## Automated dynamic approach for detecting ransomware using finite-state machine

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113400
- Metrics: TPR; FNR; FPR; Accuracy
- Objective evidence: 文章的核心贡献是提出并实现一个动态分析的勒索软件检测模型，其最终目标是提升检测效果。实验结果表明系统达到99.54%准确率、0% FPR，并与多种已有方法（Continella等、Lu等、Hampton等、Al-rimy等、Shaila等）进行比较，证明其改进效果。
- Artifact: Windows应用程序（勒索软件检测系统） — 系统由行为分析模块（包括监控用户文件、横向移动跟踪、监控系统资源、持久化活动程序四个组件）和决策制定模块（包括FSM模型和状态变更监听器）组成，并包含文件系统监视对象、事件监听器、内核模式编程组件等。
- Theory: 
- Theory-to-design: 不适用。文章中没有从心理学理论导出设计选择的链条。
- Decision: 基础筛选通过：文章以勒索软件检测的客观指标（准确率、假阳率等）为最终目标和核心贡献，并通过设计实现一个明确的软件制品（Windows勒索软件检测系统）来实现检测能力。理论细筛不通过：文章未使用任何心理学相关理论来指导系统设计，FSM属于数学/计算模型而非心理学理论。
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

## Background Music Recommendation on Short Video Sharing Platforms

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2022.0093
- Metrics: HR@N; NDCG@N; AL@N
- Objective evidence: 文章的核心目标是提高背景音乐推荐的准确性，并将HR、NDCG、AL作为模型性能的主要评价指标；通过与多种基线对比、消融实验、冷启动及不同数据子集实验，证明DL-BGM在这些指标上显著优于基线（如HR@5相对最好基线提升26.2%）。
- Artifact: 短视频分享平台上的背景音乐推荐系统（具体为所设计的DL-BGM推荐模型） — DL-BGM模型整体及其中的用户-音乐匹配模块、视频-音乐匹配模块、基于注意力机制的音乐特征聚合组件。
- Theory: 
- Theory-to-design: 
- Decision: 基础筛选通过：文章以HR、NDCG、AL等客观指标作为最终目标和核心贡献，并通过设计DL-BGM这一明确的推荐模型（软件制品组成部分）在真实数据上验证指标改善。理论细筛不通过：全文未使用心理学相关理论指导模型设计，设计依据是推荐系统与深度学习方法，而非心理机制。
- Confidence: 0.95

## Bayesian Stackelberg games for cyber-security decision support

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113599
- Metrics: 计算时间 (run-time, seconds); 优化变量数量 (number of optimization variables); 期望安全风险 (expected security risk / attack path success probability)
- Objective evidence: 文章核心贡献是高效精确求解贝叶斯Stackelberg博弈，从而为决策支持系统提供最优安全控制组合。评估部分以计算时间、变量数量和期望安全风险作为主要验证：Table 4/5显示在线优化比DOBSS、HBGS、HUNTER所需变量更少、时间更短；案例研究中在线优化将期望安全风险从0.0367降至0.00157，显著优于[1]的方法。这些客观指标是最终目标和核心贡献。
- Artifact: 网络安全决策支持系统 (cyber-security decision support system) — 系统的三个组成部分：预防优化模块、基于隐马尔可夫模型的学习与推断模块、在线优化模块（贝叶斯Stackelberg博弈求解器）；其中在线优化模块是重点设计部分。
- Theory: 
- Theory-to-design: 不存在可追溯的心理学理论到设计选择的链条。文章假设攻击者理性选择最优路径、防御者最小化期望风险，这是博弈论理性选择假设，不是心理学理论命题；没有从理论推导出具体软件设计特征，也没有解释为什么某一设计优于另一设计。
- Decision: 基础筛选通过：文章以网络安全决策支持系统为明确软件制品，以提高在线优化求解效率（更少变量、更短计算时间）和降低安全风险为最终目标与核心贡献，验证均基于可计算的客观指标。理论细筛不通过：文章未使用心理学相关理论指导设计；所用博弈论和优化理论不属于心理学理论，未形成理论到设计选择的链条。
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

## CATCHM: A novel network-based credit card fraud detection method using node representation learning

- Year/journal: 2023 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113866
- Metrics: AUCPR; F1; TP@k; PPT_A; revenue
- Objective evidence: 文章核心贡献是提出CATCHM算法以提升信用卡欺诈检测性能，全文以AUCPR、F1、TP@k等作为主要成功判断依据，并通过真实数据集上的基准比较、Bayesian检验、以及运营效率分析验证了CATCHM相对现有方法在主要指标上的改进
- Artifact: 欺诈检测软件方法/系统（CATCHM，可运行实现，代码已公开） — CATCHM的完整方法，包括三部分：三部分交易网络设计与人工欺诈节点、基于DeepWalk的归纳式池化扩展、下游XGBoost分类器优化与模型堆叠
- Theory: 
- Theory-to-design: 未发现心理学相关理论到心理机制、软件设计选择和客观指标的推导链；文中虽提及fraudsters合作等社会行为，但未以任何行为科学或心理学理论指导具体设计
- Decision: 基础筛选：文章以提升信用卡欺诈检测性能为最终目标，核心指标AUCPR、F1、TP@k、处理时间等均为客观可计算指标，不依赖主观感知；CATCHM是一个明确的软件制品（欺诈检测方法/系统），包含网络设计、归纳池化、分类器优化等明确模块，并在真实数据上验证，因此基础筛选通过。理论细筛：文章未使用心理学相关理论指导软件制品设计，方法设计均基于机器学习和网络表示学习技术，不满足要求C，因此理论细筛不通过。
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

## Combining analytics and simulation methods to assess the impact of shared, autonomous electric vehicles on sustainable urban mobility

- Year/journal: 2022 / Information & Management
- DOI: 10.1016/j.im.2020.103285
- Metrics: 未满足请求比例（share of missed requests）; 等待时间超过10分钟的行程比例; 车辆空闲时间/利用率; 车队规模 |V|; 充电桩数量 |P|
- Objective evidence: 作者的核心贡献是证明共享自动驾驶电动汽车能够在保持服务水平的同时大幅减少资源投入；摘要明确以‘substantially reduce resource investments while keeping service levels stable’为结论。第5节通过Table 3、Table 4、Table 5和Table 6等结果显示车队规模可从1104辆降至约600辆甚至更低，且充电桩数达到28个左右时未满足请求可降至0%；这些指标是判断方案是否成功的主要依据。
- Artifact: 基于Python的、模块化的Agent-based仿真平台（数据驱动决策支持系统），专门用于分析共享自动驾驶电动汽车系统。 — 作者设计并实现了完整的仿真平台，包括请求模块（Request Module）、任务模块（Task Module，含车辆再平衡/迁移决策和充电决策）、更新模块（Update Module）、需求预测分析模块，以及业务区域的蜂窝状离散化规则和车辆分配算法。
- Theory: 
- Theory-to-design: 不存在从心理学理论命题到制品设计的推导链。车辆调度、迁移和充电规则是由需求预测、距离、电池电量、阈值等运营逻辑决定的；例如式(1)中的迁移决策基于预测空闲时间和行驶时间，充电规则基于电池电量百分比。没有任何设计特征由心理学理论推导而来。
- Decision: 基础筛选通过：文章以仿真输出的客观指标（未满足请求比例、等待时间、利用率、所需车队规模和充电桩数）为核心贡献，并通过自主开发的模块化Agent-based仿真平台这一明确软件制品来产生和检验这些指标。理论细筛不通过：文章没有使用心理学相关理论来指导软件制品设计，设计依据是需求预测、调度优化和仿真方法，而非人的心理或行为机制。
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

## Cross-Lingual Cybersecurity Analytics in the International Dark Web with Adversarial Deep Representation Learning

- Year/journal: 2022 / MIS Quarterly
- DOI: 10.25300/misq/2022/16618
- Metrics: Accuracy; F1-score; AUC
- Objective evidence: 文章的核心贡献是开发CLHAD自动检测非英语暗网黑客资产，性能评价部分以Accuracy、F1-score和AUC作为主要依据，并与多种基线/基准方法（monolingual、MT-based、CLKT）比较；结果显示CLHAD在俄、法、意平台上均显著优于基准方法
- Artifact: 跨语言黑客资产检测系统CLHAD（IT artifact） — CLHAD整体框架，核心包括ADREL对抗深度表示学习方法（两个生成器和一个判别器）以及一个BiLSTM二元分类器
- Theory: 
- Theory-to-design: 
- Decision: 基础筛选通过：文章以Accuracy、F1、AUC等客观指标为核心贡献，并开发了明确的软件制品CLHAD（含ADREL和分类器）实现该目标。理论细筛不通过：文章没有使用心理学相关理论实质指导设计，设计依据是GAN和跨语言表征学习等计算/机器学习方法。
- Confidence: 0.95

## DNCP: An attention-based deep learning approach enhanced with attractiveness and timeliness of News for online news click prediction

- Year/journal: 2021 / Information & Management
- DOI: 10.1016/j.im.2021.103428
- Metrics: precision; recall; F1-score; accuracy
- Objective evidence: 文章的核心贡献是提出DNCP模型以提高新闻点击预测性能，第5.1节通过DNCP与13种基线/消融模型对比，展示DNCP在Sohu和Toutiao两个数据集上均显著优于所有基线，并进行了显著性检验。
- Artifact: 新闻点击预测深度学习模型（DNCP） — 整个DNCP模型架构，包括文本特征表示学习模块（BTM、BiGRU、CAM注意力机制）和元特征表示学习模块（FM），以及输出分类层。
- Theory: 
- Theory-to-design: 不存在从心理学理论命题到设计选择的完整链条。文章将“吸引力”和“及时性”作为特征引入模型，但设计依据是基于数据观察和工程经验，而非心理学理论推导。
- Decision: 基础筛选通过：文章以新闻点击预测的客观指标（precision/recall/F1/accuracy）为核心目标，并设计了DNCP深度学习模型这一软件制品来实现预测提升。理论细筛失败：文章没有使用心理学理论实质指导模型设计，仅引入“吸引力”和“及时性”作为特征，缺乏理论到设计的推导链。
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

## Designing Hybrid Mechanisms to Overcome Congestion in Sequential Dutch Auctions

- Year/journal: 2022 / MIS Quarterly
- DOI: 10.25300/misq/2022/16472
- Metrics: NumberOfRounds; PriceRange; S.D. of Price; WeightedAvgPrice
- Objective evidence: 文章的核心贡献是提出混合机制缓解序贯荷兰式拍卖的拥堵问题，并将市场出清速度（轮数）和价格稳定性作为主要绩效指标。理论模型预测运营效率更高且不损害分配效率；现场实验中DID估计显示Treatment×Post对ln(NumberOfRounds)为-0.177（p<0.001），约相当于轮数下降18%；对ln(PriceRange)为-0.270（p<0.001），对ln(S.D. of Price)为-0.205（p<0.001）；对收入的影响不显著。
- Artifact: 荷兰花卉拍卖行（DFA）的数字化拍卖时钟系统（digital auction clock system / projection-screen auction system） — 将传统序贯荷兰式拍卖的授予规则改造为混合机制：同一离散价格水平上的最高出价被批量合并，多个最高出价者可在同一轮中同时成交；仅当只有单一最高出价时仍按原机制进入下一轮。
- Theory: Häubl and Popkowski Leszczyc (2019) perceived competition intensity and willingness to pay
- Theory-to-design: 文章未建立从心理学理论到混合机制设计选择的完整推导链。机制设计的主要依据是拍卖钟的离散价格性质与缓解拥堵的直觉；文中提到观察多个竞争者购买可能被感知为竞争强度增加，但这是对机制可能后果的表述，且主要是在实证结果后用于解释价格稳定性，而不是在设计确定之前用于推导、选择或约束该软件制品中的具体规则。
- Decision: 基础筛选通过：文章以完成拍卖轮数、价格波动等客观指标作为最终目标和核心贡献，并通过在DFA数字化荷兰式拍卖钟系统上实现混合机制（批量处理同一价格水平的最高出价、允许多个赢家）来达成，DID分析基于交易日志客观验证了改进。理论细筛不通过：心理学相关的竞争强度感知仅在结果后用于解释价格稳定性，未被前瞻性地用于推导或选择该混合机制的设计特征，不构成理论指导软件制品设计。
- Confidence: 0.95

## Designing Personalized Treatment Plans for Breast Cancer

- Year/journal: 2021 / Information Systems Research
- DOI: 10.1287/isre.2021.1002
- Metrics: 平均辐射剂量 (Average Dose, Gy); 肿瘤控制概率 (Tumor Control Probability, TCP); 辐射诱发的肺癌和心脏病风险; 治疗成本节省（美元）
- Objective evidence: 平均辐射剂量和TCP是文章评价治疗计划的核心指标，贯穿框架设计和评估。文章通过模拟实验将所提出的个性化计划与标准均匀计划比较，显示在相同TCP目标下平均剂量降低超过90%（见表3、表4），并据此估算风险下降和每年超过2亿美元的成本节省，这些是该方案的主要贡献和验证。
- Artifact: 临床决策支持系统/放疗计划决策支持框架（clinical decision support framework for radiation treatment planning） — 框架的核心组件：预测模型（基于MTC和TCP的放射生物学模型）和优化模型（基于Adam算法的剂量优化模块），用于生成个性化放疗计划。
- Theory: 
- Theory-to-design: 不存在心理学理论→心理机制→软件设计→客观指标的推导链。虽然文章提到'decision-theoretic approach'，但这是数学决策优化，不是心理学理论。也没有用行为科学、人机交互或信息系统中的心理理论来推导任何设计特征。
- Decision: 基础筛选通过：文章以平均辐射剂量、TCP、副作用风险和成本等客观指标为核心贡献，并通过设计一个临床决策支持框架（预测模型+优化模型）在模拟中验证改善。理论细筛不通过：文章的设计由临床肿瘤学和数学优化指导，没有心理学相关理论实质指导软件制品设计。
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

## Discovering Emerging Threats in the Hacker Community: A Nonparametric Emerging Topic Detection Framework

- Year/journal: 2022 / MIS Quarterly
- DOI: 10.25300/misq/2022/15642
- Metrics: Precision; Recall; F-measure; Topic coherence; Processor time
- Objective evidence: 文章的核心贡献是提出NPETD框架，并通过实验证明其在检测新兴威胁列表上的有效性、效率和实用价值。表2显示NPETD在Recall、F-measure、Topic coherence上优于所有基线方法，在Precision上位居第二；图3显示NPETD在多数类别上取得最佳或接近最佳的F-measure，并在多个类别上大幅降低处理器时间。这些客观指标是评价框架成功与否的主要依据。
- Artifact: 新兴话题检测框架（Nonparametric Emerging Topic Detection framework, NPETD） — 整个NPETD框架，包括条件Hierarchical Dirichlet Process（条件HDP）主题建模组件、基于Bayes factor检验的涌现检测组件，以及基于随机变分推断的高效算法。
- Theory: 
- Theory-to-design: 不存在这样的链条。文章没有从心理学理论推导出任何具体的设计选择；条件HDP的构造、Bayes factor检验的采用、随机变分推断的运用均源于统计和计算效率考虑，而非心理学理论指导。
- Decision: 基础筛选通过：文章的核心目标是提升Precision、Recall、F-measure、Topic coherence和Processor time等客观指标，并实际构建了NPETD框架（软件制品）来实现这些提升，通过暗网市场实验验证了改进效果。理论细筛不通过：文章完全没有使用心理学相关理论指导设计，其设计完全基于统计学和机器学习方法。
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

## Geo-semantic-parsing: AI-powered geoparsing by traversing semantic knowledge graphs

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113346
- Metrics: Precision; Recall; F1-score; Elapsed time
- Objective evidence: 文章的核心贡献是提出并验证GSP这一geoparsing技术，其最终目标是提高地理编码性能；在NEEL16测试集上GSP取得F1=0.665，优于两个baseline和三个state-of-the-art技术（F1≤0.55），并通过消融和对比证明了召回率的大幅提升
- Artifact: GSP（Geo-Semantic-Parsing），一个AI驱动的geoparsing/geotagging软件系统或技术流水线 — GSP的完整处理流程：语义标注步骤（使用TagMe）、知识图谱水平扩展步骤（多种遍历策略）、最佳实体选择步骤（基于梯度提升回归）、地理坐标解析步骤（支持45种地理谓词）
- Theory: 
- Theory-to-design: 不存在从心理学理论命题到心理机制再到具体软件设计选择的推导链；例如Levenshtein距离、rdf2vec相似度、拓扑邻域遍历、LightGBM回归等设计均基于算法效果和知识图谱结构，而非心理学理论
- Decision: 基础筛选通过：文章以geoparsing任务的精确率、召回率、F1等客观指标为最终目标和核心贡献，并构建了GSP这一明确的软件系统或技术流水线，通过语义标注、知识图谱扩展、回归选择等模块实现指标提升。理论细筛不通过：全文没有使用心理学相关理论来推导或指导GSP的软件设计，设计依据是NLP和知识图谱等技术因素。
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

## Industry classification with online resume big data: A design science approach

- Year/journal: 2020 / Information & Management
- DOI: 10.1016/j.im.2019.103182
- Metrics: average adjusted R²; cross-industry variation
- Objective evidence: 文章在评价部分（Section 4.6.2）明确指出衡量行业分类效果的核心指标是解释股票收益变动的平均调整R²和跨行业变异，并在Section 4.7.3和4.7.4中将所提LMN方法与SIC、NAICS、GICS、HP、FDD、INM、MO等基线比较，结果平均调整R²提升（Table 4）和跨行业变异提升（Table 5），表明该指标是文章的核心贡献和最终目标
- Artifact: automatic industry classification architecture — 完整系统架构，包含三个组件：Resume Crawler（简历爬虫）、Network Constructor（网络构造器）、Industry Classifier（行业分类器）
- Theory: Resource-Based View; Resource-Related Industry Groups; skill relatedness
- Theory-to-design: 文章用Resource-Based View从人力资源角度论证行业分类的合理性（Section 2.2），但该理论并未推导出任何具体的软件设计选择，如网络构建方式、模块度最大化、层级聚类等均由网络科学和算法逻辑驱动，缺少从理论命题到心理机制再到设计特征的完整链条
- Decision: 基础筛选通过：文章以客观指标（股票收益解释力、跨行业变异）提升为核心贡献，并设计实现了明确的软件制品（自动行业分类架构）。理论细筛不通过：文章借鉴的资源基础观是管理学理论，不涉及心理学机制，也未对软件设计提供实质性的心理机制推导，因此不属于心理学相关理论指导的软件制品设计。
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

## Maximizing student opportunities for in-person classes under pandemic capacity reductions

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113697
- Metrics: Weighted in-person seats; Number of classes assigned to IP/SP; Coverage percentages of classes and seats; Solve time; Optimality gap; Average discrepancy
- Objective evidence: 文章将最大化面授学生机会作为优化问题的目标函数（第4节），并以两阶段框架在六个真实校园实例上的结果与贪婪算法基线对比（第7.6节、表2），证明了两阶段框架多分配约7%的课程和9%的座位，且报告了运行时间、覆盖率等指标作为核心贡献验证。
- Artifact: Decision Support System (DSS) — 两阶段优化框架：两个混合整数规划模型（Model A和Model B）、用于生成紧凑可行时段的预处理模型（Model S）、第二阶段差异最小化模型、数据过滤流程、可视化仪表板以及CSV输出等DSS组件。
- Theory: 
- Theory-to-design: 
- Decision: 基础筛选通过：文章以最大化面授学生座位数等客观指标为最终目标，通过设计和部署两阶段整数规划的决策支持系统实现该目标，并用真实校园数据对比贪婪算法验证改进。理论细筛不通过：全文没有使用心理学理论指导软件制品设计，仅提及学生反馈作为事后讨论，缺乏理论到设计的推导链。
- Confidence: 0.95

## Mitigating Bias in Hate Speech Detection With a Small Number of Expert Annotations: A Prompt-Based Learning Approach

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2025/18416
- Metrics: FPR; FNR; Macro-F1; ACC; Avg SP
- Objective evidence: 文章核心目标是设计一种能利用少量专家标注并缓解语言使用偏见的仇恨言论检测方法，并以FPR、FNR、F1、ACC和Avg SP作为主要成功标准。实验结果（表4-10）显示所提方法在WH16和VTWK21上均优于所有基准（p<0.05），在LGBTQ+数据集上也一致；组件消融与训练规模分析进一步验证了指标改善。
- Artifact: 基于LLM的自动仇恨言论检测系统（两阶段端到端检测框架） — 包括数据采样与组估计器、Stage 1对比学习模块（pair generator的仇恨目标检测器、候选构造器、候选排序器及SimCSE框架）、Stage 2 prompt-based learning模块（增强连续提示、软言语器），以及整个端到端可运行流程。
- Theory: 社会认同理论（social identity theory）; 民族语言认同理论（ethnolinguistic identity theory）
- Theory-to-design: 文章仅在文献综述部分引用这些理论解释语言使用差异导致偏见的现象，但未使用理论推导任何具体设计选择。例如，pair generator为何采用候选构造与排序、为何注入外部仇恨目标信息等决策，均基于对现有技术局限（术语替换无法改变句级语言模式、LLM可借助少量数据）和NLP技术推理，缺少“理论命题→心理机制→制品设计→客观指标”的完整链条。
- Decision: 基础筛选通过：文章以FPR、FNR、Macro-F1、ACC和Avg SP等客观指标作为最终目标和核心贡献，并通过设计一个基于LLM的两阶段端到端仇恨言论检测软件系统（包含对比学习、prompt-based learning等模块）来实现并验证改善。理论细筛不通过：虽然文章引用了社会认同理论和民族语言认同理论来解释语言偏见来源，但理论仅作为背景和问题动机，没有实质指导软件制品的设计选择；缺少从理论命题到具体设计特征和客观指标的推导链。
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

## S2SAN: A sentence-to-sentence attention network for sentiment analysis of online reviews

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113603
- Metrics: accuracy; training time; domain accuracy; overall accuracy
- Objective evidence: 文章的核心贡献是提出S2SAN模型，并在域特定、跨域和多域情感分析实验中，通过准确率作为主要指标与多个基线模型比较，验证S2SAN的最高平均准确率（如域特定0.788对比HAN 0.776），同时比较训练时间（平均减少25%）。这些指标直接证明了所提模型的改进效果
- Artifact: 深度情感分析模型（S2SAN） — 整个模型架构，包括句子表示层（BI-GRU + 词注意力）和文档表示层（多头的句子到句子注意力，用全局平均池化得到文档表示），以及分类层
- Theory: 
- Theory-to-design: 不存在理论到设计的推导链。文章提出的句子到句子注意力设计主要是基于对现有模型的缺陷分析（如HAN中使用序列模型编码句子），没有从心理学理论层面解释为什么句子间注意力会改善用户或模型的客观指标。因此不满足要求C
- Decision: 基础筛选通过：文章以S2SAN模型作为软件制品，通过提高准确率和降低训练时间等客观指标作为核心贡献，并在多个真实数据集上验证。理论细筛不通过：文章虽然提及注意力机制与人类视觉注意力的类比，但未使用任何可识别的心理学理论来实质指导模型设计，仅属于技术层面的类比或启发。
- Confidence: 0.95

## Secure attribute-based search in RFID-based inventory control systems

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113270
- Metrics: 安全性（非注入协议、抗重放攻击、抗冒充攻击）; 隐私性（标签匿名、标签不可追踪）; EPC标准合规性; 计算开销（门数）
- Objective evidence: 文章的核心贡献是提出了第一个属性搜索安全协议，并证明其在安全性和隐私性方面满足标准特性。通过与现有协议的对比（表1）和形式化验证（第4节），展示了其在抵抗攻击、保护隐私和符合EPC标准方面的改进。
- Artifact: RFID系统（包括RFID标签、读写器和后端服务器）中的安全属性搜索协议 — 设计了完整的属性搜索协议，包括消息交换流程、基于二次剩余的轻量级加密/解密机制、服务器端验证逻辑、标签端响应逻辑以及初始化阶段。
- Theory: 
- Theory-to-design: 不存在理论到设计的推导链。设计选择（如二次剩余、PRNG）均由密码学安全性和硬件约束驱动，而非心理学理论。
- Decision: 基础筛选通过：文章以安全性和隐私性等客观指标的提升为核心贡献，并通过设计RFID系统中的属性搜索协议来实现。理论细筛不通过：文章未使用任何心理学相关理论，设计纯粹基于密码学和安全协议原理。
- Confidence: 0.95

## Smart Markets for Real-Time Allocation of Multiproduct Resources: The Case of Shared Electric Vehicles

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2022.0204
- Metrics: gross profit; vehicle utilization; decision accuracy (confusion matrix); penalty costs
- Objective evidence: 文章的核心贡献是提出并评估FleetPower DSS以改善实时多产品资源分配。摘要明确表示“We show utilization and profit gains”；第5节以决策准确性、罚款、利用率和利润为主要评价维度；第6节总结利用率提升233%–700%、毛利提升1.8%–4.4%（Stuttgart 4.4%、Amsterdam 1.8%、San Diego 3%）。这些指标是文章验证设计成功的主要依据。
- Artifact: 决策支持系统（DSS），命名为FleetPower — FleetPower系统整体，包括五个阶段：市场与运营数据收集、资源规划、投标、资源重新规划和执行。核心组件包括机器学习预测模型（预测租赁需求和可用能量）、竞价价格计算、最优资源分配逻辑、以及应对短缺的重新规划机制。
- Theory: 
- Theory-to-design: 不存在。设计决策完全基于利润最大化、市场机制和机器学习预测，没有任何心理学理论命题推导到设计特征。例如，租赁需求预测使用特征集（w,h,o,g），但未解释这些特征如何由心理理论驱动，也未将任何心理学构念与设计选择建立因果链条。
- Decision: 基础筛选通过：文章设计了明确的软件制品FleetPower DSS，通过实时评估和投标机制将SEV资源分配到租赁或电力市场，以提升利润、利用率等客观指标为核心贡献，并用基于真实数据的模拟验证了改进，且这些指标不依赖主观感知。理论细筛不通过：文章没有使用心理学相关理论指导该软件制品的设计；其设计基于经济市场机制、运筹优化和机器学习，而非人的心理或行为机制。
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

## Automated Analysis of Changes in Privacy Policies: a Structured Self-Attentive Sentence Embedding Approach

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2024/17115
- Metrics: micro-averaged F1-score; micro-averaged precision; micro-averaged recall; micro-averaged Hamming loss; per-category F1-score and Hamming loss
- Objective evidence: 文章的核心贡献是设计SAAS自动标注隐私政策段落，并通过与常规机器学习和深度学习基准的对比实验证明其在F1-score和Hamming loss等客观指标上显著更优；消融实验进一步检验RWA和多标签分类器的作用，Amazon案例展示框架的实用价值。该分类性能是文章最终目标和主要贡献，而非附属结果。
- Artifact: 自注意标注系统（SAAS，Self-Attentive Annotation System），属于隐私政策演化分析框架中的自动文本标注软件系统/工具。 — SAAS的核心架构：基于BiGRU和multi-head self-attention的RSE（row-wise self-attentive embedding）模型、新增的row-wise attention（RWA）机制，以及共享参数的多标签分类器；还包括与ST-Ro分割工具结合的工作流。
- Theory: 
- Theory-to-design: 不存在“心理学理论→心理/行为机制→具体软件制品设计→客观指标”的完整链条。SAAS的设计由计算设计科学指南、SSASE在multi-label分类中的技术局限以及注意力机制等技术因素驱动；没有心理学理论被用于推导RWA或多标签分类器等具体设计选择。案例中对用户认知负担的讨论属于应用层面的解释，并非设计前的理论指导。
- Decision: 基础筛选通过：文章以SAAS在OPP-115上的F1、precision、recall和Hamming loss等客观分类指标提升为核心贡献，并设计、实现了一个明确的软件制品（SAAS自动标注系统），通过基准实验和消融实验验证其改进。理论细筛不通过：文章未使用心理学相关理论实质指导SAAS设计；设计推导基于ML/DL技术局限和计算设计科学，而不是人的认知或行为机制理论。
- Confidence: 0.93

## Cybersecurity vulnerability management: A conceptual ontology and cyber intelligence alert system

- Year/journal: 2020 / Information & Management
- DOI: 10.1016/j.im.2020.103334
- Metrics: SMIET分类准确率(Accuracy)、精确率(Precision)、召回率(Recall)、F值; 警报系统准确率(Accuracy)、精确率(Precision)、召回率(Recall)、F值; True Alerts比率、False Alerts比率、Alerts Discarded比率; SPARQL查询时间(毫秒)
- Objective evidence: 文章的核心贡献是设计CIA系统并声称其准确性、性能达到高水准。客观指标（如分类F-measure高达0.996、警报准确率95%、零假警报、丢弃率仅0.05%）直接证明该系统有效，并与先前工作（Mittal et al.和Lippmann et al.）比较以显示改进。这些指标是文章评价设计成功的主要依据，而非背景结果。
- Artifact: Cyber Intelligence Alert (CIA) system（网络安全情报警报系统） — 整个CIA系统，包括漏洞仓库（vulnerability repository）、社交情报提取-标注器（SMIET）、漏洞映射器（vulnerability mapper）、RDF转换器、CVO本体、CIO本体和网络警报规则引擎。
- Theory: 
- Theory-to-design: 不存在心理学理论到设计选择的完整推导链。文章的设计决策（如SMIET分类规则、警报触发规则、CVO/CIO结构）主要基于官方标准、先前实证研究和工程启发，而非由任何心理学理论推导得出。Bunge本体论虽影响了CVO的哲学基础，但它不是心理学理论，也未推导出CIA系统具体的交互或信息呈现机制。
- Decision: 基础筛选：通过。文章以设计CIA软件制品为核心，并以客观指标（分类性能、警报准确性、查询时间）作为主要评价依据，且与先前工作比较以体现改进。理论细筛：不通过。文章未使用心理学相关理论来推导软件制品设计；Bunge本体论和一般性认知论述均不构成心理学理论指导。
- Confidence: 0.93

## Taming Complexity in Search Matching: Two-Sided Recommender Systems on Digital Platforms

- Year/journal: 2020 / MIS Quarterly
- DOI: 10.25300/misq/2020/14424
- Metrics: AIC (Akaike Information Criterion) of fitted nonlinear models across simulation windows; Average student fitness; Average university fitness
- Objective evidence: 文章的核心主张是双边推荐系统能够驯服数字平台上的复杂搜索匹配问题并提升主体绩效。假设H1和H2分别以AIC降低和平均fitness提升为验证目标。结果表明双边推荐系统在student和university两侧的AIC均值均显著低于无推荐和单边推荐；回归结果也显示双边推荐系统相较无推荐使平均学生/大学fitness分别提高0.63/0.45，相较单边推荐分别提高0.31/0.13。这些指标是文章判断设计成功与否的主要依据。
- Artifact: 数字平台中的双边推荐系统（two-sided recommender system），作为平台内的软件软件组件/智能体 — 双边推荐系统框架及其推荐生成逻辑：对学生推荐课程注册、专业方向、同伴和讨论板；对大学推荐课程开设、专业方向和开设时间。该系统利用平台级数据感知学生端和大学端的涌现，并据此调整推荐。
- Theory: 
- Theory-to-design: 不存在心理学相关理论到软件制品设计的可追溯链条。文章从CABS理念推出‘不可约不确定性’和‘驯服复杂性’的设计目标，进而提出考虑两侧涌现的双边推荐框架；但这一推导来自复杂性科学和推荐系统文献，而不是心理学理论。推荐内容（按兴趣、难度、利用率等）主要依据平台运营目标、搜索匹配需求和仿真设定，没有由心理学机制的命题推导出来。
- Decision: 基础筛选通过：文章以可重复的仿真指标——AIC模型拟合值和学生/大学平均适应度——作为最终评价，指标客观可计算，不依赖用户主观感知；明确设计并实例化了双边推荐系统这一软件制品（数字平台中的推荐系统组件/智能体），并用这些客观指标与无推荐和单边推荐进行了比较。理论细筛未通过：设计主要由复杂性科学/CABS框架指导，未识别出心理学相关理论前瞻性地指导具体制品设计；‘学习’‘适应’等为系统层面的概念，不是心理学理论。
- Confidence: 0.93

## The Effect of AI-Enabled Credit Scoring on Financial Inclusion: Evidence from an Underserved Population of over One Million

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2024/18340
- Metrics: approval rate; default rate; utilization level
- Objective evidence: 文章的核心研究问题是AI模型对金融包容的影响，明确以审批率、违约率和使用率作为金融包容的度量。表4和表5的DID结果显示，AI模型使未充分服务人群的审批率提高0.150（相对+89.3%）、违约率降低0.009（相对-19.6%），同时提高使用率，因此这些客观指标是最终目标和核心贡献的验证依据。
- Artifact: AI-enabled credit scoring model（AI信用评分模型），作为银行个人贷款产品审批流程中的一个软件化决策模块 — AI模型本身，包括两层LightGBM集成学习模型、由弱信号和强信号生成的特征体系、特征筛选流程，以及与原有规则模型协同使用的决策矩阵。
- Theory: statistical discrimination theory; social capital theory（仅文献提及）
- Theory-to-design: 不存在从理论命题到心理机制、再到软件制品设计选择的完整链条。AI模型的设计目标、特征生成、算法选择和部署流程均围绕预测违约准确性展开，而非由心理学理论推导。统计歧视理论只在Abstract和Discussion等处以“findings are consistent with statistical discrimination theory”的方式事后解释结果，没有证据显示在模型设计之前用该理论选择弱信号、算法或审批机制。
- Decision: 基础筛选通过：文章以审批率、违约率、使用率等客观、可核验的借贷结果指标作为核心贡献，并通过DID验证AI模型的改进效果；该AI信用评分模型是实际部署在银行个人贷款审批流程中的软件化决策模块，文章对其开发、特征、算法和部署机制有明确说明。理论细筛不通过：统计歧视理论仅在结果解释层面被事后引用，没有在模型设计之前形成对软件制品设计选择的实质指导，因此不满足心理学相关理论前瞻性指导设计的要求。
- Confidence: 0.93

## A social investing approach for portfolio recommendation

- Year/journal: 2021 / Information & Management
- DOI: 10.1016/j.im.2021.103536
- Metrics: Portfolio Return; Treynor ratio; Jensen's alpha
- Objective evidence: 这些指标是文章评价推荐机制成败的核心标准。实验部分（Section 5）用这些指标对比了所提CIR机制与无过滤、知识型、权威型等基准方法，并报告CIR在回报、Treynor比率和Jensen alpha上均优于基准，构成了文章的主要贡献证据。
- Artifact: 投资组合推荐决策支持系统（decision support mechanism for investment portfolio recommendation） — 整个系统，包括特征词典构建模块、情感分析模块、知识分析模块、影响力分析模块、财务报表分析模块和投资组合构建模块。
- Theory: Behavioral Finance
- Theory-to-design: 文章没有建立从行为金融理论命题到具体系统设计选择的推导链条。虽然引言提到投资者非理性、情绪影响决策，但系统设计中的情感分析（基于词典的极性计分）、知识权威评分、财务报表评分等模块并未从行为金融理论中推导出来，而是基于集体智慧和数据挖掘的已有方法。理论仅在问题背景中起作用，未指导模块设计。
- Decision: 基础筛选通过：文章以投资组合回报率、Treynor比率和Jensen alpha等客观指标为核心目标，并通过构建和评估一个投资组合推荐决策支持系统来实现这些目标。理论细筛不通过：虽然行为金融学被提及作为问题背景，但文章未使用任何心理学相关理论实质指导系统设计，理论没有形成‘理论→心理机制→设计选择→客观指标’的完整链条。
- Confidence: 0.92

## A technique for determining relevance scores of process activities using graph-based neural networks

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113511
- Metrics: AUC_ROC; Sensitivity; Specificity
- Objective evidence: 论文将GRM的相关性分数有效性定义为预测质量（faithfulness），并以此作为核心评价标准；表3显示GRM在AUC上优于所有基线，在弱类敏感性和特异性上显著优于基线；表4显示去除最相关活动后AUC和特异性显著下降，从而验证了相关性分数的有效性和核心贡献。
- Artifact: Graph Relevance Miner (GRM)，一种基于图神经网络的过程分析软件工具/技术 — GRM的完整设计：事件日志转换为实例图、GGNN模型创建与训练、预测与相关性分数确定三个步骤。
- Theory: 
- Theory-to-design: 无
- Decision: 基础筛选通过：文章以预测质量（AUC等客观指标）作为核心评价，并通过设计GRM这一明确的软件工具来实现。理论细筛不通过：全文未发现任何心理学相关理论对GRM设计进行指导，仅依赖机器学习和神经网络技术。
- Confidence: 0.92

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

## How to Assign Scarce Resources Without Money: Designing Information Systems that are Efficient, Truthful, and (Pretty) Fair

- Year/journal: 2021 / Information Systems Research
- DOI: 10.1287/isre.2020.0959
- Metrics: instances of justified envy; number of students with justified envy; number of students envied; average rank of assigned course; Pareto improvement rate relative to ESDA
- Objective evidence: 文章的核心贡献是设计一个同时满足策略防伪、帕累托效率和低嫉妒的课程分配机制RESPCT，公平性和效率正是评价该机制的主要依据。第5节用10个现场数据集和多种最低配额场景比较RESPCT与ESTTC/ESPCT/ESDA，报告合理嫉妒、有嫉妒学生数、被嫉妒学生数和平均排名；结果显示RESPCT嫉妒实例数显著降低（通常减少3倍以上），且比ESDA约多10%的学生可被帕累托改进。
- Artifact: 课程分配信息系统/匹配系统（course assignment information system / matching system） — RESPCT匹配机制（Extended Seat Prioritized Clinch and Trade with a widened Range of guarantees），由克林奇（clinching）、优先指向（prioritized pointing）、最大化席位保证（maximizing seat guarantees）和扩展席位处理等模块组成，用于替换此前使用的DA机制。
- Theory: 
- Theory-to-design: 不存在由心理学相关理论到软件制品设计的可追溯链条。RESPCT的设计选择（如克林奇、优先指向、最大化保证席位）来自对TTC/ESTTC算法性质的数学分析和计算启发式，而非心理学理论推导。
- Decision: 基础筛选通过：文章以提高客观的匹配公平性（合理嫉妒实例数、有嫉妒/被嫉妒学生数）和效率（平均排名、帕累托改进率）为最终目标和核心贡献，这些指标均由偏好和优先级形式化计算，不依赖主观感知；同时文章设计并实现了RESPCT课程分配机制，并将其作为可运行匹配系统/信息系统的一部分进行部署和评估。理论细筛不通过：文章使用匹配理论和机制设计，属于经济/博弈论，而非心理学相关理论；没有心理学理论前瞻性地指导软件制品设计。
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

## Personalized Ranking at a Mobile App Distribution Platform

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1156
- Metrics: Expected Revenues; Platform Revenues; Click-through Rate (CTR); Conversion Rate (CR)
- Objective evidence: 文章的目标和核心贡献是设计个性化排名方案以提高平台收入（见摘要及第6节）。政策实验系统比较了多种排名方法，以非个性化均值效用排名为基准，展示个性化混合排名HMUM提升预期收入16.73%，且优于其他个性化方法。
- Artifact: 移动应用分发平台（app offer wall）上的应用印象排名系统/个性化推荐排序模块 — 设计了个性化排名算法，特别是混合效用和边际排名（HMUM）算法，以及与之比较的多种排序策略（基于效用、效用×边际、混合排序）；这些算法决定用户在offer wall上看到的应用排名顺序。
- Theory: 
- Theory-to-design: 缺乏从心理学理论命题到具体设计特征的可追溯链条。文章设计HMUM排名时使用的是基于效用和利润率的直观经济学推理（“顶部放置用户最可能点击的高效用应用并按CPA利润排序，其余按效用×利润排序”），没有通过心理学理论推导出该具体设计。分析模型虽考虑搜索成本，但并未形成心理学理论指导下的设计推导链。
- Decision: 基础筛选通过：文章以平台预期收入这一客观指标为最终目标和核心贡献，设计了移动应用分发平台上的个性化排名算法（软件制品），并利用用户点击/安装数据和CPA margins通过政策实验验证了收入提升。理论细筛不通过：文章未使用心理学相关理论实质指导软件设计，其设计推导主要基于经济学效用模型和直觉，缺乏心理学理论到具体设计特征的可追溯链条。
- Confidence: 0.92

## Preference enhanced hybrid expertise retrieval system in community question answering services

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2019.113164
- Metrics: MRR; P@N; R@N; Accuracy; MSC@N
- Objective evidence: 文章的核心贡献是提出并验证 PEHER 专家检索系统，目标是提高新问题专家预测的客观表现；通过与 20 个既有方法在 4 个数据集上的比较，报告 368/400（92.00%）个对比情形下 PEHER 最佳，并以多个消融实验验证各组件贡献。
- Artifact: 面向社区问答服务的偏好增强混合专家检索系统（PEHER） — PEHER 系统本身，包括 preferability estimator、authority estimator、expertise estimator；具体模块为 question preferability finder、profile familiarity estimator、network constructor、authority calculator、question similarity finder、proficiency estimator、expert list generator，以及新的融合策略算法（Algorithm 2）和修改后的 CBEN 网络权重方案。
- Theory: 
- Theory-to-design: 不存在完整的理论—心理机制—设计—指标链条。文章仅在第 4.1 节注明 intra/inter-profile 概念受 [33]、[34] 等文献启发，随后直接用词频统计定义偏好分数；没有从任何心理学或行为理论推导出具体设计选择，也没有解释为什么该理论导致这些公式或模块设计。
- Decision: 基础筛选通过：文章以专家检索的客观指标（MRR、P@N、R@N、Accuracy、MSC@N）提升为最终目标和核心贡献，并通过完整实现和评估 PEHER 这一明确软件系统来实现；该系统包含多个可识别软件模块。理论细筛不通过：虽然文中出现 'preference'、'intra/inter-profile' 等术语并引用偏好选择文献，但没有用任何心理学相关理论前瞻性地推导 PEHER 的设计，也没有形成理论到设计再到客观指标的链条。
- Confidence: 0.92

## Providing more regular road signs infrastructure updates for connected driving: A crowdsourced approach with clustering and confidence level

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113443
- Metrics: 精确率（precision）; 召回率（recall）; 真阳性率（TPR）; 假阴性率（FNR）; 假阳性率（FPR）; 假阳性检测数（FP）; 假阴性检测数（FN）
- Objective evidence: 论文的核心贡献是提出并验证一种基于众包摄像头检测整合的道路标志更新方法，重点是整合算法和置信水平计算，用于消除GPS误差和误检/漏检。实验1将整合结果与真实道路标志比较，显示整合精确率为94.7%、召回率为100%，全部消除了原始误检；实验2模拟融合云端整合标志与车载摄像头检测的系统，相比仅使用摄像头，真阳性率从80.1%提升至86.8%，假阴性率降低33.5%，假阳性率降低94.4%。这些客观指标直接支撑了论文的核心改进主张。
- Artifact: 云端众包道路标志整合平台（crowdsourced road sign consolidation platform / cloud-based processing framework） — 平台中的道路标志观测整合模块（consolidation module），包括滑动时空查询、地理分块、meanshift聚类、聚类细化、负观测计算以及基于贝叶斯概率的置信水平计算；实验2还模拟了一个合并云端整合标志与车载摄像头检测的车载融合系统。
- Theory: 
- Theory-to-design: 不存在从心理学理论命题到心理机制、具体制品设计和客观指标的完整推导链。例如，文章提到的“驾驶员注意力”“更安全”“信任”等表述属于一般性背景或未来讨论，并未作为设计依据推导任何软件模块；置信水平计算中的指数衰减类比的是地球物理、放射性和用户建模中的数学形式，并不包含心理机制的使用。
- Decision: 基础筛选通过：文章以不依赖主观感知的客观指标（精确率、召回率、TNR/FNR/FPR等）提升为核心目标，通过设计云端众包道路标志整合平台及其整合模块来实现，并用两阶段真实道路数据实验验证。理论细筛不通过：文章没有使用心理学相关理论指导软件制品设计；其方法依赖贝叶斯概率、聚类和指数衰减，属于数学/统计方法，而非心理学理论。
- Confidence: 0.92

## Shedding light on blind spots – Developing a reference architecture to leverage video data for process mining

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113794
- Metrics: 事件提取准确率/召回率/精确率; conformance checking fitness; process discovery quality (fitness, precision); 提取流程相关事件的比例（>70%）
- Objective evidence: 文章的核心贡献是设计并验证ViProMiRA参考架构及其实例化软件原型，使之能够从非结构化视频数据中提取事件日志，从而支持流程挖掘。摘要明确报告原型在监督学习场景中可自动提取超过70%的流程相关事件；第8节通过对比Extracted_Log与True_Log报告准确率69.70%、精确率82.36%、召回率69.70%，并通过一致性检查（fitness 79.81%）和流程发现的质量指标展示了原型的实用性与适用性。这些客观指标直接支撑其解决方案的成功主张。
- Artifact: 软件原型（Python prototype）以及参考架构ViProMiRA的实例化 — 原型包含Data Preprocessor（Video2Frame Converter, Background Subtractor）、Information Extractor（Image Classifier, Activity Recognizer, Object Detector, Object Specifier[Human Pose Estimator, Object Tracker, Face Recognizer, Object (Re)Identifier]）、Event Processor（Event Aggregator, Event Log Exporter, Event Notifier）等明确的软件模块。
- Theory: 
- Theory-to-design: 不存在从心理学理论命题到软件设计选择的推导链。文章没有用任何心理学理论来推导或约束原型或ViProMiRA的具体设计特征（如活动识别器、事件聚合器等组件的设计均基于计算机视觉和流程挖掘的技术考虑）。
- Decision: 基础筛选通过：文章以客观可测量的指标（事件提取准确率/精确率/召回率、conformance fitness、discovery质量）作为最终目标和核心贡献，并通过设计、实现和评估一个明确的软件原型（ViProMiRA实例化）来实现这些指标。理论细筛未通过：全文未发现心理学相关理论对软件制品设计产生实质指导，设计依据全部来自计算机视觉和流程挖掘技术领域。
- Confidence: 0.92

## Tapping into the wealth of employees’ ideas: Design principles for a digital intrapreneurship platform

- Year/journal: 2022 / Information & Management
- DOI: 10.1016/j.im.2020.103287
- Metrics: Number of submitted ideas; User activity (time spent on platform, active users, contributors); Lead time from idea submission to implementation
- Objective evidence: 文章的最终目标是促进员工驱动的创新，即内创业行为，并通过平台上的客观使用数据来验证。例如，与过去4年仅18个建议相比，平台在3个月内就产生了大量想法；表7报告了82%的使用时间增加、93%的用户保持活跃、80%的用户积极贡献等。
- Artifact: 数字内创业平台 (Digital Intrapreneurship Platform, 'Brainstation') — 平台本身及其多个功能模块，如想法工作流、评论与投票功能、奖励系统、想法挑战、用户信息披露设置等。
- Theory: Socio-technical system (STS) theory
- Theory-to-design: STS理论被用作整体分类框架，将挑战和设计原则对应到演员、结构、技术、任务、环境等组件，但并没有从心理学原理推导出具体的设计特征。设计原则（如透明度、社区整合等）主要来源于文献综述和实证反馈，STS理论仅为这些设计提供了抽象的组织视角，缺少从理论命题到具体设计选择的实质性推导。
- Decision: 基础筛选通过：文章明确设计并实现了一个数字内创业平台（软件制品），并通过日志文件等客观指标（如提交想法数量、用户活跃度、使用时间增加）验证平台对员工生成想法的改进效果，符合以客观指标为核心贡献。理论细筛失败：文章虽以STS理论为基础，但该理论不是心理学相关理论，也没有从理论命题实质推导出具体设计特征，主要是将理论作为分类框架，因而未满足心理学理论实质指导设计的要求。
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

## The effect of intention analysis-based fraud detection systems in repeated supply Chain quality inspection: A context of learning and contract

- Year/journal: 2020 / Information & Management
- DOI: 10.1016/j.im.2019.103177
- Metrics: Decision Time; Inspection Cost; Rejection Correctness
- Objective evidence: 决策时间、检验成本和拒绝正确性是文章研究问题和假设的核心因变量，也是摘要、图7和表4回归分析的焦点；文章通过IAFDS与NO-DSS的对照实验和面板回归检验这些指标的改进，发现IAFDS在传统合同下降低决策时间、减缓检验成本上升并提高拒绝正确率。
- Artifact: 决策支持系统（DSS），具体为基于意图分析的欺诈检测系统（IAFDS） — 基于BDI建模的供应商欺诈意图分析模块，以及向买方提供检验建议的DSS呈现界面；实验中通过统一的“DSS”按钮展示分析结果，并与NO-DSS静态建议界面形成对照。
- Theory: Performance Improvement Theory (PIT)
- Theory-to-design: 未形成完整链条。文章用PIT将IAFDS视为“指导”、合同类型视为“动机”，预测买方检验绩效的改善；但IAFDS的BDI推理机制、Jadex实现、建议呈现等设计来自前期研究[10,11]和系统实现，PIT没有推导或约束这些设计选择。因此缺少“心理学理论→心理机制→具体软件设计→客观指标”的可追溯链。
- Decision: 基础筛选通过：文章以决策时间、检验成本和拒绝正确性等客观指标作为研究问题和核心贡献，并用实验室实验和面板回归验证IAFDS在这些指标上的效果；IAFDS是明确设计并实现为DSS的软件制品。理论细筛不通过：PIT虽涉及学习与动机，但文章仅用来假设DSS的绩效作用，并未实质指导IAFDS的设计；其设计来自BDI系统实现，且未对理论指导的设计特征进行直接检验。
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

## A collaborative decision support system for multi-criteria automatic clustering

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113671
- Metrics: CS index; DB index; SH index; Number of clusters (NOC)
- Objective evidence: 论文的核心贡献是提出新的聚合有效性指标和协作式DSS以改进自动聚类质量，实验用CS、DB、SH等指标将协作式进化算法与三个经典算法（DBSCAN、Affinity Propagation、Mean Shift）对比（表14），并展示协作式算法生成的更多非支配解（表13）；这些指标是评价框架成功与否的主要依据。
- Artifact: 决策支持系统（DSS） — 一个六步DSS框架，包括：VI选择、质量阈值设置、单目标优化输入准备、归一化聚合函数形成、DEA输入准备、利用DEA和BWM确定最终划分；其中包含新的MINLP模型、归一化加权聚合函数、协作式进化算法模块。
- Theory: 
- Theory-to-design: 缺乏从心理学理论到心理机制、再到DSS具体设计选择、再到客观指标的完整推导链。文章的设计选择（如选择VIs、设置阈值、运行进化算法、DEA/BWM排序）主要依据优化与决策科学，而非心理学理论。
- Decision: 基础筛选通过：文章以可计算的聚类有效性指标（CS、DB、SH、NOC）的改进为核心贡献，并提出了一个明确的决策支持系统（DSS）框架，该DSS通过协作式进化算法、聚合函数和DEA/BWM等模块实现上述改进。理论细筛不通过：文章没有使用心理学相关理论来指导DSS设计；BWM属于多准则决策方法，不构成心理学理论，且没有形成理论到设计的推导链。
- Confidence: 0.9

## A decision support framework and prototype for aircraft dispatch assessment

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113338
- Metrics: information retrieval time; correct document retrieval count; dispatch decision time; maintenance task time
- Objective evidence: 文章的核心贡献是减少派飞评估中的信息检索和决策时间。4.1节实验显示平均检索时间从203秒降至55秒，约73%的下降，且正确率没有下降；4.2节实际运行演示估计端到端决策时间从约15分钟降至15秒；第5节结论也以这些时间节省作为核心成果
- Artifact: web-based mobile decision support system prototype (DSS prototype) — 原型工具及其核心功能：自动导入缺陷报告、获取飞机数据、解析TSM/MEL/AMM并自动识别维护替代方案、过滤和排序替代方案、显示预期派飞结果、3步式用户界面；实验版本的简化原型使用BM25检索
- Theory: 
- Theory-to-design: 无法追溯“心理学理论→心理机制→具体软件设计选择→客观指标”的链条。原型的三步用户界面来自框架过程模型，BM25检索来自信息检索技术，时间计算来自航班计划和延误标准，保留用户否决权来自航空安全和领域职责考虑；这些设计均不是由心理学理论推导出来的
- Decision: 基础筛选通过：文章以提高信息检索效率和派飞决策效率为核心目标，使用检索时间、正确文档数、决策时间等客观指标验证改进，并通过可运行的web移动原型这一明确软件制品实现该改进。理论细筛不通过：文章没有使用可识别的心理学理论前瞻性地推导原型设计，人为因素和心理术语仅为背景动机或事后解释。
- Confidence: 0.9

## A strategic decision-making architecture toward hybrid teams for dynamic competitive problems

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113490
- Metrics: Reward (f(s)); Total misalignment; Optimal reward for winning players
- Objective evidence: 文章提出的决策架构和任务划分方法以奖励、总失配、最优奖励等客观指标作为效果度量，并通过对比博弈论决策与人类玩家实际决策（图6）、不同任务划分方法（图8）来验证改进。
- Artifact: 人类-计算机协作决策支持架构（decision-making architecture for hybrid teams） — 架构中的计算机代理组件，包括LSTM奖励模型、基于模型预测控制和博弈论的差分博弈求解器、策略聚类模块，以及用于划分子问题的数据驱动方法。
- Theory: 
- Theory-to-design: 未建立。设计主要基于博弈论、模型预测控制、机器学习和系统分块原理，缺乏从心理学理论到具体设计特征的推导。
- Decision: 基础筛选通过：文章提出一个决策支持架构（软件制品），并以游戏奖励、总失配、最优奖励等客观计算指标作为最终目标和核心贡献，设计或改造了明确的模块。理论细筛不通过：文章未使用心理学相关理论实质指导软件制品设计，相关引用仅为背景或未来工作。
- Confidence: 0.9

## Bayesian neural networks for flight trajectory prediction and safety assessment

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113246
- Metrics: RMSE; MAE; 空间距离（预测轨迹与实际轨迹的距离）; 分离距离预测误差（MAE及误差占比）
- Objective evidence: 文章的核心贡献是构建并集成两类贝叶斯深度学习模型以提升轨迹预测精度，并用预测轨迹进行安全评估；Section 5 通过留一交叉验证比较概率DNN、确定性DNN、LSTM、集成模型及线性/SVM/决策树等基线，表中报告RMSE、MAE和空间距离的改善，Table 2报告分离距离预测MAE为3.78英里（误差占比2.7%）。
- Artifact: 飞行轨迹预测与安全评估软件程序/工具（包含基于Apache Spark的FIXM数据解析程序、DNN、LSTM、模型集成模块与分离距离安全指标） — 开发了基于Apache Spark的FIXM海量数据解析程序；构建了深度前馈贝叶斯神经网络DNN进行轨迹偏差一步预测；构建了LSTM进行多步轨迹状态预测；设计了通过偏差项融合DNN与LSTM的集成预测模块；设计了基于水平/垂直分离距离的概率安全评估指标。
- Theory: 
- Theory-to-design: 不存在从心理学理论命题到心理机制、再到具体软件设计选择、最后到客观指标的完整链条。DNN和LSTM的结构选择来自深度学习领域，MC dropout来自贝叶斯近似推断；没有心理学理论用于推导或约束模型设计。
- Decision: 基础筛选通过：文章以轨迹预测误差、空间距离误差和分离距离预测误差等客观指标的下降为核心贡献，并通过开发基于Apache Spark的解析程序、DNN、LSTM、集成模型和安全评估模块实现该目标，且用RMSE/MAE等客观指标完成验证。理论细筛不通过：未发现任何心理学相关理论实质指导软件制品设计；响应时间等人类工效学数据仅用于事后论证预测时间窗的实用性，未形成理论—设计推导链。
- Confidence: 0.9

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

## Conversational Recommender Systems and natural language:

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113250
- Metrics: HitRate@k; HitRate loss relative to upper bound; Accuracy; Mean Average Precision (MAP); Number of Questions (NQ); Interaction Time (IT); Time Per Question (TPQ); Query Density (QD)
- Objective evidence: 文章将推荐准确率和交互成本作为回答RQ1、RQ2、RQ3的核心结果，并通过实验比较三种交互模式以及组件消融来验证改进；主观问卷仅作为辅助，且在统计上没有显著差异。
- Artifact: Conversational Recommender System framework (ConveRSE)，可构建支持自然语言、按钮和混合交互的聊天机器人 — 框架的模块化架构（Dialog Manager、Intent Recognizer、Sentiment Analyzer、Entity Recognizer、Recommendation Services）以及三种交互模式（自然语言、按钮、混合）
- Theory: 
- Theory-to-design: 不存在从心理学理论命题到心理机制、再到ConveRSE具体软件设计选择、最后到客观指标的完整推导链。框架设计主要基于模块化对话系统架构和slot-filling交互模型，而非心理学理论指导。
- Decision: 基础筛选通过：文章以ConveRSE框架这一明确软件制品为核心，通过推荐准确率和交互成本等客观指标作为主要目标与贡献，并在实验中实际验证了组件影响和交互模式差异。理论细筛不通过：文章设计ConveRSE时没有以可识别的心理学理论作为前瞻性设计依据；相关心理机制仅出现在相关工作综述中，未形成理论到制品设计的推导链。
- Confidence: 0.9

## Customer Acquisition via Explainable Deep Reinforcement Learning

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2022.0529
- Metrics: Average Reward (AR@1, AR@3, AR@6); long-term revenue; customer acquisition reward
- Objective evidence: 文章在摘要和引言中明确指出优化长期收益是主要目标，并在第5.2节通过表3展示DRQN-attention在H=3和H=6时平均奖励高于MAB、DQN、DRQN等基准，验证了改进效果。
- Artifact: 客户获取系统（customer acquisition system）中的智能RL代理（RL agent） — DRQN-attention模型，包括RNN处理历史交互、定制注意力机制（query、key、value）以及Q值预测层，用于替代现有基于contextual MAB的决策模块。
- Theory: 
- Theory-to-design: 不存在从心理学理论到设计选择的完整推导链。注意力机制的query/key/value设计源于对客户获取场景下数据特性的技术分析（静态信息、历史交互固定不变，因此将注意力放在当前交互特征上），并非由可识别的心理学理论推导而来。
- Decision: 基础筛选通过：文章以长期收益（平均奖励）为核心目标，该指标由实际广告曝光、点击和客户获取行为及明确的财务数值计算，不依赖主观感知；文章设计并实现了DRQN-attention模型，作为客户获取系统中的智能决策代理，并通过离策略评估验证其收益提升。理论细筛不通过：虽然文章提到注意力机制模仿人类认知注意，但未使用任何可识别的心理学理论实质指导模型设计；注意力机制的定制决策（query/key/value的构建）基于数据特征和技术推理，而非心理学理论推导。
- Confidence: 0.9

## Deep learning for detecting financial statement fraud

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113421
- Metrics: AUC; Sensitivity; Specificity; F1-score; F2-score; Accuracy
- Objective evidence: 文章的核心研究问题RQ1和RQ2是比较不同数据组合与模型在欺诈检测上的预测性能，最终目标和核心贡献是提升欺诈检测的客观分类性能。Table 2在测试集上比较了FIN、LING、FIN+LING、TXT、FIN+TXT等设置，结果显示HAN在FIN+TXT上取得最高AUC 92.64%和最高敏感性90%，结论部分也以此作为模型有效性的核心证据。
- Artifact: 金融报表欺诈检测决策支持系统/模型（HAN-based fraud detection model / decision support application） — 基于层次注意力网络（HAN）的文本分类器，包括词级双向LSTM编码器与注意力层、句级双向LSTM编码器与注意力层、将文档表示与47个财务比率拼接后的稠密分类层，以及利用句子注意力权重生成“red-flag”句子高亮标注的审计决策支持功能。
- Theory: 欺骗检测/语言线索理论（Zhou et al. [75]；DePaulo et al. [16] 等社会心理学与欺骗线索研究）
- Theory-to-design: 论文没有形成完整的“心理学理论→心理机制→具体软件设计→客观指标”链条。文中引用社会心理学研究只是为了论证MD&A文本可能揭示管理者认知过程，从而为文本分析提供动机；选择HAN时主要依据的是NLP领域的分层文档结构和注意力机制（Yang et al. [72]），并未说明欺骗理论如何决定词级/句级注意力、双向LSTM、财务特征拼接等具体设计选择。Zhou et al.关于“欺骗线索依赖于上下文”的观点主要出现在结果和解释部分，用以解释HAN为何有效，而不是在设计确定之前用于推导设计。
- Decision: 基础筛选通过：文章以AUC、敏感性、F2等客观分类指标作为最终目标，并通过测试集比较验证了所提出的HAN模型在欺诈检测上的改进；文章明确提出构建欺诈检测系统，HAN属于该系统核心模块。理论细筛不通过：尽管引用了欺骗检测/社会心理学研究作为文本分析动机，但没有可追溯证据表明某一心理学理论在HAN设计确定之前实质指导了具体设计选择；HAN来自NLP分层注意力架构，理论更多是事后解释。
- Confidence: 0.9

## Different but Equal? A Field Experiment on the Impact of Recommendation Systems on Mobile and Personal Computer Channels in Retail

- Year/journal: 2020 / Information Systems Research
- DOI: 10.1287/isre.2020.0922
- Metrics: RecViews; RecSales; RecSalesQ; Clickthrough; Conversion; sales diversity / view diversity (Gini coefficient)
- Objective evidence: 文章的研究问题和贡献声明集中在推荐系统在移动端与 PC 端对顾客决策结果和销售多样性的影响；随机现场实验以推荐系统为处理，差分模型估计其因果效应。Tables 3–4 显示推荐系统显著提高推荐商品浏览量（PC 与移动端均正显著），并显著提高移动端的推荐商品销售额、销量、点击率和转化率；Section 4.3 和 Figures 1–2 进一步检验销售/浏览多样性。因此客观指标改进是文章的核心经验贡献，而非仅背景或附属结果。
- Artifact: 在线零售网站（PC 与移动端）中的个性化推荐面板/推荐系统 — 落地页上的推荐面板：在治疗组展示最近浏览商品以及基于 item-to-item 协同过滤生成的推荐商品列表；对照组在同一位置展示畅销商品列表。
- Theory: 信息加工理论/有限认知与满意化（Simon 1955）; 搜索成本与认知负担; 记忆提取与回忆线索（Bettman 1979; Lynch and Srull 1982）; 信号效应
- Theory-to-design: 不存在完整链条。文章虽然用心理学理论解释推荐系统为何有效，但没有从理论推导出推荐面板的任何具体设计选择；推荐面板采用标准的 item-to-item 协同过滤和“最近浏览商品+推荐列表”形式，没有说明理论约束了何种界面特征、信息呈现或交互机制。文中明确表示不预先提出正式假设，让经验分析提供指导，并在结果后用理论进行事后推测。因此理论没有前瞻性指导软件制品设计。
- Decision: 基础筛选通过：文章在真实零售网站 PC 与移动端实际部署并随机开关推荐面板，以点击流和交易日志中的浏览量、销售额、销量、点击率、转化率及 Gini 系数等客观指标作为核心结果，验证了推荐系统带来的提升和渠道差异。理论细筛不通过：心理学相关理论仅用于解释动机和事后推测机制，没有前瞻性指导推荐面板的具体设计选择，也未被用于设计某一可检验的软件功能变体；缺少理论—设计—客观指标的完整链条。
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

## Facial expression-enhanced recommendation for virtual fitting rooms

- Year/journal: 2024 / Decision Support Systems
- DOI: 10.1016/j.dss.2023.114082
- Metrics: Precision; MAP (Mean Average Precision)
- Objective evidence: 文章的核心贡献是提出 FEERS 方法，以提升虚拟试衣间中的个性化推荐准确率为最终目标。实验部分以 Precision 和 MAP 作为主要评价指标，并对比多个基线方法，结果显示 FEERS 在两项指标上均取得最高值，且通过 Mann-Whitney U 检验证明显著优于其他方法。
- Artifact: 虚拟试衣间（VFR）中的推荐系统，具体为 FEERS（Facial Expression-Enhanced Recommendation System） — 推荐系统的核心算法模块：基于矩阵分解的推荐模型，包括置信度设置策略（结合面部表情、交互行为数、停留时间）和负反馈采样策略（基于标题相似度）。
- Theory: 
- Theory-to-design: 设计链条缺失。文章在确定置信度时，简单地将“happy”编码为积极、中性为中性、其他为消极，这是一种常识性操作，没有基于特定心理学理论推导出这一设计选择。例如，没有说明为什么正性情绪导致 $c_{ui}=1$ 而不是其他权重，没有理论解释交互行为数量与喜好程度之间的心理机制。因此，理论到设计之间的推导链不成立。
- Decision: 基础筛选通过：文章以推荐准确率（Precision、MAP）这一客观指标为最终目标和核心贡献，且通过实验验证了 FEERS 这一软件制品（推荐系统）的提升效果。理论细筛未通过：文章未使用任何可识别的心理学相关理论实质指导推荐算法的设计；对于如何将面部表情映射为偏好，仅有常识性编码，缺乏理论推导链。
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

## Filaments of crime: Informing policing via thresholded ridge estimation

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113518
- Metrics: crime incident coverage percentage within distance envelopes around ridges; coverage efficiency
- Objective evidence: 文章的核心贡献是提出DREDGE软件以生成巡逻路线，其最终目标是提高巡逻效率，而覆盖率正是衡量该目标的主要指标。文章在结果部分报告了2019年事件在脊线0.1英里内覆盖94%，在0.6英里内覆盖99%，并与随机巡逻和热点中心比较，显示脊线具有更高的覆盖率，从而验证了改进。
- Artifact: 软件工具DREDGE（Density Ridge Estimation Describing Geospatial Evidence），一个纯Python实现，可通过PyPI安装。 — DREDGE工具本身，包括对SCMS算法的扩展：SCMS算法、阈值化（thresholding）、带宽优化、haversine距离计算、收敛检查、百分比截断功能。
- Theory: deterrence theory (威慑理论); routine activities theory (日常活动理论)
- Theory-to-design: 文章中不存在从心理学理论到设计特征的推导链。例如，没有说明'因为威慑理论，所以设计脊线来覆盖更多区域'。设计选择主要基于密度估计的统计方法，而非心理机制。文章提到'patrol presence'和'deterrent effects'只是结果解释，而非设计依据。
- Decision: 基础筛选通过：文章以犯罪事件覆盖率这一客观指标为核心，通过开发软件工具DREDGE实现，并进行了实证评估。理论细筛不通过：文章没有使用心理学相关理论实质指导软件制品设计，相关理论仅作为背景，未形成设计推导链。
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

## OrdinoR: A framework for discovering, evaluating, and analyzing organizational models using event logs

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113771
- Metrics: fitness; precision; F1-score
- Objective evidence: 文章的核心贡献是提出组织模型的一致性检查（conformance checking），fitness 和 precision 是这一贡献的核心度量。第 6 节用这些指标评估了 24 个发现模型，并通过表 8-11 比较不同配置，展示某些方法（如 OverallScore vs FullRecall、trace clustering vs case attribute）能获得更优的 conformance，从而使该客观指标成为评价和验证改进的主要依据。
- Artifact: 开源软件原型：OrgMiner Python 库和配套可视化工具 — OrgMiner 库中实现执行模式学习、资源分组发现、执行模式分配和一致性检查/可视化的各模块，以及作为框架产出的组织模型（OM）表示。
- Theory: 
- Theory-to-design: 未形成‘心理学相关理论→心理/行为机制→具体软件制品设计选择→预期客观指标’的链条。文章的设计推导来自过程挖掘中的事件日志、执行模式、资源特征矩阵、聚类/社区发现等概念，而不是心理学理论。
- Decision: 基础筛选通过：文章以 fitness、precision、F1-score 等可计算的客观指标作为核心贡献和评价依据，并在真实事件日志上验证；所设计的 OrgMiner 软件库/工具明确实现和检验了组织模型发现与一致性检查。理论细筛不通过：全文未使用任何心理学或行为科学理论实质指导软件制品设计，仅有的组织/流程再造文献只是背景动机引用，未形成理论到设计选择的可追溯链条。
- Confidence: 0.9

## Predicting Instructor Performance in Online Education: An Interpretable Hierarchical Transformer with Contextual Attention

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2021.0310
- Metrics: MSE; MAE
- Objective evidence: 文章核心贡献是提出预测模型并显著降低预测误差；通过与14种非深度学习基线和LectureBERT对比，均显著优于（p<0.001），并通过消融实验证明各组件贡献
- Artifact: 在线教育教师表现预测工具/决策支持系统 — 整个可解释层次Transformer模型，包括局部BERT编码器、全局Transformer层、上下文注意力机制及其预测输出模块
- Theory: 首因效应/第一印象; 近因效应; 信息相关性对记忆和注意的影响
- Theory-to-design: 未形成完整链条。模型设计（局部-全局Transformer、上下文注意力）没有从心理学理论推导而来；心理学概念仅用于在获得结果后解释不同学科、难度等情境下注意力权重的差异，或解释句子相关性、情态词与评分之间的相关性，属于事后解释。
- Decision: 基础筛选通过：文章以MSE和MAE等客观预测误差指标为核心贡献，设计并实现了明确的预测工具（层次Transformer模型）并进行对比与消融验证。理论细筛失败：心理学概念仅用于事后解释可解释性分析结果，未在设计阶段实质指导模型组件选择或形式。
- Confidence: 0.9

## Predicting shareholder litigation on insider trading from financial text: An interpretable deep learning approach

- Year/journal: 2020 / Information & Management
- DOI: 10.1016/j.im.2020.103387
- Metrics: AUC; Decile ranking
- Objective evidence: 文章的核心贡献是提出一个可解释的深度学习预测框架，其主要目标是提高内幕交易诉讼的预测性能。第6.2节报告最佳模型（Model O）的AUC达81.22%，显著高于最佳基线模型（78.95%，DeLong检验p=0.024），且第一十分位捕获45.63%正例，优于基线。这些客观指标直接用于验证模型改进，是文章的主要评价依据。
- Artifact: 文本分析/预测模型框架，具体为基于注意力机制的深度学习模型，用于监管决策支持。 — 模型架构：词嵌入层、层次注意力网络（词注意力和段落注意力）、基于业务邻近网络的节点嵌入模块、基于MD&A时间变化的GRU时序模块、数值与文本特征融合层。
- Theory: 信息操纵理论（Information Manipulation Theory）; 行为心理学关于不诚实行为的研究; 有限注意理论（Limited Attention）; 犯罪威慑理论（Becker's economic theory of crime）
- Theory-to-design: 文章虽然引用了信息操纵理论等来论证文本披露包含与内幕交易相关的线索，从而支持使用文本输入；但这些理论主要被用于论证预测的可行性（第3.1和3.2节）以及事后解释注意力结果（第6.4节），并未具体推导或约束模型中的某个设计特征。注意力机制的引入明确是受人类视觉注意力系统的启发（5.2节）和监管可解释性需求（第1节），而不是由心理学理论命题推导出的设计选择；业务邻近网络和时间变化模块也源于经济学和管理学中的竞争环境与‘lazy prices’现象（第3.2节），而非心理学理论。因此没有形成‘理论→心理机制→具体设计选择→客观指标’的完整可追溯链条。
- Decision: 基础筛选通过：文章以AUC和十分位排名等客观指标作为最终目标和核心贡献，验证了所设计的深度学习预测模型（软件制品）的改进；模型由明确的模块组成并接受这些指标评价。理论细筛不通过：文章引用了信息操纵理论、行为心理学等，但主要作为预测可行性的论证和结果的事后解释，没有证据表明这些理论前瞻性推导了模型架构中的具体设计特征，因此不满足要求C。
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

## The Effects of Featuring Product Sampling Reviews on E-Tailer Websites

- Year/journal: 2024 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00834
- Metrics: 产品销售额（daily sales）; 有机评论数量（daily organic review volume）; 净销售效应（net sales effect）
- Objective evidence: 文章的核心研究问题是展示产品试用评论对销售额和有机评论量的净影响，贡献陈述强调通过真实销售数据追踪净销售效应（见摘要、引言和结论）。H1a通过DID验证展示评论显著提升销售额（treatment×time系数正显著，Table 5）；H2a验证有机评论量减少（系数负显著）；H3a通过中介分析证明净效应为正（总效应0.193，95% CI不含零）。
- Artifact: 电商网站（e-tailer website）的产品页面及其评论展示区域 — 在既有产品页面的有机评论列表顶部，新增展示一条带有明确赞助披露标示的‘产品试用评论’（sponsored product sampling review），并伴随产品采样活动页面（申请采样、展示活动信息）
- Theory: 信号理论 (Signaling theory); 公平理论 (Equity theory); 市场交换规范 (Market exchange norms, Heyman & Ariely, 2004) 等作为背景理论
- Theory-to-design: 文章并未建立从心理学理论到软件制品设计选择的完整前瞻性推导链。设计内容（在产品页面展示一条赞助产品试用评论并披露）是平台已实施的经营措施，不是由理论推导出来的设计选择。信号理论和公平理论被用于预测这一既定展示方式的效果（H1a/H1b/H2a/H2b），即解释消费者如何回应这一设计，而非解释为什么应该采用这一设计而不是其他设计。文章没有说明理论如何约束信息呈现方式、评论挑选规则、披露图标等具体设计参数；也没有在实验条件中操作任何由理论生成的设计变体。因此不满足要求C。
- Decision: 基础筛选通过：文章以实际销售额和有机评论量这两个客观可测量指标为核心目标，通过DID和中介分析验证电商网站产品页面新增展示赞助产品试用评论的效果；该改动是明确的软件制品（电商网站产品页面评论展示区）的设计/改造。理论细筛不通过：信号理论和公平理论虽然属于心理学相关理论，但它们仅被用来预测既定展示方式的效果，并未在软件制品设计决定之前指导设计选择、约束设计特征或生成设计变体；理论与实践无设计推导链条。
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

## The crowd against the few: Measuring the impact of expert recommendations

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113345
- Metrics: Clips Watched（观看片段数）; Rec. Clicks（推荐点击次数）; Total Visits（总访问次数）; Active Visits（有效访问次数）; Multiclip Visits（多片段访问次数）; Return Rate（回访率）; Retain Rate（留存率）; Algorithm Success（算法成功度）; Taste Coverage（品味覆盖率）; Unique Recommendation Clicks (URC); Diversity (ILS, 列表多样性)
- Objective evidence: 摘要、引言和结论均把‘专家推荐对用户行为的影响’作为核心贡献；第4.1节表4显示治疗组在观看片段数、推荐点击、总访问、有效访问、多片段访问、回访率和留存率上均显著或边缘显著更高；第4.2节评估了不同推荐算法的相对成功度；第5节进一步检验了推荐属性和满意度。
- Artifact: 在线视频点播网站上的真实推荐系统（real-world recommender system on a video-on-demand website） — 在既有商用推荐系统中加入专家推荐列表，并将专家推荐与系统生成推荐混合；包括落地页和个人片段页两处推荐列表的生成与混合逻辑。
- Theory: 
- Theory-to-design: 未形成完整的理论→心理机制→设计选择→客观指标链条。加入专家推荐的主要依据来自先前离线研究中专家推荐在准确性、多样性和冷启动方面的优势，以及算法互补考量；随机混合专家推荐并约一半展示是为了避免展示位置偏差，这属于普遍行为经验或界面设计考虑，不是从明确心理学理论推导出的设计规则。文章在结果解释时才借用多样性、满意度等文献进行事后归因。
- Decision: 基础筛选通过：文章核心贡献是采用真实视频点播平台上的推荐系统，通过加入专家推荐使平台使用等客观行为指标显著提升；软件制品明确为在线推荐系统及其推荐混合模块，改造部分清晰。理论细筛不通过：虽然提到过滤气泡、多样性、满意度等概念，但未形成可识别的心理学理论对软件设计的前瞻性指导，理论—设计—客观指标链条不完整。
- Confidence: 0.9

## X-IM Framework to Overcome  Semantic Heterogeneity Across XBRL Filings

- Year/journal: 2020 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00626
- Metrics: Precision; Recall; F-measure
- Objective evidence: 文章的核心研究问题是设计一个全自动算法准确地将 XBRL 标签映射到上层本体中的金融概念；评价部分以 precision、recall 和 F-measure 作为主要成功标准，并通过与 FinCEM 的对比实验和 Wilcoxon 检验证明 X-IM 的提升。摘要明确说 'standard information retrieval metrics' 和 'significantly outperforms existing methods'；第 6 节表 6-8 给出具体改进结果。
- Artifact: X-IM 框架，一个用于 XBRL 财务报告语义互操作/本体映射的软件系统 — 整个 X-IM 框架，包括 EDGAR web crawler、IOnto generator 和 IBC learner；具体设计内容涉及从 XBRL label linkbases 提取标签特征、构建索引本体、设计基于索引的分类器以及 designative information 过滤机制。
- Theory: Representation Theory / Theory of Ontological Clarity (Wand & Weber)
- Theory-to-design: 文章建立的理论链是：representation theory 中的本体清晰性缺陷（construct deficit 和 construct redundancy）→ XBRL/UGT 存在语义异构问题 → 设计 X-IM 时使用 investor's ontology 缓解 construct deficit、使用 label terms 缓解 construct redundancy → 提高 precision/recall/F-measure。这一链条中没有解释人的心理或行为机制如何决定某个设计选择；理论指导的是语法本体层面的设计，而非人的认知/行为机制层面的设计。
- Decision: 基础筛选通过：文章以 precision、recall、F-measure 等客观信息检索指标作为最终目标和核心贡献，并构建了明确的软件制品 X-IM 框架（EDGAR crawler、IOnto generator、IBC learner）来实现 XBRL 元素映射。理论细筛不通过：文章使用的 representation theory/ontological clarity 是信息系统本体理论，其核心解释对象不是人的心理或行为机制，未满足心理学相关理论实质指导软件制品设计的要求。
- Confidence: 0.9

## <scp>Context‐aware</scp> user profiles to improve media synchronicity for individuals with severe motor disabilities

- Year/journal: 2022 / Information Systems Journal
- DOI: 10.1111/isj.12337
- Metrics: Task completion time; Selection errors; Overscan errors
- Objective evidence: 文章的核心贡献是提出将情境感知用户画像纳入AAC系统以改善沟通过程，并将“提高传输速率”作为首要设计需求。在自然主义评价中，文章以任务完成时间为主要依据，报告加入情境感知用户画像后各任务平均完成时间改善约19.88%至60.33%，并总结“情境感知用户画像能够实现更快的消息传输”（表8、6.1.1节）。这些客观指标直接服务于文章的核心改进主张。
- Artifact: AAC系统原型（augmentative and alternative communication system prototype） — AAC系统原型中加入了情境感知用户画像组件，并配套开发了医疗与舒适需求本体、扫描式选择界面，以根据用户、时间、地点和沟通对象动态调整可选择的词/短语/符号集。
- Theory: Media synchronicity theory (MST), Dennis et al., 2008
- Theory-to-design: 文章没有建立“MST命题→心理/行为机制→具体软件设计选择→待改善的客观指标”的先行推导链。情境感知用户画像这一具体制品设计主要源于推荐系统中的用户画像、灵活对话系统、情境感知BCI轮椅等思路（4.3节），并非由MST推导而来。MST在背景部分被映射到AAC情境，并在第6节用于“论证”和“解释”设计原则，是在制品创建和评价之后的事后理论透镜，而非在确定设计特征之前用于选择或约束设计。因此不满足理论实质指导软件制品设计的要求。
- Decision: 基础筛选通过：文章以改善严重运动障碍者沟通任务完成时间和减少错误为核心目标，使用客观的任务完成时间与错误计数验证了所设计的AAC系统原型；该原型是明确的情境感知用户画像软件组件。理论细筛不通过：媒体同步理论主要是在设计和评价完成后用于解释和论证设计原则，未前瞻性地推导或约束情境感知用户画像的具体软件设计选择，因而不满足心理学相关理论实质指导制品设计的要求。
- Confidence: 0.88

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

## Bidder Support in Multi-item Multi-unit Continuous Combinatorial Auctions: A Unifying Theoretical Framework

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2021.1068
- Metrics: 增量更新子拍卖状态的平均运行时间; 查询 winning level 和 deadness level 的运行时间; 计算全部 bidder support 信息的总运行时间
- Objective evidence: 文章将“设计高效的计算基础设施来提供bidder support信息”列为主要贡献，并以计算效率作为验证所设计实现的核心客观指标；摘要明确指出该实现“outperform the commonly used integer programming approach”，Section 5中的Tables 3–6进一步用仿真和基准测试证明其在增量更新和查询上的时间优势。
- Artifact: 面向连续多物品多单位（MIMU）组合拍卖的竞标者支持系统/计算基础设施（bidder support system / computational infrastructure） — 用于实时提供bidder support的核心软件模块：span vector到整数的映射方法，VAL和LastWinBid数据结构，增量更新子拍卖状态的算法（Algorithm 1），检索赢标分配的算法（Algorithm 2），以及winning/deadness level的查询逻辑。
- Theory: 
- Theory-to-design: 不成立。所设计软件制品的选择来自组合拍卖的数学性质（如子拍卖、可行配置、竞标语言、赢标确定的计算结构），而不是从心理学理论命题推导出设计特征；不存在“心理学理论→心理机制→具体软件设计选择→预期客观指标改善”的完整链条。
- Decision: 基础筛选：通过。文章以计算效率（运行时间）这一客观指标作为所设计方案的改进目标，并通过设计实时竞标者支持系统/计算基础设施（数据结构与算法）来实现，仿真及与整数规划方法的基准测试验证了改进。理论细筛：未通过。文章没有使用可识别的心理学相关理论来前瞻性指导软件制品设计；设计依据是拍卖与算法理论，而非人的心理或行为机制。
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

## HyperCARS: Using Hyperbolic Embeddings for Generating Hierarchical Contextual Situations in Context-Aware Recommender Systems

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2022.0202
- Metrics: RMSE; MAE; Hit@K; MRR@K; Silhouette; Dunn Index; DT Accuracy; IDS Accuracy; IDS AUC; Coverage; Rule Complexity
- Objective evidence: 文章的核心贡献是提出HyperCARS方法以更好地建模层次上下文情境并提升上下文感知推荐性能；第6.2节通过RMSE/MAE/Hit@K/MRR@K与多个baseline比较并报告统计显著提升，第6.1节用聚类质量指标验证层次表示优势，第6.3节用解释准确率/覆盖率验证可解释性优势。
- Artifact: 上下文感知推荐系统（CARS）中的上下文建模与推荐方法/模块，具体为HyperCARS模型，包含双曲空间变分自编码器、层次聚类模块和基于NeuMF扩展的推荐模型。 — 设计并实现了完整的HyperCARS流水线：双曲空间VAE上下文嵌入生成模块；AHC/HDBSCAN层次聚类模块；将层次上下文情境路径hcs作为输入的NeuMF扩展推荐模型，并包含Selected-Levels和Complete-Tree两种版本。
- Theory: 
- Theory-to-design: 不存在心理学理论命题到设计特征的推导链；双曲嵌入、层次聚类和NeuMF扩展的设计选择均由几何性质、嵌入表示能力和推荐性能目标驱动，而非由心理机制驱动。
- Decision: 基础筛选通过：文章以提升上下文感知推荐性能为核心目标，并通过设计/构建HyperCARS推荐系统方法（双曲嵌入+层次聚类+NeuMF推荐模块）实现该目标；评价使用RMSE、MAE、Hit@K、MRR@K等客观指标。理论细筛不通过：文章未使用心理学相关理论指导软件设计，设计推导主要基于双曲几何和机器学习方法。
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

## Multi-Party Certification on Blockchain and Its Impact in the Market for Lemons

- Year/journal: 2022 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2022.2063555
- Metrics: Dealer's initial asking price; Sale price; Dealer's relative revenue; Buyer's relative revenue; Proportion of lemons sold; Proportion of peaches sold
- Objective evidence: 文章的核心研究问题是如何影响柠檬市场，最终贡献是实证证明多主体认证降低了信息不对称、提高了市场效率和公平性。通过对比Instance A（无多主体认证）和Instance B（有多主体认证）的实验结果，使用t检验验证了H1-H3：初始要价降低（p=0.00174）、销售价格降低（p=0.00256）、经销商相对收益降低（p=0.00000）、买方相对收益提高（p=0.00213）、优质车比例上升（p=0.0011）、柠檬比例下降（p=0.0071）。
- Artifact: 在线汽车市场平台（CarMarket）以及区块链信息系统的实例（CarCerti） — 设计并实现了CarMarket，一个基于Web的实验性汽车市场；在Instance B中，集成了CarCerti，一个模拟区块链的多方认证信息系统，提供可信汽车历史证书，包含维修服务历史和驾驶员动态等额外信息类别。
- Theory: Anchoring effect; Signaling theory; Information asymmetry theory; Socio-technical artifact framework
- Theory-to-design: 缺乏从心理学理论到软件制品设计选择的推导链。文章将锚定效应用于解释为什么初始要价影响最终销售价格，并据此提出H1和H2，但CarCerti的信息呈现方式、交互机制等设计特征并未由锚定效应推导；信号理论用于说明信息越全面则信号契合度越高，但并未明确设计出具体的信息类别或界面元素。设计CarCerti时主要基于与Cardossier产业项目的协作以及对真实二手车生态系统的理解，而非心理学理论驱动的设计决策。
- Decision: 基础筛选通过：文章以客观市场指标（价格、收益、商品分配比例）的改善为最终目标和核心贡献，并通过设计实现CarMarket和CarCerti两个软件制品（及其实验对比）来验证。理论细筛失败：虽然使用了锚定效应等心理学相关概念，但它们主要用于预测实验条件下市场参与者的行为结果，并非在设计阶段指导软件制品（如CarCerti的信息内容、界面或交互）的选择；理论到设计、再到客观指标评价的链条不成立。
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

## Toward Sustainable Electricity Markets: Capacity-Based Pricing for Electric Vehicle Smart Charging

- Year/journal: 2026 / Information Systems Research
- DOI: 10.1287/isre.2023.0078
- Metrics: RMSE (Root Mean Square Error); PAPR (Peak-to-Average Power Ratio); Peak load (MWh); Revenue deviation from target (%)
- Objective evidence: 文章将电网平衡和收益保持作为其设计的最终目标，RMSE、PAPR、峰值和收益偏差是评价定价方案成功与否的主要指标。通过与传统平定价、可变定价和递增阶梯定价基准比较，CBP-CH配置在平坦负荷等场景中将RMSE从0.88降至0.02 MWh，PAPR从2.89降至1.07，同时收益偏差仅为0.08%。
- Artifact: IS-enabled pricing artifact for electric vehicle smart charging（容量定价机制及其价格设定启发式） — 容量定价方案 P_t(r)=P_{0,t}+α_t·r，以及解析启发式(AH)和计算启发式(CH)等价格设定方法。
- Theory: 
- Theory-to-design: 未形成“心理学理论→心理/行为机制→具体软件制品设计选择→客观指标”的完整推导链。价格设定通过数学定理和基于数据的学习启发式推导，而不是由任何心理学理论指导。
- Decision: 基础筛选通过：文章以不依赖主观判断的客观指标（RMSE、PAPR、峰值、收益偏差）作为最终目标和核心贡献，并通过设计容量定价这一明确的IS制品（价格公式与价格设定启发式）来实现该改进。理论细筛不通过：文章完全基于理性成本最小化假设和经济学/优化理论，没有使用任何心理学相关理论指导软件制品设计。
- Confidence: 0.88

## Unveiling the Hidden Truth of Drug Addiction: A Social Media Approach Using Similarity Network-Based Deep Learning

- Year/journal: 2021 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2021.1870388
- Metrics: Precision; Recall; F1 score
- Objective evidence: 文章的核心贡献是设计SINDEL系统以自动识别OUD治疗障碍，并以F1/precision/recall作为系统成功与否的主要验证指标；SINDEL在OUD数据集上达到76.97% F1，显著超过SVM、LR、NB、CRF、RNN、LSTM、BLSTM等基线和多种消融模型，在WebMD第二个案例中也一致优于基线模型。
- Artifact: SImilarity Network-based DEep Learning（SINDEL），一个用于社交媒体的深度文本挖掘/信息系统IT工件。 — 设计了相似性网络表示、多视图BLSTM架构、双分支融合层、Softmax序列标注模块，以及后续的K-means治疗障碍聚类模块。
- Theory: 
- Theory-to-design: 不存在可追溯的“心理学理论→心理/行为机制→具体软件设计选择→预期客观指标改善”链条。相似性网络表示是为了处理morphs之间词语相似性而设计，多视图BLSTM是为了提升序列标注性能而设计，均不是由心理学理论命题推导出的设计选择。
- Decision: 基础筛选通过：文章设计并评价了一个明确的IT制品SINDEL，以Precision、Recall和F1 score等客观文本抽取性能为核心贡献指标，并在多个数据集和基线/消融比较中验证改进。理论细筛不通过：SINDEL的设计没有受到心理学相关理论的前瞻性指导，其设计依据主要是词嵌入、相似性网络和深度学习架构等计算/语言学方法，未形成心理学理论到系统设计的推导链。
- Confidence: 0.88

## Data analytics for the sustainable use of resources in hospitals: Predicting the length of stay for patients with chronic diseases

- Year/journal: 2022 / Information & Management
- DOI: 10.1016/j.im.2020.103282
- Metrics: R²; MAE; MSE; RMSE; MAPE; ±2天容差准确率; ±3天容差准确率
- Objective evidence: 文章的核心目标是准确预测LOS，从而改善医院资源利用和可持续运营。摘要和引言均将精确预测LOS作为主要贡献；第5节通过Table 6报告COPD和肺炎测试集上的R²、MAE等指标，并在Table 7与既有数值预测研究比较，证明模型精度显著提升。
- Artifact: 基于深度MLP网络的住院时长预测组件/临床决策支持系统（CDSS）预测模块 — 设计并实现了一个全连接多层感知机（MLP）深度神经网络，含输入层（59个数值预测变量）、5个隐藏层（第一层128个神经元，其余每层256个神经元）和单神经元输出层；同时构建了从历史住院记录中生成新变量的数据工程流程。
- Theory: 
- Theory-to-design: 不存在可追溯的心理学理论到设计选择的推导链。文中没有用任何理论命题解释为什么某个软件设计能够改善LOS预测指标；对历史住院变量的引入来自“既往住院信息有助于预测”的领域经验，而非心理学理论推导。
- Decision: 基础筛选通过：文章以LOS预测准确率（R²、MAE、±2/±3天准确率等）为最终目标和核心贡献，这些指标来自实际住院天数并可客观计算；同时文章设计并实现了深度MLP预测网络，并将其定位为临床决策支持系统中的预测组件。理论细筛不通过：全文没有使用心理学相关理论指导软件制品设计，设计依据主要是数据工程和深度学习技术考量。
- Confidence: 0.87

## Matching Mobile Applications for Cross-Promotion

- Year/journal: 2020 / Information Systems Research
- DOI: 10.1287/isre.2020.0921
- Metrics: downloads (dn_ijt); download ratio (dn_ratio_ijt); post-download session time (sess_ijt); post-download connection count (conn_ijt); app ranking; AUROC, AUPRC, F1, R2, MAE in prediction evaluation; daily total downloads, session times, and connections in matching simulation
- Objective evidence: 文章的核心目标是通过理解 CP 匹配并设计匹配平台来提升广告效果；计量分析检验相似度对下载和使用的影响，DID 分析显示 CP 提升目标 app 排名和表现，Section 7 的模拟比较不同特征组和匹配算法，显示下载、会话和连接指标显著改善
- Artifact: 移动应用交叉推广的集中式 app 匹配平台（信息/匹配系统） — 平台整体架构，包括后端数据收集与主题建模子系统、前端实时匹配引擎，以及机器学习预测模型和广义延迟接受匹配算法等模块
- Theory: variety-seeking behavior; consistency-seeking behavior / customer loyalty
- Theory-to-design: 文章在 Section 2.3 综述了 variety-seeking 和 consistency-seeking 理论，并在 Section 4.3 将源-目标 app 相似度作为实证变量分析用户行为；但这些理论主要被用于解释已得到的计量结果，并未在 Section 7 的匹配平台设计之前推导具体设计选择。匹配平台的核心设计来自机器学习预测模型和 Gale-Shapley/Roth 的稳定匹配算法，而非心理学理论；文中没有说明心理学理论如何约束平台架构、特征集、优化目标或匹配算法选择。因此，理论—心理机制—具体软件设计—客观指标的完整前瞻性链条不成立。
- Decision: 基础筛选通过：文章的目标是提高 CP 广告效果，核心指标为下载量、下载率、下载后会话时长和连接次数等系统日志客观指标，并通过设计一个 app 匹配平台（包括预测模型和匹配算法）及模拟评估来实现和验证。理论细筛不通过：虽然文章引用了多样性寻求和一致性寻求等心理学理论，但这些理论主要用于解释实证结果，并未前瞻性地推导或约束匹配平台的具体软件设计；设计链来自机器学习与市场设计，而非心理学理论。
- Confidence: 0.87

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

## TheoryOn: A Design Framework and System for Unlocking Behavioral Knowledge Through Ontology Learning

- Year/journal: 2020 / MIS Quarterly
- DOI: 10.25300/misq/2020/15323
- Metrics: Precision; Recall; F1-measure; False positives; False negatives; Number of correctly retrieved constructs/articles/theories
- Objective evidence: 文章的核心目标是缓解行为研究文献的知识不可访问性问题，而解决方案的成功与否主要用抽取性能和信息检索性能来验证。摘要明确指出：“数据挖掘实验结果验证了BOLT设计原则；随机实验比较了TheoryOn与EBSCOhost、Google Scholar在四项信息检索任务上的表现，说明TheoryOn能减少假阳性和假阴性。”讨论部分进一步引用用户实验中TheoryOn的F1比基线高37%至121%。
- Artifact: 基于本体的学术搜索引擎（ontology-based search engine） — TheoryOn系统整体，包括假设抽取、变量抽取、理论关系抽取、理论网络构建、构念搜索、构念对搜索、前因/后果构念搜索、理论整合与可视化等功能模块。
- Theory: 确认偏误（confirmation bias）; 行为知识本体论（Weber 2012; Larsen et al. 2019）
- Theory-to-design: 文章没有建立“心理学理论→心理机制→具体软件设计选择→客观指标”的完整推导链。确认偏误只出现在问题动机和背景中，用于解释现有全文搜索引擎为何会导致假阴性，并未被用来推导TheoryOn的具体设计特征（如构念搜索、关系抽取、可视化方式等）。BOLT的设计推导主要基于行为知识本体论和ontology learning文献，而不是心理学理论对用户认知机制的指导。
- Decision: 基础筛选通过：文章以TheoryOn这一搜索引擎为明确软件制品，并以假设/变量/关系抽取的Precision/Recall/F1以及用户在四项信息检索任务中的客观检索性能为核心评价指标，验证其降低假阳性和假阴性、改善信息检索的效果。理论细筛不通过：虽然动机部分提到确认偏误等心理学概念，但没有用心理学相关理论前瞻性地推导具体软件设计选择；其设计框架的kernel theories主要是行为知识本体论，而非关于用户心理或行为机制的理论。
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

## A deep recurrent neural network approach to learn sequence similarities for user-identification

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113718
- Metrics: user re-identification accuracy (success rate); adjusted rand index (ARI); perfect clustering share; recall and precision for estimating number of users; computation time per triplet decision
- Objective evidence: 文章的核心贡献是提出 TL-RNN 序列相似性框架，并将其应用于用户再识别。在三个任务（双选再识别、多用户分配、用户数量估计）中，TL-RNN 的准确率、ARI、precision/recall 都优于 Smith-Waterman 和 TF-RW 基准，表 1-3 给出了具体数值，表明这些客观指标是衡量设计成功的主要依据。
- Artifact: 深度学习模型软件工具（TL-RNN 序列相似性框架，附开源参考实现） — LSTM 嵌入层、事件嵌入层、三元组损失函数、网络训练与推理流程、加入协变量（IVT）的模型扩展
- Theory: 
- Theory-to-design: 不存在可追溯的心理学理论到设计选择的链。没有理论命题用于推导 LSTM 层、三元组损失或嵌入层的设计；这些设计由机器学习经验和技术需求驱动。
- Decision: 基础筛选通过：文章以客观指标（用户再识别准确率、ARI、precision/recall、计算时间）为核心贡献，并通过构建和评估 TL-RNN 这一软件工具（开源深度学习模型）来实现这些指标提升。理论细筛失败：文章没有任何心理学相关理论指导软件制品设计，缺少理论→心理机制→设计选择的推导链。
- Confidence: 0.85

## An explanatory machine learning framework for studying pandemics: The case of COVID-19 emergency department readmissions

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113730
- Metrics: AUC; Accuracy; Sensitivity; Specificity; F1; G-mean
- Objective evidence: 文章的核心贡献是提出一个预测/解释性机器学习框架，并以预测性能作为主要评价证据；结果部分报告最佳DNN模型的AUC=0.883、准确率87.4%、F1=70.4%、G-mean=81.2%，并在Table 7中与既往ED再入院预测研究对比，说明其敏感度和AUC显著更高。
- Artifact: 临床决策支持系统（clinical decision support system, DSS/decision support tool） — 一个混合机器学习框架，包括遗传算法特征选择模块、深度前馈MLP预测模块和SHAP模型解释模块；这些模块共同构成面向COVID-19急诊再入院的临床决策支持工具。
- Theory: 
- Theory-to-design: 不存在从心理学理论到心理机制、再到具体软件设计特征和客观指标的推导链。特征选择、网络结构、正则化、超参数优化和SHAP解释均由预测准确率和模型可解释性目标驱动，而非由心理学理论指导。
- Decision: 基础筛选通过：文章以COVID-19急诊7日再入院预测性能（AUC、准确率等客观指标）作为核心贡献，并构建了称为临床决策支持系统的预测—解释性机器学习框架，满足客观指标和软件制品两项要求。理论细筛不通过：文章设计中未使用心理学相关理论，也没有理论到设计特征的推导链，因此不属于理论指导的软件制品设计。
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

## Creating Proactive Cyber Threat Intelligence with Hacker Exploit Labels: A Deep Transfer Learning Approach

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2023/17316
- Metrics: Accuracy; Precision; Recall; F1-score
- Objective evidence: 文章的核心目标和贡献是提出DTL-EL框架，用于自动标记黑客论坛中的漏洞利用代码。通过四个实验，将DTL-EL与多种基线方法比较，在准确性、精确率、召回率和F1分数上均显著提升（如目标域F1-score为70.34%，优于最佳非迁移模型的62.52%）。这些指标是验证模型设计成功与否的主要依据。
- Artifact: 深度迁移学习漏洞利用标签器（DTL-EL）框架，一个信息技术制品（软件制品） — DTL-EL模型整体，包括预初始化的BiLSTM、自注意力机制、多层迁移学习设计，以及将其集成到用户界面系统中的实现（附录D）。
- Theory: 
- Theory-to-design: 不存在理论到设计的推导链。设计决策主要基于深度学习技术（如BiLSTM、注意力机制、迁移学习）的技术优势和设计科学原则，而非心理学理论。预初始化的理由是基于专业人员的操作过程，但未形成理论命题并据此约束具体设计。
- Decision: 基础筛选通过：文章以提升准确性、精确率、召回率和F1-score等客观分类指标作为最终目标和核心贡献，并通过设计和评估DTL-EL这一软件制品来实现该提升；理论细筛不通过：文章没有使用心理学相关理论实质性地指导软件制品设计，预初始化设计模拟分析师工作流程只是一般性类比，未形成理论到设计的推导链。
- Confidence: 0.85

## Fall Detection with Wearable Sensors: A Hierarchical Attention-based Convolutional Neural Network Approach

- Year/journal: 2021 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2021.1990617
- Metrics: F-measure; Precision; Recall
- Objective evidence: 文章的核心贡献是提出HACNN以改进可穿戴传感器跌倒检测的效果；在评估和实验结果部分，F-measure是判断模型是否优于基线的主要指标，HACNN在两个数据集上均显著优于经典机器学习模型和替代深度模型，并通过消融分析检验超参数与设计选择。
- Artifact: 可穿戴传感器跌倒检测的深度学习模型/分析引擎（HACNN），作为跌倒检测信息系统的IT制品 — HACNN模型的三个组成部分：CNN特征提取器、层级注意力机制（轴级注意力和传感器级注意力）、输出层；并包含网络结构细节和模型规格。
- Theory: 
- Theory-to-design: 未形成“心理学理论→心理机制→具体制品设计→客观指标”的推导链。文章没有从任何心理学理论推导出HACNN中的注意力层、CNN结构或输出设计；attention机制作为可解释性手段被引入，但其依据是深度学习的可解释性需求，而非心理学理论。
- Decision: 基础筛选通过：文章以HACNN的跌倒检测效果为核心目标，并以F-measure、Precision、Recall等由真值标签计算得到的客观指标验证其改进；该模型被明确作为IT制品/可穿戴跌倒检测系统的分析引擎进行设计和评估。理论细筛不通过：文章没有使用可识别的心理学相关理论实质指导软件制品设计；attention机制和visual cortex仅作为深度学习的直觉类比或背景说明，未形成从心理学理论到设计选择的推导链。
- Confidence: 0.85

## ForeSim-BI: A predictive analytics decision support tool for capacity planning

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113266
- Metrics: total workload forecast error (E=F-D); percentage error (PE/E/D); mean absolute error (MAE); mean absolute percentage error (MAPE); workload errors by work type, work phase, and work skill
- Objective evidence: 文章的核心贡献是提出一个能更准确预测未来维修工作负荷和辅助容量规划的决策支持工具。摘要明确指出工具‘provides more accurate workload forecasts than current employed approaches’，并通过对比真实观测和当前工程估算来验证。第3.5节显示ForeSim-BI对总工作量的预测误差从第一次观测的13%降至后续0%，总误差MAE总体低于工程估算，并据此推算成本节约潜力。
- Artifact: 预测分析决策支持工具（decision support tool）ForeSim-BI，用于复杂产品系统维护能力规划。 — 完整工具及四个集成模块：预测模块（AHW指数平滑）、贝叶斯推断模块、仿真模块（蒙特卡洛与自助抽样）和贝叶斯网络模块；并包含一个用于工作量区间选择的线性规划（LP）模型。
- Theory: 
- Theory-to-design: 无法建立‘心理学理论→心理/行为机制→软件设计选择→客观指标改善’的链条。ForeSim-BI的模块选择主要基于统计拟合准则（AICc）、专家输入、历史数据特性和数值实验结果（如r_cut选择），而非心理学理论推导。
- Decision: 基础筛选通过：文章以预测准确率/预测误差等客观指标为核心贡献，并通过设计、开发和验证ForeSim-BI这一明确的决策支持软件工具及其模块实现。理论细筛不通过：虽然文章涉及贝叶斯等正式方法，但没有使用心理学相关理论实质指导软件制品设计；提及判断式预测偏差仅属背景动机，不构成设计推导链。
- Confidence: 0.85

## Fraudulent review detection model focusing on emotional expressions and explicit aspects: investigating the potential of feature engineering

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113728
- Metrics: Precision; Recall; F1-score; AUC
- Objective evidence: 文章的核心贡献是提出特征工程和M-SMOTE方法提升欺诈性评论检测性能，多个实验中以Precision、Recall、F1和AUC为主要成功度量，并与基线及已有方法对比验证改进。
- Artifact: 欺诈性评论检测模型（机器学习分类系统） — 特征提取与特征工程流程、数据预处理步骤、M-SMOTE算法、基于多数投票的集成分类器
- Theory: 
- Theory-to-design: 没有形成从心理学理论到心理机制、具体软件设计选择以及客观指标的完整推导链，特征选取主要基于已有文献的经验规律和统计分布。
- Decision: 基础筛选通过：文章构建了欺诈性评论检测模型（软件制品），并以Precision、Recall、F1、AUC等客观指标作为最终目标和核心贡献，进行了系统的实验验证。理论细筛未通过：文章未使用心理学相关理论来前瞻性地指导软件设计，特征选择和行为假设均来自数据分析和既有文献，而非心理理论，且缺乏从理论到设计再到指标的可追溯链条。
- Confidence: 0.85

## From Smartphones to Smart Students: Learning vs. Distraction Using Smartphones in the Classroom

- Year/journal: 2026 / Information Systems Research
- DOI: 10.1287/isre.2022.0078
- Metrics: performance gain（后测成绩 − 前测成绩）; posttest score（课后测试成绩）
- Objective evidence: performance gain是全文分析的核心结局变量。表3与表7显示，相对禁用手机基线，允许随意使用手机会降低performance gain，而教师引导使用手机辅助教学会显著提高performance gain；表5和表9的IV分析进一步表明，手机学习时间占比增加会提高成绩提升，手机分心时间占比增加会降低成绩提升。这些结果构成文章的主要发现和贡献。
- Artifact: 自定义智能手机词典应用（web-based dictionary app），即用于课堂辅助教学的软件工具 — 为实验开发的自定义词典应用，学生可扫描课桌二维码访问，用于查询生词的发音、释义和词源；配套有教师提示使用该应用辅助教学的流程，以及内容相同的纸质词典对照组。
- Theory: 
- Theory-to-design: 不存在可追溯的理论到设计的完整链条。文章没有说明某一心理学理论命题推导出app的特定设计特征（例如二维码入口、词典内容呈现、教师提示方式）；app的设计更像实用教学工具，而非由心理学理论约束或推导出的设计选择。
- Decision: 基础筛选通过：文章以客观的performance gain（前后测成绩差）作为核心结局指标，并明确设计/开发了自定义词典app这一软件制品，且用该客观指标比较不同使用条件以评价其效果。理论细筛不通过：虽有注意力、认知负荷等心理学文献，但没有证据表明这些理论实质指导了词典app的设计；理论仅用于背景和事后解释。
- Confidence: 0.85

## Greening the Cloud: A Load Balancing Mechanism to Optimize Cloud Computing Networks

- Year/journal: 2022 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2022.2063551
- Metrics: 总等待时间 (total waiting time); 作业分配均衡度 (job allocation balance); 价格 (price per job); 队列长度 (queue length)
- Objective evidence: 文章的核心贡献是设计一个负载均衡机制，其目标是最大化资源使用效率、最小化等待时间，从而绿色化云。Proposition 1 证明等量分配可使总等待时间最小化（与不等分配相比），这是改进的核心；仿真进一步展示了机制行为，验证了价格和等待时间的客观变化。
- Artifact: 私有云计算服务的资源分配与负载均衡机制 (a pricing and allocation mechanism for a private cloud computing service) — 基于动态定价模型设计的作业分配算法 (job allocation algorithm) 和定价机制
- Theory: 
- Theory-to-design: 不存在理论到设计的心理机制推导链；设计依据是经济最优定价和排队论优化，而非心理学理论。
- Decision: 基础筛选通过：文章以客观指标（总等待时间、资源分配均衡度、价格）的优化为目标和核心贡献，并通过设计私有云负载均衡算法这一软件机制来实现，仿真和数学证明对改进进行了验证。理论细筛不通过：全文未使用心理学相关理论指导设计，其设计基础是经济学定价和排队论，而非心理学机制。
- Confidence: 0.85

## Handling the Efficiency–Personalization Trade-Off in Service Robotics: A Machine-Learning Approach

- Year/journal: 2021 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2021.1870391
- Metrics: Mean Absolute Error of energy efficiency prediction; Mean Absolute Error of preference estimation
- Objective evidence: 文章的核心贡献是提出并评价处理效率-个性化权衡的机器学习方法，该方法由能量效率预测和偏好估计两个关键模型组成；评价部分使用平均绝对误差作为主要指标，并与随机猜测、线性回归、随机森林、前馈神经网络等多个基线比较，结果显示LSTM的预测误差显著更低（效率预测约为基线的3.5倍精度，偏好估计约为6倍精度）
- Artifact: 一个基于division-of-labor框架的机器学习应用程序（DoL application），属于自动驾驶汽车（AV）的驾驶策略决策软件模块 — 包括中央执行器（CE）和专家（expert）两类计算组件，内含三个ML模型：LSTM能量效率预测模型、LSTM用户偏好估计模型，以及基于梯度的权衡优化模块
- Theory: 
- Theory-to-design: 不存在完整的心理学理论→心理机制→软件制品设计选择→预期指标的推导链。文章主要在背景中引用接受度研究说明个性化重要性，在讨论中引用自动化水平模型解释中间自动化等级设计的合理性，但未在设计确定前用理论推导具体设计特征，也没有说明为什么理论导致该设计而非其他设计
- Decision: 基础筛选通过：文章以能量效率预测误差和偏好估计误差作为主要客观评价指标，并据此验证了所设计的ML应用（DoL系统）的有效性，该应用明确是AV驾驶策略决策的软件制品。理论细筛不通过：文章没有在软件制品设计之前使用明确的心理学理论来推导设计选择，心理学相关概念仅作为背景或事后解释，缺乏理论到设计到指标的完整链条。
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

## Incorporating FAT and privacy aware AI modeling approaches into business decision making frameworks

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113715
- Metrics: RMSE (Root Mean Square Error); Coverage; Model stability; Replicability; Number of variables in GLM
- Objective evidence: 文章的核心贡献是提出并评估一个FAT-based机器学习方法，并以RMSE与Cinematch基准比较作为主要成功指标：NoNulls模型改善8-14%（Table 3）；覆盖率在81-88%之间（Table 7）；不同分区下预测准确率稳定在7.5-8.5%左右，作为公平性证据。这些客观指标是最终目标和核心贡献的依据。
- Artifact: FAT-based AI/ML prediction framework (机器学习预测模型，用于商业决策支持系统) — 提出并实例化了一个FAT框架，包括数据分区、相似度度量（MCS）、GLM预测模型、预测变量计算算法等组件。
- Theory: 
- Theory-to-design: 不存在。设计选择如选择GLM作为透明模型、改进余弦相似度MCS、数据分区等均基于准确性、可解释性、稳定性等工程和统计考量，而非心理学理论推导。文中仅有一次提及'bounded rationality'，但未作为设计依据。
- Decision: 基础筛选通过：文章以RMSE、覆盖率、模型变量数等客观指标作为核心评价，并通过构建一个FAT-based GLM预测模型（软件制品）实现这些指标提升。理论细筛不通过：文章未使用心理学相关理论指导设计，FAT框架属于伦理/治理原则而非心理学理论；设计选择基于工程和统计考量。
- Confidence: 0.85

## Real-Time Sales Data, Streamer Improvisation, and Sales Performance: Evidence From Live Stream Selling

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2025/18627
- Metrics: Log(sales); Sales; product sales quantity
- Objective evidence: 销售业绩是研究问题RQ1的核心结果，也是文章的主要贡献和成功标准。随机实地实验显示处理组预售产品销量比对照组增加约40.21%（β=0.338, p<0.05），并通过中介和异质性分析加强因果证据。
- Artifact: 直播平台的主播端仪表盘（streamer-facing sales dashboard） — 在主播端仪表盘中为预售产品增加实时销售数据列（total amount of deposit 和 total remaining balance），仅对处理组主播开放。
- Theory: Improvisation Theory; Dual-process theory (System 1/System 2)
- Theory-to-design: 文章从即兴理论推导出实时销售数据可能通过主播的即兴行为影响销售，但并未从理论推导出仪表盘的具体设计特征（如显示哪些实时数据、采用何种格式、更新频率等）。实验中的制品功能（在仪表盘中增加预售产品实时销售数据列）是平台既定的业务扩展，而非由理论选择的设计方案。因此缺乏“理论→明确设计选择”的可追溯链条。
- Decision: 基础筛选通过：文章以预售产品销售量（客观交易指标）作为核心结果，通过随机实地实验证实提供实时销售数据的主播端仪表盘功能（软件制品改造）显著提高销售约40.21%。理论细筛不通过：即兴理论用于解释实时数据促进销售的机制，但未在仪表盘设计确定之前用于推导或选择其具体设计特征；实验中的功能扩展是平台既定的业务决策，因此不满足心理学理论实质指导软件制品设计的要求。
- Confidence: 0.85

## Responsible cognitive digital clones as decision-makers: a design science research study

- Year/journal: 2023 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2022.2073278
- Metrics: F1-score; accuracy; sensitivity; precision; time per candidate review; human hours saved per year
- Objective evidence: 文章在设计原则部分明确将F1-score作为决策准确性的度量，将节省时间和并行参与过程数作为效率度量，并在表6、表7、表8中用这些指标验证Pi-Mind agent带来的改进（F1从0.49升至0.96，危机情景F1=0.95，年节省1591人工小时），因此该指标是核心评价依据。
- Artifact: Pi-Mind agent：一个IT制品/软件智能体，包含克隆训练模块、个人价值系统（PSV）、本体知识库、生成对抗网络（T|C-SGAN）训练架构，并部署于TRUST Portal等信息系统中。 — Pi-Mind agent的核心设计包括：克隆训练机制（T|C-SGAN架构）、PSV驱动的决策模块、以及嵌入TRUST Portal的自动化排名/投票流程。
- Theory: 
- Theory-to-design: 无法形成完整链条：文章没有从心理学理论命题推导出具体软件设计特征。例如，没有说明启发式与偏见理论如何决定T|C-SGAN架构或PSV的特定设计选择，也没有解释为何该理论导致该设计而非其他方案。
- Decision: 基础筛选通过：文章以客观指标（F1-score、时间节省等）为核心成功标准，并实际用这些指标验证了Pi-Mind agent这一明确软件制品带来的改进。理论细筛未通过：文章虽引用启发式与偏见等心理学文献，但未形成从理论到软件设计选择的实质性推导链，理论未前瞻性指导制品设计。
- Confidence: 0.85

## Simpler is better: Lifting interpretability-performance trade-off via automated feature engineering

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113556
- Metrics: AUC (Area Under the ROC Curve); 模型参数数量，或可解释性=参数数量的倒数
- Objective evidence: 作者的核心贡献是提出SAFE ML框架以“提升可解释性-性能权衡”：在credit-g用例中，SAFE精炼逻辑回归AUC从普通逻辑回归的0.78提升到0.82，参数数量从49降到25（Fig.4）；在30个数据集的基准中，SAFE模型的可解释性显著高于复杂监督模型，而AUC没有显著下降（Table 4、Table 5、Fig.5-6）。因此，AUC和参数数量作为客观结果指标是验证框架成功的主要依据。
- Artifact: 自动化特征工程与可解释建模框架/工具库（SAFE ML framework，实现为R包rSAFE和Python库SafeTransformer） — SAFE特征提取方法：基于监督黑箱模型的PDP/ALE曲线，用PELT changepoint对连续变量进行可解释分箱；用层次聚类合并分类变量水平；并将变换后的特征用于训练逻辑回归等玻璃箱模型的完整自动流程。
- Theory: 
- Theory-to-design: 不存在完整的理论→心理机制→设计→客观指标链条。第1节和第2.1节提到“简单模型更容易被人类理解”以及GDPR、伦理指南，但这是常识性和规范性论述，不是从心理学理论推导出的设计约束；第3节的SAFE设计依据是PDP、ALE、PELT、层次聚类、AUC和模型复杂度等统计/机器学习概念，而非心理学理论。因此，心理学相关理论与具体软件制品设计之间没有可追溯的推导关系。
- Decision: 基础筛选通过：文章以AUC和模型参数数量（可解释性的客观代用指标）为核心结果目标，并通过SAFE ML这一明确实现为rSAFE/SafeTransformer的软件框架和工具来达成，基准与用例都对这些客观指标进行了实际验证。理论细筛不通过：文章虽然以信任、透明和可解释性为动机，但没有使用可识别的心理学相关理论，也没有从心理学理论推导出具体软件设计特征，因此不满足理论实质指导软件制品设计的要求。
- Confidence: 0.85

## Sustaining a Good Impression: Mechanisms for Selling Partitioned Impressions at Ad Exchanges

- Year/journal: 2020 / Information Systems Research
- DOI: 10.1287/isre.2019.0878
- Metrics: expected revenue; revenue gain relative to BASE mechanism
- Objective evidence: 文章的核心贡献是设计最优机制以最大化广告交易平台收入：摘要明确“our goal ... to address this efficiency loss by offering mechanisms”；Section 1.2列出主要贡献为提出OPT-IR和OPT-MB机制；Section 10数值实验（Table 13）显示相对BASE机制，OPT-IR收入增益7.01%（同质广告）和18.22%（异质广告），OPT-MB增益23.02%和33.60%，验证了改进。
- Artifact: 移动广告交易平台（mobile ad exchange）中的实时竞价拍卖机制 — 拍卖机制本身，即分配规则（将展示分割为时隙并顺序分配多个广告）和支付规则（含随机化支付、CPC/CPM实现方式）；具体设计了OPT-IR和OPT-MB两种机制，以及作为对照的SEQ机制。
- Theory: 
- Theory-to-design: 
- Decision: 基础筛选通过：文章以广告交易平台预期收入最大化为最终目标和核心贡献，收入指标客观可计算，并通过数值实验验证了相对传统机制的改进；通过设计拍卖机制（分配规则和支付规则）这一明确软件制品的组成部分来实现，满足软件制品设计要求。理论细筛不通过：文章仅使用经济学机制设计理论，无任何心理学相关理论指导机制设计，因此不属于理论引导子集。
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

## A cross-domain recommender system through information transfer for medical diagnosis

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113489
- Metrics: Prediction accuracy (AR_t = 1 - d(R_|Y|, R̂_|Y|)); recommendation accuracy for disease risks
- Objective evidence: 文章的最终目标和核心贡献是提高跨域推荐系统对疾病风险等级的预测准确率，以支持医生诊断。摘要明确称ITMD优于四个基线并提高疾病风险推荐准确率；第5.2节将预测准确率定义为评价指标；第5.3节表6、图2和图3显示ITMD在相同/不同症状空间均优于基线，最大提升分别为0.0973和0.0827；第6节真实病例研究表10和表11显示ITMD优于基线，最大提升0.1221、最高提升率16.69%。
- Artifact: 跨领域推荐系统（cross-domain recommender system），针对医学诊断的疾病风险推荐系统 ITMD — 整个ITMD推荐系统被设计和构建，包含：区间数患者-症状矩阵归一化、症状空间对齐（转换矩阵M1和M2）、新的区间数风险类别相异度度量、基于集体矩阵分解和条件数约束的信息迁移模块，以及目标域推荐生成模块。
- Theory: 
- Theory-to-design: 不存在心理学理论→心理/行为机制→软件制品设计→客观指标的完整推导链。ITMD的各设计选择由数据稀疏、特征空间不匹配、区间数不确定表示等数学/工程问题驱动，而不是由心理学理论推导而来。
- Decision: 基础筛选通过：文章以预测准确率这一客观指标为最终目标和核心贡献，并通过设计、实现和评估一个明确的软件制品——跨领域医学诊断推荐系统ITMD来实现该指标。理论细筛不通过：全文未见心理学相关理论实质指导ITMD的推荐系统设计；设计主要由转移学习、矩阵分解和区间数方法驱动。
- Confidence: 0.84

## Assessing and Enhancing Adversarial Robustness of Predictive Analytics: An Empirically Tested Design Framework

- Year/journal: 2022 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2022.2063549
- Metrics: Accuracy; Precision; Recall; F-measure; ROC AUC; Performance ratio robustness measures (R_A, R_P, R_R, R_F, R_ROC); Area under performance-perturbation curve robustness measures (A/P AUC, P/P AUC, R/P AUC, F/P AUC, ROC/P AUC)
- Objective evidence: 文章的核心贡献是提出并实例化一个评估和增强预测分析对抗鲁棒性的设计框架，客观鲁棒性指标是判断ARText系统成功与否的主要依据。Evaluation 1验证了评估测度的有效性；Evaluation 2通过性能比和性能-扰动曲线指标对比ARText与基线模型，并比较对抗重训练前后提升，结果表明ARText在各类鲁棒性指标上均优于基线，因此客观指标构成最终目标和核心贡献。
- Artifact: ARText系统，一个针对文本分类任务的对抗鲁棒文本分类系统 — ARText系统的整体设计，包括对抗样本生成模块、对抗鲁棒性评估模块（性能比和性能-扰动曲线测度）、基于bootstrap aggregation的集成学习分类模块，以及迭代对抗重训练模块。
- Theory: Technology Threat Avoidance Theory (TTAT); Coping theory; Cybernetics theory
- Theory-to-design: 文章声称TTAT的威胁评估与威胁应对分别对应所提出框架的对抗鲁棒性评估元需求和对抗鲁棒性增强元需求，但这一链条止于元需求层面。ARText中的具体设计——如DeepWordBug生成对抗样本、性能比和性能-扰动曲线测度、bagging集成、迭代对抗重训练——主要由对抗机器学习文献、统计学习理论和数学目标函数推导而来，文章并未说明为什么TTAT会导出这些具体设计，而非其他可选设计。
- Decision: 基础筛选通过：文章以对抗鲁棒性的客观分类指标提升为核心目标和贡献，并设计、实现了ARText文本分类系统，明确通过对抗样本生成、鲁棒性评估、集成学习和对抗重训练等软件系统组件实现该提升。理论细筛不通过：文章虽使用TTAT作为kernel theory，但TTAT仅被用来映射到评估与增强两类高层元需求，并未实质推导ARText的具体软件设计特征；具体设计来自对抗机器学习的实证和技术逻辑，且没有对TTAT指导的设计选择进行对比或消融检验，因此不满足心理学理论实质指导软件制品设计的要求。
- Confidence: 0.84

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

## A simulation-based risk interdependency network model for project risk assessment

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113602
- Metrics: simulated occurrence probability (SOP); simulated local influence (SLI); simulated global influence (SGI); total risk loss (TRL); total risk propagation loss (TRPL)
- Objective evidence: 文章的核心贡献是提出MCS-based RIN模型及新的风险指标，并通过两个案例验证该模型在风险评估和风险处理中的有效性。第4.3节和表4、表5显示，基于所提模型制定的Action 4获得最高的reduced TRL/TRPL，并在第二案例中将项目失败风险SOP降至0，优于经典P-I模型、FSE和FBBN等基准方法，因此客观指标是核心贡献的验证依据。
- Artifact: 决策支持系统（decision-support system）中的仿真模型/软件实现（MCS-based RIN model，并在MATLAB中实现） — ISM-based风险依赖网络构建模块、MCS风险发生随机模拟算法（含COP动态阈值和风险环假设-检验）、五项风险指标计算模块、敏感性分析模块，以及风险处理行动的规划与评估模块
- Theory: 
- Theory-to-design: 不存在从心理学理论命题到心理机制、具体设计选择、再到客观指标的完整推导链。ISM用于建立风险层次结构，MCS用于随机仿真，其设计依据是工程/概率逻辑而非心理机制。
- Decision: 基础筛选通过：文章以风险模拟指标（SOP、SLI、SGI、TRL、TRPL）及风险处理后的TRL/TRPL降低作为核心贡献，并通过两个案例计算验证；该改进通过明确设计并实现的决策支持/仿真软件模型（MCS-based RIN model）实现。理论细筛不通过：文章的设计指导来自ISM、MCS和概率/网络建模方法，不是心理学相关理论，缺少理论-心理机制-设计-客观指标的推导链。
- Confidence: 0.82

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

## Assuring quality and waiting time in real-time spatial crowdsourcing

- Year/journal: 2023 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113869
- Metrics: average waiting time (α); average reputation of selected workers (β); average cost (γ); assignment rate (δ); average travel distance (ε)
- Objective evidence: 摘要、引言、贡献陈述和结论均将“最小化任务请求者等待时间”和“最大化结果质量（以所选工人平均信誉表示）”作为 TP-TASC 的核心目标。第5.4节通过与 RB-TPSC 对比，在不同任务半径、任务有效时间、工人有效时间和工人平均信誉设置下展示 TP-TASC 在平均等待时间和平均信誉等指标上的改进，并据此得出结论：TP-TASC 能降低请求者等待时间并提高任务质量。
- Artifact: 空间众包平台中的自动任务分配和决策支持系统/模块（TP-TASC） — 基于 LightGBM 的工人旅行时间预测模块，以及按工人信誉分层、以最小化等待时间为目标的启发式任务分配算法（Algorithm 1）。
- Theory: 
- Theory-to-design: 不存在“心理学理论→心理/行为机制→具体软件设计选择→预期客观指标改善”的完整链条。旅行时间预测和任务分配算法主要由时间约束、信誉等级、预算约束和优化目标决定，而非由任何心理学理论推导而来。
- Decision: 基础筛选通过：文章以最小化请求者等待时间和最大化结果质量（用所选工人平均信誉衡量）为核心目标，通过在空间众包平台任务分配中设计 LightGBM 旅行时间预测模块和信誉分层的启发式分配算法实现，并在真实数据集仿真中使用客观指标验证改进。理论细筛不通过：全文没有使用心理学理论实质指导软件制品设计，等待时间与满意度的关系只是一般性背景说明，不构成理论到设计的推导链。
- Confidence: 0.82

## Augmented Reality at Work: Attention Management and Its Impact on Work Performance

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2025/18944
- Metrics: visual performance (number of key components inspected); action performance (number of standard actions performed)
- Objective evidence: 文章的研究问题和核心贡献是AR如何影响工作绩效，而非仅背景变量或附属结果；工作绩效是主要因变量，并在图9、图10、表4、表5和PROCESS检验中用于验证AR的效应以及信息依赖度、信息复杂度的调节作用。虽然全样本直接效应不显著，但模型显示了显著的中介效应和高依赖/低复杂度条件下的绩效改进，且这些客观指标是文章的主要实证证据。
- Artifact: 用于飞机过站检查的AR智能眼镜工作卡软件及配套手机应用（AR job card / mobile application） — 飞机检查步骤的实时指导信息显示功能：将步骤标题和操作指导分别显示在AR眼镜或手机屏幕上；针对9个指定步骤设计了高/低信息依赖度和高/低信息复杂度的指导信息，并包含步骤推进和确认交互。
- Theory: divided attention theory (Kahneman, 1973); dual-task interference (Pashler, 1994); peripheral attention research (e.g., Chaturvedi et al., 2019)
- Theory-to-design: 文章基于分心理论和双任务干扰提出了AR相对手机会减少注意切换、提高专注度、进而提升绩效的假设，并提出信息复杂度和信息依赖度作为调节。但这些理论主要用于预测给定AR/手机信息通道的效果和解释结果，而不是在设计确定之前推导或约束某个具体的软件制品设计特征。AR眼镜的周边视野显示是设备既有属性，不是由理论选择的设计方案；实验中对标题与指导信息间隔2秒的设计来自预测试和可读性考虑，未表明由理论推导；信息依赖度和复杂度的操作化主要依据概念定义和工程经验，也非理论驱动的设计决策。因此缺少“心理学理论命题→具体软件设计选择→客观指标”的完整设计指导链。
- Decision: 基础筛选通过：文章以工作绩效（视觉绩效和动作绩效）为最终目标和核心贡献，这些指标来自视频行为记录和目标检测，不依赖主观感知；文章设计并使用了将检查指导集成到AR眼镜和手机中的软件工作卡，并通过现场实验比较不同显示通道对绩效的影响，因此满足A和B。理论细筛不通过：分心理论和双任务干扰被用来提出和解释研究假设，但未在软件制品设计确定之前实质指导某一具体设计特征；AR周边视野显示是设备属性，2秒延迟设计来自预测试，信息类型操作化也未形成理论驱动的设计链，因此不满足要求C。
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

## Decisions for information or information for decisions? Optimizing information gathering in decision-intensive processes

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113632
- Metrics: Expected profit; Average retrieval cost; Expected revenue
- Objective evidence: 文章的核心贡献是优化DIP中的信息收集决策，使最终决策期望收益减去信息成本最大化；第7.4节表5显示MDP的期望利润为15,867.6，而人工决策树为8,226.0，MDP近似使期望利润翻倍，并以此作为主要改进证据。
- Artifact: 运行期推荐工具/决策支持系统（CMMN引擎 + MDP推荐器） — 将CMMN用户模型与过程控制计划片段集成为可部署的CMMN模型，使用MDP推荐器提供状态相关的行动建议；还包括用Python实现的MDP求解器和在线演示器。
- Theory: 
- Theory-to-design: 不存在可追溯的‘心理学理论→心理机制→具体制品设计选择→客观指标’链条。设计决策由MDP优化目标、任务成本和过程约束驱动；允许决策者忽略建议仅作为灵活性需求提出，并非由心理学理论推导出的设计特征。
- Decision: 基础筛选通过：文章以实现净期望收益最大化这一客观指标为核心贡献，并通过构建CMMN/MDP推荐工具和部署化过程控制片段来实现该改进。理论细筛未通过：文章没有使用可识别的心理学相关理论来指导软件制品设计，MDP和优化建模属于数学/运筹学方法而非心理学理论。
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

## Improving healthcare access management by predicting patient no-show behaviour

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113398
- Metrics: AUROC; coverage; risk
- Objective evidence: 论文的核心贡献是构建一个用于预测患者爽约概率并支持分组的DSS，结果部分以AUROC作为四个模型比较的主要指标，并以coverage和risk量化采用DSS后潜在干预的覆盖效果与漏诊风险，因此这些客观指标是验证所设计系统成功与否的主要依据。
- Artifact: Decision Support System (DSS) for no-show risk classification — DSS的核心组成部分：基于LASSO逻辑回归、随机森林和神经网络的爽约概率预测模型，以及将患者分为低、中、高三个风险组的分类规则；同时包含作为可解释性组件的Layer-wise Relevance Propagation（LRP）热图可视化。
- Theory: 
- Theory-to-design: 不存在可追溯的‘理论→心理/行为机制→软件设计→客观指标’链条。DSS的预测模型选择、输入变量和分组规则主要由机器学习性能、数据可得性和项目管理需求决定；行为干预措施（短信提醒、教育、参与干预）是系统外的应用策略，并非由心理学理论推导出的DSS设计特征。
- Decision: 基础筛选通过：文章核心贡献是开发一个用于预测患者爽约概率的DSS，并以AUROC、coverage、risk等客观指标验证该系统的预测和分组效果；软件制品上，这些预测模型被明确作为DSS的决策支持模块进行设计和评估。理论细筛不通过：文章未使用任何可识别的心理学相关理论来前瞻性指导DSS设计，行为干预和心理模型只作为背景或未来工作提及，不构成设计推导依据。
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

## Motion Sensor–Based Fall Prevention for Senior Care: A Hidden Markov Model with Generative Adversarial Network Approach

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2023.1203
- Metrics: Accuracy; F1-score; AUC; successful fall prevention rate with lead time >= 320 ms
- Objective evidence: 论文的摘要、引言和贡献陈述均以提升跌倒预防的预测与触发性能为核心目标；实验1检验 HMM-GAN 的状态识别能力，实验2检验 HMM-GAN+LR 在足够提前量下触发保护装置的成功率，均以 Accuracy/F1/AUC 等指标作为主要证据，并声称显著优于现有基线模型，案例研究进一步展示了超过3300万美元的经济收益。
- Artifact: 可穿戴式运动传感器跌倒预防框架/系统（HMM-GAN + Logistic Regression 触发决策模块的 IT artifact） — HMM-GAN 的片段状态识别组件（用 entropic GAN 替换 HMM 中 GMM），以及基于 Logistic Regression 的保护装置触发决策组件
- Theory: 
- Theory-to-design: 不存在从心理学理论命题到心理机制、再到具体软件制品设计选择的推导链；模型设计由运动传感器数据的时序性、状态迁移、数据分布和提前量要求等技术因素驱动，而非由心理学理论指导。
- Decision: 基础筛选通过：文章以准确率、F1、AUC 以及具有足够提前量的跌倒预防成功率等客观指标为最终目标和核心贡献，并在 TST/SisFall 基准数据集上进行了系统验证；文章采用 computational design science 范式，将 HMM-GAN 和 Logistic Regression 作为跌倒预防框架中的软件/IT 制品组件进行设计与评价。理论细筛不通过：文章没有使用任何心理学相关理论来推导或约束软件制品设计，其设计依据来自 HMM、GAN、EM 等计算与统计方法，而非人的心理或行为机制。
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

## Sensing the Future: A Design Framework for Context-Aware Predictive Systems

- Year/journal: 2023 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00821
- Metrics: Cost of forecasting errors (COST_FE); forecasting error improvement percentage
- Objective evidence: 文章在案例应用中明确将“成本预测误差最小化”作为设计目标，并通过对比基线Croston方法报告：Croston with phase-out component较基线改善4%，activity sensor较基线改善20%、较phase-out方案改善17%。这些量化结果是CAPS框架适用性和有效性的主要评价依据。
- Artifact: Context-aware predictive system / sensor-based demand forecasting information system — 包括：1) Croston基线预测模型的实施；2) 在预测模型中增加phase-out成分，形成Croston with phase-out component；3) 基于活动传感器数据的备件需求预测方法；此外还设计了连续多传感器监控系统和远程发动机监控接口两项高级系统设计。
- Theory: 
- Theory-to-design: 不存在理论到心理机制、软件设计和客观指标的完整推导链。文章没有从任何心理学理论命题推导出具体的界面、交互、反馈或系统规则设计；设计选择建立在工程和预测方法逻辑之上。
- Decision: 基础筛选通过：文章以预测误差成本这一客观指标作为案例设计目标，并通过构建和改造基于传感器的预测信息系统来验证CAPS框架，报告了相对基线的量化改善。理论细筛未通过：全文未发现心理学相关理论实质指导软件制品设计；设计依据是设计科学方法和预测分析流程，而非心理学或行为机制理论。
- Confidence: 0.82

## Task Characteristics and Incentives in Collaborative Problem Solving: Evidence from Three Field Experiments

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2021.0118
- Metrics: EngineerHours; CaseTAT; CaseIdleTime; CSGHours; PSGHours; Collaboration recommendation compliance ratio
- Objective evidence: 文章的核心目标是通过协作流程和推荐系统降低问题解决成本，首要结果指标是 EngineerHours。实验一用双重差分发现新流程使 CaseTAT 下降约25.7%、EngineerHours 下降约13.6%、CaseIdleTime 下降约31.8%；实验二以 EngineerHours 为主要结果识别协作适用条件；实验三通过合规率指标和激励修正，验证了推荐系统能引导工程师采用降低成本的工作方式。
- Artifact: 信息系统的具体实例：HRTech Analytics 推荐系统（含机器学习推荐算法和仪表盘），以及嵌入客户支持流程的协作式问题解决处理过程。 — HRTech Analytics 的核心推荐模块（根据任务特征输出正式交接或协作建议），用于展示每周协作/正式交接比例的仪表盘；同时修改了客户支持流程，增加“协作”作为寻求产品专家帮助的选项。
- Theory: Hackman (1968) task characteristics and group products; Wood (1986) task complexity; Campbell (1988) task complexity; Daley (1978) team and task characteristics; Merton (1968) reward/credit allocation; Bikard et al. (2015) collaboration and scientific reward; Vakili et al. (2021) incentives and collaboration
- Theory-to-design: 未形成“心理学理论→心理/行为机制→软件制品设计选择→预期客观指标”的完整链条。实验二中的任务特征（LTE、Severity、ProblemType）虽然被映射到难度、紧迫性和不确定性，但推荐规则来自K-means聚类和HLM回归的数据驱动结果，并非由特定理论命题推导出的设计选择；实验三的激励解释是在观察低合规率并通过访谈后提出的事后诊断，随后才修改激励制度，而不是在设计系统前根据理论选择激励设计。
- Decision: 基础筛选通过：文章以提高客观、可日志化的问题解决成本指标（EngineerHours、CaseTAT、CaseIdleTime 等）为最终目标，并通过 HRTech Analytics 推荐系统和新协作流程等明确软件制品实现和验证。理论细筛不通过：虽然引用了部分心理学/行为科学文献，但没有使用心理学相关理论前瞻性地推导推荐系统或流程设计，系统规则来自数据驱动经验结果，激励解释也是事后诊断。
- Confidence: 0.82

## Telecom traffic pumping analytics via explainable data science

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113559
- Metrics: fraud detection/cluster classification accuracy; confirmed fraudulent cases / lawsuits granted; fraud loss / access charge reduction (USD savings)
- Objective evidence: 文章的核心贡献是提出并验证一个可解释 DSS 来识别 traffic pumping 并支撑法律程序；在案例中，模型 holdout 总体准确率为 97.0%，7462 个可疑 OA-OB 对中提起的诉讼全部获判欺诈，并估计 2.5 年内为两个 MNO 节省约 500 万美元、接入费下降约 40%。这些指标被用作该方法成功的主要证据。
- Artifact: 决策支持系统 (Decision Support System, DSS) — 面向 traffic pumping 欺诈检测的五步 DSS 流水线，包括基于 CDR 的特征工程模块、无监督聚类模块（k-means/DBSCAN/OPTICS/HDBSCAN）、使用 CART 决策树将聚类结果转为可解释规则的模块，以及专家标注/验证环节。
- Theory: 
- Theory-to-design: 
- Decision: 基础筛选通过：文章以客观指标为核心贡献，包括模型准确率、法院确认欺诈案件数、接入费损失下降，并提出和实际应用了一个五步 DSS 软件制品（聚类 + 决策树规则）来实现这些改进。理论细筛不通过：文章没有用可识别的心理学相关理论前瞻性地推导 DSS 设计；可解释性主要作为法律/业务约束，而非由心理机制理论指导。
- Confidence: 0.82

## Will they take this offer? A machine learning price elasticity model for predicting upselling acceptance of premium airline seating

- Year/journal: 2023 / Information & Management
- DOI: 10.1016/j.im.2023.103759
- Metrics: accepted upgrade offers count; revenue (USD); non-relevant email messages count; F1 score; Revenue Capture
- Objective evidence: 文章的研究目标RO1和RO2明确聚焦于识别可能接受/拒绝升级offer的客户和估计其价格弹性，摘要和讨论将减少无关邮件、增加接受offer数和增加收入作为PREM的核心成功主张；实验通过组件消融、与公司启发式规则式方法比较以及整体仿真验证了这些改进。
- Artifact: ML信息系统/决策支持系统：PREM（PRice Elasticity Model），用于航空公司升级offer客户筛选和定价。 — PREM整体系统及其五个组件：特征工程、去噪自编码器特征嵌入、代价敏感分类器、个性化升级offer模型、收益最大化器。
- Theory: 价格弹性（price elasticity of demand）; 选项框架/认知可得性（option framing / cognitive availability）; 消费者细分等营销概念（仅有提及，未用于设计推导）
- Theory-to-design: 未形成“理论命题→心理机制→具体软件设计选择→预期客观指标改善”的可追溯链条。PREM的特征工程、去噪自编码器嵌入、代价敏感分类、二元自编码器分段和ILP收益最大化主要由数据稀疏、噪声、类别不平衡、业务收益目标等工程和业务因素驱动，而非由心理学理论推导。文献中提到的消费者行为文献（如选项框架、折扣感知、稀缺性）没有说明如何决定PREM的某个具体设计特征。
- Decision: 基础筛选通过：文章以接受升级offer数量、收入、无关邮件量等客观指标为最终目标，并通过PREM这一明确的ML信息系统的设计、构建和消融/仿真评价来实现这些改进。理论细筛不通过：文章虽提及价格弹性、认知框架等术语，但未用任何心理学相关理论前瞻性地推导PREM的具体设计特征，理论—设计—指标链条不成立。
- Confidence: 0.82

## sDTM: A Supervised Bayesian Deep Topic Model for Text Analytics

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1124
- Metrics: perplexity; classification accuracy; AUROC
- Objective evidence: 文章的核心贡献是提出并验证sDTM方法；第5节用困惑度比较主题模型拟合质量，第7节用准确率和AUROC比较预测性能，并与LDA、sLDA、NTM、RNN attention、BERT等基线对照，构成对sDTM改进效果的主要验证。
- Artifact: 深度主题建模软件工具（Python实现的sDTM模型） — sDTM的完整模型结构，包括VAE式神经主题模型、双向GRU序列编码器、主题注意力层以及标签预测输出层。
- Theory: 
- Theory-to-design: 不存在从心理学理论到sDTM设计选择的完整链条；文中涉及的信息过载、感知有用性等概念仅用于下游实证假设或结果解释，未指导软件制品设计。
- Decision: 基础筛选通过：文章以困惑度下降、分类准确率和AUROC提升等客观指标为核心贡献，并设计/开源了一个Python实现的深度主题建模软件工具sDTM。理论细筛不通过：sDTM的设计完全基于统计推断和深度学习机制，没有心理学理论实质指导设计。
- Confidence: 0.82

## A Data Analytics Framework for Smart Asthma Management Based on Remote Health Information Systems with Bluetooth-Enabled Personal Inhalers

- Year/journal: 2020 / MIS Quarterly
- DOI: 10.25300/misq/2020/15092
- Metrics: AUC (Area Under the Curve); false alarm rate; misdetection rate; time-to-alert
- Objective evidence: 文章的研究目标是开发一个检测异常吸入器使用的数据分析框架，性能评估部分以AUC、误报率、漏报率、时间到警报等客观指标作为主要依据，并与多种基准方法比较，显示GLMM-GQP在多数情况下性能最优（Table 4和Figure 9）。这些指标是文章判断设计成功与否的核心证据。
- Artifact: 智能哮喘管理系统（SAM system，一种远程健康信息系统HIS） — 用于检测异常吸入器使用的数据分析框架（包括GLMM-GQP统计模型、数据转换和检测算法），作为SAM系统的分析模块/功能组成部分
- Theory: 
- Theory-to-design: 不存在从心理学理论到设计选择的推导链。文章没有解释哪个心理学理论导致选择某种设计特征，也没有先验的理论命题指导算法设计。
- Decision: 基础筛选通过：文章以AUC、误报率、漏报率、时间到警报等客观指标为核心贡献，并通过对SAM系统中数据分析组件（GLMM-GQP检测算法）的设计和评估来实现；理论细筛不通过：全文未使用心理学相关理论指导软件制品设计，仅基于统计方法和环境因素。
- Confidence: 0.8

## A deep learning approach for detecting fake reviewers: Exploiting reviewing behavior and textual information

- Year/journal: 2023 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113911
- Metrics: Accuracy; Precision; Recall; F1-score; AUC
- Objective evidence: 文章的研究问题和核心贡献均是提升假评论者检测性能；实验1和实验2将其模型与LR、RF、SVM、CART、NB、CNN、BiLSTM、C-LSTM、BERT、Longformer等多种基准比较，并通过消融实验检验各组件贡献，证明其Accuracy、F1和AUC等指标显著提升。
- Artifact: 面向电子商务/在线评论平台的自动假评论者检测框架（深度学习检测模型/组件） — 端到端假评论者检测框架，包括行为敏感特征提取器（一维卷积CNN）和上下文感知注意力机制（Longformer + CNN + BiLSTM + Attention），以及最终的融合分类层。
- Theory: 
- Theory-to-design: 不存在“心理学理论→心理机制→软件制品设计选择→客观指标改善”的链条。行为特征的局部依赖性假设是基于特征相关性和统计建模，文本部分选择Longformer、CNN、BiLSTM和注意力机制是基于NLP任务需求和计算效率，而非心理学理论推导。
- Decision: 基础筛选通过：文章以假评论者检测的Accuracy、Precision、Recall、F1和AUC等客观指标为最终目标和核心贡献，并在两个Yelp数据集上通过基准对比和消融实验验证改善；其核心方案是明确的自动假评论者检测框架，包含行为敏感特征提取器和上下文感知注意力机制，可视为软件检测组件。理论细筛不通过：文章未引用或使用可识别的心理学相关理论来指导制品设计，设计依据是深度学习和统计特征建模，而非心理或行为机制理论。
- Confidence: 0.8

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

## A new approximate belief rule base expert system for complex system modelling

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113558
- Metrics: MSE (mean square error)
- Objective evidence: 案例研究以MSE作为主要有效性验证指标：比较初始ABRB与优化ABRB、ABRB与BRB/FRB/BPNN/ELM，以及不同训练集规模下的MSE；优化后MSE下降93.11%，说明客观指标是核心验证方式。
- Artifact: ABRB expert system（近似置信规则库专家系统） — 新提出的单属性近似置信规则（ABR）、基于独立性因子对属性权重进行折扣的机制、证据推理（ER）推理模块，以及属性、参考值和识别框架的扩展机制。
- Theory: 
- Theory-to-design: 
- Decision: 基础筛选通过：文章以锂电池容量估计MSE作为主要有效性指标，通过初始与优化ABRB对比、多模型对比和训练规模对比验证改进；该指标来自仪器实测容量，不依赖主观感知；所构建和优化的ABRB专家系统属于明确的软件制品/智能系统。理论细筛未通过：全文没有使用心理学相关理论指导ABRB设计，设计依据主要是信息论相关性度量、Stone-Weierstrass逼近定理和领域专家知识，未形成理论—设计链。
- Confidence: 0.8

## Algorithmic Assortative Matching on a Digital Social Medium

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2022.1135
- Metrics: Revenue (USD); Messages; Weekly event mission starts; Weekly event mission successes; Retention (14-day active)
- Objective evidence: 文章的核心贡献是评估算法分类匹配系统对用户参与、支出和社交化的因果影响；通过现场实验（系统开/关）和用户级/团队级回归，验证系统开启后收入、消息、任务开始/成功和保留率均获得统计显著的改善，并以此作为主要结论
- Artifact: 移动游戏应用内的算法匹配/推荐系统（数字社交媒介） — 为达到团队推荐资格的新用户生成团队推荐列表的匹配系统，包括用户CLV预测分类器（XGBoost）、团队活动评分分类器和每日供需匹配分配算法
- Theory: 
- Theory-to-design: 不存在完整的理论→心理机制→制品设计→客观指标推导链。文章设计匹配系统主要基于对生产函数互补性的初步经济分析和CLV/活动评分的机器学习分类；匹配策略（高价值用户匹配高活动团队）来源于经济互补性推理，而非心理学理论。条件合作者文献的引用仅是对匹配系统可能有效的解释性说明，未约束系统规则、推荐列表生成、分类阈值或交互界面的具体设计选择
- Decision: 基础筛选通过：文章以收入、消息数、每周任务开始/成功数、14天保留率等客观指标为最终目标和核心贡献，并通过设计和部署一个游戏应用内的算法匹配/推荐系统（用户CLV分类器+团队活动评分+供需匹配算法）在真实现场实验中验证了这些指标的改善。理论细筛不通过：文章没有用心理学相关理论前瞻性地指导该匹配系统的具体设计；条件合作等概念仅作为背景动机，设计由经济互补性和机器学习驱动，机制研究为事后分析。
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

## LINDA-BN: An interpretable probabilistic approach for demystifying black-box predictive models

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113561
- Metrics: 规则1在真阳性/真阴性中的占比; 规则3和规则4在假阳性/假阴性中的占比; 规则与真实分类标签的一致性
- Objective evidence: 文章的核心贡献是提出LINDA-BN及四条规则，用来帮助决策者评估黑盒预测的可靠性。评估部分通过表3和表4展示了规则在不同分类结果中的分布，发现规则1主要对应正确分类，规则3/4主要对应误分类，从而验证该方法能客观指示预测可靠性，这也构成了文章的主要改进证据。
- Artifact: 开源解释工具/框架（local post-hoc model-agnostic interpretation tool） — LINDA-BN框架，包括局部置换生成模块、贝叶斯网络结构学习模块（Greedy Hill Climbing + 离散化）、Markov blanket计算模块、四条置信度规则判定模块
- Theory: 溯因推理（Abduction, Peirce）; 有限理性（Bounded Rationality）
- Theory-to-design: 文章在3.4节提及决策者可借助溯因推理从Markov blanket中寻找最简解释，也提到人类因有限理性而倾向简化结构，但这些概念仅用于描述解释过程或背景，并未推导出任何具体设计选择。置换范围、离散化方式、网络学习算法、Markov blanket计算和规则定义均源自概率图模型和实验观察，而非心理学理论命题。因此不存在“理论→心理机制→制品设计→客观指标”的可追溯链条。
- Decision: 基础筛选通过：文章提出并实现LINDA-BN解释工具，通过置换、贝叶斯网络学习和Markov blanket生成局部解释规则，并用分类正确性（TP/TN/FP/FN）等客观指标验证规则能指示预测可靠性，满足客观指标和软件制品要求。理论细筛不通过：虽然提到溯因推理、有限理性等心理学相关概念，但仅用于解释用户如何理解图形或作为背景，没有形成从理论到具体软件设计选择的推导链，不满足实质理论指导。
- Confidence: 0.8

## Let Artificial Intelligence Be Your Shelf Watchdog: The Impact of Intelligent Image Processing-Powered Shelf Monitoring on Product Sales

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/16813
- Metrics: focal product sales (Log(Sales), monthly sales in CNY); retailer compliance rates (facing compliance rate and position compliance rate)
- Objective evidence: 文章的核心目标是检验IIP货架监控是否提升产品销售额，并通过准实验、随机现场实验、终止监控实验和成本收益分析反复验证销售额提升（约14%-17%），同时用合规率变化解释机制。销售额是最终结果变量和主要贡献。
- Artifact: IIP-powered shelf monitoring system: a mobile app installed on delegates' smartphones with cloud image upload and AI/computer vision image recognition backend — 移动App及其AI图像识别模块：拍摄货架照片、上传云端、自动识别焦点产品的面向数和货架位置、生成合规报告（面向合规率和位置合规率）。
- Theory: algorithm appreciation/aversion; monitoring and rational cheating; behavioral persistence
- Theory-to-design: 未形成理论→设计→指标的完整链条。文章没有用心理学理论前瞻性推导IIP系统或其功能的设计选择；IIP系统的核心设计（拍照、AI检测面向数和位置、生成合规报告）由货架管理和合约执行需求驱动。算法欣赏/厌恶文献用于预期业务员是否使用AI，监控/行为持续性文献用于设定研究假设和实验设计（如终止组），而非软件设计特征。
- Decision: 基础筛选通过：文章以IIP货架监控系统对产品销售额的因果提升为核心贡献，销售额由商店销售记录获得，不依赖主观感知；该系统是明确的软件制品（移动App+AI图像识别），并以销售额为主要客观指标进行评价。理论细筛未通过：文章虽引用算法欣赏/厌恶、理性欺骗、行为持续性等心理/行为概念，但多为事后解释或研究预期，未前瞻性指导软件制品的设计选择；不存在从心理学理论命题到具体设计特征再到客观指标的推导链。
- Confidence: 0.8

## Optimizing microtask assignment on crowdsourcing platforms using Markov chain Monte Carlo

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113404
- Metrics: AUC; F-Score
- Objective evidence: 文章的核心贡献是提出并验证MCMC-TA任务分配算法；评价部分通过预算驱动和群体规模实验，以AUC和F-Score为主要指标与ROUX、Gaussian、Raykar等算法比较，并辅以Wilcoxon检验，结果支持MCMC-TA更优。
- Artifact: 面向微任务众包平台的任务分配决策组件/算法（MCMC-TA） — MCMC-TA算法本身，尤其是GMM工人质量迭代估计模块、MCMC/Metropolis-Hastings工人筛选模块，以及按轮次分配任务和更新工人质量的系统规则。
- Theory: 
- Theory-to-design: 无。MCMC-TA的设计由概率建模和优化目标驱动，没有形成“心理学理论命题→心理/行为机制→软件制品设计选择→客观指标改善”的可追溯链条。
- Decision: 基础筛选通过：文章以不依赖主观感知的AUC和F-Score为核心指标，且将MCMC-TA设计为众包平台任务分配组件，并用这些客观指标验证其改进。理论细筛不通过：文章未使用可识别的心理学相关理论实质指导软件制品设计，其设计依据是MCMC、GMM等统计与优化方法。
- Confidence: 0.8

## ROLEX: A Novel Method for Interpretable Machine Learning Using Robust Local Explanations

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/17141
- Metrics: local fidelity score (LocalFid); LDA-fidelity score (local decision-boundary aware fidelity)
- Objective evidence: 局部忠实度是文章的核心贡献和主要成功依据。摘要明确称 ROLEX 在局部忠实度上优于主流基准；贡献(2)也强调提高局部忠实度；正文通过三个医疗数据集将 ROLEX 与 LIME、LS、LEAP 比较，报告 Fidelity 与 LDA-fidelity 分数（Table 5），并利用消融实验（Table 7）验证组件贡献。
- Artifact: ROLEX：用于 HPA 系统的局部、模型无关解释方法，并配套一个基于 Plotly/Dash 的 Web 原型用户界面；ROLEX 作为可运行的解释生成组件嵌入医疗预测分析系统中。 — ROLEX 的三阶段方法：(1) 合成数据生成（通过优化采样中心和采样半径、SMOTE 过采样）；(2) 局部模型拟合（利用 LinSep 分数选择线性或非线性解释模型，及 LDA 框架）；(3) 患者级解释生成与展示；此外还包括原型用户界面的多种解释模式（文本、局部系数、决策规则、可视化）。
- Theory: 
- Theory-to-design: 不存在完整的理论→心理机制→设计选择→客观指标链条。XAI 框架的三项要求是一般性设计建议；交互式界面原则只影响原型 UI 的信息呈现方式，且没有说明由哪个心理学理论命题推导出该设计；ROLEX 的采样优化、SMOTE、LinSep 和 LDA 等核心设计均来自机器学习方法和局部忠实度目标，而非心理学理论。
- Decision: 基础筛选通过：文章最终目标和核心贡献是提升局部解释的客观忠实度，并通过 ROLEX 方法在三个数据集上与多个基准比较验证改进；ROLEX 被实现为 HPA 解释系统中的明确计算组件，并配套原型用户界面。理论细筛不通过：文中没有可识别的心理学理论前瞻性地指导软件制品设计，只有一般性 XAI 框架和交互设计原则，无法构成理论→心理机制→设计→客观指标的完整链条。
- Confidence: 0.8

## Stratifying no-show patients into multiple risk groups via a holistic data analytics-based framework

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113269
- Metrics: AUC; sensitivity; specificity; accuracy
- Objective evidence: 文章的研究目的和核心贡献是准确预测no-show患者、构建简洁模型并处理数据不平衡，预测性能是衡量成功的主要依据；Section 4.2及Table 5-7以AUC、敏感性等为主要比较标准，并展示加入变量选择和数据平衡后敏感性显著提升（如ANN敏感性从0.416提高到0.792），阈值分析也说明高置信区间预测表现提升。
- Artifact: 基于Web的决策支持工具（R Shiny应用程序） — 整合最优ANN模型的web决策支持工具，包括ANN预测模块、患者个体no-show风险评分、五级风险分层输出，以及用户输入预约/患者信息并查看风险结果的功能。
- Theory: 
- Theory-to-design: 不存在从心理学理论命题到被解释的心理机制、再到具体软件设计选择的完整链条。变量选择、数据平衡、分类模型和风险分层的设计依据是预测性能、参数寻优和成本/风险权衡，而非心理学机制。
- Decision: 基础筛选通过：文章以no-show预测的分类性能（AUC、敏感性、特异性、准确率）作为最终目标和核心贡献，指标来自实际到诊/未到诊标签并由程序自动计算，不依赖主观感知；文章还开发了整合最优ANN模型的web决策支持工具，核心预测模块接受客观评测。理论细筛不通过：未识别任何心理学相关理论前瞻性地指导软件制品设计；模型和工具设计基于数据挖掘、优化算法和性能指标，而非心理学机制。
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

## A generic framework for sentiment analysis: Leveraging opinion-bearing data to inform decision making

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113304
- Metrics: classification accuracy; ROC-AUC; F1-score; precision; recall
- Objective evidence: ECCO框架的核心贡献之一是引导用户开发鲁棒的情感分类模型，论文在第5.1节明确将“所开发模型能达到与基准竞争的性能”以及“框架引导的机器学习模型显著优于lexicon-based模型”作为主要贡献；第4.3节用准确率等客观指标展示PL04、Yelp、Twitter、SMS四个数据集上的改进和竞争力。
- Artifact: 决策支持系统软件，即ECCO框架的实例化程序ECCO system — 完整的ECCO系统，包括GUI、数据库、处理组件（模块1.0–5.0）、情感建模组件（模块6.0–12.0）和分析组件（模块13.0–18.0），具体涉及文本预处理、特征工程、模型选择与超参数调优、结果可视化以及与结构化数据的关联分析。
- Theory: 
- Theory-to-design: 不适用。文中没有形成“心理学理论命题→心理/行为机制→具体软件设计选择→预期客观指标”的推导链。
- Decision: 基础筛选通过：文章设计并实现了一个明确的软件制品ECCO system（决策支持系统），并以情感分类准确率、AUC、F1等客观指标作为框架有效性和核心贡献的证据，在四个数据集上与基线和文献基准比较。理论细筛未通过：全文没有使用心理学相关理论实质指导软件制品设计，仅依赖数据科学和DSS工程原则，因此不满足要求C。
- Confidence: 0.78

## A hybrid decision support system for adaptive trading strategies: Combining a rule-based expert system with a deep reinforcement learning strategy

- Year/journal: 2024 / Decision Support Systems
- DOI: 10.1016/j.dss.2023.114100
- Metrics: 累计收益率 (%AR); 平均年化收益率; 平均日收益率; 夏普比率 (SR); 最大回撤 (MDD); 标准差 (SD); 交易信号数量
- Objective evidence: 文章的核心贡献是提出并验证混合交易系统能提升风险调整后收益并适应市场。消融实验显示 RB+RL+C1+C2 在 S&P500 上 %AR=59.37、年化夏普=0.68、MDD=-2.82，均优于基准 RB、RL、B&H；在多种市场情景和另外五只指数基金中也以这些指标验证了改进。
- Artifact: 混合决策支持系统 / 智能交易系统（hybrid decision support system / hybrid trading system），由规则型专家系统与深度强化学习策略结合 — RL 智能体的状态空间设计（加入 RB 决策信息、投资者可用资产状态）以及基于策略梯度动作概率的交易量调节机制
- Theory: 
- Theory-to-design: 不成立。文章没有给出‘心理学理论命题 → 心理机制 → 具体设计选择 → 预期客观指标’的完整链条；RB 状态空间来自金融趋势跟踪规则，C1 来自真实交易中的资产约束，C2 来自 PG 算法 softmax 输出的使用，均不是由心理学理论推导得出。
- Decision: 基础筛选通过：文章以提高风险调整后收益、降低回撤/波动等可客观计算指标为核心贡献，并通过构建混合决策支持系统（状态空间与交易量机制）实现。理论细筛不通过：文章未使用可识别的心理学理论实质指导软件制品设计，设计依据主要是金融交易规则、强化学习机制和资产约束常识。
- Confidence: 0.78

## A new emergency decision support system: the automatic interpretation and contextualisation of events to model a crisis situation in real-time

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113260
- Metrics: interpretation time delay; contextualisation time delay; visualisation time delay; correctness of interpretation/contextualisation
- Objective evidence: 第5.3节将该量化评估作为系统能力验证的主体，说明系统能够近实时获取、解释、情境化和传播事件，并以第5.4节4Vs管理作为架构级贡献。该评估直接检验了AIC系统的主要贡献（CEP引擎连接图数据库并持续更新COP），因此实时性和正确性构成核心贡献的验证依据；虽然没有传统基线，但以预先规定的近实时阈值作为参照点。
- Artifact: 应急决策支持系统（emergency decision support system），具体为AIC信息系统与R-IOSUITE原型整合后的可运行软件系统 — 设计并实现了AIC子系统：事件获取（基于发布/订阅的消息代理）、复杂事件处理引擎（解释规则与情境化规则）、Neo4J图数据库查询API、公共态势图COP的自动更新显示；并扩展了R-IOSUITE中的危机情境元模型（新增Data source、Critical infrastructure、Sensitive building概念）。
- Theory: Endsley's Situation Awareness theory; D'Aniello et al. cognition process for situation awareness; Wolbers & Boersma's Common Operational Picture / collective sensemaking
- Theory-to-design: 文章用“自动化情势感知的感知层”将Endsley理论与系统目标联系起来，但并未从理论命题具体推导出CEP规则、图数据库查询、消息代理、元模型扩展等设计选择。实现细节如规则语言、Neo4J查询、事件类型、阈值设定均来自业务规则和工程需求，而不是由心理学机制约束。因此缺少“理论命题→心理机制→具体设计特征→预期客观指标”的完整可追溯链条。
- Decision: 基础筛选通过：文章设计并实现了明确的应急决策支持系统（AIC+R-IOSUITE），目标是近实时自动解释、情境化事件并更新公共态势图；第5.3节用解释时间、情境化时间、可视化时间和确定性正确性等客观指标验证了该软件制品。理论细筛未通过：虽然引用了Endsley的情势感知理论等，但仅用于高层动机和系统功能定位，未从心理学理论命题实质推导具体软件设计，也没有对理论指导的设计部分进行专门检验。
- Confidence: 0.78

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

## Optional Verification and Signaling in Online Matching Markets: Evidence from a Randomized Field Experiment

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1194
- Metrics: verify/opt-in rate; msg_sent; msg_received; match_sent; match_received; sender_popularity; receiver_popularity
- Objective evidence: 研究问题、摘要和结果部分均以验证后的消息/匹配结果为核心；随机实验将T1/T2与控制组比较，并通过TOT估计验证效应，主要表格（表9-14）直接检验改进。
- Artifact: 在线约会平台中的可选手机号验证功能/机制 — 将手机号验证设计为可选项：一次性邀请消息、付费（50虚拟币）与免费两种验证流程、SMS验证页面、验证成功后在个人主页和搜索结果页展示的验证徽章。
- Theory: signaling theory (Spence 1978); 信号成本/可信度理论; 性别偏好文献（Buss等）
- Theory-to-design: 未形成完整的理论→心理机制→制品设计→客观指标链条。文章用信号理论推导的是用户是否/谁会验证、验证后的接收方反应和用户自身行为变化，属于对已确定实验干预的行为预测和解释；没有说明信号理论如何导致‘可选项+徽章+免费/付费’等具体软件设计选择，也没有与替代设计比较来验证理论推导。
- Decision: 基础筛选通过：文章以可观察、可重复计算的平台行为指标（消息数、匹配数、对手popularity）为核心结果，通过随机田野实验引入并评估在线约会平台的可选手机号验证功能，因此同时满足客观指标目标和明确软件制品改造。理论细筛不通过：所使用的信号理论主要用于生成用户验证选择和结果假设，并在事后解释差异，并未前瞻性地推导验证功能的具体软件设计，未达到心理学相关理论实质指导软件制品设计的要求。
- Confidence: 0.78

## Predicting employee absenteeism for cost effective interventions

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113539
- Metrics: Total misclassification cost (TC); Cost Improvement Score (CIS); Return On Investment (ROI); Balanced Accuracy (BACC); AUC; FPR; FNR
- Objective evidence: 文章核心贡献是提出员工缺勤的误分类成本矩阵和成本化评价指标，并以CIS/ROI作为模型选择和成本效果判断的主要依据；结果显示每个预测期都能找到CIS>0且ROI>0的模型，并与不干预/全干预朴素基准比较验证成本改善。
- Artifact: 决策支持系统（Decision Support System） — 基于机器学习分类的病假风险识别与干预目标选择流程，包括目标变量阈值定义、成本矩阵、多种树集成分类器、采样/校准/阈值后处理、以及CIS/ROI评价框架。
- Theory: 
- Theory-to-design: 不存在从心理学理论命题到具体软件设计选择的完整链条。干预类型和成本参数作为外部场景给出，未由心理学理论推导；预测特征、分类器和阈值规则也没有明确的心理机制依据。
- Decision: 基础筛选通过：文章以客观的成本指标（TC、CIS、ROI）为核心贡献并验证改进，同时明确设计和评价了一个决策支持系统。理论细筛不通过：全文未发现心理学理论对软件制品设计的前瞻性指导，仅涉及一般性的健康干预背景描述。
- Confidence: 0.78

## Real-Effort Incentives in Online Labor Markets: Punishments and Rewards for Individuals and Groups

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2023/15166
- Metrics: tag count (number of tags contributed per image); cosine similarity score based on GloVe and Google Cloud Vision API
- Objective evidence: 研究问题和假设围绕奖励/惩罚及个体/群体层面干预对努力的影响；结果部分以标签数作为主要因变量，通过随机效应和双向固定效应面板回归验证干预后各处理组努力显著提高。
- Artifact: 基于oTree的Web在线协作图像标注实验系统 — 包括实验界面、4人随机分组、图像标签收集、基于Google Cloud Vision API和GloVe的相似度与收益计算、第6轮随机外生干预（收益乘数变化与消息通知）等机制。
- Theory: 公共品博弈理论; 搭便车问题文献; Nash均衡与边际人均回报理论
- Theory-to-design: 理论到设计链不完整：从公共品博弈推导出‘降低收益会降低努力、提高收益会提高努力’的经济学假设，并据此设计个体/群体奖励或惩罚的乘数变化；但该链中没有心理学相关理论命题或心理机制作为设计依据，主要是经济激励预期。
- Decision: 基础筛选通过：文章以提高在线劳动力市场参与者的努力（标签数）这一客观指标为最终目标，并通过自主构建的oTree协作图像标注实验系统实施个体/群体奖励和惩罚机制，使用系统记录的标签数验证干预效果。理论细筛未通过：设计依据是公共品博弈和经济学激励预期，不属于心理学相关理论对软件制品设计的实质指导。
- Confidence: 0.78

## Retargeted vs. Generic Product Recommendations: When is it Valuable to Present Retargeted Recommendations?

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2020.0560
- Metrics: RP sales; RP impressions; RP conversion rates (click-through rate, purchase conditional on view); FP+RP total product sales; daily FP impressions; total sales in counterfactual simulation
- Objective evidence: 研究问题明确围绕retargeted与generic推荐在购买漏斗不同阶段的销售价值，主要贡献是估计两类推荐对RP销售额、印象数和转换率的相对影响，并用现场实验、在线实验和反事实模拟验证销售改善（模拟最高约3%总销售提升）；这些客观指标是最终目标而非附属结果。
- Artifact: 电子商务网站上的产品推荐系统/推荐展示模块；另包括在线实验网站及其推荐算法实现 — 现场实验中修改了商品详情页（FP页面）上的推荐产品（RP）展示模块：处理版本显示四个RP，控制版本隐藏RP；在线实验构建了实验网站，并实现了基于Slope-One算法生成generic推荐、基于用户历史浏览生成retargeted推荐的独立推荐生成与展示逻辑。
- Theory: AIDA/purchase funnel stage model; retargeted advertising literature; repeated exposure / recall / relevance mechanisms
- Theory-to-design: 不存在完整的“理论→心理机制→具体软件设计→客观指标”链条。文章用购买漏斗将用户分为早期和晚期，并随机展示/隐藏推荐，但并没有在设计推荐算法、界面展示或系统规则之前用心理学理论推导这些设计选择。在线实验的generic推荐由Slope-One算法的相似度生成，retargeted推荐由历史浏览随机生成，这些设计来自推荐算法和重定向广告实践而非心理学理论；模拟中的按漏斗阶段替换推荐规则来自实证估计结果，不是理论前瞻性推导出的系统设计。
- Decision: 基础筛选：通过。文章以提高RP销售额、FP+RP总销售额、印象数和转换率等客观指标为最终目标，指标来自系统日志和实际购买，不依赖主观感知；其实质上通过修改电商网站FP页面推荐展示模块，并搭建带独立推荐算法的在线实验网站来实现和检验。理论细筛：不通过。购买漏斗/AIDA、重复曝光/回忆/相关性等心理相关概念仅用于购买阶段划分、研究假设和结果解释，未在软件制品设计确定之前用以推导展示规则、算法或界面特征；因此不具备心理学理论实质指导软件制品设计的可追溯链条。
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

## How Do Recommender Systems Lead to Consumer Purchases? A Causal Mediation Analysis of a Field Experiment

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2021.1074
- Metrics: conversion rate / propensity to place an order (Order); order value / revenue per session (lnOrderVal); consideration set size (lnSetSize); average page views per product in consideration set (lnViewsPerItem)
- Objective evidence: 文章以随机现场实验为核心方法，将推荐系统的使用与否作为处理变量，将转化率和订单金额作为主要经济结果，并进一步用它们作因果中介分析的总效应。Table 6 和 Table 5 表明推荐系统显著提高转化率（几率提高12.4%）、订单金额（增加1.7%）、考虑集规模（增加3.2%）和平均浏览深度（增加0.9%）。这些客观指标是检验研究模型的主要依据。
- Artifact: 在线书店网页中的个性化推荐系统，具体为基于记忆型协同过滤（memory-based collaborative filtering）的推荐模块。 — 在图书详情页中设计和部署了一个推荐模块，向处理组会话显示3本推荐图书，控制组则不显示；推荐系统根据相似顾客的购买行为生成推荐。
- Theory: Consideration set / consider-then-choose decision process; Search cost theory; Consumer involvement and commitment
- Theory-to-design: 文章使用考虑集理论来推导中介模型：推荐系统通过影响考虑集规模和每个备选产品的卷入程度，进而影响购买。但该理论并未用于推导或约束推荐系统本身的软件设计选择。推荐系统采用标准的记忆型协同过滤算法，处理条件是显示3本推荐产品，这些设计选择来自两个预实验的结果和行业实践，而非心理学理论命题的推导。因此不存在“理论→心理机制→具体软件制品设计→客观指标”的完整前瞻链条。
- Decision: 基础筛选通过：文章以在线书店中的协同过滤推荐系统为软件制品，通过随机现场实验检验其对转化率、订单金额等客观指标的影响，这些指标来自服务器日志和实际购买行为，构成核心结果。理论细筛不通过：考虑集等心理学相关理论用于建立中介模型，但未前瞻性地指导推荐系统本身的设计或改造；推荐系统的具体实现和设计选择来自预实验和行业实践，未形成理论到软件设计再到客观指标的完整推导链。
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

## A two-stage machine learning framework to predict heart transplantation survival probabilities over time with a monotonic probability constraint

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113363
- Metrics: AUC; accuracy; sensitivity; specificity; G-Mean
- Objective evidence: 文章的核心贡献是提出一个两阶段机器学习框架，以获得个性化、数据驱动且单调约束的生存概率曲线；在UNOS数据上报告Stage I模型AUC在0.60–0.71之间，10年AUC为0.70，并声称高于现有文献结果；Table 4和Fig.4报告留出集上的AUC/G-Mean等；Table 5比较isotonic regression前后的AUC/G-Mean，多数时期指标有所改善。
- Artifact: Web应用程序/决策支持工具：H-TOP (Heart Transplantation Outcome Predictor)，基于R Shiny构建；同时提供可复现的R Markdown分析代码。 — H-TOP app的核心功能模块：数据输入（手动输入或CSV上传）、数据质量检查、调用训练好的11个时间点logistic回归模型、使用isotonic regression校准生存概率、输出表格和生存概率图。
- Theory: 
- Theory-to-design: 
- Decision: 基础筛选通过：文章以AUC、G-Mean等客观预测性能指标为核心评价指标，最终目标是提高心脏移植生存概率预测精度并保证单调性；文章还构建了明确的软件制品H-TOP web app，将两阶段框架封装为可运行的预测/校准工具，且核心预测/校准模块受到客观指标检验。理论细筛不通过：全文没有使用心理学相关理论来指导软件制品设计，仅有“用户友好”等常识性表述，不能构成心理学理论指导的证据。
- Confidence: 0.72

## Cost-based analysis of the impact of data completeness and representational consistency

- Year/journal: 2023 / Decision Support Systems
- DOI: 10.1016/j.dss.2023.114044
- Metrics: P_correct：能正确构造 SQL 查询解决任务的参与者比例; T_solved：解决任务所需的平均时间; 查询/尝试次数：完成任务所需提交的查询数量，包括数据质量问题相关查询数
- Objective evidence: 这些指标是文章验证成本式数据质量分析的主要因变量，用于比较 D_A、D_B、D_C 三个数据库版本，量化数据质量改进的实际影响。论文的核心主张是传统规则式质量测量不能反映实际影响，而成本式指标能够提供直接、可量化的证据，该主张完全由这些客观指标支撑。
- Artifact: 集成关系数据库（PostgreSQL）以及用于提交 SQL 查询和判定正确性的在线查询平台 — 构建了集成数据库 D_A；据此创建并实质改造了 D_B 和 D_C，包括合并重复作者、补全/统一 ORCID ID、GRID ID 和 FundRef ID、增加结构化标识符、改进数据库规范化程度（增设表）等。在线查询平台用于与数据库交互、记录提交时间并判定查询正确性。
- Theory: 
- Theory-to-design: 不存在从心理学理论命题→心理/行为机制→具体数据库或查询平台设计选择→客观指标改善的完整推导链。数据库改进（去重、统一标识符、补全 ID、增加规范化表）来自数据质量维度及成本分析框架，而非心理学理论。
- Decision: 基础筛选通过：文章以客观任务完成比例、解决时间和提交查询次数作为核心评价指标，并通过构建/改造三个集成 PostgreSQL 数据库版本（D_A/D_B/D_C）及在线查询平台来检验数据质量改进对数据可用性的影响，因此同时满足要求 A 和 B。理论细筛未通过：文章没有使用心理学相关理论前瞻性地指导软件制品设计；‘学习效应’‘疲劳’等仅是事后讨论性解释，不构成理论到设计的推导链。
- Confidence: 0.72

## Data misrepresentation detection for insurance underwriting fraud prevention

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113798
- Metrics: CDE loss; HDR coverage loss; Kullback-Leibler divergence; fraud risk score distribution difference
- Objective evidence: 文章的核心贡献是将保费欺诈检测建模为条件密度估计问题，并以CDE loss和HDR coverage loss作为模型选择、校准和比较的主要客观依据（如选择基大小、比较FlexCode与RFCDE）；同时通过欺诈风险评分在高风险子样本与总体的分布差异，说明所提方法对识别欺诈申请的有效性。
- Artifact: 保险核保欺诈风险决策支持系统（decision support system） — 该系统中的一个核心评分模块/流程：基于条件密度估计（FlexCode/RFCDE）和定价策略计算保费欺诈风险评分的模块，包含训练、验证和预测三个阶段。
- Theory: 
- Theory-to-design: 不存在从理论命题到心理机制、具体制品设计和客观指标的完整推导链。方法设计完全来自统计学与机器学习（条件密度估计、随机森林、正交基投影、Shapley值），没有心理学理论约束或推导任何设计特征、交互机制或系统规则。
- Decision: 基础筛选通过：文章以CDE loss、HDR coverage loss等客观指标作为所提条件密度估计方法的核心评估依据，并通过设计一个核保欺诈风险决策支持系统及其评分模块来实现欺诈检测目标。理论细筛不通过：文章未使用可识别的心理学理论实质指导软件制品设计，仅有欺诈动机框架的背景性提及，不构成设计推导链。
- Confidence: 0.72

## Designing information feedback for bidders in multi-item multi-unit combinatorial auctions

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2019.113230
- Metrics: 平均每笔出价的计算/处理时间（runtime per bid）; 增量计算运行时间（incremental runtime）; MDL/MWL计算正确性（通过理论正确性证明而非主观评价）
- Objective evidence: 文章的核心贡献是提出可实时计算 MDL/MWL 的精确方法和增量实现，并在摘要与结论中将‘时间与内存需求不过高’作为方法可用于在线MUCAs的关键证据。实验显示复杂实例下平均每出价处理时间小于0.2秒，增量运行时间为亚秒级，据此论证该信息反馈DSS能够满足在线连续拍卖的实时性能要求。
- Artifact: 面向竞买人的决策支持系统（DSS）/计算工具，用于在线多单元组合拍卖中的实时信息反馈 — DSS 中计算包 MDL(p,t) 和 MWL(p,t) 的核心算法模块，包括 Compute_MDL 算法、增量计算方法、MU-OR 和 MU-XOR 两种形式的动态规划实现，以及接收出价并返回反馈值的查询功能。
- Theory: 
- Theory-to-design: 不存在完整链条。文章没有从任何心理学理论命题出发，推导出 MDL/MWL 反馈的具体设计选择；设计主要由组合拍卖机制、胜者决定问题的计算复杂性和算法可行性决定。‘认知负荷’仅作为问题背景出现，未形成理论→心理机制→设计特征→客观指标的推导链。
- Decision: 基础筛选通过：文章以在线多单元组合拍卖中的竞买人实时反馈为问题，明确提出和开发了一个决策支持系统（DSS），其核心计算模块根据已收到的出价返回包的 MDL/MWL 值；客观评价指标为模拟数据和真实频谱拍卖数据上的运行时间，用于证明该软件制品可满足实时反馈需求。理论细筛未通过：文章没有使用某一心理学相关理论前瞻性地指导软件制品设计；认知负荷等概念仅作为背景或文献引用出现，未形成理论到设计特征的实质推导关系。
- Confidence: 0.72

## Dynamic, Multidimensional, and Skillset-Specific Reputation Systems for Online Work

- Year/journal: 2021 / Information Systems Research
- DOI: 10.1287/isre.2020.0972
- Metrics: Spearman rho; Kendall tau; average performance of ranked cohorts; lift; total variation distance to normal distribution; ranking correlations for nonperfect workers; within-opening top-n average performance; MAE; RMSE; AUC improvement
- Objective evidence: 核心贡献是提出HMM-W2V声誉框架，以提供准确的技能集特定动态声誉。第5.3节用10折交叉验证对比10个替代声誉系统，报告显著改进：排名相关平均改善20%-85%，非完美工人识别p<0.001，职位内Top-n表现改善；第5.4.2节显示AUC提升2.4%-10%；附录D报告MAE/RMSE显著更优。这些是文章判断设计方案成功与否的主要依据。
- Artifact: 在线劳动市场中的动态、多维、技能集特定的声誉系统/框架（HMM-W2V reputation framework） — 提出并使用三个组件：A. 技能分解到能力维度（word embedding/W2V）；B. 基于隐马尔可夫模型的动态能力特定质量评估；C. 聚合能力特定评估以生成任意技能集的声誉分数。
- Theory: Schmidt and Hunter (1983) human abilities normal-like distribution; Trust and reputation literature (Ba and Pavlou 2002; Pavlou and Gefen 2004) as background
- Theory-to-design: 不存在完整的前瞻性推导链。文中引用Schmidt-Hunter是在提出设计原则之后说明“人类能力呈正态分布，因而准确的技能集特定声誉可缓解声誉膨胀并促进区分”，更像是结果层面的解释，并未从该理论推导出具体设计特征（如W2V维数、HMM状态数或聚合公式）。信任/信息不对称理论仅解释为什么声誉系统重要，未指导HMM-W2V的组件设计。
- Decision: 基础筛选通过：文章以HMM-W2V声誉框架为明确软件制品，核心贡献是改进工人声誉排序、识别、分布和推荐效果的客观可计算指标，并进行了系统化对照验证。理论细筛不通过：文章主要依赖机器学习方法和领域问题驱动设计，心理学相关理论（Schmidt-Hunter正态能力分布、信任理论）未被用作前瞻性设计推导依据，缺少理论到具体设计选择的可追溯链条。
- Confidence: 0.72

## Finding a Needle in the Haystack: 
Recommending Online Communities on Social Media Platforms Using Network and Design Science

- Year/journal: 2021 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00694
- Metrics: Precision@k (k=1,5,10); Recall@k (k=1,5,10); F-score@k (k=1,5,10); Mean Reciprocal Rank (MRR); Discounted Cumulative Gain (DCG); Overall accuracy
- Objective evidence: 文章的核心贡献是设计并验证用于社区订阅推荐的特征，主要评价方式是推荐精度和排序质量。Table 7 和 Figure 8 报告了各特征组合的 Precision/Recall/F/MRR/DCG 结果，并声称 Network+General 在 top-1 最优、全特征组合在 top-5/top-10 最优，也优于多种 baseline，因此这些客观推荐指标构成了最终目标的验证依据。
- Artifact: 社区订阅推荐系统/推荐模型（Twitter lists recommender） — 设计并构建了社区订阅推荐模型，重点设计了三类输入特征：网络特征（structural hole assortativity、local clustering coefficient rank LCCR 等）、一般社区特征（list size、overlap），以及作为 baseline 的文本内容特征；同时提供特征提取算法，并用神经网络等模型生成推荐评分。
- Theory: Small-world networks (Watts & Strogatz); Structural holes / strength of weak connections (Burt); Random surfer model (Page et al.); Connectivity and centrality (Freeman, Borgatti); Preferential attachment (Capocci et al.)
- Theory-to-design: 不存在可追溯的“心理学理论→心理机制→具体软件设计→客观指标改善”链条。文章从网络科学概念（如 assortativity、LCC、PageRank）直接构造推荐特征 LCCR 和 structural hole assortativity，这是基于网络结构的图论/启发式设计，而不是从心理学理论向前推导出的设计选择。例如 LCCR 是 LCC、PageRank 和成员/订阅网络比较的组合，没有解释用户心理机制如何决定这一设计。
- Decision: 基础筛选通过：文章以 Precision、Recall、F-score、MRR、DCG 等可计算的推荐性能指标为最终目标，指标基于用户实际订阅行为而非主观感知；文章构建了社区订阅推荐系统/推荐模型，并以其作为解决方案进行评价。理论细筛不通过：文章使用的概念是网络科学/图论中的结构度量，不属于解释心理或行为机制的心理学相关理论，也没有形成从心理学理论到具体软件设计再到客观指标的可追溯指导链。
- Confidence: 0.7

## Novice digital service designers' decision-making with decision aids — A comparison of taxonomy and tags

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113367
- Metrics: selection accuracy
- Objective evidence: 选择准确率是研究模型中的任务绩效因变量，也是 H1、H3a、H3b、H4a、H4b 的核心被解释变量；文章通过分层回归、Kruskal-Wallis 和 Mann-Whitney U 检验显示分类法型决策辅助显著优于标签型和无辅助组，验证了改进。
- Artifact: 可交互的决策辅助界面/决策支持组件，基于 LimeSurvey 实现 — 三种决策辅助条件的信息呈现与交互方式：分类法型决策辅助（taxonomy-based decision aid）、标签型决策辅助（tags-based decision aid）、无分类的列表型决策辅助；参与者可点击对应设计技术查看详细信息。
- Theory: Cognitive fit theory (认知适配理论)
- Theory-to-design: 文章用认知适配理论提出了分类法型决策辅助比标签型更匹配选择任务、降低认知努力并提高选择准确率的假设，但并未说明该理论如何前瞻性地推导或约束决策辅助的实际设计内容（如分类层次的具体构建、标签生成规则、界面交互细节等）。理论主要服务于研究模型、变量选择（认知努力为中介、决策风格为调节）和假设预测，而不是用于确定某个软件制品的设计特征。因此，理论到具体设计选择的链条不完整，属于用理论预测已确定处理的效果，而非用理论指导制品设计。
- Decision: 基础筛选通过：文章以选择准确率这一客观计数指标为核心结果，并通过在 LimeSurvey 中构建可点击的分类法型、标签型和列表型决策辅助界面来比较其对选择准确率的影响，因此既满足客观指标核心贡献，也满足明确软件制品设计/改造。理论细筛不通过：认知适配理论主要用于提出假设、选择中介与调节变量和解释不同决策辅助的效果差异，并未前瞻性指导决策辅助的实际软件设计内容；理论指导的是研究模型和实验变量，而非软件制品本身的设计。
- Confidence: 0.7

## Antisocial online behavior detection using deep learning

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113362
- Metrics: Average Precision (Av. Prec.); AUC; F1-score
- Objective evidence: 文章的核心贡献是系统比较传统机器学习与深度学习、不同深度网络结构、注意力/池化、层级模型和预训练 transformer 在 AOB 检测上的分类性能，并以 Av. Prec、AUC、F1 作为最终判断依据。文中通过多个对照实验验证改进，例如 DL 多数情况优于 TML、psHAN 优于 HAN、BERT 在多个数据集上取得最优性能。
- Artifact: 用于在线平台内容审核的机器学习决策支持系统（AOB detection decision support system） — 该系统的分析核心组件：文本分类/检测模型，包括作者提出的 psHAN、HAN、BGRU、BERT/DistilBERT 等；以及作为系统最终阶段提出的 LIME 可解释性模块。
- Theory: 
- Theory-to-design: 
- Decision: 基础筛选通过：文章以 AOB 文本检测的 Av. Prec、AUC、F1 等客观分类性能作为核心贡献，并通过多个模型对照实验验证改进；所比较的模型和提出的 psHAN、LIME 模块被明确定位为内容审核决策支持系统的分析核心与可解释阶段。理论细筛不通过：文章没有使用心理学相关理论前瞻性指导模型或系统设计，只存在技术性注意力机制和常识性可解释性讨论。
- Confidence: 0.68

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

## Autoencoders for strategic decision support

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113422
- Metrics: outlier detection performance / top-k detection rate; dimension rank accuracy; direction accuracy
- Objective evidence: 文章将异常检测性能、维度级反馈和协同性作为验证AE解决方案的三个核心维度，并在贡献部分明确声称AE‘优于人类和其他基准模型’、‘提供细粒度维度级反馈’。客观指标是验证这些核心主张的主要证据，且与Iforest、LOF进行了比较。
- Artifact: 基于自编码器的战略决策支持系统（autoencoder-based strategic decision support system / DSS） — 自编码器神经网络作为该决策支持系统的核心分析组件，包括编码器-解码器结构、重构损失、异常评分排序，以及逐维度偏差反馈（偏差大小和方向）的输出。
- Theory: 启发式与偏差研究（Kahneman & Tversky; Gigerenzer & Gaissmaier）; 行为决策中的非理性偏差; 战略决策中的同行影响/最优独特性（optimal distinctiveness）
- Theory-to-design: 文章没有形成‘理论→心理机制→具体软件设计选择→客观指标’的完整可追溯链条。相关心理/行为文献主要用于论证人类专家做战略判断时存在不一致性和启发式局限，从而说明需要决策支持；但这些论述没有推导或约束具体的AE系统设计选择。例如，选择自编码器是因为其重构误差能提供维度级反馈，而不是由某个心理学理论推得的设计特征。
- Decision: 基础筛选通过：文章以异常检测性能、维度级反馈准确率等客观可复核指标作为核心贡献的验证依据，并将自编码器明确定位为战略决策支持系统的核心组件进行设计与评价。理论细筛不通过：文章引用的心理学/行为决策文献主要是为了说明人类判断缺陷和决策支持必要性，并未实质指导或推导自编码器系统的具体设计选择，因此不满足理论实质指导软件制品设计的要求。
- Confidence: 0.63
