---
otero_id: 19744
otero_key: "4VCGGBAC"
title: "Tun-OCM: A model-driven approach to support database tuning decision making"
authors: "Ana Carolina Almeida; Fernanda Baião; Sérgio Lifschitz; Daniel Schwabe; Maria Luiza M. Campos"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113538"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Tun-O<sub>CM</sub>: A model-driven approach to support database tuning decision making

![](/api/attachments/4VCGGBAC/fulltext/images/f6ce2dd7e47be9808a498afeb5b28cc78666948e35ebe41ac5e623cc404fb896.jpg)

Ana Carolina Almeida <sup>a,\*</sup>, Fernanda Baiao˜ <sup>b</sup>, S´ergio Lifschitz <sup>c</sup>, Daniel Schwabe <sup>c</sup>, Maria Luiza M. Campos <sup>d</sup>

<sup>a</sup> Statistics and Mathematics Institute (IME), Rio de Janeiro State University (UERJ), Rio de Janeiro, RJ, Brazil

<sup>b</sup> Department of Industrial Engineering, Pontifical Catholic University of Rio de Janeiro (PUC-Rio), Rio de Janeiro, RJ, Brazil

<sup>c</sup> Department of Informatics, Pontifical Catholic University of Rio de Janeiro (PUC-Rio), Rio de Janeiro, RJ, Brazil

<sup>d</sup> Computer Science Department, Federal University of Rio de Janeiro (UFRJ), Rio de Janeiro, RJ, Brazil

## A R T I C L E I N F O

Keywords: Database systems Tuning decision Heuristics Configuration management Ontology pattern language

## A B S T R A C T

Database tuning is a task executed by Database Administrators (DBAs) based on their practical experience and on tuning systems, which support DBA actions towards improving the performance of a database system. It is notoriously a complex task that requires precise domain knowledge about possible database configurations. Ideally, a DBA should keep track of several Database Management Systems (DBMS) parameters, configure data structures, and must be aware about possible interferences among several database (DB) configurations. We claim that an automatic tuning system is a decision support system and DB tuning may also be seen as a configuration management task. Therefore, we may characterize it by means of a formal domain conceptuali zation, benefiting from existing control practices and computational support in the configuration management domain. This work presents Tun-O<sub>CM</sub>, a conceptual model represented as a well-founded ontology, that en compasses a novel characterization of the database tuning domain as a configuration management conceptu alization to support decision making. We develop and represent Tun-O using the CM-OPL methodology and its underlying language. The benefits of Tun-O are discussed by instantiating it in a real scenario.

## 1. Introduction

Database tuning is a continuous process whose goal is to increase the performance of applications accessing a database. It is typically executed by a team of Database Administrators (DBAs). They are responsible for adjusting and experimenting with several combinations of parameters that impact the physical characteristics (e.g., buffer size) of a computational environment or even the amount of data transferred between disk and memory for each disk access or the number of checkpoint segments. They also perform several related tasks, such as deciding where data should be physically allocated across distributed platforms, creating and maintaining secondary data access structures. In addition, DBAs typically deal with a lack of standards at the physical database level due to the existence of a highly heterogeneous and competitive industry. There are specificities at each Database Manage ment System (DBMS) implementation that impact on the physical design of the database and on the choice of adequate access structures to improve the performance of the information systems connected to a DBMS. Additionally, the DBA decision needs to be disseminated to the entire team, as each decision may impact the computational environ ment and, consequently, future decisions.

There are many heuristics proposed in the database literature to help DBAs improve the performance of DBMSs [1–6]. However, their implementation typically requires commands or parameters that are native to particular DBMSs. Consequently, there is a demand for DBAs to acquire a large amount of specific knowledge, which impairs the inter operability among different DBMS and the management of data in frastructures composed by heterogeneous DBMS platforms. This scenario is increasingly common in modern organizations, especially in the case of data service providers, making the DB tuning task even more difficult.

It is crucial to establish a common conceptualization to address these issues among DBAs involving DBMSs elements and heuristics defini tions, at a level that makes it independent of specific DBMSs. This common conceptualization also facilitates the understanding of each decision made, either by the team or by the tuning system throughout the tuning task. It can also enable semantic support for their automatic implementation in different DBMS platforms.

A complicating factor is that organizations are increasingly outsourcing their physical data storage to cloud environment providers. In this case, performance parameter adjustments need to be defined and controlled through service level agreements (SLAs). There is no control over some physical configurations, which further complicates the configuration management of the DBMS. Moreover, some parameters may influence and even preclude the use of others. For example, the PostgreSQL DBMS has two settings: shared\_buffers and checkpoint\_seg ments. The shared\_buffers configuration parameter determines how much memory is dedicated to PostgreSQL to use for caching data. The check point\_segments parameter is the maximum number of log file segments between automatic WAL (Write-Ahead Logging) checkpoints. Post greSQL recommends for larger settings of shared buffers a corresponding increase in checkpoint\_segments to spread out the process of writing vast quantities of new or changed data over a larger extended time [7].

It is thus necessary to construct a precise and extensible conceptual framework to support corporate data management strategies that establish quality criteria at the physical level. Its precision enables the translation of data quality constraints to the physical level as accurately as possible without loss of semantics. Its extensibility allows such limi tations to be particularized for each operational environment (operating system, DBMS, memory architecture, distributed architecture) available in the organization. Each physical data management platform may be semantically integrated into a defined conceptual backbone. For this, a data model is used as an abstraction to provide a high-level represen tation of this universe of interest.

This paper proposes $\mathrm { T u n \mathrm { \cdot } O _ { C M } , }$ a model-driven approach to support database tuning decision-making adopting a configuration management perspective. To build Tun $- \mathrm { O } _ { \mathrm { C M } } ,$ we have used ontological analysis and an ontology pattern language (OPL) to support our conceptual model development strategy. OPLs have been largely used for constructing expressive models through the reuse of well-grounded and validated fragments (patterns), improving the models quality and speeding up the development process. We derive the proposed model using CM-OPL, which is a specific ontology pattern language defined for this task and applied to the configuration management domain. The proposal is evaluated through a proof of concept by instantiating the proposed model in an actual scenario, showing that the modeling process becomes more agile, precise, and with fewer ambiguities. In addition, Tun-O allows tracking each step taken during the tuning process until a deci sion is made, thus its impacts may be audited and assessed.

This paper is organized as follows. Section 2 characterizes the database self-tuning system as a decision support system and Section 3 discusses it from a configuration management perspective. Section 4 presents an overview of $\mathbf { C M - O P L } ,$ our proposed OPL applied to the CM domain. Section 5 illustrates how CM-OPL was used to develop Tun-${ \mathrm { O } } _ { { \mathrm { C M } } } ,$ the proposed database tuning model that we instantiate for eval uation purposes. Section 6 discusses how the perspective of the CM domain can help the database tuning task. Finally, Section 7 concludes this paper.

## 2. The database self-tuning system as a decision support system

Stair and Reynolds [8] present a well-known model developed by Herbert Simon, in which decision-making is represented as a problem solving component (Fig. 1).

In the first stage of decision making (intelligence), potential prob lems or opportunities are identified and defined together with resource and environmental constraints. Alternative solutions to the problem are developed in the design stage. The choice stage requires selecting a course of action. In the next stage (implementation), a solution is put into effect. In the last stage (monitoring), decision makers evaluate the implementation to determine whether the anticipated results were achieved, and to modify the process in light of new information.

![](/api/attachments/4VCGGBAC/fulltext/images/b270fac7dab58624fa12c2fb301bfa0689c2d269cf01cf42898bb0e104b40306.jpg)  
Fig. 1. Decision making stages based on [8].

