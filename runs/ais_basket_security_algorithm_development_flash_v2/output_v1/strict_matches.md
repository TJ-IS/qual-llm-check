# Security-relevant algorithm development (AIS Basket)

Completed: 13909 / 13909
Retained: 99

## An efficacious method for detecting phishing webpages through target domain identification

- Year/journal: 2014 / Decision Support Systems
- DOI: 10.1016/j.dss.2014.01.002
- Security status: core_security_attack_defense
- Security reason: 研究核心是检测钓鱼网页并识别其模仿的目标域，属于典型的对抗性攻击检测与防御。
- Algorithm status: novel_algorithm_with_evaluation
- Method: TID目标域识别算法及基于DNS比对的钓鱼检测方法
- Evaluation: 基于4574个真实网站（1200合法，3374钓鱼）的实证评估，与CANTINA、CANTINA+、Wenyin等方法比较，TPR 99.67%，FPR 0.5%，ACC 99.62%。
- Algorithm reason: 提出新的钓鱼检测与目标域识别算法，并实现了该系统且用真实数据集进行了实证评估。
- Data publicness: public / 合法网页来自Google top 1000、Alexa、Netcraft、Millersmiles等公开列表；钓鱼网页来自Phishtank和Reasonable-phishing公开数据库。
- Decision: 文章聚焦钓鱼网页检测与目标域识别，安全核心明确；提出并实现了新算法且进行了大规模实证评估；数据来源于公开数据集。
- Confidence: 1.0

## Automated dynamic approach for detecting ransomware using finite-state machine

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113400
- Security status: core_security_attack_defense
- Security reason: 研究核心是检测勒索软件攻击，勒索软件是恶意行为者实施的针对信息系统数据的加密、删除和锁定攻击，属于信息安全攻防领域。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于有限状态机（FSM）的动态勒索软件检测系统
- Evaluation: 使用475个勒索软件样本与1500个合法应用样本进行实验，TPR=98.1%、FPR=0%、准确率99.54%，并与ShieldFS、Lu et al.等方法对比。
- Algorithm reason: 论文提出并实现了基于FSM的动态勒索软件检测方法，包含行为分析模块和决策模块，并通过包含多家族恶意样本和合法样本的数据集进行了实证评估，方法贡献是核心。
- Data publicness: public / 恶意软件样本来自GitHub theZoo和VirusTotal公开来源；合法应用来自软件下载网站（如Softpedia、MajorGeeks等）。
- Decision: 文章研究核心是勒索软件检测与防御，属于信息系统安全攻防领域；提出并实现了基于FSM的新检测算法，并进行了实证评估。数据来源公开，故纳入。
- Confidence: 1.0

## Enhancing Predictive Analytics for Anti-Phishing by Exploiting Website Genre Information

- Year/journal: 2015 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2014.1001260
- Security status: core_security_attack_defense
- Security reason: 论文核心是钓鱼网站检测，针对恶意欺骗性网站攻击，属于信息系统安全攻防领域。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 流派树核方法（Genre Tree Kernel）
- Evaluation: 在4050个网站的测试床上与多个内容基方法和现有反钓鱼工具比较，整体准确率97.01%，显著优于基线；另进行了用户实验。
- Algorithm reason: 提出并实现了新的genre tree kernel方法，并通过大规模实验和用户研究进行了实证评估。
- Data publicness: public / 主要数据来自公开的钓鱼网站数据库（PhishTank、反钓鱼工作组、Artists Against 419等）和公开合法网站爬取。
- Decision: 文章属于信息安全领域：以钓鱼网站检测为核心，恶意行为者与安全损害明确；同时提出并实证评估了新算法（genre tree kernel），满足算法开发条件；数据主要来自公开来源。
- Confidence: 0.99

## Factor-analysis based anomaly detection and clustering

- Year/journal: 2006 / Decision Support Systems
- DOI: 10.1016/j.dss.2005.01.005
- Security status: core_security_attack_defense
- Security reason: 文章核心是网络入侵检测：基于因子分析与马氏距离的新算法用于检测和聚类网络攻击（如Neptune、Smurf、DoS等），即恶意行为者对信息系统的攻击检测与防御。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于因子分析与马氏距离的异常检测与聚类算法
- Evaluation: 在DARPA 1999入侵检测评估数据上实验，与ADAM系统比较，报告检测率、误报率、漏报率等指标。
- Algorithm reason: 作者提出并实现了以因子分析和马氏距离为核心的新型异常检测与聚类算法，在DARPA公开数据集上进行了实证评估并与ADAM比较。
- Data publicness: public / 主要数据为DARPA Intrusion Detection Evaluation Data（1998/1999），公开基准数据集。
- Decision: 该文核心是网络入侵检测（信息系统安全攻防检测），提出新的因子分析+马氏距离异常检测与聚类算法，在DARPA公开数据集上实证评估，满足安全相关与算法开发双条件；数据为公开DARPA数据。
- Confidence: 0.99

## <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" altimg="si1.gif" overflow="scroll"><mml:mrow><mml:mi>β</mml:mi><mml:mi mathvariant="script">P</mml:mi></mml:mrow></mml:math>: A novel approach to filter out malicious rating profiles from recommender systems

- Year/journal: 2013 / Decision Support Systems
- DOI: 10.1016/j.dss.2013.01.020
- Security status: core_security_attack_defense
- Security reason: 研究核心是检测推荐系统中恶意评分档案（shilling attacks/profile injection）这一对抗行为，并防御其对推荐系统完整性及用户信任的损害。
- Algorithm status: novel_algorithm_with_evaluation
- Method: Beta-Protection (βP)
- Evaluation: 在MovieLens公开数据集上模拟多种shilling攻击（单/多目标，push/nuke），以检测率和误报率为指标，并与PCA方法对比。
- Algorithm reason: 提出基于Beta分布的三阶段异常检测算法βP，并给出伪代码与实验验证，方法贡献为核心贡献。
- Data publicness: public / MovieLens数据集（GroupLens Research Lab公开数据）
- Decision: 文章聚焦推荐系统遭恶意评分档案注入攻击的检测与防御，对抗行为是研究核心，损害对象为系统数据完整性与用户信任（信息安全属性）；提出了新算法βP并基于MovieLens公开数据进行了实证评估和对比，故安全相关与算法开发均通过；数据来源于公开数据集。
- Confidence: 0.98

## A domain-feature enhanced classification model for the detection of Chinese phishing e-Business websites

- Year/journal: 2014 / Information & Management
- DOI: 10.1016/j.im.2014.08.003
- Security status: core_security_attack_defense
- Security reason: 研究核心是检测恶意钓鱼网站——攻击者创建假冒电子商务网站窃取用户身份凭据和敏感信息，属于典型的信息系统安全威胁检测。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 
- Evaluation: 
- Algorithm reason: 提出融合中文电商领域特征的新分类模型（CBML），包含15个特征（含5个全新的领域特征），用四种机器学习算法实现并在约3000个真实网站上与两个基线模型进行了实证比较，方法贡献是全文核心。
- Data publicness: public / 数据来自公共来源：1416个钓鱼网站来自315online.com.cn和anquan.org，1462个真实电商网站来自公共网络，通过WebZIP抓取源码。
- Decision: 论文核心是用机器学习方法检测恶意钓鱼电商网站——明确的安全威胁检测任务，且提出了包含新领域特征的特征向量和分类模型，进行了完整的实证评估；因此安全相关和算法开发两个模块均通过，数据来源主要是公开网站和公开报告平台，记为public。
- Confidence: 0.98

## Assessing and Enhancing Adversarial Robustness of Predictive Analytics: An Empirically Tested Design Framework

- Year/journal: 2022 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2022.2063549
- Security status: core_security_attack_defense
- Security reason: 文章核心是应对对抗性攻击（恶意行为人精心构造垃圾评论/垃圾邮件以规避SML检测系统），提出并实证评估了对抗鲁棒性评估与增强框架，属于信息系统安全攻防。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 
- Evaluation: 
- Algorithm reason: 论文核心是开发并实证评估了ARText系统，它实现了对抗鲁棒性评估新度量（性能比、性能-扰动曲线下面积）与集成学习+对抗重训练增强算法，并在公开测试集上与多个基线模型比较。
- Data publicness: public / 使用公开基准数据集：Ott等（2013）的虚假评论数据集（含TripAdvisor等渠道评论与AMT标注）和Apache SpamAssassin公开语料库。
- Decision: 安全相关性：研究直接针对恶意对抗行为者攻击SML预测系统（规避垃圾检测），核心是检测/防御/评估；算法开发：提出新系统ARText（新鲁棒性度量、集成学习+对抗重训练）并实现、实证评估，且用公开数据；故纳入。
- Confidence: 0.98

## Augmenting Social Bot Detection with Crowd-Generated Labels

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1136
- Security status: core_security_attack_defense
- Security reason: 研究核心是检测恶意社交机器人，这些机器人被明确定位为网络对手，用于操纵话语、传播垃圾信息、恶意软件和钓鱼等，属于针对社交媒体平台和用户的信息系统安全威胁；文章的主要贡献是增强此类威胁的检测能力。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于人群反应与言语行为理论增强的社交机器人检测框架（使用BERT等深度学习模型）
- Evaluation: 使用Reddit公开API收集的真实众包数据，与传统特征模型对比，并进行了消融实验、时间检测模拟和与文献方法的基准比较。
- Algorithm reason: 文章提出了一种新的计算方法：利用人群对机器人消息的反应及言语行为分类增强社交机器人检测，并使用BERT等深度学习方法实现和实证评估，核心贡献是该方法本身。
- Data publicness: public / Reddit公共API收集的对话数据，以及公开的r/BotWatchman社区众包机器人名单。
- Decision: 文章聚焦恶意社交机器人的检测，属于信息系统安全领域的攻击检测与防御；同时开发了基于人群反应和言语行为理论的新计算框架，通过深度学习实现并在真实公开数据上进行了充分的实证评估，两个核心条件均满足。数据来源为Reddit公共API，属于公开数据。
- Confidence: 0.98

## Bayesian Stackelberg games for cyber-security decision support

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113599
- Security status: core_security_attack_defense
- Security reason: 研究以对抗多阶段网络攻击为核心，通过攻击图建模攻击者行为，优化防御安全控制组合，属于典型的信息系统安全攻防与防御决策。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于攻击图的贝叶斯Stackelberg博弈在线防御优化（转化为MICP求解）
- Evaluation: 在随机生成完整攻击图和现实校园网络案例上实验，与DOBSS、HBGS、HUNTER等对比计算时间与安全风险。
- Algorithm reason: 提出将在线防御优化精确转化为MICP的新算法，核心贡献为算法设计与实现，并通过数值实验和案例研究进行了实证评估。
- Data publicness: private_or_nonpublic / 主要数据为作者随机生成的完整攻击图以及基于文献[34]和MITRE ATT&CK构造的校园网络案例，并非公开数据集。
- Decision: 安全相关：文章针对网络攻击者利用攻击图进行多阶段攻击，研究防御方选择安全控制组合以降低攻击成功概率和风险，安全损害对象为信息系统安全属性，属于核心安全攻防；算法开发：提出将在线防御优化转化为MICP的新求解算法，实现并用随机图和案例数据进行了实证评估，算法为核心贡献；数据公开性：主要数据为作者生成的随机图和案例数据，非公开数据集。
- Confidence: 0.98

## Cyber-risk decision models: To insure IT or not?

- Year/journal: 2013 / Decision Support Systems
- DOI: 10.1016/j.dss.2013.04.004
- Security status: core_security_attack_defense
- Security reason: 文章核心是评估和缓解黑客、病毒、DDoS等恶意攻击造成的安全漏洞与损失，提出漏洞评估和保险决策模型，属于信息系统安全攻防与风险缓解。
- Algorithm status: novel_algorithm_with_evaluation
- Method: CBBN（Copula辅助贝叶斯信念网络）C-VA算法与UBPP效用偏好保费定价模型
- Evaluation: 使用印度某商学院两年期实际安全设备日志数据验证；输出漏洞评估表、预期损失、保费，并与风险中性/风险厌恶等不同风险画像比较。
- Algorithm reason: 论文提出并实现了新的计算方法（CBBN漏洞评估和UBPP保费模型），并用真实数据进行了实证评估，方法是核心贡献而非仅作工具。
- Data publicness: private_or_nonpublic / 主要数据来自印度一所商学院内部 perimeter 安全设备日志数据，属于非公开渠道数据。
- Decision: 文章以恶意攻击（黑客、病毒、DDoS）引发的安全漏洞和损失为研究问题，核心贡献是开发并实证评估CBBN（漏洞评估）与UBPP（保费定价）算法，因此同时满足安全相关和算法开发条件；数据来自内部日志，为非公开数据，但不影响纳入。
- Confidence: 0.98

## Decision support for the optimal allocation of security controls

- Year/journal: 2018 / Decision Support Systems
- DOI: 10.1016/j.dss.2018.10.001
- Security status: core_security_attack_defense
- Security reason: 研究核心是优化信息系统安全控制配置，以降低完整性、机密性和可用性三类安全漏洞造成的损失，属于安全攻防和防御决策。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 
- Evaluation: 
- Algorithm reason: 提出并求解了确定性混合整数规划模型和两阶段随机优化模型，利用调查数据拟合分段线性函数并通过CPLEX进行计算实验与敏感性分析，是新的优化算法且为论文核心贡献。
- Data publicness: private_or_nonpublic / 通过调查49名安全专业人员获取漏洞概率估计，并结合焦点小组确定的安全控制成本，属于私有的一次性调查数据。
- Decision: 文章以信息系统安全漏洞（机密性、完整性、可用性）的防御为核心，提出了用于安全控制优化分配的新型确定性及随机优化模型，并使用基于调查数据拟合的分段线性函数进行CPLEX求解和实证计算实验，完全满足安全相关性与算法开发两项纳入标准；主要数据来自非公开的调查和焦点小组。
- Confidence: 0.98

## Detecting Anomalous Online Reviewers: An Unsupervised Approach Using Mixture Models

- Year/journal: 2019 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2019.1661089
- Security status: core_security_attack_defense
- Security reason: 研究核心是检测在线评论平台上的虚假评论者（opinion spammers），即恶意行为者对在线评论系统的操纵，损害评论内容的真实性与完整性，属于信息系统安全中的内容操纵攻击检测。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于堆叠混合模型的无监督异常评论者检测方法（STK）
- Evaluation: 在Yelp真实数据集和合成数据集上，与GMM、DPGMM、One-Class SVM、Uniform Stacking、FraudEagle、SpEagle等基线比较，使用ROC-AUC、precision@K、log-likelihood、AIC/BIC等指标评估。
- Algorithm reason: 论文提出并实现了一种新的无监督概率混合模型方法，核心贡献是方法本身，并进行了全面的实证评估。
- Data publicness: public / Yelp.com餐厅评论数据集，由Rayana和Akoglu共享，属于公开渠道可获取的数据集。
- Decision: 该文核心是检测在线评论平台上的虚假评论者，属于恶意行为者对信息系统内容真实性和完整性的攻击，研究重点在于检测与防御；方法上提出了新颖的堆叠混合模型无监督算法，并实现了完整的实证评估。数据为公开的Yelp数据集。
- Confidence: 0.98

## Harmonized authentication based on ThumbStroke dynamics on touch screen mobile phones

- Year/journal: 2016 / Decision Support Systems
- DOI: 10.1016/j.dss.2016.09.007
- Security status: core_security_attack_defense
- Security reason: 研究核心是移动设备用户认证，旨在防止未授权访问，针对 shoulder surfing、smudge 攻击、密码窃取等恶意行为，属于信息系统安全攻防。
- Algorithm status: novel_algorithm_with_evaluation
- Method: HATS（基于拇指运动动力学的统一认证方法，含ThumbStroke虚拟键盘和分类验证模型）
- Evaluation: 通过12名参与者的纵向受控实验，比较HATS与击键动力学方法，采用EER、准确率、输入时间等指标，并对比多种分类器（RF、NN、KNN、SVM等）。
- Algorithm reason: 论文提出新的认证方法HATS作为核心贡献，包含新型键盘和基于机器学习分类器的验证模型，并实现为Android原型，通过实证实验进行了评估。
- Data publicness: private_or_nonpublic / 受控实验室实验收集的参与者触摸行为数据，非公开数据集。
- Decision: 安全相关：研究针对移动认证中的恶意未授权访问和攻击（如shoulder surfing、smudge），属于核心安全攻防。算法开发：提出新的认证方法HATS并实现、评估，属于新算法且有实证。数据公开性：数据来自非公开的实验室实验。
- Confidence: 0.98

## Identity disclosure protection: A data reconstruction approach for privacy-preserving data mining

