# 关注上下文的边际价值：预算约束下用于 Coding Agent 仓库检索的结构感知选择方法

**英文标题：** *Attending to the Marginal Value of Context: A Structure-Aware Selection Method for Repository Retrieval under Limited Budgets*

> 稿件状态：完整研究设计稿。算法、数据、基线、评价程序和结果表结构均已明确；所有带 `[待实验]` 的位置必须由真实运行结果替换。本文不声称尚未执行的实验已经完成。

## 摘要

尽管仓库上下文对跨文件代码补全和真实软件问题修复的作用已被广泛讨论，现有上下文获取方法仍主要依赖单个候选的相关性分数，并据此选择 top-k 或在 token 上限处截断。由这些单项分数选出的代码并不必然形成有效的上下文包，因为候选项长度高度异质、内容可能重复，而定义、调用、配置与测试证据往往只有组合后才支持正确行动。基于有成本信息获取和集合边际价值的观点，本文主张，一个代码项是否值得进入提示上下文，应由它相对于已选集合所增加的任务相关信息及其 token 成本共同决定。本文分别在候选池、候选簇、代码项和结构证据单元四个层次概念化上下文的边际价值，并导出查询相关性、代表性、结构覆盖与预算效率四个可操作指标。进而，本文提出结构感知预算上下文选择器（Structure-aware Budgeted Context Selector，SBCS），以查询加权设施位置函数刻画候选替代关系，以查询加权覆盖函数刻画仓库依赖证据，并在硬 token 约束下用带部分枚举的延迟贪心算法构造上下文包。本文设计在 Agent Retrieval Bench、ContextBench、RepoBench 和 CrossCodeEval 上，从检索质量、表征可迁移性、局部上下文强基线、下游增量价值、选择路径解释与组件消融六个层次评价 SBCS；相关实证结果为 `[待实验]`。

**关键词：** Coding Agent；仓库上下文检索；信息获取成本；结构覆盖；次模优化；设计科学

## 1. 引言

大语言模型正在把代码智能从单文件补全推进到真实软件仓库中的问题定位、修改与验证。RepoBench 将仓库级代码补全拆分为检索、补全和端到端流水线任务，CrossCodeEval 进一步表明多语言跨文件补全需要理解分散在其他文件中的依赖信息（Ding et al. 2023; Liu et al. 2024）。在更接近实际开发的环境中，SWE-bench 要求模型针对真实 GitHub issue 修改完整代码库，而 SWE-agent 的结果说明，帮助模型导航、查看和编辑仓库的接口设计会显著影响最终表现（Jimenez et al. 2024; Yang et al. 2024）。这些发展使仓库上下文不再只是提示工程中的附属材料，而成为 coding agent 在行动前形成问题表示、定位修改对象和验证约束的关键投入。如何在有限上下文窗口、推理时延和调用预算下构造有效上下文包，因而同时关系到 agent 的任务成功、运行成本和部署可扩展性。

一种直接做法是让检索器为文件、符号或代码跨度产生相关性分数，随后取最高的若干候选，或按照该排序一直填充到 token 上限。该做法在候选成本相同、价值彼此独立时是合理的；真实仓库却很少满足这两个条件。相邻代码窗口、同一符号的声明与重复实现可能反复表达同一信息，定义、调用者、配置和测试又可能分别只提供一部分证据，而不同文件的长度可以相差数十倍。现有方法一方面主要把改进焦点放在如何取得更好的单项排序，例如利用文本相似度、预训练表示或数据流关系（Shrivastava et al. 2023; Cheng et al. 2024）；另一方面常以固定 k、文件数或预设窗口拼接结果，因而没有显式回答“在已经选择这些内容之后，下一个候选仍带来多少独特价值”。

仓库上下文的最终作用根植于 agent 能否据此作出正确代码行动。一个候选被检索到，并不意味着它会在有限提示中被保留；即使被保留，也不意味着生成模型能够利用它。CodeRAG-Bench 对多类检索器和生成模型的联合评价发现，高质量上下文能够改善代码生成，但检索器常难以取得真正有用的材料，生成器也可能无法有效利用已经取得的内容（Wang et al. 2025）。ContextBench 则显示，agent 探索过的上下文与实际使用的上下文之间存在明显落差（Li et al. 2026）。据此，本文提出一个中心命题：一个候选代码项的价值不是由其脱离集合时的相关性固定给定，而取决于它在当前上下文包中是否代表尚未表达的任务相关内容、是否补充尚未覆盖的仓库依赖证据，以及为此消耗多少 token。

信息检索研究通常以 MRR、Recall@k、nDCG 或相似指标衡量排序质量，仓库检索 benchmark 也多沿用这种单项排序视角（Ding et al. 2023; Liu et al. 2024; Qin and Xie 2026）。这些指标为判断金标准内容是否出现提供了必要基础，却未稳定代表下游价值。增加 k 可以提高召回，同时也会扩大提示、增加重复和噪声；一个覆盖多个金标准文件的上下文包可能遗漏连接这些文件的接口定义；一个文件级命中也可能因整文件过长而把真正关键的跨度挤出预算。Repoformer 发现许多检索上下文对代码补全无益甚至有害，并由此学习何时完全跳过检索（Wu et al. 2024）。这些发现共同表明，“相关候选越多越好”与“有限预算内形成更有用的上下文包”不是同一个问题。

从过程看，仓库上下文获取至少包含候选生成、集合构造和下游使用三个环节。RepoCoder 通过迭代检索与生成改善查询，DraCo 和 RepoGraph 分别利用数据流或仓库图扩大结构可达内容，它们主要改变候选如何被发现（Zhang et al. 2023; Cheng et al. 2024; Ouyang et al. 2025）。然而，即便候选生成器已经取得高质量候选，有限上下文预算仍要求系统决定保留哪些内容。只报告候选排序的 Recall 主要覆盖“金标准是否被发现”，没有充分刻画候选之间的替代和互补，也没有说明最终包是否以较低成本保留了下游所需的证据。因此，本文把候选生成器固定，将集合构造识别为一个独立的、可评价的信息系统设计问题。

从层次看，代码上下文可以沿着查询—候选池—候选项—结构证据单元逐级组织。任务查询决定什么信息可能相关；候选池包含词法、语义或结构检索发现的潜在内容；文件、符号或跨度是实际消耗 token 的选择项；定义—引用、调用、导入、配置和测试关联则构成这些选择项能够呈现的结构证据。沿该层次向下，系统需要从大量候选中识别少量有效内容；沿该层次向上，一个代码跨度的意义也取决于它是否补齐任务所需的关系。由此提出第一个研究问题：**RQ1：在固定 token 预算下，哪些可观察关系共同决定一个代码上下文项相对于当前已选集合的边际任务价值？**

有成本信息获取研究为回答 RQ1 提供了规范性起点。Mookerjee and Dos Santos（1993）把专家系统价值定义为决策收益与信息获取成本的共同结果；Mookerjee and Mannino（1997）进一步表明，案例检索不应忽略属性获取成本，并以单位成本带来的不确定性降低指导检索；Saar-Tsechansky and Provost（2007）则证明，减少预测误差的获取策略可能浪费资源，因为信息应由其对最终决策的影响来评价。迁移到仓库情境，查询相关性给出候选的任务先验，代表性反映候选能否替代一簇相似内容，结构覆盖反映它能否提供新的依赖证据，token 长度则是最直接的信息获取与处理成本。由此提出第二个研究问题：**RQ2：如何把查询相关性、集合代表性、结构覆盖和 token 成本转化为一个可计算、可解释并具有算法保证的仓库上下文选择方法？** 为回答 RQ2，本文提出 SBCS。

SBCS 包含两个相互协调的价值组件和一个预算优化过程。第一，查询加权代表性组件把上下文选择写成设施位置问题：一个已选项能够代表多个与查询相关且内容相近的候选，因而重复选择的边际收益会自然下降。第二，查询加权结构覆盖组件把定义—引用、调用、导入、配置和测试关系转化为可被代码项覆盖的证据单元，使选择器优先补齐与任务相关而尚未呈现的关系。最后，SBCS 以边际收益与 token 成本之比选择下一项，并用适用于单背包约束的部分枚举和延迟贪心求解。这样的设计既保留经典次模最大化的近似保证，也输出每个入选项的代表性增益、结构增益和单位成本价值，允许研究者检查算法为何选择某段代码。

本文拟在四类公开数据上建立累积证据。Agent Retrieval Bench（ARB）提供全仓候选空间、预算敏感指标和无需检索的 no-gold 情形；ContextBench 提供文件、代码块和行级金标准及 agent 轨迹；RepoBench 和 CrossCodeEval 提供可频繁运行的跨文件检索—补全任务（Ding et al. 2023; Liu et al. 2024; Li et al. 2026; Qin and Xie 2026）。评价首先比较同预算上下文包的金标准覆盖和结构覆盖，其次把不同方法的上下文交给多个冻结生成模型以检验包的可迁移价值，再以局部上下文为强基线检验仓库上下文的增量，最后通过选择轨迹、条件分层和消融把表现回连到四项设计理由。全部结果为 `[待实验]`；这种评价设计旨在使本文的贡献不依赖某一个模型、某一种候选生成器或某一个 Recall 数值。

## 2. 文献综述

### 2.1 仓库上下文对 Coding Agent 任务的作用

