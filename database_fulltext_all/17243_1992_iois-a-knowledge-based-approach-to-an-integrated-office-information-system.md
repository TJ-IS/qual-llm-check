---
otero_id: 17243
otero_key: "JDT5B5JT"
title: "IOIS: A knowledge-based approach to an integrated office information system"
authors: "Olivia R. Liu Sheng; Chandra S. Amaravadi; Milam W. Aiken; Jay F. Nunamaker"
year: "1992"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(92)90019-l"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
tems.

# IOIS: A knowledge-based approach to an integrated office information system \*

Olivia R. Liu Sheng,

Chandra S. Amaravadi, Milam W. Aiken and Jay F. Nunamaker, Jr.

University of Arizona, Tucson, AZ, USA

Research on organizational decision making, cooperative work, and relevant technological support such as group decision support systems, model management, artificial intelligence, and expert systems has failed to provide a functional architecture of the integrated, automated office environment which is essential to support knowledge workers in the office of the future. Previous research has been fragmented, focusing only on certain office tasks, or theoretical, lacking the concrete architecture of a working prototype. This paper describes an integrated office information system architecture which uses knowledgebased techniques to assist managerial and clerical workers in a complete spectrum of tasks ranging from group process support to resource management. The use of this system is illustrated with a scenario incorporating typical tasks found in many organizations. Problems encountered in the design and implementation of the system are described, and future research directions are listed.

Keywords: Office automation, Integrated office information systems, Knowledge-based systems, Expert systems.

![](/api/attachments/JDT5B5JT/fulltext/images/a61e46648008fa5b3de14c0ee413e7d8daaa2ea916a2dd0a0cbc1067b0130671.jpg)

Olivia R. Liu Sheng received the B.S. degree from the National Chiao Tung University in Taiwan, R.O.C. in 1981 and the Master's and Ph.D. Degrees in Computers ad Information Systems from the University of Rochester in 1983 and 1986. She is an Assistant Professor of Management Information Systems at University of Arizona since 1985 and a consultant to Toshiba Corporation on database design for medical image data. Her current research interests include analysis and design of distributed database and knowledge systems, pictorial and image data management, automation of systems analysis and design, computer-mediated communication support, distributed group work support, integrating office information systems and manufacturing information system design. Liu Sheng is a member of ACM, IEEE, ORSA and TIMS.

Correspondence to: Olivia R. Liu Sheng; Department of Management Information Systems, College of Business and Public Administration, University of Arizona, Tucson, AZ 85721, USA. Bitnet: sheng @arizmis. Internet: sheng @mis.arizona.edu.

\* This research was supported by a grant from the Army Institute of Research in Management Information, Communications, and Computer Science (AIRMICS), Altanta, GA. Grant No.: DAKF-11-88-C-0021.

## 1. Introduction

Competitive pressures have greatly increased the need for organizations to process information accurately and quickly $[7,15,21,24,44]$ . A major expense associated with this information processing is the cost of knowledge workers – those individuals in an organization who process, interpret, and distribute information. Labor costs for knowledge workers are expected to reach a bil-

![](/api/attachments/JDT5B5JT/fulltext/images/4285ad527081f99c921c9c4b8826bf20ad884563915f9d3564335d1c1f5d4d70.jpg)

![](/api/attachments/JDT5B5JT/fulltext/images/b6439b6fc389d927e2ac43dca7f9c16fb7c73e30383bc98a368819e261ef7054.jpg)

Chandra S. Amaravadi received his ph.D in Management Information Systems from the University of Arizona in 1989. He is interested in the issues surrounding the design and development of third generation office systems including office analyses, knowledge representation, semantic data models and executive support systems. He is currently an assistant professor at Western Illinois University.

Milam W. Aiken received the B.S. degree in Engineering and the Master's of Business Administration degree from the University of Oklahoma and the B.A. degree in Computer Science and the B.S. degree in Business from the State University of New York. He received his Ph.D. in Business Administration with a major in MIS from the University of Arizona, and his research interests include expert systems, office automation, and group decision support sys-

![](/api/attachments/JDT5B5JT/fulltext/images/f6a0f50c0794211e051daec961a761d95dcc44569c6e548b3cc6b0d1f5b2fcd7.jpg)

Jay F. Nunamaker, Jr., is Head of the Department of Management Information Systems and is a Professor of Management Information Systems (MIS) and Computer Science at the University of Arizona. He received a PhD from Case Institute of Technology in systems engineering and operations research. He was an Associate Professor of Computer Science and Industrial Administration at Purdue University. Dr. Nunamaker joined the faculty at the University of Arizona in

1974 to develop the MIS program. He has authored numerous papers on group decision support systems, the automation of software construction, performance evaluation of computer systems, decision support systems for systems analysis and design, and has lectured throughout Europe, Russia, Asia, and South America. Dr. Nunamaker is Chairman of the Association for Computing Machinery (ACM) Curriculum Committee on Information Systems.

lion dollars by the beginning of the next century [35], but commercial information systems have as of yet failed to improve their productivity substantially.

A major focus of concern for improving information systems has centered on the productivity of the office, typically an area of concentration for knowledge workers. The earlier generation of office information systems which included word-processing, spreadsheets, electronic mail, and electronic calendars, supported primarily clerical and professional office workers $[42]$ . It is likely, however; that greater benefits will be gained from supporting managerial workers $[25]$ . These workers have not been as effectively supported by the information revolution since most current office systems are generic (providing many simple functions but little specialized support), lack the capability for customization (increasing the difficulty for implementing specialized support), have a limited focus (not addressing the special needs of managers, for example), and are not well-integrated (hindering the efficient and effective exchange of information) $[11]$ . A final criticism is the scarcity of knowledge-based approaches to integrated office automation systems. Since much office work is ill-structured, it is particularly well-suited to knowledge-based techniques which can replicate expertise and manage information more efficiently $[14,39]$ .

