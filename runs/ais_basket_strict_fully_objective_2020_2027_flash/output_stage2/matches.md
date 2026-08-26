# stage2 matches

- Completed: 232
- Matches: 198

## A decision support framework for home health care transportation with simultaneous multi-vehicle routing and staff scheduling synchronization

- Record: 9312
- Year / journal: 2020 / Decision Support Systems
- Status / role: fully_objective / exclusive
- Reason: The paper's central contribution is a mathematically formulated optimization model and an algorithmic framework (HGA) to solve it. All reported success outcomes—total cost, optimality gap, computational time, and total distance—are computed by deterministic formulas or system logs, with no subjective or human-judged measures. The core role of these objective metrics is exclusive: the model's objective function minimizes cost, and the computational experiments evaluate solution quality and efficiency solely on these metrics. The framework is demonstrably a software artifact (MILP + HGA implementation) and comparative improvements over CPLEX, VNS, GAF, and GA are shown on multiple instance sets. Thus all five strict gates are satisfied.

## A decision support system for home dialysis visit scheduling and nurse routing

- Record: 1688
- Year / journal: 2020 / Decision Support Systems
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现足以推翻初筛的主观核心结果或混合核心贡献。论文的核心贡献是开发并验证HDSS，以总行驶距离、总行程时间、所需护士数和成本节省作为主要成功标准，全部由地图数据、排班数据和模型确定性计算获得；比较基准为手工排班，改善幅度明确。用户中心设计验证、管理层批准和预期管理效益等主观/定性内容是非核心叙述，删除后核心客观主张完整。因此五个门槛全部满足，判定为严格客观正例。

## A dynamic classification unit for online segmentation of big data via small data buffers

- Record: 16104
- Year / journal: 2020 / Decision Support Systems
- Status / role: fully_objective / exclusive
- Reason: 对初筛进行反向审计后未发现推翻理由。文章核心贡献是提出并实现 DCU，目标是以小缓冲区实现对大数据流的在线动态分割，并用运行时间、RMSE、段数等完全客观指标与静态/动态基线比较，证明增量动态方法在计算效率上的改善和分割质量的接近。预测试虽使用固定标签计算聚类准确率，但属于冻结标签 benchmark 例外，且作为可行性验证而非核心主张。全文无主观自报或人工语义质量判断作为效果测量。五个门槛均为 true，因此维持严格正例。

## A dynamic shipment matching problem in hinterland synchromodal transportation

- Record: 1518
- Year / journal: 2020 / Decision Support Systems
- Status / role: fully_objective / exclusive
- Reason: 论文以在线同步联运动态匹配问题为对象，提出滚动时域方法和启发式算法，并以最小化总成本为核心优化目标。所有核心成功指标均为确定性成本函数、CPU时间和gap，来自合成实例和固定系数，没有任何主观评分、自报数据或人工语义判断。实验结果相对精确算法、贪婪基准以及不同参数设置证明了总成本和计算效率的改善。因此所有五个门槛均通过，符合严格客观指标正例。

## A two-stage machine learning framework to predict heart transplantation survival probabilities over time with a monotonic probability constraint

- Record: 3854
- Year / journal: 2020 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 反向审计未发现能推翻初筛的主观或自报核心证据。全文核心成功主张完全基于UNOS冻结生存/死亡标签上的预测性能指标（AUC、G-Mean、准确性等）和等渗回归的单调性保证，未使用问卷、量表、专家评分或人工语义编码；主观/定性表述仅是附属说明。比较证据充分：Table 5给出等渗回归前后在同一holdout集上的指标差异，Section 6.1给出与文献AUC基准的比较，10年AUC超越现有方法；同时框架和Web应用均有明确实现与公开代码。因此五个门槛全部满足，应确认严格匹配，objective_status为benchmark_objective_with_fixed_labels，core_role为exclusive。

## An improvement in the quality of expert finding in community question answering networks

- Record: 7848
- Year / journal: 2020 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 反向审计未发现可推翻初筛的核心主观/自报结果。核心评价是基于固定专家黄金集的检索排序指标MAP/P@K，属于冻结标签基准；Coverage/Confidence/Fscore是客观但居中的辅助指标。唯一的人工词云检查仅为图1示意，不参与定量成功主张。制品为明确算法/软件管线，并通过与8个基线的对比证明了核心指标MAP的显著改善。因此五个门槛均满足。

## An intelligent decision support system prototype for hinterland port logistics

- Record: 9276
- Year / journal: 2020 / Decision Support Systems
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现足以推翻初筛的证据。全文所有核心成功结果均来自完全客观的仿真计算：总运输成本、行驶距离、行驶时间、车队规模、行程数和代理人成本节省，均与现状基线比较并展示显著改善。没有主观评分、自报结果或人工语义质量判断作为核心贡献；RL收敛和PCS使用概率属于机制性过程结果，删除后核心主张仍完整。因此确认严格匹配。

## Antisocial online behavior detection using deep learning

- Record: 7274
- Year / journal: 2020 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / dominant
- Reason: 初筛成立。论文的核心目标是评估和提升AOB检测的客观分类性能；提出了psHAN并相对HAN实现了多数指标改善，同时证明预训练transformer相对多个baseline有更好性能。所有核心成功结果均来自四个冻结标签数据集上的Av. Prec., AUC和F1，不包含主观评分或自报结果。LIME部分仅是辅助性解释展示，删除后不影响核心性能主张。因此满足严格客观指标正例。

## Automated discovery of business process simulation models from event logs

- Record: 15528
- Year / journal: 2020 / Decision Support Systems
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现足以推翻初筛的证据。文章的核心贡献是自动发现并优化业务流程模拟模型，核心成功指标ELS完全由模拟日志与原始事件日志的确定性编辑距离计算，不涉及问卷、自报或人工评分；Simod是明确实现的软件制品；通过与基线配置的对比和Mann-Whitney U检验，在三个日志上证明客观指标的显著改进。五个门槛全部满足，核心角色为exclusive。

## Automated dynamic approach for detecting ransomware using finite-state machine

- Record: 14428
- Year / journal: 2020 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 初筛判定成立。全文核心成功主张全部来自自动检测性能指标（TPR/FPR/FNR/ACC），且这些指标基于系统告警与固定malware/legitimate标签的混淆矩阵计算，属于冻结标签benchmark例外。人工参与仅限样本标签确认和FSM设计阶段，不构成对系统输出质量的主观评分。文章明确实现了制品并通过与现有方法比较证明客观改善，五个门槛均满足。

## Bayesian neural networks for flight trajectory prediction and safety assessment

- Record: 4736
- Year / journal: 2020 / Decision Support Systems
- Status / role: fully_objective / exclusive
- Reason: 反向审计未找到足以推翻初筛的证据。全文所有核心性能与安全评估结果均来自FAA SWIM SFDPS自动监视系统记录的位置/速度/高度数据，预测误差、空间距离、分离距离等均为客观计算指标；作者明确开发/修改了软件实现与模型（Spark处理、DNN、LSTM、融合、安全指标），并通过与确定性DNN、线性/SVM/DTR基线、单独LSTM的对比及留一交叉验证证明了客观改善。没有问卷、自报、专家评分、人工语义质量编码或主观成果指标。因此维持初筛：严格客观正例。

## Deep learning for detecting financial statement fraud

- Record: 14538
- Year / journal: 2020 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 反向审计未发现足以推翻初筛的假阳性因素。论文的核心目标是提升欺诈检测的分类性能，评价指标完全基于SEC AAER形成的固定标签计算，属于冻结标签上的计算基准。全部核心成功结果均为客观分类指标，未使用主观量表、自我报告或人工语义质量评分。红标签句子解释只是辅助机制，不影响核心性能主张的完整性。制品设计明确，并与多个基线和替代深度学习方法在统一测试集上进行了比较，证明了AUC和敏感性的提升。因此保持确认。

## Employees recruitment: A prescriptive analytics approach via machine learning and mathematical programming

- Record: 8928
- Year / journal: 2020 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 反向审计未发现足以推翻初筛的主观或混合核心证据。预测AUC基于HR预先定义的固定成功标签，属于冻结标签上的计算基准；全局优化指标（平均预测概率、熵、比例、标准差）均由公式和分配结果客观得出；优化结果相对招聘人员实际选择在多个客观维度上显著改善。可解释性洞察虽为贡献亮点，但其统计基础客观，且删除后核心预测与优化成功主张完整成立。因此维持strict_match=true。

## Evaluating the credit risk of SMEs using legal judgments

- Record: 6966
- Year / journal: 2020 / Decision Support Systems
- Status / role: fully_objective / exclusive
- Reason: 经全文反向审计，核心成功主张是加入法律判决特征后显著提升中小企业违约预测的判别性能（AUC/KS）和授信表现（实际违约数下降）。这些结果均基于银行实际贷款违约标签（逾期超过90天）和模型输出计算，完全客观、可复算。唯一的主观/外部判断出现在经济节省的说明性估算中（银行提供平均贷款额和30%损失率假设），但其不是核心成功指标；附录A的人工检查也只是开发阶段的信息抽取准确性验证。通过与基础特征基线的配对比较，模型改善被显著证明。因此初筛的正例判定成立。

## ForeSim-BI: A predictive analytics decision support tool for capacity planning

- Record: 9376
- Year / journal: 2020 / Decision Support Systems
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现推翻初筛的证据。论文核心目标是提升维护工作量预测准确性这一完全客观的结果指标。所有核心成功结果（PE、MAE、平均误差、成本节省）均基于MRO系统记录的实际工时与工具预测值的确定性计算。设计阶段使用专家输入定义工作量和类，但不作为有效性度量。没有主观评分、自报、人工评估结果。与当前工程估计模型对比，明显改善。全文无混合核心贡献。因此确认为严格客观正例。

## Forecasting demand profiles of new products

- Record: 4572
- Year / journal: 2020 / Decision Support Systems
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现任何主观或自报核心结果：所有核心成功指标（RMSE、PICP、PINAW、CSL、库存成本）均由真实销售数据、确定性库存模拟和明确公式计算；不存在人工质量评分、用户评价、语义编码或主观权重。DemandForest作为明确设计的算法系统被实质构造和实现，并与ZeroR、OneP基准进行了系统的比较，虽然少数数据集/指标上基准更优，但整体客观改善（尤其合成数据上库存成本显著降低）证据充分。因此确认严格匹配。

## Geo-semantic-parsing: AI-powered geoparsing by traversing semantic knowledge graphs

- Record: 13580
- Year / journal: 2020 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 初筛结论正确。文章的核心科学贡献是一个新的自动地理解析软件流程GSP，其最终目标是在NEEL16公开基准上提升自动地理解析效果。最终成功证据完全是确定性指标：Precision、Recall、F1，依据NEEL16固定人工标注坐标和固定距离阈值计算，另附运行时间。所有核心成功指标均不依赖对输出的人工质量评分、问卷、自报或主观评价。与2个基线和3个SOTA系统（含作者前作）在同一测试集上的比较明确展示GSP F1=0.665优于所有对比方法的F1≤0.553。辅助的特征重要性、粒度分析和叙述性应用案例均可删除而不影响核心结论。因此纳入严格完全客观指标正例，并属于冻结标签基准例外。

## Improving healthcare access management by predicting patient no-show behaviour

- Record: 12160
- Year / journal: 2020 / Decision Support Systems
- Status / role: fully_objective / exclusive
- Reason: 论文明确设计并评估了一个软件制品（DSS），其核心成功指标AUROC、Coverage和Risk全部来自历史预约记录和模型预测的可重复计算，不涉及任何主观评分、自报或人工语义判断。研究通过10×10交叉验证将神经网络与随机森林、逻辑回归和随机基线进行比较，展示了客观指标上的显著改善。研究中的定性反馈和LRP可视化是辅助性内容，删除后核心结论仍完整。因此，五个门槛全部满足，初筛判定正确。

## Is optimal recommendation the best? A laboratory investigation under the newsvendor problem

- Record: 15740
- Year / journal: 2020 / Decision Support Systems
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现可推翻初筛的主观或自报核心结果。文章核心因变量（PtC 效应、实际利润、实际订购量、PtC 不对称）均由实验系统自动记录和理论公式计算，完全客观；算法厌恶与后悔厌恶虽为心理构念，但均由行为代理度量且处于机制层。论文通过 z-Tree 明确设计/修改 DSS 推荐模块，并用 NDSS/ODSS/CDSS/RDSS 对照实验证明了客观指标的显著改善，尤其是激进 DSS 在高利润条件下几乎消除 PtC 偏差。因此 confirmed_strict_match 为 true。

## Missing care: A framework to address the issue of frequent missing values;The case of a clinical decision support system for Parkinson's disease

- Record: 7898
- Year / journal: 2020 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 反向审计未发现足以推翻初筛的证据。文章的核心成功结果全部来自预先冻结的临床诊断标签上的AUC、灵敏度和特异度，属于允许的fixed_label_benchmark例外；没有自报、量表、专家对输出质量的人工评分或人工语义编码作为核心结果。文章亦明确提出并实现了Missing Care框架和PD检测模型，并通过与不使用Missing Care的模型进行统计显著比较来证明改善。因此确认严格匹配。

## Network projection-based edge classification framework for signed networks

- Record: 4136
- Year / journal: 2020 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 反向审计未发现推翻初筛的证据。文章核心贡献是提出 NPECF 算法制品，目标是通过利用未标记边信息提升边符号预测性能；所有核心成功结果（Accuracy、GM、DOR）均基于预先存在的固定边标签自动计算，不属于自报或人工语义评价。并与 SRWR、NbA 在四个真实数据集上进行客观比较并展示改进，因此维持 strict_match=true。

## Novice digital service designers' decision-making with decision aids — A comparison of taxonomy and tags

- Record: 8476
- Year / journal: 2020 / Decision Support Systems
- Status / role: fully_objective / dominant
- Reason: 反向审计未发现推翻初筛的证据。文章以taxonomy-based决策辅助与tags-based/无辅助相比提高选择准确性为核心成功主张，选择准确性为系统直接记录、按预定义正确列表计数的完全客观指标；主观自报变量（认知努力、决策风格）为中介和调节，删除后核心客观主张依然成立。制品为明确设计并实现的Web决策辅助界面，实验比较证明客观改善，因此确认为严格客观指标正例。

## Optimizing microtask assignment on crowdsourcing platforms using Markov chain Monte Carlo

- Record: 10860
- Year / journal: 2020 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 反向审计未发现足以推翻初筛的主观或混合核心证据。文章设计的 MCMC-TA 是明确的软件/算法制品，其最终目标是优化众包平台中的任务分配和工人质量估计，并通过 AUC 与 F-Score 在固定的 Google Fact Evaluation 标签基准上比较多个基线。所有核心成功主张均由这些客观计算指标支撑，不存在问卷、自报、人工质量编码或主观权重作为共同核心结果。因此五个门槛全部满足，确认 strict_match=true。

## Partial order resolution of event logs for process conformance checking

- Record: 9796
- Year / journal: 2020 / Decision Support Systems
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现足以推翻初筛的假阳性依据。论文的核心目标是提高事件日志存在部分序不确定时的一致性检查准确性和运行效率；全部核心成功指标均由确定性公式或机器计时获得，不存在主观评分、自报或人工语义质量判断；所有核心结果均围绕所提出的行为模型和近似算法，并与基线/无近似配置进行直接比较，证明客观改善。因此五道门槛全部满足，且客观指标是唯一核心贡献。

## Predicting performances in business processes using deep neural networks

- Record: 9342
- Year / journal: 2020 / Decision Support Systems
- Status / role: fully_objective / exclusive
- Reason: 初筛判定成立。论文核心目标是提出并验证基于深度神经网络的业务流程模型级性能预测方法；评价指标是事件日志时间戳导出的实际性能与模型预测之间的MAE/MAPE，完全客观；所有核心成功证据均为这些客观误差指标上的比较，没有主观评分、自报或人工质量判断作为核心贡献；方法本身构成明确软件制品，并通过与统计和搜索基线的交叉验证比较证明了改进。

## Preference enhanced hybrid expertise retrieval system in community question answering services

- Record: 5390
- Year / journal: 2020 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 独立反向审计未发现推翻初筛的证据。文章的核心目标是提升CQA中专家检索预测性能；核心成功证据全部来自MRR、P@30、R@30、Accuracy、MSC@30这五类基于固定最佳回答者标签的客观信息检索指标。全文没有问卷、自报、主观质量评分或混合核心主观贡献。PEHER被明确实现为软件系统，并与20种已有方法和消融变体比较，在绝大多数比较案例中取得最佳结果。因此满足五个门槛，属于benchmark_objective_with_fixed_labels，核心角色为exclusive。

## Stratifying no-show patients into multiple risk groups via a holistic data analytics-based framework

- Record: 4588
- Year / journal: 2020 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 初筛判定成立。全文核心贡献是构建并验证一个能够准确预测no-show患者、同时具备变量选择和数据平衡能力的预测模型，并提供风险分层和网页决策支持工具。所有核心成功证据均来自基于历史预约记录中实际是否出席标签（冻结标签）计算得到的AUC、accuracy、sensitivity、specificity等客观分类指标，不依赖主观评分、自报或人工语义判断。模型改进通过多方案对比（不同变量集、平衡方法、模型）和阈值敏感度分析得到证明。工具本身虽然未被用户实际评价，但这不影响核心预测性能指标的客观性。因此，满足严格客观指标正例的所有条件。