现代软件仓库通常以模块、文件、类和函数分散实现功能，当前编辑位置不足以呈现所有命名约定、接口约束和行为依赖。早期代码语言模型 benchmark 多以单函数或单文件为单位，而 CrossCodeEval 专门构造必须利用跨文件信息的 Python、Java、TypeScript 和 C# 补全样本，并发现加入相关跨文件上下文能够明显改善表现（Ding et al. 2023）。RepoBench 则把一个可工作的仓库级补全系统分为检索、代码补全和检索—补全流水线三项任务，使“是否找到上下文”和“模型是否利用上下文”能够分别评价（Liu et al. 2024）。这两项工作建立了一个基本共识：对仓库级任务而言，外部代码上下文不是可有可无的提示装饰，而是模型完成跨文件引用和项目特定行为所需的信息资源。

围绕这一共识，已有工作从不同信号改善仓库上下文。Repository-level Prompt Generation（R2C2-Coder）从相似代码中生成跨文件提示，RepoCoder 让生成结果反过来更新检索查询（Shrivastava et al. 2023; Zhang et al. 2023）。CoCoMIC 使用静态分析定位跨文件上下文，并联合建模文件内与跨文件信息；DraCo 进一步构造扩展数据流图，在代码实体之间追踪定义与使用关系（Ding et al. 2024; Cheng et al. 2024）。RepoGraph 将仓库表示为代码依赖图并把图导航能力提供给软件工程 agent，LocAgent 则在异构代码图上执行多跳定位（Ouyang et al. 2025; Chen et al. 2025）。这些结果说明，文本相似性之外的静态结构能够发现查询没有直接点名、却可能影响补全或修复的代码。

然而，更多或更结构化的候选并不自动等于更高的下游效用。Repoformer 的选择性检索实验表明，固定执行检索会带来效率和稳健性问题，一部分上下文对生成无帮助或有害（Wu et al. 2024）。CodeRAG-Bench 同时比较十类检索器和十类语言模型，发现检索质量和生成器使用上下文的能力均构成瓶颈（Wang et al. 2025）。ContextBench 通过过程级金标准进一步观察到，agent 往往偏向召回而非精确，并且探索内容与实际使用内容之间存在差距（Li et al. 2026）。这些异常并未否定仓库上下文的价值，而是说明该价值取决于“什么内容与什么内容一起进入有限提示”。

真实 issue 修复进一步放大了集合构造的重要性。SWE-bench 任务要求模型在完整仓库中协调多个函数、类和文件，SWE-agent、Agentless 和 CodeAgent 分别以交互式界面、分阶段定位—修复或工具集成完成该任务（Jimenez et al. 2024; Zhang et al. 2024; Yang et al. 2024; Xia et al. 2025）。这些系统的最终成功混合了检索、推理、编辑、执行和模型能力，很难仅由端到端通过率识别上下文选择的独立贡献。本文因此采用由细到粗的评价策略：先在有金标准的检索任务中评价集合，再在固定下游模型中验证增量，最后才进入真实修复环境。

### 2.2 仓库上下文检索与选择方法

仓库检索方法大体可以按词法、表示和结构信号区分。BM25 等词法模型根据词项匹配排序，适合查询包含路径、标识符或错误消息的情形（Robertson and Zaragoza 2009）。CodeBERT、GraphCodeBERT 和 UniXcoder 等预训练模型使自然语言与代码能够进入共享或兼容的表示空间，为语义相似检索提供基础（Feng et al. 2020; Guo et al. 2021; Guo et al. 2022）。静态分析和代码图方法则利用导入、数据流、定义—使用与调用关系发现词面不相似的依赖（Ding et al. 2024; Cheng et al. 2024; Ouyang et al. 2025）。不同信号决定候选池的质量，但三类方法通常都输出单项分数或排序。

从排序得到提示上下文仍需一个截断或打包规则。最常见规则是 top-k、固定文件数或在 token 上限处截断；长度归一排序进一步考虑单位 token 的相关性。最大边际相关性（MMR）通过相关性与候选间新颖性折中，能够减少一般语义冗余（Carbonell and Goldstein 1998）。多样性还可用确定点过程或集合摘要方法建模（Kulesza and Taskar 2012; Lin and Bilmes 2011）。但是，一般语义多样性不知道哪种差异与代码任务有关：为了与其他候选不同而选择一个离题文件，不能为 agent 增加有效证据；相反，定义和调用者可能在文本上高度相似，却构成必要互补。

结构检索可以缓解这一问题，却不能替代预算选择。DraCo、RepoGraph 和 LocAgent 的主要目标是沿代码关系找到相关节点或帮助 agent 导航，并不必然决定一个固定 token 包中应保留哪些节点（Cheng et al. 2024; Ouyang et al. 2025; Chen et al. 2025）。若简单扩大 ego graph 或多跳邻域，候选数会随仓库连接度快速增加；若只保留图中心性高的节点，又可能偏向框架基础设施而偏离具体 issue。本文据此区分“结构用于发现候选”与“结构用于衡量已发现候选的互补证据”。SBCS 不重新发明图检索器，而是在任意候选生成器之后，以查询加权的结构证据覆盖决定预算内保留项。

通用 RAG 与向量检索研究还表明，候选生成的工程效率和最终上下文价值属于不同层次。RAG 与 DPR 建立了检索结果进入生成模型的典型架构，FAISS 和 HNSW 则把大规模向量搜索中的速度—内存—召回权衡变成可调实现（Lewis et al. 2020; Karpukhin et al. 2020; Johnson et al. 2019; Malkov and Yashunin 2020）。这些基础设施可以更快地产生更多候选，却不回答有限提示里哪些候选应共同存在。本文固定候选生成器和其 top-L 输出，正是为了不把索引效率、编码器质量与集合选择价值混在一个总分中。

提示压缩是与集合选择相邻但不等价的路线。LLMLingua 用预算控制与 token 级压缩缩短通用提示，LongLLMLingua进一步考虑长上下文中的位置与信息密度，LLMLingua-2 以数据蒸馏学习任务无关的抽取式压缩（Jiang et al. 2023, 2024; Pan et al. 2024）。面向代码，CodePromptZip 依据类型和静态分析信号选择信息 token，RepoDistill 则联合仓库图检索、细粒度压缩预算和策略优化（He et al. 2026; Yin et al. 2026）。这些制品证明压缩可以实际运行，也使 SBCS 的独立贡献边界更严格：它选择具有完整来源定位和程序关系的代码跨度，不做跨度内部 token 改写；实验必须与压缩法及“SBCS 后再压缩”的组合比较，才能判断集合关系是否提供额外价值。

仓库级语义检索和审计也在扩大强基线。RepoAlignBench/ReflectCode 面向变更请求学习仓库感知双编码器与对抗验证，RepoAudit 沿程序路径按需获取审计证据并报告真实时间和 token 成本（Liu et al. 2025; Guo et al. 2025）。因此本文不能把“同时考虑结构和成本”写成首次提出；更准确的缺口是，现有端到端系统较少在冻结候选池上，把内容替代、结构覆盖和实际 token 置入一个具有明确边际日志与近似性质的集合目标。若 SBCS 对这些新强基线没有同预算增量，主张应退回为一种透明可审计的替代实现。

### 2.3 有成本信息获取与集合价值

信息系统研究早已指出，信息的价值不能脱离获取成本和最终决策。Mookerjee and Dos Santos（1993）研究归纳式专家系统设计时，以系统期望价值而非单纯分类精度定义目标。Mookerjee and Mannino（1997）针对案例检索说明，若概念形成与检索策略分离且忽略属性成本，系统会付出不必要的信息获取代价；其成本敏感 ID3 变体以单位成本熵减选择属性。Mookerjee and Mannino（2000）又把均值—风险权衡引入专家系统，使平均表现相近但尾部损失不同的方案可以区分。这些研究共同提示，仓库上下文不能只由命中概率评价，还应把 token、失败风险和最终代码行动纳入设计。

决策中心型获取进一步改变了“什么信息值得获得”的判断。传统主动学习倾向取得最能减少统计误差的标签，Saar-Tsechansky and Provost（2007）却发现，误差减少不一定改善业务决策，并提出优先取得更可能改变决策的信息。Voorberg et al.（2021）把决策密集流程写成马尔可夫决策过程，使系统可以在继续取得信息和执行终局决策之间选择。尽管这些研究分别面向训练标签、属性或流程状态，其共同规范是：中间信息指标必须由下游行为价值校准。本文不直接移植它们的具体算法，而把“决策价值减获取成本”转化为 coding agent 可观察的预算包质量与最终生成/修复结果。

候选之间的关系要求进一步使用集合价值。若一个候选能够代表许多相似候选，随着代表项加入，继续选择同簇内容的边际收益应递减；设施位置函数正好具有这一性质，并被广泛用于数据摘要和代表性选择（Lin and Bilmes 2011）。若代码项能够呈现若干任务相关依赖，覆盖函数可以奖励尚未出现的结构单元。非负设施位置与加权覆盖均为单调次模函数，其和仍保持次模性；在单背包约束下，可以用部分枚举结合贪心获得经典的近似保证（Nemhauser et al. 1978; Sviridenko 2004）。这一数学结构允许本文同时表达替代、覆盖和成本，而不把方法退化为没有解释的神经重排器。

集合优化文献使上述论证不止停留在“多样性有用”。预算最大覆盖明确研究固定成本下覆盖最多需求，次模最大化把边际递减推广到更广泛集合效用（Khuller et al. 1999; Krause and Golovin 2014）。成本有效的网络检测、数据子集选择和主动学习进一步表明，代表性、覆盖与预算可以在同一目标中形成可解释取舍（Leskovec et al. 2007; Wei et al. 2015）。在算法层，lazy greedy、stochastic greedy 和 lazier-than-lazy greedy 分别减少无必要的边际重算与候选检查（Minoux 1978; Mirzasoleiman et al. 2015）。SBCS 只采用与单背包、单调目标相符的机制；超边协同、负关系惩罚或动态 LLM 反馈若破坏这些条件，必须作为无保证扩展单列。

