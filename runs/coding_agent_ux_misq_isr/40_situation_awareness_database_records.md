# Situation Awareness 在 Top11 摘要数据库中的检索记录

本文件整理 `database/ALL_AIS_Basket_11.csv` 中命中 situation awareness 相关精确短语的全部记录，并逐篇说明其研究内容及其对 coding agent UX 概念开发的价值。

## 检索口径

- 数据源：`E:\github\qual-llm-check-IS-utd\database\ALL_AIS_Basket_11.csv`
- 输出子集：`E:\github\qual-llm-check-IS-utd\runs\coding_agent_ux_misq_isr\40_situation_awareness_database_records.csv`
- 检索字段：`Title`、`Abstract`、`Author Keywords`、`Index Keywords`
- 检索词：精确短语 `situation awareness` 与 `situational awareness`，大小写不敏感
- 未纳入：缩写 `SA`，因为噪音过高，无法可靠表示 situation awareness
- 命中数量：16 篇

## 总体判断

这 16 篇文献说明，situation awareness 在 IS Top11 数据库里主要被用于五类问题：危机/应急响应、网络安全、决策支持系统、仪表盘/自动化以及在线协作感知。对我们最有价值的不是所有命中文献，而是那些把 situation awareness 做成个体层、动态任务情境、系统设计或行为后果变量的研究。

最值得作为 coding agent 概念开发参照的文献是：

1. Jaeger & Eckhardt 2021，Information Systems Journal：从一般 situation awareness 迁移出 situational information security awareness，是个体层、动态情境、前因-后果路径都比较清楚的范例。
2. Nadj et al. 2020，Decision Support Systems：直接研究 dashboard 功能如何影响 situation awareness 和 task performance，并指出性能提升可能伴随 out-of-the-loop 问题。
3. MISQ 2025 社区 first responder 研究：明确使用 perception、comprehension、projection 三层结构支持远程、非专业响应者的及时决策。
4. DSS 2014 safety-critical SASS 研究：把 situation awareness 作为降低复杂动态情境中工作负荷、压力和错误的认知支持目标。
5. DSS 2024 cyber situational awareness 研究：把 perception、comprehension、projection 用到 AI 辅助的技术风险判断中，对 coding agent 的代码风险/变更影响解释有类比价值。

因此，如果我们继续开发 coding-agent-specific UX 概念，situation awareness 比 workspace awareness 更适合作为基础概念候选。不过它不能被照搬，因为 coding agent 情境中的核心对象不是外部环境、危机事件或普通仪表盘状态，而是 agent 正在改变代码库、调用工具、生成中间行动、隐含未来影响的动态任务状态。更合理的迁移方向是：coding-agent task-state awareness，即用户对 coding agent 当前任务状态的感知、理解与预测能力。

## 逐篇介绍

### 1. Empowering crisis information extraction through actionability event schemata and domain-adaptive pre-training

- 年份/期刊：2025，Information and Management
- DOI：10.1016/j.im.2024.104065
- 命中位置：Abstract；Index Keywords
- 文章主要做了什么：这篇文章研究危机检测中的可行动信息抽取。作者指出，已有社交媒体危机检测研究往往关注 situational awareness，但缺少能直接支持 emergency response 的 actionable insights。因此文章提出 actionability schema 与 domain-adaptive pre-training，用于从社交媒体中抽取更可行动的信息，并在 F1 上改进模型表现。
- 对我们的价值：它提示一个重要边界：awareness 本身不一定足够，用户还需要能把当前状态转化为行动判断。迁移到 coding agent 场景，这可以支持我们区分“用户知道 agent 做了什么”和“用户知道自己是否需要批准、介入、回滚或继续”。不过这篇文章本身主要是危机信息抽取，不是个体 UX 构念研究，因此只能作为弱到中等相关的设计启发。

### 2. SUPPORTING COMMUNITY FIRST RESPONDERS IN AGING IN PLACE: AN ACTION DESIGN FOR A COMMUNITY-BASED SMART ACTIVITY MONITORING SYSTEM

