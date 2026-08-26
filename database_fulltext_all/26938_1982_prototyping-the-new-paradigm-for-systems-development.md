---
otero_id: 26938
otero_key: "3W4BAZWJ"
title: "Prototyping: The New Paradigm for Systems Development"
authors: "Justus D. Naumann; A. Milton Jenkins"
year: "1982"
journal: "MIS Quarterly"
doi: "10.2307/248654"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Prototyping: The New Paradigm for Systems Development
Author(s): Justus D. Naumann and A. Milton Jenkins
Source: MIS Quarterly, Vol. 6, No. 3 (Sep., 1982), pp. 29-44
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/248654

Accessed: 09/05/2014 12:50

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# Prototyping: The New Paradigm for Systems Development

By: Justus D. Naumann
A. Milton Jenkins

## Abstract

Leading MIS executives and academicians have identified systems development as one of the most critical issues of the 1980s. Their concerns include providing user accessibility to stored information, reducing development cost and delay, increasing developer productivity, and increasing MIS's impact on organizational growth, productivity, and profitability.

Among the number of proposed alternative approaches to traditional systems development, prototyping is mentioned frequently. Prototyping is routine in hardware development but not software. The authors review published references to prototyping and related concepts, and synthesize a process model for information systems. In this model, resource requirements are enumerated and discussed. The article includes an analysis of the economics of prototyping, and a brief discussion of several examples. Prototyping for information systems development addresses today's critical issues; it will no doubt raise a new set of research questions for tomorrow.

Keywords: Information systems, systems design, systems analysis, methodology, economics, productivity

ACM Categories: D2.1, D2.9, D3.2, K6.3

## Introduction

A quiet revolution is taking place in the information systems industry. Trade publications, academic journals, and advertisements are filled with references to “prototyping” for systems development. Traditional systems development methods have become more complex and cumbersome as the industry attempts to incorporate new tools in new applications. The authors believe that the traditional method — the old systems development paradigm — no longer fits the real world. Their research suggests that the new systems development paradigm is prototyping. However, the meaning of the method is not always clear in the published literature. To add to the problem of understanding, experiences and prescriptions that are very similar to prototyping have been called “heuristic development,” “infological simulation,” or “middle-out design.”

This article reports on the growing body of knowledge about prototyping. The authors synthesize fragments from the published discussions of this method into a consistent model of the prototyping process. The reasons for its emergence are discussed, and the roles of the system user and system builder in the new paradigm are discussed. Several examples of prototype systems development are also described. $^{1}$

Websters defines the word prototype as:

1. an original model on which something is patterned; an archetype, or

2. an individual that exhibits the essential features of a later type, or

3. a standard or typical example.

All three descriptions apply to systems development to some extent. Systems are developed as patterns or archetypes and are modified and enhanced for later distribution to multiple users. The first definition is closest to that of manufacturing, where a prototype frequently precedes the fabrication process. In information systems development, the familiar concept of a “pilot”

system covers this sort of prototyping. The literature suggests that this is not an adequate view of the prototyping paradigm in information systems development.

The second definition, that is, a system that captures the essential features of a later system, is the most appropriate definition of an information system prototype. A prototype system, intentionally incomplete, is to be modified, expanded, supplemented, or supplanted.

## The Prototype Model in Management Information Systems

The characteristics of completed information systems depend on the problem that was to be solved, the development process, and the resources employed for development. The parameters of the development process — problems to solve and available resources — are changing. Expectations of the resulting systems are also changing as individuals and organizations learn to interact with information systems. The process of systems development is changing too, in response to these changes in its environment.

Prototyping is a revolutionary $^{2}$ — rather than evolutionary — change in the development process. It is a way of responding to the types of changes mentioned above. This section describes changes that have taken place or are occurring in the problems to be addressed by information systems and in the resources available to the builder. The discussion presents the prototype model for systems development and describes its impact on system builders, system users, and organizations.

## MIS design problems/opportunities

As organizations gain experience and familiarity with computer data processing, they are able to recognize problems and opportunities which require the development of larger and more complex systems. Complexity can increase in specific application areas, e.g., material requirements planning supplants inventory accounting, in the level and amount of systems integration, or in the organization's goals — “information resource management” replaces “applications processing.” Many organizations have developed the data processing systems that automate previously manual applications; their system builders are now developing systems to support decision making.

Users are also recognizing the potential benefits of new applications which were not considered feasible without automation. Many such applications may not be well defined. Although users may see the potential benefits, they may not be able to describe the necessary details of a solution to analysts.

Gibson and Nolan [13] classify these applications as stage 3 or stage 4 information systems. They are characterized by more than increased complexity; they may also be:

