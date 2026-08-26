---
otero_id: 17820
otero_key: "S2XQUBQK"
title: "Information policy issues: selecting a policy framework and defining the schema horizon"
authors: "Ben Shneiderman"
year: "1978"
journal: "Information & Management"
doi: "10.1016/0378-7206(78)90027-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Policy Issues: Selecting a Policy Framework and Defining the Schema Horizon

Ben Shneiderman

Department of Information Systems Management, University of Maryland, College Park, MD 20742, USA

Technical advances in database management systems are rebalancing organizational structures as management sees to accommodate these powerful new tools. Managers must participate in establishing a framework for policy decisions and in setting goals for database usage. First, responsibility and authority must be delegated to management and not technical personnel. Second, the bounds of the application, called the schema horizon, should be carefully considered. This paper covers ten information policy issues within these two caregories and attempts to clarify management tasks.

Keywords: Database management, schema, conceptual schema, internal schema, external schema, functional model, extended set theory, data mode theory, decision making, data independence, data submodels organizational behavior, organizational design, database administrator, management information systems.

![](/api/attachments/S2XQUBQK/fulltext/images/2135f6c7c12deb2f71328439619178e05e563a031ee500051ae65aaafa584180.jpg)

Ben Shneiderman is an Associate Professor in the Department of Information Systems Management at the University of Maryland. His early work in programming and programming education; and database and file design; is now complemented by an increased interest in human factors research in information and computer systems.

Partial support for this work has been provided by NSF giant MCS 77-22244

## 1. Introduction

Organizational changes may become necessary as data processing applications are converted to integrated data management systems. In the early stages of this evolutionary process, individual data processing applications handled repetitive accounting/inventory/personnel oriented tasks, but as the scope of applications broadened, the motivation to move towards unified or integrated database management systems increased. The advantages of uniform standards, centralized control of data resources, improved data integrity, reduction in redundant entry and storage of data, accelerated system development and simplified access facilities were too powerful to ignore.

These integrated information systems, no longer merely the automated versions of their predecessors, have changed organizations and produced a new set of expectations from management. Decisions affecting the information system should not be made by low-level management or technical personnel but must be reviewed by higher authority within an organization. These information related decisions are increasingly tied with the policy alternatives for the organization. One can only expect that this trend which parallels the trend towards an information oriented society, will accelerate.

This paper reviews two broad areas of information policy which must be dealt with by high level management. Technical issues are involved, but the management policy component is critical. The first area is the selection of an information policy framework which shapes future directions by assigning decision-making authority and deals directly with the centralization vs. decentralization question. The second information policy area concerns the database definition, called the schema, and the amount of information included in the database, called the schema horizon.

## 2. Data architecture

For the purposes of this paper we adopt the four level data architecture (see fig. 1) described in refs, [1] and [2] where the highest level (Level 4) is a conceptual framework in which an abstract model of the real world is created. This highest level most closely resembles the Conceptual Schema described the ANSI/X3/SPARC Interim Report [3]. The next level (Level 3) is the data model which is a class of data structures which are permitted for describing the conceptual framework. Typical data models are the relational, hierarchic, binary relation or data-structure-set model. A data model has a set of operations for insertion, deletion and querying associated with it. The next level (Level 2) is a specific data definition Schema of the data structure used in an application. The schema is an explicit description of the data items and their interrelationships that are used in an organization. At the schema level there are a multiplicity of closely related concepts such as a subschema which is a description of a portion of the data structure. A subschema may differ slightly from the schema as long as a transformation between the subschema and the schema has been defined; for example, field orders may be changed, data names altered or new relationships established. Useful notions include the internal schemas which describe physical device related issues or external schemas which describe user oriented views of the data. Finally, at the lowest level (Level 1) we have the populated database which adheres to the schema description, i.e., the actual data items on the auxiliary storage devices. A database management system is the hardware and software which manages the database. Modeling is the process of creating a conceptual framework and schema level views of real world information and information flows.

In summary, the populated data case which exists on physical devices such as disk packets is described by an explicit schema description (also stored on the disk). The schema describes a specific data structure chosen from the class of data structures defined by the data model. The data model is derived by placing restrictions or a broader conceptual framework.

