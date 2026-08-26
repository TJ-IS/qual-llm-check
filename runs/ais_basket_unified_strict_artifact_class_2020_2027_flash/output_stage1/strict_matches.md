# Unified strict matches

Completed: 2475 / 2475
Retained: 39

## A decision support system for home dialysis visit scheduling and nurse routing

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2019.113224
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "总行驶距离", "measurement_cn": "从HDSS生成和人工生成的护士路线中计算的总行驶公里数", "objectivity_reason_cn": "距离为物理可测量事实，独立于人类感知或语义判断，可直接从地图和路线数据计算"}, {"name_cn": "总行驶时间", "measurement_cn": "从HDSS生成和人工生成的护士路线中计算的总行驶分钟数", "objectivity_reason_cn": "时间为物理可测量事实，可从路线和地图数据确定"}, {"name_cn": "所需护士数", "measurement_cn": "满足每日访问需求所需的护士数量，由计划确定", "objectivity_reason_cn": "护士人数为可审计事实，直接由计划中的分配决定"}, {"name_cn": "成本节省", "measurement_cn": "基于减少的总行驶距离和每公里补偿率（CAD 0.45/km）估算的每周/每年费用节省", "objectivity_reason_cn": "成本为可计算经济事实，由距离和费率审计确定"}]
- Artifact: 家庭透析访问调度与护士路由决策支持系统（Home Dialysis Scheduler System, HDSS） — 作者设计并实现了完整的HDSS，包括基于MILP的优化模块、用户界面模块、地图模块（GraphHopper/OpenStreetMap）、可视化模块和报告生成模块；通过可配置权重支持多目标优化（距离、成本、护士数、工作量平衡）
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除TOH案例数据和专门创建的界面后，仍保留对家庭透析访问调度与护士路由DSS类别的设计知识：模块化系统架构、多目标MILP模型、用户中心界面设计、地图集成和参数化方式；这些是可复用于其他同类系统的设计机制
- Decision: 核心评价指标（总距离、总时间、所需护士数、成本节省）是完全客观可测量的，并且是研究的设计目标和贡献所在；作者实际设计、实现并运行了一个完整的家庭透析调度与护士路由DSS（HDSS），指标的改善归因于该系统；文章明确针对同类DSS类别提供可推广的设计知识，而非仅为单一案例或仅作为算法包装。
- Confidence: 0.95

## Automated dynamic approach for detecting ransomware using finite-state machine

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113400
- Metric/core status: objective_fixed_factual_labels / objective_improvement_primary
- Metrics: [{"name_cn": "检测准确率 (Accuracy)", "measurement_cn": "在1975个样本（475个勒索软件 + 1500个合法应用）上，以系统正确分类样本数除以总样本数，公式 ACC=(M_ll+M_rr)/(总样本数)，结果为99.54%", "objectivity_reason_cn": "勒索软件与合法软件是外部可核验的事实类别，分类结果由系统检测机制决定，不依赖人的感受、语义或价值判断。"}, {"name_cn": "真正例率/召回率 (TPR)", "measurement_cn": "正确检测出的勒索软件样本数除以全部勒索软件样本数，TPR=M_rr/(M_rr+M_rl)，结果为466/475=98.1%", "objectivity_reason_cn": "基于事实标签（勒索软件/合法软件）和系统日志中的行为事件计算，客观可审计。"}, {"name_cn": "假正例率 (FPR)", "measurement_cn": "合法应用被误判为勒索软件的比率，FPR=M_lr/(M_ll+M_lr)，结果为0%", "objectivity_reason_cn": "基于合法软件事实标签和系统检测结果，客观可计算。"}]
- Artifact: 勒索软件动态检测系统（基于行为监控和有限状态机决策的Windows安全防护系统） — 作者设计了完整检测系统：行为分析模块（用户文件监控、横向移动追踪、系统资源监控、持久化监控四个监听组件）和决策模块（FSM状态机、状态变更监听器），并通过文件系统监视、注册表监控、内核态编程和Minifilter驱动实现检测与阻断机制。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除具体数据集（WannaCry/Cerber等）和具体测试界面后，论文仍提供可复用于其他勒索软件检测系统的设计知识：监控文件、资源、持久化、横向移动的四类行为监听机制，以及将这些事件组合成FSM状态转换来判定攻击的决策机制。
- Decision: 客观指标：核心指标是勒索软件检测的准确性、TPR、FPR，基于勒索软件/合法软件事实标签和系统行为日志，不依赖人类语义或感受，且论文以提升检测准确率、减少误报为最终目标和核心贡献。真实软件制品：作者设计并实现了一个完整的勒索软件检测系统，包含四个行为监控组件和基于FSM的决策模块，实际在Windows环境中运行并评估；指标改善归因于监听机制和FSM状态转换机制而非仅算法。类级贡献：贡献指向一类可复用的勒索软件检测系统，FSM行为建模和四类监控机制可进入其他同类检测系统；反事实检验表明移除特定样本和界面后仍保留可复用的系统设计知识。因此三个模块均通过，strict_include为true。
- Confidence: 0.95

## Ingredients for successful badges: evidence from a field experiment in bike commuting

- Year/journal: 2020 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2020.1808539
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "每周骑行天数（RidingDays）", "measurement_cn": "通过RFID扫描技术自动记录每周骑自行车通勤的天数；在实验期间从程序数据库收集。", "objectivity_reason_cn": "骑行天数是关于实际骑行行为的外部可验证事实，由RFID读卡器自动记录，不依赖人的感知、语义判断或主观评价。"}]
- Artifact: 游戏化系统（特别是一个包含徽章功能的自行车通勤信息系统/门户电子通讯） — 在自行车通勤程序中设计了三种徽章设计组件：1）奖励：可选的Facebook分享链接；2）标志符：自我利益与亲环境图标和标题；3）完成逻辑：固定目标（每周3次）与相对目标（前25%）。重新设计每周电子通讯和Web仪表板来显示徽章结果、过去一周骑行天数和徽章说明，并根据条件操纵用户可见的徽章元素。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 如果移除大学自行车通勤案例、RFID数据集和具体界面，本文仍然留下了关于徽章设计应如何选择奖励（如是否提供社交分享）、标志符（如亲环境与自我利益框架）和完成逻辑（固定目标与相对目标）的可推广知识，可供其他游戏化信息系统的徽章设计使用。
- Decision: 客观指标方面，本文以每周骑行天数这一由RFID自动记录的外部客观行为为最终目标和核心贡献，不涉及任何主观量表或语义判断，且客观改进是核心设计目标。软件制品方面，作者实际设计并修改了游戏化徽章组件（奖励、标志符、完成逻辑），将其作为新闻通讯和Web仪表板中的功能集成到现有自行车通勤程序中，并进行了七周的运行实验，客观改进归因于这些徽章设计机制。类级贡献方面，文章明确提出对徽章设计的研究缺口，将徽章设计分解为可复用的设计维度，贡献目标指向徽章/游戏化系统这一软件制品类别，而非特定案例或算法；移除具体案例后留下的仍是对徽章设计原则的可推广知识。因此，三项条件全部满足。
- Confidence: 0.95

## Designing Conversational Dashboards for Effective Use in Crisis Response

- Year/journal: 2023 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00801
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "透明交互（Transparent Interaction）", "measurement_cn": "基于系统日志中用户实际导航步骤数与任务所需最短导航步骤数的比值，越接近1表示透明交互越高。", "objectivity_reason_cn": "透明交互通过固定的步骤计数规则计算，完全依赖系统日志，不涉及用户感知或语义评价；该构念的操作化是客观可审计的。"}, {"name_cn": "效率（Efficiency）", "measurement_cn": "用户正确完成信息查找任务所需的平均时间，由实验系统记录的时间戳计算。", "objectivity_reason_cn": "时间是物理可测量指标，不依赖人的感受或判断。"}, {"name_cn": "有效性（Effectiveness）", "measurement_cn": "用户正确完成的信息查找任务数量，任务答案由COVID-19数据事实确定，系统自动比对答案。", "objectivity_reason_cn": "正确性基于可核验的外部事实（病例数、日期、州名等），不涉及主观质量或价值判断。"}]
- Artifact: 危机响应对话式仪表板（Conversational Dashboard for Crisis Response） — 在传统仪表板上增加自然语言交互（语音和文字），包括自然语言理解（意图识别、实体抽取）、对话管理（状态追踪、反馈生成），并引入对话式入门引导用户学习交互；同时支持用户在自然语言与鼠标交互之间选择。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除COVID-19案例、数据集和专门界面后，仍保留关于如何设计危机响应对话式仪表板的可复用知识：自然语言交互机制、多模态交互选择原则、对话式入门流程以及系统架构蓝图；这些机制面向一类软件，而非一次性案例。
- Decision: 客观指标方面，透明交互基于导航步骤日志，效率和有效性基于时间和事实答案，全部为客观可审计指标，且这些指标是设计目标和核心贡献；软件制品方面，作者实现并运行了对话式危机响应仪表板，包括自然语言交互、交互管理和对话式入门组件，指标改善可归因于这些设计机制；类级贡献方面，作者明确提出了针对危机响应对话式仪表板这一软件类别的设计原则，并提供了可复用的系统架构，实例是类别的代表而非一次性解决方案。因此三个模块全部通过。
- Confidence: 0.94

## Unlocking the Power of Voice for Financial Risk Prediction: A Theory-Driven Deep Learning Design Approach

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/17062
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "金融风险预测误差（股票收益波动率的预测精度）", "measurement_cn": "以业绩电话会后第τ天起的股票日收益标准差作为真实波动率，使用MSE和样本外R²（out-of-sample R²）比较模型预测误差；另通过期权多空跨式策略收益率衡量经济效用。", "objectivity_reason_cn": "股票波动率由公开交易价格按固定数学公式计算，不依赖人的感受、语义理解或价值判断；期权策略收益也由市场价格和固定规则计算。"}, {"name_cn": "期权交易策略收益", "measurement_cn": "基于预测波动率变化排序，构建多空跨式期权组合，按期权报价和到期收益计算组合收益率。", "objectivity_reason_cn": "期权价格和到期收益可从市场数据外部核验，计算过程客观可复现。"}]
- Artifact: 基于多模态语音/文本的财务风险预测系统（financial risk prediction system） — DeepVoice系统包含数据采集爬虫、文本-音频对齐组件、Praat声学特征提取、GloVe文本表示、两阶段LSTM声/文特征变换与融合组件、元学习堆叠组件。作者实质设计并实现了这些组件，尤其是两阶段LSTM架构和四类基础声学线索（pitch, intensity, fluency, quality）作为系统输入设计。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除S&P 500、具体公司名、6,047个样本和专门的数据集界面后，论文仍保留了财务风险预测系统中声/文特征提取、两阶段LSTM声文融合、元学习堆叠、基础声学线索选择等可复用组件设计与设计原则；这些知识指向同一类可运行软件应如何设计，而非仅仅剩下一组算法方程、市场机制或领域方案。
- Decision: 本文以股票收益波动率这一完全客观、可审计的金融指标为核心预测目标，并以MSE、out-of-sample R²和期权交易收益作为核心成功指标，目标构念不依赖人的感受或语义判断。DeepVoice不是单纯算法研究：作者设计并实际运行了从数据采集、文本-音频对齐、声学特征提取、两阶段LSTM声文融合到元学习堆叠的完整系统组件，并通过与多种基线的对比和消融实验将预测改进归因于这些系统设计机制。作者采用设计科学框架提出meta-requirements、metadesigns并总结可泛化设计原则，将DeepVoice实例化为财务风险预测系统这一软件类别的实例，达到了类级软件制品贡献的要求。
- Confidence: 0.94

