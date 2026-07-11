# 编程智能体态势感知的概念化与测量：构念开发论文逐句对标稿

> 本稿用于规划一篇以构念开发为核心的独立期刊论文。第 1 至第 3 节逐段对应 Chen 等（2024）的论证功能及引文分工，但不复写其原句。相关论据优先来自 `database/ALL_AIS_Basket_11.csv` 中的原始摘要、态势感知经典文献以及已经正式发表的近期编程智能体研究。正文中的 HTML 注释标识与 Chen 等文章的功能位置，渲染时不显示。第 4 节以后仍为预期实施方案，不得在数据收集完成前表述为已经取得的结果。

## 拟定题目

**中文题目：** 编程智能体态势感知的概念化与测量：面向代理式软件开发任务的构念开发

**英文题目：** *Conceptualization and Measurement of Coding-Agent Situation Awareness: Construct Development for Agentic Software Development Tasks*

## 摘要（研究计划版）

编程智能体能够围绕用户目标规划步骤、调用工具并连续修改软件制品，由此把人与信息系统的关系从直接操作扩展到任务委托。用户能否形成对智能体行动所生成的任务状态的主观认识，是其作出继续委托、介入调整和接受结果等判断的认知基础，但现有研究尚未形成用于描述和测量这一认识的编程智能体特定构念。本文拟以个体层面的主观态势感知为唯一基础构念，采用顺序探索型混合方法开发编程智能体态势感知。第一阶段将编码 Reddit 中用户对真实编程智能体任务的公开叙述，并在经验范畴与主观态势感知理论之间反复比较，以界定构念领域及潜在维度。第二阶段将通过题项生成、内容效度评估、认知访谈、多轮独立样本检验和法则网络验证开发 CASA 量表。预期研究将说明传统主观态势感知在代理式软件开发任务中遗漏了哪些任务状态内容，形成研究编程智能体个体体验的测量工具，并为行动、制品变化和执行证据的界面呈现提供诊断依据。

**关键词：** 编程智能体；态势感知；构念开发；量表开发；二手在线文本；混合方法

## 1 引言

人工智能正在使信息系统由接受用户操作的被动工具转变为能够感知情境、发起行动并适应反馈的能动型制品（Schuetz & Venkatesh, 2020; Baird & Maruping, 2021）。<!-- C19.1 --> 编程智能体是这一变化在软件开发中的具体表现：它可以读取项目材料、分解用户目标、调用编辑器与终端工具、修改软件制品，并依据执行结果继续选择行动（Kumar et al., 2025）。<!-- C19.2 --> 这些能力使用户能够将缺陷修复、测试生成、代码重构和项目维护等多步骤任务委托给系统，而不再逐项指定每一次操作。<!-- C19.3 --> Baird 和 Maruping（2021）据此指出，能动型信息系统能够在需求含混和结果不确定的条件下接受任务与部分行动责任，传统信息系统使用研究所假定的人类能动性优先因而需要由委托关系加以补充。<!-- C19.4 -->

编程智能体的任务价值并不只由最终代码决定，其实现还依赖用户与智能体在任务过程中形成的持续协作。<!-- C19.5 --> Kumar 等（2025）观察 19 名开发者解决 33 个真实软件问题后发现，渐进处理问题并持续调整智能体工作的参与者更容易完成任务，而一次性委托和低互动方式较少成功。<!-- C19.6 --> Dhanorkar 等（2026）对 17 名资深开发者的访谈进一步表明，用户会在事前限制、共同规划、实时查看和事后复核等阶段持续处理智能体工作，并在代码难以审查时借助计划与测试结果判断任务状况。<!-- C19.7 --> 这些研究说明，编程智能体减少了用户的直接操作，却没有消除用户在任务过程中判断进展、偏差和结果可接受性的需要。<!-- C19.8 --> 用户如何认识智能体持续行动所形成的任务状态，因而构成编程智能体交互中有待概念化的重要问题。<!-- C19.9 -->

然而，编程智能体任务中的状态认识不能由传统操作环境中的态势感知测量直接表示。<!-- C21.1 --> 经典态势感知研究主要考察操作者对外部环境和被控系统状态的感知、理解与预期，相关任务通常具有研究者可以预先分析的状态要素和目标（Endsley, 1995a, 1995b）。<!-- C21.2 --> 自动化研究虽然把部分信息处理或行动功能交给机器，但其基本设计仍以预先分配的人机功能和自动化层级为基础（Parasuraman et al., 2000）。<!-- C21.3 --> 编程智能体则围绕开放目标自行选择行动，智能体的行动轨迹不仅反映任务状态，也会通过修改软件制品持续生成新的任务状态（Baird & Maruping, 2021; Kumar et al., 2025）。<!-- C21.4 -->

这一代理行动关系在五个方面改变了用户需要认识的内容。<!-- C21.5 --> 第一，相关状态包含智能体当前行动及其理由，而不只是外部环境发生了什么。<!-- C21.6 --> 第二，状态线索分布于计划、对话、工具调用、文件差异、命令输出、测试结果和权限请求等异质载体，用户需要把这些线索联系为同一任务过程（Kumar et al., 2025; Dhanorkar et al., 2026）。<!-- C21.7 --> 第三，智能体改变的是相互依赖且可以执行的软件制品，软件变更影响分析研究表明，一个制品的改变可能要求其他制品共同变化并产生后续测试需求（Kretsou et al., 2021）。<!-- C21.8 --> 第四，用户没有亲自完成智能体采取的每一步行动，其任务认识依赖系统保留和呈现的行动痕迹，因而延续并加深了自动化研究所揭示的脱离环路问题（Endsley & Kiris, 1995）。<!-- C21.9 --> 第五，智能体可以在用户注意力转移时继续工作，主动提示的时机也会改变用户是否查看和处理系统信息（Kuo et al., 2026）。<!-- C21.10 --> 这些差异同时改变了态势感知的状态对象、信息来源和时间结构，使一般航空或自动化量表难以直接覆盖编程智能体任务。<!-- C21.11 -->

态势感知可以为描述这种任务认识提供基础。<!-- C23.1 --> Taylor（1990）以主观方式考察个体对影响任务完成的事件、因素和变量所具有的知识、认知与预期；Endsley（1995b）则把态势感知界定为对任务相关要素的感知、对其意义的理解以及对其近期状态的预期。<!-- C23.2 --> 在人工智能情境中，态势感知被认为支持用户理解自主系统的当前状态、行动依据和未来状态，并为适当介入与信任校准提供认知条件（Selkowitz et al., 2017; Endsley, 2023）。<!-- C23.3 --> 本文据此把编程智能体态势感知暂定为：个体用户在一次具体编程智能体任务中，对自己能够认识智能体代理行动所形成的任务相关状态及其近期发展的程度判断。<!-- C23.4 --> 该定义中的任务相关状态包括智能体行动、软件制品变化、执行证据以及这些内容与任务目标的关系，但其经验维度仍需由后续数据确定。<!-- C23.5 --> 较高的 CASA 表示用户感觉自己能够形成连贯且可更新的任务认识；较低的 CASA 表示用户难以判断任务已经发生什么、当前意味着什么或接下来可能发生什么。<!-- C23.6 -->

CASA 的理论价值在于刻画任务表现之外的用户认知状态。<!-- C23.7 --> 自动化可能在提高系统能力的同时削弱操作者的态势感知和接管表现（Endsley & Kiris, 1995），运营决策研究也发现，分析功能带来的任务表现提升可以与态势感知下降同时出现（Nadj et al., 2020）。<!-- C23.8 --> 主观态势感知与客观态势感知在多种测量条件下亦会发生分离（Endsley, 2020）。<!-- C23.9 --> CASA 因而不评价智能体是否正确完成任务，而评价用户是否感觉自己了解该任务目前处于何种状态。<!-- C23.10 --> 对任务状态的认识使用户能够基于当前局面作出继续委托、介入调整或接受结果的判断，并可能提高其对可用控制机制的主观把握；既有 IS 研究表明，感知控制与系统接受相关（Baronas & Louis, 1988）。<!-- C23.11 --> 人工智能成员还可能影响个体的过程满意度，即使其可信度和继续合作意愿没有相应差异（Dennis et al., 2023），这表明人机协作过程需要由信任之外的体验加以解释。<!-- C23.12 --> CASA 是否进一步解释使用满意度，以及满意度是否按照 IS 持续使用研究所建立的关系连接到持续使用意愿，是本文需要检验的法则网络（Bhattacherjee, 2001）。<!-- C23.13 -->

