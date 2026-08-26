---
otero_id: 24569
otero_key: "K6SDE7ER"
title: "GOST: An Active Modeling System for Costing and Planning NASA Space Programs"
authors: "David G. Castillo; Daniel R. Dolk; Donald J. Kridel"
year: "1991"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1991.11517934"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# GOST: An Active Modeling System for Costing and Planning NASA Space Programs

David G. Castillo, Daniel R. Dolk & Donald J. Kridel

To cite this article: David G. Castillo, Daniel R. Dolk & Donald J. Kridel (1991) GOST: An Active Modeling System for Costing and Planning NASA Space Programs, Journal of Management Information Systems, 8:3, 151-169, DOI: 10.1080/07421222.1991.11517934

To link to this article: http://dx.doi.org/10.1080/07421222.1991.11517934

![](/api/attachments/K6SDE7ER/fulltext/images/2c943fcaadbc613d0cb9b721d23154b71a726bd2a8535c6f161b69cf3ea963c7.jpg)

Published online: 18 Dec 2015.

![](/api/attachments/K6SDE7ER/fulltext/images/3b2e5a7d634b0ca5bfd2eb2dffa40133cb966af9536d5d90c63de5dabf5101e7.jpg)

Submit your article to this journal ↗

![](/api/attachments/K6SDE7ER/fulltext/images/60919e6dadf2844da3591456fd5f67fb0969c2927ce23ad06611558ce6e0d634.jpg)

View related articles ↗

# GOST: An Active Modeling System for Costing and Planning NASA Space Programs

DAVID G. CASTILLO, DANIEL R. DOLK, AND DONALD J. KRIDEL

DAVID G. CASTILLO is a Visiting Scientist at the McDonnell Douglas Research Laboratories in St. Louis. Mr. Castillo is involved with NASA-sponsored research activities in software engineering, object-oriented design, artificial intelligence, knowledge representation, object-oriented databases, decision support systems, and computer simulation. He received his Ph.D. in systems engineering at the University of Central Florida in 1991. Mr. Castillo is a member of AAAI, IEEE, and SCS.

DANIEL R. DOLK is Associate Professor of Information Systems in the Department of Administrative Sciences at the Naval Postgraduate School, Monterey, California. He received his Ph.D. in management information systems from the University of Arizona, Tucson, in 1982. His research contributions have been primarily in the area of model management and decision support systems. His current interests include symbiotic information systems, integrated modeling environments, and the application of conceptual modeling to discrete event simulation modeling. He is a member of the Association of Computing Machinery, the IEEE Computer Society, and the Institute of Management Science.

DONALD J. KRIDEL is Director of Strategic Marketing at Southwestern Bell Corporation. He received his Ph.D. in economics from the University of Arizona in 1987. His research interests are applied econometrics and telecommunications demand analyses.

ABSTRACT: This paper describes an active, or symbiotic, decision support system developed for the National Aeronautics and Space Administration called the Generic Operations Simulation Technique (GOST). GOST combines parametric modeling techniques (regression) with discrete-event simulation to cost and plan future space programs. GOST differs from previous process modeling approaches by providing an “artificially intelligent modeling expert” and an “artificially intelligent domain expert” for assisting the user in developing and analyzing process models. An object oriented knowledge representation system provides the foundation for the GOST environment. A taxonomy of Computer Directed Process Managers, implemented within the representation system, controls the appropriate processes responsible for delivering active modeling support.

An earlier version of this paper was originally published in the Proceedings of the Twenty-Fourth Hawaii International Conference on System Sciences (IEEE Computer Society Press, 1991).

KEY WORDS AND PHRASES: active DSS, modeling environment, econometrics, hierarchical knowledge system

## 1. Introduction

A SYMBIOTIC (OR ACTIVE) DECISION SUPPORT SYSTEM (DSS) is a system wherein the user and computer work as partners in the problem solving process $[7]$ . Application of this concept to econometric modeling systems has been discussed in the form of a Process Control Language (PCL) for the Progressive Econometric Modeling System (PERM) $[4]$ . We discuss another application of active modeling in the Generic Operations Simulation Technique (GOST). GOST is a generic process modeling environment designed to assist NASA engineers with planning and costing future space programs. Our approach in developing GOST extends conventional process modeling approaches by providing an “artificially intelligent modeling expert” for assisting the analyst in constructing and analyzing models. We employ both domain-specific and generic modeling knowledge within the GOST knowledge base. Conceptual models containing domain expertise are utilized as modeling templates from which specific models are derived. In addition, we employ a domain-independent process modeling methodology as a vehicle for assisting the user during model development and analysis.

Section 2 reviews aspects of active, or symbiotic, decision support systems as a foundation for describing the architecture and operation of the GOST environment. Section 3 describes the GOST environment, including its architecture and representation. In section 4, we discuss the application of active modeling to the GOST environment with particular emphasis on the roles of the user and computer-directed process managers. Finally, we illustrate how the modeling methodology provides the basis for supporting active modeling.

