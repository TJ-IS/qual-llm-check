# 让检索来源适应任务：面向 Coding Agent 的多源仓库检索与预算配置方法

**英文标题：** *Making Retrieval Sources Fit the Task: A Task-Conditioned Method for Multi-Source Repository Retrieval and Budget Allocation*

> 稿件状态：完整研究设计稿。本文不虚构任何尚未运行的效果；所有 `[待实验]` 必须由冻结版本上的真实结果替换。

## 摘要

尽管词法、稠密和结构检索已被广泛用于为 coding agent 获取仓库上下文，现有系统通常固定采用一种来源或不加区分地调用并融合所有来源。由这种固定策略得到的上下文并不必然具有较高任务价值，因为检索来源的能力随查询和仓库条件变化，其结果又可能高度重叠，同时产生不同的索引、计算与响应成本。基于分布式信息检索和有成本资源配置的观点，本文主张，一个检索来源是否值得调用以及获得多少配额，应由它在当前任务条件下相对于其他已选来源对最终上下文包所增加的净效用决定。本文分别在任务、来源组合、单一来源和候选结果四个层次概念化来源价值，并导出任务适配、来源互补、获取成本和决策风险四个可操作指标。进而，本文提出任务条件多源配置器（Task-conditioned Multi-source Allocator，TMA），离线枚举小规模来源—配额组合，以统一上下文选择器产生的成本调整效用为监督信号，学习配置的条件效用和不确定性，并在高风险任务上退化到保守配置。本文设计在 Agent Retrieval Bench、CodeRAG-Bench、ContextBench 与 RepoBench/CrossCodeEval 上，从净任务效用、配置排序质量、全来源强基线、相对固定打包器的增量、来源条件效应和组件消融六个层次评价 TMA；实证结果为 `[待实验]`。

**关键词：** Coding Agent；多源检索；来源选择；预算配置；分布式信息检索；设计科学

## 1. 引言

仓库级软件任务所需证据分散在不同文件、符号和程序关系中。查询若包含函数名、路径或异常栈，词法检索可以直接利用精确匹配；查询若以自然语言描述行为，稠密表示可以连接不同词面的语义；查询若只点明表层症状，定义—引用、调用、导入或测试关系又可能带领系统找到未被直接提及的依赖。RepoBench、CrossCodeEval、DraCo 和 RepoGraph 分别从跨文件补全、数据流与仓库图角度展示了这些检索信号的价值（Ding et al. 2023; Liu et al. 2024; Cheng et al. 2024; Ouyang et al. 2025）。因此，现代 coding agent 的仓库检索并非只有一个同质搜索框，而是由质量、成本和响应方式不同的信息服务共同组成。

一种直接做法是固定调用词法、稠密和结构检索，把各来源 top-k 结果合并，再以 reciprocal rank fusion、统一重排或简单去重生成候选池。固定全调用可以提高发现不同类型证据的机会，却把候选生成视为免费。稠密检索需要编码和向量索引，结构检索需要解析与图查询，所有来源的返回项还会增加去重、重排和序列化开销。更重要的是，多个来源可能反复返回同一文件或同一符号；此时每个来源独立看似相关，合并后的新增价值却很小。既有系统一方面重点改进某一种检索器的能力，另一方面常在所有任务上使用同一融合流程，因而没有充分利用执行前已经可见的任务和仓库差异。

检索来源的最终作用根植于它是否改变 agent 获得的上下文以及由此作出的代码行动。一个来源独立 Recall 较高，并不意味着在另一来源已经找到关键文件后仍有同等价值；一个图来源返回较少文件，也可能因补齐唯一依赖而产生较大增量。Hosanagar（2011）在分布式信息检索中把 broker 的问题写成“查询哪些服务器、等待多久以及展示哪些结果”，并以用户收益扣除访问和等待成本衡量来源。迁移到代码仓库，本文提出中心命题：来源价值不是来源的固定属性，而是任务条件、其他来源结果、最终预算打包和获取成本共同作用下的条件净贡献。

现有代码检索文献已经形成词法、表示和结构三类证据，却没有发现一个跨情境恒优来源。BM25 对稀有标识符和错误文本敏感，语义编码器可以缓解词汇不匹配，数据流或代码图则可连接跨文件依赖（Robertson and Zaragoza 2009; Guo et al. 2021; Cheng et al. 2024）。CodeRAG-Bench 对十类检索器和十类语言模型的比较进一步显示，检索收益取决于任务与生成器，取得高质量上下文和有效利用上下文都是瓶颈（Wang et al. 2025）。若查询中已经出现精确路径，昂贵语义或图来源可能只复制词法结果；若自然语言与仓库命名差异很大，固定 BM25 又可能漏掉语义相近代码。因此，来源的平均排名不足以决定每个任务上的调用。

从过程看，多源仓库检索至少经过来源调用、候选返回、候选打包和下游使用四个环节。来源选择决定是否支付获取成本；候选返回决定每个来源能提供什么；打包器决定重叠结果中哪些真正进入有限提示；下游模型决定这些内容能否改善补全或修复。Roussinov and Chau（2008）说明异质信息服务可通过组合提高事实答案质量，Hosanagar（2011）同时考虑来源质量与响应时间；但代码检索来源高度重叠，且返回内容还要经过 token 预算选择。本文因而不以各来源独立 Recall 的总和定义配置效用，而以固定打包器生成的最终上下文包及其下游结果定义。

从层次看，来源配置可以沿任务—来源组合—单一来源—候选结果组织。任务层包含执行前可见的 query 与仓库特征；组合层决定哪些来源共同被调用以及配额如何分配；单一来源层具有不同质量、成本和响应分布；结果层呈现跨来源重叠和独特证据。自上而下，任务条件改变来源先验；自下而上，返回结果的重叠决定组合边际价值。由此提出第一个研究问题：**RQ1：哪些执行前可观察的任务与仓库条件，会改变词法、稠密和结构检索对最终上下文包的净贡献？**

分布式检索和资源配置研究为 RQ1 提供了理论支点。Hosanagar（2011）说明来源进入查询集合取决于响应概率、预期效用、访问费与等待成本；Roussinov and Chau（2008）表明不同信息服务可以形成互补的“事实供应链”。Moore et al.（1997）研究多主体资源配置时比较不同信息获取政策，并把通信、计算和转换成本纳入信息系统设计；Wang et al.（2017）则证明，把下一单位资源动态分给预期增益最大的对象可以优于固定平均分配。对应到 coding agent，精确标识符、词汇不匹配与图可解析性刻画任务适配，跨来源独特文件和结构单元刻画互补，检索时延与候选处理刻画成本，预测不确定性和尾部 regret 则刻画风险。由此提出第二个研究问题：**RQ2：如何在检索开始前，以可运行、可校准且不过度复杂的方式选择来源组合和离散配额？** 为回答 RQ2，本文提出 TMA。

TMA 首先固定三个成熟来源和少量配额档位，使可行配置能够离线枚举；各来源只需运行一次，其不同配额可以由缓存排名前缀组合。随后，统一的结构感知预算打包器把合并候选转成最终上下文包，并以金标准覆盖、下游任务效用、token、检索时延和处理成本形成配置标签。TMA 使用执行前可见特征估计每个配置的条件效用及其不确定性，显式加入来源交互；在线阶段选择风险调整后效用最高的配置，高不确定时则退化到训练仓库上验证过的保守策略。这样，来源策略的增量与候选打包差异得以分离，也避免把大规模强化学习作为可行性的前提。

本文拟建立六层累积证据。ARB 提供正检索和 no-gold 任务，适合评价是否应调用来源及预算产出；CodeRAG-Bench 提供多检索器、多生成器与统一代码检索环境；ContextBench 提供细粒度金标准；RepoBench 和 CrossCodeEval 支持低成本跨语言开发（Ding et al. 2023; Liu et al. 2024; Wang et al. 2025; Li et al. 2026; Qin and Xie 2026）。评价首先比较净任务效用，其次检验配置排序、oracle regret 与校准，再以固定全来源融合为强基线，继而固定打包器验证来源配置的增量，最后用来源份额、条件效应、退化日志和消融回答 RQ1。结果为 `[待实验]`，所有来源规律都必须由分层证据限定。

## 2. 文献综述

### 2.1 异质仓库检索来源

