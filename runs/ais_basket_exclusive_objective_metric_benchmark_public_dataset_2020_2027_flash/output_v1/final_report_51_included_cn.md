# AIS Basket 2020–2027 筛选：51 篇命中文献详细介绍

- 筛选条件（三模块同时通过）：① 以完全客观指标提升为唯一核心目标；② 全文存在明确 benchmark 表述并支撑核心提升主张；③ 评价使用公开可查到、可获取的数据集。
- 语料：`database_fulltext_all` 2020–2027 共 2,475 篇；模型 `deepseek-v4-flash`（temperature=0），并发 20，全部完成、0 失败。
- 结果：**51 篇命中**（客观指标通过 197、benchmark 通过 162、公开数据集通过 281 的交集）。
- 期刊分布：Decision Support Systems 18 / Information Systems Research 14 / MIS Quarterly 9 / Journal of Management Information Systems 5 / Information & Management 3 / Journal of the Association for Information Systems 2。
- 年份分布：2020: 11、2021: 12、2022: 6、2023: 10、2024: 5、2025: 5、2026: 2。
- 数据源类型概览：公开免费数据集约 30 篇（UCI/Kaggle/OpenML、MovieLens、TDT、NEEL16、DAIC-WOZ、OPP-115、Epinions/Slashdot、Opportunity、Yelp/Amazon、BPI 等）；平台/公开 API 约 8 篇（Reddit、LinkedIn、eToro、LendingClub、VirusTotal、黑客论坛等）；政府/机构开放数据约 9 篇（Florida AHCA、CMS、FINRA、World Bank/IMF、荷兰 CBS、EPEX、Statista 等）；商业订阅数据约 10 篇（CRSP、Compustat/WRDS、CSMAR、I/B/E/S、Bloomberg、Diane、Comscore 等，多为混用）。
- 结论：51 篇全部属于"提出新方法/模型/框架 + 在公开数据上与基线/SOTA 比较证明客观指标提升"的算法开发型论文。

---

## 2020 年（11 篇）

### 1. 2020 · Journal of Management Information Systems · A Novel Recommendation Model for Online-to-Offline Service Based on the Customer Network and Service Location
- DOI：10.1080/07421222.2020.1759927
- **面对的问题**：O2O（线上到线下）服务推荐中，用户—商家网络、服务位置等异构信息未被充分利用，数据稀疏、冷启动条件下推荐精度低。
- **用的数据**：MovieLens 100K（公开标准推荐数据集）、大众点评（Dianping）官方公开网站数据、Google Maps 地理数据。
- **做了什么**：提出融合客户网络、服务位置与网络属性的推荐模型 CNLRec（含不含位置信息的 CNRec 变体），在低数据密度条件下显著优于多种主流推荐方法。
- **核心指标**：Precision、Recall、F-Score。
- **对比方法**：User-based CF、Item-based CF、H-CF、Matrix Factorization、Deep Learning、Cross-domain/Latent model、Neural Network。

### 2. 2020 · Decision Support Systems · A dynamic classification unit for online segmentation of big data via small data buffers
- DOI：10.1016/j.dss.2019.113157
- **面对的问题**：大数据流场景下在线分割（segmentation）需要随新数据增量更新，静态或全量重算代价高，难以满足实时性。
- **用的数据**：Lev 数据集、UCI Occupancy-Detection 数据集、Kaggle deepScapulaSSM 数据集。
- **做了什么**：提出基于小数据缓冲的增量动态分类单元（增量动态分割机制），与静态、动态（无限制缓冲）方法系统比较，证明在运行时间和分割保真度上的效率优势。
- **核心指标**：运行时间、段内距离 RMSE（均值/标准差）、最终段数/更新次数。
- **对比方法**：静态方法、动态无限制缓冲方法、决策树（初步聚类可行性对比）。

### 3. 2020 · Information & Management · Discovering event episodes from sequences of online news articles: A timeadjoining frequent itemset-based clustering method
- DOI：10.1016/j.im.2020.103348
- **面对的问题**：新闻流中同一事件的相关报道需要聚成 episode（事件片段），传统聚类方法忽略报道在时间上的相邻性。
- **用的数据**：TDT2、TDT3（公开 Topic Detection and Tracking 标准语料）及基于其构建的 Nallapati et al. 事件语料（53 事件、248 episode、1,468 篇新闻）。
- **做了什么**：提出时间相邻频繁项集（time-adjoining frequent itemset）聚类方法 TAFIED，发现事件 episode，并与多种基准聚类方法比较（F-measure 0.584 最优，Wilcoxon 检验显著）。
- **核心指标**：聚类召回率、聚类精确率、F-measure。
- **对比方法**：FIHC、HAC、HAC+TD、FIHC+TP（扩展分析）。

### 4. 2020 · Decision Support Systems · Geo-semantic-parsing: AI-powered geoparsing by traversing semantic knowledge graphs
- DOI：10.1016/j.dss.2020.113346
- **面对的问题**：从文本（如推特）中自动识别并链接地理位置（geoparsing）的准确率低，现有方法难以处理非正式文本。
- **用的数据**：NEEL16（2016 命名实体识别与链接挑战赛官方数据集，9,289 条英文推文、5,348 个地点标注）。
- **做了什么**：提出语义知识图谱遍历式地理解析方法 GSP，在 NEEL16 上与 2 个基线、3 个现有方法比较，F1=0.665，显著优于次优方法（0.553）。
- **核心指标**：F1、Precision、Recall、平均处理时间。
- **对比方法**：naïve geoparser、NER+geocoder、Middleton et al.、Halterman、Avvenuti et al.。

### 5. 2020 · Information Systems Research · Hiding Sensitive Information when Sharing Distributed Transactional Data
- DOI：10.1287/isre.2019.0898
- **面对的问题**：多方共享事务数据时，关联规则挖掘可能泄露敏感规则，需要在隐藏敏感信息的同时尽量保持数据效用。
- **用的数据**：Retail、BMS-POS 公开事务数据集（另有 IBM 生成器合成数据）。
- **做了什么**：提出在分布式事务数据库中隐藏敏感关联规则的优化方法，与文献基准算法比较可扩展性与解质量。
- **核心指标**：修改后数据库的准确性（未被修改事务比例）、被清洗的事务数、求解时间、产生/丢失的规则数。
- **对比方法**：三种文献基准隐藏算法。

