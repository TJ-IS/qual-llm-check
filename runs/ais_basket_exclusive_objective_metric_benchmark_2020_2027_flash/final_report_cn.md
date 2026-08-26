# AIS Basket 全库筛选报告：唯一客观指标提升 + 明确 Benchmark 表述（全部年代）

- 运行目录：`runs/ais_basket_exclusive_objective_metric_benchmark_2020_2027_flash`
- 语料：`database_fulltext_all`，1900–2026，共 **13,910** 篇完整全文；1 篇文件名无年份未纳入，实际判定 **13,909** 篇
- 模型：`deepseek-v4-flash`，temperature=0，max_tokens=40000；复用 2020–2027 轮 2,475 条判定（提示词相同）
- 判定：`strict_include = objective_metric.pass AND benchmark.pass`
- 结果：13,909 篇全部完成，重试后 0 失败；**315 篇纳入**（含 2020–2027 的 88 篇），13,594 篇排除
- 客观指标模块通过：860 篇；benchmark 模块通过：516 篇

## 纳入文献按期刊分布

- Decision Support Systems: 218
- Information Systems Research: 46
- MIS Quarterly: 24
- Journal of Management Information Systems: 14
- Information & Management: 8
- Journal of the Association for Information Systems: 5

## 纳入文献按年代分布

- 1991: 1
- 1994: 2
- 1996: 2
- 1997: 3
- 1998: 3
- 1999: 3
- 2000: 2
- 2001: 1
- 2002: 3
- 2003: 2
- 2004: 9
- 2005: 3
- 2006: 9
- 2007: 12
- 2008: 12
- 2009: 12
- 2010: 8
- 2011: 15
- 2012: 22
- 2013: 12
- 2014: 15
- 2015: 12
- 2016: 12
- 2017: 19
- 2018: 14
- 2019: 19
- 2020: 20
- 2021: 21
- 2022: 11
- 2023: 14
- 2024: 9
- 2025: 10
- 2026: 3

## 315 篇纳入清单

### Communication requirements and network evaluation within electronic meeting system environments 

- 年份/期刊：1991 / Decision Support Systems
- DOI：10.1016/0167-9236(91)90074-l
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：响应时间；配置成本
- Benchmark 状态：benchmark_comparison_central
- 参照点：IBM LAN Program 作为 Novell Advanced NetWare 的对照软件；IBM PS/2 Model 50、60、80 三种网络服务器互为配置参照；5种用户规模（4/7/10/15/20）作为负载条件参照；4种文件大小（250B/1K/10K/100K）作为传输量条件参照
- Benchmark 表述引文：摘要：'We then use this approach to benchmark the performance of two Local Area Network (LAN) operating systems (IBM LAN program and Novell Netware) and three network servers (IBM PS/2 models 50, 60 and 80) in one EMS environment.'；第3节指出'benchmarking'是与解析建模、仿真并列的第三种性能研究方法；第4节标题为'Benchmarking Methodology'，并在4.1明确'Benchmarking Strategy'。
- Benchmark 评价：文章在真实EMS应用环境（Group Systems的Electronic Brainstorming）和可复制的DOS文件传输测试中，对5种LAN配置（IBM/50、IBM/60、IBM/80、NOV/50、NOV/60）在4、7、10、15、20个用户以及250字节、1K、10K、100K文件大小条件下进行响应时间基准测试。结果显示Novell Netware在响应时间上显著快于IBM PC LAN Program，NOV/50配置在成本和性能上最优。
- 判定理由：客观指标方面，核心成功指标为响应时间，由系统时间戳和程序日志直接测量，不涉及人类主观评价；成本和性价比亦为客观事实。核心目标方面，全文以LAN配置的基准比较和响应时间提升为核心，通信需求与方法讨论只是测试参数和框架支撑，未构成并列核心贡献。Benchmark方面，作者明确使用benchmark/benchmarking表述，在第4、5、6、7节将基准比较作为核心评价，且与IBM PC LAN、不同服务器、不同负载条件等明确参照点比较。三模块均通过，strict_include为true。
- 置信度：0.88

### A decision support system for in-sample simultaneous equation systems forecasting using artificial neural systems 【全文无benchmark字样-需人工复核】

- 年份/期刊：1994 / Decision Support Systems
- DOI：10.1016/0167-9236(94)90020-5
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：SSE（平方误差和）；RMFE（均方根预测误差）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：Klein's Model 1
- 参照点：2SLS；3SLS；ULS
- Benchmark 表述引文：在第3.2节中明确写道：‘Klein's Model 1 is employed due to its widespread use in comparing in-sample forecast reliability associated with various simultaneous equation techniques.’ 这直接将其作为评估预测可靠性的标准基准。
- Benchmark 评价：在Klein's Model 1上，MLFFNN与2SLS、3SLS、ULS比较预测C、I、w1的SSE，结果显示MLFFNN的总SSE为32.49872，显著低于2SLS的60.97706、3SLS的73.60156和ULS的45.2069。该benchmark结果直接支撑了MLFFNN预测精度提升的核心主张。
- 判定理由：客观指标方面，论文的核心成功指标是SSE和RMFE，均为可计算的预测误差，完全客观；核心目标是通过MLFFNN提升SES样本内预测精度，全文研究、实验和贡献均围绕此展开，未发现并列的其他核心目标。Benchmark方面，论文明确使用了公开领域标准模型Klein's Model 1作为评价场地，并与2SLS、3SLS、ULS进行了明确的比较，benchmark结果直接支撑了MLFFNN预测精度提升的核心主张。因此，两个条件均满足，strict_include为true。
- 置信度：0.95

### Anticipatory pruning networks and forward checking in CLP over continuous domains 

- 年份/期刊：1996 / Decision Support Systems
- DOI：10.1016/s0167-9236(96)80008-x
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：搜索树访问节点数；约束检查次数
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：8-Queens；SEND + MORE = MONEY；GERALD + DONALD = ROBERT；Tennis puzzle；Six months blending problem；Mining problem
- 参照点：No APN（APN不激活时的Prolog式搜索基线）；Partial APN（只检查左侧分支相关约束）；Full APN（检查所有未探索叶节点的一致性子集）
- Benchmark 表述引文：摘要：'Overall, the benchmarks show the APN to be an effective forward checking mechanism...'；第3.2节：'In this benchmark, the number of nodes visited is counted cumulatively during the tree search process.'；第2.3.1节：'The benchmark results for each technique are given in the next section.'
- Benchmark 评价：作者在经典整数规划问题（如8皇后、SEND+MORE=MONEY等）和混合整数线性规划问题（六个月blending问题、mining问题）上评价minimal 2LP系统在No APN、Partial APN和Full APN三种配置下的搜索节点数和约束检查次数。结果显示Full APN和Partial APN普遍大幅减少节点数和约束检查次数，用以支持APN作为有效forward checking机制的改进主张。
- 判定理由：客观指标方面：核心评价指标为搜索树访问节点数和约束检查次数，二者均为可审计的计算痕迹，不依赖人类语义或体验评价，满足fully_objective_direct。唯一核心目标方面：论文围绕APN剪枝机制的客观效率改进展开，摘要、算法设计、测量和结论均以节点数/约束检查数的减少为成功标准，没有并列的核心主观或理论贡献。Benchmark方面：摘要和3.2节明确使用benchmark/benchmarks表述，在评价语境中系统测量APN效果；评价对象正是APN对搜索效率的核心改进主张；且No APN、Partial APN、Full APN提供了明确参照比较。因此strict_include=true。
- 置信度：0.95

### Hybrid neural network models for bankruptcy predictions 

- 年份/期刊：1996 / Decision Support Systems
- DOI：10.1016/0167-9236(96)00018-8
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：破产预测准确率（prediction accuracy）
- Benchmark 状态：benchmark_comparison_central
- 参照点：MDA；ID3
- Benchmark 表述引文：摘要：'The performance of the hybrid neural network model is evaluated using MDA and ID3 as a benchmark.' 引言：'We use MDA and ID3 methods as benchmarking tools.' 两处均将MDA和ID3作为本文系统评价的基准。
- Benchmark 评价：作者在自建韩国破产数据的三组保留样本上，将四种混合神经网络模型（MDA-assisted NN、ID3-assisted NN、SOFM(MDA)-assisted NN、SOFM(ID3)-assisted NN）与MDA、ID3进行系统比较，报告Table 6的预测准确率和Table 7的Z值显著性检验，以此证明混合神经网络模型的准确率提升。
- 判定理由：核心结果指标是破产/非破产事实标签上的预测准确率，属于客观固定事实标签的检测性能；全文唯一核心目标是提升破产预测准确率，评价结构和贡献声明均围绕此展开，无并列的主观、理论或政策目标。作者明确使用benchmark/benchmarking一词，将MDA和ID3作为基准进行比较，表6和表7的结果直接支持混合神经网络模型的准确率提升，因此满足strict_include。
- 置信度：0.92

### FILM: a fuzzy inductive learning method for automated knowledge acquisition 

- 年份/期刊：1997 / Decision Support Systems
- DOI：10.1016/s0167-9236(97)00019-5
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：预测准确率
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：Iris data；Appendicitis data；Breast cancer data；Wisconsin breast cancer data；Pima Indians diabetes data；Blood data；Bankruptcy data；Simulated data
- 参照点：DA (statistical discriminant analysis)；ID3
- Benchmark 表述引文：Section 5.2 Experimental procedures: 'We use DA and ID3 as the benchmark for evaluating FILM.'
- Benchmark 评价：在八个数据集上，FILM与判别分析（DA）和ID3作为基准进行比较；表2报告各方法的预测准确率，FILM平均0.857，高于DA的0.820和ID3的0.796，且与ID3差异在5%水平显著。
- 判定理由：该文核心目标是提升预测准确率这一完全客观的可测量指标，且是唯一核心贡献；评价中使用DA和ID3作为基准，在多数据集上通过分类准确率比较验证FILM的提升效果，满足明确benchmark表述、处于评价语境、支撑核心主张且具有明确比较对象。因此 strict_include=true。
- 置信度：0.95

### Knowledge discovery by inspection 【全文无benchmark字样-需人工复核】

- 年份/期刊：1997 / Decision Support Systems
- DOI：10.1016/s0167-9236(97)00012-2
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：规则发现完整性；规则支持度；算法复杂度/效率
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：contact lens data；congressional voting records data set；[6] 中的汽车数据（auto data）
- 参照点：完整规则集（理论界限/预定义目标）；contact lens 和汽车数据集上的平均支持度与完整规则集比较；与 ITRULE 的复杂度比较（用于效率主张）
- Benchmark 表述引文：Section 3 实验段：'the algorithm has been applied to some well-known data sets'；随后明确命名 contact lens data、congressional voting records data set 和 [6] 中的汽车数据集作为评价场地。
- Benchmark 评价：在 contact lens 数据上，INSPECT 仅漏掉 9 条可能规则中的 3 条，发现规则平均支持 3.7，完整规则集平均支持 3.3；在 congressional voting records 数据上，二类情况下发现全部 211 条二条件规则；在汽车数据上，发现超过 60% 的所有可能规则，平均支持 2.32，完整规则集平均支持 2.33。
- 判定理由：文章核心是提出并验证 INSPECT 规则发现算法，其核心结果指标——规则完整性、规则支持度和算法复杂度——均为客观可测量、可审计的值；全文没有以用户感知、满意度或语义质量评分作为核心成功标准。benchmark 门槛方面，虽然未使用字面‘benchmark’一词，但作者在实验部分明确将算法应用于 contact lens、congressional voting records 和汽车数据集等公开/领域标准数据集，并与完整规则集等理论界限进行比较，属于命名式 benchmark 评价，且该评价直接支撑了核心发现能力和完整性主张。因此客观指标门槛与 benchmark 门槛均通过，strict_include=true。
- 置信度：0.78

### Toward global optimization of neural networks: A comparison of the genetic algorithm and backpropagation 【全文无benchmark字样-需人工复核】

- 年份/期刊：1998 / Decision Support Systems
- DOI：10.1016/s0167-9236(97)00040-7
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：RMS误差（in-sample / interpolation / extrapolation）；错分个数（classification misclassifications）；网络连接数/隐藏节点数（精简架构）
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：Glass–Mackey chaotic time series；Hand(1981) classification dataset
- 参照点：Backpropagation trained neural networks（NeuralWorks/CRAY-BP，含best/worst/mean/standard deviation）；Wang (1995) monotonic neural network：4 misclassifications；Hand (1981)：7 misclassifications
- Benchmark 表述引文：Section 4：'In order to compare the effectiveness of the GA with commonly used versions of BP a Monte Carlo comparison was conducted on the following seven test problems.' 同一节又称第七个问题为'the well known Glass–Mackey chaotic time series'；Figure 6 标注了'Non Parametric Classification from Hand(1981)'。这些构成以公开标准测试任务为评价场地的明确benchmark表述。
- Benchmark 评价：在7个测试函数（含Glass–Mackey标准时间序列）上开展GA与BP的Monte Carlo比较，报告in-sample、interpolation、extrapolation的RMS误差，并用Wilcoxon配对符号秩检验比较；GA在所有问题上均显著优于BP。另在Hand(1981)分类数据上训练的GA网络将错分数从Wang(1995)的4个降至1个，并可去除冗余连接。
- 判定理由：客观指标门槛通过：核心成功指标是RMS误差、错分个数和网络连接数，均为可计算、可审计的客观结果，无主观量表或人类语义判断；唯一核心贡献是证明遗传算法作为神经网络全局优化方法在客观精度上优于BP，并可通过客观连接数指标实现精简架构。Benchmark门槛通过：虽然全文未直接使用'benchmark'一词，但明确命名了Glass–Mackey标准时间序列测试任务和Hand(1981)分类数据，并以系统化Monte Carlo比较作为核心证据，且与BP、Wang(1995)、Hand(1981)等明确参照点比较，证明GA的客观指标提升。因此strict_include=true。
- 置信度：0.85

### A transmission-constrained unit commitment method in power system scheduling 【全文无benchmark字样-需人工复核】

- 年份/期刊：1999 / Decision Support Systems
- DOI：10.1016/s0167-9236(98)00072-4
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：总发电成本（Total generating cost）；对偶间隙（Duality gap）；CPU时间（秒）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：IEEE Reliability Test System (IEEE 24-bus test problem)
- 参照点：Unconstrained case（不含输电约束）；Constrained F_l (i) 与 (ii) 两种线路容量场景；Direct approach vs Indirect approach
- Benchmark 表述引文：Section 4.1: “The first test problem is based on an IEEE test problem [7]. This test system contains 24 buses, 34 transmission lines and 32 generating units.” 该IEEE标准测试系统被明确用于评价所提算法。
- Benchmark 评价：在IEEE 24-bus标准测试系统上运行所提three-phase Lagrangian relaxation算法，报告了无约束/约束情况下的dual value、primal value、duality gap和CPU时间；并在同一测试系统上比较direct approach与indirect approach，direct方法获得更低的primal cost和更短的总CPU时间。
- 判定理由：文章核心目标是提出一个带输电约束的机组组合求解方法，以最小化总发电成本并提高求解效率。所有核心成功指标均为客观可测的物理/经济量（总成本、对偶间隙、CPU时间），没有任何主观评价或语义判断。在IEEE Reliability Test System（IEEE 24-bus标准测试系统）上进行数值评价，并与无约束情形以及indirect approach等明确参照点比较，benchmark评价直接支撑了核心改进主张。因此满足严格纳入条件。
- 置信度：0.93

### Circuit diagnosis support system for electronics assembly operations 

- 年份/期刊：1999 / Decision Support Systems
- DOI：10.1016/s0167-9236(99)00015-9
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：平均每板诊断时间；平均诊断所需测试次数；缺陷覆盖率
- Benchmark 状态：benchmark_comparison_central
- 参照点：随机测试选择规则 R；静态规则 S1（D3的静态版本）；动态规则 D1/D2/D3 之间的相互比较
- Benchmark 表述引文：Section 4.2：'A naive rule that randomly selects the next test at each stage provides a benchmark for comparison.'（随机选择下一测试的朴素规则作为比较基准）。Table 4 在该计算实验中列出了 D1/D2/D3/S1/R 的平均测试次数。
- Benchmark 评价：在多个随机生成的电路诊断问题场景中，将三种动态测试选择规则D1-D3和一种静态规则S1与随机选择规则R进行比较，评价指标是平均诊断所需测试次数。结果显示动态规则相对随机测试平均减少约50%的测试次数，相对静态规则平均减少约41%。
- 判定理由：客观指标方面，核心成功指标为诊断时间、测试次数和缺陷覆盖率，均为可审计的客观事实/计数，不涉及主观满意度、语义质量评分或专家偏好；唯一核心目标是提升电路诊断的有效性与效率，管理建议和用户反馈不是并列的核心贡献。Benchmark方面，Section 4.2明确以随机选择规则作为‘benchmark for comparison’，在评价语境中比较不同测试排序规则的平均测试次数，且结果用于支持核心的测试次数降低主张。因此两个模块均通过，strict_include=true。
- 置信度：0.75

### Discovering near-optimal pricing strategies for the deregulated electric power marketplace using genetic algorithms 

- 年份/期刊：1999 / Decision Support Systems
- DOI：10.1016/s0167-9236(99)00035-4
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：GA 解相对于 GAMS 精确最优解的社会福利误差率（%）
- Benchmark 状态：benchmark_comparison_central
- 参照点：GAMS 计算的精确最优解（optimal solution）；静态/动态/死亡惩罚函数 GA（定性比较，Section 5.2-5.4）
- Benchmark 表述引文：4.4 节：'The resulting computational results are used to benchmark the performance of genetic algorithms.'（将 GAMS 计算结果用于 benchmark 遗传算法的性能）
- Benchmark 评价：在作者随机产生的六节点电力网络测试场景（3 个测试集共 48 个问题）上，将 GA-1 结果与 GAMS 求得的 AFBP 精确最优解比较，报告各场景误差率，并讨论 static/dynamic/death penalty 等替代约束处理机制的失败表现。
- 判定理由：客观指标方面：核心成功指标是 GA 求解出的社会福利接近 GAMS 精确最优解的程度，该数值由确定性优化模型和算法计算，独立于人类感知，属于完全客观的直接指标；全文评价结构、研究问题和贡献声明均围绕这一客观性能提升，没有主观量表或并列核心目标。Benchmark 方面：作者在 4.4 节明确使用 benchmark 一词表述以 GAMS 最优解作为基准评价 GA 性能，该表述位于实验设计/评价语境，其误差率结果直接支撑'GA-1 能发现近优解'的核心主张，且以 GAMS 最优解（以及惩罚函数方法）为明确参照点。两个模块均通过，因此 strict_include=true。
- 置信度：0.85

### An effective data clustering measure for temporal selection and projection queries 

- 年份/期刊：2000 / Decision Support Systems
- DOI：10.1016/s0167-9236(00)00088-9
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：平均磁盘页访问次数/簇引用次数
- Benchmark 状态：benchmark_comparison_central
- 参照点：KEY（surrogate值相似性）；TTS（事务开始时间相似性）；VTS（有效开始时间相似性）；TTO（事务时间区间重叠度）；VTO（有效时间区间重叠度）
- Benchmark 表述引文：Section 5.1: “we have conducted an experiment that simulates the management of the contract of employment in a company and the benchmark query processing on clustered temporal data objects”；Section 5.1.2: “The benchmark queries used in the experiment are constructed with the canonical temporal query patterns mentioned before” 和 Table 3 “The benchmark queries and their frequencies”。
- Benchmark 评价：在性能评价部分，作者使用根据canonical temporal query patterns构造的一组benchmark查询，在CLARA聚类框架下比较所提出的temporal affinity（AF）与KEY、TTS、VTS、TTO、VTO等聚类度量。实验在不同数据对象数量N（5000/10000/50000/100000）和对象大小S（30/50/100/200/300字节）下运行，报告每个benchmark查询的平均簇引用次数；结果表6和图13-15显示AF在所有配置下都取得最少的磁盘页访问次数，表6还报告了KEY的较差表现。
- 判定理由：文章的核心目标是提出一种新的时间数据聚类度量temporal affinity，并通过减少时间查询处理的磁盘页访问次数来提升性能。该指标是完全客观、可测量的系统性能指标，且是全文唯一的核心目标与贡献，不存在主观构念或并列的理论/制度贡献。全文在性能评价部分明确使用了benchmark一词并构造了benchmark查询集，将其作为评价场地，并与多种已有聚类度量进行比较，结果证明了AF在客观性能指标上的提升。因此，客观指标、唯一核心目标和明确benchmark评价三个方面的门槛均通过，strict_include为true。
- 置信度：0.95

### Reliable classification using neural networks: a genetic algorithm and backpropagation comparison 

- 年份/期刊：2000 / Decision Support Systems
- DOI：10.1016/s0167-9236(00)00086-5
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：分类错误率（classification error percentage）；平方误差百分比（squared error percentage）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：PROBEN1
- 参照点：BP（反向传播）算法
- Benchmark 表述引文：摘要：'a collection of 10 benchmark real world data sets were used in an extensive Monte Carlo study that compares backpropagation BP with the GA for NN training.' 第4节实验设计：'this benchmark data with rules and conventions PROBEN1 is used for this comparison.'
- Benchmark 评价：在PROBEN1基准套件的10个真实世界分类数据集（Cancer、Card、Diabetes、Gene、Glass、Heart、Heartc、Horse、Soybean、Thyroid）上，用BP和GA分别训练神经网络，以测试集分类错误率和平方误差百分比为主要结果指标。结果表（Table 1、3、4）显示GA在所有或几乎所有问题上均优于BP，benchmark评价直接支撑了GA提升分类性能的核心主张。
- 判定理由：客观指标方面，核心指标为测试集分类错误率和平方误差百分比，二者均由可审计的事实标签和确定公式计算，完全客观。唯一核心目标方面，全文围绕'GA在NN训练中优于BP'这一客观性能提升展开，无主观体验或理论机制等并列核心贡献。benchmark方面，明确采用公共基准套件PROBEN1的10个真实世界分类数据集，并在实验结果中将GA与BP进行系统比较，benchmark评价直接支撑核心改进主张，且存在明确参照点BP。因此两个模块均通过，strict_include=true。
- 置信度：0.98

### A case-based approach using inductive indexing for corporate bond rating 

- 年份/期刊：2001 / Decision Support Systems
- DOI：10.1016/s0167-9236(01)00099-9
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：分类准确率（weighted average classification accuracy）
- Benchmark 状态：benchmark_comparison_central
- 参照点：MDA；Inductive learning (KATE-Induction)；Nearest-neighbor (NN)；Nearest-neighbor Expert (NN_Expert)
- Benchmark 表述引文：Section 6（Results and analysis）中明确表述：‘The results of MDA and the inductive learning model using KATE-Induction are also presented as benchmarks to verify the applicability of the proposed model to the domain.’；同时Table 6使用‘Benchmark model’与‘Proposed model’的对照。
- Benchmark 评价：在韩国公司债券评级数据集（参考集3486，验证集400）上评价所提出的IND-NN模型（决策树深度3/5/7/9 + 叶内最近邻），并将MDA、KATE-Induction、最近邻（NN）、专家权重最近邻（NN_Expert）作为基准比较。Table 5显示IND-NN(2)达到70.0%的加权准确率，高于所有基准；Table 7的McNemar检验显示IND-NN(2)在1%水平显著优于每一个基准模型。
- 判定理由：客观指标：核心结果指标为债券评级预测的分类准确率；评级是由独立评级机构给出的外部可核验事实标签，准确率计算基于确定性计数，不涉及人类感受、语义评价或偏好。唯一核心目标：研究设计、评价和贡献声明均围绕通过归纳索引提升案例检索后的分类准确率；结论中的知识组合原则是对提升机制的解释，非并列核心贡献。Benchmark：结果部分明确将MDA、KATE-Induction、NN、NN_Expert作为benchmarks进行对比，并以Table 5和Table 7的对比证据证明IND-NN(2)在准确率上显著提升。三部分全部通过，因此strict_include=true。
- 置信度：0.95

### Combinatorial auctions using rule-based bids 

- 年份/期刊：2002 / Decision Support Systems
- DOI：10.1016/s0167-9236(02)00004-0
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：拍卖收入（Revenue）；分配效率（Efficiency）；最优性（Optimality）；未售库存、拍卖轮数、计算时间及gap
- Benchmark 状态：benchmark_comparison_central
- 参照点：CPLEX 6.5 exact integer programming solver on the same IP problem；ISCA自身报告的理论上界/LP松弛gap，以及CPLEX报告的对同一解的初始gap
- Benchmark 表述引文：“The solution to the integer problem presented in Section 4 acts as a benchmark against which we compare our heuristic’s performance.”（第7节 Results）
- Benchmark 评价：作者将第4节定义的整数规划问题作为基准，在缩小规模的问题（30个投标人、104个单元、3个节目；第3轮12个活跃投标人）上，将ISCA启发式与CPLEX 6.5比较。ISCA在15分钟内完成整个5轮拍卖并找到收入1728.31的解，gap小于0.04%；CPLEX运行43小时未获得可行整数解；用ISCA的解作为初始解后CPLEX 24小时未能改进，且CPLEX报告的初始gap为43.74%，远高于启发式结果。该基准评价用于支撑启发式求解质量和近似最优性的核心主张。
- 判定理由：客观指标：收入、效率、最优性、未售库存、轮数、计算时间和gap均由模拟拍卖中的明确数值和公式计算得出，不依赖人类主观评价；唯一核心目标是设计和验证接受规则化投标的ISCA机制及其胜者决定启发式，全文评价与贡献声明均围绕这些客观绩效指标。Benchmark：第7节明确将第4节的整数规划问题作为benchmark，并用CPLEX 6.5作为明确参照点进行比较；该比较支撑了启发式解接近最优且优于难以求解的精确工具的核心主张。两个模块通过，因此 strict_include=true。
- 置信度：0.85

### Design of an interactive spell checker: optimizing the list of offered words 

- 年份/期刊：2003 / Decision Support Systems
- DOI：10.1016/s0167-9236(02)00115-x
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：正确词在候选列表中的位置均值 (AV)；正确词出现在候选列表中的比例 (P_A)；正确词排在首位的比例 (P_1)；正确词位于前五的比例 (P_5)
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：MSW97 (Microsoft Word 97 spell checker)
- 参照点：MSW97 (Microsoft Word 97 spell checker)
- Benchmark 表述引文：引言："it was chosen as a benchmark to see if our approach was viable"；4.2节："Again, there was no intent to show that one program is better than the other, but only to see if model (1) is reasonable, as compared to a respected benchmark."
- Benchmark 评价：在受试者真实打字产生的266个错误词上，将SP与MSW97的候选列表按P1、P5、PA、AV指标比较；SP在P1=0.85 vs 0.74、P5=0.98 vs 0.90、PA=1.00 vs 0.92、AV=1.36 vs 2.64上全面优于MSW97，并通过假设检验。
- 判定理由：核心指标为正确词在候选列表中的命中率与平均位置，是基于预定正确词（受试者真实打字/原文转录）的可计算任务完成指标，非主观体验或语义质量评价；核心目标唯一为提升该客观拼写纠正性能。全文存在明确benchmark表述（MSW97被选为benchmark并作为比较对象），且benchmark比较结果直接支撑核心改进主张，并有明确参照点。因此两个模块均通过。
- 置信度：0.78

### An agent for selecting optimal order set in EC marketplace 

- 年份/期刊：2004 / Decision Support Systems
- DOI：10.1016/s0167-9236(03)00027-7
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：利润；完工时间（makespan）；交货期满足度；计算时间
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：MT6×6 (Muth and Thompson's job shop scheduling benchmark)
- 参照点：MT6×6已知最优解（makespan=55）
- Benchmark 表述引文：第4.3节实验部分：“To test the above formulation, we used Muth and Thompson’s [15] MT6 × 6 which is well recognized as a benchmark problem in job shop scheduling domain.” 第4.4节GA部分再次提到“MT6 × 6 benchmark problem”。
- Benchmark 评价：使用MT6×6 job shop scheduling benchmark测试IP模型，得到makespan=55，等于该benchmark的已知最优解；随后GA也在同一benchmark上得到最优解，并在更大benchmark问题上也获得最优解。该benchmark评价用于验证选择代理核心调度算法的正确性和有效性。
- 判定理由：客观指标方面：核心成功标准是利润最大化、交货期满足与完工时间，均为客观可验证的经济/物理指标，无主观评价。唯一核心目标：研究问题、模型目标、案例评价和贡献声明均围绕选择最优订单集以最大化利润展开，无并列的主观、理论或政策目标。Benchmark方面：全文明确使用MT6×6这一公开的job shop scheduling benchmark，并报告达到已知最优makespan 55，且GA在更大benchmark上也得到最优解；benchmark结果用于验证选择代理核心调度算法的有效性，支撑核心提升主张。因此strict_include为true。
- 置信度：0.72

### Applying rough sets to market timing decisions 

- 年份/期刊：2004 / Decision Support Systems
- DOI：10.1016/s0167-9236(03)00089-7
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：净收益（Net Profit）；夏普比率（Sharpe Ratio）
- Benchmark 状态：benchmark_comparison_central
- 参照点：Buy-and-hold strategy（买入持有策略）
- Benchmark 表述引文：表5标题“Performance benchmark of buy – hold strategy and original decision attribute for period Jan. 4, 1999 to Jul. 26, 1999 of S&P 500 index”；正文“The results are compared to the buy – hold strategy. The reason to choose this simple strategy as benchmark is to beat Efficient Market Hypothesis.”（Section 5, Results and discussion）
- Benchmark 评价：在S&P 500指数数据上，将基于RoughSOM/粗糙集构建的交易系统与buy-and-hold策略进行比较，报告1988–1998和1999年两个时期的net profit、Sharpe Ratio、交易次数、胜率等，并以buy-and-hold作为明确参照基准；结果显示整个1988–1999期间交易系统净收益优于buy-and-hold，结论还提到在其他三个指数上也支持该分析。另有UCI数据集上的预测精度比较（RoughSOM vs 原始rough sets），但核心benchmark评价是与buy-and-hold策略的交易绩效对比。
- 判定理由：客观指标方面：核心成功指标为净收益、夏普比率等市场交易绩效，完全客观可测量，不依赖人类语义判断；核心目标是构建并验证基于粗糙集的交易系统，以客观交易绩效提升作为唯一核心贡献，未发现并列的主观目标或独立理论/制度贡献。Benchmark方面：全文存在明确的benchmark表述（buy-and-hold strategy作为基准），位于结果与讨论部分，属于评价语境，并且该比较用于支撑交易系统绩效改进的核心主张，有明确参照点buy-and-hold，因此满足benchmark门槛。综上两个模块均通过，strict_include为true。
- 置信度：0.82

### Arbitrage pricing theory-based Gaussian temporal factor analysis for adaptive portfolio management 

- 年份/期刊：2004 / Decision Support Systems
- DOI：10.1016/s0167-9236(03)00082-4
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：组合夏普比率（Sharpe ratio）；平均收益率与风险/波动率
- Benchmark 状态：benchmark_comparison_central
- 参照点：return-based portfolio management；APT-based approach in Scenario I；modified Sharpe ratio approach in the previous subsection；original Sharpe ratio approach
- Benchmark 表述引文：第5.1.1节：'We implement the modified Sharpe ratio simulation using the same set of data described before and the APT-based approach in Scenario I as benchmark for comparison.'；第5.2.1节：'We simulate the modified Sharpe ratio with control of expected return approach and use the modified Sharpe ratio approach in the previous subsection as benchmark.'；第5.3.1节：'We simulate the modified Sharpe ratio with control of expected downside risk approach and use the modified Sharpe ratio approach in the previous subsection as benchmark.'；另外第4.2.2节为比较目的实现了return-based portfolio management作为baseline。
- Benchmark 评价：在1998-1999年香港市场522个交易日数据上（前400个训练、后121个测试）进行模拟：核心实验在四种交易场景下将APT-based组合与return-based组合比较，报告夏普比率提升（场景I +38.24%、场景II +72.69%、场景III +65.20%、场景IV +90.97%）；改进夏普比率部分以场景I的APT-based方法或上一节改进方法作为benchmark，比较改进前后的收益、风险、下行风险、上行波动和夏普比率。
- 判定理由：核心指标为组合夏普比率、收益率和风险/波动率，完全由市场数据和确定性公式计算，不包含主观评价或人类语义判断，属于完全客观指标。研究问题、设计目标、实验评价和贡献声明均围绕最大化Sharpe ratio等客观投资绩效指标，客观指标提升是唯一核心目标与核心贡献。全文在评价语境中明确使用'benchmark'一词，并以return-based组合、场景I的APT-based方法或上一节改进方法作为明确参照点，benchmark比较结果直接支撑客观绩效提升主张。因此两个模块均通过，strict_include=true。
- 置信度：0.82

### Data mining of Bayesian networks using cooperative coevolution 

- 年份/期刊：2004 / Decision Support Systems
- DOI：10.1016/s0167-9236(03)00115-5
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：平均最终MDL分数（AFS）；平均执行时间（AET）；平均结构差异（ASD）；累计提升量、预期收益等直销响应指标
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：ALARM network；PRINTD network
- 参照点：MDLEP算法；原始网络MDL分数；直销应用中的反向传播神经网络、逻辑回归模型和随机模型
- Benchmark 表述引文：第5.1节实验方法中明确写道：“All of the data sets are generated from well-known benchmark Bayesian networks, which include the ALARM network and the PRINTD network.”并将这些基准网络生成的数据集作为CCGA与MDLEP比较的评价场地。
- Benchmark 评价：在ALARM-1000/2000/5000/10000/ALARM-O和PRINTD-5000六个基准数据集上，对CCGA和MDLEP各运行40次，比较AFS、AET、ASD等客观指标。结果显示CCGA在MDL分数和结构差异上不劣于或优于MDLEP，且执行时间快3.4至5.0倍；这些benchmark结果直接支撑核心‘更有效和更高效’的改进主张。
- 判定理由：客观指标方面：核心成功指标全部是MDL分数、执行时间、结构差异、累计lift和收益等确定性可观测指标，不依赖人类感知或语义判断；唯一核心目标是提升贝叶斯网络学习的有效性和效率，不存在其他并列核心目标。benchmark方面：第5.1节明确使用ALARM和PRINTD这两个公开基准网络生成数据集作为评价场地，并与MDLEP基线比较，结果直接支持核心改进主张。因此两个模块均通过，strict_include为true。
- 置信度：0.95

### Database design in the modern organization—identifying robust structures under changing query patterns and arrival rate conditions 

- 年份/期刊：2004 / Decision Support Systems
- DOI：10.1016/s0167-9236(03)00048-4
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：查询平均处理时间；平均系统时间（处理时间+排队等待时间）；利用率/拥塞水平；相对低效/切换损失
- Benchmark 状态：benchmark_comparison_central
- 参照点：DBS1-DBS5（前五名潜在优秀结构）与DBS6（原规范化结构）；DBS7-DBS11（25th/50th/75th/87th/100th百分位结构）；每个查询模式或复杂度分组下的最优结构；不同到达率λ（1-900或1800）下各结构的系统时间
- Benchmark 表述引文：引言末尾：'based on lowest total processing time for our benchmark queries, we identify the top five performing database structures among the 96 database structures possible in our experiment.' 即“基于基准查询的总处理时间最低，识别96种数据库结构中的前五名表现者”。
- Benchmark 评价：作者构造了520个查询组成的基准查询集，涵盖52种查询类型；96种候选数据库结构均在Oracle上执行该基准集。按总处理时间选出前五名结构（DBS1-DBS5），与原规范化结构DBS6及其他代表百分位的结构比较；随后在211种查询模式和不同到达率条件下，用排队模型计算平均系统时间，识别DBS3（低复杂度组最优）和DBS1（其他组最优）作为稳健结构。
- 判定理由：核心指标为查询处理时间和系统时间，属于完全客观、可测量、不依赖人类感知或语义判断的技术绩效；全文研究问题、评价结构和贡献声明均围绕识别稳健数据库结构这一目标展开，且不存在并列主观或理论核心贡献。虽然未使用公开命名的benchmark数据集，但作者明确使用“our benchmark queries”作为评价工具，在96种结构间比较总处理时间并以DBS1-DBS5、DBS6等为参照点，评价结果支持本文关于稳健结构性能提升的核心主张，因此满足benchmark门槛。
- 置信度：0.87

### Distribution forecasting of high frequency time series 

- 年份/期刊：2004 / Decision Support Systems
- DOI：10.1016/s0167-9236(03)00083-6
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：方向准确率 (ADA)；泰尔U统计量 (Theil's U)；模拟交易利润
- Benchmark 状态：benchmark_comparison_central
- 参照点：naive forecast（前一方向） ADA 46.2%；no change forecast（Theil's U统计量分母）
- Benchmark 表述引文：第五节 Simulations 中：'To provide a benchmark for the ADA results the accuracy of another naive forecast was calculated on the data. Predicting the future movement as the previous direction of movement achieved an ADA of 46.2%.'
- Benchmark 评价：使用日元/美元高频数据集（100,000和200,000个点），AURA-FS在多种参数组合下计算ADA、Theil's U和模拟利润；与naive forecast（前一方向）的ADA 46.2%比较，最好的ADA为56.9%，最好的Theil's U为0.892（<1优于无变化预测）。
- 判定理由：客观指标方面：ADA、Theil's U和模拟利润均基于实际价格数据，可确定性计算，不依赖人类感知或语义评价，全部核心成功结果为客观。核心目标方面：全文围绕提升预测准确性和利润这一唯一核心目标展开，没有并列的主观体验、理论机制或政策建议等核心贡献。benchmark方面：作者在评价语境中明确使用'benchmark'一词，提供naive forecast作为ADA的参照点，并以此证明AURA-FS的改进（46.2% vs 56.9%），Theil's U本身也与no-change forecast比较，符合benchmark_comparison_central。因此两个模块均通过，strict_include=true。
- 置信度：0.72

### Event detection from online news documents for supporting environmental scanning 

- 年份/期刊：2004 / Decision Support Systems
- DOI：10.1016/s0167-9236(03)00028-9
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：漏报率（miss rate）与误报率（false alarm rate）
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：INCR（single-pass incremental clustering）传统基于特征的事件检测技术
- 参照点：INCR 传统基于特征的事件检测方法（Yang et al.）
- Benchmark 表述引文：摘要：‘Using a traditional feature-based event detection technique (i.e., INCR) as benchmarks, the empirical evaluation results showed that the proposed NEED technique improved the effectiveness of event detection…’；第4.2节：‘A traditional feature-based event detection technique was used to provide the desired effectiveness benchmarks. Specifically, the single-pass incremental clustering (INCR) for event detection proposed by Yang et al. was employed.’
- Benchmark 评价：在自建的来自 excite.com 的 492 篇新闻语料上，将 NEED 与传统事件检测基线 INCR 进行对比；通过 DET 曲线比较漏报率与误报率，尤其关注低漏报率区间，并据此论证 NEED 的改进。
- 判定理由：核心指标是事件检测的漏报率和误报率，属于可客观计数的事实标签检测性能；核心目标与贡献均为提升该客观检测指标，无并列的主观或理论核心贡献；全文存在明确的 benchmark 表述，作者在实证评价部分以 INCR 作为基准进行 DET 曲线比较，并以此支撑 NEED 的改进主张。因此满足全部纳入条件。
- 置信度：0.93

### Simultaneous optimization of neural network function and architecture algorithm 

- 年份/期刊：2004 / Decision Support Systems
- DOI：10.1016/s0167-9236(02)00147-1
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：均方根误差（RMSE）；网络结构简约性（隐藏节点数、零权重比例、无关变量消除率）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：Prechelt NN benchmark datasets（Building数据集，来自The Great Energy Predictor Shootout竞赛）
- 参照点：Original Genetic Algorithm (OGA)；BP3, BP6, BP12；Pruned BP networks (Prune)；Cascade Correlation (CC)
- Benchmark 表述引文：第二节实验部分：'An additional problem (Building) was included to test how well the NNSOA performed with real-world data... This problem was taken from Prechelt’s [20] paper where he collected a set of NN benchmark datasets.' 即明确将Building问题取自Prechelt收集的NN benchmark数据集。
- Benchmark 评价：在Prechelt NN benchmark的Building数据集上，NNSOA与OGA、BP（3/6/12隐藏节点）、Prune、Cascade Correlation进行RMSE比较。NNSOA在训练集和测试集上的平均RMSE均最低（如out-of-sample 5.43e-02 vs BP最低1.06e-01），并识别出人为加入的无关变量及多个额外不相关输入。
- 判定理由：该文核心目标为同时优化神经网络预测精度（RMSE）和网络结构简约性（隐藏节点、零权重、无关变量消除），所有核心指标均为客观可审计指标，不存在主观构念或并列的非客观贡献。Benchmark方面，作者明确将Building问题取自Prechelt收集的NN benchmark数据集，并在该数据集上与多种基线算法比较，结果用于支持NNSOA的核心提升主张。因此两个模块均通过，strict_include为true。
- 置信度：0.9

### A scalable decision tree system and its application in pattern recognition and intrusion detection 【全文无benchmark字样-需人工复核】

- 年份/期刊：2005 / Decision Support Systems
- DOI：10.1016/j.dss.2004.06.016
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：分类错误率（1-accuracy）；决策树大小（叶子数）；总CPU时间
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：UCI forest cover data set（U.C. Irvine数据仓库）；CART waveform data set（基于CART书中的模型生成、常用于决策树实验的标准仿真数据）；Intrusion detection data set（来自Lee & Stolfo等的网络连接记录数据，311,029条记录）
- 参照点：RainForest（作者按已发表算法实现的比较基准）；LDA（线性判别分析，天然可扩展的统计分类器）；SURPASS unpruned（剪枝前后对照）
- Benchmark 表述引文：第5节开篇明确命名评价数据：“The first data set for the pattern recognition problem is the forest cover set, taken from U. C. Irvine’s data repository”；“This simulated data set was generated based on the model described in the CART book... extensively used in decision-tree-related experimental studies”；“The intrusion detection data is taken from Refs. [15,16]”并在其后报告三组大规模实验。
- Benchmark 评价：在森林覆盖、waveform和入侵检测三个公开/标准数据集上，随机抽取10%、20%、…、100%样本，并在每个样本内以60%训练、40%测试划分，比较SURPASS、RainForest和LDA的错误率、叶子数和CPU时间；同时报告SURPASS剪枝前后的比较，并用ANOVA/Tukey检验错误率差异的统计显著性。
- 判定理由：客观指标方面，三个核心成功度量均为错误率、树大小和CPU时间，全部是外部可核验的确定性事实，不依赖人的主观判断；固定事实标签上的分类错误率属于objective_fixed_factual_labels。唯一核心目标是提出并验证可扩展的SURPASS决策树算法，提升大规模数据分类的可扩展性和分类质量，全文没有并列的理论、制度或主观体验目标。Benchmark方面，第5节明确将UCI forest cover、CART waveform和intrusion detection三个公开/标准数据集作为评价场地，并与RainForest、LDA等明确参照点比较，结果直接支撑分类质量和可扩展性主张；虽然全文未出现“benchmark”字面词，但满足命名式Benchmark表述。因此两个模块均通过，strict_include=true。
- 置信度：0.84

### On quantified weighted MAX-SAT 

- 年份/期刊：2005 / Decision Support Systems
- DOI：10.1016/j.dss.2003.12.004
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：求解时间（CPU 秒）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：QBF benchmark problems available at http://www.informatik.uni-freiburg.de/~rintanen/qbf.html；four benchmark domains: chain of implications, bomb in toilet, blocks world, 3-CNF
- 参照点：盲搜索（blind search）；H1（MMWO-1）与盲搜索对比；H2（MMWO-2）与盲搜索对比；blind search + Rule 3 与 blind search 对比
- Benchmark 表述引文：引言中明确写有“Empirical evaluation on 40 problems from four benchmark domains is reported in Section 4”；第 4 节实证部分明确写有“We used 40 problems from four benchmark domains. Since no Q-W-MAX-SAT problems are available, the 40 problems were obtained from the benchmark QBF problems available at http://www.informatik.uni-freiburg.de/~rintanen/qbf.html”。
- Benchmark 评价：在取自公开 QBF benchmark 的 40 个 Q-W-MAX-SAT 问题上，评价盲搜索、MMWO-1（H1）、MMWO-2（H2）以及 Rule 3；报告 CPU 求解时间和加速比，其中 H1 相对盲搜索加速最高 133.36 倍，H2 相对盲搜索加速最高 7.93 倍，Rule 3 对无解实例判定加速高达 381047 倍，从而直接支撑启发式/简化规则提高求解效率的核心主张。
- 判定理由：客观指标方面，论文以 CPU 求解时间为唯一核心成功指标，属于完全客观、可直接观测的技术指标；没有主观量表或人类语义评价作为核心结果。核心目标方面，论文的研究问题和贡献声明集中于高效求解 Q-W-MAX-SAT，启发式和简化规则的效果完全以求解时间/加速比评价，未提出并列的主观或理论机制贡献。Benchmark 方面，论文在明确命名的公开 QBF benchmark 来源及其四个 benchmark domains 上构造 40 个问题，并在评价语境中比较盲搜索、H1、H2 和 Rule3 的求解时间；benchmark 结果直接支撑核心效率提升主张，且有明确对照。因此两个模块均通过，strict_include=true。
- 置信度：0.85

### Using 3D interfaces to facilitate the spatial knowledge retrieval: a geo-referenced knowledge repository system 

- 年份/期刊：2005 / Decision Support Systems
- DOI：10.1016/j.dss.2004.01.007
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：任务完成正确性（effectiveness）；任务完成时间（efficiency）
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：2D system（文中称为 benchmark system）
- 参照点：2D系统，包括2D aerial photo、2D elevation map、2D semantic map
- Benchmark 表述引文：Section 4.1原文：'A 2D system was implemented as a benchmark system to be compared with the 3D interfaces developed.'
- Benchmark 评价：作者在系统评价部分构建了一个2D基准系统，与3D系统在7个任务上比较，覆盖3种空间知识与3类界面；主要结果见表3，其中任务2（路径知识）和任务6（组合界面的configurational knowledge）中3D显著优于2D，其余任务无显著差异。
- 判定理由：该文以“带交互动画的3D界面是否能达到或超过2D界面的空间知识检索性能”为核心问题，核心成功指标是任务完成正确性和完成时间，均为客观可审计结果；全文不存在主观满意度、偏好或质量评价作为核心成功标准。评价部分明确将2D系统作为benchmark system，并在多个任务上与3D系统比较有效性和效率，benchmark评价直接支撑核心性能主张。因此同时满足客观指标、唯一核心目标和明确benchmark表述三重条件。
- 置信度：0.93

### A GIS supported Ant algorithm for the linear feature covering problem with distance constraints 

- 年份/期刊：2006 / Decision Support Systems
- DOI：10.1016/j.dss.2005.09.002
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：目标A：线性要素覆盖率 μ_A；目标B：距离均衡达成度 μ_B；综合目标 λ
- Benchmark 状态：benchmark_comparison_central
- 参照点：TC-GA（Tzeng和Chen的遗传算法）；RANDOM（随机起点两阶段局部搜索）；LFCP-Ant (LS2)（仅使用第二阶段局部搜索的变体）
- Benchmark 表述引文：第5.4节：'A computational study between the LFCP-Ant and a GA proposed in [14] (i.e. TC-GA) has been carried out for benchmarking the LFCP-Ant.' 引言中也说：'A computational study between the LFCP-Ant and TC-GA in [14] is also carried out to benchmark the efficiency of LFCP-Ant.'
- Benchmark 评价：在相同的新加坡消防站选址案例上，以8次独立运行、相同3600s时间长度，比较LFCP-Ant（LS）与TC-GA、RANDOM和LFCP-Ant（LS2）。结果显示LFCP-Ant（LS）平均λ=0.633，优于TC-GA的0.505（提升25.35%）；最优λ=0.650，优于TC-GA的0.541（提升20.15%）；变异系数2.20%低于TC-GA的3.82%；收敛曲线也显示LFCP-Ant更优。该比较是支撑‘LFCP-Ant更高效、更稳健’核心主张的关键证据。
- 判定理由：客观指标方面：核心成功指标是LFCP的线性要素覆盖率和设施间距离均衡度及其综合λ，均由空间坐标、距离和栅格覆盖计数确定性计算，不依赖人类感受或语义判断；全文评价和贡献声明都围绕λ提升展开，属于完全客观且唯一的算法优化目标。Benchmark方面：作者在第5.4节以‘benchmarking the LFCP-Ant’明确陈述系统化基准比较，并将LFCP-Ant与TC-GA、RANDOM等明确参照物在相同案例和运行条件下比较，结果直接证明LFCP-Ant在λ、稳定性和收敛性上的提升，因此benchmark评价是核心证据。两个模块均通过，strict_include=true。
- 置信度：0.92

### A hybrid sales forecasting system based on clustering and decision trees 

- 年份/期刊：2006 / Decision Support Systems
- DOI：10.1016/j.dss.2005.01.008
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：均方根误差 (RMSE)；平均绝对百分比误差 (MAPE)；中位数绝对百分比误差 (MdAPE)
- Benchmark 状态：benchmark_comparison_central
- 参照点：Mean profile predictor；ZeroR；OneR；Naïve Bayesian；IBk
- Benchmark 表述引文：第5.3节：'This mean sales profile (mean predictor) will be used later as a benchmark.' 以及 'Amongst the 4 benchmark rule based methods, IBk is the most accurate one...'
- Benchmark 评价：在285个真实测试商品上评价提出的C4.5预测系统，将其与均值剖面预测器（mean profile）、ZeroR、OneR、朴素贝叶斯、IBk等六个模型进行对比，使用RMSE、MAPE、MdAPE三项误差指标评估。结果显示提出的系统在所有指标上表现最佳。
- 判定理由：文章核心目标是提高中期销售预测准确性，评价指标为预测误差（RMSE、MAPE、MdAPE），完全客观且为唯一核心贡献。第5.3节明确使用均值剖面作为benchmark，并与其他4个分类器构成基准对比，表3显示提出的系统在所有误差指标上优于所有基准。benchmark评价直接支撑了核心改进主张，因此两个模块均通过，strict_include为true。
- 置信度：0.95

### A hybrid system by evolving case-based reasoning with genetic algorithm in wholesaler's returning book forecasting 

- 年份/期刊：2006 / Decision Support Systems
- DOI：10.1016/j.dss.2006.02.014
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：慢销书预测的平均错误率（分类准确率）
- Benchmark 状态：benchmark_comparison_central
- 参照点：Model B: back propagation neural network (BPNN)；Model C: conventional CBR；Model D: multiple-regression analysis；不同参照案例数（200/300/400/500）
- Benchmark 表述引文：Section 3.2 Step 6：'Average error rate is applied as the forecasting benchmarks to evaluate the accuracy of these four models in this research.'
- Benchmark 评价：作者在台湾书商的实际904个案例数据上，以平均错误率作为评价基准，对Model A（GA/CBR）、Model B（BPNN）、Model C（传统CBR）、Model D（多元回归）进行系统化比较；在不同训练/测试分组（200/100、200/200、300/100）下重复10次，报告平均错误率和标准差（表17、19、21），并改变参照案例数观察Model A表现。
- 判定理由：客观指标通过：核心结果为慢销书这一操作性事实标签的预测平均错误率，依据实际销量阈值可审计；无主观构念进入核心成功标准。唯一核心目标通过：全文从问题、设计到贡献均围绕准确率提升。Benchmark通过：作者明确以average error rate作为forecasting benchmarks并在实验中对四个模型作系统化比较，有明确参照点，结果用于证明GA/CBR准确率更高。因此strict_include=true。
- 置信度：0.93

### A location model for a web service intermediary 

- 年份/期刊：2006 / Decision Support Systems
- DOI：10.1016/j.dss.2004.11.016
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：WSI总体期望运营成本；求解计算时间；启发式解与最优解的间隙（solution quality gap）
- Benchmark 状态：benchmark_comparison_central
- 参照点：CPLEX 8精确最优解；CPLEX 8在未求出最优解时的anytime最佳解
- Benchmark 表述引文：Section 4 数据收集与实验：'The first test bed was used to study the solution performance of DAL. We benchmarked DAL against CPLEX 8 [11] which is a general-purpose commercial integer programming package that provides exact solutions.'
- Benchmark 评价：DAL启发式与CPLEX 8精确求解器在8个问题类别（a-h，候选位置数5到40）的模拟实例上进行系统比较。结果显示DAL平均目标函数值间隙约0.38%，最大约2.88%；在25个及以上位置的问题中CPLEX常内存不足或时间过长，DAL可用更短且更稳定的计算时间获得近似最优解。该基准评价是支持“DAL heuristic provided near optimal solutions in short computer times”这一核心主张的关键证据。
- 判定理由：客观指标方面：核心指标为WSI运营成本、求解时间和与最优解的间隙，全部来自数学模型、CPU时间或精确求解器计算，不依赖人类主观判断；核心目标是构建和求解WSI服务器选址模型以最小化运营成本，并通过高效启发式在合理时间内获得近似最优解，无并列的同等核心目标。Benchmark方面：作者在实验部分明确用“We benchmarked DAL against CPLEX 8”陈述基准评价，将DAL与精确求解器CPLEX 8在多个模拟问题类别上比较，以目标函数间隙和计算时间为核心证据，支持“近最优+短时间”的核心改进主张。因此两个模块均通过，strict_include=true。
- 置信度：0.82

### A new approach to classification based on association rule mining 

- 年份/期刊：2006 / Decision Support Systems
- DOI：10.1016/j.dss.2005.03.005
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：分类准确率；生成的规则数量；执行时间
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：UCI Machine Learning Repository
- 参照点：C4.5；CBA；SVM；NN；C4.5 tree；C4.5 tree pruning
- Benchmark 表述引文：实验部分（Section 4）明确写到：“all the following experiments are tested based on datasets from a commonly used benchmarking database in the field, namely the UCI Machine Learning Repository [27]”，并以30个UCI数据集作为评价场地。
- Benchmark 评价：在30个UCI数据集上评估GARC的分类准确率，并与C4.5、CBA、SVM、NN等分类器进行对照；同时比较规则数量和执行时间。结果显示GARC准确率与多个基准分类器无显著差异，规则数量平均仅为CBA的4.3%。
- 判定理由：论文核心目标为提出GARC算法，以在保持分类准确率的同时大幅减少规则数量，核心指标（准确率、规则数量、执行时间）均为客观可测量指标，且没有其他并列的核心贡献；全文在实验部分明确使用UCI Machine Learning Repository作为公开benchmark数据集，并在该benchmark上与C4.5、CBA、SVM、NN等明确参照对比，benchmark结果直接支撑了GARC客观性能改进的核心主张。因此两个模块均通过，严格纳入。
- 置信度：0.95

### An integrated two-stage model for intelligent information routing 

- 年份/期刊：2006 / Decision Support Systems
- DOI：10.1016/j.dss.2005.01.007
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：平均精确率 PAVG（Average Precision）；前十位精确率 P10
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：TREC AP 新闻语料（three-year news corpus from the Associated Press）；TREC 10GB Web 数据（10 GB web data used in TREC）
- 参照点：用户提供查询 + Okapi（基线，固定排序函数）；用户提供查询 + GP；系统构造查询 + Okapi；系统构造查询 + SVM
- Benchmark 表述引文：Section 4.1：'To test how our model performs compared to other well known routing systems we use two different data sets in the experiments. The first data set is the three-year news corpus from the Associated Press (AP)... The second data set is the 10 GB web data used in TREC (see http://trec.nist.gov for more details)...'；Section 5：'The results reported in this paper are based on two benchmark data collections from TREC.'
- Benchmark 评价：在两个基准语料（TREC 的 AP 新闻语料和 TREC 10GB Web 数据）上，将提出的两阶段模型（系统构造 PQ + GP 自适应排序函数）与 Okapi BM25 固定排序及 SVM 分类器基线比较，测试集上报告各查询 PAVG 与 P10 的平均值。
- 判定理由：客观指标方面：核心成功指标是 PAVG 和 P10，均基于 TREC 数据集的既有相关性标签计算，属于 objective_fixed_factual_labels；研究目标、实验设计和贡献声明均围绕检索性能提升展开，未发现并列核心目标。Benchmark 方面：全文明确将 TREC AP 和 TREC Web 数据作为两个 benchmark 数据集合进行模型评价，评价位于实验部分，结果与 Okapi、SVM 等明确基线比较，且该 benchmark 比较直接支撑核心性能提升主张。因此两个模块均通过，strict_include=true。
- 置信度：0.97

### Design of a shopbot and recommender system for bundle purchases 

- 年份/期刊：2006 / Decision Support Systems
- DOI：10.1016/j.dss.2006.05.005
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：总购买成本/节省百分比；免费赠品识别数量与价值；推荐系统额外节省；算法运行时间与最优性差距
- Benchmark 状态：benchmark_comparison_central
- 参照点：单项最低价格之和（unbundled individually-cheapest prices）；CPLEX最优解
- Benchmark 表述引文：在第4节实验部分明确写道：'For each bundle we solved the problem using both CPLEX and our algorithm and compared the resulting savings using the sum of the individually-cheapest prices of items in the bundle as a benchmark.' 同时表3和表4列出'Avg benchmark cost'、'Benchmark cost of needed items'等。
- Benchmark 评价：以随机生成的2到20件商品组合为测试集，每个规模1000个实例，使用14家零售商收集的194个真实捆绑数据。基准为所需商品各自最低售价之和，比较CPLEX最优解和GRAB算法的节省率、免费赠品价值以及推荐系统的新增成本和节省。结果表明算法能带来显著节省（中位节省10%，近10%案例节省超20%），推荐系统节省超过75%。
- 判定理由：客观指标门：核心成功指标为购买成本、节省金额/百分比、免费赠品价值、算法运行时间和最优性差距，全部为客观可测量事实，不依赖人类感受或语义判断；唯一核心目标是设计模型/算法以最大化捆绑购买节省并推荐高节省商品，无其他并列核心目标。benchmark门：全文存在明确的benchmark表述，实验部分以单项最低价格之和作为基准，并与CPLEX最优解比较，benchmark结果直接支撑节省和免费赠品主张；benchmark处于评价语境、有明确比较器且为核心主张服务。因此 strict_include=true。
- 置信度：0.97

### Economic metaphors for solving intrafirm allocation problems: What does a market buy us? 

- 年份/期刊：2006 / Decision Support Systems
- DOI：10.1016/j.dss.2006.02.009
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：解质量（最优性差距）；计算时间；agent valuation list 的实际规模
- Benchmark 状态：benchmark_comparison_central
- 参照点：complete search（已知最优解）；tabu search（Open Tabu Search framework）；Tabu(b-limit)（相同较短时间限制）
- Benchmark 表述引文：Section 4.2: “The solutions generated by complete search provide a benchmark against which the quality of the solutions from the heuristic solution techniques is evaluated. However, the requirement to find optimal allocations imposes practical constraints … tabu search is used as a benchmark for larger problem instances.”
- Benchmark 评价：在随机生成的多作业单机随机调度测试集上，作者以 complete search（完备搜索得到最优解）作为小规模算例的基准，以 tabu search 作为大规模算例的基准，分别评价 Market（SUBLIST 协议）和 Market(b-limit) 的解质量与计算时间；结果表明 Market 在相近时间内获得更优或更高的解质量。
- 判定理由：客观指标方面：核心成功指标是解质量（最优性差距）和计算时间，均为可直接计算、不依赖人类感知或语义判断的客观性能指标；研究问题、实验设计和贡献声明都围绕这些客观指标。唯一核心目标方面：文章没有把主观体验、心理机制、理论机制或政策建议作为并列核心贡献，Discussion 中的灵活性和鲁棒性是定性优势补充而非核心成功标准。Benchmark 方面：第 4.2 节明确使用“benchmark”一词，将 complete search 作为小规模算例的基准、tabu search 作为大规模算例的基准，并在评价语境中通过表格和图形比较 Market/Tabu 的解质量和时间，这些 benchmark 结果直接支撑市场搜索算法提升解质量的核心理由。因此两个模块均通过，strict_include=true。
- 置信度：0.95

### A practical approach for efficiently answering top-k relational queries 

- 年份/期刊：2007 / Decision Support Systems
- DOI：10.1016/j.dss.2007.04.005
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：总代价（Total Cost）；过量结果数（Excess）；重启查询百分比（Percentage of Restarts）
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：DWBS（Dynamic Workload Based Strategy，作为对照基准技术，非公开数据集）
- 参照点：DWBS（Dynamic Workload Based Strategy）；无重启范围、重启范围等既有范围估计基准概念
- Benchmark 表述引文：第3.2节明确称：“The DWBS [5], which we use in this paper as a benchmark technique...”；第5节实验部分声明“compare this property against the benchmark technique, the DWBS”；第7节结论再次称“comparative analysis against our benchmark strategy (the DWBS)”。
- Benchmark 评价：在约210K记录的Census收入和500K记录的合成Zipf数组数据上，使用equi-count、equi-width、MaxDiff三类直方图和多种bin数、多种k值，系统比较QLOCS与DWBS在Excess、Percentage of Restarts和Total Cost上的表现。结果显示QLOCS显著更低且更稳定，证明其“直方图无关”的高效性和稳健性。
- 判定理由：该文属于数据库查询处理技术研究。其核心目标是通过QLOCS成本模型优化top-k到范围查询的转换，提升Total Cost、Excess和Restarts等完全客观的效率指标，并无主观评价或并列性非客观贡献。全文存在明确的benchmark表述，将DWBS作为基准技术，并在实验部分系统比较QLOCS与DWBS，基准对比结果直接支持QLOCS更高效、更稳健的核心主张。因此，客观指标门槛、唯一核心目标门槛和benchmark门槛均通过。
- 置信度：0.95

### An intelligent information agent for document title classification and filtering in document-intensive domains 

- 年份/期刊：2007 / Decision Support Systems
- DOI：10.1016/j.dss.2007.04.001
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：Mean Average Precision (MAP)；Average Recall；Average elapsed time per topic
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：Reuters-21578 (Modified Lewis / ModLewis split)
- 参照点：SVM (full test documents)；SVM (test document titles)；IFC without belief revision
- Benchmark 表述引文：第4节实验部分开头："The effectiveness of our intelligent information agent is evaluated empirically based on the Modified Lewis (“ModLewis”) Split of the Reuters-21578 corpus [19] which is a commonly used benchmark collection for text classification."
- Benchmark 评价：在Reuters-21578 ModLewis split上，从135个主题中选取17个主题，构造HAL空间并用文档标题进行分类；实验评价IFC、IFC+BR和SVM三组模型，报告MAP、平均召回和时间。表6显示IFC+BR在标题任务上的平均精确率为0.698，超过SVM标题任务的0.601；文章据此主张混合模型优于SVM。
- 判定理由：客观指标方面：论文以文档分类/过滤的MAP、平均召回和计算时间为核心结果，这些指标基于Reuters-21578固定主题标签和实际运行时间，不依赖用户主观评价；Reuters主题标签属于固定基准事实标签，因此符合客观指标门槛。唯一核心目标方面：摘要、实验和结论均围绕提升分类/过滤精确率、召回率和效率展开，信息流与信念修正是实现手段而非并列的核心理论贡献，全文没有用户满意度或主观质量作为成功标准，因此唯一核心目标为客观指标提升。benchmark方面：第4节明确将Reuters-21578 ModLewis Split称为常用文本分类benchmark，在该基准上对IFC、IFC+BR和SVM进行系统比较，结果直接支撑“优于SVM”的核心性能主张，并且有明确参照点。因此两个模块均通过，strict_include=true。
- 置信度：0.9

### Dare to share: Protecting sensitive knowledge with data sanitization 【全文无benchmark字样-需人工复核】

- 年份/期刊：2007 / Decision Support Systems
- DOI：10.1016/j.dss.2006.08.007
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：数据效用（Data Utility）；数据准确度（事务级/项级）；CPU时间（秒）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：FIMI repository中的bms1、bms2和retail数据集；UCI Machine Learning Repository中的chess和mushroom数据集
- 参照点：Sliding Window Algorithm (SWA)；CPLEX branch-and-bound（仅作为不可行性对照，未在结果表中报告）
- Benchmark 表述引文：第4.1节明确选择公开真实数据集作为评价场地：‘Out of these, we selected a retail market basket dataset from an anonymous Belgian retail store..., two sets (bms1 and bms2) containing click-stream data from Blue Martini Software Inc., used for the KDD Cup 2000..., and two datasets (chess and mushroom) from the Irvine Machine Learning Database Repository’；第4.2节明确使用这些数据比较算法：‘The results of applying the three proposed sanitization approaches as well as SWA are shown in Table 4’。
- Benchmark 评价：在bms1、bms2、retail、chess、mushroom五个公开真实数据集上，以多个支持度阈值运行Aggregate、Hybrid、Disaggregate和SWA，报告数据效用、事务级/项级准确度和CPU时间。结果显示三种方法平均数据效用分别为45.82%、78.44%、79.60%，均显著高于SWA的27.73%，其中Disaggregate和Hybrid效用最高。该比较直接支撑本文的核心主张。
- 判定理由：客观指标层面：数据效用、数据准确度和CPU时间均由事务数据、项集支持数、删除操作或运行时间直接计算，不涉及主观感知或语义判断，全部核心成功结果均为客观指标。唯一核心目标层面：全文研究问题、方法设计、实验评价和贡献声明均围绕在隐藏敏感项集的前提下最大化数据效用，并声称所提方法优于SWA；数据准确度被明确称为辅助说明信息，CPU时间是权衡代价而非核心目标，不存在并列的主观、理论或制度性核心贡献。Benchmark层面：作者在FIMI和UCI的公开真实数据集（bms1、bms2、retail、chess、mushroom）上对三种方法与SWA进行系统比较，表4/表5结果直接支撑核心提升主张，且存在明确的参照点SWA；尽管全文没有使用‘benchmark’一词，但这属于明确命名公开标准数据集并作为评价场地的命名式benchmark表述。因此两个模块均通过，strict_include为true。
- 置信度：0.85

### Decision support for multi-unit combinatorial bundle auctions 

- 年份/期刊：2007 / Decision Support Systems
- DOI：10.1016/j.dss.2006.10.009
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：投标人利润（占完美信息最大利润的百分比）
- Benchmark 状态：benchmark_comparison_central
- 参照点：完美成本信息上界；随机成本参数（无信息情况）
- Benchmark 表述引文：第4.2节：“The results from the experiments were difficult to evaluate as such, creating the need for the use of benchmarks. In our experiment, the natural benchmarks were on the one hand the case of perfect cost information, and on the other hand the case of no cost information.”
- Benchmark 评价：在作者自己生成的随机组合拍卖实验上评价数量支持工具；以完美成本信息情形作为上界基准、随机成本参数作为无信息基准，报告dual heuristic和random heuristic所获利润占完美信息最大利润的百分比，并进行t检验。
- 判定理由：本文核心是提出并测试组合拍卖中投标人数量支持工具，衡量指标为投标人利润（占完美信息上界百分比），该指标由随机生成的成本函数与优化模型确定，无主观评价；大量实验比较dual heuristic与random/perfect information基准，并在第4.2节明确使用benchmark一词，因此同时满足客观指标、唯一核心目标和明确benchmark比较。排除触发码为空。
- 置信度：0.82

### Genetic programming for prevention of cyberterrorism through dynamic and evolving intrusion detection 【全文无benchmark字样-需人工复核】

- 年份/期刊：2007 / Decision Support Systems
- DOI：10.1016/j.dss.2006.04.004
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：测试集总体准确率；正例（入侵）识别准确率；负例（非入侵）识别准确率
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：1999 Knowledge Discovery in Database (KDD) Cup data (DARPA/MIT Lincoln Laboratories)；KDD'99 Classifier Learning Contest
- 参照点：KDD'99分类学习竞赛获胜者（Pfahringer的C5 bagged boosting）；简单1-最近邻分类器；同一GP框架内的普通交叉算子（ordinary crossover）
- Benchmark 表述引文：Section 5.1: 'The data selected for our study comes from the 1999 Knowledge Discovery in Database (KDD) Cup data, supplied by the Defense Advanced Research Projects Agency (DARPA) and MIT's Lincoln Laboratories.' Section 7: 'Table 5 compares the current study results with results from the KDD'99 Classifier Leaning Contest that also used the DARPA data.'
- Benchmark 评价：在KDD Cup 1999这一公开基准数据集上，对Smurf、Satan、IPSweep、PortSweep、Back、Normal、Buffer Overflow、WarezClient、Neptune等入侵域训练GP模型并用独立测试集评估；Table 2-4比较普通交叉与同源交叉的总体/正例/负例准确率，Table 5将同源交叉结果与KDD'99竞赛获胜方法（C5 bagged boosting）和简单1-近邻方法按攻击类别比较，显示在Probe、DoS、U2R、R2L上的准确率大幅提高，Normal略低。
- 判定理由：文章以KDD Cup 1999公开基准数据为实验场地，核心目标是评估GP（特别是同源交叉）能否提升网络入侵检测的准确率；所有核心成功指标均为测试集总体准确率、正例准确率和负例准确率，属于对固定事实标签（入侵/正常）的预测性能，完全客观。研究问题、方法、结果与结论均围绕这些客观指标展开，没有主观量表或并列的理论/政策贡献。KDD Cup/KDD'99竞赛是命名式公开benchmark，Table 5在结果部分将其结果作为明确参照并与竞赛获胜方法、1-NN比较，benchmark评价直接支持核心提升主张。因此两个模块均通过，strict_include=true。
- 置信度：0.93

### Predicting adequacy of vancomycin regimens: A learning-based classification approach to improving clinical decision making 

- 年份/期刊：2007 / Decision Support Systems
- DOI：10.1016/j.dss.2006.02.003
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：总体准确率；各类别预测值
- Benchmark 状态：benchmark_comparison_central
- 参照点：one-compartment pharmacokinetic model；C4.5 base system（未加Bagging）；neural network base system（未加Bagging）
- Benchmark 表述引文：第4.2节评价设计明确提出：'We included in our evaluations the one-compartment model (described in Section 2.2) to serve as a performance benchmark.'（将one-compartment药代动力学模型作为性能基准）；摘要亦报告'overall accuracy ... significantly higher than that of the benchmark one-compartment pharmacokinetic model'。
- Benchmark 评价：在987例临床万古霉素病例上评价C4.5、反向传播神经网络、Bagged C4.5和Bagged NN，与基准one-compartment药代动力学模型比较；评价任务包括方案充分性二分类、峰浓度三分类和谷浓度二分类，结果以总体准确率和各类别预测值呈现（表4-6）。
- 判定理由：该文开发并评价用于预测万古霉素方案充分性的学习型分类系统，核心结局为总体准确率和各类别预测值，是由TDM实测浓度与固定治疗范围比较得到的客观标签，不依赖主观感受或语义评价；全文唯一核心目标是提升该客观预测性能。评价设计明确将one-compartment药代动力学模型作为performance benchmark，并在结果部分以该benchmark为参照报告显著提升，benchmark评价是核心证据。两个模块均通过，因此严格纳入。
- 置信度：0.9

### Predicting home-appliance acquisition sequences: Markov/Markov for Discrimination and survival analysis for modeling sequential information in NPTB models 

- 年份/期刊：2007 / Decision Support Systems
- DOI：10.1016/j.dss.2007.02.008
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：加权正确分类率 (wPCC)
- Benchmark 状态：benchmark_comparison_central
- 参照点：比例机会准则 C_pro（理论界限/默认期望水平）
- Benchmark 表述引文：评价方法一节中明确写道：‘Secondly, we benchmark the model's performance to the proportional chance criterion (C_pro) rather than the maximum chance criterion’；结果部分再次报告：‘even the current NPTB model (wPCCh=19.94%) substantially improves upon the default expected response level (C_pro=12.63%)’。
- Benchmark 评价：作者在评价 NPTB 模型时，将最终 MNL 模型的加权正确分类率 wPCC=0.1994（留出样本）与比例机会准则 C_pro=12.63% 进行比较，证明模型显著优于随机/默认期望水平；同时在同一评价框架下比较了 NULL、NULL+ORDER、NULL+DURATION、NULL+ORDER+DURATION 四种模型，以及 MNL/HEV/PROBIT 三种模型形式。该基准比较直接支撑‘模型预测能力提升’的核心主张。
- 判定理由：核心评价指标为加权正确分类率（wPCC），基于真实购买交易记录预测下一次购买的产品类别，构念和取值均不依赖人的感受或语义判断，且最终目标就是提升该客观预测性能；全文没有并列的主观或理论核心目标。存在明确的 benchmark 表述：作者在评价方法中直接使用‘we benchmark the model's performance to the proportional chance criterion’，并将该基准比较作为证明模型预测能力较默认水平显著改进的核心证据，基准参照点为理论界限 C_pro。因此同时满足客观指标唯一核心目标和明确 benchmark 两个模块，strict_include=true。
- 置信度：0.8

### Reducing the cost of accessing relations in incremental view maintenance 

- 年份/期刊：2007 / Decision Support Systems
- DOI：10.1016/j.dss.2006.11.006
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：关系访问次数/增量维护表达式的处理代价；视图更新时间（执行时间）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：TPC-R benchmark
- 参照点：recomputation method（重计算方法）；n-term method（基于表达式(2)的Labio et al.方法）；ours(no sharing)（多视图实验中不共享中间结果）
- Benchmark 表述引文：第6节Experiments开始处明确写道：“In the experiments, we used the TPC-R benchmark 256MB RAM was used as the data warehouse environment.”；第4节亦称“TPC-R, which is a standard benchmark for decision support systems”。
- Benchmark 评价：在TPC-R基准的schema和查询Q5/Q9基础上构造两个SPJ视图V1和V2，并在这些基准数据上比较重计算方法、n-term方法（即现有最优增量维护方法）与本文最优delta evaluation方法。实验在不同更新规模（2%–20%）和不同基表规模（100%–500%）下测量更新耗时，结果显示本文方法优于所有对比方法。多视图实验同样使用TPC-R查询派生视图，并比较ours(no sharing)与ours(sharing)。
- 判定理由：文章核心目标是减少增量视图维护中的关系访问成本，核心成功指标是关系访问次数/维护表达式代价和实际更新时间，均为完全客观可观测指标；全文未使用主观量表或人类语义评价。核心贡献唯一且明确。实验在TPC-R这一命名公开基准上进行，基于TPC-R schema和查询构造视图，并以重计算方法、n-term方法等作为明确参照点，基准评价直接支撑“最优delta evaluation方法提升维护效率”的核心主张。因此两个模块均通过，严格纳入。
- 置信度：0.98

### Reference metadata extraction using a hierarchical knowledge representation framework 【全文无benchmark字样-需人工复核】

- 年份/期刊：2007 / Decision Support Systems
- DOI：10.1016/j.dss.2006.08.006
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：参考文献元数据字段抽取准确率（author/title/journal/volume/issue/year/pages）
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：Cora reference dataset (Cora dataset)
- 参照点：Citeseer（现有方法，作者字段准确率约82%）；Peng & McCallum 在 Cora 上报告的 CRF/HMM 结果（word accuracy 95.37%/85.1%，instance accuracy 77.33%/10%）
- Benchmark 表述引文：Section 6：'We conducted an experiment on the same testbed (Cora dataset) in order to compare our approach with Citeseer.' 作者虽未使用 'benchmark' 一词，但明确命名公开的 Cora 数据集作为评价场地，并以现有方法 Citeseer 为比较对象。
- Benchmark 评价：在公开的 Cora reference dataset 上运行所提出的 INFOMAP 模板式 RME 方法，报告整体字段准确率 73.34%、作者字段准确率 87.40%；在 Cora 中 166 条期刊参考文献子集上整体字段准确率 84.94%、作者字段准确率 93.37%。同时，作者以 Citeseer 的作者准确率 82% 作为现有方法参照，支持其方法在作者字段抽取上的提升。
- 判定理由：客观指标：全文以字段准确率（正确抽取字段数/总字段数）为核心因变量，在自行构建的六种参考样式测试集和公开 Cora 数据集上计算，属于可审计的事实型信息抽取性能，不依赖人类主观评价或语义质量判断。唯一核心目标：提出层次模板式 RME 方法并提升参考元数据抽取准确率，摘要、系统设计、实验、比较和结论均围绕该目标；'较少标注数据'只是辅助优点，不构成并列核心目标。Benchmark：虽然全文没有使用 'benchmark' 一词，但明确命名并使用了公开的 Cora reference dataset 作为测试床，并明确以 Citeseer 为比较对象；该比较用于支持作者字段等抽取准确率的提升主张。因此两个模块均通过，strict_include=true。
- 置信度：0.72

### SpamHunting: An instance-based reasoning system for spam labelling and filtering 【全文无benchmark字样-需人工复核】

- 年份/期刊：2007 / Decision Support Systems
- DOI：10.1016/j.dss.2006.11.012
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：正确分类率（%OK）；假阳性率（%FP）与假阴性率（%FN）；垃圾邮件召回率与精确率；总成本比（TCR）；训练与运行时间
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：SpamAssassin corpus
- 参照点：Naïve Bayes；Adaboost；SVM；ECUE；Cunn Odds Rate
- Benchmark 表述引文：Section 4.1: 'Table 3 describes the SpamAssassin corpus (created by Justin Mason of Network Associates, and public available for download at http://www.spamassassin.org/publiccorpus/) employed in our experiments.' 该语料库为垃圾邮件过滤领域广泛使用的公开基准语料库，系统在该语料库上被系统化评价。
- Benchmark 评价：在SpamAssassin 2002/2003公开语料库上，采用10折分层交叉验证，将SpamHunting与Naïve Bayes、Adaboost、SVM、ECUE和Cunn Odds Rate五种已有方法比较，报告%OK、%FP、%FN、召回率、精确率、TCR和训练时间。结果显示SpamHunting在FP/FN比率、精确率及高成本场景下TCR等方面优于其他模型。
- 判定理由：客观指标方面：所有核心成功指标均为垃圾邮件分类性能（%OK、FP/FN、召回率、精确率、TCR）和计算时间，这些指标基于外部事实标签（spam/legitimate）和可测量的物理时间，完全客观，不依赖人类感受或语义评价；系统设计和贡献声明均围绕提升这些客观指标展开，没有并列的主观或理论核心目标。Benchmark方面：文章明确命名SpamAssassin公开语料库作为评价场地，在评价语境中进行系统化比较，结果表/图与多个baseline方法对比，支撑了核心性能提升主张。因此两个模块均通过，strict_include为true。
- 置信度：0.96

### A Multi-criteria Convex Quadratic Programming model for credit data analysis 

- 年份/期刊：2008 / Decision Support Systems
- DOI：10.1016/j.dss.2007.12.001
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：分类准确率（总体、Normal类、Bad类）；Type I 和 Type II 错误率；KS score；相关系数（Correlation coefficient）；计算时间；可扩展性/数据集规模
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：German credit card application dataset (UCI Machine Learning databases)
- 参照点：SPSS Linear Discriminant Analysis (LDA)；Decision Tree See5；SVMlight；LibSVM
- Benchmark 表述引文：引言中表述：‘the classification results of MCQP were compared with four wellknown and frequently used classification benchmark tools: SPSS Linear Discriminant Analysis (LDA), Decision Tree based See5, SVMlight, and LibSVM’；实验部分表述：‘The first benchmark set is a German credit card application dataset from UCI Machine Learning databases.’
- Benchmark 评价：在四个信用数据集（German, Australian, Japanese, US bank）上，通过10折交叉验证，将MCQP与LDA、See5、SVMlight、LibSVM在总体准确率、类内准确率、Type I/II错误、KS分数、相关系数五个指标上进行比较。结果显示MCQP在Japanese集上所有指标最佳，在US集上Bad准确率与Type I错误最佳，在German和Australian集上表现高于平均水平。
- 判定理由：文章核心目标是提出并验证高效、可扩展的MCQP分类模型，评价指标包括分类准确率、错误率、KS分数、相关系数和计算时间，全部为完全客观的可测量结果；标签为外部可核验的信用状态（Normal/Bad），属于固定事实标签。全文无主观构念或语义评价作为成功标准。实验部分明确将German文档集称为benchmark set（来自UCI），并明确使用四个著名基准分类工具作为参照进行比较，比较结果直接支撑MCQP的分类性能与效率主张。因此客观指标与唯一核心目标、benchmark门槛均满足。
- 置信度：0.92

### A new approach for a proxy-level web caching mechanism 

- 年份/期刊：2008 / Decision Support Systems
- DOI：10.1016/j.dss.2008.05.001
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：总缓存成本（含用户延迟与缓存更新代价）
- Benchmark 状态：benchmark_comparison_central
- 参照点：LRU缓存替换策略（least recently used）
- Benchmark 表述引文：Section 4 Performance analysis：“Therefore we use LRU as a benchmark to compare the performance of our proposed mechanism.”
- Benchmark 评价：在IRCache网络纽约代理服务器的62天实际trace数据集上，分别评价准静态机制和集成机制的缓存总成本，并与同一trace上实现的LRU基准策略比较；Tables 7-10报告了两种机制相对LRU的总成本及百分比改进。
- 判定理由：客观指标：核心成功指标是缓存总成本与用户延迟，均由代理trace日志、机制规则和成本公式确定性计算，不涉及主观感知或语义评价。唯一核心目标：论文的研究问题、设计目标和贡献声明均围绕提出并评估缓存机制、降低代理级用户延迟/成本；不存在并列的主观体验、理论机制或政策贡献。Benchmark：作者在性能分析部分明确写出“we use LRU as a benchmark”，且该基准评价处于实验评价语境，比较对象为LRU策略，结果表直接报告相对LRU的总成本改进，支撑了核心性能提升主张。因此满足纳入条件。
- 置信度：0.96

### A stack-based prospective spatio-temporal data analysis approach 

- 年份/期刊：2008 / Decision Support Systems
- DOI：10.1016/j.dss.2007.12.008
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：精确率 Precision；召回率 Recall；F值 F-measure；告警延迟 Alarm delay；误报次数 False alarms；漏报次数 Fail to detect；计算时间 Computing time
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：space–time scan statistic (SaTScan) 作为本文明确指定的基准方法
- 参照点：SaTScan（space–time scan statistic）
- Benchmark 表述引文：第4.2节：'We have chosen the space–time scan statistic as the benchmark method since it has been widely tested and deployed, especially in public health applications ...'，并将该基准方法用于与PSVC的定量比较。
- Benchmark 评价：在emerging、expanding、moving三类模拟场景上，将PSVC与基准方法SaTScan进行系统化比较，报告精确率、召回率、F-measure、告警延迟、误报次数、漏报次数和计算时间；同时使用ROC曲线比较敏感度与特异度。结果表（表1、3、5）和ROC曲线成为证明PSVC在识别不规则异常区域方面更准确的核心证据。
- 判定理由：客观指标方面：全文核心评价指标为精确率、召回率、F值、告警延迟、误报/漏报次数和计算时间，全部来自模拟已知异常区域或系统计时，客观且可审计，不依赖人类主观评价。唯一核心目标方面：研究问题、假设、实验和结论均围绕PSVC在客观检测性能上的提升，没有并列的主观体验、理论机制或政策贡献作为核心目标；定量评价框架只是用于支撑比较的方法工具。benchmark方面：第4.2节明确将space–time scan statistic/SaTScan指定为benchmark method，并在第4.4节模拟实验中以SaTScan为对照，系统比较客观指标；该benchmark评价直接支撑“PSVC更准确检测不规则异常区域”的核心主张。因此满足全部条件。
- 置信度：0.9

### An investigation of Zipf's Law for fraud detection (DSS#06-10-1826R(2)) 

- 年份/期刊：2008 / Decision Support Systems
- DOI：10.1016/j.dss.2008.05.003
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：审计命中率（Audit Hit Rate, AHR）；贝叶斯审计命中率（BAHR）；混淆矩阵准确率与假阳性率；总/平均误分类成本（TMC/AMC）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：KDDCUP'99 intrusion detection dataset
- 参照点：100% sampling；KDDCUP'99 benchmark rate/获胜算法结果；无Zipf Analysis预处理的baseline
- Benchmark 表述引文：摘要写有“Quasi-experiment research on the KDDCUP'99 benchmark intrusion detection dataset”；第4.1节明确写“we use the KDDCUP'99 intrusion detection dataset as benchmark”。
- Benchmark 评价：在KDDCUP'99公开入侵检测数据集上，以Zipf Analysis作为预处理器（关键值1%、2%、5%），再使用KDDCUP'99获胜的C5.0决策树算法进行分类，并与无预处理的baseline及KDDCUP'99 benchmark结果比较AHR、BAHR、混淆矩阵准确率/假阳性率和误分类成本。
- 判定理由：文章核心目标为开发并验证基于Zipf定律的欺诈检测机制，评价指标AHR、BAHR、混淆矩阵准确率/FP率和误分类成本均针对KDDCUP'99已知攻击/正常标签等客观事实计算，不涉及主观感知或语义判断；全文以提升这些完全客观检测指标为唯一核心目标与贡献。同时，文章明确将KDDCUP'99命名为benchmark数据集并在评价语境中使用，比较对象包括100%抽样、KDDCUP'99 benchmark率、获胜算法及无预处理baseline，benchmark评价直接支撑核心性能提升主张。因此两个模块全部通过，严格纳入。
- 置信度：0.97

### Communication-Garden System: Visualizing a computer-mediated communication process 

- 年份/期刊：2008 / Decision Support Systems
- DOI：10.1016/j.dss.2008.02.004
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：任务完成正确率（有效性）；任务完成时间（效率）
- Benchmark 状态：benchmark_comparison_central
- 参照点：Netscape Messenger text-based interface
- Benchmark 表述引文：Section 4.1："We selected the text-based interface of Netscape Messenger as the benchmark system."
- Benchmark 评价：在系统评价部分，将 Communication-Garden 的 Content Summary、Interaction Summary、Expert Indicator 图形界面与 Netscape Messenger 文本界面进行比较；比较指标包括客观任务完成正确率、任务完成时间，以及附加的感知易用性和感知有用性。结果多数任务类型上图形界面优于文本界面，支撑了可视化设计的核心改进主张。
- 判定理由：客观指标方面，核心成功指标为任务完成正确率和任务完成时间，均属于完全客观、可独立验证的行为绩效；主观感知量表仅为附加补充结果，不构成并列核心目标。核心目标为验证可视化表示在传递事实性统计与模式方面的有效性，属于唯一的客观绩效改进目标。Benchmark 方面，作者在系统评价部分明确将 Netscape Messenger 文本界面称为 benchmark system，并在该基准上比较图形界面与文本界面的客观任务绩效，比较具有明确参照点，且结果直接支撑核心改进主张。因此两个模块均通过，strict_include=true。
- 置信度：0.82

### Effective spam filtering: A single-class learning and ensemble approach 

- 年份/期刊：2008 / Decision Support Systems
- DOI：10.1016/j.dss.2007.06.010
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：准确率（accuracy）；精确率（precision for spam）；召回率（recall for spam）
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：LingSpam；PU1；PNB；PEBL
- 参照点：PNB；PEBL
- Benchmark 表述引文：摘要：'our proposed E2 technique generally outperforms benchmark techniques (i.e., PNB and PEBL)'；引言：'we empirically evaluate the proposed E2 technique with two spam filtering corpora and include PNB and PEBL as our performance benchmarks'；4.4节：'we evaluate the performance of the proposed E2 technique for each spam filtering corpus, with the performance of PEBL and PNB as benchmarks.'
- Benchmark 评价：在LingSpam和PU1两个公开垃圾邮件语料库上，将所提出的E2与基准技术PNB、PEBL进行系统比较。评价指标为准确率、精确率、召回率。结果显示：LingSpam上E2准确率98.45%略低于PNB（99.13%），但显著高于PEBL（93.29%），精确率最高，召回率91.15%显著优于PEBL；PU1上E2准确率95.67%、召回率97.81%，显著优于PNB和PEBL。另做了对P(Cp)敏感性和训练样本规模效应的对比实验。
- 判定理由：客观指标方面：全文以垃圾邮件过滤中的准确率、精确率、召回率作为唯一成功标准，标签为语料库中垃圾/合法邮件的事实标签，指标计算完全客观可审计；提升这些客观指标是全文唯一核心目标与贡献，没有主观量表和并列理论贡献。Benchmark方面：作者在摘要、引言和实验评价中反复以'benchmarks'明确指称PNB和PEBL作为性能基准，并在LingSpam和PU1两个公开语料库上系统比较E2与基准技术，结果表提供明确参照点，支撑核心提升主张。因此两个模块均通过，strict_include为true。
- 置信度：0.95

### Identification of influencers — Measuring influence in customer networks 

- 年份/期刊：2008 / Decision Support Systems
- DOI：10.1016/j.dss.2008.06.007
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：消息扩散到达的客户数（reach）
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：无公开命名基准数据集；使用电信运营商真实数据样本NW1-NW4及模拟网络NW5-NW9作为实验场地
- 参照点：随机选择（random selection）；其他10种中心性指标：degree、closeness、betweenness、eigenvector、edge-weighted degree、authorities、hubs、PageRank、weighted PageRank、weighted SenderRank
- Benchmark 表述引文：Section 1.4: 'In Section 3 we describe the computational experiments to benchmark different centrality measures'。
- Benchmark 评价：在9个网络（真实电信网络与模拟scale-free/ER网络）上，以11种中心性指标/基线选择初始客户，在11组扩散模型参数下比较最终到达客户数，并用增益曲线和lift展示相对随机选择和各指标间的差异。
- 判定理由：客观指标方面：核心结果指标是消息扩散到达客户数，来自明确定义的计算机仿真，不依赖人的感受或语义判断，属于完全客观指标；且该指标提升是全文唯一核心目标与贡献。Benchmark方面：论文在Section 1.4明确说明用“computational experiments to benchmark different centrality measures”，实验位于评价语境，且在各网络/扩散模型下与随机选择及其他中心性指标比较，证明中心性选择带来的到达数提升。因此两个模块均通过，strict_include为true。
- 置信度：0.87

### Learning Bayesian networks from incomplete databases using a novel evolutionary algorithm 

- 年份/期刊：2008 / Decision Support Systems
- DOI：10.1016/j.dss.2008.01.002
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：平均结构差异 (ASD)；等价类结构差异 (AESD)；平均执行时间 (AET)；平均 MDL 分数 (AOMDL)；累计提升 (Cumulative Lift)
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：ALARM；PRINTD；ASIA
- 参照点：LibB (SEM algorithm)；Bayesware Discoverer (Bound-and-Collapse)；HEA1 (mode imputation + HEA)；HEA2 (missing as new state + HEA)
- Benchmark 表述引文：摘要中明确写道：'The experimental results on the databases generated from several benchmark networks illustrate that the new method has better performance...'；实验方法部分更明确说明：'we randomly sample three original data sets from the well-known benchmark networks including the ALARM [4], the PRINTD [22], and the ASIA networks [35]'。位置：Abstract 和 Section 4.1。
- Benchmark 评价：在由 ALARM、PRINTD、ASIA 三个知名基准网络生成的 9 个不完整数据集上，比较 EBN 与 LibB、Bayesware Discoverer，并额外与 HEA1、HEA2 等缺失值处理方法比较；EBN 在多数数据集上获得显著更小的 ASD/AESD、更低的 AOMDL，以及更快的执行时间（部分数据集）。
- 判定理由：文章提出 EBN 算法，核心目标是在不完整数据上更准确地学习贝叶斯网络，并通过结构差异(ASD/AESD)、MDL分数、执行时间、真实数据累计提升等完全客观指标验证提升；这些指标均不依赖主观感受或语义判断。实验明确使用 ALARM、PRINTD、ASIA 三个知名 benchmark 网络作为评价场地，并与多个已有算法/基线进行统计比较，benchmark 结果构成核心性能主张的证据。因此同时满足'客观指标提升是唯一核心目标'和'明确 benchmark 表述'两项要求，strict_include=true。
- 置信度：0.98

### Learning bidding strategies with autonomous agents in environments with unstable equilibrium 

- 年份/期刊：2008 / Decision Support Systems
- DOI：10.1016/j.dss.2008.05.005
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：利润（平均利润）；利润收敛性（利润方差/标准差）；学习策略与Nash均衡策略的欧氏距离
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：Nash payoff（理论基准）
- 参照点：Nash payoff；已知最优/最佳响应期望收益；利润上界；无sliding window protocol的同一agent
- Benchmark 表述引文：Section 2末尾：'We use the aforementioned desirable properties of rational behavior and convergence to evaluate the agents' performance, and use the Nash payoff as a benchmark in comparing the effectiveness of the agents.'
- Benchmark 评价：在离散化的两卖方reverse auction仿真中，以Nash payoff为基准，评价GA、Softmax、0.1Greedy三类学习agent；报告其面对纯策略、自我对弈/互相博弈、Nash策略时的利润平均值/标准差和策略到Nash的距离，并在第5节比较有无sliding window protocol的性能改进。
- 判定理由：客观指标方面，核心成功标准是利润、利润方差/标准差、策略到Nash均衡的距离，均为仿真中可审计、确定性的技术指标，不涉及人的感知或语义评价；唯一核心目标是证明简单学习agent能学到最优/最佳响应并收敛（即客观性能提升），Nash不稳定性分析仅为问题动机。Benchmark方面，作者在评价语境中明确写出“use the Nash payoff as a benchmark”，并以Nash payoff、最优收益、上界以及无滑动窗口版本为明确比较对象，benchmark结果直接支撑agent学习绩效的核心主张。因此两个模块均通过，strict_include=true。
- 置信度：0.93

### Shopbot 2.0: Integrating recommendations and promotions with comparison shopping 

- 年份/期刊：2008 / Decision Support Systems
- DOI：10.1016/j.dss.2008.05.006
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：推荐组合的节省金额（美元）
- Benchmark 状态：benchmark_comparison_central
- 参照点：Amazon.com 当前最佳推荐（Benchmark）；Buy.com 当前最佳推荐（Benchmark）；表2中的基准节省值
- Benchmark 表述引文：第3.4节：‘For each book we determine the benchmark savings of the current best bet as the difference between the sum of the list prices of the two books ... and the total order cost ... The resulting savings are compared to the benchmarks and are summarized in Table 2.’；此处基准为当前最佳推荐组合的节省额。
- Benchmark 评价：在Amazon.com（87本书样本）和Buy.com（46本样本）上，以当前最佳推荐作为基准，求解整数规划模型得到Our RS；Amazon平均节省16.23美元对基准12.19美元（高33%），Buy.com为21.45美元对15.67美元（高37%），均p<.001。
- 判定理由：全文的核心结果是可核验的金钱节省额，属于完全客观指标；模型设计、评价和贡献声明均围绕提升购物者节省额展开，无主观量表或并列核心目标。第3.4节明确使用‘benchmark savings’作为当前最佳推荐基线，将模型结果与之比较并报告显著提升，构成支撑核心主张的benchmark评价。因此两个模块均通过，strict_include为true。
- 置信度：0.74

### The enhancement of solving the distributed constraint satisfaction problem for cooperative supply chains using multi-agent systems 

- 年份/期刊：2008 / Decision Support Systems
- DOI：10.1016/j.dss.2008.02.001
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：订单满足率（R_OF）；平均订单履行周期（T_OF）；平均在制品库存成本（C_WIP）；平均成品库存成本（C_FP）；平均谈判轮数（NR）；平均计算时间（C_T）
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：COM（集中式优化机制）；DCSM（采用AWC的分布式协调机制）
- 参照点：COM（centralized optimization mechanism，集中式优化机制）；DCSM（distributed coordination satisfaction mechanism with AWC，采用AWC的分布式协调机制）；AWC（asynchronous weak-commitment search，异步弱承诺搜索）
- Benchmark 表述引文：第1节：'The proposed distributed coordination mechanism is evaluated by comparing its performance with two benchmark mechanisms: a centralized optimization mechanism... and a DCSP solving method, called asynchronous weakcommitment search (AWC).'；第4节：'The performance of COM and DCSM are adopted as benchmarks to investigate NegoGA's performance.'
- Benchmark 评价：在模拟的模具制造供应链（16家公司）环境中，将NegoGA与DCSM和COM三种机制进行系统比较。Experiment A在四种订单需求模式（A-1至A-4）下比较订单满足率、平均订单履行周期、WIP库存成本和成品库存成本；Experiment B在A-3动态需求环境下比较DCSM与NegoGA的谈判轮数和计算时间。结果表明NegoGA在多数动态环境下显著优于DCSM，并与集中式COM相比在真实场景中更具可行性。
- 判定理由：客观指标方面，本文以订单满足率、履行周期、库存成本、谈判轮数和计算时间等系统日志型客观指标作为成功标准，没有主观量表或人类语义评价；核心目标方面，研究问题和贡献声明都围绕NegoGA提升分布式供应链排程绩效展开，未发现并列的核心理论、政策或主观贡献；benchmark方面，作者明确使用benchmark机制/基准机制表述，将COM和DCSM/AWC作为对照基准，在模拟供应链上系统比较并用于支撑NegoGA的性能提升主张，比较对象明确。因此两个模块均通过，strict_include为true。
- 置信度：0.95

### A branch-and-cut algorithm for the Winner Determination Problem 【全文无benchmark字样-需人工复核】

- 年份/期刊：2009 / Decision Support Systems
- DOI：10.1016/j.dss.2008.10.009
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：求解时间；对偶间隙；分支树节点数
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：CATS 2.1 (Combinatorial Auction Test Suite)
- 参照点：原始整数规划公式(WDP)作为baseline；含预处理的(WDP)；不加branch-and-cut的CPLEX默认设置；不含useful inequalities的branch-and-cut
- Benchmark 表述引文：Section 7.1 The data: 'The aforementioned generator is called CATS 2.1 (Combinatorial Auction Test Suite), was introduced in [16]'；全文未直接使用'benchmark'一词，但明确以该公开测试套件作为实验评价场地，并说明其来源于标准测试套件，等价于命名式benchmark表述。
- Benchmark 评价：在CATS 2.1生成的FR、LR、D、B、P、R、A等分布实例以及自生成S实例上，评价了原始公式(WDP)、tightened公式(WDP*)、预处理和branch-and-cut算法；比较不同方法在求解时间、对偶间隙和分支节点数上的表现。表1、2、3、4展示了这些对比结果。
- 判定理由：文章核心目标是设计并验证求解Winner Determination Problem的branch-and-cut算法，以降低求解时间和对偶间隙等完全客观可测量的计算指标。全文评价体系完全基于求解时间、gap和分支节点数，无任何主观或人类语义判断指标。多面体与有效不等式研究是算法改进手段，不构成并列核心目标。计算实验使用公开标准测试套件CATS 2.1作为评价场地，并与原始公式等baseline进行显式比较，结果证明客观指标提升，因此同时满足客观指标唯一核心目标和明确benchmark表述两个条件。
- 置信度：0.9

### A decision support system for detecting products missing from the shelf based on heuristic rules 

- 年份/期刊：2009 / Decision Support Systems
- DOI：10.1016/j.dss.2008.11.004
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：准确率（Accuracy/Confidence）；覆盖率/支持度（Support/Coverage）；Total Performance
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：European OOS Index (EOI)
- 参照点：European OOS Index；ISOS Ver.1 与 ISOS Ver.2（6个月/14个月）版本对比
- Benchmark 表述引文：Section 2.1: 'The OOS Index will be used in this paper as a benchmark.'；Section 5: 'Each version was compared to the detection capabilities of the European OOS Index'，并以图4和表10给出Accuracy/Support对比。
- Benchmark 评价：在物理审计生成的不同测试集（TeS1-TeS6）和二次精炼审计中，评价ISOS Ver.1/Ver.2的OOS检测效果，并与European OOS Index基准比较；结果显示ISOS Accuracy约92-94%，OOS Index约36%，Support约13-27% vs 0.27%。
- 判定理由：文章核心目标是开发并验证基于启发式规则的ISOS系统，提升OOS自动检测的Accuracy/Support；这些指标基于物理审计得到的客观事实标签（EXISTS/OOS），属于objective_fixed_factual_labels，且没有并列的主观核心目标。全文明确将European OOS Index作为benchmark，并在实验/使用部分以其为参照比较ISOS的Accuracy和Support，benchmark评价直接支撑核心检测性能提升主张。因此两个模块均通过，strict_include=true。
- 置信度：0.9

### Detecting and forecasting economic regimes in multi-agent automated exchanges 【全文无benchmark字样-需人工复核】

- 年份/期刊：2009 / Decision Support Systems
- DOI：10.1016/j.dss.2009.05.012
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：经济制度转移预测成功率；制度概率分布的KL散度；价格分布预测误差
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：TAC SCM 2005 (Trading Agent Competition for Supply Chain Management)
- 参照点：真实制度（使用全量游戏数据离线计算）；马尔可夫校正-预测与双重指数平滑预测对比；GMM 16分量与25分量配置对比
- Benchmark 表述引文：摘要中明确命名公开竞赛任务并作为评价场地：“We validate our methods by presenting experimental results in a case study, the Trading Agent Competition for Supply Chain Management.”；第6节标题亦为“Performance of regime predictions in TAC SCM”。文章虽未使用“benchmark”一词，但TAC SCM是公开的多智能体供应链管理标准竞赛任务，且被作为全文核心评价场地，符合命名式benchmark表述。
- Benchmark 评价：在TAC SCM 2005半决赛/决赛的24场游戏（18场训练、6场测试）上，对低、中、高三个市场分别应用GMM学习制度，在线识别每日主导制度并预测未来至多20天的制度转移；报告制度转移预测成功率、制度概率分布KL散度以及价格分布预测误差。
- 判定理由：客观指标方面，核心评价指标为制度转移预测成功率、制度概率分布KL散度和价格分布预测误差，三者均由TAC SCM游戏日志中的价格、库存、供需等客观数据按确定公式计算，不依赖人类感受或语义判断；研究问题、设计目标和贡献声明均围绕“检测并预测经济制度”展开，提升预测准确性是唯一核心目标。Benchmark方面，TAC SCM 2005是公开的多智能体供应链管理标准竞赛任务，本文在第5-6节将其作为核心评价场地，并与真实制度、Markov/指数平滑预测方法以及不同GMM配置进行比较，结果直接支撑制度预测性能的核心主张。因此满足两个模块要求，strict_include=true。
- 置信度：0.74

### Evolutionary approach to the development of decision support systems in the movie industry 

- 年份/期刊：2009 / Decision Support Systems
- DOI：10.1016/j.dss.2008.12.008
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：净边际利润（net margin）；影院上座率（attendance）
- Benchmark 状态：benchmark_comparison_central
- 参照点：Rotterdam + The Hague（控制城市，无DSS）；January–August 2001 base period（基期）
- Benchmark 表述引文：Section 5.1（Net margin impact）：Two other large cities in the same “Randstad region” of Holland, Rotterdam and The Hague as well as a base period, January–August 2001 were chosen as benchmarks.
- Benchmark 评价：在净边际利润影响评价中，以Rotterdam + The Hague两个未使用DSS的城市以及2001年1-8月基期作为benchmarks，通过准实验设计比较了Pathé Amsterdam（DSS支持）在2001年9月至2002年2月实施期的实际净边际利润与投影（无DSS）净边际利润，得出€277,959的相对提升，再考虑特许经营收入后总提升约€342,000，年化后约$900,000。
- 判定理由：核心评价指标为净边际利润，来自财务核算和准实验对比，完全客观；该指标提升是排片DSS的主要目标和核心贡献，无并列的主观成功标准或独立理论贡献。Benchmark表述明确出现于5.1节评价语境，以Rotterdam + The Hague和基期作为对照参照点，直接支撑净边际利润提升的核心主张，满足benchmark比较中心地位。因此两个模块均通过。
- 置信度：0.8

### Financial time series forecasting using independent component analysis and support vector regression 

- 年份/期刊：2009 / Decision Support Systems
- DOI：10.1016/j.dss.2009.02.001
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：RMSE；NMSE；MAD；DS；CP；CD
- Benchmark 状态：benchmark_comparison_central
- 参照点：Random walk；SVR
- Benchmark 表述引文：Section 5.3 Robustness evaluation: 'it can be observed that the proposed ICA–SVR method outperforms the other benchmarking tools under all four different ratios in terms of the RMSE and DS criteria.'
- Benchmark 评价：在Nikkei 225和TAIEX两个数据集上，使用60%、70%、80%、90%四种训练/测试比例，比较ICA-SVR与random walk和SVR模型的RMSE和DS。结果显示ICA-SVR在所有比例和两个数据集上都优于其他基准工具。
- 判定理由：文章以提升金融时间序列预测的客观误差（RMSE/NMSE/MAD）和方向准确率（DS/CP/CD）为唯一核心目标与贡献，所有成功指标均为客观可计算数值，不依赖主观评价；全文在Robustness evaluation部分明确使用'benchmarking tools'一词，将random walk和SVR作为基准工具进行比较，该比较位于实验评价部分且直接支撑核心提升主张。因此两个模块均通过，strict_include=true。
- 置信度：0.95

### Histogram distance-based Bayesian Network structure learning: A supervised classification specific approach 

- 年份/期刊：2009 / Decision Support Systems
- DOI：10.1016/j.dss.2009.07.010
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：分类准确率（validated classification accuracy）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：UCI Machine Learning Repository（UCI 数据集：Breast、Cars、Cleveland、Diabetes、Glass、Iris、Vehicle、Vote 等）
- 参照点：K2 度量（Cooper-Herskovits metric）；Euk/KL/Manh/KS/χ2/Int 等其他直方图距离度量；Naive Bayes 分类器
- Benchmark 表述引文：第 6 节 Experimental setup：'some datasets were selected from the UCI repository of machine learning datasets [4], as listed in Table 1... We used 10-fold cross-validation [59] to get a validated classification accuracy.' 作者将 UCI 作为公开标准数据集来源，并在其上评估新方法。
- Benchmark 评价：在 UCI 数据集的 14+11 个标准分类任务上，用 K2 和 B 结构学习算法配合不同度量，报告 10 折交叉验证分类准确率；核心结果是 Jeff 度量在 11 个数据库中有 7 个优于 K2，25 个数据库总体 15:10 优于 K2。
- 判定理由：核心成功指标是 UCI 标准分类数据集上的 10 折交叉验证分类准确率，属于固定事实标签上的客观性能；全文研究问题、实验设计和贡献声明均围绕分类准确率/分类能力提升展开，无主观或并列核心目标。评价场地明确命名为 UCI Machine Learning Repository，并有 K2、Naive Bayes、其他距离度量等明确参照点，benchmark 结果直接支持新度量分类性能更优的核心主张。
- 置信度：0.78

### Identity disclosure protection: A data reconstruction approach for privacy-preserving data mining 【全文无benchmark字样-需人工复核】

- 年份/期刊：2009 / Decision Support Systems
- DOI：10.1016/j.dss.2009.07.003
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：记录链接率（RL ratio）；分类准确率（Accuracy）；简单统计误差（ADIM/ADIFC）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：UCI Machine Learning Repository - Diabetes；UCI Machine Learning Repository - German Credit
- 参照点：原始数据（Original）；仅聚合和交换（Aggregate and swap only）；不同匿名参数 k=2, 6, 10
- Benchmark 表述引文：Section 5：'Both datasets were taken from the Machine Learning Repository of the University of California at Irvine [17]'，并随后命名 Diabetes 和 German Credit、描述其规模与属性。
- Benchmark 评价：在 UCI Diabetes 和 German Credit 上，对原始数据、仅聚合/交换、以及聚合/交换+GA 在 k=2/6/10 下的重建结果进行比较，报告 C4.5 和 SVM 的 RL、Accuracy、FN/FP 和简单统计误差。
- 判定理由：文章的核心目标是通过数据重建方法实现k-匿名隐私保护，同时保持分类准确率；核心指标（记录链接率、分类准确率、简单统计误差）均是可确定性计算的客观指标，无主观量表或专家质量评分。实验在 UCI Diabetes 和 German Credit 两个命名公开标准数据集上进行，并以原始数据、仅聚合/交换以及不同k值作为明确参照点，基准评价支撑了“显著降低披露风险、同时保持合理数据效用”的核心主张。因此两个模块均通过，严格纳入。
- 置信度：0.68

### Neural network earnings per share forecasting models: A comparison of backward propagation and the genetic algorithm 

- 年份/期刊：2009 / Decision Support Systems
- DOI：10.1016/j.dss.2008.12.011
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：平均绝对百分比误差（MAPE）；均方误差（MSE）
- Benchmark 状态：benchmark_comparison_central
- 参照点：ULM.1-ULM.4：单变量线性/ARIMA 基准模型；MLM.1-MLM.2：多变量线性回归基准模型；UBP：反向传播估计的单变量神经网络；MBP：反向传播估计的多变量神经网络；RULM、RMLM：扩展自变量线性回归模型
- Benchmark 表述引文：第4节 Analysis 中明确写道：‘Given this conflicting evidence, we will use all three models as benchmarks to evaluate the performance of our univariate NN models.’ 同时，‘This model serves as a benchmark for evaluating the value of the fundamental signals…’。这是作者在评价设计中把 ULM 等既有模型作为比较基准的明确表述。
- Benchmark 评价：将遗传算法估计的神经网络模型（UGA、MGA）与 ULM.1-ULM.4、MLM.1-MLM.2、BP 估计的神经网络（UBP、MBP）以及扩展线性模型（RULM、RMLM）在相同 Compustat EPS 数据上比较一步前瞻预测精度；表4-表7报告 MAPE、MSE、大误差比例及 Friedman 检验排名，结果显示 GA 模型精度显著更优。
- 判定理由：客观指标：EPS 预测误差（MAPE/MSE）是对外部会计事实的确定性预测误差，完全客观；核心目标：全文唯一核心是证明用遗传算法估计神经网络权重可显著提升 EPS 预测精度，没有并列的主观或理论性核心贡献；benchmark：文章虽未使用公开命名数据集，但在评价设计中明确以 ULM/MLM 等模型作为 benchmarks，并将 GA 模型与 BP、线性基准等显式参照比较，benchmark 结果是核心提升主张的关键证据。因此 strict_include=true。
- 置信度：0.95

### Short-term prediction models for server management in Internet-based contexts 

- 年份/期刊：2009 / Decision Support Systems
- DOI：10.1016/j.dss.2009.07.014
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：预测准确性（NMAE）；运行时计算开销
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：TPC-W
- 参照点：EWMA；LR；AR；Static-ARIMA；Dynamic-ARIMA
- Benchmark 表述引文：Section 3 / Experimental testbed: “The client requests follow the TPC-W workload model, a popular industrial benchmarking that is commonly utilized for evaluating the performance of dynamic Web-based systems.”
- Benchmark 评价：在基于 TPC-W 工作负载模型构造的多层 Web 测试床上，对 CPU 利用率和磁盘吞吐量等内部资源数据应用所提出的 DFT 滤波与 AP 自适应预测模型；在 Stable、Realistic 1、Realistic 2 三种工作负载场景下，以 NMAE 为指标比较 AP 与 EWMA、LR、AR、Static-ARIMA、Dynamic-ARIMA 在不同预测窗口 k 下的预测误差。
- 判定理由：核心目标是提升短期预测准确性，使用 NMAE 和 CPU 时间等完全客观、可测量、无人类语义评价的指标；全文无主观成功标准，也无并列核心贡献。benchmark 方面，明确命名 TPC-W 作为工业 benchmark，并以其工作负载模型构造评价场景；在该场景下将 AP 模型与 EWMA、LR、AR、Static/Dynamic ARIMA 等明确参照点进行比较，结果用于支撑核心的预测精度提升主张。因此严格包含条件成立。
- 置信度：0.85

### Software project effort estimation with voting rules 

- 年份/期刊：2009 / Decision Support Systems
- DOI：10.1016/j.dss.2008.12.002
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：pred(25)；MMRE (Mean Magnitude of Relative Error)；MdMRE (Median Magnitude of Relative Error)
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：COCOMO data set；Albrecht data set；ERP data set
- 参照点：Basic COCOMO model；Linear regression；Neural network；Grey relational analysis；Case-based reasoning；Classification and regression trees；Regression analysis；Genetic programming；DEA；Analogy-based estimation
- Benchmark 表述引文：Section 5.1: 'The COCOMO Project Data Base ... has been used as a data base for many software project effort estimation methods because of its ready availability and the possibility of comparison with other approaches.' 该表述将 COCOMO 等公开数据集作为评价场地；Section 5 的 Table 4 直接命名为'Estimation accuracy for all data sets'，列出与既有方法的比较。
- Benchmark 评价：在 COCOMO、Albrecht、ERP 三个数据集上，采用 jackknife 方法评价社会选择投票规则（Copeland、Maximin、Borda，二值及加权模型）的工作量估算准确度，报告 pred(25)、MMRE、MdMRE，并与表中的既有方法（COCOMO Basic、线性回归、神经网络、灰色关联、CBR、回归树、遗传规划、DEA、类比法等）进行比较。
- 判定理由：论文的核心目标是提出并验证一种软件工作量估算方法，其成功标准是完全客观的预测误差指标（pred(25)、MMRE、MdMRE），基于公开数据集中的实际工作量计算，无任何主观构念作为核心成功标准；评价在多个公开标准数据集（COCOMO、Albrecht）上进行，并与多个既有方法（COCOMO Basic、回归、神经网络、CBR、灰色关联等）比较，符合命名式 benchmark 门槛。因此同时满足客观指标唯一核心目标和明确 benchmark 表述两个条件，予以纳入。
- 置信度：0.9

### A hybrid approach for efficient ensembles 

- 年份/期刊：2010 / Decision Support Systems
- DOI：10.1016/j.dss.2009.06.007
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：分类均方误差（MSE）；分类准确率（Accuracy）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：UCI Machine Learning Repository（13个数据集：breast-w, colic, credit-a, credit-g, diabetes, heart-c, heart-h, iris, labor, lymph, sick, sonar, vote）
- 参照点：UWA（unweighted average）；VBW（variance based weighting）；EMO（Efficient Models Only）；ESW（Efficiency Score Weighting）；AdaBoost；Bagging；Random Forest
- Benchmark 表述引文：Section 5.3：'The results were compared with four benchmarks from known literature.'；结论部分：'as indicated by outperforming all other benchmarking approaches.'
- Benchmark 评价：在13个UCI数据集上，用分层10折交叉验证评价DEA+Stacking（DST）方法，并与UWA、VBW、EMO、ESW四个已知基准组合方法以及AdaBoost、Bagging、Random Forest对比；报告MSE和配对t检验，平均MSE从ESW的0.163降至0.074，且显著优于全部基准方法。
- 判定理由：客观指标方面，核心成功指标是分类MSE/准确率，由分类器输出与UCI数据集中的既有类标签计算，完全客观且可复核。唯一核心目标方面，研究问题、设计目标、实验评价和贡献声明均围绕提升集成分类性能展开，没有主观结果或并列的核心贡献。Benchmark方面，作者在13个UCI标准数据集上明确使用benchmark字样进行了系统比较，与UWA、VBW、EMO、ESW以及AdaBoost、Bagging、Random Forest等明确参照点对比，且benchmark结果（MSE下降和显著性检验）是支撑核心提升主张的关键证据。因此两个模块均通过，strict_include=true。
- 置信度：0.95

### Application of a hybrid of genetic algorithm and particle swarm optimization algorithm for order clustering 

- 年份/期刊：2010 / Decision Support Systems
- DOI：10.1016/j.dss.2010.05.006
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：SED（簇内欧氏距离和）；生产准备时间、总生产时间、机器闲置时间
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：Iris；Glass；Vowel；Wine
- 参照点：GA；GKA；PSO；PSKO；GA-PSO；GA-PSKO
- Benchmark 表述引文：摘要表述：“Simulational results via Iris, Glass, Vowel and Wine benchmark data sets indicate that the proposed evolutionary-based clustering algorithm is more accurate than the GA-based and PSOA-based clustering algorithms.”；第4节表述：“This section applies some benchmark data sets to assess the proposed algorithm, HGAPSOA, in comparison with GA, GKA, PSO, PSKO, GA-PSO and GA-PSKO.”
- Benchmark 评价：在UCI的Iris、Glass、Vowel、Wine四个公开benchmark数据集上评价HGAPSOA及GA、GKA、PSO、PSKO、GA-PSO、GA-PSKO六种对比算法，使用SED作为性能指标，报告30次运行的平均值与标准差，并进行Mann-Whitney U显著性检验；结果显示HGAPSOA在四个数据集上的平均SED均最低。
- 判定理由：文章以完全客观的SED和实际生产时间/机器闲置时间作为核心成功指标；研究目标明确为通过订单聚类和HGAPSOA算法提升这些客观指标，且没有并列的主观核心目标或理论核心贡献。同时，文章明确将Iris、Glass、Vowel、Wine作为benchmark数据集，并在实验评价部分对HGAPSOA与多种baseline算法进行SED比较，benchmark结果直接支撑核心提升主张。因此三个模块均通过，strict_include为true。
- 置信度：0.97

### Classification by vertical and cutting multi-hyperplane decision tree induction 

- 年份/期刊：2010 / Decision Support Systems
- DOI：10.1016/j.dss.2009.06.004
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：分类准确率（LOO命中率）；计算时间（每次LOO测试的秒数）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：Japanese Banks data set (Sueyoshi, 2001)；Wisconsin Breast Cancer database (UCI repository)
- 参照点：Glen (2004) piecewise-linear model；SVM (SMO/Weka)；OC1；VDT模型；CDT模型（不同ε参数）
- Benchmark 表述引文：引言：‘report on computational tests that evaluate the accuracy on two well-established benchmark data sets to demonstrate the advantages of our approaches with respect to state-of-the-art alternatives.’；实验部分：‘We tested our models on two benchmark data sets from real-world applications’
- Benchmark 评价：在两个基准数据集上，以留一法比较VDT、CDT、Glen模型、SVM和OC1的LOO命中率与时间；表格1-4报告了不同分离带宽度下的结果，并对CDT与Glen进行配对t检验
- 判定理由：客观指标（分类准确率和计算时间）是全文唯一核心目标和核心贡献，不存在主观量表或理论机制等并列核心目标；分类标签为事实状态，性能指标客观可审计。全文在实验部分明确使用两个命名基准数据集（Japanese Banks和UCI Wisconsin Breast Cancer），并明确以benchmark表述进行系统化基准评价，结果与Glen、SVM、OC1等多个参照点比较，benchmark结果直接支撑核心改进主张。因此两个模块均通过，strict_include=true。
- 置信度：0.95

### Comparative study of adaptability and flexibility in distributed manufacturing supply chains 

- 年份/期刊：2010 / Decision Support Systems
- DOI：10.1016/j.dss.2009.09.001
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：总系统成本；顾客需求满足率（fill rate）
- Benchmark 状态：benchmark_comparison_central
- 参照点：stochastic order-up-to policy / stochastic model（内部基准）；flexible MTO vs adaptive MTO（两种机制间的比较）
- Benchmark 表述引文：Section 3.1: “This forms the basis of the stochastic model in this study which is considered as the benchmark of the proposed coordination mechanisms.” 作者明确将stochastic order-up-to policy模型作为所提协调机制的benchmark。
- Benchmark 评价：在仿真实验中，将flexible MTO和adaptive MTO两种协调机制与stochastic model（基准）比较，报告总系统成本改善百分比（Figs.1-3, Eq.20）和fill rate改善百分比（Figs.4-5, Eq.22），并用t检验验证成本改善的显著性（Table 5）。
- 判定理由：文章以总系统成本和顾客需求满足率这两个完全客观、可由仿真计算直接确定的运营指标作为核心绩效结果；核心目标是研究并改进MTO供应链中引入flexibility和adaptability后的客观绩效。作者在Section 3.1明确将stochastic model称为所提机制的benchmark，并在实验结果中以其为参照计算改善百分比和显著性检验。满足客观指标、唯一核心目标和明确benchmark三方面条件。
- 置信度：0.88

### Making words work: Using financial text as a predictor of financial events 

- 年份/期刊：2010 / Decision Support Systems
- DOI：10.1016/j.dss.2010.07.012
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：分类准确率 (accuracy)；Type I / Type II 错误率
- Benchmark 状态：benchmark_comparison_central
- 参照点：Altman (1968) Z-score 模型；Beneish (1999) 欺诈检测比率；文本单独方法（作为对比自身）；文本+定量组合方法
- Benchmark 表述引文：引言中明确提出: 'As a benchmark, we compare the results of our text method to traditional prediction methods (using quantitative financial variables).'（位置：Introduction段）；4.4节进一步具体实施：'We further test the methodology by comparing it to quantitative methods used for both bankruptcy and fraud detection.'（位置：Section 4.4）
- Benchmark 评价：在自建的破产数据集（78对）和欺诈数据集（61对）上，将所提出的文本方法（MD&A文本生成的token向量+SVM）与经典的定量模型Altman（1968）Z-score（破产）和Beneish（1999）比率（欺诈）进行基准比较，使用留一法交叉验证报告准确率和错误率；同时测试文本与定量变量的组合效果。结果显示文本单独优于或接近定量方法（破产80% vs 66.67%，欺诈75.41% vs 40.16%），组合后达到最优（83.87%和81.97%），从而支撑了文本信息具有预测价值且与定量信息互补的核心主张。
- 判定理由：客观指标方面，文章的预测目标是破产和欺诈两个完全客观的事实状态，评价指标为分类准确率和错误率，均为确定性计算；全文核心研究问题、设计目标、评价结构（留一法交叉验证、替代/互补测试）和贡献声明均围绕提升预测性能展开，不存在主观成功标准或并列核心目标。benchmark方面，引言明确使用'As a benchmark'陈述将文本方法与传统定量预测方法比较，并在4.4节实施该基准评价，比较对象包括Altman（1968）Z-score和Beneish（1999）比率等经典模型，结果明确展示文本方法的提升及组合数据的互补优势，该基准比较直接支撑了'文本信息可预测财务事件且补充定量信息'的核心主张。因此两个模块均通过，strict_include为true。
- 置信度：0.95

### Predicting the length of hospital stay of burn patients: Comparisons of prediction accuracy among different clinical stages 

- 年份/期刊：2010 / Decision Support Systems
- DOI：10.1016/j.dss.2010.09.001
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：住院天数预测误差（MAE、MRE）
- Benchmark 状态：benchmark_comparison_central
- 参照点：线性回归分析（linear regression analysis）；M5模型树回归；SVM回归；不同临床阶段（admission/acute/post-treatment）互为比较
- Benchmark 表述引文：摘要及第4节明确写出“using linear regression analysis as our performance benchmark”，将线性回归作为性能基准；引言和结论也重复该表述。
- Benchmark 评价：在1080例烧伤病例上，以线性回归分析为基准，评价M5和SVM回归在admission、acute、post-treatment三个临床阶段的LOS预测效果，报告MAE/MRE并进行统计显著性检验。
- 判定理由：目标指标为住院天数预测误差（MAE/MRE），基于实际LOS这一客观事实，不涉及主观评价；研究问题、评价和贡献均围绕预测准确率的提升与比较，客观指标是唯一核心目标。全文存在明确benchmark表述：以线性回归分析为性能基准，并在实证评价中与M5、SVM回归比较，基准比较结果直接支撑核心预测效果主张。因此两个模块均通过，strict_include=true。
- 置信度：0.72

### Visualizing social network concepts 

- 年份/期刊：2010 / Decision Support Systems
- DOI：10.1016/j.dss.2010.02.001
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：任务准确率（effectiveness）；任务完成时间（efficiency / time-to-task）
- Benchmark 状态：benchmark_comparison_central
- 参照点：基准系统（benchmark system）：基于 Fruchterman-Reingold 力导向布局算法的传统节点-链接可视化，节点大小按度中心性比例调整
- Benchmark 表述引文：摘要：'compared with the benchmark system, the NetVizer system facilitated better understanding...'；第5.1节标题为'Selection of the benchmark system'，并称'We refer to this as the benchmark system in the remainder of this paper.'
- Benchmark 评价：作者将 NetVizer 与一个基于力导向布局并稍作修改的基准可视化系统在同一犯罪网络数据上进行比较，通过受试者完成七项社会网络概念理解任务来评价；结果表3和表4报告了准确率和完成时间的统计比较，并用这些结果支撑 NetVizer 在 betweenness centrality、gatekeeper identification、structural similarity 等概念理解上的提升。
- 判定理由：核心指标是任务准确率和完成时间，均由客观任务答案和秒表计时得到，属于可观测客观绩效；论文没有将主观量表作为核心成功标准。核心目标是提出并验证以网络概念理解任务客观绩效提升为导向的概念可视化方法，没有并列的同等核心贡献。全文存在明确且处于评价语境的 benchmark 表述（自建基准系统），并以该基准比较结果作为核心改进主张的证据，因此同时满足两个模块的门槛。
- 置信度：0.94

### A hybrid SARIMA wavelet transform method for sales forecasting 【全文无benchmark字样-需人工复核】

- 年份/期刊：2011 / Decision Support Systems
- DOI：10.1016/j.dss.2010.12.002
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：平均绝对百分比误差（MAPE）；均方误差（MSE）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：Time Series Data Library 中的 Monthly Australian sales of sparkling wine；Australian Bureau of Statistics 的 Monthly production of woolen yarn in Australia
- 参照点：pure SARIMA；CSD+LESA；Exponential Smoothing (ES)；Evolutionary Neural Network (ENN)
- Benchmark 表述引文：Section 4.3: 'A publicly available data set, Monthly Australian sales of sparkling wine from Time Series Data Library http://www-personal.buseco.monash.edu.au/~hyndman/TSDL/, is used in this analysis.' 以及 'Another publicly available time series is ten years data of monthly production of woolen yarn in Australia (Australian Bureau of Statistics)'。这些公开数据集被明确命名并作为方法比较的评价场地。
- Benchmark 评价：在两组公开时间序列数据上分别对SARIMA、SW、CSD+LESA进行预测比较，报告MAPE、MSE和BIC；在真实时尚数据上还进一步比较SW、SARIMA、CSD+LESA、指数平滑（ES）和进化神经网络（ENN）的MAPE与运行时间。公开数据上的比较结果是论文论证SW优于CSD+LESA、并给出适用条件的重要证据。
- 判定理由：核心指标是销售预测精度（MAPE/MSE），属于完全客观可测指标；全文研究问题、实验评价和结论均围绕提高预测精度展开，并进一步用这一目标指导方法选择，未发现其他并列的主观或理论核心目标。文章在评价部分明确使用两个公开时间序列数据集作为比较场地，并与SARIMA、CSD+LESA等明确参照方法进行MAPE/MSE对比，benchmark证据直接支撑核心精度提升主张。因此两个模块均通过，strict_include=true。
- 置信度：0.78

### An intraday market risk management approach based on textual analysis 

- 年份/期刊：2011 / Decision Support Systems
- DOI：10.1016/j.dss.2010.08.019
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：分类性能：accuracy、precision、recall、F1、AUC；模拟期权策略收益：分类方法选择正类后的跨式期权多头收益均值
- Benchmark 状态：benchmark_comparison_central
- 参照点：R_LONG（all-long straddle benchmark）：对所有423条披露建立多头跨式期权；75% guessing equivalent benchmark：将全部样本预测为负类时的准确率基线
- Benchmark 表述引文：Section 6.2: "The classiﬁers’ return populations are also compared to a benchmark strategy $(R_{LONG})$"；同时 Section 5.1 提到 "above the 75% guessing equivalent benchmark"。
- Benchmark 评价：在模拟评估中，将四种分类器在设定不同误分类成本下的收益均值与对所有事件都建立多头跨式期权的基准策略（R_LONG）进行比较，并通过t检验验证分类方法是否显著优于该基准。模拟评估是证明文本挖掘方法能识别高风险事件的核心证据。
- 判定理由：本研究的核心目标是用文本挖掘方法识别伴随日内超常波动的公司披露，核心成功指标全部为客观计算得到的分类性能和基于真实价格的模拟期权收益，无任何主观构念或并列核心目标。全文存在明确的 benchmark 表述：第6节将分类方法收益与 all-long 基准策略 R_LONG 比较，且该比较是支撑方法有效性主张的核心证据；第5节也提及75%猜测等效基准。因此客观指标、唯一核心目标和 benchmark 三方面均通过。
- 置信度：0.95

### CLAP: Collaborative pattern mining for distributed information systems 

- 年份/期刊：2011 / Decision Support Systems
- DOI：10.1016/j.dss.2011.05.002
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：端到端系统运行时间；站点间消息交换开销
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：IBM Quest synthetic data generator 生成的 SD/WS 数据库（表2标题为 Benchmark database characteristics）；表4定义的四类基准查询 Q1-Q4
- 参照点：SQLP（SeQuentiaL Pattern mining）；PALP（PAralleL Pattern mining）；不使用Bloom filter的独立挖掘/stand-alone FP-growth（图6中的对比基准）
- Benchmark 表述引文：Section 6.1.3: “The experiments select a number of queries (listed in Table 4) as benchmarks which are provided to a dedicated master site.” 另外表2标题为“Benchmark database characteristics”。
- Benchmark 评价：在SD/WS两组基准数据库上，使用Q1-Q4基准查询对CLAP、SQLP、PALP三种框架进行系统评价；比较运行时间、消息大小和可回答性。结果显示CLAP在多数支持度设置下运行时间最短，并能回答SQLP/PALP无法回答的Q2/Q3。
- 判定理由：该文核心是设计并验证CLAP分布式模式挖掘框架，以完全客观的运行时间、消息开销和模式发现能力作为成功标准；没有任何主观量表或人类语义评价作为核心指标。实验部分明确选择一组查询作为benchmarks，并在SD/WS基准数据库上以SQLP、PALP作为显式比较对象，证明CLAP的运行时间提升和额外模式发现能力。因此客观指标、唯一核心目标和benchmark门槛均满足。
- 置信度：0.88

### Collaborative user modeling for enhanced content filtering in recommender systems 

- 年份/期刊：2011 / Decision Support Systems
- DOI：10.1016/j.dss.2011.01.012
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：Hit Rate (HR) 命中率；Reciprocal Hit Rank (RHR) 倒数命中排名
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：MovieLens（MLens）；NSF research award abstracts（NSF）
- 参照点：UCF（user-based collaborative filtering）；ICF（item-based collaborative filtering）；NB（naïve Bayes probabilistic learner）；VT（TF-IDF vector space model）；初始用户模型M（用于消融式比较）
- Benchmark 表述引文：Section 6：“we empirically evaluate the proposed approach and compare its performance against that of the benchmark algorithms.”；Section 6.2：“Our top-N recommendation strategy (M+) was then compared with the benchmark algorithms.”；Section 6.3.3：“showing how M+ outperforms the benchmark methods.”
- Benchmark 评价：在NSF和MovieLens两个数据集上，以固定训练/测试划分构建用户模型，将所提M+与UCF、ICF、NB、VT四种基准算法比较，并报告不同N值和邻域规模下的HR和RHR。结果表和图明确显示M+多数情况下优于基准方法。
- 判定理由：该文是推荐系统方法论文，核心目标是提升Top-N推荐质量，HR和RHR是唯一核心成功指标且完全客观。全文没有用户调研、主观量表或专家评分作为成功标准；也没有将理论机制、组织变革、政策建议等作为并列核心贡献。实验部分明确使用“benchmark algorithms/benchmark methods”的基准评价表述，在MovieLens和NSF数据集上与UCF、ICF、NB、VT等明确参照点比较，benchmark结果直接支撑其核心改进主张。两个模块均通过，strict_include=true。
- 置信度：0.95

### Comparative issues in large-scale mean–variance efficient frontier computation 

- 年份/期刊：2011 / Decision Support Systems
- DOI：10.1016/j.dss.2010.11.018
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：计算时间（CPU time）
- Benchmark 状态：benchmark_comparison_central
- 参照点：Risk Solver Platform 9.5；Matlab 2009a (QUADPROG)；LINGO 11；Cplex 11.1 (默认)；CIOS（参数二次规划）；离散方法 vs 参数方法
- Benchmark 表述引文：摘要：'conduct experiments ... to present an overall picture of the situation and establish benchmarks in the large-scale arena'；引言：'the goal is for a robust set of benchmarks to emerge'；第4节：'we will use the times experienced to compute the efficient frontiers of 100% dense covariance matrix problems to form the benchmark results reported in this paper'。
- Benchmark 评价：论文在 500、1000、1500、2000、3000 证券的100%密集协方差矩阵 Markowitz 问题上，对 e-约束法、λ-参数法和参数二次规划（CIOS）以及 Risk Solver Platform、Matlab、LINGO、Cplex 等优化器进行系统化时间基准评价。表4-6显示 CIOS 计算整条有效前沿的时间远小于离散方法计算单点的时间（如 n=1000 时 CIOS 5.3s vs Cplex 单点 6.0s；n=2000 时 CIOS 23.1s vs Cplex 单点 38.6s）。该基准结果用于支持参数二次规划方法在大规模前沿计算中的核心主张。
- 判定理由：客观指标：核心指标为计算有效前沿所需的 CPU 时间，是完全客观可测的技术资源指标。唯一核心目标：全文从问题提出、实验设计到结论均围绕计算时间基准比较和参数二次规划方法的性能优势展开，不存在主观体验、理论机制或其他并列核心贡献。Benchmark：作者明确使用 benchmark/benchmarking 表述建立大规模有效前沿计算时间基准，并在实验和结果部分以此支撑核心速度提升主张，且有多重参照点比较。因此 strict_include=true。
- 置信度：0.95

### Estimating the effect of word of mouth on churn and cross-buying in the mobile phone market with Markov logic networks 

- 年份/期刊：2011 / Decision Support Systems
- DOI：10.1016/j.dss.2011.01.002
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：流失预测的准确率（Accuracy）；流失预测的敏感度/召回率（Sensitivity）；流失预测的特异度与精确率；游戏下载（交叉购买）预测的准确率与敏感度
- Benchmark 状态：benchmark_comparison_central
- 参照点：logistic regression (T1) 基准模型；C4.5 decision tree 作为额外基准；六种 propositionalization 设置 (T2.1-T2.6)；三种 MLN 设置 (T3.1-T3.3)
- Benchmark 表述引文：Section 4.3: 'we compared MLN and propositionalization and benchmarked it against logistic regression on the same data set'；Section 1.2贡献声明：'we provide results comparing MLNs and propositionalization with a traditional logit model ignoring information about communication neighbors as a benchmark'；Section 5反复称logistic regression为'benchmark model'和'benchmark logistic regression'。
- Benchmark 评价：研究在专有匿名电信数据集上，对流失和游戏下载两个预测任务运行九种设置（T1 logistic基准、T2.1-T2.6 propositionalization、T3.1-T3.3 MLN），报告Accuracy/Precision/Sensitivity/Specificity和ROC曲线；结果显示T2.1-T2.4的准确率和敏感度优于logistic基准，MLN在ROC上优于基准但在敏感度上未优于最佳propositionalization，从而支持'网络邻域信息提升客观预测指标'的核心主张。
- 判定理由：核心结果指标（流失、游戏下载预测的准确率、敏感度、特异度、精确率、ROC）均基于运营商日志中的实际行为标签，不依赖人类感受或语义评价，属于客观固定事实标签；研究问题、评价结构和贡献声明均围绕通过社交网络信息提升这些客观预测指标展开。同时全文存在明确的benchmark表述：作者在研究方法与结果部分明确将logistic回归作为benchmark，并在同一专有数据集上比较了logistic、propositionalization和MLN，结果表的精确数值和ROC曲线直接支持客观指标提升主张。因此两模块均通过，strict_include=true。
- 置信度：0.72

### Multi-objective design of hierarchical consensus functions for clustering ensembles via genetic programming 

- 年份/期刊：2011 / Decision Support Systems
- DOI：10.1016/j.dss.2011.01.014
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：校正兰德指数（Corrected Rand, CR）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：UCI repository 的 iris 数据集；UCI repository 的 glass 数据集
- 参照点：KM；HAL；HSL；SNN；HBGF；SC；MOCK；MOCLE-H；MOCLE-M；MCHPF variants
- Benchmark 表述引文：摘要：'have been conducted on a number of artificial, benchmark and bioinformatics datasets'；第4.1节：'Two other datasets, iris and glass, taken from the UCI repository [1], are considered as benchmark.'
- Benchmark 评价：在UCI benchmark数据集iris和glass上运行MCHPF1，并与其他基础/高级聚类方法比较；结果以平均CR值列于表7、表8，并纳入第4.6节的Friedman/Nemenyi统计检验，用于支持MCHPF在聚类划分质量上的提升。
- 判定理由：客观指标方面，核心成功标准是校正兰德指数（CR），通过对比算法输出划分与已知参考结构标签计算，属于可独立于人的主观体验核验的事实性标签匹配指标；全文没有满意度、偏好、语义质量评分等主观构念。唯一核心目标是在多个数据集上稳健地提升聚类划分质量，研究问题、实验设计和贡献声明均围绕该客观指标展开，没有并列的核心理论贡献或主观成功标准。Benchmark方面，文中明确将UCI的iris和glass称为benchmark数据集，并在实验设置中将其作为评价场地；包含与KM、HAL、HSL、SNN、HBGF、SC、MOCK、MOCLE等明确参照物的CR比较，统计检验进一步支撑MCHPF的核心提升主张。因此严格纳入。
- 置信度：0.82

### Municipal credit rating modelling by neural networks 

- 年份/期刊：2011 / Decision Support Systems
- DOI：10.1016/j.dss.2010.11.033
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：分类准确率（classification accuracy, CA_test）
- Benchmark 状态：benchmark_comparison_central
- 参照点：LR；MDA；K-means；CT；此前研究中的统计方法结果（如MDA）
- Benchmark 表述引文：第5节实验部分：'NNs are compared to other benchmark classifiers, i.e. linear regression (LR), multiple discriminant analysis (MDA), K-means algorithm, and classification tree (CT).'；同时表6标题为'Parameters of NNs and benchmark methods for municipal credit rating modelling.'
- Benchmark 评价：在自建的美国康涅狄格州市政 Moody's 评级数据集上（4类和9类评级），使用10折交叉验证评价FFNN、RBFNN、PNN、CCNN、GMDH、SVM，并与LR、MDA、K-means和CT等基准分类器进行比较。表7报告各方法CA_test；PNN在4类问题达98.8%，9类问题达96.3%，为所有方法中最高。讨论部分还将统计方法结果与此前研究中的MDA结果比较。
- 判定理由：该文以完全客观的分类准确率作为唯一核心目标，数据标签为Moody's公开评级类别，属固定事实标签；实验结果在评价部分明确与benchmark classifiers（LR、MDA、K-means、CT等）比较，且benchmark结果直接支撑核心的分类准确率提升主张。因此两个模块均通过，strict_include=true。
- 置信度：0.92

### Pairwise issue modeling for negotiation counteroffer prediction using neural networks 

- 年份/期刊：2011 / Decision Support Systems
- DOI：10.1016/j.dss.2010.11.002
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：反报价预测误差（按议题序数层级缩放的MAE百分比）
- Benchmark 状态：benchmark_comparison_central
- 参照点：Naïve模型（以对方最近一次报价作为下一反报价预测）；全议题同时输入的非线性ANN模型（NNF）；线性pairwise模型（MLRP）
- Benchmark 表述引文：第3节：'Evaluating the performance of the proposed model requires reference benchmark models. The first benchmark proposed is the naïve model...'；第5.2节：'three reference models were included in the experiments as benchmarks for the pairwise counteroffer predictions.'
- Benchmark 评价：在Inspire的Cypress/Itex谈判数据集上，将pairwise ANN（NNP）与naïve模型、全议题ANN（NNF）和线性pairwise模型（MLRP）作为基准进行比较，报告按议题等级缩放的MAE百分比，并用t检验检验假设。结果显示NNP总体误差9.25%，低于naïve（12.08%）和MLRP（10.67%），且不高于NNF（9.37%）；对排除议题的新议题预测误差9.46%，仍低于naïve（12.08%）。
- 判定理由：客观指标与唯一核心目标通过：核心目标是构建灵活的反报价预测模型，成功指标为真实谈判数据上的预测误差，测量完全来自系统日志和可复算的MAE，无主观量表或人类语义评价。Benchmark通过：作者在第3节和第5.2节明确使用benchmark指代naïve、全议题ANN和线性pairwise参照模型，并在第6节用这些基准比较检验核心预测误差假设，且均有明确对照。因此strict_include=true。
- 置信度：0.95

### Predicting corporate bankruptcy using a self-organizing map: An empirical study to improve the forecasting horizon of a financial failure model 

- 年份/期刊：2011 / Decision Support Systems
- DOI：10.1016/j.dss.2011.04.001
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：企业破产预测正确分类率
- Benchmark 状态：benchmark_comparison_central
- 参照点：判别分析 (Discriminant Analysis)；逻辑回归 (Logistic Regression)；神经网络 (Neural Network)；Cox比例风险模型 (Cox's model)
- Benchmark 表述引文：第3.3节明确将判别分析称为'经常被用作其他模型预测技能基准的方法'，并将Cox生存分析模型作为'轨迹方法的特殊基准'；第3.3.2节标题直接为'Methods used as benchmark'，然后在4.3节将轨迹模型与这些基准方法在1、2、3年视界上进行系统比较。
- Benchmark 评价：在法国企业破产测试样本上，将所提出的轨迹模型与判别分析、逻辑回归、神经网络和Cox比例风险模型四个基准方法进行比较，报告了破产前1、2、3年的正确分类率（表8），并给出统计显著性检验（表9、11）。结果显示轨迹模型在多期视界上正确分类率下降更小，尤其3年视界显著优于其他方法。
- 判定理由：该文以提升破产预测在1至3年视界上的正确分类率为唯一核心目标和贡献，该指标基于法律破产事实标签的确定性分类，属于客观固定事实标签预测性能。全文存在明确的benchmark表述：第3.3.2节标题'Methods used as benchmark'，并将判别分析、逻辑回归、神经网络和Cox模型作为基准方法，在测试样本上系统比较，结果用于支撑轨迹模型预测稳定性的核心改进主张；比较具有明确参照点并附统计检验。因此两模块均通过，strict_include为true。
- 置信度：0.95

### Robust ensemble learning for mining noisy data streams 

- 年份/期刊：2011 / Decision Support Systems
- DOI：10.1016/j.dss.2010.11.004
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：预测准确率（Aacc）及派生排序指标（AR、#W、#L）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：KDDCUP'99 intrusion detection dataset；wireless sensor stream（公开测试数据流）
- 参照点：Tree；HE（horizontal ensemble）；WE（weighted ensemble）；VE（vertical ensemble）；AE的组件学习算法及不同HE变体
- Benchmark 表述引文：第5.3节：'we compare all ensemble methods on the KDDCUP'99 intrusion detection dataset, which is a popularly used test bed for stream data mining'；第5.4节：'AE is the most time-consuming method among all benchmark approaches'，并在公开无线传感器数据流上评价平均预测精度与训练时间。
- Benchmark 评价：在KDDCUP'99上构造随机选择、随机噪声、重排、重排噪声四种数据流，将AE与Tree、HE、WE、VE比较，报告Aacc、AR、SR、#W、#L；在无线传感器数据流上比较AE与其组件算法、不同HE变体的平均准确率和系统训练时间。结果表显示AE在含噪场景下多数取得最高准确率和最低损失次数。
- 判定理由：客观指标方面：核心成功标准为预测准确率、排序和运行时间，均由数据标签和系统时间确定性计算，不依赖主观判断；核心目标是提升含噪数据流上的预测准确率，没有其他并列核心目标。Benchmark方面：全文在评价语境中使用KDDCUP'99这一公开基准数据集和公开无线传感器测试流，并系统比较AE与Tree、HE、WE、VE等基线；这些benchmark结果正是支撑AE准确率提升的核心证据。因此两个模块均通过，strict_include=true。
- 置信度：0.97

### A brain information-aided intelligent investment system 

- 年份/期刊：2012 / Decision Support Systems
- DOI：10.1016/j.dss.2012.05.041
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：投资组合的收益率/投资表现；ABIC模型选择改进值
- Benchmark 状态：benchmark_comparison_central
- 参照点：无脑信息、仅预测收益率的投资模型（FS1/基准）；传统Markowitz组合选择模型（有效前沿）；ARMA–GARCH金融时序模型（AIC选择）；TOPIX市场指数
- Benchmark 表述引文：第5.3节：'Fixing the selected factor set and performing sequential forecasting for the remaining 20 periods, were found to result in a system performance that was clearly better than that with several benchmarks.'；第5.3.2节：'comparison of investment performance was also done using an ARMA–GARCH model, a model typically used in the field of financial statistics, as a benchmark.'；第5.3.3节：'comparison using TOPIX's rate of return as a benchmark also indicated an improvement of 4.22 basis points'；图6标题：'Use of the forecast rate of return as a predictive variable and no use of brain information whatsoever served as a benchmark.'；表3：'FS1 | Auto-correlation term (the benchmark)'。
- Benchmark 评价：在20个session中，系统用前80期学习、后20期序贯验证，将包含脑信息的系统投资收益率与几个明确基准比较：(1) 仅使用预测收益率且不使用脑信息的模型；(2) 传统Markowitz组合选择模型的有效前沿（the efficient frontier）；(3) 以AIC选择的ARMA–GARCH金融时序模型；(4) TOPIX市场指数。结果显示：相对于仅预测收益率模型平均每日改进5.28个基点（20/20 session改进）；相对于ARMA–GARCH模型平均改进33.67个基点（17/20 session改进）；相对于TOPIX平均改进4.22个基点（16/20 session改进）；14/20 session的系统收益-风险位置位于传统有效前沿的左上侧。
- 判定理由：客观指标：核心结果变量为投资收益率、风险和Sharpe比率，直接由实际市场数据和固定投资规则计算，完全客观；ABIC改进是客观统计模型选择证据。唯一核心目标：研究问题、系统设计、实验评价和贡献声明都围绕改进投资表现这一客观结果，不存在并列的用户主观体验、理论贡献或制度贡献。Benchmark：全文在实验/评价部分多次明确使用benchmark一词，并以无脑信息模型、Markowitz有效前沿、ARMA-GARCH模型和TOPIX作为明确参照点，报告了收益率的改进数值，benchmark比较直接支撑系统的核心提升主张。因此两个模块均通过，strict_include为true。
- 置信度：0.88

### A cost-sensitive technique for positive-example learning supporting content-based product recommendations in B-to-C e-commerce 

- 年份/期刊：2012 / Decision Support Systems
- DOI：10.1016/j.dss.2012.01.018
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：预测精度（accuracy）；正例与负例 F1 分数及平均 F1
- Benchmark 状态：benchmark_comparison_central
- 参照点：positive naïve Bayes (PNB)；positive example-based learning (PEBL)；COLPEL_random（替换为随机抽样）；COLPEL_single（单分类器版本）
- Benchmark 表述引文：摘要：'We evaluate the proposed method with customers' book ratings collected from Amazon.com and include two prevalent techniques for benchmark purposes; namely, positive naïve Bayes and positive example-based learning. According to our results, the proposed COLPEL technique outperforms both benchmarks, as measured by accuracy and positive and negative F1 scores.'；引言：'We empirically evaluate the COLPEL, in terms of predictive effectiveness, with book ratings collected from Amazon.com, using both PNB and PEBL techniques as performance benchmarks.'
- Benchmark 评价：在Amazon.com的36位顶级评论者的图书评分数据（SIPs/CAPs内容特征）上评价COLPEL，同时实现PNB和PEBL作为performance benchmarks；比较weighted accuracy、positive/negative F1、average F1，并报告显著性检验、参数敏感性和组件分析。
- 判定理由：客观指标：全文以分类预测的accuracy、F1为核心成功指标，标签来自Amazon评分阈值（>=4为积极），属于对固定事实标签的检测性能，不依赖人的主观评价质量；评价过程基于测试集类别计数，客观可审计。唯一核心目标：研究问题、方法设计、评价和贡献均围绕提升自动分类器预测有效性展开，没有与客观指标提升并列的主观体验、理论机制或组织变革等核心贡献。Benchmark：作者在摘要、引言和实验部分明确将PNB和PEBL称为'performance benchmarks'，并在Amazon数据上对三者进行比较；比较有明确参照对象（两个既有方法），结果表给出accuracy、F1和统计显著性，且benchmark比较直接支撑COLPEL的核心改进主张，属于benchmark_comparison_central。因此strict_include=true。
- 置信度：0.95

### A decision support system for integrating manufacturing and product design into the reconfiguration of the supply chain networks 

- 年份/期刊：2012 / Decision Support Systems
- DOI：10.1016/j.dss.2011.11.014
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：缺货量/延迟交付量（backorders）；库存水平/安全库存（inventory level/safety stock）
- Benchmark 状态：benchmark_comparison_central
- 参照点：原供应链配置（assembly sequence planning之前）；GoldSim仿真模型
- Benchmark 表述引文：第4.3节'Results and analysis'开头：'In analyzing the proposed inventory allocation model, we benchmark the original supply chain configuration before and after the assembly sequence planning.' 另一处：第6节结论中'The model validation benchmarks the proposed analytical model against the simulation model, at the same model parameters.'
- Benchmark 评价：作者将'装配序列规划前的原供应链配置'作为参照，评价'装配序列规划后的供应链配置'，通过表2与表3比较安全库存分配和库存水平；结果显示装配序列规划消除了部分库存点（如产品ABDEHI、Wheel、Pad、Stand A）的安全库存，并使总安全库存成本最小化。模型验证部分还将解析模型与GoldSim仿真模型进行benchmark对比，检验安全库存、订单率和缺货水平的一致性。
- 判定理由：核心指标backorders和inventory level均为客观可测的运营指标，不依赖人类感知或语义评价；论文的摘要、引言、结果和结论均围绕通过DSS实现供应链重构和库存分配来降低缺货与库存水平这一唯一核心目标展开，无并列主观或理论核心贡献。全文存在明确的benchmark表述：第4.3节将装配序列规划前后的供应链配置进行比较，属于评价语境，且该比较直接支持安全库存减少和总库存成本降低的核心提升主张，并有明确的参照点（规划前配置/仿真模型）。因此同时满足客观指标、唯一核心目标和明确benchmark门槛。
- 置信度：0.93

### A decision support system of vehicle routing and refueling for motor carriers with time-sensitive demands 

- 年份/期刊：2012 / Decision Support Systems
- DOI：10.1016/j.dss.2012.09.004
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：总加油成本（燃料成本）
- Benchmark 状态：benchmark_comparison_central
- 参照点：Benchmark method I: Carrier X实际路线和加油实践（购买合同）；Benchmark method II: 最优TSPTW路线+购买合同（传统成本节省方法）；Benchmark method III: 枚举法求得的TSPTWR最优解（仅实际实例）
- Benchmark 表述引文：Section 6.2 标题为 'Benchmark methods'，正文明确写道：'We compare the cost of our method with those of three benchmark methods.' 并在其后定义了三种 benchmark method（I、II、III）。
- Benchmark 评价：在三个实际实例和六个模拟实验中，将提出的方法分别与三个基准方法比较：基准方法I（Carrier X实际路线与购买合同）、基准方法II（最优TSPTW路线+购买合同）、基准方法III（枚举最优TSPTWR）。报告各方案的总加油成本，结果显示所提方法比基准II最多节省4.29%（n=20, γ=0），且在实际实例中达到最优或近优。
- 判定理由：客观指标方面：核心指标为总加油成本（燃料成本），来源于可审计的消耗量和市场价格，完全客观，且是全文唯一的核心目标与贡献；建模、求解和实验均围绕降低燃料成本展开，无主观结果指标或并列核心目标。Benchmark方面：作者在评价部分（Section 6.2）明确使用 'benchmark methods' 表述，定义三种基准方法，并以其为参照报告燃料成本节省幅度（最多4.29%），属于明确的 benchmark 比较且支撑核心主张。因此两个模块均通过，strict_include=true。
- 置信度：0.98

### A trust-semantic fusion-based recommendation approach for e-business applications 

- 年份/期刊：2012 / Decision Support Systems
- DOI：10.1016/j.dss.2012.09.005
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：平均绝对误差（MAE）；覆盖率（Coverage）
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：MovieLens dataset；Yahoo! Webscope R4 dataset
- 参照点：Resnick-UCF；Sarwar-ICF；O'Donovan-Trust；Ruiz-Semantic
- Benchmark 表述引文：在第5.3节'Benchmark algorithms'中，作者明确写道：'all obtained results of the TSF approach are compared with the performance of four benchmark user-based and item-based recommendation algorithms.' 并在第5.5节评价部分使用'improving accuracy and resolving data sparsity, CS user and CS item problems'来验证TSF相对benchmark算法的提升。
- Benchmark 评价：在MovieLens和Yahoo! Webscope R4两个数据集上，将TSF与Resnick-UCF、Sarwar-ICF、O'Donovan-Trust、Ruiz-Semantic四个基准算法进行比较，在多种邻居数量、不同的数据稀疏度、不同数量的冷启动用户/物品评分设置下，用MAE和Coverage指标度量，结果显示TSF在几乎所有条件下均优于所有基准算法。
- 判定理由：客观指标方面：全文核心目标是通过融合信任与语义信息改进推荐系统性能，核心评价指标为MAE和Coverage，两者均是可确定性计算的客观预测性能指标，不依赖于人的主观体验或语义评价，也未将用户满意度、感知质量等主观构念作为成功指标。唯一核心目标与贡献就是提升客观的推荐准确性和覆盖率，实验和结论均围绕这两个指标展开，未发现并列的理论贡献、制度建议或主观体验改善等核心目标。Benchmark方面：第5.3节明确使用“benchmark algorithms”一词，将TSF与四个既有推荐算法进行系统化基准比较；该比较位于实验评价部分，是证明TSF核心提升主张的关键证据；所有结果均有明确的对照基线（Resnick-UCF、Sarwar-ICF、O'Donovan-Trust、Ruiz-Semantic），并报告了TSF在MAE和Coverage上一致优于这些基线。两个模块均完全通过，因此strict_include为true。
- 置信度：0.98

### An adaptive learning to rank algorithm: Learning automata approach 

- 年份/期刊：2012 / Decision Support Systems
- DOI：10.1016/j.dss.2012.08.005
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：Precision at position n (P@n)；Mean Average Precision (MAP)；Normalized Discount Cumulative Gain (NDCG)
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：LETOR；TREC 2003 (Topic Distillation, TD2003)；TREC 2004 (Topic Distillation, TD2004)；OHSUMED；MQ2007
- 参照点：SVMRank；LREG；LRDRS
- Benchmark 表述引文：第4节开头：“we have conducted several simulation experiments on the renowned benchmark data collections... The datasets on which the performance of the proposed algorithm and the baselines are tested are TREC 2003 ... TREC 2004 ... OHSUMED, and MQ2007.” 第4.2节：“LETOR is a package of benchmark data sets for LEarning TO Rank released by Microsoft Research Asia”。
- Benchmark 评价：在LETOR包中的TD2003、TD2004、OHSUMED、MQ2007四个公开benchmark数据集上，使用LETOR官方Eval-Rank.pl工具评价LRUF并与SVMRank、LREG、LRDRS三个baseline比较P@n、MAP、NDCG；结果显示LRUF在几乎所有数据集和指标上明显优于三个baseline。
- 判定理由：客观指标方面：本文核心目标为提升搜索引擎排序的P@n、MAP、NDCG，这些指标基于数据集中的固定相关性标签，由标准公式和LETOR官方工具计算，完全不依赖用户或专家的主观评价；全文的研究问题、算法设计、实验和结论均围绕这一客观指标提升展开，且不存在并列的核心贡献。Benchmark方面：作者在第4节明确将TREC 2003、TREC 2004、OHSUMED、MQ2007作为“renowned benchmark data collections”，并将LETOR称为benchmark数据集包，评价位于实验部分且是支撑核心主张的主要证据；结果表与SVMRank、LREG、LRDRS三个明确baseline比较，证明的是提升而并非孤立数值。因此strict_include=true。
- 置信度：0.97

### Efficient classifiers for multi-class classification problems 【全文无benchmark字样-需人工复核】

- 年份/期刊：2012 / Decision Support Systems
- DOI：10.1016/j.dss.2012.02.014
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：分类准确率；ROC面积；假阳性率FPR；训练时间
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：segment；satimage；places；German credit；vehicle
- 参照点：C4.5；CART；SVM；NaiveBayes；GR(C4.5)；传统IG/GR特征选择；全部原始特征F vs. 本文选择特征F^
- Benchmark 表述引文：5.1节：'The five datasets used in this paper are named as segment, satimage, places, German credit, and vehicle. They are downloaded from Statlog [38], UCI [41], and StatLib [10,37]...'；且'All experimental results in this study were assessed using 10-fold cross-validation.'这构成命名式公开标准数据集benchmark评价表述。
- Benchmark 评价：在segment、satimage、places、German credit、vehicle五个公开标准数据集上，分别用原始特征F和本文选择特征F^训练C4.5、CART、SVM、NaiveBayes，并训练本文HLMC；以准确率、ROC面积、FPR和训练时间为主要结果，比较显示F^大幅缩短训练时间且准确率几乎不损失，HLMC判别能力优于多个传统分类器。
- 判定理由：该文以提升分类训练效率、保持/改善准确率和判别能力作为唯一核心目标，所有核心成功指标均为客观可计算指标；评价在公开标准数据集segment、satimage、places、German credit、vehicle上进行，并与多种显式baseline比较，benchmark评价支撑其核心改进主张。因此满足严格纳入条件。
- 置信度：0.85

### Forecasting and trading the EUR/USD exchange rate with stochastic Neural Network combination and time-varying leverage 

- 年份/期刊：2012 / Decision Support Systems
- DOI：10.1016/j.dss.2012.05.039
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：年化收益率（含/不含交易成本和杠杆成本）；信息比率（含/不含成本）；统计预测误差：MAE、MAPE、RMSE、Theil-U
- Benchmark 状态：benchmark_comparison_central
- 参照点：Naive Strategy；ARMA；MLP；RNN；Simple Average；Bayesian Average；GRR；LASSO
- Benchmark 表述引文：摘要：'This is done by benchmarking the statistical and trading performance of PSN with a Naive Strategy, an ARMA model and two different NN architectures, a Multi-Layer Perceptron (MLP) and a Recurrent Network (RNN).'；4.1 节：'we use two traditional forecasting strategies, the Naive Strategy and the Auto-Regressive Moving Average (ARMA) model, in order to benchmark the efficiency of the NNs' trading performance.'
- Benchmark 评价：在 EUR/USD ECB fixing 序列（2002–2010，最后两年为样本外）上，以 Naive、ARMA、MLP、RNN 为基准评估 PSN；以 Simple Average、Bayesian Average、GRR、LASSO 等为组合基准评估 Kalman Filter。表 3/4 报告统计性能，表 6/7/9 报告交易性能，均直接支撑 PSN 和 Kalman Filter 优于各基准的核心提升主张。
- 判定理由：客观指标：统计预测误差和交易绩效均由 EUR/USD 市场价格序列按固定规则计算，不依赖人类主观评价或语义判断。唯一核心目标：摘要、研究问题、设计、结果和贡献均围绕 PSN 及 Kalman Filter 在客观统计与交易指标上的提升展开，无并列的理论、政策或主观体验贡献。Benchmark：摘要和 4.1 节明确使用 benchmarking/benchmark models 表述，并在结果表 3/4/6/7/9 中与 Naive、ARMA、MLP、RNN 以及多种组合方法进行明确比较，该比较直接支撑核心改进主张。因此两个模块均通过，strict_include=true。
- 置信度：0.96

### Inverse matrix-free incremental proximal support vector machine 

- 年份/期刊：2012 / Decision Support Systems
- DOI：10.1016/j.dss.2012.02.007
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：运行时间/时间复杂度；预测准确率；收敛速度
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：NDC synthetic data set；UCI Mushroom data set；USPS Digit data sets；TIS biological data set
- 参照点：ISVM（增量PSVM基线）；SVCM（增量支持向量分类机）
- Benchmark 表述引文：第5.1节标题为“Benchmark data set”，并写明：“Four types of data sets (one synthetic and three real-world data sets) for binary classification problems are employed in our experiments.” 该表述位于实验部分，明确将所列公开/标准数据集作为评价场地。
- Benchmark 评价：在 NDC、UCI Mushroom、USPS 数字对和 TIS 等数据集上评价 IMISVM 与 ISVM、SVCM：图3-8比较运行时间随维度和样本数的变化，证明 IMISVM 相较于 ISVM 更高效；图9比较消除正则项后的收敛与准确率，证明 IMISVM 能保持或提升准确率并加速收敛。
- 判定理由：核心目标完全围绕客观可测的计算效率、运行时间和收敛速度，辅以外部事实标签上的分类准确率，无主观量表或语义评分；全文存在明确 benchmark 数据集节，并在这些数据集上以 ISVM/SVCM 为参照进行运行时间与准确率对比，benchmark 结果直接支撑核心效率提升主张。因此两个模块均通过，strict_include=true。
- 置信度：0.9

### Mitigating bankruptcy propagation through contractual incentive schemes 

- 年份/期刊：2012 / Decision Support Systems
- DOI：10.1016/j.dss.2012.02.003
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：破产发生次数（ANR/ANM/ANSC）；破产传播指标（CCC Lag=-1/0/+1）
- Benchmark 状态：benchmark_comparison_central
- 参照点：无任何合同情景（Benchmark）；合同有效性标准：CCC指标改善且AN指标不恶化
- Benchmark 表述引文：第5.4.1节专门以'Benchmark'为标题，原文为：'we first simulate the supply chain when no contract is applied, and summarize the corresponding CCC indexes and AN indexes under various combinations of the four parameters ... as benchmarks'。第5.2节和表3-5也反复使用'benchmark'指代无合同对照情景。
- Benchmark 评价：在第5.4节中，作者分别在RS、PD、QF合同下进行仿真，并将结果与无合同Benchmark情景在CCC和AN指标上比较；表3-5直接列出各合同的输出指标和Benchmark值，据此判断合同是否有效缓解破产传播。
- 判定理由：核心指标为仿真供应链中的破产发生次数和破产传播交叉相关，均由模拟财务规则客观计算，不涉及主观构念；全文唯一核心目标是通过合同机制降低破产发生与传播。5.4.1节明确将无合同情景作为Benchmark，并在表3-5中作为核心证据比较合同与Benchmark，满足明确的benchmark评价门槛。因此 strict_include=true。
- 置信度：0.92

### Nearest-neighbor-based approach to time-series classification 

- 年份/期刊：2012 / Decision Support Systems
- DOI：10.1016/j.dss.2011.12.014
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：漏检率 (miss rate / 假阴性率)；误报率 (false alarm rate / 假阳性率)
- Benchmark 状态：benchmark_comparison_central
- 参照点：统计转换方法 (statistical-transformation-based approach with C4.5)
- Benchmark 表述引文：第4.3节标题为 'Performance benchmark'，正文明确写道：'The statistical-transformation-based approach proposed in [32] for churn prediction of mobile telecommunications subscribers is employed as our performance benchmark.'
- Benchmark 评价：在台湾电信公司实际流失预测数据集上，将提出的 kNN-TSC（voting、weighted voting、stratified average 三种决策组合）与统计转换方法（C4.5）在 miss rate 和 false alarm rate 上比较；表2显示 kNN-TSC 总体优于 benchmark，支撑摘要和结论中的核心提升主张。
- 判定理由：本文提出并评估 kNN-TSC 时间序列分类技术，核心目标是在流失预测场景中降低漏检率与误报率；两个指标均基于客观事实标签（是否在预测期断线）可直接计算，不涉及主观评价。全文在实证部分有明确的 performance benchmark 表述（第4.3节），将所提方法与统计转换方法（C4.5）作为基准比较，表2结果直接支撑了摘要和结论中关于性能提升的核心主张。因此同时满足完全客观指标、唯一核心目标和明确 benchmark 表述的全部条件。
- 置信度：0.95

### Network optimization in supply chain: A KBGA approach 【全文无benchmark字样-需人工复核】

- 年份/期刊：2012 / Decision Support Systems
- DOI：10.1016/j.dss.2011.10.024
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：总平均成本/单位满足需求成本；需求满足率；算法收敛代数/收敛速度
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：Ding et al. [18] 的 Classic boots 供应链数值算例（需求 d=300）
- 参照点：SGA / Ding et al. [18] 已发表的现有结果（2000代收敛、最高约97.2%需求满足率）
- Benchmark 表述引文：第1节引言：'To show the efficacy of the proposed algorithm over Simple GA (SGA), a bench mark problem from the literature has been taken and it is also tested on the few moderate size of the problems.' 该句虽字面位于引言，但直接预告了第9节的基准评价，并非泛泛提及。
- Benchmark 评价：将Ding et al. [18] 的Classic boots供应链问题作为基准算例，将KBGA与SGA/文献已有结果比较：KBGA在d=300时144代收敛而SGA约为2000代；KBGA可达到接近100%的需求满足率，而SGA仅搜索到97.2%；KBGA给出的再订货点和订货量也更低。另在d=400和500上检验了KBGA的收敛性能。
- 判定理由：文章以供应链网络优化为背景，核心贡献是提出KBGA并在Ding et al.基准算例上对比SGA。核心成功指标包括总平均成本、需求满足率和收敛代数，均为可审计的客观数值指标；没有主观量表或人类语义判断作为成功标准。唯一核心目标是提升这些客观指标。虽然显式使用benchmark一词的句子位于引言，但它直接预告并支撑第9节的基准评价；该基准评价与SGA明确比较，且正是支撑核心改进主张的关键证据。因此两个模块均通过，strict_include=true。
- 置信度：0.86

### Novel linear programming approach for building a piecewise nonlinear binary classifier with a priori accuracy 【全文无benchmark字样-需人工复核】

- 年份/期刊：2012 / Decision Support Systems
- DOI：10.1016/j.dss.2011.11.006
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：分类错误率/准确率（训练集与测试集）；CPU运行时间（秒）；生成的超平面/判别面片数量
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：UCI Machine Learning Repository（Abalone, Bank, Cancer, Contraceptive, Credit, Diabetes, Heart, Housing, Ionosphere, Letter, Sonar, Spiral, Wine）；Japanese Bank dataset；合成数据集（含已知分离函数(15)与双螺旋数据集）
- 参照点：SVM(16)（5折交叉验证，Table 4）；算法单平面版本 vs 全版本；Bank数据集上的MILP方法（Better et al. [4]、Glen [15]）；双螺旋数据集上的Fung & Mangasarian结果
- Benchmark 表述引文：摘要中明确：“We compare this algorithm with a new linear SVM ... has an excellent performance on standard and synthetic data”；第5节开头：“we carried out total classification tests on several well known datasets and report our findings in Table 1”；第5.7节：“compare the algorithm's performance with the version of SVM modeled by (16)”。
- Benchmark 评价：在UCI repository多个标准数据集、Japanese Bank数据集以及带已知分离函数的合成数据上运行所提算法，报告训练/测试错误率、超平面数和CPU时间；通过5折交叉验证与SVM(16)、单平面版本等比较，用于支撑算法精度和泛化能力的核心主张。
- 判定理由：全文以构建并评估一种可先验指定精度的分段非线性二分分类器为核心，所有核心成功指标均为分类错误率/准确率、CPU时间、超平面数量等客观可审计指标；未使用主观量表或人类语义判断。数值实验明确命名UCI repository数据集、Japanese Bank数据集和合成数据集作为评价场地，并在这些标准数据上以SVM(16)等为显式参照点比较测试错误，证明算法性能提升与竞争力，因此benchmark门槛也满足。两模块均通过，严格纳入。
- 置信度：0.85

### Preprocessing unbalanced data using support vector machine 【全文无benchmark字样-需人工复核】

- 年份/期刊：2012 / Decision Support Systems
- DOI：10.1016/j.dss.2012.01.016
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：敏感性（Sensitivity）；特异性（Specificity）；准确率（Accuracy）；AUC
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：CoIL 2000 Challenge / Insurance Company Dataset（Coil dataset）
- 参照点：standalone MLP；standalone LR；standalone RF；original unbalanced data；SMOTE；25% under-sampling；50% under-sampling；100% over-sampling；200% over-sampling
- Benchmark 表述引文：第4.1节：'The dataset analyzed in this paper is used in the Coil 2000 data mining competition [46].' 该数据集是公开的数据挖掘竞赛数据和标准评价场地。
- Benchmark 评价：在 CoIL 2000 公开数据集上，使用官方划分的训练集和测试集评价所提 SVM 预处理方法；将 SVM-MLP、SVM-LR、SVM-RF 与相应的 standalone MLP、LR、RF 以及 SMOTE、下采样、过采样等多种平衡方法比较，报告敏感性、特异性、准确率和 AUC。Tables 4-9 与 Figs. 3-5 显示所提方法在敏感性上普遍优于对照方法，这直接支撑了核心改进主张。
- 判定理由：客观指标方面：目标变量为客户是否购买 caravan 保险，属于外部可审计事实；核心评价指标为敏感性、特异性、准确率和 AUC，均由固定真实标签计算，不依赖主观判断；全文核心目标是提出并验证 SVM 预处理方法以提高不平衡数据下分类器的客观预测性能，未发现并列的主观或理论核心贡献。Benchmark 方面：文章明确使用公开的 CoIL 2000 数据挖掘竞赛数据集作为评价场地，并在实验部分与多种 baseline、标准平衡方法进行系统比较，比较结果直接支撑核心改进主张，满足命名式 benchmark 门槛。因此两个模块均通过，strict_include 为 true。
- 置信度：0.9

### RFID-enabled shelf replenishment with backroom monitoring in retail stores 

- 年份/期刊：2012 / Decision Support Systems
- DOI：10.1016/j.dss.2011.11.018
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：总成本；服务水平
- Benchmark 状态：benchmark_comparison_central
- 参照点：periodic review (PR) policy（传统周期盘点基线）
- Benchmark 表述引文：Section 4.3 及 Fig. 6 处：'We used periodic review as the benchmark for our newly developed policies.' 并随后指出 BM 仅在较高 read rate 下优于传统政策，而 BM+1/BM+X 在约 80% read rate 起即可更优。
- Benchmark 评价：在仿真实验中将周期盘点（PR）作为基准，对本文提出的 BM、BM+1、BM+X 三种 RFID 补货政策在不同 read rate 下进行最小总成本和服务水平比较；该比较直接用于支持 RFID 策略相对传统流程的成本/服务水平提升主张。
- 判定理由：核心指标为总成本和服务水平，二者均由模拟计数和成本参数直接计算，属于完全客观的操作性指标；全文唯一核心目标是设计并评估 RFID 补货政策以提升成本效率和服务水平，不存在与客观指标提升并列的主观或理论核心贡献；同时，文中在评价语境明确以 periodic review 作为 benchmark，并使用该基准比较来支持 RFID 政策的改善主张，benchmark 表述位于结果部分且具有明确参照点。因此两个模块均通过，strict_include 为 true。
- 置信度：0.92

### Using structure-based data transformation method to improve prediction accuracies for small data sets 【全文无benchmark字样-需人工复核】

- 年份/期刊：2012 / Decision Support Systems
- DOI：10.1016/j.dss.2011.11.021
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：预测精度（平均MSE、误差改进率、STD、总误差）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：UCI Concrete Slump Test dataset (UCI repository)
- 参照点：Raw-SVR；Raw-BPNN；Raw-LR；变换后SVR/BPNN与原始数据SVR/BPNN的对照
- Benchmark 表述引文：实验部分第4.2节：“The second case is the concrete slump test, which is downloaded from the UCI repository, available at http://www.ics.uci.edu.” 本文未使用“benchmark”一词，但明确命名公开UCI数据集并将其作为评价场地，满足命名式公开benchmark数据集表述。
- Benchmark 评价：在UCI Concrete Slump数据（103条记录、7个输入、预测SLUMP）上，以5/10/15/20/25个训练样本进行20次重抽样实验，比较原始数据与结构变换后数据使用SVR/BPNN的预测误差；报告SVR误差改进率约2.12%–3.38%、BPNN误差改进率约10.65%–29.39%，并用t检验判断显著性。该结果直接支撑“提出方法提升预测精度”的核心主张。
- 判定理由：客观指标方面，核心成功指标是预测误差类数值（MSE、STD、误差改进率、总误差），目标对象是可观测物理/工艺量，不依赖人的主观评价，且是全文唯一核心目标。Benchmark方面，虽然正文未使用“benchmark”一词，但明确命名公开UCI Concrete Slump数据集并在实验部分作为评价场地，同时与Raw-SVR、Raw-BPNN、Raw-LR等明确参照点比较，benchmark结果直接支撑预测精度提升的核心主张。因此两个模块均通过，严格纳入。
- 置信度：0.72

### A demand forecast model using a combination of surrogate data analysis and optimal neural network approach 

- 年份/期刊：2013 / Decision Support Systems
- DOI：10.1016/j.dss.2012.12.008
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：均方误差 (MSE)；预测准确率 (Prediction accuracy)
- Benchmark 状态：benchmark_comparison_central
- 参照点：MSE-optimal neural network；Exponential smoothing；Multiple regression
- Benchmark 表述引文：引言Section 4：'the application of proposed technique is described and benchmarked with existing approaches through simulated models and a practical study'——该表述明确宣布在实验评价中用现有方法进行基准比较。
- Benchmark 评价：在两类模拟需求（线性季节需求和非线性Ikeda混沌需求）和一个实际需求（Ontario月度汽油需求）上，将MDL-optimal NN与MSE-optimal NN、指数平滑、多元回归四种方法同时比较，报告MSE和预测准确率（Tables 1-4）。
- 判定理由：客观指标方面：全文以MSE和预测准确率两个客观可测量的预测性能指标作为核心成功标准，不含主观满意度、专家评分等构念。唯一核心目标：研究问题、设计目标和贡献声明均围绕提升需求预测准确性展开，surrogate data方法和MDL都是服务该目标的技术组件，没有并列核心贡献。Benchmark方面：引言明确宣称将与现有方法在模拟和实际数据上benchmark；实验部分在多个数据场景中与MSE-optimal NN、指数平滑、多元回归等明确参照比较，并以比较结果直接支持MDL-optimal神经网络的核心提升主张。因此全部门槛满足，strict_include=true。
- 置信度：0.93

### A method for identifying market power 【全文无benchmark字样-需人工复核】

- 年份/期刊：2013 / Decision Support Systems
- DOI：10.1016/j.dss.2012.12.007
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：计算工作量（需检验的组合数）；市场势力识别正确性（与穷举完整搜索的一致性）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：IEEE 118-bus system (modified)
- 参照点：完整搜索（穷举N矩阵可行性条件）；Lesieutre et al.聚类算法；HHI指数；Lerner Index (LI)
- Benchmark 表述引文：第3节开头：“To test the method described above as a screening tool, a modified IEEE 118-bus system, shown in Fig. 1, is used.” 该句将领域标准算例IEEE 118节点系统作为评价场地；全文虽未出现“benchmark”单词，但按命名式标准，IEEE 118-bus system属于电力系统领域标准测试算例，构成明确benchmark表述。
- Benchmark 评价：在两个修改的IEEE 118节点系统算例中评价所提筛选方法，并与完整搜索、Lesieutre等聚类算法、HHI和Lerner指数比较。Case 1完整搜索发现{Firms 10,11,12}，所提方法识别出同一集合且只需432个组合，而完整搜索需要26289个组合；Case 2完整搜索发现Firm 12单独及包含Firm 12的二/三机组组合，所提方法以7313个组合正确识别；HHI和LI均未能正确筛选。
- 判定理由：客观指标方面：计算组合数和识别正确性均来自确定性算法与穷举对照，不依赖主观感知、语义评价或用户体验；唯一核心目标方面：全文围绕“高效且准确识别市场势力”这一客观工程目标，不存在并列的理论贡献或主观结果作为成功标准；benchmark方面：在领域标准IEEE 118节点系统上进行了系统化评价，并与完整搜索、聚类算法、HHI/LI等明确参照点比较，benchmark结果直接支撑了核心效率提升主张。因此两个模块均通过，strict_include=true。
- 置信度：0.78

### A stochastic, contingency-based security-constrained optimal power flow for the procurement of energy and distributed reserve 【全文无benchmark字样-需人工复核】

- 年份/期刊：2013 / Decision Support Systems
- DOI：10.1016/j.dss.2013.04.006
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：总供电成本（generation, reserves and load shedding total cost）；备用分配量（reserve allocation）；切负荷量（load shedding MW）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：IEEE 30-bus system；IEEE 118-bus system
- 参照点：传统固定备用裕量方法（fixed reserve allocations / fixed reserve margins）
- Benchmark 表述引文：第6节：'Numerical simulations were conducted with both 30-bus and 118-bus networks to illustrate that the endogenous determination of optimal reserves... results in a more economically efficient and reliable dispatch than the more traditional approach of using fixed reserve margins.'（作者明确使用IEEE 30-bus和118-bus标准测试系统作为评价场地，与固定备用裕量方法比较。）
- Benchmark 评价：在IEEE 30-bus（6台发电机，12个事故场景）和IEEE 118-bus（54台发电机，12个事故场景）标准测试系统上，对提出的SOPF模型进行数值仿真，与传统的固定备用裕量方法比较备用分配、切负荷量和总供电成本，结果显示SOPF可避免切负荷并降低总成本。
- 判定理由：客观指标方面：核心成功指标为总供电成本、备用分配量、切负荷量，均为可审计的物理/经济指标，不依赖人类主观评价，且客观指标提升是文章唯一的核心目标和贡献。Benchmark方面：文章在公开的IEEE 30-bus和118-bus标准测试系统上进行了数值比较，并与传统的固定备用裕量方法进行明确对比，证明SOPF在成本、备用分配和切负荷上的改进，该benchmark评价直接支撑核心改进主张。因此满足两个模块的通过条件，strict_include为true。
- 置信度：0.72

### Automated news reading: Stock price prediction based on financial news using context-capturing features 

- 年份/期刊：2013 / Decision Support Systems
- DOI：10.1016/j.dss.2013.02.006
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：分类准确率（Accuracy）；交易模拟回报（Trading returns）；R²（预测收益与实际收益的平方相关系数）
- Benchmark 状态：benchmark_comparison_central
- 参照点：多数类分类器（trivial majority classifier）：DGAP 58.2%，EuroAdhoc 53.3%；复现的文献方法：基于频率降维的特征类型（对应Schumaker等、Groth等）；不同特征选择方法：频率降维 vs. Chi² vs. BNS
- Benchmark 表述引文：引言：'To make our results comparable, we rebuild previous approaches in our evaluation to allow for benchmarking on the same data set.'；第4节：'we benchmark our approach by reproducing approaches in literature and applying them to the same data set.'
- Benchmark 评价：在DGAP和EuroAdhoc两个自有真实企业公告数据集上，对五种特征类型（字典、单词、2-Gram、2词组合、名词短语）分别采用频率降维、Chi²和BNS特征选择进行SVM训练与验证，并与复现的已有文献方法以及多数类分类器（trivial majority classifier）在相同数据上进行对比。结果显示2词组合+BNS达到最高准确率76.3%（DGAP）和65.4%（EuroAdhoc），显著优于多数类基准（58.2%和53.3%）及文献中低于60%的水平。
- 判定理由：核心指标为股票价格方向预测准确率、R²和交易回报，均基于外部市场可核验事实，完全客观，不涉及主观语义评价。文章从研究问题、设计到评价均围绕提升分类准确率展开，且无并列的主观或理论核心目标。全文明确使用benchmarking描述通过复现文献方法在相同数据上的系统比较，并以多数类分类器和复现基线作为参照，结果直接支撑准确率提升主张，因此满足全部benchmark门槛。
- 置信度：0.95

### Improving accuracy and diversity of personalized recommendation through power law adjustments of user similarities 【全文无benchmark字样-需人工复核】

- 年份/期刊：2013 / Decision Support Systems
- DOI：10.1016/j.dss.2013.03.006
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：平均秩比 (Mean Rank Ratio, MR)；召回提升 (Recall Enhancement, RE)；平均个性化 (Mean Personality, MP)；平均新颖性 (Mean Novelty, MN)
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：MovieLens；Netflix
- 参照点：UserSim；GlobalRank；random guess
- Benchmark 表述引文：第4.1节称：'We use two large-scale data sources to validate the proposed approach. The first data set is obtained from the MovieLens movie rating system ... The second data set is obtained from Netflix Prize...' 虽未使用benchmark一词，但明确命名了公开的标准推荐系统数据集，并将其作为评价场地。
- Benchmark 评价：在MovieLens和Netflix两个公开数据集上，采用90/10重复随机子抽样验证，比较PLUS与UserSim（同时涉及GlobalRank和随机猜测）在平均秩比、召回提升、平均个性化、平均新颖性上的表现；表1和表2显示PLUS相对UserSim在准确性和多样性上均有提升。
- 判定理由：客观指标与唯一核心目标通过：MR/RE/MP/MN均为可计算、可审计的客观指标，文章以提升这些指标为唯一核心目标与贡献。Benchmark门槛通过：全文将MovieLens和Netflix作为公开基准数据集置于评价中心，并报告PLUS与UserSim/GlobalRank/随机猜测的比较结果，支撑核心改进主张。因此strict_include=true。
- 置信度：0.9

### Managing online sales with posted price and open-bid auctions 

- 年份/期刊：2013 / Decision Support Systems
- DOI：10.1016/j.dss.2012.12.005
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：日均收益（average daily revenue/profit）
- Benchmark 状态：benchmark_comparison_central
- 参照点：only posted price regime（单渠道固定价格，最优价格为 $50）；only auction regime；independent design（双渠道各自优化）
- Benchmark 表述引文：引言中明确写到 “We consider the posted price channel's profit as the benchmark, rather than the profit from only auction, because this is the commonly used selling strategy by B-2-C online retailers.”（Introduction）；第 7 节 “Revenues comparison” 及其图 4-7 均以 only posted price 收益为基准比较双渠道/独立设计/仅拍卖的收益提升百分比。
- Benchmark 评价：作者在相同模拟环境中以 “only posted price regime” 为基准评价双渠道：每个模拟运行结尾记录双渠道收益，并依据到达消费者估值计算若只采用固定价格 p 时的收益；随后在 Section 7 比较最优双渠道设计与该基准，报告收益提升，并绘制 q-T 空间中的收益提升百分比图（Fig. 6-7）。
- 判定理由：客观指标方面：核心指标是日均收益，由模拟中的交易结果直接计算，完全客观，不依赖人类感知或语义判断；核心目标和贡献声明都是提升收益，且未发现并列的主观或理论目标。Benchmark 方面：作者明确将 only posted price regime 的利润作为 benchmark，全文在相同模拟环境中以该基准系统比较双渠道收益提升，结论的核心主张“最优设计下双渠道优于单渠道”正是由该 benchmark 比较支持；比较对象明确（单渠道固定价格等）。因此两个模块均通过，strict_include=true。
- 置信度：0.93

### Recommendation as link prediction in bipartite graphs: A graph kernel-based machine learning approach 

- 年份/期刊：2013 / Decision Support Systems
- DOI：10.1016/j.dss.2012.09.019
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：Precision@10；Recall@10；F-measure；Rank score；ROC曲线 (top 1000 recommendations)
- Benchmark 状态：benchmark_comparison_central
- 参照点：User-based；Item-based；Item popularity；Spreading activation；Link analysis；Matrix factorization；Binary matrix factorization
- Benchmark 表述引文：摘要中明确写道：'Our proposed method outperforms state-of-the-art benchmark algorithms, particularly when recommending a large number of items.'；实验部分4.3：'In the evaluation, we compare our proposed approach with state-of-the-art benchmark algorithms and the kernel-based machine learning algorithms that do not effectively use graph information.'
- Benchmark 评价：在三个真实世界数据集（图书零售、服装零售、图书评分）上，将提出的图核方法与七个基准算法（user-based、item-based、item popularity、spreading activation、link analysis、matrix factorization、binary matrix factorization）比较，报告precision、recall、F-measure、rank score和ROC曲线。结果显示图核方法在较大推荐数量上显著优于所有基准方法。
- 判定理由：客观指标：推荐性能（precision、recall、F-measure、rank score、ROC）完全基于未来实际交易事实，不依赖主观评价；唯一核心目标：全文围绕提升推荐性能展开，核有效性和复杂度证明只是方法支撑，无并列核心贡献；benchmark：作者明确使用'state-of-the-art benchmark algorithms'表述系统化基准比较，评价位于实验和结论部分，并与七个基准算法及两个核基线明确比较，结果直接支撑性能提升的核心主张。因此两个模块均通过，strict_include=true。
- 置信度：0.9

### Reliable Web service selection in choreographed environments 

- 年份/期刊：2013 / Decision Support Systems
- DOI：10.1016/j.dss.2012.12.017
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：成功率（success rate）
- Benchmark 状态：benchmark_comparison_central
- 参照点：centralized method；view-based propagation-free method；view-based reliability-free method；random method
- Benchmark 表述引文：Section 5 Performance evaluation: 'In addition, we evaluate four other methods as benchmarks: centralized, view-based propagation-free, view-based reliability-free, and random methods.'
- Benchmark 评价：在购物场景及其nontransitive修订场景中，比较view-based方法与centralized、view-based propagation-free、view-based reliability-free、random四种方法的成功率；结果显示view-based接近centralized且优于其他分布式方法。
- 判定理由：文章的核心目标是在choreographed环境中最大化整个流程的成功完成概率，评价指标为成功率，是客观可观测的技术结果，且为唯一核心成功标准。实验部分明确将四种既有方法称为benchmarks，并在购物场景和nontransitive场景中比较成功率，证明view-based方法优于三种分布式方法并接近centralized方法，满足benchmark评价支撑核心改进主张和显式比较对象的要求。因此同时通过客观指标和benchmark门槛。
- 置信度：0.96

### Simple decision forests for multi-relational classification 

- 年份/期刊：2013 / Decision Support Systems
- DOI：10.1016/j.dss.2012.11.017
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：分类准确率 (Accuracy)；AUC；加权F值 (Weighted F-measure)；学习/诱导时间 (Run time)
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：Financial (PKDD CUP 1999)；Hepatitis (PKDD'02 Discovery Challenge)；Mondial；MovieLens (UCI)；JMDB (IMDB)
- 参照点：TILDE；FORF-NA；Graph-NB；TreeLiker-Relf；TreeLiker-Poly；Naive Decision Forest；Unnormalized Decision Forest
- Benchmark 表述引文：Section 1.4: 'The final section evaluates the classification performance of the different models on five benchmark datasets.'；Section 7.1: 'We use five benchmark real-world datasets.'
- Benchmark 评价：在Financial、Hepatitis、Mondial、MovieLens、JMDB五个基准数据集上评价简单决策森林（Normalized/Unnormalized/Naive）以及TILDE、FORF-NA、Graph-NB、TreeLiker-Relf/Poly等参照方法，报告Accuracy、AUC、F-measure和诱导时间。
- 判定理由：全文以提升多关系分类的客观预测性能（Accuracy/AUC/F-measure）和学习时间为唯一核心目标；明确使用5个命名基准数据集，并在该评价场地上与TILDE、FORF-NA、Graph-NB、TreeLiker等多个参照方法比较，结果支持核心提升主张，因此严格纳入。
- 置信度：0.95

### Trading team composition for the intraday multistock market 

- 年份/期刊：2013 / Decision Support Systems
- DOI：10.1016/j.dss.2012.09.009
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：日均利润/年化利润；风险指标（最大回撤、Ulcer Index）；收益风险比率（Sharpe、Martin、Calmar、Sterling、Burke）；交易执行指标（盈利交易、亏损交易、交易次数、盈亏比）
- Benchmark 状态：benchmark_comparison_central
- 参照点：BLS baseline strategy（固定股票-时间分辨率的单股票多时段策略）
- Benchmark 表述引文：Section 5："This characteristic makes BLS well suited as an informative benchmark for MSR."；Section 6.2 标题为 "Benchmark Results"，其中对比 BLS 与 MSR 的利润、风险、收益风险比和交易指标。
- Benchmark 评价：在十二只BM&FBovespa股票的测试数据集上，将提出的MSR策略与基线策略BLS进行系统比较，报告日均利润、年化利润、最大回撤、Ulcer Index、Sharpe/Martin/Calmar/Sterling/Burke比率以及交易统计，并展示统计显著性检验。
- 判定理由：该文章以提升完全客观的交易绩效指标（利润、风险、收益风险比）为唯一核心目标与贡献；全文有明确的benchmark表述（BLS作为informative benchmark，Benchmark Results一节），并在该基准上与明确基线比较，支撑核心利润提升主张。因此两个模块均通过，strict_include为true。
- 置信度：0.95

### User community discovery from multi-relational networks 

- 年份/期刊：2013 / Decision Support Systems
- DOI：10.1016/j.dss.2012.09.012
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：综合均值 μ；社区用户散度 D_U、社区主题散度 D_T 及复合散度 D
- Benchmark 状态：benchmark_comparison_central
- 参照点：NMF；AT；MetaFac
- Benchmark 表述引文：Section 5 开头：'pure NMF and AT methods were used as the benchmark methods to compare against our NMF-AT algorithm. The MetaFac [29] model was also selected as benchmark...'
- Benchmark 评价：在 Delicious 和 Twitter 两个真实数据集上，将 NMF-AT 与 NMF、AT、MetaFac 三个基准方法比较；主要报告综合均值 μ、社区用户散度、社区主题散度和复合散度。结果显示 NMF-AT 在综合均值上优于对比方法，Delicious 上成对 t-test p<0.001，Twitter 上在整体区间内更优，并在复合散度 D 上取得最高值。
- 判定理由：客观指标：核心成功指标是软模块度、内容相似性和社区散度，均由数据和确定性公式计算，不依赖主观人工评价。唯一核心目标：研究问题、算法设计和贡献声明均围绕通过融合好友网络与用户内容来提升社区发现的客观质量，未发现并列的理论、政策或主观体验核心贡献。Benchmark：实验部分明确将 NMF、AT、MetaFac 作为 benchmark 方法进行系统比较，结果直接支持 NMF-AT 的客观指标改善，且具有明确参照对象。因此 strict_include=true。
- 置信度：0.85

### A data-driven approach to predict the success of bank telemarketing 【全文无benchmark字样-需人工复核】

- 年份/期刊：2014 / Decision Support Systems
- DOI：10.1016/j.dss.2014.03.001
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：AUC（ROC曲线下面积）；ALIFT（LIFT累积曲线下面积）
- Benchmark 状态：benchmark_comparison_central
- 参照点：LR（逻辑回归）；DT（决策树）；SVM（支持向量机）；随机基线ALIFT=0.5/AUC=0.5；当前银行不筛选客户的基线（LIFT约50%）
- Benchmark 表述引文：摘要与结论中多次以“benchmark”指代基准比较：如摘要“We also compared four DM models: logistic regression, decision trees (DTs), neural network (NN) and support vector machine”；第3.1节“For comparative purposes, we also tested LR, DT and SVM”；第3.2节以“For comparison purposes”在滚动窗口评价中与LR、DT、SVM比较；结论“four DM models were compared... using two metrics...”。这些属于明确的基准比较表述，位于实验/评价语境。
- Benchmark 评价：文章在银行电话营销成功预测任务上，以LR、DT、SVM作为明确参照方法，对提出的NN模型进行系统化比较评价。建模阶段（留出验证集）：NN的AUC=0.929、ALIFT=0.878，优于LR（0.900/0.849）、DT（0.833/0.756）、SVM（0.891/0.844），统计显著；滚动窗口阶段（测试集）：NN的AUC=0.794、ALIFT=0.672，优于LR（0.715/0.626）、DT（0.757/0.651）、SVM（0.767/0.656）。比较结果直接支撑“NN模型最佳并可用于银行电话营销”的核心主张。
- 判定理由：客观指标方面：核心目标为预测银行电话营销中客户是否实际订阅长期存款这一客观事实标签，核心评价指标AUC和ALIFT均由事实标签和预测概率计算，不依赖人的感受、语义或价值判断；研究问题、设计目标、评价和贡献声明均围绕该客观分类性能提升展开，无其他并列核心贡献，因此判定为完全客观且唯一核心目标。Benchmark方面：全文虽未命名公开基准数据集，但在实验/评价语境中明确以“compare/for comparison purposes”等基准化陈述将提出的NN与LR、DT、SVM和随机基线进行系统比较，两种评价阶段均报告NN在AUC和ALIFT上的相对提升，该基准比较直接支撑核心预测性能主张；符合benchmark_comparison_central。因此两个模块均通过，strict_include=true。
- 置信度：0.93

### A decision support system for post-disaster interim housing 

- 年份/期刊：2014 / Decision Support Systems
- DOI：10.1016/j.dss.2014.06.012
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：总加权距离（英里）；不可行分配数
- Benchmark 状态：benchmark_comparison_central
- 参照点：基准整数规划模型的最优解（CPLEX求解）
- Benchmark 表述引文：摘要中的“We develop a benchmark integer programming model for developing a balanced housing plan, and then use the model to evaluate three heuristics”；第3节中的“the value of the model for our situation is to serve as a benchmark to evaluate heuristics which are used in our housing recommender system.”
- Benchmark 评价：作者构建一个整数规划基准模型（用CPLEX求解），在假想的500个家庭、10个住房备选场景中求得“更大利益”最优分配；随后用三种贪心启发式（GS、GL、GH）在三种住房富余水平、100种家庭顺序、10次重复（共1000次运行）下运行，报告相对于基准模型最优解的加权距离平均百分比偏差和不可行分配数。Table 1 是该基准比较的核心结果，用于选择GH作为DSS的推荐方法。
- 判定理由：客观指标方面：核心结果为总加权距离和不可行分配数，均为可直接观测、用算法计算的外部事实，不涉及主观感受或语义评价；唯一核心目标是提高灾后住房分配的客观质量。benchmark方面：作者明确以“benchmark integer programming model”作为评价基准，并在第4.4节用该基准模型的CPLEX最优解来比较三种启发式的距离偏差和不可行数，比较有明确参照点，且该比较支撑了选择GH和DSS设计的核心主张。因此两个模块均通过。
- 置信度：0.78

### A decision support system for stock investment recommendations using collective wisdom 

- 年份/期刊：2014 / Decision Support Systems
- DOI：10.1016/j.dss.2013.10.005
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：投资组合绝对回报；Sharpe Ratio（Reward-to-Variability-Ratio）
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：DAX German market index
- 参照点：DAX German market index buy-and-hold；DWS Deutschland (Fund 1)；Allianz Thesaurus AT EUR (Fund 2)
- Benchmark 表述引文：摘要：'the portfolios recommended by the system clearly outperform the market benchmark and comparable public funds'；4.3.2：'the system outperforms a DAX index buy-and-hold strategy to a large extent'；4.4：'Such funds provide another benchmark for the performance of the two test runs ... they can serve as a state-of-the-art benchmark for our DSS'。
- Benchmark 评价：在2009年1月至2010年12月观察期内，原型系统通过两个测试场景（Test 1：每日投资最佳评级ISIN；Test 2：对crowd Top10使用Markowitz组合优化并月度调仓）与DAX指数买入持有策略和两只公募基金进行比较。结果显示Test 1期末收益率123.2%（扣除交易成本88.5%），Test 2期末收益率110.6%（扣除交易成本99.8%），均大幅高于DAX基准的40.6%；Sharpe Ratio分别为0.0648和0.0791，高于DAX的0.0581以及两只公募基金的0.0604和0.0476。
- 判定理由：客观指标方面，核心成功指标是投资组合绝对回报和Sharpe Ratio，均由市场价格和交易成本计算，不依赖主观感受或语义判断；该指标提升是全文唯一核心目标和核心贡献。Benchmark方面，摘要在评价语境中明确使用'outperform the market benchmark and comparable public funds'，评价部分将DAX指数和两只公募基金作为基准并与系统两个测试组合的绝对收益和Sharpe Ratio比较，benchmark结果直接支撑核心绩效提升主张，且具有明确比较对象。因此两个模块均通过，strict_include=true。
- 置信度：0.96

### A hybrid heuristic approach for attribute-oriented mining 【全文无benchmark字样-需人工复核】

- 年份/期刊：2014 / Decision Support Systems
- DOI：10.1016/j.dss.2013.08.012
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：广义表有趣性：KL散度与簇质量CQ/I_g^T；运行时间；NOT-ANY/ANY 规则比例
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：Cancer Wisconsin dataset (UCI Breast Cancer Wisconsin)；Census-income dataset1 (50K tuples)；Census-income dataset2 (200K tuples)
- 参照点：AOI算法；不同全局阈值G.Thr=1到10；AOI的ANY/NOT-ANY输出比例
- Benchmark 表述引文：第6节原文：“Experiments have been performed on three datasets: two Census income datasets and Cancer Wisconsin [19]”，并列出这些数据的UCI来源；全文虽未出现“benchmark”一词，但明确以UCI公开数据集作为评价场地，属于命名式公开benchmark表述。
- Benchmark 评价：在Cancer Wisconsin（0.7K）、Census-income 1（50K）和Census-income 2（200K）上，以全局阈值G.Thr=1到10运行clusterAOI和AOI，报告KL、I_g^T、运行时间和ANY/NOT-ANY比例。结果显示clusterAOI在多个阈值下KL更高、CQ/I_g^T更高、运行时间更短、NOT-ANY比例更高（如G.Thr=3时clusterAOI平均100% NOT-ANY，而AOI为41%）。
- 判定理由：客观指标：KL散度、簇质量I_g^T、运行时间和NOT-ANY比例均是确定性可观测指标，没有主观量表或人类语义评判。唯一核心目标：研究问题、算法设计和实验均围绕比AOI生成更有趣、更少过度泛化的广义表这一客观改进目标展开，没有并列的理论/制度/主观体验核心贡献。Benchmark：在UCI公开数据集（Cancer Wisconsin、Census-income 1/2）上以AOI为baseline、用多个阈值比较KL、I_g^T和runtime，构成命名式公开benchmark评价并直接支撑核心改进主张。因此strict_include=true。
- 置信度：0.78

### A randomized pricing decision support system in electronic commerce 

- 年份/期刊：2014 / Decision Support Systems
- DOI：10.1016/j.dss.2013.01.015
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：零售商期望利润
- Benchmark 状态：benchmark_comparison_central
- 参照点：固定价格策略（flat price strategy）
- Benchmark 表述引文：Section 3 Promotional model with price uncertainty: 'We first consider a flat price strategy as a benchmark and then a randomized pricing strategy, that is, the promotion strategy, and show how randomized pricing improves the retailer's profit.'
- Benchmark 评价：文章以固定价格策略（flat price strategy）作为基准，在其下计算最优利润Π0=1/4；然后在随机定价策略下推导最优利润Π1，并通过命题1证明Π1 ≥ Π0，即随机定价策略总能提高利润。该基准比较直接支撑核心改进主张。
- 判定理由：客观指标方面，文章核心目标是提升零售商利润，利润是客观可审计的经济指标，不存在任何主观构念或并列的核心贡献。benchmark方面，文章在模型部分明确将固定价格策略称为benchmark，并以其作为参照点，通过数学证明和数值分析展示随机定价策略在利润指标上的提升，该benchmark评价是核心改进主张的关键证据。因此，两个模块均通过，strict_include为true。
- 置信度：0.95

### Coalition formation based on marginal contributions and the Markov process 

- 年份/期刊：2014 / Decision Support Systems
- DOI：10.1016/j.dss.2013.09.019
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：代理人支付/Shapley值；搜索空间规模/剪枝率；运行时间
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：IDP；IP-Uniform；IP-Normal
- 参照点：IDP (Improved Dynamic Programming)；IP-Uniform；IP-Normal
- Benchmark 表述引文：引言贡献点：“the proposed method is illustrated by a real world example and is experimentally evaluated by comparing it with three benchmark methods, which shows the efficiency and effectiveness of our method (Sections 5, 6).”
- Benchmark 评价：在第6节模拟实验中，以零售商联盟情景为测试环境，将提出的算法（Algorithms 1-3）与三个基准方法IDP、IP-Uniform、IP-Normal比较运行时间；Fig. 4显示在n>22时本文方法更高效，n=25时耗时仅为IP-Uniform的32.76%。Table 3同时报告搜索空间剪枝效果，Fig. 5报告支付提升。
- 判定理由：完全客观指标：核心成功指标包括支付/Shapley值、搜索空间剪枝率、运行时间，均为确定性可测量技术或博弈论数量；唯一核心目标是提出并验证提升这些客观指标的高效联盟形成方法；无主观满意度、质量评分或混合主观核心结果。Benchmark：全文在引言明确称“与三个benchmark方法比较实验评价”，且第6节实际将所提方法与IDP、IP-Uniform、IP-Normal比较运行时间，构成明确的基准比较；该比较直接支撑效率改进这一核心主张，并有明确参照点。因此同时满足两个模块。
- 置信度：0.78

### Empirical evaluation of an automated intraday stock recommendation system incorporating both market data and textual news 

- 年份/期刊：2014 / Decision Support Systems
- DOI：10.1016/j.dss.2013.09.013
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：投资回报率（Returns）；夏普比率（Sharpe ratio）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：S&P 500 index benchmark / S&P 500 SPY index benchmark
- 参照点：S&P 500 index benchmark (SPY)；Market-only数据表示作为增量比较基线
- Benchmark 表述引文：Section 6 Results and discussion: 'compare these results against the corresponding performance of the S&P500 index benchmark'；以及 'our model outperforms the well-known S&P 500 SPY index benchmark'。
- Benchmark 评价：在结果部分，将NN算法在market data基础上的不同文本数据表示（news count、categories、sentiment、calibrated sentiment）上得到的Returns和Sharpe ratio，与S&P500指数基准对比。结果显示，采用NN算法并加入更高级文本表示后，模型收益和Sharpe ratio超过S&P500基准，且文本表示越高级差距越大；最佳配置达到统计显著正收益。
- 判定理由：客观指标方面：核心成功指标是投资回报率和夏普比率，由真实市场报价、交易成本与固定模拟规则确定，完全客观且不依赖主观评价；核心目标是评估/改进日內股票推荐系统的客观交易表现，技术贡献均服务于该目标。Benchmark方面：文章在结果部分明确使用S&P500指数作为benchmark，将NN模型在不同文本数据表示下的收益和Sharpe比率与该基准比较，并以该比较支撑‘高级文本表示显著提升股票购买决策’的核心主张；有明确参照点（S&P500指数基准和市场数据only基线）。因此两个模块均通过，strict_include=true。
- 置信度：0.87

### Improving learning accuracy by using synthetic samples for small datasets with non-linear attribute dependency 【全文无benchmark字样-需人工复核】

- 年份/期刊：2014 / Decision Support Systems
- DOI：10.1016/j.dss.2013.12.007
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：MAPE 平均绝对百分比误差；RMSE 均方根误差
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：UCI Machine Learning Repository – Concrete Compressive Strength Data Set (CCS)；UCI Machine Learning Repository – Istanbul Stock Exchange Data Set (ISE)；UCI Machine Learning Repository – Yacht Hydrodynamics Data Set (YH)
- 参照点：MTD (mega-trend-diffusion)；MRA (multi regression analysis)；BPN 仅使用原始数据的基线
- Benchmark 表述引文：Section 4.1：'In order to demonstrate the effectiveness of the proposed method, we use one practical process dataset ... and three real datasets, downloaded from the UCI Machine Learning Repository database [1], namely the Concrete Compressive Strength Data Set (CCS), the Istanbul Stock Exchange Data Set (ISE), and the Yacht Hydrodynamics Data Set (YH), to implement the small dataset analysis.'
- Benchmark 评价：在 UCI 的 CCS、ISE、YH 三个公开标准数据集上，以不同训练样本数 NT∈{20,40,60,80,100,125,150} 和虚拟样本数 NV∈{50,100} 进行小数据集实验；用 BPN 预测，并比较 PM、MTD、MRA 三种方法；结果表显示 PM 的 MAPE、RMSE 在多数设置中更低，t 检验给出大量显著差异（Tables 8–10）。
- 判定理由：该文以提升小数据集预测精度为唯一核心目标，核心指标 MAPE/RMSE 完全客观，不依赖主观评价。实验在 UCI 公开标准数据集 CCS/ISE/YH 上进行，具有明确命名的 benchmark 数据集，并与 MTD、MRA、原始 BPN 等明确参照点比较；benchmark 评价直接支撑其核心提升主张。因此两个模块均通过，strict_include=true。
- 置信度：0.92

### Intelligent trading of seasonal effects: A decision support algorithm based on reinforcement learning 

- 年份/期刊：2014 / Decision Support Systems
- DOI：10.1016/j.dss.2014.04.011
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：累计收益 / 年化收益；最大回撤
- Benchmark 状态：benchmark_comparison_central
- 参照点：static unfiltered seasonality strategy；buy-and-hold (b&h)
- Benchmark 表述引文：Results and Discussion部分：'The benchmark is a static strategy (static) that buys one day before an event at the close price and sells two days later at close price.' 另外，2.1节也使用平均每日交易收益作为事件交易的benchmark进行t检验。
- Benchmark 评价：在DAX（243个交易事件）和S&P 500（314个交易事件）的2000-2012真实行情上，以未过滤的季节性静态策略作为benchmark，同时给出buy-and-hold作为参照；比较RL过滤后best/average/worst情形的return、annualized return和max drawdown。表6显示DAX平均收益从106.64%提升到173.14%，最大回撤从22.35%降至14.32%；表7显示S&P 500最佳收益从63.11%提升到133.99%，最大回撤下降。该benchmark评价直接支撑RL过滤提升收益/风险比的核心主张。
- 判定理由：全文核心目标是提升完全客观的交易绩效指标（收益、年化收益、最大回撤），不存在主观构念或并列核心目标；结果部分明确使用'benchmark'一词，以未过滤的静态季节性策略为基准，并对比buy-and-hold和RL各情形，benchmark结果直接支撑核心提升主张。因此strict_include=true。
- 置信度：0.95

### Listen to me — Evaluating the influence of micro-blogs 

- 年份/期刊：2014 / Decision Support Systems
- DOI：10.1016/j.dss.2014.03.008
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：信息传播有效性（接收消息节点比例）
- Benchmark 状态：benchmark_comparison_central
- 参照点：Kiss and Bichler [26]
- Benchmark 表述引文：图7标题：'Comparison between this study and benchmarked approach in Kiss and Bichler [26].'（位置：Section 4 结果部分）
- Benchmark 评价：作者在从Twitter收集的'appleincnews'社区数据上，将所提框架与Kiss and Bichler [26]的方法进行系统对比，以信息传播覆盖率（接收消息节点比例）为核心评价指标。Tables 5-8展示了多种参数组合下所提方法相对基准方法的改进幅度（如23.94%至62.83%），该对比直接支撑核心提升主张。
- 判定理由：客观指标方面：核心成功指标为信息传播有效性（接收消息节点比例），完全由网络模拟客观计算，不依赖主观评价；该指标提升是唯一核心目标，研究问题、评价结构和贡献声明均围绕其展开。Benchmark方面：全文在图7标题明确使用'benchmarked approach'，并在Tables 5-8中与Kiss and Bichler [26]基准方法进行系统比较，所有比较均以传播覆盖率提升为核心证据，存在明确参照点。因此两个条件均满足，strict_include为true。
- 置信度：0.82

### Modeling brand post popularity dynamics in online social networks 

- 年份/期刊：2014 / Decision Support Systems
- DOI：10.1016/j.dss.2014.05.003
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：模型拟合优度（AIC值）；品牌帖子受欢迎程度（事件计数）
- Benchmark 状态：benchmark_comparison_central
- 参照点：homogeneous Poisson process (explicitly called benchmark)；ARIMA time series model (explicitly called benchmark)；self-exciting Hawkes process (candidate Model #1)
- Benchmark 表述引文：第3.3节：'Furthermore, we employ autoregressive integrated moving average (ARIMA) models as benchmarks which have been regarded as the closest framework to point processes for event data.'；第4节：'We next estimate the self-exciting Hawkes process model, ETAS model, the benchmark Poisson process model and the benchmark ARIMA model and compare their goodness-of-fit by computing their average AIC values across all datasets.'
- Benchmark 评价：在自收集的Twitter品牌帖子数据集（221个高互动帖子，125,861条活动）上，以 homogeneous Poisson process 和 ARIMA time series model 作为显式命名的 benchmark 模型，与 self-exciting Hawkes 和 ETAS 候选模型比较平均AIC；结果显示ETAS模型平均AIC最低（6415.187 vs 7143.110 vs 9047.397 vs 13398.661），用于支持ETAS优于基准模型的核心主张。
- 判定理由：客观指标方面：核心成功指标为模型拟合优度（AIC），基于Twitter活动事件日志，完全客观且不依赖人的语义判断；受欢迎程度被操作化为可观测事件计数；全文无主观量表，核心目标是提出并验证AIC更优的二维点过程模型。Benchmark方面：作者在方法/结果部分明确将 homogeneous Poisson process 和 ARIMA 命名为 benchmark 模型，并在自建数据集上通过AIC比较支持核心主张；有明确参照点。因此满足两个条件，strict_include=true。
- 置信度：0.75

### Object typicality for effective Web of Things recommendations 

- 年份/期刊：2014 / Decision Support Systems
- DOI：10.1016/j.dss.2013.09.008
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：平均绝对误差（MAE）；均方根误差（RMSE）；大误差预测分布（PE distribution）；推荐时间（计算效率）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：MovieLens；Netflix
- 参照点：CB；UBCF；IBCF；Naive Hybrid；EMDP；SCBPCC；WLR；CBT；SVD；SVD++；SocialMF
- Benchmark 表述引文：摘要：'Based on the MovieLens benchmark data set, our experimental results show that the proposed recommendation method is effective...'；'Based on the Netflix benchmark data set that simulates a large WoT recommendation space, the proposed method also significantly outperforms state-of-the-art recommendation methods in terms of Mean Absolute Error (MAE).'；第4.1节：'Since a benchmark data set specifically constructed for the evaluation of WoT recommender systems is not available, we applied the common MovieLens and Netflix data sets to evaluate the effectiveness of the proposed ROT prototype system.'；第4.3.6节：'we compare the performance of the proposed ROT system with quite a number of state-of-the-art recommender systems based on two different benchmark data sets.'
- Benchmark 评价：在 MovieLens（100,000 ratings, 943 users, 1682 movies，实验中用其子集）和 Netflix（100,480,507 ratings 子集）两个公开基准数据集上评价 ROT。第一组实验与 CB、UBCF、IBCF、Naive Hybrid、EMDP 等经典基线比较 MAE/RMSE、大误差比例和推荐时间；第二组实验与 SCBPCC、WLR、CBT、SVD、SVD++、SocialMF 等 state-of-the-art 方法比较 MAE/RMSE。结果表明 ROT 在 MovieLens 和 Netflix 上显著优于多数基线，尤其在 MAE 上。
- 判定理由：文章核心目标是设计和评估 ROT 推荐方法，以提升推荐准确度、降低大误差并提高计算效率；所有主要成功指标均为可审计的客观数值：MAE、RMSE、大误差分布和推荐耗时。研究问题、实验设计和结论均围绕这些客观指标展开，未将主观满意度、用户感知质量或理论机制贡献作为并列核心目标。全文在摘要、评价数据选择、实验讨论和结论中多次明确采用 MovieLens 和 Netflix 公共 benchmark 数据集，并在这些数据集上与多项基线和 state-of-the-art 方法比较，benchmark 结果是支持核心性能提升主张的关键证据。因此同时满足客观指标唯一核心目标和明确 benchmark 表述的门槛，strict_include 为 true。
- 置信度：0.95

### Ontology based integration of XBRL filings for financial decision making 

- 年份/期刊：2014 / Decision Support Systems
- DOI：10.1016/j.dss.2014.09.004
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：财务类别取值准确率；财务比率准确率与 RMSE
- Benchmark 状态：benchmark_comparison_central
- 参照点：SEC EDGAR 10-K 年报中人工提取的财务数值及由此计算的比率；Thomson Reuters Data Stream (TRDS) 提供的财务数值/比率；训练集（FY2011 25 家）用于开发，测试集（FY2011 43 家、FY2012 68 家）用于验证泛化
- Benchmark 表述引文：Evaluation 部分：'RMSE corresponds to the average spread of the calculated values or ratios around the benchmarked values or ratios.'；'Evaluation performance for OFXD with respect to financial ratios benchmarked against TRDS was markedly lower than OFXD performance benchmarked against EDGAR.'
- Benchmark 评价：OFXD 在 FY2011（43 家测试公司）和 FY2012（68 家）的 XBRL 10-K 申报上，以 EDGAR 人工提取值和 Thomson Reuters Data Stream 作为基准，评估 7 个财务类别和 6 个财务比率的准确率与 RMSE；结果是训练集 100%，测试集财务类别准确率约 79%–100%，比率准确率约 76%–98%，并与基准数据源存在明确的数值偏差报告。
- 判定理由：客观指标层面：OFXD 的核心成功标准是财务数据项及比率相对 EDGAR/TRDS 的准确率和 RMSE，全部来自可审计的财务事实和确定性公式，不包含满意度、感知或语义质量评价；评价结构、设计目标和贡献声明均围绕该客观性能展开，且无并列的主观/理论核心目标。Benchmark 层面：作者在 Evaluation 部分明确使用 benchmarked values / benchmarked against 描述与 EDGAR、TRDS 的系统化基准对照，benchmark 结果直接支撑 OFXD 解决语义异构、提高财务数据互操作性的核心主张，并有明确参照点。因此两个模块均通过，strict_include=true。
- 置信度：0.72

### Recommender systems based on quantitative implicit customer feedback 【全文无benchmark字样-需人工复核】

- 年份/期刊：2014 / Decision Support Systems
- DOI：10.1016/j.dss.2014.09.005
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：平均绝对误差（MAE）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：Echo Nest Taste Profile Subset（随机样本）；Ta-Feng data set；E-Commerce data set（企业私有数据）
- 参照点：基于正态分布假设的state-of-the-art矩阵分解（baseline）；用户均值预测；物品均值预测；不同分布假设之间的相互比较（Poisson/inverse Gaussian/gamma）
- Benchmark 表述引文：第5节写道："For the experimental evaluation of the proposed method, we make use of three different data sets. The first one is a random sample of the commonly available 'Echo Nest Taste Profile Subset'... The second data set is the publicly available Ta-Feng data set..."；这些命名公开数据集被用作评价场地，属于明确的基准评价表述。
- Benchmark 评价：在Taste Profile Sample、Ta-Feng和E-Commerce三个真实数据集上，分别用MAE评价基于正态分布、Poisson、inverse Gaussian、gamma分布的矩阵分解方法，并对比用户均值与物品均值预测；Table 2和图7-9表明三种分布扩展均优于正态分布MF基线，且不同数据集上最优分布不同。
- 判定理由：客观指标方面，文章以MAE为核心结果指标，数据来自客观的购买次数/播放次数，不涉及主观评价；核心目标与贡献是提升隐式反馈计数数据的预测精度，没有并列的主观或理论核心目标。Benchmark方面，文章在多个命名公开真实数据集上开展系统化比较实验，以正态分布MF、用户/物品均值等为明确参照，MAE结果表明所提分布扩展带来一致提升，该benchmark评价直接支撑核心改进主张。因此满足两个模块的全部门槛。
- 置信度：0.88

### A bi-level decision support system for uncertain network design with equilibrium flow 

- 年份/期刊：2015 / Decision Support Systems
- DOI：10.1016/j.dss.2014.12.004
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：性能指标 PM（总行程时间成本 + 容量扩展投资成本，以美元计）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：Sioux Falls city network（真实数据基准路网）
- 参照点：确定性名义条件下的解（deterministic solutions at nominal condition）；四组初始容量扩展设置及对应初始 PM 值；上界估计与下界估计（upper/lower bound estimates）
- Benchmark 表述引文：第4节开头：“numerical computations were performed using a real-data benchmark problem of Sioux Falls city network as shown in Fig. 1.”；引言贡献部分亦写“numerical computations are performed using a benchmark real-data road network with various initial data.”
- Benchmark 评价：在 Sioux Falls 标准基准路网上，用四组初始容量扩展和需求增长系数运行所提 BDSS 求解方案；报告 PM 改善率（9.76%–19.32%）、上/下界 gap 收敛至零的过程，以及与确定性名义解相比的不可行性增益 r+（29.62%–37.57%）和最优性损失 r−（2.11%–2.88%）。
- 判定理由：核心指标 PM 是完全客观可计算的总行程时间与投资成本；全文研究问题、模型、评价和结论均围绕该客观指标的改进展开，没有主观量表或并列的核心贡献。全文明确使用 Sioux Falls 真实数据基准路网，并在该 benchmark 上评价所提方案，与确定性名义解、初始设置和上下界估计进行明确比较，benchmark 结果直接支持核心改进主张。因此两个模块均通过。
- 置信度：0.9

### A collaborative filtering approach for recommending OLAP sessions 

- 年份/期刊：2015 / Decision Support Systems
- DOI：10.1016/j.dss.2014.11.003
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：精确率 (Precision)；召回率 (Recall)；F值 (F-measure)；覆盖率 (Coverage)；预见度 (Foresight)；新颖度 (Novelty)；执行时间 (Execution time)
- Benchmark 状态：benchmark_comparison_central
- 参照点：与Giacometti et al. [6]方法比较；不同参数配置（最小相关性阈值、日志密度、会话长度、最小预见度）之间的对比
- Benchmark 表述引文：5.2节：“The benchmark we adopted for our tests is based on a set of synthetic logs over the CENSUS schema.”——明确将测试基准定义为基于CENSUS模式的合成日志。
- Benchmark 评价：在该合成日志基准上，对推荐系统进行了多组有效性测试（精度、召回、F值、覆盖率、预见度、新颖度）和效率测试（执行时间），并与方法[6]在同一日志规模（200 sessions）下对比，结果显示精度0.94对0.52、召回0.87对0.52。
- 判定理由：客观指标方面：核心成功指标是完全客观的推荐质量度量（精确率、召回率、F值、覆盖率、预见度、新颖度）和效率度量（执行时间），均由定义明确的公式或物理时间计算，不依赖人类感受或语义评价；核心目标唯一地是提升这些客观指标。Benchmark方面：实验部分明确使用“benchmark”一词定义了基于CENSUS合成日志的测试基准，并在该基准上进行了系统化的有效性/效率评价，且与已有方法[6]进行明确比较，benchmark结果直接支撑核心提升主张。因此严格纳入。
- 置信度：0.93

### A multivariate approach for top-down project control using earned value management 

- 年份/期刊：2015 / Decision Support Systems
- DOI：10.1016/j.dss.2015.08.002
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：AUC（由检测性能与过度反应概率整合的曲线下面积）；检测性能 (detection performance)；过度反应概率 (probability of overreaction)
- Benchmark 状态：benchmark_comparison_central
- 参照点：univariate X-chart and R-chart EVM/ES procedures from Colin & Vanhoucke (2014) [26]；不同主成分保留数量 k 下的 T2 与 SPE 自身比较
- Benchmark 表述引文：Section 5 开头：'Section 5.1 introduces the data generation process to create a project benchmark set.'；引言纲要：'Section 6 provides results of the computational experiment and benchmarks the performance of this paper's method to the univariate methods of [26].'
- Benchmark 评价：作者自建了一个由 RanGen 生成的 900 个 30 活动项目组成的 benchmark set，用 Monte Carlo 模拟生成 EVM/ES 数据；在第一阶段建立受控参考，第二阶段评估 T2/SPE 控制图的检出性能与过度反应概率并计算 AUC；结果与 Colin & Vanhoucke (2014) 的单变量 X、R 控制图进行比较（Fig. 4-7），显示多变量方法在各类场景下 AUC 更高。
- 判定理由：该文的唯一核心目标是提出并验证基于 PCA 的多元 EVM/ES 项目进度控制指标 T2/SPE，核心成功指标是模拟项目基准集上的检测性能/过度反应概率合成的 AUC，属于客观可计算的操作性分类性能指标；全文没有将主观量表作为核心成功标准，也没有并列理论或治理贡献。Benchmark 方面，作者在实验设计部分明确构建了 project benchmark set，并在第6节把方法与 Colin & Vanhoucke (2014) 的单变量 X/R 方法进行比较，benchmark 结果直接支持核心改进主张。因此两模块均通过。
- 置信度：0.92

### A recommendation system for predicting risks across multiple business process instances 

- 年份/期刊：2015 / Decision Support Systems
- DOI：10.1016/j.dss.2014.10.006
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：故障实例百分比（% faulty instances）；平均和中位故障严重性（mean and median fault severity）
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：保险公司一年完成的索赔处理流程事件日志（1065条trace，未公开命名）
- 参照点：原始日志（original log）；无推荐的模拟模型日志（simulation model log）；不同建议遵循率的模拟日志（33%、66%、100%）；不同α参数值（0.0, 0.25, 0.5, 0.75, 1.0）
- Benchmark 表述引文：Section 9: 'The event data recording about one year of completed instances (total: 1065 traces) was used as a benchmark for our evaluation.'
- Benchmark 评价：在保险公司提供的一年事件日志（benchmark）上，作者构建了CPN Tools模拟模型，并运行推荐系统，将推荐系统产生的模拟日志（100%、66%、33%建议遵循率，多种α值）与原始日志和未加推荐的模拟日志进行比较，报告故障实例百分比、平均/中位故障严重性，并进行卡方检验、Kruskal-Wallis检验等。
- 判定理由：该文章以降低业务流程执行中的故障数量和严重性作为唯一核心目标，所有评价均基于从事件日志中计算出的客观故障指标（时间、事件出现、数量），无任何主观评价指标。Evaluation部分明确将公司一年事件日志称为benchmark，并以此作为比较基线，展示推荐系统带来的显著改进（统计检验支持）。因此同时满足客观指标提升和明确benchmark两个条件，严格纳入。
- 置信度：0.95

### A web recommendation system considering sequential information 

- 年份/期刊：2015 / Decision Support Systems
- DOI：10.1016/j.dss.2015.04.004
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：预测准确率（Accuracy）；精确率（Precision）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：MSNBC benchmark dataset（UCI web navigation dataset）
- 参照点：随机预测模型（random prediction model）；一阶马尔可夫模型（first order Markov model）
- Benchmark 表述引文：摘要：'We tested our approach on three datasets, the MSNBC benchmark dataset, simulated dataset and CTI dataset. We compared our approach with the first order Markov model as well as random prediction model.' 第4节：'The first data set is the MSNBC web navigation data set, which is a bench mark dataset.'
- Benchmark 评价：在MSNBC benchmark数据集（另加模拟数据集和CTI数据集）上评价所提出的基于S3M相似性、软聚类和SVD的推荐系统，报告Top-1、Top-2、Top-3下一页面预测的准确率和精确率；结果与随机预测模型和first-order Markov模型比较。Tables 5-8和Figures 2-4显示提出模型在准确率和精确率上均优于两个显式基线。
- 判定理由：客观指标：核心成功指标是下一页面预测的准确率和精确率，均通过web日志中的实际页面访问事实进行确定性计算，不依赖人类主观评价；且全文没有把满意度、感知质量等主观构念作为成功标准。唯一核心目标：研究问题、系统设计和贡献声明都围绕提升下一页面预测的客观性能，未发现并列的主观、理论或制度性核心贡献。Benchmark：全文明确将MSNBC称为公开benchmark dataset，并在实验部分作为核心评价场地，与随机预测模型和first-order Markov模型等显式基线比较，benchmark结果直接支撑了核心提升主张。因此strict_include=true。
- 置信度：0.95

### APATE: A novel approach for automated credit card transaction fraud detection using network-based extensions 

- 年份/期刊：2015 / Decision Support Systems
- DOI：10.1016/j.dss.2015.04.013
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：AUC（ROC曲线下面积）；Accuracy（准确率）；Specificity / Balanced Accuracy（在1%假阳性率下的特异性与平衡准确率）
- Benchmark 状态：benchmark_comparison_central
- 参照点：logistic regression；neural network；random forest；变量子集：Only RFM, Literature, Only Social Networks, All variables
- Benchmark 表述引文：Section 4.1（Prediction Results）：'According to the findings of related research (see Section 2.3), we will benchmark three of them: logistic regression, the standard general linear model for classification used in many banking related activities...; a feed-forward, one hidden layer, neural network...; and a random forest...'
- Benchmark 评价：在APATE特征组合上，分别使用逻辑回归、神经网络和随机森林三种模型进行基准比较，在同一公司真实测试集（约50万笔交易）上报告AUC和accuracy；随后在Section 4.2通过变量子集基准比较（Only RFM、Literature、All Variables - First transaction、Only Social Networks、All variables）展示网络特征加入后AUC从0.953提升到0.986。
- 判定理由：文章核心目标是提升信用卡欺诈检测的客观预测性能；核心指标为AUC、accuracy、specificity，欺诈标签为外部可核验事实标签，完全客观。全文没有并列的核心主观目标或理论机制贡献。在Results部分作者使用明确的benchmark表述，对逻辑回归、神经网络、随机森林三个模型进行基准比较，并通过变量子集比较证明网络特征带来的性能提升，benchmark评价支撑了核心客观指标提升主张，且有明确参照点。因此两个模块均通过，strict_include=true。
- 置信度：0.95

### Efficient identity matching using static pruning q-gram indexing approach 

- 年份/期刊：2015 / Decision Support Systems
- DOI：10.1016/j.dss.2015.02.015
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：匹配有效性：Precision、Recall、F-measure；效率：比较次数、约简率RR、完成时间；可扩展性：Scalability ∝ N/t
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：ADIM (adaptive detection identity matching) [32]；Pairwise identity matching approach；SecondString census dataset；Credit application dataset from [24]（FEBRL synthetic dataset）
- 参照点：Pairwise identity matching technique（作为最可信的基线基准）；Adaptive detection identity matching (ADIM) [32]（作为面向大数据集的benchmark方法）
- Benchmark 表述引文：引言明确写道：“We benchmarked our proposed identity matching technique against adaptive detection identity matching (ADIM) [32] and the most trusted pairwise identity matching technique.” 第4.4.2节将pairwise最优有效性结果用作“baseline benchmark”，第4.4.3节将pairwise效率结果用作“baseline benchmark”；结论部分又称“The benchmark ADIM technique was designed for efficiency and scalability for large datasets.”
- Benchmark 评价：在SecondString census数据集（841条记录，344对真实匹配）和FEBRL credit application合成数据集（由52,696条记录生成不同规模，并与ADIM、pairwise比较）上评价提出的static pruning q-gram索引身份匹配技术。有效性benchmark：census F-measure 0.674（pairwise 0.636，ADIM 0.543），credit F-measure 0.973（pairwise 0.960，ADIM 0.709）。效率benchmark：与ADIM相比，census数据集比较次数从218,112降至3,608（减少98%），完成时间从1,268ms降至31ms（减少97%）；credit应用数据集比较次数减少96%，完成时间大幅下降。可扩展性benchmark：在10k-50k递增数据上，提出方法优于ADIM。
- 判定理由：客观指标模块通过：核心指标包括匹配有效性（F-measure等，基于同一真实个人这一事实标签的预测性能）以及效率（比较次数、RR、完成时间）、可扩展性（N/t），全部为客观可测量指标；没有满意度、感知质量、专家评分等主观构念作为核心结果。唯一核心目标是提升效率同时保持/提升匹配有效性，全文围绕H1-H3三个客观假设和实验展开，没有并列的主观或理论贡献。Benchmark模块通过：引言明确使用benchmark动词将提出方法与ADIM和pairwise进行比较；实验部分多处将pairwise/ADIM作为baseline benchmark，并在census和credit application数据集上评价；benchmark结果直接用于支持比较次数、完成时间、F-measure和可扩展性的核心提升主张；具有明确参照点（pairwise基线和ADIM）。因此strict_include=true。
- 置信度：0.97

### Financial fraud detection using vocal, linguistic and financial cues 

- 年份/期刊：2015 / Decision Support Systems
- DOI：10.1016/j.dss.2015.04.006
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：AUC（ROC曲线下面积）；给定检测率下的误报数/误报概率
- Benchmark 状态：benchmark_comparison_central
- 参照点：AR（商业会计风险指标）；COGDIS（语音认知失调指标）；Fscore（学术欺诈评分）；未做特征选择的全特征组合；未加入基线指标的组合特征
- Benchmark 表述引文：第3.1节标题为“Benchmark results”，文中明确称“Fig. 2 simply replicates the benchmark conditions already documented in [9]”，并报告AR、COGDIS、Fscore三条基线的ROC/AUC。
- Benchmark 评价：在同一1572个电话会议样本上，将本文提出的会计风险与声学特征组合（含或不含基线指标）与AR、COGDIS、Fscore三种已有基线工具进行比较；结果显示组合特征优于最佳基线AR，最佳条件AUC达到0.81，并在90%检测率下减少15%误报。
- 判定理由：客观指标方面，核心成功标准是对外部事实标签（会计重述/财务欺诈）的检测性能（AUC、检测率、误报数），不涉及主观评价或语义质量判断，且提升检测性能是全文唯一核心目标与贡献。benchmark方面，第3.1节明确以“Benchmark results”陈述基准评价，将组合特征与AR、COGDIS、Fscore等明确基线在ROC/AUC上比较，benchmark结果直接支撑核心提升主张。因此两个模块均通过，strict_include为true。
- 置信度：0.96

### On the brink: Predicting business failure with mobile location-based checkins 

- 年份/期刊：2015 / Decision Support Systems
- DOI：10.1016/j.dss.2015.04.010
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：误分类率 (Misclassification Rate)；平均绝对偏差 (MAD)；AIC
- Benchmark 状态：benchmark_comparison_central
- 参照点：Model 1（基准模型：仅业务特征变量）；Model 2（加入focal restaurant checkin变量）；Model 3（再加入邻居checkin变量）；KNN模型（作为与Logit的额外比较）
- Benchmark 表述引文：在4.2节Logit模型结果部分，作者明确写道：“Following the predictive modeling tradition, we use the model with only business characteristics variables as our benchmark model, and then compare the proposed model (with both business characteristics and checkin variables) with our benchmark model.”
- Benchmark 评价：在自建的纽约市686家餐厅数据上，将仅含业务特征的Logit基准模型与逐步加入focal restaurant和邻居checkin变量的模型进行比较，报告in-sample/out-of-sample MAD和误分类率。结果显示加入checkin变量后MAD从0.153降至0.056，误分类率从0.134降至0.055，提升显著。
- 判定理由：客观指标：核心结果指标是预测误分类率、MAD、AIC，这些均基于客观可观测的checkin记录和固定失败定义，不依赖人类感受或语义评价；预测对象是外部可核验的虚拟死亡标签。唯一核心目标：研究问题、设计目标、评价结构和贡献声明均围绕“使用LBS checkin数据提升业务失败预测准确性”展开，无主观量表或并列核心贡献。Benchmark：4.2节明确使用“benchmark model”一词，将仅含业务特征的模型作为基准，并在评价语境中与加入checkin变量的模型比较，benchmark结果直接支撑核心预测提升主张，且有明确参照点。故两个模块均通过，strict_include=true。
- 置信度：0.95

### Process mining on noisy logs — Can log sanitization help to improve performance? 

- 年份/期刊：2015 / Decision Support Systems
- DOI：10.1016/j.dss.2015.08.003
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：行为精确率与行为召回率（Behavioral precision/recall）；结构精确率与结构召回率（Structural precision/recall）；模型紧凑性（places/transitions/arcs数量）；工作流正确性（Woflan验证结果）
- Benchmark 状态：benchmark_comparison_central
- 参照点：noisy log vs sanitized log 的对比；Alpha++ vs Heuristics Miner 两个算法的对比；不同噪声水平（2%, 5%, 10%, 20%）的对比；真实数据实验中 dirty log vs clean log 的对比
- Benchmark 表述引文：第3.2节：'For benchmarking process mining algorithms, six reference process models of increasing complexity (levels 0 through 5) were created by us...'；第3.3节：'In this section we give results from testing two algorithms on our metrics with varying amounts of noisy data'；第5.3节：'We benchmarked two process mining algorithms for noise-free, noisy, and sanitized logs.'
- Benchmark 评价：作者自建六个参考过程模型（复杂程度递增的level 0–5）作为基准，在两个知名过程挖掘算法（Alpha++和Heuristics Miner）上评价日志净化前后挖掘模型的性能；核心结果（Table 10）对比了noisy log和sanitized log在行为/结构精确率与召回率四个指标上的表现，并报告了提升百分比；还使用Woflan检验模型正确性及模型紧凑性。
- 判定理由：文章唯一核心目标是通过日志净化（log sanitization）提升过程挖掘模型的质量，所有评价指标均为可计算的客观指标（行为/结构precision/recall、模型紧凑性、Woflan验证），没有任何主观量表或人类语义评价作为核心成功标准；全文存在明确的benchmark表述：作者自建六个参考过程模型作为基准，并将两个算法在noisy与sanitized logs上的结果进行系统化对比，benchmark评价直接支撑核心提升主张，且有明确参照点。因此严格纳入条件全部满足。
- 置信度：0.97

### A model-free scheme for meme ranking in social media 

- 年份/期刊：2016 / Decision Support Systems
- DOI：10.1016/j.dss.2015.10.002
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：Kendall-tau_Sim；Edit_Sim
- Benchmark 状态：benchmark_comparison_central
- 参照点：Follower_Num（粉丝数中心性）；PageRank；Dynamic（动态行为数）；Diffusion（扩散概率）
- Benchmark 表述引文：§4.3.3开头：'To evaluate the comparative performance of the proposed ranking scheme, we also introduce four representative benchmark approaches in the literature.'（在实验设计部分明确将四种既有方法作为benchmark approaches进行比较）
- Benchmark 评价：在两个大规模真实数据集（新浪微博和Daily Kos）上，将提出的无模型方案（MF）与Follower_Num、PageRank、Dynamic、Diffusion四个基准方法比较；在Kendall-tau_Sim和Edit_Sim两个排名相似度指标上，MF显著优于四个基准。例如Kos数据集：Kendall-tau_Sim 0.822 vs 最优基准0.578，Edit_Sim 0.500 vs 最优基准0.200；Weibo数据集：Edit_Sim 0.400 vs 最优基准0.200。
- 判定理由：核心指标为排名相似度（Kendall-tau_Sim、Edit_Sim），基于平台黄金标准排名进行确定性计算，完全客观，不依赖人类感知或语义判断。论文的唯一核心目标是提出并验证meme排名方案，使排名更接近黄金标准；Issue 3的流行度因子解释是辅助性洞察，不构成并列核心贡献。实验设计明确以'benchmark approaches'名义引入四种可比较的既有方法，并在两个数据集上通过结果表证明方案优于这些对照，符合明确的benchmark比较门槛。三个模块均通过，strict_include为true。
- 置信度：0.93

### Balancing quality and budget considerations in mobile crowdsourcing 

- 年份/期刊：2016 / Decision Support Systems
- DOI：10.1016/j.dss.2016.06.019
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：平均错误率 e；平均预算利用率 B^(-)；平均旅行距离 D
- Benchmark 状态：benchmark_comparison_central
- 参照点：CrowdBudget；GeoTruCrowd
- Benchmark 表述引文：实验设计部分写明：“Two state-of-the-art approaches most related to Budget-TASC are selected as benchmark approaches.”（Section 5.1），随后用CrowdBudget和GeoTruCrowd作为比较基线。
- Benchmark 评价：在基于Foursquare新加坡子集生成的空间众包模拟场景上，将Budget-TASC与CrowdBudget、GeoTruCrowd进行比较，覆盖不同任务半径和预算设置，报告平均错误率、预算利用率、平均旅行距离；结果显示Budget-TASC的平均错误率15.4%，低于GeoTruCrowd的28.0%和CrowdBudget的81.1%，预算利用率67.6%，低于两者的84.8%和96.5%。
- 判定理由：客观指标方面，核心成功指标是平均错误率、预算利用率和平均旅行距离，均由模拟日志和可审计数值计算，不依赖主观人类评价；唯一核心目标是在预算约束下提升众包结果质量，实验和贡献声明均围绕该目标。Benchmark方面，实验部分明确将CrowdBudget和GeoTruCrowd选为benchmark approaches，在Foursquare数据生成场景上进行系统化比较，并给出明确参照点和性能提升证据。因此两个模块均通过，strict_include=true。
- 置信度：0.9

### Effective demand response for smart grids: Evidence from a real-world pilot 

- 年份/期刊：2016 / Decision Support Systems
- DOI：10.1016/j.dss.2016.07.007
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：平均峰值降低率；电费节省率
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：Gottwalt et al. (2011) variable pricing；Di Giorgio & Pimpinella (2012) two-tier TOU tariff；Di Giorgio & Pimpinella (2012) three-tier TOU tariff；Doostizadeh & Ghasemi (2012) winter variable tariff；Doostizadeh & Ghasemi (2012) summer variable tariff
- 参照点：Gottwalt et al. (2011) variable pricing；Di Giorgio & Pimpinella (2012) two-tier tariff；Di Giorgio & Pimpinella (2012) three-tier tariff；Doostizadeh & Ghasemi (2012) winter tariff；Doostizadeh & Ghasemi (2012) summer tariff
- Benchmark 表述引文：第4.4节开头："To evaluate our approach against existing ones in the literature, we use a set of benchmarks that has been used in the context of household electricity consumption."
- Benchmark 评价：在第4.4节中，作者将文献中多个基准电价方案（Gottwalt等、Di Giorgio & Pimpinella、Doostizadeh & Ghasemi）应用于相同的数据和模拟框架，报告平均峰值降低率和电费节省率，并通过图表展示所提出的TOU方案在这些客观指标上整体优于文献基准，用以支撑核心改进主张。
- 判定理由：客观指标方面：核心成功指标为平均峰值降低率和电费节省率，均来自智能电表数据和模拟计算，属于完全客观的可测量结果，且全文核心目标为设计有效DR方案以提升这些指标；未发现与客观指标提升并列的主观或理论核心贡献。Benchmark方面：第4.4节明确使用'benchmarks'一词进行系统性比较，比较对象为文献中的多个电价方案，位于评价语境并直接支撑所提方案在峰值降低和成本节省上的改进主张，且有明确参照点。因此严格包含。
- 置信度：0.78

### Fused latent models for assessing product return propensity in online commerce 

- 年份/期刊：2016 / Decision Support Systems
- DOI：10.1016/j.dss.2016.08.002
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：退货倾向（return propensity）
- Benchmark 状态：benchmark_comparison_central
- 参照点：PMF（Probabilistic Matrix Factorization）；NMF（Nonnegative Matrix Factorization）；User Frequency based Method；Item Frequency based Method；RPLM（未融合用户/商品特征的版本）
- Benchmark 表述引文：结论部分：'The performance improvement of our proposed method is substantial, compared to benchmark methods.' 第6.3节以 'Baseline algorithms' 列出比较方法，第6.5节报告与各基线的 Precision/Recall/ROC/AUC 对比。
- Benchmark 评价：在真实在线零售数据集上评价 FRPLM，并与 PMF、NMF、基于用户频率、基于商品频率的方法以及未融合特征的 RPLM 比较；FRPLM 在 Precision@N、Recall@N、ROC/AUC 等指标上优于基线。
- 判定理由：核心构念为基于订单/退货日志计算的退货倾向，属于可审计事实标签，评价指标全部客观；研究目标与贡献声明均围绕提升该预测性能展开，无主观体验或理论机制作为并列核心。benchmark 方面，虽然未命名公开数据集，但作者在结论中明确使用 benchmark methods 指称系统化基线比较，且第6.3-6.5节提供了与多个基线的客观指标对照，该比较直接支撑核心性能提升主张。因此两个模块均通过。
- 置信度：0.75

### Late payment prediction models for fair allocation of customer contact lists to call center agents 

- 年份/期刊：2016 / Decision Support Systems
- DOI：10.1016/j.dss.2016.03.002
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：客户名单分配的公平性，即各坐席实际/模拟回收债务金额的变异程度；滞纳支付预测性能（作为公平分配的前置手段）
- Benchmark 状态：benchmark_comparison_central
- 参照点：Tenure (TEN)；Cumulative unpaid month (CUM)；Cumulative unpaid amount (CUA)
- Benchmark 表述引文：方法部分（3.2节）：'Three heuristic-based approaches that are already deployed in the company that provided the experimental customer dataset are used as benchmark scoring rules (Figure 3(a)).' 结果部分表12：'The number of best cases for each benchmarked customer scoring rules...'
- Benchmark 评价：将三种现有启发式评分规则（TEN、CUM、CUA）作为 benchmark 基准，与十种基于预测模型的评分规则在十个不同坐席人数场景下比较。核心结果（表6-12）显示，模型评分规则在降低各坐席回收债务金额变异方面多数情况下优于启发式规则；EPST、EPRF 等最优次数最多，robustness test 也用 F 检验与三种启发式方法比较。
- 判定理由：该文的核心目标是构建基于机器学习的滞纳支付预测模型和客户评分规则，以降低各催收坐席之间回收债务金额的变异，实现客观可测的名单分配公平性。评价指标为标准差、极差、四分位距和变异系数，均由账单/回收金额计算，完全客观；坐席偏好调查仅作为间接补充。全文存在明确的 benchmark 表述：三种现有启发式评分规则被明确称为 benchmark scoring rules，并在实验部分与十种基于预测模型的评分规则系统比较，比较结果直接支撑公平性提升的核心主张。因此同时通过客观指标和 benchmark 两个门槛。
- 置信度：0.92

### News-based trading strategies 

- 年份/期刊：2016 / Decision Support Systems
- DOI：10.1016/j.dss.2016.06.020
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：平均每日收益率；平均每日异常收益率；波动率/风险；Sharpe比率和变异系数
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：CDAX index
- 参照点：CDAX index；Momentum trading；Portfolio trading
- Benchmark 表述引文：Section 3.1: “the so-called CDAX index works as a benchmark which the trading strategies need to surpass in terms of performance”；Section 4.1: “we start by presenting our benchmarks, namely, a momentum trading and a portfolio approach”；Section 5.1: “As our first benchmark, we choose the so-called CDAX”。
- Benchmark 评价：在CDAX指数、动量交易和组合交易等基准上评价新闻交易策略；简单新闻交易平均日收益0.4722%，监督学习1.1807%，明显高于CDAX基准0.0298%和动量交易0.0464%；统计检验进一步验证收益显著为正。
- 判定理由：全文以交易策略的财务绩效（日收益、异常收益、波动率、Sharpe比率等）作为核心结果，这些指标均由市场行情和交易模拟客观计算，不涉及主观评价或语义判断；研究问题、评价结构和贡献声明均围绕提升财务绩效展开，未发现并列的核心贡献。作者在评价部分明确使用benchmark一词，以CDAX指数、动量交易和组合交易为参照，系统比较新闻交易策略的收益提升，且该比较是支撑核心盈利性主张的关键证据。因此两个模块均通过，strict_include=true。
- 置信度：0.92

### PhishWHO: Phishing webpage detection via identity keywords extraction and target domain name finder 

- 年份/期刊：2016 / Decision Support Systems
- DOI：10.1016/j.dss.2016.05.005
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：钓鱼网页检测性能：TPR、FPR、TNR、FNR、Accuracy、MCC
- Benchmark 状态：benchmark_comparison_central
- 参照点：M1：基于文本的方法 [25]（Zhang et al., CANTINA）；M2：基于身份的方法 [20]（Ramesh et al.）；M3：基于特征的方法 [12]（Huh & Kim）
- Benchmark 表述引文：Section 4.3: “In Experiment III, the proposed method is benchmarked against a conventional feature-based method, i.e., [12], denoted as M3.”；此外Table 10和Table 11的标题均为“Benchmark results for Experiment II/III”。
- Benchmark 评价：作者在实验II中将PhishWHO与两种采用类似分析技术的传统方法M1（基于文本的CANTINA类方法[25]）和M2（基于身份的方法[20]）比较；在实验III中将PhishWHO与基于特征的搜索引擎方法M3 [12]比较。比较指标包括TPR、FPR、TNR、FNR、Accuracy和MCC。结果显示PhishWHO在TPR和MCC上优于M1/M2/M3，并用这些结果支持“PhishWHO outperforms conventional methods”的核心主张。数据集来自PhishTank/OpenPhish（钓鱼样本）和Alexa（合法样本），虽然不是公开命名benchmark套件，但作者明确用benchmarking表述在评价语境中完成系统化基准比较。
- 判定理由：客观指标方面：核心成功指标是钓鱼网页检测的TPR/FPR/TNR/FNR/Accuracy/MCC，这些是基于PhishTank/OpenPhish/Alexa事实标签计算的分类性能，完全客观且可审计；全文没有主观量表或语义质量评价作为核心结果。唯一核心目标方面：研究问题、方法设计、实验评价和贡献声明均围绕客观检测性能提升展开，没有并列的理论、制度或行为解释贡献。Benchmark方面：作者在实验III中明确使用“benchmarked against”陈述系统化基准比较，并在实验II/III中将PhishWHO与M1、M2、M3等明确参照方法比较，比较结果直接支持核心提升主张。因此两项门槛均通过，strict_include为true。
- 置信度：0.95

### Prediction uncertainty in collaborative filtering: Enhancing personalized online product ranking 

- 年份/期刊：2016 / Decision Support Systems
- DOI：10.1016/j.dss.2015.12.004
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：Top-N 推荐性能：precision 与 recall；整体排序质量：nDCG@p
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：MovieLens（公开标准电影评分数据集）；RCF（作者明确称为 benchmark ranking approach）
- 参照点：RCF（Ranking by Collaborative Filtering）；userKNN；MF；SVD；PMF；BPMF
- Benchmark 表述引文：实验部分（Section 5）开篇：'RCF can be seen as a benchmark ranking approach which does not consider the prediction uncertainty.' 同时称 '5 different CF techniques are used as benchmarks'。这是将 RCF 和多种 CF 方法作为评价基准的明确 benchmark 表述。
- Benchmark 评价：在 MovieLens 数据集上，基于 5 种基础 CF 技术（userKNN、MF、SVD、PMF、BPMF），分别比较 RCF 与两种 RPU 变体（min-max 离散化和 quantile 离散化）的 top-N precision/recall 与 nDCG@p。结果表（Table 3、Table 4）和图 4、图 5 显示 RPU 在所有设定下均优于 RCF 基准；稀疏数据实验亦显示改善。
- 判定理由：客观指标部分：文章核心目标是提升个性化产品排序的准确性，全部核心成功指标为 precision、recall 和 nDCG，均基于 MovieLens 真实评分可确定性计算，不依赖主观评价或人类语义判断；除排序准确性提升外没有并列的核心贡献。benchmark 部分：作者在实验评价语境中明确将 RCF 称为 benchmark ranking approach，并将 5 种 CF 技术用作 benchmarks，在 MovieLens 上系统比较 RPU 与 RCF，结果表显示明确提升，属于支撑核心改进主张的基准比较。因此两个模块均通过，strict_include=true。
- 置信度：0.93

### The added value of Facebook friends data in event attendance prediction 

- 年份/期刊：2016 / Decision Support Systems
- DOI：10.1016/j.dss.2015.11.003
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：AUC（ROC曲线下面积）
- Benchmark 状态：benchmark_comparison_central
- 参照点：baseline model（仅用户数据）与 augmented model（用户+朋友数据）；五种分类算法之间的性能比较（Adaboost、Random Forest、Logistic Regression、Neural Networks、Naive Bayes）
- Benchmark 表述引文：引言语境：'Furthermore, we benchmark these two models for five state-of-the-art classification algorithms namely Logistic Regression, Random Forest, Adaboost, Neural Networks and Naive Bayes.'（Section 1, Introduction）
- Benchmark 评价：作者将baseline和augmented两个模型在五种分类算法（Logistic Regression、Random Forest、Adaboost、Neural Networks、Naive Bayes）上进行基准对比；评价场地为自建的Facebook事件出席数据，使用5×2交叉验证计算AUC，并通过Wilcoxon符号秩检验比较模型差异。基准结果用于证明加入friends数据能提升AUC，是核心主张的核心证据。
- 判定理由：客观指标方面：核心成功指标AUC基于客观可观察的事件出席标签和分类器输出计算，不依赖主观感受或语义判断，所有核心成功结果均为客观指标。唯一核心目标方面：全文围绕friends data对AUC的增量提升展开，研究问题、评价设计和贡献声明均一致，未发现并行的主观、理论或机制核心贡献。Benchmark方面：作者明确使用benchmark一词描述对两个模型在五种分类算法上的系统基准比较；该基准比较是证明core improvement（AUC提升）的关键证据，且有明确参照点（baseline模型）。因此两个模块均通过，strict_include=true。
- 置信度：0.95

### Who should you follow? Combining learning to rank with social influence for informative friend recommendation 

- 年份/期刊：2016 / Decision Support Systems
- DOI：10.1016/j.dss.2016.06.017
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：C@K（coverage rate at K）；MRR（mean reciprocal rank）；DCRP（discounted cumulative ranking performance）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：WISE 2012 Challenge Weibo dataset
- 参照点：Pop；FdFd；FlFd；KNN；MF；SVD++；MF+LTR；CLiMF；SR
- Benchmark 表述引文：第 4.1 节：‘we conducted experiments using the Weibo dataset from the WISE 2012 Challenge’；同节又描述该数据：‘The Weibo dataset consists of 58,655,849 users and 366,946,149 updates, and is so big that it has been frequently used as a benchmark for big data analytics [2,3,35]’。
- Benchmark 评价：在公开的 WISE 2012 Challenge 微博数据集上，选取 Data200 和 Data300 两个子集，采用 leave-one-out 程序评价所提方法（OurMethod_fix 和 OurMethod_adaptive）与九个既有方法，在 C@K、MRR、DCRP 上比较，并附统计显著性检验。结果表显示所提方法在大部分指标上优于基线方法，支撑核心的性能提升主张。
- 判定理由：客观指标：核心结果指标 C@K、MRR、DCRP 全部由实际点赞/回复日志和推荐列表确定性计算，操作化构念是行为事实而非主观感知。唯一核心目标：全文设计、实验和贡献均围绕提升信息型好友推荐性能，不存在并列的主观体验、理论机制或制度政策核心目标。Benchmark：论文在评价部分公开命名并使用 WISE 2012 Challenge Weibo 数据集作为评价场地，明确将数据描述为 benchmark，并与九个基线方法进行对比，benchmark 比较结果是核心性能提升主张的直接证据。因此 strict_include=true。
- 置信度：0.82

### A comparative analysis of data preparation algorithms for customer churn prediction: A case study in the telecommunication industry 

- 年份/期刊：2017 / Decision Support Systems
- DOI：10.1016/j.dss.2016.11.007
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：AUC（ROC曲线下面积）；Top Decile Lift (TDL)
- Benchmark 状态：benchmark_comparison_central
- 参照点：18种DPT组合相互比较（含默认/标准DPT：no regrouping、dummy coding等）；LOGIT-DPT 对比 Bag, B-Net, DT, NN, NB, RF, SVM, SGB
- Benchmark 表述引文：摘要：'This study ... benchmarks an optimized logit model against eight state-of-the-art data mining techniques...'；3.3节：'The validation set serves to mimic real-life prediction performance and thus to benchmark the optimized DPT methods.'；4.2节：'the statistical test results that benchmark our LOGIT-DPT against the advanced benchmark algorithms.'
- Benchmark 评价：在电信客户流失数据集（以及额外的信用评分、响应建模数据）上，将优化后的LOGIT-DPT与Bag、B-Net、DT、NN、NB、RF、SVM、SGB等八个基准分类器在验证集上按AUC和TDL比较；同时对18种DPT组合进行系统比较。
- 判定理由：本文核心是提升客户流失预测的完全客观性能指标AUC和TDL，并证明优化数据准备后的logistic回归与先进分类器相比具有竞争力；无任何主观量表或语义判断作为核心成功标准。全文在摘要、实验设计和结果部分均有明确benchmark/benchmarking表述，且以8个基准分类器和多种DPT组合作为参照点进行统计比较，符合benchmark_comparison_central。因此两模块均通过，strict_include=true。
- 置信度：0.97

### A cross-domain recommender system with consistent information transfer 

- 年份/期刊：2017 / Decision Support Systems
- DOI：10.1016/j.dss.2017.10.002
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：平均绝对误差 (MAE)；均方根误差 (RMSE)
- Benchmark 状态：benchmark_comparison_central
- 参照点：PCC；FMM；SVD；CBT；RMGM
- Benchmark 表述引文：摘要中的明确表述："The results for nine cross-domain recommendation tasks show that CIT outperforms five benchmarks and increases the accuracy of recommendations in the target domain, especially with sparse data."（位置：Abstract）
- Benchmark 评价：在五个真实数据集（Movielens20M、Netflix、LibraryThing、Amazon Book、YahooMusic）上构造九个跨域推荐任务，使用 MAE 和 RMSE 与五个基线方法（PCC、FMM、SVD、CBT、RMGM）比较。CIT 在绝大多数任务中获得最低 MAE/RMSE，并通过显著性检验。
- 判定理由：客观指标 MAE/RMSE 为完全客观的推荐预测误差，全文以提升推荐精度为唯一核心目标；存在明确 benchmark 表述（摘要中 outperforms five benchmarks），且实验部分提供与五个基线的完整比较，benchmark 评价直接支撑核心提升主张。因此 strict_include=true。
- 置信度：0.9

### An empirical study of natural noise management in group recommendation systems 【全文无benchmark字样-需人工复核】

- 年份/期刊：2017 / Decision Support Systems
- DOI：10.1016/j.dss.2016.09.020
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：平均绝对误差（MAE）预测误差
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：MovieLens 100k dataset；Netflix Tiny dataset
- 参照点：Base（未进行自然噪声管理的基线GRS）；NNM-GG/NNM-H与Base的配对样本t检验；NNM-GG与NNM-H的配对样本t检验
- Benchmark 表述引文：论文虽未使用benchmark一词，但在Section 4.1 Experimental protocol中明确列出MovieLens 100k和Netflix Tiny作为评价数据集；这两个数据集是推荐系统领域常用的公开基准数据集，且随后在4.2和4.3节以其作为评价场地比较各NNM方法和基线。
- Benchmark 评价：在MovieLens 100k和Netflix Tiny两个公开数据集上，对推荐聚合和评分聚合两类GRS，结合IB/UB与Avg/Min聚合，报告Base、NNM-LL、NNM-LG、NNM-GG、NNM-H的MAE；结果以Base为参照，验证NNM-GG和NNM-H降低MAE，且NNM-H在多数IB配置下优于NNM-GG。
- 判定理由：客观指标方面，MAE是系统预测评分与测试集实际评分之间的确定性误差，不依赖人类语义评价或主观感受；全文唯一核心目标是将自然噪声管理引入GRS并提升预测精度，无并列的主观或理论核心贡献。Benchmark方面，论文虽然没有使用benchmark一词，但在评价语境中明确使用MovieLens 100k和Netflix Tiny两个公开基准数据集作为评价场地，并与Base基线及方法间进行配对t检验比较，结果直接支撑NNM-GG和NNM-H降低MAE的核心主张。因此两个模块均通过，strict_include为true。
- 置信度：0.86

### An upper approximation based community detection algorithm for complex networks 

- 年份/期刊：2017 / Decision Support Systems
- DOI：10.1016/j.dss.2017.02.010
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：归一化互信息 (NMI)；Partition Density；模块度 (Modularity)
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：Karate Club；Risk；Dolphin；High School Friendship；Les Miserables；Polbooks；Football；Jazz；Email；PolBlog；SFI Collaboration；Roget's Thesaurus；Krogan's PPI；Power Grid
- 参照点：CPM；ABL；BNMF；OSLOM；FastQ；Walktrap；INFOMAP；LPA
- Benchmark 表述引文：摘要中明确写道：“evaluate it on fourteen real-world benchmark networks”；第 5 节实验部分也写道：“We considered fourteen benchmark networks for our experiments”。这些表述出现在摘要和实验评价部分。
- Benchmark 评价：ROCONA 在 14 个公开标准网络数据集上运行，并与 CPM、ABL、BNMF、OSLOM、FastQ、Walktrap、INFOMAP、LPA 等既有算法比较；有 ground-truth 的网络使用 NMI，Les Miserables 使用 partition density，无 ground-truth 的网络使用 modularity。结果显示 ROCONA 在多数数据集上取得最高或接近最高的客观指标值。
- 判定理由：本文核心目标是提出新的社区检测算法 ROCONA，并以 NMI、partition density、modularity 等完全客观的结构性指标证明其检测准确度提升。全文不存在用户主观评价、心理机制或理论解释等并列核心目标。文章在摘要和实验部分明确使用了“fourteen benchmark networks”的表述，在 14 个公开标准网络数据集上进行系统比较，并与多种现有算法对照，benchmark 结果直接支撑“significantly outperforms state-of-the-art”的核心主张。因此两个模块均通过，strict_include=true。
- 置信度：0.95

### Computational intelligent hybrid model for detecting disruptive trading activity 

- 年份/期刊：2017 / Decision Support Systems
- DOI：10.1016/j.dss.2016.09.003
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：AUC（ROC曲线下面积）；Recall、Precision、F measure、G score
- Benchmark 状态：benchmark_comparison_central
- 参照点：kNN；GMM；LR
- Benchmark 表述引文：第4.3.1节实验设定：'The three popular computational models are selected as benchmarks for evaluating the proposed model'；摘要及实验总结亦明确称模型'outperform the selected traditional benchmark models'。
- Benchmark 评价：在NASDAQ四只股票（Google、Microsoft、Intel、Apple）2013年真实tick数据上，按三组实验注入合成/复现的异常样本，将混合模型与kNN、GMM、LR三个基准模型进行系统对比，报告Recall、Precision、F measure、G score及ROC-AUC；混合模型在所有数据集和实验组上均取得最高AUC。
- 判定理由：客观指标方面：核心成功指标为检测性能（AUC、Recall、Precision、F/G），标签为固定事实类别的disruptive trading行为，不依赖主观感受，指标客观且是唯一核心目标。Benchmark方面：作者在实验部分明确以kNN/GMM/LR为benchmark模型，系统比较并在核心提升主张中使用这些基准结果，具有明确参照点。二者均通过，因此strict_include=true。
- 置信度：0.92

### Data-driven Process Prioritization in Process Networks 

- 年份/期刊：2017 / Decision Support Systems
- DOI：10.1016/j.dss.2017.02.011
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：总机会成本（Total Opportunity Costs）；深度分析排程/优先级列表（priority list）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：2012 BPI Challenge log
- 参照点：ProcessPageRank (PPR)；Critical Process Instance Method (CPIM)
- Benchmark 表述引文：第4.4.4节：“we also compared the D2P2 against competing artefacts, i.e., PPR [9] and CPIM [21], using the real-world case as a benchmark.” 同时，第4.4节明确将2012 BPI Challenge log作为真实世界评价场景。
- Benchmark 评价：将D2P2原型应用于经层次挖掘和现金流失真处理的2012 BPI Challenge log，建立包含4个流程的过程网络，运行10,000次Monte Carlo模拟并求解MILP；在相同案例上运行PPR和CPIM，比较排程结果和总机会成本。结果显示D2P2排程为P2(1期)、P1(2期)、P3(4期)，总机会成本为0；PPR总机会成本为12,441；CPIM排程大致相同但多排P4，D2P2更节省分析容量。
- 判定理由：全文以日志驱动的D2P2流程优先排序方法设计为核心，以最小化总机会成本和生成合理排程为客观成功指标；第4.4.4节明确将真实案例称为benchmark，并与PPR、CPIM比较，表3给出客观比较结果；未发现主观核心指标或与客观指标提升并列的理论贡献，因此同时满足客观指标、唯一核心目标和明确benchmark三个门槛，strict_include=true。
- 置信度：0.72

### How can online marketplaces reduce rating manipulation? A new approach on dynamic aggregation of online ratings 

- 年份/期刊：2017 / Decision Support Systems
- DOI：10.1016/j.dss.2017.10.003
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：操纵零售商（retailer A）的销售额；诚实零售商（retailer B）的销售额；评分聚合的信息损失概率
- Benchmark 状态：benchmark_comparison_central
- 参照点：即时更新（immediate update）；评分时间衰减（decay）；单值聚合 l=12；单值聚合 l=4；三值聚合 l=12；动态k值聚合（proposed）
- Benchmark 表述引文：5.1.1节：'An immediate update of ratings ... is the most widespread method currently used in practice. It acts as a benchmark in our simulation.' 即即时更新被明确作为模拟中的基准方法。摘要中还有对state-of-the-art聚合方法的比较表述。
- Benchmark 评价：在模拟在线市场中，将动态k值聚合与即时更新、按时间衰减、单值聚合（l=12、l=4）、三值聚合进行比较，报告不同操纵水平下操纵零售商和诚实零售商的销售额。结果显示动态聚合在多数场景下能有效减少虚假评分带来的额外销售，同时仅轻微影响诚实零售商销售。
- 判定理由：本文核心目标是提出并验证一种动态评分聚合方法，以降低在线市场中虚假好评对销售额的操纵影响，同时尽量不损害诚实零售商的销售额；这两个核心结果均为模拟市场中可计数的客观销售指标。评价通过模拟研究完成，5.1.1节明确以即时更新作为基准（benchmark），并与折扣、单值聚合、三值聚合等参照方法比较；该基准评价直接支撑了核心改进主张。因此满足客观指标、唯一核心目标和明确benchmark三方面要求，应纳入。
- 置信度：0.93

### Incorporating association rule networks in feature category-weighted naive Bayes model to support weaning decision making 

- 年份/期刊：2017 / Decision Support Systems
- DOI：10.1016/j.dss.2017.01.007
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：准确率；精确率；召回率；F值
- Benchmark 状态：benchmark_comparison_central
- 参照点：NB；ANN；ANNBFS；SVM；SVMLFS；Clinical protocol performance
- Benchmark 表述引文：第5.2节标题为“Benchmark Techniques”，文中明确写道：'we included conventional NB as a comparison baseline and several data-driven techniques as performance benchmarks: artificial neural network (ANN), ANN with backward feature selection, SVM, and SVM with logistical regression based feature selection'，并在表3中将Clinical protocol performance列为benchmark。
- Benchmark 评价：在自有的1336条真实临床拔管记录上，使用十折交叉验证评价ARFCWNB，并与NB、ANN、ANNBFS、SVM、SVMLFS及临床协议对比。表6显示ARFCWNB的准确率92.60%、加权精确率93.24%、加权召回率92.59%、加权F值92.91%，优于所有基准方法；同时也在类别Y和类别N上分别报告了性能。
- 判定理由：客观指标方面，核心成功指标是拔管成败这一客观事实标签上的预测准确率、精确率、召回率和F值，均由预测结果与实际临床结果标签的混淆矩阵计算，不依赖主观感知或语义评价；全部核心评价均使用这些客观指标。唯一核心目标方面，全文的研究问题、方法设计、评价结构和贡献声明都围绕提升预测性能展开，没有并列的主观体验改善、理论机制贡献或制度建议等核心目标。benchmark方面，作者在第5.2节明确将NB、ANN、ANNBFS、SVM、SVMLFS和临床协议列为benchmark，并在第6节以表6的结果作为核心证据，表明ARFCWNB在所有客观指标上优于多个基准方法，满足明确的benchmark表述、评价语境、支撑核心主张和有明确对照四个门槛。因此严格纳入。
- 置信度：0.96

### Integrated framework for profit-based feature selection and SVM classification in credit scoring 

- 年份/期刊：2017 / Decision Support Systems
- DOI：10.1016/j.dss.2017.10.007
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：利润（Profit）；AUC、准确率、变量数、来源数
- Benchmark 状态：benchmark_comparison_central
- 参照点：Logistic regression；Fisher Score；RFE-SVM；HOSVM_AUC；HOSVM_MPC
- Benchmark 表述引文：5.2节明确写道：“Logistic regression is used as an additional benchmark approach since it is the standard model for credit scoring”；5.3节在比较结果时称“the rest of the benchmarked models”。
- Benchmark 评价：在智利银行的两个信用评分数据集（NEW和RET）上，将提出的l2l∞-SVM和l1l∞-SVM与Logistic回归、Fisher Score、RFE-SVM、HOSVM_AUC、HOSVM_MPC进行比较。表1和表2显示，以利润为模型选择指标时，提出方法在两类客户上的利润均显著高于所有对比方法；表3和表4在AUC选择下也显示利润优势。该benchmark比较是支撑“利润提升”核心主张的关键证据。
- 判定理由：客观指标方面，核心成功指标为利润，由贷款ROI、LGD×EAD和变量获取成本等财务事实直接计算，不依赖主观评价；AUC/准确率也是基于事实标签的客观指标。唯一核心目标是将商业成本收益纳入SVM分类和特征选择并提升利润，全文未提并列的主观或理论核心贡献。Benchmark方面，作者明确使用“benchmark approach”和“benchmarked models”等表述，在实验部分将所提方法与Logistic回归、Fisher、RFE-SVM、HOSVM等多种方法比较，并以利润对比结果支撑核心主张，存在明确参照点。因此两个模块均通过，strict_include=true。
- 置信度：0.93

### RFID-enabled flexible warehousing 

- 年份/期刊：2017 / Decision Support Systems
- DOI：10.1016/j.dss.2017.05.002
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：行程成本（trip cost）；提前期/单程需求交付时间（lead time）
- Benchmark 状态：benchmark_comparison_central
- 参照点：刚性仓库系统/单一配送中心（rigid warehousing case / one fixed distribution center）；静态容量/固定位置配置（static control）与动态容量/位置控制（dynamic control）
- Benchmark 表述引文：Section 4.1: “We now consider benchmarking and performance comparison between the flexible system and the rigid system.”；同一节：“We extend the above simulation (Figure 7) to four different flexible location setups, all benchmarked by the same one rigid system.”；Figure 9 说明：“Figure 9 reports the performance benchmarks on these four setups with location choices.”
- Benchmark 评价：在自行生成的多组仓库布局（5、10、15、20个随机筒仓位置）上，将所提出的柔性仓储系统与同一刚性系统（单一配送中心/固定位置检索返还）进行 benchmarking 比较；报告并绘制的指标是行程成本降低百分比，并进一步比较静态容量约束与动态控制等配置的性能差异。
- 判定理由：客观指标：核心结果指标是行程成本（trip cost）等运营成本/提前期，来自模拟优化模型和成本函数，不依赖主观体验或语义评价，所有核心成功结果均为客观性能。唯一核心目标：研究问题、设计目标、评价结构和贡献声明都围绕成本/提前期这一客观性能提升展开；文中的柔性机制和知识型系统是实现该目标的手段，不是并列的核心贡献，且无主观核心结果。Benchmark：正文在数值分析部分明确使用 benchmarking/benchmark 表述，将多个柔性布局配置与同一刚性系统/单一配送中心比较，并用表格/图形报告成本降低百分比；该 benchmark 比较是支撑核心改进主张的关键证据，且存在明确参照点。因此 strict_include=true。
- 置信度：0.9

### The Structured Process Modeling Method (SPMM) what is the best way for me to construct a process model? 

- 年份/期刊：2017 / Decision Support Systems
- DOI：10.1016/j.dss.2017.02.004
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：建模时间（modeling time）；建模努力（modeling effort）；模型质量错误（syntactic/semantic errors）
- Benchmark 状态：benchmark_comparison_central
- 参照点：每个参与者自身的基准建模任务（前测） vs 实验建模任务（后测）；处理组 vs 对照组
- Benchmark 表述引文：Section 4.1 Tasks: “tasks were used to set a benchmark for every participant in order to be able to compare the modeling results before and after the treatment.”（随后称该任务为 benchmark modeling task）。
- Benchmark 评价：在实验第二部分，每位参与者先完成一个基准建模任务（defaulter handling case），作为处理前基线；第三部分完成实验建模任务（mortgage request process），并将两者结果进行比较；处理组和对照组之间的比较也以该基准为参照。4.5.1用基准案例与实验案例对比评估处理采纳（fitting technique增加、misfitting减少），4.5.2指出基准案例得到与实验案例类似的结果。
- 判定理由：客观指标方面：核心目标是降低建模认知错误、提高建模效率（时间和努力）与有效性（错误数），均以工具日志和固定编码规则测量，不依赖主观质量偏好；用户感知仅作为初步补充，未进入核心成功主张。核心目标唯一性方面：研究问题、设计目标、评价和贡献声明均围绕客观建模改进展开，没有并列的理论、制度或政策贡献。Benchmark方面：在实验任务部分作者明确使用“benchmark”一词为每位参与者设置前测基线任务，并将基准案例与实验案例、处理组与对照组进行比较；该基准比较用于支撑处理采纳和处理效应的核心改进主张。因此两个模块均通过。
- 置信度：0.62

### The seaport service rate prediction system: Using drayage truck trajectory data to predict seaport service rates 

- 年份/期刊：2017 / Decision Support Systems
- DOI：10.1016/j.dss.2016.11.008
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：港口服务时长（service rate），即集卡在港区完成提箱/卸箱作业的停留时长
- Benchmark 状态：benchmark_comparison_central
- 参照点：普通线性模型基准（LM0-LM5），与GBM使用相同目标和预测变量对；不含惯性项的模型（LM0/GBM0）作为检查惯性效应增益的参照
- Benchmark 表述引文：第4.2节分析中明确写道：“the generalized linear models ... are used as benchmarks for assessing the performance of the gradient boosting model”；第5.3节结果中写道：“in general, the gradient boosting models performed better than the benchmark normal linear models.”
- Benchmark 评价：在Port of Rotterdam三个匿名码头（CTA、CTE、CTH）和两种数据更新率（15分钟、7.5分钟）上，构建六种梯度提升模型（GBM0-5）与六种普通线性基准模型（LM0-5），在相同目标和预测变量对下以RMSE比较。GBM在多数设置下RMSE低于LM，例如CTA 15分钟数据测试集GBM5=10.51 vs LM5=11.16，CTH 7.5分钟测试集GBM5=17.26 vs LM5=18.77，支撑“梯度提升模型提供更好预测”的核心主张。
- 判定理由：客观指标方面：核心指标是基于GPS轨迹计算的港口服务时长（分钟）和预测RMSE，均为物理事实/可审计技术指标，不涉及主观评价。唯一核心目标方面：研究的目标、模型构建、评价和贡献声明都围绕提升服务时长预测精度，未发现并列的理论、主观或非客观核心贡献。Benchmark方面：作者在第4.2节明确将线性模型作为基准（benchmarks），在第5.3节报告GBM与线性基准的比较并得出GBM预测更优，benchmark评价直接支撑核心改进主张，且具有明确参照点。因此满足全部纳入条件，strict_include=true。
- 置信度：0.95

### The value of vehicle telematics data in insurance risk selection processes 

- 年份/期刊：2017 / Decision Support Systems
- DOI：10.1016/j.dss.2017.04.009
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：客户出险索赔预测性能（AUC）
- Benchmark 状态：benchmark_comparison_central
- 参照点：仅含传统变量的Logistic回归基准模型（AUC 0.5777）；仅含标准Telematics变量的模型（AUC 0.5949）；组合模型（AUC 0.6083 / 0.6174）；组合+专家变量模型（AUC 0.6135 / 0.6176）；不同数据挖掘技术之间的横向比较
- Benchmark 表述引文：结果部分：'The final random forests model, which includes traditional variables, standard and expert-based telematics variables, improves the benchmark logistic regression model with only 1.97 percentage points.'；方法部分另有'benchmark study of Lessmann et al.'，但后者不属于本文方案的评价基准。
- Benchmark 评价：在保险公司专有数据集上，以10折交叉验证AUC为评价准则，系统比较Logistic回归、随机森林、人工神经网络三类模型在四组变量（传统变量、标准telematics、组合、组合+专家变量）上的预测性能；基准为仅含传统变量的Logistic回归模型，AUC=0.5777，最终全变量模型达到AUC=0.6135（Logistic回归）和0.6176（人工神经网络）。
- 判定理由：客观指标方面，核心结果为“2015年是否至少发生一次索赔”这一事实标签上的AUC预测性能，完全客观可审计；唯一核心目标是评估telematics数据对车险风险选择预测模型的提升，全文没有主观量表、满意度或理论机制作为并列成功标准。benchmark方面，虽然没有公开命名数据集，但作者在结果部分明确使用“benchmark logistic regression model”作为基准，并通过Table 3的系统化AUC对比证明核心的客观指标提升，符合陈述式benchmark评价门槛。因此两个模块均通过，严格纳入。
- 置信度：0.9

### Utopia in the solution of the Bucket Order Problem 

- 年份/期刊：2017 / Decision Support Systems
- DOI：10.1016/j.dss.2017.03.006
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：聚合距离（accuracy）；CPU时间；可靠性（方差/标准差）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：PrefLib (preference library) 中的50个真实世界排名数据集，包括ED-00006-Skate Data、ED-00011-Web Search、ED-00014-Sushi Data、ED-00015-Clean等
- 参照点：原始BPA算法；utopia值 (u_C) 作为超优参照；anti-utopia值 (a_C) 作为劣界参照；各变体之间的相互比较
- Benchmark 表述引文：Section 6实验开头：'As a benchmark we use 50 real-world datasets of rankings available at PrefLib[39].' 明确使用PrefLib作为基准数据集库。
- Benchmark 评价：在PrefLib的50个数据集上，对BPA、LIA_G、LIA_L及其MP/MP2多pivot变体共9种算法进行了对比实验，报告了D(C,B)距离（accuracy）、与utopia值和BPA的比值、CPU时间和标准差。主要结果：LIA_G^MP2平均比原始BPA改善17%（ratio 0.829 vs 1），且通过Friedman检验和Holm事后检验验证显著性。
- 判定理由：核心目标是改进BPA算法在OBOP上的精度（D(C,B)距离）和可靠性（方差），均为完全客观、可直接测量的数值指标，全文无任何主观量表、用户评审或语义判断作为成功标准。决策规则属于基于实验结果的次要应用，未构成并列核心贡献。实验在明确命名的PrefLib基准数据集（50个真实世界排名数据集）上进行，通过与原BPA及多个变体的比较证明改进效果，benchmark评价直接支撑了核心改进主张。因此同时满足客观指标、唯一核心目标和明确benchmark门槛。
- 置信度：0.95

### A decision maxim for efficient task realization within analytical network infrastructures 

- 年份/期刊：2018 / Decision Support Systems
- DOI：10.1016/j.dss.2018.06.005
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：总处理成本（Total processing costs）；总流量强度（Total traffic intensity）；等待任务总数（Total number of waiting jobs）；等待总时间（Total time of waiting jobs）；按时实现的任务数（Total job realization with time）
- Benchmark 状态：benchmark_comparison_central
- 参照点：Workshop-based transfers；No-transfers-at-all
- Benchmark 表述引文：摘要：'A simulation benchmarks this system with existing strategies and identifies the new decision maxim as superior in a first scenario-based simulation.'；第5节：'As the NDM is displayed alongside further strategies, a benchmark can be created in order to compare the approaches.'
- Benchmark 评价：在一个4系统场景中，模拟比较了3种转移策略（new-decision-maxim、workshop-based、no-transfers-at-all）与12种处理策略；表4汇总各转移策略性能，表5按综合目标函数排序所有36种组合；结果显示NDM在所有组合中在按时实现任务数等指标上优于其他策略。
- 判定理由：客观指标方面，文中所有核心评价指标均为模拟产生的处理成本、流量强度、等待时间/任务数、按时完成数，不依赖人类主观评价，且性能评估框架服务于客观效率比较；唯一核心目标是设计并验证更高效的任务实现决策准则，未发现并列核心目标。基准方面，摘要明确使用'benchmark'动词陈述模拟对比，第5节构建基准，并在表4/5中与workshop-based和no-transfers-at-all明确比较，结果支撑NDM的核心改进主张，满足明确基准表述并处于评价语境。因此两个模块均通过。
- 置信度：0.85

### A synthetic informative minority over-sampling (SIMO) algorithm leveraging support vector machine to enhance learning from imbalanced datasets 

- 年份/期刊：2018 / Decision Support Systems
- DOI：10.1016/j.dss.2017.11.006
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：G mean（几何平均）；AUC（ROC曲线下面积）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：UCI Machine Learning Repository 的15个公开benchmark不平衡数据集：Liver Disorders、Ionosphere、Pima Indians Diabetes、Breast Cancer Wisconsin Original、Iris、Yeast、Statlog Vehicle Silhouettes、Contraceptive Method Choice、BreastC20、Vowel、Ecoli、Libras12、Libras34、Glass、BreastC10
- 参照点：原始不平衡数据；Under-sampling；SMOTE；Borderline SMOTE；Safe-Level SMOTE；Cluster SMOTE；SMOTE-IPF；Cost-sensitive SVM
- Benchmark 表述引文：摘要中明确表述：‘We applied these algorithms to the 15 publicly available benchmark imbalanced datasets and assessed their performance in comparison with existing approaches in the area of imbalanced data learning.’；第5.2节：‘In this study, we used 15 benchmark imbalanced datasets that are publicly available in UCI Machine Learning Repository’。
- Benchmark 评价：在15个UCI benchmark数据集上，将SIMO和W-SIMO与under-sampling、SMOTE、borSMOTE、safe-level SMOTE、cluster SMOTE、SMOTE-IPF、cost-sensitive SVM以及原始数据比较；使用线性SVM、RBF SVM、逻辑回归和决策树，进行4折交叉验证重复10次，报告G mean和AUC。结果显示线性SVM下SIMO/W-SIMO在所有数据集上排名前两位，整体排名1.1和1.9，优于其他方法。
- 判定理由：客观指标方面：核心成功指标为G mean和AUC，两者基于固定事实标签（疾病、类别等）和模型预测结果计算，完全客观，不依赖人类主观评价。唯一核心目标：全文从研究问题、设计目标、评价到贡献声明均集中在提升不平衡数据分类性能，无其他并列核心目标。Benchmark方面：明确表述使用15个UCI公开benchmark数据集作为评价场地，结果与多个现有方法及原始数据比较，benchmark结果直接支撑核心改进主张，且具有明确参照点。因此严格包含为true。
- 置信度：0.97

### Automatic feature weighting for improving financial Decision Support Systems 【全文无benchmark字样-需人工复核】

- 年份/期刊：2018 / Decision Support Systems
- DOI：10.1016/j.dss.2018.01.005
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：AUC（Area under the ROC Curve，ROC曲线下面积）；执行时间（秒）
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：UCI Machine Learning Repository 中的10个金融数据集（Bank、Bank-additional、Bank-additional-full、Bank-full、Banknote、Bankruptcy、Credit-approval、Credit-Australian、Credit-German、Default-credit）
- 参照点：C4.5；Naïve Bayes (NB)；NAC（未使用自动权重）；NAC GA；NAC NBA
- Benchmark 表述引文：文章在5.1节说“In order to evaluate the proposed methodology, different datasets belonging to the financial field were used (Table 2). They were obtained from the Machine Learning repository of the University of California at Irvine [32].” 虽未使用“benchmark”一词，但这一评价数据来源及随后5.3-5.4节的系统化对比属于明确的等价基准评价表述。
- Benchmark 评价：在所选的10个UCI金融数据集上，以AUC为指标评价了C4.5、NB、NAC及NAC分别使用DE/GA/NBA自动权重后的性能，并通过Friedman检验和Holm事后检验比较；结果显示NAC DE在6个数据集上最优，NAC NBA在3个数据集上最优，NAC GA在2个数据集上最优，且显著优于未加权的NAC、C4.5和NB。
- 判定理由：客观指标方面：核心指标是AUC和执行时间，均完全客观，且来自可核验的金融事实标签（违约、破产、银行订阅、真伪纸币）和系统计时；研究问题、方法目标、实验结果和贡献声明均唯一围绕提升NAC决策性能和降低计算成本展开，未发现并列的主观或理论核心目标。Benchmark方面：全文虽未使用“benchmark”单词，但在第5节明确以UCI ML Repository的10个金融数据集作为评价场地，并与C4.5、NB、未加权NAC及三种元启发式变体进行系统的基准对比，Friedman/Holm统计检验支撑了AUC提升的核心主张；存在明确参照点。因此满足两个模块的纳入条件。
- 置信度：0.95

### Detect potential relations by link prediction in multi-relational social networks 

- 年份/期刊：2018 / Decision Support Systems
- DOI：10.1016/j.dss.2018.09.006
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：AUC；Precision；Recall；F-measure
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：YouTube；Disease-Gene Network；Climate Network；DBLP
- 参照点：CN；JC；PA；AA；LPMR
- Benchmark 表述引文：在5.3节“Compared Methods”中，作者写道：‘These four index-based methods are commonly used in relation prediction and are also used as a benchmark method to compare the quality of the prediction results.’ 即明确将CN、JC、PA、AA作为benchmark方法，并用于比较预测质量。
- Benchmark 评价：MCLP在四个真实多关系网络（YouTube、Disease-Gene、Climate、DBLP）上，与CN、JC、PA、AA、LPMR等五个参照方法比较AUC、precision、recall和F-measure。多数组关系上MCLP取得最高或次高结果，并用配对t检验说明F-measure提升显著。该benchmark比较直接支撑‘MCLP预测质量更高’的核心主张。
- 判定理由：客观指标方面，核心成功指标是链接预测的AUC、precision、recall和F-measure，它们基于网络边的客观事实标签计算，不涉及主观评价；提升这些指标是全文唯一核心目标与贡献。Benchmark方面，文章在实验方法部分明确将CN、JC、PA、AA称为benchmark方法，并在四个真实数据集上与MCLP及LPMR比较；该benchmark比较被用作证明MCLP预测质量更高的关键证据，且有明确参照点。因此两个模块均通过，strict_include=true。
- 置信度：0.92

### Detection of online phishing email using dynamic evolving neural network based on reinforcement learning 【全文无benchmark字样-需人工复核】

- 年份/期刊：2018 / Decision Support Systems
- DOI：10.1016/j.dss.2018.01.001
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：准确率 Accuracy；真正率 TPR / 召回率 Recall；真负率 TNR；假正率 FPR / 假负率 FNR；精确率 Precision、F-Measure、AUC
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：PhishingCorpus (Nazario, 2015)；SpamAssassin (Mason, 2005)
- 参照点：PEDS 在线自适应前与自适应后的 DET 曲线和性能表；Islam and Abawajy (2013)；Almomani et al. (2013)；Khonji et al. (2012)；Gansterer and Pölz (2009)；Ramanathan et al. (2012)；Ma et al. (2009)；Toolan and Carthy (2010)；Hamid & Abawajy (2011)
- Benchmark 表述引文：摘要：'Through rigorous testing using the well-known data sets'；4.1 节：'The experiments were conducted using a dataset combination from three publicly available datasets'，并明确命名 PhishingCorpus、SpamAssassin、PhishTank；4.6 节：'Table 7 shows the outcome of the comparison of the present results with those of previous work'。
- Benchmark 评价：在公开邮件语料 PhishingCorpus（钓鱼邮件）和 SpamAssassin（正常邮件）上构造 9902 封邮件的数据集，其中 4000 封作为离线数据集，其余作为在线评估数据，评估 PEDS 在零日钓鱼邮件检测上的表现；得到 Accuracy 98.63%、TPR 99.07%、TNR 98.19%、FPR 1.81%、FNR 0.93%、AUC 99.43%，并在 Table 7 中与 Islam and Abawajy、Almomani、Khonji、Gansterer、Ramanathan、Ma、Toolan、Hamid 等已有方法比较。
- 判定理由：本文以钓鱼邮件检测为任务，使用公开邮件语料上的分类性能指标（Accuracy、TPR、TNR、FPR、FNR、AUC）作为核心成功标准；这些指标基于 phishing/ham 事实标签和系统分类结果客观计算。研究问题、系统设计和贡献声明均围绕提升检测性能展开，没有将主观体验或理论机制作为并列核心目标。评价部分明确使用 PhishingCorpus 和 SpamAssassin 公开数据集，并在 Table 7 与多个既有方法进行显式比较，benchmark 评价直接支撑核心性能提升主张。因此两个模块均通过，strict_include=true。
- 置信度：0.8

### Failure pattern-based ensembles applied to bankruptcy forecasting 

- 年份/期刊：2018 / Decision Support Systems
- DOI：10.1016/j.dss.2018.01.003
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：正确分类率（accuracy）；AUC（ROC曲线下面积）；Type-I/Type-II错误及其偏差-方差分解
- Benchmark 状态：benchmark_comparison_central
- 参照点：判别分析（DA）；逻辑回归（LR）；决策树（DT）；Cox模型；支持向量机（SVM）；前馈神经网络（FNN）；极限学习机（ELM）；Bagging集成模型；Boosting集成模型；Random subspace集成模型；Rotation forest集成模型；Hybrid ensemble-based模型；最佳单模型（ELM）
- Benchmark 表述引文：Section 4.1开头的明确表述：'The accuracy of the models that were developed using Kohonen maps, and that we call “failure pattern-based models”, was benchmarked against that of models designed using common methods [58].'
- Benchmark 评价：作者在8个法国企业样本上，将所提failure pattern-based模型与判别分析、逻辑回归、决策树、Cox模型、SVM、FNN、ELM等单模型，以及bagging、boosting、random subspace、rotation forest和多种混合集成模型进行系统对比；结果以正确率、AUC和显著性检验报告，FM模型平均正确率83.22%，显著高于其他模型2.27至3.01个百分点。
- 判定理由：该文以破产预测这一客观事实标签为对象，核心目标是提升预测准确率、AUC等完全客观指标；全文未使用满意度、感知价值等主观构念作为成功标准，也没有并列的理论、制度或行为解释核心目标。作者在方法部分明确使用benchmark表述，将所提failure pattern-based模型与多种常用单模型和集成模型进行系统对比，并在结果部分用正确率和AUC的差异及显著性证明核心提升主张，因此同时满足客观指标和明确benchmark两个门槛，strict_include为true。
- 置信度：0.96

### Long-term stock index forecasting based on text mining of regulatory disclosures 

- 年份/期刊：2018 / Decision Support Systems
- DOI：10.1016/j.dss.2018.06.008
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：预测均方根误差（RMSE）
- Benchmark 状态：benchmark_comparison_central
- 参照点：线性自回归模型（lm）；带滞后值的机器学习模型（lasso、ridge、elastic net、gradient boosting、PCR、random forest）；Diebold-Mariano检验零假设（文本模型不优于基准模型）
- Benchmark 表述引文：第5.1节实验设置：“The purpose of our experiments is to compare the predictive performance of the benchmark models to the disclosure-based forecasts.”；第7节结论：“We evaluate the forecasting errors of our text-based models against various benchmarks, including linear autogression and random forests, using lagged data as predictors.”；结果表（Table 3/4）中明确列出“Benchmark: lags”。
- Benchmark 评价：在自建的滞后数据基准（线性自回归、带滞后输入值的多种机器学习模型）上，评估不同文本模型（情感特征、tf-idf机器学习、降维等）对DAX、CDAX、STOXX Europe 600在多个预测视界上的RMSE，并使用Diebold-Mariano检验比较误差差异。结果显示，尤其在长期预测（如24个月）中，文本模型相对基准模型取得显著RMSE降低。
- 判定理由：该文核心目标为通过文本挖掘提升股指预测精度，核心结果指标RMSE及其显著性检验完全客观，且是唯一核心目标与贡献。全文在实验设置、结果表和结论中明确使用benchmark一词，将滞后数据模型作为基准，系统比较文本模型的预测误差，并以RMSE降低作为核心证据。文本模型相比明确参照点（lagged baseline）展示了提升，因此同时满足唯一客观指标改进和明确benchmark表述两个条件。
- 置信度：0.97

### Predicting tax avoidance by means of social network analytics 

- 年份/期刊：2018 / Decision Support Systems
- DOI：10.1016/j.dss.2018.02.001
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：AUC（ROC曲线下面积）；Accuracy/Sensitivity/Specificity
- Benchmark 状态：benchmark_comparison_central
- 参照点：local model（仅公司特征，作者明确称为benchmark）；network unipartite model；hybrid unipartite model
- Benchmark 表述引文：Section 3.1: 'The first model is a local model using only firm characteristics. This model can be regarded as the current state and as a benchmark against which we can compare the other models.'；结果部分在out-of-time 2013/2014测试集上与local模型比较。
- Benchmark 评价：以仅含公司特征的local模型为benchmark基线，在2013和2014两个年度外样本上评价logistic回归、决策树和随机森林下的五种模型；核心结果是混合二部网络随机森林AUC达0.8431/0.8306，较local模型0.7683/0.7489提高约7个百分点，且经DeLong检验显著。
- 判定理由：客观指标：目标为预测低税企业（低税状态由三年现金ETR行业调整后最低五分位确定），评价指标AUC/accuracy/sensitivity等均来自可审计会计事实和分类混淆矩阵；唯一核心目标是提高预测性能并比较网络特征带来的提升。benchmark：作者在方法部分明确将仅公司特征的local模型作为当前状态和基准，并在out-of-time测试集上系统比较五种模型；结果表、ROC/显著性检验以基准对比为核心证据。因此 strict_include=true。
- 置信度：0.9

### Time-aware cloud service recommendation using similarity-enhanced collaborative filtering and ARIMA model 【全文无benchmark字样-需人工复核】

- 年份/期刊：2018 / Decision Support Systems
- DOI：10.1016/j.dss.2017.12.012
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：MAE（平均绝对误差）；RMSE（均方根误差）；NDCG（归一化折损累计增益）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：WS-DREAM
- 参照点：UPCC；IPCC；WSRec；AVG；Kalman approach [17]
- Benchmark 表述引文：Section 6.1 Data description 中写道：“We adopted the open QoS dataset from WS-DREAM [12], which is the most representative dataset and has been widely adopted in QoS studies [35][36][37][38][39].” 该表述明确将WS-DREAM作为评价场地，并作为核心证据比较所提方法与多种baseline。
- Benchmark 评价：在WS-DREAM公开数据集上，作者抽取120*500*64的响应时间和吞吐量矩阵，模拟不同矩阵密度，将taSR与UPCC、IPCC、WSRec、AVG以及Kalman方法在MAE、RMSE和NDCG@10/30/50上进行比较，结果显示taSR在多数设置下获得更好性能。
- 判定理由：客观指标方面：核心成功指标MAE、RMSE和NDCG均基于外部可核验的QoS测量值，不依赖人类体验或语义评价，属于完全客观指标。唯一核心目标方面：全文研究问题、方法设计、实验评价和贡献声明均围绕提升QoS预测准确性和推荐排序性能，没有与客观指标提升并列的主观结果、理论贡献或政策建议。Benchmark方面：文章虽未使用“benchmark”字样，但在实验部分明确命名公开领域标准数据集WS-DREAM作为评价场地，并在该数据集上与多个明确baseline（UPCC、IPCC、WSRec、AVG、Kalman）比较MAE/RMSE/NDCG，benchmark评价直接支撑核心性能提升主张，满足命名式benchmark表述的等价要求。因此两个模块均通过，strict_include为true。
- 置信度：0.88

### A multi-objective approach for profit-driven feature selection in credit scoring 

- 年份/期刊：2019 / Decision Support Systems
- DOI：10.1016/j.dss.2019.03.011
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：期望最大利润（EMP）；选用特征数量
- Benchmark 状态：benchmark_comparison_central
- 参照点：SFS；SBS；LASSO；单目标GA；单目标PSO；全特征评分卡（full model）
- Benchmark 表述引文：实验设置部分明确写道：'We also use a scorecard that relies on a full set of features as a benchmark. All five single-objective benchmarks use the EMP measure as a fitness function.'；图1中也将对比的外部解法称为'benchmarks'。
- Benchmark 评价：在十个信用评分数据集上，将NSGA-II生成的Pareto前沿与SFS、SBS、LASSO、单目标GA、单目标PSO及全特征评分卡进行系统比较，报告EMP和特征数量，并用S1/S2/S3非支配指标汇总相对基准的表现。
- 判定理由：客观指标方面，核心结果为EMP和特征数量：EMP由固定财务公式、违约标签和成本参数决定，特征数量为确定性计数，二者均不依赖人的感知、偏好或语义评价；全文以最大化利润和最小化特征数量作为唯一核心设计目标，经验证据和贡献声明都围绕这一目标。Benchmark方面，作者在实验设置中明确将SFS、SBS、LASSO、单目标GA、单目标PSO及全特征评分卡称为benchmark或基准，在十个数据集上通过EMP和特征数量比较验证核心提升主张，并设置了明确参照点。因此两个模块均通过。
- 置信度：0.93

### AKEGIS: automatic keyword generation for sponsored search advertising in online retailing 

- 年份/期刊：2019 / Decision Support Systems
- DOI：10.1016/j.dss.2019.02.001
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：广告关键词数量；每次点击成本 (CPC)；转化率 (Conversion Rate)；每关键词印象数
- Benchmark 状态：benchmark_comparison_central
- 参照点：manual experts (state-of-the-art approach)；未实施AKEGIS的商店B（对照组）
- Benchmark 表述引文：在6.3节（局限性与未来方向）中，作者写道：'This benchmark approach is the state-of-the-art approach successfully used for more than 100 online stores of the company with whom we cooperated in our empirical investigation.' 此处明确将人工专家方法称为benchmark approach，并说明该基准是实证评价中的对照方法。
- Benchmark 评价：在两个大规模在线商店（商店A与商店B）上进行现场DiD评价。商店A实施AKEGIS，商店B保持原有由人工专家（manual experts/state-of-the-art approach）管理的关键词生成方法作为对照。结果比较了关键词数量、每关键词印象数、每次点击成本和转化率四个客观指标，AKEGIS相对于人工基准显著提升了关键词数量、降低了CPC并提升了转化率。
- 判定理由：文章所有核心成功指标均为客观可测量的业务指标（关键词数、CPC、转化率、印象数），不包含主观量表或人类语义判断。论文的最终设计目标和核心贡献是AKEGIS对这些客观指标的提升，消费者搜索行为理论仅作为设计基础并非并列核心目标。在benchmark方面，虽然只有一个明确出现“benchmark”的表述，但它出现在讨论部分，明确指称人工专家方法为基准方法（state-of-the-art approach），且该基准比较正是支撑核心绩效提升主张的关键证据；对照对象明确（manual experts、对照组商店B），结果报告了相对提升而非孤立数值。因此两个门槛均通过，strict_include=true。
- 置信度：0.82

### Automobile insurance classification ratemaking based on telematics driving data 

- 年份/期刊：2019 / Decision Support Systems
- DOI：10.1016/j.dss.2019.113156
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：风险概率预测 AUC；索赔频率预测 RMSE
- Benchmark 状态：benchmark_comparison_central
- 参照点：逻辑回归（logistic regression）；传统定价变量集；原始变量形式
- Benchmark 表述引文：4.2节：'Logistic regression, currently the most widely used model in insurance practice, is used as the benchmark model for probability prediction'；5.2节：'we set the model that uses traditional variables only/original variables as benchmark model'。
- Benchmark 评价：在自有的2065辆投保车辆数据上，系统比较了五种风险概率模型（LR、SVM、RF、XGBoost、NN）和三类变量集（传统、驾驶行为、全部变量）及原始/分箱形式，以AUC为主要基准指标；对索赔频率模型以RMSE进行比较（表5、表8）。
- 判定理由：客观指标方面，核心结果指标为基于实际事故/索赔事实的AUC和RMSE，均客观可审计；核心目标为提升预测精度，强调的可解释性未作为结果测量，不构成并列核心目标。Benchmark方面，全文在方法/结果部分明确使用benchmark model表述，以逻辑回归和传统变量/原始变量为对照，在自有数据集上系统比较不同模型、变量和分箱形式，并以AUC/RMSE比较结果支撑核心提升主张。因此两个模块均通过，strict_include为true。
- 置信度：0.78

### Deep learning based personalized recommendation with multi-view information integration 

- 年份/期刊：2019 / Decision Support Systems
- DOI：10.1016/j.dss.2019.01.003
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：AUC；Hit Ratio@K
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：Amazon.com Women's Dresses；Amazon.com Baby Clothes
- 参照点：BPRMF；CDL；VBPR；CKE；Image-MINE；Description-MINE；Review-MINE；No cognitive styles；Uniform cognitive styles；Ordered cognitive styles；Random cognitive styles；Average cognitive styles
- Benchmark 表述引文：4.3.4节：'we proposed a series of initial cognitive indexes as benchmark indexes and compared their recommendation performances with the Deep-MINE model'；4.1节明确以Amazon.com的Women's Dresses和Baby Clothes公开数据集作为评价场地，并在4.3.1与BPRMF/CDL/VBPR/CKE进行AUC/Hit Ratio对比。
- Benchmark 评价：Deep-MINE在Amazon Women's Dresses和Baby Clothes两个公开数据集上评价产品排序推荐，主要指标为AUC和Hit Ratio；与BPRMF、CDL、VBPR、CKE基线比较，并进一步在冷启动、单视图/多视图、认知风格配置等条件下比较。4.3.4将无认知风格、统一认知风格、有序认知风格、随机认知风格、平均认知风格作为benchmark indexes与Deep-MINE比较，结果用于支持认知风格个性化提升推荐准确率的模型主张。
- 判定理由：核心评价指标AUC和Hit Ratio均来自可审计的购买反馈与推荐排序，完全客观；研究问题、模型设计、实验评价和贡献声明均围绕推荐排序准确率提升，未将主观体验、理论机制或政策建议作为并列核心贡献；全文存在明确benchmark表述（4.3.4的benchmark indexes）并在Amazon公开数据集上与多个基线比较，benchmark结果支撑核心客观指标提升，因此strict_include为true。
- 置信度：0.78

### Family profile mining in retailing 

- 年份/期刊：2019 / Decision Support Systems
- DOI：10.1016/j.dss.2019.01.007
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：目标家庭画像标签预测召回率（recall rate）；产品推荐预测误差与覆盖率（MAE / RMSE / coverage）
- Benchmark 状态：benchmark_comparison_central
- 参照点：AFRN (All Features + Random Negative)；AFBN (All Features + Bottom Negative)；RFBN (Random Feature + Bottom Negative)；随机预测的recall lift；推荐实验中的全局邻居选择（Global neighbor selection）
- Benchmark 表述引文：Section 4.3 Model comparison："We defined four other family profiling algorithms as benchmarks for comparison."
- Benchmark 评价：在自有的大型超市交易数据（50,000名会员）上，将提出的DFBN算法与AFRN、AFBN、RFBN三个对比算法在infant、child、elder、car四个画像上比较平均召回率；结果显示DFBN在平均召回率上分别提升17.18%、11.34%和21.86%。推荐实验部分又将全局邻居选择作为比较基准，报告MAE、RMSE和覆盖率的改进。
- 判定理由：客观指标方面，核心指标为家庭画像预测召回率和推荐MAE/RMSE/coverage，均是基于交易数据固定规则计算的外部事实性指标，无主观量表或语义评价。核心目标方面，研究问题、设计目标、评价结构和贡献声明均围绕算法在客观指标上的提升，未并列理论机制或主观结果作为成功标准。benchmark方面，作者在4.3节明确将四个对比算法称为benchmarks，并在自有大型数据集上系统比较，结果显示DFBN在召回率上有明显提升，该基准评价直接支撑核心改进主张。因此两个模块均通过，strict_include=true。
- 置信度：0.78

### Feature assessment and ranking for classification with nonlinear sparse representation and approximate dependence analysis 

- 年份/期刊：2019 / Decision Support Systems
- DOI：10.1016/j.dss.2019.05.004
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：分类错误率
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：isolet5；DNA；mfeat-factors；mfeat-pixel；mfeat-zernike；optdigits；spambase；musk2；14_Tumors
- 参照点：MIM；mRMR；FOU；JMI；DFS
- Benchmark 表述引文：第7.1节数据描述中明确称14_Tumors为“a well-known microarray dataset ... as the benchmark dataset”，并将mfeat-factors、mfeat-pixel、mfeat-zernike称为“the benchmark datasets”。这些公开数据集随后成为分类实验的评价场地。
- Benchmark 评价：在9个公开数据集上，以分类错误率作为评价指标，将提出的SRDA与MIM、mRMR、FOU、JMI和DFS五种代表性特征选择方法进行比较；使用kNN、朴素贝叶斯和随机森林三种分类器，比较top 20/40特征下的错误率，并采用20×5折交叉验证和Wilcoxon检验。结果显示SRDA在多数数据集上错误率更低。
- 判定理由：本文以降低分类错误率为唯一核心目标与核心贡献，评价完全基于客观可测的分类错误率，无主观量表或人类语义质量评价作为核心成功标准。实验部分明确以公开数据集（含称为benchmark dataset的14_Tumors和mfeat数据集）作为评价场地，并与MIM、mRMR、FOU、JMI、DFS等明确参照点比较，分类错误率的下降直接支撑核心改进主张。因此两个模块均通过，strict_include为true。
- 置信度：0.96

### Feature construction for fraudulent credit card cash-out detection 

- 年份/期刊：2019 / Decision Support Systems
- DOI：10.1016/j.dss.2019.113155
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：Top 5%/10%/15%/20% 精确率（Precision）；准确率、精确率、召回率、F1（平衡数据集）
- Benchmark 状态：benchmark_comparison_central
- 参照点：feature set 5（基于Whitrow聚合策略的基准特征集）；既往研究粗略性能：Dal Pozzolo et al. [41]、Nami & Shajari [23]、Bhattacharyya et al. [29]
- Benchmark 表述引文：摘要和第4节：作者明确说明“we also construct a benchmark feature set based on the traditional approach of Whitrow's strategy”，并在实验中反复以 feature set 5 为基准比较提出特征集的精确率；如“Compared with the benchmark feature set 5”. 位置包括Abstract、Section 4、Section 5.2和5.3。
- Benchmark 评价：在真实信用卡交易数据集（25,000张卡、1,067,010笔交易）上，用Xgboost、随机森林、SVM评估特征集1-4、FDA特征及其组合；核心比较对象是基于Whitrow聚合策略构造的benchmark feature set 5。结果给出相对feature set 5的top 5%-20%精确率提升，并在平衡数据集中与既往研究性能做粗略比较。
- 判定理由：文章的核心目标是构造并验证用于欺诈性信用卡套现检测的特征集，核心成功指标为精确率、召回、准确率和F1等客观预测性能；欺诈标签由发卡机构基于风控算法和运营确认的外部事实确定，不涉及主观评价。全文明确以基于Whitrow策略的feature set 5作为benchmark，并以其为参照报告各项提出特征集的性能改进，benchmark评价直接支撑核心提升主张。因此客观指标、唯一核心目标和benchmark三个门槛均通过。
- 置信度：0.88

### Financial news-based stock movement prediction using causality analysis of influence in the Korean stock market 

- 年份/期刊：2019 / Decision Support Systems
- DOI：10.1016/j.dss.2018.11.004
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：股票涨跌方向预测准确率（Accuracy）和 F1-score
- Benchmark 状态：benchmark_comparison_central
- 参照点：Oh et al. [33]（单向因果检测）；Výrost et al. [29]（Granger causality）
- Benchmark 表述引文：Section 4.2：'To test our causality detection is valid, we benchmark with two state-of-the-art causality detection papers [29, 33]... Results show that the proposed method shows better results than two state-of-the-art methods.'
- Benchmark 评价：在 Pharmacy 板块上，除因果检测方法不同外，文本预处理、MKL、网格搜索等流程均相同，比较 Proposed Method 与 Oh et al. [33]（只考虑单向因果）和 Výrost et al. [29]（Granger causality）的股票涨跌预测精度。Table 11 显示 Proposed Method 平均准确率 0.584381，高于 Oh et al. 的 0.564935 和 Výrost et al. 的 0.573040。
- 判定理由：核心指标是股票涨跌方向预测的 Accuracy 和 F1-score，其标签来自股价收益，是可审计的客观事实；全文唯一核心目标是提升该预测性能，不存在主观指标或并列核心目标。存在明确的 benchmark 表述（Section 4.2 'we benchmark with two state-of-the-art causality detection papers'），处于评价语境，并有明确比较对象（Oh et al. 和 Výrost et al.），结果用于支持本方法在预测性能上的提升。因此 strict_include=true。
- 置信度：0.86

### Improving accuracy and lowering cost in crowdsourcing through an unsupervised expertise estimation approach 

- 年份/期刊：2019 / Decision Support Systems
- DOI：10.1016/j.dss.2019.05.005
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：准确率（accuracy）；AUC；成本/预算浪费（cost/wastage）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：SQUARE-RTE；SQUARE-TEMP；SQUARE-Duchenne；Google；TREC
- 参照点：ELICE；Gaussian expertise estimation；Raykar；GLAD
- Benchmark 表述引文：Section 4.1 写道“The five real-world benchmark datasets are presented in Table 2”；Section 5 写道“ROUX was compared with these approaches in five benchmark datasets.”
- Benchmark 评价：在 RTE、TEMP、Duchenne、Google、TREC 五个真实世界 benchmark 数据集上评价 ROUX，并与 ELICE、Gaussian、Raykar、GLAD 四种主流/state-of-the-art 方法比较；报告准确率、AUC 和成本浪费，并附 Wilcoxon 检验。
- 判定理由：客观指标：核心成功指标是准确率、AUC、成本浪费，均可由 ground truth、budget 和确定性公式计算，不涉及主观评价。唯一核心目标：摘要、引言和实验一致表明设计目标是提升聚合准确率并降低成本；结论中列出的方法特性是支撑该目标的设计机制。Benchmark：实验在五个被明确称为 benchmark 的真实世界数据集上展开，与四种 state-of-the-art 方法比较并使用统计检验，证明核心客观指标提升。因此两个模块均通过，strict_include=true。
- 置信度：0.9

### Recommendation with diversity: An adaptive trust-aware model 【全文无benchmark字样-需人工复核】

- 年份/期刊：2019 / Decision Support Systems
- DOI：10.1016/j.dss.2019.113073
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：推荐精度 Precision (P)；个体多样性 Di；聚合多样性 Da；新颖性 Dn
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：Ciao；Epinions；Yelp
- 参照点：BD；Eh_HHPH；SP；PLUS；COUSIN；COSRA+T；TrAdBi1/TrAdBi2 的参数调整对照
- Benchmark 表述引文：第4.1节明确列出实验数据集为 Ciao、Epinions 和 Yelp，并说明来源；第5.2节明确写道“we compare our algorithm with other algorithms presented in Section 4.4 with four metrics”，即以这些数据集为评价场地、以多个既有算法为参照。文中虽未使用“benchmark”一词，但命名了公开领域数据集，并将结果表（Tables 3-5）作为核心证据。
- Benchmark 评价：在 Ciao、Epinions、Yelp 三个公开数据集上评价所提 TrAdBi 模型及其参数调整版本 TrAdBi1/TrAdBi2，与 BD、Eh_HHPH、SP、PLUS、COUSIN、COSRA+T 等基线比较，报告 Precision、Di、Da、Dn；同时单独报告冷启动用户和长尾物品精度（Fig.7）及经验丰富用户多样性（Fig.8）。
- 判定理由：客观指标方面：全文核心成功指标是 Precision、个体多样性、聚合多样性和新颖性，均可从用户-物品交互数据中确定性计算，不依赖用户满意度、感知质量或语义评价；研究问题、算法设计、实验结果和结论均围绕这些客观指标提升。唯一核心目标方面：目标是构建自适应信任感知推荐模型以同时提升精度和多样性，所有贡献声明均围绕客观指标改进，不存在并列的理论机制、组织变革或主观体验核心目标。Benchmark 方面：文章在 Ciao、Epinions、Yelp 三个公开领域数据集上评价模型，并以 BD、Eh_HHPH、SP、PLUS、COUSIN、COSRA+T 等多个基线与既有方法作显式比较，结果表直接支撑核心精度与多样性提升主张，满足命名式 public benchmark 和显式比较条件，因此三个模块均通过，strict_include=true。
- 置信度：0.85

### Trustworthy and profit: A new value-based neighbor selection method in recommender systems under shilling attacks 

- 年份/期刊：2019 / Decision Support Systems
- DOI：10.1016/j.dss.2019.113112
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：MAE（平均绝对误差）；MSEP（平均相似性期望利润）与MTP（平均总利润）；Precision、Recall、F1
- Benchmark 状态：benchmark_comparison_central
- 参照点：PCC（传统协同过滤，无攻击防御）；Lee & Zhu (2012) shilling attack detection (SD)；HPRS（Hybrid Perspective Recommender System，利润驱动基准）；HPRS+SD（先检测后利润推荐集成基准）
- Benchmark 表述引文：Section 4.1：'We evaluated the performance of the proposed method using two benchmarks. The first is the original recommender systems without attack detection, that is, the traditional Pearson Correlation Coeficient (PCC). The second is a well-known attack detection benchmark: Lee and Zhu's shilling attack detection (SD) method.'；Section 5：'In this section, we compare VNS with the profit-based benchmark method, HPRS.'
- Benchmark 评价：在一个Book-Crossing数据子集上，模拟Random、Average、Bandwagon(AFM/RFM)以及混合攻击，用PCC、SD和HPRS(+SD)作为基准，比较VNS在MAE、MSEP、MTP、Precision、Recall和F1上的表现。结果显示VNS在绝大多数攻击场景下MAE更低、MSEP更高，且在准确度指标上显著优于HPRS+SD，MTP优于PCC和SD而低于HPRS+SD，被解释为更好的准确度-利润平衡。
- 判定理由：完全客观指标：核心成功指标为MAE、MSEP、MTP、Precision、Recall、F1，均由评分、价格/成本和推荐列表直接计算，不依赖人类主观评价或语义判断。唯一核心目标：研究问题、方法目标函数、实验评价和贡献声明均围绕在shilling攻击下同时提升/保持准确度和电商利润，不存在并列的理论、制度或主观体验目标。Benchmark：全文明确使用'benchmark'一词，且在实验评价部分将PCC、SD、HPRS(+SD)作为基准方法进行比较，比较结果直接用于支持核心改进主张，具有明确参照点。故满足全部纳入标准。
- 置信度：0.95

### Twitter user geolocation using web country noun searches 

- 年份/期刊：2019 / Decision Support Systems
- DOI：10.1016/i.dss.2019.03.006
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：全局准确率 (Acc)；加权F1分数 (WF1)
- Benchmark 状态：benchmark_comparison_central
- 参照点：BM: 基于Stanford CoreNLP NER + Google Maps + RF的地理定位基准方法；BM2: BM的混合变体，歧义情况用GTN估计；GTN2: GTN的机器学习近似（对照GTN本身）
- Benchmark 表述引文：Section 3.4标题'Benchmark methods'：'For comparison purposes, we selected a recent WD geolocation benchmark method (BM) [15]...'；Section 3.3：'to obtain the benchmark geolocation method outputs (for comparison purposes with GTN)'。
- Benchmark 评价：在同一新建数据集上以10折交叉验证比较GTN与NER基准方法BM（以及混合方法BM2），核心结果Table 5：GTN Acc=80.6/WF1=81.3 vs BM 64.9/72.8 vs BM2 78.3/79.5；误差调整后Table 8：GTN 83.0/83.4。
- 判定理由：该文核心目标是用GTN方法提升Twitter用户国家地理定位的分类准确性（Acc和WF1），这些指标基于外部可核验的国家事实标签，完全客观且无主观量表；全文没有并列的其他核心目标（GTN2速度优化为客观效率补充）。benchmark层面：作者在Section 3.3/3.4明确将现有WD方法BM称为benchmark method，并在10折交叉验证中与GTN系统比较，核心结果在Table 5/8中显示GTN准确率显著优于BM，benchmark评价直接支撑核心提升主张，且有明确比较对象。因此同时满足两个模块。
- 置信度：0.92

### Twitter user geolocation using web country noun searches 

- 年份/期刊：2019 / Decision Support Systems
- DOI：10.1016/j.dss.2019.03.006
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：国家地理定位准确率（Acc）和加权F1（WF1）；GTN2匹配GTN响应的准确率与计算速度
- Benchmark 状态：benchmark_comparison_central
- 参照点：BM（Lee et al. [15] 的WD/NER方法）；BM2（混合NER+GTN方法）；GTN（本文提出方法）；GTN2的机器学习基线与GTN oracle
- Benchmark 表述引文：Section 3.4标题为‘Benchmark methods’，正文明确写道：‘For comparison purposes, we selected a recent WD geolocation benchmark method (BM) [15]...’；Section 3.3亦说明机器学习目标之一是‘to obtain the benchmark geolocation method outputs (for comparison purposes with GTN)’。这些表述处于方法/评价设计语境，而非泛泛提及。
- Benchmark 评价：在自建的多语言Twitter国家地理定位数据集上，通过10折交叉验证将GTN与benchmark方法BM（state-of-the-art NER/机器学习方法[15]）和混合基准BM2进行比较，报告Acc与WF1（Table 5、Table 8）；GTN显著优于BM，并在调整ground truth后显著优于BM和BM2。GTN2则与GTN及多种机器学习基线（BG/RF/SVM/MLP）比较，评估其匹配GTN响应的能力（Table 12）。
- 判定理由：客观指标方面，文章核心是Twitter用户国家地理定位的预测性能（Acc、WF1）与GTN2的匹配准确率/速度，这些均基于外部可核验的国家标签，不含主观满意度、偏好或语义质量评价；核心目标与贡献唯一且围绕客观性能提升。benchmark方面，作者在方法-评价语境明确使用‘benchmark method’表述（Section 3.4），并通过Table 5/8/12的对比支持核心改进主张，存在明确参照点（BM、BM2、GTN oracle）。因此两个模块均通过，strict_include=true。
- 置信度：0.9

### Two-stage consumer credit risk modelling using heterogeneous ensemble learning 

- 年份/期刊：2019 / Decision Support Systems
- DOI：10.1016/j.dss.2019.01.002
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：PD预测性能：Accuracy、AUC、误分类成本MC；EAD/EL预测性能：R²、RMSE、MAE；贷款组合实际利润/相对利润
- Benchmark 状态：benchmark_comparison_central
- 参照点：RF；SMOTEBagging + RF；single classifiers（Forest PA、CDT、Hoeffding DT、C4.5、LogR、Bayes Network、SVM、DNN）；homogeneous ensembles（MultiBoostAB、AdaBoostM1、LogitBoost、Rotation Forest、Decorate、Bagging、Random Subspace）；heterogeneous ensembles（Voting、Stacking）；state-of-the-art单阶段EL模型（M5P、LR、SVR、NN、FDF、Stacking）；state-of-the-art两阶段EL模型（LR+SVR、LR+NN、LogR+SVR、LogR+NN、SVM+SVR、RF+NN）
- Benchmark 表述引文：第5节实验部分明确使用benchmark一词并置于评价语境：'SMO-TEBagging oversampling was employed as a benchmark [41]'、'For comparative purposes... we used RF as the benchmark classifier [7]'；第5节表8以'Prediction performance of the proposed two-stage EL model compared with state-of-the-art credit risk models'为核心比较。
- Benchmark 评价：在Lending Club公开P2P数据和捷克非银行金融机构数据两个真实数据集上，用10次重复5折交叉验证评价所提两阶段模型；将PD模型与多种single/homogeneous/heterogeneous集成方法比较，将EAD模型与回归方法比较，并将整体EL模型与state-of-the-art单阶段和两阶段信用风险模型比较；表8显示提出模型在R²、RMSE、MAE上全面优于对照方法。
- 判定理由：客观指标方面：核心成功指标为违约状态预测、EAD/EL预测误差和贷款组合利润，均来自外部可审计事实，不涉及主观构念；主观体验、用户评分或理论解释不是核心。唯一核心目标方面：文章的问题、设计、评价和贡献均集中于提升两阶段信用风险模型的客观预测和经济绩效，MC指标和MOEFS仅作为支撑组件。Benchmark方面：虽然未使用正式命名的公开benchmark套件，但作者在实验评价语境中明确使用benchmark一词设置对照（如RF benchmark classifier、SMOTEBagging benchmark），并通过表8与state-of-the-art单阶段和两阶段模型进行系统比较，作为核心提升主张的关键证据。因此严格满足纳入条件。
- 置信度：0.95

### Using similarity measures for medical event sequences to predict mortality in trauma patients 

- 年份/期刊：2019 / Decision Support Systems
- DOI：10.1016/j.dss.2018.10.008
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：死亡率预测判别性能（AUC/ROC/operating points）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：National Trauma Data Bank (NTDB)；Retrospective mortality prediction benchmarking task
- 参照点：TMPM；original OTCS；OTCS-MES EP；OTCS-MES ES
- Benchmark 表述引文：摘要：'Retrospective mortality prediction is a benchmarking task used by trauma care governance bodies to assist with policy decisions.' 实验部分第3.6节：'We used the National Trauma Data Bank for our morbidity prediction experiment.'
- Benchmark 评价：在NTDB 2015创伤数据上（50,000训练案例、2,000测试案例）系统评价TMPM、原始OTCS、OTCS-MES EP、OTCS-MES ES和集成kNN分类器的死亡率预测性能，主要比较AUC、ROC曲线和operating points。结果显示集成分类器AUC 0.8589显著优于TMPM的0.8392（p=0.0037），并在加权Youden和Neyman-Pearson标准下相对TMPM有优势。
- 判定理由：客观指标门槛通过：核心结果是创伤患者死亡这一事实标签上的预测性能，测量为AUC、ROC曲线和operating points等可审计的客观指标，全文没有主观评分或满意度作为成功标准。唯一核心目标通过：研究问题、实验设计和贡献声明一致地将“用MES相似性方法提升创伤死亡率预测性能（尤其优于TMPM）”作为唯一核心目标；其余贡献明确为次要贡献。benchmark门槛通过：文章明确将retrospective mortality prediction称为benchmarking task，并在公开数据源National Trauma Data Bank上以TMPM、原始OTCS等为明确参照进行系统比较，benchmark结果是支撑核心提升主张的关键证据。因此strict_include=true。
- 置信度：0.87

### Using social network and semantic analysis to analyze online travel forums and forecast tourism demand 

- 年份/期刊：2019 / Decision Support Systems
- DOI：10.1016/j.dss.2019.113075
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：国际机场到达人数（international airport arrivals）；预测误差（MSFE/RMSE）
- Benchmark 状态：benchmark_comparison_central
- 参照点：AR（一阶自回归朴素基准）；BRIDGE-GF（含Google Trend Flights的桥接模型）；BRIGDE-OTH-GF（含简化变量的桥接模型）
- Benchmark 表述引文：第3.2.1节：“We evaluated model (3) (FAAR) using a first-order autoregressive model as a naïve benchmark specification, where the optimal lag of length p is chosen adaptively through the BIC. … we considered also other benchmarks: a bridge model … (model named BRIDGE-GF) …”。这是明确的benchmark表述，且位于模型评价方法部分。
- Benchmark 评价：作者在7个欧洲首都城市的国际机场到达人数数据集上，以自回归模型（AR）为朴素基准，并以BRIDGE-GF等模型为额外基准，在滚动窗口外样本框架下比较FAAR和FABM-GF等模型的预测性能。结果表（Table 4）报告相对MSFE和RMSE，显示加入社交网络和语义变量的模型在大部分情况下相对基准模型有预测精度提升。
- 判定理由：文章唯一核心目标是提升国际机场到达人数这一完全客观指标的预测精度；所有自变量均来自论坛日志和公开统计数据，成功标准是预测误差（MSFE/RMSE）的降低，不存在主观构念或人类语义评价作为核心结果。模型评价部分明确使用AR作为朴素benchmark specification并列出其他benchmark模型，且该benchmark比较直接支撑核心提升主张。因此两模块均通过，strict_include为true。
- 置信度：0.94

### A decision support framework for home health care transportation with simultaneous multi-vehicle routing and staff scheduling synchronization 

- 年份/期刊：2020 / Decision Support Systems
- DOI：10.1016/j.dss.2020.113361
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：总成本（旅行成本+路线分配成本）；计算时间（秒）；最优性差距（%）；总行驶距离
- Benchmark 状态：benchmark_comparison_central
- 参照点：CPLEX/MILP最优解或最好界；Variable Neighborhood Search (VNS)；GA with SFRH (GAF)；简单GA
- Benchmark 表述引文：Section 5.2："The solutions returned from CPLEX were used as benchmarks to assess the performance of the proposed HGA"。Section 5.5："We ran CPLEX to determine the optimal solutions as benchmark"。
- Benchmark 评价：作者在实验部分以CPLEX求解MILP得到的最优解或最好界作为基准，评估HGA在随机生成实例（A-D）和香港现实实例（A-G）上的总成本、计算时间和最优性差距；还在Table 8中将HGA与VNS、GAF、GA对比。核心结果表明HGA在大规模实例上能在远短于CPLEX的时间内取得较小最优性差距，支持算法有效性和高效性的核心主张。
- 判定理由：文章核心是以最小化总成本为目标的HHC运输与排班优化决策支持模型和算法；所有核心成功指标均为客观可审计的成本、时间、距离和最优性差距，无主观或语义评价。核心目标唯一为客观绩效提升，模型/算法创新是手段而非并列结果。实验部分明确以CPLEX最优解作为benchmark，并在评价语境中比较HGA与CPLEX、VNS、GAF和GA，比较点明确，benchmark结果直接支撑算法高效性和解质量的核心主张。因此objective_metric与benchmark模块全部通过，strict_include为true。
- 置信度：0.95

### A dynamic shipment matching problem in hinterland synchromodal transportation 

- 年份/期刊：2020 / Decision Support Systems
- DOI：10.1016/j.dss.2020.113289
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：总匹配成本；计算时间
- Benchmark 状态：benchmark_comparison_central
- 参照点：greedy approach (GA) from practice；exact algorithm (CPLEX) as benchmark for heuristic accuracy；optimization interval of 1 h as benchmark in sensitivity analysis (Section 6.4.2)
- Benchmark 表述引文：第4.1节标题为 'Benchmark: greedy approach'，正文称 'This paper proposes a rolling horizon approach for the DSM problem and uses a greedy approach as the benchmark.'；第6.3节进行动态方法比较时再次写道 'We use the GA as the benchmark.'
- Benchmark 评价：在生成的欧洲腹地多式联运网络实例上，把 greedy approach 作为基准，比较 RHA 在不同需求密度、动态程度、提前期和响应时间下的总成本；结果显示 RHA 在所有场景下总成本更低。此外，启发式算法以精确算法为参照报告 %gap 和 CPU 时间。
- 判定理由：核心指标为总匹配成本和计算时间，均为确定性模型和系统运行时间中可观测的客观量，不含任何用户主观评分或语义判断；全文唯一核心目标是通过 rolling horizon 和启发式算法在动态场景下降低总成本并保证计算效率。Benchmark 条件满足：作者在 4.1 和 6.3 中明确以 greedy approach 为 benchmark 进行系统化基准比较，且该比较直接支持 RHA 降低总成本的核心主张，并有明确对照对象。因此 strict_include=true。
- 置信度：0.93

### An intelligent decision support system prototype for hinterland port logistics 

- 年份/期刊：2020 / Decision Support Systems
- DOI：10.1016/j.dss.2019.113227
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：总运输成本；总行驶距离与总行驶时间；车队规模、车辆利用率与总出行次数
- Benchmark 状态：benchmark_comparison_central
- 参照点：status quo（现状，由观测数据构建的基准）；个体最优计划（a2）；合作最优计划（a3）；仅前十大型agent合作、除前十外合作等情景
- Benchmark 表述引文：Methods 3.2：payoff为‘compared to the status quo (as the benchmark)’；Results 4：‘The benchmark is the status quo which was built from the observed data. The comparison between these measures ... as a result of either providing the individual optimum plan ... or adopting cooperation strategies.’
- Benchmark 评价：在Port of Brisbane两周真实集装箱移动数据构建的现状基准上，比较维持现状、个体最优计划、合作最优计划等方案；报告总运输成本、时间、距离、车队规模和出行次数，并展示RL学习后各agent的成本分布和PCS使用概率收敛。该benchmark用于支持核心的成本/距离节约主张。
- 判定理由：客观指标方面，核心成功指标为总运输成本、距离、时间、车辆利用率和出行次数等可审计/可计量输出，不依赖主观评价，且全文围绕这些指标的提升展开；唯一核心目标被判定为客观成本/效率提升，agent-based模型是实现该目标的工具而非并列贡献。benchmark方面，作者在方法中明确以现状（status quo）作为benchmark，并在结果部分用该benchmark比较不同DSS方案，比较结果直接支持核心的成本/距离节约主张，满足陈述式benchmark门槛。因此两个模块均通过，strict_include=true。
- 置信度：0.92

### Directed disease networks to facilitate multiple-disease risk assessment modeling 

- 年份/期刊：2020 / Decision Support Systems
- DOI：10.1016/j.dss.2019.113171
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：MeanAccuracy（半衰期加权命中准确率）；Ratio1Score（完全命中比例）；Precision / Recall / F1 Score
- Benchmark 状态：benchmark_comparison_central
- 参照点：CF (Collaborative Filtering)；KNN (K-nearest neighbor)；DT (Decision Tree)；SPM (Sequential Pattern Mining)
- Benchmark 表述引文：Section 5.3.1 Baselines 中明确写道："collaborative filtering (CF) is used as a baseline in this study, which had been applied to multiple disease predictive modeling [10] and is the classic benchmark method in the field of multi-disease risk prediction study [27,28]"。该句出现在评价方法部分，用 benchmark 指称对比基准。
- Benchmark 评价：在两个独立医院数据集（Dataset A′、Dataset B′）以及合并数据集上，使用 10 折交叉验证，将所提 ADTLM 与 CF、KNN、DT、SPM 四种基准方法比较，报告 MeanAccuracy、Ratio1Score、Precision、Recall、F1 五个客观指标；Tables 6-8 显示 ADTLM 在这些指标上均高于各基准方法。
- 判定理由：该文以提升多疾病风险预测的客观性能指标作为唯一核心目标：预测目标是患者下次住院的真实 ICD 疾病诊断，评价指标均为可计算的准确性/精确率/召回率/F1，无主观量表或语义评价。同时，文章在评价部分明确将 CF 称为 classic benchmark method，并通过 Tables 6-8 将 ADTLM 与 CF、KNN、DT、SPM 等明确参照对象比较，报告客观指标提升；该 benchmark 对比直接支撑核心提升主张。因此两个模块均通过，strict_include=true。
- 置信度：0.78

### Forecasting demand profiles of new products 

- 年份/期刊：2020 / Decision Support Systems
- DOI：10.1016/j.dss.2020.113401
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：RMSE（预测总需求与每周需求的均方根误差）；PICP 与 PINAW（预测区间覆盖率与归一化平均宽度）；Cycle Service Level 一致性（CSL）；库存成本（订购、持有、超量持有、Lost sales）
- Benchmark 状态：benchmark_comparison_central
- 参照点：ZeroR (Zero Rule)；OneP (One Proximity)
- Benchmark 表述引文：Section 5.3 明确写出：'Therefore, we need to define other types of benchmarks. The first benchmark we define is Zero Rule ... The second benchmark ... One Proximity ...'；摘要亦言 'Compared to several benchmark methods, DemandForest provides the most accurate predictions'。
- Benchmark 评价：在合成数据集和5家企业真实数据集（A-E）上，将 DemandForest（含 Gamma/Log-Normal 扩展）与 ZeroR、OneP 两个基准方法比较，报告 RMSE、PICP、PINAW、CSL 一致性及库存成本。总体结论是 DemandForest 在多数数据集上 RMSE 最低、预测区间更可靠、合成数据集库存成本最低；少数企业数据集上 ZeroR 或 OneP 成本更低，但作者仍以 benchmark 对比作为 DemandForest 核心性能提升的证据。
- 判定理由：客观指标方面：核心成功指标均为可审计的需求预测误差、预测区间质量、服务水平一致性和库存成本，不依赖主观感受或人类语义评分；唯一核心目标是提升新产品预测和库存绩效。Benchmark方面：作者在实验设置部分明确以 benchmark 一词定义 ZeroR 和 OneP 两个对照方法，并以它们在多个真实数据集和合成数据集上的结果作为 DemandForest 性能提升的核心证据；评价位于实验/结果语境，且存在明确参照点。因此两个模块均通过，strict_include=true。
- 置信度：0.93

### From predictive to prescriptive analytics: A data-driven multi-item newsvendor model 

- 年份/期刊：2020 / Decision Support Systems
- DOI：10.1016/j.dss.2020.113340
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：需求预测误差；库存总成本/平均库存成本；多物品容量约束下的最优订货量
- Benchmark 状态：benchmark_comparison_central
- 参照点：季节朴素法（s-naïve）；ETS；ARIMA；ARIMAx；FNN；RF；DNN；Gallego-Moon max-min模型（MA）；正态分布经验库存优化模型（Norm）
- Benchmark 表述引文：作者在多处使用benchmark/benchmarking表述评价：第1.1.2节“Because it is a simple yet effective data-driven model, it is used as a benchmark to test our solution.”；第4.2节“The widely used time-series methods for sales forecasting like seasonal naïve, ETS, and ARIMA... and machine learning methods... are used as the benchmarking forecasting methods.”；第4.2.3节“The seasonal naïve method is used as a benchmark method.”。
- Benchmark 评价：在真实零售数据集上，对所提QR-ML（尤其QR-RF、QR-DNN）进行系统化基准评价：需求估计部分与s-naïve、ETS、ARIMA、ARIMAx、FNN、RF、DNN对比MAE、RMSE、MAPE、相对误差和FVA；库存优化部分与Gallego-Moon max-min分布自由模型和正态经验模型对比库存成本。结果显示所提方法在多数场景下误差和库存成本更低。结论中的核心改进主张依赖这些benchmark对比结果。
- 判定理由：本文核心目标是提升完全客观的预测误差和库存成本指标，全文评价和贡献声明均围绕该目标，不存在主观构念或并列的非客观核心目标；同时作者明确使用benchmark/benchmarking表述，在真实零售数据上将所提方法与传统时间序列、机器学习和多种库存优化方法进行系统比较，结果作为核心改进主张的关键证据。客观指标和benchmark两个模块均通过。
- 置信度：0.95

### Geo-semantic-parsing: AI-powered geoparsing by traversing semantic knowledge graphs 

- 年份/期刊：2020 / Decision Support Systems
- DOI：10.1016/j.dss.2020.113346
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：F1分数；精确率 (Precision)；召回率 (Recall)
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：NEEL16 (2016 Named entity recognition and linking challenge)
- 参照点：Naïve geoparser；NER + geocoder；Middleton et al. [33]；Halterman [37]；Avvenuti et al. [2]
- Benchmark 表述引文：在6.1节："we use the oficial dataset of the 2016 Named entity recognition and linking challenge (NEEL16). This well-known, reference dataset includes 9289 English tweets..."；在6.2节："Benchmarks. Performance comparisons are aimed at evaluating the performance of our proposed GSP technique with reference to those of baselines and other advanced geoparsing systems... we include as benchmarks the techniques proposed by Middleton et al. [33] and by Halterman [37]。"
- Benchmark 评价：在NEEL16基准数据集上，GSP与2个基线（Naïve geoparser、NER+geocoder）和3个现有技术（Middleton et al., Halterman, 以及作者之前的Avvenuti et al.）进行对比，报告precision/recall/F1（Table 2）。GSP取得F1=0.665，显著优于所有其他技术（F1≤0.553）。
- 判定理由：本文的核心目标是提升完全客观的geoparsing指标（precision/recall/F1），没有主观指标或并列的理论/组织贡献；评价在命名的公开基准数据集NEEL16上进行，并与多个baseline和SOTA方法比较，benchmark评价直接支撑核心提升主张。因此strict_include=true。
- 置信度：0.95

### Leveraging fine-grained transaction data for customer life event predictions 

- 年份/期刊：2020 / Decision Support Systems
- DOI：10.1016/j.dss.2019.113232
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：AUC（ROC曲线下面积）；Top Decile Lift（TDL，前10%提升度）
- Benchmark 状态：benchmark_comparison_central
- 参照点：现有二元伪社交网络方法 mod_psn（Martens et al. 2016）；仅含聚合数据的模型 mod_s；聚合数据+二元PSN组合模型 mod_s_psn；随机猜测基线（AUC=0.50，TDL=1）
- Benchmark 表述引文：引言中明确表述：“A new methodology for the fine-grained transaction data is proposed ... We benchmark the results against those obtained from existing methods.”；结论中表述：“Third, by benchmarking models that incorporate different types of information, we derive insights about the importance of different variable categories.”
- Benchmark 评价：在来自大型欧洲金融服务机构的约132,703名客户、约6,000万笔交易的真实数据上，对搬家、生子、新关系、关系结束四个生命事件分别建模；采用10折交叉验证，以AUC和TDL为主要评价指标，并通过Wilcoxon符号秩检验进行成对比较。核心比较包括：mod_rfm（RFM扩展PSN）对比mod_psn（原始二元PSN），以及组合模型mod_s_rfm对比单一数据源模型mod_s、mod_rfm和mod_s_psn。结果显示RFM扩展显著优于二元PSN，组合模型通常达到最高预测性能，并显著优于随机猜测。
- 判定理由：客观指标方面：核心评价指标AUC和TDL基于金融机构登记的生命事件事实标签（搬家、生子、关系变化），不依赖主观感知、语义质量或偏好判断；研究目标、模型选择、评价结构和贡献声明均围绕预测绩效提升，属于唯一核心目标。Benchmark方面：作者在引言和结论中明确使用“benchmark/benchmarking”表述，并实际在真实数据集上以现有方法、单一数据源模型和随机猜测作为参照，通过10折交叉验证比较模型AUC和TDL，证明RFM扩展和组合数据源的预测性能提升。因此两个模块均通过，strict_include=true。
- 置信度：0.9

### Partial order resolution of event logs for process conformance checking 【全文无benchmark字样-需人工复核】

- 年份/期刊：2020 / Decision Support Systems
- DOI：10.1016/j.dss.2020.113347
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：一致性检查准确度；运行时效率与近似误差
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：BPI Challenge 2012 (BPI-12)；BPI Challenge 2014 (BPI-14)；Road Traffic Fine Management Process (Traffic fines)
- 参照点：BL1：将每个可能分辨率视为等概率的基线（基于Lu et al.的既有工作）；BL2：完全排除受顺序不确定性影响轨迹的基线；金标准真实适应度值：根据轨迹中事件的真实顺序计算得到的适应度
- Benchmark 表述引文：Section 6.1：We conducted our evaluation based on both real-world and synthetic data collections. ... We used three, publicly available, real-world events logs, detailed in Table 3。虽未使用“benchmark”一词，但明确命名BPI-12、BPI-14和Traffic fines这些公开领域标准事件日志，并将其作为核心评价场地。
- Benchmark 评价：在BPI-12、BPI-14和Traffic fines三个公开真实事件日志以及500个合成模型上评价所提出的trace equivalence、N-gram和weak order行为模型；报告trace-level RMSE和log-level误差，并与BL1（均匀概率基线）和BL2（丢弃不确定轨迹的基线）比较；结果表明所提模型一致优于基线，例如Traffic fines日志RMSE为0.011 vs BL1的0.182，综合平均误差降低59.0%。
- 判定理由：该文核心问题是部分有序事件日志的一致性检查，核心贡献是概率性偏序解析、多种行为模型和带统计保证的近似方法。评价的核心指标是一致性检查准确度（trace-level RMSE和log-level误差）以及运行时效率，均为完全客观、可审计的指标，且没有与主观体验或理论机制并列的核心目标。在benchmark方面，文章虽未直接使用benchmark一词，但明确命名BPI-12、BPI-14和Traffic fines三个公开领域标准事件日志作为核心评价场地，并在该场地与BL1、BL2基线及金标准真实适应度比较，结果用于支撑“显著提升准确度（平均误差降低59.0%）”的核心主张。因此两个模块均通过，strict_include为true。
- 置信度：0.85

### mHealth App recommendation based on the prediction of suitable behavior change techniques 

- 年份/期刊：2020 / Decision Support Systems
- DOI：10.1016/j.dss.2020.113248
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：Top-n推荐的Precision@n、Recall@n、F-measure@n；BCT适合性预测的Accuracy
- Benchmark 状态：benchmark_comparison_central
- 参照点：User-based collaborative filtering (UBCF)；Item-based collaborative filtering (IBCF)；Matrix factorization-based recommendations (MF)；Singular value decomposition (SVD)
- Benchmark 表述引文：4.3.4节原文表述：we compare BHAR to several benchmark methods using the same dataset. These include User-based collaborative filtering (UBCF), Item-based collaborative filtering (IBCF), Matrix factorization-based recommendations (MF), and Singular value decomposition (SVD)。结论部分亦称性能优势是compared with several benchmark methods。
- Benchmark 评价：在来自中国移动运营商的真实数据集上，将BHAR与UBCF、IBCF、MF、SVD四种基准推荐方法比较；Fig.8显示BHAR在Precision@1=0.44、Recall@1=0.38、F-measure@1=0.41等指标上均优于各基准方法，用于支撑核心主张，即考虑BCT和用户特征可提升mHealth App推荐性能。
- 判定理由：该文以提升mHealth App推荐性能为核心目标，核心成功指标是Precision、Recall、F-measure和Accuracy，均由移动运营商系统日志与固定公式计算，不依赖主观用户评价或语义质量判断，属于完全客观的可观测结果。全部贡献围绕BCT-based推荐方法展开，无并列核心目标。在4.3.4节明确使用benchmark methods表述，将BHAR与UBCF、IBCF、MF、SVD等显式基线在同一真实数据集上比较，结果用于支撑核心性能提升主张，满足benchmark比较中心性要求。因此strict_include为true。
- 置信度：0.92

### A competing risks model based on latent Dirichlet Allocation for predicting churn reasons 

- 年份/期刊：2021 / Decision Support Systems
- DOI：10.1016/j.dss.2021.113541
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：预测客户流失概率与流失原因的性能指标（LL/AIC/BIC、P@r、top-decile lift）
- Benchmark 状态：benchmark_comparison_central
- 参照点：benchmark model (BM)：当前TSP使用的随机选择模型
- Benchmark 表述引文：第5.3节：'We compare the predictive performances of our proposed models with the predictive performances of a benchmark model (BM). This benchmark model randomly selects N customers as churners for March 2016... This benchmark model is the currently employed predictive model at the TSP.' 作者明确将该当前部署模型称为benchmark model，并在随后的表8、表9及图3中以其作为比较基准。
- Benchmark 评价：基准模型为随机从客户中选择流失者的当前TSP部署模型。在2016年3月测试集上，将所提出的持续时间模型和三个竞争风险模型与基准模型比较P@r和top-decile lift；结果显示所有提出模型的P@r和top-decile lift均高于基准模型，支持核心改进主张。
- 判定理由：客观指标方面：核心指标是流失预测与原因预测的客观性能指标（LL/AIC/BIC、P@r、lift），流失事件与原因来自公司系统记录，不依赖主观评价；预测性能提升是全文唯一核心目标与贡献，无并列核心目标。benchmark方面：作者在实验部分明确使用“benchmark model”指代当前TSP部署的模型，并将其作为比较基准（陈述式benchmark），该基准评价用于证明所提模型在P@r和lift上的提升，且具有明确比较器（BM），满足全部门槛。因此strict_include为true。
- 置信度：0.98

### A multivariate approach for multi-step demand forecasting in assembly industries: Empirical evidence from an automotive supply chain 

- 年份/期刊：2021 / Decision Support Systems
- DOI：10.1016/j.dss.2020.113452
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：预测准确度（NMAE）；库存相关总成本（TC）；损失率与填充率（LR/FR）
- Benchmark 状态：benchmark_comparison_central
- 参照点：Naïve；Theta；ARIMA；ERNN；AutoML
- Benchmark 表述引文：第5.3节标题即为“Baseline & benchmark models”，正文明确写道：“We start by comparing the forecast results with those of three traditional univariate benchmark models, including the Naïve (random walk), Theta and ARIMA, commonly adopted in researches on demand forecasting based on the M3 competition data.”另有“company benchmark ARIMA”等表述。
- Benchmark 评价：在 Bosch 汽车电子真实数据集上，用多元模型（MLP、RF、SVR、AutoML、ERNN、ARIMAX）与单变量基准模型（Naïve、Theta、ARIMA）在滚动源方案下进行多步预测对比，报告 NMAE、TC、LR/FR 等客观指标；基准模型是可比较的明确参照点，结果用于证明多元方法在预测与库存绩效上的提升。
- 判定理由：客观指标方面：核心指标为预测误差（NMAE）、库存相关成本（TC）、损失率/填充率（LR/FR），全部来自 ERP 实际需求与预测值的确定性计算，不依赖主观感受或语义评价；核心目标与贡献声明均围绕预测与库存绩效提升，无并列主观或理论核心目标。Benchmark 方面：第5.3节明确命名为“Baseline & benchmark models”，列出 Naïve、Theta、ARIMA 等基准，并作为实验评价的参照点；多个结果表将多元模型与基准比较，证明客观指标提升，benchmark 评价直接支撑核心主张。因此两个门槛均通过，strict_include=true。
- 置信度：0.97

### A personalized paper recommendation method considering diverse user preferences 【全文无benchmark字样-需人工复核】

- 年份/期刊：2021 / Decision Support Systems
- DOI：10.1016/j.dss.2021.113546
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：Precision（精确率）；Recall（召回率）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：Aminer dataset；DBLP dataset
- 参照点：BC (Bibliographic coupling)；CC (Co-citation)；MSCN；CAR；Metapath [42]
- Benchmark 表述引文：Section 4.1: "We conducted experiments to demonstrate the performance of our proposed paper recommendation method on the Aminer and DBLP datasets."
- Benchmark 评价：在 Aminer 和 DBLP 两个公开标准数据集上评价 PRHN 方法，采用 5 折交叉验证，比较 Precision 和 Recall，并与 BC、CC、MSCN、CAR、Metapath 等基线方法对比。
- 判定理由：本文核心目标明确且唯一：提出 PRHN 论文推荐方法以提升推荐精度和召回率。评价指标均为基于真实参考文献集合的 Precision/Recall，完全客观，不依赖主观评价。实验在公开标准数据集 Aminer 和 DBLP 上进行，并与多个基线方法比较，benchmark 评价直接支撑核心提升主张。因此两个模块均通过，strict_include 为 true。
- 置信度：0.88

### A technique for determining relevance scores of process activities using graph-based neural networks 

- 年份/期刊：2021 / Decision Support Systems
- DOI：10.1016/j.dss.2021.113511
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：AUC_ROC；灵敏度 (Sensitivity/TPR)；特异度 (Specificity/TNR)；去除最相关/最不相关活动后的AUC变化
- Benchmark 状态：benchmark_comparison_central
- 参照点：BiLSTM；Random Forest；XGBoost
- Benchmark 表述引文：4.2 Setup: 'As a benchmark, we use three state-of-the-art ML algorithms for predicting process outcomes: BiLSTM [29], Random Forest (RF) [30], and XGBoost (XG) [31].'
- Benchmark 评价：在四个真实事件日志（bpi2017w、bpi2018al、bpi2020pl、sp2020）上，将GRM与三个基准（BiLSTM、Random Forest、XGBoost）比较AUC_ROC、灵敏度和特异度；Table 3显示GRM在所有数据集上的AUC_ROC均优于三个基准，并在多个特定类别的灵敏度/特异度上显著更好，用于支撑GRM具有可竞争的预测质量，从而支持相关性分数的忠实性。
- 判定理由：客观指标：核心评估指标为预测质量（AUC、灵敏度、特异度以及去掉最相关/不相关活动后的AUC变化），均基于外部事实标签计算，完全客观。唯一核心目标：论文的核心目标是设计GRM技术并验证其相关性分数的忠实性，定量评估围绕客观预测质量展开；案例研究仅为辅助效用展示，不构成并列核心成功标准。Benchmark：在4.2 Setup中明确使用'As a benchmark, we use three state-of-the-art ML algorithms...'，属于评价语境，并将GRM与BiLSTM、RF、XG在四个真实事件日志上比较，结果用于支持核心预测质量/忠实性主张；具有明确比较器。因此满足全部条件，strict_include=true。
- 置信度：0.92

### Capital shortfall: A multicriteria decision support system for the identification of weak banks 

- 年份/期刊：2021 / Decision Support Systems
- DOI：10.1016/j.dss.2021.113526
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：整体分类准确率（OCA）；平均分类准确率（ACA）；AUROC（ROC曲线下面积）
- Benchmark 状态：benchmark_comparison_central
- 参照点：logistic regression；SRISK；Texas Ratio
- Benchmark 表述引文：引言中明确写道：“For comparison purposes we benchmark the UTADIS model against logistic regression.”，位置在Introduction部分。
- Benchmark 评价：在第五节“Comparison with other measures”中，作者用S1规格并采用out-of-sample bootstrap，将UTADIS模型与逻辑回归（LR）、SRISK、Texas Ratio进行比较，报告OCA、AUROC等分类性能指标，结果显示UTADIS模型整体优于比较对象。
- 判定理由：客观指标方面，核心目标是预测银行是否有资本需求，标签来自监管压力测试结果和实际资本注入事件，属于外部可核验事实，所有成功指标均为分类准确率和AUROC等客观指标，且提升预测性能是唯一核心目标。Benchmark方面，作者在引言和评价部分明确使用benchmark一词并与逻辑回归、SRISK、Texas Ratio进行比较，比较结果直接支撑了核心预测能力提升主张，满足benchmark_comparison_central条件。因此两个模块均通过，strict_include为true。
- 置信度：0.97

### DarkNetExplorer (DNE): Exploring dark multi-layer networks beyond the resolution limit 

- 年份/期刊：2021 / Decision Support Systems
- DOI：10.1016/j.dss.2021.113537
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：渐近惊奇值 (Asymptotic Surprise, AS)；显著性 (Significance)；性能 (Performance)；内部密度 (Internal density)；电导 (Conductance)；非单例社区数量
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：Noordin Top network；Caviar network；Boko Haram network
- 参照点：Louvain；InfoMap
- Benchmark 表述引文：Section 5开头：'This characteristic is reflected in the three datasets used in our benchmark: the Noordin Top terrorist network, the Caviar network, and the Boko Haram network...'；同节明确'To evaluate the baseline methods against these datasets'。
- Benchmark 评价：在三个真实多层暗网数据集上评估DNE，并与多片模块度Louvain和multiplex InfoMap两种现有方法对比；结果表（Table 5）报告AS、模块度、电导、内部密度、Significance、Performance，以及非单例社区数量，并展示AS比较图（Fig. 6）。
- 判定理由：文章以提出并验证DNE社区检测算法为核心，目标是在多层暗网中找到'小且好'的社区，通过最大化渐近Surprise等结构度量实现，并在三个命名真实数据集（Noordin Top、Caviar、Boko Haram）上以Louvain和InfoMap为基准比较，报告AS、Significance、Performance、内部密度、电导等客观指标提升；客观指标为唯一核心目标，无主观体验或理论机制等并列核心贡献；存在明确benchmark表述，且评价处于实验部分并支撑核心改进主张。
- 置信度：0.82

### Decisions for information or information for decisions? Optimizing information gathering in decision-intensive processes 

- 年份/期刊：2021 / Decision Support Systems
- DOI：10.1016/j.dss.2021.113632
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：期望利润（expected profit）
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：决策树基准（基于公司现有决策过程、由销售经理合作创建，作为 Koffer 案例的内部 benchmark，非公开数据集）
- 参照点：基于公司当前决策流程的人类决策树（decision tree），由销售经理合作创建，作为明确的 benchmark 参照
- Benchmark 表述引文：Section 7.1（Evaluation/case study, Validation case）：“Finally, the decision tree that we will use as benchmark was developed in cooperation with the same decision makers.”（我们将用作基准的决策树是与同一决策者合作开发的。）此外，Section 7.4 声明：“We compare the outcome of the approach with a decision tree that is based on the current decision process and is created in cooperation with sales managers in the company that inspired the example.”
- Benchmark 评价：在真实世界 Koffer 报价流程案例上，将本文 MDP 优化方法的结果与基于公司现有决策过程、由销售经理合作创建的人类决策树（明确称为 benchmark）进行系统比较。Table 5 显示 MDP 期望利润 15,867.6，而决策树为 8,226.0，MDP 将期望利润翻倍；Table 6 进一步对 9 个随机实例逐个比较利润，展示平均上的改进。
- 判定理由：客观指标方面：核心成功指标是完全客观、可计算的期望利润（收益减成本），不依赖主观感受或语义判断，且提升该客观指标是全文唯一核心目标与核心贡献。Benchmark 方面：Section 7.1 明确将人类决策树称为 benchmark，并在评价语境中（Section 7.4）将其作为明确参照点，系统比较 MDP 与决策树的期望利润，直接支撑“MDP 使期望利润翻倍”的核心改进主张；比较对象虽然是非公开的案例特定决策树，但作者明确以 benchmark 一词陈述了该基准评价，满足陈述式门槛。因此两个模块均通过，strict_include=true。
- 置信度：0.95

### Dynamic self-organizing feature map-based models applied to bankruptcy prediction 

- 年份/期刊：2021 / Decision Support Systems
- DOI：10.1016/j.dss.2021.113576
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：正确分类率 (Correct Classification Rate)；F2-score；AUC (Area Under the ROC Curve)
- Benchmark 状态：benchmark_comparison_central
- 参照点：Cox proportional hazard model；Extreme learning machine；Support vector machine；Bagging；AdaBoost；XGBoost；Random subspace；Random forest
- Benchmark 表述引文：第4节 Modeling methods 开头：‘To design models used as a benchmark, we selected the modeling methods commonly used in the literature dealing with bankruptcy prediction.’（为设计用作基准的模型，我们选择了文献中常用于破产预测的建模方法。）
- Benchmark 评价：作者将动态模型与传统单一模型（Cox、SVM、ELM）和集成模型（bagging、AdaBoost、XGBoost、random subspace、random forest）作为基准进行比较，在 4 个时期的多组全体样本和分行业样本上报告正确分类率、F2 和 AUC。结果显示动态模型在多数情况下显著优于所有基准（例如表10全体样本平均正确分类率84.35%对最好基准80.34–81.08%；F2平均82.02%对76.73–80.34%）。
- 判定理由：本文核心目标是构建并验证一种利用历史数据与数据分割的破产预测集成方法，核心成功指标是完全客观的预测性能指标（正确分类率、F2、AUC），破产标签是外部事实标签，不存在主观结果作为成功标准。唯一核心目标是客观指标提升。作者在方法部分明确以‘models used as a benchmark’陈述基准模型设置，并在后续实验中将动态模型与多种传统模型进行比较，结果为核心提升主张提供关键证据，且有明确比较对象。因此客观指标与 benchmark 门槛均通过。
- 置信度：0.85

### Model identification for ARMA time series through convolutional neural networks 

- 年份/期刊：2021 / Decision Support Systems
- DOI：10.1016/j.dss.2021.113544
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：ARMA 阶数正确识别率；阶数识别均方误差 (MSE)；计算时间；预测误差 (MAE/RMSE)
- Benchmark 状态：benchmark_comparison_central
- 参照点：AIC step-wise；AIC full search；BIC step-wise；BIC full search；Acme ground-truth scenario
- Benchmark 表述引文：4.1 节开头：'Table 1 shows results of performance benchmarking.' 这是作者明确将表1的系统化比较称为 performance benchmarking，属于评价语境。
- Benchmark 评价：在自行生成的 10,000 条模拟 ARMA 时间序列测试套件（长度 1,000、3,000、10,000）上，将 CNN 与 AIC step-wise、AIC full、BIC step-wise、BIC full 进行对比，评价 AR/MA 阶数识别准确率、MSE、计算时间及后续预测 MAE/RMSE。
- 判定理由：该文核心目标是用 CNN 在 ARMA 模型阶数识别上提升客观可测的准确率和速度，并改善后续预测误差；全部核心成功指标（识别准确率、MSE、计算时间、MAE/RMSE）都来自确定性的模拟标签与计算，不涉及主观评价。全文存在明确的 performance benchmarking 表述，且基准比较位于结果评价部分，以 AIC/BIC 各变体为参照点证明 CNN 的提升，因此两个模块均通过，strict_include=true。
- 置信度：0.93

### Music intelligence: Granular data and prediction of top ten hit songs 【全文无benchmark字样-需人工复核】

- 年份/期刊：2021 / Decision Support Systems
- DOI：10.1016/j.dss.2021.113535
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：AUC（ROC曲线下面积）；分类正确/错误次数与McNemar检验
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：Billboard Hot 100 weekly chart (1998–2016/2017)
- 参照点：Model2（不含acoustic features）作为基线，与Model3（含main acoustic features）和Model4（含main+auxiliary acoustic features）比较；不同训练算法（GLM、GBM、RF、DL）之间的稳健性比较；不同测试期/训练期（2013–2016）之间的稳健性比较；两个阈值选择准则作为比较设定
- Benchmark 表述引文：数据与方法部分明确命名Billboard Hot 100作为评价场地：“The weekly Billboard Hot 100 chart is one of the most popular charts and provides 100 most popular songs for a given week based on Nielsen Music data...”；并以2013–2015为训练期、2016周榜为out-of-time测试期评价预测能力。
- Benchmark 评价：在Billboard Hot 100的2016年周榜（以及2013、2014、2015年周榜作为稳健性检验）上，评价GLM、GBM、RF、DL模型对top-ten-hit-song状态的预测能力；主要比较不含acoustic features的Model2与含main/auxiliary acoustic features的Model3/Model4。结果显示AUC由Model2的0.655提升至Model3的0.679和Model4的0.687，McNemar检验在多数设定下显著支持acoustic features改善预测。
- 判定理由：文章的核心目标是客观预测能力的提升：利用Spotify声学特征改进Billboard Hot 100 top-ten-hit-song状态的预测，评价指标为AUC与基于事实标签的分类正确性/McNemar检验，全部为客观可验证指标；该预测能力提升是唯一核心目标与贡献。基准评价方面，文章明确以公开领域标准数据Billboard Hot 100作为评价场地，在out-of-time周榜上比较含/不含声学特征的模型，AUC和McNemar检验提供了与基线模型的明确对照，benchmark评价直接支撑核心提升主张。因此两个模块均通过。
- 置信度：0.72

### Predicting donation behavior: Acquisition modeling in the nonprofit sector using Facebook data 

- 年份/期刊：2021 / Decision Support Systems
- DOI：10.1016/j.dss.2020.113446
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：AUC（ROC曲线下面积）；Top Decile Lift（十分位提升度）
- Benchmark 状态：benchmark_comparison_central
- 参照点：Binary baseline（未应用降维的top-100二元变量模型）；其他6种分类算法（KNN、BT、RF、AB、XGB、NN）；其他降维技术（NMF、LDA）；现有文献中的获取模型（Meire et al. AUC 0.54-0.61；D’Haen et al. AUC 0.62；Thorleuchter et al. AUC 0.61）
- Benchmark 表述引文：摘要中：“benchmark indicates that the combination of singular value decomposition and logistic regression outperforms all other analytical methodologies with an area under the receiver operating characteristic of 0.72 and a top decile lift of 3.33”；引言中：“To increase the robustness of our results, we benchmark these different dimensionality reduction techniques over seven prediction algorithms”。
- Benchmark 评价：作者在自有Facebook粉丝数据集上，系统比较3种降维技术（SVD、NMF、LDA）与7种分类算法（LR、KNN、BT、RF、AB、XGB、NN）以及Binary baseline，使用5x2交叉验证，以AUC和TDL为评价指标，得出SVD+LR最优（AUC=0.72，TDL=3.33），并与文献中现有获取模型性能进行比较。
- 判定理由：客观指标方面：核心目标是提升预测捐赠行为的客观性能（AUC、TDL），基于非营利组织内部捐赠数据库的实际捐赠标签，不依赖人类感知或语义评价；全文围绕预测模型构建、方法比较和特征重要性评价展开，客观指标提升是唯一核心目标。benchmark方面：作者明确使用“benchmark”一词陈述系统化的基准评价（比较3种DR技术×7种分类算法及binary baseline），该benchmark评价位于评价语境，结果SVD+LR的AUC=0.72、TDL=3.33用于支持核心提升主张，并有明确参照点（baseline、其他方法、文献数据）。因此两模块均通过，strict_include=true。
- 置信度：0.95

### Process data properties matter: Introducing gated convolutional neural networks (GCNN) and key-value-predict attention networks (KVP) for next event prediction with deep learning 

- 年份/期刊：2021 / Decision Support Systems
- DOI：10.1016/j.dss.2021.113494
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：预测准确率 (Accuracy)；F1-score (加权、宏、微平均)；精确率 (Precision) 和召回率 (Recall)
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：BPI'11；BPI'12；BPI'13；Helpdesk；EnvLog
- 参照点：LSTM (Evermann et al., 2017)；LSTM (Camargo et al., 2019)；LSTM (Tax et al., 2017)；SAE (Mehdiyev et al., 2020)；MANN (Khan et al., 2018)；CNN (Pasquadibisceglie et al., 2019)；CNN (Di Mauro et al., 2019)；RegPFA (Breuker et al., 2016)；LSTM (本文复现baseline)
- Benchmark 表述引文：摘要：'In a comprehensive evaluation study on 11 real-life benchmark datasets, we show that these two novel architectures surpass prior work in 34 out of 44 metric-dataset combinations.'；Section 4.1：'we used five different dataset collections of real-life event logs... widely used for benchmark purposes in the field of PPM'；Table 3标题：'Results obtained in comparison to benchmark approaches.'
- Benchmark 评价：在11个真实事件日志benchmark数据集（BPI'11、BPI'12及其子集、BPI'13及其子集、Helpdesk、EnvLog）上，采用10折交叉验证评估GCNN、KVP、LSTM和SAE，并报告准确率、精确率、召回率、F1指标。结果表与已有方法（如LSTM [5]、LSTM [12]、LSTM [13]、SAE [9]、MANN [19]、CNN [20]、CNN [21]、RegPFA [31]）比较，证明GCNN和KVP在34/44组合上超越先前方法。
- 判定理由：本文核心目标是在下一个事件预测任务上引入并评估GCNN和KVP，以客观预测性能（准确率、精确率、召回率、F1）提升为唯一核心贡献；所有评价均基于事件日志中的客观活动标签，不涉及主观感受或语义评价。全文存在明确benchmark表述，使用BPI'11、BPI'12、BPI'13、Helpdesk、EnvLog等公开基准数据集，在评价部分与多个现有方法比较，benchmark结果直接支撑'在34/44组合中超越先前方法'的核心主张。因此两个模块均通过，strict_include=true。
- 置信度：0.98

### Recognition of human activities for wellness management using a smartphone and a smartwatch: A boosting approach 

- 年份/期刊：2021 / Decision Support Systems
- DOI：10.1016/j.dss.2020.113426
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：Accuracy（准确率）；F1 Score；AUC（ROC 曲线下面积）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：ExtraSensory dataset（公开的真人/情境识别数据集，由智能手机和智能手表传感器记录，walking/standing/sitting/exercise/sleeping 等标签）
- 参照点：Neural Network（同一数据集上实现）；SVM（同一数据集上实现）；LR [15]*（ExtraSensory 前期研究结果）；MLP [10]*（ExtraSensory 前期研究结果）；特征工程前后的 AdaBoost 模型（同一模型的自然基线对比）
- Benchmark 表述引文：Section 3.1.1 数据描述中明确写道：“We use the publicly available Extrasensory dataset [15] to build predictive models.” 这是将 ExtraSensory 作为主要评价场地。
- Benchmark 评价：作者在 ExtraSensory 数据集上使用 138 个传感器特征，分别训练 XgBoost、AdaBoost、Boosted C5.0，并与 Neural Network、SVM 以及先前的 LR [15]*、MLP [10]* 结果进行比较；同时进行特征工程，报告 Accuracy、F1、AUC。
- 判定理由：该文以在 ExtraSensory 公开数据集上识别五类基本人类活动的 Accuracy、F1 和 AUC 作为唯一核心成功指标，核心贡献是 boosting 算法相较传统机器学习在该客观分类任务上的性能提升。基准评价使用 ExtraSensory 这一公开数据集，并与 Neural Network、SVM 及先前 LR/MLP 结果形成明确参照，支撑其核心提升主张。未发现主观量表或独立并列核心目标。
- 置信度：0.82

### Simpler is better: Lifting interpretability-performance trade-off via automated feature engineering 

- 年份/期刊：2021 / Decision Support Systems
- DOI：10.1016/j.dss.2021.113556
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：分类AUC；可解释性/简洁性（模型参数数的倒数）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：OpenML100（从中选取30个二分类数据集作为评价场地）
- 参照点：vanilla logistic regression（baseline）；gbm default；gbm tuned；svm default；SAFE gbm default/tuned；SAFE svm default
- Benchmark 表述引文：Section 4.2开头：'We performed a benchmark on the selected data sets from the OpenML100 collection of data sets for classification problems.' 摘要亦有'large-scale benchmark on several tabular data sets from the OpenML database'。
- Benchmark 评价：在OpenML100的30个二分类数据集上，对vanilla logistic regression、gbm default、gbm tuned、svm default以及对应的SAFE变体（SAFE gbm default/tuned、SAFE svm）使用平均AUC进行系统比较；同时用参数数倒数量化可解释性，并用Wilcoxon检验比较AUC和可解释性差异。benchmark结果直接支撑'简化模型不损失性能且提升可解释性'的核心主张。
- 判定理由：全文以客观可复现的AUC和模型参数数作为成功标准，没有使用用户满意度、偏好等主观评分。核心贡献是SAFE ML框架能够在保持/提升性能的同时降低模型复杂度，这属于客观指标提升。Section 4.2在OpenML100的30个数据集上进行了明确命名的benchmark，并以vanilla logistic regression、gbm、svm等作为显式参照点，benchmark结果直接支撑核心提升主张。因此objective_metric与benchmark两个模块均通过，strict_include=true。
- 置信度：0.82

### A deep recurrent neural network approach to learn sequence similarities for user-identification 

- 年份/期刊：2022 / Decision Support Systems
- DOI：10.1016/j.dss.2021.113718
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：用户重识别正确率（P）；调整兰德指数（ARI）；用户数估计的召回率与精确率
- Benchmark 状态：benchmark_comparison_central
- 参照点：Smith-Waterman 局部序列比对算法；TF-RW（基于 tf-idf 的排名加权词频方法）
- Benchmark 表述引文：摘要中明确写道："We demonstrate its superior performance ... by benchmarking against more conventional approaches to measure sequence similarity."；第 3.2 节标题为 "Benchmark methods"，并说明 "we use two methods for comparison: ... Smith and Waterman ... modified term-frequency metric ... TF-RW"。
- Benchmark 评价：在 Comscore 点击流用户重识别任务中，将 TL-RNN 与 Smith-Waterman 局部序列比对和 TF-RW 两种传统相似性方法进行系统比较，Table 1 报告各序列长度下的正确率（如 seq length=10 时 TL-RNN 89.31% vs TF-RW 78.88%），并进一步在多用户分配和用户数估计任务中报告 ARI 与 recall/precision。
- 判定理由：核心指标为用户重识别正确率、ARI、召回率/精确率，均基于可审计的事实用户标签，不依赖主观评价；研究设计、实验评价和贡献声明均围绕提升这些客观指标展开，未发现并列主观或理论核心目标。文章摘要与第 3.2 节明确使用 benchmarking/benchmark 表述，将 TL-RNN 与 Smith-Waterman 和 TF-RW 两个明确参照点系统比较，并以这些 benchmark 结果作为核心性能提升证据。客观指标与 benchmark 两模块均通过，故 strict_include=true。
- 置信度：0.96

### Analysis of third-party request structures to detect fraudulent websites 

- 年份/期刊：2022 / Decision Support Systems
- DOI：10.1016/j.dss.2021.113698
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：分类性能指标：Accuracy、Sensitivity、Specificity、Precision、F1、Matthews correlation coefficient、Youden J statistic
- Benchmark 状态：benchmark_comparison_central
- 参照点：全合法预测（All legitimate）；全欺诈预测（All fraudulent）；50/50随机预测；CS5_3PU [4]；svmRadial_3PU；3PU数据模型；组合3PU+RS数据模型
- Benchmark 表述引文：第5.1节：“To create a neutral baseline, three naive prediction methods are used for benchmark comparisons: 1) predicting all websites as legitimate, 2) predicting all websites as fraudulent, and 3) a 50/50 coin toss for every website.”；第6.1节：“our method illustrates that it is possible to improve upon the benchmark and existing prediction method results across a wide category of fraudulent websites.”
- Benchmark 评价：在自建数据集上对第三方请求结构（RS）方法、第三方使用（3PU）方法、组合数据模型及集成模型进行系统化比较，并同时报告三种朴素基准（全合法、全欺诈、随机）。结果显示RS较3PU在多数指标上显著提升，集成模型Accuracy从3PU的0.728和RS的0.721提升至0.826，F1从0.800/0.821提升至0.876。
- 判定理由：客观指标、唯一核心目标和benchmark三方面均通过。核心目标是从网站第三方请求结构中预测合法/欺诈网站，全部成功指标为Accuracy、Sensitivity、Specificity、Precision、F1、MCC、Youden J等完全客观的分类性能指标；欺诈/合法标签来自外部权威事实清单，不依赖用户感受或语义质量判断，属于objective_fixed_factual_labels；无主观量表或并列核心贡献。全文在评价语境中明确使用“benchmark comparisons”表述，并在结论中称“improve upon the benchmark and existing prediction method results”，且与朴素基线、3PU基线、RS数据及组合/集成模型比较，基准结果直接支撑核心检测性能提升主张。因此strict_include=true。
- 置信度：0.93

### Encoding resource experience for predictive process monitoring 

- 年份/期刊：2022 / Decision Support Systems
- DOI：10.1016/j.dss.2021.113669
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：AUC（ROC曲线下面积）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：Teinemaa et al. [50] benchmark（包含BPIC2011、BPIC2012、BPIC2015、Road Traffic Fines事件日志）
- 参照点：nrac：不使用资源经验特征的基准模型；不同前缀长度下的AUC对比；rac与nrac在同一数据集、同一分类器下的直接对比
- Benchmark 表述引文：Section 5.1：'For our experiments, we have considered all the datasets used in the benchmark published by Teinemaa et al. [50] and containing the resource attribute.'
- Benchmark 评价：在Teinemaa等公开基准所包含的多个事件日志（BPIC2011、BPIC2012、BPIC2015、Road Traffic Fines）上，比较使用资源经验特征（rac）与不使用资源经验特征（nrac）的模型AUC；结果显示BPIC2012中rac明显更优，BPIC2015部分日志中rac更优，BPIC2011和RTF无显著差异。
- 判定理由：文章核心目标是通过在公开事件日志上的基准比较提升预测模型AUC这一完全客观指标；预测标签（客户投诉、产品退回、是否按时完成、申请接受/取消/拒绝、罚款是否缴清）均属于客观事实，AUC计算不涉及主观评价。全文有明确benchmark表述（Section 5.1引用Teinemaa et al.基准）并位于实验评价部分，比较了rac与nrac，基准结果直接支撑核心提升主张。无主观构念，理论部分仅作为背景和特征设计依据，不构成并列核心贡献。因此两个模块均通过，strict_include为true。
- 置信度：0.95

### Fraudulent review detection model focusing on emotional expressions and explicit aspects: investigating the potential of feature engineering 

- 年份/期刊：2022 / Decision Support Systems
- DOI：10.1016/j.dss.2021.113728
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：欺诈评论/欺诈者检测性能：Precision、Recall、F1、AUC；M-SMOTE算法在不同不平衡数据集上的P/R/F1/AUC
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：Yelp.com restaurant review dataset (Rayana and Akoglu [51])；Yelp Open Dataset；Amazon dataset (Jindal and Liu [23])；Amazon Deception-Detection dataset；UCI Machine Learning Repository: Haberman, Breast cancer, Telecom Churn, Abalone
- 参照点：未做预处理的原始数据baseline；SMOTE、原始不平衡数据；Jindal and Liu [23]；Feng et al. [16]；Zhang et al. [60]；Kumar et al. [28,29]；Rayana and Akoglu [51]
- Benchmark 表述引文：Introduction：'applied it on a Yelp dataset and several other benchmarking datasets to analyze the impact of data pre-processing challenges in classification performance.'；Section 5.4：'we tested six datasets from the UCI machine learning repository... our proposed M-SMOTE algorithm performs better than SMOTE according to the precision, recall, F-1, and AUC values.'；Section 6：'We also compare the results of our proposed model with several other notable previous studies conducted on the Amazon and Yelp datasets... our proposed model achieves a greater than 80% AUC score on all four datasets.'
- Benchmark 评价：作者在Yelp真实餐厅评论数据集上开发并评价模型，同时在Amazon/Yelp Open等数据集上重复特征工程和数据预处理流程；在UCI Repository上检验M-SMOTE在不同不平衡数据集上的普适性；并在Section 6将最终模型的结果与Jindal & Liu、Feng et al.、Zhang et al.、Kumar et al.、Rayana & Akoglu等先前方法在Yelp/Amazon上的AUC/准确率进行比较，最终在Yelp上达到P=79.4%、R=83.5%、F1=85.3%、AUC=87.4%。
- 判定理由：该文是欺诈评论检测的ML方法论文。核心构念为平台标记的欺诈评论/欺诈者，属于客观固定事实标签；核心评价指标全部为P/R/F1/AUC，无主观量表或人类语义评分作为成功标准。研究问题、假设、实验和贡献均围绕提高客观检测性能展开，不存在并列的理论机制、主观体验或政策建议核心目标。benchmark方面，作者在引言明确声明在Yelp及若干benchmarking数据集上评价，并在实验和验证部分分别使用UCI Repository及Yelp/Amazon多数据集，且与SMOTE、原始baseline和多个先前研究进行数值比较，benchmark结果是支撑核心提升主张的关键证据。因此满足纳入条件。
- 置信度：0.82

### A deep learning approach for detecting fake reviewers: Exploiting reviewing behavior and textual information 

- 年份/期刊：2023 / Decision Support Systems
- DOI：10.1016/j.dss.2022.113911
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：假评论者检测性能：Accuracy、Precision、Recall、F1-score、AUC
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：YelpZIP dataset；YelpNYC dataset
- 参照点：LR；RF；SVM；CART；NB；CNN；BiLSTM；C-LSTM；BERT；ALBERT；DistilBERT；RoBERTa；Longformer；Rayana and Akoglu [9]；Sandulescu and Ester [54]；Kumar et al. [8]
- Benchmark 表述引文：摘要：'We rigorously evaluate each proposed module and the entire framework against state-of-the-art benchmarks on two real-world datasets from http://Yelp.com.'；4.2节：'Experiment 1 evaluates the detection performance of our proposed behavior-sensitive feature extractor versus state-of-the-art benchmarks using behavioral data. These benchmarks include logistic regression (LR), random forest (RF), ...'
- Benchmark 评价：在YelpZIP和YelpNYC两个真实数据集上，将提出的行为敏感特征提取器与上下文感知注意力模型同LR、RF、SVM、CART、NB以及CNN、BiLSTM、C-LSTM、BERT、ALBERT、DistilBERT、RoBERTa、Longformer等基准比较，报告Accuracy、Precision、Recall、F1、AUC，并通过配对t检验说明显著提升；另与Rayana和Akoglu、Sandulescu和Ester、Kumar等的既有方法比较AUC/F1。
- 判定理由：该文以提升假评论者检测的客观分类性能为唯一核心目标，核心指标为Accuracy、Precision、Recall、F1和AUC，来源于YelpZIP/YelpNYC上冻结的假/真评论者标签，完全客观；研究问题、实验设计和贡献声明均围绕检测性能提升展开，无主观量表或并列理论贡献。全文存在明确的benchmark评价表述：作者在摘要和实验设计中将所提框架与state-of-the-art benchmarks比较，并在Yelp两个真实数据集上与多个基线模型及既有方法比较，benchmark结果直接支撑核心性能提升主张，且有多个明确比较对象。因此严格纳入。
- 置信度：0.93

### CATCHM: A novel network-based credit card fraud detection method using node representation learning 

- 年份/期刊：2023 / Decision Support Systems
- DOI：10.1016/j.dss.2022.113866
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：AUCPR（精确率-召回率曲线下面积）；F1 分数；TP@300（每日前300个标记案件中的真实欺诈数）；PPT_A（平均单笔交易预测处理时间）；Revenue（挽回资金收益）
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：DeepWalk；Node2Vec；PageRank；GraphSAGE
- 参照点：Baseline（使用原始特征的分类模型）；RFM Baseline（仅使用RFM特征）；DeepWalk Transductive；DeepWalk + Inductive Pooling；Node2Vec + Inductive Pooling；PageRank Inductive；GraphSAGE；Bayesian ROPE=5% 的成对比较阈值
- Benchmark 表述引文：第4节标题为“Benchmarks”，开篇明确写道：“To verify the performance of CATCHM, we compared it to a number of benchmarks: DeepWalk, Node2Vec, PageRank and GraphSAGE”。第5.1节标题亦为“Data & benchmarks”；结论部分还写道“our algorithm overall outperformed the benchmarked techniques”。
- Benchmark 评价：在约324万笔真实信用卡交易数据（欺诈率0.32%）上，使用1/2/4天训练数据、1天测试的滚动窗口重复10次，将CATCHM与DeepWalk、Node2Vec、PageRank、GraphSAGE等基准方法进行比较；同时加入原始特征基线和RFM特征基线。评价指标包括AUCPR、F1、TP@300、处理时间和挽回收益，并用Bayesian signed-rank检验比较显著性。结果显示CATCHM在主要分类指标上优于各基准，且满足100毫秒处理时间约束。
- 判定理由：客观指标方面，本文的欺诈标签是经调查确认的外部事实，AUCPR、F1、TP@300、处理时间和挽回收益均为客观可测、可审计的指标，全文核心目标与贡献是提升这些客观性能指标，没有主观构念或并列的理论/制度贡献。Benchmark方面，虽然未使用公开命名的数据集，但作者明确以“Benchmarks”章节和“benchmarked techniques”等表述陈述了系统化的基准比较，将该比较作为核心证据，并与Baseline、DeepWalk、Node2Vec、PageRank、GraphSAGE等明确参照点比较，因此满足benchmark门槛。两个模块均通过，strict_include为true。
- 置信度：0.95

### Interpretable cost-sensitive regression through one-step boosting 【全文无benchmark字样-需人工复核】

- 年份/期刊：2023 / Decision Support Systems
- DOI：10.1016/j.dss.2023.114024
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：平均误预测成本
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：Abalone；Bank (8FM)；House (8L)；KC House；UCI Machine Learning Repository / DELVE repository
- 参照点：Initial/base regression cost；Bansal et al. (BSZ)；Zhao et al. (BSZ-EXT)；Hernandez-Orallo (HER)；Direct cost-sensitive LGBM/NN implementations
- Benchmark 表述引文：全文未出现“benchmark”单词，但 Section 4.2 明确将 Abalone、Bank (8FM)、House (8L)、KC House 作为公开回归数据集使用，并在 Section 4.5/Table 7 将这些数据作为评价场地，与多种现有方法比较平均误预测成本。
- Benchmark 评价：在 4 个公开回归数据集上，以 LGBM、NN、RF、MT、LR 等为基础模型，将 OSB 与初始基础回归成本、Bansal et al. (BSZ)、Zhao et al. (BSZ-EXT)、Hernandez-Orallo (HER) 以及直接优化成本函数的 LightGBM/NN 方法进行比较；结果表显示 OSB 在多数数据集和成本函数组合上取得更低的平均误预测成本。
- 判定理由：核心指标为平均误预测成本：它由成本函数和预测残差确定性计算，完全客观，不依赖人的感知或语义判断。论文的研究问题、方法论设计、实验评价和贡献声明均围绕在回归中降低该成本展开，可解释性和计算效率是辅助特性而非独立成败指标，因此 core_goal_status 为 exclusive_objective_improvement。Benchmark 门槛通过：作者在命名的公开数据集（UCI/DELVE 等来源的 Abalone、Bank、House、KC House）上系统评价 OSB，并与初始成本及多种现有方法显式比较，结果支持核心成本下降主张。因此 strict_include=true。
- 置信度：0.82

### Why some products compete and others don't: A competitive attribution model from customer perspective 

- 年份/期刊：2023 / Decision Support Systems
- DOI：10.1016/j.dss.2023.113956
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：预测性能 Precision@N 和 Recall@N；竞争分群/主题的连贯性得分（coherence score）
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：DMM；LDA；CNTM；Link-LDA；PTM；nS-ACA；nB-ACA
- 参照点：DMM；LDA；CNTM；Link-LDA；PTM；nS-ACA；nB-ACA
- Benchmark 表述引文：摘要：'our approach outperforms the benchmark models meaningfully in the literature when predicting consumers' online behaviors'；第4.6节：'The proposed ACA model is compared empirically with the following seven benchmarks'。
- Benchmark 评价：在自行采集的 Edmunds.com 汽车论坛数据上，将 ACA 与 DMM、LDA、CNTM、Link-LDA、PTM 以及两个消融版本 nS-ACA、nB-ACA 比较；评价内容为竞争分群和主题的 coherence scores（表2、表3）以及预测实际评论产品的 Precision@N/Recall@N（图8），ACA 在各项指标上一致最优，且多数差异显著。
- 判定理由：客观指标方面：核心评价指标为预测实际评论产品的 Precision@N/Recall@N 和语料驱动的 coherence score，均为可计算、可审计的客观结果，不涉及用户满意度、感知质量或人工语义评分；研究问题和贡献声明均围绕 ACA 模型在这些客观指标上的提升展开。Benchmark 方面：摘要和实验部分明确使用 benchmark models/seven benchmarks 表述，并在评价语境中与多个既有模型和消融模型进行比较，比较结果直接支撑核心提升主张。因此两个模块均通过，strict_include=true。
- 置信度：0.82

### A hybrid decision support system for adaptive trading strategies: Combining a rule-based expert system with a deep reinforcement learning strategy 

- 年份/期刊：2024 / Decision Support Systems
- DOI：10.1016/j.dss.2023.114100
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：累计回报率 (%AR)；夏普比率 (SR)；最大回撤 (MDD)
- Benchmark 状态：benchmark_comparison_central
- 参照点：B&H 策略；RB；RL；RB+RL；RB+RL+C1；TI+SVM；TI+RF；TI+LSTM；TI+XGBoost+CNN+LSTM
- Benchmark 表述引文：5.4.2 节：'We selected benchmarks by prioritizing hybrid studies that employ RB models as input features for machine learning, as these models are closely related to our approach.'；7.2 节：'our model outperformed the benchmark index funds as well as single models.'；摘要/引言：'Our model consistently outperformed benchmark indexes and other hybrid models across various market scenarios.'
- Benchmark 评价：在 S&P500 指数基金及另外五个指数基金（NYSE Composite、DAX、CAC40、Hang Seng、KOSPI）上，将提出的混合模型与 B&H、RB、RL、RB+RL、RB+RL+C1、RB+RL+C1+C2 等模型变体，以及 TI+SVM、TI+RF、TI+LSTM、TI+XGBoost+CNN+LSTM 等先前混合模型进行比较，报告 %AR、年度夏普比率、最大回撤等客观财务指标。整体测试期及不同市场情景（market crash、uptrend、downtrend）均显示提出的混合模型在多数核心指标上优于基准。
- 判定理由：客观指标门槛通过：核心成功指标为累计回报率、夏普比率、最大回撤、交易信号数量等，均基于市场数据和模拟交易客观计算，不依赖人类感受或语义判断；唯一核心目标为提升这些客观财务指标，全文没有并列的主观或理论性成功标准。Benchmark 门槛通过：作者明确使用“benchmark”一词，在 5.4.2 节明确选择对比基准（TI+SVM、TI+RF、TI+LSTM、TI+XGBoost+CNN+LSTM 等），并在多个基准指数基金上开展系统化比较，结果用于支撑核心性能提升主张；比较具有明确参照点（B&H、RB、RL、模型变体、先前混合模型），报告了提升而非孤立数值。两个模块均通过，strict_include=true。
- 置信度：0.92

### A novel federated learning approach with knowledge transfer for credit scoring 

- 年份/期刊：2024 / Decision Support Systems
- DOI：10.1016/j.dss.2023.114084
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：Accuracy（准确率）；Recall（召回率）；F1-score；KS（Kolmogorov-Smirnov统计量）
- Benchmark 状态：benchmark_comparison_central
- 参照点：FedAvg；FedProx；FedCodl
- Benchmark 表述引文：在摘要和引言中出现“benchmark methods”和“benchmark federated methods”，实验部分5.2节标题为“Performance comparison between the proposed method and the benchmark federated methods”，文中明确将FedAvg、FedProx、FedCodl作为benchmark方法进行系统比较。
- Benchmark 评价：在五个信用数据集上，将FedKT与benchmark联邦方法FedAvg、FedProx、FedCodl进行比较，在IID和Non-IID两种设置下报告Accuracy、Recall、F1-score和KS的平均性能（表5、表6，图3、图4），并通过Friedman检验验证显著性。
- 判定理由：本文核心目标为通过联邦知识转移提升信用评分模型的客观分类性能（Accuracy、Recall、F1、KS），所有实验和贡献均围绕该目标展开，无主观指标并列，核心贡献唯一且客观。全文存在明确的benchmark表述：将FedAvg、FedProx、FedCodl作为benchmark联邦方法，在五个真实信用数据集上进行系统比较，比较结果直接支撑核心性能提升主张，且具有明确参照点。因此两个模块均通过。
- 置信度：0.95

### Weighted doubly robust learning: An uplift modeling technique for estimating mixed treatments' effect 

- 年份/期刊：2024 / Decision Support Systems
- DOI：10.1016/j.dss.2023.114060
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：提升曲线下面积 (AUUC)；Qini 系数
- Benchmark 状态：benchmark_comparison_central
- 参照点：S-learner；T-learner；X-learner；DML (Double Machine Learning)；DRL (Doubly Robust Learning)；Random targeting line
- Benchmark 表述引文：在4.1.2节实验设计：'Each approach utilizes four base learners, i.e., logistic regression, decision trees, random forests, and gradient boosting trees, to ensure a comprehensive benchmark study and a robust estimate of CATE.'
- Benchmark 评价：在合成数据集和工业数据集上，将WDRL与S-learner、T-learner、X-learner、DML、DRL五种主流uplift建模方法进行系统化比较，使用四种基学习器，以AUUC和Qini系数为评价指标。结果显示WDRL在多数设置下优于这些baseline。
- 判定理由：该文章的核心目标是提出并验证WDRL方法，以提升混合处理场景下uplift建模的客观绩效指标（AUUC和Qini系数）。这些指标直接基于客户实际消费金额计算，完全客观。全文评价结构围绕与多个baseline的比较展开，并在实验设计部分明确使用'comprehensive benchmark study'表述，属于陈述式benchmark，且该benchmark评价直接支撑核心性能提升主张。未发现主观构念或并列核心目标。因此两个模块均通过，strict_include为true。
- 置信度：0.95

### Software development cost estimation: Integrating neural network with cluster analysis 【全文无benchmark字样-需人工复核】

- 年份/期刊：1998 / Information & Management
- DOI：10.1016/s0378-7206(98)00041-x
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：平均百分比误差 (best average % error)
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：COCOMO dataset
- 参照点：Pure NN（未集成聚类分析的神经网络）；不同网络配置（如表 6-8 的多种拓扑）；不同数据选择方式（DATA50、DATA34、DATA25-1~4）
- Benchmark 表述引文：实验部分原文：“The approach was tested by using the COCOMO dataset.”（Section 4, Experimental study）这是明确的命名式基准表述，将 COCOMO 数据集作为评价场地。
- Benchmark 评价：在 COCOMO 数据集上，使用 63 个历史项目，通过聚类分析产生聚类信息，并结合神经网络进行成本估计。实验中的表 9 比较了纯神经网络（Pure NN）与集成聚类后的神经网络（NN+cluster）在四个不同测试集上的平均百分比误差，结果表明集成方法在所有测试集上均有改善。
- 判定理由：客观指标方面，核心指标是 COCOMO 数据集上的平均百分比误差，完全由实际历史成本与预测成本计算，不涉及主观判断或语义评估；该指标是全文唯一核心目标和贡献。benchmark 方面，虽然全文未出现“benchmark”单词，但实验部分明确命名并使用公开领域标准数据集 COCOMO dataset 作为评价场地，并以纯神经网络作为显式参照，表 9 直接支持核心的成本估计精度提升主张，因此满足命名式 benchmark 门槛。两个模块均通过，故 strict_include=true。
- 置信度：0.82

### Estimating the development cost of custom software 

- 年份/期刊：2003 / Information & Management
- DOI：10.1016/s0378-7206(02)00099-x
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：软件项目开发工作量估计精度（MMRE和PRED(25)）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：ISBSG项目仓库 Release 6（International Software Benchmarking Standards Group）
- 参照点：文献目标值：MMRE=25%、PRED(25)=75%；OLS单变量回归模型：MMRE=68%；六种校准策略之间的对比：PROJECTS、PROJECTS-H、ATTRIBUTES、ATTRIBUTES-H、TRADEOFF、TRADEOFF-H
- Benchmark 表述引文：第3节数据描述：'The database used in our analysis is the International Software Benchmarking Standards Group (ISBSG) project repository, release 6... this international cost database is becoming the standard benchmark for SCE research.'
- Benchmark 评价：在ISBSG Release 6中筛选出59个供应链信息系统项目，用jack-knife在六种策略上评价校准类比法的估计精度；核心结果表（Table 5）报告各策略的MMRE和PRED(25)，最优策略TRADEOFF-H达到MMRE=23.84%、PRED(25)=70.37%，并与OLS回归（MMRE=68%）及文献目标值（MMRE=25%、PRED(25)=75%）比较。
- 判定理由：文章核心目标是通过校准类比法提升软件项目开发工作量估计精度，核心成功指标MMRE和PRED(25)基于ISBSG中的实际人时记录，完全客观且可审计。评价在公开标准基准ISBSG Release 6上进行，并明确将其称为SCE研究的标准benchmark；结果与文献目标值、OLS模型及多种策略比较，证明估计精度提升。不存在主观满意度、专家质量评分或理论机制等并列核心贡献，因此同时满足客观指标唯一核心目标和明确benchmark表述两个门槛。
- 置信度：0.88

### Principal component case-based reasoning ensemble for business failure prediction 

- 年份/期刊：2011 / Information & Management
- DOI：10.1016/j.im.2011.05.001
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：总体预测准确率（total predictive accuracy）
- Benchmark 状态：benchmark_comparison_central
- 参照点：M-MDA；M-Logit；M-ECBR；M-MCBR；BEST base PC-CBR
- Benchmark 表述引文：第4.3节：'Two statistical methods (MDA and Logit) have been used for comparisons in BFP and were used as our benchmark methods. ECBR and MCBR were also used. For benchmarking purposes, stepwise MDA was used...'。
- Benchmark 评价：在作者自构建的中国短期和中期BFP数据集上，将PC-CBR-E与明确的benchmark方法（M-MDA、M-Logit、M-ECBR、M-MCBR）及最优基PC-CBR进行比较，报告平均预测准确率、标准差等统计量，并通过单尾显著性检验证明PC-CBR-E显著优于这些基准。
- 判定理由：客观指标：研究唯一核心指标是BFP的总体预测准确率，标签为ST/非ST等客观事实，所有核心评价均为准确率和显著性检验，无主观构念或人类语义评价。唯一核心目标：研究问题、假设、实验设计和贡献声明均围绕提升CBR预测准确率，无并列核心贡献。Benchmark：第4.3节明确使用'benchmark methods'和'benchmarking purposes'表述，将MDA、Logit、ECBR、MCBR及最优基模型作为比较基准，并在实验结果中通过准确率统计和显著性检验支撑核心提升主张。因此满足全部纳入条件。
- 置信度：0.95

### A domain-feature enhanced classification model for the detection of Chinese phishing e-Business websites 

- 年份/期刊：2014 / Information & Management
- DOI：10.1016/j.im.2014.08.003
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：精确率（Precision）；召回率（Recall）；F1值（F1-measure）
- Benchmark 状态：benchmark_comparison_central
- 参照点：Abbasi et al. (2010) model；He et al. (2011) model
- Benchmark 表述引文：第4.3节：'...it makes sense to use detection models that have also adopted this approach as benchmarks.' 作者明确将两个基线模型称为benchmarks，用于系统化比较检测性能。
- Benchmark 评价：在约3000个中国电子商务网站（1416个钓鱼网站和1462个真实网站）上，将所提出的CBML模型与两个基线模型（Abbasi et al.模型和He et al.模型）进行对比。使用相同SMO算法和相同训练/测试数据，采用30折交叉验证和配对t检验，比较precision、recall和F1。结果显示CBML显著优于两个基线模型，支持核心提升主张。
- 判定理由：核心目标是提升钓鱼网站检测的客观性能指标（precision、recall、F1），该目标贯穿研究问题、假设、评价和贡献；不存在主观构念或并列核心目标。全文存在明确的benchmark表述（第4.3节将基线模型称为benchmarks），并以此比较作为核心证据证明CBML相对于两个基线模型的显著提升，因此满足严格纳入条件。
- 置信度：0.93

### EXPRS: An extended pagerank method for product feature extraction from online consumer reviews 

- 年份/期刊：2015 / Information & Management
- DOI：10.1016/j.im.2015.02.002
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：特征提取的精确率、召回率、F值
- Benchmark 状态：benchmark_comparison_central
- 参照点：HAC算法（Eirinaki et al.）；HITS算法（Zhang et al.）；EXPRS无同义词扩展变体M1；EXPRS无隐式特征推断变体M2
- Benchmark 表述引文：在4.3节“Benchmarks”中，作者明确写道：'the HAC algorithm proposed by Eirinaki et al. and a feature extraction approach based on the HITS algorithm proposed by Zhang et al. are chosen as benchmarks.' 这一表述位于评价部分，作为方法评价的标准。
- Benchmark 评价：在三个产品（Samsung Galaxy Note II、Canon EOS 600D、Philips DVP3600）的在线评论数据上，将EXPRS及其消融变体M1、M2与两种基准方法HAC和HITS比较精确率、召回率和F值，并通过配对T检验和Cohen's d效应量验证改进显著性。
- 判定理由：文章核心目标是提升产品特征提取的精确率、召回率和F值，这些指标基于人工标注的客观产品特征标签，属于客观可测的性能指标，且是唯一核心目标和贡献；评价部分明确以HAC、HITS作为benchmarks，并在评价语境中比较了多个基准方法，结果表支持核心提升主张，因此满足全部纳入条件。
- 置信度：0.95

### Discovering event episodes from sequences of online news articles: A time-adjoining frequent itemset-based clustering method 

- 年份/期刊：2020 / Information & Management
- DOI：10.1016/j.im.2020.103348
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：聚类召回率（Cluster Recall）、聚类精确率（Cluster Precision）与F值
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：TDT2；TDT3；Nallapati事件语料（248片段/53事件/1468篇文章）
- 参照点：FIHC；HAC；HAC+TD；TAFIED without TP（消融对照）
- Benchmark 表述引文：摘要：“we empirically evaluate the proposed method and include several prevalent techniques as benchmarks”；4.2节：“Three prevalent techniques served as performance benchmarks: FIHC, HAC, and HAC augmented with a time-decaying function (HAC + TD)”。
- Benchmark 评价：在Nallapati等人提供、选自TDT2/TDT3的新闻事件语料上，将TAFIED与FIHC、HAC、HAC+TD三个基准技术比较；主要结果为图7的PRT曲线、表5的最佳F值（TAFIED 0.584，FIHC 0.543，HAC 0.533，HAC+TD 0.567）以及表6的Wilcoxon检验（对HAC p<0.01、对FIHC p<0.05、对HAC+TD p<0.1）。
- 判定理由：客观指标：事件片段发现的CR/CP/F基于固定事实标签和确定性公式，属于客观可测结果；唯一核心目标是提升该聚类性能。Benchmark：作者明确把FIHC、HAC、HAC+TD称为benchmark techniques，并在TDT2/TDT3事件语料上进行系统比较，比较结果直接支撑核心提升主张且具备明确参照点。故两个模块均通过，strict_include=true。
- 置信度：0.95

### A social investing approach for portfolio recommendation 

- 年份/期刊：2021 / Information & Management
- DOI：10.1016/j.im.2021.103536
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：投资组合收益率（Portfolio Return）；Treynor 比率；Jensen 阿尔法（Jensen's alpha）
- Benchmark 状态：benchmark_comparison_central
- 参照点：no-filter recommendation；knowledge-based recommendation；authority-based recommendation；S&P 500 market index
- Benchmark 表述引文：在 Section 5『Results and evaluation』中，作者明确写道：『we used them as the representative benchmark approaches for method comparison』，并将 no-filter、knowledge-based、authority-based 作为 benchmark approaches。摘要和结论也反复使用『outperforms the market index and other benchmark approaches』。
- Benchmark 评价：在 eToro 平台收集的股票帖子数据上，构建投资组合后，将提出的 CIR 机制与 no-filter、knowledge-based、authority-based 三种推荐方法以及 S&P 500 市场指数进行 30 日模拟交易比较，评估收益、Treynor 比率和 Jensen 阿尔法。结果显示 CIR 在多数风险偏好组合下均优于这些基准。
- 判定理由：文章核心目标是提出基于社会投资平台集体智慧的投资组合推荐机制，并验证其能够提升投资组合的客观财务绩效（收益、Treynor 比率、Jensen 阿尔法）。所有核心评价指标均来自市场数据和投资组合模拟交易，不依赖人类主观感受或语义价值判断。全文在评价部分明确使用 benchmark approaches 一词，并与 no-filter、knowledge-based、authority-based 及 S&P 500 等明确参照对象比较，基准评价直接支撑核心绩效提升主张。因此同时满足客观指标唯一核心目标和明确 benchmark 表述两项条件。
- 置信度：0.95

### A text summary-based method to detect new events from streams of online news articles 

- 年份/期刊：2022 / Information & Management
- DOI：10.1016/j.im.2022.103684
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：遗漏率；误报率
- Benchmark 状态：benchmark_comparison_central
- 参照点：INCR；BERT-NED；bi-LSTM-NED
- Benchmark 表述引文：第4.2节标题为“Performance benchmarks”，文中明确写道“we included INCR as our first benchmark technique... we developed two deep-learning-based NED methods... as additional performance benchmarks”；摘要也声称“in comparison with some prevalent full-text-based techniques”。
- Benchmark 评价：在自建训练新闻语料（excite.com，506篇）和测试新闻语料（215篇）上，将SED与INCR、BERT-NED、bi-LSTM-NED三个基准技术进行比较，以miss/false alarm DET曲线评价检测有效性，结果用于支持SED改进核心客观指标的主张。
- 判定理由：本文的核心目标是提出并验证基于文本摘要的新事件检测方法，评价指标为遗漏率和误报率，均属于对既定事件标注的确定性检测性能，构念不依赖主观体验；全文在实验部分明确使用“benchmark”表述并与INCR、BERT-NED、bi-LSTM-NED等明确参照点比较，benchmark结果直接支撑核心改进主张，因此客观指标和benchmark两个模块均通过，strict_include为true。
- 置信度：0.84

### Redesigning Case Retrieval to Reduce Information Acquisition Costs 【全文无benchmark字样-需人工复核】

- 年份/期刊：1997 / Information Systems Research
- DOI：10.1287/isre.8.1.51
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：期望信息获取成本；分类准确率（次要约束指标）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：Zoo；Lymphography
- 参照点：CR_f (baseline frequency-based retrieval)；CR_lc (separate cost-based retrieval)；ID3_c (joint cost-based decision tree)
- Benchmark 表述引文：第5.3节“Experimental Data”："The two real domain data sets, Zoo and Lymphography, were selected from the Repository of Machine Learning Databases and Domain Theories (Murphy and Aha 1991)." 作者虽未使用benchmark一词，但明确以UCI公开机器学习库中的标准数据集作为评价场地。
- Benchmark 评价：在Zoo、Lymphography及两个人工数据集上，分别用CR_f、CR_lc、ID3_c训练后对保留集分配案例；通过回归方程和响应函数比较期望信息获取成本，结果支持ID3_c成本低于CR_lc、CR_lc成本低于CR_f。
- 判定理由：客观指标方面，核心目标是降低可审计的信息获取成本；分类准确率作为固定事实标签上的次要约束，也是客观指标。全文无主观构念作为成功标准，成本降低是唯一核心目标与贡献。benchmark方面，文章虽未使用benchmark一词，但在UCI公开标准数据集Zoo和Lymphography（外加两人工集）上评价三种算法，并有明确参照点CR_f、CR_lc与ID3_c比较，结果直接支撑成本降低主张。因此两个模块均通过，strict_include=true。
- 置信度：0.82

### Privacy Protection in Data Mining: A Perturbation Approach for Categorical Data 【全文无benchmark字样-需人工复核】

- 年份/期刊：2006 / Information Systems Research
- DOI：10.1287/isre.1060.0095
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：分类错误率；汇总统计错误率
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：UCI Census (Adult) dataset；UCI Contraceptive Method Choice (CMC) dataset
- 参照点：Original unperturbed data；Random perturbation；Reiss (1984) 2-order swapping；Reiss (1984) 3-order swapping
- Benchmark 表述引文：第5节：'The proposed method is evaluated using three real-world data sets... The second data set, collected from Blake et al. (1998)... UCI repository of machine learning databases... The third data set was taken from Lerman et al. (1991)... contraceptive method choice (CMC).' 该段落在评价语境中明确使用公开标准数据集，并随后进行系统化对比。
- Benchmark 评价：在Offer、Census和CMC三个数据集上，作者将随机扰动、Reiss(1984) 2阶交换、Reiss(1984) 3阶交换与提出方法在同一隐私参数下比较，报告分类错误率和汇总统计错误率；Table 4及Figures 1-2显示提出方法在所有数据集和多种扰动比例下均优于对比方法。
- 判定理由：客观指标：核心评价指标为C4.5分类错误率和汇总统计错误率，均为客观可计算、不依赖人类语义评价的指标；研究问题、设计目标与评价结构均围绕在满足隐私约束下提高数据效用，无主观量表或并列理论贡献。Benchmark：论文虽未使用'benchmark'一词，但在UCI Census(Adult)和UCI CMC等公开标准数据集上进行评价，并与Original、Random、Reiss 2阶/3阶方法比较；Table 4和Figures 1-2直接支撑核心提升主张，属于命名式公开benchmark中心评价。两项门槛均通过，因此strict_include=true。
- 置信度：0.78

### Decision-Centric Active Learning of Binary-Outcome Models 【全文无benchmark字样-需人工复核】

- 年份/期刊：2007 / Information Systems Research
- DOI：10.1287/isre.1070.0111
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：直销活动利润；决策正确性/决策错误
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：KDD Cup 1998 direct-marketing competition data set (publicly available via UCI repository; Blake and Merz 1998)
- 参照点：uniform random sampling (URS)；error-centric acquisition (ECA/Bootstrap-LV)；uncertainty sampling for decision learning (US-DL)；GOAL-AC (含获取成本的GOAL扩展) vs GOAL；不同质量效用估计下的GOAL vs URS/ECA/DL
- Benchmark 表述引文：§4中明确说明：'The data pertain to a charity's periodic solicitations to potential donors; they were the data for the KDDCUP competition in 1998 ... and are now publicly available.' 即命名了公开竞赛数据集KDD Cup 1998，并将其作为评价场地。
- Benchmark 评价：在KDD Cup 1998直销数据上，将数据划分为初始训练集、未标记池和测试集，比较GOAL、误差中心获取(ECA/Bootstrap-LV)、均匀随机抽样(URS)和用于决策学习的uncertainty sampling(US)；在不同获取数量下计算模拟直销活动的利润，并在利润、决策错误、概率估计误差、鲁棒性和非均匀成本场景下进行评价。
- 判定理由：核心指标是直销活动利润和决策正确性，均为客观可审计结果，无主观满意度、感知价值或人体语义评分。唯一核心目标与贡献是提出并验证决策中心主动学习方法以提升客观决策盈利；论文虽有框架和理论推导，但均为支撑该目标的方法学内容，不构成并列核心结果。Benchmark门槛方面，全文虽未出现'benchmark'一词，但明确命名了公开的KDD Cup 1998数据挖掘竞赛数据集，并将其作为评价场地；在该基准上对GOAL与URS、ECA、US等明确参照点进行了系统的利润/决策性能比较，比较结果直接支撑核心改进主张。因此两个模块均通过，strict_include为true。
- 置信度：0.93

### A Computational Analysis of Linear Price Iterative Combinatorial Auction Formats 

- 年份/期刊：2009 / Information Systems Research
- DOI：10.1287/isre.1070.0151
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：配置效率；拍卖方收入份额；竞买人收入份额；拍卖轮数；价格非单调性
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：Combinatorial Auctions Test Suite (CATS) value models；pairwise synergy value model (An et al. 2005)
- 参照点：VCG 基准 (Vickrey-Clarke-Groves)；CC (Combinatorial Clock)；RAD (Resource Allocation Design)；RADne (RAD without eligibility)；ALPS；ALPSm；不同投标策略 (naive, bestResponse, powerSet, heuristic, bestChain)
- Benchmark 表述引文：摘要中写道：'The goal of this research is to benchmark different ICA formats and design and analyze new auction rules for auctions with pseudodual linear prices.' 在 §3.4 中写道：'We use allocative efficiency (or simply efficiency) as a primary measure to benchmark auction designs.' 此外，§3.1 明确采用公开测试套件：'we have adopted the combinatorial auctions test suite (CATS) value models that have been widely used for the evaluation of winner determination algorithms (Leyton-Brown et al. 2000).'
- Benchmark 评价：文章在 CATS 价值模型（包括交通、匹配、房地产等）以及 pairwise synergy 价值模型上生成了多种拍卖估值实例，对 CC、RAD、RADne、ALPS、ALPSm 等拍卖格式进行离散事件模拟，并以配置效率、拍卖方收入份额、轮数、价格非单调性等指标进行系统化基准比较。例如，Table 1 报告了 7 种价值模型下 40 组实例的平均效率：ALPSm 效率最高（98.81%-99.82%），ALPS 次之（92.8%-98.26%），CC 居中（96.24%-99.87%），RAD 效率最低（69.9%-90.09%）。同时设置 VCG 作为理论基准（效率 100%，收入作为竞争水平指示）。这些 benchmark 结果为证明 ALPSm 等设计在配置效率上的提升提供了核心证据。
- 判定理由：客观指标方面：文章的全部核心成功指标为配置效率、收入分配、轮数、价格非单调性等，均由模拟计算客观得出，不依赖人类感知、语义判断或主观评价；研究问题、评价结构和贡献声明均以这些客观指标的提升为中心，且未发现并列的核心目标。Benchmark 方面：摘要和 §3.4 明确使用 'benchmark' 一词陈述系统化基准评价，并采用公开的 CATS 测试套件作为价值模型评价场地；模拟实验将 CC、RAD、ALPS、ALPSm 等格式与 VCG 基准在不同价值模型上进行比较，结果直接支撑 ALPSm 在配置效率上的提升主张。因此两个模块均通过，strict_include 为 true。
- 置信度：0.92

### Induction over Strategic Agents 【全文无benchmark字样-需人工复核】

- 年份/期刊：2010 / Information Systems Research
- DOI：10.1287/isre.1090.0272
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：误分类数（positive/negative misclassifications）；目标函数值（objective value）；几何间隔/权重范数 (||w||)
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：UCI repository credit-screening data (Credit Approval Data Set)
- 参照点：Nonstrategic SVM (standard SVM without anticipating strategic behavior)
- Benchmark 表述引文：第5节‘Sample Application’：'In this section, we illustrate our general solution procedure for ISA using a credit-risk evaluation data set that is publicly available at the UCI repository ... and referred to as credit-screening data. The strategic case results are compared to the results of a nonstrategic solution to highlight the advantages of the strategic solution such as improvements in the number of misclassifications and objective function value.'
- Benchmark 评价：在UCI credit-screening公开数据集上，对策略性ISA解决方案与非策略性SVM解决方案进行对比评估，报告训练集和测试集上的正/负误分类数、目标函数值、权重范数等，并以表格形式展示策略性方案的显著改进。
- 判定理由：文章的核心目标是设计一个能预期策略性代理行为的分类规则，以最小化误分类风险。所有核心评价指标（误分类数、目标函数值、权重范数）均是从数据中直接计算得到的客观指标，不涉及任何主观构念或人类语义评价。评价结构在UCI公开基准数据集上比较了策略性解决方案与非策略性SVM，明确显示了客观指标的提升，并作为核心贡献证据。因此同时满足完全客观指标和明确benchmark表述的要求。
- 置信度：0.85

### A Finite Mixture Logit Model to Segment and Predict Electronic Payments System Adoption 

- 年份/期刊：2011 / Information Systems Research
- DOI：10.1287/isre.1090.0277
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：预测准确率（holdout样本中EPS采用分类准确率）；模型拟合指标（LL、BIC、伪R²）
- Benchmark 状态：benchmark_comparison_central
- 参照点：标准logit模型；两阶段模型（TwoStep聚类+分段logit）；层次logit模型（hierarchical logit）；互补log-log模型（complementary log-log）；含交互项logit模型；过采样模型
- Benchmark 表述引文：第4节‘Results and Discussions’开头明确写道：‘Following the data mining tradition, we compare the proposed finite mixture model with several benchmark models, including a standard logit model, a complementary log-log model, a two-stage sequential model employing segmentation followed by a classification approach, and a hierarchical logit model.’这属于明确的benchmark/benchmarking表述，且处于评价语境中。
- Benchmark 评价：在相同的数据划分（训练集与多个随机留出样本）上，对有限混合模型与标准logit模型、两阶段模型、层次logit模型、互补log-log模型进行比较。核心比较指标是留出样本上的预测准确率；有限混合模型总体预测准确率约为89.2%，而标准logit、层次logit等约为71.5%–72.2%；通过10次随机划分进一步验证，有限混合模型的平均预测准确率为90.2%，层次logit约72.0%。这些基准评价直接支撑了‘有限混合模型提升预测性能约17%’的核心主张。
- 判定理由：客观指标方面：本文核心指标为留出样本中的预测准确率（对实际ACH付款行为的分类），可直接从账单档案中计算，不依赖人类主观评价，属于fully_objective_direct。唯一核心目标是提升EPS采用预测准确率，并辅以模型拟合指标（BIC等）；研究问题、评价结构和贡献声明均围绕此目标。未发现并列的主观结果、理论机制贡献或政策建议作为核心贡献。Benchmark方面：虽然未使用公开命名的基准数据集，但作者在第4节明确使用“benchmark models”一词描述与标准logit、两阶段、层次logit、互补log-log等基线模型的系统化基准比较，且该比较处于评价语境，结果直接支撑核心预测性能提升主张，并具有明确参照点（多个baseline模型）。因此两条条件均满足，strict_include为true。
- 置信度：0.88

### Risk Management and Optimal Pricing in Online Storage Grids 

- 年份/期刊：2011 / Information Systems Research
- DOI：10.1287/isre.1100.0288
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：卖方期望收入（expected revenue）；卖方下行风险（downside risk）；买方成本与风险
- Benchmark 状态：benchmark_comparison_central
- 参照点：Amazon S3 当前固定定价政策（benchmark case）；纯现货市场策略（spot market alone）；现货+远期合约策略（forward contracts alongside spot markets）
- Benchmark 表述引文：§6.2 Empirical Study Results: “Using the benchmark case of Amazon S3’s current fixed-pricing policy for comparison, our analysis with 37 current clients indicates that spot markets alone can on average enhance revenues to Amazon by 41% while also increasing risks by 108%.” 结论部分亦重申 “as opposed to the benchmark case of Amazon S3’s current pricing policy.”
- Benchmark 评价：在 37 个 Amazon S3 客户的实际流量数据模拟中，以 Amazon 当前固定定价政策作为基准（benchmark case），评价提出的纯现货市场和现货+远期合约定价策略：纯现货平均提升收入 41% 但风险增加 108%；加入远期合约后平均降低风险 57% 并提升收入 51%。
- 判定理由：核心成功指标是卖方的期望收入和下行风险，两者均由公式、价格和需求分布决定，完全客观且依赖外部可审计的财务/统计事实；全文从摘要到结论均明确以收入提升和风险降低为最终目标，没有并列主观构念或理论解释作为核心贡献。benchmark 门槛方面，作者在实证评价部分明确使用“benchmark case of Amazon S3’s current fixed-pricing policy”作为基准，通过百分比提升和风险变化报告了所提定价策略的改进，该基准比较位于评价语境并直接支撑核心收入/风险主张，且具有明确比较对象。因此两个模块均通过。
- 置信度：0.85

### A Computational Analysis of Bundle Trading Markets Design for Distributed Resource Allocation 

- 年份/期刊：2012 / Information Systems Research
- DOI：10.1287/isre.1110.0366
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：市场收敛速度（迭代轮数）；市场效率/配置效率；社会福利与财富比率
- Benchmark 状态：benchmark_comparison_central
- 参照点：基准场景：P=0.2、V=NA、L=MA；其他异步通信水平：P=0.5, 0.8, 1；其他库存政策：SS, SP, FISS, FISP；其他学习模型：MS, FS, FA；扩展模型相对原始BTM基准
- Benchmark 表述引文：§6.3：'The benchmark scenario is the asynchronous communication $(P=0.2)$, the naïve inventory policy $(V=\mathrm{NA})$, and myopic learning with asymmetric access to information $(\hat{L}=\mathbf{MA})$.' 另见§3开头：'we present the basic BTM framework that we use as a benchmark for our extended model.'
- Benchmark 评价：作者在76,800个模拟观察上运行受控实验，以P=0.2、NA库存策略、MA学习模型为基准场景，回归模型比较不同异步通信水平、库存策略和学习模型的性能差异；结果是支撑核心主张（异步通信和不对称信息降低市场绩效，学习提高绩效，主动库存干预不一定有利等）的关键证据。
- 判定理由：客观指标方面，核心成功指标是市场迭代轮数、配置效率、社会福利/财富比率等完全由计算模型确定的客观值，不涉及人类主观评价。核心目标方面，研究问题、设计目标、实验评价和贡献声明均围绕扩展市场机制并改进计算性能，未发现并列的主观或理论核心目标。benchmark方面，作者在结果分析中明确设置'基准场景'并以此进行系统比较，该基准比较是核心判断的依据；同时§3将原始BTM框架作为扩展模型的基准。四个benchmark门槛均满足。因此严格纳入。
- 置信度：0.82

### Real-Time Tactical and Strategic Sales Management for Intelligent Agents Guided by Economic Regimes 

- 年份/期刊：2012 / Information Systems Research
- DOI：10.1287/isre.1110.0415
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：利润 (mean total profit)；价格预测精度 (RMSE)；体制分布预测精度 (KL divergence)；价格趋势方向预测成功率
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：Trading Agent Competition for Supply Chain Management (TAC SCM)
- 参照点：exponential smoother；Botticelli constant predictor；TacTex weighted-average predictor；linear interpolation for order probability；exponential smoother without regimes / other agent configurations
- Benchmark 表述引文：Section 4: 'We have implemented and tested our approach in an agent-based simulated market environment ... The annual Trading Agent Competition for Supply Chain Management (TAC SCM) ... is a competitive agent-based simulation of an abstract supply chain environment'；Section 4.1 亦提到 TacTex 预测器 'was also used as a benchmark by the Deep Maize team to test their predictions'。文章虽以 testbed 指称 TAC SCM，但该任务被明确命名并作为评价场地。
- Benchmark 评价：在 TAC SCM 标准仿真环境上，使用 2005 年 18 场训练、10 场测试数据评估体制预测方法；比较了三种 regime 预测方法与三种基线（指数平滑、Botticelli 常数预测器、TacTex 加权平均预测器）的价格预测 RMSE、体制分布 KL 散度、价格趋势方向成功率；另在真实时 TAC SCM 仿真中用相同竞争者集和 23 组可重复随机序列比较不同 agent 配置的平均利润。
- 判定理由：客观指标方面：核心成功指标是价格/体制预测精度（KL、RMSE、趋势正确率、订单概率）和仿真利润，全部为可审计的客观数值，不依赖人类感知或语义评价。唯一核心目标方面：研究问题、设计、评价和贡献声明均围绕改进预测精度并利用预测提升利润，未发现并列的主观、理论机制或政策贡献。Benchmark 方面：TAC SCM 是明确命名的公开标准测试环境，评价在其上完成，并与多种基线/现有 agent 预测方法进行显式比较，结果直接支撑核心改进主张。因此 strict_include=true。
- 置信度：0.85

### SOA Performance Enhancement Through XML Fragment Caching 

- 年份/期刊：2012 / Information Systems Research
- DOI：10.1287/isre.1110.0368
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：带宽消耗；端到端响应时间；吞吐量
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：TPC-App benchmark
- 参照点：无缓存基线 (no-cache)；完整消息缓存 (full message caching)
- Benchmark 表述引文：§8.2案例研究实验设置中：‘To simulate a realistic application at the origin node, we configured part of the TPC-App benchmark (Transaction Processing Performance Council 2010)’。摘要和结论中也明确报告案例研究实验在对比无缓存、完整消息缓存与片段缓存时，片段缓存降低响应时间40%–50%并提升吞吐量150%。
- Benchmark 评价：在TPC-App benchmark的数据库模式和负载特征上搭建案例研究实验环境，使用Cisco AON XML路由器和Tomcat应用服务器实现片段缓存，以响应时间和吞吐量为指标，与无缓存和完整消息缓存两种基线进行比较，并额外设计实验对比在唯一响应数量变化时片段缓存与完整消息缓存的性能差异。
- 判定理由：客观指标方面：核心目标与贡献均为提升SOA服务性能，包括带宽消耗、响应时间和吞吐量，全部属于可确定性观测的物理/系统指标，不涉及任何主观构念或人类语义评价。唯一核心目标为客观指标提升，全文没有并列的理论、政策、制度等核心贡献。Benchmark方面：案例研究明确使用公开的TPC-App benchmark作为评价场地，配置其数据库和负载模式；该基准评价位于实验部分并直接支撑核心性能改进主张；比较对象包括无缓存基线和完整消息缓存，因此满足明确的benchmark门槛。两个模块均通过，strict_include为true。
- 置信度：0.98

### Predicting Adoption Probabilities in Social Networks 

- 年份/期刊：2013 / Information Systems Research
- DOI：10.1287/isre.1120.0461
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：AUC（ROC曲线下面积）
- Benchmark 状态：benchmark_comparison_central
- 参照点：CM1；CM2；CM3；IP；NB；LWNB；SVM；k-NN
- Benchmark 表述引文：第4.1节：“we applied the proposed method and eight benchmark methods to predict adoption probability in week T+1”；“three cascade methods ... were benchmarked”；“We also benchmarked against support vector machine”。这些“benchmark methods/benchmarked/benchmark against”表述处于实验评价语境，构成对系统化基准比较的明确陈述。
- Benchmark 评价：在移动通信社交网络（主文）与虚拟世界社交网络（附录D）上，以AUC评价LEMNB与八个基准方法：CM1、CM2、CM3、IP、NB、LWNB、SVM、k-NN；50次评估中LEMNB平均AUC为0.8029，各基准平均AUC为0.5055、0.5056、0.5056、0.5203、0.7288、0.6658、0.7069、0.6910，Wilcoxon检验均显著优于基准（p<0.001），表2给出逐周结果。
- 判定理由：核心指标是真实采纳标签上的AUC，属于外部可核验事实标签上的预测性能，不依赖主观感知或语义评价；全文唯一核心目标是提升采纳概率预测效果，没有并列主观或理论核心贡献；在实验部分明确使用“benchmark methods/benchmarked/benchmark against”表述，将LEMNB与八个基准方法在AUC上比较并报告显著提升，benchmark评价直接支撑核心改善主张。因此两个模块均通过，strict_include=true。
- 置信度：0.96

### Recommendations Using Information from Multiple Association Rules: A Probabilistic Approach 

- 年份/期刊：2015 / Information Systems Research
- DOI：10.1287/isre.2015.0583
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：推荐准确率（successful recommendations / accuracy）；推荐运行时间
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：Retail (FIMI repository)；BMS-POS (FIMI repository)；comScore2013 (WRDS)
- 参照点：Zaïane (2002) single-rule approach；Wang and Shao (2004)；Baralis et al. (2004) L3G；Li et al. (2001) CMAR；Lin et al. (2002) rule combination approach；Item-based collaborative filtering (LensKit)；FunkSVD matrix factorization (LensKit)
- Benchmark 表述引文：摘要：'the recommendations made by our approach are more accurate than those made by a variety of state-of-the-art benchmarks'；引言贡献(iv)：'demonstrated through a variety of additional computational experiments that compare it to many key benchmarks'；第4节实验：'Then we conduct experiments comparing recommendations made using MLR with various benchmarks including the single-rule approaches...'。
- Benchmark 评价：在 Retail、BMS-POS、comScore2013 三个真实数据集上，通过五折交叉验证将 MLR 与 Zaïane (2002)、Wang and Shao (2004)、Baralis et al. (L3G)、Li et al. (CMAR)、Lin et al. (2002)、item-based collaborative filtering 和 FunkSVD 等基准方法比较推荐准确率和时间；结果显示 MLR 在大多数设置下准确率更高。
- 判定理由：文章的核心目标是提出 MLR 方法，通过组合多条关联规则提升推荐准确率，并用真实交易数据上的准确率和运行时间作为核心评价指标；两者均为客观可测量结果，不存在用户满意度、质量评价等主观核心指标。全文在摘要、引言和实验部分明确使用 benchmark 一词，将 MLR 与多个规则方法、协同过滤和矩阵分解等基准比较，benchmark 比较直接支持核心准确率提升主张。因此客观指标、唯一核心目标和 benchmark 三个门槛全部满足。
- 置信度：0.93

### Anonymizing and Sharing Medical Text Records 【全文无benchmark字样-需人工复核】

- 年份/期刊：2017 / Information Systems Research
- DOI：10.1287/isre.2016.0676
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：隐私披露风险（唯一重识别记录数与平均重识别风险）；数据效用（月份计数查询错误率、大项集支持度误差、搜索查询评分、医院计数错误率）；信息抽取性能（召回率、精确率、F值）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：i2b2 Medication data set；i2b2 Obesity data set；i2b2 VA data set
- 参照点：HIPAA Safe Harbor (SH) implementation；k-anonymity (k=3 and k=6)
- Benchmark 表述引文：第5节开头："We use the real-world data sets provided by the Informatics for Integrating Biology and the Bedside (i2b2) project for this study... We use three data sets for the experimental evaluation. The first set, which has 889 records, was provided for research on the medication aspect of patient care and thus is called Medication. The second set, called Obesity, includes 1,237 records... The third set contains 871 records... named VA." 此处明确将i2b2公开标准数据集作为系统评价场地。
- Benchmark 评价：在i2b2三个公开数据集上，将DAST原型系统与HIPAA Safe Harbor实现和k-anonymity方法进行比较。隐私风险方面比较唯一重识别记录数和平均重识别风险；数据效用方面比较月份计数查询错误率、大项集支持度误差、搜索查询评分和医院计数错误率。结果显示DAST在绝大多数比较中显著优于SH和k-anonymity（报告α=0.01或0.001显著性）。
- 判定理由：客观指标方面：全文核心成功标准是重识别风险和数据效用，均由可审计的计数和下游任务误差衡量，不依赖主观评分或语义评价；信息抽取性能基于i2b2的事实标签，同样客观。唯一核心目标方面：研究问题、设计目标和贡献均围绕降低披露风险并提升数据效用展开，没有与客观改进并列的主观、理论或政策目标。Benchmark方面：作者明确将公开的i2b2标准数据集作为评价场地，并在该场地上将DAST与SH和k-anonymity进行系统化比较，benchmark结果直接支撑核心改进主张；有明确参照点SH和k-anonymity。因此两个模块全部通过，strict_include为true。
- 置信度：0.92

### How High Should We Go? Determining Reservation Values to Negotiate Successfully for Composite Software Services 

- 年份/期刊：2017 / Information Systems Research
- DOI：10.1287/isre.2016.0678
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：协商成功率；协商成功时用户/服务提供者的平均效用
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：Global_RV_Bench；Component_RV_Bench
- 参照点：Global_RV_Bench；Component_RV_Bench；Fixed_RV_Proposed；Dynamic_RV_Proposed；Fixed_RV_Median
- Benchmark 表述引文：作者在引言中明确写：'To validate our method, we have conducted simulation experiments that show our method considerably increases the chance of successful negotiations over two benchmark approaches.' 并在第6.1节设有'Benchmark Methods and Evaluation Metrics'小节。
- Benchmark 评价：在自建的两个基准方法Global_RV_Bench和Component_RV_Bench上，通过改变组件数量、偏好信息完整度（无/部分/完全）和全局约束严苛程度，比较协商成功率、用户效用和提供者效用；实验表明Fixed_RV_Proposed在成功率与效用上优于两个基准，动态调整进一步提升成功率。
- 判定理由：该文核心目标是确定组合软件服务中各组件服务的保留值，以最大化自动化协商成功概率，并在仿真中通过成功率、用户效用和提供者效用等确定性可计算指标进行评价，属于完全客观指标提升。作者没有并列主观体验或理论机制贡献。实验部分明确以两个自建基准方法（Global_RV_Bench、Component_RV_Bench）进行系统的benchmark比较，该比较直接支撑核心成功率提升主张，且存在明确参照点。因此三部分门槛均通过。
- 置信度：0.88

### Software Diversity for Improved Network Security: Optimal Distribution of Software-Based Shared Vulnerabilities 

- 年份/期刊：2017 / Information Systems Research
- DOI：10.1287/isre.2017.0722
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：epidemic threshold（流行阈值）；Software Diversity Index（SDI，软件多样性指数）
- Benchmark 状态：benchmark_comparison_central
- 参照点：targeted software distribution strategy（Pastor-Satorras and Vespignani 2008）；LP1 vs LP2；Algorithm 3 vs fully optimized LP2
- Benchmark 表述引文：Section 4.2.2原文："For benchmarking purposes, we used the targeted software distribution strategy, which is the most recent software distribution strategy developed to increase the epidemic threshold in scale-free networks (Pastor-Satorras and Vespignani 2008)." 该句位于实验评价部分，明确将targeted distribution作为基准进行对比。
- Benchmark 评价：在软件多样性实验（Section 4.2）中，作者将LP1/LP2的SDI与targeted distribution的SDI比较，报告于Tables 3-5；在病毒传播实验（Section 4.3）中，将LP2与targeted distribution的epidemic threshold比较，报告于Figure 5和Table 6。结果显示LP模型在几乎所有实验条件下均优于基准策略，例如1,000节点、1-connectivity、SSI 5%情形下epidemic threshold从2.3提升到12.0及以上。
- 判定理由：客观指标方面，SDI和epidemic threshold均为确定性计算/仿真产生的客观数值，不涉及人类主观评价；评价结构、研究问题和贡献声明均围绕提升网络安全性（通过提高SDI和epidemic threshold）展开，属于完全客观指标且为唯一核心目标。Benchmark方面，作者在实验部分明确使用“For benchmarking purposes”将targeted distribution作为基准，并在SDI和epidemic threshold两个核心评价中与LP模型对比，基准比较直接支撑了核心提升主张，且存在明确参照点。因此两个模块均通过，strict_include=true。
- 置信度：0.93

### Service Agreement Trifecta: Backup Resources, Price and Penalty in the Availability-Aware Cloud 

- 年份/期刊：2018 / Information Systems Research
- DOI：10.1287/isre.2017.0755
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：最优备份虚拟机数 k*；提供方期望总成本；盈亏平衡价格 p'；期望可罚停机时间
- Benchmark 状态：benchmark_comparison_central
- 参照点：k = 10%n；k = 15%n；k = 20%n；k = 25%n；k = 30%n；k = 35%n
- Benchmark 表述引文：第6.5节标题为“Benchmarking the Dichotomous Search Algorithm”，正文表述：“we benchmark the quality of our solutions to the following suitable rules of thumb, i.e., k = 10%n, 15%n, 20%n, 25%n, 30%n, 35%n”；实验目标第(5)条也写明“compare how our VM provisioning algorithm performs vis-à-vis a set of benchmark provisioning strategies”。
- Benchmark 评价：在真实CCR服务器日志推导的停机分布下，采用n=50和n=100、T=30天、罚金/预置成本比1:100以及其他比例，将二分搜索算法得到的最优k*与六种固定比例备份规则（10%、15%、20%、25%、30%、35%的n）比较期望罚金成本、预置成本和期望总成本；Figure 9显示二分搜索解的期望总成本低于各基准规则，且该图同时验证期望总成本凸性。
- 判定理由：核心指标均为完全客观、可由系统日志和公式复现的指标：备份资源数量、期望总成本、盈亏平衡价格、期望可罚停机时间；文章唯一核心目标是面向SLA的可用性感知资源预置和定价优化，不存在与客观指标提升并列的主观构念或理论解释核心目标。全文存在明确benchmark表述：第6.5节对二分搜索算法与六种固定比例备份规则进行基准比较，并在Figure 9中显示最优解在期望总成本等客观指标上优于基准，该benchmark评价直接支撑核心贡献。故strict_include=true。
- 置信度：0.86

### Efficient Computational Strategies for Dynamic Inventory Liquidation 

- 年份/期刊：2019 / Information Systems Research
- DOI：10.1287/isre.2018.0819
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：清算总收入（total liquidation revenue）；计算运行时间/可扩展性（running time / scalability）
- Benchmark 状态：benchmark_comparison_central
- 参照点：FP (fixed-price strategy)；FQ (fixed-quantity strategy)；DP (dynamic-price strategy)；DQ (dynamic-quantity strategy)；SDP (stochastic dynamic programming, Bitran and Mondschein 1997)；ADP (approximate dynamic programming, Farias and Van Roy 2003)
- Benchmark 表述引文：摘要中明确写道：“we conduct a comprehensive set of simulation experiments to benchmark the performance of our proposed heuristic approach with alternatives, including other simple approaches ... as well as advanced stochastic approaches”；Section 6 标题为“Comprehensive Performance Evaluation Under Stochastic Demand”，且表格标题为“Performance Benchmarking with Other Scalable Liquidation Strategies”和“Total Revenue and Running Time Comparisons among PDS, SDP, and ADP”。
- Benchmark 评价：在随机需求模拟环境下，作者将启发式策略 PAS/PDS 与 FP、FQ、DP、DQ 等简单基准比较，并进一步将 PDS 与 SDP、ADP 两类先进随机动态规划方法比较；报告总收入、收入偏差和运行时间。结果显示 PAS/PDS 在多个配置下收入显著更高，PDS 相对 SDP 仅有 0.03%–1.12% 的收入损失，但快 3,000–86,000 倍，从而支撑核心的收入/效率改进主张。
- 判定理由：文章以库存清算总收入最大化和计算效率为客观核心目标，所有核心评价均为模拟得到的收入、运行时间、问题规模和可扩展性，不涉及主观构念或人类语义评价。全文在摘要和 Section 6 明确使用 benchmark 表述，并与 FP/FQ/DP/DQ/SDP/ADP 等明确参照点比较，benchmark 结果直接支撑启发式方法在收入和效率上的核心改进主张。因此 objective_metric.pass=true，benchmark.pass=true，strict_include=true。
- 置信度：0.95

### Optimal Management of Virtual Infrastructures Under Flexible Cloud Service Agreements 

- 年份/期刊：2019 / Information Systems Research
- DOI：10.1287/isre.2019.0871
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：总预期成本（含VM供应成本与SLA罚金成本）；成本节省率（如R[CL]、R[CE^on]、R[SISL^on]、R[MISL^on]）；算法竞争比（competitive ratio）
- Benchmark 状态：benchmark_comparison_central
- 参照点：Yuan et al. (2018) 静态无干预最优解 (NI)；周期性策略中最优的CL模型；CL3模型（用于和MISL比较）；理想离线算法（竞争比分析）
- Benchmark 表述引文：Section 7.1：'Using the static, no-intervention (denoted as NI) optimal solution of Yuan et al. (2018) as a benchmark, we first demonstrate the performance improvement under the periodic policies'；Section 7.2：'We choose the best-performing CL model under the periodic policy as the benchmark and compare it with online SISL and online MISL solutions.'
- Benchmark 评价：在Section 7计算实验和Section 8 Amazon EC2用例中，作者以Yuan et al. (2018)的静态无干预最优解（NI）、周期性策略中的最优CL模型、CL3模型等为基准，对比CL、CE^on、SISL^on、MISL^on等动态策略的预期总成本，汇报成本节省率；竞争比分析也以理想离线算法为基准比较最坏情况性能。
- 判定理由：客观指标方面，全文核心指标为预期总成本及各策略成本节省率，均由合约价格、罚金、故障统计等可审计客观因素计算，不涉及主观判断；唯一核心目标是以动态优化降低总运营成本，模型、算法、竞争比分析和Amazon用例均服务于此，无并列的主观或理论机制贡献。Benchmark方面，作者在计算分析中明确使用Yuan et al. (2018)静态最优解、CL模型等作为显式比较基准，属于陈述式benchmark，这些基准评价直接支撑核心成本改进主张，且包含明确参照点。两模块均通过。
- 置信度：0.98

### A Switch in Time Saves the Dime: A Model to Reduce Rental Cost in Cloud Computing 

- 年份/期刊：2020 / Information Systems Research
- DOI：10.1287/isre.2019.0912
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：总租赁成本（含切换成本）
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：自定义基准：最佳单计算资源方案（best single-resource solution / cheapest feasible single computing resource）
- 参照点：最佳单计算资源方案（best single-resource solution，即满足期限的最便宜单资源）；CPLEX 解（小规模实例）；理论下界（lower bound）
- Benchmark 表述引文：Section 1.4 理论贡献中提到：“To demonstrate the cost savings of our proposed solution, we use the cost of the best single-resource solution as a benchmark.” 计算实验部分（Section 6.1）定义“The benchmark solution is defined as a single computing resource solution corresponding to the cheapest feasible computing resource for the problem.”
- Benchmark 评价：在计算实验（Section 6）和 Cidewalk 真实案例（Section 7）中，作者将提出的 EnhancedRounding / EnhancedRounding^OC 方案与最佳单计算资源基准方案进行系统比较，报告总租赁成本的相对节省（如小规模实例平均节省 24.71%，大规模实例平均节省 24.44%，OC 场景约 14%–15%，Cidewalk 案例节省 27.91%）。
- 判定理由：客观指标：核心目标是总租赁成本最小化，该指标由云服务商定价和使用时长等可审计事实决定，完全客观。唯一核心目标：研究问题、模型目标、算法设计和评价指标均围绕总租赁成本展开，理论贡献和性能保证只是支持该核心目标的技术手段，不存在并列的主观或理论核心目标。Benchmark：作者明确使用“best single-resource solution as a benchmark”，并在计算实验和真实案例中进行系统比较，Benchmark 结果直接支撑“成本降低 15%–25%”的核心主张，且具有明确参照点。因此 strict_include=true。
- 置信度：0.95

### From Lurkers to Workers: Predicting Voluntary Contribution and Community Welfare 

- 年份/期刊：2020 / Information Systems Research
- DOI：10.1287/isre.2019.0905
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：个体用户贡献类型预测的AUC（Lurk/Append/Respond/Ask/Share）；社区福利八个维度（W1-W8）预测的RMSE；模拟干预带来的用户贡献增加（响应数和主题数增加百分比）
- Benchmark 状态：benchmark_comparison_central
- 参照点：No state variables；Dynamic HMM (Chen et al. 2018)；Dynamic network (Tagarelli and Interdonato 2014)；Logical regression / Random forest / XGBoost；LSTM
- Benchmark 表述引文：结果部分5.3.1：“To benchmark the performance of the HMM-AFT, we compare with several advanced alternative algorithms.”；5.3.2：“Three baselines benchmark the performance of the HMM-AFT.”
- Benchmark 评价：在DiabetesForum数据集上，将HMM-AFT与No state variables、Dynamic HMM（Chen et al. 2018）、Dynamic network（Tagarelli and Interdonato 2014）、逻辑回归、随机森林、XGBoost、LSTM等基线比较；图7报告个体贡献预测的10折交叉验证AUC提升，图8报告福利预测相对'No state variables'的RMSE改进，表4报告识别最严重福利下降时段的实际排名（HMM-AFT排名第2，基线最差58）。附加五个社区（附录D）支持泛化性。
- 判定理由：文章以HMM-AFT预测模型为核心，核心成功指标是用户贡献类型预测AUC、社区福利8个维度的RMSE预测误差以及模拟干预下贡献量提升，均为平台行为日志可计算的客观结果；全文没有主观量表或人类语义质量评价作为成功标准。文中在结果部分明确以'benchmark'动词陈述对多个基线的系统化比较（5.3.1和5.3.2），比较结果为核心客观提升主张提供直接证据，且有明确对照（No state variables、动态HMM、动态网络、静态分类器、LSTM）。因此两个模块均满足纳入标准。
- 置信度：0.78

### Hiding Sensitive Information when Sharing Distributed Transactional Data 

- 年份/期刊：2020 / Information Systems Research
- DOI：10.1287/isre.2019.0898
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：数据准确性 accuracy（未被消毒交易的比例）；推荐系统精确率 recommendation precision（辅助验证指标）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：Retail (Belgian retail store dataset, FIMI repository)；BMS-POS (electronics retailer dataset, FIMI repository)
- 参照点：最优解（CPLEX 求解 FIH_D 得到的 optimal number of transactions sanitized）；Verykios et al. (2004) 的 algorithm 2.b
- Benchmark 表述引文：Section 5.1 Data: “The real datasets—Retail and BMS-POS—are obtained from the frequent itemset mining implementations dataset repository (fimi.ua.ac.be/data/).” 这两个数据集是频繁项集挖掘领域的公开标准数据集，并作为本文评价算法的场地。
- Benchmark 评价：在 Retail 和 BMS-POS 公开标准数据集上，将数据集随机划分为 2/5/10 个分区，随机选择敏感项集，比较 Ensemble 与最优解（CPLEX 直接求解 FIH_D）以及 Verykios et al. (2004) 的被消毒交易数。Table 3 显示 Ensemble 与最优解的平均 gap 仅 0.04%–0.08%，而 Verykios 方法的平均 gap 达 28.75%–52.06%，且 Verykios 无法解决合成大数据集。这些结果直接支撑 Ensemble 在 accuracy 上的核心提升主张。
- 判定理由：客观指标方面：核心指标 accuracy 是直接由事务数据库和算法输出确定的客观数值，不依赖主观判断；FIH_D 的目标函数和全部评价围绕该指标展开，且文章核心主张为在 accuracy 上接近最优并优于现有方法。推荐 precision 作为辅助验证也是客观指标，且结论为非劣性而非提升目标。核心目标唯一性方面：没有提出并列的理论、制度、组织或主观贡献；理论命题仅支撑算法设计，推荐实验仅验证副作用。Benchmark 方面：虽然作者未在文中使用“benchmark”一词称呼数据集，但明确将频繁项集挖掘领域公开标准数据集 Retail 和 BMS-POS 作为评价场地，属于命名式 benchmark 表述；评价位于实验部分，且 Table 3 的 benchmark 结果直接用于证明 Ensemble 相对于最优解和 Verykios 方法的 accuracy 提升。因此所有门槛满足，strict_include=true。
- 置信度：0.85

### A Graph-Based Ant Algorithm for the Winner Determination Problem in Combinatorial Auctions 

- 年份/期刊：2021 / Information Systems Research
- DOI：10.1287/isre.2021.1031
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：胜者确定解的收入/解质量（revenue / solution quality）；达到最优/近最优解的时间（seconds）；最优解概率（optimal solution probability, OSP）
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：Combinatorial Auction Test Suite (CATS; Leyton-Brown et al. 2002)；Lau and Goh (2002) test instances (94 instances)
- 参照点：20个Table 1中的state-of-the-art heuristics；CPLEX exact solver；Max W Clique exact algorithm；MA、BHS、DDCM、ACLS、SHH、BRKGA等具体baseline
- Benchmark 表述引文：Section 4 Results: “We compare TrACA performance to the benchmark heuristics as mentioned in Table 1, along four specific measures.”；Section 3 Setup: “We considered Combinatorial Auction Test Suite (Leyton-Brown et al. 2002) and the ones developed by Lau and Goh (2002).”
- Benchmark 评价：在94个Lau-Goh公开测试实例上，TrACA与20个近年启发式算法（MA、BHS、DDCM、ACLS、SHH、GA、DE、BRKGA、SLS、TS等）以及CPLEX、Max W Clique进行系统化比较；报告median test、ISP、Z score、solution quality%、运行时间、最优解概率。结果显示TrACA在76/94实例达到全局最优，18/94达到98%最优，且达到最优解的用时最多为精确算法约1/6。
- 判定理由：客观指标方面：核心评价指标为胜者确定的收入/解质量、求解时间、最优解概率，全部可直接观测且不依赖人类语义或偏好；唯一核心目标是以算法改进实现WDP求解的速度-精度提升，理论证明和搜索有效性分析均为支撑，不构成并列核心贡献。Benchmark方面：全文在实验/结果部分明确使用benchmark heuristics表述，称与Table 1的20个基准启发式进行比较，并在CATS/Lau-Goh公开测试实例上以CPLEX、Max W Clique及众多baseline为参照报告客观提升结果；benchmark评价支撑核心性能改进主张。两个模块均通过，故strict_include=true。
- 置信度：0.94

### Designing Personalized Treatment Plans for Breast Cancer 

- 年份/期刊：2021 / Information Systems Research
- DOI：10.1287/isre.2021.1002
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：平均辐射剂量（AvgDose，Gy）；肿瘤控制概率（TCP）；放疗相关肺癌/心脏病风险；治疗成本节省；计算时间
- Benchmark 状态：benchmark_comparison_central
- 参照点：标准均匀计划（standard uniform plan）；L-BFGS-B；模拟退火（SA）；遗传算法（GA）；无约束最优计划 vs 约束最优计划（66 Gy cap）；现有临床剂量-风险基线（Grantzau et al. 2014; Darby et al. 2013）
- Benchmark 表述引文：Section 4开头：'To demonstrate the efficacy of our proposed framework, we follow the guidelines from Hevner et al. (2004) and perform a series of evaluations using different benchmarks.'；Section 4.2：'Adam consistently outperforms the three benchmark methods...'。这些表述置于评价语境中，且后文将框架计划与标准均匀计划及多种优化方法进行系统比较。
- Benchmark 评价：在Section 4.1基线评估中，比较标准均匀计划与框架生成的无约束/约束最优计划，在TCP目标90%/80%和三种误差设置下报告平均剂量（Tables 3-4）。在Section 4.2中，将Adam优化方法与L-BFGS-B、模拟退火（SA）、遗传算法（GA）在平均剂量和计算时间上比较（Tables 5-6）。在Section 4.3，将剂量降低转化为临床风险和治疗成本节省。这些比较直接支撑了核心改进主张：框架生成的计划能以更低剂量达到相同TCP并降低成本。
- 判定理由：客观指标门通过：核心成功指标为平均辐射剂量、TCP目标约束、剂量-风险推算的疾病风险和成本节省，均为物理/经济/可审计的客观指标，不涉及人类感受或语义判断。唯一核心目标门通过：研究问题、设计目标、评价结构和贡献声明均围绕用预测+优化框架提升放疗计划的客观结果，没有并列的主观体验、理论机制或政策目标。Benchmark门通过：Section 4明确使用benchmark/benchmarking语境，并开展标准均匀计划与非约束/约束最优计划、Adam与L-BFGS-B/SA/GA的系统比较；这些比较提供明确参照点，直接支撑核心改进主张。因此strict_include=true。
- 置信度：0.86

### Designing Core-Selecting Payment Rules: A Computational Search Approach 

- 年份/期刊：2022 / Information Systems Research
- DOI：10.1287/isre.2022.1108
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：效率 (Efficiency)；收入 (Revenue)；激励 (Incentives)
- Benchmark 状态：benchmark_comparison_central
- 参照点：QUADRATIC；First-price rule；Reserve price-weighted rule
- Benchmark 表述引文：第6节：“there are existing theoretical results for some rules that provide a benchmark for our experiments”；第8节：“we have measured the performance of all rules relative to QUADRATIC … we consider this the most natural benchmark.”
- Benchmark 评价：作者在LLG的29个变体设置和LLLLGG域中对366个备选规则进行系统化基准比较，以QUADRATIC作为核心基准，报告效率、收入和激励的改进百分比；并额外对比first-price和reserve price-weighted规则。
- 判定理由：本文以计算搜索方法寻找在效率、收入和激励三个完全客观、可由形式模型和算法计算的结果指标上优于QUADRATIC的MRC选择支付规则。核心目标和贡献均围绕这三个客观指标提升；全文不依赖主观量表或人类语义评价。评价部分以QUADRATIC为明确基准，在LLG和LLLLGG标准设置中进行系统化比较，所有核心改进主张都建立在这些基准比较之上。因此，客观指标门槛、唯一核心目标门槛和基准门槛均满足。
- 置信度：0.82

### Developing a Composite Measure to Represent Information Flows in Networks: Evidence from a Stock Market 

- 年份/期刊：2022 / Information Systems Research
- DOI：10.1287/isre.2021.1066
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：异常收益方向预测误差（AbnReturn）；异常收益幅度预测误差（|AbnReturn|）；交易策略超额收益（alpha）
- Benchmark 状态：benchmark_comparison_central
- 参照点：无EAC基准模型；Degree中心性；Closeness中心性；Betweenness中心性；PageRank中心性；替代网络规格/加权方式
- Benchmark 表述引文：摘要与第5.1节均明确使用benchmark一词：摘要称‘comparing EAC with a benchmark model without EAC and models with a set of alternative network metrics’；第5.1节称‘We first investigate if the EAC metric can provide additional predictive gains compared with benchmark models without EAC. Then we extend this benchmark for model comparisons by comparing the EAC metric with alternative network measures such as degree, closeness, betweenness, and PageRank centralities’。
- Benchmark 评价：在新浪财经2015-2016年构建的54个网络和2017年49个网络的持仓样本上，使用Fama-MacBeth、SVR、MLP、决策树、随机森林和GBDT等方法预测异常收益，用RMSE/MAE/MAPE比较EAC模型与无EAC基准模型，以及与度、接近、介数、PageRank中心性的对比；并用bootstrap置信区间检验预测精度差异。
- 判定理由：客观指标方面：核心成功指标是异常收益方向与幅度的预测误差以及交易策略的超额收益，均来自市场价格和可审计财务数据，不依赖主观感知或语义评价；唯一核心目标是提出并验证EAC这一新网络指标能显著提升异常收益预测，全文无并列的主观成功标准。Benchmark方面：作者明确使用‘benchmark model without EAC’并扩展为与多种替代网络指标的系统比较，比较结果位于结果部分，直接支撑EAC的核心性能提升主张，且有明确参照点。因此两个模块均通过，strict_include=true。
- 置信度：0.9

### Modifying Transactional Databases to Hide Sensitive Association Rules 

- 年份/期刊：2022 / Information Systems Research
- DOI：10.1287/isre.2021.1033
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：修改后数据库的准确率（accuracy）；求解时间（solution time）；被消毒事务数量（number of transactions sanitized）
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：Verykios et al. (2004) algorithm 2.a；Verykios et al. (2004) algorithm 2.b；Telikani and Shahbahrami (2017)
- 参照点：Verykios et al. (2004) algorithm 2.a；Verykios et al. (2004) algorithm 2.b；Telikani and Shahbahrami (2017)；不隐藏规则而隐藏对应项集（hiding itemsets）的方案；非线性AMP vs 线性化LRH vs 加入约简后的LRH
- Benchmark 表述引文：Section 6.3: “We also conducted similar experiments using three benchmarks from the literature: algorithms 2.a and 2.b from Verykios et al. (2004) and the method proposed by Telikani and Shahbahrami (2017).” 另有表11标题 “Benchmark Experiments”。
- Benchmark 评价：作者在真实数据集 retail、bms-pos 和合成数据集 10m/50m/100m 上评价其最优方法，并与文献中的三个基准方法进行比较；基准实验记录了各方法在24小时时限内能否求解、求解时间和被消毒事务数量，结果显示基准方法在多数问题上无法求解或需大量消毒事务，而所提最优方法在平均13.29秒内求解且消毒事务数大幅更少。
- 判定理由：客观指标方面，论文以修改后数据库的准确率/被消毒事务数作为核心目标，该指标基于事务修改这一可审计事实直接计算，不依赖人类感知或语义判断；求解时间也是客观技术指标。唯一核心目标方面，研究问题、模型、贡献声明和实验评价均围绕最大化准确率/最小化被修改事务数展开，未发现满意度、专家评分或理论机制等并列核心目标。Benchmark 方面，作者在实验部分明确使用“benchmark”一词指称文献中的三种基准方法，并在 Benchmark Experiments 表中将其作为比较对象，结果用于支持本文方法在被消毒事务数和求解时间上的核心提升主张；存在明确参照点（文献基准方法、itemset-hiding 方案、约简前后版本）。因此两个模块均通过，strict_include=true。
- 置信度：0.92

### Predicting Stages in Omnichannel Path to Purchase: A Deep Learning Model 

- 年份/期刊：2022 / Information Systems Research
- DOI：10.1287/isre.2021.1071
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：路径阶段预测性能：AUC、log-loss、accuracy、precision、recall、nDCG；lift（提升度）；利润曲线/增量货币价值
- Benchmark 状态：benchmark_comparison_central
- 参照点：模型1（仅用户+域名ID）；模型2（在线特征单通道）；模型3（离线特征）；Logistic regression；Bayesian ridge regression；Random forest；XGBoost；DeepFM
- Benchmark 表述引文：引言：'we also compare our analytical approach with several benchmark algorithms'；结果节表3后的结论：'the omnichannel model significantly outperforms all the benchmark models'。
- Benchmark 评价：在自有电信运营商omnichannel数据集上，以模型1-3（仅用户/域名ID、在线特征、离线特征）作为基准模型，对模型4（全渠道特征）进行系统化基准比较；并额外用Logistic regression、Bayesian ridge regression、Random forest、XGBoost、DeepFM作为基准算法与xDeepFM比较。报告AUC等六项指标、统计检验、lift曲线和利润曲线。
- 判定理由：客观指标方面，预测目标是对访问/考虑/购买阶段的0/1标签，由URL日志和固定编码规则确定，不涉及主观判断；核心目标明确为提升预测性能和经济价值，且为唯一核心贡献。Benchmark方面，作者在引言中明确使用'benchmark algorithms'，并在结果表3后称模型4显著优于'all the benchmark models'，属于评价语境中的基准比较；比较对象明确（模型1-3及多种预测方法），结果直接支撑omnichannel数据提升预测力的核心主张。因此两个模块均通过，strict_include为true。
- 置信度：0.85

### A Theory-Driven Deep Learning Method for Voice Chat–Based Customer Response Prediction 

- 年份/期刊：2023 / Information Systems Research
- DOI：10.1287/isre.2022.1196
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：AUC（ROC曲线下面积）；KS统计量和H measure
- Benchmark 状态：benchmark_comparison_central
- 参照点：LSTM；LSTM-self；LSTM-mh；AHED；GAS；CPC；MIMCL；MIRCL；MIECL；Concatenate；Latent space；Distance loss
- Benchmark 表述引文：第5.2节：“we compared DSDL against 12 state-of-the-art deep learning methods”，并明确使用benchmark一词：“we identified three benchmarks from multimodal deep learning methods”“The multimodal benchmarks include ...”“identified two attention-based benchmarks”“identified four benchmarks from contrastive learning–based deep learning methods”；第5.3节：“we compared DSDL against the 12 benchmarks in terms of prediction performance.”
- Benchmark 评价：在由10,625个真实车载语音对话构成的四个数据集（full/balanced/long/short）上，以文本、音频及文本+音频特征评估DSDL与12个深度学习方法；DSDL在所有数据集和特征组合上的AUC均最高，代表性结果为full data set Text+Audio AUC 84.78%，而最高基准GAS为82.70%。
- 判定理由：核心目标与核心指标均为客观可审计的客户响应预测：预测客户是否在30天内到店的二分类标签，核心成功指标为AUC等客观分类性能。全文不存在用户调研、专家评分、满意度量表等主观核心结果；期望-不一致理论仅作为方法设计依据，不构成并列的理论贡献。实验部分明确将12个现有深度学习方法称为benchmarks，并系统地在四个真实数据集上比较，DSDL在客观AUC指标上一致优于这些基准，benchmark评价直接支撑核心提升主张。因此两个模块均通过，严格纳入。
- 置信度：0.96

### Augmenting Social Bot Detection with Crowd-Generated Labels 

- 年份/期刊：2023 / Information Systems Research
- DOI：10.1287/isre.2022.1136
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：账户级社交机器人检测性能（F1、精确率、召回率、AUC）；时间到检测率（time-to-detection）；面向新批次bot的检测性能保持（precision/recall变化百分比）
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：Cresci et al. (2017) social spambot Twitter benchmark dataset；Garcia-Silva et al. (2019) BERT-based Twitter bot detection setting
- 参照点：传统机器人检测基线（语义嵌入+时间相似度）；增强模型（加入crowd reaction特征）；排除topic/sentiment/speech acts等特征后的受限特征集；SVM/RNN/LSTM/BiLSTM vs BERT；Garcia-Silva et al. (2019)在Cresci et al. (2017)上的BERT结果（F1=0.8388）
- Benchmark 表述引文：4.4.1节：'Thus, the developed model was benchmarked using restricted feature sets.' 4.2.3节：'Other traditional classification models were also selected for benchmarking and evaluation purposes.' 4.4.4节（标题'Considering Other Benchmarks'）：'The most direct study to benchmark against is Garcia-Silva et al. (2019)... We attempted to apply our own model against the same data set of Cresci et al. (2017) to produce benchmark results.'
- Benchmark 评价：在Cresci et al. (2017) Twitter数据上，作者将BERT模型及若干传统特征与Garcia-Silva et al. (2019)的BERT结果（F1=0.8388）比较，并报告可比或略优的结果；同时用restricted feature sets对核心模型进行benchmark式消融（Table 7），比较完整增强模型与排除topic/sentiment/speech acts等特征的模型，验证crowd reaction与speech acts对bot检测性能的贡献；Table 6比较传统特征基线与增强模型。
- 判定理由：该文核心目标为通过crowd-generated labels和speech act特征提升社交机器人检测的客观性能（F1、AUC、检测率等），构念为事实性bot标签，检测性能由系统输出与ground truth比对计算，不依赖主观感受，属于objective_fixed_factual_labels，且核心贡献声明、研究问题和评价结构均围绕该客观指标提升，属exclusive_objective_improvement。benchmark方面，正文在4.2.3、4.4.1、4.4.4中使用benchmark/benchmarking对中间分类器、核心模型的restricted feature sets消融以及直接对照Garcia-Silva et al.在Cresci et al. (2017)数据上的结果进行系统化评价；消融benchmark直接支撑‘crowd reactions/speech acts提升检测性能’的核心主张，且均含明确参照点。综合两个模块均通过，strict_include=true。
- 置信度：0.82

### Diversity Preference-Aware Link Recommendation for Online Social Networks 

- 年份/期刊：2023 / Information Systems Research
- DOI：10.1287/isre.2022.1174
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：多样性偏好匹配得分（DPMS）；精确率（Precision）；召回率（Recall）；F1 分数
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：Google+ dataset (Gong et al. 2012)
- 参照点：MMR；MSD；DPP；DiRec；GCN-LR；GraphSage-LR；GAT-LR；DPA-MMR；最优穷举解
- Benchmark 表述引文：第5.1节：'we benchmarked our method against representative diversification methods'；'we chose MMR as a benchmark method'；'We also benchmarked our method against the max-sum diversification method (MSD) ... and against the determinantal point process method (DPP) ...'
- Benchmark 评价：在 Google+ 公开数据集（主文）和另一大型美国在线社交网络数据集（在线附录 D）上评价 DPA-LR；与 MMR、MSD、DPP、DiRec 等多样化基准方法，以及与 GCN-LR、GraphSage-LR、GAT-LR 等最新链接推荐方法比较；报告 DPMS、Precision、Recall、F1 指标，并在 k=6 到 k=14 等设置下展示提升。
- 判定理由：本文以提升可客观计算的 DPMS 以及基于真实未来好友关系的 Precision/Recall/F1 作为唯一核心目标和核心贡献；全文评价由真实社交网络数据和系统日志驱动，不包含用户主观评分或满意度量表。第5.1节明确使用 benchmark/benchmarking 表述，将 DPA-LR 与多个多样化方法和最新链接推荐方法在 Google+ 公开数据集及另一大型数据集上进行比较，结果表构成核心提升主张的直接证据。所有 benchmark 门槛均满足，因此 strict_include=true。
- 置信度：0.8

### Pricing in Nonconvex Markets: How to Price Electricity in the Presence of Demand Response 

- 年份/期刊：2023 / Information Systems Research
- DOI：10.1287/isre.2022.1139
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：make-whole payments（MWP）；平均市场价格与价格波动
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：IEEE Reliability Test System (RTS-96)
- 参照点：IP pricing；ELMP pricing；AIC pricing
- Benchmark 表述引文：第2.3节：“In Section 6.2 we analyze our proposed pricing schemes based on a widely used benchmark data set: the IEEE Reliability Test System (RTS) consisting of 24 nodes, 24 hours, 32 generators (with nonconvex cost functions), and 17 consumers.”；第6.2节：“Finally, we report results of numerical experiments based on the IEEE RTS-96 system introduced by Grigg et al. (1999) in order to better understand prices in a larger and realistic test system.”
- Benchmark 评价：在IEEE RTS-96系统上，针对价格无弹性、价格敏感、可转移负荷等场景，比较IP pricing、ELMP、AIC与PBE-A/PE-A四种定价规则的make-whole payments、平均价格、标准差和计算时间。结果显示PBE-A/PE-A的MWP几乎为零（0%-0.15%），而IP和ELMP的MWP常为4%-5%甚至更高，从而证明新规则的核心提升。
- 判定理由：文章核心目标是提出一种最小化make-whole payments的定价规则，该指标是完全客观可测量的财务量，且全文围绕这一目标构建。在IEEE RTS-96公开基准数据集上进行系统化实验，与IP、ELMP、AIC等明确参照点比较，benchmark结果直接支撑核心提升主张。没有任何主观构念或并列核心贡献。因此同时满足客观指标、唯一核心目标和明确benchmark门槛。
- 置信度：0.96

### Spoiled for Choice? Personalized Recommendation for Healthcare Decisions: A Multiarmed Bandit Approach 

- 年份/期刊：2023 / Information Systems Research
- DOI：10.1287/isre.2022.1191
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：Precision@K / Recall@K；nDCG@K / MAP@K；DR@K / Simu@K（用户参与奖励）；推荐多样性的 JSD 相似度；用户改进率（user improvement）；期内减重率（扩展实验）
- Benchmark 状态：benchmark_comparison_central
- 参照点：CACF；SCF；PMF；CAMF；CB；hybrid_pure；hybrid_cacf；FAST；SLi-Rec；Caser；GRU4Rec；A2SVD；NextItNet；LSTUR；NPA；UCB；ε-greedy
- Benchmark 表述引文：第5.1节标题为“Comparison with Benchmark Recommendation Systems”，作者写道“To demonstrate the overall effectiveness of our proposed recommendation framework, we compare it with a series of state-of-the-art recommendation systems”；表4标题为“Comparison with State-of-the-Art Benchmarks”；正文亦称“Compared with the benchmark models, our proposed recommendation framework can better discover the uncaptured user preference patterns”。
- Benchmark 评价：在真实在线减重社区数据集上，将提出的 DLDE-MAB 与 CACF、SCF、PMF、CAMF、CB、hybrid_pure、hybrid_cacf、FAST、SLi-Rec、Caser、GRU4Rec、A2SVD、NextItNet、LSTUR、NPA、UCB、ε-greedy 等既有推荐和在线学习模型进行系统比较，报告 top-5/top-10 下的 Precision、Recall、nDCG、MAP、DR 和模拟评估；结果表明所提方法在各核心客观指标上全面优于基准模型，且差异大多统计显著。
- 判定理由：客观指标方面：论文的核心目标是最大化用户对在线健康干预的持续参与，评价指标均为基于平台日志的行为参与指标（Precision/Recall/nDCG/MAP/DR/模拟参与），以及作为扩展的客观体重健康结果，不包含主观满意度、感知有用性或人工质量评分；唯一核心目标是由设计目标、优化问题和评价结构共同支持的客观参与指标提升。Benchmark 方面：第5.1节明确以“benchmark recommendation systems”和“state-of-the-art benchmarks”命名并呈现系统化基准比较，表4将所提模型与大量既有推荐和在线学习模型在多类客观指标上比较，且该比较是支撑核心参与指标提升主张的核心证据；具有明确参照点，因此同时满足 benchmark 的四个门槛。
- 置信度：0.82

### sDTM: A Supervised Bayesian Deep Topic Model for Text Analytics 

- 年份/期刊：2023 / Information Systems Research
- DOI：10.1287/isre.2022.1124
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：模型拟合困惑度（Perplexity）；预测性能（Yelp 使用 AUROC；Stack Exchange 使用准确率）；经验回归的系数方向、显著性与统计效力（辅助展示）
- Benchmark 状态：benchmark_comparison_central
- 参照点：LDA；sLDA；MedLDA；BP-sLDA；sNNTM；NTM；Supervised PCA；RNN attention；Bi-LSTM；DistilBERT；BERT
- Benchmark 表述引文：第5.1节中：'We consider the following unsupervised topic models and supervised topic models as our benchmark baselines.' 以及第7.1节：'We choose a set of comprehensive benchmark models to compare sDTM with.'
- Benchmark 评价：在两个 IS 相关数据集（Yelp 在线评论、Stack Exchange 在线知识社区）上，作者将sDTM与多组基准模型进行比较：模型拟合评估中比较困惑度（表4），预测任务中比较AUROC/准确率（表11）。sDTM在所有设置下均显著优于无监督、有监督及深度学习基线。
- 判定理由：客观指标方面：文章核心评估为完全客观的模型拟合（perplexity）和预测性能（AUROC/准确率），这些指标可通过确定算法计算且不依赖人类感受或语义评价；全文未将主观量表或理论机制贡献列为同等核心目标，因此满足唯一核心目标要求。Benchmark方面：作者在评估部分明确使用“benchmark baselines/models”陈述系统化基准比较，并在两个数据集上与多个基线（LDA、sLDA、MedLDA、NTM、BERT等）比较，结果直接支撑sDTM的客观指标提升主张，且存在明确参照点。两项门槛均通过，故 strict_include=true。
- 置信度：0.85

### Attending to Customer Attention: A Novel Deep Learning Method for Leveraging Multimodal Online Reviews to Enhance Sales Prediction 

- 年份/期刊：2024 / Information Systems Research
- DOI：10.1287/isre.2021.0292
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：RMSE（均方根误差）；MAE（平均绝对误差）
- Benchmark 状态：benchmark_comparison_central
- 参照点：GRU；MPL-self；MPL-mh；AC-self；AC-mh；DIIA；CEN；MDL-CW；MCL
- Benchmark 表述引文：摘要：'our proposed method outperformed benchmarked state-of-the-art deep learning methods'；实验5.2节：'we compared DTV-AMI against ... eight benchmarks'，并明确列出GRU、MPL-self、MPL-mh、AC-self、AC-mh、DIIA、CEN、MDL-CW、MCL等作为baseline/benchmarks。
- Benchmark 评价：在自建的酒店评论数据集（2,685家酒店、1.25M评论文本、197K评论图像）上，以RMSE为主要指标，比较DTV-AMI与9个基线/基准方法在文本、图像、多模态三种设置及三个时间跨度下的预测性能；DTV-AMI在所有设置下均取得最优或统计显著改进。
- 判定理由：客观指标：核心指标为酒店月度入住率预测的RMSE/MAE，完全客观可验证，所有核心成功结果均为客观预测性能。唯一核心目标：全文以提升销售预测性能为唯一核心设计目标和贡献，客户注意力概念化及注意力机制设计均为该方法服务，无并列核心目标；无主观量表或用户调研。Benchmark：作者在摘要和实验部分明确使用'benchmarked'和'benchmarks'陈述系统化基准比较，在自建数据集上与9个基线/基准方法比较，结果作为核心提升主张的关键证据，且具备明确参照点。因此strict_include为true。
- 置信度：0.95

### Calibration of Heterogeneous Treatment Effects in Randomized Experiments 

- 年份/期刊：2024 / Information Systems Research
- DOI：10.1287/isre.2021.0343
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：个体处理效应估计的平均绝对误差（MAE）；策略效用（realized utility）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：Criteo AI Lab Uplift Prediction Dataset (Criteo large scale benchmark for uplift modeling, Diemert et al. 2018)
- 参照点：未校准的HTE估计（uncalibrated model-based CATE）；无模型差分估计（DM estimator）作为gold standard参照；多个HTE元算法之间的横向比较（如T-learner vs causal forest等）；MTUM应用中与多种专用uplift基准方法比较（DIA、SMA、CKNN、CTS、NUA、MMOA）
- Benchmark 表述引文：Section 5.3: 'We evaluate calibration on the publicly available advertising campaign data shared by Criteo AI Laboratory (Diemert et al. 2018).' 该数据集在参考文献中被描述为 'A large scale benchmark for uplift modeling.'
- Benchmark 评价：在Criteo公开benchmark数据集上，使用11种HTE模型（S/T/X/R/DR-learner、causal forest等）在训练集训练，验证集校准，测试集用MAE_CATE比较校准前后子组CATE与无模型DM估计的差异；Figure 6展示多数方法经校准后MAE_CATE下降，Figure 7以Q-Q图展示校准将模型CATE向无模型CATE对齐。该评价直接支撑核心主张：校准方法降低HTE估计误差。
- 判定理由：客观指标方面：核心指标是HTE估计误差（MAE/MAE_CATE）和下游策略效用，均为可审计的客观技术指标，不涉及主观构念或人类语义评价。唯一核心目标方面：研究问题、设计目标、评价结构和贡献声明均围绕“诊断并校正HTE估计偏差/提升校准性”这一客观目标展开，理论命题和诊断工具是服务该目标的方法组成部分，不存在并列的核心目标。benchmark方面：文章在Criteo公开benchmark数据集上系统评价了11种HTE方法，并与未校准模型及多种MTUM基准方法比较，benchmark结果直接支撑核心提升主张；同时具有明确的参照点。因此满足strict_include条件。
- 置信度：0.93

### Consumer Acquisition for Recommender Systems: A Theoretical Framework and Empirical Evaluations 

- 年份/期刊：2024 / Information Systems Research
- DOI：10.1287/isre.2023.1229
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：推荐系统性能（RMSE / AUC / 敏感性 / 准确率）；公司效用（firm utility）；消费者剩余（consumer surplus）
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：MovieLens 100K；Kelkoo (KASANDR)
- 参照点：随机获取序列（200个随机序列的平均值及标准差）；不同贪婪程度的ε-greedy策略（ε=0, 0.25, 0.5, 0.75, 1.0）之间的对比
- Benchmark 表述引文：摘要中明确写道：“We conduct simulation-based empirical evaluations on two canonical recommendation tasks: ... and benchmark our acquisition model with random acquisition sequences with respect to (i) firm utility, (ii) recommender system performance, and (iii) consumer surplus.” 第5.1节亦写道：“we benchmark the dynamic acquisition sequence against 200 randomly generated acquisition sequences.”
- Benchmark 评价：在两个真实数据集（MovieLens 100K和Kelkoo）上，分别采用warm-start和cold-start两种方案，将动态获取序列与200个随机获取序列比较，报告RMSE（或AUC、敏感性、准确率）、公司效用、消费者剩余、获取人数和总激励，并用单侧t检验进行统计比较。
- 判定理由：文章核心目标是设计并评估面向推荐系统的动态消费者获取策略，其成功标准完全由客观指标构成：推荐系统预测性能（RMSE/AUC/敏感性/准确率）、公司效用、消费者剩余，均为可审计的模型计算值，不涉及人类主观评价或语义判断；全文在摘要和评价方法中明确使用“benchmark”一词，将动态获取序列与200个随机获取序列系统比较，并在MovieLens 100K和Kelkoo两个标准数据集上作为核心评价证据，比较对象明确、结果支撑核心提升主张。因此两个模块均通过，strict_include=true。
- 置信度：0.82

### Proactive Resource Request for Disaster Response: A Deep Learning-Based Optimization Model 

- 年份/期刊：2024 / Information Systems Research
- DOI：10.1287/isre.2022.0125
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：平均单位需求剥夺成本；平均单位需求时间延迟；未来需求满足百分比
- Benchmark 状态：benchmark_comparison_central
- 参照点：ReR（反应式资源请求）；logNormMix-PRR；A-NDTT-PRR；AttnMC-PRR；CTDRP-PRR；LR-NV；DL-NV；logNormMix-IFCFS
- Benchmark 表述引文：在Section 5.2 'Benchmark Methods'开头明确写道：'We benchmarked our method against the current practice of resource request, which reactively sets quantities of requested resources as quantities of currently unfulfilled demands (Huang et al. 2015).' 以及'...we benchmarked our method against state-of-the-art data-driven inventory control (IC) models...' 这些都是作者用benchmark/benchmarking明确陈述的系统化基准比较。
- Benchmark 评价：在2021年中国河南洪水真实场景数据（来自3,496条微博帖子，识别出860条资源需求）上，以7月21-23日为训练数据、滚动请求至7月27日，评估CNM-PRR与ReR、logNormMix-PRR、A-NDTT-PRR、AttnMC-PRR、CTDRP-PRR、LR-NV、DL-NV、logNormMix-IFCFS等基准方法。结果显示CNM-PRR的平均单位剥夺成本为25.69美元，优于最佳基准A-NDTT-PRR 15.15%；平均时间延迟7.42小时，优于所有基准9.74%-62.11%；未来需求满足百分比0.80，优于最佳基准A-NDTT-PRR 8.55%。后续还进行消融分析（表7）和多利益相关者仿真（表8）进一步比较。
- 判定理由：客观指标方面：核心指标为平均单位需求剥夺成本、平均时间延迟、未来需求满足百分比（以及多目标仿真中的填充率和公平性标准差），这些指标均由可审计的时间戳、资源分配记录和确定性公式计算，不依赖任何人对质量、价值、偏好或感受的评判，属于完全客观的直接指标。唯一核心目标方面：论文的研究问题、方法设计和贡献声明均围绕“最小化延迟满足需求的成本”这一客观改进目标展开，新问题、新TPP模型和优化算法是服务于该目标的组成贡献，未发现并列的主观体验、理论机制或其他非客观核心目标。Benchmark方面：在Section 5.2明确使用benchmark/benchmarking陈述基准比较，并在Section 5.3和5.4中以真实数据和仿真数据对多个现有方法（ReR、logNormMix-PRR、A-NDTT-PRR、AttnMC-PRR、CTDRP-PRR、LR-NV、DL-NV、logNormMix-IFCFS）进行比较，报告了显著的成本、时间延迟和需求满足率改进；benchmark评价直接支撑核心客观指标提升的主张。因此两个模块均通过，strict_include为true。
- 置信度：0.95

### Customer Engagement Prediction on Social Media: A Graph Neural Network Method 

- 年份/期刊：2025 / Information Systems Research
- DOI：10.1287/isre.2021.0281
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：客户参与预测的准确率、精确率、召回率、F1分数和AUC
- Benchmark 状态：benchmark_comparison_central
- 参照点：MLP；DeepWalk；metapath2vec；GraphSAGE；RGCN；HAN；JODIE；MAGNN
- Benchmark 表述引文：4.3节实验部分明确写道：'Overall, GACE outperforms all seven benchmarks dramatically.' 此处将用于对比的baseline明确称为benchmarks，并随后用表3呈现完整比较结果。
- Benchmark 评价：在作者自建的大规模Facebook数据集（47个品牌、91,342用户、35,665帖子、666,188条互动记录）上，将GACE与MLP、DeepWalk、metapath2vec、GraphSAGE、RGCN、HAN、JODIE、MAGNN等baseline进行系统比较，报告accuracy、precision、recall、F1和AUC，并给出相对最优baseline的提升百分比（如准确率提升7.43%，AUC提升4.92%）。该比较构成支撑核心预测性能主张的关键证据。
- 判定理由：核心指标为客户参与预测性能，基于Facebook真实互动日志这一可审计事实，完全客观；研究的目标、评价和贡献均以客观预测指标提升为唯一核心，解释性和经济价值分析只是附加说明；虽然未使用公开命名benchmark，但作者在实验部分明确使用“benchmarks”指代baseline并进行系统比较，且该比较直接支撑GACE的预测性能提升主张，因此通过三部分审计。
- 置信度：0.85

### Ephemeral State-Dependent Recommendation for Digital Content 

- 年份/期刊：2025 / Information Systems Research
- DOI：10.1287/isre.2022.664
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：推荐书籍阅读率（readrate）；推荐书籍阅读时长（readtime）；支付金额（payment）；非推荐内容阅读量（spillover）
- Benchmark 状态：benchmark_comparison_central
- 参照点：C1（始终基于持久偏好同化推荐）；C2（始终基于持久偏好多样化推荐）；T1/T2（状态无关方案）；相应 Wald/F 检验
- Benchmark 表述引文：Table 2 在实验设计部分将 C1（always assimilation based on enduring preference）和 C2（always diversification based on enduring preference）明确标为 'Benchmark schemes'，并在 Table 4 等结果中作为比较基准。
- Benchmark 评价：在合作电子书平台的现场实验中，将两个状态依赖方案 T3/T4 与基准方案 C1/C2 及状态无关方案 T1/T2 比较；主要因变量为阅读率、阅读时长、支付和非推荐内容阅读量。结果称状态依赖方案显著优于状态无关方案，且 T4（congruent）整体优于 T3（incongruent）。
- 判定理由：核心成功指标均为平台可审计的阅读/支付/溢出计数，客观且为唯一核心目标；实验中使用明确标记的 Benchmark schemes（C1/C2）作为基准，并通过随机现场实验结果（Table 4 等）支持状态依赖推荐方案的客观指标提升，因此 strict_include=true。
- 置信度：0.63

### Fast Forecasting of Unstable Data Streams for On-Demand Service Platforms 

- 年份/期刊：2025 / Information Systems Research
- DOI：10.1287/isre.2023.0130
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：SMAPE（对称平均绝对百分比误差）；RMSE（均方根误差）；经济损失（货币化的预测误差）；计算时间（秒）和云计算成本（美元）
- Benchmark 状态：benchmark_comparison_central
- 参照点：Naive model；Facebook Prophet；LSTM；SARIMA；ETS；带break detection的LSTM/SARIMA/ETS
- Benchmark 表述引文：Section 5.3标题为“Benchmark Forecast Models”，明确将Naive、Prophet、LSTM、SARIMA、ETS列为基准模型；摘要中称“against several industry benchmarks”。
- Benchmark 评价：在UK按需配送平台294个区域的数据集以及NYC Citi Bike公共自行车系统数据集上，将FFUDS与Naive、Prophet、LSTM、SARIMA、ETS（部分加入break detection的变体）进行对比，报告预测误差和计算时间。
- 判定理由：本文开发FFUDS预测框架，其核心目标是提升预测准确性（SMAPE、RMSE、经济损失）和计算速度，所有核心成功指标均为客观可测量且不依赖主观判断；全文明确以benchmark形式比较FFUDS与多个基准方法（Naive、Prophet、LSTM、SARIMA、ETS），并有明确参照点和提升证据，因此同时满足客观指标唯一核心目标和明确benchmark表述。
- 置信度：0.97

### Gaining a Seat at the Table: Enhancing the Attractiveness of Online Lending for Institutional Investors 

- 年份/期刊：2025 / Information Systems Research
- DOI：10.1287/isre.2022.0638
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：内部收益率（IRR）；投资回报率（ROI）；公开市场等价（PME）；与基准指数的相关系数
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：S&P 500 Index；Bloomberg U.S. Aggregate Bond Index；S&P U.S. Treasury Bond Indexes (1–3, 3–5, 10–20 Year)；MSCI U.S. REIT Index
- 参照点：Equal-weight portfolio；Mean-variance portfolio (Guo et al. 2016)；Risk-filtering portfolio；Linear regression portfolio；Gradient-boosted regression portfolio；Neural network regression portfolio；Grade-specific equal-weight automated investing portfolios (EW-A to EW-G)；S&P 500 Index；Bloomberg U.S. Aggregate Bond Index；S&P 1–3/3–5/10–20-Year U.S. Treasury Bond Indexes；MSCI U.S. REIT Index
- Benchmark 表述引文：Section 3.4："We evaluate the out-of-sample portfolio performance of our GCPP framework, comparing it against various benchmarks, including equal-weight, mean-variance, credit risk-filtering, and regression-based portfolios." Section 5："We consider three benchmark assets: stocks, bonds, and real estate."
- Benchmark 评价：GCPP在LendingClub超过100万笔贷款样本上按月度样本外形成贷款组合，与等权组合、风险过滤组合、均值方差组合、线性/梯度提升/神经网络回归组合比较；并将贷款组合与S&P 500、美国综合债券、美国国债（1–3、3–5、10–20年）和REIT指数按相同现金流构造的指数组合进行比较，使用PME、相关系数和Pr(win)等客观指标。
- 判定理由：核心指标IRR、ROI、PME和相关系数均由贷款和指数实际现金流客观计算，不属于人类主观评价或语义判断；全文围绕GCPP组合提升样本外回报这一唯一核心目标展开，利益率偏差和金融普惠等仅为延伸含义；评价部分明确以各种基准组合和市场指数作为比较对象，比较结果直接支撑核心改进主张。因此客观指标模块和benchmark模块均通过，strict_include=true。
- 置信度：0.72

### Healthcare Cost Prediction for Heterogeneous Patient Profiles Using Deep Learning Models with Administrative Claims Data 

- 年份/期刊：2025 / Information Systems Research
- DOI：10.1287/isre.2021.0643
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：预测误差（MAPE/MAE）；支付差额（overpayment/underpayment/net pay）
- Benchmark 状态：benchmark_comparison_central
- 参照点：LR (Kuo et al. 2011)；RF (Sushmita et al. 2015)；CART (Bertsimas et al. 2008)；GBDT (Jödicke et al. 2019; Morid et al. 2019)；MLP (Osawa et al. 2020)；RNN (Zeng et al. 2021)；CNN (Morid et al. 2020)；Deep EHR/AC architectures: Rajkomar et al. (2018), Choi et al. (2016a), Choi et al. (2016b/Doctor AI), Ma et al. (2017/Dipole), Choi et al. (2016c/RETAIN)
- Benchmark 表述引文：Section 5.2 标题为“Benchmark Analysis”；5.2.1“Channel-Wise Learning Cost Prediction vs. Cost Prediction Methods in the Literature”，5.2.2“Channel-Wise Learning Cost Prediction vs. Non–Cost Prediction Methods in the Literature”。作者明确将多种已有模型作为benchmarks并在相同数据设置下比较MAPE。
- Benchmark 评价：在包含约111,000名Medicare患者的Utah数据集（以及外部California数据集）上评价channel-wise深度框架：与LR、RF、CART、GBDT、MLP、CNN (Morid et al. 2020)、RNN (Zeng et al. 2021)、Doctor AI、RETAIN、Dipole、Rajkomar等benchmark模型比较；结果报告MAPE等，channel-wise模型MAPE为46.8%，优于最佳基准CNN 62.3%等（Table 3、4）；并在高需求患者亚组中进行比较（Table 6）。
- 判定理由：文章唯一核心目标是提升医疗成本预测的客观性能指标（MAPE/MAE/支付差额），没有主观成功标准；评价建立在真实行政索赔数据上，明确设置了Benchmark Analysis章节，与多个文献模型进行系统比较，benchmark结果直接支撑预测误差和支付差额改善的核心主张，因此完全满足严格纳入条件。
- 置信度：0.96

### Post-Earnings-Announcement Drift Prediction: Leveraging Postevent Investor Responses with Multitask Learning 

- 年份/期刊：2025 / Information Systems Research
- DOI：10.1287/isre.2022.0358
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：预测性能：解释方差（EV）；经济收益：风险调整后日度超额收益（alpha）；预测目标：累计异常收益CAR(0,21)
- Benchmark 状态：benchmark_comparison_central
- 参照点：SUE；OLS；PEAD.txt；LSTM；Transformer；FinAux+GradPerp+Transformer；FinAux+Uncert+MQT；FinAux+GradCos+MQT
- Benchmark 表述引文：摘要：'our proposed design innovations not only outperform benchmark models in terms of prediction accuracy but also generate a daily risk-adjusted return (alpha) two to three times larger'；第5.1.1节标题：'Comparison with Benchmark Models on PEAD Prediction'；Table 6标题：'Description of the Benchmark and Proposed Models'。
- Benchmark 评价：作者在61,223个财报电话会议样本（2010–2022）上评估提出的FinAux+GradPerp+MQT模型，与来自金融与AI文献的SUE、OLS、PEAD.txt、LSTM、Transformer等基准模型进行预测性能（EV）比较，并在经济意义评价中比较各模型的alpha。结果显示FinAux+GradPerp+MQT在Russell 3000上取得最高EV（9.06%），显著高于所有非MTL基准模型。
- 判定理由：文章核心目标是以MTL框架提升PEAD预测的完全客观指标（预测EV、风险调整后alpha），全文评价与贡献声明均围绕这一目标，无任何主观构念或并列核心目标；实验部分在2010–2022大规模数据集上明确以benchmark models为参照，系统比较SUE、OLS、PEAD.txt、LSTM、Transformer等方法，报告EV和alpha提升，符合明确的benchmark表述和比较要求。因此两个模块全部通过，strict_include=true。
- 置信度：0.96

### Walrasian Pricing for Combinatorial Markets with Compact-Bidding Languages: An Application to Truckload Transportation 

- 年份/期刊：2025 / Information Systems Research
- DOI：10.1287/isre.2023.0676
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：总节省/相对节省；托运人与承运人剩余；残余嫉妒/偏离均衡
- Benchmark 状态：benchmark_comparison_central
- 参照点：VCG；SMRA（同时多轮拍卖）
- Benchmark 表述引文：Section 4 开篇：'For PAL, we benchmark our proposed procurement market design using IDP against VCG and a standard simultaneous multiround auction tailored for the truckload transportation market (see Online Appendix I for details).'；4.3.1：'We first present the results for PAL with only lane-bound constraints, where we benchmark VCG and IDP savings against SMRA.'
- Benchmark 评价：在基于真实参数生成的模拟卡车运输市场上，将 IDP 与 VCG 和 SMRA 对比：报告总节省、相对节省、托运人与承运人剩余和残余嫉妒；结果显示 IDP/VCG 相比 SMRA 有更高节省（13.4% vs 9.4%），IDP 保持托运人正剩余而 VCG 在高交换率下变负，clique cuts 使更多实例达到 envy-free。
- 判定理由：客观指标方面：核心结果指标（总节省、剩余、残余嫉妒）均为优化模型和成本参数直接推导出的货币/数学数值，不依赖人类感受或语义评价；唯一核心目标是提高经济效率并给出可实现的均衡价格，无并列的主观或理论核心目标。Benchmark 方面：全文在实验评价部分明确使用 benchmark 一词陈述对 IDP 与 VCG、SMRA 的系统化比较，且有明确参照点和数值提升，该 benchmark 结果直接支撑核心效率提升主张。因此 strict_include=true。
- 置信度：0.95

### Mitigating Exposure Bias for Recommendations in Physical Spaces: An Unbiased Pairwise Ranking Approach Using Spatial Movement 

- 年份/期刊：2026 / Information Systems Research
- DOI：10.1287/isre.2023.0100
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：Recall@N；DCG@N
- Benchmark 状态：benchmark_comparison_central
- 参照点：UserKNN；ItemKNN；BPR-MF；FPMC；CoFiSet；Context-BPR；Cat-MPR；Dist-MPR；GRU4Rec；JODIE；SSE-PT；Random；消融对照 UMPR-M 和 UMPR-U
- Benchmark 表述引文：第5.2节标题为“Benchmarks and Recommendation Performances”，正文明确写道：“To demonstrate the superior performance of our method, we selected several classic and state-of-the-art recommendation methods as benchmarks.”并在表4中报告“The recommendation performances of UMPR and the benchmark methods”。
- Benchmark 评价：在真实商场数据（北京大型购物中心，167,234条访问序列、175家门店）上采用 leave-one-out 评价，对候选门店排序并计算 Recall@1/3/5 与 DCG@3/5。作为对照的 benchmark 方法包括 UserKNN、ItemKNN、BPR-MF、FPMC、CoFiSet、Context-BPR、Cat-MPR、Dist-MPR、GRU4Rec、JODIE、SSE-PT 和 Random。结果显示 UMPR 在所有指标上最优，且相对各 benchmark 的改进幅度在表4中一一列出。
- 判定理由：客观指标方面：核心评价指标是基于真实门店到访记录的 Recall 与 DCG，数据来源为系统追踪行为，不依赖主观评价或语义判断，四个客观性门全部通过。唯一核心目标方面：研究问题、方法设计、实验评价和贡献声明均围绕“提高物理空间门店推荐性能”这一客观目标展开；增量收入与公平性属于附加分析，不构成并列核心目标。Benchmark 方面：第5.2节明确以 benchmark 一词描述系统化基线比较，并给出多个显式参照点（UserKNN、BPR-MF、GRU4Rec、SSE-PT 等），表4的结果直接支撑 UMPR 的核心性能提升主张，因此 benchmark 四个门全部通过。综上 strict_include=true。
- 置信度：0.93

### Toward Sustainable Electricity Markets: Capacity-Based Pricing for Electric Vehicle Smart Charging 

- 年份/期刊：2026 / Information Systems Research
- DOI：10.1287/isre.2023.0078
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：RMSE（实际充电负荷与目标需求曲线之间的均方根误差）；绝对负荷峰值（Peak）与峰均功率比（PAPR）；目标收入偏差（Revenue deviation / % Diff from target Ψ*）
- Benchmark 状态：benchmark_comparison_central
- 参照点：真实世界平坦定价（Real-world charging—flat pricing）；速率无关可变定价（Rate-independent—variable pricing）；递增分块定价（Increasing-block pricing benchmark）；期望目标曲线/目标收入（Desired profile / target revenue）
- Benchmark 表述引文：第6.4节标题为“Benchmarks”，开篇明确说“To evaluate the proposed artifact, we compare its efficacy against the following benchmarks.”；第3.4节也称会“benchmark them against well-established pricing methods”。这些表述位于评价语境，是本文核心证据。
- Benchmark 评价：在基于Power TAC规范构建的多智能体仿真测试平台上，将CBP-AH、CBP-AH-Distrib、CBP-CH、CBP-CH-Distrib四种配置与真实世界平坦定价、速率无关可变定价、递增分块定价等基准比较；三种场景目标分别是平坦充电曲线、弥补家庭负荷形成平坦总需求、匹配光伏发电曲线；使用RMSE、PAPR、峰值和收入偏差评价。结果显示CBP-CH接近最优（例如平坦场景RMSE=0.02、PAPR=1.07、Peak=1.03），均优于所有基准。
- 判定理由：本文核心目标是设计并验证一种容量定价IS构件，以客观、可测量的电网平衡指标（RMSE、峰值、PAPR）和收入偏差来评价其对EV充电负荷曲线的塑造能力。所有核心成功指标均为模拟/交易可审计的物理或财务量，不涉及主观感知或语义判断；该客观指标提升是全文唯一核心目标与贡献。全文存在明确的benchmark表述，且评价在实验/结果部分进行，基准对比（平坦定价、可变定价、递增分块定价）正是支撑核心改进主张的关键证据。因此满足全部审计条件。
- 置信度：0.96

### GANNET: A Machine Learning Approach to Document Retrieval 

- 年份/期刊：1994 / Journal of Management Information Systems
- DOI：10.1080/07421222.1994.11518048
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：Jaccard's score（Jaccard 匹配分数）
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：DIALOG 3,000篇测试库（自建测试集，非公开命名套件）
- 参照点：初始 Jaccard score（baseline）；仅 GA 优化（First GA score）；Gordon (1988) GA 约20%改进的文字比较
- Benchmark 表述引文：在‘System Implementation and Evaluation’和‘Evaluation Results’部分，作者写道‘Table 1 summarizes the results from our benchmark testing’；表1标题为‘System Benchmark Testing Results’，结论中再次称‘Our benchmark testing results confirmed...’。
- Benchmark 评价：作者从3,000篇 DIALOG 数据库中随机抽取30个测试案例（1、2、3、4、5、10篇文档各5例），对每个案例计算初始 Jaccard 适应度，运行首次 GA 得到 First GA score，再运行完整 GA/HP 周期得到 Final HP/GA score，统计改进百分比、CPU时间和选出文档数。
- 判定理由：核心成功指标是完全客观可计算的 Jaccard's score，不涉及用户满意度、专家评分或语义质量判断；研究目标、评价结构和贡献声明均围绕该系统在该指标上的提升展开，且没有并列的主观或理论核心目标。全文在评价部分明确使用 benchmark testing/System Benchmark Testing Results，属于陈述式系统化基准评价，并与初始分数和仅GA基线进行比较，用于证明核心提升主张。因此两部分均通过，strict_include=true。
- 置信度：0.88

### Software Cost Estimation Using Economic Production Models 

- 年份/期刊：1998 / Journal of Management Information Systems
- DOI：10.1080/07421222.1998.11518200
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：软件成本估算误差（MRE）；拟合优度（ASRE）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：Kemerer software project data set (Kemerer, 1987)
- 参照点：Intermediate COCOMO；SLIM；GCDT (Generalized Cobb-Douglas with time)；GCD (Generalized Cobb-Douglas)；附录中另与 Expert、Estor、Function Point 等模型比较
- Benchmark 表述引文：在 Review 部分，作者称 COCOMO 和 SLIM 'are used in many studies as the benchmark models'；在 Empirical Validation/Data 部分，作者明确写出 'The software project data set of Kemerer [16] is chosen to test the performance of the MSCM model against the COCOMO and SLIM models'。
- Benchmark 评价：在 Kemerer 数据集的 14 个项目上，将 MSCM 与 Intermediate COCOMO、SLIM、GCDT、GCD 比较拟合优度（ASRE：MSCM 15.13，GCDT 15.91，GCD 16.92，COCOMO 339.49，SLIM 21.67），并用留一法比较预测误差（平均 MRE：MSCM 50%，SLIM 53%，GCDT 62%，GCD 71%，COCOMO 593%），同时报告 25%-MRE、30%-MRE、50%-MRE 比例。
- 判定理由：文章核心目标是提出并验证一种软件成本估算模型，核心指标为成本估算误差 MRE 和拟合优度 ASRE，均为可由历史项目数据直接计算的客观指标；评价结构、摘要和结论都以 MSCM 的估算精度提升为核心，未将主观体验或独立的理论/政策贡献作为并列核心目标。benchmark 门槛满足：作者明确选择公开的 Kemerer 软件项目数据集作为评价场地，并与 COCOMO、SLIM、GCDT、GCD 等多个既有模型进行比较，比较结果支撑了核心提升主张。因此 strict_include=true。
- 置信度：0.83

### A Query-Driven Approach to the Design and Management of Flexible Database Systems 

- 年份/期刊：2002 / Journal of Management Information Systems
- DOI：10.1080/07421222.2002.11045739
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：查询处理时间（及衍生的PER/APT/MAD/MPD）
- Benchmark 状态：benchmark_comparison_central
- 参照点：Actual best assigned structures（top benchmark）；Inductive learning production rules；Inductive learning decision tree；Neural network prediction；Rough rules；Best individual structure；Worst individual structure
- Benchmark 表述引文：实验一步骤5：'Best assignment is theoretically the best one can achieve... We use it here as a top benchmarking measure.' 讨论部分：'In our analysis, the top benchmark was provided by considering the assignment of each incoming query to the structure that is most efficient at processing that query.'
- Benchmark 评价：在实验I和实验II中，作者将'实际最优分配'作为top benchmark（理论上限），在验证查询集上系统比较了归纳学习产生式规则、决策树、神经网络、粗略规则、最佳单结构和最差单结构；报告PER、APT、MAD、MPD并做统计检验。该benchmark表（表5/表8）与最佳单结构/最差单结构对照，直接支撑'灵活分配优于单一固定结构'的客观性能提升主张。
- 判定理由：客观指标方面：核心成功指标是查询处理时间和由时间衍生的效率率/偏差，均为系统可观测物理量，全文没有主观量表或人类语义评价。唯一核心目标是提升只读查询处理性能，实验、成本分析和贡献声明均围绕该目标。Benchmark方面：虽然没有使用公开命名的benchmark套件，但作者在实验评价部分明确使用benchmark概念，以'实际最优分配'作为top benchmark，并与多个明确参照点（最佳单结构、最差单结构、rough rules、学习模型）比较；benchmark表直接佐证核心性能提升主张，满足benchmark_comparison_central条件。因此strict_include=true。
- 置信度：0.75

### Evaluating and Tuning Predictive Data Mining Models Using Receiver Operating Characteristic Curves 

- 年份/期刊：2004 / Journal of Management Information Systems
- DOI：10.1080/07421222.2004.11045815
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：AUC（ROC曲线下面积）；期望误分类成本（expected misclassification cost）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：Statlog German credit data set
- 参照点：五个数据挖掘方法相互比较（NN、LR、LDA、DT、kNN）；ROC空间中的随机猜测对角线；默认阈值0.5；训练集与测试集结果比较
- Benchmark 表述引文：在Credit Evaluation Applications一节中明确命名数据集：“the German credit data set from the well-known Statlog project (see [19])”；后续Evaluation Results在该数据集的训练集和测试集上评价五个模型。
- Benchmark 评价：在Statlog German credit 数据集上开发NN、LR、LDA、DT和kNN模型，用ROC/AUC、期望成本、泛化性和鲁棒性比较模型；结果显示NN和LR的AUC最高，DT和kNN泛化较差，LR在多数成本情景下期望成本最低。该评价是支撑“LR/NN性能优越、阈值后调有效”核心主张的关键证据。
- 判定理由：客观指标方面，核心指标为AUC和期望误分类成本，均基于外部可核验的好坏贷款/信用风险事实标签和混淆矩阵计数计算，不依赖主观感知或语义评价；全文唯一核心目标是提升最小化误分类成本这一客观性能，且无并列主观或理论目标。Benchmark方面，文章明确命名公开的Statlog German credit数据集并将其作为主要评价场地，在该基准上对五种方法进行AUC和期望成本的系统比较，比较对象包括方法互比、随机对角线、默认阈值和训练/测试对照，benchmark结果直接支撑“LR/NN性能优越、后调阈值有效”的核心主张。因此两个模块均通过，strict_include为true。
- 置信度：0.86

### Preserving User Preferences in Automated Document-Category Management: An Evolution-Based Approach 

- 年份/期刊：2009 / Journal of Management Information Systems
- DOI：10.2753/mis0742-1222250404
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：聚类召回率（Cluster Recall）；聚类精确率（Cluster Precision）；F1测度；结构相似性（Structure Similarity）
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：Reuters-21578；ACM Digital Library corpus
- 参照点：CE；HA C；HA C+P
- Benchmark 表述引文：摘要明确写道：'as compared with those of associated salient techniques for benchmark purposes'；引言进一步说明：'We empirically evaluate CE2 using two real-world document corpora and two benchmark techniques, namely, CE and hierarchical agglomerative clustering (HA C)... include an extended HA C technique (i.e., HA C+P) for benchmark purposes'；结论再次称 CE 和 HAC 为 'performance benchmarks'，HAC+P 为 'benchmark'。
- Benchmark 评价：在 Reuters-21578 和 ACM 摘要语料库上，通过 Gaussian-3 到 Gaussian-6 分布创建 30 组合成的类别演化场景；对 CE2 与 CE、HAC 比较，对 CHE 与 HAC+P 比较；报告 PRT 曲线、最高 F1 值、p 值，并针对 CHE 额外比较结构相似性。结果整体显示 CE2/CHE 在多数场景下显著优于各自基准。
- 判定理由：核心指标（聚类召回率、聚类精确率、F1、结构相似性）均基于 Reuters/ACM 外部文档类别标签的确定性计算，不依赖人类主观评价或语义质量判断，属于客观固定事实标签上的性能提升；研究问题、设计与贡献声明都围绕 CE2/CHE 在文档类别重组中的客观有效性，不存在并列的主观或理论核心目标，符合唯一核心目标要求。全文多次明确使用 benchmark/performance benchmark 指称 CE、HAC、HAC+P 等对照技术，并在评价语境中报告比较结果，这些 benchmark 评价正是支撑核心提升主张的关键证据，且具有明确参照点与统计检验。因此 strict_include=true。
- 置信度：0.95

### Cost-Sensitive Learning via Priority Sampling to Improve the Return on Marketing and CRM Investment 【全文无benchmark字样-需人工复核】

- 年份/期刊：2012 / Journal of Management Information Systems
- DOI：10.2753/mis0742-1222290110
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：累积利润提升（Cumulative Profit Lift）；实际增量利润（Lifted Profit in Dollars）；响应提升/TPR提升（Response Lift / TPR Lift）
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：1998 Knowledge Discovery and Data Mining competition (KDD Cup 1998) dataset；2003 Duke University data mining competition customer churn dataset
- 参照点：Logistic regression (original imbalanced data)；Logistic regression (balanced by down-sampling)；Expected cost method [26]；AdaC2 [23]；Naive Bayes (original)；KDD Cup 1998 competition winner ($14,712 at 60% depth)；Previously published result ($15,329) [26]
- Benchmark 表述引文：Study 3 开头：“it is necessary to compare the performance of priority sampling with other methods using a popular data set that is available to the public and used in data mining competitions. The data set from the 1998 Knowledge Discovery and Data Mining competition is used in many studies.”（Study 3, Data and Method 上下文）；Study 2：“we also apply priority sampling to a well-known CRM data set ... the customer churn data set from the 2003 Duke University data mining competition.”（Study 2 开头）。
- Benchmark 评价：在KDD Cup 1998数据集上，priority sampling for logistic regression 在前两个十分位的profit lift达到882.4和571.6，显著高于logistic regression balanced（723.5/473.5）、expected cost（618.3/416.5）和AdaC2（544.4/312.9）；实际lifted profit在60%邮寄深度达$15,800，高于竞赛获胜者$14,712。在Duke 2003数据集上，priority sampling在top decile profit lift为299.7（logistic regression）和301.4（naive Bayes），lifted profit为$18,634和$18,794，均高于AdaC2等的$18,355。这些benchmark结果直接支撑核心客观指标（利润提升）的核心主张。
- 判定理由：客观指标方面：文章以利润提升、实际增量利润、响应/TPR提升等为评价指标，全部基于真实交易金额、成本和事实标签，不依赖人类主观感知或语义评价，属于完全客观可直接观测的指标。唯一核心目标：全文的研究问题、算法设计、评价和贡献声明均围绕提高营销/CRM投资回报这一客观利润指标，没有并列的主观结果或理论机制等作为同等核心贡献。Benchmark方面：文章虽未使用“benchmark”一词，但在Study 2和Study 3明确命名了公开数据挖掘竞赛数据集（2003 Duke University competition、1998 KDD Cup）作为评价场地，并在这些benchmark上比较了多个基线方法（logistic regression、expected cost、AdaC2、naive Bayes）和竞赛获胜者，benchmark结果直接支撑“priority sampling提升利润”的核心主张。因此两个模块均通过，strict_include为true。
- 置信度：0.97

### Combining Geographical and Social Influences with Deep Learning for Personalized Point-of-Interest Recommendation 

- 年份/期刊：2018 / Journal of Management Information Systems
- DOI：10.1080/07421222.2018.1523564
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：Precision@K / Recall@K / F1@K 推荐准确率
- Benchmark 状态：benchmark_comparison_central
- 参照点：Geo-CF；Geo-PFM；RBM；Semi-DAE（本文模型去掉社交条件层）；CDAE（本文模型去掉 semi-RBM 层）
- Benchmark 表述引文：Discussion 部分在评价语境中使用 benchmarks 指代基线算法并支撑核心提升主张，例如：‘our proposed method performed better than the benchmarks for all four groups’；‘We evaluated the performances of our algorithm and the benchmarks for the two split datasets’。实验部分亦明确以 baseline algorithms 进行比较。
- Benchmark 评价：在三个真实 Foursquare 数据集（纽约、布鲁克林、旧金山）上，以 Precision@K/Recall@K/F1@K 为评价指标，将所提 Semi-CDAE 与 Geo-CF、Geo-PFM、RBM 以及消融变体 Semi-DAE、CDAE 进行比较；结果显示大多数情况下所提方法相对基线提升超过10%。
- 判定理由：该文以提升 POI 推荐准确率为唯一核心目标，使用 Precision/Recall/F1 等完全客观、可审计的指标，在真实 Foursquare 数据集上与多个基线和消融模型比较；讨论部分多次在评价语境中使用 benchmarks 指代基线算法，且这些比较是支撑核心提升主张的关键证据，因此通过客观指标与 benchmark 双门槛。
- 置信度：0.78

### Leveraging Financial Social Media Data for Corporate Fraud Detection 

- 年份/期刊：2018 / Journal of Management Information Systems
- DOI：10.1080/07421222.2018.1451954
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：准确率 (Accuracy)；召回率 (Recall)；F1分数 (F1 Score)；AUC
- Benchmark 状态：benchmark_comparison_central
- 参照点：仅使用财务比率的基线模型（financial ratios only）；仅使用MD&A语言特征的基线模型（language-based features from MD&A）
- Benchmark 表述引文：讨论与结论部分："In addition, we benchmark the performance of our model against those that use just the financial ratios and/or language-based features from MD&A sections, and demonstrate that social media features perform better in our data set."（此外，我们将模型的性能与仅使用财务比率和/或MD&A语言特征的模型进行基准比较，并表明社交媒体特征在我们的数据集中表现更好。）
- Benchmark 评价：在自建欺诈检测数据集（64家欺诈公司 + 64家匹配非欺诈公司；取自SeekingAlpha文本、财务比率和MD&A）上，作者将提出的社交媒体特征模型与两类基线进行系统比较：仅使用84项财务比率的模型，以及仅使用MD&A语言特征的模型。最优SVM模型在测试集上的准确率75.50%（仅社交媒体特征）和80.00%（全特征组合）；仅财务比率基线最优SVM测试准确率56.17%；仅MD&A语言特征基线最优LR测试准确率70.33%。该比较直接支撑“社交媒体特征能提升公司欺诈检测”的核心主张。
- 判定理由：文章以提升公司欺诈检测的客观性能（accuracy/recall/F1/AUC）为唯一核心目标和核心贡献，欺诈标签来自AAER外部事实性执法记录，属于objective_fixed_factual_labels。模型在自建数据集上与仅财务比率、仅MD&A语言特征两类基线进行系统比较，讨论部分明确使用benchmark一词指称该比较，且比较结果用于支持“社交媒体特征提升欺诈检测性能”的核心主张，满足benchmark_comparison_central。适用性检查中的焦点小组主观反馈仅为非核心补充验证，不影响核心目标的客观唯一性。
- 置信度：0.93

### A Novel Recommendation Model for Online-to-Offline Service Based on the Customer Network and Service Location 【全文无benchmark字样-需人工复核】

- 年份/期刊：2020 / Journal of Management Information Systems
- DOI：10.1080/07421222.2020.1759927
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：F-Score；Precision；Recall
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：MovieLens 100K
- 参照点：CF methods；H-CF；MF；DL；CL；NN
- Benchmark 表述引文：Experiments部分原文：'we compare our proposed models with widely-used and state-of-the-art recommendation methods on our O2O data set and the MovieLens 100K, respectively.' MovieLens 100K是被明确命名的公开标准推荐数据集，并作为评价场地。
- Benchmark 评价：在MovieLens 100K上，将CNLRec和CNRec与广泛使用的CF方法及MF、DL、CL、NN等state-of-the-art方法比较，报告不同训练集密度下的F-Score、Precision、Recall；结果显示CNRec/CNDRec在低密度数据上显著优于基线方法。O2O Dianping数据也用于同类比较。
- 判定理由：客观指标方面，核心成功指标为F-Score、Precision、Recall，基于留出评分/服务使用记录客观计算，不依赖用户主观评价，且客观指标提升是全文唯一核心目标与贡献；benchmark方面，文章在Experiments中明确使用公开标准数据集MovieLens 100K作为评价场地，并与CF、MF、DL、CL、NN等显式基线比较，比较结果直接支撑CNLRec/CNRec的核心性能提升主张。两个模块均通过，因此strict_include=true。
- 置信度：0.92

### Estimating Network Effects in Two-Sided Markets 

- 年份/期刊：2020 / Journal of Management Information Systems
- DOI：10.1080/07421222.2019.1705509
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：预测准确率：买家和卖家数量的平均绝对百分比误差（MAPE）
- Benchmark 状态：benchmark_comparison_central
- 参照点：传统净变化模型（net change model）
- Benchmark 表述引文：摘要原文：“The authors propose an influx-outflow model for doing so and conduct a simulation study to benchmark the new model against the traditional model.” 位置：ABSTRACT。
- Benchmark 评价：作者构建了84,672个模拟双边市场，系统改变网络效应参数与误差水平，将传统净变化模型（net change model）和新提出的流入-流出模型（influx-outflow model）在同一数据上校准并预测，核心比较指标为买家和卖家数量的MAPE。结果显示流入-流出模型平均MAPE显著更低（买家11.63% vs 16.12%，卖家24.55% vs 48.02%），Wilcoxon符号秩检验p<.01；另用logistic回归考察在何种条件下净变化模型更优。该模拟benchmark是支持“新模型提升网络效应估计/预测性能”的核心证据。
- 判定理由：客观指标门槛：核心目标是提出流入-流出模型，并通过大规模模拟证明其在预测客户数量和恢复真实网络效应参数上优于传统净变化模型；MAPE、参数恢复、Wilcoxon检验等全部为客观可计算指标，不涉及主观感受或语义评价，且客观性能提升是唯一核心目标和贡献。Benchmark门槛：摘要明确使用benchmark一词陈述“将新模型与传统模型进行基准比较”，相应模拟比较位于评价语境，比较对象明确（传统净变化模型），其结果直接支撑核心提升主张。因此两个模块均通过，strict_include=true。
- 置信度：0.82

### Human Identification for Activities of Daily Living: A Deep Transfer Learning Approach 

- 年份/期刊：2020 / Journal of Management Information Systems
- DOI：10.1080/07421222.2020.1759961
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：人身份识别准确率/精确率/召回率/F1/AUC
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：HANDY (公开可穿戴传感器数据集，参考文献标题标注为Benchmark dataset)；OPPO/Opportunity (公开对象传感器数据集)
- 参照点：kNN w/Signal Features；SVM w/Signal Features；NB w/Signal Features；DT w/Signal Features；CNN-HID；CNN-HID/T；CNN-HID/CA；DTL-HID/T；DTL-HID/CA
- Benchmark 表述引文：摘要：'We rigorously evaluate the DTL-HID framework against state-of-the-art benchmarks (e.g., k Nearest Neighbors, Support Vector Machines, and alternative CNN designs).'；Evaluation Design：'Design science research emphasizes the importance of rigorously evaluating the proposed artifact to confirm its technical superiority against well-established benchmarks.'；Table 6中设置'Benchmarks'列，列出kNN、SVM、NB、DT和替代CNN模型。
- Benchmark 评价：在HANDY（30受试者可穿戴传感器）和OPPO的四个对象传感器目标域（Glass、Cup、Spoon、Bread）上，将DTL-HID/CNN-HID与kNN、SVM、NB、DT、CNN-HID/T、CNN-HID/CA、DTL-HID/T、DTL-HID/CA等基准模型比较，报告accuracy、precision、recall、F1和AUC。实验结果显示DTL-HID在多数比较中显著优于所有非迁移基准和替代迁移框架。
- 判定理由：客观指标方面，HID任务是对固定身份事实标签的分类，准确率/精确率/召回率/F1/AUC是从预测与真实身份标签确定性计算，不依赖主观感受；研究问题和全部实验围绕提升对象传感器HID性能，属于唯一核心目标。Benchmark方面，摘要和Evaluation Design明确使用benchmarks进行系统比较，表7-10及结果部分比较了DTL-HID与多个baseline和替代模型，并以其客观指标提升作为核心证据。两个模块均通过，因此strict_include=true。
- 置信度：0.9

### Semi-Supervised Cyber Threat Identification in Dark Net Markets: A Transductive and Deep Learning Approach 

- 年份/期刊：2020 / Journal of Management Information Systems
- DOI：10.1080/07421222.2020.1790186
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：F1-score；Precision / Recall；Accuracy；AUC
- Benchmark 状态：benchmark_comparison_central
- 参照点：k-NN；Logistic Regression；Random Forest；SVM；CNN；LSTM；TSVM；不使用半监督标注的LSTM基线
- Benchmark 表述引文：在“Method evaluation”一节中写道：“we design several experiments to evaluate the efectiveness of our model versus several state-of-the-art benchmark methods.” 这表明作者明确以基准方法比较作为系统化评价。
- Benchmark 评价：在自建的79,434条DNM产品数据集上开展实验，将提出的TSVM+LSTM与k-NN、LR、Random Forest、SVM、CNN、LSTM、TSVM等基准方法比较，报告准确率、精确率、召回率、F1和AUC；提出方法F1=89.55%，优于所有基准，且t检验显著。
- 判定理由：文章核心目标是在暗网市场产品描述中提升网络威胁自动识别的分类性能，所有核心结果均为F1、精确率、召回率、准确率、AUC等外部事实标签上的客观指标；没有主观量表或并列主观目标。评价部分明确把k-NN、LR、RF、SVM、CNN、LSTM、TSVM等称为state-of-the-art benchmark methods，并在该基准比较中证明提出方法的核心性能提升。因此三个条件均满足，strict_include=true。
- 置信度：0.9

### First, Do No Harm: Predictive Analytics to Reduce In-Hospital Adverse Events 

- 年份/期刊：2021 / Journal of Management Information Systems
- DOI：10.1080/07421222.2021.1990619
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：住院不良事件（AE）预测的 AUC、精确率、召回率、F-score；模拟应用中预防的 AE 数与假警报数、成本节省金额
- Benchmark 状态：benchmark_comparison_central
- 参照点：GLMM；MERT；MERF；CART；DNN；GBM；LR；NB；RF；SVM
- Benchmark 表述引文：Evaluation 1 结果中明确写道：“Overall, we find that SALT outperforms the alternative models in AUC across all AE categories and training periods... it should be noted that... we find that SALT tends to perform better than the benchmarks, especially in recall.” 这里“benchmarks”明确指代所比较的既有 mixed effects 模型（GLMM、MERT、MERF）。Evaluation 2 又比较了 CART、DNN、GBM、LR、NB、RF、SVM 等替代技术。
- Benchmark 评价：在佛罗里达 AHCA 心衰住院数据测试床上，采用时间前后分割，比较 SALT 与多个基准/替代模型在 AUC、F-score、precision、recall 上的表现，并用模拟评估预防 AE 与假警报；这些对比是证明 SALT 预测性能提升和实践价值的关键证据。
- 判定理由：客观指标方面：文章核心目标是预测住院期间由医疗错误导致的不良事件（AE），标签基于高 PPV 的 ICD 编码和 POA 指示，是可核验的医疗事实；所有主要成功指标（AUC、precision、recall、F-score、预防 AE 数、假警报数、成本节省）均客观可计算，不依赖主观体验或语义评价。唯一核心目标：研究问题、设计目标、评价实验与贡献声明均围绕提高 AE 预测性能和相应的客观临床/经济效用展开，没有并列的主观成功标准或理论解释核心目标。Benchmark 方面：正文实验部分明确将比较对象称为“benchmarks”，并且系统比较了 GLMM、MERT、MERF、CART、DNN、GBM、LR、NB、RF、SVM 等基线/替代方法，结果用于支撑 SALT 预测性能提升这一核心主张，存在明确参照点。因此两个模块均通过，strict_include=true。
- 置信度：0.85

### Discovery of Technological Innovation Systems: Implications for Predicting Future Innovation 

- 年份/期刊：2024 / Journal of Management Information Systems
- DOI：10.1080/07421222.2023.2301172
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：未来专利数量（Future Patenting）；未来引用数量（Future Citations）；TIS Score / Patent Capital（企业层面）
- Benchmark 状态：benchmark_comparison_central
- 参照点：Past（仅过去专利/引用）；Past+Cite（增加引文相关创新CRTI，基于Acemoglu et al. [1]的文献基准）；Past+Cite+Innov（加入作者提出的TIS创新指标）
- Benchmark 表述引文：在Innovation Metrics节中：'The citation-based predictor also serves as an important benchmark from the literature for machine learning-based prediction experiments.' 在Predictive Modeling节中：'Past patenting (Past or PP) and Citation-based Related-tech Innovation (Cite or CRTI) are important benchmarks based on previous literature [1].'
- Benchmark 评价：文章在自建的USPTO专利数据集上进行了两个预测任务：未来专利数量（Task 1）和未来引用数量（Task 2）。以Past（过去专利或引用）和Past+Cite（加入引文相关创新CRTI）作为基准特征集，用LASSO、CART、RF、XGBoost、LSTM等模型评估增加作者提出的创新指标（RTI/BSI/RTIQ）后的预测绩效，采用RMSE、RRSE、R²。结果显示加入创新指标后LSTM和树模型显著提升（如LSTM的RMSE提升40.11%，p<0.0001）。
- 判定理由：客观指标：核心成功指标为专利数量、引用数量和基于市场的专利资本，均为客观可审计事实，不涉及主观感受或语义评价。唯一核心目标：全文围绕TIS发现框架及其对预测客观创新指标（数量和质量）的提升展开，无并列的主观或理论核心贡献。Benchmark：作者明确使用benchmark一词指代Past和CRTI等文献基准，并在预测任务中通过多个模型和明确对照比较证明TIS创新指标带来显著提升。因此三个门槛均通过。
- 置信度：0.92

### Complex Problem Solving: Identity Matching Based on Social Contextual Information 

- 年份/期刊：2007 / Journal of the Association for Information Systems
- DOI：10.17705/1jais.00141
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：精确率 Precision；召回率 Recall；F-measure
- Benchmark 状态：benchmark_comparison_central
- 参照点：personal-features-only (Fp) baseline；不同数据不完整程度下同一方法自身的对比
- Benchmark 表述引文：在 Experiments 部分，作者写道：“we compared the performance for using both personal and social features with that for using personal features only, which could be regarded as a benchmark.” 即明确把仅用个人特征的条件称为基准。
- Benchmark 评价：在 Tucson Police Department 的 Meth World 真实毒品犯罪数据集上，以 Fp（个人特征）作为基准，评价 Fp+Fs（加入社会特征）的身份匹配效果；采用 10 折交叉验证计算 precision/recall/F-measure，并通过 t 检验和回归分析比较性能差异。
- 判定理由：客观指标方面：文章核心评价目标是身份匹配的 precision/recall/F-measure，真值由 SSN 金标准确定，属于客观固定事实标签，全部核心成功结果均为客观指标。唯一核心目标方面：研究问题、设计目标、评价结构和贡献声明均围绕“改进身份匹配方法有效性”展开，没有并列的主观或理论机制核心目标；Mumford 框架和设计科学定位是背景与意涵。Benchmark 方面：作者在实验部分明确将“仅用个人特征”的条件称为 benchmark，并在该基准上比较加入社会特征后的性能，比较对象明确、位于评价语境、服务于核心提升主张。因此 strict_include=true。
- 置信度：0.9

### Combining Information Seeking Services into a Meta Supply Chain of Facts 【全文无benchmark字样-需人工复核】

- 年份/期刊：2008 / Journal of the Association for Information Systems
- DOI：10.17705/1jais.00154
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：精确答案MRR（Mean Reciprocal Rank）；句子级MRR；响应时间/等待时间
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：TREC 2004 factoid question set（Text Retrieval Conference公开QA任务）
- 参照点：START、AskJeeves、BrainBoost、ASU QA、Wikipedia等单一事实检索服务；Google、MSN及Google+MSN关键词门户组合；排除单个服务的完整配置；same weights、no patterns、no semantic verification等消融配置
- Benchmark 表述引文：第六节“Test Sets”中明确写道：“We used all the factoid questions from the entire set of questions used by TREC 2004.”，并在摘要中称评价使用“standard test sets widely used in prior research”。
- Benchmark 评价：在TREC 2004的200道factoid问题上评价meta fact seeking engine，报告精确答案MRR和句子级MRR；完整meta配置的MRR为0.484（精确）和0.630（句子级），并将其与每个单一服务（START、AskJeeves、BrainBoost、ASU QA、Wikipedia）、关键词门户（Google、MSN、Google+MSN）以及排除/消融配置进行比较。
- 判定理由：该文核心目标是构建和验证一种元事实检索引擎，通过组合多个在线事实服务提升答案准确性、响应时间与鲁棒性。所有核心研究问题均围绕可客观测量的MRR和响应时间，评价在TREC 2004公开QA任务上进行，并以完整meta配置对比单一服务、关键词门户和消融配置，给出统计显著性。因此满足客观指标唯一核心目标和明确benchmark评价门槛。
- 置信度：0.92

### An Information Diffusion-Based Recommendation Framework for Micro-Blogging 

- 年份/期刊：2011 / Journal of the Association for Information Systems
- DOI：10.17705/1jais.00271
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：故事覆盖率 (Story Coverage, SC)；阅读负担 (Reading Effort, RE)；延迟时间 (Delay Time, DT)
- Benchmark 状态：benchmark_comparison_central
- 参照点：HITS (Authority)；HITS (Hub)；Google Site Search；Twitter Find People；# of Followers heuristic；# of Tweets heuristic
- Benchmark 表述引文：摘要：'compared to benchmark approaches'；4.3节：'we also selected another six recommended sets using benchmark methods'、'The performances of benchmark methods are also illustrated in Table 3 and Figure 6'；5.1节：'our method outperformed other benchmark approaches'。
- Benchmark 评价：作者在自行收集的Twitter H1N1数据集上，用第一周推文训练推荐、后两周推文测试，将扩散推荐方法与HITS(Authority)、HITS(Hub)、Google Site Search、Twitter Find People、最多粉丝、最多推文六种基准方法比较，报告SC、RE、DT、Recall、Precision和扩展F*。扩散方法在全部四种参数设置下的F*均高于所有基准。
- 判定理由：客观指标方面：核心评价指标SC、RE、DT和扩展F*均为可由推文时间戳、内容计数和自动聚类可复算的客观量，不依赖人类主观评价或语义评分；全文研究问题、设计目标、评价和贡献声明均围绕这些指标的提升。唯一核心目标虽然包含新方法框架，但该方法学成分是实现指标改进的手段，未构成并列核心贡献。Benchmark方面：作者虽未使用公开命名数据集，但在摘要、4.3节和结论中反复以benchmark methods/approaches明确陈述系统化基准比较，并提供了6种明确对照方法；该基准比较在评价语境中作为证明核心改进主张的关键证据。故两个模块均通过，strict_include=true。
- 置信度：0.82

### Who Is the Next “Wolf of Wall Street”? Detection of Financial Intermediary Misconduct 

- 年份/期刊：2020 / Journal of the Association for Information Systems
- DOI：10.17705/1jais.00633
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：分类准确率（Accuracy）；召回率（Recall）；精确率（Precision）；F1分数；AUC（ROC曲线下面积）；经济收益（Economic gain）
- Benchmark 状态：benchmark_comparison_central
- 参照点：Classifier A（仅自我披露信息）；Classifier B（自我披露+用户确认信息）；Naive classification algorithm（按历史不当行为比例6.83%随机分类）
- Benchmark 表述引文：Table 11标题：'McNemar's Test Results on Classifier Performance for Classifiers Using Self-Disclosed as Well as User and Regulator-Confirmed Information Compared to Classifiers A and B as Benchmarks (Naturally Distributed Sample)'——作者明确将Classifier A（仅自我披露信息）和Classifier B（自我披露+用户确认信息）命名为基准（Benchmarks），并报告McNemar检验的比较结果；Table D5标题亦有类似用法。
- Benchmark 评价：在自然分布测试样本（N=2051，6.87%不当行为）上，将结合监管确认信息的分类器（C和D）与仅含自我披露信息/用户确认信息的基准分类器（A和B）进行性能比较。结果显示C和D在绝大多数机器学习方法和指标上显著优于A和B（如表11中多项p<0.01），证明监管确认信息显著提升检测性能（支撑H3）。此外，各分类器还与naive随机分类基线比较，证明自我披露信息本身有检测价值（支撑H1）。
- 判定理由：客观指标方面：核心结果是检测金融中介不当行为的分类性能（accuracy、recall、precision、F1、AUC）及基于实际赔偿金额的经济收益，标签来自FINRA BrokerCheck的最终客户投诉和监管行动记录，属于可脱离人的感受和语义评价而成立的事实标签（objective_fixed_factual_labels）。核心目标唯一：研究问题、评价结构和贡献声明均围绕自动检测分类器的构建与性能提升；信息操纵理论和保证理论作为特征选择依据，其确认通过分类性能实现，是解释性而非并列核心贡献。Benchmark方面：全文在评价语境中存在明确的benchmark标识——Table 11和Table D5标题明确将Classifier A和B（及E/F）命名为'Benchmarks'并进行McNemar检验，该比较结果正是证明结合监管确认信息的分类器性能提升的关键证据，且存在明确参照点。因此两项门槛均通过，strict_include=true。
- 置信度：0.75

### GASP: A Graph Augmentation-Based Approach for Sign Prediction of Ties in Social Networks 

- 年份/期刊：2025 / Journal of the Association for Information Systems
- DOI：10.17705/1jais.00941
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：准确率；优化精度；宏平均F1；特异性与负预测值的几何均值
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：Epinions；Wikipedia Requests for Adminship (RfA)；Slashdot Zoo；Yeast Genetic Interaction Network (GIN)
- 参照点：NPECF；SRWR；ASiNE；DDRE
- Benchmark 表述引文：摘要中明确写道：‘The benchmarking networks used for experiments originate from online platforms such as Slashdot, Epinions, Wikipedia, and the Yeast Genetic Interaction Network from the biology domain.’ 第5.1节标题为‘Benchmark Datasets Used for Comparison’，并明确：‘To perform benchmarking experiments, we utilized four different datasets—namely Epinions, Wikipedia Requests for Adminship (RfA), Slashdot Zoo, and the Yeast Genetic Interaction Network (GIN).’
- Benchmark 评价：在Epinions、Wikipedia RfA、Slashdot Zoo、Yeast GIN四个公开基准网络上，以不同比例标注边（60%-80%）评估GASP，并与NPECF、SRWR、ASiNE、DDRE四个SOTA方法比较。平衡数据集使用accuracy和optimized precision，不平衡数据集使用macro F1和GM(特异性, NPV)。结果显示GASP在绝大多数设定下均优于其他方法。
- 判定理由：客观指标方面：核心成功指标为边符号预测的accuracy、optimized precision、macro F1和GM，均基于数据集中已有的离散标签计算，不依赖人主观评分或语义评价，属于客观固定事实标签上的分类性能。唯一核心目标方面：研究问题、设计目标、评价和贡献均围绕‘提升符号预测性能’，理论/实践贡献为附属论述，未构成并列核心成功标准。Benchmark方面：全文存在明确的benchmark表述（摘要和Section 5.1），在评价语境中使用，在命名公开基准数据集（Epinions、Wikipedia RfA、Slashdot Zoo、Yeast GIN）上评价GASP并与NPECF、SRWR、ASiNE、DDRE等明确参照点比较，benchmark结果直接支撑核心性能提升主张。因此strict_include=true。
- 置信度：0.87

### How Do Enterprise Resource Planning Systems Affect Firm Risk?  Post-Implementation Impact 

- 年份/期刊：2002 / MIS Quarterly
- DOI：10.25300/misq/2015/39.1.03
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：企业风险（盈利波动性）
- Benchmark 状态：benchmark_comparison_central
- 参照点：无ERP企业（未安装ERP系统）；R&D支出（效应量比较基准）
- Benchmark 表述引文：Results效应量部分：'We chose R&D spending, which has been generally considered to be a major risk factor, as a benchmark'；Robustness Checks/Appendix C：'using firms with no ERP systems as a benchmark.'
- Benchmark 评价：在样本分割稳健性检验（Appendix C）中，以无ERP企业为基准组，分别估计ERP系统范围L1-L4对企业风险的系数，结果显示各层级均显著降低风险，为风险降低主张提供基准比较证据；在效应量分析中，以R&D支出为基准比较效应量，说明ERP风险降低效应的经济意义。
- 判定理由：客观指标方面：企业风险（盈利波动性）由Compustat财务数据经固定规则计算，不涉及主观评价；全文研究问题、假设、评价和贡献均围绕ERP是否降低企业风险及条件效应，构成客观指标提升的唯一核心目标。Benchmark方面：作者在评价语境中明确使用了benchmark一词，在Appendix C中以无ERP企业为基准组进行样本分割比较，并以R&D支出为效应量比较基准；该基准比较用于支持ERP风险降低的核心主张，且存在明确参照点。因此两个模块均通过。
- 置信度：0.7

### A Cost-based Database Request Distribution Technique for Online e-Commerce Applications 

- 年份/期刊：2012 / MIS Quarterly
- DOI：10.2307/41703464
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：应用响应时间；应用吞吐量
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：TPC-W
- 参照点：Round-Robin (RR)；Lowest CPU (LCPU)；Greatest Free Memory (FMEM)；SQL Server 2005 clustering（现场实验）
- Benchmark 表述引文：实验平台部分：'We used the TPC-W benchmark from the Transaction Processing Council, a standard web benchmark for e-commerce systems, for our experiments.' 实验方法部分：'based on the TPC-W benchmark specification'。
- Benchmark 评价：在TPC-W模拟的电子商务（书店）环境上，将C-DBRD与RR、LCPU、FMEM三种现有请求分布策略进行对比，随模拟用户数增加测量平均响应时间和吞吐量；结果显示C-DBRD在高负载下响应时间比最佳对比方法FMEM降低约45%，吞吐量高出近50%。另有生产级现场实验比较C-DBRD与SQL Server 2005 clustering及RR。
- 判定理由：客观指标方面，文章完全依赖响应时间和吞吐量这类物理可测、可由工具和系统日志客观记录的结果指标，没有使用满意度、感知价值或语义评分等主观构念作为成功标准；唯一核心目标是通过请求分布技术提升数据库层资源利用率，理论模型和实现方法都服务于这一客观改进。Benchmark方面，全文在实验部分明确使用公开标准benchmark TPC-W作为评价场地，并在同一评价语境中与RR、LCPU、FMEM等明确参照点比较，benchmark结果直接支撑45%响应时间改进等核心贡献主张。因此同时满足客观指标门槛和benchmark门槛，strict_include应为true。
- 置信度：0.95

### Digression and Value Concatenation to Enable Privacy-Preserving Regression 【全文无benchmark字样-需人工复核】

- 年份/期刊：2012 / MIS Quarterly
- DOI：10.25300/misq/2014/38.3.03
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：敏感值披露风险（RSD）；回归预测误差（MAPE）；运行时间
- Benchmark 状态：named_public_benchmark_central
- 命名 Benchmark：UCI Credit dataset (Bache and Lichman 2013)；UCI Census dataset (Bache and Lichman 2013)
- 参照点：regression Mondrian (RM) (LeFevre et al. 2008)；classical k-anonymity baseline (Sweeney 2002)；Original un-anonymized data
- Benchmark 表述引文：Experimental Study 部分明确使用 Credit 数据集（Bache and Lichman 2013，UCI 公开数据集）和 Census 数据集（Bache and Lichman 2013）作为评价场地，并与现有技术比较。虽未出现 'benchmark' 一词，但属于命名式公开 benchmark 数据集表述。
- Benchmark 评价：在 Credit、Census 以及 Offer、Alcohol 等真实数据集上，通过 10 折或 2 折交叉验证比较 MART 与 regression Mondrian（RM）、经典 k-anonymity baseline；报告 RSD、线性回归 MAPE、回归树 MAPE 与运行时间。结果用于证明 MART 在相同 k 值下披露风险更低，且回归数据效用更好。
- 判定理由：文章核心目标是降低回归攻击下的敏感值披露风险并保持回归分析的数据效用，两者均通过 RSD、MAPE、运行时间等完全客观可测量的指标评价；实验在 UCI Credit、UCI Census 等公开数据集上进行，并与 RM、k-anonymity baseline 明确比较，benchmark 评价直接支撑核心改进主张。因此两个模块均通过，strict_include=true。
- 置信度：0.82

### Mining Massive Fine-Grained Behavior Data to Improve Predictive Analytics1 

- 年份/期刊：2016 / MIS Quarterly
- DOI：10.25300/misq/2016/40.4.04
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：AUC（ROC曲线下面积）；Lift（针对1%、5%、10%目标群体的提升度）
- Benchmark 状态：benchmark_comparison_central
- 参照点：BeSim模型（基准）；SD模型（使用289个传统结构化变量的线性SVM）；BeSim+SD组合模型；SVM（基于细粒度行为数据）；不同BeSim变体（ICF、NSNC、NS、S1、SB,AUC、SB,Lift）
- Benchmark 表述引文：在“行为相似度与传统结构化建模”的分析设置部分，作者写道：Tables 4 and 5 ... following the procedures described above, and using the BeSim model as a benchmark（将BeSim模型作为基准）。该表述位于结果评价语境，是本文模型比较的明确基准陈述。
- Benchmark 评价：在银行真实客户数据（非公开专有数据）上，将BeSim模型作为基准，与结构化数据模型（SD）及组合模型（BeSim+SD）在AUC和lift@1/5/10%上进行比较，结果显示组合模型在多数指标上显著优于基准和SD模型，BeSim在lift@1%上显著优于SD模型。
- 判定理由：核心成功指标是客户是否实际购买金融产品的客观事实标签上的AUC和lift，全部核心目标围绕预测性能提升，没有主观构念或并列核心贡献。虽然未使用公开基准数据集，但在结果评价部分明确将BeSim模型作为benchmark，并与SD、SVM、组合模型等明确参照点比较，基准评价直接支撑核心预测性能提升主张。因此两个模块均通过，strict_include=true。
- 置信度：0.84

### The Making of a Good Impression: Information Hiding in Ad Exchanges 

- 年份/期刊：2016 / MIS Quarterly
- DOI：10.25300/misq/2016/40.3.10
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：广告交易平台每场拍卖的期望收益（expected revenue per auction）
- Benchmark 状态：benchmark_comparison_central
- 参照点：optimal policy（枚举最优策略）；mixing hiding and revealing equally（等概率混合策略）；complete revealing policy（完全揭示策略）；complete hiding policy（完全隐藏策略）
- Benchmark 表述引文：在 Numerical Simulations 部分：'The benchmark for the performance of these policies is, of course, an optimal policy.' 同时，摘要及正文多处用 'near-optimal'、'comprehensive test bed' 描述系统化评价。
- Benchmark 评价：在综合测试床（comprehensive test bed）上评价启发式信息隐藏策略：以最优策略（通过枚举决策空间得到的收益最大化策略）为基准，比较启发式策略与完全揭示、完全隐藏、等概率混合策略的期望收益；报告平均收益比值（如启发式/最优约为0.94-1，启发式/完全揭示约1-7.33）。
- 判定理由：客观指标方面：核心构念为广告交易平台每场拍卖的期望收益，是可由拍卖规则和出价决定的客观经济量，不依赖主观判断；全文核心目标、评价和贡献均围绕该收益提升展开，无并列主观目标或其他核心贡献。Benchmark方面：作者在数值模拟部分明确使用 benchmark 一词，以最优策略为基准，在综合测试床上系统评价启发式及对比策略，结果用于证明启发式策略的收益提升（近最优且大幅优于完全揭示等策略），满足明确基准评价、处于评价语境、支撑核心主张且有明确参照点。因此两模块全部通过，strict_include 为 true。
- 置信度：0.95

### Modeling Fixed Odds Betting For Future Event Prediction1 

- 年份/期刊：2017 / MIS Quarterly
- DOI：10.25300/misq/2017/41.2.14
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：未来事件预测准确性（QSR/LSR/SSR 评分规则）
- Benchmark 状态：benchmark_comparison_central
- 参照点：BookMaker/Betting line (p_odds)；BetRatio (s_A)；ReducedForm1~ReducedForm4；ReducedFormSimu；Inklingmarkets.com auction-based prediction market
- Benchmark 表述引文：Evaluation/Baseline Methods部分："...we experimented with the combination of p_odds and s_A using logit regression and derived four benchmark models (ReducedForm1~ReducedForm4)." Robustness Check部分："For comparison, we also show the performance of the best benchmark in each dataset."
- Benchmark 评价：在三个真实数据集（sina 2008 Olympic Games、sohu Entertainment Events、sohu 2014 FIFA）上，将BD-ML/BD-AIC与bookmaker/betting line、BetRatio、ReducedForm1-4、ReducedFormSimu以及Inklingmarkets.com auction-based prediction market进行比较，采用QSR/LSR/SSR。Table 2显示BD模型显著优于各benchmark模型；Table 1显示与auction市场可比。
- 判定理由：核心指标为未来事件预测的QSR/LSR/SSR评分，完全依赖外部真实事件结果，客观可计算；预测性能提升是全文唯一核心目标和贡献。全文在评价语境中明确使用benchmark一词（four benchmark models、best benchmark），将所提BD模型与多个baseline/reduced-form/auction机制比较，并以该比较作为核心性能提升的证据。因此两个模块均通过。
- 置信度：0.87

### USING FORUM AND SEARCH DATA FOR SALES PREDICTION OF HIGH-INVOLVEMENT PROJECTS 

- 年份/期刊：2017 / MIS Quarterly
- DOI：10.25300/misq/2017/41.1.04
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：汽车品牌月度销量预测误差（MAPE）
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：Benchmark Model（作者定义的内部基准模型：消费者情绪指数、汽油价格、季节项 Sales_{i,t-12} 与历史销量）
- 参照点：Benchmark Model；Forum-Based Model；Extended Forum-Based Model；Search Trends-Based Model
- Benchmark 表述引文：Modeling 部分：'Following previous research in this domain, we utilized the following benchmark data… Having collected the data, we defined a benchmark model as a model that utilizes consumer sentiment, gasoline price, seasonality (Sales_{i,t-12}), and previous sales data.'
- Benchmark 评价：在23个美国汽车品牌月度销量数据上，以滚动窗口外样本 MAPE 对 benchmark model、forum-based、extended forum-based、search trends-based 和 combined 五种模型进行系统比较；核心结论是 combined model 相对 benchmark model（以及 forum-only 模型）显著降低 MAPE。
- 判定理由：客观指标：核心成功指标为实际汽车销量上的 out-of-sample MAPE，销量为单位销售事实，MAPE 可确定计算，不依赖主观评价。唯一核心目标：全文以预测准确性为研究问题、设计目标和贡献声明，未设置主观结果或理论机制等并列核心贡献。Benchmark：作者在评价语境中明确使用“benchmark model/benchmark data”，将 combined/forum/search 模型与基准模型进行 MAPE 比较，benchmark 结果直接支持核心提升主张，且有明确参照点。因此两个模块均通过。
- 置信度：0.88

### Know When to Run: Recommendations in Crowdsourcing Contests1 

- 年份/期刊：2018 / MIS Quarterly
- DOI：10.25300/misq/2018/14103
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：获胜预测准确率（Top n accuracy）及平均绝对误差（MAE）；推荐任务成功率（Recommendation success rate）；任务排名一致性（Ranking consistency）；模拟参与人数与平台收入影响
- Benchmark 状态：benchmark_comparison_central
- 参照点：随机选择基准（Random Selection）；基于99designs points的基准（Points-Based）；solver自身任务选择（作为推荐成功率比较参照）
- Benchmark 表述引文：在‘Evaluating the Framework Part I: Comparing Alternative Winner Prediction Models’的Baseline Models部分写道：‘Two benchmarks are used for comparison. In the first, a random solver is projected as the winner... The second benchmark predicts the solver with the most points as the winner in a task.’（另在引言RQ3(a)说：‘We compare the performance of the adapted models to two benchmarks.’）
- Benchmark 评价：在从99designs收集的958个测试任务上，将MNL、朴素贝叶斯、贝叶斯网络、神经网络、SVM及Ranked-MNL-Ties等模型与两个基准（随机选择、基于points的基准）进行比较，报告Top 1-5预测准确率、MAE及显著性；推荐系统部分进一步以solver自身选择为参照比较推荐有效率（22.17%提升至31.24%，提升40.91%）。这些基准比较直接支撑模型和推荐系统优于既有选择和平台指标的核心主张。
- 判定理由：客观指标：核心成功标准是预测任务winner的准确率和推荐提高solver赢得任务的成功率，这些基于平台客观事实标签（是否赢），不依赖人类主观评价；满意度仅作为推测性附带收益未进入评价。唯一核心目标：文章围绕构建并验证能提升solver获胜成功率的推荐系统展开，理论框架用于指导变量选择，不是并列核心贡献。Benchmark：全文存在明确的benchmark表述（‘Two benchmarks are used for comparison’），位于实验评价语境，比较对象明确（随机选择、points-based、solver自身选择），结果直接支撑客观指标提升。因此两个模块均通过，strict_include=true。
- 置信度：0.92

### Top Persuader Prediction for Social Networks1 

- 年份/期刊：2018 / MIS Quarterly
- DOI：10.25300/misq/2018/13211
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：Top-K Precision；Spearman等级相关系数；总说服信用
- Benchmark 状态：benchmark_comparison_central
- 参照点：Degree Centrality；Closeness Centrality；Betweenness Centrality；Percolation Centrality；Eigenvector Centrality；Intercentrality；INF-RANK；INF-SIM；Random Selection
- Benchmark 表述引文：引言部分：'we empirically evaluate the effectiveness of our proposed method with real-world social network data, using representative existing methods as benchmarks'；评价部分：'We therefore benchmarked our proposed method against existing methods developed on the basis of major centrality measures'。
- Benchmark 评价：在真实世界社交网络（游戏avatar网络和手机通话网络）上，以多个中心度方法、PageRank类方法、INF-SIM和随机选择为基准，比较top-K precision、Spearman系数和总说服信用；结果显示所提方法在所有指标上显著优于基准方法，且在不同γ和K值下稳健。
- 判定理由：客观指标方面，核心成功指标为top-K precision、Spearman系数和总说服信用，均由实际采纳行为日志和固定规则计算，不依赖主观感知或语义评价；预测top persuaders和提升客观预测精度是全文唯一核心目标与贡献。Benchmark方面，文章在真实数据上以多种既有方法为基准，明确使用benchmark/benchmarked表述进行系统化比较，且比较结果直接支撑核心提升主张，满足benchmark_comparison_central。因此两个模块均通过，strict_include=true。
- 置信度：0.95

### A Time-Based Dynamic Synchronization Policy for Consolidated Database Systems1 

- 年份/期刊：2019 / MIS Quarterly
- DOI：10.25300/misq/2019/14804
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：总系统成本
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：Periodic policy (Dey et al. 2006)；Query-based policy (Dey et al. 2006)；Update-based policy (Dey et al. 2006)；Query-based dynamic policy (Fang et al. 2013)；Hybrid policy (Dey et al. 2015)
- 参照点：Periodic policy (Dey et al. 2006)；Hybrid policy (Dey et al. 2015)；Query-based policy；Update-based policy；Query-based dynamic policy (Fang et al. 2013)
- Benchmark 表述引文：摘要：'Experimental results show that the TDS policy consistently outperforms benchmark policies'；Policy Comparisons部分：'we ... compare the TDS policy against benchmark policies both theoretically and numerically.'
- Benchmark 评价：在Policy Comparisons中，TDS策略与周期性策略等在1至5年时间窗上模拟比较；Table 1/Figure 7显示TDS总成本低于周期性策略，成本节约约10%；Appendix D显示TDS相对于混合策略的成本节约为3.84%至10.22%。
- 判定理由：文章的核心客观指标是总系统成本/成本节约，唯一核心目标是最小化CDB同步与数据陈旧总成本；数值实验将TDS策略与周期性策略、混合策略等基准策略比较，并以成本节约百分比作为核心改进证据，满足完全客观指标、唯一核心目标和明确benchmark比较的门槛。
- 置信度：0.95

### A Data Analytics Framework for Smart Asthma Management Based on Remote Health Information Systems with Bluetooth-Enabled Personal Inhalers 

- 年份/期刊：2020 / MIS Quarterly
- DOI：10.25300/misq/2020/15092
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：AUC（受试者工作特征曲线下面积）；误报率与漏检率；平均报警时间（time-to-alert）
- Benchmark 状态：benchmark_comparison_central
- 参照点：GLMM-P；GLMM-NB；GLMM-GQPS；Logistic Regression；SVM；CG-HMM
- Benchmark 表述引文：摘要：'We show the satisfactory performance of our data analytics framework through rigorous comparison with various benchmark methods.'；性能评估部分：'We considered various benchmark methods such as the conventional GLMMs, mixed effects logistic regression model, SVM, and CG-HMM.'
- Benchmark 评价：在SAM真实数据集上，将提出的GLMM-GQP与六个基准方法（GLMM-P、GLMM-NB、GLMM-GQPS、混合效应逻辑回归、SVM、CG-HMM）进行系统比较；以AUC为主要指标，并在不同训练数据量（k=1,4,8,12,m−1）下进行100次重复评估；结果显示GLMM-GQP在多数设置下AUC最高（Table 4），并通过误报率、漏检率和时间到报警进一步解释。
- 判定理由：核心目标是开发并验证一个以客观检测性能（AUC等）为唯一成功标准的异常吸入器使用检测框架；所有评价指标均为可审计的客观指标，无主观量表或人类语义判断。全文存在明确的benchmark表述（摘要和性能评估部分的benchmark methods），在评价语境中系统比较了六个带明确参照点的基准方法，并将benchmark比较结果作为核心改进主张的关键证据。因此同时满足客观指标唯一核心目标和明确benchmark两个条件，strict_include=true。
- 置信度：0.95

### A Prescriptive Analytics Framework for Optimal Policy Deployment Using Heterogeneous Treatment Effects 

- 年份/期刊：2021 / MIS Quarterly
- DOI：10.25300/misq/2021/15684
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：企业/组织总效用（utility = benefit - cost）；期望总效用提升；模型精度MAE
- Benchmark 状态：benchmark_comparison_central
- 参照点：ATE（平均处理效应）；Uplift modeling（UM）；Modified LinUCB（上下文bandit扩展）
- Benchmark 表述引文：摘要中明确写有“as compared to benchmark practices—i.e., the use of the average treatment effect, uplift modeling...”；实证分析部分又写道“To empirically validate our framework, we benchmarked its HTE-EST procedure ... against two other prescriptive approaches within the causal inference paradigm that currently dominates practice.”
- Benchmark 评价：在血液捐赠和推荐营销两个随机现场实验数据上，以预算约束下的期望总效用为核心指标，将HTE-EST与ATE、uplift modeling（以及扩展的modified LinUCB）进行比较。血液捐赠案例中报告HTE-EST比UM高最多240%、比ATE高最多340%，在多个预算约束水平下均优于基准方法。
- 判定理由：客观指标方面，核心结果是预算约束下的总效用，由实际捐赠、交易、奖励成本等可审计事实计算得到，不依赖人类主观评价；唯一核心目标是提升该客观效用，框架和OUR指标是实现这一目标的中间工具。Benchmark方面，作者明确使用“benchmark/benchmarking”表述，在实证评价部分将HTE-EST与ATE、uplift modeling、modified LinUCB等明确参照点进行比较，且benchmark比较直接支撑了效用提升的核心主张。因此两个模块均通过，strict_include=true。
- 置信度：0.85

### A Prescriptive Analytics Method for Cost Reduction in Clinical Decision Making 

- 年份/期刊：2021 / MIS Quarterly
- DOI：10.25300/misq/2021/14372
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：临床决策总成本（美元）
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：KDD Cup 2008 breast cancer data set (used in Appendix D)
- 参照点：THR (Threshold moving)；SMOTE (Synthetic Minority Oversampling)；IW (Instance Weighting)；MC (MetaCost)
- Benchmark 表述引文：引言部分：'we use two real-world clinical data sets to evaluate the proposed method, with several prevalent methods as benchmarks'；实证评价部分设有专门小节'Benchmark Methods and Experimental Procedure'，并明确列出THR、SMOTE、IW、MC作为Benchmark（见表9）。
- Benchmark 评价：在机械通气数据集（正文）和KDD Cup 2008乳腺癌数据集（附录D）上，将提出的ICSL方法与四种既有成本敏感学习方法（阈值移动THR、SMOTE、实例加权IW、MetaCost MC）进行系统对比；结果报告平均总成本、成本降低百分比及Wilcoxon符号秩检验，并在不同分类成本、成本变化概率、投资额和分类算法下做稳健性分析。
- 判定理由：客观指标方面：核心成功指标为临床决策的总成本（美元），属于可直接观测、可审计的财务/事实指标；全文没有主观量表或语义评价作为核心结果，设计目标、问题定义、评价和贡献声明均围绕成本降低展开，因此满足客观指标和唯一核心目标门槛。Benchmark方面：文章明确以“benchmark methods”命名并系统评价ICSL与THR、SMOTE、IW、MC等既有方法的比较（以及在KDD Cup 2008上的评价），benchmark出现在实证评价部分，结果直接支撑成本降低的核心主张，并有明确参照点。两个模块均通过，strict_include=true。
- 置信度：0.97

### What Will Be Popular Next? Predicting Hotspots in Two-Mode Social Networks 

- 年份/期刊：2021 / MIS Quarterly
- DOI：10.25300/misq/2021/15365
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：Top-K 精确率 (Precision at K)；平均精确率 (AP)；AUC；Kendall Tau 系数
- Benchmark 状态：benchmark_comparison_central
- 参照点：PageRank；HITS；Linear Threshold (LT)；Multipath Asynchronous Threshold (MAT)；Two-mode Link Prediction (LP)；Collaborative Filtering (CF)；Baseline Linear Regression (BLR)；Baseline Persistence Method (BPM)
- Benchmark 表述引文：摘要声明“In the evaluation, we benchmark the proposed method against prevalent methods, and we demonstrate its superior performance using three real-world data sets”；实证部分又明确写“we evaluated our method against eight benchmark methods”和“we benchmarked the proposed method against prevalent methods”。这些表述位于摘要和评价/实验部分。
- Benchmark 评价：在三个真实数据集（Dianping、Gowalla、图书阅读社交平台）上，将GLMR与PageRank、HITS、线性阈值LT、多路径异步阈值MAT、两模链路预测LP、协同过滤CF、基线线性回归BLR、基线持久性BPM共八个基准方法比较；采用Precision、AP、AUC、Tau四项排序指标。结果表8-10显示GLMR在全部数据集和指标上均优于所有参照方法。
- 判定理由：本文核心目标是预测未来社会焦点的流行度排名，所有主要成功指标均为基于未来可观察采纳次数（签到/书籍添加）计算的排序指标，完全客观且为唯一核心目标；评价以三个数据集上的八种基准方法对比为核心证据，存在明确、位于评价语境且支持核心提升主张的 benchmark 表述，并有明确的参照点比较。因此 strict_include=true。
- 置信度：0.93

### Combining Crowd and Machine Intelligence to Detect False News on Social Media 

- 年份/期刊：2022 / MIS Quarterly
- DOI：10.25300/misq/2022/16526
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：假新闻检测性能（PR AUC、F1、recall、precision）
- Benchmark 状态：benchmark_comparison_central
- 参照点：SVM；CNN；LSTM；Bi-LSTM；BERT；Concat；HSA；MV；BAM；CAND-1、CAND-12 等增量对照
- Benchmark 表述引文：摘要：'Evaluation based on Weibo and Twitter datasets demonstrates the effectiveness of crowd intelligence and the superior performance of the proposed framework in comparison with the benchmark methods.' 实验部分标题为'Baseline Methods and Evaluation Metrics'，并称'we designed five benchmark methods based on widely used methods from the literature of false news detection and deep learning'。
- Benchmark 评价：在 Weibo 与 Twitter 数据集上系统比较 CAND 各变体（CAND-1、CAND-12、CAND-123）与特征型基准（SVM、CNN、LSTM、Bi-LSTM、BERT）、端到端基准（Concat、HSA）以及聚合基准（MV、BAM），报告 PR AUC、F1、recall、precision，并显示 CAND 在多种不平衡比例下显著优于基准方法。
- 判定理由：文章核心目标是提出 CAND 框架以提升假新闻检测性能，核心指标为 PR AUC、F1、recall、precision，ground truth 来自官方事实核查和已有参考数据集的客观事实标签，全部核心成功结果均为客观指标。文章在实验部分明确使用 benchmark methods 作为比较基准，并在多个数据集和不平衡比例下报告相对 benchmark 的提升，符合 benchmark 比较式评价要求。因此 objective_metric、core_goal_status 和 benchmark 门槛均通过，strict_include=true。
- 置信度：0.94

### Cross-Lingual Cybersecurity Analytics in the International Dark Web with Adversarial Deep Representation Learning 

- 年份/期刊：2022 / MIS Quarterly
- DOI：10.25300/misq/2022/16618
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：跨语言黑客资产检测的准确率（Accuracy）、F1-score、AUC
- Benchmark 状态：benchmark_comparison_central
- 参照点：Lexicon Search baseline；Monolingual traditional ML：NB、SVM、RF；Monolingual deep learning：BiLSTM、BiGRU、CNN；MT-based：NB+MT、SVM+MT、RF+MT、BiLSTM+MT、BiGRU+MT、CNN+MT；CLKT alternatives：FML-CNN、MTL-BiLSTM、MTL-BiGRU
- Benchmark 表述引文：性能评价部分明确写道：“We systematically evaluated CLHAD against state-of-the-art benchmark methods for hacker asset detection in Russian, French, and Italian...”（Benchmark Evaluation 一节），并以“Benchmark Evaluation Results in Hacker Forums and DNMs for Russian and French”为表标题展示比较结果。
- Benchmark 评价：在作者构建的多语言 dark web gold-standard 测试集（英文、俄文、法文、意大利文）上，将 CLHAD 与 lexicon baseline、monolingual 传统ML/深度模型、MT-based 方法、CLKT 替代方法（FML-CNN、MTL-BiLSTM、MTL-BiGRU）进行比较。结果显示 CLHAD 在俄、法、意的 hacker forums 和 DNMs 上 Accuracy/F1/AUC 均达到最优，且多数差异具有统计显著性。
- 判定理由：客观指标方面，核心成功指标为黑客资产检测的 Accuracy/F1/AUC，属于固定事实标签上的分类性能，非主观体验或语义质量评价；核心目标是提升跨语言黑客资产检测性能，无并列主观或理论核心目标。benchmark 方面，作者在评价部分明确使用“benchmark methods”并以多种既有基线/方法作为参照，benchmark 比较结果是支持核心提升主张的主要证据。因此两个模块均通过，strict_include=true。
- 置信度：0.95

### Depicting Risk Profile over Time: A Novel Multiperiod Loan Default Prediction Approach 

- 年份/期刊：2023 / MIS Quarterly
- DOI：10.25300/misq/2022/17491
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：时间至违约预测性能（C-index、IBS、月度AUC）；多时点区分性能（AUC、KS、H-measure）；授信绩效（Granting Performance）；盈利绩效（Profitability Performance）
- Benchmark 状态：benchmark_comparison_central
- 参照点：COX；MCM；MTLSA；RSF；BR；CC；NS
- Benchmark 表述引文：摘要：'HACS outperforms the benchmarked survival analysis and multilabel learning methods on all fronts.'；实验设计部分：'We evaluated HACS in comparison with benchmarked methods from two families, i.e., survival analysis and multilabel learning.'
- Benchmark 评价：在来自某大型在线借贷平台的真实数据集上，将HACS与7种基准方法（COX、MCM、MTLSA、RSF、BR、CC、NS）在时间至违约预测、多时点区分性能、授信绩效和盈利绩效等多个层面进行系统比较，结果显示HACS在客观指标上全面优于这些基准方法。
- 判定理由：客观指标方面：核心指标为C-index、IBS、AUC、KS、H-measure、授信违约数和组合回报率，均基于真实还款记录和固定计算规则，完全客观。唯一核心目标方面：研究问题、设计目标、实验评价和贡献声明均围绕HACS提升多期违约预测和信贷决策的客观绩效展开，全文不存在并列的主观结果或理论机制解释作为核心成功标准。benchmark方面：作者明确使用benchmarked methods表述，并在实验设计、结果表和显著性检验中将HACS与COX、MCM、MTLSA、RSF、BR、CC、NS等既有方法比较，benchmark评价直接支撑核心绩效提升主张，且存在明确参照点。因此满足strict_include。
- 置信度：0.92

### Exploiting Expert Knowledge for Assigning Firms to Industries: A Novel Deep Learning Method 

- 年份/期刊：2023 / MIS Quarterly
- DOI：10.25300/misq/2022/17171
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：行业分类准确率（Accuracy）；宏平均F1（Macro-F1）
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：NAICS 2012；GICS 2016
- 参照点：SVM-IA；MLP-IA；ULMFiT-IA；HC-IA；LE-IA
- Benchmark 表述引文：在“Empirical Evaluation”开头，作者写道：‘We benchmarked DeepIA against several prevalent methods on the tasks of assigning firms to industries of two widely used ICSs: North American Industry Classification System (NAICS) and Global Industry Classification Standard (GICS).’
- Benchmark 评价：作者在两个公开行业分类体系NAICS和GICS上，将DeepIA与SVM-IA、MLP-IA、ULMFiT-IA、HC-IA、LE-IA等既有的行业分类方法或可改编的对比方法进行系统比较，使用accuracy和macro-F1作为评价指标；主结果中DeepIA在NAICS各焦点层级上均最高，例如T=2015、l*=3时accuracy 0.68，宏F1 0.26，并显著优于全部基准方法。
- 判定理由：客观指标方面，核心成功指标是行业分配准确率和宏平均F1，基于权威数据库中的既定行业标签进行比较，指标完全客观，不依赖主观判断；唯一核心目标是提升行业分配性能，动态表示和分层分配是服务于该目标的算法创新而非并列核心贡献。Benchmark方面，文章在Empirical Evaluation中明确使用“We benchmarked DeepIA against…”并在Benchmark Methods节列出多个现有方法，在NAICS和GICS两个公开行业分类体系上系统比较，以accuracy和macro-F1证明DeepIA优于多个基准，benchmark评价是支撑核心改善主张的直接证据，且具有明确的比较对象。因此严格判定为纳入。
- 置信度：0.95

### Extracting Actionable Insights from Text Data: A Stable Topic Model Approach 

- 年份/期刊：2023 / MIS Quarterly
- DOI：10.25300/misq/2022/16957
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：主题模型稳定性指标（文档-主题概率/标签、主题-词概率/Top词一致性）；模型质量指标（perplexity、主题连贯性Cv/Cuci）
- Benchmark 状态：benchmark_comparison_central
- 参照点：LDA；Doc LDA；Ensemble LDA；Granulated LDA；MRF-LDA / CRFTM（附录F）；η=1的消融对照（Table 7）
- Benchmark 表述引文：引言中明确写道“We benchmark our method with other innovative LDA instability mitigation methods.”；实验部分的Baselines小节写道“In addition to the standard LDA baseline, we include several recent approaches designed to alleviate the instability issue in our benchmarks.”；附录E标题为“Benchmark Model Parameters”。
- Benchmark 评价：在Amazon产品评论、Yelp餐厅评论、StackExchange Q&A、公司描述四个文本数据集上，将Stable LDA与标准LDA、Doc LDA、Ensemble LDA、Granulated LDA进行系统比较（附录F另对比MRF-LDA和CRFTM），报告稳定性四项指标和模型质量指标，结果显示Stable LDA显著提升稳定性且质量不下降。
- 判定理由：客观指标方面，核心成功指标是主题模型稳定性（重复运行间概率分布和标签的一致性）以及模型质量（perplexity、自动主题连贯性），均不依赖主观感受或人工语义评分；研究问题、设计目标、评价和贡献均围绕提升稳定性这一客观改进展开，无并列的理论或主观核心目标。Benchmark方面，作者在引言和实验部分明确使用benchmark/benchmarking陈述系统化比较，将Stable LDA与多个基线在同一批文本数据集上比较，并以稳定性结果作为核心主张的关键证据；存在明确参照点。因此 strict_include=true。
- 置信度：0.92

### Unlocking the Power of Voice for Financial Risk Prediction: A Theory-Driven Deep Learning Design Approach 

- 年份/期刊：2023 / MIS Quarterly
- DOI：10.25300/misq/2022/17062
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：财务风险（股票波动率）预测误差
- Benchmark 状态：benchmark_comparison_central
- 参照点：Market benchmark (Sridharan 2015 fundamentals + risk model)；Fundamental model；DeepVoice w/o Verbal；DeepVoice w/o Vocal；Concat-SVR；Concat-GradientBoosting；One-stage LSTM；Contextual LSTM (Poria et al. 2017)；DeepVoice-Attention；Emotion model (Mayew & Venkatachalam 2012)
- Benchmark 表述引文：Evaluation Metrics 部分：'we calculate and report the out-of-sample R² relative to a benchmark model as our main performance measure: R²_oos(m)=1 − MSE^m/MSE^benchmark'；并说明 'we consider the benchmark model to be the forecasting model that uses firm fundamental and historical risks, as proposed in Sridharan (2015), i.e., v=Stacking(v^Fundamental, v^Risk)'。该基准被称为市场基准（market benchmark）。
- Benchmark 评价：在自建的6,047个财报电话会议测试集上，将DeepVoice与市场基准（fundamentals+historical risk）、仅用文本（DeepVoice w/o vocal）、仅用语音（DeepVoice w/o verbal）、特征拼接类机器学习模型、Contextual LSTM等进行比较，以样本外R²_oos为核心指标。结果显示DeepVoice在3/5/10/30/60天预测范围内R²_oos分别为7.31%、8.34%、4.28%、2.26%、7.45%，显著优于市场基准和所有对比方法，并用DM检验验证显著性。该benchmark评价直接支撑核心的预测精度提升主张。
- 判定理由：文章以预测公司股票波动率（财务风险）的样本外误差（MSE/R²_oos）为核心目标，该指标完全由市场交易价格计算，客观可验证；研究问题、设计假设、评估和贡献均围绕提升这一客观指标，没有主观量表或人类评判作为成功标准，也没有并列的核心贡献。同时，文章在评价部分明确使用benchmark一词定义了市场基准和其他baseline，并在测试集上系统比较，benchmark结果直接支撑核心的预测精度提升主张，且具有明确参照点。因此两个模块均通过，strict_include=true。
- 置信度：0.98

### Creating Proactive Cyber Threat Intelligence with Hacker Exploit Labels: A Deep Transfer Learning Approach 

- 年份/期刊：2024 / MIS Quarterly
- DOI：10.25300/misq/2023/17316
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：准确率、精确率、召回率、F1-score
- Benchmark 状态：benchmark_comparison_central
- 参照点：Naive Bayes, Logistic Regression, Decision Tree, SVM, XGBoost, LightGBM；RNN, GRU, LSTM, BiLSTM, BiLSTM with self-attention；Adaptive SVM, hard/soft parameter sharing MTL, adversarial DTL, BERT；单层和多层层迁移消融（pre-initialized vs. non-pre-initialized）
- Benchmark 表述引文：摘要：“we rigorously evaluated the proposed DTL-EL against state-of-the-art non-DTL benchmark methods based in classical machine learning and deep learning”；实验部分：“we rigorously evaluated our proposed DTL-EL artifact with a series of technical benchmark experiments”。
- Benchmark 评价：在作者自建的源域（漏洞DNM和公开漏洞库）与目标域（黑客论坛）数据集上，将DTL-EL与经典ML（朴素贝叶斯、逻辑回归、决策树、SVM、XGBoost、LightGBM）、非DTL深度学习方法（RNN、GRU、LSTM、BiLSTM、BiLSTM+自注意力）、其他迁移学习方法（自适应SVM、MTL、对抗学习、BERT）以及层选择消融进行对比，报告准确率、精确率、召回率、F1-score，并给出统计显著性检验。
- 判定理由：文章以黑客漏洞利用代码标签分类为核心，所有核心成功指标均为基于攻击类型事实标签的准确率、精确率、召回率和F1-score，属于客观可核验的分类性能；研究目标、评价结构和贡献声明均围绕提升该客观分类指标展开，无主观满意度等并列核心目标。全文在摘要和实验部分明确使用“benchmark experiments/methods”表述，并在自建源域和目标域数据集上开展系统化基准比较，包含经典ML、非DTL深度模型、其他迁移学习方法及消融分析等明确参照点，benchmark评价直接支撑核心改进主张。因此两个模块均通过，strict_include为true。
- 置信度：0.95

### Automating in High-Expertise, Low-Label Environments: Evidence-Based Medicine by Expert-Augmented Few-Shot Learning 

- 年份/期刊：2025 / MIS Quarterly
- DOI：10.25300/misq/2024/18573
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：句子分类性能（F1@3、PRC）；序列标记性能（F1、BERTScore、PRC）；SR项目时间节省（最多65%）
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：EBM-NLP
- 参照点：Naïve Bayes；SVM；LSTM；CNN；VAT (SSL)；Fine-tuned BioBERT；GPT-4 Few-Shot；MAML；FSL_DS；L2AC；Matching net；ProtoNet；ProtoNER；Nearest neighbors；LSTM+CRF
- Benchmark 表述引文：在“Evaluation Strategy and Datasets”部分明确写道：“For sentence classification and sequence tagging, we benchmarked FastSR with a number of models summarized in Tables 2 and 4 and also conducted extensive ablation analyses to estimate the impact of each design component.”；引言和任务复杂度部分也有“we benchmarked FastSR against fine-tuned BioBERT, fine-tuned and few-shot prompted GPT across both open-domain and closed-domain datasets.”
- Benchmark 评价：在WD、COVID（CORD-19）和公开EBM-NLP数据集上，将FastSR与传统分类器（SVM、CNN等）、半监督（VAT）、LLM（fine-tuned BioBERT、GPT-4 few-shot）、FSL模型（ProtoNet、MAML等）等进行比较，报告句子分类F1@3、PRC和序列标记F1、BERTScore、PRC。结果显示FastSR在各个数据集上全面优先进（例如WD句子分类F1@3 73.00 vs ProtoNet 65.40 vs GPT-4 39.23；EBM-NLP句子分类F1@3 79.71 vs ProtoNet 77.26）。
- 判定理由：客观指标方面：文章核心是提升PICO元素提取的客观性能指标（句子分类和序列标记的F1、PRC），以及由此带来的时间节省，这些指标均基于可核验的医学事实标签和确定计算公式，不存在并列的主观核心成功标准。唯一核心目标：研究问题、设计需求（DR1-DR4）、评价结构和贡献声明均围绕客观提取性能和时间节省，理论指导和定性反馈属于支撑性内容，不构成与客观指标提升并列的核心目标。Benchmark方面：全文在评估方法部分明确宣称进行benchmark比较，并在三大数据集上与大量基准模型进行系统比较，结果表包含明确参照点和显著性检验，benchmark结果直接支撑FastSR性能提升的核心主张。因此满足纳入条件。
- 置信度：0.95

### RADAR: A Framework for Developing Adversarially Robust Cyber Defense AI Agents with Deep Reinforcement Learning 

- 年份/期刊：2025 / MIS Quarterly
- DOI：10.25300/misq/2024/17339
- 指标状态/核心目标：objective_fixed_factual_labels / exclusive_objective_improvement
- 核心指标：逃避率（Evasion Rate, ER）；假阳性率（False Positive Rate, FPR）
- Benchmark 状态：benchmark_comparison_central
- 命名 Benchmark：VirusTotal malware repository（作为测试数据来源，非公开基准套件）；EMBER（Figure 9 标题中称LGBM为EMBER Malware Detector，但实验主体使用VirusTotal测试床）
- 参照点：Random actions；Benign feature append (BFA)；EvadeHC；GAMMA；Surrogate-based RNN；Policy gradient (PG)；DDQN；Rainbow；MAB-malware；ACER；A3C；鲁棒化前（Before RL-RO）与鲁棒化后（After RL-RO）
- Benchmark 表述引文：摘要和引言：'We rigorously evaluate the performance of RADAR as a situated IT artifact against state-of-the-art machine learning and deep learning-based benchmark methods.'；实验设计：'To rigorously compare RADAR to other alternatives, Experiment 1 compared RADAR's performance on adversarial attack realization to eight leading black-box adversarial malware attack methods ...'；Table 6标题：'Overview of Selected Benchmark Methods'；结果：'Table 7 summarizes the benchmark evaluation results in terms of the evasion rate.'；结论：'its performance was extensively measured against state-of-the-art benchmarks.'
- Benchmark 评价：在恶意软件检测任务上，将r-VAC与8种基准对抗攻击方法（Random actions、BFA、EvadeHC、GAMMA、Surrogate RNN、PG、DDQN、Rainbow、MAB-malware、ACER、A3C）在LGBM、MalConv、NonNeg三个检测器上比较逃避率；随后通过RL-RO对检测器进行鲁棒化，比较鲁棒化前后的逃避率与FPR，并在重复博弈中比较多轮模型。
- 判定理由：客观指标：核心指标为逃避率（ER）与假阳性率（FPR），两者依据恶意/良性事实标签和检测器输出确定，不依赖人类主观评价，符合完全客观指标；唯一核心目标：研究问题、设计目标、评价结构和贡献声明均围绕提升防御AI代理的对抗鲁棒性这一客观指标展开，无并列核心目标；benchmark：全文存在多处明确的benchmark表述（'benchmark methods'、'selected benchmark methods'、'benchmark evaluation results'），且这些benchmark比较位于评价部分，包含多个显式baseline和鲁棒化前后对照，用于直接支撑核心的逃避率提升与鲁棒性提升主张。因此严格通过。
- 置信度：0.97

### Shapley Value-Based Feature Attribution for Data Masking 

- 年份/期刊：2026 / MIS Quarterly
- DOI：10.25300/misq/2025/18502
- 指标状态/核心目标：fully_objective_direct / exclusive_objective_improvement
- 核心指标：披露风险（disclosure risk）；数据效用（data utility）
- Benchmark 状态：benchmark_comparison_central
- 参照点：Benchmark I: 仅掩码机密特征；Benchmark II: 随机选择一半非机密特征进行掩码（Li & Sarkar, 2014）
- Benchmark 表述引文：实验部分开头：“we evaluate the effectiveness and robustness of the proposed framework in protecting data privacy while maintaining data utility and compare it with benchmark methods.”（Experimental Studies 第一节）；实验设置中明确命名两个基准方法：“the first benchmark method (Benchmark I) implemented in this study only selects the confidential feature to mask”和“a second benchmark method proposed by Li and Sarkar (2014)，which randomly selects half of the nonconfidential features for data masking (Benchmark II)”（Experiment Setup）。
- Benchmark 评价：在模拟数据集及Credit、Salary、CRSP/Compustat三个真实数据集上，将所提risk-only和weighted-cost特征选择方法与Benchmark I（仅掩码机密特征）和Benchmark II（随机选择一半非机密特征）比较，报告风险减少和效用损失的百分比（如Table 4、Table 5a/b/c、Table 6），以此证明所提框架能更有效地降低披露风险并保持数据效用。
- 判定理由：本文核心目标是降低推断性披露风险并保持数据效用，两者均以R²/AAD/RASD等客观统计指标度量，实验评估和贡献声明完全围绕这些客观指标提升展开，无主观量表或并列核心目标；正文实验部分明确以Benchmark I和Benchmark II作为基准方法进行比较，比较结果（风险减少和效用保持）是支撑核心提升主张的关键证据，满足benchmark四门槛；因此纳入。
- 置信度：0.9
