# 观察性干预 Warrant 闭合的补丁生成：一种理论驱动的有符号三元图方法

## 摘要

<!-- P01 -->

Coding Agent 能够在仓库级需求上生成多文件补丁，但可见测试通过、模型似然较高或验证器接受并不等同于修改已经支持了需求中的全部行为主张。现有多位置生成、测试增强和补丁筛选提高了候选搜索与验证能力，却通常把需求、修改与可执行观察压缩为补丁级分数。本文依据 Toulmin 的 claim–evidence–warrant 结构与结构平衡理论，提出观察性干预 Warrant 生成器 OIWG（Observed-Interventional Warrant Generator），把行为主张、补丁 hunk 或 coalition 与可见测试组织成带符号三元图。模型将训练期 partial-patch 重放产生的 SUPPORT、REFUTE 与 MISSING 标签、联合必要状态和替代状态编译为边预测、符号三角一致性、强制主张闭合与自然硬负例损失，并在每个完整 hunk 边界更新闭合状态。解码器以最弱未闭合或被反驳的强制主张形成下一 hunk 的条件向量，使理论状态进入新 patch 的生成而非完成后的排序。研究将利用仓库隔离的 SWE-Gym 轨迹训练本地 checkpoint，以 RACE-Bench Lite 的可见 FTP 构造封存后的观察性干预矩阵，并由隐藏 PTP 与官方评价器检验新正确补丁和任务解决。本文目前是一份尚未运行的研究设计；工作区尚无所需数据、容器、自然候选池、干预执行器或模型权重，因而文中只给出可执行方法与可证伪证据责任，不陈述任何自有经验结果。

## 1. 引言

<!-- P02 -->

仓库级代码代理正在从局部补全工具转变为能够理解功能需求、定位多处实现并提交可执行改变的软件行动系统。真实功能添加要求补丁同时满足显式需求、隐含约束和既有行为，因此单次 patch 是否正确会直接影响返工、审查与交付可靠性（Jimenez et al. 2024; Liu et al. 2026a）。RACE-Bench 收集了 12 个开源仓库中的 528 个功能添加任务，并为每题配置可执行补丁评价与结构化中间推理；其报告的代理解决率从约 29% 到 70% 不等（Liu et al. 2026a）。SWE-RPG 又把需求澄清、实现计划和代码生成置于同一评价链，显示隐含需求恢复仍是多种代理轨迹的主要失败来源（Zhou et al. 2026）。对开发组织而言，能够在生成阶段辨认哪些行为主张尚未被修改支持，可能同时改变正确补丁的产生率、审查所需证据和错误修改进入代码库的风险。

<!-- P03 -->

一个仓库级任务通常从 issue 或 Feature Request 开始，代理读取基础仓库与测试，随后逐步生成跨文件差分。每个 hunk 改变局部实现，多个 hunk 又可能共同建立接口、传播数据、更新调用者并保持回归行为。可见测试把部分行为转化为执行观察，但同一通过结果可能来自完整实现、偶然覆盖、过度拟合或彼此抵消的修改。代理在普通 beam 中主要依据 token likelihood 延伸 patch，在测试增强搜索中主要依据可见执行反馈保留候选，在 posthoc verifier 中则依据完成补丁的综合得分作选择。需求主张、修改责任与测试观察因此位于同一工作流，却没有必然在同一个生成状态中被连接。

<!-- P04 -->

最直接的正确性代理是可见测试通过数、补丁似然和完成后验证分数。RACE-Bench 报告，能够应用但最终测试失败的补丁相较成功补丁具有更低的中间推理召回和更多过度预测，说明表面可执行与需求实现之间存在可观察断层（Liu et al. 2026a）。固定测试也可能遗漏行为边界，Agent-CoEvo 因而把代码与测试补丁共同演化；Issue2Test 与 Otter 则从 issue 生成复现测试或验证测试（Li et al. 2026; Nashid et al. 2025; Ahmed et al. 2025）。这些进展扩大了约束或增强了观察，却仍可能把一个补丁视为单一对象：它们通常不表示哪条主张由哪组 hunk 通过哪项观察获得支持，以及某项局部修改是否稳定损害另一主张。若这种压缩系统性偏向“更多通过但仍有未闭合或被反驳主张”的 patch，生成目标的方向就需要改变，而不仅是增加一个评分器。

<!-- P05 -->

现有工作已经提供了三个相邻但不可替代的能力群。MultiMend、MultiFixer、SynFix、CascadeFix 与 SiblingRepair 分别推进了多 hunk 生成、协调式修复、依赖关系传播、级联计划和语义 sibling 一致修改（Gharibi et al. 2026; Hu et al. 2026; Tang et al. 2025; Zhang et al. 2026a; Liu et al. 2026b）。IBugFinder 枚举 partial-patch powerset 并区分可分与不可分多 hunk bug，TRIM 则利用代理轨迹和 delta debugging 去除冗余编辑（Xin et al. 2024; Mathai et al. 2026）。SpecRover、SWE-Gym verifier 及相关 APCA 方法又从意图、轨迹或执行结果评估完成补丁（Ruan et al. 2025; Pan et al. 2025）。这些能力分别回答“怎样改多处”“哪些修改可删”和“哪个完成补丁更可信”；本文考察的缺口更窄：带方向的主张—修改—观察状态能否在生成尚未完成时改变下一处编辑，并产生相同预算普通搜索池中不存在的新正确补丁。

<!-- P06 -->

Toulmin 论证模型为这一缺口提供第一层理论结构。一个行为 claim 陈述软件在给定触发、主体与范围下应呈现的可观察结果，测试执行提供与该 claim 相关的数据或 evidence，而 warrant 说明为何该观察能够支持该主张（Toulmin 1958）。在代码修改情境中，hunk 本身并不等同于 Toulmin 的 warrant；它是使可执行观察发生的 implementation backing，claim–test 的规范关系与 hunk/coalition–test 的观察效应共同限定 warrant 是否闭合。由此，一个“测试通过”的孤立事实不足以表示实现责任：模型还需要说明通过结果与哪条 claim 对齐、哪组修改使该结果成立，以及修改是否同时造成反向观察。这个映射把普通 patch–test 矩阵扩展为 claim、implementation backing 和 executable observation 三类对象。

<!-- P07 -->

结构平衡理论为三类对象的方向一致性提供第二层计算约束（Cartwright and Harary 1956）。G-FINDER 将 Toulmin 的 claim、evidence 与 warrant 联同结构平衡操作化为带符号三角，从而使理论决定中间图结构和评分，而非只为特征命名（Lee and Ram 2024）。迁移到补丁生成，claim–test 边表示测试对主张的规范性观察方向，coalition–test 边表示在冻结补丁、测试与环境下加入该 coalition 产生的稳定 fail→pass 或 pass→fail 变化，coalition–claim 边表示模型预测的实现责任。当三边符号乘积为正时，它们形成方向一致的观察性闭合；当乘积为负或任一必需边缺失时，主张保持被反驳或未闭合。该结构允许“增加可见通过数却破坏另一主张”的自然候选成为训练硬负例，并使搜索方向可能与似然、覆盖数或短 diff 相反。

<!-- P08 -->

本文据此提出四个递进研究问题。RQ1 询问自然代理补丁中，针对同一 claim/test 分量的联合必要 hunk 与稳定 SUPPORT–REFUTE 拮抗是否达到足以影响生成的频率。RQ2 询问仓库隔离训练能否从 issue、可见测试与候选差分预测 SUPPORT、REFUTE 和 MISSING，并保留 JOINT_ONLY、SUBSTITUTABLE 与不可识别状态。RQ3 询问符号三角一致性、强制主张闭合和最弱主张驱动解码能否生成普通等预算 completed-patch pools 之外的新正确 patch，而不是重新排列既有候选。RQ4 询问这种新生成能力能否提高隐藏官方任务解决，并在同分量定向 edge neutralization、rewire 与 sign-shuffle 下按理论预期消失。

