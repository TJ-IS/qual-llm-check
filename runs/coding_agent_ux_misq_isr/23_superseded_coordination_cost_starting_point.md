# 协调负担方向的基础概念重启：从 coordination cost 到 coding-agent-specific coordination burden

## 0. 纠偏结论

这次应该明确纠正：我们不是要用 **usability** 作为主构念，也不是把“可用性”换一个 coding agent 场景名称。

我们真正要找的是：和“协同/协调负担”有关的已有基础概念，作为后续概念开发的改造起点。

我现在的判断是：

> 最合适的广义基础概念是 **coordination cost / coordination effort in managing interdependencies**，即为了管理任务、行动、角色、工件之间的相互依赖而产生的协调成本或协调努力。

但它不能被直接照搬。它需要通过三个文献支架被改造成 coding-agent-specific 的个体 UX 构念：

1. **software project coordination**：说明软件设计/编码任务中的 task interdependence、goal conflict、coordination strategy 会影响 productivity 和 process satisfaction；
2. **artifact-based coordination / propagation costs**：说明软件代码/架构本身是协调媒介，架构可见性和相互依赖会影响开发者需要付出的 effort；
3. **IS delegation / agentic IS artifacts**：说明 coding agent 不是普通工具，而是可被委托、可自主行动、可承担部分任务责任的 agentic artifact，因此用户面对的不是简单 interaction，而是 delegation 后的 coordination。

所以，我们不是从 usability 改造，而是从 **coordination cost** 改造；不是泛泛说“用户觉得费劲”，而是研究开发者在委托 coding agent 后，为了管理 agent 行动、任务目标、代码库状态、审批交还、验证和接管之间的相互依赖而承受的协调成本。

## 1. 最合适的改造起点是什么

### 推荐起点

**Coordination cost in managing interdependencies**

可以暂时翻译为：

**管理相互依赖的协调成本**

它适合作为基础概念，是因为它正好抓住了“协同负担”的理论核心：

- coding agent 的问题不是单纯“界面难用”；
- 也不是单纯“用户不信任 AI”；
- 也不是单纯“用户没有掌控感”；
- 而是用户把任务委托给 agent 后，必须持续管理多个相互依赖对象：任务意图、agent 行动、代码库结构、权限审批、测试结果、最终责任和接管时机。

这和 coordination cost 文献的核心相通：当任务和行动之间存在相互依赖时，行动者需要付出额外努力来协调它们。

### 但不能直接照搬

传统 coordination cost 多数研究的是组织、团队、平台、外包、供应链或软件项目层面的成本。它经常是结构性、经济性或绩效层面的概念。

coding agent 情境要求改造，因为这里的 coordination cost 变成了：

1. **个体任务经历中的主观感知成本**，不是组织层面的客观成本；
2. **人和 agentic artifact 的委托后协调**，不是普通人际团队协调；
3. **围绕可执行代码工件发生**，不是一般信息交换；
4. **伴随自主行动和权限交还**，不是静态工具使用；
5. **用户保留最终责任**，即便 agent 已经完成了部分行动。

因此，基础概念可以是 coordination cost，但新构念不能只是 “coordination cost in coding agent use”。它必须说明 coding agent 如何改变了 coordination cost 的结构。

## 2. Top11 文献中最关键的基础记录

下面这些记录来自 `database/ALL_AIS_Basket_11.csv`，我已用脚本抽取到：

- `runs/coding_agent_ux_misq_isr/21_superseded_broad_coordination_foundation_records.csv`
- `runs/coding_agent_ux_misq_isr/22_superseded_broad_coordination_foundation_records.md`

### 2.1 最核心：coordination cost / effort

