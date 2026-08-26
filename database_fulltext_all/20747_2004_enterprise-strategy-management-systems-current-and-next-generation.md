---
otero_id: 20747
otero_key: "8T6GAX48"
title: "Enterprise strategy management systems: current and next generation"
authors: "Christian Wagner"
year: "2004"
journal: "The Journal of Strategic Information Systems"
doi: "10.1016/j.jsis.2004.02.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Enterprise strategy management systems: current and next generation

Christian Wagner

Department of Information Systems, City University of Hong Kong, 83 Tat Chee Avenue Kowloon, Hong Kong, China

Received 27 May 2002; accepted 25 February 2004

Available online 27 April 2004

## Abstract

Strategic planning in the ‘post-net’ era creates new challenges for senior management, due to the need for faster speed of strategy planning and implementation, frequent, significant environmental changes, and more complex organizations. Enterprise strategy management (ESM) systems promise better planning support for senior management, but are still in their infancy. Present systems focus too much on quantitative aspects, and not enough on qualitative or process aspects of planning. The article reviews the landscape of strategic information systems for ESM, identifies their contributions, and derives the requirements for the next generation of ESM systems. It also reflects on IT opportunities beyond the next generation.

Keywords: Enterprise strategy management; Strategic planning; Strategic information systems; Balanced scorecard; Post-net era

## 1. Background and introduction

## 1.1. Strategic planning challenges in the ‘post-net’ era

In the Spring of 2000, concerns grew among the senior management of a leading travel and tourism company in the United States. The company—one of the pioneers of electronic commerce—was losing valuation, while Internet startups were soaring. Major customers were not renewing their agreements, as competitor products threatened to erode the company’s market position and its dominant role in managing one of the industry’s supply chains. Not surprisingly, company management embarked on defining a new strategy. What was surprising was the speed of this undertaking: 3 months to formulate the strategy, and 6 months to implement it. For this e-commerce leader, rapid strategic transformation became the new (and successful) reality of managing in the ‘post-net’ era.

This situation illustrates the realities faced by many companies today. Enterprise strategy management (ESM) in the post-net era is fundamentally more challenging than it used to be just a few years ago. Three clearly identifiable factors contribute to today’s complexity increases:

† Shorter planning and implementation cycles.

† Frequent and rapid environmental changes, possibly with discontinuities.

† Organization units that extend beyond a single company, such as supply chains or virtual organizations.

Shorter planning and implementation cycles have been brought about by several factors, including competitive pressures from start-ups (Kambil, 2000; Hamel, 1999; Watts, 2002) and the availability of real-time or almost real-time information to manage the business (Anderson, 2002). In order to compete with start-ups, established companies have to adopt start-up agility in creating and changing business models. Strategy implementation cycles for start-ups are driven by yearly (or even shorter) funding cycles, and the constant evolutionary process of new business idea funding through venture capital. Similarly, post-net companies with their integrated enterprise information systems and on-line research capability gather data at ‘web speed’ (Van Yoder, 2001). As a result, they create pressures for all established firms to target strategy formulation and revision in short cycles (Baum and Wally, 2003; Paul, 2000; Hackett, 1998), or even as an ongoing activity.

Environmental changes have always existed in the planners’ realm. However, dotcom bubble and dotcom bust, as well as the recent worldwide economic uncertainties, are signs of changes that are frequent, impactful, and seemingly unpredictable. And while ex post most events will have had their precursors and indicators, ex ante, many are difficult to foresee or to gauge in their impact (Oliver, 2002).

Today’s organizations are significantly more complicated than they used to be. They are more distributed and networked, as supply chains, virtual organizations, or co-opetitive arrangements (Hamel et al., 1989). Should a supply chain define a unique strategy for itself? How would this be aligned with the strategies for each individual company in the supply chain? We do not even know many of the questions yet, let alone have a good answer for them.

Taken together, these factors significantly raise the demands on strategic planning, as well as planning methodologies (Hitchin, 2002), highlighting the potential contribution of strategy planning tools, including software. Strategic planning cannot remain a one-off planning activity (sometimes referred to as a ‘ritual’) whose results remain in the heads of the planners (Hackett, 1998). Furthermore, future strategic planning exercises ignore the outcomes and findings from previous strategic planning activities.

In other words, strategic planning has to change from a sequence of planning events to a business process, one that is ideally well-structured, iterative, and whose outputs are captured in organizational information systems, from which planning can be followed up by implementation, results measurement, and organizational learning (Fahy, 2002).

## 1.2. Need for enterprise strategy management software

The problem is that available software tools cannot fulfill these demands. In 2001, AMR research noted that while business strategy is at the core of the planning methodology and software world, only few applications presently support this type of task (‘The Case for Automating Strategy’, AMR Research, February 20, 2001), and little has happened in the meantime to change this situation (Smith, 2002). In addition to the lack of appropriate software tools, research into information systems for strategic planning has been scarce as well, with the result that there are very few insights available, especially for the implementation of strategic management methods into software. Prominent exceptions include El Sawy (1985), Avison et al. (1998), and Singh et al. (2002). But altogether, there is a significant research shortage in this area.

Consequently, the purpose of this article is to explain current software-based strategy planning and implementation approaches, and to identify fruitful directions for future research and development in this area. The underlying question might be stated as ‘how to provide senior management with useful strategy planning and implementation tools that help in the entire process from (1) defining a vision and initiatives to achieve it, to (2) monitoring the results of strategic initiatives, to (3) defining and monitoring of adaptive measures when current objectives are not met?

The article will investigate:

† the nature of a useful strategy planning and implementation methodology;

† the requirements for software that purposefully and methodologically supports the planning and implementation task.

The position of this article will be as follows. In order to build a system and process as suggested, we will have to achieve the following. First, formulate strategic planning and strategy implementation as a business process, with clearly defined inputs, outputs, and activities whose completion results in obtaining the outputs. Second, create and implement both the workflow and data model for this process, so as to support the executives who carry out the planning task, and to capture the results of the tasks in a database. As an added difficulty, both process and data model need to be designed to be iterative and decomposable, so that they can be delegated and later rolled up again, thus enabling alignment. Third, define and create a measurement framework that can measure the level of vision implementation, can identify deviations, and can trigger the formulation of initiatives to correct deviations from the plan.

A formal definition of processes and data, as implied by this direction, is not common in strategy management, as many planners consider the task to be unstructured and do not rely on a well-formulated methodology (see Avison et al. (1998)). However, without a well-defined methodology, there is little opportunity for formal planning, let alone information systems support. As a result, many planners in the past have relied on formal methods only for tasks such as budgeting, which was often the extent of ‘strategic planning’ (Gluck et al., 1980) or at least a large part of it (Hackett, 1998).

In order to broaden software support for strategic planning beyond budgeting software, we need to explore the extent to which IS tools and techniques can possibly support a knowledge-rich, qualitative, and non-algorithmic planning and decision making task. This will be the focus of Section 2. Section 3 will contrast these ideas against the current state of software development, reviewing key capabilities of today’s leading products. Section 4 follows up with a proposal for next generation ESM software. Section 5 reflects on a new paradigm for ESM software, beyond next generation solutions. Section 6 draws conclusions and summarizes our learning.

