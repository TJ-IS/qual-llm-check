# IS Top11 数据库检索后的概念对话建议

> **已废弃 / superseded.** 这份文档是早期理论定位备忘录。当前有效方向见 `29_individual_level_foundational_concept_revision.md`：只从 individual/dyadic 层级的 collaborative overload / perceived collaborative effort 出发。

数据源：`E:\github\qual-llm-check-IS-utd\database\ALL_AIS_Basket_11.csv`

生成目的：根据 AIS Basket 11 数据库中的历史文献记录，判断 coding agent 用户体验研究最适合和哪些既有概念对话、哪些概念可以被改造，以及我们自己的构念应如何命名和界定。

## 1. 结论先行

我现在更建议把主构念从“编码代理委托协调负担”稍微转为：

**编码代理委托可协调性**

英文建议：

**Perceived Coordinability of Coding-Agent Delegation**

也可以更窄一些：

**Perceived Coordinability of Delegated Codebase Work**

我的判断是：我们最应该对话和改造的不是掌控感、信任、可读性、technostress 或普通 coordination cost，而是：

**IS delegation / agentic IS use 中的 coordination mechanism。**

也就是说，母概念不是“负担”，而是 **agentic IS delegation**。我们要开发的新构念，是把 Baird & Maruping (2021) 中较抽象的 delegation coordination mechanism 改造为 coding agent 任务情境下的个体 UX 构念。

更具体地说：

> 编码代理委托可协调性是指，开发者在将具体编程任务委托给 coding agent 后，感知到 agent 的自主工作能否被自己以可承受的方式持续对齐、追踪、分流、验证和接管的程度。

这个构念是连续程度构念，不是 0/1 构念。

高可协调性表示：用户能比较容易地维持任务边界、理解 agent 行动、查看代码库变化、处理审批交还、验证结果并在必要时接管。

低可协调性表示：用户虽然“名义上”可以让 agent 做事，也可能有停止按钮和审批按钮，但 agent 的行动过程、代码变更、风险节点和恢复路径难以被用户协调。

## 2. 数据库检索方法

我使用 `ALL_AIS_Basket_11.csv` 作为数据源。该文件包含 17,745 条 AIS Basket 11 文献记录，年份范围为 1977 到 2026，主要字段包括题名、年份、期刊、摘要、关键词、DOI 等。

我先按概念家族检索摘要和关键词，包括：

| 概念家族 | 命中文献数 |
| --- | ---: |
| IS delegation / agentic IS use | 1084 |
| coordination / collaboration / handoff | 1656 |
| control / autonomy / controllability | 879 |
| technostress / overload / fatigue | 297 |
| interruption / attention / notification | 1259 |
| verification / monitoring / oversight | 2284 |
| transparency / explainability / visibility | 1343 |
| trust / reliance / calibration | 583 |
| IS use / post-adoptive use / feature use | 285 |
| affordance / sociomaterial / technology features | 2058 |

然后我进一步看了精确短语命中。最关键的是：

| 短语 | 命中文献数 |
| --- | ---: |
| IS delegation | 3 |
| agentic IS | 2 |
| agentic artifact | 1 |
| algorithmic control | 8 |
| human-AI collaboration | 10 |
| technostress | 47 |
| interruption overload | 3 |
| perceived control | 20 |
| user control | 9 |
| transparency | 208 |
| affordance | 209 |
| adaptive use | 4 |
| post-adoptive | 13 |

这个结果说明：如果我们要写成“coding agent 特有的新 UX 构念”，不能只抓住一个很宽的热门词。数据库里最能为我们提供理论支点的是 IS delegation 这条线；其他概念更适合作为边界、前因、后果或竞争构念。

## 3. 为什么主线应是 IS delegation

### 3.1 核心母文献

**The next generation of research on IS use: A theoretical framework of delegation to and from agentic IS artifacts**  
Baird & Maruping, 2021, MIS Quarterly: Management Information Systems

数据库摘要显示，这篇文章认为传统 IS use 研究把 IS artifact 当作被动工具，默认人类 agency 占主导。但新一代 agentic IS artifacts 可以在不确定性下发起行动，并接受实现目标所需的权利和责任。因此，研究者需要从普通 IS use 转向 IS delegation。

这篇文章对我们最重要的地方是：它把人和 agentic IS artifact 的关系改写为 delegation，并提出 delegation 中有 appraisal、distribution、coordination 等机制。