<!-- P09 -->

为回答这些问题，本文设计 OIWG 的五段前向链。第一，受约束 claim constructor 从 issue、可见 FTP 源码及修复前失败输出生成原子行为主张，并由 claim–test aligner 建立规范观察边。第二，训练期 hunk atomizer 与 coalition runner 对普通 beam 的自然候选执行重复 partial-patch 重放，形成带 SUPPORT、REFUTE、MISSING 和联合关系的监督。第三，signed warrant graph encoder 联合表示 claim、hunk/coalition 与 test，edge heads 预测有符号责任，closure recurrence 在每个 hunk 边界更新强制主张状态。第四，本地代码模型在 patch NLL 之外共同优化边分类、结构平衡、闭合、联合状态和自然硬负例目标。第五，hunk-level decoder 以最弱未闭合或被反驳主张形成下一 hunk 条件，并在无法闭合时输出 abstain 及可审计 warrant state。

<!-- P10 -->

经验设计将把训练、生成和最终评价严格分层。SWE-Gym 的 2,438 个真实可执行 Python 任务及公开轨迹将提供与 RACE 外测仓库隔离的自然候选和干预监督；SWE-RPG 的公开需求澄清记录只在去除仓库重叠后承担 claim constructor 的训练与诊断责任（Pan et al. 2025; Zhou et al. 2026）。RACE-Bench Lite 的 20 题将用于封存前的 schema、容器和 hunk 原子化调试，另 80 题构成不替换的外部评价分母；隐藏 PTP 与官方结果将在所有生成输出、可见干预矩阵和归因臂封存后才被读取。研究只有在自然有符号联合机制、仓库留出可学习性、基线池外新正确 patch 与官方任务解决同时出现时，才可能支持一个独立章节。当前缺少数据、Docker 环境、生成器、候选池、干预 runner 和本地 checkpoint，所以下文的方法、实验与贡献均是待执行和可被证伪的设计承诺。

## 2. 文献基础与研究定位

### 2.1 仓库级任务、需求与执行评价

<!-- P11 -->

仓库级基准首先建立了从自然语言问题到可执行软件改变的外部结果责任。SWE-bench 以真实 GitHub issue、基础提交和测试补丁判断候选是否解决任务，SWE-Gym 进一步提供可用于训练代理和 verifier 的真实任务、环境与轨迹（Jimenez et al. 2024; Pan et al. 2025）。RACE-Bench 将焦点收紧到功能添加，并在最终 patch correctness 之外提供 Concept、Goal、必要文件、实体与步骤等结构化推理参照；其 Lite 子集包含按难度选择的 100 题（Liu et al. 2026a）。SWE-RPG 则以 31 个 Python 与 Java 仓库的 163 个任务连接需求澄清、计划和代码生成，为显式与隐式需求恢复提供独立诊断材料（Zhou et al. 2026）。这些基准共同说明最终通过仍是外部软件结果，同时也提供了把需求理解与实现过程分层研究的公开基础。

### 2.2 测试增强、意图推断与补丁验证

<!-- P12 -->

第二类研究改善了补丁搜索可用的行为约束和完成后判断。Issue2Test 从 issue 生成能够复现问题的失败测试，Otter 从 issue 生成验证 patch 的测试，Agent-CoEvo 进一步让代码候选与行为约束共同演化（Nashid et al. 2025; Ahmed et al. 2025; Li et al. 2026）。SpecRover 在仓库搜索中推断局部意图，并由 reviewer 协调自然语言需求、测试与 patch；SWE-Gym 也利用代理轨迹训练 verifier（Ruan et al. 2025; Pan et al. 2025）。这些方法可以揭示固定测试遗漏的约束，或从完成池中挑出更可信候选。它们构成 OIWG 的强替代：若同样收益能由测试增强或 posthoc verifier 在合法 baseline pool 上复制，则 signed closure 只具有诊断价值，不构成新的生成能力。

### 2.3 多位置生成与关系化修复

<!-- P13 -->

多位置自动修复已经发展出丰富的结构先验。MultiMend 微调代码模型并结合上下文增强与 multi-hunk 组合，MultiFixer 以 coordinator–proposer 组织多位置分析、生成和两阶段 refinement（Gharibi et al. 2026; Hu et al. 2026）。SynFix 构建类、函数、变量及依赖的 RelationGraph 并同步修改邻接组件，CascadeFix 以 Use、Copy 和 Nearby 关系聚类 bug 后作级联计划与生成（Tang et al. 2025; Zhang et al. 2026a）。SiblingRepair 搜索语义 sibling 并采用同步与迭代两种策略形成一致 patch（Liu et al. 2026b）。这些方法已经覆盖“关系图引导多 hunk”和“多处修改需协调”的一般主张，因此本文的图拓扑或 multi-hunk 输出本身不构成新颖性；必须由自然负边、同分量联合状态、理论专属损失和生成期闭合操作共同产生不可替代结果。

### 2.4 Partial-patch 干预与最小化

<!-- P14 -->

第三类工作直接威胁 hunk rollback 的方法身份。IBugFinder 从开发者 patch 枚举所有 partial-patch 子集，识别 divisible 与 indivisible multi-hunk bugs，并总结八类 partial-patch 关系（Xin et al. 2024）。TRIM 沿代理 trajectory→file→edit 层次最小化最终修改，并以 DD-Hunk 作为确定性比较，说明反事实删改能够有效去除无功能贡献的编辑（Mathai et al. 2026）。RACE-Bench 自身也用 file ablation 标注必要文件（Liu et al. 2026a）。因此 powerset、rollback、ddmin、最小 patch、联合 hunk 或“某 hunk 对测试必要”在本文中只承担训练标签与强基线责任；若 OIWG 最终只是复现这些子集关系，理论包装没有增加独立能力。

### 2.5 理论驱动算法与可计算缺口

<!-- P15 -->

信息系统研究表明，理论可以直接改变算法的标签本体、结构与搜索。TheoryOn 先以行为本体规定 construct、关系、antecedent 与 consequent 的抽取任务，再据此组织学习流程；G-FINDER 则从 Toulmin 与结构平衡推导 signed triangle 及结构分数（Li et al. 2020; Lee and Ram 2024）。ACAA 让顾客注意的及时性、语义多样性、投票意识和模态适应分别进入专门注意运算，DSDL 把期望、体验、不确认与累计满意度转为跨视图注意、对比目标和双向稀疏约束（Chen et al. 2024; Chen et al. 2023）。这些先例共同给出本文的设计标准：理论需要创造普通 patch scorer 不会自然生成的中间状态，并同时改变监督、结构、损失与推断。本文的可计算缺口因而不是“补丁缺少解释”，而是自然 signed joint warrant 能否成为一个可学习且能生成新正确 patch 的中间决策状态。

## 3. 理论推导与可证伪命题

### 3.1 Claim、Observation 与 Implementation Backing

<!-- P16 -->

设任务 \(i\) 的可见输入为 \(x_i=(q_i,R_i,T_i^F,o_i^0)\)，分别表示 issue 或 Feature Request、基础仓库快照、可见 FTP 测试源码与修复前失败输出。claim constructor 将 \(x_i\) 转为行为主张集合 \(C_i\)，每条 claim 描述触发条件、行为主体、预期可观察结果、极性与作用范围。对 \(c\in C_i\) 与 \(t\in T_i^F\)，规范边 \(a_{ct}\in\{-1,0,+1\}\) 表示该测试的通过或失败是否能够支持具有相应极性的 claim。候选 patch 被原子化为 hunk 集合 \(H_i\)，coalition \(K\subseteq H_i\) 是使某一观察发生的 implementation backing。OIWG 所称 warrant closure 是 \(a_{ct}\)、coalition 对测试的观察效应和 coalition 对 claim 的预测责任相互一致，而不是把代码片段直接称为论证规则。