### 6. 2020 · Journal of Management Information Systems · Human Identification for Activities of Daily Living: A Deep Transfer Learning Approach
- DOI：10.1080/07421222.2020.1759961
- **面对的问题**：智能家居/养老场景中需要识别"谁在做日常活动"（HID，人类身份识别），但跨环境、跨设备泛化困难。
- **用的数据**：HANDY（公开 benchmark 数据集）、Opportunity 对象传感器数据集（OPPO）。
- **做了什么**：提出 CNN-HID 及深度迁移学习变体 DTL-HID，在四个实验（HANDY 与 OPPO 多传感器场景）中与非迁移基线和迁移变体比较，显著优于全部基准。
- **核心指标**：Accuracy、Precision、Recall、F1、AUC。
- **对比方法**：kNN、SVM、Naive Bayes、Decision Tree、CNN-HID/T、CNN-HID/CA 及非迁移 DTL 变体。

### 7. 2020 · Journal of Management Information Systems · Mining Semantic Soft Factors for Credit Risk Evaluation in Peer-to-Peer Lending
- DOI：10.1080/07421222.2019.1705513
- **面对的问题**：P2P 借贷违约预测中，借款人软信息（如文本语义）未得到充分利用，仅靠硬特征判别力有限。
- **用的数据**：LendingClub 历史贷款数据（公开可获取）。
- **做了什么**：挖掘语义软因子用于信用风险评估，与硬特征、LDA 主题特征、统计/可读性/情感特征等基线比较，证明加入语义软特征显著提升判别性能并降低授信组合违约率。
- **核心指标**：AUC、KS、H measure、所选组合的违约率。
- **对比方法**：LR、LASSO、RF、XGB 的硬特征/软特征组合、LDA 主题特征等。

### 8. 2020 · Decision Support Systems · Network projection-based edge classification framework for signed networks
- DOI：10.1016/j.dss.2020.113321
- **面对的问题**：社交网络中的符号边（信任/不信任）分类在数据稀疏、类别非平衡条件下性能有限。
- **用的数据**：Epinions、Slashdot Zoo、Wikipedia RfA、Yeast GIN 四个公开标准网络数据集。
- **做了什么**：提出基于网络投影的符号边分类框架 NPECF，在平衡/非平衡预处理及多种标记边比例下与现有方法比较，绝大多数设置最优。
- **核心指标**：Accuracy、Geometric Mean、Diagnostic Odds Ratio。
- **对比方法**：SRWR、NbA。

### 9. 2020 · Information Systems Research · Predicting Labor Market Competition: Leveraging Interfirm Network and Employee Skills
- DOI：10.1287/isre.2020.0954
- **面对的问题**：企业如何预测未来可能发生劳动力竞争（员工跨企业流动）的竞争对手企业。
- **用的数据**：LinkedIn 公开个人资料、Yahoo BOSS API、Compustat North America（订阅数据库）。
- **做了什么**：构建企业—年度面板，综合经济、产品重叠、劳动力重叠、网络重叠四类特征，比较多种机器学习模型，证明网络与技能特征提升新劳动力市场竞争者识别能力。
- **核心指标**：AUC、新竞争者识别比例。
- **对比方法**：KNN、LR、SVM、CART、Bagging(LR/SVM)、RF、MLP、CNN 及随机分类器。

### 10. 2020 · Information & Management · What reveals about depression level? The role of multimodal features at the level of interview questions
- DOI：10.1016/j.im.2020.103349
- **面对的问题**：临床访谈中哪些问题级多模态特征（语言、声学等）最能揭示抑郁严重程度。
- **用的数据**：DAIC-WOZ 公开研究语料（142 名受访者、7,866 条问题级回答）。
- **做了什么**：训练两层多模态预测模型，在问题级特征上与单模态/双模态基线和个体层基线比较，显著降低 PHQ-8 抑郁评分预测误差。
- **核心指标**：PHQ-8 分数的 MAE、RMSE。
- **对比方法**：单模态/双模态基线（B1）、个体层基线（B2_SVR/B2_RF）。

### 11. 2020 · Journal of the Association for Information Systems · Who Is the Next "Wolf of Wall Street"? Detection of Financial Intermediary Misconduct
- DOI：10.17705/1jais.00633
- **面对的问题**：金融中介（经纪人）不当行为检测中，自我披露信息可能被操纵，如何利用外部验证信息（监管确认、用户确认）提升检测。
- **用的数据**：FINRA BrokerCheck（公开监管数据库）、LinkedIn 公开资料。
- **做了什么**：构建多组分类器比较不同信息验证水平（自披露 vs 监管确认 vs 用户确认），证明加入监管确认信息显著提升不当行为检测性能与经济收益。
- **核心指标**：准确率、召回率、精确率、F1、AUC、经济收益。
- **对比方法**：Classifier A/B（自披露）、Classifier E/F（监管/用户确认）等组合（McNemar 检验）。

---

## 2021 年（12 篇）

### 12. 2021 · MIS Quarterly · A Deep Learning Approach for Recognizing Activity of Daily Living (ADL) for Senior Care: Exploiting Interaction Dependency and Temporal Patterns
- DOI：10.25300/misq/2021/15574
- **面对的问题**：养老照护中联合使用人体/物体传感器识别日常活动（ADL），传统模型忽视跨传感器依赖与时间模式。
- **用的数据**：Opportunity（OPPO）公开数据集（核心测试床）；INTER 为作者自采（仅用于交互提取组件，少量私有补充）。
- **做了什么**：提出多层次 ADLR 框架（I-CNN、I-CNN-GR、S2S_GRU 组件），端到端识别交互、手势与活动，四个实验与多种基准比较并做配对 t 检验。
- **核心指标**：宏平均 F1、Accuracy、平均块 Levenshtein 距离（ABLD）。
- **对比方法**：kNN、SVM、Decision Tree、CNN-1D/2D、DeepConvLSTM、HMM、S2S_LSTM、SAE+SVM、LDA 主题模型等。

