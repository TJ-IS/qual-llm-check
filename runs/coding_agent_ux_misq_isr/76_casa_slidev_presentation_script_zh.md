# 编程智能体态势感知构念开发演示讲稿

> 对应 `75_casa_slidev_deck_en_refined/slides.md` 当前可见版本，共 36 页。第 1-27 页为主讲内容，第 28-36 页为参考文献备查。文献统一采用“作者与年份、题名、期刊或会议”格式，并分别说明文献内容及其在本页的论证作用。

## 第 1 页　Coding-Agent Situation Awareness

### 讲稿

各位好。今天汇报的主题是编程智能体态势感知，也就是 Coding-Agent Situation Awareness，简称 CASA。我们关注的不是编程智能体能够完成多少任务，而是当系统替用户连续采取行动并改变软件制品时，用户在多大程度上仍然感觉自己能够感知关键行动和变化、理解这些状态对任务目标的意义，并预期任务近期将如何发展。本次汇报将说明为什么这种态势感知具有重要现实价值、为什么既有态势感知构念不能直接覆盖编程智能体情境，以及如何以动态态势感知理论指导 CASA 的候选维度。

### 转场

要说明 CASA 为什么值得研究，首先需要把编程智能体放回软件开发的经济价值与信息系统能动化趋势之中。

### 文献依据、内容摘要与本页作用

- **Baird 与 Maruping（2021），《The Next Generation of Research on IS Use: A Theoretical Framework of Delegation to and from Agentic IS Artifacts》，MIS Quarterly。** 这里的 IS 是 Information Systems，即信息系统。这篇发表于信息系统领域顶级期刊 *MIS Quarterly* 的理论文章，是本研究理解能动型信息系统委托关系的核心文献。它把系统使用从用户直接操作扩展为用户与能动型信息系统制品之间的任务委托，并指出系统可以代表用户发起行动。**本页作用：** 界定 CASA 所处的代理式信息系统使用情境。
- **Taylor（1990），《Situational Awareness Rating Technique: The Development of a Tool for Aircrew Systems Design》，Situational Awareness in Aerospace Operations，NATO AGARD Conference Proceedings No. 478。** NATO 是 North Atlantic Treaty Organization，即北大西洋公约组织；AGARD 是 Advisory Group for Aerospace Research and Development，即航空航天研究与发展咨询组。这是主观态势感知测量的奠基性来源。Taylor 从空勤人员对自身任务体验的判断出发，开发了 Situational Awareness Rating Technique，即态势感知评定技术，简称 SART，并把态势感知表述为对影响任务安全、迅速和有效执行的事件、因素与变量所具有的知识、认知和预期。**本页作用：** 提供 CASA 的主观构念基础。
- **Endsley（1995b），《Toward a Theory of Situation Awareness in Dynamic Systems》，Human Factors。** 这是态势感知研究中引用最广泛的理论奠基文献之一，发表于人因工程领域的核心期刊 *Human Factors*。Endsley 将态势感知组织为对要素的感知、对意义的理解和对近期状态的预期三个递进层级，并系统讨论其前因与决策表现后果。**本页作用：** 提供后续设计 CASA 候选维度的组织理论。

---

## 第 2 页　Software Development Is Becoming an AI-Mediated Production Activity

### 讲稿

软件开发已经成为生成式人工智能最重要的应用领域之一。这里的人工智能英文为 Artificial Intelligence，简称 AI。麦肯锡估计，生成式人工智能对软件工程的直接生产率影响可能相当于年度软件工程支出的 20% 到 45%。Stack Overflow 的调查也显示，人工智能开发工具已经进入大量开发者的实际工作。更重要的是，信息系统正在从响应命令的被动工具发展为能够接收目标、发起行动并根据反馈调整行为的能动型系统。因此，这个研究情境的重要性不只是新产品受到关注，而是一个具有显著经济价值的生产活动正在发生基本的人机关系变化。

### 转场

但并非所有人工智能编程工具都构成我们所研究的情境，因此下一页先明确编程智能体是什么。

### 文献依据、内容摘要与本页作用

- **McKinsey Global Institute（2023），《The Economic Potential of Generative AI: The Next Productivity Frontier》，McKinsey Global Institute 研究报告。** 内容摘要：该报告估计生成式人工智能在不同企业职能中的经济潜力，并把软件工程列为价值最集中的领域之一。**本页作用：** 支撑软件开发情境的经济重要性，而不用于证明某一产品已经实现全部潜在收益。
- **Stack Overflow（2025），《2025 Developer Survey: AI》，Stack Overflow Developer Survey。** 内容摘要：该调查报告开发者使用或计划使用人工智能开发工具以及人工智能代理的情况。**本页作用：** 证明人工智能编程已经进入实际开发活动。
- **Schuetz 与 Venkatesh（2020），《The Rise of Human Machines: How Cognitive Computing Systems Challenge Assumptions of User-System Interaction》，Journal of the Association for Information Systems。** 内容摘要：该文讨论具有主动性和认知能力的系统如何挑战传统的用户发起、系统响应假设。**本页作用：** 把编程智能体置于信息系统能动化的更一般趋势中。
- **Baird 与 Maruping（2021），《The Next Generation of Research on IS Use: A Theoretical Framework of Delegation to and from Agentic IS Artifacts》，MIS Quarterly。** 内容摘要：该文以委托解释能动型信息系统如何代替用户行动。**本页作用：** 把宏观技术变化连接到后续的任务关系变化。

---

## 第 3 页　Coding Agents Execute Tasks, Not Isolated Suggestions

### 讲稿

本文所说的编程智能体，不是一次代码补全，也不是只生成一段文本的对话模型。它能够接受软件开发目标、获取项目情境、规划行动、调用编辑器或终端、修改代码和配置，并根据测试或运行结果继续调整。关键区别在于委托单位发生了变化。用户委托的是完整或相对完整的任务，系统自行选择完成任务所需的行动序列。因此，编程智能体是软件工作空间中的任务执行者，而不是单项建议生成器。

### 转场

当系统从提供建议转为执行任务时，用户参与软件开发的方式也随之改变。

### 文献依据、内容摘要与本页作用

- **Baird 与 Maruping（2021），《The Next Generation of Research on IS Use: A Theoretical Framework of Delegation to and from Agentic IS Artifacts》，MIS Quarterly。** 内容摘要：该文区分传统系统使用与向能动型信息系统委托任务，强调系统可以在不确定条件下发起行动。**本页作用：** 支撑以任务而非单次操作作为编程智能体的委托单位。
- **Kumar 等（2025），《Why AI Agents Still Need You: Findings from Developer-Agent Collaborations in the Wild》，IEEE/ACM International Conference on Automated Software Engineering。** 内容摘要：该现场研究观察开发者与软件智能体解决真实软件问题，呈现智能体读取情境、推进任务、调试和测试的过程。**本页作用：** 为多步骤任务执行者的定义提供直接经验依据。

---

## 第 4 页　Delegation Changes How Users Participate in Software Tasks

### 讲稿

传统开发工具主要支持用户亲自完成操作。用户输入命令、修改文件或点击界面，因此通常能够把软件状态变化与自己的行动记忆直接联系起来。编程智能体则允许用户提出目标，由系统连续推进任务。用户的工作由直接操作扩展到任务界定、情境提供、行动确认、变化理解和后续决策。这里最关键的变化是，用户与软件变化之间出现了间接关系，部分状态由被委托的智能体行动形成，而不是由用户亲自操作形成。

### 转场

这种间接性带来一个关键问题：系统能够代替用户行动，是否意味着用户不再需要持续判断？

### 文献依据、内容摘要与本页作用

- **Baird 与 Maruping（2021），《The Next Generation of Research on IS Use: A Theoretical Framework of Delegation to and from Agentic IS Artifacts》，MIS Quarterly。** 内容摘要：该文指出委托使信息系统由被操作的工具转变为能够代表用户行动的代理。**本页作用：** 直接支撑从直接操作到目标委托的关系变化。
- **Schuetz 与 Venkatesh（2020），《The Rise of Human Machines: How Cognitive Computing Systems Challenge Assumptions of User-System Interaction》，Journal of the Association for Information Systems。** 内容摘要：该文说明认知计算系统削弱传统人机交互中的被动系统假设。**本页作用：** 说明用户角色变化具有一般信息系统理论依据。
- **Kumar 等（2025），《Why AI Agents Still Need You: Findings from Developer-Agent Collaborations in the Wild》，IEEE/ACM International Conference on Automated Software Engineering。** 内容摘要：该研究记录开发者在任务中持续提供信息、查看进展和调整智能体。**本页作用：** 具体说明委托后的用户活动不再局限于直接编码。

