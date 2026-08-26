---
otero_id: 23550
otero_key: "M68CT33S"
title: "Coordination of joint tasks in organizational processes"
authors: "Gregory N Mentzas"
year: "1993"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1993.20"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Coordination of joint tasks in organizational processes

GREGORY N. MENTZAS

Department of Electrical and Computer Engineering, National Technical University of Athens, Greece

Organizational productivity can be maximized by creating, using and maintaining structural and dynamic configurations of multi-participant interaction. The paper highlights a number of areas for consideration that arise when studying coordination within an organizational setting. The focus of the analysis is on two types of tasks: decision-making tasks and routine office processes. The paper argues that a number of (conflicting) options exist when developing the coordination aspects of group systems; they are classified across the following axes: specification and implementation of coordination; use of synchronous and asynchronous working phases; information exchange and information sharing; support of sequential and concurrent processing; support of negotiation and conflict resolution; support of analytical modelling; and description of the organizational environment.

## Introduction

The maximization of organizational productivity by creating, using and maintaining structural and dynamic configurations of multi-participant interaction is of paramount importance in today's organizational forms; see Applegate et al. (1991). The technology provided for supporting joint organizational tasks comprises a large variety of systems with different goals such as electronic meeting support systems, multi-user authoring systems, group decision support systems, negotiation support systems, mediator systems, etc (see e.g. Johansen, 1988; Greif, 1988). The focus of research in Computer-Supported Cooperative Work (CSCW) is not on supporting the individual but on supporting the coordination and cooperation of multiple interactive participants who form a group.

In a recent survey of the perceptions of researchers, developers and end-users in the CSCW field, the need for tools that support group coordination ranked high scores in the analysis of the potential impacts that CSCW technologies might have in the future (see Butterfield et al., 1992). A result in the same survey, however, was that the current availability of group coordination support is low in comparison to other CSCW technologies, thus leading to the conclusion that coordination technology belongs to the least developed ones.

The goal of the present paper is to highlight a number of areas for consideration that arise when studying the coordination issues of joint work within an organizational setting. The focus of the analysis is on two types of tasks; decision-making tasks and routine office processes.

Research on the support of multi-participant decision-making has been classified by DeSanctis and Gallupe (1987), in a widely accepted scheme, which distinguishes between three levels, based on the degree of support provided to the group. Level 1 systems provide technical functionality aimed at removing common communication barriers and facilitating information exchange; level 2 systems provide decision modelling and group decision process facilitation tools aimed at decreasing uncertainty and ambiguity; finally, level 3 systems provide normative, prescriptive intervention in group processes through structured group process tools, active filtering and structuring of information or communication, and expert systems that perform group roles and functions or advise group leaders/members when appropriate rules are not followed. As is obvious, all three levels, and most notably level 2, place emphasis on issues of coordination.

Office processes, on the other hand, capture the dynamic structure of the office part in an organizational setting. They can be considered as a set of mappings among common office objects (i.e. documents, folders, etc). Office processes are routine sequences of operations that model the event-driven behaviour of office work. They are triggered upon completion of some awaited event: the arrival of a message, the completion of a form, or the modification of a document (see Zisman, 1977; Lochovsky et al., 1988). Office models should encapsulate human cooperation, as well as provide rigorous formalisms for coordination (see Tueni et al., 1991).

In the present paper an analysis of coordination issues is given, within the context of decision-making and office domain tasks. The paper argues that a number of (conflicting) options exist when designing the coordination aspects of group systems. They are classified across the following axes: specification (i.e. activity description languages and concepts) and implementation of coordination; use of synchronous and asynchronous working phases; information exchange and information sharing; support of sequential and concurrent processing; support of negotiation and conflict resolution; support of analytical modelling; and description of the organizational environment. In examining these issues, the paper reviews some sample applications from the office information systems and the group decision support systems worlds.

The paper is organized in the following manner. Section 2 gives a short overview of research in cooperative work from the group decision support and office information systems perspectives, while section 3 presents issues related to coordination. Section 4 reviews the coordination facilities included in OIS and GDSS systems and proceeds with an analysis of the problems and options available in the development of computer-supported coordination. Finally section 5 presents the conclusions and indicates future research directions.

## Cooperative work in decision and office processes

According to Johansen (1988) and Ellis et al. (1991) two taxonomies of groupware systems are useful: the first is based upon notions of time and space and the second on application-level functionality.

The first taxonomy can be summarized in the groupware time space matrix; see Table 1. Time is affected by the synchronous, or not, mode of cooperation between agents and such system attributes as information storage and retrieval. Space, on the other hand, affects cooperation in more than one dimension; cooperating agents who are not in the same space have limited information exchange; this limitation results from all the senses not being used for communication. Such a limitation may either be a help, by focusing attention, or a hinderance by obstructing the exchange of essential information (see also Hatcher, 1992). This spatial and time classification raises the issues of synchronous and asynchronous interaction, as well as the subject of distributed or non-distributed operation. Note, however, that this taxonomy has been recently partly overturned by Johansen (1991), who added a fifth category: any place/any time. Although the synchronous/asynchronous mode may be of crucial interest to the designers of CSCW systems, the new category is of paramount importance to the users of such systems; the latter would like to be provided with adequate computer support independently of limitations posed in the time or space dimensions.

Table 1 Groupware time space matrix

<table><tr><td></td><td>Same time</td><td>Different times</td></tr><tr><td>Same place</td><td>Face-to-face interaction</td><td>Asynchronous interaction</td></tr><tr><td>Different places</td><td>Synchronous distributed interaction</td><td>Asynchronous distributed interaction</td></tr></table>

