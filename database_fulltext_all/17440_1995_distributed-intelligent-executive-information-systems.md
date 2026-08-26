---
otero_id: 17440
otero_key: "N3BVJU8A"
title: "Distributed intelligent executive information systems"
authors: "Robert T. Chi; Efraim Turban"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00006-e"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Distributed intelligent executive information systems

Robert T. Chi $^{*}$ , Efraim Turban

Information Systems Department School of Business Administration California State University, Long Beach, Long Beach, CA 90840-1003, USA

## Abstract

Executive information systems (EIS) have been successfully implemented in many organizations. Of all the various EIS commercial products, only one (Executive Edge) presents limited artificial intelligence (AI) capabilities. Yet, the ability to include various problem solving agents for collaboratively information processing, filtering and presentation, is highly desirable. It is possible that the successful EIS systems of the future will be built around AI components (expert systems, learning mechanisms and so on..), so that more efficient and effective information processing for executives can be achieved. Since much of executive processing involves complicated problem domains, a single's AI agent effort may be insufficient when the information is broad in scope and complicated in nature. For such situations we propose in this paper a framework called distributed intelligent executive information system (DIEIS). This framework illustrates how multiple resources (consisting of knowledge learning, reasoning, filtering and presentation) can be combined for information processing in an EIS environment. For example, a particular piece of information may be refined and presented based on past experiences and current practices in a particular problem domain with the help of both an expert system and neural computing. The DIEIS framework allows multiple agents to work collaboratively to help complex information processing.

Keywords: Executive information systems; Executive support systems; Artificial intelligence; Distributed artificial intelligence; Distributed intelligent executive support systems

## 1. Introduction

Executive Information systems (EIS) have been initially designed to focus on, monitor, filter, and organize executives' information, so that the executives can make more effective use of computerized information. In general, the goals of EIS (Watson et al. 1992) are (1) to reduce the amount of data bombarding the executive, (2) to increase the relevance, timeliness, and usability of the information that reaches the executive, (3) to focus a management team on critical success factors (4) to enhance executive follow-through and communication with others, and (5) to track early warning indicators: such as competitors' moves, or customer demands. In short, it is a tool that supports the executive in identifying major problems and/or finding opportunities (see phase I in Fig. 1) and in taking appropriate actions (see phase II in Fig. 1). EIS is also used for enhancing communication.

It has been recognized recently that the first generation of EISs, which intended to support mainly the identification of problems and opportunities (Phase I in Fig. 1) should be enhanced with decision making capabilities (Phase II). Thus, a second generation of EISs has been termed Executive Support Systems (ESS) (Rockart and Delong 1988). It includes several analytical tools for decision support. Indeed, most EIS vendors provide tools that are intended to build some kind of ESS (e.g., providing DSS capabilities, such as modelling in addition to the conventional EIS capabilities). For example, Commander EIS works with system W, Executive Edge with IFPS plus, Express/EIS with Express and Command Centre EIS works with Advantage/G.

Current EIS are composed of several software components which provide capabilities such as:

(1) Drill down capabilities (an intelligent agent can help in identifying what is going wrong, saving drill down time. Thus, the agent can act as a director for drill down).

(2) Information monitoring: usually a CSF methodology is used to decide what information to track.

(3) Access to aggregate (global) information.

(4) Extensive use of external data.

(5) Written interpretations.

(6) Highlights problem indicators.

(7) Ad-hoc analysis.

(8) Information presentation in hierarchical form.

(9) Incorporating graphic and text in the same display.

(10) Providing management with exception reports.

(11) Showing trends, ratios and deviations.

(12) Providing access to historical and most current data.

(13) Being organized around critical success factors.

(14) Having forecasting capability.

(15) Filtering, compressing and tracking critical data.

(16) Supporting open-ended problem explanation.

The execution of some of these capabilities requires expertise. Providing such expertise man-

![](/api/attachments/N3BVJU8A/fulltext/images/7e3cb13cb15bbbb07cab5d9f9d3a958420ec08ad4e297e36f8bb6689541bf14c.jpg)  
Fig. 1. The decision making process of an executive (the arrows indicate flow of information). Source: (Turban 1993).

Table 1  
The characteristics of DIEIS and EIS

<table><tr><td></td><td>Problem solving agents</td><td>Expertises</td><td>Nature of problem solved</td><td>Automation of problem solving</td></tr><tr><td>EIS/ESS</td><td>One (or more)</td><td>Homogeneous</td><td>Narrow</td><td>None, or limited</td></tr><tr><td>DIEIS</td><td>Several</td><td>Heterogeneous</td><td>Complex</td><td>Multiple, extensive</td></tr></table>