态势感知已经在航空、自动化、列车驾驶、决策支持和信息安全等动态任务中得到研究，但不同情境采用了不同的概念内容与测量方式。<!-- C25.1 --> Taylor（1990）依据空勤人员的情境描述和构念判断开发 SART，以注意需求、注意供给和理解评价个体对自身态势感知的主观判断。<!-- C25.2 --> Endsley（1995a, 1995b）以任务分析为基础发展 SAGAT，通过暂停任务并询问预先确定的状态问题评价操作者实际掌握的任务信息。<!-- C25.3 --> 当通用 SART 难以适应低事件列车驾驶时，Rose 等（2018）根据任务信息要求开发了 LETSSA；在信息系统领域，Jaeger 和 Eckhardt（2021）将态势感知情境化为个体面对网络钓鱼威胁时的信息安全态势感知，Nadj 等（2020）则检验分析仪表盘功能对决策者态势感知的影响。<!-- C25.4 --> 这些研究说明，态势感知可以跨情境研究，但构念内容和测量必须与特定用户所面对的状态对象和任务要求一致（Stanton et al., 2006; Moens et al., 2026）。<!-- C25.5 -->

现有主观态势感知量表缺少直接用于编程智能体任务的内容效度，因而需要大幅修订或重新开发。<!-- C25.6 --> SART 的十项评价及其注意需求、注意供给和理解结构源于航空任务，未指向智能体采取的行动、被改变的软件制品或用于判断变化效果的执行证据（Taylor, 1990）。<!-- C25.7 --> SART 中的不稳定性、复杂性、信息数量和注意分配还同时涉及任务需求与个体资源；直接纳入 CASA 会混淆用户形成了何种任务认识与这种认识为何难以形成。<!-- C25.8 --> Bolton 等（2022）进一步发现，SART 各组成部分虽多可作为区间尺度处理，却处于彼此不同的尺度，这使原有合成公式的测量意义受到质疑。<!-- C25.9 --> SAGAT 可以评价用户对研究者预设任务真值的实际掌握，却不直接测量用户对自身任务认识的主观判断（Endsley, 1995a, 2021）。<!-- C25.10 --> 37 项同时采用主客观方法的研究表明，两类态势感知测量普遍发生分离，并可能受到元认知校准和工作负荷混淆的影响（Endsley, 2020）。<!-- C25.11 --> 编程智能体任务由智能体选择的行动轨迹持续生成状态，研究者更难以用一套跨任务固定问题完整表示其状态空间。<!-- C25.12 --> 因此，CASA 需要保留主观态势感知的理论内核，同时重新识别编程智能体任务中构成这种认识的具体内容。<!-- C25.13 -->

人工智能编程研究已经揭示 CASA 所涉及的若干经验现象。<!-- C27.1 --> Barke 等（2023）发现，程序员使用代码生成工具时会在目标明确的加速模式与目标仍在形成的探索模式之间切换；Mozannar 等（2024）进一步识别了程序员阅读、验证、编辑和处理代码建议时的活动状态及其时间成本。<!-- C27.2 --> Ferdowsi 等（2024）表明，持续呈现运行时值可以降低部分人工智能生成代码的验证负担，说明界面所提供的执行证据会改变用户理解建议的条件。<!-- C27.3 --> Wang 等（2024）发现，开发者通过评价系统能力和具体代码建议形成信任判断，而现有界面缺少支持高效评价的功能。<!-- C27.4 --> 针对编程智能体，Kumar 等（2025）记录了渐进协作、调试和测试中的沟通困难，Dhanorkar 等（2026）则识别了贯穿任务前后的四类监督工作及代码审查困难。<!-- C27.5 --> Kuo 等（2026）的现场研究还显示，开发者对主动式人工智能建议的接受取决于建议出现的工作流阶段，任务中途提示更容易被忽略或拒绝。<!-- C27.6 -->

这些研究分别以互动模式、验证活动、信任判断、监督实践或提示时机为研究对象，尚未把用户对整个代理式任务状态的主观认识概念化为共同构念。<!-- C27.7 --> 代码生成研究大多围绕一项候选建议展开，而编程智能体能够连续选择行动并修改多个制品，用户所面对的认识对象由单项输出扩展为由代理行动持续形成的任务状态（Baird & Maruping, 2021; Kumar et al., 2025）。<!-- C27.8 --> 验证成本、解释、透明度和信任可以成为 CASA 的前因、后果或相邻现象，却不能回答用户在多大程度上感觉自己了解当前任务。<!-- C27.9 -->

因此，有必要发展适用于编程智能体任务的情境特定态势感知构念及量表。<!-- C29.1 --> 情境化理论只有在新情境揭示一般构念未能表达的内容或关系时才具有理论价值（Hong et al., 2014），而情境特定量表也需要证明其较一般量表具有更准确的内容覆盖和经验效度（Hoehle & Venkatesh, 2015; Chen et al., 2024）。<!-- C29.2 --> CASA 量表将使研究者能够区分智能体是否完成任务与用户是否感觉自己了解任务，并检验界面、任务和用户因素如何影响这一主观认识。<!-- C29.3 --> 该量表还可用于识别用户主观上较难把握的任务方面，并为行动记录、差异呈现、检查点和任务通知等设计机制提供评价依据。<!-- C29.4 -->

考虑到编程智能体代理行动所形成的任务状态、态势感知对用户作出任务判断的作用，以及现有文献在概念化和测量方面的缺口，本文拟回答两个研究问题：<!-- C31.1 -->

**研究问题 1：CASA 包含哪些维度，应当如何测量这些维度？**<!-- C31.2 -->

**研究问题 2：与一般主观态势感知测量相比，CASA 对感知控制、满意度和持续使用意愿是否具有增量解释效度和预测效度？**<!-- C31.3 -->

本文拟采用顺序探索型混合方法，先开展定性构念开发，再开展定量量表开发与验证（Venkatesh et al., 2013）。<!-- C33.1 --> 第一阶段将收集 Reddit 中用户关于真实编程智能体任务的公开帖子和评论，采用开放编码和轴向编码识别用户认识或难以认识任务状态时涉及的经验范畴（Corbin & Strauss, 1990）。<!-- C33.2 --> 编码结果将与 Taylor（1990）的主观态势感知及其他任务特定态势感知研究反复比较，以判断哪些范畴构成 CASA 内容，哪些范畴属于其前因、后果或相邻构念。<!-- C33.3 --> 这种理论与数据的反复比较既避免将航空量表直接移植到软件开发，也避免仅凭用户评论中出现频繁的词语形成缺乏理论边界的分类。<!-- C33.4 -->

Taylor（1990）的 SART 构念引出过程将作为第一阶段的理论起点，因为该研究从任务参与者对高、低态势感知情境的比较中识别主观判断内容，而不是预先以界面属性代替态势感知。<!-- C35.1 --> Reddit 语料用于识别编程智能体用户实际把哪些行动、变化、证据和发展判断视为掌握或失去任务局面的表现。<!-- C35.2 --> 第二阶段将依据修订后的构念定义、定性范畴和既有态势感知测量形成题项池，并依照成熟的 MIS 构念开发程序开展内容效度、题项分类、多轮独立样本验证和法则效度检验（Moore & Benbasat, 1991; Lewis et al., 2005; MacKenzie et al., 2011）。<!-- C35.3 --> 最后，本文将比较 CASA 与一般主观态势感知测量对感知控制、满意度和持续使用意愿的解释与预测能力。<!-- C35.4 -->

本文预期形成三方面贡献。<!-- C37.1 --> 第一，本文将界定 CASA 的内容领域、构念边界和经验维度，并形成可供后续研究使用的测量工具。<!-- C37.2 --> 第二，本文将通过编程智能体中的任务委托发展个体层面的主观态势感知研究，说明当系统能够自行选择行动时，用户需要认识的任务状态同时包含代理行动及其对软件制品造成的变化。<!-- C37.3 --> 第三，CASA 量表将为比较不同界面、交互模式和任务设计提供诊断工具，支持产品开发者评价计划、行动、变化和执行证据的呈现是否有助于用户形成任务认识。<!-- C39.1 --> 新构念的贡献将由后续定性材料所显示的内容差异、CASA 与相邻构念的区分效度以及相对于一般主观态势感知的增量效度共同检验。<!-- C39.2 -->

## 2 理论背景

### 2.1 编程智能体情境与其他情境中的态势感知

态势感知是个体在动态任务中形成和更新任务相关认识的构念，其内容取决于个体的目标、任务要求以及需要据以行动的状态信息（Endsley, 1995b; Stanton et al., 2006）。<!-- C45.1 --> Taylor（1990）从个体对影响任务完成的事件、因素和变量所具有的知识、认知与预期出发，通过空勤人员的构念引出形成主观态势感知测量 SART。<!-- C45.2 --> Endsley（1995b）则从动态决策出发，把态势感知表述为对相关要素的感知、对其意义的理解和对其近期状态的预期，并以目标导向任务分析建立可由客观问题评价的状态要求（Endsley, 1995a）。<!-- C45.3 --> 两条传统分别发展出主观自评和客观探测方法；最新跨领域综述据此把直接测量进一步区分为自我评价、观察者评价和探测技术，并强调测量工具应与研究所采用的态势感知概念及任务目的相一致（Moens et al., 2026）。<!-- C45.4 --> 既有研究中的主要概念化与测量如表 1 所示。<!-- C45.5 -->