经典信息检索把索引、查询表示、匹配和评价视为相互依赖的系统环节，而不是把检索器名称等同稳定能力（Baeza-Yates and Ribeiro-Neto 1999）。个性化搜索研究也说明，可观察的兴趣与活动历史能够改变查询结果的相关性分布（Teevan et al. 2005）。TMA 不迁移用户兴趣构念，但接受同一设计命题：全局平均排名无法排除实例条件所造成的相对收益变化；条件特征必须在未见仓库上证明其作用，才有资格进入配置器。

词法检索根据查询和代码中的词项匹配取得候选。BM25 以词频饱和和逆文档频率校准相关性，计算简单、结果可解释，因而广泛作为代码检索基线（Robertson and Zaragoza 2009）。在 issue 包含具体类名、函数名、路径、测试名或异常消息时，这种精确匹配具有明显优势。RepoBench、CrossCodeEval 和 RepoCoder 均把基于相似度的检索作为仓库级系统的重要组成（Ding et al. 2023; Zhang et al. 2023; Liu et al. 2024）。然而，若问题描述使用业务语言、同义改写或只呈现行为症状，词面匹配可能无法连接真实实现。

稠密检索把自然语言与代码映射到向量空间。CodeBERT、GraphCodeBERT 和 UniXcoder 分别利用双模态预训练、数据流和跨模态目标学习代码表示（Feng et al. 2020; Guo et al. 2021; Guo et al. 2022）。在仓库情境中，这类表示可以召回命名不同但语义近似的实现，也可以作为候选重排器。代价是需要离线或在线编码、近似最近邻索引和模型维护，而且表示相似仍可能偏向一般功能而非当前仓库约束。CodeRAG-Bench 的多检索器比较与 RepoAlignBench 的仓库级检索设置都表明，编码器、候选粒度和查询情境会改变检索结果及其下游价值（Wang et al. 2025; Liu et al. 2025）。

结构检索把程序分析关系作为导航信号。CoCoMIC 使用静态分析定位跨文件上下文，DraCo 构建扩展数据流图，RepoGraph 向软件工程 agent 暴露仓库级代码图，LocAgent 在异构图中执行多跳定位（Ding et al. 2024; Cheng et al. 2024; Ouyang et al. 2025; Chen et al. 2025）。结构来源能够发现 query 没有点名的定义、调用者和测试，但其有效性依赖语言解析、动态特性、生成代码和仓库构建信息。图来源还可能沿高连接节点扩展出大量任务无关内容。

三类来源的差异说明，多源选择不是从若干等价系统中挑一个平均最好者。精确标识符比例、自然语言—代码词汇重合、错误栈存在、预期跨文件距离、图解析覆盖和仓库规模都可能改变来源收益。现有文献常在各自实验设置中展示一种来源的平均优势，却较少把这些条件统一建模为推理时配置变量。本文的目标不是再训练一个更强的 BM25、embedding 或图 agent，而是决定在给定任务上何时调用它们以及分配多少候选预算。

通用检索基础设施还揭示了一个常被代码研究省略的运营层。稠密来源通常依赖近似最近邻索引；FAISS 和 HNSW 分别说明，向量检索的速度、内存与召回取决于索引实现和搜索参数，而不是由编码器精度单独决定（Johnson et al. 2019; Malkov and Yashunin 2020）。词法来源也要维护倒排索引，结构来源则承担解析、增量更新和图存储。因而，“同一任务上哪一种来源最有效”与“哪一种来源最值得在线调用”不是同一个问题：前者主要比较结果质量，后者还取决于索引是否已存在、查询是否可并行、候选规模和服务负载。TMA 将这些量留在分解成本表中，使某个来源在特定部署上的优势不会被误写成不随基础设施变化的算法规律。

最新仓库级工作使这一边界更加重要。RepoAlignBench/ReflectCode 把变更请求驱动的检索扩展到仓库级语义与依赖，RepoDistill 把检索、压缩预算分配和策略优化组成端到端框架，RepoAudit 则以按需数据流探索处理仓库审计，并显式报告时间和 token 成本（Liu et al. 2025; Yin et al. 2026; Guo et al. 2025）。这些工作证明条件检索、预算控制和结构探索已经可以运行，却也把多个机制同时改变。本文与其形成的非牵强差异是：TMA 不争夺端到端系统总分，而是冻结来源和打包器，只识别“执行前任务条件是否足以改善来源—配额决策”。若这种独立增量不存在，应优先采用固定或联合训练方案，而不应为了形式上的个性化保留 TMA。

### 2.2 多源融合与选择

传统结果合并发展了基于 logistic regression 的跨数据库分数校准，FedLemur 则在真实分布式环境中联合观察资源选择与合并（Le Calvé and Savoy 2000; Avrahami et al. 2006）。这些工作说明，来源分数不可比和来源选择是两个相邻但不同的问题。TMA 先用来源内名次和统一候选身份对齐解决可比性，再用最终包效用训练配置器；若把二者合并成一个黑箱重排器，就无法识别收益来自分数校准还是少调用了来源。

信息检索中的 metasearch、federated search 和 rank fusion 长期研究如何组合多个结果列表（Callan et al. 1995; Aslam and Montague 2001; Cormack et al. 2009）。Reciprocal rank fusion（RRF）不要求分数同量纲，按各列表中的名次累加得分，因简单稳健而常被采用（Cormack et al. 2009）。在代码 RAG 中，也可以把 BM25、向量和结构结果合并后重排。此类方法解决“怎样合并已经调用的来源”，但不直接回答“哪些来源值得调用”和“各调用多少”。

CodeRAG-Bench 为多源代码检索提供了重要经验基础。该基准汇集竞赛解答、教程、文档、Stack Overflow 和 GitHub 仓库等数据源，联合评价十类检索器与十类语言模型，并明确区分检索与端到端生成（Wang et al. 2025）。其结果支持“检索器与任务之间存在异质匹配”，但 benchmark 比较本身不是任务级配置算法。若把所有检索器都运行后才选择最佳，在线成本已经发生；若以测试金标准选择来源，又会产生 oracle 泄漏。

选择性检索提供另一条相关路径。Repoformer 学习判断检索能否改善代码补全，从而在不需要时跳过检索，并报告明显的服务速度提升（Wu et al. 2024）。它证明“是否检索”本身可以学习，但主要面向一次性检索与单个检索流程。TMA 把行动扩展为三个来源的组合和离散配额，同时把来源交互、检索成本与配置不确定性纳入目标。本文把 Repoformer 式二元选择作为边界基线，而不把它等同多源配置。

联邦检索对“先选来源、再合并结果”有更直接的技术积累。早期 collection fusion 研究学习不同集合的融合策略，GlOSS 以集合统计量估计数据库内容，decision-theoretic database selection 则把相关文档概率和访问决定联系起来（Voorhees et al. 1995; Gravano and García-Molina 1995; Fuhr 1999）。随后，relevant-document-distribution estimation 与 unified utility maximization 分别估计相关文档在资源间的分布和资源选择效用（Si and Callan 2003, 2004）；FedLemur 将联邦搜索置于真实分布式环境，Shokouhi and Si（2011）系统总结了资源表示、选择、结果合并和垂直选择。它们共同提供了 TMA 的动作结构，但多数目标在文档或集合层终止。代码候选仍需进入有限 prompt 并被下游 agent 使用，所以本文必须把经典资源选择的终点向后延伸两个环节。

算法选择研究则说明，条件配置只有在问题实例间存在可学习差异时才成立。Rice（1976）把实例特征、算法空间、性能度量和选择映射组织为统一框架；“没有免费午餐”结果提醒研究者不能在没有分布限定时宣称一种配置普遍占优（Wolpert and Macready 1997）；后续元学习与自动配置工作进一步强调特征取得成本、搜索空间和验证协议（Smith-Miles 2009; Hutter et al. 2011）。TMA 借用的是这一结构，而不是自动配置的庞大搜索：来源数和配额档位刻意保持很小，使所有配置结果能够被观察。这样，条件效应可由真实反事实检验，而不是仅由路由器权重解释。

### 2.3 分布式信息检索与资源配置

Hosanagar（2005）把等待时间直接写入分布式检索效用，Etzioni et al.（1996）则从计算角度研究互联网上的高效信息获取。这两项工作共同提示，来源数量、等待多久和计算多少不是检索完成后的附属统计，而是取得信息时同时作出的决策。TMA 的离散配额同时限制候选量和来源调用，但首版不优化异步返回顺序；异步等待属于序贯停止或后续扩展，不能由一次性配置结果越界解释。