Source: Ellis et al., 1991

The second taxonomy is application oriented and considers categories ranging from message systems, which support the asynchronous exchange of textual messages, multiuser editors, which permit the joint composition and editing of a document, group decision support systems, computer conferencing, etc.

In the following we limit the scope of the analysis to group decision support systems and office information systems, since these two approaches cover the majority of work done within an organizational setting (see also Applegate et al., 1991).

## Group decision support

It has been argued that group activities are economically necessary, efficient as means of production and reinforcing of democratic values (see Kraemer and King, 1988; Hatcher, 1992). DeSanctis and Gallupe (1987) provide the definition of a GDSS as 'an interactive computer-based system that facilitates the solution of unstructured problems by a set of decision-makers working together as a group'. Operationally this means increasing the speed at which decisions are reached without reducing, and hopefully enhancing, the quality of resulting decisions; Shaw (1981), for example, concluded that groups produce more and better solutions to problems than do individuals, particularly on judgemental tasks.

The primary problems of productivity loss in group decision meetings are from information loss, information distortion, or suboptimal decision making (i.e. not enough issues and alternatives are explored) (see Kraemer and King, 1988). These authors conceive the GDSS as a sociotechnical 'package' comprised of the following.

\- Hardware. This includes the conference facilities and the computing, telecommunications and audiovisual equipment.

\- Software. This includes database management systems, high level programming languages, and decision modelling and support software. Decision modelling includes software specifically tailored for group analysis and decision support includes modelling languages, decision structuring techniques (such as brainstorming, Delphi technique, etc.), utility and probability assessment techniques, multiattribute analysis, etc.

\- Organizationsware. This includes the organizational data, group processes and management procedures for collaborative group work.

\- People. This refers to the participants in the group and the support staff.

Table 2 Classification of the technology basis of GDSS

<table><tr><td>Technology</td><td>Description</td></tr><tr><td>Electronic boardroom</td><td>Computer and audiovisuals</td></tr><tr><td>Teleconference facility</td><td>Computer and communications</td></tr><tr><td>Group network</td><td>Computer network and interactive conferencing</td></tr><tr><td>Information centre</td><td>Computer, databases and retrieval tools</td></tr><tr><td>Decision conference</td><td>Computer and decision models</td></tr><tr><td>Collaboration facility</td><td>Computer and collaboration tools</td></tr></table>

Source: Kraemer and King, 1988.

The classification of the technology basis for GDSS proposed by Kraemer and King (1988) distinguishes between six ‘technological systems’; see also Table 2. According to this classification the electronic boardroom is the most elementary support system and differs little from its nonelectronic parent except that the audiovisual technology is computer-based. The teleconference facility is a system designed primarily to facilitate meetings between groups at two or more locations, while the group network has its roots in computer conferencing, but is asynchronous, which means that ‘meetings’ take place over an extended time period. The collaboration laboratory is focused on computer support for face-to-face group work, as well as on writing and argumentation, and involves verbal models and qualitative techniques through the manipulation of text-oriented data and graphical images. The two remaining systems, information centres and decision conferences, are of primary importance for the present analysis, since they require enhanced coordination support.

The information centre is defined as that portion of the data processing resources of an organization which is organized and dedicated to support the users of computer-based information systems in activities such as report generation and modification, data manipulation and analysis and spontaneous inquiries. The type of work intended to be supported through the information centre refers mainly to the short job, the one-time query and the simple report required within the project-oriented development environment needed by managers and professional users of information systems. The software of the information centre includes database management, statistical packages, graphics, text-processing etc., while the organizationsware includes meeting protocols, standard meetings, corporate databases, etc.

The decision conference facility is explicitly focusing on improving decision making by groups and emphasizing the use of structured decision processes, mainly involving computer models. In this case the decision analysis and modelling software is of crucial importance. Some examples of software used include: decision trees, multiattribute utility models, cost-benefit models, etc. A noteworthy part of the decision conference refers to the organizationsware; in the majority of cases, the meeting protocols are based on ‘democratic’ rather than ‘authoritarian’ or hierarchical ones, since decision conferences usually involve ‘equals’ (e.g. scientists, managers at the same organizational level, etc).

There are two main research streams in GDSS efforts. The first has concentrated on discovering the psychological or cognitive processes of individuals and groups involved in reaching conclusions and on the sociology of small-group interactions. The other major stream, which is of particular importance for our case, has been the development of technologically supported means of collecting, managing, displaying and coordinating information that might be useful in decision situations (see Vogel and Nunamaker, 1988).

## Collaborative office processes

The present section focuses on office processes, i.e. routine sequences of operations that are used to manipulate office objects. The event-driven behaviour of office work, as well as the ability to use graphical representations of office processes, has inspired research work that draws from the theory of graphs, Petri nets and finite automata; for surveys of office models and methods see Mentzas (1991) and Ang (1993).

We can define the concept of an office process (or procedure) as any reasonably long-lived information handling process in the office with a specific goal. Such processes may be carried out regularly and frequently, or at long indeterminate intervals. We can view office processes as being composed of a series of office activities, which are relatively non-decomposable units of office work; the latter when carried out in an appropriate sequence achieve the overall target of the procedure.

Consider an order entry process. Once a customer request arrives it is recorded in a logbook and an order form is typed. An administrator processes the customer file and uses information from the billing file to validate the fact that this customer is not delinquent in previous payment. Then a decision is made whether the ordered goods will be shipped together with an appropriate form or whether the customer will be billed for later payment. This fragment of office work, although simplified, can serve as an expository aid for the analysis of office processes.