## 2. Active Modeling Systems

AN ACTIVE DSS (ADSS) IS AN ANTICIPATORY SYSTEM that tries to prefigure what step(s) the user is likely to perform next, and to provide without explicit prompting the requisite support for carrying out those steps. For example, a marketing manager may query a database for projected sales figures for the next quarter. If those sales data are not available in the database, she may run a simple forecasting model to obtain those figures. An active DSS would anticipate this request and run the model automatically if the data were not present. Similarly, a programmer who is editing a program source file will most likely next want to compile, and then if no compilation errors occur, link and load, and execute the program. An active operating system would be able to identify this pattern and automatically invoke the compiler, linker, and executable program.

Manheim [8] defines an ADSS as a system that uses an explicit model of the human problem-working process to usefully do more than directed by the user. In the programming example above, the operating system would require a model of the particular programmer's process indicating which compiler is to be used, which other object files and libraries must be linked, and which parameters or external files are required for execution of the program. These models can be prespecified statically (e.g., as a macro in this case), or developed dynamically from some kind of pattern inference process (e.g., monitoring the user's command stream for occurrences of the same pattern of commands).

As Dolk and Kridel [3] note, ADSS differs from conventional DSS in that it is primarily learning-based and derives from the discipline of cognitive science rather than system design or organizational behavior. An ADSS can be characterized as “symbiotic” in that it tries to work in concert with the user, providing value-added operations that do not need to be specified explicitly.

## 2.1. Review of Active DSS

Three general components comprise an ADSS architecture: history processor, process managers and display interfaces. The history processor consists of two separate components: a history recorder, which journals user inputs and resultant outputs in a history record, and a history inference processor (HIP) which attempts to identify or construct a model of the user's image of the problem from the history record. Two types of process managers, user-directed (UDPM) and computer-directed (CDPM) coordinate to provide the user with active modeling support. The UDPM activates resident processes in response to commands issued by the user. Conversely, the CDPM, activates processes in response to commands issued by the history processor as it attempts to provide active support. Thus, the CDPM may invoke a predefined set of procedures and actions, once it determines the type of analysis the user is performing. Display interfaces filter the various outputs of the system and provide a protocol for the user to activate the UDPM.

The user initiates action via mouse, menus, or a command language. Based on the user input, the UDPM activates one or more processes to satisfy the action command (e.g., model development). The history recorder logs the command and resultant output in the history record. Each time an insertion into the history record is made, the HIP is invoked. The HIP scans the history record and attempts to create a model of the user's problem-working process either by pattern matching with a library of existing model templates, or inductively using a form of dynamic pattern matching.

The HIP is fundamental to the success or failure of an ADSS. Recall that the HIP requires a model of human problem-working processes. Manheim suggests a general processing model that resembles neural networks. The model consists of a hierarchical network of schemas that form concepts. Schemas are classified as template schemas that are similar to frames, procedural schemas that provide action sequences, and mixed schemas that are combinations of the two.

Constructing an ADSS poses a number of interesting challenges $[7]$ . First, the construction of a schematic network from an evolving library of schemas requires a representation system capable of dynamically modifying itself, while updating all relational connectivities. Second, the schematic network must possess the ability to form hypotheses about the user, the problem, and the problem-working process. Third, the ADSS should provide a vehicle for testing the hypotheses through the equivalent of simulation modeling. Fourth, the construction and evolution of a schema library is critical to the successful implementation of an ADSS.

## 2.2. An Active Econometric Modeling System

Dolk and Kridel [4] have extended conventional DSSs to provide active support in the area of econometric modeling. The Progressive Econometric Modeling system (PERM) is a commercially available DSS designed to provide decision support for econometric estimation, simulation, and forecasting. Although PERM itself is not active, a prototype (Active-PERM) based on this system has been developed that provides active modeling support within a limited domain of econometric estimation.

Active-PERM offers symbiotic support to the user in determining proper functional form for a regression, detecting autocorrelation, and identifying outliers and multicollinearity. In the first case, Active-PERM assumes the user is trying to determine functional form when two successive regression commands specify the same dependent and independent variables but different functional forms (e.g., linear and log). At that point, a message is relayed to the user asking whether functional form is indeed the objective; if so, the user is informed that the Box–Cox technique can be run to achieve this objective and this technique will be executed if so desired. This level of intrusion is passive and allows the user to override the CDPM easily. The other two areas of active support operate in a similar fashion.

Active-PERM supports active modeling in the sense described above using a model integration control language (MICL) [6] that sits on top of the PERM Action Language (PAL). PAL allows the user to specify any of PERM's available operations including regression estimation using a nonprocedural SQL-like syntax. The PERM Control Language (PCL) is an MICL that allows the development of processes that can then be invoked dynamically in a demonlike fashion. PCL has the following features:

1. process communication via message passing protocols;

2. structured programming constructs;

3. variable correspondence and dynamic synchronization for model integration;

4. variable monitoring (demons);

5. embedded PAL commands; and

6. reserved words (e.g., TSTAT, R2, SSTO, BETA).

PCL processes in concert with demons serve as the active component of the system. The general demon structure is as follows:

Demon: WHEN <Condition(s)> detected THEN <Activate> PCL Process(cs)

End-Demon

To see how this works, consider again the functional form example. A demon is constructed that searches the command stream to see whether the last two regression commands issued have the same dependent and independent variable list. If so, and different functional forms were specified in the two commands, then the functional form PCL process is fired. This process is nothing more than invoking the Box–Cox technique on the current variable list:

End-Demon

In this case, the demon conditions are monitored after every PAL command issued by the user.

The implementation of active features in Active-PERM has been hampered by the block-structured language in which PERM was developed. Each demon must be implemented explicitly by a suspend-resume mechanism programmed in Fortran. This complicates the management of processes requiring event-driven suspension. In general, each demon specified in Active-PERM must be implemented by explicitly inserting traps in the source code. This severely restricts how far we can advance active DSS concepts in this environment. The GOST system described in section 3 utilizes the object-oriented paradigm as a basis for implementing an MICL which subsequently overcomes these serious limitations experienced in Active-PERM. GOST is thus an example of how this more robust environment facilitates the development of active modeling systems.

## 2.3. Active Support for Process Modeling DSS

Our experience in developing and evolving DSSs into ADSSs favors a slightly different approach than described by Manheim [8]. We employ expert systems technology as a means for storing knowledge within the DSS and utilize an object-oriented paradigm for managing the processes responsible for delivering intelligent support. As will be discussed in section 3, we have developed a flexible, object-oriented knowledge representation system to facilitate the construction and management of the UDPM, CDPM, HIP, Schema Library, and History Recorder.

Object-oriented design provides a powerful means for simplifying the process management required in an ADSS. Object-oriented systems consist of a collection of independently related objects. By design, each object is self-contained and can be implemented as a distinct and separate process. By specifying behaviors for such objects, it is a simple matter to develop higher-level, more abstract objects that control lower-level objects. Areas where object-oriented design has proved valuable include development of operating systems for such platforms as the Macintosh and Symbolics computers. Incorporating such object-oriented technology within an ADSS provides a mechanism for managing the event-oriented nature of the UDPM, CDPM, and demon facilities described above. The challenge lies in merging this capability with the knowledge representation such that the message protocol serves as a conduit for message passing and performing inference. We have developed such a representation and discuss its details in section 3.

We have applied our knowledge gained in converting PERM from a DSS to an ADSS to the development of a Process Modeling System called GOST. While the details of the GOST system are described in section 3, a discussion on Process Oriented Modeling Systems (POMS) is warranted first. POMS involve the construction and analysis of models depicting the behavior of real-world systems. Although this general definition applies to modeling systems such as PERM, POMS require the development of a behavior model that is instrumented and exercised for the purpose of gaining insight into the real-world system.

One common method for exercising behavior models is through discrete-event simulation. Discrete-event simulation steps the model through its various states at discrete points in time. Performing a simulation experiment requires that a model be developed, verified, instrumented, exercised, and validated. Furthermore, analysis of the model should provide the analyst with feedback regarding how well the model met the goals of the experiment. According to Shannon [11], the process of developing and analyzing simulation models often requires specialized skills not widely available or easily retained from training. As a result, POMS are viable candidates for incorporating the active capability as a means for assisting the analyst with the construction, analysis, and optimization of behavior models.

The National Aeronautics and Space Administration (NASA) is involved with developing high-technology tools for assisting NASA engineers in costing and planning advanced space programs. POMS are one of many tools designed to study the impact of process improvements (based on new technology) on total program cost. As NASA has strongly encouraged the development of tool sets that actively assist the user (in this case the NASA engineer) in performing analyses, the need for active decision support is justified. We now discuss the GOST system as an active DSS.

## 3. GOST Overview

GOST IS A GENERIC MODELING ENVIRONMENT and decision support system that incorporates artificial intelligence and simulation technologies for planning and analysis of advanced space programs. Although GOST is a generic modeling environment, it is currently being used by NASA engineers for analyzing, costing, and planning future space programs, such as Lunar and Mars Missions, Space Station Freedom, Single Stage to Orbit, and Space Shuttle C. The active element within GOST minimizes the amount of knowledge the user is expected to have regarding such areas as programming, artificial intelligence, or simulation. In addition, GOST promotes a modeling methodology that allows the end user to benefit from the domain knowledge associated with a NASA expert versed in various space-related technologies.

## 3.1. GOST Modeling Methodology

