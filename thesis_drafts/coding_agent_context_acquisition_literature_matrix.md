# Coding Agent 仓库上下文获取研究：文献—理论—基准证据矩阵

> 检索与核验日期：2026-08-11  
> 用途：为《有限信息预算下 Coding Agent 的仓库上下文获取决策研究》提供可追溯的文献依据。本文档不是论文正文，而是正文的证据台账。  
> 证据等级：A=正式发表且存在官方论文页/本地全文；B=公开预印本且代码或数据已开放；C=仅预印本或开放承诺尚待兑现。

## 1. 纳入逻辑

本研究只保留同时满足下列至少一种用途的文献：

1. 直接定义仓库级上下文获取问题、算法或可运行基准；
2. 为“信息项—信息源—停止时机”之一提供可迁移的决策理论、目标函数或评估规范；
3. 为设计科学、情境化理论或计算实验的学术写作规范提供依据。

“与检索有关”并不足以纳入。若一篇论文没有公开任务实例、评价脚本、可复现数据或无法进入本研究的统一效用函数，则不作为核心实验依据。图检索、轨迹检索和强化学习检索分别被视为候选检索服务、历史信息源和未来扩展，而不被强行设置成三个互不相干的研究主题。

## 2. Coding-agent 与仓库级检索文献矩阵

