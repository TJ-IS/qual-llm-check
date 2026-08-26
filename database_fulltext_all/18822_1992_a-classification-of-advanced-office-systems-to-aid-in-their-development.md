---
otero_id: 18822
otero_key: "PYQTTUWA"
title: "A classification of advanced office systems to aid in their development"
authors: "James Ang"
year: "1992"
journal: "Information & Management"
doi: "10.1016/0378-7206(92)90036-f"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# A classification of advanced office systems to aid in their development

James Ang

National University of Singapore, Singapore

Existing classifications of office systems are unidimensional: they normally use the level of task support as the only distinguishing factor. Bracchi and Pernici, however, use the systems' underlying conceptual framework as the delineation parameter. Building on previous work, we develop a classification of office systems using both the level of support and the underlying conceptual framework as discriminating dimensions.

Keywords: AI concepts, Data semantics, Object-oriented, Office systems, Process semantics

![](/api/attachments/PYQTTUWA/fulltext/images/19f4d86eb42c309d61b2d8be239bea0f7f6466cb9130560378e7bae5e2cc4bf3.jpg)

James Ang is a senior lecturer in the Department of Decision Sciences, National University of Singapore. He holds the B.Sc. degree (Mathematics) from the University of Singapore, and the M.A.Sc. and Ph.D. degrees (Management Sciences) from the University of Waterloo, Canada. His research interests include systems modeling and design using Petri nets and object-oriented formalism, applications of speech act theory, and information systems planning within the broader context of corporate objectives.
Correspondence to: J. Ang, Department of Decision Sciences, National University of Singapore, 10 Kent Ridge Crescent, Singapore 0511. Fax: (65) 772-1296, Bitnet: FBA ANGSK@NUSVM.

## 1. Introduction

Offices are information processing centers $[17,18,27,28,58,65]$ . This information processing perspective has led system analysts to focus on designing and building systems that will enhance information flow and facilitate information interpretation as a means of enhancing organizational efficiency and effectiveness. New computer-based concepts have enabled many very advanced office systems to be developed taking advantage of these technologies.

A rigorous classification of these office systems along some meaningful dimensions will be helpful to system analysts – to serve as a guide for them to develop new office systems that would best serve organizational needs. If the system to be developed is one where a concurrency control access mechanism is an essential feature, then a system based on the object-oriented paradigm is appropriate $[71,74]$ . On the other hand, if the system is intended to enhance the efficiency of a self-contained cluster of activities, then a system based on some database language would be more efficient.

Most classifications reported in the literature are unidimensional using only level of task integration (or task support) as the discriminating factor [e.g., 55,69]. However, Bracchi and Pernici [10] classify office systems using the systems' underlying conceptual framework as the delineation parameter. Their four classes are: data-based, process-based, agent-based and mixed. Data-based systems [e.g., 37,42] use data types and their operations (e.g., storage, retrieval, manipulation, transmission) to group information and route it by means of forms. Process-based systems focus on the representation of concurrent activities in order to provide automation of office work [e.g., 24,75,76]. Essentially, these systems use the theoretical constructs of formal languages such as Petri nets $[52,54]$ . Agent-based systems [e.g., 35] handle office work by associating agents with a set of functions. Data and activities are built into the systems if they are pertinent to the functions associated with the agents. Mixed systems use more than one of these bases as the framework for system specification.

Among those using the level of support as the distinguishing factor, Ho et al's classification is the most explicit; we will use their classification for office systems using level of support as the distinguishing feature. They have three categories. Level 1 systems mechanize activity processing to cope with speed requirement by using individually mechanized facilities [25,41]. Level 2 systems emphasize integrating various office activities to accomplish office objectives. Some examples are office procedure automation software and man-machine interfacing. The main purpose here is to eliminate unnecessary, error-prone human intervention and to lessen the time-consuming transfer of office workers from one kind of facility to another [49]. Level 3 systems support office management. They are intended to provide sufficient and appropriate information to facilitate decision making, policy making, monitoring of work quality and so forth. The main purpose is to develop an office information system capable of gathering information from various sources, analyzing it and providing some suggestions to assist office managers in managing their offices. In fact, most textbook classifications categorize office systems into transaction processing systems, management information systems and decision support systems. These classes correspond somewhat crudely to Ho et al's levels 1, 2 and 3, respectively. We characterize existing office systems along two dimensions: (1) The underlying conceptual framework and (2) The level of task integration.

