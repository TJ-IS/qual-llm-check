# 公允 SOTA 声明审计：三研究外部 Benchmark 与统一比较协议

## 0. 审计结论

截至 2026 年 8 月 20 日，114 号方案能够支持“公开数据上的可实现研究链”，但**尚不能支持公允的 SOTA 声明**。34—36 号现有评价设计存在三类根本问题：

1. 直接竞争基线缺失。研究一未比较 RedCodeAgent，研究二未比较 MalSkillBench 的统一检测工具、CodeSentinel、Semia 或 MalSkills，研究三未比较 Task Shield、AgentArmor、ClawGuard 或 AgentSentinel。
2. 自产数据承担过多角色。`D_att` 同时由研究一生成、为研究二和三训练、又用于主要评价时，容易把“适配同一生成机制”误写成“优于 SOTA”。
3. 比较条件不一致。当前设计尚未固定 victim agent、模型版本、系统提示、工具集、攻击/防御预算、成功验证器和推理成本；不同方法的 ASR、F1 或防御成功率不能直接排名。

正确判断不是放弃现有研究，而是把评价改为双轨：

- **外部公共轨负责 SOTA 证据**：在竞争方法已经使用或能够公平适配的公开 benchmark 上，使用相同输入、环境、预算、验证器和官方指标重新运行所有方法。
- **本项目原生轨负责机制与系列贡献**：在 `D_att-static` 和 `D_att-trace` 上检验跨通道攻击、双视图数据复用、理论机制、定位、危害前检测和自适应压力测试，但不单独据此宣称 SOTA。

只有外部公共轨胜出，才能使用“在某 benchmark 上达到新的最佳结果”。仅在原生轨胜出，应写“在我们提出的跨通道设定中优于适配基线”，不能写成领域总体 SOTA。

## 1. 当前三篇为什么还不公允

### 1.1 研究一

