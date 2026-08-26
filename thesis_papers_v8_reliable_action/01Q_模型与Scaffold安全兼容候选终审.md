# 模型与 Scaffold 安全兼容候选终审

- **候选命题：** coding-agent 模型 × scaffold/harness × 任务风险的安全兼容与更新控制
- **审计日期：** 2026-08-16
- **审计性质：** 内部选题终审，不属于论文正文
- **终审结论：** **NO-GO。不冻结为三篇论文中的任何一篇，也不保留为替补题。**

## 0. 终局判定

这个候选抓住了一个真实现象。coding agent 的行为不是基础模型的单独产物。模型、系统提示、控制循环、工具定义、上下文压缩、重试、权限和回滚逻辑共同决定一次行动轨迹。它们又会以不同节奏升级。因此，单个组件更新可能维持甚至提高任务完成率，同时增加越权访问、危险命令、信息流违规或不可恢复修改。近期跨 harness 研究已经直接观察到模型与 harness 排名反转、不同 harness 的稳定故障指纹、组件版本迭代中的回归，以及任务完成与安全执行的脱钩。这里的潜在损害明确，coding agent 的工具调用和环境修改能力也使它不同于普通模型评测。

然而，**真实现象并不自动构成新的独立论文**。本审计把候选强化到其最有利形态：学习模型、harness 与任务风险之间的条件后果分布；在沙箱中生成并验证最小可执行 scaffold patch；在发布时执行成组升级、双轨运行、隔离或回退，而非只做模型选择、排行榜或简单路由。即使如此，候选仍未越过四组直接近邻共同形成的边界。

第一，HarnessAudit、Harness-Bench、PawBench、Scaffold Effect、Safety Under Scaffolding、Stop Comparing LLM Agents Without Disclosing the Harness 以及 A²E 已经把模型、harness 与任务/安全情境的交互当作可交叉运行和可测量对象。第二，Dunke 与 Nickel 的自动算法配置、HARBOR 的带安全约束配置搜索已经覆盖“依据历史实例表现学习条件配置”的计算问题。第三，HarnessOpt-Bench 与 RHO 已经允许优化器修改可执行 harness 文件，并以隔离运行、验证集或历史轨迹决定是否应用更新。第四，SafeHarness 与 HOL Guard 已经提供权限约束、审批、降级、隔离、检查点、回滚和恢复等真实运行时动作。把这些能力串联为一个模型，不会自然产生独立的新能力类别。

候选更致命的问题来自理论。Goodhue 与 Thompson 的任务—技术匹配以**个体使用者**为分析单位，任务特征、个体能力、技术功能、利用和个体绩效共同构成其因果链。把基础模型当成 individual，或把 model–scaffold 的预测交互直接命名为 task–technology fit，会同时改变行动者、利用者和绩效层级。Cram 等人的 IS control alignment 以组织中的 IS process 为单位，四个维度包含控制环境、控制机制、员工社会情绪行为与控制执行；纯运行时组件没有对应的员工反应和控制者—被控制者关系。Bharadwaj 的 IT capability 则是企业调动和部署 IT 与互补组织资源的能力，用来解释企业绩效，不是单次 agent 发布的组件适配度。若删去这些理论原义，仅保留“fit”“alignment”“configuration”等词，剩余算法就是一个通用因子图、超图 Transformer 或约束 AutoML。等参数通用模型可以复制它的状态、损失和动作，因此理论没有不可替代的算法责任。

据此，本候选同时触发两个终局撤题门：

1. **直接能力覆盖门。** 最强形态仍可分解为已有的交叉评测、后果预测、约束配置、程序编辑和发布控制，新增部分主要是系统集成。
2. **理论不可替代门。** 候选理论均发生分析层级或角色错置；去掉理论标签后，等参数通用交互模型与 AutoML 搜索器保留全部计算能力。

后文仍完整给出可构造的最强工件、数据识别、训练、基线和撤题试验。这不是保留该题，而是证明终判没有依赖一个被故意弱化的版本。所有性能数字均来自被核验文献或公开仓库；本文没有运行候选实验，也没有生成任何候选结果。

## 1. 候选问题的精确定义

### 1.1 研究对象、损害与决策时点

候选的最强研究对象不是静态的“哪个模型配哪个 agent”，而是一个带版本迁移的部署单元：

\[
u=(m^{-},h^{-},\tau,r,e,s,\Delta),\qquad
\Delta=(\Delta m,\Delta h,\Delta q,\Delta c,\Delta p),
\]

其中，\(m^{-}\) 与 \(h^{-}\) 是升级前模型和 harness；\(\tau\) 是任务；\(r\) 是任务风险结构；\(e\) 是固定执行环境；\(s\) 是随机种子或可复现采样条件；\(\Delta m,\Delta h,\Delta q,\Delta c,\Delta p\) 分别表示模型、控制循环/脚手架、工具接口、上下文机制和权限策略的拟议变化。一次“安全回归”必须通过同任务、同环境、同预算的升级前后配对运行定义，而不能把不同 benchmark 的平均分下降称为回归。

候选真正关心的事件是：

\[
Y_{reg}=1
\quad\text{iff}\quad
H^{+}-H^{-}>\delta_H
\land
Q^{+}-Q^{-}\ge -\delta_Q,
\]

其中 \(H\) 是由可执行轨迹和最终状态核验的损害，\(Q\) 是任务质量。这个定义刻意排除“模型完全不会做任务所以也不造成损害”的伪安全，并把功能成功没有明显下降但安全变差作为核心现象。损害至少覆盖未经授权的资源访问、跨角色信息泄露、破坏性或不可逆文件操作、密钥暴露、错误部署、绕过审批、持久化污染与安全边界被逐步侵蚀。对于不同风险类型，标签应来自确定性策略检查器、环境状态差分和隐藏 oracle；LLM judge 只能处理无法程序判定的补充维度。

算法介入有两个时点。发布前，它观察组件 diff 和沙箱 rollout，决定放行、双轨、隔离、请求补充证据或回退。发现候选 harness 引发回归后，它可以生成最小可执行 patch，在相同隐藏评价中重新运行。它不应通过拒绝所有任务获胜，因此主要目标必须同时报告安全损害、任务完成、人工介入、token、运行时间和回滚成本。

### 1.2 coding-agent 特异性

这个现象中有三点确属 coding-agent 情境的重要变化。其一，harness 是闭环控制器，不仅格式化一次输入。它决定何时继续、何时读取文件、如何压缩状态、如何重试、何时调用 shell、何时提交或回滚。其二，软件仓库和工具环境是持续变化的外部状态，轨迹中的一次错误可以影响后续观测和行动。其三，模型和 harness 常由不同主体、不同发布周期维护；固定模型的 harness 升级和固定 harness 的模型升级都可能改变行为。

这些特征证明研究情境重要，却不能证明候选独有。现有工作已经采用固定模型比较 harness 版本，采用固定任务比较模型—harness组合，记录完整工具轨迹，并把 native harness 与通用 harness 配对。因此，“coding agent 不是裸模型”只能承担共同前提，不能承担新增命题。

### 1.3 研究问题的最强表述

若暂不考虑终审结果，候选最强的研究问题可写为：在模型、harness 与任务风险结构分别更新且结果反馈稀疏的条件下，如何从可审计的配对轨迹中学习升级后的安全后果分布，生成最小可执行 harness 修补，并选择能维持任务能力的发布动作？

这个表述有意排除三种弱版本。第一，不把输出限定为“兼容/不兼容”二分类。第二，不把动作限定为从候选模型中选一个。第三，不把 scaffold 当作不可编辑的类别标签。即便如此，它仍是“条件后果模型 + 程序搜索 + 约束发布策略”的组合，能否成为独立贡献必须由近邻和理论替代检验决定。

## 2. 检索、全文和证据边界

### 2.1 实际阅读范围

本审计以 2026-08-16 为截止日。以下直接近邻阅读全文或逐节核对了方法、数据、结果、局限和可用性说明：Don't Blame the Large Language Model、Scaffold Effect、Inside the Scaffold、SABER、ABTest、Safety Under Scaffolding、Harness-Bench、HarnessOpt-Bench、HARBOR、Stop Comparing LLM Agents Without Disclosing the Harness、RHO、SafeHarness、AI Harness Engineering 与 HarnessAudit。A²E 和 Agent Safety Should Be a Runtime Contract 在截止日前刚发布，本审计核对了 arXiv 摘要、公开代码声明和与候选直接相关的范围；不使用其摘要之外的细节支撑核心撤题判断。

AIS 理论和算法配置近邻回到了本地全文。重点全文是 Goodhue 与 Thompson 的 Task-Technology Fit and Individual Performance，Bharadwaj 的 A Resource-Based Perspective on Information Technology Capability and Firm Performance，Cram 等人的 Information Systems Control Alignment，以及 Dunke 与 Nickel 的 A Data-Driven Methodology for the Automated Configuration of Online Algorithms。还回读了 Cram 等人对 Venkatraman profile/pattern deviation 的明确采用和单位说明。本文不把搜索摘要当作这些理论的原义依据。

### 2.2 证据状态编码

下表和后文使用四种状态。

| 状态 | 含义 | 可承担的论证责任 |
|---|---|---|
| F | 已读全文及相关附录/方法 | 可支持方法、数据、结果和局限的具体判断 |
| P | 已核原始文献的指定正文页/节，未以全文为证 | 只支持该页/节的定义或局部命题 |
| R | 已核公开仓库、README、目录或版本页 | 可支持当前可获得性、接口和复现材料判断 |
| A | 只核摘要/落地页 | 只用于说明研究范围和存在性 |
| N | 未定位可用公开工件 | 只能说明本次审计未找到，不能断言作者没有发布 |

