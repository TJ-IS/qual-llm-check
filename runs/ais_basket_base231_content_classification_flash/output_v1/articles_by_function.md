# Articles grouped by primary software function

Completed: 231 / 231

## prediction_detection_and_assessment (75)

### A Data Analytics Framework for Smart Asthma Management Based on Remote Health Information Systems with Bluetooth-Enabled Personal Inhalers

- Year/journal: 2020 / MIS Quarterly
- Logic: 为克服SAM系统高分辨率吸入器数据中传统模型难以识别个体异常吸入事件的问题，本文设计了整合网格化数据转换、CAR相关结构和离差子模型的GLMM-GQP检测框架，并以AUC为核心的hold-out实验证明其优于六种基准方法，实现了更准确的偏离模式吸入使用检测。
- Objective family: analytic_quality
- Context: healthcare_and_care
- Tags: 哮喘吸入器使用异常检测, 蓝牙吸入器远程监测, GLMM-GQP统计模型, 网格化时间模式分析

### A generic framework for sentiment analysis: Leveraging opinion-bearing data to inform decision making

- Year/journal: 2020 / Decision Support Systems
- Logic: 针对情感分析框架缺乏通用模型开发流程和深层结果分析的问题，文章设计了ECCO框架来引导用户完成数据预处理、模型选择三元组调优以及情感与结构化属性联合分析，并通过四个跨领域案例证明该流程可训练出与文献基准相当或更优的情感分类器，同时生成可支撑决策的洞察。
- Objective family: analytic_quality
- Context: general_or_cross_domain
- Tags: 通用情感分析框架, 模型选择三元组, 意见文本与结构化数据联合分析, 跨领域案例验证

### A new emergency decision support system: the automatic interpretation and contextualisation of events to model a crisis situation in real-time

- Year/journal: 2020 / Decision Support Systems
- Logic: 针对危机管理中人工解读异构事件流困难的问题，本文设计AIC组件将复杂事件处理引擎与Neo4J危机情境模型连接起来，用解释和情境化规则自动检测危险、风险与事件并持续更新通用作战图，通过5个洪水场景实测解释和情境化时延均低于3秒，证明系统可近实时支持应急决策。
- Objective family: technical_system_performance
- Context: public_sector_crisis_and_humanitarian
- Tags: 危机态势感知, 复杂事件处理, 通用作战图, 洪水应急决策支持

### A two-stage machine learning framework to predict heart transplantation survival probabilities over time with a monotonic probability constraint

- Year/journal: 2020 / Decision Support Systems
- Logic: 针对移植后多期生存概率预测不单调且缺乏个性化的问题，文章提出先用独立机器学习模型预测各时间点生存概率、再用等渗回归进行单调校准的两阶段框架，并在UNOS心脏移植数据上以AUC、G-Mean等指标证明该框架在保证单调性的同时取得与文献相当或更优的预测性能。
- Objective family: analytic_quality
- Context: healthcare_and_care
- Tags: 心脏移植生存预测, 等渗回归单调校准, 个性化生存概率曲线, UNOS登记数据

### Antisocial online behavior detection using deep learning

- Year/journal: 2020 / Decision Support Systems
- Logic: 针对社交媒体平台反社会行为文本检测问题，文章构建并比较了从词典、传统机器学习到CNN/GRU/HAN/psHAN及BERT等多种文本分类器，以Average Precision、AUC和F1为指标，发现全参数BERT总体最优，但部分小数据集上简单模型已接近复杂模型，同时加入LIME解释模块支持审核决策。
- Objective family: analytic_quality
- Context: digital_platform_social_media_and_crowdfunding
- Tags: 反社会在线行为检测, psHAN, LIME可解释性, BERT/DistilBERT

### Automated dynamic approach for detecting ransomware using finite-state machine

- Year/journal: 2020 / Decision Support Systems
- Logic: 针对勒索软件变种难以通用检测的问题，文章设计了基于有限状态机的动态行为监控系统，通过文件、资源、持久化和横向移动事件的状态转换识别攻击，并在1975个样本上取得99.54%准确率和0%误报率。
- Objective family: analytic_quality
- Context: cybersecurity_fraud_and_compliance
- Tags: 勒索软件检测, 有限状态机建模, 动态行为监控, Windows端点防护

### Bayesian neural networks for flight trajectory prediction and safety assessment

- Year/journal: 2020 / Decision Support Systems
- Logic: 为支撑航路安全，文章用Apache Spark从FAA SWIM FIXM数据提取航迹，训练贝叶斯DNN做高精度单步偏差预测、贝叶斯LSTM做多步轨迹预测并将两者融合，通过RMSE/MAE和空间距离验证融合模型显著优于单独LSTM，再以概率间隔距离评估两机安全。
- Objective family: analytic_quality
- Context: logistics_transport_supply_chain_and_manufacturing
- Tags: 蒙特卡洛dropout不确定性量化, DNN-LSTM多保真融合, FAA SWIM FIXM航迹解析, 飞行间隔安全评估

### Deep learning for detecting financial statement fraud

- Year/journal: 2020 / Decision Support Systems
- Logic: 针对年报舞弊筛查中MD&A文本上下文未被充分利用的问题，本文用HAN融合财务比率与MD&A全文输出舞弊概率和红旗句子，以AUC、敏感度、F2等指标评估，发现HAN在FIN+TXT上AUC达0.9264、敏感度90%，优于基准模型并提供可解释线索。
- Objective family: analytic_quality
- Context: cybersecurity_fraud_and_compliance
- Tags: 财务报表舞弊检测, MD&A文本挖掘, 分层注意力网络(HAN), 红旗句子可解释性

### Design Principles for Signal Detection in Modern Job Application Systems: Identifying Fabricated Qualifications [theory subset]

- Year/journal: 2020 / Journal of Management Information Systems
- Logic: 针对招聘申请中虚假资历难以识别的问题，本文设计并实现了一个基于网络摄像头异步视频面试的行为信号检测系统SIGHT，用语音、面部和语言等多模态信号分类回答真伪，结果表明其F1达0.95左右，明显优于人类测谎水平。
- Objective family: analytic_quality
- Context: enterprise_work_and_knowledge
- Tags: 自动化视频面试, 资历造假检测, 多模态行为信号, 招聘信号系统

### Designing scalability in required in-class introductory college courses [theory subset]

- Year/journal: 2020 / Information & Management
- Logic: 针对大型必修面授课在资源约束下难以同时维持师生互动与反馈质量的问题，文章依据干预理论提出元需求和设计原则，构建了以自动Word/Excel评分和PDF反馈报告为核心的课程社会技术制品，通过自然主义评价证明自动评分比人工更准更快且课程被接受，但作业完成率下降表明仍需引入数字触发器来维持学习节奏。
- Objective family: analytic_quality
- Context: education_training_and_learning
- Tags: 自动评分系统, 翻转课堂, 数字数据流, PDF反馈报告

### Feedback at scale: designing for accurate and timely practical digital skills evaluation [theory subset]

- Year/journal: 2020 / European Journal of Information Systems
- Logic: 为在大规模班级中提供准确及时的数字技能反馈，文章设计并迭代了一个由课程应用和Python评分引擎组成的社会技术制品，通过教学目标排序、作业分块/结构化起始文件和基于XML的自动判错相结合，使评分速度比人工快两个数量级、误报漏报率低于人类评分者，并提高了学生完成可选练习的比率。
- Objective family: multi_objective_or_tradeoff
- Context: education_training_and_learning
- Tags: 数字技能测评, Office文件自动批改, 规模化学习反馈, 作业分块设计

### ForeSim-BI: A predictive analytics decision support tool for capacity planning

- Year/journal: 2020 / Decision Support Systems
- Logic: 针对维修组织无法准确预测未来维修工作量从而难以规划产能的问题，文章构建了集成AHW预测、贝叶斯更新、仿真与贝叶斯网络的ForeSim-BI工具，以8C检查真实数据和现行工程估计为对照、用PE/MAE/MAPE评价，结果表明更新后总工作量误差可降至0%，并显著优于现行估计、具备成本节约潜力。
- Objective family: analytic_quality
- Context: logistics_transport_supply_chain_and_manufacturing
- Tags: 航空维修产能规划, 维护工作量预测, 贝叶斯更新, C检工作量分解

### Geo-semantic-parsing: AI-powered geoparsing by traversing semantic knowledge graphs

- Year/journal: 2020 / Decision Support Systems
- Logic: 针对社交媒体文本缺乏显式地理信息导致现有地理解析方法在全球尺度上性能不足的问题，文章设计GSP，通过语义标注链接知识图谱实体、水平遍历知识图谱扩展候选地理实体、并用梯度提升回归选择最佳实体，在NEEL16推文数据集上以F1=0.665超过已有技术（F1≤0.55）。
- Objective family: analytic_quality
- Context: general_or_cross_domain
- Tags: 知识图谱遍历, 语义标注, 地理编码, 位置消歧

### Human Identification for Activities of Daily Living: A Deep Transfer Learning Approach

- Year/journal: 2020 / Journal of Management Information Systems
- Logic: 为解决物体运动传感器数据稀缺下多住户ADL执行者识别问题，本文设计了同时抽取时间与跨轴运动模式并利用可穿戴传感器数据迁移的CNN-HID/DTL-HID框架；在OPPO物体传感器数据上评估显示，该方法以0.707的微平均准确率显著优于所有非迁移和单依赖基准。
- Objective family: analytic_quality
- Context: healthcare_and_care
- Tags: 多住户身份识别, 物体运动传感器, 深度迁移学习, 日常活动监测

### Improving healthcare access management by predicting patient no-show behaviour

- Year/journal: 2020 / Decision Support Systems
- Logic: 针对波哥大初级保健项目高失约率问题，本文构建了基于ML的DSS预测患者失约概率并用LRP增强可解释性，以AUROC和干预覆盖/风险指标比较模型，发现one-hot神经网络能在30%高危干预组中覆盖约72%的真实失约者。
- Objective family: analytic_quality
- Context: healthcare_and_care
- Tags: 失约预测, 患者风险分层, 医疗可及性管理, LRP可解释性

### Industry classification with online resume big data: A design science approach

- Year/journal: 2020 / Information & Management
- Logic: 针对现有行业分类滞后且忽略人力资本的问题，文章从在线简历中提取劳动力流动并构建企业网络，用层次化Louvain社区发现生成行业分类；通过平均调整R²和跨行业变异评估，证明该方法优于传统分类和现有最新方法，并且能提前揭示企业进入新行业。
- Objective family: analytic_quality
- Context: general_or_cross_domain
- Tags: 劳动力流动网络, 在线简历大数据, 层次化社区发现, 行业分类时效性

### Predicting shareholder litigation on insider trading from financial text: An interpretable deep learning approach

- Year/journal: 2020 / Information & Management
- Logic: 为解决监管机构难以从年报文本中前瞻识别内幕交易的问题，文章设计了融合层次注意力、业务邻近网络嵌入和MD&A时序变化的可解释深度预测模型，用AUC和十分位覆盖率评价；完整模型AUC达81.22%，超过最优数值基线78.95%，且注意力权重可解释高风险词。
- Objective family: analytic_quality
- Context: cybersecurity_fraud_and_compliance
- Tags: 内幕交易预测, 10-K年报文本挖掘, 可解释注意力机制, 业务邻近网络

### Stratifying no-show patients into multiple risk groups via a holistic data analytics-based framework

- Year/journal: 2020 / Decision Support Systems
- Logic: 针对患者失约预测中的类别不平衡和变量选择难题，文章通过GA/SA交集选变量、RUS平衡数据、ANN建模并将概率分为五级风险，同时开发Web工具；结果表明该框架可将少数类敏感度提升至0.792，阈值分析后AUC达0.950，为诊所提供个体化失约风险信息。
- Objective family: analytic_quality
- Context: healthcare_and_care
- Tags: 患者失约预测, 风险分层, 类别不平衡处理, Shiny决策支持工具

### The effect of intention analysis-based fraud detection systems in repeated supply Chain quality inspection: A context of learning and contract

- Year/journal: 2020 / Information & Management
- Logic: 针对供应链质量欺诈中买方难以判断供应商意图的问题，构建基于BDI的欺诈意图分析DSS；通过2×2重复博弈实验室实验评估买方决策绩效，发现传统合同下IAFDS减少决策时间、抑制检验成本上升并提高拒收正确率，但在惩罚合同下效果被抵消甚至反转。
- Objective family: human_task_performance
- Context: logistics_transport_supply_chain_and_manufacturing
- Tags: 欺诈意图分析, 质量检验决策支持, 重复博弈学习效应, 惩罚合同

### Who Is the Next “Wolf of Wall Street”? Detection of Financial Intermediary Misconduct [theory subset]

- Year/journal: 2020 / Journal of the Association for Information Systems
- Logic: 针对现有方法难以自动识别可能违规金融中介的问题，文章基于信息操纵理论和warranting理论构建融合LinkedIn自我披露、用户确认和BrokerCheck监管确认特征的机器学习分类器；以准确率、召回率、F1、AUC及经济收益评估后，发现加入监管确认信息使分类器在自然分布样本上取得最优检测性能（AUC 82.83%）和最高经济收益，支持自我披露信息与外部验证可用于金融不当行为检测。
- Objective family: analytic_quality
- Context: cybersecurity_fraud_and_compliance
- Tags: 金融中介不当行为检测, LinkedIn自我披露画像, BrokerCheck监管数据匹配, 预测性监管

### A Deep Learning Approach for Recognizing Activity of Daily Living (ADL) for Senior Care: Exploiting Interaction Dependency and Temporal Patterns

- Year/journal: 2021 / MIS Quarterly
- Logic: 针对现有ADL识别忽略人-物交互和跨层级建模的问题，本文设计了一个以2D交互卷积核提取跨传感器依赖、以启发式手势识别和Seq2Seq活动识别组成的层级框架，并在两个真实运动传感器数据集上用F1、Accuracy@1/2和ABLD等指标验证其显著优于多种基线。
- Objective family: analytic_quality
- Context: healthcare_and_care
- Tags: 2D交互卷积核, 人体-物体传感器交互, 层级ADL识别, 居家养老智能监护

### A cross-domain recommender system through information transfer for medical diagnosis

- Year/journal: 2021 / Decision Support Systems
- Logic: 为缓解医疗诊断数据稀疏和特征空间不一致问题，文章提出ITMD系统，通过区间数相异性度量、症状空间对齐和集体矩阵分解从源域迁移知识，并以预测准确率为指标，实验与案例证明其显著优于四个基线。
- Objective family: analytic_quality
- Context: healthcare_and_care
- Tags: 跨域推荐, 区间数相异性度量, 症状空间对齐, 疾病风险预测

### A dynamic simulation approach to support the evaluation of cyber risks and security investments in SMEs

- Year/journal: 2021 / Decision Support Systems
- Logic: 针对静态风险框架难以刻画中小企业网络风险动态的问题，文章设计了基于系统动力学的SMECRA工具，以Snapshot Survey初始化风险状态并模拟不同威胁环境和投资策略下的收入损失；结果显示初始防御较好的Beta五年总成本+损失显著低于Alpha（€1,413,050对€1,728,200，p=0.022），证明了该工具支持安全投资评估的能力。
- Objective family: economic_and_welfare
- Context: cybersecurity_fraud_and_compliance
- Tags: 中小企业网络风险, 系统动力学仿真, 安全投资决策, NIST框架

### A new approximate belief rule base expert system for complex system modelling

- Year/journal: 2021 / Decision Support Systems
- Logic: 为解决传统BRB规则爆炸和难扩展问题，文章提出用独立因子折扣属性权重的单属性近似置信规则构建ABRB专家系统，并以锂离子动力电池健康状态估计为案例，用MSE证明其在保持与BRB相近建模精度的同时结构更紧凑、更易扩展。
- Objective family: analytic_quality
- Context: general_or_cross_domain
- Tags: 近似信念规则, 独立因子, 锂离子蓄电池健康状态估计, 规则库可扩展性

### A simulation-based risk interdependency network model for project risk assessment

- Year/journal: 2021 / Decision Support Systems
- Logic: 针对项目风险评估忽视风险依赖的问题，本文构建 ISM-MCS 风险相互依赖网络模型，用五项依赖型风险指标量化单个风险和项目整体风险，并通过两个案例表明该模型产生不同且更有效的风险排序，所制定的处置行动能最大幅度降低项目总风险损失和风险传播损失。
- Objective family: analytic_quality
- Context: general_or_cross_domain
- Tags: 风险相互依赖网络, 蒙特卡洛模拟, 解释结构模型, 风险处置行动评估

### A technique for determining relevance scores of process activities using graph-based neural networks

- Year/journal: 2021 / Decision Support Systems
- Logic: 为解决过程分析师难以从仅含频率/时长信息的过程模型中发现绩效问题根因的问题，文章设计GRM将事件日志转为实例图并用GGNN学习流程结果预测，再以注意力权重作为各活动相关性分数来标注过程模型；定量评估显示GRM的预测质量和相关性有效性可对标甚至优于主流方法，案例研究表明这些分数能帮助分析师定位延迟原因。
- Objective family: analytic_quality
- Context: general_or_cross_domain
- Tags: 流程活动相关性分数, 门控图神经网络, 过程挖掘与过程分析, 根因分析

### Applied machine learning for a zero defect tolerance system in the automated assembly of pharmaceutical devices

- Year/journal: 2021 / Decision Support Systems
- Logic: 针对制药组装线质量控制仅能二元分类且误拒率高的问题，设计了三层机器学习质量控制系统（异常检测+集成分类+投票），在真实工业数据上实现零漏检并控制误拒率，同时执行时间满足软实时要求。
- Objective family: analytic_quality
- Context: logistics_transport_supply_chain_and_manufacturing
- Tags: 制药组装质量检测, 零缺陷容忍, 集成机器学习分类, Grad-CAM可解释性

### Assessing the Unacquainted: Inferred Reviewer Personality and Review Helpfulness [theory subset]

- Year/journal: 2021 / MIS Quarterly
- Logic: 针对评论平台无法在评论者刚出现时判断其未来评论价值的问题，文章设计 CNN 文本人格推断模型从早期评论文本提取 Big Five 人格，再用这些特质训练集成分类模型预测未来评论是否有帮助；结果显示人格模型显著优于只用历史评论数和本地状态的基准模型（recall 平均提升 28.20%，precision 平均提升 6.89%）。
- Objective family: analytic_quality
- Context: commerce_marketing_and_customer_service
- Tags: 评论有帮助性预测, 文本人格推断, Big Five人格, Yelp餐馆点评

### Autoencoders for strategic decision support

- Year/journal: 2021 / Decision Support Systems
- Logic: 针对战略决策缺少数据驱动‘正常性’反馈的问题，文章用欠完备自编码器的逐维重建误差构造异常排名和维度级偏差反馈，并以专家集成、真实数据质量扰动和合成异常实验证明其检测准确率和维度反馈能力优于LOF与Isolation Forest，且与人类专家具有协同性。
- Objective family: analytic_quality
- Context: enterprise_work_and_knowledge
- Tags: 自编码器重建误差, 维度级偏差反馈, 专家一致性, 无监督战略决策支持

### DNCP: An attention-based deep learning approach enhanced with attractiveness and timeliness of News for online news click prediction