An integrated office information system (IOIS) has been proposed as one possible solution to meet the information requirements of today's office [10]. At a broad level, these requirements can be described in terms of performance, reliability [36], physical and data security [9], flexibility [8,36], interface consistency [43], portability to different office environments [11,31], and integration [8,31]. Few office information systems have incorporated these requirements satisfactorily [23]. This paper presents a knowledge-based architecture of an integrated office information system which addresses these requirements. This integrated office information system provides support for all levels of office workers, but especially meets the needs of managers who are concerned with excessive meeting times, rapid decision making, information overload, management of scarce resources, and monitoring of competitors [13,20,21]. The architecture contributes to an understanding of the functional requirements of integrated office systems and to the potential use of knowledge-based techniques in this domain.

The remainder of this paper presents an overview of the IOIS architecture, a detailed description of the components of the architecture, and the use of the system to manage some typical office tasks. The paper concludes with implications of the architecture and some lessons learned during the construction of the system.

## IOIS CONCEPTUAL FRAMEWORK

![](/api/attachments/JDT5B5JT/fulltext/images/01673de046b80038dc4126192cf43305e326cfeb781b8ae319e58c009fa70e5f.jpg)  
Fig. 1. Four layers of integrated office support.

## 2. Four layers of integrated office support

Since the introduction of office automation, numerous office tools such as E-mail, spreadsheet; calendar- and form-management systems have emerged based on modern software, hardware, and telecommunication technologies. Without integration among these tools, users are required to manually select and set up the access to the appropriate office tool(s) for a given office task. Often, these user choices are inadequate because of users' lack of selection expertise, and the procedure for a user to monitor a task process throughout a number of office tools is therefore tedious and clumsy. For example, a user faced with the task of completing standard office forms may be unaware of the availability of form-management software and will select a more time-consuming word processing solution instead. At other times, the user does not know that the results from one software package are natural inputs to another package. The potential for sharing and coupling of such office resources as software/hardware, knowledge/data, and network devices across time and space is reduced without an integrated office support environment.

The integration support for office environments takes on many dimensions. [4,23,25,26,28, 29,30,33]. Specifically, four layers of integration are essential to bring about totally integrated office environments. As depicted in Figure 1, these layers are arranged in the order of their functionality, with the outer layers being user-oriented and the inner layers being machine-oriented.

Hardware / Network Integration: The considerations for integrating office support usually start with the interconnections of hardware and networking systems, which are typically heterogeneous. For example, integration may be needed to allow both MS DOS- and Unix-based workstations to be used jointly in a task process and to allow Local Area Networks (LANs) to be linked via a gateway with Metropolitan Area Networks (MANs) or Wide Area Networks (WANs) for distributed problem solving using geographically-dispersed resources. To achieve interoperability, such issues as physical connections as well as protocol conversions have to be addressed.

Knowledge Base / Database (KB / DB) Integration: The integration of knowledge bases with databases for office information systems is aimed at the logical integration of knowledge with data employed by a variety of applications to reduce the redundancy, increase the consistency, and expand the scope of data and knowledge. The logical integration of knowledge with data for multiple applications gives rise to such issues as schema integration and query conversion. In a distributed setting, which is typical in office environments, knowledge/data integration for multiple applications is also faced with the challenges to manage the allocation, communication, and co-operative work of distributed data and knowledge components.

Application Integration: Application integration is motivated by the need to utilize multiple application systems for one complex office task and the potential to allow concurrent processing when completing a task. Application integration requires application access entries from one system to another and knowledge/data sharing. It can be accomplished using a tight integration approach of standardizing a global procedure, data format, and interface or a loose integration approach which involves remote procedure calls and common data parameters.

Application Selection / Access Integration: Application selection/access integration provides intelligent choices of applications to use for a given office task and a means to monitor the use and status of applications during the execution of a task. Such support is especially crucial in a large and dynamic office environment where the variety of tasks and applications is large and constantly changing; therefore, the proper use of applications for given tasks becomes increasingly difficult to keep up with. Furthermore, as the need to initiate the use of an application, temporarily interrupt its usage, and return to a previous state becomes more important for high-level office workers, application monitoring is inevitable in integrated office support.

The integration support for each of these layers requires very specific domain expert knowledge. This suggests the need for the adoption of a knowledge-based approach for integrated office information systems. A preliminary prototype of an Integrated Office Information System (IOIS) [23] was developed to illustrate the use of knowledge-based technologies for providing integrated office support. This prototype integrated a number of applications developed by the MIS Department of the University of Arizona and tailored them to the needs of a faculty office. Additional research utilizing this prototype demonstrated the need for an increased focus on tools for collaborative group work, portability to different hardware environments, and an effective methodology for integrating knowledge bases with databases. An enhanced prototype of IOIS incorporating these missing features was tailored for the needs of another target environment – the Army Institute of Research in Management Information, Communications, and Computer Science (AIRMICS). This environment is briefly described in the following section and is more fully described elsewhere [2,3,5,6].

AIRMICS is in some respects an ideal environment for developing and testing an IOIS. The organization's computer terminals and workstations are networked, and the software includes a variety of tools and applications under both MS DOS and Unix operating systems. In addition, AIRMICS is engaged in numerous tasks and procedures found in many typical offices.

## 3. The IOIS target environment

In brief, AIRMICS conducts and sponsors research in very specific areas of information technology. The function of identifying, initiating, monitoring, and evaluating projects is referred to as RDTE (Research Development and Technical Evaluation). AIRMICS conducts internal research and also funds external projects. When initiating a project, the defense database (DTIC) is searched to ensure that the project is unique. If the necessary expertise and human resources to perform the research are not within AIRMICS, the research work is contracted out. If a contractor is needed, some paperwork has to be processed. Then the project is initiated and monitored for progress until it is completed. The outcome of the research is then used as input for making decisions on acquiring future services, developing additional projects, or implementing the completed projects within the Army.