## Feedback at scale: designing for accurate and timely practical digital skills evaluation

- Year/journal: 2020 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2019.1701955
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "评分速度/反馈及时性", "measurement_cn": "自动评分引擎每个文件所需的评分秒数，对比人类评分者每个文件所需的分钟数；系统日志记录的实际处理时间", "objectivity_reason_cn": "是可直接测得的物理时间量，不依赖人的感受或语义判断"}, {"name_cn": "评分有效性和准确性", "measurement_cn": "以专家复核建立的ground truth为基础，统计评分引擎在Excel/Word任务级评价中的误报率和漏报率，并与人工评分者的错误数比较", "objectivity_reason_cn": "任务完成与否可通过文件内容（XML、公式、格式等）进行外部核验；ground truth针对的是具体操作的事实正确性，而非质量或偏好"}, {"name_cn": "评分可靠性", "measurement_cn": "同一任务在不同条件下的评分不一致次数，如第二次迭代中1300个Excel任务和550个Word任务中仅6处不一致", "objectivity_reason_cn": "不一致次数是从系统评价结果和人工复核结果中统计出的客观错误数"}, {"name_cn": "学习者行为参与度", "measurement_cn": "作业提交率（feedback percentage）、任务块完成率，通过系统提交记录和日志统计", "objectivity_reason_cn": "提交次数和完成率是可观察、可审计的行为结果，不是自我报告或主观体验"}]
- Artifact: 面向大规模学习者提供实践数字技能反馈的在线反馈/评价系统，包含学习者应用和自动评分引擎 — 
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除具体课程、Excel/Word案例和专门制作的界面后，论文仍保留关于“可扩展数字技能反馈系统”应如何设计的功能结构、反馈工作流、评分引擎与作业设计协同机制，以及可复用的设计原则和元需求
- Decision: 本文核心目标是设计和评价一种可规模化的实用数字技能反馈系统；核心指标包括评分速度、误报漏报率、评分一致性、学习者提交率，均为可直接观测的客观结果。作者实际实现并运行了学习者应用和自动评分引擎，并明确将元需求和设计原则推广到“绩效反馈系统”这一软件/社会技术制品类别，而非仅提出算法或特定课程的一次性方案。因此三个条件均满足。
- Confidence: 0.93

## A novel decision support system for optimizing aircraft maintenance check schedule and task allocation

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113545
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "未使用飞行小时/平均FH、平均FC", "measurement_cn": "由DSS生成的维修检查计划中，各A/C检检查间隔与使用参数之差计算得到", "objectivity_reason_cn": "基于飞机使用参数（FH/FC/DY）和检查计划，不依赖人的感知或语义判断"}, {"name_cn": "A检和C检总检查次数", "measurement_cn": "从优化后的维修检查计划中统计各类型letter check数量", "objectivity_reason_cn": "是可审计的排程事实，直接反映维护成本和飞机可用性"}, {"name_cn": "维护成本节约/收益（Gain/Saving/Cost）", "measurement_cn": "根据减少的A/C检次数、飞机可用天数、每天运营收益和单次检查成本估算", "objectivity_reason_cn": "基于航空公司提供的单位成本/收益参数和计划中的检查次数，属于可核验的经济性指标"}, {"name_cn": "规划耗时", "measurement_cn": "DSS生成2019-2021三年计划的时间，报告为约10分钟，整体规划约30分钟", "objectivity_reason_cn": "是系统运行时间这一客观技术指标"}]
- Artifact: 航空维修计划优化决策支持系统（Aircraft Maintenance Planning Optimization DSS），涵盖维修检查排程、任务分配和轮班计划三类功能的可运行软件系统 — 作者设计并实现了DSS的三层架构：数据库层（CSV/Excel输入输出）、模型层（AMPO-1动态规划维修检查排程、AMPO-2基于WFD的维修任务分配、AMPO-3轮班计划）、GUI层（可视化检查计划、KPI、任务、人工修改约束与重新优化）
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除合作航空公司名称、具体机队数据和为演示制作的界面后，仍剩下“如何设计一个集成维修检查排程、任务分配和轮班计划的决策支持系统”的知识，包括三层架构、AMPO-1/2/3的模型层组织方式、任务分配中时间片段（bin）的定义与选择机制、移位计划工作流，以及该系统可用于维护策略评估的能力；因此剩下的是可复用的DSS类级设计贡献，而非仅剩算法或模型。
- Decision: 该文以完全客观的运营和经济指标（未使用飞行小时、检查次数、成本节约、运行时间）为最终目标和核心贡献；作者设计并实际运行了一个可识别的软件制品类别——航空维修计划优化DSS，包含数据库、模型、GUI三层，并实例化了AMPO-1/2/3三个可运行的优化组件；论文的贡献明确指向该DSS类别的架构与集成设计，且明确说明框架可推广到其他维护计划场景。因此三个模块均通过，应纳入。
- Confidence: 0.92

## Assessing and Enhancing Adversarial Robustness of Predictive Analytics: An Empirically Tested Design Framework

- Year/journal: 2022 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2022.2063549
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "对抗鲁棒性：性能比（Accuracy/Precision/Recall/F1/ROC的鲁棒性比值）", "measurement_cn": "在非对抗测试集与混合对抗样本测试集上分别计算分类指标，取两者比值 R_metric(ε)；数据来源为垃圾评论和垃圾邮件数据集，通过DeepWordBug生成对抗样本。", "objectivity_reason_cn": "分类正确与否取决于基准数据集中的垃圾/非垃圾事实标签，性能比和性能-扰动曲线下面积由模型输出和固定标签计算得到，不依赖人的感受、语义偏好或质量评价。"}, {"name_cn": "对抗鲁棒性：性能-扰动曲线下面积（A/P AUC, P/P AUC, R/P AUC, F/P AUC, ROC/P AUC）", "measurement_cn": "在不同扰动范围（0到1.0词替换比例）下计算分类指标并绘制曲线，求曲线下面积；数据来源与上述相同。", "objectivity_reason_cn": "扰动范围按词替换比例客观量化，分类指标由模型预测与固定垃圾/非垃圾标签计算，均为可审计的客观值。"}]
- Artifact: 具备对抗鲁棒性的文本分类系统（如垃圾评论检测系统、垃圾邮件过滤系统、情感分析系统等预测分析应用中的文本分类系统） — ARText系统包含四类设计组件：对抗样本生成模块、两类新的鲁棒性度量（性能比与性能-扰动曲线下面积）、基于bagging的集成分类模块、迭代对抗重训练算法。作者设计并实现了这些组件，并将其作为系统功能运行。
- Class contribution: software_artifact_class / implicit_but_well_supported / core_research_contribution
- Counterfactual: 移除'芝加哥酒店垃圾评论'和'SpamAssassin垃圾邮件'这两个具体数据集以及针对这两个用例的实验界面后，剩下的贡献仍然是：对抗鲁棒性评估模型（性能比、性能-扰动曲线）和增强原则（集成学习、对抗重训练）如何设计并集成到预测分析/文本分类系统中。这些是可复用于同类软件制品（如垃圾评论检测系统、垃圾邮件过滤系统、情感分析系统）的组件设计知识，而非只剩算法、求解器或市场机制。
- Decision: 客观指标：核心成功指标为对抗鲁棒性（性能比、性能-扰动曲线下面积），基于固定垃圾/非垃圾标签和模型输出计算，不依赖主观语义评价；核心目标明确为提升该指标。真实软件制品：作者设计并实现了ARText系统，包含对抗样本生成、鲁棒性度量、集成学习和对抗重训练等组件，并在两个数据集上实际运行评价，指标改善归因于这些设计机制。类级贡献：文章目标不是解决单一案例，而是为预测分析应用（文本分类类）提供可复用的鲁棒性评估模型和增强设计原则，ARText是该类别的一个实例，删除具体案例和数据后仍保留可复用于同类系统的组件设计知识。
- Confidence: 0.92

## Enhancing User Privacy Through Ephemeral Sharing Design: Experimental Evidence from Online Dating

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2021.0379
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "附带照片的匹配请求数（NumPhoto）", "measurement_cn": "从平台交易数据库和事件日志统计用户实验期间发送的含照片匹配请求数量。", "objectivity_reason_cn": "该数值由系统日志直接记录，不依赖人的感受、语义评价或价值判断。"}, {"name_cn": "含人脸照片的匹配请求数（NumFace）", "measurement_cn": "使用百度AI人脸检测API对发送的照片进行人脸识别，并人工验证400张照片，准确率为98.75%。", "objectivity_reason_cn": "人脸是否出现是可由检测系统核验的事实标签，不依赖主观偏好或语义评价。"}, {"name_cn": "匹配成功数（NumMatch）", "measurement_cn": "接收方接受匹配请求的次数，来自平台交易数据库。", "objectivity_reason_cn": "接受或拒绝匹配是平台记录的可观察事实，属于外部可审计的交易结果。"}, {"name_cn": "接收方发来的消息数（SumMsgFromReceiver/取对数）", "measurement_cn": "用户作为发送方的新匹配中，接收方发来的消息总数，来自第三方云数据仓库。", "objectivity_reason_cn": "消息条数是系统日志中的可计数行为，不依赖人的主观感受或语义评价。"}]
- Artifact: 在线交友/匹配平台中的附照片匹配请求功能（短暂分享 vs 持久分享设计）。 — 
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 若移除Summer平台、具体数据集和专门制作的界面截图，论文仍留下关于“在线匹配/交友平台应在初始请求阶段如何设计短暂分享式照片功能”的可复用知识：核心机制是使共享内容短时可见且不可追踪，以降低隐私顾虑并改善可观察的披露、匹配和互动结果；剩下的不是单纯算法或市场机制。
- Decision: 文章的核心现场实验以完全客观的系统记录指标（照片数、含人脸照片数、匹配数、接收方消息数）作为主要成功标准，客观提升是最终设计目标和核心贡献；短暂分享功能作为在线匹配平台中的真实软件组件，由作者设计并通过生产系统随机现场实验实现和评估，客观效果可归因于该设计机制；论文贡献明确面向在线匹配/交友平台这一软件制品类别的可复用设计模式，而非一次性案例、算法包装或纯领域机制。因此三个模块全部通过，strict_include为true。
- Confidence: 0.92

## Fast Forecasting of Unstable Data Streams for On-Demand Service Platforms

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2023.0130
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "对称平均绝对百分比误差 (SMAPE)", "measurement_cn": "由平台实际订单量与模型预测值计算 100*|actual-forecast|/(|actual|+|forecast|) 并在所有地区和时段上平均；数据来自合作平台英国294个配送区域的小时级需求，属客观记录。", "objectivity_reason_cn": "预测误差基于可观测的实际需求和确定的计算公式，不涉及人类感受、语义或价值判断。"}, {"name_cn": "均方根误差 (RMSE)", "measurement_cn": "预测误差平方的平均再开方，同样基于实际需求与预测值。", "objectivity_reason_cn": "客观技术指标，完全由数据决定。"}, {"name_cn": "经济损失函数", "measurement_cn": "用 c1=1.14, c2=0.54 对高估/低估预测进行不对称货币化损失相加，转化为英镑金额。", "objectivity_reason_cn": "经济损失由平台给定的单位成本参数和实际需求/预测值计算，反映财务影响，不依赖主观评价。"}, {"name_cn": "计算时间/计算成本", "measurement_cn": "运行一次全地区每日预测更新所需的秒数，以及按云实例小时价格折算的美元成本。", "objectivity_reason_cn": "时间和成本均可审计、可客观测量。"}]
- Artifact: 按需服务平台的高频流式数据预测系统（forecast framework/system），可扩展至其他不稳定数据流预测场景。 — 设计并实现了三个核心机制：(1) 基于PELT的流式预测失效检测，监测预测损失序列中的突变；(2) 全样本与断点后样本的等权重预测组合机制；(3) 利用可再生OLS实现的高速流式参数更新，并支持领域知识约束或LASSO数据驱动选择。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除平台名称（Stuart）、特定数据集（英国配送和Citi Bike）以及专门设计的模型规格后，论文仍然提供了关于如何设计自动断点检测、动态调整预测权重和高效流式更新的一类预测系统的方法架构和可复用机制。
- Decision: 文章的核心贡献是开发并实现一个面向不稳定数据流的预测框架（FFUDS），其目标函数和评价均基于预测误差（SMAPE、RMSE、经济损失）和计算时间/成本等完全客观的指标；该框架包含了明确的软件制品机制（断点检测、预测组合、可再生估计），并通过两个实际应用完成了运行和验证；作者明确将其作为可推广于多类数据流预测系统的设计贡献，而非一次性算法包装。因此满足全部三个条件。
- Confidence: 0.92