\- State-of-the-art: intended to perform a business function that could not be done without advanced technology,

\- Of very high potential value: they may present a payoff potential far in excess of development and operation cost,

\- Integrative by nature: they may necessitate a gathering together of many discrete applications processes, databases, models, and organization units.

Stages 3 and 4 applications require more systems development resources, offer higher benefits, and carry higher risks.

The resources required by stage 3 and 4 information systems included online systems, database management systems, higher level languages, generalized transaction processors, report generators, and easy to use or build models. New systems development opportunities plus advances in hardware and software technology demand replacement of the traditional paradigm. More of the knowledge and effort for the development process must come from the functional area. Systems need to be tailored to individual users while remaining open to rapid, verifiable changes.

The traditional development paradigm does not respond well to increased complexity and uncertainty. The tendency is to increase controls and to require more precise requirements definitions. This response conflicts with the characteristics of stage 3 and 4 information systems: more complex systems, using a more diverse set of resources, and subject to frequent changes, are much more difficult, costly, and time-consuming to specify precisely. The prototyping paradigm provides the needed alternative approach.

## The prototype model

Prototyping an information system is a four-step procedure (Figure 1).

## Identify the User's Basic Information Requirements

Two distinct emphases are suggested for this step: the “data abstracting approach” and the “process simulating approach.” Data abstraction is the focus of Research Group CADIS [7], which suggests that “infological simulation” in the form of experiments with a database driven pilot

![](/api/attachments/3W4BAZWJ/fulltext/images/0a4e2f3a5952ed7978f1837d3f8f286d9e2a5e6371a4797b39fd94cddadf0695.jpg)  
Prototyping is a four-step interactive process between User and Builder. The initial version is defined, constructed, and used quickly; as problems and misfits are discovered, revisions and enhancements are made to the working system in its user's environment.

Figure 1. The Prototype Model system is appropriate. Konsynski [22] surveys the database literature and describes DBMS as a new system design paradigm. In this view, determining requirements means constructing a model of the relevant data. The thrust of more conventional techniques such as the Jackson Methodology [19] and Logical Construction of Programs [33] is that systems design begins with identification of entities, attributes, and data structures. Canning [9] suggests that the new systems development methodologies begin with data rather than process.

The other view is that the first step in prototyping is to model the process. Basili and Turner suggest iterative enhancement [6], that is, implementation of a skeletal solution to be enhanced during interaction with users. Berrisford and Wetherbe [8] propose “heuristic development” to replace the systems analysis phase of the traditional life cycle.

In both of these approaches, the emphasis is on identifying the essential features of a user's requirements. The data abstraction approach assumes that the essential features are data and data relationships. Processes are expected to be provided through the auxiliary features of generalized DBMSs. In contrast, the process simulating approach assumes that both data and process must be identified in the first step. These two views agree that completeness is not important at this stage. $^{3}$

## Develop a Working Prototype

The initial prototype must be implemented in a very short time — almost “overnight.” Hancock [18] suggests “half specified” requirements to produce a “first cut” and “breadboard” system in half the time usually devoted to requirements determination. Online Systems, Inc. [28] suggests that many first cut systems can be developed overnight or at most in two or three days. Donovan and Madnick suggest that prototyping or breadboarding is effective only if done in weeks rather than months or years $[11]$ . According to McCracken $[24]$ , delivery of a running prototype should not take more than a day or two, and, if it does, the user is not being served properly.

This time requirement serves both the user and the builder. The user has a tangible system to experience and criticize; the builder gets responses based upon that experience. This requirement distinguishes prototyping from other approaches in two respects: the resources required by the builder and the initial analysis objectives. The initial prototype system is purposefully incomplete. It is a simulation, in the sense that it represents the essential elements desired by the user in a simplified form. Design and implementation of this system is accomplished not by completely documenting the user's information requirements but by building a working system.

## Implement and Use the Prototype System

“Hands-on” use of the system provides experience, understanding, and evaluation. Earl [12], who emphasizes an organizational development view of systems development. suggests that under prototyping:

As it is a live and operational system, users cannot escape and opt out so easily . . . Users and managers, once they realize that things can be changed and that they can exert influence, may in turn participate with more dedication.

The delivered prototype system meets a fundamental goal of design. According to one of the most quoted thinkers about design, Christopher Alexander [1]:

... the process of achieving good fit between two entities [is] a negative process of neutralizing the incongruities, or irritants, or forces, which cause misfit. The experiment of putting a prototype in the context itself is the real criterion of fit.

It should be apparent that an evaluation takes place whether the traditional or prototype model is used for system development. The users will find the incongruities and irritants which cause misfit whenever a new system is experienced. The prototype model exploits, rather than deplores, this behavior.