| 文献 | 状态 | 主要问题与方法 | 可运行数据/指标 | 在论文中的角色 |
|---|---|---|---|---|
| Liu, Xu, & McAuley (2024), **RepoBench**, ICLR | A | 将仓库级问题拆分为检索、补全和流水线三类任务 | Python/Java；EM、Edit Similarity、CodeBLEU；公开代码与 Hugging Face 数据 | 研究一的低成本开发集和跨任务外部验证；证明“检索性能”和“生成性能”可分层评估 |
| Ding et al. (2023), **CrossCodeEval**, NeurIPS Datasets and Benchmarks | A | 跨文件代码补全，比较 BM25、UniXCoder、Ada 等检索设置 | Python、Java、TypeScript、C#；检索与生成脚本公开 | 研究一的跨语言稳健性检验；避免只在 Python 缺陷修复上得出结论 |
| Zhang et al. (2023), **RepoCoder**, EMNLP | A | 检索—生成迭代，以已生成代码改写后续查询 | RepoEval；EM、CodeBLEU 等 | 说明查询会随过程更新，是研究三序贯状态的技术前件 |
| Cheng, Wu, & Hu (2024), **DraCo**, ACL | A | 用数据流图检索跨文件依赖上下文 | ReccEval；EM、Identifier F1 | 研究一的结构服务候选和“结构覆盖”指标来源 |
| Wu et al. (2024), **Repoformer**, ICML | A | 选择性检索；比较有/无检索上下文的代码生成收益，学习何时跳过检索 | 跨文件代码补全基准；质量、检索频率、时延 | 研究三“检索不是每轮必做”的直接技术先例；但其标签是一次性选择，不等同多轮停止 |
| Wang et al. (2025), **CodeRAG-Bench**, Findings of NAACL | A | 联合评价检索、生成与执行，系统比较多种检索器和语言模型 | 10 类检索器、10 类模型；仓库级任务与 SWE-bench；BEIR 格式 | 研究二构造固定候选服务池和离线回放日志的主要基准 |
| Jimenez et al. (2024), **SWE-bench**, ICLR | A | 从真实 GitHub issue 修复真实仓库问题 | Lite、Verified；Docker 测试；resolved/pass | 只作为末端任务效用验证，不用于每次算法迭代，以控制资源消耗 |
| Yang et al. (2024), **SWE-agent**, NeurIPS | A | 设计 agent–computer interface，使模型能够导航、编辑和测试仓库 | SWE-bench、HumanEvalFix；公开 agent | 端到端环境基线；说明上下文获取嵌入行动过程而非独立搜索框 |
| Xia et al. (2025), **Agentless**, FSE | A | 将修复拆成定位、修复和验证，提供成本较低的非 agent 强基线 | SWE-bench；定位与修复脚本 | 研究二、三的成本敏感基线和固定下游修复器 |
| Ouyang et al. (2025), **RepoGraph**, ICLR | A | 将仓库表示为代码依赖图并向 agent 提供图导航/子图 | SWE-bench 等；代码开放 | 研究一结构覆盖、研究二结构检索服务的核心候选 |
| Chen et al. (2025), **LocAgent**, ACL | A | 在有向异构代码图上执行多跳定位 | SWE-bench 等；文件级定位和成本指标 | 研究二结构服务基线；强调多跳依赖对 issue 定位的价值 |
| Zhang et al. (2024), **CodeAgent**, ACL | A | 通过检索、实现、测试等工具完成仓库级编程任务 | CodAgentBench；工具轨迹 | 研究三定义“检索与其他行动竞争预算”的情境依据 |
| Li et al. (2026), **One Size Does Not Fit All**, FSE | A | 比较相似度、静态分析与 agent 导航三种上下文工程范式 | 7 种方法、8 个 LLM；DCR 与效率指标 | 研究二“不同任务适合不同来源”的直接经验动机；正式实验前核验开放包版本 |
| Qin & Xie (2026), **Agent Retrieval Bench (ARB)** | B | 全仓候选空间中的 agent 检索，含有金标准和无金标准问题 | 427 样本、25 仓库；MRR、Recall@k、BCY@B、selective success；代码数据公开 | 三项研究的首要检索层 benchmark：研究一做预算打包，研究二做服务配置，研究三做选择性停止 |
| Li et al. (2026), **ContextBench** | B | 以人工金标准标注 issue 修复所需文件、符号、跨度与编辑位置 | 1,136 任务、66 仓库、8 语言；500 verified；轨迹和 runner 公开 | 研究一的细粒度覆盖评价；研究三的状态特征与轨迹初始数据 |
| Zhang et al. (2026), **SWE-Explore-Bench** | B | 专门评估 coding agent 的仓库探索过程 | 848 issues、203 repos、10 languages；行级核心/可选上下文、首个有效命中、预算 nDCG、下游补丁质量 | 研究三的主基准；其过程标注比只看最终补丁更适合训练/评价停止策略 |
| Chen et al. (2026), **CodeGrep** | C | 用 GRPO 训练专门检索 agent | 论文报告 67K 轨迹和 SWE-bench 结果；截至核验日发布极新 | 仅列为后续“学习式检索服务”，不作为博士论文可行性的支点 |
| Shah et al. (2025), **RANGER** | C | 知识图谱、Cypher 与 MCTS 图探索 | 预印本；开放成熟度需复核 | 仅作图搜索算法扩展，不据此声称已有成熟 benchmark |
| GraphCodeAgent (2025) | C | 需求图与结构—语义代码图的双图多跳检索 | 预印本，报告 DevEval/CoderEval 结果 | 仅用于讨论多视图结构，不作为 CCF-A 正式发表证据 |

## 3. AIS Basket 文献及其参考文献链

### 3.1 信息项的有成本选择