- Year/journal: 2009 / Decision Support Systems
- DOI: 10.1016/j.dss.2009.07.003
- Security status: core_security_attack_defense
- Security reason: 研究核心是防止数据入侵者通过准标识符识别个体敏感信息的身份披露攻击，属于隐私披露攻击的匿名化防御。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于遗传算法的数据重建k匿名方法（GA-based data reconstruction for k-anonymity）
- Evaluation: 使用UCI Diabetes和German Credit数据集，结合C4.5和SVM分类器，评估分类准确率、记录链接披露风险（RL）及简单统计误差（ADIM/ADIFC），并与仅聚合交换和无GA处理比较。
- Algorithm reason: 提出数值聚合、名义交换和遗传算法实例选择相结合的新颖数据重建方法，并实现了算法，在公开真实数据集上进行了实证评估。
- Data publicness: public / UCI机器学习库的Diabetes和German Credit两个公开数据集。
- Decision: 文章针对身份披露攻击（恶意入侵者通过准标识符识别敏感信息）提出数据重建防御方法，属于信息系统安全中的隐私保护；核心贡献是新颖的基于遗传算法的k匿名数据重建算法，并在公开数据集上实现和实证评估。数据来自UCI公开数据集。
- Confidence: 0.98

## PhishWHO: Phishing webpage detection via identity keywords extraction and target domain name finder

- Year/journal: 2016 / Decision Support Systems
- DOI: 10.1016/j.dss.2016.05.005
- Security status: core_security_attack_defense
- Security reason: 论文核心是检测钓鱼网页攻击，恶意行为人（phisher）直接针对信息系统用户实施凭证窃取，研究围绕攻击检测与防御，属于信息系统安全攻防。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 
- Evaluation: 
- Algorithm reason: 提出PhishWHO检测方法，包含加权URL tokens系统、N-gram身份关键词提取、搜索引擎目标域名查找和3-tier身份匹配，并基于5000个钓鱼和5000个合法网页进行实证对比评估。
- Data publicness: public / PhishTank和OpenPhish的钓鱼URL、Alexa top one million合法URL均为公开渠道数据。
- Decision: 安全相关：钓鱼攻击检测是明确的信息系统安全攻防主题，恶意行为者和安全损害均为核心；算法开发：提出新检测方法并实现实证评估；数据公开性：主要来自公开数据集。三模块均通过，strict_include为true。
- Confidence: 0.98

## Privacy Protection in Data Mining: A Perturbation Approach for Categorical Data

- Year/journal: 2006 / Information Systems Research
- DOI: 10.1287/isre.1060.0095
- Security status: core_security_attack_defense
- Security reason: 研究核心是防止或限制数据挖掘中个体记录的隐私披露（重识别和价值披露），数据窥探者作为对抗行为者，提出的扰动方法属于隐私保护与披露防御。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 
- Evaluation: 
- Algorithm reason: 提出两阶段扰动方法（线性规划+贝叶斯交换），在三个真实数据集上与随机扰动和Reiss方法对比，实验验证其有效性。
- Data publicness: public / 主要数据来自公开渠道：AIS MIS教师薪资调查公开数据、UCI Census收入数据集、UCI CMC避孕方法选择数据集。
- Decision: 文章属于信息系统安全中的隐私保护与披露防御，核心贡献是新的数据扰动算法并经过真实数据实证评估；主要数据均来自公开数据集。
- Confidence: 0.98

## RADAR: A Framework for Developing Adversarially Robust Cyber Defense AI Agents with Deep Reinforcement Learning

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2024/17339
- Security status: core_security_attack_defense
- Security reason: 研究核心是对抗性攻击（恶意软件规避攻击）及对网络防御AI代理的鲁棒性增强，属于信息系统安全攻防范畴。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 
- Evaluation: 
- Algorithm reason: 提出并实现了RADAR框架（含r-VAC和RL-RO）作为新的深度强化学习鲁棒化方法，并在多个恶意软件检测器上与多种基准进行实证比较。
- Data publicness: private_or_nonpublic / VirusTotal学术许可获取的恶意软件样本、自行收集的Windows良性文件；数据非公开可获取。
- Decision: 文章核心是面向恶意软件检测器的对抗攻击生成与防御鲁棒化，属于信息系统安全攻防；同时提出了新的深度强化学习方法（r-VAC）和鲁棒优化方法（RL-RO），实现了并有基于数据的实证评估。数据来自VirusTotal学术许可等非公开渠道，仅作记录。
- Confidence: 0.98

## Shapley Value-Based Feature Attribution for Data Masking

- Year/journal: 2026 / MIS Quarterly
- DOI: 10.25300/misq/2025/18502
- Security status: core_security_attack_defense
- Security reason: 研究针对共享微数据面临的推断性披露攻击，以恶意入侵者利用非机密特征推断机密信息为对抗核心，通过数据掩蔽提供防御，属于信息系统安全中的数据隐私保护。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 
- Evaluation: 
- Algorithm reason: 提出基于Shapley值的特征归因数据掩蔽框架，实现为Algorithm 1，并在模拟及三个真实数据集上与多种基准方法进行实证比较，核心贡献是新的特征选择与掩蔽计算方法。
- Data publicness: mixed / 实验数据包括Kaggle Home Credit模拟数据、UCI信用数据集、公开的MIS教师薪资调查数据，以及CRSP/Compustat（商业订阅数据库）等公开与非公开源的混合。
- Decision: 安全相关性上，文章明确以恶意入侵者或对抗者利用发布数据推断机密属性为威胁，研究数据掩蔽以减少推断性披露风险，属于安全攻防与防御；算法开发上，提出了新的Shapley值特征归因与特征选择框架，实现并通过模拟和真实数据实证评估，满足新算法+实证评估。数据公开性为混合，但不影响纳入。
- Confidence: 0.98

## A deep learning approach for detecting fake reviewers: Exploiting reviewing behavior and textual information

- Year/journal: 2023 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113911
- Security status: core_security_attack_defense
- Security reason: 研究核心是检测在线评论平台上的虚假评论者（opinion spammers），属于针对信息系统用户的内容操纵与误导信息攻击，对抗行为者是研究问题本身的对象，损害的是评论系统的真实性与用户信任。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于行为敏感卷积特征提取器与上下文感知注意力机制（Longformer+CNN+BiLSTM+Attention）的端到端虚假评论者检测框架
- Evaluation: 在YelpZIP和YelpNYC两个真实数据集上与LR、RF、SVM、CART、NB、CNN、BiLSTM、C-LSTM、BERT、ALBERT、DistilBERT、RoBERTa、Longformer等基准进行比较，使用准确率、精确率、召回率、F1和AUC指标，并进行了消融实验和配对t检验。
- Algorithm reason: 论文核心贡献是提出一个新的深度学习方法用于虚假评论者检测，实现了该方法并在两个Yelp数据集上进行了系统实证评估，方法不是现成工具的简单应用。
- Data publicness: public / 主要数据来自公开的YelpZIP和YelpNYC数据集，源自Yelp.com并由Rayana和Akoglu公开共享。
- Decision: 文章属于信息系统安全范畴：检测在线评论操纵者（虚假评论者）是对抗性内容操纵行为的检测与防御，损害评论系统真实性和用户信任；同时论文提出并实现了新的深度学习方法（行为敏感特征提取器+上下文感知注意力机制），并在两个公开Yelp数据集上进行了系统实证评估。数据来自公开Yelp数据集。三个模块均满足条件，故strict_include=true。
- Confidence: 0.97

## A maximum entropy approach to feature selection in knowledge-based authentication

- Year/journal: 2008 / Decision Support Systems
- DOI: 10.1016/j.dss.2008.07.008
- Security status: core_security_attack_defense
- Security reason: 研究针对知识型认证中的特征选择，以理性攻击者的猜测策略为对象，通过最大化KL散度选择最难猜的事实问题，以增强认证系统的抗未授权访问能力，属于信息系统安全攻防核心。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于最大熵的自适应特征选择方法（域自适应DomFS、身份自适应IdtFS、响应自适应ResFS）
- Evaluation: 使用MCMC生成的合成KBA域和索赔人数据，与随机特征选择比较，评估了准确率、FAR、FRR、EER，自适应方法优于随机基线。
- Algorithm reason: 提出了三种新的最大熵自适应特征选择算法，并实现了模拟实验验证其有效性，核心贡献是新的计算方法。
- Data publicness: private_or_nonpublic / 实验使用MCMC方法生成的合成数据集，非公开来源。
- Decision: 文章提出并实证评估了三种基于最大熵的KBA特征选择算法，以防御攻击者冒充合法用户为研究核心，属于信息系统安全攻防；算法开发有实现和实证评估；数据为合成数据非公开。
- Confidence: 0.97

## Cross-Lingual Cybersecurity Analytics in the International Dark Web with Adversarial Deep Representation Learning

- Year/journal: 2022 / MIS Quarterly
- DOI: 10.25300/misq/2022/16618
- Security status: core_security_attack_defense
- Security reason: 研究核心是在国际暗网中自动检测黑客资产（恶意软件、黑客工具、教程等），这些资产是黑客用于攻击信息系统、破坏安全属性的武器，属于网络安全威胁检测与防御范畴。
- Algorithm status: novel_algorithm_with_evaluation
- Method: ADREL（对抗深度表示学习），用于CLHAD跨语言黑客资产检测
- Evaluation: 在俄语、法语、意大利语暗网论坛和暗网市场数据集上，与基线、单语、机器翻译和跨语言知识迁移等基准方法比较，使用准确率、F1、AUC指标，并有代码公开。
- Algorithm reason: 论文提出新的GAN变体ADREL，实现CLHAD框架，核心贡献是新算法，并进行了系统的实证基准评估。
- Data publicness: public / 暗网公开论坛和暗网市场的公开可访问内容，通过Tor爬虫采集；标注数据集公开在GitHub。
- Decision: 安全相关：研究核心是检测暗网中的黑客资产，这些资产是攻击信息系统、破坏安全属性的工具，属于网络安全检测与防御；算法开发：提出新方法ADREL（GAN变体），实现CLHAD框架，并在多语言暗网数据上进行实证基准评估，满足新算法且有实证评估；数据主要来自公开暗网源，记录为public。
- Confidence: 0.97

## Detecting Fake Websites: The Contribution of Statistical Learning Theory

- Year/journal: 2010 / MIS Quarterly
- DOI: 10.2307/25750686
- Security status: core_security_attack_defense
- Security reason: 研究针对恶意创建的假网站（spoof和concocted）对用户进行钓鱼、身份盗窃和欺诈攻击，开发自动检测系统，核心是攻击检测与防御。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于SVM的线性复合核假网站检测方法（AZProtect系统）
- Evaluation: 在900个网站测试集上对比现有假网站检测系统、多种学习分类器和多种核函数，报告准确性、精确率、召回率、F值和ROC曲线。
- Algorithm reason: 论文提出基于统计学习理论的自定义线性复合核SVM分类器，结合约6000个欺诈线索，并实现AZProtect原型进行实证比较，核心贡献是新检测方法及其评估。
- Data publicness: public / 主要数据来自公开渠道：Phishtank.com、Anti-Phishing Working Group、Artists-Against 4-1-9、Escrow-fraud.com等公开在线社区数据库，以及公开网站。
- Decision: 文章研究假网站检测（防钓鱼、身份盗窃），属于信息系统安全攻防；核心贡献为基于统计学习理论（SVM+自定义线性复合核）的新检测方法，并实现AZProtect系统在900网站数据集上进行多组实证比较实验，因此安全相关和算法开发均通过；主要数据来自公开反钓鱼社区数据库。
- Confidence: 0.97

## Detection of online phishing email using dynamic evolving neural network based on reinforcement learning

- Year/journal: 2018 / Decision Support Systems
- DOI: 10.1016/j.dss.2018.01.001
- Security status: core_security_attack_defense
- Security reason: 研究核心是检测钓鱼邮件攻击，钓鱼者是恶意对抗行为者，损害用户身份信息与账户安全，属于信息系统安全攻防检测。
- Algorithm status: novel_algorithm_with_evaluation
- Method: PEDS框架（含FEaR特征评价与约简、DENNuRL动态进化神经网络、RL-Agent强化学习智能体）
- Evaluation: 使用公开数据集（PhishingCorpus、SpamAssassin、PhishTank）进行50次重复实验，与Islam、Almomani等方法比较，准确率98.63%、TPR 99.07%、TNR 98.19%。
- Algorithm reason: 提出并实现新的检测算法与框架，并以公开数据集进行实证评估和对比，方法贡献是全文核心。
- Data publicness: public / PhishingCorpus、SpamAssassin、PhishTank三个公开数据集
- Decision: 文章围绕钓鱼邮件攻击检测展开，恶意行为者与攻击检测为核心，属于信息系统安全攻防；提出了包含FEaR、DENNuRL和RL-Agent的新算法框架并实现，采用公开数据集进行了实证评估与对比，满足算法开发条件；数据来自公开数据集。
- Confidence: 0.97

## From conflicts and confusion to doubts: Examining review inconsistency for fake review detection

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113513
- Security status: core_security_attack_defense
- Security reason: 文章核心是检测在线评论中的虚假评论（恶意操纵评论内容误导消费者），属于内容操纵攻击的检测与防御，损害评论系统与用户决策的真实性与可信度。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 
- Evaluation: 
- Algorithm reason: 论文提出并实现了三类22个评论不一致性特征，融合到多种经典机器学习分类器中，并在真实Yelp数据集上进行实证评估，显示检测性能显著提升。
- Data publicness: public / 主要数据为来自Yelp.com的24,539条带标注餐厅评论，Yelp为公开平台，数据可公开获取。
- Decision: 文章以虚假评论检测为核心，属于对抗性内容操纵检测，符合安全相关性；同时提出新的不一致性特征并构建机器学习模型进行实证评估，符合算法开发。数据来自公开平台Yelp。综合判定纳入。
- Confidence: 0.97

## INSIDER THREATS IN A FINANCIAL INSTITUTION: ANALYSIS OF ATTACK-PRONENESS OF INFORMATION SYSTEMS APPLICATIONS

- Year/journal: 2015 / MIS Quarterly
- DOI: 10.25300/misq/2015/39.1.05
- Security status: core_security_attack_defense
- Security reason: 研究核心是内部人员对信息系统应用的未授权访问尝试（内部威胁），属于信息系统安全攻防范畴，损害对象为系统与数据的机密性、完整性、可用性。
- Algorithm status: novel_algorithm_with_evaluation
- Method: Weibull风险模型与零膨胀Poisson-Gamma模型
- Evaluation: 基于某金融机构7个月ESSO日志数据（40个应用），使用MCMC估计，并进行了鲁棒性检验，比较了两种风险测度下的模型估计结果。
- Algorithm reason: 论文提出并实现了两个新颖的统计风险模型（Weibull hazard model 和 zero-inflated Poisson-Gamma model）来量化内部威胁风险，并用真实行为日志数据实证评估，是核心贡献。
- Data publicness: private_or_nonpublic / 某美国区域性金融机构的企业单点登录（ESSO）系统日志及内部应用特征数据，非公开。
- Decision: 该文核心研究内部人员对信息系统应用的未授权访问威胁，提出并实证评估了Weibull风险模型和零膨胀Poisson-Gamma模型以量化风险，符合安全攻防与算法开发的双重要求。数据来自非公开金融机构内部系统。
- Confidence: 0.97

## Linking Exploits from the Dark Web to Known Vulnerabilities for Proactive Cyber Threat Intelligence: An Attention-based Deep Structured Semantic Model

- Year/journal: 2022 / MIS Quarterly
- DOI: 10.25300/misq/2022/15392
- Security status: core_security_attack_defense
- Security reason: 研究核心是把暗网黑客论坛中的恶意漏洞利用程序（exploits）自动关联到已知漏洞，支持主动网络威胁情报、漏洞优先排序和风险管理，属于针对信息系统攻击（漏洞利用）的检测与防御支撑。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 
- Evaluation: 
- Algorithm reason: 提出了新的深度学习模型EVA-DSSM（结合Bi-LSTM和两种注意力机制）及DVSM度量，用Keras/TensorFlow实现，并在52,590条标注数据上对多个非DL和DL基准进行了实验评估。
- Data publicness: mixed / 暗网黑客论坛（通过Tor爬取的公开网络社区）与Securityfocus.com公开漏洞信息构成主要训练/评估数据；但案例研究使用Shodan扫描的医院和SCADA设备数据，属于公开可获取但需特定接口的信息，且部分设备IP做了匿名化。
- Decision: 该文核心问题是网络安全威胁情报中的漏洞利用自动关联，直接针对黑客恶意攻击者及其利用的系统漏洞，属于核心安全攻防；同时提出并实证评估了新算法EVA-DSSM和新度量DVSM，方法为全文核心贡献；数据来源包含公开暗网论坛与漏洞库，案例研究涉及Shodan公开设备数据。
- Confidence: 0.97

## Protecting Privacy When Sharing and Releasing Data   with Multiple Records per Person

