# Unified strict matches

Completed: 52 / 52
Retained: 11

## Augmenting Social Bot Detection with Crowd-Generated Labels

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1136
- Metric/core status: objective_fixed_factual_labels / objective_improvement_primary
- Metrics: [{"name_cn": "社交机器人检测的分类性能（精确率、召回率、宏F1、微F1、AUC）", "measurement_cn": "以2016–2018年Reddit真实对话数据为测试集，将777个被社区列表报告的社交机器人账户与195,291个非机器人账户对比，分别使用仅传统特征（语义、时间相似性）和加入人群反应特征的增强模型，采用多种分类器（随机森林等）计算精确率、召回率、F1和AUC；另在2019年后新机器人子集上测试持续有效性。", "objectivity_reason_cn": "机器人/非机器人标签来自社区多人报告计数（≥10次报告）的外部公开真实事实，检测性能指标由系统预测与既定事实标签比对得出，不依赖任何人对质量、感受或偏好的评价。"}, {"name_cn": "检测速度（达到固定消息量或人群标签数时检测到的机器人比例）", "measurement_cn": "将测试集中机器人按发帖10/25/50条消息时的检测率，以及按累计人群标签1/5/10条时的检测率，比较传统模型与增强模型。", "objectivity_reason_cn": "由系统日志和消息/标签计数决定，无主观判断成分。"}]
- Artifact: 社交机器人检测系统（social bot detection system） — 
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除Reddit这一案例名称和具体数据集后，仍留下‘检测系统可利用用户对疑似机器人的回复（人群自然标签）来提高机器人检测性能’这一功能设计知识，包括：如何从对话级回复中提取bot topic、情感和speech act特征以加权不同人群标签；该类设计知识可直接移植到其他长文本社交媒体或需要检测算法生成内容的平台。若只移除案例，剩下的不是纯算法、方程或领域方案，而是明确的检测系统组件模式。
- Decision: 客观指标方面：核心最终目标是提高社交机器人检测性能，指标为检测精确率/召回率/F1/AUC和检测速度，机器人标签为社区报告的外部公开事实（≥10次报告），非主观构念；全文虽然存在人类标注训练topic/sentiment/speech act分类器，但这些标注是训练辅助特征，不是最终成功指标，核心指标完全客观。软件制品方面：论文明确构建了社交机器人检测系统，而非仅离线算法；系统由实际运行的BERT分类组件、回复特征提取、分类器集成和检测模拟组成，在真实Reddit数据上实例化。类级贡献方面：作者贡献明确指向社交机器人检测系统这一软件制品类别，提出可复用的‘利用人群自然标签+言语行为加权’的设计机制，并在Reddit实例上验证；移除案例后仍有检测系统设计知识，而不只是算法或领域机制。因此通过三项总标准。
- Confidence: 0.97

## Augmenting Password Strength Meter Design Using the Elaboration Likelihood Model: Evidence from Randomized Experiments

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1125
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "密码强度增加量（diff_strength）", "measurement_cn": "使用backoff Markov模型（基于RockYou数据集训练）计算用户观察警告消息前后的密码强度，取自然对数后相减；模型输出概率决定强度，系统在用户输入时实时计算。", "objectivity_reason_cn": "密码强度值由公开密码数据集训练的统计模型计算，不依赖人的主观评价或语义判断，是确定性的技术度量。"}, {"name_cn": "密码修改次数（num_reset）", "measurement_cn": "系统日志记录用户在观察到密码强度计警告消息后立即修改密码的次数。", "objectivity_reason_cn": "修改行为由系统日志客观记录，属于外部可核验的操作事实。"}]
- Artifact: 密码强度计（password strength meter） — 在保持底层强度计算算法不变的前提下，设计了三种基于ELM中心路径的警告消息界面：恐惧诉求（预计破解时间）、同伴比较（密码在常用密码中的排名）、共同纽带（预计相同密码的账户数），并实现了相应的消息计算与展示逻辑。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除具体论坛、数据集或定制界面后，仍保留关于‘密码强度计应如何设计’的可复用知识：通过添加理论引导的警告消息（时间、排名、概率）可以增强强度计促使用户改进密码行为的能力；实验实例只是这些设计原则的具体运行示范。
- Decision: 客观指标方面，核心成功结果（密码强度变化、密码修改次数）均由统计模型和系统日志客观确定，不依赖人的主观评价；主观调查仅用于机制检验，不构成最终设计目标。软件制品方面，作者设计并实际运行了密码强度计组件，在三个实验中实例化，并通过随机对照试验将客观行为改善归因于界面消息设计。类级贡献方面，研究明确面向密码强度计这一类可反复实例化的软件制品，提出了可复用的设计原则（ELM中心路径警告消息），并展示其在实验室和现场实例上的有效性；即使移除具体案例，仍保留关于该类软件应如何设计的知识。因此三项条件均满足，应纳入。
- Confidence: 0.95

