# 基础概念选择审查：到底基于哪个概念开发最好

> **2026-07-09 修正提示**：本文件是在仅结合 database 和初步外部检索后形成的中间判断。后续 `36_external_literature_usage_check_workspace_awareness.md` 进一步检查了外部学术索引后，认为 `workspace awareness` 虽然不是无人使用，但主要集中在 CSCW/HCI 小众文献中；若要求基础概念具有更强主流文献地基，更推荐改用 `situation awareness` 作为唯一基础概念。

## 1. 这次审查纠正什么

之前的写法有一个问题：我把“备选概念”写成了辅助清单，但没有真正把它们当作竞争性的基础概念来评估。这里重新按论文概念开发的要求来做：

> 每个候选概念都必须回答：database 是否真实使用？文献如何定义？如何测量？如果迁移到 coding agent，旧概念哪里不够？它是否比其他候选更适合作为唯一基础概念？

这次结论有调整：

> **最推荐的基础概念从 mutual understanding 转为 workspace awareness。**  
> 更准确的新构念方向是 **coding-agent workspace awareness / 编码代理工作空间觉察**。

原因很简单：我们真正想解释的现实痛点不是泛泛的“用户和 agent 是否互相理解”，而是用户在 agent 自主修改代码、运行命令、产生 diff、请求审批时，是否能及时理解 agent 在共享代码工作空间里做了什么、为什么做、影响了哪里、下一步可能做什么。

这比 mutual understanding 更清楚、更容易测量，也更能和 CLI agent 的痛点对应。

## 2. longlist：database 使用情况

检索文件：`database/ALL_AIS_Basket_11.csv`  
检索字段：`Title`, `Abstract`, `Author Keywords`, `Index Keywords`

| 候选概念 | 命中文献数 | 短语命中数 | 初步判断 |
| --- | ---: | ---: | --- |
| workspace awareness | 1 | 6 | 强候选，命中少但概念极准 |
| situation awareness / situational awareness | 16 | 50 | 强候选，定义和测量成熟，但较泛 |
| activity awareness | 4 | 9 | 与 workspace awareness 相关，可作补充证据 |
| mutual understanding | 16 | 38 | 强候选，但更偏双方认知对齐 |
| shared understanding | 37 | 84 | 强候选，但多为组织/团队层面的 shared view |
| common ground | 7 | 12 | 沟通 grounding 强，但不够覆盖代码行动 |
| transactive memory / TMS | 23 | 187 | 测量成熟，但核心是“谁知道什么” |
| shared mental model | 9 | 36 | 测量成熟但偏团队层级和 mental model similarity |
| team cognition | 3 | 9 | 与 shared mental model 同类，偏团队 |
| communication quality | 13 | 30 | 太宽，常是过程/关系质量 |
| collaboration quality | 3 | 4 | 太像结果变量 |
| teamwork quality | 1 | 4 | 太宽，像 overall collaboration quality |
| perceived control | 20 | 37 | 应作为后果或区分效度对象 |
| trust | 1127 | 4103 | 太成熟、太泛，不是 coding-agent-specific 新概念 |
| transparency / explainability | 256 / 81 | 695 / 249 | 更像系统属性或设计前因 |
| cognitive load / workload | 39 / 52 | 119 / 101 | 更像后果或负担 |
| delegation | 68 | 176 | 重要，但更像行为/关系机制 |
| calibration | 34 | 75 | 多数不是人-AI reliance calibration，也不够核心 |

真正进入最终比较的只有：

1. workspace awareness
2. situation awareness
3. mutual understanding / shared understanding
4. common ground
5. transactive memory system
6. shared mental model / team cognition
7. teamwork quality / collaboration quality
8. transparency / explainability
9. perceived control / trust

## 3. 候选一：workspace awareness

### 3.1 database 证据

| 标题 | 年份 | 期刊 | DOI | 证据价值 |
| --- | ---: | --- | --- | --- |
| The Influence of workspace awareness on group intellective decision effectiveness | 2008 | European Journal of Information Systems | 10.1057/ejis.2008.51 | 直接以 workspace awareness 为核心概念，并在 IS 顶刊中实证检验 |

database 摘要里的定义非常清楚：

> Workspace awareness is an understanding of members interactions within a shared workspace.

