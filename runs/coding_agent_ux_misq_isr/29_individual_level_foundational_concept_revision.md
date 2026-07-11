# 个体层基础概念修订：只从 individual/dyadic 协作努力出发

> **已废弃 / superseded.** 这份文件仍然把 collaborative overload、perceived user effort、AI teammate、human-AI conflict 等多个概念放在同一条基础链中，不够严格。当前有效版本见 `30_single_foundational_concept_collaborative_overload.md`，只以 **collaborative overload** 一个基础概念为起点。

## 1. 当前硬边界

这次边界必须更严格：

> 我们只使用 **individual/dyadic level** 的基础概念。

也就是说，基础概念必须描述个人或二元关系中的感知、努力、负担、冲突、满意度、意愿或行为。凡是研究层级不在个人或人-agent/人人二元互动上的文献，都不进入当前概念开发论证。

因此，当前概念开发的起点应写成：

> **individual-level collaborative overload / perceived collaborative effort**

中文暂译：

> **个体层协作过载 / 感知协作努力**

更准确地说，我们要借鉴的是：

> 个体在与另一个行动者协作时，因为需要回应、配合、理解、追踪、整合和修正对方行动，而感知到的协作性努力或负担。

这个基础概念和 coding agent 的连接点不是“协调成本”这个宽泛词，而是：

> 用户为了和一个会自主行动的 agent 完成任务，需要付出多少协作性协调努力。

## 2. 为什么这个基础概念适合

### 2.1 它是个人感知

Collaborative overload 的核心是：协作需求超过个人资源后，个人会感到注意力、时间和精力被挤压。Lansmann and Klein 的 ECIS 2018 综述明确强调 overload 是主观体验，不同员工会有不同感知。

这和我们的测量目标一致。我们测量的是：

> 某个开发者在一次 coding agent 任务中，感到自己为了协调 agent 付出了多少额外努力。

### 2.2 它不是 usability

Usability 问的是系统是否容易学、容易用、有效率。

我们的问题不是“这个工具界面是否好用”，而是：

> 即使这个工具能用、也有用，用户为了让 agent 的自主行动不偏离任务和代码上下文，还需要投入多少协作性努力？

这更接近 collaborative effort，而不是 usability。

### 2.3 它能解释你提到的实践现象

你提到的两个现象：

- CLI 里不方便查看改动；
- 一直通知审批让人疲劳。

它们不是同一种 usability 问题，而是同一种协作努力问题的不同表现：

- 看不清改动，会增加用户理解和追踪 agent 行动的努力；
- 审批太频繁，会增加用户回应、判断和恢复任务节奏的努力。

也就是说，用户累的不是“按钮难点”，而是“为了和 agent 一起完成任务，我不得不不断重新进入协作状态”。

## 3. 当前最合适的基础概念簇

### 3.1 Collaborative overload

适合作为负向基础概念。

它帮助我们说明：协作本身会消耗个人资源。当协作请求、沟通、回应、帮助和同步需求超过个人可承受范围时，协作会从资源变成负担。

迁移到 coding agent：

> coding agent 本来是帮用户完成任务的协作者，但当它不断要求用户审批、解释、检查、纠偏和接管时，协作本身会变成用户的额外负担。

不能直接照搬的地方：

- collaborative overload 常关注人与人之间的协作；
- coding agent 不是人类同事；
- coding agent 的行动会进入代码库并改变项目状态；
- 用户负担不只是回应请求，还包括理解 diff、验证测试、判断副作用和决定是否接管。

所以，它是基础，但不是最终构念。

### 3.2 Perceived user effort in agent interaction

`Scratch my back and I'll scratch yours` (2022, Information & Management) 研究 recommendation agent 中 user effort 和 recommendation agent effort 对 perceived recommendation agent quality 的影响，并引入 perceived interdependence 和 reciprocity。

这篇很有用，因为它具备三个条件：

- 个体层；
- 人-agent 互动；
- effort 是核心变量。

迁移到 coding agent：

> 用户会感知自己在与 agent 合作中投入了多少 effort；但 coding agent 的 effort 不只是输入偏好或配合推荐，而是协调一个会读写代码、运行命令并产生副作用的 agent。

不能直接照搬的地方：

- recommendation agent 主要影响选择和建议；
- coding agent 会执行任务并改变代码状态；
- coding agent 使用中的 user effort 包含追踪、审批、验证、纠偏和接管。

