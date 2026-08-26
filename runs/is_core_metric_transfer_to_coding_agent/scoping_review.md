# AIS Basket 中可迁移到 coding agent 的核心客观指标：范围性调研

## 1. 这次调研与既有工作的关系

此前确实做过一轮高度相关的筛选：`runs/coding_agent_unique_metric_transfer_from_is_benchmarks`。该轮从 956 篇已经被前序流程判定为“具有 IS 特色的客观 benchmark 改进研究”的文章出发，完成 945 篇，保留 680 篇，但只有 11 篇被模型评为 `transfer_strength=strong`。

旧轮不是本次问题的完整答案。它在进入指标迁移之前，已经要求来源文章以软件/信息系统方案设计和客观 benchmark 改进为中心。因此，它系统性排除了以下可能很重要的来源：

- 把某个结果变量作为核心，但不设计软件制品的行为研究；
- 对结果变量进行理论化、概念化或构念开发的文章；
- 研究 human–AI collaboration、delegation、resilience、effective use、process behavior 的观察或实验研究；
- 结果变量本身可迁移为 coding-agent benchmark，但原文没有“提点”的文章。

旧轮的价值在于提供候选词族；本轮则把判断单位改成“核心结果变量及其理论结构”，不再要求原文必须设计软件制品。

## 2. 本轮范围与方法

- 元数据全集：`database/ALL_AIS_Basket_11.csv`，17,745 条。
- 本地全文全集：`database_fulltext_all`，13,910 篇 Markdown 全文。
- 先在题名、摘要和关键词中检索九组结果变量词族，再精读代表性全文。
- 词法命中只用于召回，不能当作纳入结果；各词族相互重叠。

初步词法命中量：

| 词族 | 命中量 |
|---|---:|
| effective use | 78 |
| calibrated/appropriate reliance | 28 |
| human–AI complementarity | 35 |
| resilience/recovery | 93 |
| process integrity/workaround/shortcut | 67 |
| information quality/situation awareness | 283 |
| accountability/traceability/transparency | 319 |
| adaptation/learning | 152 |
| fairness/privacy/security | 118 |

本轮对候选核心指标采用六项标准：

1. 能由日志、任务真值、测试、差异、时间或行为结果客观计算；
2. 不是 correctness、time、productivity 的改名；
3. coding agent 的自主行动、工具调用、仓库环境或人机委派至少有一项不可被删去；
4. 能被 coding-agent 设计干预，而不是只能事后描述；
5. 能围绕同一指标形成三至四项研究；
6. 其贡献不会因基础模型升级或某个 benchmark 很快饱和而失效。

## 3. 核心发现

### 3.1 第一优先级：人–coding-agent 互补性实现率

最成熟的正式指标来源是 Hemmer et al. (2025), *Complementarity in Human-AI Collaboration: Concept, Sources, and Evidence*, EJIS, DOI: 10.1080/0960085X.2025.2475962。

设人单独完成任务的平均损失为 `L_H`，agent 单独完成的损失为 `L_A`，人–agent 团队的损失为 `L_T`：

- Complementary Team Performance 成立当且仅当 `L_T < min(L_H, L_A)`；
- Complementarity Potential：`CP = min(L_H, L_A) - L_oracle`；在有完整真值、oracle loss 为 0 时，`CP = min(L_H, L_A)`；
- Complementarity Effect：`CE = min(L_H, L_A) - L_T`；
- 可进一步定义 Complementarity Realization Rate：`CRR = CE / CP`。

这比“团队准确率”更强：团队只要超过较弱一方并不算互补，必须超过人和 agent 中单独表现更好的那一方。文章还把潜力和实现效果分成两部分：

- inherent complementarity：某一方本来就能解决另一方解决不了的实例；
- collaborative complementarity：双方单独都没得到正确答案，但互动后产生了更好的新答案。