该文把 workspace awareness 分成三个元素：

- **presence awareness**：是否能识别并区分工作空间中的成员；
- **behavior awareness**：是否能追踪和刻画他人的行为；
- **insight awareness**：是否理解他人行为背后的原因。

其主要发现是：insight awareness 对 decision quality 和 consensus 最关键；insight awareness 又依赖 behavior awareness；behavior awareness 又依赖 presence awareness。

### 3.2 更基础的原文定义

Gutwin and Greenberg 的 CSCW 文献将 workspace awareness 定义为对他人在共享工作空间中互动的即时理解。其核心元素包括：

- who：谁在工作空间里，谁做了某个动作；
- what：对方正在做什么，对方动作属于什么目标；
- artifact：对方作用于哪个对象；
- where：对方在哪里工作、能看见哪里、能触达哪里；
- activity history：刚刚发生过什么。

这不是“界面可读性”。它是协作中形成的一种认知状态：用户是否知道另一个行动者在共享工作空间中的活动及其含义。

### 3.3 文献怎么测量

workspace awareness 文献有两种测量传统。

第一种是 **awareness support manipulation**：

- 给界面增加 radar view、viewport、cursor、object motion 等 awareness cues；
- 比较任务完成时间、沟通效率、努力感、满意度、偏好、策略使用；
- 逻辑是：如果 awareness support 提升协作表现，说明 workspace awareness 是关键中介状态。

Gutwin and Greenberg (1998) 的实验就是这种方式。它比较普通 workspace miniature 和增强版 radar view，增强版显示他人的 viewport、cursor movement、object movement。

第二种是 **awareness components measurement**：

- Cooper and Haines (2008) 将其拆为 presence、behavior、insight awareness；
- 用实验任务检验这些 awareness 元素如何影响 decision quality 和 consensus；
- 它更接近我们需要的量表开发逻辑，因为可以直接迁移成 coding-agent-specific facets。

### 3.4 为什么它最适合 coding agent

coding agent 的核心不是普通软件工具，而是会在共享代码工作空间中自主行动的协作者式 artifact。用户的真实困难常常是：

- 不知道 agent 正在改哪里；
- 不知道它为什么改这个文件；
- 不知道 diff 的语义影响；
- 不知道它是否吸收了我的限制；
- 不知道它跑了什么测试、结果意味着什么；
- 不知道下一步批准后会发生什么；
- 不知道当前代码库状态和 agent 的行动状态是否一致。

这些都不是 trust 本身，也不是 control 本身。它们更像：

> 用户对 coding agent 在共享代码工作空间中行动的 presence、behavior、artifact/location、insight、history 和 trajectory 的觉察程度。

### 3.5 旧概念为什么必须迁移

传统 workspace awareness 不能直接照搬，原因也很清楚：

| 传统 workspace awareness | coding agent 情境中的断裂 |
| --- | --- |
| 协作者是人 | 协作者是 agentic coding artifact |
| 工作空间多为可视化共享画布、文档、图形对象 | 工作空间是代码库、终端、测试、diff、依赖和版本状态 |
| 行动通常有可见的指针、对象移动、视野位置 | agent 行动常被压缩成日志、patch、命令输出和审批提示 |
| presence 是“谁在场” | coding agent 中更关键的是“哪些状态变化由 agent 造成” |
| behavior 是“他在做什么” | coding agent 中是 edit/run/search/test/plan/rollback 等多步工具行动 |
| insight 是“为什么他这样做” | coding agent 中还要理解其对代码质量、约束、风险和下一步的含义 |

所以新构念不是原样搬运，而是应开发为：

> **Coding-agent workspace awareness**：用户在一次具体 coding-agent 编程任务中，对 agent 在共享代码工作空间中的行动来源、作用位置、操作对象、行为理由、状态影响、历史进展和下一步可能行动形成的、足以支持监督、协调、接续和纠偏的即时理解程度。

### 3.6 高低程度怎么理解

这是连续变量，不是 0-1。

高 coding-agent workspace awareness 的用户能回答：

- agent 刚刚改了哪些文件、函数或测试；
- 哪些改动是 agent 做的，哪些是自己原本已有的；
- agent 为什么做这些修改；
- 当前任务进展到哪一步；
- 哪些约束已经被遵守，哪些还可能有风险；
- 批准下一步后 agent 大概率会做什么；
- 如果要接手或纠偏，应该从哪里开始。