- Year/journal: 2021 / Information & Management
- Logic: 针对在线新闻点击预测忽略吸引力和时效性的问题，本文设计DNCP模型，用BTM和搜索热词向量分别度量吸引力与时效性并通过CAM融入BiGRU文本表示，用FM建模元特征交互，以Precision/Recall/F1/Accuracy在搜狐和今日头条数据集上评价，结果显示DNCP显著优于基线和消融模型。
- Objective family: analytic_quality
- Context: digital_platform_social_media_and_crowdfunding
- Tags: 新闻点击量预测, 阅读-评论行为主题模型, 搜索热词时效性, 拼接注意力机制

### Design Principles for Robust Fraud Detection:  The Case of Stock Market Manipulations [theory subset]

- Year/journal: 2021 / Journal of the Association for Information Systems
- Logic: 为解决欺诈者改写文本规避检测的问题，本文基于营销和金融经济学理论设计语言学特征，并将其与词袋模型和集成学习结合构建股票推荐欺诈检测分类器，通过模拟文档操纵攻击证明E0.5在攻击下保持最优或接近最优的准确率，说明理论引导特征与集成学习可显著提升鲁棒性。
- Objective family: analytic_quality
- Context: cybersecurity_fraud_and_compliance
- Tags: pump-and-dump检测, 文本分类器鲁棒性, 理论引导语言学特征, 集成学习

### Detecting Noncompliant Behavior in Organizations: How Online Survey Responses and Behaviors Reveal Risk [theory subset]

- Year/journal: 2021 / Journal of Management Information Systems
- Logic: 为解决组织难以准确识别员工不合规风险的问题，文章设计了一个带鼠标轨迹追踪的在线问卷，基于认知失调理论测量员工对合规界定和后果问题的回答宽松度与鼠标偏移；结果显示不合规者回答更宽松且合规问题上的鼠标偏移更大，二者结合的分类模型达到72.79%准确率和0.718 AUC，说明该方法可作为低成本、可扩展的合规风险筛查工具。
- Objective family: analytic_quality
- Context: cybersecurity_fraud_and_compliance
- Tags: 鼠标轨迹追踪, 认知失调, 合规风险筛查, 在线问卷回答宽松度

### Dynamic, Multidimensional, and Skillset-Specific Reputation Systems for Online Work

- Year/journal: 2021 / Information Systems Research
- Logic: 针对在线劳动市场声誉系统的膨胀、归因和静态性缺陷，文章设计了一个将技能嵌入和隐马尔可夫模型结合的 HMM-W2V 框架，以生成动态技能特定声誉分数，并通过 58,459 个任务的评估证明其在排名相关性、分布形态和非完美工人识别上均显著优于多种替代系统。
- Objective family: analytic_quality
- Context: digital_platform_social_media_and_crowdfunding
- Tags: 声誉膨胀, 技能集特定声誉, 隐马尔可夫模型, 自由职业市场

### Fall Detection with Wearable Sensors: A Hierarchical Attention-based Convolutional Neural Network Approach

- Year/journal: 2021 / Journal of Management Information Systems
- Logic: 为解决可穿戴跌倒检测依赖人工特征且深度学习缺乏可解释性的问题，文章设计了在 CNN 上叠加轴级和传感器级层级注意力机制的 HACNN 模型，以 F1、精确率和召回率为指标在 MobiFall 和 UMAFall 两个公开数据集上与多种基线比较，结果显示 HACNN 的 F1 分别达到 0.9808 和 0.9739，显著优于基线，并能通过注意力权重解释哪些传感器轴和位置最有助于跌倒判断。
- Objective family: analytic_quality
- Context: healthcare_and_care
- Tags: 可解释跌倒检测, 层级注意力机制, 可穿戴传感器, 慢性病管理

### From conflicts and confusion to doubts: Examining review inconsistency for fake review detection [theory subset]

- Year/journal: 2021 / Decision Support Systems
- Logic: 针对评论不一致性未被虚假评论检测充分利用的问题，本文设计了22个基于评分-情感、内容和语言的不一致性特征并加入分类模型，在Yelp真实标签数据上验证了这些特征能显著提升虚假评论检测的准确率、精确率、召回率和F值。
- Objective family: analytic_quality
- Context: commerce_marketing_and_customer_service
- Tags: 评论不一致性, 虚假评论检测, 评分-情感不一致, Yelp评论数据

### Predicting employee absenteeism for cost effective interventions

- Year/journal: 2021 / Decision Support Systems
- Logic: 为解决HR福利服务商需要经济高效地识别高风险缺勤员工的问题，文章构建了基于员工缺勤误分类成本矩阵的成本敏感分类决策支持系统，并以CIS和ROI为评价指标，发现成本敏感模型在所有情景下均能带来正成本改善且优于按BACC选择的模型。
- Objective family: economic_and_welfare
- Context: enterprise_work_and_knowledge
- Tags: 员工缺勤预测, 成本敏感学习, 健康干预成本效益, HR分析

### Providing more regular road signs infrastructure updates for connected driving: A crowdsourced approach with clustering and confidence level

- Year/journal: 2021 / Decision Support Systems
- Logic: 为解决车载地图中路标更新滞后且摄像头观测存在GPS与识别噪声的问题，本文在云端设计了一种基于众包路标观测、meanshift聚类和贝叶斯置信度的整合方法；通过真实道路数据对比整合前后及融合系统，结果显示整合后precision从90.8%提升至94.7%、recall从71.1%提升至100%，融合系统将假阳性率降低94.4%。
- Objective family: analytic_quality
- Context: logistics_transport_supply_chain_and_manufacturing
- Tags: 众包路标观测, 路标存在置信度, 地理空间聚类, 联网驾驶地图更新

### S2SAN: A sentence-to-sentence attention network for sentiment analysis of online reviews

- Year/journal: 2021 / Decision Support Systems
- Logic: 针对在线评论中句子重要性被忽略以及序列式句子编码造成不必要复杂度的问题，文章设计以多头自注意力为核心的句子到句子注意力网络S2SAN，在域内、跨域和多域评论数据集上用准确率和训练时间评价，结果显示平均准确率比HAN提高1.2%、训练时间减少约25%，并能提升CNN/RNN/LSTM等基础分类器的准确率。
- Objective family: analytic_quality
- Context: commerce_marketing_and_customer_service
- Tags: 在线评论情感分析, 句子到句子注意力, 层次化文本分类, 跨域/多域情感分类

### Telecom traffic pumping analytics via explainable data science

- Year/journal: 2021 / Decision Support Systems
- Logic: 针对无标签且需可解释性的电信流量泵欺诈，文章构建了“CDR特征工程—无监督聚类—决策树规则提取—专家验证”的DSS，用聚类质量指标和留出准确率选择模型，最终以法院对7462起案件全部判定欺诈和约500万美元损失减少证明其有效性。
- Objective family: risk_security_and_safety
- Context: cybersecurity_fraud_and_compliance
- Tags: 流量泵欺诈, 可解释聚类规则, 电信CDR特征工程, 法律诉讼验证

### The Phishing Funnel Model: A Design Artifact to Predict User Susceptibility to Phishing Websites [theory subset]

- Year/journal: 2021 / Information Systems Research
- Logic: 针对用户易受钓鱼网站攻击的问题，文章设计了集成用户、威胁和工具因素的PFM预测模型，并通过两个纵向实地实验验证其预测准确性（AUC）和干预有效性（减少交互率），结果表明PFM显著优于现有模型和方法。
- Objective family: analytic_quality
- Context: cybersecurity_fraud_and_compliance
- Tags: 钓鱼易感性预测, 漏斗阶段建模, 个性化警告干预, 纵向实地实验

### A collaborative decision support system for multi-criteria automatic clustering

- Year/journal: 2022 / Decision Support Systems
- Logic: 面对自动聚类中簇数和多个聚类有效性标准难以同时确定的问题，文章设计了一个六步协同DSS，让决策者选择VIs、算法和质量阈值，以GA/PSO/HS离线共享最优VI值构造归一化乘性聚合函数，并通过DEA+BWM选出唯一最优聚类划分；在合成数据和PGA巡回赛数据上，该框架相比单独进化算法和DBSCAN等经典算法在CS/DB/SH等有效性指标及非支配解数量上表现更好。
- Objective family: analytic_quality
- Context: general_or_cross_domain
- Tags: 自动聚类, 协同进化算法, 聚类有效性指标, DEA-BWM排序

### A deep recurrent neural network approach to learn sequence similarities for user-identification

- Year/journal: 2022 / Decision Support Systems
- Logic: 本文针对序列行为数据相似性度量困难的问题，设计了一个结合LSTM和三元组损失的神经网络TL-RNN以学习序列嵌入；在Comscore网页浏览数据上通过用户再识别准确率等指标与Smith-Waterman和TF-RW比较，显示该方法在短序列上显著提升了识别准确率并能高效完成多用户分配和用户数估计。
- Objective family: analytic_quality
- Context: commerce_marketing_and_customer_service
- Tags: 序列相似性学习, 用户再识别, 点击流分析, 三元组损失

### An explanatory machine learning framework for studying pandemics: The case of COVID-19 emergency department readmissions

- Year/journal: 2022 / Decision Support Systems
- Logic: 为解决大流行初期缺乏已知风险因素而难以及时识别高风险患者的问题，本文构建了遗传算法+深度神经网络+SHAP的探索-预测-解释框架，用真实电子病历数据预测COVID-19患者的7天急诊再入院并解释风险因素，最终获得AUC=0.883，并发现与临床研究一致的关键危险因素。
- Objective family: analytic_quality
- Context: healthcare_and_care
- Tags: COVID-19再入院预测, SHAP模型解释, 遗传算法特征选择, 急诊科临床决策支持

### Assessing and Enhancing Adversarial Robustness of Predictive Analytics: An Empirically Tested Design Framework

- Year/journal: 2022 / Journal of Management Information Systems
- Logic: 针对预测分析模型易被黑盒对抗样本欺骗的问题，作者构建了融合鲁棒性评估、集成学习与迭代对抗重训练的ARText系统，并在垃圾评论/垃圾邮件检测基准上证明其对抗鲁棒性显著优于各基线模型。
- Objective family: analytic_quality
- Context: cybersecurity_fraud_and_compliance
- Tags: 对抗鲁棒性评估, 文本对抗样本, 垃圾评论/垃圾邮件检测, 集成学习与对抗重训练

### Combining Crowd and Machine Intelligence to Detect False News on Social Media [theory subset]

- Year/journal: 2022 / MIS Quarterly
- Logic: 针对社交媒体假新闻检测中机器智能不足的问题，文章设计CAND框架将新闻特征、用户辟谣回复和举报数量经无监督贝叶斯模型CLNAM聚合，在Weibo和Twitter数据集上取得了优于多种基准的PR AUC和F1。
- Objective family: analytic_quality
- Context: digital_platform_social_media_and_crowdfunding
- Tags: 众包举报信号, 辟谣回复检测, 贝叶斯结果聚合, 假新闻检测

### Cross-Lingual Cybersecurity Analytics in the International Dark Web with Adversarial Deep Representation Learning

- Year/journal: 2022 / MIS Quarterly
- Logic: 针对非英语暗网黑客资产缺乏标注数据且机器翻译误译严重的问题，文章设计CLHAD框架，通过ADREL对抗深度表示学习从英语向俄语、法语、意大利语迁移语言不变表示并进行二分类；在Accuracy、F1和AUC上显著超过单语、MT和CLKT基准，验证了跨语言知识迁移用于暗网网络安全分析的有效性。
- Objective family: analytic_quality
- Context: cybersecurity_fraud_and_compliance
- Tags: 跨语言知识迁移, 暗网黑客资产检测, 对抗深度表示学习, 黑客资产画像

### Data analytics for the sustainable use of resources in hospitals: Predicting the length of stay for patients with chronic diseases

- Year/journal: 2022 / Information & Management
- Logic: 本文针对入院时预测慢性病患者数值型住院时长的准确性与实用性不足问题，通过设计融合患者历史就诊数据工程与深度MLP网络的预测模型，并采用时间切分评估和变量重要性分析，证明患者既往住院史变量显著提升LOS预测精度（COPD±2天86%、肺炎±2天74%）。
- Objective family: analytic_quality
- Context: healthcare_and_care
- Tags: 住院时长预测, COPD与肺炎, 患者既往住院史, 深度多层感知机

### Data misrepresentation detection for insurance underwriting fraud prevention

- Year/journal: 2022 / Decision Support Systems
- Logic: 文章将车险承保保费欺诈风险建模为条件密度估计问题，用已核验合同估计自报信息在车辆信息下的分布并结合定价政策计算风险分数，通过 CDE loss、覆盖率校准和 KL 散度验证估计质量，并在专家标注高风险申请上显示出更高风险分数分布。
- Objective family: analytic_quality
- Context: cybersecurity_fraud_and_compliance
- Tags: 保费欺诈, 条件密度估计, 自报信息核验, 车险核保

### Discovering Emerging Threats in the Hacker Community: A Nonparametric Emerging Topic Detection Framework

- Year/journal: 2022 / MIS Quarterly
- Logic: 针对黑客社区新兴威胁难以预知主题数量且检测效率低的问题，本文设计了一个基于条件 HDP、随机变分推断与 Bayes factor 检验的 NPETD 框架，在暗网市场测试集上用精确率/召回率/F值/主题连贯性/CPU时间验证其相比基线方法更有效且更高效，并在真实黑客论坛中识别出有意义的新兴欺诈话题。
- Objective family: analytic_quality
- Context: cybersecurity_fraud_and_compliance
- Tags: 暗网黑客社区, 新兴威胁检测, 非参数主题模型, 网络威胁情报

### Explainability and fairness of RegTech for regulatory enforcement: Automated monitoring of consumer complaints [theory subset]

- Year/journal: 2022 / Decision Support Systems
- Logic: 针对监管机构需要从大量投诉中筛选高价值案件且模型须可解释、公平的问题，文章设计了结合信息诊断性特征、词袋模型和集成的投诉结果预测分类器，用准确率/F1和分群公平性验证，发现集成分类器准确率达85.92%且显著优于理论特征模型，同时老年群体准确率下降并可用专门分类器改善公平性。
- Objective family: analytic_quality
- Context: cybersecurity_fraud_and_compliance
- Tags: 金融消费者投诉, 监管科技, 可解释AI, 公平分类

### Fraudulent review detection model focusing on emotional expressions and explicit aspects: investigating the potential of feature engineering

- Year/journal: 2022 / Decision Support Systems
- Logic: 针对虚假评论检测在特征偏斜和类别不平衡下精度下降的问题，本文构建了12特征+M-SMOTE过采样+多数投票的检测模型，在Yelp等数据上以精确率、召回率、F1和AUC证明了其相对基线、SMOTE及已有研究均有显著提升。
- Objective family: analytic_quality
- Context: commerce_marketing_and_customer_service
- Tags: 虚假评论检测, 评论者行为特征, 情感表达与词性特征, M-SMOTE过采样

### Incorporating FAT and privacy aware AI modeling approaches into business decision making frameworks

- Year/journal: 2022 / Decision Support Systems
- Logic: 为解决商业 AI 的公平-问责-透明兼顾问题，文章在隐私受限的 Netflix 评分数据上设计并实例化了一个以 GLM 为核心、带四个可解释预测器和相似度/分区机制的 FAT 建模框架，用 RMSE、覆盖率、模型精简度和跨分区稳定性评价，结果发现可解释模型在大部分分区上比 Cinematch 基准精度提升 8%–14%，且 FAT 三原则可平衡共存。
- Objective family: multi_objective_or_tradeoff
- Context: general_or_cross_domain
- Tags: 可解释AI, 公平问责透明, 隐私受限数据, 亲和度评分预测

### Social influence-based contrast language analysis framework for clinical decision support systems [theory subset]

- Year/journal: 2022 / Decision Support Systems
- Logic: 针对CDSS缺乏早期抑郁检测和可解释对比洞察的问题，文章设计了融合词级、主题级和网络级对比语言特征的社交影响分析框架，并在Facebook真实数据上用CART等分类器以Accuracy/Precision/Recall/F-Score评测，结果表明该框架显著优于LIWC/SBERT/GTF/RFE等基线，并提供了可解释的抑郁/非抑郁语言差异。
- Objective family: analytic_quality
- Context: healthcare_and_care
- Tags: 对比语言分析, 抑郁早期检测, 社交网络影响, CDSS功能增强

### A deep learning approach for detecting fake reviewers: Exploiting reviewing behavior and textual information

- Year/journal: 2023 / Decision Support Systems
- Logic: 针对虚假评论者检测中人工特征工程成本高和文本表示不充分的问题，本文构建了“Conv1d行为特征提取 + Longformer/CNN/BiLSTM/注意力文本特征提取 + 二分类”的端到端框架，并在YelpZIP/YelpNYC上以Accuracy、F1、AUC等指标与多组基线和消融对比，证明其检测性能优于现有方法。
- Objective family: analytic_quality
- Context: digital_platform_social_media_and_crowdfunding
- Tags: 虚假评论者检测, 行为特征自动学习, 上下文感知注意力, Longformer文本表示

### Augmenting Social Bot Detection with Crowd-Generated Labels [theory subset]

- Year/journal: 2023 / Information Systems Research
- Logic: 本文针对社交机器人检测未利用用户反应这一问题，设计了一个将用户回复的话题、情感和言语行为特征与账户语义和时间特征结合的分类系统，并通过与传统模型的对比实验证明，人群反应能够显著提升机器人检测的准确率，言语行为还可以进一步改善性能。
- Objective family: analytic_quality
- Context: cybersecurity_fraud_and_compliance
- Tags: 众包标签增强检测, 言语行为理论, BERT深度分类, Reddit机器人检测

### CATCHM: A novel network-based credit card fraud detection method using node representation learning

- Year/journal: 2023 / Decision Support Systems
- Logic: CATCHM通过三部分网络设计（含人工欺诈节点）、归纳池化扩展和XGBoost堆叠，从交易网络中自动学习交易嵌入来检测信用卡欺诈；在324万笔真实交易上，CATCHM以AUCPR=0.57、F1=0.63、TP@300=213和约10ms/笔的处理时间优于全部基准，验证了无需手工特征工程的网络表示学习在欺诈检测中的有效性。
- Objective family: analytic_quality
- Context: cybersecurity_fraud_and_compliance
- Tags: 信用卡欺诈检测, 网络表示学习, 人工欺诈节点, 归纳池化

### Let Artificial Intelligence Be Your Shelf Watchdog: The Impact of Intelligent Image Processing-Powered Shelf Monitoring on Product Sales

- Year/journal: 2023 / MIS Quarterly
- Logic: 针对新兴市场大量独立零售店合同异质性高、人工货架监测难以扩展的问题，文章评估基于智能图像处理的AI辅助货架监测App；准实验和随机实地实验表明，AI图像识别与合规报告提高了零售商的货架陈列合规率和产品销售额，且终止后仍有部分持续效应，而仅拍照无AI则无效。
- Objective family: economic_and_welfare
- Context: commerce_marketing_and_customer_service
- Tags: AI辅助货架监测, 零售货架陈列合规, 快消品制造企业, 独立零售店合同异质性

### Responsible cognitive digital clones as decision-makers: a design science research study