- Year/journal: 2020 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00643
- Security status: core_security_attack_defense
- Security reason: 研究以对抗性数据使用者（adversary）利用准标识符对发布数据中的个体进行身份与敏感属性披露攻击为核心问题，提出g-balance与h-affiliation匿名化防御以降低再识别和属性披露风险，属于信息安全中的隐私披露防御。
- Algorithm status: novel_algorithm_with_evaluation
- Method: g-balance/h-affiliation 隐私匿名化算法（基于kd-tree递归划分与平衡-方差比准则）
- Evaluation: 在三个真实数据集（INFORMS患者医疗记录、MovieLens电影评分、PKDD'99银行交易）与k-anonymity、PID-based K-anonymity、l-diversity比较，报告MaxGIDR/AvgGIDR、MaxGSAR/AvgGSAR与ANE信息损失。
- Algorithm reason: 论文核心提出了新的披露风险度量与匿名化算法，并利用真实数据进行了实现和实证对比评估。
- Data publicness: public / 主要数据为公开/半公开的数据集：INFORMS Data Mining Contest 2008、MovieLens公开数据集、PKDD'99 Discovery Challenge银行数据。
- Decision: 文章核心是防止恶意数据使用者对发布数据中的个体进行再识别和敏感属性披露，提出了新的披露风险度量（g-balance、h-affiliation）及匿名化算法，并在三个真实数据集上完成了与现有方法的实证对比；数据主要来自公开数据集。
- Confidence: 0.97

## Reidentification Risk in Panel Data: Protecting for<i>k</i>-Anonymity

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1169
- Security status: core_security_attack_defense
- Security reason: 研究以恶意记录链接攻击下的面板数据重识别风险为核心，提出风险度量并开发k-匿名防御方法，直接涉及身份披露与隐私机密性保护。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 图最小移动k-匿名化（k-MM）及sno-unicity重识别风险度量
- Evaluation: 在IRI咸味零食面板数据（1009个家庭）和医生处方数据（448名医生）上实施，与聚类、记录删除、随机交换、噪声添加、聚合等基准比较，并评估品牌市场份额、SCR、品牌转换和层次贝叶斯品牌选择模型参数。
- Algorithm reason: 提出新的k-MM优化算法和sno-unicity度量，用Gurobi实现，并在两个真实面板数据集上展开实证评估和基准对比，方法贡献是全文核心。
- Data publicness: private_or_nonpublic / 主要数据来自IRI商业家庭面板数据和市场研究公司的医生处方数据，均为受协议限制的非公开商业数据。
- Decision: 文章针对恶意记录链接重识别攻击提出新的风险度量与k-匿名保护算法，属于信息系统安全（隐私披露/身份披露攻击与防御）；同时算法有实现和实证评估，故strict_include=true。数据为商业专有非公开数据。
- Confidence: 0.97

## "Brute-Force Sentence Pattern Extortion from Harmful Messages for Cyberbullying Detection"

- Year/journal: 2019 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00562
- Security status: core_security_attack_defense
- Security reason: 研究核心是检测网络欺凌（恶意行为者对用户的骚扰和羞辱，包含隐私披露等安全损害），属于针对内容操纵攻击的检测与防御。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于语言组合学的暴力搜索式句子模式提取与分类方法（Sentence Pattern Extortion）
- Evaluation: 在1,490条有害和1,508条非有害日文网络欺凌数据上进行10折交叉验证，并与SVM、SO-PMI-IR等多种基线方法比较，最优F值达0.803；同时开发Android应用进行初步测试。
- Algorithm reason: 论文提出新的模式提取和分类方法，实现了可运行系统，并通过真实数据和多重对比实验提供了实证评估。
- Data publicness: private_or_nonpublic / 数据来自日本三重县人权研究所提供并由网络巡逻志愿者标注的非公开网络欺凌语料，非公开数据集。
- Decision: 研究属于网络安全领域（网络欺凌检测，涉及恶意行为者、内容操纵和隐私披露），且核心贡献是新的算法方法并进行了实证评估，故纳入。数据来自非公开渠道。
- Confidence: 0.95

## A dynamic simulation approach to support the evaluation of cyber risks and security investments in SMEs

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113580
- Security status: core_security_attack_defense
- Security reason: 研究核心是中小企业面对网络攻击的风险评估与安全投资决策，模型模拟攻击者与防御者动态，属于信息系统安全攻防范畴。
- Algorithm status: novel_algorithm_with_evaluation
- Method: SMECRA系统动力学仿真模型（基于NIST框架的快照调查+SD模型）
- Evaluation: 三个案例场景（Alpha/Beta公司在不同威胁环境下的模拟）比较，并用配对t检验验证结果差异。
- Algorithm reason: 论文提出并实现了SMECRA系统动力学模拟工具，模型含50余个方程，并通过案例研究进行了实证评估，方法本身是核心贡献。
- Data publicness: private_or_nonpublic / 案例研究中的Snapshot Survey数据（Alpha和Beta公司）来自非公开调查，未公开提供。
- Decision: 文章面向网络攻击风险与投资决策，安全攻防是核心；提出了SMECRA系统动力学仿真模型并实现、用案例实证评估；数据为非公开调查数据。两项条件均满足，纳入。
- Confidence: 0.95

## A novel risk assessment and optimisation model for a multi-objective network security countermeasure selection problem

- Year/journal: 2012 / Decision Support Systems
- DOI: 10.1016/j.dss.2012.04.001
- Security status: core_security_attack_defense
- Security reason: 研究核心是网络风险评估与安全对策选择，以威胁-漏洞利用和CIA影响为中心，属于信息系统安全攻防与防御。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 多目标禁忌搜索算法（MOTS）与RAOM模型
- Evaluation: 使用NVD漏洞/威胁/成本示例数据，与穷举搜索（ES）比较，评估运行时间和Pareto最优解近似质量（最优解比例、欧氏距离）。
- Algorithm reason: 提出新的MOTS算法并实现了多目标对策选择优化，通过实验与ES基准比较验证效果。
- Data publicness: public / 漏洞数据来自NVD/CVE公开数据库，成本数据来自公开安全产品价格与NIST指南，威胁及匹配矩阵基于公开文献和示例表。
- Decision: 安全相关性通过：研究以网络攻击威胁、漏洞利用和CIA安全属性为核心，提出防御性对策选择；算法开发通过：提出了新的MOTS算法并实现，通过与ES的实证对比验证了解质量；数据主要来自公开数据库。
- Confidence: 0.95

## A novel steganographic algorithm using animations as cover

- Year/journal: 2008 / Decision Support Systems
- DOI: 10.1016/j.dss.2008.03.005
- Security status: core_security_attack_defense
- Security reason: 研究核心是设计一种基于动画的隐写算法，以规避被动/主动攻击者（warden）的检测和干扰，保护机密数据的隐蔽传输，属于信息系统安全攻防。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于动画概率分布匹配的编码隐写算法
- Evaluation: 在100个动画上对比Gifshuffle与animated-DIIT，评估隐藏率、CPU时间、加权MSE及安全性（旋转/缩放等攻击），结果表明所提方法在隐藏率与安全性上更优。
- Algorithm reason: 论文提出新的编码式隐写算法并实现，通过与现有隐写工具进行系统性的实验比较来验证其性能，核心贡献是算法开发与实证评估。
- Data publicness: public / 主要数据来自公开网站 http://us.bestgraph.com/ 获取的100个动画作为封面载体。
- Decision: 文章以隐写攻击与防御为核心，属安全攻防研究；提出并实现新的编码式隐写算法，并在公开数据集上实证评估；数据公开，故严格纳入。
- Confidence: 0.95

## A system dynamics model for information security management

- Year/journal: 2015 / Information & Management
- DOI: 10.1016/j.im.2014.10.009
- Security status: core_security_attack_defense
- Security reason: 研究以信息系统安全攻击（内部/外部攻击）为核心，通过系统动力学模型评估检测工具与威慑投资对攻击、损害和安全成本的影响，属于安全攻防与防御投资评估。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 信息安全管理系统动力学模型（System Dynamics Model for Information Security Management）
- Evaluation: 在Vensim PLE中运行30个月仿真，比较不同安全工具投资和威慑投资共25种场景，并进行了结构验证、极端条件分析、敏感性与扰动分析。
- Algorithm reason: 论文核心贡献是开发并实证评估了一个新的系统动力学仿真模型，用于信息安全管理策略分析，包含实现和系统化的场景仿真验证。
- Data publicness: unclear / 无外部真实数据集，主要基于人为设定的模型参数和仿真生成数据。
- Decision: 安全相关性高：恶意攻击者是研究核心，聚焦检测、防御和投资评估；算法开发：核心贡献是系统动力学仿真模型，已实现并有全面的仿真评估；数据为仿真参数，公开性不明但不影响纳入。
- Confidence: 0.95

## An approach to finding the cost-effective immunization targets for information assurance

- Year/journal: 2014 / Decision Support Systems
- DOI: 10.1016/j.dss.2014.08.002
- Security status: core_security_attack_defense
- Security reason: 研究以企业信息网络中的病毒、恶意代码和谣言等威胁传播为核心，提出免疫目标选择方法以降低感染损失和成本，核心是威胁传播的防御与缓解。
- Algorithm status: novel_algorithm_with_evaluation
- Method: CEIT（Cost-Effective Immunization Targets）算法，基于savability度量和bond percolation的贪婪免疫目标选择方法
- Evaluation: 在EUMail、GDMB、CCMP三个真实信息网络上与Target、Betweenness、DegreeDiscount等策略比较感染损失，另有实际教育机构邮件网络案例研究
- Algorithm reason: 提出新的免疫目标选择算法，包含savability评价函数和bond percolation加速的期望感染概率估计，并在真实数据集上进行了系统比较和实证评估。
- Data publicness: mixed / 实验主要使用三个网络数据集：EUMail和CCMP为公开数据集，GDMB为中国南方移动运营商内部博客网络（非公开），案例研究使用某教育机构内部邮件日志（非公开）。
- Decision: 安全相关性：企业信息网络中病毒和恶意信息传播是典型的信息系统安全威胁，研究目标是免疫防御和损失缓解，符合核心安全攻防定义。算法开发：论文提出并实现CEIT算法，包含savability和bond percolation创新，并通过真实数据实验和案例研究进行了实证评估。数据公开性：公开数据集与非公开企业/机构数据混合。
- Confidence: 0.95

## Anonymizing and Sharing Medical Text Records

- Year/journal: 2017 / Information Systems Research
- DOI: 10.1287/isre.2016.0676
- Security status: core_security_attack_defense
- Security reason: 研究核心是防止医学文本共享中的患者重识别（身份披露），对抗行为者（data intruder）通过准标识符链接识别个体，属于信息系统隐私保护与攻击防御范畴。
- Algorithm status: novel_algorithm_with_evaluation
- Method: DAST（Deidentification and Anonymization for Sharing medical Texts）：递归NMF文档聚类 + 值枚举匿名化（含drill-down）
- Evaluation: 在i2b2三个真实临床文本数据集（Medication、Obesity、VA）上，与HIPAA Safe Harbor和k-anonymity比较再识别风险与数据效用（计数查询、大项集、搜索查询），并报告统计显著性。
- Algorithm reason: 提出新的去标识化/匿名化框架，包含递归NMF聚类和值枚举方法，原型实现并有系统的实证评估，方法是核心贡献而非现成工具。
- Data publicness: public / i2b2项目公开提供的研究用临床文档数据集（Medication、Obesity、VA），可从i2b2网站获取。
- Decision: 安全相关：以对抗性数据入侵者重识别隐私披露为核心，聚焦医学文本共享的隐私保护与去标识化；算法开发：提出DAST新框架（递归NMF聚类+值枚举匿名化）并实现原型，基于真实数据进行了与Safe Harbor和k-anonymity的实证比较；数据来源于i2b2公开研究数据集。
- Confidence: 0.95

## Are social bots a real threat? An agent-based model of the spiral of silence to analyse the impact of manipulative actors in social networks

- Year/journal: 2019 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2018.1560920
- Security status: core_security_attack_defense
- Security reason: 全文以名为social bots的对抗性自动化账户为核心，研究其对社交媒体舆论气候的内容操纵与影响，威胁评估服务于对这类操纵攻击的理解与防御。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于网络拓扑的沉默螺旋多智能体模型（Agent-Based Model）
- Evaluation: 在NetLogo中实现并运行模拟，通过与既有理论、实证发现及先前模型对比验证网络密度、中心节点影响和收敛速度，并系统变化bot比例、网络密度、连边策略和bot影响因子进行敏感性分析。
- Algorithm reason: 论文提出并实证评估了一个新的agent-based模拟方法，模型贡献是全文核心，而非工具性应用。
- Data publicness: unclear / 无外部真实数据源，主要数据均由agent-based仿真生成。
- Decision: 文章研究对抗性social bots对社交媒体舆论操纵的影响，属于内容操纵与虚假信息传播的安全威胁评估；同时提出并实证评估了新的agent-based模型（核心算法贡献），故纳入。数据为仿真生成，公开性不明确。
- Confidence: 0.95

## Creating Proactive Cyber Threat Intelligence with Hacker Exploit Labels: A Deep Transfer Learning Approach

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2023/17316
- Security status: core_security_attack_defense
- Security reason: 该研究以黑客论坛中的恶意漏洞利用代码为对象，旨在自动标记漏洞利用以支持主动网络威胁情报，属于信息系统安全攻防核心领域。
- Algorithm status: novel_algorithm_with_evaluation
- Method: DTL-EL（Deep Transfer Learning Exploit Labeler，深度迁移学习漏洞利用标签器）
- Evaluation: 使用收集的96,333条带标签漏洞利用（源域）和4,842条黑客论坛漏洞利用（目标域）进行实验，与经典机器学习、深度学习、其他迁移学习方法比较，以准确率、精确率、召回率和F1评估。
- Algorithm reason: 论文提出并实现了新的深度迁移学习模型DTL-EL，包含预初始化、多层迁移和自注意力机制，并通过四个基准实验验证了其性能优势。
- Data publicness: public / 主要数据来自公开渠道：9个黑客论坛、1个漏洞利用暗网市场（0day.today）和6个公共漏洞库（如ExploitDB、PacketStorm等）。
- Decision: 该文核心是开发并实证评估了新的深度迁移学习算法DTL-EL，用于自动标记黑客论坛中的漏洞利用，直接服务于网络安全威胁检测与防御，完全符合安全相关和算法开发标准。数据来源为公开渠道。
- Confidence: 0.95

## Dare to share: Protecting sensitive knowledge with data sanitization

- Year/journal: 2007 / Decision Support Systems
- DOI: 10.1016/j.dss.2006.08.007
- Security status: core_security_attack_defense
- Security reason: 研究核心是数据共享环境中的敏感知识保护，防止敏感关联规则被数据挖掘泄露，属于数据净化/防泄露防御方法。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 三种数据净化启发式方法：Aggregate、Disaggregate、Hybrid
- Evaluation: 在FIMI公开数据集（retail、bms1、bms2、chess、mushroom）上，与Sliding Window Algorithm（SWA）比较数据效用、准确性与CPU时间
- Algorithm reason: 提出三种新的数据净化启发式算法并在公开真实数据集上实证评估，方法贡献为核心。
- Data publicness: public / FIMI仓库的retail、bms1、bms2、chess、mushroom公开数据集（源自UCI、KDD Cup等公开渠道）
- Decision: 本文研究数据共享环境中敏感关联规则的披露防御，属于信息安全领域的知识泄露防护；核心贡献是提出三种数据净化启发式方法并在公开真实数据集上实证评估，严格纳入。
- Confidence: 0.95

## Detecting Review Manipulation on Online Platforms with Hierarchical Supervised Learning

- Year/journal: 2018 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2018.1440758
- Security status: core_security_attack_defense
- Security reason: 研究核心是检测在线评论平台上的虚假评论者（opinion spammers），属于内容操纵攻击的检测；恶意行为者（意见垃圾信息发送者）是问题核心，损害平台信息真实性与可信度。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于分布变换的层级监督学习（分布堆叠元分类器）
- Evaluation: 使用Yelp餐厅评论（约26万用户）和医院评论（1,235条）数据集，以5折交叉验证评估多个分类器（Logistic回归、SVM、kNN等），并与标准化特征基线和先前方法比较，AUC达0.817。
- Algorithm reason: 提出用单变量/多变量分布的概率密度变换特征并堆叠成元分类器的新特征工程方法，实现并开展多数据集实证评估，核心贡献是算法本身。
- Data publicness: public / Yelp公开评论数据（餐厅与医院评论），可公开获取/爬取。
- Decision: 该文研究在线评论操纵/虚假评论者检测，属于内容操纵攻击的检测与防御（安全相关性通过）；提出新的基于分布变换的层级监督学习方法，并基于公开Yelp数据进行了多分类器实证评估（算法开发通过）；数据为公开数据。
- Confidence: 0.95

## Digression and Value Concatenation to Enable Privacy-Preserving Regression