## The crowd against the few: Measuring the impact of expert recommendations

- Record: 13538
- Year / journal: 2020 / Decision Support Systems
- Status / role: fully_objective / dominant
- Reason: 反向审计未能推翻初筛。文章通过在线随机对照试验，在真实推荐系统中实质加入专家推荐模块，以服务器自动记录的点击流日志为主要成功依据，证明治疗组相对对照组的观看剪辑数、推荐点击数、访问数、活跃访问、多剪辑访问、回访率和留存率均有提升。感知满意度虽为自报问卷且无显著差异，但地位次要，不承载核心成功主张；删除主观部分后核心结论完整。多样性、覆盖度等客观指标进一步支持解释，但核心贡献仍是客观行为指标。因此五道门槛全部通过，确认严格匹配。

## Containing COVID-19 through physical distancing: the impact of real-time crowding information

- Record: 10546
- Year / journal: 2020 / European Journal of Information Systems
- Status / role: fully_objective / exclusive
- Reason: 反向审计未推翻初筛：文章核心干预是明确软件制品（实验 DSS 网站）的界面组件设计（CI 有无、历史平均 vs 实时即时性），核心成功结果是用户实际选择低拥挤地点的行为，由系统直接客观记录。健康焦虑、感知拥挤、感知即时性、加工流畅性等自报变量仅作为调节变量、操纵检查或机制解释，删除后不破坏 H1/H2 等核心行为主张。没有人工语义编码或主观质量评分作为核心结果。因此符合五个门槛，为严格客观指标正例。

## Ingredients for successful badges: evidence from a field experiment in bike commuting

- Record: 6738
- Year / journal: 2020 / European Journal of Information Systems
- Status / role: fully_objective / exclusive
- Reason: 第一阶段的正例判定经反向审计后仍然成立。核心成功指标是RFID系统自动记录的每周骑行天数，完全客观；文章以提升该目标行为为核心目的，通过2×2×2随机现场实验比较徽章设计组件的替代方案，并获得了统计显著的改善证据。唯一的主观/自报成分（自我报告的离家英里数）只作为稳健性模型的协变量出现，不是核心结果或贡献。没有任何人工语义质量判断或主观结果作为并列核心。因此满足全部五项门槛，属于严格客观正例。

## Discovering event episodes from sequences of online news articles: A time-adjoining frequent itemset-based clustering method

- Record: 20263
- Year / journal: 2020 / Information & Management
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 初筛正例经反向审计后仍成立。全文的核心贡献是提出TAFIED算法并证明其在事件片段发现上优于现有基准，而所有核心有效证据均来自与固定ground truth事件片段标签的确定性集合比较：CR、CP和F-measure。真实片段标签虽由人预先构建，但属于冻结标签，符合固定标签例外。第6节的人工标签选择示例仅用于说明频繁项可辅助标签建议，作者明确承认其主观性且未作为方法效果评价，删除后核心主张完整。因此五个门槛全部通过，objective_status为benchmark_objective_with_fixed_labels，core_role为exclusive。

## Discovering event episodes from sequences of online news articles: A timeadjoining frequent itemset-based clustering method

- Record: 16126
- Year / journal: 2020 / Information & Management
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 确认初筛：文章提出并实现明确软件制品 TAFIED，核心目标是在固定的人工标注基准（TDT2/TDT3 的 248 个真实事件片段）上提升事件片段发现的 CR/CP/F-measure。所有核心成功结果均基于确定性聚类评估公式，属于冻结标签基准例外；不存在作为共同核心目标的主观评分、自报或人工语义质量评估。相对 FIHC、HAC、HAC+TD 展示了 PRT 曲线、最佳 F 值及 Wilcoxon 检验的客观改善，且 TP 消融证明了方法组成部分的贡献。

## One size does not fit all: Rethinking recognition system design for behaviorally heterogeneous online communities

- Record: 2888
- Year / journal: 2020 / Information & Management
- Status / role: fully_objective / exclusive
- Reason: 尽管初筛存在潜在风险（例如人类管理者Elite标签用于权重、作者在讨论中弱化‘更好’主张），但审计确认：核心成功主张是MSR系统在六个客观Yelp平台记录参数（评论数、关注者、总票数、好友数、平均票数、经验年数）上显著优于现有Yelp系统；这些参数完全来自平台日志，无自报、人工质量评分或主观评估。人类标签仅作为内部设计输入，不影响最终客观评估。比较是与当前实践的客观对比，全部指标显著改善（p<0.001）。因此五个门槛全部满足，维持初筛确认。

## Predicting shareholder litigation on insider trading from financial text: An interpretable deep learning approach

- Record: 1790
- Year / journal: 2020 / Information & Management
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 反向审计未发现推翻初筛的证据。文章核心目标是通过设计深度学习模型提升对内幕交易诉讼这一固定事实标签的预测性能，核心成功指标为AUC和十分位捕获率，均完全由模型输出与外部客观标签计算，不依赖人工评分或自报结果。解释性分析虽存在，但不构成核心成功主张。模型相对基线的客观改进显著（AUC提升2.27个百分点，p=0.024；十分位捕获率提升）。因此，满足全部五个门槛，确认为严格正例。

## The effect of intention analysis-based fraud detection systems in repeated supply Chain quality inspection: A context of learning and contract

- Record: 9076
- Year / journal: 2020 / Information & Management
- Status / role: fully_objective / exclusive
- Reason: 初筛成立。文章的核心目标是评估IAFDS这一明确软件制品对买方质量检验绩效的影响，核心结果变量为决策时间、检验成本和正确拒绝，全部由实验系统自动记录和计算。文中的主观成分仅为操纵检查和控制变量，不构成核心成功结果。文章通过2×2实验将IAFDS与NO-DSS比较，并在传统合同下显示客观改善，在惩罚合同下显示调节效应，属于完整的比较性验证。五个门槛均通过。

## Finding Useful Solutions in Online Knowledge Communities: A Theory-Driven Design and Multilevel Analysis

- Record: 3686
- Year / journal: 2020 / Information Systems Research
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: After full-text audit, the initial stage-1 inclusion is upheld. The paper's research question is explicitly to design a machine learning algorithm to predict useful solutions without human intervention. The artifact is a concrete text analytic system with multiple implemented components. The core success outcomes are post-level and thread-level usefulness classification performance evaluated by deterministic precision/recall/f-measure against frozen labels derived from original askers' solved/helpful tags and domain-expert not-helpful annotations. This fits the fixed-label benchmark exception: the evaluation measures a computational model's predictive performance against fixed target labels, not human judgment of system-generated outputs. Extensive comparisons demonstrate improvement over lexical baselines, individual feature dimensions, full feature sets, feature-selected subsets, deep learning baselines (LSTM/CNN), and prior computational models. No subjective questionnaire, self-report, user perception, or human quality-rating outcome is used as a core result. The contribution is exclusively based on objective classification benchmark metrics. All five gates are true.

## Sustaining a Good Impression: Mechanisms for Selling Partitioned Impressions at Ad Exchanges

- Record: 1560
- Year / journal: 2020 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: 经反向审计，初筛判定成立。全文为机制设计理论研究，核心贡献是提出可实时计算的广告交易分区印象拍卖机制，并以交易所期望收入、广告商期望效用和社会福利作为成功指标。所有指标均由数学模型和数值仿真客观计算，没有主观报告、自报数据、人工语义编码或专家整体评分。主观/人工证据不存在，删除后核心主张仍完整。客观指标是主要最终目标和成功依据，而非附属结果。同时，机制设计中包含明确可计算的分配规则和支付规则，并相对 BASE 和 SEQ 机制通过解析证明及数值实验证明了改善。因此满足全部五个门槛，objective_status 为 fully_objective，core_role 为 exclusive。

## Words Matter! Toward a Prosocial Call-to-Action for Online Referral: Evidence from Two Field Experiments

- Record: 1142
- Year / journal: 2020 / Information Systems Research
- Status / role: fully_objective / dominant
- Reason: After independent audit, the paper's core contribution is a causal field-experimental comparison of CTA framing in an online referral program. The primary success outcomes are the sender's referral decision, total referrals sent, and recipient purchases, all automatically logged by the platform/company and transaction-based. The subjective MTurk measures and NPS moderator are secondary mechanism/heterogeneity analyses; removing them does not undermine the core field-result claim. Two randomized field experiments with control and alternative CTA arms demonstrate objective, statistically significant improvements. Thus the paper qualifies as a fully objective core-effectiveness study where a software-mediated artifact (CTA wording/pages) was modified and comparatively improved.

## A Novel Recommendation Model for Online-to-Offline Service Based on the Customer Network and Service Location

- Record: 1944
- Year / journal: 2020 / Journal of Management Information Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 反向审计未能推翻初筛。全文核心贡献是以离线推荐性能（F-Score、Precision、Recall）为最终目标设计和验证推荐模型；评估使用已有的用户历史评分作为冻结标签，属于允许的 benchmark_objective_with_fixed_labels。文中对评分真实性、偏好和用户感知的讨论均未作为评价指标，只作为动机和局限；删除后核心成功主张仍完整。模型中融入位置、网络、PCC 等均为算法设计，不依赖人工对产出的主观质量评定。与多个基线的对比以及参数/消融实验明确证明了客观改善。因此 confirmed_strict_match=true。

## Effectiveness of Location-Based Advertising and the Impact of Interface Design

- Record: 1946
- Year / journal: 2020 / Journal of Management Information Systems
- Status / role: fully_objective / exclusive
- Reason: 经过反向审计，未发现足以推翻初筛的主观或自报核心结果。全文所有核心成功结果——组间点击率、按显示排名/产品类别/地理区位的点击率、分层贝叶斯logit模型的距离/排名及交互系数、预测点击率——均来自应用服务器自动记录的点击日志、GPS位置计算、显示排名和实验分组，完全客观。作者对真实应用的界面设计进行了实质性随机操纵，并比较四个版本，证明距离排序的点击率显著更高。删除理论解释和机制说明后，核心成功主张仍然完整。因此确认严格匹配。

## Human Identification for Activities of Daily Living: A Deep Transfer Learning Approach

- Record: 10650
- Year / journal: 2020 / Journal of Management Information Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: Initial stage-1 judgment is upheld after adversarial audit. The paper's final goal is to accurately identify ADL performers in multi-resident object-sensor settings; the core evidence is exclusively objective classification performance on fixed subject identities. All four quantitative experiments use deterministic classification metrics computed from automatically recorded accelerometer data and preassigned IDs. No questionnaire/self-report/user-rating is a core outcome. The qualitative case study is supplemental and does not make the core claim mixed. The artifact is a substantive CNN architecture plus a transfer-learning algorithm, and comparative improvements over classical ML, alternative CNNs, no-transfer, and source-activity ablations are statistically demonstrated. The only boundary consideration is that identity labels were originally human-chosen subject IDs, but this falls under the frozen-label benchmark exception, not under human semantic evaluation of generated outputs.

## Semi-Supervised Cyber Threat Identification in Dark Net Markets: A Transductive and Deep Learning Approach

- Record: 712
- Year / journal: 2020 / Journal of Management Information Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 经反向审计，未发现非客观的核心成功指标。核心贡献是提高暗网市场威胁文本分类的F1/精确率/召回率/准确率/AUC，全部基于132条预先专家标注的验证集计算，属于冻结标签上的计算benchmark。定性示例仅为辅助说明，管理启示为推测性陈述。制品设计和相对于多个baseline的显著改善均成立，因此维持正例。

## Understanding Security Vulnerability Awareness, Firm Incentives, and ICT Development in Pan-Asia

- Record: 12356
- Year / journal: 2020 / Journal of Management Information Systems
- Status / role: fully_objective / exclusive
- Reason: 按全文反向审计，所有核心成功结果均来自外部自动安全数据源（CBL、PSBL、APWG、OpenPhish）及其确定性变换（log、PCA、Borda rank），没有自报、人工语义评分或总体主观评价；文中存在可识别的软件制品（数据收集、映射、排名和通报系统），并用随机对照组和 DID/2SLS 等比较展示了多个客观指标的显著改善。虽然平均钓鱼效应不显著，但这是研究结论的一部分，且非托管企业和高 NRI 国家子样本均有显著客观改善。因此维持严格匹配判定。

## Protecting Privacy When Sharing and Releasing Data   with Multiple Records per Person

- Record: 2834
- Year / journal: 2020 / Journal of the Association for Information Systems
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现推翻初筛的证据。文章核心贡献是设计并验证了一个多记录每人的数据匿名化算法/计算程序，以g-balance和h-affiliation作为披露风险度量、以ANE作为数据质量度量；所有核心成功指标均从数据集记录、计数和QI泛化结果经确定性公式计算，无任何主观评分、自报或人工语义判断。与k-anonymity、PID-based K-anonymity和l-diversity的广泛实验比较证明了其改善。因此确认严格匹配。

## Who Is the Next “Wolf of Wall Street”? Detection of Financial Intermediary Misconduct

- Record: 790
- Year / journal: 2020 / Journal of the Association for Information Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 反向审计未发现足以推翻初筛的证据。论文的核心成功结果全部基于固定FINRA BrokerCheck标签上的确定性分类指标（accuracy/recall/precision/F1/AUC、McNemar检验）以及由监管赔偿/罚金确定性计算的经济收益；没有任何主观评分、自报结果、人工语义编码或总体质量判断作为核心结局。人工假档案筛查和档案分类只是预处理步骤，删除后不影响核心结论。软件制品为多种机器学习分类器，并且通过naive、A/B/C/D/E/F配置、不同机器学习技术和经济敏感性分析证明了客观改善。因此，五个门槛均通过，属于固定标签基准上的完全客观核心贡献。

## X-IM Framework to Overcome  Semantic Heterogeneity Across XBRL Filings

- Record: 8372
- Year / journal: 2020 / Journal of the Association for Information Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: The stage-1 positive verdict survives reverse audit. The paper's core contribution is a concrete, implemented software artifact (X-IM) whose stated research question is to accurately map XBRL tags to financial concepts in an upper-level ontology. All formal hypotheses and main success outcomes are precision, recall, and F-measure computed against a fixed target mapping frame of reference. The target mappings and investor's ontology are constructed from an authoritative accounting textbook but are used as frozen reference labels, not as subjective ratings of X-IM's outputs. The artifact is compared against the FinCEM baseline and against a no-ontology ablation, with statistically significant improvements. No subjective, self-report, human semantic quality, or mixed co-primary contribution is required for the core success claim.

## A Data Analytics Framework for Smart Asthma Management Based on Remote Health Information Systems with Bluetooth-Enabled Personal Inhalers

- Record: 16100
- Year / journal: 2020 / MIS Quarterly
- Status / role: fully_objective / exclusive
- Reason: 本研究的核心目标不是改善临床结局或用户满意度，而是设计并验证一个针对SAM数据的计算检测框架。其最终和主要成功依据是客观检测性能指标：AUC被明确列为主要绩效指标，误报/漏报率和报警时间是同一检测任务的辅助核心指标。这些指标都来自蓝牙传感器自动记录的事件时间戳、确定性的数据替换构造情景和计算公式，不依赖专家或用户对输出质量的主观评分。ACT自报分数仅作为建模协变量和描述性分组变量，未进入核心成功主张。文章通过GLMM-GQP与六种基准方法的系统性比较（表4和图9）展示了相对改善，因此五个门槛全部满足，objective_status为fully_objective，core_role为exclusive，confirmed_strict_match为true。

## Can Recommender Systems Reduce Healthcare Costs? The Role of Time Pressure and Cost Transparency in Prescription Choice

- Record: 5368
- Year / journal: 2020 / MIS Quarterly
- Status / role: fully_objective / dominant
- Reason: 初筛为严格客观正例是正确的。论文的核心贡献是设计并实验评估成本敏感的临床推荐系统，证明其不同成本框架设计（低成本 vs 混合成本）对处方调整行为有显著影响。主要结果指标是系统自动记录的处方调整率和推荐查看率，完全客观。访谈和操纵检查属于辅助性质，不构成核心成功主张；护士/医师助理实验中的语义总结评估是数据质量筛查，不影响结局指标。虽然缺少无推荐对照组，但核心论证基于系统两种设计变体的比较，符合软件制品改进比较的要求。因此五个门槛全部通过，客观指标占主导。

## Taming Complexity in Search Matching: Two-Sided Recommender Systems on Digital Platforms

- Record: 27582
- Year / journal: 2020 / MIS Quarterly
- Status / role: fully_objective / exclusive
- Reason: 经全文反向审计，初筛结论仍然成立。文章的核心贡献是以agent-based simulation设计并评估一个two-sided recommender system软件制品，旨在驯服平台上不可约的不确定性并提升学生/大学fitness。所有核心成功结果——AIC比较、学生平均fitness、大学平均fitness——均由仿真程序输出和统计计算得到，不依赖真实用户主观评分、自报、专家编码或人工语义判断。研究明确比较了no recommender、one-sided和two-sided三种方案，且统计检验显著。因此五个门槛全部通过，属于完全客观指标核心主导的严格正例。

