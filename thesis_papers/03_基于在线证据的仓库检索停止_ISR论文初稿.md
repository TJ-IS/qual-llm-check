# 何时已经取得足够的代码证据？面向 Coding Agent 的仓库检索停止方法

**英文标题：** *When Has a Coding Agent Acquired Enough Code Evidence? A Theory-Driven Method for Stopping Repository Retrieval*

> 稿件状态：完整研究设计稿。现有公开 benchmark 可以提供任务、仓库、金标准和探索轨迹，但通常不直接提供每个轨迹前缀上“立即停止并生成补丁”的反事实结果；本文明确设计受控 prefix replay 生成这些标签。所有 `[待实验]` 均不得在运行前写成事实。

## 摘要

尽管迭代仓库检索已成为 coding agent 处理真实软件问题的重要方式，现有系统通常以固定轮数、固定 token 预算、无新文件阈值或语言模型自报来终止探索。由这些简单规则产生的停止点并不必然具有较高任务效用，因为不同任务需要的证据量不同，新增检索可能补齐关键依赖，也可能只增加重复、干扰、时延与推理成本。基于信息充分性与序贯信息获取的观点，本文主张，每个检查点上的停止应由当前证据支持立即代码行动的价值，与沿固定后续策略再检索一轮的成本调整价值共同决定。本文分别在任务、轨迹前缀、最新检索轮和证据单元四个层次概念化信息充分性，并导出目标证据满足、边际新颖性、表示稳定性与成本调整继续价值四个可操作指标。进而，本文提出证据增量停止器（Evidence-Marginal Stopping，EMS），对冻结 continuation policy 生成的轨迹执行独立前缀回放，以后向归纳构造路径内 oracle 停止标签，并学习可校准的停止值与继续值。本文设计在 SWE-Explore、ContextBench、Agent Retrieval Bench 和 SWE-bench 可执行子样本上，从终局效用—成本、价值与动作预测、固定最大预算强基线、对固定 agent 的增量、状态信号演化和组件消融六个层次评价 EMS；实证结果为 `[待实验]`。

**关键词：** Coding Agent；仓库探索；最优停止；信息充分性；序贯信息获取；设计科学

## 1. 引言

真实软件问题很少能通过一次检索完整理解。issue 描述可能只给出表层症状，agent 读取入口实现后才发现新的调用者或配置，运行测试后又可能获得此前未知的失败路径。RepoCoder 通过检索—生成迭代让当前生成结果改写下一轮查询，SWE-agent 和 CodeAgent 则允许模型在仓库导航、查看、编辑和执行之间循环（Zhang et al. 2023; Zhang et al. 2024; Yang et al. 2024）。SWE-Explore 进一步把仓库探索从最终 patch 中分离出来，按固定代码行预算评价 agent 是否找到核心和可选区域（Zhang et al. 2026）。这些工作表明，上下文获取是随证据更新的过程，而不是一次性搜索框。

一种直接做法是为所有任务规定相同最大轮数或 token 预算，并在达到上限时停止。该方法简单可复现，却对容易任务可能继续过久，对跨模块任务又可能过早。另一种做法是让 LLM 根据自然语言提示判断“是否已经足够”，但这一判断缺少反事实校准，模型、提示和版本变化都可能改变停止。现有实现一方面主要把预算当作防止无限循环的外部约束，另一方面把停止混在查询、工具、编辑和验证的完整 agent policy 中，因而难以识别一次额外检索本身何时值得。

仓库检索的最终作用根植于当前信息能否支持正确代码行动。若关键定义、修改位置和测试约束已经出现，再获得一个相似文件可能不会改变补丁；若仍缺少唯一调用者或失败测试，即使已经读取许多 token，也不应因达到平均轮数而停止。Pitts and Browne（2004）指出，信息获取需要在过度获取和获取不足之间平衡，并以信息充分性决定何时从需求获取转向系统设计。迁移到 coding agent，本文提出中心命题：停止不应由已经消耗多少资源单独决定，而应由当前证据状态下“现在行动”与“按既定流程继续一轮”的净价值比较决定。

已有系统使用多种近似充分性的信号，但它们可能适用于不同任务。固定 token 是累计量阈值，无新文件是差异阈值，关键符号命中类似单一准则，模型连续产生相似定位结果则表现为表示稳定。Pitts and Browne（2004）以及 Browne et al.（2007）发现，人类在信息获取中会使用 magnitude threshold、difference threshold、mental list、single criterion 和 representational stability 等不同停止规则，而且规则使用会随任务结构变化。本文不把这些认知机制归给 LLM；它们揭示的是信息充分性可以由多个可观察关系操作化，而非一个普遍轮数。

从过程看，每轮仓库探索包含获取、状态更新、充分性判断和终局行动。查询—检索器返回新候选，候选并入当前上下文，系统根据新增证据和已有状态决定继续或停止；停止后，固定下游代码模型使用当前上下文生成或验证修改。现有 benchmark 常观察最终是否解决 issue，最多记录读取轨迹，却不直接告诉研究者在第 $t$ 轮停下会怎样。因而，研究停止必须在每个前缀上真实运行同一个终局决策器，而不能用“未来是否最终成功”回填当前可见特征。

从层次看，信息充分性可以沿任务—轨迹前缀—最新检索轮—证据单元组织。任务层决定需要哪些类型证据；前缀层表示当前所有已获信息；最新轮层刻画新增内容是否仍在改变状态；证据单元层包含 issue 实体、错误符号、编辑位置、定义、调用和测试约束。沿时间推进，证据可能逐渐满足、增量下降并趋于稳定，也可能在某一轮因新路径出现而突变。由此提出第一个研究问题：**RQ1：哪些推理时可观察的状态信号，能够表明 coding agent 已取得足以支持终局代码行动的仓库信息？**

序贯信息获取研究为 RQ1 提供规范与描述两类基础。Moore and Whinston（1986, 1987）以及 Voorberg et al.（2021）把信息获取写成状态—行动过程，终局决策收益需要扣除获取成本；Pitts and Browne（2004）和 Browne et al.（2007）提供多种充分性规则；Mullins and Sabherwal（2022）则发现客观信息量与团队决策绩效可能呈倒 U 型，提示新增信息的边际作用可以转负。对应到仓库探索，证据清单覆盖表示目标满足，最新非重复文件和结构单元表示边际新颖性，相邻轮上下文或定位分布表示稳定性，token、工具、时延与下游调用表示成本。由此提出第二个研究问题：**RQ2：如何把这些状态信号转化为一个可训练、可校准并具有清楚反事实边界的检索停止方法？** 为回答 RQ2，本文提出 EMS。

EMS 首先冻结 continuation policy，规定继续时如何生成下一查询、调用来源和更新上下文；EMS 只在检查点决定 stop 或 continue。其次，在每个任务的每个轨迹前缀上，从干净环境独立启动固定下游决策器，取得“现在停止”的实际效用。再次，沿实际后续轨迹后向归纳，计算路径内 oracle 的停止—继续标签，并用当时可见的满足、增量、稳定和成本特征分别估计停止值与继续值。最后，只有继续的预测净优势超过风险缓冲时才继续；外分布或低置信任务退化到保守固定策略。

本文拟用公开过程 benchmark 和新增前缀回放数据建立累积证据。SWE-Explore 覆盖 848 个 issue、203 个仓库和 10 种语言，提供核心/可选代码区域及受限上下文验证；ContextBench 提供 1,136 个任务、66 个仓库、8 种语言和细粒度金标准；ARB 提供 427 个检索任务及 no-gold 情形（Li et al. 2026; Qin and Xie 2026; Zhang et al. 2026）。这些数据可直接支持状态与检索代理评价，但真实停止效用须自行回放。评价将依次比较终局效用—成本、价值和动作预测、Fixed-Max 强基线、对固定 agent 的增量、四类信号演化和消融；全部结果为 `[待实验]`，主结论限定为“给定 continuation policy 上的停止改进”。

## 2. 文献综述

### 2.1 Coding Agent 的迭代仓库探索

仓库级代码补全研究首先说明跨文件上下文的必要性。CrossCodeEval 构造必须使用其他文件信息的多语言补全样本，RepoBench 把检索、补全和流水线拆分评价（Ding et al. 2023; Liu et al. 2024）。RepoCoder 进一步发现，一次查询可能不足以找到全部上下文，因而让代码模型的当前输出参与下一轮检索（Zhang et al. 2023）。这条研究流把上下文从静态输入转变为随生成状态更新的资源。