- Year/journal: 2012 / MIS Quarterly
- DOI: 10.25300/misq/2014/38.3.03
- Security status: core_security_attack_defense
- Security reason: 研究核心是防范'回归攻击'这一隐私披露攻击：恶意数据使用者利用回归树推断个体敏感属性，论文提出以Δ-digression度量和EDP剪枝为核心的MART匿名化防御方法，属于对隐私披露/属性推断攻击的检测与防御。
- Algorithm status: novel_algorithm_with_evaluation
- Method: MART（基于回归树的多变量匿名化方法）：Δ-digression披露风险度量、误差-离差剪枝（EDP）算法、动态值连接（value concatenation）方法
- Evaluation: 在Offer、Alcohol、Credit、Census四个真实数据集上与回归Mondrian（RM）和传统k-匿名算法比较，以RSD衡量隐私披露风险、以线性回归和回归树的MAPE衡量数据效用，并采用10折或2折交叉验证。
- Algorithm reason: 论文提出新的计算方法并作为核心贡献：新的披露风险度量、剪枝算法和值连接匿名化方法，且通过实验进行了实证评估。
- Data publicness: mixed / Offer数据来自AIS公开薪酬调查，Credit和Census数据来自UCI公开库；Alcohol数据取自Kenkel & Terza (2001)，全文未明确其公开获取途径，故整体为公开与来源不明确数据混合。
- Decision: 安全相关：论文以隐私披露攻击（回归攻击）为研究核心，目标是防御对敏感个人属性的推断和数据泄露；算法开发：核心贡献是新的MART算法体系（digression度量、EDP剪枝、动态值连接），并在多个真实数据集上进行了实证评估；数据公开性：部分数据公开（UCI、AIS），Alcohol来源公开性不明确，仅记录为mixed，不影响纳入。
- Confidence: 0.95

## Discovering Emerging Threats in the Hacker Community: A Nonparametric Emerging Topic Detection Framework

- Year/journal: 2022 / MIS Quarterly
- DOI: 10.25300/misq/2022/15642
- Security status: core_security_attack_defense
- Security reason: 研究核心是从暗网黑客社区流中检测新兴威胁主题，以支持主动网络防御和威胁情报，对抗行为者（黑客/网络罪犯）及其攻击信息是研究问题本身的核心对象。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 
- Evaluation: 
- Algorithm reason: 提出并实现了非参数新兴主题检测（NPETD）框架，扩展条件HDP并结合随机变分推断与Bayes因子检验，在darknet marketplaces和Altenens论坛数据上与AOLDA、ATD、TopicSketch、BBTM等基线进行了实证比较。
- Data publicness: mixed / Alphabay darknet marketplace listings（2014-2016）和Altenens黑客论坛帖子（2018-2020）；dark web黑客社区数据通常需通过特定渠道获取，不属于常规公开数据集，但作者描述了采集和预处理过程，未明确说明数据是否完全公开可获取。
- Decision: 安全相关性：研究对象是dark web黑客社区中的网络犯罪/攻击内容，核心是检测新兴威胁主题以支持主动网络防御，属于信息系统安全攻防检测；算法开发：提出NPETD框架（条件HDP+SVI+Bayes因子检验）并实现，在黑客社区数据集上与多个基线进行了实证评估；数据公开性：Alphabay和Altenens等dark web数据为非完全公开渠道，记录为mixed。
- Confidence: 0.95

## Estimating the impact of IT security incidents in digitized production environments

- Year/journal: 2019 / Decision Support Systems
- DOI: 10.1016/j.dss.2019.113144
- Security status: core_security_attack_defense
- Security reason: 文章核心是模拟和分析网络攻击（如可用性攻击）在数字化生产环境信息网络中的传播及其对IT服务和生产的可用性损害，属于信息系统安全的攻击建模与风险评估/防御支持。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于贝叶斯网络与贝叶斯攻击图的IT可用性事件影响评估模型
- Evaluation: 实现为R/gRain软件原型，对随机生成的DPE网络进行敏感性分析，并在德国一家制造企业的真实生产网络案例中应用和验证。
- Algorithm reason: 论文提出并实现了可运行的贝叶斯网络/攻击图模型，将攻击传播与损害传播整合，并通过仿真敏感性分析和真实案例进行实证评估，方法贡献是核心。
- Data publicness: private_or_nonpublic / 主要评估数据为随机生成的模拟DPE网络数据，以及一家德国制造企业的内部生产与IT网络案例数据（非公开）；模型参数多基于文献估计。
- Decision: 文章以网络攻击/可用性事件为研究核心，目标是评估其对IT服务可用性和生产价值创造的影响，属于信息系统安全风险评估；同时提出了新的基于贝叶斯网络/攻击图的计算模型并实现为R原型，通过仿真、敏感性分析和真实案例进行了实证评估，因此纳入。数据公开性虽偏向非公开，但不影响纳入判定。
- Confidence: 0.95

## Exploring Emerging Hacker Assets and Key Hackers for Proactive Cyber Threat Intelligence

- Year/journal: 2017 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2017.1394049
- Security status: core_security_attack_defense
- Security reason: 研究以黑客论坛中的恶意工具（crypters、keyloggers、SQL注入等）为主要对象，目标是识别攻击者资产与关键黑客以支持主动网络威胁情报，核心是面向信息系统攻击的检测、识别与防御。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于Web/文本/数据挖掘与LDA、SVM、二部图社会网络分析的主动CTI框架
- Evaluation: 在7个黑客论坛收集431,518帖，使用SVM分类器与LDA主题建模，对分类器进行十折交叉验证和配对t检验，通过困惑度选择主题数并用六位专家评分验证，最后构建二部图社会网络识别关键黑客。
- Algorithm reason: 论文构建了从论坛采集、挖掘恶意资产并识别关键黑客的完整计算方法框架，包含SVM分类与LDA主题建模等实现，并在大规模真实论坛数据上进行了实证评估。
- Data publicness: unclear / 数据来自7个公开可访问的英文和俄语黑客论坛，但未明确说明原始论坛是否完全公开可获取，且涉及使用论坛凭据和Tor抓取，公开性存在不确定性。
- Decision: 安全相关性：研究核心是针对黑客论坛恶意工具和关键黑客的威胁识别与防御，属于主动网络威胁情报的安全攻防研究；算法开发：提出并实现了包括数据采集、SVM分类、LDA主题建模、二部图社会网络分析在内的完整计算方法框架，并在大规模论坛数据上进行了实证评估；数据公开性：数据来自多个论坛，但公开获取程度不完全明确，记录为unclear不影响纳入。
- Confidence: 0.95

## Extracting and reasoning about implicit behavioral evidences for detecting fraudulent online transactions in e-Commerce

- Year/journal: 2016 / Decision Support Systems
- DOI: 10.1016/j.dss.2016.04.003
- Security status: core_security_attack_defense
- Security reason: 研究核心是检测电商中由攻击机构和串谋买家发起的虚假交易攻击，此类攻击操纵平台评分系统的完整性，属于针对信息系统的对抗性滥用，论文聚焦于攻击行为的检测与防御。
- Algorithm status: novel_algorithm_with_evaluation
- Method: Dempster–Shafer强化组合（DSRC）证据融合算法、基于遗传算法（GA）的证据参数优化、证据阈值自动估计算法（Algorithm 1）
- Evaluation: 在真实淘宝蜜罐数据（8885笔交易、139864个买家、215844条行为日志）上，与DS(e)、Suvasini、Dong等基线比较，报告TPR/FPR/lam/AUC并做配对t检验
- Algorithm reason: 论文提出并实现了新的DSRC融合方法、GA参数搜索和特征阈值算法，并通过大规模实验和统计检验验证了其有效性，方法贡献是全文核心。
- Data publicness: public / 论文声明数据集和源码可从项目网站获取，虽然数据通过蜜罐自行收集，但发表时可公开下载。
- Decision: 安全相关：论文针对电商中恶意攻击机构发起的串谋虚假交易攻击，该攻击通过操纵评分系统破坏平台完整性与真实性，研究核心为攻击检测，非一般金融欺诈。算法开发：提出新的DSRC证据融合算法、GA参数优化和证据阈值算法，并在真实数据集上进行了实证评估。数据公开性：作者声明数据集和代码通过项目网站公开提供。综上满足纳入条件。
- Confidence: 0.95

## Fame for sale: Efficient detection of fake Twitter followers

- Year/journal: 2015 / Decision Support Systems
- DOI: 10.1016/j.dss.2015.09.003
- Security status: core_security_attack_defense
- Security reason: 论文核心是检测恶意创建的虚假Twitter关注者（fake followers），其行为是对社交平台真实性和完整性的滥用，属于信息系统安全中的滥用检测与防御。
- Algorithm status: novel_algorithm_with_evaluation
- Method: Class A轻量级分类器（基于低成本特征的机器学习检测模型）
- Evaluation: 在自建的BAS数据集（3900个账户）上进行10折交叉验证，并在随机采样账户和Obama粉丝两个独立测试集上验证，与多种机器学习分类器比较，准确率超过95%。
- Algorithm reason: 论文设计并实现了基于Class A（仅需profile特征）的轻量级分类器，通过成本分析和特征选择形成新模型，并通过多组实验实证评估其检测性能。
- Data publicness: public / 主要数据来自Twitter公开API爬取的账户、推文和关系数据，且作者将基线数据集（TFP、E13、FAK等）公开提供给科学社区。
- Decision: 论文以检测恶意虚假Twitter关注者为核心，属于社交平台滥用检测的安全研究；同时提出并实证评估了新的轻量级机器学习分类器，满足算法开发条件；数据集公开，不影响纳入。
- Confidence: 0.95

## Fraudulent review detection model focusing on emotional expressions and explicit aspects: investigating the potential of feature engineering

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113728
- Security status: core_security_attack_defense
- Security reason: 研究核心是针对在线评论系统中欺诈性评论/意见垃圾（opinion spamming）的检测，属于内容操纵攻击的防御，损害的是评论真实性与系统完整性。
- Algorithm status: novel_algorithm_with_evaluation
- Method: M-SMOTE（改进的SMOTE过采样算法）与基于特征工程/分布变换的欺诈评论检测框架
- Evaluation: 在Yelp真实评论数据集（5044家餐厅、260277名评论者）及Amazon、UCI等基准数据集上，与SMOTE、LR-SMOTE及多种ML基线分类器比较，报告了精确率、召回率、F1和AUC，并优于已有研究（如Feng et al., Akoglu et al., Rayana & Akoglu, Kumar et al.等）。
- Algorithm reason: 论文提出了新的M-SMOTE算法及新型特征工程方法作为核心贡献，并在多个公开数据集上进行了实证评估和基准比较，满足新算法+实证评估条件。
- Data publicness: public / 主要数据来自Yelp公开数据集（Rayana & Akoglu收集）、Amazon公开数据集及UCI机器学习仓库数据集，均可在公开渠道获取。
- Decision: 文章核心是开发并实证评估了M-SMOTE算法与特征工程方法用于检测在线评论操纵（欺诈性评论/意见垃圾），属于内容操纵攻击的检测与防御，损害对象为评论系统的真实性和完整性，属于信息系统安全领域；同时提出了新的计算方法并有充分实证评估，故strict_include=true。
- Confidence: 0.95

## Hiding Sensitive Information when Sharing Distributed Transactional Data

- Year/journal: 2020 / Information Systems Research
- DOI: 10.1287/isre.2019.0898
- Security status: core_security_attack_defense
- Security reason: 研究核心是在共享事务数据前隐藏敏感频繁项集，防止敏感商业信息泄露，属于数据净化/脱敏防御，保护组织机密性。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于拉格朗日松弛直觉的集成方法（Ensemble Approach），包括PartitionsFirst和OrgFirst两个松弛过程及合并步骤
- Evaluation: 在Retail和BMS-POS公开数据集以及IBM Quest生成的最大5亿事务合成数据集上，与最优解及Verykios等方法比较，并评估净化后推荐精度；结果显示接近最优、可扩展性强。
- Algorithm reason: 提出新的分布式频繁项集隐藏求解方法，实现了完整算法，并通过大规模计算实验和推荐质量实验验证了有效性。
- Data publicness: mixed / 小规模实验使用公开FIMI仓库的Retail和BMS-POS数据集；大规模实验使用IBM Quest生成器自造的合成数据。
- Decision: 文章聚焦共享事务数据前的敏感项集隐藏，属于信息机密性保护的净化防御技术，满足安全相关性；提出并实现新的集成求解算法，基于真实与合成数据进行了充分实证评估，满足算法开发要求；数据为公开真实数据与合成数据混合。
- Confidence: 0.95

## Identifying and Profiling Key Sellers in Cyber Carding Community: AZSecure Text Mining System

- Year/journal: 2016 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2016.1267528
- Security status: core_security_attack_defense
- Security reason: 研究针对地下carding论坛中的关键卖家（销售被盗卡信息和恶意软件的恶意行为者），通过文本挖掘识别和画像，直接服务于网络安全取证与犯罪预防，属于信息安全攻防检测核心。
- Algorithm status: novel_algorithm_with_evaluation
- Method: AZSecure文本挖掘系统（深度学习RNN情感分析 + LDA主题建模，结合MaxEnt线程分类）
- Evaluation: 在8个地下经济论坛上，对线程分类、评论情感、卖家画像三个任务与SVM、NB、kNN、N-gram等基准方法比较，平均F-measure约80%-90%，并以Rescator案例验证。
- Algorithm reason: 论文提出并实现了AZSecure系统，组合和改进了多种文本挖掘技术用于识别和画像关键卖家，并通过实验与基准方法对比验证了核心方法贡献。
- Data publicness: private_or_nonpublic / 8个匿名化的国际carding论坛数据，需反爬措施获取，论坛名称被隐去，数据不公开可复现。
- Decision: 安全相关性：恶意或对抗行为者（carding卖家和地下经济参与者）是研究核心，损害对象为支付数据与信息系统安全，研究聚焦检测、画像与威胁情报，非单纯财务欺诈。算法开发：提出并实现AZSecure系统，核心贡献是新的文本挖掘组合方法，并有三项实验和案例研究的实证评估。数据为地下论坛秘密收集，不可公开复现。故纳入。
- Confidence: 0.95

## Impact of Network Structure on Malware Propagation: A Growth Curve Perspective

- Year/journal: 2016 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2016.1172440
- Security status: core_security_attack_defense
- Security reason: 研究以恶意软件（病毒/蠕虫）传播为核心，分析传播动态并模拟免疫、对策传播和安全意识等防御策略，属于信息系统安全攻击与防御研究。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 结构风险模型（structural risk model）
- Evaluation: 使用真实MySpace社交网络与大学技术网络结构，进行200,000次恶意软件传播模拟，拟合广义逻辑增长曲线（中位R²=0.998），并用层次回归评估网络结构对传播动态的影响，同时模拟三种防御策略与基线对比。
- Algorithm reason: 提出并实现了新的结构风险模型，将网络结构特征（随机游走介数、组大小、网络类型）与恶意软件传播动态（增长曲线四参数）关联，并通过大规模仿真和实证回归验证，是全文核心贡献。
- Data publicness: mixed / 社交网络数据来自MySpace公开用户（15,276名公开用户），技术网络数据来自某大学内部校园网络结构，后者非公开渠道。
- Decision: 文章以恶意软件传播与防御为核心安全议题，提出了基于网络结构的风险模型，并通过大规模仿真与实证回归进行了评估，同时模拟了防御策略，因此同时满足安全相关性和算法开发条件；数据公开性为混合，但不影响纳入。
- Confidence: 0.95

## Protecting Privacy Against Record Linkage Disclosure: A Bounded Swapping Approach for Numeric Data

- Year/journal: 2011 / Information Systems Research
- DOI: 10.1287/isre.1100.0289
- Security status: core_security_attack_defense
- Security reason: 文章针对记录链接重识别攻击提出匿名化数据掩码方法，直接作用于隐私披露攻击的防御，属于信息系统安全中的隐私保护与披露防御。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 多变量交换树（multivariate swapping trees）/双界交换方法
- Evaluation: 在三个真实数据集（AIS教师薪资、美国人口普查、房屋数据）与多种模拟数据上，与微聚合、单变量扰动树等方法比较，采用记录链接率、ABISD、ABICO、回归/神经网络MAPE等指标进行五折交叉验证实验。
- Algorithm reason: 提出新的数据掩码算法（多变量交换树）并实现了详细实证评估，算法为核心贡献而非辅助工具。
- Data publicness: public / 主要数据来自公开渠道：AIS教师薪资调查网站、美国人口普查局数据网站、Torgo房屋数据集；模拟数据基于公开参数生成。
- Decision: 安全相关性成立：论文核心是防御记录链接重识别攻击（恶意对抗者存在，损害隐私披露安全属性）；算法开发成立：提出新的数据掩码算法并进行了充分实证评估；数据来源为公开数据。
- Confidence: 0.95

## Releasing Individually Identifiable Microdata with Privacy Protection Against Stochastic Threat: An Application to Health Information

- Year/journal: 2007 / Information Systems Research
- DOI: 10.1287/isre.1070.0112
- Security status: core_security_attack_defense
- Security reason: 本文针对微观数据发布中用户利用统计信息推断被抑制机密字段的随机威胁（stochastic threat），研究核心是设计数据重编码与通道扩展方法以预防机密性披露，属于信息系统安全中的数据隐私与属性推断防御。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 通道扩展（Channel Expansion）与线性规划最优化数据发布方法
- Evaluation: 在1百万条记录、200个输入通道的合成数据集上，变化风险比例和风险容忍度RT，使用CPLEX求解LP模型，比较数据效用损失（Ω）与风险容忍度、风险比例之间的关系；另通过改变输出通道数量分析效益递减。
- Algorithm reason: 核心贡献是提出新的数据发布安全方法，将输入通道重编码为输出通道并构建线性规划模型，实现最小信息损失下的机密性保护，且通过大规模计算实验验证了实用性与可行性。
- Data publicness: private_or_nonpublic / 作者内部生成的1百万条记录、200个输入通道的合成模拟数据集，非公开渠道来源。
- Decision: 安全相关方面，文章针对数据发布场景中的用户统计推断攻击（属性推断/披露攻击）主动设计防御性数据转换方法，以保护机密性的安全属性；算法开发方面，提出了新的通道扩展+线性规划方法，方法被实现并用大规模合成数据进行了实证评估；数据公开性为私有合成数据，不影响纳入判定。
- Confidence: 0.95