| 文献 | 已有概念 | 摘要中的核心内容 | 对我们的作用 | 不能直接照搬的原因 |
| --- | --- | --- | --- | --- |
| **Platform desertion by app developers** (2015, JMIS) | coordination costs borne by app developers | app developer 承担的 coordination costs 会影响 platform desertion；这些成本受 app decision rights 和 app microarchitecture 的共同影响 | 很重要。它已经把 coordination costs 放到开发者、平台、软件架构/接口关系中讨论，比一般组织协调更接近 coding agent | 研究对象是 app 与平台治理，不是用户委托 agent 完成具体编程任务；成本来源是平台决策权和微架构，不是 agent 自主行动、审批交还、验证和接管 |
| **Information technology and industrial cooperation: The changing economics of coordination and ownership** (1992, JMIS) | coordination economics / coordination cost | IT 可以降低协调成本，也可能改变合作关系和所有权边界 | 提供经典基础：IT 的价值常常在于改变协调成本 | 层级太宏观，适合做理论背景，不适合直接定义 coding agent 用户体验 |
| **Do large firms become smaller by using information technology?** (2013, ISR) | coordination costs | firm size 增加带来 coordination activities，IT 用来处理这些协调活动并降低 coordination costs | 支持“IT 与协调成本”在 IS 文献中是成熟基础概念 | 组织规模层面，不涉及软件开发任务，也不涉及 agentic delegation |

这一组说明：**coordination cost 是最合适的基础概念族**。但它太宽，必须被软件开发和 agentic delegation 文献进一步限定。

### 2.2 软件开发任务中的协调：software project coordination

| 文献 | 已有概念 | 摘要中的核心内容 | 对我们的作用 | 不能直接照搬的原因 |
| --- | --- | --- | --- | --- |
| **A contingency approach to software project coordination** (2002, JMIS) | software project coordination; task interdependence; goal conflict; coordination strategy | task interdependence、goal conflict、coordination strategies 会影响 software design and coding activities 的 productivity 和 process satisfaction | 很关键。它把 coordination 放在软件设计和编码任务里，说明软件开发中的相互依赖本来就会产生协调问题 | 研究的是项目成员/团队任务，不是单个用户与 coding agent 的 task episode；它讨论 coordination strategy，不直接测量用户感知负担 |
| **A configural approach to coordinating expertise in software development teams** (2017, MISQ) | expertise coordination | 软件团队中设计协作和技术协作需要不同配置，coordination success 影响 team conflict 和 performance | 支持软件开发不是单纯个人编码，常涉及知识、设计和技术协同 | 它是人类团队 expertise coordination，不是人-agent 协调；更适合作为相邻支撑，而不是主基础概念 |
| **Role of collective ownership and coding standards in coordinating expertise in software project teams** (2009, EJIS) | expertise coordination; collective ownership; coding standards | collective ownership 和 coding standards 会影响 expertise coordination 与 technical quality | 对 coding agent 有启发：代码规范、共同所有权、项目标准可能降低 agent 输出整合负担 | 仍是团队实践，不是 agentic delegated action |

这一组说明：coding agent 的协调负担不是凭空出现的。软件开发本身就是高度 interdependent 的任务；coding agent 只是把这种 interdependence 从“人类团队/项目”转化为“用户-agent-代码库”的任务级协调。

### 2.3 最像 coding agent 的桥：artifact-based coordination / propagation costs

