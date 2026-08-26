# 已通过清单（strict_include=true，截至审查时刻）

- 已判定：1445 篇；通过：31 篇（2.15%）
- security_pass=70 algorithm_pass=263

## [1] Semi-Supervised Cyber Threat Identification in Dark Net Markets: A Transductive and Deep Learning Approach
- 年份/期刊: 2020 / Journal of Management Information Systems | DOI: 10.1080/07421222.2020.1790186 | 置信度: 1 | record: 712
- 安全: core_security_attack_defense | 研究核心是在暗网市场中识别与检测恶意网络威胁产品（如勒索软件、黑客工具、被泄露账户），威胁对象是系统与用户安全，且属于威胁检测与防御范畴。
- 算法: novel_algorithm_with_evaluation | 方法: 基于转导学习（TSVM）和深度双向LSTM的半监督威胁识别方法
- 评估: 在包含79,434条产品列表的暗网市场数据集上，与SVM、LSTM、CNN等基准方法比较，F1达到89.55%，显著优于基线。
- 数据公开性: public | 数据来自九个公开暗网市场的网络爬取，作者在GitHub上公开了数据集（https://github.com/mohammadrezaebrahimi/JMIS-DarkNetMarketData）。
- 综合判定: 文章核心是针对暗网市场上恶意网络威胁产品的自动识别与检测，属于典型的安全攻防与威胁检测领域；同时提出并实证评估了新的半监督学习算法（TSVM启发式标注）与深度LSTM架构，方法实现且评估完整；数据集公开在GitHub。故安全相关性与算法开发均通过。

## [2] The Impact of Fake Reviews on Online Visibility: A Vulnerability Assessment of the Hotel Industry
- 年份/期刊: 2016 / Information Systems Research | DOI: 10.1287/isre.2016.0674 | 置信度: 0.99 | record: 606
- 安全: core_security_attack_defense | 全文围绕恶意主体通过注入虚假评论操纵在线可见性的攻击策略、脆弱性评估及防御响应，属于内容操纵与对抗攻击领域，而非纯金融欺诈。
- 算法: novel_algorithm_with_evaluation | 方法: 可见性形式化度量与虚假评论攻击注入模拟框架（含可见性量化模型、三种考虑模型、三种攻击策略及DelayIndex排序函数）
- 评估: 基于TripAdvisor 230万条评论、17城市4,709家酒店，比较平均评分与PopularityIndex排序函数及多种考虑模型下的攻击成功率，并验证DelayIndex抗操纵性能。
- 数据公开性: public | 主要数据来自TripAdvisor.com公开可爬取的酒店评论（2,305,610条）及少量Yelp.com公开评论，均属公开网络数据。
- 综合判定: 全文明确研究恶意行为者利用虚假评论攻击酒店在线可见性的脆弱性，并提出和实证评估了攻击模拟、可见性计算和抗操纵排序等方法；数据来自公开评论平台，故严格纳入。

## [3] Protecting Privacy When Sharing and Releasing Data   with Multiple Records per Person
- 年份/期刊: 2020 / Journal of the Association for Information Systems | DOI: 10.17705/1jais.00643 | 置信度: 0.98 | record: 2834
- 安全: core_security_attack_defense | 文章聚焦数据发布中的隐私披露风险，明确假设对抗者（adversary）利用准标识符重识别个体或推断敏感属性，并开发匿名化方法进行防御，属于安全攻防检测与缓解。
- 算法: novel_algorithm_with_evaluation | 方法: 基于g-balance和h-affiliation度量的递归kd-tree匿名化算法
- 评估: 在INFORMS患者数据、MovieLens电影评分数据、PKDD银行交易数据三个真实数据集上，与k-anonymity、PID-based K-anonymity、l-diversity对比披露风险和信息损失（Max/AvgGIDR、GSAR、ANE指标）。
- 数据公开性: public | 三个主要数据源均为公开数据集：INFORMS Data Mining Contest 2008医疗数据、MovieLens公开电影评分数据、PKDD'99 Discovery Challenge银行数据。
- 综合判定: 文章研究数据共享与发布中的隐私披露攻击（重识别和敏感属性推断），提出新的隐私度量与匿名化算法，并在三个公开真实数据集上实证评估，严格符合安全攻防和新算法开发两个纳入条件。

## [4] PhishWHO: Phishing webpage detection via identity keywords extraction and target domain name finder
- 年份/期刊: 2016 / Decision Support Systems | DOI: 10.1016/j.dss.2016.05.005 | 置信度: 0.98 | record: 386
- 安全: core_security_attack_defense | 文章聚焦钓鱼网页攻击，存在恶意行为者（钓鱼者），损害用户凭证与系统安全，核心为检测与防御。
- 算法: novel_algorithm_with_evaluation | 方法: PhishWHO：基于身份关键词提取与目标域名查找的钓鱼网页检测系统（加权URL令牌系统、N-gram模型、3层身份匹配）
- 评估: 使用PhishTank和OpenPhish的5000个钓鱼网页与Alexa前一百万中的5000个合法网页进行实验，与CANTINA、Ramesh等、Huh&Kim等方法比较，MCC最高达0.9244。
- 数据公开性: public | 钓鱼URL来自PhishTank和OpenPhish，合法URL来自Alexa顶级列表，均为公开渠道。
- 综合判定: 本文属于安全领域核心攻防研究，明确提出钓鱼攻击及检测系统；算法开发方面提出新的检测方法并完成实证评估，数据来自公开来源。