The following can be considered general characteristics of office processes. First, they are typically triggered upon completion of some awaited event: the arrival of a message, the completion of a form, the modification of a document, etc. In the above example the arrival of a customer request serves as the start-up event of the procedure. Second, they make use of information repositories (e.g. the customer and billing files) and office objects (e.g. the log-book and the order form). Third, they can be decomposed into elementary office activities, whose temporal ordering define office processes in a unique manner. Finally, complex synchronization of activities may be included; it may take the form of pre- and post-conditions. Two types of pre-conditions can be considered: an activity is required to wait for the completion of more than one preceding activities, or it may be activated upon the completion of either of the preceding activities. In addition, two types of post-conditions can be examined: multiple activities may be triggered in conjunction, or decisions may be required for the mutual exclusion of activities.

Coordination of office processes is necessary, in order to guarantee efficiency and consistency of office work. Consider the above example of the order entry. One can identify the work of various 'roles' and the need for their coordination. Once the administrator retrieves information for the customer from the billing file, he/she may require additional details from the financial department. In order to proceed with the shipping of ordered goods, a coordination between the financial and stock departments is necessary; the subsequent billing of the customer should be a coordinated process between the office worker responsible for the company logistics and the administrator that accepted the order, etc. Hence, the office model needs to represent coordination, so that it covers what Auramaki et al. (1988) call the 'social features of offices'.

## Analysis of coordination issues

The execution of coordinated activities can be examined independently from the initial motivation for cooperation. In order to cooperate smoothly, a certain predictability of the other participants' behaviour is necessary. The presence of such a predictability and its use in communication and operation can be considered equivalent to coordination.

A generally accepted definition of coordination does not exist in the literature. The coordination problem as defined by Singh (1989) refers to the ‘integration and harmonious adjustment of individual work efforts toward the accomplishment of a larger goal’. Holt (1988) gives a rather poetic view by comparing coordination with a ‘dynamic glue that binds tasks together into larger, meaningful wholes’.

Malone and Crowston (1990), follow a more formal approach. They distinguish four components of coordination: goals, activities, actors and interdependencies. Goals are the motivations and purposes of an activity; the latter is performed by an (human or machine) actor (single or team of agents). A workgroup is a set of actors. In order to take advantage of the multiplicity of actors in a workgroup, each activity may be broken into sub-activities; the need for coordination arises because of interdependencies between these sub-activities. These interdependencies can either be of a generic kind or of a domain-specific kind. The former could be of various types. Some examples are:

Prerequisite. E.g. the output or effect of one activity is required by another activity. Coordination can be achieved by ordering the execution of these activities. Shared resource. I.e. two or more activities share the same resource. Coordination happens through the allocation of the available resources to activities. Simultaneity. Simultaneous performance of multiple activities. In this case coordination can be achieved via synchronization.

Examples of domain-specific interdependencies include the design process in manufacturing, the relations of different divisions of a company to its customers, etc.

Using the above analysis, Malone and Croston (1990) deduce their definition of coordination as 'the act of managing interdependencies between activities performed to achieve a goal'.

The usual tasks accomplished by coordination systems include the ability of users to view their actions, as well as the relevant actions of others, within the context of an overall goal. These systems may trigger users' actions by informing them of the states of their actions and their wait conditions, or by generating reminders and alerts.

In the following we examine five topics related to coordination: coordination protocols; the existing coordination models; the issue of the timespan of coordination; synchronous versus asynchronous modes of operation; and the approaches of information sharing or information exchange.

## Coordination protocols

Protocols are mutually agreed upon ways of interacting; these protocols may be built into the hardware and software, called ‘technological’ protocols, or left to the control of the participants, called ‘social’ protocols.

Examples of technological protocols are the floor-control mechanisms in several computer conferencing systems. These systems can only process one user's input requests at a time, imposing on participants a group process of turn-taking. Social protocols can either be formal rules or policies, or informal practices, such as hand-raising.

Each approach has advantages and disadvantages. Leaving the processes to social protocols encourages collaboration, but may result in unfair, distracting or inefficient processes. On the other hand, embedding a group process as a technological protocol ensures that the process is followed, provides structure to the group's tasks and assists less experienced users. However, technological protocols may be overly restrictive and may constrain the group's working style. Note that the systems reviewed in the next section emphasize the role of technological protocols.

## Control models of coordination

Coordination systems have been classified by Ellis et al. (1991) by one of the four types of control models they embrace: form, procedure, conversation, or communication-structure oriented.

Form-oriented models typically focus on the routing of documents (forms) in organizational procedures. These systems address coordination by explicitly modelling organizational activity as fixed processes (see the OTM system by Lochovsky et al. 1988; and the work of Zisman, 1977). Recent systems, however, tend to make process support more flexible; for example exception handling can be addressed through migration specifications that describe all the possible task migration routes in terms of the steps to be carried out in processing organizational documents.

Procedure-oriented models view organizational procedures as programmable processes (see Balzer, 1989). This approach was first applied to coordination problems in the software process domains and takes the view that software process descriptions should be thought of and implemented as software. The development of process programs is itself a rigorous process consisting of specification, design, implementation and testing/verification phases.

Conversation-oriented models are based on the observation that people coordinate their activities via their conversation. The underlying theoretical basis for such systems is speech act theory (see Searle, 1969). One of the most well-known systems is the Coordinator, which is based on a set of speech acts (i.e. requests, promises, etc.) and contains a model of legal conversation moves (see Flores et al., 1988). As users make conversation moves, typically through e-mail, the system tracks their requests and commitments.