---

## 第 5 页　Delegation Does Not Eliminate the Need for User Judgment

### 讲稿

现有现场研究表明，任务委托没有消除用户判断。Kumar 等发现，采用渐进方式推进任务并持续与智能体互动的开发者，更容易成功解决真实软件问题。Dhanorkar 等进一步发现，开发者的判断和审查贯穿事前限制、共同规划、实时查看和事后复核。委托减少的是逐项操作，并没有消除用户决定是否继续、是否介入以及是否接受结果的需要。相反，用户需要在没有亲自执行全部行动的情况下作出这些判断。

### 转场

用户要作出这些判断，就必须保持对智能体任务态势的感知、理解和预期，这正是 situation awareness 进入研究的地方。

### 文献依据、内容摘要与本页作用

- **Kumar 等（2025），《Why AI Agents Still Need You: Findings from Developer-Agent Collaborations in the Wild》，IEEE/ACM International Conference on Automated Software Engineering。** 内容摘要：该研究观察 19 名开发者处理 33 个真实软件问题，发现渐进式解决、持续互动、调试与测试是成功协作的重要组成。**本页作用：** 支撑对任务过程的持续参与不能被最终结果完全替代。
- **Dhanorkar 等（2026），《Human Oversight of Agentic Systems in Practice: Examining the Oversight Work, Challenges, and Heuristics of Developers Using Software Agents》，ACM Conference on Fairness, Accountability, and Transparency。** 内容摘要：该研究把开发者监督归纳为事前约束、共同规划、实时查看和事后复核，并指出代码审查困难。**本页作用：** 支撑用户判断贯穿代理式任务全过程。

---

## 第 6 页　A Subjective CASA Pathway to User Evaluations

### 讲稿

理解为什么值得研究主观 CASA，可以从航空系统设计中的主观态势感知传统出发。随着航空自动化提高，空勤人员逐渐从持续操作者转变为自动化系统的监督者。系统设计者不仅需要知道设备是否完成预定功能，还需要了解一种设计是否让操作者感觉自己仍然掌握局面，包括情境是否容易理解、信息是否足以形成整体认识，以及操作者是否感觉自己具有应对变化所需的注意资源。这种操作者对自身态势掌握程度的评价，本身就是自动化系统使用体验和设计质量的重要组成。

Taylor 于 1990 年开发 SART，正是为了测量这种主观体验。Taylor 没有先由研究者规定态势感知应该由哪些抽象指标构成，而是请 84 名英国皇家空军测试与作战空勤人员比较高、低态势感知情境，并从他们的判断中引出注意需求、注意资源和理解等构念。SART 因而回答的是一个以操作者为中心的设计问题，即不同系统与任务条件在多大程度上使操作者感觉自己了解正在发生什么，并具有理解和应对当前情境的认知条件。主观态势感知不是客观态势感知的不完整版本，而是操作者对自身任务认识状态的评价。

Endsley 等 1998 年对 SART 与 Situation Awareness Global Assessment Technique，即态势感知全局评估技术、简称 SAGAT 的比较，进一步明确了主观态势感知的经验位置。研究发现，SART 与整体主观态势感知判断、态势感知充分性、信心和主观绩效评价高度相关。这说明主观态势感知位于用户如何评价自身认知状态和任务体验的理论领域。用户感觉自己是否知情、是否理解局面以及是否能够预期发展，会共同形成其面对复杂系统时的认知信心。

编程智能体使这种主观体验变得尤其重要。智能体替用户规划并执行多步软件行动，任务状态不断由代理行动生成，并分布在对话、计划、代码差异、终端输出和测试证据之中。不同的行动轨迹呈现、文件差异组织、执行证据和通知方式，会影响用户是否感觉自己仍然知道智能体做了什么、这些变化意味着什么以及任务将向何处发展。即使智能体提供了相同数量的信息，信息如何被组织和呈现，也可能形成完全不同的清楚感、信心和控制感。CASA 正是用来刻画这种对代理生成任务态势的主观掌握程度。

采用主观问卷与这一研究对象直接一致。CASA 是用户对自身态势认识状态的评价，因而应由经历具体智能体任务的用户报告。任务后问卷能够把分散在整个代理式任务过程中的感知、理解和预期整合为可比较的个体评价，并用于检验不同界面设计、任务复杂性和用户经验如何塑造这种体验。它还能解释为什么功能和产出相近的编程智能体会带来不同的用户信心、感知控制和满意度。

基于这条逻辑，本页从左向右提出主观 CASA 的理论路径。行动轨迹、文件差异、执行证据、通知方式和任务复杂性等设计与任务条件，可能影响用户形成 CASA。CASA 随后可能影响用户对自身判断准备程度的信心、感知控制和满意度，并通过满意度进一步关系到持续使用。这里的核心价值在于揭示编程智能体设计如何转化为用户对任务态势的主观掌握体验，以及这种体验如何进入用户评价和使用选择。

### 转场

航空领域已经说明了主观态势感知如何成为面向操作者的系统设计评价。接下来需要回答的是，这一构念进入编程智能体情境后，需要包含哪些由代理式软件任务产生的独特内容。

### 文献依据、内容摘要与本页作用

- **Endsley（1995），《Toward a Theory of Situation Awareness in Dynamic Systems》，Human Factors。** 内容摘要：该文把态势感知置于动态决策过程中，系统说明感知、理解和预期如何构成个体对变化情境的认识，并讨论设计、工作负荷、压力、复杂性和自动化的影响。**本页作用：** 提供态势感知在复杂动态系统中具有设计价值的一般理论背景。
- **Taylor（1990），《Situational Awareness Rating Technique: The Development of a Tool for Aircrew Systems Design》，NATO AGARD Conference Proceedings No. 478。** 内容摘要：该研究面向自动化航空系统设计，使用情境生成、构念引出和结构验证程序，从 84 名英国皇家空军测试及作战空勤人员关于高、低态势感知情境的判断中发展 SART。量表围绕注意需求、注意资源和理解等主观评价内容形成，用于比较不同系统设计带给操作者的态势感知体验。**本页作用：** 直接回答为什么研究者采用主观问卷，即主观评价能够取得操作者对自身认知条件的整体判断，并为系统设计比较提供低干扰、可重复的评价工具。
- **Endsley 与 Kiris（1995），《The Out-of-the-Loop Performance Problem and Level of Control in Automation》，Human Factors。** 内容摘要：实验比较不同自动化水平，发现系统承担更多控制活动会改变操作者接触和认识系统状态的方式。**本页作用：** 说明自动化提高以后，支持用户保持对任务态势的认识会成为重要的人机设计问题。
- **Endsley、Selcon、Hardiman 与 Croft（1998），《A Comparative Analysis of SAGAT and SART for Evaluations of Situation Awareness》，Proceedings of the Human Factors and Ergonomics Society Annual Meeting。** 内容摘要：该研究比较客观冻结提问式 SAGAT 与主观自评式 SART。两种方法都可能识别设计差异，但彼此并不显著对应；SART 与主观信心和主观绩效评价关系更密切，而 SAGAT 依据用户对任务事实问题的正确回答评价客观态势感知。**本页作用：** 证明主观与客观态势感知是不同的研究对象，并为 CASA 聚焦用户自我感知到的态势认识提供直接依据。
- **Salmon、Stanton、Walker 与 Green（2006），《Situation Awareness Measurement: A Review of Applicability for C4i Environments》，Brunel University。** 内容摘要：该综述比较冻结提问、自评、实时探针、观察者评价和行为指标等多类方法，说明态势感知测量应当与具体研究对象、任务环境和理论目的匹配。**本页作用：** 支撑使用任务后主观问卷测量用户对自身态势认识状态的整体评价。
- **Nadj、Maedche 与 Schieder（2020），《The Effect of Interactive Analytical Dashboard Features on Situation Awareness and Task Performance》，Decision Support Systems。** 内容摘要：该实验表明，交互功能会改变用户形成态势认识的条件，而且态势感知能够作为独立于系统功能和任务结果的用户层变量进行研究。**本页作用：** 支撑把用户态势感知作为连接系统设计与用户结果的独立研究对象。
- **Baronas 与 Louis（1988），《Restoring a Sense of Control During Implementation: How User Involvement Leads to System Acceptance》，MIS Quarterly。** 内容摘要：该文研究用户参与如何恢复感知控制并促进系统接受。**本页作用：** 为 CASA 可能影响感知控制提供信息系统依据。
- **Bhattacherjee（2001），《Understanding Information Systems Continuance: An Expectation-Confirmation Model》，MIS Quarterly。** 内容摘要：该文建立期望确认模型，表明满意度和感知有用性影响持续使用意愿。**本页作用：** 为满意度进一步连接持续使用提供经典依据。