ually may be expensive. Therefore, it makes sense to automate the process. Executive decisions are very complex and therefore they are frequently partitioned into subproblems. These subproblems are analyzed by experts who work individually, or by a task force of experts who work on a problem collectively. Attempts to provide computerized support to this kind of approach falls under two titles: distributed decision making (DDM) and group decision support system (GDSS). The topic of DDM is used as a foundation to the framework proposed in this paper. The topic of GDSS will not be treated here (for details see Jessop and Valacich (1992)). Distributed decision making (DDM) is a computerized coordinated decision making effort among communicating individuals which possess some specialized knowledge and can process the knowledge in a manner that contributes to performing some intelligent tasks involved in the decision process (Ching 1988). As a potential enhancement of EIS, distributed information processing can be supported by a computer system with the characteristics of distributed participants and various expertises. A distributed intelligent executive information system (DIEIS) is defined in this paper as a “computer system support for executive distributed information processing with heterogeneous problem-solving participants and expertises”.

![](/api/attachments/N3BVJU8A/fulltext/images/4a1e939cb1b53b5428ca2429ddd313c55fa1b27ff9dffc90658ca2c4966404d6.jpg)  
Fig. 2. Intelligent ESS.

A typical ESS framework offers single information processing mechanism, while a DIEIS focuses on multiple problem solving mechanisms and heterogeneous expertises (see Table 1).

Note that a typical EIS or even DSS does not include any automatic intelligent problem solving mechanism. The DIEIS provides such a mechanism. In other words, when the executive poses a question to the computer, an intelligent answer can be provided. The framework of DIEIS go beyond EIS by incorporating a distributed artificial intelligence (DAI) architecture into the information processing system. The objective of this paper is to describe a framework for a DIEIS. The paper is composed of the following parts: in section 2, a review of previous research is presented. In section 3, a conceptual model of DIEIS is introduced and in the last part conclusions are drawn and future research is outlined.

## 2. Computerized support to executive decisions

Since executives (and their assistants) perform a variety of tasks, it is logical to propose a support system with multiple expert systems. The logic for such an architecture is that expert systems (ES) and or other intelligent agents are confined to narrow domains. Therefore, a single ES can not support all tasks. Turban and Watson (1989) proposed such a system (Fig. 2). In their system, there are 7 intelligent agents, each performing a specialized task.

The idea of using several ES to support an single EIS can be expended along another dimension. While the Turban and Watson's system supported the various components of the EIS, on a one to one basis, it is possible to support the various tasks of the process. A system proposed by Wang and Turban (1993) is an example for a support provided to environmental scanning and interpretation activities. Another way to view a support by several systems is to visualize an executive who solicits advice from several experts, each specializes in a narrow domain (e.g. labour relations, investment, productivity improvements.)

The problem with having several automated agents supporting one EIS is basically that of implementation. Even if all ES are programmed with the same language or tool, they are basically stand-alone systems. To support an EIS, these systems need to be integrated and coordinated. The basic idea is to automate the process as much as possible. Namely, the executive as a user would like (ideally) to be able to execute his (or her) job with the help of electronic agents. For example, the executive expects the system to identify problems (opportunities) and to propose solutions! As far as the executive is concerned, the EIS should be a “black box”.

## 3. Relevant research in DAI

## 3.1. Definitions

A number of research areas deal with the support of distributed problem solving processes. To better understand our proposed framework, we define first the concept of Distributed Problem Solving (DPS): “Distributed problem solving is the cooperative solution of problems by a decentralized and loosely coupled collection of knowledge sources (KS’s) (procedures, sets of rules, etc.), located in a number of distinct processor nodes” (Smith and Davis 1981). The focus of distributed problems solving systems research (Decker 1987) is on the nature of the distributed problems and on the multi-agent environment constructed to solve these problems. Such systems are also known as distributed artificial intelligence (Huhns 1987), cooperative knowledge-based systems (Croft and Lefkowitz 1988), and group problem solving systems (Shaw and Fox 1991).

## 3.2. Limitations of current executive information systems

Current EIS emphasize knowledge retrieving, knowledge filtering and knowledge presentation based on a single processing mechanism (Elofson and Konsynski 1992). The information needed to support EIS has the characteristics of being deep in contents and broad in scope. Therefore traditional computer-based information systems may not be useful. However, intelligent agents which can help EIS in data retrieving, filtering and presentation can provide a significant contribution. In addition, since the EIS information is broad in scope, and the supporting tasks for EIS are diversified in nature, more than one problem processing agents may be needed. Finally, the process described in Fig. 1 involves multiple tasks. The automation of these tasks (or some of them) can be done only if multiple expert systems are involved.