Communication-structure oriented models describe organizational activities in terms of role relationships. For example Holt (1988) describes a system in which a person's electronic work environment is composed of a set of centres, where each centre represents a function for which the person is responsible. Within centres are roles that perform the work, and objects that form the work materials for carrying out the functions of the centre. Centres and roles are connected to other centres and roles, and the behaviour of the connections is governed by the role scripts of the interacting roles.

Table 3 Timespan of coordinated group activities

<table><tr><td>Influenced timespan</td><td>Activity objective</td><td>Examples</td></tr><tr><td>Seconds-minutes</td><td>Operational control</td><td>Establishing a conference</td></tr><tr><td>Minutes-hours</td><td>Administrative control</td><td>Preparation of an agenda</td></tr><tr><td>Days-weeks-months-year</td><td>Strategic control</td><td>Activity planning</td></tr></table>

Source: Dittrich, 1991.

## Timespan of coordination

Another characterization of coordination issues refers to the timespan of activities (see Dittrich, 1991). This timespan may range from seconds to days, or even weeks and months. Note, however, that certain coordination activities may cover all three categories; e.g. the joint editing of a report may be synchronous, in which case the duration is limited from seconds to hours, ot it may be asynchronous, in which case the production of the report may be a matter of administrative or strategic nature and may last for months (Table 3).

## Synchronous and asynchronous coordination

Group processes occur in both synchronous and asynchronous situations. For example, office processes sometimes present an asynchronous situation; problems with supporting these processes refer to the organizational knowledge, the possible exceptions, and the coordination of structured activities. Office processes may consist of many parallel asynchronous tasks related by temporal constraints. In such cases, there is clearly a need for temporal coordination; i.e. a mechanism for informing users of required tasks and reminding them of commitments in due time.

Synchronous group operations, on the other hand, are the distinctive feature of certain types of groupware like multi-user editors; the design of systems that satisfy the synchronous mode of operation has been studied extensively within the CSCW field (see Ellis et al., 1991). As already noted above, both types of operational modes are required in real-world organizations (see Johansen, 1991).

## Information sharing and exchange

In general, there exist two alternative approaches in the development of cooperative systems; the first and most traditional approach is to develop systems which support the exchange of information between users. The second refers to the development of systems which exploit the sharing of information (see also Blair and Rodden, 1991).

Systems based on information exchange are often termed ‘structured’ and assume an asynchronous and remote mode of cooperation. The assumption underlying these systems is that the members of the group coordinate primarily by exchanging messages.

The second approach considers the way users share information and aims to develop mechanisms to support sharing. In these systems, users interact through a shared information space. Two crucial characteristics provide the basis for the development of such systems: the form of interaction with the shared space (asynchronous or synchronous) and the type of information represented in the shared information space (textual or multi-media). Again, the consistent computer-based support of organizational coordination requires the existence of both types of approaches.

## Coordination aspects in group systems

The recent years have seen a proliferation of group systems that claim to provide computer support for cooperative work. Existing systems can be classified in two main axes: commercial packages and research efforts.

Commercial applications can be classified in two groups of products: mail-enabled (or mail-aware) programs, (e.g. spreadsheets or word processors that also access mail services) and messaging-centric programs. The former group of applications support group communication, while the main category of the latter includes applications that are e-mail extensions. These extensions refer to group calendaring and scheduling, user notification, rule facilities for sorting and prioritizing messages, workflow control via ordered message routings that replicate existing business processes, electronic signature facilities and integration of the ability to design and store electronic and printable forms (the most advanced products provide query facilities so that forms work as database front-ends) (see Reinhardt, 1993). Various examples can be found in the market; they include, among others, IBM'S PROFS and Digital Equipment Corps' All-in-1 in host systems, while PC systems include DaVinci Systems' Coordinator, Beyond Inc.'s BeyondMail, Reach Software's Workman, ICL's TeamOFFICE, Lotus' Notes, NCR's Cooperation, WordPerfect Corps.'s WordPerfect Office, Microsoft's Scheduler+ and Windows for Workgroups etc (for reviews see The, 1993; Hsu and Lockwood, 1993). Finally, commercial GDSS packages include VisionQuest developed by Collaborative Technologies, Ventana's TeamGraphics, and others.

Research attempts to provide cooperative work have seen the early Info Lens system and its extension to the Object Lens system (see Malone et al., 1989; Lai et al.,

1988), the Cruise system developed at Bellcore, the Japanese NTT MultiMedia Editor, the form-based e-mail system Coordinator (Winograd, 1988), the Collaborator, developed at the University of Massachusetts, the Electronic Meeting Systems (Martz et al., 1992), the GDSS developed at the University of Arizona (Easton et al., 1992), and numerous others.

From the analysis given in previous sections it can be deduced that coordination is one of the most important aspects in computer-supported cooperative work. In order to provide an analysis of the main issues associated with coordination we shall use in the following a number of existing group systems as characteristic examples. Note, however, that the section aims neither to provide a full product survey, nor to set up a formal review of research efforts.

## Characteristics of the systems

In order to analyse the coordination-related aspects of the example group systems presented later on, we classify their characteristics in five categories:

\- Objectives. The overall aims and goals of each system are presented.

\- Characteristics of formal coordination model. For each system we present the underlying control model used, and the representation forms adopted.

\- Type of processing. Two types are distinguished: synchronous and asynchronous, concerning the communication mode; and information exchange versus information sharing, concerning the mode of information flow.

\- Decision support. Some of the systems provide support for conflict resolution, negotiation and decision modelling, while others do not.

\- Organizational environment. We identify these systems that explicitly support user roles and distinguish between the ones that follow a centralized versus a decentralized control architecture.