### 13. 2021 · Information Systems Research · A Graph-Based Ant Algorithm for the Winner Determination Problem in Combinatorial Auctions
- DOI：10.1287/isre.2021.1031
- **面对的问题**：组合拍卖胜者确定问题（WDP）是 NP-hard 优化问题，需要在短时间内得到高质量解。
- **用的数据**：Lau and Goh (2002) 94 个公开测试实例、Combinatorial Auction Test Suite（CATS，Leyton-Brown et al. 2002）。
- **做了什么**：提出基于图的蚁群算法 TrACA，与 20 种现有启发式及 CPLEX、Max W Clique 精确算法系统比较，证明求解质量与速度优势。
- **核心指标**：求解质量（相对最优解百分比）、运行时间、改进解概率（ISP）、Z 分数。
- **对比方法**：MA、BHS、DDCM、ACLS、SHH、GA、DE、BRKGA 等 20 种启发式 + CPLEX + Max W Clique。

### 14. 2021 · Decision Support Systems · A personalized paper recommendation method considering diverse user preferences
- DOI：10.1016/j.dss.2021.113546
- **面对的问题**：学术论文推荐未充分考虑用户多样化的偏好（如不同研究兴趣维度）。
- **用的数据**：AMiner、DBLP 两个公开学术数据集。
- **做了什么**：提出 PRHN（个性化论文推荐方法），在 Top-N 推荐上与多种异构网络基线比较，Precision 和 Recall 优于基线。
- **核心指标**：Precision、Recall（Top-N 命中率）。
- **对比方法**：BC、CC、MSCN、CAR、Metapath。

### 15. 2021 · Information & Management · A social investing approach for portfolio recommendation
- DOI：10.1016/j.im.2021.103536
- **面对的问题**：社交投资平台上的公开信息能否用于构建收益更优的投资组合。
- **用的数据**：eToro.com 社交投资平台帖子、WRDS 财务报表数据、Yahoo Finance 股价数据。
- **做了什么**：提出 CIR 社交投资组合推荐方法，用 30 个交易日模拟交易，与多种基准推荐方法及 S&P 500 市场基准比较，多数绩效指标更优。
- **核心指标**：投资组合收益率、Treynor 比率、Jensen's alpha。
- **对比方法**：无过滤、仅知识、仅权威三种基准方法 + S&P 500。

### 16. 2021 · Decision Support Systems · Capital shortfall: A multicriteria decision support system for the identification of weak banks
- DOI：10.1016/j.dss.2021.113526
- **面对的问题**：如何连续、自动、及时地识别可能面临资本短缺的"弱银行"，作为早期预警。
- **用的数据**：V-Lab SRISK、NUS CRI（PD/AS）、IMF 金融稳健指标（FSI）、World Bank GFDD、Bloomberg（均为公开或公开订阅渠道）。
- **做了什么**：构建基于 UTADIS 多准则决策方法的银行资本短缺 DSS，与逻辑回归、SRISK、Texas Ratio 在全球/美国/欧洲样本上比较，分类精度全面更优。
- **核心指标**：OCA、ACA、SENS、SPEC、AUROC、KS 距离。
- **对比方法**：Logistic Regression、SRISK、Texas Ratio。

### 17. 2021 · Decision Support Systems · Dynamic self-organizing feature map-based models applied to bankruptcy prediction
- DOI：10.1016/j.dss.2021.113576
- **面对的问题**：企业破产预测中静态模型精度有限，且数据随时间变化。
- **用的数据**：Diane 数据库（Bureau van Dijk 商业订阅数据库）。
- **做了什么**：提出动态自组织特征图（SOFM）模型，与 Cox 生存模型及多种机器学习方法比较，正确分类率、F2、AUC 普遍更优。
- **核心指标**：正确分类率、F2 分数、AUC。
- **对比方法**：Cox、SVM、ELM、Bagging、AdaBoost、XGBoost、Random Subspace、Random Forest。
### 18. 2021 · Journal of Management Information Systems · First, Do No Harm: Predictive Analytics to Reduce In-Hospital Adverse Events
- DOI：10.1080/07421222.2021.1990619
- **面对的问题**：住院期间不良事件（AE）危害患者安全，如何提前预测高风险患者以减少伤害。
- **用的数据**：佛罗里达州 AHCA 住院患者出院数据（州政府公开数据）、CMS Hospital Compare / Physician Compare（公开）、美国医院协会 Healthcare IT 数据库（订阅）。
- **做了什么**：提出 SALT 预测模型（形式化 AE 预测问题并集成混合效应与机器学习），三个实验分别与混合效应模型、替代 ML 技术比较，并模拟防止 AE 数量与成本节省。
- **核心指标**：AUC、精确率、召回率、F 分数、防止的 AE 数量与误报数、成本节省（百万美元）。
- **对比方法**：GLMM、MERT、MERF、CART、DNN、GBM、LR、NB、RF、SVM。

### 19. 2021 · Decision Support Systems · Model identification for ARMA time series through convolutional neural networks
- DOI：10.1016/j.dss.2021.113544
- **面对的问题**：传统 AIC/BIC 准则识别 ARMA 模型阶数存在准确率与计算成本问题。
- **用的数据**：公开 R 包 forecast 的 arima.sim 函数 + 公开发表的 Beadle-Djurić 系数采样算法生成的 10,000 条模拟 ARMA 时间序列（长度 1,000/3,000/10,000，可完全复现）。
- **做了什么**：提出用 CNN 识别 AR/MA 阶数，与 AIC/BIC 的四种变体在统一测试套件上比较，准确率与速度显著更优。
- **核心指标**：AR/MA 阶数识别准确率、识别 MSE、计算时间、预测误差 MAE/RMSE。
- **对比方法**：AIC step-wise/full、BIC step-wise/full、Acme（真实阶数参照）。

