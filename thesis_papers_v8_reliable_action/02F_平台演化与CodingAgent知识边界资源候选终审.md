# 平台演化与 Coding Agent 知识边界资源候选终审

> 审计日期：2026-08-16  
> 审计对象：平台方 coding agent 在一次平台演化决策中联合产生 provider patch、兼容实现与面向下游 coding-agent 补充者的多尺度可执行资源  
> 终判：**HIGH-CONFIDENCE TERMINAL NO-GO**  
> 保留为独立论文候选：**0**  
> 本文件性质：内部选题与可行性终审，不是论文正文，也不报告任何尚未运行的候选模型结果

## 1. 一句话结论

这个问题具有真实外部损害、可以构造受控执行环境，也能形成一个计算量很大的联合系统；然而，钢人化后的新增行动能力可由 provider 兼容演化、可执行知识包、可复用迁移程序和 client-specific repair 的现有能力直接组合得到，剩余部分是普通的多客户资源组合控制。Foerderer 等人的知识边界资源理论没有检验这种组合的有效性，更没有给出可识别的资源分配策略；同信息、同标签、同动作、同参数的通用异质图模型或双层 population controller 可以复制全部决策。因此，本候选不应成为第三篇论文，也不应通过改名为 agent experience、知识编排或生态安全而返回候选池。

## 2. 审计范围、实际阅读与证据等级

### 2.1 实际完整回读的理论原文

本次逐行回读了 Foerderer、Kude、Schuetz 与 Heinzl 的本地全文 [Knowledge boundaries in enterprise software platform development: Antecedents and consequences](../database_fulltext_all/03810_2019_knowledge-boundaries-in-enterprise-software-platform-development-antecedents-and-consequences-fo.md)，并用 Otero AIS Basket 只读库核对了 DOI `10.1111/isj.12186`、作者、期刊、年份、卷期和页码。该文发表于 *Information Systems Journal* 2019 年第 29 卷第 1 期，第 119–144 页。全文共 492 个物理行，读取时的 SHA-256 为 `58D050F376B94B4FF485D21F599EE02B890A5DCFBC1D2B2336346A4FDEBBE341`。