## Group support systems for organizational processes

In the following we proceed with an analysis of the coordination aspects of seven systems that support decision-making and office processes.

The Amigo Activity Model is independent of technologies and describes the so called activities; activities refer to goals and intentions of a group (see Pankoke-Babatz, 1989). The activity description specifies the regulations required for coordination of several individual tasks. The description consists of four components: message objects, functions, roles, and rules. The latter declare the coordination of activities. Each rule consists of an antecendant part and a consequent part; the triggering of the antecendant part is done by message transfer, temporal constraints or activity-specific variables.

The scope of the Configurable Structured Message System (COSMOS) is the provision of a system to support cooperative tasks based on asynchronous message passing (see Dollimore and Wilbur, 1991). The real-world model of the design is based on the idea of each user participating in group tasks by playing one or more roles within activities; the COSMOS prototype developed provides automatic support for the participants by prompting on actions appropriate to the current state of their joint task and providing contextual information.

The DOMINO system was developed with three design goals: to achieve a high-level specification of cooperative office processes; to split responsibilities between user (executing actions) and system (coordinating actions); and to provide an open and integrated system (see Victor and Sommer, 1991). DOMINO models cooperative office processes by the use of coordination procedures which describe the information flow for accomplishing a common task within a group. The coordination procedure is performed step by step in a predefined manner; each step is performed by an actor and requires/produces information; the CoPlan-S specification language is used for the purpose of designing office procedures.

The EuroCoOp project is a recent ESPRIT project which aims at the development of computer-based systems for the support of spatially distributed persons or organizations cooperating on a common task. This comprises support for asynchronous collaboration as well as synchronous dialogues. Unfortunately, only system design information is available for this project, since it started in 1991. The CSCW toolkit to be developed in the project includes an activity coordination toolkit, a shared information base and a synchronous conferencing system. The activity coordination toolkit will provide a notation for describing collaborative actions and a mechanism for executing the description (track keeping of collaborative activities, delegation of routine tasks to fully or semi-automatic agents, offering of action alternatives, etc.).

The AMS system was developed as a knowledge-based system for the support of office procedural knowledge; recently it has been extended in order to incorporate a speech-act like model based on reusable operators (e.g. send, request, acknowledge and answer) (see Tueni et al., 1991). This extension permits the modelling of negotiations and commitments between different agents. Using the office operators, AMS is capable of supporting non-linear planning and information exchange.

The EIS system was designed in order to support multi-participant activities in organizations involved in quantitative evaluations, analytic modelling and forecasting (see Mentzas and Capros, 1991). This system aims to support the self-organization of cooperative processes and targets at the provision of transparency in information elements concerning originator and goals of produced information. EIS uses an architecture that organizes and controls both the definition and execution of prespecified tasks. It uses the notion of the job as an entity for work-flow organization; the job definition and manipulation tasks are facilitated by the development of a job specification language. From a mathematical point of view, the job can be considered isomorphous to a finite, connected, acyclic graph. The execution of a job follows a number of backward chaining searches down the graph. Coordination of joint tasks is guaranteed by the use of an information catalogue, which stores domain-specific information of the input and output produced by participants.

The PLEXSYS Planning System is a group decision support system designed for use by top level managers and planners in a decision laboratory to conduct actual planning sessions for their organizations (see Nunamker et al., 1988, 1989). The PLEXSYS system was developed as an automated system that provides support for organizational decision processes by integrating data (internal and external), models (quantitative and qualitative) and process management. Participants interact with a variety of automated and manual planning and problem solving models (e.g. through electronic brainstorming, stakeholder identification and analysis, etc). Planning process and modelling knowledge are stored using a hybrid representation technique that is a combination of a semantic inheritance framework and a frame representation.

Table 4 gives a tabular description of the coordination characteristics of the above mentioned systems.

## Issues for analysis

Seven issues are considered crucial in the analysis of coordination; they are the following.

\- Specification and implementation of coordination.

\- Synchronous and asynchronous working phases.

• Information exchange and information sharing.

\- Support of sequential and concurrent processing.

\- Support of negotiation and conflict resolution.

\- Support of analytical modelling.

• Description of organizational environment.

The paragraphs below elaborate on these issues.

## Specification and implementation of coordination

The procedure model of coordination is quite common in the specification of coordination of joint tasks. In addition, the impact of programming is seen in the extensive use of script-based approaches for the representation of the coordination models. The activity description languages constitute in the majority of systems a new 'language'; although the user interface for the specification part of these languages is either graphical (e.g. as in AMS and DOMINO), or form-based (as in EIS), the system usually generates a script-based representation for activity description; see DOMINO, EIS, etc.

Table 4 Characteristics of sample systems