## Interleaved Design for E-Learning: Theory, Design, and Empirical Findings

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2023/17206
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "后测成绩（Posttest score）", "measurement_cn": "实验结束后通过在线阅读理解测试得到的百分制得分；题目为教育部门规定的14个英语阅读主题对应的客观选择题，对错由固定答案判定。", "objectivity_reason_cn": "后测成绩是学习者答题正确性的直接观测结果，不依赖研究者、教师或学习者对质量、价值或意义的主观评价；评分规则固定且可复核。"}, {"name_cn": "会话准确率与主题掌握度", "measurement_cn": "系统根据学习者每次练习的答题正误计算会话准确率，并通过隐马尔可夫模型估计主题掌握状态。", "objectivity_reason_cn": "这些指标来自系统日志中的答题正误和基于固定概率模型的估计，属于可审计的行为事实，不涉及主观语义判断。"}]
- Artifact: 个性化/自适应电子学习系统（personalized e-learning system），具体包含弱主题检测、知识图谱和练习调度引擎。 — 设计了related-interleaving会话调度策略：使用隐马尔可夫模型动态检测学习者弱主题，使用专家规则与模糊关联规则构建并更新主题知识图谱，并设计调度引擎按弱主题和相关主题标准选择练习材料。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除当前学校、英语阅读数据集和专门练习界面后，论文仍留下关于电子学习系统应当如何设计会话结构的知识：如何根据主题相关性和学习者弱点动态选择同一会话中的练习主题，以降低认知负荷并提升学习绩效。该知识可迁移到其他电子学习平台。
- Decision: 该文以电子学习后测成绩等完全客观的学习绩效作为核心设计目标和贡献指标；作者设计并实际运行了一款个性化电子学习系统，其核心机制为相关交错（related-interleaving）调度，包含弱主题检测、知识图谱和调度引擎；贡献目标是可复用的电子学习会话设计/软件制品类别，而非仅算法、场景或一次性案例，因此三个模块均通过。
- Confidence: 0.92

## A new emergency decision support system: the automatic interpretation and contextualisation of events to model a crisis situation in real-time

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113260
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "事件解释、情境化和可视化的处理延迟", "measurement_cn": "在五个不同事件频率和规则规模场景下，分别测量解释规则、情境化规则和可视化更新的时间延迟，以秒计；例如解释规则在0.12–0.91秒内完成，情境化规则在1.83–2.25秒内完成，可视化在0.03–0.72秒内完成。", "objectivity_reason_cn": "处理时间是可直接观测、可计时复验的技术性能指标，不依赖人的感受、语义好坏或价值判断。"}, {"name_cn": "事件被正确解释和正确情境化的数量/状态", "measurement_cn": "基于预定义业务规则和危机情境模型，检查所有模拟事件是否被正确解释和情境化；论文报告所有事件均正确解释和正确情境化。", "objectivity_reason_cn": "正确性由确定性规则、阈值和模型匹配决定，而非由专家或用户作主观质量评价。"}, {"name_cn": "大数据4Vs管理能力（吞吐、速率、多样性、真实性）", "measurement_cn": "通过系统各组件的架构分析，说明消息代理、复杂事件处理引擎、元模型和通用态势图对数据/信息层面的容量、速率、多样性和真实性的控制效果。", "objectivity_reason_cn": "这是对系统可观测架构能力和事件处理性能的定性/定量评估，不依赖人对输出质量的主观评价。"}]
- Artifact: 紧急决策支持系统 / 危机管理信息系统（emergency decision support system） — 作者设计并实现了AIC信息系统，包括：扩展R-IOSUITE的危机情境元模型（新增数据源、关键基础设施、敏感建筑等概念）；开发Java复杂事件处理引擎，使用SIDDHI规则解释和情境化事件；实现从CEP规则查询Neo4J图数据库的定制函数；开发消息代理以管理事件订阅与转发；集成R-IOSEMIT事件模拟器、R-IOPLAY通用态势图、R-IODA模型器、R-IOWA/R-IOTA响应过程编排与监控组件。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除Middle Loire洪水案例、具体水位/流量/交通数据和专门制作的界面后，仍保留了面向紧急决策支持系统的可复用架构知识：CEP引擎与图数据库的联通机制、基于元模型的解释/情境化规则、事件订阅与消息代理机制，以及通用态势图的持续更新机制。这些不是纯算法或领域市场机制，而是某类可运行软件制品的设计方案。
- Decision: 客观指标方面：核心评价指标是事件解释、情境化和可视化的处理延迟，以及事件是否被确定性规则正确解释和情境化，均不依赖人的语义或偏好。核心目标方面：研究问题和贡献声明都指向构建能够实时采集、解释和情境化事件以更新通用态势图的决策支持系统，目标不是解释心理或组织理论，而是改善系统处理能力。软件制品方面：作者设计和实现了AIC信息系统，包括CEP引擎、消息代理、图数据库连通、可视化界面和事件模拟器，并在洪水案例上实际运行和测量。类级贡献方面：文章面向紧急决策支持系统这一软件类别，明确其架构可作为未来DSS研究的框架，可复用的机制（CEP规则查询情境模型、元模型支撑的解释/情境化规则、事件订阅与通用态势图更新）可迁移到其他复杂协作场景。因此三个模块均通过，strict_include为true。
- Confidence: 0.9

## Augmenting Social Bot Detection with Crowd-Generated Labels

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1136
- Metric/core status: objective_fixed_factual_labels / objective_improvement_primary
- Metrics: [{"name_cn": "社会机器人检测性能（macro-F1、AUC、precision、recall）", "measurement_cn": "在Reddit真实数据集上，将账号分类为机器人或非机器人；使用precision、recall、macro-F1、micro-F1和AUC评估，并与基线模型和消融模型对比。另通过time-to-detection模拟评估检测速度。", "objectivity_reason_cn": "目标是检测账号是否为社交机器人这一外部事实；ground truth基于众包报告但代表可核验的账号类别，不是人类感受或语义质量评价。指标数值可由分类结果和标签确定性地计算。"}]
- Artifact: 社交机器人检测系统（social bot detection system） — 设计并实现了一个计算检测流程：利用BERT对人群回复进行话题、情感和言语行为分类，将这些人群反应特征与传统的语义嵌入和时间相似性特征整合为特征矩阵，训练分类器判别账号是否为机器人；并通过言语行为对人群反应的可信度进行加权，形成增强的检测机制。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除Reddit案例和专门数据集后，仍保留关于如何设计社交机器人检测系统的可复用知识：通过人群反应生成特征、使用言语行为评估反应可信度、并将这些人类智能特征与传统检测特征整合。该贡献不是纯粹算法或域名机制，而是面向检测系统的组件设计。
- Decision: 客观指标方面，核心成功指标是机器人检测的precision、recall、F1、AUC等，针对可外部核验的bot/nonbot事实标签，且提升检测性能是研究问题和贡献的核心；真实软件制品方面，论文实现了可识别的社交机器人检测系统，具体设计了人群反应特征提取与言语行为加权机制，并在真实数据集上实际运行和评估，改进归因于该制品设计；类级贡献方面，作者明确将贡献指向可部署于多平台的社交机器人检测系统类别，机制可复用于其他平台和其他算法生成内容检测，反事实测试后仍保留类级软件设计知识。因此三个模块全部通过，strict_include为true。
- Confidence: 0.9

## Can Recommender Systems Reduce Healthcare Costs? The Role of Time Pressure and Cost Transparency in Prescription Choice

- Year/journal: 2020 / MIS Quarterly
- DOI: 10.25300/misq/2020/14435
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "处方调整（是否选择低成本的等效替代药物）", "measurement_cn": "在实验中记录参与者查看系统推荐和调整初始处方的点击行为，系统日志直接记录是否调整；药物成本由实验系统根据预先设定的成本和参与者初始选择动态赋值。", "objectivity_reason_cn": "处方选择和药物成本是外部可观察、可审计的事实，不依赖人的感受、偏好或语义评价。"}]
- Artifact: 临床处方成本敏感推荐系统（cost-aware healthcare recommender system） — 作者设计了两种成本框架（low-cost只显示低价替代方案，mixed-cost混合显示高/低价替代方案）、动态成本分配算法、基于药物类别的等效替代推荐列表，以及时间压力提示（系统队列通知、计时器、绩效竞争信息）。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除具体的患者案例、医生样本和实验数据集，论文仍保留了关于'临床成本敏感推荐系统应如何设计成本展示、处理时间压力、适应不同使用者'的可复用设计原则（如成本框架影响调整行为、时间压力对非医师影响更大、系统应提供等效疗效和可负担信息）。这些不是一次性算法、市场机制或领域政策，而是面向软件制品类别的设计知识。
- Decision: 文章以完全客观的处方成本降低为核心目标，通过作者设计并实际运行的成本敏感临床推荐系统原型，检验成本框架和时间压力对处方调整行为的影响，并明确提炼对该类软件系统设计的可复用启示。三个模块全部通过，因此strict_include为true。
- Confidence: 0.9

## Conversational Recommender Systems and natural language:

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113250
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "推荐准确率 Accuracy", "measurement_cn": "用户对系统推荐的项目做出接受或拒绝的行为选择，准确率=被接受项目数/推荐项目数", "objectivity_reason_cn": "基于用户在实际交互中的可观测选择，不依赖对质量或语义的评分"}, {"name_cn": "平均精度均值 MAP@5", "measurement_cn": "根据推荐列表中被用户接受项目的位置计算平均精度，再对所有推荐列表求均值", "objectivity_reason_cn": "由用户接受这一客观行为事件和推荐排序计算得到"}, {"name_cn": "提问数 Number of Questions", "measurement_cn": "统计对话中聊天机器人向用户提出的问题数量，包括消歧、确认和项目评价请求", "objectivity_reason_cn": "从系统日志直接计数，不涉及主观评价"}, {"name_cn": "每问耗时 Time Per Question 与交互总时间 Interaction Time", "measurement_cn": "根据消息时间戳计算用户回答问题所需时间和完成实验的总时间", "objectivity_reason_cn": "时间戳是可审计的系统日志事实"}, {"name_cn": "查询密度 Query Density", "measurement_cn": "按公式计算每条用户消息中引入的概念数量，基于对话内容计数", "objectivity_reason_cn": "由消息文本中可识别的实体/属性数量与消息数计算得到"}, {"name_cn": "命中率 HitRate@k", "measurement_cn": "在体外实验中，使用 synthetic 数据集的标准答案计算推荐列表前 k 项中的命中率，并报告相对上限的损失", "objectivity_reason_cn": "基于数据集中的固定事实标签和推荐排序计算"}]
- Artifact: 对话式推荐系统框架/聊天机器人（Conversational Recommender System framework） — 作者设计并实现了完整的 ConveRSE 架构，包括 Dialog Manager、Intent Recognizer、Sentiment Analyzer、Entity Recognizer、Recommendation Services；实现了三种交互模式（按钮、自然语言、混合），以及解释、critiquing、消歧和槽填充式对话机制。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 若移除电影、图书、音乐等具体领域实例和数据集，剩余的核心贡献仍然是 ConveRSE 中可复用的 CoRS 组件设计、交互机制、槽填充对话流程，以及关于自然语言和混合交互如何影响推荐准确率与交互成本的类级设计知识；不会退化为仅剩算法或领域方案。
- Decision: 该文以可观测的推荐准确率、命中率、交互时间、提问数等客观指标为核心评价结果，研究目标明确指向对话式推荐系统这一软件制品类别中的自然语言交互和组件设计。作者实际设计、实现并运行了ConveRSE框架及其多个领域实例，客观指标的改善被归因于交互模式与系统组件的设计机制。三类条件均满足。
- Confidence: 0.9