其两个理论来源是信息不对称和能力不对称。这可以直接变成 coding-agent 设计变量，例如仓库上下文在双方之间如何分布、何时由 agent 主导、何时请求人类、如何交换证据、何时共同修改方案。

与它组成同一文献链的关键工作：

- Fügener et al. (2021), *Will Humans-in-the-Loop Become Borgs?*, MISQ：正式计算 unique human knowledge，即“agent 错而人对”的任务比例；证明 AI 建议提高个人准确率的同时，可能消灭人类的独特知识并损害群体表现。全文：`database_fulltext_all/00186_2021_will-humans-in-the-loop-become-borgs-merits-and-pitfalls-of-working-with-ai.md`。
- Baird & Maruping (2021), *The Next Generation of Research on IS Use*, MISQ：把 agentic IS 的独特性定位为权利和结果责任的双向委派，提出 appraisal、distribution、coordination 三个委派机制。全文：`database_fulltext_all/10752_2021_the-next-generation-of-research-on-is-use-a-theoretical-framework-of-delegation-to-and-from-agen.md`。
- Liu et al. (2025), *Find the Good. Seek the Unity*, MISQ：在真实场景中用 Team-vs-Human、Team-vs-AI、Team-vs-Team 三类 KPI 建模动态委派。全文：`database_fulltext_all/03476_2025_find-the-good-seek-the-unity-a-hidden-markov-model-of-human-ai-delegation-dynamics.md`。

适合的 thesis 系列：

1. 仓库信息不对称与上下文交换如何提高 `CRR`；
2. 基于能力边界的任务分配/升级如何提高 `CRR`；
3. 证据化 review 与反建议机制如何提高 collaborative CE；
4. 长期重复使用中，如何同时提高 CE 并保存 unique human contribution。

主要优点：这是已有正式数学定义的客观核心指标，具有很强的 IS 身份，而且不会因模型升级失效——模型升级只会改变 `L_A`、`CP` 和可实现空间，是否真正产生互补仍然是问题。

主要成本：必须收集人单独、agent 单独、人–agent 团队三个条件，通常需要开发者实验。

### 3.2 第一优先级：coding-agent 情境意识

Nadj, Maedche, & Schieder (2020), *The Effect of Interactive Analytical Dashboard Features on Situation Awareness and Task Performance*, DSS，把 situation awareness 定义为当前状态知识的完整性和准确性，并用 SAGAT freeze-probe 客观测量：在任务中随机冻结界面、隐藏信息、询问当前状态和未来影响，再用冻结时刻的日志真值计算答对比例。全文：`database_fulltext_all/10216_2020_the-effect-of-interactive-analytical-dashboard-features-on-situation-awareness-and-task-performa.md`。

该研究最重要的发现不是“SA 提高绩效”这一常识，而是自动分析功能可以提高任务绩效、同时降低 SA，形成 out-of-the-loop 风险。这提供了典型的 IS 写作逻辑：短期任务分数更高，不等于人机系统状态更好。

迁移到 coding agent 后，可以定义三层客观 probe：

- perception：agent 是否知道当前分支、改动文件、失败测试、可用工具和关键依赖；
- comprehension：agent 是否理解这些状态之间的因果关系、约束和风险；
- projection：agent 是否能预测某次修改、命令或依赖变化将造成什么后果。

基本得分可以是 `ASA = correct repository-state probes / applicable probes`，同时按三层和任务阶段分层报告。probe 的答案必须对照仓库、测试、构建或运行时真值，而不是由人主观评分。

适合的 thesis 系列：

1. 建立 coding-agent SAGAT 式客观测量及其预测效度；
2. 改造 exploration/context acquisition，提高 perception；
3. 改造依赖与影响推理，提高 comprehension/projective SA；
4. 在测试失败、环境改变和恢复阶段维持 SA。

主要优点：不必把人类主观量表当结果；可直接改 agent；天然具有多个认知层级和多个软件工作阶段；也与我们此前考虑的 objective situational awareness 完全相接。