## Revise and Enhance the Prototype System

Undesirable or missing features identified by the user must be corrected. Rapid turnaround remains important; therefore, the resources required to build the first prototype are necessary to the revision and enhancement process. The user is not likely to identify all the remaining problems in the system during a single evaluation step. Therefore, several iterations will undoubtedly be required. Steps 3 and 4 must be repeated until the user accepts the system as a good fit.

## Principles underlying prototyping

The prototype model for information systems development specifies construction of a prototype system as a representation of a solution to a problem or opportunity. The prototype model is the most effective representation possible since it enables evaluation of the proposed design in context. According to Alexander [1]:

... every design problem begins with an effort to achieve fitness between two entities: the form in question and its context. The form is the solution to the problem; the context defines the problem. In other words, when we speak of design, the real object of discussion is not the form alone but the ensemble comprising the form and its context. Good fit is a desired property of this ensemble into form and context.

The prototype model is not just another among alternative representations such as written specifications. It is the representation that anticipates evaluation of the design in its operating environment.

Prototyping represents and parallels the dynamic process of growth, change, and evolution existing in any living system. It neither requires nor permits prolonged static specifications in development projects. Since any “freeze points” in the prototype design process are of only a very limited duration, prototyping accommodates changes in both the user and systems environments.

If the user environment is unstable or extremely dynamic, development iterations could continue indefinitely [29]. In such an environment the separate development and maintenance activities of traditional systems methodologies are integrated by the prototype model.

In a more static environment where a prototype meets the user's full needs, it may either serve as-is or be used as the design specification for a more efficient information system. In a stable environment, the decision to replace an operating prototype system with a traditional system can be made with a relatively simple breakeven analysis.

The prototype model is accommodating to instability in the builder's environment. With the introduction of new hardware and software technologies, operating prototypes may become inefficient. When dramatic changes in the technologies being utilized occur, an operating prototype may have to be replaced by a more efficient version. The operating prototype serves as the specification for its own replacement. Because the implementation of a prototype must be easy to change, the effects of systems changes can be largely transparent to the user.

## Prototyping resource requirements

Current technologies, especially online transaction processing and natural language based query-retrieval systems, have in many ways reintroduced a more personalized concept of transactions and accounts, and have reduced the apparent overriding concern for process control associated with earlier batch systems.

Evolution of the systems development process parallels the evolution of data processing methods. Technological capabilities and the “software problem” have impelled development of increasingly detailed and rigorous system development methodologies. This approach has reduced uncertainty about systems development once information requirements have been determined. That is, correctly specified systems can be built on budget and on schedule.

The prototype model differs from the traditional approach in the same way that new processing technology differs from batch data processing. The traditional approach adds steps to keep control of the development process; the prototype model reduces the need for process controls in favor of direct user-system interaction.

Prototyping must be supported by online interactive systems, database management systems, very high level languages, generalized input and output software, and an accessible modeling facility.

## Interactive Systems

In the prototype model, both the builder and the system must respond rapidly to the user's needs. Some batch systems are capable of rapid response, but batch systems do not permit interaction and revision at a human pace. Interactive system capabilities extend computing resources, that is, information processing resources appear to the user to be physically adjacent and immediately available. Interactive facilities extend the apparent power of information processing resources by reducing delays and by extending control over the resource to the user. User perception of rapid and efficient operation and revision helps speed evaluation.

## Database Management Systems

When coupled with interactive processing resources, the natural language based query language of database management systems provides most of the auxiliary functions of managing data. A substantial portion of traditional systems design focuses on tasks and decisions to select access methods, design physical storage structures, provide for backup, security, and integrity, and define and create special data conversion programs. These procedure oriented tasks have no direct value to the user. The supporting database system must provide for rapid and easy creation and revision, and should include input and updating procedures and extensive reporting facilities. Berild and Nachmens [7] provide a list of the features that a prototyping database management system should include.

Database management systems are central to prototyping in two ways. Prototyping without use of database management software prohibits the design and programming of data handling facilities in the desired time frame. In addition, many of the other resources needed for prototyping are being developed as extensions to database management systems. Konsynski [22] surveys a number of database oriented research projects that point in this direction.

## Generalized Input and Output Software

Report generators, report writers, and query languages of varying capabilities have been in use for many years, and are frequently features of, or associated with, database management systems. An output package that uses default formats from very brief specifications is most useful in the initial prototype, while capability to accept more precise specification permits eventual tailoring of the prototype system.

Because editing, validation, error correction, and controls are more difficult to define in any general way for batch oriented processing systems, general input software has not been in widespread use. The adoption of online technology and source data capture has permitted editing, validation, and error correction on a single transaction basis at the point of data entry. Many source data entry systems are currently available, with capabilities ranging from simple field validation and correction to fairly complete editing and validation relative to a database definition. Generalized input software provides for database creation and update without construction of complex edit programs.