## A cross-domain recommender system through information transfer for medical diagnosis

- Record: 19686
- Year / journal: 2021 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 初筛成立。文章核心贡献是提出ITMD跨域推荐系统，以目标域疾病风险预测准确率为最终优化目标和成功依据。该指标按确定性公式计算，比较对象是固定诊断类别标签（合成数据中的生成标签和真实数据中医生基于TI/BI-RADS给出的标签），属于冻结标签基准。全文未将主观满意度、自报或人工语义质量评分作为核心结果。与B1-B4基线、源域-only模型及不同距离度量的比较均显示客观改善，因此通过五道门槛。

## A dynamic simulation approach to support the evaluation of cyber risks and security investments in SMEs

- Record: 19788
- Year / journal: 2021 / Decision Support Systems
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现足以推翻初筛的证据。所有核心成功指标（收入损失、防御能力、成本+损害、统计检验）都来自 SMECRA 模型公式和模拟运行，不是问卷/自报/人工质量评分；Snapshot Survey 只是初始化输入，删除它并不破坏模拟比较的核心主张。文章通过基本方法对比及 Alpha/Beta 情景对比（t 检验 p=0.022）证明投资策略可显著降低客观经济成本，因此符合完全客观指标和软件制品改善标准。

## A new approximate belief rule base expert system for complex system modelling

- Record: 19766
- Year / journal: 2021 / Decision Support Systems
- Status / role: fully_objective / dominant
- Reason: 经反向审计，未发现足以推翻初筛的主观核心结果或人工质量判断。核心成功主张（建模精度、结构紧凑性、有限数据优势）全部基于客观测量：MSE 来自仪器直接测量的容量与模型输出的确定性公式，规则数来自确定性计数。专家知识仅用于参数初始化和模型结构设计，未作为结果评估。可解释性/扩展性的定性讨论删除后，核心结论依然完整。制品明确（ABRB）且通过多种基线、消融式前后比较和不同数据比例实验证明客观改善。虽然文章同时强调 interpretability，但它不是被测量的结果指标，未动摇客观核心的主导地位。

## A novel decision support system for optimizing aircraft maintenance check schedule and task allocation

- Record: 19756
- Year / journal: 2021 / Decision Support Systems
- Status / role: fully_objective / dominant
- Reason: The audit confirms the initial positive screening. The paper's core contribution is a concrete DSS that improves objectively measurable aircraft maintenance scheduling and task allocation: higher check utilization, fewer checks, lower estimated maintenance costs, faster planning, and near-optimal task allocation. These core results are deterministic outputs of optimization models, schedules, usage data, solver comparisons, and financial formulas. Airline expert qualitative comments are present but secondary; deleting them does not weaken the core objective success claim. The subjective validation of AMPO-3 shift planning is a limitation but does not make the primary contribution mixed-objective.

## A personalized paper recommendation method considering diverse user preferences

- Record: 19758
- Year / journal: 2021 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 初筛结论成立。全文以提出并验证计算型推荐算法 PRHN 为核心贡献，最终目标是提高论文推荐的 Precision 和 Recall。评测完全基于 Aminer/DBLP 真实引用记录形成的固定隐式反馈标签，离线计算客观指标，不存在人工对推荐结果质量的主观评估、自报满意度或人工语义编码。文中唯一的说明性内容（如 Table 3 展示个别用户的权重）只是解释个性化，不构成核心成功证据；删除后核心结论仍然完整。与多个基线在两组数据上的比较明确报告了 Precision/Recall 的客观改善。因此五条门槛均满足，属于 fixed-label benchmark，核心角色 exclusive。

## A prescriptive analytics framework for efficient E-commerce order delivery

- Record: 19796
- Year / journal: 2021 / Decision Support Systems
- Status / role: fully_objective / exclusive
- Reason: 全文核心成功主张完全围绕客观可测量结果：预测模型在真实历史配送标签上的标准分类性能、调度模拟中的总尝试次数、车辆数、总距离和总成本节省。不存在主观量表、满意度测量、用户自报或人工语义质量编码作为核心结果。配送标签是平台实际配送事件的记录，冻结后用于模型评估，属于固定标签 benchmark 范畴；成本/尝试/车辆结果由确定性模拟和成本公式计算，不依赖人的主观评价。文章明确实现两阶段框架中的预测模型、订单成功画像和 VRPTW 启发式算法，并与当前行业最短路径 baseline 进行了比较，证明了客观改善。因此通过全部反向审计门槛。

## A strategic decision-making architecture toward hybrid teams for dynamic competitive problems

- Record: 19688
- Year / journal: 2021 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: Preliminary inclusion is upheld. The paper designs and implements a computational decision-making architecture and task-partitioning methods. All core reported outcomes are computed from fixed objective game logs and derived reward models, not from human rating, self-report, or subjective scoring. The core contributions—conservative game-theoretic suggestions and partition-based improvement over all-in-one—are exclusively supported by these quantitative metrics. The frozen-label benchmark exception legitimately applies because the labels are binary wins/losses, and the models are evaluated computationally against those fixed labels, without any human semantic judgment of generated outputs.

## Analytics with digital-twinning: A decision support system for maintaining a resilient port

- Record: 19700
- Year / journal: 2021 / Decision Support Systems
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现可推翻初筛的证据。全部核心成功指标均由数字孪真仿真BoA输出、确定性公式或bootstrap统计计算；专家/运营者输入仅用于外生算例构造和背景验证，不评价任何输出质量。文章明确设计/修改了DSS及其仿真与OCBA模块，并通过默认行动、确定性模型、等量分配三类对照证明了客观改善。因此保留初筛严格匹配结论。

## Applied machine learning for a zero defect tolerance system in the automated assembly of pharmaceutical devices

- Record: 19748
- Year / journal: 2021 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 经反向审计，未发现足以推翻初筛的主观性/混合贡献/指标非核心问题。核心成功证据均由固定工业传感器标签上的分类指标和运行时测量构成，符合冻结标签benchmark例外；软件制品明确且经过多组配置/消融比较和预定阈值验证。因此确认严格匹配。

## Bayesian Stackelberg games for cyber-security decision support

- Record: 19808
- Year / journal: 2021 / Decision Support Systems
- Status / role: fully_objective / exclusive
- Reason: 初筛判定成立。该文的核心目标是提出并实现一个精确、可扩展的在线贝叶斯 Stackelberg 安全防御优化算法，并以此为安全决策支持系统的关键部分。其成功证据全部来自客观计算指标：求解时间、优化变量数量和由概率攻击图模型计算的期望安全风险；不存在自报、问卷、人工语义评分或专家对输出质量的总体评价作为核心证据。相对 DOBSS/HBGS/HUNTER/Harsanyi 变换以及 [1] 的方法，论文展示了明确、可计算的改善。案例研究中的部分输入参数是估计值、且缺少真实部署验证，这影响外部效度，但不改变核心指标本身的计算客观性。

## Capital shortfall: A multicriteria decision support system for the identification of weak banks

- Record: 19736
- Year / journal: 2021 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 反向审计未推翻初筛：论文最终目标是预测监管资本需要分类，以固定标签上的OCA/ACA/AUROC/SENS/SPEC为主要成功依据；所有核心结果来自确定性公式和固定监管标签，无主观或自报共主指标。同时与LR/SRISK/Texas Ratio的系统比较证明了客观改善。唯一风险是‘DSS软件界面’未被交付，但算法/模型作为DSS核心组件符合制品门槛。

## Classifying the ideational impact of Information Systems review articles: A content-enriched deep learning approach

- Record: 19638
- Year / journal: 2021 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / dominant
- Reason: 初筛结论可保留。文章的核心贡献是设计并评估 Deep-CENIC 这一自动分类/推荐软件制品，核心成功指标是对预先固定的人工编码 ideational 标签的 precision/recall/F1，并显著超过多个 baseline。人工编码标签属于冻结标签上的计算 benchmark，适用例外。Section 5 的定性知识增长分析为说明性补充，删除后不影响核心分类性能主张。因此确认严格客观指标正例。

## Decisions for information or information for decisions? Optimizing information gathering in decision-intensive processes

- Record: 19850
- Year / journal: 2021 / Decision Support Systems
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现足以推翻初筛的证据。核心成功结果（期望利润、期望收入、实例级利润）均由确定性公式、概率分布和成本参数计算得出，不依赖主观评分、自报或人工语义质量判断；对照基线为当前实践的人工决策树，比较显示了期望利润翻倍的客观改善。制品是实际实现的MDP优化器和推荐器，满足全部五个严格门槛。

## Filaments of crime: Informing policing via thresholded ridge estimation

- Record: 16562
- Year / journal: 2021 / Decision Support Systems
- Status / role: fully_objective / exclusive
- Reason: 全面审计后确认初筛正确。文章核心目标是通过DREDGE提取密度脊线作为巡逻路线模板，并以2019年犯罪事件的几何覆盖率为主要成功依据。覆盖率及比较指标均来自官方行政犯罪坐标和确定性几何计算，无主观评分、自报或人工语义编码。存在少量目视KDE重合检查，但属于次要机制性验证，不构成核心成功主张。制品明确且通过随机路线/热点中心点比较证明了改善，因此严格匹配。

## Inferring multi-stage risk for online consumer credit services: An integrated scheme using data augmentation and model enhancement

- Record: 19830
- Year / journal: 2021 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 初筛判定基本成立。文章核心成功主张是：通过手机使用数据增强和多阶段模型增强，提升在线消费信贷风险预测的客观性能（micro-averaged AUC、CEM），并带来平台利润（EMP）与消费者机会（误拒分布）改进。目标标签由还款逾期天数客观规则生成，主要指标为冻结标签上的计算基准与确定性利润公式；消费者福利分析中的手工信用评级仅作为分组变量，不构成对制品输出质量的人工评分或主观成功指标。SHAP人格解释和理论讨论为次要机制内容，删除后核心成功主张仍完整。因此通过反向审计。

## Model identification for ARMA time series through convolutional neural networks

- Record: 16564
- Year / journal: 2021 / Decision Support Systems
- Status / role: fully_objective / exclusive
- Reason: 初筛判定成立。全文未发现任何主观、自报、人工作业或人工质量判断；所有核心结果均来自程序生成的模拟ARMA时间序列和已知ground truth，指标为精确的识别准确率、MSE、计算时间及预测MAE/RMSE。论文的核心贡献是设计并训练CNN作为ARMA模型识别制品，并与AIC/BIC基线在同一测试套件上比较，在识别精度、MSE、速度和预测误差方面客观证明了改善。少量结果（10,000长度下both-correct accuracy和MA accuracy不如BIC full）不推翻整体核心主张，因为论文的主要成功依据是多维客观指标，且CNN在速度和MSE上的优势非常显著。

## New algorithms for automatic modelling and forecasting of decision support systems

- Record: 19798
- Year / journal: 2021 / Decision Support Systems
- Status / role: fully_objective / exclusive
- Reason: 初筛判定正确。文章的核心贡献是提出并实现UCA自动识别算法（明确软件制品），核心目标是提升DSS所依赖的时间序列预测精度，所有成功评估均基于真实观测数据与预测值计算的MASE、RMSE、MAE、sMAPE等完全客观指标。全文不存在自报、主观评分、人工语义判断或混合主观核心。通过在西班牙IPI和大型零售销售数据集上的滚动预测实验，UCA在IPI MASE上全面优于ARIMA、Theta、ETS、BSM，在零售RMSE上全面最优；预测组合（Median/M-ARIMA）也在MASE上优于所有单一方法，并经秩检验支持。五个门槛全部满足，核心角色为exclusive。

## Peak cubes in service operations: Bringing multidimensionality into decision support systems

- Record: 19642
- Year / journal: 2021 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 反向审计未发现推翻初筛的证据。全文没有任何主观核心结果或自报数据；核心成功证据是模拟生成的固定流失标签上计算的AUROC比较，属于冻结标签计算benchmark例外。PeakCube算法、特征工程和预测模型构成明确软件制品；相对单维峰值模型在4000个模拟场景中以AUROC显著改善，比较充分。Shapley值解释仅用于辅助说明，删除后核心成功主张仍完整。因此确认严格匹配。

## Predicting donation behavior: Acquisition modeling in the nonprofit sector using Facebook data

- Record: 19646
- Year / journal: 2021 / Decision Support Systems
- Status / role: fully_objective / exclusive
- Reason: 初筛判定成立。文章以预测真实首次捐赠行为为核心，目标标签来自NPO内部实际捐赠记录，而非自报或人工编码；所有核心效果指标AUC/TDL均为确定性计算。研究明确通过DR技术与算法组合的网格比较，证明SVD+LR相对binary baseline和其他组合有客观提升。唯一的‘人工解读’出现在将SVD维度解释为年龄、居住地、物质主义等特征时，该解读只是辅助性洞察，不构成效果度量，也不与客观核心指标并列。

## Prediction of initial coin offering success based on team knowledge and expert evaluation

- Record: 19776
- Year / journal: 2021 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 经反向审计，未发现足以推翻初筛的主观、自报或人工质量判断。本文核心目标是设计并验证一个ICO成功预测模型，所有核心成功结果均为分类性能指标（Accuracy、Precision、Recall、F1），指标计算基于固定且客观的成功/失败标签（实际募资额与soft cap比较）。输入特征中包含专家评分和评论文本等人类生成数据，但仅作为预测输入，不构成对模型输出的主观评价。冻结标签例外适用。制品设计（A-BiRNN、知识度量等）明确，并与多个基线和先前工作进行了系统比较，客观指标显示明确改善。因此，确认严格匹配。

## Process data properties matter: Introducing gated convolutional neural networks (GCNN) and key-value-predict attention networks (KVP) for next event prediction with deep learning

- Record: 19696
- Year / journal: 2021 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 全文反向审计确认：核心成功主张完全由基于现实事件日志固定活动标签的Accuracy、Precision、Recall、F1等客观分类指标支撑；数据来源是系统记录的客观事件日志，不涉及问卷、自报或人工质量评分。过程数据属性、泛化、类别不平衡、聚焦和增强分析均是建立在客观指标之上的解释性/辅助分析，删除后不影响‘GCNN和KVP在大多数基准组合上超越既往方法’的核心主张。制品GCNN/KVP有明确架构设计和实现，并通过多数据集、多指标及统计检验相对于LSTM、SAE、MANN、CNN等基准证明多数占优。初始暂定正例经审计仍成立，不属于假阳性。

## Providing more regular road signs infrastructure updates for connected driving: A crowdsourced approach with clustering and confidence level

- Record: 19644
- Year / journal: 2021 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: The reverse audit confirmed that the article's core contribution is a computational software artifact for consolidating crowdsourced road-sign detections and estimating their existence probability. The final success claims are entirely supported by precision, recall, and false positive/negative rates computed against fixed manual ground-truth road sign positions; this falls under the frozen-label benchmark exception. No subjective, self-report, or human semantic quality outcome is used as a core success metric, and removing all qualitative implications leaves the claimed contribution intact. Comparative improvement over camera-only detections and a camera-only simulated system is clearly demonstrated. Therefore the strict match is confirmed.

## S2SAN: A sentence-to-sentence attention network for sentiment analysis of online reviews

- Record: 19811
- Year / journal: 2021 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 反向审计未发现推翻初筛的证据。文章提出并实现S2SAN软件模型/算法，核心贡献是提升情感分类准确率和训练效率。所有核心成功指标均为在固定情感/领域标签上的可计算预测准确率或系统记录的训练时间；不存在自报、问卷、用户评分、人工语义质量判断等主观测量。冻结标签benchmark例外适用，因为评价对象是计算模型对固定ground truth标签的预测性能。因此五个门槛全部通过，应维持strict match。

## Session stitching using sequence fingerprinting for web page visits

- Record: 19787
- Year / journal: 2021 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 初筛结论可确认。文章的核心经验贡献是提出并评估基于序列指纹的会话拼接方法：其匹配性能用 F1 和 AUC 测量，特征效率用 |F| 衡量，数据来源是真实 Google Analytics 会话日志，标签是系统预先分配的 visitor ID，属于冻结标签上的分类基准，不依赖人工评分、问卷、自报或语义质量判断。它与 user-agent 特征方法和 node2bits 嵌入方法进行了明确比较，显示其在 F1/AUC 上优于 node2bits，并以低得多的特征维度达到可用匹配性能。可解释性、隐私性和管理启示属于定性优势论述，删除后不影响核心经验结论。因此五个门槛全部满足，objective_status 为 benchmark_objective_with_fixed_labels，core_role 为 exclusive。

## Simpler is better: Lifting interpretability-performance trade-off via automated feature engineering

- Record: 19762
- Year / journal: 2021 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 反向审计未发现足以推翻初筛的主观/自报/人工语义核心结果。文章的核心成功结果由两类完全客观指标构成：固定标签benchmark上的AUC和模型参数计数代理的可解释性。SAFE方法有明确软件实现，并且在use case和30个OpenML数据集上与vanilla logistic regression和supervisor复杂模型进行了比较，证明在AUC不显著下降的同时显著提升可解释性，甚至在use case中同时提升AUC和可解释性。因此五个门槛全部成立，维持strict_match=true。

## DNCP: An attention-based deep learning approach enhanced with attractiveness and timeliness of News for online news click prediction

