# 编程智能体态势感知的概念化与测量

> 本稿用于规划一篇以构念开发为核心的独立期刊论文。第 1 至第 3 节逐段对应 Chen 等（2024）的论证功能及引文分工，但不复写其原句。相关论据优先来自 `database/ALL_AIS_Basket_11.csv` 中的原始摘要、态势感知经典文献以及已经正式发表的近期编程智能体研究。正文中的 HTML 注释标识与 Chen 等文章的功能位置，渲染时不显示。第 4 节以后仍为预期实施方案，不得在数据收集完成前表述为已经取得的结果。

## 拟定题目

**中文题目** 面向代理式软件开发任务的编程智能体态势感知概念化与测量

**英文题目** *Conceptualization and Measurement of Coding-Agent Situation Awareness for Agentic Software Development Tasks*

## 摘要（研究计划版）

编程智能体能够围绕用户目标规划步骤、调用工具并连续修改软件制品，由此把人与信息系统的关系从直接操作扩展到任务委托。用户能否形成对智能体行动所生成的任务状态的主观认识，是其作出继续委托、介入调整和接受结果等判断的认知基础，但现有研究尚未形成用于描述和测量这一认识的编程智能体特定构念。本文拟以个体层面的主观态势感知为唯一基础构念，采用顺序探索型混合方法开发编程智能体态势感知。第一阶段将编码 Reddit 中用户对真实编程智能体任务的公开叙述，并依据动态态势感知理论组织和比较经验范畴，以界定构念领域及潜在维度。第二阶段将通过题项生成、内容效度评估、认知访谈、多轮独立样本检验和法则网络验证开发 CASA 量表。预期研究将说明传统主观态势感知在代理式软件开发任务中遗漏了哪些任务状态内容，形成研究编程智能体个体体验的测量工具，并为行动、制品变化和执行证据的界面呈现提供诊断依据。

**关键词** 编程智能体；态势感知；构念开发；量表开发；二手在线文本；混合方法

## 1 引言

生成式人工智能正在成为软件开发中具有重要经济潜力的技术。<!-- C19.1 --> McKinsey Global Institute（2023）将软件工程列为生成式人工智能价值最集中的四类企业职能之一，并估计其直接生产率影响可能相当于软件工程年度支出的 20% 至 45%。<!-- C19.2 --> Stack Overflow（2025）的开发者调查显示，84% 的相关受访者已经使用或计划使用人工智能开发工具；在工作中使用人工智能代理的软件开发者中，84% 将其用于软件开发。<!-- C19.3 --> 与此同时，人工智能正在使信息系统由响应用户操作的工具转变为能够接受目标、发起行动并适应反馈的能动型制品（Schuetz & Venkatesh, 2020; Baird & Maruping, 2021）。<!-- C19.4 --> 编程智能体体现了这一变化。它能够读取项目材料、分解用户目标、调用编辑器与终端工具、修改软件制品，并依据执行结果继续选择行动（Kumar et al., 2025）。<!-- C19.5 --> 用户由此可以把缺陷修复、测试生成、代码重构和项目维护等多步骤任务委托给系统，而不必预先指定每一次操作。<!-- C19.6 -->

编程智能体能否形成稳定的使用价值还取决于用户与系统如何共同推进任务。<!-- C19.7 --> Kumar 等（2025）观察 19 名开发者解决 33 个真实软件问题后发现，渐进处理问题并持续调整智能体工作的参与者更容易完成任务，而一次性委托和低互动方式较少成功。<!-- C19.8 --> Dhanorkar 等（2026）对 17 名资深开发者的访谈进一步表明，用户会在事前限制、共同规划、实时查看和事后复核等阶段持续处理智能体工作，并在代码难以审查时借助计划与测试结果判断任务状况。<!-- C19.9 --> 这些发现表明，任务委托减少了用户的直接操作，但编程智能体的使用过程仍要求用户判断任务如何推进、是否出现偏差以及结果能否接受。<!-- C19.10 --> 它们由此揭示了编程智能体使用中的一项具体要求，用户在委托行动后仍需形成足以支持后续判断的任务认识。<!-- C19.11 -->

然而，编程智能体任务中的状态认识难以由传统操作环境中的态势感知直接表示。<!-- C21.1 --> 经典态势感知研究主要考察操作者对外部环境和被控系统状态的感知、理解与预期，相关任务通常具有研究者可以预先分析的状态要素和目标（Endsley, 1995a, 1995b）。<!-- C21.2 --> 自动化研究虽然把部分信息处理或行动功能交给机器，其理论通常仍以预先分配的人机功能和自动化层级为基础（Parasuraman et al., 2000）。<!-- C21.3 --> 编程智能体则围绕开放目标选择行动，并通过修改软件制品持续生成新的任务状态（Baird & Maruping, 2021; Kumar et al., 2025）。<!-- C21.4 --> 相关状态同时分布在智能体的计划与行动轨迹、相互依赖的软件制品以及测试和运行证据之中，用户需要把不同载体中的线索联系到同一任务目标（Kretsou et al., 2021; Dhanorkar et al., 2026）。<!-- C21.5 --> 任务委托还使用户不再亲自执行每一步操作，其状态认识依赖系统保留和呈现的行动痕迹，并可能在任务已经推进后重新形成（Endsley & Kiris, 1995; Baird & Maruping, 2021）。<!-- C21.6 --> 编程智能体由此改变了任务状态的生成方式、存在形式以及用户接触状态的方式，经典态势感知需要在这一情境中得到进一步发展。<!-- C21.7 -->

主观态势感知为描述这种任务认识提供了概念基础。<!-- C23.1 --> Taylor（1990）从个体对影响任务成功的事件、因素和变量所具有的知识、认知与预期出发，发展了主观态势感知及其测量。<!-- C23.2 --> 本文将编程智能体态势感知定义为个体用户在一次具体编程智能体任务中，对自己能够认识智能体代理行动所形成的任务相关状态及其近期发展的程度判断。<!-- C23.3 --> 任务相关状态包括智能体采取的行动、软件制品发生的变化、执行结果提供的证据以及这些内容与用户任务目标之间的关系。<!-- C23.4 --> 较高的 CASA 表示用户感觉自己能够形成连贯且可更新的任务认识，较低的 CASA 表示用户难以判断任务已经发生什么、当前状态意味着什么或任务接下来可能如何发展。<!-- C23.5 --> Endsley（1995b）的动态态势感知理论将在后文用于组织这种认识所涉及的感知、理解和近期预期。<!-- C23.6 -->

CASA 所描述的任务认识与用户在编程智能体任务中需要作出的后续判断具有明确的理论联系。<!-- C23.7 --> 人工智能研究已将态势感知视为用户与自主系统有效互动以及形成适当信任的重要认知条件（Selkowitz et al., 2017; Endsley, 2023）。<!-- C23.8 --> 信息系统研究也表明，情境态势感知会影响用户的任务评价和后续行为（Jaeger & Eckhardt, 2021），而系统功能带来的任务表现提升可能与用户态势感知下降同时发生（Nadj et al., 2020）。<!-- C23.9 --> 这些研究说明，仅以编程智能体是否完成任务评价其使用效果，会遗漏用户是否感觉自己了解任务这一使用过程。<!-- C23.10 --> 据此，本文预期 CASA 可能构成用户决定继续委托、补充信息、介入调整或接受结果的认知基础，并可能进一步影响其感知控制和使用满意度。<!-- C23.11 --> 既有信息系统研究已经建立感知控制与系统接受之间的联系，以及满意度对持续使用意愿的影响（Baronas & Louis, 1988; Bhattacherjee, 2001）。<!-- C23.12 --> 识别 CASA 的构成并形成有效测量，将为检验这些预期关系和理解编程智能体的持续使用提供基础。<!-- C23.13 -->