- Year/journal: 2023 / European Journal of Information Systems
- Logic: 为缓解组织决策中“人员过载vs.韧性不足”的问题，作者用设计科学研究构建Pi-Mind认知数字克隆智能体，通过T|C-SGAN对抗训练复现捐赠者的决策偏好，并在乌克兰高校和军事物流场景中以F1等分类指标评估，结果显示克隆决策一致性从0.49提升到0.96，同时每年可节省逾1500人时。
- Objective family: analytic_quality
- Context: general_or_cross_domain
- Tags: 认知数字克隆, T|C-SGAN对抗训练, 个人价值系统, 乌克兰高校决策流程

### Sensing the Future: A Design Framework for Context-Aware Predictive Systems

- Year/journal: 2023 / Journal of the Association for Information Systems
- Logic: 针对工业传感器情境数据缺乏预测系统设计指导的问题，本文提出CAPS四步设计框架并用它在MAN Diesel & Turbo构建备件需求预测工件，以预测误差成本COST_FE为评价指标，发现基于活动传感器的情境预测将预测误差成本较Croston基线降低20%，验证了框架的可用性并提炼出设计命题。
- Objective family: operational_efficiency
- Context: logistics_transport_supply_chain_and_manufacturing
- Tags: 备件需求预测, 传感器情境数据, 发动机活动时间, 预测误差成本

### Unlocking the Power of Voice for Financial Risk Prediction: A Theory-Driven Deep Learning Design Approach [theory subset]

- Year/journal: 2023 / MIS Quarterly
- Logic: 为了利用财报电话会议中管理者“怎么说”的语音线索来改进财务风险预测，文章基于Mehrabian沟通模型设计了两阶段LSTM集成模型和基础声学特征，在6047个电话会议样本上以out-of-sample R²为指标验证，发现相对市场基准在3至60天预测上提升2.26%至8.34%，并能转化为期权交易的经济收益。
- Objective family: analytic_quality
- Context: finance_accounting_and_investment
- Tags: 财报电话会议语音分析, 财务风险预测, 两阶段LSTM多模态融合, 基础声学特征

### Will they take this offer? A machine learning price elasticity model for predicting upselling acceptance of premium airline seating

- Year/journal: 2023 / Information & Management
- Logic: 针对航空公司升舱报价精准投放和定价问题，PREM用去噪自编码器、代价敏感分类、二元自编码器分群和ILP优化组成的多阶段流水线预测升舱接受概率和价格弹性，相比规则方法获得更高F1和收入捕获，并在模拟中减少无关邮件、增加升舱接受和收入。
- Objective family: economic_and_welfare
- Context: commerce_marketing_and_customer_service
- Tags: 升舱追加销售, 价格弹性预测, 航空邮件营销, 客户分群

### Attending to Customer Attention: A Novel Deep Learning Method for Leveraging Multimodal Online Reviews to Enhance Sales Prediction [theory subset]

- Year/journal: 2024 / Information Systems Research
- Logic: 针对多模态评论销售预测中评论未加区分的问题，本文设计了融入顾客注意力（及时性、语义多样性、投票意识、自适应文本-图片交互）的深度模型DTV-AMI，并在2685家酒店的大规模评论数据上以RMSE/MAE进行基准比较，结果显示DTV-AMI显著提升了酒店月度入住率预测准确率。
- Objective family: analytic_quality
- Context: commerce_marketing_and_customer_service
- Tags: 多模态在线评论, 顾客注意力, 酒店入住率预测, 深度注意力机制

### Automated Analysis of Changes in Privacy Policies: a Structured Self-Attentive Sentence Embedding Approach

- Year/journal: 2024 / MIS Quarterly
- Logic: 为解决隐私政策长段落多标签标注不准确的问题，本文设计了引入行级注意力和共享参数多标签分类器的SAAS，在OPP-115上以0.758的微平均F1显著超越十多种基线，并用案例分析方法揭示Amazon修订政策可能违反GDPR的透明性原则。
- Objective family: analytic_quality
- Context: cybersecurity_fraud_and_compliance
- Tags: 隐私政策演化分析, 数据实践多标签分类, GDPR合规影响, 行级注意力机制

### Creating Proactive Cyber Threat Intelligence with Hacker Exploit Labels: A Deep Transfer Learning Approach

- Year/journal: 2024 / MIS Quarterly
- Logic: 针对黑客论坛漏洞利用代码缺乏标签且人工标注困难的问题，文章设计了用漏洞标题预初始化BiLSTM并融合自注意力与多层深度迁移学习的DTL-EL分类器，通过源域和黑客论坛目标域的八类漏洞标注实验，用Accuracy、Precision、Recall和F1评价，结果表明DTL-EL在目标域F1达到70.34%，显著优于非迁移和替代迁移学习基线。
- Objective family: analytic_quality
- Context: cybersecurity_fraud_and_compliance
- Tags: 黑客论坛漏洞利用标注, 深度迁移学习, 网络威胁情报, 预初始化BiLSTM

### Explainable Deep Learning for False Information Identification: An Argumentation Theory Approach [theory subset]

- Year/journal: 2024 / Information Systems Research
- Logic: 针对深度FII模型语义句法混杂和解释不可靠的问题，文章用Toulmin论证模型与结构平衡理论将声明-证据对转成带符号词网络并提取平衡度特征，拼接进既有分类模型，在提升F1/AUC的同时用SBTX解释提高人类审核准确率、信任和决策信心。
- Objective family: analytic_quality
- Context: digital_platform_social_media_and_crowdfunding
- Tags: 虚假信息识别, 结构平衡理论, Toulmin论证模型, 可解释AI

### Knowledge-Aware Learning Framework Based on Schema Theory to Complement Large Learning Models [theory subset]

- Year/journal: 2024 / Journal of Management Information Systems
- Logic: 针对知识感知模型缺乏上下文相关且具选择性的知识激活问题，文章基于图式理论设计了由ConceptNet知识库、结构化知识图式、TF-IDF式上下文知识激活和bi-LSTM+GCN融合预测组成的学习框架，在文本分类与NLI任务上以约7.6%的参数量、10%的训练数据和不到一半的训练时间达到与LLM可比的F1，表明认知理论指导的知识感知框架能同时改善学习有效性和学习效率。
- Objective family: multi_objective_or_tradeoff
- Context: general_or_cross_domain
- Tags: 图式理论, ConceptNet知识图谱, 知识激活机制, 低资源文本分类

### Motion Sensor–Based Fall Prevention for Senior Care: A Hidden Markov Model with Generative Adversarial Network Approach

- Year/journal: 2024 / Information Systems Research
- Logic: 针对现有运动传感器跌倒预防模型难以捕捉时序分布和触发提前量的问题，文章设计了HMM-GAN与逻辑回归两阶段框架，用熵GAN替代GMM并新设EM算法训练，在两个大规模公开数据集上以Accuracy/F1/AUC证实其状态识别和跌倒预防触发性能超过现有基准，案例分析估计可带来超过3300万美元收益。
- Objective family: analytic_quality
- Context: healthcare_and_care
- Tags: 跌倒预防, 可穿戴运动传感器, 隐马尔可夫生成对抗网络, 保护装置触发

### The Effect of AI-Enabled Credit Scoring on Financial Inclusion: Evidence from an Underserved Population of over One Million

- Year/journal: 2024 / MIS Quarterly
- Logic: 为解决传统信用评分模型对缺乏信用历史人群的金融排斥，文章研究了一家银行在个人贷款中部署的AI信用评分模型，通过双重差分对比发现该模型利用弱信号和先进算法提高预测精度，从而同时提高了服务不足人群的贷款审批率并降低了违约率，实现了金融包容性与贷款表现的双赢。
- Objective family: substantive_domain_outcome
- Context: finance_accounting_and_investment
- Tags: AI信用评分, 弱信号, 金融包容性, 双重差分

### 1 + 1 > 2? Information, Humans, and Machines [theory subset]

- Year/journal: 2025 / Information Systems Research
- Logic: 针对小贷审批中人机协作能否增值的问题，论文训练XGBoost违约预测模型并设计大信息量与SHAP机器解释的田野实验，以违约率为核心指标发现只有两个条件同时具备时，人类评估者的主动反思才能将违约率从机器单独决策的5.15%降至3.13%，实现1+1>2。
- Objective family: analytic_quality
- Context: finance_accounting_and_investment
- Tags: 人机协作决策, 小微贷款审批, 机器学习解释, 违约率

### An explainable lesion detection transformer model for medical imaging diagnosis decision support: Design science research

- Year/journal: 2025 / Decision Support Systems
- Logic: 针对医学影像病灶检测的精度、可解释性和数据不平衡问题，本文设计EL-DETR模型，通过可解释分离注意力、混合匹配查询和复合损失实现病灶定位与分类，并在四个真实医学影像数据集上用MAP/MAR和注意力可视化证明其检测准确性和可解释性优于多种基线模型。
- Objective family: analytic_quality
- Context: healthcare_and_care
- Tags: 病灶检测, 可解释注意力可视化, 医学影像决策支持, Transformer目标检测

### Automating in High-Expertise, Low-Label Environments: Evidence-Based Medicine by Expert-Augmented Few-Shot Learning [theory subset]

- Year/journal: 2025 / MIS Quarterly
- Logic: 针对高专业、低标注的系统评价数据提取问题，文章设计FastSR少样本深度学习框架，通过多级表示、注意力语义匹配和联合学习提升PICO句子分类与片段抽取的准确性，并在WD/COVID/EBM-NLP三个数据集上证明其优于多种基线和LLM，同时将真实SR项目时间缩短约65%。
- Objective family: analytic_quality
- Context: healthcare_and_care
- Tags: PICO要素抽取, 少样本学习, 系统评价自动化, 循证医学

### Beyond Complements and Substitutes: A Graph Neural Network Approach for Collaborative Retail Sales Forecasting [theory subset]

- Year/journal: 2025 / Information Systems Research
- Logic: 面向零售销售预测中产品关系识别不准、利用不全的问题，基于跨类别选择依赖理论设计图神经网络 CL4RSF/MS2RSF，使其能同时学习并利用正/负、间接/非对称/异步/动态产品关系，在两个真实零售数据集上以 MAE/RMSE 衡量，该模型一致优于多个深度学习和统计基准。
- Objective family: analytic_quality
- Context: commerce_marketing_and_customer_service
- Tags: 协作式销售预测, 产品关系图学习, 异步关系建模, 正负关系建模

### Mitigating Bias in Hate Speech Detection With a Small Number of Expert Annotations: A Prompt-Based Learning Approach

- Year/journal: 2025 / MIS Quarterly
- Logic: 针对通用标注造成仇恨言论检测对AAE等群体系统性误报而专家标注稀缺的问题，本文设计了“配对生成器+SimCSE对比学习”与“注入仇恨目标知识的增强连续提示+软言语器”的两阶段检测框架，仅用256条专家标注即在WH16/VTWK21上以更低FPR、更高F1/ACC和更小统计奇偶差全面超过所有基线。
- Objective family: analytic_quality
- Context: digital_platform_social_media_and_crowdfunding
- Tags: 仇恨言论检测, 提示学习, 对比学习去偏, 专家标注

### Predicting Instructor Performance in Online Education: An Interpretable Hierarchical Transformer with Contextual Attention

- Year/journal: 2025 / Information Systems Research
- Logic: 为了自动且可解释地预测在线课程教师表现，本文设计了带上下文注意力的层级Transformer模型，以讲座字幕文本为输入预测教师/课程评分，实验表明其预测误差显著低于传统机器学习模型和LectureBERT，并可通过注意力权重和反事实分析提供可操作建议。
- Objective family: analytic_quality
- Context: education_training_and_learning
- Tags: 教师绩效预测, 课程评分预测, 层级Transformer, 可解释深度学习

### AI-Augmented Content Validation in Behavioral Research: Development and Evaluation of the RATER System [theory subset]

- Year/journal: 2026 / MIS Quarterly
- Logic: 针对传统内容效度评估昂贵、耗时、难复制的问题，本文构建了基于微调大语言模型的RATER系统（RATER_C分类器与RATER_D合成评分者），用来自2,443篇文章的28.7万余条目-定义对训练和测试，以AUC、F1、ECE以及与人类H&T评分的一致性为指标，证明RATER能以接近或超过人工程序的效果辅助量表内容效度评估。
- Objective family: analytic_quality
- Context: general_or_cross_domain
- Tags: 量表内容效度评估, 大语言模型微调, Hinkin-Tracey评分模拟, 条目-构念对应性分类

## human_facing_information_and_interaction (72)

### Choose your own training adventure: designing a gamified SETA artefact for improving information security and privacy through interactive storytelling [theory subset]

- Year/journal: 2020 / European Journal of Information Systems
- Logic: 针对员工社交网站披露风险，文章设计了文本版和视觉版CYOA游戏化SETA培训，通过纵向随机对照试验与无干预和传统警告邮件比较，发现文本版更利于减少OSD和改变意向/态度，而视觉版更利于提升记忆性和用户体验。
- Objective family: behavioral_response
- Context: cybersecurity_fraud_and_compliance
- Tags: 游戏化SETA, 交互式叙事, 在线自我披露, 文本与视觉培训比较

### Containing COVID-19 through physical distancing: the impact of real-time crowding information [theory subset]

- Year/journal: 2020 / European Journal of Information Systems
- Logic: 本文针对COVID-19期间DSS显示拥挤信息能否促进用户选择人更少场所的问题，通过在线实验操纵医疗诊所选择网站中拥挤信息的有无与即时性，发现显示拥挤信息、尤其是实时信息，显著提高用户选择低拥挤诊所的可能性，且低健康焦虑用户的反应更强。
- Objective family: behavioral_response
- Context: healthcare_and_care
- Tags: 实时拥挤信息, 医疗诊所选择, 健康焦虑, COVID-19身体距离

### Designing information feedback for bidders in multi-item multi-unit combinatorial auctions

- Year/journal: 2020 / Decision Support Systems
- Logic: 针对MUCA中投标人缺乏出价指导的问题，文章设计了计算包MDL/MWL的DSS算法，并以模拟和真实频谱拍卖数据验证其每笔出价运行时间足以支持实时在线拍卖。
- Objective family: technical_system_performance
- Context: general_or_cross_domain
- Tags: 组合拍卖, 实时出价反馈, 多单位拍卖, 死亡水平计算

### Digital Nudging: Numeric and Semantic Priming in E-Commerce [theory subset]

- Year/journal: 2020 / Journal of Management Information Systems
- Logic: 文章通过七项实验在电商页面广告中实施并发数字/语义启动，证明当消费者在无价格参考的在线拍卖中自行出价时，广告中的数字和相关产品质量会显著改变支付意愿，而当存在MSRP或固定价格时这种助推效应消失。
- Objective family: behavioral_response
- Context: commerce_marketing_and_customer_service
- Tags: 数字助推, 数值启动, 语义启动, 在线拍卖支付意愿

### Effectiveness of Location-Based Advertising and the Impact of Interface Design [theory subset]

- Year/journal: 2020 / Journal of Management Information Systems
- Logic: 本研究通过2x2随机现场实验操纵基于位置的优惠券应用的界面设计（距离信息与排序机制），以优惠券点击率为客观指标衡量有效性，发现按距离排序是最有效的界面设计，且距离和排名效应随界面设计和用户地理位置而变化。
- Objective family: behavioral_response
- Context: commerce_marketing_and_customer_service
- Tags: 位置优惠券, 界面设计, 距离信息, 距离排序

### Facilitating Complex Product Choices on E-commerce Sites: An Unconscious Thought and Circadian Preference Perspective [theory subset]

- Year/journal: 2020 / Decision Support Systems
- Logic: 针对电商复杂产品选择困难，作者在仿真拍卖网站中通过弹出n-back分心任务诱发无意识思考，以是否选择最优手机作为决策质量指标，发现无意识思考整体优于有意识思考，且当昼夜偏好与决策时间不同步时优势更明显。
- Objective family: human_task_performance
- Context: commerce_marketing_and_customer_service
- Tags: 无意识思维, 昼夜偏好, 复杂产品选择, n-back分心任务

### Gamifying knowledge sharing in humanitarian organisations: a design science journey [theory subset]

- Year/journal: 2020 / European Journal of Information Systems
- Logic: 为激励MSF员工在KMS上主动分享知识，文章设计了游戏化个人资料和虚拟水族箱以提供活动反馈，通过现场与实验室实验证明这些反馈显著增加了访问、新增资源和评论等贡献行为。
- Objective family: behavioral_response
- Context: public_sector_crisis_and_humanitarian
- Tags: 游戏化反馈, 虚拟水族箱, 人道主义知识分享, 利他主义与贡献

### Ingredients for successful badges: evidence from a field experiment in bike commuting [theory subset]

- Year/journal: 2020 / European Journal of Information Systems
- Logic: 针对徽章设计知识缺口，文章在自行车通勤计划中随机改变徽章的奖励、标志和完成逻辑，以每周骑行天数为结果，发现分享选项提升骑行、环保框架无效、相对目标只对高频骑行者有效而对低频骑行者有反效果。
- Objective family: behavioral_response
- Context: healthcare_and_care
- Tags: 徽章组件设计, 社交分享奖励, 固定目标与相对目标, 自行车通勤骑行

### Is optimal recommendation the best? A laboratory investigation under the newsvendor problem [theory subset]

- Year/journal: 2020 / Decision Support Systems
- Logic: 针对最优DSS建议能否消除报童订货PtC偏差的问题，作者设计并比较提供最优、保守、激进建议及双方绩效反馈的DSS实验室实验，以PtC效应值和利润为主要指标，发现最优建议只能部分纠正偏差，而激进建议在高利润条件下通过后悔厌恶与锚定效应消除了偏差。
- Objective family: human_task_performance
- Context: logistics_transport_supply_chain_and_manufacturing
- Tags: Pull-to-Center偏差, 算法厌恶, 后悔厌恶, DSS建议设计

### Mobile health: A carrot and stick intervention to improve medication adherence [theory subset]

- Year/journal: 2020 / Decision Support Systems
- Logic: 针对慢病患者的故意/非故意不依从，文章设计了结合提醒、正强化、负强化（封锁最常用APP）、目标设定和社交连接的移动健康干预，并用解析模型证明其能显著提高达到期望MAR的概率并带来医疗节约。
- Objective family: behavioral_response
- Context: healthcare_and_care
- Tags: 药物依从性, 正强化与负强化, APP封锁式负强化, 解析建模验证

### Novice digital service designers' decision-making with decision aids — A comparison of taxonomy and tags

- Year/journal: 2020 / Decision Support Systems
- Logic: 针对设计新手难以从大量设计技术中选择合适技术的问题，本文在LimeSurvey中构造分类法、标签和无辅助三种决策辅助界面，以190名受试者的选择准确率和认知努力为客观指标进行实验比较，发现分类法辅助通过降低认知努力带来更高的设计技术选择准确率。
- Objective family: human_task_performance
- Context: enterprise_work_and_knowledge
- Tags: 设计技术选择, 分类法与标签辅助比较, 认知努力中介, 决策风格调节

### Social influence tactics in e-commerce onboarding: The role of social proof and reciprocity in affecting user registrations [theory subset]

- Year/journal: 2020 / Decision Support Systems
- Logic: 针对电商用户引导中社会影响策略组合效果不明的问题，本文在注册弹层中设计货币型/效用型互惠与社会认同线索，通过N=249在线实验和N=475,495现场随机实验测量注册/确认注册率，发现两类线索单独使用均有效，但组合使用时社会认同使货币型互惠失效、却放大效用型互惠的效果。
- Objective family: behavioral_response
- Context: commerce_marketing_and_customer_service
- Tags: 用户注册转化, 社会认同线索, 互惠设计, 电商引导流程

