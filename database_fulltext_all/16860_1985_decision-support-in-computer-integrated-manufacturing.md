---
otero_id: 16860
otero_key: "FDPGEYTS"
title: "Decision support in computer-integrated manufacturing"
authors: "Suranjan De; Shimon Y Nof; Andrew B Whinston"
year: "1985"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(85)90196-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
agencies in the United States, Canada, and Israel.

# Decision Support in Computer-Integrated Manufacturing

Suranjan De $^{+}$ , Shimon Y. Nof $^{*}$ and

Andrew B. Whinston $^{+}$

\* School of Industrial Engineering and

$^{+}$ Krannert Graduate School of Management,

Purdue University, West Lafayette, IN 47907, USA

This is a survey paper that addresses the issue of decision support in computer-integrated manufacturing (CIM). Since the complexity of the decision making process in manufacturing stems from the multilevel nature of the planning hierarchy, we emphasize the importance of adopting an integrated view of the planning hierarchy. We provide a framework for the development of a DSS for integrated manufacturing control that emphasizes a systems approach. Besides we consider some of the architectural aspects of a DSS in CIM. In particular, the specific architectural aspects of the management of data in CIM have been discussed at length.

Keywords: Decision Support System; Computer-Integrated Manufacturing; Manufacturing Systems Control; Muttilevel Planning Hierarchy; Data and Model Management; User Interface

![](/api/attachments/FDPGEYTS/fulltext/images/6b6ba8ed50167ef7810f4391a4635d7bf2d32dac4f2e3ab8e51048a39d5a7b55.jpg)  
Suranjan De is a graduate student in Management Information Systems at Purdue University. His research interests include decision support systems, natural language processing, applications of artificial intelligence to manufacturing problems, and distributed processing.

Research supported in part by the National Science Foundation, Grant No. IST-8108519 and Grant No. ECS-8116135, a grant from the Computer Integrated Design Manufacturing and Automation Center, and a gift from the IBM corporation to the Management Information Research Center. Opinions expressed are those of the authors.

## 1. Introduction

Management is the art and science of coordinating human and material resources subject to some set of objectives and constraints. Some of these decision problems are structured and capable of being resolved almost automatically; other problems are of the semistructured or the unstructured variety. Numerical control decisions required in machining a particular workpiece are generally structured, as reflected by the programmability of the decision process in a NC part program [5]. On the other hand, a manufacturing organization's long-range plans are based on crude information and rough analysis and therefore are highly unstructured. However, the importance of these unstructured decisions can hardly be overstated.

![](/api/attachments/FDPGEYTS/fulltext/images/6a80f336ff9a806733b007b5e4e6349b5a8b6d1e5dfd2a02738f0eb7b9c58a6e.jpg)

Shimon Y. Nof is an Associate Professor of Industrial Engineering at Purdue University. He received Ph.D. in Industrial and Operations Engineering at the University of Michigan. He is editor of The Handbook of Industrial Robotics, to be published by John Wiley and Sons in 1985. His research interests include planning and control of computerized production facilities, industrial information systems, and robotics, areas in which he has consulted to companies and government

![](/api/attachments/FDPGEYTS/fulltext/images/c27154be8e4ff852748b119f1ec09d2e1b33da7aad047e529679f6320936f751.jpg)

Andrew B. Whinston is a Professor of the Krannert Graduate School of Management at Purdue University. His primary teaching interest is management information systems. His current research interests include data base management and applications of artificial intelligence to economics and management on which he also consults. He has also studied applied economics, regulatory economics, and accounting theory. He has co-authored two books (with C. Holsapple and R.

Bonczek), Foundations of Decision Support Systems (Academic Press, 1981), and Micro Database Management - Practical Techniques for Application Development (Academic Press, 1985).

These plans commit the manufacturing organization to resource levels, product mixes, and sales and inventory policies that constrain more detailed planning at the intermediate- and short-range planning levels.

In recent years, effort has been directed toward the contribution of computers to improved decision making. Hence, it is of interest to examine the nature of systems that support the decision making activity. In this paper, we focus on the issue of providing computer-aided decision support in a manufacturing environment in general and a computer-integrated manufacturing environment in particular. Now in a manufacturing environment, the high degree of interdependency among machines, material handling devices, and other process resources requires a large number of timely decisions at the various levels of operation to be made. Due to the dynamic nature of the manufacturing environment, decision problems are often unstructured, and have to be continuously reviewed in view of the changing status of the system. The objective of providing decision support in manufacturing can be two-fold:

(i) To implement automatic control for structured decisions; and

(ii) To provide modeling capability and decision power for unstructured decisions.

The organization of this paper is as follows. Before we address the issue of decision support in manufacturing in greater detail, we shall discuss decision support systems in general. In Section 2, we describe the generic structure of a decision support system. In Section 3, we discuss the various issues involved in manufacturing planning and how they can be addressed using the framework discussed in Section 2. Section 4 discusses the issue of architectural aspects of DSS in manufacturing.

Section 5 discusses some of the architectural issues involved in the management of data in manufacturing. Section 6 summarizes the paper and indicates the scope of future research.

## 2. Generic Structure of a Decision Support System

Conceptually, a DSS consists of three principal components: a language system (LS), a knowledge system (KS) and a problem processing system (PPS) [2]. A language system is the total of all linguistic facilities made available to the decision maker by a DSS. It is characterized by the syntax and semantics that it furnishes to the decision maker, by the statements, commands or expressions that it allows the user to make. A knowledge system is the knowledge about a problem domain that is stored in the DSS. A problem processing system is the interfacing mechanism between the KS and the LS. The PPS lies at the heart of a DSS and its primary function is to accept problems represented with the LS and to utilize application-specific knowledge represented in the KS to generate information for decision support via LS. The LS and the KS are representation systems whereas the PPS is the dynamic component of the DSS. This generic description of a DSS structure is shown in Figure 1.

The language system referred to above is a vehicle that allows the decision maker or user to convey information to the DSS. Through the LS, the user can state the problems to the DSS. Besides, the LS is a two way avenue through which the decision maker and the PPS can interact. The syntactic and semantic rules of a LS determine the permissible problem statements that can be posed to a DSS. LSs vary in terms of the level of procedurality that they require for expressing a problem [2]. At one extreme are procedural languages that allow a user to state a problem by specifying the procedural steps (involving retrieval and/or computations) to be used in solving that problem. At the other extreme are nonprocedural languages that allow a problem to be specified by merely stating the characteristics of the problem's solution. In order that a DSS in manufacturing be user-friendly, it is imperative that the LS be flexible as well as efficient. From the user's perspective, a natural language such as English would be ideal because that provides maximal flexibility of expression to the users. However, natural languages are inherently difficult to parse because of their context-sensitive nature. Therefore, a more formal language might be preferred from an implementation point of view. The following are some of the research issues involved in the design of a language system of a DSS:

![](/api/attachments/FDPGEYTS/fulltext/images/ff265c19fd9a0b115999e581bd02d314b4f6ff20f90fd34608c9e37c7a47d156.jpg)  
Fig. 1. Structure of a Decision Support System.

(i) The formulation to describe a language system – the formalism should be easily understood, implementable and modifiable;

(ii) The storage mechanism of the aforementioned formalism – there seems to be two possible choices: either to treat the language processing in isolation or to attempt an integration in the knowledge representation framework; the former option needs a separate parser whereas the latter option can let the PPS do the parsing;

(iii) The choice of a target language in natural language proceeding.

It might be interesting to consider the possibility of using the same language at all levels of the language system. A single language adds to the elegance and economy of representation of the system. In order to determine an appropriate choice of a language, we ought to consider a language that is concise and semantically correct. One such choice is PROLOG which is a non-procedural language based on the Horn clause subset of first-order predicate calculus [25]. However, PROLOG has the disadvantage that it uses backtracking as a processing strategy and hence it might be expensive in practice. Instead we could use the language of equational logic [26] which is somewhat restricted in scope but avoids backtracking. The essential idea of the equational approach is to somehow constrain the specification of the assertions constituting the language system, thereby improving the 'performance of the LS because the restricted set of assertions allows us to avoid backtracking. The equational approach could allow us to represent the LS not only at the logical level but also at its physical level. The physical storage can also be represented using the equational approach.

A knowledge system is characterized by the facilities it furnishes for the representation and organization of knowledge. Knowledge represented in a KS must be retained in an organized, systematic manner. The knowledge representation method utilized by a particular KS may be thought of as a set of rules according to which knowledge is expressed for purposes of retention within the decision support system. KSs vary not only in terms of the knowledge they contain but also in the differing approaches that they utilize to represent and organize knowledge. If a data base is employed, it may offer relational, hierarchical or network constructs. Other knowledge representation methods include those from the artificial intelligence area, such as the predicate calculus and the production system approaches. In some cases, it may be desirable to integrate two or more of these approaches for use in a single system. Some of these issues are discussed in greater detail in Section 3.

The problem processing system is the formal specification of a DSS' behavior patterns. A PPS must possess the ability to explicitly recognize problems by transforming problem statements into appropriate executable plans of action. A PPS has explicitly recognized a problem when a problem statement has been converted into a detailed procedural specification, which, when executed, yields an answer to the problem. for LSs that require only a procedural problem statement, the PPS problem recognition ability is at most rudimentary. Non-procedural problem statements may necessitate a more sophisticated problem recognition ability. If a user directly specifies or selects a model through the LS, then there is no need for the PPS to recognize the modeling problem. A highly sophisticated problem recognition ability may be required if a PPS itself is to select or formulate a model [3]. Another important PPS ability is that of analysis. It is the process of interfacing models with data in order to generate assertions.

## 3. Decision Making in Manufacturing

## 3.1. Nature of the Manufacturing Environment

Manufacturing encompasses all those functions from the receipt of a product to the satisfactory completion of an acceptable end item. The basic structure of the manufacturing environment has been discussed at length in [4]. Here we merely point out some of the salient points.

Production is primarily a sequential process in which a set of discrete functions are performed on materials. The discrete functions are of two types.

(1) The first type is one of materials handling in which material is moved from one operation point to another in a predetermined pattern and sequence.

(2) In the second, operations are performed by people or by machines as a result of which materials are converted from an input state to a desired output state.

Now the operations are performed in a sequence of events that is a combination of four basic patterns:

(a) Disjunctive, where material is disassembled into useful components;

(b) Locational, where material is stored for a period of time without change;

(c) Sequential, where one piece of material is progressively modified by operations;

(d) Combinative, where separate pieces are selected and assembled into a functional end product [4].

As was mentioned earlier the management of manufacturing can be categorized into three levels:

(a) The strategic level, where decisions specify what to do;

(b) The tactical level, where decisions specify how and were to do it; and

(c) The operational level, where decisions are converted into action [6].

This aspect will be discussed at length in Section 3.2.

Managerial control is exercised by and on the basis of communications between levels. Order and directives flow downward from the managerial to the planning, and then to the working level, and reports on accomplishment flow upward along the reverse path. Hence management is a closed loop of activities in the manufacturing world: making plans, issuing instructions, collecting data on accomplishment, and making decisions which, in effect, restructure the plans [4]. Therefore, the managerial loop is iterative whether the objective of manufacture is a single production effort or a continual production effort. it is important to note that the foregoing loop of activities involves no materials handling of any sort. What is handled is information, and this basic distinction clearly distinguishes managerial activities from the shop floor activities.

In a computer-integrated manufacturing environment the same basic structure as discussed above exists. However, computers are used to a greater degree in the manipulation of data involved at all levels of manufacturing. The most basic level involves the control of tools in executing their function upon the material and the movement of the material from one piece of machinery to another. At the next level, the complex problems of scheduling the flow of specific products through the plant are solved, and at the top level, the managerial decisions based on commitments and accomplishments are reached. Another way of viewing the computer integrated manufacturing environment is to take an information processing point of view according to which data are collected, decisions are reached based upon this information and instructions resulting from these decisions are dispatched to the working elements of the organization. The widespread use of computers in manufacturing should not obscure the fact that it is the flow of data rather than the medium of data flow which is of prime importance. It is true, of course, that the nature of the computer and its interconnections and peripheral equipment will control the volume and handling of data.

Before we proceed to discuss the issues of planning and control, we would briefly like to point out that the introduction of the computer will have a significant effect on the nature of the entire manufacturing environment. Products will be designed or redesigned so that they can be produced utilizing the fullest capabilities of the computerized machines. Product definitions will be restyled so that they can be stored in and handled by the computer. Planning and scheduling will become far more precise and better controlled. Set-up and production time will be better controlled. Machinery will be designed to take direct numerical control from the computer and yield service data on production directly to the computer. Factories will be arranged or rearranged to take full advantage of computer-directed automated materials handling. Materials will be more closely controlled to match more closely controlled machinery. Manpower, operator and supervisor alike, will have to be retrained. Such computer-integrated manufacturing systems will provide increased flexibility while attempting to achieve the efficiency of the conventional mass production systems in manufacturing. The increased flexibility will create the need to develop new and appropriate planning and control procedures to take advantage of the system's capabilities for higher production rates as well as a wide variety of products. Since often such systems will have to be flexible enough to handle the production of a wide variety of customized products, it is extremely likely that customers will opt for products that are made to their particular specifications. Hence computer integrated manufacturing systems will become an attractive substitute for the conventional means of batch manufacturing.