- 年份/期刊：2025，MIS Quarterly: Management Information Systems
- DOI：10.25300/MISQ/2024/18446
- 命中位置：Abstract；Author Keywords；Index Keywords
- 文章主要做了什么：这篇 MISQ 文章基于三年 action design research，研究传感器和 IoT 监测系统如何支持老人居家养老场景中的社区 first responders。关键问题是，这些响应者位于远程位置，且不具备专业医疗知识，系统需要帮助他们形成 situational awareness。文章基于 situation awareness model，提出四个设计原则，目标是增强 responders 对信息的 perception、comprehension 与 projection，从而支持及时、知情的响应。
- 对我们的价值：这是强相关文献。它和 coding agent 的共通点不在领域，而在任务结构：用户并不持续亲临“现场”，而是通过系统痕迹远程理解一个动态任务；用户可能不是底层执行细节的专家，却仍然要做出及时判断。coding agent 场景里，用户也需要通过 diff、tool log、terminal output、agent message 来判断 agent 的行动是否合理。因此这篇文章可以帮助我们把概念边界写清楚：不是泛泛的信任、满意或控制感，而是用户能否在远程、异步、信息不完全的情况下形成对 agent 任务状态的感知、理解和预测。

### 3. Enhanced (cyber) situational awareness: Using interpretable principal component analysis (iPCA) to automate vulnerability severity scoring

- 年份/期刊：2024，Decision Support Systems
- DOI：10.1016/j.dss.2024.114308
- 命中位置：Title；Abstract；Author Keywords；Index Keywords
- 文章主要做了什么：这篇文章把 situational awareness theory 用于网络安全漏洞严重性评分。作者将 perception、comprehension、projection 组件整合进自动化 DSS，用 iPCA 与机器学习根据 CVE 文本预测 CVSS 分数，并比较多种模型，包括传统机器学习、LSTM 与 Transformer/ChatGPT。文章认为该系统能改善 cybersecurity managers 的 situational awareness 与决策。
- 对我们的价值：它对 coding agent 有中高价值，尤其是“AI 辅助理解技术风险状态”这一点。coding agent 用户也经常需要判断某个代码变更、依赖修改、测试失败或安全风险的严重性。但这篇文章的主要对象是漏洞评分系统，个体 UX 不是核心，因此它更适合作为“技术风险状态可解释化”的补充文献，而不是我们的主基础文献。

### 4. CROSS-LINGUAL CYBERSECURITY ANALYTICS IN THE INTERNATIONAL DARK WEB WITH ADVERSARIAL DEEP REPRESENTATION LEARNING

- 年份/期刊：2022，MIS Quarterly: Management Information Systems
- DOI：10.25300/MISQ/2022/16618
- 命中位置：Abstract
- 文章主要做了什么：这篇 MISQ research note 以 computational design science 为路径，开发 cross-lingual hacker asset detection artifact。它用 adversarial deep representation learning，把英文内容中学到的知识迁移到非英语 dark web 平台，用来检测 malware、hacking tools、hacking tutorials、malicious source code 等 hacker assets，从而增强网络安全分析组织的 situational awareness。
- 对我们的价值：这篇文章说明 AI artifact 可以通过跨语言、多源数据分析增强对复杂技术环境的 awareness。但它的核心是 cybersecurity analytics artifact 与组织/分析团队层面的态势增强，不是个体用户在与 agent 协作中的任务状态觉察。因此对我们来说是弱相关背景，不应作为概念开发主线。

### 5. THE OPM DATA BREACH: AN INVESTIGATION OF SHARED EMOTIONAL REACTIONS ON TWITTER

- 年份/期刊：2022，MIS Quarterly: Management Information Systems
- DOI：10.25300/MISQ/2022/15596
- 命中位置：Abstract；Author Keywords；Index Keywords
- 文章主要做了什么：这篇文章分析 2015 年 OPM data breach 后 Twitter 上超过 18,000 条讨论，研究公众在危机事件后的共享情绪反应。文章发现，焦虑、愤怒和悲伤等情绪在聚合层面上与公众对 breach event 的 situational awareness 相对应，并进一步分析不同 breach concepts 如何驱动这些情绪。
- 对我们的价值：这篇文章展示了 situation awareness 可以和集体 sensemaking、情绪反应、危机事件理解联系起来。但它研究的是社交媒体公共讨论和共享情绪，不是个体层任务执行中的 agent 协作体验。因此它对我们的问题只有低到中等启发：可以提醒我们 awareness 可能影响情绪性后果，但不能作为 coding agent UX 构念的核心基础。

### 6. Eyes wide open: The role of situational information security awareness for security-related behaviour