<table><tr><td>LEVEL</td><td>CONCEPT</td><td colspan="3">EXAMPLE</td></tr><tr><td>4</td><td>Conceptual Framework for Data Model Theory</td><td colspan="3">A Generalized DRMS Generator (currently on-e-stent)</td></tr><tr><td>3</td><td>Data Model</td><td colspan="3">Hierarchical Model Relational Mode Network Model (data stru-ture-set)</td></tr><tr><td rowspan="4">2</td><td rowspan="4">Database Definition by Schema Description (also sub-schemas)</td><td>Attribute</td><td>No. Characters</td><td>Picture-Claise</td></tr><tr><td>Name</td><td>30</td><td>X(50)</td></tr><tr><td>Age</td><td>5</td><td>9(5)</td></tr><tr><td>Salary</td><td>10</td><td>9(10)</td></tr><tr><td rowspan="3">1</td><td rowspan="3">Populated Database</td><td>Jones</td><td>26</td><td>20000</td></tr><tr><td>Smith</td><td>31</td><td>26000</td></tr><tr><td>Aaron</td><td>28</td><td>2400</td></tr></table>

Fig. 1. Levels of data architecture.

## 3. Selecting an information policy framework

The selection of the information policy framework has a strong and long-range impact on the usage of the database management system. We will examine single vs. multiple schema; centralized vs. decentralized responsibility, authority and access; high vs. low logical data independence; privacy and security; and choice of a high-level conceptual framework.

## 3.1. Issue no. 1: single vs. multiple schema

The motivation for database management systems is the unified or integrated approach which replaced the classic multiple independent application approach of the 1960s. The development of database management systems made it possible for large organizations to unify the application development process and centralize control of data under the database administrator, who created the data description or schema used by all applications. This one schema approach was often expanded to the schema/subschema approach offered by the CODASYL Data Base Task Group Report [4] which provided a centralized, complete data description and multiple subschemas which described portions of the database to be used by a set of application programs. The advantages of sub-schemas were outlined in the DBTG Report as:

\- An individual programmer need not be concerned with the universe of the entire database but only with those portions of the database which are relevant to the program he is writing. Since the database may contain data which is relevant to, and shared by, multiple applications, this may be important to ease the writing, debugging and maintaining of programs.

\- A program is limited to the subset of the schema that is known to it via its sub-schema. To a large extent, this automatically ensures the security and integrity of the rest of the database from that program.

\- A measure of data independence is provided for programs in that certain changes may be made to the schema for the database – and the database adjusted accordingly – without affecting existing programs using that data. This is possible because the sub-schema may vary in certain important aspects from the schema of which it is a subset.

It allows a common language to be specified for defining a data base while allowing that part of the data base known to a program to be described in a manner which is oriented towards the conventions of the language in which that program is written.

Variants of the subschema theme were soon proposed such as sub-subschemas, i.e., multiple levels of subschema, or internal schemas more closely tied to the hardware. In 1975, the ANSI/X3/SPARC Committee proposed a new organizational strategy in their Interum Report [3]. This committee proposed a Conceptual Schema which was a relatively stable high level description of information and information flow within an organization (see fig. 2). No language syntax or semantics were offered. Users would work with multiple External Schemas which described portions of the database in the form desired for applications programs. A single, but possibly time varying Internal Schema would describe the data and storage structures used in implementing the system. This tripartite description nicely separated management concerns (Conceptual Schema), efficiency related implementation issues (Internal Schema) and human factors usage issues (External Schemas) while maintaining the integrated database approach.

Paralleling these ANSI/X3/SPARC activities were the development of relational views in relational systems [5]. A relation is a tabular form of data consisting of rows, called tuples, and columns, called domains. Each tuple may be thought of as being like a record, but the tuples are not ordered nor can two tuples have the same values. A relational database consists of a large set of base relations which can be molded into sets of user oriented views just as schemas can be cut into sets of user oriented subschemas. A view may be made up of domains selected from one or more relations or from tuples selected from one or more relations. For example, a view may contain only employee information for employees in the sales department (see fig. 3). Relational databases have been more research oriented but commercial versions are beginning to emerge. Relational model concepts have been influential in the design of many commercial systems.