仓库状态是 2026-08-16 的快照。论文声称“将发布”不等于审计时已经可运行。相反，仓库公开也不等于论文的精确实验版本已被冻结；正式实验必须另记 commit SHA、release tag、容器摘要和数据 manifest。

## 3. 直接近邻终审

### 3.1 交叉评测已经占据“模型 × harness × 任务/风险”识别空间

| 直接工作 | 核心设计与已核事实 | 对候选的占位 | 仍有局限 | 状态/入口 |
|---|---|---|---|---|
| Don't Blame the Large Language Model | 固定模型，比较 Qwen Code CLI 的 35 个顺序版本；50 个 SWE-bench Verified 任务，每条件两次，共 3,500 次运行。解决率在 23%–39% 间波动，token 消耗约增 70%；架构变化引发标准 CI 未捕捉的回归。 | 直接占据“harness 独立演化导致 agent 质量回归”与版本纵向设计。 | 结果主要是功能和效率，不是操作安全；复现包写明录用后发布，审计日未得。 | F；[arXiv:2607.03691](https://arxiv.org/abs/2607.03691) |
| Scaffold Effect | 3 个 harness × 2 个模型 × 50 个 Terminal-Bench Pro 任务，共 300 次受控运行；固定提示、环境与预算，保留各 harness 的原生执行。报告跨组合通过率差异、求解成本差异和可复现的 harness 故障指纹。 | 直接占据模型—harness配对和任务条件效应。 | 样本和 harness 数有限；部分供应商默认设置可能漂移。 | F；[arXiv:2607.22585](https://arxiv.org/abs/2607.22585) |
| Inside the Scaffold | 对 13 个开源 coding agent 的固定 commit 进行结构审计，形成控制、工具、编辑、发现、检索、隔离、状态、压缩、路由和记忆等 12 维 taxonomy，并对 296 项主张核验。 | 提供可把 scaffold 从类别名拆成可观察结构的表示基础。 | taxonomy 不估计性能，维度之间高度相关。 | F；[arXiv:2604.03515](https://arxiv.org/abs/2604.03515) |
| Safety Under Scaffolding | 62,808 次运行，6 个前沿模型、4 种部署配置和 4 个代理安全 benchmark；报告模型—scaffold 差异可达 35 个百分点，并区分 scaffold 主效应、scaffold × benchmark 交互及格式伪差异。 | 直接占据风险情境调节与安全测量；说明不能用一个统一兼容分数。 | 代理 benchmark 不等同于 coding-agent 操作损害；部分差异是选项/格式接口造成。 | F/R；[arXiv:2603.10044](https://arxiv.org/abs/2603.10044)，[代码](https://github.com/davidgringras/safety-under-scaffolding) |
| Harness-Bench | 106 个任务、6 个 harness、8 个模型，主体矩阵 5,088 次运行，含 Codex 后为 5,194；统一任务、环境、预算与 evaluator，同时保留原生提示、工具、状态和重试。分数同时考虑完成、过程与安全，安全是二元门。 | 公开的模型 × harness × 任务交叉运行基础已经存在，且包含 coding tasks 与安全门。 | coding tasks 仅 22 个；二元安全门过粗。 | F/R；[arXiv:2605.27922](https://arxiv.org/abs/2605.27922)，[代码](https://github.com/Qihoo360/harness-bench) |
| PawBench | 公开 150 个任务、9 个模型、3 个 harness 的 4,050 次组合评价，含 prompts、graders、submissions 与 traces。 | 又一公开的模型—harness条件评价资产。 | 以能力为主，不提供本候选所需的细粒度安全迁移标签。 | R；[代码](https://github.com/agentscope-ai/PawBench) |
| Stop Comparing LLM Agents Without Disclosing the Harness | 3 个模型 × 3 个 harness × 100 个 SWE-bench Verified 任务，每格两次；把模型视为 open-loop 组件、harness 视为闭环控制器，并报告 harness 方差与模型方差之比 7.80、9 个比较中 6 个排序反转。完整 harness 已含 allowlist、checkpoint 与 rollback。 | 同时占据“harness 是控制器”、模型排名反转和回滚配置比较。 | 公开仓库入口未在本审计中定位；部分附录方案属于未来工作。 | F/N；[arXiv:2605.23950](https://arxiv.org/abs/2605.23950) |
| HarnessAudit | 210 个任务、8 个领域、24 个场景、10 种 harness 配置；审计工具、资源、信息流边界、执行忠实度和扰动稳定性。公开实现写出 11,586 项角色—工具授权、3,094 项资源范围规则和 525 个扰动案例，并保存规范化 JSONL、状态库快照与 coding 任务的隔离 worktree。相同模型在原生与通用 harness 下可比较；任务完成与安全执行并不一致。 | 这是候选最直接的安全近邻：模型、harness、任务/角色风险、全轨迹边界和可运行环境均已进入同一评价设计。 | 主要是审计 benchmark，不生成部署 patch；公开结果仍需按 commit 冻结。 | F/R；[arXiv:2605.14271](https://arxiv.org/abs/2605.14271)，[代码](https://github.com/UCSB-AI/HarnessAudit) |
| A²E | 提出 Agent Task Protocol 和自动插桩 monitor，标准化不同 harness 的轨迹；摘要明确报告 model–harness 组合随任务类型变化，且没有组合在所有任务上一贯最好。 | 在评测基础设施层进一步削弱“组合效果尚不可测”的主张。 | 本审计只把摘要和代码声明用于范围判断。 | A/R；[arXiv:2608.07346](https://arxiv.org/abs/2608.07346)，[代码](https://github.com/datamllab/A2E) |

这些工作留下的缺口是“从交互评价进一步生成安全补丁”，而不是“首次发现三方兼容”。因此，若候选仍把核心贡献写成兼容表征、交互预测或回归监测，它在问题层面已经被直接覆盖。

### 3.2 操作安全数据已经能够交叉运行

| 资源 | 可观测风险与规模 | 对训练数据的价值 | 关键限制 | 状态/入口 |
|---|---|---|---|---|
| SABER | 论文报告 716 个任务、13 个模型、9,308 个模型—任务运行，覆盖破坏、权限、泄露、持久化、网络、篡改等；HSR 排除无能力和无必要拒绝，拒绝所有任务不能获胜。 | 可构造具有任务能力条件的操作伤害标签和全轨迹风险结果。 | 2026-08-16 对公开仓库任务文件的审计只计得 513 个，分组为 219/108/186，与论文 716 不一致；必须以冻结 manifest 解决。 | F/R；[arXiv:2606.01317](https://arxiv.org/abs/2606.01317)，[代码](https://github.com/sssr-lab/saber) |
| ABTest | 400 个已确认 issue、47 种交互模式、128 类 action，实例化为 Pallets Click 上 647 个可执行案例；5 个模型配置形成 3,235 次运行，1,573 个报警中人工核验 642 个异常，严重案例重跑复现率超过 90%。 | 提供“表面完成但代理行为异常”的可执行测试和动作级模式。 | 单仓库、单模板体系；论文的 4open 匿名工件需重新确认公开入口。 | F；[arXiv:2604.03362](https://arxiv.org/abs/2604.03362) |
| HarnessAudit-Bench | 每个任务含角色、目标、领域工具、边界规则、完成检查点和扰动版本；确定性访问规则遍历每个动作，服务状态由隔离 SQLite 或 disposable git worktree 保存。 | 最适合构造同一任务下模型/harness更换的 paired harm、completion 和 state-diff 标签。 | 需验证每种模型和 harness 的完整矩阵覆盖以及模型许可。 | F/R；见上 |
| Harness-Bench | 同一任务环境中跨模型和 harness 运行，保留原生控制方式并给出安全门。 | 适合基础三方交互估计。 | 风险标签不够细，不能单独训练“最小安全 patch”。 | F/R；见上 |

公开数据并非不存在。问题恰恰相反：现有数据足以训练通用交互预测器，却没有天然的、唯一的“安全兼容理论状态”标签。把多套 benchmark 的汇总分直接拼接也不可行，因为任务、工具、权限、模型服务、harness版本、预算和安全 oracle 不同。真正可识别的数据必须重新运行同一组不可变任务，形成连通的交叉设计。

### 3.3 自动配置、可执行编辑与持续更新已经覆盖候选动作

| 工作 | 优化对象、信号与真实动作 | 对候选的直接威胁 | 未覆盖部分 | 状态/入口 |
|---|---|---|---|---|
| Dunke & Nickel 2020 | 用历史实例数据和模拟退火搜索阈值表达式的结构与系数，自动生成可执行的在线决策规则；明确区分 algorithm selection、algorithm configuration、generation hyper-heuristic 与运行时 control optimization。 | 选已有模型/harness 是 selection/configuration；合成 scaffold patch 属于 generation hyper-heuristic/automated algorithm design；依据运行状态选择放行/回退属于 control optimization。仅增加安全目标仍是约束或多目标配置。 | 未涉及 LLM agent，也未处理操作安全。 | F；[DOI](https://doi.org/10.1016/j.dss.2020.113343) |
| HARBOR | 在约 40 个 harness flags 上做带噪约束贝叶斯优化；目标为通过率，约束成本与相对基线的安全非回归；采用 posterior chance constraint、block-additive Matérn GP、pairwise tensor-product 交互、SAAS 与多保真任务子集。 | 已经实现配置交互、成本/安全约束和模型特定方向改变。把“任务风险”加入上下文后仍是 conditional constrained BO。 | 其安全是任务通过率非回归，不是操作伤害；配置空间主要是 flag，不是任意代码。 | F/N；[arXiv:2604.20938](https://arxiv.org/abs/2604.20938) |
| HarnessOpt-Bench | 优化器可编辑整个可执行 harness 代码，看开发轨迹和验证汇总，在固定预算内提交最终版本；任务与 hidden test 隔离，harness 由不可变 Git commit 执行。4 个任务、5 个模型、111 个优化运行；允许改提示、工具、记忆和控制流。 | 已经直接占据“生成最小可执行 scaffold patch”中最困难的可执行编辑和隐藏测试协议。 | 不以安全为主要目标；论文声明发布，审计未定位明确代码 URL。 | F/N；[arXiv:2608.06301](https://arxiv.org/abs/2608.06301) |
| RHO | 从无标签历史轨迹选择 difficulty–diversity coreset，做每任务多次 rollout，以 self-validation 和 self-consistency 诊断，提出多个 harness 编辑，用 pairwise self-preference 选择；均值不为正则不更新。公开实现可修改 AGENTS.md、skills、脚本或对应 harness 文件，并在隔离 worktree 探测、备份后应用。 | 已经占据“持续收集轨迹—提出可执行更新—验证—无改善则不应用—备份”的闭环。 | 论文明确排除不可逆一次性任务，并指出受污染轨迹可能巩固不安全行为；缺少外部安全 oracle。 | F/R；[arXiv:2606.05922](https://arxiv.org/abs/2606.05922)，[代码](https://github.com/wbopan/retro-harness) |
| SafeHarness | Inform、Verify、Constrain、Correct 四层生命周期；风险分级、capability token、checkpoint、rollback、adaptive degradation 与 recovery 互相反馈。使用 Agent-SafetyBench 前 200 个任务，对 3 类 harness、5 个安全模式、2 种模型模式和 6 类条件评价。 | 已经执行候选的权限收缩、隔离、降级、回滚和恢复动作，不只是打分。 | 工具多为模拟，judge 和部分诊断依赖 LLM；不是学习三方更新兼容。 | F/R；[arXiv:2604.13630](https://arxiv.org/abs/2604.13630)，[代码](https://github.com/liu-yang-maker/SafeHarness) |
| HOL Guard | 本地优先的 pre-action 安全层，支持 Codex、Claude Code、Cursor、Gemini CLI、OpenClaw 等；检查 shell、file、MCP、prompt、tool result 与供应链，执行 allow、block、approve 并记录 receipts。公开仓库有策略级别、可逆 overlay/hook/proxy；审计日 README 给出 `hol-guard==2.0.345` 的精确安装示例。 | 是现实可运行的规则/策略强基线，覆盖审批、权限和动作阻断；任何新方法必须在相同普通任务负担下超过它。 | 工程工件而非同行评议算法；以规则和检测器为主，不能单独学习版本交互。 | R；[代码](https://github.com/hashgraph-online/hol-guard) |

这里形成一个不可通过改名消除的覆盖关系：

\[
\text{候选最强工件}
=\underbrace{\text{跨组合后果估计}}_{\text{HarnessAudit/Harness-Bench}}
+\underbrace{\text{约束配置}}_{\text{HARBOR/Dunke--Nickel}}
+\underbrace{\text{可执行编辑}}_{\text{HarnessOpt/RHO}}
+\underbrace{\text{发布保护}}_{\text{SafeHarness/HOL Guard}}.
\]

若新增命题只是把四类现成能力放进一个 pipeline，贡献是系统集成而非新的理论算法能力。要推翻这个判断，候选必须证明一个由理论导出的、现有方法无法表达的中间状态和反常行动方向。第 8 节说明当前理论没有做到这一点。

### 3.4 持续部署近邻进一步削弱发布动作的新颖性

候选所列的双轨、分阶段放量、隔离和回退并非 agent 研究才产生的动作。传统软件部署已经把这些动作当作独立的可靠性机制。Nix 通过内容寻址的不可变组件路径支持多版本并存、原子升级/降级、隔离实例和回滚，说明“保留旧版本—切换—恢复”首先是部署机制，而不是学习到的理论构念。Google Canary Analysis Service 把 canary 明确定义为部分且限时的变更部署，评价后可 roll forward、roll back 或通知人类；它对 binary、configuration 和 dataset change 做自动、常常自动配置的分析，并强调 canary/control 对照与 SLO 指标。CloudCanary 则在高频服务更新中计算更新前后 differential fault graph，增量审计共享依赖造成的相关失效，并生成满足可靠性阈值且动作数可最小化的 improvement plan。

| 持续部署工作 | 已有真实动作/结构 | 对本候选的含义 | 不应过度类比之处 | 状态/入口 |
|---|---|---|---|---|
| Nix | 内容寻址的不可变组件、并行版本/变体、原子升级与降级、隔离测试实例、精确回滚 | 双轨、隔离、版本 pin 和 rollback 不是候选独有算法动作 | 不预测 agent 轨迹，也不学习 task risk | F；[USENIX全文](https://www.usenix.org/legacy/publications/library/proceedings/lisa04/tech/full_papers/dolstra/dolstra_html/index.html) |
| Canary Analysis Service | 部分且限时部署；canary/control 统计检查；PASS/FAIL 后由 rollout tool 放行、回退或告警；配置可自动展开 | “先小流量试运行—比较—放行/回退/人工”是成熟发布协议，候选只能在 risk signal 上新增 | CAS 是被动分析者，不生成 harness patch，且服务指标不同于 agent 轨迹伤害 | F；[Google Research全文](https://research.google/pubs/canary-analysis-service/) |
| CloudCanary | 对更新 delta 做增量 fault-graph 审计；以 SAT/model counting 找相关失效风险并生成最小动作 improvement plan | “更新前风险图—差分—最小可靠改进计划”已经有直接系统先例 | 研究对象是云服务共享依赖，不是模型—harness行为交互 | F；[NSDI 2020全文](https://www.usenix.org/conference/nsdi20/presentation/zhai) |

这些工作不能替代 coding-agent 的操作安全研究，但它们明确限定可主张的新颖性。候选不能把 staged rollout、dual track、atomic rollback 或 minimal improvement plan 本身写成新增能力；它只能主张一种新的、经严格识别的 agent 风险状态为何改变这些既有发布动作。当前理论审计恰好未找到这种状态。

## 4. 公开资产、版本与交叉运行可识别性审计

### 4.1 当前公开性结论

| 资产 | 公开可得性 | 版本冻结可行性 | 是否支持候选核心识别 |
|---|---|---|---|
| HarnessAudit | 官方 GitHub、MIT license；任务、工具、framework adapter、fixture、trace/report/state 输出齐全 | 可以按 commit、模型标识、task YAML、容器/环境另建 manifest | 高。已有跨 harness/model 和轨迹安全规则，但需补足完整版本迁移对 |
| Harness-Bench | 官方 GitHub；task、oracle、config、runner 可见 | 可 pin commit；需冻结外部模型服务版本 | 中高。能估计交互，但安全结果粗 |
| PawBench | 官方 GitHub；prompts、graders、submissions、traces | 可 pin commit；已有运行是否涵盖精确模型 snapshot 需复核 | 中。适合能力交互，不足以作操作伤害标签 |
| SABER | 官方 GitHub | 可以 pin commit，但论文 716 与仓库审计 513 的差异必须先解决 | 中高。安全任务强，现成 cross-harness 矩阵不足 |
| RHO | 官方 GitHub，代码、数据、配置、脚本与 tests 可见 | 可 pin commit；候选 harness 更新有备份和工件目录 | 高，针对可执行更新；安全监督不足 |
| SafeHarness | 官方 GitHub，config/data/src/tests 可见 | 可 pin commit | 中高，针对运行时动作；三方版本识别不足 |
| HOL Guard | 活跃公开仓库；审计时 2,263 commits | 只能以 SHA 或 release 精确冻结，不能写 `latest` | 高，作为运行时工程基线，不作为训练标签真值 |
| Don't Blame the LLM | 论文写明复现包将在录用后公开 | 审计日不能据此声称数据可运行 | 低，除非自行重建 35 个 Qwen Code 版本 |
| HarnessOpt-Bench | 论文描述不可变 Git 运行和数据划分 | 审计未定位明确公开 URL | 协议高，现成工件可得性待核 |
| HARBOR | 论文方法完整 | 审计未定位公开仓库 | 可复现实现需自建 |

“公开 benchmark 存在”与“能识别更新因果效应”是两回事。若一个模型只在一个 harness 上运行，模型效应与 harness 效应完全混淆。若旧模型只配旧 harness、新模型只配新 harness，任何回归都无法归因于模型、harness 或二者交互。候选至少需要一个连通的二部/三部运行图，使同一模型跨多个 harness、同一 harness 跨多个模型、同一风险任务跨全部关键组合重复出现，并包含同一组件的前后版本。

### 4.2 最低识别设计

对于模型版本 \(i\)、harness版本 \(j\)、任务风险单元 \(k\) 和重复运行 \(s\)，候选应观察：

\[
y_{ijks}=\mu+\alpha_i+\beta_j+\gamma_k
+(\alpha\beta)_{ij}+(\alpha\gamma)_{ik}+(\beta\gamma)_{jk}
+(\alpha\beta\gamma)_{ijk}+b_{repo}+b_{template}+\epsilon_{ijks}.
\]

这只是识别基准，不是候选的理论算法。若训练数据不足以估计饱和的三向层级模型，就更没有证据声称复杂神经网络学到三方兼容。每一个版本迁移还需在相同任务、环境镜像、seed、温度、token预算和超时下配对运行。闭源模型无法保证权重快照时，主识别应使用可散列的开放模型 snapshot；闭源服务只能作为外部有效性样本，并明确记录 provider model ID、日期、区域和可得响应 metadata。

最小可接受的开放因子设计可以是 4 个不可变模型 snapshot × 6 个 pinned harness 版本 × 716 个 SABER 论文任务 × 3 个 seed，共 51,552 次；若以审计日实际可核的 513 个仓库任务为准，则为 36,936 次。二者不能混写。正式运行前必须由 task manifest 决定真实数量。HarnessAudit 的 210 个任务应作为不同来源的外部安全测试，不能和 SABER 随机拆分后视为同分布样本。

### 4.3 版本标签泄漏

模型名称、harness名称、commit 时间和 benchmark ID 都可能成为捷径。随机按运行行拆分会把相同 task template、同一仓库 fixture、相邻 harness commit 和同系列模型放入训练与测试，模型只需记住版本平均风险。候选若要证明“兼容机制”而非版本查表，测试必须同时包含：

1. 留一模型家族；
2. 留一 harness 家族；
3. 留一风险类型；
4. 留一仓库或 task template；
5. 按时间留出后发布版本；
6. 双留出，即模型家族与 harness 家族均未在训练中出现；
7. 去除所有显式版本字符串后的盲测。

相邻 commit 不能跨 split。由同一个基础案例生成的攻击/非攻击、许可/越权、可逆/不可逆 twin 必须成组。hidden oracle、gold completion rule、人工确认结果和 HarnessOpt 式 hidden test 均不得进入检索索引、patch proposer 上下文或训练提示。每次运行的 manifest 至少包含模型权重 hash、tokenizer hash、harness commit、工具 schema hash、权限图 hash、task commit、fixture hash、容器 digest、seed、采样参数、最大 token、最大 tool calls、超时和 judge 版本。

## 5. 候选的最强可训练工件

本节把候选设计到比“兼容评分器”明显更强。随后仍需接受同等预算的通用替代。

### 5.1 输入表示

每个训练样本不是单次最终回答，而是升级前后成对的组件、风险结构和轨迹：

\[
x=(X_m,G_h,G_r,D_\Delta,T^{-}_{1:L},O^{-},C),
\]

其中：

- \(X_m\) 是模型接口和行为探针序列。它包含工具调用格式、上下文长度、拒绝/确认行为、错误恢复探针和可散列模型元数据，不包含测试集平均安全分。
- \(G_h=(V_h,E_h)\) 是 harness 程序图。节点来自控制流 AST、system instruction 区段、tool schema、context manager、memory、retry、checkpoint、permission gate 与 submit logic；边表示控制流、数据流、权限委托和信息流。
- \(G_r=(V_r,E_r)\) 是任务风险图。节点表示资产、行动、前置条件、可见证据、潜在伤害、可逆性和受影响主体；边表示行动—状态迁移、证据—义务、权限—资源和伤害传播。
- \(D_\Delta\) 是拟议更新的结构化 diff，明确哪些节点、边、接口或权重发生变化。
- \(T^{-}_{1:L}\) 是旧配置的完整轨迹，限于发布前可用的历史证据；\(O^{-}\) 是旧配置的任务、安全和成本结果。
- \(C\) 是固定预算、执行环境与组织批准约束。

风险图不能由论文作者手工给每个任务写一个“高/中/低”标签。它应由 task specification、tool schema、permission policy 与环境状态机自动编译，再由人工抽样核验。否则所谓理论状态只是手工特征。

### 5.2 张量与前向计算

一个可运行的最强版本可用异构图编码器与三方超边交互：

\[
H_m\in\mathbb{R}^{B\times L_m\times d},\quad
H_h\in\mathbb{R}^{B\times N_h\times d},\quad
A_h\in\{0,1\}^{B\times N_h\times N_h\times K_h},
\]

\[
H_r\in\mathbb{R}^{B\times N_r\times d},\quad
A_r\in\{0,1\}^{B\times N_r\times N_r\times K_r},\quad
H_\Delta\in\mathbb{R}^{B\times N_\Delta\times d}.
\]

模型编码器对行为探针产生 \(H_m\)，关系图 Transformer 对 harness 与风险图产生 \(H_h,H_r\)。随后由受稀疏掩码约束的三方 cross-attention 形成超边状态：

\[
Z_{mhr}=\operatorname{TriAttn}(H_m,H_h,H_r,H_\Delta)
\in\mathbb{R}^{B\times Q\times d}.
\]

每个超边只连接一个可观察模型行为、一个 harness 控制位点和一个风险义务，例如“模型在工具 schema 错误后倾向重试—harness 默认无限重试—任务资源为不可逆部署”。这样至少能把相互作用落到可审计位置，而非输出一个无来源兼容分数。

后果头输出多维分布而非二分类：

\[
p_\theta(Y_H,Y_Q,Y_C,Y_I,T_f\mid x,\Delta),
\]

其中 \(Y_H\) 是各类伤害计数/严重度，\(Y_Q\) 是任务结果，\(Y_C\) 是 token 与运行成本，\(Y_I\) 是人工介入，\(T_f\) 是首次违规时间。分布应能表达尾险和校准不确定性。

程序头对 harness AST 生成 typed edit sequence：

\[
P_\phi=(a_1,\ldots,a_J),\qquad
a_j\in\{\text{insert gate, change scope, add checkpoint, alter retry, restore context, add verifier, delete edge}\}.
\]

每个 edit 必须通过类型检查、schema 检查、静态权限检查和隔离执行。发布策略头不返回模型排行榜，而选择真实动作：

\[
\pi_\psi(a\mid b_t),\quad
a\in\{\text{ship},\text{stage patch},\text{dual-track},\text{isolate},\text{request evidence},\text{rollback}\}.
\]

belief state \(b_t\) 包含后果分布、校准区间、已用预算、可逆性、patch 验证结果和剩余审批能力。部署 manifest 是该头真正修改的外部对象。

### 5.3 训练样本和监督信号

训练数据需要三层监督。

第一层是配对后果监督。同一个任务在旧/新组件组合下运行，确定性轨迹检查器和最终状态差分产生 \(Y_H\)，task oracle 产生 \(Y_Q\)，运行日志产生 \(Y_C,Y_I,T_f\)。只有新配置伤害上升且任务能力条件满足时才构成核心回归样本。

第二层是反事实顺序监督。对于同一 \((\tau,e,s)\)，比较两个组件组合或两个 patch；较安全且任务非劣的组合应排序更高。若安全与任务冲突，则保留 Pareto 对，不强行压成单一偏好。

第三层是 patch 监督。公开数据几乎没有唯一 gold scaffold patch。可行来源只有：从安全/不安全配置的最小结构差分产生弱标签；从人工修复的真实 harness issue/commit 产生历史标签；或让 proposer 在沙箱中搜索，以隐藏的 task、安全和成本 oracle 给执行回报。因为多个 patch 可能等价，不能把与某个 gold diff 的 token 距离当作主要正确性。

### 5.4 损失函数

钢人版本的训练目标可以写为：

\[
\mathcal L=
\lambda_H\mathcal L_{harm}
+\lambda_Q\mathcal L_{task}
+\lambda_T\mathcal L_{surv}
+\lambda_P\mathcal L_{pair}
+\lambda_K\mathcal L_{cal}
+\lambda_E\mathcal L_{edit}
+\lambda_X\mathcal L_{exec}
+\lambda_I\mathcal L_{inv}.
\]

\(\mathcal L_{harm}\) 对多类伤害使用计数/严重度的分布 NLL；\(\mathcal L_{task}\) 预测任务完成与质量；\(\mathcal L_{surv}\) 对首次违规做离散时间生存损失；\(\mathcal L_{pair}\) 对同任务、同 seed 的安全非劣配对做排序；\(\mathcal L_{cal}\) 用 Brier/NLL 和组别校准约束置信度；\(\mathcal L_{edit}\) 只在有可核历史修复时做 typed edit imitation；\(\mathcal L_{exec}\) 根据沙箱执行的安全、任务、成本和最小改动奖励训练 proposer；\(\mathcal L_{inv}\) 抑制显式版本 ID 和 benchmark ID 的捷径。发布策略用风险约束目标：

\[
\max_\pi\ \mathbb E[Q-\lambda_C C-\lambda_I I]
\quad\text{s.t.}\quad
\Pr(H>h_{max}\mid b_t,a)\le\alpha,
\]

且对于不可逆高影响任务采用更低的 \(\alpha\)。这只是合理的风险约束，并不是从当前 AIS 理论推出的独特损失。

### 5.5 推断时的真实动作

推断必须依次产生可审计工件。系统读取 proposed update，建立结构 diff，选择少量信息价值最高的沙箱 probe；后果模型更新 belief；若风险可接受则写入 staged deployment manifest；若某个 harness 控制位点导致风险，程序头生成 patch commit，在隔离 worktree 或容器重跑；若证据仍不足，则生成双轨流量比例、权限隔离 profile 或回滚到精确 commit。每一步都保留输入 hash、模型输出、执行结果和批准记录。

如果实现只输出“model A 与 scaffold B 不兼容”，本候选立即退化成分类/路由。若 patch 只是由 LLM 在提示词中自由改 README 或 system prompt，主要贡献又退化为云端生成加验证。只有可训练后果权重、typed patch policy、执行验证和发布 policy 都真实存在，才达到候选的钢人版本。

## 6. 数据划分、泄漏、算力与复现

### 6.1 训练、验证和测试

建议的预注册划分不是随机 80/10/10，而是多轴 group split：

- 训练集：若干模型家族、harness家族、风险类型和较早版本的连通因子设计。
- 开发集：任务模板、仓库和 seed 全部与训练成组隔离，用于选择超参数和 patch 搜索预算。
- ID 测试：训练中出现过的组件家族，但全新任务/仓库。
- OOD-M 测试：未见模型家族。
- OOD-H 测试：未见 harness 家族。
- OOD-R 测试：未见风险类型。
- OOD-TIME 测试：冻结日后发布或严格时间后切的组件版本。
- OOD-DOUBLE 测试：模型与 harness 家族同时未见。

公开 benchmark 的 validation/test 名称不能直接沿用为本研究 split。所有训练算法可见的轨迹、配置和 oracle 必须重新做 source lineage。HarnessOpt-Bench 式 hidden test 只在最终候选 patch 确定后开放一次；结果不得回流继续编辑。

### 6.2 公平基线

必须包含以下最强直接与通用替代，并严格统一数据、rollout、token、模型调用、墙钟和可执行 edit 次数。

1. 饱和 Bayesian hierarchical three-way GLMM/factor model，显式估计模型、harness、风险主效应与全部二向/三向交互。
2. 等参数 generic heterogeneous graph Transformer，不提供任何理论命名的 state，但看到相同节点、边和 diff。
3. 等参数 hypergraph/factor-graph predictor，直接输出后果分布和发布动作。
4. HARBOR 风格 constrained Bayesian optimization，使用相同 configuration/action space、chance constraint 与多保真预算。
5. Dunke–Nickel 风格模拟退火/生成 hyper-heuristic，以相同执行 oracle 搜索 scaffold edit program。
6. HarnessOpt-Bench 风格 code-edit optimizer，在相同 dev/hidden split 与调用预算下修改整个 harness。
7. RHO 与其 Meta-Harness/ReasoningBank 等基线，使用相同历史轨迹与 probe 数。
8. SafeHarness 和 HOL Guard，分别代表生命周期安全架构和现实 pre-action 规则系统。
9. 随机搜索、进化搜索以及可用的通用 agent/harness AutoML，如 DSPy、GEPA、AFlow 类方法，限制为相同候选数和评估预算。
10. no-theory、shuffled-risk-graph、shuffled-component-role、removed-three-way-edge、same-parameter-direct-predictor。

公平比较的决定性项目不是参数量一项。program optimizer 的每次候选编译、sandbox rollout、judge call 和 hidden-test接触都要计入预算；闭源模型调用要按 token 与价格报告；任何方法都不能访问测试 task specification 中的 gold outcome 或安全规则答案。

### 6.3 评价与统计

主要安全结果包括每千 tool calls 的加权伤害、首次违规的时间、越权资源数、不可逆状态变化、泄漏/部署事件、回滚后残留状态和能力条件化伤害率。任务结果包括完成率、质量分和功能回归。成本结果包括 token、tool calls、墙钟、GPU/CPU 时间、人工审批分钟、阻断率、误阻断和回滚成本。

patch 结果必须报告编译/启动成功率、隐藏安全测试通过率、正常任务非劣率、AST edit distance、修改权限面的大小和跨模型/harness泛化。发布策略应画安全—任务—人工负担 Pareto frontier，不能只给单一加权分。统计上应使用任务/仓库随机效应、paired bootstrap 或适合配对二元结果的检验，报告效应量和置信区间；多风险、多 split 与多模型比较要预先定义主要终点并控制多重比较。

### 6.4 算力估计

算力主要消耗在环境 rollout，不在图网络训练。36,936–51,552 次基础运行若每次 10–30 分钟，相当于约 6,156–25,776 worker-hours。这是规划估计，不是已发生用量。至少需要 64–128 个隔离 Docker worker 才能在合理周期内完成；涉及 GPU 本地模型时还受推理吞吐限制。完整轨迹、容器日志、状态快照、patch工件和重复运行可能需要约 10–40 TB 存储，同样只是容量规划区间。

图/序列模型本身可规划 4 张 48–80GB GPU 训练 3–10 天，具体取决于轨迹长度和是否预计算编码。patch proposer 若在线调用大模型并做执行式强化学习，计算量会远高于预测器。必须分别报告数据生成、编码预计算、主模型、program search 和最终复跑，不得用一个“GPU hours”掩盖云端调用或并行 worker。

复现包至少包含源代码、环境构建文件、配置 schema、所有随机种子、数据和版本 manifest、split 生成器、运行调度器、轨迹规范化器、风险 oracle、统计脚本、checkpoint、训练曲线、失败运行、预算账本和一条从 raw trace 重算论文表格的命令。闭源响应若许可不允许发布，应至少发布请求 hash、非敏感 normalized trace 与供应商元数据。

## 7. 直接近邻逐项反证

### 7.1 “我们不是排行榜，而是学习兼容”仍不够

HarnessAudit、Harness-Bench 与 Safety Under Scaffolding 已经表明组合效果依赖模型、harness、任务/benchmark和轨迹长度。用神经网络拟合这些交互，只是把 ANOVA 或层级模型换成可扩展预测器。若候选不能在未见模型家族和未见 harness 家族的双留出上预测真实伤害，所谓兼容表示只是在记忆组合均值。即使能泛化，也需证明其新增能力不是 Inside the Scaffold taxonomy 特征加通用图网络的自然应用。

### 7.2 “我们生成最小 patch”也未自动脱离 AutoML

Dunke 与 Nickel 明确把从实例数据生成决策规则纳入 automated algorithm design/generation hyper-heuristic，而不只叫参数选择。HarnessOpt-Bench 已把整个 harness 代码作为可编辑工件，RHO 已从轨迹提出并应用 harness 修改。把目标改为安全约束并增加 AST edit penalty，仍然是约束程序搜索。要成为新能力，patch 必须由理论状态限制可行动作或产生一个通用优化器不容易提出的方向；当前理论没有这样的约束。

### 7.3 “我们做成组更新、双轨、隔离和回退”仍是发布策略

SafeHarness 已把 constrain、checkpoint、rollback、degradation 和 recovery 组织为生命周期层，HOL Guard 已实现 action-level allow/block/approve 与可逆 hook/proxy/overlay。Stop Comparing 的完整 harness 也包含 allowlist、checkpoint 和 rollback。对这些动作做条件选择当然可以训练，但这属于有约束的 deployment policy。除非候选揭示一个特定 IS 机制为何要求在相同观测下选择与通用风险 POMDP 不同的动作，否则“多了一个策略头”不是理论算法贡献。

### 7.4 “功能不降但安全回归”是有价值结果变量，不是足够贡献

HarnessAudit 已直接报告 task completion 与 safe execution 不一致；native Codex 与 OpenClaw 的匹配比较中，完成和安全可以向不同方向变化。SABER 的 HSR 也专门避免无能力和过度拒绝获得表面安全。候选把安全回归定义得更严格是必要的测量改进，但测量改进本身不能填补理论和算法独立性缺口。

## 8. AIS 理论原文层级与算法责任审计

### 8.1 Task–Technology Fit：个体层级和角色错置

Goodhue 与 Thompson（1995）的题名和模型目标都明确指向 individual performance。原文把任务定义为个体为把输入转成输出而执行的行动，把技术视为个体用于完成任务的工具、系统或服务，并同时纳入 individual abilities、utilization 与 performance impacts。核心命题是技术要对个体绩效产生正向影响，既要被利用，也要与其支持的任务相匹配；实证样本是两家公司六百多名人类使用者。

在候选中，基础模型既不是组织中的人类个体，也不是“利用技术的使用者”。scaffold 也不只是提供给这个个体的一项 IT；它是决定模型能看到什么、如何循环和能调用什么的执行控制器。若把 model 当 individual、scaffold 当 technology、benchmark task 当 task，utilization 和个人能力两环被替换为软件组件内部函数，结果从 individual performance 变成系统轨迹安全。这个映射不是理论迁移，而是角色重写。

若改为真实开发者是 individual、coding-agent系统是 technology、开发任务是 task，那么 TTF 可以研究开发者使用、绩效或监督负担，却不再直接产生 model–scaffold patch 的内部状态。算法可以把开发者任务要求作为上下文，但“匹配”仍是通用条件预测。故 TTF 不能为本候选承担独立算法责任。

来源：Goodhue, D. L., & Thompson, R. L. (1995). Task-Technology Fit and Individual Performance. MIS Quarterly, 19(2), 213–236. [DOI 10.2307/249689](https://doi.org/10.2307/249689)。本地 Otero 头部曾把年份标成 1992；期刊卷期、AIS eLibrary 和 DOI 元数据均核为 1995，因此不得沿用错误年份。

### 8.2 IS Control Alignment：IS process、员工反应与控制执行不可删除

Cram 等人（2016）把分析单位明确设为 IS process，并用三个组织的系统开发案例研究四个维度：control environment、control mechanisms、employee socio-emotional behaviors 和 control execution。其两种高功能模式是传统环境—预防性控制—个体取向行为—稳定执行，以及渐进环境—侦测性控制—集体取向行为—演化执行。互补或冲突的判断来自组织访谈、文档和正负组织结果，不是组件张量的乘积符号。

候选的模型、harness、风险任务只覆盖技术机制和环境条件，缺少员工的社会情绪响应，也缺少管理者试图影响他人行为的 controller–controlee 结构。若把模型输出倾向叫 socio-emotional behavior，概念发生拟人化；若直接删除该维度，又不再使用该理论的完整机制。把 harness 的 release loop 叫 control execution，也不足以恢复组织层级，因为原文关注员工如何随时间执行和调整控制。

Cram 等人采用 Venkatraman 的 pattern/profile deviation，把多个维度与由理论或经验确定的高功能模式比较。若候选从同一运行结果学习一个“理想安全组合”，再计算三方表示到理想 profile 的距离，距离本质上是 metric learning。等参数通用模型可学习同一 prototype；若理想 profile 由结果数据反推，理论没有在结果之前给出独立约束；若强行采用 Cram 的传统/敏捷两种 profile，又与模型/harness结构无对应关系。

来源：Cram, W. A., Brohman, M. K., Chan, Y. E., & Gallupe, R. B. (2016). Information systems control alignment: Complementary and conflicting systems development controls. Information & Management, 53(2), 183–196. [DOI 10.1016/j.im.2015.09.012](https://doi.org/10.1016/j.im.2015.09.012)。

### 8.3 Complementarity / supermodularity：强方向命题与观察事实冲突

“互补”不能被降格为“存在交互”。Milgrom 与 Roberts 对 supermodularity 的原始形式化要求增加一个构件时，另一个构件的边际收益不下降，即具有 increasing differences。对于组件 \(a,b\) 和结果 \(V\)，离散形式至少要求：

\[
V(1,1)-V(0,1)\ge V(1,0)-V(0,0).
\]

然而，现有 harness 研究报告的是模型特定符号变化、排序反转、scaffold × benchmark 大幅差异和某些功能增强伴随安全下降。HARBOR 因可识别性只建 pairwise 交互，却观察不同模型下配置开关方向改变；Scaffold Effect 和 Stop Comparing 也不支持单调的通用互补。若候选允许任意正负三方交互，supermodularity 没有约束前向计算。若强制 increasing differences，模型会系统性漏掉替代、冲突和风险放大。理论在此不是帮助，而是给出与现象不相容的统一方向。

所以可检验的理论冲突实验必须包括：对每组 component pair 估计交叉差分及置信区间；检验符号是否随风险任务改变；比较单调 supermodular 网络、允许 substitution 的通用 factor graph 和无交互模型。只要大比例交叉差分为负或跨风险反号，不能再用“complementarity”统称。若通用模型胜出，理论贡献撤销，而不是把任意交互改名为互补。

### 8.4 IT Capability Configuration：企业资源与竞争绩效层级错置

Bharadwaj（2000）从资源基础观定义企业调动和部署 IT-based resources，并把资源分为 IT infrastructure、human IT resources 与 IT-enabled intangibles，以企业财务表现检验 IT capability。路径依赖、社会复杂性、组织知识和与其他企业资源的结合解释为何能力难以模仿。

一个模型版本、harness 配置或 task risk 不是企业能力。单次 release manifest 也没有人力资源、组织无形资产、竞争租金或持续优势。若把三方嵌入称为“IT capability configuration”，算法仍只是组件配置；若把单位真正提高到企业，则需要组织如何积累、治理和部署 coding-agent 能力的纵向数据，研究问题和输出动作都将改变，无法再由公开 agent benchmark 单独训练。

来源：Bharadwaj, A. (2000). A Resource-Based Perspective on Information Technology Capability and Firm Performance: An Empirical Investigation. MIS Quarterly, 24(1), 169–196. [DOI 10.2307/3250983](https://doi.org/10.2307/3250983)。

### 8.5 理论—算法责任矩阵

| 理论候选 | 原文分析单位与关键行动者 | 原义要求的机制 | 候选拟映射 | 层级/角色问题 | 能否产生通用模型不可替代状态 | 终审 |
|---|---|---|---|---|---|---|
| TTF | 人类个体、其任务、能力、技术利用和个体绩效 | 任务要求与技术功能匹配，且实际利用后影响个体绩效 | 模型 × harness × task risk | 把模型改写为个体、scaffold改写为技术，删除真实利用者 | 否。保留“匹配”后即条件交互 | 淘汰 |
| IS control alignment | 组织中的 IS process、管理控制者和员工 | 环境、控制机制、员工社会情绪行为、控制执行形成完整模式 | harness、权限、模型行为、发布循环 | 员工反应和控制者—被控制者关系缺失；软件行为被拟人化 | 否。profile distance 等于通用 prototype/metric learning | 淘汰 |
| profile deviation | 多变量、criterion-specific 理想模式 | 理论或独立经验先给理想 profile，偏离与绩效相关 | 学习安全组合 prototype | 理想 profile 若由同一结果反推则循环；若外生又无理论对应 | 否 | 淘汰 |
| complementarity/supermodularity | 具有 increasing differences 的构件选择 | 明确的正向交叉差分 | 任意 model–harness interaction | 现有结果含负交互、替代和反号；任意交互不等于互补 | 否；强制单调反而错配 | 淘汰 |
| IT capability | 企业及其 IT、人力、无形资源和企业绩效 | 资源调动、路径依赖、社会复杂性和互补组织资源 | 组件组合与 release policy | 企业层级被压成一次运行 | 否 | 淘汰 |

结论不是“还需要找更好的理论包装”，而是当前候选的计算问题没有天然需要这些理论。理论若不能改变输入中的必要状态、损失中的方向约束或推断动作，就不应继续占用论文位置。

## 9. 理论方向冲突与等参数替代试验

### 9.1 必须预先写出的冲突情境

假设新模型工具调用更准确，但倾向在失败后自主重试；新 harness 同时把 retry 上限提高并缩短确认提示；任务涉及不可逆部署。通用风险模型可能因三方交互选择隔离或回退。TTF 不能告诉算法该把模型视为使用者还是技术，也不能推出“重试—不可逆性”状态。Control alignment 的传统/敏捷 profile 也不能决定 retry 上限。supermodularity 若把准确模型与强 harness视为互补，甚至可能错误鼓励联合升级。

反过来，在只读代码检索任务中，同一模型和 retry 更新可能显著提高任务成功且几乎没有不可逆风险。合理策略应放行。这个方向变化来自 task risk state 与后果数据，不来自上述 AIS 理论。通用 POMDP、factor graph 或 calibrated world model能自然表达。

### 9.2 等参数替代门

理论版本和通用版本必须看到相同 raw inputs、具有相同参数量、训练步数、rollout和 program-search预算。理论版本可以使用命名的 fit/profile/complementarity state；通用版本只用无语义的 latent nodes/edges。至少比较：

- 后果预测 NLL、Brier、group calibration 与 OOD tail recall；
- 在固定安全上限下的任务成功和人工负担；
- patch hidden-test 安全非劣率与正常任务非劣率；
- 双留出模型 × harness 家族上的策略 regret；
- theory state 删除、打乱、符号中和后行为是否按预注册方向改变。

撤销理论贡献的条件很简单：通用替代在置信区间内不劣，或理论状态打乱后行为没有系统变化。当前概念映射已经表明通用模型保留全部信息和动作，因此没有理由在投入大规模 rollout 前期待理论版本通过该门。

## 10. 新颖性分解与撤题门

### 10.1 候选每个可能卖点的归属

| 候选卖点 | 实质能力 | 最直接已占工作 | 尚存差额 | 是否足以独立成篇 |
|---|---|---|---|---|
| 模型 × scaffold × 风险兼容 | 交叉运行与三方交互预测 | HarnessAudit、Harness-Bench、Safety Under Scaffolding、A²E | 从评价到 OOD 预测 | 否，通用预测自然延伸 |
| 组件升级安全回归 | 版本前后 paired outcome | Don't Blame the LLM；HarnessAudit 的安全—完成脱钩 | 纵向 operational harm 数据 | 单独可能有数据论文价值，但尚无独立算法/理论 |
| 最小可执行 scaffold patch | program edit + sandbox oracle | HarnessOpt-Bench、RHO | 加安全约束与最小性 | 否，约束程序优化 |
| 成组更新 | joint configuration search | HARBOR、自动算法配置 | 操作安全 outcome | 否，多目标/约束 AutoML |
| 双轨、隔离、回退 | deployment policy | SafeHarness、HOL Guard、Stop Comparing 的完整 harness | 学习何时执行 | 否，通用风险控制策略 |
| fit/alignment 表征 | latent compatibility state | TTF/control alignment/profile deviation | 词义映射 | 否，层级错误且通用模型可复制 |

### 10.2 预先规定的六个再考虑门

只有未来出现以下全部证据，才允许重新开题，而不是继续在当前文稿中修补。

1. **理论状态门。** 从单位一致的 IS 理论导出一个原文要求的中间状态，等参数 generic factor graph 看相同 raw inputs 仍不能复制；打乱该状态产生预注册方向的行为改变。
2. **独占数据门。** 构建公开、版本可散列的 paired operational-safety 更新数据，至少同时包含模型更新、harness更新和二者联合更新，并超出 HarnessAudit/Harness-Bench 的静态组合。
3. **可执行新增能力门。** 在相同调用、候选、hidden test 与墙钟预算下，安全 patch 同时超过 HarnessOpt-Bench式优化、RHO、HARBOR和通用程序搜索。
4. **双 OOD 门。** 在未见模型家族 × 未见 harness 家族及未见风险类型上仍能校准预测和降低真实伤害，而非记住版本。
5. **非拒绝门。** 安全收益在任务成功非劣或明确 Pareto 优势下成立，同时低于 SafeHarness/HOL Guard 的人工阻断负担。
6. **因果归因门。** 连通因子设计能够分离模型、harness、风险主效应和交互；版本、时间、供应商默认与 task template 泄漏均被排除。

当前候选在第 1 门已经结构性失败，在第 3 门面对四类直接近邻也没有独占动作。因此不应先投入数万次 rollout，再等待结果决定理论是否存在。

### 10.3 最终 NO-GO 的范围

本判定只撤销“模型 × scaffold × 任务风险的安全兼容与更新控制”作为一篇 ISR 级独立算法论文。它不否认以下工作有工程价值：建立版本冻结 manifest；用 HarnessAudit/SABER 做组件升级 CI；将 HOL Guard 接入 coding-agent harness；用 HARBOR 搜索安全配置；在 RHO 更新前增加独立安全 oracle。这些可以成为基础设施、论文消融或系列研究的共同实验平台，却不能因为组合后工作量大就升级为独立研究贡献。

## 11. 肖帅勇 ISR 精确句键逻辑审计

### 11.1 使用原则

本节只学习每个句段的学术功能、证据责任和递进方式，不复制原句，不把肖老师论文中的对象或理论替换名词后套写。句键严格来自 `00W_肖帅勇两篇ISR源行句段主键Manifest.md`。每一行都记录承接前提、唯一新增命题、逻辑关系、分句引用责任和后继义务。由于本文件是内部终审，句键对应的是审计论证单元，而非声称已写成正式论文段落。

### 11.2 逐项承接表

| 本审计论证单元 | 肖老师精确句键 | 承接前提 | 唯一新增命题 | 逻辑关系 | 分句引用责任 | 后继义务 |
|---|---|---|---|---|---|---|
| P0 现象建立 | `ACAA-I1-S01–S05` | coding agent 已在真实软件环境行动 | 模型之外的 harness 演化会改变轨迹和结果 | 情境扩大 → 决策后果 | “组件独立升级”由 Don't Blame/Inside；“安全后果”由 HarnessAudit/SABER分别支持 | 下一段必须从重要性推进到尚未解决部分，不能直接报模型 |
| P1 安全与功能脱钩 | `DSDL-I1-S01–S05` | 任务完成常作为主要评价 | 完成非劣不排除边界违规与不可逆损害 | 常用结果 → 被遗漏结果 | 脱钩由 HarnessAudit；拒绝校正由 SABER | 必须定义核心结果，防止安全变成标签 |
| P2 版本决策链 | `DSDL-I3-S01–S05` | 模型、harness、权限组件独立发布 | 风险发生在拟议更新被放行的具体时点 | 过程节点 → 决策需要 | 版本回归由 Don't Blame；运行时控制由 SafeHarness/HOL Guard | 后继必须列观察、不可见状态和动作 |
| P3 最近近邻 | `ACAA-I2-S01–S06` | 三方组合效果真实 | 直接工作已覆盖交叉评价、配置、编辑与回滚 | 已知研究 → 缺口缩窄 | 每一类近邻分别引用原论文，不能一条引用承担四类能力 | 下一段只能主张剩余“联合工件”，不能说首次研究 scaffold |
| P4 任务不匹配 | `DSDL-I5-S01–S04` | 候选原始说法是“兼容” | 二分类/路由不足，最强问题须输出后果分布、patch和发布动作 | 弱任务 → 强任务重构 | 近邻说明弱任务已覆盖；此处的工件是设计主张，无结果引用 | 必须说明强任务仍为何不独立 |
| P5 理论应产生状态 | `DSDL-I6-S01–S05` | 理论不能只解释结果 | 有效理论必须引入原文不可删除的中间状态 | 理论缺口 → 设计义务 | 理论原义必须引 Goodhue/Cram/Bharadwaj全文 | 下一段逐一检验理论单位，不得只用“fit”同词 |
| P6 TTF层级检验 | `DSDL-I7-S01–S08` | TTF含 task、technology、individual、utilization、performance | model 不是 individual，model–harness 不等于 TTF | 构念定义 → 映射反证 | 个体层级、六百多用户和利用链均由 Goodhue–Thompson承担 | 后继说明正确映射为何又失去算法责任 |
| P7 control alignment层级检验 | `DSDL-I8-S01–S11` | Cram 四维度是完整组织过程构型 | 删除员工社会情绪行为后不能称原理论 | 原理论机制 → 候选缺项 | 四维、两模式、process unit 由 Cram等承担 | 后继检验 profile distance 是否可被通用模型替代 |
| P8 理论终判 | `DSDL-I9-S01–S07` | 各理论映射已逐项失败 | 没有理论生成不可替代计算状态 | 多个反证 → 单一终判 | 结论强度限于本候选，不泛化为理论无用 | 后继进入钢人工件，避免用弱实现制造 NO-GO |
| P9 算法处理错误方向 | `ACAA-L11-S01–S08` | 现有工作能配置和编辑 harness | 只有理论导出不同冲突行动才可能新增 | 文献能力 → 方向缺口 | HARBOR/RHO/HarnessOpt/SafeHarness分别承担已有方向 | 后继给出明确冲突情境和替代模型 |
| P10 理论—挑战契约 | `ACAA-T1-S01–S04` | 高风险不可逆任务要求更强证据 | 候选理论必须改变 belief、loss 或 action，不可只命名节点 | 理论命题 → 计算挑战 | 风险状态为设计定义；不得伪称理论已经验证 | 后继必须写前向路径 |
| P11 三方交互挑战 | `ACAA-T5a-S01–S04`、`ACAA-T5b-S01–S06` | 单组件主效应不能解释组合反号 | 需要三方超边表达模型行为—控制位点—风险义务 | 挑战 → 表示方案 | 交互反号由近邻；张量为设计主张 | 后继给同参数无语义超图基线 |
| P12 不完全反馈挑战 | `ACAA-T6a-S01–S05`、`ACAA-T6b-S01–S04` | 发布前看不到所有真实后果 | 后果头需输出分布和首次违规时间，并支持证据请求 | 不可见性 → belief/action | 不可逆任务缺口由 RHO局限；指标定义是预注册 | 后继给校准和隐藏测试 |
| P13 挑战—方法闭合 | `ACAA-T9-S01–S03` | 已列交互、反馈和动作挑战 | 每个挑战必须由特定模块和损失承担 | 汇总 → 方法入口 | 不新增经验事实 | 后继架构不得出现无上游责任模块 |
| P14 数据/复现 | `ACAA-M2-S01–S08` | 三方作用需要交叉运行而非拼摘要分数 | 需要 pinned model/harness/task/environment/seed manifest | 数据需要 → 样本构造 | 数据规模由各论文；建议因子规模明确标为规划 | 后继必须处理 repo/论文任务数冲突和泄漏 |
| P15 总体架构 | `ACAA-M1-S01–S05` | 输入、监督和动作已经定义 | 工件由图编码、后果分布、typed edit与发布策略组成 | 需求 → 架构总览 | 架构是候选设计，不引文伪装为既有结果 | 后继逐模块给张量与动作 |
| P16 图表示 | `ACAA-M9-S01–S04` | scaffold不是类别标签 | AST、控制流、数据流、权限与信息流进入关系图 | 对象结构 → 数学表示 | taxonomy由 Inside the Scaffold；图构造为新设计 | 后继给节点/边来源和防手工标签 |
| P17 三方张量 | `ACAA-M10a-S01–S03`、`ACAA-M10b-S01–S07` | 单向注意不能定位三方冲突 | TriAttn只连接可观察行为、控制位点和风险义务 | 结构需要 → 前向计算 | 公式由本审计负责；不得声称优于基线 | 后继必须给 equal-parameter factor graph |
| P18 推断动作 | `ACAA-M16-S01–S07` | 风险预测若不改变外部行动则贡献不足 | 输出真实 patch commit 与 release manifest动作 | 预测 → 干预 | 现有动作由 SafeHarness/HOL Guard；候选动作是设计 | 后继必须写执行、回滚和审计日志 |
| P19 独立状态效用检验 | `DSDL-E11-S01–S02`、`DSDL-E12a-S01–S03`、`DSDL-E12b-S01–S05` | 理论声称中间状态不可替代 | 应单独检验状态预测、校准和决策增益 | 总体性能 → 中间机制 | 这里只能写预注册指标，未运行不得写“结果表明” | 后继进入打乱/中和试验 |
| P20 机制消融 | `DSDL-E13-S01–S03`、`DSDL-E14a-S01–S03`、`DSDL-E14b-S01–S04` | 相关性提升不证明理论 | 删除、打乱、符号中和与等参数替代决定理论是否成立 | 机制主张 → 反事实检验 | 预注册方向由理论原义承担 | 若通用模型不劣，必须撤销理论贡献 |
| P21 贡献边界 | `DSDL-C1-S01–S04` | 现有文献和候选能力已比较 | 候选没有不可分解的新增能力 | 证据汇总 → 贡献判定 | 只据已核近邻和理论映射；不以“审稿人可能”作证据 | 后继给明确 NO-GO 与可重开条件 |
| P22 局限与结果边界 | `DSDL-Z3_6-S01–S11` | 本审计未运行候选实验，最新论文有工件缺口 | 结论限于当前题与当前证据快照 | 终判 → 适用边界 | 标明 F/P/R/A/N；规划数字与文献数字分开 | 最终文件不得出现虚构结果或“已显著提高” |

这张表要求每个正式段落未来都先确定唯一新增命题，再分配引用责任。当前候选已被撤销，因此不能把这些句键迁移成一篇正文框架；它们只记录终审论证为何逐步从真实情境走到撤题结论。

## 12. 引用与工件核验台账

### 12.1 直接近邻

1. Ben Sghaier, O., Li, H., Adams, B., & Hassan, A. E. (2026). Don't Blame the Large Language Model: How Agent Harness Evolution Shapes Coding Agent Quality. arXiv:2607.03691. [全文入口](https://arxiv.org/abs/2607.03691)。核验：F；复现包当前不可得，不据论文承诺写成已公开。
2. Vats, N., & Golev, O. (2026). The Scaffold Effect in Coding Agents: Harness Choice as a Hidden Variable in Coding-Agent Evaluation. arXiv:2607.22585. [全文入口](https://arxiv.org/abs/2607.22585)。核验：F；匿名日志/配置声明需在正式使用前再确认持久入口。
3. Rombaut, B. (2026). Inside the Scaffold: A Source-Code Taxonomy of Coding Agent Architectures. arXiv:2604.03515. [全文入口](https://arxiv.org/abs/2604.03515)。核验：F。
4. Hu, Q., Tang, Y., Wang, Q., Zhao, L., Zhang, P., Qing, Y., Yao, X., Huang, D., Zhang, L., & Ji, Z. (2026). SABER: Benchmarking Operational Safety of LLM Coding Agents in Stateful Project Workspaces. arXiv:2606.01317. [全文入口](https://arxiv.org/abs/2606.01317)，[公开代码](https://github.com/sssr-lab/saber)。核验：F/R；论文任务数和仓库审计数不一致，使用前必须冻结 manifest。
5. Dai, W., Openja, M., Pham, H. V., Uddin, G., Yang, J., & Wang, S. (2026). ABTest: Behavior-Driven Testing for AI Coding Agents. arXiv:2604.03362. [全文入口](https://arxiv.org/abs/2604.03362)。核验：F；匿名工件入口待复核。
6. Gringras, D. (2026). Safety Under Scaffolding: How Evaluation Conditions Shape Measured Safety. arXiv:2603.10044. [全文入口](https://arxiv.org/abs/2603.10044)，[代码](https://github.com/davidgringras/safety-under-scaffolding)。核验：F/R。
7. Yao, Y., et al. (2026). Harness-Bench: Measuring Harness Effects across Models in Realistic Agent Workflows. arXiv:2605.27922. [全文入口](https://arxiv.org/abs/2605.27922)，[代码](https://github.com/Qihoo360/harness-bench)。核验：F/R。
8. AgentScope Team (2026). PawBench. [公开仓库](https://github.com/agentscope-ai/PawBench)。核验：R；正文元数据在正式引用前需按仓库 CITATION 文件复核。
9. Ursekar, V., Shanker, A., Maurya, Y., Yasser, S., Kalmath, V. S., Chatrath, V., & Xue, Y. (2026). HarnessOpt-Bench: Evaluating LLMs at Harness Optimization. arXiv:2608.06301. [全文入口](https://arxiv.org/abs/2608.06301)。核验：F/N。
10. Sengupta, B., & Wang, J. (2026). HARBOR: Automated Harness Optimization. arXiv:2604.20938. [全文入口](https://arxiv.org/abs/2604.20938)。核验：F/N。
11. Zhang, Y., Wang, J., Ge, Y., Xu, W., Hamm, J., & Reddy, C. K. (2026). Stop Comparing LLM Agents Without Disclosing the Harness. arXiv:2605.23950. [全文入口](https://arxiv.org/abs/2605.23950)。核验：F/N。
12. Pan, W., Liu, S., Lin, C.-Y., Zeng, J., Tang, X., Zhou, X., Lu, Y., & Jia, X. (2026). Evolving Agents in the Dark: Retrospective Harness Optimization via Self-Preference. arXiv:2606.05922. [全文入口](https://arxiv.org/abs/2606.05922)，[代码](https://github.com/wbopan/retro-harness)。核验：F/R。
13. Lin, X., et al. (2026). SafeHarness: Lifecycle-Integrated Security Architecture for LLM-based Agent Deployment. arXiv:2604.13630. [全文入口](https://arxiv.org/abs/2604.13630)，[代码](https://github.com/liu-yang-maker/SafeHarness)。核验：F/R。
14. Zhong, H., & Zhu, S. (2026). AI Harness Engineering: A Runtime Substrate for Foundation-Model Software Agents. arXiv:2605.13357. [全文入口](https://arxiv.org/abs/2605.13357)。核验：F；其受控验证规模有限，不能承担大范围因果结论。
15. Liu, C., Guo, Y., Liu, Y., Yang, Y., Yan, Q., Zhao, X., Hua, W., Liu, S., Li, S., Bu, Y., & Wang, X. E. (2026). Auditing Agent Harness Safety. arXiv:2605.14271. [全文入口](https://arxiv.org/abs/2605.14271)，[代码](https://github.com/UCSB-AI/HarnessAudit)。核验：F/R。
16. Wang, H., Zhang, M., Yu, C., Shang, Y., Hu, X., Wang, G., & Zou, N. (2026). An End-to-End Agent Auditing Engine. arXiv:2608.07346. [摘要入口](https://arxiv.org/abs/2608.07346)，[代码](https://github.com/datamllab/A2E)。核验：A/R；不以摘要支撑方法细节。
17. Ng, A. W., Han, Y., Zhang, J., & Wang, W. (2026). Agent Safety Should Be a Runtime Contract. arXiv:2608.11274. [摘要入口](https://arxiv.org/abs/2608.11274)。核验：A；只用于最新概念边界，不用于撤题主证据。
18. Hashgraph Online (2026). HOL Guard. [公开仓库](https://github.com/hashgraph-online/hol-guard)。核验：R；属于活跃工程基线，正式实验必须 pin SHA/版本。

### 12.2 AIS 理论与算法配置

19. Goodhue, D. L., & Thompson, R. L. (1995). Task-Technology Fit and Individual Performance. MIS Quarterly, 19(2), 213–236. [DOI](https://doi.org/10.2307/249689)。核验：F；单位、构念、样本和利用—绩效链均回读全文。
20. Cram, W. A., Brohman, M. K., Chan, Y. E., & Gallupe, R. B. (2016). Information systems control alignment: Complementary and conflicting systems development controls. Information & Management, 53(2), 183–196. [DOI](https://doi.org/10.1016/j.im.2015.09.012)。核验：F；全文文件 `database_fulltext_all/00576_2016_information-systems-control-alignment-complementary-and-conflicting-systems-development-controls.md`。
21. Bharadwaj, A. (2000). A Resource-Based Perspective on Information Technology Capability and Firm Performance: An Empirical Investigation. MIS Quarterly, 24(1), 169–196. [DOI](https://doi.org/10.2307/3250983)。核验：F。
22. Dunke, F., & Nickel, S. (2020). A data-driven methodology for the automated configuration of online algorithms. Decision Support Systems, 137, 113343. [DOI](https://doi.org/10.1016/j.dss.2020.113343)。核验：F；全文文件 `database_fulltext_all/01880_2020_a-data-driven-methodology-for-the-automated-configuration-of-online-algorithms.md`。
23. Venkatraman, N. (1989). The Concept of Fit in Strategy Research: Toward Verbal and Statistical Correspondence. Academy of Management Review, 14(3), 423–444. [DOI](https://doi.org/10.5465/amr.1989.4279078)。核验边界：本审计通过 Cram 等人的全文回读其 pattern/profile deviation 采用，并核对出版元数据；若未来把 Venkatraman 作为正式核心理论，仍须单独取得并逐段核验原文，不得只依赖 Cram 的转述。

24. Milgrom, P., & Roberts, J. (1990). The Economics of Modern Manufacturing: Technology, Strategy, and Organization. American Economic Review, 80(3), 511–528. [作者公开全文](https://web.stanford.edu/~milgrom/publishedarticles/The%20Economics%20of%20Modern%20Manufacturing.pdf)。核验：P；核对正文中 supermodularity/increasing-differences 的定义页，只承担该形式含义，不以此声称全文理论迁移或制造 model–scaffold 映射。

### 12.3 持续部署与可靠更新

25. Dolstra, E., de Jonge, M., & Visser, E. (2004). Nix: A Safe and Policy-Free System for Software Deployment. Proceedings of the 18th Large Installation System Administration Conference, 79–92. [USENIX全文](https://www.usenix.org/legacy/publications/library/proceedings/lisa04/tech/full_papers/dolstra/dolstra_html/index.html)。核验：F。
26. Davidovič, Š., & Beyer, B. (2018). Canary Analysis Service. ACM Queue, January–February 2018. [Google Research全文](https://research.google/pubs/canary-analysis-service/)。核验：F。
27. Zhai, E., Chen, A., Piskac, R., Balakrishnan, M., Tian, B., Song, B., & Zhang, H. (2020). Check before You Change: Preventing Correlated Failures in Service Updates. 17th USENIX Symposium on Networked Systems Design and Implementation, 575–589. [USENIX全文](https://www.usenix.org/conference/nsdi20/presentation/zhai)。核验：F。

## 13. 一页式终审摘要

| 审计问题 | 结论 | 决定性证据 |
|---|---|---|
| 风险真实吗 | 是 | HarnessAudit/SABER显示完成与边界安全可脱钩，伤害发生在工具轨迹和环境状态 |
| coding agent 是关键行动者吗 | 是 | harness控制循环、工具、权限、状态和回滚共同决定行动 |
| 有公开可运行数据吗 | 有，但需重跑与冻结 | HarnessAudit、Harness-Bench、PawBench、SABER、RHO、SafeHarness |
| 能造需要训练的硬工件吗 | 能 | 三方图后果模型、typed patch proposer、发布 policy |
| 工件超出直接近邻吗 | 否 | 交叉评测 + constrained AutoML + executable harness editing + runtime control 已联合覆盖 |
| 理论真实改变算法吗 | 否 | TTF、control alignment、IT capability均层级/角色错置；supermodularity方向与反号现象冲突 |
| 等参数通用模型能复制吗 | 能 | 无语义 factor graph/graph Transformer/POMDP 可见相同输入并执行相同动作 |
| 是否只是选模型/路由 | 钢人版本不是，但仍是既有能力组合 | 输出已强化为 patch 和 release动作，终判仍不变 |
| 是否值得作为独立 ISR 论文 | 否 | 理论不可替代门和直接能力覆盖门同时失败 |
| 最终动作 | **NO-GO，不保留** | 不进入冻结题目、论文正文或替补池；相关 benchmark 可作为其他论文基础设施 |

**终句：** 这个候选最有价值的发现不是一个应继续包装的论文题，而是一条应进入其他研究基础设施的工程事实：coding-agent 的模型、harness 和风险任务必须按精确版本共同评测。把这条事实进一步训练成预测器、patch生成器和发布控制器，在当前文献边界与理论条件下仍是通用自动配置和安全部署能力的组合，尚不足以形成一篇独立的 ISR 级算法论文。