<!-- P17 -->

理论结构首先改变 claim 标签本体。每条记录包含 \(claim\_id, trigger, subject, expected\_observable, polarity, scope, source\_span, ftp\_observability, unresolved\_reason\)，并由来源 span 保持到可见输入的可追溯性。显式需求且至少被一项 FTP 规范观察的 claim 形成强制闭合集合 \(C_i^M\)；缺少白名单依据的内容记为 UNRESOLVED，缺少可见测试观察的显式要求记为 UNOBSERVED。后两类仍进入审计与 abstain 状态，但不允许用隐藏 PTP、Reference Reasoning 或 Gold Patch 补写。TheoryOn 式“先冻结本体再选择模型”在此改变了训练输出和终止条件：模型必须区分已支持、被反驳、缺失与不可观察，而不能把未见证据当成反例（Li et al. 2020）。

### 3.2 有符号三角与观察性干预边界

<!-- P18 -->

对训练期 coalition \(K\) 与测试 \(t\)，重复执行产生 \(\delta_{Kt}\in\{-1,0,+1,\bot\}\)：加入 \(K\) 使对齐测试稳定 fail→pass 时为 \(+1\)，稳定 pass→fail 时为 \(-1\)，无稳定变化时为 \(0\)，执行不可识别时为 \(\bot\)。edge head 预测 coalition 对 claim 的责任 \(\rho_{cK}\in[-1,1]\)，并以
\[
b_{cKt}=a_{ct}\,\delta_{Kt}\,\rho_{cK}
\]
表示三边方向一致性。对所有非 MISSING 且可识别三角，\(b_{cKt}>0\) 表示结构平衡；\(b_{cKt}<0\) 表示 coalition 的测试效应与其 claim 责任发生冲突。普通全正 coverage 会把反向效应吸收为覆盖不足，而 signed triangle 保留“某 hunk 提高一个观察却破坏另一个 claim/test 分量”的方向信息。

<!-- P19 -->

上述 \(\delta_{Kt}\) 只是在冻结 patch、测试和执行环境下观察到的干预差异。single-hunk removal 最多说明该 hunk 对这一次完整候选和测试结果具有条件必要性，不能排除替代实现、hunk 交互、偶然覆盖、测试缺口或环境波动。标签因而使用互斥的 SUPPORT、REFUTE 与 MISSING，并另存 INDIVIDUAL_WITNESS、JOINT_ONLY、SUBSTITUTABLE、NON_IDENTIFIABLE 与 INFRA。两个以上 hunk 只有共同加入才形成稳定变化时记为 JOINT_ONLY；多个不相容 coalition 均可形成同一变化时记为 SUBSTITUTABLE。观察性限定使 rollback 负责产生监督，而语义正确性仍由封存后的隐藏官方评价承担。

### 3.3 命题与设计要求

<!-- P20 -->

理论推导形成四项可证伪命题。命题 1 预期自然失败候选中会出现稳定 REFUTE/ANTAGONISTIC，并与同一 claim/test 分量的联合必要 hunk 共存；若边几乎全正，模型将退化为 minimum-claim coverage。命题 2 预期 repo-held-out edge model 能同时识别 SUPPORT、REFUTE 与 MISSING；若 MISSING 被误当负类或跨仓库不可学，闭合状态没有部署基础。命题 3 预期 signed closure 在 hunk 边界改变 token 条件分布并产生 baseline completed-patch pools 之外的新正确 hash；若只改变最终选择，它等价于 verifier。命题 4 预期定向 neutralization、rewire 与 sign-shuffle 会消除相应生成和官方结果优势；若破坏理论边后效果保持，性能来源不在 warrant 结构。

<!-- P21 -->

四项命题要求理论逐项进入算法关键路径。标签层保留三类边、联合与替代状态；表示层使用 claim、hunk/coalition 与 test 三类节点和有符号关系；学习层联合优化 edge、balance、closure 与自然硬负例；推断层在每个 hunk 边界以最弱未闭合 claim 条件化下一编辑。与之对应的最强替代依次是 all-positive minimum coverage、同参数 sign-agnostic graph、直接三分类但无 closure 的 generic graph，以及读取相同 completed-patch pool 的 posthoc verifier。只有理论方法同时越过四类替代并改善隐藏官方软件结果，才能把复杂中间工件解释为必要设计，而不是绕行实现显而易见的覆盖或筛选。

| 理论要求 | 可计算对象 | 专门运算 | 主要反事实 |
|---|---|---|---|
| 主张、观察与 backing 分离 | claim / coalition / test typed graph | 来源约束 constructor 与三类节点编码 | patch–test 二元矩阵 |
| 支持与反驳保留方向 | SUPPORT / REFUTE / MISSING | signed edge heads 与 triangle balance | all-positive coverage |
| 联合必要与替代实现 | coalition hyperedge 与 relation status | coalition encoder 与 status loss | independent hunk ablation |
| 未闭合主张改变生成 | boundary closure state | weakest-claim recurrence 与 constrained decode | posthoc rerank/verifier |

## 4. OIWG 方法

### 4.1 总体架构与输入输出

<!-- P22 -->

OIWG 接收部署白名单内的 issue、基础仓库、可见 FTP 源码与修复前失败输出，输出一个可应用 patch、ABSTAIN 或达到预算上限时的未闭合状态报告。基础生成器将采用可本地加载的 7B 代码模型，运行清单在训练前固定模型与 tokenizer revision；主设计以 Qwen2.5-Coder-7B-Instruct 为可行起点，并允许在任何 RACE 输出可见前以同规模开放模型作一次预注册替换。代码模型通过 rank-32 LoRA 更新 attention 与前馈投影，signed graph 使用 512 维节点接口、四层八头 typed attention、edge/status heads 和一个 claim-wise closure GRU。图状态不会替代语言模型，而是在每个完整 hunk 边界形成一个理论条件向量，注入下一 hunk 的 cross-attention 与 beam score。最终 checkpoint 合并 LoRA、graph encoder、edge heads、closure recurrence、claim constructor 和 decoder 参数，使其能够在没有训练期干预矩阵的仓库任务上独立生成。

### 4.2 Gold-free Claim Constructor 与 Claim–Test 对齐

<!-- P23 -->

claim constructor 是一个本地训练的 constrained encoder–decoder，而不是运行时提示词模板。训练输入只包含公开 issue、可见测试文本和基础仓库静态事实；外部监督来自去除 RACE 仓库重叠后的 SWE-RPG requirement-clarification 记录，以及由测试名、assertion、fixture 和 issue source span 确定性形成的弱对齐对（Zhou et al. 2026）。decoder 通过有限状态 schema mask 依次产生 trigger、subject、expected observable、polarity、scope 与 source span，无法从输入定位的槽位只能输出 UNRESOLVED。claim–test aligner 对 claim 表示与测试的名称、断言、fixture、失败签名和静态触达表示作 biaffine 匹配，输出方向 \(a_{ct}\) 及 observability 概率。RACE 的 Reference Reasoning 不参与 constructor 训练；20 题调试单元也只在输出封存后审计 claim recall、overprediction 和来源可追溯性。

### 4.3 Hunk 原子化与 Coalition 表示

<!-- P24 -->