## [5] A novel risk assessment and optimisation model for a multi-objective network security countermeasure selection problem
- 年份/期刊: 2012 / Decision Support Systems | DOI: 10.1016/j.dss.2012.04.001 | 置信度: 0.97 | record: 2584
- 安全: core_security_attack_defense | 论文针对网络系统面临恶意威胁（如黑客攻击、DoS、入侵）时的安全风险评估与安全对策选择，核心是降低安全风险和保护系统CIA，属于安全攻防与防御决策。
- 算法: novel_algorithm_with_evaluation | 方法: 多目标Tabu Search (MOTS)算法及RAOM风险评估优化模型
- 评估: 使用10个漏洞、15个威胁、24个安全对策的示例数据集，将MOTS与穷举搜索(ES)对比，通过Pareto前沿、欧氏距离、运行时间等评估MOTS求解质量与速度。
- 数据公开性: public | 漏洞、威胁、对策匹配等数据基于NVD、CVE等公开漏洞库及公开成本信息（如厂商网站），示例数据可公开获取。
- 综合判定: 论文核心是安全风险评估与安全对策选择，存在恶意威胁（威胁列表含黑客、DoS、入侵等），损害对象是系统安全（CIA）；同时论文提出并实现新的多目标Tabu Search算法，并通过与穷举搜索的对比实验进行实证评估，因此严格纳入。

## [6] Factor-analysis based anomaly detection and clustering
- 年份/期刊: 2006 / Decision Support Systems | DOI: 10.1016/j.dss.2005.01.005 | 置信度: 0.97 | record: 1118
- 安全: core_security_attack_defense | 论文研究的是网络入侵检测，针对恶意攻击者的攻击行为进行异常检测和攻击聚类，属于系统与网络安全防护领域。
- 算法: novel_algorithm_with_evaluation | 方法: 基于因子分析与马氏距离的异常检测与攻击聚类算法
- 评估: 使用1998/1999 DARPA入侵检测评估数据（tcpdump），通过检测率、漏报率和误报率评估，并与ADAM系统进行了简要比较。
- 数据公开性: public | 主要使用DARPA Intrusion Detection Evaluation Data（1998和1999公开基准数据集）中的tcpdump数据。
- 综合判定: 文章属于网络安全入侵检测领域，研究核心是检测和防御恶意攻击；提出并实现了一种新的因子分析+马氏距离的异常检测与聚类算法，并用DARPA公开数据集进行了实证评估。两模块均通过，数据公开。

## [7] Cross-Lingual Cybersecurity Analytics in the International Dark Web with Adversarial Deep Representation Learning
- 年份/期刊: 2022 / MIS Quarterly | DOI: 10.25300/misq/2022/16618 | 置信度: 0.97 | record: 2006
- 安全: core_security_attack_defense | 论文核心是检测暗网平台上的黑客资产（恶意软件、黑客工具、教程等），以支持网络安全态势感知，属于针对威胁的检测与防御
- 算法: novel_algorithm_with_evaluation | 方法: ADREL（对抗深度表示学习），集成在CLHAD框架中
- 评估: 在自建的多语言暗网标注数据集（英/俄/法/意共5976条）上与词典基线、单语模型、机器翻译方法及跨语言迁移方法比较，使用准确率、F1和AUC并进行五折交叉验证
- 数据公开性: public | 主要数据来自作者自行爬取的14个暗网平台（黑客论坛和暗网市场），这些平台可通过Tor公开访问；标注后的gold-standard数据集在GitHub上公开
- 综合判定: 安全相关性：暗网黑客资产检测属于网络安全攻防核心任务，恶意行为者（黑客）是研究问题核心，目标是缓解系统、用户和组织面临的攻击威胁，且并非纯金融欺诈；算法开发：论文核心是提出新算法ADREL（对抗深度表示学习），实现并公开代码，并有跨语言暗网数据上的实证评估；数据公开性：主要数据来自公开可访问的暗网平台，且标注子集公开在GitHub，故记为public。

## [8] Short Term and Total Life Impact analysis of email worms in computer systems
- 年份/期刊: 2007 / Decision Support Systems | DOI: 10.1016/j.dss.2006.12.014 | 置信度: 0.95 | record: 22
- 安全: core_security_attack_defense | 研究邮件蠕虫的破坏性影响分类与早期预测，属于恶意代码攻击的检测与缓解，安全损害对象为系统可用性、数据完整性与组织安全。
- 算法: novel_algorithm_with_evaluation | 方法: 邮件蠕虫影响分类预测框架（Total Life Impact与Short Term Impact，含Tskewness、LMH、Hit density等指标）
- 评估: 使用Symantec与Messagelabs的93个邮件蠕虫数据，比较STI与TLI框架的匹配率（三维约59.2%）并用GSI验证，呈现周/月趋势。
- 数据公开性: public | Symantec和Messagelabs公开网站上2003年至2004年的邮件蠕虫记录。
- 综合判定: 该文以邮件蠕虫恶意代码为对象，提出新的影响分类与早期预测框架，核心是安全威胁的检测与缓解；框架被实现并进行93个真实蠕虫数据的实证评估；数据来自公开渠道，故纳入。

