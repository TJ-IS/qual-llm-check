# 异质 Coding-Agent 团队知识协调新候选终审

> 审查日期：2026-08-16  
> 文献与技术边界：截至 2026-08-16 公开的一手全文与本地 AIS Basket 全文  
> 审查对象：稳定身份、重复互动且高度互依的异质 coding-agent 团队，是否可凭 TMS 的专长定位、条件可靠性、task–knowledge coordination 与行为化 knowledge application 形成独立安全算法论文  
> 终审结论：**终局 NO-GO；保留候选数为 0；不得占用第三篇题位。**

## 0. 结论先行

这个问题具有真实损害，也能构造可执行实验。两个 coding agents 各自完成局部正确的 feature，却可能因误判谁掌握关键 API 语义、把条件不成立的知识用于共享 obligation，或在专长冲突时采取折中 patch，造成联合 hidden tests 失败、语义回归和错误依赖扩散。CooperBench 已把这种协调损失落在 652 个真实仓库 feature-pair 上；其评价要求两个 feature 在合并后同时通过专家测试，而非只统计消息质量或单体 patch。因而，本次撤题不以“问题不重要”“没有 benchmark”或“尚未训练”为理由。

最强版本也不是简单 router。它为每个成员保留“谁知道什么”的成员专属信念 `D_t^(i)[a,k]`，把真实能力 `E*` 与条件可靠性 `R` 分开；只在任务分解、子任务关系和知识—责任分配上施加 selective-overlap，而不把全部 agent state 对齐；再以 correct/corrupt/sham 同前缀内容置换识别某条知识是否实际进入可执行 patch，并让该 post-action application state 更新后续的 query、allocation、handoff、verification、integration、isolation 与 serialization。这个版本满足“知识被应用”而非“消息被发送”的理论要求，也能产生 local checkpoint。

钢人化之后仍应撤题，原因不是任一近邻单独覆盖全部模块，而是四个更严格的终止条件同时触发。

1. **旧案同构已经触发。** `00P_候选二TMS理论责任与等参数反证.md` 已逐项定义稳定身份、重复且高度互依团队、member-specific `D_t^(i)`、真实能力 oracle、能力×可靠性 2×2、`Q/J/P` 技术世界、显式 `K_t^(i)[u,v,a,k,r]`、correct/corrupt/sham、post-action `A^obs`、同起点 paired rollout、targeted query、allocation、handoff、integration 与等参数 generic 反证。本轮的 selective-overlap loss 是对旧 `K` 的训练化展开，content-swap application feedback 也是旧案第 8 项机制干预，不构成新题。
2. **一般 TMS→machine-agent architecture 已被正面占据。** Lapso、Peterson 与 Miller（2023）的 HCM 已将 shared mental model 与 TMS 合并进 machine-agent project teams，并显式处理知识持有人、credibility 与 anytime selection。CoThinker（TMLR 2026）进一步把 specialization、结构化 collective memory 的 `Update/Retrieve`、expertise directory、communication moderator、small-world network 与 synthesizer 放进可运行多智能体架构。CoThinker 没有本候选的成员专属 belief、task–knowledge coordination 和 causal application，但“将 TMS 变成多 agent architecture”本身已不能再作为一般贡献。
3. **剩余可执行能力被直接近邻的同动作集合联合挤压。** ETI 已从互动历史推断 competence/reliability 并改变 allocation/verification；AgentAsk 已学习 whether/what/whom/how to ask；NeuralFSM 已学习 state transition、routing 与 trust attenuation；SkillGraph 已让技能状态和通信图随结果共同更新；Shepherd 已让 supervisor 在真实代码轨迹上 inject、handoff、discard 和 fork/replay；Claim Plane 已执行 integration 前的 dependency-aware admission、serialize 与 fail-closed；SWEET-RL 和 TeamTR 已分别占据协作信用分配与多组件训练中的 occupancy-shift 控制。候选剩余交集可以形成一次有价值的机制实验，却没有证明一种现有架构难以想到或无法复制的新算法能力。
4. **等信息、等标签、等动作、等参数通用反证成立。** 给 temporal HGT 或 Dec-POMDP 相同成员身份、历史、`D/R/Q/J/P/K/A` 标签、content-swap paired rollouts、动作集合、参数量与 FLOPs，它可以保留每个成员的 private slot，只在 task edges 上做 masked consistency，并用 application state 门控 integration/isolation/serialize。若 selective-overlap mask 由任务关系标签给出，generic 模型可以读取同一标签；若 mask 需要学习，两者面对同一监督。TMS 在这里为 factorization 提供解释和可检验假设，却没有产生 generic 模型不能执行的非交换更新或专用算子。
5. **coding-agent deletion test 失败。** 把代码、hidden tests 与 Git patch 替换成异质运维、科研工具或项目 agent 的可执行 artifact，同一 `D/R/K/A`、content-swap、partial handoff 与 integrate/isolate/serialize 策略仍成立。代码环境提高损害的可执行性和测量精度，却没有改变机制的分析单位。候选因此是一般 heterogeneous tool-agent knowledge coordination 在 coding 数据上的高质量实例，而不是 coding-agent 情境不可删除的独立安全能力。

本文件仍完整给出最强可训练设计，因为只有完成设计后才能区分“可实现”与“可作为独立论文”。结论是前者成立，后者不成立。

第 8 节另行冻结并审查窄 C28。C28 外部固定专家身份、升级点与任务分配，只学习 repo 义务级 knowledge-application program；它没有被完整 TMS 候选的结论自动吞并，而是经过独立 I/O、动作、理论责任和子 SMDP 约化后同样判定 NO-GO。

## 1. 阅读协议、实际全文与证据边界

### 1.1 本地材料的完整回读

本轮完整回读了以下本地文件，并按 `00F` 与 `00W` 的句责规则建立文末逐句卡。

- `thesis_papers_v8_reliable_action/00P_候选二TMS理论责任与等参数反证.md`。它不是本轮结论的快捷依据，而是旧案同构检验的比较基准。
- `database_fulltext_all/14982_2007_the-impact-of-knowledge-coordination-on-virtual-team-performance-over-time.md`，Kanawattanachai 与 Yoo（2007）MISQ 全文。
- `database_fulltext_all/09708_2010_the-impact-of-information-technology-and-transactive-memory-systems-on-knowledge-sharing-applica.md`，Choi、Lee 与 Yoo（2010）MISQ 全文。
- `thesis_papers_v8_reliable_action/00F_逐段双ISR写作与引用审计协议.md` 与 `00W_肖帅勇两篇ISR源行句段主键Manifest.md`。
- 肖帅勇老师 ACAA 与 DSDL 两篇 ISR 本地全文，以及 `00J_肖帅勇两篇ISR全篇逐句逻辑与引文责任索引.md`、`00K_DSDL全篇逐句逻辑与引文责任索引.md`、`00M_ACAA实证贡献与结论逐句逻辑索引.md`。本审计使用 manifest 的精确语法句键，不把段落解析成功冒充功能同位，也不近似改写原句。

通过只读 Otero Open API 搜索 `transactive memory`、`knowledge application` 与 `knowledge coordination`，并沿本地 AIS 全文的参考文献责任核查相关构念。Otero 搜索返回的条目用于定位和核对元数据；理论命题只取自实际回读的 Kanawattanachai 与 Yoo（2007）和 Choi 等（2010）全文。Faraj 与 Sproull、Kudaravalli 等仅有摘要或二手回指的文献没有被写成“已全文验证”。

### 1.2 在线一手全文回读账

