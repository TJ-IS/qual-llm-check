# 单一基础概念版：从 collaborative overload 到 coding-agent collaborative overload

> **未通过 database 概念存在性检验 / superseded.** 后续检索 `database/ALL_AIS_Basket_11.csv` 后发现，`collaborative overload` 和 `collaboration overload` 在数据库中精确命中为 0。因此，若标准是“基础概念必须被权威 IS 文献真实使用过”，本方向不能作为当前有效主线。检索结果见 `31_database_presence_check_foundational_concepts.md`。

## 1. 方法纠偏

这版严格模仿 Chen et al. (2024 MISQ) 的结构：

> 一个基础概念 + 一个新情境 + 说明原概念为什么不够 + 发展情境化构念和量表。

Chen et al. 的基础概念只有一个：

> usability

他们发展的是：

> voice-interaction usability

我们也只能选择一个基础概念。当前唯一基础概念定为：

> **collaborative overload**

我们要发展的情境化构念是：

> **coding-agent collaborative overload**

中文暂译：

> **编码代理协作过载**

本文件不再把其他概念放进概念开发主线。后续如需讨论相邻概念，只能放在区分效度、前因、后果或竞争模型部分，不能作为基础概念。

## 2. 基础概念：collaborative overload

**Collaborative overload** 描述的是：个体在协作活动中，因为需要回应、帮助、同步、协调或参与过多协作要求，导致自己的时间、注意力、精力和任务推进能力被过度消耗的状态。

它适合作为基础概念，因为它本身就是：

- individual-level；
- subjective/perceived；
- collaboration-related；
- burden/overload-oriented；
- directly linked to attention, time, effort, exhaustion, productivity, and well-being.

这和我们要研究的 coding agent 使用体验高度接近。很多 coding agent 用户并不是因为 agent 完全没用才不用，而是因为使用 agent 后产生了新的协作要求：要盯着它、审批它、看它改了什么、判断它是否越界、验证它的结果、决定是否接管。也就是说，agent 带来的不是单纯“使用成本”，而是“协作要求超过个人可轻松处理范围”的过载感。

## 3. 为什么 collaborative overload 适用于 coding agent

Coding agent 使用可以被理解为一种人-agent 协作，因为用户不是只点击一个静态工具，而是把一个编程目标交给 agent，让它在任务过程中理解上下文、规划步骤、修改代码、运行命令、反馈结果，并在关键时刻要求用户回应。

因此，coding agent 会产生 collaborative overload 的典型条件：

1. 用户需要持续回应 agent 的请求；
2. 用户需要理解 agent 的中间行动；
3. 用户需要把 agent 的输出放回自己的任务目标中判断；
4. 用户需要在协作过程中分配注意力；
5. 用户需要承担协作失败后的修复成本。

这说明 collaborative overload 可以作为 coding agent UX 构念开发的基础概念。

## 4. 为什么原有 collaborative overload 不够

虽然 collaborative overload 适用，但不能直接照搬到 coding agent。原因不是“换了一个场景”，而是 coding agent 改变了协作过载的来源和结构。

### 4.1 协作对象不是人，而是可执行的 agentic artifact

传统 collaborative overload 主要关注个体面对协作请求、沟通、帮助和同步活动时的资源消耗。

Coding agent 中，协作对象不是普通人类协作者，而是能够自主执行任务的 agentic artifact。它不会只是请求用户协助，还会主动读取上下文、采取步骤、修改代码、运行命令，并把新的判断压力交还给用户。

因此，过载不只是来自“协作太多”，还来自“一个非人协作者持续生成需要用户解释和治理的行动”。

### 4.2 协作输出会改变代码状态

传统 collaborative overload 的协作输出多体现为沟通、请求、建议、帮助或共同任务推进。

Coding agent 的协作输出会变成代码变更、命令执行、测试结果、依赖调整和潜在副作用。用户面对的不是一条消息，而是一个可能已经改变项目状态的行动结果。

因此，用户的过载不只是回应过多，而是必须理解和评估 agent 对代码状态造成的影响。

