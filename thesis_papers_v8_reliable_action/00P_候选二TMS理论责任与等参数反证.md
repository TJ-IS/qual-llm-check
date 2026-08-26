# 候选二 TMS 理论责任与等参数反证

## 1. 红队结论

本文件只审查候选二，即异质且能力会漂移的 coding-agent 团队如何学习知识协调与 handoff policy。审查对象不是题目的社会重要性，而是它能否证明 TMS 理论对算法产生了不可替代的计算责任。

**论文候选判定：NO-GO，无保留。** 现有 `D/C/Q/A/J/P→Z→policy` 设计不能冻结为论文，也不应在当前三篇论文系列中占位。主要原因有五点。第一，团队全局的 `D[a,k]` 容易退化为中央调度器的能力表，不能体现团队成员关于“谁知道什么”的分布式 meta-memory。第二，`C` 混合了能力、事实声明准确性、承诺兑现和执行机会，尚未与 `D` 建立辨别效度。第三，`Q`、`J` 和 `P` 是任务世界、软件依赖和行动可行性的技术状态，不是 TMS 构念。第四，`A` 是行动后才能观察的知识应用结果；若把同一时点的 actual `A` 放进决策瓶颈，就发生结果泄漏。第五，当前 `Z` 没有显式表示 Kanawattanachai and Yoo (2007) 所说的 task–knowledge coordination，即任务怎样分解、子任务怎样关联，以及知识应当由谁用于哪一部分工作。

下文给出的重构不是对当前候选的条件性保留，而是未来若要以一个新候选重新立项时必须重新通过的入口：形成稳定身份、重复互动且高度相互依赖的异质 agent 团队；把 member-specific expertise-location beliefs 或团队可访问的 meta-memory directory 变成真正的中间状态；将能力与条件可靠性分开识别；新增显式 task–knowledge coordination 张量；actual application 只在行动后监督状态更新；allocation、targeted query、knowledge retrieval 和 handoff 的选择必须经由这些状态改变。即便完成重构，等参数 graph Transformer、SkillGraph 式动态图、generic belief-state POMDP、Shepherd supervisor 或 Claim Plane+history 若能复制风险—成功—成本前沿及机制干预行为，新候选仍应撤题。

这里的判定故意严于“模型有效”。TMS 可以帮助解释团队表现，并不自动构成一个独立的理论驱动算法。按照肖帅勇老师 ACAA 与 DSDL 的论证标准，理论必须先指出通用计算会系统性处理错误的机制，再产生具有明确元素语义的中间张量、方向性计算或约束，最后改变真实动作；端点提升、理论命名或可解释性本身不能替代这条责任链。

## 2. 实际阅读的证据与使用边界

| 来源 | 实际阅读内容 | 本审计允许其支持的命题 | 不能由该来源支持的命题 |
|---|---|---|---|
| Kanawattanachai and Yoo (2007), *The Impact of Knowledge Coordination on Virtual Team Performance over Time*, MIS Quarterly 31(4), 783–808, DOI `10.2307/25148820`；本地全文 `database_fulltext_all/14982_2007_the-impact-of-knowledge-coordination-on-virtual-team-performance-over-time.md` | 理论、研究模型、量表、三期模型、结果、讨论、局限与附录 | expertise location 是团队关于谁知道什么的认知；cognition-based trust 包含能力与可靠性；task–knowledge coordination 包含任务分解、子任务关系和成员分配；三者会随团队历史形成且作用具有时间边界 | 不能直接支持 coding-agent policy、机器可验证 claim、权限状态、具体 handoff 动作或本文拟议损失函数有效 |
| Choi, Lee, and Yoo (2010), *The Impact of Information Technology and Transactive Memory Systems on Knowledge Sharing, Application, and Team Performance*, MIS Quarterly，DOI `10.2307/25750708`；本地全文 `database_fulltext_all/09708_2010_the-impact-of-information-technology-and-transactive-memory-systems-on-knowledge-sharing-applica.md` | 理论模型、假设、团队调查量表、PLS 结果、讨论、局限与 Appendix A | knowledge sharing 与 knowledge application 需要区分；application 是把已有知识实际用于当前问题；application 是 TMS 的下游团队过程，并连接到绩效 | 不能把消息提及当 application；其三项团队自陈量表不能直接充当 action-level 因果标签；横截面结果不能证明本文动态更新律 |
| Nevo and Wand (2005), *Organizational Memory Information Systems: A Transactive Memory Approach*, Decision Support Systems，DOI `10.1016/j.dss.2004.03.002`；本地全文 `database_fulltext_all/09294_2005_organizational-memory-information-systems-a-transactive-memory-approach.md` | TMS 信息系统设计、meta-memory 结构和 operation | 技术系统可以支持 TMS；目录需表示 knowledge subject、retainer 和 meta-knowledge，并支持 directory updating、information allocation 与 retrieval coordination | 不能把任何中央 latent state 或普通 router 都称为人工 TMS |
| CooperBench, arXiv:`2601.13295`，全文 HTML | 任务构造、652 对任务、12 个仓库、4 种语言、通信实验与失败分析 | 当前多 coding-agent 在 expectation、commitment 与 communication 上发生协调失败；现有消息能够减少 merge conflict，却未必提高端到端成功 | 轨迹不提供 checkpoint 异质性的反事实能力、独立的 expertise-location belief、claim reliability、knowledge necessity 或 actual application 真值 |
| SkillGraph, arXiv:`2604.17503`，全文 HTML | skill tuple、running accuracy、failure buffer、Graph Transformer、query-conditioned communication topology 与 policy-gradient 训练 | 动态 skill state、失败记忆和学习型协作图已经有强通用实现；它是候选二必须击败的替代解释 | 视觉多 agent 结果不能直接证明 coding-agent TMS，也没有区分“他能做”与“团队相信他能做” |
| Shepherd, arXiv:`2605.10913`，v3 全文 HTML | typed reversible effect trace、fork/replay、supervisor observation 和 `inject/handoff/discard` 动作 | 通用运行时 supervisor 与 handoff 已被直接实现；quiescent snapshot 与反事实 rollout 有可执行参照 | 不能把“有 supervisor”或“会 handoff”本身作为 TMS 新贡献 |
| Claim Plane design, arXiv:`2607.21909`，PDF；confirmatory study, arXiv:`2608.00947`，PDF | ChangeIntent、typed resource、admission、dependency invalidation、promotion、静态与动态策略、未来 SDM 动作 | semantic dependency、parallel/serialize/replan/escalate/deny 已被明确占位；总串行可提高局部安全却损失效率 | `J` 或 serialize action 单独不足以证明 TMS；Claim Plane 的结果也不支持拟议 TMS 状态有效 |
| SWEET-RL, arXiv:`2503.15478`，全文 HTML 与官方代码库 | step-wise critic、turn-level reward、DPO 和训练时 reference information | 一般协作信用分配已有强训练基线 | step-wise reward 不是 TMS，也不能区分知识分享和知识应用 |
| 肖帅勇老师 ACAA 与 DSDL 全文及本项目 `00J`、`00K`、`00M` 逐句索引 | ACAA 的 design-rationale contract、MEC→MAP→ALG 配对、专用 attention 计算；DSDL 的 E/F 状态、属性×时间张量、`F-E` 方向损失、中间表示与消融 | 用于规定本候选的理论—表示—损失—行动—证据责任链 | 只借鉴句子功能与论证节奏，不复制句子，不因词汇相似就声称理论等价 |