## 1.1 Classification by conceptual framework

Systems can be developed using data semantics, process semantics, or AI (and/or object-oriented) concepts as the fundamental conceptual framework. Data semantics systems correspond to data-based systems, while process semantics systems correspond to process-based systems. We substitute agent-based systems with knowledgebased systems, since the active elements of agent-based systems can be modeled with objects or other equivalent constructs, such as Tueni et al's [64] MOPA (Memory Organization Packet for Activities). Of course, many systems (e.g., Lochovsky et al's [44] OTM) incorporate data semantics, process semantics and AI (and/or object-oriented) concepts. However, for a particular system, it is possible to ascertain which category constitutes the underlying theoretical underpinning. As such, the mixed systems can be classified according to the underlying conceptual framework.

## 1.2. Classification by level of task integration

Two levels of task integration can be distinguished. There are systems which exist for the purpose of enhancing the efficiency of specific office activities or procedures. These systems correspond level 1 systems. At a higher level are systems that support task integration: these are level 2 systems. Essentially, they integrate or support office activities in order to achieve certain goals. In Ho et al's classification, level 2 systems are aimed at procedural synchronization, while level 3 systems are those designed for management support. We do not see the need to have more than two levels and collapse these onto one. Our distinguishing characteristic is: Are systems designed to speed up information processing by using individually mechanized facilities, or are they designed for task integration? We therefore have fewer, but well-defined, classes.

## 2. Typology of office systems

## 2.1. Data semantics systems (classification of example modern systems by level of integration)

Systems that are anchored on data semantics focus primarily on the expressive power of a database language to group data using forms as the interface. Though a database is a central component of these systems, other components, such as triggers, queries, and constraints are also needed. Office activities are then seen as a series of operations on data. An example is Zloof's [77] Office-By-Example (OBE). OBE is an extension of his query language for relational databases (Query-By-Example) and of the System for Business Automation (SBA) [78]. QBE provides a means of automating simple procedures related to data, including sending messages based on data transformations or data-related triggers. The system provides a convenient interface for specifying simple algorithmic tasks such as transmitting messages when the requisite conditions obtain. Attardi and Simi [5] and Gibbs and Tsichritzis [30] incorporated data semantics and pure procedures into their systems. In both of these, procedures are strictly confined to individual workstations; no capability for activity coordination among workstations exists. Each system is functionally independent and users cannot interact with one another within a larger work context. VAGUE [48] extends the expressive power of relational database by incorporating data metrics, which are definitions of distances between values of the same domain, to help users handle intrinsically vague queries directly. These are level 1 systems. Other level 1, data semantics systems are Ladd and Tschiritzis 's Office Form Model [42], Chang and Chang's Alters [11] and IBM's Top View [38].

Subsequent refinements of Zloof's OBE by Whang et al propose to integrate heterogeneous features (e.g., database tables, word processing, electronic mail, menus, forms, graphics and images) through a language feature called “example elements.” The database manager constitutes the backbone of this system (a level 2 system) by providing powerful computational capabilities, a feature that is necessary for complex office applications. The system permits different applications to exchange information by using “the full expressive power of the database language supported by the database management system.”

Watters and Shepherd [67] develop a prototype browsing interface (a level 2 system) for access to the New Oxford English Dictionary. The system allows users to browse and query data instances with considerable ease and is based on hypergraph-representation of data instances.

Data semantics systems that support task integration (level 2 systems) usually do so through a database management system or simple common data structures. Examples of such systems are IBM's DISOSS [36], PROFS [37], Xerox's Star [56], Lotus 1-2-3 [45] and Lotus's Symphony [46].

## 2.2. Process semantics systems (classification of example modern systems by level of integration)

Systems that use process semantics are those that specify an office procedure using a finite set of atomic actions (or input alphabet) and a set of concatenations of these atomic actions (words of a language). An example is Zisman's SCOOP. It seeks to automate specific procedures using the graphic language of Petri nets. An activity (or a transition) is executed once its preconditions are satisfied. A procedure is a concatenation of activities and conditions in juxtaposition. The system emphasizes automation of specific procedures rather than assistance to the office worker. Ellis's Information Control Net (ICN) is another example. Using ICNs, we can describe office activities that make up an office procedure. The concept of modularity, which is one of the important features of ICNs, permits us to represent each activity as an ICN. Conflict and parallelism are depicted by "or" and "and" symbols, respectively. Another advantage of ICNs is that they distinguish between data flows and control flows. The simplicity of ICNs is an important asset. Both SCOOP and ICN are level 1 systems since they do not incorporate a mechanism for task integration