GOST employs a modeling methodology that is based on the theory of Conceptual Modeling Methodology (CM) proposed by Gaines [5]. According to Gaines, CM is an abstract representation of a processing domain that is defined at a level consistent with a human expert's understanding of the domain. Deviating from conventional modeling approaches, CM is designed to identify a domain in terms of its abstract objects, relationships, functions, and behaviors. These abstract representations reflect the processing domain as the expert perceives it. Thus, the essence of CM is directed toward manipulating these model constructs and representations that directly map into the domain expert's cognitive element. In this manner, objects within the modeling environment behave in a manner consistent with the expert's perception, independently of the implementation vehicle.

One of the many benefits associated with CM is that a modeler can very quickly analyze a particular processing domain by simply instantiating and refining a conceptual model. Another significant advantage is that domain expertise is embedded within the model representation and is available to the end user. This aspect of CM has proved especially valuable for NASA analysts who lack detailed knowledge of a particular domain, yet have a solid global understanding of the system being modeled. Model reusability is yet another significant feature of CM, as it is not uncommon for models to be comprised of other submodel components.

The GOST implementation of CM is illustrated in figure 1. As an Active Decision Support System, GOST conforms to well-defined phases for performing analyses. Users typically adopt unique approaches for executing the details associated with performing a phase. Each phase is processed in the order specified by the figure. The modeling process begins with the phase labeled Domain Specifications, which describes the project specifications, name of the analyst, project date, and special requirements of the project. This is proceeded by Goal Definition, which focuses on documenting the specific goals of the project. Modeling then bounds the domain of interest and begins model construction, which includes class object instantiation, object attribute definition, relation and functional specifications, and conceptual model refinement. The product of the Modeling Process is a behavior model which is examined for inconsistencies by the Model Verification process. Model Execution exercises the behavior model using discrete-event simulation or parametric techniques, such as regression. Once Model Execution is complete, the analyst validates the model against real-world data (if available). Model Analysis evaluates the model performance indexes against specified goals. If the model is deemed sufficient to satisfy the goals of the analyst, it is committed to the model library as a scenario model and the model results are published via the Requirements process.

![](/api/attachments/K6SDE7ER/fulltext/images/a2d2c72fe68248134ce7f388eb92116558ed64c66d157735eeb28ca20e1875c3.jpg)  
Figure 1. GOST Modeling Methodology

## 3.2. GOST Architecture

The GOST architecture is specifically designed to provide the tools necessary for explicitly supporting all phases of the modeling methodology. GOST employs a layered tool set design surrounding a persistent object-oriented knowledge representation system, called KROS (see figure 2). Five distinct layers comprise the GOST environment: host system, representation system, kernel interface, tool set support environment (TSE), and model support environment (MSE). Hardware specific components, such as the operating system and host services, reside at the center of the environment. All communication is performed through the kernel interface which provides the communication protocol between all layers of the GOST system.

Users interact with GOST through the kernel interface, which serves as a direct conduit to the representation layer. Each tool set within the GOST environment is layered directly above the representation system, resulting in a tightly integrated system. This affords the unique opportunity to easily manage any tool set in the GOST environment from the representation layer. Each component within the TSE (see diagram) is implemented as a separate process and is managed by the operating system scheduler. Tool set components communicate with each other through the representation layer via the kernel interface.

GOST is grouped into logical modeling units to facilitate modeling and analysis of processing domains. Higher-level tools reside on the outer layer called the MSE. MSE tools provide the services for supporting active decision support, that is, they integrate and utilize a number of tool sets from the TSE, based on the user's model of problem-working. This capability provides a higher-level interface between the user and the particular modeling component within GOST. As will be discussed in section 4, a Computer-Directed Process Manager (CDPM) exists for each MSE to perform model definition, execution, and analysis within the GOST environment.

![](/api/attachments/K6SDE7ER/fulltext/images/da46ca250db469f05631dacc6bdb8d1dabdddd604d713815d9b676a80612a1af.jpg)  
Figure 2. GOST Conceptual Architecture

## 3.3. GOST Knowledge Representation

Effectively supporting active decision support requires a knowledge representation (KR) capable of representing both the static and the dynamic design characteristics of the modeling process. Static characteristics involve structural features of objects and their decomposition taxonomy. These characteristics include relationships such as “part/part-of” or “contains/contained-in.” Dynamic characteristics, however, are functional in nature, typically representing semantic relations, or procedures for design alternatives and evaluation $[10]$ . Therefore, an effective KR provides explicit features for representing and managing the procedures associated with object behavior. High-performance KRs also facilitate knowledge management within the context of object-oriented programming. Namely, the representation not only provides a vehicle for representing knowledge in an object-oriented fashion, but also provides an inference process that is consistent with the fundamental principles of object-oriented design. The result, called the Knowledge Representation for Object based Systems (KROS), forms the core of the GOST environment.