| 情境与研究对象 | 概念内容与状态对象 | 测量或经验依据 | 主要发现及对 CASA 的限制 | 代表文献 |
| --- | --- | --- | --- | --- |
| 航空任务中的空勤人员 | 对影响任务完成的事件、因素和变量所具有的主观知识、认知与预期 | 构念引出；SART 十项评价及三类高阶组成 | 提供 CASA 的主观、任务导向起点；具体项目和合成结构来自航空任务 | Taylor, 1990; Bolton et al., 2022 |
| 动态系统操作者 | 对任务相关要素的感知、意义理解和近期状态预期 | 目标导向任务分析；SAGAT 任务冻结与状态问题 | 提供任务内容分析和客观校准方法；不直接测量用户对自身认识程度的评价 | Endsley, 1995a, 1995b, 2021 |
| 自动化导航任务操作者 | 人在不同自动化控制水平下对系统与任务状态的认识 | 模拟任务、状态探测和接管表现 | 自动化可造成脱离环路并降低接管表现；自动化功能和状态空间相对预定 | Endsley & Kiris, 1995; Parasuraman et al., 2000 |
| 低事件列车驾驶员 | 对列车位置、速度、信号、线路与近期事件的主观认识 | 任务分析；LETSSA；专家与新手模拟实验 | 证明主观 SA 测量需按任务信息要求重建；不含代理行动或软件制品状态 | Rose et al., 2018 |
| 自主机器人使用者 | 对自主体当前行动、行动理由、未来状态及不确定性的认识 | 分层透明度界面；SA、信任、负荷与认知处理测量 | 较高透明度可提高 SA 与信任；状态围绕具身机器人和给定任务展开 | Selkowitz et al., 2017 |
| 人工智能协作者 | 对任务、人工智能状态及协作关系的当前认识 | 态势感知导向设计框架和人机协作研究综述 | 明确透明度、可解释性与 SA 的不同作用；主要讨论一般人机协作而非软件开发 | Endsley, 2023 |
| 运营决策仪表盘用户 | 对运营决策问题和分析结果的任务认识 | 实验、眼动、状态测量和任务表现 | 分析功能可以提高表现而降低 SA；系统处理信息但不连续修改任务制品 | Nadj et al., 2020 |
| 网络钓鱼情境中的个体员工 | 对当前威胁情境的注意、解释和风险认识 | 眼动、问卷、警告设计和实际应对行为 | 提供个体层 IS 情境化 SA 的先例；状态对象是威胁线索而非代理行动 | Jaeger & Eckhardt, 2021 |
| 编程智能体用户 | 对规划、行动、代码变化、执行反馈与任务进展的认识尚未被统一界定 | 观察、访谈、活动分类和现场研究 | 已揭示协作与监督所需信息，但尚无主观 CASA 构念及量表 | Kumar et al., 2025; Dhanorkar et al., 2026 |

表 1 显示，态势感知的状态对象与测量内容会随任务情境发生实质变化。<!-- C47.1 --> SART 评价空勤人员面对的不稳定性、复杂性、变量数量、信息质量、注意资源和理解程度；LETSSA 则依据列车驾驶要求重新聚焦位置、速度、线路信号和未来事件（Taylor, 1990; Rose et al., 2018）。<!-- C47.2 --> 信息安全态势感知同样围绕威胁线索及其解释建立，而不是把航空量表中的对象名称替换为钓鱼邮件（Jaeger & Eckhardt, 2021）。<!-- C47.3 --> 这些研究为 CASA 的情境化提供先例，也表明情境特定测量必须由实际任务信息要求支持。<!-- C47.4 -->

编程智能体任务尚未被现有量表覆盖。<!-- C47.5 --> SART 的一般项目不能区分用户是否认识智能体做了什么、哪些软件制品发生变化、执行证据支持何种判断以及任务下一步可能如何发展。<!-- C47.6 --> 自主机器人透明度研究虽然已经测量用户对自主体行动、理由和预期的认识，但其状态对象是具身代理在给定环境中的位置与任务，未处理可执行软件制品的跨文件变化及其技术依赖（Selkowitz et al., 2017）。<!-- C47.7 --> SAGAT 一类客观探测方法可以为统一实验任务建立状态真值，却难以单独构成跨产品、跨仓库和跨开放任务的主观体验量表。<!-- C47.8 --> 编程智能体研究也尚未形成能够比较不同用户、任务和产品的共同测量单位。<!-- C47.9 --> 现有文献由此同时缺少 CASA 的内容框架和经过验证的情境特定量表。<!-- C47.10 -->

### 2.2 编程智能体相关的邻近研究

编程智能体用户研究尚处于形成阶段，既有工作主要从程序员活动、人工智能建议、信任评价和监督实践等角度描述用户与系统的互动。<!-- C51.1 --> 表 2 按照研究对象、经验发现及其与 CASA 的关系归纳已经正式发表的代表性研究。<!-- C51.2 -->

| 研究主题 | 研究对象与方法 | 与 CASA 相关的主要发现 | 尚未覆盖的内容 | 代表文献 |
| --- | --- | --- | --- | --- |
| 人工智能编程互动模式 | 17 名程序员使用代码生成模型；扎根理论 | 用户在加速与探索两种模式间切换，并采用不同方式表达意图和验证代码 | 研究对象是代码建议，未测量连续代理任务的主观状态认识 | Barke et al., 2023 |
| 建议处理活动与成本 | 人工智能辅助编程任务；行为序列与时间成本建模 | 阅读、验证、编辑、提示和等待构成可区分的活动状态 | 描述用户做了什么及付出多少时间，不测量用户觉得自己了解多少 | Mozannar et al., 2024 |
| 代码验证界面 | 持续呈现运行时值的实验性编程界面 | 执行信息可以降低验证部分代码建议的成本 | 运行时值是可能的界面前因，不能代表完整 CASA | Ferdowsi et al., 2024 |
| 对代码生成工具的信任 | 开发者访谈及设计分析 | 用户同时评价系统一般能力和具体建议，现有界面难以支持高效评价 | 信任是依赖意愿与目标实现判断，不等同于任务状态认识 | Wang et al., 2024 |
| 开发者与软件智能体协作 | 19 名开发者解决 33 个真实软件问题 | 渐进解决、主动互动和持续迭代与更高任务成功相联系 | 以协作方式和成功为焦点，没有形成主观认知状态量表 | Kumar et al., 2025 |
| 软件智能体监督实践 | 17 名资深开发者访谈 | 监督包含事前限制、共同规划、实时查看和事后复核，代码审查困难促使用户采用替代线索 | 识别监督工作及启发式，不测量用户对任务状态的主观掌握程度 | Dhanorkar et al., 2026 |
| 主动式人工智能介入 | 15 名专业开发者的五日 IDE 现场研究 | 工作流边界提示比任务中途提示更易被接受，介入时机影响认知干扰 | 研究主动建议而非完整代理任务，主要结果是介入接受与体验 | Kuo et al., 2026 |

尽管部分研究内容可以用于理解 CASA，其覆盖范围仍不充分。<!-- C53.1 --> 从广度看，没有任何一项研究同时概念化用户对智能体行动、软件制品变化、执行证据及任务近期发展的主观认识。<!-- C53.2 --> 互动模式与活动状态描述用户如何工作，验证与监督研究描述用户如何检查智能体，信任研究描述用户是否愿意依赖系统；这些研究对象均不同于用户是否感觉自己了解任务当前状态。<!-- C53.3 --> 从深度看，一般态势感知或透明度项目也不能通过替换对象名称准确表示代理式软件开发。<!-- C53.4 --> 例如，SART 的信息数量和信息质量可以评价用户面对的信息环境，但不能区分用户是不了解智能体采取的行动、不了解代码改变的范围，还是不能判断测试结果对任务目标意味着什么（Taylor, 1990）。<!-- C53.5 --> 同样，解释和透明度能够改变用户的信息处理与心智模型，却可能同时产生确认偏差或误解，说明系统提供信息不等于用户已经形成任务认识（Gregor & Benbasat, 1999; Bauer et al., 2023）。<!-- C53.6 -->

现有知识由此存在三项相互关联的不足。<!-- C55.1 --> 第一，编程智能体研究把互动、验证、信任和监督作为彼此分离的现象，尚未建立描述用户主观任务认识的共同构念。<!-- C55.2 --> 第二，传统主观态势感知量表未表达由智能体代理行动生成的软件任务状态；若直接使用一般项目，研究只能获得整体理解评价，不能诊断用户具体缺少何种认识。<!-- C55.3 --> 第三，既有编程智能体研究以观察、访谈、活动分类和任务结果为主，缺少能够测量个体差异、比较产品设计并检验前因后果的经过验证量表。<!-- C55.4 --> 这些不足分别对应构念缺口、内容缺口和测量缺口。<!-- C55.5 --> 在没有解决这些缺口之前，研究者难以判断行动透明度、差异视图、审批频率或通知时机是否通过改善用户的任务认识发挥作用，也难以检验这种认识是否与感知控制和满意度具有不同关系。<!-- C55.6 -->