训练标签来自普通生成器产生的自然 completed patches。每个候选先用零上下文 unified diff 形成初始 hunk，再依据重叠行区间、同一语法节点和不可分编译依赖按冻结规则合并，得到 \(H=\{h_1,\ldots,h_J\}\)。当 \(J\le4\) 时，runner 执行含完整 patch 在内的全部非空 coalition；当 \(J>4\) 时保留候选并标记 NON_IDENTIFIABLE，而不是截断为有利的四块。hunk 表示连接修改前后代码、文件/符号位置、编辑类型与生成顺序，coalition 表示由置换不变 attention 汇聚成员并附加成员数、跨文件跨度和执行身份。该 coalition encoder 使 JOINT_ONLY 与 SUBSTITUTABLE 成为显式 hyperedge 状态；部署图 \(\widehat{\mathcal K}_{\le j}\) 固定包含当前 \(j\) 个 singleton hunk，并由冻结的 autoregressive pointer proposal head 仅凭当前 hunk hidden states 逐槽产生至多 16 个非 singleton coalition：每槽按递增 hunk ID 选择成员后输出 STOP，重复集合被删除，等分时按成员 ID 序列破平。因此部署不枚举 powerset，也不执行 rollback 或测试探测。

### 4.4 Signed Claim–Hunk–Test Graph

<!-- P25 -->

任务图记为 \(\mathcal G_i=(V_i,E_i)\)，节点集合由 claim \(C_i\)、hunk \(H_i\)、coalition \(K_i\) 与 visible test \(T_i^F\) 构成。静态边包括 claim 的 source span、claim–test 规范对齐、hunk 的文件/符号位置、test 的静态触达与 hunk–coalition membership；训练期动态边包括 coalition–test 的重复执行效应和由其诱导的 SUPPORT、REFUTE 或 MISSING。每条边同时保存 type、direction、sign、observed/predicted 标志、repeat stability 与 identifiability mask。claim–hunk 责任在部署时由模型预测，coalition–test 的真实观察边只存在于训练和封存后审计图中。图的计算单位因此是可见规范、实现 backing 和执行观察的 typed component，而不是把 RACE 的参考文件或 Gold Patch 位置转成节点标签。

### 4.5 Signed Warrant Graph Encoder

<!-- P26 -->

不同节点先由专属投影进入共同的 512 维空间。对第 \(\ell\) 层节点 \(v\)，typed signed attention 更新为
\[
\mathbf h_v^{\ell+1}
=\operatorname{LN}\!\left[
\mathbf h_v^\ell+
\sum_{r\in\mathcal R}\sum_{u\in\mathcal N_r(v)}
\alpha_{uvr}^{\ell}
\mathbf W_{r}^{\ell}
\big(\mathbf h_u^\ell+\mathbf e_{\operatorname{sign}(u,v)}+\mathbf e_{\operatorname{obs}(u,v)}\big)
\right],
\]
其中 \(\alpha_{uvr}^{\ell}\) 由关系专属 query/key、边方向与 identifiability mask 共同计算。四层均保留反向消息，使 test observation 能影响 claim 状态，也使 claim polarity 能调节 hunk responsibility。coalition 节点先从成员 hunk 汇聚，再与 claim 和 test 交换消息；missing edge 使用独立 epistemic embedding 而不使用负号 embedding。实现将保存每层 attention、relation basis 和 sign embedding，以支持 edge rewire、sign shuffle 和等参数关系替换。

### 4.6 Edge、Status 与 Responsibility Heads

<!-- P27 -->

对每个可识别三元组 \((c,K,t)\)，edge head 以 \([\mathbf h_c,\mathbf h_K,\mathbf h_t,\mathbf h_c\odot\mathbf h_K,\mathbf h_K\odot\mathbf h_t]\) 输出
\[
\widehat{\mathbf p}_{cKt}
=\operatorname{softmax}\{f_{\mathrm{edge}}(c,K,t)\}
\in\Delta^{\{\mathrm{SUPPORT},\mathrm{REFUTE},\mathrm{MISSING}\}}.
\]
第二个 head 在 INDIVIDUAL_WITNESS、JOINT_ONLY、SUBSTITUTABLE 与 NON_IDENTIFIABLE 间预测关系状态，INFRA 只作为 execution mask 而非可学习语义类；P24 的 pointer proposal head 在训练时以观察到的 JOINT_ONLY/SUBSTITUTABLE 集合作 teacher-forced targets，并与该 status head 共用 \(\mathcal L_{\mathrm{status}}\)。claim–coalition responsibility \(\widehat\rho_{cK}\) 由 sign-bounded MLP 输出，并由所有与 \(c,K\) 相连的可识别测试共同监督。三分类使用按训练仓库冻结的 class-balanced loss，逐类报告 precision/recall；MISSING 保持第三类，既不与 REFUTE 合并，也不用于补足自然负边。

### 4.7 Claim Closure Recurrence

<!-- P28 -->

生成到第 \(j\) 个 hunk 边界时，模型只使用当前 prefix 的预测边更新每条 claim。令
\[
s_c^{(j)}=\operatorname{LSE}_{K\in\widehat{\mathcal K}_{\le j},t}
\log \widehat p_{cKt}(\mathrm{SUPPORT}),\qquad
r_c^{(j)}=\max_{K\in\widehat{\mathcal K}_{\le j},t}
\widehat p_{cKt}(\mathrm{REFUTE}),
\]
并令 missing mass \(m_c^{(j)}\) 为与该 claim 相连三元组的平均 MISSING 概率。closure recurrence 计算
\[
\mathbf u_c^{(j)}
=\operatorname{GRU}\!\left(
\mathbf u_c^{(j-1)},
[s_c^{(j)},r_c^{(j)},m_c^{(j)},\mathbf h_c,\mathbf h_{h_j}]
\right),\qquad
q_c^{(j)}=\sigma(\mathbf w_q^\top\mathbf u_c^{(j)}).
\]
其中 \(\widehat{\mathcal K}_{\le j}\) 是 P24 的有界预测 coalition 集而不是全部子集。训练目标把可观察 mandatory claim 在存在稳定支持 coalition、没有同分量 refute 且完整候选通过相应 FTP 时标为 closed；联合必要 claim 只有在共同 coalition 出现后才能闭合。该递推使先前 hunk 的支持可以被后续 refute 重新打开，而普通累计 coverage 只能单调增加。

### 4.8 理论驱动的联合损失

<!-- P29 -->

OIWG 的总目标为
\[
\mathcal L=
\mathcal L_{\mathrm{LM}}
+\lambda_e\mathcal L_{\mathrm{edge}}
+\lambda_s\mathcal L_{\mathrm{status}}
+\lambda_b\mathcal L_{\mathrm{balance}}
+\lambda_c\mathcal L_{\mathrm{closure}}
+\lambda_h\mathcal L_{\mathrm{hard}}
+\lambda_d\mathcal L_{\mathrm{decode}}.
\]
\(\mathcal L_{\mathrm{LM}}\) 对自然 patch token 作 teacher forcing；\(\mathcal L_{\mathrm{edge}}\) 学习三类边，\(\mathcal L_{\mathrm{status}}\) 联合学习 coalition 状态与 pointer proposal；\(\mathcal L_{\mathrm{balance}}\) 对非 missing 三角惩罚预测 sign product 与观察方向不一致；\(\mathcal L_{\mathrm{closure}}\) 对每个 hunk 边界和 terminal mandatory claim 施加二元交叉熵及 hole penalty；\(\mathcal L_{\mathrm{decode}}\) 模仿训练图中优先降低最弱 claim deficit 的下一 hunk。各 \(\lambda\) 只在仓库留出开发集上选择并在 RACE 前固定；同一开发集同时检查 patch NLL、edge macro-F1、closure calibration 与 hunk action accuracy，避免用单一终端分数隐藏理论头失效。

### 4.9 自然硬负例与非理论替代

<!-- P30 -->

