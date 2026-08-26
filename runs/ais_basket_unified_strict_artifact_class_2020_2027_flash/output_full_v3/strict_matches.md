# Unified strict matches

Completed: 2475 / 2475
Retained: 27

## Assessing and Enhancing Adversarial Robustness of Predictive Analytics: An Empirically Tested Design Framework

- Year/journal: 2022 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2022.2063549
- Metric/core status: objective_fixed_factual_labels / objective_improvement_primary
- Metrics: [{"name_cn": "性能比率鲁棒性指标", "measurement_cn": "在非对抗测试集和混合对抗样本测试集上分别计算准确率、精确率、召回率、F1、ROC，再取比值作为鲁棒性衡量", "objectivity_reason_cn": "基于二分类事实标签和模型预测结果直接计算，不依赖人的感受或语义质量评价"}, {"name_cn": "性能-扰动曲线下面积", "measurement_cn": "在不同扰动比例下计算分类性能指标，并计算性能-扰动曲线下面积", "objectivity_reason_cn": "由可观测标签和模型输出确定，衡量对抗扰动与预测性能之间的客观关系"}]
- Artifact: 具有对抗鲁棒性评估与增强能力的文本分类系统，可作为预测分析应用（如垃圾评论检测、垃圾邮件检测）的通用系统组件 — 设计了对抗鲁棒性评估机制（性能比率、性能-扰动曲线）和对抗鲁棒性增强机制（bagging集成学习、迭代对抗重训练）
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除具体垃圾评论/垃圾邮件数据集和专门界面后，仍保留关于文本分类预测分析系统的可复用设计框架、鲁棒性评估指标、集成学习和对抗重训练机制；这些不是单一案例的解决方案，也不是仅剩算法/求解器
- Decision: 该文的核心目标是通过可运行的ARText系统提升预测分析/文本分类系统在对抗攻击下的客观鲁棒性指标，核心指标为基于事实标签计算的性能比率和性能-扰动曲线下面积，不依赖主观判断；ARText是实际实现并运行的系统，作者设计了鲁棒性评估、集成学习和对抗重训练等可复用机制；文章贡献明确面向预测分析应用/文本分类系统这一软件制品类别，而不仅是算法或领域方案。
- Confidence: 0.97

## Design Principles for Robust Fraud Detection:  The Case of Stock Market Manipulations

- Year/journal: 2021 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00657
- Metric/core status: objective_fixed_factual_labels / objective_improvement_primary
- Metrics: [{"name_cn": "可疑文档分类性能：Accuracy、Precision、Recall、F1", "measurement_cn": "基于10折分层交叉验证和混淆矩阵，通过micro-averaging计算；样本为按SEC公开标准标记的可疑股票推荐和来自可靠新闻源的可靠推荐。", "objectivity_reason_cn": "分类标签依据SEC文档化标准和发布者自我披露的付费广告状态确定，属于外部可核验事实类别；性能指标由确定公式计算，不依赖人对文本质量或价值的语义评判。"}, {"name_cn": "对抗反制下的鲁棒性：随文档操纵程度m变化的Accuracy和F1", "measurement_cn": "模拟欺诈者根据SVM权重将最可疑词汇替换为同义词，逐步增加操纵比例m，评估各分类器性能变化。", "objectivity_reason_cn": "操纵算法和评价指标均按确定性规则运行，衡量的是分类器对欺骗性输入变化的抵御能力，与主观感受、偏好或语义质量判断无关。"}]
- Artifact: 欺诈检测系统（FDS），尤其是基于文本分类的可疑文档检测核心组件；实例为面向股票市场信息操纵的鲁棒分类器。 — 提出并映射设计原则DP1-DP3与设计特征DF1a-DF3b：理论导向的文档转换（信息量、可读性、情绪）、SVM自动分类、组合特征集、集成学习，以及基于SVM决策边界邻近区域的Classifier E鲁棒分类机制。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除股票市场操纵案例、特定数据集和任何专门界面后，仍留下关于FDS应如何利用理论导向语言特征、组合特征和集成学习来抵御欺诈者反制措施的可复用设计知识；不会退化为纯算法、模型或领域方案。
- Decision: 客观指标方面，核心成功指标是可疑文档分类的Accuracy/Precision/Recall/F1及对抗操纵下的鲁棒性，均基于SEC文档化标准等外部事实标签和确定性计算，不依赖主观语义或体验评价；提升这些客观指标是研究问题、设计需求和结论声明的核心目标。软件制品方面，作者不是只提出算法，而是面向FDS类别提出并实例化设计原则和设计特征，实际训练并运行了可集成到FDS的核心分类组件，并将性能改善归因于理论导向语言特征、组合特征和集成学习等制品设计机制。类级贡献方面，贡献对象明确是鲁棒欺诈检测系统这一类软件制品，设计机制可迁移到其他文本型FDS场景，移除当前案例后仍保留可复用的软件设计知识。因此三个模块均通过，应纳入。
- Confidence: 0.97

## HyperCARS: Using Hyperbolic Embeddings for Generating Hierarchical Contextual Situations in Context-Aware Recommender Systems

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2022.0202
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "RMSE和MAE（评分预测误差）", "measurement_cn": "在Frappe和Yelp显式评分数据集上，比较模型预测评分与用户真实评分的均方根误差和平均绝对误差", "objectivity_reason_cn": "真实评分来自用户历史交互记录，预测误差由确定性公式计算，不依赖人的语义或偏好判断"}, {"name_cn": "Hit@K和MRR@K（Top-N推荐排名指标）", "measurement_cn": "基于用户测试集交互，计算推荐列表中命中率与平均倒数排名", "objectivity_reason_cn": "命中与否和排名位置基于用户实际行为记录，计算过程客观可复现"}, {"name_cn": "Silhouette和Dunn Index（聚类质量）", "measurement_cn": "在嵌入空间中计算聚类的紧致度与分离度几何指标", "objectivity_reason_cn": "纯几何计算，不依赖任何主观评价"}, {"name_cn": "决策树/IDS可解释性拟合指标（准确性、覆盖率、AUC、规则复杂度）", "measurement_cn": "用原始上下文变量作为标签，训练决策树或可解释决策集来预测聚类归属，并计算拟合准确率、覆盖率、AUC和规则平均长度", "objectivity_reason_cn": "该度量将可解释性操作化为固定标签上的监督分类性能，不依赖人工评估"}]
- Artifact: 上下文感知推荐系统（Context-Aware Recommender System, CARS） — 作者设计了HyperCARS方法：在双曲空间使用变分自编码器生成上下文潜在嵌入，采用AHC与HDBSCAN进行层次聚类生成层次化上下文情境，并用注意力机制自动选择重要层次；同时将层次化情境路径作为输入，修改了基于NeuMF的上下文感知推荐模型以进行评分预测和Top-N推荐。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除Frappe、Gowalla、Yelp等具体数据集和专门实验后，仍保留关于CARS应如何设计上下文表示组件的可迁移知识：双曲嵌入加层次聚类生成层次化情境，并通过注意力机制选择层次、再与任意推荐算法松散耦合。这些知识与具体数据无关，可指导其他CARS实例的设计。
- Decision: 客观指标方面，论文的核心评价指标为RMSE、MAE、Hit@K、MRR@K等推荐质量和聚类质量指标，以及将可解释性操作化为监督拟合准确率等客观度量，全部核心成功结果均为确定性、可复算的事实性指标；研究问题和贡献声明明确指向提升推荐性能，因此满足完全客观指标要求且为核心目标。软件制品方面，论文明确提出上下文感知推荐系统这一可反复实例化的软件类别，作者实质设计并实现了上下文表示组件（双曲VAE嵌入、层次聚类、注意力机制），并与NeuMF推荐模型集成，在多个真实数据集上运行并评价，客观改进可归因于该组件设计。类级贡献方面，论文对CARS中的上下文建模组件提供了可复用设计知识，并进一步提出适用于更广IS应用的表示框架；移除具体数据集和专门实验后，仍保留可指导同类推荐系统设计的机制与原则。因此严格三个条件均通过。
- Confidence: 0.97

