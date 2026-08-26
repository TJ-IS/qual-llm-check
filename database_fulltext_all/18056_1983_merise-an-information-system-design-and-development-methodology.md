---
otero_id: 18056
otero_key: "XUZQSGMB"
title: "MERISE: An information system design and development methodology"
authors: "A. Rochfeld; H. Tardieu"
year: "1983"
journal: "Information & Management"
doi: "10.1016/0378-7206(83)90032-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# MERISE: An Information System Design and Development Methodology

A. Rochfeld

Chief of Information System Operations, Société d'Informatique et de Systèmes, Tour Neptune, la Défense 1, 20 Place Napoléon 1er, 92086 Paris la Défense - Cédex 20, France

and

## H. Tardieu

Ministère de l'Urbanisme et du Logement, mission de l'Informatique, Chief of Technical Unit, 208, rue R. Losserand, 75014 Paris, France

MERISE is an Information System Design and Development methodology widely used in France. The framework of MERISE has three cycles: abstraction cycle, approval cycle and life cycle. The abstraction cycle uses the three database levels (conceptual, logical and physical). The approval cycle recognizes the necessity of identifying decision points during the development of the information system. The life cycle consists of (long range) planning, initial study, detailed study, implementation, launching and maintenance. A system of tools has been defined to support these cycles.

Keywords: Information system, design, conceptual level, logical level, physical level, information base, conceptual schema, information processor, abstraction cycle, approval cycle, life cycle, abstraction system, object system, guidance system, operating system, dynamics monitor, transition monitor, entity, relationship, event, operation, synchronization, initial study, detailed study, domains.

## 1. Introduction

Already, the major costs in a DP project are those of the software, and these will increase in the future. At the same time, users are demanding more reliable systems; yet all recent investigations show that most failures are due to poor specifications. For all these reasons, we need an improvement in design methodologies, and present research seems to converge into a common framework.

![](/api/attachments/XUZQSGMB/fulltext/images/bfd587291ab00eebf7b629bb0e872cdd1798f54243631da6ef9b4b7c883d0002.jpg)

Arnold Rochfeld is chief of Information System Operations in S.I.S., a French software house. He has a degree in computer science from the Faculté des Sciences de Paris and a business degree from ICG. He spent two years in the University of Edinburgh, in the meta-mathematics unit. He was seven years with the METRA Group (Scientific Direction) before becoming in 1977 the director of the MERISE project for the Department of Industry. Aged of 44, he is presently working on information system methodology and on software tools connected with this activity. He is member of ISO TC 97/SC5/WG3, IFIP TC8 and AFCET.

![](/api/attachments/XUZQSGMB/fulltext/images/ef42141e53fc09aaaa7cbb0280c4b87176603b846cb93e3bec05291640abd5ac.jpg)

Hubert Tardieu is an engineer from Ecole Supérieure d'Electricité in Paris; he also got a degree in Economy. After eight years devoted to the design and realization of the DBMS MIISFIIT, he was responsible of the team which developed a data-base design methodology based on the Entity Relationship approach. In 1977, he participated with the MERISE project where he specially worked on dynamical aspects of Information System Design. He is a member of ISO TC

97/SC5/WG3 and IFIP TC8. He is currently chairman of the division "Management, EDP, Decision" of AFCET. Mr. Tardieu is 37 and presently Chief of the Technical Unit "Mission de l'Informatique", Department of Urban Affairs and Transportation, France.

## 1.1. Trends in IS design methodology

The new era of Information System design was initiated by studies on data base design following the publication of the ANSI/X3/SPARC report [1] in 1975. This proposed three levels of modelling and the concepts and terminology to describe the information at each of these levels.

The model of reality was described in terms of data types, and integrity constraints were supposed to restrict this description by specifying (intentionally or extensionally) what was proscribed.

Information systems as developed in firms and civil service were not reduced to data specification, especially if they were real time systems. Bachman [2], Bodart [3] and Rolland [4] have argued that information system description does not consist exclusively of data description but also of processing and interaction descriptions. In other words, these authors propose that it is necessary to describe both static and dynamic aspects of the information system, borrowing (from the data base design approach) the utilization of three levels of abstraction and the idea that we need appropriate formalisms to describe dynamics at these different levels.

One of major difficulties is to identify the features associated with each level (conceptual, logical and physical). We assume that the physical level consists of the description of the operational system, i.e., the description and interaction between various processors, programs and resources. The logical level is supposed to describe a class of information system in terms of types of processors, types of programs and types of resources. The conceptual level deals with the description of the information system in terms of type of processors and type of information without specifying the type of resources used.