低 coding-agent workspace awareness 的用户会表现为：

- 只能盲批或全量检查；
- 看 diff 但不理解语义；
- 反复要求 agent 总结或解释；
- 不知道 agent 是否偏离任务；
- 不知道当前代码库是否处于安全状态；
- 通过频繁审批来弥补觉察不足，导致 approval fatigue；
- 最终接管、撤销、停用或降低授权。

### 3.7 初始测量方向

如果基于 workspace awareness 开发量表，初始 facets 可以严格来自原文，但做 coding-agent-specific 改造：

| 原构成 | coding-agent-specific facet | 示例题项方向 |
| --- | --- | --- |
| presence / authorship | 行动来源觉察 | 我能清楚区分哪些代码变化是 agent 造成的 |
| behavior | 行动过程觉察 | 我能及时知道 agent 正在执行什么类型的编程行动 |
| artifact/location | 作用对象觉察 | 我能清楚知道 agent 正在处理哪些文件、函数、测试或依赖 |
| history | 状态变化觉察 | 我能理解 agent 到目前为止已经改变了什么 |
| insight | 行动理由觉察 | 我能理解 agent 为什么采取当前修改或测试步骤 |
| projection / next action | 行动轨迹觉察 | 我能预期批准下一步后 agent 可能会做什么 |
| boundary/risk | 约束风险觉察 | 我能判断 agent 当前行动是否仍在我的约束边界内 |

测量可以结合三类方式：

1. **self-report scale**：任务后 7 点李克特，测用户感知的 awareness。
2. **objective awareness probes**：让用户回答“agent 改了什么、测试结果是什么、下一步是什么”，与日志和 diff ground truth 比较。
3. **behavioral outcomes**：审批准确率、误批率、检查时间、回滚率、接管率、任务完成质量。

这比 mutual understanding 更容易做出严谨测量，因为我们有真实 ground truth：agent logs、diff、tool calls、tests。

## 4. 候选二：situation awareness

### 4.1 database 证据

| 标题 | 年份 | 期刊 | DOI | 证据价值 |
| --- | ---: | --- | --- | --- |
| Eyes wide open: The role of situational information security awareness for security-related behaviour | 2021 | Information Systems Journal | 10.1111/isj.12317 | individual-level situational awareness，且用 eye tracking + survey |
| The effect of interactive analytical dashboard features on situation awareness and task performance | 2020 | Decision Support Systems | 10.1016/j.dss.2020.113322 | 操作型 DSS 中 SA 影响 task performance，且涉及 out-of-the-loop problem |
| Enhanced (cyber) situational awareness: Using interpretable principal component analysis (iPCA) to automate vulnerability severity scoring | 2024 | Decision Support Systems | 10.1016/j.dss.2024.114308 | 明确使用 perception、comprehension、projection 组件 |
| Supporting Community First Responders in Aging in Place | 2025 | MIS Quarterly | 10.25300/MISQ/2024/18446 | 设计原则用于提升远程 responders 的 perceptions、comprehension、projection |

### 4.2 定义和测量

situation awareness 的经典结构是：

- perception：感知环境中相关元素；
- comprehension：理解这些元素对当前目标的意义；
- projection：预测近期状态如何变化。

测量方式很成熟：

- **SAGAT**：任务中冻结场景，询问操作者当前状态，和 ground truth 比较；
- **SART**：操作者主观评价自己的 SA；
- **eye tracking / behavioral measures**：在 ISJ 2021 phishing 研究中被用于测量 situational information security awareness；
- **lab experiment**：DSS 2020 dashboard 研究用 SA lens、实验和 eye tracking 研究 dashboard features 对 SA 与 task performance 的影响。

### 4.3 为什么它强

situation awareness 很适合 coding agent，因为 coding agent 使用也是动态任务环境：

- 代码状态持续变化；
- agent 的行动可能导致用户 out of the loop；
- 用户需要感知当前状态、理解含义、预测下一步；
- 可以做 objective probe，测量非常严谨。

### 4.4 为什么它不是第一选择