### 20. 2021 · Decision Support Systems · Neighbor-aware review helpfulness prediction
- DOI：10.1016/j.dss.2021.113581
- **面对的问题**：评论有用性预测通常只看单条评论，忽略邻居评论（上下文）信息。
- **用的数据**：SiteJabber、ConsumerAffairs 两个公开评论平台数据（论文详细说明采集方式，可复现）。
- **做了什么**：提出邻居感知预测模型 NAP（融合邻居类型/顺序/一致性/情感分歧/熵等上下文），与独立预测和六种上下文基线比较，准确率显著提升 1%–5%。
- **核心指标**：分类准确率。
- **对比方法**：I（CNN 独立预测）、I_MLP、I+ORD_D/R/V、I+CON、I+POL、I+ENT。

### 21. 2021 · Decision Support Systems · Process data properties matter: Introducing gated convolutional neural networks (GCNN) and key-value-predict attention networks (KVP) for next event prediction with deep learning
- DOI：10.1016/j.dss.2021.113494
- **面对的问题**：业务流程事件日志的下一事件预测中，深度模型未充分利用过程数据属性。
- **用的数据**：BPI'11（Hospital Log）、BPI'12、BPI'13、Helpdesk、EnvLog 等 11 个真实事件日志基准数据集及子集。
- **做了什么**：提出门控卷积网络 GCNN 与键值预测注意力网络 KVP，10 折交叉验证，44 个指标-数据集组合中 34 个超过先前方法，并分析过程数据属性的影响。
- **核心指标**：Accuracy、Precision（加权/宏/微）、Recall、F1。
- **对比方法**：LSTM、SAE、RegPFA、MANN、CNN 等。

### 22. 2021 · Decision Support Systems · Recognition of human activities for wellness management using a smartphone and a smartwatch: A boosting approach
- DOI：10.1016/j.dss.2020.113426
- **面对的问题**：日常健康管理中的活动识别（HAR）如何利用多设备（手机+手表）传感器特征。
- **用的数据**：ExtraSensory 公开数据集。
- **做了什么**：为五个基本活动分别构建二分类模型，用 138 个特征训练 XgBoost、AdaBoost、Boosted C5.0，并与标准机器学习方法比较，验证集 AUC 与测试 Accuracy/F1 更优。
- **核心指标**：Accuracy、F1、AUC。
- **对比方法**：Neural Network、SVM、LR、MLP 及先前研究结果。

### 23. 2021 · Decision Support Systems · Simpler is better: Lifting interpretability-performance trade-off via automated feature engineering
- DOI：10.1016/j.dss.2021.113556
- **面对的问题**：可解释模型（如逻辑回归）性能不足，可解释性与性能难以兼得。
- **用的数据**：OpenML100（30 个二分类数据集）、credit-g / German Credit（UCI/OpenML task 31）。
- **做了什么**：提出 SAFE 自动特征工程方法提升简单模型（逻辑回归）性能并保持/提升可解释性（以参数数量倒数衡量），与 vanilla LR、默认/调优 GBM、SVM 比较并做 Wilcoxon 检验。
- **核心指标**：AUC、模型复杂度（参数数量倒数，可解释性代理）。
- **对比方法**：vanilla logistic regression、default/tuned gbm、default svm。

### 24. 2022 · Decision Support Systems · A deep recurrent neural network approach to learn sequence similarities for user-identification
- DOI：10.1016/j.dss.2021.113718
- **面对的问题**：跨设备/跨数据集的用户再识别（点击流序列相似性度量）准确率有限。
- **用的数据**：Comscore Web Behavior Panel（公开商业订阅渠道可获取）。
- **做了什么**：提出 TL-RNN 学习序列相似性，在双选择用户再识别、多用户分配、用户数估计三个任务上与序列比对和度量学习方法比较，多数设置更优。
- **核心指标**：用户再识别准确率（P）、聚类调整兰德指数（ARI）、估计用户数的精确率/召回率。
- **对比方法**：Smith-Waterman 序列比对、TF-RW 度量。

### 25. 2022 · Decision Support Systems · Analysis of third-party request structures to detect fraudulent websites
- DOI：10.1016/j.dss.2021.113698
- **面对的问题**：欺诈网站检测中，仅靠既有第三方使用（3PU）特征判别力不足。
- **用的数据**：Alexa top 50、欧盟委员会假冒与盗版观察名单、USTR 2019 恶名市场审查、Wikipedia 假新闻名单、EasyPrivacy、Cookipedia（均为公开名单/来源）。
- **做了什么**：提出第三方请求结构（RS）特征，与 3PU 特征组合构建检测模型，与朴素基准和既有 3PU 方法比较，组合模型显著提升（如 CS5 准确率 0.728→0.805，加权集成 0.826）。
- **核心指标**：Accuracy、Sensitivity、Specificity、Precision、F1、MCC、Youden J。
- **对比方法**：三种朴素基准、CS5、svmRadial 等 3PU 方法。

### 26. 2022 · Journal of Management Information Systems · Assessing and Enhancing Adversarial Robustness of Predictive Analytics: An Empirically Tested Design Framework
- DOI：10.1080/07421222.2022.2063549
- **面对的问题**：文本分类器（垃圾评论/垃圾邮件检测）易受对抗扰动攻击，鲁棒性缺乏系统度量与增强框架。
- **用的数据**：Deceptive Opinion Spam 数据集（Ott et al., 2013）、Apache SpamAssassin 公开语料。
- **做了什么**：提出 ARText 设计框架（集成学习 + 对抗重训练），用性能比率与性能-扰动曲线下面积度量鲁棒性，在垃圾评论与垃圾邮件两个测试床上与多种基准模型比较，证明鲁棒性提升。
- **核心指标**：对抗鲁棒性性能比率、A/P、P/P、R/P、F/P、ROC/P 曲线下面积。
- **对比方法**：NB、RF、SVM、CNN、GRU、BiGRU、LR、LSTM、BiLSTM。