| 文献 | 数据/方法 | 可迁移的核心命题 | 迁移边界 |
|---|---|---|---|
| Mookerjee & Dos Santos (1993), ISR, *Inductive Expert System Design: Maximizing System Value* | 理论建模与分类实验；DOI: 10.1287/isre.4.2.111 | 只有当预期决策收益超过信息获取成本时才获取属性；系统价值优先于分类精度 | 属性可逐项询问，而代码块之间存在依赖与冗余，不能直接照搬独立属性假设 |
| Mookerjee & Mannino (1997), ISR, *Redesigning Case Retrieval to Reduce Information Acquisition Costs* | Zoo、Lymphography 与合成数据；`ID3_c` | 用“单位获取成本带来的不确定性下降”排序信息；联合设计知识结构和检索过程 | 原文以分类正确率为终点，本研究以检索覆盖和补丁通过为终点 |
| Mookerjee & Mannino (2000), ISR, *Mean-Risk Trade-Offs in Inductive Expert Systems* | 均值—风险决策 | 平均效用相同的方案可能有不同失败风险；检索器需同时报告期望效用和尾部风险 | 不把金融式风险偏好直接解释为 LLM 心理属性，只用作鲁棒目标 |
| Saar-Tsechansky & Provost (2007), ISR, *Decision-Centric Active Learning of Binary-Outcome Models* | KDD Cup 1998；GOAL-AC 与误差/随机获取基线；DOI: 10.1287/isre.1070.0111 | 信息获取应最大化下游决策价值，而非只降低预测误差；以单位成本价值选取样本 | 主动学习选择训练标签，本研究选择推理时上下文；可迁移的是目标函数规范而非算法本身 |
| Voorberg et al. (2021), DSS, *Decisions for Information or Information for Decisions?* | Koffer 决策流程；MDP、决策树基线；DOI: 10.1016/j.dss.2021.113632 | 状态为已获信息，行动是在继续获取和作出最终决策之间选择，回报为终局收益减获取成本 | 原文流程任务状态规模较小；代码仓库状态高维，需压缩为覆盖、置信度和边际收益特征 |
| Wang, Ipeirotis, & Provost (2017), ISR, *Cost-Effective Quality Assurance in Crowd Labeling* | 合成与真实 crowd 数据，动态分配；DOI: 10.1287/isre.2016.0661 | 固定平均分配会浪费预算；应把下一单位资源分给预期增益最大的对象，并同时评估中间推断和终局质量 | 标签员不是检索器；可迁移的是动态边际分配与双层评价 |

### 3.2 多源信息获取与等待

| 文献 | 数据/方法 | 可迁移的核心命题 | 迁移边界 |
|---|---|---|---|
| Roussinov & Chau (2008), JAIS, *Combining Information Seeking Services into a Meta Supply Chain of Facts* | TREC 2004；多服务组合、消融、响应时间；DOI: 10.17705/1jais.00154 | 异质服务在质量和时延上互补；组合的评价必须同时看答案排名质量和响应时间 | 原文服务返回事实答案，本研究服务返回可能重叠的代码片段，需显式惩罚冗余 |
| Hosanagar (2011), ISR, *Usercentric Operational Decision Making in Distributed Information Retrieval* | FedStats：15 个服务器、33 天、26 查询；随机混合整数规划；DOI: 10.1287/isre.1100.0287 | 联合决定查询哪些源、等待多久、展示哪些结果；源进入条件是响应概率乘预期净效用不低于查询费用；最优等待点满足边际收益等于边际等待成本 | 原文近似假设源间文档不重叠且评价成本线性；代码检索源高度重叠，故研究二必须引入条件边际收益，研究三采用在线自适应停止 |
| Choudhury & Sampler (1993), MISQ, *Information Specificity and Environmental Scanning* | 经济学理论；DOI: 10.2307/249741 | 信息源选择取决于特异性及获取安排；“来源”本身是决策变量 | 仅作多源组织逻辑，不参与算法公式的直接推导 |

### 3.3 信息量与停止规则

| 文献 | 数据/方法 | 可迁移的核心命题 | 迁移边界 |
|---|---|---|---|
| Browne, Pitts, & Wetherbe (2007), MISQ, *Cognitive Stopping Rules for Terminating Information Search in Online Tasks* | 115 名参与者、三类在线任务；DOI: 10.2307/25148782 | 停止不是单一阈值；结构化任务倾向 mental-list/single-criterion，弱结构任务倾向 magnitude-threshold/representational-stability | 这是描述人类行为的理论，不证明 LLM 具有相同认知机制；本研究只把规则操作化为可观察的停止状态特征 |
| Browne & Walden (2021), DSS, *Stopping Information Search: An fMRI Investigation* | 行为与 fMRI；DOI: 10.1016/j.dss.2021.113498 | 信息充分性判断具有过程性；终止应基于状态变化而非固定轮数 | 只能提供构念启发，不可把神经机制外推给 agent |
| Mullins & Sabherwal (2022), MISQ, *Just Enough Information?* | 两项 ERP 模拟研究；118/60 个团队，354/328 team-rounds；GLS 与稳健性检验；DOI: 10.25300/misq/2022/17290 | 客观信息量与决策绩效呈倒 U 型；信息量应按“每个决策实际访问的信息线索”而非可用总量计量 | 人类工作记忆不是 LLM 上下文窗；迁移的是“边际信息可能转负”以及过程计量方法，机制需在 coding agent 情境重新检验 |