## 3.2. Multilevel Planning Hierarchy

Because of the dynamic nature of the manufacturing environment, planning and control decisions are critical to the overall performance of the system. In order to deal with such an environment, it is necessary to provide manufacturing systems with the control capability to make decisions for unstructured, ill-defined problems such as machine breakdown, change in priority, design changes, etc. And in order to respond to such problems, it is important for the DSS to have an integrated view of the multilevel planning hierarchy.

The complexity of the decision making process in manufacturing stems in part from the multilevel nature of the manufacturing planning and control process. Based on the length of the planning horizon and the associated functions, decision making in manufacturing involves three main levels of activities: (i) the long-range or the strategic level; (ii) the intermediate range or the tactical level; and (iii) the short range or the operational level [6]. Plans and decisions which affect the lower levels are made at the long-range management level. At the intermediate range management level, plans and decisions are made which affect the short-range management level, and progress on long-range plans and decisions is monitored. At the short-range management level, decisions are made which affect utilization of resources made available via decisions at the higher levels, and which affect the completion of shop and customer orders defined at the upper levels. In addition, actual progress on plans and decisions at higher levels is monitored. Since decision making in manufacturing is a closed loop of activities, the success of any manufacturing organization depends on the successful coordination of the various levels of activities. For example, in the strategic level, planning is needed of the production schedule to satisfy quantities which are demanded by the market. In parallel, inventory has to be controlled such that sufficient components, materials, tools are available for the planned production schedule, and such that no excessive quantities are manufactured which necessitates lengthy, costly storage. On the other hand, in the tactical level the planned production schedule and the inventory have to be coordinated with machine capacity, maintenance plans, and with labor availability for the given period. Physical storage capacities should also be considered at this level. Herein lies the importance of the concept of integrated manufacturing planning and control.

Now in selecting long-range planning tools to work in an integrated planning and control environment, care must be taken to ensure that they help management to develop plans which guide, but do not unduly restrict, decision making at lower levels. This means that the tools should allow managers to test the impact of various alternatives, to leave room for lower level planners and controllers to react to new information and contingencies, and to incorporate feedback on actual conditions and performance [1]. The same approach must be adopted in planning at the intermediate levels.

Planning issues that are important at the strategic level include master production schedule planning, resource planning, forecasting, new product planning, etc. At the tactical level, important planning issues include MRP, inventory management, capacity planning, etc. At the operational level, important planning issues include shop floor control, operations scheduling, cost control, performance measurement, etc. Figure 2 views manufacturing management in terms of three planning and control levels, their associated functions, and some names currently used to identify management tools for supporting each level [1].

<table><tr><td>Planning Horizon</td><td>Functions</td><td>Tools</td></tr><tr><td>Long Range(1–10 years)</td><td>Product DesignResource ManagementMaster Schedule DevelopmentDelivery Date SettingForecastingNew Product PlanningLong Lead Time OrderingManufacturing EngineeringInformation Management</td><td>CADMaster Production Schedule PlanningResource PlanningForecasting</td></tr><tr><td>Intermediate Range(1–24 months)</td><td>Due Date Planning and ControlPurchasingRequirements PlanningInventory Management</td><td>MRPInventory ManagementCapacity Planning</td></tr><tr><td>Short Range(1–15 Days)</td><td>Shop Order ReleaseDispatching Work to WorkstationReceivingTools and Stores ControlCost ControlPerformance MeasurementCapacity Control</td><td>Shop Floor ControlOperations SchedulingDispatching/UnloadingCost ControlStores Control</td></tr></table>

Fig. 2. Management Levels and Tools.

## 3.3. A Framework for Manufacturing Control

Given the nature of the manufacturing environment and the multilevel planning hierarchy, we now attempt to provide a framework for the development of a decision support system for manufacturing control. Before we do so, however, we need to point out certain features that are critical to the control aspects of a DSS. First, the DSS may have to support several decision makers at various levels of an organization – the decision makers may be organized in a hierarchical and/or a distributed structure. Hence it might be important to consider the degree to which manufacturing control may be decentralized and dispersed. Second, the objectives and the utility functions of various decision makers may be different. But one and only one decision has to be implemented, and immediately coordinated throughout the system. This is consistent with the view that characterizes a manufacturing system as a cooperative network of interrelated tasks. Attempts to address some of these issues have been made in [7,8], and [9]. There the general approach taken is to tackle the problem of decentralized control using the assumption that no decision maker has a complete model of the system available to it. Rather, each decision maker has the knowledge of the operation of his subsystem only. Now the assessment of the impact of his decisions on the rest of the system and of external decisions on his subsystem must be gained through communication. Thus the control activities are partitioned among the decision makers, and the coordination of planning activities is highly dependent on available communication resources. The emphasis, therefore, is on developing mechanisms, based on the underlying interactions between subsystems, to coordinate the making of decisions which are best in some system-wide sense.

The issue of decision support for manufacturing control has been addressed in the literature $[5,27]$ . These attempts were focused primarily on the manufacturing control at the operational level.

Even at this level, the decisions that have to be made could be very complex in a CIM system and often they could be unstructured as in the case of machine breakdowns and design changes. As we go from the operational level to the tactical level and from the tactical level to the strategic level, the decisions get even more complex and grow even more unstructured. Traditionally, human experts were (and by and large they still are) needed to make decisions in such a complex environment. In order to provide computer-aided decision support in such unstructured problem domains, artificial intelligence techniques need to be introduced to replicate human expertise. Attempts to develop expert systems in manufacturing have had limited success so far. In the remainder of this subsection, we shall deal with the issue of manufacturing control at the operational level.

A decision support system for manufacturing control at the operational level has three primary functions: (a) data management; (b) model management; and (c) interfacing to users and peripheral controllers [5]. The objectives of these functions is to facilitate the organization and integration of data as well as decision models and to provide decision makers with convenient access to information, both that retrieved from data files and that calculated by decision models.