问题是它太宽。situation awareness 可用于飞行、医疗、网络安全、应急响应、dashboard、DSS 等。它并不天然包含“另一个协作者正在共享工作空间中行动”的含义。

coding agent 的独特性不只是“动态环境中保持态势感知”，而是：

> 一个 agentic collaborator 正在替用户在代码工作空间里做事。

这更接近 workspace awareness，而不是普通 situation awareness。

因此，situation awareness 是强备选，尤其适合实验测量方法；但作为唯一基础概念，workspace awareness 更贴合 coding agent 的协作属性。

## 5. 候选三：mutual understanding / shared understanding

### 5.1 database 证据

| 标题 | 年份 | 期刊 | DOI | 证据价值 |
| --- | ---: | --- | --- | --- |
| Mutual understanding in information systems development: Changes within and across projects | 2019 | MIS Quarterly | 10.25300/MISQ/2019/13980 | 直接研究 ISD 项目中 mutual understanding 的变化和项目成功 |
| Does mutuality matter? Examining the bilateral nature and effects of CEO-CIO mutual understanding | 2016 | Journal of Strategic Information Systems | 10.1016/j.jsis.2016.01.001 | matched-pair survey，perceptual congruence 和 perspective-taking |
| CEO/CIO mutual understanding, strategic alignment, and the contribution of IS to the organization | 2010 | Information and Management | 10.1016/j.im.2010.01.002 | 用 CEO/CIO 双方对 IS 角色的看法测量 MU |
| Antecedents of IS Strategic Alignment: A Nomological Network | 2009 | Information Systems Research | 10.1287/isre.1070.0159 | shared understanding between CIO and TMT，前因包括 shared language/domain knowledge/systems of knowing |

### 5.2 定义和测量

mutual understanding 的核心是协作双方或多方对关键事项形成相互理解或认知对齐。测量常见为：

- 双方对同一事项的真实回答；
- 一方对另一方观点的预测；
- actual agreement；
- perceived agreement；
- perceptual congruence；
- perspective-taking；
- longitudinal process tracing：sensegiving、sensemaking、artifacts、stakeholder engagement。

shared understanding 在 Preston and Karahanna (2009) 中更具体：CIO 与 TMT 对组织中 IS 角色形成 shared understanding，并影响 IS strategic alignment。

### 5.3 为什么它强

它和 coding agent 的任务意图、约束吸收、纠偏等问题很接近。如果研究问题是：

> 用户是否感觉 agent 理解我的任务目标和约束？

mutual understanding 很有吸引力。

### 5.4 为什么它输给 workspace awareness

mutual/shared understanding 的问题是边界容易糊：

1. 它容易让人以为我们在测 agent 是否真的理解用户；
2. dyadic congruence 测量无法直接用于 agent；
3. 它会和 trust、perceived control、usability 混在一起；
4. 它没有直接抓住“共享代码工作空间中的可观察行动与状态变化”。

更关键的是，用户提到的 CLI 痛点不是“我和 agent 是否理念一致”这么抽象，而是：

- 我看不到 agent 改了什么；
- 我不知道审批下一步会发生什么；
- 我不知道它是不是越界；
- 我需要不断检查 diff 来恢复对任务状态的理解。

这些更像 workspace awareness 的缺失，而不是 mutual understanding 的缺失。

因此，mutual understanding 可以作为相邻理论或可能的后续机制，但不建议作为首选基础概念。

## 6. 候选四：common ground

### 6.1 database 证据

| 标题 | 年份 | 期刊 | DOI | 证据价值 |
| --- | ---: | --- | --- | --- |
| Supporting the design of data integration requirements during the development of data warehouses | 2017 | European Journal of Information Systems | 10.1057/ejis.2015.22 | 用 common ground 处理 data integration requirements 的 semantic heterogeneity |
| Articulation of work process models for organizational alignment and informed information system design | 2016 | Information and Management | 10.1016/j.im.2016.01.004 | 建模工具帮助协作者建立 common ground |
| Fostering quality and flow of online learning conversations by artifact-centered discourse systems | 2013 | Journal of the Association for Information Systems | 10.17705/1jais.00321 | 从 Clark 的 common ground 理论解释在线对话质量 |

### 6.2 定义和测量

common ground 强调沟通双方建立共同基础，使表达被理解并可用于后续互动。常见测量更偏过程：

