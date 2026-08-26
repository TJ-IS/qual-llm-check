# C1′ 依赖选项 Schober 救援终审

> 审查日期：2026-08-15  
> 审查对象：C1′“面向未来依赖冲击创建并行使架构选项”的 Schober-centered rescue pilot  
> 最终判定：**NO-GO。维持 FORMAL-FREEZE，不得恢复为三篇论文中的候选题。**  
> 可保留资产：两时点依赖冲击执行基准、时间封存协议和数据构造工具。它们可以成为软件工程基准或后续新题的基础设施，不能继续被表述为已经成立的 ISR 级理论算法贡献。

## 0. 判定摘要

本终审把“文献已经报告的事实”“尚可执行的研究设计”和“本次审查判断”分开。文献事实是，Schober 与 Gebauer（2011）把 flexibility-to-change 分解为初始附加投入、未来未预见任务、后续修改或升级、是否提供灵活性，以及有无灵活性时的总成本差。研究设计可以据此建立当前功能、初始 premium、未来状态分布、with/without-option 后果和 exercise/no-exercise 行动。终审判断则是，这一分解没有产生通用两阶段 POMDP、world model 或匿名 factorized model 无法自然表示或学习的状态、方向、损失或动作。

决定性反证不是“一个黑箱模型可能也能学会”，而是**精确的计算同构**。若给等参数通用模型相同的 \(I_0\)、\(C_0\)、未来状态分布、可行动作集、with/without 后果监督和效用函数，Schober-centered value relation 就是两阶段 Bellman 回溯的一种具名展开。两者可以逐状态、逐动作得到同一 \(Q_1\)、\(V_1\)、\(Q_0\) 和策略。Schober 与 Gebauer在原文结尾还明确说明，只要任意模型能提供 TCF 与 TCNF，灵活性价值差的计算不依赖所选模型。这一表述支持它作为估值框架的可移植性，同时否定了把某个 temporal GNN、twin branch 或 hierarchical decoder声称为该理论独有算法结构的依据。

数据审查得到第二个独立的 NO-GO 理由。截至审查日，没有公开资产同时提供同一 \(t_0\) 仓库与功能任务、严格当时可见的信息、matched with/without-option 设计、同一隐藏 \(t_1\) 冲击、stable/right-censored/benign 窗口、真实 exercise/no-exercise 轨迹和可执行安全结果。BUMP、SWE-Chain、FreshBrew、PyMigBench 等提供事件发生后的 breaking update 或 migration；DepDec-Bench 提供当前依赖决策的观察证据；EvoCode-Bench、SlopCodeBench、Needle in the Repo 和 SWE-EVO 提供迭代演化或结构结果。它们可以拼成数据生成来源，却不能直接识别 \(t_0\) 的 option value。用事件库反向抽样会条件化在 \(Shock=1\)，用历史事件又无法排除基础模型参数记忆。

窄范围工程 pilot 在本地算力上可以运行，但它不能解除理论同构。即使 pilot 得到显著的样本效率或风险结果改进，只要 matched-state generic POMDP 在预注册等效界内复现，该改进也只能归因于状态监督、数据生成或优化便利，不能归因于 Schober 理论带来的不可替代计算机制。依照肖老师两篇 ISR 论文的标准，候选在“通用计算为何系统性处理错，以及理论如何改写该计算”这一句尚未成立，因而不应进入正式论文写作。

## 1. 审查材料、检索范围与证据边界

### 1.1 本地材料

本次逐项复核了以下材料。

1. [00A_广义安全概念边界与系列选题论证.md](00A_广义安全概念边界与系列选题论证.md)、[00B_内部选题与可行性审计.md](00B_内部选题与可行性审计.md)、[00E_直接近邻与数据资源核验台账.md](00E_直接近邻与数据资源核验台账.md)、[00N_候选一未来依赖冲击与架构选项红队规格.md](00N_候选一未来依赖冲击与架构选项红队规格.md)和[00O_候选一架构选项理论与时间泄漏反证.md](00O_候选一架构选项理论与时间泄漏反证.md)。
2. Schober 与 Gebauer 的本地主文 database_fulltext_all/05638_2011_how-much-to-spend-on-flexibility-determining-the-value-of-information-system-flexibility.md，包括经济模型、DCF、DTA、ROA、compound ROA、风险模拟、结论和 Appendix A。
3. 肖帅勇老师两篇 ISR 主文及[00J_肖帅勇两篇ISR全篇逐句逻辑与引文责任索引.md](00J_肖帅勇两篇ISR全篇逐句逻辑与引文责任索引.md)、[00K_DSDL全篇逐句逻辑与引文责任索引.md](00K_DSDL全篇逐句逻辑与引文责任索引.md)和[00M_ACAA实证贡献与结论逐句逻辑索引.md](00M_ACAA实证贡献与结论逐句逻辑索引.md)。
4. 四篇最直接的 AIS Basket 全文：Khan et al.（2017）、Zhang and Babovic（2011）、Benaroch（2018）以及 Ghosh and Li（2013）。

肖老师两篇论文的主文已经用于句子功能、句间推进和引文责任对照。DSDL 在线附录 A–I、ACAA/DSDL 缺失的在线附件与未下载图像不在本地证据中，本终审不声称阅读或视觉核验这些部分。

### 1.2 外部检索

检索覆盖 prospective architecture flexibility、dependency selection、breaking upgrade、library migration、iterative maintainability、long-horizon coding agents、safe architecture evolution、real-options design/exercise 和 cybersecurity mitigation。技术近邻只把论文正文、正式出版页、arXiv 版本页和官方代码或数据仓库作为主要证据。搜索摘要、博客和项目二手介绍没有承担结论责任。

