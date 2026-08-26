---
otero_id: 27134
otero_key: "UCQWWW7A"
title: "Information Systems Support for Group Planning and Decision-Making Activities"
authors: "Margaret A. Rathwell; Alan Burns"
year: "1985"
journal: "MIS Quarterly"
doi: "10.2307/248952"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Information Systems Support for Group Planning and Decision-Making Activities
Author(s): Margaret A. Rathwell and Alan Burns
Source: MIS Quarterly, Vol. 9, No. 3 (Sep., 1985), pp. 255-271
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/248952

Accessed: 08/05/2014 20:47

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# Information Systems Support for Group Planning and Decision- Making Activities

By: Margaret A. Rathwell
Alan Burns
Postgraduate School of Computing
University of Bradford
Bradford, W. Yorkshire
England

## Abstract

Planning is a basic organizational decision-making activity often requiring the judgement and expertise of a group of organization members. Computer and communications support for the planning process can help individuals and groups who may have different perspectives and priorities, to communicate and coordinate their activities. This article examines how groups organize their planning and decision-making activities in a number of application areas, and identifies their requirements in terms of communication structures and online information systems capabilities. Examples are given from engineering projects, computer projects, scientific communities, company planning, and crisis management. The applicability of a distributed decision-making approach to organizing information systems support is assessed as a way of meeting these requirements.

Keywords: Information systems organization, decision support systems, distributed decision-making systems

ACM Categories: H.4.2, H.4.3, K.4.3

## Introduction

Planning, in general, is an example of an unstructured decision-making process that cannot be described fully before the decision is made. Strategic planning, for example, often requires the judgement and expertise of a group of organizational members, typically boards of directors or committees. A recent development has been the use of computer and communication support for the planning process. Computer assistance has, in many instances, been provided by online decision support systems (DSS) which aim to improve the effectiveness of decision making in problems that require some balance between judgement and analysis. Brandaid [2] for example, is a marketing planning DSS for evaluating pricing, promotion, and sales force decisions. Communication support may include computer message and conferencing systems which structure written communications within a group. The Electronic Information Exchange System (EIES) [19], which has been used in scientific research communities, is one example of a conferencing system.

A particular need in group planning and decision-making tasks is to coordinate the activities of individuals or subgroups who may have different perspectives and priorities. Decisions made in one part of the organization may constrain those to be made in other parts, and compromises have to be reached. Information systems support has traditionally focused on processing and gathering information with management information systems (MIS). Then attention moved to decisions with DSSs which support specific decision-making processes and are built upon MIS. Distinguishing features of DSSs and factors influencing their success are discussed by Meador, et al. [24], and Sanders and Courtney [35]. Thomas and Burns [40] demonstrated the need to support tasks which involve cooperation and conflict between differentiated organizational units, and extended the DSS concept to one that would enable two or more decision-making parties to cooperate in using DSS tools in distributed decision making (DDM). DDM is a mechanism for interacting DSSs in an organization to allow groups, not necessarily linked in a hierarchical manner, to cooperate with one another. In a recent article, Huber [18] has examined the design of group decision support systems (GDSS) which facilitate the interactive sharing and use of information among a group of people in a decision-related meeting. DDM incorporates the distribution of GDSSs and extends GDSS to allow communication between separate DSSs. A DDM system is built upon the DDS layer and is concerned with organizational communication and conflict in decision making and planning. Figure 1 shows this progression by adapting Sprague's connotational view of DSS [39].

The DDM focus encompasses information retrieval (and generation), information sharing, information use, and conflict resolution features such as the explanation of decisions. The architecture of a DDM system, which is described in the latter part of this article, enables cooperation and coordination between separate DSSs, which may have developed in an evolutionary manner by different subunits of an organization. The quality of support that could be provided by a DDM system depends upon an understanding of both group decision-making processes and information systems building. The aim of this report is to look at decision-making processes in the planning application area, in particular to consider:

1. how groups organize their decision-making activities,

2. how these activities can be supported by computer and communications systems, and

3. whether DDM systems could provide an effective group decision making environment.

First, group planning and decision-making processes are discussed in general terms. Then a survey is made of how groups organize their decision-making activities in application areas involving decision making by many people in separate, but interrelated nodes of an organization. From an analysis of the requirements of these applications general conclusions are drawn as to the applicability of DDM in this area.

![](/api/attachments/UCQWWW7A/fulltext/images/a1ee05136a8ab348b763f01a06133492df39fc6c62671a17c25bf5435d1c4732.jpg)  
Figure 1. Focus of DDM

## Decision-Making and Planning Processes

## Decision-making processes

Different and conflicting explanations of decision processes are provided by various theories of decision making. Decision making is often identified with choice, that is, the selection of a specific course of action from among two or more alternatives in order to maximize the expected value of a decision. Techniques such as program-planning-budgeting (PPB) and corporate planning are attempts to bring decision making more in line with a rational model. The rational view assumes clarity and agreement of goals and objectives among those involved in making decisions. This contrasts with the pluralistic perspective of organizations which holds that organizational decisions are the outcome of bargaining among actors with different interests and perceptions. The pluralistic view points to incremental theories in which decision making is seen as a succession of limiting comparisons, eventually reaching a consensus. Models of organizational decision making are discussed in depth by Huber [17] and Sage [33]. As well as the rational and political/competitive models, Huber describes the “garbage can” model, which emphasizes chance and timing in determining organizational choices. And finally, in the program model organizational decisions are the consequence of the programs (standard operating procedures, group norms, budget limitations) and the programming (professional training, reinforcements of past decision related behavior) of the units involved.