态势感知已经在航空、自动化、列车驾驶、决策支持和信息安全等动态任务中得到研究，不同情境也形成了不同的概念内容与测量方式。<!-- C25.1 --> Taylor（1990）依据空勤人员的情境描述和构念判断开发 SART，以注意需求、注意供给和理解评价个体对自身态势感知的主观判断。<!-- C25.2 --> Endsley（1995a, 1995b）以任务分析为基础发展 SAGAT，通过暂停任务并询问预先确定的状态问题评价操作者实际掌握的任务信息。<!-- C25.3 --> 当通用 SART 难以适应低事件列车驾驶时，Rose 等（2018）根据列车驾驶的信息要求开发了 LETSSA。<!-- C25.4 --> 在信息系统领域，Jaeger 和 Eckhardt（2021）将态势感知情境化为个体面对网络钓鱼威胁时的信息安全态势感知，Nadj 等（2020）则检验了分析仪表盘功能对决策者态势感知的影响。<!-- C25.5 --> 这些研究说明，态势感知可以跨情境研究，但其内容和测量需要与特定用户面对的任务状态相一致（Stanton et al., 2006; Moens et al., 2026）。<!-- C25.6 -->

既有测量只能部分表示编程智能体任务中的主观态势感知。<!-- C27.1 --> SART 的不稳定性、复杂性、信息数量、注意需求和注意供给反映航空任务及操作者面对的信息条件，但没有区分用户是否了解智能体采取了什么行动、哪些软件制品发生了变化，以及执行证据对任务目标意味着什么（Taylor, 1990）。<!-- C27.2 --> SAGAT 能够通过预定状态问题评价用户掌握的任务真值，却不直接测量用户对自身任务认识的主观判断，也难以用一组固定问题覆盖由智能体行动展开的开放任务轨迹（Endsley, 1995a, 2021）。<!-- C27.3 --> 自主智能体透明度研究已经关注用户对智能体行动、理由和未来状态的认识，但其既有测量没有处理智能体行动与可执行软件制品变化及运行证据之间的关系（Selkowitz et al., 2017）。<!-- C27.4 --> 编程智能体用户需要从按时间展开的行动记录、跨文件变化和执行反馈中形成对整个任务的认识，这些内容不能由航空或一般自主智能体量表中的对象名称替换得到。<!-- C27.5 --> 因此，编程智能体情境需要重新识别主观态势感知的具体内容，并据此形成具有内容效度的测量工具。<!-- C27.6 -->

发展 CASA 构念及量表对于推进编程智能体研究和改进产品设计具有重要意义。<!-- C29.1 --> 情境化理论只有在新情境揭示一般构念未能表达的内容或关系时才具有理论价值，情境特定量表也需要证明其具有更准确的内容覆盖和经验效度（Hong et al., 2014; Hoehle & Venkatesh, 2015）。<!-- C29.2 --> 经过验证的 CASA 量表可以为不同用户、任务和产品提供共同的测量单位，并用于检验界面、任务和用户因素如何影响用户的任务认识，以及这种认识如何连接到感知控制、满意度和持续使用。<!-- C29.3 --> 现有研究分别观察交互行为、验证投入、信任和任务结果，CASA 为检验这些现象是否通过用户对任务状态的认识发生联系提供了一条共同的理论与测量路径。<!-- C29.4 --> 对产品设计而言，CASA 还可用于评价行动记录、文件差异、执行证据、检查点和任务通知是否帮助用户形成任务认识，并识别用户主观上最难把握的任务方面。<!-- C29.5 -->

综合编程智能体任务状态的独特结构、CASA 对使用判断的重要性以及现有文献在概念化和测量方面的缺口，本文拟回答两个研究问题。<!-- C31.1 -->

**研究问题 1　CASA 包含哪些维度，应当如何测量这些维度？**<!-- C31.2 -->

**研究问题 2　与一般主观态势感知测量相比，CASA 对感知控制、满意度和持续使用意愿是否具有增量解释效度和预测效度？**<!-- C31.3 -->

本文拟采用顺序探索型混合方法，先开展定性构念开发，再开展定量量表开发与验证（Venkatesh et al., 2013）。<!-- C33.1 --> 第一阶段将收集 Reddit 中用户关于真实编程智能体任务的公开帖子和评论，采用开放编码和轴向编码识别用户认识或难以认识任务状态时涉及的经验范畴（Corbin & Strauss, 1990）。<!-- C33.2 --> 编码结果将与 Taylor（1990）的主观态势感知传统反复比较，并以 Endsley（1995b）的动态态势感知理论组织高阶内容和区分前因、构念与结果。<!-- C33.3 --> 这种理论与数据的反复比较既避免将航空量表直接移植到软件开发，也避免仅凭用户评论中出现频繁的词语形成缺乏理论边界的分类。<!-- C33.4 -->

Taylor（1990）的 SART 构念引出过程将指导研究从任务参与者对高、低态势感知情境的比较中识别主观判断内容，Endsley（1995b）的三个态势感知层级则用于比较和组织由数据形成的范畴。<!-- C35.1 --> Reddit 语料将用于识别编程智能体用户实际把哪些行动、变化、证据和发展判断视为掌握或失去任务局面的表现，并检验动态态势感知理论在代理式软件开发中的具体化与扩展空间。<!-- C35.2 --> 第二阶段将依据构念定义、定性范畴和既有态势感知测量形成题项池，并依照成熟的 MIS 构念开发程序开展内容效度、题项分类、多轮独立样本验证和法则效度检验（Moore & Benbasat, 1991; Lewis et al., 2005; MacKenzie et al., 2011）。<!-- C35.3 --> 最后，本文将比较 CASA 与一般主观态势感知测量对感知控制、满意度和持续使用意愿的解释与预测能力。<!-- C35.4 -->

本文拟从三个方面推进现有研究。<!-- C37.1 --> 第一，本文将界定 CASA 的内容领域、构念边界和经验维度，并形成可供后续研究使用的测量工具。<!-- C37.2 --> 第二，本文将通过编程智能体中的任务委托发展个体层面的主观态势感知研究，说明当系统能够自行选择行动时，用户需要认识的任务状态同时包含代理行动及其对软件制品造成的变化。<!-- C37.3 --> 第三，CASA 量表将为比较不同界面、交互模式和任务设计提供诊断工具，支持产品开发者评价行动、变化和执行证据的呈现是否有助于用户形成任务认识。<!-- C39.1 --> 这些贡献将由后续定性材料所显示的内容差异、CASA 与相邻构念的区分效度以及相对于一般主观态势感知的增量效度共同检验。<!-- C39.2 -->

## 2 理论背景

### 2.1 编程智能体态势感知与其他情境中的态势感知