\(\mathcal L_{\mathrm{hard}}\) 专门编码理论预期的方向冲突。对同一任务中可见 FTP 通过数增加、但仍含 mandatory refute 或 unclosed claim 的自然 patch \(p^-\)，以及没有该冲突的自然 patch \(p^+\)，模型施加
\[
\mathcal L_{\mathrm{hard}}
=\max\{0,\gamma-S_\theta(p^+)+S_\theta(p^-)\},
\]
其中 \(S_\theta\) 是生成期 closure-aware score，配对在任何隐藏评价可见前由 visible matrix 冻结。最强非理论图替代保留相同节点、层数、隐藏维度、LoRA rank 与参数预算，但将 sign 和 triangle loss 替换为额外的普通 message-passing/MLP 参数；另一替代直接训练三分类 edge，却删除 balance、closure recurrence 与 hunk action loss。若这些模型达到相同新 patch 与 official resolved，理论专属复杂性将没有实质贡献。

### 4.10 Hunk-Level Constrained Decoder

<!-- P31 -->

在 hunk \(j\) 完成后，decoder 依据 mandatory mask 计算 claim focus：
\[
\alpha_c^{(j)}
=\operatorname{softmax}_c
\left\{\tau\left[
\mathbf 1(c\in C^M)(1-q_c^{(j)})+r_c^{(j)}
\right]\right\},\qquad
\mathbf g_j=\sum_c\alpha_c^{(j)}\mathbf h_c .
\]
\(\mathbf g_j\) 通过 gated cross-attention 注入下一 hunk 的 token hidden states，并形成 beam 分数
\[
B(y_{\le j})=
\frac{\log p_{\mathrm{LM}}(y_{\le j}\mid x)}{|y_{\le j}|^\eta}
-\beta_c\sum_{c\in C^M}(1-q_c^{(j)})
-\beta_r\sum_{c\in C^M}r_c^{(j)}
-\beta_m\sum_{c\in C^M}m_c^{(j)} .
\]
beam 只在完整 hunk 边界比较 closure state，hunk 内仍执行标准 token expansion；这避免把不完整语法片段误当可干预单元。ordinary、diverse、test-augmented 与理论 beam 共享底模、输入、最大输出 token、completed candidates、forward-pass、FTP 和墙钟预算，因而任何新 hash 都来自搜索条件改变，而不是额外采样。

### 4.11 终止、ABSTAIN 与部署推断

<!-- P32 -->

EOS 只有在全部可观察 mandatory claim 的 \(q_c\) 超过开发集冻结阈值且 refute 概率低于阈值时才是无罚终止；仍有 UNOBSERVED mandatory claim、持续 MISSING 或预算耗尽时，decoder 可以输出 ABSTAIN 及未闭合 claim 列表。一次部署推断依次执行 claim construction、visible-test alignment、普通仓库编码、hunk-by-hunk 生成、预测图更新和 terminal check。它不执行训练期 coalition powerset，不逐候选 rollback，也不读取 RACE intervention matrix；可见 FTP 只按与基线相同的常规验证预算运行。输出 manifest 保存 patch hash、每个 hunk 的 focus claim、预测 signed edges、closure trace、停止原因与实际成本。由于 \(\mathbf g_j\) 在下一个 token 产生前进入 cross-attention，OIWG 可以到达普通 beam 未访问的 patch，而完成后的同分数 reranker 无法复制这条生成路径。

### 4.12 分阶段训练与 Checkpoint 选择

<!-- P33 -->

训练将分四阶段进行。阶段 A 在仓库隔离的 SWE-RPG 与确定性 issue–test 对齐对上训练 claim constructor/alignment；阶段 B 在 SWE-Gym 自然 partial-patch matrix 上训练 graph encoder、edge/status heads 和 closure recurrence；阶段 C 加载前两阶段权重，以联合损失训练代码模型 LoRA、claim focus 和 hunk decoder；阶段 D 在未见 repository family 开发集上校准 edge、closure、EOS 与 ABSTAIN 阈值。每阶段均保存 optimizer、seed、step、validation curve 和 checkpoint hash；阶段 C 必须相对基础 LoRA、all-positive coverage 与同参数 generic graph 同时改善预注册的 edge/closure 指标和生成开发结果，才进入 RACE。RACE 20 题不更新任何权重，RACE 80 的任何字段也不进入早停或超参数选择。

### 4.13 可复现算法工件

<!-- P34 -->

最终发布包将包含 claim schema 与 finite-state decoder、训练/开发 repository-family manifest、自然候选与 coalition label builder、typed graph vocabulary、模型配置、LoRA 与全部 graph/edge/closure 权重、hunk decoder、阈值、容器锁文件和评测脚本。每个数据单元保存 task ID、base commit、image、model/tokenizer、constructor、atomizer、test runner、patch、coalition 和输出 hash。训练脚本导出模块名、张量形状、trainable 标志与参数数，推断脚本能从同一 checkpoint 复算 patch、ABSTAIN 和 warrant trace。随机性由 task×method×seed 的 SHA256 产生，规范化 patch hash 忽略无语义 diff 元数据但保留实际代码与文件身份。该发布责任确保研究交付的是可在本地继续训练和运行的生成模型，而不是提示词、API 调用记录或结果后解释。

## 5. 标签构造、训练数据与泄漏边界

### 5.1 公开训练材料与仓库隔离

<!-- P35 -->

SWE-Gym 提供 2,438 个真实 Python 软件任务、可执行环境、测试与公开代理轨迹，是 edge supervision 和本地 generator training 的主要来源（Pan et al. 2025）。训练清单先合并 fork、代码克隆与共同演化仓库为 repository family，再排除 RACE 的 12 个外测仓库及可疑重复 issue；剩余 family 按 train/development/test 互斥。SWE-RPG 的 163 个 Python/Java 任务及 requirement-clarification/plan 参照只在仓库去重后训练或审计 constructor，不向 OIWG 提供 RACE 的文件、实体、步骤或补丁标签（Zhou et al. 2026）。所有公共数据版本、下载 URL、许可、文件 digest、取得时间和 overlap audit 将在首次训练前固化。若无法构造无仓库污染的 split，该设计不会进入外部生成评价。

### 5.2 自然 Candidate 与三分类标签

<!-- P36 -->

每个训练任务由预冻结 ordinary beam 产生四个 completed patches，只取 beam rank 最前的两个自然候选进入 intervention label pool，不依据 FTP、hunk 数或后验质量换位。对 \(J\le4\) 的候选执行全部非空 coalition，每个 variant 在全新容器对可见测试独立运行两次；冲突结果按预注册 adjudication 预算复核。相对于共同 base/empty 结果，稳定 fail→pass 标为 SUPPORT，稳定 pass→fail 标为 REFUTE/ANTAGONISTIC，其余稳定无效应、测试未覆盖、执行冲突或不可识别均标为 MISSING。自然成功候选可以产生 SUPPORT，计入理论现象的 REFUTE 必须来自自然失败候选。Gold Patch 删除、手工 bypass、synthetic sign 和看过 official outcome 后选择候选均不进入标签；rewire 与 sign-shuffle 只在机制消融中使用。

### 5.3 RACE-Bench Lite 20+80 与封存顺序

<!-- P37 -->

下载并锁定 RACE-Bench/container revision 后，实例按
\[
\operatorname{SHA256}(\text{“p2-warrant-v1|”}+\text{benchmark revision}+\text{instance id})
\]
升序排列，前 20 题只调试 constructor、schema、Docker、atomizer 和物理账，后 80 题形成不可替换的 intention-to-treat 分母。第一次读取 Reference Reasoning、Gold/Reference Patch、隐藏 PTP 或 official result 之前，先封存所有方法的 claims、candidate pools、decoder traces、final selections 与成本；再只用 visible FTP partial-patch matrix 确定现象和 task-level \(W\)；随后依据已封存 trace 与同分量规则生成、封存 targeted edge-neutralization 归因臂；最后封存全部 patch hashes 才运行 hidden official evaluator。20 题的 Reference Reasoning 也只能在 constructor 输出封存后审计 recall 和 overprediction，不进入模型、80 题效应量或阈值选择。