为防止把 Foerderer 等人的归纳类别误写成既有因果理论，本次还完整回读了 Carlile 2002 与 2004 的原文：[A Pragmatic View of Knowledge and Boundaries](https://doi.org/10.1287/orsc.13.4.442.2953) 和 [Transferring, Translating, and Transforming](https://doi.org/10.1287/orsc.1040.0094)。Star 与 Griesemer 的 [Institutional Ecology, “Translations” and Boundary Objects](https://doi.org/10.1177/030631289019003001) 只用于核对“局部适应、跨场域保持共同身份”的定义来源，不用它推出自动资源分配政策。

### 2.2 实际回读的技术全文与证据等级

下列技术论文均回读了正文的任务定义、数据、方法、实验和局限部分，而不是只看搜索摘要。

| 工作 | 状态与实际覆盖 | 对本候选的作用 |
|---|---|---|
| [When LLMs Lag Behind: Knowledge Conflicts from Evolving APIs in Code Generation](https://arxiv.org/abs/2604.09515) | 2026 arXiv；270 个真实 Python API 更新、8 个库，研究过时参数知识与新文档冲突 | 证明演化知识滞后真实，但研究对象是 client/model 适应，不是 provider 联合演化 |
| [Diagnosing Knowledge Gaps in LLM Tool Use: An Agentic Benchmark for Novel API Acquisition](https://arxiv.org/abs/2606.03657) | 2026 arXiv；NovelAPIBench 约 1.9K 个任务，拆分 signature、mechanism、source、example | 直接覆盖机器可用知识包的成分与可执行评价；示例并非可随意替代的装饰 |
| [Agentic Generation of AST Transformation Rules for Fixing Breaking Updates](https://arxiv.org/abs/2606.24446) | 2026 arXiv；BigBag 在 157 个 BUMP 编译失败实例上让 agent 生成并执行 AST transformation | 直接覆盖 cluster-level reusable migration program；多 client seed 是原文已经指出的改进方向 |
| [DepRepair: LLM-Based Source-Code Repair for Dependency Breaking Changes](https://arxiv.org/abs/2607.17957) | 2026 arXiv；DepBench 含 95 个真实更新、四个生态和 Docker oracle | 直接覆盖结构化 upstream evidence、定位与 client-specific executable patch |
| [SPELL: Synthesis of Programmatic Edits using LLMs](https://arxiv.org/abs/2602.01107) | 2026 arXiv；从生成并验证的迁移例子归纳可重复 PolyglotPiranha 变换 | 直接覆盖 executable example 到 reusable migration script 的学习链 |
| [Breaking Changes in Software Ecosystems: A Systematic Literature Review](https://arxiv.org/abs/2605.24397) | 2026 arXiv；综合 97 项 primary studies、66 类策略 | 只作研究版图索引；provider 的 deprecation、additive evolution、parallel versions、契约与生态协调不是空白 |
| [APIfix: Output-Oriented Program Synthesis for Combating Breaking Changes in Libraries](https://doi.org/10.1145/3485538) | OOPSLA 2021；从迁移/新库使用例子合成 API usage transformation | 直接覆盖从例子学习可复用 client migration transformation |
| [Adaptoring: Adapter Generation to Provide an Alternative API for a Library](https://arxiv.org/abs/2401.07053) | 2024 arXiv；从文档、用法与人工规格生成可执行 alternative API adapter | 直接覆盖 provider/中介层 versioned shim 的主体能力 |
| [BUMP: A Benchmark of Reproducible Breaking Dependency Updates](https://doi.org/10.1109/SANER60148.2024.00024) | SANER 2024；571 个可复现更新、153 个 Java/Maven 项目 | 可提供 client 破坏起点，但 upstream release 已固定 |
| [BreakBot: Static Reverse Dependency Compatibility Testing for Java Libraries](https://doi.org/10.5281/zenodo.7475823) | TSE 配套 artifact；对 library PR 做 reverse-dependency compatibility impact | 直接覆盖 provider-side 下游影响观测与 what-if 基线 |
| [PyMigBench](https://github.com/ualberta-smr/PyMigBench) | 公开 Python library migration 数据 | 覆盖跨库迁移，不提供同一 provider 目标的多种 patch 与资源组合分支 |
| [SWE-Chain: Evaluating Coding Agents on Dependency-Driven Software Evolution](https://arxiv.org/abs/2605.14415) | 2026 arXiv；跨版本依赖链任务 | 压缩跨版本连续演化空位，但不是 provider 资源组合实验 |
| [RustEvo2](https://arxiv.org/abs/2503.16922) | 2025 arXiv；版本化 Rust API 演化与 client generation | 增加跨语言 API evolution 评价资产 |
| [GitChameleon2](https://arxiv.org/abs/2507.12367) | 2025 arXiv；带测试的版本特定仓库问题 | 可测版本知识，不能标注 provider portfolio 的反事实价值 |
| [CodeUpdateArena](https://arxiv.org/abs/2407.06249) | 2024 arXiv；版本更新后的 code generation | 固定更新后的模型适应，不是 upstream 联合设计 |
| [LibEvolutionEval](https://arxiv.org/abs/2412.04478) | 2024 arXiv；多库版本特定 completion | 用于 version-specific 基线；公开资产状态须在实验前再核 |
| [Evaluating Incompatible Third-party Library API Usage in LLM-based Code Completion](https://doi.org/10.1145/3830085) | TOSEM，2026-07-15 online；10,867 个 versioned API usage tasks | 直接覆盖版本知识库、实时检测和轻量修复，仍是 client completion |
| [The Perfection Paradox: From Architect to Curator in AI-Assisted API Design](https://doi.org/10.1145/3772363.3798429) | CHI EA 2026；Google AIP 微调系统生成 API specification，16 名专家盲评 | 新增 provider-side AI API 设计直接近邻；只生成 specification，不执行 provider code 或生态资源组合 |
| [Developer Experience with AI Coding Agents: HTTP Behavioral Signatures in Documentation Portals](https://arxiv.org/abs/2604.02544) | 2026 arXiv；9 种 coding agent、6 种 assistant、受控门户与公开日志 | 实测 agent 成为文档消费者；资源设计建议被作者明确列为解释或未来检验，不是效果证据 |

Microsoft AX、Agentic Resource Discovery、`llms.txt`、`AGENTS.md`、MCP 文档服务与类似产品页面只被视为行业动向。它们不能支撑学术空白，也不能把文档发布本身抬升为算法贡献。

### 2.3 证据状态标记

全文采用三种明确状态。

- **T-OBS**：理论原文实际观察或分析得到的事实。
- **T-UNT**：理论原文明确未检验或只在讨论中提出的有效性猜想。
- **C-NEW**：本候选为钢人化而提出的新构造、新假设或待运行设计。

任何 C-NEW 都不得伪装成 Foerderer 等人的已检验命题。

## 3. 风险对象和决策时点

### 3.1 真实潜在损害

平台/API 演化会把局部 provider 决策传播到大量下游仓库。损害至少包括下游无法构建、表面可构建但行为语义改变、修复或安全更新被长期搁置、兼容层继续保留不安全旧行为，以及每个 client 重复承担迁移和验证成本。coding agent 加速 provider 与 client 两端的修改后，错误也可以更快、更广地复制，因此总体风险不能用单仓库 pass rate 代替。

### 3.2 介入时点与状态可见性

介入发生在 provider 已有明确的功能、治理或安全演化目标，但发布 patch 与配套资源尚未冻结时。平台方 agent 能观察 provider 的旧实现、变更目标、API/schema、版本策略、公开 reverse dependencies、client call graph、公开测试、历史 issue、release notes、静态分析和受控执行 trace。它看不到私有 client、未覆盖的业务语义、组织的真实升级意愿、未来组合调用和所有安全依赖传播路径。

### 3.3 行动空间

- 正常行动：完成 provider 功能或安全目标，发布兼容演化，提供版本化资源并允许下游升级。
- 风险行动：直接删除/改写 API、发布与代码不一致的文档、生成过宽 AST 规则、让 shim 继续暴露危险旧语义、只修公开 client 或用大量 client-specific patch 掩盖不可迁移的设计。
- 纠正行动：改写 provider patch、增加显式 compatibility implementation、缩小并验证 AST 变换范围、补充可执行契约/示例、为无法共享规则的 client 生成 bridge patch、延迟特定接口而非拒绝整个安全更新。

候选不能通过不修改 API、拒绝发布或让全部 client 停留在旧版本获得高分。provider 目标满足和安全更新语义必须作为硬约束。

## 4. Foerderer 理论账本：观察、未检验与本研究新主张

### 4.1 原文实际观察到的关系

Foerderer 等人以四个 enterprise software platform 为案例，依据 40 次访谈建立归纳框架，其中包括 2 位 provider executives 与 38 位 complementors。材料采集时间为 2013 年 10 月至 2014 年 6 月。以下关系属于 T-OBS。

| 原文构念 | 原分析单位与关系 | 本候选可合法继承的最低限度 |
|---|---|---|
| functional extent | 平台核心功能可被补充者重用与重组的广度/深度；与补充者知识差异相关 | 可提出平台功能覆盖影响下游异质性的待检验类比，不能直接把调用图度数当构念真值 |
| interface design | 开放或 proprietary standard 影响跨域依赖 | 可用于解释接口标准选择与依赖关系，不能推出某种 shim 必然最优 |
| evolutionary dynamics | 平台变化速度增加 novelty，并引发/加剧边界 | 可作为演化节奏的情境前因，不能被等同于单个 commit diff 大小 |
| differences | 平台方与补充者 domain knowledge 的偏离程度 | 原构念是知识差异，不是 AST edit distance |
| dependencies | 跨知识域的关联 | 原构念不是 package dependency edge 的同义词 |
| novelty | 知识变化程度 | 原构念不是 API 新增数量的机械计数 |
| syntactic boundary | 缺少共享术语/语言 | schema、名称和签名差异可以是技术代理，但须独立验证 |
| semantic boundary | 对同一术语缺少共享意义 | hidden behavior mismatch 只能作为可能结果，不能反向定义完整构念 |
| pragmatic boundary | 利益与知识在险，需要改变既有知识 | 不能把 client patch 难度或成本自动改名为 pragmatic boundary |
| KBR scope | 资源所含信息、技能与组织能力的丰富程度 | 可提出资源丰富度指标，但原文没有给出可加总的标度 |
| KBR scale | 资源能容纳补充者需求的程度 | 可提出覆盖客户数/调用簇指标，但原文没有给出最优成本函数 |

### 4.2 三类知识边界资源的原始含义

Foerderer 等人观察到的 broadcasting 包括文档、portal、changelog、tutorial、example 与 sandbox，面向整个生态，规模较高而范围较低。Brokering 依赖 helpdesk、account manager 等中介，为部分补充者提供更具情境的 meta-knowledge。Bridging 则由专家与个别补充者密集协作，范围高、规模低。Finance 案例还显示，仅靠数百页广播材料可能出现过时、不一致和缺少单一真源的问题，随后 provider 增加了 brokering。

这些材料证明不同资源形态在真实平台生态中共存。它们没有证明三类资源互斥，没有给出 broadcasting→brokering→bridging 的固定行动顺序，也没有证明哪类 client 应分配哪种资源。

### 4.3 原文明确没有检验的关系

Foerderer 等人在结果讨论中明确说明，他们不打算推导关于所识别知识边界资源有效性的命题。该限制属于 T-UNT 的边界，而不是措辞上的谦逊。原文可以支持“资源类别与边界条件共同出现”，不能支持以下因果断言。

- semantic boundary 高时，cluster AST migration 必然优于 executable example。
- pragmatic boundary 高时，client-specific bridge 必然带来更好的维护结果。
- scope/scale 的某个组合能最小化生态总损害。
- 三种资源有稳定、非交换的升级次序。
- agent 自动生成这些资源能重现人类 brokering 或 bridging 的知识转换。

### 4.4 Carlile 提供的补充与仍然存在的缺口

Carlile 2002/2004 把 transfer、translation 与 transformation 分别关联于 syntactic、semantic 与 pragmatic 边界，并指出较高层过程依赖较低层能力。这个方向关系比 Foerderer 的资源类别更强：novelty 增大时，单纯 transfer 可能不够，需 translation；利益与知识在险时可能需要 transformation。

但 Carlile 的 transformation 指参与者围绕共同利益改变既有知识与权衡。自动生成 client bridge patch 不等于利益协商；通过 hidden test 也不等于建立 shared meaning。该理论没有唯一决定 provider patch、shim、bundle、AST rule 与 client patch 的张量结构、损失权重或选择策略。

## 5. 钢人化后的最强候选

### 5.1 直白研究问题

在平台方必须完成给定功能或安全演化目标时，能否训练一个 coding agent，使其联合选择并执行 provider patch、versioned compatibility implementation、machine-readable broadcast bundle、cluster-level AST migration program 与必要的 client-specific bridge patch，从而在资源预算内降低跨 client 的构建破坏、隐藏行为不兼容、安全更新延迟和维护成本？

### 5.2 输入与输出

输入不是一份文档，也不是待分类的 client。一个样本起点包括：

- provider 旧状态 `P0`、功能/安全目标 `q`、受保护行为契约 `K` 与允许的版本策略；
- API symbol/schema/调用关系、provider test 与可见 interaction trace；
- client population `C={C1...Cn}`、版本依赖、调用点、公开测试及 provider-client heterogeneous graph `G`；
- 候选资源成本、执行预算和不允许退回旧版的约束。

联合输出是可执行程序 `A=(ΔP,Wv,B,{Tk},{ΔCi},M)`：

- `ΔP`：真正实现目标的 provider code/schema/version patch；
- `Wv`：versioned shim 或 compatibility implementation；
- `B`：版本化 machine-readable bundle，包括 API diff、schema、行为契约、可执行例子和 provenance；
- `Tk`：面向 usage cluster 的 AST migration program；
- `ΔCi`：仅在共享规则无法保持行为时生成的 client-specific bridge patch；
- `M`：release/resource manifest，记录适用版本、覆盖 client、验证 oracle、失效条件与成本。

### 5.3 coding agent 的低层行动

agent 必须真实 checkout provider/client，在隔离容器中读取 AST、schema、call graph 和 trace，编辑 provider implementation 与版本声明，构建并测试旧/新接口，生成并编译 shim，写入并执行 example，合成/应用 AST rule，运行 client hidden tests 与 interaction snapshot，检查安全目标，依据失败 trace 回到 provider 或资源动作并修订。单次自然语言 plan、文档 rerank 或三类 router 都不合格。

### 5.4 状态张量与架构

钢人化模型可包含以下张量。

- `H_P∈R^(n_p×d)`：provider symbol、行为契约、变更目标和版本状态。
- `H_C∈R^(n_c×d)`：client usage cluster、可见 test/trace、版本与维护历史。
- `H_A∈R^(n_a×d)`：shim、bundle、AST program 和 bridge candidate 的可执行状态与成本。
- `E_PC,E_CC,E_PA`：provider-client 调用/依赖、client 相似性、provider-action 可行边。
- `Z∈{0,1}^{n_c×n_a}`：resource/client assignment。
- `Y_hat[b,i,m]`：同一起点 branch `b` 对 client `i` 的 build、behavior、安全更新与成本结果预测。

架构可以是 temporal change encoder 加 HGT population encoder、code/program generator、counterfactual world model 与 constrained bilevel controller。外层选择满足 provider 目标的联合 action，内层在容器反馈下更新 patch/resource；生成头分别输出 provider diff、shim code、resource schema、AST rule 和 client patch。

### 5.5 训练信号与损失

候选的训练样本必须从同一 `P0,q,C` 产生多条可执行分支，而不能把历史唯一 patch 当作最优标签。分支至少包括 breaking patch、additive/deprecation patch、shim patch，以及 broadcast-only、cluster rule、client bridge 与组合 portfolio。

监督来自 provider goal tests、安全检查、旧/新 contract、client build、hidden behavior tests、interaction snapshots、迁移成功、更新版本可达性、resource 生成与执行成本。候选损失可写为：

`L = L_provider_goal + λ1 L_security + λ2 L_client_behavior + λ3 L_build + λ4 L_counterfactual_value + λ5 L_program_exec + λ6 L_assignment + λ7 L_cost + λ8 L_calibration`。

其中 provider 目标与安全条件是硬约束；no-change、拒绝更新或长期保留已知不安全旧行为的 branch 被判 infeasible。`L_assignment` 若仅用广播/中介/桥接类别作分类标签，则不能构成理论算法贡献。

### 5.6 推断动作与训练工件

推断时，模型针对同一 provider 目标生成若干 provider/resource branches，在隔离 client population 上实际执行可见 oracle，再以 world model 估计隐藏 client 与成本，最终提交一组 provider code、compatibility code、资源包、AST program、必要 client patch 和可审计 manifest。可复现工件包括 HGT/world-model checkpoint、生成器 LoRA、资源策略权重、AST rules、shim、容器镜像、branch manifest、配置、随机种子与执行日志。

### 5.7 划分、泄漏与算力预算

训练/验证/测试按时间、provider family、library、API symbol/change family、client repository 与 transformation template 联合去重。测试集屏蔽未来 release note、gold patch、未来 client commit、hidden tests 和由同一 edit template 派生的训练样本；近重复调用簇用 AST/semantic hash 清理。

一个最低规模的自建研究可尝试 50–150 个 provider changes、每个 20 个 client、每起点 6 个 portfolio，形成约 6,000–18,000 个 container branches。100–300M 参数的 HGT/world model 加 7B code model LoRA，预算量级可先设为 8 张 A100 80GB、5–10 天训练与独立 CPU 容器集群。这里是设计预算，不是已经消耗的算力，也不是可行性证明。

## 6. 可执行反事实数据：可自建，但现有公开资产不识别核心政策

### 6.1 现有资产的缺口

BUMP、DepBench、BigBag 和大部分 migration benchmarks 从已经发布的 upstream change 开始，提供旧/新依赖与破坏 client。它们没有为同一 provider 目标提供多个行为等价或安全等价 `ΔP`，也没有同时执行 `ΔP × shim × bundle × cluster rule × client bridge` 的 portfolio branches。NovelAPIBench 能比较知识成分，但不改变 provider implementation。BreakBot 能观测候选 provider patch 的下游影响，却不产生资源组合的反事实标签。

因此，公开资产可以组成容器基础设施，却不能直接训练“provider patch 与资源 portfolio 的联合最优政策”。把不同 benchmark 的成功率拼在一起不是同起点反事实。

### 6.2 严谨自建的有限方案

有限、可运行的研究环境可以自建，不能仅因尚未运行而否决。

1. 从开放 provider 的已关闭 issue、安全 advisory 或 API governance proposal 选定 `P0` 与不可撤销目标 `q`。
2. 固定 release 前公开 reverse clients，并冻结仓库、依赖、工具链与容器镜像。
3. 由与模型开发隔离的团队编写 provider contract、hidden behavior test、security checker 和跨调用 interaction snapshot。
4. 为同一目标构造并人工复核 breaking、additive、parallel-version、shim 等 provider variants。
5. 对每个 variant 执行 bundle 成分、AST rules 与 client bridge 的受控组合，记录成功、二次损害、运行成本和维护面。
6. 预注册哪些结果是执行 oracle，哪些只是 proxy；同一起点的全部分支进入同一 split。

### 6.3 仍不可识别的外部结果

公开 client 不能代表私有使用，测试通过不能保证全部行为语义。真实 security-update adoption delay、maintainer burden 与长期 shim debt 涉及人和组织的选择，无法从短期容器执行中得到真标签。它们需要后续现场/纵向研究，不能被下载时间、模型 token 或补丁行数冒充。

因此，构建失败、已定义 hidden behavior 与隔离安全 checker 可形成有限可识别结果；广义生态采纳和维护成本仍部分不可识别。数据问题不是单独的 NO-GO 理由，却削弱了理论所声称组织结果与模型训练标签之间的连接。

## 7. 最强直接基线与公平比较

公平实验必须固定 `P0,q,C`、可见信息、hidden oracle、模型调用预算、容器时间、候选动作和总参数量。至少包括：

1. historical provider patch + historical docs；
2. provider compatibility-first：additive evolution、deprecation、parallel version 与 contract test；
3. Adaptoring 或等价 versioned adapter/shim generator；
4. BreakBot + interaction-snapshot provider impact analysis；
5. NovelAPIBench 最优知识 bundle 构成；
6. BigBag 与 SPELL 的 reusable transformation；
7. DepRepair、Byam 或同代 client-specific coding agent；
8. full composition：compatibility baseline + structured executable bundle + BigBag/SPELL + client bridge；
9. 同信息、同标签、同动作、同参数的 generic HGT；
10. temporal world model/POMDP 与 bilevel population controller；
11. 在已执行 branch 集合上选取的 oracle portfolio upper bound。

no-change 和 refuse-update 不列为合法基线。参数和调用预算不公平时，所谓联合能力可能只是更多搜索和更多 client 执行带来的收益。

## 8. 直接能力覆盖矩阵

| 候选声称的新能力 | 已有最直接能力 | 组合后剩余部分 | 独立新增能力判断 |
|---|---|---|---|
| 产生 actual provider API design/spec | Google AIP 微调系统已生成 provider-side API specification；传统 additive/deprecation/parallel version 已成熟 | 把 design 变成实现并执行下游 tests | 仍需工程，但不是独有生成范式 |
| 生成 provider compatibility implementation | Adaptoring、adapter/shim、parallel versions | 根据 client population 选何时使用 | 普通受约束策略选择 |
| 生成 machine-readable executable bundle | NovelAPIBench 拆分并执行 signature/mechanism/source/example；DepRepair 验证 structured evidence | 为一个 provider release 自动打包并版本化 | 集成与发布工件，不足以单篇 |
| 生成 cluster reusable AST migration | BigBag、SPELL、APIfix | 多 client seed 与 cluster assignment | BigBag 已明确指出多 client seeding；assignment 是控制问题 |
| 生成 client-specific bridge | DepRepair、Byam 与通用 coding agent | 在共享 rule 失败后才分配 | route/portfolio，不是新 repair 能力 |
| 评估 provider change 的生态影响 | BreakBot、API interaction snapshots、reverse-dependency testing | 共同预测多个资源动作的结果 | 可用 world model 实现，无理论独占 |
| 服务下游 coding-agent 消费者 | agent HTTP fingerprint 研究确认其门户访问方式；行业 AX 提供 machine-readable surface | 把访问适配与代码迁移联合评价 | 新情境真实，但未产生不可替代算法 |
| 联合选择所有资源 | 上述完整组合 + generic bilevel controller | 唯一未被单篇直接命名的整体 | 系统组合与资源优化，不是独立生成能力 |

Google CHI EA 工作进一步压缩了 provider-side agent 生成 API 的空白：它的 16 人研究说明 AI 可一致地执行既有治理规范，同时可能用表面一致性掩盖领域逻辑与操作约束。它没有执行 provider code 或 client compatibility，所以不是完整覆盖；但它使本候选更难把“provider coding agent 生成 API”作为新增能力。

HTTP behavioral-signature 工作证明九种 coding agent 在受控 portal 上多以一到四次请求取文档，且实验中没有 agent 请求 `llms.txt`。作者明确把 token-aware 文档、反馈协议与标准采用列为解释性建议或未来研究，而非已测效果。这项证据加强了“agent 是不同内容消费者”的情境动机，却不支持知识资源 portfolio 的因果有效性。

## 9. 理论到算法责任审计

### 9.1 机制链逐项判定

| 理论链环节 | 合法理论责任 | 候选映射 | 终审问题 |
|---|---|---|---|
| functional extent → differences | 平台功能范围与补充者知识差异相关 | provider API coverage、client usage diversity | 图指标是技术 proxy，分析层级从组织知识降为代码结构 |
| interface design → dependencies | 标准开放程度改变跨域依赖 | schema openness、coupling edge | package edge 不是知识依赖本身；不能直接给行动方向 |
| evolutionary dynamics → novelty | 变化速度提高新颖性和边界 | temporal diff、release cadence | 可作为输入，不唯一决定 resource action |
| differences/dependencies/novelty → boundary | 边界由知识关系和新颖性产生 | client cluster/contract mismatch | 需构念测量，不能由 build failure 反向贴标签 |
| syntactic/semantic/pragmatic boundary | transfer/translation/transformation 的处理需求不同 | bundle/rule/client patch | semantic 与 pragmatic 映射发生严重层级错置 |
| KBR scope/scale tradeoff | 资源丰富度与可服务需求规模不同 | resource cost/coverage tensor | 原文没有有效性函数、最优点或可交换性命题 |
| broadcasting/brokering/bridging | 真实生态中的三类资源活动 | bundle/cluster rule/client bridge | artifact granularity 与组织互动类别混合，无法稳定一一对应 |

### 9.2 方向冲突是否足够非平庸

钢人化系统确有四种有方向的冲突。

- 广播资源成本低、覆盖广，但异质行为 client 可能需要更深的规则或 patch。
- 紧急安全更新要求快发，shim 却可能延续不安全旧语义并增加维护面。
- cluster rule 可摊薄成本，过宽规则会对非同构 client 产生 secondary harm。
- provider 接口清理提升长期可维护性，却增加当期下游破坏与迁移成本。

这些冲突是真实的，也是非交换的；但它们来自通用的多目标控制、资源覆盖和行为契约约束。Foerderer 没有给出安全更新优先级、shim 失效条件、AST rule scope 或 client assignment 的方向。把 KBR 类别拼进 action embedding 不会让冲突成为理论独有机制。

### 9.3 MEC→MAP→ALG 检验

| 层 | 最强解释 | 终判 |
|---|---|---|
| MEC | novelty 增大且差异/依赖存在时，单纯知识 transfer 可能不足；不同 scope/scale 资源共同出现 | 可保留为组织层解释，但 KBR effectiveness 未检验 |
| MAP | 把 schema/signature 视为 syntactic proxy，把 behavior contract 视为 semantic proxy，把 client-specific tradeoff 视为 pragmatic proxy | 前两者仍需测量，第三者明显把利益协商降格为 patch 难度 |
| ALG | 用 boundary embedding 进入 HGT，按 broadcasting/brokering/bridging 分配 bundle/rule/patch，并在 loss 加 scope/scale cost | 只是标签、route/head；通用模型有同样输入、动作和监督即可复制 |

理论没有产生一个通用方法无法表示的不可替代中间状态。若删除 boundary labels 仍保留 raw graph、tests、traces、cost 与 counterfactual labels，generic controller 能恢复所有决策。若禁止 raw features、强制通过三类 bottleneck，则模型可能因信息损失而变弱；即便偶尔泛化更好，也只是结构正则化，需要与等参数层级 bottleneck 比较，不能预先归因于理论。

## 10. Generic 反证与 coding-agent deletion test

### 10.1 same-information / equal-label / equal-action / equal-parameter 反证

构造完全公平的 generic HGT、temporal world model、POMDP 或 bilevel population controller，使其读取同一 `P0,q,G,K` 与 branch outcomes，输出同一 `ΔP,Wv,B,Tk,ΔCi` 动作，参数量、生成器、搜索预算和 container executions 全部相同。它可以从 client heterogeneity、action cost 和反事实结果直接学习 portfolio value，无需 syntactic/semantic/pragmatic 标签。

候选要保留独立理论算法贡献，必须出现预注册的方向冲突，并证明理论模型在未见 provider/client family 上超过所有这些 generic baselines；同时 boundary-state 打乱、中和、类别置换和关系反向应导致预期方向的行为变化。当前理论没有提供足以约束这些方向的已检验命题，故即便未来模型取胜，也不能排除层级偏置、额外 supervision 或搜索差异。

### 10.2 coding-agent deletion test

把 coding agent 替换为 program synthesizer、静态/动态分析、beam search 和同一个 population controller，系统仍能接收相同状态、产生相同 provider patch/shim/resource/AST rule/client patch，并由相同 oracle 评价。coding agent 能扩大自然语言目标下的工具搜索范围，也能降低构造多个代码工件的工程成本；它不是该研究机制不可删除的行动者。

若把下游消费者改成人类开发者，知识资源、迁移规则和兼容策略仍然成立。若把 provider agent 改成 CI 中的 synthesis service，研究问题也不改变。候选因此更接近“生态感知 API 演化与迁移 portfolio optimization”，而不是 coding-agent 独有广义安全。

## 11. 与 C1–C27 及既有候选的边界

| 既有边界 | 重叠 | 是否形成严格新增空间 |
|---|---|---|
| C1′ 未来依赖冲击与 migration option lattice | shim、迁移规则、client patch 与版本选择均回到迁移选择 | provider 共同设计是新起点，但最终控制结构同构，不能重开 C1′ |
| C10 演化/维护侵蚀 | 延迟更新、兼容债与维护成本直接重叠 | 只是把侵蚀放到 provider population，没有新的可训练机制 |
| C17 跨版本 verification debt | versioned bundle、hidden behavior、shim debt 重叠 | 合同与验证是评价/约束，不是独立生成能力 |
| C21 drift/version/freshness | 过时 API 知识和文档滞后直接重叠 | 新 provider 资源发布仍由 NovelAPIBench/ITAU 等近邻覆盖 |
| C24 multi-consumer pipeline semantic repair | 多 client hidden behavior 和传播直接重叠 | provider patch 联合生成扩大范围，却使任务变成 portfolio controller |
| C26 downstream coordinated vulnerability repair | security update adoption 与 client bridge 重叠 | 若以漏洞更新为主即退回 C26；若一般 API 演化，安全含义变薄 |

与 C3 evidence、契约/verifier 和 review-allocation 候选也有明显侧重交叉：machine-readable bundle 容易退化为证据供给，hidden behavior contract 容易退化为 verifier，client-specific bridge 分配容易退化为 review/repair allocation。它们只能作为本系统部件，不能再各自声称理论贡献。

## 12. 撤题门逐项执行

| 撤题门 | 证据 | 判定 |
|---|---|---|
| 外部损害真实且由 API 演化触发 | build break、silent behavior、延迟安全更新、维护成本均有直接文献 | 通过 |
| 不能靠拒绝或不改 API 获胜 | provider goal/security 设为硬约束 | 通过 |
| 有可运行环境 | 开放 provider + reverse clients + containers + hidden contracts 可做有限自建 | 条件通过 |
| 有同起点真实 counterfactual labels | 现有资产固定 upstream change；多 `ΔP × portfolio` 必须新造 | 未通过，但非单独致命 |
| 每个主要行动有新增可训练能力 | shim、bundle、AST rule、client patch 均有直接近邻 | 未通过，致命 |
| 理论提供已检验的方向机制 | Foerderer 明确不检验 KBR effectiveness；Carlile 不决定代码资源政策 | 未通过，致命 |
| 理论状态进入 forward/loss/action 且不可替代 | 可进入 embedding/cost/head，但 generic HGT 可复制 | 未通过，致命 |
| coding agent 不可删除 | synthesis/search/controller 替代后任务不变 | 未通过，致命 |
| full-composition baseline 之后仍有大幅独立能力 | 剩余是 portfolio assignment 与 search budget | 未通过，致命 |
| 能与 C1′/C24/C26 等旧案严格分离 | downstream migration、semantic repair、security adoption 大量重叠 | 未通过，致命 |

## 13. 终判与可保留的基础设施价值

终判为 **HIGH-CONFIDENCE TERMINAL NO-GO，保留候选数 0**。

这不是因为问题不重要，也不是因为实验尚未运行。决定性理由是：

1. **直接能力已被组合覆盖。** provider compatibility、结构化可执行知识、可复用 migration program、client repair 与 reverse-impact testing 都有可执行近邻。联合系统扩大了工程范围，没有产生独立的新生成能力。
2. **理论责任越界。** Foerderer 的案例可解释资源共存与 scope/scale，却明确没有检验 KBR effectiveness。把三类资源变成 action route 是本候选新假设，不能称为理论导出的策略。
3. **generic 替代成立。** 同信息、同监督、同动作、同参数的 HGT/world model/bilevel controller 能学习相同 portfolio；理论最多成为标签、bottleneck 或辅助 head。
4. **agent 删除成立。** 程序合成、分析、搜索和控制器的组合保持研究对象和结果不变，coding agent 只是实现载体。
5. **既有边界吸收。** 下游迁移、跨 client semantic repair 与安全更新协调分别回到 C1′、C24、C26，无法以 provider 视角重开。

以下资产仍值得作为未来两篇入选研究的共享基础设施或小型方法扩展，但不能包装成独立第三篇论文：provider-change × reverse-client 执行基准、multi-client seed 的 BigBag 扩展、versioned executable resource manifest，以及 provider contract/interaction snapshot 测试。

## 14. 关键候选句快照

以下句子仅用于肖老师两篇 ISR 的句责对照；它们是本审计自己的表述，不近似改写源文。

- K01：平台演化会把一次局部接口决策传播到大量下游仓库，使构建破坏、静默行为改变与安全更新迟滞同时成为可执行后果。
- K02：已有研究分别提供 provider 兼容实现、可执行知识包、可复用迁移程序和 client-specific repair，因此缺口不能定义为缺少其中任一工件。
- K03：真正尚未被单篇直接命名的任务，是在同一 provider 目标下联合生成这些工件并按 client population 分配资源。
- K04：Foerderer 等人观察了平台属性、知识边界与三类资源的共现，但明确没有推导资源有效性的命题。
- K05：据此，broadcasting、brokering 与 bridging 可以限定解释范围，却不能充当现成的最优行动标签。
- K06：候选模型读取 provider 变更目标、行为契约和 client heterogeneous graph，并输出 provider patch、versioned shim、executable bundle、AST migration program 与必要的 client bridge。
- K07：每个训练起点必须执行多个 provider-change × resource-portfolio 分支，才能为联合政策提供同起点的反事实监督。
- K08：现有公开基准大多固定 upstream release，因而不能直接识别 provider patch 与资源组合的联合价值。
- K09：理论映射若把 package edge 直接称为 knowledge dependency、把 test failure 直接称为 semantic boundary，就把组织层构念降成了技术特征别名。
- K10：同信息、同标签、同动作、同参数的 generic population controller 能从执行结果学习相同策略，这使理论专属能力的主张不能成立。
- K11：删除 coding agent 并换成程序合成、静态动态分析与搜索控制器后，研究输入、输出和外部结果保持不变。
- K12：因此，这个候选适合作为共享 benchmark 与系统基础设施，却不足以承担一篇独立 ISR 论文的理论和算法贡献。

## 15. 逐句 ISR 功能对照

### 15.1 K01

- 精确句键：`ACAA-I1 / ACAA-I1-S01`
- PRE：读者尚未知道为什么平台演化属于广义安全而非普通版本维护。
- SRC_NEW：源句以应用情境建立研究对象及其决策重要性。
- CAND_NEW：K01 把局部接口决策连接到跨仓库构建、行为和安全更新结果。
- REL：功能同位；都承担首个情境句，但事实与措辞完全独立。
- CIT：邻近引文应由 API breaking-change SLR、BreakBot、When LLMs Lag Behind 与 security-update 文献共同支持，不能用 Foerderer 代替技术后果证据。
- NEXT：K02 转入直接工作，收紧缺口。
- source_function_code：`CXT`
- candidate_function_code：`CXT/IMP`
- RESULT：保留

### 15.2 K02

- 精确句键：`DSDL-I5 / DSDL-I5-S02`
- PRE：K01 已建立重要后果，但尚未说明现有能力边界。
- SRC_NEW：源句压缩最近邻并指出其不能处理的对象。
- CAND_NEW：K02 枚举直接能力并禁止把任何单一工件写成空白。
- REL：功能同位；文献集合和技术命题不同。
- CIT：Adaptoring、NovelAPIBench、BigBag、SPELL、DepRepair 与 BreakBot 分别支持相邻能力。
- NEXT：K03 只保留联合任务作为待审空间。
- source_function_code：`ACK/GAP`
- candidate_function_code：`ACK/LIM`
- RESULT：保留

### 15.3 K03

- 精确句键：`DSDL-I5 / DSDL-I5-S03`
- PRE：单一工件空白已被排除。
- SRC_NEW：源句给出与近邻相比的第一项任务差异。
- CAND_NEW：K03 把最强候选限定为同一起点的联合生成与 population assignment。
- REL：位置参照，非功能同位；源句是任务差异，本句同时是钢人化后的暂存空位。
- CIT：需要前述近邻集合支持“单篇未直接命名”，不能声称“从未有人研究”。
- NEXT：K04 开始审计理论能否承担该联合动作。
- source_function_code：`GAP/MAP`
- candidate_function_code：`GAP`
- RESULT：改写

### 15.4 K04

- 精确句键：`ACAA-I2 / ACAA-I2-S04`
- PRE：K03 已得到最强技术空位，但理论责任未知。
- SRC_NEW：源句限定既有机制解释不了的关键关系。
- CAND_NEW：K04 区分 Foerderer 的观察结果与其明确未推导的有效性命题。
- REL：功能同位；都用原文边界阻止理论越权。
- CIT：直接引用 Foerderer 2019 结果与讨论，尤以原文“不打算推导 effectiveness propositions”的限制为依据。
- NEXT：K05 推出理论能做和不能做的动作边界。
- source_function_code：`LIM`
- candidate_function_code：`LIM`
- RESULT：保留

### 15.5 K05

- 精确句键：`DSDL-I6 / DSDL-I6-S05`
- PRE：K04 已确认资源有效性不是既有理论结果。
- SRC_NEW：源句说明理论差异应产生有方向的具体运算。
- CAND_NEW：K05 反向指出三类资源不能合法充当最优行动标签。
- REL：位置参照，非功能同位；源句建立正向机制，本句执行理论否证。
- CIT：Foerderer 2019 与 Carlile 2004 共同限定类别、过程与有效性之间的距离。
- NEXT：K06 暂时不依赖理论，完整给出算法 I/O。
- source_function_code：`MEC/ALG`
- candidate_function_code：`LIM/CON`
- RESULT：改写

### 15.6 K06

- 精确句键：`ACAA-M1 / ACAA-M1-S02`
- PRE：理论标签已被降级，但最强技术系统仍需具体化。
- SRC_NEW：源句给出总体数据流、输入和算法输出边界。
- CAND_NEW：K06 明确联合模型的 provider/client 输入与五类代码工件输出。
- REL：功能同位；承担方法总览中的 I/O 契约。
- CIT：方法设计句无需把候选结构伪装成既有事实；各输出的可行性由相应技术近邻支持。
- NEXT：K07 说明这种联合政策需要什么训练样本。
- source_function_code：`ALG`
- candidate_function_code：`ALG`
- RESULT：保留

### 15.7 K07

- 精确句键：`DSDL-M4 / DSDL-M4-S04`
- PRE：K06 已定义动作，但还没有可识别监督。
- SRC_NEW：源句说明样本标签如何获得及为何能对应目标状态。
- CAND_NEW：K07 要求同起点执行多 branch，避免把历史 patch 当最优标签。
- REL：功能同位；都是训练样本到监督的识别句。
- CIT：这是 C-NEW 设计要求，需在数据构建日志中验证，不能以文献引文代替实际分支执行。
- NEXT：K08 检查公开数据是否已经提供这种监督。
- source_function_code：`EVAL/ALG`
- candidate_function_code：`EVAL/ALG`
- RESULT：保留

### 15.8 K08

- 精确句键：`ACAA-M2 / ACAA-M2-S06`
- PRE：K07 已确定最小反事实样本单位。
- SRC_NEW：源句用筛选与保留规则界定最终可训练数据。
- CAND_NEW：K08 指出现有 benchmark 的固定 upstream 起点不能识别联合价值。
- REL：位置参照，非功能同位；源句是数据筛选，本句是数据可识别性否证。
- CIT：BUMP、DepBench、BigBag、NovelAPIBench 与 BreakBot 的 sample unit 和 oracle 是直接依据。
- NEXT：K09 进入构念测量与层级检查。
- source_function_code：`EVAL`
- candidate_function_code：`EVAL/LIM`
- RESULT：改写

### 15.9 K09

- 精确句键：`DSDL-I7 / DSDL-I7-S02`
- PRE：数据缺口已明确，仍需判断代码观测能否代表理论状态。
- SRC_NEW：源句把可观察通道与不可直接观测的理论状态区分开。
- CAND_NEW：K09 禁止将技术图/测试结果直接重命名为组织知识边界。
- REL：功能同位；都保护 latent construct 与 observable proxy 的差异。
- CIT：Foerderer 2019 对构念的原定义与 Carlile 2002/2004 的分析单位提供边界。
- NEXT：K10 检验即使保留这些 proxy，理论是否产生不可替代算法。
- source_function_code：`MEC/MAP`
- candidate_function_code：`MAP/LIM`
- RESULT：保留

### 15.10 K10

- 精确句键：`DSDL-M17_18 / DSDL-M17_18-S03`
- PRE：K09 已发现理论状态可能只是别名。
- SRC_NEW：源句用有方向、不可交换的理论运算改变 forward calculation。
- CAND_NEW：K10 用等参 generic controller 反证候选缺少理论专属运算。
- REL：位置参照，非功能同位；源句是正向机制计算，本句是等参替代检验。
- CIT：这是算法识别命题，必须用预注册等参实验支持；现阶段仅为终审逻辑，不写成实证结果。
- NEXT：K11 再做 coding-agent 删除检验。
- source_function_code：`MEC/ALG`
- candidate_function_code：`EVAL/LIM`
- RESULT：改写

### 15.11 K11

- 精确句键：`DSDL-Z3_6 / DSDL-Z3_6-S11`
- PRE：理论算法独占性已失败，但 coding-agent 特异性仍待审。
- SRC_NEW：源句给出研究适用边界并防止超出证据外推。
- CAND_NEW：K11 显示删除 agent 后 I/O 和结果不变，从而限定研究对象边界。
- REL：功能同位；都以边界条件收缩贡献。
- CIT：无需外部引文；由前述动作分解和替代系统的同构性推出。
- NEXT：K12 汇总终判及可保留价值。
- source_function_code：`BND`
- candidate_function_code：`BND/LIM`
- RESULT：保留

### 15.12 K12

- 精确句键：`ACAA-I6 / ACAA-I6-S04`
- PRE：技术、理论、数据和 agent 特异性均已完成审计。
- SRC_NEW：源句通常在机制铺垫后提出研究问题。
- CAND_NEW：K12 不提出 RQ，而把候选降为基础设施并终止独立论文资格。
- REL：无同功能锚点；仅借用引言收束位置，本句执行终审删除。
- CIT：由本文件第 8–12 节的组合证据支持，不增加新来源。
- NEXT：进入引用核验和机械审计，不再生成候选正文。
- source_function_code：`RQ`
- candidate_function_code：`BND/CONB`
- RESULT：删除

## 16. 肖老师写作逻辑总审计

本文件已按 `00F_逐段双ISR写作与引用审计协议.md` 与 `00W_肖帅勇两篇ISR源行句段主键Manifest.md` 回读源段。对照只学习句子功能、证据责任与推进顺序，不复制源句，不把“能解析句键”误判为功能同位。

- 情境句先落到可执行外部结果，再进入近邻；没有先用 KBR 术语制造问题。
- 近邻句分别指出工件已覆盖的能力，随后只暂存联合任务；没有用“尚无统一框架”制造虚假空白。
- 理论段先区分原文观察、未检验命题和本研究新假设，再讨论映射；没有让理论替代数据或算法证据。
- 方法段完整给出 I/O、样本、标签、张量、损失、动作、划分、算力和工件；所有数字均为来源报告或设计预算。
- 结论句由多道独立反证收束；没有用尚未运行作为 NO-GO 原因，也没有把待运行设计写成已完成发现。
- K03、K05、K08、K10 仅有位置或局部句责相似，已明确标注“位置参照，非功能同位”。K12 无同功能锚点，已如实标注。

## 17. 引用核验表

| 文献 | 元数据/全文核验 | 支持的具体命题 | 不得支持的命题 |
|---|---|---|---|
| Foerderer et al. 2019, DOI 10.1111/isj.12186 | Otero 元数据 + 本地全文完整回读 | 平台前因、知识边界、KBR 类别及 scope/scale 观察 | KBR 的因果有效性、最优 routing、自动 agent policy |
| Carlile 2002, DOI 10.1287/orsc.13.4.442.2953 | 期刊原文回读 | boundary object、共同 lexicon/meaning/interest 与跨边界处理能力 | 技术 contract test 等同 shared meaning |
| Carlile 2004, DOI 10.1287/orsc.1040.0094 | 期刊原文回读 | transfer/translation/transformation 与 novelty 下的层级关系 | client patch 等同 pragmatic transformation |
| Star & Griesemer 1989, DOI 10.1177/030631289019003001 | 原文定义段核验 | 边界对象的局部适应与跨场域共同身份 | 自动资源分配、代码修复或最优 portfolio |
| When LLMs Lag Behind, arXiv:2604.09515 | HTML/PDF 正文回读 | API evolution 引发 parametric knowledge conflict；270 updates/8 libraries | provider portfolio 或生态因果效果 |
| NovelAPIBench, arXiv:2606.03657 | HTML/PDF 正文回读 | 知识 bundle 成分、可执行 novel-API tasks、组件并非可互换 | provider patch 的最优选择 |
| BigBag, arXiv:2606.24446 | HTML 正文与失败分析回读 | agent 生成 executable AST transformation、cross-client transfer | hidden behavior 已被完全保证 |
| DepRepair, arXiv:2607.17957 | HTML 正文回读 | 95 个跨生态更新、structured evidence 与 client patch | provider-side joint evolution |
| SPELL, arXiv:2602.01107 | HTML 正文回读 | executable examples 到 reusable scripts 的生成与验证 | 资源 portfolio 的组织效果 |
| Breaking Changes SLR, arXiv:2605.24397 | HTML 正文回读 | 97 studies、66 strategies、provider/client actor 版图 | 任一 primary work 的精确因果效应 |
| APIfix, DOI 10.1145/3485538 | ACM/OOPSLA 原文与元数据回读 | output-oriented API migration transformation synthesis | provider patch 或 agent 特异性 |
| Adaptoring, arXiv:2401.07053 | HTML/PDF 正文回读 | alternative API adapter 生成、API 演化选项 | 大规模 client portfolio value |
| BUMP, DOI 10.1109/SANER60148.2024.00024 | 论文与公开仓库核验 | 571 个可复现 breaking dependency updates | 同一 provider 目标的多个 `ΔP` |
| BreakBot artifact, DOI 10.5281/zenodo.7475823 | artifact 页面与论文材料核验 | provider PR 的 static reverse-dependency compatibility impact | 自动生成兼容或迁移工件 |
| ITAU, DOI 10.1145/3830085 | ACM 元数据/正文核验 | versioned API KB、incompatible usage 检测与 repair | provider ecosystem policy |
| Perfection Paradox, DOI 10.1145/3772363.3798429 | CHI EA 2026 HTML 全文回读 | AIP 微调的 provider-side API specification generation 与 expert curation | 可执行 provider patch、下游行为兼容或 portfolio |
| HTTP Behavioral Signatures, arXiv:2604.02544 | v2 HTML 全文回读和公开日志入口核验 | 9 种 coding agent 的文档抓取行为与门户 analytics 限制 | machine-readable resource 的效果；作者也明确未测 |

## 18. 最终机械审计清单

- [x] 只把候选当作内部终审，没有写入正式论文语气。
- [x] 明确给出终判与保留候选数 0，没有为第三篇凑数。
- [x] 完整区分 T-OBS、T-UNT 与 C-NEW。
- [x] 给出真实损害、介入时点、可见/隐藏状态及正常/风险/纠正动作。
- [x] 钢人化 actual provider patch、versioned shim、bundle、AST program 和 client bridge。
- [x] 给出 I/O、工具行动、population graph、张量、架构、损失、policy、split、泄漏、算力和 checkpoints。
- [x] 说明现有公开资产为何不能直接识别同起点联合政策，也说明有限自建环境如何执行。
- [x] 完成 full-composition、等参 generic 和 coding-agent deletion 反证。
- [x] 与 C1′、C10、C17、C21、C24、C26 以及 evidence/verifier 边界逐项核对。
- [x] 对新增 Google CHI EA 与 agent documentation portal 工作按全文证据降权，没有把行业网页当空白证据。
- [x] 关键候选句均含 PRE、SRC_NEW、CAND_NEW、REL、CIT、NEXT、RESULT。
- [x] 每条记录分别给出 source_function_code 与 candidate_function_code。
- [x] RESULT 只使用保留、改写、拆分、合并、删除五种允许动作中的值。
- [x] 功能不同的句子明确标为“位置参照，非功能同位”或“无同功能锚点”。
- [x] 未运行候选始终使用设计、待检验或条件语气，没有写成已完成发现。
- [x] 文中来源报告的数字与候选预算已明确区分。