coding agent 正好符合这个转向：

- 用户不是只点击功能，而是把一个编程目标交给 agent；
- agent 不只是建议，而是读取上下文、规划步骤、运行命令、修改代码；
- agent 的行动有不确定性；
- 用户仍承担最终解释、验证和接管责任；
- 用户和 agent 之间存在持续 coordination，而不是一次性使用。

### 3.2 为什么不能直接照搬 IS delegation

Baird & Maruping (2021) 给了母理论，但它还不能直接成为我们的量表构念。原因是：

1. 它是理论框架，不是个体用户体验构念。
2. 它把 coordination 作为 delegation 的机制之一，但没有把它操作化为用户在具体任务中感知到的程度。
3. 它没有处理 coding agent 中最关键的对象：可被 agent 直接修改的代码库。
4. 它没有解释 CLI 里看不清改动、审批疲劳、diff 验证、回滚接管等现实问题。
5. 它没有回答“同样是 delegation，为什么 coding agent 的 coordination 和普通推荐系统、聊天机器人、自动化工具不同”。

所以，我们不是要提出一个完全脱离旧理论的新概念，而是要做一个更像 Chen et al. (2024) 那类工作的概念开发：

> 用 IS delegation 作为理论母体，把其中抽象的 coordination mechanism 发展为 coding-agent-specific 的个体层面 UX 构念。

## 4. 推荐构念：编码代理委托可协调性

### 4.1 定义

**编码代理委托可协调性**是指：

> 开发者在将具体编程任务委托给 coding agent 后，感知到 agent 的自主工作能否被自己以可承受的方式持续对齐任务目标、追踪行动轨迹、分流审批与注意力交还、验证代码库变化，并在必要时接管或修复的程度。

### 4.2 为什么用“可协调性”而不是“协调负担”

“协调负担”当然能描述痛点，但它很容易被 reviewers 归入 technostress、work overload、cognitive load、verification burden 或 interruption overload。

“可协调性”更像一个 UX 构念。它测量的是用户如何评价这次 agentic coding delegation 是否可被自己协调。协调负担、审批疲劳、低掌控感、放弃使用、减少委托，都可以成为低可协调性的后果。

这样写有三个好处：

1. 构念本身有高低程度，不只是负面压力。
2. 它和 perceived control 区分更清楚：control 是结果感受，coordinability 是委托工作是否能被持续组织和管理。
3. 它能直接连接设计变量：行动日志、diff 可视化、风险分级审批、checkpoint、回滚、测试支持等都可以提高可协调性。

### 4.3 适用范围

这个构念只适用于 coding agent，而不适用于所有 AI 工具。

纳入：

- 能读取或修改项目代码的 agent；
- 能运行命令、测试、构建、搜索项目文件的 agent；
- 能进行多步计划和行动的编程代理；
- 能在任务过程中请求权限、确认或用户注意力的 agent。

不纳入：

- 普通代码补全；
- 只在聊天窗口给代码建议的 chatbot；
- 只做搜索、lint、格式化的传统开发工具；
- 只给一次性答案而不进入项目行动过程的 AI。

### 4.4 构念水平

高编码代理委托可协调性：

- 用户容易设定和维护任务边界；
- 用户能看懂 agent 做了什么以及为什么这么做；
- 用户能方便地查看代码库状态和 diff；
- 审批请求能被区分为例行、风险、关键决策；
- 用户知道何时继续委托、何时暂停、何时接管；
- 用户能恢复、回滚或修复 agent 的工作。

低编码代理委托可协调性：

- 用户必须反复解释任务边界；
- agent 做了很多操作但用户难以跟上；
- 用户看不清改动涉及哪些文件、行为和依赖；
- 权限请求频繁且难以判断重要性；
- 用户不知道该继续让 agent 做还是自己接管；
- 出错后恢复成本高，用户需要重新理解整个任务状态。

## 5. 建议的一阶维度

这里先作为理论敏感维度，不应在 Reddit 开放编码前写死。

### 5.1 委托范围可协调性

用户感知到自己能否清楚设定并维持 agent 的任务范围、目标、约束和不可触碰边界。

这来自 IS delegation 中的 rights and responsibilities 分配问题，但 coding agent 的特殊性是：范围不清会直接变成代码库副作用。

### 5.2 行动轨迹可协调性

用户感知到自己能否理解 agent 的步骤、命令、文件访问、中间决策和行动理由。