两个 TMS 原文还给出必须保留的证据边界。Kanawattanachai and Yoo 的样本是 38 个 MBA virtual teams，任务结构较稳定、角色可持续、观察跨八周且任务相互依赖。作者明确讨论低相互依赖任务可能不需要 TMS。其 expertise location、cognition-based trust 与 task–knowledge coordination 虽经区别效度检验，相关仍然较高；因此本候选不应以强制正交损失制造理论上不存在的独立性。该文对团队后半程 communication→cognition-based trust 的结果存在表格与讨论文字不一致，且绩效反馈对三项状态的更新假设只获得有限支持。本候选可以检验动态形成和漂移响应，却不能把“后期通信必然减少”或“绩效必然按某固定律更新信任”写成硬编码事实。

Choi et al. 将 TMS 作为多维理论概念但在经验模型中采用整体团队量表，并在局限中承认横截面和静态测量问题。其 knowledge application 是与 TMS 分开的下游过程，测量项是团队对“使用经验知识解决新问题”的自陈。这为本候选要求行为化 application 提供概念区分，但不能替代 correct/corrupt/sham 同前缀干预，也不能证明某段代码改变是因为使用了某条知识。

## 3. 六类状态的理论所有权

### 3.1 责任矩阵

| 状态 | 当前含义 | TMS 理论责任 | 技术责任 | 红队判定 |
|---|---|---|---|---|
| `E*_{a,k,t}` | agent 在知识域 `k` 的任务隔离真实能力后验 | TMS 需要存在专长分化，但不产生这个 oracle | probe 设计、项目划分、时间更新与能力估计 | 仅作训练监督和评价真值，不能在当前测试任务上给 policy 读取 |
| `D_t[a,k]` | 团队关于 agent `a` 是否知道 `k` 的 belief | **部分直接来自 TMS**。它对应 expertise location，但必须明确是谁持有该 belief，以及团队怎样编码、更新和检索 | 概率参数化、校准、时序更新、匿名身份编码 | 当前团队全局点估计不足。重构为 member-specific `D_t^(i)[a,k]`，或团队成员可访问且有更新记录的共享 directory；否则只是 expert router |
| `C_t[a,k,q]` | claim/commitment 的可靠性 | **混合状态**。Kanawattanachai and Yoo 的 cognition-based trust 同时包含 ability 与 reliability，TMS 不直接给出机器可验证 claim schema | claim type、predicate、horizon、verifier、opportunity 和 permission 都由本研究设计 | 将观察到的 claim event 保留为 `C^obs`，将条件可靠性潜变量改记 `R`；再与能力 belief 联合形成 cognition-based trust `T=g(D,R)`。不得声称 `C` 是原文独立 TMS 构念 |
| `Q_t[u,k]` | 子任务 `u` 对知识 `k` 的内在必要性 | TMS 说明专长必须与任务需求匹配，却不产生 `Q` 构念或 its oracle | two-world task、hidden obligations、反事实可满足性判定 | 明确标为 task-world state。它为 TMS allocation 提供外部需求，不计理论构件数 |
| `A_t[a,u,k]` | 知识被正确、错误或未用于下游行动 | Choi et al. 支持“application 与 sharing 不同”，但 application 是 TMS 的下游过程，不是 TMS 内部维度 | action predicate、correct/corrupt/sham 干预、效用分类 | actual `A^obs` 只能在行动后出现。决策时只能使用基于历史的 `hat A_{t+1|h_t}`；把当期 actual `A` 输入 policy 即结果泄漏 |
| `J_t[u,v,r]` | change intents 的 semantic dependency | 无直接 TMS 所有权 | 软件 world model、资源关系、先后约束 | 纯技术状态。Claim Plane/SDM 是直接近邻；不能作为理论贡献 |
| `P_t[a,tool,path]` | permission/affordance mask | 无直接 TMS 所有权；它只改变承诺兑现的 opportunity | 权限、工具和路径可执行性 | 纯技术状态。必须作为 `R` 标签的条件变量与 action mask，不能把无权限误判为不可靠 |
| `Z_t` | 由 `D/C/Q/A` 形成 coordination bottleneck | 当前没有与原理论一一对应 | 人工拼接与瓶颈 | 删除当前定义。以显式 task–knowledge coordination `K_t` 和 policy belief state 替代 |

### 3.2 `D` 为什么不能只是能力分数

