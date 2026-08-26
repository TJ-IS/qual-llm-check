# 51 篇命中文献数据源与内容摘要

## [1] 2020 | Journal of Management Information Systems | A Novel Recommendation Model for Online-to-Offline Service Based on the Customer Network and Service Location
- 数据集: MovieLens 100K | Dianping 官方公开网站数据 | Google Maps 地理数据
- 核心指标: Precision; Recall; F-Score
- Benchmark评价: 在MovieLens 100K这一公开标准推荐数据集上评价CNRec（不含位置信息的网络推荐）及对比方法；同时在Dianping O2O数据上评价CNLRec/CNRec/LRec。结果显示CNLRec和CNRec在低数据密度条件下显著优于CF、MF、DL、CL、NN等方法。
- 判定理由: 该文以Precision、Recall、F-Score等完全客观的推荐性能指标为唯一核心成功标准，研究问题、实验设计和贡献声明均围绕提升推荐性能展开；全文在实验部分以MovieLens 100K作为明确命名的公开基准评价场地，并与广泛使用和最新推荐方法进行对比，构成对核心提升主张的证据；核心对比结果包含公开可获取的MovieLens 100K数据集，因此三个模块均通过。

## [2] 2020 | Decision Support Systems | A dynamic classification unit for online segmentation of big data via small data buffers
- 数据集: Lev dataset | UCI Occupancy-Detection dataset | Kaggle deepScapulaSSM dataset
- 核心指标: 运行时间; 段内距离 RMSE（均值/标准差）; 最终段数/更新次数
- Benchmark评价: 在 UCI Occupancy-Detection 和 Kaggle deepScapulaSSM 等公开数据集上，对静态、动态、增量动态三种方法进行系统比较，报告最终段数、RMSE 均值/标准差、运行时间，并用动态无限制缓冲作为参照验证增量动态分割结果的相似性。
- 判定理由: 客观指标模块通过：核心成功指标是运行时间、RMSE、段数等可直接观测的计算结果；论文唯一核心贡献是增量动态分割机制及其效率/保真度提升。Benchmark 模块通过：虽未使用 benchmark 一词，但论文明确命名 UCI Occupancy-Detection 等公开标准数据集，并以其为评价场地，与静态、动态参照方法进行系统比较，结果用于支持核心效率主张。Dataset 模块通过：UCI Occupancy-Detection 和 deepScapulaSSM 均可公开获取，且核心结果表基于这些公开数据。因此 strict_include=true。

## [3] 2020 | Information & Management | Discovering event episodes from sequences of online news articles: A timeadjoining frequent itemset-based clustering method
- 数据集: TDT2 | TDT3 | Nallapati et al. event corpus（基于 TDT2/TDT3 构建）
- 核心指标: 聚类召回率（Cluster Recall）; 聚类精确率（Cluster Precision）; F-measure
- Benchmark评价: 在 Nallapati et al. 的事件语料（来自 TDT2/TDT3，含 53 个事件、248 个 episode、1468 篇新闻）上评价 TAFIED，并与 FIHC、HAC、HAC+TD 等基准方法比较。使用 PRT 曲线、最佳 F-measure 及 Wilcoxon 检验；TAFIED 的 F-measure 为 0.584，优于 FIHC 的 0.543、HAC 的 0.533、HAC+TD 的 0.567，且差异显著。
- 判定理由: 核心目标完全客观：全文以 cluster recall、cluster precision、F-measure 作为唯一核心成功指标，评价 TAFIED 方法在事件 episode 发现上的性能提升；没有主观量表或并列核心贡献。全文存在明确的 benchmark 表述，摘要和第4.2节均将 FIHC、HAC、HAC+TD 称为 benchmarks，并在评价语境中用这些基准方法作为参照，比较结果直接支撑核心提升主张。数据来源清晰：使用 Nallapati et al. 的事件语料，其源自公开的 TDT2/TDT3 语料，可公开获取，且核心结果表基于该数据。三个模块均通过，故 strict_in

## [4] 2020 | Decision Support Systems | Geo-semantic-parsing: AI-powered geoparsing by traversing semantic knowledge graphs
- 数据集: NEEL16 (2016 Named Entity Recognition and Linking Challenge official dataset)
- 核心指标: F1分数; Precision; Recall; 平均处理时间
- Benchmark评价: 在公开NEEL16数据集（含9289条英文推文、5348个地点标注）上，将GSP与2个baseline（naïve geoparser、NER+geocoder）和3个现有技术（Middleton et al.、Halterman、Avvenuti et al.[2]）比较，报告precision、recall、F1和elapsed time。结果显示GSP获得F1=0.665，显著优于所有对比方法（次优Avvenuti F1=0.553，Halterman F1=0.309，其余更低），从而支持GSP的核心提升主张。
- 判定理由: 客观指标：geoparsing的precision/recall/F1/elapsed time完全客观，目标是预测NEEL16中事实性的地点坐标，标签为外部事实，不涉及主观感知；唯一核心目标：全文研究问题、设计目标、评价和贡献均围绕提升geoparsing性能，无并列理论、主观或政策贡献；Benchmark：第6.2节以'Benchmarks'小标题明确陈述基准比较，与2个baseline和3个现有SOTA方法在NEEL16数据集上比较，表2直接支撑GSP优于竞争者的核心主张，具有明确参照点；数据集：核心评价数据为公开的NEEL16官方挑战数据集，公开可查、可获取，且所有关键结果表基于该数据

## [5] 2020 | Information Systems Research | Hiding Sensitive Information when Sharing Distributed Transactional Data
- 数据集: Retail | BMS-POS
- 核心指标: 共享数据集准确率（未净化事务占比）
- Benchmark评价: 在真实数据集Retail、BMS-POS及合成数据集上，将Ensemble方法与CPLEX求得的最优解和Verykios et al. (2004)的方法比较，核心指标是净化事务数和相对最优解的Gap。结果显示Ensemble非常接近最优解，而Verykios方法Gap较大且无法处理合成大数据库。
- 判定理由: 文章核心是以最小化净化事务数量/最大化共享数据集准确率为唯一核心目标的分布式敏感项集隐藏问题，提出Ensemble方法，并在真实公开数据集Retail、BMS-POS以及合成数据集上与最优解和既有方法进行benchmark比较。客观指标是核心且唯一；存在明确benchmark表述和比较基准；核心评价使用了公开可获取数据集。三个模块均通过。

## [6] 2020 | Journal of Management Information Systems | Human Identification for Activities of Daily Living: A Deep Transfer Learning Approach
- 数据集: HANDY | Opportunity (OPPO)
- 核心指标: 宏平均精确率 (Precision); 宏平均召回率 (Recall); 宏平均F1分数; 微平均准确率 (Accuracy); ROC 曲线下面积 (AUC)
- Benchmark评价: 实验1在HANDY数据集上将CNN-HID与经典ML基准(kNN, SVM, NB, DT)及变体CNN-HID/T、CNN-HID/CA比较；实验2/3/4在OPPO四个对象传感器数据集上将DTL-HID与非迁移学习基准及其他DTL变体比较，报告了各模型的Accuracy、Precision、Recall、F1和AUC。结果证明DTL-HID在核心客观指标上显著优于所有基准。
- 判定理由: 客观指标方面：HID任务的身份标签为外部可核验事实，核心评价指标均为Accuracy/Precision/Recall/F1/AUC，不包含任何主观构念。唯一核心目标：研究问题、实验设计和贡献声明均以提升对象传感器上的HID性能为核心，设计原则和实用启示是从评估中衍生的附加讨论，不构成并列核心目标。Benchmark方面：全文在摘要和Evaluation Design中明确使用benchmark表述，在实验部分设计了系统化的基准比较（kNN/SVM/NB/DT及CNN-HID变体），基准比较直接支撑核心提升主张，且每个比较均有明确参照点。数据集方面：HANDY（公开Benchmark数据集）和

## [7] 2020 | Journal of Management Information Systems | Mining Semantic Soft Factors for Credit Risk Evaluation in Peer-to-Peer Lending
- 数据集: Lending Club 个人贷款数据
- 核心指标: 违约预测判别性能（AUC、KS、H measure）; 授信组合绩效（所选组合的违约率）
- Benchmark评价: 在Lending Club数据集上，使用LR、LASSO、RF、XGB四种模型，对硬特征、语义软特征、硬特征+语义软特征进行判别性能比较；进一步与LDA主题特征、统计/可读性/情感等软特征比较，并模拟授信组合绩效，以平台信用子级为参考线。核心结论是加入语义软特征显著提升AUC、KS、H measure并降低组合违约率。
- 判定理由: 核心结果是违约预测与授信组合违约率，均基于客观事实标签并采用AUC/KS/H measure等确定性指标；研究问题、评价结构和贡献声明均围绕“提取语义软因子并提升信用风险评估性能”这一唯一核心目标展开。全文在实证评估部分明确将logistic regression作为benchmark method，并对硬特征、语义软特征和多种基线特征进行系统比较，该比较结果是核心提升主张的直接证据。评价数据来自公开可获取的Lending Club历史贷款数据，独立研究者可凭论文信息查得并获取。因此三个模块均通过。