## Very High Level Languages

The traditional approaches seem to promote a single language view of information systems development (e.g., a COBOL shop or a PL/1 shop). Language resources of the designer must include more flexibility under the prototype model. Language selection criteria are different: self-documentation, ease of change, and coding and testing speed become far more important when operating efficiently is no longer a primary objective of program development. Languages need to be connected or connectable to the appropriate database management resource and should include provisions for rapid report specification and input processing specification. Languages like APL may have increasingly useful roles in prototype development as standard facilities for input and output of complex data structures are added to them. Emerging very high level languages, for example, BDL [17] are consistent with prototyping and may ultimately provide design primitives at or near the level or user-designer interaction. Query/update languages associated with database management systems may prove useful as very high level languages for prototyping.

![](/api/attachments/3W4BAZWJ/fulltext/images/993cdb18e0e197526fb78fa88dfcc1f9c79a466dedc27ea7ac335cbab38d4340.jpg)  
The Prototype Model requires a database populated through some generalized input processor and/or data obtained from existing databases using very high level languages. Prototype outputs are produced interactively through a generalized output processor, models from a model bank, or, for some uses, through programs and procedures developed in very high level languages.  
Figure 2. Prototyping Resources

## Modeling

Models that make decisions or support human decision making are integral to many systems. A model bank — a collection of potentially useful models — is an important prototyping resource. Inventory replenishment models that can be readily integrated in a transaction processing prototype, and simulation models that can be used to assess outcomes of alternative decisions are examples. Montgomery and Urban [25] describe the relationship of such a model bank to the decision maker and the database.

Very high level languages facilitate the development of models. Under the prototyping paradigm, however, rapid application of reliable models favors the model bank.

## Prototyping roles and results

Prototyping stresses the interactions between the user, builder, and system. This emphasis alters the critical user skills and abilities that are required for successful implementation of information systems. Similarly, the set of critical skills and abilities required of the builder are significantly different from those required for traditional systems development. Figure 3, adapted from Keen [20], illustrates the relationship of the user, system, and builder.

![](/api/attachments/3W4BAZWJ/fulltext/images/87c54a0b33ddf3d66c80e43c28c0a22d26215357eee8b2f9ea6ce210c320f2d6.jpg)  
The User is responsible for the functions of the application system, beginning with definition of basic requirements. Through use and evaluation, the user detects problems and misfits and communicates to the Builder. The Builder constructs and revises the system in response to user feedback.  
Figure 3. Prototyping Roles\*

## The user

Users play more active roles in prototyping than is possible with traditional development methods. In effect they are system designers who use and evaluate a system, and in the process, identify problems and suggest solutions. Users set the development pace by the time they spend using and evaluating the prototype. They decide when the cycle of evaluation and refinement ends.

The user's role requires understanding that along with the flexibility and responsiveness provided by the prototype model comes responsibility for the results. In the relationship established with the systems builder during the development of a prototype, the user will develop an understanding for and appreciation of the specific skills possessed by the builder. Certainly some features of an application will have been initiated by the builder rather than the user. Technical features, performance, and integration of the system with existing databases and processes is the builder's concern, not the user's. While performance and system integration are important to the user, they are primarily builder-system concerns.

In many applications, multiple organizational units and multiple individuals are involved. Here, the user's role includes coordination and communication with other users. The designer cannot perform this key linking role without usurping the user's responsibility for function systems design.

## The builder

The prototype builder constructs successive versions of the system, compromising and resolving conflicts between the context (i.e., user needs and desires) and the form, as constrained by technology and economics. This role more closely resembles that of the systems designer or programmer analyst than of the information analyst [4]. In addition to functional knowledge, e.g., understanding of the user's responsibilities, the builder must understand the available technology that can be used to support development of the prototype system.

In step one of the prototyping process, the builder works with the user to define essential features of the prototype systems. Under the data abstraction approach, the builder must identify the entities of interest, some of their attributes, and the relationships among them. Sufficient detail must be included to create a database definition. With the process simulating approach, the builder must identify those processes that are essential to the user. Finally, the builder must relate both data and processes to available databases, files, and models and decide how to quickly implement the first prototype.

In step two, the builder uses system resources to construct a working prototype. Initial prototype implementation may include report definition, screen generation, database definition, and population with existing or new data, model selection and integration, and user documentation.

In steps three and four, the builder works closely with the user, responding to perceptions of problems and misfits with rapid revisions. Use — and user learning and participation — require that the prototype system “keep up.”