### 2.3 SART 主观态势感知传统

SART 为 CASA 构念开发提供主观态势感知的理论和方法起点。<!-- C59.1 --> Taylor（1990）首先请空勤人员描述代表高、低态势感知的任务情境，再通过个人构念方格比较这些情境，以引出参与者实际用来判断自己是否掌握局面的属性。<!-- C59.2 --> 经由情境生成、构念引出、构念排序和结构分析，研究将十项评价归纳为注意需求、注意供给和理解三个组成部分，并以此形成可用于系统设计比较的 SART。<!-- C59.3 --> 因而，SART 不只是一个十题量表，也是一种从任务参与者经验识别主观态势感知内容的构念开发路径。<!-- C59.4 --> 对 CASA 而言，可以继承的是以具体任务经验引出主观认识内容的逻辑，而不是航空任务产生的项目和评分公式。<!-- C59.5 -->

SART 所处理的问题与编程智能体任务具有可辨识的共同结构。<!-- C61.1 --> 两种情境都要求个体在系统承担部分行动时，根据有限且不断更新的信息评价自己是否了解当前局面。<!-- C61.2 --> 编程智能体中的用户由每一步软件操作的直接执行者转为任务目标的提供者、过程中的协作者以及必要时的介入者，这与自动化使人转向监督角色的基本问题相连（Bainbridge, 1983; Endsley & Kiris, 1995）。<!-- C61.3 --> Baird 和 Maruping（2021）的委托框架进一步表明，能动型信息系统可以在不确定条件下接受任务并发起行动，用户与系统之间因而需要持续的评价与协调。<!-- C61.4 --> 真实编程智能体研究中的共同规划、实时查看和事后复核也显示，用户需要更新自己对任务当前状况的认识（Kumar et al., 2025; Dhanorkar et al., 2026）。<!-- C61.5 --> SART 对个体主观局面认识的关注由此与 CASA 的研究对象相符。<!-- C61.6 -->

SART 又不能直接作为 CASA 的测量。<!-- C63.1 --> 首先，其十项属性及三个组成部分来自空勤任务，没有说明软件开发中哪些代理行动、制品变化和执行证据构成任务相关状态（Taylor, 1990）。<!-- C63.2 --> Rose 等（2018）因 SART 在低事件列车驾驶中的内容与效度问题另行开发 LETSSA，说明同为主观态势感知，不同任务仍需要依据任务要求重新识别测量内容。<!-- C63.3 --> 其次，SART 将不稳定性、复杂性、注意资源、信息数量和理解共同用于计算总分，但其中若干内容在编程智能体情境中更适合作为任务或界面条件。<!-- C63.4 --> 例如，审批频率、日志冗余、主动提示和任务切换会占用注意资源，并可能影响用户能否形成任务认识；若把它们纳入 CASA 定义，研究将无法检验这些设计因素如何影响 CASA。<!-- C63.5 --> Bolton 等（2022）关于 SART 各组成部分处于不同区间尺度的结果，也要求新研究重新论证测量模型，而不能沿用原有加减公式。<!-- C63.6 -->

再次，一般性的理解评价缺少编程智能体任务所需的内容诊断。<!-- C63.7 --> 自主代理研究表明，用户可能分别需要认识代理的当前行动、行动理由、未来状态和不确定性（Selkowitz et al., 2017; Endsley, 2023）；编程智能体任务还增加了行动所造成的软件制品变化及其执行证据。<!-- C63.8 --> 最后，主观测量反映用户对自身认识程度的判断，不保证其判断与任务真值一致；主客观态势感知在既有研究中通常只有有限对应（Endsley et al., 1998; Endsley, 2020）。<!-- C63.9 --> CASA 因此需要在保留主观属性的同时，以任务状态问题或行为效标检验校准，但不能由客观正确率重新定义。<!-- C63.10 -->

本文据此只以个体层面的主观态势感知作为 CASA 的基础构念。<!-- C63.11 --> CASA 的分析单位是一次具体编程智能体任务中的个体用户，其属性是随任务状态和交互变化的主观认知状态，而不是稳定人格、一般人工智能态度或团队共享认知。<!-- C63.12 --> CASA 的判断对象是智能体代理行动所形成的任务相关状态，不是智能体的一般能力、界面属性或最终软件质量。<!-- C63.13 --> 感知、理解和预期可以作为初始理论敏感概念，用于检查经验范畴是否覆盖态势感知的基本内容，但不预先规定为最终维度。<!-- C63.14 --> 信任、透明度、感知控制、认知负荷和任务表现只用于界定构念边界、建立前因后果或检验效度。<!-- C63.15 --> CASA 与这些构念的区别如表 3 所示。

| 构念 | 主要判断对象 | 与 CASA 的区别 | 在后续研究中的位置 |
| --- | --- | --- | --- |
| 人工智能信任 | 智能体是否会帮助用户在不确定和脆弱条件下实现目标（Lee & See, 2004） | CASA 不评价智能体是否值得依赖，而评价用户是否感觉自己了解当前任务状态 | 区分效度对象；可能后果或并列态度 |
| 感知透明度 | 系统是否揭示与其行动或判断相关的信息（Xu et al., 2014; Selkowitz et al., 2017） | 透明度评价系统提供的信息，CASA 评价用户基于相关信息形成的任务认识 | 可能前因；区分效度对象 |
| 感知控制 | 用户是否感觉自己能够影响任务过程或系统行为（Baronas & Louis, 1988） | 用户可以拥有停止、审批或回滚权限却不了解何时使用，也可以了解状态却缺少相应权限 | 主要后果；区分效度对象 |
| 认知负荷 | 任务对有限认知资源的占用程度 | 负荷会影响信息加工条件，但不表明用户形成了何种任务认识 | 可能前因或控制变量 |
| 客观任务状态知识 | 用户回答根据任务真值建立的问题时的正确程度（Endsley, 1995a, 2021） | CASA 是用户对自身认识程度的主观判断，不保证客观正确 | 校准与效标效度 |
| 任务表现 | 任务完成质量、速度或正确性 | 系统功能可以提高表现而同时降低个体态势感知（Nadj et al., 2020） | 远端效标，不进入构念定义 |

## 3 混合方法路径

### 3.1 研究设计

本文拟采用顺序探索型混合方法回答两个研究问题。<!-- C69.1 --> CASA 的内容领域不能由航空量表或研究者直觉预先穷举，识别编程智能体用户实际用来判断任务局面的内容需要定性研究。<!-- C69.2 --> 确定这些内容是否构成可区分且稳定的维度，并建立具有信度、效度和预测能力的测量工具，则需要定量研究。<!-- C69.3 --> 混合方法能够在同一研究计划中连接理论生成与理论检验，使定性材料所形成的构念推断接受独立数据评价（Venkatesh et al., 2013）。<!-- C69.4 --> 本研究将由定性阶段形成 CASA 的概念定义、内容边界和候选维度，再由定量阶段检验测量模型、构念效度及法则网络。<!-- C69.5 -->

研究拟分为两个阶段。<!-- C77.1 --> 第一阶段将从公开 Reddit 讨论中收集编程智能体使用叙述，并采用源于扎根理论的开放编码和轴向编码识别用户认识或难以认识任务状态时涉及的经验内容（Corbin & Strauss, 1990）。<!-- C77.2 --> 在线用户文本能够保留用户在自然使用情境中主动提出的问题，Chen 等（2024）也据此先从二手评论识别情境特定内容，再由理论组织高阶构念。<!-- C77.3 --> CASA 编码将包括预编码、全样本开放编码、轴向编码、理论比较和负例分析，并以数据结构呈现从用户表达、一阶代码到理论范畴的推导过程（Gioia et al., 2013）。<!-- C77.4 --> 两名编码者将独立分析文本，另外两名研究者负责审查范畴定义、处理边界争议并检验替代解释。<!-- C77.5 --> 轴向范畴形成后，研究团队将逐项比较其与 Taylor（1990）的主观态势感知、任务特定态势感知量表及相邻构念的关系，判断其属于 CASA 内容、前因、后果还是构念外部条件。<!-- C77.6 --> 该阶段的目标是形成由经验材料和理论比较共同支持的内容领域与候选维度，而不是验证预设的三维结构。<!-- C77.7 -->