The theoretical background for employing a multiple intelligent information processing agents has been outlined by Simon who stated that “The capacity of the human mind for formulating and solving complex problems is very small compared with the size of the problems whose solution is required for objective rational behaviour in the real world – or even for a reasonable approximation to such objective rationality” (Simon 1957). The limitation of a human mind’s processing capacity was called by Simon “bounded rationality”. Fox (1981) postulated that “bounded rationality implies that both the information that one person can absorb and the detail of control he may yield is limited. As tasks grow larger and more complex, means must be found to effectively limit the increase of information a person sees and the complexity of control".

The inability of one intelligent agent to properly support the executive forces him (her) to conduct a tedious manual or at best semi-automatic drill down search and/or to receive a detailed DSS analysis from several experts. The distributed intelligent executive information system (DIEIS) framework proposed in this paper is designed to improve the situation.

## 3.3. Distributed intelligent executive information systems

Heterogeneous expertises support DIEIS to encompass a variety of problem domains, while distributed information processing allow the sharing of resources to improve the efficiency and effectiveness of the system. In distributed problem solving studies, intelligent agents can combine their resources so that the intelligence of the group is more than the sum of individual agents' intelligence (Durfee 1988). The coordination mechanism between agents is therefore a key issue in the success of DPS.

In the following sections, the architecture of distributed artificial intelligence is outlined and the relationship between distributed artificial intelligence and distributed intelligent executive information systems is discussed.

## 3.4. Distributed artificial intelligence (DAI)

Distributed problem solving appears in two forms (1) task-sharing and (2) result-sharing (Smith and Davis 1981). In task sharing systems, agents assist each other by sharing the computational load for the execution of subtasks of the overall problem, while in result sharing systems, agents assist each other by sharing partial results which are based on somewhat different perspectives on the overall problem. Both forms are briefly discussed next.

![](/api/attachments/N3BVJU8A/fulltext/images/3c0c9fcf0aec2ef12a985ba79281df4394ca80afa77b65a4e9ab1c2e18877a5e.jpg)  
Fig. 3. Framework of task-sharing systems.

## 3.4.1. Task-sharing systems

In task-sharing systems, the overall problem to be solved is decomposed into several smaller subproblems (see Fig. 3). Cooperation is achieved by sharing the computational (processing) load of the overall problem. Each subproblem is assigned to a particular agent that will asynchronously perform its own functions and submit a solution synchronously with other agents to an electronic coordinator. The contract-net protocol developed by Smith (1980) proposed a framework that is designed to allow agents to submit bids for tasks rather than get tasks at the discretion of the coordinator. Any agent that receives a task announcement message can reply with a bid, which is basically an indication on how the task is to be accomplished. The coordinator that announces the tasks, collects the bids and awards the task to the bidder with the highest bid (best fit). Other examples of task sharing systems are the office information system proposed by Woo and Lochovsky (1986), the scheduling system of Shaw and Whinston (1988, 1989), and the object-oriented multiple agent planning system of Kamel and Syed (1989).

Generally speaking, task-sharing based systems are most useful for problem domains in which it is appropriate to define a hierarchy of tasks or levels of data abstraction (Smith and Davis 1981). Such problems can usually be decomposed into a set of independent subproblems. Many problems tackled by executives are of this nature. For example, an evaluation of a proposed acquisition may require advice from legal, financial, technological and organizational experts. The expertise is provided to the acquisition decision maker(s) who incorporates the expertise when determining the fate of the acquisition.

## 3.4.2. Result-sharing systems

Result-sharing is a form of cooperation in which individual agents assist each other by sharing partial results, based on somewhat different perspectives of the overall problem (Smith and Davis 1981). In this type of system, control is typically “data-oriented.” At any point in time, the computation done by a certain agent is used to satisfy the information needs of a subtask done by another agent (see Fig. 4). Thus, an explicit hierarchy of task-subtask relationships does not have to exist between individual agents. Typically, one of the agents acts as the group planner (or the coordinator), and each of the other agents sends all pertinent information to this agent in order to form a global plan for problem solving. The main issue of such systems is how to guide and coordinate the interactions among the participating agents, so that the problem can be solved jointly by the group.

![](/api/attachments/N3BVJU8A/fulltext/images/04a7666421142c2c6e41a7f83ad26bad69ae984201333afd482ee440bce25efb.jpg)  
Fig. 4. Framework of result-sharing systems.

An example of result sharing in an EIS context is the process of environmental scanning where the collected data are forwarded to interpreters who transfer the interpreted information to the decision maker (e.g. see Wang and Turban (1993)). Another example is where the results of some forecasts are forwarded to an analyst for interpretation. In general, result-sharing DAI systems are most useful in problem domains in which (1) results achieved by one agent influence or constrain those that can be achieved by another agent (i.e., the results are significantly relevant to each other), (2) sharing of results drives the system to converge to a solution of the problem, and (3) sharing of results drives the system to a correct solution of the problem (Smith and Davis 1981). Such situations are typical in what is known as sequential decision making (Sprague and Carlson 1982). For example, a decision of how much to produce is interrelated with that of when to produce, which drives the machines and employees schedules, which drives cash flow and marketing plans.