### 5.4 部署白名单与隐藏责任

<!-- P38 -->

RACE 正式部署输入仅含 Feature Request/issue、base repository/environment、全部 visible FTP tests、修复前失败输出及其确定性静态派生。Gold/Reference Patch、Reference Reasoning、Test Patch 中未公开部分、reference-derived changed-file/hunk 标签、hidden PTP、official evaluator 输出和任何派生字段均隔离在生成与归因输出封存之后。hidden PTP 只判定 official resolved，既不产生 SUPPORT/REFUTE/MISSING，也不改变 final selection。RACE 80 的 observed intervention matrix 只承担封存后的现象测量与归因目标确定；部署 generator、decoder、selector 与 verifier 只能读取在 SWE-Gym 训练后冻结的预测边。该边界使 claim 来自 issue+visible FTP、生成来自本地模型、最终正确性来自独立隐藏评价，三者没有共享 gold 标签。

## 6. 实验设计、统计责任与算力

### 6.1 研究问题与分析单位

<!-- P39 -->

实验将依次回答现象、学习、生成和外部结果四类问题。现象单位是 RACE 任务中的同一 claim/test component，记录 joint-necessary hunk、自然 SUPPORT/REFUTE、W 状态和不可识别原因；学习单位是 SWE-Gym repository-family held-out 的 \((c,K,t)\) 三元组；生成单位是任务×方法×seed 的 completed patch；终端单位是任务×方法的 gold-free final selection。RQ1 以 80 题 intention-to-treat 比例判断 signed joint mechanism 是否具有实质频率，RQ2 以三分类与 closure 校准判断模型是否可部署，RQ3 以规范化 patch hash 和 sealed decoder trace 判断是否产生新搜索路径，RQ4 以 hidden official resolved、归因破坏和资源账判断外部杠杆。所有比例保留 80 题分母，按 repository 聚类的任务差异承担推断责任。

### 6.2 强基线与复现身份

<!-- P40 -->

比较集同时覆盖搜索、测试约束、关系化多 hunk 生成、subset/minimization、claim coverage、通用图和完成后验证。SWE-RPG 是需求/计划诊断基准而非 patch generator，将只报告 OIWG 与 ordinary generator 对其公开 requirement/plan 参照的后验诊断，不进入 RACE 性能臂（Zhou et al. 2026）。当前工作区没有下表各最新方法的忠实可运行 artifact，因此除 SWE-RPG 公开诊断外，现稿一律标为 style implementation；只有在任何 RACE 80 输出可见前固定作者代码 revision、通过 smoke test 并记录与原论文的输入、工具和模型差异后，才可把相应 style 臂替换为 faithful replication，且替换与否一经封存不得依据 RACE 结果选择。下表以不可合并的方法编号锁定 15 个生成臂、3 个 postprocessor 和 1 个 verifier。G15 只承担归因，不进入主效应排名；G13 是完整 OIWG，G14 则把同一 signed state 降为完成后 rerank，用于检验增益是否真正来自 hunk 边界生成。每个生成臂每题最多封存 4 个 patch hash，三个 postprocessor 每题各封存一个输出，全部 19 个身份每题各有一个 gold-free final selection 接受官方评价。因此现行前瞻容量为不超过 4,800（\(=15\times80\times4\)）个生成 hashes、240（\(=3\times80\)）个 postprocessor hashes，并保留 1,520（\(=19\times80\)）个 official method—task 评价单元；失败、缺失与 NOT_APPLICABLE 均保留状态。加上不超过 5,200 次 visible-FTP intervention executions，确定性标签与封存后评价容量不超过 6,720（\(=5{,}200+1{,}520\)）个 jobs。早期的 15 methods、1,200 official evaluations 与 6,400 jobs 只构成历史下限；任何启动清单都必须在结果不可见时按 19/1,520/6,720 容量前瞻封存，否则研究不会启动，且既定 80 题分母与所有现象/结果阈值保持不变。

| ID | 方法身份 | 类型 | 主要判别责任 |
|---|---|---|---|
| G01 | ordinary beam，共同基础模型 | generator | 普通搜索是否已到达同一 patch |
| G02 | diverse beam，共同基础模型 | generator | 多样化搜索是否已覆盖新 patch |
| G03 | test-augmented beam | generator | 更多 visible FTP 反馈是否复制收益 |
| G04 | Agent-CoEvo-style，代码可用时改为 faithful | generator | code/test constraint coevolution |
| G05 | MultiMend-style，代码可用时改为 faithful | generator | 训练式 multi-hunk 生成 |
| G06 | MultiFixer-style，代码可用时改为 faithful | generator | coordinator–proposer 与 refinement |
| G07 | SynFix-style，代码可用时改为 faithful | generator | RelationGraph 同步修改 |
| G08 | CascadeFix-style，代码可用时改为 faithful | generator | Use/Copy/Nearby 级联计划 |
| G09 | SiblingRepair-style，代码可用时改为 faithful | generator | sibling 检测与一致多处修复 |
| G10 | all-positive minimum-claim coverage | generator | 正覆盖是否已经足够 |
| G11 | 参数匹配的 sign-agnostic graph | generator | 通用关系图是否复制 signed 结构 |
| G12 | direct edge graph，无 balance、closure 或条件解码 | generator | 三分类边预测本身是否已经足够 |
| G13 | 完整 OIWG | generator | 理论方法主身份 |
| G14 | OIWG posthoc-only，将 hunk guidance 改为完成后 rerank | generator | 新 patch 是否来自生成期闭合而非选择 |
| G15 | OIWG targeted neutralization | generator，归因专用 | 同分量理论边是否导致具体新解与解决结果 |
| P01 | generic hunk ablation | postprocessor | 单 hunk 可删性 |
| P02 | IBugFinder-style exhaustive postprocessor | postprocessor | powerset、divisibility 与 joint hunk |
| P03 | TRIM-style DD-Hunk postprocessor | postprocessor | trajectory/edit minimization |
| V01 | training-split-frozen strongest verifier | verifier | 同一合法 baseline pool 的 posthoc 选择上限 |

### 6.3 一次性现象与生成继续标准

<!-- P41 -->

定义 task-level \(W\)：一题只有在同一个 claim/test component 中同时存在两个以上共同必要 hunk，以及来自自然候选的 SUPPORT 与 REFUTE/ANTAGONISTIC，才进入 \(W\)。下列八项共同防止小中间改进被写成重大贡献；全部满足只说明值得重新开展更大、独立的确认研究，不把 80 题筛查本身变成已完成章节。研究继续进入完整章节评价需要冻结 80 题一次性满足：

1. 至少 25/80 题出现针对同一 claim/test 的两个以上共同必要 hunk；多个独立 claim 各有一个 hunk 不计。
2. 至少 20/80 题且覆盖至少 4 个仓库同时出现稳定 SUPPORT 与 REFUTE/ANTAGONISTIC；MISSING 不计负边。
3. \(W\ge16/80\)，且覆盖至少 4 个仓库。
4. repo-held-out SUPPORT/REFUTE/MISSING macro-F1 至少 0.75，并逐类报告 precision、recall、repeat stability 与不可识别率。
5. hidden official resolved 相对最强 generic coverage 和同参数 generic graph 各至少增加 5/80，至少 4 个仓库内方向一致；其中至少 3 个净新增解决在同分量 targeted neutralization 后失去 official resolved。
6. OIWG 至少产生 8 个不在任何 baseline completed-patch pool 的 official-correct patch hash，其中至少 5 个具体 hash 或其 final selection 在同分量 neutralization 后消失。
7. within-task rewire 与 sign-shuffle 在保持节点、度、边数、sign marginal、候选数和预算后，各自在 \(W\) 内消掉至少一半相对最强 generic baseline 的增益。
8. 最强 posthoc verifier 在同一合法 baseline pool、训练数据和预算下，仍不能把 end-to-end resolved 差距追到 2 题以内。