A prototype of the IOIS supports the AIRMICS office in each phase of project management. The support offered by the IOIS includes: coordination support in the form of electronic mail, meeting support in the form of Group Decision Support Systems (GDSS) tools, decision sup-

## IOIS ARCHITECTURE

![](/api/attachments/JDT5B5JT/fulltext/images/aa8dbc5c345a1258520de7564c7c66159a53a9b437d0308f14c6901fa8aa782b.jpg)  
Fig. 2. IOIS architecture.

port in the form of Decision Support Systems (DSS), external information support in the form of environmental information systems, and resource information support through a resource management facility, all embedded in one system. This office support addresses the needs of clerical workers, professionals, and managers.

## 4. Addressing the requirements: The IOIS architecture

Meeting the integration requirements, an architecture of the IOIS has been developed to allow the employment of knowledge-based technologies for integrated office support (Figure 2). The architecture provides a strategy for integrating office systems by coupling an interface, a number of intelligent applications; a shared knowledge base/database, and various generic office tools. The intelligent applications layer for the IOIS architecture contains five major components in accordance with the needs of managers/professionals: a distributed GDSS for collaborative group work, an alternative ranking tool (ART) for use by individuals or groups for evaluating and selecting among alternatives, a resource management expert (RME) for managing resources, an environmental information scanning system (EIS), and an intelligent mail management/mail routing facility (AIMAIL). The Office tools layer includes typical office systems such as a calendar, a word processor, an E-mail system, a spreadsheet, a forms management tool, and DBMS/4 GLs. Integration is provided through the interface as well as through the system's common knowledge base/database. This combination of tools provides support for virtually all aspects of office work including individual and group communication, decision, and clerical support. Although many existing office systems provide a variety of support tools, none presents the degree of integration between individual and group tasks as is supported by this prototype IOIS.

The remainder of this section discusses how these modules were designed, how they were implemented, and how they address the requirements of the target environment. In the tradeoff of design versus a functional description of the prototype, the emphasis will be on the functional description (features) since the technology is a variable factor and a variety of implementations are possible for any given set of functional specifications.

## 4.1. Interface

The interface module of the IOIS provides intelligent user interface functions, a system interface with the applications, and application monitoring capabilities. These functions were implemented via a modular design for maximum flexibility, maintainability, and expandability.

## 4.1.1. Intelligent user interface

The menus for IOIS have been grouped logically so that tasks that are usually performed together appear together in the menus. The menu structure is designed to give users an idea of their location within the system. Pulldown menus are used with new menus overlapping old menus and underlining past choices. When an application is selected and later exited, the user returns to the same place in the menu from which the application was left.

A user profile is obtained from the shared KB/DB to determine what menus are shown to a particular user. System security can be enforced by this means, but other benefits are possible. User experience levels and preferences can determine which applications are normally shown when logging in. The interface for the same application can be tailored to individual preferences and expertise. For example, studies have shown that experts prefer command line interfaces for some applications and menus for others $[22]$ . Novices usually benefit from menu-driven or icon-based interfaces $[16]$ . The IOIS architecture allows menus to be flexibly tailored.

An intelligent application selection facility to aid users in deciding what application is needed for a particular task has also been implemented. This expert selection support takes into consideration factors such as the user's computer proficiency level, the task complexity, and the nature of the task. This is of importance in large organizations having numerous applications (in some corporations; hundreds of applications are available). Furthermore, as new office tools and applications that are better suited for a given task become available, their availability can be readily ought to a user's attention through the system's expert recommendation.

## 1.2. System interface

The system interface provides entries to the embedded office applications. System parameters needed by the individual application are obtained from the user, other application(s), and/or the ared KB/DB. A flexible design is essential to allow easy expandability and portability of the IOIS. The system interface of a generic software development tool such as a window system an expert system shell is possible to provide e platform for the IOIS system interface.

## 1.3. Application monitor

A feature currently under design is a monitoring function that will note when a user does not finish a task involving a particular application. Upon logging into the system again, the user will be reminded of unfinished tasks, and at the user's option, will be automatically returned to that task. The modular design of the overall interface shows this capability to be easily accomplished through a user/problem profile stored in the B/DB and system interface.

## 2. Office applications

Many office applications are possible in an integrated architecture. The IOIS focuses on five ghlevel applications which leverage productivity the office to the fullest: GDSS, AIMAIL, RT, RME, and EIS. GDSS and AIMAIL were elected to facilitate information exchange within e organization, ART was selected to provide ternative selection decision support, RME was elected to ease information monitoring tasks, and EIS was selected to enhance the gathering of formation external to the organization.

## 2.1.GDSS

The GDSS (Group Decision Support System) provides support for generic group problem instigation and solution (a typical task in office environments) through ESP (Expert Sessionanner), ESF (Expert Session Facilitator), and e underlying PLEXSYS tools [1]. The PLEXSYS tools have been implemented in a stand-alone decision room environment. Group collaboration in an office environment, however, has called for the provision of asynchronous and/or distributed group decision support in addition to the traditional synchronous decision room platform of group work support. Expert support for group session planning and facilitation are found to be important for a variety of group session formats.

1. Expert Session Planner: ESP is used by a group coordinator to determine the appropriate group participants and GDSS tools for a particular task. The group coordinator starts ESP with the group selection module to determine the appropriate GDSS session participants. The type of the meeting, the topic of the meeting, personnel interests, responsibilities, and organizational affiliations are all factors used by the knowledge base to search through the rules and user profile database to select participants. Once the group is selected, the tool selection module is used to determine which PLEXSYS tools are necessary for the session. Questions are asked concerning group characteristics such as the familiarity with the topic as well as problem characteristics such as whether or not the problem can be segmented. Once all of the questions are answered, a list of recommended tools and the session time necessary for each tool is written to a file with their accompanying certainty factors. As with the group membership list, the coordinator at this point is free to modify the recommended list of tools to reflect his own preferences. Finally, the calendar/scheduling module is used to automatically schedule the meeting for the participants if the session is face-to-face and synchronous. Once the participant list is determined, this module checks each participant's calendar as well as the meeting room's calendar to arrive at a final time for the session. The AIMAIL module can also be used at this point to disseminate the meeting schedule.