### 27. 2022 · Information Systems Research · Developing a Composite Measure to Represent Information Flows in Networks: Evidence from a Stock Market
- DOI：10.1287/isre.2021.1066
- **面对的问题**：企业网络中的信息流如何测度，以及能否提升股票异常收益预测。
- **用的数据**：新浪财经（Sina Finance）公开数据、CSMAR、CNRDS / 东方财富论坛数据。
- **做了什么**：构建信息流复合度量 EAC，用 Fama-MacBeth、SVR、MLP、决策树、RF、GBDT 等验证，与不含 EAC 的基准及 degree/closeness/betweenness/PageRank 等替代指标比较（bootstrap 置信区间），预测误差显著更低。
- **核心指标**：RMSE、MAE、MAPE、投资组合超额收益（Alpha）。
- **对比方法**：Fama-MacBeth、SVR、MLP、DT、RF、GBDT、degree/closeness/betweenness/PageRank。

### 28. 2022 · Decision Support Systems · Fraudulent review detection model focusing on emotional expressions and explicit aspects: investigating the potential of feature engineering
- DOI：10.1016/j.dss.2021.113728
- **面对的问题**：欺诈评论检测中情感表达与显式方面特征的工程化潜力。
- **用的数据**：Yelp 评论数据集（Rayana and Akoglu）、Yelp Open Dataset、Amazon 评论数据集、UCI 数据集。
- **做了什么**：提出情感 + 显式方面特征工程方法，结合 M-SMOTE 处理不平衡，在多个基准数据集上与无预处理/SMOTE 基线及先前研究比较，P/R/F1/AUC 更优。
- **核心指标**：Precision、Recall、F1、AUC。
- **对比方法**：baseline（无预处理/不平衡数据）、SMOTE、先前研究方法。

### 29. 2022 · Information Systems Research · Modifying Transactional Databases to Hide Sensitive Association Rules
- DOI：10.1287/isre.2021.1033
- **面对的问题**：共享事务数据库时隐藏敏感关联规则，需要最小化对数据的破坏且不引入虚假规则。
- **用的数据**：retail、bms-pos 公开数据集，以及 IBM 公开合成数据生成器生成的 10m/50m/100m 数据集。
- **做了什么**：提出最优线性化方法求解隐藏问题，与三种文献基准算法比较，证明在可扩展性与解质量上的显著优势。
- **核心指标**：修改后数据库的准确性（未被修改事务比例）、被清洗的事务数、求解时间、产生/丢失规则数。
- **对比方法**：三种文献基准隐藏算法。

---

## 2023 年（10 篇）

### 30. 2023 · Decision Support Systems · A deep learning approach for detecting fake reviewers: Exploiting reviewing behavior and textual information
- DOI：10.1016/j.dss.2022.113911
- **面对的问题**：假评论者（fake reviewer）检测中行为特征与文本信息未有效联合利用。
- **用的数据**：YelpZIP、YelpNYC（Yelp 公开数据集）。
- **做了什么**：提出行为敏感特征提取器 + 完整深度学习框架，两个实验（仅行为特征、全特征）与多个基准方法比较，全部指标显著更优（配对 t 检验）。
- **核心指标**：Accuracy、Precision、Recall、F1、AUC。
- **对比方法**：多组基准方法（行为/文本特征变体）。

### 31. 2023 · Decision Support Systems · Assuring quality and waiting time in real-time spatial crowdsourcing
- DOI：10.1016/j.dss.2022.113869
- **面对的问题**：实时空间众包任务分配需要同时保证等待时间与结果质量（工人信誉）。
- **用的数据**：GAIA 开放数据集（成都 2016 年 11 月订单数据，滴滴公开发布）。
- **做了什么**：提出 TP-TASC 任务分配框架，构建仿真场景，与基线方法 RB-TPSC 比较不同任务半径、有效期、信誉条件下的等待时间与结果质量。
- **核心指标**：平均等待时间、平均信誉值、平均成本、分配率、平均行驶距离。
- **对比方法**：RB-TPSC。

### 32. 2023 · Information Systems Research · Augmenting Social Bot Detection with Crowd-Generated Labels
- DOI：10.1287/isre.2022.1136
- **面对的问题**：社交机器人检测的标签获取困难，众包反应（crowd reaction）能否作为额外信号增强检测。
- **用的数据**：Reddit 公开 API 数据（r/BotWatchman 社区维护 bot 名单）、Cresci et al. (2017) Twitter social spambot 数据集。
- **做了什么**：提出用众包反应与言语行为特征增强机器人检测模型，通过受限特征消融 benchmark 与公开 Cresci 数据集上的 BERT 基线直接比较，证明性能提升或可比。
- **核心指标**：Precision、Recall、F1、AUC。
- **对比方法**：传统模型、Garcia-Silva 等 BERT 基线、消融变体。

### 33. 2023 · Information Systems Research · Diversity Preference-Aware Link Recommendation for Online Social Networks
- DOI：10.1287/isre.2022.1174
- **面对的问题**：在线社交网络链接推荐需要考虑用户对多样性的偏好，而不仅是准确率。
- **用的数据**：Google+ 数据集（Gong et al., 2012，公开下载）。
- **做了什么**：提出 DPA-LR 多样性偏好感知链接推荐方法，与四种多样化方法和三种 SOTA 链接推荐方法比较，DPMS、Precision、Recall、F1 全面更优（p<0.001）。
- **核心指标**：多样性偏好匹配得分（DPMS）、Precision、Recall、F1。
- **对比方法**：MMR、MSD、DPP、DiRec、GCN-LR、GraphSage-LR、GAT-LR。

