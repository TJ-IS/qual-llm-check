# Exclusive objective-metric improvement with explicit benchmark statements and public datasets

Completed: 2475 / 2475
Retained: 51

## Fraudulent review detection model focusing on emotional expressions and explicit aspects: investigating the potential of feature engineering

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113728
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "精确率 (Precision)", "measurement_cn": "在Yelp欺诈评论检测数据集上，分类为欺诈的评论中真正欺诈的比例，通过5折交叉验证计算。", "objectivity_reason_cn": "基于欺诈/非欺诈的事实标签，由平台或既有标注决定，不依赖人的主观感受。"}, {"name_cn": "召回率 (Recall)", "measurement_cn": "在Yelp欺诈评论检测数据集上，实际欺诈评论中被正确识别的比例，通过5折交叉验证计算。", "objectivity_reason_cn": "基于欺诈/非欺诈的事实标签，可审计。"}, {"name_cn": "F1分数", "measurement_cn": "精确率与召回率的调和平均，用于平衡评估分类性能。", "objectivity_reason_cn": "由精确率和召回率计算得出，均为基于事实标签的客观指标。"}, {"name_cn": "AUC (Area Under the ROC Curve)", "measurement_cn": "ROC曲线下面积，反映分类器区分欺诈与非欺诈的能力。", "objectivity_reason_cn": "基于事实标签的排序性能，客观可计算。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: Yelp dataset (Rayana and Akoglu [51] collected from Yelp.com) | Yelp Open Dataset [57] | Amazon dataset [12,23] | UCI machine learning repository [54]
- Benchmark evaluation: 在主Yelp数据集上开发并评估检测模型，然后在亚马逊、Yelp Open和UCI数据集上验证M-SMOTE算法与特征工程的效果。所有基准数据集上的结果均与baseline（无预处理/不平衡数据）、SMOTE以及先前研究方法进行比较。
- Dataset status: named_public_dataset_central
- Named datasets: Yelp.com review dataset (collected by Rayana and Akoglu [51]) | Yelp Open Dataset [57] | Amazon review dataset [12,23] | UCI Machine Learning Repository datasets
- Dataset obtainability: Yelp数据集是知名的公开数据集，可通过Yelp Dataset Challenge或相关研究项目获取；Amazon数据集有GitHub公开链接（参考文献[12]）；UCI数据集公开免费下载。独立研究者可按论文引用的来源获取。
- Decision: 本文核心目标是提升欺诈性评论检测的客观性能指标（精确率、召回率、F1、AUC），这些指标基于欺诈/非欺诈的事实标签，完全客观。研究问题、假设、实验设计和贡献声明均围绕该目标展开，无其他并列核心目标。全文存在明确的benchmark表述：摘要明确使用'benchmarking datasets'，实验部分在Yelp、Amazon、UCI等公开基准数据集上进行了系统评价，并与多种baseline和先前研究进行了比较。这些基准评价是支撑其核心性能提升主张的关键证据。评价核心主张所用的主要数据（Yelp、Amazon、UCI）均为公开可获取的数据集，独立研究者可查证和获取。因此三个模块全部通过。
- Confidence: 0.98

## Process data properties matter: Introducing gated convolutional neural networks (GCNN) and key-value-predict attention networks (KVP) for next event prediction with deep learning

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113494
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "准确性（accuracy）", "measurement_cn": "10折交叉验证中验证集上预测的下一事件与事件日志中实际下一事件标签一致的比例；按公式(8)在one-vs-all混淆矩阵上计算。", "objectivity_reason_cn": "下一事件是事件日志中已记录的活动/事件类型，属于可核验的外部事实标签；评估不依赖人的感受、语义质量或价值判断。"}, {"name_cn": "精确率（precision，加权/宏/微）", "measurement_cn": "基于one-vs-all混淆矩阵按公式(9)-(11)计算。", "objectivity_reason_cn": "通过预测事件标签与真实事件标签的匹配计数得到，客观可核验。"}, {"name_cn": "召回率（recall，加权/宏/微）", "measurement_cn": "基于one-vs-all混淆矩阵按公式(12)-(14)计算。", "objectivity_reason_cn": "通过预测事件标签与真实事件标签的匹配计数得到，客观可核验。"}, {"name_cn": "F1分数（F1-score，加权/宏/微）", "measurement_cn": "基于精确率和召回率按公式(15)-(17)计算。", "objectivity_reason_cn": "由客观的分类计数计算得出，不涉及主观评价。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: BPI'11 (Hospital Log) | BPI'12 (含BPI'12Cmpl、BPI'12WCmpl、BPI'12A、BPI'12O子集) | BPI'13 (含BPI'13Incidents、BPI'13Problems、BPI'13Closed子集) | Helpdesk | EnvLog
- Benchmark evaluation: 在11个真实事件日志基准数据集及若干子集上，以10折交叉验证评价GCNN、KVP，并与自行复现的LSTM、SAE以及文献中的LSTM、SAE、RegPFA、MANN、CNN等结果比较；报告accuracy、precision、recall、F1-score。结果显示KVP和GCNN在44个metric-dataset组合中有34个超过先前方法，并在统计检验、过程数据属性分析等部分继续以这些基准数据为评价场地。
- Dataset status: named_public_dataset_central
- Named datasets: BPI'11 (Hospital Log) | BPI'12 | BPI'13 | Helpdesk | EnvLog
- Dataset obtainability: 所有核心评价数据集均为公开可获取的真实事件日志：BPI系列数据集通过4TU ResearchData/DOI公开下载；Helpdesk通过Mendeley Data公开下载；EnvLog通过4TU/DOI公开下载。参考文献中提供了完整的DOI和访问日期，独立研究者可按论文信息检索并获取。
- Decision: 客观指标：核心成功指标为下一事件预测的accuracy、precision、recall、F1等基于事件日志事实标签的客观分类指标，无主观构念。核心目标：论文唯一核心目标是提出GCNN和KVP并证明其在客观预测指标上优于现有方法；过程数据属性讨论和选择指导是辅助性分析而非并列核心贡献。Benchmark：全文多次明确使用“11 real-life benchmark datasets”及“benchmark approaches”，评价位于实验/结果部分，且通过表3与多个baseline/文献方法比较，直接支撑核心提升主张。数据集：BPI'11、BPI'12、BPI'13、Helpdesk、EnvLog均为公开可获取的真实事件日志数据集，核心结果表基于这些数据。因此三个模块全部通过，strict_include=true。
- Confidence: 0.98

## GASP: A Graph Augmentation-Based Approach for Sign Prediction of Ties in Social Networks

- Year/journal: 2025 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00941
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "符号预测准确率（Accuracy）", "measurement_cn": "在Epinions、Wikipedia RfA、Slashdot Zoo、Yeast GIN基准数据集及IMDb构建网络上，随机抽取60%-80%边作为已标记边，预测剩余未标记边的正负符号，与真实符号比较计算准确率；每个比例重复10次取平均。", "objectivity_reason_cn": "预测目标是网络边已存在的正/负符号这一外部事实标签，标签通过平台用户行为（信任/不信任、支持/反对、朋友/敌人、基因交互正负）确定，不依赖人类对质量、价值或感受的语义评判；准确率由预测标签与事实标签比对确定。"}, {"name_cn": "优化精度（Optimized Precision）", "measurement_cn": "在平衡网络上，对正类和负类分别计算精度并以调和方式汇总，衡量两类的综合正确率。", "objectivity_reason_cn": "由混淆矩阵中的真阳性、假阳性等计数计算，完全由事实标签与预测标签决定，无主观评价成分。"}, {"name_cn": "宏F1（Macro F1）", "measurement_cn": "在非平衡网络上，分别计算正类和负类的F1值后取平均，衡量两个类别的综合预测性能。", "objectivity_reason_cn": "F1由精确率和召回率计算，均基于事实标签与预测标签的计数，不涉及人类对质量、价值或感受的判断。"}, {"name_cn": "特异性与负预测值的几何均值（GM(S,N)）", "measurement_cn": "对少数类（负类或正类）计算特异性和负预测值的几何均值，衡量少数类符号的预测能力。", "objectivity_reason_cn": "由混淆矩阵计数计算，预测目标仍是外部事实标签（正/负边符号），构念不依赖人类语义评价。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: Epinions | Wikipedia Requests for Adminship (RfA) | Slashdot Zoo | Yeast Genetic Interaction Network (GIN)
- Benchmark evaluation: 在Epinions、Wikipedia RfA、Slashdot Zoo、Yeast GIN四个公开基准网络上，按60%-80%已标记边比例随机划分，比较GASP与NPECF、SRWR、ASiNE、DDRE在平衡网络上的Accuracy和Optimized Precision、在非平衡网络上的Macro F1和GM(S,N)；结果显示GASP在绝大多数设置下优于全部对比方法。
- Dataset status: named_public_dataset_central
- Named datasets: Epinions | Wikipedia Requests for Adminship (RfA) | Slashdot Zoo | Yeast Genetic Interaction Network (GIN)
- Dataset obtainability: Epinions、Wikipedia RfA、Slashdot Zoo是斯坦福SNAP项目公开发布的经典符号网络数据集，可通过snap.stanford.edu/data/公开下载；Yeast GIN来自BioGRID数据库（Stark et al., 2006），可通过BioGRID公开获取；作者还声明数据与GASP的R实现已在GitHub公开。独立研究者可凭论文信息检索并下载。
- Decision: 客观指标模块：核心目标是预测网络边符号（正/负），所有主要成功指标（Accuracy、Optimized Precision、Macro F1、GM(S,N)）均基于事实标签与预测标签的混淆矩阵计算，不依赖人类语义或感受评价；全文没有将主观量表作为成功标准。唯一核心目标：研究问题、设计目标、评价结构和贡献声明均围绕提升符号预测性能展开，DSR表述和设计准则属于呈现与延伸讨论，未形成并列核心目标。Benchmark模块：第5.1节明确以benchmarking表述在Epinions、Wikipedia RfA、Slashdot Zoo、Yeast GIN四个公开基准网络上的评价，且第5.4、5.5节与四个现有方法（NPECF、SRWR、ASiNE、DDRE）比较并报告性能提升，benchmark评价直接支撑核心提升主张。数据集模块：四个基准数据集均为公开可获取的经典符号网络数据集（SNAP、BioGRID），并声明数据集和R实现已在GitHub公开，核心结果表基于这些公开数据。三模块均通过，strict_include=true。
- Confidence: 0.97

## Modifying Transactional Databases to Hide Sensitive Association Rules

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2021.1033
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "修改后数据库的准确性（未被修改事务的比例）", "measurement_cn": "数据来源为模拟及真实事务数据库；计算公式为未修改事务数 / 总事务数，由程序直接统计得出", "objectivity_reason_cn": "该指标直接基于事务是否被修改的事实，不涉及人的感受、语义或价值判断，可通过确定性程序计算"}, {"name_cn": "被清洗的事务数（Number of transactions sanitized）", "measurement_cn": "在实验结果表中报告，由算法输出直接得到；数值是客观可观测的", "objectivity_reason_cn": "事务是否被清洗是事实判定，不依赖主观评价"}, {"name_cn": "求解时间（Solution time in seconds）", "measurement_cn": "运行算法时记录的时间，以秒为单位；由计算环境直接测量", "objectivity_reason_cn": "时间测量是客观技术指标，不依赖人的主观解释"}, {"name_cn": "产生虚假规则的数量和丢失规则的数量", "measurement_cn": "在清洗后数据库中重新挖掘关联规则，与原始数据库比较得到；数值基于确定性规则计算", "objectivity_reason_cn": "这些是基于规则匹配和计数的事实结果，不依赖主观判断"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: Verykios et al. (2004) algorithm 2.a | Verykios et al. (2004) algorithm 2.b | Telikani and Shahbahrami (2017)
- Benchmark evaluation: 在五个数据集（retail、bms-pos、10m、50m、100m）上，将所提出的最优线性化方法与三种文献基准算法进行比较，报告各方法可解出的问题数量、求解时间以及清洗的事务数，证明所提方法在可扩展性和解质量上有显著优势。
- Dataset status: named_public_dataset_central
- Named datasets: retail | bms-pos | synthetic data sets 10m, 50m, 100m (generated with IBM's synthetic data generator)
- Dataset obtainability: retail和bms-pos可从FIMI公开仓库直接下载（http://fimi.uantwerpen.be/data/）；合成数据可依据Agrawal and Srikant (1994)的公开合成数据生成器按论文中给出的参数生成（100,000个物品、平均交易长度10等），独立研究者可据此复现或生成类似数据。
- Decision: 文章以最大化清洗后数据库的准确性等客观指标为唯一核心目标和贡献，全文无主观构念作为成功标准；在实验部分明确使用三个文献基准算法进行对比，benchmark评价支持核心提升主张且有明确比较对象；评价所用数据包括公开可下载的retail、bms-pos数据集和由公开IBM生成器可复现的合成数据集，公开数据支撑主要结果表。因此三个模块全部通过，strict_include为true。
- Confidence: 0.97

## Post-Earnings-Announcement Drift Prediction: Leveraging Postevent Investor Responses with Multitask Learning

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2022.0358
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "预测精度（EV，explained variance）", "measurement_cn": "EV = 1 - Var(预测CAR(0,21)-实际CAR(0,21))/Var(实际CAR(0,21))，在52个滚动窗口测试集上平均；基于CRSP等股票价格数据计算CAR(0,21)。", "objectivity_reason_cn": "CAR(0,21)由实际股票收益减去基于C5模型估计的预期收益得到，完全基于可审计的市场价格和财务数据确定，不依赖任何人类感受或语义评价。"}, {"name_cn": "经济显著性（alpha）", "measurement_cn": "根据预测PEAD构建长期/多空投资组合，将组合日收益对Mkt/SMB/HML/RMW/CMA/UMD六个风险因子回归，截距项alpha即风险调整后日超额收益。", "objectivity_reason_cn": "组合收益与风险因子均来自公开市场价格和财务数据，alpha的计算是确定性财务计量，独立于人的体验和判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在Russell 3000及其子样本上，将提出的FinAux+GradPerp+MQT与SUE、OLS、PEAD.txt、bi-LSTM、Transformer等基准模型比较，报告EV（表7），显示所提模型取得9.06%的最高EV；同时通过消融分析（表8）和与其他自适应加权方法比较（表11）证明FinAux和GradPerp的贡献。
- Dataset status: named_public_dataset_central
- Named datasets: S&P Capital IQ Transcript database | CRSP | Compustat | I/B/E/S | Thomson/Refinitiv | RavenPack
- Dataset obtainability: 上述数据库均为金融学界广泛使用的标准商业订阅数据库，可通过WRDS等平台获取访问（如CRSP/Compustat/I/B/E/S/Thomson/Refinitiv/RavenPack），S&P Capital IQ亦有公开订购渠道；独立研究者通过学术机构订阅即可获取。
- Decision: 客观指标模块通过：核心成功指标为EV和alpha，均为客观市场可审计结果，且唯一核心目标是提升预测性能和经济收益，无主观构念并列。benchmark模块通过：全文在评价语境中明确使用benchmark一词，与多个基准模型比较，benchmark结果支撑核心提升主张，且有明确参照点。数据集模块通过：核心评价数据基于S&P Capital IQ、CRSP、Compustat、I/B/E/S、Thomson/Refinitiv、RavenPack等公开可获取的标准商业订阅数据库，核心结果表完全基于这些公开数据。因此 strict_include = true。
- Confidence: 0.97

## Shapley Value-Based Feature Attribution for Data Masking

- Year/journal: 2026 / MIS Quarterly
- DOI: 10.25300/misq/2025/18502
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "披露风险降低百分比 (%Δr)", "measurement_cn": "通过隐私推断模型 g 对机密特征 y 的预测值与真实值比较，使用 R²、AAD、RASD 等风险度量计算风险，并以相对基准方法的风险降低百分比表示", "objectivity_reason_cn": "该指标基于预测误差等可计算数值，不依赖人的感受或语义判断，完全由数据、模型和固定公式决定"}, {"name_cn": "数据效用保持/损失百分比 (%Δu)", "measurement_cn": "通过数据效用模型 h 对目标特征 z 的预测值与真实值比较，使用 R²、AAD、RASD 等效用度量计算，并以相对基准方法的效用损失百分比表示", "objectivity_reason_cn": "该指标同样是基于预测误差的客观计算，不涉及人类主观评价"}, {"name_cn": "建模度量 (R²、AAD、RASD)", "measurement_cn": "分别对披露风险和效用应用这些度量，公式明确且基于真实值与预测值的差异", "objectivity_reason_cn": "这些度量是信息检索和统计建模中的标准客观评价指标，完全可复现"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在三个真实数据集（Credit、Salary、Compustat）上，将所有组合（4种掩蔽方法 × 2种模型 × 3种度量）下所提方法（risk-only 与 weighted-cost）与两个基准方法进行系统比较，表格（Table 5a-c）报告了风险降低和效用损失百分比，显示所提方法在风险降低方面优于或持平于基准方法，同时效用损失较小或持平。
- Dataset status: named_public_dataset_central
- Named datasets: Credit History (UCI Machine Learning Repository, Hofmann 1994) | MIS Faculty Salary Offers (AIS annual survey, Galletta 2004) | CRSP/Compustat Merged (CCM) database
- Dataset obtainability: UCI Credit History 可在 UCI Machine Learning Repository 免费下载；MIS Faculty Salary Offers 数据集可从公开的 Galletta 网页获取（sites.pitt.edu/~galletta/salsurv.html）；CRSP/Compustat 是学术界广泛使用的商业订阅数据库，可通过标准订阅渠道获取。三者均可被独立研究者查证和获取。
- Decision: 核心目标完全是提升客观的披露风险降低和数据效用保持指标，没有任何主观构念作为成功标准；全文在实验评价语境中明确使用 benchmark methods，并与两个显式基准比较；核心实验结果完全基于 UCI、MIS Salary Survey、CRSP/Compustat 等公开可获取数据集。因此三个模块全部通过，strict_include=true。
- Confidence: 0.97

## A Graph-Based Ant Algorithm for the Winner Determination Problem in Combinatorial Auctions

- Year/journal: 2021 / Information Systems Research
- DOI: 10.1287/isre.2021.1031
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "求解质量（solution quality）", "measurement_cn": "算法得到的胜者集合总价与已知最优解的百分比差距，或达到最优解/98%最优解的情况", "objectivity_reason_cn": "由算法计算结果与基准最优解的数值差决定，不依赖人的主观评价"}, {"name_cn": "计算时间（runtime）", "measurement_cn": "以秒计完成指定迭代或达到最优/近最优解的时间", "objectivity_reason_cn": "计算机可复现的运行时间，客观可测"}, {"name_cn": "改进解概率（ISP）", "measurement_cn": "TrACA生成解大于等于对照启发式结果的频率", "objectivity_reason_cn": "基于数值比较的频率统计，客观可计算"}, {"name_cn": "Z分数", "measurement_cn": "对照启发式结果相对TrACA解分布的标准差度量", "objectivity_reason_cn": "基于数值分布的统计量，客观可计算"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: Lau and Goh (2002) test instances | Combinatorial Auction Test Suite (Leyton-Brown et al. 2002)
- Benchmark evaluation: 在94个Lau and Goh (2002)公开测试实例上运行TrACA，并与20种现有启发式（如MA、BHS、DDCM、ACLS、SHH、GA、DE、BRKGA等）以及CPLEX和Max W Clique两种精确算法进行系统比较。通过中位数检验、ISP、Z分数和平均解质量提升等客观指标报告结果。
- Dataset status: named_public_dataset_central
- Named datasets: Lau and Goh (2002) test instances | Combinatorial Auction Test Suite (Leyton-Brown et al. 2002)
- Dataset obtainability: 论文明确称这些测试实例为‘open test instances’。Lau and Goh (2002)实例在WDP文献中被广泛使用，是公开的标准测试集；CATS也是公开可获取的组合拍卖测试套件。独立研究者可通过原始论文及公开渠道（如CATS官网和相关研究者页面）获取这些实例。
- Decision: 本文提出一种求解组合拍卖胜者确定问题（WDP）的蚁群算法TrACA，核心目标是在短时限内提高WDP求解质量和速度。核心指标为求解质量（相对最优解的百分比）、运行时间、达到最优的时间、统计比较指标（ISP、Z分数等），全部客观、可计算、不依赖人的主观评价。研究问题、实验设计和贡献声明均围绕该算法在公开测试实例上的性能提升展开，没有并列的主观或理论核心目标。论文在实验部分明确使用公开测试实例（Lau and Goh 2002和CATS），以‘benchmark heuristics’为对照，并与20种现有启发式和CPLEX、Max W Clique等精确算法进行系统比较；这些比较直接支撑核心提升主张。数据来源为公开可获取的标准测试实例，核心结果表均基于这些数据。因此三个模块全部通过，strict_include为true。
- Confidence: 0.96

## Exploiting Expert Knowledge for Assigning Firms to Industries: A Novel Deep Learning Method

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/17171
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "分类准确率（Accuracy）", "measurement_cn": "比较模型预测的 NAICS/GICS 行业代码与 Compustat COMPHIST 记录的真实行业代码，计算正确分类比例。", "objectivity_reason_cn": "行业代码是依据公开行业分类系统（NAICS/GICS）定义的事实性标签，可通过记录准确核对，不依赖人的感受或语义评价。"}, {"name_cn": "宏平均F1（Macro-F1）", "measurement_cn": "基于每个行业的精确率、召回率计算F1，再对全部行业取平均。", "objectivity_reason_cn": "由既定行业标签的预测与真实值计算得出，属于客观分类性能指标。"}, {"name_cn": "误分类成本（Misclassification Cost）", "measurement_cn": "根据真实行业与预测行业的有效税率差异乘以应纳税所得额计算平均税收差异。", "objectivity_reason_cn": "基于外部公开税率数据和公司财务数据计算，是可审计的货币化客观成本。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: NAICS 2012 | GICS 2016
- Benchmark evaluation: 在NAICS和GICS两个公开行业分类任务上，用2012-2015年数据训练、2016年新企业分类测试，对DeepIA与SVM-IA、MLP-IA、ULMFiT-IA、HC-IA、LE-IA等基线/现有方法进行系统比较；主要结果报告准确率和宏F1，并给出DeepIA相对最优基线的提升百分比及显著性检验。
- Dataset status: named_public_dataset_central
- Named datasets: Compustat Company Header History (COMPHIST) via WRDS | Stage One 10-X Parse data (Loughran-McDonald)
- Dataset obtainability: Compustat/COMPHIST通过WRDS提供，属于学术界普遍可获取的商业订阅数据库，有公开订购渠道；Stage One 10-X Parse data由Loughran-McDonald公开提供，可在线获取。分类体系NAICS、GICS为公开标准，行业定义和结构都可公开查证。
- Decision: 客观指标方面，核心成功指标是行业分类准确率、宏F1和误分类成本，均由既定行业标签和公开财务/税务数据客观计算，不涉及人类感知或语义评价；唯一核心目标是提升行业分类性能，方法创新是手段而非并列核心贡献。Benchmark方面，作者在实验部分明确使用“benchmark”一词，将DeepIA与SVM-IA、MLP-IA、ULMFiT-IA、HC-IA、LE-IA等基线/现有方法进行系统比较，并报告相对提升百分比的显著性检验，构成核心证据。数据集方面，核心评价基于公开可获取的Compustat/COMPHIST（WRDS订阅）和Loughran-McDonald 10-X Parse数据，数据集可识别、可查证、可获取，且主要结果表均基于这些公开数据。三个模块均通过，因此strict_include为true。
- Confidence: 0.96

## A deep learning approach for detecting fake reviewers: Exploiting reviewing behavior and textual information

- Year/journal: 2023 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113911
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "Accuracy (准确率)", "measurement_cn": "5折交叉验证，正确预测的样本数占总样本数比例", "objectivity_reason_cn": "基于分类结果与Yelp标签比较，可自动计算，不依赖主观评价"}, {"name_cn": "Precision (精确率)", "measurement_cn": "TP/(TP+FP)，基于5折交叉验证", "objectivity_reason_cn": "基于分类结果与Yelp标签比较，可自动计算，不依赖主观评价"}, {"name_cn": "Recall (召回率)", "measurement_cn": "TP/(TP+FN)，基于5折交叉验证", "objectivity_reason_cn": "基于分类结果与Yelp标签比较，可自动计算，不依赖主观评价"}, {"name_cn": "F1-score", "measurement_cn": "2*P*R/(P+R)，基于5折交叉验证", "objectivity_reason_cn": "基于分类结果与Yelp标签比较，可自动计算，不依赖主观评价"}, {"name_cn": "AUC (Area Under the Curve)", "measurement_cn": "ROC曲线下面积，基于5折交叉验证", "objectivity_reason_cn": "基于分类结果与Yelp标签比较，可自动计算，不依赖主观评价"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在YelpZIP和YelpNYC两个真实数据集上，通过两个实验（仅行为特征、全特征）将所提行为敏感特征提取器和完整框架与多个基准方法比较，报告Accuracy、Precision、Recall、F1、AUC，并做了配对t检验；结果表显示所提模型显著优于各基准。
- Dataset status: named_public_dataset_central
- Named datasets: YelpZIP | YelpNYC
- Dataset obtainability: YelpZIP和YelpNYC是Yelp公开数据集的子集，由Rayana和Akoglu在KDD 2015论文中分享，并已在多篇论文中使用。独立研究者可通过Yelp Dataset Challenge或Rayana和Akoglu的研究页面获取；也可从公开学术资源库搜索到。
- Decision: 客观指标：本文以fake reviewer检测的Accuracy、Precision、Recall、F1、AUC为唯一核心结果指标，标签为Yelp平台判定的伪评论者事实标签，不涉及主观构念。唯一核心目标：研究问题、实验设计和贡献声明均围绕提升检测性能，除客观指标提升外没有并列的核心目标。Benchmark：作者在摘要和实验设计中明确以'benchmarks'指称并与多个基准方法比较，benchmark结果（Table 4/7）是核心证据，且比较有明确参照点。数据集：核心评价使用公开的YelpZIP和YelpNYC数据集，可公开获取，并支撑核心提升主张。因此三个模块全部通过，strict_include=true。
- Confidence: 0.95

## A novel federated learning approach with knowledge transfer for credit scoring

- Year/journal: 2024 / Decision Support Systems
- DOI: 10.1016/j.dss.2023.114084
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "Accuracy", "measurement_cn": "测试集上正确分类样本数占总样本数的比例，由模型预测与真实违约标签比较计算", "objectivity_reason_cn": "基于固定的事实标签（违约/非违约）和模型输出计算，不依赖人的感受或语义评价"}, {"name_cn": "Recall", "measurement_cn": "测试集上正确识别的违约样本数占真实违约样本数的比例", "objectivity_reason_cn": "基于固定的事实标签和确定性分类结果计算"}, {"name_cn": "F1-score", "measurement_cn": "精确率和召回率的调和平均数", "objectivity_reason_cn": "由精确率和召回率两个客观分类指标计算"}, {"name_cn": "KS", "measurement_cn": "累计违约分布与累计非违约分布的最大差异", "objectivity_reason_cn": "基于预测违约概率分布和真实标签计算，完全客观"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: FedAvg | FedProx | FedCodl | LR | RF | XGBoost
- Benchmark evaluation: 在五个信用数据集上，将 FedKT 与 FedAvg、FedProx、FedCodl 三个基准联邦学习方法（以及非联邦 LR、RF、XGBoost）在 IID 和 Non-IID 两种数据划分下比较 Accuracy、Recall、F1-score、KS，给出表3-6、Fig.3-5以及Friedman检验。这些比较结果用于支撑 FedKT 性能提升的核心主张。
- Dataset status: named_public_dataset_central
- Named datasets: Loan Data | HMEQ | Taiwan | Give Me Some Credit (GMSC) | Home Credit (HC)
- Dataset obtainability: Taiwan 可从 UCI Machine Learning Repository 公开下载；GMSC 和 HC 分别是 Kaggle 上公开的信用评分竞赛数据集，可注册后下载。因此核心评价所涉五个数据集中至少三个是公开可获取的标准数据源。Loan Data 和 HMEQ 虽出处为专业书籍，但论文未提供直接下载渠道，不过不影响整体判断，因为主要结果表同时包含公开数据，且公开数据是支撑核心主张的关键组成部分。
- Decision: 客观指标：核心指标为 Accuracy、Recall、F1-score、KS，基于违约/非违约这一事实标签计算，完全客观，不涉及主观评价。唯一核心目标：研究问题、方法设计和贡献声明均围绕提升信用评分模型性能，无主观量表或并列核心目标。Benchmark：全文在引言和实验部分明确使用 'benchmark' 一词，5.2节将 FedAvg、FedProx、FedCodl 称为 benchmark federated methods，并与 FedKT 在全表和Friedman检验中比较，具有明确参照点，benchmark 结果直接支撑核心提升主张。数据集：核心评价使用了五个信用数据集，其中 Taiwan 明确来自 UCI，GMSC 和 HC 明确来自 Kaggle，均为公开可获取的标准数据源；这些公开数据出现在核心结果表中，是支撑核心主张的关键组成部分。因此三个模块全部通过，strict_include=true。
- Confidence: 0.95

## Assessing and Enhancing Adversarial Robustness of Predictive Analytics: An Empirically Tested Design Framework

- Year/journal: 2022 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2022.2063549
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "对抗鲁棒性性能比率（Performance Ratio）", "measurement_cn": "在给定扰动范围内，模型在混合对抗样本测试集上的accuracy、precision、recall、F1、ROC分别除以非对抗测试集上的对应指标，得到RA、RP、RR、RF、RROC。", "objectivity_reason_cn": "基于垃圾评论/垃圾邮件的客观真实标签与模型预测结果计算，不依赖主观感受或语义评价。"}, {"name_cn": "性能-扰动曲线下面积（A/P AUC, P/P AUC, R/P AUC, F/P AUC, ROC/P AUC）", "measurement_cn": "在不同扰动范围（0到1）下计算模型在混合测试集上的各类分类性能，并计算曲线下面积。", "objectivity_reason_cn": "由客观分类性能指标随扰动范围变化而汇总得到，所有数值均可从确定性公式和标签计算，无主观成分。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在垃圾评论检测和垃圾邮件检测两个测试床上，将ARText系统（集成学习+对抗重训练）与NB、RF、SVM、CNN、GRU、BiGRU、LR、LSTM、BiLSTM等基准模型进行系统比较，采用性能比率和性能-扰动曲线下面积两个鲁棒性指标体系。Evaluation 3和Evaluation 4分别验证集成学习和对抗重训练带来的鲁棒性提升，所有主要结果均与baseline对比。
- Dataset status: named_public_dataset_central
- Named datasets: Deceptive Opinion Spam dataset (Ott et al., 2013) | Apache SpamAssassin public corpus
- Dataset obtainability: Spam review数据集来自Ott et al. (2013)的公开研究数据集（可通过文献引用找到作者公开页面下载）；垃圾邮件数据集来自Apache SpamAssassin公共语料库，文中脚注给出直接URL，任何研究者均可公开下载。两个数据集均免费公开获取。
- Decision: 客观指标方面：核心结果指标为对抗鲁棒性度量（性能比率、性能-扰动曲线下面积），基于垃圾评论/垃圾邮件这一客观事实标签计算，不依赖主观评价，完全客观。唯一核心目标：研究问题、设计目标、评价和贡献均围绕提升对抗鲁棒性这一客观指标展开，理论仅用于指导设计，无并列核心目标，属于exclusive_objective_improvement。Benchmark方面：摘要明确说明在垃圾评论检测和垃圾邮件检测两个任务上与benchmark methods比较，实验部分系统性对比多个baseline模型，benchmark结果直接支撑ARText的鲁棒性提升主张，满足显式benchmark表述、评价语境、支撑核心主张、有明确参照点四个门槛。数据集方面：两个核心数据集均为公开数据集——Ott et al. (2013)的虚假评论数据集可通过引用获取，SpamAssassin公共语料库在脚注中给出URL，均为免费公开下载；所有核心实验结果（Table 3-8）均基于这两个数据集，因此公开数据支撑核心主张。三个模块全部通过，故strict_include=true。
- Confidence: 0.95

## Developing a Composite Measure to Represent Information Flows in Networks: Evidence from a Stock Market

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2021.1066
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "预测误差 (RMSE/MAE/MAPE)", "measurement_cn": "在2017年holdout样本上，用多种线性与非线性预测模型预测股票异常收益的方向和幅度，计算均方根误差、平均绝对误差和平均绝对百分比误差。", "objectivity_reason_cn": "股票异常收益和预测误差均为可审计的金融市场事实，不依赖人类感受、意义或价值判断，可由市场价格和公开财务数据确定。"}, {"name_cn": "投资组合超额收益 (Alpha)", "measurement_cn": "基于EAC和sentiment的trading strategy，用Fama-French风险因子回归估计的截距alpha衡量超额收益。", "objectivity_reason_cn": "组合收益和因子回归Alpha是客观市场数据计算所得，反映经济意义上的预测提升，不涉及主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在2017年holdout样本上，用Fama-MacBeth、SVR、MLP、决策树、随机森林、GBDT等方法，将EAC模型与不含EAC的基准模型及degree、closeness、betweenness、PageRank等替代指标逐一对比，报告RMSE/MAE/MAPE并采用bootstrap置信区间验证差异显著性。
- Dataset status: publicly_described_source_central
- Named datasets: Sina Finance coattention data | CSMAR (China Stock Market & Accounting Research) | CNRDS / eastmoney.com forum data
- Dataset obtainability: Sina Finance为公开金融门户网站，研究者可公开访问并爬取各股票当日的coattention列表；CSMAR是公开商业订阅数据库，可通过机构订购获取；CNRDS平台同样提供公开订阅或机构访问渠道，包含eastmoney论坛数据。核心预测评价表（如Table 2-7）均基于这些公开来源构建的数据。
- Decision: 本文以提升股票异常收益预测精度为唯一核心目标，核心指标（RMSE/MAE/MAPE、Alpha）均为客观可审计金融结果，不涉及主观构念。全文在评价语境中明确使用'benchmark'一词，系统比较了EAC与无EAC基准模型及多种替代网络指标，并以显式参照点证明提升。所有核心评价数据来自Sina Finance公开网站、CSMAR和CNRDS等公开/订阅可获取的数据源，且主要结果表均基于这些公开数据。因此三个模块全部通过，strict_include=true。
- Confidence: 0.95

## Discovering event episodes from sequences of online news articles: A timeadjoining frequent itemset-based clustering method

- Year/journal: 2020 / Information & Management
- DOI: 10.1016/i.im.2020.103348
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "聚类召回率（Cluster Recall）", "measurement_cn": "以事件语料中的真实 episode 标签为基准，比较生成簇与真实 episode 的文档关联对；CR = |CA| / |TA|，其中 CA 为同时出现在真实和生成 episode 中的文档关联对，TA 为真实 episode 中的文档关联对。", "objectivity_reason_cn": "由离散的文档-episode 标签和聚类结果计算，不涉及人的体验、语义价值或偏好，可由确定性公式计算。"}, {"name_cn": "聚类精确率（Cluster Precision）", "measurement_cn": "CP = |CA| / |GA|，其中 GA 为生成 episode 中的文档关联对。", "objectivity_reason_cn": "同样由离散标签和聚类结果计算，客观可审计。"}, {"name_cn": "F-measure", "measurement_cn": "综合聚类召回率和聚类精确率的调和平均，F = 2*CR*CP / (CR + CP)。", "objectivity_reason_cn": "由客观的召回率和精确率计算，无主观判断成分。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: TDT2 | TDT3
- Benchmark evaluation: 在 Nallapati et al. 的事件语料（来自 TDT2/TDT3，含 53 个事件、248 个 episode、1468 篇新闻）上评价 TAFIED，并与 FIHC、HAC、HAC+TD 等基准方法比较。使用 PRT 曲线、最佳 F-measure 及 Wilcoxon 检验；TAFIED 的 F-measure 为 0.584，优于 FIHC 的 0.543、HAC 的 0.533、HAC+TD 的 0.567，且差异显著。
- Dataset status: named_public_dataset_central
- Named datasets: TDT2 | TDT3 | Nallapati et al. event corpus（基于 TDT2/TDT3 构建）
- Dataset obtainability: TDT2 和 TDT3 是公开的 Topic Detection and Tracking 标准语料，可通过 LDC/NIST 等公开渠道订购获取。论文明确给出事件语料来自 Nallapati et al. [17]，且该语料构建自公开的 TDT2/TDT3；独立研究者可以依据论文信息检索和获取这些公开语料。
- Decision: 核心目标完全客观：全文以 cluster recall、cluster precision、F-measure 作为唯一核心成功指标，评价 TAFIED 方法在事件 episode 发现上的性能提升；没有主观量表或并列核心贡献。全文存在明确的 benchmark 表述，摘要和第4.2节均将 FIHC、HAC、HAC+TD 称为 benchmarks，并在评价语境中用这些基准方法作为参照，比较结果直接支撑核心提升主张。数据来源清晰：使用 Nallapati et al. 的事件语料，其源自公开的 TDT2/TDT3 语料，可公开获取，且核心结果表基于该数据。三个模块均通过，故 strict_include=true。
- Confidence: 0.95

## Diversity Preference-Aware Link Recommendation for Online Social Networks

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1174
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "多样性偏好匹配得分（DPMS）", "measurement_cn": "用户多样性偏好向量（由用户现有好友在各画像维度取值上的计数构成）与推荐好友多样性分布向量之间的余弦相似度，再对H个画像维度取均值。", "objectivity_reason_cn": "由用户档案和推荐结果的确定性分布计算，不依赖任何人的感受、偏好评价或语义判断；任何研究者用同一数据和规则可复现。"}, {"name_cn": "Precision（精确率）", "measurement_cn": "推荐给用户的k个好友中，在下一时间窗口实际成为用户好友的比例（TP/k）。", "objectivity_reason_cn": "基于真实链接形成事实，是可审计的外部事件，不依赖主观评价。"}, {"name_cn": "Recall（召回率）", "measurement_cn": "用户下一时间窗口新增好友中，被推荐算法命中并出现在推荐集合中的比例（TP/P）。", "objectivity_reason_cn": "基于真实链接形成事实。"}, {"name_cn": "F1 score", "measurement_cn": "Precision和Recall的调和平均：2×Precision×Recall/(Precision+Recall)。", "objectivity_reason_cn": "由Precision和Recall两个客观指标计算得到。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在公开的Google+数据集上，将DPA-LR与MMR、MSD、DPP、DiRec四种代表性多样化方法以及GCN-LR、GraphSage-LR、GAT-LR三种state-of-the-art链接推荐方法进行系统比较；主要结果表（表5、表6、表7、表9）显示DPA-LR在DPMS、Precision、Recall、F1上全面优于所有对照方法，且统计显著性p<0.001。
- Dataset status: named_public_dataset_central
- Named datasets: Google+ dataset (Gong et al., 2012)
- Dataset obtainability: 独立研究者可通过论文给出的URL公开免费下载Google+数据集；该数据集还附有公开发表的论文（Gong et al., 2012）作为出处，可查证、可复现。
- Decision: 该文的全部核心成功指标均为客观可审计结果：DPMS由用户档案分布确定性计算，Precision/Recall/F1基于真实链接形成事实；没有任何主观量表、专家评分或基于人类语义判断的结果，也没有理论机制或组织变革等并列核心目标。文章在实证评价部分明确使用benchmarking表述，将所提方法与MMR、MSD、DPP、DiRec等多样化方法及GCN-LR、GraphSage-LR、GAT-LR等SOTA链接推荐方法在多张主要结果表上进行系统比较，证明DPMS和准确率的显著提升，并报告p<0.001。支撑核心提升主张的主要结果表全部基于公开可下载的Google+数据集，论文给出了明确数据来源和下载URL；虽然次要附录使用了未命名的美国社交网络数据，但该私有数据不承担核心结果表的证据功能。因此三个模块全部通过，strict_include=true。
- Confidence: 0.95

## Extracting Actionable Insights from Text Data: A Stable Topic Model Approach

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/16957
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "模型稳定性指标（S_doc_prob、S_doc_label、S_topic_prob、S_topic_topwords）", "measurement_cn": "对同一数据集重复训练两个主题模型，经 Hungarian 对齐后计算文档-主题分布和主题-词分布的 L1 距离或共享 top 词比例；这些概率和标签来自模型输出，数值确定。", "objectivity_reason_cn": "指标计算只依赖主题模型的概率分布与标签分配，不涉及任何人类感受、语义价值判断或主观评价。"}, {"name_cn": "模型质量指标（Perplexity、C_v、C_uci）", "measurement_cn": "Perplexity 基于模型对数似然计算；C_v 和 C_uci 基于词在滑动窗口中的 NPMI/PMI 共现统计计算。", "objectivity_reason_cn": "这些指标是可重复计算的统计量，不需要人类评分或语义评价，尽管 C_v 在设计时参考了与人类评分的相关性，但指标本身是客观数值。"}, {"name_cn": "下游计量经济分析的一致性（系数方向、p值、相关性）", "measurement_cn": "在 StackExchange 和 Amazon 数据上多次运行主题模型后，基于生成的变量做回归，比较系数符号、显著性以及变量跨运行 Pearson 相关。", "objectivity_reason_cn": "因变量是投票数和评分等外部事实，系数估计和 p 值是标准统计量，完全客观。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: LDA baseline | Doc LDA | Ensemble LDA | Granulated LDA | MRF-LDA | CRFTM
- Benchmark evaluation: 在 Amazon、Yelp、StackExchange、Company Description 四个数据集上，将 Stable LDA 与标准 LDA、Doc LDA、Ensemble LDA、Granulated LDA 等稳定性缓解方法进行系统比较，主要结果见表4（稳定性）和表5（模型质量）；附录F还比较了 MRF-LDA 和 CRFTM。结果显示 Stable LDA 在稳定性上显著提升，且不降低模型质量。
- Dataset status: named_public_dataset_central
- Named datasets: Amazon Product Review dataset (Ni et al., 2019) | Yelp Restaurant Review dataset | StackExchange Q&A dataset | Company Description dataset (Qader et al., 2018)
- Dataset obtainability: Amazon Product Review 数据由 Ni et al. (2019) 公开提供，可从 UCSD Amazon product data 页面下载；Yelp Restaurant Review 数据来自 Yelp Dataset Challenge 公开数据集（可申请获取）；StackExchange Q&A 数据可通过 Stack Exchange Data Explorer 或 Stack Exchange 公共转储公开下载；Company Description 数据来源于 Qader et al. (2018) 论文，该论文描述了从 Wikipedia 收集并可公开发布（可从论文补充材料或作者处获取）。独立研究者可查到并获取全部核心评价数据。
- Decision: 客观指标方面，核心成功指标均为可重复计算的统计量（稳定性、perplexity、coherence、回归系数一致性），不依赖人类主观评价；唯一核心目标是提出 Stable LDA 以提升主题模型稳定性，全文贡献均围绕该目标的评价与验证。Benchmark 方面，作者明确使用 benchmark 一词并在系统化比较中评估 Stable LDA 与 LDA、Doc LDA、Ensemble LDA、Granulated LDA 等方法，结果直接支撑核心稳定性提升主张且存在多个显式比较对象。数据集方面，Amazon、Yelp、StackExchange、Company Description 四个数据集均可在公开渠道获取，且核心结果表全部基于这些公开数据。因此三个模块全部通过。
- Confidence: 0.95

## Gaining a Seat at the Table: Enhancing the Attractiveness of Online Lending for Institutional Investors

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2022.0638
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "内部收益率 (IRR)", "measurement_cn": "根据贷款组合的现金流出（初始投资）和现金流入（每月还款、追偿等）计算使净现值为零的折现率；数据来源于LendingClub贷款的逐月现金流。", "objectivity_reason_cn": "IRR基于实际现金流计算，不依赖人的感受或语义判断，是可审计的财务事实。"}, {"name_cn": "投资回报率 (ROI)", "measurement_cn": "基于累计折现支付（CDP）与初始投资之比计算，公式见式(2)-(3)；也基于贷款现金流。", "objectivity_reason_cn": "ROI由贷款实际还款金额和时间计算，是确定性的财务指标。"}, {"name_cn": "公共市场等价 (PME)", "measurement_cn": "贷款组合IRR与基准指数组合IRR的比值，用于比较贷款和传统资产的相对吸引力。", "objectivity_reason_cn": "PME由两个客观IRR相除得到，反映投资绩效对比。"}, {"name_cn": "IRR相关性", "measurement_cn": "贷款组合IRR与市场指数IRR的相关系数，用于衡量分散化收益。", "objectivity_reason_cn": "相关系数由客观IRR序列计算，不涉及主观判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: Equal-weight portfolio | Risk filtering portfolio | Linear regression portfolio | Gradient-boosted regression portfolio | Neural network regression portfolio | Mean-variance portfolio | S&P 500 Index | Bloomberg U.S. Aggregate Bond Index | S&P U.S. Treasury Bond Index (1-3 Year, 3-5 Year, 10-20 Year) | MSCI U.S. REIT Index
- Benchmark evaluation: 在LendingClub数据上，将线性GCPP和非线性GCPP与等权重、风险过滤、线性回归、梯度提升回归、神经网络回归、均值方差等基准组合比较，报告IRR、ROI、效用等客观指标；另外，将GCPP组合与传统资产指数（S&P 500、债券指数、REIT指数）比较，使用PME和相关性评价吸引力。非线性GCPP组合在IRR、PME等指标上显著优于基准。
- Dataset status: named_public_dataset_central
- Named datasets: LendingClub Loan Data
- Dataset obtainability: LendingClub的历史贷款数据是公开数据集，包含贷款特征、还款状态等，可通过LendingClub官方网站的公开统计页面下载，也可通过Kaggle等第三方平台获取。独立研究者依据论文信息可找到并下载该数据。
- Decision: 文章核心是提出GCPP框架以构建在线贷款投资组合，核心成功指标为IRR、ROI、PME等完全客观的财务绩效指标，没有任何主观评价或满意度构念。研究问题、设计目标、评价结构和贡献声明均围绕提升这些客观指标展开，不存在并列的其他核心目标（理论机制贡献本质由绩效提升支撑，不是独立目标）。全文存在明确的benchmark表述（如“comparing it against various benchmarks”），比较对象包括等权重、风险过滤、回归、均值方差等基准组合以及六大市场指数，benchmark评价直接支撑核心IRR提升主张，且有明确参照点。核心评价数据来自LendingClub公开数据集，公开可查、可获取，且所有主要结果表均基于该数据。因此三个模块全部通过，strict_include=true。
- Confidence: 0.95

## Geo-semantic-parsing: AI-powered geoparsing by traversing semantic knowledge graphs

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113346
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "F1分数", "measurement_cn": "基于TP/FP/FN计算：F1=2*precision*recall/(precision+recall)；预测坐标与NEEL16 ground truth坐标距离≤50km（≃31英里）计为TP。论文还报告了单个指标的F1值（GSP F1=0.665）。", "objectivity_reason_cn": "目标标签是外部事实性的地点坐标，比较规则（距离阈值）固定，TP/FP/FN可由公式直接计算，不依赖人的感受或语义评价。"}, {"name_cn": "Precision", "measurement_cn": "TP/(TP+FP)，基于同一50km距离阈值统计。", "objectivity_reason_cn": "由事实性预测与事实性ground truth计算得出，客观可复现。"}, {"name_cn": "Recall", "measurement_cn": "TP/(TP+FN)，基于同一50km距离阈值统计。", "objectivity_reason_cn": "由事实性预测与事实性ground truth计算得出，客观可复现。"}, {"name_cn": "平均处理时间", "measurement_cn": "测试集上每条推文的平均处理时间（Elapsed time，秒）。", "objectivity_reason_cn": "系统运行时间，直接可由系统日志/计时器测量。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: NEEL16 (2016 Named Entity Recognition and Linking Challenge official dataset) | Middleton et al. [33] | Halterman [37] | Avvenuti et al. [2]
- Benchmark evaluation: 在公开NEEL16数据集（含9289条英文推文、5348个地点标注）上，将GSP与2个baseline（naïve geoparser、NER+geocoder）和3个现有技术（Middleton et al.、Halterman、Avvenuti et al.[2]）比较，报告precision、recall、F1和elapsed time。结果显示GSP获得F1=0.665，显著优于所有对比方法（次优Avvenuti F1=0.553，Halterman F1=0.309，其余更低），从而支持GSP的核心提升主张。
- Dataset status: named_public_dataset_central
- Named datasets: NEEL16 (2016 Named Entity Recognition and Linking Challenge official dataset)
- Dataset obtainability: NEEL16是2016年NEEL挑战赛（Named Entity Recognition and Linking）的官方公开数据集，由挑战组织方公开提供，学术研究可下载/申请。独立研究者可凭论文信息检索到NEEL challenge官网并获取数据。
- Decision: 客观指标：geoparsing的precision/recall/F1/elapsed time完全客观，目标是预测NEEL16中事实性的地点坐标，标签为外部事实，不涉及主观感知；唯一核心目标：全文研究问题、设计目标、评价和贡献均围绕提升geoparsing性能，无并列理论、主观或政策贡献；Benchmark：第6.2节以'Benchmarks'小标题明确陈述基准比较，与2个baseline和3个现有SOTA方法在NEEL16数据集上比较，表2直接支撑GSP优于竞争者的核心主张，具有明确参照点；数据集：核心评价数据为公开的NEEL16官方挑战数据集，公开可查、可获取，且所有关键结果表基于该数据。三个模块全部通过，strict_include=true。
- Confidence: 0.95

## Human Identification for Activities of Daily Living: A Deep Transfer Learning Approach

- Year/journal: 2020 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2020.1759961
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "宏平均精确率 (Precision)", "measurement_cn": "在HANDY和OPPO目标数据集上，对每个被试类别计算Precision后取宏平均；来源为传感器识别结果与真实身份标签的比较。", "objectivity_reason_cn": "身份标签是外部可核验事实，不依赖人的感受或语义评价；Precision由分类结果直接计算。"}, {"name_cn": "宏平均召回率 (Recall)", "measurement_cn": "在HANDY和OPPO目标数据集上，对每个被试类别计算Recall后取宏平均；来源为传感器识别结果与真实身份标签的比较。", "objectivity_reason_cn": "召回率基于身份匹配的事实，客观可审计。"}, {"name_cn": "宏平均F1分数", "measurement_cn": "由精确率和召回率计算F1后取宏平均；来源同Precision/Recall。", "objectivity_reason_cn": "由客观性能指标计算，不涉及主观判断。"}, {"name_cn": "微平均准确率 (Accuracy)", "measurement_cn": "整体样本中正确识别身份的比例；在OPPO四个对象数据集上计算微平均准确率。", "objectivity_reason_cn": "准确率基于真实身份标签，客观可复现。"}, {"name_cn": "ROC 曲线下面积 (AUC)", "measurement_cn": "在OPPO目标数据集上计算的宏平均ROC曲线AUC（Figure 5）。", "objectivity_reason_cn": "AUC由分类得分与事实标签计算，客观。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: HANDY (A Benchmark dataset for context-awareness via wrist-worn motion sensors) | Opportunity (OPPO)
- Benchmark evaluation: 实验1在HANDY数据集上将CNN-HID与经典ML基准(kNN, SVM, NB, DT)及变体CNN-HID/T、CNN-HID/CA比较；实验2/3/4在OPPO四个对象传感器数据集上将DTL-HID与非迁移学习基准及其他DTL变体比较，报告了各模型的Accuracy、Precision、Recall、F1和AUC。结果证明DTL-HID在核心客观指标上显著优于所有基准。
- Dataset status: named_public_dataset_central
- Named datasets: HANDY | Opportunity (OPPO)
- Dataset obtainability: OPPO是学术界广泛使用的公开活动识别数据集，可通过项目官网/公开研究社区获取；HANDY发表于MDPI Data期刊（Data 2018, 3(3), 24），可公开下载。两数据集均可被独立研究者查证和获取。
- Decision: 客观指标方面：HID任务的身份标签为外部可核验事实，核心评价指标均为Accuracy/Precision/Recall/F1/AUC，不包含任何主观构念。唯一核心目标：研究问题、实验设计和贡献声明均以提升对象传感器上的HID性能为核心，设计原则和实用启示是从评估中衍生的附加讨论，不构成并列核心目标。Benchmark方面：全文在摘要和Evaluation Design中明确使用benchmark表述，在实验部分设计了系统化的基准比较（kNN/SVM/NB/DT及CNN-HID变体），基准比较直接支撑核心提升主张，且每个比较均有明确参照点。数据集方面：HANDY（公开Benchmark数据集）和OPPO（公开活动识别数据集）均可识别、可查证、可获取，且核心实验结果表（表7-11）均基于这些公开数据。因此三个模块全部通过，strict_include=true。
- Confidence: 0.95

## Proactive Resource Request for Disaster Response: A Deep Learning-Based Optimization Model

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2022.0125
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "平均单位需求剥夺成本", "measurement_cn": "按公式(36)计算，基于需求延迟时间δ、资源重要性得分c_k以及Holguín-Veras等(2013)估计的剥夺成本参数φ和b，在真实Weibo数据或模拟数据上求平均。", "objectivity_reason_cn": "剥夺成本是时间延迟和给定参数的确定性指数函数，可依系统日志/时间戳和公开参数客观计算，不涉及人类主观评价。"}, {"name_cn": "平均单位需求时间延迟", "measurement_cn": "从需求到达时间到满足时间的平均差值，按小时计。", "objectivity_reason_cn": "时间延迟是外部可核验的时间差，完全客观。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在真实Weibo洪水数据和模拟数据上，将提出的CNM-PRR与ReR、logNormMix-PRR、A-NDTT-PRR、AttnMC-PRR、CTDRP-PRR、LR-NV、DL-NV、logNormMix-IFCFS等8种方法比较，报告平均单位需求剥夺成本、平均时间延迟、未来需求满足百分比及多目标场景下的fill rate和公平性指标。
- Dataset status: named_public_dataset_central
- Named datasets: 2021 Henan floods Weibo posts dataset (GitHub: GiveHenanAHand/henan-rescue-viz-website)
- Dataset obtainability: 独立研究者可通过公开GitHub仓库访问并下载该数据集，链接在论文中明确给出。
- Decision: 文章以最小化灾害响应中需求延迟剥夺成本为核心目标，所有核心成功指标均为客观可计算成本/时间/百分比，无主观构念；全文明确使用“benchmark/benchmarked”表述并在评价章节与多个基线方法比较，benchmark结果直接支撑核心提升主张；核心评价基于公开GitHub发布的2021河南洪水微博需求数据集，数据集可公开获取并作为主要结果表依据。因此三项模块全部通过，strict_include为true。
- Confidence: 0.95

## RADAR: A Framework for Developing Adversarially Robust Cyber Defense AI Agents with Deep Reinforcement Learning

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2024/17339
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "逃避率 (Evasion Rate, ER)", "measurement_cn": "生成的对抗性恶意样本中被目标恶意软件检测器判定为良性（即成功逃避检测）的比例；ER = |逃逸样本数| / |生成样本总数|。在三个开源检测器 LGBM、MalConv、NonNeg 上分别计算。", "objectivity_reason_cn": "该指标基于恶意软件检测器对样本的恶意/良性分类结果计算，属于针对外部可核验事实（恶意软件是否被检测）的客观检测性能指标，不依赖人类感受或语义评价。"}, {"name_cn": "假阳性率 (False Positive Rate, FPR)", "measurement_cn": "良性可执行文件被检测器误报为恶意的比例，在从干净 Windows 安装获取的良性数据上计算。", "objectivity_reason_cn": "该指标基于检测器对良性样本的判定结果，客观可复现。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 实验1在三个检测器（LGBM、MalConv、NonNeg）和六类恶意软件上，将r-VAC与多种基准攻击方法（Random actions、BFA、EvadeHC、Surrogate RNN、Policy Gradient、DDQN、Rainbow、MAB-malware、ACER、A3C、GAMMA）比较逃避率，r-VAC在Combined列取得最高ER（28.13%、22.99%、18.98%）；实验2比较RL-RO鲁棒化前后的逃避率，平均降低约84%（即鲁棒性提升约7倍）。
- Dataset status: named_public_dataset_central
- Named datasets: VirusTotal malware corpus | Microsoft Windows clean installation benign executables
- Dataset obtainability: 恶意软件样本：VirusTotal为公开恶意软件聚合平台，提供学术/商业许可与公开API，独立研究者可申请获取；良性可执行文件：通过干净安装Microsoft Windows系统收集，方式公开可复现。
- Decision: 核心目标是提升恶意软件检测器在对抗攻击下的鲁棒性，核心指标为逃避率和假阳性率，均为基于恶意软件检测结果（恶意/良性事实标签）的客观指标，无主观构念或并列核心目标。全文明确使用'benchmark methods'、'benchmark experiments'等表述，在实验部分将r-VAC与多种SOTA基准方法比较，并以鲁棒化前后对比支撑核心提升主张。评价所用恶意样本来自公开可获取的VirusTotal平台（学术许可/API），良性样本来自Windows系统，公开可查可获取。三个模块均通过。
- Confidence: 0.95

## sDTM: A Supervised Bayesian Deep Topic Model for Text Analytics

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1124
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "模型拟合度（perplexity）", "measurement_cn": "在保留测试集上计算负对数似然，越低表示文档建模能力越强", "objectivity_reason_cn": "完全由模型概率和文本观测计算，不依赖人类主观评价"}, {"name_cn": "预测性能（AUROC / accuracy）", "measurement_cn": "Yelp二分类情感预测使用AUROC；Stack Exchange多分类类别预测使用accuracy，均为测试集上的外部标签预测结果", "objectivity_reason_cn": "结果基于平台公开标签（评级、类别）与模型预测的比对，客观可复现"}, {"name_cn": "回归系数方向与显著性", "measurement_cn": "基于sDTM导出的主题特征构造TopicEntropy和QASimilarity变量，在用户投票/帮助性回归中检验系数的方向和显著性", "objectivity_reason_cn": "因变量为平台的真实投票数，变量由主题模型确定性计算，回归系数可审计"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在Yelp和Stack Exchange两个数据集上进行系统化基准比较：模型拟合部分报告不同K值下的测试集perplexity，与LDA、sLDA、MedLDA、BP-sLDA、sNNTM、NTM等比较；预测部分报告AUROC/accuracy，并额外与RNN attention、Bi-LSTM、DistilBERT、BERT等深度模型比较。结果显示sDTM在多数设置下显著优于baseline或与SOTA可比。
- Dataset status: named_public_dataset_central
- Named datasets: Yelp.com consumer reviews | Stack Exchange online knowledge community
- Dataset obtainability: Yelp评论来自Yelp.com公开页面，可通过公开网站或Yelp官方公开数据集获取；Stack Exchange帖子可通过Stack Exchange Data Explorer或公开数据转储下载，两者均有公开API，独立研究者可凭论文信息检索并获取。
- Decision: 客观指标检查：核心指标为测试集perplexity、预测AUROC/accuracy、基于真实投票数的回归系数，均完全客观可测量，且是唯一核心目标。benchmark检查：文中在摘要、第5.1节、第7.1节明确使用benchmark/benchmarking表述，并给出LDA、sLDA、NTM、BERT等明确比较基线，评价位于实验语境且直接支撑核心提升主张；属于benchmark_comparison_central。数据集检查：核心评价基于Yelp.com和Stack Exchange两个公开平台数据，可通过公开网页/API/数据转储获取，且为主要结果表的依据。三项全部通过，因此strict_include为true。
- Confidence: 0.95

## A hybrid decision support system for adaptive trading strategies: Combining a rule-based expert system with a deep reinforcement learning strategy

- Year/journal: 2024 / Decision Support Systems
- DOI: 10.1016/j.dss.2023.114100
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "累计收益率（%AR）", "measurement_cn": "回测中投资组合相对初始投资的累计收益变化，由公开指数日线数据计算。", "objectivity_reason_cn": "由交易价格、持仓与资金公式确定，不依赖人的感受或语义判断。"}, {"name_cn": "夏普比率（Sharpe Ratio）", "measurement_cn": "年化收益率与年化标准差之比，衡量风险调整后收益，由回测日收益计算。", "objectivity_reason_cn": "基于可审计的收益与波动率数据计算。"}, {"name_cn": "最大回撤（MDD）", "measurement_cn": "回测期间资产净值从峰值到谷值的最大跌幅。", "objectivity_reason_cn": "由资产净值曲线直接可观测。"}, {"name_cn": "年化/日均收益与标准差", "measurement_cn": "回测收益率的统计量。", "objectivity_reason_cn": "由历史价格与交易结果计算。"}, {"name_cn": "交易信号数量", "measurement_cn": "模型在测试期产生的买入/卖出信号次数。", "objectivity_reason_cn": "由算法输出信号计数，客观可审计。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: TI+SVM | TI+RF | TI+LSTM | TI+XGBoost+CNN+LSTM | B&H
- Benchmark evaluation: 在 S&P 500 的测试期及市场崩溃/上涨/下跌子时期，将所提 RB+RL+C1+C2 模型与 B&H、RB、RL、消融变体以及 TI+SVM、TI+RF、TI+LSTM、TI+XGBoost+CNN+LSTM 等既有混合模型比较，报告 %AR 和夏普比率；并在六只指数基金上做扩展比较。
- Dataset status: publicly_described_source_central
- Named datasets: S&P 500 index daily data (Yahoo Finance) | NYSE Composite (Yahoo Finance) | DAX Performance Index (Yahoo Finance) | CAC40 (Yahoo Finance) | Hang Seng Index (Yahoo Finance) | KOSPI Composite Index (Yahoo Finance)
- Dataset obtainability: 独立研究者可依据论文给出的指数名称与区间，从 Yahoo Finance 免费获取日度开高低收量数据；论文也声明数据可应请求提供。
- Decision: 核心成功指标全部为客观回测财务指标（累计收益、夏普比率、最大回撤、标准差、信号数），且提升该指标是唯一核心目标与贡献；全文在方法/实验部分明确以 benchmarks 指称比较模型并进行了系统性对比，结果支持核心提升主张；评价所用数据来自 Yahoo Finance 公开可获取的指数日线数据，占核心结果表依据。三个模块均通过。
- Confidence: 0.92

## Dynamic self-organizing feature map-based models applied to bankruptcy prediction

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113576
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "正确分类率", "measurement_cn": "根据 Diane 数据库中企业破产/存活标签计算的正确分类比例，公式为 (TN+TP)/总计。", "objectivity_reason_cn": "破产状态是外部可核验的法律/商业事实，分类正确率完全由分类结果与外部标签决定，不依赖人类感受或语义评价。"}, {"name_cn": "F2 分数", "measurement_cn": "对破产企业正确分类（召回）赋予更高权重的 F 分数，由精度和召回计算。", "objectivity_reason_cn": "基于破产标签和模型预测的客观混淆矩阵计算，指标本身不涉及人为主观评价。"}, {"name_cn": "AUC", "measurement_cn": "ROC 曲线下面积，反映不同阈值下真阳率和假阳率。", "objectivity_reason_cn": "由破产标签与模型输出概率计算，指标客观，可复算。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 作者将提出的动态模型与 Cox 生存模型、SVM、ELM、Bagging、AdaBoost、XGBoost、Random Subspace、Random Forest 等方法在相同样本上比较，使用正确分类率、F2 和 AUC 三种指标；结果表格（表8-11）显示动态模型普遍优于基准模型。
- Dataset status: named_public_dataset_central
- Named datasets: Diane database (Bureau van Dijk)
- Dataset obtainability: Diane 是由 Bureau van Dijk 提供的商业金融数据库，学术界和金融机构可通过订阅渠道正式获取，符合公开商业订阅数据标准。
- Decision: 文章以破产预测正确率、F2 和 AUC 作为唯一核心成功指标，破产状态属于可核验的外部事实标签；全文存在明确的 benchmark 表述（第4节将传统模型作为基准），且比较结果直接支撑核心改进主张；核心评价数据来自可公开获取的商业订阅数据库 Diane（Bureau van Dijk），因此三个模块全部通过。
- Confidence: 0.92

## Recognition of human activities for wellness management using a smartphone and a smartwatch: A boosting approach

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113426
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "Accuracy/F1/AUC", "measurement_cn": "在ExtraSensory公开数据集上训练分类器（XgBoost、AdaBoost、Boosted C5.0，以及Neural Network、SVM等对照组），对walking、standing、sitting、exercise、sleeping五个活动标签进行二分类预测，计算测试集上的Accuracy、F1 score和验证AUC。", "objectivity_reason_cn": "活动标签（行走、站立、坐、锻炼、睡眠）对应外部可观察的物理行为，不依赖用户满意度、偏好、美感或语义质量评价；分类性能可由预测结果与标签直接计算。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: ExtraSensory dataset
- Benchmark evaluation: 在ExtraSensory数据集上，作者对五个基本活动分别构建二分类模型，使用138个特征训练XgBoost、AdaBoost和Boosted C5.0，报告验证AUC和测试Accuracy/F1；随后又与Neural Network、SVM、LR、MLP等标准机器学习方法在相同数据上比较，并引用先前研究在相同数据上的结果作为参照。
- Dataset status: named_public_dataset_central
- Named datasets: ExtraSensory dataset
- Dataset obtainability: ExtraSensory是由公开学术项目发布的自然环境下智能手机和智能手表传感器数据集；论文明确标明其公开可获得性，并通过引用原始文献（Vaizman et al., 2017）给出可查证来源。独立研究者可通过公开渠道获取该数据集。
- Decision: 文章以提升HAR分类客观性能（accuracy/F1/AUC）为唯一核心目标；评价基于公开可获取的ExtraSensory数据集，全文明确将该数据集作为模型训练与测试场地，并与多种传统机器学习方法及先前研究结果进行比较；无主观体验、用户满意度或语义质量评价作为核心成功标准，因此三个模块均通过。
- Confidence: 0.92

## Unlocking the Power of Voice for Financial Risk Prediction: A Theory-Driven Deep Learning Design Approach

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/17062
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "金融风险预测的均方误差（MSE）与样本外决定系数（R²_oos）", "measurement_cn": "以公司股票收益在未来 τ 天（τ=3,5,10,30,60）的实际波动率（标准差）为真值，模型预测值与其对比计算MSE；R²_oos = 1 - MSE^模型 / MSE^市场基准模型，作为主性能衡量。", "objectivity_reason_cn": "金融风险（波动率）由股票价格收益的数学标准差直接计算，不依赖人类感知、语义判断或价值评价；MSE和R²均为确定性数值指标。"}, {"name_cn": "期权交易策略收益", "measurement_cn": "基于DeepVoice风险预测构建多头-空头跨式期权组合，用期权市场行情（OptionMetrics）计算策略回报率。", "objectivity_reason_cn": "期权价格和回报由公开市场交易数据（bid/ask报价、到期收益）计算，完全客观可核验。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: DeepVoice在所有预测视界（3/5/10/30/60天）与市场基准模型（Sridharan 2015的基本面加历史风险堆叠模型）比较，R²_oos分别达到7.31%、8.34%、4.28%、2.26%、7.45%，且均显著。此外，表5和表6中还将DeepVoice与Concat-SVR、Concat-GradientBoosting、One-stage LSTM、Contextual LSTM、DeepVoice-attention以及Emotion模型等基准比较，DeepVoice均表现最佳。
- Dataset status: publicly_described_source_central
- Named datasets: Seeking Alpha（财报电话会议文本记录） | EarningsCast（对应音频录音） | Compustat（财务基本面数据） | CRSP（股票价格数据）
- Dataset obtainability: Seeking Alpha 和 EarningsCast 是公开网站，独立研究者可通过公开访问获取财报电话会议文本和音频（且文中描述为crawler抓取）；Compustat、CRSP、OptionMetrics、TAQ 是金融学界广泛订阅的标准商业数据库，具有公开订购渠道；S&P 500公司名单本身公开。因此，独立研究者能够根据论文信息找到并获取核心评价数据。
- Decision: 客观指标：核心目标是金融风险（波动率）的预测准确性，完全由股票市场价格数据计算，无主观语义判断；唯一核心目标是提升样本外预测性能，方法论贡献和设计原则均围绕此目标，不存在并列核心目标。Benchmark：全文在评价语境中明确使用benchmark model和market benchmark概念，并系统地将DeepVoice与多个基准模型比较，结果作为核心证据；有明确参照点。数据：核心评价数据来源于公开网站（Seeking Alpha、EarningsCast）和公开商业数据库（Compustat、CRSP），独立研究者可凭论文信息获取；公开数据支撑核心提升主张。三个模块全部通过，因此strict_include为true。
- Confidence: 0.92

## A deep recurrent neural network approach to learn sequence similarities for user-identification

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113718
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "用户再识别准确率（P）", "measurement_cn": "在双选择用户再识别实验中，模型在保留测试用户上从正负样本中选择与锚定序列同用户的正确率；另有多用户分配任务的ARI和估计用户数的精确率/召回率。", "objectivity_reason_cn": "用户身份是外部可核验事实标签，准确率、ARI、精确率和召回率均由系统输出与真实标签对比计算，不依赖人类感受或语义判断。"}, {"name_cn": "聚类调整兰德指数（ARI）", "measurement_cn": "将混合序列向量用kmeans聚类后与真实用户标签比较，计算ARI。", "objectivity_reason_cn": "真实用户标签为客观事实，ARI是标准聚类评价指标，计算确定。"}, {"name_cn": "估计用户数的精确率/召回率", "measurement_cn": "用Silhouette系数确定最优簇数，与真实用户数对比计算精确率和召回率。", "objectivity_reason_cn": "真实用户数为客观计数，精确率和召回率通过确定规则计算。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在Comscore点击流数据上，将TL-RNN与Smith-Waterman序列比对和TF-RW度量对比，在双选择用户再识别、多用户分配和用户数估计三个任务中报告准确率、ARI、精度/召回率等，结果表显示TL-RNN在多数设置下优于基准方法。
- Dataset status: named_public_dataset_central
- Named datasets: Comscore Web Behavior Panel
- Dataset obtainability: Comscore Web Behavior Panel是商业市场研究数据产品，可通过Comscore公司的公开商业渠道获取（需要订阅或许可），但独立研究者能够识别并联系获取，符合公开商业订阅数据标准。
- Decision: 该文核心目标是提出TL-RNN框架以提升序列相似性度量的客观预测性能（用户再识别准确率、ARI、精确率/召回率），评价指标全部基于外部可核验的用户身份标签，无主观构念；全文存在明确的benchmark表述（摘要和Benchmark methods节），并与Smith-Waterman、TF-RW等基准方法比较，benchmark评价直接支撑核心提升主张；核心评价数据来自Comscore Web Behavior Panel，该数据集可通过Comscore公开商业渠道识别和获取，且所有主要结果表均基于该数据。因此三个模块全部通过，strict_include=true。
- Confidence: 0.9

## Analysis of third-party request structures to detect fraudulent websites

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113698
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "准确率 (Accuracy)", "measurement_cn": "在10折交叉验证中，正确分类的网站数占总网站数的比例。", "objectivity_reason_cn": "由预测标签与事实标签（欺诈/合法）计算，不依赖主观判断。"}, {"name_cn": "敏感性 (Sensitivity)", "measurement_cn": "真正例数占实际欺诈网站数的比例。", "objectivity_reason_cn": "基于固定欺诈事实标签计算。"}, {"name_cn": "特异性 (Specificity)", "measurement_cn": "真负例数占实际合法网站数的比例。", "objectivity_reason_cn": "基于固定合法事实标签计算。"}, {"name_cn": "精确度 (Precision)", "measurement_cn": "预测为欺诈且实际为欺诈的网站数占预测为欺诈网站数的比例。", "objectivity_reason_cn": "从混淆矩阵客观计算。"}, {"name_cn": "F1分数", "measurement_cn": "精确度和敏感性的调和平均数。", "objectivity_reason_cn": "由客观混淆矩阵计算。"}, {"name_cn": "Matthews相关系数 (MCC)", "measurement_cn": "衡量二分类预测质量的相关系数。", "objectivity_reason_cn": "由混淆矩阵各元素客观计算。"}, {"name_cn": "Youden J统计量", "measurement_cn": "敏感性+特异性-1，综合衡量分类能力。", "objectivity_reason_cn": "由混淆矩阵客观计算。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 作者构建并报告了多组基准评价：1) 三种朴素基准（全判合法、全判欺诈、50/50随机）；2) 基于既有第三方使用（3PU）数据的方法（如CS5、svmRadial）作为基线；3) 对比提出的第三方请求结构（RS）数据模型、组合3PU+RS数据模型。结果显示RS及组合模型在准确率、F1、MCC等客观指标上显著优于基准，如组合CS5将准确率从0.728提升至0.805，加权集成达0.826。
- Dataset status: publicly_described_source_central
- Named datasets: Alexa.com top 50 websites | European Commission Counterfeit and Piracy Watch List | USTR 2019 Review of Notorious Markets for Counterfeiting and Piracy | Wikipedia list of fake news websites | EasyPrivacy list | Cookipedia database
- Dataset obtainability: 上述来源均为公开可获取资源：Alexa.com是公开网站排行榜，欧盟委员会和USTR的报告在官方网站公开发布，维基百科列表公开可访问；EasyPrivacy和Cookipedia也是公开的在线数据/列表。此外，Section 4.2明确描述了使用Selenium WebDriver抓取公开网站HTTP请求的获取方式，独立研究者可依据论文信息识别来源并复现数据收集过程。
- Decision: 本文核心目标是通过第三方请求结构特征预测网站欺诈状态，提升检测性能。被预测的欺诈/合法标签来自公开权威来源，属于固定事实标签，核心评价指标（准确率、F1、MCC等）均为客观分类性能指标，且论文通篇未引入主观体验或语义质量评价作为成功标准。全文存在明确的benchmark表述：在Section 5.1使用三种朴素预测方法进行benchmark比较，并在后续与既有3PU数据模型系统对比，benchmark结果直接支撑了核心提升主张。数据集来源为公开可获取的名单（Alexa、欧盟委员会、USTR、维基百科）及公开的第三方属性数据源，文章清楚描述了来源和获取方式，独立研究者可据此复现。因此三个条件全部满足。
- Confidence: 0.9

## First, Do No Harm: Predictive Analytics to Reduce In-Hospital Adverse Events

- Year/journal: 2021 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2021.1990619
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "AUC（受试者工作特征曲线下面积）", "measurement_cn": "基于佛罗里达AHCA住院患者数据，将SALT预测的AE风险概率与二元AE标签比较，计算AUC。AE标签依据UMAEC清单和POA指示器构造。", "objectivity_reason_cn": "AE标签是外部事实标签（是否发生医疗错误导致的不良事件），由诊断编码和固定规则确定，不依赖人类主观评价；AUC是可复现的统计计算。"}, {"name_cn": "精确率、召回率、F分数", "measurement_cn": "在相同数据上使用Youden指数确定判定阈值，计算精确率、召回率和F分数。", "objectivity_reason_cn": "这些指标基于客观标签和模型输出的确定性计算，不涉及主观感知。"}, {"name_cn": "防止的AE数量与误报数量", "measurement_cn": "通过模拟评估SALT在不同阈值下的预防AE数量和误报数量，与GLMM和LR比较。", "objectivity_reason_cn": "模拟逻辑基于预测风险与实际标签的一致性，指标为可审计的计数。"}, {"name_cn": "成本节省（百万美元）", "measurement_cn": "基于预防的ADE、手术AE和感染AE数量，结合文献中的单次AE成本估计并折算至2010年美元，减去误报成本。", "objectivity_reason_cn": "成本计算基于公开的成本估计和可复现的财务公式，属于可审计的财务指标。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: SALT在佛罗里达AHCA住院患者数据集上，与GLMM、MERT、MERF（Evaluation 1）以及CART、DNN、GBM、LR、NB、RF、SVM（Evaluation 2）进行系统比较，报告AUC、精确率、召回率和F分数。Evaluation 3进一步与GLMM和LR比较模拟中的防止AE数量和误报数。benchmark结果用于支持SALT预测性能提升的核心主张。
- Dataset status: named_public_dataset_central
- Named datasets: Florida Agency for Health Care Administration (AHCA) 住院患者出院数据 | Hospital Compare (CMS) | Physician Compare (CMS) | American Hospital Association Healthcare IT Database
- Dataset obtainability: 佛罗里达AHCA的医院出院数据是州政府收集和发布的公开数据，独立研究者可通过AHCA官方渠道申请或获取；辅助数据集Hospital Compare和Physician Compare由CMS公开提供，Healthcare IT数据库来自美国医院协会且通常可订阅获取。核心评价（Evaluation 1/2/3）均基于佛罗里达AHCA数据。
- Decision: 客观指标：核心成功指标为AUC、精确率、召回率、F分数、防止AE数量与成本节省，基于AE事实标签（ICD-9-CM编码+UMAEC清单+POA指示器）和财务计算确定，完全不依赖人类主观评价。唯一核心目标：研究目标、评价结构和贡献声明均围绕预测性能提升展开，无其他并列核心目标。Benchmark：在评价语境中明确使用“benchmarks”指代GLMM、LR等基线，并通过多个数据划分点比较，结果支持核心性能提升主张，且存在明确参照点。数据集：核心评价使用佛罗里达AHCA医院出院数据，该数据是州政府公开数据，可公开查找和获取；辅助数据源也是公开的。因此三个模块均通过。
- Confidence: 0.9

## Hiding Sensitive Information when Sharing Distributed Transactional Data

- Year/journal: 2020 / Information Systems Research
- DOI: 10.1287/isre.2019.0898
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "共享数据集准确率（未净化事务占比）", "measurement_cn": "最小化需要净化（sanitize）的事务数量；对应FIH_D整数规划的目标函数∑x_i，准确率定义为未被净化事务占总事务的比例。", "objectivity_reason_cn": "该指标仅依赖事务中项集支持度是否低于指定隐藏阈值以及事务是否被选择净化，是可由数据直接计算和审计的客观事实，不涉及人的感受、语义评价或价值判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在真实数据集Retail、BMS-POS及合成数据集上，将Ensemble方法与CPLEX求得的最优解和Verykios et al. (2004)的方法比较，核心指标是净化事务数和相对最优解的Gap。结果显示Ensemble非常接近最优解，而Verykios方法Gap较大且无法处理合成大数据库。
- Dataset status: named_public_dataset_central
- Named datasets: Retail | BMS-POS
- Dataset obtainability: Retail和BMS-POS可从FIMI公开数据集仓库（fimi.ua.ac.be/data/）直接下载，独立研究者可凭论文信息查到并获取；该公开数据构成表3核心结果的一部分。合成数据由IBM Quest生成器生成，但公开真实数据已足够支撑核心提升主张。
- Decision: 文章核心是以最小化净化事务数量/最大化共享数据集准确率为唯一核心目标的分布式敏感项集隐藏问题，提出Ensemble方法，并在真实公开数据集Retail、BMS-POS以及合成数据集上与最优解和既有方法进行benchmark比较。客观指标是核心且唯一；存在明确benchmark表述和比较基准；核心评价使用了公开可获取数据集。三个模块均通过。
- Confidence: 0.9

## Who Is the Next “Wolf of Wall Street”? Detection of Financial Intermediary Misconduct

- Year/journal: 2020 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00633
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "准确率", "measurement_cn": "基于自然分布样本的混淆矩阵计算 (TP+TN)/总数", "objectivity_reason_cn": "预测类别与 BrokerCheck 最终监管记录标签作确定性比较，不依赖主观评价"}, {"name_cn": "召回率", "measurement_cn": "基于自然分布样本的混淆矩阵计算 TP/(TP+FN)", "objectivity_reason_cn": "同上，客观可复现"}, {"name_cn": "精确率", "measurement_cn": "基于自然分布样本的混淆矩阵计算 TP/(TP+FP)", "objectivity_reason_cn": "同上，客观可复现"}, {"name_cn": "F1分数", "measurement_cn": "精确率与召回率的调和平均数", "objectivity_reason_cn": "基于客观分类结果计算"}, {"name_cn": "AUC", "measurement_cn": "ROC曲线下面积，基于不同分类阈值下的真阳性率与假阳性率", "objectivity_reason_cn": "由预测概率与客观标签计算"}, {"name_cn": "经济收益", "measurement_cn": "基于补偿支付和罚款金额计算的可避免损失（即经济评价）", "objectivity_reason_cn": "基于监管记录中的赔偿金额和罚款，是可审计的客观数值"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在自然分布样本上，作者将包含 regulator-confirmed 信息的分类器 C 和 D 与仅基于 self-disclosed 信息的分类器 A 和 B 作为基准进行系统比较，使用 McNemar 检验。结果显示 C/D 在多个机器学习方法上显著优于 A/B（例如 RF 的 C/A 和 D/A 均 p<0.01），从而为核心主张（regulator-confirmed 信息提升检测性能）提供关键证据。附录 D 中还将 D 与 E/F 基准比较。
- Dataset status: named_public_dataset_central
- Named datasets: BrokerCheck (FINRA) | LinkedIn
- Dataset obtainability: BrokerCheck 是 FINRA 运营的公开在线数据库，任何研究者均可通过其网站查询美国注册经纪人的披露记录；LinkedIn 是公开职业社交平台，其公开 profiles 可通过网站访问或官方 API 获取。独立研究者可按照论文描述，从 BrokerCheck 随机抽取经纪人，再匹配其公开 LinkedIn 资料，从而重建该数据集。两种数据源均公开可获取，而非私有或保密数据。
- Decision: 客观指标：核心目标构念为金融中介是否发生不当行为，基于 FINRA BrokerCheck 最终监管披露记录，属于客观事实标签；评价指标全部为分类性能（准确率、召回率、精确率、F1、AUC）和经济收益，不含任何主观量表或人类语义评判。唯一核心目标：研究问题、设计目标、评价结构和贡献声明均围绕自动化检测金融中介不当行为的性能提升展开，理论仅作为特征选择和解释依据，不构成并列核心目标。Benchmark：全文存在明确的 benchmark 表述（Table 11 标题明确以 Classifiers A/B 为 Benchmarks），该基准评价位于结果部分，并为核心主张（加入监管确认信息提升检测性能）提供关键证据，且有明确参照点。数据集：核心评价数据来自公开可获取的 BrokerCheck（FINRA 公开数据库）和 LinkedIn（公开平台），且均被明确命名，独立研究者可按论文描述复现获取。因此三个模块全部通过，strict_include=true。
- Confidence: 0.9

## A Deep Learning Approach for Recognizing Activity of Daily Living (ADL) for Senior Care: Exploiting Interaction Dependency and Temporal Patterns

- Year/journal: 2021 / MIS Quarterly
- DOI: 10.25300/misq/2021/15574
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "宏平均F1", "measurement_cn": "在INTER和OPPO-ML上对交互/手势类别预测的precision/recall/F1，再对类别取宏平均", "objectivity_reason_cn": "根据传感器记录和固定活动标签计算，不依赖人的感受或语义偏好"}, {"name_cn": "Accuracy", "measurement_cn": "在OPPO-HL上对HL-ADL标签序列逐标签正确率，以及端到端Acc@1/Acc@2", "objectivity_reason_cn": "预测标签与固定活动标签对比，可计算、可复核"}, {"name_cn": "平均块Levenshtein距离(ABLD)", "measurement_cn": "在OPPO-HL上比较预测HL-ADL块序列与真实块序列的编辑距离并取平均", "objectivity_reason_cn": "基于固定活动块序列的确定性编辑距离，不涉及主观评价"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: Opportunity (OPPO) public ADL benchmark dataset
- Benchmark evaluation: 四个实验分别将I-CNN、I-CNN-GR、S2S_GRU和整个层次ADLR框架与kNN、SVM、CNN-1D、CNN-2D、DeepConvLSTM、决策树、HMM、S2S_LSTM、SAE+SVM、LDA主题模型等基准比较，在INTER、OPPO-ML和OPPO-HL上报告F1、Accuracy、Acc@1/2、ABLD，并用配对t检验验证提升。
- Dataset status: named_public_dataset_central
- Named datasets: Opportunity (OPPO)
- Dataset obtainability: Opportunity数据集可通过其公开发布渠道获取（如项目/UCI公开下载），独立研究者可检索并下载；OPPO上的OPPO-ML和OPPO-HL是核心手势识别、活动识别和端到端评价的主要测试床。INTER为作者自采，论文未提供公开获取方式，但仅用于交互提取组件，属于少量私有补充数据。
- Decision: 客观指标方面，核心构念是固定ADL/交互/手势标签上的分类与序列识别性能，不依赖人的主观体验；核心目标是设计并评价一个多层次ADLR框架，全文无主观量表作为成功标准。benchmark方面，作者明确使用benchmark/benchmarks表述，在实验部分将各组件和整体框架与SVM、DeepConvLSTM、HMM、主题模型等基准比较，且结果直接支撑准确率提升主张。数据集方面，核心端到端、手势和活动识别评价基于公开的Opportunity数据集，虽然INTER为自采，但仅用于交互提取组件，属于公开数据主导、少量私有补充，符合混用标准。因此三个模块均通过。
- Confidence: 0.88

## Creating Proactive Cyber Threat Intelligence with Hacker Exploit Labels: A Deep Transfer Learning Approach

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2023/17316
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "Accuracy（准确率）", "measurement_cn": "在源域（96,333条带标签exploit）和目标域（4,842条ground-truth exploit）测试集上按TP/TN/FP/FN计算，并按类别support加权平均。", "objectivity_reason_cn": "标签是攻击类型等可外部核验的操作性类别（web应用、DoS、remote、local、SQL注入、XSS、file inclusion、overflow），不是主观质量或体验判断；数值由确定公式计算。"}, {"name_cn": "Precision（精确率）", "measurement_cn": "TP/(TP+FP)，按类别support加权平均，各实验表报告。", "objectivity_reason_cn": "基于ground-truth事实标签和模型预测计算，不依赖人的感受或语义评价。"}, {"name_cn": "Recall（召回率）", "measurement_cn": "TP/(TP+FN)，按类别support加权平均，各实验表报告。", "objectivity_reason_cn": "基于ground-truth事实标签和模型预测计算，不依赖人的感受或语义评价。"}, {"name_cn": "F1-score（F1值）", "measurement_cn": "precision与recall的调和平均数，按类别support加权平均，作为主要比较指标。", "objectivity_reason_cn": "由客观分类结果计算，用于衡量事实标签预测性能，不涉及主观构念。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在自建的源域（exploit DNM和公共exploit库）与目标域（黑客论坛ground-truth）数据集上，以经典机器学习（naive Bayes、logistic regression、decision tree、SVM、XGBoost、LightGBM）、深度学习（RNN、GRU、LSTM、BiLSTM、BiLSTM+self-attention）、其他迁移学习（adaptive SVM、hard/soft MTL、adversarial、BERT）以及层选择消融为基准，报告accuracy、precision、recall、F1-score。DTL-EL在源域F1=90.91%，目标域F1=70.34%，显著高于各基准。
- Dataset status: publicly_described_source_central
- Named datasets: 0day.today | Seebug | ExploitDB | PacketStorm | Metasploit | Vulnerlab | Zeroscience | 0x00sec | Altenens | AntiChat | AntiOnline | Cipher | Go4expert | PersianTools | WWHClub | WildersSecurity
- Dataset obtainability: 数据来源为公开命名的黑客论坛、exploit DNM和公共exploit库（如ExploitDB、PacketStorm、Seebug、0day.today等）。独立研究者可按表5中的平台名称通过公开网站访问、下载或爬取获取；论文未提供打包的ground-truth数据集，但来源明确、非NDA/非内部保密数据。
- Decision: 客观指标为exploit攻击类型分类的accuracy、precision、recall和F1-score，属于可外部核验的事实标签预测性能；核心目标唯一为提升该分类性能。全文在实验部分明确使用benchmark experiments/benchmark methods，并与多组baseline、SOTA和消融模型比较，benchmark结果直接支撑核心提升主张。核心评价数据来自公开命名的黑客论坛、exploit DNM和公共exploit库，来源公开可查且可通过公开网站获取。三个模块均通过，strict_include=true。
- Confidence: 0.88

## Mining Semantic Soft Factors for Credit Risk Evaluation in Peer-to-Peer Lending

- Year/journal: 2020 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2019.1705513
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "违约预测判别性能（AUC、KS、H measure）", "measurement_cn": "以Lending Club借款人是否发生违约/核销作为事实标签，使用四种分类模型（LR、LASSO、RF、XGB）在硬特征、语义软特征及组合特征下进行10折交叉验证重复10次计算。", "objectivity_reason_cn": "违约标签由平台客观支付/核销记录定义，不依赖人类主观评价；AUC/KS/H measure为可复算的确定性统计指标。"}, {"name_cn": "授信组合绩效（所选组合的违约率）", "measurement_cn": "模拟真实投资场景，根据不同风险排序策略和授信比例选择贷款组合，计算组合中违约贷款的比例。", "objectivity_reason_cn": "组合违约率基于客观违约标签和可审计的选择规则，属可量化、可核验的客观结果。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在Lending Club数据集上，使用LR、LASSO、RF、XGB四种模型，对硬特征、语义软特征、硬特征+语义软特征进行判别性能比较；进一步与LDA主题特征、统计/可读性/情感等软特征比较，并模拟授信组合绩效，以平台信用子级为参考线。核心结论是加入语义软特征显著提升AUC、KS、H measure并降低组合违约率。
- Dataset status: named_public_dataset_central
- Named datasets: Lending Club 个人贷款数据
- Dataset obtainability: Lending Club公开提供历史贷款数据，可通过Lending Club网站、Kaggle等公开渠道下载；论文明确指出数据来源为Lending Club，独立研究者可据此找到并获取该公开数据集。
- Decision: 核心结果是违约预测与授信组合违约率，均基于客观事实标签并采用AUC/KS/H measure等确定性指标；研究问题、评价结构和贡献声明均围绕“提取语义软因子并提升信用风险评估性能”这一唯一核心目标展开。全文在实证评估部分明确将logistic regression作为benchmark method，并对硬特征、语义软特征和多种基线特征进行系统比较，该比较结果是核心提升主张的直接证据。评价数据来自公开可获取的Lending Club历史贷款数据，独立研究者可凭论文信息查得并获取。因此三个模块均通过。
- Confidence: 0.88

## Neighbor-aware review helpfulness prediction

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113581
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "分类准确率（Accuracy）", "measurement_cn": "将每条评论根据用户投票的真实标签（helpful=1, unhelpful=0）与模型预测标签比较，计算正确分类的比例。实验采用80%-10%-10%时间顺序划分训练/验证/测试集，并平衡正负样本。", "objectivity_reason_cn": "帮助性标签来自用户在实际平台上的投票行为（是否点击“有帮助”），是可观察的外部事实记录，不依赖研究者或专家的主观语义评价。准确率是确定性计算的客观性能指标，类似对冻结事实标签的预测性能。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在六个真实评论域（D1-D6）上，将NAP与独立预测、MLP编码器、以及六种上下文方法（I+ORD_D, I+ORD_R, I+ORD_V, I+CON, I+POL, I+ENT）系统性比较，报告准确率并进行t检验。结果显示NAP显著优于所有baselines 1%-5%。该benchmark评价直接支撑核心准确率提升主张。
- Dataset status: publicly_described_source_central
- Named datasets: 
- Dataset obtainability: SiteJabber（sitejabber.com）和ConsumerAffairs（consumeraffairs.com）是公开的评论平台，任何独立研究者均可通过公开网站访问并抓取评论、投票和元数据。文章详细说明了收集时间、预处理步骤和划分方式，足以凭论文信息复现数据采集。
- Decision: 该文以完全客观的分类准确率为唯一核心目标，预测的标签是用户投票行为形成的冻结事实标签，无任何主观量表或语义评价作为成功标准。作者明确使用“benchmark”一词描述系统化基准比较（against a series of baselines），并将该比较作为证明核心准确率提升的关键证据，且具有多个明确参照点（baselines和独立预测）。数据来自SiteJabber和ConsumerAffairs两个公开评论平台，论文详细说明了来源和采集方式，独立研究者可凭论文信息获取该数据，且所有核心结果均基于该公开数据。因此三个模块全部通过，strict_include为true。
- Confidence: 0.88

## Pricing in Nonconvex Markets: How to Price Electricity in the Presence of Demand Response

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1139
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "make-whole payments（总补偿额及占总成本比例）", "measurement_cn": "由不同定价规则（IP、ELMP、AIC、PBE-A/PE-A）在DCOPF/SCUC模型上计算出的线性匿名价格下的个性化补偿金额；表格报告总MWP、卖方/买方MWP以及MWP/总成本百分比。", "objectivity_reason_cn": "这些金额是根据公开指定的报价、成本数据和定价公式确定性地计算出的货币数值，不依赖人类感受、价值判断或语义评价。"}, {"name_cn": "市场电价（均值、标准差）", "measurement_cn": "各定价规则在IEEE RTS-96系统上计算出的每小时/节点电价，报告均值和标准差。", "objectivity_reason_cn": "电价是模型解出的可审计数值，属于交易/技术事实，不依赖主观体验。"}, {"name_cn": "维持稳定所需的罚金（penalties）", "measurement_cn": "为避免发电商偏离有效调度而计算的罚金，表中报告卖方/买方罚金额。", "objectivity_reason_cn": "罚金由模型和调度偏离定义计算得出，是可验证的货币技术指标。"}, {"name_cn": "计算时间", "measurement_cn": "各定价规则在相同硬件条件下求解的运行秒数。", "objectivity_reason_cn": "运行时间是可复现的技术性能指标，完全客观。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: IEEE RTS-96 (IEEE Reliability Test System)
- Benchmark evaluation: 在IEEE RTS-96这一标准benchmark系统上，对PBE-A/PE-A与IP pricing、ELMP、AIC pricing在价格无弹性、价格敏感、可平移负荷等场景下进行比较；结果表13-16报告价格均值/标准差、MWP、罚金和计算时间。核心改进主张（PE-A大幅降低make-whole payments）正是由该benchmark评价支撑。
- Dataset status: named_public_dataset_central
- Named datasets: IEEE RTS-96 (IEEE Reliability Test System) | Garcia-Bertrand et al. (2006) case study bid/offer curves | Zoltowska (2016) bid data
- Dataset obtainability: IEEE RTS-96是电力市场研究中广泛使用的公开标准测试系统，研究者可通过IEEE Reliability Test System公开资料/常见学术资源库获取。文中补充使用的报价和需求曲线来自两篇公开发表的期刊论文，可经由期刊/DOI获取；核心结果表完全基于该公开benchmark系统。
- Decision: 客观指标方面：核心成功指标为make-whole payments、市场价格、罚金和计算时间，均为确定性可审计的货币/技术数值，不依赖主观评判；提升目标为最小化或消除make-whole payments。唯一核心目标方面：研究问题、设计目标和贡献声明围绕定价规则PE-A/PBE-A对客观指标的改进展开，理论不可能性证明是设计动机而非并列核心目标。Benchmark方面：全文在第6节明确将IEEE RTS-96称为广泛使用的benchmark数据集，并在评价语境中作为核心实验场地；与IP、ELMP、AIC等明确参照点比较，结果直接支撑核心改进主张。数据集方面：IEEE RTS-96是公开标准测试系统，核心结果表完全基于该公开benchmark，满足公开可查、可获取且支撑核心主张。因此三个模块均通过，strict_include=true。
- Confidence: 0.88

## Toward Sustainable Electricity Markets: Capacity-Based Pricing for Electric Vehicle Smart Charging

- Year/journal: 2026 / Information Systems Research
- DOI: 10.1287/isre.2023.0078
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "RMSE（均方根误差）", "measurement_cn": "实际充电负荷与期望负荷曲线的均方根误差，单位MWh，由模拟输出计算", "objectivity_reason_cn": "基于数值比较的确定性工程指标，不依赖主观判断"}, {"name_cn": "峰值负荷（Peak）", "measurement_cn": "观察到的最大充电需求，单位MWh", "objectivity_reason_cn": "电网负荷的直接测量值，可审计"}, {"name_cn": "峰均功率比（PAPR）", "measurement_cn": "峰值平方除以均方根平方，反映需求波动性", "objectivity_reason_cn": "由负荷曲线计算的客观数学指标"}, {"name_cn": "收入偏差（Revenue deviation）", "measurement_cn": "实际收入与目标收入的百分比偏差", "objectivity_reason_cn": "基于价格与电量乘积的货币值，可审计"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: Real-world charging—flat pricing | Rate-independent scenario—variable pricing | Increasing-block pricing
- Benchmark evaluation: 在模拟测试床中，将所提出的容量定价（AH/CH及其-Distrib变体）与三个基准比较。表格2/4/5报告RMSE、PAPR、峰值，显示CBP-CH实现最低RMSE（0.02/0.03/0.21）和接近1的PAPR，远优于基准。
- Dataset status: named_public_dataset_central
- Named datasets: CBS (Centraal Bureau voor de Statistiek) Netherlands mobility data | EPEX European Power Exchange wholesale electricity prices
- Dataset obtainability: CBS数据可通过荷兰统计局开放数据平台免费获取；EPEX批发电价可通过欧洲电力交易所公开数据服务或订阅获取（公开商业订阅渠道）。
- Decision: 文中核心目标为通过容量定价诱导期望充电负荷曲线，所有评估指标（RMSE、峰值、PAPR、收入偏差）均为可审计的客观指标，无主观构念，且客观指标提升是唯一核心贡献。实验部分明确使用'benchmark'一词描述对三个基准的系统化比较，比较结果直接支撑核心改进主张。用于校准模拟的核心数据为CBS公开数据和EPEX公开市场电价，均可通过公开渠道获取，且这些公开数据支撑了主要结果表。虽然PV数据来源未完全公开，但该场景未用于与基准比较的核心主张，且主要benchmark对比场景基于公开数据。因此满足三个模块。
- Confidence: 0.88

## A personalized paper recommendation method considering diverse user preferences

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113546
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "Precision/Recall（Top-N推荐命中率）", "measurement_cn": "在公开Aminer/DBLP数据上，以最新年份论文作者作为目标用户，将用户参考文献作为正例，使用5折交叉验证，计算公式为Precision=TP/(TP+FP)，Recall=TP/(TP+FN)。", "objectivity_reason_cn": "推荐是否命中用户参考文献列表是可由公开书目/引文数据确定性判断的事实；指标由固定公式计算，不依赖用户自评、专家评分或语义好坏判断。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: AMiner | DBLP
- Benchmark evaluation: 在AMiner和DBLP两个公开学术数据集上，将PRHN与BC、CC、MSCN、CAR、Metapath五种baseline方法比较Top-N推荐性能；主结果图（Fig.6、Fig.7）显示PRHN在Precision和Recall上优于baseline。
- Dataset status: named_public_dataset_central
- Named datasets: AMiner | DBLP
- Dataset obtainability: AMiner是公开学术引文数据集，可通过AMiner官网公开下载；DBLP是公开书目数据库，可从dblp.org公开获取。两者均为学术界广泛使用、可独立查证和获取的标准数据源。
- Decision: 文章以Top-N推荐的Precision和Recall两个确定性客观指标为核心目标，全文没有主观量表、专家评分或并列的理论/政策贡献；在公开命名的AMiner和DBLP数据集上，以BC、CC、MSCN、CAR、Metapath为baseline进行系统化基准对比，benchmark评价直接支撑核心性能提升主张；两个数据集均公开可查、可获取且核心结果表完全基于它们。因此三模块均通过。
- Confidence: 0.85

## Capital shortfall: A multicriteria decision support system for the identification of weak banks

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113526
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "总体分类精度（OCA）、平均分类精度（ACA）、灵敏度（SENS）、特异度（SPEC）、AUROC、KS距离", "measurement_cn": "将UTADIS模型对76家美欧大型银行的季度观测分类为“需要资本注入/无需资本注入”，与实际监管压力测试结果及资本注入事实标签比较，按公式计算各分类性能指标（见4.2节）。", "objectivity_reason_cn": "标签来自Fed、EBA/ECB等监管压力测试和实际资本注入的公开可审计事件，属于外部可核验事实；所有性能指标按客观公式从混淆矩阵和评分分布计算，不依赖人的感受或语义判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 第5.1节（Comparison with other measures）将UTADIS（S1规格）与逻辑回归、SRISK和Texas Ratio在Global/U.S./Europe样本上就OCA、ACA、SENS、SPEC、AUROC进行系统比较；Table 9显示UTADIS在所有区域和测试方式下均优于各基准。
- Dataset status: publicly_described_source_central
- Named datasets: V-Lab SRISK | NUS Credit Research Initiative (CRI) PD/AS | IMF Country Level Core Financial Soundness Indicators (FSI) | World Bank Global Financial Development Database (GFDD) | Bloomberg
- Dataset obtainability: IMF FSI和World Bank GFDD为免费公开下载；V-Lab公开提供SRISK估算；NUS CRI公开其PD和AS数据；Bloomberg通过机构订阅获取（学术界普遍可获取）；监管压力测试与资本注入名单和结果由监管机构公开。独立研究者可依据论文来源和在线附录（Table A3/A4）重建样本。
- Decision: 客观指标：核心目标是构建基于UTADIS的DSS以识别可能面临资本需求的弱银行，标签来自监管压力测试和资本注入事实，评价指标全部为客观分类性能指标（OCA、ACA、SENS、SPEC、AUROC、KS），且无主观量表或并列核心贡献。Benchmark：全文存在明确的benchmark表述（引言‘we benchmark the UTADIS model against logistic regression’，第5.1节比较部分），且在评价语境中与LR、SRISK、Texas Ratio等明确参照点比较，结果证据支持UTADIS提升预测精度的核心主张。数据集：所有数据来源均可在全文识别且公开可获取（V-Lab、NUS CRI、IMF FSI、World Bank GFDD、Bloomberg；监管事件公开），核心结果表完全基于这些公开来源组装的样本。三个模块均通过，strict_include=true。
- Confidence: 0.85

## Network projection-based edge classification framework for signed networks

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113321
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "Accuracy（分类准确率）", "measurement_cn": "正确预测的未标记边数除以未标记边总数（TP+TN)/(TP+FP+TN+FN)）", "objectivity_reason_cn": "以公开数据集中已存在的边符号标签作为事实真值，预测结果与真值比对，不依赖人类对质量、价值或感受的语义评价。"}, {"name_cn": "Geometric Mean（几何均值）", "measurement_cn": "sqrt(TPR * TNR)，综合真阳率和真阴率", "objectivity_reason_cn": "由分类混淆矩阵中的事实计数计算，客观可复算。"}, {"name_cn": "Diagnostic Odds Ratio（诊断优势比）", "measurement_cn": "TPR/(1-TNR) * TNR/(1-TPR)，等价于 TP*TN/(FP*FN)", "objectivity_reason_cn": "完全由客观分类结果计数构成，不涉及主观评价。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: Epinions | Slashdot Zoo | Wikipedia RfA | Yeast GIN
- Benchmark evaluation: 在四个公开数据集上（平衡/非平衡预处理后），以 60%、65%、70%、75%、80% 的标记边作为已知信息，对比 NPECF、SRWR、NbA 三类方法，报告 Accuracy、Geometric Mean、Diagnostic Odds Ratio。结果显示 NPECF 在绝大多数设置下高于 SRWR 和 NbA。
- Dataset status: named_public_dataset_central
- Named datasets: Epinions | Slashdot Zoo | Wikipedia RfA | Yeast GIN
- Dataset obtainability: Epinions、Slashdot Zoo、Wikipedia RfA 是符号网络研究中的公开标准数据集，可通过 Stanford SNAP 等公开渠道获取；Yeast GIN 可从 BioGRID 公开数据库获取。原始数据均公开可查、可下载；论文虽未给出直接 URL，但数据集名称足以让独立研究者检索和获取。
- Decision: 该文以符号网络边分类中 Accuracy、Geometric Mean、Diagnostic Odds Ratio 三个客观分类性能指标为唯一核心目标和贡献；没有主观量表或并列理论贡献。论文明确命名 Epinions、Slashdot Zoo、Wikipedia RfA、Yeast GIN 四个公开标准数据集作为评价场地，并在实验中与 SRWR、NbA 等明确参照方法比较，benchmark 评价直接支撑核心提升主张。这四个数据集均公开可查、可获取，且核心结果表基于这些数据。因此三个模块全部通过。
- Confidence: 0.85

## Simpler is better: Lifting interpretability-performance trade-off via automated feature engineering

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113556
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "AUC（测试集上的曲线下面积）", "measurement_cn": "在 OpenML 各数据集的 10 个 train/test 划分上计算 AUC，比较 vanilla logistic regression、supervisor gbm/svm 与 SAFE refined logistic regression。", "objectivity_reason_cn": "AUC 基于真实类别标签的预测排序质量，是可用审计指标，不依赖人的语义评价或主观体验。"}, {"name_cn": "模型复杂度/可解释性（参数数量倒数）", "measurement_cn": "线性回归系数个数（含截距）、SVM 支持向量数、GBM 树数乘以 4，以参数数量倒数作为 interpretability 的定量代理。", "objectivity_reason_cn": "参数数量由模型结构确定，可机械计数，属于技术/可审计事实；全文未采用主观评分或用户感知评价。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: OpenML100 collection | OpenML task 31 / credit-g (German Credit)
- Benchmark evaluation: 在 30 个 OpenML100 二分类数据集上，按每个数据集的 10 个 train/test 划分训练 vanilla logistic regression、default/tuned gbm、default svm 及对应的 SAFE refined logistic regression，报告 AUC 和标准差；同时用参数数量倒数衡量 interpretability，并通过 Wilcoxon 检验比较 AUC 与可解释性。结果用于支持 SAFE 能提升简单模型表现、维持性能并显著提升可解释性的核心主张。
- Dataset status: named_public_dataset_central
- Named datasets: OpenML100 datasets (OpenML database) | credit-g / German Credit (UCI/OpenML task 31)
- Dataset obtainability: OpenML100 是公开的机器学习数据集协作平台，独立研究者可通过 OpenML 网站或 API 获取数据集及任务划分；credit-g 也来自 UCI/OpenML 公开仓库。论文还在 GitHub (https://github.com/agosiewska/SAFE-experiments) 公开了全部 benchmark 与 use case 代码。
- Decision: 核心评价完全基于客观指标：AUC 表现和参数数量倒数化的可解释性。论文的核心目标是同时提升/保持这两个客观指标，没有主观量表、用户调研或理论机制作为并列核心贡献。全文在实验部分明确使用 OpenML100 作为命名 benchmark，并与 vanilla logistic regression、默认/调优 gbm、默认 svm 等明确参照进行比较。核心结果表基于公开可获取的 OpenML/UCI 数据集，且代码公开。因此三个模块均通过，strict_include=true。
- Confidence: 0.85

## Automated Analysis of Changes in Privacy Policies: a Structured Self-Attentive Sentence Embedding Approach

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2024/17115
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "Micro-averaged F1-score", "measurement_cn": "在OPP-115 3,749个数据实践段落上，使用5×2交叉验证计算的micro-averaged F1-score", "objectivity_reason_cn": "由固定标签（OPP-115数据实践类别）及确定性的分类性能公式计算，与人类主观偏好无关"}, {"name_cn": "Micro-averaged precision, recall, hamming loss", "measurement_cn": "同样在OPP-115上的5×2交叉验证评估，使用precision/recall/HL公式", "objectivity_reason_cn": "基于固定标签与可审计的统计公式，属于客观技术性能指标"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: OPP-115
- Benchmark evaluation: 在OPP-115上，SAAS与5种传统ML模型、10种DL/attention模型、3种消融变体和自动分割方法进行4组benchmark比较；主要结果是SAAS在micro-averaged F1等指标上以统计显著优势胜过所有基准模型并用于支撑核心性能提升主张。
- Dataset status: named_public_dataset_central
- Named datasets: OPP-115
- Dataset obtainability: OPP-115由卡内基梅隆大学Usable Privacy Policy Project开发并在其项目网站公开提供，属于可在公开渠道查找到可获取的学术数据集；论文提供了完整名称和构成描述，独立研究者可凭论文信息检索到该数据集。
- Decision: 本文核心是构建并评价SAAS自动标注方法，在公开的OPP-115数据集上与多个ML/DL基准模型进行benchmark实验，以F1等客观指标证明提升；无主观满意度等成功指标，设计原则与案例研究为衍生贡献，不影响唯一核心目标；明确的benchmark表述位于方法/实验部分且使用显式比较对象；OPP-115为公开可获取数据集并构成核心评价基础。
- Confidence: 0.82

## Model identification for ARMA time series through convolutional neural networks

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113544
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "AR/MA阶数识别准确率", "measurement_cn": "在10,000条已知真实ARMA(p,q)阶数的模拟时间序列上，比较CNN预测阶数与真实阶数是否一致，计算AR阶准确率、MA阶准确率以及两者同时正确的比例。", "objectivity_reason_cn": "真实阶数由模拟生成程序确定，属于可核验的事实标签；是否识别正确为确定性比较，不依赖人的感受或语义判断。"}, {"name_cn": "AR/MA阶数识别MSE", "measurement_cn": "分类阶数与真实阶数之差的平方均值，衡量识别结果围绕真实阶数的集中程度。", "objectivity_reason_cn": "由确定性数值计算得出，完全客观。"}, {"name_cn": "计算时间", "measurement_cn": "在同一CPU单核环境上分别记录AIC、BIC和CNN完成10,000条时间序列识别所需的小时数。", "objectivity_reason_cn": "计算机运行时间是可直接观测的物理量。"}, {"name_cn": "预测误差MAE/RMSE", "measurement_cn": "基于识别出的ARMA模型对未来1期和10期进行预测，计算平均绝对误差和均方根误差，并与使用真实阶数的Acme情景比较。", "objectivity_reason_cn": "预测误差由真实模拟值和预测值计算得出，属于客观可审计的数值。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在10,000条模拟ARMA时间序列（长度分别为1,000、3,000、10,000）上，将CNN与AIC step-wise、AIC full、BIC step-wise、BIC full四种传统方法比较，评价AR阶准确率、MA阶准确率、两者同时正确率、MSE、计算时间，并使用Acme（真实阶数）作为预测误差的参照。
- Dataset status: publicly_described_source_central
- Named datasets: 
- Dataset obtainability: 独立研究者可安装公开的R软件及forecast包，调用arima.sim函数，并按论文描述的Beadle-Djurić算法生成系数，从而复现相同的10,000条模拟ARMA时间序列测试集；无需专有或保密数据。
- Decision: 客观指标方面：核心指标全部为可确定性测量的客观值，包括AR/MA阶数识别准确率、识别MSE、计算时间、预测MAE/RMSE，不涉及人类主观评价。唯一核心目标：全文围绕提升ARMA模型识别准确率和速度这一客观性能目标展开，没有并列的主观或理论贡献。Benchmark方面：第4.1节明确使用“performance benchmarking”表述，将CNN与AIC step-wise/full、BIC step-wise/full在统一测试套件上比较，且该比较直接支持核心提升主张，并有明确参照点。数据集方面：虽然使用模拟数据，但测试数据由公开R包forecast的arima.sim函数和公开发表的Beadle-Djurić系数采样算法生成，属于基于公开模拟器且可复现的公开来源，核心结果表均基于该测试套件。因此三项门槛全部通过，strict_include为true。
- Confidence: 0.82

## A dynamic classification unit for online segmentation of big data via small data buffers

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2019.113157
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "运行时间", "measurement_cn": "对静态、动态、增量动态三种方法在同一数据集和阈值下测试阶段的执行秒数；通过实验计时获得。", "objectivity_reason_cn": "运行时间是可直接观测的计算资源消耗指标，不依赖人的感受或语义判断。"}, {"name_cn": "段内距离 RMSE（均值/标准差）", "measurement_cn": "计算每个新案例到所属段质心的 RMSE，再汇总为平均值和标准差，反映分割质量。", "objectivity_reason_cn": "由数值距离公式确定性计算，不依赖人类体验、偏好或语义评价。"}, {"name_cn": "最终段数/更新次数", "measurement_cn": "根据阈值、缓冲大小等参数统计运行结束时形成的段数量及更新过程。", "objectivity_reason_cn": "来自算法运行事件的确定性计数，完全客观可审计。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: UCI Occupancy-Detection dataset | Kaggle deepScapulaSSM dataset
- Benchmark evaluation: 在 UCI Occupancy-Detection 和 Kaggle deepScapulaSSM 等公开数据集上，对静态、动态、增量动态三种方法进行系统比较，报告最终段数、RMSE 均值/标准差、运行时间，并用动态无限制缓冲作为参照验证增量动态分割结果的相似性。
- Dataset status: named_public_dataset_central
- Named datasets: Lev dataset | UCI Occupancy-Detection dataset | Kaggle deepScapulaSSM dataset
- Dataset obtainability: UCI Occupancy-Detection 可通过 UCI Machine Learning Repository 公开下载；deepScapulaSSM 可通过 Kaggle 仓库公开获取；Lev 数据集有明确名称和引用来源，但全文未给出明确下载链接。核心效率与验证结果表主要基于 UCI 和 Kaggle 数据集，二者均为公开可获取数据。
- Decision: 客观指标模块通过：核心成功指标是运行时间、RMSE、段数等可直接观测的计算结果；论文唯一核心贡献是增量动态分割机制及其效率/保真度提升。Benchmark 模块通过：虽未使用 benchmark 一词，但论文明确命名 UCI Occupancy-Detection 等公开标准数据集，并以其为评价场地，与静态、动态参照方法进行系统比较，结果用于支持核心效率主张。Dataset 模块通过：UCI Occupancy-Detection 和 deepScapulaSSM 均可公开获取，且核心结果表基于这些公开数据。因此 strict_include=true。
- Confidence: 0.8

## A social investing approach for portfolio recommendation

- Year/journal: 2021 / Information & Management
- DOI: 10.1016/j.im.2021.103536
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "投资组合收益率", "measurement_cn": "30个交易日模拟交易的组合日收益累计变化，基于股票和市场历史价格（Yahoo Finance）计算", "objectivity_reason_cn": "收益率由市场价格直接确定，不依赖人的感受或语义评价"}, {"name_cn": "Treynor比率", "measurement_cn": "(组合收益率-无风险利率)/组合Beta，Beta根据标的与S&P500的协方差/方差计算", "objectivity_reason_cn": "基于可观察的收益率与Beta计算，属于可审计财务绩效指标"}, {"name_cn": "Jensen's alpha", "measurement_cn": "组合实际收益率减去按CAPM预期收益率（无风险利率+Beta×市场超额收益）", "objectivity_reason_cn": "由公开价格数据与公式直接计算，客观可复核"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: no-filter recommendation | knowledge-based recommendation | authority-based recommendation | S&P 500 market index
- Benchmark evaluation: 在eToro帖子和财务数据基础上构建组合，用30个交易日模拟交易；以S&P500为市场基准，以无过滤、仅知识、仅权威三种推荐方法为代表基准方法，比较组合收益率、Treynor比率和Jensen's alpha；CIR在多数绩效指标上优于其他基准。
- Dataset status: named_public_dataset_central
- Named datasets: eToro.com social investing platform posts | WRDS database (financial statement data) | Yahoo Finance (stock and market price data)
- Dataset obtainability: eToro.com是公开的社交投资平台，论坛帖子为公开用户生成内容，可访问平台查看/爬取；WRDS为学术界广泛订阅的金融数据库，可通过机构订阅获取；Yahoo Finance通过公开网站或API获取历史价格。三者均符合公开可查可获取的数据来源。
- Decision: 核心成功指标为组合收益率、Treynor比率和Jensen's alpha，全部是客观可审计财务绩效，且全文唯一核心目标是构建并验证能提升这些指标的投资组合推荐机制；第5节明确用'benchmark approaches'表述并列出无过滤、知识型、权威型三种基准与S&P500进行比较，评价与核心提升主张直接相关；核心评价所用数据来自公开的eToro.com平台、WRDS数据库和Yahoo Finance，均可识别并可获取。三个模块均通过，严格纳入。
- Confidence: 0.8

## Estimating Life Cycle Sales of Technology Products with Frequent Repeat Purchases: A Fractional Calculus-Based Approach

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1131
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "销售拟合优度与预测准确度", "measurement_cn": "基于实际产品销售额数据，计算R²、MAPE、SSE、MSE等；对比不同模型在同一数据集上的这些数值", "objectivity_reason_cn": "销售额、销售量及相应统计误差指标均为可审计的客观事实，不依赖人的感受或语义评价"}, {"name_cn": "采用趋势恢复准确度", "measurement_cn": "利用DVD播放器采用数据与销售数据比较，通过两步法或GDMR-sales过程估计采用参数，并以R²/SSE与基准模型比较", "objectivity_reason_cn": "采用率、家庭渗透率、人口数据均为外部可核验事实，评估过程为固定计算规则"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: Bass-KB-BHL | Bass-KB-Steffens
- Benchmark evaluation: 在五个销售数据集（Notebook、PC、DVD Australia、iPad、Samsung tablet）上比较GDMR与两个基准模型的全数据拟合（R²/MAPE）和1/2年预测MAPE；在美国DVD播放器数据上比较拟合和8年预测MAPE；此外还与ARIMA、LSTM、KNN、Random Forest等通用预测模型比较。结果显示GDMR通常更优或大部分指标更优。
- Dataset status: publicly_described_source_central
- Named datasets: Notebook computer annual sales 2005-2014 | PC total global annual sales 2006-2015 (Statista) | DVD player sales in Australia 2003-2011 (Screen Australia) | iPad sales quarterly 2010-2017 (Apple quarterly summaries) | Samsung tablet sales 2012-2019 (Ejectejecteject/Statista) | US DVD player adoption and sales 1997-2018 (Consumer Technology Association, Digital Entertainment Group, Statista)
- Dataset obtainability: Statista可通过商业订阅获取；Screen Australia数据可在官网公开下载；Apple季度财报为公开文件；Ejectejecteject和Statista网址在参考文献中给出；CTA家庭渗透率报告和Digital Entertainment Group报告也可公开检索。独立研究者可凭论文引用信息找到并获取这些数据。
- Decision: 文章核心是提出并验证GDMR模型，目标为提升生命周期销售预测的客观准确度（R²/MAPE/SSE等），无主观量表或人类语义评价作为核心结果。全文在评价部分明确使用“Benchmark Repeat Purchase Models”，并与多个基准模型比较，支撑核心提升主张。评价所用数据均为可识别的公开来源（Statista、Screen Australia、Apple财报等），核心结果表基于这些数据。虽然结论中提及fractional integral解释的方法学/理论贡献，但该解释不是独立评价目标，未与预测提升并列为核心目标。因此，三个模块均通过，strict_include=true。
- Confidence: 0.8

## A Novel Recommendation Model for Online-to-Offline Service Based on the Customer Network and Service Location

- Year/journal: 2020 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2020.1759927
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "Precision", "measurement_cn": "在Top-30推荐列表中对测试集中实际出现过的服务评分/选择记录的命中比例，按训练/测试划分计算。", "objectivity_reason_cn": "基于可观察的服务选择/评分记录计算，不依赖用户主观评价或语义判断。"}, {"name_cn": "Recall", "measurement_cn": "测试集中目标用户实际有过评分/选择的服务中被Top-30推荐列表命中的比例。", "objectivity_reason_cn": "根据外部可观察的持出评分记录计算，构念为服务选择事实。"}, {"name_cn": "F-Score", "measurement_cn": "Precision与Recall的调和平均值，用于综合比较推荐方法性能。", "objectivity_reason_cn": "由两个客观指标计算而得，无人类主观评价成分。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: MovieLens 100K
- Benchmark evaluation: 在MovieLens 100K这一公开标准推荐数据集上评价CNRec（不含位置信息的网络推荐）及对比方法；同时在Dianping O2O数据上评价CNLRec/CNRec/LRec。结果显示CNLRec和CNRec在低数据密度条件下显著优于CF、MF、DL、CL、NN等方法。
- Dataset status: named_public_dataset_central
- Named datasets: MovieLens 100K | Dianping 官方公开网站数据 | Google Maps 地理数据
- Dataset obtainability: MovieLens 100K可通过Grouplens公开页面直接下载；Dianping为公开的O2O平台，论文给出官网URL，数据从公开网站获取；Google Maps为公开地理信息服务。独立研究者可依据论文信息查到并获取至少MovieLens 100K公开数据集。
- Decision: 该文以Precision、Recall、F-Score等完全客观的推荐性能指标为唯一核心成功标准，研究问题、实验设计和贡献声明均围绕提升推荐性能展开；全文在实验部分以MovieLens 100K作为明确命名的公开基准评价场地，并与广泛使用和最新推荐方法进行对比，构成对核心提升主张的证据；核心对比结果包含公开可获取的MovieLens 100K数据集，因此三个模块均通过。
- Confidence: 0.78

## Assuring quality and waiting time in real-time spatial crowdsourcing

- Year/journal: 2023 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113869
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "平均等待时间", "measurement_cn": "根据仿真中的任务开始时间、工人开始时间和预测行程时间计算，公式为平均 W_ij = (st_i - st_j) + s_ij。", "objectivity_reason_cn": "等待时间是可客观测量的时间变量，不依赖人的主观判断。"}, {"name_cn": "平均信誉值", "measurement_cn": "计算被选中工人的信誉值 r_i 的平均值；信誉值在仿真中按正态分布生成，代表工人可靠性的数值属性。", "objectivity_reason_cn": "信誉值是系统设定的数值变量，计算确定且可审计，不是人类对结果质量的主观评分。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: GAIA open dataset（滴滴GAIA开放数据集）
- Benchmark evaluation: 在GAIA开放数据集（成都2016年11月订单数据）上构建仿真任务分配场景，将TP-TASC与RB-TPSC基线对比，考察不同任务半径、任务有效期、工人有效期和工人平均信誉下的平均等待时间、平均信誉值、平均成本、分配率和平均行驶距离。
- Dataset status: named_public_dataset_central
- Named datasets: GAIA open dataset
- Dataset obtainability: GAIA开放数据集由滴滴出行公开提供，独立研究者可通过论文中的网址或公开渠道注册/申请后下载；属于公开可获取的标准开放数据。
- Decision: 该文提出TP-TASC框架，核心目标是降低平均等待时间并提高结果质量（以平均工人信誉值衡量），两个指标均为可客观计算的数值，没有以用户满意度、专家评分等主观构念作为核心成功标准；实验在公开可获取的GAIA开放数据集上构建，并与明确的基线方法RB-TPSC比较，评价结果直接支撑核心提升主张；因此三个模块均通过。
- Confidence: 0.78

## Augmenting Social Bot Detection with Crowd-Generated Labels

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1136
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "社交机器人检测性能（Precision、Recall、F1、AUC）", "measurement_cn": "Reddit账号级二分类；将模型预测与由r/BotWatchman社区多人举报（至少10次报告）形成的机器人标签比对，计算precision、recall、macro/micro F1、AUC；另报告时间-检测仿真和不同crowd label数量下的检测率。", "objectivity_reason_cn": "目标是识别账户是否为自动化社交机器人这一外部事实类别，属于事实标签上的检测性能；指标由预测标签与ground truth按确定公式计算。主题、情感、言语行为等人工标注仅作为中间特征，不构成核心成功构念。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: Cresci et al. (2017) social spambot Twitter benchmark data set
- Benchmark evaluation: 核心实验在Reddit自建数据上对比传统模型与增强模型（Table 6），并用受限特征集对模型进行benchmark消融（Table 7），证明加入言语行为特征带来性能提升；在公开Cresci数据集上与Garcia-Silva等的BERT基线进行直接benchmark，验证基础模型和两个额外可实现特征的表现可比较或略优。
- Dataset status: publicly_described_source_central
- Named datasets: Reddit公开API数据（r/BotWatchman社区维护bot名单） | Cresci et al. (2017) Twitter social spambot data set（次要benchmark）
- Dataset obtainability: 独立研究者可免费注册Reddit账号、生成API key，并通过Reddit官方公开API检索对话和回复数据；r/BotWatchman是一个公开subreddit，其社区bot名单可公开访问。Cresci et al. (2017)的Twitter bot数据集也通过公开学术渠道可获取。核心结论表（Table 6-10）基于这些公开可获取的数据。
- Decision: 客观指标：核心目标是提升社交机器人检测性能，目标标签是外部事实类别的bot标签，评价指标为Precision/Recall/F1/AUC，完全客观；言语行为等人工标注仅作为中间特征。唯一核心目标：全文围绕crowd reaction增强检测性能展开，speech act是机制而非并列核心贡献，不存在主观成功标准或理论/政策并列贡献。Benchmark：评价语境中存在明确的benchmark/benchmarking表述（受限特征集benchmark消融和Cresci/Garcia-Silva直接benchmark），有明确参照点，并用于支持核心性能提升主张。数据集：核心评价数据来自Reddit公开API和r/BotWatchman公开社区名单，公开可查、可获取，且主要结果表均基于该数据；次要benchmark使用公开Cresci数据。因此三项门槛均通过，strict_include=true。
- Confidence: 0.78

## What reveals about depression level? The role of multimodal features at the level of interview questions

- Year/journal: 2020 / Information & Management
- DOI: 10.1016/j.im.2020.103349
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "抑郁严重程度预测误差（PHQ-8 分数的 MAE 与 RMSE）", "measurement_cn": "模型预测的个体抑郁水平（PHQ-8 分数）与实际 PHQ-8 分数之间的 MAE 和 RMSE；采用五折交叉验证并取平均结果。", "objectivity_reason_cn": "抑郁状态/严重程度属于可外部核验的疾病状态事实标签；PHQ-8 是标准化临床问卷得分，不是用户满意度、审美、语义质量或个人偏好的主观评价。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: DAIC-WOZ
- Benchmark evaluation: 在 DAIC-WOZ 的142名受访者、7866条问题级回答上，用五折交叉验证训练两层模型，并与单模态/双模态基线（B1）和个体层基线（B2_SVR/B2_RF）比较，报告 MAE/RMSE 并进行 t 检验。
- Dataset status: named_public_dataset_central
- Named datasets: DAIC-WOZ
- Dataset obtainability: DAIC-WOZ（Distress Analysis Interview Corpus）是公开研究语料库，由 USC ICT 发布，并用于 AVEC 相关抑郁检测挑战；独立研究者可通过 USC/挑战官网申请获取（通常需签署研究用途协议），并非仅限公司内部或保密渠道。
- Decision: 核心指标是 PHQ-8 抑郁严重程度预测的 MAE/RMSE，属于疾病状态事实标签上的客观性能提升；研究目标、模型设计和贡献声明均围绕提升抑郁检测性能展开，不存在并列的主观或理论核心目标；评价以公开标准数据集 DAIC-WOZ 为基准，并与明确的基线模型比较；DAIC-WOZ 作为公开研究语料库可通过研究申请获取，因此三项门槛均通过。
- Confidence: 0.78

## Different but the Same? An Event-Driven Approach to Determine Probabilities of Data Duplication

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2025/18178
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "F1-measure（重复检测分类性能）", "measurement_cn": "基于 gold standard 判定重复/非重复后计算 precision、recall 的调和平均；使用五折交叉验证和微平均。", "objectivity_reason_cn": "重复/非重复状态是可审计的事实标签，不依赖参与者的主观感受或语义评价；F1 是确定性计算指标。"}, {"name_cn": "ROC AUC（区分度）", "measurement_cn": "根据估计的重复概率与 gold standard 绘制 ROC 曲线并计算 AUC。", "objectivity_reason_cn": "估计概率与事实标签比较，客观可复现。"}, {"name_cn": "可靠性得分/校准曲线", "measurement_cn": "将估计概率分箱后与 gold standard 中的实际重复频率比较，计算均方偏差（Murphy score）。", "objectivity_reason_cn": "估计概率和事实标签均为客观可核验值，不依赖主观判断。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: CENSUS | BABY | BIKES | BOOKS | COSMETICS
- Benchmark evaluation: 在公开标准数据集 CENSUS、BABY、BIKES、BOOKS、COSMETICS 以及私有 INSUR1/INSUR2 上评价本文方法（Partitioning、KDE、KDE+附加数据、KDE+语言模型），以 F1-measure 为主，与 Febrl、RLTK、AWS AutoGluon、Microsoft AutoML、商业工具等方法比较；另用 INSUR1 上训练的模型迁移到 INSUR2/CENSUS 并与文献结果比较。
- Dataset status: named_public_dataset_central
- Named datasets: CENSUS | BABY | BIKES | BOOKS | COSMETICS
- Dataset obtainability: CENSUS 可通过 Loster et al. (2021) 的公开资料获取；BABY、BIKES、BOOKS、COSMETICS 是 Primpeli & Bizer (2020) 发布的公开实体匹配基准数据集，可从公开项目/仓库下载，含公开 gold standard。INSUR1/INSUR2 为保险公司私有数据，不可公开获取；但核心提升主张的主要结果表 Table 7 同时且显著基于公开数据，且 E2/E3 的多个结果以公开数据支撑。
- Decision: 客观指标模块通过：核心成功指标为重复检测的 F1、AUC、可靠性，均基于可审计的重复/非重复事实标签，无主观构念作为成功标准。唯一核心目标是通过事件驱动概率模型提升客观检测性能；理论定义和适用性检查是辅助。Benchmark 模块通过：在公开标准数据集 CENSUS、BABY、BIKES、BOOKS、COSMETICS 上进行系统评价，并与多个 baseline/SOTA 比较，结果表支撑核心提升主张。数据集模块通过：公开数据可识别、可获取，且是主要结果表的核心组成部分；私有保险数据不否定公开数据对核心主张的支撑。
- Confidence: 0.72

## Predicting Labor Market Competition: Leveraging Interfirm Network and Employee Skills

- Year/journal: 2020 / Information Systems Research
- DOI: 10.1287/isre.2020.0954
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "AUC（ROC曲线下面积）", "measurement_cn": "基于测试期2013-2014年企业对的真实未来员工流动（HCF）二值标签与模型预测概率计算，见Table 6。", "objectivity_reason_cn": "标签来自可观测的雇员职业流动记录，AUC是客观分类性能指标，不依赖人的感受或语义评价。"}, {"name_cn": "新劳动力市场竞争者识别比例（proportion of new future competitors identified）", "measurement_cn": "针对测试集中首次出现HCF的企业对，按训练集先验概率阈值判定是否识别为竞争者，见Table 7。", "objectivity_reason_cn": "结果是基于真实新增雇员流动事件的比例计算，客观可审计。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 论文在自建的企业对年度面板上，比较KNN、LR、SVM、CART、Bag(LR)、Bag(SVM)、RF、MLP、CNN等模型，并在经济、产品重叠、劳动力重叠、网络重叠四类特征集上增量比较；核心证据为Table 6的AUC提升以及Table 7的新竞争者识别比例提升。
- Dataset status: publicly_described_source_central
- Named datasets: LinkedIn公开个人资料 | Yahoo BOSS API | Compustat North America数据库
- Dataset obtainability: LinkedIn公开个人资料可通过公开搜索/API按论文描述的关键词查询获取；Yahoo BOSS是公开搜索API；Compustat是公开商业订阅数据库，学术界普遍可获取。独立研究者可依据论文描述复现数据收集流程。
- Decision: 客观指标方面，核心结果变量为客观可观测的未来雇员流动HCF，评价指标AUC和识别比例均客观，且预测性能提升是全文唯一核心目标与贡献；benchmark方面，虽无命名公开基准任务，但在评价语境中明确将KNN描述为benchmark，并与多类baselines和随机分类器比较，构成核心证据；数据集方面，核心评价基于公开可获取的LinkedIn公开个人资料、Yahoo BOSS API和Compustat订阅数据，论文明确描述获取方式且结论强调只用公开数据。三个模块均通过。
- Confidence: 0.68