- Record: 20317
- Year / journal: 2021 / Information & Management
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 初筛判定正确。文章以预测新闻点击量类别为任务，通过设计DNCP模型实现了基于实际点击量和确定性阈值标签的分类预测。所有核心成功结果均采用Precision、Recall、F1和Accuracy等客观分类指标，数据来源于平台系统日志，无任何主观评分或人工语义判断。模型通过多基线对比和消融实验证明了显著改进，所有客观指标均为最终优化目标和主要成功依据，因此确认严格匹配。

## Predicting product adoption intentions: An integrated behavioral model-inspired multiview learning approach

- Record: 20385
- Year / journal: 2021 / Information & Management
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: The stage-1 positive decision is upheld. The paper's core contribution is the design, implementation, and comparative evaluation of a concrete multiview deep learning classifier for predicting product adoption intentions. All final success claims are based on deterministic classification metrics against fixed manually labeled target labels, which falls within the frozen-label benchmark exception. The IBM theory is used only as conceptual inspiration; no self-report scales or subjective outcome ratings are measured. The artifact is improved relative to multiple baselines and ablations. Therefore confirmed_strict_match=true.

## A Graph-Based Ant Algorithm for the Winner Determination Problem in Combinatorial Auctions

- Record: 28214
- Year / journal: 2021 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: 初筛暂定正例经反向审计后仍成立。全文核心成功主张为TrACA在限时条件下提高WDP求解质量和效率，其所有核心最终结果均为程序自动计算的解收益、运行时间、OSP和统计推断，无任何人工评分、自报或主观编码。制品设计与比较改进均充分：提供了详细伪代码、设计机理，并与20种启发式和2种精确算法在94个公开实例上进行了系统比较，证明实质性改善。因此，满足全部五个严格客观门槛，应确认为严格匹配正例。

## Designing Personalized Treatment Plans for Breast Cancer

- Record: 28168
- Year / journal: 2021 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现足以推翻初筛的证据。文章核心贡献是设计个性化放疗计划优化框架，以相同TCP为约束最小化平均剂量，所有核心成功结果均源于模拟公式、优化算法、固定文献参数和客观算术，不含对输出方案的主观质量评分；与标准均匀计划和多种优化算法比较均显示客观改善。因此维持stage1的严格正例判定。

## Dynamic, Multidimensional, and Skillset-Specific Reputation Systems for Online Work

- Record: 28018
- Year / journal: 2021 / Information Systems Research
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 反向审计未发现推翻初筛的证据。全文核心成功主张均围绕声誉排序、非完美工人识别、职位内排名、推荐 AUC 和分布形状等指标，这些指标要么使用平台记录的冻结反馈标签作为基准，要么是确定性计算指标。雇主反馈分数虽然由人类产生，但属于冻结标签预测基准，不涉及人工评价干预后文本或设计质量，因此符合固定标签例外。同时文章实质设计和比较了 HMM-W2V 制品，并在多个基线上证明了显著客观改善。

## Estimating the Impact of “Humanizing” Customer Service Chatbots

- Record: 28188
- Year / journal: 2021 / Information Systems Research
- Status / role: fully_objective / dominant
- Reason: 初筛结论成立：文章以客服聊天机器人为明确软件制品，核心目标是通过受控现场实验估计拟人化设计对交易转化率这一完全客观行为结果的影响，并同时估计报价敏感性。主结果和复制结果均基于系统日志客观衡量，并与控制组比较证明改善。主观操纵检查和机制探索属于辅助性证据，删除后核心成功主张依然完整成立。

## How to Assign Scarce Resources Without Money: Designing Information Systems that are Efficient, Truthful, and (Pretty) Fair

- Record: 27998
- Year / journal: 2021 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现推翻初筛的证据。论文核心贡献是设计并实现RESPCT匹配机制，以同时实现策略真实性、Pareto效率和低水平的justified envy。所有核心成功指标（justified envy实例数、有嫉妒学生数、被嫉妒学生数、平均排名/排名分布、Pareto改进比例）均由输入偏好和优先级经确定性算法计算，没有任何对匹配结果的主观评分、满意度或人工质量编码。学生/教师偏好是问题的输入参数而非制品效果的自报测评。文章与ESTTC、ESPCT和ESDA在10个TUM真实数据集上进行了系统比较，展示了至少3倍的嫉妒减少和明显更高的效率。因此确认严格匹配。

## News-Induced Dynamic Networks for Market Signaling: Understanding the Impact of News on Firm Equity Value

- Record: 28014
- Year / journal: 2021 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: 初筛正例经反向审计仍成立。全文核心成功主张（H1-H3和交易模拟）均以股票价格、市场指数、因子收益率和交易量等可验证市场数据为来源，经Fama-French三因子、VAR/GIRF/GFEVD和组合模拟等确定性/计量公式产生；人工编码仅用于中间文本挖掘算法的冻结标签训练与验证，删除该部分后市场预测核心主张仍由Table 3-8客观结果完整支撑。文章设计了文本挖掘与动态网络框架，并相对多个基线和稳定网络显著改善了异常收益预测和市场信号价值。五个门槛全部通过。

## Designing Effective Mobile Health Apps: Does Combining Behavior Change Techniques Really Create Synergies?

- Record: 25407
- Year / journal: 2021 / Journal of Management Information Systems
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现推翻初筛的证据。文章以explanatory design theorizing为方法，实质设计并修改了四种mHealth软件原型；核心研究问题与假设H1/H2/H3直接以系统自动记录的实际使用行为——训练完成次数和应用打开次数——为依赖变量，并通过2x2随机现场实验（n=138）和ANCOVA稳健性检验证明：单独社会向上比较和保护动机显著提高客观使用，二者组合产生负交互并降低使用。所有自报操纵检查、开放反馈编码和定性访谈仅用于操纵确认、机制解释和补充佐证；将它们全部删除后，核心成功主张仍由客观日志完整支持，因此不存在混合核心贡献、主观核心结果或指标附属化问题。

## Fall Detection with Wearable Sensors: A Hierarchical Attention-based Convolutional Neural Network Approach

- Record: 25440
- Year / journal: 2021 / Journal of Management Information Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 初筛判定成立。本文提出并实现了HACNN模型，核心目标是提高基于可穿戴传感器数据的跌倒检测性能。全部核心成功结果均为F-measure、Precision、Recall，来源是对公开数据集MobiFall和UMAFall中预先固定fall/non-fall标签的自动预测比较，属于冻结标签上的计算基准，不涉及人对模型产出质量的主观评分。通过与多种经典机器学习和深度学习baseline、消融分析、数据规模与噪声实验的比较，HACNN的客观改善得到证明。注意力权重案例研究只是解释性说明，不是核心成功指标，删除后不影响主要结论。

## Handling the Efficiency–Personalization Trade-Off in Service Robotics: A Machine-Learning Approach

- Record: 25398
- Year / journal: 2021 / Journal of Management Information Systems
- Status / role: benchmark_objective_with_fixed_labels / dominant
- Reason: The paper's core technical contribution is a software/ML artifact with two principal objectively measured success outcomes: energy-efficiency prediction error and preference-estimation error, both evaluated against strong baselines on two datasets. The energy-efficiency metric is fully objective. The preference-estimation metric is a prediction benchmark using fixed recorded user behavior labels, which falls under the frozen-label exception. The willingness-to-pay survey is supplementary and not a core success claim. Although the overall trade-off module is not empirically tested and the preference labels derive from subjective human choices, these facts do not overturn the core objective evaluation. The gates are therefore satisfied.

## The Effectiveness of Social Norms in Fighting Fake News on Social Media

- Record: 25392
- Year / journal: 2021 / Journal of Management Information Systems
- Status / role: fully_objective / dominant
- Reason: 初筛判定被确认。文章的核心研究问题是社会规范消息是否提高社交媒体用户的假新闻举报行为；主要因变量由实验系统自动记录的举报点击次数构成，属于完全客观行为测量。研究通过自开发新闻流接口加入报告按钮和社会规范消息，并相对无规范对照、单一规范和规范强度基线进行回归比较，证明组合规范显著改善假新闻举报行为。Study 2中的Likert真实性判断和自报动机/障碍问卷是辅助探索，删除后核心成功主张仍完整，因此不构成混合核心主张。维持严格匹配。

## Unveiling the Hidden Truth of Drug Addiction: A Social Media Approach Using Similarity Network-Based Deep Learning

- Record: 25390
- Year / journal: 2021 / Journal of Management Information Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 经反向审计，初筛结论成立。论文的核心贡献是设计并验证SINDEL这一深度学习文本分析系统，使其在提取OUD治疗障碍和用药依从性障碍时显著优于多个baseline。评估使用预先冻结的专家IOB标签，计算precision/recall/F1，属于冻结标签基准例外。聚类后的13类障碍专家验证虽然包含人工语义判断，但它是领域发现的辅助验证，不影响SINDEL相对于baseline的客观提取性能这一核心成功主张；删除该步骤后，核心贡献完整。因此五个门槛均通过，objective_status为benchmark_objective_with_fixed_labels，core_role为exclusive。

## Design Principles for Robust Fraud Detection:  The Case of Stock Market Manipulations

- Record: 9230
- Year / journal: 2021 / Journal of the Association for Information Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 初筛判定正确。文章以设计并实现鲁棒欺诈检测分类器为核心目标，核心成功证据全部是对固定可疑/非可疑标签的确定性分类性能指标（naive和攻击模拟）。标签预先基于SEC标准和来源固定，没有人工评级或主观结果作为核心贡献。删除专家访谈、定性讨论和描述性统计后，核心主张仍然完整。因此属于冻结标签基准的完全客观改进型设计科学研究。

## Finding a Needle in the Haystack: 
Recommending Online Communities on Social Media Platforms Using Network and Design Science

- Record: 14346
- Year / journal: 2021 / Journal of the Association for Information Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 反向审计未发现推翻初筛的证据。该文核心贡献是基于网络特征和一般社区特征改进在线社区推荐，所有核心成功主张均来自基于Twitter历史订阅日志的固定标签检索/推荐性能指标（Precision、Recall、F-score、MRR、DCG），无主观评价或人工语义质量编码。制品是明确的推荐模型和特征提取算法，并且通过Table 7的多重基线比较证明了客观改进。因此五个门槛全部满足，确认为严格匹配。

## A Deep Learning Approach for Recognizing Activity of Daily Living (ADL) for Senior Care: Exploiting Interaction Dependency and Temporal Patterns

- Record: 8316
- Year / journal: 2021 / MIS Quarterly
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 初筛判定得到全文支持。文章以设计并实现ADL识别软件制品为研究目标，四个核心实验均使用固定标签上的计算指标（F1、Accuracy、ABLD、Acc@1/Acc@2）作为主要成功依据，并与多个基线/基准模型进行了系统性比较和显著性检验。人工标签属于冻结标签，而非对模型输出质量的主观评分；删除案例研究和定性讨论后，核心成功主张仍然完整。

## Assessing the Unacquainted: Inferred Reviewer Personality and Review Helpfulness

- Record: 13152
- Year / journal: 2021 / MIS Quarterly
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: Initial strict-match decision survives reverse audit. The paper's core objective is to develop and evaluate an IT artifact for inferring reviewer personality and using it to predict future review helpfulness. All core success determinations come from Yelp's logged helpfulness votes and deterministic classifier/regression computations. The prediction evaluation uses frozen threshold-based labels derived from logged votes, which falls within the fixed-label benchmark exception. The CNN personality model and ensemble-of-ensembles predictor are explicitly designed/modified software artifacts, and the predictive model is compared against a benchmark with substantial recall/precision improvements. No core outcome rests on self-reports, expert ratings, or human semantic coding. Thus all five gates are satisfied.

## Leveraging Multisource Heterogeneous Data for Financial Risk Prediction: A Novel Hybrid-Strategy-Based Self-Adaptive Method

- Record: 8114
- Year / journal: 2021 / MIS Quarterly
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 初筛通过。文章以提升金融风险预测性能为最终目标，通过设计HSB_RS方法（实质软件制品）并在两个真实数据集上相对9个基线证明了客观性能指标的显著提升。所有核心成功结果（AUC、KS、Gini、F1）均基于预先冻结的客观事实标签（逾期超过120天、ST监管状态）计算，不涉及人工对产出质量或文本语义的评分。存在的人工词典翻译和手动文本检查仅为特征构建/解释性辅助，删除后不影响核心结论。混合贡献、主观结果、指标非核心、制品不实等假阳性风险均不成立。

## Will Humans-in-the-Loop Become Borgs? Merits and Pitfalls of Working with AI

- Record: 186
- Year / journal: 2021 / MIS Quarterly
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 初筛维持。论文所有核心假设（H1a-b、H2a-b、H3a-b、H4a-c）都以基于ImageNet固定标签的人类准确率、独特人类知识和由真实分类数据模拟的群体准确率为因变量，均为完全客观或固定标签基准测量。主观信任问卷和自报置信度仅用于机制解释，不是成功指标。系统层面实质设计了AI建议展示、确定性提示和个性化建议规则，并通过实验和模拟进行条件比较，显示客观改善或非劣且独特知识改善。未发现足以推翻初筛的主观核心结果或混合核心贡献。

## A decision analytic approach for social distancing policies during early stages of COVID-19 pandemic

- Record: 19845
- Year / journal: 2022 / Decision Support Systems
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现推翻初筛的证据。全文核心成功指标全部来自确定性/随机仿真的客观计算输出（死亡数、住院数、CAR、峰值和峰时），不存在问卷、自报、专家评分或人工语义质量判断。经济/社会成本讨论仅为背景，不构成共同核心贡献。模型输入中的CDC病例数据和文献参数是建模和校准输入，不违反客观性。文章明确设计了决策分析仿真工具，并通过与无干预、不同触发阈值、不同关闭时长及不同重开策略的系统比较证明了客观指标的改善（如降低死亡、CAR、住院峰值，延迟峰时）。因此，五个门槛全部满足，objective_status为fully_objective，core_role为exclusive，confirmed_strict_match为true。

## A deep recurrent neural network approach to learn sequence similarities for user-identification

- Record: 19928
- Year / journal: 2022 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 初筛判定成立。文章核心贡献是设计并实现了一个深度学习序列相似度框架，并在用户再识别任务中验证其性能。所有核心成功结果均为自动计算且与Comscore面板的固定用户身份标签比较：再识别成功率、ARI、完美聚类比例、精确率和召回率。未发现主观评分、自报结果或人工语义质量判断作为核心指标。TL-RNN相对Smith-Waterman和TF-RW在再识别任务上取得一致客观改进，并提供了开源实现。因此满足全部五个门槛，确认严格客观指标正例。

## An interactive decision support system for real-time ambulance relocation with priority guidelines

- Record: 19916
- Year / journal: 2022 / Decision Support Systems
- Status / role: fully_objective / dominant
- Reason: 确认初筛。文章提出并实现了明确的DSS软件制品，核心目标是通过优化救护车重定位提高完全客观的运营结果指标；ANAA、ACR、ART、AWA、TWAA均基于真实呼叫数据、模拟调度活动时间等确定性来源计算，无人问卷、自报或人工语义编码作为核心成功指标。文中模糊AHP权重、RRARR主观特征和专家权重只属于模型参数/辅助指导，删除后基于表8-11的客观改进结论仍完整；与现有静态政策SP的比较证明改善，因此满足全部严格门槛。

## Analysis of third-party request structures to detect fraudulent websites

- Record: 19904
- Year / journal: 2022 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: Stage 1's strict-match verdict is confirmed. The paper's core contribution is a predictive classification system for fraudulent website detection, evaluated exclusively with confusion-matrix metrics on fixed legit/fraud website labels. The human-curated label lists are frozen benchmark ground truth, not subjective quality ratings of model outputs, so the frozen-label exception applies. No self-report, expert rating, or human semantic judgment appears as a core outcome. The software artifact is clearly implemented (request capture, structure extraction, variable construction, classifiers, and ensembles), and objective improvements over naive and prior baselines are demonstrated across multiple metrics and models.

## Combining review-based collaborative filtering and matrix factorization: A solution to rating's sparsity problem

- Record: 19948
- Year / journal: 2022 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 反向审计未发现可推翻初筛的证据。文章设计并实现了RMF推荐算法制品，核心目标是解决稀疏评分环境下的推荐准确性问题，所有核心成功结果均为在预存在的用户数值评分这一固定标签上计算的MAE和Precision/Recall/F1，不存在主观量表、用户自报或人工语义编码作为核心结果。虽然人工补充特征种子和主题解释涉及作者判断，但这些仅作为模型输入或过程解释，不是对输出质量或成果价值的评价指标；删除这些成分后核心成功主张仍然完整。因此，该文满足严格客观指标正例的五个门槛，属于冻结标签上的计算基准改进。

## Encoding resource experience for predictive process monitoring

- Record: 19878
- Year / journal: 2022 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 全文核心贡献是提出资源经验特征编码框架并评估其对结局预测性能的影响。所有核心成功证据均为基于固定结果标签的 AUC 比较，特征计算为确定性公式，无主观或人工语义质量评价。SHAP 分析为辅助解释。虽然结果跨数据集不一致，但在 BPIC 2012 和 BPIC 2015_3 等上下文中明确显示了相对基线的 AUC 改善。因此初筛判定成立。