- 年份/期刊：2021，Information Systems Journal
- DOI：10.1111/isj.12317
- 命中位置：Abstract；Index Keywords
- 文章主要做了什么：这篇文章明确从 situation awareness 文献中推导并定义 situational information security awareness。它反对只研究静态的信息安全意识，转向动态、情境化、interactionist 的视角，认为 security-related behaviours 来自个体与威胁情境感知之间的互动。文章用 107 名员工的 phishing experiment，结合 eye tracking 与 survey，检验个体层因素和系统层因素如何影响 awareness，以及 awareness 如何影响 threat appraisal、coping appraisal 和实际安全行为。结果显示，过去 phishing 经验和 security warning 会提高 awareness；邮件的 contextual relevance 和 misplaced salience 会降低 awareness；situational information security awareness 会提高 perceived threat、perceived coping efficacy，并最终影响实际行为。
- 对我们的价值：这是最强相关文献之一。它提供了一个非常好的“迁移范例”：不是简单照搬 situation awareness，而是把它改造为某一 IS 情境下的个体层、动态、情境性构念。我们可以模仿它的理论动作，把 general situation awareness 迁移为 coding-agent task-state awareness。coding agent 场景中，用户并不是一般地“有安全意识”或“信任 AI”，而是在一个具体 agent 执行任务中，对 agent 行动、代码状态、工具输出、潜在风险和下一步影响形成情境化觉察。它还给我们提供了前因/后果写法的模板：经验、系统提示、信息呈现方式可能影响 awareness；awareness 进而影响风险判断、应对效能、介入行为、采纳或回滚行为。

### 7. A new emergency decision support system: the automatic interpretation and contextualisation of events to model a crisis situation in real-time

- 年份/期刊：2020，Decision Support Systems
- DOI：10.1016/j.dss.2020.113260
- 命中位置：Author Keywords
- 文章主要做了什么：这篇文章设计并实现一种 emergency DSS，把多个实时数据源连接起来，自动解释和语境化事件，用于危机场景下的应急管理。系统结合 event-driven 与 model-driven architecture，用复杂事件处理和图数据库持续更新 common operational picture，帮助 emergency managers 理解不断变化的危机状态。
- 对我们的价值：它对 coding agent 的启发在于“动态状态建模”和“持续更新的 operational picture”。coding agent 也会产生连续行动和多源痕迹，包括对文件的修改、命令执行、测试结果、依赖安装、失败恢复等。用户需要的可能不是更多日志，而是被整合后的任务状态图景。不过该文主要是 emergency DSS 架构，不是个体 UX 量表或构念，因此适合作为设计背景，不适合作为主基础概念。

### 8. The effect of interactive analytical dashboard features on situation awareness and task performance

- 年份/期刊：2020，Decision Support Systems
- DOI：10.1016/j.dss.2020.113322
- 命中位置：Title；Abstract；Author Keywords；Index Keywords
- 文章主要做了什么：这篇文章研究 operational DSS 中 interactive analytical dashboard features 对 situation awareness 和 task performance 的影响。作者以 situation awareness 为理论镜头，考察 what-if analysis 功能如何影响决策者的 SA 和任务表现。通过 83 名参与者的实验和 eye-tracking 数据，文章发现 what-if analysis 虽然提高任务表现，却可能降低 situation awareness，从而引发 out-of-the-loop problem。
- 对我们的价值：这是非常强的相关文献。它直接说明“系统让任务表现变好”与“用户对任务状态保持觉察”可能冲突。coding agent 的核心现实问题正是如此：agent 可以替用户完成更多工作，但用户可能越来越难知道代码到底改了什么、为什么这样改、风险在哪里、下一步会发生什么。这篇文章可以支撑我们把 coding-agent task-state awareness 作为独立于 task performance、trust 和 control 的关键 UX 构念，也可以帮助我们提出后果：低 awareness 可能导致 out-of-the-loop、审批疲劳、过度依赖、错误批准、回滚困难或放弃 CLI agent。

### 9. Developing novel solutions to realise the European Energy - Information Sharing & Analysis Centre

