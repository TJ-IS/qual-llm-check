# 模仿 Chen 2024 的基础概念改造版：从 usability 到 coding-agent delegation usability

> **已废弃 / superseded.** 这份文件保留为一次误走方向的记录。用户已明确指出：我们不是要把主构念改成 usability，而是要在“协同/协调负担”这一问题线上，寻找最合适的基础概念作为改造起点。后续应以 coordination cost / coordination burden in managing interdependencies 这一概念族为起点，而不是 usability。
>
> 更新提示：本文件主要模仿 Chen et al. (2024 MISQ)。当时我进一步结合 Dong thesis 写成了 `25_superseded_usability_chen_dong_logic.md`。这条 usability 方向已经废弃，当前有效方向见 `29_individual_level_foundational_concept_revision.md`。

## 1. 先承认上一版的问题

上一版我把重点放在 **IS delegation / agentic IS use** 这条理论线上，但没有充分模仿 Chen et al. (2024 MISQ) 的概念开发写法。

Chen et al. 的逻辑不是“只有理论，没有基础概念”。它们的结构是：

| 位置 | Chen et al. 2024 的做法 | 对我们应有的启发 |
| --- | --- | --- |
| 基础概念 | usability | 我们也需要一个要被改造的基础概念 |
| 新情境 | voice interaction with smart products | coding agent delegation |
| 为什么旧概念不够 | 网站、移动应用、传统产品 usability 不能覆盖语音交互的内容、语音、拟人等特征 | 传统 usability/ease of use 不能覆盖 agent 自主行动、代码库变更、审批交还、接管恢复 |
| 理论框架 | cooperative principle theory, CPT | IS delegation + coordination theory |
| 经验材料 | 用户评论 open coding / axial coding | Reddit coding agent 用户评论 |
| 理论扩展 | 在 CPT 四原则外加入 anthropomorphism | 在传统 usability 中加入 agentic delegated work 的可协调、可治理、可恢复维度 |
| 验证方式 | 多轮量表开发，和 TAM/UTAUT/MUG 比较 | 多轮量表开发，和 TAM/UTAUT/MUG、trust/control/technostress 等比较 |

因此，我们现在应该把主线改成：

> 在 **usability** 这个基础概念上，发展 **coding-agent delegation usability**，并用 IS delegation / coordination 文献解释为什么这个新情境必须改造 usability 的维度。

## 2. 最适合被改造的基础概念：usability

### 2.1 为什么基础概念应该是 usability

如果模仿 Chen et al.，最自然的基础概念不是 trust、control、technostress，也不是 delegation 本身，而是：

**usability**

中文可以写作：

**可用性**

更具体到我们的情境：

**编码代理委托可用性**

英文建议：

**Coding-Agent Delegation Usability**

或更简洁：

**Agentic Coding Usability**

我更推荐前者，因为它同时保留了两个关键信息：

- coding agent 是研究对象；
- delegation 是区别于普通软件使用的情境特征。

### 2.2 数据库中支持 usability 作为基础概念的代表文献

Top11 数据库中，`usability / ease of use` 相关记录有 496 条。高相关代表包括：

| 文献 | 期刊年份 | 作用 |
| --- | --- | --- |
| Davis, **Perceived usefulness, perceived ease of use, and user acceptance of information technology** | MISQ, 1989 | 提供 perceived ease of use 这个最经典的接受模型基础概念 |
| Agarwal & Venkatesh, **Assessing a firm's Web presence: A heuristic evaluation procedure for the measurement of usability** | ISR, 2002 | 把 usability 情境化到网站，并发展 MUG 测量 |
| Hoehle & Venkatesh, **Mobile application usability: Conceptualization and instrument development** | MISQ, 2015 | 模仿价值很高：把 usability 情境化到移动应用并开发二阶量表 |
| Chen et al., **Conceptualization and Measurement of Voice-Interaction Usability** | MISQ, 2024 | 直接参考对象：把 usability 情境化到语音交互，并用 CPT 组织维度 |
| Wilson et al., **Behaviorally Measuring Usability by Analyzing Users’ Mouse Movement Efficiency** | MISQ, 2024 | 说明 usability 仍是 IS/HCI 重要基础概念，也可继续被重新测量 |