34 号目前比较 SWExploit、FCV、随机改写和待核实的 RLbreaker，已经不足以代表 2026 年自动红队水平。[RedCodeAgent](https://github.com/1mocat/RedCodeAgent) 是 ICLR 2026 的直接竞争者，结合记忆和攻击工具箱自适应攻击 code agents，并在 RedCode-Exec 上采用执行验证。其公开实现覆盖 27 类 Python 风险场景，每类 30 个实例，同时提供 C、C++ 和 Java 变体。

现有设计还有三项偏差：

- “规则或 LLM 裁判任一判有害即算成功”会扩大假阳性，且自产攻击可能更容易命中自产规则。主要 ASR 必须由任务特定的执行 oracle、PoC 或环境状态检查决定；LLM judge 只能处理无确定性 oracle 的辅助标签。
- `D_att` 目前只纳入成功攻击，无法完整反映攻击生成器的尝试分布、失败模式和选择偏差。应发布全部候选或至少发布成功、失败、无效和功能破坏四类回合。
- 没有统一目标查询、候选生成、token、工具调用和执行次数预算。强化学习方法若获得更多 victim feedback，即使 ASR 更高也不能称为公平胜出。

### 1.2 研究二

35 号目前的五类基线主要是无防御、随机、规则、全量扫描、文本或浅层分类器。这些基线可以做消融，但不足以支撑 SOTA。

[MalSkillBench](https://github.com/lxyeternal/MalSkillBench) 已经公开 3,944 个运行验证的恶意 skills、4,000 个匹配良性 skills、12 类检测工具和统一评估流水线；其论文显示最强 skill-specific detector 的总体 F1 仍只有 88.6%，并且代码注入、prompt 注入和 agent-control 攻击之间表现差异巨大。[CodeSentinel](https://arxiv.org/abs/2606.19235) 在代码上下文中的六类攻击上报告 0.80 的 node-level F1；[Semia](https://arxiv.org/abs/2605.00314) 在 541 个专家标注 skills 上报告 90.6% F1；[MalSkills](https://arxiv.org/abs/2603.27204) 在 200 个真实 skills 上报告 93% F1。这些结果未必都能直接复现，但它们决定了审稿人理解的竞争前沿。

当前研究二还存在两个泄漏风险：

- 若同一干净模板的攻击版进入训练、干净版进入测试，模型可能识别模板或仓库身份，而不是识别操纵机制。
- 若测试时提供攻击前后的配对快照，任务会退化成 diff 检测。配对只用于训练监督和标签生成，正式测试只能提供当前任务前快照。

### 1.3 研究三

36 号目前比较关键词、黑盒 LLM judge、文本单通道、无状态检查和无门控检测。这些属于最低基线，不是 2026 年运行防御前沿。

直接竞争者至少包括：

- [Task Shield](https://arxiv.org/abs/2412.16682)：在每条指令和 tool call 上检查其是否服务于用户任务。
- [AgentArmor](https://arxiv.org/abs/2508.01249)：把运行轨迹重构为控制流、数据流与程序依赖图，并进行策略检查。
- [ClawGuard](https://github.com/Claw-Guard/ClawGuard)：在工具调用边界实施任务特定规则，已经在 AgentDojo、Skill-Inject 和 MCP 安全 benchmark 上与 Task Shield、MELON 做过统一适配比较。
- [AgentSentinel](https://github.com/m4p1e/agent-sentinel)：CCS 2025 的端到端实时防御，通过系统 trace 与任务上下文联合审计敏感操作。

此外，MalSkillBench 是以运行验证建立 skill 恶意真值的 benchmark，不自动等于“公开的完整 action–observation 序列数据集”。除非其发布包实际包含研究三所需的逐时间步 trace 和危害前门控点，否则不能把它直接列为研究三的弱标签轨迹来源。

## 2. SOTA 声明应分为三个等级

| 等级 | 证据 | 允许的表述 | 禁止的表述 |
|---|---|---|---|
| L0 内部优势 | 只在 `D_att` 或本项目任务上优于自选基线 | 在所提出设定中取得更好结果；组件产生增量 | SOTA；优于现有最佳方法 |
| L1 benchmark-specific SOTA | 在一个公开 benchmark 的官方/等价协议上，重跑强基线并显著胜出 | 在 X benchmark、Y 设置和 Z 指标上达到最佳结果 | coding-agent 安全总体 SOTA |
| L2 多 benchmark 稳健领先 | 在至少两个来源独立、攻击面不同的公开 benchmark 上保持安全—效用 Pareto 优势 | 在多项公开 benchmark 上一致优于现有可复现方法 | 对所有 coding agents/攻击均为 SOTA |

三篇至少应以 L1 为目标。研究一和研究三若能完成两个外部环境的完整适配，可争取 L2；研究二由于不同静态对象的输入 schema 差异大，更适合分别声明 skill、代码上下文或仓库载体上的 benchmark-specific 结果。

## 3. 双轨 benchmark 结构

### 3.1 研究一

| 轨道 | 数据/环境 | 主要比较对象 | 主要目的 | 可否支持 SOTA |
|---|---|---|---|---|
| 外部公共轨 A | RedCode-Exec，优先使用官方 Python 27×30 设置 | RedCodeAgent、其论文中的 No Jailbreak、GCG、AmpleGCG、AdvPrompter、AutoDAN 与组合基线 | 公平比较自动红队的攻击有效性和成本 | 可以，前提是完全一致的 victim、轮数和执行 oracle |
| 外部公共轨 B | [RepoGuardBench](https://github.com/DaoyuanLi2816/RepoGuardBench) 的仓库载体任务 | 其 D0—D5 防护条件下的固定攻击；将 RedCodeAgent/启发式攻击适配到共同对象 API | 验证 repository-borne 攻击与功能保持 | 可支持外部有效性；该项目明确不声称其防御为 SOTA，不能把胜出写成总体 SOTA |
| 条件外部轨 | JAWS-Bench、IssueTrojanBench | 论文公开攻击和可复现生成方法 | 多文件与恶意 issue 迁移 | 只有数据、代码、许可证和 oracle 均公开时才进入 |
| 原生轨 | SWE-bench/SWE-Gym 加 `D_att` | 同预算模板、随机、启发式、扁平 RL、无反馈 RL、适配 RedCodeAgent | 跨 issue/仓库/工具通道、覆盖和系列数据价值 | 不能单独支持 SOTA |

关键现实是：AttackRL 的 workspace 操纵动作与 RedCodeAgent 的 jailbreak 工具箱并不天然同构。不能简单把双方原论文 ASR 放在一张表。需要两种比较：

1. 在 RedCode-Exec 上给 AttackRL 增加 prompt/risky-code adapter，与 RedCodeAgent 按官方协议比较通用自动红队能力。
2. 在本项目原生轨中给 RedCodeAgent 和其他基线相同的“通道—单元—算子”动作 API、相同生成模型和相同 victim feedback，只比较策略如何选择攻击路径。

第二种比较更能检验 AttackRL 的算法增量，但仍属于新设定上的适配比较；第一种才提供已有公开 benchmark 上的 SOTA 证据。

### 3.2 研究二

| 轨道 | 数据 | 可复现基线 | 主要指标 | 作用 |
|---|---|---|---|---|
| 外部公共轨 A | MalSkillBench 官方发布 | 官方 12 个工具；Prompt Guard 2、DataSentinel、Attention Tracker、Snyk Agent Scan 等按官方 harness | macro/micro F1、precision、recall、FPR、分攻击向量结果、成本 | skill 静态检测的主要 SOTA 轨 |
| 外部公共轨 B | CodeSentinel 的六类代码上下文数据，前提是数据/代码发布 | CodeGarrison、DePA、KillBadCode、CodeSentinel | node-level F1、Recall@k、清洗后下游 ASR/效用 | 代码节点定位的主要 SOTA 轨 |
| 外部公共轨 C | RepoGuardBench 的五类载体 | D0—D5 以及可静态运行的检测器 | 攻击 proposed/landed rate、任务效用、误拦截 | 仓库级载体迁移 |
| 原生轨 | `D_att-static` | 相同 backbone 的内容-only、结构-only、来源-only、早/晚融合、关系图、SOTA 可适配检测器 | 任务级 AUPRC、单元 Recall@k、校准、预算下残余 ASR | 跨对象关系与理论机制 |

Semia、MalSkills 等论文若未发布足以重跑的代码与标注数据，应作为强相关结果和设计对照；不得把论文表中的数字与本项目在不同数据上的数字直接比较。若能够获得官方实现，则纳入相同外部 harness。

### 3.3 研究三

| 轨道 | 环境 | 基线 | 主要指标 | 作用 |
|---|---|---|---|---|
| 外部公共轨 A | [AgentDojo](https://github.com/ethz-spylab/agentdojo) 官方 97 个用户任务和 629 个 security cases | AgentDojo 内置防御、Task Shield、MELON、AgentArmor、ClawGuard 的等价适配 | benign utility、utility under attack、targeted ASR、安全—效用 Pareto | 通用动态 agent 防御的主要 SOTA 轨 |
| 外部公共轨 B | ClawGuard 已使用的 Skill-Inject 与 MCP 安全 benchmark | Task Shield、MELON、ClawGuard | ASR、任务效用、额外调用、延迟 | skill/tool 注入跨通道迁移 |
| 条件外部轨 | BadComputerUse | AgentSentinel 与其基线 | defense success、误报、延迟 | 系统级 trace 迁移；需要 Linux/eBPF 环境，成本较高 |
| 原生轨 | `D_att-trace` 加公开 coding-agent 正常轨迹 | runtime-only、`p0`-only、Task Shield adapter、AgentArmor-style graph、规则、LLM judge | 危害前检测/阻断、检测延迟、安全裕度、resolve rate、绕过率 | coding-agent 时序机制与研究二连接 |

AgentDojo 不是 coding-agent benchmark，因此它只能证明动态防御内核与现有通用方法的公允竞争。coding-agent 特殊性必须由 `D_att-trace`、RepoGuardBench 或其他可执行仓库环境证明。两类证据缺一不可。

## 4. 公允比较的十项不变量

### 4.1 相同 victim 与环境

同一比较表中的所有方法必须使用完全相同的：

- victim agent scaffold 与 commit。
- 基础模型名称、具体版本或 API snapshot。
- system prompt、tool descriptions、温度、最大 token、最大步骤和超时。
- 初始仓库/环境状态、容器镜像、网络策略和权限。

闭源模型更新会改变结果。应记录日期和版本；不能把不同月份的官方结果与新实验结果直接比较。

### 4.2 相同信息权限

- 白盒、灰盒、黑盒攻击分表报告。
- 如果 AttackRL 可看 victim 反馈，基线也应获得相同反馈。
- 如果本方法知道仓库图、目标文件或 ground-truth tool sequence，必须给适配基线相同信息，或把额外信息作为独立设置。
- 防御方法只能读取其声明时点可获得的信息。研究二不得读运行轨迹，研究三不得读未来时间步。

### 4.3 相同计算与查询预算

研究一至少同时固定并报告：

- 每任务 victim queries。
- 候选攻击数和最大迭代轮次。
- 攻击生成模型调用、token 和工具调用。
- 执行 oracle 次数、墙钟时间与硬件。

研究二、三至少报告：

- 每任务/每步模型调用和 token。
- 静态分析器或规则引擎调用。
- 峰值显存/内存、墙钟时间和单步 p50/p95 延迟。

公平不一定要求所有方法完全等成本，但必须给出预算匹配表和安全—成本 Pareto；不能只比较最高性能点。

### 4.4 相同确定性 oracle

主要结果优先使用环境状态、测试、PoC、系统调用或文件/网络副作用检查。LLM judge 仅在无法定义确定性 oracle 时使用，并须：

- 与人工双盲小样本比较一致性。
- 对所有方法使用同一 judge、prompt、temperature 和重试协议。
- 不让参与攻击生成或防御决策的模型同时担任唯一 judge。

### 4.5 条件化攻击成功率

能力较弱的 victim 可能因为连正常任务或恶意目标都执行不了而显得“安全”。研究一至少同时报告：

- clean task utility。
- unconditional ASR。
- conditional ASR：只在 victim 能完成对应良性任务/攻击目标执行链的样本上计算。
- harmful-and-functional rate：危害成立且原任务功能保持。

AgentDojo 已明确分开 benign utility、utility under attack 和 targeted ASR；研究三应沿用这种三指标结构，而不是只报告 F1。

### 4.6 对象级而非行级划分

- 仓库及近邻 commit 互斥。
- 同一良性模板及其所有攻击版本不得跨 split。
- payload 近重复、攻击知识库来源和攻击家族互斥。
- 同一 tool/skill 的不同版本成组划分。

随机按样本行切分会严重高估静态检测泛化。

### 4.7 外部测试不可参与开发

外部 benchmark 的 test split 不得用于：

- AttackRL 训练或 reward shaping。
- 研究二特征/理论选择和阈值调节。
- 研究三状态定义、门控阈值和对抗重训。

若 benchmark 没有官方 train/test，应一次性预注册分组划分并锁定 hash。开发只在 train/dev 上进行。

### 4.8 独立重跑而非抄表

所有进入同一排名表的方法应由本项目在统一 harness 中重跑。论文报告数字只能放入“文献参考结果”表，不得与本项目数字做显著性检验或直接排序，除非协议、版本和环境完全一致。

### 4.9 多随机种子与配对统计

对同一任务、victim 和 seed 配对比较。报告均值、95% 置信区间、每任务差值和适当的配对检验。除总体指标外，按攻击通道、家族、仓库和 victim 分层报告，避免总体均值掩盖某一类完全失败。

### 4.10 完整发布与版本冻结

发布 benchmark schema、任务清单、split hash、容器、模型/agent 配置、原始回合、成功与失败样本、评分脚本和表格再生脚本。外部 API 无法永久冻结时，至少发布完整输入输出与日期，并将可复现开源模型结果作为主表。

## 5. 三研究的冻结顺序

为防止系列内部循环，建议采用以下时间顺序：

1. 在外部 benchmark 之外的数据上开发 `AttackRL-v1`，冻结代码、策略 checkpoint 和攻击知识库。
2. 预注册外部 benchmark、victim、预算、oracle、split hash 和主指标；运行研究一公共轨。
3. 用 `AttackRL-v1` 生成 `D_att-v1`，保留成功、失败、功能破坏和无效候选。
4. 锁定 `D_att-v1` 的对象级 split，训练研究二；外部检测 benchmark 只用于最终测试或官方 train/dev/test。
5. 冻结研究二并产生 out-of-fold `p0`。研究三训练时不能使用同一任务上由过拟合模型产生的 `p0`。
6. 训练并冻结研究三，先运行固定外部攻击，再由未参与训练的 `AttackRL-v2` 做自适应压力测试。
7. 对抗重训结果单列，不覆盖自适应攻击前的原始测试结果。

研究三中的 `p0` 必须是 out-of-fold 或来自冻结外部模型；否则研究二对训练样本的过拟合会被传递给研究三，夸大三研究连接的收益。

## 6. 每项研究的最低通过门槛

### 6.1 研究一

只有满足以下条件才可以写 benchmark-specific SOTA：

- 在 RedCode-Exec 官方或等价设置中重跑 RedCodeAgent 及其五类基线。
- 使用相同 victim、三轮交互、生成上限、攻击信息和执行 judge。
- 在至少一个主要安全指标上显著领先，同时不被查询/token/执行成本支配；或形成严格更优的 ASR—成本 Pareto。
- 结果在至少两个 victim agents 或一个 victim 加一个不同语言设置上复现。

若 AttackRL 只在新建跨通道环境中领先，论文应把贡献写为“新的 workspace attack formulation 与经验上更强的策略”，不写领域 SOTA。

### 6.2 研究二

只有满足以下条件才可以写 benchmark-specific SOTA：

- 在 MalSkillBench 官方 pipeline 上与其可复现 12 工具同表比较；若研究范围不含 skills，则必须选择另一个真正匹配输入对象的公共 benchmark。
- 测试时只提供当前静态对象，不提供干净配对和运行结果。
- 按良性模板、仓库和攻击家族分组；至少报告 macro F1/AUPRC、FPR 与分攻击向量结果。
- 性能领先同时保持可接受的推理成本；商业 API 与本地工具分表。
- 在 `D_att-static` 之外至少一个独立数据源上保持优势。

若只在 `D_att-static` 胜出，应把结论限制为“AttackRL 生成数据上的机制有效性”。

### 6.3 研究三

只有满足以下条件才可以写 benchmark-specific SOTA：

- 在 AgentDojo 或 ClawGuard 的统一环境中重跑至少 Task Shield、MELON 和 ClawGuard；能复现时加入 AgentArmor。
- 所有方法在同一 tool-call 边界实际在线干预，而不是把部分方法离线重放、部分方法在线执行。
- 同时比较 targeted ASR、benign utility、utility under attack、延迟和调用成本。
- 以安全—效用 Pareto 判断胜负；单独更低 ASR 但明显破坏任务完成不算 SOTA。
- 在外部通用 benchmark 之外，于 coding-agent 轨迹上证明危害前检测与阻断，而不是整条轨迹事后分类。

## 7. 对三篇现有评价段的修改优先级

| 优先级 | 必须修改 | 原因 |
|---|---|---|
| P0 | 研究一加入 RedCodeAgent；把执行 oracle 设为主要成功判定；固定查询预算 | 否则攻击 SOTA 无法成立且 ASR 可能被自产 judge 放大 |
| P0 | 研究二加入 MalSkillBench 官方 detector suite；研究三加入 Task Shield/MELON/ClawGuard/AgentArmor | 当前基线明显过弱 |
| P0 | 外部 benchmark 与 `D_att` 分表，外部测试完全隔离 | 防止自产数据循环论证 |
| P0 | 研究三改用在线 security—utility 指标，记录危害前门控 | F1 不能代表防御有效性 |
| P1 | `D_att` 保留所有候选和失败回合；对象级分组 split | 避免选择偏差与模板泄漏 |
| P1 | 统一 victim、版本、prompt、工具、预算和成本报告 | 保证可比性 |
| P1 | 研究二取消年度成本节省的核心结论，改用可测预算和运行成本 | 缺少真实组织参数，且不影响 SOTA 比较 |
| P2 | 扩展到第二个 victim、语言或 benchmark | 支撑多 benchmark 稳健性而非单点胜出 |

## 8. 最终判断

当前路线**可以被改造成公允的 benchmark/SOTA 方案**，因为 RedCodeAgent、RedCode、MalSkillBench、RepoGuardBench、AgentDojo、ClawGuard 和 AgentSentinel 等主要资源均有公开代码或评估环境。但这不是 114 号方案自然保证的结果，必须额外实现统一 adapter、强基线重跑、外部测试隔离、确定性 oracle 和预算匹配。

最重要的策略是放弃“一张总表证明三篇都 SOTA”的想法。三项研究处理的输出不同：研究一是攻击生成，研究二是任务前静态检测，研究三是在线控制。它们应分别在匹配的公开 benchmark 上争取 benchmark-specific SOTA，再由 `D_att` 证明三项工件之间的连接与新情境价值。这样既公允，也比在自产数据上做一个看似整齐但无法审查的综合排名更有说服力。
