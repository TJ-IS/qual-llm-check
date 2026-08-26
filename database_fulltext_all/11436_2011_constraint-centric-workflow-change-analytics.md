---
otero_id: 11436
otero_key: "E4W4EEKC"
title: "Constraint-centric workflow change analytics"
authors: "Harry Jiannan Wang; J. Leon Zhao"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.03.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Constraint-centric work<sup>fl</sup>ow change analytics

Harry Jiannan Wang <sup>a,</sup>⁎, J. Leon Zhao

<sup>a</sup> Department of Accounting and MIS, University of Delaware, Newark, DE, United States

<sup>b</sup> Department of Information Systems, City University of Hong Kong, Kowloon, Hong Kong, China

## a r t i c l e i n f o

Article history: Received 5 March 2010 Received in revised form 7 February 2011 Accepted 1 March 2011 Available online 5 March 2011

Keywords: Work<sup>fl</sup>ow modeling Workflow constraint Work<sup>fl</sup>ow changes First order logic Business process management Change management

## a b s t r a c t

In a globalized economic environment with volatile business requirements, continuous process improvement needs to be done regularly in various organizations. However, maintaining the consistency of work<sup>fl</sup>ow models under frequent changes is a signi<sup>fi</sup>cant challenge in the management of corporate information services. Unfortunately, few formal approaches are found in the literature for managing work<sup>fl</sup>ow changes systematically. In this paper, we propose an analytical framework for work<sup>fl</sup>ow change management through formal modeling of work<sup>fl</sup>ow constraints, leading to an approach called Constraint-centric Work<sup>fl</sup>ow Change Analytics (CWCA). A core component of CWCA is the formal de<sup>fi</sup>nition and analysis of work<sup>fl</sup>ow change anomalies. We operationalize CWCA by developing a change anomaly detection algorithm and validate it in the context of procurement management. A prototype system based on an open-source rule engine is presented to provide a proof-of-concept implementation of CWCA.

© 2011 Elsevier B.V. All rights reserved

## 1. Introduction

To be competitive in the global market, companies need to quickly adapt their business processes to various changes in the business environment, such as mergers/acquisitions, new regulations, and new customer demand. Various changes can occur in different work<sup>fl</sup>ow perspectives including control <sup>fl</sup>ow, data <sup>fl</sup>ow, organizational model, and work<sup>fl</sup>ow constraints. For instance, process reengineering or supply chain recon<sup>fi</sup>guration can lead to the alteration of task execution sequences and removal of non-value-added tasks, i.e. control <sup>fl</sup>ow changes. Mergers/ acquisitions can result in resource reallocation and organization restructuring, i.e. organizational model changes. New governmental regulations such as the Sarbanes-Oxley Act may require new and revised business rules to be compliant, i.e. work<sup>fl</sup>ow constraint changes.

Existing research on work<sup>fl</sup>ow changes tends to focus on a limited number of perspectives of work<sup>fl</sup>ow, mostly control <sup>fl</sup>ow and data <sup>fl</sup>ow, paying little attention to dependencies among all work<sup>fl</sup>ow perspectives [13,15,22,29,40,44,45,53]. For example, industrial reorganization such as mergers/acquisitions may result in removing certain organizational roles, i.e. an organizational model change. Consequently, tasks assigned to those roles must be delegated to other resources, and the relevant work<sup>fl</sup>ow constraints must be revised properly; otherwise, a runtime role resolution error might occur and the corresponding tasks will not be executed. Given these frequent changes in business work<sup>fl</sup>ows, managing multiperspective work<sup>fl</sup>ow changes is imperative in order to support business operations and continuous process improvement ef<sup>fi</sup>ciently.

Many process modeling speci<sup>fi</sup>cations have been used in practice, such as UML activity diagrams, BPMN, and Event-driven Process Chains (EPCs), but these speci<sup>fi</sup>cations usually lack analytical capability and therefore cannot be used to formally model and analyze work<sup>fl</sup>ow changes. Formal languages have been applied to model work<sup>fl</sup>ows, such as Petri nets [1,34,52], Metagraphs [5], Communicating Sequential Processes (CSP) [58], formal logic [10,21], and PI Calculus [46]. In addition, several rule languages have been applied to analyze work<sup>fl</sup>ow constraints and specify work<sup>fl</sup>ow exceptions [9,13–15]. Nevertheless, little research is found on formal approaches that focus on work<sup>fl</sup>ow change analysis treating a work<sup>fl</sup>ow system as a whole.

In this paper, we aim to <sup>fi</sup>ll this research gap by proposing an analytical framework for managing multi-perspective work<sup>fl</sup>ow changes via formal modeling of work<sup>fl</sup>ow constraints, referred to as Constraint-centric Work<sup>fl</sup>ow Change Analytics (CWCA). The contributions of this paper are as follows. First, we propose a novel constraint-centric approach to analyzing multi-perspective work<sup>fl</sup>ow changes by specifying work<sup>fl</sup>ow change operations and dependencies formally. Second, we apply First Order Logic to formally de<sup>fi</sup>ne work<sup>fl</sup>ow change anomalies and develop an algorithm to detect those anomalies. Third, we validate the CWCA framework through a prototype system that provides insights into the integration of CWCA with existing work<sup>fl</sup>ow management systems and rule engines.

The rest of the paper proceeds as follows. We <sup>fi</sup>rst review the relevant literature in Section 2. Then, we discuss the types of work<sup>fl</sup>ow changes and their dependencies in Section 3. In Section 4, we present a procurement process as a running case for the paper and propose a constraint-centric work<sup>fl</sup>ow modeling framework to specify different work<sup>fl</sup>ow perspectives for formal work<sup>fl</sup>ow change analysis. In Section 5, we formally de<sup>fi</sup>ne and analyze work<sup>fl</sup>ow change anomalies and develop an anomaly detection method. A proof-of-concept system is also presented to demonstrate CWCA and validate the anomaly detection algorithm. We compare our framework with some other related approaches and discuss its limitations in Section 6. Finally, we conclude in Section 7 by summarizing our contributions.

## 2. Literature review