The builder, then, is responsive to user changing perceptions of need and keeps the prototype system responsive to those needs.

## The application

Using the Gorry and Scott Morton [14] model of an information system as a frame of reference, prototyping can be used in any functional area. It will be most useful at the tactical and strategic levels of applications. Managerial activities at these levels are less structured. Decisions are more open and less programmable. More uncertainty exists in the user environment and in design alternatives.

The most promising candidates for the prototype methodology are normally related to managerial functions. Typically, these tasks concern planning, direction, controlling, problem solving, and decision making. Often, these tasks within these areas will be exploratory in nature — probing more deeply and comprehensively into the nature of the problem as well as developing a solution.

Operational control systems and transaction systems are also candidates for prototyping.

Lower level systems can be difficult to define as decision support systems. They need modification and enhancement just like higher level systems. The traditional approach is too inflexible and takes too long.

Selection of the best approach is contingent upon a number of factors including systems size, user knowledge, developer skill, and application stability. Naumann, Davis, and McKeen [26] discuss methodology selection as a function of such contingencies. They suggest that the determining factor is the level of certainty of a successful implementation. When certainty is low, an experimental approach, prototyping, is most effective.

## Development time

The total development time for any given application system may not be significantly changed by prototyping, but the time required to get a useful system in the hands of the user is greatly reduced. The prototype model focuses on quick delivery of an initial system. Both user and analyst time is minimized initially. The user will spend more time on design with the prototype model than with a traditional approach, but the user sets the pace for systems development. The builder is responsible for the rapid design and modification of the prototype. The authors have found no prototype procedures which tolerated over a month for developing the initial model, with much less time allowed for modifications and initial data conversions.

## Economics of prototyping

Anecdotal evidence [7, 16, 24, 27, 30, 31, 32] suggests an order of magnitude decrease in both development cost and time with the prototype model. No empirical comparisons have been published; such research is difficult for well-known reasons, not the least of which is determining the time when a prototype system is “finished.”

Others [22, 30] have noted the additional costs that are or might be associated with the prototype model; expensive resources may have to be acquired to support prototyping; operating costs may be higher for a given system because of the inefficiency on generalized software.

Finally, there is the question of maintenance. Maintenance costs of a traditionally developed system are generally accepted to be the largest component of life cycle cost. Since flexibility is so fundamental to prototyping, maintenance cost should be much lower.

These five factors, development cost, development time, prototyping resource cost, operating cost, and maintenance, are parameters of any economic analysis of the prototype model. Figure 4 depicts the relationships of these parameters. In Figure 4a, life cycle costs of a prototyped system include RA: the cost of acquiring additional resources to support prototyping; SD $_{p}$ : the cost of systems development; and operating cost OP $_{p}$ plus maintenance cost M $_{p}$ . Figure 4b contrasts the costs associated with the traditional systems development paradigm. Systems development, SD(t), takes considerably longer. In addition to the much higher systems development cost, there is some opportunity cost, or cost for delayed use, DE. Over the operating life of the traditionally developed system, frequent and costly maintenance $^{4}$ M $_{t}$ significantly increases life cycle cost.

Figure 4 highlights several relationships that must be considered in any comparison of the paradigms:

1. Resource acquisition RA may completely override all other cost considerations. But many organizations have already installed generalized database management systems and other resources needed to support prototyping. High initial resource costs may not be a significant part of life cycle costs when amortized over a large number of systems.

2. The slope shown in Figure 4a, $OP_{p} + M_{p}$ , for operating cost plus maintenance of a prototype is not well understood. Operating costs may be higher because of the overhead associated with generalized software, although the parallels with program code suggest otherwise. (Expert programmers can produce more efficient code than generalized software, but applications programmers generally do not do so.)

![](/api/attachments/3W4BAZWJ/fulltext/images/f75952aa07df85f1b712b467a79bef3f35f5022a91ef300fa8fe5698f1a85329.jpg)  
Prototyping resource costs (RA) may initially be large but are fixed. The opportunity cost (DE) of not having a system as rapidly, plus the continued cost of maintenance (M) may make the life cycle cost of the traditional paradigm exceed prototyping.  
Figure 4. The Economics of Prototyping

Prototype maintenance is assumed to cost much less than maintenance of traditionally developed systems because there is less to maintain and because maintenance takes place at a higher level. Prototype systems are designed with changeability in mind. Extending the change process into the operating life of a prototyped system should not greatly reduce the capacity for rapid and inextensive change.

3. The opportunity cost of traditional systems shown in Figure 4b, DE, is a critical parameter. The time from starting to completing development in the traditional paradigm means that the new system is not available for an extended period. Opportunity cost is not often included in life cycle costs in part because it is difficult to estimate and in part because it is not directly charged to the development project. It needs to be considered because the new paradigm offers the opportunity for a significant reduction.