Given this description, we claim that a database self-tuning system can be considered a decision support system (DSS). A database selftuning system is a tool which automatically adjusts database configu rations to improve performance by decreasing the response time of transactions and statements that are submitted to the database. For example, in the intelligence stage a slow query may be detected in the database production environment. This slow query remains running for longer than the limit established by the tool and generates several locks, preventing other database applications from continuing their activities. In the design stage, the tool applies heuristics to list the possible ways to solve the problem (e.g. kill the query and suggest an index to speed it up in future executions). In the choice stage, the tool applies other heu ristics to select one of the alternative solutions presented (e.g., kill the query to release other transactions). In the implementation stage, the tool kills the query and continues to monitor the database (monitoring stage).

The decision model associated with our proposal corresponds to a procedural model, according to the classification of Lahti [9]. We base our procedural model decisions on standard operating procedures or guidelines pre-established by the management system and decisionmakers’ actions following these procedures and policies. Such proce dural model includes multiple scenarios (e.g., database without indexes, with indexes, partitioned among others), objectives $( \boldsymbol { \mathrm { e . } } \boldsymbol { \mathrm { g . } } ,$ , reducing query response times, increasing throughput, and managing changes to database configurations), and alternatives (e.g., indexes, materialized views, partitioning).

In terms of the decision-making process [10], Tun-O is considered a conceptual model for the design phase. The given goals will guide the alternatives of the eventual actions. As already mentioned, the objec tives involve reducing the response time for queries, increasing throughput, and managing changes to database configurations. The other stages of the process (decision strategy, generation of alternatives; measurement of costs and benefits, among others) will depend on the heuristics implemented by the DBA in our model. For modeling per formance problems and selecting database tuning alternatives, the use of Multiple Criteria Decision Making (MCDM) theory can be considered [11,12], more specifically the Multiple Attribute Decision Making (MADM). In the context of database tuning, using MADM, we have a finite set of alternatives (e.g., indexes, materialized view, or partition ing) based on established criteria $( \boldsymbol { \mathrm { e } } . \boldsymbol { \mathrm { g } } . ,$ available disk size, available memory for the DBMS, number of nodes in the cluster).

## 3. Configuration management helps tuning decision-making

According to the ISO 10007:2017 standard, configuration is a set of physical and functional characteristics that describes a product at a given time. In the context of this standard, the term product should be interpreted as applicable to all product categories, e.g., documents, fa cilities, firmware, hardware, software, tools, materials, processes, ser vices, and systems. Configuration management (CM) is used for documenting product or service configurations – the interrelated func tional and physical characteristics of a product or service, including design, realization, verification, operation, and support [13]. This pro cess provides identification and traceability, the status of achievement of its physical and functional requirements, and access to accurate in formation in all phases of the life cycle. The life cycle is the set of consecutive and interlinked stages of a product (or service) system. Life cycle stages include the acquisition of raw materials, design, production, transportation/delivery, use, end-of-life treatment, and final disposal [14].

Moreover, ISO 10007:2017 defines that the configuration manage ment process incorporates planning, configuration identification, change control, configuration status accounting, and configuration audit activities [13]. The management planning coordinates configuration management activities in a specific context throughout the product life cycle. The configuration identification selects the items and their interrelationships, describing the product structure. Items are parts of the product or information generated during its development. Configuration items are the ones whose functional and physical characteristics can be managed separately, to achieve the overall end use performance. The configuration item (CI) and the product evolve, and their changes need to be managed. The change control involves a description of, a justifi cation for, and a record of all changes with their categorization (complexity, resources, scheduling), consequences evaluation and how changes should be dispositioned, implemented and verified. The configuration status accounting activity results in records and reports that relate to the product and its configuration information. Finally, the configuration audit activity determines whether a product conforms to its requirements and configuration information.

Although not usually approached with this perspective, DB tuning is a likely domain of knowledge for the application of the CM process. The reproducibility of tuning activities for different workloads and distinct parameter value configurations fits the desired requirements of such an experimental and empirically-driven scenario. In addition, the tuning decision making generally employs several heuristics, since they enable experimenting with different strategies under different configurations that need to be managed. If the search space of configurations is large, making correct decisions will require a long time. Configuration man agement can make tuning decision making more agile by limiting this search space during configuration identification. Configuration man agement can also assist in reviewing tuning procedures and practices according to results that did not meet expectations, since all traceability of tuning decision-making is traced. Finally, in a scenario in which there are several decision makers (such as a DBA team), configuration man agement can demonstrate the impacts of each decision as well as enable the rollback to some previous database configuration version (change control), over which the decision for a tuning action may have caused damage to the database.

## 4. CM-OPL: A configuration management ontology pattern language

The CM-OPL facilitates the reuse of conceptual models in the configuration management domain, as well as other OPLs that value reuse and guide the construction of models from existing fragments.

This paper addresses the application of ontology patterns (OPs) in a particular domain. A domain-related ontology pattern (DROP) is a reusable fragment extracted from reference ontologies that captures part of the core knowledge related to a specific field (in the present paper, the configuration management domain). Thus, a DROP may be seen as a fragment of a core ontology of that domain [15]. Any OP and DROPs, in particular, may be specified using an OPL, a language to formalize and organize DROPs in a guided application process by explicitly repre senting the relations between them [16].

An OPL comprises (i) a network of interconnected DROPs, which provide holistic support for solving ontology development problems in a specific domain, and (ii) a modeling workflow guiding how these DROPs may be applied and combined in a particular order, with suggesting patterns for solving some modeling problems in that domain [17].

OPLs are still a novel topic, but some works have already been published in different application areas. The measurement ontology pattern language (M-OPL) addresses the core conceptualization of measurement [18]. The service ontology pattern language (S-OPL) provides a network of interconnected ontology modeling patterns covering the core conceptualization of services [19], and it has been applied in a real case study to model an email service in a big Italian company. The enterprise ontology pattern language (E-OPL) [20] or ganizes aspects common to several enterprises. It has been used for building an enterprise ontology on Brazilian federal universities. Also, an ontology pattern language for the software process domain (SP-OPL) was used for creating a domain ontology about the software measure ment process [21].

For the configuration management domain, we have already pre sented an initial proposal of an OPL for the car CM domain [22], describing the first pattern group. The last full technical report, con taining all CM-OPL patterns groups, is detailed in [23]. In this present paper, the CM-OPL process is discussed in summary and applied to another domain (Database Tuning), validating it through the instantia tion of the resulting ontology.

CM-OPL is described as a set of ontology patterns and the associated process that should be followed to combine these patterns, in order to build new configuration management ontologies for distinct scenarios. The CM-OPL patterns are represented in OPL-ML [24], which is a modeling language for representing ontology pattern languages.

The patterns in CM-OPL were derived from the CM Task Ontology presented in [25]. This ontology was chosen because it is well-founded using UFO-A [26], which facilitates the removal of ambiguities and promotes common understanding. Moreover, the authors define a behavioral conceptual model of the control change process, which aids the definition of OPL, and clearly justifies the classification of the ontology as a task ontology.

The CM-OPL patterns are organized in three pattern groups, according to the process presented in the previous section: configuration identification, version control and change control (Fig. 2). In OPL-ML, a pattern group is a way of grouping related OPs and other pattern groups [24]. They are represented by regions delimited by blue solid lines (Fig. 2) [24].

Fig. 3 shows a detailed process to guide the construction of a con ceptual model based on CM-OPL.