## Augmenting Password Strength Meter Design Using the Elaboration Likelihood Model: Evidence from Randomized Experiments

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1125
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "密码强度增加（diff_strength）", "measurement_cn": "系统记录用户在观察到密码强度计警告前后所输入密码的强度；强度由训练于RockYou数据集的backoff Markov模型计算，对强度值取自然对数后求差值。", "objectivity_reason_cn": "密码强度由预先固定的概率模型确定，不依赖人的感受、语义判断或价值评价；数值可被确定性复算。"}, {"name_cn": "密码修改次数（num_reset）", "measurement_cn": "系统日志记录用户在观察警告信息后立即修改其已输入密码的次数。", "objectivity_reason_cn": "修改行为是系统可审计的事件计数，完全客观可观察。"}, {"name_cn": "是否点击密码安全提示链接（learn_more）", "measurement_cn": "系统记录用户是否点击密码强度计底部的“Tips towards strong passwords”链接。", "objectivity_reason_cn": "点击行为由系统日志记录，属于客观行为事件。"}]
- Artifact: 密码强度计（password strength meter） — 在保持密码强度计算算法一致的前提下，作者设计了三种可嵌入密码强度计界面的说服性警告消息机制：恐惧诉求（攻击者破解所需时间）、同伴比较（密码与其他人相比的排名）、共同纽带（同一密码在其他账户中的流行度），并通过JavaScript/AJAX在用户焦点离开输入框时实时计算与显示。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除具体案例（MTurk样本、亚洲在线论坛）和专用实现界面后，论文仍留下了关于密码强度计应如何设计以实现更有效说服的知识：即通过恐惧诉求、同伴比较、共同纽带等中央路径消息来增强反馈组件，并系统性评价其对实际密码行为的影响。剩余贡献不是仅算法、方程或领域业务方案，而是可复用于其他密码强度计实例的界面反馈设计机制。
- Decision: 这是一篇密码强度计设计研究。核心成功指标是实际生成的密码强度提升（由固定概率模型计算）和用户实际修改密码的次数，均是完全客观可审计的系统日志指标；研究问题和贡献声明均以提升用户密码生成行为为最终目标，主观量表仅用于检验消息加工机制，不构成共同主要终点。作者设计并实质修改了密码强度计的反馈组件，实现了可运行的web-based密码强度计，并通过实验室和30天现场实验验证其效果。贡献面向密码强度计这一可反复实例化的软件制品类别，提出了可复用的设计机制（ELM驱动的三类说服性消息），删除当前案例后仍留下该类软件应如何设计的知识。因此三个模块全部通过。
- Confidence: 0.96

## Augmenting Social Bot Detection with Crowd-Generated Labels

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1136
- Metric/core status: objective_fixed_factual_labels / objective_improvement_primary
- Metrics: [{"name_cn": "社交机器人检测的精确率、召回率、F1、AUC", "measurement_cn": "基于Reddit真实对话数据，以至少10次众包举报的777个账户作为机器人ground truth，由分类器输出账户级别bot/nonbot预测，与ground truth比对计算Precision/Recall/Macro & Micro F1/AUC；另有时间检测模拟和推进型bot测试中的检测百分比。", "objectivity_reason_cn": "机器人与真实用户是外部可核验事实类别，ground truth由多人举报+阈值过滤形成固定事实标签；性能指标按系统日志和预测标签直接计算，不依赖人的感受、偏好或语义质量评价。"}]
- Artifact: 社交机器人检测系统（social bot detection system），将人类众包反应纳入检测特征和流程，可部署于Reddit等长文本社交媒体平台。 — 作者设计了基于人类crowd reaction的检测流程：提取对话中针对bot消息的人类回复（bot topic识别），将回复按sentiment和speech act分类，作为特征与传统的语义和时间相似性特征组合构建账户级bot检测分类器；并通过speech acts对crowd labels的credibility进行加权。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除Reddit案例和专门数据后，论文仍留下关于社交机器人检测系统应如何设计的可复用知识：如何从对话回复中识别crowd labels、如何用speech acts衡量crowd label的credibility、如何将人类认知特征与传统语义/时间特征组合为检测组件，并实例化为可运行的检测系统评价其效果。
- Decision: 文章以提升社交机器人检测性能（Precision/Recall/F1/AUC、时间检测和持续对抗性能）为最终核心目标，这些指标基于外部事实标签（crowd-sourced ground truth + 阈值过滤）客观计算；作者设计并实例化了将crowd reactions、speech acts与传统语义/时间特征融合的social bot detection系统，在Reddit真实数据上运行并评价；贡献明确指向社交机器人检测这一类可复用软件制品的设计知识，而非仅为当前Reddit案例或纯算法方法。因此三个模块全部通过。
- Confidence: 0.95

## Designing Attentive Information Dashboards

- Year/journal: 2022 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00732
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "注意资源分配绩效（attentional resource allocation）", "measurement_cn": "在回访阶段，通过眼动仪记录六个AOI上的注视时长和注视次数，对比第一访问阶段与回访阶段，计算偏离理论平均16.67%的百分数，检验是否更关注先前低关注AOI并减少对先前高关注AOI的注视。", "objectivity_reason_cn": "由眼动仪对注视行为进行确定性测量，不依赖人的主观感受、质量评价或语义判断，属于可审计的行为痕迹。"}, {"name_cn": "注意力转移率（attention shift rate）", "measurement_cn": "用回访阶段用户在六个AOI之间转移的总次数表示，由眼动数据转移矩阵计算。", "objectivity_reason_cn": "转移次数是眼动记录的客观计数，不依赖主观评估，是可直接计算的技术指标。"}, {"name_cn": "注意资源管理绩效（attentional resource management）", "measurement_cn": "在任务结束时，计算六个AOI注视时长和注视次数的标准差；标准差越低表示注意力分布越均匀、管理绩效越好。", "objectivity_reason_cn": "由眼动数据计算的标准差是确定性的统计量，不依赖人类评价或主观感受，属于客观可计算指标。"}]
- Artifact: 专注型信息仪表盘（attentive information dashboard），即能够实时感知用户注意力并提供个性化视觉注意反馈的BI&A信息仪表盘。 — 作者设计了包含仪表盘子系统、眼动追踪子系统和注意感知子系统的系统架构；通过实时眼动数据计算用户的注意资源分配，并在任务后通过反馈生成器将注视时长以时间形式个性化地呈现给用户，从而形成个性化视觉注意反馈（VAF）功能。两个设计原则DP1和DP2分别映射到注意计算和个性化VAF反馈机制。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除当前销售数据实验用例、特定六图仪表盘和专门制作的实验界面后，仍留下“实时眼动监控+个性化VAF反馈”这类仪表盘可复用的功能机制、系统架构和设计原则，因此是关于软件制品类别的设计知识，而非仅剩算法、模型或领域方案。
- Decision: 本文以专注型信息仪表盘为软件制品类别，核心研究问题是设计此类仪表盘以提升信息处理中的注意力管理。全部核心结果均来自眼动仪记录的客观可计算指标：注视时长/次数、AOI间转移次数、六AOI注视分布标准差；没有以满意度、感知价值或语义质量作为主要成功终点。作者不仅提出设计原则和系统架构，还实际开发并运行了集成实时眼动追踪与个性化VAF反馈的软件制品，在92人实验中评估并确认其对客观注意指标的改善。移除具体实验数据集和界面后，仍留下面向该软件类别的可复用设计机制和架构知识，因此三个总条件均满足。
- Confidence: 0.95