Within IBM's IMS [6] the subschema concept was developed in the form of sensitive segments and logical databases which were carefully constrained subsets of the full database description. User programs could operate unaware of segment types not relevant to their application Hierarchies of logical databases are now possible, i.e., sub-subschemas.

![](/api/attachments/S2XQUBQK/fulltext/images/c8346379f88b981aac6b3e3e5d8de3974403ab283bd88372d29b49ff54846d9e.jpg)  
Fig. 2. Conceptual database schema mechanisms n.

Although the flexibility of these multiple schema approaches is appealing there are disadvantages. A central theme of this paper is that too much flexibility may be dangerous. The main fear is that the advantages of unifying the database may be dissipated by the proliferation of schemas. If each application programmer works with a different subschema then the opportunity for sharing programs, cooperating among program development teams and communicating among users may be reduced. If applications programmers are completely isolated from internal implementation issues then it becomes difficult or impossible to take advantage of performance improving strategies. If applications tears are allowed to work completely independently, then they may not be aware of useful data developed by other application teams that is available in the database. This may be true even when a data dictionary is used. Data dictionaries are increasingly popular software packages which keep descriptions of each of the thousands of data names that may be used.

![](/api/attachments/S2XQUBQK/fulltext/images/3d25e0f07759aeae68725279f90bcb4e400e018b97f40237508d9e99f26351af.jpg)  
Fig. 3. Relational model with sales department view.

The second fear is that with multiple levels of schemas it will be difficult to make the multiplicity of transformations in an efficient manner. Each level of schemas implies a transformation of data to a new format, with potentially frightening overhead costs.

The degree of flexibility and the number of schemas that an organization creates is a high level management question since it impacts the organizational design. A stable centralized organization may prefer the single schema approach because of the payoff in simplicity and efficiency. A volatile developing organization with independent divisions and high technical skills may appreciate flexible multiple schema designs because of the freedom it provides.

Of course a sensitive dynamic approach is possible. As a narrowly focused one schema organization diversities, additional schemas may be utilized. Conversely, as a diversified organization possibly resulting from a recent merger, becomes more unified, the number of schemas could be reduced. In short, multiple schemas provide independence, flexibility, case of change and diversity while single schemas require close cooperation and stability.

3.2. Issue no. 2: centralized vs. decentralized responsibility, authority and access

The establishment of a database management system implies the establishment of decision making authority and responsibility, and a definition of access rights to the database. At one extreme are highly centralized operations where data entry, program development and report generation are controlled by a single person. The advantages of such an approach are that communication failures among individuals are eliminated and operations can be closely supervised by a single individual. This environment exists in small installations or highly centralized organizations.

The other extreme is that decision making is dispersed throughout an organization. Data entry responsibility may be distributed to multiple geographically remote sites, authority for system modifications or program development is distributed and multiple terminals give a variety of users access to the database. This distributed approach has been made more viable through the development of communications, cheap minicomputers, networking systems and flexible database management systems, but requires a higher level of technical competence at the numerous decision making points. Interfacing between multiple users is complicated but each site has greater independence of action. Increased flexibility is not always an advantage.

Selection of the degree of decentralization should be made on the basis of the organizational design. A highly diversified organization with a high level of technical competence might benefit from a decentralized strategy. Too much decentralization leads to chaos, loss of control, poor communication and massive inefficiency.

3.3. Issue no. 3: high vs. low logical data independence

Data independence is the separation of user views of the data, from the implementation details. A distinction can be made between physical data independence, whose goal is to allow data administrators to change physical implementation strategies for performance reasons, and logical data independence whose goal is to isolate programs from changes to the logical data structure. Logical data independence reduces the impact of changes in the logical structure of data and enables old and new programs to operate with a minimum of interference. Logical data independence is produced by the use of sub-schemas or relational views. In their excellent paper, Chamberlin, Gray and Traiger [5] offer the following list of benefits for relational views:

(a) Renaming or permuting columns;

(b) Converting units or representation of a column;

(c) Selecting that subset of the rows of a relation which satisfy some predicate;

(d) Projecting out some columns of a relation;

(c) Linking existing relations together into joins which can then be viewed as a single larger table.

which can then be viewed as a single larger table. Transformations (a) and (b) have potentially negative side effects of increased confusion among users. If two groups use different names or units when discussing a domain, cooperation will be more difficult. For