Roussinov and Chau（2008）把多个信息寻求服务组织为事实的元供应链，通过服务组合改善答案质量并报告响应时间。该研究提示，信息服务的价值既来自自身能力，也来自与其他服务的互补；但事实服务和代码检索存在重要差异：多个代码来源经常返回同一文件，重叠不是可以忽略的边缘情形。因而，本文用最终上下文打包结果测量组合价值，而不直接相加独立来源 Recall。

Hosanagar（2011）进一步从用户中心视角建立分布式信息检索决策模型。broker 联合决定查询哪些服务器、等待多久和展示哪些结果；更多来源和更长等待可能取得更多文档，也会增加访问费和用户等待成本。基于 FedStats 的经验说明，来源质量与响应时间异质性可以被用于提高系统效用。该模型与本文最直接的联系是把“来源”本身变成运营决策变量；关键迁移边界则是原模型近似假设来源文档不重叠，而仓库来源高度重叠。

多主体信息获取研究补充了配额视角。Moore et al.（1997）考察管理者为资源分配获取不同主体偏好的政策，把通信、推断和转换成本一并考虑。Wang et al.（2017）在 crowd labeling 中比较固定与动态质量保障，说明平均分配可能浪费预算，应将下一单位资源分给预期边际增益较大的对象。虽然检索来源既不是被管理的员工也不是标注者，这两项研究提供了可迁移的决策结构：有限资源应按条件边际贡献分配，而不是按来源平均分割。

资源配置还需要考虑风险。Mookerjee and Mannino（2000）指出，平均效用相近的专家系统可能具有不同损失分布，因此设计者需要均值—风险权衡。对 coding agent 而言，平均上下文质量较高的配置若偶尔完全漏掉关键来源，部署风险可能高于表现略低但稳定的全调用策略。本文据此同时报告平均 oracle regret、P95 regret 和配置校准，并让高不确定任务退化到保守配置；这不是把风险偏好归给 LLM，而是系统运营者可设置的人工制品参数。

这条 IS 研究链还解释了为什么本文不把“更多来源”预设为更好。信息经济学把搜索持续到边际收益不再覆盖边际成本（Stigler 1961）；异质数据库检索将用户认知与系统表示相连（Krishnan et al. 2001）；shopbot 研究显示，信息聚合的界面与组织方式会改变最终效用（Montgomery et al. 2004）。Mookerjee and Dos Santos（1993）、Mookerjee and Mannino（1997）及 Saar-Tsechansky and Provost（2007）进一步表明，减少预测误差或取得更多属性不必然改善终局决策。对 TMA 而言，这些研究的共同作用是限定效用标签：来源配置只能因改变预算包和代码行动而获得价值，不能因“调用了更先进的服务”得到先验奖励。

等待成本同样不能被压缩成平均查询时间。用户对网络等待的评价会随等待长度和情境变化，系统熟悉度与信息广度也会改变延迟容忍（Dellaert and Kahn 1999; Galletta et al. 2006）。虽然自动 coding agent 不具有相同主观等待感受，工程管线仍受并发、超时和 P95/P99 延迟约束。TMA 因而不迁移人类耐心构念，只迁移“服务收益与响应代价必须同时进入选择”的运营逻辑；主文分别报告均值、尾部时延和超时率，供实际部署自行设定权重。

最后，风险机制必须区分预测不确定性和真实配置损失。现代分类器的置信度可能失准，温度缩放和深度集成分别提供轻量校准与模型分歧估计（Guo et al. 2017; Lakshminarayanan et al. 2017）。本文不把某一校准方法写成理论贡献，而把它作为 TMA 的可替换实现：核心设计要求是让“个性化优势不足以置信”成为可测试的退化条件。校准误差、覆盖率和退化后的 P95 regret 必须共同改善；只有置信曲线变好但任务损失不变，不足以支持风险组件。

### 2.4 研究缺口

Voorberg et al.（2021）把信息任务与终局决定置于同一决策过程，进一步支持“信息的价值来自它如何改变后续行动”。来源交互也不只是回归式中的装饰项：互补性理论说明，一个行动的边际回报可能随另一行动是否存在而上升，而信息不完备下的选择阈值又会随剩余不确定性形成（Topkis 1998; Feinberg and Huber 1996）。TMA 只把这些关系操作化为代理—端点校准和可枚举配置的经验交互，不声称满足一般超模性质；若交互系数不能对应独特候选或终局增量，该部分必须删除。

现有研究留下三个缺口。第一，代码检索工作主要比较单一检索器或固定融合，缺少利用执行前任务—仓库特征进行来源—配额联合配置的方法。第二，传统分布式检索提供来源选择和等待模型，却没有处理代码候选的高度重叠、token 打包和程序结构互补。第三，选择性检索说明“是否检索”可学习，但尚未建立一个可在公开仓库 benchmark 上离线枚举反事实配置、评价净效用和尾部 regret 的轻量框架。

TMA 通过明确边界回应这些缺口。来源集合固定为 Lexical、Dense 和 Graph；配置器只选择是否调用及离散配额，不改变三个检索器内部算法。各来源完整排名缓存后，有限配置可以离线重放；所有候选统一交给冻结打包器，避免来源策略和上下文选择混淆。训练特征只来自检索前可见信息，oracle 配置只用于训练标签和评价上界。端到端效用昂贵时，金标准代理用于全量枚举，真实下游子样本用于校准代理偏差。

## 3. 研究定位、设计理由与方法挑战

本文研究的是一个设计科学问题：怎样把异质检索服务组织成随任务变化的、成本可控的信息获取系统。设计科学要求人工制品既有明确环境问题和设计理由，也经过严格、相关的评价并产出可复用知识（Hevner et al. 2004; Peffers et al. 2007; Gregor and Hevner 2013）。本文由分布式检索、信息获取政策和均值—风险理论导出四项设计理由，再把它们情境化为 coding agent 可观察的输入、配置行动和评价量（Hong et al. 2014）。

这一写法与理论驱动的深度学习 IS 研究具有共同规范：先从外部理论识别容易被常规模型忽略的过程或关系，再把它们逐项转成模型组件，最后用中间机制、增量实验与消融判断理论是否真正贡献了预测或决策价值（Chen et al. 2023, 2024）。本文不借用顾客注意或语音响应的实体内容，也不把神经网络复杂度本身当作贡献；可迁移的是“构念—操作化—组件—专门证据”的追踪性。TMA 的四个设计理由因此都必须在表 1 中找到实现和实验去向。

从过程看，来源配置发生在候选返回之前，但其价值只能在候选打包和下游使用之后观察。若仅以来源独立 Recall 训练配置器，系统无法感知跨来源重复；若直接用每个任务的测试通过率训练，又需要为所有配置反复运行昂贵且随机的 agent。本文因此采用两级效用：全量任务用金标准覆盖、冗余、结构覆盖和成本形成检索代理效用；分层子样本用固定下游模型得到端到端效用，用于校准代理和限制结论。

从层次看，任务特征为来源提供先验，来源组合决定候选供给，候选交集决定真实互补，固定打包器决定哪些独特内容进入 prompt。TMA 在检索前不能看到真实返回交集，因此必须从历史训练任务中学习“在何种特征下某种组合通常产生何种净效用”。这种预测本身具有不确定性，因而人工制品不仅要给出最优点估计，还要识别何时不应相信个性化配置。

### 3.1 任务条件下的来源异质性

分布式检索服务器在结果质量和响应时间上存在异质性，最优查询集合因查询而变（Hosanagar 2011）。代码来源的异质性具有更具体的可观察基础：标识符和路径适合词法匹配，自然语言改写适合稠密表示，跨模块依赖适合结构扩展。若所有来源的相对能力在任务间固定，全局最佳配置已经足够；只有条件差异稳定存在，任务级配置才有价值。

由此产生第一个方法挑战：TMA 只能使用执行前特征，不能用未来补丁、金标准文件或某来源实际是否命中作为输入。它需要从 query 中提取标识符比例、路径/异常/测试模式、词汇集中度和语义不确定性，从 base commit 提取仓库语言、规模、模块化和图解析覆盖，并控制特征成本。专门评价将比较 Global Best 与 TMA，并按这些条件报告来源胜率和配置份额；若两者无显著差异，个性化配置的理论前提不成立。

### 3.2 来源互补与结果重叠

服务组合只有在新增来源提供独特、可用信息时才产生边际价值（Roussinov and Chau 2008）。在代码仓库中，Lexical 与 Dense 可能同时返回包含 query 标识符的实现，Graph 又可能在 Lexical 已找到定义后才有价值。来源独立分数相加会把重复命中重复计价，忽略打包器能否保留独特证据。