4. Maintenance, under the traditional paradigm, may really be a sort of extended prototyping [10]. Much of maintenance is matching a system to new users' needs and to changes in the user's and system's environment. Regardless of the purpose, the cost of changing a traditionally developed system is assumed to be higher than that of a prototype.

At this state of understanding, each manager must provide the parameter values for this analysis. The authors believe that when a careful analysis is performed, prototyping will be economically preferable for many applications. $^{5}$

The other side of prototyping economics is measurement of benefits. The cost comparison presented above is limited to a discussion of the choice of development paradigm once the decision to build a system has been made. The prototype model suggests two additional economic factors. First, as suggested by Naumann, et al. [26], for some potential applications the level of uncertainty about successful implementation is too high to attempt development with a traditional approach. The “experimental discovery of requirements” provided by prototyping permits informed evaluation of benefits at an early stage. This implies that at least some beneficial systems that could not be developed under traditional methods will be implemented with prototyping.

Secondly, prototyping implies an incremental decision strategy, i.e., the user can make an informed decision to drop a system, hold it stable, or continue development with each evaluate-refine cycle. Keen [21] suggests that value analysis is appropriate, at least for DSS, with prototypes. In this model, users establish a cost threshold by estimating the maximum benefits to be gained by a system development investment. Value analysis seems to apply to any prototype since investments can be made in relatively small increments.

## Published Examples of Prototyping

The term “prototype” appears with increasing frequency in journals, the trade press, and advertising. Users of these terms are each describing a nontraditional approach to systems development. This section surveys some of these references to prototyping. $^{6}$

## Small and simple

Bally, Brittan, and Wagner [5] describe the development of a very simple application. The initial model in this system required no computer programming and simply produced computer print-outs from cards; subsequent models introduced the computer to users. The system evolved from a listing of job transactions to experiments with job scheduling. The authors stress the importance of noting that each step in this simple development sequence was undertaken only as a response to a clearly perceived user demand that was based on the practical experience gained in a previous step.

This article illustrates the iterative nature of the prototype model and the need for user learning to determine information requirements. While the prototyping resources required in this application were minimal, the roles of the user and designer are clearly defined.

## Changeability

Appleton [2] provides an unusual example of the application of the prototype model to a functioning system. A complex operational information system was plagued by continually changing requirements and high dissatisfaction with the inability of the systems development group to respond to the users' dynamic environment. The developers replaced a conventionally developed system with a prototype system. Following this conversion, which was entirely transparent to the users, enhancements and modifications were expeditiously handled and user dissatisfaction nearly disappeared. In this example an operational information system was converted to a prototype system to be able to respond to the user's changing needs. In this article, the existing application system was used to determine basic user requirements. Users then evaluated and builders refined the prototyped systems.

## Large multiple-user system

Groner, Hopwood, Palley, and Sibley [15] present a case study illustrating the effectiveness of prototyping in conducting a thorough information requirements analysis. The article describes the use of prototypes to deal with uncertainty in both the user and designer environments.

Prototypes were required in the requirements analysis phase because users could not be sure that computer systems were needed, what functions they should perform, or how they would use them [15].

The prototyping process described in this article appears to deviate from the prototyping model in the sense that the users played a minor role in specifying the initial systems requirements. This article provides a discussion of the prototyping resources, the level of documentation, and the perceived benefits of the prototyping approach. The builders provided a tangible system to facilitate user understanding of both the problem and possible solutions.

## User learning

Earl [12] provides a brief description of three prototype case studies. He focuses on the behavioral aspects of prototyping — as a catalyst to participative design, learning, and organizational development. A financial control system prototype forced managers, who had delegated design to an accountant and a designer, to participate in the development of the system and to make critical design decisions.

## Appropriate tools

Read and Harmon [30] describe the development of an integrated reporting system supporting the U.S. Navy's Fleet Combat Direction System Support Activity. They describe the resources employed as "fourth generation language." The system they describe collects data from the databases and files of many transaction systems and supports interactive user development of tabular and graphic outputs. Read and Harmon state that a more traditional approach would have been futile for this application. In particular, they emphasize the improvement in systems development productivity with fourth generation languages.

## Quick and clean

New software is available which appears to ease or eliminate many of the problems of long periods of definition or implementation, of uncertainty around system specifications and benefits, and of the high cost of frequent alterations [31].

Scott suggests that a database can be built in a day, reports can be produced in less than a day, and such systems can be both effective and efficient. He describes a system that was estimated to cost \$350,000 to develop, and the under \$35,000 prototype that did the job instead. The managers who use the system have become eager and satisfied users as well as enthusiastic supporters of the Systems Division.