We have encountered reluctance in discussing the necessity of a third level (the conceptual level). However, the recently published ISO report on "Concepts and terminology for the conceptual schema" [5] has shown that the conceptual description of an information system can be achieved.

## 1.2. Survey of the ISO report

The ISO report of March 1982 is the result of three years of discussion by a group composed of data base specialists. The major parts of this report are:

\- a comprehensive description of the information system,

\- alternative modelling approaches for static description,

\- modelling of dynamics in order to deal with interaction oriented systems.

The information system consists of an information base and a conceptual schema, forming the universe of discourse description with an information processor (Fig. 1). The information processor produces changes in the information base or in the conceptual schema on receipt of messages originating from the environment. The behaviour of the information system is defined by behaviour rules and constraints established by the environment.

There are three methods for specifying the dynamics:

1. The state oriented approach has a universe of discourse description controlled by rules and constraints specifying which “after-states” may be reached from a given “before-state”.

2. The command oriented approach uses a procedural description for changing an existing "before-state". To control dynamics, a sequence of commands is used. The execution of these commands transform the "before-state" into a permissible "after-state".

3. The interaction-oriented approach deals with rules or constraints concerning either the interactions between the environment and the universe of discourse description or the interactions between permissible actions. This approach is especially useful for those Information Systems which interact directly with the universe of discourse; e.g. real-time system

![](/api/attachments/XUZQSGMB/fulltext/images/048d6aaf305205bcb8e36ee0aa9d3883faa8b5d6c39dc4779e5c803995493279.jpg)  
Fig. 1. Information System and the Universe of Discourse.

## 1.3. MERISE

During the final years of the seventies, an important effort was undertaken in France. The purpose was to develop an information system design methodology which would be used by both private firms and civil service to produce data processing applications which use data bases and real-time environment, and which will be more reliable.

The framework of MERISE [6] has three cycles: (1) An abstraction cycle, (2) an approval cycle, and (3) a life cycle.

1. The abstraction cycle uses the three database levels and for each of these, an Entity Relationship and Interaction Oriented approach was chosen.

2. The approval cycle recognizes the necessity of identifying decision points during the development of the information system: each point corresponds to a decision which has to be made before going further.

3. The life cycle, which is common to many engineering projects, consists of (long range) planning, initial study, detailed study, implementation, launching, and maintenance

The originality of the MERISE methodology is mostly in the abstraction cycle which uses all the modern modelling techniques.

## 1.4. The Impact of MERISE in France

By now, the MERISE methodology has been used on one hundred DP projects in various contexts, either directly by users or with consulting firms. Many DP calls for tenders issued either by private firms or by the civil service request the use of MERISE in the development of the project and their specifications employ the static and dynamic formalism used in MERISE. It is already being taught in some universities $^{1}$ , institutes of technology $^{2}$ , and in specific courses implemented by several software houses.

This paper presents an approach to information system design $^{3}$ . We first present a functional approach to provide a definition of an information system according to the ISO work.

## 2. An Information System Functional Approach

The methodology we shall describe deals with the information system design process. But first we must define the term information system.

## 2.1. The Universe of Discourse

The notion of information system is an extension of previous data base notions. Both terms refer to data (data base) or information (information system) shared by many users. To be useful and reliable, any dialogue must refer to a common understanding of the meaning of data which are shared. We call this common understanding, following [5], the Universe of discourse (UOD). That part of the UOD which embodies classification of things and rules of behaviour is called the abstraction system. The complementary portion is called the object system.

The description of the abstraction system resides in the conceptual schema and the description of the object system forms the information base. An Information system includes both description and an information processor which manages the information base and the conceptual schema (Fig. 1).

We now describe the functioning of the information. It is convenient to describe UOD as a cooperative process consisting of three (sub)systems (Fig. 2) coping with different problems.

1. The guidance system, which is decision oriented. Executives are part of that system and reliable information allows them to play their roles as decision-makers.

![](/api/attachments/XUZQSGMB/fulltext/images/bef7cf1b7933d27543596a275ce4494cab03a3006f08cd6ee7cfbfd409ec7ece.jpg)  
Fig. 2. Global Description of the Universe of Discourse.

2. The information system plays a very precise role and must represent (or model):

● the environment of the firm (arrow 1),

● interactions between the operating system and the outside world-suppliers or customers (arrows 2, 6a, 6b),

\- rules of behaviour of the firm (arrow 3a) according to budget, sales conditions, etc. These rules are transformed by the information system processor into operational rules or scheduling (arrow 3b).

● the operating system returning reports on consumption of various kind of resources, e.g., money, raw materials (arrow 4a, 4b),

● the guidance system which may act on the environment, e.g., by a marketing campaign (arrow 5a, 5b).