The DSS approach was a move away from a normative or prescriptive view of decision making toward a descriptive model based on how decisions are actually made in an organization. Studies show that there are a wide variety of decision-making processes and that these are interwoven and interrelated. They are popularly categorized into three main steps: intelligence, design, and choice [39]. Much DSS work has been concerned with the generation of alternative solutions and choice between alternatives. There has been little attention given to tools that support the initial problem recognition and description phases. Also, the role of communication in the decision-making process has been largely ignored.

In practice, communication forms a large part of planning and group decision-making activities. Scher [36] demonstrates that communication is an essential component of systems that support decision processes. Flores and Ludlow [11] also observe that decision makers tend to carry out their activities through issuing commitments in conversations. For example, as a result of an offer from a supplier a number of interactions are triggered ending with some result such as the signing of a new contract. They describe the activity in terms of a resolution having been reached instead of a decision having been made. Interactions may include giving attention to a topic, accepting, declining or countering an offer, asking for clarifications, or answering questions. Sometimes the requirements for reaching a resolution will be clear; other times the process will require a more prolonged delay and/or debate. Choosing between alternatives is only a particular case within the border context of resolution.

## Planning as a group activity

Planning is concerned with the management of change. Ackoff [1] argues that the principal benefit of planning comes from engaging in it, and that there is a need for workers to participate directly in the planning process. Similarly, Sandberg's [34] concept of democratic planning rests on the belief that participation in the preparation and carrying through of plans should be spread among all members of a system, and they all should have the same amount of resources to influence planning.

Ackoff's concept of “interactive planning” emphasizes three points. First is the importance of direct participation where workers can plan for themselves. Second, planning should be a continuous process. Third, planning should be holistic so that units at the same level of an organization should be planned for simultaneously and interdependently, and every level of the system should be involved in a multi-level system. These ideas identify planning as a group activity, with decisions being made at the lowest appropriate level and with communication and coordination between groups.

## Communication and coordination

Thomas and Burns [40] illustrated the need for communication and coordination support in group planning in a case study of scheduling resources and manpower in two divisions of a large manufacturing company. The engineering division was responsible for the design and project management of a new plant. Maintenance staff attached to the production department (electricians, plumbers, etc.) were responsible for keeping existing lines working, but were also employed for installation in the new plant. The project engineers and maintenance department mostly worked independently of each other but needed to incorporate each other's decisions in their plans. There was the potential for conflict between the priorities of the engineering projects and maintenance's need to provide for unforeseen circumstances such as equipment failure.

DSSs were built for both the engineering and maintenance groups. A project management DSS (based on critical path techniques) was introduced for the project planners to support their scheduling decisions, and a DSS was developed for the tradesmen for preventative maintenance. The project management DSS was used differently by planners on different projects. One project planner developed a simple plan concentrating on the major phases of the project; the plan being agreed upon at biweekly project control meetings. Changes were made during the meetings if plans became unrealistic due to conflicts with previous commitments. A second project planner used the system in a more detailed manner and used personal contacts in the maintenance department to draw up intricate plans for each week. In this case maintenance foremen resolved conflict amongst themselves and the plan was accordingly changed to reflect what was expected to happen.

Over time the project management DSSs were used less and less. An important reason for this failure was inadequate organizational and group support [13] between the planner and other parties on the project. Some activities involved a sequence of decisions, others depended on interaction between the separate units. Cooperation between the respective DSSs of the engineers and maintenance staff was required. For efficient scheduling both divisions needed to know what the other had scheduled.

## Group Planning and Decision-Making Applications

A useful framework for understanding decision-making processes in organizations is based on communication. Planning may also be viewed as a group activity involving many people in decision making and requiring cooperation and coordination between different groups. This article is concerned with the kinds of support required from an information system to assist group planning.

This section examines the application area of group planning in resource allocation problems in more detail. The aim is to examine how groups organize their decision-making activities and how they can be supported by computer and communications systems.

A number of multi-user applications concerned with resource allocation problems and involving planning and subsystem communication/coordination are described here and in the literature on DSS and decision making. A common feature of these applications is that they are professional groups working in environments where interaction with computer systems is a natural part of the group activity.

## Engineering projects

Different groups involved in an engineering project work, to some extent, independently on their particular sub-system of the project. Neuhold and Rabe [25] describe how engineers at the Bechtel Corporation are assisted by computers in the design and construction planning of large pressure containment vessels for chemical plants and petroleum refineries. The engineers build and maintain their own databases and simple programs for problem solving. Local information pools may contain informational or operational data such as legal codes, material descriptions, costs and experimental results. Database organizations and natural languages for database manipulation allow interactive queries of the form 'GET COST, ALL VESSELS TYPE T10, STATUS FABR'. Engineers also require modeling or analytic-type DSSs in their work, for example for calculations based on mathematical algorithms and techniques. They may develop their own programs to perform functions to fill their immediate needs.

The engineers at Bechtel created an interactive design DSS and applied it on several projects. Each group of engineers can use the system in their own way, and add their own programs and permanent data files to improve and extend it. Many DSS tools can be shared between engineers, in part or in total. Furthermore, apart from sharing data and software tools, human information sources (the judgement, experience and creative intuition of the engineers) are important. The applications suggest there is a need for interdisciplinary cooperation on engineering projects using computers as a means of communication. Proposals included “suggestions,” “gripes,” “advice,” “try it,” and “system news and views.” The potential of computer conferencing techniques in engineering projects is also described by Turoff and Scher [41]. They note that recognition of, and provision for, the communications interface by engineering management can determine the success or failure of a project.