The structural perspective of work<sup>fl</sup>ow modeling is captured by control <sup>fl</sup>ow [49]. A control <sup>fl</sup>ow model usually indicates the tasks, their execution sequences, and the corresponding transition conditions. There have been extensive research efforts on control <sup>fl</sup>ow modeling, resulting in many process modeling methods. UML activity diagrams, EPCs, and BPMN are widely adopted graphical business process modeling standards. However, they lack a rigorous mathematical foundation and therefore have limited analytical capability. Petri nets have been used to represent and analyze process models [1,52]. A number of Petri nets extensions have been proposed including timed Petri nets and colored Petri nets, which have been used to model data <sup>fl</sup>ow, temporal constraints, and work<sup>fl</sup>ow events [8,28,34]. Many work<sup>fl</sup>ow structural properties such as reachability, deadlock, and livelock, can be formally veri<sup>fi</sup>ed using Petri nets. Tools have also been developed to support Petri-nets-based work<sup>fl</sup>ow modeling and simulation such as CPN Tools (http://wiki.daimi.au.dk/cpntools) and YAWL (http://www.yawl-system.com/). Metagraphs are another rigorous process modeling approach with mathematical foundation and strong analytical capability [5]. Metagraphs provide three different views of a process model, namely, task view, data view and resources view and are able to analyze interactions among those three views via matrix computations [5]. Various logic formalisms have also been applied to work<sup>fl</sup>ow modeling and analysis, such as propositional logic, temporal logic, event algebra, and concurrent transaction logic [10,21,38]. One unique feature of logic-based approaches is the capability to model and enforce various constraints on task dependency and execution orders. Communicating sequential process (CSP) [58] and Pi-calculus [46] have also been applied to represent work<sup>fl</sup>ow, where model checking techniques can be used to verify certain work<sup>fl</sup>ow properties.

Organizational modeling in work<sup>fl</sup>ow has been identi<sup>fi</sup>ed as an important research area in business process management [7], which provides the organizational context of work<sup>fl</sup>ow applications. Several organizational meta-models have been proposed to make work<sup>fl</sup>ow management systems more “organizational aware” [61]. The speci<sup>fi</sup>cation and validation of data <sup>fl</sup>ow in work<sup>fl</sup>ow system is critical, because data <sup>fl</sup>ow anomalies may prevent work<sup>fl</sup>ows from proper execution if not detected prior to work<sup>fl</sup>ow deployment [45,50]. Speci<sup>fi</sup>cally, Sun et al. (2006) identify three types of data anomalies, namely missing data, redundant data, and con<sup>fl</sup>icting data, and propose a data anomaly veri<sup>fi</sup>cation algorithm. The proper execution of work<sup>fl</sup>ows requires authorization constraints to enforce the assignment of tasks to organizational resources, such as human users, roles, organization units, or machine agents [15]. Different mechanisms have been proposed to specify and enforce work<sup>fl</sup>ow authorization constraints, such as Secure Petri Nets [3], logic-based constraint speci<sup>fi</sup>cation [9] and ECA (event-conditionaction) rules [15].

Curtis et al. proposed four perspectives in process representation, namely, functional, informational, organizational, behavioral perspectives [19]. Functional perspective models what process elements are being executed. and what flows of informational entities. are relevant to the process elements. Informational perspective speci<sup>fi</sup>es the informational entities produced or manipulated by a process. Organizational perspective de<sup>fi</sup>nes where and by which agents in the organizational model that process elements are performed. Behavioral perspective concerns with when and how process elements are performed through different work<sup>fl</sup>ow structures. In this paper, the four perspectives are substantiated via control <sup>fl</sup>ow, data <sup>fl</sup>ow, and organizational model, and work<sup>fl</sup>ow constraints, which are well-known concepts in work<sup>fl</sup>ow modeling. More speci<sup>fi</sup>cally, control <sup>fl</sup>ow is related to both the functional and behavioral perspectives; data <sup>fl</sup>ow mainly models the informational perspective, organizational model speci<sup>fi</sup>es the organizational perspective; and work-<sup>fl</sup>ow constraints serve as the glue to all four perspectives.

Another related research area is business rules research. Many rule representation languages have been developed to express business rules, enable rule reasoning, and facilitate rule extraction, reuse and integration [14,41]. There have been extensive implementation efforts in rule engines and development tools, such as JESS, CLIPS, and Drools. As a key enabling technology for process management, work<sup>fl</sup>ow technology has been applied in services computing research areas such as web services orchestration and choreograph [60], web-service-based process integration [11], and web-service-enabled process management for collaborative commerce[16]. A number of languages have been proposed to describe the process models of web services, such as Business Process Execution Language (BPEL) for web service orchestration [2], Web Services Choreography Description Language (WS-CDL) for web service choreography [30], XML Process Description Language (XPDL) for business process de<sup>fi</sup>nition interchangeability [57], and First-order Logic Ontology for Web Services (FLOWS) [51]. In particular, FLOWS is developed by extending the Process Speci<sup>fi</sup>cation Languages (PSL) [25], which is based on First Order Logic. The goal of FLOWS is to enable reasoning about web service semantics by providing a fully expressive language and framework for modeling semantic aspects of service behavior [26]. Nevertheless, none of the languages list above is designed for analyzing multi-dimensional work<sup>fl</sup>ow changes. Our research in this paper leverages First Order Logic to model work<sup>fl</sup>ow changes and change consequences among different work<sup>fl</sup>ow perspectives, which can be incorporated into other languages and frameworks, e.g. FLOWS, to provide analytical capability for handling work<sup>fl</sup>ow changes.

Organizations are recognizing that work<sup>fl</sup>ow management systems must be able to adapt ef<sup>fi</sup>ciently to changes in business in order to realize the real power of process automation [29]. As such, research in dynamic and adaptive work<sup>fl</sup>ow has received much attention [12,40]. Sadiq et al. (2000) found that changes to work<sup>fl</sup>ow models are often permanent as the result of process improvement, process reengineering, merger/acquisitions, etc., whereas changes in work<sup>fl</sup>ow instances are usually due to unforeseen and rare situations in process operations. They de<sup>fi</sup>ned <sup>fi</sup>ve work<sup>fl</sup>ow modi<sup>fi</sup>cation policies to cope with work<sup>fl</sup>ow changes, namely, Flush, Abort, Migrate, Adapt, and Build [44]. Change management involves thorough analysis of process structure and current process status in order to avoid process errors known as “dynamic change bugs” [53]. Several mathematical models have been proposed to formally represent work<sup>fl</sup>ow dynamic changes and identify “safe” ways to migrate existing instances without incurring dynamic change bugs [22,40,53]. Change adaptation means that there are some instances that need to be treated differently due to exceptions de<sup>fi</sup>ned as “deviations from an ideal collaborative work<sup>fl</sup>ow process caused by errors, failures, resources or requirements changes” [31]. Different methods for exception speci<sup>fi</sup>cation and handling have been proposed in the literature, such as knowledge-based approach [31], active rule based approach [13], and meta modeling approach [17].

In sum, most previous works have focused on some limited perspectives of work<sup>fl</sup>ow changes such as those in terms of control <sup>fl</sup>ow and data <sup>fl</sup>ow, leaving out other important perspectives such as changes in organizational models and work<sup>fl</sup>ow constraints. In addition, research on formal approach to analyzing multi-perspective work<sup>fl</sup>ow changes has been scant. As such, systematic and comprehensive multi-perspective change management features are virtually not found in existing work<sup>fl</sup>ow management systems.

## 3. Work<sup>fl</sup>ow changes and dependencies

In this section, we <sup>fi</sup>rst discuss various changes in different work<sup>fl</sup>ow perspectives, including control <sup>fl</sup>ow, data <sup>fl</sup>ow, organizational model, and work<sup>fl</sup>ow constraints. Then, we show how work<sup>fl</sup>ow consistency can be affected by the interactions among those changes, which we refer to as change dependencies.

## 3.1. Workflow perspectives and changes

A work<sup>fl</sup>ow model can be studied from four perspectives, namely, control <sup>fl</sup>ow, data <sup>fl</sup>ow, organizational model, and work<sup>fl</sup>ow constraints [49]. Control <sup>fl</sup>ow concerns the execution orders of tasks. Five basic routing patterns, namely, sequence, fork, join, branch, and merge can be used to model most commonly used business processes, as shown in Fig. 1. Sequence means that tasks are executed sequentially. Fork and Join are used to model parallel routing. Branch and Merge are used to model conditional routing. More thorough studies of control <sup>fl</sup>ow constructs can be found on work<sup>fl</sup>ow patterns [54]. Data <sup>fl</sup>ow describes data items that are consumed, produced and transferred by tasks and routing constructs and their dependencies. Organizational model de<sup>fi</sup>nes work<sup>fl</sup>ow-related resources, such as users, roles, organization units, machine agents, and applications, and their relationships. Work<sup>fl</sup>ow constraints serve as a hub that connects the aforementioned three perspectives by specifying rules for work<sup>fl</sup>ow execution, such as routing rules at branching nodes, assigning resources to tasks, and relating data items to tasks.

At the conceptual level, various work<sup>fl</sup>ow changes can be classi<sup>fi</sup>ed into three basic operations to different work<sup>fl</sup>ow perspectives, namely, insertion, deletion, and modification. Some work<sup>fl</sup>ow change examples using this classi<sup>fi</sup>cation are listed in Table 1. Given different work<sup>fl</sup>ow perspectives are related to one another, changes in one perspective can have signi<sup>fi</sup>cant impact on other perspectives. For instance, removing an organizational resource can cause all tasks depending on that resource unable to complete, i.e. an organizational model change leading to a control <sup>fl</sup>ow anomaly. Such work<sup>fl</sup>ow change anomalies must be detected and corrected to avoid costly run-time work<sup>fl</sup>ow errors. As aforementioned, control <sup>fl</sup>ow, data <sup>fl</sup>ow, and organizational model are connected to one another via work<sup>fl</sup>ow constraints, and therefore changes in one work<sup>fl</sup>ow perspective can only affect other perspectives through work<sup>fl</sup>ow constraint changes, i.e. multi-perspective workflow change anomalies are essentially workflow constraint anomalies. As a result, we suggest treating formal analysis of change dependencies between work<sup>fl</sup>ow constraints and other work<sup>fl</sup>ow perspectives as the core issue of work<sup>fl</sup>ow change management. This idea lays the foundation of our CWCA approach and is a cornerstone of our research.

## 3.2. Workflow change dependencies

Fig. 2 shows dependencies between work<sup>fl</sup>ow constraints and other three work<sup>fl</sup>ow perspectives. These dependencies illustrate how changes in one work<sup>fl</sup>ow perspective can affect work<sup>fl</sup>ow constraints, leading to work<sup>fl</sup>ow change anomalies.

• Workflow Change Dependency 1 (C–W Change Dependency). Control <sup>fl</sup>ow changes can result in work<sup>fl</sup>ow constraint anomalies. In particular, insertion, deletion, and modi<sup>fi</sup>cation of tasks or routing constructs in a control <sup>fl</sup>ow can all lead to anomalies. For example, adding a new task requires new constraints to assign resources to the new task, and otherwise the new task cannot be executed. Deleting a routing construct such as a Branch or changing a Branch into a Fork construct can make the related routing constraints redundant.

• Workflow Change Dependency 2 (D–W Change Dependency). Removing or modifying existing data items can cause work<sup>fl</sup>ow constraint anomalies. Constraints de<sup>fi</sup>ned on data items may become invalid or redundant when data items change. For example, a routing constraint may de<sup>fi</sup>ne that if the value of a data item $d _ { 1 }$ is greater than 1000 then execute task $t _ { 1 } . \operatorname { I f } d _ { 1 }$ is removed or the name of $d _ { 1 }$ is modi<sup>fi</sup>ed, this routing constraint becomes invalid. Adding data items does not affect existing work<sup>fl</sup>ow constraints because we assume that new data items are not speci<sup>fi</sup>ed in the existing work<sup>fl</sup>ow constraints.

• Workflow Change Dependency 3 (O–W Change Dependency). Work<sup>fl</sup>ow constraint anomalies can occur when removing or modifying existing resources in an organizational model. A control <sup>fl</sup>ow is tied to the organization model via resource assignment constraints. When an organizational model changes, work<sup>fl</sup>ow constraints are also subject to change in order to be consistent. For instance, a constraint may state that task “Purchasing” is handled by a “Purchasing Clerk”. This constraint becomes invalid and needs to be revised if the role “Purchasing Clerk” is either removed or renamed due to organization restructuring.

• Workflow Change Dependency 4 (W–W Change Dependency). Work<sup>fl</sup>ow constraints can relate to one another, and therefore changes in one constraint may have impact on other constraints. For example, a “binding of duties” constraint may specify that task “Prepare documents” and task “Send documents” must be handled by the same person [14]. This constraint can never be evaluated to true if the roles assigned by authorization constraints to both tasks do not have any users in common.

The four work<sup>fl</sup>ow change dependencies further illustrate that work<sup>fl</sup>ow constraint perspective is the center of work<sup>fl</sup>ow changes. Given that control <sup>fl</sup>ow, data <sup>fl</sup>ow, and organizational model are connected via work<sup>fl</sup>ow constraints, the four types of work<sup>fl</sup>ow changes provide a complete classi<sup>fi</sup>cation of work<sup>fl</sup>ow changes. Note that there may be change dependencies within a single work<sup>fl</sup>ow perspective, e.g. one data item depends on another data item. These intra-perspective work<sup>fl</sup>ow changes are not the focus of this paper and thus are not emphasized in this paper. In order to formally analyze work<sup>fl</sup>ow constraint changes and anomalies, we propose a constraint-centric work<sup>fl</sup>ow modeling framework as presented next.

(a) Sequence  
![](/api/attachments/E4W4EEKC/fulltext/images/795be6859db3d2efef9a101660b5295c0ee47f9c0c182db97af10238a988c878.jpg)

![](/api/attachments/E4W4EEKC/fulltext/images/8ca6c487718c4208e3b4a8d4cb8e13847f00bfb401662cf4aca9b936a0812a62.jpg)

![](/api/attachments/E4W4EEKC/fulltext/images/8e309d4fa570cf286499c89177d1a0c5894c472e1128f93c82e6c6e3d9508572.jpg)

![](/api/attachments/E4W4EEKC/fulltext/images/959f0b238876e0dddf0bb3f5c12c6ac27ca1607877ed90c812285a2dd762c88d.jpg)  
(d) Branch

![](/api/attachments/E4W4EEKC/fulltext/images/9abaa7842514095b5fa2053c7c8d53bcbff1a9923c77fe1bf5de067b77efb54a.jpg)  
Fig. 1. Basic routing patterns  
(e) Merge

Examples of work<sup>fl</sup>ow changes.

<table><tr><td></td><td>Insertion</td><td>Deletion</td><td>Modification</td></tr><tr><td>Control flow</td><td rowspan="2">Adding tasksAdding a routing constructsHire new employeeCreate new positionsForm new departments</td><td rowspan="2">Remove tasksRemove routing constructsEmployee terminationsRemove positionsRemove departments</td><td rowspan="2">Change task execution orderChange sequential execution into parallel executionReassign employees to a new positionsRestructure the organization</td></tr><tr><td>Organizational Model</td></tr><tr><td>Data flow</td><td>Adding new data item</td><td>Remove data item</td><td>Update data item values</td></tr><tr><td>Workflow Constraints</td><td>Specify new routing rulesAssign additional resources to tasks</td><td>Remove resources from task executionRemove routing constraints</td><td>Revise routing conditionsRevise resource assignment rule</td></tr></table>

## 4. Constraint-centric work<sup>fl</sup>ow modeling

In this section, we <sup>fi</sup>rst present a procurement management case to illustrate various work<sup>fl</sup>ow constraints. Then, we formally de<sup>fi</sup>ne the four work<sup>fl</sup>ow perspectives, i.e. control <sup>fl</sup>ow, data <sup>fl</sup>ow, organizational model, and work<sup>fl</sup>ow constraint, using First Order Logic, which provides a formal framework for analyzing work<sup>fl</sup>ow changes.

## 4.1. A procurement management case

Procurement is a very important step in supply chain management, which involves many functional areas such as purchasing, inventory management, and warehouse operations [18]. A procurement work<sup>fl</sup>ow is given as a UML activity diagram in Fig. 3. This work<sup>fl</sup>ow is developed by simplifying the procurement process from SAP process reference models presented in [18].

The tasks in this procurement work<sup>fl</sup>ow are described in Table 2. Related data items include: $d _ { 1 } -$ supervisor approval, $d _ { 2 }$ — item total value, $d _ { 3 } -$ available fund, $d _ { 4 } -$ mgmt approval, $d _ { 5 } - \mathrm { r e q u e s t e d }$ item quantity, and $d _ { 6 } -$ requested item inventory. Fig. 4 shows the organizational model associated with this work<sup>fl</sup>ow. The employees for each role are speci<sup>fi</sup>ed as follows: GM (John), ED (Joe), PD (Jason), AD (Maggie), SE (Eric, Ray), PC (Peter), IC (Sam), DC (Dan, Jack), and AC (Steve, Ben).

To ensure proper work<sup>fl</sup>ow execution, work<sup>fl</sup>ow constraints must be speci<sup>fi</sup>ed to enforce business and operational rules. Fig. 5 lists the constraints for the procurement work<sup>fl</sup>ow. Constraints $c _ { I }$ through $c _ { 8 }$ are resource assignment constraints. Constraint c is a separation of duties constraint, whereas $c _ { 1 0 }$ is a binding of duties constraint. Constraints $c _ { 1 1 }$ through $c _ { 2 0 }$ are routing rules for the <sup>fi</sup>ve branch constructs in the process. Constraints $c _ { 2 1 }$ through $c _ { 2 7 }$ specify the input data for the branch constructs.

Next, we present a work<sup>fl</sup>ow speci<sup>fi</sup>cation framework based on First Order Logic, which is used to represent the procurement process and analyze work<sup>fl</sup>ow constraint anomalies.

![](/api/attachments/E4W4EEKC/fulltext/images/bb25b0856ee86a98f9a469775b314129118ae8ad63df7a102c32dfdde9ad9b49.jpg)  
Fig. 2. Work<sup>fl</sup>ow change dependencies

## 4.2. Constraint-centric workflow specification

Given the work<sup>fl</sup>ow change dependencies shown in Fig. 2, we need a uni<sup>fi</sup>ed representation for the four work<sup>fl</sup>ow perspectives in order to formally analyze work<sup>fl</sup>ow changes. In this paper, we extend previous research on work<sup>fl</sup>ow constraint speci<sup>fi</sup>cation by means of First Order Logic. We choose First Order Logic for several reasons: <sup>fi</sup>rst, it has been widely used to present declarative knowledge [24,42], which is a natural choice for specifying work<sup>fl</sup>ow constraints. Second, it is suf<sup>fi</sup>ciently expressive to represent control <sup>fl</sup>ow, data <sup>fl</sup>ow, and organizational model by de<sup>fi</sup>ning appropriate predicates with formal work<sup>fl</sup>ow semantics. Third, it enables us to specify formally work<sup>fl</sup>ow changes. Lastly, we can leverage logic programming and the wide array of rule engines to support the implementation of our CWCA approach.

The four work<sup>fl</sup>ow perspectives are formally de<sup>fi</sup>ned as follows.

## De<sup>fi</sup>nition 1. Control Flow

Control <sup>fl</sup>ow is a 5-tuple bT, start, end, RC, LN, where

$T = \{ t \}$ t is a task of the work<sup>fl</sup>ow},