2. Expert Session Faciliator: Once the group and GDSS tools have been determined, and the group has been notified, ESF provides support for a distributed GDSS session. The architecture provides facilities for participant reminders (in case a member is not contributing to the discussion), as well as automatic initiation and termination of extended, distributed electronic meetings.

3. PLEXSYS Tools: The PLEXSYS planning tools support the group's information gathering and decision making activities [1]. This group of tools covers the spectrum from programs that enhance idea generation to those that facilitate organizing and voting on ideas. These tools include Electronic Brainstorming, Issue Analyzer, Automated Delphi, Nominal Group Technique, Issue Organizer, Policy Formation, Vote Selection, Alternative Evaluator. Topic Commenter, Stakeholder Identification and Assumption Surfacing, and Enterprise Analyzer. The planning activities conducted through the PLEXSYS tools can neutralize many of the group effects that have been responsible for poor performance of group meetings in the past [32]. For instance, they can preserve the anonymity of group members and prevent any one group member from dominating the discussion. Empirical evidence has shown that groups using the PLEXSYS tools have been very satisfied with the results and have been able to reduce meeting times by up to 50 percent. Since a considerable amount of the manager's time is spent in planning through group meetings, the PLEXSYS tools provide an excellent medium to support their group communication and decision making activities.

## 4.2.2. AIMAIL

AIMAIL [17,28] is an intelligent message management system superimposed on an existing Electronic Mall System (EMS). AIMAIL deals with the problems of information overload, responding to routine mail messages, enforcement of reporting relationships, and implementation of a dynamic organizational structure. Such a system transcends conventional EMS and will be an invaluable tool for managers.

The system uses knowledge organized in three levels to infer the addressing and handling of messages: the inter-organizational level, intra-organizational level, and individual level. The inter-organizational level contains knowledge about the relationships across organizations. The intra-organizational level is concerned with knowledge about the organization including responsibilities; functions, policies, and reporting relationships, and the individual level of knowledge has within it the mapping of addresses between physical and logical names and also the user profiles. The user profiles will determine how informal messages will be handled.

## 4.2.3. ART

The Alternative Ranking Tool (ART) and its built-in expert system $[27]$ were designed to provide quantitative modeling capability in individual and group decision making situations. Specifically, ART is a spreadsheet-based, user-friendly, and menu-driven tool written in the spreadsheet macro-programming language of LOTUS 1-2-3 version 2.0 for alternative evaluation. According to Simon's decision making theory $[38]$ , alternative evaluation is the stage just before choice and implementation. In the alternative evaluation process, the various alternatives are ranked against a list of criteria. The various alternatives can be shown under one column and the criteria can be shown as column headings of multiple columns. Then the individual decision makers can be asked to rank each alternative against each criterion. Ratings of the alternatives are calculated as a weighted sum of the ranks according to individual criteria. This can be evaluated for each individual decision-maker or a group of participants in a group decision making session, synchronously or asynchronously.

## 4.2.4. RME

The Resource Management Expert (RME) provides assistance to AIRMICS personnel in all activities involving resources (funds/expenses, personnel, equipment, and schedules). The process that AIRMICS goes through to plan, execute, and evaluate research in the areas of interest consists of selecting the projects to be funded, collecting the resource information, allocating resources, and administering contracts. RME consists of two main components: a knowledge-based component for estimating and allocating resources and a database query/update component for viewing and modifying the status of resources.

## Resource Allocation / Estimation

Once a project is selected as a funding candidate, resources (e.g., personnel) are allocated to the project. The allocation component retrieves attributes of the project and the resource from the database. RME invokes the knowledge base and begins reasoning about project and resource attributes to arrive at a match factor (a number between 0 and 1) which is the degree of fit between the project and resource. For each project, the resources and their matching factors are listed in separate windows. A retrospective explanation facility provides a rationale for the matching factor assignment. If the recommended assignment is not accepted for some reason, the final allocation is done manually by either the division chief or the project officer at AIRMICS.

## Resource Status / Update

The Resource Status/Update component is a forms facility, coupled with a database, for obtaining the status of resources and updating new resources. It has been implemented using principles of form management described by Tsichritzis [41]. A number of different templates allow the user to view and update the resource information. For example, expenses are automatically recorded against a project whenever a member of the project team completes an equipment request form or a travel form.

RME would also be used to gather and consolidate project information during meetings. During various stages of a meeting, RME input forms would be accessed by participants and updated. General information would include project names, times, funds needed, and sources of funds.

Table 1
RME input form

<table><tr><td>Project Name</td><td>Approved?</td><td>Awarded?</td><td>Time</td><td>Cost</td><td>Source of Funds</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

A spreadsheet format is used with data appearing in highlighted cells (Table 1).

In Table 1, rows represent separate projects. A function key brings up a second form with more detailed information on the project currently highlighted. Detailed information about the project would include the name of the project manager, review schedules, project descriptions, etc.

The first form will also display information about current projects that have been entered in prior meetings. If the projects are approved, an appropriate box will be checked. Checked projects cannot be modified during a group meeting. RME can be accessed independently from the meeting tools to make the modifications.

## 4.2.5. EIS

Environmental monitoring has become an important managerial activity [21,34]. Some of this information can be obtained from online databases [15]. In the IOIS, environmental information is stored in the form of projects that have been completed in the past.

![](/api/attachments/JDT5B5JT/fulltext/images/7b95432480ce6e62fe954c80cf7d509821d2a0c348f6233a1dd5f40314c9f06e.jpg)  
Fig. 3. The keyword structure.