| 文献 | 已有概念 | 摘要中的核心内容 | 对我们的作用 | 不能直接照搬的原因 |
| --- | --- | --- | --- | --- |
| **How Artifact-Based and Authority-Based Coordination Affect Propagation Costs in Open Source Software Development** (2025, MISQ) | artifact-based coordination; authority-based coordination; propagation costs; architecture visibility | OSS 项目的成功取决于低 propagation costs；coordination 的形式会影响 interdependent contributions 如何被管理；artifact-based coordination 指开发者通过 work artifact/architecture 本身协调；architecture visibility 是重要条件 | 这是最强桥梁。coding agent 也通过修改代码工件参与协作；用户痛点“看不清改了什么”“担心副作用”可以接到 architecture visibility 和 propagation costs | 该文是项目/架构层面的模拟模型，不是个体 UX；artifact-based coordination 在文中主要是开发者通过工件间接协调，而 coding agent 还包含对话、审批、工具调用、测试、权限交还和接管 |
| **Coordinating interdependencies in online communities: A study of an open source software project** (2016, ISR) | unresolved interdependencies; arm's-length coordination mechanisms | 在线社区通过平台和实践机制管理 work interdependencies，但仍有 unresolved interdependencies | 支持“工具机制不能消除所有相互依赖”，coding agent 也会留下 unresolved dependencies，需要用户继续协调 | 研究对象是开源社区群体，不是单个开发者与 agent |
| **Organizing for Software Product Development** (2026, ISR) | product complexity; cross-team coordination; mirroring | 软件产品复杂度、团队结构和跨团队协调共同影响开发表现 | 支持代码/产品复杂度会改变 coordination burden 的边界条件 | 层级是组织/团队结构，不是个体使用经历 |

这一组最能帮助我们解释 coding agent 的“agentic”到底体现在哪里：agent 的行动不是停留在建议层面，而是进入共享代码工件并产生可能传播的变更。用户的负担不是阅读普通输出，而是协调一个会改变项目状态的行动者。

### 2.4 技术如何支持协调：technology-enabled coordination affordances

| 文献 | 已有概念 | 摘要中的核心内容 | 对我们的作用 | 不能直接照搬的原因 |
| --- | --- | --- | --- | --- |
| **Understanding the Role of Technology in Coordination Through Affordance Configurations** (2025, JMIS) | technology-enabled coordination affordances; coordination episodes; coordination breakdowns | 技术中介下的 work coordination 经常 breakdown；文章识别了七种 technology-enabled coordination affordances，并用 coordination episode 和 dependency 类型解释成功协调 | 对我们非常有用。它可以帮助我们把 coding agent 的 UI/工作流特征写成前因：行动可见性、状态同步、审批设计、变更组织方式等 | 它研究的是技术如何促成 coordination success，不是用户感知到的 coordination burden；affordance 更适合作为前因或设计机制，而不是主构念 |
| **Social media, knowledge sharing, and innovation: Toward a theory of communication visibility** (2014, ISR) | communication visibility; message transparency; network translucence; metaknowledge | 可见的沟通信息帮助人形成 metaknowledge | 可作为“行动轨迹可见性/过程可见性”的理论支撑 | 它关注组织知识共享，不是代码工件和 agent 行动 |
| **Ambient awareness and knowledge acquisition** (2015, MISQ) | ambient awareness; metaknowledge | 暴露于数字活动流能帮助用户获得 metaknowledge | 可支持“更好的状态流/行动流可降低协调负担” | 它研究社交媒体信息流，不是 agentic code modification |

这一组提醒我们：不要把主构念写成“可见性”或“可读性”。可见性、可追踪性、状态同步、审批设计更可能是协调负担的前因；它们解释为什么某些工具让用户协调起来更轻松。

### 2.5 为什么这是 coding agent 问题：IS delegation / agentic IS

| 文献 | 已有概念 | 摘要中的核心内容 | 对我们的作用 | 不能直接照搬的原因 |
| --- | --- | --- | --- | --- |
| **The Next Generation of Research on IS Use: A Theoretical Framework of Delegation to and from Agentic IS Artifacts** (2021, MISQ) | IS delegation; agentic IS artifacts; appraisal; distribution; coordination | 传统 IS use 假设 IS artifact 是被动工具；agentic IS artifacts 可以主动行动、接受权利和责任，因此需要用 delegation 理解人-系统关系 | 这是 coding agent 的理论入口。它说明 coding agent 使用不是普通 use，而是 delegation；coordination 是 delegation 的关键机制之一 | 它提供的是抽象框架，不是具体 UX 构念；它没有告诉我们 coding agent 中 coordination burden 如何定义、分维度和测量 |
| **Toward Triadic Delegation** (2025, JAIS) | triadic delegation; agentic IS artifacts | agentic IS artifacts 改变人际关系，使 dyad 变 triad | 支持 agentic artifact 会重构角色和责任关系 | 医疗情境，与 coding agent 的代码工件和任务执行差异大 |
| **Navigating autonomy and control in human-AI delegation** (2024, DSS) | human-AI delegation; user-invoked vs IS-invoked delegation | 用户面对 AI 主动提出承担任务时，会有不同接受反应 | 有助于解释 autonomy/control 与 delegation 的关系 | 重点是 delegation acceptance，不是委托后的持续协调成本 |