3. The operating system, acts on raw materials flow (arrow 8) using, as an evaluator, the financial flow (arrow 7). It yields a flow of products (arrow 10), which brings in financial income (arrow 9).

The raw materials flow is functional. Depending on the type of the firm, it can be: the raw material, or money collected from the public and lent (in the sense of a bank) or used to cover risks (i.e., as an insurance).

Raw material can also consist of information. Some governmental offices collect elementary information and produce elaborate data concerning people and things. For instance, the Department of Health produces statistics about diseases, and Social Security states people's rights to public funds according to their illness or unemployment.

Here we have to draw a difference between information flow used for representation or as a decision carrier, and information flow used as a raw material. As far as information flow is concerned (arrows 1, 2, 3, 4, 5, 6), we consider incoming information as events and outgoing information as results.

We find it also convenient to consider the active part of an IS (the information monitor) as consisting of: circulation of information (M1), and management of data (M2), representing information stored in the information base. The role of these is shown in Fig. 3. In some cases, the interactions between them are so important that the IS must be seen as being part of the OS (e.g. in a process control application). In this case, the IS must describe how the IS interact with the OS. Therefore an IS has to be able to work with the classical data base approach (monitor M2) and also describe the transformation of information (monitor M1).

A gross architecture of such an information system is shown in Fig. 4. More details of this approach may be found in [5].

![](/api/attachments/XUZQSGMB/fulltext/images/75f670df270c5b7023e814e06052b6e5124c470086b4f0bec7f6578a43d43c67.jpg)  
Fig. 4. Gross Architecture for the Information System.

![](/api/attachments/XUZQSGMB/fulltext/images/94a1acbbbba9a8a9fe446925488480c8af01cad03c6950f7d7f7e9419a5b967b.jpg)  
Fig. 3. Global Description of the Information System.

## 2.2. Interaction between the IS and its Environment.

The IS deals with various information flows (Fig. 5) coming from the guidance system (decision on the OS behaviour, decision on the IS behaviour, decision about IS inputs etc.), and the operating system (representational and OS information). The IS also exchanges information with the Operating system. All this information is controlled by the dynamics monitor which is in charge of information circulation in the firm.

An even resulting in arrival of information has an effect on the information base. This is controlled by the transition monitor. To deal with such events and to produce proper results, the dynamic monitor sends a call for consultation or for updating to the transition monitor and receives a report of those operations (including the information needed for producing the result). These interactions are depicted in Fig. 6.

![](/api/attachments/XUZQSGMB/fulltext/images/19d82bf87de5fd949bd8b8d6054b6d510c597c847c832cf96117eb3164cc3fc8.jpg)  
Fig. 5. Classes of Information in the IS.

## 2.3. A Taxonomy of Policy (Guidance)

The guidance system as described, is too broad to provide help in the design process of an IS. The importance of decisions must be considered with respect to the time scale and to the scale of changes. It is thus necessary to define different policies:

1. Business Policy: a day-to-day guidance. Its aims are to define targets (production level, market shares) and to control the execution of the policy according to those targets or goals. Parts of this are embedded is the OS (scheduling, supply policy).

2. Evolution Policy: middle range planning monitoring the firm according to targets, market trends and events.

3. Change Policy: the survival of the firm during deep economical perturbations. This includes long range planning and the future of the firm.

Since the users of the information system belong to both operating system and guidance system, we have to consider all guidance types when we design the information system. We should be very careful when analyzing IS to distinguish between the representation of actual behaviour of the UOD, and anticipated future behaviour. The second is a result of a decision of the guidance system over a period of time.

## 3. A Formal Approach

Most of the methods for description of information systems have concentrated on static aspects; i.e., the way in which valid states of the information base may be described. Until recently, less attention was directed to the study of dynamic aspects (the description of change in the universe of discourse and in the universe of discourse description).

The formal description should provide:

\- a description of the abstraction system to which the universe of discourse description and behaviour must conform;

\- a formulation of the models of the abstraction system at different levels;

![](/api/attachments/XUZQSGMB/fulltext/images/df024980180b67081c09729086a0888ebf387480a7602727cc8ed38ad96c7ddd.jpg)  
Fig. 6. Interactions between GS, IS, OS and Environment.

● the result of a step in the interactive design process of an information system;

● the basis for communication between the persons involved in the IS design.

Predicate logic is definitely sufficient to describe statics and dynamics if we add the concepts of present and past state in order to introduce dynamics. Unfortunately, such an approach appears to be much too formal. We must find constructs using predicate logic as a basis, but appearing less formal.