To date, several result-sharing based DAI systems have been developed. One example is MACE (Multi-Agent Computing Environment) (Gasser et al. 1987), which is an instrumented testbed for building a wide range of experimental distributed artificial intelligence systems at different levels of granularity. The dominant metaphor of MACE is a collection of intelligent, semi-autonomous agents interacting in organized ways. The computational units (agents) run in parallel, and communicate via messages for problem solving. Mason et al. (1989) proposed a distributed assumption-based truth maintenance system (DATMS) which interprets data from a seismic sensor network for nuclear test ban treaty verification. Each agent interprets data from a sensor site or geological region and relies on its communications lines to guide its search for an interpretation of its own data. DATMS is implemented under MATE (Multi-Agent Test Environment) using C and Common Lisp. Nii et al. (1989) incorporated two concurrent systems, Cage (Aiello 1986) and Poligon (Rice 1986), to solve problems based on the blackboard architecture. Both Cage and Poligon are designed to exploit multiprocessor hardware with the intent of achieving computational speedup. Shaw and Fox (1991) proposed a networked expert system testbed (NEST) which consists of a network of four expert systems. The architecture of NEST is based on a variation of the blackboard architecture, with “mailbox” areas added to the blackboard shared area for coordinating the agents. With three functional expert systems (marketing, production, and purchasing), and another expert system serving as the coordinator, NEST proposes a solution to determine the quantity of a new product that is about to be sent to the market.

## 3.4.3. Comparison for task-sharing and result-sharing systems

Task-sharing is used to organize problem decomposition through the relationship of task-subtask connections between nodes. The result, which is typically a hierarchy, is used to structure answer synthesis. One important assumption made by task-sharing systems is that subtasks can be accomplished by agents working independently. This allows the improvements of problem solving efficiency by reducing internode communication. Result-sharing is used to facilitate problems which can not be solved by individual agents working independently without significant communication with other agents (Smith and Davis 1981). Result-sharing systems do not have the capability of problem decomposition, therefore, problem decomposition and distribution of subproblems to individual agents are handled by an agent outside of these systems.

## 3.5. Coordination mechanisms for distributed problem solving

Coordination is the key factor to the success of any distributed problem solving. The purpose of the coordination mechanism is to manage problem solving so that cooperating agents work together as a coherent team (Durfee 1988). The coordination is achieved by exchanging data, partial solution plans, and constraints among agents. Several research projects have emerged in the area of designing coordination mechanisms for solution plan processes in a multi-agent environment. Shaw and Fox (1991) classified coordination mechanisms into seven categories. Four of them can be used in a DIEIS (see Table 2).

Table 2  
Coordination mechanisms of distributed problem solving

<table><tr><td>Coordination method</td><td>Features</td><td>References</td></tr><tr><td>Coordination by revising actions</td><td>Conflicts avoidance</td><td>Cammarata et al. (1983)</td></tr><tr><td>Coordination by synchronization</td><td>Timing control, interaction regulation</td><td>Corkill (1977), Georgeff (1983)</td></tr><tr><td>Coordination by structured</td><td rowspan="2">Delphi technique, Nominal group technique</td><td rowspan="2">Nunamaker et al. (1988)</td></tr><tr><td>Group mediation</td></tr><tr><td>Coordination by opportunistic goal satisfaction</td><td>Blackboard model, Information sharing</td><td>Nii et al. (1989), Shaw et al. (1990, 1991)</td></tr></table>

## 4. A conceptual model for distributed intelligent executive information systems

The purpose of the proposed DIEIS is to electronically support the activities of executives. The structure, operation and information flow is described next.

## 4.1. The framework of distributed intelligent executive information systems

In the DIEIS framework (see Fig. 5), a decentralized group of agents cooperatively attempt to provide a solution to a complex problem through a coordinator. Since the problem is complex, it is being decomposed to subproblems. Information of decomposed subproblems and partial solutions is shared among agents. Each agent works independently, and may even be at a different geographical location, and is supported by a specific knowledge base. In general, a DIEIS contains seven independent but closely related subsystems:

(a) Knowledge Processing agents.

(b) Knowledge Bases (a case base, a rule base and a database).

(c) Knowledge Creating/Collecting Agents.

(d) User Interface.

(e) Multimedia agent.

(f) The Environment.

(g) Coordinator.

Any EIS is heavily based on data available in both internal and external databases. Fast accessibility to the data is critical. Once located, data need to be processed (e.g. interpreted). The automation of this process is achieved by using the knowledge processing agents. Knowledge process-