### 4.3 协作过程包含频繁的权限交还

Coding agent 经常通过 approval、permission、confirmation、continue/stop 等机制把注意力交还给用户。

这些机制本意是让用户保留控制，但它们也会制造一种特殊的协作过载：用户需要不断判断这些请求是例行、安全、关键、危险还是应该拒绝。

传统 collaborative overload 没有充分刻画这种由 agentic action + permission handoff 造成的判断负担。

### 4.4 用户保留最终责任

Coding agent 可以执行部分任务，但用户通常仍要对最终代码质量、项目状态和提交结果负责。

因此，用户在协作中过载，不只是因为 agent 要求他们参与，而是因为他们必须在 agent 已经行动之后继续承担判断、验证、接管和修复责任。

这也是 coding agent collaborative overload 不同于一般 collaborative overload 的关键。

## 5. 新构念定义

**编码代理协作过载**是指：

> 开发者在一次具体编程任务中与 coding agent 协作时，因为 agent 的自主代码行动、权限交还、过程反馈和结果变更持续要求开发者理解、回应、验证、纠偏或接管，从而感知到自己的注意力、时间和认知资源被过度消耗的程度。

英文定义：

> **Coding-agent collaborative overload** refers to the extent to which a developer perceives excessive demands on attention, time, and cognitive resources when collaborating with a coding agent whose autonomous code-related actions, permission handoffs, process feedback, and output changes require the developer to understand, respond to, verify, correct, or take over during a concrete programming task episode.

这个定义保留了 collaborative overload 的核心：个体资源被协作要求过度消耗。

同时，它加入 coding agent 独有的情境条件：

- autonomous code-related actions；
- permission handoffs；
- process feedback；
- output changes；
- understand/respond/verify/correct/take over；
- concrete programming task episode。

## 6. 构念高低怎么理解

这是一个连续构念，不是 0/1。

低 coding-agent collaborative overload：

- 用户能轻松跟上 agent 的行动；
- 审批请求数量和风险层级可处理；
- 代码变更容易理解和验证；
- 用户不需要频繁中断自己的思路来恢复上下文；
- 用户觉得与 agent 协作没有明显挤占自己的注意力和任务推进能力。

高 coding-agent collaborative overload：

- 用户经常被 agent 的请求打断；
- 用户很难跟上 agent 做了什么；
- 用户需要花很多时间检查 diff、命令、测试和副作用；
- 用户需要反复纠正或限制 agent；
- 用户觉得和 agent 协作本身消耗了太多注意力、时间和认知资源。

## 7. 初步维度：只从 collaborative overload 扩展

这些维度不是从多个概念拼出来的，而是从 collaborative overload 的核心内涵扩展出来：

> 协作要求消耗个人资源。

Coding agent 情境下，协作要求主要表现为五类。

| 维度 | 定义 | 为什么属于 collaborative overload 的情境化扩展 |
| --- | --- | --- |
| 响应过载 | agent 的确认、权限、继续/停止请求让用户感到需要投入过多回应资源 | collaborative overload 中的协作请求，在 coding agent 中表现为权限交还和确认请求 |
| 追踪过载 | 用户为了跟上 agent 的多步行动、命令和代码修改而感到资源被过度消耗 | collaborative overload 中的同步要求，在 coding agent 中表现为行动轨迹同步 |
| 理解过载 | 用户为了理解 agent 为什么这样改、这些改动与任务有什么关系而感到吃力 | collaborative overload 中的共同理解要求，在 coding agent 中表现为对 agent rationale 和 code change 的理解 |
| 验证过载 | 用户为了确认 agent 的输出是否正确、安全、可合入而感到检查负担过高 | collaborative overload 中的协作质量保障要求，在 coding agent 中表现为代码验证和副作用判断 |
| 接管过载 | 用户为了判断何时暂停、纠偏、回滚、自己接手而感到决策负担过高 | collaborative overload 中的协作修复要求，在 coding agent 中表现为 takeover/recovery 判断 |