## HyperCARS: Using Hyperbolic Embeddings for Generating Hierarchical Contextual Situations in Context-Aware Recommender Systems

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2022.0202
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "RMSE", "measurement_cn": "预测评分与真实评分的均方根误差，基于用户历史评分数据计算。", "objectivity_reason_cn": "评分是外部可观测的用户行为数据，误差计算不依赖主观评判。"}, {"name_cn": "MAE", "measurement_cn": "预测评分与真实评分的平均绝对误差，基于用户历史评分数据计算。", "objectivity_reason_cn": "评分是外部事实，误差计算客观。"}, {"name_cn": "Hit@K", "measurement_cn": "推荐列表中命中用户实际交互项目的比例，基于真实交互记录计算。", "objectivity_reason_cn": "命中与否基于实际交互事实，不涉及主观判断。"}, {"name_cn": "MRR@K", "measurement_cn": "推荐列表中第一个真实交互项目的倒数排名均值，基于真实交互记录计算。", "objectivity_reason_cn": "排名由客观交互事实决定，计算确定。"}]
- Artifact: 上下文感知推荐系统（CARS） — 设计了双曲空间中的VAE嵌入、层次聚类（AHC/HDBSCAN）生成层次化上下文情境路径，并修改了基于NeuMF的推荐模型以松耦合方式集成这些情境。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除Frappe/Gowalla/Yelp等具体数据集后，仍保留'如何在CARS中使用双曲空间表示层次化上下文情境并提供更优推荐'的设计知识，而非仅剩算法或方程。
- Decision: 文章以标准推荐指标（RMSE、MAE、Hit@K、MRR@K）作为最终设计目标和核心贡献，指标完全客观；作者设计并运行了HyperCARS组件，包含双曲嵌入、层次聚类和松耦合推荐集成，属性可归因于该设计；贡献明确指向上下文感知推荐系统这一软件制品类别，并提出了可复用的机制，符合类级贡献要求。校准案例明确将HyperCARS列为应通过，因此判定包含。
- Confidence: 0.95

## Assessing and Enhancing Adversarial Robustness of Predictive Analytics: An Empirically Tested Design Framework

- Year/journal: 2022 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2022.2063549
- Metric/core status: objective_fixed_factual_labels / objective_improvement_primary
- Metrics: [{"name_cn": "对抗鲁棒性分类性能（accuracy、precision、recall、F1、ROC）", "measurement_cn": "在spam review和spam email测试集上，用DeepWordBug生成对抗样本，比较模型在非对抗测试集和混合对抗测试集上的性能，并计算performance ratio和performance-perturbation curve下的面积。", "objectivity_reason_cn": "spam/非spam是外部可核验的事实类别；预测结果、扰动范围和鲁棒性指标均由确定性算法和系统日志计算，不依赖用户感受、偏好或语义质量评价。"}, {"name_cn": "performance ratio鲁棒性指标", "measurement_cn": "将对抗样本影响下的分类性能与非对抗基线性能相除，得到R_A、R_P、R_R、R_F、R_ROC等比值。", "objectivity_reason_cn": "该指标由客观的分类性能数值直接计算，反映对抗扰动造成的可量化性能损失。"}, {"name_cn": "performance-perturbation curve鲁棒性指标", "measurement_cn": "在不同扰动范围（0到1）下测量模型分类性能，计算accuracy/precision/recall/F1/ROC扰动曲线下面积，如A/P AUC、R/P AUC等。", "objectivity_reason_cn": "扰动范围是明确可量化的输入修改程度，模型性能是确定性的分类结果统计，不包含主观评价。"}]
- Artifact: 具备对抗鲁棒性的预测分析/文本分类系统（robust text classification system for predictive analytics） — ARText系统实现了两个meta-requirement：对抗鲁棒性评估组件（性能比、性能-扰动曲线）和对抗鲁棒性增强组件（bagging集成学习和迭代对抗重训练）。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除spam review/spam email案例和具体数据集后，仍留下关于如何设计具备对抗鲁棒性的预测分析/文本分类系统的可复用知识：鲁棒性评估措施、性能-扰动权衡测度、集成学习与对抗重训练的防御机制。这些不是仅剩的算法或领域方案，而是可进入同类软件系统的设计组件。
- Decision: 三个模块均通过：核心目标是提升预测分析应用对对抗攻击的鲁棒性，并以分类性能比、性能-扰动曲线等完全客观指标作为主要成功标准；作者设计、实现并运行了ARText鲁棒文本分类系统，将鲁棒性评估与增强机制实例化为系统组件；贡献声明明确指出这是面向预测分析/文本分类系统类别的设计框架，而非仅算法或单一案例方案。
- Confidence: 0.94