## Explainability and fairness of RegTech for regulatory enforcement: Automated monitoring of consumer complaints

- Record: 19964
- Year / journal: 2022 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 文章以设计科学方法提出并评估了一个 RegTech 文本分类制品，核心成功主张全部基于 CFPB 公开投诉数据库中固定的补偿结果标签，计算 accuracy/precision/recall/F1/McNemar/lift 等指标，属于冻结标签上的预测性能基准。主观 helpfulness 投票仅用于初步特征验证，删除后不影响核心贡献。公平性分析也是基于固定标签上的子组性能。因此维持初筛：strict_match 为 true。

## Fraudulent review detection model focusing on emotional expressions and explicit aspects: investigating the potential of feature engineering

- Record: 16770
- Year / journal: 2022 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 全文核心贡献是特征工程和 M-SMOTE 算法对欺诈评论检测分类性能的提升；所有核心成功主张均由固定标签上的 P/R/F1/AUC 客观指标支撑，没有主观评分、问卷、自报或人工语义质量编码作为共同核心。标签即便部分来自人工/众包或平台过滤，也是用于评估分类模型预测性能的冻结标签，符合基准例外。比较对象包括未预处理、SMOTE/LR-SMOTE、多种 ML baseline 以及已有研究，且全文展示了明确改善。因此初筛判定成立。

## Maximizing student opportunities for in-person classes under pandemic capacity reductions

- Record: 19902
- Year / journal: 2022 / Decision Support Systems
- Status / role: fully_objective / exclusive
- Reason: 初筛判定应维持。论文核心目标是在COVID容量约束下最大化线下授课学生机会；核心结果（线下/混合班级覆盖率、座位数覆盖率、容量失配惩罚）均由优化输出和行政数据确定性计算，无人工评分或主观编码。论文实质设计并部署了该DSS，与贪心基线、替代场景及计算性能比较证明了明显改进。8.2节的学生反馈和7.7节的人工调整仅属定性讨论和部署过程，删除后核心成功主张仍完整，因此不属于混合核心贡献。

## OrdinoR: A framework for discovering, evaluating, and analyzing organizational models using event logs

- Record: 16575
- Year / journal: 2022 / Decision Support Systems
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现推翻初筛的证据。本文核心贡献是提出并实现一个组织模型挖掘与一致性检查框架，核心成功指标 fitness、precision、F1 和局部诊断均来自公开真实事件日志与确定性公式，无主观评分、自报或人工语义编码。论文在 WABO 和 BPIC17 两个真实日志上通过系统配置比较，证明了 OverallScore 相对 FullRecall 在 precision 和 F1 上的客观改善。五个门槛全部满足，objective_status 为 fully_objective，core_role 为 exclusive，因此确认严格匹配。

## A text summary-based method to detect new events from streams of online news articles

- Record: 20539
- Year / journal: 2022 / Information & Management
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 初筛成立。论文的核心贡献是提出并实现一个基于文本摘要的新事件检测方法，最终成功指标是在固定人工事件标签上计算的miss/false alarm率，属于允许的冻结标签计算基准；没有用户自报、主观评分或人工评价系统输出质量作为核心结果。虽然事件标签的构建有一定人工判断，但标签在评估前固定，对比的是计算模型输出与固定ground truth的一致性。同时，文中实际设计和修改了软件制品，并与INCR、BERT-NED、bi-LSTM-NED、TextRank-based SED等基准进行了客观比较，给出了可验证的改善证据。效率优势是未测量的次要定性主张，不影响核心有效性的客观性。

## An anticrime information support system design: Application of K-means-VMD-BiGRU in the city of Chicago

- Record: 20211
- Year / journal: 2022 / Information & Management
- Status / role: fully_objective / exclusive
- Reason: 初筛正例经反向审计未被推翻。核心成功主张完全由模型在R²、MSE、RMSE、MAE和DA上的客观表现支撑，原始数据来自芝加哥官方警方记录，不是主观问卷、自报或人工语义质量编码。文中的公众感知讨论和管理含义是定性阐述，移除后不影响模型有效性的核心结论。系统具有明确的算法制品设计，并通过输入范围变体比较和文献数值对比展示了预测精度的改善。因此五个门槛全部满足。

## Consumer preference analysis based on text comments and ratings: A multi-attribute decision-making perspective

- Record: 20521
- Year / journal: 2022 / Information & Management
- Status / role: fully_objective / exclusive
- Reason: 初筛成立。论文核心目标是从文本评论和评分中分析消费者属性偏好并用于推荐，最终核心成功指标是对真实评分的预测误差MSE/MAE/RMSE，完全客观可计算。虽然内部使用了人工标注的情感极性训练数据，但该标注只作为特征提取中间步骤，不构成最终核心结果或核心主观贡献。与多个baseline的对比显示预测误差更低，制品和改善证据充分。

## Data analytics for the sustainable use of resources in hospitals: Predicting the length of stay for patients with chronic diseases

- Record: 20225
- Year / journal: 2022 / Information & Management
- Status / role: fully_objective / exclusive
- Reason: The paper's primary goal and core contribution is accurate early prediction of hospital LOS as a numerical variable. All core success outcomes are objective metrics computed from system-recorded admission/discharge timestamps; no subjective ratings, self-reports, human semantic coding, or expert opinions are used. The study designs and implements a deep MLP model and a data-engineering method to augment EMR data with historical variables. Improvement is demonstrated through architecture comparisons and through sensitivity analysis showing the dominant contribution of engineered features. Although there is no full ablation of the model without all engineered features, the evidence is sufficient and no mixed subjective core claim exists. Therefore the strict fully-objective improvement criterion is met.

## Algorithmic Assortative Matching on a Digital Social Medium

- Record: 28478
- Year / journal: 2022 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现推翻初筛的证据。全文所有核心成功结果（收入、消息数、任务开始/成功、留存）均来自游戏服务器日志自动记录的客观行为计数，无问卷、自报、专家/用户总体评分或人工语义质量判断。团队活动分类中产品经理参与设计活动得分，但这仅影响系统内部的分类机制，不是结果度量，且其有效性通过未来收入占比这一客观指标验证。用户CLV分类器的预测标签是未来30天实际购买金额，由服务器记录，属于对未来客观事件的预测，并非人工标签上的性能评价。论文通过现场实验（系统开/关）与随机匹配基线对比，展示了用户级和团队级多个客观指标的显著改善，匹配系统是明确设计、部署和比较的软件制品。因此确认严格匹配。

## Bidder Support in Multi-item Multi-unit Continuous Combinatorial Auctions: A Unifying Theoretical Framework

- Record: 28268
- Year / journal: 2022 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: 对初筛判定进行反向审计，未发现推翻证据。全文没有主观、自报、人工质量判断或混合核心贡献。所有核心成功指标均为完全客观的系统运行时间（milliseconds/microseconds），源自C程序在模拟拍卖中的时钟测量。本文明确设计并实现了计算软件制品（数据结构和算法），并通过与整数规划的对比实验证明了其客观性能优势。理论框架虽占一定篇幅，但服务于高效bidder support计算这一核心目标，未引入主观结果。因此五个门槛全部满足，确认严格匹配。

## Designing Core-Selecting Payment Rules: A Computational Search Approach

- Record: 28438
- Year / journal: 2022 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现推翻初筛的证据。论文的核心贡献是提出并实现一个计算搜索框架，以发现比QUADRATIC更好的MRC-selecting支付规则；最终目标和主要成功依据是效率、激励、收入三个完全客观的指标，均由BNE策略和概率分布经数值积分或蒙特卡洛采样计算得到。全文不存在问卷、自报、人工语义质量评价或主观权重，也不存在需要冻结标签例外的人工评价文本/创意场景。以QUADRATIC为基线的比较在多个域和大量设置中系统展示了改进，且代码开源。因此满足严格客观指标的五个门槛，属于fully_objective且核心角色为exclusive。

## Managing Congestion in a Matching Market via Demand Information Disclosure

- Record: 28496
- Year / journal: 2022 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: 初筛判定正确。该论文通过随机田野实验在真实移动约会应用中实施了需求信息披露UI干预，核心成功结果为平台自动记录的请求行为、匹配结果和匹配效率；所有核心结果均不依赖问卷、自报、人工编码或主观评价。访谈和实验室实验仅用于操纵有效性和阈值选择，不属于核心贡献，删除后核心主张完整。实验有明确控制组和多种处理组作为比较，需求+容量提示组在匹配效率上取得显著客观改善，且绝对匹配量未受损。因此五个门槛全部满足，确认为严格客观指标正例。

## Modifying Transactional Databases to Hide Sensitive Association Rules

- Record: 28218
- Year / journal: 2022 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现推翻初筛的证据。论文的核心成功主张围绕消毒后数据库准确性（等价于最小化修改事务数）展开，该指标是 RHP/AMP/LRH 的目标函数，完全由公式和求解器计算；敏感规则是否隐藏由确定性支持度/置信度约束保证；求解时间和 spurious/lost rules 也是客观自动输出。不存在与主观效果并列的核心贡献，也没有人工语义编码或自报结果。因此维持 strict_match=true。

## The Secret to Finding a Match: A Field Experiment on Choice Capacity Design in an Online Dating Platform

- Record: 28211
- Year / journal: 2022 / Information Systems Research
- Status / role: fully_objective / dominant
- Reason: 初筛正例成立。文章的核心目标是回答不同选择容量设计如何影响参与度和匹配结果，并据此给出设计指南。核心成功结果（选择数、聊天数、转化率、收入等）全部来自平台后台日志，是客观行为或交易记录，不依赖用户自报、专家评分或人工语义编码。用户吸引力评分虽为主观数据，但仅用于机制解释和控制变量；删除这些主观机制后，文章关于选择容量对客观参与度和匹配结果影响的核心主张仍然完整。实验通过控制组与三个处理组的对照，以及处理组之间的比较，清楚证明了客观指标上的改善。

## Assessing and Enhancing Adversarial Robustness of Predictive Analytics: An Empirically Tested Design Framework

- Record: 25465
- Year / journal: 2022 / Journal of Management Information Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 对照六类假阳性检查后，初筛判定成立。所有核心成功指标均为固定基准标签上的确定性分类指标及由此派生的鲁棒性指标，无主观、自报或人工输出质量评价；人类判断仅存在于预先冻结的基准标签，属于冻结标签例外。ARText 是明确的软件制品并实质修改了文本分类系统的评估与训练组件；相对于九个基线和对抗重训练前后均展示了客观改善。因此 confirmed_strict_match=true。

## Designing Attentive Information Dashboards

- Record: 11474
- Year / journal: 2022 / Journal of the Association for Information Systems
- Status / role: fully_objective / exclusive
- Reason: Reverse audit confirms the initial positive screening. The article designs and instantiates a concrete software artifact (attentive information dashboard with individualized VAF) and evaluates it against a general-VAF control in a controlled lab experiment. All three core hypotheses are tested exclusively with objective eye-tracking metrics: fixation duration/count, transition counts, and standard deviation of attention distribution. Subjective/self-report measures appear only as demographic controls or exclusion criteria and are not part of the core success claim. There is no human judgment of system output, no semantic coding, and no subjective quality rating. The objective metrics are the endpoint success criteria, not merely mediators or manipulation checks, and the comparative improvements are statistically significant. Therefore, the article satisfies the strict fully-objective criterion.

## Combining Crowd and Machine Intelligence to Detect False News on Social Media

- Record: 2826
- Year / journal: 2022 / MIS Quarterly
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 反向审计未能推翻初筛。文章的核心贡献是设计并实现CAND/CLNAM假新闻检测框架，并通过固定事实核查标签上的PR AUC、F1、召回率、精确率等benchmark指标，与多种基线和聚合方法比较，证明其检测性能提升。虽然T2辟谣回应检测使用人工标注训练，新闻类型敏感性含人工标注，且微博举报数据部分模拟，但这些均不构成对最终系统输出的主观评价，也不动摇最终检测性能这一核心成功主张的客观性。因此满足严格客观指标正例条件。

## Cross-Lingual Cybersecurity Analytics in the International Dark Web with Adversarial Deep Representation Learning

- Record: 2006
- Year / journal: 2022 / MIS Quarterly
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 经独立反向审计，初筛结论成立：论文以计算设计科学范式明确设计了CLHAD软件制品，核心目标是自动检测非英语暗网黑客资产。所有核心成功证据均来自在预先冻结的人类标注金标准上计算的Accuracy、F1和AUC，通过五折交叉验证和配对t检验与多种基线比较并显著提升。人工参与仅存在于创建冻结标签环节，不涉及对模型输出的人工质量评价；SHAP解释和资产分布剖析为辅助内容，删除后不影响核心成功主张。因此满足五门槛，属于固定标签计算benchmark，确认为严格客观匹配。

## Designing Hybrid Mechanisms to Overcome Congestion in Sequential Dutch Auctions

- Record: 1558
- Year / journal: 2022 / MIS Quarterly
- Status / role: fully_objective / exclusive
- Reason: 独立反向审计未发现推翻初筛的证据。文章核心目标是缓解顺序荷兰拍卖的拥堵，所有关键实证结果均来自系统自动记录的交易日志（回合数、成交价、数量），DID与多种稳健性检验显示混合机制在回合数和价格离散度上显著改善、收入未受损；博弈论分配效率是客观数学推导，不引入主观/自报/人工质量判断。虽然分配效率未在实验中实测、实验为准自然设计，不完全随机，但这些限制不构成将核心成功主张变为主观或混合证据的理由。

## Discovering Emerging Threats in the Hacker Community: A Nonparametric Emerging Topic Detection Framework

- Record: 10970
- Year / journal: 2022 / MIS Quarterly
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 初筛判定正确。文章以设计科学范式提出并实现NPETD框架，核心目标是提高黑客社区新兴威胁列表检测的有效性与效率。正式实验在Alphabay DNM测试集上与四个基线比较，核心结果全部是Precision、Recall、F-measure、UMass topic coherence和processor time；前三者是固定标签benchmark（研究者预先选择六个Alphabay类别作为正例，所有方法在同一冻结标签上比较），coherence和processor time为确定性计算。论坛Altenens演示只是定性效用说明，不参与核心成功指标，删除后核心主张仍完整。因此五个门槛全部满足，严格匹配。

## Peer-to-Peer Loan Fraud Detection: Constructing Features from Transaction Data

- Record: 8062
- Year / journal: 2022 / MIS Quarterly
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 初筛判定成立。文章以提升P2P借贷欺诈检测性能为最终目标和核心贡献，明确设计并修改机器学习检测流程中的特征组成部分；全部核心成功结果均为基于预先冻结的欺诈/合法标签计算的Accuracy、Recall、Precision、F score和AUC，属于允许的冻结标签benchmark；不存在作为共同核心或主要结果的主观评分、自报、人工语义质量判断；通过在两个平台数据集上对Set A/Set B/Set C进行10折交叉验证和显著性检验，证明了相对基线特征集合的客观性能改善。因此，confirmed_strict_match为true。

## Reciprocity or Self-Interest? Leveraging Digital Social Connections for Healthy Behavior

- Record: 4624
- Year / journal: 2022 / MIS Quarterly
- Status / role: fully_objective / dominant
- Reason: 初筛成立。文章核心目标是提升健康行为（挑战完成率和跑步距离），并通过数字社交连接设计互惠激励干预机制来实现；核心成功结果全部由平台自动记录的距离和系统判定的完成状态支撑，社会亲近度也由客观网络结构衡量。随机对照实验通过与自利激励组、朋友送礼自利组和正常用户基线的比较，显著证明了互惠激励的客观改善。主观问卷仅用于机制解释、副作用检查和补充稳健性，删除后核心结论仍完整成立，因此符合严格客观指标和核心主导贡献的门槛。

## Understanding Medication Nonadherence from Social Media: A Sentiment-Enriched Deep Learning Approach

- Record: 13032
- Year / journal: 2022 / MIS Quarterly
- Status / role: benchmark_objective_with_fixed_labels / dominant
- Reason: After full-text reverse audit, SEDEL is a clearly instantiated software artifact. Its core contribution is an information extraction/retrieval method for medication nonadherence reasons from social media. The main success criterion is precision, recall, and F1 against fixed expert-annotated ground-truth spans. This is the permitted fixed-label benchmark exception. Ablation and baseline comparisons provide objective evidence of improvement. The expert-verified nine-category taxonomy is secondary and removable without undermining the core benchmark claim. Thus the initial strict-match judgment is confirmed.

## Wearable Sensor-Based Chronic Condition Severity Assessment: An Adversarial Attention-Based Deep Multisource Multitask Learning Approach

- Record: 10800
- Year / journal: 2022 / MIS Quarterly
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 初筛判定成立。文章以设计科学范式创建了AADMML这一可复现的计算制品，核心目标是改善慢性病严重程度评估的预测误差和训练效率。所有核心成功证据均来自固定MDS-UPDRS标签上的确定性预测误差、训练日志中的验证损失，以及固定标签下的召回/AUC；这些属于冻结标签benchmark例外。注意力权重解释、示例案例和经济收益推演只是辅助机制与应用展示，删除后核心成功主张仍然完整。AADMML相对基准模型和ablation变体展示了客观、一致的比较改善，因此严格满足五道门槛。