真实软件工程 agent 将迭代扩展到导航、执行与编辑。SWE-agent 通过专门 agent-computer interface 帮助模型查看仓库、编辑代码和执行测试，CodeAgent 集成检索、实现与测试工具，Agentless 则用定位—修复—验证的分阶段流程提供低复杂度强基线（Zhang et al. 2024; Yang et al. 2024; Xia et al. 2025）。这些系统证明多轮行动具有实际价值，但其最终通过率混合查询生成、工具选择、上下文保留、停止和编辑质量，很难直接形成停止算法的监督信号。

过程级 benchmark 开始缓解这一局限。ContextBench 跟踪 agent 轨迹并评价上下文 recall、precision 和效率，发现复杂 scaffold 不必然改善上下文获取，探索与使用之间还存在落差（Li et al. 2026）。SWE-Explore 将 explorer 的输出限制为固定行预算下的相关代码区域，提供比最终 pass/fail 更细的探索效用（Zhang et al. 2026）。ARB 的预算指标和 no-gold 任务则允许判断“是否应返回任何上下文”（Qin and Xie 2026）。然而，这些 benchmark 通常没有在每个原始轨迹前缀上运行终局修复器，因而不能直接给出停止反事实。

近期系统也开始把成本和上下文管理放到仓库流程内部。RepoAudit 沿可行程序路径按需探索并同时报告真实项目上的时间与 token 成本；RepoDistill 把仓库上下文管理表述为多步决策，并学习压缩预算的分配策略；CodePromptZip 依据代码结构和信息增益在给定压缩率下保留 token（Guo et al. 2025; Yin et al. 2026; He et al. 2026）。它们说明“何时、在哪部分继续花费上下文预算”已经具备可运行制品，但各自同时改变检索、压缩或审计策略。EMS 的必要性不能建立在它们“没有停止”这一过强说法上，而在于可识别性：固定其余动作后，研究者能否独立测量继续一轮检索的边际价值。

RepoAlignBench/ReflectCode、DraCo、RepoGraph 和 LocAgent 又说明，新信息可能来自语义、数据流或多跳图路径，而不同来源的新增节奏并不一致（Cheng et al. 2024; Ouyang et al. 2025; Chen et al. 2025; Liu et al. 2025）。这使单纯的“连续两轮没有新文件”尤其危险：图来源可能在早期只确认入口，随后才触达未被 query 点名的依赖；稠密来源也可能一次返回若干同义实现。EMS 因而把来源标识、独特证据和跨来源分歧保留为状态，而不是把所有新增项压缩成一个计数。

### 2.2 选择性检索与现有停止实践

Repoformer 是与本文最接近的技术先例。它指出固定使用检索会带来效率和稳健性问题，并以自监督方式学习某次代码补全是否需要检索，从而在不损害性能时跳过检索（Wu et al. 2024）。该方法把“检索不是必做动作”明确化，但其主要行动是单次 retrieve/skip，而不是在已经取得若干轮证据后判断是否继续。它的标签和上下文也面向代码补全，不等同真实 issue 探索中的多轮停止。

agent 工程通常采用固定轮数、固定 token/工具预算、连续无新结果或 LLM 自报。固定规则容易复现，却假定所有任务共享同一充分性曲线。差异阈值能够检测最新一轮是否有新文件，却不知新文件是否有任务价值；稳定阈值能够检测表示变化，却可能在错误假设上稳定；LLM 自报利用模型推理，却需要额外 token 且缺少与真实停止结果的校准 `[待系统综述引用]`。因此，任一简单规则都可作为基线，但不足以充当普遍目标。

完整的 agent policy 可以用强化学习同时学习查询、工具、编辑和停止，但这种行动空间需要大量可验证轨迹与稳定奖励。更重要的是，当查询策略也变化时，未执行分支的反事实不可从一条轨迹观察，停止收益与查询质量纠缠。本文通过冻结 continuation policy 收缩问题：继续的后果由实际 rollout 观察，停止的后果由前缀回放观察。该边界牺牲全局最优性，却换来可实施、可审计的停止比较。

通用语言 agent 研究进一步说明这种收缩为何必要。ReAct 将推理与外部行动交错，Reflexion 通过语言反馈更新后续尝试，Tree of Thoughts 显式搜索多条推理分支（Yao et al. 2023a; Shinn et al. 2023; Yao et al. 2023b）。在这些完整策略中，“继续”可能意味着换查询、换工具、回滚编辑或开始另一分支，停止价值无法与探索动作质量分开。本文不声称 EMS 优化这些 agent 的全局规划；它只把一个工程上普遍存在、理论上可以隔离的决策抽出：当下一步检索过程已被冻结时，当前证据是否足以进入代码行动。

这一边界也使评价数据能够实际生成。对每个任务先运行一次最长轨迹，再把每个已观察前缀复制到独立容器，并用固定模型生成补丁或定位输出；Repo2Run 所代表的自动可执行环境构建虽不能解决所有依赖问题，却表明批量恢复仓库测试环境已成为可评价的研究对象（Hu et al. 2025）。无法重放的任务不静默丢弃，而要报告构建失败、测试不确定和模型调用失败三类缺失。由此，benchmark 的“公开数据集”与 EMS 的“可跑标签生成器”形成明确分工。

### 2.3 信息充分性与停止理论

问题求解研究把行动理解为在当前问题表示上搜索，而不是对原始输入作一次静态反应（Newell and Simon 1972）。仓库级提示生成和 CodeRAG-Bench 又分别说明，仓库上下文提议可以改变代码模型输出，但更高检索分数并不保证生成器有效使用上下文（Shrivastava et al. 2023; Wang et al. 2025）。这两条研究链把停止问题夹在表示与行动之间：EMS 必须观察前缀如何改变可用问题表示，同时用真实代码行动校准，而不能用检索列表的累计长度替代充分性。

Pitts and Browne（2004）研究系统分析员在信息需求获取中何时认为已有信息足够。其核心矛盾与仓库探索高度相似：过度获取浪费时间和资源，获取不足形成不完整问题表示并把成本推迟到后续设计与维护。该研究归纳 magnitude threshold、difference threshold、mental list 和 representational stability，并发现停止规则与信息获取结果相关。本文迁移的是这些规则的结构，而非系统分析员的心理：代码任务中的清单、增量和稳定均由日志可计算。

Browne et al.（2007）在三类在线任务中进一步发现，停止规则依赖任务类型；结构化任务更容易使用 mental list 或 single criterion，弱结构任务更可能使用 magnitude threshold 或 representational stability。Browne and Walden（2021）从行为与神经层面继续研究停止过程。由于 coding agent 不具有人类相同认知和神经机制，本文不声称复制心理理论，只据此提出一个可检验设计理由：信息充分性是多维且任务条件化的，单一阈值不应被预设为普遍最优。

规范性研究提供“何时应停止”的目标。Moore and Whinston（1986, 1987）建立带序贯信息获取的决策模型；Hosanagar（2011）在分布式检索中以额外等待的边际收益和成本决定最优等待；Voorberg et al.（2021）把决策密集流程中的信息任务和终局决定统一到 MDP。经典最优停止理论同样把当前停止回报与继续后的期望价值比较（Wald 1947; Peskir and Shiryaev 2006）。这些理论并不直接给出高维代码状态如何表示，却限定了 EMS 的目标必须是价值差而非“当前上下文相关性”。

信息量的非单调作用进一步要求真实前缀评价。Mullins and Sabherwal（2022）发现，在 IS 支持的团队决策中，实际访问的信息量与绩效可能呈倒 U 型。coding agent 的潜在机制不同：重复代码、位置稀释、冲突实现或错误证据可能降低模型表现，而不是人类工作记忆过载。因而本文只迁移“边际信息可能为零或为负”及按实际访问量计量的原则；是否存在平台期或下降必须由同一任务不同前缀的下游结果检验。