van Biljon [66] uses Petri nets to specify user interfaces, calling them man-machine dialogues. Sttots and Furata [62] develop a prototype hyertext browsing and authoring system using Petri nets. These are level 2 systems since they are interactive and support task integration.

We can also classify systems developed using linguistic units $[9,15,70]$ as process semantics systems. Basically, these systems model organizational processes as concatenations of speech acts or other meaningful linguistic units. Each linguistic act is similar to an atomic action. Systems having this theoretical orientation are The Coordinator $[26]$ , CHAOS $[19,20,21]$ and COSMOS. These systems are interactive in nature and permit a high level of task integration. They are level 2 systems. For example, The Coordinator is a system for supporting the network of organizational interactions using various linguistic actions as basic building blocks. A conversation is then a concatenation of primitive linguistic units or actions. Though such a system is one for conducting conversations for actions, it also provides facilities for other types of conversations, such as those for possibilities and requests for information.

## 2.3. Knowledge-based systems [including object-oriented systems] (classification of example modern systems by level of integration)

Stefik and Bobrow [60] and Wirfs-Brock and Johnson discuss the variations of concepts subsumed under the rubric of an object-oriented formalism. Here, we use the term to refer to systems using the following concepts:

(1) Abstraction of data [40,57];

(2) Inheritance of properties, whether based on single or multiple inheritance mechanism [40,57];

(3) Encapsulation of data and operations [40,57]; and

(4) Persistence of data [4].

Objects are a powerful abstraction mechanism, since they can represent conceptual/physical entities quite directly. Objects are used widely in the area of Distributed Artificial Intelligence, an area concerned “with cooperative problem solving by a decentralized and loosely coupled collection of knowledge sources” [74]. Knowledge-based systems require unprecedented flexibility, including the ability to support multiple representations of objects, and the ability to replace objects incrementally and transparently with new, upward versions [43]. It is appropriate to classify such object-oriented systems as knowledge-based systems.

ACTOR [32] uses actors (or active objects) as knowledge sources with a computing and communication capability. Each actor has its own behavioral set, and actors communicate with one another through message exchange. Each has to “know” the names of other actors so that it can communicate with them. ACTOR functions as an object-oriented message passing system (a level system), and does not address explicitly the issue of integrated task support. However, it contains powerful constructs such as shared resources, inherent concurrency, and dynamic reconfigurability; these are useful for developing integrated office systems that suit the open-ended nature of that environment.

Barber [6,7,8] used AI techniques to develop a system, called OMEGA, for solving office tasks by viewing them in terms of goal attainment. OMEGA incorporates many of ACTOR's constructs. For example, static knowledge (made of office entities) is embedded in the knowledge base by descriptions or viewpoints (for aggregated objects) and dynamic knowledge is embedded in the form of “sprites,” which serve as triggers of actions when assertions are made or goals posted in the knowledge base. OMEGA is a level 2 system.

Lochovsky et al's Office Task Management (OTM) (a level 2 system) is designed to provide office workers with facilities to help them computerize their own office activities. OTM utilizes a concurrent object-oriented programming language, specifically designed to support office tasks, and an object-oriented database management system. OTM is built on the original actor concept [32]. The system is based exclusively on the remote procedure call model, and expresses simultaneous actions by concurrent calls. As such, the relationships between actions of various objects are explicit, and the control of hierarchies of actions or tasks (encapsulated as complex objects decomposable into primitive objects) is easily achieved.

Croft and Lefkowitz's POISE [16] is equipped to handle task integration. The POISE system seeks to automate structured tasks and to provide assistance to certain categories of unstructured tasks. It is a procedure-based system, but one that is augmented by a goal-driven mechanism. Building on POISE, Nirenburg and Lesser [50] developed OFFICE which attempts to provide intelligent assistance in a distributed office environment by constructing an architecture that takes on a task-centered, an agent-centered, and a cognition-oriented perspective. Both systems support task integration.