这些文献说明，IS 领域本来就允许并鼓励把 usability 迁移到新型交互对象中重新概念化。

所以我们不应说“没有基础概念”。更准确的说法是：

> 我们要改造的是 usability；我们要说明 coding agent delegation 让传统 usability 的维度不够用了。

## 3. 为什么传统 usability 不能直接用于 coding agent

传统 usability 通常关注：用户能否用系统有效、有效率、满意地完成目标。

这对 coding agent 当然适用，但太粗。coding agent 的情境改变了“用系统完成目标”的基本方式。

### 3.1 传统 usability 默认的是直接使用

传统网站、移动应用、桌面软件中，用户通常直接操作界面：

- 用户点击；
- 系统反馈；
- 用户根据反馈继续操作；
- 系统本身通常不自主决定下一步；
- 用户的行动和系统状态之间比较直接。

coding agent 中不是这样。

用户把目标委托给 agent 后，agent 可能：

- 自己读取文件；
- 自己规划步骤；
- 自己运行命令；
- 自己修改多个文件；
- 自己决定先修什么、后修什么；
- 中途请求权限或确认；
- 产生需要用户审查、测试、回滚或接管的代码库状态。

因此，coding agent 的 usability 不是“我能否容易地操作这个界面”，而是：

> 我能否通过委托 agent 的方式，有效且可承受地完成编程任务。

### 3.2 传统 usability 维度有些不够，有些不匹配

模仿 Chen et al. 对 voice usability 的写法，我们也可以说：

一些传统 usability 属性可以部分适用，例如：

- ease of use；
- feedback；
- learnability；
- consistency；
- efficiency；
- error recovery；
- user control。

但是，它们不能充分刻画 coding agent delegation，因为：

1. **ease of use 太泛**：它不能说明用户到底是在任务边界设定、行动追踪、审批分流、代码验证还是接管恢复上觉得困难。
2. **feedback 太窄**：coding agent 不只是给 feedback，而是在代码库中产生行动轨迹和状态变化。
3. **user control 不够**：用户有停止按钮不代表能理解、纠偏、恢复 agent 的工作。
4. **error recovery 要被重写**：传统软件中的 error recovery 可能是撤销一步；coding agent 中的 recovery 可能涉及跨文件 diff、git 回滚、测试失败定位和重新提示。
5. **efficiency 可能有悖论**：agent 写代码很快，但用户如果花大量时间审查、协调和修复，总体使用未必有效率。
6. **satisfaction 是后果**：用户满意或不满意，不能替代对这种 agentic task episode 的具体可用性结构。

这正是我们开发新构念的空间。

## 4. 推荐主构念：Coding-Agent Delegation Usability

### 4.1 中文名

**编码代理委托可用性**

### 4.2 英文名

**Coding-Agent Delegation Usability**

缩写可用：

**CADU**

### 4.3 定义

**编码代理委托可用性**是指：

> 开发者感知到自己能够通过将具体编程任务委托给 coding agent，以有效、有效率且可承受的方式达成编程目标的程度；这种可用性取决于用户能否清楚表达委托意图、理解 agent 的自主行动、治理权限与注意力交还、检视和验证代码库变更，并在必要时接管或恢复任务。

这个定义保留了传统 usability 的核心：

- goal achievement；
- effectiveness；
- efficiency；
- user experience。

但它把传统 usability 改造成了适合 coding agent 的版本：

- 不是直接操作，而是委托；
- 不是界面使用，而是 agentic work episode；
- 不是只看输出，而是看行动过程和代码库状态；
- 不是只看错误提示，而是看接管和恢复；
- 不是只看系统是否容易用，而是看委托是否可协调、可治理、可验证、可恢复。

### 4.4 构念程度

高 CADU：

- 用户容易把任务目标、边界和约束交给 agent；
- agent 的计划、命令、文件修改和中间状态容易理解；
- 权限请求和注意力交还不造成混乱；
- 代码变更容易检视、验证和整合；
- 出错后用户知道如何暂停、回滚、重新提示或接管。

低 CADU：