The data management function is to organize and manage data that are used for decision making at the operational level. The primary responsibility here is to develop an adequate model for the representation, storage and retrieval of data used by the DSS. Nof et al. [5] point out that there are two kinds of data that are dealt with by the decision maker:

(1) We have reference data specifying the static manufacturing system elements and relationships such as the machines, process controllers, material handling and storage devices, and the linkages between them;

(2) We have operational data representing dynamic values and relationships among time dependent variables such as workpiece properties, machine conditions, and system goals.

Such data can be systematically represented in a data using one of the commonly used data models - the relational model, the hierarchical model or the network model.

The model management function is to organize and implement the decision models. A decision model is defined by its inputs and outputs and the relationship between them. A model management system is a software system that facilitates user access to models. The task of model management involves the representation, storage, retrieval and execution of algorithms at decision points in the system. Model management systems can also be accommodated in the database as discussed earlier. Blanning has pointed out [10] that a model bank can be viewed as a set of relations in a relational view of models. The advantage of such an approach is that a relational view of models may be combines with a relational view of data to yield a unified framework for information management in DSSs, in which information may be retrieved from a file or calculated by a model solution procedure. A relational framework is not the only one in which a synthesis of data and model management may be achieved. The CODASYL framework has also been extended to support model description and manipulation [12,13]. Now the model management function serves two purposes. Some decision models are used for structured decisions which are assigned completely to the DSS for automatic execution. There are other models which perform data reduction, computation, and evaluation of performance measures that are useful as aids to human decision making for non-automatic, unstructured decisions.

A third important function is to provide interfaces to peripheral process controllers and to other users of the DSS. The controller interface provides a communication capability between other functional components of the DSS and various peripheral machines and controllers comprising a manufacturing facility. Access methods provide standardized commands for sending data to, and receiving data from the many types of peripherals. A user interface is also an important component of the DSS. Through the interface the user can interact with the DSS to obtain information necessary for decision making, and to communicate decisions back to the control system for execution. Through the interface, the user defines the specification of the manufacturing system, including data and decision models, defines goals and system slates. The important issue here is the development of a natural language interface. This is because from a user's perspective, a natural language such as English would be ideal. This would allow the users maximal flexibility of expression.

In order to gain a clear understanding of the control mechanisms in a complex manufacturing environment, it might be appropriate to develop models of the manufacturing environment. Such models should not only be able to represent the static manufacturing system elements and relationships such as machines, material handling and storage devices and the linkages between them but should also be able to represent dynamic elements and their associated relationships such as system goals, machine status, etc. The structure of such representations is useful for the analytical evaluation of control issues. Attempts in this direction have already been made $[5,14]$ , as will be discussed below.

In [5], the manufacturing environment has been modeled by using E-nets or evaluation nets, which are modified Petri nets. A Petri net is an abstract, formal model of information flow [15]. The Petri net graph models the static properties of a system. In addition, a Petri net has dynamic properties that result from its execution. Petri nets have been extensively used to study the control flow of computer systems. Now the E-net model can be modeled by three components comprising the system data base [5]:

(i) Reference data;

(ii) Operational data; and

(iii) Decision logic.

The reference data describes the static manufacturing system elements and relationships. The operational data describes the dynamic properties that result from the operational of the manufacturing system. The reference data defines the operands, nodes, operators and paths of a traditional Petri net model whereas the operational data denotes the status of conditions in the E-net model by specifying the distribution of operands to nodes over time. The decision logic component, on the other hand, represents decision making algorithms in the system which are required for deterministic control. Now a DSS for manufacturing control will combine the three above-mentioned components to implement automatic control and decision support. An advantage of the E-net model is that it provides the DSS with the capability to capture control and temporal interdependencies in a distributed, hierarchical system as well as with the ability to evaluate performance measures and issues of concurrency and conflict in the manufacturing operation. Besides, it has been noted [6] that the E-net model can be utilized for graphic, visual aids for human interaction.

In [14], a second approach to modeling the manufacturing environment has been adopted by applying predicate logic and theorem proving techniques using the resolution principle. The rationale for such an approach is that although computers are capable of processing vast amounts of information, many of the necessary decisions have to await human attention. Use of artificial intelligence techniques can aid in handling large streams of data as well as performing logic manipulation for conflict resolution, sequencing and resource allocation. Now predicate logic is a natural language for stating facts and making inferences in such an environment. The static manufacturing system elements as well as simple relationships among these elements can be modeled by predicates while complex relationships among elements can be defined by axioms. However, the manufacturing environment is not static as a multitude of changes continually occur over time. Even an element such as a machine, whose existence is static in the system, undergoes state changes as it goes from an idle state to an allocated state while machining a part, then back to idle again. To reflect the changing states in manufacturing, Bullers et al. [14] have introduced time into all predicates for which assertions of fact are dynamic. The advantage of this approach is the systematic representation of planning and control knowledge details by predicates, and the use of reasoning algorithms to extract pertinent decision information.

## 4. Architectural Aspects of DSS in Manufacturing

## 4.1. Introduction

In Section 3, we have addressed some of the major issues pertaining to decision making in the manufacturing environment. We have looked at the nature of the manufacturing environment in which decisions must be made. In particular, we have attempted to take an integrated view of the multilevel planning hierarchy and have considered some of the techniques that could be helpful in modeling the manufacturing environment. Now one of the major hindrances in the development of a computer-integrated manufacturing system is the lack of a theoretically sound systems architecture. Such a system should reduce the overall system complexity by focusing on one subsystem at a time, defining component modules and their interfaces. From an implementation point of view, such an architecture would allow users to build systems in increments. From a conceptual point of view, such an architecture would provide a framework for integrated manufacturing control.

In Section 2, we had pointed out that a DSS can be described by its three principal components – the LS, the PPS and the KS – and the interactions between them. It was maintained that the LS and the KS are primarily representation systems whereas the PPS is the analytic component of the DSS. With that point of view in mind, we shall propose an architectural framework for DSS in manufacturing having four major components: manufacturing systems control corresponding to the PPS, data administration corresponding to the KS, user interfaces corresponding to the LS and finally, communication systems corresponding to the interaction mechanisms among the other three components. Each of these components is described in greater detail in one of the four subsections that follow.

## 4.2. Manufacturing Systems Control