These application articles illustrated that systems are being implemented using the prototype model. The literature also presents several related design techniques, e.g., heuristic development, iterative enhancement, systems sketching, evolutionary design, pilot models. All of these techniques share with the prototype model the recognition that development of complete and correct information requirements specifications prior to implementation is both technically and behaviorally infeasible. However, all of these techniques differ from the prototype model in terms of the resources required, the roles of the users and designer, and in the nature of the resulting information system.

## Conclusions

Builders and users of information systems continue to be dissatisfied with the traditional approach to systems development. Information requirements are very difficult to determine, and there is substantial risk that a system, when implemented, will not fit the user environment. Systems take a long time to implement; during that time, users and their environments change. Over the operational life cycle of a system, both environmental changes and user learning necessitate system modifications and enhancements.

More complex systems that must operate in less structured environments are demanded. Such systems must be designed to respond rapidly to user learning, user environment changes, and new technology.

Prototyping presents a different way of approaching information systems implementation. The prototype model requires extremely rapid construction of systems. The prototype builder's and user's paradigm accepts the uncertainty of information requirements statements and the certainty of continuing change. Prototype information systems are purposely incomplete and very changeable. Users interact with their system in its environment to specify their requirements more completely and correctly. System builders accept more costly technology and continual change in order to match changing user perceptions of need.

Prototyping, like any new paradigm, can be expected to introduce a new set of problems. The economics justifying prototyping in general seem clear, but the decision rules for specific organizations and applications are not.

Advances in technology have made prototyping feasible, but no integrated set of prototyping resources is yet available. Individual applications can be and are being developed under the prototype model. No one has studied the implications of a portfolio of prototypes. Issues such as developer training, management control, data integrity and security, and the behavioral implications of more frequent change must be studied and resolved.

Understanding of these issues and solutions to the problems of prototyping will require research. Applied research on prototyping is very expensive, the technology is costly, and experiments will need real users in their organizational environments.

It is not clear how much of system development can or should be done with prototyping. Certainly, many structured problems require it. The authors are convinced that this paradigm addresses the most critical issue facing MIS managers today: the organizational productivity gained if applications systems are put into operation when they are needed.

## References

[1] Alexander, C. Notes on the Synthesis of Form, Harvard University Press, Cambridge, Massachusetts, 1964, pp. 21, 24.

[2] Appleton, D.S. "System 2000 Database Management System," Guide 37, Session No. IS-23, Boston, Massachusetts, November 1-2, 1973.

[3] Appleton, D.S. "What Data Base Isn't," Datamation, January 1977, pp. 85-92.

[4] Ashenhurst, R.L., ed. “Curriculum Recommendations for Graduate Professional Programs in Information Systems,” Communications of the ACM, Volume 15, Number 5, May 1972, pp. 368-98.

[5] Bally, L., Brittan, J., and Wagner, K.H. "A Prototype Approach to Information Systems Design and Development," Information and Management, Volume 1, Number 1, November 1977, pp. 21-26.

[6] Basili, V.R. and Turner, A.H. "Iterative Enhancement: A Practical Technique for Software Development," IEEE Tutorial: Structured Programming, #75CH1049-6, September 1975.

[7] Berild, S. and Nachmens, S. "CS4—A Tool for Database Design by Infological Simulation," Research Group CADIS Report TRITH-IBADB 3103, IEEE Tutorial: Software Methodology, #EHO 142-0, November 1978.

[8] Berrisford, T.R. and Wetherbe, J.C. "Heuristic Development: A Redesign of Systems Design," Management Information Systems Quarterly, Volume 3, Number 1, March 1979, pp. 11-19.

[9] Canning, R.G. "The Production of Better Software," EDP Analyzer, Volume 17, Number 2, Canning Publications, Inc., February, 1979.

[10] Dodd, W.P. “Prototype Programs,” Computer, Volume 13, Number 2, February 1980, p. 81.

[11] Donovan, J.J. and Madnick, S.E., "Institutional and Ad Hoc DSS and Their Effective Use," Database, Volume 8, Number 3, Winter 1977, pp. 79-88.

[12] Earl, M.J. "Prototype Systems for Accounting, Information and Control," Accounting, Organizations and Society, Volume 3, Number 2, March 1978, pp. 161-170.

[13] Gibson, F. and Nolan, R.S. “Managing the Four Stages of EDP Growth,” Harvard Business Review, Volume 52, Number 2, January-February 1974, pp. 76-88.

[14] Gorry, G.A. and Scott Morton, M.S. "A Framework for Management Information Systems," Sloan Management Review, Volume 13, Number 1, Fall 1971, pp. 55-70.