- 用户很难让 agent 明白任务边界；
- agent 做了很多事，但用户不知道它做了什么；
- CLI 或工具界面让 diff、日志、命令、测试结果分散难追；
- 审批请求频繁且风险等级不清；
- 用户必须花大量时间检查、修复或重建任务状态；
- 用户最后觉得还不如自己写。

## 5. 理论框架：IS delegation 用来改造 usability

### 5.1 为什么 IS delegation 是理论框架，而不是基础概念本身

Baird & Maruping (2021 MISQ) 的 **IS delegation / agentic IS artifacts** 是我们的理论框架，不是我们唯一的基础概念。

它的作用相当于 Chen et al. 中的 CPT：

| Chen et al. 2024 | 我们 |
| --- | --- |
| 基础概念：usability | 基础概念：usability |
| 理论框架：CPT | 理论框架：IS delegation / coordination |
| 新构念：voice-interaction usability | 新构念：coding-agent delegation usability |
| CPT 四原则解释语音交互维度 | IS delegation 解释 agentic coding usability 维度 |
| 新增 anthropomorphism 扩展 CPT | 新增 mutable-codebase coordination / recoverability 扩展传统 usability |

### 5.2 IS delegation 为什么适用

Baird & Maruping (2021) 认为，agentic IS artifacts 不再只是被动工具，而可以在不确定性下发起行动并承担目标达成中的权利与责任。

coding agent 正是这种对象：

- 用户把编程任务交给 agent；
- agent 具备多步行动能力；
- agent 能访问工具和代码库；
- agent 能修改真实项目状态；
- 用户仍保留最终责任和验收权。

所以，coding agent use 不是普通 direct IS use，而是 **agentic IS delegation**。

### 5.3 IS delegation 为什么还不够

IS delegation 理论告诉我们：

- 为什么 agentic IS 改变了 IS use；
- 为什么 rights and responsibilities 需要重新分配；
- 为什么 delegation 包含 appraisal、distribution、coordination。

但它还没有告诉我们：

- coding agent 的 usability 应该有哪些维度；
- 用户如何评价一次委托任务是否“好用”；
- 代码库变更如何影响 agentic delegation 的 UX；
- 审批交还和接管恢复如何进入 usability；
- 为什么 CLI agent 可能有能力但仍然不好用。

因此，我们不是直接测 IS delegation，而是用它来改造 usability。

## 6. 相关基础概念：哪些要吸收，哪些要区分

### 6.1 基础概念关系总表

| 概念 | 代表文献 | 和 CADU 的关系 | 为什么不能直接照搬 |
| --- | --- | --- | --- |
| Usability | Agarwal & Venkatesh 2002 ISR; Hoehle & Venkatesh 2015 MISQ; Chen et al. 2024 MISQ | 最核心基础概念 | 传统维度多基于直接操作、网站、移动应用或语音交互，不能覆盖 agentic code delegation |
| Perceived ease of use | Davis 1989 MISQ; Venkatesh 2000 ISR | 竞争构念/上位感知 | 太泛，只知道“容易/不容易”，不知道 coding agent 委托到底哪里难 |
| User satisfaction | Doll & Torkzadeh 1988 MISQ; CRM satisfaction 文献 | 后果变量 | 满意是结果，不是具体可用性结构 |
| IS delegation | Baird & Maruping 2021 MISQ | 理论框架 | 它解释 agentic IS use，但不是 usability 量表 |
| Human-AI productive delegation | Fügener et al. 2022 ISR | 解释委托质量和 metaknowledge | 重点是该不该委托/委托给谁，不是 agent 工作过程是否可用 |
| Delegation dynamics | Liu et al. 2025 MISQ | 后果/动态模型 | 研究委托意愿如何变化，不测 coding agent 任务 episode 的 usability |
| Indirect IS use | Tong et al. 2017 ISR | 边界概念 | 委托给人，不是委托给能自主改代码的 artifact |
| Coordination | JMIS 2002 软件项目协调; JMIS 2025 coordination affordances | 维度生成理论 | 传统 coordination 多是团队/组织层面，不是个体用户感知的 usability |
| Artifact-based coordination | Zaggl 2025 MISQ | 解释代码库为何是协调对象 | 研究 OSS 项目层面的贡献协调，不是个体 user-agent task episode |
| Communication visibility / ambient awareness | Leonardi 2014 ISR; Leonardi 2015 MISQ | 行动轨迹/状态可见性的理论来源 | 主要研究人际沟通可见性，不覆盖 agent 对代码库的自主操作 |
| Perceived control / user control | human-AI delegation DSS 2024; IS control 文献 | 后果或子属性 | 控制感是结果；有控制按钮不代表委托工作可用 |
| Monitoring / supervisory control | monitoring 与自动化相关文献 | 监督维度来源 | coding agent 不是只被监控，它会和用户交替推进、请求权限、改变代码库 |
| Technostress / overload | Ragu-Nathan et al. 2008 ISR; Ayyagari et al. 2011 MISQ | 负面后果/竞争模型 | technostress 解释压力，不解释具体 agentic usability 结构 |
| Interruption / warning habituation | Chen & Karahanna 2018 MISQ; Vance et al. 2025 MISQ | 审批疲劳机制 | 只覆盖权限提示和注意力中断，不覆盖整体委托可用性 |