## Designing Attentive Information Dashboards

- Year/journal: 2022 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00732
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "注意力资源分配绩效（revisit阶段）", "measurement_cn": "基于眼动仪记录的各AOI注视时长和注视次数百分比，以16.67%为理论均分基准计算偏差；比较revisit阶段相对first visit阶段的分配变化", "objectivity_reason_cn": "数据来自眼动仪自动记录和确定性计数，不依赖人的体验、语义判断或主观评分"}, {"name_cn": "注意力转移率", "measurement_cn": "revisit阶段用户在六个AOI之间发生的眼动转移总数", "objectivity_reason_cn": "转移次数由眼动轨迹按固定AOI规则自动计算，属于系统日志类客观指标"}, {"name_cn": "注意力资源管理绩效", "measurement_cn": "任务结束时六个AOI注视时长和注视次数的标准差，SD越低表示分配越均匀", "objectivity_reason_cn": "SD由眼动计数和预设的六AOI分布计算，数值确定且可复核，不涉及主观评价"}]
- Artifact: attentive information dashboard / 注意力感知信息仪表盘，属于BI&A系统交互界面类软件制品 — 作者设计和实现了三个子系统：仪表盘子系统、实时眼动追踪子系统、注意力感知子系统；核心可复用机制包括基于眼动的注意力分配计算（DP1）和个体化视觉注意力反馈生成（DP2），并通过反馈生成器把用户在各AOI上的注视时长以时间格式展示给用户
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除当前销售dashboard案例、实验数据和专门制作的六图界面后，仍剩余可复用的类级设计知识：attentive information dashboard类软件应如何实时监测用户注意力、计算注意力分配并向用户提供个体化VAF的功能结构与设计原则；DP1和DP2可被同类仪表盘设计采用，而非仅用于当前案例。
- Decision: 客观指标方面，核心成功指标均为眼动仪自动记录的注视时长、注视次数、转移次数和标准差，属于完全客观且可复核的系统日志类指标，且没有将主观满意度或语义质量作为核心结果。核心目标方面，研究问题、设计原则和假设均指向通过软件设计提升用户的信息处理/注意力管理，客观指标改善是主要评价和贡献依据。软件制品方面，作者设计并实际运行了自研attentive dashboard实验软件，包含实时眼动追踪、注意力分析和个体化VAF反馈组件，指标改善可归因于该制品的反馈设计机制。类级贡献方面，作者明确贡献系统架构和设计原则，面向attentive information dashboards这一类软件制品，而非只解决单一案例、单一数据集或只提出算法；移除具体案例后仍保留可复用的仪表盘类软件设计知识。因此三个模块全部通过，strict_include为true。
- Confidence: 0.9

## Finding a Needle in the Haystack: 
Recommending Online Communities on Social Media Platforms Using Network and Design Science

- Year/journal: 2021 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00694
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "推荐精度 Precision@1/5/10", "measurement_cn": "模型推荐结果与用户实际订阅的Twitter列表比较，计算top-k推荐中正确订阅的比例", "objectivity_reason_cn": "是否订阅是平台用户真实行为记录，无需人类感受或语义评价"}, {"name_cn": "召回率 Recall@1/5/10", "measurement_cn": "模型推荐结果与实际订阅列表的重合比例，基于系统日志中的订阅行为", "objectivity_reason_cn": "基于可审计的订阅事实，不依赖主观判断"}, {"name_cn": "F-score、MRR、DCG、Overall accuracy", "measurement_cn": "由实际订阅/未订阅标签计算的标准检索与推荐指标", "objectivity_reason_cn": "结果标签为真实订阅行为，计算规则固定"}]
- Artifact: 社交媒体平台在线社区/列表订阅推荐系统（online community/list recommender system） — 作者设计了网络特征构建机制（structural hole assortativity、LCCR等）、一般社区特征（size/overlap）、用户-列表/列表-列表/用户-用户三类网络的构建方法，以及推荐评分模型和高效的网络指标计算算法。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除Twitter列表这一具体案例后，论文仍保留了推荐系统设计中可复用的三类网络建模方法、网络特征计算机制（如LCCR、assortativity）和一般社区特征，可用于其他社交平台的社区推荐器设计。
- Decision: 核心目标是设计社区订阅推荐系统并通过客观指标提升推荐质量：precision、recall、F-score、MRR、DCG均基于真实订阅行为标签，指标完全客观。软件制品是可识别的推荐系统类别；作者实际设计并运行了特征提取算法、网络构建以及推荐模型，而非仅提出算法。贡献声明和可复用性说明指向同类在线社区推荐系统的设计，而不是单一Twitter案例或单纯算法模型。
- Confidence: 0.9

## Smart Markets for Real-Time Allocation of Multiproduct Resources: The Case of Shared Electric Vehicles

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2022.0204
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "车队总毛利润", "measurement_cn": "基于Car2Go实际租赁交易推断的租金收入、上调和下调备用市场清算价格、模拟执行中的机会成本与罚金，按市场分别汇总为美元毛利润。", "objectivity_reason_cn": "利润由实际交易、市场价格和模拟执行规则确定，不依赖任何人感受或语义评价，可审计可复算。"}, {"name_cn": "车辆利用率", "measurement_cn": "计算每辆SEV在租赁市场与作为虚拟电厂参与电力市场的生产性使用时间占可运行时间的比例。", "objectivity_reason_cn": "利用率基于系统日志和已实现/承诺的分配状态，是客观的时间和容量事实。"}, {"name_cn": "分配决策准确性", "measurement_cn": "将FleetPower的承诺与完美预知条件下的最优决策进行混淆矩阵比较，报告VPP/租赁市场分配准确率和错分情况。", "objectivity_reason_cn": "对照基准是同一模拟环境下按事后客观收益计算的最优分类，不是人对质量的评价。"}]
- Artifact: 面向多产品资源实时分配的决策支持系统（DSS），具体为共享电动车车队的多市场资源分配DSS（FleetPower）。 — 作者设计了五阶段DSS：市场与运营数据收集（ML需求/价格/可用性预测）、按盈利排序的资源规划、向电力备用市场和租赁市场投标、资源再规划（违约罚金与替代车辆选择）、执行与核算。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除Car2Go、Stuttgart/Amsterdam/San Diego数据和专门界面后，剩余的贡献仍是‘如何设计一个实时多产品资源分配DSS以在多种异构智能市场间持续评估吸引力并投标’的可复用五阶段组件与机制；不是仅剩算法或市场机制。
- Decision: 文章以FleetPower这一DSS为核心贡献，设计、实现并在真实数据参数化的模拟中运行；核心评价指标为利润、利用率、预测/分配准确性，均属完全客观可测结果；研究目标和贡献声明明确指向提升这些客观指标；FleetPower被呈现为可推广到共享电动车、共享出租车、零工经济、热电联产等多产品实时分配DSS类别的五阶段蓝图，移除具体城市与数据后仍保留可复用的DSS组件设计知识，因此三类资格均通过。
- Confidence: 0.9

## Timely, Granular, and Actionable: Designing a Social Listening Platform for Public Health 3.0

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2023/17381
- Metric/core status: objective_fixed_factual_labels / objective_improvement_primary
- Metrics: [{"name_cn": "相关内容收集的精度/召回率/F1", "measurement_cn": "在3700万URL测试床上，用专家标注的黄金标准分类器判定每个URL是否与PMDS或阿片类药物任务相关，统计HealthSense和基准方法在5M/10M收集量下的precision、recall、F-measure及AUC。", "objectivity_reason_cn": "相关性标签由两位领域专家按本体和情感标注指南手工标注，但评价目标是系统能否按既定任务定义收集相关页面；标签对应外部事实（页面是否涉及特定药物/阿片类药物及其情感倾向），标注协议有明确规则，且最终指标是可计算的检索性能。敏感性在于情感标注有一定语义判断，但该判断是用于构建任务相关的二元事实标签，而非评价系统输出的质量、价值或偏好。"}, {"name_cn": "事件检测的召回率/信号精度（disproportionality analysis）", "measurement_cn": "使用报告比值比（ROR）对HealthSense、GBS、BFS收集的5M PMDS数据做药物-反应共现统计，阳性信号对照PharmCo五位专家确认的21个真实阳性病例计算case recall和signal precision。", "objectivity_reason_cn": "事件是否为真实不良药物反应的判断由领域专家基于外部证据作出，但统计信号计算本身基于文本共现的可审计事实；主要对比的是不同数据收集方法对下游可审计事件检测的影响。"}, {"name_cn": "用户实验中的真阳性和假阳性识别精度/召回率", "measurement_cn": "77名PharmCo安全团队成员使用相同Tableau仪表盘，分别基于HealthSense、GBS、BFS收集的数据在3小时内判断20个病例为真阳性或假阳性，由五位专家核查证据后计算precision、recall、F-measure。", "objectivity_reason_cn": "该实验包含人的判断，但人的任务是依据培训规则和书面证据将病例归类为外部可核验的真/假阳性，且正确性由专家核查证据决定；这是对数据制品在下游决策任务中效果的客观评估。"}]
- Artifact: 面向公共卫生的社会倾听平台（social listening platform），属于可识别的一类软件制品：从多个在线渠道自动发现、评估、优先抓取相关健康信息并提供给下游分析。 — 作者设计了HealthSense的三大模块：RAM（相关性评估模块）、CAM（可信度评估模块）、LAM（渠道景观导航模块），并实现多级双向图传播、双关系边增强节点嵌入、GNN图分类、基于RAM/CAM/LAM得分的优先队列抓取机制，以及基于活动理论的多路复用关系特征。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除具体案例（PMDS、阿片类药物）和专门数据集后，文章仍提供了关于‘面向时间敏感公共卫生任务的社会倾听平台应如何设计’的知识：如何用RAM/CAM/LAM模块评估相关性、可信度和通道穿越，如何使用多路复用网络特征、图传播和双关系嵌入来提高抓取效率和下游事件检测能力。这些是可进入其他社会倾听平台实例的设计机制。
- Decision: 客观指标：核心评价指标是相关URL收集的precision/recall/F1、事件检测的case recall/signal precision以及用户对病例真/假阳性的识别准确率，均可由系统日志、专家黄金标签和下游统计事实验证，不依赖用户满意度或语义质量评价。核心目标：论文明确以提升社会倾听平台收集效率、及时性和下游公共卫生活动检测能力为设计目标和核心贡献，而非仅解释理论关系。真实制品：作者设计并实现了HealthSense平台，包含RAM/CAM/LAM三个模块、图传播和GNN组件，在3700万URL测试床和PharmCo现场实际运行并评价。类级贡献：论文面向‘公共卫生社会倾听平台’这一类软件制品，提出可复用的元需求、设计要素和机制（表2，a-j），并在PMDS和阿片任务两个实例中实例化；移除具体案例后仍留下关于此类平台应如何设计相关性/可信度/跨渠道导航机制的可迁移知识。综合三个模块均通过，因此strict_include=true。
- Confidence: 0.9