经典行为研究为四类状态之间的关系提供了更细的反例。Pitz et al.（1969）观察延迟决策中的信息寻求策略，Rapoport and Tversky（1970）及 Rapoport et al.（1972）比较可选停止与不可选停止，Saad and Russo（1996）则讨论序贯选择中的停止准则。Connolly and Gilani（1982）以及 Connolly and Thorn（1987）表明，任务变量与先验判断会改变搜索行为；Busemeyer（1982）和 Busemeyer and Rapoport（1988）进一步用动态模型描述延迟选择。它们共同反对用一个固定数量阈值代表所有情境，却不能直接告诉算法在代码状态上如何行动。EMS 将其功能收缩为两个可检验要求：状态必须随前缀更新，停止必须相对当前任务的终局效用评价。

需求获取文献提供与软件情境更近的桥梁。Miyake and Norman（1979）指出，提出有效问题本身需要已有知识；Marakas and Elam（1998）显示分析员对事实的语义组织会影响需求表示；Todd and Benbasat（1987）则倡导用过程追踪打开决策支持的“黑箱”。这些结论解释了为何检索历史不能只保存数量：先前证据会改变下一查询可提出什么，也会改变同一新文件在问题表示中的作用。因此 EMS 记录前缀内容和变化，却仍以外部 patch/test 结果而非主观“理解程度”判定效用。

信息过多也可能通过不同机制损害决定。无关信息会干扰有经验决策者，局部理性的额外搜索甚至可能降低管理表现（Gaeth and Shanteau 1984; Glazer et al. 1992）。快速启发式研究则提醒，在某些结构中少量诊断性线索可以胜过广泛搜集（Gigerenzer and Goldstein 1999; Payne et al. 1992）。这些人类研究不能证明 LLM 会以相同方式过载，但它们为实验次序提供理由：先观察更多上下文是否真的改变同一模型的结果，再解释重复、位置或冲突证据是否与下降相关，不能从理论直接宣称负边际已经存在。

规范层面，MDP 和最优停止理论把问题严格限定为状态、停止回报、转移和继续价值（Puterman 1994; Chow et al. 1971）。信息经济学与决策中心获取则分别要求计入搜索成本和终局行动改变（Stigler 1961; Mookerjee and Dos Santos 1993; Mookerjee and Mannino 1997; Saar-Tsechansky and Provost 2007）。EMS 由此采用双价值估计而不是二元模仿：即便训练标签最终是 stop/continue，模型也必须输出可比较的停止值和继续值，评价必须报告 value error 与 regret。动作准确率高但在少数高价值前缀上做错，不能被写成有效停止器。

### 2.4 研究缺口

均值—风险研究还提醒，平均收益相同的获取策略可能具有不同尾部损失（Mookerjee and Mannino 2000）。因此停止研究若只比较平均 token 节省，可能掩盖少数任务上的灾难性早停。本文把这一 IS 逻辑落实为 P95 stop regret、premature-stop 率和风险缓冲消融；它不要求 coding agent 具有风险偏好，风险权重由部署者设定。

现有研究留下三个缺口。第一，coding agent 的多轮探索已成为事实，但停止通常仍是固定预算或完整 policy 中不可分辨的动作。第二，IS 停止理论提供了多种充分性信号和规范价值比较，却尚未被情境化为代码仓库中可计算的证据状态。第三，现有 benchmark 提供任务、轨迹和金标准，但缺少每个前缀的真实立即行动效用；不生成这类反事实，就无法评价过早与过晚停止的实际损失。

EMS 通过四项边界回应缺口。行动空间只含 stop/continue；continue 使用冻结策略，stop 使用冻结下游决策器；状态只使用当前日志，不含未来金标准或后续轨迹；oracle 只在给定实际路径上后向计算，不声称考虑所有未执行查询。这样，研究可以把停止从完整 agent 中隔离出来，又不把离线代理误写成真实代码行动。

## 3. 研究定位、设计理由与方法挑战

本文采用设计科学范式，把信息充分性理论转化为可运行停止人工制品。理论在这里承担三项约束：规定系统应感知哪些状态，规定停止和继续应比较什么价值，规定评价必须区分过早、过晚和成本（Hevner et al. 2004; Peffers et al. 2007; Gregor and Hevner 2013）。情境化工作则识别代码仓库特有的证据单元、检索轮、执行反馈和模型随机性，不把人类认知名词直接赋予 agent（Hong et al. 2014）。

这一构造方式与肖帅勇参与的两篇 ISR 方法研究一致之处，在于每个理论维度都必须改变可运行制品，并拥有一项能够排除“只是最终预测头更强”的专门证据（Chen et al. 2023, 2024）。不同之处在于，原研究从多模态顾客信号构造静态或序列预测表示，EMS 从仓库轨迹构造停止状态和反事实价值；因此本文模仿其论证职责与验证顺序，不迁移领域变量或网络结构。后文的满足、增量、稳定和价值四节都按“理论关系—代码对象—现有规则不足—组件—专门实验”展开。

双价值模型还必须正视校准。神经网络的分数常与真实正确率不一致，温度缩放和模型集成提供了两类实用不确定性估计（Guo et al. 2017; Lakshminarayanan et al. 2017）。EMS 不把校准方法本身作为新理论，而要求风险缓冲具有决策后果：当继续优势接近零或任务外分布时，系统应减少高代价误判，并在覆盖率—regret 曲线上体现。若校准仅改善概率指标而不改善 stop regret，风险组件应从主贡献中删除。

从过程看，任务开始时只有 query 和仓库；每次继续产生新查询、检索结果和更新后的上下文；每个检查点都可以立即交给下游模型行动。充分性不是一个静态标签，而是当前前缀相对于终局任务的状态。DSDL 将动态期望、体验和满意度逐步嵌入序列模型的写法提示，动态理论构念必须对应每个时间步可观察的表示、专门学习目标和解释性结果（Chen et al. 2023）。EMS 同样在每个前缀计算状态和立即效用，但不借用满意度内容。

从层次看，任务目标产生一组可能需要的证据，轨迹前缀累积已获内容，最新一轮改变或不改变该内容，成本随轮次累积。四类指标分别回答：目标是否已经满足、最新一轮还带来多少新信息、问题表示是否趋于稳定，以及继续的预期增益是否超过成本。它们共同描述充分性，但最终行动由价值比较统一。

### 3.1 目标证据满足

Mental-list 和 single-criterion 规则表明，当任务结构允许预先形成需要查明的项目或关键条件时，信息获取可以在这些项目满足后停止（Pitts and Browne 2004; Browne et al. 2007）。在代码任务中，清单不由 LLM 自由臆造，而由 query 与仓库工具提取的可核验目标构成：出现的路径、类、函数、异常帧、失败测试、配置键和明确修改对象。当前上下文是否覆盖这些实体及其定义、引用或测试关系，形成目标满足向量。

第一个挑战是清单不完备。issue 没有提到的根因或间接依赖可能至关重要，因而满足显式清单不能单独触发停止。EMS 把清单覆盖作为状态特征，而不是硬规则，并区分“实体已出现”与“相关关系已呈现”。专门评价按 query 结构化程度比较其价值，并通过去满足特征消融观察 premature-stop 是否增加。

### 3.2 边际新颖性

Difference-threshold 规则要求评价最后一条信息增加了什么；当边际信息低于阈值时停止（Pitts and Browne 2004）。对应到仓库轨迹，最新一轮的新文件数并不足够，因为一个新文件可能与已有内容重复。本文同时计算新符号、新结构单元、候选簇代表性增益、金标准不可见代理增益和上下文替换量。只有任务时可计算的量进入 EMS，金标准增量只用于事后评价。

第二个挑战是增量具有非单调性。一轮可能没有新文件，却通过更精确跨度替换长文件而提高效用；一轮也可能新增许多文件但稀释关键内容。EMS 因而保留有符号的变化特征，并用真实前缀下游效用学习其含义，而不预设“新增越多越好”。专门评价比较无新文件规则、单一差异阈值与多维增量模型。

### 3.3 表示稳定性

Representational-stability 规则认为，当连续获取的信息不再改变问题表示时可以停止（Pitts and Browne 2004; Browne and Walden 2021）。本文用外部可观察代理操作化表示：相邻轮最终上下文集合的 Jaccard、文件/符号定位概率分布的 Jensen–Shannon 距离、证据角色分布变化、来源排名一致性和固定摘要表示的余弦变化。来源共识既可能表明定位稳定，也可能表明多个来源共享盲区，因此只作为组合信号。