## [8] 2020 | Decision Support Systems | Network projection-based edge classification framework for signed networks
- 数据集: Epinions | Slashdot Zoo | Wikipedia RfA | Yeast GIN
- 核心指标: Accuracy（分类准确率）; Geometric Mean（几何均值）; Diagnostic Odds Ratio（诊断优势比）
- Benchmark评价: 在四个公开数据集上（平衡/非平衡预处理后），以 60%、65%、70%、75%、80% 的标记边作为已知信息，对比 NPECF、SRWR、NbA 三类方法，报告 Accuracy、Geometric Mean、Diagnostic Odds Ratio。结果显示 NPECF 在绝大多数设置下高于 SRWR 和 NbA。
- 判定理由: 该文以符号网络边分类中 Accuracy、Geometric Mean、Diagnostic Odds Ratio 三个客观分类性能指标为唯一核心目标和贡献；没有主观量表或并列理论贡献。论文明确命名 Epinions、Slashdot Zoo、Wikipedia RfA、Yeast GIN 四个公开标准数据集作为评价场地，并在实验中与 SRWR、NbA 等明确参照方法比较，benchmark 评价直接支撑核心提升主张。这四个数据集均公开可查、可获取，且核心结果表基于这些数据。因此三个模块全部通过。

## [9] 2020 | Information Systems Research | Predicting Labor Market Competition: Leveraging Interfirm Network and Employee Skills
- 数据集: LinkedIn公开个人资料 | Yahoo BOSS API | Compustat North America数据库
- 核心指标: AUC（ROC曲线下面积）; 新劳动力市场竞争者识别比例（proportion of new future competitors identified）
- Benchmark评价: 论文在自建的企业对年度面板上，比较KNN、LR、SVM、CART、Bag(LR)、Bag(SVM)、RF、MLP、CNN等模型，并在经济、产品重叠、劳动力重叠、网络重叠四类特征集上增量比较；核心证据为Table 6的AUC提升以及Table 7的新竞争者识别比例提升。
- 判定理由: 客观指标方面，核心结果变量为客观可观测的未来雇员流动HCF，评价指标AUC和识别比例均客观，且预测性能提升是全文唯一核心目标与贡献；benchmark方面，虽无命名公开基准任务，但在评价语境中明确将KNN描述为benchmark，并与多类baselines和随机分类器比较，构成核心证据；数据集方面，核心评价基于公开可获取的LinkedIn公开个人资料、Yahoo BOSS API和Compustat订阅数据，论文明确描述获取方式且结论强调只用公开数据。三个模块均通过。

## [10] 2020 | Information & Management | What reveals about depression level? The role of multimodal features at the level of interview questions
- 数据集: DAIC-WOZ
- 核心指标: 抑郁严重程度预测误差（PHQ-8 分数的 MAE 与 RMSE）
- Benchmark评价: 在 DAIC-WOZ 的142名受访者、7866条问题级回答上，用五折交叉验证训练两层模型，并与单模态/双模态基线（B1）和个体层基线（B2_SVR/B2_RF）比较，报告 MAE/RMSE 并进行 t 检验。
- 判定理由: 核心指标是 PHQ-8 抑郁严重程度预测的 MAE/RMSE，属于疾病状态事实标签上的客观性能提升；研究目标、模型设计和贡献声明均围绕提升抑郁检测性能展开，不存在并列的主观或理论核心目标；评价以公开标准数据集 DAIC-WOZ 为基准，并与明确的基线模型比较；DAIC-WOZ 作为公开研究语料库可通过研究申请获取，因此三项门槛均通过。

## [11] 2020 | Journal of the Association for Information Systems | Who Is the Next “Wolf of Wall Street”? Detection of Financial Intermediary Misconduct
- 数据集: BrokerCheck (FINRA) | LinkedIn
- 核心指标: 准确率; 召回率; 精确率; F1分数; AUC; 经济收益
- Benchmark评价: 在自然分布样本上，作者将包含 regulator-confirmed 信息的分类器 C 和 D 与仅基于 self-disclosed 信息的分类器 A 和 B 作为基准进行系统比较，使用 McNemar 检验。结果显示 C/D 在多个机器学习方法上显著优于 A/B（例如 RF 的 C/A 和 D/A 均 p<0.01），从而为核心主张（regulator-confirmed 信息提升检测性能）提供关键证据。附录 D 中还将 D 与 E/F 基准比较。
- 判定理由: 客观指标：核心目标构念为金融中介是否发生不当行为，基于 FINRA BrokerCheck 最终监管披露记录，属于客观事实标签；评价指标全部为分类性能（准确率、召回率、精确率、F1、AUC）和经济收益，不含任何主观量表或人类语义评判。唯一核心目标：研究问题、设计目标、评价结构和贡献声明均围绕自动化检测金融中介不当行为的性能提升展开，理论仅作为特征选择和解释依据，不构成并列核心目标。Benchmark：全文存在明确的 benchmark 表述（Table 11 标题明确以 Classifiers A/B 为 Benchmarks），该基准评价位于结果部分，并为核心主张（加入监管确认信息提升检测性

## [12] 2021 | MIS Quarterly | A Deep Learning Approach for Recognizing Activity of Daily Living (ADL) for Senior Care: Exploiting Interaction Dependency and Temporal Patterns
- 数据集: Opportunity (OPPO)
- 核心指标: 宏平均F1; Accuracy; 平均块Levenshtein距离(ABLD)
- Benchmark评价: 四个实验分别将I-CNN、I-CNN-GR、S2S_GRU和整个层次ADLR框架与kNN、SVM、CNN-1D、CNN-2D、DeepConvLSTM、决策树、HMM、S2S_LSTM、SAE+SVM、LDA主题模型等基准比较，在INTER、OPPO-ML和OPPO-HL上报告F1、Accuracy、Acc@1/2、ABLD，并用配对t检验验证提升。
- 判定理由: 客观指标方面，核心构念是固定ADL/交互/手势标签上的分类与序列识别性能，不依赖人的主观体验；核心目标是设计并评价一个多层次ADLR框架，全文无主观量表作为成功标准。benchmark方面，作者明确使用benchmark/benchmarks表述，在实验部分将各组件和整体框架与SVM、DeepConvLSTM、HMM、主题模型等基准比较，且结果直接支撑准确率提升主张。数据集方面，核心端到端、手势和活动识别评价基于公开的Opportunity数据集，虽然INTER为自采，但仅用于交互提取组件，属于公开数据主导、少量私有补充，符合混用标准。因此三个模块均通过。

## [13] 2021 | Information Systems Research | A Graph-Based Ant Algorithm for the Winner Determination Problem in Combinatorial Auctions
- 数据集: Lau and Goh (2002) test instances | Combinatorial Auction Test Suite (Leyton-Brown et al. 2002)
- 核心指标: 求解质量（solution quality）; 计算时间（runtime）; 改进解概率（ISP）; Z分数
- Benchmark评价: 在94个Lau and Goh (2002)公开测试实例上运行TrACA，并与20种现有启发式（如MA、BHS、DDCM、ACLS、SHH、GA、DE、BRKGA等）以及CPLEX和Max W Clique两种精确算法进行系统比较。通过中位数检验、ISP、Z分数和平均解质量提升等客观指标报告结果。
- 判定理由: 本文提出一种求解组合拍卖胜者确定问题（WDP）的蚁群算法TrACA，核心目标是在短时限内提高WDP求解质量和速度。核心指标为求解质量（相对最优解的百分比）、运行时间、达到最优的时间、统计比较指标（ISP、Z分数等），全部客观、可计算、不依赖人的主观评价。研究问题、实验设计和贡献声明均围绕该算法在公开测试实例上的性能提升展开，没有并列的主观或理论核心目标。论文在实验部分明确使用公开测试实例（Lau and Goh 2002和CATS），以‘benchmark heuristics’为对照，并与20种现有启发式和CPLEX、Max W Clique等精确算法进行系统比较；这些比较直接支撑核心提升主