## A decision support framework and prototype for aircraft dispatch assessment

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113338
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "信息检索时间", "measurement_cn": "实验中对受训飞机维修技术员使用PDF版AMM与简化版原型查找正确维护文档所需时间，通过系统时间记录自动获取；PDF平均203秒，原型平均55秒，降低73%。", "objectivity_reason_cn": "时间是可直接观测的物理量，不依赖人的感受、语义判断或价值评价。"}, {"name_cn": "放行决策时间", "measurement_cn": "在TAP运营环境中的5次模拟演示中，通过观察和访谈估计当前流程平均15分钟，使用原型后约15秒，声称最高降低98%。", "objectivity_reason_cn": "决策时间本身是客观可测事实；虽然样本小且基于估计，但构念仍是时间而非主观体验。"}, {"name_cn": "正确找到文档的数量/比例", "measurement_cn": "六个问题案例均指向AMM中特定且唯一的维护任务，实验者依据该任务核对受训者返回结果；PDF为89/102，原型为91/102。", "objectivity_reason_cn": "正确性由预先定义的具体文档任务决定，属于固定事实核对，而非专家或用户的好坏偏好评价。"}]
- Artifact: 飞机放行评估决策支持系统/实时运营维护决策支持原型 — 作者设计并实现了基于Node.js的Web/移动原型：自定义SGML/XML解析器自动索引TSM、AMM、MEL；依据故障信息自动识别维护备选方案；按CSN过滤；根据可用时间（式1）与所需时间（式2）计算预期放行结果并排序；BM25信息检索界面；三步骤用户界面（选择缺陷、选择任务、确认任务）。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 如果移除TAP的WAIV案例、具体飞机数据和专门制作的界面，剩余的贡献仍是飞机放行/复杂维护DSS的可复用设计知识：六步决策过程模型、自动化备选方案识别与排序机制、数据集成层、时间准则计算公式、人工在环的交互设计。这些不是算法或领域机制本身，而是可进入同类软件制品的设计组件。
- Decision: 客观指标方面，核心成功指标是信息检索时间和放行决策时间，均为完全客观、可直接观测的时间指标；实验给出了精确的秒级减少，运营演示也以时间减少为核心结论。正确找到文档按预先定义的具体任务核对，不属于人类语义偏好。核心目标明确为减少决策时间、避免延误和成本，时间改善是论文的主要贡献，而非次要因变量。软件制品方面，论文设计和实现了可运行的Web/移动决策支持原型，包括自定义手册解析器、自动备选方案识别、过滤排名和用户界面，并在实验和真实运营环境中实际运行和评价。类级贡献方面，作者贡献的是面向飞机放行/复杂维护DSS的可复用框架和原型机制，明确说明可迁移到其他复杂维护环境，移除单一案例后仍保留可复用的DSS设计知识。因此三个模块均通过，strict_include为true。
- Confidence: 0.88

## Responsible cognitive digital clones as decision-makers: a design science research study

- Year/journal: 2023 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2022.2073278
- Metric/core status: objective_fixed_factual_labels / objective_improvement_primary
- Metrics: [{"name_cn": "决策准确性（F1-score）", "measurement_cn": "在员工奖励分配、危机资源重组等流程中，将决策与门户记录的实际成就、事后订单是否必要等事实标签做混淆矩阵，计算F1。", "objectivity_reason_cn": "标签来自系统记录、实际成就数据、订单是否被取消/修改等可审计事实，不依赖人的感受或语义质量评价。"}, {"name_cn": "节省人时（human hours saved）", "measurement_cn": "招聘流程中每个候选人的审阅时间由约10分钟降至1分钟，按学术委员会规模与每年候选人数推算总节省时间。", "objectivity_reason_cn": "时间、人数、交易次数均为客观可计数事实。"}, {"name_cn": "并行的流程数量/克隆数量", "measurement_cn": "统计大学实际运行的Pi-Mind agents数量、已启动并存储的过程数量。", "objectivity_reason_cn": "由系统日志和流程数据库统计得出。"}]
- Artifact: 认知数字克隆决策代理（Pi-Mind agent），即可代表人类决策者进行决策的智能代理/数字孪生系统。 — 
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除NURE、乌克兰HE、NATO案例名称和特定界面后，仍保留关于'认知数字克隆决策代理'类软件应如何设计、训练和运行的可复用知识；若只剩GAN或PSV算法，则会退化为AI方法，但论文的核心贡献是作为IT制品的Pi-Mind agent及其设计机制，而非算法本身。
- Decision: 客观指标方面：核心评价指标为F1决策准确性、节省人时和运行流程数，均来自系统记录、事实标签和可审计时间，且论文以提升这些客观指标为设计目标和贡献核心。软件制品方面：Pi-Mind agent作为认知数字克隆决策代理，包含PSV、T|C-SGAN训练架构、决策本体和克隆生命周期，作者实际在TRUST门户和NATO实验室中实现并运行，并将F1提升和时间节省归因于该制品。类级贡献方面：论文的目标是一类可复用的认知数字克隆决策代理软件，提出设计原则和组件机制，适用场景包括高校管理、安全物流、工业4.0等，不是一次性案例包装或纯算法论文。因此三个模块均通过，strict_include为true。
- Confidence: 0.88

## Estimating the Impact of “Humanizing” Customer Service Chatbots

- Year/journal: 2021 / Information Systems Research
- DOI: 10.1287/isre.2021.1015
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "交易转化（Conversion）", "measurement_cn": "系统日志记录客户是否完成二手服装回购流程并获得可打印的运单标签，二值变量0/1。", "objectivity_reason_cn": "是否完成交易是可审计的外部事实，不依赖人的感受、偏好或语义评价。"}, {"name_cn": "信息披露里程碑（邮寄地址/法定姓名/电话等）", "measurement_cn": "基于聊天记录/系统日志确认客户是否推进到各信息披露步骤。", "objectivity_reason_cn": "这些步骤由固定的业务流程定义，状态可从系统日志中确定性观测。"}]
- Artifact: 客户服务聊天机器人（customer service chatbot） — 作者使用DialogFlow和Python定制构建了Facebook Messenger聊天机器人；设计了社交临场（人类名字、非正式语言、输入/已读提示）、动态回复延迟（70词/分钟）、幽默（随机笑话）三种拟人化机制，并整合了回购业务流程和随机报价逻辑。
- Class contribution: software_artifact_class / implicit_but_well_supported / core_research_contribution
- Counterfactual: 若移除服装零售商案例、二手回购数据集和专门界面，仍剩下了关于客户服务聊天机器人应如何采用拟人化功能（社交临场、延迟、幽默）以影响转化和报价敏感性的可复用设计知识；不是只剩算法、市场机制或单一案例方案。
- Decision: 客观指标方面，核心结果变量是交易转化率和信息披露里程碑，均为可审计的系统日志事实，不依赖主观感受；研究问题和贡献声明都以提升这些客观结果为目标。软件制品方面，作者实际设计并运行了一个客户服务聊天机器人，具体的拟人化机制（社交临场、延迟、幽默）就是被评价的设计干预，转化率提升可直接归因于该软件制品的功能设计。类级贡献方面，目标制品类别是客户服务聊天机器人，独立于服装零售商案例；三种拟人化设计机制可复用于同类系统，论文也明确以该类系统的设计效能为贡献。因此三个模块均通过。
- Confidence: 0.87

## Design Principles for Signal Detection in Modern Job Application Systems: Identifying Fabricated Qualifications

- Year/journal: 2020 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2020.1790201
- Metric/core status: objective_fixed_factual_labels / objective_improvement_primary
- Metrics: [{"name_cn": "虚构资格/欺骗性回答检测的分类性能（Accuracy, Precision, Recall, F1）", "measurement_cn": "通过原型SIGHT采集的语音、面部、语言行为特征，在100轮蒙特卡洛交叉验证下使用SVM、随机森林、Boosting LR、Bagged ANN进行分类；标签依据申请者在看到职位要求前后对技能自评的确定性变化规则生成：初始为零后改为有经验则标记为虚假。", "objectivity_reason_cn": "标签来自可审计的自我报告变化事实，不依赖考官、专家或众包者对回答质量、语义或态度的主观评价；分类指标是可直接计算的外部可验证性能。"}]
- Artifact: 现代求职申请/异步视频面试信号检测系统（SIGHT类系统），可扩展至安全审查、审计访谈等大规模行为评估场景。 — 原型系统包含：基于web的异步结构化面试界面；30秒准备/60秒回答的计时与录制流程；使用普通webcam采集语音、面部和语言信号；OpenSmile、IBM Watson、SPLICE、Intraface等特征提取管线；基于理论的信号选择与受试者内标准化；多信号融合分类模块。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除当前的本科生模拟实验、StatView问题和特定数据集后，仍然剩下关于‘一类能够自动采集并分析求职者行为信号的软件系统应如何设计’的可复用知识，即SIGHT的设计原则、信号处理流程和评估机制；剩余贡献不是单纯算法或领域政策。
- Decision: 文章核心目标是客观识别求职申请中的虚构资质，使用由自我报告变化规则生成的确定标签，并以分类准确率、精确率、召回率和F1作为核心结果；作者设计并实际运行了SIGHT原型系统；贡献明确指向一类可复用的求职申请信号检测软件系统的设计原则，符合三个模块的全部条件。
- Confidence: 0.85

## HyperCARS: Using Hyperbolic Embeddings for Generating Hierarchical Contextual Situations in Context-Aware Recommender Systems

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2022.0202
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "推荐排序性能：Hit@K, MRR@K", "measurement_cn": "基于用户与物品交互记录、训练/验证/测试划分，以及模型打分排序结果计算；K=1,3,5。", "objectivity_reason_cn": "来源于真实使用记录（评分、签到、点击等）和确定的排序计算公式，不依赖人的主观评价或语义判断。"}, {"name_cn": "评分预测性能：RMSE, MAE", "measurement_cn": "在Frappe和Yelp显式评分数据上，比较预测评分与真实评分的均方根误差和平均绝对误差。", "objectivity_reason_cn": "真实评分作为外部可审计的用户交互记录；误差计算遵循固定公式，结果客观可复现。"}]
- Artifact: 上下文感知推荐系统（CARS）的核心上下文建模与推荐组件 — 设计并实现HyperCARS组件：在Poincaré球上构建上下文的双曲VAE嵌入，采用AHC/HDBSCAN层次聚类生成层次化上下文情境hcs，并将hcs作为聚类ID路径松耦合融入NeuMF扩展推荐模型；还实现完整树层级注意力机制自动选择重要层级。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除Frappe、Gowalla、Yelp等具体数据集和专门实验包装后，仍然留下关于“如何为CARS设计可复用的层次双曲上下文情境组件”的知识：双曲嵌入→层次聚类→hcs路径→松耦合融入推荐模型。这不是单一案例的包装脚本或算法孤立贡献，而是该类软件核心组件的一般化设计方法。
- Decision: 核心目标是通过HyperCARS组件提升上下文感知推荐的客观性能（RMSE、MAE、Hit@K、MRR@K），这些指标基于真实交互记录和固定计算公式，不依赖主观感受或语义优劣判断；论文明确设计、实现并实际运行了CARS核心组件，包括双曲VAE嵌入、层次聚类生成hcs和松耦合推荐模型；贡献指向可复用的CARS类软件组件，而不仅限于单一数据集或算法实验。解释性虽作为附加贡献，但通过决策树/IDS的客观拟合指标评估，且不构成唯一核心成功标准。因此满足三个模块的全部条件。
- Confidence: 0.85