次模思想已经用于有预算摘要、科学文献发现、机器翻译数据选择和图像集合摘要，说明同一数学性质可以支持不同领域的“少而有代表性”制品（Lin and Bilmes 2010; El-Arini and Guestrin 2011; Kirchhoff and Bilmes 2014; Tschiatschek et al. 2014）。与此同时，集合覆盖的近似下界、带背包/覆盖约束的变体和快速近似算法也说明保证依赖明确条件，不能从“目标看起来像覆盖”自动推出（Feige 1998; Iyer and Bilmes 2013; Badanidiyuru and Vondrák 2014; Bach 2013）。本文引用这些工作不是增加算法名词，而是固定证明责任：附录必须逐项说明非负、单调、次模及成本约束，任一经验增强破坏条件时都要撤回相应保证。

代表性目标也有已知失败方式。高维相似度可能不能忠实反映任务所需方向，谱与次模选择研究据此考察表示几何和子集质量之间的关系（Das and Kempe 2011）。最大覆盖则可能偏向容易覆盖的大簇，忽视稀少但关键的证据。SBCS 用 query 权重、证据类型权重和最小必要结构单元缓解这些问题，但不预设缓解成功。第 5 节需按罕见符号、小簇和多跳任务分层，并报告设施位置是否系统性压低小簇；这类失败分析是理论边界的一部分，而不是消融表后的附注。

### 2.4 研究缺口

综上，现有研究留下三个相互关联的缺口。第一，仓库检索主要评价候选单项排名，缺少对最终预算包中重复、代表性和结构互补的联合建模。第二，结构检索擅长扩大可达候选，但一般未把实际 token 成本与查询加权结构证据共同纳入集合目标。第三，现有 benchmark 虽逐渐提供文件、代码块、行和轨迹金标准，却缺少一套把检索包质量、下游任务价值、资源成本与机制解释累积起来的评价设计（Li et al. 2026; Qin and Xie 2026; Zhang et al. 2026）。

本文用 SBCS 回应这些缺口。它不改变基础检索器，而把其 top-L 结果视为同一候选池；不把所有图关系都视为有用，而只覆盖由查询相关种子和限定跳数诱导的证据单元；不以文件数代表成本，而以最终序列化后的 token 为硬预算；不只报告 Recall，而在同一候选池、同一预算和同一下游模型下比较集合算法。由此，本文可以识别性能变化是来自更好的候选生成，还是来自更好的有限预算配置。

## 3. 研究定位、设计理由与方法挑战

本文旨在根据代码证据进入 agent 决策的方式，更有效地利用已经检索到的仓库候选。该目标属于设计科学研究范式：研究不仅要给出一个可运行的人工制品，还要说明其设计来自哪些可检验命题、怎样回应环境中的真实约束，以及评价结果可以形成何种可复用知识（Hevner et al. 2004; Peffers et al. 2007; Gregor and Hevner 2013）。按照情境化理论的要求，本文保留有成本信息获取的核心关系，同时把一般理论中的“属性”“获取成本”和“决策收益”重新操作化为代码跨度、token/计算成本和固定 coding agent 的任务效用（Hong et al. 2014）。

从过程层次看，查询并不直接进入下游模型，而是先诱导候选池，再由集合构造器选择有限代码项，最终序列化为提示。候选池层回答“哪些信息可能相关”，集合层回答“哪些信息值得共同保留”，下游层回答“这些信息能否支持代码行动”。本文聚焦第二层，但用第一层输出定义选择空间，并用第三层结果校准其有效性。这一定位意味着 SBCS 的理论对象不是 LLM 的内部注意力或理解，而是一个外部信息系统在有限预算下作出的可记录选择。

在空间层次上，一个代码项同时属于内容簇和仓库关系网络。内容簇反映它与其他候选之间的替代性；关系网络反映它能够呈现的定义、调用、导入、配置和测试证据。二者不能相互替代：只看内容簇会把结构互补误当重复，只看图连接会把结构相连误当任务相关。因此，本文以查询作为共同条件，对两类关系加权，并把 token 作为进入上下文的共同成本。

尽管长上下文模型扩大了可用窗口，有限预算问题并未消失。更长输入仍增加推理成本和时延，而且模型对长上下文中不同位置的信息利用并不均匀（Liu et al. 2024; Jiang et al. 2024）。企业仓库还可能包含许可证、隐私和安全上不应发送给外部模型的文件 `[待引用]`。因而，“能够放入更多”不等于“应当放入所有”；选择算法需要在预算与边界约束内呈现足够且可追踪的证据。

这里的长上下文论据可以由已核实研究具体化。Lost in the Middle 发现，相关信息处于长输入不同位置时，模型利用效果并不一致；LongLLMLingua 则把位置与信息密度共同纳入压缩并报告成本—质量权衡（Liu et al. 2024; Jiang et al. 2024）。因此本文删除“窗口越长即可取消选择”的隐含假设，同时不声称所有模型都会随长度单调退化。SBCS 的位置序列化组件与集合选择分开消融：若只改变顺序即可取得同等提升，代表性和结构覆盖不应被归功。

### 3.1 查询相关与成本调整的价值

经济学信息搜索把额外信息的收益与搜索成本共同考虑（Stigler 1961）。在专家系统情境中，Mookerjee and Dos Santos（1993）进一步把分类收益、错误损失与属性成本合并为系统价值；Mookerjee and Mannino（1997）以单位成本的不确定性降低改变检索顺序。对 coding agent 而言，候选代码项的直接成本是最终 prompt 中的 token，间接成本还包括读取、重排、序列化和模型推理。两个相关性相近的候选若长度差异巨大，其单位成本价值不应相同。

这一命题带来第一个方法挑战：基础检索分数通常未按 token 校准，不同粒度候选的分数也不可直接比较。简单用相关性除以长度虽可控制成本，却仍把候选价值视为固定值。SBCS 因而必须在硬预算内，根据当前集合重新计算边际价值，并以边际价值/token 而非原始分数决定下一项。该机制在第 5 节通过同预算 BCY、预算利用率、每成功任务 token 和长度方差分层检验。

### 3.2 查询加权代表性

案例检索的目标不是复述所有相似案例，而是以足够少的信息支持分类或决策（Mookerjee and Mannino 1997）。在仓库候选池中，相邻窗口、重复接口说明、别名导入和相似实现可能形成内容簇。若一个已选项已经高质量代表某簇，再选近似项只增加少量新信息。设施位置模型把每个未选候选分配给与之最相似的已选代表，天然呈现边际递减（Lin and Bilmes 2011）。

第二个挑战是，一般代表性可能偏向大簇而牺牲查询相关小簇。例如，仓库中大量日志工具代码彼此相似，却与当前 issue 无关。SBCS 因而用查询相关权重调节每个被代表候选的价值，使代表性只奖励对当前任务有先验关联的内容。第 5 节将以候选内平均相似度、重复文件/符号比例、被代表的高相关簇比例以及移除代表性组件的消融检验这一设计。

### 3.3 查询加权结构覆盖

跨文件任务的关键信息经常沿程序关系分布。CrossCodeEval 用静态分析识别跨文件使用，DraCo 以扩展数据流图追踪相关代码实体，RepoGraph 和 LocAgent 则表明仓库图能够支持多跳定位（Ding et al. 2023; Cheng et al. 2024; Ouyang et al. 2025; Chen et al. 2025）。这些发现说明，一个有效上下文包不仅要减少语义重复，还要覆盖支持行动的不同关系角色。

第三个挑战是如何在不破坏可优化性的条件下表达结构互补。若奖励“只有两个端点同时入选才产生价值”的超边，目标可能不再保持单调次模，经典贪心保证也随之失效。主版本因此把结构关系转化为可由单个候选呈现的证据单元：例如，包含函数签名和其调用摘要的跨度可覆盖一个定义—调用单元，测试文件中指向目标符号的断言可覆盖一个测试关联单元。单元权重由查询相关种子、路径长度和关系类型共同确定。该操作化只声称“上下文显式呈现了关系证据”，不声称模型已经理解关系。第 5 节将以结构单元覆盖、多文件/多跳任务表现和去结构消融检验它。

### 3.4 可追踪的边际选择

设计科学人工制品需要产生可交流的设计知识，而不是只给出一个暂时领先的总分（Gregor and Hevner 2013）。黑箱重排器能够学习复杂交互，却不容易说明某项为何在第 t 步进入上下文，也难以区分提升来自减少重复、补齐结构还是偏好短文本。SBCS 的每一步都计算代表性增益、结构增益、总边际价值和 token 密度，并记录新覆盖的候选簇与结构单元。

第四个挑战是使解释与实际算法完全一致。事后生成自然语言理由可能与真实评分无关，因而本文只输出由目标函数直接产生的结构化日志；自然语言说明若被使用，只能把这些字段模板化呈现。第 5 节将绘制选择顺序上的边际曲线，分析不同任务类别的选择理由，并对失败个案检查高分理由是否对应错误的查询权重、相似度或图关系。解释性在本文中是可审计性，而非对 LLM 内部认知的推断。

**表 1  理论命题、方法挑战与 SBCS 设计的对应**