态势感知是动态任务研究中一个成熟的个体层构念。<!-- C45.1 --> Taylor（1990）从主观评价出发，将态势感知表述为个体对影响任务成功的事件、因素和变量所具有的知识、认知与预期，并据此发展了态势感知评定技术。<!-- C45.2 --> Endsley（1995b）从动态决策出发，将态势感知界定为个体对一定时间和空间范围内环境要素的感知、对这些要素意义的理解以及对其近期状态的预期。<!-- C45.3 --> 本文由 Taylor 的主观传统确定 CASA 所测量的个体属性，并在第 2.2 节以 Endsley 理论组织构念内容及其与前因和结果的关系。<!-- C45.4 --> 态势感知的具体内容取决于行动者的目标、任务和所操作的系统，因而不同任务需要识别不同的状态要求并选择与概念化相一致的测量方法（Endsley, 1995a; Stanton et al., 2006; Moens et al., 2026）。<!-- C45.5 --> 这一构念不仅受到人因与人机交互研究的持续关注，也已被引入信息系统支持的运营决策与信息安全行为研究（Nadj et al., 2020; Jaeger & Eckhardt, 2021）。<!-- C45.6 --> 表 1 汇总了与 CASA 概念化和测量直接相关的主要研究传统。<!-- C45.7 -->

**表 1　个体态势感知的主要概念化与测量**

| 研究情境 | 研究对象 | 态势感知的概念内容或任务状态 | 测量方式 | 代表文献 |
| --- | --- | --- | --- | --- |
| 航空系统设计 | 空勤人员 | 对影响任务成功的事件、因素和变量所具有的主观知识、认知与预期；包括不稳定性、复杂性、变量数量、信息质量、注意需求、注意供给与理解 | 从参与者经验引出构念；SART 任务后自评 | Taylor, 1990 |
| 动态决策系统 | 个体操作者 | 对任务相关要素的感知、对要素意义的理解以及对近期状态的预期 | 目标导向任务分析；SAGAT 任务冻结与状态问题 | Endsley, 1995a, 1995b |
| 自动化导航 | 自动化系统操作者 | 在不同自动化水平下对系统状态、任务进展和接管条件的认识 | SAGAT、接管与任务表现 | Endsley & Kiris, 1995 |
| 指挥、控制、通信、计算与情报任务 | 个体操作者 | 随决策目标变化的任务、系统与环境信息 | 对主观评价、观察、探测及表现等测量方法的适用性比较 | Stanton et al., 2006 |
| 低事件列车驾驶 | 列车驾驶员 | 对列车位置、速度、线路信号、运行限制和近期事件的主观认识 | 任务分析；LETSSA；SAGAT 与表现比较 | Rose et al., 2018 |
| 主观与客观态势感知比较 | 动态任务参与者 | 个体对自身认识的评价与其实际掌握的任务信息 | SART 与 SAGAT 同时测量 | Endsley et al., 1998; Endsley, 2020 |
| 客观态势感知测量 | 动态任务参与者 | 依据任务目标预先确定的状态知识 | SAGAT 与 SPAM 的系统综述和元分析 | Endsley, 2021 |
| 自主机器人交互 | 自主智能体操作者 | 对智能体当前行动与计划、行动理由、未来状态及不确定性的认识 | 分层透明度界面；态势感知、信任、工作负荷与表现测量 | Selkowitz et al., 2017 |
| 自主智能体透明度 | 自动化与自主系统操作者 | 系统提供的行动、理由和预测信息是否支持用户形成态势感知 | 17 项实验研究的系统综述；SAGAT、SART、信心及过程概览等测量 | van de Merwe et al., 2024 |
| 人与人工智能协作 | 人工智能使用者 | 对当前任务、人工智能行动和协作关系的认识；区分当前与前瞻性透明度和面向一般知识的解释 | 理论整合与态势感知导向设计 | Endsley, 2023 |
| 交互式运营仪表盘 | 个体决策者 | 对运营问题中当前状态、因果关系和未来结果的认识 | 实验、SAGAT、眼动与任务表现 | Nadj et al., 2020 |
| 网络钓鱼防护 | 个体员工 | 对当前安全威胁情境的注意、解释和风险认识 | 眼动、调查、系统警告与实际应对行为 | Jaeger & Eckhardt, 2021 |
| 跨领域态势感知测量 | 多类动态任务中的个体 | 与研究定义和任务目的相对应的主观评价、观察者评价或探测内容 | 跨领域元综述 | Moens et al., 2026 |

表 1 表明，既有态势感知测量并不适合直接用于编程智能体情境。<!-- C47.1 --> SART 的评价内容反映航空任务中的动态性、复杂性、信息与注意资源；其中注意需求和注意供给还同时描述任务条件与个体资源，而不是只描述个体已经形成的任务认识（Taylor, 1990）。<!-- C47.2 --> Rose 等（2018）发现，长时间低事件的列车驾驶不符合 SART 所隐含的高事件任务条件，因而依据列车位置、速度、信号和未来事件等任务要求另行开发 LETSSA。<!-- C47.3 --> SAGAT 通过任务分析建立问题和正确答案，适合评价参与者实际掌握的预定状态信息，却不直接提供一项跨仓库、跨产品和跨开放任务的主观体验量表（Endsley, 1995a, 2021）。<!-- C47.4 --> 信息安全态势感知和运营仪表盘研究也分别围绕威胁线索与运营决策问题界定状态内容，未涉及能够自行行动并改变软件制品的智能体（Nadj et al., 2020; Jaeger & Eckhardt, 2021）。<!-- C47.5 -->

自主智能体研究与 CASA 更为接近，但仍未提供适用的构念和测量。<!-- C47.6 --> 基于态势感知的智能体透明度研究按当前行动与计划、行动理由以及未来结果与不确定性组织界面信息，这些内容能够支持用户认识自主体，却主要围绕具身智能体在预定任务环境中的状态展开（Selkowitz et al., 2017）。<!-- C47.7 --> 透明度是系统向用户呈现行动及内部过程信息的设计属性，态势感知则是用户基于可获得信息形成的认知状态；实验研究中透明度对态势感知、工作负荷和表现的影响并不一致，进一步说明两者不能相互替代（van de Merwe et al., 2024）。<!-- C47.8 --> 编程智能体任务还要求用户把行动轨迹与代码、配置、测试及运行证据联系到同一开发目标，现有自主智能体量表未表达这种跨软件制品的状态关系。<!-- C47.9 --> 因此，既有文献尚未形成编程智能体态势感知的情境特定维度框架或经过验证的主观量表。<!-- C47.10 -->

随着代码生成工具和编程智能体的普及，研究者已经从多种任务与产品情境考察人工智能辅助编程中的互动、验证、信任和监督。<!-- C51.1 --> 表 2 归纳了与 CASA 内容最接近的正式发表研究，并区分其研究方法、相关属性与已有测量。<!-- C51.2 -->

**表 2　人工智能辅助编程研究中与 CASA 相关的属性**

| 研究对象 | 评价技术 | 与 CASA 相关的属性或发现 | CASA 量表 | 代表文献 |
| --- | --- | --- | --- | --- |
| 程序员使用代码生成模型 | 访谈、观察与扎根分析 | 加速与探索两种互动模式；意图表达、代码检查与模式切换 | 无 | Barke et al., 2023 |
| 人工智能辅助编程活动 | 行为序列与时间成本建模 | 阅读、验证、编辑、提示和等待等活动状态及其成本 | 无 | Mozannar et al., 2024 |
| 人工智能生成代码的验证 | 对照实验与交互日志 | 持续呈现运行时值改变用户检查和理解代码建议的条件 | 无 | Ferdowsi et al., 2024 |
| 人工智能代码生成工具 | 开发者访谈与设计分析 | 对系统能力和具体建议的评价、信任形成与界面支持不足 | 无 | Wang et al., 2024 |
| 开发者与软件智能体解决真实问题 | 19 名开发者、33 个真实软件问题的现场观察 | 渐进解决、持续互动、调试与测试中的协作困难 | 无 | Kumar et al., 2025 |
| 开发者监督软件智能体 | 17 名资深开发者访谈 | 事前限制、共同规划、实时查看、事后复核以及代码审查困难 | 无 | Dhanorkar et al., 2026 |
| 主动式人工智能开发工具 | 15 名专业开发者的五日现场研究 | 介入时机、认知干扰以及用户对主动建议的接受 | 无 | Kuo et al., 2026 |