<table><tr><td></td><td>AMIGO</td><td>COSMOS</td><td>DOMINO</td><td>EuroCoOp</td><td>AMS</td><td>EIS</td><td>PLEXSYS</td></tr><tr><td>Objectives of system</td><td>Advanced messaging for organizations</td><td>Configurable structured messages</td><td>Support for office procedures</td><td>Support for cooperating organizations</td><td>Support of collaborative office tasks</td><td>Support of multiparticipant analytical tasks</td><td>Support of unstructured decision processes</td></tr><tr><td colspan="8">Formal coordination model characteristics</td></tr><tr><td>Control model</td><td rowspan="2">Procedure/Communication Script based</td><td rowspan="2">Communication/Conversation Script based</td><td rowspan="2">Procedure</td><td rowspan="2">Procedure/Communication ?</td><td rowspan="2">Conversation Network</td><td>Procedure</td><td rowspan="2">Communication (Forms)</td></tr><tr><td>Representation mechanism</td><td>Script based</td></tr><tr><td colspan="8">Type of processing</td></tr><tr><td>(S)synchronous and (A)synchronous phases</td><td>A</td><td>A</td><td>A</td><td>A &amp; S</td><td>A &amp; S</td><td>A</td><td>A</td></tr><tr><td>Information sharing (IS) or exchange (IE)</td><td>IS</td><td>IE</td><td>IS</td><td>IS/IE</td><td>IS/IE</td><td>IS</td><td>IS</td></tr><tr><td colspan="8">Decision support issues</td></tr><tr><td>Conflict resolution, negotiation</td><td>—</td><td>—</td><td>Yes</td><td>—</td><td>—</td><td>—</td><td>Yes</td></tr><tr><td>Mathematical modelling</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>Yes</td><td>Yes</td></tr><tr><td colspan="8">Environment</td></tr><tr><td>Support of roles</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>—</td><td>Yes</td></tr><tr><td>Control architecture</td><td>Central</td><td>Central</td><td>Central</td><td>?</td><td>Central</td><td>Central</td><td>Central</td></tr></table>

A feature not generally found in the specification of coordination refers to the ability to dynamically apply changes in the specifications. The systems reviewed here permit the static description of activity coordination but include only partial support for the dynamic (run-time) modification of predefined specifications; see e.g. the EIS system, in which the user has the ability to dynamically change the 'route' of backward searches for jointly produced information entities.

## Synchronous and asynchronous working phases

The majority of CSCW systems adopt an asynchronous approach. It has been argued that 'the most misunderstood concept is the view that an asynchronous (or nonsimultaneous) communication process is a problem, because it is not the sequential process that people use in the face-to-face mode' (see Turoff, 1991, p. 96). The main idea behind this argument is that the potential for real involvement in the group processes lies in the fact that individuals can deal with that part of the problem they can contribute at at a given time, regardless of where the other individuals are in the process.

This approach benefits from the very advantage of group processes: since individuals with different psychology, expertise and resulting approaches to problem solving, contribute their ‘differences’ to the group problem, the role of computer-based support is to allow to do exactly this and to integrate the results for the group as a whole. On the other hand, the specification of group processes may well be in conflict with the ways which specific members of the group can best contribute to dealing with the problem.

Hence, the challenge for group processes is to support the individual to deal with the problem in ways consistent with his or her cognitive style; the design challenge deals with developing these communication facilities which would allow for both synchronous and asynchronous processes.

## Information exchange and information sharing

Successful group coordination systems require aspects of both information (i.e. message) exchange and information sharing to be integrated. Shared spaces, however, need to capture the organizational context of the work and should take into account the co-existence of many different forms of coordination and cooperation.

Work conducted in the open distributed systems area, provides a number of open research issues ranging from distribution transparency to the subject of continuous synchronization for the control of event orderings and precise timing of multimedia interactions (see Blair and Rodden, 1991). The support of group processes could benefit greatly from advancements in such research.

## Support of sequential and concurrent processing

A subject that arises from the two above mentioned issues refers to concurrency control. A wide spectrum of solutions have been proposed for concurrency control; they range from ‘pessimistic’ ones that prevent users from any access that would cause data inconsistency, to ‘optimistic’ ones that allow transient inconsistencies; see Barghouti and Kaiser (1990) for a survey of concurrency control mechanisms which may support coordinative activities.

The pessimistic approach has been traditionally supported by means of simple locking and transaction mechanisms. These approaches, however, are too restrictive for cooperative work systems. Hence, a relative relaxation of the strict consistency criteria is required; for example, soft locking could be used, in which the system only marks data items as reserved and produces warnings for data objects that may produce inconsistencies. On the other hand, provisions for users who did not properly finish their activities (i.e. did not unlock some data objects) have to be made; the more common approach is the use of tickle locks, in which an agreement is made that after a time-out a related lock must be released (see Greif and Sarin, 1987). Concurrency mechanisms such as dependency-detection, reversible execution and operations transformations have only recently been applied to the group process systems (see Ellis et al., 1991).

## Support of negotiation and conflict resolution

The subjects of negotiation and conflict resolution during the coordination of group processes have received little attention in the systems developed in the literature. Issues to be examined refer to the types of messages exchanged, the protocols according to which the negotiation takes place, the development of technically sound coordination frameworks that include negotiation protocols, etc.

Research in this field could make use of recent advances in the distributed artificial intelligence area; see Durfee (1988). For example Kreifelts and Martial (1991) developed a coordination framework for negotiation of autonomous agents, based on the conversational paradigm; in their framework negotiations for activity coordination are performed as conversations with a coordination agent who mediates between the other agents.

## Support of analytical modelling

Information retrieval and modelling systems facilitate identification of key issues in group decision processes by providing a means of probing the assumptions and facts underlying a particular problem. While data can be used to clarify the factual bases of the discussion and reveal where the participants' beliefs about facts may be in error, analytical quantitative models make it possible to relax or tighten constraints, change assumptions, and bring in or throw out variables from consideration.

Although only two of the reviewed systems provide explicit support for quantitative modelling, it is commonly agreed that explicit support is required for storing and manipulating models in the decision processing component of group support systems (see Nunamaker et al., 1991).

## Description of organizational environment

The incorporation of features applicable to the overall organizational environment may enhance the coordination aspects of group systems. The use of job profiles and the definition of specific task domains and responsibilities for group participants should be added in a complete system, in order to increase the effectiveness of coordination.

## Conclusions