## [14] 2021 | Decision Support Systems | A personalized paper recommendation method considering diverse user preferences
- 数据集: AMiner | DBLP
- 核心指标: Precision/Recall（Top-N推荐命中率）
- Benchmark评价: 在AMiner和DBLP两个公开学术数据集上，将PRHN与BC、CC、MSCN、CAR、Metapath五种baseline方法比较Top-N推荐性能；主结果图（Fig.6、Fig.7）显示PRHN在Precision和Recall上优于baseline。
- 判定理由: 文章以Top-N推荐的Precision和Recall两个确定性客观指标为核心目标，全文没有主观量表、专家评分或并列的理论/政策贡献；在公开命名的AMiner和DBLP数据集上，以BC、CC、MSCN、CAR、Metapath为baseline进行系统化基准对比，benchmark评价直接支撑核心性能提升主张；两个数据集均公开可查、可获取且核心结果表完全基于它们。因此三模块均通过。

## [15] 2021 | Information & Management | A social investing approach for portfolio recommendation
- 数据集: eToro.com social investing platform posts | WRDS database (financial statement data) | Yahoo Finance (stock and market price data)
- 核心指标: 投资组合收益率; Treynor比率; Jensen's alpha
- Benchmark评价: 在eToro帖子和财务数据基础上构建组合，用30个交易日模拟交易；以S&P500为市场基准，以无过滤、仅知识、仅权威三种推荐方法为代表基准方法，比较组合收益率、Treynor比率和Jensen's alpha；CIR在多数绩效指标上优于其他基准。
- 判定理由: 核心成功指标为组合收益率、Treynor比率和Jensen's alpha，全部是客观可审计财务绩效，且全文唯一核心目标是构建并验证能提升这些指标的投资组合推荐机制；第5节明确用'benchmark approaches'表述并列出无过滤、知识型、权威型三种基准与S&P500进行比较，评价与核心提升主张直接相关；核心评价所用数据来自公开的eToro.com平台、WRDS数据库和Yahoo Finance，均可识别并可获取。三个模块均通过，严格纳入。

## [16] 2021 | Decision Support Systems | Capital shortfall: A multicriteria decision support system for the identification of weak banks
- 数据集: V-Lab SRISK | NUS Credit Research Initiative (CRI) PD/AS | IMF Country Level Core Financial Soundness Indicators (FSI) | World Bank Global Financial Development Database (GFDD) | Bloomberg
- 核心指标: 总体分类精度（OCA）、平均分类精度（ACA）、灵敏度（SENS）、特异度（SPEC）、AUROC、KS距离
- Benchmark评价: 第5.1节（Comparison with other measures）将UTADIS（S1规格）与逻辑回归、SRISK和Texas Ratio在Global/U.S./Europe样本上就OCA、ACA、SENS、SPEC、AUROC进行系统比较；Table 9显示UTADIS在所有区域和测试方式下均优于各基准。
- 判定理由: 客观指标：核心目标是构建基于UTADIS的DSS以识别可能面临资本需求的弱银行，标签来自监管压力测试和资本注入事实，评价指标全部为客观分类性能指标（OCA、ACA、SENS、SPEC、AUROC、KS），且无主观量表或并列核心贡献。Benchmark：全文存在明确的benchmark表述（引言‘we benchmark the UTADIS model against logistic regression’，第5.1节比较部分），且在评价语境中与LR、SRISK、Texas Ratio等明确参照点比较，结果证据支持UTADIS提升预测精度的核心主张。数据集：所有数据来源均可在全文识别且公开可

## [17] 2021 | Decision Support Systems | Dynamic self-organizing feature map-based models applied to bankruptcy prediction
- 数据集: Diane database (Bureau van Dijk)
- 核心指标: 正确分类率; F2 分数; AUC
- Benchmark评价: 作者将提出的动态模型与 Cox 生存模型、SVM、ELM、Bagging、AdaBoost、XGBoost、Random Subspace、Random Forest 等方法在相同样本上比较，使用正确分类率、F2 和 AUC 三种指标；结果表格（表8-11）显示动态模型普遍优于基准模型。
- 判定理由: 文章以破产预测正确率、F2 和 AUC 作为唯一核心成功指标，破产状态属于可核验的外部事实标签；全文存在明确的 benchmark 表述（第4节将传统模型作为基准），且比较结果直接支撑核心改进主张；核心评价数据来自可公开获取的商业订阅数据库 Diane（Bureau van Dijk），因此三个模块全部通过。

## [18] 2021 | Journal of Management Information Systems | First, Do No Harm: Predictive Analytics to Reduce In-Hospital Adverse Events
- 数据集: Florida Agency for Health Care Administration (AHCA) 住院患者出院数据 | Hospital Compare (CMS) | Physician Compare (CMS) | American Hospital Association Healthcare IT Database
- 核心指标: AUC（受试者工作特征曲线下面积）; 精确率、召回率、F分数; 防止的AE数量与误报数量; 成本节省（百万美元）
- Benchmark评价: SALT在佛罗里达AHCA住院患者数据集上，与GLMM、MERT、MERF（Evaluation 1）以及CART、DNN、GBM、LR、NB、RF、SVM（Evaluation 2）进行系统比较，报告AUC、精确率、召回率和F分数。Evaluation 3进一步与GLMM和LR比较模拟中的防止AE数量和误报数。benchmark结果用于支持SALT预测性能提升的核心主张。
- 判定理由: 客观指标：核心成功指标为AUC、精确率、召回率、F分数、防止AE数量与成本节省，基于AE事实标签（ICD-9-CM编码+UMAEC清单+POA指示器）和财务计算确定，完全不依赖人类主观评价。唯一核心目标：研究目标、评价结构和贡献声明均围绕预测性能提升展开，无其他并列核心目标。Benchmark：在评价语境中明确使用“benchmarks”指代GLMM、LR等基线，并通过多个数据划分点比较，结果支持核心性能提升主张，且存在明确参照点。数据集：核心评价使用佛罗里达AHCA医院出院数据，该数据是州政府公开数据，可公开查找和获取；辅助数据源也是公开的。因此三个模块均通过。

## [19] 2021 | Decision Support Systems | Model identification for ARMA time series through convolutional neural networks
- 数据集: 
- 核心指标: AR/MA阶数识别准确率; AR/MA阶数识别MSE; 计算时间; 预测误差MAE/RMSE
- Benchmark评价: 在10,000条模拟ARMA时间序列（长度分别为1,000、3,000、10,000）上，将CNN与AIC step-wise、AIC full、BIC step-wise、BIC full四种传统方法比较，评价AR阶准确率、MA阶准确率、两者同时正确率、MSE、计算时间，并使用Acme（真实阶数）作为预测误差的参照。
- 判定理由: 客观指标方面：核心指标全部为可确定性测量的客观值，包括AR/MA阶数识别准确率、识别MSE、计算时间、预测MAE/RMSE，不涉及人类主观评价。唯一核心目标：全文围绕提升ARMA模型识别准确率和速度这一客观性能目标展开，没有并列的主观或理论贡献。Benchmark方面：第4.1节明确使用“performance benchmarking”表述，将CNN与AIC step-wise/full、BIC step-wise/full在统一测试套件上比较，且该比较直接支持核心提升主张，并有明确参照点。数据集方面：虽然使用模拟数据，但测试数据由公开R包forecast的arima.sim函数和公开发表的

## [20] 2021 | Decision Support Systems | Neighbor-aware review helpfulness prediction
- 数据集: 
- 核心指标: 分类准确率（Accuracy）
- Benchmark评价: 在六个真实评论域（D1-D6）上，将NAP与独立预测、MLP编码器、以及六种上下文方法（I+ORD_D, I+ORD_R, I+ORD_V, I+CON, I+POL, I+ENT）系统性比较，报告准确率并进行t检验。结果显示NAP显著优于所有baselines 1%-5%。该benchmark评价直接支撑核心准确率提升主张。
- 判定理由: 该文以完全客观的分类准确率为唯一核心目标，预测的标签是用户投票行为形成的冻结事实标签，无任何主观量表或语义评价作为成功标准。作者明确使用“benchmark”一词描述系统化基准比较（against a series of baselines），并将该比较作为证明核心准确率提升的关键证据，且具有多个明确参照点（baselines和独立预测）。数据来自SiteJabber和ConsumerAffairs两个公开评论平台，论文详细说明了来源和采集方式，独立研究者可凭论文信息获取该数据，且所有核心结果均基于该公开数据。因此三个模块全部通过，strict_include为true。