After a project has been approved for funding, the project manager or other person responsible for preparing an acquisition package accesses EIS (outside of the GDSS setting) to retrieve information on related projects that are in progress or have been completed in the past. Two sources of information are available. One is the DTIC database, and the other is the local AIRMICS database containing information on past AIRMICS projects. In either case, a keyword help facility provides information on related words that could be used for database queries. Keywords can be browsed alphabetically or by relationships between words. A complex tree structure allowing multiple parents and children is used to map the relationships between keywords. Part of this structure is reproduced in Figure 3.

Keywords can be browsed from the top level of the tree downward or from any known starting point within the tree (the starting keyword will be typed in from a prompt in this case). Keywords at each level are displayed in popup menus consistent with the IOIS main menu. The tree can be searched upward or downward by selecting any of the keywords listed in the popup menu. After finding the related keywords, the system can automatically generate a query to the DTIC database for information, or the user can choose to manually create or modify the query. Project information is returned in the format previously used when choosing projects.

## 4.3. KB / DB

A major part of the integration of IOIS has been achieved by a logical integration of the knowledge base/database (KB/DB). An integrated KB/DB speeds up application development since new applications can take advantage of components within the KB/DB that have already been developed and implemented. Knowledge common to all office applications, e.g. the structural knowledge and general office knowledge, can be isolated and maintained independently. Changes to the schema or knowledge may be made quickly, as it is easier to assess its effects in a shared environment than in a fragmented environment. Lastly, duplication of any part of the KB/DB can be reduced.

![](/api/attachments/JDT5B5JT/fulltext/images/9a8390c9d175fe7aec18888702d11ec28010033b8ada3655a0a1d5de120c79b1.jpg)  
Fig. 4. The knowledge base/database.

Table 2  
An example schema used for IOIS DB.

<table><tr><td>Fund No.</td><td>Source</td><td>Description</td><td>Date of Expiry</td><td>Amount Spent</td><td>Balance</td></tr><tr><td>DY-10-07</td><td>AIRMICS</td><td>Operations</td><td>6-15-89</td><td>$80,000</td><td>$60,000</td></tr></table>

The database contains records of entities that are relevant to the RDTE process, such as projects, personnel, contractors, funds, schedules, reports, forms, equipment, etc. For illustrative purposes, a sample schema for the entity “funds” is reproduced in Table 2 with some fictitious data.

The knowledge representation used for the IOIS is somewhat different from that used in traditional systems such as MYCIN [37]. The representation uses both a rule base to encode the reasoning required for the applications and a class-object structure for describing static relationships [18,19]. IOIS applications make use of the class-object structure to describe parent-child relationships as in EIS, to describe GDSS tool attributes (in ESP), to describe properties of personnel and projects (in RME), and so on. So far, little overlap in knowledge exists between applications; therefore, the rule base is a collection of rule bases, each of which executes the inferencing needed for a particular application. The details of the knowledge base/database are shown in Figure 4.

The class-object structure is coupled with the knowledge base and database (Figure 5). Records from a database are retrieved under control of an inference engine through special rules. Each record instantiates the object to which it is linked. Figure 5 shows the linkage for RME. The inference engine retrieves a personnel record and a project record and instantiates the property values of the corresponding objects. The inference engine uses these values to inference on rules. For the example, the output of the inferencing is a match factor describing the degree of fit between the project and the person. The instantiation of objects is similar to SQL queries under a host programming language, using “cursors.” Experience with the prototype has showed this to be a suitable approach when reasoning with static facts.

## 4.4. Summary and implementation status

Recapping, the IOIS architecture incorporates effective software engineering and knowledgebased principles to provide integrated support for multi-level and multi-user office tasks. The architecture offers a number of advantages, including:

![](/api/attachments/JDT5B5JT/fulltext/images/0df66d5b85392e9699aca9ee7def6e61039a22f575532f997e4a39160698fdd0.jpg)  
Fig. 5. KB-DB, Class-object, and rule-object linkages.

\- Uniform system entries,

\- Easy security control for multiple levels of users,

\- Smooth expandability,

\- Distributed and parallel problem solving,

\- Data/knowledge sharing by multiple users across multiple applications,

\- Intelligent application selection support,

\- Intelligent application monitoring support,

\- High level managerial task support.

Although the architecture was designed for a distributed, heterogeneous, and multi-user environment, the initial prototype implementation has focused on a homogeneous PC microcomputer operating environment. A prototype of IOIS capable of the major functions included in the architecture has been developed in an MS DOS environment. A variety of software packages such as an expert system shell (Nexpert Object), a DBMS (DBase III + ), windowing system (Windows for C and Vermont Views), and programming languages (Microsoft C and Turbo Pascal) have provided the primary development environment. The next section presents a scenario to demonstrate the functionality of the IOIS prototype and its usefulness in the AIRMICS context.

## 5. A scenario illustrating the use of IOIS

The tasks to be supported within IOIS can be divided into two general categories: (1) Planning for Projects, and (2) Initiating and Monitoring projects. The technologies to be used for these tasks can be subdivided into four general categories: (1) GDSS (Group Decision Support System) and DSS for generic group and individual problem investigation and solution, (2) RME (Resource Management Expert) and EIS (Environmental Information Scanning) for office resource and project management, (3) AIMAIL for knowledgebased communication support, and (4) various commercial software tools (Office Tools) which support simple tasks (Figure 6). The tasks handled in the process of project management and the IOIS prototype features employed for the support of task completion are depicted in Figures 7, 8, and 9. The manner in which the IOIS supports the tasks is described in this section.

![](/api/attachments/JDT5B5JT/fulltext/images/f6fbbefa6aa034ccccd6428afeecd0516d51a70d03c3356c3d128467278fc190.jpg)  
Fig. 6. The IOIS menu structure.