## A decision support framework to incorporate textual data for early student dropout prediction in higher education

- Record: 16584
- Year / journal: 2023 / Decision Support Systems
- Status / role: fully_objective / dominant
- Reason: 论文核心目标是能否通过纳入学生文本反馈并增加文本分割层来提升辍学预测，核心有效证据是 AUC 与 TDL，二者均由机构固定 dropout 标签与模型预测确定性计算，完全客观，且通过多个基线和显著性检验证明改善。RQ2 的专家 bigram 标注和可视化仅用于可解释性洞察，不参与模型有效性判定；删除后核心成功主张仍完整。因此确认严格正例。

## A deep learning approach for detecting fake reviewers: Exploiting reviewing behavior and textual information

- Record: 20024
- Year / journal: 2023 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 经过反向审计，未发现可推翻初筛的主观或人工质量判断。该文核心成功主张完全由在YelpZIP/YelpNYC冻结标签上计算的分类性能指标构成；标签属于预先固定的基准标签，符合冻结标签例外。文中没有自报、满意度、人工语义编码或主观评分作为核心证据；SHAP和特征重要性分析属于解释性内容，不影响主结论。模型架构有实质设计与多个模块消融，并在两个数据集上相对多种基线和变体证明显著提升。因此五个门槛均满足，确认为严格客观指标正例。

## Assuring quality and waiting time in real-time spatial crowdsourcing

- Record: 20016
- Year / journal: 2023 / Decision Support Systems
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现足以推翻初筛的主观测量、自报结果、人工质量评分或混合核心贡献。论文的正式优化目标是最小化平均等待时间（α）和最大化被选中工人平均声誉（β），两者均由明确公式和仿真数据计算，不依赖人类判断。软件制品明确，包含预测模型和分配算法，并与RB-TPSC基线在多个场景比较，客观指标上报告了改进。虽然β是任务质量代理而非直接质量测量，但其数值生成和计算完全客观，不属于人工语义判断或主观权重。

## CATCHM: A novel network-based credit card fraud detection method using node representation learning

- Record: 20011
- Year / journal: 2023 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 初筛结论成立。论文提出的CATCHM是明确设计/修改的软件制品，其最终目标是在真实信用卡交易数据集上提升欺诈检测的分类性能和运行效率。所有核心成功指标——AUCPR、F1、TP@300、平均预测处理时间和挽回收入——均为完全客观的或基于固定ground truth标签的基准指标，不存在主观问卷、自报数据、专家对模型产出的质量评分或混合主观核心贡献。标签虽由领域专家调查确认，但作为冻结的分类ground truth，在固定标签基准例外范围内。CATCHM通过与多个基准和baseline的对比，在关键指标上证明了实质性改善；贝叶斯显著性检验进一步支持其优越性。

## Co-evolution of neural architectures and features for stock market forecasting: A multi-objective decision perspective

- Record: 16588
- Year / journal: 2023 / Decision Support Systems
- Status / role: fully_objective / exclusive
- Reason: 初筛判定成立。全文所有核心有效性证据均来自基于历史价格和确定性日涨跌公式的客观分类指标（准确率/Hit-Rate、MCC、平衡误差），没有依赖人工评分、自报数据或主观质量判断。论文实质设计并实现了一个协同进化神经架构搜索框架，并通过21种基线设计方法的比较和统计检验证明其在客观指标上的显著改进。DM偏好仅作为方法输入进入后验选择，不影响核心结果指标的客观性。

## Removing order effects from human-classified datasets: A machine learning method to improve decision making systems

- Record: 20023
- Year / journal: 2023 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: After full-text reverse audit, the stage-one positive judgment is upheld. The core success claim is that OERM detects and reduces order effects using deterministic computational metrics computed from classifier outputs and frozen dataset labels. No subjective ratings, self-reports, or human quality evaluations are used to establish the core success. The fixed-label benchmark exception applies. Although Reuters and PhysRev retain order-effect imbalance after equilibrium splitting, the paper explicitly attributes this to human labeling rather than writing style, and this does not negate the objective comparative improvement demonstrated on ScopusAbstracts and ISAbstracts. The artifact is specified algorithmically and implemented, satisfying the software-artifact requirement. All five gates are true.

## Will they take this offer? A machine learning price elasticity model for predicting upselling acceptance of premium airline seating

- Record: 20559
- Year / journal: 2023 / Information & Management
- Status / role: fully_objective / exclusive
- Reason: 初筛判定成立。PREM是明确软件制品，其核心目标是用ML预测升舱接受并优化报价，从而提升客观业务指标。主要效果证据来自真实历史交易和接受/拒绝记录上的F1与Revenue Capture，并通过对当前启发式方法、多种嵌入、分类器、分群、收益最大化基线和系统消融的系统比较验证改进。论文中的模拟数字是模型外推估计，但来源为历史分布和确定性算法，不涉及主观判断；即便忽略这些模拟，历史数据上的核心评价仍然完整。因此未发现足以推翻初筛的主观、自报、人工质量判断或混合核心贡献。

## A Comparison of Methods for Treatment Assignment with an Application to Playlist Generation

- Record: 28498
- Year / journal: 2023 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: The audit confirms the stage-one positive classification. The paper's core empirical contribution is an at-scale comparison and improvement of algorithmic treatment-assignment policies for playlist generation. The final objective and central success metric is the automatically logged number of streamed songs; no subjective, self-report, or human semantic judgment is used in the core evaluation. The artifacts are learned decision policies/classifiers, and improvements are demonstrated relative to production, standard A/B practice, and competing metalearners. Therefore all five gates are satisfied and the match is strict.

## Augmenting Password Strength Meter Design Using the Elaboration Likelihood Model: Evidence from Randomized Experiments

- Record: 28462
- Year / journal: 2023 / Information Systems Research
- Status / role: fully_objective / dominant
- Reason: 确认初筛。文章以提升密码强度计的实际效果为最终目标，设计并实现了增强型密码强度计（明确软件制品），核心结果指标（diff_strength和num_reset）来自系统日志和算法计算，完全客观，且通过随机对照实验和现场实验与传统控制组比较，证明了客观改善。Study 1的自我报告量表仅作为机制验证，删除后核心成功主张仍完整，因此不构成混合核心。所有核心成功结果均为客观测量，制品改进得到证明，确认严格匹配。

## Augmenting Social Bot Detection with Crowd-Generated Labels

- Record: 28480
- Year / journal: 2023 / Information Systems Research
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 该论文明确构建了一个社交机器人检测系统，核心目标是提升bot检测性能。所有核心成功指标均为在众包生成的冻结标签上计算的计算模型预测性能（Precision、Recall、F1、AUC、检测率等），属于允许的冻结标签基准。系统通过与传统模型、消融版本及新bot测试的比较，证明了客观改进。核心成功主张不依赖主观或人工质量评审结果，因此满足所有严格客观指标标准。

## Could Gamification Designs Enhance Online Learning Through Personalization? Lessons from a Field Experiment

- Record: 28459
- Year / journal: 2023 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现必须推翻初筛的主观成功结果或人工语义评分。核心因变量均来自平台日志、时间戳和标准化测试；目标导向问卷和开放评论是调节变量/辅助解释，不是核心结果。作者实质修改了MOOC平台上的游戏化反馈组件，并相对控制组和其他处理组在SRL参与度和学习效率上证明显著客观改善，且SRL显著中介测试成绩。因此确认严格匹配。

## Diversity Preference-Aware Link Recommendation for Online Social Networks

- Record: 28537
- Year / journal: 2023 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现足以推翻初筛的主观指标、人工语义判断或混合核心贡献。论文提出的DPA-LR方法明确解决了新定义的多样性偏好感知链接推荐问题，其核心成功指标为DPMS、precision、recall和F1，全部由档案数据、真实平台链接日志和确定性公式计算，没有任何问卷、自报偏好、专家评分或人工语义编码作为结果。通过与五种多样化/推荐基准和三种图神经网络链接推荐方法的比较，并通过对GCN-LR和DPA-MMR的消融/机制分析，论文证明了在全部完全客观指标上的显著改善。讨论中关于用户体验和满意度的论述是理论动机而非实测结果，删除后核心主张不受影响。

## Fun Shopping: A Randomized Field Experiment on Gamification

- Record: 28494
- Year / journal: 2023 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: 经过反向审计，未发现主观或自报结果作为核心成功指标。满意度调查仅用于平衡检查和协变量，不用于结果分析。核心成功主张（销售、距离、到店次数）完全来自自动交易记录和Wi-Fi追踪，属于完全客观测量。论文明确设计/实现了游戏化软件组件，并通过随机对照实验证明了对核心客观指标的显著改善。因此，初筛判定成立，严格匹配。

## Green Data Analytics of Supercomputing from Massive Sensor Networks: Does Workload Distribution Matter?

- Record: 28656
- Year / journal: 2023 / Information Systems Research
- Status / role: fully_objective / dominant
- Reason: 反向审计未发现推翻初筛的证据。文章以降低 HPC 数据中心总能耗为最终核心目标，明确设计了多种核心分配与调度策略（软件/算法制品），并通过模拟实验和真实 NSCC 数据集，与商业调度器及替代策略进行了系统比较，展示了显著且一致的能耗改善。所有核心结果指标均来源于 RPDU 和热负载传感器自动记录、作业日志以及确定性公式，没有问卷、自报、专家评分、人工语义编码或主观权重作为核心成功指标。作业完成时间/通信开销作为第二目标同样来自日志与公式，不构成主观混合。因此五个门槛全部满足。

## Optional Verification and Signaling in Online Matching Markets: Evidence from a Randomized Field Experiment

- Record: 28565
- Year / journal: 2023 / Information Systems Research
- Status / role: fully_objective / dominant
- Reason: 全文核心有效性结果均来自平台日志记录的消息行为、匹配行为和平台计算的popularity得分，属于完全客观测量。文章设计并引入可选电话验证功能，通过随机现场实验将验证用户与未验证用户比较，证明验证在消息接收/发送数量、对象质量和最终匹配数上均有显著改善。调查问卷和深度学习美颜模型仅用于机制解释、操纵检查或构造协变量，删除后不损害核心成功主张。因此初筛正例成立。

## Personalized Ranking at a Mobile App Distribution Platform

- Record: 28510
- Year / journal: 2023 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现需推翻初筛的主观或自报核心结果。全文以平台预期收入为最终目标和核心贡献，该指标由服务器日志（点击/安装）与平台合同CPA边际收入计算；政策实验相对基线明确证明了所提出个性化混合排名算法的客观改进。因此确认严格匹配。

## Spoiled for Choice? Personalized Recommendation for Healthcare Decisions: A Multiarmed Bandit Approach

- Record: 28562
- Year / journal: 2023 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现足以推翻初筛的主观/自报/人工质量判断或混合核心贡献。论文提出的明确软件制品（推荐系统框架）以提升用户长期参与为目标，核心成功指标均为基于平台真实行为日志的客观推荐性能度量（Precision/Recall/nDCG/MAP），辅助指标（多样性JSD、用户改善率）也源自同一客观日志。人工标注的干预元属性仅用于训练中间表示，不构成最终结果评价。所有核心证据均通过固定历史数据上的基准对比和消融实验证明改善。因此五个门槛均通过，objective_status为fully_objective，core_role为exclusive，confirmed_strict_match=true。

## Designing Conversational Dashboards for Effective Use in Crisis Response

- Record: 13598
- Year / journal: 2023 / Journal of the Association for Information Systems
- Status / role: fully_objective / exclusive
- Reason: The article's core evaluation rests on objectively measured outcomes: behavioral navigation ratios, system-recorded task times, and objectively scored task correctness. Subjective self-efficacy is confined to a manipulation check, and NLP performance uses a frozen-label benchmark as secondary support. The artifact is explicitly implemented and comparatively evaluated across multiple versions, demonstrating significant improvements. No disqualifying mixed subjective core, human semantic output judgment, or artifact failure was found. All five gates pass, and the core role is exclusive.

## Depicting Risk Profile over Time: A Novel Multiperiod Loan Default Prediction Approach

- Record: 5034
- Year / journal: 2023 / MIS Quarterly
- Status / role: fully_objective / exclusive
- Reason: 初筛方向正确。全文核心成功主张完全由客观性能指标支撑：C-index、IBS、AUC、KS、H-measure、违约计数、平均回报率。所有数据均来自平台真实贷款违约和还款记录，无自报、问卷、人工语义评分或专家总体判断。没有混合核心贡献，案例分析是机制验证且基于确定性数值计算。制品HACS是明确设计的预测模型，通过多基准比较、统计显著性检验、效应量分析和消融研究证明了在客观指标上的实质改善。因此五个门槛全部满足，strict_match为true。

## Exploiting Expert Knowledge for Assigning Firms to Industries: A Novel Deep Learning Method

- Record: 12586
- Year / journal: 2023 / MIS Quarterly
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 第一阶段初步判定为真。反向审计未发现应推翻该判定的证据。全文核心成功主张完全基于对固定行业标签的预测性能：NAICS/GICS准确率和宏F1、误分类成本、树距离以及生产率下的准确率。这些指标在原始数据上均为确定性计算或固定标签基准，属于冻结标签例外。不存在问卷、自报、专家评分或人工语义质量编码构成的核心结果。DeepIA是明确设计并实现的软件制品，且通过多个基准、消融和变体比较证明了客观指标的显著改善。因此确认strict_match=true。

## Let Artificial Intelligence Be Your Shelf Watchdog: The Impact of Intelligent Image Processing-Powered Shelf Monitoring on Product Sales

- Record: 9116
- Year / journal: 2023 / MIS Quarterly
- Status / role: fully_objective / dominant
- Reason: 本文明确研究一款软件制品（IIP货架监测系统）对完全客观的结果指标——产品销售额——的提升作用，并通过准实验和随机田野实验提供了对照比较证据。核心成功主张全部依赖厂商记录的门店销售额，客观、可验证；合规率由系统自动生成，仅作机制证据；访谈等定性材料不构成为核心成功证据。删除所有主观证据不影响核心结论。因此满足全部五个门槛，确认为严格匹配。

## Nudging Private Ryan: Mobile Microgiving under Economic Incentives and Audience Effects

- Record: 13938
- Year / journal: 2023 / MIS Quarterly
- Status / role: fully_objective / dominant
- Reason: 初筛判定成立。论文核心经验证据完全来自两个大规模实地实验中由系统日志客观记录的捐赠决策和捐赠金额；应用软件被实质修改以加入捐赠、助推、激励和社交可见性功能，并与无激励控制组及不同处理组比较，证明显著改善。理论模型是附加贡献，但不占用或混合经验结果，删除后核心成功主张仍完整。

## ROLEX: A Novel Method for Interpretable Machine Learning Using Robust Local Explanations

- Record: 5780
- Year / journal: 2023 / MIS Quarterly
- Status / role: fully_objective / dominant
- Reason: 初筛判定的核心成功指标是自动计算的local fidelity和LDA-fidelity，文章将其作为ROLEX方法的直接优化目标和主要性能证据，并通过多数据集、多基准、消融和SMOTE增强比较证明改善。专家访谈虽有主观编码，但明确是界面潜在价值的补充讨论，删除后核心方法结论完整，不构成混合核心贡献。因此确认严格匹配。

## Unifying Algorithmic and Theoretical Perspectives: Emotions in Online Reviews and Sales

- Record: 8482
- Year / journal: 2023 / MIS Quarterly
- Status / role: fully_objective / dominant
- Reason: 初筛判定正确。论文的核心研究目标是提升票房预测精度（客观MAPE），为此实质设计了情感词典扩展与情感检测算法，并通过多种基线和组合比较证明了离散情感特征的显著预测改进。研究2的主观实验仅用于解释机制和检验跨文化泛化，不参与算法有效性的评估，删除后核心成功主张仍然完整成立。因此，文章以完全客观的票房预测MAPE作为最终目标和主要成功依据，符合严格匹配条件。

## Unlocking the Power of Voice for Financial Risk Prediction: A Theory-Driven Deep Learning Design Approach

- Record: 11058
- Year / journal: 2023 / MIS Quarterly
- Status / role: fully_objective / exclusive
- Reason: 初筛判定成立。文章以设计科学范式开发 DeepVoice 制品，核心目标是通过加入经理语音中的基础声学线索提升财务风险预测准确率。所有核心成功指标（OOS R^2、MSE、DM 检验、期权策略收益）均由完全客观的市场数据计算：目标变量来自 CRSP 日收益率，期权收益来自 OptionMetrics 市场报价。没有任何自报、主观评分或人工语义编码参与核心结果评价。存在定性案例（AMD），但它是辅助说明，不构成核心证据，删除后不影响主结论。论文通过市场基准、消融、SOTA 模型、时间序列模型、情感构念模型、纯噪声对照等多个比较证明了客观改善。因此 five gates 全部满足，objective_status 为 fully_objective，core_role 为 exclusive，confirmed_strict_match=true。

## A hybrid decision support system for adaptive trading strategies: Combining a rule-based expert system with a deep reinforcement learning strategy