The architecture of the control system is one of the most important part of the manufacturing system architecture. In this paper, we take a hierarchical view of the manufacturing control system – the architecture thus reflects the hierarchy not only at the planning level but also at the manufacturing level. Hence the architecture, as we shall presently discuss, of the control system is a hierarchical structure in which overall control is exercised through the cooperation of decentralized system elements. Each controller takes commands from only one higher level system, but it may direct several others at the next lower level. The planning horizon (i.e., the amount of time any control system sets aside to handle its tasks) can be used as the basis for selecting the processing requirements at each level. Now long-range tasks enter the system at the highest level and are broken down into subtasks, to be executed as procedures at that level or put out as commands to the next lower level. Control systems at each level will be free to make decisions within boundaries established by higher levels.

The specific structure of the proposed hierarchy is composed of five major levels: facility, shop, cell, workstation and processor (Fig. 3). Each level has multiple controls that are further broken down into sublevels or modules. Each module at every level has its own set of controllers for its internal control processes. All modules communicate through the communication network. Besides, each module has access to its own database. Database and communication issues will be discussed in later subsections. It should be noted that each module is essentially a functional module performing one logical task, e.g., MRP at the tactical planning level, or production scheduling at the operational planning level. In practice, one such task may be performed on more than one processor or one processor might perform a multiplicity of tasks from the same planning horizon. We shall now discuss the control issues at each level of control.

Facility: This highest level of control assumes responsibility for tasks that are performed at the strategic or the long-range planning level. Each such task can be assigned to one of the k functional modules. The functional modules act in a cooperative manner by interacting with one another through the communication network. Among the important tasks that are executed at this level are product design, manufacturing engineering, information management and production management. If the item is to be manufactured to specifications, the design will have been prepared by the customer. On the other hand, if the product is proprietary, the manufacturer is responsible for its development and design. The manufacturing engineering function consists typically of four responsibilities:

(i) Advising the product 'design department on the producibility of the part;

(ii) Process planning, i.e., the determination of the sequence of individual manufacturing operations needed to produce a part;

(iii) Specification of tools, jigs, and fixtures used to produce a part; and

![](/api/attachments/FDPGEYTS/fulltext/images/ea64613cfdb2789467fbfe5dc5dcff80492371909e428d91eaa0f6c5eec2651c.jpg)  
Fig. 3. Schematic Diagram for Manufacturing Systems Control.

(iv) Troubleshooting when problems arise in production.

Information management provides interfaces and supports the handling of customer orders, administrative functions, etc. Production management tracks major projects, generates long-range schedules, and identifies production resource requirements and excess production capacity. The production planning data generated at this level is used to direct the shop control system at the next lower level.

Shop: This level of control is responsible for the control of tasks at the tactical planning level. Among its primary responsibilities are requirements planning, inventory management, task management and resource management. The task of requirements planning is to determine, based on the master schedule generated at the strategic planning level, the individual components and subassemblies that make up each product and order them so that they are available when needed.

Inventory management determines the optimal level of inventory at any given time. Task management schedules job orders, equipment maintenance, and shop support services. Besides, it creates and controls virtual manufacturing cells by the dynamic reconfiguration of lower level functional modules to schedule and execute various parts, and eventually removes the virtual cells from the control structure when their assigned tasks are completed. Resource management allocates workstations, storage buffers, tools and materials to cell level control systems and to particular production jobs. In addition, the shop level control classifies parts and defines parts families, using part processing requirements, geometric shapes, tools used, production costs, and the composition of materials.

Cell: This level of control is responsible for the tasks at the operational planning level. Modules within the cell control the performance of system tasks, analyze the availability of resources, report on job progress, schedule activity, requisition resources, and keep track of tasks being done at workstations. Now the cells themselves are dynamically configured production-control structures that permit the time sharing of workstation processing systems. This dynamic reconfiguration of the same set of workstations to form different cells enhances the flexibility of the manufacturing cells. These dynamically configured cells are different from traditional manufacturing cells, which are defined by fixed groupings of equipment or machinery on the shop floor.

Workstation: This level of control directs and coordinates the groupings of processors on the shop floor. Each workstation is designed to be capable of performing a small set of primitive operations. The controller at this level sequences the processors through various stages including job set-up, actual machiing, inspection of the machined part, etc. A typical workstation in an automated manufacturing environment might consist of a robot, one or more machine tools, a materials storage buffer, and a control computer. An important design issue here is the development of an appropriate interface between a cell and a workstation, whereby a variable number of workstations can be assigned to a cell. A simple way to implement this interface is to use a multiplexor arrangement. A multiplexor is a device intended to route data from one of several sources to a common destination. The source is determined by applying appropriate control (select) signals to the multiplexor. The cell-workstation interface is shown in Fig. 4(a) while the multiplexor arrangement for a given cell is shown in Fig. 4(b). Each workstation is connected to one and only one cell, depending on its MUX CONTROL. The MUX CONTROL is set by the shop level control for a particular assignment of workstations to cells – this allocation of workstations to cells is part of the resource management function performed by the shop level control. This multiplexor arrangement allows the assignment of a variable number of workstations to a cell depending on the nature of the processing requirements that a particular job or a set of jobs requires.

![](/api/attachments/FDPGEYTS/fulltext/images/c8b0b7453c17897c1a5492adac992146032584b3183f051918c3f2586c84fbef.jpg)  
Fig. 4. Cell-Workstation Interface.

Processor: This level of control is tied to processors on the shop floor. Now a processor is a generic term used to characterize individual robots, NC machines, automated material handling devices, etc. These processors perform the basic machine level functions of materials storage, transportation, handling, materials processing, inspection, etc.

The issue of incorporating artificial intelligence into manufacturing control as well as other architectural issues such as fault-tolerant systems will be discussed in Section 4.6.

In fine, we have attempted to describe a hierarchical control structure that reflects the multilevel planning hierarchy as well as a multilevel manufacturing hierarchy. The essence of this approach is to take an integrated view – a total system view – of the manufacturing system; the development of a manufacturing systems architecture provides the framework for adopting such a view.

## 4.3. Data Administration

For control systems to share information, there must be a standard interface to data bases. In this section we shall briefly discuss the nature and the importance of data bases in a computerized manufacturing environment. Specific architectural issues about the management of data will be discussed at length in Section 5.

Now each functional module in Fig. 3 involves one or more control processes. In the architecture we propose, each control process is, in turn, composed of a number of manufacturing processes that operate through a common data administration system. As for the distribution of functions and data in a data administration system, the requirements depend on the level of control. In general, the volume of data is larger and the acceptable response times larger at higher level of control. Besides, the nature of control processes at the highest levels also require to use aggregated information from data bases at lower levels, decision models to make long-range decisions, etc. Some control levels need very high rates of data access and modification, implying that the data base should be in the computer memory rather than stored peripherally. Hence, the data administration environment for the system as a whole consists of extremely heterogeneous multiple data base management systems.