The direct use of personal computers by engineers to develop their own applications is also described by Goodwin [12] and Kull [21]. In civil engineering, jobs tend to be one time and judgements are based on similar, but not identical experiences. The intuitive judgements of individual engineers may be supported by computers and communications for conveying accurate and up-to-date information about a project. In the consulting engineering firm of W.S. Atkins [12] engineers work on separate components of a structure and use a selection of complementary applications software packages at different stages of a project. Similarly, at Ove Arup [8] engineers decide which computer-aided design tools they wish to use from those available and can opt out of using the computer if manual methods seem to be more efficient.

## Development projects

Project coordination is also required in large computer hardware or software development projects such as the writing of a compiler. Some of these requirements are discussed by Brooks [4]. The development of a large system is likely to be partitioned between small teams of engineers or programmers, each responsible for a part of the system. Resource allocation decisions involving machine time, staff, equipment, administrative support, and work agreements with other groups need to be made. A good description of these types of decisions can be found in Tracy Kidder's The Soul of a New Machine [20] which describes organizational conflict and pressure behind the design and building of the MV/8000 at Data General.

One characteristic of the division of responsibility in a project is the allocation of different tasks to groups and different roles to individuals. On the MV/8000 project, for example, there were three main groups: the hardware team, microcoders, and programmers. Individual roles included someone in charge of the overall design, a secretary, and team leaders. In a software project typically there are different teams for different modules of the project, each led by a team leader. Other roles might include someone responsible for the design specification, a testing team, a documentation team, and a librarian responsible for current releases of software and test data. Individuals in supervisory roles may have information gathering and retrieval tools to keep track of team members' activities for scheduling, priority assignment, technical evaluation, and guidance during the project.

Communication between different groups in a project is vital for the coordination of plans and activities. In a centralized management structure task coordination would be the responsibility of a single manager, but in a decentralized system group members must develop and sustain cooperation between themselves. If one team encounters a problem relating to an interface with another part of the system, then the two parties need to discuss the nature of the problem and reach agreement together. If a new feature is desirable, then this would have to be agreed with the member of the project group with overall responsibility for the design. The need for coordination is particularly obvious in the interfacing of different modules for unit testing and system testing. Many of these communication functions could be mediated by computer.

Cashman and Holt [7], and Dzida [10], note that cooperation between team members in a software engineering environment requires more than a simple message system, and they argue that a means for structuring project communication is needed. Cashman and Holt describe a protocol-driven, computer-based message system called MONSTR, implemented under the National Software Works project, a distributed operating system for the Arpanet internet. In this system a manager defines the rules of communication, including the allowable paths of communication, the meaning of messages sent over each path, and a description of the project structure. Dzida proposes a contrasting rule-guided communication system in which new message types and communication rules can be introduced by all members of a team.

As with the engineering projects described earlier, different teams are likely to have their own diagnostic programs and data banks of results. One example of a practical software development system is that used by Plantronics/Zehntel [43]. It includes software tools such as compiler generator utilities and text processing routines for program documentation, electronic mail, and configuration management tools for tracking and combining pieces of software. The development of a distributed integrated project support environment (IPSE) is part of the Alvey (UK) software engineering strategy, for example the ASPECT project [27].

## Scientific communities

In scientific communities groups of scientists engaged in the same area of research communicate often and intensively with each other in order to carry out their work. Garvey and Griffith [16] have shown how science relies heavily on informal networks of discussion, small group meetings, and exchange of drafts and preprints to keep abreast of current activities and views on the value and relevance of specific research problems. Typical decisions include which problems to choose, where and how to spend time and resources, which techniques to use, and so on.

Cardwell [6] describes the use of computer systems in an atomic energy research and development environment at Oak Ridge National Laboratory. Staff members used a variety of computer systems linked together by telecommunications lines, including small machines for localized dedicated functions as well as large central machines. The systems are used for scientific and engineering calculations, collection and analysis of experimental process data, storage and selective retrieval of bibliographic references or data files, and data processing systems such as stock control and management accounting. Common tools, such as text processors and editors, are also used. In research laboratories and engineering environments local area networks are increasingly being employed to facilitate communication between users.

The distributed computing system used by the Xerox Corporation, called Grapevine $[3,37]$ , is a large-scale example since the research internet extends across the USA and also includes Canada and Britain. Most computing is done on personal workstations which may be used at different times for different tasks. The primary use of the Grapevine system is for delivering computer mail, allowing a group of users to exchange messages.

Project planning, forecasting activities on a long-term basis, and shorter-term scheduling of resources are also part of scientific research. Since these activities depend upon the expertise of a wide variety of personnel and are based on human judgement, they require considerable lateral communication and feedback. For example, individuals discuss proposals, look at their implications, and attempt to reach agreement. Delphi conferencing, a form of structured brainstorming, is a tool used for coordinating such group communication. Participants record their ideas and judgements according to tailored questionnaires, the results of which are fed back to the group, and in this way a decision emerges.

## Company planning

In commercial organizations, group decision support systems have been used to support information sharing amongst groups of individuals in company planning and decision making. GDSSs are used primarily to support a group of people in a decision-related meeting $[18]$ . This type of application is illustrated by executive group planning at the Execucom Systems Corporation, reported by Wagner $[42]$ . DSS modeling activities are carried out in the planning laboratory, which is essentially an electronically equipped boardroom. Executives assemble round a boardroom table, have their own graphics terminal embedded in the table top, and at the front of the room is a large color video projector and screen. Each executive's terminal can either be a slave to the large screen or can be used as a personal terminal. This latter mode is used for retrieving data from databases, sending messages to staff and receiving communications from them, analyzing data, and interrogating private models.