`E*` 回答“agent 实际擅长什么”，`D` 回答“团队在时点 `t` 根据已经可见的历史，认为谁擅长什么”。两者的差异是 TMS 最重要的可检验内容之一。若 `D` 由当前任务的 oracle probe 直接写入，模型没有学习 meta-memory；若只有 coordinator 持有 `D`，其他成员既不能检索也不受其影响，则模型更接近 MoE gating 或 centralized expert routing。

可接受的两种实现是：

1. member-specific belief：`D_t^(i)[a,k]` 表示成员 `i` 对成员 `a` 的知识定位信念，同时保留 belief dispersion、overlap 和更新来源；
2. technology-supported shared directory：目录显式记录 knowledge subject、retainer、meta-knowledge、时间戳和证据，并被团队用于更新、分配和检索。它可以是中央服务，但必须是团队可用的协调记忆，而不是只在 policy 网络内部起作用的隐向量。

第二种实现可借鉴 Nevo and Wand 的 artificial meta-memory，但需要实验表明目录的 update、allocation 与 retrieval 三类 operation 各有行为后果。仅给图节点命名为 `expertise` 或在 attention edge 上可视化权重，不足以证明 `D` 具有 expertise-location belief 的语义。

### 3.3 `C` 与 `D` 的辨别效度

建议取消“`D`—`C` 强制 disentanglement”这一笼统表述。TMS 文献中的 cognition-based trust 本来就把能力判断与可靠执行联系起来，Kanawattanachai and Yoo 的量表间相关也不为零。所需辨别不是数学正交，而是条件概率和行为后果不同：

\[
D_t^{(i)}[a,k] = \Pr(a\text{ 在完整机会下能正确处理 }k\mid h_t^{(i)}),
\]

\[
R_t^{(i)}[a,k,q] = \Pr(a\text{ 的声明或承诺按时兑现}\mid a\text{ 具备所需能力},q,O_t,P_t,h_t^{(i)}).
\]

`q` 是 claim type，`O_t` 是执行机会，`P_t` 是权限。`R` 不应吸收知识缺失、工具不可用或根本没有执行机会。能力 belief 与 residual reliability 可经联合校准形成 `T_t^(i)=g(D_t^(i),R_t^(i))`，作为 cognition-based trust 的操作化；具体函数由数据学习，不能仅凭理论宣称高能力低可靠或低能力高可靠时哪个必然优先。

辨别效度至少需要以下设计。

- 建立 capability checkpoint 高/低 × reporting/execution fidelity 高/低的 2×2 因子。改变 reporting policy 时固定 checkpoint、工具与任务；改变能力时固定 reporting mechanism、权限和机会。仅靠 prompt 说“你是不可靠的 agent”不构成稳定操纵。
- `D` 用未见知识域 probe 和未来时点的 `E*` 校准；`R` 用在能力、机会和权限条件化以后仍可检验的 claim/commitment fulfillment 校准。
- 使用相同任务难度、相同 claim schema 和多种测量方法，报告 cross-loading、增量预测效度、Brier/NLL、校准曲线及四格覆盖，不把低相关当作唯一标准。
- 做独立干预。打乱 `D` 应主要改变任务所有权与知识请求对象；打乱 `R` 应主要改变验证强度、承诺依赖和 handoff 门槛。两者若总是触发同一动作，模型没有建立不同构念。
- 在能力漂移但 reporting fidelity 不变、以及 reporting fidelity 漂移但能力不变的两类 episode 中检验更新方向。若两个 latent state 总是同步变化，`C/R` 只是成功历史的重复编码。

以下任一结果触发理论 NO-GO：2×2 的关键单元无法稳定构造；`R` 在条件化 `D/O/P` 后不再预测兑现；`D` 和 `R` 的干预产生不可区分的 action distribution；或者等参数单一 success-history state 与双状态模型表现及干预行为相同。

## 4. `Q` 与 `A` 的因果标签审查

### 4.1 `Q`：two-world 设计是必要条件，不是自动充分条件

同一 receiver 可见前缀、私有知识取 `k0/k1`、两个世界的 hidden obligations 不同，是识别 task-intrinsic knowledge need 的正确方向。但开放式 coding task 通常存在多条等价实现路径。“gold patch 在两世界不同”或“某个 reference solver 选择不同”都不能证明没有一个知识无关动作同时满足两世界。

`Q=1` 必须满足更强的合同：

1. 两世界在 receiver 决策前的代码、消息、文件元数据、测试可见性和 token 长度上不可区分，排除 lexical 或 generator-template 泄漏；
2. `k0/k1` 导致互斥且可执行验证的语义义务，例如互斥 API signature、symbol semantics、system invariant、dependency/order fact 或 test obligation；
3. 在预先限定的 permitted action class 内，没有同一行动可同时满足两个世界；若无法证明，标签必须是 `ambiguous/unknown`，不能强行记作 positive；
4. generator、solver 与 evaluator 分离，hidden tests 和 obligation verifier 不进入训练输入；
5. 建立同仓库、同难度、同表面线索的 `Q=0` matched item，并按 repo lineage、base commit、generator template 与 two-world variants 整组划分；
6. 除 reference solver 外，再用独立 solver 搜索可能的 knowledge-free workaround。发现可行替代时撤销该 item。

因此，`Q` 能成为可信的技术监督信号，但不能算作 TMS 理论的新构念。它的作用是让后续 allocation 有“谁的什么知识在这里真正必要”的外部 ground truth。

### 4.2 `A`：行为识别不能被写成未观察的心理使用

correct/corrupt/sham 三臂和同前缀 paired rollout 明显优于“消息被读取或在回复中复述”。不过下游动作随知识 packet 改变，仍可能来自字面服从、来源信誉、格式差异、拒绝倾向或随机采样，并不自动识别对语义知识的应用。

最低限度需要：