![](/api/attachments/N3BVJU8A/fulltext/images/2027e7f9b1c99aee3f27550bbd9270be659fcb00c0dce45be65c9f8c0d92e4e0.jpg)  
Fig. 5. The conceptual framework of DIEIS.

![](/api/attachments/N3BVJU8A/fulltext/images/871d99d185dacb493c5568777fe67bf355da3253d2c38dfa6e079b3b55c6e3a8.jpg)  
Shaded areas indicate that concurrent processing is possible  
Fig. 6. Knowledge processing and creation in DIEIS.

ing agents (left side of Fig. 5) consist of DBMS, inductive and deductive reasoning agents, and computational agents. Their responsibilities are to retrieve and organize data from the knowledge and databases and refine them. The refined data is then sent to the presentation mechanism for executives. The inductive reasoning can be a case-based reasoning agent (Slade 1991; Sombe 1990; Vosniadou and Ortony 1989; Owen 1990; Riesbeck and Schank 1989) which uses past experiences for current problem solving, especially when the problem domain is poorly understood, or the domain theory is too weak to be acquired from the experts. (Chi et al. 1993). Another technology that can be used as an inductive mechanism is neural computing. The deductive reasoning agents are rule-based mechanisms or expert systems. New solution is deduced from previously stored knowledge rules.

The user interface is part of the dialogue system in a basic decision support framework. The user interface usually provides EIS with strong graphical capability so that executives' inquiries can be collected effectively and organized information can be presented in a more comprehensive format. The user interface is divided into two submechanisms based on the functionalities: (1) action (input) mechanism and (2) presentation (output) mechanism. In addition, raw information from different information processing agents can be refined and organized graphically since information may be collected from various sources by the coordinator and sent to the user interface. Furthermore, the user interface can be adjusted based on different executives' requirements. This subsystem can have its own intelligent agent who will determine, for example, the media to be used in specific presentation (Sipior and Garrity 1992). Generally speaking, user functions in EIS interface are designed in modules. Typical modules are:

(1) Status report (with possibility of drill down and exception reporting): textual explanation and trend graph.

(2) Reminder: notes, calendar, tracking information about messages.

(3) Investigation: comparisons, calculations, drill down, personalized analysis, graphics.

(4) Electronic mail: alerts if mail is pending, monitoring mail, can transmit any screen of other modules.

(5) New service: both external and internal with capability to drill down for details. Hypertext capabilities are available.

(6) Detailed analysis: in this case, monitored results are going through a quantitative analysis. This is typically done in executive support systems (ESS).

Executives utilize the modules to issue inquiries. To answer these inquiries a DBMS may be activated, or multiple intelligent agents can be triggered for a more complex problem solving. For example, An “Investigation” query may involve using several DBMS agents to retrieve data from the different databases and employing a spreadsheet agent for calculation; the results will then be sent to a rule based agent for interpretation.

If no existing knowledge is available to answer a inquiry, knowledge creating/collecting agents are triggered (right-hand side of Fig. 5). These agents can be of three types: inductive/deductive learning agents, environment scanning agents, and E-mail agents. The inductive (Michalski and Stepp 1983) and deductive learning agents (Mitchell et al. 1986) are used when new knowledge is needed or existing knowledge needs to be modified. Induction learning agent infers the description of a class from descriptions of individual objects of that class. Training examples are given as cases and described by a vector of attribute values. A general concept description is induced by inspecting specific instances of the concept. Since the concept description is generated by inspecting similarities among examples, it is a form of learning by examples. To arrive at a correct concept description in accordance with training examples, a hypothesis concept description is chosen to cover positive examples and exclude negative ones. As the process continues, new examples are fed in and the learner updates the hypothesis to keep it consistent with new examples, until all training examples are consistent with the learned concept description. Similarity-based learning systems have been widely used to acquire knowledge for reasoning systems which perform classification tasks (Winston 1975; Michalski and Stepp 1983).

The deductive learning agent uses existing knowledge to explain and generalize a single example and thereby acquires an operational concept description and problem-solving knowledge (DeJong and Mooney 1986; Mitchell et al. 1986). An explanation based learning (EBL) program takes a single positive instance as the training example, explains this example by an existing knowledge base (or the domain theory), and produces a generalized concept description as the final output. This class of learning method allows generalized concepts to be determined by only one instance, in contrast to multiple instances needed for the deductive learning agent. The deductive learning agents' construction and analysis of explanations require extremely detailed knowledge of the problem domain. The environment scanning agents collect available data from the environment for the knowledge base and other learning agents. The E-mail agents receive data or information from outside sources such as other decision support systems or outside database intelligent agents.

Both the internal and external environments provide the learning mechanism with data resources so that useful information (usually regularities and commonalities) is retrieved. The environment also provides the knowledge retrieving mechanism with raw data to be organized into the databases.