The model developer starts (EP entry point) by selecting the configuration item to be managed (ISelection). Next, s/he decides who will manage the configuration (Configuration Manager) and, in the case the item to be configured is to be decomposed into sub-items whose configuration should also be configured, it is necessary to define how these configuration items will be decomposed (CIDecomposition).

The model developer proceeds to define the configuration version control using the CIVersion pattern, which models the configuration item’s version. This group’s other patterns are optional and are only applied when considered relevant to that specific domain. The version of the configuration item can also be decomposed (CIVDecomposition) into atomic or composite. Then, a baseline of the configuration item version is defined (CIVBaseline). A baseline is a product configuration that was revised and designated to be a basis for future development [25]. In addition, a variant or revision of the configuration item version may be specified (CIVMode). Wang and colleagues [27] discuss ontology-driven software configuration management, highlighting the difference be tween revision and variant processes formally. Besides, they mention that the layered ontology (as a conceptual model) makes these processes more disciplined by providing a general mechanism to explicitly express what is changed when a new version is created.

S/he then proceeds to define how to control the changes of the configuration item. A change request is submitted by the Requester (CIVCRequest). If the change is considered relevant, the Evaluator de cides if it should be implemented or not (CIVCREvaluation). In the former case, the version to be changed is checked out (CIVCheckout) and the Executor implements the requested modification (CIVCRExecution). After the modification, the new version is checked-in (CIVCheckin) for verification (CIVCRVerification) by the Verifier.

![](/api/attachments/4VCGGBAC/fulltext/images/2ae0e6d5ee3815ab8a2214bf043673a1e713a819d6f34c2b2cae1c7fcdfc52e0.jpg)  
Fig. 2. General view of the CM-OPL Process.

![](/api/attachments/4VCGGBAC/fulltext/images/3811e12b97136b052bf7a094331593a7e77d82778050793de199c15a756a4cfe.jpg)  
Fig. 3. CM-OPL detailed process.

The approach proposed by [16] was applied to derive the DROPs from the CM core conceptual model. The steps are: (i) modularize the core conceptual model according to the three main activities of CM; (ii) fragment each sub-model into smaller pieces still meaningful for the domain based on competency questions; (iii) review the model frag ments and select the DROPs supported by foundational ontology pat terns (FOPs); and (iv)pack the DROP with its associated useful information.

The following competency questions were considered: (CQ1) Which items have their configuration managed? (CO2) Who is the configuration manager that selects each configuration item? (CQ3) Who can play the role of configuration manager? (CQ4) How is a configuration item decomposed? (CQ5) Which version of the configuration item will be changed? (CQ6) How is an item version decomposed? (CQ7) Which configuration has the configuration manager set as a baseline? (CQ8) Does the version change correspond to a revision or a parallel version (variant)? (CQ9) Who requested the modification of the configuration item? (CQ10) Which change the person/computational agent has requested? (CQ11) Which item version the person/agent submitted for change? (CQ12) What is the result of the change request evaluation? (CQ13) Which version of the item does the person/computational agent want to modify or check out? (CQ14) Who checked out the version to be modified? (CO15) Which change is going to be performed on the item? (CQ16) Who executed the modification of the configuration item? (CQ17) Which modification or change has the person/computational agent made? (CQ18) Which modified version has the person/agent generated? (CQ19) Which configuration item version the person/ computational agent wants to become current configuration item version? (CQ20) Who implemented the new configuration item version that will be checked-in? (CQ21) Has the change been effectively implemented?

## 5. The Tun-O mode

CM-OPL provides a network of reusable patterns to foster the con struction of high quality conceptual models that may be considered as domain ontologies. These patterns have been applied to build Tun ${ \bf \Gamma } \cdot { \bf O } _ { { \bf C M } } ,$ a well-founded conceptual model that encompasses a novel character ization of the database tuning domain as a configuration management conceptualization. This section presents the database tuning domain from the perspective of a CM task, and describes the proposed Tun-O<sub>CM</sub> model using the CM-OPL methodology and subjacent language. The benefits of Tun ${ \mathrm { \partial } } { \cdot } { \mathrm { O } } _ { \mathrm { C M } }$ are also discussed by instantiating it in a real scenario.

## 5.1. Characterizing database tuning as configuration management

As stated in Section 2, Configuration Management (CM) is a process that includes the design, realization, verification, operation, and support of the characteristics of a product or service, and is used for doc umenting product or service configurations. CM helps in the control and organizational changes made to the product throughout its life cycle, preventing significant losses to a project.

Similarly, database tuning involves the design, realization, verifica tion, operation, and support of all the changes made by (a team of) DBAs on a DBMS and on its managed databases, towards improving the per formance of applications accessing them. These changes, however, in fluence many resources managed by the DBMS in ways that may be complex to manage and difficult to predict. For example, the creation of several indexes and materialized views to speed up a query workload can reach the maximum disk or storage space, leading to a shutdown and, if it happens, it is important to identify which action caused this shutdown and make it possible to undo such action so that the envi ronment returns to its operation. In this scenario, the heuristic for creating a data structure (such as an index) should be extended so as to evaluate the available disk space before creating it. Given the potential impact that database tuning actions may trigger on a system environ ment, it is important to manage DBMS configuration carefully.

Considering the main activities that compose the configuration management process, database tuning may be characterized as follows:

(i) Item Type Definition: the DBMS itself and the database instance are the Item Types to be tuned and have their configuration managed. While the several parameters of the DBMS enable DBAs to manage the hardware-related parameters of the database, as well as its features and physical design, the database instance can be modified with additional data structures to improve its performance;

(ii) Item Atomicity: for tuning the DB, it is necessary to know which configuration items compose others and how they are related, in order to evaluate potential impacts of a database tuning decision. For example, a configurable database is composed of many database tuning CIs (atomic or composite), such as data struc tures (e.g. table, index). In this way, the configurable database is classified as a composite CI. In addition, configurable primary storage and configurable secondary storage (which are of kinds “memory” and “disk”, respectively) are classified as composite CIs too, since they have components (e.g. “disk block” and “buffer”, respectively) that can be configured separately, to speed up the DB performance;

(iii) A DBMS is considered atomic because its configuration depends on the behavior of its modules and none of them can be directly and individually configured (that is, they may not be considered mereological parts of a DBMS as a CI). There are parameters associated with the DBMS to establish the size of the storage components (e.g. disk block and buffer) that the DBMS must allocate. So, these atomic CIs are configurable to improve the DB performance. Moreover, a relational database, for example, is organized into data structures called tables, which are atomic CIs. The logical structure of a table is defined by columns, and each column is an atomic CI because its domain is configurable. Finally, there are two configurable classic data structures used to tune the database: index and view. According to Elmasri and Navathe [28], an index structure is an auxiliary file, that is, an alternative access path that allows direct access to data using an index key, and a view in SQL terminology is a single virtual table (not physically existent) that is derived from other tables (refer enced in a query defining the view);

(iv) Configuration Definition: DB tuning CIs (atomic or composite) must be selected and need to be created or changed to improve DB performance, and the person responsible for managing that task must be defined;

(v) Version Control: it should be possible to record all the tuning actions performed as well as to have the option to undo any ac tion, returning to an earlier version of a particular CI;

(vi) Change Request: a database tuning requester (which may be a human agent, such as a DBA, or a computational agent, such as a monitoring tool, as represented in Fig. 12), may request many changes to tune the database (such as an index creation):

(vii) Change Evaluation: any requested change must be evaluated before it is implemented so that, for example, database unavail ability does not occur or the index creation requested by the developer may not be necessary (even if the index exists, the optimizer will not use it);