Computerized manufacturing is even more cost effective if the computerization is taken one step further to integrate the design and manufacturing processes through a well-structured data base. After all, the entire manufacturing industry is heavily dependent on data communication, starting with the preliminary design of a product and continuing through production design, manufacturing and sales [16]. Hence the concept of a manufacturing data base should encompass activities from preliminary design to customer support. Each activity can draw from the data base and also contribute to and modify it.

The use of computers in the various phase of the manufacturing process has two distinct implications. The first is the integration of the information content of the various phases like product design, production scheduling, etc. The second is the derivation from this integrated data base (IDB) the data required to automate these activities. Karma and Chu have pointed out [17] that this has broad implications for the very nature of the data that is stored. They have pointed out, for example, that in the integration of CAD and CAM, 2-D line drawing must be replaced by a suitable computer-based information form capable of supporting the various processes in the manufacturing environment. This new information must be complete, consistent and accurate, and it must be able to support automatic application programs. This key element is usually referred to as geometric data base management system. With such a system, users could automatically check the manufactured parts and generate numerical control tool paths, process plans, and optimum part dimensions. Information such as these need to be stored in the data base and forms the corporate data base (Fig. 5). Karma and Chu have pointed out [17] the type of information that is stored in the corporate data base containing corporate data seems to be the key to achieving total integration.

<table><tr><td>Mechanical Computer - Aided Engineering (CAD)</td><td>Manufacturing Computer - Aided Engineering (CAM)</td></tr><tr><td>Performance Specifications</td><td>Parts List</td></tr><tr><td>Conceptual Design</td><td>Material List</td></tr><tr><td>Assembly Drawings</td><td>Numerical Control Data</td></tr><tr><td>Detail Drawing</td><td>Tools Data</td></tr><tr><td>Documentation Aids</td><td>Robotics</td></tr><tr><td>Configuration Control</td><td>Computerized Testing</td></tr><tr><td>Mechanical Design</td><td>Quality Control and Reliability</td></tr><tr><td>Mass Properties</td><td>Configuration Control</td></tr><tr><td>Modeling: Mechanism, Structural Thermal</td><td></td></tr><tr><td>Mechanism Analysis</td><td></td></tr><tr><td>Thermal Analysis</td><td></td></tr><tr><td>Structural Analysis</td><td></td></tr><tr><td>Antenna Analysis</td><td>Electrical Computer - Aided Engineering (CAD/CAM)</td></tr><tr><td>Mechanical Test Data</td><td>Performance Specifications</td></tr><tr><td></td><td>Logic Simulation/Analysis</td></tr><tr><td></td><td>Logic Design/Layout</td></tr><tr><td>Corporate Data</td><td>Printed Circuit Board Layout</td></tr><tr><td>Sales and Marketing Data</td><td>Technology Definition</td></tr><tr><td>Customer Support Data</td><td>Test Generation</td></tr><tr><td>Finance Data</td><td>Manufacturing Data Generation</td></tr></table>

Fig. 5. A Corporate Data Base for the Spacecraft Industry [20].

A system architecture for an integrated data base is shown in Fig. 6. The integrated data base structure includes data corresponding to 3-D solid geometric forms as well as design, manufacturing, marketing and other information. It also consists of data base management systems, a user interface and a communications processing network. The communications processing network is required to facilitate rapid transfer of data between the IDB and any discipline in the plant. Integrated data bases having this general structure are being used by the Boeing Commercial Airplane Co. [16] and the spacecraft industry [17].

![](/api/attachments/FDPGEYTS/fulltext/images/112a983dc88ee5a95625f083e77b5717e3379081fd3578bd4474403aaa429872.jpg)  
Fig. 6. A System Architecture for an Integrated Data Base.

## 4.4. Communications Systems

In order that control processes share information effectively, it is imperative that there be an effective communications network that allows rapid transfer of data between the data and any discipline in the plant. There are a wide variety of networks available in the market today. On a local communication level, a high bandwidth local network such as Ethernet, Net/One, Wangnet, Hyperchannel, etc. may be used. A local network could be baseband, broadband or a combination of the two. On a remote communication level, a long-haul network such as Telenet, Cybernet, Tynnet, etc. may be used. The appropriate choice depends on the nature of the manufacturing environment, the geographical location of its various subsystems, etc. However, four basic ideas should motivate the communications architecture system [18]:

(i) The distribution of logical control processes and their related data bases over a network of different computer systems;

(ii) Communication mechanisms that satisfy the performance requirements of the control systems;

(iii) The transparency of the actual mechanisms used for communications between the control processors; and

(iv) A common communications and computer-process management language that simplifies distributed system development.

Now if control levels are distributed over multiple computer controllers, one might consider having several communication systems in a plant, each dedicated to different levels of production. However, it might be more appropriate, particularly in view of the nature of integrated manufacturing, to have a common network that permits communication between processes on separate subsystems and for access to nonresident data bases. The most flexible network architecture is a broadcast network, in which every system is physically connected to a single transmission medium but is logically connected only to systems with which interchange is required. Broadcast networks are robust and they can function with any number of systems, and their cost is incremental.

Each functional module shown in Fig. 3 constitutes a computer system, which may have multiple processors. A communications node can be associated with a single computer system. A node supports a group of logically related processes such as manufacturing control, data administration, program control, communications control, etc. (Fig. 7). Communications between processes residing on the same node can be carried out through the common local data paths whereas communication between processes residing on different nodes should take place through the broadcast network.

## 4.5. User Interface

To maintain a distributed computing architecture for an automated manufacturing environment, system interfaces are required for operators, programmers, maintenance technicians, and data-entry and management personnel. Ideally, a user interface should be friendly and efficient. Simple graphics and English-like interfaces are needed before inexperienced users can operate automated manufacturing systems.

User interface can be divided into four components [17]. One of them, the user's model, underlines the other three. The user's model is the conceptual model formed by the user of the information he manipulates and the processes he applies to this information. The second component is the command language, which provides a set of commands to manipulate the system. The third component of the interface is feedback, and this assists the user in operating the computer program. The fourth component, information display, shows him the state of the information he is manipulating.

Karma and Chu have given [17] a software architecture which incorporates the above-mentioned components of the interface (Fig. 8).