The coordinator, the heart of a DIEIS, regulates the internal actions among individual agents. All the communication activities among agents is transferred through the coordinator. The meta knowledge of the coordinator is stored in the index which regulates the way agents communicate, problem decomposition, sub-problem assignments, and proposal evaluation.

## 4.2. Information flow and knowledge processing in dieis

Information processing in DIEIS is classified into two categories: (1) knowledge processing and (2) knowledge creating/collecting. Knowledge processing utilizes existing knowledge processing agents (e.g., DBMS, Inductive reasoning agent, Deductive reasoning agents...) to “reason, retrieve and filter” existing knowledge. A query such as “get the value of total-sales in region “A” during 1991”, may require a DBMS accessing an existing database of annual sales account. The agent maybe a combination of a natural language processor and a DBMS so that the query can be asked in a plain English. If existing knowledge does not contain the needed information, the coordinator will trigger the knowledge creating/collecting agents for knowledge collection form the environment. For example, if the rule “to select good stocks” can not be retrieved from any rule-based agents based on existing knowledge bases, the learning agent will be used to implement a similarity-based learning process with the help of existing databases where historical stock information is stored. Fig. 6 summarizes the knowledge processing flow in DIEIS. A query is received by the “action mechanism” of the user interface. The query is passed on to the coordinator who checks the index to find if there is existing knowledge in the knowledge base. If there is knowledge available to solve this query, the necessary knowledge processing agent(s) will be located and information processing is triggered. If the current problem is solved, the coordinator checks to see whether any subproblems have emerged. That is, the current problem is decomposed into subproblems. For each subproblem, another iteration will be triggered and concurrent information processing is possible. However, if there is no existing knowledge available, knowledge creating/collecting agents will be employed to create/learn new concepts/knowledge from the environment. New learned concepts/knowledge is then stored in the knowledge base for further processing. In the meantime, the index is also updated.

If the current problem is not solved, the coordinator checks the availability of additional processing agents (based on the index). If such agents exist, they are assigned the processing tasks. If such agents are not available, the coordinator is looking for knowledge creation agents who are assigned knowledge creation tasks. The new knowledge is added to the knowledge base and the coordinator attempts to resolve the problem.

## 5. Conclusion and suggested research

In this paper we propose an EIS framework with intelligent distributed information processing agents. The multiple intelligent agents enable the processing of more complicated information by the cooperative efforts of various agents. In fact, many executive tasks contain various aspects of problem domains which can not be supported by a single data retrieving and processing mechanism. In other words, current EIS retrieve data directly from the database and present it with no automated data processing. By employing the proposed framework, a more intelligent EIS can be constructed by having a set of agents working cooperatively.

Multiple intelligent agents can support some of the most difficult issues in EIS/ESS implementation. They are:

(1) Finding the executive information requirements (e.g., see Wetherbe (1991) and Watson and Frolick (1992)).

(2) Managing the development process of EIS (e.g., see Watson et al. (1991)).

(3) Improve environmental scanning and interpretation (e.g., see Preedy (1990); Wang and Turban (1993); Watson et al. (1992)).

(4) Justification of EIS and especially DIEIS (e.g., see Barkan (1991); Watson et al. (1992)).

(5) Integration of EIS with other computer-based information systems.

In order to commercially implement a DIEIS, it is necessary to conduct further research. The generic EIS research directions proposed by Watson et al. (1992) can be extended by the following DIEIS topics:

(1) DIEIS architecture; especially its relationship to a blackboard structure.

(2) Learning mechanisms for DIEIS.

(3) Which agents will participate in the DIEIS and which role each of them is going to play (for different possible scenarios).

(4) The economics of DIEIS; i.e., when would it be economically feasible to use a DIEIS.

(5) The development methodology; How DIEIS is going to be developed? Would it be possible to use existing tools?

(6) The nature of the interface between the DIEIS and other CBIS (especially DSS and intelligent DSS.)

The investigation of these and related research issues could provide the insights needed for the creation of powerful DIEIS which would support large number of executives in their complex job.

## References

Barkan, Wayne C. (1991), Executive Information Systems, New York, Van Nosttand Reinholl.

Cammarata, S., D. McArthur and R. Steeb (1983), “Strategies of Cooperation in Distributed Problem Solving”, Proceedings of the 8th International Joint Conference of Artificial Intelligence, pp. 767–770.

Chi, T.H. Robert, Minder Chen and Melody Y. Kiang (1993), A Generalized Case Based Reasoning System for Portfolio Management, Expert Systems with Applications, Vol. 6, pp. 67–76.

Croft, W.B. and Lefkowitz (1988), Knowledge-based Support of Cooperative Activities, Proceedings of the 21st Annual Hawaii International Conference on System Science, Vol. III, pp. 312–318.