The article is intended to offer the following insights: first, today’s leading strategic information systems have not yet sufficiently addressed the issue of strategic planning and management, as evidenced by the gap between what strategic planning and management should be, and what today’s software can support. Second, there is great potential for increased software support, but it requires a detailed and thorough analysis of the planning activities. Third, a feasible model for future ESM software will rely on the analytical intelligence of planners, and software tools to facilitate the process, to minimize process losses, and to amplify process gains.

Throughout the article, any reference to ‘strategic information systems’ will refer to information systems that help in shaping the strategy as planning tools, rather than to information systems that define a company’s business or generate a significant share of the bottom-line. However, for clarity, they will be frequently referred to as ESM systems. Further, any reference to the post-net era will not imply that the era of the Internet is over, but that we are in an era defined by widespread adoption of the Internet and the World Wide Web.

## 2. Methodology for enterprise strategy management

## 2.1. Overview

If we wish to build software for ESM, we need to begin with an understanding of what ESM might entail. A useful framework for this purpose is Gluck et al. (1980), as it describes the evolution in strategic thinking, and offers a good map for past and present software developments, which will be applied in Section 3. Although the framework is more than 20 years old, it still captures the range of planning approaches used in organizations today. Section 5 will consider alternative approaches to strategic management and a potential corresponding paradigm shift in ESM systems.

## 2.2. Gluck et al.’s four phase maturity model

Strategic management has considerably evolved over the last few decades, and can be differentiated into different phases of maturity, according to Gluck et al.:

† Phase 1: Financial planning, is described by a functional focus and annual budgets. Simple techniques are used for budgeting, and the planning goal is to meet budgets. Accordingly, the focus is very much internal.

† Phase 2: Forecast-based planning, incorporates multi-year (e.g. 5-year) budgets, gap analysis (between targets and actual performance), planning and static allocation of resources. This planning process forecasts sales and market growth, and estimates income, expenses, and overall balance sheets. This analysis is also quantitative in nature and highly internally focused.

† Phase 3: Externally oriented planning, is defined by situation analysis and competitive assessments, evaluation of strategic options, and dynamic allocation of resources. Company planners look increasingly outside the organization, identify attractive market segments, competitive advantages, and then plan to move the company’s product portfolio accordingly.

† Phase 4: Strategic management, is characterized by a well-defined strategic framework, a strategically focused organization, widespread strategic thinking capability, and reinforcing management processes. The company’s fundamental goal is to change its business environment through innovation. Instead of being a competitor, the company redefines the industry and separates itself from the competition. Obviously, this lofty goal requires very significant strategic planning, combined with high levels of innovation, and the ability to execute. The focus of this form of planning is highly external, as well as largely non-quantitative and non-‘algorithmic’.

Despite its age, Gluck et al.’s framework is still timely in describing today’s planning approaches. In fact, many organizations limit their highest level planning to annual budgeting, and even large, multi-national corporations may only go as far as multi-year planning or externally oriented planning (Montgomery, 2002; Freeman, 2001; Leauby, 2002). Further, companies that engage in strategic management often do this as an annual exercise that is more a ritual than part of the true strategic management activity (Carpenter, 1986; Coveney, 1998). For higher levels of planning (e.g. Phase 2 or 3), the ‘Balanced Scorecard’ (BSC) has emerged as the leading strategic management methodology, as it is now positioned by its creators (Kaplan and Norton, 1996).

Any planning beyond Phase 2 requires the knowledge of methodologies that go beyond financial analysis, budgeting, and ‘managing by the numbers’. Phases 3 and 4 require procedural approaches for activities such as external analysis, or core competency analysis. Furthermore, once these analyses have been completed, planners have to understand how to represent the findings, and how to properly use them, so as to finally come up with a new plan. This is neither easy nor described in most planning methodologies, which are generally more declarative than procedural.

If we map the four phase maturity model into a planning framework (Fig. 1), based for instance on Hax and Majluf (1996), or Hill and Jones (2001), we can see that planning methods beyond Phase 1 and 2 incorporate significantly more, and more complex activities.

![](/api/attachments/8T6GAX48/fulltext/images/40c1d3da46d0192acc0881f0291e3d7c1d5c55d6c0dee22d2a6514c1f37346d8.jpg)  
Fig. 1. Planning framework (Phase 4)—procedural view.

## 2.3. Planning framework

The framework in Fig. 1 depicts the planning process for an intended strategy, with several activities. The process begins with the mission formulation and setting of high-level goals. Then, strategic choices are made, informed by external and internal analysis, where goals are mapped against opportunities, threats, internal capabilities, company values, and so forth. Several decomposition steps might follow, where the strategy is cascaded downwards into business unit strategies, functional strategies, and further to the operational level. Several parallel implementation steps will define initiatives to affect goal achievement, define new organization designs, and set budgets to fund the organization’s plans. The measurement and control system will monitor adherence to plans and goal achievement, and will feed back to the planning processes where changes can be made. Alignment from vision to implementation can potentially be achieved through the process of strategy decomposition, and a budgeting process based on strategic goals, initiatives, and organization design. The planning loop is closed through feedback from the measurement and control system.

The real planning process can still be considerably more complicated, as it has to consider issues such as new versus existing strategies, managing hundreds or thousands of ‘legacy’ initiatives, and numerous dependencies not shown in this simple top-down view.

Different planning methodologies will address different subsets of this model. Financial planning methodologies will focus primarily on the budgeting system and the measurement and control system. The BSC (Kaplan and Norton, 1996) focuses on the measurement and control system, but also enables the formulation of vision, mission, strategic goals. It further permits the decomposition of high-level (corporate) scorecards into business unit and functional scorecards (Kaplan and Norton, 2000) and can capture the results, but offers no specific guidance on how to do it. The BSC specifically facilitates the monitoring and management of alignment, by representing specific links between different elements of a strategy (so-called ‘perspectives’), and enabling causal analysis when measurement system parameters miss their targets.

Other planning methodologies exist for other aspects of the planning process. Scenario analysis (Schoemaker, 1992), for instance, targets the external analysis activity, and provides both framework and process. Schoemaker’s planning methodology actually extends beyond external analysis and includes vision and goal definition, strategic choice, and definition of initiatives. Prahalad and Hamel (1990) offer a methodology for internal analysis, through the study of competitive forces, while Porter’s competitive forces model (Porter, 1980) offers another view of external analysis (especially industry analysis).