- Record: 20052
- Year / journal: 2024 / Decision Support Systems
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现推翻初筛的证据。全文核心目标是提升交易绩效，所有核心结果均来自公开市场价格、确定性交易模拟和财务公式，不存在主观评价、自报或人工质量编码。即使RB规则由人类专家制定，也只是系统内部先验知识，不污染结果测量。作者通过消融和与多类基线对比，证明提出的完整制品在客观指标上获得改善。因此确认strict_match为true。

## A novel federated learning approach with knowledge transfer for credit scoring

- Record: 20050
- Year / journal: 2024 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 全文审计后确认初筛判定合理。核心贡献是提出FedKT算法，目标是通过联邦学习中的知识迁移提升信用评分的分类性能。所有核心成功指标（Accuracy、Recall、F1-score、KS）均由模型预测与固定信用标签计算，完全客观，无主观问卷、自报或人工质量编码。联邦学习框架和FedKT是明确的算法制品，且在五个公开信用数据集上通过与非联邦及联邦基线的系统比较和Friedman显著性检验证明了客观改善。因此满足全部五个严格门槛，属于以完全客观固定标签基准为核心目标的算法改进文章。

## Analyzing the online word of mouth dynamics: A novel approach

- Record: 20066
- Year / journal: 2024 / Decision Support Systems
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现足以推翻初筛的主观或自报核心结果。文章的核心贡献是提出并实现新方法MultiSeqCCoA，并通过模拟研究中的载荷恢复准确性和运行时间对比，以及实证中的DID和t检验，以完全客观的计算和统计指标验证了方法的有效性与效率。没有人工语义质量编码、专家评分或自报测量作为核心证据；主观事件标签只是辅助解释。因此五个门槛均通过，客观状态为fully_objective，核心角色为exclusive。

## Explaining the model and feature dependencies by decomposition of the Shapley value

- Record: 16830
- Year / journal: 2024 / Decision Support Systems
- Status / role: fully_objective / dominant
- Reason: 初筛判定成立。论文明确提出并实质实现了将 Shapley 值分解为 interventional 和 dependent 两部分的软件算法，并通过确定性的模型输出变化实验、解析依赖归因曲线和数学定理，与 conditional SHAP、interventional SHAP 和 Shapley residuals 进行了比较，展示了客观改善。所有核心成功证据均来自可重复的数值/解析计算，不存在人工评分、自报或主观质量测量。定性力点图解读属于辅助说明，删除后核心客观成功主张仍然完整。因此五道门槛均通过。

## Measuring service quality based on customer emotion: An explainable AI approach

- Record: 20039
- Year / journal: 2024 / Decision Support Systems
- Status / role: benchmark_objective_with_fixed_labels / dominant
- Reason: 反向审计未发现推翻初筛的充分证据。文章以提升服务质量预测性能为核心目标，所有核心成功结果均是在冻结标签（客户调查服务质量、人工情绪标注、客户自报推荐意愿）上的计算性能指标（F1、recall、precision、accuracy），符合benchmark_objective_with_fixed_labels例外。解释性发现和应用展示不构成核心结果的并列主观贡献。软件制品明确设计并比较改善得到验证。虽然存在正文与表B.1在F-score上的不一致等小瑕疵，但不足以改变结论。

## Attending to Customer Attention: A Novel Deep Learning Method for Leveraging Multimodal Online Reviews to Enhance Sales Prediction

- Record: 28706
- Year / journal: 2024 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: 初筛判定成立。文章的核心贡献是提出并验证 DTV-AMI 这一软件制品/方法，以提升基于多模态评论的酒店月度入住率预测性能。所有核心成功结果均为 RMSE/MAE 等完全客观预测误差指标，真实标签来自酒店运营记录；不存在问卷、自报、专家评分或人工语义编码作为核心成功依据。‘客户注意力’是理论设计动机和探索性解释，不是需要主观测量的并列结果。文章通过主实验、表示学习实验、集成实验和消融分析，相对多种基线和基准展示了统计显著的客观改善。因此五个门槛均通过。

## Background Music Recommendation on Short Video Sharing Platforms

- Record: 28336
- Year / journal: 2024 / Information Systems Research
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 反向审计未发现足以推翻初筛的证据。全文核心贡献是设计并评估DL-BGM背景音乐推荐模型，最终目标明确为提升推荐性能；核心指标HR、NDCG基于冻结的用户历史选择标签，AL基于平台客观点赞记录，均不依赖自报或人工质量评分。模型相对于多个基线在多个场景中展现了显著且一致的客观改善。所有五个门槛均满足，因此确认严格匹配。

## Contextual Targeting in mHealth Apps: Harnessing Weather Information and Message Framing to Increase Physical Activity

- Record: 26551
- Year / journal: 2024 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: 核心成功结果（目标达成、步数、后续天数、重复干预）全部来自智能手机计步器自动记录，完全客观；自报动机仅用于机制分析，不构成核心贡献；文章实质设计并实现了天气-框架匹配的干预模块，并通过随机实验比对neutral或相互对比证明了显著改善。符合严格客观指标正例标准。

## Dynamic Bayesian Network–Based Product Recommendation Considering Consumers’ Multistage Shopping Journeys: A Marketing Funnel Perspective

- Record: 27959
- Year / journal: 2024 / Information Systems Research
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 独立反向审计未能推翻初筛正例。文章以设计科学视角提出并实现 MS-DBN 计算制品，核心目标是提高动态产品推荐的准确率和排序；全部核心成功结果均由大规模真实行为日志上的 HR@10/NDCG@10 支撑，标签为固定实际交互产品，属于冻结标签上的客观基准。消费者心理阶段和兴趣的可视化只是机制说明，不是主观或混合核心结果。因此五门槛全部通过。

## Longitudinal Impact of Preference Biases on Recommender Systems’ Performance

- Record: 28045
- Year / journal: 2024 / Information Systems Research
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 反审计未发现推翻初筛的证据：所有核心成功结果由固定 ground-truth 标签、确定性公式或仿真日志计算，无任何人工主观判断；文章明确设计了软件组件（去偏算法）并相对对照证明客观指标改善。满足全部五个门槛。

## Motion Sensor–Based Fall Prevention for Senior Care: A Hidden Markov Model with Generative Adversarial Network Approach

- Record: 28654
- Year / journal: 2024 / Information Systems Research
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 全文采用计算设计科学范式，核心贡献是设计并评估HMM-GAN + LR制品。主要成功依据是实验1片段状态识别和实验2跌倒预防触发上的Accuracy/F1/AUC，均在两个公开数据集上以固定标签基准比较并显著优于基线。TST标签虽由研究生人工标注，但属于冻结目标标签，适用benchmark例外；SisFall标签为自动生成。不存在主观/自报/人工质量评分作为核心成功指标，也无混合核心贡献；案例经济效益由客观预测与成本公式推导。因此确认严格匹配。

## Personalized Privacy Preservation in Consumer Mobile Trajectories

- Record: 28678
- Year / journal: 2024 / Information Systems Research
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 论文明确设计了一个算法框架，核心目标是量化并降低消费者隐私风险同时保持广告商效用，所有核心成功结果均为通过自动GPS轨迹数据和固定标签（如Google Places类别）计算的风险/效用指标，不包含任何主观评分、自报或人工语义质量判断；通过与原始数据和十种基线的量化比较证明了改进，因此符合“完全客观指标+冻结标签基准”的严格匹配条件。

## Smart Markets for Real-Time Allocation of Multiproduct Resources: The Case of Shared Electric Vehicles

- Record: 28355
- Year / journal: 2024 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现推翻初筛的证据。论文的核心成功主张是利润提升、利用率提升和决策精度/罚款规避，全部基于实际交易日志、实际市场价格和确定性公式计算，不依赖任何自报、满意度、专家评分或人工语义质量判断。FleetPower是明确设计的软件制品，通过与朴素仅租赁基线在三个真实数据仿真场景中的比较证明了客观改善。因此确认严格匹配。

## Task Characteristics and Incentives in Collaborative Problem Solving: Evidence from Three Field Experiments

- Record: 28044
- Year / journal: 2024 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: 经独立反向审计，未发现足以推翻初筛的主观/自报/人工judged核心结局。全部核心成功结局均来自企业工单数据库和系统日志，包括CaseTAT、EngineerHours、CaseIdleTime、CSGHours/PSGHours、协作合规率。访谈仅用于形成解释性假设，不构成核心测量或并列贡献。文章明确设计并使用HRTech Analytics这一软件制品，且通过实验一DiD、实验二干预验证、实验三激励纠正前后对比提供了客观改善证据。因此维持初筛：严格客观匹配成立。

## When Is More Merrier? A Cloud-Based Architecture to Procure Impressions from Multiple Ad Exchanges

- Record: 28670
- Year / journal: 2024 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: 反向审计未能推翻初筛。论文的核心贡献是以最小化期望总成本为最终目标，设计并实质修改了可实施的云基采购架构及其关键模块（交易所选择算法与 EFlex 选择性出价）。所有核心成功结果均来自成本模型、公式、真实投标日志和云账单，不依赖人工评分、自报或主观质量判断；数值实验和 Cidewalk 案例均相对明确基准（单一最佳交易所、当前单交易所方案）证明了成本改善。因此五个门槛均满足，strict_match 维持为 true。

## When Variety Seeking Meets Unexpectedness: Incorporating Variety-Seeking Behaviors into Design of Unexpected Recommender Systems

- Record: 28035
- Year / journal: 2024 / Information Systems Research
- Status / role: benchmark_objective_with_fixed_labels / dominant
- Reason: 反向审计未发现足以推翻初筛的假阳性因素。论文核心贡献是设计并实现将消费者variety-seeking行为融入unexpected recommender system的推荐模型，最终性能由离线AUC/HR@10和在线CTR/VV/TS等客观指标支撑，并通过多个baseline和在线生产系统比较证明了显著改进。问卷自报仅用于验证variety-seeking度量的构建效度，属于次级组件验证，删除后推荐系统核心改进主张仍然完整。离线标签属于冻结标签基准，在线指标为平台客观日志。因此判定为严格匹配。

## Discovery of Technological Innovation Systems: Implications for Predicting Future Innovation

- Record: 25512
- Year / journal: 2024 / Journal of Management Information Systems
- Status / role: fully_objective / exclusive
- Reason: 初筛正例经反向审计仍成立。论文核心成功主张为：通过自主设计的自动化TIS发现框架，以客观USPTO专利量和引用量为预测目标，借助机器学习和计量模型证明TIS类创新指标对焦点类未来创新数量和质量有显著解释力和预测力。所有核心结果均来自专利/引用登记数据、机器学习预测误差和金融市场价格数据，没有使用问卷、自报、人工评分或主观评价作为成功标准。删除人工主题标签和说明性案例后，核心客观证据链完整。制品有明确算法设计/模块实现，并与过去专利量、citation-based CRTI、无TIS指标等基准比较，展示显著改进。因此满足五个严格门槛。

## Knowledge-Aware Learning Framework Based on Schema Theory to Complement Large Learning Models

- Record: 16424
- Year / journal: 2024 / Journal of Management Information Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 逐项检查未发现假阳性证据。文章核心目标是构建知识感知学习框架，所有核心成功判断均基于固定标签基准上的F1、参数量、训练时间和低数据比例性能；没有问卷、自报、人工语义质量评分或主观权重。虽然存在对认知科学理论的讨论，但没有作为核心结果测量；删除后结论完整。

## Consumers’ Opinion Orientations and Their Credit Risk: An Econometric Analysis Enhanced by Multimodal Analytics

- Record: 7534
- Year / journal: 2024 / Journal of the Association for Information Systems
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现足以推翻初筛的证据。核心成功主张是意见风险构念与客观逾期天数之间的显著关联，以及加入该构念后对客观信贷风险预测误差（RMSE/MAE）的显著改善。因变量完全来自金融科技公司记录，预测误差由确定性交叉验证计算；领域专家标注和自报问卷只出现在训练过程和辅助效度验证中，删除后核心结论仍完整。文章设计了 mBERT 和 attention-based DCNN 等明确软构件，并通过 F1 vs F2/F3/F4 的基线比较证明了客观改善。因此五个门槛均为真。

## Digital Institutionalization: The Case of E-Prescribing

- Record: 14444
- Year / journal: 2024 / Journal of the Association for Information Systems
- Status / role: fully_objective / dominant
- Reason: 初筛未被推翻。文章采用ADR设计并实质实现了NEF交换契约这一软件/系统规则制品，核心效能评估是自动验证软件对实施前后所有XML电子处方进行的规则偏离计数，完全客观；自动错误大幅下降、全国采纳率99%和法规变革共同支撑成功主张。药房调查等主观材料仅补充论证“务实合法性”，删除后核心结论仍完整，因此符合严格客观制品改善标准。

## Automated Analysis of Changes in Privacy Policies: a Structured Self-Attentive Sentence Embedding Approach

- Record: 7654
- Year / journal: 2024 / MIS Quarterly
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 全文以SAAS在OPP-115固定标签上的多标签分类性能为核心贡献，所有关键实验均使用micro-averaged precision/recall/F1和Hamming loss等客观指标，并通过对多个基线和消融变体比较证明了显著改进。案例研究仅为实用演示，不构成核心成功结果。主观或人工评价仅存在于标签来源，符合冻结标签例外。因此严格匹配成立。

## Creating Proactive Cyber Threat Intelligence with Hacker Exploit Labels: A Deep Transfer Learning Approach

- Record: 11686
- Year / journal: 2024 / MIS Quarterly
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 反向审计未发现足以推翻初筛的主观或自报核心结果。全文核心成功主张是DTL-EL在固定exploit类别标签上的分类性能（accuracy、precision、recall、F1-score），并通过四项基准/消融实验证明其优于多个非迁移和迁移基线。目标域ground-truth虽经关键词筛选和人工核实，但这是冻结基准标签的构建过程，并非对模型输出质量的人工语义评分，符合benchmark_objective_with_fixed_labels例外；对抗注意力验证、CKA、UI演示和成本敏感分析均非核心成功证据。因此五个门槛均通过，confirmed_strict_match=true。

## Interleaved Design for E-Learning: Theory, Design, and Empirical Findings

- Record: 8352
- Year / journal: 2024 / MIS Quarterly
- Status / role: fully_objective / exclusive
- Reason: 初筛判定成立。文章核心贡献是提出并实例化相关交错设计的个性化学习系统，以提升学习绩效为最终目标。核心成功主张（H1、H2）完全基于系统自动评分的后测成绩，属于完全客观测量；主题掌握度和会话准确率作为机制证据同样来自系统客观记录。全文无主观评分、自报或混合核心贡献。人工输入（教师编码题目标签、专家知识图谱）仅用于系统构建和操纵检查，不影响结果测量的客观性。随机现场实验明确比较了相关交错与无关交错、非交错两种基准，并证明了统计显著的改善。因此符合严格客观指标正例。

## Timely, Granular, and Actionable: Designing a Social Listening Platform for Public Health 3.0

- Record: 11292
- Year / journal: 2024 / MIS Quarterly
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 反向审计未发现足以推翻初筛的证据。文章核心成功指标全部建立在预先固定的专家金标准标签上：数据实验和事件检测均为对计算模型/自动检测器的检索与分类性能评估，属于冻结标签基准；用户实验衡量的是人类分析师对固定金标准案例的分类准确率（precision/recall/F），不是主观感知、满意度或人工语义质量编码。文章没有报告或依赖任何主观量表作为核心结论。HealthSense是明确实现的软件制品，并通过16种基线/基准方法、消融分析、随机用户对照实验和统计事件检测相对基线证明了客观改善。因此五个门槛均满足，判定为严格匹配。

## Beyond Complements and Substitutes: A Graph Neural Network Approach for Collaborative Retail Sales Forecasting

- Record: 28640
- Year / journal: 2025 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现推翻初筛的证据。论文的最终目标确实是提升多步销售预测的完全客观指标MAE和RMSE。所有核心成功结果均直接来源于平台/交易系统记录的销售数据，无任何主观评分、自报或人工质量判断。制品设计明确（CL4RSF/MS2RSF），并通过与10个基准的对比及消融实验证明了客观改进。经济价值分析虽含运营成本估算，但仍是公式化计算，且为次要结果，不影响核心判断。

## Customer Acquisition via Explainable Deep Reinforcement Learning

- Record: 28396
- Year / journal: 2025 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: 全文所有量化核心成功结果均为完全客观的：以点击流日志和固定财务参数为基础的平均奖励（AR@1/3/6）贯穿模型性能比较、联邦学习验证、注意力权重有效性验证和广告渠道案例验证。不存在问卷、自报、专家评分或人工语义编码，也没有将主观/自报结果作为并列贡献。文章明确设计并实现了DRQN-attention这一软件制品，通过与多个基线的离线评估证明了其在长期平均奖励上的改进（至少与多数state-of-the-art方法相比竞争力强，且显著优于公司现行MAB），同时用客观指标支撑了注意力机制的可解释性价值。因此，五个门槛全部满足，初筛判定得以确认。

## Customer Engagement Prediction on Social Media: A Graph Neural Network Method