• start is the start node of the work<sup>fl</sup>ow,

• end is the end node of the work<sup>fl</sup>ow,

$\bullet \ R C = \{ r c \ | \ r c \in \{ f , j , b , m \} \}$ is the set of routing constructs where f (fork) and j (join) are used to represent parallel execution and synchronization of a set of tasks, and b (branch) and m (merge) are used to choose one task from a set of tasks for execution.

$L = \{ n e x t ( x , y ) | x , y \in T \cup$ {start, end} ∪ RC and x precedes y} is the set of links in the control <sup>fl</sup>ow.

The control <sup>fl</sup>ow perspective de<sup>fi</sup>nes the tasks, routing constructs, start and end nodes, and the task execution orders. Given De<sup>fi</sup>nition 1, the control <sup>fl</sup>ow of the procurement process can be formally represented as the set of logic facts and predicates in Fig. 6.

## De<sup>fi</sup>nition 2. Data Flow

Data <sup>fl</sup>ow is a 3-tuplebD, I, ON, where

• D={d | d is a data item used in the work<sup>fl</sup>ow},

• I={input(n,d) | d ∈ D and n ∈ T ∪ {start, end} ∪ RC} is the set of predicates to specify input data to process nodes,

• O={output(n, d) | d ∈ D and n ∈ T ∪ {start, end} ∪ RC} is the set of predicates to specify output data to process nodes.

The data <sup>fl</sup>ow perspective concerns what data objects are related to the work<sup>fl</sup>ow and what are inputs and outputs for different process nodes.

## De<sup>fi</sup>nition 3. Organizational Model

Organizational model is a 3-tuplebR, B, MN, where

• R=U ∪ RO is the set of organizational resources, $U = \{ u \}$ | u is a user in the organization}, RO={ro | ro is a role or position in the organization,

$\bullet B = \{ b e l o n g ( a , b ) \mid a \in U , b \in R O \}$ speci<sup>fi</sup>es user a has role $b ,$

• M={manage(j, k) | j, k ∈ R} speci<sup>fi</sup>es resource j manages resource k.

![](/api/attachments/E4W4EEKC/fulltext/images/4faeb7fbf5910b03eddb3cbf40e3f6ae1e96fcec3699356b0b76f2fc8ae9cde9.jpg)  
Fig. 3. A procurement work<sup>fl</sup>ow.

The organizational perspective de<sup>fi</sup>nes organizational resources related to the work<sup>fl</sup>ow and their relationships. An organizational resource is de<sup>fi</sup>ned as an entity that is capable of doing work, which may be either human or non-human [43]. In De<sup>fi</sup>nition 3, human resources are further classi<sup>fi</sup>ed into users, roles, and groups, whereas non-human resources are called agents. Predicates belong(a, b) and manage(j, k) are used to de<sup>fi</sup>ne the relationships among resources, e.g. associating users to roles and specifying role hierarchy. For example, belong(John, GM) means user John is associated with the role GM (General Manager) and manage(GM, PD) speci<sup>fi</sup>es role GM has control over PD (Purchasing Director). According to De<sup>fi</sup>nition 3, the organizational model for the procurement work<sup>fl</sup>ow can be expressed as in Fig. 7.

By De<sup>fi</sup>nitions 1, 2, and 3, control <sup>fl</sup>ow, data <sup>fl</sup>ow, and organizational model are speci<sup>fi</sup>ed separately from one another. This assumption is based on our experiences with several commercial process modeling tools, such as the IBM WebSphere Business Modeler, TIBCO iProcess Suite, and Ultimus BPM Suite, where those three perspectives are modeled separately <sup>fi</sup>rst and then integrated together via proprietary system functions, i.e., work<sup>fl</sup>ow constraints. This assumption is not a limitation of our approach. Instead, it aligns very well with our innovative treatment of multi-perspective work-<sup>fl</sup>ow changes through a constraint-centric approach as discussed previously in Section 3. Thus, work<sup>fl</sup>ow constraints are formally de<sup>fi</sup>ned as follows.

Descriptions of procurement tasks.

<table><tr><td>Task</td><td>Name</td><td>Description</td></tr><tr><td> $t_{1}$ </td><td>Submit purchase request</td><td>Employees submit purchase request.</td></tr><tr><td> $t_{2}$ </td><td>Supervisor approval</td><td>The supervisor of task initiator approves the request</td></tr><tr><td> $t_{3}$ </td><td>Check fund</td><td>When request amount is greater than $1000, a checking is conducted to make sure there is sufficient fund.</td></tr><tr><td> $t_{4}$ </td><td>Mgmt approval</td><td>When fund is sufficient, general manager needs to approve.</td></tr><tr><td> $t_{5}$ </td><td>Check inventory</td><td>Check whether the requested item is in stock.</td></tr><tr><td> $t_{6}$ </td><td>Purchasing</td><td>Purchase order is issued to vendor to buy the requested item.</td></tr><tr><td> $t_{7}$ </td><td>Receive item</td><td>Item is received from vendor and checked for quality.</td></tr><tr><td> $t_{8}$ </td><td>Item delivery</td><td>The requested item is delivered.</td></tr><tr><td> $t_{9}$ </td><td>Delivery notification</td><td>Delivery notification is sent to the item requester.</td></tr><tr><td> $t_{10}$ </td><td>Archiving</td><td>The transaction information is archived.</td></tr><tr><td> $t_{11}$ </td><td>Disapproval notification</td><td>The requestor is notified about the request denial.</td></tr></table>

## De<sup>fi</sup>nition 4. Work<sup>fl</sup>ow Constraint

A work<sup>fl</sup>ow constraint $c \in C$ is a logic formula used to connect control <sup>fl</sup>ow, data <sup>fl</sup>ow, and organizational model or enforce business and operational rules. A work<sup>fl</sup>ow constraint is in the following form:

$$
H \leftarrow X _ {1}, \dots , X _ {n}, n o t Y _ {1}, \dots , n o t Y _ {m}, n, m \geq 0
$$

where H, $X _ { 1 } , . . . , X _ { n } , Y _ { 1 } , . . . , Y _ { m }$ are logic formulas and not is a negation by failure [24,36]. H is the head of the constraint, and $X _ { 1 } , . . . ,$ $X _ { n } ,$ not $Y _ { 1 } , . . . ,$ not $Y _ { m }$ consist of the constraint body. A constraint is activated if and only if $X _ { 1 } , . . . , X _ { n } ,$ not $Y _ { 1 } , . . . ,$ not $Y _ { m }$ are all true, resulting in H being true. Note a workflow constraint may contain only head where body is empty. In that case, H is said to be true.

Several object and predicate symbols have been de<sup>fi</sup>ned in De<sup>fi</sup>nitions 1, 2, and 3, including T, s, e, RC, next, D, input, output, R, belong, and manage. In order to represent work<sup>fl</sup>ow constraints for the procurement work<sup>fl</sup>ow as shown in Fig. 5, additional predicate symbols need to be de<sup>fi</sup>ned as shown in Table 3. With this succinct set of object and predicate symbols, the problem of unifying control <sup>fl</sup>ow, data <sup>fl</sup>ow, organization model, and work<sup>fl</sup>ow constraints is resolved by means of a set of logic formulas.

It is worth noting that specifying a complete set of predicates to model all kinds of work<sup>fl</sup>ows is not the focus of this paper. Instead, our goal is to formally introduce the new constraint-centric work<sup>fl</sup>ow change management approach using a small set of predicates that are enough to model all perspectives in the sample procurement management process. More object and predicate symbols can always be added as needed to make the CWCA modeling framework capable for modeling any speci<sup>fi</sup>c work<sup>fl</sup>ow. The choice of what symbols to include depends on the work<sup>fl</sup>ow modeling context as well as the interests and concerns of work<sup>fl</sup>ow designer and stakeholders. With the CWCA modeling framework de<sup>fi</sup>ned in this section, three types of constraints can be modeled: 1) routing constraints that specify the routing conditions for branches; 2) authorization constraints that associate resources with task, and 3) data constraints that relate data items with tasks and routing constructs. The constraint type can be speci<sup>fi</sup>ed as constraint metadata as de<sup>fi</sup>ned below.

![](/api/attachments/E4W4EEKC/fulltext/images/15e5f6845e0de64c688c30f09b276cd9cc48306f8eb9fa6b5dddf1bc591a4ec1.jpg)  
Fig. 4. Organization model for the procurement work<sup>fl</sup>ow.

## De<sup>fi</sup>nition 5. Work<sup>fl</sup>ow Constraint Metadata

For each work<sup>fl</sup>ow constraint $c \in C ,$ , its metadata is de<sup>fi</sup>ned as a <sup>fi</sup>ve tuplebcid, TY, P, H, EN, where

• cid is the unique identi<sup>fi</sup>er of the constraint,

• TY ∈ {routing, authorization, data} is the constraint type,

• P is the premise of the constraint

• H is the conclusion of the constraint, and • E={e | e ∈ T ∪ RC ∪ D ∪ R ∪ C is a work<sup>fl</sup>ow element involved in the constraint}.

Thus, the constraints for the procurement work<sup>fl</sup>ow in Fig. 5 can be formalized as shown in Fig. 8. In particular, constraints c to c are authorization constraints. Constraint $c _ { 1 1 } \mathrm { t o } c _ { 2 0 }$ are routing constraints. Constraints c to c are data constraints. To the best of our knowledge, the constraint-centric work<sup>fl</sup>ow modeling framework is the <sup>fi</sup>rst attempt with using First Order Logic to unify the four work<sup>fl</sup>ow perspectives for managing work<sup>fl</sup>ow changes.

## 5. Work<sup>fl</sup>ow constraint anomalies

The uni<sup>fi</sup>ed logic representation of a work<sup>fl</sup>ow model enables us to specify formally work<sup>fl</sup>ow changes in multiple work<sup>fl</sup>ow perspectives. In this section, we de<sup>fi</sup>ne work<sup>fl</sup>ow constraint anomalies and present the associated anomaly detection algorithm. We use the procurement work<sup>fl</sup>ow case to validate the algorithm.

## 5.1. Types of workflow constraint anomalies

Work<sup>fl</sup>ow changes are formally de<sup>fi</sup>ned in terms of a work<sup>fl</sup>ow change function.

## De<sup>fi</sup>nition 6. Work<sup>fl</sup>ow Change Function