主要风险：SA 是近端状态指标，不必然等于最终软件变更成功。因此 thesis 必须同时验证 SA 对 regression-safe success、恢复表现或错误率的增量解释力，但不能把这些普通绩效变量替代 SA 本身。

### 3.3 第一优先级：验证过程完整性 / 关键步骤捷径率

Ghasemaghaei & Turel (2022), *Why Do Data Analysts Take IT-Mediated Shortcuts?*, JMIS，把 IT-mediated shortcut 定义为为了更快完成任务而跳过一个或多个规定步骤。文章用三个实验客观记录 shortcut-taking 和任务表现，并用 ego depletion、自我调节和目标设定理论解释为什么复杂 IT 和结果压力会诱发捷径。全文：`database_fulltext_all/25480_2022_why-do-data-analysts-take-it-mediated-shortcuts-an-ego-depletion-perspective.md`。

这可以迁移为 coding-agent 的 `Verification Process Integrity (VPI)`：

`VPI = 已完成且产生有效证据的关键验证步骤权重 / 当前任务适用的关键验证步骤总权重`

相应的 shortcut rate 为 `1 - VPI`。关键步骤可按任务预注册，例如：

- exploration：读取必要文件和依赖，而不是凭局部片段修改；
- change：变更范围符合任务与架构约束；
- verification：执行规定测试、静态检查、构建和 diff review；
- recovery：出现失败后重新诊断而不是删除/绕过检查。

适合的 thesis 系列：

1. agent 在 token、时间或并发预算压力下何时跳步；
2. 过程可视化、检查单或阶段门控如何提高 VPI；
3. 学习目标式提示与单纯结果目标式提示如何影响 VPI；
4. 自适应验证预算如何在完整性与成本之间取得更好前沿。

主要优点：完全由工具轨迹和执行日志计算；非常适合改造现有 coding agent；无需大规模人类实验；模型再强也仍面临预算、速度和验证充分性的权衡。

主要风险：不能把“步骤越多”误当成完整性。必须预先定义任务所需的 evidence-bearing steps，并允许功能等价路径，否则指标会奖励形式主义和无效工具调用。

### 3.4 第二优先级：自主软件变更韧性

Tim & Leidner (2023), *Digital Resilience: A Conceptual Framework for Information Systems Research*, JAIS，把数字韧性区分为 continuity、adaptation 和 advancement：冲击中维持连续性、适应新状态、并在冲击后形成更强能力。全文：`database_fulltext_all/06140_2023_digital-resilience-a-conceptual-framework-for-information-systems-research.md`。

迁移后可定义 agent 在仓库冲击下的客观表现：

- continuity：无关功能保持率、冲击后的性能降幅；
- adaptation：发现假设失效后的恢复成功率、恢复步骤/成本；
- advancement：恢复后在后续相关任务上的复发率是否下降。

它适合动态依赖、测试变化、冲突、环境漂移和跨任务记忆研究。优点是长期稳定且有阶段性；缺点是要构造可信的 shock benchmark，实验工程量高于 SA 和 VPI。

### 3.5 第二优先级：仓库表示/信息质量

Wang & Strong (1996), *Beyond Accuracy: What Data Quality Means to Data Consumers*, JMIS，把数据质量组织为 intrinsic、contextual、representational、accessibility 四类，而不是只看 accuracy。全文：`database_fulltext_all/24796_1996_beyond-accuracy-what-data-quality-means-to-data-consumers.md`。

可迁移为 coding agent 内部仓库表示的质量：正确性、任务相关完整性/及时性、跨制品一致表示、可检索性与访问安全。它特别适合做 situation awareness 的上游设计质量或中介变量，但单独作为最终 SOTA 核心指标略弱，因为“表示质量高”仍需证明会改善 agent 行动。

### 3.6 更适合作为理论机制，而非 thesis 最终核心指标