Basically we must distinguish between the universe of discourse consisting of entities and propositions and the universe of discourse description consisting of terms (referring to entity) and sentences (referring to a proposition). Additional concepts are rules or constraints which constitute prescription or proscription of the behaviour of the universe of discourse.

The description of dynamics in the universe of discourse consists of the description of the following elementary actions: insertion, deletion, and retrieval. In order to insure consistency in the information base, we add the concept of action: a set of elementary operations which must be performed completely in order to reach a new permissible state.

We use the Entity Relationships approach [11] to describe statics. In order to be able to design real time systems, we use an approach which makes very explicit concepts (such as event, process and synchronization) even though the last concept is not by itself absolutely essential. After three years of experiments of this dynamic modelling technique, we can ratify that choice.

## 3.1. Static description of the IS

Descriptions of the Entity Relationship approach have been given in many papers [11-13]. We present here a very brief discussion of this approach.

An entity is any concrete or abstract thing (such as a person, place, invoice, or other object of interest).

An attribute is the representation of a property of an entity or the property of an association between entities. An attribute is said to have a value.

A relationship is a perceived association between entities.

Two basic abstraction concepts are used, "type" and "occurrence". A type is a classification of similar things: we recognize entity-type relationship-type, and attribute-type. An occurrence of a type is a unique individual thing belonging to that type. An entity-type is a classification of entities, each of which has similar attributes. Each occurrence of an entity-type must be unique and therefore distinguishable from all other occurrences of that entity-type. One or more attributes (called identifiers) perform that distinction.

An attribute-type is a classification of similar attributes of all entity occurrences belonging to an entity type or of all relationship occurrences belonging to a relationship-type.

A relationship-type is a relationship defined for one or more entity types. The entity-types over which the relationship-type has been defined from the collection of entity-types of the relationship-type. The dimension of a relationship type is the number of entity occurrences in a single occurrence of the relationship-type.

The functionality of a relationship is given with respect to two distinct entity-types. The possible kinds of functionalities for such a binary relationship-type defined over entity-types A and B are:

... one-to-one (1-1)

one-to-many (1-n)

\- many-to-many $(n - n)$

A total-relationship defined over entity-type A and B requires that every occurrence of A and every occurrence of B must participate in a relationship-occurrence of the relationship-type. In an S partial relationship, some occurrences of A and some occurrence of B may participate in a relationship occurrence of the relationship-type.

The combination of functionality and totality/partiality establishes the cardinality of the relationship (see Fig. 7). It is expressed in term of min-cardinality and max-cardinality where:

![](/api/attachments/XUZQSGMB/fulltext/images/4b06b23cb808bf140e068e96d515cce71f86377c5d3c180529510af9563df27e.jpg)  
Fig. 7. Examples of Cardinality of a Relationship.

\- the min-cardinality is the minimum number of times (possibly 0) that each occurrence of an entity-type can be involved in an occurrence of the relationship-type.

\- the max-cardinality is the maximum number of times (maybe 1) that each occurrence of an entity-type can be involved in an occurrence of the relationship-type.

## 3.2. Dynamical Description of the IS

The conceptual framework for dynamic aspects used in MERISE is based on three concepts: event, operation and synchronization.

1. An event is the observation that something has happened in either the UOD (external) or in the information system (internal). An external event carries a message containing a command. An internal event is produced by the termination of some operation in the IS. It is relevant only if the reporting of termination must be followed by a reaction or by a message to the environment (Fig. 2). An event may belong to certain types. Characteristics of event-types are number and frequency of event-occurrences.

2. An operation is one or more actions accomplished by the information processor as a reaction to an event. An operation, once activated, can be completed regardless of any other event.

The information processor includes dynamic and transition monitors. External and internal events are produced by the dynamic monitor. A single operation of that monitor, can produce one or more internal event (s), maybe depending on the content of the information base. The transition monitor may insert, retrieve, delete and modify sentences in the information base. At any time several operations can be active in the Is. These operations may belong to the same or different types of operation. Two operations which are active at the same time operate completely, independently of each other. The type of an operation determines what the operation will do. An operation is triggered by the reporting of an event. The type of an event determines what type of operation will be triggered. An event-occurrence triggers an instance of an operation-type.

3. The synchronization of an operation is the list of (external and internal) events which must have occurred before the operation occurs, and a rule or set of rules about the necessary condition for the operation to be triggered (see Fig. 8). If more than one event is involved, then the last event fulfills the synchronization condition. The arrival of other events bring the synchronization in a “wait-state”. This wait-state may be limited in time. Local conditions, expressed by rules about sentences accompanying events, may be attached to a synchronization.