For software development, this has several implications. First, any software that extends beyond budgeting and control has to support numerous additional planning activities, and potentially more than one planning methodology for any activity (e.g. some companies may prefer scenario analysis, others may prefer SWOT). Second, many of the planning activities outside of budgeting and control deal with non-quantitative information, while the strengths of most software applications lies in the representation and manipulation of numeric data. Third, the relative difficulty of strategic planning (more art than science), requires guidance through the process, which usually is part of the role of consultants, and is their proprietary intellectual property (see Simon (1997)). Thus, any software attempting to implement the consulting process would have to offer guidance on how to carry out the activity (process or workflow model) and would have to offer mechanisms to interpret the findings gathered from the planning process. All this would have to be done with relatively little understanding of the (non-quantitative) data within the software. On top of this, senior managers may not even like to use the resulting software since it takes away some of the creative aspects of the planning process and forces them into a structured model of planning. These are serious challenges, which place the ‘sweet spot’ of the application of ESM software much closer to the financial analysis, budgeting, and monitoring activities than to higher levels of planning as identified by Gluck et al. (1980).

As a result, implementation of complex planning methodologies has lagged behind that of financial planning systems, and of other enterprise software. So much so, that AMR research considers ESM as the next ERP frontier (‘ERP Keeps Plugging Along as the Foundation of Enterprise Management’, AMR Research, January 10, 2001). Section 3 will offer a more detailed view into the capabilities of current planning software and the frontier of planning systems.

## 3. Current state of planning and monitoring software

## 3.1. Overview