| 一手工作 | 实际回读范围 | 本审计允许其承担的责任 | 不允许外推的责任 |
|---|---|---|---|
| [CooperBench](https://arxiv.org/abs/2601.13295) | arXiv 全文、附录与项目方法页 | 652 个 feature-pair、12 个 libraries、4 种语言、真实仓库、专家测试、协作低于 solo、消息/承诺/预期失配 | 轨迹没有 `D/R/K/A` 真值，也不是稳定重复团队 |
| [Multi-Agent Teams Hold Experts Back](https://arxiv.org/abs/2602.01011) | OpenReview/arXiv 全文 | 团队即使知道 expert 仍会 integrative compromise；expert leveraging 比 identification 更接近瓶颈；规模扩大加剧稀释，并存在对抗鲁棒性权衡 | 非 coding、非学习型长期团队策略；不能直接给 TMS 状态标签 |
| [SkillGraph](https://arxiv.org/abs/2604.17503) | arXiv HTML 全文 | query/content/skill-conditioned 图、skill bank、running accuracy、failure buffer 与动态图更新 | 视觉任务，不区分 actual ability 与 member belief，也不识别 knowledge application |
| [Shepherd](https://arxiv.org/abs/2605.10913) | arXiv HTML/PDF 全文 | typed effect trace、fork/replay、inject/handoff/discard；CooperBench 上的 live supervision | prompt-based meta-agent 不证明 TMS；不能把 runtime substrate 当本候选 checkpoint |
| [Claim Plane design](https://arxiv.org/abs/2607.21909) 与 [confirmatory study](https://arxiv.org/abs/2608.00947) | 两份 arXiv 全文 | versioned ChangeIntent、typed dependency、pre-write admission、promotion、serialize/fail-closed；30 pairs×3 seeds 的公开确认性边界 | 静态策略主要靠串行获得可靠性；`J` 与 serialization 不能算 TMS |
| [SWEET-RL](https://arxiv.org/abs/2503.15478) | arXiv 全文 | ColBench backend/frontend 协作、训练时额外信息、step-wise critic 和多轮信用分配 | 人—agent 协作不等于稳定异质 agent team；细粒度 reward 不等于 TMS |
| [ETI](https://aclanthology.org/2026.acl-long.77/) | ACL 2026 正式全文 | 从历史推断 warmth/competence，competence 明含 ability、reliability、adaptability、efficiency，并改变 reassign/verify 等协调决定 | 主要是 inference-time structured profile，不提供内容级 application 因果标签 |
| [AgentAsk](https://aclanthology.org/2026.acl-long.1294/) | ACL 2026 正式全文 | edge error taxonomy；`ask gate + addressee + question`；SFT 与 E-GRPO 权衡准确率、成本和时延 | 未处理成员专属 TMS 与 executable patch application |
| [NeuralFSM](https://aclanthology.org/2026.acl-long.1543/) | ACL 2026 正式全文 | Temporal Coordination Controller 学习 transition distribution 与 communication weights；graph regularization 与 trust attenuation | `trust` attenuation 不等于 cognition-based trust，learned state 也不天然是 TMS |
| [AgentRouter](https://aclanthology.org/2026.acl-long.33/) | ACL 2026 正式全文 | query/entity/agent 异质图、经验软标签、routing distribution 与 weighted aggregation | QA router 不能证明 coding safety，但构成等信息 HGT 直接基线 |
| [Social Dynamics](https://aclanthology.org/2026.acl-long.1756/) | ACL 2026 正式全文 | 控制 peer 数、相对能力、论证长度和修辞，显示 perceived expertise 与社会压力可改变代表 agent 的客观判断 | adversarial peer 实验不等于良性条件可靠性，也没有学习协调动作 |
| [HiddenBench](https://arxiv.org/abs/2505.11556) | arXiv/OpenReview 全文与公开格式 | 65 个 hidden-profile tasks、非对称信息和 distributed knowledge integration failure | 选择题正确率不等于知识进入可执行 artifact |
| [EMRC](https://arxiv.org/abs/2508.13754) | arXiv 全文 | 医疗部门×难度 expertise table、动态招募、confidence fusion 与 adversarial validation | 静态 expertise table 和自信分数不能替代真实条件可靠性 |
| [TeamBench](https://arxiv.org/abs/2605.07073) | arXiv 全文与项目方法页 | 851 templates、931 instances；OS 强制 Planner/Executor/Verifier 信息与权限分离；deterministic grader 与人类研究 | 固定三角色不是重复形成的 TMS；verifier verdict 不是 application 标签 |
| [TeamTR](https://arxiv.org/abs/2605.15207) | arXiv HTML 全文 | sequential component update 的 compounding occupancy shift；逐组件重采样和 KL trust region | 解决训练分布漂移，不产生 TMS 构念，但必须作为协作训练强基线 |
| [Collaborative Expertise Delegation](https://arxiv.org/abs/2505.07313) | arXiv 全文 | expertise-domain alignment、structured workflow 与 diversity integration、team scale 的权衡 | 探索性设计不提供长期 belief 或 coding harm 标签 |
| [SciCrafter](https://arxiv.org/abs/2604.24697) | ICLR 2026/OpenReview 全文与项目页 | 将 gap identification、discovery、consolidation、application 分开，并用可执行 Minecraft redstone 任务诊断 | application 是残余能力测量，不是团队内来源特异的 causal application state |
| [KATE](https://aclanthology.org/2026.findings-acl.710/) | Findings ACL 2026 正式全文 | acquisition、activation、internalization 分段；经验知识、并行采样、knowledge-aware SFT/RL 进入真实 tool execution | 单 agent tool calling，不含 member-specific task–knowledge coordination |
| [CoThinker](https://openreview.net/forum?id=8BYJHZiZ5T) | TMLR 2026 正式全文及附录中的 TMS prompt architecture | specialization、结构化 collective memory `Update/Retrieve`、expertise directory、consensus/open issues、communication moderator、small-world 与 synthesizer | 主要责任是 cognitive-load/context compression；没有 member-specific belief、TKC 或 content-swap application |
| [A Hybrid Cognitive Model for Machine Agents](https://doi.org/10.1016/j.cogsys.2023.02.007) | Cognitive Systems Research 正文、模型与结果 | SMM+TMS 的 machine-agent hybrid；知识持有人、credibility、project/action team 与 anytime selection | 不是 LLM coding agent，也没有本候选的可训练反事实政策 |

`Claim Plane`、`CooperBench` 和预印本的数字只用于报告原作者已运行的设计与结果。下面所有拟议模型、算力和效应均是钢人化研究设计，不是已发生的实验。

## 2. 广义安全对象与行动边界

### 2.1 真实损害

候选的安全结果不是“团队聊得不顺”，而是知识协调错误进入可执行修改。具体损害包括：一个 agent 提供在旧版本成立的 API 语义，另一 agent 将其用于共享 abstraction；真实专家的正确方案被多名较弱成员折中稀释；成员有能力却不能稳定兑现 handoff，导致依赖方按未完成接口继续实现；团队只看见两个 feature 的局部测试通过，却在 integration 时破坏跨 feature invariant。受影响对象是代码仓库、下游使用者、依赖该软件的组织流程和承担返工的开发团队。

主要外部安全指标应是联合 hidden-contract violation、语义回归、错误知识导致的 executable state delta、进入 integration 的不安全 patch、二次修复与 rollback 数量。单纯的消息提及率、专家选择准确率、merge 率、评论数或 agent 自评不得作为主要风险结果。

### 2.2 决策时点与可见状态

算法在五类时点介入。

1. 分解相互依赖任务后、尚未确定知识责任时，决定是否 probe、询问、扩大共享还是保持成员专门化。
2. 收到知识 packet 或能力声明后、尚未把它写入代码时，决定 route、验证、暂存或隔离。
3. 一个成员开始修改共享 obligation 前，决定 allocate、reassign、partial handoff、overlap verification 或 serialize。
4. 多个 patch 即将合并时，决定 integrate、isolate、discard、replay 或回到另一分支。
5. 可执行结果返回后，依据 post-action application 与 outcome 更新成员专属 belief 和后续协调策略。

可见信息包括稳定 agent 身份、历史任务与工具轨迹、成员消息及其来源、当前 repo tree、issue、tests、diff、权限、暂定 assignment、显式依赖和已经运行的 probes。不可见信息包括当前任务上的真实专长、隐藏合同、未来 patch 的语义结果、某成员在具备机会时是否兑现、以及一段被共享知识是否真正造成特定代码动作。测试时不得读取当期 `E*`、隐藏测试和实际 `A^obs`；只能从过去历史形成 belief 与 outcome prediction。

### 2.3 正常、风险与纠正动作

- **正常动作**：inspect repo、查阅 API 与 tests、执行无副作用 probe、发送定向问题、给知识 packet 附可执行证据、按 assignment 修改局部代码、运行局部和联合测试。
- **风险动作**：无视成员条件可靠性直接接受高能力者声明；将全部状态强制对齐而抹平专门化；把所有单项看似正确的方案都合并；在任务关系不明时继续并行；用多数折中替代可执行义务。
- **纠正动作**：请求内容特异 probe；改变 packet 路由；reassign 或 partial handoff；只对任务关系形成共享表征；增加 overlap verification；隔离错误 branch；serialize 有依赖的 obligation；discard/replay 可逆轨迹；依据实际 application 和 outcome 修订 `D/R/K`。

候选不能靠“拒绝所有共享”“始终选最大模型”或“全部串行”获胜。主要 Pareto frontier 必须同时报告风险、联合任务成功、通信与工具成本、时延、重复工作和成员专门化利用率。

## 3. AIS 理论原义与层级校正

### 3.1 Kanawattanachai 与 Yoo（2007）实际检验了什么

Kanawattanachai 与 Yoo 在 38 个 virtual teams、146 名 MBA 学生和八周商业模拟中检验 TMS 的时间结构。成员被赋予持续的业务角色，任务高度互依，团队在第 2、5、8 周测量状态。论文区分三项维度。

- `expertise location` 是成员关于“谁知道什么”的 meta-knowledge，而不是研究者掌握的真实能力表。
- `cognition-based trust` 的量表同时涉及 competence/preparation、careless work 和是否兑现承诺，不能被简化成一次 success score，也不能被硬拆成理论本身要求正交的能力与可靠性。
- `task–knowledge coordination` 涉及对成员决策关系、行动互联、整体绩效和业务功能协调的共同理解。论文将 expertise location 与 cognition-based trust 对 performance 的影响放在 TKC 中介链上。

纵向结果还给出重要边界。早期 task-oriented communication 有助于形成 expertise location 与 cognition-based trust；后期 TKC 才成为绩效的重要前因。expertise location 与 cognition-based trust 较为黏着，TKC 更动态。绩效反馈对三项状态的负向调节并未普遍获得支持，只有部分时间路径成立。因此，本候选可预注册早期 evidence acquisition、后期 coordinated application 的差异，却不能把“坏结果必然按某固定律重置信任”写成硬编码更新。

原分析单位是真正的团队成员、持续角色和共同任务。一个中央 coordinator 自己保存 `D[a,k]` 并把其输出发给匿名、一次性 subagents，不足以形成分布式 TMS。最低映射必须保留谁持有关于谁的 belief，并观察成员能否检索、采纳或修订该 belief。

### 3.2 Choi、Lee 与 Yoo（2010）对 knowledge application 的责任

Choi 等在韩国两家公司 139 个持续团队、743 名成员上检验 IT support、TMS、knowledge sharing、knowledge application 与 team performance。全文将 knowledge application 定义为把既有知识用于当前问题的阶段。论文报告 TMS 同时关联 sharing 与 application，sharing 关联 application，application 直接关联 performance；sharing 对 performance 的直接路径不成立，其作用由 application 完全中介。

这组结果只支持三项设计约束。第一，消息被发出、读到或复述不能当作 application。第二，若 shared packet 没有内容特异地改变后续 executable action，它不能承担 performance 机制。第三，application 是 TMS 的下游过程，不能被重命名为 TMS 的第四维。该研究是横截面团队问卷，knowledge application 使用团队感知量表；它不提供 action-level 标签、动态更新律或 content-swap 因果识别。候选的 `A^obs` 与 paired intervention 是本研究新增的测量设计，不能归给原理论。

### 3.3 HCM 与 CoThinker 压缩的一般理论空位

HCM 已证明 SMM 与 TMS 可被形式化为 machine-agent team 的混合认知结构。其 TMS 表示知识由谁持有以及来源 credibility，共享区又承担共同 task/state/goal/plan 等内容；模型依据团队类型和信息条件选择认知表示。该工作排除了“以 TMS 为机器团队建模”这一一般新颖性。

CoThinker 是更直接的 LLM 多智能体基线。它让专门化 agents 各自处理子问题，由 TMS manager 将 expertise directory、共识、artifact、分歧和 open issues 压缩成 collective memory，并在轮次间执行 `UpdateMem`；communication moderator 再限制每个成员读取的 peer messages。其 TMS 主要解决长上下文与 cognitive load，而非测量成员之间互不一致的 belief，也没有显式 TKC 张量或 causal application label。这个差异足以支持一项更严格的机制比较，却不足以再宣称“首次将 TMS 进入多智能体 forward”。

### 3.4 合法与不合法的构念映射

| 状态 | 理论所有权 | 技术所有权 | 本轮判定 |
|---|---|---|---|
| `E*_{a,k,t}`，隔离测试得到的真实能力 | TMS 预设专门化，但不产生 oracle | probe、hidden tests、时间切片 | 仅作训练/评价真值，测试时不可见 |
| `D_t^(i)[a,k]`，成员 `i` 对成员 `a` 的专长定位 belief | expertise location 的直接映射 | 概率化、校准、证据 provenance | 合法；必须 member-specific，不能退化成中央表 |
| `R_t^(i)[a,k,q]`，在具备能力、机会和权限时兑现某类声明的概率 | cognition-based trust 支持能力与可靠执行均重要 | 条件化定义、claim schema、机会与权限 | 部分合法；`R` 是为辨别效度新增的潜变量，不是原文独立维度 |
| `Q_t[u,k]`，子任务需要什么知识 | 理论说明知识需匹配任务，不给出 oracle | two-world contract 与任务生成器 | 外部 task-world state，不计理论工件 |
| `J_t[u,v,r]`，软件语义依赖 | 无 TMS 所有权 | dependency/world model | 纯技术状态；Claim Plane 直接基线 |
| `P_t[a,tool,path]`，权限与可执行机会 | 无 TMS 所有权 | sandbox/capability mask | 纯技术状态；用于避免把无机会误判为不可靠 |
| `K_t^(i)[u,v,a,k,r]`，成员对任务分解、关系、知识和 owner 的联合表示 | TKC 的最接近映射 | 张量因子化、稀疏图、overlap 计算 | 合法但必须只在 task relations 上形成重叠，不能池化成一个团队向量 |
| `A_t[a,u,k,c]`，知识 packet 对 executable action 的内容特异应用 | Choi 等支持 sharing/application 区分；不是 TMS 内部维度 | correct/corrupt/sham、paired rollout、action predicate | 合法下游状态；实际 `A^obs` 只能在行动后更新下一时点 |

### 3.5 理论方向冲突

理论真正有用的地方是阻止四种看似合理却方向相反的通用做法。

1. **all-alignment 与 no-alignment 冲突。** 全部 hidden states 对齐会抹平专门化；完全不重叠又使成员不知道任务如何分解、子任务怎样关联和知识应由谁用于何处。最强候选只对 `G[u,v,r]`、`Q[u,k]` 与 assignment relation 的 task-scope projection 施加 overlap，对 `D/R` 与来源证据保持成员差异。
2. **真实能力与条件可靠性冲突。** 高能力但常在无权限或无时间窗口时做出未兑现承诺的成员，不应与低能力但稳定复述简单知识的成员压成一个 trust score。理论只要求团队同时识别 competence 与 reliable work；具体何时 query、verify 或 reassign 必须从可执行 outcome 学习。
3. **expert leveraging 与 corruption robustness 冲突。** `Experts Back` 显示强 expert 的方案可能被折中稀释，但盲从最强成员又会降低面对错误或 adversarial member 的鲁棒性。只有条件化 packet evidence、task need 与 application outcome，才能在两者间学习动作。
4. **sharing 与 application 冲突。** 大量消息可以提高知识可见性，却增加 context load，并不能保证知识进入正确 obligation。应用反馈若显示 packet 只被复述而未改变代码，后续策略应降低广播、改用 targeted probe 或 executable handoff。

这些冲突支持机制假设与消融，但不自动构成算法独占。第 8 节将证明同信息 generic model 可以实施完全相同的 selective-overlap 与 post-action update。

## 4. 旧 `00P` 同构审计

### 4.1 新候选与旧案逐项对照

| 本轮钢人化要素 | `00P` 已有责任 | 本轮是否形成严格新结构 |
|---|---|---|
| stable identities、重复互动、高任务互依 | `00P` 第 5.2 节将三者列为 TMS 最低环境，并要求低互依负控制 | 否 |
| member-specific expertise belief | `D_t^(i)[a,k]`、belief dispersion、overlap 与 provenance 已定义 | 否 |
| actual ability ≠ belief | `E*` 与 `D` 的角色、测试时隔离和 relocation 干预已定义 | 否 |
| ability ≠ conditional reliability | `R_t^(i)[a,k,q]`、机会 `O`、权限 `P` 与 2×2 因子已定义 | 否 |
| explicit task–knowledge coordination | `K_t^(i)[u,v,a,k,r]` 及 `G/Q/X` 因子化已定义 | 否 |
| selective overlap without erasing specialization | 旧案已要求 overlap/dispersion 和低互依负控制；本轮仅把它写成 masked loss | 只有训练表达的细化，不是新题 |
| correct/corrupt/sham application | 同来源、同格式、同长度内容置换、paraphrase、source/format control 与 `A^obs` 已定义 | 否 |
| post-action feedback | 旧案明确 actual `A` 不能进入当期 policy，只能训练 `hat A` 并更新下一时点 | 否 |
| query、allocate、handoff、verify、integrate/isolate/serialize | 旧案已有 query、allocate、handoff、serialize、discard/rollback 责任与近邻边界 | 否 |
| equal-parameter HGT/POMDP counterproof | 旧案已规定 same raw evidence 与 same `D/R/Q/A/J/P` supervision 两层比较 | 否 |

### 4.2 为什么“旧案修复”不能冒充“新候选”

旧 `00P` 的结尾允许未来在完成 member-specific directory、TKC、2×2、two-world、post-action application 与 equal generic pilot 后，以新候选重新送审。那是一个重新审查的程序条件，不是保留题位的承诺。本轮确实把旧案最薄弱的 `K` 进一步变成 selective-overlap loss，也加入 CoThinker、HCM、ETI、AgentAsk、NeuralFSM、TeamTR、SciCrafter 与 KATE 等 2026 近邻。然而，新资料没有产生不同的行动结构，反而压缩了一般 TMS architecture、skill-conditioned routing、application 与 learned transition 的空位。

因此，新候选不能以“旧案缺的构念已经补齐”为理由通过。补齐使它成为可运行设计，却没有使它与旧研究对象、旧状态、旧动作和旧反证分离。

## 5. 直接技术近邻的联合挤压

### 5.1 现象、benchmark 与外部损害

CooperBench 是最合适的 coding 外部评价，而不是 TMS 训练真值。两个 agents 只看见自己的 feature 需求并在同一 repo 上工作，最终由两组 tests 的合并结果判定。论文显示沟通可缓解部分空间冲突，却不能稳定解决语义协调，且团队平均低于 solo。这证明“消息存在不等于协调成功”，也给 executable harm 提供真实入口。它没有稳定团队、成员能力干预、belief 或 application 标签，因此必须扩展而不能直接监督 `D/R/K/A`。

`Multi-Agent Teams Hold Experts Back` 更直接证明 expertise dilution。即使团队被告知谁是 expert，也会把强意见与弱意见折中；团队规模扩大时该倾向增强。其同时发现 consensus 对 adversarial robustness 的潜在收益，正好提供“用 expert”与“抗错误 expert”的冲突。该实验不是 coding，也没有训练 agent-side controller，不能单独覆盖候选；但它排除了“只需告诉团队 expert identity”这一弱方案。

HiddenBench 给 distributed information integration 提供 65 个可复现 hidden-profile tasks，TeamBench 则用 OS 权限把 specification、编辑与认证分给 Planner、Executor、Verifier。两者都比自由对话更容易观察信息缺口，却仍缺少内容特异 knowledge application。它们适合作 pretraining/diagnostic 与 role-access robustness 测试，不能替代 two-world executable coding 环境。

### 5.2 inference、query 与 routing 已占据的能力

ETI 已把 interaction history 转成 structured partner traits，并让 competence profile 改变任务分配和额外验证。其 competence 维度明含 ability 与 reliability，虽然没有本候选的条件化 `R` 和 member-specific belief owner。故 `D/R→allocate/verify` 不能单独成为新增能力。

AgentAsk 的动作已经是 whether、what、whom 与 how to ask，训练又显式权衡任务效用、成本和时延。故 targeted query 不是候选贡献，只能是 action-space 成员。AgentRouter 用 query/entity/agent 的 heterogeneous GNN 与经验 performance 软监督学习 routing distribution；EMRC 用部门×难度 expertise table 动态招募医疗 agents；二者要求候选必须击败 expertise-aware routing，而不能只报“选对专家”。

NeuralFSM 更接近完整 policy。它从 task context 与历史学习 state-transition distribution 和 communication weights，用 graph regularization 与 trust-aware attenuation 控制 noisy/adversarial agent。候选若只把 `D/R/K` 拼成一个 state 再输出下一 agent 或 message edge，就与 NeuralFSM 同构。SkillGraph 又让 skill embeddings、failure buffer 和 collaboration graph 随结果共演化。只有 task–knowledge selective overlap 与 causal application 还能构成差异化机制实验。

### 5.3 executable action 与训练已占据的能力

Shepherd 已提供 typed、可逆且可 fork/replay 的 coding-agent trace，并让 live supervisor 在 CooperBench 上执行 inject、handoff 和 discard。候选不能把“看到多 agent 轨迹后做 partial handoff”当新能力；公平基线必须给 Shepherd meta-agent 同 observation、continuation budget 和 fork 数。

Claim Plane 已在写入前用 typed dependency 与 versioned intent 决定并行、promotion、serialize 和 fail-closed。其确认性研究还显示静态策略可因近似总串行获得表面可靠性。候选必须把 `J`、scope 和 action budget 对齐，并单独报告真正并行的成功与 wall-clock；若收益来自更准确 dependency 或更多 serialization，应归给 concurrency control，而非 TMS。

SWEET-RL 已用训练时额外信息训练 step-wise critic；TeamTR 已说明逐组件更新会改变后续 agent 的 occupancy distribution，并通过重采样与 KL trust region 控制累积偏移。前者挤压“细粒度 handoff reward”，后者挤压“按顺序微调多个 agent 即可稳定协调”。最强候选可以采用 TeamTR 作为优化器，但不能把它计入理论贡献。

### 5.4 knowledge application 与 TMS architecture 已占据的能力

SciCrafter 明确区分 gap identification、discovery、consolidation 与 application，并用可执行 redstone artifact 测量 discovery-to-application loop。KATE 则区分 knowledge acquisition、activation 与 internalization，用并行采样和 knowledge-aware RL 改善真实 tool execution。两者都没有成员间 task–knowledge coordination，也没有 source-specific content swap，但已经排除“一般知识应用缺口”和“让知识进入 tool action”作为独立主张。

CoThinker 的重要性高于普通背景。它已经把 TMS 专长目录、共享 artifact、共识、分歧、open issues、轮次更新、通信 moderation 和 specialization 放进多 agent forward。候选的剩余责任必须是 CoThinker 没有的 member-specific belief dispersion、TKC selective overlap 与 causal application update。把 CoThinker 只列为 prompt baseline 会低估直接覆盖；它必须与相同 backbone、轮数、token 与 memory budget 正面比较。

### 5.5 联合覆盖为何在本案可以终止

“没有任何一篇论文同时包含全部部件”不能证明空白。通常，联合覆盖只提示应做组合基线，不能自动撤题。本案之所以终止，是联合覆盖还叠加了两个独立事实：第一，旧 `00P` 已把同一交集完整送审；第二，等信息 generic model 能复制理论 factorization 的全部动作效果。若只存在联合覆盖而 generic 反证不成立，本候选仍可进入 identification pilot；当前两项都成立，所以不能保留。

## 6. 最强可训练版本

### 6.1 直白研究问题

在稳定、重复且高度互依的异质 coding-agent 团队中，一个分布式知识协调策略能否通过成员专属 expertise/reliability belief、只针对 task–knowledge relations 的选择性共享表征，以及内容特异的 post-action knowledge-application feedback，在不抹平专门化、不依赖总串行和不过量验证的条件下，减少错误知识进入联合 patch 所造成的 hidden-contract violation？

这一定义故意把主要结果放在可执行 harm，而非 member selection accuracy。若只预测“谁更擅长”或“该不该问”，题目应降格为 ETI/AgentAsk/AgentRouter 的领域移植并撤销。

### 6.2 环境与同起点反事实

可运行环境以 CooperBench 的 repo、feature pairs、专家 tests 和语言多样性为基础，再增加三层冻结资产。

1. **two-world contract。** 对同一代码前缀创建 `W0/W1` 两个世界；公开 issue、可见 tests 与大部分 repo 相同，但某个 hidden obligation 方向相反。知识 packet 才包含区分世界所需的 API/contract 事实。应先证明没有 knowledge-free workaround。
2. **correct/corrupt/sham。** correct 与 corrupt packet 同来源、同长度、同格式、同置信语气，只替换关键谓词方向；sham packet 保持结构但不含决定性信息。另设语义等价 paraphrase、source-swap 与 format-swap 控制。
3. **stable team sequence。** 同一组 3–5 个 agent identities 跨 20–40 个任务重复合作；仓库家族、知识域、工具权限和模型 checkpoint 形成稳定但可干预的异质性。低互依 tasks 作为理论负控制。

能力×可靠性采用 2×2 操纵。`E*` 通过独立、隔离且不泄露当前 hidden obligation 的 executable probes 定义；`R` 通过固定能力 checkpoint 后改变 claim/follow-through policy，并条件化机会、权限和 deadline。不能仅在 prompt 中宣称“你是不可靠的成员”。

每个关键决策点从同一 filesystem、agent memory、消息历史、随机种子和 tool state fork，多臂执行 query/route/allocate/handoff/verify/integrate 等动作，得到后续 state delta、hidden-test vector、task success、harm 与成本。Shepherd 的 typed trace 与 fork/replay 可作为运行底座，但不能计入候选贡献。

### 6.3 输入、输出与关键张量

设 agent 集合为 `A`，知识域为 `K`，子任务为 `U`，任务关系为 `R_g`，claim 类型为 `Q_c`。

- `H_t^(i)`：成员 `i` 可见的历史，包括消息、tool events、diff、test evidence、assignment 与 provenance。
- `E*_{a,k,t} ∈ [0,1]`：真实能力 oracle，只在训练/评价标签中出现。
- `D_t^(i) ∈ [0,1]^{|A|×|K|}`：成员 `i` 对每个知识持有者的 belief distribution，并附 evidence provenance 与 uncertainty。
- `R_t^(i) ∈ [0,1]^{|A|×|K|×|Q_c|}`：条件可靠性，估计有能力且有机会时某类 claim/commitment 的兑现概率。
- `G_t ∈ {0,1}^{|U|×|U|×|R_g|}`：任务分解和子任务关系。
- `Q_t ∈ {0,1}^{|U|×|K|}`：每个子任务的知识需求。
- `X_t^(i) ∈ [0,1]^{|U|×|A|×|K|}`：成员 `i` 认为某成员应在某 obligation 上持有或应用何种知识的 assignment belief。
- `K_t^(i)`：由 `G/Q/X` 因子化形成的 TKC，不允许只保存 pooled graph embedding。
- `J_t ∈ {0,1}^{|U|×|U|×|R_s|}`：代码/配置/API 的软件语义依赖，明确标为技术 world state。
- `P_t ∈ {0,1}^{|A|×|Tool|×|Path|}`：权限与执行机会 mask。
- `A_t^obs[a,u,k,c]`：post-action application 标签，`c∈{correct,corrupt,sham,none}`；同时记录知识是否改变 action predicate 及其 utility。
- `Y_t`：hidden tests、functional/security regression、state delta、task success、tool/communication cost 和 latency。

输出不是一个 risk score，而是分布式 policy 对真实低层动作的条件分布：`probe(k,u)`、`query(i→a,k,u)`、`route(packet,a→b,u)`、`allocate/reassign(u,a)`、`partial_handoff(scope,a→b)`、`overlap_verify(u,k)`、`integrate/isolate(branch)`、`parallel/serialize(edge)`、`discard/replay(trace)`。动作之后仍由 coding agents 调用 read/edit/test/git 等工具执行真实修改。

### 6.4 架构与前向计算

最强架构由四部分组成。

1. **成员专属 temporal encoder。** 每个成员以共享参数编码自己的可见事件，stable identity embedding 只标识长期槽位，不携带当前任务 oracle。GRU/TGN 更新 `D/R` 的自然参数和 provenance attention。
2. **typed temporal HGT。** 节点含 agent、subtask、knowledge、file/API、claim 与 branch，边含 owns、needs、depends、claims、applies、modifies 与 verifies。消息传递保留 member-private views，再形成 task-relation projection。
3. **selective-overlap TKC layer。** 只对 `G/Q/X` 所定义的 task decomposition、subtask relation 与 assignment projection 施加跨成员 consistency；`D/R` 的 holder-specific evidence 不被全局对齐。其核心不是让所有 hidden states 相似，而是让成员对共同任务结构形成最小必要重叠。
4. **counterfactual application world model 与 actor。** world model 预测不同 packet content 和协调动作下的 `A`、state delta、hidden-test vector 与 cost；actor 在该 belief state 上选择低层协调动作，并把实际 post-action `A^obs/Y` 写回下一时点的 local belief。

可写成：

```text
Z_t^(i) = Enc_theta(H_t^(i), id_i)
(D_t^(i), R_t^(i)) = Belief_phi(Z_t^(i), provenance_t)
K_t^(i) = TKC_psi(G_t, Q_t, X_t^(i), D_t^(i), R_t^(i))
M_task = Mask(G_t, Q_t, active_obligations_t)
B_t = HGT_omega({Z_t^(i)}, {K_t^(i)}, J_t, P_t)
(A_hat, Delta_hat, Y_hat) = World_xi(B_t, packet_content, action)
action_t ~ pi_eta(B_t, A_hat, Delta_hat, Y_hat, action_mask)
```

`Mask` 是本候选最容易被误写成理论贡献的部分。TMS 说明任务—知识协调需要共同理解任务分解、关系和分配；它不提供具体 AST relation、hidden contract 或 mask oracle。因此 `M_task` 的标注与学习属于研究者的技术设计。公平 generic baseline 获得同一 mask supervision。

### 6.5 损失函数

拟议总目标仅是设计，不是已验证公式：

```text
L = lambda_D L_cal(D, E*)
  + lambda_R L_cond(R, fulfillment | E*, opportunity, permission)
  + lambda_K L_edge(K, G, Q, X)
  + lambda_sel L_selective_overlap
  + lambda_A L_application
  + lambda_cf L_content_swap
  + lambda_W L_world
  + lambda_pi L_CMDP
  + lambda_cost L_budget.
```

- `L_cal` 用 held-out probes 的 ability label 校准 `D`，但屏蔽当前任务 oracle；另报成员之间 belief dispersion 与 Brier/ECE。
- `L_cond` 在具备能力、机会和权限的样本上估计 claim fulfillment，防止把无权限或未被调用混入不可靠。
- `L_edge` 监督 task decomposition、knowledge need 与 assignment relations。`G/Q/X` 错误必须分别报告，不能让一个 pooled accuracy 掩盖。
- `L_selective_overlap = Σ_{i<j} ||M_task ⊙ (Proj(K_i)-Proj(K_j))||²`，只压缩共同 task relations。专长保持由 holder-specific evidence prediction、identity permutation test 与 collapse penalty 检查；理论不支持人为让 `D` 正交。
- `L_application` 用 executable action predicate 与 hidden outcome 训练 correct/corrupt/sham/none；消息复述或模型自评不入真值。
- `L_content_swap` 约束同前缀 correct/corrupt 两臂的预测差与实际 state-delta 差一致，并用 sham/source/format controls 排除一般服从。
- `L_world` 预测 test vector、semantic state delta、secondary regression 与成本，而非只预测 pass/fail。
- `L_CMDP` 优化联合任务效用，同时约束 executable harm、人工/工具/通信预算；采用 TeamTR 式逐组件重采样和 KL trust region 作为训练稳定基线。

若去掉 `L_application` 后 actor 动作不变，它只是辅助头；若去掉 `L_selective_overlap` 后 generic model 仍学习相同 task alignment，则 TMS 专用计算责任不成立。

### 6.6 训练样本、标签与 local checkpoint

训练数据分三层。

- **belief layer**：稳定团队的历史 probes、任务结果、兑现机会和权限事件，生成 member-visible evidence 与研究者 oracle `E*/R`。belief label 必须遵守成员可见边界。
- **coordination layer**：从 gold task contracts、AST/call graph、test ownership 与 feature dependencies 构造 `G/Q/J/X`；多人专家抽样审核一部分 relation，防止 gold patch 结构成为唯一真理。
- **application layer**：同起点执行 correct/corrupt/sham、source-swap、format-swap 与 knowledge relocation，依据 diff predicate、execution trace、hidden tests 和 state delta 标 `A^obs/Y`。

可训练工件包括 temporal event encoder、HGT、`D/R/K/A` heads、counterfactual world model、actor/critic、calibration maps，以及固定版本的 tokenizer、feature schema 和 relation manifest。不得把云端 LLM 生成的自然语言判断当标签；云端模型若用于 worker rollout，只能作为冻结环境组件，主算法 checkpoint 必须本地训练并可复现。

### 6.7 split、泄漏与算力

训练/验证/测试需同时按 repository family、time、hidden contract template、knowledge domain、agent checkpoint 与 team identity 分组。任何同一 repo commit、feature pair 的 paraphrase、correct/corrupt/sham sibling 或 forked prefix 必须位于同一 split。gold patch、hidden tests、`E*` 当前任务值、未来 `A^obs` 和对照臂结果不得进入推断输入。测试集再设置三类 OOD：新仓库/语言、新 agent checkpoint、新的 dependency topology。

一个可行但尚未运行的资源包为：50,000–100,000 个 team decision prefixes，每个 3–6 个反事实 continuation；300M–800M 参数的 event/code encoder 与 30M–100M HGT/world-model heads；2×80GB GPU 完成离线 representation/world-model pilot，8×80GB GPU 用 7B worker adapters 进行多 agent SFT/RL 与 confirmatory rollout，预计 7–14 天。应保存每阶段 checkpoint、optimizer state、数据/容器 hash、随机种子、fork manifest、worker version、prompt/tool schema 与逐臂执行日志。算力估计只证明可实现，不是放行证据。

### 6.8 外部结果与统计

主要风险结果预注册为每 100 个联合任务的 hidden-contract violations、由 corrupt packet 因果引发的错误 state deltas、unsafe/incorrect patch reaching integration 和 secondary regression。任务结果包括 both-feature pass、partial score、salvaged work、重复修改和 rollback；成本结果包括 wall-clock、tokens、tool calls、tests、messages、forks 和 GPU-hours。

以 task-pair 为 cluster，报告 paired risk difference、relative risk、bootstrap 95% interval 与 Pareto hypervolume。模型×仓库×风险类型使用分层 mixed-effects 或 cluster-robust model；不以单次随机种子或 LLM judge preference 给显著性。应单列低互依负控制、能力×可靠性 2×2、correct/corrupt/sham first stage、knowledge-free workaround 与拒绝/总串行率。

## 7. Content-swap knowledge application 的识别上限

### 7.1 它比 message mention 强在哪里

同一 prefix 下只改变 packet 中的关键谓词方向，再观察 patch predicate 与 hidden executable outcome，可以检验共享知识是否内容特异地进入行动。一个 agent 即使在回复中引用 packet，只要其 patch 未体现相应 obligation，`A` 仍应标为 `none`。反之，patch 没有复述 packet，却在正确 API branch、边界条件或 serialization order 上产生与内容一致的变化，可标为 application。

行为标签至少同时满足三项。

1. packet treatment 对目标 action predicate 有 first-stage effect；
2. correct/corrupt 两臂在 source、格式、长度、语气、prefix 和工具状态上可交换；
3. action predicate 的变化连接到 independent hidden tests 或 state-delta oracle，而非 LLM 解释。

knowledge relocation 再固定内容、只改变 retainer，检验 query/routing 是否随 member-specific directory 变化；sham 与 format/source controls 排除一般服从、权威和格式偏好。

### 7.2 仍然不能识别什么

content swap 可识别一个局部 treatment 对行动的因果影响，却不直接识别自然团队中的长期 TMS 形成。packet 也可能改变计划、风险厌恶或注意分配，而非被 agent 作为“知识”内化。若 correct/corrupt 触发明显字面模板，模型可能用表面 cue；若任务存在 knowledge-free workaround，application label 失真；若 packet 本身泄露 hidden-test vocabulary，则发生训练污染。

因此需要 paraphrase、source/format swap、对抗性无关 packet、knowledge-free solver search 和 mediator intervention。即便这些都成功，所得新增能力仍是一个内容因果 world-model state；同标签 generic controller 可以使用它。这是识别可行但理论独占失败的典型情形。

## 8. 窄 C28：repo 义务级 knowledge-application program 的独立终审

### 8.1 先把 C28 与完整 TMS 候选分开

C28 固定专家身份、升级点、任务分解和任务分配。它不学习“谁知道什么”，不估计谁应负责哪个 subtask，也不主张形成完整 TMS。输入中直接给出 agent 来源、预定 owner、repo obligation、共享知识 packet、代码状态、依赖、权限和当前 trace。研究对象只有一个：怎样把来自异质 coding agents 的已共享知识转化为可执行 application program，同时阻止错误知识造成 hidden semantic regression。

其动作不是二元 accept/reject，也不是一条 verifier score。application program 至少可以依次执行：

```text
contractize(packet, obligation)
→ shadow_apply(branch, bounded_scope)
→ cross_verify(predicate, independent_world)
→ partial_integrate(validated_subgraph)
→ isolate(conflicting_or_uncertain_subgraph)
→ serialize(dependent_obligations)
→ rollback(reversible_prefix)
```

correct/corrupt/sham 内容置换识别 `A`，实际 hidden tests、state delta 与 secondary regression 评价程序是否把知识正确用于代码。这个冻结消除了 expert routing、TMS directory 与 task allocation 的干扰，也正面回应 `Experts Back` 的核心区分：知道谁是 expert 不等于有效利用其知识。

### 8.2 C28 的最强 I/O、损失与动作结果

输入为 `x=(repo_t, obligation_graph, fixed_owner, packet_content, packet_source, J_t, P_t, trace_t, budget_t)`。`fixed_owner` 与 escalation point 由环境给定，policy 不得改写。中间状态为 obligation-level `A_hat[u,k,c]`、shadow state-delta distribution、hidden-test risk、reversibility 和 cross-verification coverage。输出是可变长度 application program，而不是 member ranking。

训练样本从同起点 repo state fork。每个 packet 生成 correct/corrupt/sham、paraphrase、source-swap 和 format-swap；program executor 在隔离 branch 中实际 contractize、shadow apply、验证和局部合并。标签来自目标 obligation predicate、独立 hidden tests、cross-feature tests、state delta、rollback completeness 和成本。主损失可写为：

```text
L_C28 = L_A(content-specific application)
      + L_delta(shadow state transition)
      + L_contract(obligation coverage)
      + L_program(program imitation / offline RL)
      + L_harm(constrained outcome)
      + L_cost.
```

推断时，candidate 必须真正创建 contract artifact、隔离 branch、patch、verification evidence、partial integration commit 或 rollback state。只有在 hidden regression 下降且正确知识仍能被整合时才算安全改善。单纯扩大 shadow tests、全部 isolate 或全部 serialize 不合格。

### 8.3 Choi 的中介链是否足以产生独立机制

Choi 等的 `sharing→application→performance` 中介链为 C28 提供比完整 TMS 更直接的理论入口。它要求算法不能在 packet 被发送或复述时停止，而应显式建模 knowledge application，并将其连接到 executable performance。`Experts Back` 又说明 expert identity 已知后仍存在 utilization failure。因此，把专家身份外部固定并研究 application，不是一个逻辑错误。

然而，原理论没有给出 obligation graph、contractization、shadow branch、partial integration、cross-verification、serialization 或 rollback 的方向关系。它只规定 sharing 与 application 要区分，以及 application 更接近 performance。不同 program action 的选择实际由代码依赖 `J`、权限 `P`、可逆性、测试覆盖和 counterfactual state delta 决定。换言之，Choi 使 `A` 成为必要的测量/中介状态，却没有产生 program grammar、transition operator 或某两项动作之间的非交换顺序。

若 `A_hat` 只作为额外 prediction head，C28 明确触发本项目的辅助头否决门。若 `A_hat` 门控 program policy，动作会改变，但同信息、同 `A` 标签的 generic world-model controller 可以使用相同 gate；此时理论改变了研究者如何命名和检验 state，却没有改变可执行算法结构。只有理论能规定一个 generic controller 不会自然得到的更新或顺序，C28 才可能保留。全文没有这样的命题。

### 8.4 对旧 `00P` 的精确可约化证明

这不是“任何算法都能由 Transformer 表达”的万能逼近论证。定义旧 `00P` 的最强重构为 belief-state SMDP：

```text
M_P = <S_P, A_P, T_P, R_P>
S_P = {D, R, Q, K, J, P, packet, repo, trace, A_hat, Y_hat}
A_P = {probe, query, route, allocate, reassign, handoff,
       overlap_verify, integrate, isolate, serialize, discard, replay}
```

对 `M_P` 作以下可执行限制，而不是语义类比。

1. 令 `D=D_bar`、`R=R_bar`、`Q=Q_bar`、`K=K_bar`，这些常量由外部固定 owner、任务分配和升级点写入；关闭所有 directory/update/recruitment 动作。
2. 把 `packet/repo/J/P/trace/A_hat/Y_hat` 原样保留，训练仍使用旧案已规定的 correct/corrupt/sham、同前缀 paired rollout 与 post-action `A^obs`。
3. 将 `route` 固定到给定 owner，把 `overlap_verify` 具体化为 cross-verification；把 Shepherd 的 fork/replay 实例化为 `shadow_apply/rollback`，把 Claim Plane 的 intent/admission 实例化为 `contractize/partial_integrate/serialize`。
4. 保留旧 `world model→policy→post-action update` 的转移与 harm/cost reward，只将动作解码器改成上述 program grammar。

所得受限 SMDP `M_P|fixed(D,R,Q,K)` 与 C28 在观测、反事实标签、可执行状态转移、外部结果和动作序列上相同。C28 新增的三个动作名都能逐项还原为已有 substrate primitive：`contractize/partial_integrate/serialize` 来自 Claim Plane 的 typed intent/admission，`shadow_apply/rollback` 来自 Shepherd 的 fork/replay/discard，`cross_verify` 是旧 `overlap_verify` 的 obligation-level 实例。该约化不依赖训练结果，也不依赖“网络足够大”。它说明 C28 是旧 `00P` application 子 SMDP 的聚焦实现，而非不同研究对象。

聚焦一个子 SMDP 有时仍可成为独立论文，但本项目要求它拥有独立理论机制和新增算法能力。C28 的唯一新理论状态 `A` 已在旧 `00P` 中被定义、监督并用于 policy；其 program primitives 又来自直接 substrate。因而，聚焦并未达到独立贡献规模。

### 8.5 同输入—动作—结果近邻链

没有一篇近邻单独拥有 C28 全部输入与处理，但下面的链条在相同层级逐项占据其动作责任。

| C28 责任 | 同层直接近邻 | 相同点 | 剩余差异 |
|---|---|---|---|
| knowledge→真实 tool action | KATE | 输入 experiential knowledge，输出多步 tool execution；训练以执行结果内化知识 | 非 coding、无来源异质和 content swap |
| consolidated knowledge→executable artifact | SciCrafter | knowledge book、工程任务、实际建造与可执行结果，明确测 application gap | 非 repo integration；主要是诊断而非 learned program policy |
| trace→shadow branch/handoff/discard/rollback | Shepherd | 同 repo/tool trace，fork/replay 并执行真实 supervisor action，以 tests 衡量 | 无显式 `A` mediator 与 obligation knowledge treatment |
| obligation/dependency→contract/admit/serialize | Claim Plane | typed resource/dependency、program admission、partial scope promotion、serialize/fail-closed，以 pair pass 衡量 | deterministic control；不学习 knowledge application |
| expert 已知→仍未有效利用 | Experts Back | 固定或告知 expert identity 后，团队仍会稀释其知识 | 无 coding application program |
| sharing 与 application 分离 | Choi 等（2010） | application 比 sharing 更接近 performance | 团队问卷中介，不给程序动作与 executable label |

将 KATE/SciCrafter 的 knowledge-to-action、Shepherd 的 reversible shadow execution 与 Claim Plane 的 contract/integration primitives 接在同一 frozen repo prefix 上，已经得到 C28 的 program action skeleton。剩余的 correct/corrupt/sham `A` 是一项更严格的因果监督和 benchmark 设计，而非新的 program primitive。这条链本身不是“一篇组合基线等于直接覆盖”的偷换；致命证据来自上一节的旧案精确约化和本节每个 action 的同层实现共同成立。

### 8.6 C28 终判：不是仅凭 generic expressibility

C28 判定为 **终局 NO-GO**，不是 CONDITIONAL/RESULT-GATED。理由不是“generic model 理论上可能追平”，而是以下设计期等价已经成立。

- 若公平 generic baseline 获得相同 `A` 标签、obligation graph、shadow transitions 和 program actions，它与所谓 theory model 可以使用完全相同的 encoder、world model、program decoder、loss 和 policy；移除变量的理论名称后没有任何前向计算差异。
- 若不给 generic baseline `A` 标签，C28 的优势只能说明额外反事实监督有用，不能归因于 Choi 的理论结构；比较不公平。
- 若把 `A` 变成显式 gate，generic baseline 可使用同一 gate，因为 gate 的输入、标签、更新和动作后果均来自本研究数据，不来自理论独有运算。
- C28 的 program grammar由 repo dependency、reversibility 和已有 runtime/control-plane primitives产生。Choi 的理论只决定要检验 application，而未决定 contractize、shadow apply、partial integrate、verify、serialize 或 rollback 的顺序。

未来若能从另一 IS 理论取得 obligation-level program 的非交换顺序、结构化更新或有方向约束，并且该约束不能以同标签 generic program controller原样复现，可以将其作为全新候选重审。当前不能把“一项可能有价值的 content-swap benchmark 与显式 mediator”包装成第三篇 ISR 级算法论文。C28 因此也不计保留候选。

## 9. 等信息、等标签、等动作、等参数通用反证

### 9.1 公平比较矩阵

| 基线 | 同信息 | 同标签 | 同动作 | 同预算 | 要排除的替代解释 |
|---|---|---|---|---|---|
| raw temporal HGT | 全部 events、identity、repo graph、packet、tests | endpoint `Y` | 完整 action set | 参数/FLOPs/rollout matched | 结构化图本身即可 |
| equal-label temporal HGT | 再给 `D/R/G/Q/X/A` supervision | 与主模型完全相同 | 完整 action set | matched | 额外标签而非 TMS factorization |
| centralized shared-state HGT | 同上 | 同上 | 同上 | matched | private beliefs 无增益 |
| anonymous selective-alignment | 稳定 slot 但打乱语义身份，读取同一 task mask | 同上 | 同上 | matched | masked consistency 本身即可 |
| all-alignment / no-alignment | 同输入 | 同 endpoint 与 state labels | 同上 | matched | 选择性 overlap 的必要性 |
| Dec-POMDP/CMDP world model | 成员局部 observation 与共享事件 | 同 counterfactual labels | 同低层动作 | matched | 通用 belief-state policy 即可 |
| CoThinker | 同 backbone、轮数、token、memory slots | endpoint | query/communication/integration 可对齐部分 | matched | TMS prompt memory/context compression |
| ETI + AgentAsk + NeuralFSM | 同 history、profile、edge state | endpoint 与可给中间 labels | query/reassign/verify/route | matched | trait inference、asking 与 learned transition 组合 |
| Shepherd + Claim Plane | 同 trace、fork、dependency、continuation | tests/state delta | handoff/discard/replay/admit/serialize | matched | runtime/control substrate 产生收益 |

比较必须报告参数量、激活 FLOPs、tokens、tool calls、tests、forks、wall-clock、训练 rollouts 和 action availability。不能给主模型 oracle `G/Q/K/A`，却只给 baseline 原始文本；也不能让主模型 shadow apply 三个分支而 baseline 只有一次 continuation。

### 9.2 逐项复制证明

- `member-specific D/R` 可由 HGT 的 `(observer_i, target_a, knowledge_k)` typed edge state表示；稳定 identity 只是 node key，不是 TMS 专用运算。
- `selective overlap` 可由 generic model 读取同一 `M_task` 后计算相同 masked consistency。anonymous baseline 甚至可以保留 private slots，只删除“谁知道什么”的语义名称。
- `K[u,v,a,k,r]` 可由 task、knowledge、agent typed hyperedge 表示；主模型的因子化提高可读性，却没有新增 action support。
- content-swap `A` 可作为 generic counterfactual world-model 的 mediator，并以同一 contrastive loss训练。
- integration/isolation/serialize/rollback 是 action decoder 的离散 tokens；generic actor 接收同一 transition labels 后可以学习相同非线性政策。
- `D/R/K/A` 的干预响应若由 supervised labels 与 action reward决定，equal-label generic model 能收到同一 intervention distribution。理论模型没有额外观测，也没有不同环境转移。

这不是抽象的 universal approximation。主模型与 equal-label generic baseline 可以共享逐行相同的 tensor shapes、attention blocks、world model、action decoder 和损失，只把命名为 `D/R/K/A` 的 heads 改成匿名 typed states。若连前向代码都相同，理论 factorization 不可能作为独立算法贡献。它最多带来解释、诊断或样本效率假设；本项目不接受仅靠可解释名称或辅助头占一篇论文。

### 9.3 必须执行但不会改变当前终判的消融

若未来仍做验证性 pilot，应执行：成员身份 permutation；belief relocation；能力×可靠性 2×2；task interdependence removal；correct/corrupt/sham；source/format/paraphrase controls；application mediator neutralization；`K` shuffle；selective mask shuffle；all/no alignment；no `A`、no `D`、no `R`、no `K`；固定/移除 `J/P`；禁用 total serialization；matched communication/tool/fork budgets；new repo/model/team OOD。

这些实验可以确认机制测量是否有效，却不会自动恢复独立论文。恢复条件是出现一个现有构念或技术近邻未覆盖、且匿名等标签模型不能原样实现的新增计算责任。当前设计中不存在这一责任。

## 10. Coding-agent deletion test 与系列边界

### 10.1 deletion test

删除 coding agent 后，把 repo obligation 换成数据管道部署、科研仪器步骤或多工具业务流程，把 patch/hidden tests 换成 executable artifact/state constraints。成员专长 belief、条件可靠性、task–knowledge coordination、content-swap application、partial handoff、integration/isolation/serialize/rollback 全部保留。`D/R/K/A` 的数学对象、selective-overlap loss 和 policy action structure 不需要变化。

coding 环境提供三项重要但非独占的优势：代码 diff 使 application predicate 可观察，tests 使 external harm 可执行，Git/fork 使 counterfactual 和 rollback 可复现。这些是识别环境优势，不是机制独特性。因此删除测试失败。若论文的新增能力只剩“在代码上更容易量化一般团队知识应用”，它可以成为 benchmark 或测量论文，却不满足当前系列对 coding-agent 独立算法能力的要求。

### 10.2 与现有候选和近邻的边界

- 与 C3 的 post-escalation 真人证据不同：本候选研究 machine-agent team 内部知识协调，不研究人在升级后如何审查证据。加入 reviewer 会引入新的 human oversight 分析单位，不能用于补足本候选理论。
- 与 Claim Plane/并发控制不同：`J`、scope、intent admission 和 serialize 的技术责任属于 concurrency substrate；TMS 只能解释成员如何定位、信任和协调知识。若收益在固定 `D/R/K/A` 后仍存在，应归 Claim Plane。
- 与 Shepherd/runtime recovery 不同：fork/replay、handoff、discard 和 rollback 是执行底座。若去掉 TMS/application state 后 meta-agent仍以 trace 做出同样动作，候选没有新增机制。
- 与 memory 固化候选不同：这里的 belief 随团队互动更新，但没有把审查纠正写入跨会话规则库，也不研究 memory poisoning、scope、forgetting 或 unlearning。
- 与平台迁移和 API 演化候选不同：这里的 knowledge packet只影响当前 repo obligation；不生成 provider change、compatibility shim 或面向大量下游 clients 的边界资源。
- 与开放源码维护者注意力候选不同：这里没有 maintainer queue、review minutes、follow-up escrow 或 newcomer access；PR review burden 不能作为主要结果。

边界可以避免重复，却不能创造贡献。最直接的内部重复仍是 `00P`；外部最强 TMS baseline 是 CoThinker，最强通用 learned controller 是 NeuralFSM/TeamTR，最强 coding action substrate 是 Shepherd/Claim Plane。

## 11. 撤题门与终局判定

### 11.1 已触发的终止条件

| 撤题门 | 证据 | 是否触发 |
|---|---|---|
| 新候选与旧案研究对象、状态、反事实标签和动作同构 | 第 4 节逐项对照；第 8.4 节固定 `D/R/Q/K` 的子 SMDP 约化 | 是 |
| 一般 TMS→machine-agent architecture 已有直接工作 | HCM 与 CoThinker 全文 | 是 |
| 最窄剩余只是 application head/label | Choi 只规定 sharing/application 区分；同标签 generic 可使用相同 `A` gate | 是 |
| theory-specific forward/operator 缺失 | selective overlap、program grammar 与 state transitions 均来自任务标签或技术 substrate | 是 |
| equal-label generic 与主模型代码同构 | 第 9.2 节逐项 tensor/action 复制 | 是 |
| coding-agent deletion failure | 第 10.1 节一般 tool-agent 替换保持机制不变 | 是 |
| 数据不可构造或结果尚未运行 | two-world、paired fork 与 stable-team sequence 可严谨自建 | 否，不作为撤题理由 |
| 只能靠拒绝/总串行降低风险 | 设计已排除，但 Claim Plane 显示这是必须控制的实证风险 | 未触发，需未来控制 |

### 11.2 为什么不是 CONDITIONAL 或 RESULT-GATED

结果门适用于“理论产生了与 generic 不同的结构，但尚不知道是否有经验优势”。本候选没有这种结构差。主模型和 equal-label generic model 可以逐行共享 encoder、HGT、application world model、masked consistency、actor、action grammar 与全部标签；只改变中间 state 的理论名称。C28 更能被固定旧状态后的子 SMDP 精确还原。即便未来主模型在某次训练中领先，也需先排除初始化、标签访问、预算和优化差异；领先本身不能把同构代码变成理论专用算法。

因此，未运行结果不是撤题依据，设计期同构才是。`CONDITIONAL` 会把一个可识别的 benchmark/机制实验误当作已有独立 thesis 空位。

### 11.3 终局结论

完整 TMS 候选和窄 C28 均判 **终局 NO-GO**。保留候选数为 0。问题、环境和 causal application 测量都值得保留为未来诊断资产，但不得占用第三篇论文题位，不得以“专家知识利用”“application program”或“选择性知识协调”换名返回。

撤题不否定三项可复用成果：CooperBench/TeamBench 可支持稳定团队和权限边界扩展；correct/corrupt/sham 可以成为团队知识应用 benchmark；selective all/no alignment 与 identity relocation 可以成为多 agent coordination 的机制实验。它们目前适合作共享基础设施、附加评价或未来新理论的识别组件，不足以单独构成 ISR 级理论算法论文。

## 12. 肖帅勇 ISR 逐句功能责任账

本节审计本报告的关键候选句，不把内部终审伪装成正式论文。每张卡使用 `00W` 的源语法句主键。`SRC_NEW` 只释义源句承担的学术功能，不复写源句；`CAND_NEW` 是本报告实际承担相应责任的句子。若只是位置相似，`REL` 明写“位置参照，非功能同位”。`RESULT` 只使用保留、改写、拆分、合并、删除五种法定动作。

### 卡 K-01：建立可执行协作情境

- `source_anchor = DSDL-I1 / DSDL-I1-S01`
- `source_function_code = CXT`
- `candidate_function_code = CXT`
- `PRE`：读者尚不知道多 coding-agent 协作发生在何种日常软件行动中。
- `SRC_NEW`：源句先用可识别的实时互动实例建立研究情境，而未先抛出模型名称。
- `CAND_NEW`：两个 coding agents 可以各自完成局部正确的 feature，却在同一仓库的共享 obligation 上形成不兼容修改。
- `REL`：功能同位；均先建立可观察情境，研究对象不同。
- `CIT`：CooperBench 的任务定义、真实仓库与联合测试承担该句。
- `NEXT`：下一句把协调失败连接到 hidden regression 和组织损害。
- `RESULT`：保留

### 卡 K-02：把行动错误连接到外部后果

- `source_anchor = DSDL-I3 / DSDL-I3-S01, DSDL-I3-S05`
- `source_function_code = IMP`
- `candidate_function_code = IMP`
- `PRE`：前句已经说明局部 patch 可相互不兼容。
- `SRC_NEW`：源段先说明预测为何决定运营成败，再说明预测怎样改变资源行动和结果。
- `CAND_NEW`：误用异质成员提供的知识会让联合 hidden tests 失败、语义回归进入 integration，并增加返工和 rollback。
- `REL`：功能同位；都把技术任务连到可执行行动和外部结果。
- `CIT`：CooperBench、Shepherd 与 Claim Plane 的可执行代码结果；具体因果效应仍由拟议实验负责。
- `NEXT`：下一句界定算法介入时点，而不是提前介绍 TMS。
- `RESULT`：保留

### 卡 K-03：承认最直接既有工作

- `source_anchor = ACAA-I4 / ACAA-I4-S01`
- `source_function_code = ACK`
- `candidate_function_code = ACK`
- `PRE`：问题重要性已经建立，接下来不能假设没有现有解决方案。
- `SRC_NEW`：源句并列界定三条传统研究路径，先承认共识再寻找边界。
- `CAND_NEW`：CoThinker 已把 TMS directory、collective memory 和 communication moderation 放入多 agent architecture，HCM 更早已将 SMM 与 TMS 用于 machine-agent teams。
- `REL`：功能同位；均主动承认最强理论/算法近邻。
- `CIT`：CoThinker TMLR 正式全文与 HCM DOI 全文。
- `NEXT`：后句只讨论 member-specific belief、TKC 与 causal application 的剩余差异。
- `RESULT`：改写

### 卡 K-04：用冲突证据而非空泛缺口

- `source_anchor = ACAA-I4 / ACAA-I4-S04, ACAA-I4-S06`
- `source_function_code = MEC+CON`
- `candidate_function_code = MEC+CON`
- `PRE`：前句已承认 TMS architecture 直接工作。
- `SRC_NEW`：源段以偏好异质和相反经验效应削弱朴素 helpfulness 指标的稳定性。
- `CAND_NEW`：专家身份已知仍可能发生 integrative compromise，而盲从 expert 又会牺牲面对错误成员的鲁棒性。
- `REL`：功能同位；用方向冲突而非“无人研究”导出机制需要。
- `CIT`：Multi-Agent Teams Hold Experts Back 的 expert-leveraging 与 robustness 分析。
- `NEXT`：下一句引入 ability、conditional reliability 与 application 的分离。
- `RESULT`：保留

### 卡 K-05：理论建立有方向中间状态

- `source_anchor = DSDL-I6 / DSDL-I6-S04, DSDL-I6-S05`
- `source_function_code = DEF+MEC`
- `candidate_function_code = MAP+MEC`
- `PRE`：现象冲突已说明一个 skill score 不足。
- `SRC_NEW`：源句引入两项理论状态，并以有方向关系定义中间机制及其结果含义。
- `CAND_NEW`：TMS 要求区分成员关于专长位置的 belief、基于能力与兑现的认知信任，以及把这些状态经 task–knowledge coordination 连接到共同任务。
- `REL`：部分功能同位；源文有明确差运算，本候选只有结构链，没有同等强度的唯一算子。
- `CIT`：Kanawattanachai 与 Yoo（2007）全文的三维 TMS 模型和中介路径。
- `NEXT`：后句必须诚实说明 `R`、`Q/J/P` 与 `A` 哪些是研究新增技术状态。
- `RESULT`：拆分

### 卡 K-06：区分 theory state 与 technical state

- `source_anchor = DSDL-I9 / DSDL-I9-S01–S05`
- `source_function_code = LIM+MEC`
- `candidate_function_code = MAP+BND`
- `PRE`：上一句已建立 TMS 的三项理论责任。
- `SRC_NEW`：源段并置理论路径与数据路径，逐一说明各自不能独立承担的责任。
- `CAND_NEW`：`D` 与 `K` 可对应 expertise location 和 TKC，`R` 是为条件辨别新增，`Q/J/P` 属于任务世界，`A` 则是 TMS 下游的 knowledge application。
- `REL`：功能同位；均通过责任分工防止把全部模型状态归给理论。
- `CIT`：Kanawattanachai 与 Yoo（2007）、Choi 等（2010）以及本审计的构念表。
- `NEXT`：下一句把 sharing/application 区分转成 content-swap 测量。
- `RESULT`：保留

### 卡 K-07：由不可观察性导出反事实测量

- `source_anchor = DSDL-I9 / DSDL-I9-S03`
- `source_function_code = LIM`
- `candidate_function_code = LIM+MAP`
- `PRE`：application 已被定位为下游状态，但自然轨迹不能观察知识是否造成行动。
- `SRC_NEW`：源句指出理论中间状态没有真值标签，因而不能直接优化。
- `CAND_NEW`：消息被发送或复述不能标记 application；需要 correct/corrupt/sham 同前缀置换与 executable state delta 才能构造 `A^obs`。
- `REL`：功能同位；都从标签不可得推进到专门测量，但候选额外加入因果干预。
- `CIT`：Choi 等（2010）的 sharing/application 区分；paired intervention 的有效性由拟议实验承担。
- `NEXT`：后句给出同来源、同格式、同长度与 hidden-test 隔离条件。
- `RESULT`：改写

### 卡 K-08：将理论状态落实为前向表示

- `source_anchor = DSDL-I7 / DSDL-I7-S06–S08`
- `source_function_code = ALG+MAP`
- `candidate_function_code = ALG+MAP`
- `PRE`：反事实标签已经建立，但尚未进入模型。
- `SRC_NEW`：源段把不可见偏好转成可计算模板，再展开为时序矩阵并解释元素语义。
- `CAND_NEW`：成员专属 `D_t^(i)`、条件 `R_t^(i)` 与因子化 `K_t^(i)[u,v,a,k,r]` 保留 belief owner、任务关系、知识域和责任人，不池化成团队向量。
- `REL`：功能同位；均要求中间张量具有可核查元素语义。
- `CIT`：Kanawattanachai 与 Yoo（2007）负责构念；张量形式由本研究负责。
- `NEXT`：下一句说明只对 task relations 施加 overlap。
- `RESULT`：保留

### 卡 K-09：把方向冲突变成 selective-overlap

- `source_anchor = ACAA-I7 / ACAA-I7-S02–S06`
- `source_function_code = MEC+MAP`
- `candidate_function_code = MAP+ALG`
- `PRE`：上一句已给出成员专属状态和共同任务状态。
- `SRC_NEW`：源段逐一把不同注意机制映射到不同粒度，而非用一个通用权重替代全部状态。
- `CAND_NEW`：算法只对 task decomposition、subtask relation 和 assignment projection 施加跨成员一致性，同时保留 holder-specific expertise 与 reliability evidence。
- `REL`：部分功能同位；都是机制分责到不同粒度，具体 overlap 运算是候选新增。
- `CIT`：Kanawattanachai 与 Yoo（2007）的 specialization 与 TKC；算法公式由本研究负责。
- `NEXT`：后句必须设置 all-alignment、no-alignment 和 anonymous selective-alignment 基线。
- `RESULT`：保留

### 卡 K-10：工件必须输出真实动作

- `source_anchor = ACAA-I8 / ACAA-I8-S03, ACAA-I8-S04`
- `source_function_code = ALG`
- `candidate_function_code = ALG`
- `PRE`：中间状态已经定义，尚未说明工件改变什么行动。
- `SRC_NEW`：源句先命名完整工件，再将构件逐项对应前文机制。
- `CAND_NEW`：temporal HGT、application world model 与 actor 共同输出 probe、query、route、reassign、partial handoff、verify、integrate、isolate、serialize 和 rollback，并由 coding agents 执行真实工具动作。
- `REL`：功能同位；都把机制逐项落实为工件，但候选动作是序贯控制而非预测。
- `CIT`：本研究规格；Shepherd、Claim Plane、AgentAsk 与 NeuralFSM 只承担动作近邻责任。
- `NEXT`：下一段交代训练样本、标签和 checkpoint。
- `RESULT`：保留

### 卡 K-11：训练数据按来源和时点分责

- `source_anchor = DSDL-M2 / DSDL-M2-S01–S08`
- `source_function_code = EVAL+ALG`
- `candidate_function_code = EVAL+ALG`
- `PRE`：工件身份和动作已建立，需要说明每种监督从哪里来。
- `SRC_NEW`：源段依次说明数据来源、样本筛选、分段和模型可用输入。
- `CAND_NEW`：belief、coordination 与 application 三层数据分别来自历史 probes、gold/审计后的 obligation relations 和同起点 executable content-swap rollouts。
- `REL`：位置与功能均可参照；具体数据对象完全不同。
- `CIT`：CooperBench、TeamBench 和自建 two-world manifest；所有未生成规模均写成设计值。
- `NEXT`：后句逐项说明 split、hidden-test 隔离和 sibling grouping。
- `RESULT`：拆分

### 卡 K-12：最强基线不作稻草人

- `source_anchor = DSDL-E3 / DSDL-E3-S01–S07`
- `source_function_code = EVAL+ACK`
- `candidate_function_code = EVAL+ACK`
- `PRE`：训练设计已经给出，接下来需要证明新增能力而非额外预算。
- `SRC_NEW`：源段按任务与方法类型组织比较对象，并说明公平评价接口。
- `CAND_NEW`：基线同时包含 CoThinker、ETI、AgentAsk、NeuralFSM、SkillGraph、Shepherd、Claim Plane、TeamTR，以及等信息等标签等参数 temporal HGT/Dec-POMDP。
- `REL`：功能同位；都用分层强基线限制贡献强度。
- `CIT`：各正式全文与 arXiv 一手全文。
- `NEXT`：后句锁定 tokens、FLOPs、tools、forks 和 action availability。
- `RESULT`：保留

### 卡 K-13：机制干预而非端点消融

- `source_anchor = DSDL-E13 / DSDL-E13-S01–S03; DSDL-E14b / DSDL-E14b-S01–S04`
- `source_function_code = EVAL+MEC`
- `candidate_function_code = EVAL+MEC`
- `PRE`：强基线只能比较端点，尚不能证明理论状态承担动作责任。
- `SRC_NEW`：源段用消融与中间状态评价检验专门组件的贡献。
- `CAND_NEW`：identity relocation、能力×可靠性 2×2、`K`/mask shuffle、application neutralization 和低互依负控制分别检验 `D/R/K/A` 对动作的责任。
- `REL`：功能同位；候选把普通消融扩展成状态干预。
- `CIT`：TMS 全文规定构念与边界；干预操作由本研究负责。
- `NEXT`：下一句说明 equal-label generic 若响应相同则撤销理论算法贡献。
- `RESULT`：保留

### 卡 K-14：未运行结果不得预告为事实

- `source_anchor = DSDL-I10 / DSDL-I10-S03; ACAA-I9 / ACAA-I9-S06`
- `source_function_code = RES`
- `candidate_function_code = BND`
- `PRE`：源文在对应位置可预告已完成结果，本审计没有运行候选实验。
- `SRC_NEW`：源句预告真实数据上的主性能和机制证据。
- `CAND_NEW`：本文件不写候选性能、显著性或机制结果，所有数字仅为已出版近邻结果或未来设计规模。
- `REL`：位置参照，非功能同位；候选主动删除结果预告功能。
- `CIT`：无外部引用；这是证据边界声明。
- `NEXT`：直接进入可复制性和撤题门，不写“结果表明”。
- `RESULT`：删除

### 卡 K-15：窄 C28 不能靠换名重开

- `source_anchor = ACAA-I2 / ACAA-I2-S03–S06`
- `source_function_code = ACK+LIM`
- `candidate_function_code = LIM+BND`
- `PRE`：完整 TMS 候选已终止，但仍需审查固定专家与分配的窄题。
- `SRC_NEW`：源段承认既有预测研究，再用数据与模型处理边界逐步限定缺口。
- `CAND_NEW`：固定 `D/R/Q/K` 后，C28 的 packet、repo、`A`、world model 和 program actions可逐项还原为旧 `00P` 的 application 子 SMDP。
- `REL`：部分功能同位；候选用精确约化而非一般文献边界终止。
- `CIT`：`00P` 内部规格、Shepherd 和 Claim Plane 的动作原语。
- `NEXT`：下一句检验 Choi 中介链是否产生 program grammar。
- `RESULT`：合并

### 卡 K-16：理论支持强度不超过原证据

- `source_anchor = ACAA-L2 / ACAA-L2-S01–S04`
- `source_function_code = ACK+CON`
- `candidate_function_code = BND+LIM`
- `PRE`：C28 使用 sharing/application 中介，需要防止从问卷结果越级到算法顺序。
- `SRC_NEW`：源段用相反经验发现限制朴素指标的普适解释。
- `CAND_NEW`：Choi 等的横截面团队问卷支持 sharing 与 application 区分及其中介关系，却不提供 obligation-level causal label、动态更新或 contractize→shadow apply 的动作顺序。
- `REL`：功能同位；都用原证据边界限制论断强度。
- `CIT`：Choi 等（2010）全文的模型、测量、PLS 结果与局限。
- `NEXT`：后句说明 C28 的 program grammar 属于技术 substrate。
- `RESULT`：保留

### 卡 K-17：equal generic 反证

- `source_anchor = ACAA-L9 / ACAA-L9-S01–S04`
- `source_function_code = MEC+BND`
- `candidate_function_code = BND+LIM`
- `PRE`：理论状态和技术工件已经建立，必须检验同名映射是否真实。
- `SRC_NEW`：源段明确行为 attention 与 neural attention 不同，前者只提供设计动机，避免同名制造等价。
- `CAND_NEW`：给 generic HGT 相同 `D/R/K/A` 标签、task mask 和 program actions 后，其 forward 与主模型可逐行同构；理论名称不产生额外计算。
- `REL`：功能同位；均拆开理论概念与通用计算对象。
- `CIT`：本审计的 matched architecture 证明；不需要用某篇文献替代代码责任。
- `NEXT`：下一句据此撤销独立理论算法贡献。
- `RESULT`：保留

### 卡 K-18：局限与终局边界

- `source_anchor = DSDL-Z3_6 / DSDL-Z3_6-S01–S11`
- `source_function_code = LIM+BND`
- `candidate_function_code = BND+CONB`
- `PRE`：所有理论、数据、算法和替代模型责任已经审查。
- `SRC_NEW`：源段将不同局限分别绑定到数据、表示、机制和外部效度，而不以一条泛化免责声明收束。
- `CAND_NEW`：候选可运行且测量有价值，但旧案同构、TMS architecture 直接覆盖、等标签前向同构和 coding-agent deletion failure 同时触发，所以保留数为零。
- `REL`：部分功能同位；源文报告研究局限，候选报告内部终审判定。
- `CIT`：本文件第 4、8、9、10 节；结论不借单一外部引文代替反证。
- `NEXT`：进入引用核验表和机械检查，不再引入新主张。
- `RESULT`：保留

## 13. 引用核验表

| 文献 | 元数据核验 | 本文件中支持的具体责任 | 原文证据边界 | 状态 |
|---|---|---|---|---|
| Kanawattanachai, P., & Yoo, Y. (2007). *The Impact of Knowledge Coordination on Virtual Team Performance over Time*. MISQ 31(4), 783–808. DOI [10.2307/25148820](https://doi.org/10.2307/25148820) | 本地 Otero front matter、全文与 JSTOR stable id 一致 | 三维 TMS、38 teams/146 members/8 weeks、EL/CBT→TKC→performance、时间边界 | 学生商业模拟和 Likert/PLS；不承担 agent 张量、因果标签或更新律 | 已全文核验 |
| Choi, S. Y., Lee, H., & Yoo, Y. (2010). *The Impact of Information Technology and Transactive Memory Systems on Knowledge Sharing, Application, and Team Performance*. MISQ. DOI [10.2307/25750708](https://doi.org/10.2307/25750708) | 本地 Otero front matter 与全文 | 139 teams/743 members；sharing/application 区分；application 连接 performance；sharing 直接路径不成立且完全中介 | 横截面团队问卷与 PLS；不承担 action-level causal `A` 或 program grammar | 已全文核验 |
| Lapso, J. A., Peterson, G. L., & Miller, M. E. (2023). *A Hybrid Cognitive Model for Machine Agents*. Cognitive Systems Research 81, 1–10. DOI [10.1016/j.cogsys.2023.02.007](https://doi.org/10.1016/j.cogsys.2023.02.007) | 出版商页面与正文 | SMM+TMS machine-agent architecture、knowledge holder/credibility、project/action team | 非 LLM coding、非反事实训练 policy | 已全文核验 |
| Shang et al. (2026). *United Minds or Isolated Agents?* TMLR, OpenReview [8BYJHZiZ5T](https://openreview.net/forum?id=8BYJHZiZ5T) | TMLR accepted page、正式全文与附录 | CoThinker specialization、TMS collective memory、expertise directory、Update/Retrieve、moderator、small-world、synthesizer | 主要是 CLT/context compression；无 member-specific TKC/application | 已全文核验 |
| Khatua et al. (2026). *CooperBench: Why Coding Agents Cannot be Your Teammates Yet*. [arXiv:2601.13295](https://arxiv.org/abs/2601.13295) | arXiv 全文、项目页、附录 | 652 pairs、12 libraries、4 languages、联合测试与 coordination gap | 非稳定重复团队；无 TMS state labels | 已全文核验 |
| Pappu et al. (2026). *Multi-Agent Teams Hold Experts Back*. [arXiv:2602.01011](https://arxiv.org/abs/2602.01011) | arXiv/OpenReview 全文 | expert identity 已知仍被稀释、integrative compromise、规模与 robustness trade-off | 非 coding、非 learned controller | 已全文核验 |
| Nie et al. (2026). *SkillGraph*. [arXiv:2604.17503](https://arxiv.org/abs/2604.17503) | arXiv HTML/PDF | multimodal graph、skill bank、failure buffer、query-conditioned topology update | 视觉 benchmarks；不识别 belief/application | 已全文核验 |
| Yu et al. (2026). *Shepherd*. [arXiv:2605.10913](https://arxiv.org/abs/2605.10913) | arXiv 全文 | typed trace、fork/replay、inject/handoff/discard、CooperBench runtime action | substrate 不是 TMS；meta-agent 主体为 prompt-based | 已全文核验 |
| Nikolaev (2026). *Claim Plane: Enforceable Change Intents and Dynamic Scope for Parallel Coding Agents*. [arXiv:2607.21909](https://arxiv.org/abs/2607.21909) | arXiv 全文 | typed intent/dependency、admission、promotion、serialize/fail-closed | 初步六对只作可行性；不承担 learned semantic policy | 已全文核验 |
| Nikolaev (2026). *Claim Plane: Reliability Gains and the Limits of Selective Concurrency...*. [arXiv:2608.00947](https://arxiv.org/abs/2608.00947) | arXiv 全文 | 30 pairs×3 seeds、静态/动态策略、总串行与 undeclared scope 边界 | 原作者结果；不证明本候选 | 已全文核验 |
| Zhou et al. (2025). *SWEET-RL*. [arXiv:2503.15478](https://arxiv.org/abs/2503.15478) | arXiv 全文 | ColBench、step-wise critic、训练时额外信息、多轮信用分配 | 人—agent 设置；非 TMS | 已全文核验 |
| Abdurahman et al. (2026). *Explicit Trait Inference for Multi-Agent Coordination*. ACL. DOI [10.18653/v1/2026.acl-long.77](https://doi.org/10.18653/v1/2026.acl-long.77) | ACL Anthology 正式元数据与 PDF | 历史→warmth/competence profile→allocation/verification | inference-time profile；不提供内容级 application | 已全文核验 |
| Lin et al. (2026). *AgentAsk*. ACL. DOI [10.18653/v1/2026.acl-long.1294](https://doi.org/10.18653/v1/2026.acl-long.1294) | ACL Anthology 正式元数据与 PDF | whether/what/whom/how to ask；SFT/E-GRPO；成本权衡 | edge clarification，不是完整 knowledge coordination | 已全文核验 |
| Wang et al. (2026). *NeuralFSM*. ACL. DOI [10.18653/v1/2026.acl-long.1543](https://doi.org/10.18653/v1/2026.acl-long.1543) | ACL Anthology 正式元数据与 PDF | learned transition/routing、graph protection、trust attenuation | generic coordination；trust 不等于 TMS CBT | 已全文核验 |
| Zhang et al. (2026). *AgentRouter*. ACL. DOI [10.18653/v1/2026.acl-long.33](https://doi.org/10.18653/v1/2026.acl-long.33) | ACL Anthology/DBLP 正式元数据与 PDF | heterogeneous GNN、empirical soft labels、routing distribution | QA；跨任务 transfer 有边界 | 已全文核验 |
| Ko et al. (2026). *Social Dynamics as Critical Vulnerabilities...*. ACL. DOI [10.18653/v1/2026.acl-long.1756](https://doi.org/10.18653/v1/2026.acl-long.1756) | ACL Anthology 正式元数据与 26 页 PDF | peer 数、relative intelligence、argument length、rhetoric 对代表 agent 的影响 | adversarial persuasion；不等于良性 `R` | 已全文核验 |
| Li, Naito, & Shirado (2025/2026). *HiddenBench*. [arXiv:2505.11556](https://arxiv.org/abs/2505.11556) | arXiv/OpenReview 全文 | 65 hidden-profile tasks 与分布式信息整合 | 非 executable coding artifact | 已全文核验；出版状态按 arXiv 处理 |
| Bao et al. (2025). *EMRC*. [arXiv:2508.13754](https://arxiv.org/abs/2508.13754) | arXiv 全文 | expertise table、dynamic recruitment、confidence fusion/adversarial validation | 医疗 QA；self-confidence 非真实 reliability | 已全文核验 |
| Kim et al. (2026). *TeamBench*. [arXiv:2605.07073](https://arxiv.org/abs/2605.07073) | arXiv 全文与项目页 | OS-enforced role separation、851 templates/931 instances、deterministic grading | 固定 roles；非长期 TMS | 已全文核验 |
| Xie et al. (2026). *TeamTR*. [arXiv:2605.15207](https://arxiv.org/abs/2605.15207) | arXiv v2 全文，页面标注 ICML 2026 accepted | occupancy shift、逐组件 resampling、KL trust region | 训练稳定，不产生理论状态 | 已全文核验 |
| Xu et al. (2025). *Collaborative Expertise Delegation*. [arXiv:2505.07313](https://arxiv.org/abs/2505.07313) | arXiv 全文 | expertise-domain alignment、workflow/diversity、scale trade-off | 探索性设计；无 coding harm | 已全文核验 |
| Zhou et al. (2026). *SciCrafter*. [arXiv:2604.24697](https://arxiv.org/abs/2604.24697) | ICLR/OpenReview 全文与项目页 | gap identification/discovery/consolidation/application 分解和 executable build | application 作为残余 gap；非团队 source-specific state | 已全文核验 |
| Hao et al. (2026). *KATE*. Findings ACL. DOI [10.18653/v1/2026.findings-acl.710](https://doi.org/10.18653/v1/2026.findings-acl.710) | ACL Anthology 正式元数据与 PDF | acquisition/activation/internalization、knowledge-aware RL、tool execution | 单 agent；不含 TKC | 已全文核验 |

引用责任按分句分配。理论来源不承担拟议张量、损失、action policy、算力或效果；技术近邻不承担 IS 构念；本报告的同构约化和终局判定由本文件逻辑负责。没有取得全文的来源不参与关键命题，也没有用貌似完整的参考文献填补待引文位置。

## 14. 终稿机械核验口径

- 逐句功能卡共 18 张；每张均有 source anchor、source/candidate function code 和 `PRE→SRC_NEW/CAND_NEW→REL→CIT→NEXT→RESULT` 全链。
- `RESULT` 只出现保留、改写、拆分、合并、删除五种动作；位置类比和非功能同位均已显式标注。
- Markdown 表格逐表校验列数；没有不齐行。文件以 UTF-8 读取和 round-trip，无解码错误。
- 候选实验没有性能、效应量或显著性结果。文中数字均标明来自已运行的一手近邻或属于未来设计/算力范围。
- 关键文献均给出 DOI、arXiv、ACL Anthology 或 OpenReview 一手链接；未取得全文的来源不承担关键命题。
- 本 agent 的写权限只用于新建和编辑本文件；没有改写 `00P`、理论全文、肖老师全文、`00F`、`00W` 或任何其他候选文件。
