# Security-relevant algorithm development (AIS Basket)

Completed: 300 / 13909
Retained: 5

## Semi-Supervised Cyber Threat Identification in Dark Net Markets: A Transductive and Deep Learning Approach

- Year/journal: 2020 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2020.1790186
- Security status: core_security_attack_defense
- Security reason: 研究核心是在暗网市场中识别与检测恶意网络威胁产品（如勒索软件、黑客工具、被泄露账户），威胁对象是系统与用户安全，且属于威胁检测与防御范畴。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 基于转导学习（TSVM）和深度双向LSTM的半监督威胁识别方法
- Evaluation: 在包含79,434条产品列表的暗网市场数据集上，与SVM、LSTM、CNN等基准方法比较，F1达到89.55%，显著优于基线。
- Algorithm reason: 提出了新的半监督标签算法（TSVM结合词汇和结构启发式）以及定制的双向LSTM架构作为核心贡献，并实现了基于数据的实证评估。
- Data publicness: public / 数据来自九个公开暗网市场的网络爬取，作者在GitHub上公开了数据集（https://github.com/mohammadrezaebrahimi/JMIS-DarkNetMarketData）。
- Decision: 文章核心是针对暗网市场上恶意网络威胁产品的自动识别与检测，属于典型的安全攻防与威胁检测领域；同时提出并实证评估了新的半监督学习算法（TSVM启发式标注）与深度LSTM架构，方法实现且评估完整；数据集公开在GitHub。故安全相关性与算法开发均通过。
- Confidence: 1.0

## The Impact of Fake Reviews on Online Visibility: A Vulnerability Assessment of the Hotel Industry

- Year/journal: 2016 / Information Systems Research
- DOI: 10.1287/isre.2016.0674
- Security status: core_security_attack_defense
- Security reason: 全文围绕恶意主体通过注入虚假评论操纵在线可见性的攻击策略、脆弱性评估及防御响应，属于内容操纵与对抗攻击领域，而非纯金融欺诈。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 可见性形式化度量与虚假评论攻击注入模拟框架（含可见性量化模型、三种考虑模型、三种攻击策略及DelayIndex排序函数）
- Evaluation: 基于TripAdvisor 230万条评论、17城市4,709家酒店，比较平均评分与PopularityIndex排序函数及多种考虑模型下的攻击成功率，并验证DelayIndex抗操纵性能。
- Algorithm reason: 论文的核心贡献是开发并实证评估了新的计算模型与算法框架（可见性度量、攻击模拟、抗欺诈排序函数），而非仅将现成算法用于其他目的。
- Data publicness: public / 主要数据来自TripAdvisor.com公开可爬取的酒店评论（2,305,610条）及少量Yelp.com公开评论，均属公开网络数据。
- Decision: 全文明确研究恶意行为者利用虚假评论攻击酒店在线可见性的脆弱性，并提出和实证评估了攻击模拟、可见性计算和抗操纵排序等方法；数据来自公开评论平台，故严格纳入。
- Confidence: 0.99

## PhishWHO: Phishing webpage detection via identity keywords extraction and target domain name finder

- Year/journal: 2016 / Decision Support Systems
- DOI: 10.1016/j.dss.2016.05.005
- Security status: core_security_attack_defense
- Security reason: 文章聚焦钓鱼网页攻击，存在恶意行为者（钓鱼者），损害用户凭证与系统安全，核心为检测与防御。
- Algorithm status: novel_algorithm_with_evaluation
- Method: PhishWHO：基于身份关键词提取与目标域名查找的钓鱼网页检测系统（加权URL令牌系统、N-gram模型、3层身份匹配）
- Evaluation: 使用PhishTank和OpenPhish的5000个钓鱼网页与Alexa前一百万中的5000个合法网页进行实验，与CANTINA、Ramesh等、Huh&Kim等方法比较，MCC最高达0.9244。
- Algorithm reason: 提出新的检测算法（加权URL令牌系统、N-gram身份关键词提取、3层身份匹配），实现并基于大规模公开数据实证评估，是全文核心贡献。
- Data publicness: public / 钓鱼URL来自PhishTank和OpenPhish，合法URL来自Alexa顶级列表，均为公开渠道。
- Decision: 本文属于安全领域核心攻防研究，明确提出钓鱼攻击及检测系统；算法开发方面提出新的检测方法并完成实证评估，数据来自公开来源。
- Confidence: 0.98

## A hierarchical Naïve Bayes model for approximate identity matching

- Year/journal: 2011 / Decision Support Systems
- DOI: 10.1016/j.dss.2011.01.007
- Security status: core_security_attack_defense
- Security reason: 论文针对执法和反恐领域中的身份匹配，核心是检测因故意欺骗（如犯罪分子和恐怖分子使用假身份误导调查）和错误导致的身份不一致，属于威胁检测和防御范畴。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 分层朴素贝叶斯模型（HNB）用于近似身份匹配，结合半监督EM学习
- Evaluation: 使用Tucson警察局COPLINK真实执法数据，对2000个身份比较样本进行10折交叉验证，与精确匹配和记录比较算法在精度、召回率、F值上比较
- Algorithm reason: 提出新的分层朴素贝叶斯模型及半监督学习框架，并实现了完整的身份匹配系统，通过真实数据实验证明了其有效性。
- Data publicness: private_or_nonpublic / Tucson警察局COPLINK数据库中的2.4百万身份记录（非公开执法数据），随机抽取200个嫌疑人记录及人工验证的匹配记录。
- Decision: 论文提出并实证评估了一个新的分层朴素贝叶斯模型用于身份匹配，该模型服务于执法和反恐中的安全需求，能够检测错误和故意欺骗身份；数据来自警方内部数据库，属于非公开数据。
- Confidence: 0.95

## Short Term and Total Life Impact analysis of email worms in computer systems

- Year/journal: 2007 / Decision Support Systems
- DOI: 10.1016/j.dss.2006.12.014
- Security status: core_security_attack_defense
- Security reason: 研究邮件蠕虫的破坏性影响分类与早期预测，属于恶意代码攻击的检测与缓解，安全损害对象为系统可用性、数据完整性与组织安全。
- Algorithm status: novel_algorithm_with_evaluation
- Method: 邮件蠕虫影响分类预测框架（Total Life Impact与Short Term Impact，含Tskewness、LMH、Hit density等指标）
- Evaluation: 使用Symantec与Messagelabs的93个邮件蠕虫数据，比较STI与TLI框架的匹配率（三维约59.2%）并用GSI验证，呈现周/月趋势。
- Algorithm reason: 论文提出并实现了新的蠕虫影响分类与预测框架，并基于93个蠕虫数据进行了统计验证与比较。
- Data publicness: public / Symantec和Messagelabs公开网站上2003年至2004年的邮件蠕虫记录。
- Decision: 该文以邮件蠕虫恶意代码为对象，提出新的影响分类与早期预测框架，核心是安全威胁的检测与缓解；框架被实现并进行93个真实蠕虫数据的实证评估；数据来自公开渠道，故纳入。
- Confidence: 0.95