## Design Principles for Robust Fraud Detection:  The Case of Stock Market Manipulations

- Year/journal: 2021 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00657
- Metric/core status: objective_fixed_factual_labels / objective_improvement_primary
- Metrics: [{"name_cn": "分类准确性、精确率、召回率、F1", "measurement_cn": "10折交叉验证和模拟攻击场景中，将文档分类为可疑或非可疑推荐，并依据与SEC标准匹配的真实标签计算accuracy、precision、recall、F1", "objectivity_reason_cn": "分类标签是否“可疑推荐”由可披露的SEC书面标准确定，并由领域专家和市场监管机构审查；文档操纵的模拟也基于SVM权重、WordNet/SentiWordNet等确定性改写规则，不依赖人类对质量或意义的语义评价"}, {"name_cn": "鲁棒性：不同操纵程度m下的分类性能", "measurement_cn": "按照给定攻击算法替换最高权重可疑词，逐步提高m值，重新计算accuracy和F1等指标，比较各分类器性能", "objectivity_reason_cn": "操纵过程、替换词选择和性能指标均按固定算法和外部门知识资源计算，不涉及主观感受或语义好坏判断"}]
- Artifact: 欺诈检测系统（Fraud Detection System, FDS）中的文档分类组件/分类器 — 作者设计了三个设计原则和五个设计特征，具体化为多个SVM分类器（A: bag-of-words；B: 理论驱动的语言特征；C: 组合特征集；D: 基本集成；E: 基于超平面边界的鲁棒集成），以及攻击模拟验证流程；这些机制被设置为FDS的核心组件。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除当前股票市场操纵案例、特定数据集和专门界面后，仍保留面向欺诈检测系统的设计知识：理论指导的知识发现过程、自动文档处理和分类、以及对欺诈者反制的预期与鲁棒分类机制（组合特征集和集成学习）；这些是可供其他FDS实例复用的制品设计机制，而非仅算法、方程或案例方案。
- Decision: 客观指标：核心成功指标是分类准确性/精确率/召回率/F1和在模拟攻击下的鲁棒性指标，标签依据SEC书面标准，不依赖语义好坏或主观感受；设计目标是提升完全客观的检测和鲁棒性，是文章核心贡献。真实软件制品：文章明确开发可作为FDS核心组件的IT制品，实现了多个具体分类器和攻击模拟，分类器被实际训练和评估；指标改善归因于理论语言特征、组合特征集与集成学习等设计机制。类级贡献：作者明确贡献对象是鲁棒欺诈检测系统这一软件制品类别，以设计原则和设计特征形式提供可复用设计知识，并将其推广到文本分类和意见垃圾信息等领域；移除股票市场案例和数据集后，仍保留FDS类别应如何设计以应对反制的知识。
- Confidence: 0.93