### The Relative Effect of the Convergence of Product Recommendations from Various Online Sources [theory subset]

- Year/journal: 2020 / Journal of Management Information Systems
- Logic: 针对电商网站多推荐来源汇聚如何影响消费者接受推荐的问题，文章构造了同时呈现RA、专家和消费者三类来源的实验网站并操控来源间的共同推荐产品，以推荐接受率为结果，发现RA与专家来源的汇聚因同时降低三类产品不确定性而优于其他两来源组合。
- Objective family: behavioral_response
- Context: commerce_marketing_and_customer_service
- Tags: 推荐来源汇聚, 产品不确定性三维度, 推荐接受率, 专家与推荐代理互补

### The effect of interactive analytical dashboard features on situation awareness and task performance [theory subset]

- Year/journal: 2020 / Decision Support Systems
- Logic: 本文在APS生产计划仪表盘中加入what-if分析，通过对比有无该功能的仪表盘并使用SAGAT和眼动测量，发现what-if分析提高任务绩效但降低态势感知，揭示了自动化分析功能可能带来的out-of-the-loop权衡。
- Objective family: multi_objective_or_tradeoff
- Context: logistics_transport_supply_chain_and_manufacturing
- Tags: what-if分析, 态势感知, 眼动追踪, 生产计划仪表盘

### Understanding Security Vulnerability Awareness, Firm Incentives, and ICT Development in Pan-Asia [theory subset]

- Year/journal: 2020 / Journal of Management Information Systems
- Logic: 针对企业安全投入不足与信息不对称问题，文章设计并向企业披露基于垃圾邮件和钓鱼网站数据的安全漏洞指数与同行排名，通过随机田野实验的DID分析证明该信息披露显著降低企业CBL垃圾邮件量，且效果受企业激励（是否托管网站）和国家ICT发展水平调节。
- Objective family: risk_security_and_safety
- Context: cybersecurity_fraud_and_compliance
- Tags: 安全漏洞指数, 网络安全信息披露, 垃圾邮件与钓鱼治理, 随机田野实验

### Using Design-Science Based Gamification to Improve Organizational Security Training and Compliance [theory subset]

- Year/journal: 2020 / Journal of Management Information Systems
- Logic: 针对员工防钓鱼失败和现有安全培训不受欢迎的问题，文章基于设计科学方法构建了一个以 HMSAM 为核心理论的游戏化安全培训系统；六个月的现场实验用真实钓鱼邮件作为客观行为指标，显示游戏化组被钓鱼成功率（27.3%）显著低于无培训对照组（44.7%）和传统邮件培训组（39.7%），从而证明游戏化培训能改善员工安全学习与合规行为。
- Objective family: behavioral_response
- Context: cybersecurity_fraud_and_compliance
- Tags: 安全培训游戏化, 钓鱼邮件防御, 员工安全合规, 内在动机与沉浸

### Words Matter! Toward a Prosocial Call-to-Action for Online Referral: Evidence from Two Field Experiments [theory subset]

- Year/journal: 2020 / Information Systems Research
- Logic: 文章在Collage.com在线照片产品平台推荐计划中只改变行动呼吁的措辞框架，通过两个10万客户随机现场实验发现，亲社会框架（强调朋友获益）显著提高发送者发起推荐的概率、推荐总数和朋友购买转化，机制是降低内疚并增强利他动机。
- Objective family: behavioral_response
- Context: commerce_marketing_and_customer_service
- Tags: 亲社会行动呼吁, 推荐奖励计划, 口碑传播, 随机现场实验

### Animation as a dynamic visualization technique for improving process model comprehension [theory subset]

- Year/journal: 2021 / Information & Management
- Logic: 为了解决静态流程模型行为信息难以理解的问题，文章设计了带颜色信号和两级交互的自适应动画环境；通过194名参与者的在线实验，以问题解决测试得分为指标比较动画与静态呈现，发现动画显著提升理解，且该效应受专业知识调节呈U形。
- Objective family: human_task_performance
- Context: enterprise_work_and_knowledge
- Tags: 流程模型动画, 自适应交互, 专业知识调节, BPMN理解

### Designing Effective Mobile Health Apps: Does Combining Behavior Change Techniques Really Create Synergies? [theory subset]

- Year/journal: 2021 / Journal of Management Information Systems
- Logic: 针对移动健康应用中组合行为改变技术可能产生非协同作用的问题，文章将保护动机和社会上行比较理论实例化为四款WORKLAX原型，通过五周现场实验测量训练完成数和应用打开次数，发现两种机制单独有效但组合时产生负向交互，从而质疑了行为改变技术组合必然协同的假设。
- Objective family: behavioral_response
- Context: healthcare_and_care
- Tags: 移动健康应用, 行为改变技术, 社会上行比较, 恐惧诉求

### Estimating the Impact of “Humanizing” Customer Service Chatbots [theory subset]

- Year/journal: 2021 / Information Systems Research
- Logic: 为检验客服聊天机器人拟人化对交易结果的影响，作者在与美国二手服装零售商合作的Facebook Messenger买回流程中随机加入社交临场、沟通延迟和幽默三类拟人特征，并用成交转换率和报价敏感性作为结果指标，发现拟人化显著提高成交率，但三类特征齐备时顾客对报价更为敏感。
- Objective family: behavioral_response
- Context: commerce_marketing_and_customer_service
- Tags: 客服聊天机器人, 拟人化设计, 二手服装回购, 报价敏感度

### How does scarcity promotion lead to impulse purchase in the online market? A field experiment [theory subset]

- Year/journal: 2021 / Information & Management
- Logic: 针对在线稀缺促销如何诱发冲动购买的问题，作者在淘宝搭建真实奶茶券网店，通过2×2田野实验操纵商品限量（20/200份）与限时（10分钟/1小时）信息展示，发现高限量和高限时都能提高消费者感知唤醒，进而显著提高实际冲动下单概率，且限时压力高时限量效应减弱。
- Objective family: behavioral_response
- Context: commerce_marketing_and_customer_service
- Tags: 稀缺促销, 冲动购买, 感知唤醒, 在线田野实验

### LINDA-BN: An interpretable probabilistic approach for demystifying black-box predictive models

- Year/journal: 2021 / Decision Support Systems
- Logic: 为解决黑盒模型逐条预测缺乏可解释性和可靠性信号的问题，LINDA-BN通过在数据点邻域置换采样并学习局部贝叶斯网络及马尔可夫毯，将输出规则与真实分类正误对照，发现Rule 1集中于正确分类、Rule 3/4集中于误分类，从而为决策者提供解释特征依赖、判断预测置信度和识别潜在误分类的模型无关事后解释工具。
- Objective family: analytic_quality
- Context: general_or_cross_domain
- Tags: 贝叶斯网络局部解释, 马尔可夫毯, 模型无关事后解释, 误分类识别

### Peer Effects in Competitive Environments: Field Experiments on Information Provision and Interventions [theory subset]

- Year/journal: 2021 / MIS Quarterly
- Logic: 针对竞争性课堂中大学生拖延和成绩问题，作者在 Canvas LMS 上开发了自动读取日志、计算同伴信息并发送干预消息的插件，通过随机现场实验以 StartTime 和 Grade 为指标发现，同伴信息干预能减少拖延并提高成绩，且对男生、男性占多数环境及过去表现较差的学生效果更强。
- Objective family: behavioral_response
- Context: education_training_and_learning
- Tags: 同伴信息干预, 拖延行为, Canvas学习管理系统, 性别差异

### The Effectiveness of Social Norms in Fighting Fake News on Social Media [theory subset]

- Year/journal: 2021 / Journal of Management Information Systems
- Logic: 针对社交媒体用户举报假新闻意愿低的问题，作者在仿Facebook新闻流界面中加入指令性和描述性社会规范消息，并通过两个在线实验比较不同规范提示下的举报数量，发现指令性规范显著提升举报率、描述性规范单独无效、两者联合效果最强且描述性规范强度呈倒U形。
- Objective family: behavioral_response
- Context: digital_platform_social_media_and_crowdfunding
- Tags: 假新闻举报, 社会规范消息, 指令性规范, 描述性规范

### Will Humans-in-the-Loop Become Borgs? Merits and Pitfalls of Working with AI [theory subset]

- Year/journal: 2021 / MIS Quarterly
- Logic: 文章通过分析模型和三类众包图像分类实验，考察AI建议对个体准确率和独特人类知识的影响，发现AI建议提升个体准确率但削弱独特人类知识并损害群体智慧，而根据个体临界比选择性提供个性化AI建议能同时维持个体与群体表现。
- Objective family: human_task_performance
- Context: general_or_cross_domain
- Tags: 独特人类知识, 群体智慧, 个性化AI建议, AI确定性

### <scp>Context‐aware</scp> user profiles to improve media synchronicity for individuals with severe motor disabilities

- Year/journal: 2022 / Information Systems Journal
- Logic: 针对严重运动障碍者AAC沟通速度过慢的问题，文章设计在AAC中嵌入依时间、地点、沟通对象过滤词语短语的上下文感知用户画像，并以10名受试在表达三条医疗/舒适需求上的任务完成时间对比评价，发现完成时间缩短约20%-60%。
- Objective family: human_task_performance
- Context: healthcare_and_care
- Tags: 上下文感知用户画像, AAC辅助沟通系统, 医疗与舒适需求表达, 媒体同步性理论

### Achieving a Balance Between Privacy Protection and Data Collection: A Field Experimental Examination of a Theory-Driven Information Technology Solution [theory subset]

- Year/journal: 2022 / Information Systems Research
- Logic: 为在隐私保护与数据收集之间取得平衡，作者基于公正理论在移动银行App中设计了结合协商与主动推荐的隐私政策应用；现场实验表明，该设计通过提升消费者的公正感知，显著降低隐私担忧并提升披露意愿和实际披露行为，而单独协商不足以实现这一平衡。
- Objective family: behavioral_response
- Context: finance_accounting_and_investment
- Tags: 隐私政策协商, 个性化隐私推荐, 移动银行, 公正感知

### Bidder Support in Multi-item Multi-unit Continuous Combinatorial Auctions: A Unifying Theoretical Framework

- Year/journal: 2022 / Information Systems Research
- Logic: 针对连续 MIMU 组合拍卖缺乏实时投标支持的问题，本文基于子拍卖概念设计数据结构和动态规划更新算法来计算胜出水平与死亡水平，并通过与整数规划的模拟基准实验证明其在计算全部投标支持信息时快多个数量级。
- Objective family: technical_system_performance
- Context: general_or_cross_domain
- Tags: 多物品多单位组合拍卖, 实时投标人支持, 胜出水平与死亡水平, OR/XOR投标语言

### Can Positive Online Social Cues Always Reduce User Avoidance of Sponsored Search Results? [theory subset]

- Year/journal: 2022 / MIS Quarterly
- Logic: 文章通过在模拟淘宝搜索页面上操控SSR旁的正向社会线索，检验社会线索能否减少用户回避；结果发现所有线索都减少认知回避，但行为和情感回避仅在线索与用户激活的隐性担忧匹配时才减少，且卖家可信度线索具有跨担忧类型的溢出效应。
- Objective family: behavioral_response
- Context: commerce_marketing_and_customer_service
- Tags: 赞助搜索结果回避, 在线社会线索, 隐性担忧, 眼动追踪

### Designing Attentive Information Dashboards [theory subset]

- Year/journal: 2022 / Journal of the Association for Information Systems
- Logic: 针对仪表盘用户注意力资源有限且难以均衡探索信息的问题，本文设计了基于实时眼动数据计算注意力分配并提供个性化视觉注意力反馈的注意力感知仪表盘，并通过92人实验室实验对比个性化与一般反馈，发现个性化反馈显著改善了回访阶段的注意分配、降低了注意力转移率并提升了注意力资源管理。
- Objective family: behavioral_response
- Context: enterprise_work_and_knowledge
- Tags: 实时眼动追踪, 个性化视觉注意力反馈, 仪表盘注意力管理, 数据探索任务

### How to elicit and cease herding behaviour? On the effectiveness of a warning message as a debiasing decision support system [theory subset]

- Year/journal: 2022 / Decision Support Systems
- Logic: 本文将10%–90%随机同伴信息和选择后的警示消息嵌入两个金融决策模拟DSS，通过768名比利时公众的随机对照试验发现同伴信息显著诱发羊群选择且至少50%的社会证据才生效，但警示消息未能显著去偏。
- Objective family: behavioral_response
- Context: finance_accounting_and_investment
- Tags: 羊群偏差, 同伴信息干预, 警示消息去偏, 金融决策模拟DSS

### Managing Congestion in a Matching Market via Demand Information Disclosure [theory subset]

- Year/journal: 2022 / Information Systems Research
- Logic: 文章针对交友匹配市场中的需求拥堵，通过在用户资料页披露他人近期需求信息并附加容量框架提示来引导用户减少向高需求用户发请求，以随机现场实验中的请求分布和每次请求匹配率指标证明该设计可使请求转化率提高约7%-9%，从而提升匹配效率。
- Objective family: behavioral_response
- Context: digital_platform_social_media_and_crowdfunding
- Tags: 需求信息披露, 在线交友平台, 匹配效率, 消息框架提示

### Tapping into the wealth of employees’ ideas: Design principles for a digital intrapreneurship platform

- Year/journal: 2022 / Information & Management
- Logic: 针对实体建议箱无法促进员工创新想法的问题，作者通过行动设计研究设计了一个集透明流程、实时提醒、社区互动、奖励和角色识别于一体的数字内部创业平台，并在IT服务提供商进行12周现场研究，结果发现提交想法数量和用户活跃度显著提升，并成功识别出内部创业者。
- Objective family: behavioral_response
- Context: enterprise_work_and_knowledge
- Tags: 数字内部创业平台, 员工驱动创新, 行动设计研究, 想法管理

### A Warning Approach to Mitigating Bandwagon Bias in Online Ratings: Theoretical Analysis and Experimental Investigations [theory subset]

- Year/journal: 2023 / Journal of the Association for Information Systems
- Logic: 针对在线评分中的从众偏差，文章在评分界面中设计了“直接风险警告”和“风险警告加排序任务”两种警告内容，通过四个受控实验以DDAR为指标比较不同警告策略，发现带排序任务的警告既能减少从众偏差，又能避免在无偏差情境下产生新的评分扭曲。
- Objective family: behavioral_response
- Context: commerce_marketing_and_customer_service
- Tags: 从众偏差, 警告信息设计, 排序任务, 在线评分去偏

### Ambivalence Is Better than Indifference: A Behavioral and Neurophysiological Assessment of Ambivalence in Online Environments [theory subset]

- Year/journal: 2023 / MIS Quarterly
- Logic: 文章通过四个实验（含EEG）比较矛盾/冷漠态度以及双极vs双变量评分表征，发现双变量评分能区分矛盾与冷漠态度，从而使带有矛盾信息的商品购买决策比传统星级评分提高至少50%。
- Objective family: behavioral_response
- Context: commerce_marketing_and_customer_service
- Tags: 矛盾态度与冷漠态度, 双变量评分量表, 在线星级评分缺陷, 信息顺序与购买决策

### Augmenting Password Strength Meter Design Using the Elaboration Likelihood Model: Evidence from Randomized Experiments [theory subset]

- Year/journal: 2023 / Information Systems Research
- Logic: 针对传统密码强度计反馈设计缺乏理论支撑、弱密码仍普遍的问题，文章在强度算法不变的前提下，基于 ELM 中央路径为强度计加入恐惧诉求、同伴比较、共同纽带三类说服消息，并通过概念验证调查、受控实验室实验和真实论坛实地实验表明，同伴比较消息显著增加了用户修改密码的次数与密码强度提升量。
- Objective family: behavioral_response
- Context: general_or_cross_domain
- Tags: 密码强度计, 说服性警告消息, ELM中央路径, 同伴比较排名

### Be Together, Run More: Enhancing Group Participation in Fitness Technology [theory subset]

- Year/journal: 2023 / Journal of the Association for Information Systems
- Logic: 为促进健身App中的群体跑步参与，文章利用跑步App新增的Running Spot功能（可见同组人在同一指定跑步点跑步）通过降低心理距离和促进线下随意社交互动来提升团体活跃度；基于151个团体38周面板数据的DID+PSM分析显示该功能显著提高团体参与度，且在小规模、中等距离团体中效应更强。
- Objective family: behavioral_response
- Context: healthcare_and_care
- Tags: Running Spot跑步点, 线下群体参与, 团体活跃度, 心理距离与关系凝聚

### Could Gamification Designs Enhance Online Learning Through Personalization? Lessons from a Field Experiment [theory subset]

- Year/journal: 2023 / Information Systems Research
- Logic: 本文针对MOOC学习者自我调节学习不足的问题，在KEEP MOOC平台上设计并实施“个人/社会比较×积极/消极目标框架”四类游戏化绩效反馈，通过5周田野实验追踪学生数字足迹，发现只有与学习者目标导向匹配的反馈才能提升SRL参与、学习效率和测试成绩，而不匹配的反馈会损害掌握目标导向学生的参与。
- Objective family: behavioral_response
- Context: education_training_and_learning
- Tags: 游戏化绩效反馈, 目标导向个性化, 自我调节学习(SRL), MOOC在线学习

### Customer Complaint Avoidance: A Randomized Field Experiment of Platform Governance Based on Value Co-Creation and Appropriation [theory subset]

- Year/journal: 2023 / MIS Quarterly
- Logic: 针对P2P长租平台租客投诉问题，平台设计并随机发送包含不同价值共创/价值获取陈述的提醒短信，结果发现租客中心型陈述减少投诉、房东中心型陈述增加投诉，且竞争型价值获取强化动机而合作型价值获取因搭便车削弱动机。
- Objective family: substantive_domain_outcome
- Context: digital_platform_social_media_and_crowdfunding
- Tags: P2P长租平台, 投诉预防消息设计, 价值共创与价值获取, 房东搭便车

### Designing Conversational Dashboards for Effective Use in Crisis Response [theory subset]

- Year/journal: 2023 / Journal of the Association for Information Systems
- Logic: 针对普通公众难以透明使用危机响应仪表盘的问题，文章基于有效使用理论设计并实现了支持自然语言交互和对话式引导的COVID-19会话式仪表盘，通过271人实验发现自然语言交互能提高透明交互，并进而提高找信息的效率和正确率。
- Objective family: human_task_performance
- Context: public_sector_crisis_and_humanitarian
- Tags: 会话式仪表盘, 自然语言交互, 对话式引导, 危机响应信息查询

### Differential Impact of Content in Online Communication on Heterogeneous Candidates: A Field Study in Technical Recruitment [theory subset]

- Year/journal: 2023 / Information Systems Research
- Logic: 针对技术招聘中如何通过在线沟通内容吸引合适候选人的问题，文章在招聘邮件中嵌入员工工作成果或个人兴趣两类内容，通过随机田野实验比较不同绩效和资历候选人的实际申请行为，发现工作成果内容提高高绩效候选人申请概率并降低低绩效候选人申请概率，个人兴趣内容仅提高初级候选人申请概率。
- Objective family: behavioral_response
- Context: enterprise_work_and_knowledge
- Tags: 技术招聘, 在线沟通内容, 候选人异质性, 员工社交媒体帖子