### 6.2 这里最关键的转变

上一版我把“可协调性”当作主构念。现在看，更模仿 Chen et al. 的写法应该是：

> **可协调性不是最终主构念，而是 coding-agent delegation usability 的核心机制。**

也就是说：

- 主构念：编码代理委托可用性；
- 基础概念：usability；
- 理论框架：IS delegation / coordination；
- 核心机制：用户能否协调 agentic coding work；
- 独特扩展：mutable codebase 下的验证、接管和恢复。

## 7. 初步维度：从基础概念到 coding-agent-specific 维度

这里不应写成最终结论，而应写成 Reddit 编码前的 sensitizing framework。

### 7.1 委托意图可表达性

英文可写为：

**Delegation articulability**

定义：

> 用户感知到自己能够清楚表达任务目标、边界、约束、验收标准和不可触碰代码范围的程度。

基础概念来源：

- usability 中的 ease of use；
- IS delegation 中的 rights and responsibilities distribution；
- 软件项目协调中的 task interdependence / goal conflict。

为什么需要改造：

传统 usability 里“输入是否容易”主要是界面输入问题；coding agent 中，输入不是表单或命令，而是委托任务。用户必须把意图、边界、上下文和风险约束转化为 agent 可执行的任务。

### 7.2 代理行动可追踪性

英文可写为：

**Agent action traceability**

定义：

> 用户感知到自己能够理解 agent 在任务过程中做了哪些操作、为什么这样做、这些操作如何推进任务的程度。

基础概念来源：

- communication visibility；
- transparency / observability；
- workspace awareness；
- usability 中的 feedback 和 visibility。

为什么需要改造：

传统 visibility 通常指界面状态或他人沟通可见。coding agent 中，用户需要追踪的是 agent 的多步行动轨迹，包括命令、文件访问、代码编辑、测试运行和中间决策。

### 7.3 权限交还可治理性

英文可写为：

**Handoff governability**

定义：

> 用户感知到自己能够有效处理 agent 在任务过程中发起的权限请求、确认提示、继续/停止选择和风险分级判断的程度。

基础概念来源：

- user control；
- interruption overload；
- warning habituation；
- human-AI delegation 中的 autonomy/control。

为什么需要改造：

传统 usability 可能只关心用户是否有控制选项；coding agent 中，问题不是有没有按钮，而是 agent 何时把注意力交还给用户、交还的信息是否足以判断风险、用户是否能分流例行审批和关键审批。

### 7.4 代码库状态可检视性

英文可写为：

**Codebase-state inspectability**

定义：

> 用户感知到自己能够检查、理解和评估 agent 对代码库造成的变更及其潜在影响的程度。

基础概念来源：

- artifact-based coordination；
- software project coordination；
- usability 中的 feedback / error prevention；
- verification / monitoring 文献。

为什么需要改造：