A typical activity might be a committee convened to consider a request for resources. A model is presented in Execucom's Interactive Financial Planning System (IFPS) language, which is an example of an end user (or fourth generation) language used for developing DSSs quickly [23]. IFPS is based on a spreadsheet model and the assumptions of the model — variables, data, and interrelationships — are shown on the large screen for discussion in the planning laboratory. Results can be displayed and participants may challenge the assumptions by offering additions, deletions, and modifications of the model, performing 'what if' analyses through the DSS.

One of the packages used in the planning laboratory, called Mindsight, is an example of a DSS for quantifying and externalizing human judgement. It is used to extract from group members their judgement, opinions and thoughts about the assumptions in the model being presented, and provides a number of tools to assist in the process. One such tool is a voting facility; for example, participants may be asked to vote on whether or not to continue funding the development of a new product. The poll can be either open or anonymous and the results are presented graphically on the screen. Another tool is the idea dialogue which is a means for individuals to display their feelings about some particular issue. Each employee composes their answer, and then the results are presented in a scrambled order on the screen for anonymity. These activities help in the process of achieving consensus, primarily by identifying areas of non-agreement and incomplete communication thereby helping to bring about a quicker and more rational resolution of differences. A similar type of system to Mindsight is CONSENSOR [38], an electronic decision tool which facilitates discussion and decision making in meetings.

The planning laboratory facility can also be used for briefing sessions on operational information in a user's system. One or more individuals control such briefings, calling a sequence of data presentation packages which have been prepared for review and discussion by participants. Users can also call directly for displays or dynamically create new ones. At Execucom, the planning laboratory is used for monthly financial meetings in which the previous month's results are reviewed. Wagner also hypothesizes the concept of a distributed planning laboratory whereby managers are also to participate in collective DSS processes without assembling at the same location.

## Crisis management

Crisis management involves major and unexpected events in the routine of an organization. Some examples of crises in engineering management are: delay or unavailability of a crucial physical component in a project, departure of a key engineer, a cost overrun, or a major project not meeting performance specifications at the first test [41]. From work on political and economic crises of a national and international nature, Kupperman [22] found that conventional information systems rarely help in crises so managers tend to fall back on experience, intuition, and bias to make ad hoc decisions.

Hiltz and Turoff [16] observed that crisis management often requires the following:

1. factual information from various sources,

2. value judgements by key individuals,

3. discussion on proposed alternatives and their ramifications,

4. anonymity in voting or discussing such issues, and

5. a way to determine a general consensus within a short period of time when a decision must be reached.

These requirements indicate the potential of DSS's for quantifying and externalizing human judgement. Ordinary database and modeling DSSs may also be used; for example, simulation models can be used to allow management to examine the consequences of alternative courses of action as a mechanism for preparing for and/or preventing crises.

EMISARI (Emergency Management Information System and Reference Index) [16] is an example of a computer conferencing system developed by the Office of Emergency Preparedness (OEP) for domestic crisis management. During the wage-price freeze in 1971 in the United States, the ten regional offices of the OEP needed to be able to generate and share timely and useful data on policies, problems, and programs. Staff had to interpret and convey information to the public. The EMISARI system acts like a large blackboard on which up to 100 participants of a conference can write. The blackboard is under the control of one individual, the monitor, who keeps the names and descriptions of individuals participating in the conference. Tables of data or text items, such as policy, situation reports and news, are each assigned to a member of the group who is responsible for supplying the information on a regular basis. The system includes facilities for voting on proposals put forward in a discussion. Communication support for multiple party decision-making processes is an important feature of many public sector DSSs [14].

## Issues From The Survey

In order to understand the nature of, and potential for, computer support of organizational decision making, a number of application areas have been examined. One characteristic of the groups involved is that individuals define their own tasks and information processing needs. Through the use of DSSs, the groups allow their decisions to be supported by computer systems. Where decisions made by one subunit of an organization constrain decisions in other parts (such as scheduling activities in engineering or software projects), or where information is gathered from many parts of the organization for planning (for example in strategic planning), cooperation between groups is required. Negotiation and conflict resolution between different groups may be involved in the process. Communication consists of making tentative decisions and commitments, and a series of interactions with feedback between participants. In this way, decision-making parties may move in stages towards a goal such as the design of a new software system or the formulation of a divisional plan.

This kind of interactive planning is not supported by traditional systems, organized to filter information up through a hierarchy to a few decision makers at the top. Instead, the problem structure requires coordination between subunits on a horizontal level. These considerations indicate both technical and managerial requirements for information systems support, forming the background for the development of the distributed decision-making model which is explored in the next section.

## IS Support and Distributed Decision Making

Neuhold and Rabe [25] identify three types of mechanisms for user support provided by a computer system. These are:

1. database functions for the description and manipulation of data contained in systems,

2. languages and direct user support features for communication between user and systems, and

3. control functions that supervise utilization of the system by multiple users and ensure the integrity of internal data manipulation and user communication with programs and databases.

Communication systems extend the functions of the second category to allow communication between geographically dispersed machines. Hence, individuals are able to communicate with each other using the computer system as an intermediary. The group activities described above illustrate the use of computer systems for planning and decision-making support which included DSSs, database management systems, natural language interfaces, computer conferencing systems (CCS), and computer-based message systems.

Even though networking is now becoming common, a mechanism for cooperating DSSs in an organization does not yet exist. Several people cooperating around one DSS as in a GDSS [13,18], and the distribution of a single DSS through an organization [36], have been described, but little attention has been paid to interaction between several DSSs. Distributed decision making (DDM) is an extension of the DSS concept to allow a number of such systems to co-exist within an organization in a manner that need not imply any particular managerial structure. A distributed decision-making system is an integrating mechanism enabling groups of decision makers to use and interface separate support systems. Thus, it provides the control mechanisms identified in Neuhold and Rabe's third category, enabling decision makers to make effective use of DSSs in a distributed environment.