### Digital nudging for technical debt management at Credit Suisse [theory subset]

- Year/journal: 2023 / European Journal of Information Systems
- Logic: 针对自上而下技术债管理难以触及团队日常决策的问题，Credit Suisse设计了一个基于Tableau的可视化数字助推，通过评级、社会比较和趋势等设计元素向软件开发团队呈现IT应用技术债状态；以一年内技术债指数变化和前后问卷为评价指标，结果显示实际使用助推的团队技术债下降，而未使用的团队上升，说明数字助推能有效引导集体技术债决策。
- Objective family: substantive_domain_outcome
- Context: enterprise_work_and_knowledge
- Tags: 技术债管理, 数字助推, Tableau可视化仪表盘, 软件研发团队

### Does Social Influence Change with Other Information Sources? A Large-Scale Randomized Experiment in Medical Crowdfunding [theory subset]

- Year/journal: 2023 / Information Systems Research
- Logic: 文章在医疗众筹病例页上随机显示或不显示朋友捐赠信息，以捐赠可能性为核心指标，发现社会影响总体上提高捐赠约16%，但在病例属性信息价值高时效应消失、信息价值低时效应显著，说明朋友捐赠信息主要作为信息性社会影响补充其他信息来源。
- Objective family: behavioral_response
- Context: digital_platform_social_media_and_crowdfunding
- Tags: 医疗众筹, 朋友捐赠信息提示, 案例属性信息价值, 捐赠行为随机实验

### Fun Shopping: A Randomized Field Experiment on Gamification [theory subset]

- Year/journal: 2023 / Information Systems Research
- Logic: 本文通过随机实地实验对比徽章、排行榜和优惠券对实体商场消费者购物行为的影响，发现游戏化虽在治疗期销售额增幅低于优惠券，却更能促进行走距离和店铺访问且在停止后效果持续，而优惠券效果在停止后消失。
- Objective family: behavioral_response
- Context: commerce_marketing_and_customer_service
- Tags: 徽章收集, 排行榜竞争, 实体商场游戏化, 优惠券对比

### Learning not to take the bait: a longitudinal examination of digital training methods and overlearning on phishing susceptibility [theory subset]

- Year/journal: 2023 / European Journal of Information Systems
- Logic: 针对反钓鱼培训效果随时间衰减的问题，文章设计了规则式、正念和对照三种数字化培训内容并加入100%过度学习练习，以2个月内的邮件识别测试和模拟钓鱼邮件点击为指标，发现正念培训比规则式培训保留更久且更不易受钓鱼影响，过度学习能提高谨慎并降低点击率但不改善辨别力。
- Objective family: human_task_performance
- Context: cybersecurity_fraud_and_compliance
- Tags: 反钓鱼培训, 正念训练, 过度学习, 技能保留

### Nudging Private Ryan: Mobile Microgiving under Economic Incentives and Audience Effects [theory subset]

- Year/journal: 2023 / MIS Quarterly
- Logic: 针对移动私密环境下小额捐赠激励效果不明的问题，文章在奖励应用中新增积分捐赠功能，并通过两轮现场实验改变返现/配比激励、推送通知和社交可见性，发现低激励隐性场景下返现更有效、高激励或可见场景下配比更有效且推送通知稳定提升捐赠行为，从而建立解释该机制的理论模型。
- Objective family: behavioral_response
- Context: public_sector_crisis_and_humanitarian
- Tags: 积分捐赠, 推送通知数字助推, 返现与配比补贴, 社交可见性/观众效应

### On the Same Page? What Users Benefit from a Desktop View on Mobile Devices [theory subset]

- Year/journal: 2023 / Information Systems Research
- Logic: 本文通过两个实验室酒店预订实验证明，相比单页桌面信息架构，将信息分层分布到多页的移动信息架构降低了用户的决策准确性，其机制是用户采用更省力的启发式策略，而在不一致移动IA下用户会转而增加努力以避免准确性继续下降。
- Objective family: human_task_performance
- Context: commerce_marketing_and_customer_service
- Tags: 移动信息架构, 桌面视图, 多属性选择任务, 努力-准确性权衡

### Pushing Yourself Harder: The Effects of Mobile Touch Modes on Users’ Self-Regulation [theory subset]

- Year/journal: 2023 / Information Systems Research
- Logic: 针对显性健康干预失效问题，本文将移动App的触摸交互设计为按压/轻触模式，借助具身认知激活趋近动机，实验表明按压相比轻触显著提高选择健康饮料、设立更高锻炼目标并减少卫生违规等自我调节行为。
- Objective family: behavioral_response
- Context: healthcare_and_care
- Tags: 按压与轻触触摸模式, 具身认知, 健康自我调节, 移动健康App助推

### ROLEX: A Novel Method for Interpretable Machine Learning Using Robust Local Explanations

- Year/journal: 2023 / MIS Quarterly
- Logic: 针对黑箱医疗预测模型缺乏可信个体解释的问题，本文设计ROLEX局部解释方法，通过直接优化采样中心与半径、加入SMOTE并选择线性/非线性局部解释模型来提高局部保真度，以local fidelity和LDA-fidelity为指标在三个医疗数据集上与LIME/LS/LEAP比较，结果表明ROLEX能生成更忠实、更稳健的个体级解释。
- Objective family: analytic_quality
- Context: healthcare_and_care
- Tags: 局部模型无关解释, 局部保真度评估, 脆性骨折风险预测, SMOTE过采样

### Standardize or Let a Thousand Flowers Bloom? Interface Design Coordination between Software Platforms and Hosted Apps [theory subset]

- Year/journal: 2023 / MIS Quarterly
- Logic: 针对平台与应用界面协调设计价值不明的问题，文章在微信平台上操纵笑话应用的界面相似性、嵌入性和同步性，发现三者在高条件下增强用户分组感知，并显著促进平台到应用的正向衍生使用，但没有显著促进应用回流平台的反向衍生使用。
- Objective family: behavioral_response
- Context: digital_platform_social_media_and_crowdfunding
- Tags: 界面相似性, 界面嵌入性, 界面同步性, 平台-应用衍生使用

### The Attraction Effect in Crowdfunding [theory subset]

- Year/journal: 2023 / Information Systems Research
- Logic: 针对回报式众筹奖励菜单中能否通过加入诱饵选项影响出资者选择的问题，文章设计并比较无诱饵、价格诱饵和质量诱饵三种数字奖励菜单，以选择高价目标奖励的人数比例为核心指标，通过七项在线实验和一项Kickstarter实地研究，发现诱饵选项使选择高价奖励的比例提高18.8–28.2个百分点。
- Objective family: behavioral_response
- Context: digital_platform_social_media_and_crowdfunding
- Tags: 吸引效应（诱饵效应）, 奖励菜单设计, 回报式众筹, 显著性理论

### The Effectiveness of Highlighting Different Communication Orientations in Promoting Mobile Communication Technology at Work vs. at Home: Evidence from a Field Experiment [theory subset]

- Year/journal: 2023 / Journal of the Association for Information Systems
- Logic: 针对4G服务推广中如何依据工作/家庭领域和沟通对象设计促销信息的问题，文章通过随机现场实验比较促进聚焦与防御聚焦的短信框架，发现与领域和沟通对象匹配的框架能显著提高实际购买率，如工作域强调与同事的促进聚焦、家庭域强调避免失联的防御聚焦。
- Objective family: behavioral_response
- Context: commerce_marketing_and_customer_service
- Tags: 4G服务推广, 调节焦点信息框架, 短信促销与位置情境定向, 工作-家庭领域沟通

### Contextual Targeting in mHealth Apps: Harnessing Weather Information and Message Framing to Increase Physical Activity [theory subset]

- Year/journal: 2024 / Information Systems Research
- Logic: 针对mHealth推送未考虑天气导致干预效果有限的问题，本文设计基于实时天气（晴/阴）自动选择收益/损失框架消息的推送策略，通过三项随机田野实验以是否完成10000步和步数为指标评估，发现晴天用损失框架、阴天用收益框架显著提高步行目标完成率且重复四次不衰减。
- Objective family: behavioral_response
- Context: healthcare_and_care
- Tags: 天气情境感知, 消息框架, 体力活动, 随机田野实验

### Delays in Information Presentation Lead to Brain State Switching, Which Degrades User Performance, and There May Not Be Much We Can Do about It [theory subset]

- Year/journal: 2024 / MIS Quarterly
- Logic: 本文通过fMRI发现系统长延迟会诱发脑状态切换，进而显著延长延迟后任务的决策时间，并通过行为实验检验四种等待界面干预，发现它们只能部分缓解而不能消除这一性能损害。
- Objective family: human_task_performance
- Context: general_or_cross_domain
- Tags: 系统延迟, 脑状态切换, fMRI, 等待期干预设计

### Encouraging Eco-driving with Post-trip Visualized Storytelling: An Experiment Combining Eye-Tracking and a Driving Simulator [theory subset]

- Year/journal: 2024 / Information Systems Research
- Logic: 针对如何通过环保可视化促进实际生态驾驶的问题，本文设计并比较了行程后可视化叙事的关联插图与叙事顺序特征，在驾驶模拟器加眼动实验中以驾驶平稳性、制动激进性和视觉注意力等客观指标检验，结果发现前瞻叙事下成对动画比静态图更能提升生态驾驶行为，且可行性感知是行为改变的重要中介。
- Objective family: behavioral_response
- Context: logistics_transport_supply_chain_and_manufacturing
- Tags: 行程后可视化叙事, 生态驾驶行为, 前瞻/回顾叙事顺序, 眼动追踪与驾驶模拟

### More Than a Bot? The Impact of Disclosing Human Involvement on Customer Interactions with Hybrid Service Agents [theory subset]

- Year/journal: 2024 / Information Systems Research
- Logic: 在电信网站混合服务代理聊天中，文章通过操纵欢迎语/接管消息是否披露人类员工参与，发现披露使顾客因印象管理关注而采用更拟人化沟通风格，进而使聊天机器人将更多消息转交人工，增加员工工作负荷。
- Objective family: behavioral_response
- Context: commerce_marketing_and_customer_service
- Tags: 人类参与披露, 混合服务代理, 顾客沟通风格, 印象管理

### Roles of Feedback and Phishing Characteristics in Antiphishing Training Performance: Perspectives of Goal Setting and Skill Acquisition [theory subset]

- Year/journal: 2024 / Journal of the Association for Information Systems
- Logic: 本文在反钓鱼测验式训练中操纵反馈类型、反馈数量、钓鱼线索显著性和感知检测效能，发现示例式反馈在含链接邮件中显著提高检测准确率并减少决策回避，同时反馈数量通过调节线索显著性的作用影响训练绩效。
- Objective family: human_task_performance
- Context: cybersecurity_fraud_and_compliance
- Tags: 反钓鱼培训, 示例式反馈, 决策回避, 钓鱼线索显著性

### The Effects of Featuring Product Sampling Reviews on E-Tailer Websites

- Year/journal: 2024 / Journal of the Association for Information Systems
- Logic: 文章针对电商平台是否应置顶展示披露型产品试用评论的问题，用真实销售/评论面板DID和情境实验检验商品页置顶展示试用评论的设计，发现它通过品牌质量感知提升销量、通过感知不公平减少有机评论，但中介分解后净销售效应仍为正。
- Objective family: behavioral_response
- Context: commerce_marketing_and_customer_service
- Tags: 产品试用评论, 赞助评论披露, 商品页置顶展示, 有机评论挤出

### Using Digital Nudges to Enhance Collective Intelligence in Online Collaboration: Insights from Unexpected Outcomes [theory subset]

- Year/journal: 2024 / MIS Quarterly
- Logic: 本文针对临时在线小组协作过程薄弱的问题，在 POGS/TCI 界面嵌入四种数字助推，通过随机实验比较各组在技能利用、任务策略、集体努力上的中介差异，发现技能引导机器人能通过提高技能利用提升集体智慧，而待办列表和实时反馈显示却产生了意料之外的负向中介效应。
- Objective family: human_task_performance
- Context: general_or_cross_domain
- Tags: 数字助推, 在线临时团队, 集体智慧, 协作过程干预

### Addressing Online Users’ Suspicion of Sponsored Search Results: Effects of Informational Cues [theory subset]

- Year/journal: 2025 / Information Systems Research
- Logic: 针对用户对偏离查询词的赞助搜索结果产生怀疑而回避的问题，该文在模拟淘宝搜索页上向被试展示附带评分信息线索的SSR，并用认知/情感/行为回避、眼动和点击等指标评价，结果发现当SSR品牌知名或评分与前列自然结果相当时，信息线索通过降低决策不确定性/平台恶意感知显著增加用户对SSR的处理。
- Objective family: behavioral_response
- Context: commerce_marketing_and_customer_service
- Tags: 赞助搜索结果回避, 用户生成内容评分线索, 品牌知名度调节, 眼动追踪实验

### Augmented Reality at Work: Attention Management and Its Impact on Work Performance

- Year/journal: 2025 / MIS Quarterly
- Logic: 针对飞机检查中反复切换指令与实物导致注意力流失的问题，作者设计了用AR眼镜在周边视野显示步骤指令的电子工卡，并通过现场实验证明AR比手机更能通过提升工作注意力提高检查绩效，且该优势在高情境依赖、低复杂信息下最大。
- Objective family: human_task_performance
- Context: enterprise_work_and_knowledge
- Tags: 增强现实工卡, 注意力分配, 信息呈现位置, 飞机维修现场实验

### Enhancing User Privacy Through Ephemeral Sharing Design: Experimental Evidence from Online Dating [theory subset]

- Year/journal: 2025 / Information Systems Research
- Logic: 为缓解在线交友因隐私顾虑导致的冷启动问题，文章在Summer平台的匹配请求流程中引入“阅后即焚”照片上传交互；7万余名用户的随机田野实验表明，与持久照片相比，该设计促使发送者上传更多含人脸照片，并通过这一披露增加获得更多匹配和接收者消息，且该效应由隐私关注降低所驱动、对隐私敏感用户更强。
- Objective family: behavioral_response
- Context: digital_platform_social_media_and_crowdfunding
- Tags: 阅后即焚, 在线交友冷启动, 隐私增强设计, 照片披露

### From Detractors to Enhancers: Harnessing the Power of Ad Customization for User Engagement on Media Websites [theory subset]

- Year/journal: 2025 / Journal of the Association for Information Systems
- Logic: 针对广告降低媒体网站参与度的问题，文章在音乐新闻网站上设计并部署广告数量定制（AQC）界面，通过随机现场实验比较 AQC 与默认广告和无广告条件，发现 AQC 显著提高访问时长、页面访问数和回访率，且移动设备用户在访问时长上的提升更强。
- Objective family: behavioral_response
- Context: other_context
- Tags: 广告数量定制, 用户参与度, 随机现场实验, 设备类型调节

### Improving Students’ Argumentation Skills Using Dynamic Machine-Learning–Based Modeling [theory subset]

- Year/journal: 2025 / Information Systems Research
- Logic: 针对大规模教育中论证反馈不足的问题，作者构建了基于论证挖掘的ArgueLearn动态建模写作反馈系统，并通过三类实验对比脚本式、自适应、静态/无建模，结果证明动态建模能显著提高学生论证写作的客观质量并迁移到另一论证领域。
- Objective family: human_task_performance
- Context: education_training_and_learning
- Tags: 动态行为建模, 论证挖掘, 论证写作反馈, 同伴互评

### Mobile Advertising in Distracted Environments: Exploring the Impact of Distractions on Dual-Task Interference [theory subset]

- Year/journal: 2025 / MIS Quarterly
- Logic: 针对用户在环境干扰下使用手机时弹出广告效果不确定的问题，文章通过自研Anagram App控制弹出广告的内容一致性、投放时机和任务-环境距离，以品牌再认得分为主要结果，发现任务投入与广告再认正相关、广告与环境内容一致且安排在低环境投入时段能显著提升再认，而增大屏幕距离会削弱这一提升。
- Objective family: human_task_performance
- Context: commerce_marketing_and_customer_service
- Tags: 移动弹出广告, 双任务干扰, 广告-环境一致性, 品牌再认

### Privacy Concerns and Data Donations: Do Societal Benefits Matter? [theory subset]

- Year/journal: 2025 / MIS Quarterly
- Logic: 针对数据捐赠中隐私担忧阻碍捐赠的问题，作者在DataDonors和Fight COVID-19两个数据捐赠应用中操纵隐私控制与（隐性/显性）社会效益呈现，用捐赠条目总数衡量捐赠决策，发现隐私担忧抑制捐赠，但提供隐私控制或让用户感知社会效益会显著削弱这一抑制效应。
- Objective family: behavioral_response
- Context: healthcare_and_care
- Tags: 数据捐赠, 隐私担忧, 社会效益信息, 隐私控制设置

### Real-Time Sales Data, Streamer Improvisation, and Sales Performance: Evidence From Live Stream Selling

- Year/journal: 2025 / MIS Quarterly
- Logic: 本文通过淘宝直播随机田野实验，将预售商品实时销售数据显示在处理组主播仪表盘上，发现相比对照组，处理组主播更倾向催促下单、使用情感化语言并调整语速和讲解时长，从而带来约40.21%的预售商品销量提升。
- Objective family: behavioral_response
- Context: commerce_marketing_and_customer_service
- Tags: 预售商品实时销售数据, 主播即兴销售策略, 淘宝直播仪表盘, 随机田野实验

### The Fog of Warnings: How Non-Security-Related Notifications Diminish the Efficacy of Security Warnings [theory subset]

- Year/journal: 2025 / MIS Quarterly
- Logic: 针对日常通知的习惯化泛化导致用户第一次见到相似安全警告就忽视的问题，文章通过设计视觉上或交互方式上更独特的安全警告（如滑块交互）作为干预，以警告忽略率、反应时间和fMRI脑激活为客观指标开展两项现场实验和一项fMRI实验，发现两种干预均能显著削弱泛化并提高警告遵从。
- Objective family: behavioral_response
- Context: cybersecurity_fraud_and_compliance
- Tags: 习惯化泛化, 警告视觉区分度, 警告交互模式, 浏览器安全警告

### A Field Experiment in Local Personalization for Charitable Crowdfunding [theory subset]

- Year/journal: 2026 / MIS Quarterly
- Logic: 针对本地个性化能否激活家乡偏好并产生何种分配后果的问题，文章在DonorsChoose对近16万名此前捐赠非本地项目的捐赠者随机发送本地化或默认个性化邮件，发现本地个性化显著提升打开、点击和捐款率，但将资金更多引向高收入及相似社区，且对受社会影响型捐赠者只提升参与而不提升捐款。
- Objective family: behavioral_response
- Context: digital_platform_social_media_and_crowdfunding
- Tags: 本地个性化邮件, 家乡偏好, 社会影响, 慈善众筹资金分配

### Enhancing AI-Assisted Purchase Decisions: The Role of the Sense of Autonomy [theory subset]

- Year/journal: 2026 / MIS Quarterly
- Logic: 针对AI推荐系统忽视消费者独特性的问题，文章通过高自主感描述和个人智能手机端AI设计增强消费者的自主感，使消费者更多融入个人偏好，实验室和实地实验均显示购买意愿、满意度、实际销量提升且退货率降低。
- Objective family: behavioral_response
- Context: commerce_marketing_and_customer_service
- Tags: 自主感, AI推荐系统, 独特性忽视, 退货率