## When Variety Seeking Meets Unexpectedness: Incorporating Variety-Seeking Behaviors into Design of Unexpected Recommender Systems

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2021.0053
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "点击率 (CTR)", "measurement_cn": "在线A/B实验中，用户是否点击推荐的视频（二进制），通过平台日志直接观测", "objectivity_reason_cn": "点击行为是外部可审计事实，不依赖人的感受或语义评价"}, {"name_cn": "视频观看完成 (VV)", "measurement_cn": "用户是否完整观看推荐视频（二进制），通过平台日志直接观测", "objectivity_reason_cn": "实际观看行为是客观行为记录"}, {"name_cn": "停留时长 (TS)", "measurement_cn": "用户观看推荐视频的持续秒数，通过平台日志统计", "objectivity_reason_cn": "时间度量是可直接观测的物理量"}, {"name_cn": "AUC / Hit Rate@10", "measurement_cn": "离线实验中点击/评分二值化后，模型预测排序的AUC和前10命中率", "objectivity_reason_cn": "预测目标是对外部行为（评分/点击）的量化事实，可用标准机器学习指标客观计算"}]
- Artifact: 意外推荐系统（Unexpected Recommender System） — 作者设计了将多样寻求水平作为个性化调节因子的效用函数：U(i,j) = Relevance(i,j) + Variety_Seeking(i) × Unexpectedness(i,j)；同时设计了对应的多样寻求度量机制（潜在距离、时间衰减、平稳性）。该机制在生产推荐系统中作为核心评分组件被实现，以决定向用户推荐内容的意外程度。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除当前公司、数据集和专门生成的界面后，论文仍然贡献了以下可复用知识：如何利用消费记录中的距离、时间衰减和平稳性计算用户多样寻求水平，如何用该水平替代固定的意外度权重进行个性化推荐。这些不是只为当前案例存在的算法/求解器，而是适用于'意外推荐系统'这一软件制品类别的设计机制。
- Decision: 论文最终目标和核心贡献是提升推荐系统的客观业务指标（CTR、观看完成率、停留时长、离线AUC/HR@10）。这些指标全部来自外部可观察行为，不涉及主观质量评价。作者实际设计并实现了推荐系统核心评分组件，将其投入真实平台A/B测试并最终部署，因此属于implemented_artifact_component。贡献明确面向'意外推荐系统'这一软件制品类别，提供了基于用户多样寻求水平个性化意外程度这一可复用设计机制，并在多个数据集和两个推荐场景中验证，满足类级软件制品贡献要求。问卷验证仅用于中间机制验证，不构成共同主要终点，故不排除。
- Confidence: 0.93

## A hybrid decision support system for adaptive trading strategies: Combining a rule-based expert system with a deep reinforcement learning strategy

- Year/journal: 2024 / Decision Support Systems
- DOI: 10.1016/j.dss.2023.114100
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "累计收益（%AR）", "measurement_cn": "交易模拟中相对于初始投资100,000的资产价值变化百分比", "objectivity_reason_cn": "由系统交易记录和资产账本确定，不依赖任何人类感受或语义判断"}, {"name_cn": "夏普比率（SR）", "measurement_cn": "年化超额收益除以年化收益标准差，基于日收益率序列计算", "objectivity_reason_cn": "由可审计的收益和波动率数据推导，客观可复现"}, {"name_cn": "最大回撤（MDD）", "measurement_cn": "资产曲线中峰值到谷底的最大跌幅", "objectivity_reason_cn": "由资产曲线数值计算，客观可审计"}, {"name_cn": "交易信号数量", "measurement_cn": "系统在测试期间实际生成的买入/卖出/止损信号次数", "objectivity_reason_cn": "来自系统日志和交易记录，属于可审计事实"}]
- Artifact: 自适应交易决策支持系统（hybrid decision support system for adaptive trading strategies） — （1）将基于规则的专家系统（Turtle策略）的交易决策信息编码为RL状态空间；（2）引入投资者可用资产状态（平均买入价波动率、持股比例）；（3）基于策略梯度动作概率调整交易量的交易执行机制
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除当前市场名称和数据集后，仍保留下述知识：如何将专家规则系统的决策信息纳入强化学习状态空间、如何引入交易者可用资产状态、如何利用策略概率确定交易量，以设计可自适应不同市场的混合交易决策支持系统
- Decision: 客观指标：所有核心成功指标（累计收益、风险调整后收益、最大回撤、信号数量）均为完全客观的可审计交易结果，且是最终设计目标的核心贡献。软件制品：论文实现了并运行了混合自适应交易决策支持系统，包含了RB专家系统、深度RL agent、状态空间设计和交易量执行机制等明确组件；消融实验将性能和风险指标的改进归因于这些系统设计机制。类级贡献：论文明确面向自适应交易决策支持系统这一类可反复实例化的软件制品，提出可复用的状态空间编码与交易执行机制，并在多个市场和替代RB模型上验证其通用性。因此三个条件均满足。
- Confidence: 0.92