## A prescriptive analytics framework for efficient E-commerce order delivery

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113584
- Metric/core status: objective_fixed_factual_labels / objective_improvement_primary
- Metrics: [{"name_cn": "配送总成本/单均成本", "measurement_cn": "通过仿真实验计算，涉及配送车辆数、行驶距离、车辆日运营成本、燃油成本以及因失败配送导致的重新配送成本。", "objectivity_reason_cn": "成本由可审计的运营数量（车辆、距离、尝试次数）和给定费率计算，不依赖人的感知或语义判断。"}, {"name_cn": "配送尝试次数", "measurement_cn": "仿真中统计每天实际需要执行的订单配送尝试次数，包括失败后的重新配送。", "objectivity_reason_cn": "配送尝试和失败配送是运营事实，可从订单交付记录和系统日志中确定性观测。"}, {"name_cn": "配送成功预测性能", "measurement_cn": "在历史订单交付数据上计算AUC、G-mean、召回率、精确率、F1和准确率。", "objectivity_reason_cn": "预测标签为配送成功/失败，是外部可验证的事实状态，不是基于人类感受、偏好或语义价值的判断。"}]
- Artifact: 面向电子商务最后一公里配送的排程决策支持系统/框架（delivery scheduling DSS） — 设计了两阶段机制：第一阶段由机器学习模型生成订单成功画像（OSP），将配送成功概率映射到一天中的时间点；第二阶段从OSP推断每个订单的合适配送时间窗，并将其作为VRPTW约束，还改进了插入启发式，加入订单优先级和按区域方向聚类的规则，最后用迭代局部搜索改进排程。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除当前电商平台、两个hub的数据集以及专门制作的界面后，剩余贡献仍是一类配送排程DSS的可复用功能结构：用订单和位置特征预测配送成功、生成订单成功画像、推断配送时间窗、用带优先级和区域方向的VRPTW启发式生成排程。因此不是只留下算法/数学规则或单一案例方案。
- Decision: 客观指标方面，核心评价指标是配送成本、配送尝试次数、车辆数以及基于配送成功/失败事实标签的预测性能，全部可确定性观测且不依赖人类主观判断；客观指标改进是论文的核心目标与贡献。软件制品方面，作者实际实现并运行了决策支持框架，包括ML预测模型、订单成功画像生成、时间窗推断和VRPTW排程启发式，并通过仿真实验评价其效果。类级贡献方面，贡献指向可复用的最后一公里配送排程决策支持系统类别，而不是一次性案例、纯算法包装或领域机制。因此三个模块全部通过。
- Confidence: 0.82

## Containing COVID-19 through physical distancing: the impact of real-time crowding information

- Year/journal: 2020 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2020.1814681
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "就诊地点选择的拥挤等级（是否选择低拥挤地点）", "measurement_cn": "在线实验中，参与者在虚构网站 find-your-doctor.org 上从四个已知拥挤等级（0%、33%、67%、100%）的医疗诊所中选择一个，系统记录其选择；使用序数逻辑回归分析所选拥挤等级。", "objectivity_reason_cn": "选择行为由实验系统直接记录，选项的拥挤等级由操纵预先固定，不依赖参与者或研究者的主观评价、语义判断或质量评分。"}]
- Artifact: 显示拥挤信息（CI）的决策支持系统（DSS）/数字选择环境，例如医疗诊所选择网站、地图类实时拥挤信息应用。 — 作者设计并实现了虚构网站 find-your-doctor.org，包含地图、四个医疗诊所及用小人图标表示的拥挤等级；在实验条件下加入CI，并将CI的即时性操作化为“过去2个月的通常人数”（历史平均）与“刚刚更新的实时人数”（实时）两个版本。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 如果移除医疗诊所这一具体案例、德国/意大利数据以及find-your-doctor.org这个特定界面，仍保留的知识是：在显示拥挤信息的决策支持系统中，提供CI以及更高即时性的CI可以引导用户选择低拥挤地点；这是关于一类DSS应如何设计其信息展示机制的可复用设计知识，而不仅仅是算法、方程或领域政策。
- Decision: 文章通过在线实验考查DSS中CI及其实时性对用户选择低拥挤地点的影响；核心结果是指实际选择行为（所选地点的拥挤等级），客观可直接观测，且提升选择低拥挤地点是核心目标与贡献。作者构建并运行了find-your-doctor.org实验网站，实际实现了CI显示与即时性提示机制，并将效果归因于该设计机制。贡献明确面向显示CI/实时拥挤信息的DSS类别，提出可迁移的设计建议，而非仅算法或领域政策。三个模块均通过。
- Confidence: 0.82

## Ephemeral State-Dependent Recommendation for Digital Content

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2022.664
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "推荐书籍阅读率（readrate）", "measurement_cn": "12天观测期内，用户至少阅读一章的推荐书籍数占推荐总数的百分比；由平台阅读日志计算。", "objectivity_reason_cn": "阅读行为是外部可审计事实，不依赖用户对质量、价值或语义的判断。"}, {"name_cn": "推荐书籍阅读时长（readtime）", "measurement_cn": "用户阅读推荐书籍的总分钟数；由平台日志自动记录。", "objectivity_reason_cn": "时长是确定性可观测的行为指标。"}, {"name_cn": "支付金额（payment）", "measurement_cn": "用户在观测期内对推荐内容产生的支付金额（美元）；来自平台交易记录。", "objectivity_reason_cn": "交易金额是客观商业事实。"}, {"name_cn": "非推荐书籍阅读量（溢出效应）", "measurement_cn": "观测期内阅读的非推荐书籍数量，按总体、同类别、跨类别分别计数；来自平台阅读日志。", "objectivity_reason_cn": "阅读计数是客观行为数据，不依赖人的主观评价。"}]
- Artifact: 数字内容推荐系统/推荐模块（电子书平台个人虚拟书架上的推荐组件） — 设计并实现状态依赖推荐规则：根据用户近7天阅读类型宽度判定短暂状态（固化/觅食），在同类推荐（assimilation）与多样化推荐（diversification）之间自适应切换；实验中采用简单的基于已读/未读类型的随机选择算法执行该策略-状态配对机制。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除电子书平台案例、数据集和具体界面后，论文仍提供了关于数字内容推荐系统应如何根据用户短暂消费状态在同类与多样化策略间自适应切换的设计知识，而非仅剩下算法或数学模型。
- Decision: 核心结果指标均为平台日志和交易记录的客观行为（阅读率、阅读时长、支付、溢出阅读），不存在以主观语义评价作为成功标准；研究问题和贡献声明以状态依赖推荐方案带来消费/利润提升为核心。作者通过修改电子书平台推荐规则并在10.8万真实用户上运行田野实验，实际实例化了状态依赖推荐组件；该机制可移植到其他数字内容推荐系统，属于类级软件制品贡献。
- Confidence: 0.82

## RADAR: A Framework for Developing Adversarially Robust Cyber Defense AI Agents with Deep Reinforcement Learning

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2024/17339
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "规避率（Evasion Rate, ER）", "measurement_cn": "在保持恶意功能的前提下，对生成对抗样本逐一交由被测恶意软件检测器判定；ER = 被判定为良性（成功规避）的变体数 / 生成的变体总数。", "objectivity_reason_cn": "检测器的输出是确定性的软件判定结果，不依赖人的感受、偏好或语义质量评价；恶意/良性标签基于文件事实与检测器规则。"}, {"name_cn": "假阳性率（False Positive Rate, FPR）", "measurement_cn": "在干净Windows环境收集的良性可执行文件上统计误报为恶意的比例；FPR = 被误报为恶意的良性文件数 / 良性文件总数。", "objectivity_reason_cn": "良性样本来源和检测器结果均为可核验的外部事实，计算规则固定，无主观语义判断。"}]
- Artifact: 面向网络防御AI智能体（如恶意软件检测器）的对抗攻击仿真、鲁棒性评估与强化训练框架/系统 — 设计了RADAR两阶段机制：第一阶段r-VAC通过Concrete分布重参数化离散动作空间，生成对抗恶意软件变体；第二阶段RL-RO将r-VAC策略产生的对抗样本纳入鲁棒优化外极小化，迭代微调检测器；并基于OpenAI Gym和malware-env构建可运行的RL环境，使用LIEF实现恶意软件动作。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 若移除VirusTotal数据集、LGBM/MalConv/NonNeg三个具体检测器和恶意软件专用动作表，剩余贡献仍是面向'网络防御AI智能体'这一软件制品类别的可复用对抗攻击仿真与鲁棒化流程设计，而非仅剩孤立的算法、方程或市场机制。
- Decision: 核心指标规避率和FPR均为外部可核验的检测器判定计数，不依赖人的语义或感受评价；文章以鲁棒性提升为核心设计目标和贡献。RADAR被实现为可运行的对抗攻击仿真与鲁棒化框架/系统，包含r-VAC和RL-RO等可复用组件，并在恶意软件检测这一具体实例上验证；其贡献指向网络防御AI智能体这一软件制品类别，而非仅算法、实验脚本或一次性案例。
- Confidence: 0.82

## The crowd against the few: Measuring the impact of expert recommendations

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113345
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "观看短片数", "measurement_cn": "基于系统点击流日志统计每位用户观看的短片数量", "objectivity_reason_cn": "由平台可审计点击记录直接生成，不依赖用户主观评价"}, {"name_cn": "推荐点击次数", "measurement_cn": "基于系统点击流日志统计用户点击推荐列表的次数", "objectivity_reason_cn": "客观系统行为记录"}, {"name_cn": "平台访问次数", "measurement_cn": "基于系统访问日志统计用户访问网站的次数", "objectivity_reason_cn": "客观系统行为记录"}, {"name_cn": "活跃访问/多短片访问次数", "measurement_cn": "基于点击流日志统计单次访问中至少观看一个或多个短片的访问数", "objectivity_reason_cn": "客观系统行为记录"}, {"name_cn": "回访率与留存率", "measurement_cn": "根据用户访问日期和最后一周访问状态计算", "objectivity_reason_cn": "由平台访问日志确定，结果可复核"}, {"name_cn": "推荐列表多样性（ILS）", "measurement_cn": "基于推荐列表中短片元数据计算加权余弦相似度", "objectivity_reason_cn": "按固定公式和元数据计算，不依赖用户感受"}, {"name_cn": "品味覆盖率与唯一推荐使用率", "measurement_cn": "基于被点击推荐短片数和用户观看短片数计算", "objectivity_reason_cn": "由点击行为和推荐记录确定"}]
- Artifact: 在线视频点播推荐系统（Recommender System） — 在现有商用推荐系统中加入专家维护的推荐列表组件，将专家推荐与系统生成推荐混合展示，约一半推荐来自专家，并在首页和个人短片页实际生效；对照组不包含专家推荐。
- Class contribution: software_artifact_class / implicit_but_well_supported / core_research_contribution
- Counterfactual: 移除具体电视网络、该视频网站数据集和专门制作界面后，仍然留下对某类可运行软件制品的设计知识：在推荐系统中引入并混合专家维护的推荐列表可提高用户参与和多样性；这一机制可进入其他推荐系统实例，而非仅是该网站的一次性方案。
- Decision: 核心指标均为客观可审计行为或推荐属性，包括观看量、访问次数、推荐点击、回访/留存率、多样性和品味覆盖率；满意度为主观测量但只是非核心补充结果，不影响核心客观贡献。软件制品真实存在且被作者实质修改：在商用视频推荐系统中加入专家推荐混合组件并实际部署运行，随机对照实验证明处理组在多个客观指标上显著提升。贡献对象是推荐系统这一软件制品类别，机制可迁移至其他推荐系统，不是单纯算法、市场机制或单案例解决方案。因此三个模块均通过。
- Confidence: 0.82