既有研究提出的若干属性有助于认识 CASA，但将这些属性直接用于编程智能体态势感知仍存在显著问题。<!-- C53.1 --> 就覆盖广度而言，目前没有一套概念体系同时表示用户对智能体行动、软件制品变化、执行证据及任务近期发展的主观认识。<!-- C53.2 --> 互动模式和活动状态刻画用户如何工作，验证与监督研究刻画用户如何检查智能体，信任研究刻画用户是否愿意依赖系统；这些研究均未把用户在多大程度上感觉自己了解当前任务作为共同的个体认知状态。<!-- C53.3 --> 就内容深度而言，表面上相关的一般项目也不能准确表达编程智能体任务。<!-- C53.4 --> 例如，SART 的信息数量和信息质量能够评价用户面对的信息环境，但无法区分用户不了解智能体采取了哪些行动、不了解代码变化的范围与依赖，或不了解测试结果对任务目标意味着什么（Taylor, 1990）。<!-- C53.5 --> 自主智能体透明度中的当前行动、理由和未来状态与 CASA 具有更直接的联系，但仍未表示这些行动怎样落实为可执行的软件变化以及执行证据怎样改变用户对任务的判断（Selkowitz et al., 2017）。<!-- C53.6 --> 因此，既有概念既未覆盖编程智能体任务认识的完整对象，也未达到区分不同认识缺口所需的具体程度。<!-- C53.7 -->

基于上述文献比较，可以识别三项相互关联的研究缺口。<!-- C55.1 --> 第一，现有人工智能辅助编程研究分别讨论互动、验证、信任和监督，缺少用于整合用户主观任务认识的完整概念化；由此容易产生分类遗漏，也难以说明不同研究所观察的认识问题是否属于同一构念。<!-- C55.2 --> 第二，部分研究沿用信任、透明度、验证成本和一般理解等概念评价用户与人工智能编程工具的互动，但这些概念分别表示依赖判断、系统信息披露、检查投入或笼统认知，不能准确表示用户对代理行动所形成任务状态的主观认识。<!-- C55.3 --> 第三，表 2 所列研究主要使用观察、访谈、活动分类、实验结果或自编评价，尚未形成经过系统内容验证和独立样本检验的 CASA 量表。<!-- C55.4 --> 因此，研究者目前缺少共同的测量工具，用以比较不同用户与产品的 CASA，并检验行动透明度、差异呈现、审批和通知设计是否通过 CASA 影响用户的感知控制、满意度或后续使用。<!-- C55.5 -->

### 2.2 动态态势感知理论

Endsley（1995b）的动态态势感知理论为识别和组织 CASA 的内容提供了理论透镜。<!-- C59.1 --> 该理论把态势感知置于动态决策过程之中，认为个体需要持续获取与当前目标相关的信息、形成对当前局面的认识，并据此选择行动。<!-- C59.2 --> 态势感知包含三个递进层级。第一层是感知环境中与任务相关的要素及其当前状态；第二层是结合目标与已有知识理解这些要素共同构成的意义；第三层是基于当前状态及其变化趋势预期近期发展（Endsley, 1995b）。<!-- C59.3 --> 这三个层级描述个体形成了什么认识，而注意和工作记忆、目标、经验与心智模型、界面设计、工作负荷、压力、系统复杂性和自动化则影响这种认识能否形成。<!-- C59.4 --> 态势感知进一步为决策与表现提供认知基础，但良好的态势感知并不单独保证正确决策，因为策略选择、能力与其他任务条件仍会影响行动结果。<!-- C59.5 --> 表 3 概括该理论的三个态势感知层级。<!-- C59.6 -->

**表 3　动态态势感知理论的层级**

| 理论层级 | 具体含义 |
| --- | --- |
| 第一层态势感知（感知） | 察觉当前目标所需的相关要素及其属性、状态和动态变化 |
| 第二层态势感知（理解） | 整合不同要素，并结合个体目标和已有知识理解它们对当前局面的意义 |
| 第三层态势感知（预期） | 依据当前状态、变化趋势与任务机制预期相关要素在近期如何发展 |

注　根据 Endsley（1995b）整理。

动态态势感知理论已经用于航空、自动化、列车驾驶、决策支持、信息安全以及人与自主智能体交互等研究领域（Endsley & Kiris, 1995; Rose et al., 2018; Nadj et al., 2020; Jaeger & Eckhardt, 2021; Endsley, 2023）。<!-- C61.1 --> 这些研究面对的具体状态对象不同，但都要求个体围绕任务目标更新对当前局面及其近期发展的认识。<!-- C61.2 --> 信息系统研究进一步表明，交互式分析功能可能同时改变个体的态势感知和任务表现，情境化的信息安全态势感知也连接系统警告、个体经验、威胁评价与实际行为（Nadj et al., 2020; Jaeger & Eckhardt, 2021）。<!-- C61.3 --> 在自主智能体研究中，当前行动、行动理由、未来状态和不确定性等信息被用于支持用户的不同层级态势感知，说明该理论能够解释用户面对可自主行动系统时的任务认识（Selkowitz et al., 2017; van de Merwe et al., 2024）。<!-- C61.4 --> 编程智能体任务同样具有明确目标、持续变化的任务状态和需要用户作出后续判断的过程。<!-- C61.5 --> 因此，动态态势感知理论可以作为理解编程智能体用户如何形成当前任务认识的理论起点。<!-- C61.6 -->

在典型的编程智能体任务中，用户提出目标并提供必要约束，智能体解释任务、规划步骤、调用工具、修改软件制品，并依据命令、测试或运行反馈继续行动（Kumar et al., 2025; Dhanorkar et al., 2026）。<!-- C63.1 --> 用户若要判断是否继续委托、补充信息或介入，需要察觉这些行动和结果，理解它们对开发目标的意义，并对任务近期发展形成预期；这一过程与动态态势感知理论的三个层级具有直接对应。<!-- C63.2 --> Baird 和 Maruping（2021）的信息系统委托理论进一步说明，能动型信息系统能够在不确定条件下接受任务并发起行动，使用户与系统的关系不同于对被动工具的逐项操作。<!-- C63.3 --> 因而，动态态势感知理论能够解释 CASA 的一般认知结构，信息系统委托则界定了这一认知结构发生的代理式使用情境。<!-- C63.4 -->

编程智能体与既有态势感知研究对象之间存在三类结构差异。<!-- C63.5 --> 第一，任务状态并非完全外在于行动者，智能体围绕开放目标采取的行动会持续生成新的软件任务状态。<!-- C63.6 --> 第二，相关状态同时分布于智能体的计划与行动轨迹、相互依赖且可执行的软件制品以及测试和运行证据，用户需要认识这些对象之间随任务推进而形成的关系（Kretsou et al., 2021; Kumar et al., 2025）。<!-- C63.7 --> 第三，委托使用户不再亲自执行每一步操作，其状态认识依赖系统保留和呈现的行动痕迹，并可能在任务已继续推进后重新形成（Baird & Maruping, 2021; Dhanorkar et al., 2026）。<!-- C63.8 --> 第一类差异使相关状态要素随着智能体行动展开而产生，第二类差异要求用户把不同软件制品和执行证据之间的关系整合为任务意义，第三类差异则要求用户依据未必亲历的行动痕迹重建任务进程。<!-- C63.9 --> 因而，CASA 面对的并非既有状态清单中的对象替换，而是一种由代理行动生成、跨制品分布并由用户间接接触的任务状态结构。<!-- C63.10 --> 现有理论适合组织 CASA 的高阶认知内容，但需要依据编程智能体用户经验发展其情境特定状态对象和测量表达。<!-- C63.11 -->