(viii) Change Execution: any required and approved configuration changes need to be implemented in the DB;

(ix) Change Validation: any implemented change needs to be vali dated by verifying the DB metadata and evaluating its statistics. The database objects (DB Tuning CIs) carry metadata with properties that can be used for managing those objects [28]. For example, the DB metadata can be consulted to confirm if an index was created or not. Also, the statistics can help the DB optimizer to decide if the created index is adequate to speed the response time of a query. The DBA can verify the use of the index through the execution plan generated by the optimizer. Statistics allow the user to validate that the submitted tuning actions have indeed improved the performance of the DBMS. For example, the execution plan shows the costs of operations to answer a query and the DBA can validate the tuning action comparing the costs before and after the tuning action. If the total cost decreases it means that the tuning action was properly defined.

## 5.2. Applying CM-OPL in the development of $T u n – O _ { C M }$

This section describes the application of CM-OPL. Each colored rectangle in the figures of this section represents a DROP derived from CM-OPL. The application of a DROP in the database tuning domain is represented as a dotted rectangle of the same color as its corresponding DROP.

Following the CM-OPL process, the first step of the Configuration Identification group (Fig. 4) is to apply the ISelection pattern. Both a DBMS and a Database (i.e., a DB schema with its data) are items that can be configured (i.e., Configuration Items). A DBMS is a (software) system that manages several databases simultaneously, while each DB is managed by exactly one DBMS. From a CM perspective, the CI is specialized into Database Tuning Configuration Item and the Configuration Selection is specialized into Database Tuning Configu ration Item Selection. This way, the CIs that can impact the perfor mance of the DB are made explicit, and make it possible to track which of the CIs contributed to achieve performance gains, thus creating evi dence to support the choice of a specific CI, which otherwise would rely on tacit knowledge from the DBA.

Then, the Configuration Manager variant pattern group was applied. In real scenarios, database tuning may be supported by a tool that just guides the DBA in analyzing, conceiving and implementing steps to improve the performance of the DBMS (manual mode), in semiautomatic mode or completely automated carried out by a tool (selftuning mode). Therefore, the Database Tuning Configuration Man ager may be either a Database Administrator (i.e., a human agent using the P-Manager pattern), a semi-automatic mode (both types of agents, using the PA-Manager pattern) or a self-tuning mode (i.e., a Database Tuning Computational Agent using the A-Manager pattern). This is illustrated in Fig. 5.

The last pattern of this group is the CIDecomposition pattern group. In this pattern, a Configuration Item is specialized into Atomic CI and Composite CI and, for database tuning in particular, into Database Tuning Atomic CI and Database Tuning Composite CI, respectively.

Database Tuning Atomic CI is further specialized into Config urable DBMS, Configurable Disk Block, Configurable Buffer, Con figurable Column, Configurable Index, Configurable Table and Configurable View, since these are not composed of other items. A DBMS may be configured by its parameters that impact its modules and performance. A Disk Block (Secondary Storage Component) may be configured by the balanced distribution of space occupied by each DBMS module. A disk is a random access addressable device and the transfer of data between main memory and disk takes place in units of disk blocks [28]. Depending on the values assigned to the number of available disk blocks, I/O may decrease and thus increase DBMS performance. A Buffer (Primary Storage Component) may be configured by deter mining the size used for caching tables and index data pages as they are read from disk. As larger portions of data are transferred to memory, fewer disk accesses will be required. A Column may be configured by changing its domain (Column Domain - for example, a column with char domain can be changed to varchar domain to optimize the disk space). An Index may be configured by choosing its type (Index Type), which defines the data structure used for the index implementation and therefore strongly impacts database performance. Possible types are B + -tree, hash and bitmap. For example, a bitmap index helps to speed up the search on columns with a narrow domain (e.g. gender), but may degrade performance if created over a column with many variations. A Configurable Index indexes one or more columns. A Table (which, as defined in the database literature, is formed by several Columns) may be configured by specifying different partitioning schemas, where each schema defines a set of complete and non overlapping subsets of tuples from the table. Table partitioning potentially reduces the amount of data from a table that needs to be scanned to answer a query, and also enables parallel execution of queries, thus improving database performance [28]. Table and Index are specializations of Data Structures. A View may be configured by materializing the data resulting from a query (Materialized View) to speed up a complex query that, for example, needs to aggregate data. In this way, the Materialized View concept was modeled as a View and it is materialized in a Table. Also, a View is derived from one or more Tables referenced in the query.

![](/api/attachments/4VCGGBAC/fulltext/images/ba8aee1aca5b382bc48b9b002ccb11fe6cb01a8a8776a6158e5bd1546a53b3ac.jpg)  
Fig. 4. Fragment of configuration identification group applied to database tuning configuration model – Part 1.

Database Tuning Composite CI is further specialized into Config urable Database, Configurable Primary Storage and Configurable Secondary Storage. To have its performance improved, a Database may be configured by changing its composing Database Tuning Configuration Items (e.g. Columns, Indexes). The Primary Storage (Memory) and a Secondary Storage (Disk) may be configured by setting the size of their parts (Storage Components): Buffer (Primary Storage Component) and Disk Block (Secondary Storage Compo nent), respectively.

To model the configuration of the memory parameter measures that influence the performance of the database, the Tun-O (Fig. 6) also partially used the M-OPL [18].

The first pattern of the M-OPL used is the MEnt pattern, responsible for identifying which entities and elements should be measured. Measurable Entity is a concept whose instances represent anything that can be measured. In the database tuning domain, the Measurable Entity can be any Storage Component, such as Buffer and Disk Block. Measurable Entities are characterized by Measurable Elements. Buffer and Disk Block are characterized by their respective sizes (Buffer Size and Disk Block Size). The Disk Block Size determines the transference unit for each I/O operation between the storage device and memory. All these size characteristics specialize Storage Measurable Item Size.

Next, the Mea pattern was used, which concerns modeling problems related to identifying measures that quantify measurable elements. The Measure used to quantify these sizes is the Allocation area. Through the MUnit pattern, the measure is expressed in units. In the database domain, we called the unit as Storage Unit (e.g. megabyte, gigabyte). Also, the MScale pattern is related to scales for measures and the TMScale pattern is about types of scales. In the storage scope for database tuning, the allocation area has a Typical Disk Block Interval Scale, which may vary from 512 to 8192 bytes [29]. Taking advantage of the Scale concept, the generalization relationship of Column Domain (e.g. var char2, integer) and Index Type (e.g. b-tree, hash) to Nominal Scale was added because they cannot be objectively measured. Finally, the MUnit&Scale pattern establishes the relation between measurement units and scales. Measures have Scales composed by all possible values (Scale Value) to be associated by the measure to a measurable element

![](/api/attachments/4VCGGBAC/fulltext/images/c2ce3c15fd25eac17b9b31674de7a12b77a6f9b4adc8b70b900017aac7ba6911.jpg)  
Fig. 5. Using the rolemixin pattern to define a configuration manager.

![](/api/attachments/4VCGGBAC/fulltext/images/f0a97fa8229b845902cf0c19927e5ec89b7108013f28f6a83bb43cd8415303e3.jpg)  
Fig. 6. Fragment of configuration identification group applied to database tuning configuration model – Part 2.

[18].

Next, the Version Control pattern group (Fig. 7) was applied.

Version is a mode (in UFO terms) of a Configuration Item. The CIVersion pattern has been applied with the database version mode (Database Version) as a specialization of a version and it characterizes the Database Tuning Configuration Item. The Database Version in cludes versions of objects that compose the database and can be configured to tune the database, such as: columns, indexes, tables among others.