example, if one group uses the term "ton" and the other group thinks it means "metric ton" then errors may result when numeric computations are performed. There is an advantage to terminology standardization if intercommunication among groups is anticipated. Transformations (c), (d) and (e) may also lead to difficulties because of different perceptions of the database contents. These problems are independent of the additional overhead of maintaining different external views and the complications of performing insertions, deletions and updates when multiple views are permitted.

An alternative resolution of the problem of dealing with complex databases does exist. Instead of multiple views which differ in the naming and organization of entities, overlapping partitions may reduce the amount of information required to develop queries or application programs without introducing discordant variations. A single unified description of the database is created, but individuals can be provided with a description of portions relevant to their work. This approach differs from the subscema approach in that variations on the schema, such as renaming or permuting columns and converting units, are not permitted. For example, personnel related entities can be grouped and presented separately from inventory or sales entities (see fig. 4). Similarly overlapping partitions can be created for the inventory management and the ships management staffs. Most standard applications can be written by examining the contents of the relevant partition. When an application covering two partitions is required, say a study of the sales performance as related to years of employment, two partitions would be examined.

![](/api/attachments/S2XQUBQK/fulltext/images/d2e7780c94901f8a44dd4c325f5f2f21298b4d722539db03adb030aad3eb318f.jpg)  
Fig. 4. Overlapping partitions.

The partitions should closely parallel the organizational structure. Change in an organization should be reflected in the development of new partitions. Using this strategy, entities remain uniform throughout an organization and communication is enhanced. Applications programmers are required to examine entities in their partition only. Naming groups of items enhances modularity of data and can improve comprehensibility.

This overlapping partition approach not only responds directly to the question of data independence, but can be an alternative for dealing with multiple schemas and centralization/decentralization.

## 3.4. Issue no. 4: privacy and security

Privacy is the complex of legal and administrative policy issues which defines access rights to information. Security is the technical means for implementing privacy and for preserving the integrity of the data from malicious attacks or inadvertent errors. High level management must be aware of the legal aspects, such as new legislation, affecting the development of a database management system and must assign responsibility for giving access to the database. Management must decide who has the authority to issue passwords, how information is to be protected from improper disclosure and where liability for breach of privacy occurs.

The higher level of security demanded, the higher will be the overhead costs of running the system. Management must prescribe their degree of concern for the divulgence, loss, or alteration of a single field of data, a record and a tile. Backup and replacement costs must be evaluated in the light of the expectation of the severity of a threat and its consequences.

Tighter security can be maintained in highly centralized organization where the traditional techniques of physical security control can be implemented. By controlling physical access to the computer and libraries, and eliminating remote terminal access a high degree of security can be maintained. If a distributed system is required, then the security problems are amplified.

Data encryption should be used since the costs are low and implementation is simple. Since the most vulnerable part of a system is the people who have legitimate access to the data, personnel control is a central management issue.

## 3.5. Issue no. 5: choice of a high level data architecture or conceptual schema

Rothnie and Hardgrave [1] define four levels of data architecture, the highest of which is a conceptual framework described by a generalized system or theory of information. Using this taxonomy as a base Sibley and Kerschberg [2] describe two candidates, the functional model of data [7] and extended set theory [8] for the generalized theory of information. These abstract models are remote from implementation details and allow management to focus on information policy issues. These tools enable management to consider alternative information organization strategies and permit mapping to a lower level relational, hierarchical or data-structure-set model at a later time.

Working within the functional model, management can define the scope of the database and clarify the meaning of information items. The semantics or meaning of the information is specified completely separately from concerns about implementation. This high level data architecture closely resembles the ANSI/X3/SPARC Conceptual Schema whose goal is to describe information and information flows. A successful description at this level might be considered as a precise specification for the ensuing implementation.

Unfortunately, these concepts are still in the research stage, but managers can and should be thinking beyond the detail level provided in data description language syntax. Managers should focus on functional aspects of system usage, for example, what data items will be necessary for future decisions. This is above the level of concern over the coding or physical placement of data items. In short managers must deal with abstractions of data flows which closely mirror real world processes.

## 4. Defining the schema horizon

In developing a database management system, one of the fundamental questions is: How much of the real world should be modeled? In short, how much information should be included in machine readable form in the computer managed database?