## <scp>Context‐aware</scp> user profiles to improve media synchronicity for individuals with severe motor disabilities

- Year/journal: 2022 / Information Systems Journal
- DOI: 10.1111/isj.12337
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "任务完成时间", "measurement_cn": "原型系统记录被试完成规定医疗/舒适表达（如“I'm tired”“Adjust head to middle”“Ears sore”）所需的时间，比较有无情境感知用户画像两种条件下的完成时间。", "objectivity_reason_cn": "时间由系统或客观计时获得，不依赖人的感受、语义评价或价值判断。"}, {"name_cn": "选择错误数与扫描遗漏错误数", "measurement_cn": "统计被试在扫描界面中错误选择或错过选项的次数。", "objectivity_reason_cn": "错误次数是可审计的系统日志事实，不依赖主观判断。"}]
- Artifact: 面向严重运动障碍者的增强与替代沟通（AAC）系统/原型，尤其是带情境感知用户画像的医疗与舒适需求表达界面。 — 在AAC系统中加入情境感知用户画像和访客画像，依据时间、地点、对话者过滤和调整词/短语/符号选项；同时设计并实现了医疗舒适本体驱动的扫描选择界面，并比较有/无情境感知用户画像两种界面。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除Todd案例、具体医疗舒适数据集和专门界面后，仍然保留关于AAC系统应如何设计的可复用知识：情境感知用户画像/访客画像机制、按上下文裁剪符号集、设计原则等；这些知识可指导其他AAC系统的设计。
- Decision: 客观指标方面，任务完成时间和错误次数是可直接观测、可审计的客观结果，且速度提升是设计需求1的核心目标；感知速度量表为补充结果而非核心成功标准。软件制品方面，作者设计并实际运行了一个AAC原型，其核心机制是情境感知用户画像对词/短语选项的过滤与调整，且客观速度改善归因于该机制。类级贡献方面，作者明确将贡献定位于AAC系统设计中的可复用设计要素和设计原则，而非一次性案例软件或纯算法。因此三个必要条件均满足。
- Confidence: 0.8

## An interactive decision support system for real-time ambulance relocation with priority guidelines

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113712
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "平均响应时间（ART）", "measurement_cn": "基于真实呼叫数据模拟一周所有班次，从呼叫到救护车到达现场的时间，按呼叫类型统计平均值，单位为分钟。", "objectivity_reason_cn": "响应时间是可审计的物理时间变量，不依赖人的感受或语义评价。"}, {"name_cn": "平均覆盖率（ACR）", "measurement_cn": "呼叫在预设的7/15/25分钟等要求时间范围内得到响应的比例，由系统日志和确定性判断计算。", "objectivity_reason_cn": "覆盖率是依据客观时间阈值对事件是否满足要求的事实计数，不涉及主观质量评价。"}, {"name_cn": "平均可用救护车数（ANAA）", "measurement_cn": "每次呼叫发生时在要求时间范围内可调度的救护车数量，由系统状态计算。", "objectivity_reason_cn": "可调用车辆数由真实系统状态和空间距离决定，是可观测的运营事实。"}, {"name_cn": "平均和总工作时长（AWA/TWAA）", "measurement_cn": "每辆救护车及全部救护车在一个班次中的总活动分钟数，由仿真日志累积。", "objectivity_reason_cn": "工作时长是物理时间消耗，可由系统日志精确测量。"}]
- Artifact: 实时救护车再定位决策支持系统（EMS ambulance relocation decision support system） — 
- Class contribution: software_artifact_class / implicit_but_well_supported / core_research_contribution
- Counterfactual: 移除德黑兰案例名称、具体数据集和专门制作的界面后，仍留下关于“实时救护车再定位DSS应如何设计”的知识：事件驱动更新、覆盖数动态修正、工作量限制机制、风险分级优先级指南。这些属于可复用的DSS组件/工作流，而非只剩纯算法或领域政策。
- Decision: 客观指标方面：核心评价指标为响应时间、覆盖率、可用救护车数和总工作时长，均为可审计的运营事实，不依赖主观满意度或语义评价；且摘要、引言、结论均以这些客观指标的改善作为DSS的核心贡献。软件制品方面：作者实际实现了带数据库、过程模型和GUI的DSS，并在真实数据上运行一周仿真，不是仅有算法脚本或概念原型。类级贡献方面：贡献面向实时救护车再定位DSS这一可重复实例化的软件类别，所设计的流程、覆盖数动态机制、工作量约束和风险优先级指南可迁移至同类系统；德黑兰案例只是该类别的一个运行实例。因此三个模块均通过，strict_include为true。
- Confidence: 0.8

## Providing more regular road signs infrastructure updates for connected driving: A crowdsourced approach with clustering and confidence level

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113443
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "道路标志合并结果的精确率和召回率（相对真实道路标志位置）", "measurement_cn": "将合并得到的道路标志位置与人工采集的真实道路标志位置比较，按小于20米和航向差小于45°判定匹配，形成混淆矩阵后计算精确率和召回率。", "objectivity_reason_cn": "道路标志的存在性和物理位置是外部可核验事实，比较规则为固定几何阈值，不依赖人的价值或语义评价。"}, {"name_cn": "融合系统相对仅摄像头系统的TPR/FNR/FPR改善", "measurement_cn": "在真实路段上模拟摄像头检测与云端合并道路标志融合，统计真阳性、假阳性和假阴性，比较两种系统的率值。", "objectivity_reason_cn": "检测结果与真实标志存在性的匹配可依据固定规则计算，改进幅度是客观可审计的检测性能指标。"}, {"name_cn": "摄像头原始检测的精确率与召回率作为基线", "measurement_cn": "对摄像头检测事件与真实道路标志存在性构建混淆矩阵，计算precision和recall。", "objectivity_reason_cn": "摄像头检测事件和道路标志物理存在性均为可观测事实，无需主观判断。"}]
- Artifact: 基于众包车载传感器数据的道路标志地图更新/合并平台，具体为云端道路标志合并与置信度计算组件（road sign consolidation system/component） — 设计了滑动时空查询、地理瓦片分配、基于位置和航向的meanshift聚类、聚类细化、负样本推断，以及基于贝叶斯概率和指数衰变的置信度计算流程；同时设计云端数据接入、存储、预处理和分发框架。
- Class contribution: software_artifact_class / implicit_but_well_supported / core_research_contribution
- Counterfactual: 移除Regensburg案例、具体数据集和专用实验设置后，仍留下关于众包道路标志地图更新系统应如何设计的知识：包括云端数据接入与存储架构、基于位置/航向/瓦片的可扩展聚类、负样本推导、带半衰期的贝叶斯置信度计算，以及车辆端融合策略示例；这些不是仅剩通用算法或市场机制。
- Decision: 客观指标方面，道路标志存在性和位置是外部物理事实，实验以精确率、召回率、TPR/FNR/FPR等客观检测性能作为核心结果，且研究目标和贡献均指向提升地图道路标志信息的准确性和更新及时性。软件制品方面，文章描述了并实际运行了一个云端道路标志合并与置信度计算组件，该组件是所提平台的真正核心，而非单纯算法包装。类级贡献方面，该合并组件与置信度机制可复用于道路标志地图更新系统类别，作者也明确将其定位为可服务车厂、地图商和导航服务商的可扩展平台组件，并非一次性案例解决方案。因此三个条件均满足。
- Confidence: 0.8

## ForeSim-BI: A predictive analytics decision support tool for capacity planning

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113266
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "总工作量预测误差（PE/MAE/MAPE）", "measurement_cn": "将ForeSim-BI预测的8C检查工作量区间上界与实际维护工时观察值比较，按固定公式计算百分比误差、平均绝对误差和平均绝对百分比误差；实际工时来自主机维修组织的工程和维护项目记录。", "objectivity_reason_cn": "维护工时是可审计的事实性记录，预测值与观察值的差值由确定公式计算，不依赖人的感受、偏好或语义判断。"}, {"name_cn": "工作类型、工作阶段和工作技能的MAE/MAPE", "measurement_cn": "分别按维护工作类型（WT）、工作阶段（WP）和技能（WS）汇总工时，比较ForeSim-BI预测区间上界与实际观察工时，计算平均绝对误差。", "objectivity_reason_cn": "这些分类下的工时同样是可观察、可记录的事实，误差计算为确定性算术操作，不包含主观评价。"}]
- Artifact: 面向复杂产品系统维护组织的维护能力规划决策支持系统（DSS），具体实例为航空维修MRO中的预测性能力规划工具ForeSim-BI。 — 作者设计并集成了四个功能模块：AHW预测模块（生成先验工作量分布）、贝叶斯推断模块（随新观察更新为预测分布）、基于蒙特卡罗与自助抽样的仿真模块（将总工作量分解为工作类型/阶段/技能变量）、贝叶斯网络模块（结合历史与模拟数据进行概率推理）；并设计LP模型自动选择总工作量区间和其余工作量区间的规划组合，避免了人工选择的不确定性和效率损失。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除葡萄牙航空MRO案例、8C数据集和具体专门化界面后，论文仍提供一种可复用的维护能力规划DSS设计知识：如何用AHW先验预测、以新观察做贝叶斯更新、用蒙特卡罗/自助抽样分解工作量、用贝叶斯网络整合历史与模拟数据，并用LP自动选择规划工作量区间。这套模块化和更新机制可进入其他维护能力规划DSS实例，而不只是算法或数据集本身。
- Decision: 客观指标方面：文章以维护工时预测误差（PE/MAE/MAPE）为工具评价的核心成功标准，这些值是真实工时记录与预测值之间的确定性比较，不涉及主观构念。核心目标方面：标题、摘要和验证均明确指向通过工具设计提升预测准确性和能力规划效率，并量化成本节省潜力。软件制品方面：ForeSim-BI是一个可识别的维护能力规划决策支持系统类别实例，作者设计并实现了四个模块和LP选择机制，且用真实数据运行并验证。类级贡献方面：作者明确面向复杂产品系统维护组织的一般性DSS设计，模块化集成、观察驱动的贝叶斯更新和区间选择流程可复用于同类工具，而非一次性案例解决或纯算法研究。因此三个模块全部通过。
- Confidence: 0.78

## Would you please like my tweet?! An artificially intelligent, generative probabilistic, and econometric based system design for popularity-driven tweet content generation

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113497
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "推文总参与度（retweets + favorites）", "measurement_cn": "通过Twitter API返回的推文retweet和favorite计数之和，系统日志记录的外部事实数据", "objectivity_reason_cn": "该指标是平台记录的可审计事实计数，不依赖人的感受、语义理解或价值判断"}]
- Artifact: 社交媒体推文生成/建议决策支持系统（DSS） — 多模块系统设计：数据流与过滤、上下文解释（LDA）、文本分析（句法与情感）、流行度预测（8种计量模型）、生成式概率模型（PoS计数、序列生成、混合分布词采样）、报告模块和推文评估模块
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除2018年中期选举政治推文案例、具体数据集和临时R界面后，论文仍提供关于推文生成DSS应如何设计的模块化知识（数据流、上下文解释、文本分析、流行度预测、生成式PoS序列采样、报告与评估），这些机制可迁移至其他社交媒体推文生成系统实例。
- Decision: 客观指标：核心目标是最大化推文总参与度（retweets+favorites），该指标为平台记录的外部事实，完全客观且为系统设计的最终目标。真实软件制品：文章提出了模块化的推文生成/建议DSS，并实际用R实现和运行，包括数据采集、文本分析、预测模型、生成模型和报告模块，指标改善归因于系统设计机制。类级贡献：贡献明确指向流行的推文生成与建议软件类别，模块化和生成机制可复用于其他实例，演示只是该类别的一个实例而非一次性解决方案。因此严格纳入。
- Confidence: 0.78