它和 transparency、visibility、legibility 有关系，但不等同于可读性。可读性只说信息是否容易看懂；行动轨迹可协调性还关心这些信息能否支持用户持续安排、纠偏和接管 agent 的工作。

### 5.3 审批交还可协调性

用户感知到自己能否有效处理 agent 在任务过程中交还给自己的权限请求、确认提示和继续/停止判断。

它吸收了 interruption overload 和 warning habituation 的启发，但不等同于审批疲劳。审批疲劳是后果；审批交还可协调性测量的是这些交还是否能被用户分流和判断。

### 5.4 代码库状态可协调性

用户感知到自己能否把 agent 的代码变更、diff、测试结果、日志、依赖影响和潜在副作用整合成对当前代码库状态的判断。

这是最 coding-agent-specific 的部分。普通聊天 AI、推荐系统和多数自动化系统不直接改变一个复杂、共享、可执行、带依赖结构的代码库。coding agent 的 delegation coordination 必须围绕 mutable codebase 展开。

### 5.5 接管恢复可协调性

用户感知到自己能否在 agent 偏离、失败或进入高风险状态时，及时暂停、接管、回滚、重新指示或修复。

这不是一般掌控感。用户可能有“停止”按钮，但如果不知道 agent 改了什么、为什么失败、如何恢复，那么接管恢复仍然不可协调。

## 6. 需要对话但不能等同的相邻概念

| 相邻概念 | 代表文献 | 它覆盖什么 | 为什么不能等同 |
| --- | --- | --- | --- |
| IS delegation | Baird & Maruping, 2021, MISQ | agentic IS artifact 接受权利与责任，委托包含 appraisal、distribution、coordination | 这是母理论，但 coordination 仍太抽象，没有任务级 UX 测量 |
| Delegation dynamics | Liu et al., 2025, MISQ | 人对 AI 的委托意愿在绩效反馈中动态变化 | 解释委托意愿变化，但不解释委托工作本身是否可协调 |
| Productive delegation / metaknowledge | Fügener et al., 2022, ISR | 人是否能正确评估自己和 AI 的能力，影响委托质量 | 重点是“该不该委托/委托给谁”，不是委托后的持续协调 |
| Direct/indirect IS use | Tong et al., 2017, ISR | 指定用户把 IS 使用部分委托给其他人，但仍承担责任 | 委托对象是人，不是自主修改代码库的 agentic artifact |
| Perceived control | DSS 2024 human-AI delegation paper; IS control 文献 | 用户是否觉得自己仍能影响或控制过程 | 它更适合作为后果。可协调性低会降低掌控感，但二者不重合 |
| Technostress | Ragu-Nathan et al., 2008, ISR; Ayyagari et al., 2011, MISQ | ICT 使用造成压力、过载、角色模糊等 | 太宽泛。可协调性低可能造成 technostress，但它不是 stress 本身 |
| Interruption overload | Chen & Karahanna, 2018, MISQ | 技术中断造成心理转换、过载和耗竭 | 只覆盖审批/通知打断，不能覆盖代码变更、任务边界、接管恢复 |
| Warning habituation | Vance et al., 2025, MISQ | 普通通知习惯化会泛化到安全警告 | 很适合解释 approval fatigue，但只是一个后果或子机制 |
| Adaptive system use | Sun, 2012, MISQ | 用户在后采纳阶段修正系统功能使用方式 | 适合作为后果，例如用户改用更低自主模式，但不是主构念 |
| Communication visibility / ambient awareness | Leonardi, 2014, ISR; Leonardi, 2015, MISQ | 可见沟通提升对他人知识和关系的感知 | 可支持行动轨迹可协调性，但其对象主要是人际沟通，不是 agent 修改代码库 |
| Technology-enabled coordination affordances | 2025 JMIS coordination affordance paper | 技术如何支持 coordination episodes | 可作为支撑理论，但不是 coding agent 个体 UX 构念 |
| Artifact-based coordination | Zaggl, 2025, MISQ | OSS 中开发者通过软件架构本身协调贡献 | 非常有启发，因为它把代码架构视为协调对象，但研究层次是 OSS 项目结构，不是用户和 agent 的任务委托 |

## 7. 关键代表文献及其作用

### 7.1 Baird & Maruping, 2021, MISQ

**The next generation of research on IS use: A theoretical framework of delegation to and from agentic IS artifacts**