## Interleaved Design for E-Learning: Theory, Design, and Empirical Findings

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2023/17206
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "后测成绩", "measurement_cn": "实验后在线英语阅读测试得分，0-100分，由系统按选择题答案正确性客观判定", "objectivity_reason_cn": "后测成绩是基于固定正确答案的试题得分，不依赖人的主观质量评价、偏好或感知"}, {"name_cn": "会话答题准确率", "measurement_cn": "学习会话中练习题的客观正确率，由系统自动记录和判定", "objectivity_reason_cn": "准确率由系统日志中的对错结果直接计算，属于可审计的外部行为结果"}]
- Artifact: 个性化电子学习系统中的学习会话调度与练习选择系统（personalized e-learning system with adaptive session design） — 作者设计了相关交错（related-interleaving）会话调度机制，包括基于隐马尔可夫模型的弱项主题动态检测、基于模糊关联规则及专家知识的知识图谱更新，以及按弱项和主题相关性选择练习题目的调度引擎
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 即使移除当前中学、英语阅读数据集和专门界面，文章仍留下关于某类可运行软件制品应如何设计的知识：如何检测学习者的弱项主题、如何构建和更新知识图谱、如何通过调度引擎实现相关交错练习选择；这些机制可迁移到其他电子学习平台，而非仅仅是算法、求解器或教育策略声明
- Decision: 该文以设计科学范式提出并实现了一个个性化电子学习系统中的相关交错学习会话设计，核心成功指标是客观可测量的后测成绩、会话准确率和主题掌握状态，且这些指标是研究的主要假设和贡献声明；系统由作者设计并在真实现场实验中运行，HMM弱项检测、知识图谱和调度引擎构成可复用的软件机制；贡献面向电子学习平台这一类软件制品而非单一案例或纯算法。因此三个模块均通过。
- Confidence: 0.9

## Effectiveness of Location-Based Advertising and the Impact of Interface Design

- Year/journal: 2020 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2020.1759922
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "优惠券点击率（click-through rate）", "measurement_cn": "系统日志记录的用户点击优惠券次数除以优惠券曝光次数；按处理组比较均值，并采用层次贝叶斯logit模型估计距离、展示排名等对点击概率的影响。", "objectivity_reason_cn": "点击行为由移动应用系统日志直接记录，是用户对界面展示内容的可观察选择，不依赖人的感受、语义评价或主观质量判断。"}]
- Artifact: 基于位置的拉取式优惠券移动应用（location-based pull coupon application），核心界面组件为距离信息显示与优惠券列表排序机制。 — 作者通过全因子2×2设计在真实应用中操纵两个界面组件：是否显示到店距离信息；优惠券按距离排序还是随机排序。服务端分配用户至四种界面版本，且用户全程保持同一版本。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除德国具体应用、商家和数据集后，仍留下“位置优惠券应用应采用距离排序；距离信息并非必要且需考虑城乡用户异质性”等关于该类软件界面如何设计的可复用知识，不是仅剩算法、求解器或单一案例方案。
- Decision: 本文以真实运行的位置拉取式优惠券应用为对象，通过2×2现场实验操纵距离信息显示与距离排序两种界面组件，以系统记录的点击率作为完全客观的核心有效性指标，发现基于距离排序的界面最有效，并明确面向location-based advertising applications这一可反复实例化的软件类别给出界面设计启示。三项总条件均满足。
- Confidence: 0.85