- appropriate/calibrated reliance：非常适合解释接受、拒绝、修改、升级 agent 输出的行为，但 trust 本身常用主观量表测量；应把客观 reliance discrimination 当作 complementarity 的机制或子指标。
- effective delegation：Baird & Maruping 的 appraisal、distribution、coordination 极其贴合 agentic IS，但原文没有提供一个成熟的单一客观总分；更适合作为设计理论，结果用 CE/CRR 或 delegation regret 衡量。
- effective use：Burton-Jones & Grange (2013) 的 transparent interaction、representational fidelity、informed action 是很强的 IS 理论模板，但过于通用。全文：`database_fulltext_all/01272_2013_from-use-to-effective-use-a-representation-theory-perspective.md`。
- algorithm aversion/appreciation：核心是对人或算法的相对偏好，并不保证决策正确；不适合作为“提点”的最终指标。全文：`database_fulltext_all/05990_2024_an-integrative-perspective-on-algorithm-aversion-and-appreciation-in-decision-making.md`。
- accountability、transparency、explainability：多为感知或治理机制；除非把它们落到可追溯责任链、违规率或审计发现率，否则不应直接当客观核心指标。

## 4. 候选比较

评分范围 1–5；“既有度”表示来源文献是否已经给出成熟定义/测量，而非我们自行发明。

| 候选核心指标 | 客观性 | coding-agent 独特性 | IS 理论背书 | 四研究扩展性 | 抗模型升级 | 既有度 | 综合判断 |
|---|---:|---:|---:|---:|---:|---:|---|
| Complementarity Effect / CRR | 5 | 5 | 5 | 5 | 5 | 5 | 最强 IS 方案，但需要人类实验 |
| Agentic Situation Awareness | 5 | 4 | 5 | 5 | 5 | 4 | 最适合延续现有 objective-SA 思路 |
| Verification Process Integrity | 5 | 5 | 4 | 5 | 5 | 4 | 最容易改 agent、跑 benchmark、形成四篇 |
| Autonomous Change Resilience | 5 | 4 | 5 | 5 | 5 | 4 | 长期价值强，benchmark 构建较重 |
| Effective Delegation / Delegation Regret | 5 | 5 | 5 | 5 | 5 | 3 | 理论最贴 agent，客观总指标需开发 |
| Repository Representation Quality | 5 | 4 | 5 | 4 | 5 | 4 | 更适合做 SA 的上游变量 |
| Unique Human Knowledge | 5 | 5 | 5 | 4 | 5 | 5 | 适合作为 complementarity 系列的一章 |

## 5. 当前结论

如果目标是“既像 benchmark 提点，又明显不是普通 CS 刷分”，最值得继续深挖的不是单一 task success，而是以下三个方案：

1. **人–coding-agent 互补性实现率 CRR**：现成的正式指标，IS 身份最强；核心问题从“agent 是否赢”变成“人–agent 系统是否实现了原本存在的互补潜力”。
2. **coding-agent objective situation awareness**：最贴近已有构念尝试；可用 SAGAT 式真值 probe 客观测量，并围绕感知、理解、预测以及工作阶段组织系列研究。
3. **verification process integrity**：最适合仅改造现有 coding agent 并做低成本 benchmark；重点不是多调用工具，而是在约束下不省略必要的证据生成与验证过程。

三者也可以形成清楚的层次，但不应在一篇 thesis 中并列为三个核心结果：

`Situation awareness（知道发生了什么） → process integrity（按充分过程行动） → complementarity / verified outcome（人机系统产生了什么结果）`

若必须只选一个作为整个 thesis 的 headline outcome：

- 能做开发者实验：优先 `CRR`；
- 主要做自动 benchmark：优先 `VPI`；
- 希望延续此前构念开发并形成最鲜明的认知型 IS 贡献：优先 `Agentic Situation Awareness`。