## Gamifying knowledge sharing in humanitarian organisations: a design science journey

- Year/journal: 2020 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2020.1718009
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "KMS访问次数", "measurement_cn": "系统日志记录用户过去30天内的平台访问次数，作为参与度指标。", "objectivity_reason_cn": "访问次数是系统日志可直接统计的行为事实，不依赖人的感受或语义评价。"}, {"name_cn": "新增条目数量", "measurement_cn": "实验任务中用户在KMS空间内新添加的资源数量，由系统记录。", "objectivity_reason_cn": "新增条目是可审计的系统行为计数，独立于主观体验。"}, {"name_cn": "新增条目上的评论数", "measurement_cn": "用户对新增资源发表的评论数量，由系统日志统计。", "objectivity_reason_cn": "评论数量是客观行为计数，可直接从系统日志获得。"}, {"name_cn": "对已有条目的点赞和评论数", "measurement_cn": "用户对KMS空间中已有条目点赞和评论的次数，由系统日志统计。", "objectivity_reason_cn": "这些是外部可观察的操作行为计数，属于系统日志指标。"}]
- Artifact: 带游戏化反馈的知识管理系统（KMS），以及KMS外的环境反馈可视化组件（虚拟水族箱）。 — 作者在Graasp KMS中设计了用户个人资料游戏化反馈机制，包括六维指标（Commenter、Influencer、Contributor、Collaborator、Visitor、Sharer）、总体Graasper分数、百分位等级和蜘蛛网图；同时设计了与KMS联动的虚拟水族箱，将空间活动、用户参与度、评论和文档映射为鱼的大小、数量、水草和岩石等动态环境反馈。
- Class contribution: software_artifact_class / implicit_but_well_supported / core_research_contribution
- Counterfactual: 移除MSF案例、Graasp名称和专门制作的界面后，论文仍保留了关于如何在KMS中设计基于活动日志的反馈可视化、匿名环境反馈对象、百分位等级和利他用户交互等类级可复用设计知识；剩余贡献不是单纯的算法、求解器或市场机制。
- Decision: 核心成功指标为系统日志中的访问次数、新增条目数和评论/点赞数，完全客观，且这些指标是H1a/H1b的主要因变量；主观的sociometric status感知和专家质量评分是机制解释或补充验证，不替代客观核心目标。作者实际设计并运行了Graasp KMS中的游戏化个人资料和虚拟水族箱组件，并通过现场A/B测试和实验室实验将参与度提升归因于这些设计机制。贡献指向可推广的KMS游戏化反馈设计类别，而非单纯算法、仿真或一次性案例方案。
- Confidence: 0.76

## Overcoming Breakdowns in Customer-Chatbot Interaction: Design and Impact of Collaborative Repair Strategies

- Year/journal: 2026 / MIS Quarterly
- DOI: 10.25300/misq/2025/18742
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "故障解决率（breakdown resolution）", "measurement_cn": "实地实验中，根据聊天记录判断顾客在故障后最终是否从聊天机器人收到对其请求的回应，二值变量。", "objectivity_reason_cn": "由系统对话日志确定，不依赖顾客或研究者的主观感受、语义质量或价值判断，是可审计的行为结果。"}, {"name_cn": "故障后立即放弃率（immediate abandonment）", "measurement_cn": "根据对话日志记录顾客在首次故障后是否继续输入下一条消息，二值变量。", "objectivity_reason_cn": "该值由系统记录的实际交互行为决定，客观可验证。"}]
- Artifact: 客户服务聊天机器人及其对话故障修复组件（customer service chatbot repair module） — 
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除InsurCo名称、保险数据集和专门界面后，仍留下关于'客户服务聊天机器人协作式故障修复组件应如何设计'的知识：故障分类维度、自适应消息结构、渐进升级规则和实时处理集成方式。这些是可进入其他同类聊天机器人的组件机制，而非仅剩算法、市场机制或领域方案。
- Decision: 该文属于DSR设计制品研究：核心目标是提升客户服务聊天机器人故障解决的客观行为表现，并在真实运行系统上实现和评价了协作式修复组件。客观指标（故障解决率、立即放弃率）是主要成功标准且得到显著改善；主观满意度/反馈属于辅助影响检验。软件制品类别明确，作者实质设计并运行了修复组件，且贡献面向'客户服务聊天机器人修复策略'这一可复用类级设计，而非一次性案例或算法包装。因此三个模块全部通过。
- Confidence: 0.76

## Analytics with digital-twinning: A decision support system for maintaining a resilient port

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113496
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "船舶到港靠泊率（BoA rate）", "measurement_cn": "在数字孪生仿真中，统计到达船舶在约定时间窗内（通常2小时）完成靠泊的比例；案例中每次仿真包含3天预热期和1天统计期，共1000次IID重复运行。", "objectivity_reason_cn": "该指标可由仿真系统日志直接判定是否在时间窗内靠泊，不依赖人的感受、语义或价值判断。"}, {"name_cn": "港口韧性水平 R(s)", "measurement_cn": "R(s)=灾后最优恢复行动下的BoA率/灾前BoA率（如98.58%），由仿真输出的客观绩效按公式计算。", "objectivity_reason_cn": "基于客观可观测的BoA率之比，计算规则固定，不涉及主观评价。"}, {"name_cn": "正确选择概率（PCS）与计算加速倍数", "measurement_cn": "在固定仿真预算下，OCBA与等量分配EQ各自从仿真估计中选出最佳恢复行动，重复10000次bootstrap抽样得到PCS，并由达到相同PCS所需仿真次数计算加速倍数。", "objectivity_reason_cn": "PCS和加速倍数是可重复计算的过程性能指标，反映DSS计算效率，不依赖主观感受。"}]
- Artifact: 港口韧性决策支持系统（Digital-twin-driven DSS for port resilience），可扩展为数字孪生驱动的港口/基础设施韧性分析软件。 — 作者设计并实现了DSS的恢复分析与韧性分析双模块架构；数字孪生模型以分层方式刻画集装箱码头（泊位与岸桥、堆场与场桥、AGV交通网络）的运作逻辑；将OCBA嵌入恢复分析模块以在有限仿真预算下分配各恢复行动的仿真次数；并对数字孪生模型进行实质升级，加入电动AGV和充电站分配策略。
- Class contribution: software_artifact_class / implicit_but_well_supported / core_research_contribution
- Counterfactual: 移除具体案例（真实规模码头的电力短缺情景）、合成数据集和专门为案例制作的界面后，仍留下DSS双模块架构、数字孪生分层建模方法、OCBA仿真预算分配机制、韧性指标计算与历史分布输出方式、外部输入配置逻辑。这些是关于某类数字孪生驱动的港口韧性决策支持系统应如何设计的可复用知识，而非仅剩下算法、方程或领域方案。
- Decision: 客观指标方面，BoA率、韧性比率、PCS和加速倍数均为可重复观测、不依赖主观语义的绩效指标，且提升这些指标是文章的核心目标。软件制品方面，文章实现并运行了一个数字孪生驱动的港口韧性DSS，包含恢复分析和韧性分析模块，OCBA集成和数字孪生升级属于作者的实质性设计。类级贡献方面，作者贡献的是港口韧性DSS这一类软件的设计架构和可复用机制，案例只是该类的实例；移除具体案例和界面后仍保留DSS设计知识。因此三个模块均通过，严格纳入。
- Confidence: 0.74

## A Warning Approach to Mitigating Bandwagon Bias in Online Ratings: Theoretical Analysis and Experimental Investigations

- Year/journal: 2023 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00817
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "距离显示平均评分的距离（DDAR）", "measurement_cn": "DDAR = |个体评分 - 显示平均评分|；在受控实验中通过显示/不显示平均评分以及不同警告策略，比较个体评分相对显示均值的距离。", "objectivity_reason_cn": "评分数字和显示平均评分均为可观察的数值事实，不依赖人类感知、语义理解或价值判断；从众偏差的程度由可计算的评分距离刻画。"}]
- Artifact: 在线评分/评论平台中的警告反馈组件与交互机制 — 设计了两种警告策略：直接风险提醒（risk-alert）和风险提醒附加排序任务（risk-alert-with-ranking-task）；排序任务要求用户在评分前按整体偏好对目标影片与参照影片进行拖拽排序，以帮助用户形成更准确的基线评估。
- Class contribution: software_artifact_class / implicit_but_well_supported / core_research_contribution
- Counterfactual: 移除微电影案例、Qualtrics界面和具体实验数据后，仍留下“在线评分系统警告组件应如何设计：风险提醒+排序任务”的可复用设计机制；该机制可迁移至其他在线评分/评论平台，而非仅解决单一案例。
- Decision: 客观指标DDAR是核心因变量，直接度量评分向显示均值偏移的程度，不依赖主观语义判断；研究目标与贡献均围绕通过警告组件缓解从众偏差。警告策略被实例化为可运行的在线评分实验界面（弹窗、排序任务、计时交互），并实际运行于四项受控实验；作者进一步将警告策略推广为在线评分平台可采用的反馈/交互组件设计。因而三个模块均通过，strict_include为true。
- Confidence: 0.7

## Animation as a dynamic visualization technique for improving process model comprehension

- Year/journal: 2021 / Information & Management
- DOI: 10.1016/j.im.2021.103478
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "过程模型理解测试得分", "measurement_cn": "参与者针对10个BPMN过程模型回答8道封闭式选择题和1道开放式问题，按预先由专家根据BPMN控制流语义确定的正确答案计分，总分范围0-100。", "objectivity_reason_cn": "答案正误取决于过程模型中的执行顺序、排他、并发、重复等可验证语义，不涉及对质量、价值、美感或偏好的主观评价；开放式问题也按是否存在死锁/活锁等事实进行编码。"}]
- Artifact: 过程模型动态可视化/理解支持环境，即可集成到过程建模工具中的动画化过程模型浏览与交互功能。 — 颜色变换信号、活动状态变化、时间抽象设计，以及低交互连续动画视频和高交互逐步点击动画的两级自适应交互机制。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除具体10个过程模型、数据集和实验被试后，仍剩下关于过程建模工具动画功能如何设计的可复用知识：颜色变换/活动状态/时间抽象、低交互视频与高交互点击动画的自适应切换。这不是单纯算法、方程或市场机制，而是某类软件的界面、交互和反馈组件设计。
- Decision: 客观指标方面，核心结果变量是过程模型理解测试得分，依据BPMN语义的固定正确答案客观计分，主观认知负荷和感知有用性仅为次要探索。核心目标方面，论文明确以动画提升过程模型理解绩效为研究问题，并由实验证实。软件制品方面，作者设计并实际实现了自适应动画环境，具备颜色变换、活动状态、两级交互和自适应机制。类级贡献方面，该环境属于过程模型动画可视化软件类别，作者明确主张可集成到工业建模工具，移除案例和数据集后仍留下可复用的动画功能与交互设计知识。因此三个模块均通过。
- Confidence: 0.7
