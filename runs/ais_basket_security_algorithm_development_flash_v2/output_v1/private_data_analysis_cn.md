# 通过清单（99 篇）中 private 数据的逐篇分析

- 全量通过 99 篇：public 46、private 35、mixed 11、unclear 7
- 说明：mixed 表示公开与非公开混合（如公开网络+内部数据），unclear 表示全文无法判断。

## 一、private 35 篇的用途类别

1. 企业/组织内部专有数据（8 篇）：安全设备日志、单点登录日志、员工调查、公司案例数据。
2. 商业专有数据（协议限制）（3 篇）：商业家庭面板、医生处方、移动位置聚合数据、地下论坛采集。
3. 执法/机构内部数据（2 篇）：警方犯罪数据库、机构内部语料。
4. 实验室受控实验（4 篇）：参与者触摸/鼠标轨迹/皮电/现场实验数据。
5. 纯合成/仿真数据（约 15 篇）：作者自建仿真、随机生成、数值模拟，无真实数据。
6. 研究者爬取自建但非公开/协议受限（3 篇）：VirusTotal 学术许可、公司内部日志、项目合作数据。

## 二、逐篇明细（35 篇）

[01] Decision support for the optimal allocation of security controls（2018, Decision Support Systems）conf=0.98
- 数据：通过调查49名安全专业人员获取漏洞概率估计，并结合焦点小组确定的安全控制成本，属于私有的一次性调查数据。
- 用途：

[02] RADAR: A Framework for Developing Adversarially Robust Cyber Defense AI Agents with Deep Reinforcement Learning（2025, MIS Quarterly）conf=0.98
- 数据：VirusTotal学术许可获取的恶意软件样本、自行收集的Windows良性文件；数据非公开可获取。
- 用途：

[03] Bayesian Stackelberg games for cyber-security decision support（2021, Decision Support Systems）conf=0.98
- 数据：主要数据为作者随机生成的完整攻击图以及基于文献[34]和MITRE ATT&CK构造的校园网络案例，并非公开数据集。
- 用途：在随机生成完整攻击图和现实校园网络案例上实验，与DOBSS、HBGS、HUNTER等对比计算时间与安全风险。

[04] Harmonized authentication based on ThumbStroke dynamics on touch screen mobile phones（2016, Decision Support Systems）conf=0.98
- 数据：受控实验室实验收集的参与者触摸行为数据，非公开数据集。
- 用途：通过12名参与者的纵向受控实验，比较HATS与击键动力学方法，采用EER、准确率、输入时间等指标，并对比多种分类器（RF、NN、KNN、SVM等）。

[05] Cyber-risk decision models: To insure IT or not?（2013, Decision Support Systems）conf=0.98
- 数据：主要数据来自印度一所商学院内部 perimeter 安全设备日志数据，属于非公开渠道数据。
- 用途：使用印度某商学院两年期实际安全设备日志数据验证；输出漏洞评估表、预期损失、保费，并与风险中性/风险厌恶等不同风险画像比较。

[06] Reidentification Risk in Panel Data: Protecting for<i>k</i>-Anonymity（2023, Information Systems Research）conf=0.97
- 数据：主要数据来自IRI商业家庭面板数据和市场研究公司的医生处方数据，均为受协议限制的非公开商业数据。
- 用途：在IRI咸味零食面板数据（1009个家庭）和医生处方数据（448名医生）上实施，与聚类、记录删除、随机交换、噪声添加、聚合等基准比较，并评估品牌市场份额、SCR、品牌转换和层次贝叶斯品牌选择模型参数。

[07] INSIDER THREATS IN A FINANCIAL INSTITUTION: ANALYSIS OF ATTACK-PRONENESS OF INFORMATION SYSTEMS APPLICATIONS（2015, MIS Quarterly）conf=0.97
- 数据：某美国区域性金融机构的企业单点登录（ESSO）系统日志及内部应用特征数据，非公开。
- 用途：基于某金融机构7个月ESSO日志数据（40个应用），使用MCMC估计，并进行了鲁棒性检验，比较了两种风险测度下的模型估计结果。

[08] A maximum entropy approach to feature selection in knowledge-based authentication（2008, Decision Support Systems）conf=0.97
- 数据：实验使用MCMC方法生成的合成数据集，非公开来源。
- 用途：使用MCMC生成的合成KBA域和索赔人数据，与随机特征选择比较，评估了准确率、FAR、FRR、EER，自适应方法优于随机基线。