- Record: 28081
- Year / journal: 2025 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: 文章以提升顾客互动预测性能为核心目标，所有核心成功证据均来自Facebook平台自动记录的用户互动行为形成的冻结标签，并基于这些标签计算Accuracy/Precision/Recall/F1/AUC等确定性分类指标，与多个基线比较并取得显著提升。未发现任何主观、自报或人工质量评价指标作为核心成功依据。GPT-3.5自动标注仅用于构建输入特征，不影响结果指标客观性。经济价值分析为附加说明，删除后核心主张依然成立。因此符合严格客观指标正例标准。

## Enhancing User Privacy Through Ephemeral Sharing Design: Experimental Evidence from Online Dating

- Record: 28109
- Year / journal: 2025 / Information Systems Research
- Status / role: fully_objective / dominant
- Reason: 独立反向审计未发现足以推翻初筛的证据。核心成功结果均来自随机现场实验（70,275用户）中的平台日志客观指标：照片披露、人脸披露、匹配数、接收者消息数。所有核心指标均展示了显著改进，且制品（短暂分享照片上传功能）被明确设计和部署。在线实验中的主观隐私担忧、披露意愿等构念仅作为机制解释，删除后不影响核心成功主张；替代机制分析中使用的人工程序（面部吸引力众包评分等）仅用于排除替代解释或工具校准，不构成核心结果。因此五个门槛全部通过，定义为完全客观（主导角色），核心角色为dominant而非exclusive，因为作者在讨论中采用了主客观结合的方式表述隐私增强效果，但客观行为指标仍是核心贡献。

## Ephemeral State-Dependent Recommendation for Digital Content

- Record: 28570
- Year / journal: 2025 / Information Systems Research
- Status / role: fully_objective / dominant
- Reason: 反向审计后，初筛结论仍然成立。核心成功指标readrate、readtime、payment和demand spillover全部来自平台自动日志，属于完全客观测量。在线调查中的Likert自报只用于探索Schema/Isolation机制，不是制品有效性的核心证据，删除后不影响核心结论。文章确实设计并实质修改了推荐系统的决策规则/算法，并通过大规模随机现场实验，与多个状态独立基线和T3/T4互相比较，在阅读、支付和溢出等客观指标上证明了改进。因此五个门槛均为true，符合严格客观指标正例。

## Fast Forecasting of Unstable Data Streams for On-Demand Service Platforms

- Record: 28588
- Year / journal: 2025 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现推翻初筛的证据。文章设计并实现了明确的软件制品FFUDS，其最终目标是提高不稳定性环境下的大规模需求预测准确性和计算效率。所有核心成功结果（SMAPE、经济损失、计算时间、Citi Bike SMAPE）均源自平台/传感系统自动记录的需求计数、模型输出和计算机测量，不含任何人工评分、自报或主观感知测量。经济损失中的成本参数是平台提供的固定业务常量，不构成评价性主观权重；需求数据的线性缩放不影响相对比较。与多个基准和消融变体的比较在所有核心指标上显示了客观改善，并且这些指标是文章的最终优化目标和主要成功依据。因此维持第一阶段判定：strict match成立。

## Gaining a Seat at the Table: Enhancing the Attractiveness of Online Lending for Institutional Investors

- Record: 28414
- Year / journal: 2025 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: 全文核心成功主张均为基于LendingClub实际贷款现金流的IRR/ROI/PME，及基于市场指数价格的比较，客观、可复现；主观/自报/人工判断不存在于核心路径；GCPP是明确的计算制品，并完成了对多个基准的out-of-sample比较改善。偏差分析仅为附加分析，不改变核心。五个门槛均满足。

## Healthcare Cost Prediction for Heterogeneous Patient Profiles Using Deep Learning Models with Administrative Claims Data

- Record: 28160
- Year / journal: 2025 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现可推翻初筛的主观或混合核心证据。核心性能指标全部由行政索赔的实际支付金额客观计算，核心贡献是降低预测误差和支付差异；明确设计软件制品并通过多组对比和消融证明改进。因此确认严格匹配。

## HyperCARS: Using Hyperbolic Embeddings for Generating Hierarchical Contextual Situations in Context-Aware Recommender Systems

- Record: 28352
- Year / journal: 2025 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现足以推翻初筛的证据。全文所有核心成功结果均基于确定性计算指标：推荐性能来自固定历史交互标签上的预测误差/排序指标，聚类质量来自嵌入几何指标，可解释性来自自动决策树/IDS拟合指标而非人类评分。不存在问卷、自报、人工语义编码或专家总体评分作为核心结果，也没有主观机制/中介与客观指标并列构成混合核心贡献。HyperCARS方法实现了明确的软件制品，并在多个数据集上通过统计检验相对Euclidean基线和多种强基线显著改善，五个门槛全部满足，因此确认严格匹配。

## Irrationality-Aware Human Machine Collaboration: Mitigating Alterfactual Irrationality in Copy Trading

- Record: 28632
- Year / journal: 2025 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: 全文核心成功主张均基于ZuluTrade平台记录的实际交易行为与已实现盈亏结果，无问卷、自报、专家评分或人工语义编码。算法制品明确（RXGBoost与收缩程序），并在多个客观指标上相对于原始决策、XGBoost收缩、随机收缩、深度学习基线及多种变体展示了显著改进。机制分析是附属解释，不构成共同核心贡献。因此符合严格全客观指标匹配。

## Post-Earnings-Announcement Drift Prediction: Leveraging Postevent Investor Responses with Multitask Learning

- Record: 28378
- Year / journal: 2025 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: 初筛判定为严格正例。反向审计确认：文章核心目标是提升PEAD预测精度和经济收益，两个核心成功指标（EV和alpha）均基于真实市场数据和确定性计算，完全没有主观评分、人工质量判断或自报结果。辅助任务虽然包含文本情感等特征，但作为模型输入而非结果评价。所有核心贡献（预测精度、经济收益）都是客观的、独占性的，制品（MTL模型）被明确设计并通过与多个基准和消融对比证明了改善。因此五个门槛全部满足，严格匹配成立。

## Predicting Instructor Performance in Online Education: An Interpretable Hierarchical Transformer with Contextual Attention

- Record: 28089
- Year / journal: 2025 / Information Systems Research
- Status / role: benchmark_objective_with_fixed_labels / dominant
- Reason: 初筛判定基本准确。论文的核心是为 online education 构建一个内容驱动的教师/课程评分预测模型，核心成功指标是 frozen Coursera 评分标签上的 MSE/MAE，并通过与 14 个非深度学习基线、LectureBERT 和消融变体的比较证明改善，属于固定的众包标签 benchmark。AMT 随机实验虽然使用主观偏好，但被定位为平台应用展示，不支撑核心预测精度主张，因此可视为次级结果。综合五个门槛均通过；不过若将 AMT 实验视为与预测精度并列的核心贡献，则结论会转为混合并排除。

## Probing Digital Footprints and Reaching for Inherent Preferences: A Cause-Disentanglement Approach to Personalized Recommendations

- Record: 28598
- Year / journal: 2025 / Information Systems Research
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 经反向审计，未发现可推翻初筛的主观、自报或人工语义质量指标。核心成功结果（样本内购买预测和固有偏好导向推荐）的标签全部来源于平台自动行为日志或由观测日志经确定性抽样生成的固定标签；指标P、MAP、NDCG、AUC均由公式确定计算。决策路径验证和代理相关性验证属于机制解释而非核心成功主张，删除后不影响核心结论。制品DISC被明确设计并与多个基线和替代因果图比较，在真实数据集上展示显著改善。因此判定严格匹配。

## Walrasian Pricing for Combinatorial Markets with Compact-Bidding Languages: An Application to Truckload Transportation

- Record: 28638
- Year / journal: 2025 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: 经全文反向审计，未发现推翻初筛的证据。文章的核心贡献是设计并提出一个面向卡车运输组合市场的定价/分配机制 IDP，并用仿真实验证明其在总成本节约、参与方盈余和接近 Walrasian equilibrium 上的客观改善。所有核心成功指标均由随机生成的仿真数据、Mixed-Integer/LP 优化模型和确定性支付公式计算，不涉及问卷、自报、人工语义评估或主观总体评分。机制与 SMRA、VCG 和 with/without clique cuts 的对比明确展示了客观指标改善。主观或激励相关讨论（如 bid shading、manipulability）不是本文结果，删除后核心主张依然完整。

## From Detractors to Enhancers: Harnessing the Power of Ad Customization for User Engagement on Media Websites

- Record: 1882
- Year / journal: 2025 / Journal of the Association for Information Systems
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现推翻初筛的证据。核心成功结果全部来自现场实验的自动日志数据（访问时长、唯一页面数、回访率），均为完全客观的测量。预测试中的主观量表仅用于验证操纵设计的有效性，不属于核心成功结果。文章明确设计并部署了AQC软件功能，并通过随机现场实验与默认广告和无广告条件比较，证明了客观行为指标的显著改善。因此，五个门槛全部通过，objective_status为fully_objective，core_role为exclusive。

## GASP: A Graph Augmentation-Based Approach for Sign Prediction of Ties in Social Networks

- Record: 8182
- Year / journal: 2025 / Journal of the Association for Information Systems
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 初筛结论得到确认。文章核心目标是通过设计科学流程提出并评估GASP这一明确软件制品，以提升社交网络边符号预测性能。所有核心成功结果均为在固定目标标签上由确定性混淆矩阵计算出的分类指标（ACC、OP、Macro F1、GM(S,N)），并和多个最先进基线方法在多个基准数据集及IMDb演示网络上进行了系统比较，证明客观改善。虽然数据标签最初来源涉及人类行为或生物实验，但评价对象是计算模型对固定标签的预测性能，完全落入冻结标签例外。全文不存在并列的主观、自报或人工语义质量核心结果，删除任何此类内容均不影响核心主张。

## Automating in High-Expertise, Low-Label Environments: Evidence-Based Medicine by Expert-Augmented Few-Shot Learning

- Record: 13398
- Year / journal: 2025 / MIS Quarterly
- Status / role: benchmark_objective_with_fixed_labels / dominant
- Reason: 反向审计未能推翻初筛。文章核心目标是通过FastSR提升SR数据抽取的完全客观指标（句子分类和序列标注的F1、PRC等），评价对象是对固定专家PICO标签的预测性能，属于冻结标签基准例外。FastSR是明确设计的软件制品，并通过多数据集基准比较、广泛消融和确定性时间/成本模型证明改善。定性专家反馈和报告完整性比较为辅助适用性证据，删除后核心定量成功主张仍完整。WD/COVID测试集存在专家标注核查，但属于标签创建和验证而非对干预后文本质量的主观评价，不违反冻结标签例外。因此确认严格匹配。

## Mitigating Bias in Hate Speech Detection With a Small Number of Expert Annotations: A Prompt-Based Learning Approach

- Record: 27636
- Year / journal: 2025 / MIS Quarterly
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 全文所有核心成功结果均由模型预测与固定专家/金标准标签的确定性比较产生（FPR、FNR、Macro-F1、ACC、Avg SP），完全符合冻结标签例外。不存在问卷、自报、人工语义质量评分等主观结果，也没有并列的核心主观贡献。文章明确设计并实现了新的检测框架，并通过多个基准、消融和泛化实验证实了客观指标的显著改善。因此应确认初筛正例。

## RADAR: A Framework for Developing Adversarially Robust Cyber Defense AI Agents with Deep Reinforcement Learning

- Record: 27598
- Year / journal: 2025 / MIS Quarterly
- Status / role: fully_objective / exclusive
- Reason: The reverse-audit did not reveal disqualifying subjectivity. The paper's core success claims are the improved adversarial robustness of malware detectors (evasion rate reduction, FPR stability, repeated-game robustness) and the relative effectiveness of the r-VAC attack generator. These are all operationalized through automated malware detector outputs and deterministic formulas. Human expert consultation appears only in attack-vector selection and functionality validation, which is not a core outcome measure. The artifact is a concrete software framework with explicit algorithmic components, and improvement is demonstrated against multiple baselines and via pre/post comparisons. Therefore, the five gates are satisfied.

## Real-Time Sales Data, Streamer Improvisation, and Sales Performance: Evidence From Live Stream Selling

- Record: 15532
- Year / journal: 2025 / MIS Quarterly
- Status / role: fully_objective / exclusive
- Reason: 通过反向审计，未发现推翻初筛的充分证据。核心成功结果是预售产品销量，完全由平台交易系统自动记录，是客观测量；随机对照实验比较了有无实时数据功能的仪表盘（制品扩展）对销量的影响，处理组显著高于对照组（40.21%），比较改善明确。访谈和人工分类仅用于背景、机制说明和调节分析，删除后核心成功主张仍然完整。机制变量虽然基于文本分析，但通过ASR和LIWC等确定性程序计算，且不是核心成功结果。因此，所有门槛均通过，确认严格匹配。

## Ruckus in the Rentals, Seeking New Arrangements: Remedying the Impact of Home-Sharing on Urban Noise

- Record: 8796
- Year / journal: 2025 / MIS Quarterly
- Status / role: fully_objective / dominant
- Reason: 文章设计了一个具体、可实现的助推算法作为软件治理机制，其核心目标是通过排名调整减少完全客观的社会结果指标（噪音投诉），同时维持收入和偏好。所有核心成功结果均基于行政记录、平台交易和确定性模型计算，没有依赖主观评分或自报。模拟实验将算法干预情景与真实情景进行对比，展示了噪音减少、偏好增强和收入几乎不变的量化改善。文章同时包含实证分析，但算法是回答治理问题、提供解决方案的核心贡献之一，且所有核心评估指标均为客观。因此确认严格匹配。

## The Fog of Warnings: How Non-Security-Related Notifications Diminish the Efficacy of Security Warnings

- Record: 27642
- Year / journal: 2025 / MIS Quarterly
- Status / role: fully_objective / dominant
- Reason: The initial screening is upheld. The paper's central contribution is to demonstrate and mitigate generalization of habituation from notifications to security warnings. All three core hypotheses are evaluated with: (a) automatically logged unsafe-click choices, (b) automatically logged reaction times, and (c) fMRI BOLD activation. The subjective concern/realism ratings appear only as manipulation checks or auxiliary evidence that participants consciously distinguished warnings from notifications, not as core success outcomes. The supplementary MST human classification is also a robustness check. Thus the core success claim is fully objective and dominant. The study also designed and compared concrete warning UI variants, showing objective improvements: distinct visual appearance or distinct interaction mode reduced warning disregard and reaction-time decline attributable to generalization. Therefore all five gates are true.

## Mitigating Exposure Bias for Recommendations in Physical Spaces: An Unbiased Pairwise Ranking Approach Using Spatial Movement

- Record: 28582
- Year / journal: 2026 / Information Systems Research
- Status / role: benchmark_objective_with_fixed_labels / exclusive
- Reason: 反向审计未发现足以推翻初筛的主观或自报结果。文章核心贡献是提出并实现 UMPR 推荐算法，核心成功指标是 Recall/DCG，在固定 ground-truth（智能视频系统记录的真实进店标签）上计算，且通过 12 个基线、2 个消融对照、增量收入模拟和公平性指标比较证明改善。增量收入和公平性虽是扩展分析，但都建立在对核心客观准确率改善的基础上，没有混合主观质量评价或人工评分。经济收益模拟的假设是客观参数，不改变核心结论。五个门槛均满足。

## Toward Sustainable Electricity Markets: Capacity-Based Pricing for Electric Vehicle Smart Charging

- Record: 28578
- Year / journal: 2026 / Information Systems Research
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现推翻初筛的证据。文章核心贡献是一个IS-enabled容量基定价制品及其价格设定启发式，所有核心成功结果均由仿真模型产生的聚合需求曲线和价格/收入公式直接计算，完全客观。不存在用户满意度、自报行为、人工质量编码等主观测量，也没有以主观结果为并列核心贡献。制品通过多智能体仿真在多个真实校准场景中与多种基准（真实平定价、时变定价、递增阶梯定价）比较，在RMSE、Peak、PAPR和Revenue目标偏差上均展现明确改善。所有五个门槛均满足，objective_status为fully_objective，core_role为exclusive，故确认为严格匹配。

## Latent Similarity-Enhanced Credit Risk Prediction

- Record: 27625
- Year / journal: 2026 / MIS Quarterly
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现足以推翻初筛的证据。全文的核心成功主张完全由AUC、Precision、Recall、F1、Accuracy、Macro F1、MAE等客观预测性能指标支撑，这些指标基于银行系统自动记录的还款行为冻结标签，模型为纯计算制品；案例研究经济利润虽然涉及银行提供的业务参数，但属于secondary 演示，删除后核心主张仍完整。不存在问卷、自报、人工质量评分或混合核心贡献，因此确认严格匹配。

## Shapley Value-Based Feature Attribution for Data Masking

- Record: 27640
- Year / journal: 2026 / MIS Quarterly
- Status / role: fully_objective / exclusive
- Reason: 反向审计未发现足以推翻初筛的主观或非核心指标问题。文章以降低推断性披露风险并保持数据效用为最终目标，所有核心成功结果均为R²/AAD/RASD的确定性计算；不存在人工语义编码、专家总体评分、自报依赖或需要主观评价才能成立的核心贡献。提出的Algorithm 1构成明确的软件制品/方法实现，并通过与两个基准方法在模拟和三个真实数据集上的比较，证明了客观指标的改善。因此，五个门槛全部满足，确认严格客观正例。