1. The process starts with receiving a pre-proposal from the contractor (Figure 7). A review officer is assigned to the project proposed by the contractor. At this stage, the personnel allocation model in the RME could be used to make the assignment by a single (final) decision-maker. The RME makes use of the requirements of the project and the

![](/api/attachments/JDT5B5JT/fulltext/images/e3aef57b59380e435b187d9ce66e34423321ff175a512701d8915a02059d9e21.jpg)  
Fig. 7. An AIRMICS scenario using the IOIS: preproposal screening.

availability and expertise of the researchers to recommend a suitable project officer. If a group of people are involved in making the assignment, then the GDSS functions can be invoked to set up a group session (synchronous or asynchronous) and conduct the session to arrive at an assignment.

2. The proposal is reviewed internally by the

![](/api/attachments/JDT5B5JT/fulltext/images/85b40333633682061e933f6319f6fb389899ee3f251884e8b2e0296f3656ccb1.jpg)  
Fig. 8. An AIRMICS scenario using the IOIS: Formal proposal review.

director, division chiefs, and the assigned review officer to determine whether or not it is consistent with the AIRMICS RDTE plan. It goes through an alternative evlation stage using ART either in a DSS by an individual or in a GDSS by a group of decision-makers.

![](/api/attachments/JDT5B5JT/fulltext/images/ce3db9dcb356fab33d5aa974103ba939c7e688ae14d8bba3b79378c514d5123f.jpg)  
ig. 9. An AIRMICS scenario using the IOIS: Project initiation and monitoring.

If the group form is assumed, a group ART session (face-to-face or distributed and synchronous or asynchronous) will be planned using ESP and facilitated using ESF. If the pre-proposal is rejected, a letter is sent to the contractor proposing the project. The IOIS architecture provides access to Office Tools, and a word processor can be used to prepare and send the rejection letter.

3. If a pre-proposal passes the internal review, it is subjected to more evaluations. But at this stage, AIRMICS also attempts to solicit external sponsorship for the project. Regardless of the communication means (mail, E-mail or, phone) that are used to contact the potential candidates for funding the project, the intelligent dissemination function of AIMAIL can be employed on-line or off-line to identify potential funding sources. Criteria such as the interests of each funding organization, current projects in progress, the project scope, and resource requirements are used in this decision. The pre-proposal is then sent out to these external organizations for review.

4. If there is no external interest for the project, then a rejection letter is sent again to the contractor, but since the project was already found to be consistent with AIRMICS' objectives; it is retained as a pending internal project in the KB/DB using the RME. As in the internal decision process, the Office Tools (word processor) can be used for sending the rejection letter. If there was external interest for the project, the contractor is asked to submit a formal proposal, including budgets, deliverables, etc. Again, an AIMAIL or a regular mail message written with a word processor could be used for communicating this information.

5. When a formal proposal is received from the contractor (Figure 8), it is subjected to another internal review and another external review. Similar to the pre-proposal screening process, DSS, GDSS, and AIMAIL are the typical IOIS support applications useful in this stage. Again, the outcome of these decisions may be to reject the project (a rejection letter is sent out with the help of Office Tools) or to move the proposal further in the review process.

6. At this stage, resource requirements of the project are assessed with RME. It makes use of the knowledge base to estimate costs for the project. The knowledge base contains heuristics from previous projects, such as the time it takes to develop communications software or the time it takes to analyze a potential system.