Decker, K.S. (1987), Distributed Problem Solving: A Survey, IEEE Transactions on Systems, Man, and Cybernetics, Vol. 17, No. 5, September.

DeJong, G.F. and R.J. Mooney (1986), Explanation-Based Learning: An Alternative View, Machine Learning 1, 2, pp. 145–176.

Durfee, E.H. (1988), Coordination of Distributed Problem Solvers, Kluwer Academic Publishers, Boston, MA.

Elofson, G. and B.R. Konsynski (1992), Delegation Technologies for Environmental Scanning, Journal of MIS, Spring.

Fox, Mark (1981), An Organizational View of Distributed Systems, IEEE Transactions on Systems, Man, and Cybernetics, Vol. 11, No. 1, January.

Gasser, Les, Carl Braganza, and Nava Herman (1987), MACE: A Flexible Testbed for Distributed AI Research, in Distributed Artificial Intelligence, Michael N. Huhns (Ed.), Morgan Kaufmann, Los Altos, CA.

Georgeff, M. (1983), Communication and Interaction in Multi-agent Planning, Proceedings AAAI-1983.

Huhns, Michael N. (1987), Distributed Artificial Intelligence, Vol. 1, Morgan Kaufmann Publisher, Inc., Los Altos, CA.

Jessop, L.M. and J.S. Valacich (1992), Group Support Systems, Macmillan, New York.

Kamel, M. and A. Syed (1989), An Object-Oriented Multiple Agent Planning System, in Distributed Artificial Intelligence, Vol. II, Les Gasser and Michael N. Huhns (Eds.), Morgan Kaufmann, San Mateo, CA.

Mason, Cindy L. and Rowland R. Johnson (1989), DATMS: A Framework for Distributed Assumption Based Reasoning, in Distributed Artificial Intelligence, Vol. 2, Morgan Kaufmann Publishers, edited by Les Gasser and Michael N. Huhns.

Mitchell, Tom M., Richard M. Keller and Smadar T. Kedar-Cabelli (1986), Explanation-Based Generalization - A Unifying View, Machine Learning 1, 1 (January). 47–80.

Nunamaker, J.F., L.M. Applegate and B.R. Konsynski (1988), Computer-aided Deliberation: Model Management and Group Decision Support, Operation Research, vol. 36, no. 6, pp. 826–847.

Newell, A and Herbert Simon (1972), Human Problem Solving, Englewood, N.J.: Prentice-Hall.

Nii, H.P., Aiello, N., and Rice, J. (1989), Experiments on Cage and Poligon: Measuring the Performance of Parallel Blackboard Systems, Distributed Artificial Intelligence, vol. II., L Gasser and M. Huhns (Eds.), Pitman, London, pp. 319–384.

Owen, S (1990), Analog for Automated Reasoning, New York, Academic Press.

Preedy, D (1990), The Theory and Practical Use of Executive Information Systems, International Journal of Information Management, 10 (96–104).

Riesbeck, Christopher K. and Roger C. Schank (1989), Inside Case-based Reasoning, Lawrence Relbaum Associates, Hillsdale, New Jersey.

Rice, James (1986), Poligon: A System for Parallel Problem Solving, Technical Report KSL-86-19, Knowledge Systems Laboratory, Computer Science Department, Stanford University, April.

Rockart, F. John and David W. Delong (1988), Executive Support Systems, The Emergence of Top Management Computer Use, Dow Jones-Irwin, Homewood, Illinois.

Sathi, A. and M. Fox (1989), Constraint-Directed Negotiation of Resources Reallocations, Distributed Artificial Intelligence, Vol. II, L. Gasser and M. Huhns (Eds.), Pitman, London, pp. 163 - 194.

Shaw M. and M. Fox (1991), Distributed Artificial Intelligence for Group Decision Support: Integration of Problem Solving, Coordination, and Learning, Working paper.

Shaw, M., B. Harrow and S. Herman (1990), NEST: A Networked Expert Systems Testbed for Cooperative Problem Solving and Group Learning, the Proceedings of the Working Conference on Cooperating Knowledge Based Systems, University of Keele, Keele, UK.

Shaw, M., B. Harrow and S. Herman (1991), Distributed Artificial Intelligence for Multi-agent Problem Solving and Group Learning, the Proceedings of Hawaii International Conference of Systems Science, IEEE Press.

Shaw, M. and A.B. Whinston (1988), A Distributed Knowledge-based Approach to Flexible Automation: The Contract-net Framework, International Journal of Flexible Manufacturing Systems, pp. 85–104.

Shaw, M. and A.B. Whinston (1989), Learning and Adaptation in Distributed Artificial Intelligence Systems, Distributed Artificial Intelligence, Vol. II, L. Gasser and M. Huhns (Eds), Pitman, London, pp. 413–430.