### 3.3 AI agents as team members

`AI Agents as Team Members` (2023, JMIS) 研究 AI agents 作为 virtual team members 时，人们对 satisfaction、conflict、trustworthiness 和 willingness to work with 的感知。摘要显示，AI team member 会降低 process satisfaction；当 AI 表现好时，相比同等表现的人类成员，参与者感知到更少 conflict。

这篇重要，是因为它已经把 AI 作为协作对象，而不是被动工具。

迁移到 coding agent：

> coding agent 也不是普通工具，而是被用户当作任务协作者来处理；因此用户体验不只来自产出质量，也来自协作过程中的满意度、冲突和继续合作意愿。

不能直接照搬的地方：

- AI team member 不一定直接修改代码；
- coding agent 的行动通过 diff、命令、测试和权限请求呈现；
- 用户还要判断 agent 行动是否可接受、可恢复、可继续。

### 3.4 Human-AI conflict

`Partner or Rival? How Human-Artificial Intelligence Conflict Shapes Artificial Intelligence Aversion` (2026, JMIS) 研究 human-AI conflict、goal interdependence、cognitive dissonance 和 AI aversion。

它适合作为相邻个体层理论，因为 coding agent 也会出现用户意图和 agent 行动之间的冲突。

迁移到 coding agent：

> 当 agent 的修改方向、风险判断或任务理解与用户不一致时，用户不只是“不信任”，而是需要投入额外努力去识别冲突、解释冲突、纠正冲突，并判断是否继续委托。

不能直接照搬的地方：

- human-AI conflict 关注判断冲突；
- coding agent 中的冲突还会沉淀为代码变更、测试失败、架构副作用或回滚需求；
- 因此冲突只是协调负担的来源之一，不等同于协调负担。

### 3.5 Distributed cognition in software design

`Distributed cognition in software design` (2014, MISQ) 用软件从业者实验研究 design patterns 和 collaborating pairs 对软件设计结果的影响。摘要显示，设计模式提高质量、减少时间、提高满意度；协作配对能提升设计质量，但需要更多时间。

它不是主基础概念，但能帮助我们把个体协作努力放进软件设计情境。

迁移到 coding agent：

> coding agent 同时像协作者，也像外部认知工件。用户不是单纯和人协作，也不是单纯使用工具，而是和一个会生成、修改和解释代码的行动性工件共同完成软件任务。

不能直接照搬的地方：

- 它研究人类协作和设计模式；
- coding agent 会自主推进任务；
- 用户必须持续判断 agent 的行动是否仍然符合任务意图和代码上下文。

## 4. 新构念定义

建议把当前构念定义为：

> **编码代理委托协调负担**是指：开发者在一次具体编程任务中，将部分工作委托给能够自主执行并改变代码状态的 coding agent 后，为了使 agent 的行动与自己的任务意图、代码依赖、风险边界和最终责任保持一致，而感知到必须投入的额外协作性协调努力。

英文定义：

> **Perceived coordination burden in coding-agent delegation** refers to a developer's perceived collaborative coordination effort required to keep a delegated coding agent's autonomous code-related actions aligned with the developer's task intent, code dependencies, risk boundaries, and residual responsibility during a concrete programming task episode.

这个定义中最关键的是：

- **developer's perceived**：个人感知；
- **collaborative coordination effort**：来自协作努力/协作过载，而不是宽泛成本；
- **delegated coding agent**：不是普通工具；
- **autonomous code-related actions**：体现 agentic；
- **task intent, code dependencies, risk boundaries, residual responsibility**：体现 coding agent 特有边界。

## 5. 它和基础概念的严格区别

| 基础或相邻概念 | 能借鉴什么 | 为什么必须改造 |
| --- | --- | --- |
| collaborative overload | 协作需求会消耗个人资源 | coding agent 的负担不是一般协作过多，而是委托后协调 agent 的自主代码行动 |
| perceived user effort | 用户会感知自己在 agent 互动中投入了多少努力 | coding agent 的用户努力不仅是提供输入，还包括追踪、审批、验证、纠偏和接管 |
| AI teammate process satisfaction/conflict | AI 作为协作对象会改变过程满意度和冲突感 | coding agent 不只是队友类型，而是会改变代码状态的任务执行者 |
| human-AI conflict | 人和 AI 的目标/判断冲突会影响态度 | 冲突只是来源之一；我们测量的是用户为了处理这些冲突和依赖而投入的协调努力 |
| distributed cognition in software design | 软件任务中的协作和外部认知工件会影响质量、时间、满意度 | coding agent 同时是协作者和行动性代码工件，需要额外处理委托、验证和恢复 |