## [9] Capturing the essence of word-of-mouth for social commerce: Assessing the quality of online e-commerce reviews by a semi-supervised approach
- 年份/期刊: 2013 / Decision Support Systems | DOI: 10.1016/j.dss.2013.06.002 | 置信度: 0.95 | record: 2492
- 安全: core_security_attack_defense | 文章针对在线评论系统中的垃圾/恶意评论（review spam）进行检测与分类，识别误导消费者的恶意或低质量评论，属于安全攻防中的内容操纵检测与缓解。
- 算法: novel_algorithm_with_evaluation | 方法: ORQM（Online Review Quality Mining），基于ICA预处理的Co-EM集成学习半监督分类方法
- 评估: 在Amazon.com四个产品类别数据集（mProducts、Music、Books、DVD/VHS）上进行10折交叉验证，与Random Forest、SVM、Logistic回归、Co-EM SVM、Co-training、Co-EM Bayesian、KNN等基线比较，使用ACC、F-score、AUC、APR、RMS、MXE、Mean七个指标。
- 数据公开性: public | Amazon.com公开评论数据集（2006年6月发布，含5.8 million reviews，覆盖Music、Books、DVD/VHS和mProducts四类产品）。
- 综合判定: 安全相关性通过：文章明确将垃圾评论（review spam）定义为恶意行为者通过恶意评价损害产品声誉或误导消费者，并将垃圾/低质量评论检测作为评论质量分类的重要目标，属于内容操纵检测。算法开发通过：提出并实现了ORQM（ICA预处理+Co-EM集成学习）新方法，并在Amazon公开数据集上进行了多基线实证评估，方法为核心贡献。数据为公开数据。因此严格纳入。

## [10] A Decision Support System for predictive police patrolling
- 年份/期刊: 2015 / Decision Support Systems | DOI: 10.1016/j.dss.2015.04.012 | 置信度: 0.95 | record: 2132
- 安全: core_security_attack_defense | 文章围绕犯罪预测与警力优化部署，旨在预防和减少盗窃等犯罪行为，核心是评估和缓解由罪犯构成的公共安全威胁，属于安全攻防领域。
- 算法: novel_algorithm_with_evaluation | 方法: P3-DSS预测警务决策支持系统（含DPPU时空预处理、CRFU指数平滑预测、PSOU的MC-PDP优化、operational envelope算法）
- 评估: 使用马德里中央区2008-2012年105,755起盗窃记录，与naive baseline及SNPC现有配置对比，通过MSE、统计检验和效率损失量化评估。
- 数据公开性: private_or_nonpublic | 西班牙国家警察部队（SNPC）内部犯罪报告数据库，未公开。
- 综合判定: 安全上，文章针对犯罪威胁进行预测和防御优化，是核心安全攻防任务；算法上，提出了新的数据预处理、预测、优化方法并实现和实证评估；数据来自警方内部未公开数据库。

## [11] Extracting and reasoning about implicit behavioral evidences for detecting fraudulent online transactions in e-Commerce
- 年份/期刊: 2016 / Decision Support Systems | DOI: 10.1016/j.dss.2016.04.003 | 置信度: 0.95 | record: 2032
- 安全: core_security_attack_defense | 文章聚焦检测电子商务中由攻击机构组织、合谋买家参与的串通欺诈交易攻击，属于恶意行为者对系统与用户的操纵与滥用，核心是威胁检测与防御。
- 算法: novel_algorithm_with_evaluation | 方法: DSRC（Dempster-Shafer Reinforced Combination）欺诈交易检测框架，包含证据阈值估计算法（Algorithm 1）、层次化证据融合算法（Algorithm 2）和基于遗传算法的参数搜索机制
- 评估: 基于淘宝蜜罐店铺采集的真实交易与行为数据（8885笔交易），与Dong、Suvasini、DS(e)等基线系统比较，交易检测达到TPR 83%、FPR 2.4%，并通过配对t检验验证显著提升。
- 数据公开性: private_or_nonpublic | 通过蜜罐方法在淘宝自建店铺采集的交易与行为数据，数据经攻击机构发起欺诈交易得到，非公开数据集。
- 综合判定: 安全上：存在明确恶意行为者（攻击机构、合谋买家）对电子商务系统进行串通欺诈攻击，损害系统完整性与用户信任，核心是检测与防御；算法上：提出并实现了新的DSRC证据融合框架及配套算法，并进行了真实数据实证评估；数据为蜜罐实验采集，非公开。故纳入。