这些维度后续必须由 Reddit 评论和访谈来修订，不能预先当作最终结构。

## 8. 和 Chen et al. 的对应关系

| Chen et al. (2024) | 我们的研究 |
| --- | --- |
| 基础概念：usability | 基础概念：collaborative overload |
| 新情境：voice interaction with smart products | 新情境：coding-agent collaboration in programming task episodes |
| 为什么原概念适用：voice interaction 也是用户为达成目标而使用产品 | 为什么原概念适用：coding agent 使用包含持续协作要求，会消耗用户资源 |
| 为什么原概念不够：voice input/output、听觉顺序呈现、人机对话、拟人化等特征改变 usability 结构 | 为什么原概念不够：agentic code action、permission handoff、code-state changes、verification/takeover responsibility 改变 collaborative overload 结构 |
| 新构念：voice-interaction usability | 新构念：coding-agent collaborative overload |
| 数据作用：用户评论用于发现维度 | 数据作用：Reddit 评论用于发现 coding-agent collaborative overload 的维度 |
| 后续验证：多轮量表开发与竞争模型比较 | 后续验证：多轮量表开发，并与 general collaborative overload 比较增量解释力 |

## 9. Reddit 编码应如何服务这个单一基础概念

Reddit 编码不应漫无边界地找所有 coding agent UX 主题，而应围绕一个问题：

> 用户是否在描述与 coding agent 协作时，协作要求如何过度消耗他们的注意力、时间和认知资源？

开放编码时优先关注这些表达：

- 用户说自己被 approval、permission、confirmation 打断；
- 用户说自己看不懂 agent 改了什么；
- 用户说自己需要花太多时间 review diff；
- 用户说自己必须一直盯着 agent；
- 用户说自己不断纠正 agent；
- 用户说自己宁愿不用 agent，因为协作过程太累；
- 用户说 agent 生成了工作，但自己要花很多精力收尾；
- 用户说 CLI 或界面让自己难以追踪协作状态。

这些材料要被解释为 collaborative overload 的情境化表现，而不是另起多个概念。

## 10. 后续量表开发思路

参照 Chen et al. 的做法，后续步骤应是：

1. 先整理 collaborative overload 的定义和已有测量；
2. 收集 Reddit 评论作为自然语言材料；
3. 对评论做 open coding，找出 coding-agent collaboration 中的 overload 表达；
4. 将 open codes 聚合为 coding-agent collaborative overload 的一阶维度；
5. 生成初始题项；
6. 做 Q-sort / card sorting 检验维度归属；
7. 做 EFA/CFA 或 PLS 二阶模型检验；
8. 与 general collaborative overload 比较，证明 coding-agent-specific 构念有增量解释力。

## 11. 当前最稳的理论表述

英文：

> We build on collaborative overload as the single foundational concept. Collaborative overload captures individuals' perceived depletion of attention, time, and cognitive resources caused by excessive collaboration demands. We argue that this concept is relevant but insufficient for coding-agent use because coding agents are agentic artifacts that autonomously perform code-related actions, request permissions, produce process feedback, modify code states, and leave developers with verification and takeover responsibilities. We therefore conceptualize coding-agent collaborative overload as a context-specific UX construct that captures the extent to which developers perceive excessive attention, time, and cognitive demands when collaborating with coding agents during concrete programming task episodes.

中文：

> 本研究以 collaborative overload 作为唯一基础概念。Collaborative overload 描述个体因过多协作要求而感知到注意力、时间和认知资源被消耗的状态。我们认为，这一概念适用于 coding agent 使用，但不能直接照搬，因为 coding agent 是能够自主执行代码相关行动、请求权限、反馈过程、改变代码状态，并让开发者承担验证和接管责任的 agentic artifact。因此，我们提出 coding-agent collaborative overload，用来描述开发者在具体编程任务中与 coding agent 协作时，因过度的理解、回应、验证、纠偏和接管要求而感知到注意力、时间和认知资源被过度消耗的程度。