这一组不是“基础成本概念”，而是解释为什么这个成本在 coding agent 中变成一个新问题：因为 agentic artifacts 改变了用户和工具的关系。

## 3. 为什么 coordination cost 需要被改造

如果我们只说：

> coding agent 使用中有 coordination cost。

这不够新，也不够精确。因为 coordination cost 本来就是老概念。

真正需要开发新构念的理由在于：coding agent 让 coordination cost 出现了旧概念难以覆盖的对象结构。

### 3.1 旧概念中的协调对象主要是人、团队或组织

软件项目协调文献关心的是团队成员如何协调任务、知识、目标和流程。平台文献关心开发者如何协调 app 与平台架构。组织文献关心 IT 如何降低企业内外协调成本。

coding agent 中的协调对象变成：

- 用户的任务意图；
- agent 的自主计划和行动；
- 代码库当前状态；
- diff、测试、命令、日志等过程证据；
- 权限审批和注意力交还；
- 用户最终责任和接管时机。

这不是传统团队协调的简单缩小版。

### 3.2 旧概念常把技术当成降低协调成本的工具

很多 IS 文献把 IT 看成降低 coordination costs 的工具，例如通过信息共享、过程集成、平台机制、标准化接口、可见性等降低协调难度。

coding agent 不同：它既可能降低协调成本，也可能制造新的协调成本。

例如：

- agent 自动修改代码，减少用户亲自编码成本；
- 但用户必须检查它改了哪些文件、为什么改、是否越界；
- agent 请求权限，提供安全边界；
- 但频繁审批会把注意力不断交还给用户；
- agent 能运行测试；
- 但用户仍要判断测试覆盖是否足够、失败是否可信。

所以 coding agent 不是单纯 coordination technology，而是一个既执行任务又需要被协调的 agentic artifact。

### 3.3 旧概念多是结构成本，我们需要个体感知成本

coordination cost 在组织和平台研究中常常表现为绩效、退出、生产率、架构传播成本、团队冲突或项目结果。

我们要测量的是：

> 在一次具体 coding agent task episode 中，用户感到自己为了让 agent 的自主工作保持可对齐、可追踪、可审批、可验证、可接管，需要付出多少额外协调努力。

这使它成为个体层面的 UX 构念，而不是组织效率变量。

### 3.4 coding agent 特有的是“委托后的代码工件协调”

普通 AI chatbot 可以建议代码，但不会直接改变项目状态。普通 IDE 工具可以修改代码，但不会以多步自主行动方式承担任务。人类同事可以协作编码，但不会以工具权限、CLI 输出、diff、审批提示和自动命令的形式不断交还注意力。

coding agent 的独特组合是：

- 可被委托；
- 可多步自主行动；
- 可读取和修改代码库；
- 可运行命令和测试；
- 会请求权限或交还注意力；
- 用户仍保留最终责任。

这个组合让 coordination cost 不再只是“沟通成本”或“团队协作成本”，而是 **delegated autonomous code-work coordination cost**。

## 4. 建议的新构念表述

名称仍可以调整，但目前最清楚的工作名称是：

**编码代理委托协调负担**

英文：

**Perceived Coordination Burden in Coding-Agent Delegation**

也可以更短：

**Coding-Agent Coordination Burden**

### 定义草案

编码代理委托协调负担是指：