Programming manuals and journal research papers give limited examples involving employee files, inventory control or student enrollment. In realistic environments deciding on the scope of the database or the schema horizon is a severe challenge. The pressures for completeness and generality push the horizon far into the distance and result in huge and complex databases. The demands of efficiency and simplicity pull the horizon closer and result in a small easily manageable but limited use databases. A reasonable resolution might be an evolutionary approach which begins with the minimal configuration, but allows easy expansion to a broader horizon.

4.1. Issue no. 6: choosing the relevant entities and attributes

Deciding on a minimum set of entities to include in the schema description is relatively easy. Experience with previous file systems and a knowledge of the currently required outputs gives systems analysts a reasonable impression of the entity requirements. For example, in a university database focusing on student grade information we must know about students, courses, departments, faculty, course grades, course sections, and other intuitively clear entities. Years of experience with student file systems and knowledge of the expected reports have clarified the needs. The difficult issues are the anticipation of new reports and data requirements. Financial aid information, health information, high school grades, course attendance, course crop information, detailed faculty evaluations, psychological counseling information or membership in student organizations may not currently be maintained in the computerized database but could become required items. Because of the substantial impact of database usage and the high costs, the definition of the scheme horizon for the inclusion of entities and attributes should be a high level information policy decision.

## 4.2. Issue no. 7: choosing the relevant relationships

The useful decomposition of a real world model into entities and relationships developed by Senko et al. [9], Chen [10] and others clarifies some issues in schema design. Having chosen the entities to be included in the database, we turn our attention to expressing relationships among the entities. Explicit description of relationships suggests the kind of queries and reports that may be made from the database. Continuing with the previous example, a reasonable student database should show what students are enrolled in courses, what faculty are appointed to departments, what students major in departments, what courses are held in which classrooms, what grades are assigned to a student for a section of a course, and what departments offer courses. These fundamental relationships are clear, but more subtle relationships may have to be derived. For example, the fact that a student takes a course within a certain department may not be explicitly stated in the schema but can be derived from the relationship of students or rolled in courses which are offered by departments. Deciding on which relationships to include in the schema is an information policy question. Such decisions affect the kind of questions that will be posed and strongly impact the complexity and efficiency of the system.

Although Chen's model does not allow relationships on relationships, this is an important possibility which should not be ignored [7]. It may be useful to represent the fact that a student majors in a department and the fact that a professor is in a department. Then on top of these two relationships we may wish to show which students majoring in a department have faculty advisers, that is, we have a relationship built on two other relationships (see fig. 5).

## 4.3. Issue no. 8: modeling the time varying schema

In stable environments with simple scenarios there is a minimum of confusion and ease of use is enhanced. Larger more complex organizations may have extensive schemas which vary over time. In these environments it may be useful to explicitly model the time varying history schema. The entities of the history schema would be entity and relationship descriptions and time periods. These entities of the history schema would be related to queries and application programs by a processing relationship (see fig. 6). This would be an aid in improving logical data independence, since old applications programs using only portions of the current schema could access this information to determine the mapping from old to current schemas. Of course, this elaborate model requires sophisticated users and a more complex implementation.

![](/api/attachments/S2XQUBQK/fulltext/images/5f50f868dd7b18fcb26e8950cc5118d4a8838a3048dc2b7764d89148da565715.jpg)  
Fig. 5. Counsels relationship between two other relationships

![](/api/attachments/S2XQUBQK/fulltext/images/466cdbdc346d9f0e5bac3d99757c823f0d9dc7bfc7814aba8b4b3462662fce09.jpg)  
Fig. 6. Schema model of database processes over time.

This idea has been partially adopted in relational systems which contain relations whose tuples describe other relations in the database. One of the implementations of the CODASYL DBTG Report uses a similar technique to store information about the record and set types.

4.4. Issue no. 9: modeling the database interaction with the real world

Most descriptions of database modeling suggest that the database exists as a representation of real world information items a 1 flows. A more sophisticated approach would be to include in the schema a description of the schema itself and its interaction with the real world. The existence of the database may actually modify or interact with the real world.