---

## 第 7 页　1. Research Question

### 讲稿

前面说明了编程智能体为何重要，以及用户为什么仍需保持态势感知。第一部分接下来完成三项工作：把现实中的判断活动概括为明确研究现象；说明既有态势感知对 situation 的定义为什么不适合直接迁移；据此提出 CASA 的定义和研究问题。

### 转场

首先需要把编程智能体使用中分散的判断活动概括为一个准确的态势感知问题。

### 文献依据、内容摘要与本页作用

- **Hong 等（2014），《A Framework and Guidelines for Context-Specific Theorizing in Information Systems Research》，Information Systems Research。** 内容摘要：该文指出情境化理论需要明确新情境改变了哪些实体、属性或关系，不能只宣称研究对象新颖。**本页作用：** 规定问题提出必须同时证明现实重要性和理论内容差异。
- **Chen 等（2024），《Conceptualization and Measurement of Voice-Interaction Usability: The Development of Cooperative Principle Theory for Smart Product Use》，MIS Quarterly。** 内容摘要：该研究逐项比较语音交互与既有可用性情境，论证传统构念内容不足。**本页作用：** 提供本研究从情境差异进入构念开发的论证参照。

---

## 第 8 页　Agentic Delegation Creates a Specific Awareness Problem

### 讲稿

编程智能体让用户可以委托多步骤软件任务，但用户仍然需要在任务过程中判断进展和结果。要作出这些判断，用户不能只看到最终代码，还需要感知智能体采取了什么行动和哪些制品发生了变化，理解测试或运行证据对任务目标意味着什么，并预期当前行动将把任务带向哪里。因此，我们研究的是用户对一个由代理行动生成的软件任务状态所具有的主观态势感知。

### 转场

如果经典态势感知已经定义了同一种 situation，就没有必要发展 CASA；下一步要比较两类态势对象的结构。

### 文献依据、内容摘要与本页作用

- **Kumar 等（2025），《Why AI Agents Still Need You: Findings from Developer-Agent Collaborations in the Wild》，IEEE/ACM International Conference on Automated Software Engineering。** 内容摘要：该研究显示开发者需要在任务中持续理解、调试和测试智能体工作。**本页作用：** 支撑用户需要保持对行动、变化与结果的态势感知，而不只是接收最终输出。
- **Dhanorkar 等（2026），《Human Oversight of Agentic Systems in Practice: Examining the Oversight Work, Challenges, and Heuristics of Developers Using Software Agents》，ACM Conference on Fairness, Accountability, and Transparency。** 内容摘要：该研究揭示多阶段监督以及代码理解与审查困难。**本页作用：** 说明继续、介入和接受判断需要用户保持态势感知。
- **Endsley（2023），《Supporting Human-AI Teams: Transparency, Explainability, and Situation Awareness》，Computers in Human Behavior。** 内容摘要：该文把透明度、解释和态势感知整合到人与人工智能团队研究中，强调用户需要理解人工智能当前与未来行动。**本页作用：** 支撑在自主人工智能交互中研究态势感知具有理论合理性。

---

## 第 9 页　Traditional Situation Awareness Does Not Directly Represent This Task State

### 讲稿

经典态势感知主要研究操作者对外部环境或被控系统状态的感知、理解和预期。编程智能体带来三项结构变化。第一，相关状态随着智能体围绕开放目标选择行动而不断生成。第二，状态分布在计划、行动轨迹、代码、配置、测试和运行证据等载体中。第三，用户没有亲自经历每一步行动，往往需要根据痕迹重建已经发生的过程。因此，变化的不只是对象名称，而是 situation 的生成方式、存在形式和用户接触方式。

### 转场

正因为态势对象发生了这些变化，我们需要在主观态势感知基础上给 CASA 一个明确且具有程度差异的定义。

### 文献依据、内容摘要与本页作用

- **Endsley（1995a），《Measurement of Situation Awareness in Dynamic Systems》，Human Factors；Endsley（1995b），《Toward a Theory of Situation Awareness in Dynamic Systems》，Human Factors。** 内容摘要：两篇经典文献以目标导向任务分析识别操作者需要掌握的环境和系统状态。**本页作用：** 建立经典态势感知通常面对可预先分析状态要求的比较基准。
- **Parasuraman、Sheridan 与 Wickens（2000），《A Model for Types and Levels of Human Interaction with Automation》，IEEE Transactions on Systems, Man, and Cybernetics Part A。** 内容摘要：该文按照信息获取、分析、决策和行动划分自动化类型与水平。**本页作用：** 说明传统自动化通常以可预先分配的人机功能为基础，与开放目标下的代理行动不同。
- **Baird 与 Maruping（2021），《The Next Generation of Research on IS Use: A Theoretical Framework of Delegation to and from Agentic IS Artifacts》，MIS Quarterly。** 内容摘要：该文说明能动型系统可以代表用户发起行动。**本页作用：** 支撑任务状态由代理行动生成以及用户间接接触变化。
- **Kretsou 等（2021），《Change Impact Analysis: A Systematic Mapping Study》，Journal of Systems and Software。** 内容摘要：该综述说明软件变更影响跨文件、依赖关系和系统行为传播。**本页作用：** 支撑编程任务态势分布于多个相互依赖的软件制品。

---

## 第 10 页　CASA Represents Subjective Situation Awareness of an Agent-Generated Task State

### 讲稿

本文将 CASA 定义为：个体用户在一次具体编程智能体任务中，对自己针对智能体代理行动所形成的任务相关状态及其近期发展所具有的主观态势感知程度。这里的态势对象包括智能体行动、软件制品变化、执行证据，以及它们与用户任务目标的关系。高 CASA 意味着用户感觉自己能够感知关键状态、理解其意义并预期近期发展；低 CASA 则意味着其中一个或多个方面难以形成。这个定义明确了个体层次、具体任务、态势对象和程度属性。

### 转场

清楚定义 CASA 是什么之后，还必须说明它与信任、透明度、控制和表现为什么不是同一构念。

### 文献依据、内容摘要与本页作用

- **Taylor（1990），《Situational Awareness Rating Technique: The Development of a Tool for Aircrew Systems Design》，Situational Awareness in Aerospace Operations，NATO AGARD Conference Proceedings No. 478。** 内容摘要：Taylor 从参与者对自身态势感知的评价出发形成主观测量。**本页作用：** 支撑 CASA 是个体对自身态势感知程度的主观判断，而不是客观正确率。
- **Endsley（1995b），《Toward a Theory of Situation Awareness in Dynamic Systems》，Human Factors。** 内容摘要：Endsley 将态势感知分为感知、理解和预期。**本页作用：** 支撑定义中的三个认识方向，但不在构念定义阶段断言它们必然是最终统计维度。
- **Podsakoff、MacKenzie 与 Podsakoff（2016），《Recommendations for Creating Better Concept Definitions in the Organizational, Behavioral, and Social Sciences》，Organizational Research Methods。** 内容摘要：该文要求构念定义明确实体、属性、条件和与相邻概念的区别。**本页作用：** 支撑定义中对用户、任务、态势对象和主观程度的明确限定。

---

## 第 11 页　CASA Is Situation Awareness, Not an Evaluation of the Agent or Interface

### 讲稿

CASA 描述用户对当前智能体任务态势所具有的主观感知、理解和预期。它不评价智能体是否真正完成了任务，也不等于用户是否愿意依赖智能体的信任。透明度描述系统提供了多少行动和过程信息，感知控制描述用户是否感觉能够影响系统，工作负荷描述完成或监控任务所需的认知投入。这些变量可以成为 CASA 的前因、后果或相关变量，但不能被纳入 CASA 的定义。

### 转场

明确边界以后，我们需要回顾态势感知在不同动态任务中如何被情境化，以判断可以继承什么、必须发展什么。