### 34. 2023 · Information Systems Research · Estimating Life Cycle Sales of Technology Products with Frequent Repeat Purchases: A Fractional Calculus-Based Approach
- DOI：10.1287/isre.2022.1131
- **面对的问题**：存在频繁重复购买的技术产品生命周期销售预测（传统 Bass 类扩散模型拟合与预测不足）。
- **用的数据**：Notebook 年销量（2005–2014）、PC 全球年销量（Statista）、澳大利亚 DVD 销量（Screen Australia）、iPad 季度销量（Apple 财报）、Samsung 平板销量、美国 DVD 采用数据（CTA/DEG/Statista）等 6 个公开来源数据集。
- **做了什么**：提出基于分数阶微积分的 GDMR 模型，与两个 Bass 基准变体及 ARIMA、LSTM、KNN、RF、Holt 等通用预测模型比较，拟合（R²）与 1/2/8 年预测（MAPE）多数更优。
- **核心指标**：拟合优度 R²、预测准确度 MAPE、采用趋势恢复准确度。
- **对比方法**：Bass-KB-BHL、Bass-KB-Steffens、ARIMA、LSTM、KNN、Random Forest、Holt。
### 35. 2023 · MIS Quarterly · Exploiting Expert Knowledge for Assigning Firms to Industries: A Novel Deep Learning Method
- DOI：10.25300/misq/2022/17171
- **面对的问题**：自动给企业分配行业分类（NAICS/GICS）时，现有方法忽视行业定义知识、结构知识与赋值知识的时间特性。
- **用的数据**：Compustat Company Header History（COMPHIST，经 WRDS 订阅获取）、Loughran-McDonald Stage One 10-X Parse 数据（公开）。
- **做了什么**：提出 DeepIA 深度学习方法（动态行业表示 + 层次赋值），用 2012–2015 年训练、2016 年新企业测试，与五种基线/现有方法比较，准确率、宏 F1、误分类成本全面更优并报告显著性。
- **核心指标**：分类准确率、宏平均 F1、误分类成本。
- **对比方法**：SVM-IA、MLP-IA、ULMFiT-IA、HC-IA、LE-IA。

### 36. 2023 · MIS Quarterly · Extracting Actionable Insights from Text Data: A Stable Topic Model Approach
- DOI：10.25300/misq/2022/16957
- **面对的问题**：LDA 主题模型结果不稳定（随机种子敏感），影响下游文本分析结论的可靠性。
- **用的数据**：Amazon Product Review（Ni et al., 2019，公开）、Yelp Restaurant Review（Yelp 数据集挑战）、StackExchange Q&A（公开转储）、Company Description（Qader et al., 2018）。
- **做了什么**：提出 Stable LDA 稳定化主题模型方法，与标准 LDA 及多种稳定性缓解方法比较，稳定性显著提升且不降低模型质量，并用下游计量经济分析验证。
- **核心指标**：稳定性指标（S_doc_prob、S_doc_label、S_topic_prob、S_topic_topwords）、Perplexity、C_v/C_uci、下游回归系数一致性。
- **对比方法**：LDA、Doc LDA、Ensemble LDA、Granulated LDA、MRF-LDA、CRFTM。

### 37. 2023 · Information Systems Research · Pricing in Nonconvex Markets: How to Price Electricity in the Presence of Demand Response
- DOI：10.1287/isre.2022.1139
- **面对的问题**：需求响应存在时电力市场非凸定价会产生巨大的 make-whole payments（补偿款），损害效率。
- **用的数据**：IEEE RTS-96（公开标准测试系统）、Garcia-Bertrand et al. (2006) 算例报价曲线、Zoltowska (2016) 报价数据。
- **做了什么**：提出 PBE-A/PE-A 定价规则，在价格无弹性、价格敏感、可平移负荷等场景下与 IP pricing、ELMP、AIC pricing 比较，大幅降低 make-whole payments 与罚金。
- **核心指标**：make-whole payments（总额及占比）、市场电价（均值/标准差）、罚金、计算时间。
- **对比方法**：IP pricing、ELMP、AIC pricing。

### 38. 2023 · MIS Quarterly · Unlocking the Power of Voice for Financial Risk Prediction: A Theory-Driven Deep Learning Design Approach
- DOI：10.25300/misq/2022/17062
- **面对的问题**：财报电话会议中的语音信息（高管语气）能否提升金融风险（波动率）预测。
- **用的数据**：Seeking Alpha（电话会议文本，公开网站）、EarningsCast（对应音频）、Compustat（财务基本面）、CRSP（股价）。
- **做了什么**：提出理论驱动的深度学习方法 DeepVoice（融合语音特征、基本面与历史风险），与市场基准模型及多种深度学习/机器学习基准比较，样本外 R² 显著更优，并验证期权交易策略收益。
- **核心指标**：MSE、样本外 R²_oos、期权交易策略收益。
- **对比方法**：Sridharan (2015) 市场基准、Concat-SVR、Concat-GradientBoosting、One-stage LSTM、Contextual LSTM、DeepVoice-attention、Emotion 模型等。

### 39. 2023 · Information Systems Research · sDTM: A Supervised Bayesian Deep Topic Model for Text Analytics
- DOI：10.1287/isre.2022.1124
- **面对的问题**：主题模型与下游监督预测任务分离，无监督表示不直接服务于预测目标。
- **用的数据**：Yelp.com 消费者评论、Stack Exchange 知识社区（均为公开平台数据）。
- **做了什么**：提出监督贝叶斯深度主题模型 sDTM，模型拟合与预测两阶段评价：与 LDA、sLDA、MedLDA、BP-sLDA、sNNTM、NTM 比 perplexity，与 RNN attention、Bi-LSTM、DistilBERT、BERT 比 AUROC/accuracy，多数设置显著更优或与 SOTA 可比。
- **核心指标**：Perplexity、AUROC、Accuracy、回归系数方向与显著性。
- **对比方法**：LDA、sLDA、MedLDA、BP-sLDA、sNNTM、NTM、RNN attention、Bi-LSTM、DistilBERT、BERT。

---

## 2024 年（5 篇）