这篇是主文献。它把传统 IS use 推向 IS delegation，指出 agentic IS artifact 不再是被动工具，而可以发起行动并接受目标达成中的权利与责任。

对我们的意义：coding agent 使用不是普通使用，而是 agentic coding delegation。

需要改造的地方：文章给出了 delegation 的理论机制，但没有把 coordination 转化为个体用户可感知、可测量、可解释实际 UX 痛点的构念。

### 7.2 Fügener et al., 2022, ISR

**Cognitive Challenges in Human-Artificial Intelligence Collaboration: Investigating the Path Toward Productive Delegation**

这篇研究 human-AI collaboration 中的 productive delegation。它发现，人和 AI 组合有潜力超过单独 AI，但只有当 AI 把任务委托给人时更有效；人委托给 AI 反而没有获得同样收益。关键原因不是算法厌恶，而是人缺乏 metaknowledge，无法准确判断自己和 AI 的能力边界。

对我们的意义：coding agent 的问题不应被简单写成 trust 或 algorithm aversion。用户愿意用 agent，也可能认可 agent，但仍可能因为不知道 agent 在当前代码库、当前任务、当前测试条件下是否适合继续做，而产生协调问题。

需要改造的地方：该文主要关注委托决策是否 productive，而我们关注委托发生后，agentic coding work 是否可持续协调。

### 7.3 Liu et al., 2025, MISQ

**Find the Good. Seek the Unity: A Hidden Markov Model of Human-AI Delegation Dynamics**

这篇研究人对 AI 的动态委托意愿。摘要显示，管理者会根据对 AI 绩效的持续评价形成 delegation feedback loop，从而增加或减少对 AI 的委托。

对我们的意义：我们可以把“编码代理委托可协调性”放进动态委托模型中。低可协调性会让用户减少委托、降级到聊天式使用，或只让 agent 做低风险任务。高可协调性则可能提升继续委托意愿。

需要改造的地方：这篇研究委托意愿的动态变化，不研究具体委托任务中用户如何协调 agent 的行动、代码变更和接管。

### 7.4 Navigating autonomy and control in human-AI delegation, 2024, DSS

这篇区分 user-invoked delegation 和 IS-invoked delegation，研究当 IS 主动提出接管任务时，用户如何受 self-threat 和 perceived control 影响。

对我们的意义：coding agent 可能从“用户指示一步”发展到“agent 主动建议下一步、请求权限、触发工具调用”。这说明 autonomy 与 control 是重要前因和后果。

需要改造的地方：它把 perceived control 放在 delegation 接受中研究，而我们的构念不是“我是否有控制感”，而是“agentic coding work 是否可被我协调”。control 可以作为结果变量。

### 7.5 Tong et al., 2017, ISR

**Direct and indirect information system use: A multimethod exploration of social power antecedents in healthcare**

这篇提出 indirect IS use：指定用户把部分 IS 使用委托给其他用户，但仍承担主要责任和问责。

对我们的意义：它能帮助我们回应“这不就是间接 IS 使用吗”的质疑。

关键区别：indirect IS use 的委托对象是其他人，责任和行动能力分布在人际关系中；coding agent delegation 的委托对象是 agentic artifact，它能直接操作工具、修改代码库、产生可提交成果。用户面对的不是“让别人帮我用系统”，而是“让一个自主 artifact 在代码库里行动，同时我还要维护最终责任”。

### 7.6 Ragu-Nathan et al., 2008 ISR; Ayyagari et al., 2011 MISQ

**The consequences of technostress for end users in organizations: Conceptual development and validation**  
**Technostress: Technological antecedents and implications**

这两篇是 technostress 线的重要文献。它们说明 ICT 会造成过载、角色模糊、压力和相关后果。

对我们的意义：这是最大的重合风险。如果我们把概念写成“用 coding agent 很累、压力大、要处理很多信息”，那确实会被 technostress 吸收。

改造方向：把 technostress 放在结果或竞争构念位置。编码代理委托可协调性不是压力，而是一次 agentic coding delegation 是否容易被用户协调。低可协调性可以造成 technostress、work overload 或 role ambiguity。

### 7.7 Chen & Karahanna, 2018 MISQ; Vance et al., 2025 MISQ

**Life interrupted: The effects of technology-mediated work interruptions on work and nonwork outcomes**  
**The Fog of Warnings: How Non-Security-Related Notifications Diminish the Efficacy of Security Warnings**