The general aims of using computer support in planning are to allow the generation of more ideas and more information on the implications of these ideas, and to widen the scope for making choices to all those affected. This rests on the belief that better solutions can be developed by the people concerned locally rather than by a central authority or agency; that is, planning should be a process with full participation. Norman [26] discusses the different forms of participation and the motivation for their use. Distributed decision making is a framework for information systems support which is suited to the requirements of increased participation.

## Distributed decision making

In terms of system development DDM views organizations as composed of subsystems in mutual interaction. Coordination between tasks is at the level of the task rather than up and down a hierarchy. Coordinating functions are the responsibility of the workers in horizontal groups. When decision making and planning are decentralized, decision support is required at all levels of the organization not just at the top.

DSSs may evolve to support the style of working of those groups. For coordinating functions between groups, these DSSs can be accessed by other groups.

In DDM, the decision-making system is viewed as a network of nodes. Each node is a point in the organization at which some decision-making activity occurs. A node may include DSS and DP systems, with local DP systems and databases feeding the DSSs as shown in Figure 2.

A DDM system provides a flexible association between nodes which can change to meet particular requirements. As patterns of cooperation change between groups the information system must be able to adapt easily. The system recognizes that individuals will have their own values, interests, and ways of working and ensures their independence and autonomy.

The structure of a DDM system allows horizontal association between groups to be built. Information is owned by its producers who control access to data through their software. This is a different approach to a hierarchical structure where subunits provide information which is filtered up the organizational hierarchy and over which they have no control. Pulkkinen [29] has demonstrated the relationships between DSS and the development of organizational structure, communication, and decision making. The DDM model fits most closely with advanced stages of organizational development where the emphasis is on teams and task groups and the potential for DSS use is greatest. A non-hierarchical association between groups is implied, as in a matrix or network organization structure as illustrated by Herbst [15] (see Figure 3). In a matrix structure members may join into different work groups for different tasks. A variety of alternative structures can be formed.

Organizing information systems resources and activities in decentralized environments is more complex than in hierarchical systems, as Zmud [44] discusses. Effective coordination and control without loss of local autonomy may be hard to accomplish. Coordinating and interfacing distributed DSS tools, is also more difficult because of the ad hoc and end user driven nature of DSS development. The distributed nature of a group planning environment means that the management of resources in the system, access to information, and the distribution of control are important issues. The way these issues are handled in a DDM system is considered in the next section.

![](/api/attachments/UCQWWW7A/fulltext/images/ce901fb0abab6e5798fce69d9208545beac892c53c0604ae6721f0eacd3f4f8c.jpg)  
Figure 2. Interaction Between DSSs in a DDM System

![](/api/attachments/UCQWWW7A/fulltext/images/d4432ced1bbec4d1229d6a795298db90d78765e1c9645306fdb23ee4da2590aa.jpg)  
Figure 3. Hierarchical vs Matrix Organizational Structure

## Organization of a DDM System

DDM nodes, comprised of some computing facility supporting a group activity, are loosely coupled into a network in which all nodes are equal and there is no central or controlling node. A node is able to communicate with any other node so all possible pairs of connections are needed, but not simultaneously or permanently. A variety of computer systems may be connected but all have a standard interface to the DDM system. The system is a dynamic one in the sense that new nodes can be added and the structure of the network can change. Nodes are not assumed to share memory and a DDM system may be implemented as a locally distributed system using data transmission facilities such as a local area network.

The DDM system structure is based on operator sharing, and activity is driven by the receipt of messages. DSS operators or application tools at a node are called functions. Where support is given from one node to another a transaction takes place with resources passing between the nodes. Transactions are performed by the execution of a function in a called node. Functions and data are private to a node. It is only by the execution of exportable functions, which have been explicitly defined as usable by other nodes, that internode communication can take place. Agents provide the facility for grouping together transactions to undertake a collection of tasks for the user. Agents can execute local functions at their node and request the execution of external functions. In the case of external function calls the request will be forwarded to the node in question as a message.

A DDM system guarantees user control over data by providing facilities for users to control access to their software and, hence, to data owned by them. The distributed components in a system may already exist and have different communications conventions. The DDM system software provides a framework for accessing distributed DSS components by multiple users. Nodes are responsible for publishing information about how to use DSS operators, and there is no network-wide view of data as in a distributed database system. Resources can only pass out of a node under the control of the owner.

A help function can be called at each node to describe the DDM functions available at that node and how to use them. For example, if the function manpower was registered with the DDM system at the personnel node, the enquiry personnel.help{}, requesting the help function at personnel, would return details of the manpower function plus other functions at that node. The help function, together with an electronic mail facility, must be present at each node in the system. Owner nodes determine which other nodes can access data by specifying access rights.

The detailed model of a DDM system is based on Hewitt's Actor Model in which computations are represented by the passing of messages between actors, that is, the objects being modeled. In a DDM system the basic object is the node. Based on the model, a prototype system has been developed which is a message-based implementation under the UNIX™ operating system. The model and its implementation are described elsewhere [30,32]. Working systems on two machines, a VAX 11/750 and a PDP 11/60, have been used to demonstrate a variety of distributed decision-making applications. Some illustrations of the use of a DDM system to support group planning are described in the following section.

## Applicability of DDM

## Combining distributed DSS operators

In decision making there is often a requirement for combining DSS operations. Operators may be quite simple, providing access to facts, retrieving information such as database queries, or producing data analyses or displays. In a DDM system, tasks may involve data collection and analysis using all parts of the available information system and a wide range of problem solving techniques.