![](/api/attachments/XUZQSGMB/fulltext/images/b4f2b7cb0864d926dcb95a25d92ee3ab598a82d0bbd263df97f55194f7918c69.jpg)  
Fig. 8. Description of a Synchronization.

An event (occurrence) itself is information bearing, as it establishes that something has happened. This is not established in general terms, but in a most specific way; for example, a car numbered PCXX999 was produced by Ford Motor Company.

Therefore, an internal event does not establish that an operation of certain type has occurred, but that particular operation (occurrence) with that particular result took place. As a consequence, internal events are submitted to prescriptive rules for the event. A type of operation may possible terminate in a number of different internal events depending on the result of the operation occurrence.

## 4. The Methodological Approach

The life cycle of the information system presents a biological analogy of its construction. We identify a starting point – conception, birth, growth maturity, obsolescence, and death.

The approval cycle is characterised by the set of decisions which have been made during the life cycle. It establishes the hierarchy of decisions that select those elements which are supposed to remain valid for the longest time. Other issues are to identify the actors making the decisions about subsystems (guidance and operating system) and the way to compromise between conflicting views. Last but not least, the approval cycle is also concerned with the acceptance of the new information system both its technical aspects and usability.

The abstraction cycle is commonly used in engineering science in order to isolate at a specific level the relevant elements contributing to the description of a consistent system. For instance, when designing an integrated circuit, electronic engineers first consider the logical level using only NOR gates in order to verify the functionality of the circuit, without considering the cooling system. A second level is generally the electronic description of identified components and the third consists of the implantation of the circuitry.

No information system can be designed ignoring any one of these cycles. We can summarize this in the three axis schema of Fig. 9.

When designing the IS, only considering the plan approval-cycle/life-cycle leads us to make decisions without any global backing of the choices. The design on the abstraction-cycle/life-cycle plan may also be dangerous, because it suppresses any intermediary decision during the life cycle. Finally the use of only the abstraction-cycle/approval-cycle plan is unfortunately common (especially in IS engineering where systems have been carefully studied but never implemented).

In MERISE we made a clear choice to use all three:

1. The classical life cycle: long range planning, initial study, detailed study, implementation, launching, and maintenance

![](/api/attachments/XUZQSGMB/fulltext/images/4b2200cb96fbab673c65d89891c47d24207667e94e3319b7e3db35d52f246b19.jpg)

2. The hierarchy of decision: priority is given to the delimitation of the domain, and the identification of the functions and the information in that domain. Technological choices are postponed after deciding on the automation policy.

3. The abstraction cycle: at a conceptual level, ignoring allocation of resources; at the organizational level, taking into account allocation of classes of resource; and at the operational level identifying the resources which are effectively used.

## 4.1. The Approval Cycle

The approval cycle consists of the hierarchy of decisions which must be made during the life cycle. We classify these before proposing a sequence of decisions.

## 4.1.1. Decisions in the Approval Cycle

The technical decisions concern all choices dealing with hardware and manufacturer's software. What kind of hardware architecture do we want to use? (E.g., a large computer with a star network allowing many CRT terminals, or many distributed mini computers interconnected via a network and supporting local CRT terminals).

Which kind of processing do we need (real time or batch processing)? Do we need a data base management system or a classical file management system?

The organizational decisions deal with the gross architecture. Which tasks are to be performed by human and which tasks are to be performed by computers? How do we organize these resources? Do we concentrate these means in a single place, or do we decide to provide each working station with the necessary processing and storing capability? Do we choose to process events once at a time in order to get immediate response, or do we prefer to group these events in order to optimize the processing?

The management decisions involve the choice of functions which we think are essential for the enterprise. What are the major Input and Output flow? What are the major variables that help the guidance system to make its decisions?

The identification decisions deal with the definition of the objectives and definition of the enterprise (considered as a system). What are the major actors of the enterprise?

The financial decision are the results of all cost-benefit analyses which are made. The design and development of an information system has two major consequences to the enterprise: it costs a lot before working correctly and any error may lead to wrong decision which can affect the profitability or effectiveness of the enterprise.

## 4.1.2. The Hierarchy of Decisions in the Approval Cycle

The hierarchy of decisions is often implicit in information system design. We believe that it is essential to make it explicit, because this hierarchy impacts the abstraction cycle and the life cycle drastically. As an example, the specific order of decisions may be:

\- decide to put micro computers in various places of the enterprise allowing then to be operated in a self service mode;

\- teach Basic to volunteers;

\- let each employee computerize each activity which seems important;

define the nature of the information sent by employees to their managers as reports on activities but without paying any attention to the physical medium containing three informations.

This ordering may be perfectly correct in specific environment, leads to a specific life cycle of the information system design.