第二阶段将开发并验证 CASA 测量工具。<!-- C79.1 --> 第一项工作是依据定性代码、构念定义和既有态势感知测量生成初始题项，并通过专家评审、认知访谈和多轮题项分类检验内容与表面效度（Moore & Benbasat, 1991; MacKenzie et al., 2011）。<!-- C79.2 --> 第二项工作是使用第一轮独立调查数据开展探索性分析，净化题项并比较可能的构念结构。<!-- C79.3 --> 第三项工作是使用第二轮独立调查数据开展验证性分析，检验信度、收敛效度、区分效度和跨群体稳定性；构念与维度之间的关系将依据概念含义而不是统计便利确定（Law et al., 1998; Jarvis et al., 2003; Petter et al., 2007）。<!-- C79.4 --> 第四项工作是使用第三轮独立数据重新检验量表，并建立包含感知控制、满意度和持续使用意愿的法则网络。<!-- C79.5 --> 最后，研究将比较 CASA 与一般主观态势感知测量的解释效度和样本外预测效度，并在实验子样本中比较 CASA 与客观任务状态知识。<!-- C79.6 -->

表 4 概括预期研究阶段。表中的样本规模是最低规划范围，正式实施前将依据最终题项数、模型复杂度和统计功效分析确定。

| 阶段 | 目标 | 主要程序 | 预期证据 |
| --- | --- | --- | --- |
| 阶段 1：构念开发 | 界定 CASA 内容领域与候选维度 | Reddit 语料筛选；预编码；双人开放编码；轴向编码；理论比较；负例分析 | 数据结构、范畴定义、边界证据、理论饱和 |
| 阶段 2A：初始量表 | 生成并净化题项内容 | 题项池；ITEM 语义审计；专家内容效度；认知访谈；多轮卡片分类 | 内容代表性、清晰性、构念可区分性 |
| 阶段 2B：探索与验证 | 确定测量模型并检验稳定性 | 独立样本 EFA；独立样本 CFA；竞争测量模型；测量不变性 | 因子结构、信度、收敛与区分效度 |
| 阶段 2C：法则网络与预测 | 证明 CASA 的理论和实践增量 | 两时点或多来源调查；法则网络；与 SART 比较；样本外预测；任务真值子研究 | 法则效度、增量效度、预测效度、主客观校准 |

---

# 以下为预期实施内容

## 4 阶段 1：使用二手在线文本开发 CASA 构念

### 4.1 数据来源与抽样范围

研究将使用 Reddit 公开帖子和评论作为第一阶段的经验材料。选择 Reddit 不是因为该平台能够代表所有编程智能体用户，而是因为产品专属社区和跨产品编程社区中保留了用户对具体任务、界面、失败、检查和后续处理的自然叙述。相较于仅询问研究者预设问题的问卷，这些叙述更可能暴露用户自发认为重要的任务状态及其缺失方式。与此同时，Reddit 用户具有自选择性，帖子受到社区规范和产品热度影响，而且问题与失败经历可能比平稳使用经历更容易被发布。因此，该数据只用于发现和界定构念内容，不用于估计总体发生率。

候选语料来源将同时包含跨产品的编程智能体讨论社区和产品专属社区，以避免把某一产品界面的特征误当作 CASA 的普遍内容。正式社区名单将在试采集阶段依据三个标准确定：社区中存在持续的第一手使用讨论；讨论能够识别所用工具或交互形态；社区规则允许研究者在遵守平台政策的条件下访问公开内容。研究将记录产品、界面形态、任务类型、发布时间和可识别的使用经验信息，以支持分层比较，但不会收集私信、受限社区内容或已删除内容。由于公开讨论可能遗漏企业内部任务和用户未主动言明的隐性认识，研究将在阶段 1 完成覆盖审计；若企业情境、平稳高 CASA 经历或关键状态内容明显不足，将补充以关键事件为中心的开发者访谈，而不以 Reddit 单一来源宣称内容饱和。

语料检索将采用宽入口、严筛选的策略。入口检索围绕编程智能体产品、代理式任务和软件开发活动展开，不要求文本必须出现理解、态势感知或控制等理论词汇，以免只收集能够印证既有定义的材料。纳入文本需要满足以下条件：描述本人或可明确识别用户的编程智能体使用经历；涉及一个具体任务或连续任务过程；包含智能体行动、软件变化、执行反馈、任务进展、检查判断或后续影响中的至少一项。仅讨论模型排行、价格、新闻、一般产品推荐、纯粹代码求助、自动生成内容或无法判断是否实际使用的文本将被排除。

分析单位以能够表达一个完整意义的任务片段为主，而不是机械地以单条评论为单位。研究将保留必要的帖子标题、上文评论和回复关系，使编码者能够判断代词、产品、任务和事件顺序。每个分析片段将附带去标识化的情境属性，但用户名、个人主页和可追踪身份信息不会进入分析数据集。

### 4.2 伦理与数据治理

公开可访问不等于不存在研究伦理风险。研究实施前将向所在机构伦理审查机构提交方案，并依据互联网研究伦理指南采用情境化风险判断（Franzke et al., 2020; Gliniecka, 2023）。数据采集将遵守届时有效的 Reddit 平台政策和访问方式，不绕过访问限制。研究数据库将用随机编号替代用户名，移除个人身份、雇主、项目名称、仓库地址和其他可追踪信息。

论文呈现原始文本时将评估反向搜索风险。对于包含敏感项目、工作关系或独特表述的材料，优先采用保持分析含义的转述，而不是逐字引用。原始数据不公开发布；可复核材料将以去标识化代码本、范畴定义、审计轨迹和经过风险处理的例证为主。若某个社区对研究使用存在明确反对规范，研究将排除该社区或与管理者沟通后再决定。

### 4.3 编码程序

编码团队预期由四名研究者组成。两名编码者独立完成预编码、开放编码和轴向分类；另外两名具有信息系统、软件工程或人机交互背景的研究者负责审查构念定义、处理争议和检查理论映射。编程智能体可以辅助去重、格式整理和检索，但不得代替研究者作出范畴归属和构念边界判断。所有人工决策、代码修改和争议处理将保留审计记录。

**准备阶段：形成初始编码协议。** 研究团队将先从不同产品、交互形态和任务类型中抽取少量材料，共同识别分析单位、上下文保留规则和排除标准。初始协议只提供任务、智能体行动、软件制品、执行反馈、认识表达和后续反应等宽泛观察位置，不把它们设为最终维度。进入 CASA 候选内容的一阶代码必须表达用户对自身认识状态的判断，例如用户说明自己能够或不能判断智能体做了什么、变化意味着什么或任务将如何继续。仅陈述智能体修改了某个文件、测试失败或任务完成等事实，而没有显示用户如何评价自身认识的文本，只作为任务情境或客观事件编码，不作为 CASA 的直接表现。编码者需要同时标记正向材料、负向材料和边界材料，例如用户明确了解任务、明确不了解任务、拥有大量信息却仍无法判断，以及缺乏信息但凭经验能够判断等情形。

**步骤 1：开放编码预试。** 在符合条件的语料确定后，研究将随机抽取约 10% 作为预试样本，并保证其中覆盖主要产品、界面和任务类型。两名编码者逐段独立标记用户认为自己知道、理解、能够预期或无法判断的任务内容，并用尽可能贴近用户语言的一阶代码表达。双方随后比较差异，澄清代码定义、合并纯同义代码并修订排除规则。预试的目的不是获得高一致性数字，而是暴露构念边界和代码本中不清楚的地方。

**步骤 2：全样本开放编码。** 编码者依据修订后的协议独立处理其余语料，并对重叠子样本进行双人编码。对于已经形成稳定代码定义的代码，将报告 Cohen's kappa 或适合数据结构的 Krippendorff's alpha；对于仍在发现中的开放代码，将报告差异解决过程而不把一致性系数误作理论有效性的替代。研究团队将分批检查新代码出现情况。当连续三个异质批次不再产生新的轴向范畴后，再使用一个此前未参与理论形成的保留批次检验饱和。

**步骤 3：轴向编码。** 两名编码者将独立比较一阶代码之间的对象、状态、时间和意义关系，把描述同一类任务认识的代码聚合为轴向范畴。每个轴向范畴必须包含明确名称、定义、纳入标准、排除标准、正例、负例以及与相邻范畴的区别。仅有极少材料支持、只属于单一产品功能或无法与态度评价区分的代码不会因为新颖而自动保留。

**步骤 4：理论比较与选择性编码。** 轴向范畴形成后，研究团队将与 Taylor（1990）的主观态势感知、SART 的注意需求、注意供给与理解，以及 Endsley（1995b）的感知、理解和预期进行反复比较。感知、理解和预期在此用于内容覆盖审计，而不是强制形成三个最终维度。比较将回答五个问题：该范畴是否表达用户对自身任务认识的程度判断；是否只是客观任务事实；是否只是影响这种认识的条件；是否是认识形成后的态度或行为；是否只是智能体能力或界面的属性。属于 CASA 的范畴还需说明它是对一般态势感知内容的具体化，还是由编程智能体代理行动与软件制品耦合带来的新增内容。