## [12] Impact of Network Structure on Malware Propagation: A Growth Curve Perspective
- 年份/期刊: 2016 / Journal of Management Information Systems | DOI: 10.1080/07421222.2016.1172440 | 置信度: 0.95 | record: 1744
- 安全: core_security_attack_defense | 研究恶意软件（malware）在组织网络中的传播过程，并基于网络结构提出防御策略（免疫、对策传播、安全意识），核心是攻击传播的建模与防御。
- 算法: novel_algorithm_with_evaluation | 方法: 结构风险模型（基于四参数广义逻辑增长曲线和网络结构度量）
- 评估: 基于MySpace社会网络与组织技术网络数据，进行20万次SIR/病毒传播模拟，用层次回归评估模型，并模拟三种防御策略进行比较。
- 数据公开性: mixed | MySpace公开用户网络数据与组织内部技术网络结构数据，以及基于它们生成的模拟数据。
- 综合判定: 恶意软件传播是典型安全威胁，文章核心目标是理解传播机制并评估防御策略；同时提出了新的结构风险模型并进行了基于真实网络和仿真的实证评估，满足安全和算法开发双重标准。数据来源包括公开的MySpace数据和私有的组织技术网络数据。

## [13] A Rigidity Detection System for Automated Credibility Assessment
- 年份/期刊: 2014 / Journal of Management Information Systems | DOI: 10.2753/mis0742-1222310108 | 置信度: 0.95 | record: 1694
- 安全: core_security_attack_defense | 文章开发自动化刚性检测系统，用于安全筛查中识别隐藏信息（如携带爆炸物）和欺骗，属于安全威胁检测与防御。
- 算法: novel_algorithm_with_evaluation | 方法: 自动化刚性检测系统（基于计算机视觉的Kinesic Rigidity检测）
- 评估: 两个实验：实验1为mock crime CIT，实验2为安全筛查情境，使用多级回归模型比较有罪与无罪组在目标项上的运动减少量。
- 数据公开性: private_or_nonpublic | 两个实验的参与者视频和运动数据，不公开。
- 综合判定: 文章核心为安全筛查中的欺骗检测，存在恶意行为者（携带违禁品者），并开发了自动化刚性检测的新方法，通过两个实验实证评估，数据和代码均非公开。

## [14] Combining Crowd and Machine Intelligence to Detect False News on Social Media
- 年份/期刊: 2022 / MIS Quarterly | DOI: 10.25300/misq/2022/16526 | 置信度: 0.95 | record: 2826
- 安全: core_security_attack_defense | 文章核心是检测社交媒体上的虚假新闻，明确提及恶意用户账户（社交机器人、trolls）对响应和报告的操纵，属于内容操纵与虚假信息检测的安全攻防任务。
- 算法: novel_algorithm_with_evaluation | 方法: CAND框架与CLNAM贝叶斯聚合模型
- 评估: 在Weibo和Twitter两个真实数据集上与SVM、CNN、LSTM、Bi-LSTM、BERT、Concat、HSA、MV、BAM等多个基准方法比较，报告PR AUC、F1、召回率、精确率等指标
- 数据公开性: public | 新浪微博公开数据（官方事实核查公告及真实帖子）和Twitter公开数据集（Ma et al., 2016; Ma et al., 2017），报告数据部分为模拟但主要数据均来自公开渠道。
- 综合判定: 文章研究虚假新闻检测这一内容操纵威胁，明确涉及恶意行为者（虚假信息制造者、社交机器人和trolls）及其对系统、用户和组织的安全损害，属于核心安全攻防检测；同时提出了新的计算方法CAND/CLNAM，并进行了多数据集、多基准的实证评估，算法开发贡献显著；主要数据来自公开社交平台。

## [15] Software Diversity for Improved Network Security: Optimal Distribution of Software-Based Shared Vulnerabilities
- 年份/期刊: 2017 / Information Systems Research | DOI: 10.1287/isre.2017.0722 | 置信度: 0.95 | record: 3040
- 安全: core_security_attack_defense | 文章核心针对病毒/蠕虫等恶意软件在网络中的传播，提出软件多样性策略以提升网络对攻击的韧性（提高流行病阈值），属于安全攻防与缓解。
- 算法: novel_algorithm_with_evaluation | 方法: 软件多样性最优分配LP模型（LP1/LP2）、软件多样性指数（SDI）、扩展SIS病毒传播模型及动态软件分配算法（Algorithm 1-3）
- 评估: 在生成的无标度网络（1,000-5,000节点，1/2连接，低/高网络度中心性，软件相似度5%/40%）上进行仿真实验，以SDI和流行病阈值为指标与目标分布策略比较。
- 数据公开性: private_or_nonpublic | 实验数据为作者生成的合成无标度网络和软件-漏洞矩阵，非公开渠道数据。
- 综合判定: 安全相关性明确：针对病毒/蠕虫攻击的防御与缓解，恶意行为者为核心。算法开发明确：提出新的LP优化模型、SDI度量、扩展SIS模拟及动态分配算法，并实现和实证评估。数据为合成模拟，属于非公开渠道，但仅记录不影响纳入。