7. A final high level meeting takes place involving the director of AIRMICS and other high level personnel to make funding decisions. The Expert Session Planner (ESP) of GDSS enables the project officer to plan the meeting in terms of selecting the group participants (based on organizational knowledge), selecting the GDSS tools (based on tool knowledge), and determining the time of the meeting (based on participants' calendars). After determining the meeting participants with the help of ESP, mail messages announcing the meeting can be sent automatically via AIMAIL. The Voting tools of PLEXSYS are used in the funding meeting to vote on the ultimate fate of the project. If approved, the project's status is updated using RME, triggering other activity relating to monitoring the project.

8. Once a project is finally approved, the review officer prepares an acquisition package to acquire the services of the contractor (Figure 9). Two tasks are supported in preparing the acquisition package: searches of databases for historical project information and completing the forms associated with the acquisition package. The review officer accesses the EIS to retrieve information on related projects that are in progress or have been completed in the past. Two sources of information are available. One is the Defense Technology Information Center (DTIC) database. The other is the local AIRMICS database containing information on past AIRMICS projects. In either case, a keyword help facility will provide information on related words that could be used for database queries. After finding the related keywords, the system can automatically query the local AIRMICS database for information, or the user can choose to manually create the query. DTIC queries are similar. Support for completing the Broad Agency Announcement forms online is provided. Some of the fields in the ms are automatically filled from information contained in the database (such as the ision, addresses, etc.).

ter the package is prepared, it is forwarded
the contracting officer at Ft. McPherson.
e contracting officer conducts a financial
alysis of the contract and either approves it
suggests changes. If there are any changes,
y are made by the Contractor and coordi-
ed by the review officer. The project is
n formally awarded. RME should be used
update project status. After the acquisition
kage is processed, personnel and equip-
nt are formally allocated to projects using
1E. Personnel allocation is used for assign-

contracting officers (CORs) and re-
rchers to projects. This tool invokes a
wledge base to determine the degree of
between the project and the personnel.

ce a project is under way, it is monitored marily by the COR and the division chief. The COR may travel to the site of the conctor (in which case it may be necessary to nplete some paperwork). The purpose of COR's visit is to assess the progress of project and to recommend or approve changes if necessary. RME provides sup-t for reminding the COR of the project view schedule and for completing the pa-work. After the COR finishes the review, uses the office tools to complete his trip port. Also, when a project is in progress, I especially for internal projects, the COR periodically updates and checks the resource tus to make sure that the usage is in line h the budget.

then the project terminates, a final In Pro-s Review (IPR) is conducted. The director, division chief, the COR, and any inter-ed party within AIRMICS participate in review. The meeting participants, the tools required, and the meeting times are all nned with ESP and meeting scheduler and nounced by AIMAIL. After the final IPR, COR updates the DTIC database and forms some additional internal procedures terminate the contract.

section illustrated one possible scenario complex project management tasks involving of the IOIS prototype. Tle IOIS architecture is flexible enough to provide integrated office support in the manner a user prefers. The project management tasks described in this section represent a wide variety of office activities that take place in intra- and inter-organizational settings, demonstrating the capacity of the IOIS architecture for supporting a broad range of office operations. Although the prototype has not been installed for day-to-day usage, it is expected that the integration of a number of applications under the generic architecture will be able to increase the effectiveness and productivity of office functions.

## 6. Conclusions

To meet the increasing pressure for effective and efficient office operations, computer-based office support must be integrated through application selection and access, data and knowledge sharing, and heterogeneous computing resources. An integrated office information system (IOIS) has been developed to incorporate knowledge-based techniques for providing intelligent and integrated support for office activities in an interconnected office environment. This system represents one of the first efforts to take into consideration the need for supporting distributed problem solving and cooperative work in offices. In addition, the prototype is perhaps the only existing system which provides integrated support throughout all aspects of office work: from clerical to managerial, from individual to group, from synchronous to asynchronous, and from centralized to distributed.

The architecture of the IOIS, which couples an interface module, a collection of intelligent and office applications, and a shared knowledge base/database, offers easy expandability, portability, and flexibility. These are important properties of office systems, as organizations continue to be impacted by fast-developing technologies in computer, telecommunication, and management information systems.

From an organizational perspective, the application of the architecture can have three potential benefits. First, the tools provide a powerful environment for managers to explore the technology and identify the scope for new systems [40]. Second, the ready availability of powerful office systems would enable them to develop new models of thinking about their organizations [12]. Lastly, the use of technology by management would encourage other end users to be more adventurous and identify more uses for it.

Two prototype developments of the IOIS have been completed in an MS DOS development environment. A scenario of project management tasks has been described to demonstrate the usefulness of the IOIS. The collections of application systems embedded in the IOIS system provide support for a complete spectrum of tasks with emphasis on a manager's activities. The GDSS module supports the group decision-making functions which may account for almost two-thirds of the manager's time. Similarly, AIMAIL supports the mail management tasks of managers, using heuristics that would be used by a secretary to process incoming and outgoing mail messages. RME supports resource monitoring and scheduling functions, and EIS supports environmental monitoring.

The main goal in the early stages of prototype implementation is to explore implementation considerations and demonstrate the principal concepts of the architecture's design. The development of the current prototype has given us sufficient assurance of the effectiveness of the IOIS architecture, and we are extending the implementation to handle distributed and heterogeneous computing resources in MS DOS and Unix environments. This phase will be able to feed back design insight into distributed problem solving schemes, distributed knowledge/data sharing, and system interface design for heterogeneous computing systems. In addition, efforts will be focused on enhancing the group support capabilities of the system, since the automated support of collaborative group work continues to be a fertile field of study. When these extensions are completed, a prototype working under distributed and heterogeneous MS-DOS and Unix operating environments will be installed for daily usage. The effectiveness of this integrated office information system in improving office productivity will then be evaluated through field studies.

As the number of office information systems used to handle office tasks grows rapidly, integration of these systems is essential to provide efficient and effective support through data/knowledge sharing, distributed problem solving, and cooperative work. This paper describes an initial effort toward integrated office information systems. Continued research is needed to bring about integrated support for offices of the future.

## Acknowledgements

The authors wish to thank Major Ted Hengst and Dr. Jim Gantt of AIRMICS Atlanta for supplying information about the AIRMICS office environment. The authors also wish to thank Dr. Kunihiko Higa, Dr. Luvai Motiwalla, Dr. Minder Chen, Charles M. Morrison, and Debabrata Mishra for their contributions to this project.

## References

[1] PLEXSYS User Guide, 1987, Department of MIS, The University of Arizona.

[2] Software Engineering Research Center, “An Information Systems Plan for the Army Institute for Research in Management Information, Communications, and Computer Science,” Internal Report, Georgia Institute of Technology, Atlanta, Georgia, June 1988.

[3] Software Engineering Research Center, “Information Systems Analysis for the Army Institute for Research in Management Information, Communications, and Computer Science,” Internal Report, Georgia Institute of Technology, Atlanta, Georgia, June 1988.

[4] Aguilar, Joseph Francis, “Scanning the Business Environment,” The Macmillan Company: New York, 1967.

[5] Aiello, L., Nardi, D., and Panti M., “Modeling the Office Structure: A First Step Towards the Office Expert System,” ACM SIGOA Conference, 1984, pp. 25–32.

[6] Amaravadi, Chandra, “Towards a Conceptual Model for the Office: An Integrating Approach,” Ph.D dissertation, University of Arizona, Tucson, 1989.

[7] Becker, Hal B., “Can Users Really Absorb Data at Today’s Rates?, Tomorrow’s ?” Data Communications, July 1986. pp. 177–193.

[8] Bracchi, Giampio and Pernici, Barbara, “The Design Requirements of Office Systems,” ACM Transactions on Office Information Systems, Vol. 2, No. 2, April 1984, pp. 151–170.

[9] Bracker, Lynne C. and Konsynski, Benn R., “Office Automation – A Model for Design,” Computer Networks, 1980. pp. 173–177.

[10] Bullen, Christine V. and Bennett, John L., “Requirements for Office Tools Used by Administrative Managers and Professionals,” ICIS Conference Proceedings, 1983, pp. 69–83.

[11] Croft, Bruce W. and Leffowitz, Lawrence S., “Task Support in an Office System,” ACM Transactions on Office Information Systems, July 1984, pp. 197–212.

[12] Dhar, Vasanth, “On the Plausibility and Scope of Expert

Systems in Management," Journal of Management Information Systems, Summer 1987, pp. 25–41.

3] Dickson, Gary W., "Key Information Systems Issues for the 1980's," MIS Quarterly, September 1984, pp. 135-147.