### 文献依据、内容摘要与本页作用

- **Selkowitz、Lakhmani 与 Chen（2017），《Using Agent Transparency to Support Situation Awareness of the Autonomous Squad Member》，Cognitive Systems Research。** 内容摘要：该实验操纵自主智能体提供的行动、理由和未来状态信息，并测量用户态势感知。**本页作用：** 证明透明度是系统信息属性，态势感知是用户形成的认知状态，两者不能等同。
- **van de Merwe、Mallam 与 Nazir（2024），《Agent Transparency, Situation Awareness, Mental Workload, and Operator Performance: A Systematic Literature Review》，Human Factors。** 内容摘要：该综述发现透明度对态势感知、工作负荷和表现的作用并不一致。**本页作用：** 支撑这些变量相关但在概念上独立。
- **Wang 等（2024），《Investigating and Designing for Trust in AI-Powered Code Generation Tools》，ACM Conference on Fairness, Accountability, and Transparency。** 内容摘要：该研究讨论开发者如何评价系统能力和具体代码建议并形成信任。**本页作用：** 说明信任的焦点是依赖判断，不是用户对当前任务态势的感知。
- **Baronas 与 Louis（1988），《Restoring a Sense of Control During Implementation: How User Involvement Leads to System Acceptance》，MIS Quarterly。** 内容摘要：该研究把感知控制视为系统实施过程中的用户体验和接受因素。**本页作用：** 支撑感知控制更适合作为 CASA 的潜在后果。

---

## 第 12 页　Situation Awareness Has Been Contextualized Across Dynamic Tasks

### 讲稿

态势感知并不只适用于航空。Taylor 从空勤人员的主观评价发展 SART；Endsley 从动态决策任务发展感知、理解和预期理论以及 SAGAT；列车驾驶、信息安全和分析仪表盘研究又分别围绕各自的态势对象进行情境化。这些研究共同说明，situation awareness 可以跨情境，但 situation 的具体内容必须与用户目标、任务和系统一致。

### 转场

因此，接下来的问题不是能否使用态势感知，而是既有构念究竟把什么定义为 situation，以及这种定义是否覆盖编程智能体。

### 文献依据、内容摘要与本页作用

- **Taylor（1990），《Situational Awareness Rating Technique: The Development of a Tool for Aircrew Systems Design》，Situational Awareness in Aerospace Operations，NATO AGARD Conference Proceedings No. 478。** 内容摘要：该研究从空勤人员对高低态势感知情境的比较中引出主观评价内容。**本页作用：** 展示主观态势感知如何与具体任务结合。
- **Endsley（1995a），《Measurement of Situation Awareness in Dynamic Systems》，Human Factors；Endsley（1995b），《Toward a Theory of Situation Awareness in Dynamic Systems》，Human Factors。** 内容摘要：两文通过任务目标识别相关状态，并区分感知、理解和预期。**本页作用：** 展示动态态势感知理论传统。
- **Rose、Bearman 与 Dorrian（2018），《The Low-Event Task Subjective Situation Awareness Technique: Development and Evaluation of a New Subjective Measure of Situation Awareness》，Applied Ergonomics。** 该文开发了 Low-Event Task Subjective Situation Awareness Technique，即低事件任务主观态势感知技术，简称 LETSSA。研究者认为通用 SART 不能充分反映长时间低事件列车驾驶，因而围绕列车位置、速度、信号、操作约束和未来事件重新界定测量内容。**本页作用：** 提供任务结构变化要求重新界定态势感知内容的直接先例。
- **Jaeger 与 Eckhardt（2021），《Eyes Wide Open: The Role of Situational Information Security Awareness for Security-Related Behaviour》，Information Systems Journal。** 内容摘要：该研究把态势感知情境化为个体对网络钓鱼威胁的注意、解释和风险认识。**本页作用：** 证明个体态势感知能够在信息系统研究中形成情境特定内容。
- **Nadj、Maedche 与 Schieder（2020），《The Effect of Interactive Analytical Dashboard Features on Situation Awareness and Task Performance》，Decision Support Systems。** 内容摘要：该研究在运营决策支持情境中分别测量态势感知和任务表现。**本页作用：** 证明同一理论在不同任务中需要围绕不同状态内容展开。

---

## 第 13 页　Existing Situation-Awareness Conceptualizations Define a Different Situation

### 讲稿

这一页的重点不是现有量表题项写得不够像编程，而是既有构念对 situation 的定义与编程智能体不同。SART 传统把态势感知表述为对航空任务动态性、信息条件、注意资源和理解的综合主观评价，其中部分内容其实描述任务条件和个体资源。Endsley 传统围绕由目标导向任务分析预先识别的环境与系统要素定义态势感知。自主智能体透明度研究进一步加入行动、理由和未来状态，但仍然假定一个预定义任务环境。CASA 面对的 situation 则由代理行动持续生成，并分布在可执行软件制品和运行证据之间。因此，理论缺口首先存在于构念内容，而不是测量措辞。

### 转场

当既有构念没有把这种态势对象概念化时，CASA 的价值就在于使一个重要的代理式用户状态在理论上可见。

### 文献依据、内容摘要与本页作用

- **Taylor（1990），《Situational Awareness Rating Technique: The Development of a Tool for Aircrew Systems Design》，Situational Awareness in Aerospace Operations，NATO AGARD Conference Proceedings No. 478。** 内容摘要：SART 的内容包括不稳定性、复杂性、变量数量、信息质量、注意需求、注意供给和理解。**本页作用：** 说明 SART 对态势感知的概念化混合了航空任务条件、认知资源和理解评价。
- **Endsley（1995a），《Measurement of Situation Awareness in Dynamic Systems》，Human Factors；Endsley（1995b），《Toward a Theory of Situation Awareness in Dynamic Systems》，Human Factors。** 内容摘要：Endsley 以目标导向任务分析确定需要感知、理解和预期的状态要素。**本页作用：** 说明经典理论通常假定相关状态要求可以预先分析。
- **Selkowitz、Lakhmani 与 Chen（2017），《Using Agent Transparency to Support Situation Awareness of the Autonomous Squad Member》，Cognitive Systems Research。** 内容摘要：该研究把自主智能体当前行动、理由和未来状态纳入态势感知支持。**本页作用：** 提供最接近 CASA 的概念化，同时暴露其未处理软件制品关系和运行证据的边界。
- **van de Merwe、Mallam 与 Nazir（2024），《Agent Transparency, Situation Awareness, Mental Workload, and Operator Performance: A Systematic Literature Review》，Human Factors。** 内容摘要：该综述显示自主智能体态势感知研究主要围绕预定义操作环境展开。**本页作用：** 支撑 CASA 的理论缺口不是简单缺少一套编程措辞量表。

---

## 第 14 页　CASA Makes an Important Agentic User State Visible

### 讲稿

CASA 的第一项价值是把分散的现象整合为一个态势感知构念。智能体行动、软件制品变化、执行证据和近期发展不再被分别归入监督、验证或界面问题，而被理解为用户所面对的同一任务态势。第二项价值是解释用户为什么能够或不能够作出继续、介入和接受判断。第三项价值是形成精确的设计问题：用户究竟无法感知关键变化、无法理解变化意义，还是无法预期下一步发展。这样的区分比笼统讨论透明度或可用性更能指导编程智能体界面设计。

### 转场

基于现实重要性、构念内容缺口和理论价值，研究问题可以收敛为构念维度与相对解释价值两个方面。

### 文献依据、内容摘要与本页作用

- **Hong 等（2014），《A Framework and Guidelines for Context-Specific Theorizing in Information Systems Research》，Information Systems Research。** 内容摘要：该文认为情境化理论只有在新情境揭示一般构念未表达的内容、关系或边界时才有理论价值。**本页作用：** 支撑 CASA 的价值必须来自代理式任务态势内容，而不是名称新颖。
- **Endsley（2023），《Supporting Human-AI Teams: Transparency, Explainability, and Situation Awareness》，Computers in Human Behavior。** 内容摘要：该文把态势感知视为人与自主人工智能有效互动的重要认知条件。**本页作用：** 支撑 CASA 可以解释用户如何依据态势感知作出后续判断。
- **Nadj、Maedche 与 Schieder（2020），《The Effect of Interactive Analytical Dashboard Features on Situation Awareness and Task Performance》，Decision Support Systems。** 内容摘要：what-if analysis 同时提高任务表现并降低态势感知，显示系统功能和用户态势感知可能分离。**本页作用：** 支撑把 CASA 单独概念化具有解释价值。
- **Chen 等（2024），《Conceptualization and Measurement of Voice-Interaction Usability: The Development of Cooperative Principle Theory for Smart Product Use》，MIS Quarterly。** 内容摘要：该文把语音交互中的分散用户评价整合为多维情境构念，并形成针对具体设计属性的解释。**本页作用：** 提供从情境构念内容连接理论解释与设计诊断的参照。