A broad overview of leading commercial software packages for planning and monitoring was compiled in 2001 by CFO.COM (‘Top Providers of Budgeting and Planning Systems’, http://www.cfo.com/charts/1,5520,b|1|122|142|3,00.html). The survey lists no less than 31 different packages. Although not comprehensive, it shows the (volatile) spectrum of leading packages. Furthermore, according to Marr and Neely (2001), there were 28 companies alone offering BSC software that year, while http://www. findingaccountingsoftware.com lists 41 commercial software applications for planning, budgeting and forecasting. Altogether, the market for planning, budgeting, and strategy management software appears to be relatively busy and well covered.

At the same time, market overviews also reveal that few of the leading applications expand their focus beyond budgeting and financial planning. Among those that go beyond budgeting, most focus on BSC implementation and business intelligence. Only two applications of those surveyed by CFO.COM extend their scope beyond scorecarding to include strategic planning.

## 3.2. Implementations

The majority of planning packages targets the highly quantitative and internally focused planning and control processes (Phases 1 and 2) where the strengths of computational software can be put to most effective use. Present ERP technology can then enable these planning models, as ERP systems (or their extensions) are largely quantitative in nature and have access to vast amounts of internal data, generated by the organization’s transaction processes. Hence, systems such as SAPs EIS module of the R/3 system or J.D. Edwards’ Financial Planning and Budgeting enable a strong reporting capability with some planning components attached to it. Similarly, Comshare’s Management Planning and Control (MPC) software provides corresponding capabilities (more so than a basic reporting system such as SAP-EIS). Few software offerings are ‘pure’ Phase 1 planning tools, but combine Phase 1 and 2 capabilities. An overview of process, application example, and functionality is given in Table 1.

ERP solutions previously functioned more as reporting tools (Phase 1), while vendors such as Comshare, or Hyperion have offered significantly more sophisticated planning solutions (Phase 2), but these differences are becoming more blurred. Comshare’s MPC system, for instance, is a web-based software package that links and integrates quantitative data and work related to strategic planning, budgeting, forecasting, financial consolidation, management reporting and analysis. Comshare’s software has the ability to for instance represent non-quantitative organization initiatives and can tie them to metrics. The strategy planning process is methodologically not part of the system. Strategic goals are assumed as a priori given (www.comshare.com). ERP software providers have extended their reach to include increasingly sophisticated reporting tools, and many of them have moved towards enterprise monitoring via the BSC (e.g. SAP, Oracle, Peoplesoft). Similarly, Comshare now also offers a BSC module.

Table 1  
Software support for strategy management

<table><tr><td>Planning process supported</td><td>Vendor/application example</td><td>Functionality</td></tr><tr><td rowspan="2">Phase 1–2: financial planning, resource allocation, initiative planning</td><td>J.D. Edwards Financial Planning and Budgeting</td><td>Multi-level budgeting, actual-to-budget, long-range financial planning (beyond one period), what-if analysis</td></tr><tr><td>Comshare Management Planning and Control (MPC)</td><td>Planning, budgeting, consolidation, initiative planning, and management reporting</td></tr><tr><td>Phase 2–3: strategic planning based on a defined set of strategic factors in four key areas</td><td>CorVu RapidScorecard</td><td>Balanced scorecard (part of a suite of reporting, analysis, business intelligence, and modeling tools)</td></tr><tr><td>Phase 3: strategy formulation</td><td>Active strategy Active Strategy Enterprise</td><td>Balanced scorecard for monitoring. Various templates for strategic planning, such as SWOT or core process analysis</td></tr><tr><td>Phase 3–4: strategy planning, alignment, implementation, and reporting</td><td>NextStrat NextSTRAT</td><td>Encompasses entire process of strategy formulation, alignment, implementation, and tracking, using proprietary methodology</td></tr></table>

Among the pure BSC solutions (Phase 2–3), one of the widely known was Gentia’s Enterprise Performance Management (EPM) system (Gentia was acquired by Open Ratings in early 2002). Another leading product is CorVu’s RapidScorecard. However, there are many products in this busy space, and with the intellectual property being open source, they are highly similar with respect to their planning and monitoring models.

In 2002, Active Strategy’s Active Strategy Enterprise and NextStrat’s NextSTRAT software were the only two strategy management software packages explicitly targeting Phases 3 or 4. Active Strategy’s predominant component is its BSC. However, the product also promotes the vision of an Enterprise Strategy Execution Cycle (ESE) and contains several strategic planning templates, including SWOT analysis, competitive analysis and competitive advantage analysis, as well as internal core process, technology, market and customer analysis. It is not clear, however, how tightly these templates are integrated with the monitoring model of the BSC. The planning templates and scorecarding module seemingly do not share a unified data model. In contrast, NextStrat’s solution contains a unified data model and also incorporates strategic alignment as a further element in the planning process. Contrary to many other providers, NextStrat does not offer a BSC monitoring solution, but instead uses its own ‘NextAct’ monitoring and implementation management methodology (see the ‘Strategy Cycle’ in NextStrat’s 2001 whitepaper).

While seemingly the most comprehensive solution, NextStrat’s software may not be available anymore, as the company appears to have folded recently. Another ill-fated attempt at building a comprehensive strategy management software was Strategy Print, originally developed by Braxton, a strategy consulting firm acquired by Deloitte and Touche. Strategy Print was intended to map part of the strategy management process, focusing predominantly on planning. Once considered a high-profile project, which would have placed a significant portion of consultant knowledge into software, it was never completed.

A new software product that can support planning at Phase 3 is the Y-Change ESM software. Y-Change’s software can represent numerous non-quantitative planning objects, including vision, mission, initiatives, objectives, projects and tasks. Additionally, it offers support for alignment, by enabling the linking of corporate strategy with group (business unit) and functional strategies, as well as with initiatives and projects. Furthermore, it contains several tools for managing the many initiatives that large companies carry out concurrently, and for keeping track of legacy initiatives.

With relatively few existing software products extending their reach beyond Phase 3 planning support, it is worthwhile to look into the requirements for providing software-based Phase 3 or even Phase 4 planning capabilities. With the BSC market space being saturated (as well as the enterprise resource planning, portal and business intelligence software market spaces), one should expect that software companies will soon be looking for the next extension to their planning software, and ideally an extension that entrenches their software firmly within the senior management planning ranks. Furthermore, consulting companies are eager to explore this direction as well, indicated among other developments by Deloitte’s unsuccessful Strategy Print project.

## 4. Requirements for enterprise strategy management software

## 4.1. Introduction

Is it difficult to develop a high-level planning software? Section 3 identified four challenges such a planning system has to overcome. In response, the article will now identify requirements for such a system, drawn in part from the author’s expertise as former chief technology officer for a software company.

First, we have to realize that the development deliverable is not just software, but an entire process (or a ‘practice’ in the language of consultancy), consisting of methodology, software and integration model (for integration into the organization’s operational activities). Any planning tool needs an underlying methodology or point of view, which is then supported through the software’s data and process models. Hence, development of an integrated, consistent, and detailed planning model and the corresponding software are tightly linked. This is similar to the experience made during the development of the SAP software. SAPs breakthrough came with the development of ‘reference data models’ and reference process (in version R/3) which captured the essence of successful business processes, rather than generically supporting any possible process (Keller et al., 1998; Bihr and Seelos, 1997).

In addition to a consulting methodology and the software itself, a third important component is the integration model, with both technical and organizational considerations. Technical aspects include the identification and tapping of data sources, design of data extraction routines, negotiation of access rights and protocols for data security, and so forth. Organizational aspects include the management of change concerning organizational processes that are affected by the new system. To make an impact, the ‘information system’ needs to change the way in which the organization goes about its planning and implementation tasks. But any such change will need to be managed to avoid unnecessary resistance and failures. For example, the new planning process will require organization members to take responsibility for critical success factors (CSFs), and to be monitored by the measurement system. Hence, a change management process has to develop this understanding of CSF ownership responsibility, as well as the process for setting performance levels. Unfortunately, the latter part is the least predictable, as it very much depends on the current organizational culture, expertise and core values. Data models and planning processes are more predictable and can be more clearly described outside of the context of any particular organization. They will be the focus of this section.

## 4.2. Software scope

Table A1 describes the scope of the development for Phase 4 software (with the exception of the financial planning component of which there exist many implementations already). Requirements are organized by planning activity, corresponding to the planning model in Fig. 1. Not all the shown activities can be equally supported by software. Activity 1a, the representation of planning information, for instance will be relatively easy. In contrast, activity 1c, the interpretation of findings from the planning process, will be impossible to complete without planner insight, thus allowing only a rudimentary software implementation.

Among the most difficult requirements will be the strategy decomposition and maintenance tasks (activities 3a, 4a, 5a and 6a). Cascading down and roll-up of strategies is conceptually difficult. While the literature has long recognized the need to align highlevel and supporting strategies (Henderson and Venkatraman, 1993), specific, procedural planning methods have not yet been publicized.

Strategy maintenance requires planning processes that take into account an existing strategy and its objectives and initiatives, and converts it into a new strategy, instead of a planning effort that ignores the past. Planning methodologies usually do not take this point of view. Yet when organizations have hundreds or thousands of initiatives ongoing at the time when a new strategic plan is formulated, those initiatives do not suddenly disappear or get cancelled. On the contrary, they form part of the legacy upon which the new strategy needs to be built. Apparently, the only planning software that presently recognizes this need is Y-change’s ESM software. It allows a search for legacy initiatives, depiction of inter-relationships between initiatives, and can depict the relationships between (legacy) initiatives and underlying goals.

Overall, development of Phase 4 planning software is a task of considerable scope and complexity, whose need for intelligence stretches the capabilities of traditional, computational software.

## 4.3. Analytic process

The business processes strategic planning, implementation, and monitoring, need to be modeled before they can be implemented into software. Fig. 2 shows a high-level process model, in form of a data flow diagram. Fig. 2 contains the processes of strategic planning previously shown in Fig. 1, as well as the data flows between them. Each of the processes in the model can represent a number of different and possibly interchangeable planning techniques. For example, environment analysis might be carried out using Porter’s competitive forces model, or Schoemaker’s Scenario Planning technique, or one of several other techniques. Based on the specific technique or techniques used, the process will have a number of well-defined outcomes, i.e. data items, here shown as trends, uncertainties, competitor goals, competitor resources, opportunities, and threats.

To successfully complete the modeling process, analysts and planners have to cooperate and jointly map out the process. This is not a straightforward exercise. In practice, strategic planners are often unable to explain their own planning processes (Hansson, 2002). Much of the literature describes strategic planning techniques not in ‘how to’ form, with clearly outlined process steps, but instead describes the framework structure, and the process outcome. The how to is considered the consultant’s domain. Consultants, however, use so many different variants of the same process, that it is difficult for them to blueprint a single reference process. Also, they are not particularly eager to give up a process that took years to develop so that it can be built into software and becomes shared knowledge. Hence, extracting a ‘generic’ planning process and formalizing it sufficiently so that it can serve a range of planning situations is one of the obstacles for the development of this type of software.

![](/api/attachments/8T6GAX48/fulltext/images/e15eb74f56cd8886189eca16a0b70fe7d6324a06e1207f62677c6ec6f2dd8a5e.jpg)  
Fig. 2. High-level data flow diagram for enterprise strategy management.

A detailed and complete process model will contain more than one hundred different processes, many of which will be elementary data input processes. For example, an elementary data input process may be ‘define current company products’. Many of the processes will be impossible to automate fully, due to their need for planner or consultant intelligence. For example, once products are defined (as part of Internal Analysis), follow-up activities might include defining shared product platforms, and then extracting the organization’s core capabilities. Ideally, we would want the software to have enough insight to perform these tasks, i.e. deriving core capabilities from knowledge about product platforms. But in reality, each of these activities relies almost exclusively on the intelligence and abilities of the planners. The main role of the system is to capture the results, store them, and re-display them later in the context of another planning activity. This is an important insight in the process design itself. The system will not be expected to ‘compute’ a new strategy, but instead will be designed to capture the process and its outputs so as to create efficiencies (e.g. 50% or more time savings) during the planning process, to enable significantly tighter integration between planning and implementation, and to provide a knowledge repository for future strategy modifications. The paradigm for this type of support is analogous to that described by Nunamaker et al. (1991): the software amplifies process gains, while reducing process losses.

## 4.4. Organizational process (business use case)

The design (and subsequent implementation) process will also need to model the organizational aspects of the planning activity. For example, the analytic activity ‘list specific core capabilities for the department’, in organizational terms means, ‘members of the department meet on a quarterly basis and jointly brainstorm to identify any strengths. They then aggregate repeatedly mentioned, persistent strengths, to identify core capabilities’. While the analytical and the organizational activities are essentially identical in the core activity and the outcome, the first one considers only the informational side (input of core capabilities), while the second one considers the “how to” of performing the task. Detailed design of business use cases (see for instance Sparks (2000), or www.iconprocess.com) is crucial for a faithful representation of the desired process and a suitable software design.

The resulting organizational model should contain workflows, activities, data elements and documents (artifacts), people who perform the planning tasks (stakeholders) and their roles, plus information on frequency of activities, and indicators for when an activity can be started, or when it is finished.

The organizational aspects of planning suggest the following generic software functionalities:

1. Data capture, recording, and reporting capability for all relevant data objects within the strategy. This feature already exists in all current planning tools as a minimum requirement.

2. Links to live data feeds to allow updates of trend information, capability information, or measurement of progression towards strategy implementation. Many planning tools already contain data feeds to internal data. Some portals and executive information systems can accept external feeds. Much of this capability is well structured, while planning requires a broad search and serendipitous fact discovery (El Sawy, 1985).

3. Groupware for brainstorming, idea sharing, idea categorization, and idea prioritization. These components are not part of typical planning software, but are part of separate group support systems.

4. Workflow tools to structure the strategy formulation and implementation workflow, to send triggers upon detection of deviation from plans, and to provide closed-loop reporting, informing the decision making team when a plan deviation has been corrected. Workflows are not part of typical planning software products.

## 4.5. Model details: process and data

This section demonstrates in more detail the procedural and data aspects of planning software. The illustrations will focus on parts of Schoemaker’s Scenario Planning technique. Two articles by Schoemaker (1992, 1995) serve as useful examples, as they describe the procedural and data elements in considerable detail.

## 4.5.1. Process model illustration

Table A2 illustrates the details for the process ‘Constructing Scenarios for Scenario Planning’ (Steps 1 and 2 only). Schoemaker focuses largely on the analytical aspects of the process, but nevertheless also offers some suggestions for organizational aspects, namely the use of group process. The process description also suggests the use of ‘default’ lists, such as a list of typical stakeholders. This is part of consultant knowledge, but can be easily implemented in software, thus adding to the software’s usefulness and perceived ‘intelligence’.

## 4.5.2. Data model illustration

Given the relative size of the strategic planning process, a strategic planning data model easily consists of more than one hundred ‘planning objects’. To illustrate, if one extracts just the main data elements from Schoemaker’s (1992) Scenario Planning, the model already reveals nine major objects (see Table A3). However, any analytical planning object (as listed) may eventually become several objects within the software, as organizational planning processes may necessitate a separation between objects depending on the process step. For example, planners may only be interested in core capabilities as an output, but nevertheless, the data model also needs to represent a larger set of generic capabilities, as the planning process derives core capabilities from an analysis of generic capabilities.

Strategy planning ‘reference data models’, such as the one briefly sketched out in Table A3, are still in their infancy. The development of such models is hampered for instance by the fact that the different strategic planning models introduce semantically related, yet different concepts (e.g. strength versus competency versus core competency). Hence, the designer’s task requires the choice of one set of consistent planning methodologies and then the implementation of that ‘point of view’ within the data model. Consequently, organizations adopting such software will also need to subscribe to the point of view of the chosen strategic planning model.

## 4.6. Use of enterprise strategic management software in practice

The operational model for this next generation of ESM is an iterative 3-cycle model. Cycle 1 is the planning cycle. The senior planning team, possibly supported by consultants, convenes to define or re-define a strategy. Analysts will have carried out prior work to elicit information about factors such as organization capabilities, competitors, market needs, and so forth. This information, gathered over several weeks or months, will reside in the system in well-structured databases (based on the planning model’s object model).

The planning team then carries out a well-structured planning process, moderated by a senior planner or consultant, and supported by the software. The software provides inputs (facts the planners have to know in the context of the planning task), offers the templates, defaults, and mechanisms for the planning activities (process model) and at the same time captures results. After the conclusion of the planning process, the strategy resides in the system in a well-structured form, from where it can be shared and re-used, distributed in form of printed reports, or extracted via queries.

Cycle 2 is an integration cycle, consisting of both technical and organizational integration activities. At the organizational level, issues such as leadership roles and responsibilities for measures and targets are negotiated and agreed upon, while at the technical level, access points are set up to the proper data sources. For example, depending on the organization’s definition of ‘revenue’ or ‘ROI’, the data items accessed and computed can differ significantly. This is a non-trivial process, which identifies data sources within the corporate databases and ERP systems. From these, the relevant data is extracted via an extraction-transfer-load (ETL) system and presented via a reporting or an on-line analytic processing (OLAP) system. Other data sources might be defined as external, and data may have to be fed into the system manually, or possibly preprocessed by analysts.

Cycle 3 is a monitoring, measurement, and ‘control’ cycle similar to strategy measurement via BSC systems. The main advantage of having an integrated system and Cycle 1 (and Cycle 2) carried out, is that any implementation under-performance can be linked back to the planning model. Hence, the impact of missed targets on the strategy can be better understood, and can be potentially used to trigger a new Cycle 1 (plan revision), as part of a closed-loop planning model.

According to the organization’s planning cycles, or when significant performance gaps are experienced, the organization can initiate another Cycle 1. The next planning cycle will not be a clean-sheet strategy cycle, but one that is based on the planning information from the previous cycle, as well as the updates generated during the monitoring process. Hence, the organization now possesses a ‘knowledge management system’ for strategic planning.

## 4.7. Role of the web in the ‘post-net era’

Networking capability, and especially internetworking, plays a fundamental role in the process design for three reasons: internal information collection, internal strategy information dissemination and monitoring, and external data gathering.

First, any ESM system relies on data inputs from all parts of the organization. In the past, strategies were often lacking in quality because they were based on incomplete and incorrect data. Either senior management was ‘supposed to know’ characteristics such as the capabilities of their organization units, or teams of consultants were commissioned to gather quickly the information as part of a one-off effort. The new model of strategic management foresees an ongoing planning process were organizational information is continuously captured by those who directly deal with the information.

Second, to be successful, strategies need to be communicated and their implementation be monitored. Pre-net executive information systems provided strategy information only to high-level staff within the organization (Top 1%), largely for reasons of feasibility and cost. Per-seat investment in these EIS frequently amounted to tens of thousands of dollars. Web-based information portals enable information dissemination to the entire organization, at per-seat costs of hundreds of dollars (or about 1% of former cost). Furthermore, data from multiple internal sources can be drawn into the same portal, so that database integration at the desktop level becomes a reality. Compare for instance Auditore (2001) for the impact and ‘disruptive effect’ of enterprise information portals.

Third, Internet access can play a vital role in offering access to external data for use in environmental scanning. El Sawy (1985) pointed to the use of EIS for environmental scanning, while Watson et al. (1991), found that a large percentage of EIS provided access to external information already during pre-net times, such as news services, stock market data, or trade/industry data. Still, the goal of the planning system to independently search the Internet, harvest all valuable information while leaving all irrelevant information behind, and then presenting that information in a concise manner is an elusive one. Intelligent agent software will hopefully soon help in this activity, but substantial work lies ahead for the development of intelligent agents, and possibly the indexing and structuring of information (e.g. via XML), before environmental scanning can be highly automated.

## 5. Beyond post-net: new views of strategic planning and their potential impact on enterprise strategy management systems

With current ESM systems still lacking Gluck’s Phase 3 and 4 capabilities, it is nevertheless important to look beyond Gluck’s model and reflect on more dramatic changes in planning systems. After all, if all organizations adopt the above-mentioned, somewhat mechanistic planning approaches, followed by the use ERP systems to implement them, and then followed by performance measurement via the de facto standard BSC, strategic planning and implementation may finally become manageable, but also predictable.

## 5.1. Alternate views of strategy: images and sense making

Cummings and Wilson (2003), extending the work of Mintzberg et al. (1998), advocate a new and less mechanistic perspective on strategy (or better: multiple views of strategy) with increased consideration of subjective, personalized views. Applying the metaphor of an image or map, they discount the importance of the accuracy of the metaphorical map but stress its use (which creates a planning process) and the choice of imagery chosen for the map (representing a point of view or interpretation of the future). The book by Cummings and Wilson also includes an article by Galliers and Newell (2003), which portrays strategy as ‘data and sense making’, namely, deriving meaning from data. Elsewhere, Blanco et al. (2003) put forward new models of sense making, through the interpretation of weak signals. Similarly, the use of visualizations and rich pictures has been part of scenario planning and change management (Ragsdell, 2000) and knowledge management (Brown, 2001; Smolnik and Erdmann, 2001; Eden and Ackermann, 1998), as well as several systems development methodologies, including soft systems methodology (Checkland, 1981) and UML (Sparks, 2000). Hence, pictures and visualization are seen as increasingly important in organization planning at even the highest level. Nevertheless, few IT applications incorporate visualization into planning, or link data to visualization (sense making) in significant ways.

## 5.2. Applicable technologies: pre-net, net, and post-net

Information systems developers have relatively few fundamental technologies they can employ in their development activities, namely: computational power, database, network, intelligence, sensors, and multimedia. While all these technologies have rapidly advanced, their essence has remained the same. Notably, not all these technologies have been equally used in the development of planning systems. Computational power, the raw speed provided by computers vis-a-vis conventional processing is the most basic advantage of computing and has been applied in planning early, on when companies created large (but ineffective) MIS reporting systems. Still in the pre-net era, the addition of intelligence together with small uses of database and rudimentary visualization (multimedia) led to decision support systems, executive information systems and related applications (Fahy, 2002). The net era leveraged the power of the network, vast databases (data warehouses), and some remote sensing capability to create business intelligence, and distributed organization-wide planning systems, as discussed above. The two technologies that have been largely overlooked, visualization (multimedia) and remote sensors are therefore obvious sources for further exploitation in future systems.

## 5.3. Planning tools that exploit visualization and remote sensors

Even today, companies such as SAP are trying to offer users better ways to interpret their data, by creating ‘war rooms’ or a ‘management cockpit’ (Georges, 1997) to depict key parameters of organizational performance on numerous displays in parallel. Yet these systems are not creating a holistic image of the organization and its strategic path as of yet, but instead show numerous individual measures. If an organization formulated its desired future and its present in form of a rich picture, then the change process from present to future would become a ‘movie’ during which the organization would ‘morph’ into its new state. Significant, unexpected changes in environmental conditions (via remote sensors) or organizational performance would change the movie’s storyboard and eventually rewrite the outcome. Alternatively, an organization would already have defined multiple outcomes (scenarios) and ‘movies’, and successively evaluate the likelihood of each of the outcomes, and evolving stories.

At present, such a planning process implementation would appear far-fetched, given its playfulness and the unavailability of needed technologies. Furthermore, the images created would not be part of a movie, but instead resemble a role playing game. With the very significant advancement in game technology, already today there are numerous ‘game engines’ available (e.g. ‘Unreal’ by Epic Games) which are well parameterized and thus can generate various games, if supplied with the necessary data for characters, scenes, interaction and so forth. And, contextual virtual reality prototypes have already been prototyped for applications in marketing and R&D to depict a product in use before it exists (Malhotra, 2002; Manninen, 2000; Miliano, 1999). Today’s senior managers may not readily adopt such visualization tools for their strategic planning activities, but the next generation of executives may find this the most natural way to simulate future scenarios and to explore alternative courses of action in a holistic manner.

## 6. Summary and conclusions

ESM systems still lack the capabilities to support sophisticated strategic planning processes (i.e. Phase 3 or 4 in Gluck et al.’s (1980) model). There are several reasons for this situation. To some extent, planning systems have not yet shed their heritage as performance measurement systems. This is still the prevailing and shared model for planning systems. Relying on the strengths of data computation and presentation, they forego non-quantitative planning activities. While it is important to measure, the measurement activity must however not be the ultimate goal, but a means to better planning and implementation. Yet, the lack of a well-defined and sufficiently detailed strategic planning and implementation methodology has hindered the evolution away from quantitative measurement. Furthermore, there has been relatively limited need for software that supports strategic planning on a frequent basis, as strategic planning has been an infrequent exercise, often supported by outside consultants who would manage the process, capture the findings, and generate reports.

The next generation of ESM systems needs to operate differently. It must be based on the principle that measurement systems are significantly more useful if they are connected back to a (non-quantitative) planning and management system and therefore business objectives (Singh et al., 2002), and that managerial planning approaches are significantly more impactful when linked forward to a measurement system that measures the success of a strategy (Fahy, 2002). Furthermore, future strategic planning has to be understood as an on-going activity that enables companies to define and redefine strategies under increasingly competitive conditions.

Consequently, such systems will contain both planning and measurement components. The planning component is not a computerized consultant or an expert system for strategy planning, but a support system that provides senior planners with workflow, data structures and planning techniques to ensure the input of sufficient data, structuring of that data, and the development of outputs required for the planning process. Some guidance, checklists, and advice will be possible, but the cognitive effort will largely remain with the planners or consultants. Nevertheless, the structure of the process, the well-defined inputs and outputs, the reusability and maintainability of strategies, and the seamless integration between planning and measuring, promises significant improvements in speed and effectiveness of strategy implementation.

The word ‘system’ is inadequate to describe this new type of strategic information system. It is better understood as a new enterprise management practice, at whose core there is support through information technology. While such practices are clearly feasible with today’s technologies (and have already been created by a few companies), their impact and benefit remain to be demonstrated. Singh et al.’s (2002) study offers a sobering insight on this issue. Singh et al. found that process support was not a critical factor for the success of an EIS (their terminology), regardless of the process being environmental scanning, strategy formulation, implementation or control (monitoring). Only the link to corporate objectives proved to be a success determinant for such systems. However, since most leading planning systems today do not implement a significant strategy management component, those surveyed by Singh et al., may never have experienced real support for strategy management.

Beyond this next generation, we might envision a completely new paradigm for ESM systems, one which seeks to create more holistic planning models and uses rich imagery for their capture. Such systems would rely on new developments in virtual reality and gaming that would allow the rendering of multiple future worlds, and the paths towards them.

## Acknowledgements

This research was supported in part by CERG Grant CityU 1151/02H. The author thanks the editors and reviewers for their insightful comments and improvement suggestions, especially with respect to the ideas in Section 5.

## Appendix

## Tables A1–A3.

Table A1 Scope of the planning software

<table><tr><td>Planning activity</td><td>Requirement</td><td>System requirement</td></tr><tr><td rowspan="3">1. Strategic planning</td><td>a. Ability to represent information gathered via different planning models</td><td>Reference data models for major planning methodologies (data structures, data model, database)</td></tr><tr><td>b. Ability to support the ‘how to’ process of different planning models</td><td>Workflow, reference process model, consulting knowledge on how to carry out a planning task. Consulting intelligence on how to complete the information gathering tasks</td></tr><tr><td>c. Ability to interpret the findings from a planning activity and to feed its findings as inputs into another planning task</td><td>Consultant intelligence. Consistent data models and well defined data feeds/work flow connectivity</td></tr><tr><td>2. Strategic planning intelligence</td><td>a. Ability to recognize changes in external or internal environment conditions on which the strategic plans hinge</td><td>External data feeds. Intelligent search capability. Data mining/ profiling</td></tr><tr><td>3. Planning maintenance</td><td>a. Ability to modify existing plans and to understand the impact of plan changes on downstream activities, such as initiatives in progress</td><td>Reference data and process model which incorporate historical data, and multiple strategy versions</td></tr><tr><td>4. Plan decomposition/ alignment</td><td>a. Ability to delegate part of a strategy to another group. Ability to roll-up results and determine changes and inconsistencies</td><td>Delegation. Iterative strategy formulation with ‘version management’ and history management. Change propagation from high-level strategies to lower level strategies. Change requests to push lower level strategies upwards. Planners can review previous versions of a strategy and detect + changes</td></tr><tr><td rowspan="2">5. Implementation planning</td><td>a. Initiative management. Understanding the role of initiatives (link to goals, alignment). Understanding interactions between initiatives (sequence, logical dependence). Project (initiative) management capability</td><td>Reference data model, workflow model, project management techniques</td></tr><tr><td>b. Measurement and control. Ability to define measures that capture strategic goals and their implementation ‘objectives’. Ability to assign responsibility, targets, and alerts when targets are missed</td><td>Measurement system similar to balanced scorecard, with multiple perspectives, objectives, measures, targets, responsibilities, alerts</td></tr></table>

(continued on next page)

Table A1 (continued)

<table><tr><td>Planning activity</td><td>Requirement</td><td>System requirement</td></tr><tr><td rowspan="2">6. Implementation planning maintenance</td><td>a. Management of legacy initiatives and non-strategic initiatives</td><td>Reference data model with project version management, project change management version comparison checking. Search capability for initiatives/projects</td></tr><tr><td>b. Feedback system</td><td>Triggers that initiate or alert to planning functions (re-work)</td></tr></table>

Table A2  
Planning method detail: constructing scenarios for scenario planning (Activities 1 and 2, out of 10)

<table><tr><td>Planning activities</td><td>Detailed activity</td><td>Activity description</td><td>Data Elements</td></tr><tr><td rowspan="3">Define scope</td><td>Set time frame</td><td>Consider rate of technology change, product life cycles, political elections, competitor planning cycles</td><td>Time frame (output).External time frame (input)</td></tr><tr><td>Set scope of analysis</td><td>Define products, markets, geographic areas, technologies</td><td>Product, market, region, technology (all outputs)</td></tr><tr><td>Determine most important sources of information</td><td>‘What do you wish you had known in the past, that you know now?’Identify past sources of uncertainty and rate of volatility, and extrapolate into the future. Group process</td><td>Information source (output) with type attribute (e.g. uncertainty), and volatility attribute (e.g. low/high)</td></tr><tr><td rowspan="3">Identify major stakeholders</td><td>Identify stakeholders</td><td>Create list of relevant stakeholders.Default list includes: customer, supplier, competitor, employee, shareholder, government</td><td>Stakeholder (output)</td></tr><tr><td>Identify stakeholder roles</td><td>Identify roles, interests, and power positions of stakeholders</td><td>Stakeholder (input).Stakeholder role—present (output)</td></tr><tr><td>Identify stakeholder role change</td><td>Identify how roles have changed over time, and rationale for change</td><td>Stakeholder role—past (output) with rationale attribute, stakeholder role—present (input)</td></tr></table>

Based on Schoemaker (1995).

## Table A3

Key elements of a strategy management data model

<table><tr><td>Data item</td><td>Description</td></tr><tr><td>Scope</td><td>‘Angle of view’ for the strategy definition. For example, domestic versus international. Defines what is considered and what is not</td></tr><tr><td>Stakeholder</td><td>Outside players who need to be considered in the strategy formulation because they have enough influence to affect the organization’s performance(continued on next page)</td></tr><tr><td>Scenario</td><td>A state of the world described by all trends combined with a set of uncertainties. Based on a time frame, scope, and stakeholder definition</td></tr><tr><td>Trend</td><td>A highly likely future influence on some aspect of the world. Examples include economic, political, societal, technological, or industry trends. Trends are described by ‘what they do’ and their impact</td></tr><tr><td>Uncertainty</td><td>An unlikely influence on some aspect of the world. For example, strength of the economy, or industry structure, or technology breakthrough</td></tr><tr><td>Segmentation criterion</td><td>Factors by which the industry can be meaningfully separated (e.g. by product, distribution, application, or market)</td></tr><tr><td>Industry segment</td><td>Part of the industry, defined based on a combination of values of particular segmentation criteria (e.g. particular product in a particular market, distributed in a particular way)</td></tr><tr><td>Core capability</td><td>Assets, skills, resources that are part of the ‘fiber’ of the organization and which are difficult to imitate or replicate by others (i.e. cannot be ‘bought off the shelf’)</td></tr><tr><td>Core capability matrix cell</td><td>Data element that describes the mapping between core capabilities and industry segments. Answers the question to what is needed to successfully compete in a given industry segment within a given scenario</td></tr></table>

Based on Schoemaker (1992).

## References

Anderson, A., 2002. Real-time wisdom. MSI 20(4), 36–40.

Auditore, P.J., 2001. The emerging enterprise information portal market. Enterprise Systems Journal 16(1), 32–34.

Avison, D.E., Eardley, W.A., Powell, P., 1998. Suggestions for capturing corporate vision in strategic information systems. OMEGA 26(4), 443–459.

Baum, J.R., Wally, S., 2003. Strategic decision speed and firm performance. Strategic Management Journal 24, 1107–1129.

Bihr, H., Seelos, H.J., 1997. Entwicklung eines Referenzdatenmodells fu¨r Krankenha¨user (realizing a reference data model for hospitals). Wirtschaftsinformatik 39(4), 367–371.

Blanco, S., Caron-Fasan, M.L., Lesca, H., 2003. Developing capabilities to create collective intelligence within organizations. Journal of Competitive Intelligence and Management 1(1), 80–92.

Brown, J.S., 2001. Storytelling—scientist’s perspective, in Storytelling: Passport to the 21st Century, available at http://www2.parc.com/ops/members/brown/storytelling/jsb.html.

Carpenter, M.A., 1986. Planning vs strategy—which will win? Long Range Planning 19(6), 50–53.

Checkland, P.B., 1981. Systems Thinking, Systems Practice, Wiley, London.

Coveney, M., 1998. Budgeting: strategic initiative or corporate induced waste of time? Credit Control 19(2), 18–21.

Cummings, S., Wilson, D., 2003. Images of strategy. In: Cummings, S., Wilson, D. (Eds.), Images of Strategy, Blackwell, Oxford, pp. 1–40.

Eden, C., Ackerman, F., 1998. Making Strategy, Sage, Beverly Hills, CA.

El Sawy, O., 1985. Personal information systems for strategic scanning in turbulent environments: can the CEO go on-line. MIS Quarterly 9(1), 53–60.

Fahy, M., 2002. Strategic Enterprise Management Systems: Tools for the 21st Century, American Institute of Certified Public Accountants.

Freeman, L.N., 2001. Measure performance with a balanced scorecard. Ophthalmology Times 26(24), 17.

Galliers, R., Newell, S., 2003. Strategy as data plus sense-making. In: Cummings, S., Wilson, D. (Eds.), Images of Strategy, Blackwell, Oxford, pp. 164–196.

Georges, P., 1997. How management cockpits facilitate managerial work. Unpublished manuscript, available at http://www.management-cockpit.net/download\_ref.htm.

Gluck, F.W., Kaufmann, S.P., Walleck, A.S., 1980. Strategic management for competitive advantage. Harvard Business Review 58, 154–161.

Hackett, G., 1998. Prime your planning process. Financial Executive 14(5), 45–46.

Hamel, G., 1999. Bringing silicon valley inside. Harvard Business Review 77, 70–84.

Hamel, G., Doz, Y.L., Prahalad, C.K., 1989. Collaborate with your competitors and win. Harvard Business Review 67.133-139

Hansson, J., 2002. Management of Knowledge Transfer in Knowledge Service Firms, Proceedings EURAM 2002, Innovative Research in Management, Stockholm Sweden.

Hax, A.C., Majluf, N.S., 1996. The Strategy Concept and Process. A Pragmatic Approach, Prentice-Hall, Englewood Cliffs, NJ.

Henderson, J.C., Venkatraman, N., 1993. Strategic alignment: leveraging information technology for transforming organizations. IBM Systems Journal 32(1), 4–16.

Hill, W.L., Jones, G.R., 2001. Strategic management: an integrated approach. Houghton Mifflin.

Hitchin, D.E., 2002. Lessons from the tech wreck. The Journal of Business Strategy 23(1), 24–26.

Kambil, A., 2000. Fast venturing: the quick way to start web businesses. Sloan Management Review 41(4), 55–67.

Kaplan, R.S., Norton, D.P., 1996. Using the balanced scorecard as a strategic management system. Harvard Business Review 74, 75–85.

Kaplan, R.S., Norton, D.P., 2000. Having trouble with your strategy? Then map it. Harvard Business Review 78, 167–176.

Keller, G., Ladd, A., Curran, T., 1998. SAP R/3 Business Blueprint: Understanding the Business Process Reference Model, Prentice-Hall, Englewood Cliffs, NJ.

Leauby, B.A., 2002. Know the score: the balanced scorecard approach to strategically assist clients. Pennsylvania CPA Journal 73(1), 28–32.

Malhotra, P., 2002. Issues Involved in Real-time Rendering of Virtual Environments. Unpublished Master’s Thesis, College of Architecture and Urban Studies, Virginia Polytechnic Institute and State University, Blacksburg, Virginia.

Manninen, T., 2000. Contextual virtual reality prototyping: co-operative user-centered design using distributed simulations. Proceedings NordiCHI2000, October 23–25, Stockholm, 1–2.

Marr, B., Neely, A., 2001. The Balanced Scorecard Software Report, InfoEdge.

Miliano, V., 1999. Unreality: Application of a 3D Game Engine to Enhance the Design, Visualization and Presentation of Commercial Real Estate, Proceedings of the Conference on Virtual Systems and Multimedia, September 1–3, Dundee.

Mintzberg, H., Ahlstrand, B., Lampel, J., 1998. Strategy Safari: A Guided Tour through the Wilds of Strategic Management, Simon and Schuster, New York.

Montgomery, P., 2002. Effective rolling forecasts. Strategic Finance 83(8), 41–44.

Nunamaker, J.F., Dennis, A.R., Valacich, J.S., Vogel, D.R., George, J.F., 1991. Electronic meetings systems to support group work. Communications of the ACM 34(7), 41–61.

Oliver, R.W., 2002. Cold strategy, hot strategy. The Journal of Business Strategy 23(1), 6 – 8.

Paul, D., 2000. World-class planning and decision-making. Financial Executive 16(6), 56–57.

Porter, M.E., 1980. Competitive Strategy, Free Press, London.

Prahalad, C.K., Hamel, G., 1990. The core competence of the corporation. Harvard Business Review 68(3), 79–91.

Ragsdell, G., 2000. Engineering a paradigm shift? An holistic approach to organizational change management. Journal of Organizational Change Management 13(2), 104–120.

Schoemaker, P.J.H., 1992. How to link strategic vision to core capabilities. Sloan Management Review 34(1), 67–81.

Schoemaker, P.J.H., 1995. Scenario planning: a tool for strategic thinking. Sloan Management Review 36(2), 25–40.

Simon, G.A., 1997. What to share? Journal of Management Consulting 9(4), 2–3.

Singh, S.K., Watson, H.J., Watson, R.T., 2002. EIS support for the strategic management process. Decision Support Systems 33(3), 71–85.

Smith, M., 2002. Business planning or business performance management, Intelligent Enterprise, available at http://www.intelligententerprise.com/online\_only/analyst/020924.shtml.

Smolnik, S., Erdmann, I., 2001. Visual navigation of distributed knowledge structures in groupware-based organizational memories. Business Process Management Journal 9(3), 261–280.

Sparks, G., 2000. An introduction to UML: the use case model, Sparxsystems whitepaper.

Van Yoder, S., 2001. Research at web speed. Financial Executive 17(3), 40–42.

Watson, H., Rainer, R.K., Koh, C., 1991. Executive information systems: a framework for development and a survey of current practices. MIS Quarterly 15(1), 13–30.

Watts, R.M., 2002. Strategies for market disruptions. The Journal of Business Strategy 23(3), 19–22.