The bias towards technological development makes efforts on group support systems very ‘supply push’ in their orientation. The designers of such systems usually develop technological aids that they presume will be needed by decision makers, in contrast to the ‘demand pull’ forces of innovation, in which demand lures developers into creating a supply that meets that demand (see Kraemer and King, 1988). Coordination of joint tasks is an organizational issue crucial in the day-to-day work of all organizations, which falls in the category of issues for which although demand is considerable, the supply provided is not adequate.

The present paper highlighted the crucial role of coordination in computer-based group-support systems and identified a number of issues that arise with reference to coordination of joint work within an organizational setting.

Recent technology advancements permit the introduction of commercial applications that support group processes in organizations (see Kirkpatrick, 1992). On the other hand, studies on the implications of the introduction and assimilation of group-support technologies in organizations are rather limited. For example Applegate (1991) proposes a framework of research on the introduction and assimilation of CSCW technologies in organizations and of the linkages between R & D and target organizational units. The focus on her research, however, covers the whole area of CSCW technologies. The importance of electronic coordination, nevertheless, requires special analysis, that would treat the issues mentioned in the present paper in more detail.

In addition, the social implications of networked organizations have been studied by Sproul and Kiesler (1991). They argue that the use of e-mail and computer conferencing within organizations alters social relationships, and show that electronic groups often behave differently than face-to-face groups, even when working on similar tasks. Specifically, they show that electronic groups can take from four to ten times as long as face-to-face groups to develop a consensus, that the decisions at which they reach are often riskier, but participants trust them as much as they do the more conventional decisions made in face-to-face groups.

Similar analyses that would focus to the various forms of electronic coordination are needed, in order to reveal the potential problems, and/or advantages of the technological advances. Beside the time required for a consensus to be reached and the riskiness of decisions, additional implications of coordination that should be examined include aspects of information overload, privacy, misinformation, technical risks, and long-term management of the available information.

## Acknowledgement

The author is grateful to Leslie Willcocks and the two anonymous referees for their comments and suggestions to improve the paper.

## References

Applegate, L. (1991) Technology support for cooperative cork: a framework for studying introduction and assimilation in organizations. Journal of Organizational Computing, 1, 11–39.

Ang, J.S.K. (1993) Performance criteria of a sound office

analysis methodology. International Journal of Information Management, 13, 51–67.

Applegate, L., Ellis, C., Holsapple, C.W., Radermacher, F. and Whinston, A.B. (1991) Organizational computing: definition and issues. Journal of Organizational Computing, 1, 1–10.

Auramaki, E., Lehtinen, E. and Lyytinen, K. (1988) A speech-act based office modelling approach. ACM Transactions on Office Information Systems, 6, April, 7–23.

Balzer, R. (1989) Process programming: passing into a new phase. Software Engineering Notes, ACM Sigsoft, 14, 43–5.

Barghouti, N.S. and Kaiser, G. (1990) Concurrency Control in Advanced Database Applications. Technical Report CUCS-425–89 November (Columbia University, Department of Computer Science, New York).

Blair, G.S. and Rodden, T. (1991) The Impact of CSCW on Open Distributed Processing, presented, in International IFIP Workshop on Open Distributed Processing, Berlin, Germany, October 8–11.

Butterfield, J., Rathman, S. and Whinston, A.B. (1992) Groupware: a survey of perceptions and practice. ACM SIGOIS Bulletin (Special Interest Group on Office Information Systems), 13, 6–7.

DeSanctis, G. and Gallupe, R.B. (1987) A foundation for the study of group decision support systems. Management Science, 33, 589–606.

Dittrich, J. (1991) Groupware Report: Requirements. State of the Art and Analysis of Group Support Systems. Technical Report (GMD Focus, Berlin).

Dolimore, J. and Wilbur, S. (1991) Experiences in Building a Configurable CSCW System, in Bowers, J.M. and Benford, S.D. (eds) Studies in Computer Supported Cooperative Work (Science Publishers B.V., Elsevier, Amsterdam).

Durfee, E.H. (1988) Coordination of Distributed Problem Solvers (Kluwer, Boston).

Easton, A.C., Vogel, D.R. and Nunamaker, J.F. (1992) Interactive versus stand-alone group decision support systems for stakeholder identification and assumption surfacing. Decision Support Systems, 8, 159–68.

Ellis, C.A., Gibbs, S.J. and Rein, G.L. (1991) Groupware: some issues and experiences. Communications of the ACM, 34, 39–58.

Flores, F., Graves, M., Hartfield, B. and Winograd, T. (1988) Computer systems and the design of organizational interaction. ACM Transactions of Office Information Systems, 6, 153–72.

Greif, I. (1988) Computer-Supported Cooperative Work: A Book of Readings. (Morgan Kaufman, San Mateo, CA).

Greif, I. and Sarin, S. (1987) Data sharing in group work. ACM Transactions on Office Information Systems. 5, 187–211.

Hatcher, M.E. (1992) Group decision support systems: decision process, time and space. Decision Support Systems, 8, 83–4.

Holt, A. (1988) Diplans: a new language for the study and implementation of coordination. ACM Transactions on Office Information Systems. 6, 109–25.

Hsu, J. and Lockwood, T. (1993) Collaborative computing. Byte, March, 113–20.

Johansen, R. (1988) Groupware. Computer-Support for Business Teams (The Free Press, New York).

Johansen, R. (1991) Teams for tomorrow, plenary speech. Proceedings of the 24th Hawaii International Conference on Systems Sciences, 3, 521–34.

Kirkpatrick, D. (1992) Here comes the payoff from PCs.
Fortune, March 23rd, 51–7.