第二个挑战是，检索前无法直接观察本次任务的结果交集。TMA 因而在离线枚举标签中以配置经过固定打包器后的效用为目标，并在条件模型中加入来源交互。对一个配置的价值估计不是各来源预测值的机械相加，而允许 Lexical×Dense、Lexical×Graph、Dense×Graph 和三者联合项随任务特征变化。专门评价包括去交互消融、独特文件/结构单元贡献和配置反事实排序。

### 3.3 获取、处理与等待成本

Hosanagar（2011）同时考虑查询费用和等待成本，Moore et al.（1997）还把通信、计算和转换纳入信息获取政策。对应到仓库检索，来源成本至少包括索引摊销、在线查询、候选读取/去重、图遍历、打包 token 和下游推理。只以最终 prompt token 计费会低估那些返回大量重复候选的来源；只以在线延迟计费又会忽略离线索引和基础设施。

第三个挑战是成本量纲与部署情境不同。本文分别报告不含离线索引的在线成本和包含摊销的总拥有成本，不用一个任意权重掩盖组成项。TMA 的主目标使用预注册的标准化成本权重，并通过一组权重网格绘制质量—成本帕累托前沿。专门消融去除成本项，检验无成本配置是否只通过更多调用改善质量却降低净效用。

### 3.4 配置不确定性与尾部风险

均值最优策略可能在少数任务上造成高损失（Mookerjee and Mannino 2000）。ARB 规模有限且仓库分布不均，高容量路由器可能学习仓库身份而非一般条件。若 TMA 错误地不给唯一关键来源分配预算，损失可能远大于多调用一次的成本。配置器因而必须表达预测不确定性，并允许运营者设置风险容忍。

第四个挑战是避免“保守”退化成永远全调用。本文让每个配置输出均值和不确定区间，以风险调整效用选择；只有当个性化最优配置相对 Global Best 的下置信优势不足或任务超出训练支持时才退化。评价同时报告平均和 P95 oracle regret、校准误差、退化比例与退化后的净效用。若退化频率过高且没有提高尾部表现，说明不确定性机制没有实用价值。

**表 1  理论命题、设计挑战与 TMA 组件的对应**

| 层次 | 理论/经验依据 | 可观察指标 | 方法挑战 | TMA 组件 | 专门证据 |
|---|---|---|---|---|---|
| 任务 | 来源质量异质性 | 标识符、错误栈、语义重合、图可解析性 | 不能使用未来命中 | 执行前条件特征 | Global Best 对比、条件胜率 |
| 组合 | 信息服务互补 | 历史独特文件、结构单元、打包后增量 | 检索前未知真实交集 | 来源交互效用模型 | 去交互消融、配置排序 |
| 来源 | 有成本获取与等待 | 查询、索引摊销、候选处理、P95 时延 | 多种成本量纲 | 离散配额与成本调整效用 | 帕累托前沿、去成本消融 |
| 决策 | 均值—风险权衡 | 不确定区间、平均/P95 regret | 个性化错配可能灾难 | 下置信选择与保守退化 | 校准、尾部 regret、退化消融 |

综上，本文不是把现有检索器包装成一个路由网络，而是将来源异质、互补、成本和风险转化为彼此可追踪的设计约束。来源与配额的条件配置，以及围绕该配置建立的反事实枚举、净效用评价和风险控制，构成 TMA 的设计科学贡献。

## 4. 所提出的方法

### 4.1 TMA 总览

对任务 $x=(q,R,e)$，可用检索来源集合记为 $\mathcal{M}=\{L,D,G\}$，分别对应 Lexical、Dense 和 Graph。每个来源具有离散配额集合 $\mathcal{B}_m$，例如 $\{0,8,32,128\}$ 个候选或等价 token 档位。配置 $b=(b_L,b_D,b_G)$ 决定调用哪些来源以及从各自冻结排名前缀取得多少候选。TMA 不修改来源内部算法，也不在返回后重新选择来源；所有候选合并、去重后交给冻结上下文选择器 $A_{\mathrm{pack}}$，在上下文预算 $B^{\mathrm{ctx}}$ 下产生最终包。

图 1（待绘制）包含离线和在线两部分。离线阶段对每个训练任务运行三种来源一次，缓存完整排名及成本；枚举所有满足检索预算的配置，重放排名前缀，经统一打包器计算代理效用，并在端到端子样本上运行固定代码模型校准代理。随后用执行前任务—仓库特征学习每个配置的条件效用和不确定性。在线阶段只抽取这些低成本特征，选择风险调整效用最高的配置；若任务超出训练支持或优势不确定，则退化到 Global Best。执行所选来源后，候选由同一打包器生成 prompt。

选择小规模、可枚举行动空间是一项有意设计。若每个来源有四个配额档位，理论上只有 $4^3-1=63$ 个非空配置，检索预算约束会进一步减少。与任意逐步工具策略相比，这一空间允许为每个训练任务观察全部配置的反事实结果，不需要从 bandit 日志估计未采取行动的回报，也不需要大规模强化学习。首版研究因而可以在公开 benchmark 上真实实施，并清楚区分标签生成成本与在线推理成本。

### 4.2 检索来源与结果对齐

#### 4.2.1 Lexical 来源

Lexical 使用冻结 BM25 索引，文档单位与 benchmark 粒度一致。查询由原始 issue/补全前缀、路径、标识符和异常帧组成；代码分词保留 camelCase、snake_case 拆分前后的 token。BM25 参数、停用规则和索引版本在训练前冻结（Robertson and Zaragoza 2009）。其在线成本包括查询时间和读取 top-$b_L$ 候选的时间，不把一次性构建索引完全忽略，而另报告按预期任务量摊销的成本。

#### 4.2.2 Dense 来源

Dense 使用公开代码—文本表示模型 `[待确定模型及引用]` 将查询和候选映射到向量空间，并以固定近似最近邻配置检索。候选向量在 base commit 级缓存，查询向量在线计算。为了公平，Dense 与 Lexical 使用相同候选切分；若某模型要求不同最大长度，超长项的切分规则在验证集冻结。成本记录编码、索引搜索和候选读取，显存与索引大小在附录报告。

#### 4.2.3 Graph 来源

Graph 在静态关系图上从 query 匹配到的路径、标识符、异常帧和锚点文件出发，按定义—引用、调用、导入、配置和测试关系执行限定跳数扩展。节点以路径/符号/跨度映射回与另两来源相同的候选单位。其排名由种子相关性、关系类型和图距离的冻结组合给出。解析失败时来源返回空结果并记录失败成本；TMA 可在执行前使用仓库图覆盖率，但不能使用“本任务是否最终命中”的未来信息。

#### 4.2.4 跨来源去重与打包

各来源结果按仓库相对路径和行区间对齐。完全相同候选合并来源标签；高度重叠跨度按冻结规则合并，并保留其在各来源的名次。打包器主版本使用论文一所定义的 SBCS，但论文二的结论不依赖它必须优于其他算法：稳健性实验会更换为 Rank-Truncate 和 MMR。关键约束是同一实验中的所有来源配置共享同一个打包器，因而 TMA 的增量不能来自配置间不同的上下文选择。

### 4.3 配置空间与净效用

#### 4.3.1 可行配置

来源 $m$ 在配额 $b_m$ 下的获取成本为 $c_m^{\mathrm{ret}}(b_m)$。可行配置集合为

\[
\mathcal{A}_x=\left\{b\in\prod_{m\in\mathcal M}\mathcal B_m:
\sum_m c_m^{\mathrm{ret}}(b_m)\le B_x^{\mathrm{ret}},
\ b\ne \mathbf 0\right\}.
\tag{1}
\]

若任务允许不检索，则另加入 $\mathbf 0$。这里 $B_x^{\mathrm{ret}}$ 控制候选生成资源，$B_x^{\mathrm{ctx}}$ 控制最终 prompt；二者不能混用。一个来源可以返回大量候选但最终只有少量进入包，其获取成本仍然发生。

给定配置 $b$，合并候选为 $V_x(b)$，最终上下文为

\[
S_x(b)=A_{\mathrm{pack}}\big(q,V_x(b),B_x^{\mathrm{ctx}}\big).
\tag{2}
\]

#### 4.3.2 检索代理效用

对存在金标准 $Y_x$ 的任务，定义代理质量