One of the key attributes of the KROS KR is that it supports object persistence. By integrating the transient KROS with an object-oriented database (OODB), a persistent representation system capable of modeling and simulating very large modeling domains (in excess of 20,000 objects) is feasible. Furthermore, through the OODB connection, KROS is effectively able to communicate and translate enterprise data that are stored in relational and object-oriented databases into meaningful knowledge units. Using a hierarchical segmented architecture, KROS organizes knowledge according to an object taxonomy. This allows knowledge to be segmented according to specific categories or themes and attached to the hierarchical object structure. These knowledge segments are then inherited by the descendants of an object for which the knowledge resides. In many conventional knowledge-based systems, the number of rules created for a single application is often enormous. Searching through this global rule base each time a rule is fired is computationally expensive. Since many rules frequently apply to specific situations, there is little that can be done to speed up the search for executing these rules.

Hierarchical Segmented Knowledge Bases (HSKB), developed by Castillo, McRoberts, and Sieck [2], encapsulate all rules in a general collection of rule sets that form the local knowledge base. These categories, or Rule Sets (RS), contain specific rules belonging to a particular theme. Special messages, called HSKB messages, are used to attach the rule sets to specific objects. When fired, HSKB messages collect relevant rules within the rule sets and form a local knowledge base on the object. Unification and search occur over these rules. The entire process is performed within the context of object oriented design. As an example, consider figure 3 where a Booster object uses Rule1 to select a Liquid Rocket Booster configuration. When a Liquid Rocket Booster object is faced with the same decision, Rule2 and Rule1 are used in the decision-making process. Since a Liquid Rocket Booster is a specialized type of Booster, it inherits Rule1 from its parent. Thus, the local knowledge base consists of both Rule1 and Rule2. It should be noted that a child object may also choose to override knowledge defined at the parent level. In such circumstances, rules defined at parent levels are not inherited by the children.

## 3.4. GOST Modeling Environment

The GOST modeling environment consists of both high- and low-level tools that explicitly support the CM methodology for developing and analyzing process models. Each tool provides a unique set of services and functions. Figure 4 illustrates the GOST Main User Interface which identifies four general phases for developing GOST models. Object Definition is the process whereby the user identifies the objects in the real-world system. Model Definition refers to the assimilation of these objects into a meaningful model structure complete with behaviors and model objectives. Model Analysis provides the tools to exercise the behavior model and analyze whether the objectives of the experiment are achieved. The Utilities component provides services for managing and organizing models and user data. These general modeling capabilities correspond to the MSEs of figure 1.

GOST supports two distinct classes of users: expert and end users. Expert model development captures the expert's domain knowledge and incorporates it into the model. These models form the templates from which other models are derived.

![](/api/attachments/K6SDE7ER/fulltext/images/91d251b96c0adfa43d200ccc76d619f8b8af72a37a3fcbfd947ef04fe945cbb2.jpg)  
Figure 3. HSKB Rule Architecture

![](/api/attachments/K6SDE7ER/fulltext/images/2ac3eb2aca3ef94a28b6970c94b6631bbeac04b52969e091fd69c51fe1420a3f.jpg)  
Figure 4. GOST Main User Interface

End-user model development generally involves the instantiation and manipulation of expert models. In the event that end users require a model that does not yet exist, then they must develop it themselves, or solicit the assistance of a domain expert for addressing the domain-specific decision-making processes within the model.

## 3.5. Applying the Modeling Environment to the Methodology

Constructing a model involves a number of phases, depending on the type of user (expert or end user). Expert users generally begin with the Object Definition tool set, proceed to Model Definition, and conclude with Model Analysis. End users typically begin with the Model Definition suite of tools and progress to Model Analysis. In general, domain expertise is inserted into a model using the tools from both the Object Definition and Model Definition MSEs.

![](/api/attachments/K6SDE7ER/fulltext/images/023a29b1ab16219906bd8b1c58e244269a5a90a2e689a95a7eb0b80e7712a4ad.jpg)  
Figure 5. Genealogy Tree for Shuttle Processing

Object Definition begins with the Genealogy tool, which provides the mechanism for creating GOST objects that are representative of the real-world system. This process not only identifies the objects, but associates them in terms of their taxonomic relations. For example, suppose a model of the NASA Kennedy Space Center (KSC) launch operations is desired. This model would contain the manpower and equipment associated with processing and launching the Space Shuttle. The Genealogy tool facilitates the identification and positioning of these objects in a Genealogy Tree. Figure 5 illustrates a genealogy tree for the above scenario. Genealogy trees allow lower-level objects to inherit properties from higher-level objects. Therefore, placing the objects in their appropriate position in the inheritance chain dictates from whom they may inherit attributes, icons, knowledge, and behaviors.