- correct 与 corrupt packet 等长、同格式、同来源、同置信语气，只改变内容方向；另加语义等价 paraphrase 和 source/format control；
- 在运行前预注册 content-specific action predicate，predicate 落到可执行 API、symbol、invariant、test assertion 或 dependency order，不能由模型事后主观解释；
- 固定 receiver checkpoint、repo/tool state、未来 collaborator behavior、permission 和 paired decoding seed，并随机化 branch order；
- 报告 immediate application 与 delayed transfer。若模型只复述 packet 而后续实现不遵守语义义务，应归为 not-used；
- 将 `used-helpfully`、`used-harmfully`、`not-used` 与 `ambiguous` 分开。application 是有无内容特异性影响，utility 是影响是否正确，两者不能合并；
- 覆盖 `Q1A1/Q1A0/Q0A1/Q0A0`。缺少 `Q0A1` 或 `Q1A0` 时，知识需要与知识使用仍难分离；
- 对人工复核报告盲评协议、Cohen's kappa 与 disagreement adjudication，不用 LLM judge 单独决定 application。

这里可以声称的是“知识 packet 对可观察 coding action 的内容特异性因果影响”，不能声称 agent 内部形成了某种不可观察心理状态。尤其重要的是时序隔离：

\[
\hat A_{t+1\mid h_t}=f_\phi(D_t,R_t,Q_t,K_t,J_t,P_t,h_t)
\]

可以进入当前 policy；

\[
A^{obs}_{t+1}=\operatorname{Classify}(\text{post-action trace under intervention})
\]

只能在行动完成后进入更新和训练损失。若 `A^{obs}_{t+1}` 或由 terminal test 反推出的同义变量进入时点 `t` 的 policy，立即撤题，无需再比较性能。

## 5. TMS 必须产生的中间表示

### 5.1 从 `Z` 改为可审计的 TMS 状态

当前 `Z=Fuse(D,C,Q,A)` 没有清楚的理论元素语义。建议把模型分成四层，并让每层所有权不同。

**第一层是外部技术世界。** `Q_t[u,k]` 描述知识需求，`J_t[u,v,r]` 描述软件语义依赖，`P_t[a,tool,path]` 描述可执行权限。它们可以由专门预测器学习，但其性能不计入 TMS 理论贡献。

**第二层是 meta-memory directory。** 对每个观察者 `i`，保存

\[
M_t^{(i)}=\{D_t^{(i)}\in[0,1]^{|A|\times|K|},
R_t^{(i)}\in[0,1]^{|A|\times|K|\times|Q_c|},
U_t^{(i)},\tau_t,E_t^{src}\},
\]

其中 `U` 是不确定性，`tau` 是最近更新时间，`E^{src}` 是证据来源。共享目录版本必须保留每次 update 的 provenance，不能把不同成员的证据无痕平均。

**第三层是 task–knowledge coordination。** 新增

\[
K_t^{(i)}[u,v,a,k,r],
\]

其元素表示成员 `i` 对“子任务 `u/v` 具有关系 `r`、知识 `k` 需要由成员 `a` 负责或提供”的联合表征。为控制张量规模，可将其因子化为 task decomposition `G_t[u,v,r]`、knowledge need `Q_t[u,k]`、assignment belief `X_t^{(i)}[u,a,k]` 和跨成员 overlap/dispersion；但不能只保留一个 pooled graph embedding。Kanawattanachai and Yoo 所定义的 task–knowledge coordination 正是任务分解、子任务关系和成员分配的重叠认知。缺少 `K` 时，候选二只建模“谁可能厉害”，没有建模知识怎样与共同任务协调。

**第四层是预期 application 与 policy belief。** `hat A` 只预测某成员在给定 allocation/query/handoff 后会否把所需知识用于行动。policy state 可以包含 `D/R/K/hat A` 与外部 `Q/J/P`，但 actual `A^obs` 必须延迟。主模型应禁止 raw evidence 绕过这些理论状态；同时必须设置允许 raw bypass 的等参数模型作为反证，而不是用瓶颈规则预先赢得比赛。

### 5.2 TMS 形成需要真实的时间与团队边界

一轮任务中临时创建两个匿名、同 checkpoint、同上下文的 worker，不足以形成 TMS。最低研究环境应具有：

- 稳定但可匿名化的 agent identity，使过去证据能归属于同一 retainer；
- 可验证的异质知识、checkpoint、adapter、repo experience 或 private context，而不是 prompt role-play；
- 多轮、重复且相互依赖的任务，使 directory 能编码、更新与检索；
- 能力漂移、reporting-fidelity 漂移、权限撤销与知识过期，让模型需要区别更新不同状态；
- 低相互依赖任务作为负控制。若 TMS 模块在任务可完全独立时仍有同样优势，更可能是额外容量、正则化或 supervisor effect。

## 6. 前向计算、损失与真实动作

### 6.1 必须闭合的前向循环

候选二若保留，推断循环应按下列顺序实现，而不能在终点后回填状态：

1. **encode/update**：根据时点 `t` 之前的 probe、claim、commitment、tool trace 和 outcome evidence，更新每个成员或共享目录中的 `D/R/U`；
2. **decompose/coordinate**：用 `Q/J/P` 与 directory 构造 `K_t`，明确子任务关系、所需知识和暂定 owner；
3. **retrieve/query**：当 directory 对必要知识的位置不确定时，选择具体 retainer 和 knowledge item 发起 targeted query 或 probe，而非广播；
4. **allocate/sequence/handoff**：输出任务 ownership、执行顺序、contract、cross-verification 或 checkpoint handoff；
5. **execute/observe**：执行 coding/tool action，观察 fulfillment、diff、tests、conflict、wasted work 与 `A^obs`；
6. **directory update**：将新证据按来源、机会和权限写回 `D/R/K`，进入下一时点。

这个循环对应 Nevo and Wand 的 directory updating、information allocation 和 retrieval coordination，也把 Kanawattanachai and Yoo 的动态团队过程落实成可审计 transition。任何只有第 4 步的 model 都只是 action router。

### 6.2 损失的理论与技术分工

总损失可以写为

\[
\mathcal L = \lambda_D\mathcal L_D+\lambda_R\mathcal L_R+
\lambda_K\mathcal L_K+\lambda_{dir}\mathcal L_{dir}+
\lambda_A\mathcal L_A+\lambda_\pi\mathcal L_\pi+
\lambda_J\mathcal L_J+\lambda_Q\mathcal L_Q.
\]