- 年份/期刊：2019，Decision Support Systems
- DOI：10.1016/j.dss.2019.05.007
- 命中位置：Abstract；Author Keywords；Index Keywords
- 文章主要做了什么：这篇文章研究欧洲能源部门的信息共享与分析中心 EE-ISAC 的形成，目标是通过共享最新网络安全知识，提高从技术层到战略层的 multilevel situation awareness，以改善对网络事件的准备和响应。
- 对我们的价值：这篇文章说明 situation awareness 可被用于跨主体的信息共享和网络安全响应，但它明显偏向行业/部门层面的安全协作。因为我们当前明确聚焦 individual-level coding agent UX，这篇不应进入核心理论基础，只能作为数据库中 SA 使用范围的记录。

### 10. Role of social media in social change: An analysis of collective sense making during the 2011 Egypt Revolution

- 年份/期刊：2015，Information Systems Research
- DOI：10.1287/isre.2015.0565
- 命中位置：Abstract
- 文章主要做了什么：这篇 ISR 文章研究 2011 年埃及革命期间 Twitter 在社会变革中的作用，重点分析 collective sense making。作者将社交媒体中的集体 sensemaking 理解为 human-machine collaborative information processing，并通过 hashtags 的使用研究 milling 和 keynoting 等现象。文章发现，一些 hashtags 用来聚合注意力，另一些用于分享变化中的 situational information，从而帮助维持不稳定政治情境中的 situational awareness。
- 对我们的价值：这篇文章对“human-machine collaborative information processing”有启发，但它研究的是群体层面的社交媒体 sensemaking，不是 coding agent 中个体用户对 agent 任务状态的觉察。它可以帮助我们理解信息痕迹如何支持动态情境理解，但不适合作为核心量表开发基础。

### 11. An intelligent situation awareness support system for safety-critical environments

- 年份/期刊：2014，Decision Support Systems
- DOI：10.1016/j.dss.2014.01.004
- 命中位置：Title；Abstract；Author Keywords；Index Keywords
- 文章主要做了什么：这篇文章面向 safety-critical environments 中的 abnormal situations，提出一个 cognition-driven decision support system，即 situation awareness support system。文章认为操作者在异常情境中需要认知支持，以降低 workload、stress 和 error rate；其中正确理解情境，也就是 situation awareness，是提高表现和减少错误的关键。系统包含数据收集、基于动态贝叶斯网络的情境评估、风险估计、恢复建议和 HCI，并建议使用 SA measures 做完整评价。
- 对我们的价值：这是中高相关文献。coding agent 虽然不是传统 safety-critical 系统，但同样包含动态、不完全信息、潜在风险和人机分工。它尤其能帮助我们说明：我们的目标不是让用户“看到更多信息”，而是帮助用户在复杂 agent 行动中维持正确情境理解，从而减少错误批准、遗漏风险和高负荷检查。它也支持把 system design 作为 awareness 的前因，把 workload、stress、error reduction 或 task quality 作为后果。

### 12. Object typicality for effective Web of Things recommendations

- 年份/期刊：2014，Decision Support Systems
- DOI：10.1016/j.dss.2013.09.008
- 命中位置：Abstract；Author Keywords；Index Keywords
- 文章主要做了什么：这篇文章研究 Web of Things 推荐中的 object typicality，目标是解决稀疏推荐空间和 big-error recommendations 问题。作者提出基于认知心理学中 object typicality 原理的推荐方法，并在 MovieLens 和 Netflix benchmark 上测试效果。文章最后指出该方法可以增强 WoT applications 的 situation awareness，促进资源复用和企业间互操作。
- 对我们的价值：这篇文章与我们的主题关系较弱。它的核心不是 situation awareness，而是推荐算法；SA 更像是附带的应用收益表述。因此它不适合作为 coding agent UX 概念开发的基础文献。

### 13. A platform for situational awareness in operational BI

- 年份/期刊：2012，Decision Support Systems
- DOI：10.1016/j.dss.2011.11.011
- 命中位置：Title；Abstract；Author Keywords；Index Keywords
- 文章主要做了什么：这篇文章提出 HP Labs 的 SIE-OBI 平台，用于 operational BI 中的 situational awareness。平台把近实时的非结构化 web data 与企业内部文档关联起来，使 business managers 能意识到影响业务运营或合同的外部事件，并及时做出运营决策。
- 对我们的价值：它说明 situation awareness 可以被理解为从多源、非结构化、流式信息中形成对当前业务状态的及时理解。coding agent 中也存在多源流式痕迹：agent 消息、diff、terminal output、test failures、dependency changes 等。不过这篇文章主要是 BI 平台架构和业务事件感知，不是个体层测量研究，因此可作为设计类参照，而不是核心基础文献。