The second pattern of the Version Control group - CIVDecomposition pattern – has been applied. For each Configuration Item that is part of a Composite CI, there must be a Version that is part of a Configuration. In summary, the generalization set specializing Version into Atomic Version and Configuration is the counterpart of the generalization set specializing Configuration Item into Atomic CI and Composite CI. So, in the database tuning domain, a similar version of each configuration item defined is created in the configuration identification group. Although there are other tuning strategies, this second and the third group are detailed only for the physical design tuning concepts, involving index and materialized view. In this way, the Atomic Version mode is specialized in Configurable Column Version, Configurable Index Version, Configurable Table Version and Configurable View Version; and the Configuration mode is specialized in Database Tuning Configuration. All these versions correspond to configuration items defined in the previous group: Configurable Column, Configurable Index, Configurable Table, Configurable View and Configurable Database, respectively.

As baseline is in the scope, the CIVBaseline pattern has been extended with Database Snapshot. In the database domain, the closest concept that can serve as a baseline is a database snapshot. Database snapshot is the structure, constraints and instances of a database at a particular moment in time. For example, the Database Tuning Configuration Manager selects/creates a data structure s/he wants. In addition, the configuration manager creates a baseline (Database Physical Schema Snapshot) of the database before any updates, so that s/he can restore the database if a problem occurs. As there is no equivalent concept of markup semantics in the database tuning domain, we created and named it Database Markup concept.

![](/api/attachments/4VCGGBAC/fulltext/images/befd94dcc90836b61e883dc0934c0c48830d0d0e0826da2436e3990eae9799f7.jpg)  
Fig. 7. Fragment of version control group applied to database tuning configuration model.

The last pattern CIVMode distinguishes the version types (variant and revision). The Database Version has been classified as Database Variant Version (e.g. parallel versions of the same database according to the environment applied - development, acceptance and production environments) and Database Revision Version (e.g. replaced version of database in the same environment).

In the next step, the patterns of the Change Control group were used (Fig. 8).

Since there is no adaptation to be made to the change control man agement for the database tuning task, most of the concepts were specialized with names similar to those in the patterns. The CIVCRequest pattern models the change request regarding, for example, data struc ture maintenance (e.g. index creation or index rebuild). The change could be any DB Tuning Change (e.g. execution of a Data Definition Language command to create an index). So, in a DB Tuning Change, the DB Tuning Requester does a DB Tuning Change Request about a DB Version Submitted For Tuning. The cardinality between DB Tuning Change Request and DB Version Submitted For Tuning was restricted for our domain (1) because at this point, it is important to know to which Database Version the DB Tuning Change applies. If the cardinality was maintained as 1..\*, then it would not be possible to know at this point which Database Version would be changed.

![](/api/attachments/4VCGGBAC/fulltext/images/cbfc4ca25c04cf16629e71b0d42c6f169be2a2349f11ca2b772029641cf1a866.jpg)  
Fig. 8. Fragment of change control group applied to database tuning configuration model.

The CM task ontology collapses two different concepts (problem and solution) in the Change Request concept. In our database tuning domain, a database user can raise a problem thinking it is a database tuning problem. It is not necessary to register who raised the problem, as it is not relevant to our domain. But, for example, the Database Adminis trator can evaluate (CIVCREvaluation pattern) and verify that it is only a lock transaction problem. In this scenario, it is not necessary to issue a DB Tuning Change Request. For this reason, we opted to separate the problem from the possible solution, where the problem is the Perfor mance Improvement Need and the solution is the DB Tuning Change Request concept. In addition, only the human agent (Database Administrator) has knowledge and can evaluate this problem (Per formance Improvement Need Evaluation), generating the role of Evaluated Performance Improvement Need, that requests (or not) the DB Tuning Change Request (solution) after the evaluation.

Once there is an agreement about the DB Tuning Change, the CIVCheckout pattern can be applied. In the database tuning domain, there are no concepts equivalent to checkout and check-in. Nevertheless, these concepts seem to be very important when there is a collaborative scenario in which many DBAs can tune the same database, or when the DBA wants to make a database version unavailable for changes by others. So, these concepts were imported from the configuration man agement domain into the database tuning domain. The DB Tuning Executor does a DB Check-Out. When it occurs, the Database Version takes on the role of Checked-Out DB Version. Similarly, the DB Tuning Change takes on the role of On Going DB Tuning Change.

The database environment is actually changed (Modification Rela tor) using the CIVCRExecution pattern. The DB Tuning Executor sub mits a DB Tuning Execution (e.g. create index). When this execution is done, the Database Version assumes the role of Modified DB Version. After the execution, this change needs to be registered. The pattern responsible to register this change is the CIVCheckin pattern. At this moment, the DB Tuning Executor executes the DB Check-In, making DB Tuning Execution as a Registered DB Tuning Execution and the DB Tuning Change as an Implemented DB Tuning Change.

Finally, the DB Tuning Verifier (a person or the system itself) can verify (DB Tuning Verification) whether or not the change was successful (CIVCRVerification pattern). This verification can be done through queries submitted to the database metadata (e.g. new param eter value or new access structure). After the verification, the imple mented DB Tuning Change assumes the role of the Verified DB Tuning Change.

## 5.3. Database tuning model instance example

A possible instantiation of the Tun-O model, as a proof of concept, is the Database Self-Tuning task for physical design tuning. In section 5.3.1., we present a real application, and in section 5.3.2, we describe the Tun-O model working with two database tuning strategies (index and materialized view).

## 5.3.1. ENEM database

In Brazil, most universities accept the national high school exam (ENEM) as a form of entry. This exam consists of 4 tests (Human Sci ences, Natural Sciences, Languages, and codes, Mathematics), taken by students on two days. On average, 7 million students take this exam each year. The federal government makes the data from the tests available anonymously and in a comma-separated values (CSV) format. The analysis of the available data is very important at different levels for distinct stakeholders: public managers assess the performance of the students from all schools of a state or city, school principals and edu cators monitor the students of a specific school for marketing purposes, to advertise its ranking among all secondary schools of a specific region. These analyses, however, are challenging due to the enormous amount of data per year and the format available. To reproduce these data analyses, we inserted the ENEM data between the years of 2015–2019 in a relational DBMS.<sup>1</sup> Five distinct databases were created (one per year), containing the following amount of data: the 2015 database contained 105 GB of data, the 2016 database contained 102 GB of data, the 2017 database contained 81 GB of data, the 2018 database contained 70 GB of data, and the 2019 database contained 78 GB of data.

Although data analysis has been facilitated by the use of a relational DBMS, the large volume of data made available makes it impossible to quickly respond to users’ statistical queries, requiring tuning strategies.

## 5.3.2. Tuning ENEM database using Tun ${ \mathrm { - } } O _ { C M }$ model

Fig. 9 presents a query that had a slow response (5:08 min) when submitted to the 2015 database. This query counts the number of registered candidates who correctly answered the questions (answer\_correct a JOIN candidate c ON (a.fk\_candidate\_- subscription = c.pk\_subscription\_number)) of the Human Sciences test $( \mathsf { a } . \mathsf { f k } _ { - } \mathsf { a r e a } = \mathsf { \Omega } ^ { \prime } \mathrm { H C } ^ { \prime } ) _ { : }$ , who studied (JOIN school s ON (c.fk\_school\_code = s.pk\_code)) at state public school (s.type = 2) in the federative unit of Rio de Janeiro $\left( \mathsf { s } \cdot \mathsf { f u } = \mathsf { \Omega } ^ { \bullet } \mathsf { R } \mathsf { J } ^ { \bullet } \right) \left( \mathsf { F i g } . \mathsf { \Omega } ^ { \mathsf { 9 } } \right)$