各项责任如下。

- `L_D`：对未来未见 probe 的 `E*` 做 Beta-Binomial NLL 或 proper scoring calibration，同时保留 observer-specific belief。它检验“谁知道什么”的定位是否准确。
- `L_R`：在能力、opportunity 与 permission 条件化后，对可验证 claim/commitment 的 fulfillment 做 Brier/NLL；UNKNOWN 不进入负例。这里不加入把 `D` 和 `R` 强推到零相关的损失。
- `L_K`：监督 task decomposition、subtask relation、knowledge–subtask matching 与 owner assignment，并用反事实 allocation outcome 检查协调表征。若只预测 `J`，不算 `K`。
- `L_dir`：对证据到达后的 directory update、所需知识的 retainer retrieval、以及 allocation 的 counterfactual regret 施加训练信号。它必须能区分更新错人、检索错人和分配错人。
- `L_A`：只根据 correct/corrupt/sham 行动后的 `A^obs` 训练 `hat A`，预测行为 application 和 utility 两个输出，不能用消息复述当标签。
- `L_pi`：在相同前缀多动作 continuation 上优化 constrained/CVaR risk–success–cost objective，风险包含 conflict-induced regression、overwrite、lost work、unmet joint obligation 和不可恢复浪费；同时控制 both-task success、wall-clock、token、GPU/tool cost 和 human intervention。
- `L_Q` 与 `L_J`：分别训练 two-world need 和 semantic dependency，是必要技术损失，但在贡献表中单列为 supporting world models。

可以把早期 directory uncertainty、后期 coordination 与 communication efficiency 写成待检验机制，不应把“团队成熟后一定减少通信”硬编码成单调正则。原始时间研究对相关路径的证据并不一致。更稳妥的检验是：同等不确定性和任务互依下，成熟 directory 是否让 query 更有针对性、重复广播更少，而不是通信总量机械下降。

### 6.3 动作与理论责任不能混写

| policy action | TMS 可以承担的机制 | 主要技术机制 | 必须观察到的冲突情境 |
|---|---|---|---|
| actual allocation / reassign | `D/T` 与 `K` 让任务交给具有必要知识且可可靠执行的人；错误 belief 会导致 misallocation | workload、runtime 与工具可用性 | 同 `J/P` 下交换 `D` 行，owner 应改变；只交换 `R` 时验证或协作方式应变，但能力归属不应完全翻转 |
| targeted query / retrieval | expertise location 决定问谁、问什么；directory uncertainty 决定是否先检索 | query syntax、verifier 和 message protocol | 保持任务和 agent 不变，仅提高对必要知识位置的不确定性，应增加定向 probe/query 而非全局广播 |
| handoff with checkpoint | 新证据表明现 owner 缺少必要知识或不可靠，`K` 需要重配 | checkpoint serialization、state transfer 和 reversible trace | capability drift 与 reporting drift 应产生不同 handoff/verification pattern；单纯失败不应总触发同一规则 |
| structured contract / cross-verification | cognition-based trust 的可靠性部分可以影响依赖承诺的程度 | claim schema、machine verifier 和 test generation | 高 `D` 低 `R` 时可保留 expert 但增加可验证 contract；低 `D` 高 `R` 时不应因守信而承担其不懂的任务 |
| serialize / continue parallel | TMS 只通过“谁需要谁的知识、分配是否协调”间接影响顺序 | `J/P`、资源冲突、Claim Plane admission 是主要责任 | 固定 `D/R/K` 只改变 `J` 时，顺序变化应归因于 world model；若所谓 TMS 收益全来自总串行，撤题 |
| discard / rollback | 可作为错误 coordination 后的恢复动作 | Shepherd trace、事务和恢复机制 | 删除 TMS 状态后仍同样触发 discard，说明该动作不构成理论证据 |

TMS 并不规定高能力低可靠与中等能力高可靠时唯一正确的 allocation。理论提供需要同时表示的冲突维度；具体选择必须从结果中学习并由机制干预验证。把任意手工分数 `alpha D+(1-alpha)C` 称为理论策略不够。

## 7. 等参数通用替代的反证协议

### 7.1 必须进入主表的替代模型

1. **raw heterogeneous graph Transformer**：节点、边、历史和 action decoder 与主模型相同，不使用 TMS factorization；
2. **SkillGraph-coding adaptation**：skill embedding、running accuracy、failure buffer、version 和 query-conditioned topology，用同样 coding evidence 更新；
3. **generic belief-state POMDP**：隐状态维数、transition capacity 与 action space 同预算，不指定 `D/R/K` 语义；
4. **Claim Plane/SDM+history**：以 ChangeIntent、typed resources、dependency 与 admission history 选择 parallel/serialize/replan/escalate/deny；
5. **Shepherd supervisor**：相同 snapshot、observation horizon 与 `inject/handoff/discard` 能力；
6. **SWEET-RL / generic stepwise critic**：相同 rollout 与 reference budget，排除一般信用分配；
7. **central planner、MoE router、shared scratchpad、fixed expert、leader/follower 与总串行策略**：分别排除中央能力路由、更多共享上下文、角色固定和降低并发的简单解释。

### 7.2 公平性约束

- 相同 base model、checkpoint/adapter pool、train/dev/test episodes、raw observations、消息历史、工具、结构化 action decoder 与 terminal evaluator；
- 参数量控制在 ±2%，同时控制 activated parameters、FLOPs、context tokens、消息 tokens、tool calls、rollout continuations、wall-clock 和超参数搜索预算；
- 分两层比较。第一层让通用模型取得同一 raw evidence；第二层让等参数通用模型取得同一 `D/R/Q/A/J/P` supervision，但不强制 TMS factorization。主模型若只因额外标签或 oracle 状态胜出，不能归因于理论架构；
- 所有模型使用相同 quiescent-prefix branches、paired seeds 与 branch-order randomization；
- 以 repo/fork lineage、base commit、generator template 与 counterfactual family 整组划分，并做 chronological、unseen checkpoint、unseen agent pair、unseen repo 和 drift 测试；
- 报告完整 risk–success–cost Pareto frontier，不能只挑某个串行化程度或单一 team pass rate；
- 同时比较 sample efficiency、calibration、机制状态、动作干预和端点结果。通用模型不能只在端点上弱化配置，理论模型也不能独占更多 verifier 或更强 hidden oracle。