![](/api/attachments/FDPGEYTS/fulltext/images/8cfd5d7b89c40f3f39cedd81ca711ad3248cb215e4b7a87e8784dabce5b7d780.jpg)  
Fig. 7. Communications System at a Typical Function Module.

![](/api/attachments/FDPGEYTS/fulltext/images/1e8f41406d70d032c4645a4a300e58b0a39a40df63247f7241a30ec2fa321d43.jpg)

\- Def. of Screen Layouts

\- Syntax Analysis

\- Help

\- Def. of Commands

\- Device Control

• Display of User Input

• Def. of Command Menus

• View-part Control

\- Display of Messages

• Def. of User Dialogues

\- Menu Handling

• Display of 'Error Messages, etc.

• Def. of Error Messages

\- Help Functions

\- Def. of Utility Commands and Commands for Initiating IDB and for Designing Data Base Contents, etc.

\- Logging commands, etc.

Fig. 8. Software Architecture for User Interface [20].

## 4.6. Other Architectural Issues

In conventional manufacturing systems, humans are needed to provide the expertise and intuition to adapt the system to new and unforeseen situations. Automated manufacturing systems must do its own adapting by acquiring the ability to plan and to handle unpredictable events. In order to provide computer-aided decision support in such unstructured problem domains, artificial intelligence techniques can be used to provide better planning and control towards a higher productivity of automated manufacturing. Such techniques are not only capable of handling large streams of data but also performing logic manipulation for conflict resolution, sequencing and resource allocation, etc.

Broadly speaking, three different classes of intelligent functions are performed by automated manufacturing systems. In order of increasing complexity they are reaction, learning and problem solving. Reaction is the most primitive form of intelligent function in which the manufacturing system does some form of pattern recognition and provides some response to it. Learning is another intelligent function that requires that the manufacturing system recognize significant experiences, data or generated plans and incorporate this new information into the control structure. Learning incorporates a capability in the manufacturing system to modify its knowledge base. Problem solving is the most complex form of intelligent function performed by the manufacturing system. Problem solving activities in manufacturing include modeling the problem domain as a set of states and then describing the process of change as a transition from one state to another, generating plans for such transitions that take from an initial state to a goal state, monitoring the execution of such plans, generating optimal resource allocation plans, etc. Generation of such plans is a nontrivial task because most problems of practical interest in manufacturing would be NP-complete. Hence problem solving techniques should attempt to develop heuristics which generate ‘reasonably good’ but not necessarily optimal solutions.

It should be noted that an automated manufacturing system would perform efficiently only if its components continue to function properly without failure. But components will breakdown intermittently and hence it is necessary to design faulttolerant manufacturing systems that would keep functioning even after a fault has occurred. For a system to be truly fault-tolerant, it should be capable of continued operation after one or more faults anywhere within the system, with minimum degradation. The design of fault tolerant systems has great implications for computerized manufacturing – it will allow the design of non-stop manufacturing systems; i.e., systems with continuous availability despite the occurrences of failures.

The essential ingredient of all fault-tolerance is redundancy, both in hardware and in software. The amount of redundancy, and where to employ the redundancy, is largely determined by the number of the types of failures to which the system is designed to be immune. In general, failures can be of three types [19]:

(i) Permanent physical failures such as shortened connectors or burnt out chips;

(ii) Transient component failures due primarily to temporary environmental disturbances; and

(iii) Operational failures such as data entry errors, the use of erroneous software, etc.

One obvious way of building fault tolerant systems would be to employ duplicate components, either as standby spare parts, or in a majority voting type of configuration, whereby the duplicate components would simultaneously replicate each other's actions. The major disadvantage of this approach is one of cost – at least three or four times the number of components needed to build an equivalent non-fault-tolerant system would be needed to build one such system, but with no added output. Attempts to alleviate the problem of wasted duplicate resources have been made in the domain of transaction processing computer systems [19–21].

## 5. Data Administration System in Manufacturing

It is now widely accepted that information is a vital corporate asset that should be invested in, controlled, and used like other resources. Automated manufacturing systems can become more cost effective by the integration of the design and manufacturing processes through a well-structured data base. What is new in all this is the argument that data should be administered on a firm-wide basis (data administration) as opposed to a geometrical and fabrication data base administered separately (data base administration). The data administration function has broader responsibilities than does a traditional data base administration system [16]. The data administration function generally is responsible for the firm-wide inventory and control of data. Data inventory management requires pertinent facts and relationships about the various data objects, processes, users, processes, users, and equipment in the data processing environment. Data administration's internal control procedures restrict access to data, manage development of new types of data, and protect data from erroneous update and system failure. it develops data organization strategies in line with corporate business strategies, interacts with user and system management to develop data-resource requirements, formulates policies for data-resource development and use, and develops an overall plan for data acquisition, storage and use throughout the organization. It was noted earlier that each control module has access to its own data administration system (DAS). Besides, because of the varying requirements of functions and data, the various DAS's are not exactly identical. Hence we have a heterogeneous and distributed data administration environment.

A schematic diagram of a typical DAS is given in Fig. 9. The major functional units in a DAS are:

(i) Common data management language translator;

(ii) Data base management system (DBMS);

(iii) Integrated directory/dictionary system (D/D); and

(iv) Storage media.

Each functional control module needs a translator. The translator must be accessible from the local control programs and from other control programs in the network. The translator uses the local data directory to determine whether a request can be satisfied from resident data bases. If it can, the query is translated and transmitted to the local DBMS. If the data are not locally resident, the query is passed via the communications system to corresponding DAS's at other functional modules.

The DBMS is a critical element of any DAS. DBMS issues are well-known and are widely discussed in the literature [22,23].

An important element of the DAS is the integrated dictionary/directory system (D/D) [24]. A D/D system is an automated information system composed of:

(i) A data base that contains data describing the data, processes, users and processors of an organization, i.e., metadata;

(ii) Retrieval and analysis capabilities that assist a wide range of user groups in application development;

(iii) Management tools that help ensure the security, validity, recoverability, integrity, and shared accessibility of the D/D; and

(iv) Functional interfaces that permit other software modules to access the D/D and that convert metadata into the format required by the D/D system.

Now the D/D system provides two primary functions: first, it facilitates understanding and communication about the relationship between system applications and system data usage; second, it assists in achieving data independence by permitting system applications to access data without knowledge of the location or storage characteristics of the data in the system.