**步骤 5：负例与替代解释检验。** 研究将主动查找能够推翻初步结构的材料。例如，用户表示自己完全不知道智能体改了什么但仍相信结果时，应分别编码为低 CASA 与高信任；用户拥有清楚的差异视图却仍然无法说明变化意义时，应编码为高信息可见性与低 CASA；用户拥有停止和回滚权限却不知道何时应使用时，应编码为具有控制机制但 CASA 较低。相反，用户仅陈述智能体修改了三个文件而没有评价自己是否了解这些变化时，不据此推断 CASA 高低。只有能够经受这些边界检验的范畴才进入候选构念结构。

### 4.4 构念结构与定义验证

定性阶段结束后，研究团队将依据一阶代码和轴向范畴修订 CASA 的概念定义。清晰的概念定义需要明确构念所指对象、核心属性、适用条件及其与相邻概念的区别（Podsakoff et al., 2016）。修订后的 CASA 定义还将按照个体用户、编程智能体、具体任务和理论功能说明其分析单位、状态对象、时间范围与法则位置（Burton-Jones & Straub, 2006）。研究不会仅因为经验范畴可以对应感知、理解和预期就宣布三维结构成立，也不会仅因为若干范畴在文本中共同出现就宣布它们属于同一构念。

候选维度将经过至少两轮卡片分类。第一轮邀请具有编程智能体实际经验的开发者，根据维度定义把一阶范畴归入候选维度，并允许设置无法归类选项。第二轮邀请信息系统、人机交互和软件工程研究者独立完成同样任务。研究将依据命中率、评判者一致性和争议说明修订定义；如果某些范畴持续跨维度混淆，应优先修改概念边界，而不是只修改名称。

CASA 的测量模型将在内容领域明确后决定。多维构念可能把维度视为潜在构念的表现、共同形成的聚合或不可相互替换的特征组合，不同关系对应不同的理论含义和操作化方式（Law et al., 1998）。若各维度是同一主观状态的可互换表现，删除某一维度不改变构念内涵，并且维度应当高度共变，则可以考虑反映式高阶模型。若各维度共同构成 CASA、不能互换，且删除任一维度会遗漏一种必要任务状态，则应考虑形成式高阶模型（Jarvis et al., 2003; Petter et al., 2007）。模型选择必须基于构念与指标之间的关系，而不能依据哪一种统计模型更容易获得良好拟合。

### 4.5 阶段 1 的预期产出

阶段 1 应形成六项可审计产出：完整的数据筛选流程；一阶代码、轴向范畴和候选维度的数据结构；每个范畴的定义与边界；一般态势感知内容与编程智能体新增内容的比较表；前因、构念内容和后果的分类表；支持和挑战最终结构的正例与负例。数据结构将保留从用户表达、一阶代码到理论范畴的推导过程，以便审稿者检查经验材料与构念主张之间的联系（Gioia et al., 2013）。只有这些产出能够表明编程智能体情境确实产生了稳定且有理论意义的内容差异时，研究才进入新量表开发。

## 5 阶段 2：CASA 量表开发与验证

### 5.1 阶段 2A：建立初始量表

初始题项将依据成熟的量表开发程序，来自阶段 1 中用户描述任务认识的语言、修订后的 CASA 及各维度定义，以及 SART 和其他态势感知文献中的相关表达（Hinkin, 1998; MacKenzie et al., 2011）。题项不会直接测量界面是否提供差异视图、日志或通知，因为这些属于潜在前因；也不会询问用户是否信任、喜欢或能够控制智能体，因为这些属于相邻构念或后果。每个题项都将锚定一次刚刚完成或能够清楚回忆的具体任务，例如使用在刚才的任务中作为共同时间边界。

研究团队将生成大于最终量表需求的题项池，使每个候选维度在净化前具有充分内容覆盖。题项将避免同时包含多个不同判断对象。例如，了解智能体做了什么并理解代码为什么变化同时包含行动认识和意义理解，不应在维度尚未确定时写入同一题项。研究将使用 ITEM Ontology 对题项中的对象、被测属性、限定词和反应集合进行语义审计，以识别双重问题、对象漂移和限定范围不一致（Larsen et al., 2026）。

内容效度评估将分为人类判断与人工智能辅助检查两部分。首先，由编程智能体用户和相关领域学者独立判断每个题项是否属于目标维度、是否代表必要内容、是否与其他维度混淆。其次，可以使用 RATER 对题项与定义的语义对应和构念区分提供补充诊断，但人工智能结果不替代专家判断（Pillet et al., 2026）。随后，研究将使用认知访谈检验参与者如何理解题项对象、时间边界、程度限定和反应选项，并根据参与者复述与作答理由修订项目。

经过内容效度和认知访谈后，题项将进入多轮卡片分类。评判者获得 CASA、候选维度和主要相邻构念的定义，并把题项分配到最符合的类别或无法判断类别。研究将报告题项归类命中率、评判者一致性和每轮删除或改写原因。卡片分类不仅用于删除弱题项，也用于发现构念定义本身是否仍然含混（Moore & Benbasat, 1991）。

### 5.2 阶段 2B：量表净化与结构验证

第一轮调查将面向近期实际使用过编程智能体并能回忆具体任务的用户。筛选问题需要确认参与者使用的是能够读取项目、修改软件制品或调用工具的编程智能体，而不是仅使用一次代码补全或一般对话模型。参与者将先描述最近一次任务的工具、目标、持续时间和主要行动，再回答 CASA 题项，以降低不同任务参照造成的测量误差。

第一轮独立样本将用于探索性因子分析和初步题项净化。样本量原则上不低于 500，并在最终题项数和因子结构确定后通过功效分析调整。研究将检查题项分布、缺失、极端反应、项目间冗余和探索性结构。题项删除不能只依据载荷，而要同时确认删除后是否仍然覆盖构念内容。若定性结构与探索性结构不一致，研究团队需要回到原始代码和定义解释差异，而不能只服从统计输出。

第二轮独立样本将用于验证性因子分析和竞争测量模型比较。研究将比较单因子模型、理论提出的多维模型以及合理的高阶模型，并依据最终测量理论选择反映式或形成式估计方法。反映式维度将检验标准化载荷、复合信度、omega、平均方差提取和区分效度；形成式部分将检验指标权重、冗余和多重共线性。模型拟合将报告适合估计方法的指标，不把某一个阈值作为构念正确的充分证据。

第二轮还将检验 CASA 与人工智能信任、感知透明度、感知控制、认知负荷和一般主观态势感知之间的区分效度。CASA 应与这些变量相关，但不能因为相关性过高而失去独立内容。研究还将比较不同编程经验、智能体经验、CLI 与 IDE 交互形态以及不同任务类型下的测量不变性。若量表只能在某一种产品或界面中成立，构念边界需要相应收窄。

### 5.3 阶段 2C：量表复核、法则网络与预测比较

第三轮独立数据将重新检验最终量表，并尽可能采用两时点设计降低共同方法偏差。第一时点要求参与者围绕最近一次具体任务报告 CASA、一般主观态势感知和相邻构念；第二时点测量该次使用后的感知控制、满意度和持续使用意愿。问卷还将依据最终研究设计加入理论上无关的标记变量或共同方法因子，配合时间分离检验共同方法方差，而不依赖单一的 Harman 单因子检验（Podsakoff et al., 2003）。若研究条件允许，还可以从产品日志或任务记录获得使用持续时间、介入和任务完成等行为信息，但这些数据不替代主观结果变量。

法则网络将围绕已经在论文开篇明确的结果链展开：CASA 为用户作出继续、介入和接受判断提供认知基础，可能进一步影响感知控制和满意度，并关系到持续使用意愿。构念开发论文的主要目的不是一次检验所有可能前因，而是证明 CASA 能够在理论上合理的网络中发挥作用。感知透明度、任务复杂性、用户经验和认知负荷可作为前因或控制变量；人工智能信任用于检验区分效度和替代解释。

增量效度检验将使用相同结果变量比较多组基准模型。第一组基准采用 Taylor（1990）的十维 SART，并仅把任务指称最小程度地调整为刚刚完成的编程智能体任务；三维 SART 及其传统合成分数将作为替代计分方式，同时依据 Bolton 等（2022）的提醒报告各组成部分结果。第二组基准将在独立于 Reddit 编码结果的条件下，由软件开发与态势感知专家依据统一任务分析形成简短的任务特定主观态势感知项目，以降低 CASA 仅因具有具体措辞而获得优势的可能。所有基准项目均需经过认知访谈与内容效度评估，不能直接把航空术语替换为编程术语。CASA 模型将在控制上述基准测量后解释感知控制、满意度和持续使用意愿，并通过解释方差、信息准则、嵌套模型差异及保留样本预测误差评价增量。只有 CASA 在保持区分效度的同时稳定增加解释或预测能力，情境特定构念的开发价值才得到支持。