第三个挑战是错误稳定。agent 可能从第一轮开始围绕错误模块重复搜索，此时状态稳定但目标证据未满足，终局效用仍低。EMS 必须联合稳定与满足、增量和任务特征；稳定不能作为单独停止条件。评价将专门分析“稳定且成功”“稳定但失败”“不稳定后成功”三类轨迹，并通过去稳定消融观察 late-stop 与 premature-stop 的变化。

### 3.4 成本调整的继续价值

规范性序贯模型要求比较当前停止收益与继续后的期望收益减成本（Moore and Whinston 1986, 1987; Hosanagar 2011; Voorberg et al. 2021）。令当前状态为 $s_t$，立即行动效用为 $u(s_t)$，下一轮成本为 $c_{t+1}$，继续后的价值为 $V^+(s_t)$；理想规则是当 $u(s_t)\ge V^+(s_t)-c_{t+1}$ 时停止。该关系使清单、增量和稳定不再是彼此竞争的硬阈值，而成为估计两个价值的输入。

第四个挑战是继续价值的反事实不可直接从普通日志观察。只有对同一路径各前缀独立行动，才能知道早停结果；只有固定继续策略，实际后续前缀才能代表“继续”的结果。EMS 因而构造 prefix replay 和路径内后向 oracle。专门评价使用价值 MAE、校准、stop regret、premature/late-stop 和任务效用—成本前沿，而不以动作准确率单独判断。

**表 1  信息充分性、方法挑战与 EMS 组件的对应**

| 层次 | 理论来源 | 可观察状态 | 方法挑战 | EMS 组件 | 专门证据 |
|---|---|---|---|---|---|
| 证据单元 | Mental list / single criterion | 实体、定义、调用、测试清单覆盖 | 显式清单不完备 | 软满足向量 | 结构化任务分层、去满足消融 |
| 最新轮 | Difference threshold | 新文件、符号、结构单元、替换量 | 数量不等于价值 | 有符号多维增量 | 无效后续轮、去增量消融 |
| 轨迹前缀 | Representational stability | 集合、定位分布、角色、来源一致性 | 可能错误稳定 | 多尺度稳定特征 | 稳定类型分析、去稳定消融 |
| 决策 | 序贯边际价值 | 停止值、继续值、token/工具/时延 | 反事实与随机性 | prefix replay、后向 oracle、风险阈值 | stop regret、校准、成本前沿 |

综上，本文的理论贡献不在于重述“边际收益等于边际成本”，而在于识别仓库探索中哪些外部证据状态可以用来估计这项比较，并用真实前缀行动结果评价。EMS 的四类状态、路径内 oracle 和双价值决策共同构成核心人工制品。

## 4. 所提出的方法

### 4.1 EMS 总览

一个任务 $x=(q,R,e)$ 在冻结仓库 $R$ 上由 continuation policy $\pi_c$ 产生最长 $H$ 个检索检查点。检查点 $t$ 保存当时可见的查询历史、来源结果、已选上下文、工具日志和可选执行反馈。EMS 的行动集合只有 $\{\text{stop},\text{continue}\}$：stop 把当前上下文交给固定下游决策器 $\pi_d$；continue 严格执行 $\pi_c$ 的下一步。查询生成、来源配置、上下文打包、编辑器和测试器都在比较前冻结。

图 1（待绘制）包含四个环节。第一，运行 $\pi_c$ 生成最大轨迹并保存前缀。第二，从每个前缀的干净环境独立运行 $\pi_d$，获得立即停止效用。第三，沿实际后续轨迹后向计算路径内 oracle 值和动作。第四，只用当时特征训练停止值、继续值和不确定性模型；在线时比较二者的成本调整差，并输出结构化停止理由。

这种设计与完整 agent 强化学习不同。EMS 不决定下一条查询是什么，也不从多种工具中选择；它只判断是否接受固定流程给出的下一轮。由此，继续行动在数据中有实际后果，停止行动可由独立回放观察。研究结论始终写作“EMS 改善了给定 $\pi_c$ 的停止”，不写成“找到了全局最优仓库搜索策略”。

### 4.2 轨迹、检查点与前缀回放

#### 4.2.1 固定 continuation policy

主实验选择一个可公开运行的轻量仓库探索器 `[待确定冻结实现]`。它在每轮根据 query、已读内容和固定提示产生下一检索请求，调用冻结来源配置和上下文打包器。为验证停止规律不只适配一种轨迹，外部实验再使用一个 RepoCoder 式迭代检索策略或另一固定 agent（Zhang et al. 2023）。两种策略分别训练/测试和交叉测试，不在测试任务上微调提示。

$\pi_c$ 必须确定：每轮允许的查询数、来源、候选配额、上下文更新、是否执行测试、最大时域 $H$ 和硬成本上限。若某轮工具失败，失败本身进入日志，策略按预注册退化继续或终止。EMS 不能把“工具异常强制终止”计作自己正确停止。

#### 4.2.2 检查点

初始状态记为 $s_0$，表示只拥有 query 与必要局部上下文；每次完成一轮检索和打包后形成 $s_t$。状态保存完整上下文包而非只保存新增项，以便下游回放与实际在线行为一致。对于测试反馈扩展，检查点还保存编译/测试结果及其变化；主论文先以纯检索状态为主，防止不同执行环境混入结论。

轨迹长度不等时，在实际终止点后不人为填充空轮。最大时域 $H$ 用于控制生成成本，但不是标签中的理想停止；若路径在 $H$ 仍显示继续价值，任务标记为右删失，并在主分析中使用保守处理或单独报告 `[待确定统计方案]`。

#### 4.2.3 独立前缀回放

普通 trajectory 只观察完整 agent 最终一次行动。为得到“在 $t$ 停止”的效用，本文对每个前缀执行：

1. 恢复 base commit 的干净容器；
2. 注入截至 $t$ 的固定上下文包和结构化日志；
3. 禁止 $\pi_d$ 额外读取仓库或调用检索工具；
4. 用冻结提示与模型生成定位、补全或补丁；
5. 运行 benchmark evaluator，记录任务结果、token、时延与失败原因；
6. 对随机生成器在预注册子样本运行多个种子。

若下游 agent 被允许继续自由浏览，前缀差异会被后续读取抵消，停止评价失去意义。因而 $\pi_d$ 必须是上下文封闭的固定决策器，或其额外工具调用被视为终局行动成本而非检索 continuation。

### 4.3 信息充分性状态

第 $t$ 个状态表示为

\[
s_t=(\phi_x,\kappa_t,\delta_t,\sigma_t,\rho_t,\epsilon_t,C_{1:t}),
\tag{1}
\]

其中 $\phi_x$ 是任务和仓库静态特征，$\kappa_t$ 是目标证据满足，$\delta_t$ 是最新增量，$\sigma_t$ 是表示稳定，$\rho_t$ 是来源一致与分歧，$\epsilon_t$ 是可选执行反馈，$C_{1:t}$ 是累计成本。

#### 4.3.1 目标证据满足向量

从 query 提取实体集合 $E_x^q$：路径、模块、类、函数、配置键、异常帧和测试名。对每个实体记录其是否在当前上下文出现、是否获得定义、是否获得至少一个引用/调用关系、是否关联测试。令 $K$ 类证据的满足率为

\[
\kappa_{tk}=\frac{\sum_{e\in E_x^q}\omega_e
\mathbb I[\text{e 的第 k 类证据在 }S_t\text{ 中可见}]}
{\sum_{e\in E_x^q}\omega_e+\varepsilon}.
\tag{2}
\]

若 query 没有显式实体，相应维度使用缺失掩码而不是零，防止模型把“无清单”误解为“完全未满足”。另用查询相关图种子生成潜在关系槽位，但只作为弱证据，不称为真实需求。

#### 4.3.2 边际新颖性

令当前包为 $S_t$，上一包为 $S_{t-1}$。增量向量包括

\[
\delta_t=(\Delta\text{files},\Delta\text{symbols},\Delta\text{units},
\Delta\text{representativeness},\Delta\text{query-score},
\text{replacement-ratio},\Delta\text{tokens}).
\tag{3}
\]

所有差值保留正负号。若新一轮用短而精确的跨度替换整文件，文件数可能不变而 token 下降、代表性上升；若加入大量重复项，$\Delta$files 为正但代表性边际低。主状态不使用 gold gain；评价阶段再比较 $\delta_t$ 与真实 gold/downstream gain 的关系。