### From Smartphones to Smart Students: Learning vs. Distraction Using Smartphones in the Classroom

- Year/journal: 2026 / Information Systems Research
- Logic: 文章通过两轮课堂随机对照实验，以自研手机词典App作为辅助教学工具，比较禁止手机、允许随意使用、教师引导使用和纸质词典四种条件下学生前测后测成绩增益的变化，并结合视频编码的学习/分心时间发现，教师引导下的智能手机学习收益足以抵消分心损失并显著提升学生学业表现。
- Objective family: substantive_domain_outcome
- Context: education_training_and_learning
- Tags: 智能手机课堂政策, 学习时间与分心时间, 手机词典App辅助教学, 职业学校语文课堂

### Overcoming Breakdowns in Customer-Chatbot Interaction: Design and Impact of Collaborative Repair Strategies [theory subset]

- Year/journal: 2026 / MIS Quarterly
- Logic: 针对客服聊天机器人理解失败导致对话中断的问题，本文基于 TLCE-bot 理论设计并实现了将实时中断类型诊断与自适应修复消息相结合的协作式修复策略，并在保险聊天机器人中通过随机现场实验显示，相比让顾客单独重试的基线策略，该策略提高了中断解决率、降低了立即放弃率，并部分缓解了顾客负面反馈与满意度下降。
- Objective family: behavioral_response
- Context: commerce_marketing_and_customer_service
- Tags: 对话中断修复, 协作式人机交互, 保险客服聊天机器人, 自适应修复消息

## recommendation_search_and_matching (34)

### A Novel Recommendation Model for Online-to-Offline Service Based on the Customer Network and Service Location [theory subset]

- Year/journal: 2020 / Journal of Management Information Systems
- Logic: 针对O2O评分数据稀疏且忽略服务位置的问题，文章设计了基于顾客共同使用网络与服务位置距离的CNLRec推荐模型，在Dianping O2O和MovieLens 100K上以Precision、Recall、F-Score与多种方法比较，结果显示CNLRec在低密度稀疏数据下显著优于对比方法，并验证了顾客网络属性和服务位置的贡献。
- Objective family: analytic_quality
- Context: commerce_marketing_and_customer_service
- Tags: O2O服务推荐, 顾客共现网络, 服务位置距离, 稀疏评分矩阵

### A decision support framework and prototype for aircraft dispatch assessment

- Year/journal: 2020 / Decision Support Systems
- Logic: 针对飞机短停放行评估中维修手册检索耗时且决策支持不足的问题，文章设计了一个自动解析TSM/AMM/MEL并生成、过滤、排序维修替代方案的Web/移动原型，通过信息检索实验和真实运行环境演示，发现文档检索时间下降73%、端到端放行决策时间可减少约98%。
- Objective family: human_task_performance
- Context: logistics_transport_supply_chain_and_manufacturing
- Tags: 飞机放行评估, 维修手册自动检索, 维护替代方案排序, 移动决策支持原型

### A social recommendation approach for reward-based crowdfunding campaigns [theory subset]

- Year/journal: 2020 / Information & Management
- Logic: 针对众筹成功率低、发起人难以找到合适支持者的问题，文章构建按筹资阶段动态切换社交关系、偏好与经济能力权重的支持者推荐系统；实验表明其点赞率和分享率显著高于内容、协同和社交基线，证明分阶段社交推荐能更有效识别潜在支持者。
- Objective family: behavioral_response
- Context: digital_platform_social_media_and_crowdfunding
- Tags: 奖励式众筹, 支持者推荐, 分阶段推荐, Facebook社交关系

### Can Recommender Systems Reduce Healthcare Costs? The Role of Time Pressure and Cost Transparency in Prescription Choice [theory subset]

- Year/journal: 2020 / MIS Quarterly
- Logic: 针对开处方时缺乏药价信息导致可避免的高成本处方问题，文章设计了一个在处方点显示等效替代药物及其费用的临床推荐系统，以查看率和处方调整率为客观指标，通过两个受控实验和一个访谈发现成本透明促使大部分处方者转向低成本等效药，但医生受成本框架影响、执业护师/医生助理受时间压力影响。
- Objective family: behavioral_response
- Context: healthcare_and_care
- Tags: 处方成本透明, 临床推荐系统, 时间压力, 等效替代药品推荐

### Conversational Recommender Systems and natural language:

- Year/journal: 2020 / Decision Support Systems
- Logic: 为检验自然语言对对话式推荐系统的影响，文章实现了模块化框架 ConveRSE，先用合成数据做组件消融测量 HitRate 损失，再在三个领域开展真实用户实验比较纯 NL、按钮和混合模式，结果表明实体识别准确率在冷启动时最关键，而自然语言与按钮结合的混合交互在交互成本和推荐准确率上总体最佳。
- Objective family: analytic_quality
- Context: general_or_cross_domain
- Tags: ConveRSE框架, 自然语言与按钮混合交互, 对话式推荐系统组件消融, 实体识别与冷启动

### Different but Equal? A Field Experiment on the Impact of Recommendation Systems on Mobile and Personal Computer Channels in Retail

- Year/journal: 2020 / Information Systems Research
- Logic: 通过在韩国时尚电商网站上进行随机现场实验，将协同过滤推荐面板随机分配给PC与移动端顾客，并用双重差分和基尼系数分析发现，推荐系统对移动端顾客的浏览、点击、购买和转化促进作用普遍强于PC端，同时提升浏览多样性但对销售多样性无显著净效应，移动渠道本身带来更高的销售多样性。
- Objective family: behavioral_response
- Context: commerce_marketing_and_customer_service
- Tags: 移动端与PC端推荐效果对比, 协同过滤推荐面板, 销售多样性, 推荐系统现场随机实验

### Matching Mobile Applications for Cross-Promotion

- Year/journal: 2020 / Information Systems Research
- Logic: 为解决移动应用市场高搜索成本和跨推广配对低效问题，文章构建了基于LDA相似度、机器学习预测和广义延迟接受算法的应用匹配平台，并用韩国41,294个随机匹配跨推广活动的数据验证，发现用户在下载阶段偏好差异应用而在使用阶段偏好相似应用，且加入分析和个体用户数据可显著提升下载与使用效果。
- Objective family: behavioral_response
- Context: digital_platform_social_media_and_crowdfunding
- Tags: 跨应用交叉推广, LDA主题相似度, 延迟接受匹配算法, 移动应用广告效果

### Preference enhanced hybrid expertise retrieval system in community question answering services

- Year/journal: 2020 / Decision Support Systems
- Logic: 为减少CQA未回答问题，本文设计了融合回答者偏好、文本熟悉度加权PageRank权威和QLL相似度熟练度的PEHER系统，用MRR、P@30、R@30、Accuracy、MSC@30在4个真实数据集上与20个基线比较，结果在92.00%的比较情形中取得最优。
- Objective family: analytic_quality
- Context: digital_platform_social_media_and_crowdfunding
- Tags: 社区问答专家检索, 回答者偏好建模, 混合文本与网络方法, CBEN边权文本熟悉度

### Secure attribute-based search in RFID-based inventory control systems

- Year/journal: 2020 / Decision Support Systems
- Logic: 针对库存RFID系统只能按单一ID搜索且低成本无源标签无法承载重密码原语的问题，该文设计了基于二次剩余的轻量属性搜索协议；通过Scyther形式化验证和与既有搜索协议的对比，证明其在Dolev-Yao敌手下安全（抗重放/冒充）并满足健全性/完备性，从而让合法读写器无需知道标签ID即可安全查询满足某类属性的库存商品。
- Objective family: risk_security_and_safety
- Context: logistics_transport_supply_chain_and_manufacturing
- Tags: RFID属性搜索, 库存盘点, 二次剩余轻量加密, EPC C1G2合规

### Taming Complexity in Search Matching: Two-Sided Recommender Systems on Digital Platforms

- Year/journal: 2020 / MIS Quarterly
- Logic: 针对数字平台上双边搜索匹配的不可约复杂性，文章设计了同时学习学生和大学两侧涌现的双边推荐系统，并通过基于教育平台的智能体仿真，以AIC和平均适应度评估，发现双边推荐在驯服不确定性和提升双方绩效上均优于单边推荐和无推荐。
- Objective family: substantive_domain_outcome
- Context: education_training_and_learning
- Tags: 双边推荐系统, 复杂适应商业系统, 搜索匹配复杂性, MOOC教育平台

### The crowd against the few: Measuring the impact of expert recommendations

- Year/journal: 2020 / Decision Support Systems
- Logic: 针对专家推荐在真实在线环境中能否改善用户行为的问题，该文在一大型视频点播网站中向商业推荐系统加入雇佣专家手工维护的推荐并开展随机对照实验；以观看数、访问数、推荐点击、回访/留存、多样性和品味覆盖为指标，发现虽然专家推荐本身点击率低于预期，但混合专家推荐显著提高了平台使用量和推荐多样性。
- Objective family: behavioral_response
- Context: other_context
- Tags: 专家推荐, 视频点播平台, 用户行为随机对照实验, 推荐多样性

### TheoryOn: A Design Framework and System for Unlocking Behavioral Knowledge Through Ontology Learning

- Year/journal: 2020 / MIS Quarterly
- Logic: 针对全文搜索引擎难以加工行为构念知识的问题，作者提出BOLT框架并用其构建TheoryOn本体检索系统，通过数据挖掘实验和随机用户实验验证系统抽取与检索能力，结果显示TheoryOn在信息检索任务上的F值比EBSCOhost和Google Scholar高37%-121%。
- Objective family: human_task_performance
- Context: enterprise_work_and_knowledge
- Tags: 行为本体学习, 构念检索, 理论网络可视化, 学术文献信息检索

### A social investing approach for portfolio recommendation

- Year/journal: 2021 / Information & Management
- Logic: 为帮助缺乏金融知识的投资者从社交投资平台海量帖文中选出可盈利标的，本文设计了融合帖文情感、作者知识与影响力、公司财务面的集体智慧投资组合推荐机制；eToro上的30日模拟交易实验表明，该机制推荐的组合获得30.369%的收益率，并在Treynor比率和Jensen's alpha上优于S&P 500及其他基准方法。
- Objective family: economic_and_welfare
- Context: finance_accounting_and_investment
- Tags: eToro社交投资平台, 帖文群体智慧挖掘, 投资者可信度评分, 风险偏好定制组合

### A social mechanism for task-oriented crowdsourcing recommendations [theory subset]

- Year/journal: 2021 / Decision Support Systems
- Logic: 针对任务型众包中请求者难以及时找到合适贡献者的问题，本文设计了综合贡献者偏好、历史表现和社交影响并采用AHP加权的SCT推荐机制；实验以推荐准确率、满意度、契合度、喜爱度和接受意愿等指标对比四种基准模型，结果显示SCT机制显著更优。
- Objective family: analytic_quality
- Context: digital_platform_social_media_and_crowdfunding
- Tags: 任务型众包, 社交推荐机制, 贡献者匹配, AHP加权

### Finding a Needle in the Haystack: 
Recommending Online Communities on Social Media Platforms Using Network and Design Science

- Year/journal: 2021 / Journal of the Association for Information Systems
- Logic: 针对社交媒体在线社区订阅推荐问题，文章利用Twitter列表的三种网络关系设计结构特征（结构洞同配性、LCCR等）和通用社区特征，使用神经网络生成订阅推荐，以Precision/Recall/F-score/MRR/DCG等指标评价，发现网络+通用特征在Top-1最佳、全部特征组合在Top-5/Top-10最佳。
- Objective family: analytic_quality
- Context: digital_platform_social_media_and_crowdfunding
- Tags: Twitter列表推荐, 网络结构特征, 局部聚类系数排序, 社区订阅推荐

### Algorithmic Assortative Matching on a Digital Social Medium

- Year/journal: 2022 / Information Systems Research
- Logic: 针对freemium社交游戏随机推荐导致高价值用户与高活跃社区匹配不足的问题，文章设计了基于XGBoost CLV预测和团队活动度评分的用户-团队正向分类匹配系统，通过现场实验对比开关状态，发现该系统显著提高用户参与、社交和收入，且该效果由团队生产技术的超模性和社交行为中介所驱动。
- Objective family: behavioral_response
- Context: digital_platform_social_media_and_crowdfunding
- Tags: 同配匹配, 团队推荐, 免费增值游戏, 社交行为中介

### Combining review-based collaborative filtering and matrix factorization: A solution to rating's sparsity problem [theory subset]

- Year/journal: 2022 / Decision Support Systems
- Logic: 针对评分稀疏导致协同过滤和矩阵分解不准确的问题，文章提出RMF，先用评论特征级情感分析构建商品-主题矩阵并填充缺失评分，再进行矩阵分解生成推荐，在两个真实电商数据集上证明其MAE更低、推荐命中率更高。
- Objective family: analytic_quality
- Context: commerce_marketing_and_customer_service
- Tags: 评分稀疏性, 在线评论特征级情感分析, 评分填充, 矩阵分解推荐

### How Do Recommender Systems Lead to Consumer Purchases? A Causal Mediation Analysis of a Field Experiment

- Year/journal: 2022 / Information Systems Research
- Logic: 作者在一家在线书店开展随机实地实验，部署基于协同过滤的推荐系统，运用因果中介分析证明推荐系统通过扩大考虑集规模和增加消费者对备选项目的参与度来提升购买转化率。
- Objective family: behavioral_response
- Context: commerce_marketing_and_customer_service
- Tags: 推荐系统, 考虑集, 因果中介分析, 在线图书零售

### Diversity Preference-Aware Link Recommendation for Online Social Networks [theory subset]

- Year/journal: 2023 / Information Systems Research
- Logic: 针对社交网络好友推荐忽视个体多样性偏好的问题，文章设计DPA-LR方法，在GCN候选好友基础上通过维度级优化选择与用户多样性偏好匹配的好友，并在Google+等数据集上同时显著提高DPMS与precision/recall/F1。
- Objective family: analytic_quality
- Context: digital_platform_social_media_and_crowdfunding
- Tags: 社交网络好友推荐, 多样性偏好, 维度级画像匹配, 好友推荐优化

### Personalized Ranking at a Mobile App Distribution Platform

- Year/journal: 2023 / Information Systems Research
- Logic: 文章用点击/安装两阶段结构模型估计个体消费者效用，据此设计结合CPA边际收入的个性化HMUM排序；政策实验显示该设计相比非个性化平均效用排序可将平台期望收入提高16.73%。
- Objective family: economic_and_welfare
- Context: digital_platform_social_media_and_crowdfunding
- Tags: 移动应用分发平台, 个性化应用排序, CPA计价收入, 点击与安装两阶段模型

### Spoiled for Choice? Personalized Recommendation for Healthcare Decisions: A Multiarmed Bandit Approach [theory subset]

- Year/journal: 2023 / Information Systems Research
- Logic: 针对在线健康平台干预选择过载导致参与不足的问题，文章设计了结合深度表示学习和理论驱动多样性约束的Thompson sampling推荐框架DLDE-MAB，在真实减肥社区数据上以Precision/Recall/nDCG/MAP等指标与多种推荐模型比较，结果显示该框架的推荐质量、多样性匹配和用户改善率均显著优于基线。
- Objective family: analytic_quality
- Context: healthcare_and_care
- Tags: 在线减重社区, 干预推荐多样性, 汤普森采样, 健康行为序列表示

### The Decoy Effect and Recommendation Systems [theory subset]

- Year/journal: 2023 / Information Systems Research
- Logic: 文章通过自建电影推荐平台，对个性化与非个性化推荐分别比较有无诱饵的推荐集合，发现非个性化推荐中诱饵会提高目标项选择概率，而个性化推荐中诱饵会促使用户转向无选项，表明诱饵效应在推荐系统中因用户对系统可靠性的期望不同而方向相反。
- Objective family: behavioral_response
- Context: commerce_marketing_and_customer_service
- Tags: 诱饵效应, 个性化推荐, 电影推荐平台, 选择实验

### Background Music Recommendation on Short Video Sharing Platforms

- Year/journal: 2024 / Information Systems Research
- Logic: 针对短视频配乐推荐中用户-视频-音乐三元关系难以建模的问题，本文设计同时考虑用户-音乐匹配和视频-音乐匹配并带注意力聚合的 DL-BGM 模型，在抖音真实数据上用 HR、NDCG 和 AL 证明其推荐效果显著优于多种基线，并在冷启动和不同数据密度、类别场景下保持稳健。
- Objective family: analytic_quality
- Context: digital_platform_social_media_and_crowdfunding
- Tags: 背景音乐推荐, 短视频平台, 用户-视频-音乐三方关系, 注意力聚合

### Facial expression-enhanced recommendation for virtual fitting rooms

- Year/journal: 2024 / Decision Support Systems
- Logic: 针对虚拟试衣间推荐未充分利用AR交互与表情信息的问题，文章在矩阵分解中设计了基于面部表情与行为/停留时间的置信度赋值和基于标题相似度的负反馈采样，并用81名用户实验的Precision和MAP证明FEERS显著优于传统反馈基线。
- Objective family: analytic_quality
- Context: commerce_marketing_and_customer_service
- Tags: 虚拟试衣间, 面部表情识别, 化妆品个性化推荐, 隐式反馈负采样

### Retargeted vs. Generic Product Recommendations: When is it Valuable to Present Retargeted Recommendations?

- Year/journal: 2024 / Information Systems Research
- Logic: 通过在电商网站商品页随机显示或隐藏基于协同过滤的推荐商品，并区分推荐是否曾被用户浏览以及用户处于购买漏斗的早晚期，研究发现generic推荐仅在漏斗早期提高转化率而retargeted推荐在漏斗晚期提高销售额，按此策略替换推荐可使总销售额提高约3%。
- Objective family: economic_and_welfare
- Context: commerce_marketing_and_customer_service
- Tags: 重定向推荐, 通用推荐, 购买漏斗阶段, 协同过滤推荐

### Task Characteristics and Incentives in Collaborative Problem Solving: Evidence from Three Field Experiments

- Year/journal: 2024 / Information Systems Research
- Logic: 文章通过实地实验识别出任务特征（难度、不确定性、紧迫性）决定协作是否降低工时，据此构建HRTech Analytics推荐系统，并发现激励不匹配导致工程师偏离推荐，通过调整激励使遵从率提高，从而优化问题解决成本。
- Objective family: operational_efficiency
- Context: enterprise_work_and_knowledge
- Tags: LTE任务特征, 协作模式推荐, 激励对齐, 工程师工时

### Timely, Granular, and Actionable: Designing a Social Listening Platform for Public Health 3.0 [theory subset]

- Year/journal: 2024 / MIS Quarterly
- Logic: 为突破现有社会倾听工具缺少上下文的问题，HealthSense以活动理论扩展为指导，将相关性、可信度和跨渠道景观评估与图传播、图神经网络结合，实现对健康相关URL的高效排序采集，从而在数据实验和实地研究中显著提升检索质量及下游药物安全分析表现。
- Objective family: analytic_quality
- Context: public_sector_crisis_and_humanitarian
- Tags: 社会倾听平台, 图神经网络与图传播, 上市后药物警戒, 阿片类药物危机监测

### When Variety Seeking Meets Unexpectedness: Incorporating Variety-Seeking Behaviors into Design of Unexpected Recommender Systems [theory subset]