这是最 coding-agent-specific 的维度。传统聊天 AI 的输出是文本，传统网站的输出是页面反馈；coding agent 的输出是对 mutable codebase 的状态改变。用户必须理解 diff、依赖、测试、日志和副作用。

### 7.5 接管恢复可操作性

英文可写为：

**Takeover recoverability**

定义：

> 用户感知到自己能够在 agent 偏离、失败或产生风险时暂停、接管、回滚、重新提示或修复任务的程度。

基础概念来源：

- usability 中的 recoverability / error recovery；
- autonomous system takeover；
- service recovery / system recovery；
- IS delegation 中的 residual responsibility。

为什么需要改造：

传统 error recovery 多是用户从系统错误中恢复；coding agent 中，恢复对象是 agent 已经改变过的代码库和任务进程。接管不是简单撤销一步，而是重建“agent 做到哪里、哪里错了、如何继续”的任务状态。

## 8. CADU 与“可协调性”的关系

可以这样处理：

### 方案 A：CADU 是主构念，可协调性是核心解释机制

这是我现在推荐的方案。

写法：

> Coding-agent delegation usability captures the extent to which developers perceive delegated agentic coding work as usable. Its distinctive mechanism is coordinability: the user must coordinate agentic action, permission handoffs, codebase state changes, and takeover/recovery within a mutable software artifact.

优点：

- 明确基础概念是 usability；
- 和 Chen et al. 结构最像；
- 易于和 TAM/UTAUT/MUG 比较；
- 不会被问“可协调性是不是凭空造的”。

### 方案 B：Perceived coordinability 是主构念，usability 是理论背景

这个方案也可行，但更难防守。

风险：

- coordinability 在 IS/HCI 中不是像 usability 那样成熟的基础概念；
- 容易被质疑只是 coordination cost、perceived control、transparency 的拼接；
- 不如 CADU 容易模仿 Chen et al. 的 scale development 论文结构。

因此我建议主论文路线采用方案 A。

## 9. 和 Chen et al. 结构一一对应的写法

### 9.1 Chen 的句式

Chen et al. 的论证大致是：

> Usability is important and context dependent. Existing usability scales for websites, mobile apps, and products cannot fully capture voice-interaction usability because voice interaction has unique input/output modality and anthropomorphic features. Therefore, we develop a context-specific voice-interaction usability construct and scale, using CPT as theoretical lens and user reviews as empirical material.

### 9.2 我们可以对应写成

> Usability is central to users' effective and satisfactory use of information systems and is inherently context dependent. However, existing usability conceptualizations and scales primarily assume direct manipulation of passive IS artifacts. They are not well suited for coding agents, where users delegate programming tasks to agentic IS artifacts that autonomously plan actions, invoke tools, modify a mutable codebase, request permissions, and return control to users for verification and recovery. Drawing on IS delegation theory and coordination research, we conceptualize coding-agent delegation usability as a context-specific usability construct and develop its dimensions using user discussions of coding-agent experiences.

这就比上一版更像 Chen 2024：有基础概念，有情境差异，有理论框架，有新构念。

## 10. 研究问题也应改写

模仿 Chen et al. 的 RQ，可以写成：

**RQ1: What are the dimensions of coding-agent delegation usability, and how can they be measured?**

**RQ2: How well does coding-agent delegation usability predict users' delegation-related outcomes compared with existing models of technology use, usability, trust, control, and technostress?**

这比“coding agent 是否有独特 UX 概念”更像一篇概念开发和量表开发论文。

## 11. 量表和 competing models 应该怎么设计

### 11.1 主模型

CADU 的一阶维度暂定：

1. delegation articulability；
2. agent action traceability；
3. handoff governability；
4. codebase-state inspectability；
5. takeover recoverability。

CADU 可以作为二阶形成式构念，因为五个维度共同形成整体可用性，且不一定高度相关。

### 11.2 结果变量

模仿 Chen et al. 用 intention to use 和 use behavior，我们可以用：

- continued use intention；
- delegation willingness；
- agent mode use frequency；
- willingness to use higher-autonomy mode；
- perceived productivity；
- perceived control；
- task satisfaction；
- reduced takeover avoidance。

### 11.3 Competing models

需要比较：