5.3.2.1. Scenario 1: index strategy. As a first tuning alternative, the heuristic defined by the DBA is managed by the $\mathrm { T u n - O _ { C M } }$ model, which registers the creation of indexes on the columns presented in the WHERE clause (test area - a.fk\_area, school type - s.type, and federative unit - s. fu). The heuristics defined and selected by the DBA establishes the reasoning for creating indexes on the WHERE clause. The DBA can define multiple heuristics at the same time. In this scenario, the chosen heuristics change the database configuration by adding only indexes. Fig. 10 shows an instance example of the change control group about the new design with these indexes.

In the first moment (identification need), a database user indicates a database performance problem. This problem is instantiated with the name Need01 and refers to the slow query (hasQuery property) that caused the database performance problem. During the evaluation need moment. the human database administrator DBA01 (Carol) evaluates the need (Evaluation01) and concludes that it is, in fact, a database tuning problem. At this moment, Need01 plays the role of an evaluated performance improvement need.

From that moment on, the decisions to take all actions are made automatically, without DBA interference. In the change request moment, Agent01(AgentHeur1) requests the solution (CRequest01) about the CDB01 – DB\_ENEM database version, which plays the DB version submitted for the tuning role. The solution request (CRequest01) mediates the DB tuning change, and this version originated from the Need01. The DB tuning change Change01 involves creating new indexes on the test area, school type, and school columns’ federative unit (configurable indexes).

During the check-out moment, the executor Agent01 (AgentHeur1) is responsible for checking-out the database version. In the check-out process (Checkout01), Change01 assumes the ongoing DB tuning change role, and we have the DB version submitted for tuning (CDB01 –

```sql
SELECT c.fk_school_code, s.name, a.fk_question_id, count(*)
FROM answer_correct a
JOIN candidate c
ON (a.fk_candidate_subscription = c.pk_subscription_number)
JOIN school s
ON (c.fk_school_code = s.pk_code)
WHERE (a.fk_area = 'HC') and (s.type = 2) and (s.fu = 'RJ')
GROUP BY c.fk_school_code, s.name, a.fk_question_id;
```  
Fig. 9. Slow query example

DB\_ENEM) the checked-out DB version role. After the check-out, changes are then executed. The change execution (Execution\_01) com prises the database version receiving the modified DB version role (CDB01 – DB\_ENEM). When the change execution is finished, it is registered (Execution01) through the check-in (Checkin01), and the change is implemented (Change01).

Finally, the software agent assumes the role of verifier (Agent01 - AgentHeur1) to check (Verification01) if the database tuning actions were successful through accessing the database metadata submitting queries to the pg\_indexes view of PostgreSQL DBMS (select \* from pg\_indexes;). When it is confirmed, the implemented change (Change01) assumes the role of verified DB tuning change.

Once a database tuning change has been made, the Agent01 (Agen tHeur1) needs to maintain the version control about the database ver sions. For example, the versions of the configurable database CDB01, the configurable columns (fk\_area, type, and fu), the configurable tables (answer\_correct and school), and the configurable indexes (CIndex01, CIndex02, and CIndex03). These versions are database revision versions because the objects are replaced.

After the index creation, the query did not decrease the execution time, probably because of the aggregation function that induces the optimizer to scan the tables involved.

5.3.2.2. Scenario 2: materialized view strategy. The query of Fig. 9 pre sented a high frequency in our database, varying only in the value of the school type (1- federal public, 2- state public, 3- municipal public or 4- private) and federative unit columns. Brazil has 27 federative units. In a second step, with an usual non I/O-bound context taken into account, there is another heuristic’s agent (AgentHeur2) that decided to create a generic materialized view that is rarely updated and could meet the set of queries requirements similar to that presented in Fig. 9, since this query involves aggregation of values. The proposed materialized view is shown in Fig. 11.

Fig. 12 shows an instance example of the change control group about the new configuration with this materialized view.

Queries were rewritten, such as: SELECT \* FROM mv\_sch\_quest\_correct\_ch where fu = ‘RJ’ and type =2;. After this configuration change, the query decreased the response time to 5 s 521 msec.

5.3.2.3. Scenario 3: reflection on database tuning strategies used. After a while, the DBA team consulted the $\mathrm { T u n - O _ { C M } }$ model and found that the same query generated two different database tuning strategies (index and materialized view). When generating the query execution plan (Fig. 13), the DBAs found that indexes generated in scenario 1 were not used for the query that originated them. As no other query was included in the model as being benefited by these indexes, the DBAs chose to remove them, since there is a benefit generated by the materialized view (scenario 2) and indexes were only taking up disk space.

Three benefits provided by the model should be noted:

1. The identification of the source of the non-beneficial tuning action.

2. The comparison of database configuration versions.

3. The stability of a better configuration version for the database (less space and less impact on inserts) was only possible because of the Tun- $\cdot 0 _ { \mathrm { C M } }$ model’s use that provided the registration of the actions and their provenance. In case of a better index configuration (sce nario 1), the $\mathrm { T u n - O _ { C M } }$ model would also allow the database to return to the previous design more quickly than using restore, requiring the DBA to undo all actions of the last version.

It is worth noting that this work does not aim to evaluate the tuning heuristics’ effectiveness but demonstrate its management. This man agement enables collaborative and organized work as seen through the example scenarios described using the Tun $- \mathrm { O } _ { \mathrm { C M } }$ model, where it is possible to identify the provenance of the tuning decisions, discuss such choices, and adjust the environment according to stable and more beneficial configurations.

![](/api/attachments/4VCGGBAC/fulltext/images/8a5558205b9a1fe0fc91eaa9086f1a245a75d181fd92dccd2a03efab5b23e395.jpg)  
Fig. 10. Instance example of the change control group - indexes created.

![](/api/attachments/4VCGGBAC/fulltext/images/d26c2020ee2a0fccd02db179f4786cfcb0fe7ccf0b2f6e017e083c4ec1d2d329.jpg)  
Fig. 11. Materialized View created.

![](/api/attachments/4VCGGBAC/fulltext/images/91a855dbdab40057416d291ef12c1f5745e5c971b652db35bf50857a21dab023.jpg)  
Fig. 12. Instance example of the change control group - materialized view created.

## 6. Discussion

The instances of the Tun-O model precisely describe which changes were made to each check-in performed. For example, CheckIn01 creates three indexes (CIndex01, CIndex02, and CIn dex03) and CheckIn02 creates a materialized view. Thus, it is possible to analyze the tuning actions that may impact existing structures. For example, if it is detected that after the last check-in, some old index is no longer used, it is possible to analyze which actions (indexes or materi alized view) are acting on the same indexed attribute set. An example would be an old index on a column that already exists in the newly created materialized view. It may be that the optimizer prefers to rewrite some queries in the database workload to use the materialized view rather than the existing index, making it unnecessary. Without this moment-by-moment control, the analysis would become much more complex, thus hindering understanding and decision-making. Another advantage that configuration management concepts bring to database tuning is that they enable database snapshots (CDB01), allowing the