---

## 第 15 页　Research Questions

### 讲稿

第一个研究问题关注 CASA 包含哪些维度，以及这些维度如何被测量。第二个问题关注开发 CASA 是否真的增加理论解释：与一般主观态势感知相比，CASA 能否对感知控制、满意度和持续使用意愿提供额外解释和预测。这里先提出问题，不提前承诺研究设计、贡献类型或具体结果。

### 转场

要回答第一个问题，下一部分首先明确基础构念、组织理论和代理式情境之间的分工。

### 文献依据、内容摘要与本页作用

- **Hong 等（2014），《A Framework and Guidelines for Context-Specific Theorizing in Information Systems Research》，Information Systems Research。** 内容摘要：该文要求情境化理论明确相对于一般理论增加了什么。**本页作用：** 支撑第二个研究问题需要比较 CASA 与一般主观态势感知的增量价值。
- **Chen 等（2024），《Conceptualization and Measurement of Voice-Interaction Usability: The Development of Cooperative Principle Theory for Smart Product Use》，MIS Quarterly。** 内容摘要：该研究提出两个高度聚焦的问题，分别关注情境构念维度与相对预测能力。**本页作用：** 为 CASA 研究问题的数量与功能分工提供顶级期刊范例。

---

## 第 16 页　2. Theoretical Background

### 讲稿

理论背景回答三个问题：CASA 从哪个已有构念出发，哪套理论负责组织构念内容，以及编程智能体情境为什么要求发展这些内容。这里始终以个体层主观态势感知为唯一基础构念，以 Endsley 的动态态势感知理论指导高阶候选维度，并以信息系统委托理论界定代理式任务情境。

### 转场

首先澄清 Taylor 和 Endsley 在研究中不是相互竞争，而是分别解决测量属性和内容结构问题。

### 文献依据、内容摘要与本页作用

- **Taylor（1990），《Situational Awareness Rating Technique: The Development of a Tool for Aircrew Systems Design》，Situational Awareness in Aerospace Operations，NATO AGARD Conference Proceedings No. 478。** 内容摘要：提供主观态势感知传统。**本页作用：** 确定 CASA 的基础构念与主观属性。
- **Endsley（1995b），《Toward a Theory of Situation Awareness in Dynamic Systems》，Human Factors。** 内容摘要：提供感知、理解和预期三个层级。**本页作用：** 指导 CASA 的高阶候选维度。
- **Baird 与 Maruping（2021），《The Next Generation of Research on IS Use: A Theoretical Framework of Delegation to and from Agentic IS Artifacts》，MIS Quarterly。** 内容摘要：提供向能动型信息系统委托任务的理论。**本页作用：** 界定 CASA 发生的代理式信息系统情境。

---

## 第 17 页　Taylor and Endsley Serve Different Roles in the CASA Project

### 讲稿

Taylor 的传统决定 CASA 测量的是个体对自身态势掌握程度的主观评价。Endsley 的理论则把态势感知内容组织为感知相关要素、理解要素意义和预期近期发展，并把界面、经验和工作负荷定位为形成这种体验的条件。两者结合后，CASA 聚焦用户对代理生成任务态势的感知、理解与预期，而透明度、感知控制和工作负荷分别进入其前因或后果网络。

### 转场

这种分工是否合理，还要看态势感知在不同任务中的迁移方式及其边界。

### 文献依据、内容摘要与本页作用

- **Taylor（1990），《Situational Awareness Rating Technique: The Development of a Tool for Aircrew Systems Design》，Situational Awareness in Aerospace Operations，NATO AGARD Conference Proceedings No. 478。** 内容摘要：SART 通过参与者对自身态势感知的评价形成主观测量。**本页作用：** 确定 CASA 是主观态势感知。
- **Endsley（1995b），《Toward a Theory of Situation Awareness in Dynamic Systems》，Human Factors。** 内容摘要：该理论区分态势感知内容、影响因素与决策表现。**本页作用：** 指导 CASA 的内容结构和法则边界。
- **Endsley、Selcon、Hardiman 与 Croft（1998），《A Comparative Analysis of SAGAT and SART for Evaluations of Situation Awareness》，Human Factors and Ergonomics Society Annual Meeting。** 内容摘要：该研究显示 SART 稳定关联操作者的主观态势感知、充分性感受、信心和主观绩效评价。**本页作用：** 支撑 CASA 作为用户对自身任务认识状态的主观评价构念。

---

## 第 18 页　Existing Situation-Awareness Research Establishes Transferability and Limits

### 讲稿

这一页不只是罗列态势感知被用于哪些领域，而是比较不同研究如何界定构念中的 situation。五篇论文的共同基础仍然是个体对动态情境的感知、理解与预期，但它们认识的对象不同。自动化研究关注系统状态以及失效后的接管，自主智能体研究关注智能体的行动、理由和未来状态，运营仪表盘研究关注决策者当前知识状态的完整性与准确性，信息安全研究关注特定威胁线索形成的安全知识。由此可见，态势感知的一般认知逻辑具有可迁移性，但构念内容必须由具体情境中的相关状态决定。现有研究尚未覆盖编程智能体通过工具调用、跨文件修改和运行反馈持续生成的软件任务状态，这正是 CASA 需要发展的内容。

答辩时要避免说这五篇论文都提出了新的态势感知定义。Endsley 与 Kiris、Selkowitz 以及 Endsley 主要沿用经典三层定义并改变应用对象；Nadj 等明确把态势感知表述为当前知识状态的质量；Jaeger 与 Eckhardt 则真正提出了信息安全情境下的特定构念定义。这种差别也说明，CASA 不能仅把 coding agent 填入旧量表，而要说明编程智能体情境中的 situation 由哪些状态内容构成。

### 转场

除相邻领域外，还需要检查人工智能辅助编程研究已经观察到哪些与 CASA 接近的经验现象。

### 文献依据、内容摘要与本页作用