- Year/journal: 2024 / Information Systems Research
- Logic: 针对消费者异质多样化寻求需求未被意外推荐系统建模的问题，文章提出距离函数+时间衰减+平稳性假设的多样化寻求度量，并将其作为个性化意外性权重加入推荐效用函数；离线AUC/HR与在线CTR/观看完成/观看时长实验均表明该方法显著优于固定权重意外推荐与生产系统，并已在视频平台全量部署。
- Objective family: behavioral_response
- Context: digital_platform_social_media_and_crowdfunding
- Tags: 多样化寻求行为, 意外性推荐, 在线A/B实验, 视频流媒体平台

### Customer Acquisition via Explainable Deep Reinforcement Learning

- Year/journal: 2025 / Information Systems Research
- Logic: 针对银行客户获取中广告顺序定向的长期收益优化与可解释性不足，文章在DRQN中加入以历史状态和静态特征查询下一次曝光特征的定制注意力机制，构成DRQN-attention模型；离策略评估显示其在H=3和H=6时平均奖励高于多个深度强化学习基线和现网策略，同时注意力权重能揭示行业、行为与季节性广告渠道选择。
- Objective family: economic_and_welfare
- Context: finance_accounting_and_investment
- Tags: 可解释强化学习, 广告渠道选择, 顺序定向, 小微企业信贷获客

### Ephemeral State-Dependent Recommendation for Digital Content [theory subset]

- Year/journal: 2025 / Information Systems Research
- Logic: 针对数字内容消费短暂状态被忽视的问题，文章在电子书平台设计并部署了根据消费者固着/觅食状态自适应切换同化/多样化推荐的方案，通过10.8万用户的随机现场实验发现一致方案整体最优、不一致方案适合偏好更流动或更广的人群，并产生正向消费溢出。
- Objective family: behavioral_response
- Context: commerce_marketing_and_customer_service
- Tags: 电子书推荐, 状态依赖推荐, 短暂偏好, 随机现场实验

### HyperCARS: Using Hyperbolic Embeddings for Generating Hierarchical Contextual Situations in Context-Aware Recommender Systems

- Year/journal: 2025 / Information Systems Research
- Logic: 为克服欧氏上下文嵌入难以表达层次情境且不可解释的问题，HyperCARS在双曲空间用VAE生成上下文嵌入，再用层次聚类构造情境路径并松散耦合到NeuMF推荐模型；在Frappe、Gowalla、Yelp上相比欧氏方法和现有CARS基线，推荐准确率、聚类分离度和可解释性均显著提升。
- Objective family: analytic_quality
- Context: general_or_cross_domain
- Tags: 双曲嵌入, 层次化上下文情境, 上下文感知推荐, 可解释性分析

### Probing Digital Footprints and Reaching for Inherent Preferences: A Cause-Disentanglement Approach to Personalized Recommendations [theory subset]

- Year/journal: 2025 / Information Systems Research
- Logic: 为消除隐式反馈中项目显著性与从众效应对内在偏好的污染，文章构建以消费者行为理论为基础的因果图并通过解纠缠表示学习分离各驱动因素，用P、MAP、NDCG在干预测试集上证明DISC显著优于基线，从而实现基于内在偏好的个性化推荐。
- Objective family: analytic_quality
- Context: commerce_marketing_and_customer_service
- Tags: 因果解纠缠, 多类型隐式反馈, 内在偏好推荐, 电商个性化推荐

### Ruckus in the Rentals, Seeking New Arrangements: Remedying the Impact of Home-Sharing on Urban Noise [theory subset]

- Year/journal: 2025 / MIS Quarterly
- Logic: 基于纽约市Airbnb交易与噪声投诉数据，文章先验证房源使用增加噪声投诉、空间/时间集中通过执法威慑削弱该效应，然后提出基于相似度和偏好得分提高聚集区房源排名的助推算法；仿真表明该算法可在收入基本不变的情况下降低城市噪声投诉。
- Objective family: multi_objective_or_tradeoff
- Context: digital_platform_social_media_and_crowdfunding
- Tags: 住房共享外部性, 城市噪声投诉, 房源排序助推算法, 执法威慑效应

### Mitigating Exposure Bias for Recommendations in Physical Spaces: An Unbiased Pairwise Ranking Approach Using Spatial Movement [theory subset]

- Year/journal: 2026 / Information Systems Research
- Logic: 为缓解实体空间POI推荐中由行人移动与空间布局造成的曝光偏差，文章提出UMPR，将行人移动建模与无偏成对排序学习结合，并用交替随机梯度上升优化；在真实购物中心数据上以Recall和DCG证明其推荐准确性显著优于各类基线，同时进一步带来增量收入和推荐公平性的提升。
- Objective family: analytic_quality
- Context: commerce_marketing_and_customer_service
- Tags: 实体空间POI推荐, 曝光偏差去偏, 行人移动建模, 购物中心店铺推荐

## planning_optimization_and_allocation (24)

### A decision support system for home dialysis visit scheduling and nurse routing

- Year/journal: 2020 / Decision Support Systems
- Logic: 针对居家透析每日护士访问排程和路线规划这一复杂手工任务，HDSS利用多准则MILP模型生成优化计划，与医院管理员手工方案相比，显著降低总行驶距离（27%~38%）和行驶时间（25%~33%），并减少每日所需护士数（11%~16%）。
- Objective family: operational_efficiency
- Context: healthcare_and_care
- Tags: 居家透析排程, 护士路径规划, 混合整数线性规划, 工作量平衡

### A dynamic shipment matching problem in hinterland synchromodal transportation

- Year/journal: 2020 / Decision Support Systems
- Logic: 为解决现货集装箱请求实时到达下的同步联运匹配问题，文章在集中式平台上设计了滚动时域方法与预处理启发式算法，以最小化运输、换装、仓储、延误和碳税总成本为目标生成请求与服务/路径的匹配；实验表明启发式算法与精确解几乎无成本差距且计算时间大幅下降，滚动时域法在各动态场景下总成本均低于贪心法。
- Objective family: operational_efficiency
- Context: logistics_transport_supply_chain_and_manufacturing
- Tags: 滚动时域方法, 同步联运匹配, 启发式算法, 集装箱多式联运

### An intelligent decision support system prototype for hinterland port logistics [theory subset]

- Year/journal: 2020 / Decision Support Systems
- Logic: 针对港口腹地集装箱运输碎片化导致的额外成本和低效问题，文章开发了一个将强化学习与动态车辆路径优化结合的智能DSS原型，并在Port of Brisbane两周真实数据上模拟货运代理使用PCS后的行动选择，发现若全体代理采用最优/合作方案总运输成本下降超过50%，且小型货运代理更应选择合作。
- Objective family: operational_efficiency
- Context: logistics_transport_supply_chain_and_manufacturing
- Tags: 港口社区系统(PCS), 腹地集装箱运输, 强化学习与车辆路径优化, 货运代理合作

### Customer-centric prioritization of process improvement projects [theory subset]

- Year/journal: 2020 / Decision Support Systems
- Logic: 针对流程改进项目优先级排序缺乏客户中心视角的问题，文章设计了一个以风险调整后NPV为目标函数、以Kano模型刻画客户满意度并将特征类型切换纳入项目组合选择的决策模型/原型，在保险公司案例中通过比较最优/强制/最差组合的NPV和鲁棒性分析证明了其适用性和决策支持价值。
- Objective family: economic_and_welfare
- Context: enterprise_work_and_knowledge
- Tags: 客户中心化, Kano模型特征类型, 流程改进项目组合选择, 风险调整后NPV

### Optimizing microtask assignment on crowdsourcing platforms using Markov chain Monte Carlo

- Year/journal: 2020 / Decision Support Systems
- Logic: 针对众包微任务平台现有算法只能在任务完成后或仅一次性估计工人质量的问题，本文提出MCMC-TA，通过GMM迭代估计工人质量并用MCMC筛选下一轮任务的最合适工人；在Google Fact Evaluation数据集上的AUC和F-Score对比表明MCMC-TA优于Raykar、ROUX和Gaussian基线，并在仅使用10%预算和存在spammer的群体条件下保持稳定。
- Objective family: analytic_quality
- Context: digital_platform_social_media_and_crowdfunding
- Tags: 众包微任务, 任务分配优化, 工人质量迭代估计, MCMC与GMM

### A novel decision support system for optimizing aircraft maintenance check schedule and task allocation

- Year/journal: 2021 / Decision Support Systems
- Logic: 针对航空公司人工维修计划低效且不优的问题，文章构建了集维修检查排程（动态规划）、任务分配（装箱启发式）与班组排班于一体的DSS；通过与合作航空公司现行计划对比，结果显示该DSS能减少A/C检次数、提高平均飞行小时、生成最优差距仅0.028%的任务分配，并在约20-30分钟内完成三年维修计划。
- Objective family: operational_efficiency
- Context: logistics_transport_supply_chain_and_manufacturing
- Tags: 维修检查排程, 维修任务装箱分配, 班组排班, 未来维修策略情景分析

### A prescriptive analytics framework for efficient E-commerce order delivery

- Year/journal: 2021 / Decision Support Systems
- Logic: 针对电商配送失败率高的问题，文章用历史订单与位置数据训练XGBoost生成每个订单的成功时段档案，再将其转为时间窗约束进行VRPTW排程，仿真显示在真实数据上相比行业基线节省了7.2%和10.2%的配送成本。
- Objective family: operational_efficiency
- Context: logistics_transport_supply_chain_and_manufacturing
- Tags: 订单成功档案, 配送时间窗推断, VRPTW调度, 末端配送成本节省

### A strategic decision-making architecture toward hybrid teams for dynamic competitive problems

- Year/journal: 2021 / Decision Support Systems
- Logic: 针对动态竞争问题中战略决策难、单机优化易陷入局部最优的问题，文章用历史数据训练LSTM奖励模型并用模型预测控制求解博弈论建议、同时用数据驱动任务划分组建计算机团队，在StarCraft II回放数据上的奖励值比较表明该架构能为低水平玩家提供安全保守且有效的战略建议，而多代理分区决策能明显提升决策质量。
- Objective family: analytic_quality
- Context: general_or_cross_domain
- Tags: 动态竞争问题, 混合人机团队, 博弈论策略建议, StarCraft II

### Analytics with digital-twinning: A decision support system for maintaining a resilient port

- Year/journal: 2021 / Decision Support Systems
- Logic: 文章针对港口电力中断后缺乏恢复决策工具的问题，设计了集成数字孪生与OCBA的韧性决策支持系统，以BoA率为核心指标评估候选设备配置并选择最优恢复行动，案例实验表明DSS推荐配置将BoA率最多提升15.74个百分点，并揭示忽略运营随机性会显著高估韧性。
- Objective family: operational_efficiency
- Context: logistics_transport_supply_chain_and_manufacturing
- Tags: 港口韧性评估, 数字孪生仿真, 电力中断恢复, 最优计算预算分配

### Bayesian Stackelberg games for cyber-security decision support

- Year/journal: 2021 / Decision Support Systems
- Logic: 针对多阶段网络攻击下的安全控制组合选择问题，文章设计了由预防性优化、HMM学习和在线防御优化组成的决策支持系统，其中在线优化被建模为贝叶斯Stackelberg博弈并用MICP高效求解；实验表明该方法在大规模攻击图上求解时间远低于现有求解器，并使案例研究的预期安全风险从0.0367降至0.00157。
- Objective family: technical_system_performance
- Context: cybersecurity_fraud_and_compliance
- Tags: 安全控制组合优化, 攻击图建模, 贝叶斯Stackelberg博弈, 混合整数锥规划

### Decisions for information or information for decisions? Optimizing information gathering in decision-intensive processes

- Year/journal: 2021 / Decision Support Systems
- Logic: 为解决DIP中信息收集与最终决策之间的成本-收益权衡，文章将CMMN流程模型转化为MDP并求解最优信息收集策略，再通过CMMN计划片段和运行期推荐器向决策者提供每个状态下的最优动作建议；在真实飞机部件维修报价案例中，该方法的期望利润约是现有决策树的两倍。
- Objective family: economic_and_welfare
- Context: commerce_marketing_and_customer_service
- Tags: CMMN与MDP集成, 信息获取策略优化, 维修合同报价, 运行期决策推荐

### Designing Personalized Treatment Plans for Breast Cancer

- Year/journal: 2021 / Information Systems Research
- Logic: 针对早期乳腺癌标准放疗计划未个体化导致疗效与损伤失衡的问题，文章构建了TCP预测与剂量优化相结合的治疗计划框架，仿真结果显示该框架能在维持TCP目标的同时大幅降低正常组织剂量，从而减少心肺并发症风险和医疗成本。
- Objective family: substantive_domain_outcome
- Context: healthcare_and_care
- Tags: 乳腺癌放疗计划优化, 肿瘤控制概率预测, 个体化剂量分布, 放射性心肺损伤与成本控制

### Filaments of crime: Informing policing via thresholded ridge estimation

- Year/journal: 2021 / Decision Support Systems
- Logic: 针对热点巡逻只盯核心而忽视周围高密度路径的问题，文章设计了DREDGE密度脊估计工具，用2018年芝加哥Part I犯罪数据生成巡逻路线模板，并以2019年早期事件在脊线缓冲区内的覆盖率（0.1英里约94%）证明其比随机热点巡逻和中心点参考更有效地覆盖犯罪。
- Objective family: analytic_quality
- Context: public_sector_crisis_and_humanitarian
- Tags: 密度脊估计, 巡逻路线优化, 犯罪热点, 警务路线模板

### Handling the Efficiency–Personalization Trade-Off in Service Robotics: A Machine-Learning Approach

- Year/journal: 2021 / Journal of Management Information Systems
- Logic: 针对自动驾驶汽车中能量效率与个性化之间的动态冲突，文章设计了一个由两个LSTM预测模型和梯度权衡模块组成的分工式机器学习制品，用实时数据同时学习高效驾驶模式与用户偏好并自动生成平衡两者的车辆配置；离线评价表明其在能耗预测和偏好估计的平均绝对偏差上显著优于多种基线模型（分别约3.5倍和6倍更准确）。
- Objective family: analytic_quality
- Context: logistics_transport_supply_chain_and_manufacturing
- Tags: 效率-个性化权衡, 自动驾驶车辆配置, 在线LSTM能耗预测, 共享汽车用户偏好建模

### How to Assign Scarce Resources Without Money: Designing Information Systems that are Efficient, Truthful, and (Pretty) Fair

- Year/journal: 2021 / Information Systems Research
- Logic: 针对无货币支付且存在最小开课人数的课程分配问题，设计RESPCT匹配机制（clinch + prioritized pointing + 最大化座位保证），在保持策略防伪和Pareto效率的同时，将合理嫉妒降低到ESTTC的约三分之一，并比无嫉妒的ESDA效率更高。
- Objective family: multi_objective_or_tradeoff
- Context: education_training_and_learning
- Tags: 课程匹配机制, 最小配额, 合理嫉妒, Top Trading Cycles

### Long-term multi-criteria improvement planning [theory subset]

- Year/journal: 2021 / Decision Support Systems
- Logic: 为应对多准则长期改进中忽视实施阻力与瓶颈的问题，文章设计了一个基于有向图和Dijkstra算法的改进路径生成框架（软件MCDMBM），以单准则改进为边、用瓶颈风险、运营变化和排名提升三指标求权衡路径；在ARWU20大学排名案例中生成5条ULB改进路径，其中p1在54组权重下56%为最优，说明该方法能生成可转化为战略行动的长期改进序列。
- Objective family: multi_objective_or_tradeoff
- Context: general_or_cross_domain
- Tags: 多准则改进规划, 逐步标杆管理, 瓶颈机制, 组织变革阻力

### An interactive decision support system for real-time ambulance relocation with priority guidelines

- Year/journal: 2022 / Decision Support Systems
- Logic: 针对德黑兰东部静态急救车部署无法及时覆盖需求的问题，文章设计了一个以两目标整数规划为核心、带实时风险分级优先指南的急救车在线重定位DSS；在基于一周真实数据与静态策略的仿真比较中，该DSS将平均覆盖率从73%提高到89%、平均响应时间从12.6分钟降至8.2分钟，并将每班总工作时间降低约9%。
- Objective family: operational_efficiency
- Context: healthcare_and_care
- Tags: 急救车实时重定位, 需求覆盖与响应时间, 风险分级优先级指南, EMS决策支持系统

### Combining analytics and simulation methods to assess the impact of shared, autonomous electric vehicles on sustainable urban mobility

- Year/journal: 2022 / Information & Management
- Logic: 本文针对SAEV城市共享出行的资源规划问题，设计了结合历史行程数据预测与智能体仿真的决策支持平台，通过模拟不同车队规模和充电桩配置下的请求拒绝率与等待时间，发现自动驾驶和电动化可将车队规模减少约一半，且仅需约28个充电桩即可维持当前服务水平。
- Objective family: operational_efficiency
- Context: logistics_transport_supply_chain_and_manufacturing
- Tags: 共享自动驾驶电动车(SAEV), 柏林自由浮动汽车共享, 充电基础设施规划, 智能体仿真

### Greening the Cloud: A Load Balancing Mechanism to Optimize Cloud Computing Networks

- Year/journal: 2022 / Journal of Management Information Systems
- Logic: 针对私有云负载不均衡和资源利用效率低的问题，文章设计了基于动态定价的最优价格模型和均衡任务分配算法，并通过数学证明和模拟表明均等分配可最小化总等待时间、保障 QoS，从而帮助组织更绿色地利用云资源。
- Objective family: operational_efficiency
- Context: general_or_cross_domain
- Tags: 私有云负载均衡, 动态定价, 队列长度约束, 等待时间最小化

### Maximizing student opportunities for in-person classes under pandemic capacity reductions

- Year/journal: 2022 / Decision Support Systems
- Logic: 文章针对疫情导致教室容量大幅缩减下的课程排课问题，设计了先最大化线下教学座位数、再最小化容量差异的两阶段MIP排课DSS；与行政人员原拟使用的贪心算法相比，该DSS在六个校区多安排了约7%的课程和近9%的线下座位，并在15分钟内解决了最大的Storrs实例。
- Objective family: operational_efficiency
- Context: education_training_and_learning
- Tags: 疫情容量缩减, 课程教学模态分配, 教室排课优化, 拆分授课模式

### Assuring quality and waiting time in real-time spatial crowdsourcing

- Year/journal: 2023 / Decision Support Systems
- Logic: 针对空间众包任务分配缺少真实通行时间且需同时保证质量与等待时间的问题，本文用LightGBM基于历史时空气候特征预测工人通行时间，再用预算约束下优先高声誉、最小等待时间的启发式算法分配任务，在成都滴滴GAIA数据模拟中相比RB-TPSC降低了请求者等待时间并提高了被选工人平均声誉。
- Objective family: multi_objective_or_tradeoff
- Context: digital_platform_social_media_and_crowdfunding
- Tags: 空间众包任务分配, LightGBM通行时间预测, 请求者等待时间, 工人声誉

### A hybrid decision support system for adaptive trading strategies: Combining a rule-based expert system with a deep reinforcement learning strategy