| 层次 | 理论/经验依据 | 情境指标 | 方法挑战 | SBCS 解决方案 | 专门评价 |
|---|---|---|---|---|---|
| 候选池 | 有成本信息获取 | 查询相关权重、token 成本 | 分数未按成本校准 | 硬预算与边际价值/token | BCY、预算利用、每成功 token |
| 候选簇 | 案例代表性与边际递减 | 候选相似度、内容簇 | 一般多样性可能离题 | 查询加权设施位置 | 冗余、代表簇、去代表性消融 |
| 结构单元 | 跨文件依赖与结构检索 | 定义—引用、调用、导入、配置、测试 | 图连接不等于任务相关；成对互补会破坏保证 | 查询加权单项证据覆盖 | 结构覆盖、多跳分层、去结构消融 |
| 选择过程 | 设计科学可审计性 | 逐项边际收益与覆盖变化 | 事后解释可能不忠实 | 目标函数原生日志 | 选择轨迹、边际曲线、错误分析 |

综上，利用有限仓库候选增强 coding agent，需要一个专门面向集合关系和实际成本的选择机制。相关性、图关系和 token 长度在既有研究中均有概念或技术基础，但把它们组织为一个保持可优化性、可解释性和下游可评价性的预算选择人工制品，才是本文的核心设计贡献。下一节给出该人工制品的完整形式。

## 4. 所提出的方法

本文把一个任务实例记为 $x=(q,R,e)$，其中 $q$ 是 issue、补全前缀、失败轨迹或评审意见形成的查询，$R$ 是冻结在指定提交上的代码仓库，$e$ 是可选的当前编辑位置或锚定文件。基础检索器在 $R$ 上返回候选池 $V_x$。SBCS 的输入仅包括 $q$、$V_x$、从冻结提交静态构造的关系图以及 token 预算；其输出是上下文集合、序列化顺序和逐项选择日志。金标准文件、未来补丁、测试结果和下游模型输出在选择时均不可见。

### 4.1 SBCS 总览

图 1（待绘制）给出 SBCS 的整体流程。第一步统一候选粒度并计算最终序列化成本。第二步从查询和基础检索分数得到非负相关权重，从候选表示得到两两相似度。第三步在仓库图中围绕查询相关种子抽取限定跳数的诱导子图，并把关系转化为结构证据单元。第四步把查询加权代表性与查询加权结构覆盖组合成集合目标。第五步在 token 背包约束下用部分枚举和延迟贪心求解。第六步按可用的代码阅读顺序输出上下文，并保留每一步的边际收益分解。

SBCS 与常见重排器有两个区别。其一，候选分数并非一次计算后固定，而是随着已选集合变化；一个候选若与已选内容重复，其代表性边际收益会降低，若它补充尚未呈现的关系，其结构边际收益会提高。其二，预算作用于最终发送给下游模型的序列化 token，而不是候选数。算法因此允许一个短签名、一个测试断言和一个配置跨度共同替代一个过长文件，也允许在预算充足时保留完整实现。

### 4.2 候选构造、对齐与成本

#### 4.2.1 候选实例

对每个任务，基础检索器返回至多 $L$ 个原始结果。文件级 benchmark 以文件为候选；符号或跨度级 benchmark 按解析器边界切分函数、类、配置块和测试块。为了使不同 benchmark 的结果可比较，本文还构造一个共同的“可序列化跨度”表示：每项由仓库相对路径、起止行、符号签名、必要导入和正文构成。相邻且属于同一符号的重叠跨度先合并，完全包含的重复跨度只保留基础分数较高的一项。

候选窗口只能依据任务时可见信息扩展。若某一检索结果命中函数体中部，可以向外扩展到完整函数或固定行窗，但扩展规则必须在验证集冻结。未来补丁修改行、金标准跨度和测试通过信息只用于评价，不能用于决定窗口。这一约束避免把 benchmark 答案泄漏为选择特征。

#### 4.2.2 缺失结构与粒度掩码

不同语言和文件类型对静态解析的支持不一致。SBCS 为每个候选记录结构可用掩码 $m_v^{mathrm{str}}$。解析成功时，候选可以覆盖定义—引用、调用、导入、配置和测试单元；解析失败时，结构部分为零，算法退化为成本与代表性感知选择，而不是删除该任务。主结果同时报告全样本和结构可解析子样本，防止算法通过排除困难语言取得优势。

文件、符号和跨度也可能同时出现在同一候选池。主实验为避免粒度本身成为混杂因素，将分别在单一粒度下比较；混合粒度作为扩展实验，并加入包含关系去重。每种设置都以最终 prompt 的真实 tokenizer 重新计算成本，而不以字符数或文件大小近似。

#### 4.2.3 Token 成本

令 $g(v)$ 为候选的固定序列化模板，包括路径、行号、符号签名和代码正文。对冻结 tokenizer $mathcal{T}$，候选成本定义为

\[
c(v)=\left|\mathcal{T}\big(g(v)\big)\right|+c_{\mathrm{sep}},
\tag{1}
\]

其中 $c_{\mathrm{sep}}$ 是分隔符和元数据的 token。集合成本原则上还可能受共同头部和去重影响。主版本在候选预处理后保证序列化可加，使 $c(S)=\sum_{v\in S}c(v)$；若部署版本进一步压缩重复导入或共享路径，相关非可加成本作为无理论保证的扩展单独报告。

### 4.3 查询权重、候选相似度与结构证据

#### 4.3.1 查询相关权重

基础检索器给出原始分数 $s_x(v)$。由于 BM25、稠密检索和图检索的分数量纲不同，本文不在跨检索器情形下直接相加，而在每个任务—检索器内用验证集冻结的单调校准函数 $h_m$ 映射到 $[0,1]$：

\[
r_x(v)=h_m\big(s_x(v)ig).
\tag{2}
\]

在单一来源实验中，$h_m$ 可取基于排序百分位的非参数映射；在多来源扩展中，先按来源校准再去重。为避免零权重使相关小簇完全消失，定义

\[
w_x(v)=\epsilon+(1-\epsilon)r_x(v),\qquad 0<\epsilon\ll 1.
\tag{3}
\]

$\epsilon$ 只在验证集选择并做敏感性分析。金标准不参与测试任务的校准。

#### 4.3.2 候选相似度

候选间相似度 $k(u,v)\in[0,1]$ 用于识别替代关系。主版本采用词法重叠与冻结代码表示的凸组合：

\[
k(u,v)=\omega k_{\mathrm{lex}}(u,v)+(1-\omega)k_{\mathrm{emb}}(u,v),
\tag{4}
\]

其中 $k_{\mathrm{lex}}$ 是标识符加权 Jaccard 或 BM25 归一相似度，$k_{\mathrm{emb}}$ 是余弦相似度经截断和重标度后的非负值。路径相同或跨度重叠可以增加一个冻结的重复惩罚，但所有相似度必须非负，以保持设施位置函数的单调次模性。$\omega$ 在仓库级验证划分上选择。

表示模型只用于测量候选替代，不作为本文贡献。主结果固定一个公开代码编码器，稳健性实验更换为另一编码器及纯词法版本。这样可以判断 SBCS 的增量来自集合目标，还是来自某个特定 embedding。

#### 4.3.3 结构证据单元

静态解析器在仓库提交级构造有类型关系图 $G_R=(N_R,E_R)$。节点包括文件、模块、类、函数、变量、配置键和测试；边至少包括 defines、references、calls、imports、configures 和 tests。查询中的路径、标识符、异常帧和测试名与图节点匹配为种子集合 $A_x$，再抽取不超过 $d$ 跳的邻域。所有匹配、关系类型和 $d$ 均在测试前冻结。

令 $\mathcal{Z}_x$ 为邻域中可由候选显式呈现的结构证据单元。例如，函数签名及其被调用摘要、导入语句及目标模块、测试断言及被测符号都可成为单元。每个单元的查询权重为

\[
a_x(z)=\max_{a\in A_x}\left\{r_x(a)\cdot \delta_{\mathrm{type}(z)}
\cdot \exp\big(-\rho\,d_G(a,z)\big)\right\},
\tag{5}
\]

其中 $\delta_{\mathrm{type}(z)}$ 为关系类型权重，$d_G$ 为图距离，$\rho$ 为衰减参数。若种子本身不是候选，则其相关权重由查询匹配规则给出。候选 $v$ 能覆盖的单元集合记为 $A(v)\subseteq\mathcal{Z}_x$。

式（5）不是用图距离替代任务相关性。只有查询相关种子附近且能够被候选内容呈现的单元进入 $\mathcal{Z}_x$；全仓中心性、无限跳扩展和未来补丁关系均不使用。图权重的作用是限定哪类结构差异值得奖励。

### 4.4 SBCS 集合模型

#### 4.4.1 查询加权代表性

给定选择集合 $S\subseteq V_x$，查询加权代表性定义为

\[
F_{\mathrm{rep}}(S)=\sum_{v\in V_x}w_x(v)\max_{u\in S}k(u,v),
\qquad \max_{u\in\varnothing}k(u,v)=0.
\tag{6}
\]

式（6）把每个候选分配给已选集合中最相似的代表。若某一高相关簇尚无代表，加入其中心项可以同时提高多个 $v$ 的最大相似度；若该簇已有近似项，再加入一个重复窗口只改善少数微小差值。因此，代表性增益随集合扩大递减。查询权重使一个离题大簇不会仅因规模大而获得高价值。

#### 4.4.2 查询加权结构覆盖

结构覆盖定义为

\[
F_{\mathrm{str}}(S)=\sum_{z\in\mathcal{Z}_x}a_x(z)
\mathbb{I}\left[\exists v\in S:z\in A(v)\right].
\tag{7}
\]