## [21] 2021 | Decision Support Systems | Process data properties matter: Introducing gated convolutional neural networks (GCNN) and key-value-predict attention networks (KVP) for next event prediction with deep learning
- 数据集: BPI'11 (Hospital Log) | BPI'12 | BPI'13 | Helpdesk | EnvLog
- 核心指标: 准确性（accuracy）; 精确率（precision，加权/宏/微）; 召回率（recall，加权/宏/微）; F1分数（F1-score，加权/宏/微）
- Benchmark评价: 在11个真实事件日志基准数据集及若干子集上，以10折交叉验证评价GCNN、KVP，并与自行复现的LSTM、SAE以及文献中的LSTM、SAE、RegPFA、MANN、CNN等结果比较；报告accuracy、precision、recall、F1-score。结果显示KVP和GCNN在44个metric-dataset组合中有34个超过先前方法，并在统计检验、过程数据属性分析等部分继续以这些基准数据为评价场地。
- 判定理由: 客观指标：核心成功指标为下一事件预测的accuracy、precision、recall、F1等基于事件日志事实标签的客观分类指标，无主观构念。核心目标：论文唯一核心目标是提出GCNN和KVP并证明其在客观预测指标上优于现有方法；过程数据属性讨论和选择指导是辅助性分析而非并列核心贡献。Benchmark：全文多次明确使用“11 real-life benchmark datasets”及“benchmark approaches”，评价位于实验/结果部分，且通过表3与多个baseline/文献方法比较，直接支撑核心提升主张。数据集：BPI'11、BPI'12、BPI'13、Helpdesk、E

## [22] 2021 | Decision Support Systems | Recognition of human activities for wellness management using a smartphone and a smartwatch: A boosting approach
- 数据集: ExtraSensory dataset
- 核心指标: Accuracy/F1/AUC
- Benchmark评价: 在ExtraSensory数据集上，作者对五个基本活动分别构建二分类模型，使用138个特征训练XgBoost、AdaBoost和Boosted C5.0，报告验证AUC和测试Accuracy/F1；随后又与Neural Network、SVM、LR、MLP等标准机器学习方法在相同数据上比较，并引用先前研究在相同数据上的结果作为参照。
- 判定理由: 文章以提升HAR分类客观性能（accuracy/F1/AUC）为唯一核心目标；评价基于公开可获取的ExtraSensory数据集，全文明确将该数据集作为模型训练与测试场地，并与多种传统机器学习方法及先前研究结果进行比较；无主观体验、用户满意度或语义质量评价作为核心成功标准，因此三个模块均通过。

## [23] 2021 | Decision Support Systems | Simpler is better: Lifting interpretability-performance trade-off via automated feature engineering
- 数据集: OpenML100 datasets (OpenML database) | credit-g / German Credit (UCI/OpenML task 31)
- 核心指标: AUC（测试集上的曲线下面积）; 模型复杂度/可解释性（参数数量倒数）
- Benchmark评价: 在 30 个 OpenML100 二分类数据集上，按每个数据集的 10 个 train/test 划分训练 vanilla logistic regression、default/tuned gbm、default svm 及对应的 SAFE refined logistic regression，报告 AUC 和标准差；同时用参数数量倒数衡量 interpretability，并通过 Wilcoxon 检验比较 AUC 与可解释性。结果用于支持 SAFE 能提升简单模型表现、维持性能并显著提升可解释性的核心主张。
- 判定理由: 核心评价完全基于客观指标：AUC 表现和参数数量倒数化的可解释性。论文的核心目标是同时提升/保持这两个客观指标，没有主观量表、用户调研或理论机制作为并列核心贡献。全文在实验部分明确使用 OpenML100 作为命名 benchmark，并与 vanilla logistic regression、默认/调优 gbm、默认 svm 等明确参照进行比较。核心结果表基于公开可获取的 OpenML/UCI 数据集，且代码公开。因此三个模块均通过，strict_include=true。

## [24] 2022 | Decision Support Systems | A deep recurrent neural network approach to learn sequence similarities for user-identification
- 数据集: Comscore Web Behavior Panel
- 核心指标: 用户再识别准确率（P）; 聚类调整兰德指数（ARI）; 估计用户数的精确率/召回率
- Benchmark评价: 在Comscore点击流数据上，将TL-RNN与Smith-Waterman序列比对和TF-RW度量对比，在双选择用户再识别、多用户分配和用户数估计三个任务中报告准确率、ARI、精度/召回率等，结果表显示TL-RNN在多数设置下优于基准方法。
- 判定理由: 该文核心目标是提出TL-RNN框架以提升序列相似性度量的客观预测性能（用户再识别准确率、ARI、精确率/召回率），评价指标全部基于外部可核验的用户身份标签，无主观构念；全文存在明确的benchmark表述（摘要和Benchmark methods节），并与Smith-Waterman、TF-RW等基准方法比较，benchmark评价直接支撑核心提升主张；核心评价数据来自Comscore Web Behavior Panel，该数据集可通过Comscore公开商业渠道识别和获取，且所有主要结果表均基于该数据。因此三个模块全部通过，strict_include=true。

## [25] 2022 | Decision Support Systems | Analysis of third-party request structures to detect fraudulent websites
- 数据集: Alexa.com top 50 websites | European Commission Counterfeit and Piracy Watch List | USTR 2019 Review of Notorious Markets for Counterfeiting and Piracy | Wikipedia list of fake news websites | EasyPrivacy list | Cookipedia database
- 核心指标: 准确率 (Accuracy); 敏感性 (Sensitivity); 特异性 (Specificity); 精确度 (Precision); F1分数; Matthews相关系数 (MCC); Youden J统计量
- Benchmark评价: 作者构建并报告了多组基准评价：1) 三种朴素基准（全判合法、全判欺诈、50/50随机）；2) 基于既有第三方使用（3PU）数据的方法（如CS5、svmRadial）作为基线；3) 对比提出的第三方请求结构（RS）数据模型、组合3PU+RS数据模型。结果显示RS及组合模型在准确率、F1、MCC等客观指标上显著优于基准，如组合CS5将准确率从0.728提升至0.805，加权集成达0.826。
- 判定理由: 本文核心目标是通过第三方请求结构特征预测网站欺诈状态，提升检测性能。被预测的欺诈/合法标签来自公开权威来源，属于固定事实标签，核心评价指标（准确率、F1、MCC等）均为客观分类性能指标，且论文通篇未引入主观体验或语义质量评价作为成功标准。全文存在明确的benchmark表述：在Section 5.1使用三种朴素预测方法进行benchmark比较，并在后续与既有3PU数据模型系统对比，benchmark结果直接支撑了核心提升主张。数据集来源为公开可获取的名单（Alexa、欧盟委员会、USTR、维基百科）及公开的第三方属性数据源，文章清楚描述了来源和获取方式，独立研究者可据此复现。因此三个条件全部

## [26] 2022 | Journal of Management Information Systems | Assessing and Enhancing Adversarial Robustness of Predictive Analytics: An Empirically Tested Design Framework
- 数据集: Deceptive Opinion Spam dataset (Ott et al., 2013) | Apache SpamAssassin public corpus
- 核心指标: 对抗鲁棒性性能比率（Performance Ratio）; 性能-扰动曲线下面积（A/P AUC, P/P AUC, R/P AUC, F/P AUC, ROC/P AUC）
- Benchmark评价: 在垃圾评论检测和垃圾邮件检测两个测试床上，将ARText系统（集成学习+对抗重训练）与NB、RF、SVM、CNN、GRU、BiGRU、LR、LSTM、BiLSTM等基准模型进行系统比较，采用性能比率和性能-扰动曲线下面积两个鲁棒性指标体系。Evaluation 3和Evaluation 4分别验证集成学习和对抗重训练带来的鲁棒性提升，所有主要结果均与baseline对比。
- 判定理由: 客观指标方面：核心结果指标为对抗鲁棒性度量（性能比率、性能-扰动曲线下面积），基于垃圾评论/垃圾邮件这一客观事实标签计算，不依赖主观评价，完全客观。唯一核心目标：研究问题、设计目标、评价和贡献均围绕提升对抗鲁棒性这一客观指标展开，理论仅用于指导设计，无并列核心目标，属于exclusive_objective_improvement。Benchmark方面：摘要明确说明在垃圾评论检测和垃圾邮件检测两个任务上与benchmark methods比较，实验部分系统性对比多个baseline模型，benchmark结果直接支撑ARText的鲁棒性提升主张，满足显式benchmark表述、评价语境、支撑