Let W be a work<sup>fl</sup>ow model $W { = } T \cup R C \cup D \cup R \cup C , i$ a work<sup>fl</sup>ow change function is de<sup>fi</sup>ned as $f _ { c } \colon W \to W ^ { \prime }$ where $W ^ { \prime } { = } T \cup R C ^ { \prime } \cup D ^ { \prime } \cup R ^ { \prime } \cup C ^ { \prime }$ is the result of performing operations OP {Insertion, Deletion, Modification} on W.

Given the work<sup>fl</sup>ow models before and after changes, i.e. W and W′, work<sup>fl</sup>ow constraint anomalies can be classi<sup>fi</sup>ed into four categories, namely, Missing Constraint Anomaly, Defective Constraint Anomaly, Redundant Constraint Anomaly, and Conflicting Constraint Anomaly, as discussed next.

## 5.1.1. Missing constraint anomaly

Missing constraint anomaly occurs when a work<sup>fl</sup>ow cannot be properly executed due to a lack of certain constraints. Each of the following scenarios can cause missing constraint anomalies.

![](/api/attachments/E4W4EEKC/fulltext/images/49c3d18697a558658f3fdd01c6bc8365ec60f37556c00ec42db29559abe88f6f.jpg)  
Fig. 5. Key constraints for the procurement work<sup>fl</sup>ow.

<table><tr><td>start, end, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, b1, b2, b3, b4, b5, f1, j1, m1, next(start, t1), next(t1, t2), next(t2, b1), next(b1, b2), next(b1, t11), next(b2, t3), next(b2, t5), next(t3, b3), next (b3, t11), next(b3, t4), next(t4, b4), next(b4, t11), next(b4, t5), next(t5, b5), next(b5, t6), next(b5, t8), next(t6, t7), next(t7, t8), next(t8, f1), next(f1, t10), next(f1, t9), next(t10, j1), next(t9, j1), next(j1, m1), next(t11, m1), next(m1,end)</td></tr></table>

Fig. 6. Logic representation of the control <sup>fl</sup>ow.

<table><tr><td>manage(GM,ED), manage(GM,PD), manage(GM,AD),manage(ED,SE), manage(PD,PC), manage(PD,IC),manage(PD,DC), manage(AD,AC), belong(John, GM),belong (Joe, ED), belong(Jason, PD), belong(Maggie, AD),belong (Eric, SE), belong(Ray, SE), belong(Peter, PC), belong(Sam, IC), belong(Jack, DC), belong(Dan, DC), belong(Steve, AC), belong(Ben, AC)</td></tr></table>

Fig. 7. Logic representation of the organizational model.

Scenario 1 (Task without Resources). A task is given in the work<sup>fl</sup>ow model, but no resources are speci<sup>fi</sup>ed to execute the task. As a result, the task cannot be executed during runtime, resulting in halting of work<sup>fl</sup>ow execution at the task.

Scenario 2 (Branch without Routing Constraints). A branch routing construct is inserted in the work<sup>fl</sup>ow model, but no routing constraints are speci<sup>fi</sup>ed. This will cause a work<sup>fl</sup>ow execution fault.

Every branch routing construct represents a decision point since the control <sup>fl</sup>ow takes a particular path according to a given condition. Therefore, at least two outgoing links must be speci<sup>fi</sup>ed at each decision point, and thus at least two routing constraints must be in place to specify the routing conditions.

## Proposition 1. Condition for Missing Constraint Anomaly

Given a task $t \in T ^ { \prime }$ that $\mathfrak { t } \notin \cup _ { i = 1 } ^ { n } c _ { i } . E$ where $c _ { i } \in C ^ { \prime }$ and $c _ { i } . T Y =$ {authorization}, or a branch routing construc $b \in R C ^ { \prime }$ that b ∉ $\cup _ { j = 1 } ^ { m } c _ { j } . E$ where $c _ { j } \in C ^ { \prime }$ and $c _ { j } . T Y { = } \{ \mathrm { r o u t i n g } \} ,$ , a work<sup>fl</sup>ow model after the change $W ^ { \prime }$ contains at least one missing constraint anomaly.

Discussion. $\cup _ { i = 1 } ^ { n } c _ { i }$ Eis the set of process elements referenced in all authorization constraints after the change. Given a task $t \in T ^ { \prime }$ , t is part of the work<sup>fl</sup>ow model after the change. Given ${ \mathfrak { t } } \ \notin \ \cup _ { i = 1 } ^ { n } c _ { i } . E ,$ no authorization constraints are de<sup>fi</sup>ned for t, leading to a missing constraint anomaly. Similarly, $\cup _ { j = 1 } ^ { m } c _ { j } .$ E is the set of process elements referenced in all routing constraints after the change. Given a branch $b \in$ RC′, b is part of the work<sup>fl</sup>ow model after the change. Given $b \not \in \cup _ { j = 1 } ^ { m } c _ { j } . E ,$ b is not referenced in any routing constraints, resulting in a missing constraint anomaly.

## 5.1.2. Invalid constraint anomaly

Constraints are identi<sup>fi</sup>ed as invalid if they refer to non-existing work<sup>fl</sup>ow elements. Invalid constraints can be further divided into two subtypes, namely, defective constraint and redundant constraint, based on whether the constraint is required for work<sup>fl</sup>ow execution. More speci<sup>fi</sup>cally, each of the following scenarios can cause defective constraint anomalies.

Scenario 3 (Non-existing Resource). One or more resources in authorization constraints are not available. For example, constraint c : execute(DC, t ) is defective when the role Distribution Clerk (DC) becomes unavailable due to organizational restructuring. Constraint ${ \bf C } _ { 3 }$ cannot be enforced properly for t during work<sup>fl</sup>ow execution, which will cause an execution halt.

Scenario 4 (Non-existing Target Task). The target tasks in a routing constraint become unavailable, resulting in defective routing constraints. For example, constraint $c _ { 1 3 } \colon n e x t ( b _ { 2 } , t _ { 3 } ) \gets d _ { 2 } \geq$ 5000 can cause a routing exception if $\mathbf { t } _ { 3 }$ is removed.

Scenario 5 (Non-existing Routing Data Item). The data item in a routing constraint become unavailable, resulting in defective routing constraints. For example, constraint $c _ { 1 4 } .$ next $\cdot b _ { 2 } , t _ { 5 } ) \gets d _ { 2 } { < } 5 0 0 0$ can cause a routing exception if ${ \sf d } _ { 2 }$ becomes unavailable.

## Proposition 2. Condition for Defective Constraint Anomaly

Given a constraint $c \in C ^ { \prime }$ that $c . T Y =$ {authorization}, ${ \mathfrak { c } } . E \cap T | T ^ { \prime } = \emptyset , c . E$ $\cap R | R ^ { \prime } \neq \emptyset , \operatorname { o r } c . T Y =$ {routing}, c.E $\cap R C | R C ^ { \prime } = \varnothing , c . E \cap ( T \backslash T ^ { \prime } \cup D \backslash D ^ { \prime } ) \neq \varnothing ,$ , the work<sup>fl</sup>ow model after changes W′ contains at least one defective constraint anomaly.

Discussion. $c . T Y { = } \{ { \mathrm { a u t t h o r i z a t i o n } } \}$ means c is an authorization constraint. $T \backslash T ^ { \prime }$ is the set of removed tasks and $c . E \cap T | T ^ { \prime } = \varnothing$ speci<sup>fi</sup>es that c does not refer to non-existing tasks. $R \vert { R } ^ { \prime }$ is the set of removed resources and $c . E \cap R | R ^ { \prime } \neq \emptyset$ speci<sup>fi</sup>es that c references to some non-existing resources, leading to a defective constraint anomaly. $c . T Y =$ {routing} means c is a routing constraint. RC\RC′ is the set of removed routing constructs and $D | D ^ { \prime }$ is the set of removed data items. $c . E \cap R C | R C ^ { \prime } = \emptyset$ speci<sup>fi</sup>es that c does not refer to non-existing routing construct, and c.E ∩ $( T \backslash T ^ { \prime } \cup D \backslash D ^ { \prime } ) \neq$ ∅ speci<sup>fi</sup>es that contains either removed tasks or removed data items, resulting in a defective constraint anomaly.

It is noteworthy that although some defective constraints may be due to some non-existing work<sup>fl</sup>ow elements, those constraints are still required for work<sup>fl</sup>ow execution, and the errors should be <sup>fi</sup>xed. On the other hand, if some invalid constraints are no longer needed for work<sup>fl</sup>ow execution, they are referred to as redundant constraints, which can be simply removed. Each of the following scenarios can lead to redundant constraints.

Scenario 6 (Redundant Authorization Constraint). Authorization constraints become redundant when the related task does not exist. For example, constraint $c _ { 2 } \colon e x e c u t e ( A C , t _ { 3 } )$ becomes redundant when task $t _ { 3 }$ is removed from the work<sup>fl</sup>ow although role Accounting Clerk (AC) may still exist.

Scenario 7 (Redundant Routing Constraint). Routing constraints become redundant when the related routing construct does not exist. For example, constraint $c _ { 1 3 } \mathrm { : }$ next $( b _ { 2 } , t _ { 3 } )  d _ { 2 } { \geq } 5 0 0 0$ becomes redundant when routing construct $b _ { 2 }$ is removed even when $t _ { 3 }$ and $d _ { 2 }$ both exist.

Scenario 8 (Redundant Data Constraint). Data constraints become redundant when a related data item, task or routing construct does not exist. For example, constraint $c _ { 3 1 } \colon$ input $( b _ { 1 } , \ d _ { 1 } )$ becomes redundant when data $d _ { 1 }$ is removed or branch $b _ { 1 }$ is deleted, because there is no need to specify the input in cases.

Summary of additional predicate symbols.

<table><tr><td>Symbols</td><td>Meaning</td></tr><tr><td>execute(x, y)</td><td>x ∈ R, y ∈ T, x is assigned to execute task y</td></tr><tr><td>cannot_execute(x, y)</td><td>x ∈ R, y ∈ T, x cannot execute task y</td></tr><tr><td>=, &lt;, ≤, &gt;, ≥</td><td>Relational operators: equal to, less than, less than or equal to, greater than, greater than or equal to.</td></tr><tr><td>+, -, *, /</td><td>Arithmetic operators: addition, subtraction, multiplication, division</td></tr></table>

![](/api/attachments/E4W4EEKC/fulltext/images/2ac1694357dbb156f6df6181dc3a8e494d99cb7e63dc9506709b5b29f3980fb4.jpg)  
Fig. 8. Logic representation of work<sup>fl</sup>ow constraints

## Proposition 3. Condition for Redundant Constraint Anomaly

Given a constraint $c \in C ^ { \prime }$ that c.TY={authorization}, c.E ∩ $T \lbrack T ^ { \prime } \neq \varnothing ,$ or $c . T Y =$ {routing}, c.E ∩ RC\RC′≠∅, or c.TY ∈ {data}, c.E ∩ (T\T ′ ∪ RC\RC′ ∪ $D \backslash D ^ { \prime } \cup R \backslash R ^ { \prime } ) \neq \emptyset ,$ the work<sup>fl</sup>ow model after changes W′ contains at least one redundant constraint anomaly.

Discussion. Given $c . T Y = \{ \mathrm { a u t h o r i z a t i o n } \} ,$ c is an authorization constraint and c.E $\cap T \backslash T ^ { \prime } \neq \emptyset$ means c refers to non-existing tasks. An authorization constraint is redundant if the associated tasks have been removed. Similarly, given $c . T Y = \{ \mathrm { r o u t i n g } \} , c . E \cap R C | R C ^ { \prime } \neq \emptyset ,$ , the routing constraint becomes redundant when the associated routing construct no longer exists. For data and association constraints, i.e. c. $T Y \in \{ \mathsf { d a t a } \}$ , if any of the involved process elements does not exist, i.e. $c . E \cap ( T | T ^ { \prime } \cup R C | R C ^ { \prime } \cup D \backslash D ^ { \prime } \cup R \backslash R ^ { \prime } ) \neq \emptyset ,$ , the constraint is no longer needed for work<sup>fl</sup>ow execution as discussed in Scenario 8.