每个证据单元第一次被呈现时取得其全部权重，后续重复呈现不再增加覆盖价值。定义、调用和测试可以分别成为不同单元，因而算法能够奖励角色互补；同一关系被多个跨度重复呈现则只计一次。对于结构不可用候选，$A(v)=\varnothing$，其价值仍可由代表性部分获得。

#### 4.4.3 综合目标与理论性质

先按各任务候选池中的单项上界归一化两部分，得到 $\bar F_{\mathrm{rep}}$ 和 $\bar F_{\mathrm{str}}$。SBCS 求解

\[
\max_{S\subseteq V_x}
F_x(S)=\alpha\bar F_{\mathrm{rep}}(S)+(1-\alpha)\bar F_{\mathrm{str}}(S),
\quad
\text{s.t. }\sum_{v\in S}c(v)\le B_x,
\tag{8}
\]

其中 $\alpha\in[0,1]$ 控制内容代表性与结构覆盖的折中，$B_x$ 是上下文 token 预算。

**命题 1。** 若 $w_x(v)\ge 0$、$k(u,v)\ge 0$、$a_x(z)\ge 0$ 且候选成本在选择前固定，则 $F_x$ 是归一化、非负、单调次模函数。

**证明。** 对任意 $v$，$\max_{u\in S}k(u,v)$ 随 $S$ 扩大不减；向较小集合加入候选更可能提高当前最大值，故其边际增益不小于向较大集合加入同一候选的增益。以非负 $w_x(v)$ 求和后，$F_{\mathrm{rep}}$ 单调且次模。对任意结构单元 $z$，集合指示函数在未覆盖时的边际增益为 $a_x(z)$，覆盖后为零，故加权覆盖 $F_{\mathrm{str}}$ 亦单调次模。非负线性组合保持这些性质，且空集合两部分均为零。证毕。

命题 1 允许使用适用于单背包约束的次模最大化算法。按照 Sviridenko（2004），对常数规模种子进行部分枚举，再对剩余候选按边际密度贪心，可以达到 $1-1/e$ 近似保证。实现中用 Minoux（1978）的延迟更新维护边际收益上界，以减少重复计算。本文的保证不覆盖三种扩展：选择后动态扩大窗口导致成本变化；奖励只有两个端点共同出现才产生价值的超边；在每一步调用 LLM 重新估计相关权重。这些扩展若进行，只作为无保证变体报告。

#### 4.4.4 序列化与位置安排

集合目标只决定选择什么，不决定如何排列。为防止排序方式与选择方法混淆，主实验使用所有方法共享的冻结序列化规则：先放查询锚点或入口，再按定义—实现—调用者—配置—测试的角色优先级排列，同角色内按第一次选择的边际密度排序。另一种按路径和行号排列的版本作为稳健性检验。若不同位置会影响长上下文利用（Liu et al. 2024b），这种共享规则保证位置效应不会只惠及 SBCS。

### 4.5 优化算法与实现

算法 1 给出 SBCS 主流程。

```text
输入：查询 q，候选池 V，关系图 G，token 预算 B，折中参数 alpha
输出：上下文集合 S，序列化上下文 P，选择日志 L

1  预处理候选，计算固定成本 c(v)
2  校准查询相关权重 w(v)，计算非负相似度 k(u,v)
3  从查询相关种子抽取限定跳数子图，构造证据单元 Z 与 A(v)
4  定义 F(S) = alpha * F_rep(S) + (1-alpha) * F_str(S)
5  best <- 最佳可行单项解；L <- 空
6  对允许的常数规模种子 T 进行部分枚举：
7      S <- T；建立所有剩余候选的边际密度上界堆
8      当堆非空：
9          弹出上界最大的候选 v
10         重新计算 DeltaF(v | S) / c(v)
11         若 v 可装入且重算值仍为最大，则加入 S 并记录增益分解
12         否则以新上界回堆；非正增益候选丢弃
13     若 F(S) > F(best)，令 best <- S
14 按冻结角色规则序列化 best，返回集合、prompt 与日志
```

候选规模为 $L$ 时，完整相似度矩阵的空间复杂度为 $O(L^2)$。本文不在全仓节点上构造该矩阵，而只在固定 top-$L$ 池中计算；$L$ 的主值和敏感性范围均预注册。结构图在仓库提交级缓存，任务级只抽取局部证据单元。最坏情况下贪心仍可能多次计算所有候选边际收益，因而实验除报告任务质量外，还报告选择器 CPU/GPU 时间、峰值内存和 P95 时延。优化带来的候选处理成本必须计入净效用，不能只比较下游 token。

每条日志至少包含：候选路径与跨度、加入前已用预算、代表性增益、结构增益、新覆盖簇数、新覆盖结构单元、token 成本、边际密度和未选择的主要原因。该日志同时服务于复现、探索性分析和失败审计。

## 5. 实证评价

### 5.1 数据

本文采用分层 benchmark 组合，而不是把所有实验压在昂贵的真实修复上。快速开发使用 RepoBench-R/RepoBench-P 与 CrossCodeEval。RepoBench 支持 Python 和 Java，并明确区分检索、补全和流水线；CrossCodeEval 覆盖 Python、Java、TypeScript 和 C#，可用于未见语言与跨文件依赖验证（Ding et al. 2023; Liu et al. 2024）。这两类任务可离线缓存候选和金标准，适合频繁调试目标函数。

主检索实验使用 ARB 的冻结版本。按 2026 年 8 月核验的公开版本，ARB 包含 427 个样本和 25 个开源仓库，其中 345 个为正检索案例，82 个为自然 no-gold 或反事实错误仓库案例；其子任务覆盖从实现变化找测试、从评审意见找额外上下文、从失败轨迹找代码以及 ripple-effect 关系，并提供预算敏感评价（Qin and Xie 2026）。正式运行时记录 release tag、校验和与下载日期，若 benchmark 更新则同时报告冻结旧版与最新版。

细粒度验证使用 ContextBench。该基准包含 1,136 个真实 issue、66 个仓库和 8 种语言，并为任务提供人工标注金标准上下文和过程评价框架（Li et al. 2026）。主结果先使用作者标记的 verified 子集 `[待核冻结版本数量]`，再扩展全量；文件、代码块和行级评价分别报告，不用文件命中替代关键跨度命中。SWE-bench Verified 的分层子样本只用于算法冻结后的末端修复验证（Jimenez et al. 2024）。

所有划分以仓库为组，而不是随机拆分任务。任何超参数、相似度组合、关系权重和阈值只能在训练仓库和验证仓库选择，测试仓库不可用于调节。对一个仓库多个版本的重复或近似任务执行去重审计 `[待实现脚本]`。静态图只从 base commit 构造，未来补丁和测试补丁不得进入索引。

### 5.2 主要实验

除仓库检索候选外，下游生成还依赖查询和当前文件局部上下文。本文因而设计四项主实验。实验 1 比较同 token 预算下不同集合选择器的检索包质量。实验 2 把冻结的上下文包交给多个下游代码模型，检验选择价值是否跨模型保持。实验 3 评价不使用仓库检索、只使用当前文件/锚点局部上下文的强基线。实验 4 将局部上下文与不同方法选择的仓库上下文整合，检验 SBCS 是否在传统局部证据之上产生增量任务价值。随后用探索性日志分析回答 RQ1，并以消融回答各设计组件是否必要。

基线按排除的设计能力分层：

1. **Rank-Truncate**：按基础分数排序，在预算处截断，代表惯常做法；
2. **Length-Normalized Rank**：按相关性/token 排序，隔离单纯成本归一；
3. **Independent Knapsack**：以固定单项相关值求 0-1 背包，隔离动态集合价值；
4. **MMR**：相关性与一般多样性折中，隔离代表性但不使用代码结构；
5. **Graph-only Coverage**：仅优化查询加权结构覆盖，检验结构是否会离题；
6. **Facility-only**：仅优化查询加权代表性，检验结构的增量；
7. **Random Feasible**：随机可行集合，只作完整性检查；
8. **Oracle Gold Packing**：在金标准可得时按最小成本装入金标准跨度，只作上界，不参加公平排名。

所有方法共享相同候选池、基础分数、候选粒度、tokenizer、预算、序列化规则和下游模型。若某基线原论文需要专门候选生成器，则另设“完整系统比较”，不能把候选生成优势误归因于集合算法。SBCS 的主参数为 $\alpha$、$\omega$、图跳数 $d$、距离衰减 $\rho$ 和证据类型权重；调参范围、选择准则和计算预算在测试前登记。

预算设为 2K、4K、8K、16K 和 32K token，另以各 benchmark 中位金标准成本的倍数做相对预算分析。每项实验至少报告五类指标：

- 金标准检索：Recall、Precision、MRR，以及 benchmark 官方预算指标（如 ARB 的 BCY@B）；
- 集合质量：token 加权 precision/recall、候选冗余、重复路径比例、结构证据覆盖；
- 下游质量：Exact Match、Edit Similarity、Identifier F1、编译/测试通过或 issue resolved；
- 成本效率：实际输入 token、选择耗时、总时延、模型调用成本、每成功任务成本；
- 风险与稳健性：仓库级方差、失败率、P95 成本、不同语言/任务/预算的最差组表现。

统计推断以任务为观测但按仓库聚类。对成对差异使用仓库分层 bootstrap 置信区间和置换检验；多基线比较使用 Holm 校正；同时报告效应量而非只报告 p 值。生成模型有随机性时，对预注册子样本运行多个种子，并报告 pass@1 的均值、方差和一致成功率。模型版本、API 日期、温度与系统提示全部冻结并附录披露。

### 5.3 实验结果

> 本节为与 ACAA 同构的正式结果写作模板。方括号中的数值、方向、显著性和解释均须由真实结果替换；若数据不支持预期，保留真实模式并收缩结论。