## [27] 2022 | Information Systems Research | Developing a Composite Measure to Represent Information Flows in Networks: Evidence from a Stock Market
- 数据集: Sina Finance coattention data | CSMAR (China Stock Market & Accounting Research) | CNRDS / eastmoney.com forum data
- 核心指标: 预测误差 (RMSE/MAE/MAPE); 投资组合超额收益 (Alpha)
- Benchmark评价: 在2017年holdout样本上，用Fama-MacBeth、SVR、MLP、决策树、随机森林、GBDT等方法，将EAC模型与不含EAC的基准模型及degree、closeness、betweenness、PageRank等替代指标逐一对比，报告RMSE/MAE/MAPE并采用bootstrap置信区间验证差异显著性。
- 判定理由: 本文以提升股票异常收益预测精度为唯一核心目标，核心指标（RMSE/MAE/MAPE、Alpha）均为客观可审计金融结果，不涉及主观构念。全文在评价语境中明确使用'benchmark'一词，系统比较了EAC与无EAC基准模型及多种替代网络指标，并以显式参照点证明提升。所有核心评价数据来自Sina Finance公开网站、CSMAR和CNRDS等公开/订阅可获取的数据源，且主要结果表均基于这些公开数据。因此三个模块全部通过，strict_include=true。

## [28] 2022 | Decision Support Systems | Fraudulent review detection model focusing on emotional expressions and explicit aspects: investigating the potential of feature engineering
- 数据集: Yelp.com review dataset (collected by Rayana and Akoglu [51]) | Yelp Open Dataset [57] | Amazon review dataset [12,23] | UCI Machine Learning Repository datasets
- 核心指标: 精确率 (Precision); 召回率 (Recall); F1分数; AUC (Area Under the ROC Curve)
- Benchmark评价: 在主Yelp数据集上开发并评估检测模型，然后在亚马逊、Yelp Open和UCI数据集上验证M-SMOTE算法与特征工程的效果。所有基准数据集上的结果均与baseline（无预处理/不平衡数据）、SMOTE以及先前研究方法进行比较。
- 判定理由: 本文核心目标是提升欺诈性评论检测的客观性能指标（精确率、召回率、F1、AUC），这些指标基于欺诈/非欺诈的事实标签，完全客观。研究问题、假设、实验设计和贡献声明均围绕该目标展开，无其他并列核心目标。全文存在明确的benchmark表述：摘要明确使用'benchmarking datasets'，实验部分在Yelp、Amazon、UCI等公开基准数据集上进行了系统评价，并与多种baseline和先前研究进行了比较。这些基准评价是支撑其核心性能提升主张的关键证据。评价核心主张所用的主要数据（Yelp、Amazon、UCI）均为公开可获取的数据集，独立研究者可查证和获取。因此三个模块全部通过。