The Model Definition phase collects the objects identified during Object Definition and defines their interactions. Model Definition attaches behaviors to objects and defines the messages that invoke those behaviors. GOST employs a declarative structure, called a script, for representing object behavior $[2]$ . Scripts are the collection of temporally ordered activities that form the plan to achieve a desired goal state. Figure 6 illustrates a script defined for the object “Orbiters” that describes the activities an orbiter goes through during its Vehicle Assembly Building (VAB) operations. Each activity contains information regarding time of operation, required resources, location, and whether a learning curve is applied to the task.

![](/api/attachments/K6SDE7ER/fulltext/images/46b6edfaa1191c3cedfac862036d5926ce8ec890fea5e81f9b629e2c19ab9267.jpg)  
Figure 6. Orbiter Script for VAB Operations

The final stage in model development is to attach cost information to the model. GOST provides a unique method for defining cost information for model objects. Consider the object called “Engineer” from figure 6. Suppose we are interested in tracking how much of our manpower costs are associated with Engineering for shuttle launches over the next seven years. Further, suppose that historical data from the last ten years on Engineering hourly wages are available. GOST allows us to incorporate these historical wage data into a regression model which may then be used within an equation for calculating the Engineering direct cost. Figure 7 represents an equation for calculating Engineering direct cost. This equation is attached to the engineering object and updated throughout the simulation process. During simulation, Engineering utilization statistics are collected. When a value for Engineering direct cost is requested, the Engineer object applies its current utilization statistics to the equation. Engineering wage rate is regressed using the current simulation time as the independent variable. In this manner, GOST can effectively combine parametric data with state data derived from the simulation.

Once the model is constructed, and verified, it is simulated using a discrete-event approach. Results of the simulation are then analyzed to determine if the objectives of the experiment were achieved. Depending on the outcome of the analysis, future simulations based on modifications to the model are possible. As we will see in section 4, suggestions regarding what parameters to change are part of GOST's active modeling support.

## 4. GOST as an Active DSS

GOST ACQUIRED ITS ACTIVE CAPABILITY by implementing the following ADSS components: UDPM, CDPM, HIP, History Recorder, Schema Library, and Active Values (demons). Process managers (UDPM and CDPM) are represented as objects within the KROS representation system. We have identified a unique process manager associated with each MSE within the GOST environment. The process manager hierarchy is illustrated in figure 8. The root object is the class called Process-Manager. Two subclass objects are defined: User-Directed-PM and Computer-Directed-PM. The User-Directed-PM is a class object currently only supporting a single instance, called the UDPM (user directed process manager).

![](/api/attachments/K6SDE7ER/fulltext/images/361b6b9867cdd978b814e8352deefd8332b4ea0d5bad47e793012a7ce3427c16.jpg)  
Figure 7. Equation for Computing Engineering Direct Cost

![](/api/attachments/K6SDE7ER/fulltext/images/2d977f09a25975e6f3c8e3101ec09ddaf9765280d492f4219a2c7a96dba380e6.jpg)  
Figure 8. GOST Process Manager Taxonomy

Computer-Directed-PM represents the computer-directed family of process managers. Currently, there are four instances of the Computer-Directed-PM. The first instance, called the CDPM-Object-MSE, is the CDPM for providing support in the object definition tools. Similarly, the CDPM-Model-MSE manages support for the Model definition process. Instance objects CDPM-EXEC-MSE and CDPM-ANALYSIS-MSE manage support for model execution and analysis respectively. By specializing the CDPM into a set of computer-directed process managers, each directly related to a high-level modeling activity, we effectively reduce the amount of heuristic programming needed for a single CDPM. Essentially, each specialized CDPM contains a local schema library associated with the tool sets it is responsible for managing. This local schema library is unified with the user History Record to determine if active support is required. When a successful unification is made, the CDPM invokes the appropriate command sequences that invoke the active support.

Just as in PERM, the inference process is triggered each time the user issues a command or series of commands. The primary difference is that the History Recorder informs the History Record to assert a new user entry. After the assertion is performed, an after-added demon is fired alerting the appropriate Process Manager of the new entry. At this point, a specific Process Manager, such as the CDPM-Model-MSE, performs an inference over the history record attempting to match the user's input with a template schema contained in the CDPM-Model-MSE's local knowledge base or any of its ancestor's knowledge bases. If a match is located, the CDPM-Model-MSE informs the appropriate MSE to activate a tool set to assist the user with the desired task. Although the implementation details differ from our experience with PERM, the ADSS concepts implemented in GOST are similar. The primary differences are a function of the implementation vehicle. Through the use of an integrated. objectoriented representation and inference system, process-to-process communication and control are easily managed.

## 4.1. A Domain-Dependent Example of Active Model Development

As discussed in section 3.1, the amount of modeling and domain knowledge required to formulate and exercise behavior models is often overwhelming for an end user. The utility of a DSS, however, is measured by its ability to provide the user with effective decision support. Many users often lack the technical skills or expertise required to fully understand the complexities of a processing domain. Thus, the active DSS should provide assistance in the form of domain-dependent and/or domain-independent support for the end user. Our efforts in providing the end user with active support have focused on the model development and analysis activities.