## Timely, Granular, and Actionable: Designing a Social Listening Platform for Public Health 3.0

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2023/17381
- Metric/core status: objective_fixed_factual_labels / objective_improvement_primary
- Metrics: [{"name_cn": "相关内容收集的查准率、查全率与F值（数据实验）", "measurement_cn": "基于37,064,742个URL的测试集，使用两个领域专家标注的16,000个训练/测试样本训练gold-standard分类器（PMDS准确率97.2%，Opioid准确率95.3%），对全部URL标注相关/不相关；比较HealthSense与基准方法在收集5M/10M URL时的precision、recall、F-measure及曲线下AUC。", "objectivity_reason_cn": "相关标签由固定本体/实体词典（UMLS、SIDER、drug abuse ontology等）与固定情感极性标注规则判定，专家一致性kappa高达0.95/0.93；评价目标是平台收集是否更快、更全地获取任务相关文档，属于可审计的检索/收集性能。"}, {"name_cn": "下游药品不良事件自动检测的召回率与信号精确率（事件实验）", "measurement_cn": "对PharmCo专家确认的21个真实阳性病例，使用报告比值比(ROR)进行不成比例分析；比较使用HealthSense、GBS、BFS在5M收集阈值下数据的case recall与signal precision。", "objectivity_reason_cn": "真实阳性病例由专业药物安全团队依据内部协议与全文证据判定；检测信号为药-反应二元组共现的统计显著ROR，目标为客观可审计的不良事件检测性能。"}, {"name_cn": "人工分析员不良事件判别准确率（用户实验）", "measurement_cn": "77名PharmCo药物安全团队成员随机分配至HealthSense、GBS、BFS三种数据组，使用相同Tableau仪表盘在3小时内判定20个病例（10真阳性/10假阳性）；五名专家核验书面证据后计算正确判别的precision/recall/F。", "objectivity_reason_cn": "结局变量是分析员对固定病例的二分类判别是否正确，正确性由专家依据明确证据核查；虽然参与者是人，但目标结果是外部事实（是否存在支持不良事件证据）的识别，不是评价主观偏好或感受。"}]
- Artifact: 公共卫生社会聆听平台（social listening platform for public health；类级上属于面向跨渠道在线内容采集与分析的社会聆听系统/情报平台） — 作者设计了HealthSense的三个核心模块：相关性评估模块(RAM)、可信度评估模块(CAM)和渠道景观评估模块(LAM)，并定义了模块间的优先级收集流水线（公式7），包括图传播与GNN耦合、双向关系边增强节点嵌入、多层级图传播等机制；这些机制被转译为平台的功能组件而非仅离线模型。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除具体案例（阿片危机、某种药物）和数据集的命名后，仍留下关于社会聆听平台应如何设计以在跨渠道在线环境中实现及时、相关、可信、完整信息收集的知识——包括活动理论扩展指导的RAM/CAM/LAM模块化机制和优先级收集流程，这些可复用于其他公共卫生及其他及时性社会聆听系统。
- Decision: 客观指标：最终目标为支持公卫3.0的及时、粒细、可操作数据收集，所有核心成功结果均为可审计的收集性能（precision/recall/F/AUC）、自动事件检测性能（recall/precision）和人工判别准确率；标注使用固定本体/实体词典和固定情感规则，非主观语义价值判断。软件制品：HealthSense是明确的社会聆听平台制品，作者实质设计了RAM/CAM/LAM模块及其图传播、GNN、跨渠道导航机制，并在37M URL测试集、数据实验、用户实验和事件实验中实际运行；性能提升可归因于设计机制（消融实验证实）。类级贡献：论文贡献指向社会聆听平台类别的设计元需求与可复用机制，扩展活动理论指导该类软件设计，并在结论中明确可泛化到其他公共卫生问题和数字营销等社会聆听场景；移除当前案例与数据集后仍保留平台设计知识。因此三项均通过。
- Confidence: 0.95

## Designing Conversational Dashboards for Effective Use in Crisis Response

- Year/journal: 2023 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00801
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "透明交互（transparent interaction）", "measurement_cn": "基于系统日志，将用户完成信息查找任务的实际导航步数与预先确定的最短导航步数之比平均化；最短路径按各仪表盘类型分别计算。", "objectivity_reason_cn": "直接由可审计的系统日志、固定编码的最短路径和客观任务结果计算，不依赖用户感受、质量判断或语义评价。"}, {"name_cn": "效率（efficiency）", "measurement_cn": "正确完成信息查找任务所需的平均时间，来自实验系统记录。", "objectivity_reason_cn": "时间是外部可观测的物理量，由系统日志直接测量。"}, {"name_cn": "有效性（effectiveness）", "measurement_cn": "正确解决的客观信息查找任务数量；任务答案对应可核验的疫情事实（州名、日期、病例数等）。", "objectivity_reason_cn": "任务答案和判定依据外部事实标签，不是主观满意度或语义质量评分。"}]
- Artifact: 面向危机响应的会话式仪表盘（conversational dashboard / crisis response dashboard） — 作者设计并实现了自然语言交互能力（DP1）、自然语言与鼠标可选交互（DP2）和会话式引导（DP3），包括仪表盘可视化组件、交互管理组件、NLP组件和会话式引导机制。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除COVID-19案例、具体数据集和COVID-19专用界面后，仍留下关于如何为危机响应仪表盘增加自然语言交互和会话式引导的可复用设计原则、系统架构和组件机制。
- Decision: 最终目标是以自然语言交互和会话式引导提升危机响应仪表盘的透明交互、效率和有效性；这些核心结果均由系统日志、外部任务答案和时间直接测量，不依赖主观评价。作者设计并实际实现了可运行的会话式仪表盘（含可视化、交互管理、NLP和引导组件），并声明面向危机响应仪表盘这一软件制品类别的可推广设计知识。三个模块均通过。
- Confidence: 0.93

## Digital Institutionalization: The Case of E-Prescribing

- Year/journal: 2024 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00845
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "电子处方合规错误数量", "measurement_cn": "通过自动验证规则统计NEF交换合同实施前后各一个月的全部电子处方中违反规则（结构、数据、动态一致性、标识）的错误数量；实施前5,970,737个错误，实施后13,764个错误；含有至少一个错误的处方集从98.6%降至0.9%。", "objectivity_reason_cn": "错误定义为对正式化、自动化验证的交换合同规则的偏离，基于系统日志和XML验证结果，不依赖人的感受或语义质量判断。"}, {"name_cn": "错误状态（拒绝/警告）分类", "measurement_cn": "按错误类型和状态（R拒绝、W警告）统计，衡量错误是否到达药师环节；拒绝型错误从5,843,075降至5,896，警告型错误从127,662降至7,868。", "objectivity_reason_cn": "错误状态由交换合同规则和系统反馈自动判定，是可审计事实。"}]
- Artifact: 数字基础设施中的交换合同/API契约及自动验证组件，服务电子处方等数字制度化实体交换系统 — 设计并实现新的国家电子处方格式（NEF）交换合同：将结构规则和数据规则编码为XML Schema，动态一致性和标识规则通过在线验证实现；废除网关修补机制，引入创建点的自动有效性控制、错误信息和反馈机制，以及模块认证流程。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除瑞典电子处方案例名称、具体数据集和专门界面后，留下的核心贡献是关于如何设计可交换合同、自动验证、错误反馈和制度情境适配等数字基础设施可复用设计知识，而不是仅剩算法或领域方案。
- Decision: 文章以完全客观的电子处方合规错误数作为核心结果指标，作者实质设计并实现了NEF交换合同（XML schema、自动验证、反馈机制）并实际运行，错误大幅减少可归因于该设计；贡献明确指向数字制度系统这一可反复实例化的软件制品类别，并给出可迁移的设计原则；主观合法性讨论和药师调查仅作为补充机制解释，不构成共同主要终点。
- Confidence: 0.92