## Secure federation of semantic information services

- Year/journal: 2013 / Decision Support Systems
- DOI: 10.1016/j.dss.2012.05.049
- Security status: core_security_attack_defense
- Security reason: 文章核心是保护语义信息联邦的信息安全，通过SemForce访问控制、认证和加密等措施，防止未授权访问和篡改，属于信息系统安全攻防范畴。
- Algorithm status: novel_algorithm_with_evaluation
- Method: SemForce（语义感知访问控制执行与决策系统）、Aletheia-SSO（联邦认证）、BPAX（跨域角色与策略工程转换器）
- Evaluation: 在Amazon EC2分布式环境上用真实工业本体数据（1000/10000/100000实例）进行了多组性能实验，比较了有无SemForce和TLS保护下的响应时间，并测试了并发请求；结果显示安全开销可接受。
- Algorithm reason: 文章提出并实现了SemForce查询重写访问控制、Aletheia-SSO联邦认证以及BPAX策略工程方法，并进行分布式性能实验评估，属于新方法且核心贡献为算法/系统开发。
- Data publicness: private_or_nonpublic / 实验数据来自Aletheia项目合作伙伴的真实工业本体数据，并在作者控制的Amazon EC2实例上构建的实验数据集，不来自公开数据集或公开渠道。
- Decision: 安全方面：文章核心是防止对信息联邦中语义信息服务的未授权访问和篡改，恶意/对抗威胁包括外部窃听、篡改、未授权访问和内部越权，损害信息安全属性（机密性和完整性），属于信息系统安全攻防。算法方面：核心贡献是设计并实现了SemForce访问控制机制、Aletheia-SSO认证和BPAX策略生成方法，并以分布式性能实验进行实证评估，符合新算法并有实证评估。数据来自项目合作伙伴和实验部署，非公开渠道。
- Confidence: 0.95

## Selection of optimal countermeasure portfolio in IT security planning

- Year/journal: 2013 / Decision Support Systems
- DOI: 10.1016/j.dss.2013.01.001
- Security status: core_security_attack_defense
- Security reason: 研究核心是选择IT安全对策组合以预防或缓解网络攻击，针对成功网络攻击的损失和系统安全属性，属于安全攻防与风险管理。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 
- Evaluation: 
- Algorithm reason: 提出基于CVaR和混合整数规划的安全对策组合选择模型，并用AMPL/Gurobi实现，通过数值算例和计算实验验证。
- Data publicness: public / 数值示例数据基于公开的IT安全论坛威胁集（EndpointSecurity.org）及文献[20]的参数，非私有数据。
- Decision: 文章聚焦IT安全规划中针对网络攻击的对策选择，属于安全攻防；核心贡献为新的混合整数规划/CVaR优化方法，并有实现和数值计算实验；数据来自公开来源，不改变纳入判断。
- Confidence: 0.95

## Semi-Supervised Cyber Threat Identification in Dark Net Markets: A Transductive and Deep Learning Approach

- Year/journal: 2020 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2020.1790186
- Security status: core_security_attack_defense
- Security reason: 研究核心是在暗网市场中识别恶意网络威胁商品（黑客工具、勒索软件、数据泄露、被盗账户等），属于网络威胁情报与威胁检测，直接针对信息系统安全属性。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 结合启发式与TSVM的半监督标注算法+双向LSTM威胁识别框架（Algorithm 1）
- Evaluation: 在79,434条DNM商品描述上，与kNN、LR、RF、SVM、CNN、LSTM、TSVM等基准比较，F1达到89.55%，10折交叉验证并进行了t检验。
- Algorithm reason: 论文提出了新的半监督标注与深度LSTM识别方法，并实现了可运行模型，在大型DNM数据集上完成了实证评估。
- Data publicness: public / 暗网市场爬虫采集的商品描述数据，论文声明数据集公开于GitHub：https://github.com/mohammadrezaebrahimi/JMIS-DarkNetMarketData
- Decision: 安全相关：核心是检测暗网市场中的网络攻击工具、恶意软件、泄露数据等网络威胁，恶意商家行为直接危害系统与用户安全，且检测/防御是研究焦点；算法开发：提出了TSVM半监督标注+双向LSTM威胁识别新方法，并实现和在大规模数据集上进行了实证对比；数据公开性：数据集声明公开于GitHub。因此strict_include=true。
- Confidence: 0.95

## Short Term and Total Life Impact analysis of email worms in computer systems

- Year/journal: 2007 / Decision Support Systems
- DOI: 10.1016/j.dss.2006.12.014
- Security status: core_security_attack_defense
- Security reason: 研究以邮件蠕虫这一恶意代码为对象，开发影响分类与预测框架，直接服务安全威胁评估、防御响应和资源分配，损害对象是系统安全属性。
- Algorithm status: novel_algorithm_with_evaluation
- Method: TLI/STI邮件蠕虫影响分类与预测框架（含Tskewness、LMH、hit density等指标）
- Evaluation: 基于93个真实邮件蠕虫数据，通过卡方独立性检验、相关性分析、匹配率和GSI相似性指标进行了实证验证。
- Algorithm reason: 提出了两个新的影响分类与预测框架（TLI、STI）及Tskewness等新指标，并在真实蠕虫数据上实现和验证，属于新颖计算分类方法并有实证评估。
- Data publicness: public / Symantec和Messagelabs网站上公开的93个邮件蠕虫感染记录（2003-2004）。
- Decision: 安全相关：邮件蠕虫属于恶意代码攻击，研究聚焦其影响分类和早期预测，直接支持威胁评估和防御响应，损害对象为系统可用性、数据保密性等安全属性。算法开发：提出了TLI/STI两个分类预测框架及多个新指标（TSKI、LMH等），并基于93个真实蠕虫数据进行实证验证。数据公开性：数据来自公开网站，属于公开数据。
- Confidence: 0.95

## Socially optimal IT investment for cybersecurity

- Year/journal: 2019 / Decision Support Systems
- DOI: 10.1016/j.dss.2019.05.009
- Security status: core_security_attack_defense
- Security reason: 论文针对恶意网络攻击（恶意代码、网络攻击、钓鱼、DoS、僵尸网络等）建模，以最小化包含信息泄露等外部性的社会成本为目标，优化预防与检测/遏制防护措施的投资组合，核心是安全防御与缓解的资源优化。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 
- Evaluation: 
- Algorithm reason: 提出并实现了基于椭球不确定集的鲁棒优化模型（含线性化与可求解的锥二次规划形式），并通过案例数据进行了25个确定性场景和54个鲁棒测试实例的实证评估。
- Data publicness: public / 主要数据来自Ponemon Institute公开研究报告、德国BSI IT-Grundschutz公开目录等公开来源。
- Decision: 安全相关：研究核心是防御网络攻击的防护措施配置优化，威胁与损害对象为信息系统安全属性；算法开发：提出并实现了新的鲁棒优化模型，有案例实证评估；数据公开性：主要数据来自公开报告和公开知识库。因此strict_include为true。
- Confidence: 0.95

## Software Diversity for Improved Network Security: Optimal Distribution of Software-Based Shared Vulnerabilities

- Year/journal: 2017 / Information Systems Research
- DOI: 10.1287/isre.2017.0722
- Security status: core_security_attack_defense
- Security reason: 研究针对恶意软件（病毒/蠕虫）利用软件漏洞在网络中的传播与防御，核心是软件多样性策略以提升网络对安全攻击的弹性，属于信息系统安全攻防范畴。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 软件多样性最优分配模型（LP1/LP2）、基于信息论的软件多样性指数（SDI）、动态软件分配算法（Algorithm 3）、扩展SIS病毒传播仿真模型
- Evaluation: 在合成scale-free网络上，通过CPLEX求解LP模型，并与targeted distribution策略比较SDI和epidemic threshold，基于20次重复模拟评估。
- Algorithm reason: 论文核心贡献是提出新的组合优化模型和病毒传播仿真模型，并实现与系统化实验评估，而非仅用现成算法作为分析工具。
- Data publicness: private_or_nonpublic / 主要数据为生成的scale-free网络（Barabási-Albert模型）和合成的软件-漏洞矩阵，无公开数据集，全部由研究构建。
- Decision: 文章以恶意软件利用共享漏洞传播为安全威胁，提出并实证评估软件多样性的优化分配模型，安全相关与算法开发条件均满足；数据为模拟生成的非公开数据。
- Confidence: 0.95

## SpamHunting: An instance-based reasoning system for spam labelling and filtering

- Year/journal: 2007 / Decision Support Systems
- DOI: 10.1016/j.dss.2006.11.012
- Security status: core_security_attack_defense
- Security reason: 论文以垃圾邮件对电子邮件系统的滥用和对抗性躲避为研究问题，核心贡献是垃圾邮件的自动检测与过滤，属于对信息系统可用性/完整性威胁的防御。
- Algorithm status: novel_algorithm_with_evaluation
- Method: SpamHunting：基于增强实例检索网络（EIRN）的实例推理垃圾邮件过滤系统
- Evaluation: 在公开SpamAssassin语料（2002-2003）上进行10折分层交叉验证，与SVM、Naïve Bayes、Adaboost、ECUE等模型比较，采用%OK、%FP、%FN、召回率、精确率、TCR和运行时间等指标。
- Algorithm reason: 文章提出新的EIRN记忆结构、加权距离与投票机制，并实现为可运行的垃圾邮件过滤系统，通过公开语料实验验证了其性能优势。
- Data publicness: public / 主要使用公开的SpamAssassin公共语料库（http://www.spamassassin.org/publiccorpus/），2002年和2003年邮件集。
- Decision: 安全相关性：垃圾邮件被视为对电子邮件系统完整性/可用性的对抗性滥用，研究核心是垃圾邮件的检测与过滤；算法开发：提出并实现EIRN实例推理垃圾邮件过滤方法，并用公开语料进行了实证比较评估；数据公开性：主要数据来自公开SpamAssassin语料。
- Confidence: 0.95

## The Impact of Fake Reviews on Online Visibility: A Vulnerability Assessment of the Hotel Industry

- Year/journal: 2016 / Information Systems Research
- DOI: 10.1287/isre.2016.0674
- Security status: core_security_attack_defense
- Security reason: 研究以虚假评论注入攻击为核心，明确将竞争性商家视为恶意攻击者，攻击目标是操纵在线评论平台的排名与信息真实性，并系统研究攻击模拟、脆弱性评估与防御策略，属于信息系统内容操纵与虚假信息攻击范畴。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于可见性度量的虚假评论攻击脆弱性评估框架（含可见性概率模型、排名函数估计与DelayIndex抗欺诈排名函数）
- Evaluation: 基于TripAdvisor 2.3M+评论、4,709家酒店、17个城市的数据，比较平均评分与PopularityIndex在不同考虑模型下的攻击成功率，并评估DelayIndex的防御效果。
- Algorithm reason: 论文核心贡献是提出并实现了新的可见性度量框架、攻击策略模拟与抗欺诈排名函数，并通过大规模真实数据进行实证评估。
- Data publicness: public / 主要数据来自公开的TripAdvisor.com评论数据，以及用于虚假评论分布分析的Yelp.com公开评论数据。
- Decision: 文章明确研究虚假评论攻击对酒店在线可见性的影响，提出并实证评估了可见性度量框架、攻击策略与抗欺诈排名算法，符合核心安全攻防与新算法开发要求；数据来自公开评论平台。
- Confidence: 0.95

## The Phishing Funnel Model: A Design Artifact to Predict User Susceptibility to Phishing Websites

- Year/journal: 2021 / Information Systems Research
- DOI: 10.1287/isre.2020.0973
- Security status: core_security_attack_defense
- Security reason: 钓鱼攻击是典型的信息系统安全威胁，文章以预测用户对钓鱼网站的易感性为核心，属于对攻击的检测与防御，损害对象为用户的机密性与真实性等安全属性。
- Algorithm status: novel_algorithm_with_evaluation
- Method: PFM（支持向量序数回归+复合核SVORCK，含CLMM漏斗核）
- Evaluation: 在两个组织的12个月纵向现场实验（1,278名员工，49,373次交互）中与HITLSF、DRKM、AAM及SVM、SVOR等方法比较AUC，PFM显著领先；另有三个月干预现场实验评估效果。
- Algorithm reason: 文章提出新的复合核支持向量序数回归模型作为核心贡献，并利用大规模现场数据进行实证评估，方法本身是研究和贡献的中心。
- Data publicness: private_or_nonpublic / 两个组织（金融和法务公司）内部的员工行为数据、企业端点安全日志和调查问卷数据，非公开渠道。
- Decision: 文章核心是钓鱼攻击场景下用户易感性的预测和防御干预，属于信息安全攻防；同时提出并实证评估了新算法PFM/SVORCK，满足算法开发条件；数据为企业内部私有数据。
- Confidence: 0.95

## The Security of Confidential Numerical Data in Databases

- Year/journal: 2002 / Information Systems Research
- DOI: 10.1287/isre.13.4.389.74
- Security status: core_security_attack_defense
- Security reason: 本文核心是评估并防御数据库中机密数值数据被窥探者（snooper）利用线性模型进行推断性披露的安全威胁，属于数据库机密性防护。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于典型相关分析（CCA）的数据库推断安全评估方法
- Evaluation: 使用模拟的50,000条记录工资数据库演示安全评估与推断控制机制选择，并用250,000条记录数据库测试计算性能；与Palley和Simonoff的R²方法及Tendick的线性组合R²进行了理论比较。
- Algorithm reason: 论文提出了以CCA为核心的推断安全评估方法，扩展了已有安全度量，并用模拟数据库进行了实现与实证演示。
- Data publicness: private_or_nonpublic / 作者模拟生成的数据库（50,000条记录工资库及250,000条记录实验库），非公开渠道数据。
- Decision: 本文核心是针对数据库中保密数值数据的推断性披露攻击（snooper用线性模型预测机密属性），提出基于CCA的安全评估与推断控制选择方法，并利用模拟数据库进行实证演示。安全相关和算法开发均通过；数据为模拟生成，非公开。
- Confidence: 0.95

## Towards a highly effective and robust Web credibility evaluation system

- Year/journal: 2015 / Decision Support Systems
- DOI: 10.1016/j.dss.2015.07.010
- Security status: core_security_attack_defense
- Security reason: 研究核心是针对Web可信度评价系统的模仿攻击（imitating attack）的检测与防御，恶意行为者攻击系统信誉与评分完整性，属于信息系统安全攻防。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 融合矩阵分解与LDA的个性化推荐模型；基于Beta分布的模仿攻击检测机制；自适应声誉系统
- Evaluation: 使用Wikimedia Article Feedback Tool真实数据集评估推荐性能（与Random、LDA、MF对比）；使用多智能体模拟评估攻击检测精度、召回和F-measure。
- Algorithm reason: 论文提出并实现了新的推荐与防御算法，并用真实数据和模拟数据实证评估，方法贡献是核心。
- Data publicness: mixed / 推荐模型采用公开的Wikimedia Article Feedback Tool数据集；整体系统评估采用自行生成的多智能体模拟（合成）数据。
- Decision: 文章核心是设计并评估提升Web可信度评价系统鲁棒性和覆盖率的新方法，明确针对恶意用户（模仿攻击者）对系统的攻击行为进行检测与防御，属于信息系统安全的攻击防御范畴；同时提出了新的推荐、防御和声誉算法并进行了实证评估。数据包含公开真实数据与合成数据，但不影响纳入判定。
- Confidence: 0.95

## Towards controlling virus propagation in information systems with point-to-group information sharing

- Year/journal: 2009 / Decision Support Systems
- DOI: 10.1016/j.dss.2009.05.014
- Security status: core_security_attack_defense
- Security reason: 文章以计算机病毒在信息系统中的传播为研究核心，病毒是恶意代码攻击者，研究对象是病毒传播与多种杀毒/免疫对策的检测、防御和控制，属于信息系统安全攻防领域。
- Algorithm status: novel_algorithm_with_evaluation
- Method: E-SEIR 病毒传播模型及其 C_L/C_S 控制策略
- Evaluation: 通过自设参数的数值仿真（ODE 系统模拟）验证病毒无病/流行病平衡点、短期爆发临界点及 C_S-控制/多阶段 C_S-控制的效果，并与无控制及 C_L-控制进行对比。
- Algorithm reason: 论文核心贡献是提出新的病毒传播计算模型 E-SEIR，并基于该模型设计控制参数和策略；模型以微分方程形式实现并在数值实验中进行了系统评估。
- Data publicness: private_or_nonpublic / 数值仿真使用作者自设的模型参数（如 N=100000、μ=1/4380、r=30 等），非公开真实数据集或公开渠道数据。
- Decision: 该文核心是计算机病毒在信息共享网络中的传播建模和杀毒控制，属于信息系统安全攻防；同时提出新的 E-SEIR 计算模型并通过数值仿真验证，满足算法开发要求；数据为自设仿真参数，不来自公开渠道。
- Confidence: 0.95