\[
Q_x(b)=\theta_1\operatorname{BCY}(S_x(b),Y_x)
+\theta_2\operatorname{StructCov}(S_x(b),Y_x)
-\theta_3\operatorname{Redundancy}(S_x(b)),
\tag{3}
\]

其中指标按训练集尺度归一，$\theta$ 只在验证仓库选择。若 benchmark 不提供结构金标准，第二项不进入标签；不得用研究者自行推断的关系冒充人工金标准。no-gold 任务的 $Q_x$ 以正确空返回或低错误检索为目标，与普通 Recall 分开。

配置的代理净效用为

\[
\widetilde J_x(b)=Q_x(b)
-\lambda_{\mathrm{ret}}C_x^{\mathrm{ret}}(b)
-\lambda_{\mathrm{ctx}}C_x^{\mathrm{ctx}}(S_x(b))
-\lambda_{\mathrm{lat}}C_x^{\mathrm{lat}}(b).
\tag{4}
\]

成本既报告原始单位，也在式（4）中按验证集稳健尺度标准化。主论文预注册一组业务中性权重，并通过权重网格展示帕累托前沿，避免只选择最有利于 TMA 的 $\lambda$。

#### 4.3.3 端到端效用与代理校准

对端到端子样本，在冻结下游模型与环境中运行上下文 $S_x(b)$，得到任务结果 $U_x^{\mathrm{task}}(b)$，例如补全 EM、定位成功、测试通过或 resolved。真实净效用定义为

\[
J_x(b)=U_x^{\mathrm{task}}(b)
-\lambda_{\mathrm{ret}}C_x^{\mathrm{ret}}(b)
-\lambda_{\mathrm{ctx}}C_x^{\mathrm{ctx}}(S_x(b))
-\lambda_{\mathrm{lat}}C_x^{\mathrm{lat}}(b)
-\lambda_{\mathrm{llm}}C_x^{\mathrm{llm}}(b).
\tag{5}
\]

全量配置都运行真实修复成本过高。本文不把式（4）直接等同式（5），而在分层端到端样本上拟合单调校准 $g(\widetilde J,\psi_x)$，并报告代理对真实效用的排序相关、校准误差和失败类别。若代理相关性不足，TMA 的主要结论只能停留在检索层，不能用代理标签声称提高修复率。

### 4.4 执行前条件特征

TMA 的输入 $\phi_x$ 只包含配置执行前可见量：

\[
\phi_x=(\phi_x^{q},\phi_x^{R},\phi_x^{\mathrm{anchor}},\phi_x^{\mathrm{cost}}).
\tag{6}
\]

$\phi_x^{q}$ 包括 query 长度、代码标识符比例、路径/函数/类模式数、异常帧、测试名、自然语言比例、词项稀有度和语义集中度；$\phi_x^{R}$ 包括主要语言、文件/符号数、平均模块度、图解析覆盖、平均调用度和测试—实现比；$\phi_x^{\mathrm{anchor}}$ 包括锚点是否存在、锚点与 query 词汇重合以及锚点在图中的局部连接；$\phi_x^{\mathrm{cost}}$ 包括可用索引、预估队列和预算档位。

高成本探测特征不进入主模型。例如，先对所有来源做小额检索再用真实交集路由，可能改善配置，却已支付调用成本，并把研究变成两阶段在线策略。该“probe-then-route”仅作为扩展基线，必须把探测成本完整计入。主结论限定为无探测的 ex ante 配置。

所有连续特征在训练仓库上标准化，仓库身份、文件名哈希和 benchmark 子集标签不得作为特征。对高维文本不直接使用可记忆仓库的 LLM embedding；若加入 query embedding，只在严格仓库外划分上评价并与浅层可解释特征比较。

### 4.5 条件效用、来源交互与风险调整

#### 4.5.1 条件效用模型

对每个配置 $b\in\mathcal A$，TMA 估计

\[
\widehat\mu_x(b)=f(\phi_x,b).
\tag{7}
\]

主模型采用梯度提升树或广义加性模型 `[由验证集确定但预先限定候选]`，因为样本规模不足以支持高容量神经路由器。配置以来源是否启用、配额档位和总预算编码；模型训练目标可以是预测 $\widetilde J_x(b)$ 的回归损失，也可以是同任务配置对的排序损失。主指标以 oracle regret 为准，因而优先选择在验证仓库上 regret 较低且校准较好的版本。

#### 4.5.2 来源交互

令 $z_m(b)$ 表示来源 $m$ 的配额编码。一个可解释的效用分解为

\[
\widehat\mu_x(b)=\beta_0+\sum_m f_m(\phi_x,z_m)
+\sum_{m<n}f_{mn}(\phi_x,z_m,z_n)
+f_{LDG}(\phi_x,z_L,z_D,z_G).
\tag{8}
\]

主效应表示来源在任务条件下的独立价值，二阶和三阶项允许互补或重叠。为了控制过拟合，主版本先比较无交互、仅二阶交互和完整交互，按仓库级交叉验证选择；不因完整模型理论上更灵活就默认采用。

#### 4.5.3 不确定性与保守退化

通过仓库 bootstrap、分位回归或 conformal 校准 `[待验证后选定]` 得到每个配置的不确定性 $\widehat\sigma_x(b)$。风险调整分数为

\[
R_x(b)=\widehat\mu_x(b)-\beta\widehat\sigma_x(b),
\tag{9}
\]

其中 $\beta\ge0$ 由部署风险容忍决定。令 $b^{GB}$ 为训练仓库上的 Global Best。在线选择

\[
b_x^*=\begin{cases}
\arg\max_{b\in\mathcal A_x}R_x(b), &
R_x(\arg\max_b R_x(b))-R_x(b^{GB})>\tau
\text{ 且 }x\text{ 在支持域内},\\
b^{GB}, & \text{其他情况。}
\end{cases}
\tag{10}
\]

$\tau$ 是个性化配置必须超过的最小可信优势。支持域用训练特征距离或 conformal 非一致分数识别。若 Global Best 本身在高风险部署中不足，可把全来源低配额设为保守基线，但必须在训练/验证阶段确定。

### 4.6 离线训练与在线执行

```text
离线输入：训练任务 X，三个冻结来源 M，配额集合 B，固定打包器 A_pack
离线输出：效用模型 f，不确定性模型 s，保守配置 b_GB

1  对每个仓库构建并冻结三类索引
2  对每个训练任务分别运行 L/D/G 到最大配额，缓存排名、时延与成本
3  枚举每个可行配置 b，用缓存前缀合并候选并运行同一 A_pack
4  计算代理净效用；在预注册子样本上运行固定下游模型得到端到端效用
5  按仓库划分拟合代理校准、条件效用与不确定性
6  在验证仓库选择模型容量、beta、tau 与 Global Best

在线输入：新任务 x
1  只提取执行前特征 phi_x
2  对所有可行配置预测风险调整效用
3  若可信优势充分则选个性化配置，否则退化到 b_GB
4  只执行所选来源与配额，统一打包并返回上下文
5  记录预测、实际成本、来源贡献与退化原因
```

在线预测复杂度为 $O(|\mathcal A|)$，在三来源小行动空间中可忽略；主要成本来自被选择的来源。离线枚举不需要重复运行检索器，只重放缓存前缀和打包器；端到端配置仍昂贵，因此只在分层子样本执行。本文将分别报告离线标签生成资源、训练资源和在线每任务资源，防止把昂贵离线过程从总成本中隐藏。

## 5. 实证评价

### 5.1 数据

主检索数据使用 ARB。其正检索子任务包含不同工作流信号，no-gold 子任务允许检验来源配置器是否在无仓库证据时仍盲目调用全部服务（Qin and Xie 2026）。CodeRAG-Bench 用于多检索器接口和跨数据源外部验证；本文只选其中能明确映射为仓库候选且许可证允许的任务，不把教程、Stack Overflow 与仓库内部代码混为同一种来源（Wang et al. 2025）。

ContextBench 提供文件、代码块或行级金标准和过程日志，适合分析不同来源的独特贡献（Li et al. 2026）。RepoBench-R/P 与 CrossCodeEval 用于快速开发、语言外验证和下游补全（Ding et al. 2023; Liu et al. 2024）。算法冻结后，在 SWE-bench Verified 或等价可执行子样本上运行固定 Agentless/最小 agent `[待确定]`，只验证来源配置的任务增量，不重新调参（Jimenez et al. 2024; Xia et al. 2025）。