## 6. 暂定维度

这些维度只是 sensitizing concepts，后续 Reddit 和访谈可以推翻、合并或新增。

| 暂定维度 | 个体层含义 |
| --- | --- |
| 意图与边界协调努力 | 用户为了让 agent 明确任务目标、范围、约束和不可触碰区域而投入的努力 |
| 行动过程跟踪努力 | 用户为了理解 agent 做了什么、为什么做、改了哪里而投入的努力 |
| 审批与注意力分流努力 | 用户为了处理权限请求、继续/停止判断和风险分流而投入的努力 |
| 代码变更整合努力 | 用户为了整合 diff、测试、日志和上下文并判断是否接受而投入的努力 |
| 接管与恢复决策努力 | 用户为了判断何时接管、回滚、纠偏或重新委托而投入的努力 |

## 7. 前因和后果应该怎么研究

### 可能前因

- agent 自主性水平；
- agent 行动可见性；
- diff 展示清晰度；
- 审批请求频率；
- 审批请求风险区分度；
- agent 可靠性；
- 用户对代码库熟悉度；
- 任务复杂度；
- 代码依赖复杂度；
- 恢复/回滚机制；
- 用户 coding agent 使用经验。

### 可能后果

- perceived control；
- process satisfaction；
- continued delegation intention；
- willingness to work with the agent；
- takeover frequency；
- verification fatigue；
- AI aversion；
- perceived productivity gain；
- task completion quality。

这个模型的逻辑是：

> 工具和任务特征影响用户感知到的协作性协调努力；这种努力再影响用户是否觉得可控、是否满意、是否愿意继续委托，以及是否真正获得生产率收益。

## 8. 当前最稳的论文表述

可以这样写：

> Prior individual-level research on collaborative overload and user effort suggests that collaboration can impose personal costs when coordination demands consume attention, time, and cognitive resources. Research on human-agent interaction further shows that users evaluate both their own effort and the agent's effort, while AI teammate studies suggest that AI collaborators can shape process satisfaction, perceived conflict, and willingness to work together. However, these concepts do not fully capture coding-agent use, where developers delegate programming tasks to agentic systems that autonomously inspect, modify, and test mutable code artifacts while developers retain residual responsibility. We therefore develop perceived coordination burden in coding-agent delegation as a coding-agent-specific UX construct that captures the collaborative coordination effort developers perceive when keeping an agent's autonomous code work aligned, traceable, approvable, verifiable, and recoverable during a concrete programming task episode.

中文版本：

> 个体层的协作过载和用户努力文献说明，协作需求会消耗个人注意力、时间和认知资源；人-agent 互动文献进一步说明，用户会评价自己和 agent 在互动中投入的努力；AI 协作对象研究则表明，AI 会影响用户的过程满意度、冲突感和继续合作意愿。然而，这些概念不能完整刻画 coding agent 使用，因为开发者会把编程任务委托给能够自主检查、修改和测试代码工件的 agentic system，同时仍保留最终责任。因此，我们开发编码代理委托协调负担，用来描述开发者在具体编程任务中，为了让 agent 的自主代码工作保持对齐、可追踪、可审批、可验证和可恢复而感知到的协作性协调努力。

## 9. 后续工作

下一步只做 individual/dyadic 层级材料：

1. 整理 collaborative overload、perceived user effort、AI teammate process satisfaction/conflict、human-AI conflict、distributed cognition in software design；
2. 建一个层级筛选表，只保留 individual/dyadic；
3. 用 Reddit 评论检验用户是否自然表达了“协作性协调努力”，尤其是追踪改动、审批分流、验证整合、接管恢复这些具体表现；
4. 不再把非 individual/dyadic 层级文献放进理论链条。

当前结论：

> 主基础概念应从 **individual-level collaborative overload / perceived collaborative effort** 出发；我们的新构念是 coding-agent-specific 的 **perceived collaborative coordination effort/burden**。