### 40. 2024 · Decision Support Systems · A hybrid decision support system for adaptive trading strategies: Combining a rule-based expert system with a deep reinforcement learning strategy
- DOI：10.1016/j.dss.2023.114100
- **面对的问题**：股票自适应交易策略中，规则专家系统与深度强化学习如何结合以提升收益并控制风险。
- **用的数据**：Yahoo Finance 公开指数日线数据（S&P 500、NYSE Composite、DAX、CAC40、Hang Seng、KOSPI）。
- **做了什么**：提出 RB+RL+C1+C2 混合交易 DSS（规则专家系统 + DRL + 两个组合组件），在 S&P 500 测试期及崩溃/上涨/下跌子时期与买入持有、纯规则、纯 RL、消融变体及多种既有混合模型比较，并在六只指数基金上扩展验证。
- **核心指标**：累计收益率（%AR）、夏普比率、最大回撤（MDD）、年化/日均收益与标准差、交易信号数。
- **对比方法**：B&H、RB、RL、消融变体、TI+SVM、TI+RF、TI+LSTM、TI+XGBoost+CNN+LSTM。

### 41. 2024 · Decision Support Systems · A novel federated learning approach with knowledge transfer for credit scoring
- DOI：10.1016/j.dss.2023.114084
- **面对的问题**：联邦学习信用评分中，各参与方数据分布异质（Non-IID）导致模型性能下降，如何跨机构迁移知识。
- **用的数据**：Loan Data、HMEQ、Taiwan、Give Me Some Credit（GMSC）、Home Credit（HC）五个公开信用数据集。
- **做了什么**：提出 FedKT 联邦知识迁移方法，在 IID 与 Non-IID 两种划分下与 FedAvg、FedProx、FedCodl 及非联邦 LR/RF/XGBoost 比较，Accuracy、Recall、F1、KS 更优（含 Friedman 检验）。
- **核心指标**：Accuracy、Recall、F1、KS。
- **对比方法**：FedAvg、FedProx、FedCodl、非联邦 LR、RF、XGBoost。

### 42. 2024 · MIS Quarterly · Automated Analysis of Changes in Privacy Policies: a Structured Self-Attentive Sentence Embedding Approach
- DOI：10.25300/misq/2024/17115
- **面对的问题**：隐私政策变更条款的人工审查成本高，需要自动检测与标注。
- **用的数据**：OPP-115（公开隐私政策标注数据集）。
- **做了什么**：提出 SAAS（结构化自注意力句嵌入）方法，与 5 种传统 ML 模型、10 种 DL/attention 模型、3 种消融变体进行 4 组 benchmark 比较，micro-F1 等指标统计显著最优。
- **核心指标**：Micro-averaged F1、Precision、Recall、Hamming loss。
- **对比方法**：5 种传统 ML、10 种 DL/attention 模型、3 种消融变体、自动分割方法。

### 43. 2024 · MIS Quarterly · Creating Proactive Cyber Threat Intelligence with Hacker Exploit Labels: A Deep Transfer Learning Approach
- DOI：10.25300/misq/2023/17316
- **面对的问题**：黑客论坛中的 exploit 帖子需要自动分类（漏洞利用类型）以生成主动网络威胁情报，但标注数据少、域差异大。
- **用的数据**：0day.today、Seebug、ExploitDB、PacketStorm、Metasploit 等公共 exploit 库 + 多个黑客论坛（ground-truth 目标域）。
- **做了什么**：提出深度迁移学习方法 DTL-EL，从公共 exploit 库（源域）迁移到黑客论坛（目标域），与经典 ML、深度序列模型、BERT 及多种迁移学习方法比较，目标域 F1=70.34%，显著更高。
- **核心指标**：Accuracy、Precision、Recall、F1。
- **对比方法**：NB、LR、DT、SVM、XGBoost、LightGBM、RNN、GRU、LSTM、BiLSTM、BiLSTM+attention、adaptive SVM、hard/soft MTL、adversarial、BERT。

### 44. 2024 · Information Systems Research · Proactive Resource Request for Disaster Response: A Deep Learning-Based Optimization Model
- DOI：10.1287/isre.2022.0125
- **面对的问题**：灾害（洪水）响应中资源请求被动滞后，如何从社交媒体主动预测资源需求并优化调度。
- **用的数据**：2021 河南洪水微博数据集（GitHub 公开发布：GiveHenanAHand/henan-rescue-viz-website）+ 模拟数据。
- **做了什么**：提出深度学习优化模型 CNM-PRR，与 8 种基线方法比较，显著降低平均单位需求剥夺成本与时间延迟，提升未来需求满足率。
- **核心指标**：平均单位需求剥夺成本、平均单位需求时间延迟、未来需求满足百分比、fill rate 与公平性指标。
- **对比方法**：ReR、logNormMix-PRR、A-NDTT-PRR、AttnMC-PRR、CTDRP-PRR、LR-NV、DL-NV、logNormMix-IFCFS。

---

## 2025 年（5 篇）

### 45. 2025 · MIS Quarterly · Different but the Same? An Event-Driven Approach to Determine Probabilities of Data Duplication
- DOI：10.25300/misq/2025/18178
- **面对的问题**：实体解析/记录重复检测需要可靠的重复概率（而不只是二分类结果），用于下游风险决策。
- **用的数据**：CENSUS、BABY、BIKES、BOOKS、COSMETICS 五个公开标准数据集（另有私有 INSUR1/INSUR2 仅作迁移验证）。
- **做了什么**：提出事件驱动概率方法（Partitioning、KDE、KDE+附加数据、KDE+语言模型），与 Febrl、RLTK、AWS AutoGluon、Microsoft AutoML 等工具比较，F1、AUC 与校准更优；私有数据不承担核心结果表功能。
- **核心指标**：F1-measure、ROC AUC、可靠性得分/校准曲线。
- **对比方法**：Febrl、RLTK、AWS AutoGluon、Microsoft AutoML、商业工具。