划分按仓库分组，并在训练、验证和测试中保持任务类型分布。若样本量不足以同时实现语言和仓库完全分层，主优先级为仓库隔离，语言外推另设严格子实验。所有索引从 base commit 构造，未来补丁、金标准和测试结果不进入特征。数据版本、解析成功率、缺失任务和每种来源的失败率完整报告。

### 5.2 主要实验

实证部分包含四项主实验。实验 1 在固定打包器和下游模型下比较 TMA 与固定策略的净任务效用。实验 2 检验条件效用估计是否能正确排序配置、逼近每任务 oracle 并保持校准。实验 3 建立 All+RRF/All+SBCS 这一全来源强基线，检验个性化是否在不牺牲关键证据的情况下节省成本。实验 4 把 TMA 与不同打包器组合，验证来源配置的增量是否独立于 SBCS。探索性分析回答 RQ1，消融归因四项组件。

比较策略包括：Lexical-only、Dense-only、Graph-only、Equal Split、Global Best、All+RRF、All+SBCS、基于标识符/错误栈的 Rule-based、Probe-then-route、TMA-NoInteraction、TMA-NoGuard、TMA，以及每任务 Oracle Config。Oracle 使用测试结果选配置，只作上界；Probe-then-route 的探测成本完整计入。

主要指标为：端到端任务效用、代理净效用、配置 Top-1 命中、配置排序 Spearman、平均/P95 oracle regret、校准误差、来源调用率、候选独特率、P50/P95 时延、总 token、超预算率和每成功任务成本。定义 regret 为

\[
\operatorname{Regret}_x(\pi)=J_x(b_x^{oracle})-J_x(\pi(x)).
\tag{11}
\]

若只具代理标签，则明确写作 proxy regret。统计推断按仓库聚类 bootstrap，比较同任务配对差异并做多重校正。配置准确率不作为唯一主指标，因为多个配置效用可能近似；regret 与成本—质量前沿更能反映错误严重性。

### 5.3 实验结果

> 以下均为结果写作模板，不是发现。

#### 5.3.1 实验 1：多源配置的净任务效用

**表 2  多源策略在固定打包器上的表现 `[待实验]`**

| 策略 | ARB BCY@8K | Context span recall | 下游效用 | 检索 P95 ms | 每成功成本 | 净效用 |
|---|---:|---:|---:|---:|---:|---:|
| Lexical-only | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| Dense-only | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| Graph-only | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| Equal Split | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| Global Best | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| TMA | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |

结果首先报告 TMA 相对每个固定策略的差异、置信区间和校正后显著性 `[待实验]`。然后解释表现来自质量、成本还是二者共同变化。若 TMA 只减少时延而任务质量持平，其贡献是效率配置；若只提高 Recall 却没有提高下游或净效用，不能声称任务价值；若平均净效用提高但 P95 regret 变差，则必须进入风险分析而不能以平均数收束。

#### 5.3.2 实验 2：配置排序、oracle regret 与校准

**表 3  条件效用预测质量 `[待实验]`**

| 方法 | 排序相关 | Top-1 | Mean proxy regret | P95 proxy regret | 端到端 regret | ECE/校准误差 |
|---|---:|---:|---:|---:|---:|---:|
| Global Best | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | — |
| Rule-based | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | — |
| TMA-NoInteraction | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| TMA-NoGuard | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| TMA | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |

这一实验排除“只是总体平均配置碰巧较好”的解释。TMA 必须在未见仓库上区分配置相对效用，并在效用差距大时避免严重错配。若 Top-1 不高但 regret 低，说明多个配置近似等价，系统仍可用；若排序相关高而端到端 regret 高，说明代理效用没有捕捉真实任务价值。代理—端点偏差将决定结论能否从检索配置提升到 coding-agent 任务配置。

#### 5.3.3 实验 3：全来源强基线与成本边界

固定调用全部来源是保守而有竞争力的策略。它可能取得较高覆盖，却支付最大查询与处理成本。实验 3 比较 All+RRF、All+SBCS、TMA 和 Oracle，并在不同 $\lambda$ 和服务负载下绘制帕累托前沿。

**表 4  全来源策略与 TMA `[待实验]`**

| 策略 | Gold coverage | 独特候选率 | 下游效用 | 查询成本 | P95 时延 | 净效用 |
|---|---:|---:|---:|---:|---:|---:|
| All + RRF | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| All + SBCS | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| TMA + SBCS | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| Oracle Config | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |

若 TMA 接近 All 的任务质量但成本较低，说明条件配置在保守基线之上有实际价值。若 All 始终帕累托占优，则任务特征或行动空间不足，主张应收缩为“全来源低配额是当前更优设计”。若 TMA 在平均条件占优但困难多跳任务退化，需要提高风险缓冲或保留 Graph 最低配额。

#### 5.3.4 实验 4：相对于固定上下文打包器的增量

为确认 TMA 不是只适配 SBCS，分别在 Rank-Truncate、MMR 和 SBCS 三种固定打包器下比较 Global Best 与 TMA。

**表 5  来源配置与打包器的交叉实验 `[待实验]`**

| 打包器 | 固定来源净效用 | TMA 净效用 | 增量 | 端到端增量 | 来源×打包交互 |
|---|---:|---:|---:|---:|---:|
| Rank-Truncate | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| MMR | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| SBCS | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |

如果 TMA 在三个打包器上方向一致，来源配置可以作为独立人工制品；若只与 SBCS 组合有效，则应把贡献写成联合设计，并分析 SBCS 是否更能保留来源独特证据。该实验也检验 Roussinov and Chau（2008）式服务组合是否必须与下游整合机制共同评价。

### 5.4 探索性分析

训练后的 TMA 提供任务特征、配置预测、来源份额、不确定性和退化原因。本文用这些记录回答 RQ1，但明确把它们解释为算法在数据上学得的条件关联，而不是开发者或 LLM 的心理偏好。

#### 5.4.1 词法来源的条件价值

按 query 标识符比例、路径匹配和异常栈存在分组，比较 Lexical 配额、独特金标准命中和下游增量。若精确代码信号高时 Lexical 获得更多配额且产生独特命中，这与理论预期一致；若只是配额变化而结果没有变化，则不能形成来源价值知识 `[待实验]`。

#### 5.4.2 稠密来源的条件价值

按自然语言比例、query—仓库词汇重合和语义集中度分组，检验 Dense 是否在低词汇重合任务上提供更大增量。还要控制仓库规模和语言，因为 embedding 表现可能受训练语料覆盖混杂。不同编码器下条件规律是否稳定作为外部验证 `[待实验]`。

#### 5.4.3 结构来源的条件价值

按图解析覆盖、锚点局部连接、多文件金标准距离和任务类型分析 Graph。若结构来源只在解析率高的少数语言有效，结论必须限定；若高连接仓库导致大量重复或离题候选，应分析配额是否自动下降。Graph 的高成本只有在补齐独特结构证据时才被解释为合理 `[待实验]`。

#### 5.4.4 互补、重叠与退化

绘制三种来源两两交集、SBCS 最终保留比例和条件交互效应。TMA 的交互项若为负，应能对应较高结果重叠；若为正，应对应独特文件或结构单元。随后比较高不确定任务和正常任务的特征，报告退化是否集中在未见语言、极大仓库或解析失败情形，以及退化是否实际降低 P95 regret `[待实验]`。

### 5.5 消融分析

消融依次移除任务特征、仓库结构特征、来源交互、成本项、不确定性和保守退化。另比较代理效用训练与端到端校准后训练，量化代理偏差。

**表 6  TMA 组件消融 `[待实验]`**

| 变体 | Mean regret | P95 regret | 下游效用 | 检索成本 | 校准误差 |
|---|---:|---:|---:|---:|---:|
| 无任务特征 | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| 无仓库特征 | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| 无来源交互 | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| 无成本 | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| 无守护退化 | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| 完整 TMA | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |

若移除交互几乎不改变配置和结果，说明来源重叠无需复杂建模；若移除成本提高质量却使净效用下降，支持成本设计；若移除守护只改善平均数但恶化 P95，支持风险控制。任何组件只有在对应中间机制和终局结果同时改变时，才被写成必要贡献。

## 6. 贡献与启示

本文的第一项潜在贡献是把多源仓库检索概念化为任务条件下的信息服务配置，而非固定流水线。已有代码研究分别证明词法、表示和结构信号有用，本文进一步区分任务、来源组合、单一来源和候选结果四个层次，并把来源价值定义为相对于其他来源、经过统一打包后的净贡献。这一概念化把分布式信息检索中的服务器选择扩展到高度重叠、具有程序关系且受 token 预算约束的代码环境。