## [16] Enhancing border security: Mutual information analysis to identify suspect vehicles
- 年份/期刊: 2007 / Decision Support Systems | DOI: 10.1016/j.dss.2006.09.007 | 置信度: 0.95 | record: 1710
- 安全: core_security_attack_defense | 文章聚焦于利用互信息识别可能参与毒品走私等犯罪活动的可疑车辆，以增强边境安全，核心是检测和防御跨境犯罪威胁。
- 算法: novel_algorithm_with_evaluation | 方法: 改进的互信息方法（时间启发式MIT、港口启发式MIP）
- 评估: 在Tucson地区警方数据和约1100万条CBP边境过境记录上，比较MIT、MIP与经典MIC在识别有警方接触记录的潜在可疑车辆上的性能，采用t检验和领域专家案例评估。
- 数据公开性: private_or_nonpublic | Tucson警察局、Pima县警长等警方执法记录和CBP边境过境数据，通过BorderSafe项目合作提供，非公开渠道获取。
- 综合判定: 安全相关性满足：存在明确的恶意行为者（走私/贩毒车辆），损害范围是边境安全，核心是威胁检测与防御；算法开发满足：提出了改进的互信息方法（MIT/MIP）并实现和实证评估；数据来自非公开执法数据，不影响纳入。

## [17] Releasing Individually Identifiable Microdata with Privacy Protection Against Stochastic Threat: An Application to Health Information
- 年份/期刊: 2007 / Information Systems Research | DOI: 10.1287/isre.1070.0112 | 置信度: 0.95 | record: 1034
- 安全: core_security_attack_defense | 论文针对数据发布中的机密性威胁（用户利用统计信息推断被抑制的机密医疗诊断），提出防御性数据重编码方法以保护数据主体隐私，属于安全攻防中的隐私保护与数据发布安全。
- 算法: novel_algorithm_with_evaluation | 方法: 通道扩展重编码方法（基于线性规划的IIM安全发布优化模型）
- 评估: 基于100万条合成记录（200个输入通道）在不同风险比例和风险容忍度下进行LP求解，使用CPLEX比较不同输出通道数量的信息损失并分析R-U权衡。
- 数据公开性: private_or_nonpublic | 主要数据为作者生成的合成数据（模拟100万条个体记录，含200个输入通道），非公开渠道可获取。
- 综合判定: 安全相关：文章针对数据发布中的机密性威胁（用户利用统计信息推断被抑制的机密医疗诊断），提出防御性数据重编码方法，属于安全攻防中的隐私保护与数据发布安全。算法开发：提出并实现了基于线性规划的通道扩展重编码新方法，并通过大规模合成数据实验实证评估其性能。数据公开性：主要数据为作者生成的合成数据，非公开渠道可获取，不影响纳入判定。故strict_include为true。

## [18] Autonomous Scientifically Controlled Screening Systems for Detecting Information Purposely Concealed by Individuals
- 年份/期刊: 2014 / Journal of Management Information Systems | DOI: 10.1080/07421222.2014.995535 | 置信度: 0.95 | record: 992
- 安全: core_security_attack_defense | 文章核心是检测个人故意隐藏的安全相关信息（如简易爆炸装置走私），面向物理安全筛查、内部威胁等安全防御场景，属于安全攻防检测领域。
- 算法: novel_algorithm_with_evaluation | 方法: 自主科学控制筛查系统（ASCSS）及其自动化筛查亭（ASK），包含基于眼动定向和防御行为的分类算法
- 评估: 172名大学生参与实验，构建并试图走私模拟IED，通过实验室实验收集眼动数据，使用多水平回归和ROC分析评估检测准确率（AUC 0.69-0.70）。
- 数据公开性: private_or_nonpublic | 主要数据来自作者在实验室进行的受控实验（172名大学生），眼动数据等为实验采集，属于非公开专有数据。
- 综合判定: 安全相关性通过：全文围绕检测故意隐藏的安全威胁（如爆炸物），有明确恶意行为者，面向安全防御的检测；算法开发通过：提出了新的ASCSS系统及ASK实现，包含新的眼动防御测量和分类算法，并进行了受控实验实证评估；数据公开性为私密实验数据。

## [19] Integrating relations and criminal background to identifying key individuals in crime networks
- 年份/期刊: 2020 / Decision Support Systems | DOI: 10.1016/j.dss.2020.113405 | 置信度: 0.95 | record: 456
- 安全: core_security_attack_defense | 研究针对犯罪集团和恐怖组织中的关键嫌疑人识别，恶意行为者（罪犯/恐怖分子）是研究核心，损害对象为公共安全与犯罪调查，属于安全攻防与威胁检测。
- 算法: novel_algorithm_with_evaluation | 方法: 社会网络犯罪嫌疑人评估器（SNCSE）
- 评估: 在智利检察官办公室入室盗窃嫌疑网络和希腊恐怖组织11月17日网络两个真实数据集上，与度中心性、介数中心性、PageRank、HITS等基线比较，使用性能度量和FPR/FNR评估。
- 数据公开性: mixed | 第一个应用使用智利检察官办公室提供的专有犯罪数据（非公开），第二个应用使用希腊恐怖组织11月17日的公开数据（基于已有研究整理）。
- 综合判定: 文章核心是提出并实证评估一种融合犯罪倾向与网络结构的新型节点评估器，用于犯罪网络和恐怖组织中的关键嫌疑人识别，属于安全领域的威胁检测与防御；同时满足新方法开发和实证评估条件。数据公开性为混合，不影响纳入。