### 46. 2025 · Journal of the Association for Information Systems · GASP: A Graph Augmentation-Based Approach for Sign Prediction of Ties in Social Networks
- DOI：10.17705/1jais.00941
- **面对的问题**：社交网络正负关系（边符号）预测在稀疏、非平衡网络上的性能提升。
- **用的数据**：Epinions、Wikipedia RfA、Slashdot Zoo、Yeast GIN 四个公开基准网络。
- **做了什么**：提出图增强方法 GASP，在不同标记边比例下与四种现有方法比较，绝大多数设置下 Accuracy、Optimized Precision、Macro F1、GM(S,N) 更优。
- **核心指标**：Accuracy、Optimized Precision、Macro F1、特异性与负预测值几何均值 GM(S,N)。
- **对比方法**：NPECF、SRWR、ASiNE、DDRE。

### 47. 2025 · Information Systems Research · Gaining a Seat at the Table: Enhancing the Attractiveness of Online Lending for Institutional Investors
- DOI：10.1287/isre.2022.0638
- **面对的问题**：如何构建在线贷款（P2P）投资组合，使其对机构投资者更有吸引力（更高 IRR、更接近公共市场表现）。
- **用的数据**：LendingClub Loan Data（公开数据集）。
- **做了什么**：提出 GCPP 组合构建框架（线性/非线性），与等权重、风险过滤、线性回归、梯度提升回归、神经网络回归、均值方差等基准组合及 S&P 500、债券、REIT 等传统指数比较，非线性 GCPP 在 IRR、PME 等指标显著更优。
- **核心指标**：内部收益率（IRR）、投资回报率（ROI）、公共市场等价（PME）、IRR 相关性。
- **对比方法**：等权重、风险过滤、回归、梯度提升、神经网络、均值方差组合 + 六大市场指数。

### 48. 2025 · Information Systems Research · Post-Earnings-Announcement Drift Prediction: Leveraging Postevent Investor Responses with Multitask Learning
- DOI：10.1287/isre.2022.0358
- **面对的问题**：盈余公告后漂移（PEAD）预测中，公告后投资者反应信息未被充分利用。
- **用的数据**：S&P Capital IQ 电话会议文本库、CRSP、Compustat、I/B/E/S、Thomson/Refinitiv、RavenPack（均为公开商业订阅数据库）。
- **做了什么**：提出多任务学习模型 FinAux+GradPerp+MQT，在 Russell 3000 及子样本上与 SUE、OLS、PEAD.txt、bi-LSTM、Transformer 等基准比较，解释方差 EV=9.06% 最高，并通过消融验证组件贡献与 alpha。
- **核心指标**：预测精度（EV，explained variance）、经济显著性（alpha）。
- **对比方法**：SUE、OLS、PEAD.txt、bi-LSTM、Transformer。

### 49. 2025 · MIS Quarterly · RADAR: A Framework for Developing Adversarially Robust Cyber Defense AI Agents with Deep Reinforcement Learning
- DOI：10.25300/misq/2024/17339
- **面对的问题**：恶意软件检测器在对抗攻击下容易被绕过，如何系统开发鲁棒的防御 AI 智能体。
- **用的数据**：VirusTotal 恶意软件语料（公开平台/学术许可 API）、Microsoft Windows 干净安装的可执行文件（良性样本）。
- **做了什么**：提出 RADAR 框架（r-VAC 深度强化学习攻击器 + RL-RO 鲁棒化），在两个实验中与 10 种基准攻击方法比较逃避率，鲁棒化后逃避率平均降低约 84%（鲁棒性提升约 7 倍）。
- **核心指标**：逃避率（ER）、假阳性率（FPR）。
- **对比方法**：Random actions、BFA、EvadeHC、Surrogate RNN、Policy Gradient、DDQN、Rainbow、MAB-malware、ACER、A3C、GAMMA。

---

## 2026 年（2 篇）

### 50. 2026 · MIS Quarterly · Shapley Value-Based Feature Attribution for Data Masking
- DOI：10.25300/misq/2025/18502
- **面对的问题**：数据共享前如何量化每个特征对披露风险的贡献，并据此选择掩蔽特征与噪声水平，在降风险的同时保效用。
- **用的数据**：UCI Credit History（免费下载）、MIS Faculty Salary Offers（Galletta 公开网页）、CRSP/Compustat Merged（订阅）。
- **做了什么**：提出基于 Shapley 值的特征归因数据掩蔽框架（risk-only 与 weighted-cost 两种策略），在三个真实数据集上对所有掩蔽方法×模型×度量组合与两个基准掩蔽方法比较，风险降低更优或持平、效用损失更小或持平。
- **核心指标**：披露风险降低百分比（%Δr）、数据效用保持/损失百分比（%Δu）、R²、AAD、RASD。
- **对比方法**：Benchmark I（仅掩蔽机密特征）、Benchmark II（随机掩蔽一半非机密特征）。

### 51. 2026 · Information Systems Research · Toward Sustainable Electricity Markets: Capacity-Based Pricing for Electric Vehicle Smart Charging
- DOI：10.1287/isre.2023.0078
- **面对的问题**：EV 智能充电需求波动大，如何设计定价机制诱导期望充电负荷曲线、匹配可再生能源并满足收入目标。
- **用的数据**：荷兰统计局 CBS 出行数据（免费开放）、EPEX 欧洲电力交易所批发电价（公开/订阅）。
- **做了什么**：提出容量定价机制（AH/CH 及 -Distrib 变体）与启发式方法，在模拟测试床中与三种基准定价比较，CBP-CH 实现最低 RMSE、接近 1 的 PAPR 与更低峰值负荷。
- **核心指标**：RMSE、峰值负荷（Peak）、峰均功率比（PAPR）、收入偏差。
- **对比方法**：固定电价（flat pricing）、与速率无关可变定价、递增阶梯定价（increasing-block pricing）。

---

## 附：阅读提示

- 完整判定细节（各模块 gates、证据引文、排除码）见 `output_v1/decisions.csv` / `decisions.jsonl`。
- 本文件按年份组织；如需按期刊或按主题（推荐/检测/金融/文本/优化/隐私）重新排序，可再生成一版。
- 数据源口径：商业订阅数据（CRSP、Compustat、Bloomberg 等）按"公开商业订阅渠道可获取"纳入；如需收紧为仅免费公开下载，需复核约 10 篇（如第 17、24、27、35、38、48、50 篇等）。