## Enhancing User Privacy Through Ephemeral Sharing Design: Experimental Evidence from Online Dating

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2021.0379
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "发送照片的匹配请求数（NumPhoto）", "measurement_cn": "来自平台事务数据库的用户行为日志，记录用户发送匹配请求时是否附带照片。", "objectivity_reason_cn": "系统日志记录的实际行为事实，不依赖人的评价或感受。"}, {"name_cn": "含人脸照片的匹配请求数（NumFace）", "measurement_cn": "通过百度AI人脸检测API对用户上传照片进行识别，并辅以人工验证400张照片，精度98.75%。", "objectivity_reason_cn": "人脸是否存在是外部可核实的事实，由自动化API检测，不依赖语义或主观评价。"}, {"name_cn": "匹配数（NumMatch）", "measurement_cn": "接收者接受发送者匹配请求的数量，来自平台交易数据库。", "objectivity_reason_cn": "匹配成功是平台系统确认的客观事件。"}, {"name_cn": "接收者发送的消息数（SumMsgFromReceiver）", "measurement_cn": "匹配后接收者向发送者发送的消息总数，来自第三方云数据仓库的通讯日志。", "objectivity_reason_cn": "消息数量是系统记录的实际行为，不涉及内容质量或主观评价。"}]
- Artifact: 在线约会/匹配平台中的临时分享（ephemeral sharing）功能组件，具体为匹配请求阶段的临时照片上传机制。 — 
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除Summer平台、数据集和专门制作的界面截图后，仍留下“ephemeral sharing作为一种隐私增强设计，通过降低数据收集、传播和身份滥用担忧来增加个人信息披露、从而提升匹配和参与”的类级设计知识；这是关于在线匹配平台等软件制品应如何设计其分享机制的可复用贡献，而非仅剩算法或领域政策。
- Decision: 客观指标方面，论文的最终设计目标和核心贡献是提升完全客观的结果指标：照片披露数、含人脸照片数、匹配数和接收者消息数，均来自系统日志或自动化API；在线实验的隐私担忧和披露意图仅作为机制解释，不构成核心成功终点，因此通过客观指标门。软件制品方面，作者在真实在线约会平台Summer中设计并实际部署了临时照片上传功能，通过UI变化和底层临时性机制构成对平台功能的实质修改，并在现场实验中运行，指标改善可归因于该设计。类级贡献方面，作者明确将ephemeral sharing定位为面向在线匹配平台及其他隐私敏感平台的可复用隐私增强设计，提供了功能机制和交互设计，而非一次性案例方案或算法/方法包装；移除Summer案例和数据后仍保留关于该类软件组件应如何设计的知识。因此三个模块全部通过，strict_include为true。
- Confidence: 0.92

## Automated dynamic approach for detecting ransomware using finite-state machine

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113400
- Metric/core status: objective_fixed_factual_labels / objective_improvement_primary
- Metrics: [{"name_cn": "检测准确率（Accuracy）", "measurement_cn": "在1975个样本（1500个合法应用和475个勒索软件样本）上，将系统预测结果与真实类别标签比对，按混淆矩阵计算正确分类比例。", "objectivity_reason_cn": "勒索软件/合法应用标签是外部可核验的事实标签，不依赖人的感受、语义或价值判断；系统输出为确定性的分类结果，可直接计算。"}, {"name_cn": "真正率/假正率/假负率（TPR/FPR/FNR）", "measurement_cn": "分别由混淆矩阵中的正确识别样本、合法应用误报和勒索软件漏报计算得出，见公式(4)-(7)。", "objectivity_reason_cn": "这些指标完全由系统日志/告警与实际样本类别决定，不涉及主观评价构念。"}]
- Artifact: 勒索软件检测系统（动态行为监控、状态机决策、告警与阻断的Windows安全应用） — 作者设计的系统包含行为分析模块和决策模块：用户文件监控（基于熵的阈值判断）、横向移动跟踪、系统资源监控、持久化检测四个监听组件，以及基于FSM的状态转移决策模块、状态变更监听器和告警/终止进程机制。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除WannaCry、Cerber等具体样本、当前数据集和特定虚拟机后，仍保留关于勒索软件检测系统应如何设计的知识：行为分析模块的监听机制、FSM状态空间与转移条件、基于状态序列的决策告警流程，均可迁移到其他勒索软件检测系统的实例中。
- Decision: 客观指标方面，检测目标标签（勒索软件/合法应用）是外部事实标签，评价指标为准确率、TPR、FPR等确定性客观指标，且提升检测性能是文章的核心目标和贡献。软件制品方面，文章实现并运行了一个实际的勒索软件检测系统，具有明确的软件制品类别（动态行为监控与FSM决策的Windows安全应用），作者具体设计了监听组件、FSM状态转移、告警和阻断机制；性能提升直接归因于该系统的设计机制。类级贡献方面，作者明确面向勒索软件检测这一可反复实例化的软件制品类别，提出了可复用的FSM状态模型和行为监控机制，并在多家族样本上验证其通用性，不是一次性案例软件或纯算法包装。因此三部分均通过。
- Confidence: 0.9

## Interleaved Design for E-Learning: Theory, Design, and Empirical Findings

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2023/17206
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "后测成绩（Posttest score）", "measurement_cn": "现场实验结束后，由在线学习系统按固定正确答案自动评分的英语阅读理解测试成绩，0-100分。", "objectivity_reason_cn": "该指标是对学习者答题正确性的直接观测，评分遵循固定答案和规则，不依赖人的体验、偏好或语义质量判断。"}]
- Artifact: 个性化在线学习系统/电子学习平台，尤其具有自适应学习会话调度功能。 — 作者设计了三个核心软件机制：基于隐马尔可夫模型的薄弱知识点动态检测、基于专家规则与模糊关联规则动态更新的知识地图、以及按“薄弱+相关”准则选择练习的调度引擎，并将相关交错、非交错、无关交错三种会话设计实现于系统中。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除当前英语阅读、中学样本和专门练习册场景后，仍留下关于“如何在个性化电子学习系统中设计相关交错学习会话”的可复用知识：薄弱主题检测—知识地图相关主题建模—调度引擎的功能结构，以及“提高同会话内主题相关性可降低基本加工负荷并促进图式建构”的软件机制。因此，剩下的是电子学习软件制品类别的设计知识，而非只有算法、方程或领域方案。
- Decision: 该文的核心目标是提升电子学习绩效，主要评价指标为后测成绩，属于完全客观、可审计的测试表现；现场实验随机分配并以系统日志和自动评分检验设计效果。作者设计并实例化了一个实际运行的个人化电子学习系统，包含薄弱主题检测、知识地图和调度引擎等可复用软件机制，且设计贡献明确面向电子学习平台类制品，而非仅算法、模型或当前案例解决方案。因此三个模块均通过，strict_include为true。
- Confidence: 0.9

## A new emergency decision support system: the automatic interpretation and contextualisation of events to model a crisis situation in real-time

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113260
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "事件解释时间延迟", "measurement_cn": "从事件到达CEP引擎到完成解释（生成Danger等）的耗时，以秒计，在不同事件频率场景下测量三次。", "objectivity_reason_cn": "由系统处理和日志计时得出，不依赖人的感受或语义评价。"}, {"name_cn": "事件情境化时间延迟", "measurement_cn": "从复杂事件触发到查询Neo4J图数据库并推断出风险所需时间，以秒计。", "objectivity_reason_cn": "是系统处理链路的客观执行时间。"}, {"name_cn": "可视化时间延迟", "measurement_cn": "复杂事件被解读/情境化后显示到共性作战图（COP）上的耗时，以秒计。", "objectivity_reason_cn": "是系统界面更新时间的客观数据。"}, {"name_cn": "事件解释与情境化正确性", "measurement_cn": "在场景中所有事件是否按既定业务规则被正确解释和情境化，依据规则触发结果与预期模型比对。", "objectivity_reason_cn": "正确性是基于预定义规则/阈值的可审计结果，不是人的主观质量评价。"}]
- Artifact: 应急决策支持系统（Emergency Decision Support System），面向危机响应的实时情境建模信息系统 — 
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除Loire洪水案例、具体数据集和专用界面后，仍保留通用危机元模型、事件获取/解释/情境化规则机制、CEP-图数据库交互架构、组件松耦合设计等，这些是关于应急DSS类内其他实例可复用的软件设计知识，而非仅剩算法或领域方案。
- Decision: 客观指标方面：核心评价为事件解释/情境化/可视化时间延迟及按规则核验的处置正确性，均为可确定性观测的系统性能指标，不依赖人的语义或感受；研究问题、贡献声明和评价结构均以实时更新公共操作图并支撑应急决策为核心，客观性能改进是主要目标。软件制品方面：文章明确设计并实现了AIC信息系统，实质设计了CEP-图数据库集成、消息代理、元模型扩充、COP机制等新型功能组件，且该原型在真实洪水场景中运行并测量了效果，并非只停留在算法或概念。类级贡献方面：作者面向应急决策支持系统这一可反复实例化的软件类别，贡献了可复用的架构、元模型和规则机制，实例是其声称类别的体现；删除具体案例后仍保留类级软件设计知识。因此三个模块全部通过。
- Confidence: 0.88