这两篇帮助解释用户提到的 approval fatigue。前者说明技术中断如何造成心理转换和耗竭，后者说明频繁普通通知会让用户对关键警告产生习惯化。

对我们的意义：coding agent 的权限请求和确认提示，如果不能区分风险等级，就会让用户形成机械批准或疲劳拒绝。

需要改造的地方：approval fatigue 不是主构念，而是低审批交还可协调性的后果之一。

### 7.8 Sun, 2012, MISQ

**Understanding user revisions when using information system features: Adaptive system use and triggers**

这篇提出 adaptive system use，关注用户在后采纳阶段如何修正自己使用系统功能的方式。

对我们的意义：用户可能因为 coding agent 不可协调，而改变使用策略。例如从 agent mode 退回 chat mode，只让 agent 改小文件，关掉自动执行命令，或只让它生成 patch 不直接应用。

需要改造的地方：adaptive use 是行为后果，不是我们要开发的 UX 构念本身。

### 7.9 Leonardi, 2014 ISR; Leonardi, 2015 MISQ

**Social media, knowledge sharing, and innovation: Toward a theory of communication visibility**  
**Ambient awareness and knowledge acquisition: Using social media to learn "who knows what" and "who knows whom"**

这两篇说明 visible communication 可以提升 metaknowledge 和 ambient awareness。

对我们的意义：coding agent 的行动日志、命令轨迹、diff 摘要、计划更新也有类似作用。它们让用户形成关于 agent 当前工作状态和能力边界的感知。

需要改造的地方：这些文献关注人际沟通可见性，而 coding agent 场景里，可见的不只是“沟通”，还有 agent 对代码库的行动和状态变化。

### 7.10 Zaggl, 2025, MISQ

**How Artifact-Based and Authority-Based Coordination Affect Propagation Costs in Open Source Software Development**

这篇非常值得纳入，因为它研究 OSS 中 artifact-based coordination，并把软件架构可见性和 propagation costs 连接起来。

对我们的意义：它给了“代码库/软件架构本身是协调对象”的理论入口。coding agent 特殊之处就在于：用户不是只和 agent 对话，而是要通过 agent 对代码库的修改来协调委托工作。

需要改造的地方：该文研究 OSS 项目层面的贡献协调，而我们研究个体开发者和 coding agent 在一次任务委托中的 UX 感知。

## 8. 理论贡献应如何写

我建议我们把理论贡献写成三层。

### 贡献 1：从 IS use 转向 coding-agent delegation

传统 IS use 视角不足以解释 coding agent，因为 coding agent 不是被动工具。它能自主读取、修改、测试和请求权限。因此，coding agent 使用应被视为一种 agentic coding delegation。

### 贡献 2：把 IS delegation 的 coordination mechanism 个体化、体验化、操作化

Baird & Maruping (2021) 已经提出 coordination 是 IS delegation 的重要机制，但没有说明用户在一次具体 agentic task episode 中如何感知这种 coordination。

我们的构念把 coordination mechanism 改造为：

> 用户对委托给 coding agent 的自主编程工作是否可被持续协调的感知。

### 贡献 3：提出 coding-agent-specific 的 mutable codebase coordination

coding agent 的独特性不只是“它是 AI”，而是它能在多步自主行动中改变代码库。代码库是共享、复杂、可执行、带依赖、可回滚但也可能产生隐性副作用的 artifact。

因此，coding agent delegation 的 coordination 不只是沟通协调，也不是普通人机协作，而是：

> 用户、agent 行动过程、审批交还和 mutable codebase state 之间的协调。

这是我们最可能做出新意的地方。

## 9. 现实价值

这个构念能解释几个真实痛点。

### 9.1 为什么很多人不爱用 CLI agent

用户不是单纯不信任 CLI agent，也不一定觉得它没用。一个核心问题是：CLI 中 agent 的行动和代码库变化经常不够可协调。

例如：

- diff 不够集中或不够可理解；
- 用户难以看到 agent 已经改了哪些地方；
- agent 的中间动作和最终修改之间关系不清楚；
- 出错后用户不知道该从哪里接管。

这些不是 perceived control 能完全解释的。用户可能知道自己能停止 agent，但仍然觉得这次委托工作不可协调。

### 9.2 为什么审批会疲劳

审批疲劳不只是“通知太多”。更准确地说，是 approval handoff 不可协调。