#### 5.3.1 实验 1：同预算上下文包质量

表 2 比较不同方法在 ARB 和 ContextBench 上的预算选择结果。

**表 2  同预算上下文选择表现 `[待实验]`**

| 方法 | BCY@4K | BCY@8K | Gold-span Recall@8K | Token Precision | 冗余率 | 结构覆盖 | 选择 P95 ms |
|---|---:|---:|---:|---:|---:|---:|---:|
| Rank-Truncate | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| Length-Normalized | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| Independent Knapsack | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| MMR | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| SBCS | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |

结果段首先只报告事实：SBCS 相对各基线在每个预算、粒度和任务上的差值、置信区间和校正后显著性 `[待实验]`。随后解释跨预算模式。若优势主要出现在 2K—8K 紧预算，并随预算扩大而收敛，这与“集合选择在稀缺时最重要”一致；若只在 32K 出现，说明优势可能来自获得更多候选而非更有效配置。第三步检查冗余和结构覆盖是否与金标准提升共同出现。若 Recall 提高但结构覆盖、下游结果不变，不能宣称结构互补机制成立。

no-gold 案例单独评价。SBCS 的单调目标会倾向选择正价值候选，因此主版本增加一个只在验证集校准的最小单项/总价值门槛；所有候选低于门槛时允许返回空集合。报告 selective success、coverage、错误检索率和空返回成本，不把 no-gold 与普通 Recall 混成一个平均数。

#### 5.3.2 实验 2：上下文包的跨模型可迁移价值

为了排除“结果只适配某个生成头或提示”的解释，本文冻结每种方法产生的上下文包，并分别交给 `[模型 A]`、`[模型 B]` 和 `[模型 C]` 三个能力与架构不同的代码模型。RepoBench-P 和 CrossCodeEval 使用统一补全模板；issue 定位子任务使用统一文件/跨度输出格式。

**表 3  不同下游模型使用冻结上下文包的表现 `[待实验]`**

| 上下文方法 | 模型 A EM / ID-F1 | 模型 B EM / ID-F1 | 模型 C EM / ID-F1 | 跨模型平均秩 |
|---|---:|---:|---:|---:|
| Rank-Truncate | [待实验] | [待实验] | [待实验] | [待实验] |
| MMR | [待实验] | [待实验] | [待实验] | [待实验] |
| Graph-only | [待实验] | [待实验] | [待实验] | [待实验] |
| SBCS | [待实验] | [待实验] | [待实验] | [待实验] |

若 SBCS 在多个下游模型中保持较好平均秩，说明其改善更可能属于上下文包而非单一模型偶合。若只在某个长上下文模型上有效，则应检查该模型是否更能利用结构化序列；若检索指标提高但所有模型均无增量，则可能是 benchmark 金标准包含生成器不需要的信息，或当前序列化抵消了选择优势。后一结果仍可质疑检索指标的效度，却不能写成生成性能贡献。

#### 5.3.3 实验 3：局部上下文强基线

仓库上下文不是代码生成的唯一信息。当前文件前缀、相邻函数、错误行附近窗口和 issue 锚点往往提供强局部信号。实验 3 在相同总预算下比较 Local-only、Retrieved-only、Rank-Truncate Repository 和 Oracle Local Expansion。其目的不是证明仓库检索必然胜过局部上下文，而是建立实际系统中必须超过的强基线。

**表 4  局部与仓库上下文基线 `[待实验]`**

| 输入 | RepoBench EM | CrossCodeEval EM | Identifier F1 | 平均 token |
|---|---:|---:|---:|---:|
| Query / prefix only | [待实验] | [待实验] | [待实验] | [待实验] |
| Local-only | [待实验] | [待实验] | [待实验] | [待实验] |
| Retrieved-only | [待实验] | [待实验] | [待实验] | [待实验] |
| Local + Rank-Truncate | [待实验] | [待实验] | [待实验] | [待实验] |

如果 Local-only 在单文件或显式标识符任务上已经很强，这一结果限定仓库选择的适用条件；如果 Retrieved-only 较弱，也不意味着检索无价值，因为仓库内容可能必须与当前编辑语境共同解释。该过渡直接引出实验 4 的集成评价。

#### 5.3.4 实验 4：SBCS 在局部上下文之上的增量价值

实验 4 固定局部上下文和总预算，把剩余预算分别分配给 Rank-Truncate、MMR 和 SBCS。对补全任务报告 EM、Edit Similarity 和 Identifier F1；对 SWE-bench/ContextBench 分层子样本报告定位、补丁通过、总 token 和每成功成本。

**表 5  集成局部与仓库上下文的下游表现 `[待实验]`**

| 集成方法 | RepoBench-P EM | CrossCodeEval ES | Issue 定位成功 | SWE-bench 子样本通过 | 总 token | 每成功成本 |
|---|---:|---:|---:|---:|---:|---:|
| Local-only | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| Local + Rank-Truncate | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| Local + MMR | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| Local + SBCS | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |

解释分三层。第一，SBCS 是否在相同仓库预算下提高最终任务质量；第二，其增量是否在扣除选择耗时和推理 token 后仍成立；第三，结构覆盖和冗余变化是否能解释任务差值。只有这三层同时获得支持，本文才把结果写成“集合边际价值设计改善了 coding agent 的上下文效用”。如果只节省成本而质量相同，则贡献收缩为效率；如果只改善中间指标，则贡献限定为预算检索。

### 5.4 探索性分析

主实验完成后，本文从 SBCS 日志提取四类量以回答 RQ1：被选项的基础相关性、加入时的代表性增益、加入时的结构增益和单位 token 边际价值。为避免只展示成功案例，分析覆盖全部测试任务，并按预算、语言、仓库规模、修改文件数、查询是否含标识符、结构可解析比例和基础检索器分层。

#### 5.4.1 查询相关与 token 效率

首先按候选长度分位数绘制入选概率与基础相关性。若 SBCS 简单偏爱短片段，低长度项会在控制边际价值后仍异常占优；若成本设计按预期工作，较长候选只有在代表或覆盖更多高权重信息时进入。进一步比较 Length-Normalized Rank，确认结果不是把相关性除以长度即可复制 `[待实验]`。

#### 5.4.2 代表性与冗余

其次，按候选与已选集合的最大相似度排序，绘制代表性边际增益。预期随着相似度上升，新增候选的代表性价值下降；但若其结构增益高，仍可能被选择。本文将展示典型的“内容相似但结构角色不同”和“内容不同但任务无关”案例 `[待实验]`，用来检验查询加权设施位置是否比一般 MMR 更符合代码情境。

#### 5.4.3 结构覆盖

第三，统计不同关系类型在入选集合中的新增覆盖及其与任务结果的关联。多文件修改、测试定位和 ripple-effect 任务若从 calls/tests/configures 覆盖中获得更大增量，说明结构价值具有任务条件；若 imports 等关系在所有任务中高频但与结果无关，应降低或删除其权重，而不是把图覆盖本身当作成功。所有关联分析均控制预算和候选池质量，不解释为因果效果。

#### 5.4.4 边际选择路径

最后，绘制每个选择步骤的 $\Delta F_{\mathrm{rep}}$、$\Delta F_{\mathrm{str}}$ 和 $\Delta F/c$。边际曲线应总体下降，但具体任务可能在某一步因新结构簇出现而短暂上升 `[待实验]`。本文将人工编码一组成功和失败任务，区分错误查询权重、相似度误判、图解析缺失、预算粒度不当和下游利用失败。日志只解释 SBCS 的外部决策，不被表述为 agent 的“心理注意”。

### 5.5 消融分析

本文构造四个主要消融：去掉结构覆盖的 SBCS-Rep、去掉代表性的 SBCS-Str、去掉 token 成本而用固定项数的 SBCS-NoCost，以及保留集合但使用原检索顺序的 SBCS-NoOrder。另将完整算法与不做部分枚举的纯密度贪心比较，以量化理论增强步骤的实际价值。

**表 6  SBCS 组件消融 `[待实验]`**

| 变体 | BCY@8K | 冗余率 | 结构覆盖 | 下游效用 | 选择时延 |
|---|---:|---:|---:|---:|---:|
| SBCS-Rep | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| SBCS-Str | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| SBCS-NoCost | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| SBCS-NoOrder | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| SBCS-GreedyOnly | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| SBCS | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |

组件贡献只有在移除后相关中间量按预期变化并且任务结果随之变化时才成立。例如，去结构后结构覆盖下降而多跳任务退化，支持结构机制；若去结构后指标变化但下游无差异，则结构单元可能不是模型可利用证据。去成本后若 Recall 略升但每成功成本恶化，支持成本调整目标；若完整 SBCS 与 SBCS-Rep 无差异，则本文应把贡献收缩为成本与冗余感知选择。

## 6. 贡献与启示

本文的第一项潜在贡献是概念性的。仓库上下文研究通常把相关性赋给单个文件或代码块，本文把上下文价值概念化为一个层次化、集合依赖的关系：查询在候选池中产生任务先验，候选簇形成替代关系，代码项消耗实际预算，结构证据单元形成互补覆盖。由此，“相关”与“值得进入当前上下文包”被明确区分。该概念化把有成本信息获取理论从独立属性选择扩展到具有内容重复和程序依赖的数字人工制品情境，也为解释为何高 Recall 不必然带来高任务效用提供了可检验结构。