Subunits in a differentiated organization are generally called upon to supply information for use by other subunits in their decision-making activities. In the scheduling case study described earlier, the engineering and maintenance departments needed to incorporate information from each other's plans into their own DSSs. If certain items of information are required regularly, then it may be useful for a DDM node to automate the function so that users can obtain that information directly rather than supplying it via telephone calls, memos, or computer listings. Various local information sources, different DP systems, and DSSs may be drawn upon. In this way nodes may call up functions at an external node to supply information required and incorporate that information into their own decision-making procedure.

In Execucom's planning laboratory sequences of activities could be carried out, for example a series of displays in a planning process. However, a GDSS describes several people cooperating around one DSS; whereas DDM extends this communication to allow interaction between several DSSs. DSSs are extended for multiple use throughout a decision-making community. Users can construct models from distributed components by combining DDM functions in a flexible way to carry out a decision-making activity. Decisions and information can be sent to nodes by requesting exportable functions at the node. The user interface to the DDM system is provided by the agent language (AL) which provides high level control of DSS processes. The language which is defined in [31] contains parallel and sequential function statements, and selection and looping constructs. Exceptions handle cases where function modules cannot be found (or are not available to the calling node), or fail during execution.

## Communication between nodes

A feature identified through the applications surveyed is that DSSs are owned by individual users and groups. At Bechtel, design engineers developed specific tools to assist in their problem-solving tasks using local data. Similarly, in a software development project a small team requires access to common data and programs. In this type of project organization responsibilities are divided between groups which work on their own and then join together for communication when cooperation with other groups is necessary. A DDM system is specifically designed to allow user control over data.

In a case study of research project support, carried out using the prototype system, a project planning function was designed for scheduling team activities and monitoring progress. A system of bar charts is used by the planner, using estimated completion dates for different activities obtained from the programming teams. As work is completed nodes can request a function at the planner node to update the schedule with actual completion dates. The procedure can be initiated by any member requesting their current schedule from the planner. The function generates a questionnaire for reporting progress which is sent to the calling node and executed as shown in Figure 4. Other group planning applications may be developed along the same lines.

In this framework, a user defines a task and there is a series of message exchanges or transactions between participants. Some interactions may be initiated automatically while others require human intervention. Commitments are made and negotiations may take place, perhaps resulting in a redefinition of tasks. In Dzida's system used in the software maintenance environment described earlier, the different types of communication between programmers were supported by means of different message types. In a DDM system, rather than different types of messages, different functions are called for different tasks.

## Idea generation and conferencing

In addition to databases and models, decision makers can use mail or conference information. Decision processes in a group often proceed in an iterative manner, as illustrated by the idea dialogue used in company planning. Another example would be a research problem broadcast simultaneously to a number of individuals in a scientific community for comment. Conferencing systems and DSSs for quantifying and externalizing human judgement tend to be concerned with soft data — opinions, explanations, and non-factual information typically stored in an unstructured format. The handling of assumptions and facilitation of communication about conflicting ideas appear to have much to offer in increasing the understanding of alternatives and encouraging creativity in decision making. By opening questions for examination, including diagnoses of problems and reidentification of objectives, the planning process becomes more open-ended.

<table><tr><td colspan="3"><img src="/api/attachments/UCQWWW7A/fulltext/images/00fba345a87dfa61940a54cc159e351c30f49899e9410d8b0c1c6bb7cc0fdfd4.jpg"/></td></tr><tr><td>man-days</td><td>start</td><td>end</td></tr><tr><td>15</td><td>28/08</td><td>12/09</td></tr><tr><td>Enter progress?</td><td></td><td></td></tr><tr><td>&gt;</td><td></td><td></td></tr><tr><td>:</td><td></td><td></td></tr><tr><td>:</td><td></td><td></td></tr></table>

Figure 4. Gathering Progress Data in Project Planning

The DDM system structure allows electronic mail and conferencing systems to be constructed. Two computer conferencing systems (CCSs) have been implemented in the prototype DDM system. The CONFER system, which allows users to set up a conference on a particular topic and to enter and receive contributions, is based on the command structure of Telecenter [28], a CCS implemented at the International Institute for Applied Systems Analysis in Austria. Unlike the Telecenter system, CONFER keeps a stored record of contributions to a particular conference at its originator node and uses exportable functions at each member node to manage the system.

The second system follows a structured technique called the Nominal Group Technique (NGT) [9], where a decision-making conference, guided by a group leader, proceeds through a number of distinct steps: idea generation, discussion of ideas, preliminary vote on item importance, discussion of preliminary vote, final vote, and report. The goal is to produce a list of ideas on a theme recommended by the group. An important feature of the NGT system is that users are anonymous, thus controversial and unusual ideas may be generated without pressure for conformity. Also, people are less likely to be influenced by the importance of the person making the contribution. In the example in Figure 5 new research and development proposals are being assessed in a plastics manufacturing company in order to choose the projects that will be funded.

Participants need not be in the same room nor be participating simultaneously. Comments can be sent and read whenever convenient. During the discussion of ideas or proposals users may draw on supporting information using DDM functions, perhaps producing statistics or running simulations and making these available to conference participants.

![](/api/attachments/UCQWWW7A/fulltext/images/d20673bb5309502e5b233007abc55126d78ca4a49c5e2b37e5479eb69403f337.jpg)  
Figure 5. NGT Idea Generation

## Conflict resolution