The hierarchy of decision in MERISE is built upon our expectations of the evolution of IS. The first decision that we make are those which concern that part of the system which is least likely to change, i.e. the identification decisions (the objectives, the activity of the enterprise, and the corporate goals). The next decisions to be made are management decisions (the choice of the most representative functions of the enterprise and what classes of information are needed to help the guidance system). Further decisions concern the architecture for an efficient information system: organizational decisions. Organizational decisions cannot be made without taking into account financial aspects. A cost-benefit analysis has to be accomplished in order to evaluate decisions and before deciding on a framework, taking into account constraints (such as existing system, reluctance to change, etc.).

Finally, we must decide how to implement the information system: which hardware and software architecture is the best (after a cost-benefit analysis).

As a consequence of this hierarchy, this method deals easily with technical changes, and takes into account organizational changes. We also see that the information system design will be badly affected by management and identification changes.

## 4.1.3. The Abstraction Cycle

An information system is intended to model a complex object system. As in many other engineering sciences, it is essential to identify several abstraction levels. An abstraction level is representation of the information system which is global because the whole system is described, but which is also partial because some details are ignored. The use of abstraction levels will:

\- verify the consistency of the Information system at each level,

\- allow simulation of the behaviour of the system at each level,

\- take into account only one class of problem at each level.

Using the abstraction level lead us to the following questions of choice:

1. Do we need to distinguish a hierarchy of level which is associated with the method, or is it better to allow the designer to chose the appropriate abstraction levels depending on the kind of Information system?

2. In the first hypothesis, how many abstraction levels are necessary?

3. Which abstraction levels are the most helpful?

In MERISE we have chosen three abstraction levels (see Fig. 10): 1. The conceptual level, (2) the organizational level, and (3) the operational level.

1. The conceptual level is the result of identification and management decisions. It is the description of the classes of things and the rules of behaviour which seem to the designer relevant, according to the objectives of the guidance system.

![](/api/attachments/XUZQSGMB/fulltext/images/2f34ce17e43de9ea7bfc1114bff8295892e7ad13dcecc478b92ee92db8c52aa7.jpg)  
Fig. 20 Cross Description of the Abstraction Cycle.

This description is made using both a static and dynamic approach

2. The organizational level describes the natures of resources which are to be used for supporting static and dynamic description. These resources can by human machines, or mixed.

Dynamics at the organizational level. We provide each operation described at the conceptual level with specific resources which can be shared or not. We use the same formalism as the conceptual level, but a conceptual operation will be split into several organizational operations in order to describe tasks; we have also to deal with synchronization at the conceptual level in order to take into account the use of resources.

Examples are shown in Fig. 11 for the conceptual level, and in Fig. 12 for the organizational level. In this example the operation “Check the order” has been split into two operations in order to free the customer data base (DB) and to allow later access to the stock DB. We can notice that the clerk is not freed before checking the stock. Another solution could be to free the clerk after each customer check. In that case the clerk could either check the stock for the same order, or decide to check the customer of the next order.

![](/api/attachments/XUZQSGMB/fulltext/images/629023e7b6078667040d5073546d84b912ff6a7293d2af8cd2456d08f743bff8.jpg)  
Fig. 11.

Statics at the organizational level. Here we use a CODASYL-like formalism to produce a logical design of the information base, as presented in [11]. We obtain a set of DB which will be considered as responses for dynamics. These DB could be considered either as sharable or exclusive resources; if they are sharable, we shall have to deal with sharing of data, either at the type-level or at the occurrence level in the DBMS.

3. The Operational Level. The operational level results from the technical decisions made according to technical targets and constraints (performance, size of secondary storage, response-time, etc.). The choices may be:

\- the type of data organizational such as that described in a Device Media Control Language (hierarchical, network, inverted files, etc.).

\- the type of computer (mini, main-frame, micro).

![](/api/attachments/XUZQSGMB/fulltext/images/70530a9e9a575f87e3b2f88e028ceab9d552816b27b8020e65ba06cc860bafdd.jpg)  
Fig. 12.

All operations, synchronizations, and data bases associated with specific resources; e.g., we may have several working stations, computers or human making the same kind of operations. All organizational operations and synchronizations are translated into program specifications. The general framework of programs can be obtained using a structured programming approach [14], and then a tree-program is produced.

A program generator, such as PROTEE [15], can also be used to produce the general summary of programs. The transaction menu and classes of errors are finally described. Data base physical descriptions may also be obtained (these depend on the DBMS type).

## 4.3. The Life Cycle

The life cycle involves a series of steps which are:

1. Long range planning.

2. Initial study.

3. Detailed study.

4. Implementation.

5. Launching.

6. Support.