### 3.4 方法论与写作规范

| 文献 | 对本论文的约束 |
|---|---|
| Hevner et al. (2004), MISQ, *Design Science in Information Systems Research* | 人工制品必须对应明确问题、经过严格评价并形成可交流知识；三项算法不能只是工程组件清单 |
| Peffers et al. (2007), JMIS, *A Design Science Research Methodology for Information Systems Research* | 按问题识别—目标—设计开发—示范—评价—传播组织研究过程；当前稿将“未完成实证”明示为预注册方案 |
| Gregor & Hevner (2013), MISQ, *Positioning and Presenting Design Science Research for Maximum Impact* | 同时陈述问题成熟度和解决方案成熟度；本研究属于已有问题的新情境化决策设计，而非声称发明仓库检索问题 |
| Hong et al. (2014), ISR, *A Framework and Guidelines for Context-Specific Theorizing* | 从一般信息获取理论出发，识别 coding agent 特有因素（token 预算、仓库图依赖、执行反馈），检验交互和替代模型；不能只给新名词 |

### 3.5 肖帅勇等 ISR 论文的“理论驱动人工制品”写法

| 文献 | 论证结构 | 对本论文的具体借鉴 | 不直接照搬之处 |
|---|---|---|---|
| Chen, Xiao, Zhang, & Zhao (2023), ISR, *A Theory-Driven Deep Learning Method for Voice Chat-Based Customer Response Prediction*, DOI: 10.1287/isre.2022.1196 | 用期望不一致理论把个性化偏好、动态期望、实际体验和动态满意度转译成三项方法挑战，再让三项算法组件逐一响应；评价依次覆盖端到端预测、表征质量、理论构念的增量效用、累积构念、消融与解释性分析 | 每项上下文决策必须给出“理论命题—情境变量—设计要求—算法机制—专门证据”的闭环；除最终修复率外，单独检验检索表示、中间效用估计、算法增量与机制有效性 | 不把不可直接观测的构念强行伪装成真值；本研究的状态特征均由金标准、工具日志或执行反馈定义 |
| Chen, Huang, Xiao, Zhang, & Zhao (2024), ISR, *Attending to Customer Attention: A Novel Deep Learning Method for Leveraging Multimodal Online Reviews to Enhance Sales Prediction*, DOI: 10.1287/isre.2021.0292 | 从信息处理过程和粒度框架概念化四类顾客注意指标，逐一嵌入网络；用预测、表征、历史销售强基线、集成增量、权重探索与消融形成累积证据 | 本论文将三种决策维度做成可追踪映射表；采用“检索层—生成/修复层—成本层—解释层”分层评价，并用固定强下游 agent 证明上下文获取的增量价值 | 不把模型内部权重等同真实心理注意；同理，不把检索分数直接称作 agent 的“理解”或“认知” |

这两篇论文提示了一种有 IS 特色但仍可检验的写法：技术人工制品不是先造出来再贴理论标签，而是让理论限定人工制品应该感知什么、优化什么以及如何被评价。因而，本论文不只问“新算法是否比 BM25 高若干点”，而要依次回答：（1）成本敏感的决策价值是否被可靠估计；（2）该估计是否确实改变上下文、来源和停止决策；（3）这些改变是否在固定下游 agent 上产生增量任务效用；（4）设计原则在哪些仓库、任务和预算条件下成立。

## 4. 参考文献链与三项研究的关系