4] Fikes, Robert E. and Henderson, Austin D., "On Supporting the Use of Procedures in Office Work," Proceedings of the AAAI, August 1980, pp. 202–207.

5] Fujitani, Larry, "Laser Optical Disk: The Coming Revolution in On-line Storage," Communications of the ACM, June 1984, pp. 546–554.

6] Hammer, M., Kunin, J., and Schoichet, S., “What Makes a Good User Interface?,” Proceedings of Office Automation Conference, Philadelphia, PA, February 1983, pp. 121–130.

7] Higa, K. and Liu Sheng, O.R., “Intelligent Database Development: An AIMAIL Example,” in Expert Systems and Advanced Data Processing, 1988, pp. 128–139.

8] Higa, K. and Liu Sheng, O.R., "An Object-Oriented Methodology for End-User Logical Database Design: A Structured Entity Model Approach," Proceedings of IEEE International Compsac, pp. 365–374, 1989.

9] Higa, K. and Liu Sheng, O.R., “An Object-Oriented Methodology for Databases/Knowledgebase Coupling: An Implementation of the Structured Entity Model in Nexpert System,” Data Base, Vol. 20, No. 1, pp. 24–29, 1989.

0] Hiltz, Roxanne and Turoff, Murray, “Structuring Computer-Mediated Communication Systems to Avoid Information Overload,” Communications of the ACM, July 1985, pp. 680–689.

1] Huber, George P., “The Nature and Design of Post Industrial Organizations,” Management Science, August 1984, pp. 928–951.

2] Jagodzinski, A.P., “A Theoretical Basis for the Representation of On-Line Computer Systems to Naive Users,” International Journal of Man-Machine Studies, Vol. 18, 1953, pp. 215–252.

3] Liu Sheng, O., Motiwallia, M., Nunamaker, J., and Vogel, D., “A Framework to Support Managerial Activities Using Office Information Systems,” Journal of Management Information Systems, Vol. 6, No. 3, pp. 45–63, 1989.

4] Masuda, Yoneji, “The Information Society,” The World Future Society, 1980.

5] McLeod, R. and Jones, J.W., "A Framework for Office Automation," MIS Quarterly, March 1987, pp. 87–104.

6] Mintzberg, H., The Nature of Managerial Work, Prentice Hall, NJ, 1973.

7] Mishra, Debabrata, "An Alternative Ranking Tool," Masters Project Report, University of Arizona, 1989.

8] Motiwalla, L., Higa, K., Liu Sheng, O., and Nunamaker, J., “A Knowledge-Based Mail System to Support Managerial Activities,” Proceedings of the Twenty-Second Annual Hawaii International Conference on System Sciences, Kailua-Kona, Hawaii, January 3–6, pp. 650–659, 1989.

[29] Naffah, N., “Integrated Office Systems Protocols,” Integrated Office Systems, North Holland, 1980, pp. 13–25.

[30] Naffah, N., White, G., and Gibbs, S., “Design Issues of an Intelligent Workstation for the Office,” Proceedings of the National Computer Conference, AFIPS, 1986.

[31] Notkin, D., Hutchinson, N., Sanislo, J., and Shwartz, M., "Heterogenous Computing Environments: Report on the ACM SIGOPS Workshop on Accomodating Heterogellicity," Communications of the ACM, February 1987, Vol. 30, No. 2, pp. 132–140.

[32] Nunamaker, J.F., Applegate, L.M., and Konsynski, B.R., "Facilitating Group Creativity: Experience with a GDSS," Journal of Management Information Systems, Spring 1987, pp. 5–19.

[33] Nunamaker, Jay F., Amaravadi, Chandra S., Motiwalla, Luvai F., “OSA: An Office Systems Architecture for Supporting Managerial Activities,” U.S. Army Information Systems Engineering Command’s Technology Strategies Conference, February 1988.

[34] El Sawy, Omar A., “Personal Information Systems for Strategic Scanning in Turbulent Environments: Can the CEO Go On-Line?”, MIS Quarterly, March 1985, pp. 53–60.

[35] Poppel, Harvey L., “Who Needs the Office of the Future?,” Harvard Business Review, November-December 1982, pp. 146–155.

[36] Sasso, William C., Olson, Judith Reitman, and Merten, Alan G., “The Practice of Office Analysis: Objectives, Obstacles, and Opportunities,” IEEE Technical Committee on Office Automation Newsletter, May 1987, Vol. 1, No. 2, pp. 11–24.

[37] Shorttiffe, E.H., Buchanan, B.G., Merigan, T.C., and Cohen, S.N., “An Artificial Intelligence Program to Advise Physicians Regarding Antimicrobial Therapy,” Computers and Biomedical Research, Vol. 6, 1973, pp. 544–560.

[38] Simon, H., The New Science of Management Decision, Harper and Row, New York, New York, 1960.

[39] Suchman, Lucy A., "Office Procedure as Practical Action: Models of Work and System Design," ACM Transactions on Office Information Systems, Vol. 1, No. 4, October 1983.

[40] Sviokla, John J., “Business Implications of Knowledge-Based Systems,” Data Base, Summer 1986.

[41] Tsichritzis, D., “Form Management,” Communications of the ACM, Vol. 25, No. 7, July 1982, pp. 453–478.

[42] Tsichritzis, Dennis, “Office Automation Tools,” in Managers, Micros and Mainframes edited by M. Jarke, John Wiley and Sons, 1986, pp. 11–20.

[43] Uhlig, R., Farber, D., and Bair. J., “The Office of The Future,” Vol. 1, 1979, North Holland.

[44] Vallee, Jacques, The Network Revolution, AND/OR Press, Berkeley, CA, 1982.