- clarification；
- acknowledgment；
- repair；
- reference resolution；
- conversation flow；
- conversation quality。

### 6.3 为什么不选

common ground 适合解释 prompt 交互、澄清、上下文共享。但 coding agent 的核心 UX 不只是沟通是否说清楚，而是 agent 在代码工作空间中实际行动后，用户是否能理解行动轨迹和代码状态变化。

所以 common ground 不如 workspace awareness 覆盖完整。

## 7. 候选五：transactive memory system

### 7.1 database 证据

| 标题 | 年份 | 期刊 | DOI | 证据价值 |
| --- | ---: | --- | --- | --- |
| Attaining individual creativity and performance in multidisciplinary and geographically distributed IT project teams | 2022 | MIS Quarterly | 10.25300/MISQ/2022/14596 | TMS 影响 IT project team 中 individual creativity/performance |
| The group mind of hybrid teams with humans and intelligent agents in knowledge-intense work | 2025 | Journal of Information Technology | 10.1177/02683962241296883 | human + intelligent agent hybrid teams |
| Transactive memory systems as a collective filter for mitigating information overload | 2013 | Information and Organization | 10.1016/j.infoandorg.2013.06.001 | TMS 作为群体过滤信息过载的机制 |
| Team knowledge and coordination in geographically distributed software development | 2007 | Journal of Management Information Systems | 10.2753/MIS0742-1222240104 | team knowledge 和 coordination 在软件开发中的关系 |

### 7.2 定义和测量

TMS 研究的是团队围绕“谁知道什么”形成的分布式认知系统。Lewis (2003) 的经典量表是 15 item，三个维度：

- specialization；
- credibility；
- coordination。

这套测量非常成熟。

### 7.3 为什么不选

TMS 对 coding agent 很有用，但它关心的是：

> 用户是否知道 agent 擅长什么、该把什么交给它、是否相信它的专业性。

这更像 delegation calibration 或 task-agent fit 的前因。它不能直接解释用户为什么在 CLI agent 中看不清改动、为什么审批疲劳、为什么需要不断查看 diff。

所以 TMS 适合作为前因，不适合作为主基础概念。

## 8. 候选六：shared mental model / team cognition

### 8.1 database 证据

| 标题 | 年份 | 期刊 | DOI | 证据价值 |
| --- | ---: | --- | --- | --- |
| How pair programming influences team performance | 2019 | Information Systems Research | 10.1287/isre.2019.0856 | 软件开发团队中的 shared mental models |
| Team cognition: Development and evolution in software project teams | 2007 | Journal of Management Information Systems | 10.2753/MIS0742-1222240210 | software project teams 中 team cognition 演化 |
| Team knowledge and coordination in geographically distributed software development | 2007 | Journal of Management Information Systems | 10.2753/MIS0742-1222240104 | team knowledge、presence awareness、coordination |

### 8.2 定义和测量

shared mental model 测的是团队成员 mental models 的相似性、准确性或 sharedness。常见方式包括：

- concept maps；
- card sorting；
- paired comparison；
- Pathfinder networks；
- UCINET / multidimensional scaling；
- survey-based similarity。

### 8.3 为什么不选

它输在层级和对象：

- 偏 team-level；
- 需要比较多个成员的 mental model；
- 容易假设 agent 有可等同于人的 mental model；
- 很难自然做成普通 coding agent 用户体验量表。

因此它不是最好的基础概念。

## 9. 候选七：teamwork quality / collaboration quality

### 9.1 database 证据

| 概念 | 标题 | 年份 | 期刊 | DOI |
| --- | --- | ---: | --- | --- |
| teamwork quality | Relating collaborative technology use to teamwork quality and performance | 2003 | Journal of Management Information Systems | 10.1080/07421222.2003.11045747 |
| collaboration quality | Evaluating Team Collaboration Quality | 2015 | Journal of Management Information Systems | 10.1080/07421222.2015.1095042 |

### 9.2 定义和测量

Hoegl and Gemuenden (2001) 将 Teamwork Quality 定义为团队协作质量的综合概念，六个 facets 是：

- communication；
- coordination；
- balance of member contributions；
- mutual support；
- effort；
- cohesion。

### 9.3 为什么不选