## When Variety Seeking Meets Unexpectedness: Incorporating Variety-Seeking Behaviors into Design of Unexpected Recommender Systems

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2021.0053
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "点击率 (CTR)", "measurement_cn": "线上A/B测试中用户是否点击推荐视频，由平台日志记录并回归估计处理效应", "objectivity_reason_cn": "用户点击行为是外部可核验事实，不依赖任何人的主观评价"}, {"name_cn": "视频观看完成率 (VV)", "measurement_cn": "线上A/B测试中用户是否完整观看推荐视频，由平台日志记录", "objectivity_reason_cn": "观看完成是客观行为事实"}, {"name_cn": "观看时长 (TS)", "measurement_cn": "用户观看推荐视频的秒数，连续变量，由系统时间戳计算", "objectivity_reason_cn": "时间是物理可测量指标，不依赖主观感受"}, {"name_cn": "AUC (离线)", "measurement_cn": "点击预测任务的ROC曲线下面积，基于历史行为标签计算", "objectivity_reason_cn": "预测性能基于外部可核验的点击/观看行为标签"}, {"name_cn": "Hit Rate@10 (离线)", "measurement_cn": "推荐列表前10项中命中用户实际点击/观看物品的比例", "objectivity_reason_cn": "基于行为事实的命中率"}]
- Artifact: 意外推荐系统（unexpected recommender systems），属于推荐系统产品类别下追求意外/新颖推荐的子类，可被多个平台实例化 — 设计了variety-seeking度量子组件（距离函数、时间衰减函数、平稳性汇总）和在效用函数中根据消费者多样性寻求水平自动调整意外性权重的推荐核心组件
- Class contribution: software_artifact_class / implicit_but_well_supported / core_research_contribution
- Counterfactual: 移除具体平台、数据集和专门界面后，仍留下关于意外推荐系统应如何设计的知识：多样性寻求度量组件的选型（距离函数+时间衰减+平稳性）以及效用函数中按用户特性动态调节意外性的机制，而不是只剩某个数据集上的算法或求解器。
- Decision: 客观指标方面，最终设计目标和核心贡献是提升点击率、观看完成率、观看时长等完全客观的业务指标，离线AUC/HR@10也基于行为事实；问卷研究仅作为variety-seeking度量框架的效度验证，不属于最终成功标准，因此通过。软件制品方面，文章明确针对可反复实例化的意外推荐系统类别，实质设计了variety-seeking度量子系统和效用函数调节机制，并在离线数据集及真实视频平台生产环境实例化运行，业务改进归因于该设计机制。类级贡献方面，移除具体平台和数据集后仍留下关于意外推荐系统应如何设计的可复用知识（距离函数+时间衰减+平稳性度量，以及按多样性寻求水平调节意外性），且线上推荐系统是该类别的操作实例。故三个模块均通过。
- Confidence: 0.88

## Using Design-Science Based Gamification to Improve Organizational Security Training and Compliance

- Year/journal: 2020 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2019.1705512
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "实际网络钓鱼响应行为（是否点击钓鱼链接）", "measurement_cn": "由第三方钓鱼测试公司向员工发送伪装成公司密码修改链接的钓鱼邮件；员工点击恶意链接记1，未点击记0，形成二元客观变量。", "objectivity_reason_cn": "该指标反映员工是否实际执行组织安全政策，直接来自系统日志/第三方跟踪记录，不依赖员工自我感受或研究者语义判断。"}, {"name_cn": "各处理组与对照组的被钓鱼比例对比", "measurement_cn": "统计游戏化组、电子邮件组、纯控制组中被钓鱼人数百分比，并计算Z-score差异显著性。", "objectivity_reason_cn": "被钓鱼比例是对外部可审计行为事件的汇总统计，属于完全客观的结果指标。"}]
- Artifact: 游戏化安全培训系统（gamified security training system），即基于SETA的组织安全培训软件。 — 作者设计并实现了一个完整的Web游戏化培训应用，包括用户注册与登录、虚拟头像选择、游戏管理员（gamemaster）、积分系统、怪物奖杯、等级（青铜/银/金）、排行榜、双周测验和反馈提示等游戏化交互机制；同时提出两条设计原则：通过多样化设计元素增强动机，以及通过有意义、有趣的学习过程传递安全知识。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 如果移除法国公司、具体数据集和专门制作的界面，文章仍留下可复用的游戏化安全培训系统设计原则、游戏元素与动机/沉浸/挑战的映射关系，以及如何通过这类系统改进员工实际反钓鱼行为的设计知识；因此不是仅剩算法、求解器或领域方案。
- Decision: 客观指标方面，文章以实际钓鱼点击行为作为最终核心成功指标，由第三方跟踪系统客观记录，属于完全客观可审计结果；虽然模型中包含主观感知变量，但它们是用于解释机制和理论路径的中介构念，最终设计目标是改善实际安全遵从行为。软件制品方面，作者设计、构建并实际运行了一款Web游戏化安全培训系统，包含明确的游戏化交互机制，并通过与电子邮件组和纯控制组的现场实验证明设计机制带来了客观行为改善。类级贡献方面，文章面向‘游戏化安全培训系统/SETA系统’这一可反复实例化的软件类别提出设计原则，系统映射可复用的游戏元素与动机/挑战/沉浸机制，并明确讨论推广到其他组织的路径；当前实现是该类软件的一个运行实例，并非一次性案例包装。综合三项均通过，因此 strict_include=true。
- Confidence: 0.87

## A novel decision support system for optimizing aircraft maintenance check schedule and task allocation

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113545
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "平均未使用飞行小时/飞行循环（FH/FC）", "measurement_cn": "由DSS输出和航空公司维护计划中的检查日期、机队使用参数计算，例如C-check平均FH、平均FC", "objectivity_reason_cn": "飞行小时、飞行循环是航空运营中可审计的物理使用量，不依赖人的感受或语义判断"}, {"name_cn": "维护检查总次数（A/C-check）", "measurement_cn": "从优化后检查计划和航空公司现有计划中直接计数", "objectivity_reason_cn": "检查次数是离散计划事实，可由计划文件核对"}, {"name_cn": "总收益/节省/成本（Gain/Saving/Cost）", "measurement_cn": "按伙伴航空公司给定的每日运营收入、每次A/C-check成本和槽位成本估算", "objectivity_reason_cn": "数值由明确财务参数和计划事实计算得出，可审计"}]
- Artifact: 飞机维修计划优化决策支持系统（Aircraft Maintenance Planning Optimization DSS，简称AMPO DSS） — 
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除案例航空公司、51架机队数据和专门生成的屏幕界面后，仍留下关于‘将维护检查排程、任务分配、班组排班集成到同一DSS’的可复用架构与工作流设计知识；不只是DP排程或bin-packing算法本身。
- Decision: 本文最终设计目标是提升飞机维护计划的可审计客观结果指标（平均FH/FC、检查次数、维护成本、规划耗时），主观专家意见仅用于验证可行性而非主要成功终点；作者设计并运行了一个可执行的AMPO DSS，包含数据库/模型/GUI和集成工作流，评价的是该DSS生成计划的结果；核心贡献指向‘飞机维修计划优化DSS’这一可反复实例化的软件类别，并在结论中明确框架可迁移至类似维护计划系统。因此三项条件均满足，予以纳入。
- Confidence: 0.86

## Effectiveness of Location-Based Advertising and the Impact of Interface Design