Tueni et al's [64] Activity Management System (AMS) (a level 2 system) is a knowledge-based support system designed to support office work in a distributed office environment. AMS uses the declarative formalism of AI to represent office activities and their activation conditions, and involves the use of the MPOA (Memory Organization Packet for Activities) to abstract knowledge so that the abstraction can be instantiated in various concrete situations.

Cheng [13], Chou [14] and Du [23] designed systems that interactively acquire knowledge from the office designers for an office automation system. They represent the knowledge (both static and dynamic) in the ORAL language. ORAL is a logic programming language augmented by data typing and referenced in logic programs. These are level 2 systems inasmuch as they are designed to support office workers in cooperative problem solving activities.

Kaye and Karam [39] presented a level 2, knowledge-based system written in PROLOG to provide integrated task support for office workers by embedding knowledge in “a network of distributed cooperating knowledgebased or expert ‘assistants’ and servers.” Their objective is to support cooperating workers by introducing a network of knowledge-based or expert “assistants” that communicate with each other by means of messages.

Chang and Leung [12] designed a knowledge-based message management system with a linguistic filter to screen out junk messages. Relevant messages are then processed by an expert system into various classes. The objective of this system is strictly to eradicate junk messages, permitting the relevant messages to be sorted quickly. There is no attempt to integrate other office activities with the message system. Though Pollock's [53] prototypical ISCREEN incorporates more sophisticated features, such as the classification of messages in terms of predefined criteria, its utility is limited unless its domain of applications extends beyond intelligent message filtering. Park and Teorey's [51] MTP (Multiple Transaction Processor) is a rule-based expert system using a forward chaining inference mechanism that allows users to perform multiple transactions and process multiple queries, and updates simultaneously in both centralized and distributed office environments. However, the idea of cooperation among users is not addressed. FORMS [63] is a powerful, object-oriented system for handing inputs and outputs through dialogue windows. FORMS enables the user to create, modify, retrieve and store forms interactively. The basic concept of FORMS is the “part,” which is an object represented graphically by a subwindow. These systems belong to the level 1 category.

Classification of existing office systems level of task support

<table><tr><td>Conceptual framework</td><td>Level 1</td><td>Level 2</td></tr><tr><td rowspan="10">Data semantics</td><td>Attardi and Simi&#x27;s [5]</td><td>Enhanced OBE [69]</td></tr><tr><td>Programming by Examples</td><td>IBM DISOSS [36]</td></tr><tr><td>Alter [11]</td><td>Lotus 1-2-3 [45]</td></tr><tr><td>Gibb and Tsichritzis&#x27;s [30]</td><td>Lotus Symphony [46]</td></tr><tr><td>Data Model System</td><td>PROFS [37]</td></tr><tr><td>IBM [38]</td><td>Waters and Shepherd&#x27;s [67]</td></tr><tr><td>Office Form Model [42]</td><td>Hypertext</td></tr><tr><td>OBE [77]</td><td>Xerox Star [56]</td></tr><tr><td>SBA [78]</td><td></td></tr><tr><td>VAGUE [48]</td><td></td></tr><tr><td rowspan="6">Process semantics</td><td>ICNs [24]</td><td>CHAOS [19,20,21]</td></tr><tr><td>SCOOP [75,76]</td><td>Sttots and Furata&#x27;s [62]</td></tr><tr><td></td><td>Hypertext System</td></tr><tr><td></td><td>The Coordinator [26]</td></tr><tr><td></td><td>van Bijon&#x27;s [66]</td></tr><tr><td></td><td>Man-Machine Dialogues</td></tr><tr><td rowspan="14">AI (and/or object-oriented concepts)</td><td>ACTOR [32]</td><td>AMS [64]</td></tr><tr><td>Chang and Leung&#x27;s [12]</td><td>INFORMATION LENS [47]</td></tr><tr><td>Message System</td><td>ITHACA [3]</td></tr><tr><td>FORMS [63]</td><td>IWS [2]</td></tr><tr><td>ISCREEN [53]</td><td>Kaye and Karam&#x27;s [39] Knowledge-Based Assistants</td></tr><tr><td>MTP [51]</td><td>OFFICE [50]</td></tr><tr><td></td><td>OMEGA [6,7,8]</td></tr><tr><td></td><td>ORAL-Based Systems [13,14,23]</td></tr><tr><td></td><td>OTM [44]</td></tr><tr><td></td><td>POISE [16]</td></tr><tr><td></td><td>Weiser&#x27;s [68] Object Protocol System</td></tr><tr><td></td><td>WYSIWIS [61]</td></tr><tr><td></td><td>Woo and Lochovsky&#x27;s [72,73]</td></tr><tr><td></td><td>Problem-Solving System</td></tr></table>