## 5.1.3. Conflicting constraint anomaly

A con<sup>fl</sup>icting constraint anomaly occurs when there are constraints causing a contradiction. Each of the following scenarios can cause con<sup>fl</sup>icting constraint anomalies.

Scenario 9 (Con<sup>fl</sup>icting Routing Constraint). A con<sup>fl</sup>icting constraint occurs when two routing constraints create a routing contradiction. For example, if the following two constraints exist at a branch b: nex $t ( b , t _ { 1 } )  d$ and nex $\ ( b , t _ { 2 } )  d$ , then when d is true, the two target tasks from b lead to a con<sup>fl</sup>ict.

Scenario 10 (Con<sup>fl</sup>icting Authorization Constraint). A con<sup>fl</sup>icting constraint occurs when two authorization constraints are against each other. For example, if both constraints execute(r, t), and cannot\_execute(r, t) exist, a resource assignment con<sup>fl</sup>iction occurs for task t. Another example could be a binding of duties constraint as $c _ { 1 0 } \mathrm { : }$ execute(u, t )←execute(u, t ) can cause a con<sup>fl</sup>ict when the resources assigned to tasks $t _ { 7 }$ and $t _ { 8 }$ do not have any common users.

## Proposition 4. Conditions for Con<sup>fl</sup>icting Constraint Anomaly

Given three constraints $c _ { i } , c _ { j } , c _ { k } \in C ^ { \prime }$ if any of the following three conditions holds, the work<sup>fl</sup>ow model $W ^ { \prime }$ contains at least one con<sup>fl</sup>icting constraint anomaly:

1) $c _ { i } . T Y = c _ { j } . T Y = \{ { \mathrm { r o u t i n g } } \} , c _ { i } . P = c _ { j } . P , c _ { i } . H = n e x t ( x , y ) , c _ { j } . H = n e x t ( x , z )$ where x, y, z ∈ {start, end} ∪ T ∪ RC, x ∉{f, end}, y, z ∉{start}, y ≠z

2) c<sub>i</sub>.T Y = c<sub>j</sub>.T Y = {authorization}, $c _ { i } . P { = } c _ { j } . P , c _ { i } . \mathrm { E } { = } c _ { j } . \mathrm { E } , c _ { i } . H { \neq } c _ { j } . H$

3) c .T Y=c .TY=c .T Y={authorization}, $c _ { i } . H { = e x e c u t e ( \alpha , t _ { m } ) , c _ { j } . H } { = }$ execut $\begin{array} { r } { \mathsf {  { \boldsymbol { z } } } ( \beta , t _ { n } ) , c _ { k } . H = e x e c u t e ( \gamma , t _ { n } ) , c _ { k } . P = e x e c u t e ( \gamma , t _ { m } ) , } \end{array}$ , where $t _ { m } ,$ $t _ { n } \in T , \alpha , \beta \in R O , \gamma \in U , \nexists \ \gamma ,$ so that belong(γ, α) and belong(γ, β) are both true.

Discussion. Given two constraints $c _ { i } , c _ { j } \in C ^ { \prime }$ that $c _ { i } . T Y = c _ { j } . T Y =$ {routing}, $c _ { i } . P { = } c _ { j } . P$ means the two routing constraints have the same premises, but $c _ { j } . H = n e x t ( x , z )$ , where $x , y , z \in \{ s t a r t , e n d \} \cup T \cup R C , \mathbf { x } \notin$ { f, end}, y, z ∉{start}, $y \neq z$ speci<sup>fi</sup>es that there exists two control <sup>fl</sup>ow links starting from the same process node x leading to two different process nodes y and z. When x is not a fork routing construct, a con<sup>fl</sup>icting constraint anomaly occurs. Given two constraints $c _ { i } , c _ { j } \in C ^ { \prime }$ that $c _ { i } . T Y = c _ { j } . T Y = \{ \mathrm { a u t h o r i z a t i o n } \}$ $c _ { i } . P { = } c _ { j } . P , \ c _ { i } . \operatorname { E } { = } c _ { j } . \operatorname { E }$ indicate the two authorization constraints are de<sup>fi</sup>ned on the same resources and tasks and the premises of the constraints are the same, but $c _ { i } . H \neq c _ { j } . H$ speci<sup>fi</sup>es that the predicates in the conclusions are different, i.e. both execute and cannot\_execute exist, resulting in a con<sup>fl</sup>icting authorization. $c _ { i } . T Y { = } c _ { j } . T Y { = } c _ { k } . T Y { = }$ {authorization}, $\begin{array} { r } { c _ { i } . H { = } e x e c u t e ( \alpha , t _ { m } ) , } \end{array}$ $c _ { j } H = e x e c u t e ( \beta , t _ { n } ) , c _ { k } H = e x e c u t e ( \gamma , t _ { n } ) , c _ { k } P = e x e c u t e ( \gamma , t _ { m } ) , \alpha , \beta \in R O$ $\gamma \in U$ indicates that $c _ { k }$ is a binding of duties constraint that requires user $\gamma ~ \mathrm { t o }$ execute both tasks $t _ { m }$ and $t _ { n } ,$ and $c _ { i }$ and $c _ { j }$ are two resource assignment constraints that assign α and $\beta$ as the roles to execute tasks $t _ { m }$ and $t _ { n }$ respectively. Then, ∄ γ, so that belong(γ, α) and belong $( \gamma , \beta )$ are both true states that there are no users that belong to both α and $\beta$ roles. In this case, the “binding of duties” constraint cannot be satis<sup>fi</sup>ed because proper task assignments are not possible with the two given resource assignment constraints due to a lack of common users assigned to the two relevant roles.

A Venn diagram representing different categories of work<sup>fl</sup>ow constraints with respect to constraint anomalies is developed as shown in Fig. 9. This Venn diagram is useful for understanding the relationships among work<sup>fl</sup>ow constraint anomalies and the basic principles of constraint management after a work<sup>fl</sup>ow change. In addition, we can show that the classi<sup>fi</sup>cation of work<sup>fl</sup>ow constraint is complete. Let C be the set of work<sup>fl</sup>ow constraints and MI, IN, VA, RE, DE, CO be the sets of missing, invalid, valid, redundant, defective, and con<sup>fl</sup>icting constraints respectively. Given any work<sup>fl</sup>ow constraint c $\in C ,$ it can always be placed into the space of work<sup>fl</sup>ow constraints represented by the Venn diagram in Fig. 9. This can be shown algorithmically. For each constraint, it must be either existing or missing, i.e., $\forall c \in C , c \in M I \cup \neg M I ,$ , without exception. For an existing constraint, it must be either valid or invalid based whether the constraint references non-existing work<sup>fl</sup>ow elements, i.e., $\forall c \in \neg M I ,$ $c \in I N \cup V A$ . Note that these three constraint types are mutually exclusive, $\mathrm { i . e . } M I \cap I N \cap V A = \emptyset$ . Further, for each invalid constraint $c ^ { \prime } \in$ $I N ,$ if it is not required for work<sup>fl</sup>ow execution, it is a redundant constraint $c ^ { \prime } \in R E ;$ otherwise it is a defective constraint $c ^ { \prime } \in D E .$ . Lastly, for each valid constraint $c ^ { \prime \prime } \in V A ,$ , it either causes con<sup>fl</sup>ict, i.e. $c ^ { \prime \prime } \in C O _ { \mathrm { { \ell } } }$ or does not lead to contradiction, i.e., $c ^ { \prime \prime } \in \neg C O$ . Thus, the space of work<sup>fl</sup>ow constraints as depicted in Fig. 9 is complete.

Propositions 1 through 4 de<sup>fi</sup>ne all possible conditions where work<sup>fl</sup>ow constraint anomalies can occur within our CWCA framework, they provide the foundation for designing algorithms to detect work<sup>fl</sup>ow constraint anomalies as we will discuss in the next section. It is worth noting that work<sup>fl</sup>ow constraints are often not explicitly modeled in work<sup>fl</sup>ow systems. Work<sup>fl</sup>ow constraints can also be informally de<sup>fi</sup>ned as business rules related to work<sup>fl</sup>ow, which are often speci<sup>fi</sup>ed in policy and procedure documents. In this paper, we assume that work<sup>fl</sup>ow constraints have been properly identi<sup>fi</sup>ed and speci<sup>fi</sup>ed using process mapping approaches [35,47,56]. The CWCA approach consists of a set of extensible anomaly detection rules to identify work<sup>fl</sup>ow anomalies during system changes and thus provides a <sup>fl</sup>exible and extensible framework to accommodate new business environments. For example, our current approach can detect anomalies due to a missing resource, which requires that the system speci<sup>fi</sup>es all resources needed for executing existing tasks. However, in a new business environment, new detection rules may be needed to handle new work<sup>fl</sup>ow resources that have not been de<sup>fi</sup>ned. The ability to extend the modeling framework with new predicates and rules is a strength of the CWCA approach.

The space of workflow constraints  
![](/api/attachments/E4W4EEKC/fulltext/images/aff3ab34c23305e1f8ac163173a702bf5a6351110d300b2ee3e93c781464b5fe.jpg)  
Fig. 9. Venn diagram of work<sup>fl</sup>ow constraint types.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
PROCEDURE ConstraintAnomalyDetection
for each  $t \in T'$  {count(execute(x, t), m)
    if (m = 0) print "missing constraint for t"} // detect scenario 1
for each  $b \in RC'$  {count(constraint(c, b), n)
    if (n &lt; 2) print "missing constraint for b"} // detect scenario 2