- Year/journal: 2024 / Decision Support Systems
- Logic: 针对现有混合交易模型缺乏自适应性和忽略投资者余额/交易量约束的问题，本文将海龟规则专家系统决策信息、投资者可用资产状态和策略梯度概率交易量调节机制融入深度强化学习，并在六个指数基金上用收益、回撤和夏普比率等指标验证，结果表明该系统在多种市场条件下优于基准和既往混合模型。
- Objective family: economic_and_welfare
- Context: finance_accounting_and_investment
- Tags: 海龟趋势跟踪规则, 深度强化学习交易, 动作概率交易量调节, 指数基金交易

### Interleaved Design for E-Learning: Theory, Design, and Empirical Findings [theory subset]

- Year/journal: 2024 / MIS Quarterly
- Logic: 针对在线交错学习可能增加认知负荷的问题，文章提出并实现以相关主题交错为核心、由HMM弱项检测、知识图谱和调度引擎支持的个性化在线学习系统，并通过510名初中生的随机现场实验，用后测成绩证明相关交错显著优于非交错和无关交错，且对弱学习者更有利。
- Objective family: substantive_domain_outcome
- Context: education_training_and_learning
- Tags: 相关交错学习, 认知负荷理论, 个性化学习调度, 弱项主题检测

### Smart Markets for Real-Time Allocation of Multiproduct Resources: The Case of Shared Electric Vehicles

- Year/journal: 2024 / Information Systems Research
- Logic: 为解决SEV车队在租赁与电力市场间实时分配电池资源的问题，文章开发了FleetPower决策支持系统，利用机器学习预测和市场投标动态配置车辆；基于三城市真实数据的仿真表明，相比仅租赁策略，它可将车辆利用率提升233%-700%，并在不同城市实现1.8%-4.4%的毛利增长。
- Objective family: economic_and_welfare
- Context: logistics_transport_supply_chain_and_manufacturing
- Tags: 共享电动汽车车队, 虚拟电厂, 电力平衡市场, 实时多产品资源分配

## data_knowledge_representation_and_integration (12)

### Automated discovery of business process simulation models from event logs

- Year/journal: 2020 / Decision Support Systems
- Logic: 针对手工构建仿真模型耗时且已有自动方法不优化精度的问题，Simod 将事件日志转换为仿真模型并用 BPTD/ELS 度量模型精度，再用 TPE 超参数优化搜索配置，实验表明优化后的模型在三个日志上的 ELS 显著高于默认基线。
- Objective family: analytic_quality
- Context: general_or_cross_domain
- Tags: 流程仿真模型自动发现, 事件日志, 超参数优化, BPTD相似度

### Cybersecurity vulnerability management: A conceptual ontology and cyber intelligence alert system

- Year/journal: 2020 / Information & Management
- Logic: 针对漏洞信息多源分散且普通用户缺少预警渠道的问题，本文设计整合NIST、CERT/CC、CVSS和Twitter知识的CVO本体，并据此构建基于SWRL规则生成漏洞警报的CIA系统；以推文分类准确率和警报准确率为核心指标，结果显示集成学习分类F1多在0.96以上、警报准确率达95%，验证了多源本体化漏洞预警方案的可行性。
- Objective family: analytic_quality
- Context: cybersecurity_fraud_and_compliance
- Tags: 漏洞本体, 多源漏洞情报整合, 社交媒体漏洞预警, SWRL规则推理

### X-IM Framework to Overcome  Semantic Heterogeneity Across XBRL Filings

- Year/journal: 2020 / Journal of the Association for Information Systems
- Logic: 针对XBRL filings中同一财务概念由不同XBRL元素表示造成的语义异构，文章设计X-IM框架，通过自动抓取EDGAR标签链接库构建索引本体，并利用基于索引的分类器将异构XBRL元素映射到投资者本体中的统一财务概念，实验以precision、recall和F-measure与FinCEM对比，显示映射精度显著提升。
- Objective family: analytic_quality
- Context: finance_accounting_and_investment
- Tags: XBRL语义异构, 本体映射, 标签链接库, 投资者本体

### Peak cubes in service operations: Bringing multidimensionality into decision support systems [theory subset]

- Year/journal: 2021 / Decision Support Systems
- Logic: 该文针对峰终定律只能处理单维服务水平的局限，设计了 peak cube 多维峰值表示并嵌入流失预测模型，在模拟物流客户数据上验证了多维峰值特征能显著提升客户流失预测的 AUROC。
- Objective family: analytic_quality
- Context: logistics_transport_supply_chain_and_manufacturing
- Tags: 多维峰值表示, 客户流失预测, 峰终定律, 物流服务运营

### Simpler is better: Lifting interpretability-performance trade-off via automated feature engineering

- Year/journal: 2021 / Decision Support Systems
- Logic: 本文针对黑箱模型不可解释的问题，提出SAFE ML框架，用复杂监督模型的PDP/ALE曲线和层次聚类自动生成可解释新特征并训练简单逻辑回归，在信用评分案例和30个OpenML任务上以AUC和参数数量评估，发现简单精炼模型能在不显著损失AUC的情况下大幅提高可解释性。
- Objective family: analytic_quality
- Context: general_or_cross_domain
- Tags: 自动特征工程, 可解释机器学习, 玻璃箱模型, PELT变点检测分箱

### Unveiling the Hidden Truth of Drug Addiction: A Social Media Approach Using Similarity Network-Based Deep Learning

- Year/journal: 2021 / Journal of Management Information Systems
- Logic: 针对药物论坛中因俚语变体导致难以自动提取OUD治疗障碍的问题，本文设计了融合词相似网络与多视角BLSTM的SINDEL系统，以F1为核心指标证明其显著优于现有基线，并通过聚类揭示13类治疗障碍。
- Objective family: analytic_quality
- Context: healthcare_and_care
- Tags: 阿片类药物使用障碍, 治疗障碍挖掘, 药名俚语变体, 社交媒体健康分析

### Multi-Party Certification on Blockchain and Its Impact in the Market for Lemons

- Year/journal: 2022 / Journal of Management Information Systems
- Logic: 针对柠檬市场信息不对称问题，文章以区块链多方认证 CarCerti 作为更高 fit 的信号机制，在实验性二手车市场 CarMarket 中对比有无多方认证的信息结构，发现多方认证显著降低要价和成交价、缩小买卖双方相对收益差距并提高优质车成交比例，从而实现更高效配置和更高市场公平。
- Objective family: economic_and_welfare
- Context: commerce_marketing_and_customer_service
- Tags: 区块链多方认证, 柠檬市场, 二手车信息不对称, 实验室市场实验

### OrdinoR: A framework for discovering, evaluating, and analyzing organizational models using event logs

- Year/journal: 2022 / Decision Support Systems
- Logic: 针对组织模型挖掘中案例/时间维度利用不足、资源组与过程执行脱节、缺乏基于日志的评估这三个问题，文章定义了关联执行模式的组织模型并实现 OrgMiner 挖掘与一致性检查框架；在 WABO 和 BPIC17 真实日志上用 fitness/precision/F1 比较方法组合，显示 trace clustering+OverallScore 取得最佳 F1（0.696/0.724），而 FullRecall 以极低 precision 换取完美 fitness。
- Objective family: analytic_quality
- Context: general_or_cross_domain
- Tags: 组织模型挖掘, 资源分组, 一致性检查, 事件日志

### Shedding light on blind spots – Developing a reference architecture to leverage video data for process mining

- Year/journal: 2022 / Decision Support Systems
- Logic: 针对流程挖掘无法覆盖手工活动盲点的问题，文章设计了 ViProMiRA 参考架构及其原型，用计算机视觉从 Crêpe 视频数据集自动抽取 XES 事件日志；在 12 个评估案例上达到 69.70% 召回率和 82.36% 精确率，并可用提取日志完成一致性检查（fitness 79.81%）和流程发现，证明该架构能系统化利用视频数据支持流程挖掘。
- Objective family: analytic_quality
- Context: general_or_cross_domain
- Tags: 视频流程挖掘, 参考架构, 事件日志抽取, 活动识别

### Cost-based analysis of the impact of data completeness and representational consistency

- Year/journal: 2023 / Decision Support Systems
- Logic: 文章从“fitness for use”视角提出基于任务成本的代价度量，通过在原始和改进后的PubMed-ORCID-GRID集成数据库上让218名受试者执行SQL任务，比较其解决率、解决时间和查询次数，发现数据质量改善的实际效果与规则测量预期不同，最高可减少约65%的解决时间。
- Objective family: human_task_performance
- Context: general_or_cross_domain
- Tags: 数据质量成本分析, 适用性视角, 数据集成与标识符一致性, SQL任务实验

### sDTM: A Supervised Bayesian Deep Topic Model for Text Analytics

- Year/journal: 2023 / Information Systems Research
- Logic: 针对无监督主题模型忽略文本辅助标签导致主题表示不准的问题，文章提出以主题注意力层连接NTM和GRU的监督式深度主题模型sDTM，并用困惑度、主题极性、下游回归显著性和预测准确率证明其相比LDA、NTM及深度基线能显著改善主题建模质量和预测表现。
- Objective family: analytic_quality
- Context: general_or_cross_domain
- Tags: 监督式深度主题模型, 主题注意力层, 辅助标签监督, Yelp与Stack Exchange实证

### Guided Diverse Concept Miner (GDCM): Uncovering Relevant Constructs for Managerial Insights from Text [theory subset]

- Year/journal: 2025 / Information Systems Research
- Logic: 针对无预设概念下从文本中挖掘管理相关概念的难题，作者设计GDCM，以共享嵌入空间、概念多样性正则和结局分类损失同时优化可解释性、多样性与相关性；在电商评论—转化数据上，GDCM在概念一致性、Garvin概念召回和转化预测AUC上优于主题模型基线，并复现了既有因果研究的系数方向。
- Objective family: analytic_quality
- Context: commerce_marketing_and_customer_service
- Tags: 文本概念挖掘, 可解释深度学习, 消费者评论与购买转化, 多样性正则化

## platform_mechanism_and_governance (12)

### Sustaining a Good Impression: Mechanisms for Selling Partitioned Impressions at Ad Exchanges

- Year/journal: 2020 / Information Systems Research
- Logic: 针对移动广告交易平台将整段展示机会只卖给单一广告主造成的分配低效，文章设计按时间片分割展示机会的OPT-IR与OPT-MB拍卖机制；以期望收入、广告主效用和社会福利衡量，与BASE和SEQ等机制比较后，发现两种机制都能提高交易平台收入，其中OPT-MB在保证广告主长期福利不下降的同时获得最高收入增益（异质场景33.60%），并达到一阶最优社会福利。
- Objective family: economic_and_welfare
- Context: commerce_marketing_and_customer_service
- Tags: 时间片分割展示机会, 广告交易平台拍卖机制, 随机化支付规则, 互惠机制

### Bringing transparency and trustworthiness to loot boxes with blockchain and smart contracts [theory subset]

- Year/journal: 2021 / Decision Support Systems
- Logic: 文章针对开箱不透明且不可验证的问题，设计了将开箱表示为以太坊智能合约的机制，通过公开概率和不可篡改的链上随机抽取建立信任，并以卡方检验证明抽取分布符合预期，同时评估了安全性和成本。
- Objective family: analytic_quality
- Context: commerce_marketing_and_customer_service
- Tags: 区块链, 智能合约, 开箱透明度, 以太坊

### Impact of Incentive Mechanism in Online Referral Programs: Evidence from Randomized Field Experiments [theory subset]

- Year/journal: 2021 / Journal of Management Information Systems
- Logic: 本文通过两个移动社交游戏的随机现场实验，操纵推荐奖励在邀请者和被邀请者之间的分配方式（自私/平分/慷慨），以转化邀请数、发送邀请数和接受概率为指标，发现亲社会型平分和慷慨奖励显著优于自私奖励，主要原因是提高了被邀请者的接受率并促使更有经验的用户进行更精准的推荐。
- Objective family: behavioral_response
- Context: commerce_marketing_and_customer_service
- Tags: 推荐奖励机制, 口碑传播, 随机现场实验, 移动社交游戏

### Designing Hybrid Mechanisms to Overcome Congestion in Sequential Dutch Auctions

- Year/journal: 2022 / MIS Quarterly
- Logic: 针对顺序荷兰式拍卖中同一价格点的多个出价无法同时成交所导致的拥堵，文章设计了一种将同一最高价出价批量成交并随机分配的混合拍卖机制；通过博弈论模型和荷兰花卉拍卖市场的准自然现场实验验证，该机制在不降低收入/分配效率的同时显著减少拍卖轮数并提高价格稳定性。
- Objective family: operational_efficiency
- Context: commerce_marketing_and_customer_service
- Tags: 顺序荷兰式拍卖, 混合拍卖机制, 市场拥堵缓解, 荷兰花卉拍卖现场实验

### Reciprocity or Self-Interest? Leveraging Digital Social Connections for Healthy Behavior [theory subset]

- Year/journal: 2022 / MIS Quarterly
- Logic: 通过在移动跑步社交平台上进行随机现场实验，设计朋友赠送金币并要求接收者完成挑战以回报朋友的互惠激励消息，与传统自利激励相比，互惠激励显著提高跑步挑战完成率和跑步距离，且其效果随社交亲密度呈倒U型变化。
- Objective family: behavioral_response
- Context: healthcare_and_care
- Tags: 互惠激励, 社交亲密度, 跑步挑战, 健康行为

### Socialize More, Pay Less: Randomized Field Experiments on Social Pricing [theory subset]

- Year/journal: 2022 / Information Systems Research
- Logic: 针对社会定价对存量消费者是否有效的问题，文章在线上生鲜零售商处设计并实施‘邀请好友砍价获折扣’的社会砍价功能，通过随机现场实验以销售额、利润、购买频率和订单金额为指标与常规定价及固定折扣比较，发现社会砍价显著提升零售商利润，且要求砍价者购买频率更高的异质性互动规则能进一步增强效果。
- Objective family: economic_and_welfare
- Context: commerce_marketing_and_customer_service
- Tags: 社会砍价, 社会资本定价, 存量消费者复购, 异质性互动规则

### The Secret to Finding a Match: A Field Experiment on Choice Capacity Design in an Online Dating Platform [theory subset]

- Year/journal: 2022 / Information Systems Research
- Logic: 本文通过在约会平台上随机改变每天可查看和选择的候选人数（选择容量）并进行隔离分组实验，发现提高男性选择容量最大化参与（选择次数），提高女性选择容量因女性受competition effect驱使而更不挑剔，从而最大化匹配（聊天次数），为选择容量设计提供了因果证据。
- Objective family: behavioral_response
- Context: digital_platform_social_media_and_crowdfunding
- Tags: 选择容量设计, 在线约会平台, 双边市场机制, 性别差异选择行为

### Optional Verification and Signaling in Online Matching Markets: Evidence from a Randomized Field Experiment

- Year/journal: 2023 / Information Systems Research
- Logic: 针对在线约会平台缺乏可信信息机制的问题，本文通过随机田野实验引入可选手机号验证徽章作为信号机制，比较付费/免费验证与控制组，发现男女用户因已有主导信号可靠性不同而呈现不同的验证选择模式，且验证显著增加了用户的消息与匹配行为。
- Objective family: behavioral_response
- Context: digital_platform_social_media_and_crowdfunding
- Tags: 可选手机号验证, 信号传递, 在线约会匹配, 随机田野实验

### Digital Institutionalization: The Case of E-Prescribing [theory subset]

- Year/journal: 2024 / Journal of the Association for Information Systems
- Logic: 为解决数字基础设施设计缺乏制度合法性的问题，文章设计了一个将制度规则编码为XML自动校验的电子处方交换契约（NEF），把错误控制从配药端移到处方创建端；实施前后连续样本对比显示含错误处方集比例从98.6%降到0.9%，从而说明数字基础设施可通过有意制度设计促成数字制度化。
- Objective family: analytic_quality
- Context: healthcare_and_care
- Tags: 电子处方, 交换契约, 自动校验, 数字化制度化

### Real-Effort Incentives in Online Labor Markets: Punishments and Rewards for Individuals and Groups

- Year/journal: 2024 / MIS Quarterly
- Logic: 针对在线劳动市场协作标注中的免费搭车问题，文章在图像标注平台中设计了基于收益乘数调整的外生奖励/惩罚机制（个人/群体两个层级），以每人每轮标签数为客观指标比较干预前后，发现群体层面的全部奖励和全部惩罚均能显著提高努力，且惩罚最差个人还产生了非预期的激励效果。
- Objective family: behavioral_response
- Context: digital_platform_social_media_and_crowdfunding
- Tags: 在线劳动市场, 免费搭车, 协作图像标注, 奖励与惩罚机制

### Algorithms to the Rescue: Market Mechanisms for Consensual Trading of Unbiased Individual Data

- Year/journal: 2025 / Information Systems Research
- Logic: 针对数据中介平台无法低成本获得无偏个人数据的问题，文章设计了一个由第二补偿拍卖与随机滚动配对抽样组成、激励相容且个体理性的市场机制（RSP），用偏差、总补偿/总成本等指标与固定补偿和集中优化比较，证明其能达到接近最优基准SRS的零偏差和近最优补偿成本，并在模拟和真实数据上优于现行方法。
- Objective family: multi_objective_or_tradeoff
- Context: digital_platform_social_media_and_crowdfunding
- Tags: 个人数据市场, 激励相容拍卖, 无偏抽样, 隐私补偿

### Toward Sustainable Electricity Markets: Capacity-Based Pricing for Electric Vehicle Smart Charging

- Year/journal: 2026 / Information Systems Research
- Logic: 为缓解EV充电引发的电网雪崩效应和峰值问题，文章设计容量定价及其价格设定启发式，用多智能体仿真证明该方法能把EV充电需求塑造成平坦、互补或跟随光伏的曲线，并在RMSE/PAPR/峰值和目标收入上显著优于平电价、时变电价和递增阶梯电价基准。
- Objective family: operational_efficiency
- Context: other_context
- Tags: 容量定价, 电动汽车充电协调, 电网负荷整形, 可再生能源消纳

## other_software_function (1)

### A method for resolving organisation‐enterprise system misfits: An action research study in a pluralistic organisation [theory subset]

- Year/journal: 2023 / Information Systems Journal
- Logic: 针对医院 EHR 与新生儿听力筛查流程之间的组织-系统失配，文章以用户感知为起点、以 affordance 实际化视角和参与式会议为核心提出并应用诊断与解决方法，实施 EHR 与流程调整，结果使数据完整性从 68% 升至 90% 以上、ORL 随访率从 54% 升至 78%，证明该方法可行有效。
- Objective family: substantive_domain_outcome
- Context: healthcare_and_care
- Tags: 新生儿听力筛查, 组织-企业系统失配, EHR流程与配置调整, 参与式诊断方法

## security_privacy_and_access_control (1)

### RADAR: A Framework for Developing Adversarially Robust Cyber Defense AI Agents with Deep Reinforcement Learning [theory subset]

- Year/journal: 2025 / MIS Quarterly
- Logic: 针对AI恶意软件检测器易被对抗样本绕过的问题，本文用r-VAC生成离散动作序列的对抗恶意软件，再用RL-RO将这些攻击样本纳入鲁棒优化目标来鲁棒化检测器，实验显示平均逃逸率下降约84%、鲁棒性提升约7倍。
- Objective family: risk_security_and_safety
- Context: cybersecurity_fraud_and_compliance
- Tags: 对抗恶意软件样本生成, 检测器鲁棒化, 二值黑盒攻击仿真, 重复攻防博弈

## workflow_automation_and_coordination (0)