## Trustworthy and profit: A new value-based neighbor selection method in recommender systems under shilling attacks

- Year/journal: 2019 / Decision Support Systems
- DOI: 10.1016/j.dss.2019.113112
- Security status: core_security_attack_defense
- Security reason: 研究核心是推荐系统面临托攻击（恶意用户注入虚假评分）时的检测与防御，提出VNS方法控制攻击者影响，属于信息系统安全攻防。
- Algorithm status: novel_algorithm_with_evaluation
- Method: Value-based Neighbor Selection (VNS) 方法
- Evaluation: 基于Book-Crossing数据集，模拟随机、平均、流行、分段等多种攻击场景，与PCC、SD、HPRS+SD等方法对比MAE、MSEP、MTP、精确率、召回率和F1。
- Algorithm reason: 提出并实现了VNS算法，核心贡献是新的邻居选择优化方法，并通过多组实验实证评估了其在准确性和盈利性上的优势。
- Data publicness: public / 主要数据来自公开的Book-Crossing评分数据集，辅以从Amazon.com公开获取的书价信息。
- Decision: 安全相关性：恶意攻击者（shilling attackers）注入虚假评分直接影响推荐系统数据完整性和推荐可靠性，文章核心是攻击检测与防御，属于对抗性攻击防御；算法开发：提出并实现VNS算法，以实证实验评估其性能，核心是方法贡献；数据为公开Book-Crossing数据集与公开价格信息。
- Confidence: 0.95

## What Online Reviewer Behaviors Really Matter? Effects of Verbal and Nonverbal Behaviors on Detection of Fake Online Reviews

- Year/journal: 2016 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2016.1205907
- Security status: core_security_attack_defense
- Security reason: 研究核心是检测在线虚假评论（deceptive fake reviews），评论造假者是有意误导消费者的对抗性行为者，直接操纵/滥用信息系统（在线评论平台）的内容与信任机制，造成信息真实性/可信度损害，属于典型的内容操纵攻击及其检测防御。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 融合口头/非口头行为的机器学习假评论检测模型（含RF/CART/SVM/NB分类器、敏感性分析与特征剪枝）
- Evaluation: 使用Yelp.com真实餐馆评论（1,033真+1,100假）与酒店评论（1,299条）进行十折交叉验证，对比只用语言特征的基线（含Mukherjee et al.等方法）及特征剪枝前后性能。
- Algorithm reason: 论文提出并实现了将新型非言语行为特征（如有用票、发布突发性、好友数等）与言语特征相结合的假评论检测计算模型，并进行了系统的实证评估与特征剪枝分析，核心贡献是新的检测方法。
- Data publicness: public / Yelp.com公开评论数据（餐馆与酒店评论，含Yelp过滤标注的真假标签）
- Decision: 该文以恶意评论造假者为核心对抗行为者，研究在线虚假评论（内容操纵/信任滥用）的检测与防御，属于信息系统安全攻防；同时提出了新的融合言语与非言语特征的机器学习检测模型，并以真实Yelp数据进行了实证评估，满足算法开发条件；主要数据为Yelp公开评论数据，故数据公开性为public。
- Confidence: 0.95

## When Being Hot Is Not Cool: Monitoring Hot Lists for Information Security

- Year/journal: 2016 / Information Systems Research
- DOI: 10.1287/isre.2016.0677
- Security status: core_security_attack_defense
- Security reason: 全文研究会话级安全监控热列表优化，核心是检测和阻止恶意会话与攻击，属于信息系统安全攻防检测领域。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于微分方程与峰值/高流量近似的会话监控优化方法及大小/年龄阈值策略
- Evaluation: 通过离散事件仿真与近似/精确积分对比验证H和J的准确性，并进行敏感性分析和策略比较（(n,P_f) vs (n,P_f,τ)）
- Algorithm reason: 论文提出了监控热列表规模的解析优化模型、峰值近似和高流量近似，并用C#离散事件仿真和数值实验进行了实证评估，方法贡献是核心。
- Data publicness: unclear / 数值实验使用假设基准参数和仿真生成数据，无真实公开或私有数据源。
- Decision: 安全相关性方面，研究核心是信息安全监控中的攻击检测与防御优化，恶意行为者及其攻击是建模对象，损害对象为信息系统安全属性；算法开发方面，论文提出了新的解析优化模型和近似方法，并通过仿真与数值实验进行实证评估，方法贡献为核心贡献。数据公开性仅记录，不影响纳入。
- Confidence: 0.95

## Android application classification and anomaly detection with graph-based permission patterns

- Year/journal: 2017 / Decision Support Systems
- DOI: 10.1016/j.dss.2016.09.006
- Security status: core_security_attack_defense
- Security reason: 研究核心是检测Android应用中滥用权限、异常请求和恶意软件，提出风险评分与告警阈值，属于移动信息系统安全威胁检测与防御。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于图权限模式与图中心性指标的应用异常检测/风险评分方法（权限共现图构建、z-score过滤、图特征分类、隐私分数与风险阈值）
- Evaluation: 在9,512个Google Play应用、35个类别上构建模式，用Naive Bayes进行10折交叉验证分类（全指标组合F-measure=0.809，正确率80.86%）；在摄影类应用中注入100个恶意应用，比较风险阈值检测性能，β=3时优于随机游走基线和权限二值向量。
- Algorithm reason: 文章核心贡献是新的基于权限图模式和图指标的风险检测方法，并利用大规模真实应用和注入恶意样本进行了实证评估。
- Data publicness: public / 主要数据来自2013年通过公开的非官方API爬取的Google Play应用列表、应用描述与权限声明；恶意应用注入集来源未详细说明。
- Decision: 安全相关性通过：文章以Android权限滥用和恶意应用检测为核心，威胁对象是用户隐私与系统安全，且主要贡献为风险检测与告警；算法开发通过：提出图模式构建、图指标特征、分类与隐私分数的完整计算方法，并在真实数据集和恶意注入集上实证评估；数据公开性记录为public，因主要数据来自Google Play公开爬取。
- Confidence: 0.94

## Personalized Privacy Preservation in Consumer Mobile Trajectories

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2023.1227
- Security status: core_security_attack_defense
- Security reason: 研究核心是防御恶意stalker对移动轨迹数据发布后的隐私推理攻击（家庭位置推断、重识别），通过个性化数据抑制保护消费者隐私，属于信息系统安全中的隐私保护攻防。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 个性化灵活隐私保护数据发布框架（基于个性化风险量化和结构化网格搜索的轨迹抑制混淆方案）
- Evaluation: 基于40,000消费者一百万条真实移动轨迹，与LSUP、GSUP、PPMTF、LSTM-TrajGAN等10种基线方法比较，评估风险降低与效用保持
- Algorithm reason: 论文核心贡献是提出新的个性化灵活轨迹混淆框架，实现为可运行的计算方法，并在大规模真实数据上与多种基线进行实证比较。
- Data publicness: private_or_nonpublic / 与领先数据聚合商合作的专有移动位置数据（40,012消费者、940,000个位置记录），非公开渠道获取。
- Decision: 文章以恶意stalker对移动轨迹数据的隐私推理攻击为核心研究对象，提出并实证评估了个性化数据混淆（抑制）算法，属于信息系统安全攻防与算法开发均有核心贡献；数据来自企业专有，非公开。
- Confidence: 0.93

## Stylometric Identification in Electronic Markets: Scalability and Robustness

- Year/journal: 2008 / Journal of Management Information Systems
- DOI: 10.2753/mis0742-1222250103
- Security status: core_security_attack_defense
- Security reason: 研究针对电子市场信誉系统中的身份改变与信誉操纵（匿名滥用）这一对抗行为，损害系统身份真实性与声誉完整性，核心是检测此类威胁以缓解欺诈。
- Algorithm status: novel_algorithm_with_evaluation
- Method: Writeprint（基于Karhunen-Loeve变换与模式扰动机制的文体测量识别技术）
- Evaluation: 在200名eBay交易者的反馈评论数据集上，通过可扩展性（交易者/身份数量）与鲁棒性（词语替换和伪造）实验，与PCA、n-gram、Markov、cross entropy、K-L相似度等多种基线技术比较，Writeprint取得最优或显著优越性能。
- Algorithm reason: 提出新的文体相似度检测方法Writeprint并进行了系统的实证评估和基准比较。
- Data publicness: public / 从eBay公开反馈评论中随机抽取200名交易者的3,000条评论。
- Decision: 文章研究的核心是检测电子市场信誉系统中的身份变化和信誉操纵（恶意行为人滥用匿名机制），属于信息系统安全范畴；同时提出并实证评估了新的算法Writeprint，因此纳入。数据为eBay公开反馈评论。
- Confidence: 0.93

## Complex Problem Solving: Identity Matching Based on Social Contextual Information

- Year/journal: 2007 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00141
- Security status: core_security_attack_defense
- Security reason: 研究核心是检测犯罪分子刻意伪造身份对执法数据库造成的记录失配与身份欺骗，属于对信息系统数据真实性和完整性的攻击/操纵的检测与防御。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 社会上下文身份匹配方法（结合个人特征与社会网络特征的分类方法）
- Evaluation: 基于Tucson警方Meth World真实毒品犯罪数据，采用10折交叉验证比较仅个人特征与加入社会特征时的precision/recall/F-measure，并绘制ROC曲线。
- Algorithm reason: 提出了新的身份匹配算法（含特征提取、聚类、相似度计算与J48分类），并通过真实数据进行了系统的实证评估。
- Data publicness: private_or_nonpublic / Tucson Police Department提供的Meth World执法数据库（非公开警方数据）。
- Decision: 安全上，本文聚焦执法数据库中犯罪分子的身份欺骗与失配问题，属于对系统数据真伪的对抗性操纵及相应检测防御；算法上，提出了融入社会上下文的新身份匹配方法并用真实数据进行实证评估。数据来源为警方非公开数据。
- Confidence: 0.92

## Decision support for Cybersecurity risk planning

- Year/journal: 2011 / Decision Support Systems
- DOI: 10.1016/j.dss.2011.02.013
- Security status: core_security_attack_defense
- Security reason: 研究核心是应对恶意网络攻击（恶意代码、未授权访问、拒绝服务、社会工程等）的对策组合决策，目标是降低对信息系统机密性、完整性、可用性及资产的威胁，属于安全攻防与缓解。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于模糊集与遗传算法的网络安全风险规划决策支持系统（Fuzzy-GA DSS）
- Evaluation: 使用Verizon Business收集的制造业企业调查数据，运行GA 15次迭代，将企业风险从1775K降至324K，总风险与成本从2216.8K降至891.8K。
- Algorithm reason: 论文核心贡献是构建并实现一个DSS，将模糊集系统风险计算与遗传算法搜索相结合以选择近似最优安全对策组合，并用行业数据进行实证评估。
- Data publicness: private_or_nonpublic / 主要数据来自Verizon Business内部/客户调查数据，且约定不披露企业名称和识别信息，属于非公开渠道数据。
- Decision: 该文核心是面向网络攻击的安全风险规划决策支持，使用模糊集计算不确定风险并利用遗传算法搜索安全对策组合；方法被实现并用非公开Verizon行业数据实证。满足安全相关和算法开发两个条件，数据公开性仅记录为私有。
- Confidence: 0.92

## Managing user relationships in hierarchies for information system security

- Year/journal: 2007 / Decision Support Systems
- DOI: 10.1016/j.dss.2006.11.010
- Security status: core_security_attack_defense
- Security reason: 论文核心是信息系统安全中的访问控制保护机制，防止未授权访问，属于安全攻防/防御检测领域。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于算术基本定理的密钥对(KTK)方案及键向量化改进
- Evaluation: 通过Visual Basic仿真实验（改变矩阵密度与Pmax）测度系统容量，并与多种KTK/SKL方法在初始化、计算、增删、存储等六准则上进行比较
- Algorithm reason: 论文提出新的KTK密钥分配算法并实现，通过仿真和对比表进行了实证评估，算法是核心贡献。
- Data publicness: private_or_nonpublic / 主要数据来自作者自行设计的仿真实验生成，非公开渠道获取。
- Decision: 安全相关：以未授权访问为威胁，核心是设计访问控制保护机制，损害对象为系统机密性/完整性；算法开发：提出新KTK方案并实现，有仿真实验和与既有方法的比较；数据为仿真生成，非公开。
- Confidence: 0.92

## Network externalities, layered protection and IT security risk management

- Year/journal: 2007 / Decision Support Systems
- DOI: 10.1016/j.dss.2006.08.009
- Security status: core_security_attack_defense
- Security reason: 论文核心是IT安全风险管理中的安全资源分配，明确针对外部和内部攻击者、攻击成功概率及机密性/完整性/可用性损失，研究安全投资缓解策略，恶意对抗行为者是研究问题核心。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 考虑网络外部性与分层保护的安全资源分配优化模型（基于KKT条件的闭式解与数值算法）
- Evaluation: 使用Matlab v6.5进行数值仿真，基于假设参数（如200个系统、100,000次攻击）比较不同情形下的安全投资、风险和风险降低，但未使用真实数据
- Algorithm reason: 论文提出了新的非线性安全资源分配优化模型及求解算法，模型是核心贡献，并在数值例子中实现和验证。
- Data publicness: private_or_nonpublic / 未使用真实数据，全部为人为设定的仿真参数（如系统数、攻击数、初始脆弱性等），属于非公开模拟数据
- Decision: 安全相关：研究问题为IT安全风险管理中的安全资金分配，明确包含恶意/对抗行为者（外部与内部攻击者）、安全属性（机密性、完整性、可用性）损害，核心是攻击的防御与缓解。算法开发：提出了新的安全资源分配优化模型（P1/P2）及求解算法（KKT条件、闭式解、系统/集群计数算法），并用Matlab数值仿真实证评估，方法为核心贡献。数据为模拟数据，但数据公开性不影响纳入。
- Confidence: 0.92

## The “Most Popular News” Recommender: Count Amplification and Manipulation Resistance

- Year/journal: 2014 / Information Systems Research
- DOI: 10.1287/isre.2014.0529
- Security status: core_security_attack_defense
- Security reason: 论文核心研究恶意操纵者通过虚假点击攻击新闻推荐系统，目标是提高推荐系统对操纵的抵抗力，属于信息系统安全中的对抗操纵与防御。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 概率选择（probabilistic selection）新闻推荐机制及其参数化扩展（反馈参数γ）
- Evaluation: 基于五个本地新闻网站真实数据驱动的仿真实验，与Top-N推荐和改编的Influence Limiter启发式进行比较，使用M1、M2、MAE和KL距离等指标。
- Algorithm reason: 论文提出并实现了新的概率选择推荐算法，通过仿真和理论分析（Pólya/Friedman urn模型）实证评估了其抗操纵性和计数放大抑制效果。
- Data publicness: private_or_nonpublic / 主要数据来自DailyMe Inc.提供的五个本地新闻网站的非公开文章点击数据。
- Decision: 论文将恶意操纵者（通过虚拟点击操纵新闻推荐排名）作为核心研究对象，提出了概率选择推荐机制以抵抗操纵并减少计数放大，通过基于真实点击分布数据的仿真实验及理论分析提供了实证评估；数据为非公开的公司数据，不影响纳入。
- Confidence: 0.92

## <b>Research Note</b>—Generating Shareable Statistical Databases for Business Value: Multiple Imputation with Multimodal Perturbation

- Year/journal: 2012 / Information Systems Research
- DOI: 10.1287/isre.1110.0361
- Security status: core_security_attack_defense
- Security reason: 研究核心是统计数据库共享中的重识别/隐私披露攻击防御：数据掩蔽方法MIMP明确以入侵者通过最近邻记录链接重识别个体为威胁模型，损害对象为数据主体的机密性与隐私。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 多重插补与多模态扰动（MIMP）
- Evaluation: 采用蒙特卡洛模拟（正态与非正态数据、不同噪声参数/样本量/插补次数）与2007年美国公立大学教师薪酬公开数据，与秩交换、无扰动多重插补等基线比较，评估估计偏差、统计推断等价性和披露风险。
- Algorithm reason: 论文提出了新数据掩蔽算法MIMP（模型无关多重插补+多模态扰动），并实现了该算法，通过模拟和真实数据进行了实证评估，方法贡献是全文核心。
- Data publicness: public / 主要评估数据为蒙特卡洛模拟数据；实例数据为美国公立大学2007年教师薪酬公开数据（年龄变量为模拟生成）。
- Decision: 文章聚焦数据掩蔽/匿名化这一信息系统安全中的隐私披露防御问题，威胁模型包含试图重识别个体的对抗性入侵者；同时提出了新算法MIMP并以模拟和真实数据实证评估。因此安全相关与算法开发均通过；数据为模拟加公开数据，仅记录不参与纳入判定。
- Confidence: 0.9

## A social referral appraising mechanism for the e-marketplace