- Year/journal: 2020 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2020.1759922
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "优惠券点击率（click rate）", "measurement_cn": "来自真实移动应用系统日志：用户点击某条优惠券即记为一次点击；点击次数除以展示次数得到点击率。", "objectivity_reason_cn": "点击是用户可观测的实际行为，不依赖用户感受、语义判断或研究者主观评价；数据由系统自动记录且可验证。"}]
- Artifact: 基于位置的拉式优惠券应用 / 移动位置广告应用（location-based pull coupon application）的界面设计 — 作者通过2x2现场实验实质性操作了应用界面的两个设计机制：是否显示距离信息，以及按距离排序还是随机排序；还进一步在管理启示中提出距离分桶、排名位次拍卖、筛选按钮等界面设计修改方案。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 若移除当前德国运营商、具体优惠券数据和专门截图，文章仍保留关于‘位置优惠券应用应如何选择距离信息显示和排序机制’的可复用设计知识：距离排序优于随机排序、距离信息的作用取决于排序和用户位置、排名与距离效应的相对大小等，均属于该类应用界面设计的通用机制。
- Decision: 核心结果指标为真实应用产生的点击率，完全客观且是最终设计目标；研究在真实运行的位置优惠券应用上实质操作了界面设计组件（距离信息显示与排序机制），并将点击率改善归因于该界面设计；研究问题和贡献声明明确面向位置广告/位置优惠券应用这一软件制品类别的界面设计，提供了可迁移到同类应用的设计知识。因此三个模块全部通过。
- Confidence: 0.86

## Gamifying knowledge sharing in humanitarian organisations: a design science journey

- Year/journal: 2020 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2020.1718009
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "平台访问次数（KMS参与度）", "measurement_cn": "在真实KMS的A/B现场实验中，通过系统日志统计过去30天每位用户的访问次数；治疗组可看到游戏化个人主页，对照组不可见。", "objectivity_reason_cn": "系统日志直接记录的事实行为，不依赖人的感受、语义理解或价值判断。"}, {"name_cn": "新增资源、评论数和点赞数（知识共享行为）", "measurement_cn": "在实验室实验中统计参与者加入KMS空间的新项目数、对新项目的评论数、对已有项目的点赞数和评论数；另有专家质量评分作为辅助鲁棒性检查。", "objectivity_reason_cn": "这些是平台中可审计的量化行为计数；专家质量评分不属于核心成功终点，仅用于确认数量增长不是以明显低质量为代价。"}]
- Artifact: 知识管理系统（KMS）中的游戏化反馈组件，包括系统内的个人主页反馈组件和系统外的环境可视化组件（虚拟水族箱）。 — 作者在Graasp KMS中设计与实现了游戏化个人主页：六维贡献指标（Commenter、Influencer、Contributor、Collaborator、Visitor、Sharer）、百分位等级、总体Graasper分数，以及对应的可视化与反馈机制；同时设计并实现了虚拟水族箱，根据用户在KMS空间中的活动动态改变鱼的大小、鱼代表用户、岩石代表项目、水草代表评论，作为KMS外部的环境反馈。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除MSF、Graasp、Tiburon/海地等具体案例和数据后，仍保留“在KMS中通过个人游戏化反馈和周围环境反馈提高用户参与和知识共享行为”的可复用设计知识；这不是仅剩算法、方程、求解器或领域政策，而是关于某类软件组件应如何设计的机制和功能结构。
- Decision: 文章最终设计目标是以游戏化反馈提升人道组织KMS中的实际知识共享行为，核心评价指标为访问次数、新增资源/评论/点赞等系统日志客观行为；主观感知、美学问卷和访谈仅用于解释机制或辅助验证，不构成最终成功标准。软件方面，作者在Graasp KMS中设计并实际实现了个人主页游戏化评分反馈和虚拟水族箱环境反馈组件，并在真实MSF平台A/B测试和实验室实验中证明其提升参与度。贡献面向KMS游戏化设计这一软件制品类别，包含可复用的功能维度、反馈机制和概念模型，而非仅算法、包装或单一案例。三个部分均满足，故纳入。
- Confidence: 0.85

## <scp>Context‐aware</scp> user profiles to improve media synchronicity for individuals with severe motor disabilities

- Year/journal: 2022 / Information Systems Journal
- DOI: 10.1111/isj.12337
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "沟通任务完成时间", "measurement_cn": "在原型AAC系统上，参与者分别使用有/无上下文感知用户画像的版本完成三种医疗/舒适需求沟通任务，记录完成时间并计算改善百分比。", "objectivity_reason_cn": "完成时间由客观计时产生，不依赖人的感受或语义评价，可直接观察和验证。"}, {"name_cn": "选择错误数和扫描越界错误数", "measurement_cn": "系统记录参与者在任务中的错误选择次数和错过滚动选项的次数。", "objectivity_reason_cn": "错误计数来自系统日志或可核验的操作记录，属于客观可审计事实。"}]
- Artifact: AAC系统（增强与替代沟通系统），具体为面向严重运动障碍个体的辅助沟通软件原型。 — 作者设计了上下文感知用户画像、访客画像、医疗/舒适领域本体和替代符号集，通过画像过滤词/短语选择空间，采用扫描界面和键盘空格键选择，并比较有/无上下文感知用户画像两种配置。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除Todd个案、医疗舒适本体数据和专门制作的医学沟通界面后，仍会留下关于AAC系统设计的可复用知识：上下文感知用户画像、访客画像、替代符号集，以及四条设计原则。这些是软件系统的功能/交互/反馈设计机制，而不只是算法、方程或领域方案。
- Decision: 文章以设计科学研究回答如何设计AAC系统，核心目标是通过软件制品提升严重运动障碍个体的沟通传输速度和准确性；评价在实际运行的原型上进行，记录客观任务完成时间和错误数，改善效果可归因于上下文感知用户画像这一设计机制。制品类别为AAC系统，作者明确提出面向该类系统的设计原则，删除Todd个案和专门医学界面后仍保留可复用的AAC软件设计知识。因此三个模块均通过。感知速度量表为补充主观证据，不构成混合核心终点。
- Confidence: 0.82

## Automated discovery of business process simulation models from event logs

- Year/journal: 2020 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113284
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "Event Log Similarity (ELS) / Business Process Trace Distance (BPTD)", "measurement_cn": "将模拟日志与真实事件日志的轨迹进行最优配对，计算带时间信息的编辑距离（BPTD），再求和得到ELS；ELS越小表示模拟模型与真实过程行为越接近。", "objectivity_reason_cn": "该指标完全由事件日志中的活动标签、处理时间、等待时间和并发关系经确定性算法计算得出，不依赖人的感受、语义判断或价值评价。"}]
- Artifact: 业务流程仿真模型自动发现工具（Business Process Simulation Model Discovery Tool），即从事件日志自动生成可执行BPS模型的软件工具。 — 作者设计了Simod的整体流水线：控制流发现、日志修复（removal/replacement/alignment）、事件日志回放、到达/处理时间分布拟合、分支概率发现、资源池发现、模型组装、BPTD准确度度量以及基于TPE的超参数优化。
- Class contribution: software_artifact_class / implicit_but_well_supported / core_research_contribution
- Counterfactual: 移除P2P、ACR、MP三个具体日志和案例后，剩余贡献仍然是BPS模型自动发现工具的设计知识：控制流发现与日志修复、回放算法、分布拟合、资源池发现、BPTD/ELS精度度量、TPE超参数优化搜索空间等机制，均属于该类软件工具的可复用设计。
- Decision: 核心目标是提升BPS模型相对于真实事件日志的客观相似度（ELS/BPTD），无主观构念作为核心结果；Simod是作者实际设计、实现并运行的软件工具，而非仅算法或实验脚本；贡献指向一类可复用的BPS模型自动发现工具，且在多个领域日志上实例化验证。因此三个模块全部通过。
- Confidence: 0.82

## Ingredients for successful badges: evidence from a field experiment in bike commuting