### 7.3 何时等参数替代已经复制理论能力

理论模型必须同时提供四层证据。

1. **端点层**：在相同成功率或成本下减少 conflict regression、overwrite、lost work 与 unmet obligation，或在相同风险下提高 both-task success；
2. **表征层**：`D/R/K/hat A` 对未见任务和漂移保持校准，并具有独立于 terminal label 的行为效度；
3. **干预层**：交换 expertise belief、reliability、task interdependence 或 knowledge location 时，allocation/query/handoff 按理论责任改变；
4. **边界层**：优势集中在知识异质、部分可观察且任务相互依赖的情境，在低互依或知识完全共享时缩小。

若等参数 generic graph Transformer 或 POMDP 达到相同 Pareto frontier，并在预注册状态干预下作出同样动作，则 TMS factorization 没有新增算法能力。即使其 latent state 更容易解释，也不满足本项目“理论带来不可替代计算”的入选标准。若通用模型端点相同而理论模型仅在中间状态可读性上更好，可以保留为可解释性发现，但应撤销“独立理论算法贡献”，候选二在三篇论文系列中仍应 NO-GO。

## 8. 直接近邻对候选二的占位压力

### 8.1 CooperBench

CooperBench 提供的是两个兼容但可能冲突的 feature task、私有上下文和联合测试环境。其失败分析中的 expectation、commitment 和 communication 能说明问题重要，却不能给 `D/R/Q/A` 真值。现有 team trajectories 主要是单次 realized outcome，同一 agent deployment 也无法构造“实际能力相同但团队 belief 不同”或“能力不变但 reporting fidelity 改变”的反事实。它适合作 external evaluation，不适合作 TMS state supervision。

### 8.2 SkillGraph

SkillGraph 已把 active skill、running accuracy、failure buffer 和动态 communication topology 联合训练。若候选二只是把这些节点改名为 expertise、trust 和 coordination，再多加一个 handoff head，贡献会被直接吸收。候选二必须额外证明：belief 与 actual ability 可分；reliability 与 expertise 可分；task–knowledge coordination 不是 query-conditioned edge；成员知道“谁知道什么”会改变 retrieval/allocation；actual application 只从行动干预识别。

### 8.3 Shepherd

Shepherd 在 typed reversible effect trace 上已让 supervisor 观察 worker 状态并执行 inject、handoff 和 discard。候选二不能把可逆 trace、central supervisor 或 handoff success 当作理论创新。Shepherd 应作为同 observation、同 continuation budget 的直接 action-policy 基线；TMS 的新增责任只能来自知识位置 belief、可靠性、任务—知识分配和随经验更新。

### 8.4 Claim Plane

Claim Plane 已区分 independent、compatible overlap、contract dependency、hard conflict 与 uncertain 等关系，并让 policy 选择 parallel、serialize、notify、replan 或 reject。其 confirmatory study 还展示 static policy 可能通过接近总串行获得表面安全，dynamic policy 又受 undeclared scope 限制。这直接要求候选二把 `J` 固定或单独消融：若收益来自更准确的 semantic dependency 或更多 serialization，它是 software coordination/world-model 贡献，不是 TMS。

### 8.5 SWEET-RL

SWEET-RL 的 step-wise critic 和 turn-level reward 已覆盖协作轨迹的细粒度信用分配。候选二若只给每次 handoff 一个更密 reward，属于通用 RL 改进。TMS 需要让 reward/transition 对 directory update、错误 retainer retrieval、misallocation 和 knowledge application 分别负责，并与等预算 generic critic 比较。

## 9. 用 ACAA/DSDL 的句子功能链建立理论—计算责任

这里学习的是肖帅勇老师论文中“每句话完成什么论证动作”，不是借用 attention、satisfaction、expectation 等词汇。ACAA 最关键的做法是先签署 design-rationale contract，随后按 MEC→MAP→ALG 配对：理论说明一般 affinity calculation 为什么会朝错误方向计算，概念化产生 timeliness/diversity/voting 等可计算指标，算法再改变权重。DSDL 最关键的做法是把期望与体验放入同一属性×时间坐标，产生具有元素语义的 `E/F` 张量，用理论规定方向的 `F-E` 进入前向与损失，并分别验证中间状态、联合损失和端点结果。

候选二应采用下列句子功能链。它不是正式正文模板，而是每个论证单元的责任清单。