Silver, Bernard, William Frawley, Glenn Iba, John Vittal and Kelly Bradford (1990), ILS: A Framework for Multi-Paradigmatic Learning, Proceedings of the 7th International Conference on Machine Learning, Austin TX.

Simon, H.A. (1957), Models of Man, New York: Wiley.

Sipior, J.C. and E.J. Garrity (1992), Merging Expert Systems with Multimedia Technology, Database, Winter.

Slade, S. (1991), Case-based Reasoning: A Research Paradigm, AI Magazine, Spring.

Smith, R.G. and R. Davis (1981), Frameworks for Cooperation in Distributed Problem Solving, IEEE Transactions on Systems Man and Cybernetics, Vol. 11, No. 1.

Smith, R. (1980), The Contract-net Protocol: High-level Communication and Control in a Distributed Problem Solver, IEEE Transactions on Computers, Vol. 29, pp. 1104–1113, Dec.

Sombe, L. (1990), Reasoning Under Incomplete Information in Artificial Intelligence, New York, John Wiley and Sons.

Sprague, R.H. and E.D. Carlson (1982), Building Effective Decision Support Systems, Prentice-Hall, Englewood cliff, N.J.

Turban, E., Decision Support and Expert Systems, 3rd ed., Macmillan Pub. Co., New York.

Turban, E., and Watson H.J., Integrating Expert Systems, Executive Information Systems and Decision Support Systems, DSS-89 Transactions, George R. Widmeyer (Ed). The Institute of Management Science.

Vosniadou, S. and A Ortony (1989), Similarity and Analogical Reasoning, Cambridge, Mass, Cambridge Press.

Wang P., and E. Turban (1993), Executive Support Systems in Strategic Environmental Information Processing, Behaviour and Information Technology, January.

Watson, H.J., et al. (1991), Executive Information Systems: A Framework for Development and a Survey of Current Practices, MIS Quarterly, March.

Watson, H.J., et al. (1992), Executive Information Systems, Wiley, New York, 1992.

Watson, H.J., and M. Frolick (1992), Determining Information Requirements for an Executive Information System, Information Systems Management, Spring.

Watson, H.J., and R.K. Rainer (1991), Managers Guide to Executive Support Systems, Business Horizons, March-April.

Watson, Hugh J., R.K. Rainer, and C. Koh (1991), Executive Information Systems: A Framework for Development and a Survey of Current Practices, Management Science, March.

Wetherbe, J.C. (1991), Executive Information Requirements: Getting it right, MIS Quarterly, March.

Winston, P.H. (1975), Learning Structural Description from Examples. Psychology of Computer Vision, (Winston, P.H. Ed.), (McGraw Hill, New York).

Woo, C. and F. Lochovsky (1986), Supporting Distributed Office Problem Solving in Organizations, ACM Transactions on Office Information Systems, July, pp. 185–204.

![](/api/attachments/N3BVJU8A/fulltext/images/da11e2a2ee3336a884d0f786742d6d35750bcc8d7091f9e195a6b0da38b885d5.jpg)

Robert T. Chi is Assistant Professor of Information Systems at California State University at Long Beach. He received his M.S. from University of Wisconsin-Madison, and Ph.D. in Management Science and Information Systems from University of Texas at Austin. His research interests include AI application in management and finance, distributed AI, decision support systems and executive information systems. Dr. Chi has pub-

![](/api/attachments/N3BVJU8A/fulltext/images/1ebe679de3484bfcb770ef4357854ee9e08ff1f984cf12c7464295dce9aec24a.jpg)

Efraim Turban (MBA, Ph.D., University of California at Berkeley) is professor of Information Systems at California State University, Long Beach. Prior to joining CSULB, Dr. Turban was a distinguished professor at Eastern Illinois University. Dr. Turban also taught at UCLA, USC, Florida International University and Lehigh University. Of his many books, the most known are DSS and Expert Systems (MACMILLAN) and Funda-

lished in Journal of Management Information Systems, Journal of Expert Systems with Applications, The Journal of Operational Research Society, Annuals of Operational Research, International Journal of Intelligent Systems, Journal of Knowledge Based Systems, and other professional journals. He is a member of TIMS and DSI.

mentals of Management Science (R.D. IRWIN). His latest book, is Applied Artificial Intelligence and Expert Systems. (MACMILLAN). Dr. Turban authored about 75 papers in journals such as Management Science, Operations Research, MIS Quarterly, Journal of Operations Management, Computers and Operations Research, and The Journal of MIS. Dr. Turban was worked several years in industry (General Electric) and he provided-consulting services to many corporations and governments. His research interests are in the applications of emerging technologies to Management Support Systems. His current work is in the areas of expert systems and multimedia, neural computing and expert systems and executive information systems.