## [20] Robustness of Multiple Indicators in Automated Screening Systems for Deception Detection
- 年份/期刊: 2015 / Journal of Management Information Systems | DOI: 10.1080/07421222.2015.1138569 | 置信度: 0.95 | record: 800
- 安全: core_security_attack_defense | 文章核心是检测欺骗者（恶意行为者）以挫败安全筛查系统，属于安全威胁的检测与防御。
- 算法: novel_algorithm_with_evaluation | 方法: 多指标自动化欺骗检测系统（含朴素贝叶斯、逻辑回归、随机森林、SVM及集成分类器）
- 评估: 175人实验室实验，比较五种条件（无辜、有罪、心理/身体/多重反制），使用留出集和十折交叉验证评估分类性能。
- 数据公开性: private_or_nonpublic | 实验室受控实验采集的参与者行为与生理数据，非公开渠道。
- 综合判定: 该研究针对欺骗者（对抗行为者）攻击自动筛查系统（安全系统）的反制行为，核心是开发并实证评估多指标自动欺骗检测算法，属于安全攻防与算法开发双重核心；数据为实验室私有数据。

## [21] A hierarchical Naïve Bayes model for approximate identity matching
- 年份/期刊: 2011 / Decision Support Systems | DOI: 10.1016/j.dss.2011.01.007 | 置信度: 0.95 | record: 314
- 安全: core_security_attack_defense | 论文针对执法和反恐领域中的身份匹配，核心是检测因故意欺骗（如犯罪分子和恐怖分子使用假身份误导调查）和错误导致的身份不一致，属于威胁检测和防御范畴。
- 算法: novel_algorithm_with_evaluation | 方法: 分层朴素贝叶斯模型（HNB）用于近似身份匹配，结合半监督EM学习
- 评估: 使用Tucson警察局COPLINK真实执法数据，对2000个身份比较样本进行10折交叉验证，与精确匹配和记录比较算法在精度、召回率、F值上比较
- 数据公开性: private_or_nonpublic | Tucson警察局COPLINK数据库中的2.4百万身份记录（非公开执法数据），随机抽取200个嫌疑人记录及人工验证的匹配记录。
- 综合判定: 论文提出并实证评估了一个新的分层朴素贝叶斯模型用于身份匹配，该模型服务于执法和反恐中的安全需求，能够检测错误和故意欺骗身份；数据来自警方内部数据库，属于非公开数据。

## [22] Design Principles for Signal Detection in Modern Job Application Systems: Identifying Fabricated Qualifications
- 年份/期刊: 2020 / Journal of Management Information Systems | DOI: 10.1080/07421222.2020.1790201 | 置信度: 0.95 | record: 1598
- 安全: core_security_attack_defense | 论文核心是检测求职者在申请过程中伪造资格/撒谎的对抗行为，属于欺骗检测与人员安全风险评估，并明确提到可扩展到安全筛查、审计访谈等领域。
- 算法: novel_algorithm_with_evaluation | 方法: SIGHT（识别真正隐藏人才系统）——基于网络摄像头捕捉视觉、语音、语言信号并融合机器学习分类的自动面试信号检测方法
- 评估: 89名本科生的模拟面试实验，提取信号后使用径向SVM、随机森林、Boosted LR、Bagged ANN四个分类器进行100折蒙特卡洛交叉验证，F1值在0.84-0.95之间。
- 数据公开性: private_or_nonpublic | 作者在2017年春季、美国某大学进行的89名本科生的模拟招聘实验数据（视频、音频、语言及问卷数据），属于非公开的实验采集数据。
- 综合判定: 安全相关性：存在恶意行为者（伪造资格的求职者），核心是检测和防御欺骗，损害的是组织的人员诚信与安全风险，不属于纯金融欺诈；算法开发：论文核心是提出并实现新系统SIGHT并实证评估，包含多模态信号处理与分类模型，满足新方法开发与实证评估条件；数据公开性：主要数据来自私有实验收集，非公开。

## [23] Network externalities, layered protection and IT security risk management
- 年份/期刊: 2007 / Decision Support Systems | DOI: 10.1016/j.dss.2006.08.009 | 置信度: 0.93 | record: 2776
- 安全: core_security_attack_defense | 论文以IT安全风险为研究对象，明确考虑外部/内部攻击者、系统漏洞、攻击成功概率与级联攻击，核心是安全防护资源的最优分配与风险缓解，属于典型的安全攻防与风险管理领域。
- 算法: novel_algorithm_with_evaluation | 方法: 安全投资分配优化模型（单层/双层保护、含网络外部性与聚类保护）
- 评估: 使用Matlab构造200系统的数值仿真，对比基线、分层保护、网络外部性、聚类保护及不确定性场景下的风险水平（如Table 4聚合风险结果）。
- 数据公开性: private_or_nonpublic | 全文使用人工设定的数值仿真参数（如200个系统、正态分布系统价值、假设攻击概率），无真实企业或公开数据集。
- 综合判定: 安全相关性：全文围绕IT系统安全风险，存在攻击者与级联攻击，核心是防御资源分配与缓解，非金融欺诈或一般预测。算法开发：提出新的安全投资优化模型并给出解析解法与算法，通过Matlab数值仿真进行实证评估，核心贡献是方法本身。数据公开性：仅用合成数值仿真，无公开真实数据。故strict_include=true。