| 模型 | 变量 |
| --- | --- |
| TAM-based model | perceived usefulness, perceived ease of use |
| UTAUT-based model | performance expectancy, effort expectancy, facilitating conditions, social influence |
| Generic usability model | effectiveness, efficiency, satisfaction, learnability, error recovery |
| Trust/control model | trust in AI, perceived control, perceived autonomy |
| Technostress model | overload, complexity, invasion/intrusion, strain |
| Verification burden model | review effort, test effort, output uncertainty |
| Interruption/approval fatigue model | interruption overload, warning habituation, approval fatigue |

我们的目标不是说这些模型错，而是证明：

> CADU 对 coding-agent delegation outcomes 的解释力更强，并且其 coding-agent-specific 维度提供增量解释力。

## 12. Reddit 编码时要如何服务“基础概念改造”

Reddit 数据不是随便归纳主题，而是要回答：

> 用户在真实 coding agent 使用中提到的体验，哪些是传统 usability 已能解释的，哪些需要把 usability 改造成 coding-agent delegation usability？

编码时可以先保留三类标签。

### 12.1 传统 usability 可解释的代码

例如：

- easy to use；
- fast；
- accurate；
- useful；
- confusing interface；
- poor feedback；
- hard to learn。

这些说明 CADU 不能脱离 usability。

### 12.2 传统 usability 可部分解释但需要改造的代码

例如：

- “I cannot see what files it changed”；
- “I have to babysit it”；
- “It keeps asking me to approve commands”；
- “It made changes across the repo and I lost track”；
- “I spend more time reviewing than coding”。

这些是最重要的材料，因为它们说明旧 usability 语言不够精确。

### 12.3 可能形成新维度的代码

例如：

- long-horizon agent task drift；
- context feeding and memory maintenance；
- permission triage fatigue；
- codebase pollution；
- rollback confidence；
- test-mediated reassurance；
- multi-agent conflict；
- CLI/IDE visibility mismatch。

这些可能成为类似 Chen et al. 中 anthropomorphism 的 context-specific extension。

## 13. 当前推荐定位

我现在建议把项目定位从：

**开发一个 coding-agent-specific 的协调负担概念**

改成：

**基于 usability 这个基础概念，开发 coding-agent delegation usability，并用 IS delegation / coordination 理论解释其维度结构。**

最短表述：

> 本研究改造 usability 这一基础概念，将其从直接操作被动软件工具的可用性，扩展到用户委托 agentic IS artifact 执行编程任务时的可用性。我们认为，coding-agent delegation usability 的独特性在于，用户不仅要完成目标，还必须在 mutable codebase 中协调 agent 的自主行动、权限交还、代码变更检视和接管恢复。

这样，它和 Chen 2024 的对应关系非常清楚：

| Chen et al. 2024 | 我们 |
| --- | --- |
| Voice-interaction usability | Coding-agent delegation usability |
| Usability 是基础概念 | Usability 是基础概念 |
| Voice interaction 是新情境 | Agentic coding delegation 是新情境 |
| CPT 是理论组织框架 | IS delegation / coordination 是理论组织框架 |
| 用户评论生成一阶维度 | Reddit 评论生成一阶维度 |
| Anthropomorphism 是新增维度 | Mutable-codebase coordination / takeover recoverability 可能是新增维度 |
| 和 TAM/UTAUT/MUG 比较 | 和 TAM/UTAUT/MUG/trust/control/technostress 比较 |

## 14. 下一步应补的文档

为了真正模仿 docs_ref_MISQ，我建议下一步补两个文件：

1. **`CADU_foundational_concept_gap_table.md`**
   - 仿 Chen 2024 Table 1 和 Table 2；
   - 列出传统 usability、website usability、mobile usability、voice usability、ease of use、control、feedback、recoverability 等旧维度；
   - 逐项说明为什么它们不能直接测 coding-agent delegation usability。

2. **`CADU_reddit_coding_protocol.md`**
   - 不再只按“协调负担”编码；
   - 改成先识别 usability-related experiences，再判断哪些需要 agentic delegation 改造；
   - 保留 IS delegation/coordination 作为 theory-mapping 阶段的框架。