| 顺序 | 句子/单元功能 | 候选二必须承担的内容 | 需要的证据 | 禁止的替代 |
|---|---|---|---|---|
| 1 | CXT | coding agents 会同时修改相互依赖的软件对象，成员可见的信息、能力和权限不完全相同 | CooperBench 与实际工具工作流 | 先宣布 TMS 或模块名 |
| 2 | OUT | 错误协调会造成冲突回归、覆盖、lost work、unmet obligation 和不必要串行成本 | CooperBench/Claim Plane/Shepherd 的直接事实 | 只说 pass rate 低 |
| 3 | ACK | 承认现有 communication、supervisor、dependency admission、dynamic skill graph 与 RL critic 已能处理部分问题 | 五个直接近邻原文 | 把近邻降成 prompt baseline |
| 4 | LIM | 指出这些方法没有区分 actual expertise、团队对 expertise location 的 belief、条件可靠性和 actual application | 对各工件输入/状态/监督的逐项核验 | 因术语未出现便断言能力不存在 |
| 5 | MEC-1 | TMS 将团队能力视为 cognitive labor 的分工，成员需要知道谁保有什么知识 | Kanawattanachai and Yoo；Nevo and Wand | 用普通 skill score 代替 belief |
| 6 | MAP-1 | 将机制映射为 observer-specific meta-memory directory，并区分 `E*` 与 `D` | 本文操作化和标签合同 | 在理论文献中虚构现成张量 |
| 7 | ALG-1 | 定义 `D_t^(i)`、uncertainty、evidence provenance 与 update/retrieval 运算 | 公式、数据流、更新日志 | pooled graph embedding 无元素语义 |
| 8 | MEC-2 | cognition-based trust 涉及成员能力与可靠履责，而不是一般友善或消息数量 | Kanawattanachai and Yoo 的定义与量表 | 把 verifier schema 冒充原构念 |
| 9 | MAP-2 | 把 residual reliability `R` 与能力 belief `D` 条件化分开，并声明二者可相关 | 2×2 操纵、增量效度 | 强制正交或同一 success score |
| 10 | ALG-2 | `D/R` 在前向中共同决定依赖程度、验证和分配，而不同干预改变不同动作 | joint state、loss、action probe | 只在 auxiliary head 预测 `C` |
| 11 | MEC-3 | 团队表现依赖的不是孤立专家列表，而是任务分解、子任务关系与知识—成员分配的协调 | Kanawattanachai and Yoo 的 task–knowledge coordination | 将 `J` 或 communication graph 直接改名 TKC |
| 12 | MAP-3 | 创建 `K_t^(i)[u,v,a,k,r]` 或等价因子化，并定义 overlap/dispersion | 元素语义、可观察对应 | 只输出一个 `Z` 向量 |
| 13 | ALG-3 | `K` 必须进入 allocation、targeted query、handoff 和 reassign 的 logits 或约束 | 前向公式与理论中和实验 | 仅在解释器中展示 `K` |
| 14 | MEC-4 | knowledge sharing 不等于 knowledge application；有效协调需要知识真正进入下游行动 | Choi et al. | 用消息发送/复述当 application |
| 15 | MAP-4 | `A^obs` 定义为 correct/corrupt/sham 对可观察 action 的内容特异影响，并与 utility 分开 | 同前缀干预合同 | accepted patch overlap 或自陈 |
| 16 | ALG-4 | 训练 `hat A`，但 actual `A^obs` 仅在 post-action update 使用 | 时间索引、leakage test | 当期 actual `A` 输入 policy |
| 17 | RIVAL | 明确普通 graph/POMDP/SkillGraph 为何可能复制，并给同数据、同动作、等参数反证 | 公平基线协议 | 只和 fixed role 或 no-communication 比 |
| 18 | EVID | 依次报告端点、理论表示、机制干预和边界条件 | 主结果、校准、intervention、低互依负控制 | 端点提升后回填理论解释 |
| 19 | CON | 理论贡献限定为“可识别的 meta-memory 与 task–knowledge coordination 是否改善风险动作”，算法贡献限定为经反证仍未被通用模型复制的能力 | 本文运行结果 | 宣称 TMS 普遍优于通用 agent |

这条链对引文责任也有明确限制。Kanawattanachai and Yoo 负责 TMS 构念、时间性与任务互依边界；Choi et al. 负责 sharing/application 区分；Nevo and Wand 负责 technology-supported directory 的结构与 operation；CooperBench 等负责现象和近邻能力。新的 `D/R/K/hat A` 张量、损失、action policy 以及效果都由本研究的数据和实验负责，不能让理论引文代替 artifact evidence。

在正式论文中，每一个 MEC 段后都应像 ACAA 一样紧跟 MAP/ALG 段，回答“通用计算朝哪个方向做错、因此必须新增什么元素、它在哪一条公式里改变什么”。每一个理论中间状态都应像 DSDL 的 `E/F` 一样有元素语义、方向或关系约束、可单独测量的表示质量和中和实验。如果 `D/R/K` 只是三个辅助预测头，最后又由 unrestricted Transformer 从 raw history 直接决定动作，这条责任链没有闭合。

## 10. 预注册机制反证

下列实验不是普通消融，而是检验 TMS 状态是否承担它所声称的动作责任。

1. **expertise-location swap**：固定 agent checkpoint、task、`R/Q/J/P` 和 raw history，只交换 coordinator/member 对两个 agent 的 `D` belief。预测是 allocation 和 targeted query 对象改变；若不变，`D` 未进入真实决策。
2. **belief–ability mismatch**：分别构造正确高信念、低估专家、高估非专家。模型应在新 outcome 到来前按 belief 行动，之后用证据校正。若模型从未受错误 belief 影响，可能偷读 `E*` 或 raw capability signature。
3. **reliability-only intervention**：固定能力和知识位置，只改变 reporting/execution fidelity。预测是 contract、cross-verification 和 reliance/handoff threshold 改变，而不是把可靠但无能力者自动当专家。
4. **capability-only drift**：固定 reporting fidelity，交换 checkpoint/adapter。预测是 `D` 和 owner 更新快于 `R`；与 reliability-only drift 的状态和动作应可区分。
5. **knowledge-location relocation**：知识内容不变，只换 retainer。targeted retrieval 应随 directory 变化；若总广播或询问固定 leader，未使用 TMS。
6. **task-interdependence removal**：将任务改为可独立完成且无跨任务知识义务。TMS 相对优势应明显缩小。若优势不变，更可能来自额外容量或通用历史摘要。
7. **TKC neutralization**：保持 `D/R/Q/J/P`，打乱 task decomposition、subtask relation 与 member assignment 的联结。高互依任务应出现更多 unmet obligation、wasted work 或错误 handoff；低互依任务影响较小。
8. **application content swap**：在相同前缀交换 correct/corrupt packet，检验 `hat A` 与后续行为，不允许用消息 mention 评分。
9. **raw-bypass refutation**：开放同容量 raw-history bypass。若其复制主模型全部结果和干预行为，理论瓶颈没有新增能力；不能以“解释性较差”回避。
10. **communication-budget match**：固定 tokens、turns 和 tool calls。若 TMS 只通过更多消息或总串行改善风险，机制假设被否证。