#### 4.3.3 表示稳定与来源分歧

集合稳定定义为 $J_t=|S_t\cap S_{t-1}|/|S_t\cup S_{t-1}|$，路径和跨度级分别计算。若定位器输出文件分布 $p_t$，分布变化用 Jensen–Shannon divergence：

\[
D_t^{JS}=\frac12D_{KL}(p_t\|m_t)+\frac12D_{KL}(p_{t-1}\|m_t),
\quad m_t=\frac12(p_t+p_{t-1}).
\tag{4}
\]

还计算证据角色分布、查询嵌入和固定上下文摘要表示的变化。来源一致性 $\rho_t$ 包括排名相关、top-k 交集、唯一来源命中和熵。高一致性只有与较高满足或下游值共同出现时才支持停止。

#### 4.3.4 成本与执行反馈

累计成本向量 $C_{1:t}$ 分别记录检索查询、读取/打包 token、下游上下文 token、工具调用、墙钟时延和货币成本；不预先压成一个数字。下一轮成本预测 $\hat c_{t+1}$ 由历史同策略日志和当前来源配置估计。若启用执行状态，$\epsilon_t$ 记录编译是否通过、失败测试集合、错误类型和相邻轮变化；未来测试结果不得回填当前状态。

### 4.4 路径内最优停止标签

#### 4.4.1 立即停止效用

对任务 $i$ 在前缀 $t$ 的一次回放，终局任务得分为 $y_{it}$，生成和执行成本为 $c_{it}^{d}$。立即停止效用定义为

\[
u_{it}=y_{it}-\lambda_d c_{it}^{d}.
\tag{5}
\]

$y_{it}$ 在补全任务可为 EM/Edit Similarity，在 issue 修复任务主值为测试通过或 resolved，并可保留连续部分测试改善作为次要信号。二元 resolved 与连续代理分开训练/报告，不通过任意加权混成不可解释分数。

模型随机性使 $u_{it}$ 为随机变量。主全量标签先以单个冻结种子生成；分层子样本多种子估计均值与方差，并检验单种子标签的稳定性。资源允许时，对接近停止边界的前缀优先追加重复，而不是平均分配所有回放。

#### 4.4.2 后向归纳

令从 $t$ 继续到 $t+1$ 的检索成本为 $c_{i,t+1}^{r}$，轨迹末端 $H_i$ 的路径内价值为

\[
V_{iH_i}=u_{iH_i}.
\tag{6}
\]

随后后向递推

\[
V_{it}=\max\left\{u_{it},-\lambda_r c_{i,t+1}^{r}+V_{i,t+1}\right\},
\quad t=H_i-1,\ldots,0.
\tag{7}
\]

若第一项较大，oracle 动作为 stop；若第二项较大，动作为 continue；接近相等时按预注册容忍区间标为等价动作。该递推允许后续效用下降：即使第 $t+1$ 轮较差，继续值仍包含以后可能恢复的前缀；也允许在成功后继续导致失败，从而使更早停止最优。

式（7）的 oracle 只知道实际 $\pi_c$ 路径的未来。它不比较另一条未执行查询、另一检索器或另一编辑策略；因此称为 **fixed-path prefix oracle**。训练标签中使用未来结果是监督构造所需，但在线特征严格不含未来。数据集同时发布标签生成脚本、轨迹 ID 和回放状态，避免把 oracle 泄漏隐入特征。

### 4.5 停止值、继续值与在线策略

EMS 分别估计

\[
\widehat U(s_t)=\mathbb E[u_t\mid s_t],
\tag{8}
\]

以及

\[
\widehat V^+(s_t)=\mathbb E[V_{t+1}\mid s_t,\pi_c].
\tag{9}
\]

主模型采用可校准的梯度提升树或广义加性模型，序列模型作为容量扩展而非默认。分别估计两个值比直接分类 stop/continue 更符合理论目标，也允许运营者改变成本权重后重新决策。模型使用按仓库分组的训练集，前缀来自同一任务时不能跨训练和测试。

继续净优势为

\[
A^{\mathrm{cont}}(s_t)=\widehat V^+(s_t)-\lambda_r\widehat c_{t+1}
-\widehat U(s_t).
\tag{10}
\]

最终策略为

\[
\pi_{EMS}(s_t)=
\begin{cases}
\text{continue}, & A^{\mathrm{cont}}(s_t)>\tau+\beta\widehat\sigma(s_t),\\
\text{stop}, & \text{otherwise},
\end{cases}
\tag{11}
\]

其中 $\widehat\sigma$ 表示价值差不确定性，$\tau$ 是继续所需最小优势，$\beta$ 控制风险缓冲。若过早停止代价很高，可以降低 $\tau$ 或采用非对称损失；若资源稀缺，可以提高它。外分布任务可退化到在验证集选择的 Fixed-$k$ 或 Fixed-Max 策略。

### 4.6 训练与部署算法

```text
数据生成：
1  冻结仓库、continuation policy、打包器、下游决策器和最大时域
2  对每个训练任务运行最大轨迹，保存每个检查点的完整前缀与成本
3  从干净环境独立运行每个前缀的终局决策，得到 u_it
4  沿固定路径后向递推 V_it 与 oracle stop/continue
5  仅从当时日志抽取满足、增量、稳定、分歧和成本状态

模型训练：
6  按仓库划分，拟合停止值 U、继续值 V+ 与不确定性
7  在验证仓库选择 tau、beta 和保守退化策略

在线部署：
8  每轮完成后计算当前 s_t
9  若继续净优势高于风险阈值且未达硬上限，则执行冻结 continuation
10 否则停止并把当前上下文交给冻结下游决策器
11 记录价值分解、行动、实际成本与结构化理由
```

数据生成的主要成本不是特征抽取，而是每个前缀的终局模型调用和测试。本文将先在 RepoBench/CrossCodeEval 的可执行补全上验证流程，再在 SWE-Explore/ContextBench 全量任务上用检索代理开发，最后对按仓库、语言、难度和轨迹长度分层的真实修复子样本运行 prefix replay。代理与真实结果始终分栏，不用前者填补后者。

## 5. 实证评价

### 5.1 数据

SWE-Explore 是过程评价主数据。按 2026 年 8 月公开版本，它包含 848 个 issue、203 个仓库和 10 种语言，并提供由成功轨迹聚合的核心/可选代码区域、预算排名与受限上下文验证（Zhang et al. 2026）。本文使用其仓库和 gold region 计算满足、增量和检索代理，但不把原有最终轨迹直接当作停止最优；必须用冻结 $\pi_c$ 重新生成可控轨迹。

ContextBench 包含 1,136 个 issue、66 个仓库和 8 种语言，提供文件、代码块或行级金标准及 agent 轨迹评价（Li et al. 2026）。它用于验证状态特征能否跨粒度工作。ARB 的正检索和 no-gold 子任务检验“继续找证据”与“本就没有仓库证据”的边界（Qin and Xie 2026）。RepoBench-P 与 CrossCodeEval 用于低成本前缀补全，SWE-bench Verified 的分层子样本用于真实补丁回放（Ding et al. 2023; Jimenez et al. 2024; Liu et al. 2024）。

所有任务按仓库划分。若同一 issue 产生多个前缀，它们只能属于同一数据分区；标准化、特征选择、$H$、$\lambda$、$\tau$ 和 $\beta$ 全部在训练/验证仓库确定。每次回放从 base commit 干净环境启动，模型和 evaluator 版本冻结。环境失败、超时和不可重现任务按预注册规则计为单独失败类型，不静默删除。

### 5.2 主要实验

实验 1 比较 EMS 与固定/启发式停止在终局任务效用和获取成本上的表现。实验 2 评价停止值、继续值、动作、校准和 regret，并把同一状态表示交给多个浅层预测器以排除单个预测头解释。实验 3 以 Fixed-Max 和 Oracle Prefix 建立“取得最多信息”和“路径内最佳时点”的强边界。实验 4 把 EMS 嵌入两个冻结 continuation policy，检验其增量是否跨 agent 保持。随后用四类状态的轨迹曲线回答 RQ1，并用消融归因。