### 6.4 机制归因与消融

<!-- P42 -->

targeted neutralization 将在主输出封存、visible matrix 确定 \(W\)、hidden PTP 仍不可见时生成。对 signed decoder 的每个封存 candidate，算法只在其原 decoder trace 中寻找经 visible matrix 判为 \(W\) 的同分量，按冻结 signed contribution 降序和 component hash 破平选择一个，把该分量 signed edges 置为中性，并以相同 seed、token、forward-pass、candidate 与 test budget 重新解码；没有合格分量时记 NOT_APPLICABLE。outcome-level 归因要求 neutralization 后原净新增任务不再 official resolved，patch-level 归因只要求特定 hash 或对应 final selection 消失，两者分开计数。机制消融另包括 all-positive signs、sign-agnostic graph、删除 joint coalition、删除 balance、删除 closure、将 hunk guidance 改为 posthoc rerank、within-task rewire 与 sign-shuffle。每项消融首先检查 edge/closure 或 decoder-trace 中间量，再检查 novel patch 与 official resolved，避免只以终端跌幅反推理论机制。

### 6.5 统计推断、缺失与停止规则

<!-- P43 -->

现象比例将报告 Clopper–Pearson 区间和 repository-cluster bootstrap，方法差异报告配对 risk difference、clustered 95% 区间及按仓库方向，edge/closure 指标使用 family-blocked bootstrap。多方法终端比较与预设机制消融分别采用 Holm（1979）校正；novel hash 以规范化集合差报告，不对重复 hash 作独立样本。至少 64/80 题必须完成预注册 candidates 与 intervention matrix 且覆盖至少 4 个仓库，筛查才足以支持永久放弃该题的判断；不足时结论为信息不足并保留当前有界假说。判断是否继续时，未完成单元留在 80 分母且不算成功；判断是否永久放弃时，则先把每个 NON_IDENTIFIABLE/INFRA 单元同时补成潜在 \(W\)、潜在自然负边和最大理论优势。只有这种最有利理论补全后的 \(W\) 单侧 95% 上界仍低于 20%，或 generic coverage/graph 的最坏情形配对区间完全落入 \([-0.025,0.025]\) 且没有任何已观察或潜在 pool 外新正确解，才可永久放弃该题；稳定自然负边为零只有 80/80 都完成负边识别时才可单独支持这一判断。其他任一八项责任失败只说明证据不足以把该设计作为独立论文继续，不允许降低阈值、替换任务或用 synthetic patch 补数。

### 6.6 算力、物理账与当前可执行性

<!-- P44 -->

每个执行事件将以 task/method/patch/coalition/repeat 标识，记录 image、base commit、filesystem、config、model、claim、edge、decoder 与 output hashes，以及 token、forward pass、FTP/PTP 调用、CPU/GPU、内存、I/O、墙钟和货币成本。在不超过 6,720 个确定性 jobs 的容量账之外，19×80 个生成/选择单元分别冻结资源向量 \(\mathbf b_{m,i}=(n_{FTP},n_{compile},n_{tool},n_{forward},tokens,wall,compute,money)\)，并按维度聚合 \(\mathbf B_{\mathrm{gen,total}}=\sum_{m=1}^{19}\sum_{i=1}^{80}\mathbf b_{m,i}\)；缓存减少物理执行但不删除逻辑调用成本。SWE-Gym label construction 与 7B LoRA/512-d graph training 计划使用一张 80GB 或两张 48GB GPU，实际 GPU-hour、container-hour、磁盘与货币硬帽只能在 20 题和训练小样本测得 median/P95 后冻结，本文不虚构数值。完整资源账还包括 20 题 debug、公开数据取得、镜像构建、SWE-RPG constructor training 和 infra retries。当前工作区没有 RACE-Bench、SWE-Gym、SWE-RPG、Docker/Linux harness、自然 agent patches、intervention runner、生成器或 checkpoint，因此没有任何 job 已执行，也没有训练或效果曲线可报告。

## 7. 预注册结果责任与解释路径

<!-- P45 -->

未来结果章节将按五张主表与两组图报告，而不是围绕单一 resolved 数字组织叙述。表 1 给出 80 题 expected-cell manifest、自然 joint/refute/\(W\) 发生率和不可识别原因；表 2 给出 repo-held-out 三分类、status 与 closure calibration；表 3 给出各生成器的 completed pool、novel correct hashes、final selections 和资源；表 4 给出 paired official resolved、仓库方向与 verifier gap；表 5 给出 neutralization、rewire、sign-shuffle 和逐组件消融。图 1 展示 hunk 边界上最弱 claim、signed edge 与生成动作的 trace，图 2 展示 cost–resolved 与 pool-overlap frontier。若只出现 edge F1 而没有 pool 外正确 patch，结论将限于诊断；若出现新 patch 而 official resolved 不增，结论将限于搜索差异；若外部增益不随理论破坏消失，则不能归因于 warrant closure。

## 8. 讨论

### 8.1 条件性理论贡献

<!-- P46 -->

若全部证据责任成立，本文可能推进论证理论在生成式信息系统中的计算单位。Toulmin 角色将不再停留于完成补丁的自然语言解释，而会把行为 claim、可执行 observation 与 implementation backing 组织为生成过程中的中间状态；结构平衡则会给该状态提供支持、反驳与缺失的方向一致性。joint-only、substitutable 和 unclosed 状态将说明相同测试通过数为何对应不同实现责任，定向 neutralization 又把该状态连接到具体 hunk 选择与外部软件结果。这种贡献与 ACAA 由 attention 构念改变兼容方向、DSDL 由 expectation–experience 差异创造动态满意度状态的逻辑相同：理论价值来自一个普通目标不会自然保留、且能被单独训练和破坏的中间机制（Chen et al. 2024; Chen et al. 2023）。若自然负边、联合状态或归因链不成立，这项理论推进也不成立。

### 8.2 方法、实践与实质贡献边界

<!-- P47 -->

条件成立时，方法贡献将是一个本地可训练的 patch generator，而不是 claim 特征、解释面板或 verifier。它以 gold-free constructor 改变标签，以 signed coalition graph 改变表示，以 balance/closure/hard-negative 改变损失，并以 weakest-claim focus 改变下一 hunk 的 token 分布；保存的 checkpoint、schema、runner 和 trace 使四项改变可复算。实践上，输出 patch 之外还提供未闭合或被反驳 claim、相关 hunk/test 分量和 abstain 原因，帮助开发者把“测试过了”区分为有 implementation backing 的观察与仍有缺口的观察。该设计的复杂度只有在至少 5/80 official resolved 增益、8 个 baseline-pool 外正确 hash 和预设归因同时出现时才有章节规模；若效果上限只是一两个重排任务，复杂图与运行成本就是小题大做，研究将停在诊断工件而不包装为算法贡献。

### 8.3 与论文一、论文三的边界

<!-- P48 -->

论文一研究任务—代理—证据区域—取得尝试上的有效使用机制，输出取得、表征和行动状态，并在首个实质行动前至多选择一次补取区域或 ACT-NOW；它不构造或压缩静态上下文包，也不生成具体 patch。论文一计划中的验证/提交若出现，只是首行动前一次性冻结、由共享 executor 落实的 open-loop 骨架，不根据随后真实观测重决策。本文研究行动前的任务—候选补丁生成过程，读取 issue、base repo 与 visible FTP，输出新 patch、ABSTAIN 和 warrant state，不加载论文一 checkpoint。论文三从已持久化 patch snapshot 出发，在每项真实运行观测到达后重算下一验证实验、ReturnToEdit、Submit 或 Handoff，不生成任意新补丁，也不读取本文的 graph weights。三篇可以共享公开仓库解析器与 official evaluator 接口，但训练表、标签、损失、模型权重、部署动作和决策时点相互独立。由此，本文的 hunk-level generation 不被重写为证据补取，也不扩张为补丁后的 closed-loop stop、test selection 或 handoff。