It may be crucial to model the fact that certain entities are included in the database and that others are excluded. For example, it might be helpful to know that a student got a grade in a course, which is recorded in the database, and secondly that a written evaluation of the student exists external to the database. In an airlines reservation system for a particular airline, data may be kept about the existence of other airline flights to the same location, even if it is not possible to grant reservations on the other airlines's flight.

A second and more important class of problems relating to the interaction of the database with the real world, concern time of availability of information in the database [11]. In a military intelligence system it is important to record the time of events, such as a battle, but it is also crucial to record the time of events, such as a battle, but it is also crucial to record the time at which the information became available to the information system. This idea of "time stamping" the arrival of information seems natural in some situations, but is often overlooked. In banking systems, the time of a deposit and the time a deposit is entered into the database may be sufficiently different to affect the balance critically. The decision to time stamp transactions should be part of the information policy decisions.

A final topic within this issue is the inclusion of privacy and security controls as an explicit part of the schema. The information concerning which individual users or programs have access to which entities and relationships under what constraints is simply another relationship (see fig. 7). By including these factors in the schema the uniformity of processing is enhanced and usage is simplified.

4.5. Issue no. 10: modeling application programs, queries and utilities

Database schema are models of entities and relationships in the real world while processes such as applications programs, queries and utilities are considered separately from the schema. A more inclusive approach would be to model these processes as part of the database schema (see fig 8). Each query application program or utility is an entity which creates new relationships in the database. Queries are invoked and produce output which is simply another entity. Applications programs are merely complex queries. Utility programs such as audit trailing or backup copying, produce new entities which are different from the main database only in their location and form on physical devices

![](/api/attachments/S2XQUBQK/fulltext/images/6435cb7cc688d903d4792c7eb4b24f1e79cc58107595f39960beaa0fa8cdd483.jpg)  
Fig. 7. Information about the database itself shown as a schema.

By making the information policy decision to include this information as part of the schema, uniformity of processing and simplicity of usage is enhanced.

## 5. Summary

These ten issues in information policy clarify management responsibilities during the establishment of a data base management system. Many other issues must be considered, especially cost/benefit constraints, but the goal here has been to portray traditionally technical issues as management concerns.

![](/api/attachments/S2XQUBQK/fulltext/images/e2badee63d7d950500d147e536a832840773318fd8f8468608618ac95b7ba0d6.jpg)  
Fig. 8. Schema model of database processes and their environment.

## References

[1] J.B. Rothnie and W.T. Hardgrave, Data Model Theory: A Beginning, Proceedings Fifth Texas Conference on Computing Systems, Austin, 1976.

[2] E.H. Sibley and L. Kerschberg, Data Architecture and Data Model Considerations, Proceedings of the National Computer Conference, 1977, AFIPS Press, Montvale, NJ.

[3] ANSI/X3/SPARC Interim Report, SIGFIDET Bulletin, Vol. 8, No. 3.

[4] CODASYL Data Base Task Group Report, April 1973, available from ACM, New York.

[5] D. Chamberlin, J. Gray and I.L. Traiger, Views, Authorization and Locking in a Relational Database Management System, Database Management Systems (Editor, Ben Shneiderman), AFIPS Press, Montvale, NJ, 1976.

[6] IMS/VS Version 1 Application Programming Reference Manual IBM Corp., San Jose, Form SH20-9026-4, 1976.

[7] L. Kerschberg, E.A. Ozkarahan, and J.E.S. Pacheco, A Synthetic English Query Language for a Relational Associative Processor, Proceedings Second International Conference on Software Engineering, San Francisco, 1976, pp. 505–519.

[8] D.L. Childs, Extended Set Theory: A Formalism of the Design, Implementation, and Operation of Information Systems, Volume IV. Current Trends on Programming Methodology, edited by R.T. Yeh, Prentice-Hall, 1977.

[9] M.F., Senko, E.B., Altman, M.M., Astahan, and P.L. Fehder, Data Structures and Accessing in Database Systems, IBM Systems Journal, Vol. 12, No. 1, 1973, pp. 9–36.

[10] P. Chen, The Equity-Relationship Model Toward a Unified View of Data ACM Transactions on Database Systems, Vol. 1, No. 1, March 1976, pp. 30–93.

[11] J.A. Bulenko, Jr., The Temporal Dimension in Information Modelling, Proceeding IFIP TC-2 Conference, Nice, 1977.