为区分主观任务认识和客观任务知识，研究还将设计一个统一任务的实验或任务回放子研究。研究团队将在实验前固定初始仓库、任务目标、工具权限和可接受结果，并由智能体日志、版本差异、命令输出和测试结果共同建立每次实际行动轨迹的任务真值。参与者在任务结束后先填写 CASA，随后在隐藏界面线索的任务回放中回答与该次实际轨迹相匹配的状态问题；该顺序避免用探测问题提示 CASA 作答，也不机械采用 SAGAT 的任务中途冻结程序。研究将检验高 CASA 是否通常伴随更准确的任务状态判断，以及何种界面或任务条件下出现高主观、低客观或低主观、高客观的脱节。客观问题只提供校准和效标证据，不用于把 CASA 重新定义为任务问题正确率。

## 6 构念开发的判断门槛

本研究不能预设 CASA 必然是一个成立的新构念。阶段 1 和阶段 2 将设置以下判断门槛：

1. 如果定性范畴完全落入 SART 或一般态势感知的既有内容，且没有形成稳定的编程智能体任务内容，则研究应定位为一般主观态势感知量表的情境适配，而不是新构念开发。
2. 如果候选维度主要描述信息是否可见、界面是否易用或用户是否信任智能体，则应把它们分别放回透明度、可用性或信任，而不能通过更名纳入 CASA。
3. 如果所谓编程智能体特定内容只存在于单一产品或单一交互界面，应收窄研究对象，或将其作为产品特征而非普遍维度。
4. 如果 CASA 与一般主观态势感知、感知控制或信任缺乏区分效度，应修订定义与量表，必要时终止新构念主张。
5. 如果 CASA 没有表现出相对于一般主观态势感知的内容优势、增量效度或诊断价值，则不能声称开发情境特定构念改善了理论解释。

## 7 与 Chen 等（2024）的逐段逻辑对应

| Chen 等（2024）的功能位置 | 原文承担的论证功能 | CASA 稿对应内容 |
| --- | --- | --- |
| C19 | 说明新技术如何改变交互，并由对象变化引出研究现象 | 编程智能体由生成内容转向代理行动；用户需要认识任务推进状态 |
| C21 | 逐项比较新情境与母理论原情境的结构差异 | 代理行动、分布式状态、可执行制品、间接经验和异步推进 |
| C23 | 选择唯一母构念、给出定义并说明现实后果 | 以个体态势感知为基础定义 CASA，连接感知控制、满意度与持续使用 |
| C25-C27 | 回顾母构念在其他情境的量表，说明哪些可用、哪些不适用 | 比较 SART、SAGAT、信息安全态势感知、仪表盘研究和编程交互研究 |
| C29 | 说明情境量表的理论与实践必要性 | 区分任务表现与用户任务认识，并识别用户主观上较难把握的任务方面 |
| C31 | 将情境特征、现实重要性和测量缺口汇合为少量研究问题 | 一个问题开发维度与量表，一个问题检验相对一般 SA 的增量价值 |
| C33-C35 | 简述定性到定量的研究过程，并解释理论如何参与编码 | Reddit 开放与轴向编码；与 SART/SA 反复比较；多轮量表验证 |
| C37-C39 | 分别提出构念、理论扩展和实践工具贡献 | CASA 内容与量表；代理行动下的主观 SA；产品状态呈现诊断工具 |
| C45-C55 | 系统比较既有构念和量表，形成宽度、深度和实证三类缺口 | 对象遗漏、前因混入、主客观混淆、相关现象碎片化和缺少量表 |
| C59-C63 | 说明母理论为何可用，又为何必须扩展 | SART 的构念引出与主观测量适用，但航空内容和需求-供给结构不能照搬 |
| C69-C79 | 说明混合方法必要性并概括两个阶段 | 定性识别内容，定量验证量表、法则网络和相对预测能力 |

## 8 参考文献