基线包括 Fixed-0/1/2/.../Max、Fixed Token Budget、No-new-file、Difference Threshold、Stability Threshold、Mental-list Coverage、LLM Self-Stop、Repoformer-style one-shot selective、EMS-NoRisk 和 Oracle Prefix。所有阈值在验证仓库选择。LLM Self-Stop 使用同一模型和冻结提示，其判断 token、时延和调用费计入成本。Oracle 只作上界。

主指标包括任务通过/EM、平均轮数、上下文 token、工具调用、总时延、每成功成本、停止值 MAE、继续优势 MAE、Brier/ECE、stop regret、premature-stop、late-stop、首次成功前缀后的额外轮数和失败任务无效消耗。定义策略 regret 为

\[
\operatorname{StopRegret}_i(\pi)=V_{i0}^{oracle}-
\left(u_{i,T_i^\pi}-\lambda_r C_{i,1:T_i^\pi}^{r}\right).
\tag{12}
\]

动作准确率只作次要指标，因为多数前缀可能属于同一动作且近似等价。统计推断按仓库聚类 bootstrap；多模型随机性在预注册子样本用层级模型或多种子 bootstrap 处理 `[待确定]`。

### 5.3 实验结果

> 本节是结果模板，不是已有发现。

#### 5.3.1 实验 1：终局任务效用与成本

**表 2  停止策略的终局表现 `[待实验]`**

| 策略 | 任务效用 | 平均轮数 | 上下文 token | 工具调用 | P95 时延 | 每成功成本 | 净效用 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Fixed-1 | [待实验] | 1 | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| Fixed-Max | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| Difference Threshold | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| LLM Self-Stop | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| EMS | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |

结果先报告同任务配对差异和置信区间 `[待实验]`，再区分三种可能模式。若 EMS 保持 Fixed-Max 的任务效用并减少轮次，贡献是无明显质量损失的效率；若相同成本下任务效用更高，说明状态依赖分配改善了信息使用；若通过率下降但成本显著降低，则只是改变风险偏好，必须用不同 $\lambda$ 前沿呈现，不能称为全面改进。

#### 5.3.2 实验 2：价值、动作与状态表示

**表 3  停止价值与动作预测 `[待实验]`**

| 方法 | Stop-value MAE | Continue-advantage MAE | 动作准确率 | Stop regret | Premature | Late | 校准误差 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Difference Threshold | — | — | [待实验] | [待实验] | [待实验] | [待实验] | — |
| Stability Threshold | — | — | [待实验] | [待实验] | [待实验] | [待实验] | — |
| LLM Self-Stop | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| EMS | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |

随后把完整状态分别输入 logistic/GAM、随机森林和梯度提升，比较其跨预测器平均秩。若多种预测器都能从状态降低 regret，说明理论驱动表示本身有用；若只有高容量模型有效，则可能来自模型拟合而非清晰状态。继续优势的校准尤其重要：高置信继续若频繁无收益，在线策略会系统性 late-stop。

#### 5.3.3 实验 3：Fixed-Max 与 Oracle Prefix 强边界

Fixed-Max 表示允许固定流程探索到最大预算，通常最不容易因缺信息失败，却可能承担最大成本和信息干扰。Oracle Prefix 用未来前缀结果选择路径内最优时点，是 EMS 可逼近但不可在线达到的上界。

**表 4  强基线与可改善空间 `[待实验]`**

| 策略 | 任务效用 | 成功任务最早可停轮 | 成功后额外轮 | 失败任务无效轮 | Stop regret |
|---|---:|---:|---:|---:|---:|
| Fixed-Max | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| Best Fixed-k | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| EMS | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| Oracle Prefix | [待实验] | [待实验] | 0 | [待实验] | 0 |

Oracle 与 Best Fixed-k 的差距衡量任务条件停止的最大路径内空间；若差距很小，复杂停止器没有必要。Oracle 与 EMS 的差距衡量状态和估计仍未捕捉的价值。若 Fixed-Max 的后续轮次经常降低实际任务效用，可进一步检验信息平台期或下降；仅成本增加而质量不变不能称为信息过量。

#### 5.3.4 实验 4：跨 continuation policy 的增量

**表 5  EMS 嵌入不同固定探索器 `[待实验]`**

| Continuation policy | 固定停止效用 | EMS 效用 | token 改变 | regret 改变 | 交叉训练结果 |
|---|---:|---:|---:|---:|---:|
| Policy A | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| Policy B | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |

先在各策略自身轨迹上训练测试，再把 A 上训练的 EMS 应用于 B，反之亦然。若同策略有效而交叉失效，停止状态依赖基础执行器，贡献需限定；若方向稳定，说明满足、增量和稳定具有一定可迁移性。任何情况下都不把两条路径的 oracle 直接比较为查询策略优劣，因为它们访问的状态不同。

### 5.4 探索性分析

#### 5.4.1 目标证据满足

按 query 可提取实体数量和任务结构化程度绘制 $\kappa_t$ 与立即停止效用。检验关键测试、错误符号或编辑位置的满足是否在特定任务中形成单一准则，以及显式清单为空时模型是否依赖其他信号 `[待实验]`。该分析回答“什么样的任务可用清单停止”，而不声称 agent 在心理上维护清单。

#### 5.4.2 边际新颖性

绘制每轮新文件、新结构单元、代表性增益和真实 $u_{t}-u_{t-1}$。比较“新增很多但效用下降”“文件不增但跨度替换后效用提高”和“关键单元首次出现后成功”三类案例 `[待实验]`。如果简单无新文件规则已经接近 EMS，完整增量设计应被收缩。

#### 5.4.3 表示稳定

按集合 Jaccard 与定位分布变化划分稳定度，比较其与任务效用和 oracle 动作的关系。重点识别错误稳定：高稳定、低满足且持续失败。若稳定只有与高满足联合才有预测力，正文将其写成条件机制而非独立规则 `[待实验]`。

#### 5.4.4 信息量—任务效用曲线

对每个任务记录累计 token、轮数和立即停止效用，用任务固定效应的分段模型或非参数平滑估计总体及分层曲线。区分单调增加、平台和下降三种轨迹。只有控制任务难度且同任务后续前缀表现下降时，才讨论 coding agent 情境中的负边际信息；不能把人类“过载”机制直接套用。

### 5.5 消融分析

依次移除目标满足、边际新颖、表示稳定、来源分歧、累计成本和可选执行反馈；另比较直接动作分类与双价值估计、无风险缓冲与完整 EMS。

**表 6  EMS 组件消融 `[待实验]`**

| 变体 | Stop regret | Premature | Late | 任务效用 | token | 校准误差 |
|---|---:|---:|---:|---:|---:|---:|
| 无满足 | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| 无增量 | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| 无稳定 | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| 无成本 | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| 直接分类 | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |
| 完整 EMS | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] | [待实验] |

组件只有在对应错误按理论方向变化时才得到支持。例如，去满足若增加结构化任务的 premature-stop，支持清单信号；去稳定若增加成功后的无效轮次，支持稳定信号；去成本若只增加轮数而任务不变，支持净价值目标。若完整状态并不优于 difference threshold，应保留简单规则并放弃复杂制品优势。

## 6. 贡献与启示

本文的第一项潜在贡献是把 coding-agent 仓库探索中的信息充分性概念化为四个可观察维度。已有工程实践以轮数或 token 表示充分，本文区分目标证据满足、最新边际新颖、跨轮表示稳定和成本调整继续价值，并把它们定位在任务、前缀、轮次和证据单元四个层次。该概念化把 IS 停止理论从人类在线搜索和需求获取情境扩展到数字 agent，但严格保留迁移边界：状态是外部日志，不是 LLM 认知。

第二项潜在贡献是 EMS 这一设计科学制品及其数据构造。EMS 不依赖现成 benchmark 已经提供停止标签，而用冻结 continuation policy、上下文封闭的下游决策器、独立 prefix replay 和路径内后向归纳生成可审计反事实。双价值估计允许成本和风险参数改变，结构化理由直接来自状态和价值分解。若评价获得支持，该流程可以复用于其他具有可执行终局评价的 agent 信息获取任务。

第三项潜在贡献是关于停止条件的经验知识。本文将检验结构化 query 是否更适合目标清单、弱结构任务是否更依赖稳定、最新结构单元是否比新文件数更能预测继续价值，以及更多上下文何时进入平台或下降。所有规律都按 continuation policy、仓库、语言和任务类型限定。模型特征贡献只能说明这些信号对外部停止结果有预测关系，不证明人类停止理论在 LLM 内部被复制。