## [29] 2022 | Information Systems Research | Modifying Transactional Databases to Hide Sensitive Association Rules
- 数据集: retail | bms-pos | synthetic data sets 10m, 50m, 100m (generated with IBM's synthetic data generator)
- 核心指标: 修改后数据库的准确性（未被修改事务的比例）; 被清洗的事务数（Number of transactions sanitized）; 求解时间（Solution time in seconds）; 产生虚假规则的数量和丢失规则的数量
- Benchmark评价: 在五个数据集（retail、bms-pos、10m、50m、100m）上，将所提出的最优线性化方法与三种文献基准算法进行比较，报告各方法可解出的问题数量、求解时间以及清洗的事务数，证明所提方法在可扩展性和解质量上有显著优势。
- 判定理由: 文章以最大化清洗后数据库的准确性等客观指标为唯一核心目标和贡献，全文无主观构念作为成功标准；在实验部分明确使用三个文献基准算法进行对比，benchmark评价支持核心提升主张且有明确比较对象；评价所用数据包括公开可下载的retail、bms-pos数据集和由公开IBM生成器可复现的合成数据集，公开数据支撑主要结果表。因此三个模块全部通过，strict_include为true。

## [30] 2023 | Decision Support Systems | A deep learning approach for detecting fake reviewers: Exploiting reviewing behavior and textual information
- 数据集: YelpZIP | YelpNYC
- 核心指标: Accuracy (准确率); Precision (精确率); Recall (召回率); F1-score; AUC (Area Under the Curve)
- Benchmark评价: 在YelpZIP和YelpNYC两个真实数据集上，通过两个实验（仅行为特征、全特征）将所提行为敏感特征提取器和完整框架与多个基准方法比较，报告Accuracy、Precision、Recall、F1、AUC，并做了配对t检验；结果表显示所提模型显著优于各基准。
- 判定理由: 客观指标：本文以fake reviewer检测的Accuracy、Precision、Recall、F1、AUC为唯一核心结果指标，标签为Yelp平台判定的伪评论者事实标签，不涉及主观构念。唯一核心目标：研究问题、实验设计和贡献声明均围绕提升检测性能，除客观指标提升外没有并列的核心目标。Benchmark：作者在摘要和实验设计中明确以'benchmarks'指称并与多个基准方法比较，benchmark结果（Table 4/7）是核心证据，且比较有明确参照点。数据集：核心评价使用公开的YelpZIP和YelpNYC数据集，可公开获取，并支撑核心提升主张。因此三个模块全部通过，strict_inc

## [31] 2023 | Decision Support Systems | Assuring quality and waiting time in real-time spatial crowdsourcing
- 数据集: GAIA open dataset
- 核心指标: 平均等待时间; 平均信誉值
- Benchmark评价: 在GAIA开放数据集（成都2016年11月订单数据）上构建仿真任务分配场景，将TP-TASC与RB-TPSC基线对比，考察不同任务半径、任务有效期、工人有效期和工人平均信誉下的平均等待时间、平均信誉值、平均成本、分配率和平均行驶距离。
- 判定理由: 该文提出TP-TASC框架，核心目标是降低平均等待时间并提高结果质量（以平均工人信誉值衡量），两个指标均为可客观计算的数值，没有以用户满意度、专家评分等主观构念作为核心成功标准；实验在公开可获取的GAIA开放数据集上构建，并与明确的基线方法RB-TPSC比较，评价结果直接支撑核心提升主张；因此三个模块均通过。

## [32] 2023 | Information Systems Research | Augmenting Social Bot Detection with Crowd-Generated Labels
- 数据集: Reddit公开API数据（r/BotWatchman社区维护bot名单） | Cresci et al. (2017) Twitter social spambot data set（次要benchmark）
- 核心指标: 社交机器人检测性能（Precision、Recall、F1、AUC）
- Benchmark评价: 核心实验在Reddit自建数据上对比传统模型与增强模型（Table 6），并用受限特征集对模型进行benchmark消融（Table 7），证明加入言语行为特征带来性能提升；在公开Cresci数据集上与Garcia-Silva等的BERT基线进行直接benchmark，验证基础模型和两个额外可实现特征的表现可比较或略优。
- 判定理由: 客观指标：核心目标是提升社交机器人检测性能，目标标签是外部事实类别的bot标签，评价指标为Precision/Recall/F1/AUC，完全客观；言语行为等人工标注仅作为中间特征。唯一核心目标：全文围绕crowd reaction增强检测性能展开，speech act是机制而非并列核心贡献，不存在主观成功标准或理论/政策并列贡献。Benchmark：评价语境中存在明确的benchmark/benchmarking表述（受限特征集benchmark消融和Cresci/Garcia-Silva直接benchmark），有明确参照点，并用于支持核心性能提升主张。数据集：核心评价数据来自Reddit

## [33] 2023 | Information Systems Research | Diversity Preference-Aware Link Recommendation for Online Social Networks
- 数据集: Google+ dataset (Gong et al., 2012)
- 核心指标: 多样性偏好匹配得分（DPMS）; Precision（精确率）; Recall（召回率）; F1 score
- Benchmark评价: 在公开的Google+数据集上，将DPA-LR与MMR、MSD、DPP、DiRec四种代表性多样化方法以及GCN-LR、GraphSage-LR、GAT-LR三种state-of-the-art链接推荐方法进行系统比较；主要结果表（表5、表6、表7、表9）显示DPA-LR在DPMS、Precision、Recall、F1上全面优于所有对照方法，且统计显著性p<0.001。
- 判定理由: 该文的全部核心成功指标均为客观可审计结果：DPMS由用户档案分布确定性计算，Precision/Recall/F1基于真实链接形成事实；没有任何主观量表、专家评分或基于人类语义判断的结果，也没有理论机制或组织变革等并列核心目标。文章在实证评价部分明确使用benchmarking表述，将所提方法与MMR、MSD、DPP、DiRec等多样化方法及GCN-LR、GraphSage-LR、GAT-LR等SOTA链接推荐方法在多张主要结果表上进行系统比较，证明DPMS和准确率的显著提升，并报告p<0.001。支撑核心提升主张的主要结果表全部基于公开可下载的Google+数据集，论文给出了明确数据来源和下

## [34] 2023 | Information Systems Research | Estimating Life Cycle Sales of Technology Products with Frequent Repeat Purchases: A Fractional Calculus-Based Approach
- 数据集: Notebook computer annual sales 2005-2014 | PC total global annual sales 2006-2015 (Statista) | DVD player sales in Australia 2003-2011 (Screen Australia) | iPad sales quarterly 2010-2017 (Apple quarterly summaries) | Samsung tablet sales 2012-2019 (Ejectejecteject/Statista) | US DVD player adoption and sales 1997-2018 (Consumer Technology Association, Digital Entertainment Group, Statista)
- 核心指标: 销售拟合优度与预测准确度; 采用趋势恢复准确度
- Benchmark评价: 在五个销售数据集（Notebook、PC、DVD Australia、iPad、Samsung tablet）上比较GDMR与两个基准模型的全数据拟合（R²/MAPE）和1/2年预测MAPE；在美国DVD播放器数据上比较拟合和8年预测MAPE；此外还与ARIMA、LSTM、KNN、Random Forest等通用预测模型比较。结果显示GDMR通常更优或大部分指标更优。
- 判定理由: 文章核心是提出并验证GDMR模型，目标为提升生命周期销售预测的客观准确度（R²/MAPE/SSE等），无主观量表或人类语义评价作为核心结果。全文在评价部分明确使用“Benchmark Repeat Purchase Models”，并与多个基准模型比较，支撑核心提升主张。评价所用数据均为可识别的公开来源（Statista、Screen Australia、Apple财报等），核心结果表基于这些数据。虽然结论中提及fractional integral解释的方法学/理论贡献，但该解释不是独立评价目标，未与预测提升并列为核心目标。因此，三个模块均通过，strict_include=true。

## [35] 2023 | MIS Quarterly | Exploiting Expert Knowledge for Assigning Firms to Industries: A Novel Deep Learning Method
- 数据集: Compustat Company Header History (COMPHIST) via WRDS | Stage One 10-X Parse data (Loughran-McDonald)
- 核心指标: 分类准确率（Accuracy）; 宏平均F1（Macro-F1）; 误分类成本（Misclassification Cost）
- Benchmark评价: 在NAICS和GICS两个公开行业分类任务上，用2012-2015年数据训练、2016年新企业分类测试，对DeepIA与SVM-IA、MLP-IA、ULMFiT-IA、HC-IA、LE-IA等基线/现有方法进行系统比较；主要结果报告准确率和宏F1，并给出DeepIA相对最优基线的提升百分比及显著性检验。
- 判定理由: 客观指标方面，核心成功指标是行业分类准确率、宏F1和误分类成本，均由既定行业标签和公开财务/税务数据客观计算，不涉及人类感知或语义评价；唯一核心目标是提升行业分类性能，方法创新是手段而非并列核心贡献。Benchmark方面，作者在实验部分明确使用“benchmark”一词，将DeepIA与SVM-IA、MLP-IA、ULMFiT-IA、HC-IA、LE-IA等基线/现有方法进行系统比较，并报告相对提升百分比的显著性检验，构成核心证据。数据集方面，核心评价基于公开可获取的Compustat/COMPHIST（WRDS订阅）和Loughran-McDonald 10-X Parse数据，数据集可识

## [36] 2023 | MIS Quarterly | Extracting Actionable Insights from Text Data: A Stable Topic Model Approach
- 数据集: Amazon Product Review dataset (Ni et al., 2019) | Yelp Restaurant Review dataset | StackExchange Q&A dataset | Company Description dataset (Qader et al., 2018)
- 核心指标: 模型稳定性指标（S_doc_prob、S_doc_label、S_topic_prob、S_topic_topwords）; 模型质量指标（Perplexity、C_v、C_uci）; 下游计量经济分析的一致性（系数方向、p值、相关性）
- Benchmark评价: 在 Amazon、Yelp、StackExchange、Company Description 四个数据集上，将 Stable LDA 与标准 LDA、Doc LDA、Ensemble LDA、Granulated LDA 等稳定性缓解方法进行系统比较，主要结果见表4（稳定性）和表5（模型质量）；附录F还比较了 MRF-LDA 和 CRFTM。结果显示 Stable LDA 在稳定性上显著提升，且不降低模型质量。
- 判定理由: 客观指标方面，核心成功指标均为可重复计算的统计量（稳定性、perplexity、coherence、回归系数一致性），不依赖人类主观评价；唯一核心目标是提出 Stable LDA 以提升主题模型稳定性，全文贡献均围绕该目标的评价与验证。Benchmark 方面，作者明确使用 benchmark 一词并在系统化比较中评估 Stable LDA 与 LDA、Doc LDA、Ensemble LDA、Granulated LDA 等方法，结果直接支撑核心稳定性提升主张且存在多个显式比较对象。数据集方面，Amazon、Yelp、StackExchange、Company Description 四个数

## [37] 2023 | Information Systems Research | Pricing in Nonconvex Markets: How to Price Electricity in the Presence of Demand Response
- 数据集: IEEE RTS-96 (IEEE Reliability Test System) | Garcia-Bertrand et al. (2006) case study bid/offer curves | Zoltowska (2016) bid data
- 核心指标: make-whole payments（总补偿额及占总成本比例）; 市场电价（均值、标准差）; 维持稳定所需的罚金（penalties）; 计算时间
- Benchmark评价: 在IEEE RTS-96这一标准benchmark系统上，对PBE-A/PE-A与IP pricing、ELMP、AIC pricing在价格无弹性、价格敏感、可平移负荷等场景下进行比较；结果表13-16报告价格均值/标准差、MWP、罚金和计算时间。核心改进主张（PE-A大幅降低make-whole payments）正是由该benchmark评价支撑。
- 判定理由: 客观指标方面：核心成功指标为make-whole payments、市场价格、罚金和计算时间，均为确定性可审计的货币/技术数值，不依赖主观评判；提升目标为最小化或消除make-whole payments。唯一核心目标方面：研究问题、设计目标和贡献声明围绕定价规则PE-A/PBE-A对客观指标的改进展开，理论不可能性证明是设计动机而非并列核心目标。Benchmark方面：全文在第6节明确将IEEE RTS-96称为广泛使用的benchmark数据集，并在评价语境中作为核心实验场地；与IP、ELMP、AIC等明确参照点比较，结果直接支撑核心改进主张。数据集方面：IEEE RTS-96是公开标准测

## [38] 2023 | MIS Quarterly | Unlocking the Power of Voice for Financial Risk Prediction: A Theory-Driven Deep Learning Design Approach
- 数据集: Seeking Alpha（财报电话会议文本记录） | EarningsCast（对应音频录音） | Compustat（财务基本面数据） | CRSP（股票价格数据）
- 核心指标: 金融风险预测的均方误差（MSE）与样本外决定系数（R²_oos）; 期权交易策略收益
- Benchmark评价: DeepVoice在所有预测视界（3/5/10/30/60天）与市场基准模型（Sridharan 2015的基本面加历史风险堆叠模型）比较，R²_oos分别达到7.31%、8.34%、4.28%、2.26%、7.45%，且均显著。此外，表5和表6中还将DeepVoice与Concat-SVR、Concat-GradientBoosting、One-stage LSTM、Contextual LSTM、DeepVoice-attention以及Emotion模型等基准比较，DeepVoice均表现最佳。
- 判定理由: 客观指标：核心目标是金融风险（波动率）的预测准确性，完全由股票市场价格数据计算，无主观语义判断；唯一核心目标是提升样本外预测性能，方法论贡献和设计原则均围绕此目标，不存在并列核心目标。Benchmark：全文在评价语境中明确使用benchmark model和market benchmark概念，并系统地将DeepVoice与多个基准模型比较，结果作为核心证据；有明确参照点。数据：核心评价数据来源于公开网站（Seeking Alpha、EarningsCast）和公开商业数据库（Compustat、CRSP），独立研究者可凭论文信息获取；公开数据支撑核心提升主张。三个模块全部通过，因此stri

## [39] 2023 | Information Systems Research | sDTM: A Supervised Bayesian Deep Topic Model for Text Analytics
- 数据集: Yelp.com consumer reviews | Stack Exchange online knowledge community
- 核心指标: 模型拟合度（perplexity）; 预测性能（AUROC / accuracy）; 回归系数方向与显著性
- Benchmark评价: 在Yelp和Stack Exchange两个数据集上进行系统化基准比较：模型拟合部分报告不同K值下的测试集perplexity，与LDA、sLDA、MedLDA、BP-sLDA、sNNTM、NTM等比较；预测部分报告AUROC/accuracy，并额外与RNN attention、Bi-LSTM、DistilBERT、BERT等深度模型比较。结果显示sDTM在多数设置下显著优于baseline或与SOTA可比。
- 判定理由: 客观指标检查：核心指标为测试集perplexity、预测AUROC/accuracy、基于真实投票数的回归系数，均完全客观可测量，且是唯一核心目标。benchmark检查：文中在摘要、第5.1节、第7.1节明确使用benchmark/benchmarking表述，并给出LDA、sLDA、NTM、BERT等明确比较基线，评价位于实验语境且直接支撑核心提升主张；属于benchmark_comparison_central。数据集检查：核心评价基于Yelp.com和Stack Exchange两个公开平台数据，可通过公开网页/API/数据转储获取，且为主要结果表的依据。三项全部通过，因此strict

## [40] 2024 | Decision Support Systems | A hybrid decision support system for adaptive trading strategies: Combining a rule-based expert system with a deep reinforcement learning strategy
- 数据集: S&P 500 index daily data (Yahoo Finance) | NYSE Composite (Yahoo Finance) | DAX Performance Index (Yahoo Finance) | CAC40 (Yahoo Finance) | Hang Seng Index (Yahoo Finance) | KOSPI Composite Index (Yahoo Finance)
- 核心指标: 累计收益率（%AR）; 夏普比率（Sharpe Ratio）; 最大回撤（MDD）; 年化/日均收益与标准差; 交易信号数量
- Benchmark评价: 在 S&P 500 的测试期及市场崩溃/上涨/下跌子时期，将所提 RB+RL+C1+C2 模型与 B&H、RB、RL、消融变体以及 TI+SVM、TI+RF、TI+LSTM、TI+XGBoost+CNN+LSTM 等既有混合模型比较，报告 %AR 和夏普比率；并在六只指数基金上做扩展比较。
- 判定理由: 核心成功指标全部为客观回测财务指标（累计收益、夏普比率、最大回撤、标准差、信号数），且提升该指标是唯一核心目标与贡献；全文在方法/实验部分明确以 benchmarks 指称比较模型并进行了系统性对比，结果支持核心提升主张；评价所用数据来自 Yahoo Finance 公开可获取的指数日线数据，占核心结果表依据。三个模块均通过。

## [41] 2024 | Decision Support Systems | A novel federated learning approach with knowledge transfer for credit scoring
- 数据集: Loan Data | HMEQ | Taiwan | Give Me Some Credit (GMSC) | Home Credit (HC)
- 核心指标: Accuracy; Recall; F1-score; KS
- Benchmark评价: 在五个信用数据集上，将 FedKT 与 FedAvg、FedProx、FedCodl 三个基准联邦学习方法（以及非联邦 LR、RF、XGBoost）在 IID 和 Non-IID 两种数据划分下比较 Accuracy、Recall、F1-score、KS，给出表3-6、Fig.3-5以及Friedman检验。这些比较结果用于支撑 FedKT 性能提升的核心主张。
- 判定理由: 客观指标：核心指标为 Accuracy、Recall、F1-score、KS，基于违约/非违约这一事实标签计算，完全客观，不涉及主观评价。唯一核心目标：研究问题、方法设计和贡献声明均围绕提升信用评分模型性能，无主观量表或并列核心目标。Benchmark：全文在引言和实验部分明确使用 'benchmark' 一词，5.2节将 FedAvg、FedProx、FedCodl 称为 benchmark federated methods，并与 FedKT 在全表和Friedman检验中比较，具有明确参照点，benchmark 结果直接支撑核心提升主张。数据集：核心评价使用了五个信用数据集，其中 Tai

## [42] 2024 | MIS Quarterly | Automated Analysis of Changes in Privacy Policies: a Structured Self-Attentive Sentence Embedding Approach
- 数据集: OPP-115
- 核心指标: Micro-averaged F1-score; Micro-averaged precision, recall, hamming loss
- Benchmark评价: 在OPP-115上，SAAS与5种传统ML模型、10种DL/attention模型、3种消融变体和自动分割方法进行4组benchmark比较；主要结果是SAAS在micro-averaged F1等指标上以统计显著优势胜过所有基准模型并用于支撑核心性能提升主张。
- 判定理由: 本文核心是构建并评价SAAS自动标注方法，在公开的OPP-115数据集上与多个ML/DL基准模型进行benchmark实验，以F1等客观指标证明提升；无主观满意度等成功指标，设计原则与案例研究为衍生贡献，不影响唯一核心目标；明确的benchmark表述位于方法/实验部分且使用显式比较对象；OPP-115为公开可获取数据集并构成核心评价基础。

## [43] 2024 | MIS Quarterly | Creating Proactive Cyber Threat Intelligence with Hacker Exploit Labels: A Deep Transfer Learning Approach
- 数据集: 0day.today | Seebug | ExploitDB | PacketStorm | Metasploit | Vulnerlab | Zeroscience | 0x00sec | Altenens | AntiChat | AntiOnline | Cipher | Go4expert | PersianTools | WWHClub | WildersSecurity
- 核心指标: Accuracy（准确率）; Precision（精确率）; Recall（召回率）; F1-score（F1值）
- Benchmark评价: 在自建的源域（exploit DNM和公共exploit库）与目标域（黑客论坛ground-truth）数据集上，以经典机器学习（naive Bayes、logistic regression、decision tree、SVM、XGBoost、LightGBM）、深度学习（RNN、GRU、LSTM、BiLSTM、BiLSTM+self-attention）、其他迁移学习（adaptive SVM、hard/soft MTL、adversarial、BERT）以及层选择消融为基准，报告accuracy、precision、recall、F1-score。DTL-EL在源域F1=90.91%，目标域F1=70.34%，显著高于各基准。
- 判定理由: 客观指标为exploit攻击类型分类的accuracy、precision、recall和F1-score，属于可外部核验的事实标签预测性能；核心目标唯一为提升该分类性能。全文在实验部分明确使用benchmark experiments/benchmark methods，并与多组baseline、SOTA和消融模型比较，benchmark结果直接支撑核心提升主张。核心评价数据来自公开命名的黑客论坛、exploit DNM和公共exploit库，来源公开可查且可通过公开网站获取。三个模块均通过，strict_include=true。

## [44] 2024 | Information Systems Research | Proactive Resource Request for Disaster Response: A Deep Learning-Based Optimization Model
- 数据集: 2021 Henan floods Weibo posts dataset (GitHub: GiveHenanAHand/henan-rescue-viz-website)
- 核心指标: 平均单位需求剥夺成本; 平均单位需求时间延迟
- Benchmark评价: 在真实Weibo洪水数据和模拟数据上，将提出的CNM-PRR与ReR、logNormMix-PRR、A-NDTT-PRR、AttnMC-PRR、CTDRP-PRR、LR-NV、DL-NV、logNormMix-IFCFS等8种方法比较，报告平均单位需求剥夺成本、平均时间延迟、未来需求满足百分比及多目标场景下的fill rate和公平性指标。
- 判定理由: 文章以最小化灾害响应中需求延迟剥夺成本为核心目标，所有核心成功指标均为客观可计算成本/时间/百分比，无主观构念；全文明确使用“benchmark/benchmarked”表述并在评价章节与多个基线方法比较，benchmark结果直接支撑核心提升主张；核心评价基于公开GitHub发布的2021河南洪水微博需求数据集，数据集可公开获取并作为主要结果表依据。因此三项模块全部通过，strict_include为true。

## [45] 2025 | MIS Quarterly | Different but the Same? An Event-Driven Approach to Determine Probabilities of Data Duplication
- 数据集: CENSUS | BABY | BIKES | BOOKS | COSMETICS
- 核心指标: F1-measure（重复检测分类性能）; ROC AUC（区分度）; 可靠性得分/校准曲线
- Benchmark评价: 在公开标准数据集 CENSUS、BABY、BIKES、BOOKS、COSMETICS 以及私有 INSUR1/INSUR2 上评价本文方法（Partitioning、KDE、KDE+附加数据、KDE+语言模型），以 F1-measure 为主，与 Febrl、RLTK、AWS AutoGluon、Microsoft AutoML、商业工具等方法比较；另用 INSUR1 上训练的模型迁移到 INSUR2/CENSUS 并与文献结果比较。
- 判定理由: 客观指标模块通过：核心成功指标为重复检测的 F1、AUC、可靠性，均基于可审计的重复/非重复事实标签，无主观构念作为成功标准。唯一核心目标是通过事件驱动概率模型提升客观检测性能；理论定义和适用性检查是辅助。Benchmark 模块通过：在公开标准数据集 CENSUS、BABY、BIKES、BOOKS、COSMETICS 上进行系统评价，并与多个 baseline/SOTA 比较，结果表支撑核心提升主张。数据集模块通过：公开数据可识别、可获取，且是主要结果表的核心组成部分；私有保险数据不否定公开数据对核心主张的支撑。

## [46] 2025 | Journal of the Association for Information Systems | GASP: A Graph Augmentation-Based Approach for Sign Prediction of Ties in Social Networks
- 数据集: Epinions | Wikipedia Requests for Adminship (RfA) | Slashdot Zoo | Yeast Genetic Interaction Network (GIN)
- 核心指标: 符号预测准确率（Accuracy）; 优化精度（Optimized Precision）; 宏F1（Macro F1）; 特异性与负预测值的几何均值（GM(S,N)）
- Benchmark评价: 在Epinions、Wikipedia RfA、Slashdot Zoo、Yeast GIN四个公开基准网络上，按60%-80%已标记边比例随机划分，比较GASP与NPECF、SRWR、ASiNE、DDRE在平衡网络上的Accuracy和Optimized Precision、在非平衡网络上的Macro F1和GM(S,N)；结果显示GASP在绝大多数设置下优于全部对比方法。
- 判定理由: 客观指标模块：核心目标是预测网络边符号（正/负），所有主要成功指标（Accuracy、Optimized Precision、Macro F1、GM(S,N)）均基于事实标签与预测标签的混淆矩阵计算，不依赖人类语义或感受评价；全文没有将主观量表作为成功标准。唯一核心目标：研究问题、设计目标、评价结构和贡献声明均围绕提升符号预测性能展开，DSR表述和设计准则属于呈现与延伸讨论，未形成并列核心目标。Benchmark模块：第5.1节明确以benchmarking表述在Epinions、Wikipedia RfA、Slashdot Zoo、Yeast GIN四个公开基准网络上的评价，且第5.4、5.

## [47] 2025 | Information Systems Research | Gaining a Seat at the Table: Enhancing the Attractiveness of Online Lending for Institutional Investors
- 数据集: LendingClub Loan Data
- 核心指标: 内部收益率 (IRR); 投资回报率 (ROI); 公共市场等价 (PME); IRR相关性
- Benchmark评价: 在LendingClub数据上，将线性GCPP和非线性GCPP与等权重、风险过滤、线性回归、梯度提升回归、神经网络回归、均值方差等基准组合比较，报告IRR、ROI、效用等客观指标；另外，将GCPP组合与传统资产指数（S&P 500、债券指数、REIT指数）比较，使用PME和相关性评价吸引力。非线性GCPP组合在IRR、PME等指标上显著优于基准。
- 判定理由: 文章核心是提出GCPP框架以构建在线贷款投资组合，核心成功指标为IRR、ROI、PME等完全客观的财务绩效指标，没有任何主观评价或满意度构念。研究问题、设计目标、评价结构和贡献声明均围绕提升这些客观指标展开，不存在并列的其他核心目标（理论机制贡献本质由绩效提升支撑，不是独立目标）。全文存在明确的benchmark表述（如“comparing it against various benchmarks”），比较对象包括等权重、风险过滤、回归、均值方差等基准组合以及六大市场指数，benchmark评价直接支撑核心IRR提升主张，且有明确参照点。核心评价数据来自LendingClub公开数据集，公开

## [48] 2025 | Information Systems Research | Post-Earnings-Announcement Drift Prediction: Leveraging Postevent Investor Responses with Multitask Learning
- 数据集: S&P Capital IQ Transcript database | CRSP | Compustat | I/B/E/S | Thomson/Refinitiv | RavenPack
- 核心指标: 预测精度（EV，explained variance）; 经济显著性（alpha）
- Benchmark评价: 在Russell 3000及其子样本上，将提出的FinAux+GradPerp+MQT与SUE、OLS、PEAD.txt、bi-LSTM、Transformer等基准模型比较，报告EV（表7），显示所提模型取得9.06%的最高EV；同时通过消融分析（表8）和与其他自适应加权方法比较（表11）证明FinAux和GradPerp的贡献。
- 判定理由: 客观指标模块通过：核心成功指标为EV和alpha，均为客观市场可审计结果，且唯一核心目标是提升预测性能和经济收益，无主观构念并列。benchmark模块通过：全文在评价语境中明确使用benchmark一词，与多个基准模型比较，benchmark结果支撑核心提升主张，且有明确参照点。数据集模块通过：核心评价数据基于S&P Capital IQ、CRSP、Compustat、I/B/E/S、Thomson/Refinitiv、RavenPack等公开可获取的标准商业订阅数据库，核心结果表完全基于这些公开数据。因此 strict_include = true。

## [49] 2025 | MIS Quarterly | RADAR: A Framework for Developing Adversarially Robust Cyber Defense AI Agents with Deep Reinforcement Learning
- 数据集: VirusTotal malware corpus | Microsoft Windows clean installation benign executables
- 核心指标: 逃避率 (Evasion Rate, ER); 假阳性率 (False Positive Rate, FPR)
- Benchmark评价: 实验1在三个检测器（LGBM、MalConv、NonNeg）和六类恶意软件上，将r-VAC与多种基准攻击方法（Random actions、BFA、EvadeHC、Surrogate RNN、Policy Gradient、DDQN、Rainbow、MAB-malware、ACER、A3C、GAMMA）比较逃避率，r-VAC在Combined列取得最高ER（28.13%、22.99%、18.98%）；实验2比较RL-RO鲁棒化前后的逃避率，平均降低约84%（即鲁棒性提升约7倍）。
- 判定理由: 核心目标是提升恶意软件检测器在对抗攻击下的鲁棒性，核心指标为逃避率和假阳性率，均为基于恶意软件检测结果（恶意/良性事实标签）的客观指标，无主观构念或并列核心目标。全文明确使用'benchmark methods'、'benchmark experiments'等表述，在实验部分将r-VAC与多种SOTA基准方法比较，并以鲁棒化前后对比支撑核心提升主张。评价所用恶意样本来自公开可获取的VirusTotal平台（学术许可/API），良性样本来自Windows系统，公开可查可获取。三个模块均通过。

## [50] 2026 | MIS Quarterly | Shapley Value-Based Feature Attribution for Data Masking
- 数据集: Credit History (UCI Machine Learning Repository, Hofmann 1994) | MIS Faculty Salary Offers (AIS annual survey, Galletta 2004) | CRSP/Compustat Merged (CCM) database
- 核心指标: 披露风险降低百分比 (%Δr); 数据效用保持/损失百分比 (%Δu); 建模度量 (R²、AAD、RASD)
- Benchmark评价: 在三个真实数据集（Credit、Salary、Compustat）上，将所有组合（4种掩蔽方法 × 2种模型 × 3种度量）下所提方法（risk-only 与 weighted-cost）与两个基准方法进行系统比较，表格（Table 5a-c）报告了风险降低和效用损失百分比，显示所提方法在风险降低方面优于或持平于基准方法，同时效用损失较小或持平。
- 判定理由: 核心目标完全是提升客观的披露风险降低和数据效用保持指标，没有任何主观构念作为成功标准；全文在实验评价语境中明确使用 benchmark methods，并与两个显式基准比较；核心实验结果完全基于 UCI、MIS Salary Survey、CRSP/Compustat 等公开可获取数据集。因此三个模块全部通过，strict_include=true。

## [51] 2026 | Information Systems Research | Toward Sustainable Electricity Markets: Capacity-Based Pricing for Electric Vehicle Smart Charging
- 数据集: CBS (Centraal Bureau voor de Statistiek) Netherlands mobility data | EPEX European Power Exchange wholesale electricity prices
- 核心指标: RMSE（均方根误差）; 峰值负荷（Peak）; 峰均功率比（PAPR）; 收入偏差（Revenue deviation）
- Benchmark评价: 在模拟测试床中，将所提出的容量定价（AH/CH及其-Distrib变体）与三个基准比较。表格2/4/5报告RMSE、PAPR、峰值，显示CBP-CH实现最低RMSE（0.02/0.03/0.21）和接近1的PAPR，远优于基准。
- 判定理由: 文中核心目标为通过容量定价诱导期望充电负荷曲线，所有评估指标（RMSE、峰值、PAPR、收入偏差）均为可审计的客观指标，无主观构念，且客观指标提升是唯一核心贡献。实验部分明确使用'benchmark'一词描述对三个基准的系统化比较，比较结果直接支撑核心改进主张。用于校准模拟的核心数据为CBS公开数据和EPEX公开市场电价，均可通过公开渠道获取，且这些公开数据支撑了主要结果表。虽然PV数据来源未完全公开，但该场景未用于与基准比较的核心主张，且主要benchmark对比场景基于公开数据。因此满足三个模块。