When tasks depend on each other, as they do in scheduling, there is a requirement for decision-making parties to know about each other's decisions. If the decisions are not acceptable, then any conflict must be resolved. For example, in the scheduling case study discussed earlier, if a particular request for a plumber cannot be fulfilled because of illness, then a response giving this information could be provided using a simple function to satisfy most requestors. Where explanations are not detailed, an understanding of the rules used to make the decision may be needed. For this type of situation an expert system might be employed as a conflict resolver [5]. Rules may be used to resolve conflict, and then be applied to resolving future similar conflicts. Such a system developed for resource scheduling has been demonstrated using the prototype DDM system. The DDM system supports conflict resolution by allowing for interaction between DSSs.

## Evolutionary development

Decision-making activities in a particular application will change as the environment changes and new ways of working evolve. Use of the project management DSSs in the scheduling case study, for example, varied according to the working habits of individual project planners. Flexibility of adding, deleting, or changing DSS functions is an important feature of a DDM system. New nodes may also become part of a decision-making system and a node may establish new patterns of coordination with other nodes. A DDM system allows groups to evolve their support software and gives complete flexibility in the number and type of group activities that are present at any one time.

DSS's are designed to support activities where novel, idiosyncratic, and ad hoc methods are required. Thus, they should lend themselves to rapid modification to meet the needs of a particular decision maker in each new situation. This implies end user control and simple means for building models to solve particular decision-making tasks. These two issues are addressed by DDM. In a DDM system users can choose which activities they wish to support and which of the DSS tools they will make available for other users. It is a different concept of systems design from top-down methods. Systems are designed in an evolutionary manner and the services provided are a result of negotiation.

## Conclusion

An important characteristic pointed to in the applications considered is that communication was not organized in a hierarchy but as communication among equals, such as engineers, software developers, scientists and management teams. In some organizational structures, notably cooperatives, this is the natural method of association between groups. In other cases only parts of the organization work as a team; for example, teams of executive managers in Wagner's planning laboratory. A DDM system is structured as a network and provides for the communication of information and coordination and cooperation among decision makers at parallel levels.

A number of distributed decision-making applications in planning and subsystem communication/coordination, were described using a prototype DDM system. In these applications decision making appears as a process of resolution resulting from transactions and conversations between groups with different interests and perspectives. As such, the DMM approach seems to be appropriate both for facilitating participation and cooperation in resource allocation decisions, and allowing individuals and groups to place their own tasks into a cooperative framework. It provides a framework for groups to work in a cooperative manner and the means for involving more people in planning and decision making.

## Acknowledgement

This work was supported by a Science and Engineering Council (UK) research studentship.

## References

[1] Ackoff, R.L. “Resurrecting the Future of Operational Research,” Journal of the

Operational Research Society, Volume 30, Number 3, March 1979, pp. 189-199.

[2] Alter, S.L. Decision Support Systems: Current Practices and Continuing Challenges, Addison-Wesley, Reading, Massachusetts, 1980.

[3] Birrell, A.D., Levin, R., Needham, R.M. and Schroeder, M.D. “Grapevine: An Exercise in Distributed Computing,” Communications of the ACM, Volume 25, Number 4, April 1982, pp. 260-274.

[4] Brooks, F.P. The Mythical Man-Month: Essays on Software Engineering, Addison-Wesley, Reading, Massachusetts, 1975.

[5] Burns, A. “A Rule-Based Approach to Resource Scheduling,” Computer Centre Research Report, CCR.46, University of Bradford, England, 1984.

[6] Cardwell, D.W. “Application of Multipurpose Computer Telecommunications Systems to Atomic Energy Research and Development Facilities,” Online 72 Conference Proceedings, Volume 1, Brunel University, Uxbridge, England, September 4-7, 1972, pp. 129-148.

[7] Cashman, P.M. and Holt, A.W. “A Communication-oriented Approach to Structuring the Software Maintenance Environment,” ACM Software Engineering Notes, Volume 5, Number 1, January 1980, pp. 4-17.

[8] Colley, S. “Holding Back on a Total CAD Policy,” Computing — The Magazine, December 6, 1984, pp. 10-11.

[9] Delbecq, A.L., Van de Ven, A.H. and Gustafson, D.H. Group Techniques for Program Planning, Scott, Foresman and Company, Glenview, Illinois, 1975.

[10] Dzida, W. “Computer Mediated Messaging for Interactive Purposes,” in Computer Message Systems, R.P. Uhlig (ed.), North-Holland, Amsterdam, Holland, 1981, pp. 79-87.

[11] Flores, F. and Ludlow, J.J. “Doing and Speaking in the Office,” in Decision Support Systems: Issues and Challenges, G. Fick and R.H. Sprague (eds.), Pergamon Press, New York, New York, 1980, pp. 95-118.

[12] Goodwin, C. “Restructuring a High Tech Future,” Computing — The Magazine December 6, 1984, pp. 6-8.

[13] Hackathorn, R.D. and Keen, P.G.W. "Organizational Strategies for Personal

Computing in Decision Support Systems," MIS Quarterly, Volume 5, Number 3, September 1981, pp. 21-27.

[14] Henderson, J.C. and Schilling, D.A. "Design and Implementation of Decision Support Systems in the Public Sector, MIS Quarterly, Volume 9, Number 2, June 1985, pp. 157-169.

[15] Herbst, P.G. Alternatives to Hierarchies, Martinus Nijhoff, Leiden, The Netherlands, 1976.

[16] Hiltz, R.S. and Turoff, M. The Network Nation, Addison-Wesley, Reading, Massachusetts, 1978.

[17] Huber, G. “The Nature of Organizational Decision Making and the Design of Decision Support Systems,” MIS Quarterly, Volume 5, Number 2, June 1981, pp. 1-10.