### 8.4 局限

<!-- P49 -->

本研究首先受制于观察性干预的语义边界：partial-patch 重放只能描述冻结候选和测试下的条件变化，无法证明某段代码在所有实现中导致某条需求成立。visible FTP 的覆盖不足会增加 MISSING、UNOBSERVED 和 ABSTAIN，隐藏 PTP 又只能评价最终结果而不能修复训练标签。\(J\le4\) 的完整 coalition 上限使较大 patch 保持不可识别，RACE 的 feature-addition 情境也限制了对缺陷修复、其他语言和长期演化的外推。SWE-RPG 辅助监督、自动 claim atomization 和 style baselines 可能带来构念或实现偏差，因而需要来源审计、人工盲评小样本和忠实 artifact 替换。80 题筛查的仓库聚类与功效只适合发现较大机制；即使全部通过，仍需在独立任务上确认，并与未来更强 test generation、多 hunk agent 和 verifier 重新比较。

## 9. 结论

<!-- P50 -->

本文提出一项尚待执行的研究设计，用 Toulmin claim–evidence–warrant 与结构平衡把补丁生成重构为有符号 claim–hunk/coalition–test 闭合过程。OIWG 将理论依次编译为 gold-free claim 本体、SUPPORT/REFUTE/MISSING 与联合状态、typed signed graph、balance/closure/hard-negative loss，以及最弱未闭合 claim 驱动的 hunk-level decoder。公开 SWE-Gym 与 SWE-RPG 将承担仓库隔离训练，RACE-Bench Lite 20+80 将在严格封存下承担自然现象、池外新 patch、hidden official resolved 和定向机制归因。当前资产不足以启动任何训练或评价，因而本文没有经验发现；完整设计的作用是让该题能够以有限公共数据被明确证成或证伪。只有理论状态真实改变生成并产生强基线池外的正确软件行动，观察性干预 warrant 闭合才值得成为独立论文。

## 参考文献

Ahmed, T., Ganhotra, J., Pan, R., Shinnar, A., Sinha, S., and Hirzel, M. 2025. “Otter: Generating Tests from Issues to Validate SWE Patches.” *Proceedings of the 42nd International Conference on Machine Learning*, 752–771.

Cartwright, D., and Harary, F. 1956. “Structural Balance: A Generalization of Heider’s Theory.” *Psychological Review* 63(5):277–293.

Chen, G., Huang, L., Xiao, S., Zhang, C., and Zhao, H. 2024. “Attending to Customer Attention: A Novel Deep Learning Method for Leveraging Multimodal Online Reviews to Enhance Sales Prediction.” *Information Systems Research*. https://doi.org/10.1287/isre.2021.0292.

Chen, G., Xiao, S., Zhang, C., and Zhao, H. 2023. “A Theory-Driven Deep Learning Method for Voice Chat–Based Customer Response Prediction.” *Information Systems Research* 34(4):1513–1532. https://doi.org/10.1287/isre.2022.1196.

Gharibi, R., Sadreddini, M. H., and Fakhrahmad, S. M. 2026. “MultiMend: Multilingual Program Repair with Context Augmentation and Multi-Hunk Patch Generation.” *Automated Software Engineering* 33:69. https://doi.org/10.1007/s10515-026-00611-2.

Holm, S. 1979. “A Simple Sequentially Rejective Multiple Test Procedure.” *Scandinavian Journal of Statistics* 6(2):65–70.

Hu, H., Fang, C., Shang, Y., Liu, J., Sun, W., Xie, G., Zhong, C., and Zhang, Q. 2026. “MultiFixer: A Coordinator-Proposer Based Multi-Agent Framework for Fixing Multi-Hunk Bugs.” *arXiv:2607.26591*.

Jimenez, C. E., Yang, J., Wettig, A., Yao, S., Pei, K., Press, O., and Narasimhan, K. 2024. “SWE-bench: Can Language Models Resolve Real-World GitHub Issues?” *International Conference on Learning Representations*.

Lee, K., and Ram, S. 2024. “Explainable Deep Learning for False Information Identification: An Argumentation Theory Approach.” *Information Systems Research* 35(2):890–907. https://doi.org/10.1287/isre.2020.0097.

Li, J., Larsen, K. R., and Abbasi, A. 2020. “TheoryOn: A Design Framework and System for Unlocking Behavioral Knowledge through Ontology Learning.” *MIS Quarterly* 44(4). https://doi.org/10.25300/MISQ/2020/15323.

Li, K., Yuan, Y., Wang, M., Zheng, S., Wang, W., Yang, P., Li, M., and Lv, W. 2026. “Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints.” *arXiv:2604.04580*.

Liu, S., Zhao, Z., Hu, X., Liu, K., Yang, X., and Xia, X. 2026a. “A Benchmark for Evaluating Repository-Level Code Agents with Intermediate Reasoning on Feature Addition Task.” *arXiv:2603.26337*.

Liu, X., Ren, J., Wang, Y., Xin, Q., Xie, X., and Xuan, J. 2026b. “SiblingRepair: Sibling-Based Multi-Hunk Repair with Large Language Models.” *arXiv:2605.06209*.

Mathai, A., Iyer, S., Nogikh, A., Maniatis, P., Ivancic, F., Yang, J., and Ray, B. 2026. “TRIM: Reducing AI-Generated CodeSlop via Agent Trajectory Minimization.” *arXiv:2607.18161*.

Nashid, N., Bouzenia, I., Pradel, M., and Mesbah, A. 2025. “Issue2Test: Generating Reproducing Test Cases from Issue Reports.” *arXiv:2503.16320*.

Pan, J., Wang, X., Neubig, G., Jaitly, N., Ji, H., Suhr, A., and Zhang, Y. 2025. “Training Software Engineering Agents and Verifiers with SWE-Gym.” *Proceedings of the 42nd International Conference on Machine Learning*, 47717–47737.

Ruan, H., Zhang, Y., and Roychoudhury, A. 2025. “SpecRover: Code Intent Extraction via LLMs.” *47th IEEE/ACM International Conference on Software Engineering*, 963–974.

Tang, X., Gao, J., Xu, J., Sun, T., Song, Y., Ezzini, S., Ouédraogo, W. C., Klein, J., and Bissyandé, T. F. 2025. “SynFix: Dependency-Aware Program Repair via RelationGraph Analysis.” *Findings of the Association for Computational Linguistics: ACL 2025*, 4878–4894. https://doi.org/10.18653/v1/2025.findings-acl.252.

Toulmin, S. E. 1958. *The Uses of Argument*. Cambridge University Press.

Xin, Q., Wu, H., Tang, J., Liu, X., Reiss, S. P., and Xuan, J. 2024. “Detecting, Creating, Repairing, and Understanding Indivisible Multi-Hunk Bugs.” *Proceedings of the ACM on Software Engineering* 1(FSE):2747–2770. https://doi.org/10.1145/3660828.

Zhang, H., Kuang, L., Yang, Y., Fang, Y., and Xia, Y. 2026a. “CascadeFix: Multi-Location Program Repair via Cascading Planning and Generation.” *Findings of the Association for Computational Linguistics: ACL 2026*, 39374–39385. https://doi.org/10.18653/v1/2026.findings-acl.1962.

Zhou, X., Chong, C. Y., Kim, K., Peng, Y., Shu, R., Wu, Z., Han, X., Yuan, G., Zhuang, Z., Kim, J., Ju, J., Ju, S., Yoon, T., and Lo, D. 2026. “A Unified Issue Resolution Benchmark for Requirement Clarification, Planning, and Code Generation for Coding Agents.” *arXiv:2608.09072*.