第二项潜在贡献是方法和设计科学制品。SBCS 把查询加权设施位置、查询加权结构覆盖和 token 背包约束组合为一个单调次模目标，并通过带部分枚举的延迟贪心给出近似保证。更重要的是，四项设计理由分别对应可运行机制和专门证据：成本对应真实 token 与净效用，替代对应代表性与冗余，互补对应结构单元覆盖，可审计性对应逐项边际日志。若实证获得支持，SBCS 不只是某个 benchmark 上的重排技巧，而是一种可以嵌入不同候选生成器和下游 agent 的预算上下文构造模式。

第三项潜在贡献是经验知识。分预算、粒度、语言、任务类型和图可解析性的结果可以揭示集合选择何时最有价值。本文特别关注四种条件规律：紧预算是否放大代表性设计的收益；多文件和 ripple-effect 任务是否更依赖结构覆盖；候选长度方差是否改变成本归一的价值；结构解析失败时算法是否安全退化。只有实际结果支持的规律才进入终稿。算法权重和选择日志被解释为人工制品的决策记录，而不是 LLM 内部理解或人类认知的代理。

本研究也具有四类实践启示。第一，对 coding-agent 开发者，与其持续扩大 top-k，不如把候选生成与预算打包分开评价，并记录每项新增证据。第二，对检索基础设施提供者，API 应返回可比较分数、稳定跨度、token 成本和结构元数据，使上层系统能够作集合决策。第三，对 benchmark 维护者，仅提供文件级金标准不足以区分“命中文件”和“呈现可用证据”，应尽可能发布跨度、关系角色和预算评价。第四，对企业部署者，SBCS 的预算和可审计日志可以支持成本上限、敏感文件过滤和失败复盘，但隐私与安全约束仍需在候选进入算法前独立执行。

## 7. 结论

本文研究有限 token 预算下 coding agent 的仓库上下文选择问题。基于有成本信息获取和集合边际价值，本文将上下文价值分解为查询相关性、候选代表性、结构证据覆盖和预算效率，并提出 SBCS 作为对应人工制品。所设计的评价将在公开检索、跨文件补全和真实 issue 子样本上，依次检验预算包质量、跨模型使用价值、相对局部上下文的增量、选择路径与组件贡献；实证结论为 `[待实验]`。

本研究存在四类边界。第一，主评价依赖 ARB、ContextBench、RepoBench 和 CrossCodeEval，它们覆盖的仓库、语言和任务仍不能代表企业单体仓库、生成代码库或高度动态依赖；跨域可推广性需另行验证。第二，主模型只使用仓库内部静态内容，没有纳入 issue 讨论、构建日志、外部 API 文档和竞争实现等环境信息；这些来源可能改变候选价值。第三，$\alpha$、关系类型权重、图距离衰减、候选粒度和成本系数均具有情境依赖，部署时需要在不泄漏测试任务的验证样本上重新校准。第四，为保持次模保证，本文使用固定成本和可由单项呈现的结构单元，没有直接奖励成对代码共同出现的超边互补，也没有让 LLM 在每一步动态重估价值；更强交互模型可能提高表现，但需要新的优化和评价。

未来研究可以在三方面扩展。其一，将静态选择推广为随测试反馈更新的动态上下文包，但应与“何时停止检索”的序贯问题区分。其二，在安全和隐私约束下研究多背包或分区预算，使敏感度、来源许可和 token 同时成为约束。其三，研究下游模型利用能力与上下文选择的联合设计；若某些结构证据稳定被检索却无法被模型使用，改进方向可能不在检索器，而在提示表示、工具接口或代码模型训练。

## 参考文献

Carbonell, J., & Goldstein, J. (1998). The use of MMR, diversity-based reranking for reordering documents and producing summaries. *Proceedings of SIGIR 1998*, 335–336.

Chen, G., Huang, L., Xiao, S., Zhang, C., & Zhao, H. (2024). Attending to customer attention: A novel deep learning method for leveraging multimodal online reviews to enhance sales prediction. *Information Systems Research, 35*(2), 829–849. https://doi.org/10.1287/isre.2021.0292

Chen, G., Xiao, S., Zhang, C., & Zhao, H. (2023). A theory-driven deep learning method for voice chat-based customer response prediction. *Information Systems Research, 34*(4), 1513–1532. https://doi.org/10.1287/isre.2022.1196

Chen, Z., Tang, R., Deng, G., Wu, F., Wu, J., Jiang, Z., Prasanna, V., Cohan, A., & Wang, X. (2025). LocAgent: Graph-guided LLM agents for code localization. *Proceedings of ACL 2025*, 8697–8727. https://doi.org/10.18653/v1/2025.acl-long.426

Cheng, W., Wu, Y., & Hu, W. (2024). Dataflow-guided retrieval augmentation for repository-level code completion. *Proceedings of ACL 2024*, 7957–7977. https://doi.org/10.18653/v1/2024.acl-long.431

Ding, Y., Wang, Z., Ahmad, W. U., Ding, H., Tan, M., Jain, N., Ramanathan, M. K., Nallapati, R., Bhatia, P., Roth, D., & Xiang, B. (2023). CrossCodeEval: A diverse and multilingual benchmark for cross-file code completion. *Advances in Neural Information Processing Systems, 36*, Datasets and Benchmarks Track.

Ding, Y., Wang, Z., Ahmad, W. U., Ramanathan, M. K., Nallapati, R., Bhatia, P., Roth, D., & Xiang, B. (2024). CoCoMIC: Code completion by jointly modeling in-file and cross-file context. *Proceedings of LREC-COLING 2024*, 3433–3445.

Feng, Z., Guo, D., Tang, D., Duan, N., Feng, X., Gong, M., Shou, L., Qin, B., Liu, T., Jiang, D., & Zhou, M. (2020). CodeBERT: A pre-trained model for programming and natural languages. *Findings of EMNLP 2020*, 1536–1547.

Gregor, S., & Hevner, A. R. (2013). Positioning and presenting design science research for maximum impact. *MIS Quarterly, 37*(2), 337–355. https://doi.org/10.25300/MISQ/2013/37.2.01

Guo, D., Ren, S., Lu, S., Feng, Z., Tang, D., Liu, S., Zhou, L., Duan, N., Svyatkovskiy, A., Fu, S., Tufano, M., Deng, S. K., Clement, C., Drain, D., Sundaresan, N., Yin, J., Jiang, D., & Zhou, M. (2021). GraphCodeBERT: Pre-training code representations with data flow. *International Conference on Learning Representations*.

Guo, D., Lu, S., Duan, N., Wang, Y., Zhou, M., & Yin, J. (2022). UniXcoder: Unified cross-modal pre-training for code representation. *Proceedings of ACL 2022*, 7212–7225.

Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. *MIS Quarterly, 28*(1), 75–105. https://doi.org/10.2307/25148625

Hong, W., Chan, F. K. Y., Thong, J. Y. L., Chasalow, L. C., & Dhillon, G. (2014). A framework and guidelines for context-specific theorizing in information systems research. *Information Systems Research, 25*(1), 111–136. https://doi.org/10.1287/isre.2013.0501

Jimenez, C. E., Yang, J., Wettig, A., Yao, S., Pei, K., Press, O., & Narasimhan, K. R. (2024). SWE-bench: Can language models resolve real-world GitHub issues? *International Conference on Learning Representations*.

Kulesza, A., & Taskar, B. (2012). *Determinantal point processes for machine learning*. Foundations and Trends in Machine Learning, 5(2–3), 123–286.

Li, H., Zhu, L., Zhang, B., Feng, R., Wang, J., Pan, Y., Barr, E. T., Sarro, F., Chu, Z., & Ye, H. (2026). ContextBench: A benchmark for context retrieval in coding agents. *arXiv preprint arXiv:2602.05892*.

Lin, H., & Bilmes, J. (2011). A class of submodular functions for document summarization. *Proceedings of ACL-HLT 2011*, 510–520.

Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P. (2024). Lost in the middle: How language models use long contexts. *Transactions of the Association for Computational Linguistics, 12*, 157–173.

Liu, T., Xu, C., & McAuley, J. (2024). RepoBench: Benchmarking repository-level code auto-completion systems. *International Conference on Learning Representations*.

Minoux, M. (1978). Accelerated greedy algorithms for maximizing submodular set functions. In *Optimization Techniques* (pp. 234–243). Springer.

Mookerjee, V. S., & Dos Santos, B. L. (1993). Inductive expert system design: Maximizing system value. *Information Systems Research, 4*(2), 111–133. https://doi.org/10.1287/isre.4.2.111

Mookerjee, V. S., & Mannino, M. V. (1997). Redesigning case retrieval to reduce information acquisition costs. *Information Systems Research, 8*(1), 51–68. https://doi.org/10.1287/isre.8.1.51

Mookerjee, V. S., & Mannino, M. V. (2000). Mean-risk trade-offs in inductive expert systems. *Information Systems Research, 11*(2), 137–153. https://doi.org/10.1287/isre.11.2.137.11777

Nemhauser, G. L., Wolsey, L. A., & Fisher, M. L. (1978). An analysis of approximations for maximizing submodular set functions—I. *Mathematical Programming, 14*, 265–294. https://doi.org/10.1007/BF01588971

Ouyang, S., Yu, W., Ma, K., Xiao, Z., Zhang, Z., Jia, M., Han, J., Zhang, H., & Yu, D. (2025). RepoGraph: Enhancing AI software engineering with repository-level code graph. *International Conference on Learning Representations*.

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems, 24*(3), 45–77. https://doi.org/10.2753/MIS0742-1222240302

Qin, B., & Xie, Y. (2026). Agent Retrieval Bench: Evaluating repository context retrieval for coding agents. *arXiv preprint arXiv:2607.24882*.