```txt
"Finalize GroupAggregate (cost=5530183.47..6245374.73 rows=5772527 width=46)"
" Group Key: c.fk_school_code, s.name, a.fk_question_id"
" -> Gather Merge (cost=5530183.47..6139545.06 rows=4810440 width=46)"
" Workers Planned: 2"
" -> Partial GroupAggregate (cost=5529183.45..5583300.90 rows=2405220 width=46)"
" Group Key: c.fk_school_code, s.name, a.fk_question_id"
" -> Sort (cost=5529183.45..5535196.50 rows=2405220 width=38)"
" Sort Key: c.fk_school_code, s.name, a.fk_question_id"
" -> Hash Join (cost=140941.15..5142720.34 rows=2405220 width=38)"
" Hash Cond: (a.fk_candidate Subscription = c.pk Subscription number)"
" -> Parallel Seq Scan on answer correct a (cost=0.00..4367434.50 rows=44953470 width=12)"
" Filter: (fk_area = 'HC')"
" -> Hash (cost=134361.30..134361.30 rows=309028 width=42)"
" -> Hash Join (cost=824.23..134361.30 rows=309028 width=42)"
" Hash Cond: (c.fk_school_code = s.pk_code)"
" -> Seq Scan on candidate c (cost=0.00..118375.27 rows=5775727 width=12)"
" -> Hash (cost=803.31..803.31 rows=1674 width=34)"
" -> Seq Scan on school s (cost=0.00..803.31 rows=1674 width=34)"
" Filter: ((s.type = 2) AND (s.fu = 'RJ'))"
```  
Fig. 13. Execution plan of slow query (not rewritten).

DBA to return the database to previous states that may be more stable o more performative. Finally, $\mathrm { T u n - O _ { C M } }$ records each person/agent responsible for each step of configuration management, allowing for technical discussions among the tuning DBA team members in case of tuning action disagreements, as well as increased auditability. This scenario allows for better-informed discussions, favoring collaborative team work in order to facilitate decision-making and make it more reliable.

In summary, the main benefits of Tun-O in relation to other tuning tools [1–6] are: (i) maintenance of the origin of the decisions through the registration of versions of the DBMS configurations; (ii) easiness of future audits of the databases configurations; (iii) definition of concepts that are common to several database technologies (relational, object relational and noSQL); (iv) easiness in the identification of the actions that need to be undone to return the DBMS to a previous and more stable configuration (imagining a database with more than 50 TB, the restore task would be more costly).

## 7. Conclusion

OPL notoriously facilitates the reuse of models and ontologies frag ments by providing a path towards (re)use of predefined patterns. We may use such patterns to improve correctness by adding models that are more precisely specified through ontologies. The configuration task is commonly present, in some sort, in many systems and may help in the database tuning decision-making. In this work, CM-OPL was applied to develop Tun-O , a database tuning conceptual model used by a tool to help DBAs experiment with different tuning heuristics. Tun-O improved the understanding and transparency of the decisions made by tuning heuristics, provided a means to address this complex task’s explainability, and enriched the discussions held in a DBA team.

Although CM-OPL has been extracted from the ontology that initially sees the configuration as a task for the software development, we can also apply it to the feature configuration task. There are many activities and concepts in common among these tasks.

As future work, we plan to explore CM-OPL in other software areas and develop a software tool to automate the OPL process of building new ontologies requiring a configuration task. Besides, we plan to identify more patterns and apply them to the database log control task. This way, we would add semantics to logs, and we could make them more explainable and self-explanatory, paving the way to automate decisions based on database logs. For example, when we detect a lock, the causing transaction may be automatically identified and killed. The DBA may have the full explanation of how it happened (users, queries, and timestamp involved as a workflow) in a formal and more precise way. Additionally, we can identify new groups of patterns to contemplate, for example, activities present in the configuration planning phase. Finally, we can create a multilevel model to detail, for instance, the difference between the moments when the database tuning refers to the database table generic type or a specific table of a particular database.

Finally, we plan to extend the $\operatorname { T u n - O } _ { \operatorname { C M } }$ model to include the entire database administration and not just the database tuning task. For that, it would only be necessary to define the other concepts involved. For example, if the DBA wants to include the backup job, this concept would be described as a configuration item since it may be configured in several ways $( \boldsymbol { \mathrm { e } } . \boldsymbol { \mathrm { g } } . ,$ full or incremental; daily, monthly, or yearly) and need to be managed in some way. In addition, we need to define the measures (e.g., used disk space) and the changes that need to be addressed during this process by including concepts, properties, and relationships.

## Acknowledgements

The authors thank FAPERJ, CAPES and CNPq for partially supporting this work.

## References

[1] A. Pavlo, M. Butrovich, A. Joshi, L. Ma, P. Menon, D. Van Aken, L. Lee, R. Salakhutdinov, External vs. internal: an essay on machine learning agents for autonomous database management systems. in: Bulletin of the JEEE Computer Society Technical Committee on Data Engineering, 2019, pp. 32–46.

[2] Z. Ding, Z. Wei, H. Chen, A software cybernetics approach to self-tuning performance of on-line transaction processing systems, J. Syst. Softw. (2017) 247–259.

[3] N.N. Noon, J.R. Getta, Automated performance tuning of data management systems with materializations and indices, J. Comp. Commun. 4 (2016) 46–52.

[4] A.C. Almeida. A. Brayner, J.M.S.M. Filho. S. Lifschitz, R.P. Oliveira, A Non: Intrusive approach for automated physical design tuning. in: Proceedings of Brazilian Symposium on Databases (SBBD 2016). 2016, pp. 115–120. Salvador Bahia, Brazil.

[5] E. Morelli, A. Almeida, S. Lifschitz, J.M. Monteiro, J. Machado, Autonomous reindexing, in: Procs ACM Symp. on Applied Computing (SAC), 2012, pp. 893–897.

[6] L. Bellatreche, M. Schneider, H. Lorinquer, M. Mohania, Bringing together partition-ing, materialized views and indexes to optimize performance of relational data warehouses, in: Procs. Intl. Conf. Data Warehousing and Knowledge Discover (DAWAK), 2004, pp. 15–25.

[7] PostgreSQL - The PostgreSQL, Global development group. PostgreSQL 9.1.24 documentation - Chapter 18 - server configuration - 18.4. resource consumption, Retrieved from, https://www.postgresql.org/docs/9.1/static/runtime-config-reso urce.html, 2018 (accessed July 2020).

[8] R. Stair. G. Reynolds. Principles of Information Systems. Ninth ed., Course Technology, Cengage Learning. Boston, MA. USA. 2010

[9] R.K. Lahti, Group Decision Making within the Organization: Can Models Help? CSWT Reports, 1999.

[10] V. Lofti, C.C. Pegels, Decision Support Systems for Operations Management & Management Science, McGraw-Hill Book Companies, Inc., Chicago, IL, USA, 1996.

[11] R.G. Coyle, Decision Analysis, The Camelot Press Ltd, London, Great Britain, 1972.

[12] B.D. Prescott, Effective Decision-Making, Gower Publishing Company, 1980.

[13] ISO - International Organization for Standardization, ISO 10007: Quality Management - Guidelines for Configuration Management, 2017.

[14] ISO - International Organization for Standardization, ISO 14001: Environmenta management systems - Requirements with guidance for use, 2015.

[15] R.A. Falbo, G. Guizzardi, A. Gangemi, V. Presutti, Ontology patterns: clarifying concepts and terminology. in: Proceedings of the 4th Workshop on Ontology and Semantic Web Patterns. Sidney. Australia. 2013

[16] F.B. Ruy, G. Guizzardi, R.A. Falbo, C.C. Reginato, V.A. Santos, From reference ontologies to ontology patterns and back. J. Data & Knowledge Eng. 109 (C) (2017) 41-69. Elsevier Science Publishers. The Netherlands

[17] R.A. Falbo, M.P. Barcellos, F.B. Ruy, G. Guizzardi, R.S.S. Guizzardi, Ontology pattern languages, in: A. Gangemi, P. Hitzler, K. Janowicz, A. Krisnadhi, V. Presutti