它太像 overall outcome。如果基于它开发 coding agent 概念，很容易变成“和 agent 协作质量高不高”，这太宽，也不够独特。

它适合做后果变量：

> coding-agent workspace awareness 越高，perceived collaboration quality 越高。

## 10. 候选八：transparency / explainability

### 10.1 database 证据

| 标题 | 年份 | 期刊 | DOI | 证据价值 |
| --- | ---: | --- | --- | --- |
| Algorithm Sensemaking: How Platform Workers Make Sense of Algorithmic Management | 2022 | Journal of the Association for Information Systems | 10.17705/1jais.00774 | algorithmic opacity/transparency 影响 workers 的 sensemaking |
| How transparency affects algorithmic advice utilization | 2024 | Decision Support Systems | 10.1016/j.dss.2024.114273 | performance/process/purpose transparency 影响 trust 和 advice use |
| Explainable AI 相关文献 | 多篇 | DSS / I&M / MISQ 等 | 多个 | 多数把 explainability 当成设计机制或系统属性 |

### 10.2 定义和测量

transparency/explainability 通常测或操纵：

- performance transparency；
- process transparency；
- purpose transparency；
- explanation presence；
- feature importance；
- rationale；
- user trust；
- advice utilization；
- reliance。

### 10.3 为什么不选

它们是前因，不是我们要开发的用户体验状态。

比如 coding agent 显示 diff、计划、命令日志、测试摘要，这些都是 workspace awareness support。它们应该影响用户的 coding-agent workspace awareness，而不是替代这个构念。

换句话说：

> transparency/explainability 是设计属性；workspace awareness 是用户在协作中形成的认知状态。

## 11. 候选九：perceived control / trust

### 11.1 database 证据

database 中 `trust` 和 `control` 命中极多，说明它们当然是成熟概念。比如 trust calibration of automated security IT artifacts 研究关注 trust 与 tool reliance 的匹配。

### 11.2 为什么不选

这两个概念太成熟，也太泛。它们不能作为 coding-agent-specific 新概念的基础，因为旧理论基本能直接解释：

- trust：是否愿意依赖 agent；
- perceived control：是否感到自己能影响过程和结果。

真正需要解释的是更上游的东西：

> 为什么用户会失去控制感？为什么不信任？为什么需要频繁审批？

workspace awareness 给出更具体的机制：用户看不清 agent 在共享代码工作空间中的行动和影响，所以只能通过检查、审批、接管来恢复控制。

## 12. 最终比较

| 候选 | individual/task-episode 适配 | 定义清晰 | 测量成熟 | coding-agent 独特痛点适配 | 迁移必要性 | 最终判断 |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| workspace awareness | 5 | 5 | 4 | 5 | 5 | 最推荐 |
| situation awareness | 5 | 5 | 5 | 4 | 4 | 强备选 |
| mutual understanding | 4 | 4 | 4 | 3 | 4 | 可用但不最优 |
| shared understanding | 3 | 4 | 3 | 3 | 3 | 不如 mutual understanding 精确 |
| common ground | 4 | 5 | 3 | 3 | 4 | 只适合沟通 grounding |
| TMS | 4 | 5 | 5 | 3 | 3 | 前因/相邻构念 |
| shared mental model | 2 | 4 | 4 | 3 | 3 | 层级不合适 |
| teamwork quality | 3 | 4 | 4 | 2 | 2 | 后果变量 |
| transparency/explainability | 4 | 4 | 4 | 3 | 2 | 设计前因 |
| trust/control | 5 | 5 | 5 | 2 | 1 | 后果或区分效度对象 |

## 13. 当前最佳路线

建议把主线改成：

> **基础概念：workspace awareness**  
> **新构念：coding-agent workspace awareness**  
> **中文名：编码代理工作空间觉察**

初步定义：

> 编码代理工作空间觉察是指，用户在一次具体 coding-agent 编程任务中，对 agent 在共享代码工作空间中的行动来源、作用位置、操作对象、行为理由、状态影响、历史进展和下一步可能行动形成的、足以支持监督、协调、接续和纠偏的即时理解程度。

它和相邻概念的边界：