They are performed with different precision scale, as shown in Figs. 13 and 14. We just give some details for the three steps which play a major role in this life cycle.

## 4.3.1. Long Range Planning

The major objective of this step is to establish the mapping between the corporate goals and the information needs of the firm. First, a gross description of the existing situation to be made and afterwards the usage of tools such as scenarios allow a partitioning of the Information System into “domains”. For each of those a long range plan (master plan) and a precise schedule, year by year, of the application that are to be implemented, are defined. Such an approach determines

![](/api/attachments/XUZQSGMB/fulltext/images/dbdf33f96b923f44de5da2f22faf268982a2c75c104dfe988fcc45c5cb8ed866.jpg)  
1.2.13 Scopes and Steps.

![](/api/attachments/XUZQSGMB/fulltext/images/812aedf844f70cf250c9a6e64b56f52e7202c477286b21b6a28f1583bbad4404.jpg)  
Fig. 14. Impact of Planning, Initial Study, Detailed Study on a Domain Description.

the general policy for:

1. Human resources strategy (training, hiring, promotion, etc.).

2. Computer strategy (main-frame, mini, micro, or mixed).

3. Software products strategy (DBMS, transaction monitor, development tools).

4. Methodologies strategies (structured programming, SADT, MERISE, etc.)

This general policy can be reviewed during the information system life cycle.

## 4.3.2. Initial Study

The initial study is the second step. It must primarily show that the IS will be functionally acceptable, that its implementation will not exceed a anticipated cost and schedule and that its use will not cost more than expected in the long range planning.

Therefore this study is a trade-off between several conflicting constraints. It must be as short as possible and it must gather as much information as possible in order to make precise economic predictions and to be sure that the proposed system is described in sufficient detail to make it understandable.

For the initial study, the whole abstraction cycle is performed, and so is the approval cycle. We limit investigations to that necessary precision. Therefore, the conceptual level is almost entirely described while only part of the others are needed.

As an example at the operational level we only described operations involved in transactions requiring a short response time.

The results of the initial study is a report summarizing the major decisions which have been made. Each proposed solution is backed by an abstraction cycle showing its impact (especially at the organizational and operational levels). It is the duty of members of the guidance system to make the decision either to choose one of the proposed solutions or to abort the cycle.

## 4.3.3. Detailed Study

The detailed study is only concerned with that part of the information system to be automated. It is performed for each project.

The detailed study completes and validates the choices made. The abstraction cycle covers the entire domain description. The designer must explain (to all concerned users) the choices which have been made and negotiates with them to reach an agreement.

The results of the detailed study are:

the external requirements and specifications, as seen by the future users;

the technical specifications, including test procedures and files;

the internal specifications of the implementation.

The development process, which follows, is more classical and will not be detailed here.

## 5. Conclusion

MERISE has already been used on many projects and has proven its underlying hypothesis. But beyond this experimental validation, we think that many IS design methods are converging in the same direction. In order to make this statement more explicit we have investigated three other methodologies, namely ISDOS PSL/DSL [16], SADT [9] and AXIAL [8] and have a communication from C. Bachman on “application system architecture” [2].

## 5.1. Similarities with Other Methods

If we refer to the three cycles that we described earlier, it seems quite clear that in the abstraction cycle we find great similarities in the basic concepts used for representing statics and dynamics. Using different terminology, all these methods use a static approach based on ER formalism and a dynamic approach based on interaction oriented formalism (event, process, synchronization).

Some of these methods (SADT, AXIAL) do not recognize synchronization as a basic concept. All use abstraction levels but some of them are using an hierarchy of levels embedded in their method (ISDOS, AXIAL, Bachman) and SADT lets the designer distinguish as many abstraction levels as he wishes.

ISDOS (as MERISE) proposes a data dictionary representing a meta level (as defined in (16)) for all the abstraction levels. This data dictionary, supported by a data base management system, is intended to produce an appropriate documentation at each step of the life cycle. It is also used for consistency checking, structural analysis and decomposition, and (more recently) simulation of the behaviour of the IS. Other methods (SADT, AXIAL) are not supported by automated tools.

The approval cycle seems common to all these methods. We think that AXIAL, MERISE and BACHMAN cover the approval cycle since the identification decisions are dealt with through the technical decisions. ISDOS and SADT are primarily application design method, so they are neither concerned with identification decisions, nor by technical decisions.

The life cycle of these methods may be classified in two ways. In a first we find out methods which have a life cycle that can be mapped one to one with the approval cycle; this is the case for SADT, ISDOS and BACHMAN. Another approach is found in MERISE and AXIAL, where the steps of the life cycle are determined by the type of people making the decisions (i.e., executive decisions at the end of the initial study, user decision at the end of the detailed study etc.). These differences are not so important and strongly depend on the decisional process in the enterprise.