Several large-scale efforts to develop integrated (i.e., level 2) office systems using AI and/or object-oriented have been reported. The prototypical office workstation developed under ESPRIT's Intelligent Workstation (IWS) project [2] uses the Knowledge Representation System (KRS) [59], an object-oriented language to represent both office knowledge structures and dedicated reasoning mechanisms. The goal of another large ESPRIT project, ITHACA (Integrated Toolkits for Highly Advanced Computer Applications) [3], is to develop a generic object-oriented office information system so that system analysts can tailor the system to the specific needs of any organization. The generic system is built using a kernel consisting of object-oriented languages and compilers.

Others who have used AI (and/or object-oriented) concepts to develop level 2 systems include Ho et al, Malone et al [47], Stefik et al [61], Weiser [68] and Woo and Lochovsky [72,73].

A classification of office systems along the two dimensions discussed here is shown in Table 1. The classification is by no means exhaustive, but it does reflect a well-balanced list of systems. We could have classified Group Decision Support Systems (GDSSs) [e.g., 1,22,29,31] as level 2 systems, but have decided otherwise. Essentially, they use personal terminals and a public screen, and incorporate communication technologies such as electronic messaging, local- and wide-area networks and teleconferencing. We feel that it is more appropriate to consider GDSSs as an enhanced form of computer-based communication media.

## 3. Discussion

Our classification of office systems using conceptual framework (semantic level) and the level of support (i.e., degree of mechanization or level of integration) as organizing dimensions help highlight two important features. First, the classification serves to separate the underlying conceptual tools of a system from its application domain. This is markedly helpful to designers. If the system to be developed is one where large-scale concurrency is an important requirement, then AI concepts are more appropriate. Such systems will be open-ended and will incorporate mechanisms such as knowledge abstraction, modularity, reusability and extensibility to accommodate continual changes [34]. On the other hand, if the system is intended to enhance the efficiency factor of a self-contained cluster of activities, a level 1 system suffices. It is better to construct a system based on data semantics or process semantics where the speed requirements of information processing can be more easily met. AI (and/or object-oriented) techniques are used only when special features are needed.

Second, the open-ended nature of the office environment [33] underscores the importance of using AI and/or object-oriented concepts as theoretical underpinnings upon which integrated office systems can be developed. Since Barber introduced AI and object-oriented concepts to develop OMEGA, there has been an active interest in the design of integrated systems using AI and/or object-oriented concepts. That is why we dealt with these systems in greater detail.

## References

[1] Adelman, L. “Real-time Computer Support for Decision Analysis in a Group Setting: Another Class of Decision Support Systems,” Interfaces, 14(2), March–April 1984, 75–83.

[2] Ader, M. and Tueni, M. “An Office Assistant Prototype Using a Knowledge-Based Office Model on a Personal Workstation,” ESPRIT Results and Achievements, North-Holland, 1987, 1295–1225.

[3] Ader, M., Nierstrasz, O.M., McMahon, S., Muller, G. and Proefrock. "The ITHACA Technology: A Landscape for Object-Oriented Application Development," In Proceedings of the 1990 Esprit Technical Weeks, Brussels, November 1990.

[4] Atkinson, M.P. and Morrison, R. “Procedures as Persistent Objects,” ACM Transaction on Programming Languages and Systems. 7(4), October 1985, 539–559.

[5] Attardi, G. and Simi, M. “Extending the power of programming by examples,” In Proceedings of the first ACM-SIGOA Conference on Office Information Systems

(Philadelphia Pa, June 21–23), ACM, New York, 1982, 52–66.

[6] Barber, G. Office Semantics. Ph.D. Dissertation, Department of Electrical Engineering and Computer Science, MIT, Camb., Mass., 1982

[7] Barber, G. “Supporting Organizational Problem Solving with a Workstation,” ACM Transactions On Office Information Systems, 1(1), January 1983, 45–67.