- **Endsley 与 Kiris（1995），《The Out-of-the-Loop Performance Problem and Level of Control in Automation》，Human Factors。** **英文原文：** “the perception of elements in the environment ... the comprehension of their meaning, and the projection of their status in the near future.” **中文翻译：** 态势感知是对环境要素的感知、对这些要素意义的理解，以及对其近期状态的预期。**定义判断：** 该文直接沿用 Endsley（1988）的经典定义，并把三个层级具体化为对相关系统状态变量的感知、结合操作者目标理解系统状态的意义，以及预期系统未来趋势。它没有创造新的自动化态势感知构念。**内容摘要：** 研究比较不同自动化控制水平，发现自动化使用户由主动处理转为被动监视时，态势感知会下降，并延缓系统失效后的人工决策。**本页作用：** 证明系统替用户承担行动可能削弱用户的态势感知，且这种损失会在需要介入时产生实际后果。
- **Selkowitz、Lakhmani 与 Chen（2017），《Using Agent Transparency to Support Situation Awareness of the Autonomous Squad Member》，Cognitive Systems Research。** **英文原文：** “perception of the basic elements ... comprehension of the elements' meaning ... projection of their status in the near future.” **中文翻译：** 态势感知包括感知基本要素、理解这些要素的意义，以及预期它们近期的状态。**定义判断：** 该文明确说明采用 Endsley（1995）的定义，理论上没有重定义态势感知；它的贡献是把三个层级的认识对象转向自主机器人。第一层信息包括机器人当前行动、计划及其对环境的感知，第二层包括其行动理由，第三层包括未来状态与不确定性。**内容摘要：** 实验比较四种智能体透明度界面，较高的 SAT 信息层级提高了用户对机器人的态势感知、信任和认知加工，同时没有显著增加主观工作负荷。**本页作用：** 证明经典态势感知能够迁移到自主智能体，但也显示迁移的关键在于重新确定每个层级所指向的智能体状态内容。
- **Endsley（2023），《Supporting Human-AI Teams: Transparency, Explainability, and Situation Awareness》，Computers in Human Behavior。** **英文原文：** “a constantly updated state of knowledge about what is happening in a dynamically changing world.” **中文翻译：** 态势感知是一种持续更新的知识状态，反映个体对动态变化世界中正在发生之事的认识。**定义判断：** 该文仍以经典三层定义为基础，没有提出与经典态势感知相独立的新构念；其理论扩展在于区分人与人工智能团队所需的任务工作态势感知、智能体态势感知和团队工作态势感知。**内容摘要：** 该文论证人工智能透明度主要为用户提供当前和前瞻性状态信息，解释则更多帮助形成较稳定的心理模型；有效监督、介入、协调和信任校准都依赖相关态势感知。**本页作用：** 支撑在自主人工智能交互中研究态势感知的必要性，同时提醒 CASA 必须明确用户需要认识的是软件任务、智能体及其协作关系中的哪些状态。
- **Nadj、Maedche 与 Schieder（2020），《The Effect of Interactive Analytical Dashboard Features on Situation Awareness and Task Performance》，Decision Support Systems。** **英文原文：** “a quality criterion in terms of completeness and accuracy of the current state of knowledge.” **中文翻译：** 态势感知是关于当前知识状态之完整性与准确性的质量标准。**定义判断：** 该文采用 Endsley 模型，但把态势感知进一步表述为有高低程度的知识状态质量，因此可以和任务表现分开检验。**内容摘要：** 83 人实验显示，同一种 what-if analysis 功能提高了任务表现，却降低了 SAGAT 所测得的态势感知。原因不是任务表现同时升降，而是参与者可以借助系统得到较好决策结果，同时较少掌握当前生产计划状态，由此出现脱离回路风险。**本页作用：** 证明态势感知不是系统输出质量或任务表现的替代说法，也为把 CASA 表述为具有程度差异的用户认知状态提供依据。
- **Jaeger 与 Eckhardt（2021），《Eyes Wide Open: The Role of Situational Information Security Awareness for Security-Related Behaviour》，Information Systems Journal。** **英文原文：** “a user's knowledge of particular security threats transported by security-related information cues captured in a situational process in the immediate system environment.” **中文翻译：** 情境性信息安全态势感知是用户在即时系统环境的情境过程中，通过捕捉安全相关信息线索而形成的关于特定安全威胁的知识。**定义判断：** 与前三类研究不同，该文明确发展了一个情境特定的个体层构念。它没有把一般安全意识直接搬入网络钓鱼情境，而是把构念限定为用户在具体交互过程中由即时线索形成的特定威胁知识。**内容摘要：** 研究使用眼动、实验和问卷分析 107 名员工。既往钓鱼经验和安全警告提高该态势感知，邮件的情境相关性和错置显著性降低该态势感知；该态势感知继而提高威胁评价、应对效能评价和实际安全行为。**本页作用：** 这是 CASA 最接近的信息系统先例，证明可以从一般态势感知出发，围绕一种新的信息系统情境重新定义用户需要形成的具体知识内容及其前因后果。

**原文核对说明：** Endsley 与 Kiris、Selkowitz、Endsley（2023）和 Nadj 等的定义均已由论文原文或出版社全文页面核对。Jaeger 与 Eckhardt 的定义由该文原文定义被 Ofte 与 Katsikas（2023）逐字转引的版本核对；当前本地尚未取得其 Wiley 正文，因此答辩时宜把这一定义称为经后续同行评议综述逐字转引核对，而不要声称已保存出版社 PDF。

---

## 第 19 页　AI-Assisted Programming Research Reveals Pieces of the CASA Phenomenon

### 讲稿

现有人工智能辅助编程研究已经触及 CASA 的不同部分。Barke 等研究互动模式和代码检查；Mozannar 等刻画阅读、验证和编辑活动；Ferdowsi 等说明运行时证据改变代码理解条件；Wang 等研究信任评价；Kumar 等和 Dhanorkar 等研究持续协作与监督。这些研究都涉及用户如何获得或失去态势感知，但分别以互动、成本、验证、信任、协作或监督为中心，尚未把感知、理解和预期整个代理式任务态势概念化为共同构念。

### 转场

因此，问题不是没有相关研究，而是现有证据仍然碎片化，由此形成覆盖、精度和构念验证三个缺口。

### 文献依据、内容摘要与本页作用

- **Barke、James 与 Polikarpova（2023），《Grounded Copilot: How Programmers Interact with Code-Generating Models》，Proceedings of the ACM on Programming Languages，OOPSLA。** 内容摘要：识别加速和探索两种互动模式，以及意图表达、代码检查与模式切换。**本页作用：** 说明用户对代码与目标的理解已被观察，但未上升为完整态势感知构念。
- **Mozannar、Bansal、Fourney 与 Horvitz（2024），《Reading Between the Lines: Modeling User Behavior and Costs in AI-Assisted Programming》，ACM Conference on Human Factors in Computing Systems。** 内容摘要：对阅读、验证、编辑、提示和等待活动进行行为序列与时间成本建模。**本页作用：** 说明活动成本研究不等于态势感知研究。
- **Ferdowsi、Huang、James、Polikarpova 与 Lerner（2024），《Validating AI-Generated Code with Live Programming》，ACM Conference on Human Factors in Computing Systems。** 内容摘要：持续呈现运行时值改变用户检查和理解生成代码的条件。**本页作用：** 为执行证据可能影响 CASA 提供直接设计依据。
- **Wang、Cheng、Ford 与 Zimmermann（2024），《Investigating and Designing for Trust in AI-Powered Code Generation Tools》，ACM Conference on Fairness, Accountability, and Transparency。** 内容摘要：研究开发者如何评价系统能力和具体建议并形成信任。**本页作用：** 说明信任研究触及评价活动，但不等于态势感知。
- **Kumar 等（2025），《Why AI Agents Still Need You: Findings from Developer-Agent Collaborations in the Wild》，IEEE/ACM International Conference on Automated Software Engineering。** 内容摘要：观察真实软件问题中的渐进互动、调试和测试。**本页作用：** 支撑 CASA 涉及持续代理任务而非单项建议。
- **Dhanorkar 等（2026），《Human Oversight of Agentic Systems in Practice: Examining the Oversight Work, Challenges, and Heuristics of Developers Using Software Agents》，ACM Conference on Fairness, Accountability, and Transparency。** 内容摘要：揭示多阶段监督与代码审查困难。**本页作用：** 支撑智能体行动、制品变化和执行证据需要被整合为态势感知。

---

## 第 20 页　The Literature Leaves Three Interlocking Gaps

### 讲稿

第一个缺口是构念覆盖不足，没有一个概念同时表示用户对智能体行动、软件制品变化、执行证据和近期发展的态势感知。第二个缺口是概念精度不足，信任、透明度、验证成本和一般理解分别描述其他属性。第三个缺口是现有研究尚未形成经过系统验证的 CASA 构念结构。结果是，我们无法比较不同产品和用户的 CASA，也无法检验设计条件是否通过 CASA 影响后续体验。

### 转场

填补这些缺口需要一个能够组织态势感知内容、同时保持前因和结果边界的理论框架。

### 文献依据、内容摘要与本页作用

- **Barke 等（2023），《Grounded Copilot: How Programmers Interact with Code-Generating Models》，Proceedings of the ACM on Programming Languages，OOPSLA；Mozannar 等（2024），《Reading Between the Lines: Modeling User Behavior and Costs in AI-Assisted Programming》，ACM Conference on Human Factors in Computing Systems；Ferdowsi 等（2024），《Validating AI-Generated Code with Live Programming》，ACM Conference on Human Factors in Computing Systems；Wang 等（2024），《Investigating and Designing for Trust in AI-Powered Code Generation Tools》，ACM Conference on Fairness, Accountability, and Transparency；Kumar 等（2025），《Why AI Agents Still Need You》，IEEE/ACM International Conference on Automated Software Engineering；Dhanorkar 等（2026），《Human Oversight of Agentic Systems in Practice》，ACM Conference on Fairness, Accountability, and Transparency。** 内容摘要：这些研究分别覆盖互动、成本、验证、信任、协作和监督。**本页作用：** 共同证明相关现象已经出现，但缺乏统一态势感知构念。
- **Hong 等（2014），《A Framework and Guidelines for Context-Specific Theorizing in Information Systems Research》，Information Systems Research。** 内容摘要：该文要求情境化理论明确基础构念的内容遗漏。**本页作用：** 把碎片化、概念精度和结构缺失组织为可以支持 CASA 开发的理论缺口。