> 开发者在一次具体编程任务中，将部分工作委托给能够多步行动并改变项目状态的 coding agent 后，为了管理用户目标、agent 行动、代码库依赖、权限交还、验证证据和接管责任之间不断生成的相互依赖关系，而感知到的额外协调努力。

这个定义的重点不是“工具难用”，而是“委托后为了协调相互依赖而付出的努力”。

### 它测量什么

它测量的是一个连续程度：

> 用户为了让 coding agent 的自主工作保持可对齐、可追踪、可分流、可整合、可恢复，需要额外操心和操作到什么程度。

低协调负担：

- 用户容易界定 agent 的任务边界；
- agent 的行动轨迹和代码变更容易跟上；
- 审批请求少且风险层级清楚；
- diff、测试、日志等证据足以支持判断；
- 用户清楚什么时候继续委托、什么时候介入或接管。

高协调负担：

- 用户需要不断补充任务边界和约束；
- 很难理解 agent 做了什么、为什么做、改动会影响哪里；
- 审批和通知频繁打断任务节奏；
- 用户需要额外整合 diff、测试、日志和上下文才能决定是否接受；
- 用户不断纠结是否暂停、回滚、接管或重做。

## 5. 初步维度只能作为 sensitizing concepts

这些维度不应被写死。Reddit 评论和后续访谈必须允许推翻、合并或新增维度。

但从现有文献看，可以先把以下五类作为 sensitizing concepts：

| 暂定维度 | 来自哪些基础概念 | coding agent 中的含义 |
| --- | --- | --- |
| 任务/依赖界定负担 | task interdependence; software project coordination; IS delegation appraisal/distribution | 用户需要把任务目标、边界、约束、不可触碰文件、完成标准讲清楚，避免 agent 在相互依赖的代码库中误动 |
| 行动与工件状态追踪负担 | artifact-based coordination; architecture visibility; communication visibility | 用户需要理解 agent 的多步行动、命令、文件修改、diff 与当前代码库状态之间的关系 |
| 审批与注意力交还分流负担 | coordination episodes; technology-mediated coordination; interruption/warning literature | 用户需要判断哪些权限请求是例行的，哪些是高风险的，并在注意力被交还时保持任务连续性 |
| 变更传播验证整合负担 | propagation costs; software architecture interdependence; verification burden | 用户需要判断 agent 的代码修改是否会在模块、依赖、测试、行为上产生副作用 |
| 接管与恢复决策负担 | IS delegation coordination; autonomy/control; unresolved interdependencies | 用户需要判断什么时候继续让 agent 做，什么时候限制、接管、回滚、修复或重新委托 |

这里的维度不是“拼贴旧概念”。它们共同指向一个更高层的东西：

> 用户在委托 coding agent 后，如何承担管理 agent 行动与代码工件相互依赖关系的协调成本。

## 6. 与相邻概念的严格区别

| 相邻概念 | 为什么相近 | 为什么不能替代我们要开发的构念 |
| --- | --- | --- |
| usability | 都和用户体验有关 | usability 过宽，通常回答系统是否容易学、容易用、有效率；我们回答的是委托 agent 后协调相互依赖需要付出多少努力 |
| perceived control | 高协调负担可能降低掌控感 | 掌控感是用户觉得事情是否在控制中；协调负担是用户为了维持这种状态需要付出多少协调努力。它更像前因，控制感更像后果 |
| trust in AI | 信任会影响是否愿意委托 | 用户可能信任 agent 但仍觉得协调它很累；也可能不信任但通过高强度协调勉强使用。trust 不能解释审批、追踪、变更整合、接管等具体负担 |
| technostress/work overload | 都涉及负担和压力 | technostress 太宽，来源可以是任何技术复杂性、侵入、过载；我们的负担来源被严格限定为委托后管理 agent-code-task interdependencies |
| verification burden | 代码检查是重要部分 | verification 只覆盖判断产出是否正确；协调负担还包括任务边界、行动追踪、审批分流、接管恢复 |
| interruption/approval fatigue | 审批交还会造成疲劳 | approval fatigue 只解释频繁提示导致疲劳或习惯化；协调负担还解释为什么每次提示都需要用户把它放回任务和代码状态中判断 |
| coordination affordance | 技术功能可以支持协调 | affordance 是设计能力或前因；coordination burden 是用户仍然感知到的协调成本 |
| software project coordination | 软件开发本来需要协调 | 传统软件项目协调多为团队/项目层面；我们是个体开发者与 agentic code-changing artifact 的 task episode 层面 |