- Year/journal: 2020 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2020.1808539
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "每周骑行天数 (RidingDays)", "measurement_cn": "大学自行车通勤项目RFID站点自动记录每位注册用户的每日自行车扫描，按周统计骑行天数；七周内共得到13,825个用户-周观测。", "objectivity_reason_cn": "该指标来自RFID系统日志，是可审计的物理事实记录，不依赖人的感受、语义评价或价值判断。"}]
- Artifact: 基于徽章的游戏化信息系统（badge-based gamified information system）中的徽章组件，具体是可嵌入通勤、健康、学习等目标系统的徽章奖励/标识/完成逻辑设计。 — 在既有自行车通勤信息系统中新增并变造徽章组件：奖励（是否附带Facebook分享链接）、标识（环保框架vs自我成就框架）、完成逻辑（固定目标vs相对目标），并同步改造每周邮件简报和门户仪表盘的徽章展示。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除大学自行车通勤案例、RFID数据集和专门定制的邮件/仪表盘后，仍留下关于徽章应如何设计的可复用知识：奖励中增加社交分享选项可提高目标行为，完成逻辑采用相对目标仅对高频用户有正向作用，环保/自我成就两种标识框架未产生差异。这些知识适用于其他徽章式游戏化信息系统，而非仅针对当前案例的算法或业务方案。
- Decision: 核心结果指标是完全客观的RFID系统记录骑行天数，研究目标明确为检验不同徽章设计对骑行行为的影响；作者在既有通勤信息系统中实际设计、修改并运行了徽章组件（分享奖励、标识框架、完成逻辑），并将这些设计作为核心研究贡献；贡献对象是徽章式游戏化信息系统这一可反复实例化的软件制品类别，而非仅针对单车案例、算法或领域机制。因此三项条件均通过。
- Confidence: 0.82

## Responsible cognitive digital clones as decision-makers: a design science research study

- Year/journal: 2023 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2022.2073278
- Metric/core status: objective_fixed_factual_labels / objective_improvement_primary
- Metrics: [{"name_cn": "决策一致性/准确率 F1-score", "measurement_cn": "将决策视为二分类任务，比较克隆/排名输出与捐赠者或官方记录中的“增加/不增加”等决策标签，基于混淆矩阵计算F1；危机管理场景以订单及时性和最终状态计算F1。", "objectivity_reason_cn": "标签来自可审计的行政记录、排名数据和订单状态，不依赖用户主观感受或语义质量评价；F1的计算公式是确定性的。"}, {"name_cn": "决策时间节省（人力工时节省）", "measurement_cn": "招聘委员会场景中，每位候选人审批时间由10分钟降至1分钟，乘以委员会人数、候选人数和会议频次，得到全校每年节省的工时数。", "objectivity_reason_cn": "时间、人数和候选数均可直接观测和计算，不依赖人类体验或价值判断。"}]
- Artifact: 认知数字克隆代理/决策者代理软件（Pi-Mind agent / cognitive digital clone as decision-maker） — 设计了DP0-DP3设计原则、T|C-SGAN对抗训练架构、个人价值系统PSV、决策本体、语义知识库，以及TRUST Portal中的代理决策流程与工具。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除NURE、NATO、TRUST具体案例、数据集和专门界面后，仍剩下关于认知数字克隆代理的设计原则、训练环境结构、个人决策本体/PSV和T|C-SGAN组件机制等类级软件设计知识；不会退化为只与某个数据集或领域绑定的算法、方程或求解器。
- Decision: 文章以设计科学方法构建并实际部署Pi-Mind认知克隆代理，核心目标是通过克隆实现负责任、韧性和泛在的决策，提升决策准确性和节省决策时间；评价主要使用F1、工时节省、流程数量等可观测/可计算指标，未以主观满意度或语义质量评价作为核心成功终点。Pi-Mind agent是明确可反复实例化的软件制品类别，作者设计了DP0-DP3、PSV、决策本体、T|C-SGAN等可复用机制，并在NURE/TRUST和NATO场景中实际运行验证；移除具体案例后仍留下类级软件设计知识。因此客观指标、真实软件制品和类级贡献三个模块均通过。
- Confidence: 0.82

## Smart Markets for Real-Time Allocation of Multiproduct Resources: The Case of Shared Electric Vehicles

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2022.0204
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "总利润（gross profit）", "measurement_cn": "基于Car2Go真实租赁数据和三个市场（斯图加特、阿姆斯特丹、圣迭戈）的调频市场电价数据，在仿真中计算租赁收入、VPP收入、机会成本和惩罚后的净收益。", "objectivity_reason_cn": "收入、价格、成本和惩罚均由真实市场数据和系统日志决定，不依赖人的感受、偏好或语义评价。"}, {"name_cn": "车辆利用率（utilization）", "measurement_cn": "以车辆处于生产性服务（租赁、上调和下调频）与闲置时间的比例进行衡量，统计各市场已承诺和已清算数量。", "objectivity_reason_cn": "利用率由系统分配记录和市场清算结果直接计算，是可审计的执行事实。"}, {"name_cn": "决策准确率（confusion matrix）", "measurement_cn": "将FleetPower在租赁市场和VPP市场的资源承诺决策与完美预知下的最优决策进行比较，形成混淆矩阵和准确率。", "objectivity_reason_cn": "准确率基于明确的资源分配状态和利润结果计算，不涉及人类质量或语义判断。"}]
- Artifact: 面向实时多产品资源分配的智能市场决策支持系统（DSS），可实例化为SEV车队运营者的资源分配决策工具。 — 设计了FleetPower的五阶段DSS架构：（1）市场和运营数据采集（ML预测需求、价格和可用能量）；（2）资源规划（按预期利润排序市场）；（3）投标（向调频市场和租赁市场提交数量和价格）；（4）资源重规划（基于实际可用量和惩罚处理缺口）；（5）执行。这些机制超出单纯预测模型，构成可运行DSS的功能流程。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除Car2Go、三座城市的具体数据集和专门界面后，论文仍留下'通过智能市场实时分配多产品资源'的五阶段DSS设计蓝图：包括需求/价格/可用量预测、市场吸引力排序、迭代投标、资源重规划和执行流程。这些是可进入其他多产品资源分配DSS实例的功能结构和机制，而非仅剩预测算法、优化方程或市场机制。
- Decision: 文章核心目标是改进SEV车队在租赁市场和电力调频市场之间的实时资源分配，以提升利润和利用率；这些核心结果均由真实数据和仿真计算决定，完全客观。文中存在可识别的软件制品类别——实时多产品资源分配DSS（FleetPower），作者实质设计了五阶段运行机制，并通过离散事件仿真实际运行和评价该DSS。贡献声明明确指向可复用的DSS蓝图，适用于多产品资源分配类软件，而非仅限当前车队、单一数据集或纯算法。因此三个模块均通过。
- Confidence: 0.82

## Automating in High-Expertise, Low-Label Environments: Evidence-Based Medicine by Expert-Augmented Few-Shot Learning

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2024/18573
- Metric/core status: objective_fixed_factual_labels / objective_improvement_primary
- Metrics: [{"name_cn": "句子分类的P@N、R@N、F1@3、PRC", "measurement_cn": "在WD、COVID、EBM-NLP测试集上，以SR专家标注或公开标注的PICO句子为真值，计算模型推荐句子与真值匹配的precision/recall/F1/PRC", "objectivity_reason_cn": "PICO元素对应研究设计、样本量、国家、干预药物/剂量等可核实事实；专家标注用于记录这些外部事实，不评价质量或偏好"}, {"name_cn": "序列标注（PICO文本片段抽取）的F1和BERTScore", "measurement_cn": "在检索到的句子中，将预测片段与专家标注片段按词重叠和BERT语义相似度计算F1/PRC", "objectivity_reason_cn": "片段是PICO事实在文本中的具体位置，虽需语义识别，但目标是客观实体信息而非主观感受或价值判断"}, {"name_cn": "SR项目时间/成本节约", "measurement_cn": "以WD项目为案例估算四种方案（FastSR、ProtoNet、CNN、人工）在标注、训练、验证和纠错上的时间，计算总时间及成本减少", "objectivity_reason_cn": "时间是可直接审计的客观指标，成本按固定时薪估算"}]
- Artifact: 系统性文献综述自动化/辅助数据抽取系统（systematic review automation/data extraction systems） — 设计FastSR少样本深度学习框架：语义表示（BioBERT+CNN）、全局上下文表示（基于PubMed预训练的层次分类器+指针网络）、基于注意力的PICO片段表示、片段关注查询表示、联合学习与跨任务正则化；还提出FastSR增强的SR人工-机器协同流程
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除WD/COVID/EBM-NLP特定数据集和当前案例后，仍保留面向SR自动化系统的设计需求与组件映射（上下文表示、语义片段注意力、联合学习），可迁移到其他SR系统；不是仅剩通用算法或优化方法
- Decision: 文章核心目标是设计并在实际数据和工作流中运行FastSR组件，以客观的PICO句子/片段抽取准确率（F1、PRC）和SR时间节约作为主要成功指标；专家标注对应可核实事实，定性访谈仅补充适用性。FastSR是SR自动化数据抽取系统的核心组件，作者从任务复杂度推导设计需求并映射到模块化机制，且验证其可迁移到多个疾病场景，属于类级软件制品贡献。
- Confidence: 0.8

