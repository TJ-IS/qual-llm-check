# Exclusive objective-metric improvement with explicit benchmark statements

Completed: 13909 / 13909
Retained: 315

## A competing risks model based on latent Dirichlet Allocation for predicting churn reasons

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113541
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "预测客户流失概率与流失原因的性能指标（LL/AIC/BIC、P@r、top-decile lift）", "measurement_cn": "基于荷兰电信公司真实客户数据，使用Cox比例风险模型和竞争风险模型预测流失；用训练集估计模型，用2016年3月作为测试集；在排序后的流失概率列表上计算precision at r（r=100,500,1000,均值N）和top-decile lift，与基准模型比较；另用in-sample的log-likelihood、AIC、BIC比较不同模型拟合。", "objectivity_reason_cn": "流失事件及流失原因（Controllable/Uncontrollable/Unknown）来自公司系统的合同终止记录和客服人员录入的原因，属于可核实的事实标签；预测性能指标是数学计算，不依赖主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 基准模型为随机从客户中选择流失者的当前TSP部署模型。在2016年3月测试集上，将所提出的持续时间模型和三个竞争风险模型与基准模型比较P@r和top-decile lift；结果显示所有提出模型的P@r和top-decile lift均高于基准模型，支持核心改进主张。
- Decision: 客观指标方面：核心指标是流失预测与原因预测的客观性能指标（LL/AIC/BIC、P@r、lift），流失事件与原因来自公司系统记录，不依赖主观评价；预测性能提升是全文唯一核心目标与贡献，无并列核心目标。benchmark方面：作者在实验部分明确使用“benchmark model”指代当前TSP部署的模型，并将其作为比较基准（陈述式benchmark），该基准评价用于证明所提模型在P@r和lift上的提升，且具有明确比较器（BM），满足全部门槛。因此strict_include为true。
- Confidence: 0.98

## A decision support system of vehicle routing and refueling for motor carriers with time-sensitive demands

- Year/journal: 2012 / Decision Support Systems
- DOI: 10.1016/j.dss.2012.09.004
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "总加油成本（燃料成本）", "measurement_cn": "由车辆行驶路线和加油决策产生的总加油成本，即每个加油站购买的加油量（加仑）乘以该站燃料单价（美元/加仑）后求和。数据来自燃料消耗量（加仑/英里×行驶英里数 + 怠速消耗）和实际市场价格（OPIS/ProMiles数据库）。", "objectivity_reason_cn": "燃料成本由物理消耗量和可审计的市场价格直接计算，不依赖任何人的感受、语义理解或价值判断，是完全客观可测量的结果指标。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在三个实际实例和六个模拟实验中，将提出的方法分别与三个基准方法比较：基准方法I（Carrier X实际路线与购买合同）、基准方法II（最优TSPTW路线+购买合同）、基准方法III（枚举最优TSPTWR）。报告各方案的总加油成本，结果显示所提方法比基准II最多节省4.29%（n=20, γ=0），且在实际实例中达到最优或近优。
- Decision: 客观指标方面：核心指标为总加油成本（燃料成本），来源于可审计的消耗量和市场价格，完全客观，且是全文唯一的核心目标与贡献；建模、求解和实验均围绕降低燃料成本展开，无主观结果指标或并列核心目标。Benchmark方面：作者在评价部分（Section 6.2）明确使用 'benchmark methods' 表述，定义三种基准方法，并以其为参照报告燃料成本节省幅度（最多4.29%），属于明确的 benchmark 比较且支撑核心主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.98

## A trust-semantic fusion-based recommendation approach for e-business applications

- Year/journal: 2012 / Decision Support Systems
- DOI: 10.1016/j.dss.2012.09.005
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "平均绝对误差（MAE）", "measurement_cn": "在测试集上计算系统预测评分与用户实际评分（rating矩阵中已记录的评分）之间的平均绝对误差，公式见式(19)。", "objectivity_reason_cn": "MAE 是预测数值与实际历史评分数值之间的算术差异，完全根据公式从数据中计算，不依赖于任何人当下的主观评价、语义判断或偏好，属于可审计的预测性能指标。"}, {"name_cn": "覆盖率（Coverage）", "measurement_cn": "系统能够产生预测的项数占所有待预测项数的比例，公式见式(20)。", "objectivity_reason_cn": "覆盖率是能够生成预测的物品数量比例，完全由推荐算法的输出决定，是确定性可观测的客观指标，不涉及主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: MovieLens dataset | Yahoo! Webscope R4 dataset
- Benchmark evaluation: 在MovieLens和Yahoo! Webscope R4两个数据集上，将TSF与Resnick-UCF、Sarwar-ICF、O'Donovan-Trust、Ruiz-Semantic四个基准算法进行比较，在多种邻居数量、不同的数据稀疏度、不同数量的冷启动用户/物品评分设置下，用MAE和Coverage指标度量，结果显示TSF在几乎所有条件下均优于所有基准算法。
- Decision: 客观指标方面：全文核心目标是通过融合信任与语义信息改进推荐系统性能，核心评价指标为MAE和Coverage，两者均是可确定性计算的客观预测性能指标，不依赖于人的主观体验或语义评价，也未将用户满意度、感知质量等主观构念作为成功指标。唯一核心目标与贡献就是提升客观的推荐准确性和覆盖率，实验和结论均围绕这两个指标展开，未发现并列的理论贡献、制度建议或主观体验改善等核心目标。Benchmark方面：第5.3节明确使用“benchmark algorithms”一词，将TSF与四个既有推荐算法进行系统化基准比较；该比较位于实验评价部分，是证明TSF核心提升主张的关键证据；所有结果均有明确的对照基线（Resnick-UCF、Sarwar-ICF、O'Donovan-Trust、Ruiz-Semantic），并报告了TSF在MAE和Coverage上一致优于这些基线。两个模块均完全通过，因此strict_include为true。
- Confidence: 0.98

## Learning Bayesian networks from incomplete databases using a novel evolutionary algorithm

- Year/journal: 2008 / Decision Support Systems
- DOI: 10.1016/j.dss.2008.01.002
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "平均结构差异 (ASD)", "measurement_cn": "将学习到的贝叶斯网络与生成数据的原始网络比较，计算添加、反向和遗漏的边的数量，并在多次运行中取平均。", "objectivity_reason_cn": "基于固定的图结构比较，不涉及人的感受、语义评价或价值判断。"}, {"name_cn": "等价类结构差异 (AESD)", "measurement_cn": "比较学习网络的等价类与原始网络等价类的弧添加/删除以及 compeled 边的差异，取平均。", "objectivity_reason_cn": "基于形式化的等价类定义和固定图操作，计算过程客观可审计。"}, {"name_cn": "平均执行时间 (AET)", "measurement_cn": "每次试验的运行秒数，取平均。", "objectivity_reason_cn": "时钟时间是可以直接测量的物理量，不依赖人类判断。"}, {"name_cn": "平均 MDL 分数 (AOMDL)", "measurement_cn": "在原始完整数据集上用原始网络结构计算的 MDL 分数，取平均。", "objectivity_reason_cn": "MDL 分数由公式确定，是客观计算值，不包含主观评价。"}, {"name_cn": "累计提升 (Cumulative Lift)", "measurement_cn": "在真实直接营销数据上，根据模型排序的客户名单，计算每个十分位段内实际回应者累计占比相对于总体回应率的倍数。", "objectivity_reason_cn": "基于实际购买/回应标签审计，属于可验证的外部事实，不依赖主观感受。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: ALARM | PRINTD | ASIA
- Benchmark evaluation: 在由 ALARM、PRINTD、ASIA 三个知名基准网络生成的 9 个不完整数据集上，比较 EBN 与 LibB、Bayesware Discoverer，并额外与 HEA1、HEA2 等缺失值处理方法比较；EBN 在多数数据集上获得显著更小的 ASD/AESD、更低的 AOMDL，以及更快的执行时间（部分数据集）。
- Decision: 文章提出 EBN 算法，核心目标是在不完整数据上更准确地学习贝叶斯网络，并通过结构差异(ASD/AESD)、MDL分数、执行时间、真实数据累计提升等完全客观指标验证提升；这些指标均不依赖主观感受或语义判断。实验明确使用 ALARM、PRINTD、ASIA 三个知名 benchmark 网络作为评价场地，并与多个已有算法/基线进行统计比较，benchmark 结果构成核心性能主张的证据。因此同时满足'客观指标提升是唯一核心目标'和'明确 benchmark 表述'两项要求，strict_include=true。
- Confidence: 0.98

## Optimal Management of Virtual Infrastructures Under Flexible Cloud Service Agreements

- Year/journal: 2019 / Information Systems Research
- DOI: 10.1287/isre.2019.0871
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "总预期成本（含VM供应成本与SLA罚金成本）", "measurement_cn": "由随机动态规划模型计算，总预期成本 = 备份VM供应成本 + 预期违约罚金成本；基于服务合同参数（α、T、h、π）和故障/恢复过程（MTBF、MTTR）生成，并在合成数据和Amazon EC2定价/服务信用数据上计算。", "objectivity_reason_cn": "成本直接来源于合同价格、罚金费率、故障统计和资源数量，均可从合约和系统日志客观推导，不依赖人类感受、语义或价值判断。"}, {"name_cn": "成本节省率（如R[CL]、R[CE^on]、R[SISL^on]、R[MISL^on]）", "measurement_cn": "以静态无干预最优解或其他基准模型的预期成本为分母，计算相对成本减少百分比，见Table 1、2、4、5。", "objectivity_reason_cn": "由客观的预期成本数值简单算术计算得到，与主观感知无关。"}, {"name_cn": "算法竞争比（competitive ratio）", "measurement_cn": "在线算法成本与理想离线最优成本之比的最坏情况上界，通过Propositions 1、3、6做理论推导，均小于2。", "objectivity_reason_cn": "是定义严格、可按逻辑推导的数学比值，不涉及人类评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在Section 7计算实验和Section 8 Amazon EC2用例中，作者以Yuan et al. (2018)的静态无干预最优解（NI）、周期性策略中的最优CL模型、CL3模型等为基准，对比CL、CE^on、SISL^on、MISL^on等动态策略的预期总成本，汇报成本节省率；竞争比分析也以理想离线算法为基准比较最坏情况性能。
- Decision: 客观指标方面，全文核心指标为预期总成本及各策略成本节省率，均由合约价格、罚金、故障统计等可审计客观因素计算，不涉及主观判断；唯一核心目标是以动态优化降低总运营成本，模型、算法、竞争比分析和Amazon用例均服务于此，无并列的主观或理论机制贡献。Benchmark方面，作者在计算分析中明确使用Yuan et al. (2018)静态最优解、CL模型等作为显式比较基准，属于陈述式benchmark，这些基准评价直接支撑核心成本改进主张，且包含明确参照点。两模块均通过。
- Confidence: 0.98

## Process data properties matter: Introducing gated convolutional neural networks (GCNN) and key-value-predict attention networks (KVP) for next event prediction with deep learning

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113494
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "预测准确率 (Accuracy)", "measurement_cn": "10折交叉验证中，模型预测的下一活动标签与真实活动标签匹配的比例，按公式(8)计算", "objectivity_reason_cn": "活动标签是事件日志中的客观事件类别，匹配与否可确定性计算，不依赖人的感受或语义评价"}, {"name_cn": "F1-score (加权、宏、微平均)", "measurement_cn": "基于预测与真实标签的混淆矩阵计算精确率和召回率的调和平均，按公式(15)-(17)计算", "objectivity_reason_cn": "基于客观活动标签的计数和公式计算，不涉及主观判断"}, {"name_cn": "精确率 (Precision) 和召回率 (Recall)", "measurement_cn": "基于预测与真实标签的混淆矩阵计算，按公式(9)-(14)计算", "objectivity_reason_cn": "基于客观活动标签预测结果的计数，确定性计算"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: BPI'11 | BPI'12 | BPI'13 | Helpdesk | EnvLog
- Benchmark evaluation: 在11个真实事件日志benchmark数据集（BPI'11、BPI'12及其子集、BPI'13及其子集、Helpdesk、EnvLog）上，采用10折交叉验证评估GCNN、KVP、LSTM和SAE，并报告准确率、精确率、召回率、F1指标。结果表与已有方法（如LSTM [5]、LSTM [12]、LSTM [13]、SAE [9]、MANN [19]、CNN [20]、CNN [21]、RegPFA [31]）比较，证明GCNN和KVP在34/44组合上超越先前方法。
- Decision: 本文核心目标是在下一个事件预测任务上引入并评估GCNN和KVP，以客观预测性能（准确率、精确率、召回率、F1）提升为唯一核心贡献；所有评价均基于事件日志中的客观活动标签，不涉及主观感受或语义评价。全文存在明确benchmark表述，使用BPI'11、BPI'12、BPI'13、Helpdesk、EnvLog等公开基准数据集，在评价部分与多个现有方法比较，benchmark结果直接支撑'在34/44组合中超越先前方法'的核心主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.98

## Reducing the cost of accessing relations in incremental view maintenance

- Year/journal: 2007 / Decision Support Systems
- DOI: 10.1016/j.dss.2006.11.006
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "关系访问次数/增量维护表达式的处理代价", "measurement_cn": "使用线性工作量成本模型（linear work metric），根据维护表达式中操作数大小之和计算，并在实验中统计各基表在优化前后的访问次数。", "objectivity_reason_cn": "由关系大小、连接选择率等数据库可审计统计量按明确公式计算，不依赖人的感受、意义理解或价值判断。"}, {"name_cn": "视图更新时间（执行时间）", "measurement_cn": "在TPC-R数据仓库环境中，测量重计算方法、n-term方法与本文最优delta evaluation方法完成视图更新所需的时间。", "objectivity_reason_cn": "物理执行时间可由系统时钟和日志观测，属于可审计的客观性能指标。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: TPC-R benchmark
- Benchmark evaluation: 在TPC-R基准的schema和查询Q5/Q9基础上构造两个SPJ视图V1和V2，并在这些基准数据上比较重计算方法、n-term方法（即现有最优增量维护方法）与本文最优delta evaluation方法。实验在不同更新规模（2%–20%）和不同基表规模（100%–500%）下测量更新耗时，结果显示本文方法优于所有对比方法。多视图实验同样使用TPC-R查询派生视图，并比较ours(no sharing)与ours(sharing)。
- Decision: 文章核心目标是减少增量视图维护中的关系访问成本，核心成功指标是关系访问次数/维护表达式代价和实际更新时间，均为完全客观可观测指标；全文未使用主观量表或人类语义评价。核心贡献唯一且明确。实验在TPC-R这一命名公开基准上进行，基于TPC-R schema和查询构造视图，并以重计算方法、n-term方法等作为明确参照点，基准评价直接支撑“最优delta evaluation方法提升维护效率”的核心主张。因此两个模块均通过，严格纳入。
- Confidence: 0.98

## Reliable classification using neural networks: a genetic algorithm and backpropagation comparison

- Year/journal: 2000 / Decision Support Systems
- DOI: 10.1016/s0167-9236(00)00086-5
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "分类错误率（classification error percentage）", "measurement_cn": "测试集上被错误分类的样本数占总样本数的百分比，由网络输出类别与真实类别直接比较计算。", "objectivity_reason_cn": "分类错误率基于可审计的外部事实标签（如癌症诊断、信用卡批准、疾病类别等）计算，数值由数据决定，不依赖人的感受或主观评价。"}, {"name_cn": "平方误差百分比（squared error percentage）", "measurement_cn": "使用公式计算网络输出与目标输出的归一化平方误差百分比。", "objectivity_reason_cn": "该指标由网络输出值和目标值通过确定公式计算，不涉及主观判断，是客观的拟合误差度量。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: PROBEN1
- Benchmark evaluation: 在PROBEN1基准套件的10个真实世界分类数据集（Cancer、Card、Diabetes、Gene、Glass、Heart、Heartc、Horse、Soybean、Thyroid）上，用BP和GA分别训练神经网络，以测试集分类错误率和平方误差百分比为主要结果指标。结果表（Table 1、3、4）显示GA在所有或几乎所有问题上均优于BP，benchmark评价直接支撑了GA提升分类性能的核心主张。
- Decision: 客观指标方面，核心指标为测试集分类错误率和平方误差百分比，二者均由可审计的事实标签和确定公式计算，完全客观。唯一核心目标方面，全文围绕'GA在NN训练中优于BP'这一客观性能提升展开，无主观体验或理论机制等并列核心贡献。benchmark方面，明确采用公共基准套件PROBEN1的10个真实世界分类数据集，并在实验结果中将GA与BP进行系统比较，benchmark评价直接支撑核心改进主张，且存在明确参照点BP。因此两个模块均通过，strict_include=true。
- Confidence: 0.98

## SOA Performance Enhancement Through XML Fragment Caching

- Year/journal: 2012 / Information Systems Research
- DOI: 10.1287/isre.1110.0368
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "带宽消耗", "measurement_cn": "在模拟实验和案例研究中测量网络各hop传输的字节数，比较缓存与无缓存情况下的平均每hop带宽消耗。", "objectivity_reason_cn": "带宽消耗是网络传输字节数的物理量，独立于人的感知、语义或价值判断，可由模拟器或系统日志确定性记录。"}, {"name_cn": "端到端响应时间", "measurement_cn": "从服务消费者发出请求到收到完整响应的时间差，在模拟中通过线程时间差测量，在案例研究中通过往返请求-响应时间测量。", "objectivity_reason_cn": "响应时间是系统日志或计时器可观测的客观性能指标，与人的主观体验无关。"}, {"name_cn": "吞吐量", "measurement_cn": "在案例研究中，以每秒完成的请求数衡量，记录在不同并行请求线程数下的吞吐量变化。", "objectivity_reason_cn": "吞吐量是单位时间内完成的事务数，是可审计的系统性能事实。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: TPC-App benchmark
- Benchmark evaluation: 在TPC-App benchmark的数据库模式和负载特征上搭建案例研究实验环境，使用Cisco AON XML路由器和Tomcat应用服务器实现片段缓存，以响应时间和吞吐量为指标，与无缓存和完整消息缓存两种基线进行比较，并额外设计实验对比在唯一响应数量变化时片段缓存与完整消息缓存的性能差异。
- Decision: 客观指标方面：核心目标与贡献均为提升SOA服务性能，包括带宽消耗、响应时间和吞吐量，全部属于可确定性观测的物理/系统指标，不涉及任何主观构念或人类语义评价。唯一核心目标为客观指标提升，全文没有并列的理论、政策、制度等核心贡献。Benchmark方面：案例研究明确使用公开的TPC-App benchmark作为评价场地，配置其数据库和负载模式；该基准评价位于实验部分并直接支撑核心性能改进主张；比较对象包括无缓存基线和完整消息缓存，因此满足明确的benchmark门槛。两个模块均通过，strict_include为true。
- Confidence: 0.98

## Unlocking the Power of Voice for Financial Risk Prediction: A Theory-Driven Deep Learning Design Approach

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/17062
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "财务风险（股票波动率）预测误差", "measurement_cn": "目标变量为股票收益在未来3/5/10/30/60天窗口内的标准差（波动率），由CRSP每日股票价格计算；核心评估指标为样本外均方误差（MSE）及相对市场基准的样本外R²（R²_oos），并由Diebold-Mariano检验显著性。", "objectivity_reason_cn": "股票波动率由市场交易价格直接计算，是外部可核验的金融事实，不依赖任何人类感受、语义理解或价值判断。预测误差由模型预测值与实际计算值比较得出，完全客观。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在自建的6,047个财报电话会议测试集上，将DeepVoice与市场基准（fundamentals+historical risk）、仅用文本（DeepVoice w/o vocal）、仅用语音（DeepVoice w/o verbal）、特征拼接类机器学习模型、Contextual LSTM等进行比较，以样本外R²_oos为核心指标。结果显示DeepVoice在3/5/10/30/60天预测范围内R²_oos分别为7.31%、8.34%、4.28%、2.26%、7.45%，显著优于市场基准和所有对比方法，并用DM检验验证显著性。该benchmark评价直接支撑核心的预测精度提升主张。
- Decision: 文章以预测公司股票波动率（财务风险）的样本外误差（MSE/R²_oos）为核心目标，该指标完全由市场交易价格计算，客观可验证；研究问题、设计假设、评估和贡献均围绕提升这一客观指标，没有主观量表或人类评判作为成功标准，也没有并列的核心贡献。同时，文章在评价部分明确使用benchmark一词定义了市场基准和其他baseline，并在测试集上系统比较，benchmark结果直接支撑核心的预测精度提升主张，且具有明确参照点。因此两个模块均通过，strict_include=true。
- Confidence: 0.98

## A Prescriptive Analytics Method for Cost Reduction in Clinical Decision Making

- Year/journal: 2021 / MIS Quarterly
- DOI: 10.25300/misq/2021/14372
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "临床决策总成本（美元）", "measurement_cn": "对每个测试病例，根据方法作出的投资决策与分类决策，计算投资成本（无投资则为$0）与期望分类成本之和；分类成本依据分类成本矩阵C或投资后的新成本矩阵C并结合成本变化概率计算。在100次随机划分实验中汇总平均总成本，并与基准方法比较。", "objectivity_reason_cn": "成本以美元计价，来源于文献和医院费用等可审计财务事实，不依赖人的感受、价值判断或语义评价；决策标签是外部临床事实（是否应撤机、是否恶性肿瘤）。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: KDD Cup 2008 breast cancer data set (used in Appendix D)
- Benchmark evaluation: 在机械通气数据集（正文）和KDD Cup 2008乳腺癌数据集（附录D）上，将提出的ICSL方法与四种既有成本敏感学习方法（阈值移动THR、SMOTE、实例加权IW、MetaCost MC）进行系统对比；结果报告平均总成本、成本降低百分比及Wilcoxon符号秩检验，并在不同分类成本、成本变化概率、投资额和分类算法下做稳健性分析。
- Decision: 客观指标方面：核心成功指标为临床决策的总成本（美元），属于可直接观测、可审计的财务/事实指标；全文没有主观量表或语义评价作为核心结果，设计目标、问题定义、评价和贡献声明均围绕成本降低展开，因此满足客观指标和唯一核心目标门槛。Benchmark方面：文章明确以“benchmark methods”命名并系统评价ICSL与THR、SMOTE、IW、MC等既有方法的比较（以及在KDD Cup 2008上的评价），benchmark出现在实证评价部分，结果直接支撑成本降低的核心主张，并有明确参照点。两个模块均通过，strict_include=true。
- Confidence: 0.97

## A comparative analysis of data preparation algorithms for customer churn prediction: A case study in the telecommunication industry

- Year/journal: 2017 / Decision Support Systems
- DOI: 10.1016/j.dss.2016.11.007
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "AUC（ROC曲线下面积）", "measurement_cn": "由模型输出的流失概率与实际流失标签计算；AUC为随机正例排在随机负例之前的概率。", "objectivity_reason_cn": "流失标签是客户是否终止合约的事实状态，AUC由确定性排序统计计算，不依赖人的感受或语义评价。"}, {"name_cn": "Top Decile Lift (TDL)", "measurement_cn": "按预测流失概率将客户从高到低排序，取前10%客户中的流失密度与总体流失密度之比。", "objectivity_reason_cn": "基于实际事实流失标签和模型排序的客观比率，直接可审计，不依赖主观判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在电信客户流失数据集（以及额外的信用评分、响应建模数据）上，将优化后的LOGIT-DPT与Bag、B-Net、DT、NN、NB、RF、SVM、SGB等八个基准分类器在验证集上按AUC和TDL比较；同时对18种DPT组合进行系统比较。
- Decision: 本文核心是提升客户流失预测的完全客观性能指标AUC和TDL，并证明优化数据准备后的logistic回归与先进分类器相比具有竞争力；无任何主观量表或语义判断作为核心成功标准。全文在摘要、实验设计和结果部分均有明确benchmark/benchmarking表述，且以8个基准分类器和多种DPT组合作为参照点进行统计比较，符合benchmark_comparison_central。因此两模块均通过，strict_include=true。
- Confidence: 0.97

## A multivariate approach for multi-step demand forecasting in assembly industries: Empirical evidence from an automotive supply chain

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113452
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "预测准确度（NMAE）", "measurement_cn": "基于滚动源方案的实际需求与预测值的绝对误差归一化到目标值范围；实际需求来自 ERP 系统记录的周需求。", "objectivity_reason_cn": "误差由实际需求值与预测值直接计算，不依赖人的感受或语义评价，属于可审计的时间序列预测误差。"}, {"name_cn": "库存相关总成本（TC）", "measurement_cn": "根据预测偏差导致的持有成本与缺货成本加权计算，采用固定成本因子，数据来自 ERP 实际需求。", "objectivity_reason_cn": "成本和库存积压/缺货是可审计事实，计算规则固定，不涉及主观评价。"}, {"name_cn": "损失率与填充率（LR/FR）", "measurement_cn": "基于超量预测与实际需求的比率、需求满足率定义，用公式量化。", "objectivity_reason_cn": "由实际需求与预测值决定，客观可复核。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在 Bosch 汽车电子真实数据集上，用多元模型（MLP、RF、SVR、AutoML、ERNN、ARIMAX）与单变量基准模型（Naïve、Theta、ARIMA）在滚动源方案下进行多步预测对比，报告 NMAE、TC、LR/FR 等客观指标；基准模型是可比较的明确参照点，结果用于证明多元方法在预测与库存绩效上的提升。
- Decision: 客观指标方面：核心指标为预测误差（NMAE）、库存相关成本（TC）、损失率/填充率（LR/FR），全部来自 ERP 实际需求与预测值的确定性计算，不依赖主观感受或语义评价；核心目标与贡献声明均围绕预测与库存绩效提升，无并列主观或理论核心目标。Benchmark 方面：第5.3节明确命名为“Baseline & benchmark models”，列出 Naïve、Theta、ARIMA 等基准，并作为实验评价的参照点；多个结果表将多元模型与基准比较，证明客观指标提升，benchmark 评价直接支撑核心主张。因此两个门槛均通过，strict_include=true。
- Confidence: 0.97

## A synthetic informative minority over-sampling (SIMO) algorithm leveraging support vector machine to enhance learning from imbalanced datasets

- Year/journal: 2018 / Decision Support Systems
- DOI: 10.1016/j.dss.2017.11.006
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "G mean（几何平均）", "measurement_cn": "基于测试集混淆矩阵计算真正率TPR和真负率TNR，取几何平均√(TPR×TNR)", "objectivity_reason_cn": "分类性能指标，由客观预测类别与固定事实标签比对确定，不依赖人类主观感受或语义评价"}, {"name_cn": "AUC（ROC曲线下面积）", "measurement_cn": "基于测试集预测概率与真实标签，通过改变决策阈值计算ROC曲线下面积", "objectivity_reason_cn": "客观的分类性能度量，基于外部客观类标签与模型输出，不涉及主观评价"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: UCI Machine Learning Repository 的15个公开benchmark不平衡数据集：Liver Disorders、Ionosphere、Pima Indians Diabetes、Breast Cancer Wisconsin Original、Iris、Yeast、Statlog Vehicle Silhouettes、Contraceptive Method Choice、BreastC20、Vowel、Ecoli、Libras12、Libras34、Glass、BreastC10
- Benchmark evaluation: 在15个UCI benchmark数据集上，将SIMO和W-SIMO与under-sampling、SMOTE、borSMOTE、safe-level SMOTE、cluster SMOTE、SMOTE-IPF、cost-sensitive SVM以及原始数据比较；使用线性SVM、RBF SVM、逻辑回归和决策树，进行4折交叉验证重复10次，报告G mean和AUC。结果显示线性SVM下SIMO/W-SIMO在所有数据集上排名前两位，整体排名1.1和1.9，优于其他方法。
- Decision: 客观指标方面：核心成功指标为G mean和AUC，两者基于固定事实标签（疾病、类别等）和模型预测结果计算，完全客观，不依赖人类主观评价。唯一核心目标：全文从研究问题、设计目标、评价到贡献声明均集中在提升不平衡数据分类性能，无其他并列核心目标。Benchmark方面：明确表述使用15个UCI公开benchmark数据集作为评价场地，结果与多个现有方法及原始数据比较，benchmark结果直接支撑核心改进主张，且具有明确参照点。因此严格包含为true。
- Confidence: 0.97

## An adaptive learning to rank algorithm: Learning automata approach

- Year/journal: 2012 / Decision Support Systems
- DOI: 10.1016/j.dss.2012.08.005
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "Precision at position n (P@n)", "measurement_cn": "在TREC 2003/2004、OHSUMED、MQ2007等LETOR数据集上，用官方Eval-Rank.pl工具基于二元/多级相关性标注计算前n位中相关文档比例", "objectivity_reason_cn": "相关性标签是数据集中固定的事实/外显标签；P@n是确定性的可审计计数，与研究者或用户主观感受无关"}, {"name_cn": "Mean Average Precision (MAP)", "measurement_cn": "在各数据集的5折测试集上，由LETOR官方评价工具计算所有查询的AP平均值", "objectivity_reason_cn": "基于固定相关性标签的确定性信息检索指标，不依赖人的体验或语义评价"}, {"name_cn": "Normalized Discount Cumulative Gain (NDCG)", "measurement_cn": "在固定多级相关性标签（TREC二元、OHSUMED和MQ2007三级）上，由LETOR评价工具计算折扣累积增益的归一化值", "objectivity_reason_cn": "NDCG是建立在数据集固定相关性等级上的客观IR性能指标，有明确公式和标准化计算"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: LETOR | TREC 2003 (Topic Distillation, TD2003) | TREC 2004 (Topic Distillation, TD2004) | OHSUMED | MQ2007
- Benchmark evaluation: 在LETOR包中的TD2003、TD2004、OHSUMED、MQ2007四个公开benchmark数据集上，使用LETOR官方Eval-Rank.pl工具评价LRUF并与SVMRank、LREG、LRDRS三个baseline比较P@n、MAP、NDCG；结果显示LRUF在几乎所有数据集和指标上明显优于三个baseline。
- Decision: 客观指标方面：本文核心目标为提升搜索引擎排序的P@n、MAP、NDCG，这些指标基于数据集中的固定相关性标签，由标准公式和LETOR官方工具计算，完全不依赖用户或专家的主观评价；全文的研究问题、算法设计、实验和结论均围绕这一客观指标提升展开，且不存在并列的核心贡献。Benchmark方面：作者在第4节明确将TREC 2003、TREC 2004、OHSUMED、MQ2007作为“renowned benchmark data collections”，并将LETOR称为benchmark数据集包，评价位于实验部分且是支撑核心主张的主要证据；结果表与SVMRank、LREG、LRDRS三个明确baseline比较，证明的是提升而并非孤立数值。因此strict_include=true。
- Confidence: 0.97

## An integrated two-stage model for intelligent information routing

- Year/journal: 2006 / Decision Support Systems
- DOI: 10.1016/j.dss.2005.01.007
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "平均精确率 PAVG（Average Precision）", "measurement_cn": "在测试集上，对每个查询，每当检索到一篇标注为相关的文档时计算一次精确率，求平均值并除以集合中相关文档总数；各查询取平均。", "objectivity_reason_cn": "相关性的金标准来自 TREC 数据集的既有相关性判定标签，属于外部固定事实标签；计算基于文档排序位置和标签，不依赖作者或用户的主观质量评价。"}, {"name_cn": "前十位精确率 P10", "measurement_cn": "检索结果前 10 篇文档中相关文档的比例，基于 TREC 相关性标签计算。", "objectivity_reason_cn": "同样基于公开语料库中的相关性标签，值可确定性地从排序结果计算。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: TREC AP 新闻语料（three-year news corpus from the Associated Press） | TREC 10GB Web 数据（10 GB web data used in TREC）
- Benchmark evaluation: 在两个基准语料（TREC 的 AP 新闻语料和 TREC 10GB Web 数据）上，将提出的两阶段模型（系统构造 PQ + GP 自适应排序函数）与 Okapi BM25 固定排序及 SVM 分类器基线比较，测试集上报告各查询 PAVG 与 P10 的平均值。
- Decision: 客观指标方面：核心成功指标是 PAVG 和 P10，均基于 TREC 数据集的既有相关性标签计算，属于 objective_fixed_factual_labels；研究目标、实验设计和贡献声明均围绕检索性能提升展开，未发现并列核心目标。Benchmark 方面：全文明确将 TREC AP 和 TREC Web 数据作为两个 benchmark 数据集合进行模型评价，评价位于实验部分，结果与 Okapi、SVM 等明确基线比较，且该 benchmark 比较直接支撑核心性能提升主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.97

## An investigation of Zipf's Law for fraud detection (DSS#06-10-1826R(2))

- Year/journal: 2008 / Decision Support Systems
- DOI: 10.1016/j.dss.2008.05.003
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "审计命中率（Audit Hit Rate, AHR）", "measurement_cn": "检测出的欺诈/攻击记录数除以该簇总记录数，以百分比表示；由Zipf Analysis分簇后的计数计算。", "objectivity_reason_cn": "基于KDDCUP数据集的已知攻击/正常标签或案例中经验证的真实欺诈记录，可通过系统日志和真实类别计数确定，不依赖人的感受或语义评价。"}, {"name_cn": "贝叶斯审计命中率（BAHR）", "measurement_cn": "由混淆矩阵得到P(F|S)的条件概率，表示欺诈信号中真实欺诈的比例，公式给定。", "objectivity_reason_cn": "由真实类别和预测信号的可审计计数计算，构念为客观分类性能。"}, {"name_cn": "混淆矩阵准确率与假阳性率", "measurement_cn": "在KDDCUP'99五类（Normal、Probe、DOS、U2R、R2L）上统计正确预测比例和负例误报比例。", "objectivity_reason_cn": "类别标签为KDDCUP公开基准中的客观事实标签，指标计算公式确定。"}, {"name_cn": "总/平均误分类成本（TMC/AMC）", "measurement_cn": "使用KDDCUP官方成本矩阵对测试样本的误分类代价求和并除以样本数。", "objectivity_reason_cn": "成本矩阵和类别标签均为外部客观给定，值可通过预测结果确定。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: KDDCUP'99 intrusion detection dataset
- Benchmark evaluation: 在KDDCUP'99公开入侵检测数据集上，以Zipf Analysis作为预处理器（关键值1%、2%、5%），再使用KDDCUP'99获胜的C5.0决策树算法进行分类，并与无预处理的baseline及KDDCUP'99 benchmark结果比较AHR、BAHR、混淆矩阵准确率/假阳性率和误分类成本。
- Decision: 文章核心目标为开发并验证基于Zipf定律的欺诈检测机制，评价指标AHR、BAHR、混淆矩阵准确率/FP率和误分类成本均针对KDDCUP'99已知攻击/正常标签等客观事实计算，不涉及主观感知或语义判断；全文以提升这些完全客观检测指标为唯一核心目标与贡献。同时，文章明确将KDDCUP'99命名为benchmark数据集并在评价语境中使用，比较对象包括100%抽样、KDDCUP'99 benchmark率、获胜算法及无预处理baseline，benchmark评价直接支撑核心性能提升主张。因此两个模块全部通过，严格纳入。
- Confidence: 0.97

## Application of a hybrid of genetic algorithm and particle swarm optimization algorithm for order clustering

- Year/journal: 2010 / Decision Support Systems
- DOI: 10.1016/j.dss.2010.05.006
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "SED（簇内欧氏距离和）", "measurement_cn": "对 Iris、Glass、Vowel、Wine 等数据集，按聚类中心计算所有数据点到所属簇中心的欧氏距离之和；每个算法运行30次并取平均和标准差，实际订单数据运行10次。", "objectivity_reason_cn": "SED由公式直接计算，数值来源是数据集特征和算法输出的质心，不依赖人的感受、意义理解或价值判断。"}, {"name_cn": "生产准备时间、总生产时间、机器闲置时间", "measurement_cn": "使用案例公司提供的生产计划，按照FCFS和SPT规则模拟材料绑定、安装等过程，统计改进前后的材料准备时间、总生产时间和机器闲置时间。", "objectivity_reason_cn": "这些时间指标来自确定性工时测算和算法聚类分组结果，属于可审计的技术/时间指标，不依赖主观评价。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: Iris | Glass | Vowel | Wine
- Benchmark evaluation: 在UCI的Iris、Glass、Vowel、Wine四个公开benchmark数据集上评价HGAPSOA及GA、GKA、PSO、PSKO、GA-PSO、GA-PSKO六种对比算法，使用SED作为性能指标，报告30次运行的平均值与标准差，并进行Mann-Whitney U显著性检验；结果显示HGAPSOA在四个数据集上的平均SED均最低。
- Decision: 文章以完全客观的SED和实际生产时间/机器闲置时间作为核心成功指标；研究目标明确为通过订单聚类和HGAPSOA算法提升这些客观指标，且没有并列的主观核心目标或理论核心贡献。同时，文章明确将Iris、Glass、Vowel、Wine作为benchmark数据集，并在实验评价部分对HGAPSOA与多种baseline算法进行SED比较，benchmark结果直接支撑核心提升主张。因此三个模块均通过，strict_include为true。
- Confidence: 0.97

## Capital shortfall: A multicriteria decision support system for the identification of weak banks

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113526
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "整体分类准确率（OCA）", "measurement_cn": "基于测试样本，模型分类正确的银行观测数除以总观测数；标签来自监管压力测试/资本注入事件的实际结果（资本需求 vs 无资本需求）。", "objectivity_reason_cn": "分类标签对应真实监管决定和实际资本注入事实，不依赖人的主观体验或价值判断；计算方式为确定性比对。"}, {"name_cn": "平均分类准确率（ACA）", "measurement_cn": "敏感性（SENS）和特异性（SPEC）的算术平均；SENS为无资本需求银行正确分类比例，SPEC为有资本需求银行正确分类比例。", "objectivity_reason_cn": "基于事实标签的客观统计，不涉及人类主观评价。"}, {"name_cn": "AUROC（ROC曲线下面积）", "measurement_cn": "基于模型全局得分对两类银行排序，计算ROC曲线下面积；衡量所有阈值下的判别能力。", "objectivity_reason_cn": "由客观分类得分和事实标签计算得到，公式确定。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在第五节“Comparison with other measures”中，作者用S1规格并采用out-of-sample bootstrap，将UTADIS模型与逻辑回归（LR）、SRISK、Texas Ratio进行比较，报告OCA、AUROC等分类性能指标，结果显示UTADIS模型整体优于比较对象。
- Decision: 客观指标方面，核心目标是预测银行是否有资本需求，标签来自监管压力测试结果和实际资本注入事件，属于外部可核验事实，所有成功指标均为分类准确率和AUROC等客观指标，且提升预测性能是唯一核心目标。Benchmark方面，作者在引言和评价部分明确使用benchmark一词并与逻辑回归、SRISK、Texas Ratio进行比较，比较结果直接支撑了核心预测能力提升主张，满足benchmark_comparison_central条件。因此两个模块均通过，strict_include为true。
- Confidence: 0.97

## Cost-Sensitive Learning via Priority Sampling to Improve the Return on Marketing and CRM Investment

- Year/journal: 2012 / Journal of Management Information Systems
- DOI: 10.2753/mis0742-1222290110
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "累积利润提升（Cumulative Profit Lift）", "measurement_cn": "基于测试数据中实际客户购买金额/利润，计算按模型排序后各十分位的实际累计利润与随机模型的累计利润之比（乘以100）。", "objectivity_reason_cn": "利润、购买金额、成本均为可审计的事实金额，不依赖任何人的感受、语义判断或价值偏好。"}, {"name_cn": "实际增量利润（Lifted Profit in Dollars）", "measurement_cn": "模型在特定分位（尤其是前两个十分位）下实现的利润减去随机模型实现的利润，以美元计。", "objectivity_reason_cn": "由真实交易金额和固定成本计算得出，是确定性的财务数值。"}, {"name_cn": "响应提升/TPR提升（Response Lift / TPR Lift）", "measurement_cn": "模型在前几个十分位识别出的真实买家/流失者数量与随机模型期望数量的比值；流失者标签为客观状态。", "objectivity_reason_cn": "购买行为与流失状态是外部可核验的事实标签，不涉及主观感知。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: 1998 Knowledge Discovery and Data Mining competition (KDD Cup 1998) dataset | 2003 Duke University data mining competition customer churn dataset
- Benchmark evaluation: 在KDD Cup 1998数据集上，priority sampling for logistic regression 在前两个十分位的profit lift达到882.4和571.6，显著高于logistic regression balanced（723.5/473.5）、expected cost（618.3/416.5）和AdaC2（544.4/312.9）；实际lifted profit在60%邮寄深度达$15,800，高于竞赛获胜者$14,712。在Duke 2003数据集上，priority sampling在top decile profit lift为299.7（logistic regression）和301.4（naive Bayes），lifted profit为$18,634和$18,794，均高于AdaC2等的$18,355。这些benchmark结果直接支撑核心客观指标（利润提升）的核心主张。
- Decision: 客观指标方面：文章以利润提升、实际增量利润、响应/TPR提升等为评价指标，全部基于真实交易金额、成本和事实标签，不依赖人类主观感知或语义评价，属于完全客观可直接观测的指标。唯一核心目标：全文的研究问题、算法设计、评价和贡献声明均围绕提高营销/CRM投资回报这一客观利润指标，没有并列的主观结果或理论机制等作为同等核心贡献。Benchmark方面：文章虽未使用“benchmark”一词，但在Study 2和Study 3明确命名了公开数据挖掘竞赛数据集（2003 Duke University competition、1998 KDD Cup）作为评价场地，并在这些benchmark上比较了多个基线方法（logistic regression、expected cost、AdaC2、naive Bayes）和竞赛获胜者，benchmark结果直接支撑“priority sampling提升利润”的核心主张。因此两个模块均通过，strict_include为true。
- Confidence: 0.97

## Design of a shopbot and recommender system for bundle purchases

- Year/journal: 2006 / Decision Support Systems
- DOI: 10.1016/j.dss.2006.05.005
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "总购买成本/节省百分比", "measurement_cn": "通过CPLEX或GRAB算法求解捆绑购买模型得到最小总成本，与单项最低价格之和（benchmark）比较计算节省百分比；数据来自14家零售商10天内收集的194个真实捆绑促销和36个产品价格，每个bundle size随机生成1000次模拟", "objectivity_reason_cn": "成本和价格是可审计的交易事实，计算公式固定，不依赖人的感受或语义判断"}, {"name_cn": "免费赠品识别数量与价值", "measurement_cn": "求解最优捆绑组合后，额外获得的商品（多出所需商品集合的部分）的数量和价格价值；以免费赠品最低单项价格计算净节省", "objectivity_reason_cn": "免费赠品由模型解直接给出，其价值源于商品价格，客观可核验"}, {"name_cn": "推荐系统额外节省", "measurement_cn": "在已选捆绑基础上逐一添加候选推荐商品，计算新增成本与推荐商品基准价值，以基准价值节省百分比和额外成本百分比表示", "objectivity_reason_cn": "推荐结果由模型解出，节省和成本均基于价格数据，客观可计算"}, {"name_cn": "算法运行时间与最优性差距", "measurement_cn": "将GRAB算法与CPLEX通用整数规划求解器比较，统计时间节省比例和平均目标函数值相对最优解的百分比差距", "objectivity_reason_cn": "运行时间和目标函数值都是系统日志和计算结果，客观可测量"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 以随机生成的2到20件商品组合为测试集，每个规模1000个实例，使用14家零售商收集的194个真实捆绑数据。基准为所需商品各自最低售价之和，比较CPLEX最优解和GRAB算法的节省率、免费赠品价值以及推荐系统的新增成本和节省。结果表明算法能带来显著节省（中位节省10%，近10%案例节省超20%），推荐系统节省超过75%。
- Decision: 客观指标门：核心成功指标为购买成本、节省金额/百分比、免费赠品价值、算法运行时间和最优性差距，全部为客观可测量事实，不依赖人类感受或语义判断；唯一核心目标是设计模型/算法以最大化捆绑购买节省并推荐高节省商品，无其他并列核心目标。benchmark门：全文存在明确的benchmark表述，实验部分以单项最低价格之和作为基准，并与CPLEX最优解比较，benchmark结果直接支撑节省和免费赠品主张；benchmark处于评价语境、有明确比较器且为核心主张服务。因此 strict_include=true。
- Confidence: 0.97

## Efficient identity matching using static pruning q-gram indexing approach

- Year/journal: 2015 / Decision Support Systems
- DOI: 10.1016/j.dss.2015.02.015
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "匹配有效性：Precision、Recall、F-measure", "measurement_cn": "在SecondString census数据集和FEBRL credit application数据集上，将算法输出的匹配/非匹配结果与真实同一个人标签（rec_id或生成记录的真实身份标签）对比，按公式(1)-(3)计算Precision、Recall、F-measure。", "objectivity_reason_cn": "两条身份记录是否指向同一真实个人是外部可核验事实，不依赖人的感受、意义理解或价值判断；评价指标由算法输出和事实标签确定性计算。"}, {"name_cn": "效率：比较次数、约简率RR、完成时间", "measurement_cn": "统计算法执行的候选记录对比较次数，以pairwise方法N(N-1)/2为基线，按公式RR=1-n_evaluated/n_pairwise计算约简率；同时记录Java实现完成所有匹配判断的时间（ms）。", "objectivity_reason_cn": "比较次数和时间是可审计的计算日志和系统时间，不依赖主观评价。"}, {"name_cn": "可扩展性：Scalability ∝ N/t", "measurement_cn": "按Wang et al. [32]的可扩展性公式，用记录数N与算法完成时间t的比值评估，并在10,000至50,000条递增数据上观测。", "objectivity_reason_cn": "由记录的客观数量和可审计运行时间计算，属客观技术性能指标。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: ADIM (adaptive detection identity matching) [32] | Pairwise identity matching approach | SecondString census dataset | Credit application dataset from [24]（FEBRL synthetic dataset）
- Benchmark evaluation: 在SecondString census数据集（841条记录，344对真实匹配）和FEBRL credit application合成数据集（由52,696条记录生成不同规模，并与ADIM、pairwise比较）上评价提出的static pruning q-gram索引身份匹配技术。有效性benchmark：census F-measure 0.674（pairwise 0.636，ADIM 0.543），credit F-measure 0.973（pairwise 0.960，ADIM 0.709）。效率benchmark：与ADIM相比，census数据集比较次数从218,112降至3,608（减少98%），完成时间从1,268ms降至31ms（减少97%）；credit应用数据集比较次数减少96%，完成时间大幅下降。可扩展性benchmark：在10k-50k递增数据上，提出方法优于ADIM。
- Decision: 客观指标模块通过：核心指标包括匹配有效性（F-measure等，基于同一真实个人这一事实标签的预测性能）以及效率（比较次数、RR、完成时间）、可扩展性（N/t），全部为客观可测量指标；没有满意度、感知质量、专家评分等主观构念作为核心结果。唯一核心目标是提升效率同时保持/提升匹配有效性，全文围绕H1-H3三个客观假设和实验展开，没有并列的主观或理论贡献。Benchmark模块通过：引言明确使用benchmark动词将提出方法与ADIM和pairwise进行比较；实验部分多处将pairwise/ADIM作为baseline benchmark，并在census和credit application数据集上评价；benchmark结果直接用于支持比较次数、完成时间、F-measure和可扩展性的核心提升主张；具有明确参照点（pairwise基线和ADIM）。因此strict_include=true。
- Confidence: 0.97

## Fast Forecasting of Unstable Data Streams for On-Demand Service Platforms

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2023.0130
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "SMAPE（对称平均绝对百分比误差）", "measurement_cn": "基于预测demand与实际demand的误差，计算每个区域每小时预测误差并求平均，结果以相对于FFUDS的百分比表示。", "objectivity_reason_cn": "直接计算可观察的实际demand与预测demand之间的差异，不依赖人的感受或语义判断。"}, {"name_cn": "RMSE（均方根误差）", "measurement_cn": "平方损失函数取平均后开平方，用于评估预测精度。", "objectivity_reason_cn": "从实际demand与预测值计算，客观可测量。"}, {"name_cn": "经济损失（货币化的预测误差）", "measurement_cn": "使用用户定义的不对称损失函数，根据低估/高估demand的不同每次单位成本计算货币损失，并汇总成年度英镑收益。", "objectivity_reason_cn": "基于明确的成本和实际demand差异计算，客观可审计。"}, {"name_cn": "计算时间（秒）和云计算成本（美元）", "measurement_cn": "测量一次每日顺序更新跨所有区域的估计和预测所需秒数，以及按云服务单价折算的成本。", "objectivity_reason_cn": "是系统日志中的物理时间与成本，客观可测量。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在UK按需配送平台294个区域的数据集以及NYC Citi Bike公共自行车系统数据集上，将FFUDS与Naive、Prophet、LSTM、SARIMA、ETS（部分加入break detection的变体）进行对比，报告预测误差和计算时间。
- Decision: 本文开发FFUDS预测框架，其核心目标是提升预测准确性（SMAPE、RMSE、经济损失）和计算速度，所有核心成功指标均为客观可测量且不依赖主观判断；全文明确以benchmark形式比较FFUDS与多个基准方法（Naive、Prophet、LSTM、SARIMA、ETS），并有明确参照点和提升证据，因此同时满足客观指标唯一核心目标和明确benchmark表述。
- Confidence: 0.97

## Long-term stock index forecasting based on text mining of regulatory disclosures

- Year/journal: 2018 / Decision Support Systems
- DOI: 10.1016/j.dss.2018.06.008
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "预测均方根误差（RMSE）", "measurement_cn": "基于真实股指水平与模型预测水平的差异，按标准公式计算；同时使用Diebold-Mariano检验的p值判断误差差异显著性。", "objectivity_reason_cn": "RMSE和DM检验均基于公开可观察的金融时间序列数据和模型预测值，由确定性公式计算，不依赖任何人类感受、语义理解或价值判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在自建的滞后数据基准（线性自回归、带滞后输入值的多种机器学习模型）上，评估不同文本模型（情感特征、tf-idf机器学习、降维等）对DAX、CDAX、STOXX Europe 600在多个预测视界上的RMSE，并使用Diebold-Mariano检验比较误差差异。结果显示，尤其在长期预测（如24个月）中，文本模型相对基准模型取得显著RMSE降低。
- Decision: 该文核心目标为通过文本挖掘提升股指预测精度，核心结果指标RMSE及其显著性检验完全客观，且是唯一核心目标与贡献。全文在实验设置、结果表和结论中明确使用benchmark一词，将滞后数据模型作为基准，系统比较文本模型的预测误差，并以RMSE降低作为核心证据。文本模型相比明确参照点（lagged baseline）展示了提升，因此同时满足唯一客观指标改进和明确benchmark表述两个条件。
- Confidence: 0.97

## Process mining on noisy logs — Can log sanitization help to improve performance?

- Year/journal: 2015 / Decision Support Systems
- DOI: 10.1016/j.dss.2015.08.003
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "行为精确率与行为召回率（Behavioral precision/recall）", "measurement_cn": "将日志中的轨迹在参考模型与挖掘模型上回放，比较每一步启用的活动集合的交集与大小，按轨迹出现频率加权计算，值在[0,1]", "objectivity_reason_cn": "基于Petri网中启用的活动和因果关系集合的数学计算，不依赖人的感受或语义判断"}, {"name_cn": "结构精确率与结构召回率（Structural precision/recall）", "measurement_cn": "比较参考模型与挖掘模型因果关系集合的交集大小除以各自因果关系总数，值在[0,1]", "objectivity_reason_cn": "基于模型结构的因果关系集合的集合运算，完全客观可审计"}, {"name_cn": "模型紧凑性（places/transitions/arcs数量）", "measurement_cn": "统计挖掘模型中的库所数、变迁数和弧数", "objectivity_reason_cn": "直接计数模型元素，客观可验证"}, {"name_cn": "工作流正确性（Woflan验证结果）", "measurement_cn": "使用Woflan工具检查模型是否通过正确性验证", "objectivity_reason_cn": "工具基于工作流网的数学性质判定，不涉及主观评价"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 作者自建六个参考过程模型（复杂程度递增的level 0–5）作为基准，在两个知名过程挖掘算法（Alpha++和Heuristics Miner）上评价日志净化前后挖掘模型的性能；核心结果（Table 10）对比了noisy log和sanitized log在行为/结构精确率与召回率四个指标上的表现，并报告了提升百分比；还使用Woflan检验模型正确性及模型紧凑性。
- Decision: 文章唯一核心目标是通过日志净化（log sanitization）提升过程挖掘模型的质量，所有评价指标均为可计算的客观指标（行为/结构precision/recall、模型紧凑性、Woflan验证），没有任何主观量表或人类语义评价作为核心成功标准；全文存在明确的benchmark表述：作者自建六个参考过程模型作为基准，并将两个算法在noisy与sanitized logs上的结果进行系统化对比，benchmark评价直接支撑核心提升主张，且有明确参照点。因此严格纳入条件全部满足。
- Confidence: 0.97

## RADAR: A Framework for Developing Adversarially Robust Cyber Defense AI Agents with Deep Reinforcement Learning

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2024/17339
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "逃避率（Evasion Rate, ER）", "measurement_cn": "由RL攻击生成器生成的恶意软件变体中，能够逃避目标恶意软件检测器检测的比例，按每类恶意软件和总体计算；根据检测器返回的恶意/良性二元判定统计", "objectivity_reason_cn": "检测结果是系统对恶意/良性事实标签的判定，不依赖人类满意度、偏好或语义评价；逃避成功与否是可审计的外部事实，数据来自系统日志和检测器输出"}, {"name_cn": "假阳性率（False Positive Rate, FPR）", "measurement_cn": "良性样本被错误检测为恶意的比例，在鲁棒化前后通过干净Windows安装获取的良性可执行文件上计算", "objectivity_reason_cn": "良性/恶意标签是外部可核验事实，错误分类计数为客观可测结果；不涉及人类主观体验"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: VirusTotal malware repository（作为测试数据来源，非公开基准套件） | EMBER（Figure 9 标题中称LGBM为EMBER Malware Detector，但实验主体使用VirusTotal测试床）
- Benchmark evaluation: 在恶意软件检测任务上，将r-VAC与8种基准对抗攻击方法（Random actions、BFA、EvadeHC、GAMMA、Surrogate RNN、PG、DDQN、Rainbow、MAB-malware、ACER、A3C）在LGBM、MalConv、NonNeg三个检测器上比较逃避率；随后通过RL-RO对检测器进行鲁棒化，比较鲁棒化前后的逃避率与FPR，并在重复博弈中比较多轮模型。
- Decision: 客观指标：核心指标为逃避率（ER）与假阳性率（FPR），两者依据恶意/良性事实标签和检测器输出确定，不依赖人类主观评价，符合完全客观指标；唯一核心目标：研究问题、设计目标、评价结构和贡献声明均围绕提升防御AI代理的对抗鲁棒性这一客观指标展开，无并列核心目标；benchmark：全文存在多处明确的benchmark表述（'benchmark methods'、'selected benchmark methods'、'benchmark evaluation results'），且这些benchmark比较位于评价部分，包含多个显式baseline和鲁棒化前后对照，用于直接支撑核心的逃避率提升与鲁棒性提升主张。因此严格通过。
- Confidence: 0.97

## Robust ensemble learning for mining noisy data streams

- Year/journal: 2011 / Decision Support Systems
- DOI: 10.1016/j.dss.2010.11.004
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "预测准确率（Aacc）及派生排序指标（AR、#W、#L）", "measurement_cn": "将数据流按块划分，用当前模型预测下一数据块实例的类标签，计算预测标签与真实标签一致的百分比；Aacc为所有块的均值，AR为平均排序，#W/#L为各方法排名第一/最后的次数。传感器流实验还报告系统训练时间。", "objectivity_reason_cn": "类标签来自人工生成规则、传感器ID或KDDCUP'99客观类别，不依赖人的感受、质量评价或语义偏好；准确率、排序、运行时间均可由系统日志和标签对比确定性计算。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: KDDCUP'99 intrusion detection dataset | wireless sensor stream（公开测试数据流）
- Benchmark evaluation: 在KDDCUP'99上构造随机选择、随机噪声、重排、重排噪声四种数据流，将AE与Tree、HE、WE、VE比较，报告Aacc、AR、SR、#W、#L；在无线传感器数据流上比较AE与其组件算法、不同HE变体的平均准确率和系统训练时间。结果表显示AE在含噪场景下多数取得最高准确率和最低损失次数。
- Decision: 客观指标方面：核心成功标准为预测准确率、排序和运行时间，均由数据标签和系统时间确定性计算，不依赖主观判断；核心目标是提升含噪数据流上的预测准确率，没有其他并列核心目标。Benchmark方面：全文在评价语境中使用KDDCUP'99这一公开基准数据集和公开无线传感器测试流，并系统比较AE与Tree、HE、WE、VE等基线；这些benchmark结果正是支撑AE准确率提升的核心证据。因此两个模块均通过，strict_include=true。
- Confidence: 0.97

## A Theory-Driven Deep Learning Method for Voice Chat–Based Customer Response Prediction

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1196
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "AUC（ROC曲线下面积）", "measurement_cn": "基于10,625条真实语音对话，预测客户是否在30天内到店；通过5次独立十折交叉验证得到的50个测试折计算AUC均值与标准差。", "objectivity_reason_cn": "客户到店行为是外部可审计事实标签，AUC由预测概率与真实到店标签计算，不依赖人的感受、语义理解或价值判断。"}, {"name_cn": "KS统计量和H measure", "measurement_cn": "同一二分类预测任务上的辅助鲁棒性指标。", "objectivity_reason_cn": "均由预测分数和真实到店标签客观计算。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在由10,625个真实车载语音对话构成的四个数据集（full/balanced/long/short）上，以文本、音频及文本+音频特征评估DSDL与12个深度学习方法；DSDL在所有数据集和特征组合上的AUC均最高，代表性结果为full data set Text+Audio AUC 84.78%，而最高基准GAS为82.70%。
- Decision: 核心目标与核心指标均为客观可审计的客户响应预测：预测客户是否在30天内到店的二分类标签，核心成功指标为AUC等客观分类性能。全文不存在用户调研、专家评分、满意度量表等主观核心结果；期望-不一致理论仅作为方法设计依据，不构成并列的理论贡献。实验部分明确将12个现有深度学习方法称为benchmarks，并系统地在四个真实数据集上比较，DSDL在客观AUC指标上一致优于这些基准，benchmark评价直接支撑核心提升主张。因此两个模块均通过，严格纳入。
- Confidence: 0.96

## A decision support system for stock investment recommendations using collective wisdom

- Year/journal: 2014 / Decision Support Systems
- DOI: 10.1016/j.dss.2013.10.005
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "投资组合绝对回报", "measurement_cn": "从10万欧元初始资金出发，按系统推荐策略模拟建仓和调仓，使用实际股票价格和交易成本规则计算期末资产价值和收益率；比较对象为DAX指数买入持有和公募基金。", "objectivity_reason_cn": "资产价值和收益率由市场价格、订单价格和交易成本决定，不依赖人的感受、语义判断或质量评价。"}, {"name_cn": "Sharpe Ratio（Reward-to-Variability-Ratio）", "measurement_cn": "以每日收益的均值除以标准差计算，用于比较不同组合的风险调整后回报。", "objectivity_reason_cn": "收益和波动率均从可审计的市场价格序列计算，属于客观财务绩效指标。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: DAX German market index
- Benchmark evaluation: 在2009年1月至2010年12月观察期内，原型系统通过两个测试场景（Test 1：每日投资最佳评级ISIN；Test 2：对crowd Top10使用Markowitz组合优化并月度调仓）与DAX指数买入持有策略和两只公募基金进行比较。结果显示Test 1期末收益率123.2%（扣除交易成本88.5%），Test 2期末收益率110.6%（扣除交易成本99.8%），均大幅高于DAX基准的40.6%；Sharpe Ratio分别为0.0648和0.0791，高于DAX的0.0581以及两只公募基金的0.0604和0.0476。
- Decision: 客观指标方面，核心成功指标是投资组合绝对回报和Sharpe Ratio，均由市场价格和交易成本计算，不依赖主观感受或语义判断；该指标提升是全文唯一核心目标和核心贡献。Benchmark方面，摘要在评价语境中明确使用'outperform the market benchmark and comparable public funds'，评价部分将DAX指数和两只公募基金作为基准并与系统两个测试组合的绝对收益和Sharpe Ratio比较，benchmark结果直接支撑核心绩效提升主张，且具有明确比较对象。因此两个模块均通过，strict_include=true。
- Confidence: 0.96

## A deep recurrent neural network approach to learn sequence similarities for user-identification

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113718
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "用户重识别正确率（P）", "measurement_cn": "从测试集（holdout 用户）中重复随机抽取锚点、正样本和负样本三元组，根据嵌入空间中 L1 距离判断锚点与正样本是否更近，计算正确决策数占总决策数的比例，见 Table 1。", "objectivity_reason_cn": "用户身份标签来自 Comscore 面板可审计的真实用户记录，正确率由模型预测与事实标签对比计算，不依赖人类感受或语义判断。"}, {"name_cn": "调整兰德指数（ARI）", "measurement_cn": "在多用户合成记录中，对 50 条序列的嵌入向量进行 k-means 聚类，再将聚类结果与真实用户标签对比计算 ARI，见 Table 2。", "objectivity_reason_cn": "ARI 是比较两个划分与随机划分的客观统计量，真实用户标签为已知事实，结果可复现计算。"}, {"name_cn": "用户数估计的召回率与精确率", "measurement_cn": "使用 Silhouette 系数选择聚类数 k，与真实用户数对比，计算召回率和精确率，见 Table 3。", "objectivity_reason_cn": "真实用户数由构造数据时的标签确定，召回率/精确率按照标准公式计算，属于客观事实标签上的分类性能。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在 Comscore 点击流用户重识别任务中，将 TL-RNN 与 Smith-Waterman 局部序列比对和 TF-RW 两种传统相似性方法进行系统比较，Table 1 报告各序列长度下的正确率（如 seq length=10 时 TL-RNN 89.31% vs TF-RW 78.88%），并进一步在多用户分配和用户数估计任务中报告 ARI 与 recall/precision。
- Decision: 核心指标为用户重识别正确率、ARI、召回率/精确率，均基于可审计的事实用户标签，不依赖主观评价；研究设计、实验评价和贡献声明均围绕提升这些客观指标展开，未发现并列主观或理论核心目标。文章摘要与第 3.2 节明确使用 benchmarking/benchmark 表述，将 TL-RNN 与 Smith-Waterman 和 TF-RW 两个明确参照点系统比较，并以这些 benchmark 结果作为核心性能提升证据。客观指标与 benchmark 两模块均通过，故 strict_include=true。
- Confidence: 0.96

## A new approach for a proxy-level web caching mechanism

- Year/journal: 2008 / Decision Support Systems
- DOI: 10.1016/j.dss.2008.05.001
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "总缓存成本（含用户延迟与缓存更新代价）", "measurement_cn": "基于IRCache代理服务器实际trace日志，模拟缓存命中/未命中与缓存更新次数，按总成本 = t × 未命中请求数 + c × 更新对象数计算；延迟通过未命中请求的下载代价反映。", "objectivity_reason_cn": "由日志中的请求时间、请求URL及缓存机制规则决定，可确定性计算，不依赖人的感受、意义理解或价值判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在IRCache网络纽约代理服务器的62天实际trace数据集上，分别评价准静态机制和集成机制的缓存总成本，并与同一trace上实现的LRU基准策略比较；Tables 7-10报告了两种机制相对LRU的总成本及百分比改进。
- Decision: 客观指标：核心成功指标是缓存总成本与用户延迟，均由代理trace日志、机制规则和成本公式确定性计算，不涉及主观感知或语义评价。唯一核心目标：论文的研究问题、设计目标和贡献声明均围绕提出并评估缓存机制、降低代理级用户延迟/成本；不存在并列的主观体验、理论机制或政策贡献。Benchmark：作者在性能分析部分明确写出“we use LRU as a benchmark”，且该基准评价处于实验评价语境，比较对象为LRU策略，结果表直接报告相对LRU的总成本改进，支撑了核心性能提升主张。因此满足纳入条件。
- Confidence: 0.96

## Failure pattern-based ensembles applied to bankruptcy forecasting

- Year/journal: 2018 / Decision Support Systems
- DOI: 10.1016/j.dss.2018.01.003
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "正确分类率（accuracy）", "measurement_cn": "在8个年份的外样本、外时间测试集上，将模型预测的破产/非破产类别与公司实际司法状态（被法院清算或重整）比较，计算正确分类率，并对bootstrap 100次的结果取平均。", "objectivity_reason_cn": "破产状态是法院裁决形成的客观事实标签，正确分类率可由预测标签与事实标签确定性地计算，不依赖人的感受、语义评价或价值判断。"}, {"name_cn": "AUC（ROC曲线下面积）", "measurement_cn": "按模型对每家公司输出的破产倾向得分与实际事实标签计算AUC，用独立于误分类成本的指标评价判别能力。", "objectivity_reason_cn": "AUC由客观事实标签与模型输出直接计算，不含主观评分或偏好。"}, {"name_cn": "Type-I/Type-II错误及其偏差-方差分解", "measurement_cn": "将错误分为第一类错误和第二类错误，并用Kohavi和Wolpert的分解方法计算bias和variance。", "objectivity_reason_cn": "错误类型和分解来自预测标签与事实标签的比较，具有确定性，不依赖主观判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 作者在8个法国企业样本上，将所提failure pattern-based模型与判别分析、逻辑回归、决策树、Cox模型、SVM、FNN、ELM等单模型，以及bagging、boosting、random subspace、rotation forest和多种混合集成模型进行系统对比；结果以正确率、AUC和显著性检验报告，FM模型平均正确率83.22%，显著高于其他模型2.27至3.01个百分点。
- Decision: 该文以破产预测这一客观事实标签为对象，核心目标是提升预测准确率、AUC等完全客观指标；全文未使用满意度、感知价值等主观构念作为成功标准，也没有并列的理论、制度或行为解释核心目标。作者在方法部分明确使用benchmark表述，将所提failure pattern-based模型与多种常用单模型和集成模型进行系统对比，并在结果部分用正确率和AUC的差异及显著性证明核心提升主张，因此同时满足客观指标和明确benchmark两个门槛，strict_include为true。
- Confidence: 0.96

## Feature assessment and ranking for classification with nonlinear sparse representation and approximate dependence analysis

- Year/journal: 2019 / Decision Support Systems
- DOI: 10.1016/j.dss.2019.05.004
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "分类错误率", "measurement_cn": "使用kNN、朴素贝叶斯和随机森林三个分类器，在每次特征选择后选出的top 20/40特征上，通过20次5折交叉验证计算平均分类错误率，并进行Wilcoxon秩和检验。", "objectivity_reason_cn": "分类错误率是分类器预测标签与数据集中既定真实标签的确定性比较结果，不依赖用户感受、语义质量或价值判断，可直接由系统日志或预测结果计算获得。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: isolet5 | DNA | mfeat-factors | mfeat-pixel | mfeat-zernike | optdigits | spambase | musk2 | 14_Tumors
- Benchmark evaluation: 在9个公开数据集上，以分类错误率作为评价指标，将提出的SRDA与MIM、mRMR、FOU、JMI和DFS五种代表性特征选择方法进行比较；使用kNN、朴素贝叶斯和随机森林三种分类器，比较top 20/40特征下的错误率，并采用20×5折交叉验证和Wilcoxon检验。结果显示SRDA在多数数据集上错误率更低。
- Decision: 本文以降低分类错误率为唯一核心目标与核心贡献，评价完全基于客观可测的分类错误率，无主观量表或人类语义质量评价作为核心成功标准。实验部分明确以公开数据集（含称为benchmark dataset的14_Tumors和mfeat数据集）作为评价场地，并与MIM、mRMR、FOU、JMI、DFS等明确参照点比较，分类错误率的下降直接支撑核心改进主张。因此两个模块均通过，strict_include为true。
- Confidence: 0.96

## Financial fraud detection using vocal, linguistic and financial cues

- Year/journal: 2015 / Decision Support Systems
- DOI: 10.1016/j.dss.2015.04.006
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "AUC（ROC曲线下面积）", "measurement_cn": "使用GLRT分类器，在10折交叉验证下对1572个公司季度电话会议样本进行欺诈/非欺诈分类，并根据分类器输出计算ROC曲线下面积；部分结果用100次10折交叉验证的AUC分布验证稳健性。", "objectivity_reason_cn": "欺诈标签来自外部可审计的会计重述数据库（Audit Analytics irregularity restatements），属于事实标签；AUC由算法输出与事实标签比对得到，不依赖人的感受、语义评价或主观价值判断。"}, {"name_cn": "给定检测率下的误报数/误报概率", "measurement_cn": "从ROC曲线选取不同操作点（如90%、50%、20%检测率），统计对应假阳性数量或概率。", "objectivity_reason_cn": "误报数由分类器输出与客观欺诈标签比对得出，是可直接审计的系统日志/分类结果统计，不涉及主观体验或语义质量评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在同一1572个电话会议样本上，将本文提出的会计风险与声学特征组合（含或不含基线指标）与AR、COGDIS、Fscore三种已有基线工具进行比较；结果显示组合特征优于最佳基线AR，最佳条件AUC达到0.81，并在90%检测率下减少15%误报。
- Decision: 客观指标方面，核心成功标准是对外部事实标签（会计重述/财务欺诈）的检测性能（AUC、检测率、误报数），不涉及主观评价或语义质量判断，且提升检测性能是全文唯一核心目标与贡献。benchmark方面，第3.1节明确以“Benchmark results”陈述基准评价，将组合特征与AR、COGDIS、Fscore等明确基线在ROC/AUC上比较，benchmark结果直接支撑核心提升主张。因此两个模块均通过，strict_include为true。
- Confidence: 0.96

## Forecasting and trading the EUR/USD exchange rate with stochastic Neural Network combination and time-varying leverage

- Year/journal: 2012 / Decision Support Systems
- DOI: 10.1016/j.dss.2012.05.039
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "年化收益率（含/不含交易成本和杠杆成本）", "measurement_cn": "基于 EUR/USD ECB fixing 价格序列和固定的多空交易规则，按 252 个交易日年化计算；交易成本和杠杆成本在表 6/7/9 中分别列出。", "objectivity_reason_cn": "由市场价格、固定交易规则和成本参数计算，可被第三方用相同数据复算，不依赖人的感受、语义判断或价值评价。"}, {"name_cn": "信息比率（含/不含成本）", "measurement_cn": "年化收益率除以年化波动率，由实际交易收益序列计算。", "objectivity_reason_cn": "基于客观收益与波动率，属于可审计的量化绩效指标。"}, {"name_cn": "统计预测误差：MAE、MAPE、RMSE、Theil-U", "measurement_cn": "比较模型预测收益率与实际收益率之间的误差，分样本内和样本外报告。", "objectivity_reason_cn": "在同一价格序列上由确定公式计算，不涉及主观质量或语义评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在 EUR/USD ECB fixing 序列（2002–2010，最后两年为样本外）上，以 Naive、ARMA、MLP、RNN 为基准评估 PSN；以 Simple Average、Bayesian Average、GRR、LASSO 等为组合基准评估 Kalman Filter。表 3/4 报告统计性能，表 6/7/9 报告交易性能，均直接支撑 PSN 和 Kalman Filter 优于各基准的核心提升主张。
- Decision: 客观指标：统计预测误差和交易绩效均由 EUR/USD 市场价格序列按固定规则计算，不依赖人类主观评价或语义判断。唯一核心目标：摘要、研究问题、设计、结果和贡献均围绕 PSN 及 Kalman Filter 在客观统计与交易指标上的提升展开，无并列的理论、政策或主观体验贡献。Benchmark：摘要和 4.1 节明确使用 benchmarking/benchmark models 表述，并在结果表 3/4/6/7/9 中与 Naive、ARMA、MLP、RNN 以及多种组合方法进行明确比较，该比较直接支撑核心改进主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.96

## Healthcare Cost Prediction for Heterogeneous Patient Profiles Using Deep Learning Models with Administrative Claims Data

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2021.0643
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "预测误差（MAPE/MAE）", "measurement_cn": "基于行政索赔数据预测次年总成本，与实际年度成本比较；MAPE=mean(|Actual-Predicted|/Actual)，MAE=mean(|Actual-Predicted|)，在测试集上计算", "objectivity_reason_cn": "预测成本和实际成本均为可审计的货币金额，误差计算完全由数据和公式确定，不依赖人的感知、语义评价或主观偏好"}, {"name_cn": "支付差额（overpayment/underpayment/net pay）", "measurement_cn": "由预测成本与实际成本的差值累计得到：实际>预测的部分为underpay，预测>实际的部分为overpay，二者之和为net pay", "objectivity_reason_cn": "支付差额是基于客观货币金额的算术结果，反映了实际支付与预测支付的偏差，是可审计的财务事实，不依赖主观判断"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在包含约111,000名Medicare患者的Utah数据集（以及外部California数据集）上评价channel-wise深度框架：与LR、RF、CART、GBDT、MLP、CNN (Morid et al. 2020)、RNN (Zeng et al. 2021)、Doctor AI、RETAIN、Dipole、Rajkomar等benchmark模型比较；结果报告MAPE等，channel-wise模型MAPE为46.8%，优于最佳基准CNN 62.3%等（Table 3、4）；并在高需求患者亚组中进行比较（Table 6）。
- Decision: 文章唯一核心目标是提升医疗成本预测的客观性能指标（MAPE/MAE/支付差额），没有主观成功标准；评价建立在真实行政索赔数据上，明确设置了Benchmark Analysis章节，与多个文献模型进行系统比较，benchmark结果直接支撑预测误差和支付差额改善的核心主张，因此完全满足严格纳入条件。
- Confidence: 0.96

## Incorporating association rule networks in feature category-weighted naive Bayes model to support weaning decision making

- Year/journal: 2017 / Decision Support Systems
- DOI: 10.1016/j.dss.2017.01.007
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "准确率", "measurement_cn": "十折交叉验证中正确分类的样本数除以总样本数，来自预测拔管结果与实际拔管结果的对比", "objectivity_reason_cn": "由确定性的分类计数计算，不依赖人的感受、语义评价或价值判断"}, {"name_cn": "精确率", "measurement_cn": "分别计算每个类别的精确率并取加权平均，基于混淆矩阵中的真正例和假正例计数", "objectivity_reason_cn": "根据预测标签与客观临床结果标签的混淆矩阵直接计算"}, {"name_cn": "召回率", "measurement_cn": "分别计算每个类别的召回率并取加权平均，基于混淆矩阵中的真正例和假负例计数", "objectivity_reason_cn": "根据预测标签与客观临床结果标签的混淆矩阵直接计算"}, {"name_cn": "F值", "measurement_cn": "精确率和召回率的调和平均值", "objectivity_reason_cn": "由两个客观的混淆矩阵派生指标计算"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在自有的1336条真实临床拔管记录上，使用十折交叉验证评价ARFCWNB，并与NB、ANN、ANNBFS、SVM、SVMLFS及临床协议对比。表6显示ARFCWNB的准确率92.60%、加权精确率93.24%、加权召回率92.59%、加权F值92.91%，优于所有基准方法；同时也在类别Y和类别N上分别报告了性能。
- Decision: 客观指标方面，核心成功指标是拔管成败这一客观事实标签上的预测准确率、精确率、召回率和F值，均由预测结果与实际临床结果标签的混淆矩阵计算，不依赖主观感知或语义评价；全部核心评价均使用这些客观指标。唯一核心目标方面，全文的研究问题、方法设计、评价结构和贡献声明都围绕提升预测性能展开，没有并列的主观体验改善、理论机制贡献或制度建议等核心目标。benchmark方面，作者在第5.2节明确将NB、ANN、ANNBFS、SVM、SVMLFS和临床协议列为benchmark，并在第6节以表6的结果作为核心证据，表明ARFCWNB在所有客观指标上优于多个基准方法，满足明确的benchmark表述、评价语境、支撑核心主张和有明确对照四个门槛。因此严格纳入。
- Confidence: 0.96

## Post-Earnings-Announcement Drift Prediction: Leveraging Postevent Investor Responses with Multitask Learning

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2022.0358
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "预测性能：解释方差（EV）", "measurement_cn": "模型在2010–2022年52个滚动窗口上预测CAR(0,21)，EV=1−Var(yhat−y)/Var(y)，数值越高表示预测越准。", "objectivity_reason_cn": "EV由模型预测值与实际股票收益之间的客观财务数据计算，不依赖人的感受、语义评价或价值判断。"}, {"name_cn": "经济收益：风险调整后日度超额收益（alpha）", "measurement_cn": "根据预测PEAD构造多头/多空组合，持有21个交易日，再对Carhart/Fama-French六因子模型回归得到截距alpha。", "objectivity_reason_cn": "alpha基于实际股价、交易成本和风险因子计算，是可审计的客观市场交易结果。"}, {"name_cn": "预测目标：累计异常收益CAR(0,21)", "measurement_cn": "以C5模型估计预期收益，从财报电话会议后21个交易日的实际收益中扣除预期收益后累加。", "objectivity_reason_cn": "CAR由股票价格和财务数据按固定公式计算，属于客观可核验的金融事实。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 作者在61,223个财报电话会议样本（2010–2022）上评估提出的FinAux+GradPerp+MQT模型，与来自金融与AI文献的SUE、OLS、PEAD.txt、LSTM、Transformer等基准模型进行预测性能（EV）比较，并在经济意义评价中比较各模型的alpha。结果显示FinAux+GradPerp+MQT在Russell 3000上取得最高EV（9.06%），显著高于所有非MTL基准模型。
- Decision: 文章核心目标是以MTL框架提升PEAD预测的完全客观指标（预测EV、风险调整后alpha），全文评价与贡献声明均围绕这一目标，无任何主观构念或并列核心目标；实验部分在2010–2022大规模数据集上明确以benchmark models为参照，系统比较SUE、OLS、PEAD.txt、LSTM、Transformer等方法，报告EV和alpha提升，符合明确的benchmark表述和比较要求。因此两个模块全部通过，strict_include=true。
- Confidence: 0.96

## Predicting Adoption Probabilities in Social Networks

- Year/journal: 2013 / Information Systems Research
- DOI: 10.1287/isre.1120.0461
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "AUC（ROC曲线下面积）", "measurement_cn": "在移动通信社交网络（主实验）和虚拟世界社交网络（附录D）上，以周为时间单位，用截至第T周的通信、用户画像和采纳数据训练/预测第T+1周未采纳用户的服务采纳概率，然后将预测概率与实际该周是否采纳进行比较，计算50次评估的AUC；对每个基准方法做Wilcoxon符号秩检验。", "objectivity_reason_cn": "是否采纳移动服务A或虚拟物品是由系统日志记录的外部可审计事实标签，不依赖人的感受、意义理解或价值判断；AUC由预测概率排序与真实采纳标签计算得出，数值客观可复核。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在移动通信社交网络（主文）与虚拟世界社交网络（附录D）上，以AUC评价LEMNB与八个基准方法：CM1、CM2、CM3、IP、NB、LWNB、SVM、k-NN；50次评估中LEMNB平均AUC为0.8029，各基准平均AUC为0.5055、0.5056、0.5056、0.5203、0.7288、0.6658、0.7069、0.6910，Wilcoxon检验均显著优于基准（p<0.001），表2给出逐周结果。
- Decision: 核心指标是真实采纳标签上的AUC，属于外部可核验事实标签上的预测性能，不依赖主观感知或语义评价；全文唯一核心目标是提升采纳概率预测效果，没有并列主观或理论核心贡献；在实验部分明确使用“benchmark methods/benchmarked/benchmark against”表述，将LEMNB与八个基准方法在AUC上比较并报告显著提升，benchmark评价直接支撑核心改善主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.96

## Pricing in Nonconvex Markets: How to Price Electricity in the Presence of Demand Response

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1139
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "make-whole payments（MWP）", "measurement_cn": "市场运营商为确保个体理性而支付的场外补贴总额，由定价模型计算得出，单位为美元；文章通过对比不同定价规则下的MWP绝对值及占总成本比例来衡量。", "objectivity_reason_cn": "MWP是财务金额，由明确数学公式和系统日志决定，不依赖人的感受、语义或价值判断，是可以审计的客观事实。"}, {"name_cn": "平均市场价格与价格波动", "measurement_cn": "在IEEE RTS-96系统各节点每小时价格的平均值和标准差，由模型计算结果统计。", "objectivity_reason_cn": "价格是交易结果，由求解模型得出，是客观可观测的市场信号。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: IEEE Reliability Test System (RTS-96)
- Benchmark evaluation: 在IEEE RTS-96系统上，针对价格无弹性、价格敏感、可转移负荷等场景，比较IP pricing、ELMP、AIC与PBE-A/PE-A四种定价规则的make-whole payments、平均价格、标准差和计算时间。结果显示PBE-A/PE-A的MWP几乎为零（0%-0.15%），而IP和ELMP的MWP常为4%-5%甚至更高，从而证明新规则的核心提升。
- Decision: 文章核心目标是提出一种最小化make-whole payments的定价规则，该指标是完全客观可测量的财务量，且全文围绕这一目标构建。在IEEE RTS-96公开基准数据集上进行系统化实验，与IP、ELMP、AIC等明确参照点比较，benchmark结果直接支撑核心提升主张。没有任何主观构念或并列核心贡献。因此同时满足客观指标、唯一核心目标和明确benchmark门槛。
- Confidence: 0.96

## Reliable Web service selection in choreographed environments

- Year/journal: 2013 / Decision Support Systems
- DOI: 10.1016/j.dss.2012.12.017
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "成功率（success rate）", "measurement_cn": "模拟执行10000次目标Web服务，统计整个choreography成功完成的比例，重复100次并取平均；每次操作调用以固定概率α成功。", "objectivity_reason_cn": "该指标衡量的是技术执行成功与否的可审计事实，不依赖用户的感受、语义评价或价值判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在购物场景及其nontransitive修订场景中，比较view-based方法与centralized、view-based propagation-free、view-based reliability-free、random四种方法的成功率；结果显示view-based接近centralized且优于其他分布式方法。
- Decision: 文章的核心目标是在choreographed环境中最大化整个流程的成功完成概率，评价指标为成功率，是客观可观测的技术结果，且为唯一核心成功标准。实验部分明确将四种既有方法称为benchmarks，并在购物场景和nontransitive场景中比较成功率，证明view-based方法优于三种分布式方法并接近centralized方法，满足benchmark评价支撑核心改进主张和显式比较对象的要求。因此同时通过客观指标和benchmark门槛。
- Confidence: 0.96

## SpamHunting: An instance-based reasoning system for spam labelling and filtering

- Year/journal: 2007 / Decision Support Systems
- DOI: 10.1016/j.dss.2006.11.012
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "正确分类率（%OK）", "measurement_cn": "10折交叉验证中预测类别与真实标签一致的邮件占比，由系统日志和真实标签对比计算。", "objectivity_reason_cn": "垃圾邮件/合法邮件的真实标签是外部事实，分类结果可审计，不依赖人的感受或语义评价。"}, {"name_cn": "假阳性率（%FP）与假阴性率（%FN）", "measurement_cn": "在SpamAssassin语料库上，将合法邮件误判为垃圾邮件的比例与将垃圾邮件误判为合法的比例，由预测与真实标签统计得出。", "objectivity_reason_cn": "两类错误是客观的分类结果计数，且与成本相关，不涉及主观偏好。"}, {"name_cn": "垃圾邮件召回率与精确率", "measurement_cn": "基于混淆矩阵计算召回率（过滤器有效性）和精确率（过滤器安全性）。", "objectivity_reason_cn": "混淆矩阵可由系统预测与真实标签确定，计算公式明确，完全客观。"}, {"name_cn": "总成本比（TCR）", "measurement_cn": "在不同成本场景（λ=1, 9, 999）下，根据FP/FN的加权成本计算的性能指标。", "objectivity_reason_cn": "TCR基于客观错误计数和预定义成本权重，可复现，不依赖主观评价。"}, {"name_cn": "训练与运行时间", "measurement_cn": "在2.8GHz Pentium IV处理器上执行10折交叉验证的耗时（分钟），用于比较计算复杂度。", "objectivity_reason_cn": "时间为可测量的物理量，完全客观。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: SpamAssassin corpus
- Benchmark evaluation: 在SpamAssassin 2002/2003公开语料库上，采用10折分层交叉验证，将SpamHunting与Naïve Bayes、Adaboost、SVM、ECUE和Cunn Odds Rate五种已有方法比较，报告%OK、%FP、%FN、召回率、精确率、TCR和训练时间。结果显示SpamHunting在FP/FN比率、精确率及高成本场景下TCR等方面优于其他模型。
- Decision: 客观指标方面：所有核心成功指标均为垃圾邮件分类性能（%OK、FP/FN、召回率、精确率、TCR）和计算时间，这些指标基于外部事实标签（spam/legitimate）和可测量的物理时间，完全客观，不依赖人类感受或语义评价；系统设计和贡献声明均围绕提升这些客观指标展开，没有并列的主观或理论核心目标。Benchmark方面：文章明确命名SpamAssassin公开语料库作为评价场地，在评价语境中进行系统化比较，结果表/图与多个baseline方法对比，支撑了核心性能提升主张。因此两个模块均通过，strict_include为true。
- Confidence: 0.96

## Toward Sustainable Electricity Markets: Capacity-Based Pricing for Electric Vehicle Smart Charging

- Year/journal: 2026 / Information Systems Research
- DOI: 10.1287/isre.2023.0078
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "RMSE（实际充电负荷与目标需求曲线之间的均方根误差）", "measurement_cn": "在仿真中比较聚合EV充电负荷与实际/目标需求曲线，公式为 RMSE = sqrt(sum_t (D_t^o - D_t)^2)，单位MWh；数值越低表示负荷塑造越精确。", "objectivity_reason_cn": "该指标由系统模拟产生的聚合负荷和预设目标曲线直接计算，不依赖人的感受、偏好或语义评价，是可审计的工程/物理量。"}, {"name_cn": "绝对负荷峰值（Peak）与峰均功率比（PAPR）", "measurement_cn": "从聚合需求曲线计算：Peak = max_t D_t^o；PAPR = (Peak^2)/(RMS^2)，用于衡量需求波动/峰值强度。", "objectivity_reason_cn": "峰值和PAPR均由模拟系统的客观负荷输出直接计算，反映电网容量与波动性，不涉及主观判断。"}, {"name_cn": "目标收入偏差（Revenue deviation / % Diff from target Ψ*）", "measurement_cn": "对比实际收取电费与目标总收入Ψ*的差异百分比，数值越低表示在重塑负荷的同时越能维持收入目标。", "objectivity_reason_cn": "收入由价格与电量等可审计交易数据计算，是客观的财务/交易指标。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在基于Power TAC规范构建的多智能体仿真测试平台上，将CBP-AH、CBP-AH-Distrib、CBP-CH、CBP-CH-Distrib四种配置与真实世界平坦定价、速率无关可变定价、递增分块定价等基准比较；三种场景目标分别是平坦充电曲线、弥补家庭负荷形成平坦总需求、匹配光伏发电曲线；使用RMSE、PAPR、峰值和收入偏差评价。结果显示CBP-CH接近最优（例如平坦场景RMSE=0.02、PAPR=1.07、Peak=1.03），均优于所有基准。
- Decision: 本文核心目标是设计并验证一种容量定价IS构件，以客观、可测量的电网平衡指标（RMSE、峰值、PAPR）和收入偏差来评价其对EV充电负荷曲线的塑造能力。所有核心成功指标均为模拟/交易可审计的物理或财务量，不涉及主观感知或语义判断；该客观指标提升是全文唯一核心目标与贡献。全文存在明确的benchmark表述，且评价在实验/结果部分进行，基准对比（平坦定价、可变定价、递增分块定价）正是支撑核心改进主张的关键证据。因此满足全部审计条件。
- Confidence: 0.96

## A Cost-based Database Request Distribution Technique for Online e-Commerce Applications

- Year/journal: 2012 / MIS Quarterly
- DOI: 10.2307/41703464
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "应用响应时间", "measurement_cn": "在TPC-W工作负载下使用模拟用户，通过实验平台测量端到端平均响应时间（毫秒）；也被作者用作容量利用率的代理。", "objectivity_reason_cn": "响应时间是对系统处理时间的物理测量，可由负载测试工具和系统日志客观记录，不依赖用户感受、语义评价或价值判断。"}, {"name_cn": "应用吞吐量", "measurement_cn": "每秒处理的请求数，由负载测试工具（如Radview WebLoad和LoadRunner）记录；现场实验中记录事务/秒。", "objectivity_reason_cn": "吞吐量是基于系统实际处理请求数量的可审计计数，独立于任何主观人类体验或质量判断。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: TPC-W
- Benchmark evaluation: 在TPC-W模拟的电子商务（书店）环境上，将C-DBRD与RR、LCPU、FMEM三种现有请求分布策略进行对比，随模拟用户数增加测量平均响应时间和吞吐量；结果显示C-DBRD在高负载下响应时间比最佳对比方法FMEM降低约45%，吞吐量高出近50%。另有生产级现场实验比较C-DBRD与SQL Server 2005 clustering及RR。
- Decision: 客观指标方面，文章完全依赖响应时间和吞吐量这类物理可测、可由工具和系统日志客观记录的结果指标，没有使用满意度、感知价值或语义评分等主观构念作为成功标准；唯一核心目标是通过请求分布技术提升数据库层资源利用率，理论模型和实现方法都服务于这一客观改进。Benchmark方面，全文在实验部分明确使用公开标准benchmark TPC-W作为评价场地，并在同一评价语境中与RR、LCPU、FMEM等明确参照点比较，benchmark结果直接支撑45%响应时间改进等核心贡献主张。因此同时满足客观指标门槛和benchmark门槛，strict_include应为true。
- Confidence: 0.95

## A Data Analytics Framework for Smart Asthma Management Based on Remote Health Information Systems with Bluetooth-Enabled Personal Inhalers

- Year/journal: 2020 / MIS Quarterly
- DOI: 10.25300/misq/2020/15092
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "AUC（受试者工作特征曲线下面积）", "measurement_cn": "通过性能评估算法：将患者i的第k+1周数据替换为另一随机患者j的数据作为异常（TP）场景，使用原始第k+1周数据作为正常（TN）场景；根据检测方法的报警结果计算ROC曲线，以AUC作为主要性能指标。", "objectivity_reason_cn": "AUC由真实的吸入器使用事件和明确的替换/非替换标签计算，不依赖人的感受、语义或质量判断；标签由客观事实（是否来自同一患者）决定。"}, {"name_cn": "误报率与漏检率", "measurement_cn": "在性能评估中统计检测方法产生的假阳性（误报）和假阴性（漏检）比例，展示于Figure 9(a)。", "objectivity_reason_cn": "由检测算法输出与客观事实标签比较得到，可审计。"}, {"name_cn": "平均报警时间（time-to-alert）", "measurement_cn": "统计检测方法在异常事件发生到产生报警之间的时间间隔，展示于Figure 9(b)。", "objectivity_reason_cn": "基于系统时间戳计算，完全客观。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在SAM真实数据集上，将提出的GLMM-GQP与六个基准方法（GLMM-P、GLMM-NB、GLMM-GQPS、混合效应逻辑回归、SVM、CG-HMM）进行系统比较；以AUC为主要指标，并在不同训练数据量（k=1,4,8,12,m−1）下进行100次重复评估；结果显示GLMM-GQP在多数设置下AUC最高（Table 4），并通过误报率、漏检率和时间到报警进一步解释。
- Decision: 核心目标是开发并验证一个以客观检测性能（AUC等）为唯一成功标准的异常吸入器使用检测框架；所有评价指标均为可审计的客观指标，无主观量表或人类语义判断。全文存在明确的benchmark表述（摘要和性能评估部分的benchmark methods），在评价语境中系统比较了六个带明确参照点的基准方法，并将benchmark比较结果作为核心改进主张的关键证据。因此同时满足客观指标唯一核心目标和明确benchmark两个条件，strict_include=true。
- Confidence: 0.95

## A Switch in Time Saves the Dime: A Model to Reduce Rental Cost in Cloud Computing

- Year/journal: 2020 / Information Systems Research
- DOI: 10.1287/isre.2019.0912
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "总租赁成本（含切换成本）", "measurement_cn": "由所选云计算资源的每小时租金、使用小时数以及切换成本计算得出，公式为 min sum c_i x_it + S * switches，符合云服务商公布的定价与使用时长。", "objectivity_reason_cn": "租金与时段选择均为可审计的交易事实，成本值由云服务商定价和使用时长确定，不依赖任何人的感受、偏好或语义判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 自定义基准：最佳单计算资源方案（best single-resource solution / cheapest feasible single computing resource）
- Benchmark evaluation: 在计算实验（Section 6）和 Cidewalk 真实案例（Section 7）中，作者将提出的 EnhancedRounding / EnhancedRounding^OC 方案与最佳单计算资源基准方案进行系统比较，报告总租赁成本的相对节省（如小规模实例平均节省 24.71%，大规模实例平均节省 24.44%，OC 场景约 14%–15%，Cidewalk 案例节省 27.91%）。
- Decision: 客观指标：核心目标是总租赁成本最小化，该指标由云服务商定价和使用时长等可审计事实决定，完全客观。唯一核心目标：研究问题、模型目标、算法设计和评价指标均围绕总租赁成本展开，理论贡献和性能保证只是支持该核心目标的技术手段，不存在并列的主观或理论核心目标。Benchmark：作者明确使用“best single-resource solution as a benchmark”，并在计算实验和真实案例中进行系统比较，Benchmark 结果直接支撑“成本降低 15%–25%”的核心主张，且具有明确参照点。因此 strict_include=true。
- Confidence: 0.95

## A Time-Based Dynamic Synchronization Policy for Consolidated Database Systems1

- Year/journal: 2019 / MIS Quarterly
- DOI: 10.25300/misq/2019/14804
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "总系统成本", "measurement_cn": "由同步成本（固定同步成本CU）和数据陈旧成本（单位陈旧成本×错误数量×查询到达率等）构成，通过动态规划/仿真模拟计算；比较TDS策略与周期性策略等基准策略的总成本及成本节约百分比。", "objectivity_reason_cn": "成本和成本节约是货币化、可审计的量化指标，完全由模型参数和到达过程决定，不依赖人类感受、语义评价或主观偏好。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: Periodic policy (Dey et al. 2006) | Query-based policy (Dey et al. 2006) | Update-based policy (Dey et al. 2006) | Query-based dynamic policy (Fang et al. 2013) | Hybrid policy (Dey et al. 2015)
- Benchmark evaluation: 在Policy Comparisons中，TDS策略与周期性策略等在1至5年时间窗上模拟比较；Table 1/Figure 7显示TDS总成本低于周期性策略，成本节约约10%；Appendix D显示TDS相对于混合策略的成本节约为3.84%至10.22%。
- Decision: 文章的核心客观指标是总系统成本/成本节约，唯一核心目标是最小化CDB同步与数据陈旧总成本；数值实验将TDS策略与周期性策略、混合策略等基准策略比较，并以成本节约百分比作为核心改进证据，满足完全客观指标、唯一核心目标和明确benchmark比较的门槛。
- Confidence: 0.95

## A case-based approach using inductive indexing for corporate bond rating

- Year/journal: 2001 / Decision Support Systems
- DOI: 10.1016/s0167-9236(01)00099-9
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "分类准确率（weighted average classification accuracy）", "measurement_cn": "在400个验证集样本上，模型预测的债券评级与评级机构（National Information and Credit Evaluation）给出的真实评级一致的比例，并按各评级样本数加权平均；对IND-NN（2）等模型与基准模型的差异使用McNemar检验。", "objectivity_reason_cn": "债券评级是由独立评级机构发布的外部可核验事实标签；预测是否与标签一致是可审计的计数，不依赖人的感受、语义评价或偏好。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在韩国公司债券评级数据集（参考集3486，验证集400）上评价所提出的IND-NN模型（决策树深度3/5/7/9 + 叶内最近邻），并将MDA、KATE-Induction、最近邻（NN）、专家权重最近邻（NN_Expert）作为基准比较。Table 5显示IND-NN(2)达到70.0%的加权准确率，高于所有基准；Table 7的McNemar检验显示IND-NN(2)在1%水平显著优于每一个基准模型。
- Decision: 客观指标：核心结果指标为债券评级预测的分类准确率；评级是由独立评级机构给出的外部可核验事实标签，准确率计算基于确定性计数，不涉及人类感受、语义评价或偏好。唯一核心目标：研究设计、评价和贡献声明均围绕通过归纳索引提升案例检索后的分类准确率；结论中的知识组合原则是对提升机制的解释，非并列核心贡献。Benchmark：结果部分明确将MDA、KATE-Induction、NN、NN_Expert作为benchmarks进行对比，并以Table 5和Table 7的对比证据证明IND-NN(2)在准确率上显著提升。三部分全部通过，因此strict_include=true。
- Confidence: 0.95

## A cost-sensitive technique for positive-example learning supporting content-based product recommendations in B-to-C e-commerce

- Year/journal: 2012 / Decision Support Systems
- DOI: 10.1016/j.dss.2012.01.018
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "预测精度（accuracy）", "measurement_cn": "在Amazon.com图书评分数据集上，将评分≥4视为正例、其余为负例，比较各模型在独立测试集上的分类准确率，采用10次重复试验的加权平均", "objectivity_reason_cn": "目标是预测'产品是否对顾客有吸引力'这一操作性类别，标签由Amazon评分阈值确定，构念和结果值不依赖用户主观体验或语义质量判断"}, {"name_cn": "正例与负例 F1 分数及平均 F1", "measurement_cn": "根据预测类别与实际类别计算 precision、recall，再计算 F1；分别报告正类和负类F1及两者平均", "objectivity_reason_cn": "基于可审计的分类正误计数，计算公式客观，且评价对象是固定的兴趣/非兴趣类别判定"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在Amazon.com的36位顶级评论者的图书评分数据（SIPs/CAPs内容特征）上评价COLPEL，同时实现PNB和PEBL作为performance benchmarks；比较weighted accuracy、positive/negative F1、average F1，并报告显著性检验、参数敏感性和组件分析。
- Decision: 客观指标：全文以分类预测的accuracy、F1为核心成功指标，标签来自Amazon评分阈值（>=4为积极），属于对固定事实标签的检测性能，不依赖人的主观评价质量；评价过程基于测试集类别计数，客观可审计。唯一核心目标：研究问题、方法设计、评价和贡献均围绕提升自动分类器预测有效性展开，没有与客观指标提升并列的主观体验、理论机制或组织变革等核心贡献。Benchmark：作者在摘要、引言和实验部分明确将PNB和PEBL称为'performance benchmarks'，并在Amazon数据上对三者进行比较；比较有明确参照对象（两个既有方法），结果表给出accuracy、F1和统计显著性，且benchmark比较直接支撑COLPEL的核心改进主张，属于benchmark_comparison_central。因此strict_include=true。
- Confidence: 0.95

## A decision support framework for home health care transportation with simultaneous multi-vehicle routing and staff scheduling synchronization

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113361
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "总成本（旅行成本+路线分配成本）", "measurement_cn": "由MILP目标函数(1)定义，包含距离相关旅行成本C、车辆固定成本F和护士固定成本B，在随机生成实例和香港现实实例中计算。", "objectivity_reason_cn": "成本由距离、固定费用和决策变量确定计算，不依赖人的感受、意义或价值判断，可直接审计。"}, {"name_cn": "计算时间（秒）", "measurement_cn": "CPLEX和HGA求解各实例的CPU时间，在固定硬件环境下记录。", "objectivity_reason_cn": "时间为客观可观测物理量，可通过日志或计时器验证。"}, {"name_cn": "最优性差距（%）", "measurement_cn": "HGA总成本与CPLEX最优解/最好界之间的相对差距，按文中公式计算。", "objectivity_reason_cn": "差距由数值计算得出，属于客观可复核的算法性能指标。"}, {"name_cn": "总行驶距离", "measurement_cn": "MILP和HGA方案中各路线距离合计，如Table 7和图6所示。", "objectivity_reason_cn": "距离是确定性的几何/路网事实，不依赖主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 作者在实验部分以CPLEX求解MILP得到的最优解或最好界作为基准，评估HGA在随机生成实例（A-D）和香港现实实例（A-G）上的总成本、计算时间和最优性差距；还在Table 8中将HGA与VNS、GAF、GA对比。核心结果表明HGA在大规模实例上能在远短于CPLEX的时间内取得较小最优性差距，支持算法有效性和高效性的核心主张。
- Decision: 文章核心是以最小化总成本为目标的HHC运输与排班优化决策支持模型和算法；所有核心成功指标均为客观可审计的成本、时间、距离和最优性差距，无主观或语义评价。核心目标唯一为客观绩效提升，模型/算法创新是手段而非并列结果。实验部分明确以CPLEX最优解作为benchmark，并在评价语境中比较HGA与CPLEX、VNS、GAF和GA，比较点明确，benchmark结果直接支撑算法高效性和解质量的核心主张。因此objective_metric与benchmark模块全部通过，strict_include为true。
- Confidence: 0.95

## A decision support system for in-sample simultaneous equation systems forecasting using artificial neural systems

- Year/journal: 1994 / Decision Support Systems
- DOI: 10.1016/0167-9236(94)90020-5
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "SSE（平方误差和）", "measurement_cn": "在Klein's Model 1实验中，对每个内生变量（C、I、w1）计算预测值与实际值的平方误差之和；在蒙特卡洛实验中，对每次复制计算SSE，并用于统计NN支配传统估计器的次数。", "objectivity_reason_cn": "预测误差基于确定的数值计算，不依赖任何人类感受、语义判断或偏好，完全可复核。"}, {"name_cn": "RMFE（均方根预测误差）", "measurement_cn": "在蒙特卡洛实验中，对500次复制计算Y1和Y2的第一个观测值的预测误差平方和的均方根。", "objectivity_reason_cn": "由实际观测值与预测值直接计算，客观可复制。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: Klein's Model 1
- Benchmark evaluation: 在Klein's Model 1上，MLFFNN与2SLS、3SLS、ULS比较预测C、I、w1的SSE，结果显示MLFFNN的总SSE为32.49872，显著低于2SLS的60.97706、3SLS的73.60156和ULS的45.2069。该benchmark结果直接支撑了MLFFNN预测精度提升的核心主张。
- Decision: 客观指标方面，论文的核心成功指标是SSE和RMFE，均为可计算的预测误差，完全客观；核心目标是通过MLFFNN提升SES样本内预测精度，全文研究、实验和贡献均围绕此展开，未发现并列的其他核心目标。Benchmark方面，论文明确使用了公开领域标准模型Klein's Model 1作为评价场地，并与2SLS、3SLS、ULS进行了明确的比较，benchmark结果直接支撑了MLFFNN预测精度提升的核心主张。因此，两个条件均满足，strict_include为true。
- Confidence: 0.95

## A hybrid approach for efficient ensembles

- Year/journal: 2010 / Decision Support Systems
- DOI: 10.1016/j.dss.2009.06.007
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "分类均方误差（MSE）", "measurement_cn": "在13个UCI数据集上使用分层10折交叉验证，由集成方法对测试实例进行预测后计算预测与真实类标签的均方误差；主要结果见Table 9和Table 11。", "objectivity_reason_cn": "MSE完全由分类器的预测输出和数据集中的既有事实类标签计算得到，不依赖人的感受、语义评价或偏好，数值确定且可复核。"}, {"name_cn": "分类准确率（Accuracy）", "measurement_cn": "在示例和部分分析中，由混淆矩阵中正确分类数除以总实例数得到，如公式(1)。", "objectivity_reason_cn": "准确率由分类器输出与数据集中已知类标签直接比较得到，是客观可审计的技术指标。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: UCI Machine Learning Repository（13个数据集：breast-w, colic, credit-a, credit-g, diabetes, heart-c, heart-h, iris, labor, lymph, sick, sonar, vote）
- Benchmark evaluation: 在13个UCI数据集上，用分层10折交叉验证评价DEA+Stacking（DST）方法，并与UWA、VBW、EMO、ESW四个已知基准组合方法以及AdaBoost、Bagging、Random Forest对比；报告MSE和配对t检验，平均MSE从ESW的0.163降至0.074，且显著优于全部基准方法。
- Decision: 客观指标方面，核心成功指标是分类MSE/准确率，由分类器输出与UCI数据集中的既有类标签计算，完全客观且可复核。唯一核心目标方面，研究问题、设计目标、实验评价和贡献声明均围绕提升集成分类性能展开，没有主观结果或并列的核心贡献。Benchmark方面，作者在13个UCI标准数据集上明确使用benchmark字样进行了系统比较，与UWA、VBW、EMO、ESW以及AdaBoost、Bagging、Random Forest等明确参照点对比，且benchmark结果（MSE下降和显著性检验）是支撑核心提升主张的关键证据。因此两个模块均通过，strict_include=true。
- Confidence: 0.95

## A hybrid sales forecasting system based on clustering and decision trees

- Year/journal: 2006 / Decision Support Systems
- DOI: 10.1016/j.dss.2005.01.008
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "均方根误差 (RMSE)", "measurement_cn": "基于真实销售曲线与预测原型的绝对误差计算，使用标准 RMSE 公式", "objectivity_reason_cn": "预测误差由实际销售数据与算法输出直接计算，不依赖人的感受或语义判断"}, {"name_cn": "平均绝对百分比误差 (MAPE)", "measurement_cn": "计算真实销售与预测之间的绝对百分比误差并取平均", "objectivity_reason_cn": "基于数值事实的确定性计算公式，结果可审计"}, {"name_cn": "中位数绝对百分比误差 (MdAPE)", "measurement_cn": "取绝对百分比误差的中位数，降低异常点影响", "objectivity_reason_cn": "基于数值事实的确定性公式，不依赖主观评价"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在285个真实测试商品上评价提出的C4.5预测系统，将其与均值剖面预测器（mean profile）、ZeroR、OneR、朴素贝叶斯、IBk等六个模型进行对比，使用RMSE、MAPE、MdAPE三项误差指标评估。结果显示提出的系统在所有指标上表现最佳。
- Decision: 文章核心目标是提高中期销售预测准确性，评价指标为预测误差（RMSE、MAPE、MdAPE），完全客观且为唯一核心贡献。第5.3节明确使用均值剖面作为benchmark，并与其他4个分类器构成基准对比，表3显示提出的系统在所有误差指标上优于所有基准。benchmark评价直接支撑了核心改进主张，因此两个模块均通过，strict_include为true。
- Confidence: 0.95

## A new approach to classification based on association rule mining

- Year/journal: 2006 / Decision Support Systems
- DOI: 10.1016/j.dss.2005.03.005
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "分类准确率", "measurement_cn": "在测试数据集上预测正确的样本数占总样本数的百分比", "objectivity_reason_cn": "分类标签为外部事实，预测正确与否可客观核对，不依赖人的感受或语义评价"}, {"name_cn": "生成的规则数量", "measurement_cn": "分类器产生的分类规则条数的直接计数", "objectivity_reason_cn": "规则数量是客观计数结果，可审计"}, {"name_cn": "执行时间", "measurement_cn": "算法运行所花费的物理时间（秒）", "objectivity_reason_cn": "物理时间客观可测，不受主观评价影响"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: UCI Machine Learning Repository
- Benchmark evaluation: 在30个UCI数据集上评估GARC的分类准确率，并与C4.5、CBA、SVM、NN等分类器进行对照；同时比较规则数量和执行时间。结果显示GARC准确率与多个基准分类器无显著差异，规则数量平均仅为CBA的4.3%。
- Decision: 论文核心目标为提出GARC算法，以在保持分类准确率的同时大幅减少规则数量，核心指标（准确率、规则数量、执行时间）均为客观可测量指标，且没有其他并列的核心贡献；全文在实验部分明确使用UCI Machine Learning Repository作为公开benchmark数据集，并在该benchmark上与C4.5、CBA、SVM、NN等明确参照对比，benchmark结果直接支撑了GARC客观性能改进的核心主张。因此两个模块均通过，严格纳入。
- Confidence: 0.95

## A novel federated learning approach with knowledge transfer for credit scoring

- Year/journal: 2024 / Decision Support Systems
- DOI: 10.1016/j.dss.2023.114084
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "Accuracy（准确率）", "measurement_cn": "正确分类的样本数占总体样本数的比例，由预测标签与真实标签对比计算。", "objectivity_reason_cn": "基于客观的违约/非违约标签，不依赖主观评价，数值由分类结果确定。"}, {"name_cn": "Recall（召回率）", "measurement_cn": "正确识别的正类（违约）样本数占所有真实正类样本数的比例。", "objectivity_reason_cn": "基于事实违约标签和预测标签计算，完全客观。"}, {"name_cn": "F1-score", "measurement_cn": "精确率与召回率的调和平均数。", "objectivity_reason_cn": "由客观的精确率和召回率计算，无主观成分。"}, {"name_cn": "KS（Kolmogorov-Smirnov统计量）", "measurement_cn": "累积事件分布与累积非事件分布的最大差异。", "objectivity_reason_cn": "基于预测分数和真实违约标签计算，客观可复现。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在五个信用数据集上，将FedKT与benchmark联邦方法FedAvg、FedProx、FedCodl进行比较，在IID和Non-IID两种设置下报告Accuracy、Recall、F1-score和KS的平均性能（表5、表6，图3、图4），并通过Friedman检验验证显著性。
- Decision: 本文核心目标为通过联邦知识转移提升信用评分模型的客观分类性能（Accuracy、Recall、F1、KS），所有实验和贡献均围绕该目标展开，无主观指标并列，核心贡献唯一且客观。全文存在明确的benchmark表述：将FedAvg、FedProx、FedCodl作为benchmark联邦方法，在五个真实信用数据集上进行系统比较，比较结果直接支撑核心性能提升主张，且具有明确参照点。因此两个模块均通过。
- Confidence: 0.95

## A practical approach for efficiently answering top-k relational queries

- Year/journal: 2007 / Decision Support Systems
- DOI: 10.1016/j.dss.2007.04.005
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "总代价（Total Cost）", "measurement_cn": "根据重启代价与过量结果排序代价之和计算，见公式（8）；实验中以数据库基数T作为最坏情况下的重启代价代理，并按实际返回结果数计算过量排序代价。", "objectivity_reason_cn": "代价由明确公式、查询返回记录数和数据库统计量计算，属于可审计的技术性成本，不依赖人的感知、偏好或语义判断。"}, {"name_cn": "过量结果数（Excess）", "measurement_cn": "统计查询返回结果数相对于请求的k值的多余记录数；发生重启时按保证无重启范围返回的记录数计算。", "objectivity_reason_cn": "记录数是可观察、可核查的执行结果事实，计算过程不含主观评价。"}, {"name_cn": "重启查询百分比（Percentage of Restarts）", "measurement_cn": "在一组实验查询中，首次执行未能取回k条结果而需要重新执行的查询所占比例。", "objectivity_reason_cn": "该指标由查询是否成功取得至少k条可审计结果直接计数得到，完全客观。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: DWBS（Dynamic Workload Based Strategy，作为对照基准技术，非公开数据集）
- Benchmark evaluation: 在约210K记录的Census收入和500K记录的合成Zipf数组数据上，使用equi-count、equi-width、MaxDiff三类直方图和多种bin数、多种k值，系统比较QLOCS与DWBS在Excess、Percentage of Restarts和Total Cost上的表现。结果显示QLOCS显著更低且更稳定，证明其“直方图无关”的高效性和稳健性。
- Decision: 该文属于数据库查询处理技术研究。其核心目标是通过QLOCS成本模型优化top-k到范围查询的转换，提升Total Cost、Excess和Restarts等完全客观的效率指标，并无主观评价或并列性非客观贡献。全文存在明确的benchmark表述，将DWBS作为基准技术，并在实验部分系统比较QLOCS与DWBS，基准对比结果直接支持QLOCS更高效、更稳健的核心主张。因此，客观指标门槛、唯一核心目标门槛和benchmark门槛均通过。
- Confidence: 0.95

## A randomized pricing decision support system in electronic commerce

- Year/journal: 2014 / Decision Support Systems
- DOI: 10.1016/j.dss.2013.01.015
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "零售商期望利润", "measurement_cn": "由理论模型推导的平均每期期望利润，通过比较随机定价策略与固定价格策略的利润公式计算得出", "objectivity_reason_cn": "利润是可审计的客观经济指标，不依赖人类感知、语义评价或主观体验；虽然文中使用数学模型计算期望利润，但其数值逻辑和比较标准是完全客观的"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 文章以固定价格策略（flat price strategy）作为基准，在其下计算最优利润Π0=1/4；然后在随机定价策略下推导最优利润Π1，并通过命题1证明Π1 ≥ Π0，即随机定价策略总能提高利润。该基准比较直接支撑核心改进主张。
- Decision: 客观指标方面，文章核心目标是提升零售商利润，利润是客观可审计的经济指标，不存在任何主观构念或并列的核心贡献。benchmark方面，文章在模型部分明确将固定价格策略称为benchmark，并以其作为参照点，通过数学证明和数值分析展示随机定价策略在利润指标上的提升，该benchmark评价是核心改进主张的关键证据。因此，两个模块均通过，strict_include为true。
- Confidence: 0.95

## A recommendation system for predicting risks across multiple business process instances

- Year/journal: 2015 / Decision Support Systems
- DOI: 10.1016/j.dss.2014.10.006
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "故障实例百分比（% faulty instances）", "measurement_cn": "在模拟或原始事件日志中，根据预定义的故障函数（超时、成本、声誉）计算每条trace是否故障，统计故障trace占比", "objectivity_reason_cn": "故障由定时器、事件出现与否、工作项数量等可审计事实决定，可从事件日志确定性地计算，不依赖人的主观评价"}, {"name_cn": "平均和中位故障严重性（mean and median fault severity）", "measurement_cn": "每条trace根据故障函数得到一个0-1的严重性值，统计所有trace的平均值和中位数", "objectivity_reason_cn": "严重性由公式（如超时程度、成本超支程度）直接计算，数值完全客观"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 保险公司一年完成的索赔处理流程事件日志（1065条trace，未公开命名）
- Benchmark evaluation: 在保险公司提供的一年事件日志（benchmark）上，作者构建了CPN Tools模拟模型，并运行推荐系统，将推荐系统产生的模拟日志（100%、66%、33%建议遵循率，多种α值）与原始日志和未加推荐的模拟日志进行比较，报告故障实例百分比、平均/中位故障严重性，并进行卡方检验、Kruskal-Wallis检验等。
- Decision: 该文章以降低业务流程执行中的故障数量和严重性作为唯一核心目标，所有评价均基于从事件日志中计算出的客观故障指标（时间、事件出现、数量），无任何主观评价指标。Evaluation部分明确将公司一年事件日志称为benchmark，并以此作为比较基线，展示推荐系统带来的显著改进（统计检验支持）。因此同时满足客观指标提升和明确benchmark两个条件，严格纳入。
- Confidence: 0.95

## A social investing approach for portfolio recommendation

- Year/journal: 2021 / Information & Management
- DOI: 10.1016/j.im.2021.103536
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "投资组合收益率（Portfolio Return）", "measurement_cn": "基于 eToro 数据构建投资组合后，在 30 个交易日内模拟交易，计算组合价值变化百分比，并与 S&P 500 市场指数对比。", "objectivity_reason_cn": "收益率由市场交易价格和组合权重决定，不依赖人的感受或语义评价，可审计复算。"}, {"name_cn": "Treynor 比率", "measurement_cn": "（组合收益率 - 无风险利率）/ 组合 Beta，反映每单位系统性风险获得的超额回报。", "objectivity_reason_cn": "由收益率、无风险利率和 Beta 计算得出，Beta 基于历史市场数据协方差估计，全部为客观财务数据。"}, {"name_cn": "Jensen 阿尔法（Jensen's alpha）", "measurement_cn": "组合实际收益率减去基于 CAPM 的预期收益率（无风险利率 + Beta ×（市场收益率 - 无风险利率）），衡量异常收益。", "objectivity_reason_cn": "由组合收益率、市场收益率、无风险利率和 Beta 计算，均为客观市场数据，不涉及主观判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在 eToro 平台收集的股票帖子数据上，构建投资组合后，将提出的 CIR 机制与 no-filter、knowledge-based、authority-based 三种推荐方法以及 S&P 500 市场指数进行 30 日模拟交易比较，评估收益、Treynor 比率和 Jensen 阿尔法。结果显示 CIR 在多数风险偏好组合下均优于这些基准。
- Decision: 文章核心目标是提出基于社会投资平台集体智慧的投资组合推荐机制，并验证其能够提升投资组合的客观财务绩效（收益、Treynor 比率、Jensen 阿尔法）。所有核心评价指标均来自市场数据和投资组合模拟交易，不依赖人类主观感受或语义价值判断。全文在评价部分明确使用 benchmark approaches 一词，并与 no-filter、knowledge-based、authority-based 及 S&P 500 等明确参照对象比较，基准评价直接支撑核心绩效提升主张。因此同时满足客观指标唯一核心目标和明确 benchmark 表述两项条件。
- Confidence: 0.95

## A web recommendation system considering sequential information

- Year/journal: 2015 / Decision Support Systems
- DOI: 10.1016/j.dss.2015.04.004
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "预测准确率（Accuracy）", "measurement_cn": "对测试用户会话，系统预测下一个页面类别，与实际日志中的下一个页面类别比对；一致记为hit，否则为miss；准确率=命中数/总预测数。", "objectivity_reason_cn": "实际下一页面类别来自web日志，是可外部核验的事实；是否命中由确定性比较决定，不依赖人的感受、意义或价值判断。"}, {"name_cn": "精确率（Precision）", "measurement_cn": "在Top-1、Top-2、Top-3预测中，检索到的推荐项中实际相关（命中）的比例；相关与否以真实日志中的实际下一次页面为基准。", "objectivity_reason_cn": "相关项界定为真实发生的页面访问，是外部可审计事实；精确率由确定性公式计算，无主观语义评价。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: MSNBC benchmark dataset（UCI web navigation dataset）
- Benchmark evaluation: 在MSNBC benchmark数据集（另加模拟数据集和CTI数据集）上评价所提出的基于S3M相似性、软聚类和SVD的推荐系统，报告Top-1、Top-2、Top-3下一页面预测的准确率和精确率；结果与随机预测模型和first-order Markov模型比较。Tables 5-8和Figures 2-4显示提出模型在准确率和精确率上均优于两个显式基线。
- Decision: 客观指标：核心成功指标是下一页面预测的准确率和精确率，均通过web日志中的实际页面访问事实进行确定性计算，不依赖人类主观评价；且全文没有把满意度、感知质量等主观构念作为成功标准。唯一核心目标：研究问题、系统设计和贡献声明都围绕提升下一页面预测的客观性能，未发现并列的主观、理论或制度性核心贡献。Benchmark：全文明确将MSNBC称为公开benchmark dataset，并在实验部分作为核心评价场地，与随机预测模型和first-order Markov模型等显式基线比较，benchmark结果直接支撑了核心提升主张。因此strict_include=true。
- Confidence: 0.95

## APATE: A novel approach for automated credit card transaction fraud detection using network-based extensions

- Year/journal: 2015 / Decision Support Systems
- DOI: 10.1016/j.dss.2015.04.013
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "AUC（ROC曲线下面积）", "measurement_cn": "模型对每笔交易输出欺诈概率，与公司调查确认的欺诈/非欺诈标签比较计算AUC", "objectivity_reason_cn": "欺诈标签是由信用卡公司调查确认的外部事实标签，AUC是模型预测与事实标签的量化比较，不依赖人的感受、意义或价值判断"}, {"name_cn": "Accuracy（准确率）", "measurement_cn": "测试集上预测正确的交易比例，按欺诈/非欺诈标签计算", "objectivity_reason_cn": "由预测结果与外部事实标签对比得到，完全客观可审计"}, {"name_cn": "Specificity / Balanced Accuracy（在1%假阳性率下的特异性与平衡准确率）", "measurement_cn": "在测试集上设定1%假阳性阈值后计算的欺诈检出率（特异性）和平衡准确率", "objectivity_reason_cn": "基于交易真实标签和模型输出直接计算，不涉及主观评价"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在APATE特征组合上，分别使用逻辑回归、神经网络和随机森林三种模型进行基准比较，在同一公司真实测试集（约50万笔交易）上报告AUC和accuracy；随后在Section 4.2通过变量子集基准比较（Only RFM、Literature、All Variables - First transaction、Only Social Networks、All variables）展示网络特征加入后AUC从0.953提升到0.986。
- Decision: 文章核心目标是提升信用卡欺诈检测的客观预测性能；核心指标为AUC、accuracy、specificity，欺诈标签为外部可核验事实标签，完全客观。全文没有并列的核心主观目标或理论机制贡献。在Results部分作者使用明确的benchmark表述，对逻辑回归、神经网络、随机森林三个模型进行基准比较，并通过变量子集比较证明网络特征带来的性能提升，benchmark评价支撑了核心客观指标提升主张，且有明确参照点。因此两个模块均通过，strict_include=true。
- Confidence: 0.95

## An effective data clustering measure for temporal selection and projection queries

- Year/journal: 2000 / Decision Support Systems
- DOI: 10.1016/s0167-9236(00)00088-9
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "平均磁盘页访问次数/簇引用次数", "measurement_cn": "通过仿真实验构造聚类后的时间数据库，使用CLARA算法生成与磁盘页数量相等的簇；统计1000次benchmark查询执行期间的平均簇引用次数，作为平均磁盘页访问次数。", "objectivity_reason_cn": "磁盘页访问次数是系统可观测的物理资源消耗指标，完全由查询处理过程和存储布局决定，不依赖人的感受、语义判断或价值评价，数值可直接从实验结果表中读出。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在性能评价部分，作者使用根据canonical temporal query patterns构造的一组benchmark查询，在CLARA聚类框架下比较所提出的temporal affinity（AF）与KEY、TTS、VTS、TTO、VTO等聚类度量。实验在不同数据对象数量N（5000/10000/50000/100000）和对象大小S（30/50/100/200/300字节）下运行，报告每个benchmark查询的平均簇引用次数；结果表6和图13-15显示AF在所有配置下都取得最少的磁盘页访问次数，表6还报告了KEY的较差表现。
- Decision: 文章的核心目标是提出一种新的时间数据聚类度量temporal affinity，并通过减少时间查询处理的磁盘页访问次数来提升性能。该指标是完全客观、可测量的系统性能指标，且是全文唯一的核心目标与贡献，不存在主观构念或并列的理论/制度贡献。全文在性能评价部分明确使用了benchmark一词并构造了benchmark查询集，将其作为评价场地，并与多种已有聚类度量进行比较，结果证明了AF在客观性能指标上的提升。因此，客观指标、唯一核心目标和明确benchmark评价三个方面的门槛均通过，strict_include为true。
- Confidence: 0.95

## An intraday market risk management approach based on textual analysis

- Year/journal: 2011 / Decision Support Systems
- DOI: 10.1016/j.dss.2010.08.019
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "分类性能：accuracy、precision、recall、F1、AUC", "measurement_cn": "在10折交叉验证下，将公司披露按ARISK是否高于75%分位数标记为正/负类，用NB、kNN、NNet、SVM分类，计算混淆矩阵中的accuracy、precision、recall、F1和ROC AUC。ARISK由日内价格计算的已实现波动率经偏差修正后与前期风险比较得出，标签完全由客观价格数据按固定规则生成。", "objectivity_reason_cn": "标签和指标均不依赖人类感受、语义判断或主观评分；价格、波动率、分类结果都是可审计的客观事实和可复现的计算。"}, {"name_cn": "模拟期权策略收益：分类方法选择正类后的跨式期权多头收益均值", "measurement_cn": "在独立测试集上，若披露被预测为正类则模拟买入跨式期权（Black-Scholes定价，基于真实股票价格和利率），到期按实际价格结算，计算收益均值，并与全多头基准策略（R_LONG）比较，并用t检验验证是否显著更高。", "objectivity_reason_cn": "收益由真实股价、固定期权定价公式和确定性规则计算得出，不涉及任何主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在模拟评估中，将四种分类器在设定不同误分类成本下的收益均值与对所有事件都建立多头跨式期权的基准策略（R_LONG）进行比较，并通过t检验验证分类方法是否显著优于该基准。模拟评估是证明文本挖掘方法能识别高风险事件的核心证据。
- Decision: 本研究的核心目标是用文本挖掘方法识别伴随日内超常波动的公司披露，核心成功指标全部为客观计算得到的分类性能和基于真实价格的模拟期权收益，无任何主观构念或并列核心目标。全文存在明确的 benchmark 表述：第6节将分类方法收益与 all-long 基准策略 R_LONG 比较，且该比较是支撑方法有效性主张的核心证据；第5节也提及75%猜测等效基准。因此客观指标、唯一核心目标和 benchmark 三方面均通过。
- Confidence: 0.95

## An upper approximation based community detection algorithm for complex networks

- Year/journal: 2017 / Decision Support Systems
- DOI: 10.1016/j.dss.2017.02.010
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "归一化互信息 (NMI)", "measurement_cn": "将检测到的社区划分与已知 ground-truth 社区标签比较，按 Esquivel et al. 的 NMI 公式计算，用于有已知社区结构的网络。", "objectivity_reason_cn": "社区标签是外部可核验的群体归属事实（俱乐部成员、年级、政治倾向等），NMI 值是确定性的数学计算结果，不依赖人的感受或语义评价。"}, {"name_cn": "Partition Density", "measurement_cn": "在无 ground-truth 的 Les Miserables 网络上，根据检测到的重叠社区内部链接密度计算 D 值。", "objectivity_reason_cn": "该指标由网络拓扑和检测出的社区结构直接计算，属于图结构的可审计度量，不涉及人类主观判断。"}, {"name_cn": "模块度 (Modularity)", "measurement_cn": "在无 ground-truth 的 Jazz、Email、Power Grid 等网络上，根据社区内外边比例计算模块度 Q。", "objectivity_reason_cn": "模块度是基于图边分布的确定函数，反映社区内部的紧密程度，完全客观可计算。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: Karate Club | Risk | Dolphin | High School Friendship | Les Miserables | Polbooks | Football | Jazz | Email | PolBlog | SFI Collaboration | Roget's Thesaurus | Krogan's PPI | Power Grid
- Benchmark evaluation: ROCONA 在 14 个公开标准网络数据集上运行，并与 CPM、ABL、BNMF、OSLOM、FastQ、Walktrap、INFOMAP、LPA 等既有算法比较；有 ground-truth 的网络使用 NMI，Les Miserables 使用 partition density，无 ground-truth 的网络使用 modularity。结果显示 ROCONA 在多数数据集上取得最高或接近最高的客观指标值。
- Decision: 本文核心目标是提出新的社区检测算法 ROCONA，并以 NMI、partition density、modularity 等完全客观的结构性指标证明其检测准确度提升。全文不存在用户主观评价、心理机制或理论解释等并列核心目标。文章在摘要和实验部分明确使用了“fourteen benchmark networks”的表述，在 14 个公开标准网络数据集上进行系统比较，并与多种现有算法对照，benchmark 结果直接支撑“significantly outperforms state-of-the-art”的核心主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.95

## Anticipatory pruning networks and forward checking in CLP over continuous domains

- Year/journal: 1996 / Decision Support Systems
- DOI: 10.1016/s0167-9236(96)80008-x
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "搜索树访问节点数", "measurement_cn": "在树搜索过程中累计计数，见3.2节：'the number of nodes visited is counted cumulatively during the tree search process'。", "objectivity_reason_cn": "节点数是搜索过程的确定性日志计数，不依赖人的感受、语义或价值判断。"}, {"name_cn": "约束检查次数", "measurement_cn": "累计统计规则右侧出现的约束数以及APN一致性检查次数，见3.2节：'The number of constraint checks ... is a cumulative addition of the number of constraints appearing on the right hand of a rule and the consistency checking.'", "objectivity_reason_cn": "约束检查次数是可审计的执行计数，数值由程序和算法确定，无需主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 8-Queens | SEND + MORE = MONEY | GERALD + DONALD = ROBERT | Tennis puzzle | Six months blending problem | Mining problem
- Benchmark evaluation: 作者在经典整数规划问题（如8皇后、SEND+MORE=MONEY等）和混合整数线性规划问题（六个月blending问题、mining问题）上评价minimal 2LP系统在No APN、Partial APN和Full APN三种配置下的搜索节点数和约束检查次数。结果显示Full APN和Partial APN普遍大幅减少节点数和约束检查次数，用以支持APN作为有效forward checking机制的改进主张。
- Decision: 客观指标方面：核心评价指标为搜索树访问节点数和约束检查次数，二者均为可审计的计算痕迹，不依赖人类语义或体验评价，满足fully_objective_direct。唯一核心目标方面：论文围绕APN剪枝机制的客观效率改进展开，摘要、算法设计、测量和结论均以节点数/约束检查数的减少为成功标准，没有并列的核心主观或理论贡献。Benchmark方面：摘要和3.2节明确使用benchmark/benchmarks表述，在评价语境中系统测量APN效果；评价对象正是APN对搜索效率的核心改进主张；且No APN、Partial APN、Full APN提供了明确参照比较。因此strict_include=true。
- Confidence: 0.95

## Attending to Customer Attention: A Novel Deep Learning Method for Leveraging Multimodal Online Reviews to Enhance Sales Prediction

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2021.0292
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "RMSE（均方根误差）", "measurement_cn": "基于酒店月度入住率预测值与真实值的差异计算，经10折交叉验证重复5次，报告均值与标准差。", "objectivity_reason_cn": "入住率是外部可核验的运营事实，预测误差可由系统日志或官方运营记录确定，不依赖人的感受、语义评价或价值判断。"}, {"name_cn": "MAE（平均绝对误差）", "measurement_cn": "类似RMSE，基于月度入住率预测值与真实值的绝对误差计算（在线附录E）。", "objectivity_reason_cn": "同样基于可审计的运营事实，客观且可重复计算。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在自建的酒店评论数据集（2,685家酒店、1.25M评论文本、197K评论图像）上，以RMSE为主要指标，比较DTV-AMI与9个基线/基准方法在文本、图像、多模态三种设置及三个时间跨度下的预测性能；DTV-AMI在所有设置下均取得最优或统计显著改进。
- Decision: 客观指标：核心指标为酒店月度入住率预测的RMSE/MAE，完全客观可验证，所有核心成功结果均为客观预测性能。唯一核心目标：全文以提升销售预测性能为唯一核心设计目标和贡献，客户注意力概念化及注意力机制设计均为该方法服务，无并列核心目标；无主观量表或用户调研。Benchmark：作者在摘要和实验部分明确使用'benchmarked'和'benchmarks'陈述系统化基准比较，在自建数据集上与9个基线/基准方法比较，结果作为核心提升主张的关键证据，且具备明确参照点。因此strict_include为true。
- Confidence: 0.95

## Automated news reading: Stock price prediction based on financial news using context-capturing features

- Year/journal: 2013 / Decision Support Systems
- DOI: 10.1016/j.dss.2013.02.006
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "分类准确率（Accuracy）", "measurement_cn": "正确分类的新闻消息数除以总消息数，通过比较SVM预测的股票价格方向（正/负）与实际观察到的股票价格反应（基于DGAP和EuroAdhoc数据集的日间开盘/收盘价计算）得到。", "objectivity_reason_cn": "预测目标是基于真实市场数据的外部可核验事实（股价上涨/下跌），不依赖人类感知或语义判断；准确率可确定性地从分类结果和真实标签计算。"}, {"name_cn": "交易模拟回报（Trading returns）", "measurement_cn": "通过简单的交易策略（正信号买入、负信号卖空，持有至当日收盘）基于选定的流动性股票（HDAX前110支）的实际股价数据计算平均每笔交易回报和11年组合投资回报，并扣除交易成本、点差和订单影响。", "objectivity_reason_cn": "回报基于实际市场交易和市值变化，是可审计的财务数字，不涉及主观评价。"}, {"name_cn": "R²（预测收益与实际收益的平方相关系数）", "measurement_cn": "使用支持向量回归（SVR）预测股票收益，计算预测收益与实际市场收益之间的平方相关系数。", "objectivity_reason_cn": "R²由客观预测值和实际市场连续收益数据计算，反映预测准确度，不依赖主观评估。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在DGAP和EuroAdhoc两个自有真实企业公告数据集上，对五种特征类型（字典、单词、2-Gram、2词组合、名词短语）分别采用频率降维、Chi²和BNS特征选择进行SVM训练与验证，并与复现的已有文献方法以及多数类分类器（trivial majority classifier）在相同数据上进行对比。结果显示2词组合+BNS达到最高准确率76.3%（DGAP）和65.4%（EuroAdhoc），显著优于多数类基准（58.2%和53.3%）及文献中低于60%的水平。
- Decision: 核心指标为股票价格方向预测准确率、R²和交易回报，均基于外部市场可核验事实，完全客观，不涉及主观语义评价。文章从研究问题、设计到评价均围绕提升分类准确率展开，且无并列的主观或理论核心目标。全文明确使用benchmarking描述通过复现文献方法在相同数据上的系统比较，并以多数类分类器和复现基线作为参照，结果直接支撑准确率提升主张，因此满足全部benchmark门槛。
- Confidence: 0.95

## Automatic feature weighting for improving financial Decision Support Systems

- Year/journal: 2018 / Decision Support Systems
- DOI: 10.1016/j.dss.2018.01.005
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "AUC（Area under the ROC Curve，ROC曲线下面积）", "measurement_cn": "在10个UCI金融数据集上，使用Dob-SCV五折分层交叉验证计算NAC分类器在决策支持中的AUC；AUC由混淆矩阵中的TPR和TNR平均值计算获得；同时记录三种元启发式算法的执行时间（秒）。", "objectivity_reason_cn": "AUC由分类器在已有事实标签（如破产、违约、银行订阅、真伪纸币）上的预测结果与真实标签比对计算得到，不依赖人的感受、语义评价或价值判断；执行时间为系统时钟可观测的物理事实。"}, {"name_cn": "执行时间（秒）", "measurement_cn": "在阶段1中分别记录DE、GA、NBA三种元启发式算法在10个数据集上的平均执行耗时，并以Friedman检验和Holm事后检验比较差异。", "objectivity_reason_cn": "执行时间是系统运行可观测的物理事实，不涉及任何主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: UCI Machine Learning Repository 中的10个金融数据集（Bank、Bank-additional、Bank-additional-full、Bank-full、Banknote、Bankruptcy、Credit-approval、Credit-Australian、Credit-German、Default-credit）
- Benchmark evaluation: 在所选的10个UCI金融数据集上，以AUC为指标评价了C4.5、NB、NAC及NAC分别使用DE/GA/NBA自动权重后的性能，并通过Friedman检验和Holm事后检验比较；结果显示NAC DE在6个数据集上最优，NAC NBA在3个数据集上最优，NAC GA在2个数据集上最优，且显著优于未加权的NAC、C4.5和NB。
- Decision: 客观指标方面：核心指标是AUC和执行时间，均完全客观，且来自可核验的金融事实标签（违约、破产、银行订阅、真伪纸币）和系统计时；研究问题、方法目标、实验结果和贡献声明均唯一围绕提升NAC决策性能和降低计算成本展开，未发现并列的主观或理论核心目标。Benchmark方面：全文虽未使用“benchmark”单词，但在第5节明确以UCI ML Repository的10个金融数据集作为评价场地，并与C4.5、NB、未加权NAC及三种元启发式变体进行系统的基准对比，Friedman/Holm统计检验支撑了AUC提升的核心主张；存在明确参照点。因此满足两个模块的纳入条件。
- Confidence: 0.95

## Automating in High-Expertise, Low-Label Environments: Evidence-Based Medicine by Expert-Augmented Few-Shot Learning

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2024/18573
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "句子分类性能（F1@3、PRC）", "measurement_cn": "在WD、COVID和EBM-NLP三个数据集上，对PICO元素相关句子的检索性能，根据专家标注的PICO元素事实标签计算top-3精确率、召回率、F1和PRC", "objectivity_reason_cn": "PICO元素对应医学文献中的客观事实（患者、干预、结局等），标签不依赖主观感受或价值判断；F1、PRC等指标由确定性公式计算"}, {"name_cn": "序列标记性能（F1、BERTScore、PRC）", "measurement_cn": "在识别出的句子中标记PICO片段，用词级F1和语义相似度BERTScore以及PRC评估，对比专家标注的PICO片段", "objectivity_reason_cn": "PICO片段是文献中可核验的具体医学信息，性能指标基于客观重叠计算，BERTScore基于固定嵌入的余弦相似度"}, {"name_cn": "SR项目时间节省（最多65%）", "measurement_cn": "基于WD SR项目的真实工作流程，根据FastSR与人工、其他ML方法的完成时间对比估计项目总时间减少百分比", "objectivity_reason_cn": "时间是可审计的客观资源消耗，节省百分比由工作流时间模型计算，不依赖主观感受"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: EBM-NLP
- Benchmark evaluation: 在WD、COVID（CORD-19）和公开EBM-NLP数据集上，将FastSR与传统分类器（SVM、CNN等）、半监督（VAT）、LLM（fine-tuned BioBERT、GPT-4 few-shot）、FSL模型（ProtoNet、MAML等）等进行比较，报告句子分类F1@3、PRC和序列标记F1、BERTScore、PRC。结果显示FastSR在各个数据集上全面优先进（例如WD句子分类F1@3 73.00 vs ProtoNet 65.40 vs GPT-4 39.23；EBM-NLP句子分类F1@3 79.71 vs ProtoNet 77.26）。
- Decision: 客观指标方面：文章核心是提升PICO元素提取的客观性能指标（句子分类和序列标记的F1、PRC），以及由此带来的时间节省，这些指标均基于可核验的医学事实标签和确定计算公式，不存在并列的主观核心成功标准。唯一核心目标：研究问题、设计需求（DR1-DR4）、评价结构和贡献声明均围绕客观提取性能和时间节省，理论指导和定性反馈属于支撑性内容，不构成与客观指标提升并列的核心目标。Benchmark方面：全文在评估方法部分明确宣称进行benchmark比较，并在三大数据集上与大量基准模型进行系统比较，结果表包含明确参照点和显著性检验，benchmark结果直接支撑FastSR性能提升的核心主张。因此满足纳入条件。
- Confidence: 0.95

## CATCHM: A novel network-based credit card fraud detection method using node representation learning

- Year/journal: 2023 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113866
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "AUCPR（精确率-召回率曲线下面积）", "measurement_cn": "基于模型预测得分与经调查确认的欺诈标签计算 precision-recall 曲线下面积；10次滚动窗口重复实验取均值。", "objectivity_reason_cn": "欺诈标签是经调查确认的外部事实，AUCPR 由预测与事实标签确定性计算，不依赖人的感受或语义评价。"}, {"name_cn": "F1 分数", "measurement_cn": "在验证集上优化阈值后，以预测类别与欺诈标签计算精确率和召回率的调和平均。", "objectivity_reason_cn": "输入是客观欺诈标签和可复现的预测结果，计算规则固定，指标值可审计。"}, {"name_cn": "TP@300（每日前300个标记案件中的真实欺诈数）", "measurement_cn": "按模型怀疑分数排序，取每日最多300个标记案件，统计其中被确认为欺诈的案件数。", "objectivity_reason_cn": "由调查确认的欺诈标签和系统标记结果计数得到，属于可审计的业务结果指标。"}, {"name_cn": "PPT_A（平均单笔交易预测处理时间）", "measurement_cn": "在批量层面测量并除以交易数量，得到单笔交易的平均预测处理时间，以毫秒计。", "objectivity_reason_cn": "处理时间是系统日志可测的客观物理量，不依赖主观评判。"}, {"name_cn": "Revenue（挽回资金收益）", "measurement_cn": "按每日300个标记案件统计被阻止欺诈交易所对应的金额，以欧元计，并在10天测试期汇总。", "objectivity_reason_cn": "交易金额和欺诈标签是客观事实，计算得到的收益是可审计的财务结果。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: DeepWalk | Node2Vec | PageRank | GraphSAGE
- Benchmark evaluation: 在约324万笔真实信用卡交易数据（欺诈率0.32%）上，使用1/2/4天训练数据、1天测试的滚动窗口重复10次，将CATCHM与DeepWalk、Node2Vec、PageRank、GraphSAGE等基准方法进行比较；同时加入原始特征基线和RFM特征基线。评价指标包括AUCPR、F1、TP@300、处理时间和挽回收益，并用Bayesian signed-rank检验比较显著性。结果显示CATCHM在主要分类指标上优于各基准，且满足100毫秒处理时间约束。
- Decision: 客观指标方面，本文的欺诈标签是经调查确认的外部事实，AUCPR、F1、TP@300、处理时间和挽回收益均为客观可测、可审计的指标，全文核心目标与贡献是提升这些客观性能指标，没有主观构念或并列的理论/制度贡献。Benchmark方面，虽然未使用公开命名的数据集，但作者明确以“Benchmarks”章节和“benchmarked techniques”等表述陈述了系统化的基准比较，将该比较作为核心证据，并与Baseline、DeepWalk、Node2Vec、PageRank、GraphSAGE等明确参照点比较，因此满足benchmark门槛。两个模块均通过，strict_include为true。
- Confidence: 0.95

## Classification by vertical and cutting multi-hyperplane decision tree induction

- Year/journal: 2010 / Decision Support Systems
- DOI: 10.1016/j.dss.2009.06.004
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "分类准确率（LOO命中率）", "measurement_cn": "在Japanese Banks和Wisconsin Breast Cancer数据集上采用留一法交叉验证，计算正确分类样本数占总测试数的百分比", "objectivity_reason_cn": "分类标签是银行/肿瘤等事实状态，不依赖人类感受或语义评价；正确分类与否可确定性观测并审计"}, {"name_cn": "计算时间（每次LOO测试的秒数）", "measurement_cn": "使用CPLEX 10.0在同一工作站的运行时间，按每次留一法测试记录", "objectivity_reason_cn": "物理可测的运行时间，不依赖主观体验"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: Japanese Banks data set (Sueyoshi, 2001) | Wisconsin Breast Cancer database (UCI repository)
- Benchmark evaluation: 在两个基准数据集上，以留一法比较VDT、CDT、Glen模型、SVM和OC1的LOO命中率与时间；表格1-4报告了不同分离带宽度下的结果，并对CDT与Glen进行配对t检验
- Decision: 客观指标（分类准确率和计算时间）是全文唯一核心目标和核心贡献，不存在主观量表或理论机制等并列核心目标；分类标签为事实状态，性能指标客观可审计。全文在实验部分明确使用两个命名基准数据集（Japanese Banks和UCI Wisconsin Breast Cancer），并明确以benchmark表述进行系统化基准评价，结果与Glen、SVM、OC1等多个参照点比较，benchmark结果直接支撑核心改进主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.95

## Collaborative user modeling for enhanced content filtering in recommender systems

- Year/journal: 2011 / Decision Support Systems
- DOI: 10.1016/j.dss.2011.01.012
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "Hit Rate (HR) 命中率", "measurement_cn": "将用户历史兴趣项目随机划分为训练集和测试集，计算测试集项目与系统返回的Top-N推荐列表的交集数量，再除以测试项目数；最后对所有用户平均。", "objectivity_reason_cn": "HR基于兴趣内容与推荐列表的集合运算，是可审计的客观计数；不依赖用户主观评价、语义质量判断或偏好感受。"}, {"name_cn": "Reciprocal Hit Rank (RHR) 倒数命中排名", "measurement_cn": "对每个用户测试集中被命中的推荐项目，取推荐排名的倒数并求和；再对所有用户平均。排名和命中集合均由系统输出与历史兴趣记录确定。", "objectivity_reason_cn": "RHR由推荐列表中的客观位置和历史兴趣事实决定，计算规则固定，值可复现；不涉及人工评分或语义评估。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: MovieLens（MLens） | NSF research award abstracts（NSF）
- Benchmark evaluation: 在NSF和MovieLens两个数据集上，以固定训练/测试划分构建用户模型，将所提M+与UCF、ICF、NB、VT四种基准算法比较，并报告不同N值和邻域规模下的HR和RHR。结果表和图明确显示M+多数情况下优于基准方法。
- Decision: 该文是推荐系统方法论文，核心目标是提升Top-N推荐质量，HR和RHR是唯一核心成功指标且完全客观。全文没有用户调研、主观量表或专家评分作为成功标准；也没有将理论机制、组织变革、政策建议等作为并列核心贡献。实验部分明确使用“benchmark algorithms/benchmark methods”的基准评价表述，在MovieLens和NSF数据集上与UCF、ICF、NB、VT等明确参照点比较，benchmark结果直接支撑其核心改进主张。两个模块均通过，strict_include=true。
- Confidence: 0.95

## Comparative issues in large-scale mean–variance efficient frontier computation

- Year/journal: 2011 / Decision Support Systems
- DOI: 10.1016/j.dss.2010.11.018
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "计算时间（CPU time）", "measurement_cn": "在 2.66 GHz Core 2 Duo Dell 桌面计算机上，对每个规模、方法和优化器组合运行样本量5，测量计算单个有效前沿中间点或整条连续有效前沿的平均时间。", "objectivity_reason_cn": "计算时间是物理可测量的运行资源消耗指标，不依赖任何人的感受、语义理解或价值判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 论文在 500、1000、1500、2000、3000 证券的100%密集协方差矩阵 Markowitz 问题上，对 e-约束法、λ-参数法和参数二次规划（CIOS）以及 Risk Solver Platform、Matlab、LINGO、Cplex 等优化器进行系统化时间基准评价。表4-6显示 CIOS 计算整条有效前沿的时间远小于离散方法计算单点的时间（如 n=1000 时 CIOS 5.3s vs Cplex 单点 6.0s；n=2000 时 CIOS 23.1s vs Cplex 单点 38.6s）。该基准结果用于支持参数二次规划方法在大规模前沿计算中的核心主张。
- Decision: 客观指标：核心指标为计算有效前沿所需的 CPU 时间，是完全客观可测的技术资源指标。唯一核心目标：全文从问题提出、实验设计到结论均围绕计算时间基准比较和参数二次规划方法的性能优势展开，不存在主观体验、理论机制或其他并列核心贡献。Benchmark：作者明确使用 benchmark/benchmarking 表述建立大规模有效前沿计算时间基准，并在实验和结果部分以此支撑核心速度提升主张，且有多重参照点比较。因此 strict_include=true。
- Confidence: 0.95

## Creating Proactive Cyber Threat Intelligence with Hacker Exploit Labels: A Deep Transfer Learning Approach

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2023/17316
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "准确率、精确率、召回率、F1-score", "measurement_cn": "在黑客论坛目标域以及暗网市场/公开漏洞库源域上，以八类攻击类型标签（Web应用、DoS、远程、本地、SQL注入、XSS、文件包含、溢出）计算分类性能，使用带类支持的加权平均和单尾配对t检验比较模型。", "objectivity_reason_cn": "攻击类型标签是可外部核验的技术事实（代码执行方式），不依赖人的感受、偏好或语义价值判断；指标由真实标签与预测结果的确定性计数计算。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在作者自建的源域（漏洞DNM和公开漏洞库）与目标域（黑客论坛）数据集上，将DTL-EL与经典ML（朴素贝叶斯、逻辑回归、决策树、SVM、XGBoost、LightGBM）、非DTL深度学习方法（RNN、GRU、LSTM、BiLSTM、BiLSTM+自注意力）、其他迁移学习方法（自适应SVM、MTL、对抗学习、BERT）以及层选择消融进行对比，报告准确率、精确率、召回率、F1-score，并给出统计显著性检验。
- Decision: 文章以黑客漏洞利用代码标签分类为核心，所有核心成功指标均为基于攻击类型事实标签的准确率、精确率、召回率和F1-score，属于客观可核验的分类性能；研究目标、评价结构和贡献声明均围绕提升该客观分类指标展开，无主观满意度等并列核心目标。全文在摘要和实验部分明确使用“benchmark experiments/methods”表述，并在自建源域和目标域数据集上开展系统化基准比较，包含经典ML、非DTL深度模型、其他迁移学习方法及消融分析等明确参照点，benchmark评价直接支撑核心改进主张。因此两个模块均通过，strict_include为true。
- Confidence: 0.95

## Cross-Lingual Cybersecurity Analytics in the International Dark Web with Adversarial Deep Representation Learning

- Year/journal: 2022 / MIS Quarterly
- DOI: 10.25300/misq/2022/16618
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "跨语言黑客资产检测的准确率（Accuracy）、F1-score、AUC", "measurement_cn": "在作者构建的多语言 gold-standard 数据集上，通过五折交叉验证计算分类准确率、F1 和 AUC，并进行配对 t 检验。标签由母语者和网络安全专家按黑客资产/非黑客资产的操作化定义标注。", "objectivity_reason_cn": "黑客资产（恶意软件、黑客工具、黑客教程、恶意源代码）属于可核验的网络安全事实类别，类似 malware/fraud 等固定事实标签；标注过程记录的是内容的功能性类别，而非满意度、质量、价值或偏好等主观体验。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在作者构建的多语言 dark web gold-standard 测试集（英文、俄文、法文、意大利文）上，将 CLHAD 与 lexicon baseline、monolingual 传统ML/深度模型、MT-based 方法、CLKT 替代方法（FML-CNN、MTL-BiLSTM、MTL-BiGRU）进行比较。结果显示 CLHAD 在俄、法、意的 hacker forums 和 DNMs 上 Accuracy/F1/AUC 均达到最优，且多数差异具有统计显著性。
- Decision: 客观指标方面，核心成功指标为黑客资产检测的 Accuracy/F1/AUC，属于固定事实标签上的分类性能，非主观体验或语义质量评价；核心目标是提升跨语言黑客资产检测性能，无并列主观或理论核心目标。benchmark 方面，作者在评价部分明确使用“benchmark methods”并以多种既有基线/方法作为参照，benchmark 比较结果是支持核心提升主张的主要证据。因此两个模块均通过，strict_include=true。
- Confidence: 0.95

## Data mining of Bayesian networks using cooperative coevolution

- Year/journal: 2004 / Decision Support Systems
- DOI: 10.1016/s0167-9236(03)00115-5
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "平均最终MDL分数（AFS）", "measurement_cn": "在ALARM和PRINTD基准网络生成的数据集上，运行CCGA 40次后最终网络结构的MDL得分平均值；MDL分数由固定的MDL准则计算得出。", "objectivity_reason_cn": "MDL分数由数据、网络结构和确定性公式算出，不依赖人的感受、语义评判或偏好，构念和值均客观。"}, {"name_cn": "平均执行时间（AET）", "measurement_cn": "算法运行到终止条件所需的平均秒数，由工作站计时获取。", "objectivity_reason_cn": "执行时间是可直接观测的技术性能指标，完全客观。"}, {"name_cn": "平均结构差异（ASD）", "measurement_cn": "最终发现网络与已知原始网络相比，增加、删除和反向的边数之和的平均值；原始网络结构作为固定参照。", "objectivity_reason_cn": "结构差异通过比较两个有向图的边集合而计算，为可审计的客观事实。"}, {"name_cn": "累计提升量、预期收益等直销响应指标", "measurement_cn": "在真实直销数据集上按十分位分析计算累计lift、累计活跃客户百分比和按购买金额估算的收益；基于实际购买记录和模型排序结果。", "objectivity_reason_cn": "购买与否、金额和排名来自实际交易数据与固定统计公式，不涉及主观体验或价值判断。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: ALARM network | PRINTD network
- Benchmark evaluation: 在ALARM-1000/2000/5000/10000/ALARM-O和PRINTD-5000六个基准数据集上，对CCGA和MDLEP各运行40次，比较AFS、AET、ASD等客观指标。结果显示CCGA在MDL分数和结构差异上不劣于或优于MDLEP，且执行时间快3.4至5.0倍；这些benchmark结果直接支撑核心‘更有效和更高效’的改进主张。
- Decision: 客观指标方面：核心成功指标全部是MDL分数、执行时间、结构差异、累计lift和收益等确定性可观测指标，不依赖人类感知或语义判断；唯一核心目标是提升贝叶斯网络学习的有效性和效率，不存在其他并列核心目标。benchmark方面：第5.1节明确使用ALARM和PRINTD这两个公开基准网络生成数据集作为评价场地，并与MDLEP基线比较，结果直接支持核心改进主张。因此两个模块均通过，strict_include为true。
- Confidence: 0.95

## Decisions for information or information for decisions? Optimizing information gathering in decision-intensive processes

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113632
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "期望利润（expected profit）", "measurement_cn": "由信息结构函数 Y（基于已知属性值和最终决策计算期望收益）减去信息收集任务成本得到；案例中实际为 Expected profit = Expected revenue - Average retrieval cost 等，数据来源为 Table 3 中任务成本、Table 4 中属性概率分布，以及 MDP 求解结果。", "objectivity_reason_cn": "期望利润、收益和成本均为可审计的财务/时间/交易类事实，由概率分布和明确数学公式计算得出，不依赖任何人的感受、语义理解或价值判断，可以独立复算和比较。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 决策树基准（基于公司现有决策过程、由销售经理合作创建，作为 Koffer 案例的内部 benchmark，非公开数据集）
- Benchmark evaluation: 在真实世界 Koffer 报价流程案例上，将本文 MDP 优化方法的结果与基于公司现有决策过程、由销售经理合作创建的人类决策树（明确称为 benchmark）进行系统比较。Table 5 显示 MDP 期望利润 15,867.6，而决策树为 8,226.0，MDP 将期望利润翻倍；Table 6 进一步对 9 个随机实例逐个比较利润，展示平均上的改进。
- Decision: 客观指标方面：核心成功指标是完全客观、可计算的期望利润（收益减成本），不依赖主观感受或语义判断，且提升该客观指标是全文唯一核心目标与核心贡献。Benchmark 方面：Section 7.1 明确将人类决策树称为 benchmark，并在评价语境中（Section 7.4）将其作为明确参照点，系统比较 MDP 与决策树的期望利润，直接支撑“MDP 使期望利润翻倍”的核心改进主张；比较对象虽然是非公开的案例特定决策树，但作者明确以 benchmark 一词陈述了该基准评价，满足陈述式门槛。因此两个模块均通过，strict_include=true。
- Confidence: 0.95

## Discovering event episodes from sequences of online news articles: A time-adjoining frequent itemset-based clustering method

- Year/journal: 2020 / Information & Management
- DOI: 10.1016/j.im.2020.103348
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "聚类召回率（Cluster Recall）、聚类精确率（Cluster Precision）与F值", "measurement_cn": "以Nallapati事件语料中已标注的事件片段为真值，计算系统生成片段与真值片段之间文档关联集合的重叠比例：CR=|CA|/|TA|, CP=|CA|/|GA|；再按事件加权平均，并用F-measure综合精确率与召回率；Wilcoxon符号秩检验比较方法间差异。", "objectivity_reason_cn": "事件片段归属是外部可核验的文档-事件阶段事实标签，不是对质量、价值或感受的主观评价；CR/CP/F由确定性公式从聚类结果和固定标签计算得出。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: TDT2 | TDT3 | Nallapati事件语料（248片段/53事件/1468篇文章）
- Benchmark evaluation: 在Nallapati等人提供、选自TDT2/TDT3的新闻事件语料上，将TAFIED与FIHC、HAC、HAC+TD三个基准技术比较；主要结果为图7的PRT曲线、表5的最佳F值（TAFIED 0.584，FIHC 0.543，HAC 0.533，HAC+TD 0.567）以及表6的Wilcoxon检验（对HAC p<0.01、对FIHC p<0.05、对HAC+TD p<0.1）。
- Decision: 客观指标：事件片段发现的CR/CP/F基于固定事实标签和确定性公式，属于客观可测结果；唯一核心目标是提升该聚类性能。Benchmark：作者明确把FIHC、HAC、HAC+TD称为benchmark techniques，并在TDT2/TDT3事件语料上进行系统比较，比较结果直接支撑核心提升主张且具备明确参照点。故两个模块均通过，strict_include=true。
- Confidence: 0.95

## EXPRS: An extended pagerank method for product feature extraction from online consumer reviews

- Year/journal: 2015 / Information & Management
- DOI: 10.1016/j.im.2015.02.002
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "特征提取的精确率、召回率、F值", "measurement_cn": "在jd.com三个产品的真实评论数据上，由人工标注形成正确特征集作为金标准，将自动提取的特征集与金标准比对，计算精确率、召回率和F值。", "objectivity_reason_cn": "产品特征（如电池、屏幕、价格等）是客观存在的产品属性或属性类别，不依赖于人的感受、偏好或价值判断；人工标注只是识别评论中是否提及这些客观特征，P/R/F计算规则明确、可重复。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在三个产品（Samsung Galaxy Note II、Canon EOS 600D、Philips DVP3600）的在线评论数据上，将EXPRS及其消融变体M1、M2与两种基准方法HAC和HITS比较精确率、召回率和F值，并通过配对T检验和Cohen's d效应量验证改进显著性。
- Decision: 文章核心目标是提升产品特征提取的精确率、召回率和F值，这些指标基于人工标注的客观产品特征标签，属于客观可测的性能指标，且是唯一核心目标和贡献；评价部分明确以HAC、HITS作为benchmarks，并在评价语境中比较了多个基准方法，结果表支持核心提升主张，因此满足全部纳入条件。
- Confidence: 0.95

## Economic metaphors for solving intrafirm allocation problems: What does a market buy us?

- Year/journal: 2006 / Decision Support Systems
- DOI: 10.1016/j.dss.2006.02.009
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "解质量（最优性差距）", "measurement_cn": "在可求解到最优的算例上，用 1 - V_heuristic / V_complete 计算与已知最优解的差距；在大型算例上以 Tabu 搜索解为参照比较相对百分比。", "objectivity_reason_cn": "解质量由算法输出值与最优解或基线解的可计算比值确定，不依赖人的感知、语义偏好或质量评价。"}, {"name_cn": "计算时间", "measurement_cn": "记录各算法达到均衡或给定停止条件所需的秒数，比较市场算法与 Tabu 搜索在相近时间约束下的表现。", "objectivity_reason_cn": "计算时间是可审计的机器运行事实，完全客观。"}, {"name_cn": "agent valuation list 的实际规模", "measurement_cn": "统计随机生成实例中每个 agent 的非支配、可行 valuation tuple 数量，并与最坏情况 2^d 比较。", "objectivity_reason_cn": "valuation list 规模是算法内部数据的可测量计数，不涉及主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在随机生成的多作业单机随机调度测试集上，作者以 complete search（完备搜索得到最优解）作为小规模算例的基准，以 tabu search 作为大规模算例的基准，分别评价 Market（SUBLIST 协议）和 Market(b-limit) 的解质量与计算时间；结果表明 Market 在相近时间内获得更优或更高的解质量。
- Decision: 客观指标方面：核心成功指标是解质量（最优性差距）和计算时间，均为可直接计算、不依赖人类感知或语义判断的客观性能指标；研究问题、实验设计和贡献声明都围绕这些客观指标。唯一核心目标方面：文章没有把主观体验、心理机制、理论机制或政策建议作为并列核心贡献，Discussion 中的灵活性和鲁棒性是定性优势补充而非核心成功标准。Benchmark 方面：第 4.2 节明确使用“benchmark”一词，将 complete search 作为小规模算例的基准、tabu search 作为大规模算例的基准，并在评价语境中通过表格和图形比较 Market/Tabu 的解质量和时间，这些 benchmark 结果直接支撑市场搜索算法提升解质量的核心理由。因此两个模块均通过，strict_include=true。
- Confidence: 0.95

## Effective spam filtering: A single-class learning and ensemble approach

- Year/journal: 2008 / Decision Support Systems
- DOI: 10.1016/j.dss.2007.06.010
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "准确率（accuracy）", "measurement_cn": "在LingSpam和PU1语料库上，分类正确的邮件数占测试邮件总数的比例，经30次随机验证取平均。", "objectivity_reason_cn": "基于垃圾/合法邮件的客观事实标签与分类器输出直接计算，不依赖人的感受或语义评价。"}, {"name_cn": "精确率（precision for spam）", "measurement_cn": "被分类为垃圾邮件的邮件中实际为垃圾邮件的比例，基于语料库事实标签统计。", "objectivity_reason_cn": "垃圾邮件标签是外部可核验事实，计算方式确定性可审计。"}, {"name_cn": "召回率（recall for spam）", "measurement_cn": "实际垃圾邮件中被正确识别为垃圾邮件的比例，基于语料库事实标签统计。", "objectivity_reason_cn": "垃圾邮件标签是外部可核验事实，计算方式确定性可审计。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: LingSpam | PU1 | PNB | PEBL
- Benchmark evaluation: 在LingSpam和PU1两个公开垃圾邮件语料库上，将所提出的E2与基准技术PNB、PEBL进行系统比较。评价指标为准确率、精确率、召回率。结果显示：LingSpam上E2准确率98.45%略低于PNB（99.13%），但显著高于PEBL（93.29%），精确率最高，召回率91.15%显著优于PEBL；PU1上E2准确率95.67%、召回率97.81%，显著优于PNB和PEBL。另做了对P(Cp)敏感性和训练样本规模效应的对比实验。
- Decision: 客观指标方面：全文以垃圾邮件过滤中的准确率、精确率、召回率作为唯一成功标准，标签为语料库中垃圾/合法邮件的事实标签，指标计算完全客观可审计；提升这些客观指标是全文唯一核心目标与贡献，没有主观量表和并列理论贡献。Benchmark方面：作者在摘要、引言和实验评价中反复以'benchmarks'明确指称PNB和PEBL作为性能基准，并在LingSpam和PU1两个公开语料库上系统比较E2与基准技术，结果表提供明确参照点，支撑核心提升主张。因此两个模块均通过，strict_include为true。
- Confidence: 0.95

## Efficient Computational Strategies for Dynamic Inventory Liquidation

- Year/journal: 2019 / Information Systems Research
- DOI: 10.1287/isre.2018.0819
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "清算总收入（total liquidation revenue）", "measurement_cn": "在随机需求模拟中，根据每日定价、顾客到达和顾客估值计算实际销售量与收入，汇总整个清算期的总收入；公式为 R(S_d,d)=S_d * p_d 和总收入 = Σ R(S_d,d)。", "objectivity_reason_cn": "总收入是可审计的货币化结果，由确定的模拟交易和数学计算产生，不依赖人的感受、语义判断或价值评价。"}, {"name_cn": "计算运行时间/可扩展性（running time / scalability）", "measurement_cn": "记录求解清算策略的运行时间（秒），并通过给定时间框架内可处理的最大问题规模比较不同方法的扩展性；例如 Table 5 和 Table 6 报告 PDS、SDP、ADP 的运行时间及倍数差异。", "objectivity_reason_cn": "运行时间是可客观测量的物理量，问题规模和参数均有明确表述，不涉及主观体验。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在随机需求模拟环境下，作者将启发式策略 PAS/PDS 与 FP、FQ、DP、DQ 等简单基准比较，并进一步将 PDS 与 SDP、ADP 两类先进随机动态规划方法比较；报告总收入、收入偏差和运行时间。结果显示 PAS/PDS 在多个配置下收入显著更高，PDS 相对 SDP 仅有 0.03%–1.12% 的收入损失，但快 3,000–86,000 倍，从而支撑核心的收入/效率改进主张。
- Decision: 文章以库存清算总收入最大化和计算效率为客观核心目标，所有核心评价均为模拟得到的收入、运行时间、问题规模和可扩展性，不涉及主观构念或人类语义评价。全文在摘要和 Section 6 明确使用 benchmark 表述，并与 FP/FQ/DP/DQ/SDP/ADP 等明确参照点比较，benchmark 结果直接支撑启发式方法在收入和效率上的核心改进主张。因此 objective_metric.pass=true，benchmark.pass=true，strict_include=true。
- Confidence: 0.95

## Encoding resource experience for predictive process monitoring

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113669
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "AUC（ROC曲线下面积）", "measurement_cn": "在公开事件日志上训练二分类模型（随机森林、XGBoost），对前缀进行预测，基于真阳性和假阳性率计算AUC", "objectivity_reason_cn": "AUC由模型输出与已知客观业务结果标签（如客户投诉、产品退回、是否按时完成、贷款是否获批、罚款是否缴清）计算得出；标签是事件日志中的客观事实，不依赖人类主观评价"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: Teinemaa et al. [50] benchmark（包含BPIC2011、BPIC2012、BPIC2015、Road Traffic Fines事件日志）
- Benchmark evaluation: 在Teinemaa等公开基准所包含的多个事件日志（BPIC2011、BPIC2012、BPIC2015、Road Traffic Fines）上，比较使用资源经验特征（rac）与不使用资源经验特征（nrac）的模型AUC；结果显示BPIC2012中rac明显更优，BPIC2015部分日志中rac更优，BPIC2011和RTF无显著差异。
- Decision: 文章核心目标是通过在公开事件日志上的基准比较提升预测模型AUC这一完全客观指标；预测标签（客户投诉、产品退回、是否按时完成、申请接受/取消/拒绝、罚款是否缴清）均属于客观事实，AUC计算不涉及主观评价。全文有明确benchmark表述（Section 5.1引用Teinemaa et al.基准）并位于实验评价部分，比较了rac与nrac，基准结果直接支撑核心提升主张。无主观构念，理论部分仅作为背景和特征设计依据，不构成并列核心贡献。因此两个模块均通过，strict_include为true。
- Confidence: 0.95

## Exploiting Expert Knowledge for Assigning Firms to Industries: A Novel Deep Learning Method

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/17171
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "行业分类准确率（Accuracy）", "measurement_cn": "将模型预测的行业代码与Compustat/NAICS或GICS中的真实行业代码逐一比对，计算正确分类的新企业占全部新企业的比例。", "objectivity_reason_cn": "行业代码是权威数据库中的既定事实标签，分类是否正确可直接由离散标签比对确定，不依赖评测者的主观感受或语义质量判断。"}, {"name_cn": "宏平均F1（Macro-F1）", "measurement_cn": "以每个行业为类别，分别计算precision和recall后求F1，再对所有行业取算术平均。", "objectivity_reason_cn": "基于外部事实标签的混淆矩阵计算，指标值完全由预测结果和真实行业代码决定，不涉及主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: NAICS 2012 | GICS 2016
- Benchmark evaluation: 作者在两个公开行业分类体系NAICS和GICS上，将DeepIA与SVM-IA、MLP-IA、ULMFiT-IA、HC-IA、LE-IA等既有的行业分类方法或可改编的对比方法进行系统比较，使用accuracy和macro-F1作为评价指标；主结果中DeepIA在NAICS各焦点层级上均最高，例如T=2015、l*=3时accuracy 0.68，宏F1 0.26，并显著优于全部基准方法。
- Decision: 客观指标方面，核心成功指标是行业分配准确率和宏平均F1，基于权威数据库中的既定行业标签进行比较，指标完全客观，不依赖主观判断；唯一核心目标是提升行业分配性能，动态表示和分层分配是服务于该目标的算法创新而非并列核心贡献。Benchmark方面，文章在Empirical Evaluation中明确使用“We benchmarked DeepIA against…”并在Benchmark Methods节列出多个现有方法，在NAICS和GICS两个公开行业分类体系上系统比较，以accuracy和macro-F1证明DeepIA优于多个基准，benchmark评价是支撑核心改善主张的直接证据，且具有明确的比较对象。因此严格判定为纳入。
- Confidence: 0.95

## FILM: a fuzzy inductive learning method for automated knowledge acquisition

- Year/journal: 1997 / Decision Support Systems
- DOI: 10.1016/s0167-9236(97)00019-5
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "预测准确率", "measurement_cn": "在八个数据集上使用留一法、70/30划分或10折交叉验证，计算三类方法正确预测的案例比例", "objectivity_reason_cn": "预测对象是客观事实类别（破产/非破产、是否患病、鸢尾种类、模拟类别等），准确率按已知事实标签统计，不依赖人的感受或语义评价"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: Iris data | Appendicitis data | Breast cancer data | Wisconsin breast cancer data | Pima Indians diabetes data | Blood data | Bankruptcy data | Simulated data
- Benchmark evaluation: 在八个数据集上，FILM与判别分析（DA）和ID3作为基准进行比较；表2报告各方法的预测准确率，FILM平均0.857，高于DA的0.820和ID3的0.796，且与ID3差异在5%水平显著。
- Decision: 该文核心目标是提升预测准确率这一完全客观的可测量指标，且是唯一核心贡献；评价中使用DA和ID3作为基准，在多数据集上通过分类准确率比较验证FILM的提升效果，满足明确benchmark表述、处于评价语境、支撑核心主张且具有明确比较对象。因此 strict_include=true。
- Confidence: 0.95

## Financial time series forecasting using independent component analysis and support vector regression

- Year/journal: 2009 / Decision Support Systems
- DOI: 10.1016/j.dss.2009.02.001
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "RMSE", "measurement_cn": "实际值与预测值之间均方根误差", "objectivity_reason_cn": "由数值计算得出，不依赖主观判断"}, {"name_cn": "NMSE", "measurement_cn": "标准化均方误差", "objectivity_reason_cn": "由数值计算得出，不依赖主观判断"}, {"name_cn": "MAD", "measurement_cn": "平均绝对误差", "objectivity_reason_cn": "由数值计算得出，不依赖主观判断"}, {"name_cn": "DS", "measurement_cn": "方向正确率", "objectivity_reason_cn": "根据预测值与实际值的涨跌方向是否一致计算，客观可验证"}, {"name_cn": "CP", "measurement_cn": "上涨趋势正确率", "objectivity_reason_cn": "根据预测值与实际值在上涨情况下的方向一致程度计算"}, {"name_cn": "CD", "measurement_cn": "下跌趋势正确率", "objectivity_reason_cn": "根据预测值与实际值在下跌情况下的方向一致程度计算"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在Nikkei 225和TAIEX两个数据集上，使用60%、70%、80%、90%四种训练/测试比例，比较ICA-SVR与random walk和SVR模型的RMSE和DS。结果显示ICA-SVR在所有比例和两个数据集上都优于其他基准工具。
- Decision: 文章以提升金融时间序列预测的客观误差（RMSE/NMSE/MAD）和方向准确率（DS/CP/CD）为唯一核心目标与贡献，所有成功指标均为客观可计算数值，不依赖主观评价；全文在Robustness evaluation部分明确使用'benchmarking tools'一词，将random walk和SVR作为基准工具进行比较，该比较位于实验评价部分且直接支撑核心提升主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.95

## From predictive to prescriptive analytics: A data-driven multi-item newsvendor model

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113340
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "需求预测误差", "measurement_cn": "基于真实零售点销售数据，计算ME、MAE、RMSE、MAPE、相对误差和FVA分析", "objectivity_reason_cn": "值由实际销售额与预测值的差异直接计算，不依赖人的感受或语义评价"}, {"name_cn": "库存总成本/平均库存成本", "measurement_cn": "根据订货量、实际需求、缺货/持有成本参数计算期望库存成本，并比较不同方法", "objectivity_reason_cn": "库存成本由可审计的成本参数和实际需求数据决定，是客观可测的经济结果"}, {"name_cn": "多物品容量约束下的最优订货量", "measurement_cn": "通过所提启发式和产品层级历史比例计算各产品订货量，并在容量约束内求得", "objectivity_reason_cn": "订货量是决策输出，通过公式和实际数据计算，不涉及主观评价"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在真实零售数据集上，对所提QR-ML（尤其QR-RF、QR-DNN）进行系统化基准评价：需求估计部分与s-naïve、ETS、ARIMA、ARIMAx、FNN、RF、DNN对比MAE、RMSE、MAPE、相对误差和FVA；库存优化部分与Gallego-Moon max-min分布自由模型和正态经验模型对比库存成本。结果显示所提方法在多数场景下误差和库存成本更低。结论中的核心改进主张依赖这些benchmark对比结果。
- Decision: 本文核心目标是提升完全客观的预测误差和库存成本指标，全文评价和贡献声明均围绕该目标，不存在主观构念或并列的非客观核心目标；同时作者明确使用benchmark/benchmarking表述，在真实零售数据上将所提方法与传统时间序列、机器学习和多种库存优化方法进行系统比较，结果作为核心改进主张的关键证据。客观指标和benchmark两个模块均通过。
- Confidence: 0.95

## Geo-semantic-parsing: AI-powered geoparsing by traversing semantic knowledge graphs

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113346
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "F1分数", "measurement_cn": "将GSP预测的坐标与NEEL16数据集中人工标注的真实坐标进行比较，距离小于50 km（阈值T）计为正确，统计TP/FP/FN后计算F1。", "objectivity_reason_cn": "坐标匹配与否是可审计的地理事实，不依赖人的感受或语义判断；ground truth为坐标，评估规则标准化。"}, {"name_cn": "精确率 (Precision)", "measurement_cn": "在相同的地理距离阈值下，计算预测正确的坐标占所有预测坐标的比例。", "objectivity_reason_cn": "基于TP/FP的客观计数，由坐标匹配确定。"}, {"name_cn": "召回率 (Recall)", "measurement_cn": "在相同的地理距离阈值下，计算预测正确的坐标占所有真实标注坐标的比例。", "objectivity_reason_cn": "基于TP/FN的客观计数，由坐标匹配确定。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: NEEL16 (2016 Named entity recognition and linking challenge)
- Benchmark evaluation: 在NEEL16基准数据集上，GSP与2个基线（Naïve geoparser、NER+geocoder）和3个现有技术（Middleton et al., Halterman, 以及作者之前的Avvenuti et al.）进行对比，报告precision/recall/F1（Table 2）。GSP取得F1=0.665，显著优于所有其他技术（F1≤0.553）。
- Decision: 本文的核心目标是提升完全客观的geoparsing指标（precision/recall/F1），没有主观指标或并列的理论/组织贡献；评价在命名的公开基准数据集NEEL16上进行，并与多个baseline和SOTA方法比较，benchmark评价直接支撑核心提升主张。因此strict_include=true。
- Confidence: 0.95

## Intelligent trading of seasonal effects: A decision support algorithm based on reinforcement learning

- Year/journal: 2014 / Decision Support Systems
- DOI: 10.1016/j.dss.2014.04.011
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "累计收益 / 年化收益", "measurement_cn": "在2000-2012年DAX和S&P 500真实历史价格上，按交易日事件执行多空、杠杆和持仓期组合，以收盘价进出，根据模拟交易日志计算累计收益和年化收益。", "objectivity_reason_cn": "收益由市场价格、交易规则和系统日志确定，不依赖人的感受、语义评价或价值判断。"}, {"name_cn": "最大回撤", "measurement_cn": "基于模拟交易权益曲线计算的最大峰谷跌幅，作为风险指标。", "objectivity_reason_cn": "由客观价格序列和交易结果计算，属于可审计的财务/技术指标。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在DAX（243个交易事件）和S&P 500（314个交易事件）的2000-2012真实行情上，以未过滤的季节性静态策略作为benchmark，同时给出buy-and-hold作为参照；比较RL过滤后best/average/worst情形的return、annualized return和max drawdown。表6显示DAX平均收益从106.64%提升到173.14%，最大回撤从22.35%降至14.32%；表7显示S&P 500最佳收益从63.11%提升到133.99%，最大回撤下降。该benchmark评价直接支撑RL过滤提升收益/风险比的核心主张。
- Decision: 全文核心目标是提升完全客观的交易绩效指标（收益、年化收益、最大回撤），不存在主观构念或并列核心目标；结果部分明确使用'benchmark'一词，以未过滤的静态季节性策略为基准，并对比buy-and-hold和RL各情形，benchmark结果直接支撑核心提升主张。因此strict_include=true。
- Confidence: 0.95

## Making words work: Using financial text as a predictor of financial events

- Year/journal: 2010 / Decision Support Systems
- DOI: 10.1016/j.dss.2010.07.012
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "分类准确率 (accuracy)", "measurement_cn": "使用SVM对MD&A文本生成的token向量进行留一法交叉验证，计算破产/欺诈公司与对照公司的正确分类比例", "objectivity_reason_cn": "破产和欺诈是客观事实标签（SEC/Compustat等可核验来源），预测结果可审计，准确率可通过分类结果直接计算，不依赖人类的感受、意义理解或价值判断。"}, {"name_cn": "Type I / Type II 错误率", "measurement_cn": "在留一法交叉验证中统计事件公司被误分类为非事件（Type I）和非事件被误分类为事件（Type II）的比例", "objectivity_reason_cn": "错误率基于客观事实标签和确定性的分类输出，计算方式明确且可复现。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在自建的破产数据集（78对）和欺诈数据集（61对）上，将所提出的文本方法（MD&A文本生成的token向量+SVM）与经典的定量模型Altman（1968）Z-score（破产）和Beneish（1999）比率（欺诈）进行基准比较，使用留一法交叉验证报告准确率和错误率；同时测试文本与定量变量的组合效果。结果显示文本单独优于或接近定量方法（破产80% vs 66.67%，欺诈75.41% vs 40.16%），组合后达到最优（83.87%和81.97%），从而支撑了文本信息具有预测价值且与定量信息互补的核心主张。
- Decision: 客观指标方面，文章的预测目标是破产和欺诈两个完全客观的事实状态，评价指标为分类准确率和错误率，均为确定性计算；全文核心研究问题、设计目标、评价结构（留一法交叉验证、替代/互补测试）和贡献声明均围绕提升预测性能展开，不存在主观成功标准或并列核心目标。benchmark方面，引言明确使用'As a benchmark'陈述将文本方法与传统定量预测方法比较，并在4.4节实施该基准评价，比较对象包括Altman（1968）Z-score和Beneish（1999）比率等经典模型，结果明确展示文本方法的提升及组合数据的互补优势，该基准比较直接支撑了'文本信息可预测财务事件且补充定量信息'的核心主张。因此两个模块均通过，strict_include为true。
- Confidence: 0.95

## Nearest-neighbor-based approach to time-series classification

- Year/journal: 2012 / Decision Support Systems
- DOI: 10.1016/j.dss.2011.12.014
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "漏检率 (miss rate / 假阴性率)", "measurement_cn": "测试集中未被正确检测为流失者的实际流失者所占比例；流失标签依据电信公司记录的预测期内是否主动断线确定。", "objectivity_reason_cn": "流失状态是外部可核验事实，漏检率由预测结果与实际标签比对得到，不依赖人类感受、意义理解或价值判断。"}, {"name_cn": "误报率 (false alarm rate / 假阳性率)", "measurement_cn": "测试集中被错误预测为流失者的非流失者占实际非流失者比例；同样基于客观电信记录标签。", "objectivity_reason_cn": "指标基于客观事实标签和确定性的分类结果计算，无主观评价成分。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在台湾电信公司实际流失预测数据集上，将提出的 kNN-TSC（voting、weighted voting、stratified average 三种决策组合）与统计转换方法（C4.5）在 miss rate 和 false alarm rate 上比较；表2显示 kNN-TSC 总体优于 benchmark，支撑摘要和结论中的核心提升主张。
- Decision: 本文提出并评估 kNN-TSC 时间序列分类技术，核心目标是在流失预测场景中降低漏检率与误报率；两个指标均基于客观事实标签（是否在预测期断线）可直接计算，不涉及主观评价。全文在实证部分有明确的 performance benchmark 表述（第4.3节），将所提方法与统计转换方法（C4.5）作为基准比较，表2结果直接支撑了摘要和结论中关于性能提升的核心主张。因此同时满足完全客观指标、唯一核心目标和明确 benchmark 表述的全部条件。
- Confidence: 0.95

## Neural network earnings per share forecasting models: A comparison of backward propagation and the genetic algorithm

- Year/journal: 2009 / Decision Support Systems
- DOI: 10.1016/j.dss.2008.12.011
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "平均绝对百分比误差（MAPE）", "measurement_cn": "基于 Compustat 每股收益（EPS）实际值，按公式 MAPE = (1/10) Σ |Y_t − Ŷ_t| / |Y_t| 计算；每个滚动样本使用前30个季度估计模型，下一季度做一步前瞻预测，共10次预测。", "objectivity_reason_cn": "EPS 是外部可核验的会计事实；预测误差由固定公式直接计算，不依赖人的感受、语义判断或质量评价。"}, {"name_cn": "均方误差（MSE）", "measurement_cn": "基于同一组一步前瞻预测，按 MSE = (1/10) Σ ((Y_t − Ŷ_t) / Y_t)^2 计算；EPS 来自 Compustat。", "objectivity_reason_cn": "预测值与实际会计数据之差经确定公式计算；核心构念和数值均可脱离人类主观体验独立成立。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 将遗传算法估计的神经网络模型（UGA、MGA）与 ULM.1-ULM.4、MLM.1-MLM.2、BP 估计的神经网络（UBP、MBP）以及扩展线性模型（RULM、RMLM）在相同 Compustat EPS 数据上比较一步前瞻预测精度；表4-表7报告 MAPE、MSE、大误差比例及 Friedman 检验排名，结果显示 GA 模型精度显著更优。
- Decision: 客观指标：EPS 预测误差（MAPE/MSE）是对外部会计事实的确定性预测误差，完全客观；核心目标：全文唯一核心是证明用遗传算法估计神经网络权重可显著提升 EPS 预测精度，没有并列的主观或理论性核心贡献；benchmark：文章虽未使用公开命名数据集，但在评价设计中明确以 ULM/MLM 等模型作为 benchmarks，并将 GA 模型与 BP、线性基准等显式参照比较，benchmark 结果是核心提升主张的关键证据。因此 strict_include=true。
- Confidence: 0.95

## Object typicality for effective Web of Things recommendations

- Year/journal: 2014 / Decision Support Systems
- DOI: 10.1016/j.dss.2013.09.008
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "平均绝对误差（MAE）", "measurement_cn": "在 MovieLens 和 Netflix 测试集上，比较系统预测评分与实际用户评分的平均绝对差；采用 5 折交叉验证。", "objectivity_reason_cn": "MAE 由预测数值与数据集中的实际评分直接计算，结果可由系统输出和日志数据复核，不依赖研究者的主观判断或用户满意度评价。"}, {"name_cn": "均方根误差（RMSE）", "measurement_cn": "对预测评分与实际用户评分的误差平方后取平均再开方，用于放大并评估大误差预测。", "objectivity_reason_cn": "RMSE 同样是基于记录的用户评分与系统输出的确定数值计算，计算公式客观，结果可审计。"}, {"name_cn": "大误差预测分布（PE distribution）", "measurement_cn": "统计预测评分与实际评分之间误差为 0、1、2、3、4 的预测比例，特别比较 PE=4 的大误差比例。", "objectivity_reason_cn": "该指标是预测评分离散误差的频次统计，来自可审计的预测输出与真实评分记录。"}, {"name_cn": "推荐时间（计算效率）", "measurement_cn": "比较各推荐系统在相同训练/测试划分下的推荐阶段耗时，例如在 x=0.9 条件下的推荐时间。", "objectivity_reason_cn": "推荐时间为可测的系统运行耗时，属于物理/技术性可观测指标，不依赖人类体验评估。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: MovieLens | Netflix
- Benchmark evaluation: 在 MovieLens（100,000 ratings, 943 users, 1682 movies，实验中用其子集）和 Netflix（100,480,507 ratings 子集）两个公开基准数据集上评价 ROT。第一组实验与 CB、UBCF、IBCF、Naive Hybrid、EMDP 等经典基线比较 MAE/RMSE、大误差比例和推荐时间；第二组实验与 SCBPCC、WLR、CBT、SVD、SVD++、SocialMF 等 state-of-the-art 方法比较 MAE/RMSE。结果表明 ROT 在 MovieLens 和 Netflix 上显著优于多数基线，尤其在 MAE 上。
- Decision: 文章核心目标是设计和评估 ROT 推荐方法，以提升推荐准确度、降低大误差并提高计算效率；所有主要成功指标均为可审计的客观数值：MAE、RMSE、大误差分布和推荐耗时。研究问题、实验设计和结论均围绕这些客观指标展开，未将主观满意度、用户感知质量或理论机制贡献作为并列核心目标。全文在摘要、评价数据选择、实验讨论和结论中多次明确采用 MovieLens 和 Netflix 公共 benchmark 数据集，并在这些数据集上与多项基线和 state-of-the-art 方法比较，benchmark 结果是支持核心性能提升主张的关键证据。因此同时满足客观指标唯一核心目标和明确 benchmark 表述的门槛，strict_include 为 true。
- Confidence: 0.95

## On the brink: Predicting business failure with mobile location-based checkins

- Year/journal: 2015 / Decision Support Systems
- DOI: 10.1016/j.dss.2015.04.010
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "误分类率 (Misclassification Rate)", "measurement_cn": "基于混淆矩阵计算：错误分类数/总分类数，在186家留出样本上评估", "objectivity_reason_cn": "由预测类别与客观定义的失败标签（三个月内日均checkin少于1次）比对得出，不依赖人的感受或语义判断"}, {"name_cn": "平均绝对偏差 (MAD)", "measurement_cn": "预测概率与实际0/1标签绝对偏差的平均值，分样本内和样本外计算", "objectivity_reason_cn": "基于固定标签和模型输出的数值计算，完全可审计"}, {"name_cn": "AIC", "measurement_cn": "根据似然函数和参数个数计算的模型拟合指标", "objectivity_reason_cn": "由数据似然和模型复杂度客观计算"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在自建的纽约市686家餐厅数据上，将仅含业务特征的Logit基准模型与逐步加入focal restaurant和邻居checkin变量的模型进行比较，报告in-sample/out-of-sample MAD和误分类率。结果显示加入checkin变量后MAD从0.153降至0.056，误分类率从0.134降至0.055，提升显著。
- Decision: 客观指标：核心结果指标是预测误分类率、MAD、AIC，这些均基于客观可观测的checkin记录和固定失败定义，不依赖人类感受或语义评价；预测对象是外部可核验的虚拟死亡标签。唯一核心目标：研究问题、设计目标、评价结构和贡献声明均围绕“使用LBS checkin数据提升业务失败预测准确性”展开，无主观量表或并列核心贡献。Benchmark：4.2节明确使用“benchmark model”一词，将仅含业务特征的模型作为基准，并在评价语境中与加入checkin变量的模型比较，benchmark结果直接支撑核心预测提升主张，且有明确参照点。故两个模块均通过，strict_include=true。
- Confidence: 0.95

## Pairwise issue modeling for negotiation counteroffer prediction using neural networks

- Year/journal: 2011 / Decision Support Systems
- DOI: 10.1016/j.dss.2010.11.002
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "反报价预测误差（按议题序数层级缩放的MAE百分比）", "measurement_cn": "使用Inspire系统Cypress/Itex谈判案例的真实谈判日志数据，将下一反报价的实际值与模型预测值比较，计算平均绝对误差（MAE），并按各议题的离散等级数缩放为百分比误差。", "objectivity_reason_cn": "反报价数值和误差可以直接从系统谈判日志中确定性地观测和复算，不依赖任何人的感受、意义理解或价值判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在Inspire的Cypress/Itex谈判数据集上，将pairwise ANN（NNP）与naïve模型、全议题ANN（NNF）和线性pairwise模型（MLRP）作为基准进行比较，报告按议题等级缩放的MAE百分比，并用t检验检验假设。结果显示NNP总体误差9.25%，低于naïve（12.08%）和MLRP（10.67%），且不高于NNF（9.37%）；对排除议题的新议题预测误差9.46%，仍低于naïve（12.08%）。
- Decision: 客观指标与唯一核心目标通过：核心目标是构建灵活的反报价预测模型，成功指标为真实谈判数据上的预测误差，测量完全来自系统日志和可复算的MAE，无主观量表或人类语义评价。Benchmark通过：作者在第3节和第5.2节明确使用benchmark指代naïve、全议题ANN和线性pairwise参照模型，并在第6节用这些基准比较检验核心预测误差假设，且均有明确对照。因此strict_include=true。
- Confidence: 0.95

## PhishWHO: Phishing webpage detection via identity keywords extraction and target domain name finder

- Year/journal: 2016 / Decision Support Systems
- DOI: 10.1016/j.dss.2016.05.005
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "钓鱼网页检测性能：TPR、FPR、TNR、FNR、Accuracy、MCC", "measurement_cn": "在下载的5000个钓鱼网页（来自PhishTank/OpenPhish）和5000个合法网页（来自Alexa top one million）上，将PhishWHO预测的钓鱼/合法标签与数据源提供的真实类别标签比较，计算TPR、FPR、TNR、FNR、Accuracy和MCC。", "objectivity_reason_cn": "网页是否为钓鱼网页是可外部核验的事实状态，标签来自PhishTank/OpenPhish/Alexa等公开来源；检测结果的统计指标由分类预测与事实标签逐项比对确定，不依赖人的感受、价值或语义质量判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 作者在实验II中将PhishWHO与两种采用类似分析技术的传统方法M1（基于文本的CANTINA类方法[25]）和M2（基于身份的方法[20]）比较；在实验III中将PhishWHO与基于特征的搜索引擎方法M3 [12]比较。比较指标包括TPR、FPR、TNR、FNR、Accuracy和MCC。结果显示PhishWHO在TPR和MCC上优于M1/M2/M3，并用这些结果支持“PhishWHO outperforms conventional methods”的核心主张。数据集来自PhishTank/OpenPhish（钓鱼样本）和Alexa（合法样本），虽然不是公开命名benchmark套件，但作者明确用benchmarking表述在评价语境中完成系统化基准比较。
- Decision: 客观指标方面：核心成功指标是钓鱼网页检测的TPR/FPR/TNR/FNR/Accuracy/MCC，这些是基于PhishTank/OpenPhish/Alexa事实标签计算的分类性能，完全客观且可审计；全文没有主观量表或语义质量评价作为核心结果。唯一核心目标方面：研究问题、方法设计、实验评价和贡献声明均围绕客观检测性能提升展开，没有并列的理论、制度或行为解释贡献。Benchmark方面：作者在实验III中明确使用“benchmarked against”陈述系统化基准比较，并在实验II/III中将PhishWHO与M1、M2、M3等明确参照方法比较，比较结果直接支持核心提升主张。因此两项门槛均通过，strict_include为true。
- Confidence: 0.95

## Predicting corporate bankruptcy using a self-organizing map: An empirical study to improve the forecasting horizon of a financial failure model

- Year/journal: 2011 / Decision Support Systems
- DOI: 10.1016/j.dss.2011.04.001
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "企业破产预测正确分类率", "measurement_cn": "使用法国Diane数据库中的测试样本（440家破产企业和440家健康企业），根据企业是否在2004年发生法律清算或重组作为事实标签，计算判别分析、逻辑回归、神经网络、Cox模型和轨迹模型在破产前1年、2年、3年的正确分类率，并进行比例差异显著性检验。", "objectivity_reason_cn": "破产状态是法律上可审计的事实标签，不依赖人的感受、意义理解或价值判断；正确分类率由确定性匹配计算得出，属于客观预测性能指标。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在法国企业破产测试样本上，将所提出的轨迹模型与判别分析、逻辑回归、神经网络和Cox比例风险模型四个基准方法进行比较，报告了破产前1、2、3年的正确分类率（表8），并给出统计显著性检验（表9、11）。结果显示轨迹模型在多期视界上正确分类率下降更小，尤其3年视界显著优于其他方法。
- Decision: 该文以提升破产预测在1至3年视界上的正确分类率为唯一核心目标和贡献，该指标基于法律破产事实标签的确定性分类，属于客观固定事实标签预测性能。全文存在明确的benchmark表述：第3.3.2节标题'Methods used as benchmark'，并将判别分析、逻辑回归、神经网络和Cox模型作为基准方法，在测试样本上系统比较，结果用于支撑轨迹模型预测稳定性的核心改进主张；比较具有明确参照点并附统计检验。因此两模块均通过，strict_include为true。
- Confidence: 0.95

## Predicting donation behavior: Acquisition modeling in the nonprofit sector using Facebook data

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113446
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "AUC（ROC曲线下面积）", "measurement_cn": "基于5x2交叉验证，对每次测试集根据预测得分和实际捐赠标签计算AUC；实际捐赠标签由非营利组织内部捐赠者数据库匹配确定。", "objectivity_reason_cn": "捐赠状态为可审计的事实标签，AUC由确定性算法从预测分数与事实标签计算，不依赖人类感受或语义评价。"}, {"name_cn": "Top Decile Lift（十分位提升度）", "measurement_cn": "在5x2交叉验证测试集中，取预测得分最高的10%样本，计算其中捐赠者比例与整体捐赠者比例的比值。", "objectivity_reason_cn": "基于实际捐赠记录和模型预测排名的客观计算，不包含主观判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 作者在自有Facebook粉丝数据集上，系统比较3种降维技术（SVD、NMF、LDA）与7种分类算法（LR、KNN、BT、RF、AB、XGB、NN）以及Binary baseline，使用5x2交叉验证，以AUC和TDL为评价指标，得出SVD+LR最优（AUC=0.72，TDL=3.33），并与文献中现有获取模型性能进行比较。
- Decision: 客观指标方面：核心目标是提升预测捐赠行为的客观性能（AUC、TDL），基于非营利组织内部捐赠数据库的实际捐赠标签，不依赖人类感知或语义评价；全文围绕预测模型构建、方法比较和特征重要性评价展开，客观指标提升是唯一核心目标。benchmark方面：作者明确使用“benchmark”一词陈述系统化的基准评价（比较3种DR技术×7种分类算法及binary baseline），该benchmark评价位于评价语境，结果SVD+LR的AUC=0.72、TDL=3.33用于支持核心提升主张，并有明确参照点（baseline、其他方法、文献数据）。因此两模块均通过，strict_include=true。
- Confidence: 0.95

## Preserving User Preferences in Automated Document-Category Management: An Evolution-Based Approach

- Year/journal: 2009 / Journal of Management Information Systems
- DOI: 10.2753/mis0742-1222250404
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "聚类召回率（Cluster Recall）", "measurement_cn": "正确文档对关联数（CA）除以真实类别中的文档对关联数（TA），即 CR=|CA|/|TA|；文档对是否在同一类别由真实类别标签和生成聚类决定。", "objectivity_reason_cn": "基于文档外部事实标签（Reuters/ACM 的原始类别）的确定性计算，不依赖任何人的主观评价或语义质量判断。"}, {"name_cn": "聚类精确率（Cluster Precision）", "measurement_cn": "正确文档对关联数（CA）除以生成聚类的文档对关联数（GA），即 CP=|CA|/|GA|。", "objectivity_reason_cn": "同样基于外部事实标签的确定性集合运算，客观可审计。"}, {"name_cn": "F1测度", "measurement_cn": "由 CR 和 CP 计算的调和平均数：F1=(2*CR*CP)/(CR+CP)，并在每个阈值下取最高值。", "objectivity_reason_cn": "是 CR/CP 的派生客观指标，用于统计检验。"}, {"name_cn": "结构相似性（Structure Similarity）", "measurement_cn": "在层层次结构场景中，基于文档对在真实层次与生成层次中的路径匹配程度计算，SS = 平均路径相似度。", "objectivity_reason_cn": "基于层次结构的路径字符串比较，确定性计算，不涉及主观评分。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: Reuters-21578 | ACM Digital Library corpus
- Benchmark evaluation: 在 Reuters-21578 和 ACM 摘要语料库上，通过 Gaussian-3 到 Gaussian-6 分布创建 30 组合成的类别演化场景；对 CE2 与 CE、HAC 比较，对 CHE 与 HAC+P 比较；报告 PRT 曲线、最高 F1 值、p 值，并针对 CHE 额外比较结构相似性。结果整体显示 CE2/CHE 在多数场景下显著优于各自基准。
- Decision: 核心指标（聚类召回率、聚类精确率、F1、结构相似性）均基于 Reuters/ACM 外部文档类别标签的确定性计算，不依赖人类主观评价或语义质量判断，属于客观固定事实标签上的性能提升；研究问题、设计与贡献声明都围绕 CE2/CHE 在文档类别重组中的客观有效性，不存在并列的主观或理论核心目标，符合唯一核心目标要求。全文多次明确使用 benchmark/performance benchmark 指称 CE、HAC、HAC+P 等对照技术，并在评价语境中报告比较结果，这些 benchmark 评价正是支撑核心提升主张的关键证据，且具有明确参照点与统计检验。因此 strict_include=true。
- Confidence: 0.95

## Principal component case-based reasoning ensemble for business failure prediction

- Year/journal: 2011 / Information & Management
- DOI: 10.1016/j.im.2011.05.001
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "总体预测准确率（total predictive accuracy）", "measurement_cn": "在随机划分的训练/测试集上，由PC-CBR-E预测企业是否ST/失败，并与真实ST状态比较计算正确率；重复50次随机划分后报告均值、标准差、中位数、最大值、最小值，并用单尾t检验比较。", "objectivity_reason_cn": "业务失败标签由中国证券市场ST状态等客观财务事实定义，不依赖人的感受或语义评价；预测准确率可由分类结果与事实标签确定性计算。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在作者自构建的中国短期和中期BFP数据集上，将PC-CBR-E与明确的benchmark方法（M-MDA、M-Logit、M-ECBR、M-MCBR）及最优基PC-CBR进行比较，报告平均预测准确率、标准差等统计量，并通过单尾显著性检验证明PC-CBR-E显著优于这些基准。
- Decision: 客观指标：研究唯一核心指标是BFP的总体预测准确率，标签为ST/非ST等客观事实，所有核心评价均为准确率和显著性检验，无主观构念或人类语义评价。唯一核心目标：研究问题、假设、实验设计和贡献声明均围绕提升CBR预测准确率，无并列核心贡献。Benchmark：第4.3节明确使用'benchmark methods'和'benchmarking purposes'表述，将MDA、Logit、ECBR、MCBR及最优基模型作为比较基准，并在实验结果中通过准确率统计和显著性检验支撑核心提升主张。因此满足全部纳入条件。
- Confidence: 0.95

## Proactive Resource Request for Disaster Response: A Deep Learning-Based Optimization Model

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2022.0125
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "平均单位需求剥夺成本", "measurement_cn": "根据每个单位需求的延迟时间δ，通过剥夺成本公式 e^(φ + b·c_k·δ) - e^φ (式36) 计算，再对所有单位需求求平均。δ由需求时间与满足时间的差异确定，φ、b取自Holguín-Veras et al. (2013)，c_k为资源类型重要性分数。", "objectivity_reason_cn": "构念为满足需求的时间延迟带来的经济成本，其数值基于可审计的时间戳（需求时间、满足时间）和事先定义的确定性公式计算，不依赖任何人关于质量、价值、偏好或感受的评价。c_k虽由研究者设定，但只是成本函数的权重参数，不是核心结果本身的主观构念。"}, {"name_cn": "平均单位需求时间延迟", "measurement_cn": "在滚动评估流程中记录每个单位需求从需求时间到满足时间的时长（小时），再对所有单位需求求平均。", "objectivity_reason_cn": "时间延迟是直接可观察、可验证的物理/操作事实，来自系统时序和资源到达记录，不涉及人类主观判断。"}, {"name_cn": "未来需求满足百分比", "measurement_cn": "在资源请求时间T到资源到达时间T+之间到达的未来需求中，被主动请求并在T+得到满足的需求比例，基于资源请求和需求事件时间记录计算。", "objectivity_reason_cn": "该指标基于需求到达事件和资源分配结果这些客观可审计事实，不依赖主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在2021年中国河南洪水真实场景数据（来自3,496条微博帖子，识别出860条资源需求）上，以7月21-23日为训练数据、滚动请求至7月27日，评估CNM-PRR与ReR、logNormMix-PRR、A-NDTT-PRR、AttnMC-PRR、CTDRP-PRR、LR-NV、DL-NV、logNormMix-IFCFS等基准方法。结果显示CNM-PRR的平均单位剥夺成本为25.69美元，优于最佳基准A-NDTT-PRR 15.15%；平均时间延迟7.42小时，优于所有基准9.74%-62.11%；未来需求满足百分比0.80，优于最佳基准A-NDTT-PRR 8.55%。后续还进行消融分析（表7）和多利益相关者仿真（表8）进一步比较。
- Decision: 客观指标方面：核心指标为平均单位需求剥夺成本、平均时间延迟、未来需求满足百分比（以及多目标仿真中的填充率和公平性标准差），这些指标均由可审计的时间戳、资源分配记录和确定性公式计算，不依赖任何人对质量、价值、偏好或感受的评判，属于完全客观的直接指标。唯一核心目标方面：论文的研究问题、方法设计和贡献声明均围绕“最小化延迟满足需求的成本”这一客观改进目标展开，新问题、新TPP模型和优化算法是服务于该目标的组成贡献，未发现并列的主观体验、理论机制或其他非客观核心目标。Benchmark方面：在Section 5.2明确使用benchmark/benchmarking陈述基准比较，并在Section 5.3和5.4中以真实数据和仿真数据对多个现有方法（ReR、logNormMix-PRR、A-NDTT-PRR、AttnMC-PRR、CTDRP-PRR、LR-NV、DL-NV、logNormMix-IFCFS）进行比较，报告了显著的成本、时间延迟和需求满足率改进；benchmark评价直接支撑核心客观指标提升的主张。因此两个模块均通过，strict_include为true。
- Confidence: 0.95

## Simple decision forests for multi-relational classification

- Year/journal: 2013 / Decision Support Systems
- DOI: 10.1016/j.dss.2012.11.017
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "分类准确率 (Accuracy)", "measurement_cn": "在5个基准数据集上使用训练/验证/测试划分，统计正确预测类别占全部实例的比例。", "objectivity_reason_cn": "预测目标为数据库中可审计的类标签（贷款成败、肝炎类型、国家宗教、用户年龄分组、电影评分分组等），将预测输出与事实标签比对即可计算，不依赖人对结果质量的主观评价。"}, {"name_cn": "AUC", "measurement_cn": "对二元分类任务计算ROC曲线下面积。", "objectivity_reason_cn": "由预测概率排序和事实标签计算得到，数值确定可复现。"}, {"name_cn": "加权F值 (Weighted F-measure)", "measurement_cn": "按类先验加权的precision/recall调和平均。", "objectivity_reason_cn": "基于事实标签的混淆矩阵计算，不涉及人类主观评价。"}, {"name_cn": "学习/诱导时间 (Run time)", "measurement_cn": "记录算法完成模型诱导的秒数，如Table 1。", "objectivity_reason_cn": "系统日志中的可审计时间度量。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: Financial (PKDD CUP 1999) | Hepatitis (PKDD'02 Discovery Challenge) | Mondial | MovieLens (UCI) | JMDB (IMDB)
- Benchmark evaluation: 在Financial、Hepatitis、Mondial、MovieLens、JMDB五个基准数据集上评价简单决策森林（Normalized/Unnormalized/Naive）以及TILDE、FORF-NA、Graph-NB、TreeLiker-Relf/Poly等参照方法，报告Accuracy、AUC、F-measure和诱导时间。
- Decision: 全文以提升多关系分类的客观预测性能（Accuracy/AUC/F-measure）和学习时间为唯一核心目标；明确使用5个命名基准数据集，并在该评价场地上与TILDE、FORF-NA、Graph-NB、TreeLiker等多个参照方法比较，结果支持核心提升主张，因此严格纳入。
- Confidence: 0.95

## The Making of a Good Impression: Information Hiding in Ad Exchanges

- Year/journal: 2016 / MIS Quarterly
- DOI: 10.25300/misq/2016/40.3.10
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "广告交易平台每场拍卖的期望收益（expected revenue per auction）", "measurement_cn": "在二价密封拍卖中，广告交易平台从胜出者处获得的支付，即第二高出价值；通过理论公式（Rev^I、Rev^II）计算，或在数值模拟中通过生成估值矩阵、枚举策略并计算平均收益来测量。", "objectivity_reason_cn": "拍卖支付是可由拍卖规则和出价决定的可审计经济事实，不依赖人的感受、意义理解或价值判断，完全由模型与模拟数据决定。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在综合测试床（comprehensive test bed）上评价启发式信息隐藏策略：以最优策略（通过枚举决策空间得到的收益最大化策略）为基准，比较启发式策略与完全揭示、完全隐藏、等概率混合策略的期望收益；报告平均收益比值（如启发式/最优约为0.94-1，启发式/完全揭示约1-7.33）。
- Decision: 客观指标方面：核心构念为广告交易平台每场拍卖的期望收益，是可由拍卖规则和出价决定的客观经济量，不依赖主观判断；全文核心目标、评价和贡献均围绕该收益提升展开，无并列主观目标或其他核心贡献。Benchmark方面：作者在数值模拟部分明确使用 benchmark 一词，以最优策略为基准，在综合测试床上系统评价启发式及对比策略，结果用于证明启发式策略的收益提升（近最优且大幅优于完全揭示等策略），满足明确基准评价、处于评价语境、支撑核心主张且有明确参照点。因此两模块全部通过，strict_include 为 true。
- Confidence: 0.95

## The added value of Facebook friends data in event attendance prediction

- Year/journal: 2016 / Decision Support Systems
- DOI: 10.1016/j.dss.2015.11.003
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "AUC（ROC曲线下面积）", "measurement_cn": "基于模型输出的出席概率与用户真实出席/不出席标签计算ROC曲线下面积；结合5次2折交叉验证取中位数。", "objectivity_reason_cn": "出席与否是用户对事件的真实行为/事实性声明，不依赖人的感受或语义判断；AUC由分类器输出与客观二元标签计算，可审计、可复现。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 作者将baseline和augmented两个模型在五种分类算法（Logistic Regression、Random Forest、Adaboost、Neural Networks、Naive Bayes）上进行基准对比；评价场地为自建的Facebook事件出席数据，使用5×2交叉验证计算AUC，并通过Wilcoxon符号秩检验比较模型差异。基准结果用于证明加入friends数据能提升AUC，是核心主张的核心证据。
- Decision: 客观指标方面：核心成功指标AUC基于客观可观察的事件出席标签和分类器输出计算，不依赖主观感受或语义判断，所有核心成功结果均为客观指标。唯一核心目标方面：全文围绕friends data对AUC的增量提升展开，研究问题、评价设计和贡献声明均一致，未发现并行的主观、理论或机制核心贡献。Benchmark方面：作者明确使用benchmark一词描述对两个模型在五种分类算法上的系统基准比较；该基准比较是证明core improvement（AUC提升）的关键证据，且有明确参照点（baseline模型）。因此两个模块均通过，strict_include=true。
- Confidence: 0.95

## The enhancement of solving the distributed constraint satisfaction problem for cooperative supply chains using multi-agent systems

- Year/journal: 2008 / Decision Support Systems
- DOI: 10.1016/j.dss.2008.02.001
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "订单满足率（R_OF）", "measurement_cn": "模拟实验中成功履行订单数与总订单数的比值，由系统运行日志统计。", "objectivity_reason_cn": "基于确定性的订单履行结果计数，不依赖人的感受或语义评价。"}, {"name_cn": "平均订单履行周期（T_OF）", "measurement_cn": "所有成功履行订单的履行周期时间平均值，由模拟时间戳计算。", "objectivity_reason_cn": "时间是物理可测维度，由仿真事件记录确定。"}, {"name_cn": "平均在制品库存成本（C_WIP）", "measurement_cn": "所有成功履行订单的在制品库存成本平均值，由仿真库存成本规则计算。", "objectivity_reason_cn": "库存成本来自确定性成本核算规则和系统记录，不涉及主观感知。"}, {"name_cn": "平均成品库存成本（C_FP）", "measurement_cn": "所有成功履行订单的成品库存成本平均值，由仿真库存成本规则计算。", "objectivity_reason_cn": "库存成本来自确定性成本核算规则和系统记录，不涉及主观感知。"}, {"name_cn": "平均谈判轮数（NR）", "measurement_cn": "所有成功排程订单的累计谈判轮数平均值，由代理交互日志统计。", "objectivity_reason_cn": "谈判轮数是系统运行中的计数值，具有确定性。"}, {"name_cn": "平均计算时间（C_T）", "measurement_cn": "从接收订单到成功规划排程的总计算时间平均值，由系统计时。", "objectivity_reason_cn": "计算时间是可客观测量的物理量。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: COM（集中式优化机制） | DCSM（采用AWC的分布式协调机制）
- Benchmark evaluation: 在模拟的模具制造供应链（16家公司）环境中，将NegoGA与DCSM和COM三种机制进行系统比较。Experiment A在四种订单需求模式（A-1至A-4）下比较订单满足率、平均订单履行周期、WIP库存成本和成品库存成本；Experiment B在A-3动态需求环境下比较DCSM与NegoGA的谈判轮数和计算时间。结果表明NegoGA在多数动态环境下显著优于DCSM，并与集中式COM相比在真实场景中更具可行性。
- Decision: 客观指标方面，本文以订单满足率、履行周期、库存成本、谈判轮数和计算时间等系统日志型客观指标作为成功标准，没有主观量表或人类语义评价；核心目标方面，研究问题和贡献声明都围绕NegoGA提升分布式供应链排程绩效展开，未发现并列的核心理论、政策或主观贡献；benchmark方面，作者明确使用benchmark机制/基准机制表述，将COM和DCSM/AWC作为对照基准，在模拟供应链上系统比较并用于支撑NegoGA的性能提升主张，比较对象明确。因此两个模块均通过，strict_include为true。
- Confidence: 0.95

## The seaport service rate prediction system: Using drayage truck trajectory data to predict seaport service rates

- Year/journal: 2017 / Decision Support Systems
- DOI: 10.1016/j.dss.2016.11.008
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "港口服务时长（service rate），即集卡在港区完成提箱/卸箱作业的停留时长", "measurement_cn": "通过车辆GPS轨迹的地理围栏分析，记录每辆卡车进入和离开目标港区的时间戳，计算二者差值（分钟）；预测模型的性能用RMSE（实际服务时长与预测值之差的样本标准差）衡量。", "objectivity_reason_cn": "服务时长是由GPS时间戳和地理围栏边界确定的物理时间间隔，不依赖人类感受、意义理解或价值判断；RMSE是客观预测误差。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在Port of Rotterdam三个匿名码头（CTA、CTE、CTH）和两种数据更新率（15分钟、7.5分钟）上，构建六种梯度提升模型（GBM0-5）与六种普通线性基准模型（LM0-5），在相同目标和预测变量对下以RMSE比较。GBM在多数设置下RMSE低于LM，例如CTA 15分钟数据测试集GBM5=10.51 vs LM5=11.16，CTH 7.5分钟测试集GBM5=17.26 vs LM5=18.77，支撑“梯度提升模型提供更好预测”的核心主张。
- Decision: 客观指标方面：核心指标是基于GPS轨迹计算的港口服务时长（分钟）和预测RMSE，均为物理事实/可审计技术指标，不涉及主观评价。唯一核心目标方面：研究的目标、模型构建、评价和贡献声明都围绕提升服务时长预测精度，未发现并列的理论、主观或非客观核心贡献。Benchmark方面：作者在第4.2节明确将线性模型作为基准（benchmarks），在第5.3节报告GBM与线性基准的比较并得出GBM预测更优，benchmark评价直接支撑核心改进主张，且具有明确参照点。因此满足全部纳入条件，strict_include=true。
- Confidence: 0.95

## Top Persuader Prediction for Social Networks1

- Year/journal: 2018 / MIS Quarterly
- DOI: 10.25300/misq/2018/13211
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "Top-K Precision", "measurement_cn": "预测的Top-K说服者与第二段10周数据中按说服信用识别出的Top-K说服者的交集大小除以K。", "objectivity_reason_cn": "基于系统日志中的实际采纳行为（虚拟物品购买、手机服务订阅）和固定信用分配规则计算，不依赖人的感受或语义评价。"}, {"name_cn": "Spearman等级相关系数", "measurement_cn": "预测排序与按说服信用计算的排序之间的Spearman相关系数。", "objectivity_reason_cn": "由客观排序数值计算，反映两个排序的一致性，不含主观判断。"}, {"name_cn": "总说服信用", "measurement_cn": "预测出的Top-K说服者的说服信用之和；说服信用按固定规则从后续采纳行为中分配。", "objectivity_reason_cn": "直接来自可审计的采纳行为日志和公开算法式定义，无主观评分成分。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在真实世界社交网络（游戏avatar网络和手机通话网络）上，以多个中心度方法、PageRank类方法、INF-SIM和随机选择为基准，比较top-K precision、Spearman系数和总说服信用；结果显示所提方法在所有指标上显著优于基准方法，且在不同γ和K值下稳健。
- Decision: 客观指标方面，核心成功指标为top-K precision、Spearman系数和总说服信用，均由实际采纳行为日志和固定规则计算，不依赖主观感知或语义评价；预测top persuaders和提升客观预测精度是全文唯一核心目标与贡献。Benchmark方面，文章在真实数据上以多种既有方法为基准，明确使用benchmark/benchmarked表述进行系统化比较，且比较结果直接支撑核心提升主张，满足benchmark_comparison_central。因此两个模块均通过，strict_include=true。
- Confidence: 0.95

## Trading team composition for the intraday multistock market

- Year/journal: 2013 / Decision Support Systems
- DOI: 10.1016/j.dss.2012.09.009
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "日均利润/年化利润", "measurement_cn": "根据交易策略在测试期的每日实际交易回报计算，日均利润取平均，年化利润由日均利润外推得到", "objectivity_reason_cn": "利润是客观可审计的财务结果，不依赖人的感受、语义或价值判断"}, {"name_cn": "风险指标（最大回撤、Ulcer Index）", "measurement_cn": "基于每日利润序列计算最大回撤和Ulcer指数", "objectivity_reason_cn": "这些指标由价格和利润序列确定性计算，独立于人类感知"}, {"name_cn": "收益风险比率（Sharpe、Martin、Calmar、Sterling、Burke）", "measurement_cn": "基于利润序列和风险指标计算标准金融比率", "objectivity_reason_cn": "财务绩效比率，计算规则明确客观"}, {"name_cn": "交易执行指标（盈利交易、亏损交易、交易次数、盈亏比）", "measurement_cn": "从实际交易记录中统计", "objectivity_reason_cn": "交易记录是可审计事实"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在十二只BM&FBovespa股票的测试数据集上，将提出的MSR策略与基线策略BLS进行系统比较，报告日均利润、年化利润、最大回撤、Ulcer Index、Sharpe/Martin/Calmar/Sterling/Burke比率以及交易统计，并展示统计显著性检验。
- Decision: 该文章以提升完全客观的交易绩效指标（利润、风险、收益风险比）为唯一核心目标与贡献；全文有明确的benchmark表述（BLS作为informative benchmark，Benchmark Results一节），并在该基准上与明确基线比较，支撑核心利润提升主张。因此两个模块均通过，strict_include为true。
- Confidence: 0.95

## Trustworthy and profit: A new value-based neighbor selection method in recommender systems under shilling attacks

- Year/journal: 2019 / Decision Support Systems
- DOI: 10.1016/j.dss.2019.113112
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "MAE（平均绝对误差）", "measurement_cn": "在Book-Crossing数据子集上模拟多种shilling攻击场景，计算预测评分与实际评分之差的绝对值均值（Eq.8）。", "objectivity_reason_cn": "评分是数据中已有的外部事实，MAE由预测值与实际值的确定算术差计算，不依赖任何人的主观评价。"}, {"name_cn": "MSEP（平均相似性期望利润）与MTP（平均总利润）", "measurement_cn": "根据项目利润（价格减估计成本）和预测偏好似然计算SEP（Eq.6），再平均至每个测试用户；MTP进一步统计Top-K推荐项目的利润总和。", "objectivity_reason_cn": "价格、成本、评分和推荐列表均为可审计数据，利润计算遵循明确公式，不依赖用户感受或语义判断。"}, {"name_cn": "Precision、Recall、F1", "measurement_cn": "将原始评分10视为“喜欢”，其余为“不喜欢”，比较推荐列表与实际偏好，按Eq.(10)-(12)计算。", "objectivity_reason_cn": "该二分类基于预先固定的评分阈值，标签和匹配都是确定性计算；虽然阈值选择带有研究者设定，但标签本身不依赖人类体验或价值判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在一个Book-Crossing数据子集上，模拟Random、Average、Bandwagon(AFM/RFM)以及混合攻击，用PCC、SD和HPRS(+SD)作为基准，比较VNS在MAE、MSEP、MTP、Precision、Recall和F1上的表现。结果显示VNS在绝大多数攻击场景下MAE更低、MSEP更高，且在准确度指标上显著优于HPRS+SD，MTP优于PCC和SD而低于HPRS+SD，被解释为更好的准确度-利润平衡。
- Decision: 完全客观指标：核心成功指标为MAE、MSEP、MTP、Precision、Recall、F1，均由评分、价格/成本和推荐列表直接计算，不依赖人类主观评价或语义判断。唯一核心目标：研究问题、方法目标函数、实验评价和贡献声明均围绕在shilling攻击下同时提升/保持准确度和电商利润，不存在并列的理论、制度或主观体验目标。Benchmark：全文明确使用'benchmark'一词，且在实验评价部分将PCC、SD、HPRS(+SD)作为基准方法进行比较，比较结果直接用于支持核心改进主张，具有明确参照点。故满足全部纳入标准。
- Confidence: 0.95

## Two-stage consumer credit risk modelling using heterogeneous ensemble learning

- Year/journal: 2019 / Decision Support Systems
- DOI: 10.1016/j.dss.2019.01.002
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "PD预测性能：Accuracy、AUC、误分类成本MC", "measurement_cn": "在10次重复5折交叉验证的50次实验上，将银行/非银贷款是否违约（60天以上逾期）作为事实标签，计算预测分类与实际违约状态的一致性、AUC以及由利率和LGD计算的误分类成本。", "objectivity_reason_cn": "违约状态来自贷款实际还款表现这一可审计外部事实，不依赖人的感受、语义判断或质量评价；所有指标由确定公式计算。"}, {"name_cn": "EAD/EL预测性能：R²、RMSE、MAE", "measurement_cn": "对进入第二阶段的违约贷款预测EAD，并与实际未偿金额/EL目标值比较；对整体EL同样计算R²、RMSE、MAE。", "objectivity_reason_cn": "EAD是贷款实际未偿金额的比例，EL由PD×EAD×LGD客观计算；预测误差均为可审计的数值误差。"}, {"name_cn": "贷款组合实际利润/相对利润", "measurement_cn": "根据模型排序选择前10%、20%等贷款，计算组合实际获得的利润（绝对和相对）。", "objectivity_reason_cn": "利润由贷款利率、违约损失等实际财务结果计算，属于可审计的交易结果，不涉及主观感受。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在Lending Club公开P2P数据和捷克非银行金融机构数据两个真实数据集上，用10次重复5折交叉验证评价所提两阶段模型；将PD模型与多种single/homogeneous/heterogeneous集成方法比较，将EAD模型与回归方法比较，并将整体EL模型与state-of-the-art单阶段和两阶段信用风险模型比较；表8显示提出模型在R²、RMSE、MAE上全面优于对照方法。
- Decision: 客观指标方面：核心成功指标为违约状态预测、EAD/EL预测误差和贷款组合利润，均来自外部可审计事实，不涉及主观构念；主观体验、用户评分或理论解释不是核心。唯一核心目标方面：文章的问题、设计、评价和贡献均集中于提升两阶段信用风险模型的客观预测和经济绩效，MC指标和MOEFS仅作为支撑组件。Benchmark方面：虽然未使用正式命名的公开benchmark套件，但作者在实验评价语境中明确使用benchmark一词设置对照（如RF benchmark classifier、SMOTEBagging benchmark），并通过表8与state-of-the-art单阶段和两阶段模型进行系统比较，作为核心提升主张的关键证据。因此严格满足纳入条件。
- Confidence: 0.95

## Utopia in the solution of the Bucket Order Problem

- Year/journal: 2017 / Decision Support Systems
- DOI: 10.1016/j.dss.2017.03.006
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "聚合距离（accuracy）", "measurement_cn": "对于每个数据集，利用pair order matrix C，计算算法得到的bucket order矩阵B与C之间的L1距离 D(C,B)=Σ|B(u,v)-C(u,v)|。该值越小表示聚合结果越接近输入的成对偏好矩阵。", "objectivity_reason_cn": "距离是基于数值矩阵的确定性算术运算，不依赖任何人的主观感受、语义判断或价值评价；输入矩阵C由真实排名数据客观统计得到，距离值可复算、可审计。"}, {"name_cn": "CPU时间", "measurement_cn": "在固定硬件（3.40 GHz, 8 cores, 16GB RAM）上运行各算法并记录秒数，用于效率对比。", "objectivity_reason_cn": "CPU时间是可测量的物理时间，不依赖主观解释。"}, {"name_cn": "可靠性（方差/标准差）", "measurement_cn": "多次独立运行（30次）所得结果的样本标准差，计算每种算法相对原始BPA标准差的比值。", "objectivity_reason_cn": "标准差是统计量，由算法输出数值计算得到，不涉及人的感知或情感。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: PrefLib (preference library) 中的50个真实世界排名数据集，包括ED-00006-Skate Data、ED-00011-Web Search、ED-00014-Sushi Data、ED-00015-Clean等
- Benchmark evaluation: 在PrefLib的50个数据集上，对BPA、LIA_G、LIA_L及其MP/MP2多pivot变体共9种算法进行了对比实验，报告了D(C,B)距离（accuracy）、与utopia值和BPA的比值、CPU时间和标准差。主要结果：LIA_G^MP2平均比原始BPA改善17%（ratio 0.829 vs 1），且通过Friedman检验和Holm事后检验验证显著性。
- Decision: 核心目标是改进BPA算法在OBOP上的精度（D(C,B)距离）和可靠性（方差），均为完全客观、可直接测量的数值指标，全文无任何主观量表、用户评审或语义判断作为成功标准。决策规则属于基于实验结果的次要应用，未构成并列核心贡献。实验在明确命名的PrefLib基准数据集（50个真实世界排名数据集）上进行，通过与原BPA及多个变体的比较证明改进效果，benchmark评价直接支撑了核心改进主张。因此同时满足客观指标、唯一核心目标和明确benchmark门槛。
- Confidence: 0.95

## Walrasian Pricing for Combinatorial Markets with Compact-Bidding Languages: An Application to Truckload Transportation

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2023.0676
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "总节省/相对节省", "measurement_cn": "模拟市场参与前后总运输成本之差；由 Ex-WDPR 最优目标值、状态基线和 spot 成本计算", "objectivity_reason_cn": "总成本是基于确定的运输距离、每英里成本参数和优化求解结果计算出的可比货币数字，不依赖任何人的感受或语义评价"}, {"name_cn": "托运人与承运人剩余", "measurement_cn": "由线性价格、VCG 折扣、预算平衡支付等计算得出各方相对于不参与市场的货币收益", "objectivity_reason_cn": "剩余是基于定价机制输出的支付额与成本参数计算的可审计数值，属于经济事实而非主观感受"}, {"name_cn": "残余嫉妒/偏离均衡", "measurement_cn": "ε-WAD 模型中 ε_c 的最优值，即承运人在最终价格下相对于其最优包的最大额外利润松弛", "objectivity_reason_cn": "ε_c 是数学规划的解，衡量与 Walrasian 均衡约束的客观计算偏差"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在基于真实参数生成的模拟卡车运输市场上，将 IDP 与 VCG 和 SMRA 对比：报告总节省、相对节省、托运人与承运人剩余和残余嫉妒；结果显示 IDP/VCG 相比 SMRA 有更高节省（13.4% vs 9.4%），IDP 保持托运人正剩余而 VCG 在高交换率下变负，clique cuts 使更多实例达到 envy-free。
- Decision: 客观指标方面：核心结果指标（总节省、剩余、残余嫉妒）均为优化模型和成本参数直接推导出的货币/数学数值，不依赖人类感受或语义评价；唯一核心目标是提高经济效率并给出可实现的均衡价格，无并列的主观或理论核心目标。Benchmark 方面：全文在实验评价部分明确使用 benchmark 一词陈述对 IDP 与 VCG、SMRA 的系统化比较，且有明确参照点和数值提升，该 benchmark 结果直接支撑核心效率提升主张。因此 strict_include=true。
- Confidence: 0.95

## Weighted doubly robust learning: An uplift modeling technique for estimating mixed treatments' effect

- Year/journal: 2024 / Decision Support Systems
- DOI: 10.1016/j.dss.2023.114060
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "提升曲线下面积 (AUUC)", "measurement_cn": "根据估计的CATE对客户降序排序，计算不同目标分位下处理组与对照组累计收入差，并对分位积分。", "objectivity_reason_cn": "直接基于客户未来三个月的消费金额（平台收入）计算，不依赖主观评价或语义判断，可审计。"}, {"name_cn": "Qini 系数", "measurement_cn": "基于Qini曲线与随机目标线之间的面积，其中Qini曲线为处理组与对照组按样本量校正后的累计收入差。", "objectivity_reason_cn": "同样基于实际消费金额和分组，属于客观绩效指标。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在合成数据集和工业数据集上，将WDRL与S-learner、T-learner、X-learner、DML、DRL五种主流uplift建模方法进行系统化比较，使用四种基学习器，以AUUC和Qini系数为评价指标。结果显示WDRL在多数设置下优于这些baseline。
- Decision: 该文章的核心目标是提出并验证WDRL方法，以提升混合处理场景下uplift建模的客观绩效指标（AUUC和Qini系数）。这些指标直接基于客户实际消费金额计算，完全客观。全文评价结构围绕与多个baseline的比较展开，并在实验设计部分明确使用'comprehensive benchmark study'表述，属于陈述式benchmark，且该benchmark评价直接支撑核心性能提升主张。未发现主观构念或并列核心目标。因此两个模块均通过，strict_include为true。
- Confidence: 0.95

## A Graph-Based Ant Algorithm for the Winner Determination Problem in Combinatorial Auctions

- Year/journal: 2021 / Information Systems Research
- DOI: 10.1287/isre.2021.1031
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "胜者确定解的收入/解质量（revenue / solution quality）", "measurement_cn": "在94个Lau-Goh公开测试实例上运行TrACA，以WDP-IP目标函数（入选投标价之和）度量；与全局最优值及20个启发式算法的最佳值比较，计算解质量%、ISP、Z分数和中位数检验结果", "objectivity_reason_cn": "投标价格和分配约束均为可审计的输入事实，收入由确定性目标函数计算，不依赖人的感受、语义评估或价值判断"}, {"name_cn": "达到最优/近最优解的时间（seconds）", "measurement_cn": "记录TrACA在各实例上达到全局最优或98%最优所需的墙钟时间，并与CPLEX和Max W Clique等精确算法的求解时间比较", "objectivity_reason_cn": "运行时间由可重复计算的时钟结果产生，属于可直接观测的技术/物理指标"}, {"name_cn": "最优解概率（optimal solution probability, OSP）", "measurement_cn": "在30次重复运行中TrACA生成全局最优解的比例，按不同蚁群规模（100/200/300/400）报告", "objectivity_reason_cn": "是否达到全局最优可由同一WDP-IP的精确解核验，属于外部可审计事实"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: Combinatorial Auction Test Suite (CATS; Leyton-Brown et al. 2002) | Lau and Goh (2002) test instances (94 instances)
- Benchmark evaluation: 在94个Lau-Goh公开测试实例上，TrACA与20个近年启发式算法（MA、BHS、DDCM、ACLS、SHH、GA、DE、BRKGA、SLS、TS等）以及CPLEX、Max W Clique进行系统化比较；报告median test、ISP、Z score、solution quality%、运行时间、最优解概率。结果显示TrACA在76/94实例达到全局最优，18/94达到98%最优，且达到最优解的用时最多为精确算法约1/6。
- Decision: 客观指标方面：核心评价指标为胜者确定的收入/解质量、求解时间、最优解概率，全部可直接观测且不依赖人类语义或偏好；唯一核心目标是以算法改进实现WDP求解的速度-精度提升，理论证明和搜索有效性分析均为支撑，不构成并列核心贡献。Benchmark方面：全文在实验/结果部分明确使用benchmark heuristics表述，称与Table 1的20个基准启发式进行比较，并在CATS/Lau-Goh公开测试实例上以CPLEX、Max W Clique及众多baseline为参照报告客观提升结果；benchmark评价支撑核心性能改进主张。两个模块均通过，故strict_include=true。
- Confidence: 0.94

## Combining Crowd and Machine Intelligence to Detect False News on Social Media

- Year/journal: 2022 / MIS Quarterly
- DOI: 10.25300/misq/2022/16526
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "假新闻检测性能（PR AUC、F1、recall、precision）", "measurement_cn": "在 Weibo 和 Twitter 两个真实数据集上，以官方事实核查/参考数据集标签为 ground truth，将 CAND 框架与若干基准方法比较，计算标准分类性能指标；PR AUC 是主要指标。", "objectivity_reason_cn": "待预测标签是外部可核验的事实类别（false vs true news），不依赖用户的满意度、价值判断或主观质量评价；指标计算方式是确定性的分类性能统计。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在 Weibo 与 Twitter 数据集上系统比较 CAND 各变体（CAND-1、CAND-12、CAND-123）与特征型基准（SVM、CNN、LSTM、Bi-LSTM、BERT）、端到端基准（Concat、HSA）以及聚合基准（MV、BAM），报告 PR AUC、F1、recall、precision，并显示 CAND 在多种不平衡比例下显著优于基准方法。
- Decision: 文章核心目标是提出 CAND 框架以提升假新闻检测性能，核心指标为 PR AUC、F1、recall、precision，ground truth 来自官方事实核查和已有参考数据集的客观事实标签，全部核心成功结果均为客观指标。文章在实验部分明确使用 benchmark methods 作为比较基准，并在多个数据集和不平衡比例下报告相对 benchmark 的提升，符合 benchmark 比较式评价要求。因此 objective_metric、core_goal_status 和 benchmark 门槛均通过，strict_include=true。
- Confidence: 0.94

## Using social network and semantic analysis to analyze online travel forums and forecast tourism demand

- Year/journal: 2019 / Decision Support Systems
- DOI: 10.1016/j.dss.2019.113075
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "国际机场到达人数（international airport arrivals）", "measurement_cn": "从EUROSTAT数据库按月提取的欧洲7个首都城市国际机场到达人数（不含过境旅客），作为旅游需求的代理变量；预测模型的目标是降低该序列的预测误差（MSFE/RMSE）。", "objectivity_reason_cn": "国际机场到达人数是可审计的外部事实数据，不依赖任何人的感受、意义理解或价值判断；预测精度通过实际观测值与模型预测值之间的数值误差确定，属于完全客观的直接指标。"}, {"name_cn": "预测误差（MSFE/RMSE）", "measurement_cn": "通过滚动窗口外样本预测，比较AR、FAAR、BRIDGE-GF、FABM-GF等模型的平均均方预测误差和均方根误差。", "objectivity_reason_cn": "预测误差由实际到达人数与预测值的确定性计算得出，是客观可复核的精度指标。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 作者在7个欧洲首都城市的国际机场到达人数数据集上，以自回归模型（AR）为朴素基准，并以BRIDGE-GF等模型为额外基准，在滚动窗口外样本框架下比较FAAR和FABM-GF等模型的预测性能。结果表（Table 4）报告相对MSFE和RMSE，显示加入社交网络和语义变量的模型在大部分情况下相对基准模型有预测精度提升。
- Decision: 文章唯一核心目标是提升国际机场到达人数这一完全客观指标的预测精度；所有自变量均来自论坛日志和公开统计数据，成功标准是预测误差（MSFE/RMSE）的降低，不存在主观构念或人类语义评价作为核心结果。模型评价部分明确使用AR作为朴素benchmark specification并列出其他benchmark模型，且该benchmark比较直接支撑核心提升主张。因此两模块均通过，strict_include为true。
- Confidence: 0.94

## Visualizing social network concepts

- Year/journal: 2010 / Decision Support Systems
- DOI: 10.1016/j.dss.2010.02.001
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "任务准确率（effectiveness）", "measurement_cn": "受试者完成网络概念理解任务，由实验者依据网络数据的客观事实核对答案；例如结构等价任务按受试者所选人物与目标人物的共同连接数除以目标人物连接数计分。", "objectivity_reason_cn": "答案正确性由网络结构本身决定，不依赖受试者的感受、偏好或主观质量判断，计分规则固定可复现。"}, {"name_cn": "任务完成时间（efficiency / time-to-task）", "measurement_cn": "实验者使用秒表记录每个受试者完成每项任务的时间，以秒为单位。", "objectivity_reason_cn": "完成时间是可直接观测和审计的客观行为数据，不依赖人的感受或价值判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 作者将 NetVizer 与一个基于力导向布局并稍作修改的基准可视化系统在同一犯罪网络数据上进行比较，通过受试者完成七项社会网络概念理解任务来评价；结果表3和表4报告了准确率和完成时间的统计比较，并用这些结果支撑 NetVizer 在 betweenness centrality、gatekeeper identification、structural similarity 等概念理解上的提升。
- Decision: 核心指标是任务准确率和完成时间，均由客观任务答案和秒表计时得到，属于可观测客观绩效；论文没有将主观量表作为核心成功标准。核心目标是提出并验证以网络概念理解任务客观绩效提升为导向的概念可视化方法，没有并列的同等核心贡献。全文存在明确且处于评价语境的 benchmark 表述（自建基准系统），并以该基准比较结果作为核心改进主张的证据，因此同时满足两个模块的门槛。
- Confidence: 0.94

## A collaborative filtering approach for recommending OLAP sessions

- Year/journal: 2015 / Decision Support Systems
- DOI: 10.1016/j.dss.2014.11.003
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "精确率 (Precision)", "measurement_cn": "根据推荐会话 r_s 与实际未来 f_s 的相似度判定真/假正例，公式 Precision = |TP| / (|TP|+|FP|)，在合成日志上计算。", "objectivity_reason_cn": "构造依赖OLAP会话形式化相似度，不涉及人类感受或语义价值判断，值由日志和算法确定。"}, {"name_cn": "召回率 (Recall)", "measurement_cn": "Recall = |TP| / (|TP|+|FN|)，在合成日志上基于实际未来计算。", "objectivity_reason_cn": "基于可审计的真实未来和相似度判定，非主观评价。"}, {"name_cn": "F值 (F-measure)", "measurement_cn": "F = 2 * Precision * Recall / (Precision + Recall)，由精确率和召回率计算。", "objectivity_reason_cn": "是客观指标的组合。"}, {"name_cn": "覆盖率 (Coverage)", "measurement_cn": "Coverage = |RS| / |S|，即能够给出推荐的比例。", "objectivity_reason_cn": "由推荐系统输出计数得到，完全客观。"}, {"name_cn": "预见度 (Foresight)", "measurement_cn": "Foresight(s) = (1 - σ_que(s[.], r_s[.])) * (1 - σ_ses(a))，基于查询/会话相似度计算。", "objectivity_reason_cn": "由定义好的相似度公式计算，不依赖人类体验。"}, {"name_cn": "新颖度 (Novelty)", "measurement_cn": "Novelty(s) = min_{l∈L}(1 - σ_ses(a'))，基于推荐会话与日志的最小相似度。", "objectivity_reason_cn": "由相似度公式计算，是客观属性。"}, {"name_cn": "执行时间 (Execution time)", "measurement_cn": "测量三个阶段的运行时间，单位为毫秒，在不同日志特征下记录。", "objectivity_reason_cn": "物理时间度量，完全客观。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在该合成日志基准上，对推荐系统进行了多组有效性测试（精度、召回、F值、覆盖率、预见度、新颖度）和效率测试（执行时间），并与方法[6]在同一日志规模（200 sessions）下对比，结果显示精度0.94对0.52、召回0.87对0.52。
- Decision: 客观指标方面：核心成功指标是完全客观的推荐质量度量（精确率、召回率、F值、覆盖率、预见度、新颖度）和效率度量（执行时间），均由定义明确的公式或物理时间计算，不依赖人类感受或语义评价；核心目标唯一地是提升这些客观指标。Benchmark方面：实验部分明确使用“benchmark”一词定义了基于CENSUS合成日志的测试基准，并在该基准上进行了系统化的有效性/效率评价，且与已有方法[6]进行明确比较，benchmark结果直接支撑核心提升主张。因此严格纳入。
- Confidence: 0.93

## A data-driven approach to predict the success of bank telemarketing

- Year/journal: 2014 / Decision Support Systems
- DOI: 10.1016/j.dss.2014.03.001
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "AUC（ROC曲线下面积）", "measurement_cn": "在银行电话营销客户订阅长期存款的成功/失败二分类预测中，基于留出验证集和滚动窗口测试集，由rminer包计算的ROC曲线下面积", "objectivity_reason_cn": "预测目标是客户是否实际订阅长期存款（success/failure），这是银行系统记录的可审计事实标签，不依赖人的感受、价值判断或语义评价；AUC由预测概率和事实标签计算，客观可复现"}, {"name_cn": "ALIFT（LIFT累积曲线下面积）", "measurement_cn": "在相同二分类预测场景下，基于测试集预测概率排序和实际订阅事实标签计算的LIFT累积曲线下面积", "objectivity_reason_cn": "LIFT值基于实际订阅结果这一外部可核验事实，计算过程确定，不涉及主观评价"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 文章在银行电话营销成功预测任务上，以LR、DT、SVM作为明确参照方法，对提出的NN模型进行系统化比较评价。建模阶段（留出验证集）：NN的AUC=0.929、ALIFT=0.878，优于LR（0.900/0.849）、DT（0.833/0.756）、SVM（0.891/0.844），统计显著；滚动窗口阶段（测试集）：NN的AUC=0.794、ALIFT=0.672，优于LR（0.715/0.626）、DT（0.757/0.651）、SVM（0.767/0.656）。比较结果直接支撑“NN模型最佳并可用于银行电话营销”的核心主张。
- Decision: 客观指标方面：核心目标为预测银行电话营销中客户是否实际订阅长期存款这一客观事实标签，核心评价指标AUC和ALIFT均由事实标签和预测概率计算，不依赖人的感受、语义或价值判断；研究问题、设计目标、评价和贡献声明均围绕该客观分类性能提升展开，无其他并列核心贡献，因此判定为完全客观且唯一核心目标。Benchmark方面：全文虽未命名公开基准数据集，但在实验/评价语境中明确以“compare/for comparison purposes”等基准化陈述将提出的NN与LR、DT、SVM和随机基线进行系统比较，两种评价阶段均报告NN在AUC和ALIFT上的相对提升，该基准比较直接支撑核心预测性能主张；符合benchmark_comparison_central。因此两个模块均通过，strict_include=true。
- Confidence: 0.93

## A decision support system for integrating manufacturing and product design into the reconfiguration of the supply chain networks

- Year/journal: 2012 / Decision Support Systems
- DOI: 10.1016/j.dss.2011.11.014
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "缺货量/延迟交付量（backorders）", "measurement_cn": "由解析模型和GoldSim离散事件/系统动力学仿真输出，依据需求、生产提前期、库存控制方程计算。", "objectivity_reason_cn": "backorders是供应链运作中的可审计运营状态，不依赖人的感受、语义或价值判断；数值由模型方程和仿真日志决定。"}, {"name_cn": "库存水平/安全库存（inventory level/safety stock）", "measurement_cn": "通过GI/G/1排队模型、Erlang分布、库存分配公式以及仿真模型计算各阶段安全库存和总库存成本。", "objectivity_reason_cn": "库存量是物理/技术性运营指标，由需求波动、提前期、服务水平等参数确定，独立于人类主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 作者将'装配序列规划前的原供应链配置'作为参照，评价'装配序列规划后的供应链配置'，通过表2与表3比较安全库存分配和库存水平；结果显示装配序列规划消除了部分库存点（如产品ABDEHI、Wheel、Pad、Stand A）的安全库存，并使总安全库存成本最小化。模型验证部分还将解析模型与GoldSim仿真模型进行benchmark对比，检验安全库存、订单率和缺货水平的一致性。
- Decision: 核心指标backorders和inventory level均为客观可测的运营指标，不依赖人类感知或语义评价；论文的摘要、引言、结果和结论均围绕通过DSS实现供应链重构和库存分配来降低缺货与库存水平这一唯一核心目标展开，无并列主观或理论核心贡献。全文存在明确的benchmark表述：第4.3节将装配序列规划前后的供应链配置进行比较，属于评价语境，且该比较直接支持安全库存减少和总库存成本降低的核心提升主张，并有明确的参照点（规划前配置/仿真模型）。因此同时满足客观指标、唯一核心目标和明确benchmark门槛。
- Confidence: 0.93

## A deep learning approach for detecting fake reviewers: Exploiting reviewing behavior and textual information

- Year/journal: 2023 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113911
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "假评论者检测性能：Accuracy、Precision、Recall、F1-score、AUC", "measurement_cn": "在YelpZIP和YelpNYC数据集的假/真评论者标签上，通过5折交叉验证计算TP、FP、TN、FN，并按式(10)-(12)计算P、R、F1，同时报告AUC。", "objectivity_reason_cn": "标签是外部可核验的评论者事实状态（Yelp平台过滤产生的假/真评论者标签），预测性能完全由确定性公式从预测标签与真实标签计算，不依赖人类感受或语义质量评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: YelpZIP dataset | YelpNYC dataset
- Benchmark evaluation: 在YelpZIP和YelpNYC两个真实数据集上，将提出的行为敏感特征提取器与上下文感知注意力模型同LR、RF、SVM、CART、NB以及CNN、BiLSTM、C-LSTM、BERT、ALBERT、DistilBERT、RoBERTa、Longformer等基准比较，报告Accuracy、Precision、Recall、F1、AUC，并通过配对t检验说明显著提升；另与Rayana和Akoglu、Sandulescu和Ester、Kumar等的既有方法比较AUC/F1。
- Decision: 该文以提升假评论者检测的客观分类性能为唯一核心目标，核心指标为Accuracy、Precision、Recall、F1和AUC，来源于YelpZIP/YelpNYC上冻结的假/真评论者标签，完全客观；研究问题、实验设计和贡献声明均围绕检测性能提升展开，无主观量表或并列理论贡献。全文存在明确的benchmark评价表述：作者在摘要和实验设计中将所提框架与state-of-the-art benchmarks比较，并在Yelp两个真实数据集上与多个基线模型及既有方法比较，benchmark结果直接支撑核心性能提升主张，且有多个明确比较对象。因此严格纳入。
- Confidence: 0.93

## A demand forecast model using a combination of surrogate data analysis and optimal neural network approach

- Year/journal: 2013 / Decision Support Systems
- DOI: 10.1016/j.dss.2012.12.008
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "均方误差 (MSE)", "measurement_cn": "在测试数据上，由神经网络预测值与实际需求值直接计算均方误差；见Tables 1-4。", "objectivity_reason_cn": "MSE完全由数值运算得到，不依赖人的感受、语义或价值判断。"}, {"name_cn": "预测准确率 (Prediction accuracy)", "measurement_cn": "以测试数据标准差为阈值，将预测偏差低于阈值的预测计为准确，计算准确比例；见Fig.5/7/10/13及Tables 1-4。", "objectivity_reason_cn": "准确率由固定的确定性规则判定预测偏差是否在阈值内，不依赖人工评分或主观判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在两类模拟需求（线性季节需求和非线性Ikeda混沌需求）和一个实际需求（Ontario月度汽油需求）上，将MDL-optimal NN与MSE-optimal NN、指数平滑、多元回归四种方法同时比较，报告MSE和预测准确率（Tables 1-4）。
- Decision: 客观指标方面：全文以MSE和预测准确率两个客观可测量的预测性能指标作为核心成功标准，不含主观满意度、专家评分等构念。唯一核心目标：研究问题、设计目标和贡献声明均围绕提升需求预测准确性展开，surrogate data方法和MDL都是服务该目标的技术组件，没有并列核心贡献。Benchmark方面：引言明确宣称将与现有方法在模拟和实际数据上benchmark；实验部分在多个数据场景中与MSE-optimal NN、指数平滑、多元回归等明确参照比较，并以比较结果直接支持MDL-optimal神经网络的核心提升主张。因此全部门槛满足，strict_include=true。
- Confidence: 0.93

## A domain-feature enhanced classification model for the detection of Chinese phishing e-Business websites

- Year/journal: 2014 / Information & Management
- DOI: 10.1016/j.im.2014.08.003
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "精确率（Precision）", "measurement_cn": "TP/(TP+FP)，基于对钓鱼/真实网站的二元分类结果计算", "objectivity_reason_cn": "分类标签（钓鱼网站或真实网站）是由第三方平台核实的外部事实，不依赖人的主观感受或语义评价；精确率的计算是确定性公式。"}, {"name_cn": "召回率（Recall）", "measurement_cn": "TP/(TP+FN)，基于对钓鱼/真实网站的二元分类结果计算", "objectivity_reason_cn": "同上，标签为外部可核验事实，计算方式客观。"}, {"name_cn": "F1值（F1-measure）", "measurement_cn": "2*(precision*recall)/(precision+recall)，由精确率和召回率计算", "objectivity_reason_cn": "基于客观分类结果和确定性公式，不涉及主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在约3000个中国电子商务网站（1416个钓鱼网站和1462个真实网站）上，将所提出的CBML模型与两个基线模型（Abbasi et al.模型和He et al.模型）进行对比。使用相同SMO算法和相同训练/测试数据，采用30折交叉验证和配对t检验，比较precision、recall和F1。结果显示CBML显著优于两个基线模型，支持核心提升主张。
- Decision: 核心目标是提升钓鱼网站检测的客观性能指标（precision、recall、F1），该目标贯穿研究问题、假设、评价和贡献；不存在主观构念或并列核心目标。全文存在明确的benchmark表述（第4.3节将基线模型称为benchmarks），并以此比较作为核心证据证明CBML相对于两个基线模型的显著提升，因此满足严格纳入条件。
- Confidence: 0.93

## A dynamic shipment matching problem in hinterland synchromodal transportation

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113289
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "总匹配成本", "measurement_cn": "由 MILP/BIP 目标函数计算，包括运输成本、转运成本、仓储成本、延误成本和碳税，单位欧元", "objectivity_reason_cn": "成本由模型参数和确定性决策变量直接算出，不依赖人的感受、语义理解或价值判断"}, {"name_cn": "计算时间", "measurement_cn": "MATLAB R2017a 中运行，CPLEX 12.6.3 求解的 CPU 秒数", "objectivity_reason_cn": "运行时间是可审计的系统日志指标，属于完全客观的技术性能指标"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在生成的欧洲腹地多式联运网络实例上，把 greedy approach 作为基准，比较 RHA 在不同需求密度、动态程度、提前期和响应时间下的总成本；结果显示 RHA 在所有场景下总成本更低。此外，启发式算法以精确算法为参照报告 %gap 和 CPU 时间。
- Decision: 核心指标为总匹配成本和计算时间，均为确定性模型和系统运行时间中可观测的客观量，不含任何用户主观评分或语义判断；全文唯一核心目标是通过 rolling horizon 和启发式算法在动态场景下降低总成本并保证计算效率。Benchmark 条件满足：作者在 4.1 和 6.3 中明确以 greedy approach 为 benchmark 进行系统化基准比较，且该比较直接支持 RHA 降低总成本的核心主张，并有明确对照对象。因此 strict_include=true。
- Confidence: 0.93

## A hybrid system by evolving case-based reasoning with genetic algorithm in wholesaler's returning book forecasting

- Year/journal: 2006 / Decision Support Systems
- DOI: 10.1016/j.dss.2006.02.014
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "慢销书预测的平均错误率（分类准确率）", "measurement_cn": "将每本书预测为慢销书或畅销书（0/1），与按实际总销量阈值（发行后6个月总销量<5本）定义的 A_i 比较，O_i=1 若预测等于实际；e=k-ΣO_i；平均错误率=(1/m)Σ(e_t/k)，见式(6)。", "objectivity_reason_cn": "实际类别 A_i 由可审计的销售记录（6个月实际总销量是否小于5本）确定，不依赖人的感受、语义价值判断或偏好；比较结果为确定性的命中/未命中计数。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 作者在台湾书商的实际904个案例数据上，以平均错误率作为评价基准，对Model A（GA/CBR）、Model B（BPNN）、Model C（传统CBR）、Model D（多元回归）进行系统化比较；在不同训练/测试分组（200/100、200/200、300/100）下重复10次，报告平均错误率和标准差（表17、19、21），并改变参照案例数观察Model A表现。
- Decision: 客观指标通过：核心结果为慢销书这一操作性事实标签的预测平均错误率，依据实际销量阈值可审计；无主观构念进入核心成功标准。唯一核心目标通过：全文从问题、设计到贡献均围绕准确率提升。Benchmark通过：作者明确以average error rate作为forecasting benchmarks并在实验中对四个模型作系统化比较，有明确参照点，结果用于证明GA/CBR准确率更高。因此strict_include=true。
- Confidence: 0.93

## A model-free scheme for meme ranking in social media

- Year/journal: 2016 / Decision Support Systems
- DOI: 10.1016/j.dss.2015.10.002
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "Kendall-tau_Sim", "measurement_cn": "将方案生成的meme排名与网站黄金标准排名比较，按式(15)将Kendall tau距离归一化为相似度", "objectivity_reason_cn": "排名列表是平台可观察事实，成对一致/不一致是确定性计算，不依赖人类感受、语义理解或价值判断"}, {"name_cn": "Edit_Sim", "measurement_cn": "将方案生成的排名列表与网站黄金标准排名比较，按式(16)将编辑距离归一化为相似度", "objectivity_reason_cn": "基于Levenshtein距离的确定性计算，排名列表本身可审计，不依赖人类感受或语义判断"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在两个大规模真实数据集（新浪微博和Daily Kos）上，将提出的无模型方案（MF）与Follower_Num、PageRank、Dynamic、Diffusion四个基准方法比较；在Kendall-tau_Sim和Edit_Sim两个排名相似度指标上，MF显著优于四个基准。例如Kos数据集：Kendall-tau_Sim 0.822 vs 最优基准0.578，Edit_Sim 0.500 vs 最优基准0.200；Weibo数据集：Edit_Sim 0.400 vs 最优基准0.200。
- Decision: 核心指标为排名相似度（Kendall-tau_Sim、Edit_Sim），基于平台黄金标准排名进行确定性计算，完全客观，不依赖人类感知或语义判断。论文的唯一核心目标是提出并验证meme排名方案，使排名更接近黄金标准；Issue 3的流行度因子解释是辅助性洞察，不构成并列核心贡献。实验设计明确以'benchmark approaches'名义引入四种可比较的既有方法，并在两个数据集上通过结果表证明方案优于这些对照，符合明确的benchmark比较门槛。三个模块均通过，strict_include为true。
- Confidence: 0.93

## A multi-objective approach for profit-driven feature selection in credit scoring

- Year/journal: 2019 / Decision Support Systems
- DOI: 10.1016/j.dss.2019.03.011
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "期望最大利润（EMP）", "measurement_cn": "基于评分卡在保留样本上的违约预测、违约标签以及成本/收益参数（如LGD、EAD、ROI）按公式(3)计算得出，反映相对不筛选授信基线的增量利润。", "objectivity_reason_cn": "构念为可审计的财务利润，值由固定公式、客观违约事实和财务成本参数决定，不依赖人的感受或语义评价。"}, {"name_cn": "选用特征数量", "measurement_cn": "直接统计NSGA-II个体或最终评分卡所选入的二进制特征基因数量，用于衡量模型简洁性及数据获取/存储成本。", "objectivity_reason_cn": "特征个数是可确定性清点的事实计数，不依赖人类主观判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在十个信用评分数据集上，将NSGA-II生成的Pareto前沿与SFS、SBS、LASSO、单目标GA、单目标PSO及全特征评分卡进行系统比较，报告EMP和特征数量，并用S1/S2/S3非支配指标汇总相对基准的表现。
- Decision: 客观指标方面，核心结果为EMP和特征数量：EMP由固定财务公式、违约标签和成本参数决定，特征数量为确定性计数，二者均不依赖人的感知、偏好或语义评价；全文以最大化利润和最小化特征数量作为唯一核心设计目标，经验证据和贡献声明都围绕这一目标。Benchmark方面，作者在实验设置中明确将SFS、SBS、LASSO、单目标GA、单目标PSO及全特征评分卡称为benchmark或基准，在十个数据集上通过EMP和特征数量比较验证核心提升主张，并设置了明确参照点。因此两个模块均通过。
- Confidence: 0.93

## A transmission-constrained unit commitment method in power system scheduling

- Year/journal: 1999 / Decision Support Systems
- DOI: 10.1016/s0167-9236(98)00072-4
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "总发电成本（Total generating cost）", "measurement_cn": "在测试算例上由算法求解得到的primal value，包括燃料成本和启动成本，以美元计。", "objectivity_reason_cn": "成本由经济函数和发电计划直接计算，属于可审计的技术经济量，不依赖人的主观评价。"}, {"name_cn": "对偶间隙（Duality gap）", "measurement_cn": "由dual value与primal value的差值百分比计算。", "objectivity_reason_cn": "由数学优化结果直接确定，是算法收敛质量的客观度量。"}, {"name_cn": "CPU时间（秒）", "measurement_cn": "在HP 700工作站上各阶段及总运行时间。", "objectivity_reason_cn": "系统的物理运行时间，客观可复现。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: IEEE Reliability Test System (IEEE 24-bus test problem)
- Benchmark evaluation: 在IEEE 24-bus标准测试系统上运行所提three-phase Lagrangian relaxation算法，报告了无约束/约束情况下的dual value、primal value、duality gap和CPU时间；并在同一测试系统上比较direct approach与indirect approach，direct方法获得更低的primal cost和更短的总CPU时间。
- Decision: 文章核心目标是提出一个带输电约束的机组组合求解方法，以最小化总发电成本并提高求解效率。所有核心成功指标均为客观可测的物理/经济量（总成本、对偶间隙、CPU时间），没有任何主观评价或语义判断。在IEEE Reliability Test System（IEEE 24-bus标准测试系统）上进行数值评价，并与无约束情形以及indirect approach等明确参照点比较，benchmark评价直接支撑了核心改进主张。因此满足严格纳入条件。
- Confidence: 0.93

## Analysis of third-party request structures to detect fraudulent websites

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113698
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "分类性能指标：Accuracy、Sensitivity、Specificity、Precision、F1、Matthews correlation coefficient、Youden J statistic", "measurement_cn": "在自建网站数据集（205个合法网站、93个欺诈网站）上，使用10折交叉验证对17种预测模型计算上述指标；网站真值来自权威外部清单（欧盟假冒与盗版观察清单、美国贸易代表署恶名市场清单、维基百科虚假新闻网站清单）。", "objectivity_reason_cn": "预测目标是外部可核验的欺诈/合法网站事实标签，不依赖用户感受、偏好或语义质量判断；所有性能指标由预测结果与固定标签的确定性比较计算得出。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在自建数据集上对第三方请求结构（RS）方法、第三方使用（3PU）方法、组合数据模型及集成模型进行系统化比较，并同时报告三种朴素基准（全合法、全欺诈、随机）。结果显示RS较3PU在多数指标上显著提升，集成模型Accuracy从3PU的0.728和RS的0.721提升至0.826，F1从0.800/0.821提升至0.876。
- Decision: 客观指标、唯一核心目标和benchmark三方面均通过。核心目标是从网站第三方请求结构中预测合法/欺诈网站，全部成功指标为Accuracy、Sensitivity、Specificity、Precision、F1、MCC、Youden J等完全客观的分类性能指标；欺诈/合法标签来自外部权威事实清单，不依赖用户感受或语义质量判断，属于objective_fixed_factual_labels；无主观量表或并列核心贡献。全文在评价语境中明确使用“benchmark comparisons”表述，并在结论中称“improve upon the benchmark and existing prediction method results”，且与朴素基线、3PU基线、RS数据及组合/集成模型比较，基准结果直接支撑核心检测性能提升主张。因此strict_include=true。
- Confidence: 0.93

## Calibration of Heterogeneous Treatment Effects in Randomized Experiments

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2021.0343
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "个体处理效应估计的平均绝对误差（MAE）", "measurement_cn": "模拟中：MAE = (1/L)Σ_l (1/N)Σ_i |τ̂(X_i)-τ(X_i)|，其中 τ(X_i) 为DGP生成的ground-truth ITE；真实实验中：使用子组CATE的MAE_CATE = (1/|P|)Σ_S |τ̂(S)-τ^DM(S)|，其中 τ^DM(S) 为随机化实验中无模型差分估计。", "objectivity_reason_cn": "ground-truth ITE由数据生成过程固定；DM估计在RCT中由可审计的结果差异直接计算；MAE/MAE_CATE不依赖任何人的感受、偏好或语义判断。"}, {"name_cn": "策略效用（realized utility）", "measurement_cn": "在预算约束优化、多KPI优化和多处理uplift建模中，基于校准/未校准HTE制定策略，并用ground-truth ITE、off-policy evaluation或期望响应/Qini等客观规则计算实现效用。", "objectivity_reason_cn": "策略效用由模拟的真实潜在结果或OPE的客观期望公式计算，不依赖主观体验。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: Criteo AI Lab Uplift Prediction Dataset (Criteo large scale benchmark for uplift modeling, Diemert et al. 2018)
- Benchmark evaluation: 在Criteo公开benchmark数据集上，使用11种HTE模型（S/T/X/R/DR-learner、causal forest等）在训练集训练，验证集校准，测试集用MAE_CATE比较校准前后子组CATE与无模型DM估计的差异；Figure 6展示多数方法经校准后MAE_CATE下降，Figure 7以Q-Q图展示校准将模型CATE向无模型CATE对齐。该评价直接支撑核心主张：校准方法降低HTE估计误差。
- Decision: 客观指标方面：核心指标是HTE估计误差（MAE/MAE_CATE）和下游策略效用，均为可审计的客观技术指标，不涉及主观构念或人类语义评价。唯一核心目标方面：研究问题、设计目标、评价结构和贡献声明均围绕“诊断并校正HTE估计偏差/提升校准性”这一客观目标展开，理论命题和诊断工具是服务该目标的方法组成部分，不存在并列的核心目标。benchmark方面：文章在Criteo公开benchmark数据集上系统评价了11种HTE方法，并与未校准模型及多种MTUM基准方法比较，benchmark结果直接支撑核心提升主张；同时具有明确的参照点。因此满足strict_include条件。
- Confidence: 0.93

## Decision-Centric Active Learning of Binary-Outcome Models

- Year/journal: 2007 / Information Systems Research
- DOI: 10.1287/isre.1070.0111
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "直销活动利润", "measurement_cn": "在独立测试集上模拟邮寄决策：若模型估计的期望收入大于邮寄成本则发出邮件，利润为实际捐款总额减去邮寄成本；各学习曲线为10次随机划分的平均值。", "objectivity_reason_cn": "利润由实际捐款金额、邮寄成本、是否响应等可审计的财务与行为事实直接计算，不依赖人类感受、偏好或语义评价。"}, {"name_cn": "决策正确性/决策错误", "measurement_cn": "对照由真实概率和效用导出的最优决策，计算测试集上的决策一致率或错误率；论文说明结果与利润结论类似。", "objectivity_reason_cn": "最优决策由期望效用理论定义，正确与否是客观可判定的事实，不涉及主观体验或语义判断。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: KDD Cup 1998 direct-marketing competition data set (publicly available via UCI repository; Blake and Merz 1998)
- Benchmark evaluation: 在KDD Cup 1998直销数据上，将数据划分为初始训练集、未标记池和测试集，比较GOAL、误差中心获取(ECA/Bootstrap-LV)、均匀随机抽样(URS)和用于决策学习的uncertainty sampling(US)；在不同获取数量下计算模拟直销活动的利润，并在利润、决策错误、概率估计误差、鲁棒性和非均匀成本场景下进行评价。
- Decision: 核心指标是直销活动利润和决策正确性，均为客观可审计结果，无主观满意度、感知价值或人体语义评分。唯一核心目标与贡献是提出并验证决策中心主动学习方法以提升客观决策盈利；论文虽有框架和理论推导，但均为支撑该目标的方法学内容，不构成并列核心结果。Benchmark门槛方面，全文虽未出现'benchmark'一词，但明确命名了公开的KDD Cup 1998数据挖掘竞赛数据集，并将其作为评价场地；在该基准上对GOAL与URS、ECA、US等明确参照点进行了系统的利润/决策性能比较，比较结果直接支撑核心改进主张。因此两个模块均通过，strict_include为true。
- Confidence: 0.93

## Event detection from online news documents for supporting environmental scanning

- Year/journal: 2004 / Decision Support Systems
- DOI: 10.1016/s0167-9236(03)00028-9
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "漏报率（miss rate）与误报率（false alarm rate）", "measurement_cn": "将系统对新闻事件是否为新增事件的判断与人工标注的每条新闻所属事件标签进行比较，在不同新颖性阈值下计算漏报率（未能检测出新事件的比例）和误报率（未能识别出旧事件的比例），并用 Detection Error Tradeoff（DET）曲线展示二者的权衡。", "objectivity_reason_cn": "事件标签对应可外部核验的事实性事件（飞机失事、利率调整、企业并购等），检测错误可依据系统输出与事实标签确定性地计数，不依赖用户满意度、偏好或质量评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: INCR（single-pass incremental clustering）传统基于特征的事件检测技术
- Benchmark evaluation: 在自建的来自 excite.com 的 492 篇新闻语料上，将 NEED 与传统事件检测基线 INCR 进行对比；通过 DET 曲线比较漏报率与误报率，尤其关注低漏报率区间，并据此论证 NEED 的改进。
- Decision: 核心指标是事件检测的漏报率和误报率，属于可客观计数的事实标签检测性能；核心目标与贡献均为提升该客观检测指标，无并列的主观或理论核心贡献；全文存在明确的 benchmark 表述，作者在实证评价部分以 INCR 作为基准进行 DET 曲线比较，并以此支撑 NEED 的改进主张。因此满足全部纳入条件。
- Confidence: 0.93

## Forecasting demand profiles of new products

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113401
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "RMSE（预测总需求与每周需求的均方根误差）", "measurement_cn": "根据式(1)，比较预测需求与实际历史销售需求逐期计算；同时用于总需求和每周需求预测。", "objectivity_reason_cn": "实际需求来自企业数据库/合成数据生成模型的销量记录，预测值与观测值差异可确定计算，不依赖人类感知或语义评价。"}, {"name_cn": "PICP 与 PINAW（预测区间覆盖率与归一化平均宽度）", "measurement_cn": "按式(2)(3)，基于实际需求是否落入预测区间、区间宽度与需求极差之比计算。", "objectivity_reason_cn": "区间覆盖率与宽度均由实际销售数据和确定的预测区间边界计算，属于可审计的数值指标。"}, {"name_cn": "Cycle Service Level 一致性（CSL）", "measurement_cn": "按式(4)，在库存补货模拟中统计未发生缺货的周期比例，并与目标分位数/目标服务水平比较。", "objectivity_reason_cn": "缺货与否由实际需求与库存策略模拟确定，CSL为可复现的客观运营绩效指标。"}, {"name_cn": "库存成本（订购、持有、超量持有、Lost sales）", "measurement_cn": "在三种库存情景下按给定成本参数和实际需求模拟，计算各方法的总库存成本。", "objectivity_reason_cn": "成本由明确公式、给定参数和模拟库存/缺货事件计算，虽含假设但确定可复现，不含主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在合成数据集和5家企业真实数据集（A-E）上，将 DemandForest（含 Gamma/Log-Normal 扩展）与 ZeroR、OneP 两个基准方法比较，报告 RMSE、PICP、PINAW、CSL 一致性及库存成本。总体结论是 DemandForest 在多数数据集上 RMSE 最低、预测区间更可靠、合成数据集库存成本最低；少数企业数据集上 ZeroR 或 OneP 成本更低，但作者仍以 benchmark 对比作为 DemandForest 核心性能提升的证据。
- Decision: 客观指标方面：核心成功指标均为可审计的需求预测误差、预测区间质量、服务水平一致性和库存成本，不依赖主观感受或人类语义评分；唯一核心目标是提升新产品预测和库存绩效。Benchmark方面：作者在实验设置部分明确以 benchmark 一词定义 ZeroR 和 OneP 两个对照方法，并以它们在多个真实数据集和合成数据集上的结果作为 DemandForest 性能提升的核心证据；评价位于实验/结果语境，且存在明确参照点。因此两个模块均通过，strict_include=true。
- Confidence: 0.93

## Genetic programming for prevention of cyberterrorism through dynamic and evolving intrusion detection

- Year/journal: 2007 / Decision Support Systems
- DOI: 10.1016/j.dss.2006.04.004
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "测试集总体准确率", "measurement_cn": "在KDD Cup 1999/DARPA数据划分出的测试集上，将GP模型预测结果与连接记录的事实标签（入侵/非入侵）比对，计算正确分类百分比（Table 2）。", "objectivity_reason_cn": "入侵/非入侵是攻击记录的事实类别，不依赖人的感受、意义理解或价值判断；正确率可由预测标签与固定事实标签直接计算。"}, {"name_cn": "正例（入侵）识别准确率", "measurement_cn": "在测试集中仅对标记为特定类型入侵的连接计算正确识别百分比（Table 3）。", "objectivity_reason_cn": "以KDD数据中的攻击类型标注为事实真值，模型输出与该事实比对，结果可审计。"}, {"name_cn": "负例（非入侵）识别准确率", "measurement_cn": "在测试集中对标记为非入侵的连接计算正确识别百分比（Table 4）。", "objectivity_reason_cn": "与正例准确率同理，依据固定事实标签和可复算的分类结果。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: 1999 Knowledge Discovery in Database (KDD) Cup data (DARPA/MIT Lincoln Laboratories) | KDD'99 Classifier Learning Contest
- Benchmark evaluation: 在KDD Cup 1999这一公开基准数据集上，对Smurf、Satan、IPSweep、PortSweep、Back、Normal、Buffer Overflow、WarezClient、Neptune等入侵域训练GP模型并用独立测试集评估；Table 2-4比较普通交叉与同源交叉的总体/正例/负例准确率，Table 5将同源交叉结果与KDD'99竞赛获胜方法（C5 bagged boosting）和简单1-近邻方法按攻击类别比较，显示在Probe、DoS、U2R、R2L上的准确率大幅提高，Normal略低。
- Decision: 文章以KDD Cup 1999公开基准数据为实验场地，核心目标是评估GP（特别是同源交叉）能否提升网络入侵检测的准确率；所有核心成功指标均为测试集总体准确率、正例准确率和负例准确率，属于对固定事实标签（入侵/正常）的预测性能，完全客观。研究问题、方法、结果与结论均围绕这些客观指标展开，没有主观量表或并列的理论/政策贡献。KDD Cup/KDD'99竞赛是命名式公开benchmark，Table 5在结果部分将其结果作为明确参照并与竞赛获胜方法、1-NN比较，benchmark评价直接支持核心提升主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.93

## How can online marketplaces reduce rating manipulation? A new approach on dynamic aggregation of online ratings

- Year/journal: 2017 / Decision Support Systems
- DOI: 10.1016/j.dss.2017.10.003
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "操纵零售商（retailer A）的销售额", "measurement_cn": "模拟在线市场中1200个消费者逐轮购买决策，记录购买A产品的次数；比较不同聚合方法下额外虚假好评带来的销售额增幅。", "objectivity_reason_cn": "销售额是模拟市场中可计数的交易结果，不依赖人的感受、价值判断或语义评价。"}, {"name_cn": "诚实零售商（retailer B）的销售额", "measurement_cn": "同一模拟市场中记录购买B产品的次数，用于衡量聚合方法对未操纵评分零售商造成的附带损害。", "objectivity_reason_cn": "销售额是模拟市场中可计数的交易结果，是客观可审计的模拟事实。"}, {"name_cn": "评分聚合的信息损失概率", "measurement_cn": "基于二项分布公式计算负向或正向评分在单值、三值和动态聚合下被忽略的概率。", "objectivity_reason_cn": "该概率由给定产品和评分序列的统计分布直接计算，不涉及主观感知。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在模拟在线市场中，将动态k值聚合与即时更新、按时间衰减、单值聚合（l=12、l=4）、三值聚合进行比较，报告不同操纵水平下操纵零售商和诚实零售商的销售额。结果显示动态聚合在多数场景下能有效减少虚假评分带来的额外销售，同时仅轻微影响诚实零售商销售。
- Decision: 本文核心目标是提出并验证一种动态评分聚合方法，以降低在线市场中虚假好评对销售额的操纵影响，同时尽量不损害诚实零售商的销售额；这两个核心结果均为模拟市场中可计数的客观销售指标。评价通过模拟研究完成，5.1.1节明确以即时更新作为基准（benchmark），并与折扣、单值聚合、三值聚合等参照方法比较；该基准评价直接支撑了核心改进主张。因此满足客观指标、唯一核心目标和明确benchmark三方面要求，应纳入。
- Confidence: 0.93

## Integrated framework for profit-based feature selection and SVM classification in credit scoring

- Year/journal: 2017 / Decision Support Systems
- DOI: 10.1016/j.dss.2017.10.007
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "利润（Profit）", "measurement_cn": "在验证集上按公式计算：正确识别非违约者的收益（贷款ROI）减去错误接受违约者的损失（LGD×EAD）再减去所选变量来源的获取成本。", "objectivity_reason_cn": "收益、损失和变量获取成本均由贷款金额、利率、期限、违约状态、LGD/EAD及固定获取成本等财务或审计事实确定，不依赖人的感受、语义评价或专家偏好。"}, {"name_cn": "AUC、准确率、变量数、来源数", "measurement_cn": "基于预测分类与实际违约标签计算的AUC和准确率，以及模型中使用的变量数和变量来源数。", "objectivity_reason_cn": "违约标签是外部可核验事实，AUC/准确率由固定统计公式计算，均是客观可测指标。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在智利银行的两个信用评分数据集（NEW和RET）上，将提出的l2l∞-SVM和l1l∞-SVM与Logistic回归、Fisher Score、RFE-SVM、HOSVM_AUC、HOSVM_MPC进行比较。表1和表2显示，以利润为模型选择指标时，提出方法在两类客户上的利润均显著高于所有对比方法；表3和表4在AUC选择下也显示利润优势。该benchmark比较是支撑“利润提升”核心主张的关键证据。
- Decision: 客观指标方面，核心成功指标为利润，由贷款ROI、LGD×EAD和变量获取成本等财务事实直接计算，不依赖主观评价；AUC/准确率也是基于事实标签的客观指标。唯一核心目标是将商业成本收益纳入SVM分类和特征选择并提升利润，全文未提并列的主观或理论核心贡献。Benchmark方面，作者明确使用“benchmark approach”和“benchmarked models”等表述，在实验部分将所提方法与Logistic回归、Fisher、RFE-SVM、HOSVM等多种方法比较，并以利润对比结果支撑核心主张，存在明确参照点。因此两个模块均通过，strict_include=true。
- Confidence: 0.93

## Learning bidding strategies with autonomous agents in environments with unstable equilibrium

- Year/journal: 2008 / Decision Support Systems
- DOI: 10.1016/j.dss.2008.05.005
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "利润（平均利润）", "measurement_cn": "在拍卖仿真中，按最低价卖方获得容量k、剩余需求给高价卖方的规则，以(bid-c)×数量计算每轮利润，再取多次随机种子运行的平均值。", "objectivity_reason_cn": "利润由支付矩阵和报价规则确定性地计算，不依赖人的感受或语义判断。"}, {"name_cn": "利润收敛性（利润方差/标准差）", "measurement_cn": "在最后1000次迭代中统计利润的标准差（表1-5及图8），衡量agent自博弈或互博弈时的收敛性。", "objectivity_reason_cn": "方差是对可审计仿真输出（利润序列）的统计，构念和数值均客观。"}, {"name_cn": "学习策略与Nash均衡策略的欧氏距离", "measurement_cn": "计算agent当前混合策略向量与Nash混合策略向量在10维策略空间中的欧氏距离（表1-3）。", "objectivity_reason_cn": "该距离由已定义的Nash策略向量与学习到策略向量直接计算，是确定性的技术指标。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: Nash payoff（理论基准）
- Benchmark evaluation: 在离散化的两卖方reverse auction仿真中，以Nash payoff为基准，评价GA、Softmax、0.1Greedy三类学习agent；报告其面对纯策略、自我对弈/互相博弈、Nash策略时的利润平均值/标准差和策略到Nash的距离，并在第5节比较有无sliding window protocol的性能改进。
- Decision: 客观指标方面，核心成功标准是利润、利润方差/标准差、策略到Nash均衡的距离，均为仿真中可审计、确定性的技术指标，不涉及人的感知或语义评价；唯一核心目标是证明简单学习agent能学到最优/最佳响应并收敛（即客观性能提升），Nash不稳定性分析仅为问题动机。Benchmark方面，作者在评价语境中明确写出“use the Nash payoff as a benchmark”，并以Nash payoff、最优收益、上界以及无滑动窗口版本为明确比较对象，benchmark结果直接支撑agent学习绩效的核心主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.93

## Leveraging Financial Social Media Data for Corporate Fraud Detection

- Year/journal: 2018 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2018.1451954
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "准确率 (Accuracy)", "measurement_cn": "测试集上十折交叉验证平均预测正确比例", "objectivity_reason_cn": "由模型预测标签与AAER事实性欺诈标签逐项比对计算，不依赖主观评价"}, {"name_cn": "召回率 (Recall)", "measurement_cn": "测试集上十折交叉验证中真实欺诈样本被正确识别的比例", "objectivity_reason_cn": "基于事实性欺诈标签计算，不依赖主观判断"}, {"name_cn": "F1分数 (F1 Score)", "measurement_cn": "精确率与召回率的调和平均，在测试集上以十折交叉验证计算", "objectivity_reason_cn": "由客观分类结果计算，反映分类性能"}, {"name_cn": "AUC", "measurement_cn": "ROC曲线下面积，测试集上以十折交叉验证计算", "objectivity_reason_cn": "基于分类评分与事实性欺诈标签计算，完全客观可复现"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在自建欺诈检测数据集（64家欺诈公司 + 64家匹配非欺诈公司；取自SeekingAlpha文本、财务比率和MD&A）上，作者将提出的社交媒体特征模型与两类基线进行系统比较：仅使用84项财务比率的模型，以及仅使用MD&A语言特征的模型。最优SVM模型在测试集上的准确率75.50%（仅社交媒体特征）和80.00%（全特征组合）；仅财务比率基线最优SVM测试准确率56.17%；仅MD&A语言特征基线最优LR测试准确率70.33%。该比较直接支撑“社交媒体特征能提升公司欺诈检测”的核心主张。
- Decision: 文章以提升公司欺诈检测的客观性能（accuracy/recall/F1/AUC）为唯一核心目标和核心贡献，欺诈标签来自AAER外部事实性执法记录，属于objective_fixed_factual_labels。模型在自建数据集上与仅财务比率、仅MD&A语言特征两类基线进行系统比较，讨论部分明确使用benchmark一词指称该比较，且比较结果用于支持“社交媒体特征提升欺诈检测性能”的核心主张，满足benchmark_comparison_central。适用性检查中的焦点小组主观反馈仅为非核心补充验证，不影响核心目标的客观唯一性。
- Confidence: 0.93

## Managing online sales with posted price and open-bid auctions

- Year/journal: 2013 / Decision Support Systems
- DOI: 10.1016/j.dss.2012.12.005
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "日均收益（average daily revenue/profit）", "measurement_cn": "通过 NetLogo 模拟市场运行，记录固定价格和拍卖渠道的销售收入，并在对于每种设计组合大量重复模拟后取平均值；同时在同一模拟实现中计算仅用固定价格 p 时的收益作为对比基准。", "objectivity_reason_cn": "收益是模拟中按成交价格和数量直接计算出的货币数值，不依赖任何人的满意度、偏好或语义评价；消费者行为模型和估值分布虽含假设，但输出值本身是确定性的客观结果。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 作者在相同模拟环境中以 “only posted price regime” 为基准评价双渠道：每个模拟运行结尾记录双渠道收益，并依据到达消费者估值计算若只采用固定价格 p 时的收益；随后在 Section 7 比较最优双渠道设计与该基准，报告收益提升，并绘制 q-T 空间中的收益提升百分比图（Fig. 6-7）。
- Decision: 客观指标方面：核心指标是日均收益，由模拟中的交易结果直接计算，完全客观，不依赖人类感知或语义判断；核心目标和贡献声明都是提升收益，且未发现并列的主观或理论目标。Benchmark 方面：作者明确将 only posted price regime 的利润作为 benchmark，全文在相同模拟环境中以该基准系统比较双渠道收益提升，结论的核心主张“最优设计下双渠道优于单渠道”正是由该 benchmark 比较支持；比较对象明确（单渠道固定价格等）。因此两个模块均通过，strict_include=true。
- Confidence: 0.93

## Mitigating Exposure Bias for Recommendations in Physical Spaces: An Unbiased Pairwise Ranking Approach Using Spatial Movement

- Year/journal: 2026 / Information Systems Research
- DOI: 10.1287/isre.2023.0100
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "Recall@N", "measurement_cn": "对每条测试访问序列采用 leave-one-out 策略，将序列中最后一次真实到访的门店作为 ground truth；模型对所有候选门店按预测相关度排序，统计 ground truth 门店是否落入前 N 个推荐。数据来自商场视频追踪系统记录的真实门店到访行为。", "objectivity_reason_cn": "真实门店到访是可观测、可审计的行为事实，不依赖用户自评、专家评分或语义质量判断；Recall 由实际访问状态和确定性公式计算。"}, {"name_cn": "DCG@N", "measurement_cn": "对推荐列表中真实门店所在位置按折扣累计增益计算排序质量；同样基于真实门店到访记录和标准 DCG 公式。", "objectivity_reason_cn": "排序位置和真实到访状态均为客观事实，DCG 是确定的计算指标，不涉及人类主观体验或价值判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在真实商场数据（北京大型购物中心，167,234条访问序列、175家门店）上采用 leave-one-out 评价，对候选门店排序并计算 Recall@1/3/5 与 DCG@3/5。作为对照的 benchmark 方法包括 UserKNN、ItemKNN、BPR-MF、FPMC、CoFiSet、Context-BPR、Cat-MPR、Dist-MPR、GRU4Rec、JODIE、SSE-PT 和 Random。结果显示 UMPR 在所有指标上最优，且相对各 benchmark 的改进幅度在表4中一一列出。
- Decision: 客观指标方面：核心评价指标是基于真实门店到访记录的 Recall 与 DCG，数据来源为系统追踪行为，不依赖主观评价或语义判断，四个客观性门全部通过。唯一核心目标方面：研究问题、方法设计、实验评价和贡献声明均围绕“提高物理空间门店推荐性能”这一客观目标展开；增量收入与公平性属于附加分析，不构成并列核心目标。Benchmark 方面：第5.2节明确以 benchmark 一词描述系统化基线比较，并给出多个显式参照点（UserKNN、BPR-MF、GRU4Rec、SSE-PT 等），表4的结果直接支撑 UMPR 的核心性能提升主张，因此 benchmark 四个门全部通过。综上 strict_include=true。
- Confidence: 0.93

## Model identification for ARMA time series through convolutional neural networks

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113544
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "ARMA 阶数正确识别率", "measurement_cn": "在 10,000 条已知真实阶数的模拟 ARMA 时间序列上，分别统计 AR 阶、MA 阶及两者同时正确的百分比，并与真实阶数比对。", "objectivity_reason_cn": "真实阶数由模拟算法确定，识别结果与真实标签的比对是计算事实，不依赖人的感受或语义判断。"}, {"name_cn": "阶数识别均方误差 (MSE)", "measurement_cn": "平均（分类阶数 - 实际阶数）^2，衡量预测阶数离真实阶数的集中程度。", "objectivity_reason_cn": "该值由可审计的阶数差平方平均计算得出，完全客观。"}, {"name_cn": "计算时间", "measurement_cn": "在相同 CPU 单核环境下完成 10,000 条时间序列模型识别所需的小时数。", "objectivity_reason_cn": "处理时间是可直接测量的系统资源消耗。"}, {"name_cn": "预测误差 (MAE/RMSE)", "measurement_cn": "使用各方法识别的 ARMA 模型对后续 1 期和 10 期进行预测，计算与实际生成值的 MAE 和 RMSE。", "objectivity_reason_cn": "预测值与模拟真值之间的误差是确定性计算，不涉及主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在自行生成的 10,000 条模拟 ARMA 时间序列测试套件（长度 1,000、3,000、10,000）上，将 CNN 与 AIC step-wise、AIC full、BIC step-wise、BIC full 进行对比，评价 AR/MA 阶数识别准确率、MSE、计算时间及后续预测 MAE/RMSE。
- Decision: 该文核心目标是用 CNN 在 ARMA 模型阶数识别上提升客观可测的准确率和速度，并改善后续预测误差；全部核心成功指标（识别准确率、MSE、计算时间、MAE/RMSE）都来自确定性的模拟标签与计算，不涉及主观评价。全文存在明确的 performance benchmarking 表述，且基准比较位于结果评价部分，以 AIC/BIC 各变体为参照点证明 CNN 的提升，因此两个模块均通过，strict_include=true。
- Confidence: 0.93

## Prediction uncertainty in collaborative filtering: Enhancing personalized online product ranking

- Year/journal: 2016 / Decision Support Systems
- DOI: 10.1016/j.dss.2015.12.004
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "Top-N 推荐性能：precision 与 recall", "measurement_cn": "在 MovieLens 测试集上，以用户真实评分为 ground truth，将 RPU 与 RCF 生成的 top-N 列表与真实相关产品集合比较，计算 precision 和 recall。", "objectivity_reason_cn": "precision/recall 由推荐列表与真实评分的集合运算直接确定，不需要用户主观评价或语义判断，数值可复现、可审计。"}, {"name_cn": "整体排序质量：nDCG@p", "measurement_cn": "以用户真实评分为相关性得分，按排序位置计算 DCG 并除以理想 DCG，得到 nDCG@p；p=1 到 10 均报告。", "objectivity_reason_cn": "nDCG 是对排序列表与真实评分之间的确定性计算，构念为该方法的排序准确性，不依赖研究者或用户的感受、偏好或质量评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: MovieLens（公开标准电影评分数据集） | RCF（作者明确称为 benchmark ranking approach）
- Benchmark evaluation: 在 MovieLens 数据集上，基于 5 种基础 CF 技术（userKNN、MF、SVD、PMF、BPMF），分别比较 RCF 与两种 RPU 变体（min-max 离散化和 quantile 离散化）的 top-N precision/recall 与 nDCG@p。结果表（Table 3、Table 4）和图 4、图 5 显示 RPU 在所有设定下均优于 RCF 基准；稀疏数据实验亦显示改善。
- Decision: 客观指标部分：文章核心目标是提升个性化产品排序的准确性，全部核心成功指标为 precision、recall 和 nDCG，均基于 MovieLens 真实评分可确定性计算，不依赖主观评价或人类语义判断；除排序准确性提升外没有并列的核心贡献。benchmark 部分：作者在实验评价语境中明确将 RCF 称为 benchmark ranking approach，并将 5 种 CF 技术用作 benchmarks，在 MovieLens 上系统比较 RPU 与 RCF，结果表显示明确提升，属于支撑核心改进主张的基准比较。因此两个模块均通过，strict_include=true。
- Confidence: 0.93

## Recommendations Using Information from Multiple Association Rules: A Probabilistic Approach

- Year/journal: 2015 / Information Systems Research
- DOI: 10.1287/isre.2015.0583
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "推荐准确率（successful recommendations / accuracy）", "measurement_cn": "在三个真实交易数据集上做五折交叉验证；每个测试交易被逐步构造成购物篮，推荐系统推荐一个商品，若该商品出现在交易剩余部分则记为一次成功推荐；最终计算成功推荐数占推荐篮数的百分比。", "objectivity_reason_cn": "推荐是否成功由真实交易记录中商品是否出现决定，是可审计事实，不依赖用户或专家的主观评价、偏好或语义判断。"}, {"name_cn": "推荐运行时间", "measurement_cn": "在 Pentium Dual Core 2.6GHz、32GB RAM 的桌面机上，记录每次推荐的平均耗时（毫秒或秒）。", "objectivity_reason_cn": "运行时间是可客观测量的物理量，不依赖人的感知或体验。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: Retail (FIMI repository) | BMS-POS (FIMI repository) | comScore2013 (WRDS)
- Benchmark evaluation: 在 Retail、BMS-POS、comScore2013 三个真实数据集上，通过五折交叉验证将 MLR 与 Zaïane (2002)、Wang and Shao (2004)、Baralis et al. (L3G)、Li et al. (CMAR)、Lin et al. (2002)、item-based collaborative filtering 和 FunkSVD 等基准方法比较推荐准确率和时间；结果显示 MLR 在大多数设置下准确率更高。
- Decision: 文章的核心目标是提出 MLR 方法，通过组合多条关联规则提升推荐准确率，并用真实交易数据上的准确率和运行时间作为核心评价指标；两者均为客观可测量结果，不存在用户满意度、质量评价等主观核心指标。全文在摘要、引言和实验部分明确使用 benchmark 一词，将 MLR 与多个规则方法、协同过滤和矩阵分解等基准比较，benchmark 比较直接支持核心准确率提升主张。因此客观指标、唯一核心目标和 benchmark 三个门槛全部满足。
- Confidence: 0.93

## Software Diversity for Improved Network Security: Optimal Distribution of Software-Based Shared Vulnerabilities

- Year/journal: 2017 / Information Systems Research
- DOI: 10.1287/isre.2017.0722
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "epidemic threshold（流行阈值）", "measurement_cn": "通过扩展SIS病毒传播仿真模型迭代计算：令病毒传播率λ=β/δ，在感染率和消毒率之间搜索使感染从系统中消失或持续的临界值，直至两次连续VSR差值小于0.0001，并取20次重复的平均值。", "objectivity_reason_cn": "该值由网络拓扑、软件-漏洞矩阵、感染/消毒过程和仿真规则计算得出，是可复核的系统状态数值，不依赖人的感受、意义理解或价值判断。"}, {"name_cn": "Software Diversity Index（SDI，软件多样性指数）", "measurement_cn": "基于节点-漏洞矩阵（NVM）与Shannon熵公式计算，并以最大可能值标准化到0-1区间。", "objectivity_reason_cn": "SDI由确定性数学公式和软件-漏洞矩阵数据计算，反映节点间共享漏洞的分布结构，是客观可复核的量化指标。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在软件多样性实验（Section 4.2）中，作者将LP1/LP2的SDI与targeted distribution的SDI比较，报告于Tables 3-5；在病毒传播实验（Section 4.3）中，将LP2与targeted distribution的epidemic threshold比较，报告于Figure 5和Table 6。结果显示LP模型在几乎所有实验条件下均优于基准策略，例如1,000节点、1-connectivity、SSI 5%情形下epidemic threshold从2.3提升到12.0及以上。
- Decision: 客观指标方面，SDI和epidemic threshold均为确定性计算/仿真产生的客观数值，不涉及人类主观评价；评价结构、研究问题和贡献声明均围绕提升网络安全性（通过提高SDI和epidemic threshold）展开，属于完全客观指标且为唯一核心目标。Benchmark方面，作者在实验部分明确使用“For benchmarking purposes”将targeted distribution作为基准，并在SDI和epidemic threshold两个核心评价中与LP模型对比，基准比较直接支撑了核心提升主张，且存在明确参照点。因此两个模块均通过，strict_include=true。
- Confidence: 0.93

## Using 3D interfaces to facilitate the spatial knowledge retrieval: a geo-referenced knowledge repository system

- Year/journal: 2005 / Decision Support Systems
- DOI: 10.1016/j.dss.2004.01.007
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "任务完成正确性（effectiveness）", "measurement_cn": "受试者完成7个空间知识检索任务，答对记1分或按正确比例计分；所有答案由系统/研究者依据客观事实判定正误。", "objectivity_reason_cn": "每个任务都有确定的事实答案，如地点是否存在、某类别是否有文档、哪个类别文档更多、某地点是否在城区等，不依赖受试者的感受、偏好或语义评价。"}, {"name_cn": "任务完成时间（efficiency）", "measurement_cn": "记录每个受试者完成每个任务所需的时间。", "objectivity_reason_cn": "时间为系统/实验者直接记录的可审计客观量，不涉及主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 2D system（文中称为 benchmark system）
- Benchmark evaluation: 作者在系统评价部分构建了一个2D基准系统，与3D系统在7个任务上比较，覆盖3种空间知识与3类界面；主要结果见表3，其中任务2（路径知识）和任务6（组合界面的configurational knowledge）中3D显著优于2D，其余任务无显著差异。
- Decision: 该文以“带交互动画的3D界面是否能达到或超过2D界面的空间知识检索性能”为核心问题，核心成功指标是任务完成正确性和完成时间，均为客观可审计结果；全文不存在主观满意度、偏好或质量评价作为核心成功标准。评价部分明确将2D系统作为benchmark system，并在多个任务上与3D系统比较有效性和效率，benchmark评价直接支撑核心性能主张。因此同时满足客观指标、唯一核心目标和明确benchmark表述三重条件。
- Confidence: 0.93

## What Will Be Popular Next? Predicting Hotspots in Two-Mode Social Networks

- Year/journal: 2021 / MIS Quarterly
- DOI: 10.25300/misq/2021/15365
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "Top-K 精确率 (Precision at K)", "measurement_cn": "将预测的未来热门社会焦点排名与真实未来排名（基于未来实际签到数/添加数）比较，计算前K个重叠比例。", "objectivity_reason_cn": "真实排名来自平台日志中可审计的签到或书籍添加次数，不依赖人的感受或语义评价。"}, {"name_cn": "平均精确率 (AP)", "measurement_cn": "在预测排名列表中逐位计算精确率并取平均，真实标签仍是未来实际采纳次数形成的排名。", "objectivity_reason_cn": "排名基准为外部可观察行为计数，计算规则固定且可复现。"}, {"name_cn": "AUC", "measurement_cn": "判断随机选择的一个真实Top-K焦点是否比随机选择的非Top-K焦点在预测排名中更靠前。", "objectivity_reason_cn": "正负标签由未来实际签到/添加次数是否进入Top-K决定，非主观分类。"}, {"name_cn": "Kendall Tau 系数", "measurement_cn": "衡量预测排名与真实未来排名之间逐对顺序一致性。", "objectivity_reason_cn": "真实排名依据未来可观测的采纳次数，指标计算无需主观判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在三个真实数据集（Dianping、Gowalla、图书阅读社交平台）上，将GLMR与PageRank、HITS、线性阈值LT、多路径异步阈值MAT、两模链路预测LP、协同过滤CF、基线线性回归BLR、基线持久性BPM共八个基准方法比较；采用Precision、AP、AUC、Tau四项排序指标。结果表8-10显示GLMR在全部数据集和指标上均优于所有参照方法。
- Decision: 本文核心目标是预测未来社会焦点的流行度排名，所有主要成功指标均为基于未来可观察采纳次数（签到/书籍添加）计算的排序指标，完全客观且为唯一核心目标；评价以三个数据集上的八种基准方法对比为核心证据，存在明确、位于评价语境且支持核心提升主张的 benchmark 表述，并有明确的参照点比较。因此 strict_include=true。
- Confidence: 0.93

## A Computational Analysis of Linear Price Iterative Combinatorial Auction Formats

- Year/journal: 2009 / Information Systems Research
- DOI: 10.1287/isre.1070.0151
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "配置效率", "measurement_cn": "最终分配的总竞买人估值总和与有效分配的总估值总和之比，即 E(X)=Σv_i(allocated)/Σv_i(X*)，由模拟中的真实估值与分配结果计算", "objectivity_reason_cn": "该指标基于给定的估值函数和最终分配结果计算，不依赖任何人类感受、语义判断或主观评价，完全可由系统日志和确定规则复现"}, {"name_cn": "拍卖方收入份额", "measurement_cn": "拍卖方最终收入占有效分配总估值总和的比例，即 R(X)=Σb_i(S)/Σv_i(X*)，由模拟中的成交价格与估值计算", "objectivity_reason_cn": "收入份额由模拟中的实际成交价格和估值计算，属于可审计的交易金额，不涉及主观体验"}, {"name_cn": "竞买人收入份额", "measurement_cn": "配置效率减去拍卖方收入份额，即 E(X)-R(X)，表示竞买人获得的总剩余占比", "objectivity_reason_cn": "由两个客观指标推导而来，同样是可计算的客观事实"}, {"name_cn": "拍卖轮数", "measurement_cn": "模拟拍卖从开始到终止所经历的轮数，直接记录于拍卖处理器日志", "objectivity_reason_cn": "轮数是可观测的系统过程数据，不依赖人类判断"}, {"name_cn": "价格非单调性", "measurement_cn": "价格下降量之和与价格上升量之和的比值，用于量化线性价格在拍卖过程中的波动性，由每轮各物品价格变化计算", "objectivity_reason_cn": "该指标基于价格序列的数值变化，属于可验证的计算结果"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: Combinatorial Auctions Test Suite (CATS) value models | pairwise synergy value model (An et al. 2005)
- Benchmark evaluation: 文章在 CATS 价值模型（包括交通、匹配、房地产等）以及 pairwise synergy 价值模型上生成了多种拍卖估值实例，对 CC、RAD、RADne、ALPS、ALPSm 等拍卖格式进行离散事件模拟，并以配置效率、拍卖方收入份额、轮数、价格非单调性等指标进行系统化基准比较。例如，Table 1 报告了 7 种价值模型下 40 组实例的平均效率：ALPSm 效率最高（98.81%-99.82%），ALPS 次之（92.8%-98.26%），CC 居中（96.24%-99.87%），RAD 效率最低（69.9%-90.09%）。同时设置 VCG 作为理论基准（效率 100%，收入作为竞争水平指示）。这些 benchmark 结果为证明 ALPSm 等设计在配置效率上的提升提供了核心证据。
- Decision: 客观指标方面：文章的全部核心成功指标为配置效率、收入分配、轮数、价格非单调性等，均由模拟计算客观得出，不依赖人类感知、语义判断或主观评价；研究问题、评价结构和贡献声明均以这些客观指标的提升为中心，且未发现并列的核心目标。Benchmark 方面：摘要和 §3.4 明确使用 'benchmark' 一词陈述系统化基准评价，并采用公开的 CATS 测试套件作为价值模型评价场地；模拟实验将 CC、RAD、ALPS、ALPSm 等格式与 VCG 基准在不同价值模型上进行比较，结果直接支撑 ALPSm 在配置效率上的提升主张。因此两个模块均通过，strict_include 为 true。
- Confidence: 0.92

## A GIS supported Ant algorithm for the linear feature covering problem with distance constraints

- Year/journal: 2006 / Decision Support Systems
- DOI: 10.1016/j.dss.2005.09.002
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "目标A：线性要素覆盖率 μ_A", "measurement_cn": "基于GIS栅格化，将SCDF路线转为25m微单元；统计在临界距离R=3.03km内被至少一个消防站覆盖的路线单元数，除以全部路线单元数1967；采用全有全无覆盖规则。", "objectivity_reason_cn": "覆盖率只依赖空间坐标、距离和栅格覆盖计数，不涉及人的感受、语义或价值判断。"}, {"name_cn": "目标B：距离均衡达成度 μ_B", "measurement_cn": "计算每个新设施与其最近设施（含现有设施）的欧氏距离 d_l，与期望距离D=5.0km及上下界9.0/1.0km比较，按分段线性隶属函数计算；最终取所有设施中的最小值。", "objectivity_reason_cn": "距离值由地理坐标和既定距离约束确定性计算，是物理可审计事实，不含主观评价。"}, {"name_cn": "综合目标 λ", "measurement_cn": "模糊多目标模型取 λ=max min(μ_A, μ_B)；表1和表2报告8次独立运行的λ值、AVE(λ)和CoV(λ)，作为算法比较的主要指标。", "objectivity_reason_cn": "λ由两个客观子目标的隶属函数最小化得到，是几何和距离约束的确定性函数，不依赖人类体验或语义评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在相同的新加坡消防站选址案例上，以8次独立运行、相同3600s时间长度，比较LFCP-Ant（LS）与TC-GA、RANDOM和LFCP-Ant（LS2）。结果显示LFCP-Ant（LS）平均λ=0.633，优于TC-GA的0.505（提升25.35%）；最优λ=0.650，优于TC-GA的0.541（提升20.15%）；变异系数2.20%低于TC-GA的3.82%；收敛曲线也显示LFCP-Ant更优。该比较是支撑‘LFCP-Ant更高效、更稳健’核心主张的关键证据。
- Decision: 客观指标方面：核心成功指标是LFCP的线性要素覆盖率和设施间距离均衡度及其综合λ，均由空间坐标、距离和栅格覆盖计数确定性计算，不依赖人类感受或语义判断；全文评价和贡献声明都围绕λ提升展开，属于完全客观且唯一的算法优化目标。Benchmark方面：作者在第5.4节以‘benchmarking the LFCP-Ant’明确陈述系统化基准比较，并将LFCP-Ant与TC-GA、RANDOM等明确参照物在相同案例和运行条件下比较，结果直接证明LFCP-Ant在λ、稳定性和收敛性上的提升，因此benchmark评价是核心证据。两个模块均通过，strict_include=true。
- Confidence: 0.92

## A Multi-criteria Convex Quadratic Programming model for credit data analysis

- Year/journal: 2008 / Decision Support Systems
- DOI: 10.1016/j.dss.2007.12.001
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "分类准确率（总体、Normal类、Bad类）", "measurement_cn": "10折交叉验证下，根据预测类别与真实类别（Normal/Bad）比较，计算正确分类比例。", "objectivity_reason_cn": "标签为外部可核验的信用状态（正常/违约），准确率由分类结果统计得出，不依赖人的感受或语义评价。"}, {"name_cn": "Type I 和 Type II 错误率", "measurement_cn": "基于混淆矩阵计算：Type I=FN/(FN+TN)，Type II=FP/(FP+TP)，由10折交叉验证结果汇总。", "objectivity_reason_cn": "错误率由类别事实计算，反映分类性能，完全客观。"}, {"name_cn": "KS score", "measurement_cn": "计算Bad类与Normal类累计分布之差的最大值。", "objectivity_reason_cn": "基于类别分布统计，客观可计算。"}, {"name_cn": "相关系数（Correlation coefficient）", "measurement_cn": "由混淆矩阵元素按公式计算，用于衡量预测与真实标签的一致性。", "objectivity_reason_cn": "基于事实标签和预测结果的统计量，客观可复算。"}, {"name_cn": "计算时间", "measurement_cn": "在合成大规模数据集（1亿条记录）上记录10折交叉验证的平均训练时间（如711.3秒）。", "objectivity_reason_cn": "直接的系统日志计时，物理可测量。"}, {"name_cn": "可扩展性/数据集规模", "measurement_cn": "在大规模合成数据集（O(10^9)）上的可行性及算法迭代过程。", "objectivity_reason_cn": "数据集大小和处理能力是可审计的规模事实。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: German credit card application dataset (UCI Machine Learning databases)
- Benchmark evaluation: 在四个信用数据集（German, Australian, Japanese, US bank）上，通过10折交叉验证，将MCQP与LDA、See5、SVMlight、LibSVM在总体准确率、类内准确率、Type I/II错误、KS分数、相关系数五个指标上进行比较。结果显示MCQP在Japanese集上所有指标最佳，在US集上Bad准确率与Type I错误最佳，在German和Australian集上表现高于平均水平。
- Decision: 文章核心目标是提出并验证高效、可扩展的MCQP分类模型，评价指标包括分类准确率、错误率、KS分数、相关系数和计算时间，全部为完全客观的可测量结果；标签为外部可核验的信用状态（Normal/Bad），属于固定事实标签。全文无主观构念或语义评价作为成功标准。实验部分明确将German文档集称为benchmark set（来自UCI），并明确使用四个著名基准分类工具作为参照进行比较，比较结果直接支撑MCQP的分类性能与效率主张。因此客观指标与唯一核心目标、benchmark门槛均满足。
- Confidence: 0.92

## A Novel Recommendation Model for Online-to-Offline Service Based on the Customer Network and Service Location

- Year/journal: 2020 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2020.1759927
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "F-Score", "measurement_cn": "在保留的测试评分/服务使用记录上，根据Top-30推荐列表计算F-Score；数据来源为Dianping O2O数据与MovieLens 100K的留出测试集", "objectivity_reason_cn": "推荐是否命中用户实际使用/评分的服务，由历史行为记录和固定公式客观计算，不依赖受访者主观评价"}, {"name_cn": "Precision", "measurement_cn": "Top-30推荐列表中命中测试集实际使用服务的比例；由留出评分矩阵确定", "objectivity_reason_cn": "命中与否是外部可核验的行为事实，计算过程完全确定"}, {"name_cn": "Recall", "measurement_cn": "测试集中用户实际使用服务被Top-30推荐列表覆盖的比例；由留出评分矩阵确定", "objectivity_reason_cn": "覆盖对象是实际发生的服务选择事实，计算客观"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: MovieLens 100K
- Benchmark evaluation: 在MovieLens 100K上，将CNLRec和CNRec与广泛使用的CF方法及MF、DL、CL、NN等state-of-the-art方法比较，报告不同训练集密度下的F-Score、Precision、Recall；结果显示CNRec/CNDRec在低密度数据上显著优于基线方法。O2O Dianping数据也用于同类比较。
- Decision: 客观指标方面，核心成功指标为F-Score、Precision、Recall，基于留出评分/服务使用记录客观计算，不依赖用户主观评价，且客观指标提升是全文唯一核心目标与贡献；benchmark方面，文章在Experiments中明确使用公开标准数据集MovieLens 100K作为评价场地，并与CF、MF、DL、CL、NN等显式基线比较，比较结果直接支撑CNLRec/CNRec的核心性能提升主张。两个模块均通过，因此strict_include=true。
- Confidence: 0.92

## A hybrid decision support system for adaptive trading strategies: Combining a rule-based expert system with a deep reinforcement learning strategy

- Year/journal: 2024 / Decision Support Systems
- DOI: 10.1016/j.dss.2023.114100
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "累计回报率 (%AR)", "measurement_cn": "模拟交易期末资产价值相对初始投资的百分比变化", "objectivity_reason_cn": "基于市场数据决定的买卖价格、持仓数量和资产价值客观计算，不涉及人的感受或语义判断。"}, {"name_cn": "夏普比率 (SR)", "measurement_cn": "年化超额收益除以年化波动率", "objectivity_reason_cn": "基于可审计的收益序列和波动率计算，用于衡量风险调整后收益，完全客观。"}, {"name_cn": "最大回撤 (MDD)", "measurement_cn": "交易期间资产价值从峰值到谷值的最大跌幅", "objectivity_reason_cn": "从模拟交易产生的资产价值序列中直接计算，不依赖任何主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在 S&P500 指数基金及另外五个指数基金（NYSE Composite、DAX、CAC40、Hang Seng、KOSPI）上，将提出的混合模型与 B&H、RB、RL、RB+RL、RB+RL+C1、RB+RL+C1+C2 等模型变体，以及 TI+SVM、TI+RF、TI+LSTM、TI+XGBoost+CNN+LSTM 等先前混合模型进行比较，报告 %AR、年度夏普比率、最大回撤等客观财务指标。整体测试期及不同市场情景（market crash、uptrend、downtrend）均显示提出的混合模型在多数核心指标上优于基准。
- Decision: 客观指标门槛通过：核心成功指标为累计回报率、夏普比率、最大回撤、交易信号数量等，均基于市场数据和模拟交易客观计算，不依赖人类感受或语义判断；唯一核心目标为提升这些客观财务指标，全文没有并列的主观或理论性成功标准。Benchmark 门槛通过：作者明确使用“benchmark”一词，在 5.4.2 节明确选择对比基准（TI+SVM、TI+RF、TI+LSTM、TI+XGBoost+CNN+LSTM 等），并在多个基准指数基金上开展系统化比较，结果用于支撑核心性能提升主张；比较具有明确参照点（B&H、RB、RL、模型变体、先前混合模型），报告了提升而非孤立数值。两个模块均通过，strict_include=true。
- Confidence: 0.92

## A multivariate approach for top-down project control using earned value management

- Year/journal: 2015 / Decision Support Systems
- DOI: 10.1016/j.dss.2015.08.002
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "AUC（由检测性能与过度反应概率整合的曲线下面积）", "measurement_cn": "在第二阶段 Monte Carlo 模拟中，计算 T2/SPE 控制图在不同容忍限下对活动层非受控状态的检出率（检测性能）和误报率（过度反应概率），并按不同 α 阈值积分得到 AUC", "objectivity_reason_cn": "受控/非受控状态由 Kolmogorov-Smirnov 统计量对模拟活动工期分布的事后检验确定，警告信号由控制图算法产生，二者均为确定性计算，不依赖人的感受、语义或价值判断"}, {"name_cn": "检测性能 (detection performance)", "measurement_cn": "对不符合预定受控状态的项目执行样本，控制图在项目周期内发出警告的比例", "objectivity_reason_cn": "基于模拟项目执行是否通过 K-S 检验这一确定性类别，客观可复算"}, {"name_cn": "过度反应概率 (probability of overreaction)", "measurement_cn": "对符合预定受控状态的项目执行样本，控制图错误发出警告的比例", "objectivity_reason_cn": "同样基于确定性分类标签和算法信号"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 作者自建了一个由 RanGen 生成的 900 个 30 活动项目组成的 benchmark set，用 Monte Carlo 模拟生成 EVM/ES 数据；在第一阶段建立受控参考，第二阶段评估 T2/SPE 控制图的检出性能与过度反应概率并计算 AUC；结果与 Colin & Vanhoucke (2014) 的单变量 X、R 控制图进行比较（Fig. 4-7），显示多变量方法在各类场景下 AUC 更高。
- Decision: 该文的唯一核心目标是提出并验证基于 PCA 的多元 EVM/ES 项目进度控制指标 T2/SPE，核心成功指标是模拟项目基准集上的检测性能/过度反应概率合成的 AUC，属于客观可计算的操作性分类性能指标；全文没有将主观量表作为核心成功标准，也没有并列理论或治理贡献。Benchmark 方面，作者在实验设计部分明确构建了 project benchmark set，并在第6节把方法与 Colin & Vanhoucke (2014) 的单变量 X/R 方法进行比较，benchmark 结果直接支持核心改进主张。因此两模块均通过。
- Confidence: 0.92

## A technique for determining relevance scores of process activities using graph-based neural networks

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113511
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "AUC_ROC", "measurement_cn": "十折交叉验证下，基于模型预测概率与事实标签计算得到的ROC曲线下面积", "objectivity_reason_cn": "标签为外部可核验事实（贷款是否接受、是否拒绝、是否超支、是否按时维修），不依赖人的感受或语义评价"}, {"name_cn": "灵敏度 (Sensitivity/TPR)", "measurement_cn": "混淆矩阵中真正例率，基于预测结果与事实标签计算", "objectivity_reason_cn": "基于事实标签的统计量，可审计"}, {"name_cn": "特异度 (Specificity/TNR)", "measurement_cn": "混淆矩阵中真负例率，基于预测结果与事实标签计算", "objectivity_reason_cn": "基于事实标签的统计量，可审计"}, {"name_cn": "去除最相关/最不相关活动后的AUC变化", "measurement_cn": "从sp2020数据集中删除最相关或最不相关活动后，重新训练模型并计算AUC，比较变化", "objectivity_reason_cn": "AUC不变式基于事实标签和预测结果的客观计算，用于验证相关性分数的忠实性"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在四个真实事件日志（bpi2017w、bpi2018al、bpi2020pl、sp2020）上，将GRM与三个基准（BiLSTM、Random Forest、XGBoost）比较AUC_ROC、灵敏度和特异度；Table 3显示GRM在所有数据集上的AUC_ROC均优于三个基准，并在多个特定类别的灵敏度/特异度上显著更好，用于支撑GRM具有可竞争的预测质量，从而支持相关性分数的忠实性。
- Decision: 客观指标：核心评估指标为预测质量（AUC、灵敏度、特异度以及去掉最相关/不相关活动后的AUC变化），均基于外部事实标签计算，完全客观。唯一核心目标：论文的核心目标是设计GRM技术并验证其相关性分数的忠实性，定量评估围绕客观预测质量展开；案例研究仅为辅助效用展示，不构成并列核心成功标准。Benchmark：在4.2 Setup中明确使用'As a benchmark, we use three state-of-the-art ML algorithms...'，属于评价语境，并将GRM与BiLSTM、RF、XG在四个真实事件日志上比较，结果用于支持核心预测质量/忠实性主张；具有明确比较器。因此满足全部条件，strict_include=true。
- Confidence: 0.92

## An intelligent decision support system prototype for hinterland port logistics

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2019.113227
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "总运输成本", "measurement_cn": "由仿真模型求解DCVRPTW优化后，按时间成本、距离成本和车辆固定成本汇总各agent成本，并与现状基准比较计算节约百分比。", "objectivity_reason_cn": "成本由车辆行驶时间、距离、固定费用等可审计运营参数计算，不依赖人的主观评价或语义判断。"}, {"name_cn": "总行驶距离与总行驶时间", "measurement_cn": "仿真输出的车辆在时间依赖路网上的行驶距离和时间，使用ArcGIS/Google矩阵生成并作为绩效指标。", "objectivity_reason_cn": "距离和时间是物理可测量、可核验的技术指标。"}, {"name_cn": "车队规模、车辆利用率与总出行次数", "measurement_cn": "优化模型选择的最少车辆数、车辆类型及总出行次数，用于衡量合作和共享带来的利用效率。", "objectivity_reason_cn": "车辆数和出行次数是系统日志/仿真输出中的可计数事实。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在Port of Brisbane两周真实集装箱移动数据构建的现状基准上，比较维持现状、个体最优计划、合作最优计划等方案；报告总运输成本、时间、距离、车队规模和出行次数，并展示RL学习后各agent的成本分布和PCS使用概率收敛。该benchmark用于支持核心的成本/距离节约主张。
- Decision: 客观指标方面，核心成功指标为总运输成本、距离、时间、车辆利用率和出行次数等可审计/可计量输出，不依赖主观评价，且全文围绕这些指标的提升展开；唯一核心目标被判定为客观成本/效率提升，agent-based模型是实现该目标的工具而非并列贡献。benchmark方面，作者在方法中明确以现状（status quo）作为benchmark，并在结果部分用该benchmark比较不同DSS方案，比较结果直接支持核心的成本/距离节约主张，满足陈述式benchmark门槛。因此两个模块均通过，strict_include=true。
- Confidence: 0.92

## Anonymizing and Sharing Medical Text Records

- Year/journal: 2017 / Information Systems Research
- DOI: 10.1287/isre.2016.0676
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "隐私披露风险（唯一重识别记录数与平均重识别风险）", "measurement_cn": "在匿名化后的数据上，根据QID属性profile（年龄、入院年月等）计算可唯一识别记录的数量/比例，以及公式(6)定义的平均重识别风险 1/(1+n_i)。数据来源是i2b2数据集和DAST/SH/k-anonymity处理后的输出。", "objectivity_reason_cn": "构念是重识别风险，依赖于记录间QID取值的客观计数，不依赖人的感受或语义评价；计算方式确定、可审计。"}, {"name_cn": "数据效用（月份计数查询错误率、大项集支持度误差、搜索查询评分、医院计数错误率）", "measurement_cn": "将匿名化数据与原始数据在计数查询、关联规则大项集、关键词检索等任务上比较，使用公式(7)(8)(9)(10)计算误差或相似度。数据来源为i2b2数据集及系统输出。", "objectivity_reason_cn": "效用通过可重复执行的查询/挖掘结果与原始数据结果的数值差异衡量，不涉及专家评分或主观质量判断。"}, {"name_cn": "信息抽取性能（召回率、精确率、F值）", "measurement_cn": "在i2b2 Medication数据集的PHI标注上评估对Patient Name、Admission Date、Age三类信息的提取效果，使用标准recall/precision/F-measure。", "objectivity_reason_cn": "标注表示的是文本中是否出现PHI类别（固定事实标签），判定不依赖人的主观满意度，属于可核验的事实分类性能。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: i2b2 Medication data set | i2b2 Obesity data set | i2b2 VA data set
- Benchmark evaluation: 在i2b2三个公开数据集上，将DAST原型系统与HIPAA Safe Harbor实现和k-anonymity方法进行比较。隐私风险方面比较唯一重识别记录数和平均重识别风险；数据效用方面比较月份计数查询错误率、大项集支持度误差、搜索查询评分和医院计数错误率。结果显示DAST在绝大多数比较中显著优于SH和k-anonymity（报告α=0.01或0.001显著性）。
- Decision: 客观指标方面：全文核心成功标准是重识别风险和数据效用，均由可审计的计数和下游任务误差衡量，不依赖主观评分或语义评价；信息抽取性能基于i2b2的事实标签，同样客观。唯一核心目标方面：研究问题、设计目标和贡献均围绕降低披露风险并提升数据效用展开，没有与客观改进并列的主观、理论或政策目标。Benchmark方面：作者明确将公开的i2b2标准数据集作为评价场地，并在该场地上将DAST与SH和k-anonymity进行系统化比较，benchmark结果直接支撑核心改进主张；有明确参照点SH和k-anonymity。因此两个模块全部通过，strict_include为true。
- Confidence: 0.92

## Combining Information Seeking Services into a Meta Supply Chain of Facts

- Year/journal: 2008 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00154
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "精确答案MRR（Mean Reciprocal Rank）", "measurement_cn": "将系统生成的精确答案与TREC 2004官方正确答案正则表达式进行自动匹配，按前20个答案中第一个正确答案的倒数排名计分；所有问题得分的均值为MRR。", "objectivity_reason_cn": "正确性由TREC官方的事实答案标签确定，不依赖用户满意度、偏好或语义质量评价；计算方式为确定性自动匹配。"}, {"name_cn": "句子级MRR", "measurement_cn": "检查返回的排序句子中第一条包含正确事实答案的句子的排名，同样使用官方正确答案正则自动判断。", "objectivity_reason_cn": "判断标准是句子是否包含官方固定的事实答案，属于外部事实标签的自动核对，不涉及人类主观评分。"}, {"name_cn": "响应时间/等待时间", "measurement_cn": "通过处理日志和时间戳估计各服务的响应时间，并模拟超时策略下的平均总等待时间。", "objectivity_reason_cn": "由系统日志可审计地记录和计算，属于可客观测量的时间指标。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: TREC 2004 factoid question set（Text Retrieval Conference公开QA任务）
- Benchmark evaluation: 在TREC 2004的200道factoid问题上评价meta fact seeking engine，报告精确答案MRR和句子级MRR；完整meta配置的MRR为0.484（精确）和0.630（句子级），并将其与每个单一服务（START、AskJeeves、BrainBoost、ASU QA、Wikipedia）、关键词门户（Google、MSN、Google+MSN）以及排除/消融配置进行比较。
- Decision: 该文核心目标是构建和验证一种元事实检索引擎，通过组合多个在线事实服务提升答案准确性、响应时间与鲁棒性。所有核心研究问题均围绕可客观测量的MRR和响应时间，评价在TREC 2004公开QA任务上进行，并以完整meta配置对比单一服务、关键词门户和消融配置，给出统计显著性。因此满足客观指标唯一核心目标和明确benchmark评价门槛。
- Confidence: 0.92

## Computational intelligent hybrid model for detecting disruptive trading activity

- Year/journal: 2017 / Decision Support Systems
- DOI: 10.1016/j.dss.2016.09.003
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "AUC（ROC曲线下面积）", "measurement_cn": "在注入已知异常交易样本的NASDAQ真实tick数据上，比较混合模型与kNN/GMM/LR基准模型的ROC-AUC", "objectivity_reason_cn": "检测目标是固定的事实标签（是否属于注入的disruptive trading行为），AUC根据模型输出与已知标签确定性计算，不依赖人的感受或语义质量评价"}, {"name_cn": "Recall、Precision、F measure、G score", "measurement_cn": "在三个实验组（单订单、多订单、混合）四个股票数据集上报告混淆矩阵派生指标", "objectivity_reason_cn": "这些指标由模型预测与已知固定事实标签比对得到，计算客观，构念为金融欺诈/异常交易检测，不涉及主观体验"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在NASDAQ四只股票（Google、Microsoft、Intel、Apple）2013年真实tick数据上，按三组实验注入合成/复现的异常样本，将混合模型与kNN、GMM、LR三个基准模型进行系统对比，报告Recall、Precision、F measure、G score及ROC-AUC；混合模型在所有数据集和实验组上均取得最高AUC。
- Decision: 客观指标方面：核心成功指标为检测性能（AUC、Recall、Precision、F/G），标签为固定事实类别的disruptive trading行为，不依赖主观感受，指标客观且是唯一核心目标。Benchmark方面：作者在实验部分明确以kNN/GMM/LR为benchmark模型，系统比较并在核心提升主张中使用这些基准结果，具有明确参照点。二者均通过，因此strict_include=true。
- Confidence: 0.92

## Depicting Risk Profile over Time: A Novel Multiperiod Loan Default Prediction Approach

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/17491
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "时间至违约预测性能（C-index、IBS、月度AUC）", "measurement_cn": "基于平台实际还款记录定义的违约（逾期超过30天）与违约时间，通过10次10折交叉验证计算C-index、IBS和每月AUC。", "objectivity_reason_cn": "违约状态和违约时间来自可审计的还款系统记录，不依赖人的感受、语义或价值判断；预测性能指标由固定计算公式得出。"}, {"name_cn": "多时点区分性能（AUC、KS、H-measure）", "measurement_cn": "在贷前和贷后阶段多个时间窗口，用预测违约概率对借款人的风险排序能力，计算AUC、KS、H-measure。", "objectivity_reason_cn": "评估对象是真实违约标签和预测概率排序，均为可核验事实；不存在主观评分或偏好判断。"}, {"name_cn": "授信绩效（Granting Performance）", "measurement_cn": "模拟银行按预测风险排序选择不同授信比例下的贷款，统计实际违约贷款数量。", "objectivity_reason_cn": "违约数量直接来自真实还款记录和模拟授信决策，属于可审计的客观结果。"}, {"name_cn": "盈利绩效（Profitability Performance）", "measurement_cn": "模拟投资者按不同策略选择贷款组合，计算组合平均回报率。", "objectivity_reason_cn": "回报率由实际利率、真实违约状态和违约时间计算，不依赖任何主观判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在来自某大型在线借贷平台的真实数据集上，将HACS与7种基准方法（COX、MCM、MTLSA、RSF、BR、CC、NS）在时间至违约预测、多时点区分性能、授信绩效和盈利绩效等多个层面进行系统比较，结果显示HACS在客观指标上全面优于这些基准方法。
- Decision: 客观指标方面：核心指标为C-index、IBS、AUC、KS、H-measure、授信违约数和组合回报率，均基于真实还款记录和固定计算规则，完全客观。唯一核心目标方面：研究问题、设计目标、实验评价和贡献声明均围绕HACS提升多期违约预测和信贷决策的客观绩效展开，全文不存在并列的主观结果或理论机制解释作为核心成功标准。benchmark方面：作者明确使用benchmarked methods表述，并在实验设计、结果表和显著性检验中将HACS与COX、MCM、MTLSA、RSF、BR、CC、NS等既有方法比较，benchmark评价直接支撑核心绩效提升主张，且存在明确参照点。因此满足strict_include。
- Confidence: 0.92

## Detect potential relations by link prediction in multi-relational social networks

- Year/journal: 2018 / Decision Support Systems
- DOI: 10.1016/j.dss.2018.09.006
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "AUC", "measurement_cn": "在10折交叉验证中，将预测出的相似度分数对已有边和非存在边进行排序，按公式(23)计算AUC。", "objectivity_reason_cn": "基于网络中存在或不存在的边这一客观事实标签计算，不依赖人的感受、意义或价值判断。"}, {"name_cn": "Precision", "measurement_cn": "取相似度最高的L个节点对中属于真实存在边的比例，公式(24)。", "objectivity_reason_cn": "由预测结果与客观边标签对照确定，可审计、可复现。"}, {"name_cn": "Recall", "measurement_cn": "预测出的真实存在边数占全部真实边数的比例，公式(25)。", "objectivity_reason_cn": "基于客观存在的边集合计算，不含主观判断。"}, {"name_cn": "F-measure", "measurement_cn": "由Precision和Recall按公式(26)综合得到。", "objectivity_reason_cn": "是对两个客观指标的确定性综合，仍属于客观预测性能度量。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: YouTube | Disease-Gene Network | Climate Network | DBLP
- Benchmark evaluation: MCLP在四个真实多关系网络（YouTube、Disease-Gene、Climate、DBLP）上，与CN、JC、PA、AA、LPMR等五个参照方法比较AUC、precision、recall和F-measure。多数组关系上MCLP取得最高或次高结果，并用配对t检验说明F-measure提升显著。该benchmark比较直接支撑‘MCLP预测质量更高’的核心主张。
- Decision: 客观指标方面，核心成功指标是链接预测的AUC、precision、recall和F-measure，它们基于网络边的客观事实标签计算，不涉及主观评价；提升这些指标是全文唯一核心目标与贡献。Benchmark方面，文章在实验方法部分明确将CN、JC、PA、AA称为benchmark方法，并在四个真实数据集上与MCLP及LPMR比较；该benchmark比较被用作证明MCLP预测质量更高的关键证据，且有明确参照点。因此两个模块均通过，strict_include=true。
- Confidence: 0.92

## Discovery of Technological Innovation Systems: Implications for Predicting Future Innovation

- Year/journal: 2024 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2023.2301172
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "未来专利数量（Future Patenting）", "measurement_cn": "使用USPTO专利数据按技术类（四字符CPC）聚合，统计未来5年内该技术类申请并授权的专利数量；预测任务中用下一年的专利数量。", "objectivity_reason_cn": "专利数量是USPTO授予/申请的可审计事实，不依赖人类感受或语义评价。"}, {"name_cn": "未来引用数量（Future Citations）", "measurement_cn": "按技术类统计未来5年内专利获得的引用量，并按年度均值缩放；预测任务中用下一年的引用量。", "objectivity_reason_cn": "专利引用记录是USPTO数据库中的客观计数，反映外部可核验事实。"}, {"name_cn": "TIS Score / Patent Capital（企业层面）", "measurement_cn": "TIS Score为企业专利组合中属于TIS相关技术类的专利占比；Patent Capital基于专利公告后3天异常股票回报估计的市场价值。", "objectivity_reason_cn": "专利档案和股票市场交易数据都是可审计的外部事实，不依赖主观评分或偏好。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 文章在自建的USPTO专利数据集上进行了两个预测任务：未来专利数量（Task 1）和未来引用数量（Task 2）。以Past（过去专利或引用）和Past+Cite（加入引文相关创新CRTI）作为基准特征集，用LASSO、CART、RF、XGBoost、LSTM等模型评估增加作者提出的创新指标（RTI/BSI/RTIQ）后的预测绩效，采用RMSE、RRSE、R²。结果显示加入创新指标后LSTM和树模型显著提升（如LSTM的RMSE提升40.11%，p<0.0001）。
- Decision: 客观指标：核心成功指标为专利数量、引用数量和基于市场的专利资本，均为客观可审计事实，不涉及主观感受或语义评价。唯一核心目标：全文围绕TIS发现框架及其对预测客观创新指标（数量和质量）的提升展开，无并列的主观或理论核心贡献。Benchmark：作者明确使用benchmark一词指代Past和CRTI等文献基准，并在预测任务中通过多个模型和明确对照比较证明TIS创新指标带来显著提升。因此三个门槛均通过。
- Confidence: 0.92

## Extracting Actionable Insights from Text Data: A Stable Topic Model Approach

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/16957
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "主题模型稳定性指标（文档-主题概率/标签、主题-词概率/Top词一致性）", "measurement_cn": "同一数据集上重复训练两次模型，经匈牙利算法对齐主题后计算S_doc_prob、S_doc_label、S_topic_prob、S_topic_topwords；实验重复30次取平均。", "objectivity_reason_cn": "稳定性指标只比较算法输出的概率分布和离散标签在不同运行间的一致性，不依赖任何人的主观感受、语义价值判断或偏好。"}, {"name_cn": "模型质量指标（perplexity、主题连贯性Cv/Cuci）", "measurement_cn": "Perplexity由模型对数似然计算；Cv/Cuci通过语料中词语共现的NPMI/PMI固定公式计算。", "objectivity_reason_cn": "这些指标均由确定性的计算流程从模型输出和文本语料自动生成，无专家评分、用户调研或人工语义好坏判断作为核心证据。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在Amazon产品评论、Yelp餐厅评论、StackExchange Q&A、公司描述四个文本数据集上，将Stable LDA与标准LDA、Doc LDA、Ensemble LDA、Granulated LDA进行系统比较（附录F另对比MRF-LDA和CRFTM），报告稳定性四项指标和模型质量指标，结果显示Stable LDA显著提升稳定性且质量不下降。
- Decision: 客观指标方面，核心成功指标是主题模型稳定性（重复运行间概率分布和标签的一致性）以及模型质量（perplexity、自动主题连贯性），均不依赖主观感受或人工语义评分；研究问题、设计目标、评价和贡献均围绕提升稳定性这一客观改进展开，无并列的理论或主观核心目标。Benchmark方面，作者在引言和实验部分明确使用benchmark/benchmarking陈述系统化比较，将Stable LDA与多个基线在同一批文本数据集上比较，并以稳定性结果作为核心主张的关键证据；存在明确参照点。因此 strict_include=true。
- Confidence: 0.92

## Hybrid neural network models for bankruptcy predictions

- Year/journal: 1996 / Decision Support Systems
- DOI: 10.1016/0167-9236(96)00018-8
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "破产预测准确率（prediction accuracy）", "measurement_cn": "使用韩国1979-1992年破产企业及配对公司样本，按Group I/II/III分为训练和保留样本，在保留样本上统计正确分类为破产/非破产的比例；并辅以Z检验比较不同模型的准确率差异。", "objectivity_reason_cn": "破产/非破产状态由韩国证券交易所、法定清盘、停业、连续亏损管理等外部事实标准界定，不依赖人类感受、语义评价或价值判断；准确率是对确定标签的分类结果进行可复核计数。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 作者在自建韩国破产数据的三组保留样本上，将四种混合神经网络模型（MDA-assisted NN、ID3-assisted NN、SOFM(MDA)-assisted NN、SOFM(ID3)-assisted NN）与MDA、ID3进行系统比较，报告Table 6的预测准确率和Table 7的Z值显著性检验，以此证明混合神经网络模型的准确率提升。
- Decision: 核心结果指标是破产/非破产事实标签上的预测准确率，属于客观固定事实标签的检测性能；全文唯一核心目标是提升破产预测准确率，评价结构和贡献声明均围绕此展开，无并列的主观、理论或政策目标。作者明确使用benchmark/benchmarking一词，将MDA和ID3作为基准进行比较，表6和表7的结果直接支持混合神经网络模型的准确率提升，因此满足strict_include。
- Confidence: 0.92

## Improving learning accuracy by using synthetic samples for small datasets with non-linear attribute dependency

- Year/journal: 2014 / Decision Support Systems
- DOI: 10.1016/j.dss.2013.12.007
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "MAPE 平均绝对百分比误差", "measurement_cn": "由 BPN 模型预测值与实际观测值计算：MAPE = (1/n)Σ|yi - ŷi| / yi × 100%", "objectivity_reason_cn": "预测目标是 TFT-LCD assembly shift、混凝土抗压强度、股票指数、游艇水动力等外部可测量的数值事实；误差计算完全由公式和实验数据决定，不依赖人的感受、语义或价值判断。"}, {"name_cn": "RMSE 均方根误差", "measurement_cn": "由 BPN 模型预测值与实际观测值计算：RMSE = sqrt(Σ(yi - ŷi)^2 / n)", "objectivity_reason_cn": "同上，RMSE 是预测误差的确定性客观统计量，不涉及用户满意度、专家评分或任何主观构念。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: UCI Machine Learning Repository – Concrete Compressive Strength Data Set (CCS) | UCI Machine Learning Repository – Istanbul Stock Exchange Data Set (ISE) | UCI Machine Learning Repository – Yacht Hydrodynamics Data Set (YH)
- Benchmark evaluation: 在 UCI 的 CCS、ISE、YH 三个公开标准数据集上，以不同训练样本数 NT∈{20,40,60,80,100,125,150} 和虚拟样本数 NV∈{50,100} 进行小数据集实验；用 BPN 预测，并比较 PM、MTD、MRA 三种方法；结果表显示 PM 的 MAPE、RMSE 在多数设置中更低，t 检验给出大量显著差异（Tables 8–10）。
- Decision: 该文以提升小数据集预测精度为唯一核心目标，核心指标 MAPE/RMSE 完全客观，不依赖主观评价。实验在 UCI 公开标准数据集 CCS/ISE/YH 上进行，具有明确命名的 benchmark 数据集，并与 MTD、MRA、原始 BPN 等明确参照点比较；benchmark 评价直接支撑其核心提升主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.92

## Know When to Run: Recommendations in Crowdsourcing Contests1

- Year/journal: 2018 / MIS Quarterly
- DOI: 10.25300/misq/2018/14103
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "获胜预测准确率（Top n accuracy）及平均绝对误差（MAE）", "measurement_cn": "在958个测试任务上，将模型预测的最高获胜概率或得分排名前n的solver与实际winner比较；n=1..5时预测命中数除以958；MAE为预测winner排名与实际排名1的平均距离。", "objectivity_reason_cn": "winner是平台上可审计的事实标签，预测命中与否由系统日志直接判定，不依赖人类评价。"}, {"name_cn": "推荐任务成功率（Recommendation success rate）", "measurement_cn": "对每个solver，用ranked-MNL-ties估计其参与任务的获胜概率并排序，取前n个任务（n为该solver实际获胜数），推荐成功率=k/n；与solver自身历史成功率n/m比较。", "objectivity_reason_cn": "是否赢得任务是客观事实；solver历史成功率和推荐成功率均可从任务结果日志计算。"}, {"name_cn": "任务排名一致性（Ranking consistency）", "measurement_cn": "在同一完成阶段（25%/50%/75%竞争者已知）时，比较对任务对的相对推荐是否与最终竞争结构下的推荐一致，报告一致比例89.32%、93.56%、96.47%。", "objectivity_reason_cn": "基于模型预测概率的排名比较，结果由数据和模型计算得出，可复现。"}, {"name_cn": "模拟参与人数与平台收入影响", "measurement_cn": "在100个新任务上模拟推荐，设置adoption probability p=0.1/0.2，比较模拟参与人数与实际人数，以及失败任务减少导致的平台预期收入增加（>8%）。", "objectivity_reason_cn": "参与人数和任务成败是平台日志事实，模拟规则透明且不含主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在从99designs收集的958个测试任务上，将MNL、朴素贝叶斯、贝叶斯网络、神经网络、SVM及Ranked-MNL-Ties等模型与两个基准（随机选择、基于points的基准）进行比较，报告Top 1-5预测准确率、MAE及显著性；推荐系统部分进一步以solver自身选择为参照比较推荐有效率（22.17%提升至31.24%，提升40.91%）。这些基准比较直接支撑模型和推荐系统优于既有选择和平台指标的核心主张。
- Decision: 客观指标：核心成功标准是预测任务winner的准确率和推荐提高solver赢得任务的成功率，这些基于平台客观事实标签（是否赢），不依赖人类主观评价；满意度仅作为推测性附带收益未进入评价。唯一核心目标：文章围绕构建并验证能提升solver获胜成功率的推荐系统展开，理论框架用于指导变量选择，不是并列核心贡献。Benchmark：全文存在明确的benchmark表述（‘Two benchmarks are used for comparison’），位于实验评价语境，比较对象明确（随机选择、points-based、solver自身选择），结果直接支撑客观指标提升。因此两个模块均通过，strict_include=true。
- Confidence: 0.92

## Late payment prediction models for fair allocation of customer contact lists to call center agents

- Year/journal: 2016 / Decision Support Systems
- DOI: 10.1016/j.dss.2016.03.002
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "客户名单分配的公平性，即各坐席实际/模拟回收债务金额的变异程度", "measurement_cn": "根据分配给每个坐席的客户实际支付金额，计算回收债务金额的标准差、极差、四分位距、变异系数；数值越小表示分配越公平。", "objectivity_reason_cn": "该构念不依赖任何人的主观感受或语义评价，直接由可审计的债务回收金额计算得出，外部可核验。"}, {"name_cn": "滞纳支付预测性能（作为公平分配的前置手段）", "measurement_cn": "按十分位计算的 lift 值及 AUROC；目标变量由 paid_amount 与 unpaid_amount 的系统记录客观生成。", "objectivity_reason_cn": "支付/未支付是账单系统中的外部事实，预测性能计算方式客观；但预测精度本身服务于公平分配目标，而非并列核心贡献。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 将三种现有启发式评分规则（TEN、CUM、CUA）作为 benchmark 基准，与十种基于预测模型的评分规则在十个不同坐席人数场景下比较。核心结果（表6-12）显示，模型评分规则在降低各坐席回收债务金额变异方面多数情况下优于启发式规则；EPST、EPRF 等最优次数最多，robustness test 也用 F 检验与三种启发式方法比较。
- Decision: 该文的核心目标是构建基于机器学习的滞纳支付预测模型和客户评分规则，以降低各催收坐席之间回收债务金额的变异，实现客观可测的名单分配公平性。评价指标为标准差、极差、四分位距和变异系数，均由账单/回收金额计算，完全客观；坐席偏好调查仅作为间接补充。全文存在明确的 benchmark 表述：三种现有启发式评分规则被明确称为 benchmark scoring rules，并在实验部分与十种基于预测模型的评分规则系统比较，比较结果直接支撑公平性提升的核心主张。因此同时通过客观指标和 benchmark 两个门槛。
- Confidence: 0.92

## Mitigating bankruptcy propagation through contractual incentive schemes

- Year/journal: 2012 / Decision Support Systems
- DOI: 10.1016/j.dss.2012.02.003
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "破产发生次数（ANR/ANM/ANSC）", "measurement_cn": "在400期仿真中分别统计零售商、制造商及全供应链的平均破产次数；破产定义为期末净资产低于零，由模型现金流和资产等式计算。", "objectivity_reason_cn": "破产状态由模拟财务规则客观判定，不依赖人的感受、偏好或语义评价，可从仿真日志中复现。"}, {"name_cn": "破产传播指标（CCC Lag=-1/0/+1）", "measurement_cn": "以零售商破产时间序列与制造商破产时间序列的交叉相关系数衡量破产传播方向与强度，由仿真生成的破产事件序列计算。", "objectivity_reason_cn": "数值基于可审计的破产事件发生序列统计得到，构念和取值均为客观、可复现的。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在第5.4节中，作者分别在RS、PD、QF合同下进行仿真，并将结果与无合同Benchmark情景在CCC和AN指标上比较；表3-5直接列出各合同的输出指标和Benchmark值，据此判断合同是否有效缓解破产传播。
- Decision: 核心指标为仿真供应链中的破产发生次数和破产传播交叉相关，均由模拟财务规则客观计算，不涉及主观构念；全文唯一核心目标是通过合同机制降低破产发生与传播。5.4.1节明确将无合同情景作为Benchmark，并在表3-5中作为核心证据比较合同与Benchmark，满足明确的benchmark评价门槛。因此 strict_include=true。
- Confidence: 0.92

## Modifying Transactional Databases to Hide Sensitive Association Rules

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2021.1033
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "修改后数据库的准确率（accuracy）", "measurement_cn": "准确率定义为未被修改的事务占原数据库事务总数的比例；目标函数等价于最小化被消毒/修改的事务数量。", "objectivity_reason_cn": "该指标由事务是否被修改的可审计事实直接决定，不依赖人的感受、语义评价或质量偏好。"}, {"name_cn": "求解时间（solution time）", "measurement_cn": "在给定数据集和实验环境下求解优化问题或运行算法的CPU/时钟时间。", "objectivity_reason_cn": "运行时间是可复现、可测量的技术性能指标。"}, {"name_cn": "被消毒事务数量（number of transactions sanitized）", "measurement_cn": "从原始数据库中因隐藏敏感关联规则而修改的事务数量。", "objectivity_reason_cn": "事务是否被修改是可直接审计的数据库操作记录。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: Verykios et al. (2004) algorithm 2.a | Verykios et al. (2004) algorithm 2.b | Telikani and Shahbahrami (2017)
- Benchmark evaluation: 作者在真实数据集 retail、bms-pos 和合成数据集 10m/50m/100m 上评价其最优方法，并与文献中的三个基准方法进行比较；基准实验记录了各方法在24小时时限内能否求解、求解时间和被消毒事务数量，结果显示基准方法在多数问题上无法求解或需大量消毒事务，而所提最优方法在平均13.29秒内求解且消毒事务数大幅更少。
- Decision: 客观指标方面，论文以修改后数据库的准确率/被消毒事务数作为核心目标，该指标基于事务修改这一可审计事实直接计算，不依赖人类感知或语义判断；求解时间也是客观技术指标。唯一核心目标方面，研究问题、模型、贡献声明和实验评价均围绕最大化准确率/最小化被修改事务数展开，未发现满意度、专家评分或理论机制等并列核心目标。Benchmark 方面，作者在实验部分明确使用“benchmark”一词指称文献中的三种基准方法，并在 Benchmark Experiments 表中将其作为比较对象，结果用于支持本文方法在被消毒事务数和求解时间上的核心提升主张；存在明确参照点（文献基准方法、itemset-hiding 方案、约简前后版本）。因此两个模块均通过，strict_include=true。
- Confidence: 0.92

## Municipal credit rating modelling by neural networks

- Year/journal: 2011 / Decision Support Systems
- DOI: 10.1016/j.dss.2010.11.033
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "分类准确率（classification accuracy, CA_test）", "measurement_cn": "10折交叉验证中，测试集上被正确分类的市政债券评级对象比例；以 Moody's 发布的评级类别作为真值标签，分别针对4类与9类评级任务计算。", "objectivity_reason_cn": "评级类别是外部评级机构（Moody's）公开给出的固定事实标签；分类准确率可由预测标签与真值标签直接计算，不依赖用户感受、语义质量判断或主观偏好。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在自建的美国康涅狄格州市政 Moody's 评级数据集上（4类和9类评级），使用10折交叉验证评价FFNN、RBFNN、PNN、CCNN、GMDH、SVM，并与LR、MDA、K-means和CT等基准分类器进行比较。表7报告各方法CA_test；PNN在4类问题达98.8%，9类问题达96.3%，为所有方法中最高。讨论部分还将统计方法结果与此前研究中的MDA结果比较。
- Decision: 该文以完全客观的分类准确率作为唯一核心目标，数据标签为Moody's公开评级类别，属固定事实标签；实验结果在评价部分明确与benchmark classifiers（LR、MDA、K-means、CT等）比较，且benchmark结果直接支撑核心的分类准确率提升主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.92

## News-based trading strategies

- Year/journal: 2016 / Decision Support Systems
- DOI: 10.1016/j.dss.2016.06.020
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "平均每日收益率", "measurement_cn": "基于股票历史价格和交易模拟，计算各策略在1956个交易日内的平均日收益；表1直接报告百分比。", "objectivity_reason_cn": "收益由市场价格和交易信号客观计算，不依赖人的感受、语义评价或价值判断。"}, {"name_cn": "平均每日异常收益率", "measurement_cn": "用个股日收益扣除同期市场（CDAX）收益后的异常收益，按交易模拟数据计算。", "objectivity_reason_cn": "异常收益基于可审计的市场行情数据，属于客观财务指标。"}, {"name_cn": "波动率/风险", "measurement_cn": "基于日收益序列的标准差，作为策略风险的客观度量。", "objectivity_reason_cn": "由收益分布直接计算，不依赖主观风险感受。"}, {"name_cn": "Sharpe比率和变异系数", "measurement_cn": "基于超额收益与收益标准差计算的风险调整绩效指标。", "objectivity_reason_cn": "由客观收益和波动数据计算，属于金融绩效度量。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: CDAX index
- Benchmark evaluation: 在CDAX指数、动量交易和组合交易等基准上评价新闻交易策略；简单新闻交易平均日收益0.4722%，监督学习1.1807%，明显高于CDAX基准0.0298%和动量交易0.0464%；统计检验进一步验证收益显著为正。
- Decision: 全文以交易策略的财务绩效（日收益、异常收益、波动率、Sharpe比率等）作为核心结果，这些指标均由市场行情和交易模拟客观计算，不涉及主观评价或语义判断；研究问题、评价结构和贡献声明均围绕提升财务绩效展开，未发现并列的核心贡献。作者在评价部分明确使用benchmark一词，以CDAX指数、动量交易和组合交易为参照，系统比较新闻交易策略的收益提升，且该比较是支撑核心盈利性主张的关键证据。因此两个模块均通过，strict_include=true。
- Confidence: 0.92

## RFID-enabled shelf replenishment with backroom monitoring in retail stores

- Year/journal: 2012 / Decision Support Systems
- DOI: 10.1016/j.dss.2011.11.018
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "总成本", "measurement_cn": "通过事件驱动模拟统计，PR政策下为 Π_PR = c_i*y_i + c_r*y_r + c_a*S*T + c_p*(y_c - y_f - y_s)；BM政策下另加 RFID 标签成本和库存调整成本。", "objectivity_reason_cn": "总成本由模拟中的货币成本参数和可计数事件（补货次数、检查次数、失销数等）计算，不依赖人的感知或语义评价。"}, {"name_cn": "服务水平", "measurement_cn": "定义为 β = y_s / (y_c - y_f)，即实际售出单位数除以剔除了 shrinkage 的总需求，由模拟输出计数计算。", "objectivity_reason_cn": "服务水平是需求满足比例，基于模拟事件计数得出，属于可审计、客观的运营指标。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在仿真实验中将周期盘点（PR）作为基准，对本文提出的 BM、BM+1、BM+X 三种 RFID 补货政策在不同 read rate 下进行最小总成本和服务水平比较；该比较直接用于支持 RFID 策略相对传统流程的成本/服务水平提升主张。
- Decision: 核心指标为总成本和服务水平，二者均由模拟计数和成本参数直接计算，属于完全客观的操作性指标；全文唯一核心目标是设计并评估 RFID 补货政策以提升成本效率和服务水平，不存在与客观指标提升并列的主观或理论核心贡献；同时，文中在评价语境明确以 periodic review 作为 benchmark，并使用该基准比较来支持 RFID 政策的改善主张，benchmark 表述位于结果部分且具有明确参照点。因此两个模块均通过，strict_include 为 true。
- Confidence: 0.92

## Twitter user geolocation using web country noun searches

- Year/journal: 2019 / Decision Support Systems
- DOI: 10.1016/i.dss.2019.03.006
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "全局准确率 (Acc)", "measurement_cn": "10折交叉验证下，GTN/GTN2预测用户国家与保守双源验证ground truth（用户资料位置字段+LIW经Google Maps）比较得到的正确分类比例", "objectivity_reason_cn": "用户国家是外部可核验事实标签，分类结果和准确率计算不依赖用户或评估者的主观感受/语义评价"}, {"name_cn": "加权F1分数 (WF1)", "measurement_cn": "在54类不平衡分类中按类别频率加权平均F1分数，由混淆矩阵计算", "objectivity_reason_cn": "基于客观预测与客观事实标签的混淆矩阵，公式客观"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在同一新建数据集上以10折交叉验证比较GTN与NER基准方法BM（以及混合方法BM2），核心结果Table 5：GTN Acc=80.6/WF1=81.3 vs BM 64.9/72.8 vs BM2 78.3/79.5；误差调整后Table 8：GTN 83.0/83.4。
- Decision: 该文核心目标是用GTN方法提升Twitter用户国家地理定位的分类准确性（Acc和WF1），这些指标基于外部可核验的国家事实标签，完全客观且无主观量表；全文没有并列的其他核心目标（GTN2速度优化为客观效率补充）。benchmark层面：作者在Section 3.3/3.4明确将现有WD方法BM称为benchmark method，并在10折交叉验证中与GTN系统比较，核心结果在Table 5/8中显示GTN准确率显著优于BM，benchmark评价直接支撑核心提升主张，且有明确比较对象。因此同时满足两个模块。
- Confidence: 0.92

## mHealth App recommendation based on the prediction of suitable behavior change techniques

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113248
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "Top-n推荐的Precision@n、Recall@n、F-measure@n", "measurement_cn": "基于移动运营商App使用日志计算：TP@n为推荐列表中被用户长期使用的App数量，N为用户长期使用的mHealth App总数；Precision@n=TP@n/n，Recall@n=TP@n/N，F-measure为二者的调和平均。", "objectivity_reason_cn": "数据来源是真实系统使用日志，计算方式由公式确定，不需要用户自我报告或人类语义评价，可审计可复现。"}, {"name_cn": "BCT适合性预测的Accuracy", "measurement_cn": "用训练/测试集比较AdaBoost、随机森林和逻辑回归预测Poss(u_i,b_k)的准确率；标签由用户-App使用时长矩阵与App-BCT编码矩阵相乘并二值化得到。", "objectivity_reason_cn": "标签是从系统日志和固定BCT编码规则中派生出来的，预测准确率按确定性公式计算，不依赖主观满意度或质量评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在来自中国移动运营商的真实数据集上，将BHAR与UBCF、IBCF、MF、SVD四种基准推荐方法比较；Fig.8显示BHAR在Precision@1=0.44、Recall@1=0.38、F-measure@1=0.41等指标上均优于各基准方法，用于支撑核心主张，即考虑BCT和用户特征可提升mHealth App推荐性能。
- Decision: 该文以提升mHealth App推荐性能为核心目标，核心成功指标是Precision、Recall、F-measure和Accuracy，均由移动运营商系统日志与固定公式计算，不依赖主观用户评价或语义质量判断，属于完全客观的可观测结果。全部贡献围绕BCT-based推荐方法展开，无并列核心目标。在4.3.4节明确使用benchmark methods表述，将BHAR与UBCF、IBCF、MF、SVD等显式基线在同一真实数据集上比较，结果用于支撑核心性能提升主张，满足benchmark比较中心性要求。因此strict_include为true。
- Confidence: 0.92

## A bi-level decision support system for uncertain network design with equilibrium flow

- Year/journal: 2015 / Decision Support Systems
- DOI: 10.1016/j.dss.2014.12.004
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "性能指标 PM（总行程时间成本 + 容量扩展投资成本，以美元计）", "measurement_cn": "由式(8)/(19)计算 PM(μ,y,f)=Σ_a c_a(y_a,f)f_a+ωV_a(y_a)；在 Sioux Falls 路网上用四组初始数据求解 Stackelberg 均衡，得到 PM 值及改善率。", "objectivity_reason_cn": "PM 由网络均衡流量、行程成本函数和投资成本函数计算得出，是可审计的经济/物理量；不依赖用户满意度、偏好或任何语义评价。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: Sioux Falls city network（真实数据基准路网）
- Benchmark evaluation: 在 Sioux Falls 标准基准路网上，用四组初始容量扩展和需求增长系数运行所提 BDSS 求解方案；报告 PM 改善率（9.76%–19.32%）、上/下界 gap 收敛至零的过程，以及与确定性名义解相比的不可行性增益 r+（29.62%–37.57%）和最优性损失 r−（2.11%–2.88%）。
- Decision: 核心指标 PM 是完全客观可计算的总行程时间与投资成本；全文研究问题、模型、评价和结论均围绕该客观指标的改进展开，没有主观量表或并列的核心贡献。全文明确使用 Sioux Falls 真实数据基准路网，并在该 benchmark 上评价所提方案，与确定性名义解、初始设置和上下界估计进行明确比较，benchmark 结果直接支持核心改进主张。因此两个模块均通过。
- Confidence: 0.9

## A branch-and-cut algorithm for the Winner Determination Problem

- Year/journal: 2009 / Decision Support Systems
- DOI: 10.1016/j.dss.2008.10.009
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "求解时间", "measurement_cn": "使用CPLEX 9.1在固定硬件（Sun Java Workstation，2×Opteron 2.6GHz，4GB RAM）上求解实例的CPU秒数，表中记为t。", "objectivity_reason_cn": "运行时间由计算环境和求解器直接记录，不依赖人的感受、意义或价值判断，完全客观且可审计。"}, {"name_cn": "对偶间隙", "measurement_cn": "整数最优值与线性规划松弛最优值之间的相对百分比差距，由求解器在根节点或求解过程中计算。", "objectivity_reason_cn": "对偶间隙是基于模型数学结构的可计算数值，不涉及人类评价，客观可验证。"}, {"name_cn": "分支树节点数", "measurement_cn": "求解过程中CPLEX分支定界树的节点数量，表中记为nodes。", "objectivity_reason_cn": "节点数由分支定界过程客观产生，可通过求解器日志核实，属于可审计的技术指标。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: CATS 2.1 (Combinatorial Auction Test Suite)
- Benchmark evaluation: 在CATS 2.1生成的FR、LR、D、B、P、R、A等分布实例以及自生成S实例上，评价了原始公式(WDP)、tightened公式(WDP*)、预处理和branch-and-cut算法；比较不同方法在求解时间、对偶间隙和分支节点数上的表现。表1、2、3、4展示了这些对比结果。
- Decision: 文章核心目标是设计并验证求解Winner Determination Problem的branch-and-cut算法，以降低求解时间和对偶间隙等完全客观可测量的计算指标。全文评价体系完全基于求解时间、gap和分支节点数，无任何主观或人类语义判断指标。多面体与有效不等式研究是算法改进手段，不构成并列核心目标。计算实验使用公开标准测试套件CATS 2.1作为评价场地，并与原始公式等baseline进行显式比较，结果证明客观指标提升，因此同时满足客观指标唯一核心目标和明确benchmark表述两个条件。
- Confidence: 0.9

## A cross-domain recommender system with consistent information transfer

- Year/journal: 2017 / Decision Support Systems
- DOI: 10.1016/j.dss.2017.10.002
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "平均绝对误差 (MAE)", "measurement_cn": "在测试集上计算预测评分与实际评分之差的绝对值的平均值", "objectivity_reason_cn": "预测评分和实际评分都是数值事实，误差计算完全确定，不依赖人类情感、语义或质量判断。"}, {"name_cn": "均方根误差 (RMSE)", "measurement_cn": "在测试集上计算预测评分与实际评分之差的平方平均后再开方", "objectivity_reason_cn": "同 MAE，均为数值事实的确定性计算，客观可审计。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在五个真实数据集（Movielens20M、Netflix、LibraryThing、Amazon Book、YahooMusic）上构造九个跨域推荐任务，使用 MAE 和 RMSE 与五个基线方法（PCC、FMM、SVD、CBT、RMGM）比较。CIT 在绝大多数任务中获得最低 MAE/RMSE，并通过显著性检验。
- Decision: 客观指标 MAE/RMSE 为完全客观的推荐预测误差，全文以提升推荐精度为唯一核心目标；存在明确 benchmark 表述（摘要中 outperforms five benchmarks），且实验部分提供与五个基线的完整比较，benchmark 评价直接支撑核心提升主张。因此 strict_include=true。
- Confidence: 0.9

## A decision support system for detecting products missing from the shelf based on heuristic rules

- Year/journal: 2009 / Decision Support Systems
- DOI: 10.1016/j.dss.2008.11.004
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "准确率（Accuracy/Confidence）", "measurement_cn": "由混淆矩阵计算：D/(B+D)，其中D为正确识别的OOS数，B+D为系统判定为OOS的总数；基于物理审计得到的EXISTS/OOS标签验证。", "objectivity_reason_cn": "OOS表示商品未实际摆放在货架上的物理事实，可由物理审计按固定规则观测；准确率是分类器预测与外部事实标签的客观比对。"}, {"name_cn": "覆盖率/支持度（Support/Coverage）", "measurement_cn": "由混淆矩阵计算：D/(C+D)，即真实OOS案例中被系统正确检测的比例。", "objectivity_reason_cn": "同样基于物理审计标签，反映检测系统覆盖真实缺失货架事件的能力，客观可复核。"}, {"name_cn": "Total Performance", "measurement_cn": "Support和Accuracy的调和平均数，用于比较分类器在类别不平衡下的综合性能。", "objectivity_reason_cn": "由两个客观性能指标计算得到，不依赖主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: European OOS Index (EOI)
- Benchmark evaluation: 在物理审计生成的不同测试集（TeS1-TeS6）和二次精炼审计中，评价ISOS Ver.1/Ver.2的OOS检测效果，并与European OOS Index基准比较；结果显示ISOS Accuracy约92-94%，OOS Index约36%，Support约13-27% vs 0.27%。
- Decision: 文章核心目标是开发并验证基于启发式规则的ISOS系统，提升OOS自动检测的Accuracy/Support；这些指标基于物理审计得到的客观事实标签（EXISTS/OOS），属于objective_fixed_factual_labels，且没有并列的主观核心目标。全文明确将European OOS Index作为benchmark，并在实验/使用部分以其为参照比较ISOS的Accuracy和Support，benchmark评价直接支撑核心检测性能提升主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.9

## A stack-based prospective spatio-temporal data analysis approach

- Year/journal: 2008 / Decision Support Systems
- DOI: 10.1016/j.dss.2007.12.008
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "精确率 Precision", "measurement_cn": "C/A，其中 A 为算法识别出的异常区域大小，C 为与真实异常区域重叠的大小", "objectivity_reason_cn": "基于模拟数据中已知的真实异常区域几何重叠关系计算，可由确定性算法计算，不依赖人的感受或语义评价"}, {"name_cn": "召回率 Recall", "measurement_cn": "C/B，其中 B 为真实异常区域大小，C 为与算法识别区域重叠的大小", "objectivity_reason_cn": "基于已知真实异常区域与算法输出的面积重叠计算，客观可审计"}, {"name_cn": "F值 F-measure", "measurement_cn": "精确率和召回率的调和平均数", "objectivity_reason_cn": "由客观的精确率和召回率直接计算"}, {"name_cn": "告警延迟 Alarm delay", "measurement_cn": "异常发生时刻到算法触发告警时刻之间的延迟", "objectivity_reason_cn": "由模拟数据中异常开始时间和算法告警时间的时间戳计算"}, {"name_cn": "误报次数 False alarms", "measurement_cn": "算法报告区域不与真实异常区域重叠时的告警次数", "objectivity_reason_cn": "基于模拟数据中已知异常区域和算法输出区域的客观重叠判断"}, {"name_cn": "漏报次数 Fail to detect", "measurement_cn": "整个监测期间算法未能触发告警的次数", "objectivity_reason_cn": "根据模拟异常事件是否被算法报告直接计数"}, {"name_cn": "计算时间 Computing time", "measurement_cn": "算法在模拟数据集上运行所需秒数", "objectivity_reason_cn": "来自实验运行的客观计时数据"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: space–time scan statistic (SaTScan) 作为本文明确指定的基准方法
- Benchmark evaluation: 在emerging、expanding、moving三类模拟场景上，将PSVC与基准方法SaTScan进行系统化比较，报告精确率、召回率、F-measure、告警延迟、误报次数、漏报次数和计算时间；同时使用ROC曲线比较敏感度与特异度。结果表（表1、3、5）和ROC曲线成为证明PSVC在识别不规则异常区域方面更准确的核心证据。
- Decision: 客观指标方面：全文核心评价指标为精确率、召回率、F值、告警延迟、误报/漏报次数和计算时间，全部来自模拟已知异常区域或系统计时，客观且可审计，不依赖人类主观评价。唯一核心目标方面：研究问题、假设、实验和结论均围绕PSVC在客观检测性能上的提升，没有并列的主观体验、理论机制或政策贡献作为核心目标；定量评价框架只是用于支撑比较的方法工具。benchmark方面：第4.2节明确将space–time scan statistic/SaTScan指定为benchmark method，并在第4.4节模拟实验中以SaTScan为对照，系统比较客观指标；该benchmark评价直接支撑“PSVC更准确检测不规则异常区域”的核心主张。因此满足全部条件。
- Confidence: 0.9

## An intelligent information agent for document title classification and filtering in document-intensive domains

- Year/journal: 2007 / Decision Support Systems
- DOI: 10.1016/j.dss.2007.04.001
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "Mean Average Precision (MAP)", "measurement_cn": "在Reuters-21578 ModLewis split的14个测试主题上，基于系统分类/过滤结果与数据集固定主题标签比较，在11个召回点计算平均精确率并跨类别平均。", "objectivity_reason_cn": "取值由系统输出与固定基准标签决定，不依赖用户感受、偏好或在线人工质量评分；即使标签由人标引，也是已发布的标准基准事实。"}, {"name_cn": "Average Recall", "measurement_cn": "在Reuters-21578测试集中，对每个类别召回率后跨类别平均，数据来自固定测试文档和主题标签。", "objectivity_reason_cn": "与MAP相同，基于确定性分类输出和固定基准标签计算，属于可审计的检索/分类性能指标。"}, {"name_cn": "Average elapsed time per topic", "measurement_cn": "在单台Pentium III 800 MHz CPU和1GB内存配置下，记录各模型每个主题的平均处理耗时。", "objectivity_reason_cn": "时间为客观可测量的物理量，不依赖人的主观判断。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: Reuters-21578 (Modified Lewis / ModLewis split)
- Benchmark evaluation: 在Reuters-21578 ModLewis split上，从135个主题中选取17个主题，构造HAL空间并用文档标题进行分类；实验评价IFC、IFC+BR和SVM三组模型，报告MAP、平均召回和时间。表6显示IFC+BR在标题任务上的平均精确率为0.698，超过SVM标题任务的0.601；文章据此主张混合模型优于SVM。
- Decision: 客观指标方面：论文以文档分类/过滤的MAP、平均召回和计算时间为核心结果，这些指标基于Reuters-21578固定主题标签和实际运行时间，不依赖用户主观评价；Reuters主题标签属于固定基准事实标签，因此符合客观指标门槛。唯一核心目标方面：摘要、实验和结论均围绕提升分类/过滤精确率、召回率和效率展开，信息流与信念修正是实现手段而非并列的核心理论贡献，全文没有用户满意度或主观质量作为成功标准，因此唯一核心目标为客观指标提升。benchmark方面：第4节明确将Reuters-21578 ModLewis Split称为常用文本分类benchmark，在该基准上对IFC、IFC+BR和SVM进行系统比较，结果直接支撑“优于SVM”的核心性能主张，并且有明确参照点。因此两个模块均通过，strict_include=true。
- Confidence: 0.9

## Balancing quality and budget considerations in mobile crowdsourcing

- Year/journal: 2016 / Decision Support Systems
- DOI: 10.1016/j.dss.2016.06.019
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "平均错误率 e", "measurement_cn": "在模拟空间众包任务中，聚合结果与模拟任务真实值不一致的任务数占总任务数的比例（式11）", "objectivity_reason_cn": "任务真实值是实验者生成的二元模拟事实，聚合结果由工人输出和多数投票规则计算，错误率可直接从实验日志确定，不依赖人的感受或语义判断。"}, {"name_cn": "平均预算利用率 B^(-)", "measurement_cn": "每个空间任务实际花费金额与预算之比的均值（式12）", "objectivity_reason_cn": "实际花费和预算都是模拟系统中的可审计数值，直接可观察、可复算。"}, {"name_cn": "平均旅行距离 D", "measurement_cn": "每个任务所选工人的位置与任务地点距离的平均值（式13）", "objectivity_reason_cn": "距离由GPS坐标和欧氏/球面距离计算得到，属于物理可测事实，不依赖主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在基于Foursquare新加坡子集生成的空间众包模拟场景上，将Budget-TASC与CrowdBudget、GeoTruCrowd进行比较，覆盖不同任务半径和预算设置，报告平均错误率、预算利用率、平均旅行距离；结果显示Budget-TASC的平均错误率15.4%，低于GeoTruCrowd的28.0%和CrowdBudget的81.1%，预算利用率67.6%，低于两者的84.8%和96.5%。
- Decision: 客观指标方面，核心成功指标是平均错误率、预算利用率和平均旅行距离，均由模拟日志和可审计数值计算，不依赖主观人类评价；唯一核心目标是在预算约束下提升众包结果质量，实验和贡献声明均围绕该目标。Benchmark方面，实验部分明确将CrowdBudget和GeoTruCrowd选为benchmark approaches，在Foursquare数据生成场景上进行系统化比较，并给出明确参照点和性能提升证据。因此两个模块均通过，strict_include=true。
- Confidence: 0.9

## Complex Problem Solving: Identity Matching Based on Social Contextual Information

- Year/journal: 2007 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00141
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "精确率 Precision", "measurement_cn": "身份匹配二元分类的 TP/(TP+FP)；预测匹配对与 SSN 认定的真实匹配对比较。", "objectivity_reason_cn": "匹配真值由警方数据库中的 SSN 作为金标准确定，属于可核验的身份等同事实，不依赖人的感受或语义质量评价。"}, {"name_cn": "召回率 Recall", "measurement_cn": "身份匹配二元分类的 TP/(TP+FN)；预测匹配对与 SSN 认定的真实匹配对比较。", "objectivity_reason_cn": "同上，真值由 SSN 金标准确定，数值由系统日志/数据库记录计算。"}, {"name_cn": "F-measure", "measurement_cn": "精确率与召回率的调和平均，用于综合衡量匹配性能。", "objectivity_reason_cn": "由两个客观分类指标计算得到，不包含主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在 Tucson Police Department 的 Meth World 真实毒品犯罪数据集上，以 Fp（个人特征）作为基准，评价 Fp+Fs（加入社会特征）的身份匹配效果；采用 10 折交叉验证计算 precision/recall/F-measure，并通过 t 检验和回归分析比较性能差异。
- Decision: 客观指标方面：文章核心评价目标是身份匹配的 precision/recall/F-measure，真值由 SSN 金标准确定，属于客观固定事实标签，全部核心成功结果均为客观指标。唯一核心目标方面：研究问题、设计目标、评价结构和贡献声明均围绕“改进身份匹配方法有效性”展开，没有并列的主观或理论机制核心目标；Mumford 框架和设计科学定位是背景与意涵。Benchmark 方面：作者在实验部分明确将“仅用个人特征”的条件称为 benchmark，并在该基准上比较加入社会特征后的性能，比较对象明确、位于评价语境、服务于核心提升主张。因此 strict_include=true。
- Confidence: 0.9

## Developing a Composite Measure to Represent Information Flows in Networks: Evidence from a Stock Market

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2021.1066
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "异常收益方向预测误差（AbnReturn）", "measurement_cn": "持有期实际异常收益（实际收益减去基于Fama-French等风险因子的预期收益）与模型预测值之间的RMSE/MAE/MAPE", "objectivity_reason_cn": "异常收益由市场价格和可审计的财务/因子数据计算，不依赖人的感受、语义评价或价值判断"}, {"name_cn": "异常收益幅度预测误差（|AbnReturn|）", "measurement_cn": "实际异常收益绝对值与模型预测绝对值之间的RMSE/MAE/MAPE", "objectivity_reason_cn": "绝对异常收益同样来自可观察的市场数据和因子模型，数值可确定性复算"}, {"name_cn": "交易策略超额收益（alpha）", "measurement_cn": "按EAC与情绪分组的投资组合收益对Fama-French因子回归后的截距alpha，检验是否产生显著正超额收益", "objectivity_reason_cn": "组合收益与因子收益均为市场成交和公开定价数据，alpha估计来自标准计量程序"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在新浪财经2015-2016年构建的54个网络和2017年49个网络的持仓样本上，使用Fama-MacBeth、SVR、MLP、决策树、随机森林和GBDT等方法预测异常收益，用RMSE/MAE/MAPE比较EAC模型与无EAC基准模型，以及与度、接近、介数、PageRank中心性的对比；并用bootstrap置信区间检验预测精度差异。
- Decision: 客观指标方面：核心成功指标是异常收益方向与幅度的预测误差以及交易策略的超额收益，均来自市场价格和可审计财务数据，不依赖主观感知或语义评价；唯一核心目标是提出并验证EAC这一新网络指标能显著提升异常收益预测，全文无并列的主观成功标准。Benchmark方面：作者明确使用‘benchmark model without EAC’并扩展为与多种替代网络指标的系统比较，比较结果位于结果部分，直接支撑EAC的核心性能提升主张，且有明确参照点。因此两个模块均通过，strict_include=true。
- Confidence: 0.9

## Human Identification for Activities of Daily Living: A Deep Transfer Learning Approach

- Year/journal: 2020 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2020.1759961
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "人身份识别准确率/精确率/召回率/F1/AUC", "measurement_cn": "在HANDY和OPPO对象传感器数据集上，将模型预测的受试者身份与预定义身份标签比较，计算宏平均precision、recall、F1、micro-averaged accuracy和ROC AUC", "objectivity_reason_cn": "受试者身份是固定外部事实标签，不依赖人的感受、语义理解或价值判断；指标可由预测标签与已知标签的匹配确定性计算。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: HANDY (公开可穿戴传感器数据集，参考文献标题标注为Benchmark dataset) | OPPO/Opportunity (公开对象传感器数据集)
- Benchmark evaluation: 在HANDY（30受试者可穿戴传感器）和OPPO的四个对象传感器目标域（Glass、Cup、Spoon、Bread）上，将DTL-HID/CNN-HID与kNN、SVM、NB、DT、CNN-HID/T、CNN-HID/CA、DTL-HID/T、DTL-HID/CA等基准模型比较，报告accuracy、precision、recall、F1和AUC。实验结果显示DTL-HID在多数比较中显著优于所有非迁移基准和替代迁移框架。
- Decision: 客观指标方面，HID任务是对固定身份事实标签的分类，准确率/精确率/召回率/F1/AUC是从预测与真实身份标签确定性计算，不依赖主观感受；研究问题和全部实验围绕提升对象传感器HID性能，属于唯一核心目标。Benchmark方面，摘要和Evaluation Design明确使用benchmarks进行系统比较，表7-10及结果部分比较了DTL-HID与多个baseline和替代模型，并以其客观指标提升作为核心证据。两个模块均通过，因此strict_include=true。
- Confidence: 0.9

## Improving accuracy and diversity of personalized recommendation through power law adjustments of user similarities

- Year/journal: 2013 / Decision Support Systems
- DOI: 10.1016/j.dss.2013.03.006
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "平均秩比 (Mean Rank Ratio, MR)", "measurement_cn": "将测试对象与其对照对象按判别分数排序，测试对象的秩除以测试对象和对照对象总数，再对所有测试对象取平均；重复随机子抽样20次取均值。", "objectivity_reason_cn": "由历史评分转换的二元链接和排序公式直接计算，不依赖人的感受、语义判断或价值评价。"}, {"name_cn": "召回提升 (Recall Enhancement, RE)", "measurement_cn": "在给定阈值L下，统计用户测试对象中被排在Top-L的比例，并与随机猜测的期望召回相比得到倍数；重复随机子抽样取均值。", "objectivity_reason_cn": "基于链接是否进入排序列表的计数计算，属于可审计的行为/系统日志类结果。"}, {"name_cn": "平均个性化 (Mean Personality, MP)", "measurement_cn": "对每位用户取Top-L推荐对象，计算用户之间推荐列表的重叠度，用1减去平均重叠度得到个性化程度；重复随机子抽样取均值。", "objectivity_reason_cn": "由推荐列表集合的交集与阈值L直接计算，不依赖人的主观评价。"}, {"name_cn": "平均新颖性 (Mean Novelty, MN)", "measurement_cn": "对推荐列表中每个对象计算其信息含量（用户覆盖比例的负对数），再对Top-L中的对象和所有用户取平均。", "objectivity_reason_cn": "由对象的全局流行度/用户覆盖比例直接计算，属于可观测的客观属性。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: MovieLens | Netflix
- Benchmark evaluation: 在MovieLens和Netflix两个公开数据集上，采用90/10重复随机子抽样验证，比较PLUS与UserSim（同时涉及GlobalRank和随机猜测）在平均秩比、召回提升、平均个性化、平均新颖性上的表现；表1和表2显示PLUS相对UserSim在准确性和多样性上均有提升。
- Decision: 客观指标与唯一核心目标通过：MR/RE/MP/MN均为可计算、可审计的客观指标，文章以提升这些指标为唯一核心目标与贡献。Benchmark门槛通过：全文将MovieLens和Netflix作为公开基准数据集置于评价中心，并报告PLUS与UserSim/GlobalRank/随机猜测的比较结果，支撑核心改进主张。因此strict_include=true。
- Confidence: 0.9

## Improving accuracy and lowering cost in crowdsourcing through an unsupervised expertise estimation approach

- Year/journal: 2019 / Decision Support Systems
- DOI: 10.1016/j.dss.2019.05.005
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "准确率（accuracy）", "measurement_cn": "将估计出的专家子集的多数投票结果与数据集中的 ground truth 比较，正确比例即为准确率；在五个数据集上按不同 expertise 阈值报告。", "objectivity_reason_cn": "ground truth 是已给定的任务类别标签，准确率按确定性规则计算，不依赖人的感受、偏好或质量判断。"}, {"name_cn": "AUC", "measurement_cn": "根据 worker 的 expertise 排序与 ground truth 计算 ROC 曲线下面积。", "objectivity_reason_cn": "由确定性算法和已知标签计算，可审计。"}, {"name_cn": "成本/预算浪费（cost/wastage）", "measurement_cn": "按 Wastage = B_explore + B_exploit × (1 - accuracy) 计算，越低越好。", "objectivity_reason_cn": "由预算参数和准确率构成的公式计算，属于可计算的交易/资源成本指标。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: SQUARE-RTE | SQUARE-TEMP | SQUARE-Duchenne | Google | TREC
- Benchmark evaluation: 在 RTE、TEMP、Duchenne、Google、TREC 五个真实世界 benchmark 数据集上评价 ROUX，并与 ELICE、Gaussian、Raykar、GLAD 四种主流/state-of-the-art 方法比较；报告准确率、AUC 和成本浪费，并附 Wilcoxon 检验。
- Decision: 客观指标：核心成功指标是准确率、AUC、成本浪费，均可由 ground truth、budget 和确定性公式计算，不涉及主观评价。唯一核心目标：摘要、引言和实验一致表明设计目标是提升聚合准确率并降低成本；结论中列出的方法特性是支撑该目标的设计机制。Benchmark：实验在五个被明确称为 benchmark 的真实世界数据集上展开，与四种 state-of-the-art 方法比较并使用统计检验，证明核心客观指标提升。因此两个模块均通过，strict_include=true。
- Confidence: 0.9

## Inverse matrix-free incremental proximal support vector machine

- Year/journal: 2012 / Decision Support Systems
- DOI: 10.1016/j.dss.2012.02.007
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "运行时间/时间复杂度", "measurement_cn": "在 Matlab 环境中计时训练/更新过程；不同维度、样本数下的累计运行时间，以及与 ISVM、SVCM 的对比。", "objectivity_reason_cn": "运行时间是系统可审计的物理耗时，不依赖人的感受或语义评价；算法时间复杂度的推导也是确定性事实。"}, {"name_cn": "预测准确率", "measurement_cn": "在 NDC、UCI Mushroom、USPS Digit、TIS 等二分类数据集上，用分类器预测标签并与给定事实标签比较，计算正确分类比例。", "objectivity_reason_cn": "标签为外部事实标签（数字类别、可食/有毒、翻译起始位点、合成分布类别），准确率由确定性计算得到，不涉及主观偏好或语义质量判断。"}, {"name_cn": "收敛速度", "measurement_cn": "观察随着增量样本增加，预测精度达到稳定或更优的速度；用准确率曲线随样本数变化表示。", "objectivity_reason_cn": "该指标由客观准确率和样本数变化关系直接刻画，不依赖人类体验或评价。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: NDC synthetic data set | UCI Mushroom data set | USPS Digit data sets | TIS biological data set
- Benchmark evaluation: 在 NDC、UCI Mushroom、USPS 数字对和 TIS 等数据集上评价 IMISVM 与 ISVM、SVCM：图3-8比较运行时间随维度和样本数的变化，证明 IMISVM 相较于 ISVM 更高效；图9比较消除正则项后的收敛与准确率，证明 IMISVM 能保持或提升准确率并加速收敛。
- Decision: 核心目标完全围绕客观可测的计算效率、运行时间和收敛速度，辅以外部事实标签上的分类准确率，无主观量表或语义评分；全文存在明确 benchmark 数据集节，并在这些数据集上以 ISVM/SVCM 为参照进行运行时间与准确率对比，benchmark 结果直接支撑核心效率提升主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.9

## Leveraging fine-grained transaction data for customer life event predictions

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2019.113232
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "AUC（ROC曲线下面积）", "measurement_cn": "在10折交叉验证的测试集上，根据模型预测概率与生命事件是否发生的二元事实标签计算AUC；生命事件标签由金融机构依据地址变更、子女出生、关系状态变化等外部事实严格登记。", "objectivity_reason_cn": "生命事件是外部可核验的事实标签，AUC是由预测概率与事实标签计算的确定性统计量，不涉及人类感受、语义质量评价或价值判断。"}, {"name_cn": "Top Decile Lift（TDL，前10%提升度）", "measurement_cn": "将预测概率最高的10%客户与随机基线（TDL=1）比较，计算该部分客户中生命事件发生率的倍数，10折平均；同样基于生命事件二元事实标签。", "objectivity_reason_cn": "以生命事件是否发生这一客观事实为标签，衡量排序顶端客户相对于随机选择的提升程度，属客观可审计的预测性能指标。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在来自大型欧洲金融服务机构的约132,703名客户、约6,000万笔交易的真实数据上，对搬家、生子、新关系、关系结束四个生命事件分别建模；采用10折交叉验证，以AUC和TDL为主要评价指标，并通过Wilcoxon符号秩检验进行成对比较。核心比较包括：mod_rfm（RFM扩展PSN）对比mod_psn（原始二元PSN），以及组合模型mod_s_rfm对比单一数据源模型mod_s、mod_rfm和mod_s_psn。结果显示RFM扩展显著优于二元PSN，组合模型通常达到最高预测性能，并显著优于随机猜测。
- Decision: 客观指标方面：核心评价指标AUC和TDL基于金融机构登记的生命事件事实标签（搬家、生子、关系变化），不依赖主观感知、语义质量或偏好判断；研究目标、模型选择、评价结构和贡献声明均围绕预测绩效提升，属于唯一核心目标。Benchmark方面：作者在引言和结论中明确使用“benchmark/benchmarking”表述，并实际在真实数据集上以现有方法、单一数据源模型和随机猜测作为参照，通过10折交叉验证比较模型AUC和TDL，证明RFM扩展和组合数据源的预测性能提升。因此两个模块均通过，strict_include=true。
- Confidence: 0.9

## Predicting adequacy of vancomycin regimens: A learning-based classification approach to improving clinical decision making

- Year/journal: 2007 / Decision Support Systems
- DOI: 10.1016/j.dss.2006.02.003
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "总体准确率", "measurement_cn": "在987例万古霉素临床病例上预测万古霉素方案充分性；采用80/20训练/测试随机划分并重复30次，总体准确率=正确分类病例数/总病例数。", "objectivity_reason_cn": "结局标签由TDM实测峰浓度和谷浓度与固定目标范围（峰20-40 mg/l、谷<10 mg/l）比较得到，不是主观感受或价值判断；准确率是客观可复核的预测性能。"}, {"name_cn": "各类别预测值", "measurement_cn": "对每个决策类Ci，预测值=TC_i/(TC_i+FC_i)，计算来自30次随机测试集上的平均结果。", "objectivity_reason_cn": "TC_i/FC_i由预测类别与客观标签比较得到；标签由固定编码规则确定。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在987例临床万古霉素病例上评价C4.5、反向传播神经网络、Bagged C4.5和Bagged NN，与基准one-compartment药代动力学模型比较；评价任务包括方案充分性二分类、峰浓度三分类和谷浓度二分类，结果以总体准确率和各类别预测值呈现（表4-6）。
- Decision: 该文开发并评价用于预测万古霉素方案充分性的学习型分类系统，核心结局为总体准确率和各类别预测值，是由TDM实测浓度与固定治疗范围比较得到的客观标签，不依赖主观感受或语义评价；全文唯一核心目标是提升该客观预测性能。评价设计明确将one-compartment药代动力学模型作为performance benchmark，并在结果部分以该benchmark为参照报告显著提升，benchmark评价是核心证据。两个模块均通过，因此严格纳入。
- Confidence: 0.9

## Predicting tax avoidance by means of social network analytics

- Year/journal: 2018 / Decision Support Systems
- DOI: 10.1016/j.dss.2018.02.001
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "AUC（ROC曲线下面积）", "measurement_cn": "在2013和2014两个out-of-time测试集上，对低税/非低税分类的预测概率计算ROC曲线下面积；低税企业由三年现金有效税率（CETR）行业调整后最低五分位定义。", "objectivity_reason_cn": "标签和预测值都来自可审计的会计数据和确定性公式（TXPD、PI、SPI及行业分位），不依赖人的感受、语义评价或偏好。"}, {"name_cn": "Accuracy/Sensitivity/Specificity", "measurement_cn": "在相同测试集上按50%或适配截断值计算正确率、低税企业识别的灵敏度和特异度。", "objectivity_reason_cn": "由二分类混淆矩阵的可计数结果计算，属于外部可核验事实。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 以仅含公司特征的local模型为benchmark基线，在2013和2014两个年度外样本上评价logistic回归、决策树和随机森林下的五种模型；核心结果是混合二部网络随机森林AUC达0.8431/0.8306，较local模型0.7683/0.7489提高约7个百分点，且经DeLong检验显著。
- Decision: 客观指标：目标为预测低税企业（低税状态由三年现金ETR行业调整后最低五分位确定），评价指标AUC/accuracy/sensitivity等均来自可审计会计事实和分类混淆矩阵；唯一核心目标是提高预测性能并比较网络特征带来的提升。benchmark：作者在方法部分明确将仅公司特征的local模型作为当前状态和基准，并在out-of-time测试集上系统比较五种模型；结果表、ROC/显著性检验以基准对比为核心证据。因此 strict_include=true。
- Confidence: 0.9

## Preprocessing unbalanced data using support vector machine

- Year/journal: 2012 / Decision Support Systems
- DOI: 10.1016/j.dss.2012.01.016
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "敏感性（Sensitivity）", "measurement_cn": "测试集中实际购买 caravan 保险的正类客户被正确预测的比例，由预测标签与实际标签比较计算。", "objectivity_reason_cn": "购买行为是外部可审计事实，预测正确与否由固定标签决定，不依赖人类感受或语义评价。"}, {"name_cn": "特异性（Specificity）", "measurement_cn": "测试集中实际未购买 caravan 保险的负类客户被正确预测的比例。", "objectivity_reason_cn": "未购买行为是客观事实，计算基于固定真实标签与预测标签的比较。"}, {"name_cn": "准确率（Accuracy）", "measurement_cn": "测试集中正确预测的正类和负类样本占总样本的比例。", "objectivity_reason_cn": "由客观真实标签和预测结果直接计算，不涉及主观判断。"}, {"name_cn": "AUC", "measurement_cn": "ROC 曲线下面积，衡量分类器区分两类的客观性能。", "objectivity_reason_cn": "由预测评分和客观真实标签计算，属于可审计的预测性能指标。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: CoIL 2000 Challenge / Insurance Company Dataset（Coil dataset）
- Benchmark evaluation: 在 CoIL 2000 公开数据集上，使用官方划分的训练集和测试集评价所提 SVM 预处理方法；将 SVM-MLP、SVM-LR、SVM-RF 与相应的 standalone MLP、LR、RF 以及 SMOTE、下采样、过采样等多种平衡方法比较，报告敏感性、特异性、准确率和 AUC。Tables 4-9 与 Figs. 3-5 显示所提方法在敏感性上普遍优于对照方法，这直接支撑了核心改进主张。
- Decision: 客观指标方面：目标变量为客户是否购买 caravan 保险，属于外部可审计事实；核心评价指标为敏感性、特异性、准确率和 AUC，均由固定真实标签计算，不依赖主观判断；全文核心目标是提出并验证 SVM 预处理方法以提高不平衡数据下分类器的客观预测性能，未发现并列的主观或理论核心贡献。Benchmark 方面：文章明确使用公开的 CoIL 2000 数据挖掘竞赛数据集作为评价场地，并在实验部分与多种 baseline、标准平衡方法进行系统比较，比较结果直接支撑核心改进主张，满足命名式 benchmark 门槛。因此两个模块均通过，strict_include 为 true。
- Confidence: 0.9

## RFID-enabled flexible warehousing

- Year/journal: 2017 / Decision Support Systems
- DOI: 10.1016/j.dss.2017.05.002
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "行程成本（trip cost）", "measurement_cn": "基于模型中的需求位置、仓库/筒仓位置、距离相关的边际成本、检索/归还成本等参数计算总运输成本；数值实验中以与刚性系统相比的成本降低百分比报告，如Table 1、Figure 7/9/10/11。", "objectivity_reason_cn": "成本由距离、容量、需求分配等可审计的模型参数和优化目标决定，不依赖人的感受、语义理解或价值判断。"}, {"name_cn": "提前期/单程需求交付时间（lead time）", "measurement_cn": "文章在摘要和结论中声称“减少提前期”，属于可客观测量的运营时间类指标；数值实验部分主要量化行程成本，但该指标仍为客观运营结果。", "objectivity_reason_cn": "提前期/时间是客观可审计的运营事实，不涉及主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在自行生成的多组仓库布局（5、10、15、20个随机筒仓位置）上，将所提出的柔性仓储系统与同一刚性系统（单一配送中心/固定位置检索返还）进行 benchmarking 比较；报告并绘制的指标是行程成本降低百分比，并进一步比较静态容量约束与动态控制等配置的性能差异。
- Decision: 客观指标：核心结果指标是行程成本（trip cost）等运营成本/提前期，来自模拟优化模型和成本函数，不依赖主观体验或语义评价，所有核心成功结果均为客观性能。唯一核心目标：研究问题、设计目标、评价结构和贡献声明都围绕成本/提前期这一客观性能提升展开；文中的柔性机制和知识型系统是实现该目标的手段，不是并列的核心贡献，且无主观核心结果。Benchmark：正文在数值分析部分明确使用 benchmarking/benchmark 表述，将多个柔性布局配置与同一刚性系统/单一配送中心比较，并用表格/图形报告成本降低百分比；该 benchmark 比较是支撑核心改进主张的关键证据，且存在明确参照点。因此 strict_include=true。
- Confidence: 0.9

## Recommendation as link prediction in bipartite graphs: A graph kernel-based machine learning approach

- Year/journal: 2013 / Decision Support Systems
- DOI: 10.1016/j.dss.2012.09.019
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "Precision@10", "measurement_cn": "推荐列表中前10个物品中与测试期实际购买匹配的数量除以10", "objectivity_reason_cn": "基于用户未来是否实际购买物品的交易事实，不依赖主观评价"}, {"name_cn": "Recall@10", "measurement_cn": "推荐列表中前10个物品中与测试期实际购买匹配的数量除以未来购买总数", "objectivity_reason_cn": "基于实际交易记录计算"}, {"name_cn": "F-measure", "measurement_cn": "Precision 和 Recall 的调和平均值", "objectivity_reason_cn": "由客观的 precision 和 recall 计算"}, {"name_cn": "Rank score", "measurement_cn": "根据推荐列表中命中物品所在排名，按半衰期折扣加权后的得分", "objectivity_reason_cn": "基于实际交易匹配和排名计算"}, {"name_cn": "ROC曲线 (top 1000 recommendations)", "measurement_cn": "在不同推荐数量下，推荐列表命中实际购买物品的比率曲线", "objectivity_reason_cn": "基于实际交易事实绘制"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在三个真实世界数据集（图书零售、服装零售、图书评分）上，将提出的图核方法与七个基准算法（user-based、item-based、item popularity、spreading activation、link analysis、matrix factorization、binary matrix factorization）比较，报告precision、recall、F-measure、rank score和ROC曲线。结果显示图核方法在较大推荐数量上显著优于所有基准方法。
- Decision: 客观指标：推荐性能（precision、recall、F-measure、rank score、ROC）完全基于未来实际交易事实，不依赖主观评价；唯一核心目标：全文围绕提升推荐性能展开，核有效性和复杂度证明只是方法支撑，无并列核心贡献；benchmark：作者明确使用'state-of-the-art benchmark algorithms'表述系统化基准比较，评价位于实验和结论部分，并与七个基准算法及两个核基线明确比较，结果直接支撑性能提升的核心主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.9

## Semi-Supervised Cyber Threat Identification in Dark Net Markets: A Transductive and Deep Learning Approach

- Year/journal: 2020 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2020.1790186
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "F1-score", "measurement_cn": "在人工标注验证集上，基于威胁/非威胁预测结果计算精确率与召回率的调和平均；论文报告提出方法F1=89.55%，显著高于基准方法。", "objectivity_reason_cn": "威胁类别是产品清单的外部事实类别（如黑客工具、勒索软件、被盗账户），F1由预测标签与事实标签比对计算，不依赖用户感受或语义质量评价。"}, {"name_cn": "Precision / Recall", "measurement_cn": "同样基于预测结果与专家标注的事实标签计算；论文强调提出方法同时提升精确率和召回率。", "objectivity_reason_cn": "精确率和召回率是分类器在外部事实标签上的可审计统计量，不涉及主观偏好或体验。"}, {"name_cn": "Accuracy", "measurement_cn": "在验证集上正确分类比例；由于类别不平衡，论文将其作为辅助指标并主要依赖F1。", "objectivity_reason_cn": "准确率由预测标签与固定事实标签对比得到，客观可计算。"}, {"name_cn": "AUC", "measurement_cn": "ROC曲线下面积；有、无半监督标注的LSTM分别从0.94提高到0.96。", "objectivity_reason_cn": "AUC基于真阳性率与假阳性率计算，属于客观分类性能指标。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在自建的79,434条DNM产品数据集上开展实验，将提出的TSVM+LSTM与k-NN、LR、Random Forest、SVM、CNN、LSTM、TSVM等基准方法比较，报告准确率、精确率、召回率、F1和AUC；提出方法F1=89.55%，优于所有基准，且t检验显著。
- Decision: 文章核心目标是在暗网市场产品描述中提升网络威胁自动识别的分类性能，所有核心结果均为F1、精确率、召回率、准确率、AUC等外部事实标签上的客观指标；没有主观量表或并列主观目标。评价部分明确把k-NN、LR、RF、SVM、CNN、LSTM、TSVM等称为state-of-the-art benchmark methods，并在该基准比较中证明提出方法的核心性能提升。因此三个条件均满足，strict_include=true。
- Confidence: 0.9

## Shapley Value-Based Feature Attribution for Data Masking

- Year/journal: 2026 / MIS Quarterly
- DOI: 10.25300/misq/2025/18502
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "披露风险（disclosure risk）", "measurement_cn": "使用线性回归/回归树等推断模型预测机密特征值，用R²、AAD、RASD等距离/方差指标计算真实值与预测值的差距", "objectivity_reason_cn": "指标基于数值预测误差或决定系数，由数据与模型可直接计算、可审计，不依赖用户的感知、偏好或语义判断"}, {"name_cn": "数据效用（data utility）", "measurement_cn": "使用线性回归/回归树等预测模型预测效用特征值，用R²、AAD、RASD等指标衡量掩盖后数据的预测性能", "objectivity_reason_cn": "指标同样是客观的统计预测性能度量，不依赖用户满意度或主观质量评价"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在模拟数据集及Credit、Salary、CRSP/Compustat三个真实数据集上，将所提risk-only和weighted-cost特征选择方法与Benchmark I（仅掩码机密特征）和Benchmark II（随机选择一半非机密特征）比较，报告风险减少和效用损失的百分比（如Table 4、Table 5a/b/c、Table 6），以此证明所提框架能更有效地降低披露风险并保持数据效用。
- Decision: 本文核心目标是降低推断性披露风险并保持数据效用，两者均以R²/AAD/RASD等客观统计指标度量，实验评估和贡献声明完全围绕这些客观指标提升展开，无主观量表或并列核心目标；正文实验部分明确以Benchmark I和Benchmark II作为基准方法进行比较，比较结果（风险减少和效用保持）是支撑核心提升主张的关键证据，满足benchmark四门槛；因此纳入。
- Confidence: 0.9

## Simultaneous optimization of neural network function and architecture algorithm

- Year/journal: 2004 / Decision Support Systems
- DOI: 10.1016/s0167-9236(02)00147-1
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "均方根误差（RMSE）", "measurement_cn": "在10个蒙特卡洛合成问题及Building数据集上，分别计算训练集和测试集（out-of-sample）的RMSE平均值，并与OGA、BP3/6/12、Prune、CC等算法比较。", "objectivity_reason_cn": "RMSE由数据与模型预测值直接计算，完全不依赖人类感受、语义判断或主观评价，属于可审计的数值指标。"}, {"name_cn": "网络结构简约性（隐藏节点数、零权重比例、无关变量消除率）", "measurement_cn": "统计最终网络的隐藏节点数、非零权重的比例、以及与人为加入的无关输入相连接权重的归零比例。", "objectivity_reason_cn": "这些结构属性由算法输出的权重矩阵和网络拓扑直接确定，外部可验证，不涉及人类体验或价值判断。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: Prechelt NN benchmark datasets（Building数据集，来自The Great Energy Predictor Shootout竞赛）
- Benchmark evaluation: 在Prechelt NN benchmark的Building数据集上，NNSOA与OGA、BP（3/6/12隐藏节点）、Prune、Cascade Correlation进行RMSE比较。NNSOA在训练集和测试集上的平均RMSE均最低（如out-of-sample 5.43e-02 vs BP最低1.06e-01），并识别出人为加入的无关变量及多个额外不相关输入。
- Decision: 该文核心目标为同时优化神经网络预测精度（RMSE）和网络结构简约性（隐藏节点、零权重、无关变量消除），所有核心指标均为客观可审计指标，不存在主观构念或并列的非客观贡献。Benchmark方面，作者明确将Building问题取自Prechelt收集的NN benchmark数据集，并在该数据集上与多种基线算法比较，结果用于支持NNSOA的核心提升主张。因此两个模块均通过，strict_include为true。
- Confidence: 0.9

## Software project effort estimation with voting rules

- Year/journal: 2009 / Decision Support Systems
- DOI: 10.1016/j.dss.2008.12.002
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "pred(25)", "measurement_cn": "估计值落在实际工作量±25%范围内的项目比例，由 d=|e-a|/a 与阈值0.25比较后计数得到", "objectivity_reason_cn": "基于数据集中实际工作量（可审计事实）和算法预测值计算，不依赖人的感受或语义判断"}, {"name_cn": "MMRE (Mean Magnitude of Relative Error)", "measurement_cn": "所有项目的相对误差 d 的均值", "objectivity_reason_cn": "由实际工作量与预测值直接计算"}, {"name_cn": "MdMRE (Median Magnitude of Relative Error)", "measurement_cn": "所有项目的相对误差 d 的中位数", "objectivity_reason_cn": "由实际工作量与预测值直接计算"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: COCOMO data set | Albrecht data set | ERP data set
- Benchmark evaluation: 在 COCOMO、Albrecht、ERP 三个数据集上，采用 jackknife 方法评价社会选择投票规则（Copeland、Maximin、Borda，二值及加权模型）的工作量估算准确度，报告 pred(25)、MMRE、MdMRE，并与表中的既有方法（COCOMO Basic、线性回归、神经网络、灰色关联、CBR、回归树、遗传规划、DEA、类比法等）进行比较。
- Decision: 论文的核心目标是提出并验证一种软件工作量估算方法，其成功标准是完全客观的预测误差指标（pred(25)、MMRE、MdMRE），基于公开数据集中的实际工作量计算，无任何主观构念作为核心成功标准；评价在多个公开标准数据集（COCOMO、Albrecht）上进行，并与多个既有方法（COCOMO Basic、回归、神经网络、CBR、灰色关联等）比较，符合命名式 benchmark 门槛。因此同时满足客观指标唯一核心目标和明确 benchmark 表述两个条件，予以纳入。
- Confidence: 0.9

## The value of vehicle telematics data in insurance risk selection processes

- Year/journal: 2017 / Decision Support Systems
- DOI: 10.1016/j.dss.2017.04.009
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "客户出险索赔预测性能（AUC）", "measurement_cn": "以2015年是否至少发生一次索赔为二进制事实标签，使用10折交叉验证在验证集上计算AUC。", "objectivity_reason_cn": "索赔发生是保险公司记录的可审计外部事实，不依赖人的感受、语义理解或价值判断；AUC是确定性可复算的客观性能指标。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在保险公司专有数据集上，以10折交叉验证AUC为评价准则，系统比较Logistic回归、随机森林、人工神经网络三类模型在四组变量（传统变量、标准telematics、组合、组合+专家变量）上的预测性能；基准为仅含传统变量的Logistic回归模型，AUC=0.5777，最终全变量模型达到AUC=0.6135（Logistic回归）和0.6176（人工神经网络）。
- Decision: 客观指标方面，核心结果为“2015年是否至少发生一次索赔”这一事实标签上的AUC预测性能，完全客观可审计；唯一核心目标是评估telematics数据对车险风险选择预测模型的提升，全文没有主观量表、满意度或理论机制作为并列成功标准。benchmark方面，虽然没有公开命名数据集，但作者在结果部分明确使用“benchmark logistic regression model”作为基准，并通过Table 3的系统化AUC对比证明核心的客观指标提升，符合陈述式benchmark评价门槛。因此两个模块均通过，严格纳入。
- Confidence: 0.9

## Twitter user geolocation using web country noun searches

- Year/journal: 2019 / Decision Support Systems
- DOI: 10.1016/j.dss.2019.03.006
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "国家地理定位准确率（Acc）和加权F1（WF1）", "measurement_cn": "在自建Twitter用户数据集上，通过10折交叉验证将预测的国家标签与保守双重来源ground truth（元数据+LIW，并进行人工修正）比较，计算全局准确率与类别频率加权F1。GTN2则以GTN响应为oracle标签评估其匹配准确率。", "objectivity_reason_cn": "用户国家/国家兴趣是外部可核验的地理事实；准确率和加权F1由预测标签与事实标签对照得到，不依赖用户感受、语义价值或主观偏好。"}, {"name_cn": "GTN2匹配GTN响应的准确率与计算速度", "measurement_cn": "用机器学习模型（BG/RF/SVM/MLP）学习GTN分类目标，在10折交叉验证中报告Acc/WF1；同时报告MLP训练和测试时间（约3ms/用户）。", "objectivity_reason_cn": "匹配GTN响应属于系统日志/预测性能测度，运行时间可审计，均不依赖主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在自建的多语言Twitter国家地理定位数据集上，通过10折交叉验证将GTN与benchmark方法BM（state-of-the-art NER/机器学习方法[15]）和混合基准BM2进行比较，报告Acc与WF1（Table 5、Table 8）；GTN显著优于BM，并在调整ground truth后显著优于BM和BM2。GTN2则与GTN及多种机器学习基线（BG/RF/SVM/MLP）比较，评估其匹配GTN响应的能力（Table 12）。
- Decision: 客观指标方面，文章核心是Twitter用户国家地理定位的预测性能（Acc、WF1）与GTN2的匹配准确率/速度，这些均基于外部可核验的国家标签，不含主观满意度、偏好或语义质量评价；核心目标与贡献唯一且围绕客观性能提升。benchmark方面，作者在方法-评价语境明确使用‘benchmark method’表述（Section 3.4），并通过Table 5/8/12的对比支持核心改进主张，存在明确参照点（BM、BM2、GTN oracle）。因此两个模块均通过，strict_include=true。
- Confidence: 0.9

## A Finite Mixture Logit Model to Segment and Predict Electronic Payments System Adoption

- Year/journal: 2011 / Information Systems Research
- DOI: 10.1287/isre.1090.0277
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "预测准确率（holdout样本中EPS采用分类准确率）", "measurement_cn": "将数据随机分为训练集（约60%，9078个账户）和验证集/留出样本（6098个账户）；用训练数据估计各模型，再以0.5截断值计算验证样本中ACH/非ACH支付选择的正确分类比例。", "objectivity_reason_cn": "因变量是实际支付方式（ACH debit 或 conventional check），可在账单数据中直接观察和审计，不依赖人类感受、语义判断或主观评价。预测准确率由确定性的分类比对计算得到。"}, {"name_cn": "模型拟合指标（LL、BIC、伪R²）", "measurement_cn": "基于最大似然估计计算对数似然值、BIC、AIC、CAIC以及伪R²，用于模型比较和分段数选择。", "objectivity_reason_cn": "这些统计量由数据和模型公式确定计算，属于可审计的数值结果，不涉及主观判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在相同的数据划分（训练集与多个随机留出样本）上，对有限混合模型与标准logit模型、两阶段模型、层次logit模型、互补log-log模型进行比较。核心比较指标是留出样本上的预测准确率；有限混合模型总体预测准确率约为89.2%，而标准logit、层次logit等约为71.5%–72.2%；通过10次随机划分进一步验证，有限混合模型的平均预测准确率为90.2%，层次logit约72.0%。这些基准评价直接支撑了‘有限混合模型提升预测性能约17%’的核心主张。
- Decision: 客观指标方面：本文核心指标为留出样本中的预测准确率（对实际ACH付款行为的分类），可直接从账单档案中计算，不依赖人类主观评价，属于fully_objective_direct。唯一核心目标是提升EPS采用预测准确率，并辅以模型拟合指标（BIC等）；研究问题、评价结构和贡献声明均围绕此目标。未发现并列的主观结果、理论机制贡献或政策建议作为核心贡献。Benchmark方面：虽然未使用公开命名的基准数据集，但作者在第4节明确使用“benchmark models”一词描述与标准logit、两阶段、层次logit、互补log-log等基线模型的系统化基准比较，且该比较处于评价语境，结果直接支撑核心预测性能提升主张，并具有明确参照点（多个baseline模型）。因此两条条件均满足，strict_include为true。
- Confidence: 0.88

## A brain information-aided intelligent investment system

- Year/journal: 2012 / Decision Support Systems
- DOI: 10.1016/j.dss.2012.05.041
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "投资组合的收益率/投资表现", "measurement_cn": "以实际市场价格序列（日经225股票）进行模拟投资，按系统确定的最优投资率计算每日平均收益率，并计算标准差和夏普比率；与基准模型比较收益率增量（basis points）。", "objectivity_reason_cn": "收益率、风险（标准差）和夏普比率来自实际市场数据和明确的投资规则，是可审计的财务事实，不依赖人的感受、语义判断或主观评价。"}, {"name_cn": "ABIC模型选择改进值", "measurement_cn": "使用Akaike's Bayesian Information Criterion（ABIC）评价加入脑信息后的预测/投资模型相对于基准基准（仅自回归项或仅预测收益率）的拟合改进，记录各session的ABIC差异。", "objectivity_reason_cn": "ABIC是基于似然和参数惩罚的客观统计准则，计算结果由数据和模型决定，不依赖人类主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在20个session中，系统用前80期学习、后20期序贯验证，将包含脑信息的系统投资收益率与几个明确基准比较：(1) 仅使用预测收益率且不使用脑信息的模型；(2) 传统Markowitz组合选择模型的有效前沿（the efficient frontier）；(3) 以AIC选择的ARMA–GARCH金融时序模型；(4) TOPIX市场指数。结果显示：相对于仅预测收益率模型平均每日改进5.28个基点（20/20 session改进）；相对于ARMA–GARCH模型平均改进33.67个基点（17/20 session改进）；相对于TOPIX平均改进4.22个基点（16/20 session改进）；14/20 session的系统收益-风险位置位于传统有效前沿的左上侧。
- Decision: 客观指标：核心结果变量为投资收益率、风险和Sharpe比率，直接由实际市场数据和固定投资规则计算，完全客观；ABIC改进是客观统计模型选择证据。唯一核心目标：研究问题、系统设计、实验评价和贡献声明都围绕改进投资表现这一客观结果，不存在并列的用户主观体验、理论贡献或制度贡献。Benchmark：全文在实验/评价部分多次明确使用benchmark一词，并以无脑信息模型、Markowitz有效前沿、ARMA-GARCH模型和TOPIX作为明确参照点，报告了收益率的改进数值，benchmark比较直接支撑系统的核心提升主张。因此两个模块均通过，strict_include为true。
- Confidence: 0.88

## A personalized paper recommendation method considering diverse user preferences

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113546
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "Precision（精确率）", "measurement_cn": "Top-N 推荐列表中相关论文（用户实际参考文献）所占比例，按公式(13)对所有用户平均", "objectivity_reason_cn": "相关与否由用户是否实际在参考文献中收录决定，属于可核验的真实行为，不依赖主观评分"}, {"name_cn": "Recall（召回率）", "measurement_cn": "用户实际参考文献中被成功推荐的比例，按公式(14)对所有用户平均", "objectivity_reason_cn": "基于用户真实参考文献集合与推荐列表的集合匹配，客观可计算"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: Aminer dataset | DBLP dataset
- Benchmark evaluation: 在 Aminer 和 DBLP 两个公开标准数据集上评价 PRHN 方法，采用 5 折交叉验证，比较 Precision 和 Recall，并与 BC、CC、MSCN、CAR、Metapath 等基线方法对比。
- Decision: 本文核心目标明确且唯一：提出 PRHN 论文推荐方法以提升推荐精度和召回率。评价指标均为基于真实参考文献集合的 Precision/Recall，完全客观，不依赖主观评价。实验在公开标准数据集 Aminer 和 DBLP 上进行，并与多个基线方法比较，benchmark 评价直接支撑核心提升主张。因此两个模块均通过，strict_include 为 true。
- Confidence: 0.88

## CLAP: Collaborative pattern mining for distributed information systems

- Year/journal: 2011 / Decision Support Systems
- DOI: 10.1016/j.dss.2011.05.002
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "端到端系统运行时间", "measurement_cn": "在四个基准查询和SD/WS合成数据库上，以秒为单位记录各框架回答相同查询的总运行时间；具体见图7、图8、表6.1-6.3和表7。", "objectivity_reason_cn": "运行时间由程序执行过程直接产生，是可审计的系统日志/计时结果，不依赖人的感受、语义判断或价值评价。"}, {"name_cn": "站点间消息交换开销", "measurement_cn": "记录Bloom filter大小（KB）、Bloom filter构建时间、查询时间，以及剪枝效率/规则数目；见表5、图6。", "objectivity_reason_cn": "消息字节数、计时和规则计数都是确定性的技术事实，不依赖主观评估。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: IBM Quest synthetic data generator 生成的 SD/WS 数据库（表2标题为 Benchmark database characteristics） | 表4定义的四类基准查询 Q1-Q4
- Benchmark evaluation: 在SD/WS两组基准数据库上，使用Q1-Q4基准查询对CLAP、SQLP、PALP三种框架进行系统评价；比较运行时间、消息大小和可回答性。结果显示CLAP在多数支持度设置下运行时间最短，并能回答SQLP/PALP无法回答的Q2/Q3。
- Decision: 该文核心是设计并验证CLAP分布式模式挖掘框架，以完全客观的运行时间、消息开销和模式发现能力作为成功标准；没有任何主观量表或人类语义评价作为核心指标。实验部分明确选择一组查询作为benchmarks，并在SD/WS基准数据库上以SQLP、PALP作为显式比较对象，证明CLAP的运行时间提升和额外模式发现能力。因此客观指标、唯一核心目标和benchmark门槛均满足。
- Confidence: 0.88

## Communication requirements and network evaluation within electronic meeting system environments

- Year/journal: 1991 / Decision Support Systems
- DOI: 10.1016/0167-9236(91)90074-l
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "响应时间", "measurement_cn": "EBS测试中记录每个工作站在文件复制到服务器到从服务器读取新文件之间的时间差；DOS测试中记录copy from/to前后时间差。结果以秒计，并用t检验与回归分析比较不同配置。", "objectivity_reason_cn": "响应时间是可由系统时钟/程序日志直接测量的物理时间量，不依赖人的感受、语义理解或质量判断；测试在受控网络负载下重复执行，数据来源为系统记录。"}, {"name_cn": "配置成本", "measurement_cn": "通过IBM PS/2 Model 50/60/80处理器和硬盘的公开列表价格比较；结论中用于判断性价比。", "objectivity_reason_cn": "价格是可审计的交易事实，独立于人的主观体验。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 文章在真实EMS应用环境（Group Systems的Electronic Brainstorming）和可复制的DOS文件传输测试中，对5种LAN配置（IBM/50、IBM/60、IBM/80、NOV/50、NOV/60）在4、7、10、15、20个用户以及250字节、1K、10K、100K文件大小条件下进行响应时间基准测试。结果显示Novell Netware在响应时间上显著快于IBM PC LAN Program，NOV/50配置在成本和性能上最优。
- Decision: 客观指标方面，核心成功指标为响应时间，由系统时间戳和程序日志直接测量，不涉及人类主观评价；成本和性价比亦为客观事实。核心目标方面，全文以LAN配置的基准比较和响应时间提升为核心，通信需求与方法讨论只是测试参数和框架支撑，未构成并列核心贡献。Benchmark方面，作者明确使用benchmark/benchmarking表述，在第4、5、6、7节将基准比较作为核心评价，且与IBM PC LAN、不同服务器、不同负载条件等明确参照点比较。三模块均通过，strict_include为true。
- Confidence: 0.88

## Comparative study of adaptability and flexibility in distributed manufacturing supply chains

- Year/journal: 2010 / Decision Support Systems
- DOI: 10.1016/j.dss.2009.09.001
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "总系统成本", "measurement_cn": "由仿真模型中的成本公式计算，包括顾客和供应商的库存持有成本、缺货/延期成本、订单设置成本等，如Eq.(1)、(6)、(10)所示。", "objectivity_reason_cn": "成本数值完全由仿真状态和明确公式决定，不依赖人的感受、语义判断或质量评价。"}, {"name_cn": "顾客需求满足率（fill rate）", "measurement_cn": "按Eq.(21)从仿真中的缺货量和需求量计算：Fill Rate = (1 - sum(B_jpt)/sum(d_jpt)) * 100%。", "objectivity_reason_cn": "满足率是可由系统日志/仿真记录直接核验的运营指标，反映订单满足的外部事实，不依赖主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在仿真实验中，将flexible MTO和adaptive MTO两种协调机制与stochastic model（基准）比较，报告总系统成本改善百分比（Figs.1-3, Eq.20）和fill rate改善百分比（Figs.4-5, Eq.22），并用t检验验证成本改善的显著性（Table 5）。
- Decision: 文章以总系统成本和顾客需求满足率这两个完全客观、可由仿真计算直接确定的运营指标作为核心绩效结果；核心目标是研究并改进MTO供应链中引入flexibility和adaptability后的客观绩效。作者在Section 3.1明确将stochastic model称为所提机制的benchmark，并在实验结果中以其为参照计算改善百分比和显著性检验。满足客观指标、唯一核心目标和明确benchmark三方面条件。
- Confidence: 0.88

## Estimating the development cost of custom software

- Year/journal: 2003 / Information & Management
- DOI: 10.1016/s0378-7206(02)00099-x
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "软件项目开发工作量估计精度（MMRE和PRED(25)）", "measurement_cn": "在ISBSG历史项目数据上采用jack-knife逐一估计每个项目的开发工作量，按公式MRE=|actual-estimated|/actual计算单个相对误差，再汇总为MMRE和PRED(25)。", "objectivity_reason_cn": "实际工作量来自ISBSG项目库中的记录人时/人月，是可由项目日志审计的事实；MMRE和PRED(25)是公式化算术计算，不依赖人的感受、语义评价或质量偏好。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: ISBSG项目仓库 Release 6（International Software Benchmarking Standards Group）
- Benchmark evaluation: 在ISBSG Release 6中筛选出59个供应链信息系统项目，用jack-knife在六种策略上评价校准类比法的估计精度；核心结果表（Table 5）报告各策略的MMRE和PRED(25)，最优策略TRADEOFF-H达到MMRE=23.84%、PRED(25)=70.37%，并与OLS回归（MMRE=68%）及文献目标值（MMRE=25%、PRED(25)=75%）比较。
- Decision: 文章核心目标是通过校准类比法提升软件项目开发工作量估计精度，核心成功指标MMRE和PRED(25)基于ISBSG中的实际人时记录，完全客观且可审计。评价在公开标准基准ISBSG Release 6上进行，并明确将其称为SCE研究的标准benchmark；结果与文献目标值、OLS模型及多种策略比较，证明估计精度提升。不存在主观满意度、专家质量评分或理论机制等并列核心贡献，因此同时满足客观指标唯一核心目标和明确benchmark表述两个门槛。
- Confidence: 0.88

## Feature construction for fraudulent credit card cash-out detection

- Year/journal: 2019 / Decision Support Systems
- DOI: 10.1016/j.dss.2019.113155
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "Top 5%/10%/15%/20% 精确率（Precision）", "measurement_cn": "将25,000张信用卡按80/20划分为训练/测试集，用Xgboost、随机森林、SVM输出欺诈概率并按降序排序，计算前5%、10%、15%、20%卡片中的精确率；重复10次取均值。", "objectivity_reason_cn": "欺诈/合法标签由发卡机构基于风控算法和运营确认的外部事实确定，预测结果由可审计的分类命中率计算，不依赖人类感受、语义评价或主观质量判断。"}, {"name_cn": "准确率、精确率、召回率、F1（平衡数据集）", "measurement_cn": "另从3000张欺诈卡和3000张合法卡构造平衡数据集，使用随机森林模型报告accuracy、precision、recall、F1。", "objectivity_reason_cn": "这些指标均由真实欺诈标签与模型预测结果确定性计算，属于对客观事实标签的分类性能度量。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在真实信用卡交易数据集（25,000张卡、1,067,010笔交易）上，用Xgboost、随机森林、SVM评估特征集1-4、FDA特征及其组合；核心比较对象是基于Whitrow聚合策略构造的benchmark feature set 5。结果给出相对feature set 5的top 5%-20%精确率提升，并在平衡数据集中与既往研究性能做粗略比较。
- Decision: 文章的核心目标是构造并验证用于欺诈性信用卡套现检测的特征集，核心成功指标为精确率、召回、准确率和F1等客观预测性能；欺诈标签由发卡机构基于风控算法和运营确认的外部事实确定，不涉及主观评价。全文明确以基于Whitrow策略的feature set 5作为benchmark，并以其为参照报告各项提出特征集的性能改进，benchmark评价直接支撑核心提升主张。因此客观指标、唯一核心目标和benchmark三个门槛均通过。
- Confidence: 0.88

## GANNET: A Machine Learning Approach to Document Retrieval

- Year/journal: 1994 / Journal of Management Information Systems
- DOI: 10.1080/07421222.1994.11518048
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "Jaccard's score（Jaccard 匹配分数）", "measurement_cn": "对用户选定的文档集合，计算每篇文档与其他文档的关键词集合交集大小除以并集大小，得到个体适应度；系统优化后再计算同一指标，并在表1中报告初始值、首次GA值、最终HP/GA值及提升百分比。", "objectivity_reason_cn": "该指标由文档关键词集合的集合运算直接确定，不依赖用户、专家或研究者的主观评价、语义判断或感受；给定关键词集合后，Jaccard 值可确定性地计算和复现。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: DIALOG 3,000篇测试库（自建测试集，非公开命名套件）
- Benchmark evaluation: 作者从3,000篇 DIALOG 数据库中随机抽取30个测试案例（1、2、3、4、5、10篇文档各5例），对每个案例计算初始 Jaccard 适应度，运行首次 GA 得到 First GA score，再运行完整 GA/HP 周期得到 Final HP/GA score，统计改进百分比、CPU时间和选出文档数。
- Decision: 核心成功指标是完全客观可计算的 Jaccard's score，不涉及用户满意度、专家评分或语义质量判断；研究目标、评价结构和贡献声明均围绕该系统在该指标上的提升展开，且没有并列的主观或理论核心目标。全文在评价部分明确使用 benchmark testing/System Benchmark Testing Results，属于陈述式系统化基准评价，并与初始分数和仅GA基线进行比较，用于证明核心提升主张。因此两部分均通过，strict_include=true。
- Confidence: 0.88

## How High Should We Go? Determining Reservation Values to Negotiate Successfully for Composite Software Services

- Year/journal: 2017 / Information Systems Research
- DOI: 10.1287/isre.2016.0678
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "协商成功率", "measurement_cn": "在仿真协商过程中，所有组件服务均在截止期内达成协议的实验次数占比；每次实验根据协商成功或失败记录二值结果并统计平均。", "objectivity_reason_cn": "协商是否成功是一个可外部审计的事件（协议达成或失败），不依赖人的感受或语义评价。"}, {"name_cn": "协商成功时用户/服务提供者的平均效用", "measurement_cn": "根据论文定义的线性效用函数和QoS属性值计算用户及每个提供者的效用，再对成功协商的实验取平均。", "objectivity_reason_cn": "效用值由明确公式和仿真生成的QoS数值确定，是系统结构化的数学输出，并非真人主观评分。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: Global_RV_Bench | Component_RV_Bench
- Benchmark evaluation: 在自建的两个基准方法Global_RV_Bench和Component_RV_Bench上，通过改变组件数量、偏好信息完整度（无/部分/完全）和全局约束严苛程度，比较协商成功率、用户效用和提供者效用；实验表明Fixed_RV_Proposed在成功率与效用上优于两个基准，动态调整进一步提升成功率。
- Decision: 该文核心目标是确定组合软件服务中各组件服务的保留值，以最大化自动化协商成功概率，并在仿真中通过成功率、用户效用和提供者效用等确定性可计算指标进行评价，属于完全客观指标提升。作者没有并列主观体验或理论机制贡献。实验部分明确以两个自建基准方法（Global_RV_Bench、Component_RV_Bench）进行系统的benchmark比较，该比较直接支撑核心成功率提升主张，且存在明确参照点。因此三部分门槛均通过。
- Confidence: 0.88

## Recommender systems based on quantitative implicit customer feedback

- Year/journal: 2014 / Decision Support Systems
- DOI: 10.1016/j.dss.2014.09.005
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "平均绝对误差（MAE）", "measurement_cn": "在独立验证集上，计算预测的购买数量/播放次数与真实记录值的绝对误差均值；数据来自用户-商品交易或歌曲播放日志。", "objectivity_reason_cn": "预测目标是客观可审计的计数数据（销售量、播放次数），MAE 由确定公式和数据库记录计算，不依赖人的感受、语义评价或主观质量判断。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: Echo Nest Taste Profile Subset（随机样本） | Ta-Feng data set | E-Commerce data set（企业私有数据）
- Benchmark evaluation: 在Taste Profile Sample、Ta-Feng和E-Commerce三个真实数据集上，分别用MAE评价基于正态分布、Poisson、inverse Gaussian、gamma分布的矩阵分解方法，并对比用户均值与物品均值预测；Table 2和图7-9表明三种分布扩展均优于正态分布MF基线，且不同数据集上最优分布不同。
- Decision: 客观指标方面，文章以MAE为核心结果指标，数据来自客观的购买次数/播放次数，不涉及主观评价；核心目标与贡献是提升隐式反馈计数数据的预测精度，没有并列的主观或理论核心目标。Benchmark方面，文章在多个命名公开真实数据集上开展系统化比较实验，以正态分布MF、用户/物品均值等为明确参照，MAE结果表明所提分布扩展带来一致提升，该benchmark评价直接支撑核心改进主张。因此满足两个模块的全部门槛。
- Confidence: 0.88

## Time-aware cloud service recommendation using similarity-enhanced collaborative filtering and ARIMA model

- Year/journal: 2018 / Decision Support Systems
- DOI: 10.1016/j.dss.2017.12.012
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "MAE（平均绝对误差）", "measurement_cn": "在WS-DREAM数据集上，比较真实QoS值与预测QoS值，按公式(9)计算平均绝对误差", "objectivity_reason_cn": "QoS值是外部测量的响应时间和吞吐量，误差计算完全客观可审计"}, {"name_cn": "RMSE（均方根误差）", "measurement_cn": "在WS-DREAM数据集上，按公式(10)计算预测值与真实值的均方根误差", "objectivity_reason_cn": "基于真实QoS值的量化误差，不依赖人的感受或语义判断"}, {"name_cn": "NDCG（归一化折损累计增益）", "measurement_cn": "基于真实QoS值生成理想排序，按公式(11)-(12)计算推荐列表与理想排序的排名质量", "objectivity_reason_cn": "排序相关性基于可核验的QoS数值，不涉及主观偏好或质量评分"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: WS-DREAM
- Benchmark evaluation: 在WS-DREAM公开数据集上，作者抽取120*500*64的响应时间和吞吐量矩阵，模拟不同矩阵密度，将taSR与UPCC、IPCC、WSRec、AVG以及Kalman方法在MAE、RMSE和NDCG@10/30/50上进行比较，结果显示taSR在多数设置下获得更好性能。
- Decision: 客观指标方面：核心成功指标MAE、RMSE和NDCG均基于外部可核验的QoS测量值，不依赖人类体验或语义评价，属于完全客观指标。唯一核心目标方面：全文研究问题、方法设计、实验评价和贡献声明均围绕提升QoS预测准确性和推荐排序性能，没有与客观指标提升并列的主观结果、理论贡献或政策建议。Benchmark方面：文章虽未使用“benchmark”字样，但在实验部分明确命名公开领域标准数据集WS-DREAM作为评价场地，并在该数据集上与多个明确baseline（UPCC、IPCC、WSRec、AVG、Kalman）比较MAE/RMSE/NDCG，benchmark评价直接支撑核心性能提升主张，满足命名式benchmark表述的等价要求。因此两个模块均通过，strict_include为true。
- Confidence: 0.88

## USING FORUM AND SEARCH DATA FOR SALES PREDICTION OF HIGH-INVOLVEMENT PROJECTS

- Year/journal: 2017 / MIS Quarterly
- DOI: 10.25300/misq/2017/41.1.04
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "汽车品牌月度销量预测误差（MAPE）", "measurement_cn": "使用 Automotive News 实际美国月度销量作为真实值；以预测月份前24个月数据训练，对 t=25,…,36 个月进行滚动窗外样本预测；计算实际去归一化销量上的平均绝对百分比误差（MAPE）。", "objectivity_reason_cn": "销量是外部可审计的单位销售事实，MAPE 由确定公式从实际销量与模型预测值计算，不依赖人的感受、意义理解或语义评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: Benchmark Model（作者定义的内部基准模型：消费者情绪指数、汽油价格、季节项 Sales_{i,t-12} 与历史销量）
- Benchmark evaluation: 在23个美国汽车品牌月度销量数据上，以滚动窗口外样本 MAPE 对 benchmark model、forum-based、extended forum-based、search trends-based 和 combined 五种模型进行系统比较；核心结论是 combined model 相对 benchmark model（以及 forum-only 模型）显著降低 MAPE。
- Decision: 客观指标：核心成功指标为实际汽车销量上的 out-of-sample MAPE，销量为单位销售事实，MAPE 可确定计算，不依赖主观评价。唯一核心目标：全文以预测准确性为研究问题、设计目标和贡献声明，未设置主观结果或理论机制等并列核心贡献。Benchmark：作者在评价语境中明确使用“benchmark model/benchmark data”，将 combined/forum/search 模型与基准模型进行 MAPE 比较，benchmark 结果直接支持核心提升主张，且有明确参照点。因此两个模块均通过。
- Confidence: 0.88

## Database design in the modern organization—identifying robust structures under changing query patterns and arrival rate conditions

- Year/journal: 2004 / Decision Support Systems
- DOI: 10.1016/s0167-9236(03)00048-4
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "查询平均处理时间", "measurement_cn": "在Oracle数据库上逐一执行520个生成查询，对96种数据库结构采集处理时间；在无排队环境下计算平均处理时间 x̄。", "objectivity_reason_cn": "处理时间由数据库系统实际执行日志决定，是可审计的技术性能事实，不依赖人的感受或语义判断。"}, {"name_cn": "平均系统时间（处理时间+排队等待时间）", "measurement_cn": "将实测处理时间分布代入M/G/1排队模型的Pollaczek-Khinchin公式，按不同到达率λ计算系统时间。", "objectivity_reason_cn": "由实测处理时间、到达率和数学排队公式计算得出，属于可直接验证的技术绩效指标。"}, {"name_cn": "利用率/拥塞水平", "measurement_cn": "按 ρ = λ x̄ 计算系统利用率，用于衡量不同到达率下的拥塞程度。", "objectivity_reason_cn": "由客观到达率和处理时间决定，是对系统负载的确定性描述。"}, {"name_cn": "相对低效/切换损失", "measurement_cn": "将非最优结构与最优结构的平均系统时间比较，报告相对劣化百分比（如选择DBS6代替DBS1导致270%的低效）。", "objectivity_reason_cn": "基于客观性能数字的比率计算，用来证明结构选择的性能提升。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 作者构造了520个查询组成的基准查询集，涵盖52种查询类型；96种候选数据库结构均在Oracle上执行该基准集。按总处理时间选出前五名结构（DBS1-DBS5），与原规范化结构DBS6及其他代表百分位的结构比较；随后在211种查询模式和不同到达率条件下，用排队模型计算平均系统时间，识别DBS3（低复杂度组最优）和DBS1（其他组最优）作为稳健结构。
- Decision: 核心指标为查询处理时间和系统时间，属于完全客观、可测量、不依赖人类感知或语义判断的技术绩效；全文研究问题、评价结构和贡献声明均围绕识别稳健数据库结构这一目标展开，且不存在并列主观或理论核心贡献。虽然未使用公开命名的benchmark数据集，但作者明确使用“our benchmark queries”作为评价工具，在96种结构间比较总处理时间并以DBS1-DBS5、DBS6等为参照点，评价结果支持本文关于稳健结构性能提升的核心主张，因此满足benchmark门槛。
- Confidence: 0.87

## Empirical evaluation of an automated intraday stock recommendation system incorporating both market data and textual news

- Year/journal: 2014 / Decision Support Systems
- DOI: 10.1016/j.dss.2013.09.013
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "投资回报率（Returns）", "measurement_cn": "基于NYSE TAQ真实买卖报价和交易数据模拟日内交易，按买卖价差和经纪费用扣除交易成本，汇总独立验证月（8.5个月）的总收益率；对初始资金10万至50万美元重复模拟。", "objectivity_reason_cn": "收益率由实际市场报价、交易成本与固定模拟规则决定，不依赖人的感受、意义理解或价值判断，可直接审计和复算。"}, {"name_cn": "夏普比率（Sharpe ratio）", "measurement_cn": "基于每日模拟资金曲线计算收益与风险的比率并年化；数据来源为模拟交易结果，反映风险调整后的交易表现。", "objectivity_reason_cn": "夏普比率由客观可验证的收益序列和波动率计算得到，不涉及主观体验或语义评价。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: S&P 500 index benchmark / S&P 500 SPY index benchmark
- Benchmark evaluation: 在结果部分，将NN算法在market data基础上的不同文本数据表示（news count、categories、sentiment、calibrated sentiment）上得到的Returns和Sharpe ratio，与S&P500指数基准对比。结果显示，采用NN算法并加入更高级文本表示后，模型收益和Sharpe ratio超过S&P500基准，且文本表示越高级差距越大；最佳配置达到统计显著正收益。
- Decision: 客观指标方面：核心成功指标是投资回报率和夏普比率，由真实市场报价、交易成本与固定模拟规则确定，完全客观且不依赖主观评价；核心目标是评估/改进日內股票推荐系统的客观交易表现，技术贡献均服务于该目标。Benchmark方面：文章在结果部分明确使用S&P500指数作为benchmark，将NN模型在不同文本数据表示下的收益和Sharpe比率与该基准比较，并以该比较支撑‘高级文本表示显著提升股票购买决策’的核心主张；有明确参照点（S&P500指数基准和市场数据only基线）。因此两个模块均通过，strict_include=true。
- Confidence: 0.87

## GASP: A Graph Augmentation-Based Approach for Sign Prediction of Ties in Social Networks

- Year/journal: 2025 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00941
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "准确率", "measurement_cn": "在平衡数据集中，对未标记边预测为正或负标签的正确比例，基于实际边标签计算。", "objectivity_reason_cn": "边符号是数据集中已有的离散标签（如信任/不信任、朋友/敌人、支持/反对、遗传互作正/负），预测结果可通过真实标签直接核验，不依赖人的主观评分。"}, {"name_cn": "优化精度", "measurement_cn": "平衡数据集中用于综合评价正类和负类分类性能的精度指标，基于混淆矩阵计算。", "objectivity_reason_cn": "由分类结果和真实标签确定性计算，属于可审计的分类性能。"}, {"name_cn": "宏平均F1", "measurement_cn": "不平衡数据集中，对正类和负类分别计算F1后取平均，衡量两类都重要的分类性能。", "objectivity_reason_cn": "基于真实标签和预测结果的统计量，客观可计算。"}, {"name_cn": "特异性与负预测值的几何均值", "measurement_cn": "不平衡数据集中，专门评估少数类（负类或正类）预测性能的指标，由混淆矩阵计算。", "objectivity_reason_cn": "由真实标签和预测结果确定，客观可审计。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: Epinions | Wikipedia Requests for Adminship (RfA) | Slashdot Zoo | Yeast Genetic Interaction Network (GIN)
- Benchmark evaluation: 在Epinions、Wikipedia RfA、Slashdot Zoo、Yeast GIN四个公开基准网络上，以不同比例标注边（60%-80%）评估GASP，并与NPECF、SRWR、ASiNE、DDRE四个SOTA方法比较。平衡数据集使用accuracy和optimized precision，不平衡数据集使用macro F1和GM(特异性, NPV)。结果显示GASP在绝大多数设定下均优于其他方法。
- Decision: 客观指标方面：核心成功指标为边符号预测的accuracy、optimized precision、macro F1和GM，均基于数据集中已有的离散标签计算，不依赖人主观评分或语义评价，属于客观固定事实标签上的分类性能。唯一核心目标方面：研究问题、设计目标、评价和贡献均围绕‘提升符号预测性能’，理论/实践贡献为附属论述，未构成并列核心成功标准。Benchmark方面：全文存在明确的benchmark表述（摘要和Section 5.1），在评价语境中使用，在命名公开基准数据集（Epinions、Wikipedia RfA、Slashdot Zoo、Yeast GIN）上评价GASP并与NPECF、SRWR、ASiNE、DDRE等明确参照点比较，benchmark结果直接支撑核心性能提升主张。因此strict_include=true。
- Confidence: 0.87

## Identification of influencers — Measuring influence in customer networks

- Year/journal: 2008 / Decision Support Systems
- DOI: 10.1016/j.dss.2008.06.007
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "消息扩散到达的客户数（reach）", "measurement_cn": "通过计算机仿真：用不同中心性指标选择初始客户集合，在电信真实网络与模拟网络上运行扩散模型，统计平均10轮模拟后被到达的客户数量，并以增益曲线和lift呈现。", "objectivity_reason_cn": "该指标由定义明确的扩散模型和网络数据计算得到，是仿真系统可审计的输出；不涉及人对质量、价值或偏好的评价。扩散参数中的随机性不影响其客观可计算性。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 无公开命名基准数据集；使用电信运营商真实数据样本NW1-NW4及模拟网络NW5-NW9作为实验场地
- Benchmark evaluation: 在9个网络（真实电信网络与模拟scale-free/ER网络）上，以11种中心性指标/基线选择初始客户，在11组扩散模型参数下比较最终到达客户数，并用增益曲线和lift展示相对随机选择和各指标间的差异。
- Decision: 客观指标方面：核心结果指标是消息扩散到达客户数，来自明确定义的计算机仿真，不依赖人的感受或语义判断，属于完全客观指标；且该指标提升是全文唯一核心目标与贡献。Benchmark方面：论文在Section 1.4明确说明用“computational experiments to benchmark different centrality measures”，实验位于评价语境，且在各网络/扩散模型下与随机选择及其他中心性指标比较，证明中心性选择带来的到达数提升。因此两个模块均通过，strict_include为true。
- Confidence: 0.87

## Modeling Fixed Odds Betting For Future Event Prediction1

- Year/journal: 2017 / MIS Quarterly
- DOI: 10.25300/misq/2017/41.2.14
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "未来事件预测准确性（QSR/LSR/SSR 评分规则）", "measurement_cn": "模型输出事件概率，与事后真实事件结果（实际赢家/输家）对比计算。QSR=100-400×p_lose^2；LSR=100+144.27×log(1-p_lose)；SSR=-241.42+341.42×(1-p_lose)/sqrt(p_A^2+p_B^2)。分数越高预测越准确。", "objectivity_reason_cn": "事件结果是外部可核验的事实，评分只依赖模型概率与实际结果，不涉及人类感受、偏好或语义质量判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在三个真实数据集（sina 2008 Olympic Games、sohu Entertainment Events、sohu 2014 FIFA）上，将BD-ML/BD-AIC与bookmaker/betting line、BetRatio、ReducedForm1-4、ReducedFormSimu以及Inklingmarkets.com auction-based prediction market进行比较，采用QSR/LSR/SSR。Table 2显示BD模型显著优于各benchmark模型；Table 1显示与auction市场可比。
- Decision: 核心指标为未来事件预测的QSR/LSR/SSR评分，完全依赖外部真实事件结果，客观可计算；预测性能提升是全文唯一核心目标和贡献。全文在评价语境中明确使用benchmark一词（four benchmark models、best benchmark），将所提BD模型与多个baseline/reduced-form/auction机制比较，并以该比较作为核心性能提升的证据。因此两个模块均通过。
- Confidence: 0.87

## Using similarity measures for medical event sequences to predict mortality in trauma patients

- Year/journal: 2019 / Decision Support Systems
- DOI: 10.1016/j.dss.2018.10.008
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "死亡率预测判别性能（AUC/ROC/operating points）", "measurement_cn": "使用National Trauma Data Bank 2015创伤数据，以出院死亡（deceased/non-deceased）为事实标签，比较TMPM与OTCS、OTCS-MES EP、OTCS-MES ES及集成kNN分类器的AUC、ROC曲线、Youden指数、weighted Youden和Neyman-Pearson operating points；AUC差异采用Mann-Whitney置信区间检验。", "objectivity_reason_cn": "死亡结局是创伤登记中的外部事实标签，不依赖人的感受、语义评价或价值判断；AUC、ROC和operating points由预测分数与死亡标签按确定公式计算，数值可复现、可审计。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: National Trauma Data Bank (NTDB) | Retrospective mortality prediction benchmarking task
- Benchmark evaluation: 在NTDB 2015创伤数据上（50,000训练案例、2,000测试案例）系统评价TMPM、原始OTCS、OTCS-MES EP、OTCS-MES ES和集成kNN分类器的死亡率预测性能，主要比较AUC、ROC曲线和operating points。结果显示集成分类器AUC 0.8589显著优于TMPM的0.8392（p=0.0037），并在加权Youden和Neyman-Pearson标准下相对TMPM有优势。
- Decision: 客观指标门槛通过：核心结果是创伤患者死亡这一事实标签上的预测性能，测量为AUC、ROC曲线和operating points等可审计的客观指标，全文没有主观评分或满意度作为成功标准。唯一核心目标通过：研究问题、实验设计和贡献声明一致地将“用MES相似性方法提升创伤死亡率预测性能（尤其优于TMPM）”作为唯一核心目标；其余贡献明确为次要贡献。benchmark门槛通过：文章明确将retrospective mortality prediction称为benchmarking task，并在公开数据源National Trauma Data Bank上以TMPM、原始OTCS等为明确参照进行系统比较，benchmark结果是支撑核心提升主张的关键证据。因此strict_include=true。
- Confidence: 0.87

## An empirical study of natural noise management in group recommendation systems

- Year/journal: 2017 / Decision Support Systems
- DOI: 10.1016/j.dss.2016.09.020
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "平均绝对误差（MAE）预测误差", "measurement_cn": "在MovieLens 100k和Netflix Tiny上，按GRS评估协议划分训练/测试集，随机生成组，结合IB/UB与Avg/Min聚合方式生成推荐，将预测评分与测试集中用户实际评分比较，计算MAE。", "objectivity_reason_cn": "MAE由系统预测评分与用户实际评分之间的绝对误差决定，是确定性、可审计的技术指标；不依赖第三方质量判断、满意度或主观语义评价。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: MovieLens 100k dataset | Netflix Tiny dataset
- Benchmark evaluation: 在MovieLens 100k和Netflix Tiny两个公开数据集上，对推荐聚合和评分聚合两类GRS，结合IB/UB与Avg/Min聚合，报告Base、NNM-LL、NNM-LG、NNM-GG、NNM-H的MAE；结果以Base为参照，验证NNM-GG和NNM-H降低MAE，且NNM-H在多数IB配置下优于NNM-GG。
- Decision: 客观指标方面，MAE是系统预测评分与测试集实际评分之间的确定性误差，不依赖人类语义评价或主观感受；全文唯一核心目标是将自然噪声管理引入GRS并提升预测精度，无并列的主观或理论核心贡献。Benchmark方面，论文虽然没有使用benchmark一词，但在评价语境中明确使用MovieLens 100k和Netflix Tiny两个公开基准数据集作为评价场地，并与Base基线及方法间进行配对t检验比较，结果直接支撑NNM-GG和NNM-H降低MAE的核心主张。因此两个模块均通过，strict_include为true。
- Confidence: 0.86

## Designing Personalized Treatment Plans for Breast Cancer

- Year/journal: 2021 / Information Systems Research
- DOI: 10.1287/isre.2021.1002
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "平均辐射剂量（AvgDose，Gy）", "measurement_cn": "由最优剂量分布和乳房组织体积按公式计算，如Table 3/4中的平均剂量；对照标准均匀计划。", "objectivity_reason_cn": "辐射剂量是物理可测量值，不依赖人的感受或语义判断，可通过剂量分布函数和体积数据确定性地计算。"}, {"name_cn": "肿瘤控制概率（TCP）", "measurement_cn": "基于TCP模型（公式3）计算的约束目标值，评价中以TCP目标（90%/80%）作为优化约束。", "objectivity_reason_cn": "TCP是模型输出的概率数值，基于剂量和肿瘤细胞参数计算，不是主观评价构念。"}, {"name_cn": "放疗相关肺癌/心脏病风险", "measurement_cn": "通过文献中的线性剂量-风险关系（Grantzau et al. 2014; Darby et al. 2013）从平均剂量降低推算出的风险降低百分比。", "objectivity_reason_cn": "风险变化由已发表的客观流行病学剂量反应关系计算，不依赖人类主观判断。"}, {"name_cn": "治疗成本节省", "measurement_cn": "用预期新发乳腺癌人数、风险降低比例和已知治疗成本进行乘数估算，得到每年节省的美元数额。", "objectivity_reason_cn": "成本节省由客观流行病学风险和公开治疗成本数据算术推算，属于可审计的经济结果。"}, {"name_cn": "计算时间", "measurement_cn": "在统一计算机硬件上运行优化算法所需分钟数（Table 5/6）。", "objectivity_reason_cn": "计算时间是机械、可复现的物理客观指标。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在Section 4.1基线评估中，比较标准均匀计划与框架生成的无约束/约束最优计划，在TCP目标90%/80%和三种误差设置下报告平均剂量（Tables 3-4）。在Section 4.2中，将Adam优化方法与L-BFGS-B、模拟退火（SA）、遗传算法（GA）在平均剂量和计算时间上比较（Tables 5-6）。在Section 4.3，将剂量降低转化为临床风险和治疗成本节省。这些比较直接支撑了核心改进主张：框架生成的计划能以更低剂量达到相同TCP并降低成本。
- Decision: 客观指标门通过：核心成功指标为平均辐射剂量、TCP目标约束、剂量-风险推算的疾病风险和成本节省，均为物理/经济/可审计的客观指标，不涉及人类感受或语义判断。唯一核心目标门通过：研究问题、设计目标、评价结构和贡献声明均围绕用预测+优化框架提升放疗计划的客观结果，没有并列的主观体验、理论机制或政策目标。Benchmark门通过：Section 4明确使用benchmark/benchmarking语境，并开展标准均匀计划与非约束/约束最优计划、Adam与L-BFGS-B/SA/GA的系统比较；这些比较提供明确参照点，直接支撑核心改进主张。因此strict_include=true。
- Confidence: 0.86

## Evaluating and Tuning Predictive Data Mining Models Using Receiver Operating Characteristic Curves

- Year/journal: 2004 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2004.11045815
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "AUC（ROC曲线下面积）", "measurement_cn": "基于每个分类器在测试集上的预测输出与真实好坏标签计算ROC曲线，并求曲线下面积；用Hanley-McNeil方法对成对AUC进行显著性比较。", "objectivity_reason_cn": "好坏贷款/信用风险是外部可核验的历史事实标签，AUC由混淆矩阵中的计数推算，不依赖人的感受、偏好或语义评价。"}, {"name_cn": "期望误分类成本（expected misclassification cost）", "measurement_cn": "在设定的假阴性成本c01、假阳性成本c10和先验概率p1、p0下，用混淆矩阵的敏感度与特异度按Cost公式计算；跨25个成本—概率比比较。", "objectivity_reason_cn": "成本和先验是明确设定的数值，混淆矩阵来自事实标签，成本计算完全确定，不涉及主观构念。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: Statlog German credit data set
- Benchmark evaluation: 在Statlog German credit 数据集上开发NN、LR、LDA、DT和kNN模型，用ROC/AUC、期望成本、泛化性和鲁棒性比较模型；结果显示NN和LR的AUC最高，DT和kNN泛化较差，LR在多数成本情景下期望成本最低。该评价是支撑“LR/NN性能优越、阈值后调有效”核心主张的关键证据。
- Decision: 客观指标方面，核心指标为AUC和期望误分类成本，均基于外部可核验的好坏贷款/信用风险事实标签和混淆矩阵计数计算，不依赖主观感知或语义评价；全文唯一核心目标是提升最小化误分类成本这一客观性能，且无并列主观或理论目标。Benchmark方面，文章明确命名公开的Statlog German credit数据集并将其作为主要评价场地，在该基准上对五种方法进行AUC和期望成本的系统比较，比较对象包括方法互比、随机对角线、默认阈值和训练/测试对照，benchmark结果直接支撑“LR/NN性能优越、后调阈值有效”的核心主张。因此两个模块均通过，strict_include为true。
- Confidence: 0.86

## Financial news-based stock movement prediction using causality analysis of influence in the Korean stock market

- Year/journal: 2019 / Decision Support Systems
- DOI: 10.1016/j.dss.2018.11.004
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "股票涨跌方向预测准确率（Accuracy）和 F1-score", "measurement_cn": "每个新闻数据点按当日收益率（Close/Open 是否 >=1）标记为 Up/Down；在2016年下半年的测试集上计算分类准确率和 F1-score。", "objectivity_reason_cn": "涨跌标签直接来源于可审计的股价数据，预测性能由实际价格标签计算，不依赖人的感受、语义理解或价值判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在 Pharmacy 板块上，除因果检测方法不同外，文本预处理、MKL、网格搜索等流程均相同，比较 Proposed Method 与 Oh et al. [33]（只考虑单向因果）和 Výrost et al. [29]（Granger causality）的股票涨跌预测精度。Table 11 显示 Proposed Method 平均准确率 0.584381，高于 Oh et al. 的 0.564935 和 Výrost et al. 的 0.573040。
- Decision: 核心指标是股票涨跌方向预测的 Accuracy 和 F1-score，其标签来自股价收益，是可审计的客观事实；全文唯一核心目标是提升该预测性能，不存在主观指标或并列核心目标。存在明确的 benchmark 表述（Section 4.2 'we benchmark with two state-of-the-art causality detection papers'），处于评价语境，并有明确比较对象（Oh et al. 和 Výrost et al.），结果用于支持本方法在预测性能上的提升。因此 strict_include=true。
- Confidence: 0.86

## Network optimization in supply chain: A KBGA approach

- Year/journal: 2012 / Decision Support Systems
- DOI: 10.1016/j.dss.2011.10.024
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "总平均成本/单位满足需求成本", "measurement_cn": "由式(1)计算，即各项成本（订货、采购、运输、库存、惩罚等）除以已满足需求量；在仿真/数值实验中根据供应商选择、运输方式、需求实现和缺货量确定。", "objectivity_reason_cn": "该值由确定性的成本参数、数量参数和损失需求量计算得到，不依赖人的感受、语义评价或主观质量判断。"}, {"name_cn": "需求满足率", "measurement_cn": "由式(2)计算，即(总需求-损失需求)/总需求；在仿真或数值实验中记录需求和缺货量。", "objectivity_reason_cn": "需求量和缺货量是可审计的外部事实类数值，满足率是确定性的比例计算，客观可验证。"}, {"name_cn": "算法收敛代数/收敛速度", "measurement_cn": "记录KBGA达到收敛或满意解所需的进化代数；文中报告KBGA在d=300时144代收敛，而SGA约2000代收敛。", "objectivity_reason_cn": "收敛代数是算法执行过程的确定性计数，不受人类体验或语义评价影响。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: Ding et al. [18] 的 Classic boots 供应链数值算例（需求 d=300）
- Benchmark evaluation: 将Ding et al. [18] 的Classic boots供应链问题作为基准算例，将KBGA与SGA/文献已有结果比较：KBGA在d=300时144代收敛而SGA约为2000代；KBGA可达到接近100%的需求满足率，而SGA仅搜索到97.2%；KBGA给出的再订货点和订货量也更低。另在d=400和500上检验了KBGA的收敛性能。
- Decision: 文章以供应链网络优化为背景，核心贡献是提出KBGA并在Ding et al.基准算例上对比SGA。核心成功指标包括总平均成本、需求满足率和收敛代数，均为可审计的客观数值指标；没有主观量表或人类语义判断作为成功标准。唯一核心目标是提升这些客观指标。虽然显式使用benchmark一词的句子位于引言，但它直接预告并支撑第9节的基准评价；该基准评价与SGA明确比较，且正是支撑核心改进主张的关键证据。因此两个模块均通过，strict_include=true。
- Confidence: 0.86

## Service Agreement Trifecta: Backup Resources, Price and Penalty in the Availability-Aware Cloud

- Year/journal: 2018 / Information Systems Research
- DOI: 10.1287/isre.2017.0755
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "最优备份虚拟机数 k*", "measurement_cn": "通过二分搜索最小化期望总成本 Q_k = hkT + π∫_{ (1-α)T}^{T} v(τ)(τ-(1-α)T)dτ；停机分布来自真实CCR服务器日志数据，并采用分段线性近似。", "objectivity_reason_cn": "备份虚拟机数量是可由系统配置审计的物理/技术事实；成本、罚金、停机时间均由确定公式和日志数据计算，不依赖人的感受、语义或价值判断。"}, {"name_cn": "提供方期望总成本", "measurement_cn": "由预置成本与期望罚金成本加总得到，公式为Q_k；实验中将二分搜索方案与固定比例规则比较，报告期望总成本差值。", "objectivity_reason_cn": "成本是客观财务/运营指标，可在相同输入下由公式和计算实验复现。"}, {"name_cn": "盈亏平衡价格 p'", "measurement_cn": "由期望利润非负条件推导，p' ≥ [h(n+k)T + π∫_{ (1-α)T}^{T} v(τ)(τ-(1-α)T)dτ]/(nT)，结合罚金率和预置成本计算。", "objectivity_reason_cn": "价格是可审计交易/合约指标，由确定的成本、罚金和分布参数计算。"}, {"name_cn": "期望可罚停机时间", "measurement_cn": "由真实服务器日志推导停机概率密度，经分段线性近似后计算超过SLA允许停机时间的期望值。", "objectivity_reason_cn": "停机时间是datacenter日志记录的外部事实，不依赖用户主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在真实CCR服务器日志推导的停机分布下，采用n=50和n=100、T=30天、罚金/预置成本比1:100以及其他比例，将二分搜索算法得到的最优k*与六种固定比例备份规则（10%、15%、20%、25%、30%、35%的n）比较期望罚金成本、预置成本和期望总成本；Figure 9显示二分搜索解的期望总成本低于各基准规则，且该图同时验证期望总成本凸性。
- Decision: 核心指标均为完全客观、可由系统日志和公式复现的指标：备份资源数量、期望总成本、盈亏平衡价格、期望可罚停机时间；文章唯一核心目标是面向SLA的可用性感知资源预置和定价优化，不存在与客观指标提升并列的主观构念或理论解释核心目标。全文存在明确benchmark表述：第6.5节对二分搜索算法与六种固定比例备份规则进行基准比较，并在Figure 9中显示最优解在期望总成本等客观指标上优于基准，该benchmark评价直接支撑核心贡献。故strict_include=true。
- Confidence: 0.86

## A Prescriptive Analytics Framework for Optimal Policy Deployment Using Heterogeneous Treatment Effects

- Year/journal: 2021 / MIS Quarterly
- DOI: 10.25300/misq/2021/15684
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "企业/组织总效用（utility = benefit - cost）", "measurement_cn": "在预算约束下，依据随机现场实验中的实际捐赠量、奖励成本、推荐转化金额、用户获取价值、交易金额等可审计事实，构造个体层面的收益与成本矩阵，进而得到总效用；用于比较HTE-EST与ATE、uplift modeling等策略。", "objectivity_reason_cn": "效用直接由可核验的金额、交易、捐赠和成本数据计算得出，不依赖任何人的感受、偏好或语义评价。"}, {"name_cn": "期望总效用提升", "measurement_cn": "在测试集上对收益/成本矩阵进行优化分配，报告不同预算约束下的期望总效用，并与ATE、uplift modeling和modified LinUCB比较。", "objectivity_reason_cn": "比较结果基于同一客观收益/成本矩阵和确定性优化规则，属于可审计的量化结果。"}, {"name_cn": "模型精度MAE", "measurement_cn": "在测试集上计算收益、成本和效用预测与实际观测值之间的平均绝对误差。", "objectivity_reason_cn": "MAE是基于确定性数值误差计算，不涉及主观质量判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在血液捐赠和推荐营销两个随机现场实验数据上，以预算约束下的期望总效用为核心指标，将HTE-EST与ATE、uplift modeling（以及扩展的modified LinUCB）进行比较。血液捐赠案例中报告HTE-EST比UM高最多240%、比ATE高最多340%，在多个预算约束水平下均优于基准方法。
- Decision: 客观指标方面，核心结果是预算约束下的总效用，由实际捐赠、交易、奖励成本等可审计事实计算得到，不依赖人类主观评价；唯一核心目标是提升该客观效用，框架和OUR指标是实现这一目标的中间工具。Benchmark方面，作者明确使用“benchmark/benchmarking”表述，在实证评价部分将HTE-EST与ATE、uplift modeling、modified LinUCB等明确参照点进行比较，且benchmark比较直接支撑了效用提升的核心主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.85

## A decision maxim for efficient task realization within analytical network infrastructures

- Year/journal: 2018 / Decision Support Systems
- DOI: 10.1016/j.dss.2018.06.005
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "总处理成本（Total processing costs）", "measurement_cn": "由模拟模型根据各系统任务到达率、处理率、单位成本等参数计算得到（如式18及跨系统汇总式28）", "objectivity_reason_cn": "处理成本为可审计的经济/资源消耗量，不依赖人类感受或语义判断"}, {"name_cn": "总流量强度（Total traffic intensity）", "measurement_cn": "由式19计算各系统流量强度并跨系统汇总（式31）", "objectivity_reason_cn": "基于到达率和处理率的确定性队列关系，客观可计算"}, {"name_cn": "等待任务总数（Total number of waiting jobs）", "measurement_cn": "由队列公式（式20-22）计算各系统等待队长并汇总（式29）", "objectivity_reason_cn": "由队列理论公式推导，反映排队长度，客观可测量"}, {"name_cn": "等待总时间（Total time of waiting jobs）", "measurement_cn": "由式23-25计算各系统等待时间并汇总（式30）", "objectivity_reason_cn": "基于队列理论的确定性时间度量，客观可审计"}, {"name_cn": "按时实现的任务数（Total job realization with time）", "measurement_cn": "模拟中统计在截止时间内完成的任务类型数（表4中{7,8}等）", "objectivity_reason_cn": "直接统计是否按时完成，是二值客观事实，不依赖主观评价"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在一个4系统场景中，模拟比较了3种转移策略（new-decision-maxim、workshop-based、no-transfers-at-all）与12种处理策略；表4汇总各转移策略性能，表5按综合目标函数排序所有36种组合；结果显示NDM在所有组合中在按时实现任务数等指标上优于其他策略。
- Decision: 客观指标方面，文中所有核心评价指标均为模拟产生的处理成本、流量强度、等待时间/任务数、按时完成数，不依赖人类主观评价，且性能评估框架服务于客观效率比较；唯一核心目标是设计并验证更高效的任务实现决策准则，未发现并列核心目标。基准方面，摘要明确使用'benchmark'动词陈述模拟对比，第5节构建基准，并在表4/5中与workshop-based和no-transfers-at-all明确比较，结果支撑NDM的核心改进主张，满足明确基准表述并处于评价语境。因此两个模块均通过。
- Confidence: 0.85

## Combinatorial auctions using rule-based bids

- Year/journal: 2002 / Decision Support Systems
- DOI: 10.1016/s0167-9236(02)00004-0
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "拍卖收入（Revenue）", "measurement_cn": "由模拟竞买人的投标金额和最终分配结果计算，即被接受投标的总金额。", "objectivity_reason_cn": "收入是可由投标数据直接计算的可审计货币值，不依赖人类主观感受或语义评价。"}, {"name_cn": "分配效率（Efficiency）", "measurement_cn": "E = 最终配置中获胜投标的保留价值总和 / 在所有可行配置下可达到的最大价值总和，基于模拟中设置的竞买人保留价格/价值参数计算。", "objectivity_reason_cn": "效率由模拟中的固定数值参数按明确公式计算得到，不是专家评分或用户自我报告；结果为可复现的确定性数值。"}, {"name_cn": "最优性（Optimality）", "measurement_cn": "卖方从最终配置中实际捕获的最大可能收入百分比，基于投标价格与保留价值之差计算。", "objectivity_reason_cn": "由投标金额和设定价值按公式计算，属于可审计的量化绩效指标，不依赖人类评价。"}, {"name_cn": "未售库存、拍卖轮数、计算时间及gap", "measurement_cn": "从未售库存单元数、达到停止条件的轮次、启发式计算时间、以及启发式解与上界之间的相对gap等系统记录获得。", "objectivity_reason_cn": "这些均是直接可观察或可计算的系统日志类指标，不涉及主观构念。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 作者将第4节定义的整数规划问题作为基准，在缩小规模的问题（30个投标人、104个单元、3个节目；第3轮12个活跃投标人）上，将ISCA启发式与CPLEX 6.5比较。ISCA在15分钟内完成整个5轮拍卖并找到收入1728.31的解，gap小于0.04%；CPLEX运行43小时未获得可行整数解；用ISCA的解作为初始解后CPLEX 24小时未能改进，且CPLEX报告的初始gap为43.74%，远高于启发式结果。该基准评价用于支撑启发式求解质量和近似最优性的核心主张。
- Decision: 客观指标：收入、效率、最优性、未售库存、轮数、计算时间和gap均由模拟拍卖中的明确数值和公式计算得出，不依赖人类主观评价；唯一核心目标是设计和验证接受规则化投标的ISCA机制及其胜者决定启发式，全文评价与贡献声明均围绕这些客观绩效指标。Benchmark：第7节明确将第4节的整数规划问题作为benchmark，并用CPLEX 6.5作为明确参照点进行比较；该比较支撑了启发式解接近最优且优于难以求解的精确工具的核心主张。两个模块通过，因此 strict_include=true。
- Confidence: 0.85

## Customer Engagement Prediction on Social Media: A Graph Neural Network Method

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2021.0281
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "客户参与预测的准确率、精确率、召回率、F1分数和AUC", "measurement_cn": "基于Facebook品牌帖子的真实互动日志（该用户是否对帖子进行点赞、评论或分享）作为二分类标签，在T4时间窗随机抽样20%为测试集，使用10折交叉验证计算accuracy、precision、recall、F1和AUC。", "objectivity_reason_cn": "预测目标是对品牌帖子是否发生实际互动行为的可审计事实，标签来自平台系统日志，不依赖用户或专家对质量、价值、意义或偏好的主观判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在作者自建的大规模Facebook数据集（47个品牌、91,342用户、35,665帖子、666,188条互动记录）上，将GACE与MLP、DeepWalk、metapath2vec、GraphSAGE、RGCN、HAN、JODIE、MAGNN等baseline进行系统比较，报告accuracy、precision、recall、F1和AUC，并给出相对最优baseline的提升百分比（如准确率提升7.43%，AUC提升4.92%）。该比较构成支撑核心预测性能主张的关键证据。
- Decision: 核心指标为客户参与预测性能，基于Facebook真实互动日志这一可审计事实，完全客观；研究的目标、评价和贡献均以客观预测指标提升为唯一核心，解释性和经济价值分析只是附加说明；虽然未使用公开命名benchmark，但作者在实验部分明确使用“benchmarks”指代baseline并进行系统比较，且该比较直接支撑GACE的预测性能提升主张，因此通过三部分审计。
- Confidence: 0.85

## Dare to share: Protecting sensitive knowledge with data sanitization

- Year/journal: 2007 / Decision Support Systems
- DOI: 10.1016/j.dss.2006.08.007
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "数据效用（Data Utility）", "measurement_cn": "净化后数据库中仍可挖掘的非敏感项集数占原始数据库中非敏感项集数的百分比；由事务中的项集支持数确定。", "objectivity_reason_cn": "项集及其支持计数是事务数据的确定性事实，不依赖人的感受、语义理解或价值判断。"}, {"name_cn": "数据准确度（事务级/项级）", "measurement_cn": "事务级准确度为未被修改的准确事务百分比；项级准确度为未删除项频率的保留比例。", "objectivity_reason_cn": "基于删除操作、实际事务记录和项频数计算，属于可审计的客观结果。"}, {"name_cn": "CPU时间（秒）", "measurement_cn": "各算法在相同机器环境下运行所需的秒数。", "objectivity_reason_cn": "程序运行时间是可复现、可测量的技术性能指标；本文将其报告为效率代价，而非核心贡献目标。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: FIMI repository中的bms1、bms2和retail数据集 | UCI Machine Learning Repository中的chess和mushroom数据集
- Benchmark evaluation: 在bms1、bms2、retail、chess、mushroom五个公开真实数据集上，以多个支持度阈值运行Aggregate、Hybrid、Disaggregate和SWA，报告数据效用、事务级/项级准确度和CPU时间。结果显示三种方法平均数据效用分别为45.82%、78.44%、79.60%，均显著高于SWA的27.73%，其中Disaggregate和Hybrid效用最高。该比较直接支撑本文的核心主张。
- Decision: 客观指标层面：数据效用、数据准确度和CPU时间均由事务数据、项集支持数、删除操作或运行时间直接计算，不涉及主观感知或语义判断，全部核心成功结果均为客观指标。唯一核心目标层面：全文研究问题、方法设计、实验评价和贡献声明均围绕在隐藏敏感项集的前提下最大化数据效用，并声称所提方法优于SWA；数据准确度被明确称为辅助说明信息，CPU时间是权衡代价而非核心目标，不存在并列的主观、理论或制度性核心贡献。Benchmark层面：作者在FIMI和UCI的公开真实数据集（bms1、bms2、retail、chess、mushroom）上对三种方法与SWA进行系统比较，表4/表5结果直接支撑核心提升主张，且存在明确的参照点SWA；尽管全文没有使用‘benchmark’一词，但这属于明确命名公开标准数据集并作为评价场地的命名式benchmark表述。因此两个模块均通过，strict_include为true。
- Confidence: 0.85

## Discovering near-optimal pricing strategies for the deregulated electric power marketplace using genetic algorithms

- Year/journal: 1999 / Decision Support Systems
- DOI: 10.1016/s0167-9236(99)00035-4
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "GA 解相对于 GAMS 精确最优解的社会福利误差率（%）", "measurement_cn": "在 48 个随机生成的六节点电力网络 AFBP 场景中，先用 GAMS 计算精确最优解，再运行 GA-1，读取其最优适应值，计算（最优值- GA 值）/最优值 × 100%", "objectivity_reason_cn": "社会福利值由确定性优化模型（式 2-9）定义，GAMS 和 GA 均通过程序计算输出数值，不依赖任何人类感受、语义评价或质量判断"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在作者随机产生的六节点电力网络测试场景（3 个测试集共 48 个问题）上，将 GA-1 结果与 GAMS 求得的 AFBP 精确最优解比较，报告各场景误差率，并讨论 static/dynamic/death penalty 等替代约束处理机制的失败表现。
- Decision: 客观指标方面：核心成功指标是 GA 求解出的社会福利接近 GAMS 精确最优解的程度，该数值由确定性优化模型和算法计算，独立于人类感知，属于完全客观的直接指标；全文评价结构、研究问题和贡献声明均围绕这一客观性能提升，没有主观量表或并列核心目标。Benchmark 方面：作者在 4.4 节明确使用 benchmark 一词表述以 GAMS 最优解作为基准评价 GA 性能，该表述位于实验设计/评价语境，其误差率结果直接支撑'GA-1 能发现近优解'的核心主张，且以 GAMS 最优解（以及惩罚函数方法）为明确参照点。两个模块均通过，因此 strict_include=true。
- Confidence: 0.85

## Dynamic self-organizing feature map-based models applied to bankruptcy prediction

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113576
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "正确分类率 (Correct Classification Rate)", "measurement_cn": "在测试样本上，模型预测的破产/非破产状态与 Diane 数据库中企业真实法律状态的匹配比例；结果在 100 个 bootstrap 测试子样本上取平均。", "objectivity_reason_cn": "破产状态是外部可核验的法律/事实状态，不依赖人类感受或语义评价；正确分类率是从确定事实标签中计算的确定性指标。"}, {"name_cn": "F2-score", "measurement_cn": "精确率与召回率的加权调和平均，权重偏向召回率（破产企业正确识别）。基于测试样本中的真实破产标签计算。", "objectivity_reason_cn": "基于破产事实标签计算，不依赖主观判断。"}, {"name_cn": "AUC (Area Under the ROC Curve)", "measurement_cn": "在不同阈值下真正例率与假正例率的曲线下面积，基于模型排序和真实破产标签计算。", "objectivity_reason_cn": "基于事实标签的排序质量，客观可计算。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 作者将动态模型与传统单一模型（Cox、SVM、ELM）和集成模型（bagging、AdaBoost、XGBoost、random subspace、random forest）作为基准进行比较，在 4 个时期的多组全体样本和分行业样本上报告正确分类率、F2 和 AUC。结果显示动态模型在多数情况下显著优于所有基准（例如表10全体样本平均正确分类率84.35%对最好基准80.34–81.08%；F2平均82.02%对76.73–80.34%）。
- Decision: 本文核心目标是构建并验证一种利用历史数据与数据分割的破产预测集成方法，核心成功指标是完全客观的预测性能指标（正确分类率、F2、AUC），破产标签是外部事实标签，不存在主观结果作为成功标准。唯一核心目标是客观指标提升。作者在方法部分明确以‘models used as a benchmark’陈述基准模型设置，并在后续实验中将动态模型与多种传统模型进行比较，结果为核心提升主张提供关键证据，且有明确比较对象。因此客观指标与 benchmark 门槛均通过。
- Confidence: 0.85

## Efficient classifiers for multi-class classification problems

- Year/journal: 2012 / Decision Support Systems
- DOI: 10.1016/j.dss.2012.02.014
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "分类准确率", "measurement_cn": "在五个公开数据集上采用10折交叉验证，比较原始特征F和本文选择特征F^下C4.5、CART、SVM、NaiveBayes及HLMC的正确分类比例。", "objectivity_reason_cn": "由固定类标签与分类器输出直接统计，不依赖人的感受、偏好或语义评价。"}, {"name_cn": "ROC面积", "measurement_cn": "根据TPR与FPR绘制ROC曲线并计算曲线下面积，衡量判别能力。", "objectivity_reason_cn": "由固定事实标签和分类器输出计算，客观可复现。"}, {"name_cn": "假阳性率FPR", "measurement_cn": "在ROC分析中计算误将负类判定为正类的比例。", "objectivity_reason_cn": "基于分类结果与固定标签直接计算，可审计。"}, {"name_cn": "训练时间", "measurement_cn": "在同一工作站上记录各分类器建模耗时，单位为秒。", "objectivity_reason_cn": "由系统计时直接获得，不依赖人类体验或主观判断。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: segment | satimage | places | German credit | vehicle
- Benchmark evaluation: 在segment、satimage、places、German credit、vehicle五个公开标准数据集上，分别用原始特征F和本文选择特征F^训练C4.5、CART、SVM、NaiveBayes，并训练本文HLMC；以准确率、ROC面积、FPR和训练时间为主要结果，比较显示F^大幅缩短训练时间且准确率几乎不损失，HLMC判别能力优于多个传统分类器。
- Decision: 该文以提升分类训练效率、保持/改善准确率和判别能力作为唯一核心目标，所有核心成功指标均为客观可计算指标；评价在公开标准数据集segment、satimage、places、German credit、vehicle上进行，并与多种显式baseline比较，benchmark评价支撑其核心改进主张。因此满足严格纳入条件。
- Confidence: 0.85

## First, Do No Harm: Predictive Analytics to Reduce In-Hospital Adverse Events

- Year/journal: 2021 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2021.1990619
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "住院不良事件（AE）预测的 AUC、精确率、召回率、F-score", "measurement_cn": "基于佛罗里达州 AHCA 心衰住院出院记录，用高 PPV 的 UMAEC ICD-9-CM 编码且非 POA 的 AE 作为标签，按时间分割训练/测试集，计算各类 AE 的 AUC、precision、recall、F-score", "objectivity_reason_cn": "AE 标签是可核验的医疗事实（由高 PPV 诊断代码和入院时是否存在指示判定），不依赖人的感受、偏好或语义评价；预测表现是确定的统计计算"}, {"name_cn": "模拟应用中预防的 AE 数与假警报数、成本节省金额", "measurement_cn": "通过模拟在入院时使用模型发出警报，统计被预防的 AE 数量、假警报数量，并按公开文献中的 AE 成本与团队工时估算成本节省", "objectivity_reason_cn": "被预防 AE、假警报、成本节省均可由模拟流程与可审计的成本参数计算，不涉及主观体验或价值判断"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在佛罗里达 AHCA 心衰住院数据测试床上，采用时间前后分割，比较 SALT 与多个基准/替代模型在 AUC、F-score、precision、recall 上的表现，并用模拟评估预防 AE 与假警报；这些对比是证明 SALT 预测性能提升和实践价值的关键证据。
- Decision: 客观指标方面：文章核心目标是预测住院期间由医疗错误导致的不良事件（AE），标签基于高 PPV 的 ICD 编码和 POA 指示，是可核验的医疗事实；所有主要成功指标（AUC、precision、recall、F-score、预防 AE 数、假警报数、成本节省）均客观可计算，不依赖主观体验或语义评价。唯一核心目标：研究问题、设计目标、评价实验与贡献声明均围绕提高 AE 预测性能和相应的客观临床/经济效用展开，没有并列的主观成功标准或理论解释核心目标。Benchmark 方面：正文实验部分明确将比较对象称为“benchmarks”，并且系统比较了 GLMM、MERT、MERF、CART、DNN、GBM、LR、NB、RF、SVM 等基线/替代方法，结果用于支撑 SALT 预测性能提升这一核心主张，存在明确参照点。因此两个模块均通过，strict_include=true。
- Confidence: 0.85

## Hiding Sensitive Information when Sharing Distributed Transactional Data

- Year/journal: 2020 / Information Systems Research
- DOI: 10.1287/isre.2019.0898
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "数据准确性 accuracy（未被消毒交易的比例）", "measurement_cn": "由 FIH_D 整数规划的目标函数衡量，即需要被消毒的交易数占交易总数的比例；文章直接报告被消毒交易数量，最小化该数量即最大化 accuracy。该数值由事务数据库和算法决策直接确定。", "objectivity_reason_cn": "accuracy 是完全客观的数据库操作结果，不依赖任何人类感受、语义判断或主观评分；仅涉及交易是否被标记为消毒。"}, {"name_cn": "推荐系统精确率 recommendation precision（辅助验证指标）", "measurement_cn": "将测试集交易随机分为购物篮和剩余部分，用从原始或消毒后数据集挖掘的关联规则产生推荐，若推荐商品出现在交易剩余部分则记为成功，统计成功百分比。", "objectivity_reason_cn": "推荐是否成功取决于真实交易中是否客观出现该商品，不是用户或专家打分，因此属于客观可测指标；但该指标仅用于验证消毒后与原始数据无显著差异，不是核心提升目标。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: Retail (Belgian retail store dataset, FIMI repository) | BMS-POS (electronics retailer dataset, FIMI repository)
- Benchmark evaluation: 在 Retail 和 BMS-POS 公开标准数据集上，将数据集随机划分为 2/5/10 个分区，随机选择敏感项集，比较 Ensemble 与最优解（CPLEX 直接求解 FIH_D）以及 Verykios et al. (2004) 的被消毒交易数。Table 3 显示 Ensemble 与最优解的平均 gap 仅 0.04%–0.08%，而 Verykios 方法的平均 gap 达 28.75%–52.06%，且 Verykios 无法解决合成大数据集。这些结果直接支撑 Ensemble 在 accuracy 上的核心提升主张。
- Decision: 客观指标方面：核心指标 accuracy 是直接由事务数据库和算法输出确定的客观数值，不依赖主观判断；FIH_D 的目标函数和全部评价围绕该指标展开，且文章核心主张为在 accuracy 上接近最优并优于现有方法。推荐 precision 作为辅助验证也是客观指标，且结论为非劣性而非提升目标。核心目标唯一性方面：没有提出并列的理论、制度、组织或主观贡献；理论命题仅支撑算法设计，推荐实验仅验证副作用。Benchmark 方面：虽然作者未在文中使用“benchmark”一词称呼数据集，但明确将频繁项集挖掘领域公开标准数据集 Retail 和 BMS-POS 作为评价场地，属于命名式 benchmark 表述；评价位于实验部分，且 Table 3 的 benchmark 结果直接用于证明 Ensemble 相对于最优解和 Verykios 方法的 accuracy 提升。因此所有门槛满足，strict_include=true。
- Confidence: 0.85

## Induction over Strategic Agents

- Year/journal: 2010 / Information Systems Research
- DOI: 10.1287/isre.1090.0272
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "误分类数（positive/negative misclassifications）", "measurement_cn": "在训练集、测试集及合并集上统计分类错误的样本数量", "objectivity_reason_cn": "分类正确与否由真实标签和预测标签比对得出，是可审计事实，不依赖人类主观判断。"}, {"name_cn": "目标函数值（objective value）", "measurement_cn": "由SVM/MIP目标函数计算，包括w'w、误分类惩罚项C*ξ以及可选的正类代理移动惩罚λ*q_i，全部由公式和参数决定", "objectivity_reason_cn": "目标函数值是模型求解的直接输出，完全由数学公式和训练数据决定，无主观成分。"}, {"name_cn": "几何间隔/权重范数 (||w||)", "measurement_cn": "对学习到的线性判别函数的权重向量取范数", "objectivity_reason_cn": "范数是数学计算，反映分类间隔，客观可复现。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: UCI repository credit-screening data (Credit Approval Data Set)
- Benchmark evaluation: 在UCI credit-screening公开数据集上，对策略性ISA解决方案与非策略性SVM解决方案进行对比评估，报告训练集和测试集上的正/负误分类数、目标函数值、权重范数等，并以表格形式展示策略性方案的显著改进。
- Decision: 文章的核心目标是设计一个能预期策略性代理行为的分类规则，以最小化误分类风险。所有核心评价指标（误分类数、目标函数值、权重范数）均是从数据中直接计算得到的客观指标，不涉及任何主观构念或人类语义评价。评价结构在UCI公开基准数据集上比较了策略性解决方案与非策略性SVM，明确显示了客观指标的提升，并作为核心贡献证据。因此同时满足完全客观指标和明确benchmark表述的要求。
- Confidence: 0.85

## Novel linear programming approach for building a piecewise nonlinear binary classifier with a priori accuracy

- Year/journal: 2012 / Decision Support Systems
- DOI: 10.1016/j.dss.2011.11.006
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "分类错误率/准确率（训练集与测试集）", "measurement_cn": "在UCI repository、Japanese Bank数据集及合成数据集上运行算法，将预测类别与数据集中给定的事实类标比较，计算误差百分比；测试误差通过约20%随机划分或5折交叉验证得到。", "objectivity_reason_cn": "类标是可审计的外部事实标签，错误率由确定的预测-真实标签比较计算，不依赖人的感受、语义评价或价值判断。"}, {"name_cn": "CPU运行时间（秒）", "measurement_cn": "MATLAB实现中记录的算法运行耗时，如Table 1中的Time sec.。", "objectivity_reason_cn": "CPU时间是可直接测量的物理资源消耗，客观可审计。"}, {"name_cn": "生成的超平面/判别面片数量", "measurement_cn": "算法迭代生成的分段判别函数所包含的平面数或非线性面片数，如Table 1和Table 2中的Planes/Hyperplanes。", "objectivity_reason_cn": "这是算法输出结构的可计数属性，与主观判断无关。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: UCI Machine Learning Repository（Abalone, Bank, Cancer, Contraceptive, Credit, Diabetes, Heart, Housing, Ionosphere, Letter, Sonar, Spiral, Wine） | Japanese Bank dataset | 合成数据集（含已知分离函数(15)与双螺旋数据集）
- Benchmark evaluation: 在UCI repository多个标准数据集、Japanese Bank数据集以及带已知分离函数的合成数据上运行所提算法，报告训练/测试错误率、超平面数和CPU时间；通过5折交叉验证与SVM(16)、单平面版本等比较，用于支撑算法精度和泛化能力的核心主张。
- Decision: 全文以构建并评估一种可先验指定精度的分段非线性二分分类器为核心，所有核心成功指标均为分类错误率/准确率、CPU时间、超平面数量等客观可审计指标；未使用主观量表或人类语义判断。数值实验明确命名UCI repository数据集、Japanese Bank数据集和合成数据集作为评价场地，并在这些标准数据上以SVM(16)等为显式参照点比较测试错误，证明算法性能提升与竞争力，因此benchmark门槛也满足。两模块均通过，严格纳入。
- Confidence: 0.85

## On quantified weighted MAX-SAT

- Year/journal: 2005 / Decision Support Systems
- DOI: 10.1016/j.dss.2003.12.004
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "求解时间（CPU 秒）", "measurement_cn": "在固定硬件配置（Dell PC, P3 800MHz, 256M RAM）上运行 Q-W-MAX-SAT 求解器，记录完成求解或判定无解所耗的 CPU 秒数；加速比通过盲搜索与启发式搜索的时间之比计算。", "objectivity_reason_cn": "CPU 求解时间是物理上可审计、可复现的技术指标，不依赖人的感知、偏好、情绪或语义判断。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: QBF benchmark problems available at http://www.informatik.uni-freiburg.de/~rintanen/qbf.html | four benchmark domains: chain of implications, bomb in toilet, blocks world, 3-CNF
- Benchmark evaluation: 在取自公开 QBF benchmark 的 40 个 Q-W-MAX-SAT 问题上，评价盲搜索、MMWO-1（H1）、MMWO-2（H2）以及 Rule 3；报告 CPU 求解时间和加速比，其中 H1 相对盲搜索加速最高 133.36 倍，H2 相对盲搜索加速最高 7.93 倍，Rule 3 对无解实例判定加速高达 381047 倍，从而直接支撑启发式/简化规则提高求解效率的核心主张。
- Decision: 客观指标方面，论文以 CPU 求解时间为唯一核心成功指标，属于完全客观、可直接观测的技术指标；没有主观量表或人类语义评价作为核心结果。核心目标方面，论文的研究问题和贡献声明集中于高效求解 Q-W-MAX-SAT，启发式和简化规则的效果完全以求解时间/加速比评价，未提出并列的主观或理论机制贡献。Benchmark 方面，论文在明确命名的公开 QBF benchmark 来源及其四个 benchmark domains 上构造 40 个问题，并在评价语境中比较盲搜索、H1、H2 和 Rule3 的求解时间；benchmark 结果直接支撑核心效率提升主张，且有明确对照。因此两个模块均通过，strict_include=true。
- Confidence: 0.85

## Partial order resolution of event logs for process conformance checking

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113347
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "一致性检查准确度", "measurement_cn": "在不确定轨迹上，比较预测的加权适应度与基于真实事件顺序的金标准适应度；trace级用RMSE，log级用绝对误差。", "objectivity_reason_cn": "结果完全由事件日志、过程模型和原始终点顺序决定，不依赖人的感受、语义评价或价值判断。"}, {"name_cn": "运行时效率与近似误差", "measurement_cn": "记录一致性检查的运行时（分钟/秒）以及使用近似方法后相对于无近似结果新增的RMSE误差。", "objectivity_reason_cn": "运行时间可直接计时观测，近似误差由数值计算结果确定，均为可审计的客观指标。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: BPI Challenge 2012 (BPI-12) | BPI Challenge 2014 (BPI-14) | Road Traffic Fine Management Process (Traffic fines)
- Benchmark evaluation: 在BPI-12、BPI-14和Traffic fines三个公开真实事件日志以及500个合成模型上评价所提出的trace equivalence、N-gram和weak order行为模型；报告trace-level RMSE和log-level误差，并与BL1（均匀概率基线）和BL2（丢弃不确定轨迹的基线）比较；结果表明所提模型一致优于基线，例如Traffic fines日志RMSE为0.011 vs BL1的0.182，综合平均误差降低59.0%。
- Decision: 该文核心问题是部分有序事件日志的一致性检查，核心贡献是概率性偏序解析、多种行为模型和带统计保证的近似方法。评价的核心指标是一致性检查准确度（trace-level RMSE和log-level误差）以及运行时效率，均为完全客观、可审计的指标，且没有与主观体验或理论机制并列的核心目标。在benchmark方面，文章虽未直接使用benchmark一词，但明确命名BPI-12、BPI-14和Traffic fines三个公开领域标准事件日志作为核心评价场地，并在该场地与BL1、BL2基线及金标准真实适应度比较，结果用于支撑“显著提升准确度（平均误差降低59.0%）”的核心主张。因此两个模块均通过，strict_include为true。
- Confidence: 0.85

## Predicting Stages in Omnichannel Path to Purchase: A Deep Learning Model

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2021.1071
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "路径阶段预测性能：AUC、log-loss、accuracy、precision、recall、nDCG", "measurement_cn": "在时间嵌套交叉验证下，对每个用户-域名对预测未来两周是否发生访问/考虑/购买三类二元标签；标签由URL日志和固定编码规则生成（访问购物网站、停留超过5分钟且浏览至少2个页面、出现支付/购买相关URL），模型输出预测分数后计算六项指标。", "objectivity_reason_cn": "预测目标是由系统日志按固定编码规则产生的0/1标签，不依赖人的感受、语义偏好或质量判断；指标计算和比较可完全审计。"}, {"name_cn": "lift（提升度）", "measurement_cn": "按预测分数排序后计算各分位点的正例提升倍数；omnichannel模型相对单通道模型平均提升7.38%。", "objectivity_reason_cn": "基于预测排名和真实标签计算的客观比率，不涉及主观评价。"}, {"name_cn": "利润曲线/增量货币价值", "measurement_cn": "基于混淆矩阵、成本收益矩阵及示例参数，计算每个实例的期望货币价值，以及omnichannel相对单通道模型的增量价值（示例中每实例$0.060，年化约5.04亿美元）。", "objectivity_reason_cn": "由客观预测性能与可核验的成本/收益参数计算得到，虽含假设但属于可审计的经济价值量化。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在自有电信运营商omnichannel数据集上，以模型1-3（仅用户/域名ID、在线特征、离线特征）作为基准模型，对模型4（全渠道特征）进行系统化基准比较；并额外用Logistic regression、Bayesian ridge regression、Random forest、XGBoost、DeepFM作为基准算法与xDeepFM比较。报告AUC等六项指标、统计检验、lift曲线和利润曲线。
- Decision: 客观指标方面，预测目标是对访问/考虑/购买阶段的0/1标签，由URL日志和固定编码规则确定，不涉及主观判断；核心目标明确为提升预测性能和经济价值，且为唯一核心贡献。Benchmark方面，作者在引言中明确使用'benchmark algorithms'，并在结果表3后称模型4显著优于'all the benchmark models'，属于评价语境中的基准比较；比较对象明确（模型1-3及多种预测方法），结果直接支撑omnichannel数据提升预测力的核心主张。因此两个模块均通过，strict_include为true。
- Confidence: 0.85

## Real-Time Tactical and Strategic Sales Management for Intelligent Agents Guided by Economic Regimes

- Year/journal: 2012 / Information Systems Research
- DOI: 10.1287/isre.1110.0415
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "利润 (mean total profit)", "measurement_cn": "TAC SCM 仿真中 agent 的期末银行余额/平均总利润，跨 23 次可重复伪随机序列计算", "objectivity_reason_cn": "由仿真市场状态和决策规则直接产生，不依赖人类感受、语义判断或价值评价"}, {"name_cn": "价格预测精度 (RMSE)", "measurement_cn": "预测的归一化价格与实际每日归一化价格之间的均方根误差，按公式(24)跨天和跨仿真平均", "objectivity_reason_cn": "直接比较可观测价格序列，数值可审计，不含主观评价"}, {"name_cn": "体制分布预测精度 (KL divergence)", "measurement_cn": "预测经济体制概率分布与事后实际体制概率分布之间的 KL 散度，公式(23)", "objectivity_reason_cn": "体制由历史价格数据的统计模式定义，KL 散度为确定的概率距离计算"}, {"name_cn": "价格趋势方向预测成功率", "measurement_cn": "预测价格趋势符号与实际价格趋势符号一致的比例，图 9 所示", "objectivity_reason_cn": "基于可观测价格序列和固定符号判断规则，客观可复算"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: Trading Agent Competition for Supply Chain Management (TAC SCM)
- Benchmark evaluation: 在 TAC SCM 标准仿真环境上，使用 2005 年 18 场训练、10 场测试数据评估体制预测方法；比较了三种 regime 预测方法与三种基线（指数平滑、Botticelli 常数预测器、TacTex 加权平均预测器）的价格预测 RMSE、体制分布 KL 散度、价格趋势方向成功率；另在真实时 TAC SCM 仿真中用相同竞争者集和 23 组可重复随机序列比较不同 agent 配置的平均利润。
- Decision: 客观指标方面：核心成功指标是价格/体制预测精度（KL、RMSE、趋势正确率、订单概率）和仿真利润，全部为可审计的客观数值，不依赖人类感知或语义评价。唯一核心目标方面：研究问题、设计、评价和贡献声明均围绕改进预测精度并利用预测提升利润，未发现并列的主观、理论机制或政策贡献。Benchmark 方面：TAC SCM 是明确命名的公开标准测试环境，评价在其上完成，并与多种基线/现有 agent 预测方法进行显式比较，结果直接支撑核心改进主张。因此 strict_include=true。
- Confidence: 0.85

## Recommendation with diversity: An adaptive trust-aware model

- Year/journal: 2019 / Decision Support Systems
- DOI: 10.1016/j.dss.2019.113073
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "推荐精度 Precision (P)", "measurement_cn": "对每个用户在测试集中的已评分/感兴趣物品，计算其出现在推荐列表前N项中的比例，然后对所有目标用户取平均；数据来源是用户-物品二分网络的留出测试集。", "objectivity_reason_cn": "构念为用户历史交互事实（评分≥3即为感兴趣），不依赖用户主观满意度或语义评价；计算方式是确定性的可审计计数。"}, {"name_cn": "个体多样性 Di", "measurement_cn": "对每个用户推荐列表内物品两两之间的余弦不相似度取平均，余弦相似度由用户共现交互计算。", "objectivity_reason_cn": "基于可观测的交互矩阵的确定算法，不涉及人对质量、价值或感受的判断。"}, {"name_cn": "聚合多样性 Da", "measurement_cn": "统计所有用户推荐列表中去重后的不同物品总数。", "objectivity_reason_cn": "纯计数指标，可直接从推荐列表集合确定。"}, {"name_cn": "新颖性 Dn", "measurement_cn": "根据推荐列表中物品的度（被评次数）计算 log2(|U|/k_o) 的平均值。", "objectivity_reason_cn": "基于物品度数的确定性计算，不需要人类语义评价。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: Ciao | Epinions | Yelp
- Benchmark evaluation: 在 Ciao、Epinions、Yelp 三个公开数据集上评价所提 TrAdBi 模型及其参数调整版本 TrAdBi1/TrAdBi2，与 BD、Eh_HHPH、SP、PLUS、COUSIN、COSRA+T 等基线比较，报告 Precision、Di、Da、Dn；同时单独报告冷启动用户和长尾物品精度（Fig.7）及经验丰富用户多样性（Fig.8）。
- Decision: 客观指标方面：全文核心成功指标是 Precision、个体多样性、聚合多样性和新颖性，均可从用户-物品交互数据中确定性计算，不依赖用户满意度、感知质量或语义评价；研究问题、算法设计、实验结果和结论均围绕这些客观指标提升。唯一核心目标方面：目标是构建自适应信任感知推荐模型以同时提升精度和多样性，所有贡献声明均围绕客观指标改进，不存在并列的理论机制、组织变革或主观体验核心目标。Benchmark 方面：文章在 Ciao、Epinions、Yelp 三个公开领域数据集上评价模型，并以 BD、Eh_HHPH、SP、PLUS、COUSIN、COSRA+T 等多个基线与既有方法作显式比较，结果表直接支撑核心精度与多样性提升主张，满足命名式 public benchmark 和显式比较条件，因此三个模块均通过，strict_include=true。
- Confidence: 0.85

## Risk Management and Optimal Pricing in Online Storage Grids

- Year/journal: 2011 / Information Systems Research
- DOI: 10.1287/isre.1100.0288
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "卖方期望收入（expected revenue）", "measurement_cn": "通过最优定价模型中买家在不同定价策略下选择（自建/现货/远期）的成本函数计算卖方总收入，并用 Alexa/Quantcast 公开流量数据估计 37 个 Amazon S3 客户的需求分布后，结合多项式算法和模拟计算得出。", "objectivity_reason_cn": "收入是货币金额，由价格、需求量、选择行为按公式确定，不依赖人类感受、语义评价或主观判断。"}, {"name_cn": "卖方下行风险（downside risk）", "measurement_cn": "定义为基于需求分布的风险度量 d_{X/c}，并构造风险-收益有效前沿；文中报告风险百分比变化。", "objectivity_reason_cn": "下行风险由需求分布和价格通过数学公式定义，是可审计的统计量，不依赖主观体验。"}, {"name_cn": "买方成本与风险", "measurement_cn": "在 buyer perspective 中，比较自建、固定定价、纯现货、现货加远期四种情形下买方的期望成本和下行风险百分比。", "objectivity_reason_cn": "成本和风险均为可计算的财务/统计指标，不依赖人的感受。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在 37 个 Amazon S3 客户的实际流量数据模拟中，以 Amazon 当前固定定价政策作为基准（benchmark case），评价提出的纯现货市场和现货+远期合约定价策略：纯现货平均提升收入 41% 但风险增加 108%；加入远期合约后平均降低风险 57% 并提升收入 51%。
- Decision: 核心成功指标是卖方的期望收入和下行风险，两者均由公式、价格和需求分布决定，完全客观且依赖外部可审计的财务/统计事实；全文从摘要到结论均明确以收入提升和风险降低为最终目标，没有并列主观构念或理论解释作为核心贡献。benchmark 门槛方面，作者在实证评价部分明确使用“benchmark case of Amazon S3’s current fixed-pricing policy”作为基准，通过百分比提升和风险变化报告了所提定价策略的改进，该基准比较位于评价语境并直接支撑核心收入/风险主张，且具有明确比较对象。因此两个模块均通过。
- Confidence: 0.85

## Short-term prediction models for server management in Internet-based contexts

- Year/journal: 2009 / Decision Support Systems
- DOI: 10.1016/j.dss.2009.07.014
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "预测准确性（NMAE）", "measurement_cn": "基于系统监控数据与预测值计算归一化平均绝对误差，公式为 (Σ(f̂_j - f_j)^2)/(N*mean(f)) * 100%。", "objectivity_reason_cn": "NMAE 由服务器资源监控值（如 CPU 利用率、磁盘吞吐量）与模型预测值直接计算得到，不依赖人类感知、偏好或语义评价，是可审计的数值指标。"}, {"name_cn": "运行时计算开销", "measurement_cn": "测量每个预测值所需的 CPU 时间以及扩展到 Web 集群后的总时间，如 Table 2 所示。", "objectivity_reason_cn": "CPU 时间是物理可测量、确定性可观测的客观指标，用于验证模型的运行时可行性。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: TPC-W
- Benchmark evaluation: 在基于 TPC-W 工作负载模型构造的多层 Web 测试床上，对 CPU 利用率和磁盘吞吐量等内部资源数据应用所提出的 DFT 滤波与 AP 自适应预测模型；在 Stable、Realistic 1、Realistic 2 三种工作负载场景下，以 NMAE 为指标比较 AP 与 EWMA、LR、AR、Static-ARIMA、Dynamic-ARIMA 在不同预测窗口 k 下的预测误差。
- Decision: 核心目标是提升短期预测准确性，使用 NMAE 和 CPU 时间等完全客观、可测量、无人类语义评价的指标；全文无主观成功标准，也无并列核心贡献。benchmark 方面，明确命名 TPC-W 作为工业 benchmark，并以其工作负载模型构造评价场景；在该场景下将 AP 模型与 EWMA、LR、AR、Static/Dynamic ARIMA 等明确参照点进行比较，结果用于支撑核心的预测精度提升主张。因此严格包含条件成立。
- Confidence: 0.85

## Toward global optimization of neural networks: A comparison of the genetic algorithm and backpropagation

- Year/journal: 1998 / Decision Support Systems
- DOI: 10.1016/s0167-9236(97)00040-7
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "RMS误差（in-sample / interpolation / extrapolation）", "measurement_cn": "将GA与BP训练的神经网络用于7个测试函数；比较网络输出与已知真实函数值之间的均方根误差，分别在训练集、插值集和外推集上计算。", "objectivity_reason_cn": "真实函数值由数学公式预先确定，RMS误差是可直接计算的数值比较结果，不依赖人的感知、语义评价或偏好。"}, {"name_cn": "错分个数（classification misclassifications）", "measurement_cn": "在Hand(1981)/Wang(1995)分类数据上，比较GA训练神经网络的预测类别与固定类别标签，统计错误分类数量。", "objectivity_reason_cn": "类别标签（非医疗/医疗用户等）对应外部事实，错分个数是可审计的计数结果，不涉及主观质量判断。"}, {"name_cn": "网络连接数/隐藏节点数（精简架构）", "measurement_cn": "在使用修正目标函数 min{βM + Σ|Yi−Y^i|} 后，统计保留的非零连接权数量或等价隐藏节点数。", "objectivity_reason_cn": "连接数和隐藏节点数是对网络结构的直接计数，客观可验证，属于资源消耗类客观指标。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: Glass–Mackey chaotic time series | Hand(1981) classification dataset
- Benchmark evaluation: 在7个测试函数（含Glass–Mackey标准时间序列）上开展GA与BP的Monte Carlo比较，报告in-sample、interpolation、extrapolation的RMS误差，并用Wilcoxon配对符号秩检验比较；GA在所有问题上均显著优于BP。另在Hand(1981)分类数据上训练的GA网络将错分数从Wang(1995)的4个降至1个，并可去除冗余连接。
- Decision: 客观指标门槛通过：核心成功指标是RMS误差、错分个数和网络连接数，均为可计算、可审计的客观结果，无主观量表或人类语义判断；唯一核心贡献是证明遗传算法作为神经网络全局优化方法在客观精度上优于BP，并可通过客观连接数指标实现精简架构。Benchmark门槛通过：虽然全文未直接使用'benchmark'一词，但明确命名了Glass–Mackey标准时间序列测试任务和Hand(1981)分类数据，并以系统化Monte Carlo比较作为核心证据，且与BP、Wang(1995)、Hand(1981)等明确参照点比较，证明GA的客观指标提升。因此strict_include=true。
- Confidence: 0.85

## User community discovery from multi-relational networks

- Year/journal: 2013 / Decision Support Systems
- DOI: 10.1016/j.dss.2012.09.012
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "综合均值 μ", "measurement_cn": "定义为软模块度 Qs 与用户内容相似度 Su 的平均值；Qs 由社区分布和网络邻接矩阵计算，Su 由用户 tf-idf 向量两两余弦相似度按社区隶属加权计算。", "objectivity_reason_cn": "两者均通过确定性的公式从网络结构和文本词频计算，不依赖用户、专家或研究者的主观评分和语义质量判断。"}, {"name_cn": "社区用户散度 D_U、社区主题散度 D_T 及复合散度 D", "measurement_cn": "基于 JS 散度计算社区之间用户分布和主题分布的差异，取平均值或调和平均。", "objectivity_reason_cn": "由检测出的概率分布按数学公式可复现计算，不涉及主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在 Delicious 和 Twitter 两个真实数据集上，将 NMF-AT 与 NMF、AT、MetaFac 三个基准方法比较；主要报告综合均值 μ、社区用户散度、社区主题散度和复合散度。结果显示 NMF-AT 在综合均值上优于对比方法，Delicious 上成对 t-test p<0.001，Twitter 上在整体区间内更优，并在复合散度 D 上取得最高值。
- Decision: 客观指标：核心成功指标是软模块度、内容相似性和社区散度，均由数据和确定性公式计算，不依赖主观人工评价。唯一核心目标：研究问题、算法设计和贡献声明均围绕通过融合好友网络与用户内容来提升社区发现的客观质量，未发现并列的理论、政策或主观体验核心贡献。Benchmark：实验部分明确将 NMF、AT、MetaFac 作为 benchmark 方法进行系统比较，结果直接支持 NMF-AT 的客观指标改善，且具有明确参照对象。因此 strict_include=true。
- Confidence: 0.85

## sDTM: A Supervised Bayesian Deep Topic Model for Text Analytics

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1124
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "模型拟合困惑度（Perplexity）", "measurement_cn": "在测试集上计算文档负对数似然，以 exp(-1/D_test * sum(1/N_d * log p(d|t))) 形式度量；值越低表示主题模型泛化能力越强。", "objectivity_reason_cn": "基于模型概率的可计算数值，不依赖任何人工评价或主观判断。"}, {"name_cn": "预测性能（Yelp 使用 AUROC；Stack Exchange 使用准确率）", "measurement_cn": "训练后在测试集上评估模型预测标签的性能；Yelp 为二分类情绪预测，报告 AUROC；Stack Exchange 为多分类类别预测，报告准确率。", "objectivity_reason_cn": "由既定算法从测试集真实标签与模型预测计算得到，属于可审计的外部可验证指标。"}, {"name_cn": "经验回归的系数方向、显著性与统计效力（辅助展示）", "measurement_cn": "基于回归模型估计的系数符号、p 值以及1,000次子样本重复估计的显著性次数。", "objectivity_reason_cn": "因变量为平台用户对评论或答案的有用性投票数，是可观察的外部行为记录；回归估计和显著性检验可由确定统计方法复现。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在两个 IS 相关数据集（Yelp 在线评论、Stack Exchange 在线知识社区）上，作者将sDTM与多组基准模型进行比较：模型拟合评估中比较困惑度（表4），预测任务中比较AUROC/准确率（表11）。sDTM在所有设置下均显著优于无监督、有监督及深度学习基线。
- Decision: 客观指标方面：文章核心评估为完全客观的模型拟合（perplexity）和预测性能（AUROC/准确率），这些指标可通过确定算法计算且不依赖人类感受或语义评价；全文未将主观量表或理论机制贡献列为同等核心目标，因此满足唯一核心目标要求。Benchmark方面：作者在评估部分明确使用“benchmark baselines/models”陈述系统化基准比较，并在两个数据集上与多个基线（LDA、sLDA、MedLDA、NTM、BERT等）比较，结果直接支撑sDTM的客观指标提升主张，且存在明确参照点。两项门槛均通过，故 strict_include=true。
- Confidence: 0.85

## A scalable decision tree system and its application in pattern recognition and intrusion detection

- Year/journal: 2005 / Decision Support Systems
- DOI: 10.1016/j.dss.2004.06.016
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "分类错误率（1-accuracy）", "measurement_cn": "在测试集上被错误分类的记录数除以测试记录总数；三个数据集分别对应森林覆盖类型、波形类别和入侵/正常连接类别的真实标签。", "objectivity_reason_cn": "类别标签是外部事实（森林覆盖类型、波形类型、网络入侵类型），可通过系统日志或数据生成程序核验；错误率是确定性的计数比例，不依赖人的感受或语义评价。"}, {"name_cn": "决策树大小（叶子数）", "measurement_cn": "最终决策树中的叶子节点数量，由算法生成的树结构直接统计。", "objectivity_reason_cn": "叶子节点数是模型结构的可计数属性，不依赖用户或专家主观评价。"}, {"name_cn": "总CPU时间", "measurement_cn": "算法在给定数据集上运行的总CPU秒数，记录在实验环境中。", "objectivity_reason_cn": "CPU时间是物理可测量的计算资源消耗，不依赖人的感知或判断。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: UCI forest cover data set（U.C. Irvine数据仓库） | CART waveform data set（基于CART书中的模型生成、常用于决策树实验的标准仿真数据） | Intrusion detection data set（来自Lee & Stolfo等的网络连接记录数据，311,029条记录）
- Benchmark evaluation: 在森林覆盖、waveform和入侵检测三个公开/标准数据集上，随机抽取10%、20%、…、100%样本，并在每个样本内以60%训练、40%测试划分，比较SURPASS、RainForest和LDA的错误率、叶子数和CPU时间；同时报告SURPASS剪枝前后的比较，并用ANOVA/Tukey检验错误率差异的统计显著性。
- Decision: 客观指标方面，三个核心成功度量均为错误率、树大小和CPU时间，全部是外部可核验的确定性事实，不依赖人的主观判断；固定事实标签上的分类错误率属于objective_fixed_factual_labels。唯一核心目标是提出并验证可扩展的SURPASS决策树算法，提升大规模数据分类的可扩展性和分类质量，全文没有并列的理论、制度或主观体验目标。Benchmark方面，第5节明确将UCI forest cover、CART waveform和intrusion detection三个公开/标准数据集作为评价场地，并与RainForest、LDA等明确参照点比较，结果直接支撑分类质量和可扩展性主张；虽然全文未出现“benchmark”字面词，但满足命名式Benchmark表述。因此两个模块均通过，strict_include=true。
- Confidence: 0.84

## A text summary-based method to detect new events from streams of online news articles

- Year/journal: 2022 / Information & Management
- DOI: 10.1016/j.im.2022.103684
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "遗漏率", "measurement_cn": "将测试新闻按时间顺序输入NED技术，依据人工标注的事件簇，计算未能将真正属于新事件的文章识别为新事件的概率；重复30次随机70%采样后取平均。", "objectivity_reason_cn": "遗漏率是预测结果与既定事件标注之间的确定性比较，反映的是新闻流中新事件是否被检测到的客观事实，不依赖用户感受、偏好或质量评价。"}, {"name_cn": "误报率", "measurement_cn": "将测试新闻按时间顺序输入NED技术，依据人工标注的事件簇，计算将已知事件文章误判为新事件的概率；重复30次随机70%采样后取平均。", "objectivity_reason_cn": "误报率同样是预测与既定事件标注的确定性比较，属于可审计的检测错误，不涉及人类满意度和语义价值判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在自建训练新闻语料（excite.com，506篇）和测试新闻语料（215篇）上，将SED与INCR、BERT-NED、bi-LSTM-NED三个基准技术进行比较，以miss/false alarm DET曲线评价检测有效性，结果用于支持SED改进核心客观指标的主张。
- Decision: 本文的核心目标是提出并验证基于文本摘要的新事件检测方法，评价指标为遗漏率和误报率，均属于对既定事件标注的确定性检测性能，构念不依赖主观体验；全文在实验部分明确使用“benchmark”表述并与INCR、BERT-NED、bi-LSTM-NED等明确参照点比较，benchmark结果直接支撑核心改进主张，因此客观指标和benchmark两个模块均通过，strict_include为true。
- Confidence: 0.84

## Mining Massive Fine-Grained Behavior Data to Improve Predictive Analytics1

- Year/journal: 2016 / MIS Quarterly
- DOI: 10.25300/misq/2016/40.4.04
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "AUC（ROC曲线下面积）", "measurement_cn": "基于银行客户是否实际购买金融产品的二元事实标签，由模型打分后在测试集上计算 AUC。", "objectivity_reason_cn": "购买与否是银行系统中的客观事实，不依赖人的感受或语义评价；AUC 是确定性计算的分类型预测性能指标。"}, {"name_cn": "Lift（针对1%、5%、10%目标群体的提升度）", "measurement_cn": "选择模型打分最高的前若干比例客户，计算其实际购买率与随机选择购买率的比值，标签来自银行交易/产品记录。", "objectivity_reason_cn": "目标群体的实际购买行为是可审计事实，提升度由客观标签与模型排序计算得出。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在银行真实客户数据（非公开专有数据）上，将BeSim模型作为基准，与结构化数据模型（SD）及组合模型（BeSim+SD）在AUC和lift@1/5/10%上进行比较，结果显示组合模型在多数指标上显著优于基准和SD模型，BeSim在lift@1%上显著优于SD模型。
- Decision: 核心成功指标是客户是否实际购买金融产品的客观事实标签上的AUC和lift，全部核心目标围绕预测性能提升，没有主观构念或并列核心贡献。虽然未使用公开基准数据集，但在结果评价部分明确将BeSim模型作为benchmark，并与SD、SVM、组合模型等明确参照点比较，基准评价直接支撑核心预测性能提升主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.84

## Software Cost Estimation Using Economic Production Models

- Year/journal: 1998 / Journal of Management Information Systems
- DOI: 10.1080/07421222.1998.11518200
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "软件成本估算误差（MRE）", "measurement_cn": "MRE = |估计成本−实际成本| / 实际成本；实际成本与估计成本均为 Kemerer 数据集中软件项目的人月数，使用留一法计算预测误差。", "objectivity_reason_cn": "项目实际成本、进度、规模来自公开历史项目数据，是可审计的客观事实；MRE 由确定公式计算，不依赖人对质量、价值或满意度的主观评价。"}, {"name_cn": "拟合优度（ASRE）", "measurement_cn": "ASRE = (1/n) * sqrt(Σ(E0i−E1i)^2)，其中 E0i 为项目实际成本，E1i 为模型拟合成本，数据来源为 Kemerer 数据集的 14 个软件项目。", "objectivity_reason_cn": "以历史项目人月数作为实际值，模型拟合值与实际值的偏差由公式直接计算，属于确定性、可复核的客观指标。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: Kemerer software project data set (Kemerer, 1987)
- Benchmark evaluation: 在 Kemerer 数据集的 14 个项目上，将 MSCM 与 Intermediate COCOMO、SLIM、GCDT、GCD 比较拟合优度（ASRE：MSCM 15.13，GCDT 15.91，GCD 16.92，COCOMO 339.49，SLIM 21.67），并用留一法比较预测误差（平均 MRE：MSCM 50%，SLIM 53%，GCDT 62%，GCD 71%，COCOMO 593%），同时报告 25%-MRE、30%-MRE、50%-MRE 比例。
- Decision: 文章核心目标是提出并验证一种软件成本估算模型，核心指标为成本估算误差 MRE 和拟合优度 ASRE，均为可由历史项目数据直接计算的客观指标；评价结构、摘要和结论都以 MSCM 的估算精度提升为核心，未将主观体验或独立的理论/政策贡献作为并列核心目标。benchmark 门槛满足：作者明确选择公开的 Kemerer 软件项目数据集作为评价场地，并与 COCOMO、SLIM、GCDT、GCD 等多个既有模型进行比较，比较结果支撑了核心提升主张。因此 strict_include=true。
- Confidence: 0.83

## A Computational Analysis of Bundle Trading Markets Design for Distributed Resource Allocation

- Year/journal: 2012 / Information Systems Research
- DOI: 10.1287/isre.1110.0366
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "市场收敛速度（迭代轮数）", "measurement_cn": "在模拟市场运行中，从初始状态到达最优分配或价格收敛所需的交易轮数；由算法迭代次数直接记录。", "objectivity_reason_cn": "迭代轮数是算法模拟产生的可审计计数，不依赖人感知或语义判断。"}, {"name_cn": "市场效率/配置效率", "measurement_cn": "以各代理当前资源水平下总运营成本与中央问题最优成本的比值衡量；由线性规划计算结果确定。", "objectivity_reason_cn": "效率值来自确定性的线性规划成本计算，是可复现的数学事实。"}, {"name_cn": "社会福利与财富比率", "measurement_cn": "基于现金禀赋、资源分配和代理成本计算的总财富及代理净财富与系统总节约的比值；由模拟结算规则确定。", "objectivity_reason_cn": "财富和成本均为计算模型中的可观测数值，不涉及人类主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 作者在76,800个模拟观察上运行受控实验，以P=0.2、NA库存策略、MA学习模型为基准场景，回归模型比较不同异步通信水平、库存策略和学习模型的性能差异；结果是支撑核心主张（异步通信和不对称信息降低市场绩效，学习提高绩效，主动库存干预不一定有利等）的关键证据。
- Decision: 客观指标方面，核心成功指标是市场迭代轮数、配置效率、社会福利/财富比率等完全由计算模型确定的客观值，不涉及人类主观评价。核心目标方面，研究问题、设计目标、实验评价和贡献声明均围绕扩展市场机制并改进计算性能，未发现并列的主观或理论核心目标。benchmark方面，作者在结果分析中明确设置'基准场景'并以此进行系统比较，该基准比较是核心判断的依据；同时§3将原始BTM框架作为扩展模型的基准。四个benchmark门槛均满足。因此严格纳入。
- Confidence: 0.82

## A location model for a web service intermediary

- Year/journal: 2006 / Decision Support Systems
- DOI: 10.1016/j.dss.2004.11.016
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "WSI总体期望运营成本", "measurement_cn": "以整数规划目标函数(1)计算：客户端-WSI服务器通信成本、WSI服务器-WSP通信成本、WSI服务器间通信成本、服务器固定成本与WSP固定费用；在模拟US backbone网络上生成确定性数据后由DAL启发式和CPLEX 8求解并比较目标函数值。", "objectivity_reason_cn": "成本由确定性参数和数学目标函数计算，来自网络延迟折算、固定费用等可审计事实，不依赖人类感受或语义判断。"}, {"name_cn": "求解计算时间", "measurement_cn": "在933 MHz、Windows 2000平台上记录DAL和CPLEX 8在各类问题实例上的CPU秒数，比较平均时间、相对标准差及anytime表现。", "objectivity_reason_cn": "计算时间是系统可审计的执行日志指标，可直接客观测量。"}, {"name_cn": "启发式解与最优解的间隙（solution quality gap）", "measurement_cn": "将DAL求解的目标函数值与CPLEX 8得到的最优目标函数值比较，计算平均和最大百分比差距。", "objectivity_reason_cn": "最优值由精确求解器给出，差距是可复算的数学量，无需主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: DAL启发式与CPLEX 8精确求解器在8个问题类别（a-h，候选位置数5到40）的模拟实例上进行系统比较。结果显示DAL平均目标函数值间隙约0.38%，最大约2.88%；在25个及以上位置的问题中CPLEX常内存不足或时间过长，DAL可用更短且更稳定的计算时间获得近似最优解。该基准评价是支持“DAL heuristic provided near optimal solutions in short computer times”这一核心主张的关键证据。
- Decision: 客观指标方面：核心指标为WSI运营成本、求解时间和与最优解的间隙，全部来自数学模型、CPU时间或精确求解器计算，不依赖人类主观判断；核心目标是构建和求解WSI服务器选址模型以最小化运营成本，并通过高效启发式在合理时间内获得近似最优解，无并列的同等核心目标。Benchmark方面：作者在实验部分明确用“We benchmarked DAL against CPLEX 8”陈述基准评价，将DAL与精确求解器CPLEX 8在多个模拟问题类别上比较，以目标函数间隙和计算时间为核心证据，支持“近最优+短时间”的核心改进主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.82

## AKEGIS: automatic keyword generation for sponsored search advertising in online retailing

- Year/journal: 2019 / Decision Support Systems
- DOI: 10.1016/j.dss.2019.02.001
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "广告关键词数量", "measurement_cn": "从Google AdWords账户中统计每日活跃关键词数，并相对于t=0标准化；DiD估计AKEGIS的影响。", "objectivity_reason_cn": "关键词数量是广告账户中的可审计事实，不依赖人的感受或语义判断。"}, {"name_cn": "每次点击成本 (CPC)", "measurement_cn": "通过公司竞价管理软件记录的实际支付成本，按日汇总并相对于t=0标准化。", "objectivity_reason_cn": "CPC是竞价交易产生的实际费用，属于可验证的财务/交易数据。"}, {"name_cn": "转化率 (Conversion Rate)", "measurement_cn": "访客中完成购买的比例，通过在线商店的交易日志和访问日志计算，按日汇总并相对于t=0标准化。", "objectivity_reason_cn": "转化率基于实际购买行为（交易事实），不依赖主观体验或语义评价。"}, {"name_cn": "每关键词印象数", "measurement_cn": "Google AdWords中每个关键词的广告展示次数除以关键词数，按日汇总并相对于t=0标准化。", "objectivity_reason_cn": "展示次数由广告系统日志客观记录，是可审计的事实。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在两个大规模在线商店（商店A与商店B）上进行现场DiD评价。商店A实施AKEGIS，商店B保持原有由人工专家（manual experts/state-of-the-art approach）管理的关键词生成方法作为对照。结果比较了关键词数量、每关键词印象数、每次点击成本和转化率四个客观指标，AKEGIS相对于人工基准显著提升了关键词数量、降低了CPC并提升了转化率。
- Decision: 文章所有核心成功指标均为客观可测量的业务指标（关键词数、CPC、转化率、印象数），不包含主观量表或人类语义判断。论文的最终设计目标和核心贡献是AKEGIS对这些客观指标的提升，消费者搜索行为理论仅作为设计基础并非并列核心目标。在benchmark方面，虽然只有一个明确出现“benchmark”的表述，但它出现在讨论部分，明确指称人工专家方法为基准方法（state-of-the-art approach），且该基准比较正是支撑核心绩效提升主张的关键证据；对照对象明确（manual experts、对照组商店B），结果报告了相对提升而非孤立数值。因此两个门槛均通过，strict_include=true。
- Confidence: 0.82

## An Information Diffusion-Based Recommendation Framework for Micro-Blogging

- Year/journal: 2011 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00271
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "故事覆盖率 (Story Coverage, SC)", "measurement_cn": "在测试期（5月3日-16日）由推荐账号集合覆盖的“重要故事”数量（或按扩散参与者加权的数量）。故事通过K-means和扩展Jaccard连通分量对推文进行自动聚类识别，并筛选被三个以上账号发布的故事。", "objectivity_reason_cn": "故事集合由确定性文本聚类算法生成，不依赖人类评分或语义偏好；某账号是否发布某故事可通过推文时间戳和内容核对，属于可审计事实。"}, {"name_cn": "阅读负担 (Reading Effort, RE)", "measurement_cn": "测试期内订阅推荐账号集合后需要阅读的推文总数，即该集合中所有账号发布的推文数量之和（或并集大小）。", "objectivity_reason_cn": "推文数量可由系统日志统计，不涉及用户主观感受；虽然名称含“Reading”，但操作化为可数推文数。"}, {"name_cn": "延迟时间 (Delay Time, DT)", "measurement_cn": "对于每个故事，从该故事在社区首次出现到被推荐集合中任一账号捕获的时间差，测试期内取平均/中位数。", "objectivity_reason_cn": "基于推文时间戳的净值，可审计、可复算。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 作者在自行收集的Twitter H1N1数据集上，用第一周推文训练推荐、后两周推文测试，将扩散推荐方法与HITS(Authority)、HITS(Hub)、Google Site Search、Twitter Find People、最多粉丝、最多推文六种基准方法比较，报告SC、RE、DT、Recall、Precision和扩展F*。扩散方法在全部四种参数设置下的F*均高于所有基准。
- Decision: 客观指标方面：核心评价指标SC、RE、DT和扩展F*均为可由推文时间戳、内容计数和自动聚类可复算的客观量，不依赖人类主观评价或语义评分；全文研究问题、设计目标、评价和贡献声明均围绕这些指标的提升。唯一核心目标虽然包含新方法框架，但该方法学成分是实现指标改进的手段，未构成并列核心贡献。Benchmark方面：作者虽未使用公开命名数据集，但在摘要、4.3节和结论中反复以benchmark methods/approaches明确陈述系统化基准比较，并提供了6种明确对照方法；该基准比较在评价语境中作为证明核心改进主张的关键证据。故两个模块均通过，strict_include=true。
- Confidence: 0.82

## Applying rough sets to market timing decisions

- Year/journal: 2004 / Decision Support Systems
- DOI: 10.1016/s0167-9236(03)00089-7
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "净收益（Net Profit）", "measurement_cn": "交易系统在历史/验证期内的总利润，基于价格差计算，忽略佣金和滑点，直接从交易记录或价格数据得出。", "objectivity_reason_cn": "净收益是客观可审计的市场交易结果，不依赖人的感受、语义评价或价值判断。"}, {"name_cn": "夏普比率（Sharpe Ratio）", "measurement_cn": "收益均值除以收益标准差（式2），由交易系统的收益序列计算。", "objectivity_reason_cn": "夏普比率是对可观测交易收益的统计度量，数值可复现，不依赖主观判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在S&P 500指数数据上，将基于RoughSOM/粗糙集构建的交易系统与buy-and-hold策略进行比较，报告1988–1998和1999年两个时期的net profit、Sharpe Ratio、交易次数、胜率等，并以buy-and-hold作为明确参照基准；结果显示整个1988–1999期间交易系统净收益优于buy-and-hold，结论还提到在其他三个指数上也支持该分析。另有UCI数据集上的预测精度比较（RoughSOM vs 原始rough sets），但核心benchmark评价是与buy-and-hold策略的交易绩效对比。
- Decision: 客观指标方面：核心成功指标为净收益、夏普比率等市场交易绩效，完全客观可测量，不依赖人类语义判断；核心目标是构建并验证基于粗糙集的交易系统，以客观交易绩效提升作为唯一核心贡献，未发现并列的主观目标或独立理论/制度贡献。Benchmark方面：全文存在明确的benchmark表述（buy-and-hold strategy作为基准），位于结果与讨论部分，属于评价语境，并且该比较用于支撑交易系统绩效改进的核心主张，有明确参照点buy-and-hold，因此满足benchmark门槛。综上两个模块均通过，strict_include为true。
- Confidence: 0.82

## Arbitrage pricing theory-based Gaussian temporal factor analysis for adaptive portfolio management

- Year/journal: 2004 / Decision Support Systems
- DOI: 10.1016/s0167-9236(03)00082-4
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "组合夏普比率（Sharpe ratio）", "measurement_cn": "由测试期组合每日收益计算，S_p = M(R_T) / sqrt(V(R_T))，其中M(R_T)为平均收益，V(R_T)为收益方差/风险；亦使用下行风险V_T^-和上行波动V_T^+的改进夏普比率变体。", "objectivity_reason_cn": "组合收益由历史股价/指数、权重规则和交易成本公式确定计算，不依赖人的感受、语义评价或主观偏好；夏普比率等指标是可由市场数据和算法确定性复算的财务绩效指标。"}, {"name_cn": "平均收益率与风险/波动率", "measurement_cn": "测试期组合日收益的均值、标准差、下行风险和上行波动，按文中公式由实际收益数据计算。", "objectivity_reason_cn": "这些指标均为对投资组合收益分布的可审计统计量，数据来源为香港市场股票和指数价格，值可被客观验证。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在1998-1999年香港市场522个交易日数据上（前400个训练、后121个测试）进行模拟：核心实验在四种交易场景下将APT-based组合与return-based组合比较，报告夏普比率提升（场景I +38.24%、场景II +72.69%、场景III +65.20%、场景IV +90.97%）；改进夏普比率部分以场景I的APT-based方法或上一节改进方法作为benchmark，比较改进前后的收益、风险、下行风险、上行波动和夏普比率。
- Decision: 核心指标为组合夏普比率、收益率和风险/波动率，完全由市场数据和确定性公式计算，不包含主观评价或人类语义判断，属于完全客观指标。研究问题、设计目标、实验评价和贡献声明均围绕最大化Sharpe ratio等客观投资绩效指标，客观指标提升是唯一核心目标与核心贡献。全文在评价语境中明确使用'benchmark'一词，并以return-based组合、场景I的APT-based方法或上一节改进方法作为明确参照点，benchmark比较结果直接支撑客观绩效提升主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.82

## Augmenting Social Bot Detection with Crowd-Generated Labels

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1136
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "账户级社交机器人检测性能（F1、精确率、召回率、AUC）", "measurement_cn": "在保留测试集账户上，由分类器对bot/非bot账户分类，对照777个经10+次众包举报过滤的bot账户作为ground truth，计算bot类precision/recall、macro-F1、micro-F1、AUC（Table 6/7）。", "objectivity_reason_cn": "目标构念是账户是否为算法生成的bot，属于外部可核验事实标签；指标由分类输出与事实标签比对计算，不依赖人类体验或语义评价。"}, {"name_cn": "时间到检测率（time-to-detection）", "measurement_cn": "在账户发布10/25/50条消息时以及收到1/5/10条crowd label时，统计已知bot被检测出的百分比（Table 8/9）。", "objectivity_reason_cn": "基于系统日志中账户消息数量与检测状态的客观计数，外部可审计。"}, {"name_cn": "面向新批次bot的检测性能保持（precision/recall变化百分比）", "measurement_cn": "将原训练模型应用于2019年新识别的260个bot账户，比较precision/recall相对原实验的百分比变化（Table 10）。", "objectivity_reason_cn": "检测目标仍是事实性bot标签，指标由分类输出与ground truth比对得出。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: Cresci et al. (2017) social spambot Twitter benchmark dataset | Garcia-Silva et al. (2019) BERT-based Twitter bot detection setting
- Benchmark evaluation: 在Cresci et al. (2017) Twitter数据上，作者将BERT模型及若干传统特征与Garcia-Silva et al. (2019)的BERT结果（F1=0.8388）比较，并报告可比或略优的结果；同时用restricted feature sets对核心模型进行benchmark式消融（Table 7），比较完整增强模型与排除topic/sentiment/speech acts等特征的模型，验证crowd reaction与speech acts对bot检测性能的贡献；Table 6比较传统特征基线与增强模型。
- Decision: 该文核心目标为通过crowd-generated labels和speech act特征提升社交机器人检测的客观性能（F1、AUC、检测率等），构念为事实性bot标签，检测性能由系统输出与ground truth比对计算，不依赖主观感受，属于objective_fixed_factual_labels，且核心贡献声明、研究问题和评价结构均围绕该客观指标提升，属exclusive_objective_improvement。benchmark方面，正文在4.2.3、4.4.1、4.4.4中使用benchmark/benchmarking对中间分类器、核心模型的restricted feature sets消融以及直接对照Garcia-Silva et al.在Cresci et al. (2017)数据上的结果进行系统化评价；消融benchmark直接支撑‘crowd reactions/speech acts提升检测性能’的核心主张，且均含明确参照点。综合两个模块均通过，strict_include=true。
- Confidence: 0.82

## Communication-Garden System: Visualizing a computer-mediated communication process

- Year/journal: 2008 / Decision Support Systems
- DOI: 10.1016/j.dss.2008.02.004
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "任务完成正确率（有效性）", "measurement_cn": "用户在使用 Communication-Garden 图形界面或 Netscape Messenger 文本界面完成事实性理解任务时，答对任务的比例；每个任务有明确正确答案。", "objectivity_reason_cn": "任务答案基于存档中的可核验事实（如日期、消息数、参与者数、线程数等），不由用户主观感受或语义评价决定。"}, {"name_cn": "任务完成时间（效率）", "measurement_cn": "用户完成每个任务所花费的时间，通过实验记录。", "objectivity_reason_cn": "时间是可独立测量的外部客观指标，不依赖用户感受或质量判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在系统评价部分，将 Communication-Garden 的 Content Summary、Interaction Summary、Expert Indicator 图形界面与 Netscape Messenger 文本界面进行比较；比较指标包括客观任务完成正确率、任务完成时间，以及附加的感知易用性和感知有用性。结果多数任务类型上图形界面优于文本界面，支撑了可视化设计的核心改进主张。
- Decision: 客观指标方面，核心成功指标为任务完成正确率和任务完成时间，均属于完全客观、可独立验证的行为绩效；主观感知量表仅为附加补充结果，不构成并列核心目标。核心目标为验证可视化表示在传递事实性统计与模式方面的有效性，属于唯一的客观绩效改进目标。Benchmark 方面，作者在系统评价部分明确将 Netscape Messenger 文本界面称为 benchmark system，并在该基准上比较图形界面与文本界面的客观任务绩效，比较具有明确参照点，且结果直接支撑核心改进主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.82

## Consumer Acquisition for Recommender Systems: A Theoretical Framework and Empirical Evaluations

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2023.1229
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "推荐系统性能（RMSE / AUC / 敏感性 / 准确率）", "measurement_cn": "在MovieLens 100K上使用SVD计算RMSE；在Kelkoo上使用二元矩阵分解计算AUC、敏感性和准确率；在动态或随机获取序列后基于用户实际消费数据（评分或点击）计算。", "objectivity_reason_cn": "基于客观历史消费数据（电影评分、点击/不点击行为）的预测准确性指标，不依赖人的主观评价、偏好或体验。"}, {"name_cn": "公司效用（firm utility）", "measurement_cn": "按公式(1) U_F(S(n)) = 系统加权价值 + 价值潜力 - 激励支出，在模拟实验中由模型参数和消费者接受/拒绝模拟结果计算。", "objectivity_reason_cn": "由明确数学公式和模拟参数确定，属于可审计的利润/效用数值，不涉及人类语义或主观评价。"}, {"name_cn": "消费者剩余（consumer surplus）", "measurement_cn": "按公式(3) U_C(s*) = 网络外部性效用 + 激励 - 参与成本，由模型参数和模拟参与成本计算。", "objectivity_reason_cn": "虽然参与成本是模拟参数，但数值由确定性公式计算，不依赖真实用户的自我报告或主观体验评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: MovieLens 100K | Kelkoo (KASANDR)
- Benchmark evaluation: 在两个真实数据集（MovieLens 100K和Kelkoo）上，分别采用warm-start和cold-start两种方案，将动态获取序列与200个随机获取序列比较，报告RMSE（或AUC、敏感性、准确率）、公司效用、消费者剩余、获取人数和总激励，并用单侧t检验进行统计比较。
- Decision: 文章核心目标是设计并评估面向推荐系统的动态消费者获取策略，其成功标准完全由客观指标构成：推荐系统预测性能（RMSE/AUC/敏感性/准确率）、公司效用、消费者剩余，均为可审计的模型计算值，不涉及人类主观评价或语义判断；全文在摘要和评价方法中明确使用“benchmark”一词，将动态获取序列与200个随机获取序列系统比较，并在MovieLens 100K和Kelkoo两个标准数据集上作为核心评价证据，比较对象明确、结果支撑核心提升主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.82

## DarkNetExplorer (DNE): Exploring dark multi-layer networks beyond the resolution limit

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113537
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "渐近惊奇值 (Asymptotic Surprise, AS)", "measurement_cn": "从网络划分中根据KL散度公式计算，衡量社区内链接相对随机期望的偏离；结果为确定性数值。", "objectivity_reason_cn": "完全由网络拓扑和划分决定，不依赖人的感知、语义或价值判断。"}, {"name_cn": "显著性 (Significance)", "measurement_cn": "根据社区在随机图中的出现概率计算，是结构上的统计显著性度量。", "objectivity_reason_cn": "由网络结构和划分的统计性质确定，无主观成分。"}, {"name_cn": "性能 (Performance)", "measurement_cn": "计算正确解释的节点对比例，基于节点间是否位于同一/不同社区。", "objectivity_reason_cn": "基于图结构的可计算比例，不依赖人类评价。"}, {"name_cn": "内部密度 (Internal density)", "measurement_cn": "社区内部连接相对于潜在连接的比例，由边和节点数确定。", "objectivity_reason_cn": "直接由网络拓扑计算。"}, {"name_cn": "电导 (Conductance)", "measurement_cn": "社区与外部连接边数除以社区内边数加外部边数，反映社区隔离程度。", "objectivity_reason_cn": "由边集确定，是标准化结构度量。"}, {"name_cn": "非单例社区数量", "measurement_cn": "算法输出的包含多个节点的社区个数，直接计数。", "objectivity_reason_cn": "客观可审计的计数。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: Noordin Top network | Caviar network | Boko Haram network
- Benchmark evaluation: 在三个真实多层暗网数据集上评估DNE，并与多片模块度Louvain和multiplex InfoMap两种现有方法对比；结果表（Table 5）报告AS、模块度、电导、内部密度、Significance、Performance，以及非单例社区数量，并展示AS比较图（Fig. 6）。
- Decision: 文章以提出并验证DNE社区检测算法为核心，目标是在多层暗网中找到'小且好'的社区，通过最大化渐近Surprise等结构度量实现，并在三个命名真实数据集（Noordin Top、Caviar、Boko Haram）上以Louvain和InfoMap为基准比较，报告AS、Significance、Performance、内部密度、电导等客观指标提升；客观指标为唯一核心目标，无主观体验或理论机制等并列核心贡献；存在明确benchmark表述，且评价处于实验部分并支撑核心改进主张。
- Confidence: 0.82

## Decision support for multi-unit combinatorial bundle auctions

- Year/journal: 2007 / Decision Support Systems
- DOI: 10.1016/j.dss.2006.10.009
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "投标人利润（占完美信息最大利润的百分比）", "measurement_cn": "在随机生成的逆向组合拍卖实验中，根据生成的“真实”成本函数和WDP/数量支持优化模型，计算各投标人从数量支持工具建议中获得的利润，并与完美信息情形下的最大利润进行比较。", "objectivity_reason_cn": "利润是由模型输入成本函数和优化求解确定得出的货币/经济数值，不依赖人的感受、语义评价或主观判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在作者自己生成的随机组合拍卖实验上评价数量支持工具；以完美成本信息情形作为上界基准、随机成本参数作为无信息基准，报告dual heuristic和random heuristic所获利润占完美信息最大利润的百分比，并进行t检验。
- Decision: 本文核心是提出并测试组合拍卖中投标人数量支持工具，衡量指标为投标人利润（占完美信息上界百分比），该指标由随机生成的成本函数与优化模型确定，无主观评价；大量实验比较dual heuristic与random/perfect information基准，并在第4.2节明确使用benchmark一词，因此同时满足客观指标、唯一核心目标和明确benchmark比较。排除触发码为空。
- Confidence: 0.82

## Designing Core-Selecting Payment Rules: A Computational Search Approach

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2022.1108
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "效率 (Efficiency)", "measurement_cn": "机制在BNE策略下实现的社会福利期望值除以最优配置的社会福利期望值，见式(4)，通过数值积分或蒙特卡洛采样计算。", "objectivity_reason_cn": "基于真实估值和配置结果计算，属于可审计的经济结果，不依赖人的感知或语义判断。"}, {"name_cn": "收入 (Revenue)", "measurement_cn": "机制在BNE下所有赢家支付总额的期望值，相对于VCG收入的比值，见式(5)。", "objectivity_reason_cn": "收入由规则和报价计算得出，是客观的支付金额，不涉及主观评价。"}, {"name_cn": "激励 (Incentives)", "measurement_cn": "BNE策略与真实报价策略之间的L2/L1距离，见式(6)，由算法求解的ε-BNE计算。", "objectivity_reason_cn": "该指标是数学上定义的均衡偏离程度，反映策略性扭曲，不依赖人类体验或价值判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 作者在LLG的29个变体设置和LLLLGG域中对366个备选规则进行系统化基准比较，以QUADRATIC作为核心基准，报告效率、收入和激励的改进百分比；并额外对比first-price和reserve price-weighted规则。
- Decision: 本文以计算搜索方法寻找在效率、收入和激励三个完全客观、可由形式模型和算法计算的结果指标上优于QUADRATIC的MRC选择支付规则。核心目标和贡献均围绕这三个客观指标提升；全文不依赖主观量表或人类语义评价。评价部分以QUADRATIC为明确基准，在LLG和LLLLGG标准设置中进行系统化比较，所有核心改进主张都建立在这些基准比较之上。因此，客观指标门槛、唯一核心目标门槛和基准门槛均满足。
- Confidence: 0.82

## Digression and Value Concatenation to Enable Privacy-Preserving Regression

- Year/journal: 2012 / MIS Quarterly
- DOI: 10.25300/misq/2014/38.3.03
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "敏感值披露风险（RSD）", "measurement_cn": "基于匿名化分组后敏感属性的组内离散度与整体离散度的比值计算，RSD 越大表示披露风险越低，完全由数据分布和分组结构决定。", "objectivity_reason_cn": "RSD 是公式化的统计量，不依赖人的感受、语义评价或专家判断，可由发布数据和敏感属性值直接计算。"}, {"name_cn": "回归预测误差（MAPE）", "measurement_cn": "用 10 折交叉验证，在匿名化训练数据上构建线性回归或回归树模型，再在匿名化测试集上计算平均绝对百分比误差。", "objectivity_reason_cn": "MAPE 是预测值与观测值间的可审计误差，属于可客观测量的技术指标，不涉及主观质量判断。"}, {"name_cn": "运行时间", "measurement_cn": "实验记录算法完成匿名化的秒数，如 Census 数据集上 MART 约 10.5 秒、baseline 约 8345 秒。", "objectivity_reason_cn": "运行时间是可客观观测的计算资源消耗指标。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: UCI Credit dataset (Bache and Lichman 2013) | UCI Census dataset (Bache and Lichman 2013)
- Benchmark evaluation: 在 Credit、Census 以及 Offer、Alcohol 等真实数据集上，通过 10 折或 2 折交叉验证比较 MART 与 regression Mondrian（RM）、经典 k-anonymity baseline；报告 RSD、线性回归 MAPE、回归树 MAPE 与运行时间。结果用于证明 MART 在相同 k 值下披露风险更低，且回归数据效用更好。
- Decision: 文章核心目标是降低回归攻击下的敏感值披露风险并保持回归分析的数据效用，两者均通过 RSD、MAPE、运行时间等完全客观可测量的指标评价；实验在 UCI Credit、UCI Census 等公开数据集上进行，并与 RM、k-anonymity baseline 明确比较，benchmark 评价直接支撑核心改进主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.82

## Estimating Network Effects in Two-Sided Markets

- Year/journal: 2020 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2019.1705509
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "预测准确率：买家和卖家数量的平均绝对百分比误差（MAPE）", "measurement_cn": "在84,672个模拟市场中，用前52周数据校准净变化模型与流入-流出模型，预测后52周买家和卖家数量，计算第T+52周的MAPE；同时也以模拟中的真实网络效应参数作为参数恢复准确性的基准。", "objectivity_reason_cn": "MAPE由模型预测值与模拟/实际客户数量直接计算，不依赖人的感受、语义评价或主观判断；参数恢复通过模拟已知真值比较，也是客观可计算的统计性能。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 作者构建了84,672个模拟双边市场，系统改变网络效应参数与误差水平，将传统净变化模型（net change model）和新提出的流入-流出模型（influx-outflow model）在同一数据上校准并预测，核心比较指标为买家和卖家数量的MAPE。结果显示流入-流出模型平均MAPE显著更低（买家11.63% vs 16.12%，卖家24.55% vs 48.02%），Wilcoxon符号秩检验p<.01；另用logistic回归考察在何种条件下净变化模型更优。该模拟benchmark是支持“新模型提升网络效应估计/预测性能”的核心证据。
- Decision: 客观指标门槛：核心目标是提出流入-流出模型，并通过大规模模拟证明其在预测客户数量和恢复真实网络效应参数上优于传统净变化模型；MAPE、参数恢复、Wilcoxon检验等全部为客观可计算指标，不涉及主观感受或语义评价，且客观性能提升是唯一核心目标和贡献。Benchmark门槛：摘要明确使用benchmark一词陈述“将新模型与传统模型进行基准比较”，相应模拟比较位于评价语境，比较对象明确（传统净变化模型），其结果直接支撑核心提升主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.82

## Fraudulent review detection model focusing on emotional expressions and explicit aspects: investigating the potential of feature engineering

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113728
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "欺诈评论/欺诈者检测性能：Precision、Recall、F1、AUC", "measurement_cn": "在Yelp真实评论数据集（Rayana & Akoglu收集的Yelp过滤标签）及Amazon/Yelp Open验证数据集上，经5折交叉验证，由分类结果计算P/R/F1/AUC；M-SMOTE在UCI及Amazon/Yelp数据集上与SMOTE等比较也使用同一组指标。", "objectivity_reason_cn": "目标标签是平台/系统标记的欺诈评论或欺诈账户（fraud/fake review固定事实标签），不依赖用户满意度、偏好或语义质量评价；P/R/F1/AUC由预测标签与固定标签对比计算，数值可审计、可复算。"}, {"name_cn": "M-SMOTE算法在不同不平衡数据集上的P/R/F1/AUC", "measurement_cn": "在UCI Machine Learning Repository六个数据集以及Amazon/Yelp数据集上，比较M-SMOTE与SMOTE及原始数据在XGBoost和随机森林下的P/R/F1/AUC。", "objectivity_reason_cn": "UCI等数据集的分类标签是疾病、流失、类别等固定事实标签；比较指标为客观分类性能指标，不涉及主观感受或专家质量评分。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: Yelp.com restaurant review dataset (Rayana and Akoglu [51]) | Yelp Open Dataset | Amazon dataset (Jindal and Liu [23]) | Amazon Deception-Detection dataset | UCI Machine Learning Repository: Haberman, Breast cancer, Telecom Churn, Abalone
- Benchmark evaluation: 作者在Yelp真实餐厅评论数据集上开发并评价模型，同时在Amazon/Yelp Open等数据集上重复特征工程和数据预处理流程；在UCI Repository上检验M-SMOTE在不同不平衡数据集上的普适性；并在Section 6将最终模型的结果与Jindal & Liu、Feng et al.、Zhang et al.、Kumar et al.、Rayana & Akoglu等先前方法在Yelp/Amazon上的AUC/准确率进行比较，最终在Yelp上达到P=79.4%、R=83.5%、F1=85.3%、AUC=87.4%。
- Decision: 该文是欺诈评论检测的ML方法论文。核心构念为平台标记的欺诈评论/欺诈者，属于客观固定事实标签；核心评价指标全部为P/R/F1/AUC，无主观量表或人类语义评分作为成功标准。研究问题、假设、实验和贡献均围绕提高客观检测性能展开，不存在并列的理论机制、主观体验或政策建议核心目标。benchmark方面，作者在引言明确声明在Yelp及若干benchmarking数据集上评价，并在实验和验证部分分别使用UCI Repository及Yelp/Amazon多数据集，且与SMOTE、原始baseline和多个先前研究进行数值比较，benchmark结果是支撑核心提升主张的关键证据。因此满足纳入条件。
- Confidence: 0.82

## Interpretable cost-sensitive regression through one-step boosting

- Year/journal: 2023 / Decision Support Systems
- DOI: 10.1016/j.dss.2023.114024
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "平均误预测成本", "measurement_cn": "在 2×5 交叉验证的训练/测试数据上，按 LinLin、QuadQuad、ExLin 等非对称成本函数计算预测残差的平均成本", "objectivity_reason_cn": "成本函数和残差均为数学定义，数值由数据与算法确定性计算，不依赖人的感受、偏好或语义评价"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: Abalone | Bank (8FM) | House (8L) | KC House | UCI Machine Learning Repository / DELVE repository
- Benchmark evaluation: 在 4 个公开回归数据集上，以 LGBM、NN、RF、MT、LR 等为基础模型，将 OSB 与初始基础回归成本、Bansal et al. (BSZ)、Zhao et al. (BSZ-EXT)、Hernandez-Orallo (HER) 以及直接优化成本函数的 LightGBM/NN 方法进行比较；结果表显示 OSB 在多数数据集和成本函数组合上取得更低的平均误预测成本。
- Decision: 核心指标为平均误预测成本：它由成本函数和预测残差确定性计算，完全客观，不依赖人的感知或语义判断。论文的研究问题、方法论设计、实验评价和贡献声明均围绕在回归中降低该成本展开，可解释性和计算效率是辅助特性而非独立成败指标，因此 core_goal_status 为 exclusive_objective_improvement。Benchmark 门槛通过：作者在命名的公开数据集（UCI/DELVE 等来源的 Abalone、Bank、House、KC House）上系统评价 OSB，并与初始成本及多种现有方法显式比较，结果支持核心成本下降主张。因此 strict_include=true。
- Confidence: 0.82

## Listen to me — Evaluating the influence of micro-blogs

- Year/journal: 2014 / Decision Support Systems
- DOI: 10.1016/j.dss.2014.03.008
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "信息传播有效性（接收消息节点比例）", "measurement_cn": "在模拟网络中，接收某条消息的节点数占网络总节点数的比例；重复模拟500次取均值，并通过与基准方法对比计算提升百分比。", "objectivity_reason_cn": "该指标完全基于网络拓扑、传播规则和模拟参数计算得到，节点计数可审计、不受人类感知或语义评价影响。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 作者在从Twitter收集的'appleincnews'社区数据上，将所提框架与Kiss and Bichler [26]的方法进行系统对比，以信息传播覆盖率（接收消息节点比例）为核心评价指标。Tables 5-8展示了多种参数组合下所提方法相对基准方法的改进幅度（如23.94%至62.83%），该对比直接支撑核心提升主张。
- Decision: 客观指标方面：核心成功指标为信息传播有效性（接收消息节点比例），完全由网络模拟客观计算，不依赖主观评价；该指标提升是唯一核心目标，研究问题、评价结构和贡献声明均围绕其展开。Benchmark方面：全文在图7标题明确使用'benchmarked approach'，并在Tables 5-8中与Kiss and Bichler [26]基准方法进行系统比较，所有比较均以传播覆盖率提升为核心证据，存在明确参照点。因此两个条件均满足，strict_include为true。
- Confidence: 0.82

## Multi-objective design of hierarchical consensus functions for clustering ensembles via genetic programming

- Year/journal: 2011 / Decision Support Systems
- DOI: 10.1016/j.dss.2011.01.014
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "校正兰德指数（Corrected Rand, CR）", "measurement_cn": "将算法最终输出的数据划分与数据集中已知的真实结构/参考划分进行标签匹配，计算CR值；每个已知结构取多次运行的最高CR，再对多次运行取平均。", "objectivity_reason_cn": "CR衡量算法划分与预先已知的数据结构标签之间的一致性，标签属于可外部核验的事实性参考划分（人工合成结构、UCI类别标签、生物信息学类别标签），计算过程不依赖人的感受、语义价值或偏好判断。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: UCI repository 的 iris 数据集 | UCI repository 的 glass 数据集
- Benchmark evaluation: 在UCI benchmark数据集iris和glass上运行MCHPF1，并与其他基础/高级聚类方法比较；结果以平均CR值列于表7、表8，并纳入第4.6节的Friedman/Nemenyi统计检验，用于支持MCHPF在聚类划分质量上的提升。
- Decision: 客观指标方面，核心成功标准是校正兰德指数（CR），通过对比算法输出划分与已知参考结构标签计算，属于可独立于人的主观体验核验的事实性标签匹配指标；全文没有满意度、偏好、语义质量评分等主观构念。唯一核心目标是在多个数据集上稳健地提升聚类划分质量，研究问题、实验设计和贡献声明均围绕该客观指标展开，没有并列的核心理论贡献或主观成功标准。Benchmark方面，文中明确将UCI的iris和glass称为benchmark数据集，并在实验设置中将其作为评价场地；包含与KM、HAL、HSL、SNN、HBGF、SC、MOCK、MOCLE等明确参照物的CR比较，统计检验进一步支撑MCHPF的核心提升主张。因此严格纳入。
- Confidence: 0.82

## Recognition of human activities for wellness management using a smartphone and a smartwatch: A boosting approach

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113426
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "Accuracy（准确率）", "measurement_cn": "在保留测试集上由预测标签与 ground truth 标签计算，(TP+TN)/(TP+TN+FP+FN)，用于评估 boosting 与传统 ML 的活动分类性能。", "objectivity_reason_cn": "活动类别（walking、standing、sitting、exercise、sleeping）是可外部核验的客观行为事实，非主观质量评价；计算结果由分类预测和固定标签确定。"}, {"name_cn": "F1 Score", "measurement_cn": "精确率与召回率的调和平均数，在测试集混淆矩阵上计算。", "objectivity_reason_cn": "基于预测标签和固定事实标签计算，不依赖人的感受、语义判断或偏好。"}, {"name_cn": "AUC（ROC 曲线下面积）", "measurement_cn": "在模型验证阶段通过 bootstrap 重抽样获得 ROC 曲线并计算 AUC，用于选择最优模型参数。", "objectivity_reason_cn": "由分类器输出分数与固定事实标签计算，属于可审计的预测性能指标。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: ExtraSensory dataset（公开的真人/情境识别数据集，由智能手机和智能手表传感器记录，walking/standing/sitting/exercise/sleeping 等标签）
- Benchmark evaluation: 作者在 ExtraSensory 数据集上使用 138 个传感器特征，分别训练 XgBoost、AdaBoost、Boosted C5.0，并与 Neural Network、SVM 以及先前的 LR [15]*、MLP [10]* 结果进行比较；同时进行特征工程，报告 Accuracy、F1、AUC。
- Decision: 该文以在 ExtraSensory 公开数据集上识别五类基本人类活动的 Accuracy、F1 和 AUC 作为唯一核心成功指标，核心贡献是 boosting 算法相较传统机器学习在该客观分类任务上的性能提升。基准评价使用 ExtraSensory 这一公开数据集，并与 Neural Network、SVM 及先前 LR/MLP 结果形成明确参照，支撑其核心提升主张。未发现主观量表或独立并列核心目标。
- Confidence: 0.82

## Redesigning Case Retrieval to Reduce Information Acquisition Costs

- Year/journal: 1997 / Information Systems Research
- DOI: 10.1287/isre.8.1.51
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "期望信息获取成本", "measurement_cn": "对每个属性赋予获取成本；算法在保留集上完成案例到簇的匹配时，按实际收集的属性累计成本，并在25次随机训练/保留划分上取平均。", "objectivity_reason_cn": "信息获取成本是可审计的货币/资源数值，由算法执行路径和给定属性成本决定，不依赖人的感受、意义理解或语义质量评价。"}, {"name_cn": "分类准确率（次要约束指标）", "measurement_cn": "系统在保留集上被正确分配到类别的案例比例；四个数据集均为预先标注且类别不重叠。", "objectivity_reason_cn": "使用的是预先存在的事实类别标签（如Zoo动物类别、Lymphography类别），可外部核验，不是专家对质量/价值的语义评分；且文章仅将其作为保证成本降低不牺牲准确率的次要约束。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: Zoo | Lymphography
- Benchmark evaluation: 在Zoo、Lymphography及两个人工数据集上，分别用CR_f、CR_lc、ID3_c训练后对保留集分配案例；通过回归方程和响应函数比较期望信息获取成本，结果支持ID3_c成本低于CR_lc、CR_lc成本低于CR_f。
- Decision: 客观指标方面，核心目标是降低可审计的信息获取成本；分类准确率作为固定事实标签上的次要约束，也是客观指标。全文无主观构念作为成功标准，成本降低是唯一核心目标与贡献。benchmark方面，文章虽未使用benchmark一词，但在UCI公开标准数据集Zoo和Lymphography（外加两人工集）上评价三种算法，并有明确参照点CR_f、CR_lc与ID3_c比较，结果直接支撑成本降低主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.82

## Simpler is better: Lifting interpretability-performance trade-off via automated feature engineering

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113556
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "分类AUC", "measurement_cn": "在OpenML任务定义的10个train/test split上，用测试集预测与真实二分类标签计算平均AUC和标准差。", "objectivity_reason_cn": "真实标签是外部可核验事实（如信用风险、垃圾邮件、故障等类别），AUC是确定性的预测性能统计量，不依赖人的感受或语义评价。"}, {"name_cn": "可解释性/简洁性（模型参数数的倒数）", "measurement_cn": "统计模型参数数量：线性模型系数数、SVM支持向量数、GBM树数×节点结构参数等，取倒数作为可解释性指标。", "objectivity_reason_cn": "参数数量是模型结构的可审计技术事实，按固定规则计数，未使用人工评分、偏好或感知量表；它是可解释性的客观代理，而非人类理解度直接测量。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: OpenML100（从中选取30个二分类数据集作为评价场地）
- Benchmark evaluation: 在OpenML100的30个二分类数据集上，对vanilla logistic regression、gbm default、gbm tuned、svm default以及对应的SAFE变体（SAFE gbm default/tuned、SAFE svm）使用平均AUC进行系统比较；同时用参数数倒数量化可解释性，并用Wilcoxon检验比较AUC和可解释性差异。benchmark结果直接支撑'简化模型不损失性能且提升可解释性'的核心主张。
- Decision: 全文以客观可复现的AUC和模型参数数作为成功标准，没有使用用户满意度、偏好等主观评分。核心贡献是SAFE ML框架能够在保持/提升性能的同时降低模型复杂度，这属于客观指标提升。Section 4.2在OpenML100的30个数据集上进行了明确命名的benchmark，并以vanilla logistic regression、gbm、svm等作为显式参照点，benchmark结果直接支撑核心提升主张。因此objective_metric与benchmark两个模块均通过，strict_include=true。
- Confidence: 0.82

## Software development cost estimation: Integrating neural network with cluster analysis

- Year/journal: 1998 / Information & Management
- DOI: 10.1016/s0378-7206(98)00041-x
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "平均百分比误差 (best average % error)", "measurement_cn": "在 COCOMO 数据集的 63 个历史项目上，将模型估算的开发成本与实际成本比较，计算百分比误差，并在不同训练/测试划分下取平均。", "objectivity_reason_cn": "实际开发成本是历史事实，预测值与实际值的差异可以确定性地计算，不依赖人的感受、偏好或语义判断。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: COCOMO dataset
- Benchmark evaluation: 在 COCOMO 数据集上，使用 63 个历史项目，通过聚类分析产生聚类信息，并结合神经网络进行成本估计。实验中的表 9 比较了纯神经网络（Pure NN）与集成聚类后的神经网络（NN+cluster）在四个不同测试集上的平均百分比误差，结果表明集成方法在所有测试集上均有改善。
- Decision: 客观指标方面，核心指标是 COCOMO 数据集上的平均百分比误差，完全由实际历史成本与预测成本计算，不涉及主观判断或语义评估；该指标是全文唯一核心目标和贡献。benchmark 方面，虽然全文未出现“benchmark”单词，但实验部分明确命名并使用公开领域标准数据集 COCOMO dataset 作为评价场地，并以纯神经网络作为显式参照，表 9 直接支持核心的成本估计精度提升主张，因此满足命名式 benchmark 门槛。两个模块均通过，故 strict_include=true。
- Confidence: 0.82

## Spoiled for Choice? Personalized Recommendation for Healthcare Decisions: A Multiarmed Bandit Approach

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1191
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "Precision@K / Recall@K", "measurement_cn": "将推荐的前K个干预项与用户周度实际参与记录比对，计算准确率与召回率；数据来自真实在线减重社区的用户参与日志。", "objectivity_reason_cn": "参与/未参与是平台记录的可审计行为事实，不依赖人的感受、质量判断或语义评价。"}, {"name_cn": "nDCG@K / MAP@K", "measurement_cn": "基于推荐排序与实际参与行为的排序指标，由确定性公式在参与日志上计算。", "objectivity_reason_cn": "排序质量由可观察的参与标签决定，是客观行为结果的排序度量。"}, {"name_cn": "DR@K / Simu@K（用户参与奖励）", "measurement_cn": "使用 doubly robust 离线评估和 omniscient simulation 生成或校正参与反馈，然后计算推荐表现。", "objectivity_reason_cn": "评估目标仍是对用户实际参与行为的预测和推荐效果；模拟器的反馈信号也是依据参与行为训练，不引入主观评价。"}, {"name_cn": "推荐多样性的 JSD 相似度", "measurement_cn": "计算推荐集合中干预类型的分布与真实用户选择类型分布之间的 Jensen-Shannon divergence。", "objectivity_reason_cn": "多样性分布由干预类型频次构成，是客观可计算的统计量。"}, {"name_cn": "用户改进率（user improvement）", "measurement_cn": "统计相比基准算法，从推荐中获得更多偏好项的用户比例；偏好项由实际参与反馈和推荐排名定义。", "objectivity_reason_cn": "“获得更多偏好项”以历史参与行为为计算依据，属于可审计的推荐质量结果，不依赖主观满意度。"}, {"name_cn": "期内减重率（扩展实验）", "measurement_cn": "以体重记录为基础，计算推荐后用户在期内体重不增加或下降的比例，作为健康结果目标。", "objectivity_reason_cn": "体重变化是外部可核验的生理/健康事实，不依赖人的主观判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在真实在线减重社区数据集上，将提出的 DLDE-MAB 与 CACF、SCF、PMF、CAMF、CB、hybrid_pure、hybrid_cacf、FAST、SLi-Rec、Caser、GRU4Rec、A2SVD、NextItNet、LSTUR、NPA、UCB、ε-greedy 等既有推荐和在线学习模型进行系统比较，报告 top-5/top-10 下的 Precision、Recall、nDCG、MAP、DR 和模拟评估；结果表明所提方法在各核心客观指标上全面优于基准模型，且差异大多统计显著。
- Decision: 客观指标方面：论文的核心目标是最大化用户对在线健康干预的持续参与，评价指标均为基于平台日志的行为参与指标（Precision/Recall/nDCG/MAP/DR/模拟参与），以及作为扩展的客观体重健康结果，不包含主观满意度、感知有用性或人工质量评分；唯一核心目标是由设计目标、优化问题和评价结构共同支持的客观参与指标提升。Benchmark 方面：第5.1节明确以“benchmark recommendation systems”和“state-of-the-art benchmarks”命名并呈现系统化基准比较，表4将所提模型与大量既有推荐和在线学习模型在多类客观指标上比较，且该比较是支撑核心参与指标提升主张的核心证据；具有明确参照点，因此同时满足 benchmark 的四个门槛。
- Confidence: 0.82

## Who should you follow? Combining learning to rank with social influence for informative friend recommendation

- Year/journal: 2016 / Decision Support Systems
- DOI: 10.1016/j.dss.2016.06.017
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "C@K（coverage rate at K）", "measurement_cn": "在 leave-one-out 评估中，移除一个目标用户实际反馈过的信息型好友，若该好友出现在推荐列表前 K 位则计为命中；C@K=|hit|/|T|，由系统反馈日志和推荐列表确定性计算。", "objectivity_reason_cn": "信息型好友被操作化为“其发布更新曾被目标用户点赞或回复”的用户，这是外部可审计的行为事实，不依赖研究者或用户的主观质量/价值判断。"}, {"name_cn": "MRR（mean reciprocal rank）", "measurement_cn": "对每个目标用户，取被移除的信息型好友在推荐列表中排名的倒数，再对所有用户平均；由推荐列表排名确定性计算。", "objectivity_reason_cn": "排名基于实际反馈日志和算法输出，构念是系统记录的行为事实，非主观评分。"}, {"name_cn": "DCRP（discounted cumulative ranking performance）", "measurement_cn": "根据信息型好友的反馈频率和推荐列表排名位置计算，是 DCG 的变体；值由日志频率和推荐列表确定性计算。", "objectivity_reason_cn": "反馈频率是实际行为次数，排名位置是算法输出，不依赖人的感受或语义质量评价。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: WISE 2012 Challenge Weibo dataset
- Benchmark evaluation: 在公开的 WISE 2012 Challenge 微博数据集上，选取 Data200 和 Data300 两个子集，采用 leave-one-out 程序评价所提方法（OurMethod_fix 和 OurMethod_adaptive）与九个既有方法，在 C@K、MRR、DCRP 上比较，并附统计显著性检验。结果表显示所提方法在大部分指标上优于基线方法，支撑核心的性能提升主张。
- Decision: 客观指标：核心结果指标 C@K、MRR、DCRP 全部由实际点赞/回复日志和推荐列表确定性计算，操作化构念是行为事实而非主观感知。唯一核心目标：全文设计、实验和贡献均围绕提升信息型好友推荐性能，不存在并列的主观体验、理论机制或制度政策核心目标。Benchmark：论文在评价部分公开命名并使用 WISE 2012 Challenge Weibo 数据集作为评价场地，明确将数据描述为 benchmark，并与九个基线方法进行对比，benchmark 比较结果是核心性能提升主张的直接证据。因此 strict_include=true。
- Confidence: 0.82

## Why some products compete and others don't: A competitive attribution model from customer perspective

- Year/journal: 2023 / Decision Support Systems
- DOI: 10.1016/j.dss.2023.113956
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "预测性能 Precision@N 和 Recall@N", "measurement_cn": "将用户数据按时间分为前90%训练、后10%测试；仅给定测试评论文本，按条件概率 p(e|w_test) 对产品排序，与实际被该用户评论过的产品集合比较，计算 Precision@N 和 Recall@N。", "objectivity_reason_cn": "ground truth 是用户在论坛中实际评论过的产品，属于可审计的线上行为；排序评价由确定性公式和系统日志计算，不依赖人的感受或语义评价。"}, {"name_cn": "竞争分群/主题的连贯性得分（coherence score）", "measurement_cn": "对每个竞争分群的Top代表产品和每个竞争主题的Top代表词，基于原始语料中产品共被评论次数或词语共现次数，按式(24)计算连贯性，再取平均；并与七个基准模型比较。", "objectivity_reason_cn": "该指标由语料中的共现计数和确定性公式计算，不是专家/用户的主观质量评分；虽然它被文献认为与人类判断相关，但此处作为完全自动化的语料统计指标使用。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: DMM | LDA | CNTM | Link-LDA | PTM | nS-ACA | nB-ACA
- Benchmark evaluation: 在自行采集的 Edmunds.com 汽车论坛数据上，将 ACA 与 DMM、LDA、CNTM、Link-LDA、PTM 以及两个消融版本 nS-ACA、nB-ACA 比较；评价内容为竞争分群和主题的 coherence scores（表2、表3）以及预测实际评论产品的 Precision@N/Recall@N（图8），ACA 在各项指标上一致最优，且多数差异显著。
- Decision: 客观指标方面：核心评价指标为预测实际评论产品的 Precision@N/Recall@N 和语料驱动的 coherence score，均为可计算、可审计的客观结果，不涉及用户满意度、感知质量或人工语义评分；研究问题和贡献声明均围绕 ACA 模型在这些客观指标上的提升展开。Benchmark 方面：摘要和实验部分明确使用 benchmark models/seven benchmarks 表述，并在评价语境中与多个既有模型和消融模型进行比较，比较结果直接支撑核心提升主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.82

## Detection of online phishing email using dynamic evolving neural network based on reinforcement learning

- Year/journal: 2018 / Decision Support Systems
- DOI: 10.1016/j.dss.2018.01.001
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "准确率 Accuracy", "measurement_cn": "正确分类为钓鱼邮件和正常邮件的样本数除以总样本数，基于模型输出与语料标签比对计算", "objectivity_reason_cn": "钓鱼/正常邮件是外部事实标签，分类是否正确可通过日志与标签确定，不依赖人的感受或语义质量判断"}, {"name_cn": "真正率 TPR / 召回率 Recall", "measurement_cn": "被正确识别为钓鱼邮件的样本数除以真实钓鱼邮件总数", "objectivity_reason_cn": "由系统预测与既定钓鱼/正常标签计算，结果可复核"}, {"name_cn": "真负率 TNR", "measurement_cn": "被正确识别为正常邮件的样本数除以真实正常邮件总数", "objectivity_reason_cn": "由系统预测与既定标签计算，客观可审计"}, {"name_cn": "假正率 FPR / 假负率 FNR", "measurement_cn": "正常邮件被误判为钓鱼的比例；钓鱼邮件被误判为正常的比例", "objectivity_reason_cn": "两类错误均可从分类结果与标签直接计数"}, {"name_cn": "精确率 Precision、F-Measure、AUC", "measurement_cn": "由 TP/FP/FN/TN 计算得到，AUC 基于预测得分与真实标签", "objectivity_reason_cn": "构念为分类性能指标，不涉及人类体验、价值或偏好"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: PhishingCorpus (Nazario, 2015) | SpamAssassin (Mason, 2005)
- Benchmark evaluation: 在公开邮件语料 PhishingCorpus（钓鱼邮件）和 SpamAssassin（正常邮件）上构造 9902 封邮件的数据集，其中 4000 封作为离线数据集，其余作为在线评估数据，评估 PEDS 在零日钓鱼邮件检测上的表现；得到 Accuracy 98.63%、TPR 99.07%、TNR 98.19%、FPR 1.81%、FNR 0.93%、AUC 99.43%，并在 Table 7 中与 Islam and Abawajy、Almomani、Khonji、Gansterer、Ramanathan、Ma、Toolan、Hamid 等已有方法比较。
- Decision: 本文以钓鱼邮件检测为任务，使用公开邮件语料上的分类性能指标（Accuracy、TPR、TNR、FPR、FNR、AUC）作为核心成功标准；这些指标基于 phishing/ham 事实标签和系统分类结果客观计算。研究问题、系统设计和贡献声明均围绕提升检测性能展开，没有将主观体验或理论机制作为并列核心目标。评价部分明确使用 PhishingCorpus 和 SpamAssassin 公开数据集，并在 Table 7 与多个既有方法进行显式比较，benchmark 评价直接支撑核心性能提升主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.8

## Diversity Preference-Aware Link Recommendation for Online Social Networks

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1174
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "多样性偏好匹配得分（DPMS）", "measurement_cn": "对每个画像维度，计算用户多样偏好向量 d^h 与被推荐好友集合的多样性分布 r^h 之间的余弦相似度，再对 H 个维度取平均。d^h 由用户既有好友在该维度上的取值计数构成，r^h 由被推荐候选人的画像取值计数构成；全部来自社交网络关系和画像数据，无人工评分。", "objectivity_reason_cn": "尽管名称中含“偏好”，论文将多样偏好严格操作化为好友画像取值的计数向量；该向量可由网络关系和画像属性直接复算，不依赖用户感受或语义判断。"}, {"name_cn": "精确率（Precision）", "measurement_cn": "推荐给用户的 k 个好友中，在下一时间窗口确实成为该用户好友的比例；基于系统记录的真实好友关系计算。", "objectivity_reason_cn": "真实好友建立是外部可核验事实，不依赖主观评价。"}, {"name_cn": "召回率（Recall）", "measurement_cn": "下一时间窗口新增的真实好友中，出现在推荐集合中的比例；基于真实链接日志计算。", "objectivity_reason_cn": "真实好友建立是外部可核验事实。"}, {"name_cn": "F1 分数", "measurement_cn": "Precision 和 Recall 的调和平均数，由上述客观指标计算。", "objectivity_reason_cn": "由两个客观指标组合得到，不包含主观判断。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: Google+ dataset (Gong et al. 2012)
- Benchmark evaluation: 在 Google+ 公开数据集（主文）和另一大型美国在线社交网络数据集（在线附录 D）上评价 DPA-LR；与 MMR、MSD、DPP、DiRec 等多样化基准方法，以及与 GCN-LR、GraphSage-LR、GAT-LR 等最新链接推荐方法比较；报告 DPMS、Precision、Recall、F1 指标，并在 k=6 到 k=14 等设置下展示提升。
- Decision: 本文以提升可客观计算的 DPMS 以及基于真实未来好友关系的 Precision/Recall/F1 作为唯一核心目标和核心贡献；全文评价由真实社交网络数据和系统日志驱动，不包含用户主观评分或满意度量表。第5.1节明确使用 benchmark/benchmarking 表述，将 DPA-LR 与多个多样化方法和最新链接推荐方法在 Google+ 公开数据集及另一大型数据集上进行比较，结果表构成核心提升主张的直接证据。所有 benchmark 门槛均满足，因此 strict_include=true。
- Confidence: 0.8

## Evolutionary approach to the development of decision support systems in the movie industry

- Year/journal: 2009 / Decision Support Systems
- DOI: 10.1016/j.dss.2008.12.008
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "净边际利润（net margin）", "measurement_cn": "通过准实验设计比较Pathé Amsterdam（DSS支持）与Rotterdam + The Hague（无DSS）在实施期（2001年9月至2002年2月）的净边际利润，并以基期（2001年1-8月）比例进行年化调整。数据来源于票房收入、特许经营利润和合同分成的会计记录。", "objectivity_reason_cn": "净边际利润是财务核算指标，由可审计的票房、特许经营和合同条款数据计算得出，不依赖人的感受、偏好或语义判断。"}, {"name_cn": "影院上座率（attendance）", "measurement_cn": "通过每周各影院实际售票记录获得，作为净边际利润的基础数据之一。", "objectivity_reason_cn": "上座率是客观交易记录，独立于主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在净边际利润影响评价中，以Rotterdam + The Hague两个未使用DSS的城市以及2001年1-8月基期作为benchmarks，通过准实验设计比较了Pathé Amsterdam（DSS支持）在2001年9月至2002年2月实施期的实际净边际利润与投影（无DSS）净边际利润，得出€277,959的相对提升，再考虑特许经营收入后总提升约€342,000，年化后约$900,000。
- Decision: 核心评价指标为净边际利润，来自财务核算和准实验对比，完全客观；该指标提升是排片DSS的主要目标和核心贡献，无并列的主观成功标准或独立理论贡献。Benchmark表述明确出现于5.1节评价语境，以Rotterdam + The Hague和基期作为对照参照点，直接支撑净边际利润提升的核心主张，满足benchmark比较中心地位。因此两个模块均通过。
- Confidence: 0.8

## Predicting home-appliance acquisition sequences: Markov/Markov for Discrimination and survival analysis for modeling sequential information in NPTB models

- Year/journal: 2007 / Decision Support Systems
- DOI: 10.1016/j.dss.2007.02.008
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "加权正确分类率 (wPCC)", "measurement_cn": "在留出样本上，用估计的 MNL 模型预测每个顾客下一次购买的产品类别，与实际购买类别比较；按类别相对频率的反比计算类别权重，得到加权 PCC。同时报告混淆矩阵、各类别 PCC 以及与比例机会准则 C_pro 的对比。", "objectivity_reason_cn": "购买类别来自零售商交易扫描数据库的实际购买记录，是外部可核验事实；wPCC 由确定性分类计数公式计算，不涉及人的感受、语义评价或价值判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 作者在评价 NPTB 模型时，将最终 MNL 模型的加权正确分类率 wPCC=0.1994（留出样本）与比例机会准则 C_pro=12.63% 进行比较，证明模型显著优于随机/默认期望水平；同时在同一评价框架下比较了 NULL、NULL+ORDER、NULL+DURATION、NULL+ORDER+DURATION 四种模型，以及 MNL/HEV/PROBIT 三种模型形式。该基准比较直接支撑‘模型预测能力提升’的核心主张。
- Decision: 核心评价指标为加权正确分类率（wPCC），基于真实购买交易记录预测下一次购买的产品类别，构念和取值均不依赖人的感受或语义判断，且最终目标就是提升该客观预测性能；全文没有并列的主观或理论核心目标。存在明确的 benchmark 表述：作者在评价方法中直接使用‘we benchmark the model's performance to the proportional chance criterion’，并将该基准比较作为证明模型预测能力较默认水平显著改进的核心证据，基准参照点为理论界限 C_pro。因此同时满足客观指标唯一核心目标和明确 benchmark 两个模块，strict_include=true。
- Confidence: 0.8

## A decision support system for post-disaster interim housing

- Year/journal: 2014 / Decision Support Systems
- DOI: 10.1016/j.dss.2014.06.012
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "总加权距离（英里）", "measurement_cn": "所有家庭从被分配住房到偏好社会经济区域、所需医疗设施和所需教育设施的加权距离总和；由模型目标函数和启发式算法计算得出。", "objectivity_reason_cn": "距离是地理可测量的物理量，分配结果可由算法确定，不依赖人的感受、语义或价值判断。"}, {"name_cn": "不可行分配数", "measurement_cn": "在500个家庭中，无法找到满足住房容量或学校容量要求的家庭数；通过模拟运行统计。", "objectivity_reason_cn": "不可行性由容量约束和学校容量约束的可审计事实决定，是确定性的系统日志结果。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 作者构建一个整数规划基准模型（用CPLEX求解），在假想的500个家庭、10个住房备选场景中求得“更大利益”最优分配；随后用三种贪心启发式（GS、GL、GH）在三种住房富余水平、100种家庭顺序、10次重复（共1000次运行）下运行，报告相对于基准模型最优解的加权距离平均百分比偏差和不可行分配数。Table 1 是该基准比较的核心结果，用于选择GH作为DSS的推荐方法。
- Decision: 客观指标方面：核心结果为总加权距离和不可行分配数，均为可直接观测、用算法计算的外部事实，不涉及主观感受或语义评价；唯一核心目标是提高灾后住房分配的客观质量。benchmark方面：作者明确以“benchmark integer programming model”作为评价基准，并在第4.4节用该基准模型的CPLEX最优解来比较三种启发式的距离偏差和不可行数，比较有明确参照点，且该比较支撑了选择GH和DSS设计的核心主张。因此两个模块均通过。
- Confidence: 0.78

## A hybrid SARIMA wavelet transform method for sales forecasting

- Year/journal: 2011 / Decision Support Systems
- DOI: 10.1016/j.dss.2010.12.002
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "平均绝对百分比误差（MAPE）", "measurement_cn": "根据预测值F_i与实际销售值A_i计算：MAPE=(1/n)∑|F_i-A_i|/A_i，用于比较不同预测方法在测试期上的相对误差。", "objectivity_reason_cn": "实际销售值和预测值都是可审计的数值，误差计算不需要人的感受、语义评价或主观偏好。"}, {"name_cn": "均方误差（MSE）", "measurement_cn": "对预测误差求平方和并取平均，来自实际销售值与预测值的直接计算。", "objectivity_reason_cn": "由数值误差直接确定，完全不依赖人类主观体验。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: Time Series Data Library 中的 Monthly Australian sales of sparkling wine | Australian Bureau of Statistics 的 Monthly production of woolen yarn in Australia
- Benchmark evaluation: 在两组公开时间序列数据上分别对SARIMA、SW、CSD+LESA进行预测比较，报告MAPE、MSE和BIC；在真实时尚数据上还进一步比较SW、SARIMA、CSD+LESA、指数平滑（ES）和进化神经网络（ENN）的MAPE与运行时间。公开数据上的比较结果是论文论证SW优于CSD+LESA、并给出适用条件的重要证据。
- Decision: 核心指标是销售预测精度（MAPE/MSE），属于完全客观可测指标；全文研究问题、实验评价和结论均围绕提高预测精度展开，并进一步用这一目标指导方法选择，未发现其他并列的主观或理论核心目标。文章在评价部分明确使用两个公开时间序列数据集作为比较场地，并与SARIMA、CSD+LESA等明确参照方法进行MAPE/MSE对比，benchmark证据直接支撑核心精度提升主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.78

## A hybrid heuristic approach for attribute-oriented mining

- Year/journal: 2014 / Decision Support Systems
- DOI: 10.1016/j.dss.2013.08.012
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "广义表有趣性：KL散度与簇质量CQ/I_g^T", "measurement_cn": "KL按输出规则概率分布与均匀分布之间的散度计算；CQ/I_g^T按簇内紧度、簇间相似度和局部有趣性启发式的调和/求和公式计算，均直接由广义化输出表和概念层次结构确定。", "objectivity_reason_cn": "KL、紧度、相似度等均为确定性数学函数，不依赖任何用户评价或语义偏好；输出概率与层次结构可复核。"}, {"name_cn": "运行时间", "measurement_cn": "在同一环境（Intel Pentium Dual 2GHz, 2GB RAM）下对相同数据集的AOI和clusterAOI计时，并推导O(np)复杂度。", "objectivity_reason_cn": "运行时间和复杂度是直接可观测、可复测的客观技术指标。"}, {"name_cn": "NOT-ANY/ANY 规则比例", "measurement_cn": "统计广义化输出规则中不包含“ANY”的规则数与总规则数之比。", "objectivity_reason_cn": "规则是否出现“ANY”是输出中可直接审计的字符串/泛化层次事实，可自动计数。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: Cancer Wisconsin dataset (UCI Breast Cancer Wisconsin) | Census-income dataset1 (50K tuples) | Census-income dataset2 (200K tuples)
- Benchmark evaluation: 在Cancer Wisconsin（0.7K）、Census-income 1（50K）和Census-income 2（200K）上，以全局阈值G.Thr=1到10运行clusterAOI和AOI，报告KL、I_g^T、运行时间和ANY/NOT-ANY比例。结果显示clusterAOI在多个阈值下KL更高、CQ/I_g^T更高、运行时间更短、NOT-ANY比例更高（如G.Thr=3时clusterAOI平均100% NOT-ANY，而AOI为41%）。
- Decision: 客观指标：KL散度、簇质量I_g^T、运行时间和NOT-ANY比例均是确定性可观测指标，没有主观量表或人类语义评判。唯一核心目标：研究问题、算法设计和实验均围绕比AOI生成更有趣、更少过度泛化的广义表这一客观改进目标展开，没有并列的理论/制度/主观体验核心贡献。Benchmark：在UCI公开数据集（Cancer Wisconsin、Census-income 1/2）上以AOI为baseline、用多个阈值比较KL、I_g^T和runtime，构成命名式公开benchmark评价并直接支撑核心改进主张。因此strict_include=true。
- Confidence: 0.78

## A method for identifying market power

- Year/journal: 2013 / Decision Support Systems
- DOI: 10.1016/j.dss.2012.12.007
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "计算工作量（需检验的组合数）", "measurement_cn": "在修改的IEEE 118节点系统两个算例中，统计完整搜索与所提筛选方法需要进行的可行性检验组合数；Case 1为26289对432，Case 2完整搜索为指数级而所提方法只需7313个组合。", "objectivity_reason_cn": "组合数是确定性算法运行结果，可直接审计，不依赖人的感知、语义判断或主观偏好。"}, {"name_cn": "市场势力识别正确性（与穷举完整搜索的一致性）", "measurement_cn": "将所提方法识别出的具有市场势力的机组集合与完整搜索根据N矩阵可行性条件得到的机组集合进行比对；Case 1正确识别{Firms 10,11,12}，Case 2正确识别Firm 12及相关二/三机组组合，同时与HHI、LI、聚类算法的识别结果对比。", "objectivity_reason_cn": "正确性通过与确定性的穷举算法输出比对衡量，市场势力本身由式(11)的数学条件定义，不依赖主观评价。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: IEEE 118-bus system (modified)
- Benchmark evaluation: 在两个修改的IEEE 118节点系统算例中评价所提筛选方法，并与完整搜索、Lesieutre等聚类算法、HHI和Lerner指数比较。Case 1完整搜索发现{Firms 10,11,12}，所提方法识别出同一集合且只需432个组合，而完整搜索需要26289个组合；Case 2完整搜索发现Firm 12单独及包含Firm 12的二/三机组组合，所提方法以7313个组合正确识别；HHI和LI均未能正确筛选。
- Decision: 客观指标方面：计算组合数和识别正确性均来自确定性算法与穷举对照，不依赖主观感知、语义评价或用户体验；唯一核心目标方面：全文围绕“高效且准确识别市场势力”这一客观工程目标，不存在并列的理论贡献或主观结果作为成功标准；benchmark方面：在领域标准IEEE 118节点系统上进行了系统化评价，并与完整搜索、聚类算法、HHI/LI等明确参照点比较，benchmark结果直接支撑了核心效率提升主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.78

## Automobile insurance classification ratemaking based on telematics driving data

- Year/journal: 2019 / Decision Support Systems
- DOI: 10.1016/j.dss.2019.113156
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "风险概率预测 AUC", "measurement_cn": "基于保单期间是否发生至少一次索赔的实际事故标签，通过10折交叉验证计算的ROC曲线下面积；模型间用Delong检验比较。", "objectivity_reason_cn": "是否发生事故/索赔是可外部核验的事实标签，不依赖人的主观感受或语义判断；AUC由预测概率和实际标签计算，是确定性客观指标。"}, {"name_cn": "索赔频率预测 RMSE", "measurement_cn": "基于保单期间实际索赔次数，通过10折交叉验证计算的预测平方误差均值的平方根。", "objectivity_reason_cn": "索赔次数是可审计的客观计数事实，RMSE是确定性的预测误差度量。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在自有的2065辆投保车辆数据上，系统比较了五种风险概率模型（LR、SVM、RF、XGBoost、NN）和三类变量集（传统、驾驶行为、全部变量）及原始/分箱形式，以AUC为主要基准指标；对索赔频率模型以RMSE进行比较（表5、表8）。
- Decision: 客观指标方面，核心结果指标为基于实际事故/索赔事实的AUC和RMSE，均客观可审计；核心目标为提升预测精度，强调的可解释性未作为结果测量，不构成并列核心目标。Benchmark方面，全文在方法/结果部分明确使用benchmark model表述，以逻辑回归和传统变量/原始变量为对照，在自有数据集上系统比较不同模型、变量和分箱形式，并以AUC/RMSE比较结果支撑核心提升主张。因此两个模块均通过，strict_include为true。
- Confidence: 0.78

## Coalition formation based on marginal contributions and the Markov process

- Year/journal: 2014 / Decision Support Systems
- DOI: 10.1016/j.dss.2013.09.019
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "代理人支付/Shapley值", "measurement_cn": "由特征函数v(C)和Shapley值公式确定地计算；在零售商联盟实例中由价格折扣、数量、截止时间等公式计算。", "objectivity_reason_cn": "支付值是博弈论中的确定性数学数量，不依赖人的感受、意义理解或价值判断。"}, {"name_cn": "搜索空间规模/剪枝率", "measurement_cn": "统计算法1和算法2生成的优越联盟结构数量与全部可能联盟结构数量，报告剪枝百分比。", "objectivity_reason_cn": "联盟结构数量可枚举、可审计，属于确定性技术指标。"}, {"name_cn": "运行时间", "measurement_cn": "在固定软硬件环境（Intel i5-2410M, 4GB RAM, Windows 7, Java 1.6）下测试并取100次平均。", "objectivity_reason_cn": "运行时间是物理可测量、可复现的技术性指标。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: IDP | IP-Uniform | IP-Normal
- Benchmark evaluation: 在第6节模拟实验中，以零售商联盟情景为测试环境，将提出的算法（Algorithms 1-3）与三个基准方法IDP、IP-Uniform、IP-Normal比较运行时间；Fig. 4显示在n>22时本文方法更高效，n=25时耗时仅为IP-Uniform的32.76%。Table 3同时报告搜索空间剪枝效果，Fig. 5报告支付提升。
- Decision: 完全客观指标：核心成功指标包括支付/Shapley值、搜索空间剪枝率、运行时间，均为确定性可测量技术或博弈论数量；唯一核心目标是提出并验证提升这些客观指标的高效联盟形成方法；无主观满意度、质量评分或混合主观核心结果。Benchmark：全文在引言明确称“与三个benchmark方法比较实验评价”，且第6节实际将所提方法与IDP、IP-Uniform、IP-Normal比较运行时间，构成明确的基准比较；该比较直接支撑效率改进这一核心主张，并有明确参照点。因此同时满足两个模块。
- Confidence: 0.78

## Combining Geographical and Social Influences with Deep Learning for Personalized Point-of-Interest Recommendation

- Year/journal: 2018 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2018.1523564
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "Precision@K / Recall@K / F1@K 推荐准确率", "measurement_cn": "将模型输出的 top-K POI 推荐列表与测试集中用户真实 check-in 记录比对；precision@K=|推荐∩真实访问|/K，recall@K=|推荐∩测试集真实访问频率|/测试集总访问频率，F1@K 为二者调和平均，K=5,10,15,20,25,30。", "objectivity_reason_cn": "评价基于用户实际发生的 check-in 行为这一外部可核验事实，由确定性集合运算和测试集频率计算，不依赖任何用户、专家或研究者的主观感受、语义判断或质量评分。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在三个真实 Foursquare 数据集（纽约、布鲁克林、旧金山）上，以 Precision@K/Recall@K/F1@K 为评价指标，将所提 Semi-CDAE 与 Geo-CF、Geo-PFM、RBM 以及消融变体 Semi-DAE、CDAE 进行比较；结果显示大多数情况下所提方法相对基线提升超过10%。
- Decision: 该文以提升 POI 推荐准确率为唯一核心目标，使用 Precision/Recall/F1 等完全客观、可审计的指标，在真实 Foursquare 数据集上与多个基线和消融模型比较；讨论部分多次在评价语境中使用 benchmarks 指代基线算法，且这些比较是支撑核心提升主张的关键证据，因此通过客观指标与 benchmark 双门槛。
- Confidence: 0.78

## Deep learning based personalized recommendation with multi-view information integration

- Year/journal: 2019 / Decision Support Systems
- DOI: 10.1016/j.dss.2019.01.003
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "AUC", "measurement_cn": "在测试集上计算用户对购买/未购买商品对中，预测分数排序正确的比例；由用户历史购买记录和模型预测分数确定。", "objectivity_reason_cn": "购买记录是可审计的交易事实，AUC是确定性的排序统计量，不依赖人的主观评价或语义判断。"}, {"name_cn": "Hit Ratio@K", "measurement_cn": "统计测试用户中至少有一个真实购买商品出现在模型推荐Top-K列表中的比例；由购买记录和推荐列表确定。", "objectivity_reason_cn": "真实购买行为和推荐列表都是外部可核验事实，命中比例是确定性计算。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: Amazon.com Women's Dresses | Amazon.com Baby Clothes
- Benchmark evaluation: Deep-MINE在Amazon Women's Dresses和Baby Clothes两个公开数据集上评价产品排序推荐，主要指标为AUC和Hit Ratio；与BPRMF、CDL、VBPR、CKE基线比较，并进一步在冷启动、单视图/多视图、认知风格配置等条件下比较。4.3.4将无认知风格、统一认知风格、有序认知风格、随机认知风格、平均认知风格作为benchmark indexes与Deep-MINE比较，结果用于支持认知风格个性化提升推荐准确率的模型主张。
- Decision: 核心评价指标AUC和Hit Ratio均来自可审计的购买反馈与推荐排序，完全客观；研究问题、模型设计、实验评价和贡献声明均围绕推荐排序准确率提升，未将主观体验、理论机制或政策建议作为并列核心贡献；全文存在明确benchmark表述（4.3.4的benchmark indexes）并在Amazon公开数据集上与多个基线比较，benchmark结果支撑核心客观指标提升，因此strict_include为true。
- Confidence: 0.78

## Design of an interactive spell checker: optimizing the list of offered words

- Year/journal: 2003 / Decision Support Systems
- DOI: 10.1016/s0167-9236(02)00115-x
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "正确词在候选列表中的位置均值 (AV)", "measurement_cn": "对每个错误词m，SP/MSW97生成的候选列表L(m)中正确词w*的位置求平均；未出现计为11。", "objectivity_reason_cn": "基于预先定义的正确词w*（原文转录或受试者指认）与程序输出列表计算，是可核查的任务完成结果，不涉及主观质量评价。"}, {"name_cn": "正确词出现在候选列表中的比例 (P_A)", "measurement_cn": "统计错误词中w*出现在L(m)中的比例。", "objectivity_reason_cn": "由列表是否包含预定正确词确定，可确定性计算。"}, {"name_cn": "正确词排在首位的比例 (P_1)", "measurement_cn": "统计w*位于L(m)第一位的错误词比例。", "objectivity_reason_cn": "由排序结果与预定正确词比较确定。"}, {"name_cn": "正确词位于前五的比例 (P_5)", "measurement_cn": "统计w*位于L(m)前五位的错误词比例。", "objectivity_reason_cn": "由排序结果与预定正确词比较确定。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: MSW97 (Microsoft Word 97 spell checker)
- Benchmark evaluation: 在受试者真实打字产生的266个错误词上，将SP与MSW97的候选列表按P1、P5、PA、AV指标比较；SP在P1=0.85 vs 0.74、P5=0.98 vs 0.90、PA=1.00 vs 0.92、AV=1.36 vs 2.64上全面优于MSW97，并通过假设检验。
- Decision: 核心指标为正确词在候选列表中的命中率与平均位置，是基于预定正确词（受试者真实打字/原文转录）的可计算任务完成指标，非主观体验或语义质量评价；核心目标唯一为提升该客观拼写纠正性能。全文存在明确benchmark表述（MSW97被选为benchmark并作为比较对象），且benchmark比较结果直接支撑核心改进主张，并有明确参照点。因此两个模块均通过。
- Confidence: 0.78

## Directed disease networks to facilitate multiple-disease risk assessment modeling

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2019.113171
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "MeanAccuracy（半衰期加权命中准确率）", "measurement_cn": "以患者下一次住院的实际 ICD-10 诊断疾病组作为真实标签，对推荐列表按位置加权（2^{-k/c}）计算命中分数，再对所有测试患者求平均。", "objectivity_reason_cn": "真实标签是医院病历中记录的疾病诊断事实，不依赖人的感受、语义评价或价值判断；计算结果完全由确定性匹配逻辑决定。"}, {"name_cn": "Ratio1Score（完全命中比例）", "measurement_cn": "推荐列表与真实标签完全匹配（标准化半衰期准确率为1）的患者占测试集的比例。", "objectivity_reason_cn": "基于可审计的疾病诊断事实进行匹配，是客观可计算的预测性能指标。"}, {"name_cn": "Precision / Recall / F1 Score", "measurement_cn": "在推荐长度 Q=10 下，根据预测推荐疾病组与实际下次就诊疾病组计算精确率、召回率和 F1。", "objectivity_reason_cn": "这些指标完全由外部病历标签和预测列表的集合运算决定，不涉及主观体验或语义质量判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在两个独立医院数据集（Dataset A′、Dataset B′）以及合并数据集上，使用 10 折交叉验证，将所提 ADTLM 与 CF、KNN、DT、SPM 四种基准方法比较，报告 MeanAccuracy、Ratio1Score、Precision、Recall、F1 五个客观指标；Tables 6-8 显示 ADTLM 在这些指标上均高于各基准方法。
- Decision: 该文以提升多疾病风险预测的客观性能指标作为唯一核心目标：预测目标是患者下次住院的真实 ICD 疾病诊断，评价指标均为可计算的准确性/精确率/召回率/F1，无主观量表或语义评价。同时，文章在评价部分明确将 CF 称为 classic benchmark method，并通过 Tables 6-8 将 ADTLM 与 CF、KNN、DT、SPM 等明确参照对象比较，报告客观指标提升；该 benchmark 对比直接支撑核心提升主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.78

## Effective demand response for smart grids: Evidence from a real-world pilot

- Year/journal: 2016 / Decision Support Systems
- DOI: 10.1016/j.dss.2016.07.007
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "平均峰值降低率", "measurement_cn": "基于智能电表采集的基线负荷数据，通过蒙特卡洛模拟消费者在TOU电价下的负荷曲线，计算模拟后相对基线的峰值变化百分比。", "objectivity_reason_cn": "峰值是电网负荷的可审计物理量，完全由计量数据确定，不依赖人的感受或语义判断。"}, {"name_cn": "电费节省率", "measurement_cn": "根据模拟优化后的分时用电量与相应电价计算电费，并与基线（不改变用电行为）电费比较得到节省百分比。", "objectivity_reason_cn": "电费是交易性金额，由用电量和电价客观计算，不依赖主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: Gottwalt et al. (2011) variable pricing | Di Giorgio & Pimpinella (2012) two-tier TOU tariff | Di Giorgio & Pimpinella (2012) three-tier TOU tariff | Doostizadeh & Ghasemi (2012) winter variable tariff | Doostizadeh & Ghasemi (2012) summer variable tariff
- Benchmark evaluation: 在第4.4节中，作者将文献中多个基准电价方案（Gottwalt等、Di Giorgio & Pimpinella、Doostizadeh & Ghasemi）应用于相同的数据和模拟框架，报告平均峰值降低率和电费节省率，并通过图表展示所提出的TOU方案在这些客观指标上整体优于文献基准，用以支撑核心改进主张。
- Decision: 客观指标方面：核心成功指标为平均峰值降低率和电费节省率，均来自智能电表数据和模拟计算，属于完全客观的可测量结果，且全文核心目标为设计有效DR方案以提升这些指标；未发现与客观指标提升并列的主观或理论核心贡献。Benchmark方面：第4.4节明确使用'benchmarks'一词进行系统性比较，比较对象为文献中的多个电价方案，位于评价语境并直接支撑所提方案在峰值降低和成本节省上的改进主张，且有明确参照点。因此严格包含。
- Confidence: 0.78

## Family profile mining in retailing

- Year/journal: 2019 / Decision Support Systems
- DOI: 10.1016/j.dss.2019.01.007
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "目标家庭画像标签预测召回率（recall rate）", "measurement_cn": "在购买确定特征（definite features）至少两次的可靠正例验证集上，使用五次五折交叉验证计算被分类器召回的比率；也使用召回提升率（相对随机预测）进行展示。", "objectivity_reason_cn": "家庭画像标签（是否有婴儿、儿童、老人、汽车）属于外部可核验的人口统计事实；召回率由交易日志和固定编码规则计算，不依赖用户主观评价。"}, {"name_cn": "产品推荐预测误差与覆盖率（MAE / RMSE / coverage）", "measurement_cn": "将消费金额按分位数转换为1—5评分后，使用协同过滤预测新会员在画像相关品类上的评分，计算MAE、RMSE和覆盖率，并与全局邻居选择对比。", "objectivity_reason_cn": "评分由购买金额分位数转换而来，预测结果与实际购买金额均为交易数据中的客观可审计事实，不涉及主观感受或语义偏好判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在自有的大型超市交易数据（50,000名会员）上，将提出的DFBN算法与AFRN、AFBN、RFBN三个对比算法在infant、child、elder、car四个画像上比较平均召回率；结果显示DFBN在平均召回率上分别提升17.18%、11.34%和21.86%。推荐实验部分又将全局邻居选择作为比较基准，报告MAE、RMSE和覆盖率的改进。
- Decision: 客观指标方面，核心指标为家庭画像预测召回率和推荐MAE/RMSE/coverage，均是基于交易数据固定规则计算的外部事实性指标，无主观量表或语义评价。核心目标方面，研究问题、设计目标、评价结构和贡献声明均围绕算法在客观指标上的提升，未并列理论机制或主观结果作为成功标准。benchmark方面，作者在4.3节明确将四个对比算法称为benchmarks，并在自有大型数据集上系统比较，结果显示DFBN在召回率上有明显提升，该基准评价直接支撑核心改进主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.78

## From Lurkers to Workers: Predicting Voluntary Contribution and Community Welfare

- Year/journal: 2020 / Information Systems Research
- DOI: 10.1287/isre.2019.0905
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "个体用户贡献类型预测的AUC（Lurk/Append/Respond/Ask/Share）", "measurement_cn": "在DiabetesForum的周级用户行为序列上训练HMM-AFT，使用10折交叉验证计算每个贡献类别的AUC；AUC基于预测概率与真实行为标签（创建主题、回复、追加、沉默）比较得出", "objectivity_reason_cn": "标签来自平台日志的可观察动作及LDA对主题内容的自动分类；不是人类对质量或价值的评分，预测性能可被任何审阅者按相同数据复现"}, {"name_cn": "社区福利八个维度（W1-W8）预测的RMSE", "measurement_cn": "根据月度时间序列，用多种回归模型（SVR/ARIMAX/kNN/LSTM/XGBoost）预测未来12个月的W1-W8（新主题数、响应数、响应/主题、唯一用户/主题、互惠帖、新用户数、新贡献者数、新用户贡献比例），计算RMSE并与基线比较", "objectivity_reason_cn": "W1-W8均为社区活动计数或比例，来自数据库可审计的记录；RMSE是预测值与实际日志值的确定性误差度量"}, {"name_cn": "模拟干预带来的用户贡献增加（响应数和主题数增加百分比）", "measurement_cn": "基于HMM-AFT预测关键福利下降期，模拟对可动员潜水者（状态s3）或随机用户按预算投放干预，重复100次，计算贡献量增加的平均百分比", "objectivity_reason_cn": "贡献量来自平台日志计数，干预效果以可计算的帖子和响应数量变化衡量，不依赖人类主观评价"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在DiabetesForum数据集上，将HMM-AFT与No state variables、Dynamic HMM（Chen et al. 2018）、Dynamic network（Tagarelli and Interdonato 2014）、逻辑回归、随机森林、XGBoost、LSTM等基线比较；图7报告个体贡献预测的10折交叉验证AUC提升，图8报告福利预测相对'No state variables'的RMSE改进，表4报告识别最严重福利下降时段的实际排名（HMM-AFT排名第2，基线最差58）。附加五个社区（附录D）支持泛化性。
- Decision: 文章以HMM-AFT预测模型为核心，核心成功指标是用户贡献类型预测AUC、社区福利8个维度的RMSE预测误差以及模拟干预下贡献量提升，均为平台行为日志可计算的客观结果；全文没有主观量表或人类语义质量评价作为成功标准。文中在结果部分明确以'benchmark'动词陈述对多个基线的系统化比较（5.3.1和5.3.2），比较结果为核心客观提升主张提供直接证据，且有明确对照（No state variables、动态HMM、动态网络、静态分类器、LSTM）。因此两个模块均满足纳入标准。
- Confidence: 0.78

## Histogram distance-based Bayesian Network structure learning: A supervised classification specific approach

- Year/journal: 2009 / Decision Support Systems
- DOI: 10.1016/j.dss.2009.07.010
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "分类准确率（validated classification accuracy）", "measurement_cn": "在 UCI 数据集上使用 10 折交叉验证计算被正确分类案例的比例，报告于表 4 和表 6。", "objectivity_reason_cn": "以数据集中固定的类别标签为事实基准，预测是否正确可由计算唯一确定，不依赖人的感受、偏好或语义质量判断。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: UCI Machine Learning Repository（UCI 数据集：Breast、Cars、Cleveland、Diabetes、Glass、Iris、Vehicle、Vote 等）
- Benchmark evaluation: 在 UCI 数据集的 14+11 个标准分类任务上，用 K2 和 B 结构学习算法配合不同度量，报告 10 折交叉验证分类准确率；核心结果是 Jeff 度量在 11 个数据库中有 7 个优于 K2，25 个数据库总体 15:10 优于 K2。
- Decision: 核心成功指标是 UCI 标准分类数据集上的 10 折交叉验证分类准确率，属于固定事实标签上的客观性能；全文研究问题、实验设计和贡献声明均围绕分类准确率/分类能力提升展开，无主观或并列核心目标。评价场地明确命名为 UCI Machine Learning Repository，并有 K2、Naive Bayes、其他距离度量等明确参照点，benchmark 结果直接支持新度量分类性能更优的核心主张。
- Confidence: 0.78

## Knowledge discovery by inspection

- Year/journal: 1997 / Decision Support Systems
- DOI: 10.1016/s0167-9236(97)00012-2
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "规则发现完整性", "measurement_cn": "统计 INSPECT 在 contact lens、congressional voting records、汽车等数据集上发现的规则数占所有可能规则的比例；Theorem 2 保证在二类情况下发现所有一条件和二条件规则。", "objectivity_reason_cn": "规则集合及其条件数可由数据和算法确定，规则数的计数不依赖人的感受、语义判断或价值评价。"}, {"name_cn": "规则支持度", "measurement_cn": "计算每条规则所支持的数据实例数或平均支持数，并与完整规则集的平均支持数比较。", "objectivity_reason_cn": "支持数是对实例集合基数的计数，来自确定性数据表和集合运算，客观可审计。"}, {"name_cn": "算法复杂度/效率", "measurement_cn": "分析 INSPECT 的最坏情况复杂度，并在特定条件下与 ITRULE 的复杂度比较。", "objectivity_reason_cn": "复杂度是数学推导结果，完全客观，不依赖人类参与者的体验或偏好。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: contact lens data | congressional voting records data set | [6] 中的汽车数据（auto data）
- Benchmark evaluation: 在 contact lens 数据上，INSPECT 仅漏掉 9 条可能规则中的 3 条，发现规则平均支持 3.7，完整规则集平均支持 3.3；在 congressional voting records 数据上，二类情况下发现全部 211 条二条件规则；在汽车数据上，发现超过 60% 的所有可能规则，平均支持 2.32，完整规则集平均支持 2.33。
- Decision: 文章核心是提出并验证 INSPECT 规则发现算法，其核心结果指标——规则完整性、规则支持度和算法复杂度——均为客观可测量、可审计的值；全文没有以用户感知、满意度或语义质量评分作为核心成功标准。benchmark 门槛方面，虽然未使用字面‘benchmark’一词，但作者在实验部分明确将算法应用于 contact lens、congressional voting records 和汽车数据集等公开/领域标准数据集，并与完整规则集等理论界限进行比较，属于命名式 benchmark 评价，且该评价直接支撑了核心发现能力和完整性主张。因此客观指标门槛与 benchmark 门槛均通过，strict_include=true。
- Confidence: 0.78

## Privacy Protection in Data Mining: A Perturbation Approach for Categorical Data

- Year/journal: 2006 / Information Systems Research
- DOI: 10.1287/isre.1060.0095
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "分类错误率", "measurement_cn": "每个数据集约70%作训练/扰动集，30%未扰动测试集；用C4.5在扰动后的训练集上建模，在未扰动测试集上计算分类错误率（Table 4）。", "objectivity_reason_cn": "分类错误率由预测类别与数据中的事实类别标签比较得到，不依赖人的感受、语义价值或质量判断；类别标签是客观事实类别。"}, {"name_cn": "汇总统计错误率", "measurement_cn": "按式(18)计算机密属性各类别频数在原数据与扰动数据之间的平均绝对相对误差。", "objectivity_reason_cn": "频率计数是可直接计算、可审计的数量，不涉及任何主观评价。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: UCI Census (Adult) dataset | UCI Contraceptive Method Choice (CMC) dataset
- Benchmark evaluation: 在Offer、Census和CMC三个数据集上，作者将随机扰动、Reiss(1984) 2阶交换、Reiss(1984) 3阶交换与提出方法在同一隐私参数下比较，报告分类错误率和汇总统计错误率；Table 4及Figures 1-2显示提出方法在所有数据集和多种扰动比例下均优于对比方法。
- Decision: 客观指标：核心评价指标为C4.5分类错误率和汇总统计错误率，均为客观可计算、不依赖人类语义评价的指标；研究问题、设计目标与评价结构均围绕在满足隐私约束下提高数据效用，无主观量表或并列理论贡献。Benchmark：论文虽未使用'benchmark'一词，但在UCI Census(Adult)和UCI CMC等公开标准数据集上进行评价，并与Original、Random、Reiss 2阶/3阶方法比较；Table 4和Figures 1-2直接支撑核心提升主张，属于命名式公开benchmark中心评价。两项门槛均通过，因此strict_include=true。
- Confidence: 0.78

## A Query-Driven Approach to the Design and Management of Flexible Database Systems

- Year/journal: 2002 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2002.11045739
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "查询处理时间（及衍生的PER/APT/MAD/MPD）", "measurement_cn": "在Access与Oracle实验环境中运行查询，由系统记录每个查询在候选数据库结构上的处理时间，排除显示时间；再计算处理效率率、平均处理时间、绝对偏差、百分比偏差，并进行t检验/ANOVA。", "objectivity_reason_cn": "处理时间是数据库系统日志可观测的物理时间，不依赖人的感受或语义评价；效率率、偏差均由该时间数据按固定公式推导。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在实验I和实验II中，作者将'实际最优分配'作为top benchmark（理论上限），在验证查询集上系统比较了归纳学习产生式规则、决策树、神经网络、粗略规则、最佳单结构和最差单结构；报告PER、APT、MAD、MPD并做统计检验。该benchmark表（表5/表8）与最佳单结构/最差单结构对照，直接支撑'灵活分配优于单一固定结构'的客观性能提升主张。
- Decision: 客观指标方面：核心成功指标是查询处理时间和由时间衍生的效率率/偏差，均为系统可观测物理量，全文没有主观量表或人类语义评价。唯一核心目标是提升只读查询处理性能，实验、成本分析和贡献声明均围绕该目标。Benchmark方面：虽然没有使用公开命名的benchmark套件，但作者在实验评价部分明确使用benchmark概念，以'实际最优分配'作为top benchmark，并与多个明确参照点（最佳单结构、最差单结构、rough rules、学习模型）比较；benchmark表直接佐证核心性能提升主张，满足benchmark_comparison_central条件。因此strict_include=true。
- Confidence: 0.75

## Circuit diagnosis support system for electronics assembly operations

- Year/journal: 1999 / Decision Support Systems
- DOI: 10.1016/s0167-9236(99)00015-9
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "平均每板诊断时间", "measurement_cn": "在实际电子装配环境中，手动诊断约25分钟/板，使用CDSS辅助后约10分钟/板；作者说明这是对随机样本板的非正式观察估算。", "objectivity_reason_cn": "诊断时间是可直接审计的物理时间量，不依赖人的感受、语义评价或价值判断。"}, {"name_cn": "平均诊断所需测试次数", "measurement_cn": "在随机生成的问题实例模拟中，分别记录动态规则D1-D3、静态规则S1和随机规则R的平均测试次数，见Table 4。", "objectivity_reason_cn": "测试次数是模拟器中的程序计数，属于可复现的系统日志型客观指标。"}, {"name_cn": "缺陷覆盖率", "measurement_cn": "在5周试用期内，每周使用当前案例库正确诊断的缺陷比例；第1周约17%，第3周达85%，第5周达90%。", "objectivity_reason_cn": "覆盖率基于实际缺陷能否被案例库正确匹配，真实缺陷可由修复后功能测试等外部事实确认，不是用户评分或主观判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在多个随机生成的电路诊断问题场景中，将三种动态测试选择规则D1-D3和一种静态规则S1与随机选择规则R进行比较，评价指标是平均诊断所需测试次数。结果显示动态规则相对随机测试平均减少约50%的测试次数，相对静态规则平均减少约41%。
- Decision: 客观指标方面，核心成功指标为诊断时间、测试次数和缺陷覆盖率，均为可审计的客观事实/计数，不涉及主观满意度、语义质量评分或专家偏好；唯一核心目标是提升电路诊断的有效性与效率，管理建议和用户反馈不是并列的核心贡献。Benchmark方面，Section 4.2明确以随机选择规则作为‘benchmark for comparison’，在评价语境中比较不同测试排序规则的平均测试次数，且结果用于支持核心的测试次数降低主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.75

## Fused latent models for assessing product return propensity in online commerce

- Year/journal: 2016 / Decision Support Systems
- DOI: 10.1016/j.dss.2016.08.002
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "退货倾向（return propensity）", "measurement_cn": "客户-产品对的历史退货次数/购买次数，来自订单和退货/退款记录；在测试集上用预测值与观测值比较。", "objectivity_reason_cn": "退货行为和购买行为是系统记录的可审计事实，退货倾向由这些事实的频次比例确定，不依赖人的感受、语义评价或偏好判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在真实在线零售数据集上评价 FRPLM，并与 PMF、NMF、基于用户频率、基于商品频率的方法以及未融合特征的 RPLM 比较；FRPLM 在 Precision@N、Recall@N、ROC/AUC 等指标上优于基线。
- Decision: 核心构念为基于订单/退货日志计算的退货倾向，属于可审计事实标签，评价指标全部客观；研究目标与贡献声明均围绕提升该预测性能展开，无主观体验或理论机制作为并列核心。benchmark 方面，虽然未命名公开数据集，但作者在结论中明确使用 benchmark methods 指称系统化基线比较，且第6.3-6.5节提供了与多个基线的客观指标对照，该比较直接支撑核心性能提升主张。因此两个模块均通过。
- Confidence: 0.75

## Modeling brand post popularity dynamics in online social networks

- Year/journal: 2014 / Decision Support Systems
- DOI: 10.1016/j.dss.2014.05.003
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "模型拟合优度（AIC值）", "measurement_cn": "基于Twitter品牌帖子的用户活动事件数据（转推、回复、收藏计数），使用最大似然估计拟合模型，计算Akaike信息准则（AIC）值；AIC越低表示模型拟合越好。", "objectivity_reason_cn": "事件计数来自Twitter公开API，具有时间戳和关注者数；AIC由数据和模型公式确定，不依赖人的感受或语义判断。"}, {"name_cn": "品牌帖子受欢迎程度（事件计数）", "measurement_cn": "品牌推文在生命周期内获得的转推、回复、收藏总数，作为受欢迎程度的操作化代理指标，由Twitter活动日志直接获得。", "objectivity_reason_cn": "受欢迎程度虽在概念上主观，但本文操作化为可核验的事件计数，是外部可观察事实。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在自收集的Twitter品牌帖子数据集（221个高互动帖子，125,861条活动）上，以 homogeneous Poisson process 和 ARIMA time series model 作为显式命名的 benchmark 模型，与 self-exciting Hawkes 和 ETAS 候选模型比较平均AIC；结果显示ETAS模型平均AIC最低（6415.187 vs 7143.110 vs 9047.397 vs 13398.661），用于支持ETAS优于基准模型的核心主张。
- Decision: 客观指标方面：核心成功指标为模型拟合优度（AIC），基于Twitter活动事件日志，完全客观且不依赖人的语义判断；受欢迎程度被操作化为可观测事件计数；全文无主观量表，核心目标是提出并验证AIC更优的二维点过程模型。Benchmark方面：作者在方法/结果部分明确将 homogeneous Poisson process 和 ARIMA 命名为 benchmark 模型，并在自建数据集上通过AIC比较支持核心主张；有明确参照点。因此满足两个条件，strict_include=true。
- Confidence: 0.75

## Who Is the Next “Wolf of Wall Street”? Detection of Financial Intermediary Misconduct

- Year/journal: 2020 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00633
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "分类准确率（Accuracy）", "measurement_cn": "基于金融中介是否发生不当行为的监管记录标签（FINRA BrokerCheck最终客户投诉和监管行动）与分类器预测结果构建混淆矩阵计算", "objectivity_reason_cn": "不当行为标签是监管机构确认的客观事实记录，不依赖人的感受或语义评价"}, {"name_cn": "召回率（Recall）", "measurement_cn": "真正例数除以真正例与假负例之和，即实际发生不当行为的中介被正确识别的比例", "objectivity_reason_cn": "基于事实标签计算，客观可审计"}, {"name_cn": "精确率（Precision）", "measurement_cn": "真正例数除以真正例与假正例之和，即被预测为不当行为的中介中实际发生不当行为的比例", "objectivity_reason_cn": "基于事实标签计算，客观可审计"}, {"name_cn": "F1分数", "measurement_cn": "精确率和召回率的调和平均", "objectivity_reason_cn": "由客观分类指标推导，客观"}, {"name_cn": "AUC（ROC曲线下面积）", "measurement_cn": "基于不同分类阈值下真正例率和假正例率计算", "objectivity_reason_cn": "基于事实标签的客观分类性能度量"}, {"name_cn": "经济收益（Economic gain）", "measurement_cn": "基于实际赔偿金额（compensation payment）和罚款计算的平均经济收益，排除搜索成本或进行敏感性分析", "objectivity_reason_cn": "基于可审计的监管记录金额，客观可核验"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在自然分布测试样本（N=2051，6.87%不当行为）上，将结合监管确认信息的分类器（C和D）与仅含自我披露信息/用户确认信息的基准分类器（A和B）进行性能比较。结果显示C和D在绝大多数机器学习方法和指标上显著优于A和B（如表11中多项p<0.01），证明监管确认信息显著提升检测性能（支撑H3）。此外，各分类器还与naive随机分类基线比较，证明自我披露信息本身有检测价值（支撑H1）。
- Decision: 客观指标方面：核心结果是检测金融中介不当行为的分类性能（accuracy、recall、precision、F1、AUC）及基于实际赔偿金额的经济收益，标签来自FINRA BrokerCheck的最终客户投诉和监管行动记录，属于可脱离人的感受和语义评价而成立的事实标签（objective_fixed_factual_labels）。核心目标唯一：研究问题、评价结构和贡献声明均围绕自动检测分类器的构建与性能提升；信息操纵理论和保证理论作为特征选择依据，其确认通过分类性能实现，是解释性而非并列核心贡献。Benchmark方面：全文在评价语境中存在明确的benchmark标识——Table 11和Table D5标题明确将Classifier A和B（及E/F）命名为'Benchmarks'并进行McNemar检验，该比较结果正是证明结合监管确认信息的分类器性能提升的关键证据，且存在明确参照点。因此两项门槛均通过，strict_include=true。
- Confidence: 0.75

## Detecting and forecasting economic regimes in multi-agent automated exchanges

- Year/journal: 2009 / Decision Support Systems
- DOI: 10.1016/j.dss.2009.05.012
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "经济制度转移预测成功率", "measurement_cn": "在TAC SCM 2005的6场测试游戏中，从第1天到第199天每天预测未来20天的主导制度，并与离线使用全量游戏数据计算出的真实制度逐日比较，统计预测正确的次数比例（Fig. 13）。", "objectivity_reason_cn": "真实制度由游戏日志中的价格、库存、供需比例等可审计数据经确定算法计算，预测正确性按离散匹配规则判定，不依赖人的感受、语义评价或质量判断。"}, {"name_cn": "制度概率分布的KL散度", "measurement_cn": "计算Markov预测和指数平滑预测的制度概率分布与真实制度概率分布之间的KL散度（式21，Fig. 14），以比特为单位衡量预测分布与真实分布的差距。", "objectivity_reason_cn": "概率分布和KL散度均由公式和日志数据计算，值是确定性的，不含主观评分或偏好。"}, {"name_cn": "价格分布预测误差", "measurement_cn": "从学习到的GMM中进行蒙特卡洛抽样，与真实游戏数据的价格经验直方图比较，用1-范数距离作为预测误差（Fig. 15，Table 2）。", "objectivity_reason_cn": "价格直方图和1-范数误差均由交易数据计算，属于可审计的统计指标，不涉及人类理解或价值判断。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: TAC SCM 2005 (Trading Agent Competition for Supply Chain Management)
- Benchmark evaluation: 在TAC SCM 2005半决赛/决赛的24场游戏（18场训练、6场测试）上，对低、中、高三个市场分别应用GMM学习制度，在线识别每日主导制度并预测未来至多20天的制度转移；报告制度转移预测成功率、制度概率分布KL散度以及价格分布预测误差。
- Decision: 客观指标方面，核心评价指标为制度转移预测成功率、制度概率分布KL散度和价格分布预测误差，三者均由TAC SCM游戏日志中的价格、库存、供需等客观数据按确定公式计算，不依赖人类感受或语义判断；研究问题、设计目标和贡献声明均围绕“检测并预测经济制度”展开，提升预测准确性是唯一核心目标。Benchmark方面，TAC SCM 2005是公开的多智能体供应链管理标准竞赛任务，本文在第5-6节将其作为核心评价场地，并与真实制度、Markov/指数平滑预测方法以及不同GMM配置进行比较，结果直接支撑制度预测性能的核心主张。因此满足两个模块要求，strict_include=true。
- Confidence: 0.74

## Shopbot 2.0: Integrating recommendations and promotions with comparison shopping

- Year/journal: 2008 / Decision Support Systems
- DOI: 10.1016/j.dss.2008.05.006
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "推荐组合的节省金额（美元）", "measurement_cn": "对每本图书，计算推荐捆绑中图书的标价总和与实际订单成本（含运费、优惠券、免邮等）之差；与当前最佳推荐基准比较，报告平均节省、最高/最低节省及统计显著性。", "objectivity_reason_cn": "价格、运费、优惠券金额均为公开可核验的数字，节省额由明确公式计算，不依赖人的感受、语义评价或偏好。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在Amazon.com（87本书样本）和Buy.com（46本样本）上，以当前最佳推荐作为基准，求解整数规划模型得到Our RS；Amazon平均节省16.23美元对基准12.19美元（高33%），Buy.com为21.45美元对15.67美元（高37%），均p<.001。
- Decision: 全文的核心结果是可核验的金钱节省额，属于完全客观指标；模型设计、评价和贡献声明均围绕提升购物者节省额展开，无主观量表或并列核心目标。第3.4节明确使用‘benchmark savings’作为当前最佳推荐基线，将模型结果与之比较并报告显著提升，构成支撑核心主张的benchmark评价。因此两个模块均通过，strict_include为true。
- Confidence: 0.74

## A stochastic, contingency-based security-constrained optimal power flow for the procurement of energy and distributed reserve

- Year/journal: 2013 / Decision Support Systems
- DOI: 10.1016/j.dss.2013.04.006
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "总供电成本（generation, reserves and load shedding total cost）", "measurement_cn": "在IEEE 30-bus和118-bus测试系统上运行所提出的随机安全约束最优潮流（SOPF）与固定备用裕量方法，计算发电、备用和切负荷的总期望成本。", "objectivity_reason_cn": "成本以美元计，由系统仿真中的经济参数和物理调度结果直接计算，不依赖人的感受、语义评价或主观偏好。"}, {"name_cn": "备用分配量（reserve allocation）", "measurement_cn": "在相同测试系统和条件下，比较SOPF内生产出的最优备用分配量与固定备用裕量方法分配的备用MW。", "objectivity_reason_cn": "备用容量是电力系统调度中的物理量（MW），由模型输出直接读取，客观可核实。"}, {"name_cn": "切负荷量（load shedding MW）", "measurement_cn": "在IEEE 30-bus和118-bus系统的各预设事故场景中，比较SOPF与固定备用裕量方法所需的切负荷MW。", "objectivity_reason_cn": "切负荷是负荷损失量，以MW计，由系统仿真模型确定，不涉及主观评价。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: IEEE 30-bus system | IEEE 118-bus system
- Benchmark evaluation: 在IEEE 30-bus（6台发电机，12个事故场景）和IEEE 118-bus（54台发电机，12个事故场景）标准测试系统上，对提出的SOPF模型进行数值仿真，与传统的固定备用裕量方法比较备用分配、切负荷量和总供电成本，结果显示SOPF可避免切负荷并降低总成本。
- Decision: 客观指标方面：核心成功指标为总供电成本、备用分配量、切负荷量，均为可审计的物理/经济指标，不依赖人类主观评价，且客观指标提升是文章唯一的核心目标和贡献。Benchmark方面：文章在公开的IEEE 30-bus和118-bus标准测试系统上进行了数值比较，并与传统的固定备用裕量方法进行明确对比，证明SOPF在成本、备用分配和切负荷上的改进，该benchmark评价直接支撑核心改进主张。因此满足两个模块的通过条件，strict_include为true。
- Confidence: 0.72

## An agent for selecting optimal order set in EC marketplace

- Year/journal: 2004 / Decision Support Systems
- DOI: 10.1016/s0167-9236(03)00027-7
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "利润", "measurement_cn": "由选择变量 O_i 与订单利润 p_i 乘积求和，即 MAX Σ p_i O_i，是整数规划的目标函数，结果来自模型计算。", "objectivity_reason_cn": "利润是客观的经济数值，可由订单价格和成本直接计算，不依赖人类感受或语义评价。"}, {"name_cn": "完工时间（makespan）", "measurement_cn": "所有订单最后完工时间 F_max，由调度模型计算，并在 MT6×6 问题中与已知最优值比较。", "objectivity_reason_cn": "完工时间是物理生产事实，由机器操作时序决定，可外部核验。"}, {"name_cn": "交货期满足度", "measurement_cn": "每个订单的完成时间与 due date 比较，是否满足截止日期，案例研究中以 ○/× 标记。", "objectivity_reason_cn": "是否在截止日期前完成是可审计的事实，不涉及主观判断。"}, {"name_cn": "计算时间", "measurement_cn": "案例研究报告中 GA 模块的计算时间（秒），如 46s、98s、164s。", "objectivity_reason_cn": "计算时间是可测量的技术性能指标，客观直接。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: MT6×6 (Muth and Thompson's job shop scheduling benchmark)
- Benchmark evaluation: 使用MT6×6 job shop scheduling benchmark测试IP模型，得到makespan=55，等于该benchmark的已知最优解；随后GA也在同一benchmark上得到最优解，并在更大benchmark问题上也获得最优解。该benchmark评价用于验证选择代理核心调度算法的正确性和有效性。
- Decision: 客观指标方面：核心成功标准是利润最大化、交货期满足与完工时间，均为客观可验证的经济/物理指标，无主观评价。唯一核心目标：研究问题、模型目标、案例评价和贡献声明均围绕选择最优订单集以最大化利润展开，无并列的主观、理论或政策目标。Benchmark方面：全文明确使用MT6×6这一公开的job shop scheduling benchmark，并报告达到已知最优makespan 55，且GA在更大benchmark上也得到最优解；benchmark结果用于验证选择代理核心调度算法的有效性，支撑核心提升主张。因此strict_include为true。
- Confidence: 0.72

## Data-driven Process Prioritization in Process Networks

- Year/journal: 2017 / Decision Support Systems
- DOI: 10.1016/j.dss.2017.02.011
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "总机会成本（Total Opportunity Costs）", "measurement_cn": "由预测的聚合绩效差异和表现阈值计算各期机会成本，再通过混合整数线性规划最小化总机会成本；表3给出D2P2、PPR、CPIM的总机会成本分别为0、12,441、0。", "objectivity_reason_cn": "机会成本是欧元货币值，由日志推导的现金流分布、阈值和优化模型计算，不依赖人的感受或语义评价；虽然包含模型假设，但数值确定且可复核。"}, {"name_cn": "深度分析排程/优先级列表（priority list）", "measurement_cn": "D2P2返回各流程应接受下次深度分析的未来期间；表3对比D2P2、PPR、CPIM在1至6期的安排结果。", "objectivity_reason_cn": "排程是优化模型输出的离散决策，由日志数据和预设参数确定，不是主观评分或偏好判断。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: 2012 BPI Challenge log
- Benchmark evaluation: 将D2P2原型应用于经层次挖掘和现金流失真处理的2012 BPI Challenge log，建立包含4个流程的过程网络，运行10,000次Monte Carlo模拟并求解MILP；在相同案例上运行PPR和CPIM，比较排程结果和总机会成本。结果显示D2P2排程为P2(1期)、P1(2期)、P3(4期)，总机会成本为0；PPR总机会成本为12,441；CPIM排程大致相同但多排P4，D2P2更节省分析容量。
- Decision: 全文以日志驱动的D2P2流程优先排序方法设计为核心，以最小化总机会成本和生成合理排程为客观成功指标；第4.4.4节明确将真实案例称为benchmark，并与PPR、CPIM比较，表3给出客观比较结果；未发现主观核心指标或与客观指标提升并列的理论贡献，因此同时满足客观指标、唯一核心目标和明确benchmark三个门槛，strict_include=true。
- Confidence: 0.72

## Distribution forecasting of high frequency time series

- Year/journal: 2004 / Decision Support Systems
- DOI: 10.1016/s0167-9236(03)00083-6
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "方向准确率 (ADA)", "measurement_cn": "在留出测试集上，比较预测的价格方向与实际价格方向的正确百分比", "objectivity_reason_cn": "基于实际市场价格数据，方向比较是客观可计算事实，不涉及人类评价"}, {"name_cn": "泰尔U统计量 (Theil's U)", "measurement_cn": "预测均方根误差与无变化预测的均方根误差之比", "objectivity_reason_cn": "由价格数据计算，客观可比，低于1表示优于无变化预测"}, {"name_cn": "模拟交易利润", "measurement_cn": "基于预测信号采用简单交易策略，以初始100美元计算最终价值", "objectivity_reason_cn": "交易规则明确，基于价格数据计算；虽然假设无交易成本，但结果是可审计的客观数值"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 使用日元/美元高频数据集（100,000和200,000个点），AURA-FS在多种参数组合下计算ADA、Theil's U和模拟利润；与naive forecast（前一方向）的ADA 46.2%比较，最好的ADA为56.9%，最好的Theil's U为0.892（<1优于无变化预测）。
- Decision: 客观指标方面：ADA、Theil's U和模拟利润均基于实际价格数据，可确定性计算，不依赖人类感知或语义评价，全部核心成功结果为客观。核心目标方面：全文围绕提升预测准确性和利润这一唯一核心目标展开，没有并列的主观体验、理论机制或政策建议等核心贡献。benchmark方面：作者在评价语境中明确使用'benchmark'一词，提供naive forecast作为ADA的参照点，并以此证明AURA-FS的改进（46.2% vs 56.9%），Theil's U本身也与no-change forecast比较，符合benchmark_comparison_central。因此两个模块均通过，strict_include=true。
- Confidence: 0.72

## Estimating the effect of word of mouth on churn and cross-buying in the mobile phone market with Markov logic networks

- Year/journal: 2011 / Decision Support Systems
- DOI: 10.1016/j.dss.2011.01.002
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "流失预测的准确率（Accuracy）", "measurement_cn": "在留出的测试集上，比较预测流失/非流失与运营商记录的真实合同解约状态；准确率=(TP+TN)/(TP+FN+TN+FP)。", "objectivity_reason_cn": "考核的是客户是否实际发出解约通知且合同最终停用，来自公司日志的可审计事实，不依赖人的主观评价。"}, {"name_cn": "流失预测的敏感度/召回率（Sensitivity）", "measurement_cn": "测试集中真实流失客户中被正确识别为流失的比例，TP/(TP+FN)，并比较加入邻域信息后的提升（如T2.1较T1敏感度由34.7%提升至54.37%）。", "objectivity_reason_cn": "基于真实流失标签与模型预测的确定性计数，客观可复核。"}, {"name_cn": "流失预测的特异度与精确率", "measurement_cn": "测试集上TN/(TN+FP)、TP/(TP+FP)，来自混淆矩阵的客观计数。", "objectivity_reason_cn": "均为预测标签与事实标签的确定性匹配结果。"}, {"name_cn": "游戏下载（交叉购买）预测的准确率与敏感度", "measurement_cn": "客户是否通过HTTP/WAP下载游戏作为事实标签，测试集上Accuracy/Sensitivity等指标（如T2.1 Accuracy 69.72% vs T1 61.06%）。", "objectivity_reason_cn": "游戏下载行为来自运营商可审计的服务使用记录，非主观报告。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 研究在专有匿名电信数据集上，对流失和游戏下载两个预测任务运行九种设置（T1 logistic基准、T2.1-T2.6 propositionalization、T3.1-T3.3 MLN），报告Accuracy/Precision/Sensitivity/Specificity和ROC曲线；结果显示T2.1-T2.4的准确率和敏感度优于logistic基准，MLN在ROC上优于基准但在敏感度上未优于最佳propositionalization，从而支持'网络邻域信息提升客观预测指标'的核心主张。
- Decision: 核心结果指标（流失、游戏下载预测的准确率、敏感度、特异度、精确率、ROC）均基于运营商日志中的实际行为标签，不依赖人类感受或语义评价，属于客观固定事实标签；研究问题、评价结构和贡献声明均围绕通过社交网络信息提升这些客观预测指标展开。同时全文存在明确的benchmark表述：作者在研究方法与结果部分明确将logistic回归作为benchmark，并在同一专有数据集上比较了logistic、propositionalization和MLN，结果表的精确数值和ROC曲线直接支持客观指标提升主张。因此两模块均通过，strict_include=true。
- Confidence: 0.72

## Gaining a Seat at the Table: Enhancing the Attractiveness of Online Lending for Institutional Investors

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2022.0638
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "内部收益率（IRR）", "measurement_cn": "根据借款人的实际还款、违约、核销产生的现金流，按公式(1)求解使NPV=0的折现率；形成月度贷款组合后取样本外平均并年化。", "objectivity_reason_cn": "构念是投资现金流的时间价值，值由LendingClub平台可审计的还款和核销事实决定，不依赖人的感受、意义理解或价值判断。"}, {"name_cn": "投资回报率（ROI）", "measurement_cn": "按公式(2)-(3)，用累计折现支付CDP与初始本金计算组合ROI；用于优化目标和部分业绩比较。", "objectivity_reason_cn": "由贷款实际现金流入和固定折现假设计算，客观可验证。"}, {"name_cn": "公开市场等价（PME）", "measurement_cn": "贷款组合IRR除以按相同现金流构造的指数组合IRR，公式(16)并在表3中报告。", "objectivity_reason_cn": "贷款组合IRR和指数组合IRR均由客观现金流计算，PME为两个客观财务指标的比值。"}, {"name_cn": "与基准指数的相关系数", "measurement_cn": "样本外期间贷款组合IRR与各基准指数组合IRR的相关系数，表3报告。", "objectivity_reason_cn": "基于客观IRR序列计算，反映分散化收益，不依赖主观体验。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: S&P 500 Index | Bloomberg U.S. Aggregate Bond Index | S&P U.S. Treasury Bond Indexes (1–3, 3–5, 10–20 Year) | MSCI U.S. REIT Index
- Benchmark evaluation: GCPP在LendingClub超过100万笔贷款样本上按月度样本外形成贷款组合，与等权组合、风险过滤组合、均值方差组合、线性/梯度提升/神经网络回归组合比较；并将贷款组合与S&P 500、美国综合债券、美国国债（1–3、3–5、10–20年）和REIT指数按相同现金流构造的指数组合进行比较，使用PME、相关系数和Pr(win)等客观指标。
- Decision: 核心指标IRR、ROI、PME和相关系数均由贷款和指数实际现金流客观计算，不属于人类主观评价或语义判断；全文围绕GCPP组合提升样本外回报这一唯一核心目标展开，利益率偏差和金融普惠等仅为延伸含义；评价部分明确以各种基准组合和市场指数作为比较对象，比较结果直接支撑核心改进主张。因此客观指标模块和benchmark模块均通过，strict_include=true。
- Confidence: 0.72

## Music intelligence: Granular data and prediction of top ten hit songs

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113535
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "AUC（ROC曲线下面积）", "measurement_cn": "模型对2016年Billboard Hot 100周榜歌曲是否为top-ten hit song的out-of-time预测概率与实际榜单事实标签比较计算AUC。", "objectivity_reason_cn": "预测目标是由公开Billboard榜单确定的top-ten/non-top-ten事实标签，不依赖人的感受、语义评价或价值判断；AUC由确定性的分类事实计算。"}, {"name_cn": "分类正确/错误次数与McNemar检验", "measurement_cn": "在选定阈值下统计两个模型对测试歌曲分类的正确/错误混淆数，并用McNemar检验比较含与不含acoustic features的模型预测能力。", "objectivity_reason_cn": "正确/错误由模型预测类别与实际Billboard榜单事实标签比对得出，统计检验基于该客观分类结果。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: Billboard Hot 100 weekly chart (1998–2016/2017)
- Benchmark evaluation: 在Billboard Hot 100的2016年周榜（以及2013、2014、2015年周榜作为稳健性检验）上，评价GLM、GBM、RF、DL模型对top-ten-hit-song状态的预测能力；主要比较不含acoustic features的Model2与含main/auxiliary acoustic features的Model3/Model4。结果显示AUC由Model2的0.655提升至Model3的0.679和Model4的0.687，McNemar检验在多数设定下显著支持acoustic features改善预测。
- Decision: 文章的核心目标是客观预测能力的提升：利用Spotify声学特征改进Billboard Hot 100 top-ten-hit-song状态的预测，评价指标为AUC与基于事实标签的分类正确性/McNemar检验，全部为客观可验证指标；该预测能力提升是唯一核心目标与贡献。基准评价方面，文章明确以公开领域标准数据Billboard Hot 100作为评价场地，在out-of-time周榜上比较含/不含声学特征的模型，AUC和McNemar检验提供了与基线模型的明确对照，benchmark评价直接支撑核心提升主张。因此两个模块均通过。
- Confidence: 0.72

## Ontology based integration of XBRL filings for financial decision making

- Year/journal: 2014 / Decision Support Systems
- DOI: 10.1016/j.dss.2014.09.004
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "财务类别取值准确率", "measurement_cn": "OFXD 从 XBRL 10-K 实例中提取的 7 个财务项目（净收益、总资产、经营性现金流、净销售额、流动资产、流动负债、普通股）与人工从 EDGAR 10-K 提取值以及 Thomson Reuters Data Stream（TRDS）值精确匹配的百分比。", "objectivity_reason_cn": "财务数值是公司披露的可审计外部事实，精确匹配可被确定性核验，不依赖人的感受、意义理解或价值判断。"}, {"name_cn": "财务比率准确率与 RMSE", "measurement_cn": "OFXD 依据 SWRL 规则计算的 ROA、CFO、ACCRUAL、TURN、LIQUID、EQ_OFFER 六个比率，与用 EDGAR/TRDS 数据手工计算出的比率精确匹配的百分比，以及围绕基准值的 RMSE。", "objectivity_reason_cn": "比率由客观财务数值和公开公式确定性计算；RMSE 是与基准数值的确定性偏差度量，不涉及主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: OFXD 在 FY2011（43 家测试公司）和 FY2012（68 家）的 XBRL 10-K 申报上，以 EDGAR 人工提取值和 Thomson Reuters Data Stream 作为基准，评估 7 个财务类别和 6 个财务比率的准确率与 RMSE；结果是训练集 100%，测试集财务类别准确率约 79%–100%，比率准确率约 76%–98%，并与基准数据源存在明确的数值偏差报告。
- Decision: 客观指标层面：OFXD 的核心成功标准是财务数据项及比率相对 EDGAR/TRDS 的准确率和 RMSE，全部来自可审计的财务事实和确定性公式，不包含满意度、感知或语义质量评价；评价结构、设计目标和贡献声明均围绕该客观性能展开，且无并列的主观/理论核心目标。Benchmark 层面：作者在 Evaluation 部分明确使用 benchmarked values / benchmarked against 描述与 EDGAR、TRDS 的系统化基准对照，benchmark 结果直接支撑 OFXD 解决语义异构、提高财务数据互操作性的核心主张，并有明确参照点。因此两个模块均通过，strict_include=true。
- Confidence: 0.72

## Predicting the length of hospital stay of burn patients: Comparisons of prediction accuracy among different clinical stages

- Year/journal: 2010 / Decision Support Systems
- DOI: 10.1016/j.dss.2010.09.001
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "住院天数预测误差（MAE、MRE）", "measurement_cn": "基于医院病案记录中的实际LOS与模型预测LOS计算平均绝对误差（MAE）和平均相对误差（MRE），通过十折交叉验证重复三次取平均。", "objectivity_reason_cn": "实际LOS是可审计的外部事实，预测误差由确定公式计算，不依赖人的感受、语义判断或主观评价。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在1080例烧伤病例上，以线性回归分析为基准，评价M5和SVM回归在admission、acute、post-treatment三个临床阶段的LOS预测效果，报告MAE/MRE并进行统计显著性检验。
- Decision: 目标指标为住院天数预测误差（MAE/MRE），基于实际LOS这一客观事实，不涉及主观评价；研究问题、评价和贡献均围绕预测准确率的提升与比较，客观指标是唯一核心目标。全文存在明确benchmark表述：以线性回归分析为性能基准，并在实证评价中与M5、SVM回归比较，基准比较结果直接支撑核心预测效果主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.72

## Reference metadata extraction using a hierarchical knowledge representation framework

- Year/journal: 2007 / Decision Support Systems
- DOI: 10.1016/j.dss.2006.08.006
- Metric/core status: objective_fixed_factual_labels / exclusive_objective_improvement
- Metrics: [{"name_cn": "参考文献元数据字段抽取准确率（author/title/journal/volume/issue/year/pages）", "measurement_cn": "字段级准确率 = 正确抽取字段数 / 总字段数；在自行构建的六种参考样式测试集（每种10,000条）上计算，并在 Cora reference dataset 上进行了额外比较实验。", "objectivity_reason_cn": "抽取对象是引用字符串中的事实型元数据字段，正确性通过与参考答案的字段标签比对确定；不涉及人类感受、语义质量或价值判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: Cora reference dataset (Cora dataset)
- Benchmark evaluation: 在公开的 Cora reference dataset 上运行所提出的 INFOMAP 模板式 RME 方法，报告整体字段准确率 73.34%、作者字段准确率 87.40%；在 Cora 中 166 条期刊参考文献子集上整体字段准确率 84.94%、作者字段准确率 93.37%。同时，作者以 Citeseer 的作者准确率 82% 作为现有方法参照，支持其方法在作者字段抽取上的提升。
- Decision: 客观指标：全文以字段准确率（正确抽取字段数/总字段数）为核心因变量，在自行构建的六种参考样式测试集和公开 Cora 数据集上计算，属于可审计的事实型信息抽取性能，不依赖人类主观评价或语义质量判断。唯一核心目标：提出层次模板式 RME 方法并提升参考元数据抽取准确率，摘要、系统设计、实验、比较和结论均围绕该目标；'较少标注数据'只是辅助优点，不构成并列核心目标。Benchmark：虽然全文没有使用 'benchmark' 一词，但明确命名并使用了公开的 Cora reference dataset 作为测试床，并明确以 Citeseer 为比较对象；该比较用于支持作者字段等抽取准确率的提升主张。因此两个模块均通过，strict_include=true。
- Confidence: 0.72

## Using structure-based data transformation method to improve prediction accuracies for small data sets

- Year/journal: 2012 / Decision Support Systems
- DOI: 10.1016/j.dss.2011.11.021
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "预测精度（平均MSE、误差改进率、STD、总误差）", "measurement_cn": "在MLCC、Concrete Slump、TFT-LCD三组真实数据上，用SVR、BPNN、LR对原始与结构变换后的数据分别建模，计算预测值与实际值的MSE、STD、总误差，并以误差改进率=(Raw−Transform)/Raw汇总比较。", "objectivity_reason_cn": "预测目标K值、混凝土坍落度、cell vernier均为可观测的物理/工艺量；MSE/STD/误差改进率由预测值和真实值之间的数值误差直接计算，不依赖人的感受、语义评价或主观打分。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: UCI Concrete Slump Test dataset (UCI repository)
- Benchmark evaluation: 在UCI Concrete Slump数据（103条记录、7个输入、预测SLUMP）上，以5/10/15/20/25个训练样本进行20次重抽样实验，比较原始数据与结构变换后数据使用SVR/BPNN的预测误差；报告SVR误差改进率约2.12%–3.38%、BPNN误差改进率约10.65%–29.39%，并用t检验判断显著性。该结果直接支撑“提出方法提升预测精度”的核心主张。
- Decision: 客观指标方面，核心成功指标是预测误差类数值（MSE、STD、误差改进率、总误差），目标对象是可观测物理/工艺量，不依赖人的主观评价，且是全文唯一核心目标。Benchmark方面，虽然正文未使用“benchmark”一词，但明确命名公开UCI Concrete Slump数据集并在实验部分作为评价场地，同时与Raw-SVR、Raw-BPNN、Raw-LR等明确参照点比较，benchmark结果直接支撑预测精度提升的核心主张。因此两个模块均通过，严格纳入。
- Confidence: 0.72

## How Do Enterprise Resource Planning Systems Affect Firm Risk?  Post-Implementation Impact

- Year/journal: 2002 / MIS Quarterly
- DOI: 10.25300/misq/2015/39.1.03
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "企业风险（盈利波动性）", "measurement_cn": "以未来5年年度盈利（经总资产缩放）的标准差衡量，数据来自Compustat数据库。", "objectivity_reason_cn": "该值由公开可审计的财务数据按固定规则计算，不依赖用户/专家感知、感受或语义价值判断。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在样本分割稳健性检验（Appendix C）中，以无ERP企业为基准组，分别估计ERP系统范围L1-L4对企业风险的系数，结果显示各层级均显著降低风险，为风险降低主张提供基准比较证据；在效应量分析中，以R&D支出为基准比较效应量，说明ERP风险降低效应的经济意义。
- Decision: 客观指标方面：企业风险（盈利波动性）由Compustat财务数据经固定规则计算，不涉及主观评价；全文研究问题、假设、评价和贡献均围绕ERP是否降低企业风险及条件效应，构成客观指标提升的唯一核心目标。Benchmark方面：作者在评价语境中明确使用了benchmark一词，在Appendix C中以无ERP企业为基准组进行样本分割比较，并以R&D支出为效应量比较基准；该基准比较用于支持ERP风险降低的核心主张，且存在明确参照点。因此两个模块均通过。
- Confidence: 0.7

## Identity disclosure protection: A data reconstruction approach for privacy-preserving data mining

- Year/journal: 2009 / Decision Support Systems
- DOI: 10.1016/j.dss.2009.07.003
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "记录链接率（RL ratio）", "measurement_cn": "将掩码/重建后的记录与原始记录按归一化欧氏距离匹配，若最近或第二近的原始记录是对应记录则记为链接，RL=链接记录百分比。", "objectivity_reason_cn": "该指标完全由数据之间的可审计距离计算得出，不依赖人的感受或语义评价。"}, {"name_cn": "分类准确率（Accuracy）", "measurement_cn": "在UCI Diabetes和German Credit数据上，用C4.5和SVM对未匿名化测试集进行评估，报告多次运行的平均准确率。", "objectivity_reason_cn": "准确率是对数据集中已知事实类标签（疾病结果、信用评级）的客观预测匹配率，不依赖主观评分。"}, {"name_cn": "简单统计误差（ADIM/ADIFC）", "measurement_cn": "计算重建数据与原始数据在数值属性均值上的平均偏差ADIM，以及在名义属性频数上的平均偏差ADIFC。", "objectivity_reason_cn": "这些是确定性的统计距离指标，可由数据直接计算，不涉及人类体验或价值判断。"}]
- Benchmark status: named_public_benchmark_central
- Named benchmarks: UCI Machine Learning Repository - Diabetes | UCI Machine Learning Repository - German Credit
- Benchmark evaluation: 在 UCI Diabetes 和 German Credit 上，对原始数据、仅聚合/交换、以及聚合/交换+GA 在 k=2/6/10 下的重建结果进行比较，报告 C4.5 和 SVM 的 RL、Accuracy、FN/FP 和简单统计误差。
- Decision: 文章的核心目标是通过数据重建方法实现k-匿名隐私保护，同时保持分类准确率；核心指标（记录链接率、分类准确率、简单统计误差）均是可确定性计算的客观指标，无主观量表或专家质量评分。实验在 UCI Diabetes 和 German Credit 两个命名公开标准数据集上进行，并以原始数据、仅聚合/交换以及不同k值作为明确参照点，基准评价支撑了“显著降低披露风险、同时保持合理数据效用”的核心主张。因此两个模块均通过，严格纳入。
- Confidence: 0.68

## Ephemeral State-Dependent Recommendation for Digital Content

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2022.664
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "推荐书籍阅读率（readrate）", "measurement_cn": "在12天观察期内，用户阅读至少一章的推荐书数/总推荐书数，来自平台阅读日志", "objectivity_reason_cn": "由系统日志直接统计的事实行为，不依赖人的感受或语义评价"}, {"name_cn": "推荐书籍阅读时长（readtime）", "measurement_cn": "阅读推荐书的总分钟数，来自平台阅读日志", "objectivity_reason_cn": "平台可审计的行为时长，客观可验证"}, {"name_cn": "支付金额（payment）", "measurement_cn": "用户在观察期内为推荐内容支付的金额，来自平台交易日志", "objectivity_reason_cn": "交易金额是客观可审计事实"}, {"name_cn": "非推荐内容阅读量（spillover）", "measurement_cn": "同一类别/跨类别/总体非推荐书被阅读的数量，来自平台日志", "objectivity_reason_cn": "需求溢出用阅读计数表示，客观可验证"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在合作电子书平台的现场实验中，将两个状态依赖方案 T3/T4 与基准方案 C1/C2 及状态无关方案 T1/T2 比较；主要因变量为阅读率、阅读时长、支付和非推荐内容阅读量。结果称状态依赖方案显著优于状态无关方案，且 T4（congruent）整体优于 T3（incongruent）。
- Decision: 核心成功指标均为平台可审计的阅读/支付/溢出计数，客观且为唯一核心目标；实验中使用明确标记的 Benchmark schemes（C1/C2）作为基准，并通过随机现场实验结果（Table 4 等）支持状态依赖推荐方案的客观指标提升，因此 strict_include=true。
- Confidence: 0.63

## The Structured Process Modeling Method (SPMM) what is the best way for me to construct a process model?

- Year/journal: 2017 / Decision Support Systems
- DOI: 10.1016/j.dss.2017.02.004
- Metric/core status: fully_objective_direct / exclusive_objective_improvement
- Metrics: [{"name_cn": "建模时间（modeling time）", "measurement_cn": "从开始阅读案例描述到建模工具中最后一次操作的时间，由 Cheetah Experimental Platform 自动记录。", "objectivity_reason_cn": "基于系统日志的持续时长，不依赖人的感受、语义评价或价值判断。"}, {"name_cn": "建模努力（modeling effort）", "measurement_cn": "建模工具中的操作次数（元素创建、移动、删除等），由工具自动记录。", "objectivity_reason_cn": "基于可核验的系统日志计数，客观可重复。"}, {"name_cn": "模型质量错误（syntactic/semantic errors）", "measurement_cn": "根据附录 F/G 的固定编码方案，由外部编码者对照 BPMN 语法规则和案例文本标记缺失、多余、错误等错误类型，再统计错误数和错误类型数。", "objectivity_reason_cn": "目标是判断模型元素与语法规则/案例文本的事实一致性，属于可核验的事实标签；尽管需要人工编码，但依据固定规则而非主观质量偏好。"}]
- Benchmark status: benchmark_comparison_central
- Named benchmarks: 
- Benchmark evaluation: 在实验第二部分，每位参与者先完成一个基准建模任务（defaulter handling case），作为处理前基线；第三部分完成实验建模任务（mortgage request process），并将两者结果进行比较；处理组和对照组之间的比较也以该基准为参照。4.5.1用基准案例与实验案例对比评估处理采纳（fitting technique增加、misfitting减少），4.5.2指出基准案例得到与实验案例类似的结果。
- Decision: 客观指标方面：核心目标是降低建模认知错误、提高建模效率（时间和努力）与有效性（错误数），均以工具日志和固定编码规则测量，不依赖主观质量偏好；用户感知仅作为初步补充，未进入核心成功主张。核心目标唯一性方面：研究问题、设计目标、评价和贡献声明均围绕客观建模改进展开，没有并列的理论、制度或政策贡献。Benchmark方面：在实验任务部分作者明确使用“benchmark”一词为每位参与者设置前测基线任务，并将基准案例与实验案例、处理组与对照组进行比较；该基准比较用于支撑处理采纳和处理效应的核心改进主张。因此两个模块均通过。
- Confidence: 0.62