如果每个请求看起来都像同等重要，用户无法判断哪些是低风险例行请求，哪些是高风险代码库状态改变，最后就会机械点击或完全回避。

### 9.3 为什么 coding agent 能提高生产力但仍让人累

agent 可能真的写得快，也可能完成大量机械工作，但如果用户为了维持委托过程要持续追踪、解释、审查和接管，那么生产力收益会被协调成本抵消。

所以，可协调性可以解释 productivity paradox 式的体验：工具有能力，但用户未必愿意持续委托。

## 10. 可研究的前因和后果

### 10.1 前因

工具设计前因：

- agent 自主性水平；
- action trace visibility；
- diff 和代码库状态可视化；
- 风险分级审批设计；
- checkpoint、rollback、undo 支持；
- 任务边界表达机制；
- 测试、CI、lint、类型检查集成；
- agent 对计划、变更和失败的解释方式。

任务和代码库前因：

- 任务复杂度；
- 代码库耦合度；
- 变更文件数量；
- 测试覆盖率；
- 依赖和副作用风险；
- 任务是否跨模块、跨语言、跨服务。

用户前因：

- 用户对代码库熟悉度；
- 用户 AI 使用经验；
- 用户对自己和 agent 能力边界的 metaknowledge；
- 用户风险偏好；
- 用户最终问责压力。

### 10.2 后果

体验后果：

- perceived control；
- cognitive load；
- technostress；
- approval fatigue；
- verification fatigue；
- perceived usefulness；
- perceived productivity。

行为后果：

- continued use intention；
- delegation willingness；
- agent mode 使用频率；
- 从 agent mode 降级到 chat mode；
- takeover frequency；
- workaround use；
- adaptive system use；
- 对高自主 coding agent 的回避。

任务后果：

- 实际完成时间；
- rework；
- bug introduction；
- code review effort；
- task success；
- human-AI complementary performance。

## 11. 后续 Reddit 概念开发应准备什么

如果后续从 Reddit 收集 coding agent 评论，建议不要用量表维度直接套数据，而是把上面的构念作为 sensitizing concept。

开放编码时重点看用户是否在谈这些 episode：

1. 委托前：如何设定任务、范围、约束和权限；
2. agent 行动中：用户如何理解 agent 的计划、命令、文件访问和中间结果；
3. 审批交还中：用户如何处理继续、允许、拒绝、风险判断和注意力切换；
4. 代码变更后：用户如何看 diff、跑测试、审查副作用、合并或回滚；
5. 失败或偏离后：用户如何接管、修复、重新提示或放弃委托。

理论上需要准备：

- 明确母理论是 IS delegation；
- 明确我们开发的是 coordination mechanism 的个体 UX 化构念；
- 准备相邻概念边界表，尤其是 perceived control、trust、technostress、interruption overload、verification burden、adaptive use；
- 用 Reddit 数据确认哪些维度是真实反复出现的用户体验，而不是我们先验想象；
- 找出无法被现有 IS delegation coordination 充分解释的 coding-agent-specific 维度，尤其是代码库状态可协调性和接管恢复可协调性；
- 最后再进入题项池生成、专家评审、预测试、EFA/CFA、区分效度和 nomological validity。

## 12. 当前推荐的研究定位

如果只能选一个最值得继续推进的方向，我建议选：

**编码代理委托可协调性**

而不是：

- coding agent trust；
- coding agent control；
- coding agent readability；
- coding agent technostress；
- coding agent approval fatigue；
- coding agent verification burden。

原因是：

1. 它直接接在 IS delegation 这条高质量理论主线上。
2. 它能解释你提到的 CLI 看不清改动、approval fatigue、接管困难等现实痛点。
3. 它不会和掌控感完全重合，因为掌控感更像结果。
4. 它不会被 technostress 完全吸收，因为它不是压力，而是委托工作是否可协调。
5. 它能吸收可读性、可见性、审批设计、验证支持、回滚支持等多个设计前因。
6. 它最独特的部分是 mutable codebase coordination，这个是 coding agent 相比普通 AI/IS 更特殊的地方。

简短定位可以写成：

> Building on IS delegation theory, we develop perceived coordinability of coding-agent delegation as an individual-level UX construct that captures the extent to which users perceive delegated agentic coding work as alignable, traceable, triageable, verifiable, and recoverable within a mutable codebase.