- Year/journal: 2017 / Information & Management
- DOI: 10.1016/j.im.2016.07.001
- Security status: core_security_attack_defense
- Security reason: 研究直接针对电子商务中卖家操纵在线评价系统（如购买虚假好评、刷评）的信任欺诈攻击，提出基于社交网络的卖家信誉评估机制以检测和防御此类操纵，属于信息系统安全领域的攻防研究。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 社交推荐评估机制（SRM），包含吸引力分析、专业知识分析、共同取向分析和可信度分析模块
- Evaluation: 收集Facebook社交互动和Yahoo! Auction购买记录（187名参与者，730条交易记录，145个卖家），通过准确率、MAE、precision/recall/F1与EO、CF、Public等基准方法对比评估
- Algorithm reason: 论文提出并实现了一个新的计算框架，结合社交网络分析、RFM、相关分析、时间衰减和加权投票等方法，并通过真实用户数据实验验证了其有效性。
- Data publicness: private_or_nonpublic / 通过雪球抽样邀请Facebook用户并获授权收集其社交互动（墙贴）和Yahoo! Auction购买历史，属于需授权才能获取的非公开个人数据
- Decision: 安全相关：研究核心是针对在线评价系统操纵（信任欺诈）的防御机制，恶意行为者（欺诈卖家）操纵信息系统评价，损害评价系统完整性，属于信息系统安全攻防。算法开发：提出了新的SRM计算方法并通过实证数据评估，方法为核心贡献。因此严格纳入。数据主要来自需要授权的私人用户数据，属非公开。
- Confidence: 0.9

## An investigation of Zipf's Law for fraud detection (DSS#06-10-1826R(2))

- Year/journal: 2008 / Decision Support Systems
- DOI: 10.1016/j.dss.2008.05.003
- Security status: core_security_attack_defense
- Security reason: 研究核心是基于Zipf定律检测欺诈/攻击记录，主要实验使用KDDCUP'99入侵检测数据集，并包含企业网络遭外部攻击和病毒入侵的真实案例，属于信息系统攻防检测。
- Algorithm status: novel_algorithm_with_evaluation
- Method: Zipf Analysis（基于Zipf定律的异常/欺诈检测分析程序）
- Evaluation: 在KDDCUP'99入侵检测数据集上以Audit Hit Rate、Bayes Audit Hit Rate、混淆矩阵和误分类成本对比KDDCUP'99基线/无预处理分类模型；另以企业防火墙和核心交换机日志案例验证。
- Algorithm reason: 论文提出并实现了Zipf Analysis频次模式异常检测方法，包括模式生成、理论频次回归、置信区间和Z统计检验等步骤，并通过仿真实验和案例进行了实证评估。
- Data publicness: mixed / 主要仿真数据为公开的KDDCUP'99入侵检测基准数据集；另有非公开的台湾某企业防火墙和核心交换机日志作为案例数据。
- Decision: 安全相关性：文章以检测欺诈/网络攻击记录为核心，使用入侵检测基准数据和真实企业网络攻击日志，涉及系统可用性和网络入侵等安全损害，符合核心安全攻防检测。算法开发：提出并实现了Zipf Analysis这一新异常检测分析程序，并在KDDCUP'99数据和真实案例中进行了实证评估，符合新方法加实证评估。数据公开性：主要实验数据为KDDCUP'99公开数据集，另有非公开企业日志案例，记为mixed。
- Confidence: 0.9

## Decision support approaches for cyber security investment

- Year/journal: 2016 / Decision Support Systems
- DOI: 10.1016/j.dss.2016.02.012
- Security status: core_security_attack_defense
- Security reason: 研究以商品化网络攻击者为对手，建模攻击者与防御者博弈，核心目标是选择网络安全控制措施以防御攻击、降低数据资产损失，属于信息系统安全攻防与防御投资决策。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 控制博弈与控制子博弈 + 0-1多选择多目标背包优化的混合方法，并与完全博弈和纯背包方法比较
- Evaluation: 基于SANS/CWE真实数据构建案例研究（小型：7控制13漏洞；大型：27控制36攻击），比较三种方法，并对照UK Cyber Essentials指南验证，同时复现Rakes et al.案例获得95%以上成功率。
- Algorithm reason: 论文提出并实现了多种安全投资决策计算方法（博弈、背包优化及混合），核心贡献在于方法框架和比较，并通过案例数据进行了实证评估，而非仅将现成算法作为工具。
- Data publicness: public / 案例研究使用CVE/CWE、SANS Critical Security Controls等公开数据，作者将案例数据在线公开（https://www.panaousis.com/papers/casestudy.pdf）。
- Decision: 文章核心是网络安全投资防御决策，明确建模恶意商品化攻击者与防御者博弈，提出并实现三种计算方法（完全博弈、混合博弈-背包、纯背包），基于SANS/CWE/Cyber Essentials公开数据构建案例进行实证比较和验证，因此同时通过安全相关性与算法开发条件；数据为公开渠道来源。
- Confidence: 0.9

## How can online marketplaces reduce rating manipulation? A new approach on dynamic aggregation of online ratings

- Year/journal: 2017 / Decision Support Systems
- DOI: 10.1016/j.dss.2017.10.003
- Security status: core_security_attack_defense
- Security reason: 研究核心是应对在线市场中零售商通过提交虚假评分操纵评分系统的对抗行为，属于对信息系统完整性和真实性的攻击与防御，提出的动态聚合方法是缓解此类威胁的防御技术。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 动态k值评分聚合方法
- Evaluation: 通过仿真实验（1200轮、多种初始评分分布、不同虚假评分水平）与即时更新、时间折扣、单值聚合、三值聚合等方法比较，并进行了多项稳健性检验。
- Algorithm reason: 论文提出一种根据最近评分分布动态确定k值（1/2/3）的评分聚合方法，作为核心贡献被实现并在仿真中评估，且不是仅作为现成工具使用。
- Data publicness: private_or_nonpublic / 全文未使用真实数据集，主要数据为模拟仿真生成的评分序列，非公开渠道数据。
- Decision: 安全相关：存在恶意零售商对评分系统的操纵（虚假评分），损害评分完整性和消费者信任，研究核心为防御/缓解该威胁。算法开发：提出动态k值评分聚合新方法，实现了仿真并进行了实证评估。数据公开性：仅使用模拟数据。
- Confidence: 0.9

## Manipulation of online reviews: An analysis of ratings, readability, and sentiments

- Year/journal: 2012 / Decision Support Systems
- DOI: 10.1016/j.dss.2011.11.002
- Security status: core_security_attack_defense
- Security reason: 针对在线评论操纵的检测研究，属于内容操纵与虚假信息传播的安全攻防主题
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于Wald-Wolfowitz Runs检验的在线评论操纵检测方法（结合情感分析和可读性指标）
- Evaluation: 使用Amazon书籍评论数据集，通过Runs检验识别非随机评论，并建立线性回归模型评估操纵对销售排名的影响
- Algorithm reason: 提出并实证评估了一种结合Runs检验、情感评分和可读性分析的评论操纵检测方法
- Data publicness: public / Amazon.com公开书籍评论数据，通过Amazon Web Services采集
- Decision: 文章核心是检测在线评论操纵（内容操纵攻击），提出Runs test统计检测方法并基于Amazon数据实证评估，符合安全相关与算法开发双条件
- Confidence: 0.9

## MegaFake: A theory-driven dataset of fake news generated by large language models

- Year/journal: 2026 / Decision Support Systems
- DOI: 10.1016/j.dss.2026.114676
- Security status: core_security_attack_defense
- Security reason: 研究核心是恶意行为者利用LLM大规模生成假新闻，并针对此类内容操纵/虚假信息威胁的检测与治理，属于信息系统内容安全攻防。
- Algorithm status: novel_algorithm_with_evaluation
- Method: LLM-Fake Theory 驱动的理论引导假新闻生成流水线（prompt engineering pipeline）及 MegaFake 数据集构建方法
- Evaluation: 使用GLM和Llama实现生成，评估了生成质量（困惑度、多样性、人工评价）及多种LLM/深度学习模型的检测、跨域迁移、泛化对比和数据规模敏感性实验。
- Algorithm reason: 提出了基于LLM的理论驱动假新闻自动生成方法与数据集，方法实现并开展了大规模实证评估，构成全文核心贡献。
- Data publicness: public / 基于公开的FakeNewsNet（GossipCop和PolitiFact）数据，并在Online Data Repository中公开提供MegaFake数据集。
- Decision: 安全相关性：论文针对恶意行为者利用LLM生成假新闻（内容操纵/虚假信息）的检测与治理，属于信息系统安全攻防；算法开发：提出LLM-Fake Theory驱动的假新闻自动生成流水线并构建数据集，方法已实现并经过大量实证评估；数据公开：基于公开FakeNewsNet且数据集在线公开，故判定为public。
- Confidence: 0.9

## Modifying Transactional Databases to Hide Sensitive Association Rules

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2021.1033
- Security status: core_security_attack_defense
- Security reason: 研究核心是开发数据净化/脱敏方法，通过修改事务数据库隐藏敏感关联规则，防止共享数据时敏感信息被挖掘泄露，属于隐私保护数据挖掘中的敏感数据净化与防泄露防御，针对数据机密性泄露威胁进行防御。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于整数规划的敏感关联规则隐藏与准确性最大化方法（RHP/AMP/LRH，包含净化问题整数规划与启发式算法）
- Evaluation: 在真实公开数据集（retail 88,162笔、bms-pos 515,597笔）和合成数据集（10m/50m/100m，最大1亿笔）上实验，与Verykios et al. (2004)和Telikani & Shahbahrami (2017)等基准比较，报告准确性、求解时间、spurious rules等指标
- Algorithm reason: 论文提出非线性整数规划公式并分解为净化与准确性最大化问题，开发线性化及问题缩减技术，并在大规模数据上实证评估，方法为核心贡献。
- Data publicness: public / 真实数据集retail和bms-pos来自公开FIMI仓库（http://fimi.uantwerpen.be/data/），合成数据集由公开的IBM合成数据生成器产生
- Decision: 文章属于隐私保护数据挖掘中的敏感数据净化方法，通过修改事务数据库隐藏敏感关联规则以防御敏感信息泄露，是明确的系统数据安全防御；同时提出了新的整数规划模型、线性化启发式并大规模实证验证，核心贡献是算法开发。数据以公开真实数据集和公开生成器合成数据为主。
- Confidence: 0.9

## Understanding the Value of Countermeasure Portfolios in Information Systems Security

- Year/journal: 2008 / Journal of Management Information Systems
- DOI: 10.2753/mis0742-1222250210
- Security status: core_security_attack_defense
- Security reason: 文章以信息系统安全威胁（病毒、DoS、信息窃取）为研究问题，建模并评估安全对策组合对攻击的缓解与恢复价值，属于安全防御与评估。
- Algorithm status: novel_algorithm_with_evaluation
- Method: ISSC对策组合价值模拟模型（基于几何布朗运动与跳跃过程的蒙特卡洛仿真）
- Evaluation: 通过在合成数据上进行的三个模拟实验（ANOVA分析、不同威胁情景与组合效果比较），评估了模型与投资组合价值。
- Algorithm reason: 论文核心贡献是开发并实现了集成的模拟模型来量化ISSC组合价值，并通过系统实验验证，属于新计算方法。
- Data publicness: private_or_nonpublic / 使用合成的参数化模拟数据，非公开真实数据集。
- Decision: 安全相关：核心是信息安全威胁（攻击）的防御与评估（对策组合价值）；算法开发：提出并实现新的模拟模型，有实证实验；数据为合成数据，不参与纳入判定。
- Confidence: 0.9

## Cybersecurity vulnerability management: A conceptual ontology and cyber intelligence alert system

- Year/journal: 2020 / Information & Management
- DOI: 10.1016/j.im.2020.103334
- Security status: core_security_attack_defense
- Security reason: 研究核心是漏洞信息整合与警报系统，目标是防止漏洞被利用，属于信息系统安全中的漏洞管理与缓解，对抗性利用是核心威胁。
- Algorithm status: novel_algorithm_with_evaluation
- Method: Cybersecurity Vulnerability Ontology (CVO) + Cyber Intelligence Alert (CIA) system（含SMIET集成学习分类器和SWRL规则引擎）
- Evaluation: 基于13,277条Twitter推文、3,389个CVE漏洞和厂商数据，使用10折交叉验证评估分类器（F-score多在0.94以上），警报系统准确率95%，用户调查满意率82%，并与Mittal et al.及Lippmann et al.进行比较。
- Algorithm reason: 提出了新的本体驱动的警报系统，包含可运行的组件和规则引擎，并进行了系统的实证评估，方法贡献是核心。
- Data publicness: public / 主要数据来自Twitter公共API、CVE/NVD公开数据库、厂商公开补丁信息、NIST手册和德国IT Grundschutz手册等公开来源。
- Decision: 该研究聚焦网络安全漏洞管理，以漏洞利用威胁为核心，提出了本体和警报系统，并进行了实现与实证评估，因此安全相关和算法开发均通过，数据来源公开。
- Confidence: 0.88

## Explainable Deep Learning for False Information Identification: An Argumentation Theory Approach

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2020.0097
- Security status: core_security_attack_defense
- Security reason: 核心是自动化识别在线虚假信息/谣言（FII），属于内容操纵威胁的检测，符合社会工程与内容操纵攻击类别，且围绕对用户/信息真实性的危害进行防御。
- Algorithm status: novel_algorithm_with_evaluation
- Method: G-FINDER（基于结构平衡理论的通用虚假信息检测器）
- Evaluation: 在PHEME Twitter数据集和Wikipedia众包数据集上对比Riedel、MBiLSTM、Attention、BERT、RoBERTa、ELECTRA等基线；另通过MTurk用户实验（254名参与者）评估可解释性SBTX对任务准确率、信任、决策信心的影响。
- Algorithm reason: 提出基于Toulmin论证理论与结构平衡理论的新特征构造方法和框架，并集成到多种ML/DL模型中，通过两个实证实验验证性能与可解释性。
- Data publicness: public / 主要使用公开的PHEME Twitter谣言数据集，证据来自公开新闻文章；另使用实验室创建的Wikipedia众包数据集（公开来源）和MTurk用户实验数据。
- Decision: 研究核心为虚假信息识别这一信息安全内容操纵威胁的检测；提出并实现了基于结构平衡理论的新算法G-FINDER，并经数据驱动的性能实验与用户实验验证，因此同时满足安全相关与新算法实证评估的要求；主要数据来自公开PHEME数据集，记录为公开。
- Confidence: 0.88

## Matching information security vulnerabilities to organizational security profiles: a genetic algorithm approach

- Year/journal: 2006 / Decision Support Systems
- DOI: 10.1016/j.dss.2004.06.004
- Security status: core_security_attack_defense
- Security reason: 研究核心是选择安全技术组合覆盖信息系统漏洞、降低恶意行为者利用漏洞的风险，属于信息安全漏洞管理与防御。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 遗传算法（GA）漏洞-安全技术匹配方法
- Evaluation: 25个随机漏洞场景下与枚举（Brute Force）方法比较，报告适应度、误差和执行时间；并分析不同问题规模与种群大小下的准确性与可扩展性。
- Algorithm reason: 提出并实现了GA-based approach用于最小成本最大化漏洞覆盖，并通过模拟实验与枚举法对比评估。
- Data publicness: private_or_nonpublic / 实验使用25个随机生成的漏洞场景及随机权重，无公开真实数据；漏洞与安全技术分类表基于RAND报告。
- Decision: 安全相关性：以信息系统漏洞覆盖与防御为核心，恶意行为者明确存在，损害对象为信息安全属性，属于攻防检测防御缓解。算法开发：提出了GA匹配方法并实现，通过与枚举法的模拟实验实证评估了准确性和效率。数据公开性：主要数据为模拟随机生成，非公开渠道。
- Confidence: 0.88

## Distributed decision support systems under limited degrees of competence: A simulation study

- Year/journal: 1997 / Decision Support Systems
- DOI: 10.1016/s0167-9236(96)00073-5
- Security status: core_security_attack_defense
- Security reason: 论文研究分布式决策支持系统中存在不真诚或不称职的节点，它们故意提供虚假信息以误导决策，属于对信息系统信息完整性的对抗操纵；研究核心是设计并评估信念修正机制以检测矛盾、识别不可靠节点并缓解错误信息的影响。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于ATMS的信念修正模型（含可信度与可靠性动态更新算法）
- Evaluation: 在基于MICE的CLUE模拟测试台上进行了约700小时的模拟实验，变化节点能力与真诚度分布，评估收敛性、正确性和可靠性估计。
- Algorithm reason: 论文提出了一种新的信念修正模型，并实现为可运行的模拟系统，通过大量仿真实验评估了不同局部策略对全局性能的影响，方法贡献是核心。
- Data publicness: private_or_nonpublic / 主要数据来自作者自建的CLUE仿真测试台生成的模拟数据，非公开渠道。
- Decision: 文章核心研究不真诚/不称职节点对分布式决策支持系统的误导攻击，并提出信念修正算法作为检测与防御手段，属于信息系统安全中的对抗性信息操纵防御；同时算法被实现并通过仿真实验进行了实证评估，因此两个模块均通过。数据为自建模拟数据，不参与纳入判定。
- Confidence: 0.87