[09] Releasing Individually Identifiable Microdata with Privacy Protection Against Stochastic Threat: An Application to Health Information（2007, Information Systems Research）conf=0.95
- 数据：作者内部生成的1百万条记录、200个输入通道的合成模拟数据集，非公开渠道来源。
- 用途：在1百万条记录、200个输入通道的合成数据集上，变化风险比例和风险容忍度RT，使用CPLEX求解LP模型，比较数据效用损失（Ω）与风险容忍度、风险比例之间的关系；另通过改变输出通道数量分析效益递减。

[10] The Phishing Funnel Model: A Design Artifact to Predict User Susceptibility to Phishing Websites（2021, Information Systems Research）conf=0.95
- 数据：两个组织（金融和法务公司）内部的员工行为数据、企业端点安全日志和调查问卷数据，非公开渠道。
- 用途：在两个组织的12个月纵向现场实验（1,278名员工，49,373次交互）中与HITLSF、DRKM、AAM及SVM、SVOR等方法比较AUC，PFM显著领先；另有三个月干预现场实验评估效果。

[11] The Security of Confidential Numerical Data in Databases（2002, Information Systems Research）conf=0.95
- 数据：作者模拟生成的数据库（50,000条记录工资库及250,000条记录实验库），非公开渠道数据。
- 用途：使用模拟的50,000条记录工资数据库演示安全评估与推断控制机制选择，并用250,000条记录数据库测试计算性能；与Palley和Simonoff的R²方法及Tendick的线性组合R²进行了理论比较。

[12] A dynamic simulation approach to support the evaluation of cyber risks and security investments in SMEs（2021, Decision Support Systems）conf=0.95
- 数据：案例研究中的Snapshot Survey数据（Alpha和Beta公司）来自非公开调查，未公开提供。
- 用途：三个案例场景（Alpha/Beta公司在不同威胁环境下的模拟）比较，并用配对t检验验证结果差异。

[13] Estimating the impact of IT security incidents in digitized production environments（2019, Decision Support Systems）conf=0.95
- 数据：主要评估数据为随机生成的模拟DPE网络数据，以及一家德国制造企业的内部生产与IT网络案例数据（非公开）；模型参数多基于文献估计。
- 用途：实现为R/gRain软件原型，对随机生成的DPE网络进行敏感性分析，并在德国一家制造企业的真实生产网络案例中应用和验证。

[14] Secure federation of semantic information services（2013, Decision Support Systems）conf=0.95
- 数据：实验数据来自Aletheia项目合作伙伴的真实工业本体数据，并在作者控制的Amazon EC2实例上构建的实验数据集，不来自公开数据集或公开渠道。
- 用途：在Amazon EC2分布式环境上用真实工业本体数据（1000/10000/100000实例）进行了多组性能实验，比较了有无SemForce和TLS保护下的响应时间，并测试了并发请求；结果显示安全开销可接受。

[15] Identifying and Profiling Key Sellers in Cyber Carding Community: AZSecure Text Mining System（2016, Journal of Management Information Systems）conf=0.95
- 数据：8个匿名化的国际carding论坛数据，需反爬措施获取，论坛名称被隐去，数据不公开可复现。
- 用途：在8个地下经济论坛上，对线程分类、评论情感、卖家画像三个任务与SVM、NB、kNN、N-gram等基准方法比较，平均F-measure约80%-90%，并以Rescator案例验证。

[16] Software Diversity for Improved Network Security: Optimal Distribution of Software-Based Shared Vulnerabilities（2017, Information Systems Research）conf=0.95
- 数据：主要数据为生成的scale-free网络（Barabási-Albert模型）和合成的软件-漏洞矩阵，无公开数据集，全部由研究构建。
- 用途：在合成scale-free网络上，通过CPLEX求解LP模型，并与targeted distribution策略比较SDI和epidemic threshold，基于20次重复模拟评估。

[17] "Brute-Force Sentence Pattern Extortion from Harmful Messages for Cyberbullying Detection"（2019, Journal of the Association for Information Systems）conf=0.95
- 数据：数据来自日本三重县人权研究所提供并由网络巡逻志愿者标注的非公开网络欺凌语料，非公开数据集。
- 用途：在1,490条有害和1,508条非有害日文网络欺凌数据上进行10折交叉验证，并与SVM、SO-PMI-IR等多种基线方法比较，最优F值达0.803；同时开发Android应用进行初步测试。