实践上，agent 开发者应把“为什么继续”与“为什么停止”记录为显式价值比较，而不只设最大循环数。benchmark 维护者可发布可恢复前缀、冻结环境和受限上下文 evaluator，使停止研究无需重新构造全部基础设施。企业部署者可以根据失败代价设置非对称风险缓冲，并查看 premature/late-stop 而不是只看平均 token。基础设施提供者则应记录每轮新增证据、集合变化、来源分歧和真实时延，为停止器提供忠实状态。

## 7. 结论

本文研究 coding agent 在迭代仓库检索中何时已经取得足够信息。基于信息充分性和序贯信息价值，本文提出四类状态，并用 prefix replay、fixed-path oracle 和双价值估计构成 EMS。公开 benchmark 提供了可运行任务、仓库、轨迹和金标准，真实前缀停止效用则通过受控回放生成；研究因而既利用成熟基础设施，又诚实承认新增数据成本。实证结果为 `[待实验]`。

本研究存在四类边界。第一，EMS 只对冻结 continuation policy 求路径内停止，未考虑未执行查询、替代工具或编辑策略，不能称为全局最优 agent。第二，prefix replay 计算昂贵且受生成随机性影响；有限多种子会造成标签噪声，端到端子样本也限制统计功效。第三，SWE-Explore、ContextBench、ARB 和 SWE-bench 的仓库与语言仍不足以代表私有仓库、动态系统和非代码证据。第四，充分性特征、成本权重、最大时域和风险阈值均依赖基础模型与部署环境，跨模型版本需重新校准。

未来研究可以在保持可识别性的前提下逐步放宽边界，例如比较多个固定 continuation policy、用离线策略评价处理有限查询分支、把执行反馈纳入状态，或联合学习来源配置与停止。但若行动空间扩大到完整 agent，研究必须重新解决未执行分支反事实、策略选择偏差和计算可行性，不能沿用本文路径内 oracle 的结论。

## 参考文献

Browne, G. J., Pitts, M. G., & Wetherbe, J. C. (2007). Cognitive stopping rules for terminating information search in online tasks. *MIS Quarterly, 31*(1), 89–104. https://doi.org/10.2307/25148782

Browne, G. J., & Walden, E. A. (2021). Stopping information search: An fMRI investigation. *Decision Support Systems, 143*, 113498. https://doi.org/10.1016/j.dss.2021.113498

Chen, G., Xiao, S., Zhang, C., & Zhao, H. (2023). A theory-driven deep learning method for voice chat-based customer response prediction. *Information Systems Research, 34*(4), 1513–1532. https://doi.org/10.1287/isre.2022.1196

Ding, Y., Wang, Z., Ahmad, W. U., Ding, H., Tan, M., Jain, N., Ramanathan, M. K., Nallapati, R., Bhatia, P., Roth, D., & Xiang, B. (2023). CrossCodeEval: A diverse and multilingual benchmark for cross-file code completion. *Advances in Neural Information Processing Systems, 36*, Datasets and Benchmarks Track.

Gregor, S., & Hevner, A. R. (2013). Positioning and presenting design science research for maximum impact. *MIS Quarterly, 37*(2), 337–355.

Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. *MIS Quarterly, 28*(1), 75–105.

Hong, W., Chan, F. K. Y., Thong, J. Y. L., Chasalow, L. C., & Dhillon, G. (2014). A framework and guidelines for context-specific theorizing in information systems research. *Information Systems Research, 25*(1), 111–136.

Hosanagar, K. (2011). Usercentric operational decision making in distributed information retrieval. *Information Systems Research, 22*(4), 739–755. https://doi.org/10.1287/isre.1100.0287

Jimenez, C. E., Yang, J., Wettig, A., Yao, S., Pei, K., Press, O., & Narasimhan, K. R. (2024). SWE-bench: Can language models resolve real-world GitHub issues? *International Conference on Learning Representations*.

Li, H., Zhu, L., Zhang, B., Feng, R., Wang, J., Pan, Y., Barr, E. T., Sarro, F., Chu, Z., & Ye, H. (2026). ContextBench: A benchmark for context retrieval in coding agents. *arXiv preprint arXiv:2602.05892*.

Liu, T., Xu, C., & McAuley, J. (2024). RepoBench: Benchmarking repository-level code auto-completion systems. *International Conference on Learning Representations*.

Moore, J. C., & Whinston, A. B. (1986). A model of decision-making with sequential information-acquisition (Part 1). *Decision Support Systems, 2*(4), 285–307.

Moore, J. C., & Whinston, A. B. (1987). A model of decision-making with sequential information-acquisition (Part 2). *Decision Support Systems, 3*(1), 47–72.

Mullins, J. K., & Sabherwal, R. (2022). Just enough information? The contingent curvilinear effect of information volume on decision performance in IS-enabled teams. *MIS Quarterly, 46*(4), 2197–2228. https://doi.org/10.25300/MISQ/2022/17290

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems, 24*(3), 45–77.

Peskir, G., & Shiryaev, A. (2006). *Optimal stopping and free-boundary problems*. Birkhäuser.

Pitts, M. G., & Browne, G. J. (2004). Stopping behavior of systems analysts during information requirements elicitation. *Journal of Management Information Systems, 21*(1), 203–226. https://doi.org/10.1080/07421222.2004.11045795

Qin, B., & Xie, Y. (2026). Agent Retrieval Bench: Evaluating repository context retrieval for coding agents. *arXiv preprint arXiv:2607.24882*.

Voorberg, S., Eshuis, R., van Jaarsveld, W., & van Houtum, G. J. (2021). Decisions for information or information for decisions? Optimizing information gathering in decision-intensive processes. *Decision Support Systems, 151*, 113632. https://doi.org/10.1016/j.dss.2021.113632

Wald, A. (1947). *Sequential analysis*. Wiley.

Wu, D., Ahmad, W. U., Zhang, D., Ramanathan, M. K., & Ma, X. (2024). Repoformer: Selective retrieval for repository-level code completion. *Proceedings of ICML 2024*, 53270–53290.

Xia, C. S., Deng, Y., Dunn, S., & Zhang, L. (2025). Agentless: Demystifying LLM-based software engineering agents. *Proceedings of the ACM on Software Engineering, 2*(FSE).

Yang, J., Jimenez, C. E., Wettig, A., Lieret, K., Yao, S., Narasimhan, K., & Press, O. (2024). SWE-agent: Agent-computer interfaces enable automated software engineering. *Advances in Neural Information Processing Systems, 37*.

Zhang, F., Chen, B., Zhang, Y., Keung, J., Liu, J., Zan, D., Mao, Y., Lou, J.-G., & Chen, W. (2023). RepoCoder: Repository-level code completion through iterative retrieval and generation. *Proceedings of EMNLP 2023*, 2471–2484.

Zhang, K., Li, J., Li, G., Shi, X., & Jin, Z. (2024). CodeAgent: Enhancing code generation with tool-integrated agent systems for real-world repo-level coding challenges. *Proceedings of ACL 2024*, 13643–13658.

Zhang, S., Wang, Y., Liang, J., Shi, Y., Zeng, W., Wang, M., He, S., Xu, N., Ye, S., Cai, K., & Gu, X. (2026). SWE-Explore: Benchmarking how coding agents explore repositories. *arXiv preprint arXiv:2606.07297*.

Busemeyer, J. R. (1982). Choice behavior in a sequential decision making task. *Organizational Behavior and Human Decision Processes, 29*(2), 175–207.

Busemeyer, J. R., & Rapoport, A. (1988). Psychological models of deferred decision making. *Journal of Mathematical Psychology, 32*(2), 91–134.

Chen, G., Huang, L., Xiao, S., Zhang, C., & Zhao, H. (2024). Attending to customer attention: A novel deep learning method for leveraging multimodal online reviews to enhance sales prediction. *Information Systems Research, 35*(2), 829–849. https://doi.org/10.1287/isre.2021.0292