| 传统问题 | IS 参考文献链 | Coding-agent 接续 | 本论文新增决策 |
|---|---|---|---|
| 是否获取某项信息 | Mookerjee & Dos Santos (1993) → Mookerjee & Mannino (1997) → Saar-Tsechansky & Provost (2007) → Voorberg et al. (2021) | RepoBench、DraCo、ARB、ContextBench | 在 token 预算下联合考虑相关性、依赖覆盖、冗余与成本，选择上下文包 |
| 从哪些来源获取 | Roussinov & Chau (2008) → Hosanagar (2011)；并参考动态资源分配的 Wang et al. (2017) | BM25/dense/static graph；CodeRAG-Bench、RepoGraph、LocAgent | 根据检索前可观察的任务与仓库特征，选择来源组合和离散配额；研究二不引入多轮在线决策，以免与研究三重叠 |
| 何时停止获取 | 经济边际规则 → Browne et al. (2007) → Browne & Walden (2021)；Voorberg et al. (2021) 的序贯获取；Mullins & Sabherwal (2022) 的倒 U 型证据 | Repoformer 的选择性检索、RepoCoder 的迭代、SWE-Explore-Bench/ContextBench 的轨迹 | 在每轮检索后比较继续的预期增量与 token、工具、时延成本，输出可解释的停止原因 |

该链条不是“IS 文献给 coding agent 贴标签”。三项研究分别保留了 IS 文献中可操作的决策结构——单位成本价值、异质来源联合配置、序贯边际停止——同时把效用、成本和状态重新定义为代码仓库环境中可观测、可运行的量。

## 5. Benchmark 可行性与使用顺序

| 层次 | 首选基准 | 适用研究 | 计算负担与使用方式 |
|---|---|---|---|
| 快速算法开发 | RepoBench-R、CrossCodeEval | 研究一 | 静态离线检索/补全，可频繁迭代；不需完整 agent rollout |
| 检索决策主实验 | ARB | 研究一、二、三 | 427 个样本、完整候选仓库、预算指标和 no-gold 任务；采用 repository-grouped split 防止仓库泄漏 |
| 细粒度上下文验证 | ContextBench | 研究一、三 | 文件/符号/跨度/编辑位置，多语言；先使用 500 verified 子集，再扩展全部任务 |
| 探索过程与停止 | SWE-Explore-Bench | 研究三 | 带读取过程和核心/可选行标注，可评估首次有效命中、噪声和预算覆盖 |
| 检索—生成联合 | CodeRAG-Bench | 研究二 | 复用多检索器和生成器接口，产生可比的来源收益与互补性日志 |
| 最终端到端 | SWE-bench Lite/Verified 子集 | 三项研究的总体验证 | Docker 成本高，只在算法冻结后运行；报告任务通过率、总 token、工具调用、时延和失败类型 |

因此，“是否有现成 benchmark 和测试数据”不是本选题的主要不可行性来源。真正的风险在于：不同 benchmark 的金标准和任务效用不完全一致、2026 年新基准规模仍有限、端到端回放昂贵。论文方案通过分层评价、仓库级切分、固定下游 agent、末端小规模 SWE-bench 验证来控制这些风险。

## 6. 不作为核心支点的方向

- **大规模强化学习检索器**：可作为未来扩展，但它要求大量可靠轨迹、奖励建模和算力；不适合作为目前博士论文三个研究中任何一个的必要条件。
- **纯轨迹 RAG**：成功轨迹可作为研究二的第四类信息源，但现有任务间可迁移性和数据许可尚不足，不单独设章。
- **任意 MCTS 图搜索**：树搜索只是实现方式，若没有成本目标、公开环境和优于简单图遍历的证据，不构成独立研究问题。
- **只优化 Recall@k**：高召回可能通过塞入更多上下文取得，却提高 token、干扰和时延；只能作为中间指标，不能作为最终贡献。

## 7. 证据使用纪律

1. 正文中所有关于 2026 年基准规模的陈述均注明核验日期，正式投稿前再次检查版本和许可。
2. 对预印本不写“已发表于 CCF-A”；只有存在正式会议/期刊页面时才标注正式发表。
3. 人类信息处理与停止理论只用于提出情境化设计命题，不声称 LLM 具有工作记忆、焦虑或神经机制。
4. 正式实验前不填写任何显著性、提升百分比或置信区间。正文中的示例表统一标注“假想结果/占位”，不得被当作实证事实引用。
5. 评价至少同时报告中间检索质量、最终任务效用、资源成本、稳健性和失败类型，防止单指标叙事。