[18] Towards controlling virus propagation in information systems with point-to-group information sharing（2009, Decision Support Systems）conf=0.95
- 数据：数值仿真使用作者自设的模型参数（如 N=100000、μ=1/4380、r=30 等），非公开真实数据集或公开渠道数据。
- 用途：通过自设参数的数值仿真（ODE 系统模拟）验证病毒无病/流行病平衡点、短期爆发临界点及 C_S-控制/多阶段 C_S-控制的效果，并与无控制及 C_L-控制进行对比。

[19] Personalized Privacy Preservation in Consumer Mobile Trajectories（2024, Information Systems Research）conf=0.93
- 数据：与领先数据聚合商合作的专有移动位置数据（40,012消费者、940,000个位置记录），非公开渠道获取。
- 用途：基于40,000消费者一百万条真实移动轨迹，与LSUP、GSUP、PPMTF、LSTM-TrajGAN等10种基线方法比较，评估风险降低与效用保持

[20] Decision support for Cybersecurity risk planning（2011, Decision Support Systems）conf=0.92
- 数据：主要数据来自Verizon Business内部/客户调查数据，且约定不披露企业名称和识别信息，属于非公开渠道数据。
- 用途：使用Verizon Business收集的制造业企业调查数据，运行GA 15次迭代，将企业风险从1775K降至324K，总风险与成本从2216.8K降至891.8K。

[21] Complex Problem Solving: Identity Matching Based on Social Contextual Information（2007, Journal of the Association for Information Systems）conf=0.92
- 数据：Tucson Police Department提供的Meth World执法数据库（非公开警方数据）。
- 用途：基于Tucson警方Meth World真实毒品犯罪数据，采用10折交叉验证比较仅个人特征与加入社会特征时的precision/recall/F-measure，并绘制ROC曲线。

[22] Network externalities, layered protection and IT security risk management（2007, Decision Support Systems）conf=0.92
- 数据：未使用真实数据，全部为人为设定的仿真参数（如系统数、攻击数、初始脆弱性等），属于非公开模拟数据
- 用途：使用Matlab v6.5进行数值仿真，基于假设参数（如200个系统、100,000次攻击）比较不同情形下的安全投资、风险和风险降低，但未使用真实数据

[23] Managing user relationships in hierarchies for information system security（2007, Decision Support Systems）conf=0.92
- 数据：主要数据来自作者自行设计的仿真实验生成，非公开渠道获取。
- 用途：通过Visual Basic仿真实验（改变矩阵密度与Pmax）测度系统容量，并与多种KTK/SKL方法在初始化、计算、增删、存储等六准则上进行比较

[24] The “Most Popular News” Recommender: Count Amplification and Manipulation Resistance（2014, Information Systems Research）conf=0.92
- 数据：主要数据来自DailyMe Inc.提供的五个本地新闻网站的非公开文章点击数据。
- 用途：基于五个本地新闻网站真实数据驱动的仿真实验，与Top-N推荐和改编的Influence Limiter启发式进行比较，使用M1、M2、MAE和KL距离等指标。

[25] A social referral appraising mechanism for the e-marketplace（2017, Information & Management）conf=0.9
- 数据：通过雪球抽样邀请Facebook用户并获授权收集其社交互动（墙贴）和Yahoo! Auction购买历史，属于需授权才能获取的非公开个人数据
- 用途：收集Facebook社交互动和Yahoo! Auction购买记录（187名参与者，730条交易记录，145个卖家），通过准确率、MAE、precision/recall/F1与EO、CF、Public等基准方法对比评估

[26] Understanding the Value of Countermeasure Portfolios in Information Systems Security（2008, Journal of Management Information Systems）conf=0.9
- 数据：使用合成的参数化模拟数据，非公开真实数据集。
- 用途：通过在合成数据上进行的三个模拟实验（ANOVA分析、不同威胁情景与组合效果比较），评估了模型与投资组合价值。

[27] How can online marketplaces reduce rating manipulation? A new approach on dynamic aggregation of online ratings（2017, Decision Support Systems）conf=0.9
- 数据：全文未使用真实数据集，主要数据为模拟仿真生成的评分序列，非公开渠道数据。
- 用途：通过仿真实验（1200轮、多种初始评分分布、不同虚假评分水平）与即时更新、时间折扣、单值聚合、三值聚合等方法比较，并进行了多项稳健性检验。

[28] Matching information security vulnerabilities to organizational security profiles: a genetic algorithm approach（2006, Decision Support Systems）conf=0.88
- 数据：实验使用25个随机生成的漏洞场景及随机权重，无公开真实数据；漏洞与安全技术分类表基于RAND报告。
- 用途：25个随机漏洞场景下与枚举（Brute Force）方法比较，报告适应度、误差和执行时间；并分析不同问题规模与种群大小下的准确性与可扩展性。