(Eds.), Ontology Engineering with, Foundations and Applications. IOS Press, Ontology Design Patterns, 2016.

[18] M.P. Barcellos, R.A. Falbo, V. Frauches, Towards a measurement ontology pattern language, ONTO. COM/ODISE@FOIS 1301 (2014).

[19] R. Falbo, G.K. Quirino, M.P. Barcellos, G. Guizzardi, An ontology pattern language for service modeling, in: 31st ACM Symposium on Applied Computing (ACM SAC 2016), Pisa, Italy, 2016.

[20] R.A. Falbo, F.B. Ruy, G. Guizzardi, M.P. Barcellos, J.P.A. Almeida, Towards an enterprise ontology pattern language, in: 29th ACM Symposium On Applied Computing (ACM SAC 2014), Gyeongju, Korea, 2014.

[21] R.A. Falbo, M.P. Barcellos, J.C. Nardi, G. Guizzardi, Organizing ontology design patterns as ontology pattern languages, in: The Semantic Web: Semantics and Big Data v. 7882, 2013, pp. 61–75, of the series Lecture Notes in Computer Science.

[22] A.C. Almeida, D. Schwabe, S. Lifschitz, M.L.M. Campos, CM-OPL: an ontology pattern language for configuration management task, in: Seminar on Ontology Research in Brazil (ONTOBRAS 2018), S˜ao Paulo, SP, Brazil, 2018.

[23] A.C. Almeida, M.L.M. Campos, F. Baião, D. Schwabe, S. Lifschitz, CM-OPL: Configuration Management Ontology Pattern Language Specification - Revised Edition, Technical Report, Puc-Rio, Rio de Janeiro, Brazil, from, ftp://ftp.inf.puc-r io.br/pub/docs/techreports/18 09 almeida.pdf, 2018.

[24] G.K.S. Quirino, M.P. Barcellos, R. Falbo, OPL-ML: a modeling language for representing ontology pattern languages, Lect. Notes Comput. Sci (2017) 187–201.

[25] R.F. Calhau, R.A. Falbo, A configuration management task ontology for semantic integration, in: Proceedings of the 27th Annual ACM Symposium on Applied Computing (SAC’12), ACM, New York, NY, USA, 2012, pp. 348–353.

[26] G. Guizzardi, Ontological Foundations for Structural Conceptual Models, Universal Press, The Netherlands, 2005.

[27] X. Wang, N. Guarino, G. Guizzardi, J. Mylopoulos, Software as a social artifact: a management and evolution perspective, in: Conceptual Modeling. ER 2014. Lecture Notes in Computer Science vol 8824, Springer, Cham, 2014, https://doi. org/10.1007/978-3-319-12206-9 27

[28] R. Elmasri, S.B. Navathe, Fundamentals of Database Systems, 7th ed., Pearson, England, 2016.

[29] D. Shasha, P. Bonnet, Database Tuning: Principles, Experiments, and Troubleshooting Techniques, Elsevier, 2002.

![](/api/attachments/4VCGGBAC/fulltext/images/549b4090ac0f91f4b7ba1a5acaeae1de055498a781f13a941140696e55379138.jpg)  
in: http://lattes.cnpq.br/8306729029606464.  
Ana Carolina Almeida is an adjunct professor at the State University of Rio de Janeiro (UERJ). located in the Department of Informatics and a judicial analyst with a specialization in Informatics at the Federal Regional Court of the 2nd Region (TRF2), acting as DBA. Post-doctorate with an emphasis on Big Data at the Federal University of Rio de Janeiro (UFRJ) (Oct / 2014 to Apr / 2015). PhD in Informatics with a specialization in BD Tuning from the Pontifical Catholic University of Rio de Janeiro (PUC-Rio) (2013). Master in Systems and Computing from the Military Institute of Engineering (IME / RJ) (2006). Researcher in the database area with an emphasis on: (i) DB (auto) tuning systems and (ii) ontologies. She was a consultant in database and taught courses at Petrobras University. Details

![](/api/attachments/4VCGGBAC/fulltext/images/06417f294812cafbd0fe91f9520787847c47349176fc2b29a4216ad58d319925.jpg)

Fernanda Baiao ˜ is a professor at the Department of Industrial Engineering of the Pontifical Catholic University of Rio de Janeiro (PUC-Rio). She holds DSc (2001) and MSc (1997) de grees in Systems and Computer Engineering from COPPE/ UFRJ, Brazil, and her research topics are in the areas of Data Science, Conceptual Modeling and Ontologies, Business Process Management (BPM) and Semantic Data Integration. Fernanda has authored more tan 150 peer-reviewed publications, participated and coordinated national and international research projects, and developed valuable expertise in knowl edge transfer between the Academy and Industry in R&D pro jects on Data Science, BPM, Business Architecture, Data Management and Information Security, in the fields of Oil

Exploration and Production and Gas, Insurance, IT Service Management and Fraud Pre diction. Details in: http://lattes.cnpq.br/5068302552861597.

![](/api/attachments/4VCGGBAC/fulltext/images/771080e408891843a4fbfc7d354ac328d1018d5a55becc4f604e11a5fc8a8072.jpg)

Sergio ´ Lifschitz is an associate professor at the Department of Informatics of the Pontifical Catholic University of Rio de Janeiro (PUC-Rio). Holds a Doctor’s degree in Informatics by Ecole <sup>´</sup> Nationale Sup´erieure des T´el´ecommunications, ENST Paris, France (1994), a MSc (1990) and BSc (1986) in Electrical Engineering, both from PUC-Rio. His main research areas involve (i) autonomous computing and database systems and (ii) tools and database systems for bioinformatics applications. Details in: http://lattes.cnpq.br/8164403687403639.

![](/api/attachments/4VCGGBAC/fulltext/images/f2cd2e10183683b29b60cafa754b15421be39923ce21cc2e0bcdf46c0f783070.jpg)

Daniel Schwabe a full professor (retired) at the Department of Informatics of the Pontifical Catholic University of Rio de Janeiro (PUC-Rio). He received a PhD in Computer Science from University Of California, Los Angeles (1981). MSc in Computer Science from Pontifical Catholic University of Rio de Janeiro (PUC-Rio) (1976) and BSc in Mathematics from Pontifical Catholic University of Rio de Janeiro (PUC-Rio (1975). His research focuses on model driven design and implementation of Socio-Technical Systems, seen as menmachine teams that solve problems, with a focus on Knowl edge Graphs and inclusion of human values. Details in: http://lattes.cnpq.br/5842794652841557.

![](/api/attachments/4VCGGBAC/fulltext/images/f978f37659e7906d4f26e6a861254bea8e4ac251cbd67a7337cb8eb98922637c.jpg)

Maria Luiza M. Campos is a professor at the Department of Computer Science, Federal University of Rio de Janeiro (UFRJ). She coordinates the Knowledge Engineering Group (GRECO Group). supervising master and doctorate students at the Postgraduate Program in Informatics (PPGI/UFRJ) in the same university. She received a Ph.D. in Information Systems from the University of East Anglia (1993), M.SC. in Computer Engi neering, at Federal University of Rio de Janeiro (1984) and Bachelor in Civil Engineering, at Federal University of Rio Grande do Sul (1978). The main area of interest is heteroge neous information integration, focusing on metadata, ontol ogies, conceptual modeling, data bases, data warehousing and semantic web. Main application domains include bioinformat

ics, e-gov, e-science and emergency systems. Details in: http://lattes.cnpq.br/06596588 20912418.