第二项潜在贡献是 TMA 这一设计科学制品。它用小而可枚举的行动空间取得完整配置反事实，以代理—端点两级效用处理计算约束，以来源交互处理重叠，以不确定性和保守退化处理尾部风险。人工制品的每个组件都对应独立评价，而不是把复杂路由器的平均涨点作为唯一证据。若结果获得支持，TMA 可与不同检索器、打包器和下游 agent 组合，形成可复用的来源配置模式。

第三项潜在贡献是条件性经验知识。标识符、词汇重合、错误栈、图解析覆盖、跨文件距离和仓库规模是否稳定改变来源价值，将由分层结果和消融共同决定。本文不会先验宣布“有标识符就用 BM25”或“多跳就用图”；只有在未见仓库和替代实现上重复出现的规律才写入结论。若条件关系不稳定，负结果同样说明固定保守配置可能优于任务级路由。

实践上，coding-agent 开发者应把来源调用、结果融合和上下文打包分成可观测层，并为每个来源记录独特贡献和全链路成本。检索服务提供者应暴露稳定排名、时延、失败和索引版本，而不只返回分数。企业部署者可以根据服务负载、隐私和失败代价设置 $\lambda$、$\beta$ 与 $\tau$，但应查看帕累托前沿而非照搬论文单点。benchmark 维护者则应提供统一候选接口、no-gold 情形和可重放排名，以支持来源配置而非只支持单检索器排名。

## 7. 结论

本文研究 coding agent 应从哪些仓库检索来源取得多少信息。基于分布式检索、信息获取政策和均值—风险权衡，本文把来源价值分解为任务适配、组合互补、获取成本和配置风险，并提出 TMA。研究设计利用成熟公开 benchmark、可缓存检索器和有限配置枚举生成训练与评价数据，再以固定打包器和下游模型识别来源配置的独立增量；实际结果为 `[待实验]`。

本研究有四类边界。第一，首版只含 Lexical、Dense 和 Graph 三类来源，不能代表轨迹记忆、外部文档、动态执行或人工协作来源；新增来源会指数扩大枚举空间。第二，代理效用依赖 benchmark 金标准，可能与真实修复效用不一致，端到端校准只能降低而不能消除该偏差。第三，来源实现、索引硬件、服务负载和成本权重具有部署情境性；某一实验中的最优配额不能直接移植。第四，TMA 在检索前一次性配置，不利用来源返回后的实际交集更新策略；这是与序贯停止研究保持清晰边界的有意限制。

未来研究可以研究带小额探测的两阶段配置、来源不可用时的鲁棒优化、受隐私和许可证约束的多目标路由，以及配置策略随仓库演化的在线更新。但这些扩展只有在保留全链路成本和真实反事实评价时，才构成信息获取决策而非单纯增加 agent 复杂度。

## 参考文献

Aslam, J. A., & Montague, M. (2001). Models for metasearch. *Proceedings of SIGIR 2001*, 276–284.

Callan, J. P., Lu, Z., & Croft, W. B. (1995). Searching distributed collections with inference networks. *Proceedings of SIGIR 1995*, 21–28.

Chen, Z., Tang, R., Deng, G., Wu, F., Wu, J., Jiang, Z., Prasanna, V., Cohan, A., & Wang, X. (2025). LocAgent: Graph-guided LLM agents for code localization. *Proceedings of ACL 2025*, 8697–8727. https://doi.org/10.18653/v1/2025.acl-long.426

Cheng, W., Wu, Y., & Hu, W. (2024). Dataflow-guided retrieval augmentation for repository-level code completion. *Proceedings of ACL 2024*, 7957–7977. https://doi.org/10.18653/v1/2024.acl-long.431

Cormack, G. V., Clarke, C. L. A., & Buettcher, S. (2009). Reciprocal rank fusion outperforms Condorcet and individual rank learning methods. *Proceedings of SIGIR 2009*, 758–759.

Ding, Y., Wang, Z., Ahmad, W. U., Ding, H., Tan, M., Jain, N., Ramanathan, M. K., Nallapati, R., Bhatia, P., Roth, D., & Xiang, B. (2023). CrossCodeEval: A diverse and multilingual benchmark for cross-file code completion. *Advances in Neural Information Processing Systems, 36*, Datasets and Benchmarks Track.

Ding, Y., Wang, Z., Ahmad, W. U., Ramanathan, M. K., Nallapati, R., Bhatia, P., Roth, D., & Xiang, B. (2024). CoCoMIC: Code completion by jointly modeling in-file and cross-file context. *Proceedings of LREC-COLING 2024*, 3433–3445.

Feng, Z., Guo, D., Tang, D., Duan, N., Feng, X., Gong, M., Shou, L., Qin, B., Liu, T., Jiang, D., & Zhou, M. (2020). CodeBERT: A pre-trained model for programming and natural languages. *Findings of EMNLP 2020*, 1536–1547.

Gregor, S., & Hevner, A. R. (2013). Positioning and presenting design science research for maximum impact. *MIS Quarterly, 37*(2), 337–355.

Guo, D., Ren, S., Lu, S., Feng, Z., Tang, D., Liu, S., Zhou, L., Duan, N., Svyatkovskiy, A., Fu, S., Tufano, M., Deng, S. K., Clement, C., Drain, D., Sundaresan, N., Yin, J., Jiang, D., & Zhou, M. (2021). GraphCodeBERT: Pre-training code representations with data flow. *International Conference on Learning Representations*.

Guo, D., Lu, S., Duan, N., Wang, Y., Zhou, M., & Yin, J. (2022). UniXcoder: Unified cross-modal pre-training for code representation. *Proceedings of ACL 2022*, 7212–7225.

Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. *MIS Quarterly, 28*(1), 75–105.

Hong, W., Chan, F. K. Y., Thong, J. Y. L., Chasalow, L. C., & Dhillon, G. (2014). A framework and guidelines for context-specific theorizing in information systems research. *Information Systems Research, 25*(1), 111–136.

Hosanagar, K. (2005). A utility theoretic approach to determining optimal wait times in distributed information retrieval. *Proceedings of SIGIR 2005*.

Hosanagar, K. (2011). Usercentric operational decision making in distributed information retrieval. *Information Systems Research, 22*(4), 739–755. https://doi.org/10.1287/isre.1100.0287

Jimenez, C. E., Yang, J., Wettig, A., Yao, S., Pei, K., Press, O., & Narasimhan, K. R. (2024). SWE-bench: Can language models resolve real-world GitHub issues? *International Conference on Learning Representations*.

Li, H., Zhu, L., Zhang, B., Feng, R., Wang, J., Pan, Y., Barr, E. T., Sarro, F., Chu, Z., & Ye, H. (2026). ContextBench: A benchmark for context retrieval in coding agents. *arXiv preprint arXiv:2602.05892*.

Liu, T., Xu, C., & McAuley, J. (2024). RepoBench: Benchmarking repository-level code auto-completion systems. *International Conference on Learning Representations*.

Mookerjee, V. S., & Mannino, M. V. (2000). Mean-risk trade-offs in inductive expert systems. *Information Systems Research, 11*(2), 137–153.

Moore, J. C., Rao, H. R., Whinston, A. B., Nam, K., & Raghu, T. S. (1997). Information acquisition policies for resource allocation among multiple agents. *Information Systems Research, 8*(2), 151–170. https://doi.org/10.1287/isre.8.2.151

Ouyang, S., Yu, W., Ma, K., Xiao, Z., Zhang, Z., Jia, M., Han, J., Zhang, H., & Yu, D. (2025). RepoGraph: Enhancing AI software engineering with repository-level code graph. *International Conference on Learning Representations*.

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems, 24*(3), 45–77.

Qin, B., & Xie, Y. (2026). Agent Retrieval Bench: Evaluating repository context retrieval for coding agents. *arXiv preprint arXiv:2607.24882*.

Robertson, S., & Zaragoza, H. (2009). The probabilistic relevance framework: BM25 and beyond. *Foundations and Trends in Information Retrieval, 3*(4), 333–389.

Roussinov, D., & Chau, M. (2008). Combining information seeking services into a meta supply chain of facts. *Journal of the Association for Information Systems, 9*(3/4). https://doi.org/10.17705/1jais.00154