## [24] Intrusion Prevention in Information Systems: Reactive and Proactive Responses
- 年份/期刊: 2007 / Journal of Management Information Systems | DOI: 10.2753/mis0742-1222240110 | 置信度: 0.92 | record: 1230
- 安全: core_security_attack_defense | 论文聚焦入侵防御中的恶意事件检测与主动/被动响应决策，核心是安全攻防与缓解。
- 算法: novel_algorithm_with_evaluation | 方法: 入侵防御中检测配置与响应策略的联合最优控制模型
- 评估: 通过四组数值算例和敏感性分析，与静态模型对比验证成本节省与策略切换。
- 数据公开性: unclear | 全部使用假设参数数值算例，未使用真实数据或公开数据集。
- 综合判定: 论文属于安全领域的入侵检测与防御研究，存在恶意行为者（攻击者）且核心围绕威胁检测/响应；提出了新的动态最优控制模型并实现了数值实证评估；符合两个模块的纳入标准。数据为假设参数，公开性无法判断但仅记录。

## [25] A decision methodology for managing operational efficiency and information disclosure risk in healthcare processes
- 年份/期刊: 2014 / Decision Support Systems | DOI: 10.1016/j.dss.2012.10.046 | 置信度: 0.92 | record: 854
- 安全: core_security_attack_defense | 论文针对医疗工作流中的信息披露风险，明确提及恶意员工可收集信息用于身份盗窃、勒索等，核心是设计控制策略防止信息泄露和欺诈，属于信息安全的防御。
- 算法: novel_algorithm_with_evaluation | 方法: 两阶段决策方法（吞吐量优化与安全控制放置优化，含集合覆盖与随机规划扩展）
- 评估: 基于一个13任务、7员工的临床工作流假设参数，对六个最优任务分配进行比较，分析不同员工/任务控制方案的冲突集覆盖效果。
- 数据公开性: unclear | 计算实验所用临床工作流参数（服务率、技能矩阵、冲突集等）为作者设定或校准，未说明是否来自公开真实数据集。
- 综合判定: 文章研究的问题是医疗工作流中的信息披露风险，属于信息安全防护；核心贡献是开发并实证评估了新的两阶段决策优化方法，因此安全相关性和算法开发均通过。数据来自假设参数，公开性不明确。

## [26] A social referral appraising mechanism for the e-marketplace
- 年份/期刊: 2017 / Information & Management | DOI: 10.1016/j.im.2016.07.001 | 置信度: 0.92 | record: 2702
- 安全: core_security_attack_defense | 论文针对卖家操纵在线评级的信任欺诈问题，提出社交推荐机制以帮助买家评估并避开欺诈卖家，核心是防御声誉操纵。
- 算法: novel_algorithm_with_evaluation | 方法: 社交推荐机制（SRM），结合吸引力、专业知识、共同取向和可信度分析
- 评估: 基于Facebook社交互动与Yahoo!拍卖交易数据的实验，与EO、CF、Public基准比较，报告准确率、MAE、precision/recall/F1。
- 数据公开性: private_or_nonpublic | 通过雪球抽样招募参与者并获取其Facebook互动数据与Yahoo!拍卖交易记录。
- 综合判定: 安全上，核心针对卖家的恶意评级操纵（信任欺诈），属于对抗行为者下的防御与缓解；算法上，提出并实证评估了新的社交推荐信誉算法。数据主要来自私有参与者授权数据。

## [27] An investigation of Zipf's Law for fraud detection (DSS#06-10-1826R(2))
- 年份/期刊: 2008 / Decision Support Systems | DOI: 10.1016/j.dss.2008.05.003 | 置信度: 0.92 | record: 1662
- 安全: core_security_attack_defense | 文章提出Zipf Analysis用于检测网络入侵攻击（KDDCUP'99数据集中的DoS、Probe等）及案例中的网络攻击，核心是恶意攻击的检测与防御。
- 算法: novel_algorithm_with_evaluation | 方法: Zipf Analysis（基于Zipf定律的模式频率异常检测方法）
- 评估: 在公开KDDCUP'99入侵检测数据集上进行准实验，使用AHR、BAHR、混淆矩阵和误分类成本与基准比较；另以真实公司防火墙日志进行案例验证。
- 数据公开性: mixed | 主要实验数据为公开的KDDCUP'99入侵检测数据集；案例研究使用某公司的非公开防火墙和核心交换机日志。
- 综合判定: 文章核心是开发并实证评估基于Zipf定律的异常/攻击检测算法（Zipf Analysis），其研究场景明确为网络入侵检测与网络攻击事件，符合安全攻防检测定义；算法贡献有实现和基于KDDCUP'99及案例数据的评估。数据以公开为主，含非公开案例数据。