### 14. Design principles of integrated information platform for emergency responses: The case of 2008 Beijing Olympic Games

- 年份/期刊：2012，Information Systems Research
- DOI：10.1287/isre.1110.0387
- 命中位置：Index Keywords
- 文章主要做了什么：这篇 ISR 文章基于 action research、participatory design 和 situation-awareness oriented design，研究北京奥运会应急响应集成信息平台的设计原则。系统包括信息收集、数据库管理、决策支持服务，其中决策支持包括 situational overview、instant risk assessment、emergency response preplan 和 disaster development prediction。
- 对我们的价值：它对 coding agent 有一定设计启发：用户需要的不只是原始数据，而是 overview、risk assessment、response plan 和 future prediction。不过它是应急管理平台设计研究，且检索命中主要来自索引关键词；对个体层 UX 构念开发的直接价值有限。

### 15. Using AI and games for decision support in command and control

- 年份/期刊：2007，Decision Support Systems
- DOI：10.1016/j.dss.2006.06.012
- 命中位置：Abstract；Author Keywords；Index Keywords
- 文章主要做了什么：这篇文章面向 command and control centers 的决策支持，处理来自不同传感器的大量不确定报告，目标是进行信息融合、形成可理解的信息，并预测未来事件。作者提出结合 game theory、AI、Bayesian networks 和 influence diagrams 的 decision support tool，用来增强 situation awareness。
- 对我们的价值：这篇文章的价值在于强调 SA 不只是当前状态展示，还包括不确定信息整合与未来事件预测。coding agent 场景里，用户也需要预测 agent 后续行动、代码变更影响和潜在风险。但它属于军事/指挥控制 DSS，距离 individual-level coding agent UX 较远，因此应作为外围参照。

### 16. Meeting others - Supporting situation awareness on the WWW

- 年份/期刊：2001，Decision Support Systems
- DOI：10.1016/S0167-9236(01)00101-4
- 命中位置：Title；Abstract；Author Keywords
- 文章主要做了什么：这篇较早的 DSS 文章讨论 WWW 平台上的 situation awareness 支持。作者指出 WWW 支持文档共享和信息检索，但缺少直接用户互动和 awareness 支持机制。文章介绍 situation awareness 概念、用于考察 awareness support systems 的理论框架，并分析 PeopleAwarenessEngine 如何支持用户沟通与协作。
- 对我们的价值：这篇文章更接近 CSCW/在线协作中的“他人意识”或“协作感知”，与 workspace awareness 有一定重合。它可以帮助我们理解为什么 awareness 文献中会出现多种对象：环境状态、任务状态、他人状态、协作状态。但对 coding agent 来说，关键不是知道“其他人在哪里/做什么”，而是知道 agent 对代码任务正在做什么、做到了哪里、意味着什么、下一步会影响什么。因此它可作为概念边界辨析材料，而不应作为主基础文献。

## 对我们下一步的启示

如果以 situation awareness 为基础概念，最严谨的做法不是直接使用原概念，而是像 ISJ 2021 那样进行情境化迁移：

- 基础概念：situation awareness，尤其是 perception、comprehension、projection 三层结构。
- 已有迁移范例：situational information security awareness，说明 IS 文献允许把 general SA 改造为具体 IS 使用情境下的个体层动态构念。
- coding agent 中的新情境差异：用户觉察的对象不是一般环境、危机事件或静态仪表盘，而是 agent 在代码库中执行任务的动态状态，包括行动、理由、证据、代码影响、风险和后续轨迹。
- 可能的新构念：coding-agent task-state awareness。
- 可能定义：用户在与 coding agent 协作完成编程任务时，对 agent 当前行动、代码库变化、工具执行结果、任务进展、潜在风险及下一步影响的感知、理解与预测程度。
- 可能后果：更高质量的审批/介入/回滚决策、更低 out-of-the-loop 风险、更低检查负担、更高有效控制感、更高持续使用意愿。
- 可能前因：diff 可视化质量、工具调用可追踪性、变更摘要质量、检查点设计、审批频率、agent 行动粒度、用户编程经验、任务复杂度、失败/回滚经历。