---

## 第 21 页　Dynamic Situation Awareness Organizes What the User Comes to Know

### 讲稿

Endsley 将动态态势感知分为三个递进层级。第一层是感知，即察觉与当前目标有关的要素、属性和变化。第二层是理解，即把不同要素整合起来，并结合目标和已有知识解释意义。第三层是预期，即根据当前状态和变化趋势判断近期会如何发展。这三个层级描述态势感知本身；界面、工作负荷、经验和任务复杂性是影响条件，决策和表现则是后果。

### 转场

动态态势感知解释一般认知结构，但还需要说明为什么这种结构发生在不同于传统工具使用的代理关系中。

### 文献依据、内容摘要与本页作用

- **Endsley（1995b），《Toward a Theory of Situation Awareness in Dynamic Systems》，Human Factors。** 内容摘要：提出感知、理解和预期三个层级，并区分个体因素、任务条件、系统设计、态势感知与决策表现。**本页作用：** 是本页理论结构的直接来源。
- **Endsley（1995a），《Measurement of Situation Awareness in Dynamic Systems》，Human Factors。** 内容摘要：说明不同任务需要依据目标识别具体状态要求。**本页作用：** 支撑三个层级是一般结构，具体内容必须依据编程智能体情境发展。

---

## 第 22 页　Delegation Theory Specifies Why This Awareness Occurs in an Agentic IS Context

### 讲稿

动态态势感知解释用户如何感知、理解和预期变化中的态势。Baird 和 Maruping 的委托理论解释这种态势为什么由系统行动形成。能动型信息系统能够接受任务并发起行动，因此用户面对的不再是被动工具，而是代表自己推进任务的代理。两者结合以后，CASA 的理论位置是：用户向能动型信息系统委托软件任务时，对代理行动所形成任务状态的主观态势感知。

### 转场

在这一理论桥梁上，可以进一步把 Endsley 的一般层级转化为 CASA 的高阶候选维度。

### 文献依据、内容摘要与本页作用

- **Endsley（1995b），《Toward a Theory of Situation Awareness in Dynamic Systems》，Human Factors。** 内容摘要：提供动态任务中感知、理解和预期的一般认知结构。**本页作用：** 解释 CASA 的 situation awareness 部分。
- **Baird 与 Maruping（2021），《The Next Generation of Research on IS Use: A Theoretical Framework of Delegation to and from Agentic IS Artifacts》，MIS Quarterly。** 内容摘要：提出用户向能动型信息系统委托任务的理论框架。**本页作用：** 解释 CASA 中任务状态为什么由代理行动形成。

---

## 第 23 页　Dynamic Situation Awareness Guides Three Candidate CASA Dimensions

### 讲稿

这一页对应 Chen 等文章中 Cooperative Principle Theory，即合作原则理论，简称 CPT，所发挥的理论作用，也得到 Zhou 等发表于 *Journal of Management Information Systems*，即《管理信息系统杂志》、简称 JMIS 的文章补充支持。Chen 等先从用户评论编码得到 13 个一阶范畴，再用合作原则理论把这些范畴组织为高阶维度，同时允许数据增加原理论没有的拟人化维度。Zhou 等研究元宇宙游戏经验价值时，则以经验价值自身的经典框架作为理论组织基础。研究者先从在线评论中归纳 21 个子维度和 6 个具体维度，再把这些经验维度映射到经验价值理论的内在/外在和主动/反应两条轴上。两篇文章共同说明，基础构念的理论结构可以指导高阶组织，但不应预先替代二手数据中的内容发现。

对 CASA 而言，Endsley 的三个层级可以据此指导三个高阶候选维度。第一是对代理生成状态的感知，包括关键行动、制品变化和执行证据。第二是对任务意义的理解，即把痕迹、制品关系和证据整合到任务目标、依赖和未解决问题中。第三是对近期发展的预期，包括智能体下一步行动、当前变化的后果和新风险。这里称为候选维度，是因为 Reddit 数据仍需判断它们是可区分维度、递进层级，还是需要被修正的结构。Endsley 理论负责提出有依据的初始组织方式，Reddit 编码负责决定编程智能体态势感知的具体内涵和最终结构。

### 转场

理论维度明确以后，后面只需简要交代如何使用 Reddit 编码发展具体内容，并继续开发量表。

### 文献依据、内容摘要与本页作用

- **Endsley（1995b），《Toward a Theory of Situation Awareness in Dynamic Systems》，Human Factors。** 内容摘要：提出感知、理解和预期三个递进层级。**本页作用：** 为 CASA 提供三个高阶候选维度的理论来源。
- **Baird 与 Maruping（2021），《The Next Generation of Research on IS Use: A Theoretical Framework of Delegation to and from Agentic IS Artifacts》，MIS Quarterly。** 内容摘要：说明代理能够代表用户发起行动。**本页作用：** 把三个一般层级具体化为对代理行动所生成软件状态的感知、理解和预期。
- **Chen 等（2024），《Conceptualization and Measurement of Voice-Interaction Usability: The Development of Cooperative Principle Theory for Smart Product Use》，MIS Quarterly。** 内容摘要：该研究先编码 30,834 条用户评论得到 13 个轴向范畴，再用合作原则理论把它们归纳为数量、质量、关系和方式等高阶维度，并根据数据增加拟人化维度。**本页作用：** 提供理论组织高阶维度、二手数据形成具体内容并反向修正理论的直接方法论参照。
- **Zhou、Chen、Li、Zhang 与 Jin（2025），《Demystifying the Dimensions and Roles of Metaverse Gaming Experience Value: A Multi-Study Investigation》，Journal of Management Information Systems。** 内容摘要：该研究从在线评论开放编码得到 21 个子维度，通过轴向编码形成 6 个元宇宙游戏经验价值维度，再与经验价值理论中的内在/外在和主动/反应框架往返对照，形成情境特定类型学。**本页作用：** 进一步证明基础构念自身的成熟理论结构可以指导高阶维度组织，而二手用户文本负责发现情境特定的具体内容并检验既有结构是否充分。

---

## 第 24 页　3. Research Design

### 讲稿

研究设计只保留两项核心工作。第一阶段基于 Reddit 中真实编程智能体使用叙述，通过编码识别 CASA 候选维度的具体内容与边界。第二阶段把构念内容转化为量表题项，并使用独立样本检验结构、效度和相对于一般主观态势感知的增量价值。方法部分服务于前面的理论问题，因此这里不展开所有操作细节。

### 转场

下一页简要说明 Reddit 数据如何进入构念开发。

### 文献依据、内容摘要与本页作用

- **Venkatesh、Brown 与 Bala（2013），《Bridging the Qualitative-Quantitative Divide: Guidelines for Conducting Mixed Methods Research in Information Systems》，MIS Quarterly。** 内容摘要：该文强调定性理论形成与定量理论检验应围绕同一研究目的整合。**本页作用：** 支撑从构念内容发现到量表验证的顺序设计。
- **Chen 等（2024），《Conceptualization and Measurement of Voice-Interaction Usability: The Development of Cooperative Principle Theory for Smart Product Use》，MIS Quarterly。** 内容摘要：该研究先从二手用户评论发展构念维度，再开展量表验证。**本页作用：** 提供本研究两阶段结构的直接对标。

---

## 第 25 页　Stage 1 Develops the CASA Construct from Coding-Agent Use Narratives

### 讲稿

第一阶段收集 Reddit 中围绕具体编程智能体任务的公开叙述，要求材料涉及智能体行动、软件变化、执行证据或态势感知的形成与中断。研究者先开放编码，尽量保留用户语言，再通过轴向编码形成具体内容。之后用 Endsley 的三个候选维度组织和比较范畴，并使用负例区分 CASA 与信任、透明度、工作负荷和控制。Reddit 用于发现内容，不用于估计问题发生率。

### 转场

构念内容和维度稳定以后，第二阶段才把 CASA 转化为可以跨用户和产品比较的量表。

### 文献依据、内容摘要与本页作用