## Providing more regular road signs infrastructure updates for connected driving: A crowdsourced approach with clustering and confidence level

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113443
- Metric/core status: objective_fixed_factual_labels / objective_improvement_primary
- Metrics: [{"name_cn": "道路标志合并结果的精确率/召回率/假阳性率（相对实地真值）", "measurement_cn": "采集真实路段数据，将合并算法输出的道路标志与人工实地收集的真实标志在20米距离和45°航向差内匹配，构建混淆矩阵并计算precision/recall等", "objectivity_reason_cn": "道路标志是否真实存在及其物理位置是外部可审计事实；通过真值位置与固定匹配规则确定，不依赖人的感受、语义评价或价值判断"}, {"name_cn": "模拟融合系统相对仅摄像头系统的真阳性率/假阴性率/假阳性率", "measurement_cn": "对比“摄像头单独检测”与“合并道路标志+摄像头”两类系统在同一真实路段上的TP、FN、FP，计算TPR、FNR、FPR", "objectivity_reason_cn": "检测事件和道路标志真实存在均为可观测事实，按固定匹配规则计数，结果客观"}]
- Artifact: 基于众包车辆传感器数据的道路标志数字地图更新平台/系统（road-sign map update platform from crowdsourced vehicle sensor data；属于connected driving与ITS中的地图更新软件类别） — 作者设计了云平台处理流水线：滑动时空查询、tile地理分区、带heading距离的meanshift聚类、基于车辆轨迹的负观测推导、基于贝叶斯推断和指数衰变的置信水平计算，以及摄像头+合并标志的融合规则
- Class contribution: software_artifact_class / implicit_but_well_supported / core_research_contribution
- Counterfactual: 移除Regensburg/Continental具体案例后，仍保留：面向车联网众包传感器数据的云平台架构、滑动窗口查询、tile并行化、带heading的聚类、负观测推导、贝叶斯置信水平与融合规则等知识；这些不是仅剩算法方程或单一案例方案，而是可进入其他道路标志/道路对象更新系统实例的设计机制
- Decision: 客观指标方面，道路标志存在性及其位置是外部事实，实验以精确率、召回率、假阳性率等客观结果作为核心成功终点；软件制品方面，存在可识别的“道路标志众包地图更新系统/平台”类别，作者实质设计了云平台中的聚类、负观测、置信水平、融合规则等组件，并在AWS/Spark环境和Continental真实数据上实际运行；类级贡献方面，移除具体案例后留下的不是单纯算法或领域方案，而是可复用于同类道路标志/道路对象更新系统的平台流水线和组件机制。三个模块均通过，因此strict_include为true。
- Confidence: 0.74

## Feedback at scale: designing for accurate and timely practical digital skills evaluation

- Year/journal: 2020 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2019.1701955
- Metric/core status: objective_fixed_factual_labels / objective_improvement_primary
- Metrics: [{"name_cn": "评分速度（可扩展性）", "measurement_cn": "自动评分引擎与人工评分者完成同一批Excel/Word考试文件的平均处理时间；使用秒表/日志记录", "objectivity_reason_cn": "时间是可外部观测、完全客观的技术指标，不依赖人类感受或语义判断"}, {"name_cn": "评分有效性与可靠性（误报/漏报错误率）", "measurement_cn": "以专家建立的任务级ground truth为基准，统计评分引擎对每个任务的正确/错误评价、误报与漏报数量及百分比；另统计评分不一致数量", "objectivity_reason_cn": "任务完成与否是对Word/Excel文件内容的可核验外部事实，按固定评分键和XML检查规则判定，不评价主观质量或满意度"}, {"name_cn": "学习者投入度（作业完成率/反馈获取率）", "measurement_cn": "系统日志记录提交作业或分块的学生人数占选课人数比例，以及分块完成数", "objectivity_reason_cn": "提交和完成行为由系统日志客观记录，属于可审计的行为事实"}]
- Artifact: 面向大规模数字技能掌握的表现反馈系统（含学习者应用和自动评分引擎的社会技术制品） — 
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除具体课程、Excel/Word数据集和专门界面后，仍然留下关于'大规模数字技能反馈系统应如何设计'的可复用知识：如作业分块以保证管理性、结构化起始文件以减少复合错误、即时反馈循环以提升投入度、基于XML的评分引擎以兼顾真实性和可扩展性，以及教学优先、作业设计与自动测量协同的设计机制。
- Decision: 文章以完全客观可测的评分速度、误报/漏报率和学习者完成率为核心评价指标，目标是在大规模条件下提供准确及时的数字技能反馈；作者实际设计、实现并运行了学习者应用和自定义Python评分引擎，且部署至310名用户；贡献明确落在'大规模数字技能反馈系统'这一软件制品类别，提出了可复用的元需求、设计原则和具体设计特征。因此三个模块均通过。
- Confidence: 0.68

## Augmented Reality at Work: Attention Management and Its Impact on Work Performance

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2025/18944
- Metric/core status: objective_fixed_factual_labels / objective_improvement_primary
- Metrics: [{"name_cn": "视觉绩效", "measurement_cn": "通过第一视角视频中YOLO目标检测识别关键飞机部件，若部件出现在中央视野区域并持续至少2秒则编码为1，最终汇总按规定检查的关键部件数量。", "objectivity_reason_cn": "检查的对象是外部物理部件是否出现在视频中央视野且持续时间达到规定阈值，不依赖人的感受、语义或价值判断。"}, {"name_cn": "动作绩效", "measurement_cn": "对第三人称视角视频进行人工编码，对需要下蹲等标准动作的步骤判断是否执行规定动作（0/1编码），最终汇总标准动作数量。", "objectivity_reason_cn": "动作是否执行是外部可观察的行为事实，编码员仅执行固定的行为判定规则，不进行质量或语义评价。"}, {"name_cn": "工作专注度", "measurement_cn": "根据第一视角视频人工编码，计算每个步骤中实际检查飞机部件或查看指导信息的时间占步骤总时间的比例。", "objectivity_reason_cn": "时间比例基于视频中的客观时间记录和固定编码规则，不涉及主观感受或偏好。"}]
- Artifact: AR辅助检查/维护作业卡系统：在工业维护场景中通过近眼AR显示或移动屏幕向操作员提供分步骤操作指令与部件信息的信息系统类别。 — 作者设计了AR显示的信息呈现机制：步骤标题与具体指导信息采用2秒延迟的分屏显示；信息置于使用者周边视野（约10-30度）的显示位置；依据信息依赖性和复杂性设计了文本与图像组合提示；同时整合了视觉记录和手机滑屏逐步操作交互。
- Class contribution: software_artifact_class / implicit_but_well_supported / core_research_contribution
- Counterfactual: 去掉航空维修案例和特定AR眼镜后，仍可提炼出供同类AR任务指引系统使用的设计知识：将高度依赖物理情境且复杂度较低的信息放置于周边视野可减少注意力切换、提升绩效；信息复杂度高时周边视觉处理受限，应避免将复杂信息大量投射到AR显示中。这是关于AR信息系统如何设计的信息呈现机制，而非单纯的算法或领域方案。
- Decision: 客观指标（视觉绩效、动作绩效）均基于外部可观察行为事实，工作绩效提升是研究的核心因变量和贡献目标；作者设计并实际运行了AR显示/移动交互组件，现场实验证据充分；可复用设计知识面向AR辅助作业信息系统这一软件类别，而非单纯算法或领域方案。因此三个模块均通过，strict_include为true。
- Confidence: 0.65