The GOST modeling methodology facilitates model development by providing the end user with a meta-model that can be instantiated, manipulated, and exercised. Meta-models contain expert knowledge regarding the behavior of a domain under various conditions. This knowledge is contained and managed within the meta-model. For the sake of this discussion, we will assume the user wishes to investigate the feasibility of replacing Solid Boosters with Liquid Boosters. The user first logs on to the GOST system by typing in a password. Upon entry, the UDPM consults the user database to determine the sophistication level of the user. Once this is determined, the UCPM displays the following choices:

1. Develop a Model

2. Continue Working on an Existing Model

3. Exercise a Model

4. Analyze a Model

5. Report Model Results

Suppose the user selects the option “Develop a Model.” The History Recorder informs the History Record of the user level and GOST command. Upon receiving these data, the History Record broadcasts that a new entry has been posted. The CDPM-Model-MSE is the only CDPM able to match the command in the History Record against its local knowledge base (local schema library). Upon matching the command, the CDPM-Model-MSE determines the user level and triggers an automated scenario-generation process to assist the user in developing the model.

Automated scenario generation follows the methodology illustrated in figure 9. The process labeled “Bound Domain” accepts the analyst’s informal goals and bounds the domain of interest. This is performed by asking the user which processing domain they are interested in modeling. The CDPM-Model-MSE retrieves the various domains from the model repository and presents them to the user in the form of a dialog menu. Selecting the domain of interest then serves to bound the problem and focus the effort of the CDPM-Model-MSE.

Models are catalogued in a model repository in much the same manner as data are stored in a relational database. The difference, however, is that GOST stores and manages models according to an object-oriented format. Therefore, it is straightforward to tell the database to return all the processing domains it currently contains. There are a number of projects associated with a particular processing domain. Similarly, there are a number of models associated with a project, and a number of objects contained within a single model. This relationship is maintained by the structures illustrated in figure 10.

![](/api/attachments/K6SDE7ER/fulltext/images/58038f1ae6192710cb6ba3ee92a07abf34de0a9298f1926146a92f8016592ff3.jpg)  
Figure 9. Active Modeling Process

![](/api/attachments/K6SDE7ER/fulltext/images/1cd9882e5431e81d208318584c3a2de85609d492489a89e984e5c143fecd3dfd.jpg)  
Figure 10. GOST Model Base Structure

Once the domain is selected by the user, the CDPM-Model-MSE displays all the projects associated with the selected domain. The user then peruses the projects and determines the one that best represents his problem domain. Each project model is then presented to the user to determine which model is best suited to address the specific needs of the study. For example, a model determining the amount of space needed to accommodate fifty additional employees at NASA-KSC is not well suited for determining the feasibility of replacing Solid Boosters with Liquid Boosters. Upon selecting a model, the CDPM-Model-MSE begins a process called Model Synthesis.

Model Synthesis is a process whereby the CDPM-Model-MSE engages a pruning process that traverses the genealogy tree for the purpose of selecting only those objects required by the user. At each level of the tree, the user is issued a query regarding whether the object in question is relevant to the study. For example:

Does your Analysis require the use of BOOSTERS?

YES NO HELP >Y

There are 2 classes of BOOSTERS, select the appropriate ones.

SOLID-BOOSTERS LIQUID-BOOSTERS

The user has confirmed that his analysis requires the use of BOOSTERS. The pruning process determines that the model supports two types of BOOSTER rockets: solid and liquid. Both options are presented to the user for selection. In this case, both are selected, as both are required in the analysis. Following the pruning process, the CDPM-Model-MSE asks the user if any additional objects are required for performing the analysis. If the response is yes, the user is placed in the Genealogy Editor where he can manually construct any additional objects.

Exercising behavior models involves attaching instruments to the model structure for reporting the various states of the objects. For example, an instrument may be attached to the Engineer class reflecting how many Engineers are being utilized. After the model is instrumented, a simulation is performed over a predetermined time period or until all events within the model have completed. Results of the model (generally contained on the instruments) are then analyzed by the user. Changes can then be made to the model to investigate “what if” scenarios. An example in the BOOSTER world may reflect a simulation that utilizes existing facilities for processing Liquid Boosters. Another simulation may create a new facility designed specifically for processing Liquid Boosters. These scenarios may then be compared to determine which is most cost effective.

What-if analysis is an area where domain specific knowledge adds to the active capability of GOST. Suppose a domain expert defines a set of rules suggesting changes in the model based on specified simulation results. For example, consider the rule:

IF Utilization of VAB > .85 AND

Total Cost of LB 30M AND

Total Time 6 Months AND

Utilization of LRB Techs .5

THEN Construct New Facility = (Volume of VAB \*.5)