| 相邻概念 | 边界 |
| --- | --- |
| readability | readability 是信息是否易读；workspace awareness 是用户是否形成了对 agent 工作状态的即时理解 |
| transparency | transparency 是系统提供什么信息；workspace awareness 是用户获得了什么认知状态 |
| explainability | explainability 是解释机制；workspace awareness 是用户是否能用这些信息监督和接续任务 |
| control | control 是用户是否能影响过程/结果；workspace awareness 是控制之前的认知基础 |
| trust | trust 是是否愿意依赖；workspace awareness 是是否知道 agent 正在怎样行动 |
| mutual understanding | mutual understanding 是双方理解对齐；workspace awareness 是用户对 agent 在共享代码工作空间中行动的觉察 |
| cognitive load | cognitive load 是认知资源消耗；workspace awareness 低会增加负荷，但不是负荷本身 |

## 14. 这个概念的实践价值

它可以直接解释 coding agent 产品设计问题：

- **为什么 CLI agent 难用**：缺少足够的 workspace awareness cues，用户无法持续形成对 agent 行动和代码状态的理解。
- **为什么 approval fatigue 出现**：审批请求本来应该是控制点，但如果没有足够的 awareness，审批变成高频风险判断。
- **为什么用户反复查 diff**：diff inspection 是用户自行恢复 workspace awareness 的补偿行为。
- **为什么用户不愿意给 agent 更大权限**：不是单纯不信任，而是不知道 agent 会怎么改变共享代码工作空间。
- **为什么好的 agent UI 应该显示计划、当前动作、文件范围、测试结果、风险和下一步**：这些都是 workspace awareness support。

## 15. 后续概念开发需要准备什么

如果按这个路线继续，下一步应该准备：

1. **原文证据包**：精读 Gutwin & Greenberg (1998, 2002)、Cooper & Haines (2008)，摘出 workspace awareness 定义、元素、测量和因果链。
2. **coding-agent domain facets**：从 Reddit/Codex/Cursor/Claude Code/GitHub Copilot agent 评论中编码用户谈到的 awareness problems。
3. **初始 item pool**：从 presence、behavior、artifact/location、history、insight、trajectory、boundary/risk 改造题项。
4. **区分效度设计**：同时测 trust、perceived control、transparency、readability、cognitive load、verification burden。
5. **实验或调查设计**：让用户完成 coding-agent task episode，保留 logs/diffs/tests 作为 ground truth，可做 subjective scale + objective probes。

## 16. 参考链接

- Gutwin and Greenberg (1998), The Effects of Workspace Awareness Support on the Usability of Real-Time Distributed Groupware: https://www.cs.usask.ca/faculty/gutwin/1998/effects-techreport/html/report.html
- Gutwin and Greenberg (2002), A Descriptive Framework of Workspace Awareness for Real-Time Groupware: https://dl.eusset.eu/items/b46e156f-ecac-4ca6-9044-4fd37666d421
- Cooper and Haines (2008), The Influence of workspace awareness on group intellective decision effectiveness: https://www.researchgate.net/publication/220393158_The_Influence_of_workspace_awareness_on_group_intellective_decision_effectiveness
- Endsley et al. (1998), A Comparative Analysis of SAGAT and SART: https://journals.sagepub.com/doi/10.1177/154193129804200119
- Franke et al. (2021), Situational information security awareness: https://onlinelibrary.wiley.com/doi/abs/10.1111/isj.12317
- Speier-Pero et al. / DSS dashboard SA article: https://www.sciencedirect.com/science/article/pii/S0167923620300774
- Jenkin, Chan, and Sabherwal (2019), Mutual Understanding in ISD: https://aisel.aisnet.org/misq/vol43/iss2/15/
- Preston and Karahanna (2009), Antecedents of IS Strategic Alignment: https://pubsonline.informs.org/doi/10.1287/isre.1070.0159
- Benlian and Haffke (2016), CEO-CIO mutual understanding: https://www.researchgate.net/publication/291422047_Does_mutuality_matter_Examining_the_bilateral_nature_and_effects_of_CEO-CIO_mutual_understanding
- Lewis (2003) TMS scale summary: https://psychiatry.ucsd.edu/research/programs-centers/instep/tools-resource/definitions/emergent-states/cognitive-emergent-states/tms.html
- Hoegl and Gemuenden (2001), Teamwork Quality: https://ideas.repec.org/a/inm/ororsc/v12y2001i4p435-449.html