[18] Huber, G. “Issues in the Design of Group Decision Support Systems,” MIS Quarterly, Volume 8, Number 3, September 1984, pp. 195-204.

[19] Johansen, R., Vallee, J. and Spangler, K. Electronic Meetings: Technical Alternatives and Social Choices, Addison-Wesley, Reading, Massachusetts, 1979.

[20] Kidder, T. The Soul of a New Machine, Allen Lane, London, England, 1981.

[21] Kull, D. “Personal Computers Let Engineers Retire Their Old Tools,” Computer Decisions, Volume 16, Number 1, January 1984, pp. 136-145.

[22] Kupperman, R., Wilcox, R. and Smith, H. "Crisis Management: Some Opportunities," Science, Volume 187, Number 4175, February 7, 1975, pp. 404-410.

[23] Meador, C.L. and Mezger, R.A. “Selecting an End User Programming Language for DSS Development,” MIS Quarterly, Volume 8, Number 4, December 1984, pp. 267-281.

[24] Meador, C.L., Guyote, M.J. and Keen, P.G.W. “Setting Priorities for DSS Development,” MIS Quarterly, Volume 8, Number 2, June 1984, pp. 117-130.

[25] Neuhold, E.J. and Rabe, G. “Co-operative Use — Development of Interactive Systems,” Online 72 Conference Proceedings, Volume 1, Brunel University, Ux-Georgia, June 8-10, 1981, pp. 130-140. bridge, England, September 4-7, 1972, pp. 165-185.

[26] Norman, M. “Democratic Systems Design,” in New Information Technology, A. Burns

(ed.), Ellis Horwood, Chichester, England, 1984, pp. 83-107.

[27] Owen, K. “Focus on: Software Engineering,” Alvey News, Issue Number 5, June 1984, pp. 9-11.

[28] Pearson, M.L. and Kulp, J.E. “Creating an Adaptive Computerized Conferencing Systems on Unix,” in Computer Message Systems, R.P. Uhlig (ed.), North-Holland, Amsterdam, Holland, 1981, pp. 129-143.

[29] Pulkkinen, K. “The Premises for Decision Support Systems,” Paper #B-55, Helsinki School of Economics, Helsinki, Finland, 1982.

[30] Rathwell, M.A., Burns, A. and Thomas, R.C. "A Message-Based Model of Distributed Decision-Making Systems," Computer Centre Research Report, CCR.10, University of Bradford, England, 1983.

[31] Rathwell, M.A. and Burns, A., “AL: A Command Language for Distributed Support Systems,” Computer Centre Research Report, CCR.48, University of Bradford, England, 1984.

[32] Rathwell, M.A. and Burns, A. “Distributed Decision Making under UNIX,” EUUG Spring Conference, Nijmegen, Holland, April 16-18, 1984.

[33] Sage, A.P. “Behavioral and Organizational Considerations in the Design of Information Systems and Processes for Planning and Decision Support,” IEEE Transactions on Systems, Man and Cybernetics, Volume SMC-11, Number 9, September 1981, pp. 640-678.

[34] Sandberg, A. “The Demos Project: Democratic Control and Planning in Working Life,” in Working on the Quality of Working Life: Developments in Europe, H. Van Beinum (ed.), Martinus Nijhoff, Boston, Massachusetts, 1979, pp. 291-302.

[35] Sanders, G.L. and Courtney, J.F. “A Field Study of Organizational Factors Influencing DSS Success,” MIS Quarterly, Volume 9, Number 1, March 1985, pp. 77-93.

[36] Scher, J.M. “Distributed Decision Support Systems for Management Organizations,” DSS-81 Transactions, Atlanta,

[37] Schroeder, M.D., Birrell, A.D. and Needham, R.M. “Experience with Grapevine: The Growth of a Distributed System.” ACM Transactions on Computer Systems, Volume

2, Number 1, February 1984, pp. 3-23.

[38] Simmons, W.W. “Planners Look at Planning Again,” Managerial Planning, January/February 1981, pp. 11-12.

[39] Sprague, R.H. and Carlson, E.D. Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, New Jersey, 1982.

[40] Thomas, R.C. and Burns, A. “The Case for Distributed Decision Making System,” Computer Journal, Volume 25, Number 1, February 1982, pp. 147-152.

[41] Turoff, M. and Scher, J. “Computerized Conferencing and its Impact on Engineering Management,” Proceedings of the 23rd Annual Joint Engineering Management Conference, Washington DC, October 1975, pp. 59-70.

[42] Wagner, G.R. “DSS: Dealing with Executive Assumptions in the Office of the Future,” DSS-81 Transactions, Atlanta, Georgia, June 8-10, 1981, pp. 113-121.

[43] Warren, F.E. “The Selection of a Software Development System,” Mini-Micro Software, Volume 6, Number 4, April 1981, pp. 11-17.

[44] Zmud, R.W. “Design Alternatives for Organizing Information Systems Activities,” MIS Quarterly, Volume 8, Number 2, June 1984, pp. 79-93.

## About the Authors

Dr. Alan Burns is a Lecturer in the Postgraduate School of Computing at the University of Bradford (UK). He received his D.Phil. from the University of York (UK) in 1978 and has published widely in a number of areas of computer science including: concurrent programming languages, software engineering, human-computer interfaces, and decision support systems. These interests are combined in one of his present research topics — the design of a distributed multi-user decision support environment. He is editor of the recently published book, New Information Technology (Ellis Horwood, 1984).

Margaret Rathwell received an M.Sc. in Computer Science from the University of Bradford in 1980, and is currently completing her Ph.D. thesis in distributed decision-making systems. She has worked as an analyst/programmer with the automation support group of an international bank and in local government in the United Kingdom.