Taylor（1990）的主观态势感知传统为这种发展提供了与理论相容的经验路径。<!-- C63.12 --> SART 先由空勤人员对高、低态势感知情境的比较引出其实际使用的判断属性，再形成任务后的主观测量；CASA 同样需要从用户对具体编程智能体任务的叙述中识别其用来判断自己是否了解任务的内容。<!-- C63.13 --> 本研究将以 Endsley 理论的三个层级检查经验范畴的内容覆盖，并以其关于前因、态势感知和结果的区分确定构念边界，但不预先规定三个层级必然构成 CASA 的最终经验维度。<!-- C63.14 --> 只有在二手文本中稳定出现、能够与透明度、信任、工作负荷、感知控制和客观任务知识相区分的内容，才会进入 CASA 的候选构念结构。<!-- C63.15 -->

## 3 混合方法路径

### 3.1 研究设计

本文拟采用顺序探索型混合方法回答两个研究问题。<!-- C69.1 --> CASA 的内容领域不能由航空量表或研究者直觉预先穷举，识别编程智能体用户实际用来判断任务局面的内容需要定性研究。<!-- C69.2 --> 确定这些内容是否构成可区分且稳定的维度，并建立具有信度、效度和预测能力的测量工具，则需要定量研究。<!-- C69.3 --> 混合方法能够在同一研究计划中连接理论生成与理论检验，使定性材料所形成的构念推断接受独立数据评价（Venkatesh et al., 2013）。<!-- C69.4 --> 本研究将由定性阶段形成 CASA 的概念定义、内容边界和候选维度，再由定量阶段检验测量模型、构念效度及法则网络。<!-- C69.5 -->

研究拟分为两个阶段。<!-- C77.1 --> 第一阶段将从公开 Reddit 讨论中收集编程智能体使用叙述，并采用源于扎根理论的开放编码和轴向编码识别用户认识或难以认识任务状态时涉及的经验内容（Corbin & Strauss, 1990）。<!-- C77.2 --> 在线用户文本能够保留用户在自然使用情境中主动提出的问题，Chen 等（2024）也据此先从二手评论识别情境特定内容，再由理论组织高阶构念。<!-- C77.3 --> CASA 编码将包括预编码、全样本开放编码、轴向编码、理论比较和负例分析，并以数据结构呈现从用户表达、一阶代码到理论范畴的推导过程（Gioia et al., 2013）。<!-- C77.4 --> 两名编码者将独立分析文本，另外两名研究者负责审查范畴定义、处理边界争议并检验替代解释。<!-- C77.5 --> 轴向范畴形成后，研究团队将以 Taylor（1990）确认范畴是否属于主观态势感知，并以 Endsley（1995b）的理论层级和影响机制组织高阶内容、区分前因与结果，再与任务特定量表及相邻构念比较。<!-- C77.6 --> 该阶段的目标是形成由经验材料和理论比较共同支持的内容领域与候选维度，而不是验证预设的三维结构。<!-- C77.7 -->

第二阶段将开发并验证 CASA 测量工具。<!-- C79.1 --> 第一项工作是依据定性代码、构念定义和既有态势感知测量生成初始题项，并通过专家评审、认知访谈和多轮题项分类检验内容与表面效度（Moore & Benbasat, 1991; MacKenzie et al., 2011）。<!-- C79.2 --> 第二项工作是使用第一轮独立调查数据开展探索性分析，净化题项并比较可能的构念结构。<!-- C79.3 --> 第三项工作是使用第二轮独立调查数据开展验证性分析，检验信度、收敛效度、区分效度和跨群体稳定性；构念与维度之间的关系将依据概念含义而不是统计便利确定（Law et al., 1998; Jarvis et al., 2003; Petter et al., 2007）。<!-- C79.4 --> 第四项工作是使用第三轮独立数据重新检验量表，并建立包含感知控制、满意度和持续使用意愿的法则网络。<!-- C79.5 --> 最后，研究将比较 CASA 与一般主观态势感知测量的解释效度和样本外预测效度，并在实验子样本中比较 CASA 与客观任务状态知识。<!-- C79.6 -->

表 4 概括预期研究阶段。表中的样本规模是最低规划范围，正式实施前将依据最终题项数、模型复杂度和统计功效分析确定。

| 阶段 | 目标 | 主要程序 | 预期证据 |
| --- | --- | --- | --- |
| 阶段 1　构念开发 | 界定 CASA 内容领域与候选维度 | Reddit 语料筛选；预编码；双人开放编码；轴向编码；理论比较；负例分析 | 数据结构、范畴定义、边界证据、理论饱和 |
| 阶段 2A　初始量表 | 生成并净化题项内容 | 题项池；ITEM 语义审计；专家内容效度；认知访谈；多轮卡片分类 | 内容代表性、清晰性、构念可区分性 |
| 阶段 2B　探索与验证 | 确定测量模型并检验稳定性 | 独立样本 EFA；独立样本 CFA；竞争测量模型；测量不变性 | 因子结构、信度、收敛与区分效度 |
| 阶段 2C　法则网络与预测 | 证明 CASA 的理论和实践增量 | 两时点或多来源调查；法则网络；与 SART 比较；样本外预测；任务真值子研究 | 法则效度、增量效度、预测效度、主客观校准 |

---

# 以下为预期实施内容

## 4 阶段 1　使用二手在线文本开发 CASA 构念

### 4.1 数据来源与抽样范围

研究将使用 Reddit 公开帖子和评论作为第一阶段的经验材料。选择 Reddit 不是因为该平台能够代表所有编程智能体用户，而是因为产品专属社区和跨产品编程社区中保留了用户对具体任务、界面、失败、检查和后续处理的自然叙述。相较于仅询问研究者预设问题的问卷，这些叙述更可能暴露用户自发认为重要的任务状态及其缺失方式。与此同时，Reddit 用户具有自选择性，帖子受到社区规范和产品热度影响，而且问题与失败经历可能比平稳使用经历更容易被发布。因此，该数据只用于发现和界定构念内容，不用于估计总体发生率。

候选语料来源将同时包含跨产品的编程智能体讨论社区和产品专属社区，以避免把某一产品界面的特征误当作 CASA 的普遍内容。正式社区名单将在试采集阶段依据三个标准确定。社区中应存在持续的第一手使用讨论，讨论应能够识别所用工具或交互形态，社区规则应允许研究者在遵守平台政策的条件下访问公开内容。研究将记录产品、界面形态、任务类型、发布时间和可识别的使用经验信息，以支持分层比较，但不会收集私信、受限社区内容或已删除内容。由于公开讨论可能遗漏企业内部任务和用户未主动言明的隐性认识，研究将在阶段 1 完成覆盖审计；若企业情境、平稳高 CASA 经历或关键状态内容明显不足，将补充以关键事件为中心的开发者访谈，而不以 Reddit 单一来源宣称内容饱和。