- **Corbin 与 Strauss（1990），《Grounded Theory Research: Procedures, Canons, and Evaluative Criteria》，Qualitative Sociology。** 内容摘要：提供开放编码、轴向编码和持续比较程序。**本页作用：** 支撑从 Reddit 用户语言形成经验范畴。
- **Gioia、Corley 与 Hamilton（2013），《Seeking Qualitative Rigor in Inductive Research: Notes on the Gioia Methodology》，Organizational Research Methods。** 内容摘要：强调保留从一阶用户语言到二阶主题和聚合维度的数据结构。**本页作用：** 支撑经验材料与构念主张之间的可审计联系。
- **Chen 等（2024），《Conceptualization and Measurement of Voice-Interaction Usability: The Development of Cooperative Principle Theory for Smart Product Use》，MIS Quarterly。** 内容摘要：使用大规模二手评论进行开放和轴向编码，再以理论组织高阶维度。**本页作用：** 提供使用二手用户文本发展情境构念的直接先例。
- **Franzke 等（2020），《Internet Research: Ethical Guidelines 3.0》，Association of Internet Researchers；Gliniecka（2023），《The Ethics of Publicly Available Data Research: A Situated Ethics Framework for Reddit》，Social Media + Society。** 内容摘要：两者强调公开网络数据仍需考虑情境期望、去标识化和反向搜索风险。**本页作用：** 支撑 Reddit 数据使用的伦理边界。

---

## 第 26 页　Stage 2 Develops and Tests a CASA Scale

### 讲稿

第二阶段根据构念定义、定性范畴和用户语言生成题项，并通过专家评审、认知访谈、语义审计和卡片分类检查内容。随后使用独立样本进行探索性和验证性分析，检验信度、收敛效度、区分效度和跨群体稳定性。最后比较 CASA 与一般主观态势感知对感知控制、满意度和持续使用的解释与预测能力。如果 CASA 没有稳定的编程智能体特定内容或没有增量价值，研究应定位为量表适配，而不能坚持新构念主张。

### 转场

由此可以回到整场汇报最核心、同时也是有条件成立的理论判断。

### 文献依据、内容摘要与本页作用

- **Moore 与 Benbasat（1991），《Development of an Instrument to Measure the Perceptions of Adopting an Information Technology Innovation》，Information Systems Research。** 内容摘要：使用题项生成、专家评审和分类程序开发信息技术创新感知量表。**本页作用：** 支撑初始题项和内容分类程序。
- **MacKenzie、Podsakoff 与 Podsakoff（2011），《Construct Measurement and Validation Procedures in MIS and Behavioral Research: Integrating New and Existing Techniques》，MIS Quarterly。** 内容摘要：整合内容效度、测量模型、区分效度和法则效度程序。**本页作用：** 规定 CASA 量表成立所需的完整证据。
- **Larsen 等（2026），《The ITEM Ontology: A Tool to Elucidate the Anatomy of Psychometric Indicators》，Information Systems Research。** ITEM 是 Indicator Terminology for Explanation and Measurement，即用于解释与测量的指标术语体系。该文把题项分解为对象、被测属性、限定条件和反应集合等语义组成。**本页作用：** 支撑 CASA 题项的语义审计。
- **Pillet 等（2026），《AI-Augmented Content Validation in Behavioral Research: Development and Evaluation of the RATER System》，MIS Quarterly。** RATER 是该文开发的人工智能增强内容效度评估系统名称。首次介绍时应把它理解为一套由人工智能辅助、但仍由研究者承担最终判断的题项评估系统，而不是传统量表缩写。**本页作用：** 支撑人工智能可辅助题项诊断但不能替代专家判断。

---

## 第 27 页　The Central Claim

### 讲稿

本研究的核心主张是，编程智能体创造了一种不同的态势感知对象。它由委托行动生成，跨可执行软件制品和执行证据分布，并且部分通过行动痕迹而非直接操作被用户感知、理解和预期。CASA 是否值得作为新构念开发，最终取决于 Reddit 材料和后续量表研究能否证明这种 situation 需要超出一般主观态势感知的内容与解释。我们的目标不是因为情境新就创造概念，而是检验既有构念对 situation 的定义是否确实遗漏了编程智能体代理行动形成的关键状态。

### 文献依据、内容摘要与本页作用

- **Taylor（1990），《Situational Awareness Rating Technique: The Development of a Tool for Aircrew Systems Design》，Situational Awareness in Aerospace Operations，NATO AGARD Conference Proceedings No. 478。** 内容摘要：提供主观态势感知基础。**本页作用：** 规定 CASA 仍然是 situation awareness，而不是另造近义概念。
- **Endsley（1995b），《Toward a Theory of Situation Awareness in Dynamic Systems》，Human Factors。** 内容摘要：提供感知、理解和预期层级。**本页作用：** 规定 CASA 的理论维度来源。
- **Baird 与 Maruping（2021），《The Next Generation of Research on IS Use: A Theoretical Framework of Delegation to and from Agentic IS Artifacts》，MIS Quarterly。** 内容摘要：提供能动型信息系统任务委托理论。**本页作用：** 支撑态势由代理行动生成和用户间接接触的独特关系。
- **Hong 等（2014），《A Framework and Guidelines for Context-Specific Theorizing in Information Systems Research》，Information Systems Research。** 内容摘要：要求情境化理论证明实际内容或关系增量。**本页作用：** 规定最终结论有条件成立，必须接受经验检验。

---

## 第 28 页　References 1

### 讲稿

本页及后续八页为参考文献备查，正式汇报在第 27 页结束。本页主要包括信息系统委托、人工智能编程互动、控制感、持续使用、主观态势感知和构念开发研究。

### 文献说明

本页不提出新的理论主张；页面文献的题名、出处、内容摘要和具体作用已经在对应主讲页中逐项说明。

---

## 第 29 页　References 2

### 讲稿

本页集中列出自动化监督、动态态势感知及人与人工智能研究。若被追问脱离回路、SAGAT、经典三层模型或人工智能团队中的态势感知，可以返回本页。

### 文献说明

对应文献的详细摘要和作用见第 6、12、16-18、21 和 23 页讲稿。

---

## 第 30 页　References 3

### 讲稿

本页主要包括人工智能代码验证、网络研究伦理、定性编码、量表开发、移动应用可用性和情境化理论研究。若被追问 Reddit 伦理、Gioia 数据结构、量表程序或情境化理论，可以返回本页。

### 文献说明

对应文献的详细摘要和作用见第 9、12-15、19、24-26 页讲稿。

---

## 第 31 页　References 4

### 讲稿

本页主要包括信息安全态势感知、构念指标、软件变更影响、编程智能体研究、多维构念和 MIS 构念验证。若被追问 CASA 的情境迁移、软件制品关系或测量模型，可以返回本页。

### 文献说明

对应文献的详细摘要和作用见第 9、12-15、18-20 和 26 页讲稿。

---

## 第 32 页　References 5

### 讲稿

本页主要包括商业价值、量表开发、人工智能编程行为、运营仪表盘、自动化和形成式构念研究。若被追问 Nadj 等研究结果、编程活动成本或后续量表程序，可以返回本页。

### 文献说明

对应文献的详细摘要和作用见第 2、6、9、12、14、19 和 26 页讲稿。

---

## 第 33 页　References 6

### 讲稿

本页主要包括内容效度、共同方法偏差、构念定义和 LETSSA 研究。正式汇报无须逐条讲解，只在问答时按问题返回相应来源。

### 文献说明

对应文献的详细摘要和作用见第 10-14、17 和 26 页讲稿。

---

## 第 34 页　References 7

### 讲稿

本页主要包括人与机器、自主智能体透明度、开发者调查和 SART。若被追问态势感知与智能体透明度的关系，或者 SART 的来源，可以返回本页。

### 文献说明

对应文献的详细摘要和作用见第 2、12、13、17 和 18 页讲稿。

---

## 第 35 页　References 8

### 讲稿

本页主要包括智能体透明度综述和混合方法研究。若被追问透明度、态势感知、工作负荷、表现之间的区别，或后续定性与定量研究如何衔接，可以返回本页。

### 文献说明

对应文献的详细摘要和作用见第 13、18、24 和 26 页讲稿。

---

## 第 36 页　References 9

### 讲稿

本页包括人工智能代码信任和元宇宙游戏经验价值研究。其中 Zhou 等的 JMIS 文章是第 23 页理论指导与二手数据往返开发维度的重要参照。

### 文献说明

对应文献的详细摘要和作用见第 19 和 23 页讲稿。