The above rule states that if the simulation results indicate that the utilization of the

Vehicle Assembly Building (VAB) is high, and the cost for processing Liquid Boosters exceeds 30 million in a six-month period, and the utilization of Liquid Rocket Booster Technicians is low, then create an additional facility whose volume is estimated at half the volume of the VAB.

As the model is executing, the CDPM-Analysis-MSE monitors the state of the objects described in the above rule. When conditions of the rule are satisfied, the rule fires and the user is presented with an option to continue the simulation, or stop and make the recommended changes to the model. This capability in essence places an artificially intelligent domain expert at the end user's side.

## 4.2. NASA's Experience with GOST

Since its delivery in January of 1990, GOST has assisted NASA engineers and cost analysts in a number of studies at the Kennedy Space Center. These applications have ranged from assessing the cost associated with processing liquid rocket booster space shuttle configurations to evaluating the cost effectiveness of a large-scale unmanned cargo shuttle (Shuttle C) for developing Space Station Freedom. In addition, Lunar and Mars Mission studies are actively being pursued using the GOST environment. Preliminary feedback from the GOST user community strongly supports the usability and effectiveness of GOST as a decision support environment. As a result of this acceptance, GOST has gained increased visibility throughout the NASA community.

Based on feedback from the NASA user community, improvements/enhancements to GOST will span three primary areas. The first area involves capturing more domain-specific knowledge within the NASA models. The second area includes the addition of more parametric cost modeling tools that provide domain-independent active support, such as those contained within PERM. Third, research issues concerning model management using object-oriented techniques are being pursued by the authors. GOST is written in C++ and runs on UNIX Motif workstations.

## 5. Conclusions and Future Research

THIS PAPER HAS DISCUSSED AN ACTIVE DECISION SUPPORT SYSTEM, called GOST, currently in use at NASA for costing and planning advanced space programs. The GOST implementation is based on our experience with PERM for delivering active modeling support in the area of econometric estimation. Our approach, however, extends this previous effort by providing a layered tool set architecture that surrounds an object-oriented persistent knowledge representation system. This results in a modular decision support environment that is tightly integrated with the HIP, UDPM, CDPMs, and History Recorder, all of which are essential components of an ADSS. By using an object-oriented design approach, we distribute the control and management of the active processes across the various ADSS objects. The results of our efforts have demonstrated an effective means for coordinating and delivering active support within a decision support environment.

Future research will span both the practical and theoretical aspects of ADSS technology. From a practical standpoint, we will investigate the incorporation of PERM-like parametric modeling capability within the GOST environment. Other, more theoretical concerns will focus on developing student models to assist the CDPMs with detecting when active support is warranted, as well as selecting the type of active modeling to present to the user. The results of this research will benefit both domain-dependent and domain-independent active modeling approaches.

## REFERENCES

1. Castillo, D.; McRoberts, M.; and Sieck, B. Embedded expert systems improve model intelligence in simulation experiments. Proceedings of 1988 Summer Simulation Conference, Society for Computer Simulation, 1988.

2. Castillo, D.; McRoberts, M.; and Sieck, B. HSKB: an architecture for embedded reasoning in simulation systems. Proceedings of SCS Western Multiconference, Society for Computer Simulation, 1989.

3. Dolk, D.R., and Kridel, D.J. Toward a symbiotic expert system for econometric modeling. Proceedings of the 22nd HICSS, vol. 3. IEEE Computer Society, 1989, pp. 3–13.

4. Dolk, D.R., and Kridel, D.J. An active modeling system for econometric analysis. Decision Support Systems, 7, 4 (1991), pp. 315–328.

5. Gaines, B.R. An overview of knowledge acquisition and transfer. In Knowledge Acquisition for Knowledge-Based Systems, B.R. Gaines and J.H. Boose, eds. New York: Harcourt Brace Jovanovich, 1988.

6. Kotteman, J.E., and Dolk, D.R. Process-oriented model integration. Proceedings of the 21st HICSS, vol. 3. IEEE Computer Society, 1988, pp. 396–402.

7. Manhiem, M. An architecture for active DSS. Proceedings of the 21st HICSS, vol. 3. IEEE Computer Society, 1988, pp. 356–365.

8. Manhiem, M. Issues in design of a symbiotic DSS. Proceedings of the 22nd HICSS, vol. 3. IEEE Computer Society, 1989, pp. 14–23.

9. Oldford, R.R., and Peters, S.C. Implementation and study of statistical strategy. In Artificial Intelligence and Statistics, W.A. Gale, ed. Reading, MA: Addison-Wesley, 1986.

10. Rozenblit, J., and Zeigler, B. Design and modeling concepts. In Encyclopedia of Robotics, R. Dorf, ed. New York: Wiley, 1988.

11. Shannon, R.E. Intelligent simulation environments. Intelligent Simulation Environments, 17, 1 (1986), 150–156.