语料检索将采用宽入口、严筛选的策略。入口检索围绕编程智能体产品、代理式任务和软件开发活动展开，不要求文本必须出现理解、态势感知或控制等理论词汇，以免只收集能够印证既有定义的材料。纳入文本需要描述本人或可明确识别用户的编程智能体使用经历，涉及一个具体任务或连续任务过程，并包含智能体行动、软件变化、执行反馈、任务进展、检查判断或后续影响中的至少一项。仅讨论模型排行、价格、新闻、一般产品推荐、纯粹代码求助、自动生成内容或无法判断是否实际使用的文本将被排除。

分析单位以能够表达一个完整意义的任务片段为主，而不是机械地以单条评论为单位。研究将保留必要的帖子标题、上文评论和回复关系，使编码者能够判断代词、产品、任务和事件顺序。每个分析片段将附带去标识化的情境属性，但用户名、个人主页和可追踪身份信息不会进入分析数据集。

### 4.2 伦理与数据治理

公开可访问不等于不存在研究伦理风险。研究实施前将向所在机构伦理审查机构提交方案，并依据互联网研究伦理指南采用情境化风险判断（Franzke et al., 2020; Gliniecka, 2023）。数据采集将遵守届时有效的 Reddit 平台政策和访问方式，不绕过访问限制。研究数据库将用随机编号替代用户名，移除个人身份、雇主、项目名称、仓库地址和其他可追踪信息。

论文呈现原始文本时将评估反向搜索风险。对于包含敏感项目、工作关系或独特表述的材料，优先采用保持分析含义的转述，而不是逐字引用。原始数据不公开发布；可复核材料将以去标识化代码本、范畴定义、审计轨迹和经过风险处理的例证为主。若某个社区对研究使用存在明确反对规范，研究将排除该社区或与管理者沟通后再决定。

### 4.3 编码程序

编码团队预期由四名研究者组成。两名编码者独立完成预编码、开放编码和轴向分类；另外两名具有信息系统、软件工程或人机交互背景的研究者负责审查构念定义、处理争议和检查理论映射。编程智能体可以辅助去重、格式整理和检索，但不得代替研究者作出范畴归属和构念边界判断。所有人工决策、代码修改和争议处理将保留审计记录。

**准备阶段　形成初始编码协议。** 研究团队将先从不同产品、交互形态和任务类型中抽取少量材料，共同识别分析单位、上下文保留规则和排除标准。初始协议只提供任务、智能体行动、软件制品、执行反馈、认识表达和后续反应等宽泛观察位置，不把它们设为最终维度。进入 CASA 候选内容的一阶代码必须表达用户对自身认识状态的判断，例如用户说明自己能够或不能判断智能体做了什么、变化意味着什么或任务将如何继续。仅陈述智能体修改了某个文件、测试失败或任务完成等事实，而没有显示用户如何评价自身认识的文本，只作为任务情境或客观事件编码，不作为 CASA 的直接表现。编码者需要同时标记正向材料、负向材料和边界材料，例如用户明确了解任务、明确不了解任务、拥有大量信息却仍无法判断，以及缺乏信息但凭经验能够判断等情形。

**步骤 1　开放编码预试。** 在符合条件的语料确定后，研究将随机抽取约 10% 作为预试样本，并保证其中覆盖主要产品、界面和任务类型。两名编码者逐段独立标记用户认为自己知道、理解、能够预期或无法判断的任务内容，并用尽可能贴近用户语言的一阶代码表达。双方随后比较差异，澄清代码定义、合并纯同义代码并修订排除规则。预试的目的不是获得高一致性数字，而是暴露构念边界和代码本中不清楚的地方。

**步骤 2　全样本开放编码。** 编码者依据修订后的协议独立处理其余语料，并对重叠子样本进行双人编码。对于已经形成稳定代码定义的代码，将报告 Cohen's kappa 或适合数据结构的 Krippendorff's alpha；对于仍在发现中的开放代码，将报告差异解决过程而不把一致性系数误作理论有效性的替代。研究团队将分批检查新代码出现情况。当连续三个异质批次不再产生新的轴向范畴后，再使用一个此前未参与理论形成的保留批次检验饱和。

**步骤 3　轴向编码。** 两名编码者将独立比较一阶代码之间的对象、状态、时间和意义关系，把描述同一类任务认识的代码聚合为轴向范畴。每个轴向范畴必须包含明确名称、定义、纳入标准、排除标准、正例、负例以及与相邻范畴的区别。仅有极少材料支持、只属于单一产品功能或无法与态度评价区分的代码不会因为新颖而自动保留。在开放编码和轴向编码完成以前，编码者不使用感知、理解和预期作为代码名称；一阶代码表和初步轴向范畴将在理论比较前冻结并保留版本记录。

**步骤 4　理论比较与选择性编码。** 轴向范畴形成后，研究团队将先与 Taylor（1990）的主观态势感知定义和构念引出结果比较，再以 Endsley（1995b）的感知、理解和预期审查内容覆盖，并依据该理论关于个体因素、任务条件、系统设计、态势感知和决策结果的区分确定范畴位置。三个态势感知层级在此用于理论比较，不被强制设定为最终经验维度；跨越多个层级或无法映射到既有层级的稳定范畴将原样保留，并在理论对应表中报告。比较将围绕该范畴是否表达用户对自身任务认识的程度判断、是否只是客观任务事实、是否只是影响这种认识的条件、是否是认识形成后的态度或行为，以及是否只是智能体能力或界面的属性展开。属于 CASA 的范畴还需说明它是对一般态势感知内容的具体化，还是由编程智能体代理行动与软件制品耦合带来的新增内容。未参与前述编码的研究者将依据冻结前后的代码表审查范畴是否因理论映射被删除、拆分或改名，以识别强制拟合。

**步骤 5　负例与替代解释检验。** 研究将主动查找能够推翻初步结构的材料。例如，用户表示自己完全不知道智能体改了什么但仍相信结果时，应分别编码为低 CASA 与高信任；用户拥有清楚的差异视图却仍然无法说明变化意义时，应编码为高信息可见性与低 CASA；用户拥有停止和回滚权限却不知道何时应使用时，应编码为具有控制机制但 CASA 较低。相反，用户仅陈述智能体修改了三个文件而没有评价自己是否了解这些变化时，不据此推断 CASA 高低。只有能够经受这些边界检验的范畴才进入候选构念结构。

### 4.4 构念结构与定义验证

定性阶段结束后，研究团队将依据一阶代码和轴向范畴修订 CASA 的概念定义。清晰的概念定义需要明确构念所指对象、核心属性、适用条件及其与相邻概念的区别（Podsakoff et al., 2016）。修订后的 CASA 定义还将按照个体用户、编程智能体、具体任务和理论功能说明其分析单位、状态对象、时间范围与法则位置（Burton-Jones & Straub, 2006）。研究不会仅因为经验范畴可以对应感知、理解和预期就宣布三维结构成立，也不会仅因为若干范畴在文本中共同出现就宣布它们属于同一构念。

候选维度将经过至少两轮卡片分类。第一轮邀请具有编程智能体实际经验的开发者，根据维度定义把一阶范畴归入候选维度，并允许设置无法归类选项。第二轮邀请信息系统、人机交互和软件工程研究者独立完成同样任务。研究将依据命中率、评判者一致性和争议说明修订定义；如果某些范畴持续跨维度混淆，应优先修改概念边界，而不是只修改名称。