[8] Barber., G, DeJong, P. and Hewitt, C. “Semantic Support for Work Organizations,” In Proceedings of IFIP Congress (Paris, France, Sept. 19–23). North-Holland, Amsterdam (1983), 561–566.

[9] Bowers, J.M. Discourse Analysis, Speech-act Theory and Computer Mediated Communication: An introductory review. Unpublished COSMOS Document 42.1, Department of Psychology, University of Manchester, 1987.

[10] Bracchi, G. and Pernici, B. “Design Requirements of Office Systems,” ACM Transactions on Office Information Systems, 2(2), April 1984, 151–170.

[11] Chang, J.M. and Chang, S.K. "Database Alerting Techniques for Office Activities Management," IEEE Transactions Communication, COM-30(1), 1981, 74–81.

[12] Chang, S.K. and Leung, L. "A Knowledge-Based Message Management System," ACM Transactions on Office Information Systems, 5(3), July 1987, 273–289.

[13] Cheng, P.W. Design of Interactive Office Automation System. Masters Thesis, Department Of Electrical Engineering, National Taiwan University, Taiwan, 1984.

[14] Chou. M.S. Office Information Systems Requirement Specification and Analysis. Masters Thesis, Department Of Electrical Engineering, National Taiwan University, Taiwan, 1983.

[15] COSMO (1988). Interim Report on the COSMOS Project. Issued by COSMOS Coordinator's office.

[16] Croft. W.B. and Lefkowitz, L.S. "Task Support in an Office System," ACM Transactions on Office Information Systems, 2(3), July 1984, 197-212.

[17] Daft, R.L. and Huber, G.P. “Organizational Learning: Two Perspectives and an Integration,” In Research in the Sociology of Organizations, (Eds), S. Bacharach and N. Tomasso, 1986.

[18] Daft, R.L. and Lengel, R.H. “Organizational Information Requirements, Media Richness and Structural Design,” Management Science, 32(5), May 1986, 554–571.

[19] De Cindio, F., De Michelis, G., Pomello, L. and Simone, C. "Superposed Automata Nets. Application and Theory of Petri nets," In Informatik Fachberichte, 52, Springer-Verlag, Berlin, 1982.

[20] De Cindio, F., De Michelis, G. and Simone, C. “CHAOS as a Coordination Technology,” In Proceedings Conference on Computer Supported Cooperative Work, Austin, Texas, 1986.

[21] De Cindio, F., De Michelis, G. and Simone, C. "GAMERU: A Language for the Analysis and Design of Human Communication Pragmatics within Organizational Systems," In Advances In Petri Nets, (Ed), G. Rozenberg, Lecture Notes In Computer Science 222, 1987, 21–44.

[22] De Sanctis, G. and Gallupe, R.B. "Foundation for the

Study of Group Decision Support System," Management Science, 33(5), 1987, 589–609.

[23] Du, W.C. “Office Information Systems Design Methodology for Interactive Office Automation System.” In Proceedings of the International Computer Symposium, Taipei, Taiwan, December 1984.

[24] Ellis, C.A. “Information Control Nets: A Mathematical Model of Office Information Flow,” In ACM Proceedings on the Conference on simulation modeling and management of computer systems. New York, 1979, 225–240.

[25] Ellis, C.A. and Bernal, M. "Officetalk-D: An Experimental Office Information System," In SIGOA Conference on Office Information Automation Systems (Philadelphia, Pa., June 21–23), ACM, N.Y., 1982, 131–140.

[26] Flores, F., Graves, M., Hartfield, B. and Winograd, T. "Computer Systems and the Design of Organizational Interaction," ACM Transactions on Office Information Systems, 6(2), April 1988, 153–172.

[27] Galbraith, J.R. “Organizational Design: An Information Processing View,” Interfaces, 4(3). May 1974, 28–36.

[28] Galbraith, J.R. Organizational Design. Addison Wesley Reading, Mass., 1977.

[29] Gallupe, B. “Experimental Research into Group Decision Support Systems: Practical Issues and Problems,” Proceedings of the 19th Hawaii International Conference on Systems Science (Honolulu, Hawaii), 1, 1986, 515–523.

[30] Gibbs, S. and Tsichritzis, D. "A Data Modeling Approach for Office Information Systems," ACM Transactions On Office Information Systems, 1(4). October 1983, 299–319.