Chen, Z., Tang, R., Deng, G., Wu, F., Wu, J., Jiang, Z., Prasanna, V., Cohan, A., & Wang, X. (2025). LocAgent: Graph-guided LLM agents for code localization. *Proceedings of ACL 2025*, 8697–8727. https://doi.org/10.18653/v1/2025.acl-long.426

Cheng, W., Wu, Y., & Hu, W. (2024). Dataflow-guided retrieval augmentation for repository-level code completion. *Proceedings of ACL 2024*, 7957–7977. https://doi.org/10.18653/v1/2024.acl-long.431

Chow, Y. S., Robbins, H., & Siegmund, D. (1971). *Great expectations: The theory of optimal stopping*. Houghton Mifflin.

Connolly, T., & Gilani, N. (1982). Information search in judgment tasks: A regression model and some preliminary findings. *Organizational Behavior and Human Decision Processes, 30*(3), 330–350.

Connolly, T., & Thorn, B. K. (1987). Predecisional information acquisition: Effects of task variables on suboptimal search strategies. *Organizational Behavior and Human Decision Processes, 39*(3), 397–416.

Gaeth, G. J., & Shanteau, J. (1984). Reducing the influence of irrelevant information on experienced decision makers. *Organizational Behavior and Human Decision Processes, 33*(2), 263–282.

Gigerenzer, G., & Goldstein, D. G. (1999). Betting on one good reason: The take the best heuristic. In G. Gigerenzer, P. M. Todd, & the ABC Research Group (Eds.), *Simple heuristics that make us smart* (pp. 75–95). Oxford University Press.

Glazer, R., Steckel, J. H., & Winer, R. S. (1992). Locally rational decision making: The distracting effect of information on managerial performance. *Management Science, 38*(2), 212–226.

Guo, C., Pleiss, G., Sun, Y., & Weinberger, K. Q. (2017). On calibration of modern neural networks. *Proceedings of ICML 2017*, 1321–1330.

Guo, J., Wang, C., Xu, X., Su, Z., & Zhang, X. (2025). RepoAudit: An autonomous LLM-agent for repository-level code auditing. *Proceedings of ICML 2025*, 21083–21100.

He, P., Wang, S., & Chen, T.-H. (2026). CodePromptZip: Code-specific prompt compression for retrieval-augmented generation in coding tasks with LMs. *Findings of ACL 2026*, 27811–27825. https://doi.org/10.18653/v1/2026.findings-acl.1384

Hu, R., Peng, C., Wang, X., Xu, J., & Gao, C. (2025). Repo2Run: Automated building executable environment for code repository at scale. *Advances in Neural Information Processing Systems, 38*.

Lakshminarayanan, B., Pritzel, A., & Blundell, C. (2017). Simple and scalable predictive uncertainty estimation using deep ensembles. *Advances in Neural Information Processing Systems, 30*.

Liu, A., Song, S., Li, H., Yang, C., & Qi, Y. (2025). Beyond function-level search: Repository-aware dual-encoder code retrieval with adversarial verification. *Findings of EMNLP 2025*, 21034–21049. https://doi.org/10.18653/v1/2025.findings-emnlp.1147

Marakas, G. M., & Elam, J. J. (1998). Semantic structuring in analyst acquisition and representation of facts in requirements analysis. *Information Systems Research, 9*(1), 37–63.

Miyake, N., & Norman, D. A. (1979). To ask a question, one must know enough to know what is not known. *Journal of Verbal Learning and Verbal Behavior, 18*(3), 357–364.

Mookerjee, V. S., & Dos Santos, B. L. (1993). Inductive expert system design: Maximizing system value. *Information Systems Research, 4*(2), 111–133.

Mookerjee, V. S., & Mannino, M. V. (1997). Redesigning case retrieval to reduce information acquisition costs. *Information Systems Research, 8*(1), 51–68.

Mookerjee, V. S., & Mannino, M. V. (2000). Mean-risk trade-offs in inductive expert systems. *Information Systems Research, 11*(2), 137–153.

Ouyang, S., Yu, W., Ma, K., Xiao, Z., Zhang, Z., Jia, M., Han, J., Zhang, H., & Yu, D. (2025). RepoGraph: Enhancing AI software engineering with repository-level code graph. *International Conference on Learning Representations*.

Payne, J. W., Bettman, J. R., & Johnson, E. J. (1992). Behavioral decision research: A constructive processing perspective. *Annual Review of Psychology, 43*, 87–131.

Pitz, G. F., Reinhold, H., & Geller, E. S. (1969). Strategies of information seeking in deferred decision making. *Organizational Behavior and Human Performance, 4*(1), 1–19.

Puterman, M. L. (1994). *Markov decision processes: Discrete stochastic dynamic programming*. Wiley.

Rapoport, A., Lissitz, R. W., & McAllister, H. A. (1972). Search behavior with and without optional stopping. *Organizational Behavior and Human Performance, 7*(1), 1–17.

Rapoport, A., & Tversky, A. (1970). Choice behavior in an optional stopping task. *Organizational Behavior and Human Performance, 5*(2), 105–120.

Saar-Tsechansky, M., & Provost, F. (2007). Decision-centric active learning of binary-outcome models. *Information Systems Research, 18*(1), 4–22.

Saad, G., & Russo, J. E. (1996). Stopping criteria in sequential choice. *Organizational Behavior and Human Decision Processes, 67*(3), 258–270.

Shinn, N., Cassano, F., Gopinath, A., Narasimhan, K., & Yao, S. (2023). Reflexion: Language agents with verbal reinforcement learning. *Advances in Neural Information Processing Systems, 36*.

Shrivastava, D., Larochelle, H., & Tarlow, D. (2023). Repository-level prompt generation for large language models of code. *Proceedings of ICML 2023*, 31693–31715.

Stigler, G. J. (1961). The economics of information. *Journal of Political Economy, 69*(3), 213–225.

Todd, P., & Benbasat, I. (1987). Process tracing methods in decision support systems: Exploring the black box. *MIS Quarterly, 11*(4), 493–512.

Wang, Z. Z., Asai, A., Yu, X. V., Xu, F. F., Xie, Y., Neubig, G., & Fried, D. (2025). CodeRAG-Bench: Can retrieval augment code generation? *Findings of NAACL 2025*, 3199–3214. https://doi.org/10.18653/v1/2025.findings-naacl.176

Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2023a). ReAct: Synergizing reasoning and acting in language models. *International Conference on Learning Representations*.

Yao, S., Yu, D., Zhao, J., Shafran, I., Griffiths, T. L., Cao, Y., & Narasimhan, K. (2023b). Tree of thoughts: Deliberate problem solving with large language models. *Advances in Neural Information Processing Systems, 36*.

Yin, X., Ding, Z., Zhang, Y., Wang, Q., Wang, R., Ni, C., & Cui, Z. (2026). RepoDistill: Distilling repository knowledge through compression-aware budget allocation and policy optimization. *Findings of ACL 2026*, 4425–4443. https://doi.org/10.18653/v1/2026.findings-acl.217

Newell, A., & Simon, H. A. (1972). *Human problem solving*. Prentice-Hall.

## 附录 A：固定路径 oracle 的边界例子

若 $\pi_c$ 在第 2 轮错误地继续沿模块 A 搜索，而另一未执行查询可以转向真正根因模块 B，式（7）只能在 A 路径上选择第 1、2、…轮何时停止。它不会发现 B，也不能据此评价查询生成器是否最优。因此，EMS 可以减少 A 路径上的无效轮次，却不能替代检索策略研究。

## 附录 B：预注册收缩规则

1. 若 Oracle Prefix 与 Best Fixed-k 差距很小，停止个性化缺少必要空间。
2. 若 EMS 只在代理效用有效而真实 patch 无效，结论限定为检索停止。
3. 若交叉 policy 失效，状态规律限定在基础执行器内。
4. 若稳定特征导致错误稳定，删除或条件化该组件，而非保留理论预期。
5. 若多种子标签不稳定，增加重复或报告不确定区间，不选择性保留有利种子。

## 附录 C：待补齐引文与实现

- coding agent 工程中固定预算、无新文件和 LLM 自报停止的系统综述 `[待引用]`；
- 冻结 continuation policy、下游决策器和模型版本 `[待确定后引用]`；
- 右删失轨迹与近边界多种子分配的统计方案 `[待方法核验]`；
- 2026 年 benchmark 的最终版本、许可证与 release tag `[待复核]`。