## [28] Sharing and access right delegation for confidential documents: A practical solution
- 年份/期刊: 2006 / Information & Management | DOI: 10.1016/j.im.2006.03.003 | 置信度: 0.9 | record: 2442
- 安全: core_security_attack_defense | 研究针对机密文档的未授权访问与网络攻击者威胁，提出通过加密与ACL相结合的防御方案，核心目标是保护文档机密性。
- 算法: novel_algorithm_with_evaluation | 方法: 基于会话密钥和ACL的加密文档共享与访问权限委派方案（含虚拟用户扩展）
- 评估: 在约50个用户的原型上测试上传/下载耗时，并与无加密基线比较；实验结果显示性能可接受。
- 数据公开性: private_or_nonpublic | 作者自建原型并生成约50个用户进行内部性能测试，未使用公开数据集。
- 综合判定: 文章针对机密文档保护中的共享和委派问题，明确将攻击者视为威胁，并提出一个结合ACL和加密的技术方案；该方案实现为原型，并进行了基于数据的性能评估，故安全相关性和算法开发均通过。

## [29] An outlier-based data association method for linking criminal incidents
- 年份/期刊: 2006 / Decision Support Systems | DOI: 10.1016/j.dss.2004.06.005 | 置信度: 0.85 | record: 2012
- 安全: core_security_attack_defense | 文章针对连环抢劫案件的事件关联，以识别和打击犯罪行为，存在恶意行为者（连环罪犯）且核心是犯罪威胁的检测与防御。
- 算法: novel_algorithm_with_evaluation | 方法: 基于异常值的数据关联方法（outlier score function + 熵不确定性函数）
- 评估: 使用美国Richmond, VA 1998年抢劫数据集（1198条记录），以嫌疑人数据库为真值，与基于相似度的关联方法比较，采用真关联检测率和平均相关记录数两个指标。
- 数据公开性: private_or_nonpublic | 主要数据来自美国Richmond, VA警方1998年抢劫事件数据集和嫌疑人数据库（专有非公开），另有公开的人口普查数据作为辅助属性。
- 综合判定: 安全相关：存在恶意行为者（连环抢劫犯），研究核心是关联犯罪事件以检测犯罪模式并辅助执法，损害对象为用户/组织安全（公共安全），不属于金融欺诈；算法开发：提出了新的基于异常值的数据关联方法（含异常值评分函数和熵不确定性度量），实现了方法并在真实数据集上进行了实证比较评估；数据公开性：主要数据来自警方专有抢劫与嫌疑人数据，属于非公开。

## [30] Effects of Automated and Participative Decision Support in Computer-Aided Credibility Assessment
- 年份/期刊: 2011 / Journal of Management Information Systems | DOI: 10.2753/mis0742-1222280107 | 置信度: 0.82 | record: 1262
- 安全: core_security_attack_defense | 文章核心是检测欺骗性信息，对抗性行为者（说谎者）处于研究中心，目标是通过计算机辅助系统检测防御欺骗，属于社会工程与误导信息检测范畴，而非单纯金融欺诈。
- 算法: novel_algorithm_with_evaluation | 方法: 混合行为分析系统（H-BAS），结合自动语言特征挖掘与间接线索诱发
- 评估: 实验室实验，167名参与者随机分配到四种条件，比较了决策辅助的推荐准确率、用户接受率和用户评估准确率，使用了t检验、ANCOVA等统计方法。
- 数据公开性: private_or_nonpublic | 实验数据来自实验室招募的167名学生参与者，刺激材料为先前实验收集的高风险访谈录像，未公开渠道获取。
- 综合判定: 安全相关性：研究针对欺骗性信息检测这一对抗性行为，属于安全领域的误导信息检测与防御；算法开发：提出了新的混合决策辅助方法并进行了实证评估，核心贡献是系统开发与实验验证。数据为非公开实验数据。

## [31] Decision support for network disruption mitigation
- 年份/期刊: 2008 / Decision Support Systems | DOI: 10.1016/j.dss.2007.11.003 | 置信度: 0.82 | record: 2256
- 安全: core_security_attack_defense | 文章聚焦于网络基础设施在恐怖袭击、蓄意破坏等对抗行为下的中断影响评估与缓解，属于安全攻防领域。
- 算法: novel_algorithm_with_evaluation | 方法: 空间决策支持系统NIMPRO（集成Flow Interdiction Model、场景枚举/采样、流中断指数FDI等）
- 评估: 在Abilene电信骨干网络（11节点14弧）上使用真实流量数据，评估不同中断场景、节点加固和链路增加对流量中断的影响，并与原网络比较。
- 数据公开性: public | Abilene Internet2骨干网络拓扑与节点间流量数据，来自公开的Abilene项目及所引文献[1,28]。
- 综合判定: 安全相关性：明确针对恐怖袭击、蓄意攻击等恶意行为者对关键网络基础设施的中断影响评估与防御缓解，属于核心安全攻防；算法开发：提出了新的决策支持系统NIMPRO及新指标FDI，并实现和基于真实网络数据进行实证评估；数据公开性：主要使用公开的Abilene网络数据。因此纳入。