Since the architecture for the manufacturing system requires a distributed DAS, the D/D system required is a distributed D/D system. Such a D/D system should contain metadata describing the data base distribution, the characteristics of the nodes, and some aspects of the data communications network [24]. The D/D in the distributed data base environment itself becomes a distributed data base. Each functional module needs access to its own D/D system. Contents of the global D/D system may reside at various locations. Replications of parts of the D/D may or may not be desirable, depending upon characteristics of the system.

In fine, we need to point out certain control modules, particularly those at the higher levels of control, need to store not only operational and geometric data but also decision models. Hence model management should also be an integral part of the data administration system. The incorporation of model management into the architecture of a data administration system should be an interesting topic for future research.

![](/api/attachments/FDPGEYTS/fulltext/images/02ff65520d677510b545a729dc73fe3071490827e843b08122b47eeaeb9c0d30.jpg)  
To other data administration systems or other functional modules  
Fig. 9. Schematic Diagram for a Data Administration System.

## 6. Conclusion

So far we have dealt with some of the DSS issues in computer integrated manufacturing. We have adopted an information processing approach to study the manufacturing environment. This approach assumes that an information transition associated with changing an entity's measured attributes is accompanied by a material transition changing the physical attributes of the machined workpiece. In other words, the logical transformation of operand data by one or more processors into a finished information product is accompanied by a concurrent physical transformation of the workpiece into a financial product.

The same approach could also be extended to the study of organizations as a whole. After all, a manufacturing system is but an inseparable part of manufacturing firms. The firm exists principally to develop, manufacture and market goods for a profit. This indicates that there are three primary functions of such firms: marketing and sales, product engineering and manufacturing. The automation of such firms requires the understanding of four basic concepts: transfer of data, transform of data, transfer of material and transform of material. Transforms of both data and material add value. Hence the ideal goal might be to automate the creation and transformation of logical data and then automate completely the creation of the physical counterparts of the logical data. By doing so, the firm will have automated both the blue-collar and the white-collar functions. More importantly, this provides a synergistic integration of each of the automated functions into a cohesive computer-integrated organization.

## References

[1] Lodato, M., Computerized Tools for Resource Planning and Materials Management, Manufacturing Management Systems, Gruenberger, F. (ed.), Hayden Book Co. Inc., Rochelle Park NJ (1974).

[2] Bonczek, R.H., C.W. Holsapple, and A.B. Whinston, Foundations of Decision Support Systems, Academic Press, New York (1981).

[3] Bonczek, R.H., W. Holsapple, and A.B. Whinston, Specification of Modeling Knowledge in Decision Support Systems, Working Paper, Krannert School of Management, Purdue University (Jan. 1982).

[4] Harrington, J., Computer Integrated Manufacturing, Computer Integrated Manufacturing, Industrial Press, Inc., New York (1973).

[5] Nof, S.Y., A.B. Whinston, and W.I. Bullers, Control and Decision Support in Automatic Manufacturing Systems, AIIE Transactions, 12 (1980) no. 2.

[6] Nof, Y., Theory and Practice in Decision Support for Manufacturing Control, in: Data Base Management: Theory and Applications, Holsapple, C.W. and A.B. Whinston, Reidel, Dordrecht (1983).

[7] Smith, R.G. and R. Davis, Frameworks for Cooperation in Distributed Problem Solving, IEEE Transactions on Systems, Man and Cybernetics, SMC-11 (Jan. 1981) pp. 61–69.

[8] Tenney, R.R. and R. Sandell, Structures for Distributed Decision Making, IEEE Transactions on Systems, Man and Cybernetics, SMC-11 (Aug. 1981) pp. 517–527.

[9] Tenney, R.R. and N.R. Sandell, 'Strategies for Distributed Decision Making, IEEE Transactions on Systems, Man and Cybernetics, SMC-11 (Aug. 1981) pp. 527–538.

[10] Blanning, R.W., Issues in the Design of Relational Model Management Systems, National Computer Conference, 1981, AFIPS Conference Proceedings, AFIPS Press, Vol. 52 (1983) pp. 395–401.

[11] Blanning, R.W., A Relational Framework for Model Management in Decision Support Systems, DSS-82 Transactions (June 1982) pp. 16–28.

[12] Konsynski, B.B., On the Structure of a Generalized Model Management System Proceedings of the Fourteenth Hawaii

International Conference on System Sciences 1 (Jan. 1981) pp. 630–638.

[13] Stohr, E.A., and M. Tanniru, A Database for Operations Research Models, Policy Analysis and Information Systems, 4 (1980) pp. 105–121.

[14] W.I. Bullers, Y. Nof, and A.B. Whinston, Artificial Intelligence in Manufacturing Planning and Control, AIIE Transactions, 12 (1980) pp. 351–363.

[15] Peterson, J.L., Petri Nets, Computing Surveys, 9 (Sept. 1977) pp. 223–250.

[16] Beeby, W.D., The Heart of Integration: A Sound Data Base, IEEE Spectrum, 20 (May 1983) pp. 44–48.

[17] Karma, K.N. and D.F. Chu, Computer-Aided Engineering in Communications Satellite Design, IEEE Computer, 16 (April 1983) pp. 69–82.

[18] McLean, C., M. Mitchell, and E. Barkmeyer, A Computer Architecture for Small Batch Manufacturing, IEEE Spectrum, 20 (May 1983) pp. 59–64.

[19] Gostamian, R., The Auragen System 4000, Data Base Engineering, 6 (June 1983) pp. 3–8.

[20] Bartlett, J.N., A Nonstop Kernel, Communications of the ACN, Communications of the ACM (Dec. 1981) pp. 22–29.

[21] Westl, J.C. M. Isman, and S.G. Hamaford, Transaction Processing in the PERPOS Operating System, Data Base Engineering 6 (June 1983) pp. 9–19.

[22] Date, C.J., An Introduction to Data Base Systems (3rd edn) Addison-Wesley, Reading MA (1981).

[23] Ullman, J.D., Principles of Data Base Systems, Computer Science Press, New York (1980).

[24] Allen, F.W., M.E.S. Loomis, and M.V. Manmino, The Integrated Dictionary/Directory System, Computing Surveys, 14 (June 1982) pp. 245–286.

[25] Kowalski, R., Logic for Problem Solving, Elsevier/North-Holland, Amsterdam, New York (1979).

[26] O'Donnell, M.J., Lecture Notes in Computer Science, Vol. 58: Computing in Systems Described by Equations, Springer-Verlag, Berlin, New York (1977).

[27] Nof, S.Y. and Gwrecki, R., MDSS: Manufacturing Decision Support System, Proceedings of the AIIE Spring Conference, Atlanta GA (May 1980).