for each  $c \in C'$ 
    if c.E  $\in T' \cup RC' \cup D' \cup R' \cup C'$ 
    add c to set VA // add c to the valid constraint set VA
    else // c is identified as an invalid constraint
    if (c.TY = {data}) {print "redundant constraint c"} // detect scenarios 8
    if (c.TY = {authorization}) {
    if (c.E  $\cap$  T\T ' ≠ ∅) print "redundant authorization constraint c" // detect scenario 6
    else if (c.E  $\cap$  R\R' ≠ ∅) print "defective constraint c due to missing resource" } // detect scenario 3
    if (c.TY = {routing}) {
    if (c.E  $\cap$  RC\RC' ≠ ∅) print "redundant routing constraint c" // detect scenario 7
    else if (c.E  $\cap$  (T\T' ∪ D\D') ≠ ∅) print "defective constraint c" } // detect scenarios 4 and 5
for each pair  $c_i, c_j \in VA$ 
    if ( $c_i.TY = c_j.TY = \{routing\}$ ,  $c_i.P = c_j.P$ ,  $c_i.H = next(x, y)$ ,  $c_j.H = next(x, z)$ , where x, y, z ∈ {start, end} ∪ T ∪ RC, x∉{f, end}, y, z∉{start}, y ≠ z) {
    print "conflicting routing constraints c_i and c_j"} // detect scenario 9
    if ( $c_i.TY = c_j.TY = \{authorization\}$ ,  $c_i.P = c_j.P$ ,  $c_i.E = c_j.E$ ,  $c_i.H ≠ c_j.H$ 
    print "conflicting authorization constraint for c_i and c_j"} // detect scenario 10
    if ( $c_i.TY = c_j.TY = \{authorization\}$ ,  $c_i.H = execute(\alpha, t_m)$ ,  $c_j.H = execute(\beta, t_n)$ , α, β ∈ RO),
    there exists  $c_k \in VA$ $c_k.H = execute(\gamma, t_n)$ ,  $c_k.P = execute(\gamma, t_m)$ , γ ∈ U, and ∉ γ, belong(γ, α) and belong(γ, β) are both true) {
    print "conflicting binding of duties constraint for c_i, c_j, and c_k"} // detect scenario 10
</div>

Fig. 10. Constraint anomaly detection algorithm.

## 5.2. Workflow constraint anomaly detection

Based on Propositions 1 through 4, we develop an algorithm to detect work<sup>fl</sup>ow constraint anomalies as shown in Fig. 10. One aggregation function supported by most existing logic programming languages and systems [20,24], namely, count(Q, n) is leveraged in the algorithm, where count(Q, n) returns the number of different answers of query←Q to n. This algorithm also illustrates the precedence of the four propositions, i.e., the sequence of applying the propositions to detect work<sup>fl</sup>ow constraint anomalies. More speci<sup>fi</sup>cally, we <sup>fi</sup>rst check each task and routing construct to detect missing constraints. Then, we divide all existing constraints into valid and invalid constraints based on whether they refer to non-existing work<sup>fl</sup>ow elements. For invalid constraints, according to different types of constraints, we <sup>fi</sup>rst detect redundant constraints and then defective constraints, because the conditions for redundant constraints are easier to check. After that, we detect con<sup>fl</sup>icting constraints among all valid constraints. According to the four propositions, the algorithm shown in Fig. 10 is able to detect all constraint anomalies in our CWCA framework. Once the anomalies are detected, proper actions must be taken according to the anomaly types to ensure work<sup>fl</sup>ow consistency. In particular, additional constraints should be added to address missing constraint anomalies. Redundant constraints should be removed. Defective and con<sup>fl</sup>icting constraints should be resolved to achieve constraint consistency. Note that the algorithm should be executed every time there is a change in the work<sup>fl</sup>ow model to update the anomaly list. In this paper, we focus on detecting work<sup>fl</sup>ow change anomalies, and leave detailed discussions on anomaly correction to future research.

In order to validate the algorithm, we make some changes to the procurement work<sup>fl</sup>ow and apply the algorithm to detect potential anomalies. The changes are listed in Table 4 and the new work<sup>fl</sup>ow is shown in Fig. 11. In particular, a new task $t _ { 1 2 }$ (Vendor Selection) is added to incorporate a formal procedure for selecting the best vendor for the requested items. Tasks t (Check Fund) is removed to improve the ef<sup>fi</sup>ciency of the work<sup>fl</sup>ow by reassigning the “check fund” task to task t (Supervisor Approval). $t _ { 1 0 }$ (Archiving) is removed because the integration of a new automatic archiving system with the procurement process. Some related routing constructs are also deleted, including $b _ { 3 } ,$ $f _ { 1 } ,$ and $j _ { 1 } .$ Due to a new organizational restriction, role ‘Inventory Clerk’ is merged into role ‘Purchasing Clerk’. A data item is renamed $d _ { 2 }$ (item total value), which corresponds to the deletion of $\dot { \ b { d } } _ { 2 }$ and the insertion of d (request item total). The new control <sup>fl</sup>ow is presented in Fig. 12, and the new organizational model is represented in Fig. 13.

By applying the algorithm to the modi<sup>fi</sup>ed work<sup>fl</sup>ow model, we can identify <sup>fi</sup>ve missing constraint anomalies, seven redundant constraints, and six invalid constraints. Missing constraints are identi<sup>fi</sup>ed for tasks t (Purchase Request), t (Supervisor Approval), $t _ { 9 }$ (Delivery Noti<sup>fi</sup>cation), $t _ { 1 1 }$ (Disapproval Noti<sup>fi</sup>cation), and $t _ { 1 2 }$ (Vender Selection). In particular, $\mathrm { t } _ { 1 }$ can be executed by any employee in the organization, and no resource in the existing organizational model shown in Fig. 4 can be assigned to $t _ { 1 } .$ . To address this, we add one special role “Any Employee” and assign it to $t _ { 1 }$ by adding a constraint $c _ { 2 8 } \colon$ execute(“Any Employee”, t ). The role executing tasks $\mathrm { t } _ { 2 }$ is resolved based on role hierarchy. We need to add another special role “Supervisor” to execute $t _ { 2 } ,$ in order to achieve constraint consistency. Therefore, one more constraint is added $c _ { 2 9 } \mathrm { : }$ execute(“Supervisor”, t ). For tasks t and $\mathrm { \Delta t _ { 1 0 } , }$ the email system should be the associated resource, which is not part of the organizational model in Fig. 13 either. To solve this problem, we add an machine agent role “Email System” and assign it to $\mathrm { t _ { 9 } }$ and $\mathrm { t } _ { 1 0 }$ by adding two more constraints, i.e., c : execute(“Email System”, t ) and $c _ { 4 1 } { \mathrm { : } }$ execute(“Email System”, $t _ { 1 0 } )$ $t _ { 1 2 }$ (Vender Selection) is a newly inserted task and a resource such as the purchasing manager should be assigned to execute the task.

Changes to the procurement process.

<table><tr><td></td><td>Insertion</td><td>Deletion</td><td>Modification</td></tr><tr><td>Control flow</td><td> $t_{12}$  (Vendor Selection)</td><td> $t_3$  (check fund) $t_{10}$  (archiving) $b_3, f_1, j_1$ </td><td> $t_2$  (Supervisor approval)is revised to checkthe fund</td></tr><tr><td>Organizational model</td><td>None</td><td>role ‘inventory clerk’</td><td>Assign all inventoryclerks as purchasingclerks</td></tr><tr><td>Data Flow</td><td> $d_7$  (request item total)</td><td> $d_2$  (item total value)</td><td>none</td></tr></table>

![](/api/attachments/E4W4EEKC/fulltext/images/cdf2adc984040c593eb26a6c0dc3ae412084ca36c3e33d880d890a091ca1068d.jpg)  
Fig. 11. Procurement process after changes.

Due to the removal of task $t _ { 3 } ,$ Constraints $c _ { 2 }$ and $c _ { 9 }$ become redundant, and Constraint $c _ { 1 3 }$ is now invalid. Because all resource assignment constraints associated with $t _ { 3 }$ are no longer necessary, the separation of duty constraint de<sup>fi</sup>ned on $t _ { 1 }$ and $t _ { 3 }$ is always true, and the routing constraint for $b _ { 2 }$ cannot route the <sup>fl</sup>ow to $t _ { 3 }$ anymore. Similarly, deletion of task $t _ { 1 0 }$ makes its resource assignment constraint $c _ { 1 0 }$ redundant. In the same way, removing $b _ { 3 }$ results in redundant constraints $c _ { 2 3 } ,$ and $c _ { 2 4 } ,$ , and invalid constraints $c _ { 1 5 }$ and $c _ { 1 6 } .$ Renaming data item d makes the related constraints c , c , c , and $c _ { 1 6 }$ invalid. In this section, we used an example to illustrate our algorithm for detecting work<sup>fl</sup>ow constraint anomalies. Next, we further validate our approach by means of a proof-of-concept prototype system based on a rule engine and a work<sup>fl</sup>ow management system.

## 5.3. A proof-of-concept system

Although the anomaly detection algorithm shown in Fig. 10 can be implemented by either procedural languages or declarative languages, we choose a declarative rule-based approach to develop the CWCA prototype system. This is done for three reasons. First, CWCA is based on First Order Logic, which is a natural <sup>fi</sup>t for a rule-based approach. Second, the anomaly detection algorithm is essentially a set of detection rules that can scale up in quantity and may change frequently due to new business requirements. The declarative rule-based approach can handle large number of rules with frequent changes better than a procedural approach [24]. Third, there is a recent trend in industry on integrating rule management systems with other enterprise systems, e.g., work<sup>fl</sup>ow management systems, to better align business with IT [37,39], so that a declarative CWCA implementation can maximally leverage existing organizational assets on rule engines and work<sup>fl</sup>ow management systems.

Fig. 14 shows the architecture of the CWCA prototype system, which contains two sub-systems, i.e. a work<sup>fl</sup>ow management system and a rule management system. In particular, we choose jBPM (http://www.jboss. org/jbossjbpm/) as the work<sup>fl</sup>ow management system and Drools (http:// www.jboss.org/drools/) as the rule management system, because they are both open-source, contain user-friendly development tools based on Eclipse, and provide web-based interfaces for work<sup>fl</sup>ow execution and rule management. Further, both systems are being actively developed and supported by the JBoss community and can be neatly integrated into the JBoss Application Server.

The rules for detecting work<sup>fl</sup>ow constraint anomalies are de<sup>fi</sup>ned using the Drools rule language, which is based on First Order Logic. Fig. 15 shows some anomaly detection rules in the Drools rule workbench in Eclipse. The work<sup>fl</sup>ow model is de<sup>fi</sup>ned using the graphical process designer of jBPM. All basic work<sup>fl</sup>ow modeling constructs we de<sup>fi</sup>ned in Section 4 are supported by the process designer. The process diagram can be exported into an XML <sup>fi</sup>le, which is transformed into rules to create the knowledge base for the detection rules to reason about. After the work<sup>fl</sup>ow model and detection rules are loaded into the rule base, the rule engine performs rule reference and presents the results to the rule design GUI as shown in Fig. 16.

The proof-of-concept prototype system helps demonstrate the feasibility of our CWCA approach and further validates the anomaly detection algorithm via a rule engine. Given that jBPM and Drools can be used as embedded systems and accessed via APIs, the CWCA framework can be integrated into existing applications to provide work<sup>fl</sup>ow capability that supports continuous process improvement.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
start, end,  $t_{1}$ ,  $t_{2}$ ,  $t_{4}$ ,  $t_{5}$ ,  $t_{6}$ ,  $t_{7}$ ,  $t_{8}$ ,  $t_{9}$ ,  $t_{11}$ ,  $t_{12}$ ,  $b_{1}$ ,  $b_{2}$ ,  $b_{4}$ ,  $b_{5}$ ,  $m_{1}$ , next(start,  $t_{1}$ ), next( $t_{1}$ ,  $t_{2}$ ), next( $t_{2}$ ,  $b_{1}$ ), next( $b_{1}$ ,  $b_{2}$ ), next( $b_{1}$ ,  $t_{11}$ ), next( $b_{2}$ ,  $t_{4}$ ), next( $b_{2}$ ,  $t_{5}$ ), next( $t_{4}$ ,  $b_{4}$ ), next( $b_{4}$ ,  $t_{11}$ ), next( $b_{4}$ ,  $t_{5}$ ), next( $t_{5}$ ,  $b_{5}$ ), next( $b_{5}$ ,  $t_{11}$ ), next( $b_{5}$ ,  $t_{8}$ ), next( $t_{12}$ ,  $t_{6}$ ), next( $t_{6}$ ,  $t_{7}$ ), next( $t_{7}$ ,  $t_{8}$ ), next( $t_{8}$ ,  $t_{9}$ ), next( $t_{9}$ ,  $m_{1}$ ), next( $t_{11}$ ,  $m_{1}$ ), next( $m_{1}$ , end)
</div>

manage(GM,ED), manage(GM,PD), manage(GM,AD), manage(ED,SE), manage(PD,PC), manage(PD,DC), manage(AD,AC), belong(John, GM), belong (Joe, ED), belong(Jason, PD), belong(Maggie, AD), belong (Eric, SE), belong(Ray, SE), belong(Peter, PC), belong(Sam, PC), belong(Jack, DC), belong(Dan, DC), belong(Steve, AC), belong(Ben, AC)

Fig. 13. Logic representation of revised org model.

## 6. Discussion

In this section, we compare our Constraint-centric Work<sup>fl</sup>ow Change Analytics (CWCA) framework with some related approaches and discuss limitations of our research. Table 5 shows the comparison results between CWCA and other approaches, namely Petri nets [52,53], Metagraphs [5,6], Communicating Sequential Process (CSP) [58,59], where NA means information not found in the related references.

The <sup>fi</sup>rst issue is the expressive power of the languages used in different approaches in terms of modeling the four work<sup>fl</sup>ow perspectives as de<sup>fi</sup>ned in Section 4, including control <sup>fl</sup>ow, data <sup>fl</sup>ow, organizational model, and work<sup>fl</sup>ow constraints. Petri nets with its extensions including colored, timed, and hierarchical Petri nets and Metagraphs have been applied to represent control <sup>fl</sup>ow, data <sup>fl</sup>ow, and organizational models. Work<sup>fl</sup>ow constraints are essentially declarative rules, which cannot be easily represented by graphical formalisms such as Petri nets and Metagraphs. CSP has been used to provide formal semantics to BPMN [59], thus representing control <sup>fl</sup>ow and data <sup>fl</sup>ow. Work<sup>fl</sup>ow constraints are essentially declarative rules, which have been represented using First Order Logic in many research works. Although there has been research on translations between logic programs and Petri net models [32,48], research on leveraging Petri nets, Metagraphs, or CSP to model work<sup>fl</sup>ow constraints has been scant. In comparison with other three approaches, CWCA enables a uni<sup>fi</sup>ed representation of all four work<sup>fl</sup>ow perspectives by attaching formal work<sup>fl</sup>ow semantics to First Order Logic. However, the expressive power of CWCA framework de<sup>fi</sup>ned in this paper in terms of modeling different work<sup>fl</sup>ow patterns are limited compared with Petri nets and CSP [54,59]. Therefore, extending CWCA's expressiveness is an important future research topic.

The second issue is supporting multi-perspective changes. One of the key innovations of CWCA is the ability to analyze change consequences among all four work<sup>fl</sup>ow perspectives within one uni<sup>fi</sup>ed constraintcentric framework. Petri nets have been applied to study change interactions within control <sup>fl</sup>ow and between control <sup>fl</sup>ow and data <sup>fl</sup>ow. In this paper, we focus on de<sup>fi</sup>ning multi-perspective work<sup>fl</sup>ow changes and analyzing basic change anomalies, thus leaving change veri<sup>fi</sup>cation within a single perspective, such as control <sup>fl</sup>ow veri<sup>fi</sup>cation, to future research. Given CWCA is grounded on First Order Logic, it can be extended to control <sup>fl</sup>ow veri<sup>fi</sup>cation using the methods found in [10,21]. Furthermore, we are planning to analyze more complex change interactions among different perspectives using CWCA.

The third issue is the capability of handling dynamic work<sup>fl</sup>ow change. Dynamic work<sup>fl</sup>ow changes refer to the problem of managing change consequences to running instances of a work<sup>fl</sup>ow [12]. Petri nets have been extensively used in handling dynamic work<sup>fl</sup>ow changes [53]. Metagraphs and CSP have not been used to study work<sup>fl</sup>ow changes. In this paper, CWCA only deals with static change consequences during the work<sup>fl</sup>ow design time. However, CWCA could be extended to support dynamic work<sup>fl</sup>ow changes. More speci<sup>fi</sup>cally, additional predicates will need to be de<sup>fi</sup>ned to represent instances of work<sup>fl</sup>ow components and additional rules need to be speci<sup>fi</sup>ed for handling dynamic change anomalies. For instance, once a task is activated and a resource is assigned to the task instance, we could use execute\_instance (instance\_id, task\_name, resource\_id) to represent this resource assignment and create an additional rule: missing\_resource (resource\_id) ←execute\_instance (instance\_id, task\_name, resource\_id), not resource(resource\_id, resource\_name) to show a temporal missing resource anomaly whenever a resource become occupied when the corresponding task is still active.

The fourth issue is about the veri<sup>fi</sup>cation mechanism and tool supports. All four approaches shown in Table 5 are grounded in rigorous veri<sup>fi</sup>cation mechanisms. However, supporting tools for the Metagraphs approach has not been found. Although CPN Tools for Petri nets approach and FDR Model Checker for CSP approach are powerful tools widely used in research projects and industry practice, their supports in existing work<sup>fl</sup>ow management systems are very limited. The CWCA approach can be implemented using any rule engines as illustrated in Section 5.3. Various industry-strength rule engines are either freely available, such as Drools, XSB, CLIPS, and JESS, or have been offered by many leading software vendors, such as IBM ILOG, Oracle Business Rules, and Microsoft Windows Work<sup>fl</sup>ow Foundation Rules Engine. Thus, organizations can leverage more easily their existing IT assets to implement CWCA. We are re<sup>fi</sup>ning and enhancing the prototype system and plan to use it in real organizations to further validate CWCA approach. Based on our experience with several work<sup>fl</sup>ow modeling and management systems, such as

![](/api/attachments/E4W4EEKC/fulltext/images/e36ba8fbd30e18af9d217ce6390cb9a6882749da29bccc6381e9397eaf761f8f.jpg)  
Fig. 14. Architecture of the prototype system.

![](/api/attachments/E4W4EEKC/fulltext/images/988217f170ba6710ab7050d846340559185265aa82ef6c72bc94eac9363ee7f0.jpg)  
Fig. 15. Anomaly detection rules in drools rule workbench.

Ultimus BPM Suite 7, jBoss jBPM, and IBM Websphere Business Modeler, there is no systematic support for multi-perspective work<sup>fl</sup>ow change analytics in those systems. For instance, Ultimus cannot detect defective data constraint anomaly during work<sup>fl</sup>ow design time and can only <sup>fi</sup>nd task-without-resource anomaly during simulation. For jBoss jBPM, work<sup>fl</sup>ow constraints need to be manually speci<sup>fi</sup>ed in work<sup>fl</sup>ow model speci<sup>fi</sup>cation <sup>fi</sup>le using jPDL language. Thus, jBPM does not provide any support for design-time work<sup>fl</sup>ow change analysis. IBM Websphere Business Modeler can detect some of the change anomalies via their proprietary approaches, such as missing routing constraint anomaly, non-existing resources anomaly, and missing routing data item anomaly. It prevents some anomalies, such as the missing resource anomaly, by assigning a default built-in resource to any new task. However, IBM does not provide a systematic discussion on how IBM Webshphere Business Modeler handles work<sup>fl</sup>ow changes.

Another important issue is about the performance of rule engines in terms of supporting large number of facts and rules. Many benchmarking and performance tests have been conducted to analyze and evaluate the performance and scalability of different rule engines [4,27,33]. The recent OpenRuleBench project (http://rulebench.projects.semwebcentral.org/) evaluates eleven rule engines with different technologies, such as XSB, Yap, Ontobroker, Jess, and Drools, for their performance and scalability for a number of problems using large data sets with up to 1,000,000 facts [33]. The results show that many rule engines have reasonable performance with large data sets. For example, the Wine ontology has 815 rules and 654 facts and many of its predicates are recursively dependent on each other through chains of rules. In the Wine ontology test, many rule engines, such as XSB and Ontobroker, can complete the evaluation test within few seconds. Drools, the rule engine we use to develop our prototype system, achieved the best score for the DBLP test, which contains 2,500,000 facts, but lagged behind other systems for other tests [33]. Given that our CWCA approach is based on First Order Logic, we could leverage any rule engine with the best performance to implement our approach. Drools is developed based on the well-known RETE algorithm, we can evaluate the performance of our approach more formally by leveraging research on the computational complexity of RETE [23]. Given the number of rules (P), number of facts (W), and average number of patterns/conditional elements (C), the algorithmic complexity of RETE in average case and worst case are O(PW) and O(PW<sup>c</sup>) respectively. As shown in the Section 5, we de<sup>fi</sup>ned ten scenarios for work<sup>fl</sup>ow constraint anomalies in total, so that P and C for our CWCA approach are relatively small numbers. W in CWCA depends on the number of tasks, data items, constraints, and their relationships, which varies for different work<sup>fl</sup>ow models. Based on our case study of several process reference models from vendors such as SAP, and Oracle [55], most work<sup>fl</sup>ows in enterprises have only dozens of tasks and constraints. Therefore, W in our proposed CWCA knowledge base should be much smaller than the data sets used in the OpenRuleBench tests aforementioned and our proposed system should be able to handle most work<sup>fl</sup>ow change analysis with good performance.

![](/api/attachments/E4W4EEKC/fulltext/images/501102c0eeff7dabbfc093d9d5ff1b4b830a9c5c22904c1c1fc7798cfb55df55.jpg)  
Fig. 16. A screenshot of constraint detection results.

Besides the issues discussed above, there are other challenges for implementing CWCA. For example, work<sup>fl</sup>ow models are usually speci<sup>fi</sup>ed using different notations, such as BPMN, Petri nets, BPEL, and EPCs, and CWCA may be implemented using different rule engines with different rule languages. Translating work<sup>fl</sup>ow models in different notations into the logic formulas in different rule languages is challenging tedious process. Another challenge is the integration of a rule engine into the work<sup>fl</sup>ow system for seamless analysis of work<sup>fl</sup>ow changes. Some rule engines, such as Drools, can be easily embedded into Java application, whereas other rules systems, such as WebSphere ILOG Business Rule Management Systems, must be accessed via APIs. Given the heterogeneity of various implementation environments, seamlessly integration of CWCA with existing work-<sup>fl</sup>ow management system requires additional research.

## 7. Conclusions

In order to support continuous process improvement systematically, there is a critical need to manage work<sup>fl</sup>ow changes more rigorously. In this paper, we presented a constraint-centric analytical approach for managing work<sup>fl</sup>ow changes, named Constraint-centric Work<sup>fl</sup>ow Change Analytics (CWCA). CWCA advocates a uni<sup>fi</sup>ed view of work<sup>fl</sup>ow changes based on work<sup>fl</sup>ow constraint analysis and enables a comprehensive representation of multiple work<sup>fl</sup>ow perspectives for the purpose of detecting work<sup>fl</sup>ow change anomalies. More speci<sup>fi</sup>cally, multi-perspective work<sup>fl</sup>ow change anomalies are formally de<sup>fi</sup>ned and classi<sup>fi</sup>ed into four categories, namely, missing, redundant, defective, and con<sup>fl</sup>icting anomalies. In order to validate the CWCA approach, we developed an anomaly detection algorithm and a proof-of-concept system using a rule-based approach. Our research <sup>fi</sup>lls a critical void in work<sup>fl</sup>ow change management and has signi<sup>fi</sup>cant impact on continuous process improvement and work<sup>fl</sup>ow management. The CWCA approach presented in this paper has some unique features and innovations compared with the existing body of work on work<sup>fl</sup>ow modeling and change management. At the same time, CWCA has great potential for future extensions and re<sup>fi</sup>nements to provide more utility for work<sup>fl</sup>ow change management.

Table 5  
Comparison between CWCA and other approaches.

<table><tr><td></td><td>CWCA</td><td>Petri nets</td><td>Metagraphs</td><td>CSP</td></tr><tr><td>Control flow</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Data flow</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Org model</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>Constraint</td><td>Yes</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Static change</td><td>Yes</td><td>Yes</td><td>NA</td><td>NA</td></tr><tr><td>Multi-perspective change support</td><td>Yes</td><td>Some</td><td>Some</td><td>NA</td></tr><tr><td>Dynamic change</td><td>No</td><td>Yes</td><td>NA</td><td>NA</td></tr><tr><td>Verification Mechanism</td><td>Rule inference</td><td>Petri-nets-based Simulation</td><td>Matrix Operations</td><td>Model Checking</td></tr><tr><td>Tool support</td><td>Rule engines</td><td>CPN tools</td><td>NA</td><td>FDR model checker</td></tr></table>

## Acknowledgement

This work was partially supported by a SRG grant from the City University of Hong Kong (No. 7002522).

## References

[1] N.R. Adam, V. Atluri, W.K. Huang, Modeling and analysis of work<sup>fl</sup>ows using Petri nets, Journal of Intelligent Information Systems 10 (2) (1998) 131–158.

[2] T. Andrews, et al., Business process execution language for web services, version 1.1, BEA Systems, IBM Corp., Microsoft Corp., SAP AG, Siebel Systems, May 5 2003.

[3] V. Atluri, W.-k. Huang, V. Atluri, W.-k. Huang, An authorization model for work<sup>fl</sup>ows, Proceedings of Proceedings of the 4th European Symposium on Research in Computer Security: Computer Security, 1996, pp. 44–64

[4] M. Bali, Drools JBoss rules 5.0 Developer's Guide, Packt Publishing, 2009.

[5] A. Basu, R.W. Blanning, A formal approach to work<sup>fl</sup>ow analysis, Information Systems Research 11 (1) (2000) 17-36.

[6] A. Basu, R.W. Blanning, Synthesis and decomposition of processes in organizations, Information Systems Research 14 (4) (2003) 337–355.

[7] A. Basu, A. Kumar, Research commentary: work<sup>fl</sup>ow management issues in e-Business, Information Systems Research 13 (1) (2002) 1–14.

[8] B. Berthomieu, M. Diaz, T. Cnrs, Modeling and veri<sup>fi</sup>cation of time dependent systems using timePetri nets, IEEE Transactions on Software Engineering 17 (3) (1991) 259-273.

[9] E. Bertino, E. Ferrari, V. Atluri, The speci<sup>fi</sup>cation and enforcement of authorization constraints in work<sup>fl</sup>ow management systems, ACM Transactions on Information and System Security 2 (1) (1999) 65–104.

[10] H.H. Bi, J.L. Zhao, Applying propositional logic to work<sup>fl</sup>ow veri<sup>fi</sup>cation, Information Technology and Management 5 (3-4) (2004) 293-318.

[11] M.B. Blake, H. Gomaa, Agent-oriented compositional approaches to services-based cross-organizational work<sup>fl</sup>ow, Decision Support Systems 40 (1) (2005) 31–50.

[12] F. Casati, S. Ceri, B. Pernici, G. Pozzi, Work<sup>fl</sup>ow evolution, Data & Knowledge Engineering 24 (3) (1998) 211–238.

[13] F. Casati, S. Ceri, S. Paraboschi, G. Pozzi, Speci<sup>fi</sup>cation and implementation of exceptions in work<sup>fl</sup>ow management systems, ACM Transactions on Database Systems 24 (3) (1999) 405–451.

[14] F. Casati, S. Castano, M. Fugini, I. Mirbel, B. Pernici, Using patterns to design rules in work<sup>fl</sup>ows, IEEE Transactions on Software Engineering 26 (8) (2000) 760–785.

[15] F. Casati, S. Castano, M. Fugini, Managing work<sup>fl</sup>ow authorization constraints through active database technology, Information Systems Frontiers 3 (3) (2001) 319–338.

[16] M. Chen, D. Zhang, L. Zhou, Empowering collaborative commerce with Web services enabled business process management systems, Decision Support Systems 43 (2) (2007) 530–546.

[17] D.K.W. Chiu, Q. Li, K. Karlapalem, A meta modeling approach to work<sup>fl</sup>ow management systems supporting exception handling, Information Systems 24 (2) (1999) 159–184.

[18] T. Curran, G. Keller, A. Ladd, SAP R/3 business blueprint : understanding the business process reference model, Prentice Hall PTR, Upper Saddle River, N.J., 1998.

[19] B. Curtis, M.I. Kellner, J. Over, Process modeling, Communications of the ACM 35 (9) (1992) 75–90

[20] S.K. Das, Deductive databases and logic programming, Addison-Wesley, 1992

[21] H. Davulcu, M. Kifer, C.R. Ramakrishnan, I.V. Ramakrishnan, Logic based modeling and analysis of work<sup>fl</sup>ows, Proceedings of the 17th ACM SIGACT-SIGMOD-SIGART symposium on Principles of database systems, 1998, pp. 25–33.

[22] C. Ellis, K. Keddara, ML-DEWS: modeling language to support dynamic evolution within work<sup>fl</sup>ow systems, Computer Supported Cooperative Work 9 (2000) 293–333.

[23] C.L. Forgy, Rete: A fast algorithm for the many pattern/many object pattern match problem, Arti<sup>fi</sup>cial Intelligence 19 (1) (1982) 17–37.

[24] J.C. Giarratano, G. Riley, Expert systems: principles and programming, Course Technology (2005).

[25] M. Gruninger, C. Menzel, The process speci<sup>fi</sup>cation language (PSL) theory and applications, AI magazine 24 (3) (2003) 63–74.

[26] M. Gruninger, R. Hull, S.A. McIlraith, Short overview of <sup>fl</sup>ows: a <sup>fi</sup>rst-order logic ontology for web services, Bulletin of the IEEE Computer Society Technical Committee on Data Engineering (2008).

[27] Illation Ltd, Business Rule Engine Benchmarks, http://illation.com.au/benchmarks 2007.

[28] K. Jensen, Coloured Petri nets: basic concepts, analysis methods, and practical use, Springer, 1992.

[29] P.J. Kammer, G.A. Bolcer, Richard N. Taylor, A.S. Hitomi, M. Bergman, Techniques for Supporting Dynamic and Adaptive Work<sup>fl</sup>ow, Computer Supported Cooperative Work 9 (2000) 269–292

[30] N. Kavantzas, D. Burdett, G. Ritzinger, T. Fletcher, Y. Lafon, C. Barreto, Web services choreography description language version 1.0, W3C Working Draft 17 (2004)8 10- 20041217.

[31] M. Klein, C. Dellarocas, A knowledge-based approach to handling exceptions in work<sup>fl</sup>ow systems, Computer Supported Cooperative Work 9 (2000) 399–412.

[32] L. Li, High-level Petri net model of logic program with negation, IEEE Transactions on Knowledge and Data Engineering 6 (3) (1994) 382–395.

[33] S. Liang, P. Fodor, H. Wan, M. Kifer, OpenRuleBench: an analysis of the performance of rule engines, Proceedings of 18th International World Wide Web Conference, Madrid, Spain, 2009.

[34] R. Liu, A. Kumar, W. Van Der Aalst, A formal modeling approach for supply chain event management, Decision Support Systems 43 (3) (2007) 761–778.

[35] D. Madison, Process Mapping, Process Improvement and Process Management, Paton Press, 2005.

[36] A. Margaris, First order Mathematical logic, Courier Dover Publications, 1990

[37] T. Morgan, Business rules and information systems: aligning IT with business goals, Addison-Wesley Professional, 2002.

[38] S. Mukherjee, H. Davulcu, M. Kifer, P. Senkul, G. Yang, Logic Based Approaches to Work<sup>fl</sup>ow Modeling and Veri<sup>fi</sup>cation, Logics for Emerging Applications of Databases, Springer, 2003, pp. 167–203.

[39] Oracle, State of the Business Process Management Market 2008, 2008

[40] M. Reichert, P. Dadam, ADEPT<sup>fl</sup>ex: supporting dynamic changes of work<sup>fl</sup>ows without losing control, Journal of Intelligent Information Systems 10 (2) (1998) 93–129.

[41] R.G. Ross, The business rule approach, IEEE Computer 36 (5) (2003) 85–87.

[42] S.J. Russell, P. Norvig, J.F. Canny, J. Malik, D.D. Edwards, Arti<sup>fi</sup>cial intelligence: a modern approach, Prentice Hall Englewood Cliffs, NJ, 1995.

[43] N. Russell, W.M.P.v.d. Aalst, A.H.M.t. Hofstede, D. Edmond, Work<sup>fl</sup>ow resource patterns: identi<sup>fi</sup>cation, representation and tool support, Proceedings of Proceedings of the 17th International Conference on Advanced Information Systems Engineering (CAiSE 05), Porto, Portugal, 2005.

[44] S.W. Sadiq, O. Marjanovic, M.E. Orlowska, Managing change and time in dynamic work<sup>fl</sup>ow processes, International Journal of Cooperative Information Systems 9 (1–2) (2000) 93–116.

[45] S. Sadiq, M. Orlowska, W. Sadiq, C. Foulger, Data <sup>fl</sup>ow and validation in work<sup>fl</sup>ow modelling, Proceedings of the Fifteenth Conference on Australasian Database, Dunedin, New Zealand, 2004, pp. 207–214.

[46] D. Sangiorgi, D. Walker, The pi-calculus: a theory of mobile processes, Cambridge University Press, 2001.

[47] A.-W. Scheer, ARIS — business process modeling, Third ed.Springer, 2000

[48] T. Shimura, J. Lobo, T. Murata, An extended Petri net model for normal logic programs, IEEE Transactions on Knowledge and Data Engineering 7 (1) (1995) 150–162.

[49] E.A. Stohr, J.L. Zhao, Work<sup>fl</sup>ow automation: overview and research issues, Info. Systems Frontiers: Special Issue on Work<sup>fl</sup>ow Automation 3 (3) (2001) 281–296.

[50] S.X. Sun, J.L. Zhao, J.F. Nunamaker, O.R.L. Sheng, Formulating the data <sup>fl</sup>ow perspective for business process management, Information systems research 17 (4) (2006) 374–391.

[51] SWSF Committee, Semantic Web Service Ontology (SWSO): First-order Logic Ontology for Web Services (FLOWS), 2005.

[52] W.M.P. van der Aalst, The application of Petri nets to work<sup>fl</sup>ow management, Journal of Circuits, Systems and Computers 8 (1) (1998) 21–66.

[53] W.M.P. van der Aalst, Exterminating the dynamic change bug: a concrete approach to support work<sup>fl</sup>ow change, Information Systems Frontiers 3 (3) (2001) 297–317.

[54] W.M.P. van der Aalst, A.H.M. ter Hofstede, B. Kiepuszewski, A.P. Barros, Work<sup>fl</sup>ow patterns, Distributed and Parallel Databases 14 (3) (2003) 5–51.

[55] H.J. Wang, H. Wu, Supporting process design for e-business via an integrated process repository, Information Technology and Management (in press).

[56] H.J. Wang, J.L. Zhao, L.-J. Zhang, Policy-Driven Process Mapping (PDPM): discovering process models from business policies, Decision Support Systems 48 (1) (2009) 267–281.

[57] WfMC, XPDL 2.1 Speci<sup>fi</sup>cation, http://www.wfmc.org/index.php?option= com\_docman&task=doc\_details&gid=132&Itemid=126, 2008.

[58] P.Y.H. Wong, J. Gibbons, A process-algebraic approach to work<sup>fl</sup>ow speci<sup>fi</sup>cation and re<sup>fi</sup>nement, Lecture Notes in Computer Science 482 (9) (2007) 51.

[59] P.Y.H. Wong, J. Gibbons, A process semantics for BPMN, Proceedings of 10th International Conference on Formal Engineering Methods, 2008.

[61] M. zur Muhlen, Organizational management in work<sup>fl</sup>ow applications — issues and perspectives, Information Technology and Management 5 (3) (2004) 271–291.

Harry Jiannan Wang is an Assistant Professor of Management Information Systems in the Lerner College of Business and Economics at the University of Delaware. He received Ph.D. in Management Information Systems from the Eller College of Management, University of Arizona, and B.S. in Management Information Systems from Tianjin University, China. His research interests involve business process management, work<sup>fl</sup>ow technologies and applications, services computing, and enterprise systems. He has published several research articles in academic journals and conferences such as Decision Support Systems, Communication of the AIS, Information Technology and Management, International Journal of Web Services Research, Journal of Information Systems and E-Business Management JEEE IT Professional International Conference on Information Systems (ICIS), Workshop on Information Technologies and Systems (WITS), and Americas Conference on Information Systems (AMCIS).

J. Leon Zhao is Head and Chair Professor in Information Systems, City University of Hong Kong. He was Eller Professor in the Department of Management Information Systems, University of Arizona before January 2009. He also taught previously at HKUST and College of William and Mary, respectively. He holds Ph.D. and M.S. degrees from the Haas School of Business, UC Berkeley, M.S. degree from UC Davis, and B.S. degree from Beijing Institute of Agricultural Mechanization. His research is on information technology and management, with a particular focus on work<sup>fl</sup>ow technology and applications in knowledge distribution, e-learning, supply chain management, organizational performance management, and services computing. His research has been supported by NSF, SAP, and other sponsors. He received an IBM Faculty Award in 2005 for his work in business process management and services computing and was awarded Chang Jiang Scholar Chair Professorship at Tsinghua University by the Ministry of Education of China in 2009. He has been associate editor of ACM Transactions on MIS, Information Systems Research, IEEE Transactions on Services Computing, Decision Support Systems, and Electronic Commerce Research and Applications. He has been chair or program chair for numerous conferences including the 5th International Conference on Design Science Research in Information Systems and Technology (DESRIST’10), the IEEE International Conference on Services Computing, Bangalore, India (SCC’09), the 2007 China Summer Workshop on Information Management (CSWIM'07), and the 2005 Workshop on Information Technology and Systems (WITS'05).