## A decision methodology for managing operational efficiency and information disclosure risk in healthcare processes

- Year/journal: 2014 / Decision Support Systems
- DOI: 10.1016/j.dss.2012.10.046
- Security status: core_security_attack_defense
- Security reason: 研究以恶意或越权员工获取患者隐私信息导致披露风险为核心，通过安全冲突集和任务/员工监控控制的部署来预防未授权的信息访问，属于信息系统安全的防护与缓解。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 两阶段优化决策方法（吞吐量优化的开放Jackson排队网络模型 + 控制成本最小化的集合覆盖模型，及顺序决策近似方法）
- Evaluation: 基于临床工作流参数化计算实验，求解得到6个最优人员分配方案，并评估各方案的安全冲突暴露程度及任务/员工监控控制效果。
- Algorithm reason: 核心贡献是新的两阶段决策优化方法，实现了P0吞吐量优化和P1控制部署优化，并通过临床工作流计算实验进行了实证评估。
- Data publicness: unclear / 主要数据为临床工作流图示与人工校准的参数（服务率、技能矩阵、转移概率等），未说明真实数据来源渠道。
- Decision: 文章核心是防止由恶意或越权员工造成的信息披露风险，属于信息系统安全攻防与缓解；同时提出了可运行的两阶段优化决策方法，并通过计算实验进行实证评估。数据为校准的示例性参数，公开性不明确，但不影响纳入判定。
- Confidence: 0.85

## An Information Systems Security Risk Assessment Model Under the Dempster-Shafer Theory of Belief Functions

- Year/journal: 2006 / Journal of Management Information Systems
- DOI: 10.2753/mis0742-1222220405
- Security status: core_security_attack_defense
- Security reason: 本文核心是信息系统安全（ISS）风险评估模型，将威胁代理（如黑客、内部人员）对信息资源的攻击与滥用作为风险因子，以机密性、完整性等信息安全属性的损害为评估对象，属于安全攻防中的风险评估。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于Dempster–Shafer证据推理的ISS风险评估模型
- Evaluation: 利用假设的硬件安全例子和真实WebTrust保证业务案例，通过Auditor's Assistant软件进行证据传播计算，并对逻辑关系、证据位置和证据强度进行了敏感性分析。
- Algorithm reason: 本文提出了一种新的ISS风险评估方法论（证据推理模型），定义了ISS风险为负面结果的plausibility，并通过真实案例和敏感性分析对模型进行了实证评估，方法贡献是全文核心。
- Data publicness: private_or_nonpublic / 主要数据来自审计公司提供的WebTrust保证业务内部工作底稿，具有保密限制；另有假设的数值示例。
- Decision: 文章属于信息系统安全风险评估研究，有明确的恶意威胁主体（黑客、内部人员等），损害对象为系统信息安全属性，核心是威胁风险的评估；同时提出新的证据推理计算方法，并在真实案例中实现和进行了敏感性分析，满足新算法与实证评估要求。数据来自非公开审计工作底稿。
- Confidence: 0.85

## An entropy approach to disclosure risk assessment: Lessons from real applications and simulated domains

- Year/journal: 2011 / Decision Support Systems
- DOI: 10.1016/j.dss.2010.11.014
- Security status: core_security_attack_defense
- Security reason: 研究核心是评估分布式数据库中的trail重识别（隐私披露攻击）风险并提出熵度量以支持缓解，属于信息系统安全中的隐私披露风险检测与评估。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于信息论自信息/熵的trail披露风险评估指标
- Evaluation: 在模拟环境（均匀与Zipf分布，完全指定/不完全指定系统）及真实案例（伊利诺伊州出院数据库、Homenet数据）中比较熵得分与实测披露率，并用形状分数σ评估曲线匹配。
- Algorithm reason: 论文提出并实证评估了一个新的熵度量用于估计trail披露风险，核心贡献是方法本身且经过模拟与案例验证。
- Data publicness: private_or_nonpublic / 核心评估数据为合成模拟数据；辅助案例分析使用伊利诺伊州公开医院出院数据库和Homenet项目非公开数据。
- Decision: 文章聚焦trail re-identification这一隐私披露攻击的风险评估，属于信息系统安全；核心贡献是新的熵度量方法，并基于真实与模拟数据进行了实证评估；数据公开性不参与判定。
- Confidence: 0.85

## Assessing the severity of phishing attacks: A hybrid data mining approach

- Year/journal: 2011 / Decision Support Systems
- DOI: 10.1016/j.dss.2010.08.020
- Security status: core_security_attack_defense
- Security reason: 文章以钓鱼攻击（恶意社交工程和身份盗窃）为核心研究对象，评估其风险等级与对企业的市场价值损失，属于信息系统安全威胁评估。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 混合文本与数据挖掘分类方法（关键短语概念提取 + DT/SVM/NN 监督分类）
- Evaluation: 基于1030条Millersmiles钓鱼警报及CRSP财务数据，采用10折交叉验证和30%验证集，比较文本/财务/混合三种输入下DT、SVM、NN对风险等级与CAR分类的准确率（最高89.13%）和top decile lift（最高8.52）。
- Algorithm reason: 论文核心贡献是构建并实证评估了用于预测钓鱼攻击严重性的混合文本与数据挖掘框架，包含特征构造和分类建模。
- Data publicness: mixed / 钓鱼警报来自公开数据库Millersmiles；企业财务数据来自CRSP订阅数据库（属于公开市场数据但需授权访问）。
- Decision: 文章聚焦钓鱼攻击（恶意对抗行为者），评估其风险等级与市场价值损失，属于信息安全攻防评估；提出了混合文本挖掘+监督分类的预测方法并进行了实证评估，满足算法开发条件；数据为公开警报数据库与订阅金融数据库混合，但不影响纳入。
- Confidence: 0.85

## Combining Crowd and Machine Intelligence to Detect False News on Social Media

- Year/journal: 2022 / MIS Quarterly
- DOI: 10.25300/misq/2022/16526
- Security status: core_security_attack_defense
- Security reason: 文章核心是检测社交媒体上的虚假信息，属于内容操纵攻击的检测，保护信息真实性；全文详细提出CAND检测框架并对抗故意操纵的鲁棒性进行分析，符合安全攻防检测定义。
- Algorithm status: novel_algorithm_with_evaluation
- Method: CAND框架（核心为CLNAM贝叶斯聚合模型）
- Evaluation: 在Weibo和Twitter两个真实数据集上评估，与SVM、CNN、LSTM、Bi-LSTM、BERT、Concat、HSA、MV、BAM等基准比较，使用PR AUC、F1、召回率等指标，并在多种不平衡比率下检验。
- Algorithm reason: 提出了新的CAND框架和CLNAM概率聚合模型，并实现了完整的计算流程，在多个真实数据集上进行了系统的实证评估，方法贡献是全文核心。
- Data publicness: public / 主要数据来自公开社交媒体平台：新浪微博的公开帖子和评论，以及Twitter上公开的学术数据集（Ma et al., 2016, 2017）
- Decision: 此文核心是检测社交媒体虚假信息，属于内容操纵攻击的检测防御，安全相关性足；同时提出了CAND新框架和CLNAM新模型，并经重要真实数据集实证，满足算法开发要求；数据均来自公开数据集，故公开属性。
- Confidence: 0.85

## Constructing a reliable Web graph with information on browsing behavior

- Year/journal: 2012 / Decision Support Systems
- DOI: 10.1016/j.dss.2012.06.001
- Security status: core_security_attack_defense
- Security reason: 论文以Web垃圾页面和垃圾链接对搜索引擎排序的对抗性操纵为核心问题，提出并评估了利用用户浏览行为检测垃圾页面、提升页面质量估计的方法，属于对抗性内容操纵的检测与防御。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于‘带先验知识的冲浪模型’的userPageRank/userTrustRank算法，以及BG、user-HG、user-CG三种Web图构建算法
- Evaluation: 在大规模搜索引擎工具栏点击日志（28亿次点击事件）构建的图上，与PageRank、TrustRank、DiffusionRank、BrowseRank进行ROC/AUC和成对有序性比较；并在微博社交图上评估userPageRank/userTrustRank。
- Algorithm reason: 论文核心贡献是提出新的冲浪模型、改进的PageRank/TrustRank算法以及三种图构建算法，并实现了完整的实证评估和基线比较。
- Data publicness: private_or_nonpublic / 主要数据来自某中国搜索引擎公司内部工具栏Web访问日志、内部爬虫抓取的原Web图以及微博内部采集数据，均非公开渠道。
- Decision: 安全相关：文章核心是检测Web垃圾页面/链接对搜索引擎的对抗性操纵，属于内容操纵攻击的检测与防御，损害搜索引擎排序的完整性与真实性；算法开发：提出了新冲浪模型、userPageRank/userTrustRank以及三种图构建算法，并在大规模私有日志数据上进行了实证评估。数据公开性仅记录：主要数据为非公开内部日志。
- Confidence: 0.85

## Regulating Cryptocurrencies: A Supervised Machine Learning Approach to De-Anonymizing the Bitcoin Blockchain

- Year/journal: 2019 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2018.1550550
- Security status: core_security_attack_defense
- Security reason: 研究核心是利用监督学习去匿名化比特币区块链，识别勒索软件、诈骗、暗网市场等网络犯罪实体，属于威胁检测与网络威胁情报，而非单纯的金融欺诈。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于监督机器学习（Gradient Boosting等）的比特币区块链实体类型去匿名化分类方法
- Evaluation: 使用957个已标注实体（约3.85亿交易）进行训练，比较7种监督学习算法，Gradient Boosting默认参数达到80.42%交叉验证准确率和79.64% F1；并在22个疑似网络犯罪集群和153,293个未标注集群上进行预测演示。
- Algorithm reason: 论文明确提出开发并验证了新的去匿名化方法，包含特征工程、多分类器构建与原型实现，并有基于真实数据的实证评估。
- Data publicness: mixed / 原始比特币区块链交易数据公开，但聚类和标签数据由Chainalysis专有处理提供，核心训练标注不公开。
- Decision: 研究属于信息系统安全领域的威胁检测，核心是开发并实证评估新的监督学习去匿名化方法；数据公开性为混合但不影响纳入。
- Confidence: 0.85

## Secure attribute sharing of linked microdata

- Year/journal: 2016 / Decision Support Systems
- DOI: 10.1016/j.dss.2015.10.005
- Security status: core_security_attack_defense
- Security reason: 研究核心是防止链接微数据共享中的敏感属性值披露（属性推断/值披露攻击），开发了掩码防御程序并评估披露风险，属于信息系统机密性保护。
- Algorithm status: novel_algorithm_with_evaluation
- Method: SASH（Secure Attribute Sharing of Linked Microdata）：基于高斯 copula 条件分布、安全秩相关矩阵计算与反向映射的数据掩码方法
- Evaluation: 使用仿真数据（n=100/1000/5000，1000次重复）评估 SASH 与 data swapping（10%/25%/50%）在分析有效性（相关系数保持）和披露风险（R²）上的表现，并展示散点图验证非线性关系保持。
- Algorithm reason: 论文提出新的掩码共享算法 SASH，并实现了基于仿真的实证评估和与现成方法的基准比较。
- Data publicness: private_or_nonpublic / 实验数据为作者模拟生成（synthetic data），并非来自公开渠道。
- Decision: 该文属于信息系统安全中的数据隐私保护（防止属性推断/值披露攻击），提出了新的掩码算法 SASH 并进行了仿真实证评估，因此 strict_include 为 true；数据为模拟数据，记录为非公开。
- Confidence: 0.85

## Sleight of Hand: Identifying Concealed Information by Monitoring Mouse-Cursor Movements

- Year/journal: 2019 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00527
- Security status: core_security_attack_defense
- Security reason: 论文核心是检测内部人员/员工隐瞒信息（如窃取部门信用卡数据文件的内部威胁），属于信息系统安全威胁检测与防御。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于CIT问卷的鼠标轨迹欺骗检测方法与理论驱动决策树分类模型
- Evaluation: 受控实验66名有效被试，同时采集鼠标轨迹与皮电活动，与基线和真实组比较；鼠标模型平均准确率78.3%、假阳性率21.7%，并与皮电模型对比。
- Algorithm reason: 核心贡献是提出可自动化的在线CIT鼠标移动检测方法并实现理论驱动决策树分类模型，且用实验数据进行实证评估。
- Data publicness: private_or_nonpublic / 作者实验室招募75名大学生完成模拟盗窃与筛查问卷所采集的鼠标轨迹、皮电及视频数据，非公开。
- Decision: 安全相关：该文针对内部威胁和敏感数据窃取等对抗行为，以检测隐瞒信息为研究核心，属于信息系统安全中的攻击检测与防御；算法开发：提出新的CIT鼠标移动检测方法并实现可运行的决策树分类模型，有实证数据评估；数据为实验室采集的非公开数据。
- Confidence: 0.82

## A novel means to address RFID tag/item separation in supply chains

- Year/journal: 2018 / Decision Support Systems
- DOI: 10.1016/j.dss.2018.09.003
- Security status: core_security_attack_defense
- Security reason: 论文针对RFID标签与物品分离问题，明确指出可能由不诚实方故意实施（如ticket-switching、身份伪造），这会操纵RFID识别系统、破坏物品身份完整性与真实性；提出的方法用于检测和缓解此类分离威胁，并包含对主动/被动攻击的安全分析，属于信息安全攻防核心。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于知识系统与环境条件传感器的RFID标签分离检测及相互认证协议
- Evaluation: 使用仿真数据（1000个模拟物品）比较关联标签、直接传感器、交叉验证和知识型系统四种方案，通过配对t检验评估误读率，结果显示知识型系统总体错误最少。
- Algorithm reason: 论文提出新的知识型系统框架融合密码学认证协议和环境传感器信息来检测RFID标签分离，核心贡献是方法本身，且通过仿真实验与统计检验进行了实证评估。
- Data publicness: unclear / 全文基于作者构造的仿真模拟数据，未提及真实公开或私有数据来源。
- Decision: 安全相关性：论文研究RFID标签分离检测，恶意行为者可通过故意分离/切换标签（如ticket-switching）攻击RFID识别系统，损害完整性/真实性，研究核心是检测与缓解该威胁；算法开发：提出了知识型系统与密码学协议相结合的新方法，并通过仿真实验进行了实证评估；数据公开性：基于仿真数据，来源不明。综合判定strict_include=true。
- Confidence: 0.8

## Filtering trust opinions through reinforcement learning

- Year/journal: 2014 / Decision Support Systems
- DOI: 10.1016/j.dss.2014.06.006
- Security status: core_security_attack_defense
- Security reason: 核心是针对在线声誉/信任系统中恶意见证人的偏见证言与合谋操纵（ballot-stuffing/badmouthing）进行检测、过滤和防御，属于内容操纵攻击与对抗性防御。
- Algorithm status: novel_algorithm_with_evaluation
- Method: Actor-Critic Trust (ACT) 自适应信任证据聚合模型
- Evaluation: 在包含1000个服务提供者、100个见证人和100个服务消费者的自建仿真测试床中，与W2010、Y2003、B2002等方法比较NAUL和Collusion Power，ACT平均改善约20%-25%。
- Algorithm reason: 论文提出基于actor-critic强化学习的ACT算法，实现为可运行算法并通过大规模仿真进行了实证评估。
- Data publicness: private_or_nonpublic / 数据来自作者自建仿真测试床生成，未使用公开数据集，也未提及公开代码或数据发布。
- Decision: 全文核心是防御恶意见证人对信任/声誉系统操纵（偏见证言与合谋），属于安全相关的内容操纵攻击检测与防御；同时提出并实现了新的强化学习算法ACT，并通过仿真实证评估。数据为仿真生成，不来自公开渠道。
- Confidence: 0.8

## The economic impact of cyber terrorism

- Year/journal: 2013 / The Journal of Strategic Information Systems
- DOI: 10.1016/j.jsis.2012.10.004
- Security status: core_security_attack_defense
- Security reason: 文章核心是研究网络恐怖分子和普通黑客对信息系统的攻击，并通过博弈论模型分析最优信息安全投资与威慑，属于以攻击/防御为核心的信息系统安全研究。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于博弈论的信息系统安全最优投资模型（一般和静态博弈模型）
- Evaluation: 在MatLab中使用Gordon-Loeb和Hausken两类breach函数进行仿真，改变攻击者偏好（贴现率）、breach函数敏感性和威慑水平，比较不同情境下的最优安全投资；无真实数据或基准算法比较。
- Algorithm reason: 论文提出新的博弈论投资模型作为核心贡献，并通过仿真实验评估其对网络恐怖分子与普通黑客攻击下的最优投资行为。
- Data publicness: unclear / 主要数据为仿真生成的参数化情境，未使用明确的外部数据来源；breach函数取自已发表文献，非实际数据集。
- Decision: 安全性上，文章聚焦网络恐怖分子/黑客对信息系统的攻击与防御投资，属核心安全攻防；算法开发上，提出博弈论安全投资模型并用MatLab仿真评估，作为核心贡献；数据公开性不可判定，但不影响纳入。
- Confidence: 0.75