Wang, J., Ipeirotis, P. G., & Provost, F. (2017). Cost-effective quality assurance in crowd labeling. *Information Systems Research, 28*(1), 137–158. https://doi.org/10.1287/isre.2016.0661

Wang, Z. Z., Asai, A., Yu, X. V., Xu, F. F., Xie, Y., Neubig, G., & Fried, D. (2025). CodeRAG-Bench: Can retrieval augment code generation? *Findings of NAACL 2025*, 3199–3214. https://doi.org/10.18653/v1/2025.findings-naacl.176

Wu, D., Ahmad, W. U., Zhang, D., Ramanathan, M. K., & Ma, X. (2024). Repoformer: Selective retrieval for repository-level code completion. *Proceedings of ICML 2024*, 53270–53290.

Xia, C. S., Deng, Y., Dunn, S., & Zhang, L. (2025). Agentless: Demystifying LLM-based software engineering agents. *Proceedings of the ACM on Software Engineering, 2*(FSE).

Zhang, F., Chen, B., Zhang, Y., Keung, J., Liu, J., Zan, D., Mao, Y., Lou, J.-G., & Chen, W. (2023). RepoCoder: Repository-level code completion through iterative retrieval and generation. *Proceedings of EMNLP 2023*, 2471–2484.

Avrahami, T. T., Yao, L., Si, L., & Callan, J. (2006). The FedLemur project: Federated search in the real world. *Journal of the American Society for Information Science and Technology, 57*(3), 347–358.

Chen, G., Huang, L., Xiao, S., Zhang, C., & Zhao, H. (2024). Attending to customer attention: A novel deep learning method for leveraging multimodal online reviews to enhance sales prediction. *Information Systems Research, 35*(2), 829–849. https://doi.org/10.1287/isre.2021.0292

Chen, G., Xiao, S., Zhang, C., & Zhao, H. (2023). A theory-driven deep learning method for voice chat-based customer response prediction. *Information Systems Research, 34*(4), 1513–1532. https://doi.org/10.1287/isre.2022.1196

Dellaert, B. G. C., & Kahn, B. E. (1999). How tolerable is delay? Consumers' evaluations of Internet Web sites after waiting. *Journal of Interactive Marketing, 13*(1), 41–54.

Fuhr, N. (1999). A decision-theoretic approach to database selection in networked IR. *ACM Transactions on Information Systems, 17*(3), 229–249.

Galletta, D. F., Henry, R. M., McCoy, S., & Polak, P. (2006). When the wait isn't so bad: The interacting effects of Web site delay, familiarity, and breadth. *Information Systems Research, 17*(1), 20–37.

Gravano, L., & García-Molina, H. (1995). Generalizing GlOSS to vector-space databases and broker hierarchies. *Proceedings of VLDB 1995*.

Guo, C., Pleiss, G., Sun, Y., & Weinberger, K. Q. (2017). On calibration of modern neural networks. *Proceedings of ICML 2017*, 1321–1330.

Guo, J., Wang, C., Xu, X., Su, Z., & Zhang, X. (2025). RepoAudit: An autonomous LLM-agent for repository-level code auditing. *Proceedings of ICML 2025*, 21083–21100.

Hutter, F., Hoos, H. H., & Leyton-Brown, K. (2011). Sequential model-based optimization for general algorithm configuration. *Proceedings of LION 5*, 507–523.

Johnson, J., Douze, M., & Jégou, H. (2019). Billion-scale similarity search with GPUs. *IEEE Transactions on Big Data, 7*(3), 535–547.

Krishnan, R., Li, X., Steier, D., & Zhao, L. (2001). On heterogeneous database retrieval: A cognitively guided approach. *Information Systems Research, 12*(3), 286–301.

Lakshminarayanan, B., Pritzel, A., & Blundell, C. (2017). Simple and scalable predictive uncertainty estimation using deep ensembles. *Advances in Neural Information Processing Systems, 30*.

Le Calvé, A., & Savoy, J. (2000). Database merging strategy based on logistic regression. *Information Processing & Management, 36*(3), 341–359.

Liu, A., Song, S., Li, H., Yang, C., & Qi, Y. (2025). Beyond function-level search: Repository-aware dual-encoder code retrieval with adversarial verification. *Findings of EMNLP 2025*, 21034–21049. https://doi.org/10.18653/v1/2025.findings-emnlp.1147

Malkov, Y. A., & Yashunin, D. A. (2020). Efficient and robust approximate nearest neighbor search using hierarchical navigable small world graphs. *IEEE Transactions on Pattern Analysis and Machine Intelligence, 42*(4), 824–836.

Montgomery, A. L., Hosanagar, K., Krishnan, R., & Clay, K. B. (2004). Designing a better shopbot. *Management Science, 50*(2), 189–206.

Mookerjee, V. S., & Dos Santos, B. L. (1993). Inductive expert system design: Maximizing system value. *Information Systems Research, 4*(2), 111–133.

Mookerjee, V. S., & Mannino, M. V. (1997). Redesigning case retrieval to reduce information acquisition costs. *Information Systems Research, 8*(1), 51–68.

Rice, J. R. (1976). The algorithm selection problem. *Advances in Computers, 15*, 65–118.

Saar-Tsechansky, M., & Provost, F. (2007). Decision-centric active learning of binary-outcome models. *Information Systems Research, 18*(1), 4–22.

Shokouhi, M., & Si, L. (2011). Federated search. *Foundations and Trends in Information Retrieval, 5*(1), 1–102.

Si, L., & Callan, J. (2003). Relevant document distribution estimation method for resource selection. *Proceedings of SIGIR 2003*.

Si, L., & Callan, J. (2004). Unified utility maximization framework for resource selection. *Proceedings of CIKM 2004*.

Smith-Miles, K. A. (2009). Cross-disciplinary perspectives on meta-learning for algorithm selection. *ACM Computing Surveys, 41*(1), Article 6.

Stigler, G. J. (1961). The economics of information. *Journal of Political Economy, 69*(3), 213–225.

Voorberg, S., Eshuis, R., van Jaarsveld, W., & van Houtum, G. J. (2021). Decisions for information or information for decisions? Optimizing information gathering in decision-intensive processes. *Decision Support Systems, 151*, 113632.

Voorhees, E. M., Gupta, N. K., & Johnson-Laird, B. (1995). Learning collection fusion strategies. *Proceedings of SIGIR 1995*.

Wolpert, D. H., & Macready, W. G. (1997). No free lunch theorems for optimization. *IEEE Transactions on Evolutionary Computation, 1*(1), 67–82.

Yin, X., Ding, Z., Zhang, Y., Wang, Q., Wang, R., Ni, C., & Cui, Z. (2026). RepoDistill: Distilling repository knowledge through compression-aware budget allocation and policy optimization. *Findings of ACL 2026*, 4425–4443. https://doi.org/10.18653/v1/2026.findings-acl.217

Baeza-Yates, R., & Ribeiro-Neto, B. (1999). *Modern information retrieval*. Addison-Wesley.

Etzioni, O., Hanks, S., Jiang, T., Karp, R. M., Madani, O., & Waarts, O. (1996). Efficient information gathering on the Internet. *Proceedings of the 37th Annual Symposium on Foundations of Computer Science*, 234–243.

Feinberg, F. M., & Huber, J. (1996). A theory of cutoff formation under imperfect information. *Management Science, 42*(1), 65–84.

Teevan, J., Dumais, S. T., & Horvitz, E. (2005). Personalizing search via automated analysis of interests and activities. *Proceedings of SIGIR 2005*.

Topkis, D. M. (1998). *Supermodularity and complementarity*. Princeton University Press.

## 附录 A：解释与收缩规则

1. TMA 必须在固定来源实现和固定打包器下比较；否则不能归因于配置。
2. 代理 regret 与端到端 regret 分开报告；前者不得冒充后者。
3. 平均净效用提升但 P95 regret 恶化时，结论必须包含尾部风险。
4. 条件来源规律必须在未见仓库和至少一种替代来源实现中复现，才写成设计知识。
5. 若 Global Best 或 All+SBCS 帕累托占优，保留负结果并放弃个性化优越性主张。

## 附录 B：待补齐信息

- Dense 模型、向量索引与 Graph 解析器的冻结版本及软件引用 `[待确定]`；
- 成本单位换算、硬件、并发与索引摊销假设 `[待实验环境]`；
- 配置不确定性的最终实现与校准方法 `[待验证集选择]`；
- 2026 年预印本 benchmark 的投稿时最终版本与许可 `[待复核]`。