[15] Groner, C., Hopwood, M.D., Palley, N.A., and Sibley, W. "Requirements Analysis in Clinical Research Information Processing—A Case Study," Computer, Volume 12, Number 9, September 1979, pp. 100-108.

[16] Halbrecht, H.Z., Edelman, F., Peterson, D.J., Bedell, E.F., and Perry, G.M. "Critical Perspectives on MIS: The MIS Executive Perspective," Proceedings of the Eleventh Annual Conference of the Society for Management Information Systems, September 1979, pp. 161-171.

[17] Hammer, M.W., Howe, G., Kruskal, V.J., and Wladawsky, I. "A Very High Level Programming Language for Data Processing Applications," Communications of the ACM, Volume 20, Number 11, November 1977, pp. 832-840.

[18] Hancock, J.L. Presentation to the Society for Management Information Systems, Washington, D.C., May 1977.

[19] Jackson, M.A. Principles of Program Design, Academic Press, London, England, 1975.

[20] Keen, P.G.W. “Adoptive Design for Decision Support Systems,” Database, Volume 12, Numbers 1 and 2, Fall 1980, pp. 15-25.

[21] Keen, P.G.W. "Value Analysis: Justifying Decision Support Systems," MIS Quarterly, Volume 5, Number 1, March 1981, pp. 1-16.

[22] Konsynski, B.R. "Data Base Driven System Design," Proceedings of the First Conference on Systems Analysis and Design, Elsevier-North Holland, Atlanta, Georgia, 1981.

[23] Lientz, B.P., Swanson, E.B., and Tompkins, G.E. "Characteristics of Application Software Maintenance," Communications of the ACM, Volume 21, Number 6, June 1978, pp. 466-471.

[24] McCracken, D.D. "A Maverick Approach to Systems Analysis and Design," Pro-

ceedings of the First Conference on Systems Analysis and Design, Elsevier-North Holland, Atlanta, Georgia, 1981.

[25] Montgomery, D.B. and Urban, G.L. "Marketing Decision-Information Systems: An Emerging View," Journal of Marketing Research, Volume 7, Number 2, May 1980, pp. 226-234.

[26] Naumann, J.D., Davis, G.B., and McKeen, J.D. “Determining Information Requirements: A Contingency Method for Selection of a Requirements Assurance Strategy,” The Journal of Systems and Software, Volume 1, Number 4, Elsevier-North Holland, New York, New York, 1980, pp. 273-281.

[27] Nichols, P.L. "The Radical Effect of Data Base on Systems Development," Canadian Data Systems, Volume 9, Number 3, May-June 1977, pp. 64-65.

[28] On-Line Systems, Inc. OLIVER Reference Manual, Pittsburg, Pennsylvania, 1973.

[29] Podolsky, J.L. "Horace Builds a Cycle," Datamation, Volume 23, Number 11, November 1977, pp. 162-168.

[30] Read, N.S. and Harmon, D.L. “Assuring MIS Success,” Datamation, Volume 27, Number 2, February 1981, pp. 109-120.

[31] Scott, J.H. "The Management Science Opportunity: A Systems Development Management Viewpoint," MIS Quarterly, Volume 2, Number 4, December 1978, pp. 59-61.

[32] Sprague, R.H. "Decision Support Systems: Implications for the Systems Analyst," Proceedings of the First Conference on Systems Analysis and Design, Elsevier-North Holland, Atlanta, Georgia, 1981.

[33] Warnier, J. Logical Construction of Pro-

grams, Van Nostrant Reinhold, New York, New York, 1974.

## About the Authors

Justus D. Naumann, Ph.D., is Assistant Professor of Management Information Systems and Computer Science at the University of Minnesota. He has been in the computer industry for 25 years, holding technical and managerial positions in hardware and software design, marketing, and systems analysis, and design. He is currently conducting research in information systems development, software engineering, and management of systems development. Professor Naumann holds a BA degree, plus MS and Ph.D. degrees in MIS from the University of Minnesota. He is a member of ACM, AIDS, IEEE, SMIS, and TIMS.

Milt Jenkins, M.B.A., Ph.D., is an Associate Professor of Management Information Systems at the Graduate School of Business, Indiana University where he has developed Masters and Doctoral Programs in Management Information Systems. He has twelve years of industrial experience in engineering, systems design, purchasing, and management with Whitin Machine Works and Sandia Laboratories. He is active as a consultant with various business and government organizations, and as a researcher in systems analysis and design, and the MIS user systems interface. He is a member of the American Institute for Decision Sciences, the Society for Management Information Systems, the Association for Computing Machinery, and the Association for Systems Management.