## Spoiled for Choice? Personalized Recommendation for Healthcare Decisions: A Multiarmed Bandit Approach

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1191
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "推荐精度指标：Precision@K、Recall@K、nDCG@K、MAP@K、DR估计、omniscient simulation", "measurement_cn": "基于平台日志中用户每周是否实际参与被推荐挑战的事实；将推荐集合与实际选择集合对比计算，或通过反事实估计和基于日志的模拟评估。", "objectivity_reason_cn": "用户是否参与某干预是平台记录的外部行为事实，不依赖人的感受、语义或价值判断；计算结果完全由可审计的选择事件决定。"}, {"name_cn": "推荐多样性分布相似度（JSD）", "measurement_cn": "比较推荐集合中各类型干预的频率分布与真实用户选择类型分布，使用Jensen-Shannon散度量化。", "objectivity_reason_cn": "划分维度来自干预属性（饮食/运动/减重），分布频率来自系统生成推荐和用户真实选择日志，均为可核验事实。"}, {"name_cn": "下游健康结果：周内减重率", "measurement_cn": "用户每周称重记录，计算体重下降或保持体重不变的比例；评估中以是否达到该事实状态为奖励信号。", "objectivity_reason_cn": "体重数据来自平台称重记录，是外部可核验的生理状态，不依赖人类主观判断。"}]
- Artifact: 在线健康干预个性化推荐系统（healthcare intervention recommender system），其核心功能包括用户上下文建模、干预项目表示、在线偏好适应和带多样性约束的Top-K推荐。 — 作者设计了：(1) 多序列深度用户表示模型（eLSTM + 注意力 + 健康结果辅助损失），同时处理健康史、干预史、自我监测和社会行为序列；(2) 基于SMART属性的干预项目深度表示模型；(3) 基于社会认知理论的结构化多样性约束；(4) 带多样性约束的Thompson sampling自适应推荐策略（Algorithm 1）。
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除当前减肥社区名称、具体数据集和专门制作的界面后，仍留下关于‘如何设计在线健康干预推荐系统’的可复用知识：如何用多序列深度表示刻画用户动态健康情境，如何用理论驱动的健康管理维度约束推荐多样性，以及如何用bandit在线适应偏好变化。这些不是仅剩的算法方程，而是推荐系统组件的可复用设计机制。
- Decision: 客观指标方面：最终目标是提升用户参与等外部可观察结果，所有核心成功指标均来自平台选择日志、称重记录和基于事实的推荐评价，不依赖主观感知。核心目标与贡献：研究问题和评价结构均指向提升推荐参与等客观结果，并以此作为主要贡献。软件制品方面：在线健康干预推荐系统是可识别的类别，作者实质设计了深度表示、多样性约束和bandit推荐组件并实际运行评价，客观指标改善通过ablation归因于这些组件。类级贡献方面：作者以design science artifact定位，明确提供了可迁移到其他健康干预推荐系统的设计原则和组件机制，当前实现是该类系统在减肥社区数据上的一个实例，反事实检查后仍有类级设计知识，因此判定通过。
- Confidence: 0.84

## Can Recommender Systems Reduce Healthcare Costs? The Role of Time Pressure and Cost Transparency in Prescription Choice

- Year/journal: 2020 / MIS Quarterly
- DOI: 10.25300/misq/2020/14435
- Metric/core status: fully_objective_direct / objective_improvement_primary
- Metrics: [{"name_cn": "处方调整率（是否从初始处方改为推荐的更低价等效药物）", "measurement_cn": "在受控实验中通过系统日志记录每位参与者是否查看推荐以及是否调整处方；调整行为直接对应选择更低成本药物。", "objectivity_reason_cn": "该指标记录的是实际点击/选择行为，不依赖人的感受或语义判定；处方成本是外部可审计的价格事实。"}]
- Artifact: 临床处方推荐系统（healthcare/clinical recommender system） — 
- Class contribution: software_artifact_class / explicit_within_artifact_class / core_research_contribution
- Counterfactual: 移除具体病例、数据集和专门制作的实验界面后，仍留下关于临床处方推荐系统应如何设计成本呈现和信息呈现的可复用知识，例如低成本和混合成本推荐框架的差异效果，以及是否需要按用户类型适配。
- Decision: 目标构念为处方选择成本，可直接观测；核心成功指标是查看和调整推荐的行为，客观且不依赖主观评价。研究问题、实验设计和贡献声明均以通过推荐系统降低医疗成本为核心。系统中的成本呈现机制（低成本/混合成本推荐）、时间压力提示和实际运行的实验原型构成可识别的软件制品。贡献明确针对临床处方推荐系统这一软件类别，并提出可推广的设计启示。
- Confidence: 0.72