CASA 的测量模型将在内容领域明确后决定。多维构念可能把维度视为潜在构念的表现、共同形成的聚合或不可相互替换的特征组合，不同关系对应不同的理论含义和操作化方式（Law et al., 1998）。若各维度是同一主观状态的可互换表现，删除某一维度不改变构念内涵，并且维度应当高度共变，则可以考虑反映式高阶模型。若各维度共同构成 CASA、不能互换，且删除任一维度会遗漏一种必要任务状态，则应考虑形成式高阶模型（Jarvis et al., 2003; Petter et al., 2007）。模型选择必须基于构念与指标之间的关系，而不能依据哪一种统计模型更容易获得良好拟合。

### 4.5 阶段 1 的预期产出

阶段 1 应形成六项可审计产出，包括完整的数据筛选流程，一阶代码、轴向范畴和候选维度的数据结构，每个范畴的定义与边界，一般态势感知内容与编程智能体新增内容的比较表，前因、构念内容和后果的分类表，以及支持和挑战最终结构的正例与负例。数据结构将保留从用户表达、一阶代码到理论范畴的推导过程，以便审稿者检查经验材料与构念主张之间的联系（Gioia et al., 2013）。只有这些产出能够表明编程智能体情境确实产生了稳定且有理论意义的内容差异时，研究才进入新量表开发。

## 5 阶段 2　CASA 量表开发与验证

### 5.1 阶段 2A　建立初始量表

初始题项将依据成熟的量表开发程序，来自阶段 1 中用户描述任务认识的语言、修订后的 CASA 及各维度定义，以及 SART 和其他态势感知文献中的相关表达（Hinkin, 1998; MacKenzie et al., 2011）。题项不会直接测量界面是否提供差异视图、日志或通知，因为这些属于潜在前因；也不会询问用户是否信任、喜欢或能够控制智能体，因为这些属于相邻构念或后果。每个题项都将锚定一次刚刚完成或能够清楚回忆的具体任务，例如使用在刚才的任务中作为共同时间边界。

研究团队将生成大于最终量表需求的题项池，使每个候选维度在净化前具有充分内容覆盖。题项将避免同时包含多个不同判断对象。例如，了解智能体做了什么并理解代码为什么变化同时包含行动认识和意义理解，不应在维度尚未确定时写入同一题项。研究将使用 ITEM Ontology 对题项中的对象、被测属性、限定词和反应集合进行语义审计，以识别双重问题、对象漂移和限定范围不一致（Larsen et al., 2026）。

内容效度评估将分为人类判断与人工智能辅助检查两部分。首先，由编程智能体用户和相关领域学者独立判断每个题项是否属于目标维度、是否代表必要内容、是否与其他维度混淆。其次，可以使用 RATER 对题项与定义的语义对应和构念区分提供补充诊断，但人工智能结果不替代专家判断（Pillet et al., 2026）。随后，研究将使用认知访谈检验参与者如何理解题项对象、时间边界、程度限定和反应选项，并根据参与者复述与作答理由修订项目。

经过内容效度和认知访谈后，题项将进入多轮卡片分类。评判者获得 CASA、候选维度和主要相邻构念的定义，并把题项分配到最符合的类别或无法判断类别。研究将报告题项归类命中率、评判者一致性和每轮删除或改写原因。卡片分类不仅用于删除弱题项，也用于发现构念定义本身是否仍然含混（Moore & Benbasat, 1991）。

### 5.2 阶段 2B　量表净化与结构验证

第一轮调查将面向近期实际使用过编程智能体并能回忆具体任务的用户。筛选问题需要确认参与者使用的是能够读取项目、修改软件制品或调用工具的编程智能体，而不是仅使用一次代码补全或一般对话模型。参与者将先描述最近一次任务的工具、目标、持续时间和主要行动，再回答 CASA 题项，以降低不同任务参照造成的测量误差。

第一轮独立样本将用于探索性因子分析和初步题项净化。样本量原则上不低于 500，并在最终题项数和因子结构确定后通过功效分析调整。研究将检查题项分布、缺失、极端反应、项目间冗余和探索性结构。题项删除不能只依据载荷，而要同时确认删除后是否仍然覆盖构念内容。若定性结构与探索性结构不一致，研究团队需要回到原始代码和定义解释差异，而不能只服从统计输出。

第二轮独立样本将用于验证性因子分析和竞争测量模型比较。研究将比较单因子模型、理论提出的多维模型以及合理的高阶模型，并依据最终测量理论选择反映式或形成式估计方法。反映式维度将检验标准化载荷、复合信度、omega、平均方差提取和区分效度；形成式部分将检验指标权重、冗余和多重共线性。模型拟合将报告适合估计方法的指标，不把某一个阈值作为构念正确的充分证据。

第二轮还将检验 CASA 与人工智能信任、感知透明度、感知控制、认知负荷和一般主观态势感知之间的区分效度。CASA 应与这些变量相关，但不能因为相关性过高而失去独立内容。研究还将比较不同编程经验、智能体经验、CLI 与 IDE 交互形态以及不同任务类型下的测量不变性。若量表只能在某一种产品或界面中成立，构念边界需要相应收窄。

### 5.3 阶段 2C　量表复核、法则网络与预测比较

第三轮独立数据将重新检验最终量表，并尽可能采用两时点设计降低共同方法偏差。第一时点要求参与者围绕最近一次具体任务报告 CASA、一般主观态势感知和相邻构念；第二时点测量该次使用后的感知控制、满意度和持续使用意愿。问卷还将依据最终研究设计加入理论上无关的标记变量或共同方法因子，配合时间分离检验共同方法方差，而不依赖单一的 Harman 单因子检验（Podsakoff et al., 2003）。若研究条件允许，还可以从产品日志或任务记录获得使用持续时间、介入和任务完成等行为信息，但这些数据不替代主观结果变量。

法则网络将围绕已经在论文开篇明确的结果链展开。本文预期 CASA 可能为用户作出继续、介入和接受判断提供认知基础，并进一步影响感知控制和满意度，进而关系到持续使用意愿。构念开发论文的主要目的不是一次检验所有可能前因，而是评价 CASA 能否在理论上合理的网络中发挥作用。感知透明度、任务复杂性、用户经验和认知负荷可作为前因或控制变量；人工智能信任用于检验区分效度和替代解释。

增量效度检验将使用相同结果变量比较多组基准模型。第一组基准采用 Taylor（1990）的十维 SART，并仅把任务指称最小程度地调整为刚刚完成的编程智能体任务；三维 SART 及其传统合成分数将作为替代计分方式，同时依据 Bolton 等（2022）的提醒报告各组成部分结果。第二组基准将在独立于 Reddit 编码结果的条件下，由软件开发与态势感知专家依据统一任务分析形成简短的任务特定主观态势感知项目，以降低 CASA 仅因具有具体措辞而获得优势的可能。所有基准项目均需经过认知访谈与内容效度评估，不能直接把航空术语替换为编程术语。CASA 模型将在控制上述基准测量后解释感知控制、满意度和持续使用意愿，并通过解释方差、信息准则、嵌套模型差异及保留样本预测误差评价增量。只有 CASA 在保持区分效度的同时稳定增加解释或预测能力，情境特定构念的开发价值才得到支持。

为区分主观任务认识和客观任务知识，研究还将设计一个统一任务的实验或任务回放子研究。研究团队将在实验前固定初始仓库、任务目标、工具权限和可接受结果，并由智能体日志、版本差异、命令输出和测试结果共同建立每次实际行动轨迹的任务真值。参与者在任务结束后先填写 CASA，随后在隐藏界面线索的任务回放中回答与该次实际轨迹相匹配的状态问题；该顺序避免用探测问题提示 CASA 作答，也不机械采用 SAGAT 的任务中途冻结程序。研究将检验高 CASA 是否通常伴随更准确的任务状态判断，以及何种界面或任务条件下出现高主观、低客观或低主观、高客观的脱节。客观问题只提供校准和效标证据，不用于把 CASA 重新定义为任务问题正确率。