Kraemer, K.L. and King, J.L. (1988) Computer-based systems for cooperative work and group decision making. ACM Computing Surveys, 20, 115–46.

Kreifelts, T. and Martial, F.V. (1991) A Negotiation Framework for Autonomous Agents, in Demazeau, Y. and Muller, J.P. (eds) Decentralized Artificial Intelligence, (North Holland, Amsterdam).

Lai, K-Y., Malone, T.W. and Yu, K-C. (1988) Object lens: a 'spreadsheet' for cooperative work. ACK Transactions on Office Information Systems, 6, 332–53.

Lochovsky, F.H., Hogg, J.S., Weiser, S.P. and Mendelzon, A.O. (1988) OTM: specifying office taks, in Proceedings of the Conference on Office Information Systems, (Palo Alto, California, March 23–25) (ACM, New York).

Malone, T. and Crowston, K. (1990) What is coordination theory and how can it help design cooperative work systems? in CSCW'90, Proceedings of the Conference on Computer-Supported Cooperative Work (ACM, New York).

Malone, T.W., Yu, K.-C. and Lee, J. (1989) What good are semistructured objects? Adding semiformal structure to hypertext, Technical Report #3064.89.MS (Massachusetts Institute of Technology, Cambridge, MS).

Martz, Jr., W.B., Vogel, D.R. and Nunamker, J.F. (1992) Electronic meeting systems: results from the field. Decision Support Systems, 8, 141–58.

Mentzas, G.N. (1991) A review of object-orientation and knowledge processing in office models. European Journal of Information Systems, 1, 193–203.

Mentzas, G.N. and Capros, P. (1991) A Synergetic DSS for Support of Work-Flow in an Analytical Environment, in Decision Support Systems and Qualitative Reasoning Singh, M.G. and Trave-Massuyes, L. (eds) (North Holland Publ. Co., Amsterdam).

Nunamaker, J.F., Applegate, L. and Konsynski, B. (1988) Computer-aided deliberation: model management and group decision support. Operations Research, 36, 826–48.

Nunamker, J.F., Vogel, D. and Konsynski, B. (1989) Interaction of tasks and technology to support large groups. Decision Support Systems, 5, 139–52.

Nunamaker, J.F., Dennis, A.R., Valacich, J.S., Vogel, D.R. and George, J.F. (1991) Electronic meeting systems to support group work. Communications of the ACM, 34(7), July, 40–61.

Pankoke-Babatz, U. (1989) Computer-based Group Communication - Amigo Activity Model (Ellis Horwood Limited, New York).

Reinhardt, A. (1993) Smarter e-mail is coming. Byte, March, 90–108.

Searle, J.R. (1969) Speech Acta: An Essay in the Philosophy of Language (Cambridge University Press, Cambridge).

Shaw, M.E. (1981) Group Dynamics: The Pyschology of Small Group Behavior, 3rd edition (McGraw Hill, New York).

Singh, B. (1989) Invited Talk on Coordination Systems, at the

Organizational Computing Conference, November 13–14, Austin, Texas.

Sproul, L. and Kiesler, S. (1991) Connections - New Ways of Working in the Networked Organisation (The MIT Press, Cambridge, MA).

The, L. (1993) Turn your e-mail into groupware. Datamation, April 15, 28–32.

Tueni, M., Li, J. and Ang, J. (1991) Knowledge-Based Office Automation and CSCW, in Studies in Computer Supported Cooperative Work, Bowers, J.M. and Benford, S.D. (eds), (Elsevier Science Publishers B.V., Amsterdam).

Turoff, M. (1991) Computer-mediated communication requirements for group support. Journal of Organizational Computing, 1, 85–113.

Victor, F. and Sommer, E. (1991) Supporting the Design of Office Procedures in the DOMINO systems, in Studies in Computer Supported Cooperative Work Bowers, J.M. and Benford, S.D. (eds) (Elsevier Science Publishers B.V., Amsterdam).

Vogel, D. and Nunamaker, J.F. (1988) Group Decision Support System Impact: Multimethodological Exploration, in Proceedings of Conference on Technology and Cooperative Work Galegher, J., Kraut, R. and Egido, C. (eds) (Tuscon, Arizona, February 25–28, National Science Foundation, Bell Communications, University of Arizona, Tucson).

Winograd, T. (1988) A Language/action Perspective on the design of Cooperative Work, in Computer-Supported Cooperative Work: A Book of Readings, Greif, I. (Morgan Kaufman, San Mateo, CA).

Zisman, M.D. (1977) Representation, Specification and Automation of Office Procedures, PhD dissertation, Wharton School, University of Pennsylvania, Philadelphia.

## Biographical note

Dr Gregory Mentzas is Assistant Professor in the Department of Electrical and Computer Engineering of the National Technical University of Athens (NTUA). He received a Diploma in Engineering in 1984 and a PhD in 1988, both from NTUA. From 1984 to 1989 he worked as a principal researcher in projects financed by the Commission of the European Communities and the Greek Secretariat for Research and Technology. During 1990–1991 he developed the Energy Information System of EEC/DG-17/A2, a group support system that includes an information repository on energy, macroeconomic and environmental issues of EEC countries. In the 1991–1992 period he was involved in the design and development of an office information system in the ESPRIT project Large-Scale Correct Systems Using Formal Methods (ESPRIT, 5383).

His articles appear in several refereed journals and books. His current research activities are focused on information engineering for organizational systems, computer-assisted mathematical modelling, information systems strategy planning, cooperative work, and intelligent office systems.

Address for correspondence: Department of Electrical and Computer Engineering, National Technical University of Athens, 42, 28th October str., 10682 Athens, Greece.