[31] Gray, P. “Initial Observations from the Decision Room Project,” Transactions of the 3rd International Conference on Decision Support Systems, (Boston, Mass.), 1983.

[32] Hewitt, C. “Viewing Control Structures as Patterns of Passing Objects,” Artificial Intelligence 8(3), 1977, 323–364.

[33] Hewitt, C. "Offices are Open Systems," ACM Transactions on Office Information Systems, 4(3). July 1986, 271-287.

[34] Hewitt, C. and De Jong, P. Open Systems. A.I. MEMO 692, MIT Artificial Intelligence Laboratory, 1982.

[35] Ho, Cheng-Seen, Hong, Yang-Cheng and Kuo, Te-Son. "A Society Model for Office Information Systems," ACM Transactions On Office Information Systems. 4(2), April 1986, 104–131.

[36] IBM. IBM distributed office system/370/vse. GH12-5137-0. 1st edition, IBM Marketing, May 1981.

[37] IBM. IBM Professional Office System: Programming RPQ P09033 User's Guide, SH 20-5503-1. 2nd edition. IBM Marketing, November 1982.

[38] IBM. Top View: Personal computer software. IBM Marketing, 1984

[39] Kaye, R.A. and Karam, G.M. “Cooperating Knowledge-Based Assistants for the Office,” ACM Transactions on Office Information Systems, 5(4), October 1987, 297–326.

[40] Kim, W. and Lochovsky, F.H. (Eds). Object-Oriented Concepts, Databases, and Applications. Addison-Wesley, 1989.

[41] King, K.J. and Maryanski, F.J. "Information Manage-

ment Trends in Office Automation," In IEEE Proceedings 71 (1983), 519–528.

[42] Ladd, L. and Tsichritzis, D. “An Office Form Flow Model,” In Proceedings of the National Computer Conference, AFIPS Press, Reston, Va, (1980), 533–540.

[43] Liberman, H. “Concurrent Object-Oriented Programming in ACT 1,” In Object-Oriented Concurrent Programming, A. Yonezawa and M. Tokoro, Eds., The MIT Press, Camb. Mass., 1987, 9–35.

[44] Lochovsky, F.H., Hogg, J.S., Weiser, S.P. and Mendelzon, A.O. "OTM: Specifying Office Tasks," In Conference on Office Information Systems. (Ed), Allen, R.B., Palo Alto, California, March 23–25, (1988), 46–53.

[45] Lotus Development Co. Lotus 1-2-3 User Manual, Camb., Mass., 1983.

[46] Lotus Development Co. Symphony User Manual, Camb., Mass., 1984.

[47] Malone, T.W., Grant, K.R., Lai, K.Y., Ramana, R. and Rosenblitt, D. “Semi-structured Messages are Surprisingly Useful for Computer-Supported Coordination,” ACM Transactions On Office Information Systems, 5(2), April 1987, 115–131.

[48] Motro, A. “A User Interface to Relational Databases That Permits Vague Querics,” ACM Transaction on Office Information Systems, 6(3), July 1988, 187–214.

[49] Newman, W.M. “Office Models and Office System Design,” In Integrated office systems, (Ed), N. Naffah, North-Holland, N.Y., 1980.

[50] Nirenburg, S. and Lesser, V. "Providing Intelligent Assistance in Distributed Office Environments," In Proceedings Third ACM-SIGOIS Conference on Office Information Systems, 7(2 & 3), Hewitt, C. and Zdonik, S., Ed., (Rhode Island, October 6–8, 1986), 104–119.

[51] Park, J.T. and Teorey, T.J. A Knowledge-Based Approach to Multiple Processing in Distributed Database Systems," In Proceedings of the 1987 Fall Joint Computer Conference: Exploring Technology – Today and Tomorrow, Dallas, Texas, (October 25–29, 1987), 461–468.

[52] Peterson, J.L. Petri Nets and the Modeling of systems. Prentice-Hall, Englewood Cliffs, N.J., 1981.

[53] Pollock, S. "A Rule-Based Message Filtering System," ACM Transactions on Office Information Systems, 6(3), July 1988, 232–254.

[54] Reisig, W. Petri Nets: An Introduction. Springer Verlag, N.Y., 1981.

[55] Senn, J.A. Information Systems in Management. Wadsworth Publishing Co., Fourth edition, 1990.

[56] Seybold, J. Xerox Star. Seybold report 10(16), 1981, Seybold Publications, Media, Pa.