[29] Distributed decision support systems under limited degrees of competence: A simulation study（1997, Decision Support Systems）conf=0.87
- 数据：主要数据来自作者自建的CLUE仿真测试台生成的模拟数据，非公开渠道。
- 用途：在基于MICE的CLUE模拟测试台上进行了约700小时的模拟实验，变化节点能力与真诚度分布，评估收敛性、正确性和可靠性估计。

[30] Constructing a reliable Web graph with information on browsing behavior（2012, Decision Support Systems）conf=0.85
- 数据：主要数据来自某中国搜索引擎公司内部工具栏Web访问日志、内部爬虫抓取的原Web图以及微博内部采集数据，均非公开渠道。
- 用途：在大规模搜索引擎工具栏点击日志（28亿次点击事件）构建的图上，与PageRank、TrustRank、DiffusionRank、BrowseRank进行ROC/AUC和成对有序性比较；并在微博社交图上评估userPageRank/userTrustRank。

[31] Secure attribute sharing of linked microdata（2016, Decision Support Systems）conf=0.85
- 数据：实验数据为作者模拟生成（synthetic data），并非来自公开渠道。
- 用途：使用仿真数据（n=100/1000/5000，1000次重复）评估 SASH 与 data swapping（10%/25%/50%）在分析有效性（相关系数保持）和披露风险（R²）上的表现，并展示散点图验证非线性关系保持。

[32] An Information Systems Security Risk Assessment Model Under the Dempster-Shafer Theory of Belief Functions（2006, Journal of Management Information Systems）conf=0.85
- 数据：主要数据来自审计公司提供的WebTrust保证业务内部工作底稿，具有保密限制；另有假设的数值示例。
- 用途：利用假设的硬件安全例子和真实WebTrust保证业务案例，通过Auditor's Assistant软件进行证据传播计算，并对逻辑关系、证据位置和证据强度进行了敏感性分析。

[33] An entropy approach to disclosure risk assessment: Lessons from real applications and simulated domains（2011, Decision Support Systems）conf=0.85
- 数据：核心评估数据为合成模拟数据；辅助案例分析使用伊利诺伊州公开医院出院数据库和Homenet项目非公开数据。
- 用途：在模拟环境（均匀与Zipf分布，完全指定/不完全指定系统）及真实案例（伊利诺伊州出院数据库、Homenet数据）中比较熵得分与实测披露率，并用形状分数σ评估曲线匹配。

[34] Sleight of Hand: Identifying Concealed Information by Monitoring Mouse-Cursor Movements（2019, Journal of the Association for Information Systems）conf=0.82
- 数据：作者实验室招募75名大学生完成模拟盗窃与筛查问卷所采集的鼠标轨迹、皮电及视频数据，非公开。
- 用途：受控实验66名有效被试，同时采集鼠标轨迹与皮电活动，与基线和真实组比较；鼠标模型平均准确率78.3%、假阳性率21.7%，并与皮电模型对比。

[35] Filtering trust opinions through reinforcement learning（2014, Decision Support Systems）conf=0.8
- 数据：数据来自作者自建仿真测试床生成，未使用公开数据集，也未提及公开代码或数据发布。
- 用途：在包含1000个服务提供者、100个见证人和100个服务消费者的自建仿真测试床中，与W2010、Y2003、B2002等方法比较NAUL和Collusion Power，ACT平均改善约20%-25%。

## 三、对「必须使用公开数据」要求的含义

- 99 篇中可直接满足公开数据要求的只有 46 篇 public（另有部分 mixed 的暗网/论坛爬取数据可公开复现，如 ADREL、暗网威胁识别）。
- private 35 篇中有约 15 篇为纯合成仿真：它们没有数据可得性问题，但也没有可供他人复用的真实数据集。
- 值得注意：RADAR（MISQ 2025）本身也被标记 private（VirusTotal 学术许可+自采良性文件），即我们参考的锚点文章并不满足「公开数据」要求；而 ADREL（MISQ 2022，GitHub 公开）与暗网威胁识别（JMIS 2020，GitHub 公开）满足。
- 安全领域可公开获取的数据类型（从 public 46 篇归纳）：公开基准数据集（DARPA/KDDCUP99、PhishTank、OpenPhish、Alexa、Yelp、Amazon、Book-Crossing、i2b2、FIMI、UCI）、公开可爬平台（Twitter、Google Play、TripAdvisor、暗网论坛）、公开报告（Ponemon、BSI、NVD/CVE）。