Robertson, S., & Zaragoza, H. (2009). The probabilistic relevance framework: BM25 and beyond. *Foundations and Trends in Information Retrieval, 3*(4), 333–389.

Saar-Tsechansky, M., & Provost, F. (2007). Decision-centric active learning of binary-outcome models. *Information Systems Research, 18*(1), 4–22. https://doi.org/10.1287/isre.1070.0111

Shrivastava, D., Larochelle, H., & Tarlow, D. (2023). Repository-level prompt generation for large language models of code. *Proceedings of ICML 2023*, 31693–31715.

Stigler, G. J. (1961). The economics of information. *Journal of Political Economy, 69*(3), 213–225.

Sviridenko, M. (2004). A note on maximizing a submodular set function subject to a knapsack constraint. *Operations Research Letters, 32*(1), 41–43. https://doi.org/10.1016/S0167-6377(03)00062-2

Voorberg, S., Eshuis, R., van Jaarsveld, W., & van Houtum, G. J. (2021). Decisions for information or information for decisions? Optimizing information gathering in decision-intensive processes. *Decision Support Systems, 151*, 113632. https://doi.org/10.1016/j.dss.2021.113632

Wang, Z. Z., Asai, A., Yu, X. V., Xu, F. F., Xie, Y., Neubig, G., & Fried, D. (2025). CodeRAG-Bench: Can retrieval augment code generation? *Findings of NAACL 2025*, 3199–3214. https://doi.org/10.18653/v1/2025.findings-naacl.176

Wu, D., Ahmad, W. U., Zhang, D., Ramanathan, M. K., & Ma, X. (2024). Repoformer: Selective retrieval for repository-level code completion. *Proceedings of ICML 2024*, 53270–53290.

Xia, C. S., Deng, Y., Dunn, S., & Zhang, L. (2025). Agentless: Demystifying LLM-based software engineering agents. *Proceedings of the ACM on Software Engineering, 2*(FSE). https://doi.org/10.1145/3715754

Yang, J., Jimenez, C. E., Wettig, A., Lieret, K., Yao, S., Narasimhan, K., & Press, O. (2024). SWE-agent: Agent-computer interfaces enable automated software engineering. *Advances in Neural Information Processing Systems, 37*.

Zhang, F., Chen, B., Zhang, Y., Keung, J., Liu, J., Zan, D., Mao, Y., Lou, J.-G., & Chen, W. (2023). RepoCoder: Repository-level code completion through iterative retrieval and generation. *Proceedings of EMNLP 2023*, 2471–2484.

Zhang, K., Li, J., Li, G., Shi, X., & Jin, Z. (2024). CodeAgent: Enhancing code generation with tool-integrated agent systems for real-world repo-level coding challenges. *Proceedings of ACL 2024*, 13643–13658. https://doi.org/10.18653/v1/2024.acl-long.737

Zhang, S., Wang, Y., Liang, J., Shi, Y., Zeng, W., Wang, M., He, S., Xu, N., Ye, S., Cai, K., & Gu, X. (2026). SWE-Explore: Benchmarking how coding agents explore repositories. *arXiv preprint arXiv:2606.07297*.

Bach, F. (2013). Learning with submodular functions: A convex optimization perspective. *Foundations and Trends in Machine Learning, 6*(2–3), 145–373.

Badanidiyuru, A., & Vondrák, J. (2014). Fast algorithms for maximizing submodular functions. *Proceedings of SODA 2014*, 1497–1514.

Das, A., & Kempe, D. (2011). Submodular meets spectral: Greedy algorithms for subset selection, sparse approximation and dictionary selection. *Proceedings of ICML 2011*, 1057–1064.

El-Arini, K., & Guestrin, C. (2011). Beyond keyword search: Discovering relevant scientific literature. *Proceedings of KDD 2011*, 439–447.

Feige, U. (1998). A threshold of ln n for approximating set cover. *Journal of the ACM, 45*(4), 634–652.

Guo, J., Wang, C., Xu, X., Su, Z., & Zhang, X. (2025). RepoAudit: An autonomous LLM-agent for repository-level code auditing. *Proceedings of ICML 2025*, 21083–21100.

He, P., Wang, S., & Chen, T.-H. (2026). CodePromptZip: Code-specific prompt compression for retrieval-augmented generation in coding tasks with LMs. *Findings of ACL 2026*, 27811–27825. https://doi.org/10.18653/v1/2026.findings-acl.1384

Iyer, R., & Bilmes, J. (2013). Submodular optimization with submodular cover and submodular knapsack constraints. *Advances in Neural Information Processing Systems, 26*.

Jiang, H., Wu, Q., Lin, C.-Y., Yang, Y., & Qiu, L. (2023). LLMLingua: Compressing prompts for accelerated inference of large language models. *Proceedings of EMNLP 2023*, 13358–13376. https://doi.org/10.18653/v1/2023.emnlp-main.825

Jiang, H., Wu, Q., Luo, X., Li, D., Lin, C.-Y., Yang, Y., & Qiu, L. (2024). LongLLMLingua: Accelerating and enhancing LLMs in long context scenarios via prompt compression. *Proceedings of ACL 2024*, 1658–1677. https://doi.org/10.18653/v1/2024.acl-long.91

Johnson, J., Douze, M., & Jégou, H. (2019). Billion-scale similarity search with GPUs. *IEEE Transactions on Big Data, 7*(3), 535–547.

Karpukhin, V., Oguz, B., Min, S., Lewis, P., Wu, L., Edunov, S., Chen, D., & Yih, W.-T. (2020). Dense passage retrieval for open-domain question answering. *Proceedings of EMNLP 2020*, 6769–6781.

Khuller, S., Moss, A., & Naor, J. S. (1999). The budgeted maximum coverage problem. *Information Processing Letters, 70*(1), 39–45.

Kirchhoff, K., & Bilmes, J. (2014). Submodularity for data selection in machine translation. *Proceedings of EMNLP 2014*, 131–141.

Krause, A., & Golovin, D. (2014). Submodular function maximization. In L. Bordeaux, Y. Hamadi, & P. Kohli (Eds.), *Tractability: Practical approaches to hard problems*. Cambridge University Press.

Leskovec, J., Krause, A., Guestrin, C., Faloutsos, C., VanBriesen, J., & Glance, N. (2007). Cost-effective outbreak detection in networks. *Proceedings of KDD 2007*, 420–429.

Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W.-T., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. *Advances in Neural Information Processing Systems, 33*, 9459–9474.

Lin, H., & Bilmes, J. (2010). Multi-document summarization via budgeted maximization of submodular functions. *Proceedings of NAACL-HLT 2010*, 912–920.

Liu, A., Song, S., Li, H., Yang, C., & Qi, Y. (2025). Beyond function-level search: Repository-aware dual-encoder code retrieval with adversarial verification. *Findings of EMNLP 2025*, 21034–21049. https://doi.org/10.18653/v1/2025.findings-emnlp.1147

Malkov, Y. A., & Yashunin, D. A. (2020). Efficient and robust approximate nearest neighbor search using hierarchical navigable small world graphs. *IEEE Transactions on Pattern Analysis and Machine Intelligence, 42*(4), 824–836.

Mirzasoleiman, B., Badanidiyuru, A., Karbasi, A., Vondrák, J., & Krause, A. (2015). Lazier than lazy greedy. *Proceedings of AAAI 2015*, 1812–1818.

Pan, Z., Wu, Q., Jiang, H., Xia, M., Luo, X., Zhang, J., Lin, Q., Rühle, V., Yang, Y., Lin, C.-Y., Zhao, H. V., Qiu, L., & Zhang, D. (2024). LLMLingua-2: Data distillation for efficient and faithful task-agnostic prompt compression. *Findings of ACL 2024*, 963–981. https://doi.org/10.18653/v1/2024.findings-acl.57

Tschiatschek, S., Iyer, R., Wei, H., & Bilmes, J. (2014). Learning mixtures of submodular functions for image collection summarization. *Advances in Neural Information Processing Systems, 27*.

Wei, K., Iyer, R., & Bilmes, J. (2015). Submodularity in data subset selection and active learning. *Proceedings of ICML 2015*, 1954–1963.

Yin, X., Ding, Z., Zhang, Y., Wang, Q., Wang, R., Ni, C., & Cui, Z. (2026). RepoDistill: Distilling repository knowledge through compression-aware budget allocation and policy optimization. *Findings of ACL 2026*, 4425–4443. https://doi.org/10.18653/v1/2026.findings-acl.217

## 附录 A：预注册的结果解释规则

1. 只有 SBCS 在同候选池、同预算下优于 Rank-Truncate，才能归因于集合选择，而不是候选生成。
2. 只有结构消融改变结构覆盖并传递到多文件下游任务，才能声称结构机制有效。
3. 只有代表性消融提高冗余并降低任务效用，才能声称替代关系带来增量。
4. 若中间检索提升未传递到生成/修复，结论限定为检索包质量，不用“提高 coding agent 能力”。
5. 若只在一个语言、仓库或基础模型有效，贡献必须标明该边界。
6. 所有负结果、无显著差异和异常高方差均保留在正文或附录，不以只报告最佳预算替代。

## 附录 B：仍需补齐的引文与实现信息

- 企业代码发送、敏感文件过滤与上下文安全边界的直接文献 `[待引用]`；
- 候选切分解析器、版本、许可证与软件引用 `[待引用/软件版本]`；
- 实际采用的代码 embedding、tokenizer 和下游模型卡 `[待确定后引用]`；
- ARB、ContextBench 与 SWE-Explore 在正式投稿日的最终版本、许可和作者顺序 `[待复核]`。