## 6 构念开发的判断门槛

本研究不能预设 CASA 必然是一个成立的新构念。阶段 1 和阶段 2 将设置以下判断门槛。

1. 如果定性范畴完全落入 SART 或一般态势感知的既有内容，且没有形成稳定的编程智能体任务内容，则研究应定位为一般主观态势感知量表的情境适配，而不是新构念开发。
2. 如果候选维度主要描述信息是否可见、界面是否易用或用户是否信任智能体，则应把它们分别放回透明度、可用性或信任，而不能通过更名纳入 CASA。
3. 如果所谓编程智能体特定内容只存在于单一产品或单一交互界面，应收窄研究对象，或将其作为产品特征而非普遍维度。
4. 如果 CASA 与一般主观态势感知、感知控制或信任缺乏区分效度，应修订定义与量表，必要时终止新构念主张。
5. 如果 CASA 没有表现出相对于一般主观态势感知的内容优势、增量效度或诊断价值，则不能声称开发情境特定构念改善了理论解释。

## 7 与 Chen 等（2024）的逐段逻辑对应

| Chen 等（2024）的功能位置 | 原文承担的论证功能 | CASA 稿对应内容 |
| --- | --- | --- |
| C19 | 说明新技术如何改变交互，并由对象变化引出研究现象 | 编程智能体由生成内容转向代理行动；用户需要认识任务推进状态 |
| C21 | 逐项比较新情境与既有研究情境的结构差异 | 状态由代理行动生成、状态跨行动轨迹与软件制品和执行证据分布、用户通过痕迹间接接触状态 |
| C23 | 选择唯一母构念、给出定义并说明现实后果 | 以个体态势感知为基础定义 CASA，连接感知控制、满意度与持续使用 |
| C25-C27 | 回顾母构念在其他情境的量表，说明哪些可用、哪些不适用 | 比较 SART、SAGAT、信息安全态势感知、仪表盘研究和编程交互研究 |
| C29 | 说明情境量表的理论与实践必要性 | 区分任务表现与用户任务认识，并识别用户主观上较难把握的任务方面 |
| C31 | 将情境特征、现实重要性和测量缺口汇合为少量研究问题 | 一个问题开发维度与量表，一个问题检验相对一般 SA 的增量价值 |
| C33-C35 | 简述定性到定量的研究过程，并解释理论如何参与编码 | Reddit 开放与轴向编码；Taylor 界定主观属性；Endsley 组织高阶内容；多轮量表验证 |
| C37-C39 | 分别提出构念、理论扩展和实践工具贡献 | CASA 内容与量表；代理行动下的主观 SA；产品状态呈现诊断工具 |
| C45-C55 | 系统比较既有构念和量表，形成宽度、深度和实证三类缺口 | 对象遗漏、前因混入、主客观混淆、相关现象碎片化和缺少量表 |
| C59-C63 | 说明理论原义、跨情境使用、适用桥梁与发展空间 | Endsley 动态态势感知理论组织认知层级；信息系统委托界定代理式情境；Taylor 指导主观内容引出 |
| C69-C79 | 说明混合方法必要性并概括两个阶段 | 定性识别内容，定量验证量表、法则网络和相对预测能力 |

## 8 参考文献

- Baird, A., & Maruping, L. M. (2021). The next generation of research on IS use: A theoretical framework of delegation to and from agentic IS artifacts. *MIS Quarterly, 45*(1), 315-341. https://doi.org/10.25300/MISQ/2021/15882
- Barke, S., James, M. B., & Polikarpova, N. (2023). Grounded Copilot: How programmers interact with code-generating models. *Proceedings of the ACM on Programming Languages, 7*(OOPSLA1), Article 78, 85-111. https://doi.org/10.1145/3586030
- Baronas, A.-M. K., & Louis, M. R. (1988). Restoring a sense of control during implementation: How user involvement leads to system acceptance. *MIS Quarterly, 12*(1), 111-123. https://doi.org/10.2307/248811
- Bhattacherjee, A. (2001). Understanding information systems continuance: An expectation-confirmation model. *MIS Quarterly, 25*(3), 351-370. https://doi.org/10.2307/3250921
- Bolton, M. L., Biltekoff, E., & Humphrey, L. R. (2022). The level of measurement of subjective situation awareness and its dimensions in the Situation Awareness Rating Technique (SART). *IEEE Transactions on Human-Machine Systems, 52*(6), 1147-1154. https://doi.org/10.1109/THMS.2021.3121960
- Burton-Jones, A., & Straub, D. W., Jr. (2006). Reconceptualizing system usage: An approach and empirical test. *Information Systems Research, 17*(3), 228-246. https://doi.org/10.1287/isre.1060.0096
- Chen, Q., Gong, Y., Keil, M., Liu, S., & Lu, Y. (2024). Conceptualization and measurement of voice-interaction usability: The development of cooperative principle theory for smart product use. *MIS Quarterly, 48*(3), 1009-1046. https://doi.org/10.25300/MISQ/2023/17525
- Corbin, J. M., & Strauss, A. (1990). Grounded theory research: Procedures, canons, and evaluative criteria. *Qualitative Sociology, 13*(1), 3-21. https://doi.org/10.1007/BF00988593
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
- Lewis, B. R., Templeton, G. F., & Byrd, T. A. (2005). A methodology for construct development in MIS research. *European Journal of Information Systems, 14*(4), 388-400. https://doi.org/10.1057/palgrave.ejis.3000552
- MacKenzie, S. B., Podsakoff, P. M., & Podsakoff, N. P. (2011). Construct measurement and validation procedures in MIS and behavioral research: Integrating new and existing techniques. *MIS Quarterly, 35*(2), 293-334. https://doi.org/10.2307/23044045
- McKinsey Global Institute. (2023). *The economic potential of generative AI: The next productivity frontier*. https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier
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
- Stack Overflow. (2025). *2025 Developer Survey: AI*. https://survey.stackoverflow.co/2025/ai
- Stanton, N. A., Salmon, P. M., Walker, G. H., & Green, D. (2006). Situation awareness measurement: A review of applicability for C4i environments. *Applied Ergonomics, 37*(2), 225-238. https://doi.org/10.1016/j.apergo.2005.02.001
- Taylor, R. M. (1990). Situational awareness rating technique (SART): The development of a tool for aircrew systems design. In *Situational Awareness in Aerospace Operations* (AGARD-CP-478, pp. 3/1-3/17). NATO Advisory Group for Aerospace Research and Development.
- van de Merwe, K., Mallam, S., & Nazir, S. (2024). Agent transparency, situation awareness, mental workload, and operator performance: A systematic literature review. *Human Factors, 66*(1), 180-208. https://doi.org/10.1177/00187208221077804
- Venkatesh, V., Brown, S. A., & Bala, H. (2013). Bridging the qualitative-quantitative divide: Guidelines for conducting mixed methods research in information systems. *MIS Quarterly, 37*(1), 21-54. https://doi.org/10.25300/MISQ/2013/37.1.02
- Wang, R., Cheng, R., Ford, D., & Zimmermann, T. (2024). Investigating and designing for trust in AI-powered code generation tools. In *Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency* (pp. 1475-1493). Association for Computing Machinery. https://doi.org/10.1145/3630106.3658984