值得强调的是，理论不保证每个单项干预都有单调端点提升。比如错误 belief 被交换后，模型按该 belief 调整 allocation 正是表示有效的证据，但端点可能下降；随后能否根据证据纠正才是动态协调能力。机制有效性、policy optimality 与 endpoint utility 必须分开报告。

## 11. pilot 门槛与撤题条件

### 11.1 未来新候选重新立项前的必要门槛

这些门槛不挽救当前候选，只定义未来新候选重新审查时的最低证据。pilot 至少覆盖 20 个 repos、120 个 task families、200 个 policy prefixes、稳定身份的异质 agent profiles 和重复 interdependent episodes。需同时满足：

- two-world construction pass rate 不低于 70%；
- application non-ambiguous rate 不低于 25%；
- correct/corrupt content treatment first-stage effect 不低于 0.20；
- paired-seed agreement 的 Cohen's kappa 不低于 0.60；
- `D/R` 2×2 可构造，且二者在条件化能力、机会与权限后具有增量效度；
- `Q/A` 四格均有足够样本，且没有 generator/template leakage；
- actual `A` 时间索引和训练 pipeline 通过自动 leakage audit；
- `K` 显式包含 task decomposition、subtask relation 与 member assignment，并有可检查的 element-level target 或 intervention；
- member-specific belief 或 shared directory 至少完成 update、allocation、retrieval 三类 transaction；
- 一个小规模等参数 generic graph/POMDP pilot 尚未复制全部 frontier 与机制行为。

通过这些门槛只允许提交一次新的理论审查，不自动获得论文占位，也不等于理论成立。

### 11.2 立即 NO-GO

出现下列任一情形，不应为凑足三篇论文继续包装：

1. 研究环境只有一次性、同质、无稳定身份的 agent pair，无法形成或更新 transactive memory；
2. `D` 只是中央 oracle capability table，团队成员无法访问、更新或据此检索；
3. `C/R` 与 `D` 无辨别效度，或 reliability 只是任务成败的另一种编码；
4. `Z` 没有显式 task–knowledge coordination，只把 `D/C/Q/A` 拼接；
5. 当期 actual `A`、terminal tests 或 repeated-rollout oracle 进入当前 policy；
6. two-world 任务不能排除 knowledge-free workaround，或 correct/corrupt/sham 只识别字面服从；
7. 收益在去掉 task interdependence 后不缩小，或主要来自 `J/P`、总串行、更多 tokens、广播、oracle verifier；
8. SkillGraph、Claim Plane+history、Shepherd 或等参数 generic graph/POMDP 在相同预算下复制 risk–success–cost frontier 与机制干预行为；
9. 理论模块只提高中间状态可读性或充当 auxiliary regularizer，没有改变 allocation/query/handoff action；
10. 主要结果只有 team pass rate，未测 conflict/security regression、overwrite、lost work、unmet obligation、wasted work 与人工/计算成本；
11. 无法在 unseen checkpoint、agent pair、repo 或 capability/reliability drift 上保持校准；
12. 理论中和、row swap、knowledge relocation 和低互依负控制不能产生预注册的差异行为。

## 12. 最终判定及对总体系列的建议

候选二所面对的问题真实且重要：coding-agent 团队的风险并不只来自某个 worker 写错代码，也来自团队误判谁掌握关键知识、错误依赖未兑现的承诺、没有把必要知识用于相互依赖修改，以及在错误分配后继续并行造成传播性损害。这个问题与 TMS 有自然联系，但自然联系不等于当前算法已经由 TMS 产生。

现版本最薄弱的点不是算力，也不是数据量，而是理论状态的时序和所有权。`D` 尚未明确由谁相信，`C` 尚未从能力和机会中剥离，`A` 被放在了可能泄漏结果的位置，`Z` 缺少真正的 task–knowledge coordination。与此同时，SkillGraph、Shepherd 和 Claim Plane 已分别占据动态技能图、supervisor/handoff 与 semantic dependency/action admission。若不完成上述重构，候选二只是把强通用 coordinator 的状态改成 TMS 术语，应立即撤题。

因此，本审计对候选二作出 **NO-GO，无保留** 的最终判定，并建议立即从当前三篇论文系列中移除。理由不是尚缺几个实验，而是当前构念所有权、时序和计算责任均未闭合，且核心状态很可能被等参数通用图模型或 belief-state policy 吸收。未来只有在稳定、异质、重复且高度互依的 agent team 上，先完成 meta-memory directory、task–knowledge coordination、`D/R` 2×2、two-world `Q`、post-action `A` 和等参数替代 pilot，才可以把重构后的设计作为一个**新候选**重新送审；在此之前不得为它保留 thesis 槽位，也不得把它降成 routing、提示词或辅助评分头继续包装。

## 参考文献与直接来源

Choi, S. Y., Lee, H., & Yoo, Y. (2010). The impact of information technology and transactive memory systems on knowledge sharing, application, and team performance. *MIS Quarterly*. https://doi.org/10.2307/25750708

Kanawattanachai, P., & Yoo, Y. (2007). The impact of knowledge coordination on virtual team performance over time. *MIS Quarterly, 31*(4), 783–808. https://doi.org/10.2307/25148820

Nevo, D., & Wand, Y. (2005). Organizational memory information systems: A transactive memory approach. *Decision Support Systems*. https://doi.org/10.1016/j.dss.2004.03.002

CooperBench. arXiv:2601.13295. https://arxiv.org/abs/2601.13295

SWEET-RL. arXiv:2503.15478. https://arxiv.org/abs/2503.15478

SkillGraph. arXiv:2604.17503. https://arxiv.org/abs/2604.17503

Shepherd. arXiv:2605.10913. https://arxiv.org/abs/2605.10913

Claim Plane design paper. arXiv:2607.21909. https://arxiv.org/abs/2607.21909

Claim Plane confirmatory study. arXiv:2608.00947. https://arxiv.org/abs/2608.00947