[57] Shriver, B. and Wegner, P. (Eds) Research directions in object-oriented programming. The MIT Press, 1987.

[58] Simon, H.A. "Applying Information Technology to Organization Design," Public Administration Review, 33(3), May/June 1973, 268–278.

[59] Steels, L., van de Velde, W., Paredis, J., van Marcke, K. and Jonckers, V. Report on KRS Formalisms. IWS deliverable D2/R2, Al-Lab., University of Brussels, 1987.

[60] Stefik, M. and Bobrow, D.G. Object-Oriented Programming: Theme and Variation. Artificial Intelligence Magazine, 6(4), 1986, 40–62.

[61] Stefik, M., Bobrow, D.G., Fostor, G., Lanning, S. and Tatar, D. "WYSIWIS Revised: Early Experiences with

Multiuser Interfaces," ACM Transactions On Office Information Systems, 5(2), April 1987, 147–167.

[62] Sttots, P.D. and Furata, R. Petri-Net Based Hypertext," ACM Transactions on Information Systems, 7(1), January 1989, 3–29.

[63] Texier, M. Systeme de Gestion de Formularies pour des Applications Bureatiques. Internal Technical Report, Directions des Etudes Advancees, Bull MTS, September 1985.

[64] Tueni, M., Li, Jianzhang and Fares, Pascal. “AMS: A Knowledge-Based Approach To Task Representation, Organization and Coordination,” In Conference On Office Information Systems, (Ed), Allen, R.B., Palo Alto, California, (March 23–25 1988), 46–53.

[65] Tushman, M. and Nadler, D.A. "An Information Processing Approach to Organization Design," Management Review, 3(3), July 1978, 613–624.

[66] van Biljon, W.R. “Extending Petri Nets for specifying Man-machine Dialogues,” International Journal of Man–Machine Studies, 28, 1988, 437–455.

[67] Watters, C. and Shepherd, M.A. A Transient Hypergraph-Based Model for Data Access," ACM Transactions on Information Systems, 8(2), April 1990, 77–102.

[68] Weiser, S.P. "An Object-Oriented Protocol for Managing Data," IEEE Technical Committee Database Engineering, 8(4), (1985), 41–48.

[69] Whang, Kyu-Young, Ammann, A., Bolmarcich, A., Hanrahan, M., Hochgesang, G., Huang, K.T., Khorasani, A., Krishnamurthy, R., Sockut, G., Sweeny, P., Waddle, V. and Zloof, M. “Office by Example: An Integrated Office Systems and Database Manager,” ACM Transactions on Office Information Systems, 5(4), October 1987, 393–427.

[70] Winograd, T. and Flores, F. Understanding Computers and Cognition: A New Foundation for Design. Wesley, Reading, Mass., 1987.

[71] Wirfs-Brock, R.J. and Johnson, R.E. "Surveying Current Research in Object-Oriented Design," Communications of the ACM, (9), September 1990, 104–124.

[72] Woo, C.C. and Lochovsky, F.H. "An Object Approach to Modeling Office Work," IEEE Technical Committee Database Engineering, 8(4), (1985), 14–22.

[73] Woo, C.C. and Lochovsky, F.H. "Integrating Procedure-Automation and Problem-Solving Approaches to Supporting Office Work," In Proceedings IFIP, W.G., 8.4, Working Conference on Methods and Tools for Office Systems, Pisa, (1986), 301–324.

[74] Yonezawa, A. and Tokoro, M. (Eds). Object-oriented concurrent programming. The MIT Press, Camb., MA, 1987, 1–7.

[75] Zisman, M.D. Representation, Specification and Automation of Office Procedures. Ph.D. dissertation, Wharton School, University Of Pennsylvania, Philadelphia Pa, 1977.

[76] Zisman, M.D. "Use of Production Systems for Modeling Asynchronous Concurrent Processes," In Pattern Directed Inferences Systems, (Eds), Waterman and Hayes-Roth, Academic Press, New York, 1978, 53–68.

[77] Zloof, M.M. "QBE/OBE: A Language for Office and Business automation. IEEE Computer, 14, (1981), 13–22.

[78] Zloof, M. and De Jong, S. “The System for Business Automation (SBA): Programming Language,” Communications of the ACM, 20(6), June 1977, 324–343.