检索截止日为 2026-08-15。快速更新的预印本按版本固定。尤其是 SlopCodeBench 已从[arXiv:2603.24755v1](https://arxiv.org/abs/2603.24755)更新到 v2；v2 的范围为 36 个问题、196 个 checkpoints，而现有 00E 仍记录 v1 的 20 个问题和 93 个 checkpoints。依照“只新增本文件”的任务边界，本终审只记录版本漂移，不改动 00E。EvoCode-Bench 官方仓库在 2026-06-20 说明早期 Harbor verifier 存在泄漏并重新发布数据；因此任何复现实验都必须固定修订后的 manifest，不能沿用此前结果。

## 2. Schober 与 Gebauer 原理论究竟能负责什么

Schober, Franz, and Judith Gebauer. 2011. “How Much to Spend on Flexibility? Determining the Value of Information System Flexibility.” Decision Support Systems 51(3): 638–647. DOI [10.1016/j.dss.2011.03.004](https://doi.org/10.1016/j.dss.2011.03.004)。

原研究的对象是支持业务流程的 IS 成本估值，不是代码生成 agent，也不是 dependency safety。其关键对象与本候选可合法使用的责任如下。

| 原文对象 | 原文中的含义 | C1′ 可合法保留的含义 | 原文不能替 C1′ 承担的内容 |
|---|---|---|---|
| \(x_1\)、flexibility-to-use | 系统初始化时已预见并由系统支持的任务份额 | \(t_0\) 当前功能必须先通过，未来收益不能补偿当前任务失败 | 当前应选哪个包、如何生成 patch |
| \(y\)、FCOST | 是否预先提供 flexibility-to-change，以及为此支付的初始附加投入 | option existence 与当前 incremental premium 必须分开测量 | wrapper、adapter、隔离进程天然就是 option |
| \(x_2\)、UCOST | 初始化时未预见、随后通过修改或升级纳入系统的任务及其成本 | \(t_1\) 必须发生真实状态变化并实际执行 upgrade、replace、quarantine、disable、degrade 或 remove | dependency shock 的发生率、provider 图或代码 action representation |
| \(w_1,w_2,w_3\) | 分别由原始功能、后续改变和系统外人工方式处理的活动份额 | exercise、no-exercise 和系统外处置必须可区分 | 哪一种安全行动应成为最优动作 |
| TCF、TCNF、\(c^*\) | 有无 flexibility-to-change 时的总成本及其差 \(c^*=TCNF-TCF\) | 同任务、同未来状态下比较 with/without-option 后果 | twin network、potential-outcome identification 或因果效应 |
| DTA、ROA、simulation | 在不同风险假设下估值；DTA/ROA采用风险中性，simulation 查看完整分布 | 不能把未来状态压成确定性成本，应报告分布与校准 | 某一种 tail-risk aggregator、POMDP 或 neural architecture 是理论唯一推出的 |

原文数值例中的“确定性估值可能较低”“ROA 在低风险时可能高估”等结论依赖其业务流程参数和估值假设，只能作为测量警示。它们不能被改写为 dependency safety 的普遍方向假设。原文也没有学习数据、表示网络、agent action、代码执行器、hazard 标签或安全结果。

更重要的是，原文把 \(c^*\) 定义为 TCNF 与 TCF 的差，并在结论中说明，只要所用模型提供这两个输入，灵活性价值的计算不依赖具体模型。由此可得：

1. 理论强项是把“当前功能—初始 premium—未来改变—外部处置—有无灵活性”组织成估值账户。
2. 理论不要求 TCF/TCNF 必须由某种神经结构得到。
3. 把 generic world model 的两个 outcome heads 改名为 TCF/TCNF，不会产生新的算法能力。
4. 若研究者用自己定义的 TCF/TCNF 标签训练差值，再以恢复 \(c^*\) 证明理论有效，证据是恒等式回收，不是独立机制验证。

## 3. 救援模型与通用两阶段 POMDP 的精确同构

### 3.1 救援版最强可能形式

令 \(I_0\) 为 \(t_0\) 当时可见的仓库、功能任务、manifest/lock、registry、历史 advisory、测试和执行 trace。令 \(b\) 为 agent 实际生成且通过当前任务的 dependency design，\(b_0\) 为 matched no-option design，\(\omega,\tau\) 为未来状态及发生时间，\(a\) 为 \(t_1\) 行动。

当前 premium 为：

\[
C_0(b)=Cost_{t_0}(b)-Cost_{t_0}(b_0).
\]

未来状态分布为：

\[
p_0(\omega,\tau\mid I_0).
\]

候选 \(b\) 的可行动作集为 \(\mathcal A_b(\omega)\)，其中必须包含 no-exercise。with-option 与 without-option 后果为：

\[
Y^F(I_0,b,\omega,a),\qquad Y^{NF}(I_0,\omega).
\]

在当前任务成功约束下，最强 Schober-centered 决策关系可以写成：

\[
V^{Sch}_0(b\mid I_0)=
-C_0(b)+
\rho_{p_0}
\left[
\max_{a\in\mathcal A_b(\omega)}
U\!\left(Y^F(I_0,b,\omega,a)\right)
-U\!\left(Y^{NF}(I_0,\omega)\right)
\right].
\]

这已经是对原理论最有利的救援形式。它显式保留 option premium、未来不确定性、with/without 后果、可行 exercise 和 no-exercise，也允许任务成功、安全损害、人工负担与计算成本共同进入 \(U\)。

### 3.2 通用模型的逐项对应

构造一个两阶段 POMDP 或 fully observed-after-shock stochastic control model：

| Schober-centered 名称 | 通用序贯决策对象 |
|---|---|
| \(I_0\) 与 \(p_0(\omega,\tau\mid I_0)\) | 初始 belief state |
| 选择 \(b\)、支付 \(C_0(b)\) | \(t_0\) action 与 immediate reward |
| \(\omega,\tau\) | 状态转移与 \(t_1\) observation |
| \(\mathcal A_b(\omega)\) | state-dependent feasible action set |
| exercise/no-exercise | \(t_1\) actions，其中 no-op 是普通动作 |
| \(Y^F,Y^{NF}\) | action-conditioned transition/outcome model |
| TCF/TCNF 或 \(U(Y)\) | return / cost-to-go |
| \(c^*\) 或 \(V^{Sch}_0\) | \(Q_0\) 的动作差或 option advantage |

令：

\[
Q_1(s_1,a)=U(Y(s_1,a)),\qquad
V_1(s_1)=\max_{a\in\mathcal A(s_1)}Q_1(s_1,a),
\]

\[
Q_0(s_0,b)=-C_0(b)+\rho_{p_0}[V_1(s_1)\mid s_0,b].
\]

把 without-option branch 作为基准动作或基准设计减去后，\(Q_0\) 与 \(V^{Sch}_0\) 完全一致。只要两者共享状态、动作、outcome、效用与风险聚合，等价是代数上的，不依赖训练样本足够大，也不依赖 Transformer 是否“碰巧学会”。Temporal GNN 可以编码同一 repo-package-time 图，world model 可以预测同一分支后果，constrained policy 可以使用同一 feasibility mask，Bellman backup 可以执行同一 exercise maximization。

因此，Schober 提供的是**具名 factorization**，并未提供以下任一不可替代对象：

- 通用 POMDP 没有的 latent state；
- 与通用 expected utility 或 optimal stopping 相反的方向；
- 只有理论才定义的可观察标签；
- 改变 attention compatibility、message passing 或 transition operator 的专有关系；
- 通用 action set 无法表达的真实动作；
- 非 Bellman、非 survival、非 causal twin、非 standard calibration 的独立损失。

### 3.3 所谓“方向冲突”仍是一般决策论方向

| 冲突情境 | Schober-centered 预期 | 通用模型是否自然得到 |
|---|---|---|
| hazard 低、未来损害小、direct call 当前便宜 | 不创建昂贵 option | 是。当前成本大于折现后未来收益时由 \(Q_0\) 直接得到 |
| hazard 高、损害大、成熟替代可执行 | 创建 replace/isolate option | 是。未来可行 action 提高 \(V_1\) |
| option 已存在但本次 exercise 成本高于 no-op | 不行使 | 是。no-op 参与 \(\max_a Q_1\) |
| stable/right-censored 窗口 | 支付 premium 但窗口内无 exercise，需防止普遍建 option | 是。校准后的低事件率降低预期 return |
| 不修改即可承受 shock | 报告 robustness，不把它误称 flexibility-to-change | 这是构念分类，可改善解释；动作和结果仍可由通用模型表示 |
| 当前功能与未来可改性冲突 | 在当前成功约束下比较长期 return | 是。constrained MDP 或多目标 policy 的标准形式 |

这些情境对构造评价集很重要，却没有暴露通用两阶段模型的系统性错误。它们都是有限视野决策、可行性约束、最优停止或风险校准的正常结果。

### 3.4 候选损失逐项审查

| 拟议损失 | 实际统计责任 | 是否由 Schober 独有 |
|---|---|---|
| hazard calibration / survival NLL | 从风险集估计 \(p_0(\omega,\tau\mid I_0)\) | 否，属于 survival/competing-risk 学习 |
| premium regression | 预测当前增量成本 | 否，属于 cost model |
| feasibility BCE / ranking | 预测动作是否可执行 | 否，属于 constrained policy 或 affordance learning |
| twin-outcome loss | 预测不同设计与动作的后果 | 否，属于 potential-outcome/world-model 学习 |
| same-task same-shock pairwise loss | 排序实际风险—任务—成本结果 | 否，属于 counterfactual ranking |
| exercise/no-exercise policy loss | 选择 \(t_1\) 行动 | 否，属于 imitation、offline RL 或 Bellman optimization |
| \(TCNF-TCF=c^*\) consistency | 强制估值恒等式 | 代数冗余；若标签也由该式生成则循环 |
| option-state shuffle / pair break | 检验中间状态是否被使用 | 是有价值的消融，但只能证明 factorization 被模型使用，不能证明 Schober 不可被通用模型复制 |

没有剩余的 Schober-specific loss 可以在不循环的前提下产生新方向。若另加 loss 使模型偏好 wrapper、adapter 或 provider diversity，该方向来自研究者的技术启发式或另一理论，不来自 Schober 原文。

## 4. 最强等参数反证及预注册撤题规则

### 4.1 不能只与 raw Transformer 比

raw Transformer 或 raw temporal GNN 可能因缺少中间监督而表现较差。这样的胜利只能说明显式分解、额外标签或训练便利有用，不能排除一般序贯模型。真正有判别力的比较必须包含四层。

1. **S-Schober**：显式具名 \(C_0,p_0,F,Y^F,Y^{NF}\)、exercise/no-exercise 与理论 value relation。
2. **G-Matched-State POMDP**：获得完全相同的中间输入与监督、相同状态维度、相同 action masks、相同 decoder、相同训练样本和 utility，只用普通 Bellman/backward-induction 组合；所有状态使用匿名名称。
3. **A-Anonymous Factorized Model**：相同的 twin branches、hazard head、feasibility head 和参数量，但不加入 \(TCNF-TCF\) 命名或 Schober consistency；由 end-to-end return 和各任务监督学习。
4. **R-Raw World Model**：从相同原始 \(I_0\) 和图输入直接学习两阶段 transition、outcome 与 policy，作为“理论分解是否提升样本效率”的次级检验。

S 与 G 是决定性比较。二者必须共享：

- 相同基础模型 checkpoint、冻结层、LoRA rank 和 trainable parameter 数；
- 相同 \(t_0/t_1\) action space、code decoder 与 verifier；
- 相同中间状态标签、数据量、batch、optimizer、搜索预算和 early stopping；
- 相同 rollouts、tool calls、wall-clock 上限与随机种子集合；
- 相同 repository/package/shock-family 分组；
- 相同风险聚合与 current-task constraint。

### 4.2 精确反例

给定任一 S-Schober 参数化 outcome model，可以令 G 的匿名 state slots 逐一复制 \(C_0,p_0,F,Y^F,Y^{NF}\)，令其 terminal \(Q_1\) 等于同一 \(U(Y)\)，令其 \(Q_0\) 执行同一 \(\rho_{p_0}\) 和 \(\max_a\)。此时对每一个输入：

\[
Q^{G}_0(I_0,b)=V^{Sch}_0(b\mid I_0).
\]

这构成一个等输入、等隐藏维度、等 decoder、且组合层不需要更多参数的模型。若 S 使用无参数的 \(TCNF-TCF\) 与 max 运算，G 使用同样无参数的 Bellman 运算；若 S 把聚合器做成可训练网络，G 可复制该网络并保持参数相等。因而不存在“Schober 结构的表达能力是 G 无法复制”的空间。

可能剩下的经验主张只有两类：

- 理论命名或额外监督改善优化、可解释性或小样本表现；
- 使用 Schober 构念使数据收集者补齐 stable、no-exercise 与 premium。

前者应由样本效率和人类解释实验支持，不能升级为独立理论算法能力；后者是研究设计贡献或 benchmark ontology，不是神经算法的新能力。

### 4.3 必须比较的结果和撤题阈值

主要结果不能只看平均 task success。至少应同时报告：

1. 当前功能成功与回归；
2. shock 后漏洞暴露时长、不可修复率、服务中断、权限或数据损害；
3. \(t_0\) premium、\(t_1\) remediation cost、人工介入与 token/tool/wall-clock；
4. stable-window 的不必要 option 创建率；
5. exercise 适当率与 no-exercise 适当率；
6. hazard、feasibility、with/without outcome 的校准；
7. unseen repository、package family、shock family 和未来时间段；
8. 任务—安全—成本 Pareto frontier，而非以拒绝或一律加 wrapper 获得表面安全。

预注册撤题规则应为：若 G-Matched-State POMDP 在上述主要结果的联合等效界内复制 S-Schober，或 S 的优势只出现在 raw baseline 而不出现在 G/A，则 Schober 的独立算法责任失败。这里无需等待 pilot 才能判定表达同构；pilot 只能检验训练便利，不能推翻精确反例。由于本任务要求理论产生通用替代无法复制的中间状态、方向或约束，C1′ 已在进入实验前触发撤题条件。

## 5. 直接近邻审查

### 5.1 IS 与真实期权的直接近邻

| 工作 | 已核验的核心内容 | 对 C1′ 的挤压 |
|---|---|---|
| Schober & Gebauer 2011，DSS，DOI [10.1016/j.dss.2011.03.004](https://doi.org/10.1016/j.dss.2011.03.004) | 用 DCF、DTA、ROA 和 simulation 比较有无 IS flexibility-to-change 的成本；区分初始 premium 与升级成本 | 提供时间与估值分解，不提供 learned policy；原文还允许任意能产生 TCF/TCNF 的模型 |
| Khan, Zhao, Kumar, and Stylianou 2017，JAIS 18(5):372–402，DOI [10.17705/1jais.00459](https://doi.org/10.17705/1jais.00459) | 区分 real option 的 recognize、value 和 exercise，并研究 IT 投资中的 exercise decision 与管理偏差 | 说明“有 option/value”不等于正确 exercise；Schober 不能单独承担 \(t_1\) 行动机制 |
| Zhang and Babovic 2011，DSS 51(1):119–129，DOI [10.1016/j.dss.2010.12.001](https://doi.org/10.1016/j.dss.2010.12.001) | 结合 real-options valuation、decision analysis、Monte Carlo 与 evolutionary algorithms，搜索相互作用的 option portfolio 和 exercise conditions | “理论到算法、选择 option portfolio、随未来状态自适应行使”早已有直接方法先例；换成 neural world model 不是天然新增贡献 |
| Benaroch 2018，ISR，DOI [10.1287/isre.2017.0714](https://doi.org/10.1287/isre.2017.0714) | 建模序贯、可选的主动不确定性降低措施，处理 impulse effect、替代/互补/协同作用和 path dependence，并应用于 cybersecurity investment | 对主动安全 mitigation、顺序和相互作用的理论责任比 Schober 更直接；C1′ 不能声称“风险下预先创建可行应对路径”本身尚未研究 |
| Ghosh and Li 2013，ISR 24(4):1011–1027，DOI [10.1287/isre.2013.0488](https://doi.org/10.1287/isre.2013.0488) | 为 generalized meta-staged project 建立 real-options 模型并评价 SOA migration | 软件架构迁移与真实期权的结合已有 ISR 直接近邻 |

这组近邻带来两层结论。第一，Schober-centered 研究若只做 option valuation，理论新增空间已经很小。第二，若转向 option portfolio、exercise condition、主动安全 mitigation 或软件迁移，Zhang–Babovic、Benaroch 和 Ghosh–Li 已分别占据核心机制。C1′ 必须证明 coding agent 的代码级行动产生一种这些框架和 generic POMDP 都不能表达的关系；当前方案没有做到。

### 5.2 coding agent、依赖与长期演化的直接近邻

| 工作与版本 | 可公开使用的对象 | 已占据的问题 | 对 C1′ 仍缺的字段 |
|---|---|---|---|
| [DepDec-Bench, arXiv:2601.00205v2](https://arxiv.org/abs/2601.00205) | 2,807 个仓库、40,214 个 PR、117,062 次 dependency changes；论文提出 benchmark roadmap | 当前依赖复用、克制、安全版本和 remediation disruption | 非现成完整训练集；无 \(t_0\) option construction 与隐藏 \(t_1\) exercise |
| [BUMP](https://github.com/chains-project/bump)，SANER 2024，DOI [10.1109/SANER60148.2024.00024](https://doi.org/10.1109/SANER60148.2024.00024) | 571 个 breaking dependency updates、153 个 Java 项目、1,142 个 pre/breaking Docker images，完整镜像约 250GB | 可复放的 post-shock breaking updates | 条件化在事件；无 stable risk set、\(t_0\) 功能任务或 matched boundary twins |
| [SWE-Chain, arXiv:2605.14415](https://arxiv.org/abs/2605.14415) | 9 个 Python packages、12 条 chains、155 个 transitions、1,660 个 grounded requirements | 连续 package release upgrade 的 Build+Fix | 无冲击前 option premium、总体 hazard 或随机化的早期架构 |
| [FreshBrew, arXiv:2510.04852](https://arxiv.org/abs/2510.04852)及[官方仓库](https://github.com/mrcabbage972/freshbrew) | 228 个 Java repositories 的 JDK 8→17 migration，带编译、原测试与 coverage guard | 已发生平台迁移后的 agent 修复 | 无 \(t_0\) option creation；arXiv 与正式项目页结果口径有修订，使用前需固定版本 |
| [PyMigBench](https://doi.org/10.1109/MSR59073.2023.00075) | 官方当前 2.0 资产含 335 个 Python library migrations、3,096 个 migration-related changes；后续 LLM 研究使用其中 321 个 migrations、2,989 个 changes | post-hoc library replacement | 可运行测试只覆盖较小子集；无当时风险集和 matched no-option |
| [EvoCode-Bench, arXiv:2605.24110](https://arxiv.org/abs/2605.24110)及[官方仓库](https://github.com/UniPat-AI/EvoCodeBench) | 26 个任务、227 轮、每任务 5–15 个 stateful steps | inherited code、dependency 与架构对未来需求的影响 | benchmark-designed requirements，不提供生态 shock base rate 或 option twins；需使用 2026-06-20 后修订数据 |
| [SlopCodeBench, arXiv:2603.24755v2](https://arxiv.org/abs/2603.24755) | v2 为 36 个问题、196 个 checkpoints、15 个 agents；评价 regression、verbosity 与 structural erosion | agent 迭代开发的长期退化 | 无 dependency-specific hazard、with/without option 或真实 exercise；00E 的 v1 数值已过时 |
| [Needle in the Repo, arXiv:2603.27745](https://arxiv.org/abs/2603.27745) | 21 个 C++ repository probes、9 个 maintainability dimensions、功能 hidden tests 与 structural oracles | 功能通过但结构不可维护的失败 | 结构结果不是未来依赖冲击，也无 \(t_0\) 概率与 option value |
| [SWE-EVO, arXiv:2512.18470](https://arxiv.org/abs/2512.18470) | 7 个成熟 Python 项目中的 48 个 long-horizon evolution tasks，任务平均涉及约 21 个文件和 874 个测试 | 跨文件长期软件演化 | 无 prospectively sampled dependency risk set 和同 shock twins |
| [Architecture Without Architects, arXiv:2604.04990](https://arxiv.org/abs/2604.04990) | 说明 coding agents 会隐式作出依赖、框架与架构决策 | “coding agent 是架构行动者”已被直接提出 | 研究议程与案例，不提供训练标签 |
| Chondamrongkul and Sun 2023，Science of Computer Programming 230:102978，DOI [10.1016/j.scico.2023.102978](https://doi.org/10.1016/j.scico.2023.102978) | formal architecture model、fitness properties 与 PDDL4J 演化规划，在六个系统上评价 | 安全 architecture-evolution path 的自动规划 | 非 agent、非未知 shock，但必须作为提供架构模型时的强规划基线 |

检索后的新颖性边界已经非常窄：不能把 current dependency choice、post-shock migration、iterative maintainability、implicit architecture decision 或 safe evolution planning作为空白。剩余的技术空白只是“同一 agent 在未知冲击前创建可执行 option，之后在隐藏冲击上实际行使，并按总体风险率学习”。这是一个有价值的数据与评价空白，但 Schober 没有把它转化成不可由 generic sequential learning 复制的理论算法空白。

## 6. \(t_0\) 风险集与 \(t_1\) exercise 的可识别性终审

### 6.1 目标观察单位

能够识别该问题的最小单位不是单个 PR、单个 CVE 或单个 migration patch，而是：

\[
\mathcal U=
(R_{\tau_0},q_0,I_0,\{b^{NF},b^F_1,\ldots,b^F_J\},
\omega_{\tau_1},\mathcal A_{b\omega},
Y_{b\omega a}).
\]

其中所有 \(b\) 必须完成同一 \(q_0\)，在 \(\tau_0\) 时不知道 \(\omega_{\tau_1}\)，并在同一个 sealed shock 上以相同预算执行。风险集还必须从 \(\tau_0\) 向前抽样，包含：

- 后来发生 security advisory、malicious/yanked release、breaking release 或 abandonment 的 event windows；
- 到观察期结束仍未发生目标事件的 right-censored windows；
- 长期 stable windows；
- 正常或 benign upgrade，但没有安全或破坏性冲击的 competing events；
- 事件发生但不行使任何 option 更优的 no-exercise instances。

### 6.2 公开资产只能提供碎片

| 识别要素 | 可用来源 | 当前状态 |
|---|---|---|
| 包—版本—时间风险集 | registry history、deps.dev、OSV/GHSA、release/yank/maintenance metadata | 可以新建，但当前数据库没有现成冻结快照；当前 advisory 页面可能被后写 |
| breaking/security event | BUMP、OSV/GHSA、registry、历史项目 | 可获得；BUMP本身是 \(Shock=1\) 条件样本 |
| post-shock migration | BUMP、PyMigBench、SWE-Chain、FreshBrew、BigBag/Byam 等 | 可获得，但只回答冲击后的 repair |
| same-task with/without option | 无现成公开基准 | 必须让独立 \(t_0\) builder 在看不到 shock 时生成并执行 |
| stable/censored 的真实执行结果 | 无现成 paired rollout | 可以随访当前设计，但稳定窗口只观测 premium/no exercise，不能单独识别反事实收益 |
| action feasibility 与 \(Y_{b\omega a}\) | 容器 build、hidden tests、static/dynamic/security checks | 可以生成，成本高；每一候选必须承受完全相同 shock |
| 自然 prospective shock | 冻结后等待真实生态事件 | 最强但数量、等待期和事件类型不可控 |
| 无参数记忆的隐藏 shock | sealed behavior-equivalent fork | 可构造，但估计对象变为合成机制上的策略，不等同自然生态效果 |

把 BUMP 或 migration corpus 与 OSV 的历史发生率简单 join 不能得到训练真值。事件库中的仓库因“发生且可复现”被选择，stable 项目因测试、维护强度和流行度不同而进入另一选择过程。即使使用 inverse-probability weighting、case-cohort sampling 或 competing-risk hazard，也只能校正已测量的抽样机制，不能补出从未观察的 \(b^F/b^{NF}\) 反事实。

stable/right-censored 样本解决的是 \(p_0(\omega,\tau\mid I_0)\) 和“不应总建 option”的校准问题。它们本身没有 \(t_1\) shock，因而不能验证某个 boundary 真能降低 future harm。event 样本验证 exercise consequence，却只在事件条件下观察。必须从同一个预先冻结风险集中随访两类样本，并在 outcome 公开前构造 variants，才能把二者连成严谨两阶段证据。

### 6.3 数据进入门

只有同时满足下列条件，数据才可称为 paper-grade；当前没有一项已由现成公开资产完整满足。

1. **风险集门**：以 package-family、repository lineage、生态和 \(\tau_0\) 为单位前向抽样；明确 event、stable、right-censored、benign/competing event 及 censor reason。
2. **时间门**：保存 \(\tau_0\) 时真实可见的 registry、advisory、issue、release、documentation 和 dependency graph 快照，而不是用当前网页回填历史。
3. **option 门**：每个 \(b^F\) 必须相对 matched \(b^{NF}\) 在当前任务等效界内，并由真实 \(t_1\) 执行证明新增或显著改善至少一条 action path；名称、LOC、接口数量和 LLM judge 不能作标签。
4. **盲构造门**：variant builder 看不到 future shock；shock builder 看不到 variant identity 与模型分数。两侧 manifest、密钥和进程隔离。
5. **同冲击门**：所有候选受到相同 API、runtime、permission、dependency 或 advisory behavior；不得给 option design 更多 token、测试或外部信息。
6. **独立样本门**：功效分析按 repo、package family、shock family 聚类。一个任务的三个 variants 或一个包的多个 CVE 不能被当作独立样本虚增。
7. **隐藏测试门**：\(t_0\) 和 \(t_1\) 功能、安全、服务状态、数据/权限副作用均由独立 verifier 评估；生成器不得读取 gold patch、future test names 或 oracle output。
8. **许可门**：逐仓库记录 source、commit、license、redistribution 条款、container 与依赖许可证。benchmark 自身开源不自动授权再分发第三方 repo snapshots。

00N 的约 1,500 个配对、约 100 个 package families 只是预冻结规模设想，不是已经有统计依据的下限。真正的样本量应由 pilot 的组内相关、事件率、主要安全结果方差和联合等效界计算。100–200 个事件加多个 variants 可作工程诊断，不能据其 variant 数声称 paper-grade 独立样本。

**数据判定：原则上可新建，当前不可由公开资产直接、严谨、低成本地构造为现成训练集。进入门未通过。**

## 7. 模型记忆与时间泄漏终审

### 7.1 输入时间切分不足以排除记忆

历史 advisory 往往有多个先行信号：issue、PR、patch commit、release candidate、registry publish/yank、maintainer message、GHSA、OSV、NVD 和下游 issue。对每个事件应定义最早公开信号：

\[
\tau_{leak}=
\min(\tau_{issue},\tau_{PR},\tau_{patch},\tau_{release},
\tau_{registry},\tau_{maintainer},\tau_{GHSA},\tau_{OSV},\tau_{NVD}).
\]

\(\tau_0\) 必须早于 \(\tau_{leak}\) 并留预注册 buffer。Git author date、当前网页 affected range 和后来补写的 release notes 都不能自动视为当时可见。这个 protocol 能阻止 forward input leakage，却不能删除基础模型参数中已经记住的 package、CVE、迁移 diff 或典型修复。

### 7.2 三层证据强度

| 层级 | 设计 | 能排除什么 | 仍不能回答什么 |
|---|---|---|---|
| Tier A | 冻结模型、adapter、retrieval index 与 \(t_0\) manifest 后，等待 post-freeze 真实 shock | 最强地排除参数见过具体未来事件 | 需要等待；事件率、分布和样本量不可控 |
| Tier B | 冻结后由独立构造器注入从未存在、行为等价的 sealed shock，并随机化 package/API/symbol | 排除具体事件身份记忆，检验机制泛化 | 外部效度是 synthetic mechanism，不是自然生态发生率 |
| Tier C | 历史事件 identity masking、路径扰动和 advisory 文本删除 | 检查明显的字符串或身份 shortcut | 模型仍可凭代码结构、常见 API 和 patch pattern 识别；不能单独承担主结论 |

主评价至少需要 Tier B，真实生态外部效度需要 Tier A。不断更新、训练截止不透明的云端模型不能承担“未见未来”的 primary test；可以作为工程上限，但必须与冻结 hash 的本地 open checkpoint 分开报告。

### 7.3 必做的记忆与信息流检验

- 对 base model 运行 known-event probe：仅给 \(\tau_0\) 代码，询问 future advisory ID、fixed version、release change 和迁移 diff；命中样本从 primary history replay 移除。
- 运行 shock-identity probe：从 anonymized \(t_0\) feature 或 hidden state 预测具体 shock family/ID；高于预注册阈值说明构造器泄漏。
- 对每个 feature、retrieval document、test、prompt、directory 和 seed 保存 provenance 与最早可见时间；CI 自动拒绝晚于 \(\tau_0\) 的字段。
- 训练、验证和测试按 repository lineage、package family、shock mechanism 与时间联合分组；transitive dependency、fork 和同一 migration family 不能跨 split。
- sealed shock 的模板先由历史机制抽象，具体 symbol、行为参数和 package fork 在模型与 variant 冻结后采样；shock 不得针对某一 boundary 量身设计。
- 所有 checkpoint、adapter、tokenizer、retrieval index、container、registry snapshot、OSV/GHSA export、seed 与 manifest 使用不可变 hash。

**泄漏判定：历史公开资产单独不能严谨隔离模型参数记忆。Tier B 在技术上可执行但改变估计对象，Tier A 尚需前瞻等待。当前进入门未通过。**

## 8. 本地算力、执行成本与可复现性

### 8.1 窄 pilot 可执行

在单一 Java 或 Python 生态中，约 100–200 个诊断性单位、每个单位 2–3 个 \(t_0\) variants、1–2 类 sealed shocks 和有限 \(t_1\) actions，可以用本地容器集群执行。hazard/survival model、temporal GNN 或较小 world model 的训练不是主要瓶颈；7B–14B code model 的 LoRA 或冻结 decoder 条件化在 2–4 张 24/48GB GPU 上也有可行路径。

### 8.2 paper-grade 成本尚未闭合

真正昂贵的是执行数据，而不是增加一个理论 head。

- BUMP 完整 pre/breaking images 已约 250GB；加入 repo snapshots、registry archives、variants、build caches、security traces 和多个生态后应按多 TB 存储规划。
- 571 个事件乘以 3 个 designs、多个 \(t_1\) actions、多个 agent baselines 与随机 seeds，会形成数千至上万条容器构建和 agent rollout。
- 需要隔离网络、package cache、registry mirror、恶意或权限类 shock sandbox、CPU/RAM 配额和可恢复日志。GPU 利用率可能低于容器验证成本。
- 2–4 张 GPU、256–512GB RAM、4TB NVMe 是合理的窄 pilot 配置估计，不是已经实测的 paper-grade预算。跨生态、强 baseline 和功效充足的运行应先用前 20 个单位测量 wall-clock、失败率、重试和缓存命中。
- 变体不是独立样本。即使执行链数量很多，真正统计自由度仍受 repo、package 与 shock family 数量限制。
- 每一项失败都必须区分 agent failure、repository bit rot、dependency unavailable、container failure 和 oracle failure，不能把基础设施错误计入安全改善。

### 8.3 必须留下的工件

若作为基准基础设施继续，至少应发布或内部封存：

- 风险集抽样脚本、事件定义、censor/competing-risk manifest；
- \(\tau_0\) input whitelist、feature lineage 和 \(\tau_{leak}\) 证据；
- repo/package/license manifest 与不可变 commit/container hash；
- blind variant builder 与 sealed shock builder；
- 当前任务、隐藏 \(t_1\) 功能/安全/服务/权限 oracle；
- base-model memory probes 与泄漏测试；
- 模型配置、参数匹配表、seed、训练日志、失败分类和完整结果空值规则；
- 原始执行 trace、构造日志和去标识化后的可再分发数据。

**算力判定：窄工程 pilot 为 GO；ISR 论文所需的多生态、前瞻、独立样本充分且含强等参反证的实验为 CONDITIONAL。算力可行不能覆盖理论 NO-GO。**

## 9. 与肖老师两篇 ISR 论文的逐句逻辑和引文责任对照

### 9.1 不是模仿表面章节，而是检查每一句是否完成闭环

| 肖老师原文锚点 | 该位置的句子逻辑与证据责任 | C1′ 对应句必须完成什么 | 本终审结果 |
|---|---|---|---|
| ACAA-I2/I3/I4 | 先界定具体业务预测任务和既有测量，再指出为什么当前表示遗漏 customer attention；引用分别承担现象、已有方法和限制，不替作者承担新构念 | 先说明 coding agent 在 \(t_0\) 选择依赖并改变 \(t_1\) 可行动作，直接近邻已覆盖 current selection/post-shock migration，再指出唯一遗漏 | 数据与现象空白可以成立；不能据此推出 Schober-specific algorithm |
| ACAA-L10/L11 | 理论先定义 attention 分配与经济后果，再把理论概念压成可计算对象 | Schober 必须先界定 premium、future requirement、exercise/no-exercise 与 with/without cost | 可以完成估值分解 |
| ACAA-T1/T4/T6a-b | 将 customer attention 分到不同计算粒度，并指出理论对 attention 的方向要求 | 必须说明通用模型在哪一种兼容性或聚合方向上系统性错误 | 未完成；generic POMDP 已有相同两时点和最优行动方向 |
| ACAA-M10a/M10b | 不是给普通 attention 加一个分数，而是以 complementary、nonredundant 关系改写 compatibility function | Schober 必须改写 transition、message、attention 或 action selection，使同输入 generic 计算不能等价复制 | 未找到这样的关系；\(TCNF-TCF\) 只是 return difference |
| ACAA-P5.2/P5.3/P5.5 | 数据、基线、任务和多类实验先固定；表值、显著性、权重解释与消融各自承担不同证据强度 | 分开报告风险、任务、成本、校准、机制干预和 OOD，不用外部引用替代自己的执行结果 | 可以设计，但当前数据未构造、实验未运行 |
| ACAA-P6/P7 | 贡献在多组证据之后按概念、方法、经验回收；局限不遮蔽未完成结果 | 只有 matched-state baseline 不能复制且 option state 干预改变行动后，才能声称理论算法贡献 | 解析同构已先否定该条件 |
| DSDL-I3/I5 | 先把预测连到组织资源分配，再精确说明直接深度方法为什么不适合动态、交错、个性化体验 | 说明危险依赖行动对团队维护、安全暴露和服务连续性的后果，并精确承认 DepDec、BUMP、SWE-Chain 等 | 组织后果与近邻边界可成立 |
| DSDL-I6/I7–I9 | 期望不一致理论建立 \(E\)、\(F\)、属性/fragment 和动态累积状态，随后逐一形成研究问题 | 理论必须建立一个不等于 generic belief/action/outcome 的中间状态 | Schober 只把 generic cost-to-go 分项命名 |
| DSDL-T1–T8 | 理论关系逐步收缩为动态期望、体验、signed \(F-E\) 和 cumulative satisfaction，且方向可被标签和时间检验 | 应有明确符号、顺序或冲突方向，删除后产生预期行为变化 | premium 与 future benefit 的差就是一般 return；没有专有方向 |
| DSDL-M15–M23 | \(E\)、\(F\)、\(F-E\) 进入前向表示、对比方向、累积状态和联合损失；理论不是旁路解释器 | theory state 必须进入 code generation 和 action logits，而且通用同状态模型仍不能复制 | 进入 logits 可以做到；不可复制条件做不到 |
| DSDL-E1–E14 | 时间边界、基线、总体预测、中间状态效用、累积机制与消融逐层提供不同证据 | 需将 hazard calibration、twin outcome、no-exercise、state shuffle、pair break 与真实安全结果逐层回收 | 可形成严谨 benchmark 评价，不足以挽救理论独立性 |
| DSDL-C/Z | 方法贡献、管理用途、迁移边界、数据和计算局限都对应已展示证据 | 不得把待运行结果写成完成事实，也不得把基础设施工作量当理论贡献 | 当前只能写内部设计，不能写正式论文贡献 |

ACAA 的关键并非“用了四个 attention 指标”，而是 customer-attention 理论指出普通相似性兼容函数会偏好相近、冗余信息，而理论要求 complementary、nonredundant information，于是方法改写 compatibility。DSDL 的关键也并非“多了几个 loss”，而是期望不一致理论产生相对独立的 \(E\) 与 \(F\)、有方向的 \(F-E\)、随 fragment 推进的 cumulative state，并让这些对象进入前向计算、损失与专门实验。

C1′ 尚无对应句。它可以说 current-fit optimizer 忽略 future shock，也可以说 event-only training 高估 option；前者由加入未来 return 的任何序贯模型修正，后者由正确风险集和 survival calibration 修正。Schober 使研究者记得收集 premium、stable window 和 no-exercise，却没有让一般 POMDP 在相同信息下作出错误方向。依照肖老师原文逐句推进标准，这一差异足以否决理论算法题位。

### 9.2 引文责任必须局部限定

| 引文类型 | 只能支持什么 | 不能支持什么 |
|---|---|---|
| ecosystem advisory、registry、dependency empirical studies | 风险发生、频率、版本和维护现象 | 某个 boundary 是 option，或算法降低了风险 |
| DepDec、BUMP、SWE-Chain、FreshBrew、PyMigBench | 数据单位、任务、post-shock action、可复放范围和直接基线 | Schober 理论、\(t_0\) 因果 option value |
| EvoCode、SlopCode、NITR、SWE-EVO | 长期演化、结构退化与多轮任务的存在 | dependency shock hazard 或真实 exercise |
| Schober & Gebauer | 初始功能/premium、future change、exercise/no-exercise、external path 与 TCF/TCNF 估值关系 | provider graph、twin neural architecture、risk-sensitive POMDP、代码生成器 |
| Khan et al. | recognize/value/exercise 的区分及 IT manager exercise evidence | coding agent 的最优 \(t_1\) policy |
| Zhang & Babovic | algorithmic option portfolio 与 exercise-condition search 的先例 | C1′ 的代码级表现 |
| Benaroch | 主动 mitigation、序列、相互作用与 path dependence 的理论先例 | dependency boundary 的构念效度 |
| Ghosh & Li | real options 与 SOA migration 的直接先例 | 当前 agent 的 prospective safety result |
| 本研究的容器与隐藏测试 | 任务、安全、成本和 action feasibility 结果 | 不能由外部文献代替；未运行时必须留空 |

每个正式句子若以后被保留，都应在逐段审计中明确标记为事实背景、近邻能力、理论关系、设计主张或待运行结果。一个引用不得跨越这些责任。

## 10. 进入门终表

| 进入门 | 判据 | 当前证据 | 判定 |
|---|---|---|---|
| G1 理论新增状态 | Schober 产生 generic two-stage model 不自然拥有的状态或关系 | 所有状态一一对应 belief、cost、transition、action mask、outcome 与 return | **FAIL** |
| G2 方向冲突 | 理论在冲突情境中要求与 generic optimizer 不同的行动 | 低/高 hazard、exercise/no-exercise、premium 权衡均由同一 Bellman policy 得到 | **FAIL** |
| G3 非循环损失 | 存在独有且不由标签恒等式定义的 loss | 候选损失分别归入 survival、cost、feasibility、twin outcome、ranking 或 Bellman；\(TCNF-TCF\) 为恒等式 | **FAIL** |
| G4 最强等参反证 | matched-state generic model 无法在等效界内复制 | 已给出逐输入精确复制构造 | **FAIL，决定性** |
| G5 真实 option 数据 | 同任务、盲构造、同 shock、真实新增 action path | 公开资产无成套 units，需新建 | **UNPASSED** |
| G6 风险集 | event、stable、right-censored、benign/competing events 同源前向抽样 | BUMP/migration corpora为事件条件资产；完整历史快照未建 | **UNPASSED** |
| G7 时间与记忆隔离 | 输入、检索、标签、split、基础模型参数均有隔离证据 | Tier B 可构造；historical-only 不足，Tier A 需等待 | **UNPASSED** |
| G8 数据与许可 | 独立样本、可执行 oracle、license manifest 和可再分发性 | 尚未完成 | **UNPASSED** |
| G9 本地执行 | 窄 pilot 能在受控资源上运行 | 100–200 单位可行；完整规模未实测 | **PILOT GO / PAPER CONDITIONAL** |
| G10 直接近邻后净新增 | 超过 real-options algorithm、mitigation、migration 与长期维护近邻 | 仅余有价值的数据/evaluation gap，无独有理论计算 | **FAIL** |
| G11 肖老师标准 | 理论指出 generic computation 的系统性失配并改写前向关系，随后由分层实验回收 | 只有具名 factorization；无非同构计算 | **FAIL** |

进入门不是多数表决。G1–G4 与 G11 属于理论身份门，任一失败都不得以更多数据、更多模块或更大算力补偿。本候选同时失败。

## 11. 最终处置

### 11.1 对论文题位

**正式结论为 NO-GO。C1′ 不能从 FORMAL-FREEZE 中被 Schober-centered rescue 真正救回。** 不应开始摘要、引言或方法正文，不应把它恢复为三篇博士论文之一，也不应以“理论引导收集了更好数据”替代用户要求的理论驱动算法能力。

该判定不依赖未来 pilot 是否可能得到正向性能。它基于如下不可逆事实：Schober 原理论允许任意能产生 TCF/TCNF 的模型；救援版最强关系与 generic two-stage Bellman recursion 精确同构；直接真实期权近邻已经覆盖 option portfolio、exercise condition、主动风险 mitigation 和软件迁移。继续增加 temporal GNN、world model、twin head 或 decoder 只会增加工程复杂度，不会产生 Schober 独有的计算责任。

### 11.2 可以保留的研究资产

若项目需要，以下工作仍有独立价值，但必须更名和降格，不占用论文一题位。

1. 构建 prospective dependency shock risk set，包含 stable、right-censored 与 competing events。
2. 建立同任务、blind with/without-boundary、same-shock 的可执行 benchmark。
3. 发布模型记忆、\(\tau_0\) feature provenance 和 sealed behavior-equivalent shock 协议。
4. 比较 current-only、event-conditioned 与 population-calibrated agent policy，作为数据偏差或评价方法研究。
5. 将 Schober 仅作为 benchmark ontology 的来源，帮助区分 premium、exercise、no-exercise 和外部处置；不声称它推出神经结构。

这些资产若形成新论文，应重新寻找真正改变学习对象或行动规则的理论，或者坦率定位为软件工程 benchmark/measurement 贡献。它们不能以本候选的原名继续救援。

## 12. 已核验参考文献与版本链接

1. Schober, F., and J. Gebauer. 2011. How Much to Spend on Flexibility? Determining the Value of Information System Flexibility. Decision Support Systems 51(3):638–647. [DOI](https://doi.org/10.1016/j.dss.2011.03.004)。
2. Khan, S. S., K. Zhao, R. Kumar, and A. Stylianou. 2017. Examining Real Options Exercise Decisions in Information Technology Investments. Journal of the Association for Information Systems 18(5):372–402. [DOI](https://doi.org/10.17705/1jais.00459)。
3. Zhang, S. X., and V. Babovic. 2011. An Evolutionary Real Options Framework for the Design and Management of Projects and Systems with Complex Real Options and Exercising Conditions. Decision Support Systems 51(1):119–129. [DOI](https://doi.org/10.1016/j.dss.2010.12.001)。
4. Benaroch, M. 2018. Real Options Models for Proactive Uncertainty-Reducing Mitigations and Applications in Cybersecurity Investment Decision Making. Information Systems Research. [DOI](https://doi.org/10.1287/isre.2017.0714)。
5. Ghosh, S., and X. Li. 2013. A Real Options Model for Generalized Meta-Staged Projects—Valuing the Migration to SOA. Information Systems Research 24(4):1011–1027. [DOI](https://doi.org/10.1287/isre.2013.0488)。
6. Reyes et al. 2024. BUMP. SANER 2024. [DOI](https://doi.org/10.1109/SANER60148.2024.00024)，[官方仓库](https://github.com/chains-project/bump)。
7. DepDec-Bench. arXiv:2601.00205v2. [版本页](https://arxiv.org/abs/2601.00205)。
8. SWE-Chain. arXiv:2605.14415. [版本页](https://arxiv.org/abs/2605.14415)。
9. FreshBrew. arXiv:2510.04852. [版本页](https://arxiv.org/abs/2510.04852)，[官方仓库](https://github.com/mrcabbage972/freshbrew)。
10. EvoCode-Bench. arXiv:2605.24110. [版本页](https://arxiv.org/abs/2605.24110)，[官方仓库及修订说明](https://github.com/UniPat-AI/EvoCodeBench)。
11. SlopCodeBench. arXiv:2603.24755v2. [版本页](https://arxiv.org/abs/2603.24755)。
12. Needle in the Repo. arXiv:2603.27745. [版本页](https://arxiv.org/abs/2603.27745)。
13. SWE-EVO. arXiv:2512.18470. [版本页](https://arxiv.org/abs/2512.18470)。
14. Architecture Without Architects. arXiv:2604.04990. [版本页](https://arxiv.org/abs/2604.04990)。
15. Chondamrongkul, N., and J. Sun. 2023. Software Evolutionary Architecture: Automated Planning for Functional Changes. Science of Computer Programming 230:102978. [DOI](https://doi.org/10.1016/j.scico.2023.102978)。
16. Islam, M., A. K. Jha, S. Nadi, and I. Akhmetov. 2023. PyMigBench: A Benchmark for Python Library Migration. MSR 2023:511–515. [DOI](https://doi.org/10.1109/MSR59073.2023.00075)，[官方数据页](https://ualberta-smr.github.io/PyMigBench/)。

本文件没有报告任何尚未运行的实验结果。所有性能、效应量、显著性和模型优劣均保持为待执行设计；NO-GO 由理论计算同构、已核验直接近邻和当前数据识别条件共同支持。