- Bainbridge, L. (1983). Ironies of automation. *Automatica, 19*(6), 775-779. https://doi.org/10.1016/0005-1098(83)90046-8
- Baird, A., & Maruping, L. M. (2021). The next generation of research on IS use: A theoretical framework of delegation to and from agentic IS artifacts. *MIS Quarterly, 45*(1), 315-341. https://doi.org/10.25300/MISQ/2021/15882
- Barke, S., James, M. B., & Polikarpova, N. (2023). Grounded Copilot: How programmers interact with code-generating models. *Proceedings of the ACM on Programming Languages, 7*(OOPSLA1), Article 78, 85-111. https://doi.org/10.1145/3586030
- Baronas, A.-M. K., & Louis, M. R. (1988). Restoring a sense of control during implementation: How user involvement leads to system acceptance. *MIS Quarterly, 12*(1), 111-123. https://doi.org/10.2307/248811
- Bauer, K., von Zahn, M., & Hinz, O. (2023). Expl(AI)ned: The impact of explainable artificial intelligence on users' information processing. *Information Systems Research, 34*(4), 1582-1602. https://doi.org/10.1287/isre.2023.1199
- Bhattacherjee, A. (2001). Understanding information systems continuance: An expectation-confirmation model. *MIS Quarterly, 25*(3), 351-370. https://doi.org/10.2307/3250921
- Bolton, M. L., Biltekoff, E., & Humphrey, L. R. (2022). The level of measurement of subjective situation awareness and its dimensions in the Situation Awareness Rating Technique (SART). *IEEE Transactions on Human-Machine Systems, 52*(6), 1147-1154. https://doi.org/10.1109/THMS.2021.3121960
- Burton-Jones, A., & Straub, D. W., Jr. (2006). Reconceptualizing system usage: An approach and empirical test. *Information Systems Research, 17*(3), 228-246. https://doi.org/10.1287/isre.1060.0096
- Chen, Q., Gong, Y., Keil, M., Liu, S., & Lu, Y. (2024). Conceptualization and measurement of voice-interaction usability: The development of cooperative principle theory for smart product use. *MIS Quarterly, 48*(3), 1009-1046. https://doi.org/10.25300/MISQ/2023/17525
- Corbin, J. M., & Strauss, A. (1990). Grounded theory research: Procedures, canons, and evaluative criteria. *Qualitative Sociology, 13*(1), 3-21. https://doi.org/10.1007/BF00988593
- Dennis, A. R., Lakhiwal, A., & Sachdeva, A. (2023). AI agents as team members: Effects on satisfaction, conflict, trustworthiness, and willingness to work with. *Journal of Management Information Systems, 40*(2), 307-337. https://doi.org/10.1080/07421222.2023.2196773
- Dhanorkar, S., Passi, S., & Vorvoreanu, M. (2026). Human oversight of agentic systems in practice: Examining the oversight work, challenges, and heuristics of developers using software agents. In *Proceedings of the 2026 ACM Conference on Fairness, Accountability, and Transparency* (pp. 6438-6465). Association for Computing Machinery. https://doi.org/10.1145/3805689.3812402
- Endsley, M. R. (1995a). Measurement of situation awareness in dynamic systems. *Human Factors, 37*(1), 65-84. https://doi.org/10.1518/001872095779049499
- Endsley, M. R. (1995b). Toward a theory of situation awareness in dynamic systems. *Human Factors, 37*(1), 32-64. https://doi.org/10.1518/001872095779049543
- Endsley, M. R., & Kiris, E. O. (1995). The out-of-the-loop performance problem and level of control in automation. *Human Factors, 37*(2), 381-394. https://doi.org/10.1518/001872095779064555
- Endsley, M. R., Selcon, S. J., Hardiman, T. D., & Croft, D. G. (1998). A comparative analysis of SAGAT and SART for evaluations of situation awareness. *Proceedings of the Human Factors and Ergonomics Society Annual Meeting, 42*(1), 82-86. https://doi.org/10.1177/154193129804200119
- Endsley, M. R. (2020). The divergence of objective and subjective situation awareness: A meta-analysis. *Journal of Cognitive Engineering and Decision Making, 14*(1), 34-53. https://doi.org/10.1177/1555343419874248
- Endsley, M. R. (2021). A systematic review and meta-analysis of direct objective measures of situation awareness: A comparison of SAGAT and SPAM. *Human Factors, 63*(1), 124-150. https://doi.org/10.1177/0018720819875376
- Endsley, M. R. (2023). Supporting human-AI teams: Transparency, explainability, and situation awareness. *Computers in Human Behavior, 140*, 107574. https://doi.org/10.1016/j.chb.2022.107574
- Ferdowsi, K., Huang, R., James, M. B., Polikarpova, N., & Lerner, S. (2024). Validating AI-generated code with live programming. In *Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems* (Article 143, pp. 1-8). Association for Computing Machinery. https://doi.org/10.1145/3613904.3642495
- Franzke, A. S., Bechmann, A., Zimmer, M., Ess, C., & the Association of Internet Researchers. (2020). *Internet research: Ethical guidelines 3.0*. Association of Internet Researchers. https://aoir.org/reports/ethics3.pdf
- Gioia, D. A., Corley, K. G., & Hamilton, A. L. (2013). Seeking qualitative rigor in inductive research: Notes on the Gioia methodology. *Organizational Research Methods, 16*(1), 15-31. https://doi.org/10.1177/1094428112452151
- Gliniecka, M. (2023). The ethics of publicly available data research: A situated ethics framework for Reddit. *Social Media + Society, 9*(3). https://doi.org/10.1177/20563051231192021
- Gregor, S., & Benbasat, I. (1999). Explanations from intelligent systems: Theoretical foundations and implications for practice. *MIS Quarterly, 23*(4), 497-530. https://doi.org/10.2307/249487
- Hinkin, T. R. (1998). A brief tutorial on the development of measures for use in survey questionnaires. *Organizational Research Methods, 1*(1), 104-121. https://doi.org/10.1177/109442819800100106
- Hoehle, H., & Venkatesh, V. (2015). Mobile application usability: Conceptualization and instrument development. *MIS Quarterly, 39*(2), 435-472. https://doi.org/10.25300/MISQ/2015/39.2.08
- Hong, W., Chan, F. K. Y., Thong, J. Y. L., Chasalow, L. C., & Dhillon, G. (2014). A framework and guidelines for context-specific theorizing in information systems research. *Information Systems Research, 25*(1), 111-136. https://doi.org/10.1287/isre.2013.0501
- Jaeger, L., & Eckhardt, A. (2021). Eyes wide open: The role of situational information security awareness for security-related behaviour. *Information Systems Journal, 31*(3), 429-472. https://doi.org/10.1111/isj.12317
- Jarvis, C. B., MacKenzie, S. B., & Podsakoff, P. M. (2003). A critical review of construct indicators and measurement model misspecification in marketing and consumer research. *Journal of Consumer Research, 30*(2), 199-218. https://doi.org/10.1086/376806
- Kretsou, M., Arvanitou, E.-M., Ampatzoglou, A., Deligiannis, I., & Gerogiannis, V. C. (2021). Change impact analysis: A systematic mapping study. *Journal of Systems and Software, 174*, 110892. https://doi.org/10.1016/j.jss.2020.110892
- Kumar, A., Bajpai, Y., Gulwani, S., Soares, G., & Murphy-Hill, E. (2025). Why AI agents still need you: Findings from developer-agent collaborations in the wild. In *2025 IEEE/ACM 40th International Conference on Automated Software Engineering* (pp. 432-444). IEEE. https://doi.org/10.1109/ASE63991.2025.00043
- Kuo, N., Sergeyuk, A., Chen, V., & Izadi, M. (2026). Developer interaction patterns with proactive AI: A five-day field study. In *Proceedings of the 31st International Conference on Intelligent User Interfaces* (pp. 264-275). Association for Computing Machinery. https://doi.org/10.1145/3742413.3789148
- Larsen, K. R., Mueller, R. M., Bonaretti, D., Fischer-Preßler, D., Burleson, J. J., Singh, N., Parsons, J., Pillet, J.-C., Sang, L., & Zhang, Z. (2026). The ITEM Ontology: A tool to elucidate the anatomy of psychometric indicators. *Information Systems Research, 37*(1), 549-567. https://doi.org/10.1287/isre.2023.0257
- Law, K. S., Wong, C.-S., & Mobley, W. H. (1998). Toward a taxonomy of multidimensional constructs. *Academy of Management Review, 23*(4), 741-755. https://doi.org/10.5465/amr.1998.1255636
- Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors, 46*(1), 50-80. https://doi.org/10.1518/hfes.46.1.50_30392
- Lewis, B. R., Templeton, G. F., & Byrd, T. A. (2005). A methodology for construct development in MIS research. *European Journal of Information Systems, 14*(4), 388-400. https://doi.org/10.1057/palgrave.ejis.3000552
- MacKenzie, S. B., Podsakoff, P. M., & Podsakoff, N. P. (2011). Construct measurement and validation procedures in MIS and behavioral research: Integrating new and existing techniques. *MIS Quarterly, 35*(2), 293-334. https://doi.org/10.2307/23044045
- Moens, L. L., Lydon, S., Cucurachi, S., O'Connor, P., Sauter, T. C., Töndury, G.-A., & Manser, T. (2026). Measuring situation awareness: A meta-review across domains. *Human Factors, 68*(5). https://doi.org/10.1177/00187208251412110
- Moore, G. C., & Benbasat, I. (1991). Development of an instrument to measure the perceptions of adopting an information technology innovation. *Information Systems Research, 2*(3), 192-222. https://doi.org/10.1287/isre.2.3.192
- Mozannar, H., Bansal, G., Fourney, A., & Horvitz, E. (2024). Reading between the lines: Modeling user behavior and costs in AI-assisted programming. In *Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems* (Article 142, pp. 1-16). Association for Computing Machinery. https://doi.org/10.1145/3613904.3641936
- Nadj, M., Maedche, A., & Schieder, C. (2020). The effect of interactive analytical dashboard features on situation awareness and task performance. *Decision Support Systems, 135*, 113322. https://doi.org/10.1016/j.dss.2020.113322
- Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A model for types and levels of human interaction with automation. *IEEE Transactions on Systems, Man, and Cybernetics Part A: Systems and Humans, 30*(3), 286-297. https://doi.org/10.1109/3468.844354
- Petter, S., Straub, D., & Rai, A. (2007). Specifying formative constructs in information systems research. *MIS Quarterly, 31*(4), 623-656. https://doi.org/10.2307/25148814
- Pillet, J.-C., Larsen, K. R., Dobolyi, D., Queiroz, M., Handler, A., Arnulf, J. K., & Sharma, R. (2026). AI-augmented content validation in behavioral research: Development and evaluation of the RATER system. *MIS Quarterly, 50*(1), 59-86. https://doi.org/10.25300/MISQ/2025/18946
- Podsakoff, P. M., MacKenzie, S. B., Lee, J.-Y., & Podsakoff, N. P. (2003). Common method biases in behavioral research: A critical review of the literature and recommended remedies. *Journal of Applied Psychology, 88*(5), 879-903. https://doi.org/10.1037/0021-9010.88.5.879
- Podsakoff, P. M., MacKenzie, S. B., & Podsakoff, N. P. (2016). Recommendations for creating better concept definitions in the organizational, behavioral, and social sciences. *Organizational Research Methods, 19*(2), 159-203. https://doi.org/10.1177/1094428115624965
- Rose, J., Bearman, C., & Dorrian, J. (2018). The Low-Event Task Subjective Situation Awareness (LETSSA) technique: Development and evaluation of a new subjective measure of situation awareness. *Applied Ergonomics, 68*, 273-282. https://doi.org/10.1016/j.apergo.2017.12.006
- Schuetz, S., & Venkatesh, V. (2020). Research perspectives: The rise of human machines: How cognitive computing systems challenge assumptions of user-system interaction. *Journal of the Association for Information Systems, 21*(2), 460-482. https://doi.org/10.17705/1jais.00608
- Selkowitz, A. R., Lakhmani, S. G., & Chen, J. Y. C. (2017). Using agent transparency to support situation awareness of the Autonomous Squad Member. *Cognitive Systems Research, 46*, 13-25. https://doi.org/10.1016/j.cogsys.2017.02.003
- Stanton, N. A., Salmon, P. M., Walker, G. H., & Green, D. (2006). Situation awareness measurement: A review of applicability for C4i environments. *Applied Ergonomics, 37*(2), 225-238. https://doi.org/10.1016/j.apergo.2005.02.001
- Taylor, R. M. (1990). Situational awareness rating technique (SART): The development of a tool for aircrew systems design. In *Situational Awareness in Aerospace Operations* (AGARD-CP-478, pp. 3/1-3/17). NATO Advisory Group for Aerospace Research and Development.
- Venkatesh, V., Brown, S. A., & Bala, H. (2013). Bridging the qualitative-quantitative divide: Guidelines for conducting mixed methods research in information systems. *MIS Quarterly, 37*(1), 21-54. https://doi.org/10.25300/MISQ/2013/37.1.02
- Wang, R., Cheng, R., Ford, D., & Zimmermann, T. (2024). Investigating and designing for trust in AI-powered code generation tools. In *Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency* (pp. 1475-1493). Association for Computing Machinery. https://doi.org/10.1145/3630106.3658984
- Xu, J., Benbasat, I., & Cenfetelli, R. T. (2014). The nature and consequences of trade-off transparency in the context of recommendation agents. *MIS Quarterly, 38*(2), 379-406. https://doi.org/10.25300/MISQ/2014/38.2.03