Convergence will be helped by the following actions:

\- standardization of concepts for describing statics and dynamics,

\- standardization of the meta description of these concepts in a data dictionary,

\- identification of a taxonomy of tools (such as data dictionary facility, static and dynamic analyser facility, simulation facility and specification languages).

5.2. New language and the Information System Approach

Beyond the scope of these methodologies, it seems to us that the appearance of very high level languages such as ADA [10] may reduce the gap which exists between the description of the operational level and the implementation of programs. We find in ADA, concepts such as “Tasks”, and “Rendez-vous” which are very close to the concepts of operation and synchronization. Another significant trend is the combination of the command language and the programming language (see for instance UNIX [19]). Then the operational level will use a unique language to provide the requested IS dynamics.

## 5.3. Impact on Software Engineering

A growing part of EDP is utilized by real-time business applications. It is surprising to notice the lack of common studies in software engineering and information system design methods. We believe that the results of these studies will be used during the information system life cycle, but no attempt is made to help the user to use these techniques within the same project. We see a need to help the user to consider the whole cycle using one method. This is the way taken in the ISDOS project and it is our choice in MERISE even if the development steps (implementation, launching and support) have been less studied than earlier steps.

## References

[1] ANSI-SPARC DBTG Group. Interim Report - February 1975 SIGMOD Record (ACM, New York).

[2] C.W. Bachman, 'Application System Architecture'. Proceedings of the IIIE Compsac conference (1980).

[3] F. Bodart and Y. Pigneur, 'A model and a language for functional specification and evolution of information system dynamics', in: Formal Models and Practical tools for Information Systems design, H.J. Schneider (ed) (North Holland Publishing Company, 1979; ISBN: 0-4444-35394-4).

[4] C. Rolland, 'Concepts for Information System Conceptual Schema and its utilisation in the REMORA PROJECT', Proceeding of VLDB 1978 (Berlin).

[5] 'Concepts and Terminology for the conceptual schema and the Information base', ISO TC 97/SC5/WG3 (March 1982) ANSI, New York.

[6] A. Rochfeld, 'La méthode MERISE', 01 - Informatique, PARIS Février 1980: 32-37, Mars 1980: 40-45.

[7] D. Teichroew, E.A. Herschey, 'PSL/PSA: A computer - aided technique for structured documentation and Analysis of Information Processing systems', IEEE Trans. Software Engineering, 3 (1) January 1977.

[8] Ph. Pellaumail, 'AXIAL: une méthode de conception de système d'information proposée par IBM France; Informatique et gestion, no. 118, PARIS, (octobre 1980).

[9] D.T. Ross, 'Structured Analysis (SA): A language for Communicating Ideas', IEEE Trans. Software Engineering (January 1977). In: tutorial on software design techniques: 107–125 (IEEE, 1980, New York).

[10] J.D. Ichbiah, Ed, 'Preliminary References Manual', ACM SIGPLAN Notices, 14 (6) (June 1979).

[11] H. Tardieu et al., 'A method, a formalism and tools for data base design: three years of experimental practice', In: P.P. Chen (Ed.), Entity-Relationship Approach to system and Analysis, (North-Holland Publishing Company, 1980, ISBN: 0-444-85487-8).

[12] P. Scheuerman et al., 'Abstraction capabilities and invariant properties modelling with the Entity-Relationship Approach to system and Analysis', in: P.P. Chen (Ed), Entity-Relationship approach to system and analysis, (North-Holland Publishing Company, 1980. ISBN: 0-444-85487-8).

[13] P. Moulin, J. Random, H. Tardieu, 'Conceptual model as a data base design tool', In: Modelling in data base management systems proceedings, IFIP TC2 conference, Freudenstadt, 1976 (North-Holland Publishing Company).

[14] O.J. Dahl, E.W. Dijkstra, C.A.R. Hoare, Structured Programming (London, Academic, 1972).

[15] PROTEE Reference manual (SIS, Paris 1980).

[16] A. Rochfeld, Y. Tabourier, 'Bases de données: un essai de formalisation', Vol XIII (4) Metra Paris 1974: 533-548.

[17] F. Bodard, 'Logical specifications for system dynamics. An extension to PSL', ISDOS Working paper no. 183 (April 1979).

[18] C. Bohm and G. Jacopini, "Flow Diagrams, Turing Machines and Languages with only two Formation Rules", CACM 9 (5), (May 1966) 366–371.

[19] D.M. Ritchie and K. Thompson, "The UNIX Time Sharing System". CACM 17 (7) (july 1974) 365–375.