## 7. 如何模仿 Chen 和 Dong 的写法

Dong thesis 的做法可以这样迁移：

| Dong thesis | 我们的对应 |
| --- | --- |
| 广义基础概念：IT affordance | 广义基础概念：coordination cost / coordination effort in managing interdependencies |
| 新情境：social commerce | 新情境：coding-agent delegation in software development task episodes |
| 旧概念不足：传统 affordance 维度不能覆盖 social commerce | 旧概念不足：传统 coordination cost 多为组织/团队/平台层面，不能覆盖 agentic artifact 自主修改代码、审批交还、验证整合和接管恢复 |
| 情境化构念：social commerce IT affordance | 情境化构念：perceived coordination burden in coding-agent delegation |
| 数据：访谈、专家、量表开发 | 数据：Reddit 评论、真实用户访谈、task episode 材料、专家/Q-sort、量表开发 |

Chen 2024 的做法可以这样迁移：

| Chen 2024 | 我们的对应 |
| --- | --- |
| 不是纯归纳，而是用评论材料回到 cooperative principle theory | 不是纯 Reddit 主题分析，而是用评论材料回到 coordination cost / IS delegation / software coordination |
| 发现原理论不够覆盖 voice-interaction 的 anthropomorphism | 发现传统 coordination cost 不够覆盖 coding agent 的 autonomous code-changing delegation |
| 开发 voice-interaction usability 的维度和量表 | 开发 coding-agent-specific coordination burden 的维度和量表 |
| 和 TAM、UTAUT、MUG 等比较 | 和 usability、trust、control、technostress、verification burden、approval fatigue 比较 |

关键写法应该是：

1. coordination cost 适用，因为 coding agent 委托后确实要管理 interdependencies；
2. coordination cost 不够，因为传统文献没有处理“agentic artifact 自主改变代码库且持续交还权限/注意力”的个体任务体验；
3. 所以需要开发一个 coding-agent-specific 的 perceived coordination burden 构念；
4. Reddit 和访谈不是为了证明我们预设的五个维度，而是为了发现用户如何自然描述这种协调负担，并检验哪些旧概念能迁移、哪些必须改造。

## 8. 下一步需要准备的材料

为了避免再“乱写”，下一步最好做三个具体产物：

1. **基础概念矩阵**  
   把 coordination cost、software project coordination、artifact-based coordination、technology-enabled coordination affordance、IS delegation 五条文献线逐篇整理成：原定义、研究对象、层级、前因、后果、测量或操作化方式、迁移限制。

2. **Reddit 开放编码代码本初稿**  
   不预设最终维度，只设 sensitizing questions：用户在委托 coding agent 后需要协调什么、为什么协调困难、协调失败造成什么后果、哪些工具设计降低/增加协调负担。

3. **相邻概念排除表**  
   对 usability、trust、control、technostress、verification burden、approval fatigue、cognitive load、readability、transparency 逐一说明：可解释什么、不能解释什么、在模型中应该作为前因/后果/竞争构念/控制变量。

当前最重要的判断是：

> 我们应该以 **coordination cost in managing interdependencies** 为基础概念，以 **artifact-based coordination / propagation costs** 和 **software project coordination** 缩小到代码情境，再用 **IS delegation / agentic IS** 说明为什么 coding agent 使这个基础概念必须被改造。
