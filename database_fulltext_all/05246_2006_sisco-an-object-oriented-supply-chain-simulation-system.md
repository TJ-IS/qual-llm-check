---
otero_id: 5246
otero_key: "FD6FS55Z"
title: "SISCO: An object-oriented supply chain simulation system"
authors: "Dean C. Chatfield; Terry P. Harrison; Jack C. Hayya"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.02.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# SISCO: An object-oriented supply chain simulation system

Dean C. Chatfield <sup>a</sup>, Terry P. Harrison <sup>b,T</sup>, Jack C. Hayya <sup>b</sup>

<sup>a</sup> Department of Business Information Technology, 1007 Pamplin Hall (0235), Pamplin College of Business, Virginia Tech, Blacksburg, VA 24061, USA

<sup>b</sup> Department of Supply Chain and Information Systems, Smeal College of Business, 509L Business Administration Building, Penn State University, University Park, PA 16802, USA

Available online 7 April 2005

## Abstract

We present SISCO, the Simulator for Integrated Supply Chain Operations, an object-oriented supply chain simulation tool. SISCO advances the concept of a supply chain simulator in a number of ways. With SISCO, we introduce a fundamentally new approach to supply chain specification, storage, and model generation. The user specifies the structure and policies of a supply chain with a GUI-based application and then saves the supply chain description in the open, XML-based Supply Chain Modeling Language (SCML) format. SISCO automatically generates the simulation model when needed by mapping the contents of the SCML file to a library of supply-chain-oriented simulation classes. SISCO’s object-oriented, agent-style system architecture and detailed output improve upon current supply chain simulation tools.

Keywords: Supply chain; Simulation; Object-oriented simulation; Agent-based simulation; Decision support systems; XML; Java

## 1. Introduction

We begin by providing the motivation for creating SISCO and the research issues we encountered, especially capturing the effects of uncertainty in supply chain processes. We discuss the relative advantages of SISCO and the flexibility it offers in the simulation of supply chain operations.

## 1.1. Supply chain simulation

Simulation modeling can provide valuable insights into the operational characteristics of supply chains. Variability and uncertainty are endemic in all systems, and certainly so in supply chains. In Ref. [3], Chatfield found that uncertainty in demands, production yields and rates, transportation times, and cost of goods over time are commonplace in the actual operation of a supply chain, yet these operational factors are often modeled deterministically. By accounting for uncertainty when modeling supply chains, we can gain insight into the impact of these factors. Thus, simulation modeling provides an important tool for understanding supply chain behavior under changing conditions and can give the information necessary to make informed decisions regarding supply chain design and management. Realizing the potential of supply chain simulation, academics and practitioners alike have developed many supply chain simulation tools to assist modelers. However, there are many areas for improvement of such simulation tools.

## 1.2. Issues addressed and contributions

We developed the Simulator for Integrated Supply Chain Operations (SISCO) to provide researchers and practitioners with a robust and flexible simulation tool designed to address the complexities in modeling supply chains. SISCO improves upon current supply chain simulation tools by addressing five issues: model storage, system architecture, ease of use, model depth, and output. First, we employ a novel approach to model storage. We do not store the model at all. Instead, we focus on storing a description of the supply chain in an XML-based file and generate the simulation model on demand. Second, SISCO’s architecture is well-matched to the task of supply chain simulation, while also providing extensibility. We create a tool that produces objectoriented, agent-style, multi-threaded simulation models. Third, we create an easy to use tool. Although other simulators have taken a GUI-driven approach, we change the user focus to that of creating an accurate supply chain description, not on modeling. Then, users create a supply chain description and the SISCO system generates the model. Fourth, with regard to model depth, we believe SISCO to be a step forward from current simulators, because it allows users to specify any aspect of a supply chain’s operations as stochastic; it allows explicit description of the connections (arcs) between supply chain participants; and it allows a complex user-defined logic. Fifth, SISCO provides a wider variety of output data than currently available, for example, replication and time series data. We have already used SISCO to investigate the phenomenon of demand variability amplification, often referred to as the Bullwhip Effect (BWE), by examining the impact of lead-time variability and forecasting method on the severity of the BWE [4].

## 1.3. Organization of paper

This paper is organized into seven sections. Section 2 discusses related literature and software, assessing the shortcomings of current simulators and highlighting the importance of our research. Section 3 is an overview. The components of SISCO are described according to their role (input, processing, or output) in Sections 4, 5, and 6. Section 7 discusses the ideas behind SISCO. Section 8 outlines further research directions. To conserve space, we have placed technical details and appendices in a working paper [6].

## 2. Related work

In Section 1 we provided the motivation for the development of SISCO. Here we relate SISCO to other supply chain simulators. We focus especially on the ability and ease of use to create, analyze and share supply chain models.

## 2.1. Other simulators

Several supply chain simulators have been created in recent years, with the intent of providing a simple environment for supply chain modeling. In Refs. [17,18] the authors describe the architecture and foundation for a supply chain simulator that takes a decentralized perspective and allows one to specify that individual processes in the supply chain act which operate autonomously. That work resulted in a prototype toolkit for a general supply chain simulation system, which used CACI Inc.’s SimProcess as a foundation. The prototype was used as the basis for IBM’s Supply Chain Simulator (now Analyzer).

Other early simulators include those mentioned in Ref. [7] which describes a Visual Basic supply chain simulator, and in Ref. [19], a logistics simulator that allows a user to define a simple supply chain via a set of wizards. The Zhang et al. system [19] was developed using Microsoft Visual Basic and Rockwell’s Arena.

IBM presented the Supply Chain Analyzer (SCA), formerly Supply Chain Simulator [1]. IBM’s SimProcess-based SCA represents the current state of the art; it is a further development (2+years) beyond the

Swaminathan [16] prototype. Other commercial examples include Simulation Dynamics’ Supply Chain Builder [14] and LlamaSoft’s Supply Chain Guru [11].

Most supply chain simulators utilize a general simulation language as their engine, and many of the simulator vendors have become partners with the suppliers of the general simulation language they employ. The simulators add supply-chain-specific building blocks to the general purpose simulation tool to assist the modeler with the complexities of supply chain simulation modeling. LlamaSoft’s core is a Pro-Model-based and ProModel-supported application that emphasizes a four-step approach to supply chain analysis and design: network optimization, network simulation, policy optimization, and design for robustness. Along the same lines, Simulation Dynamics <sup>b</sup>Supply Chain Builder<sup>Q</sup> is an Extend-based simulation tool. Imagine That (maker of Extend) is an active partner in the promotion of Supply Chain Builder, which utilizes the Extend + Industry product as its core [14].

Herrmann et al. [10] describe a system that follows the Supply Chain Operating Reference (SCOR) model as a framework for information storage. Their system is based on Rockwell’s Arena in conjunction with Microsoft’s Excel, with the goal of creating supply chain simulation models based on reusable Arena components and using the SCOR model as a central framework. GenSym’s e-SCOR simulator [8] takes a similar approach to that of Herrmann et al. The e-SCOR tool allows the user to build a simulation model using the basic SCOR format plus additional details. GenSym’s e-SCOR is built on their G2 modeling environment, a general, object-oriented modeling tool.

In Ref. [13], Rossetti and Chan developed a prototype simulator called SCSF (supply chain simulation framework), which is a Java-based object-oriented representation of a supply chain that uses a database to store the model. They indicate that using the database to store object information solves the <sup>b</sup>object persistence problem,<sup>Q</sup> which requires that the objects be recreated each time the model is built.

Biswas and Narahari [2] discuss an object-oriented tool called DESSCOM for supporting supply chain decision making. It is comprised of a workbench of optimization and simulation solution techniques, and a modeling tool featuring pre-built supply chain objects.

## 2.2. Assessment

We identify five important supply chain simulator design and development issues and assess the shortcomings of current simulators in these areas. As described in Section 1.2, we developed SISCO to address these issues by using new technologies, new approaches, and judicious design.

## 2.2.1. Model storage

Some simulation languages, such as SimProcess, store their models in XML-based files. However, this does not provide any interoperability advantage, since the format is still not open to the public and, more importantly, the model description is still only applicable to the simulation language being used. Herrmann et al. [10] and GenSym’s e-SCOR [8] both utilize the SCOR model for modeling the supply chain, which is appealing, since the SCOR model is well-known and the Supply Chain Council backs it as a supply chain process documentation standard [15]. However, the SCOR model was not designed with quantitative modeling in mind, and thus SCOR must be augmented with additional detail to make it useful for simulation modeling. Finally, all current simulators store a representation of the model, not the supply chain itself. None of the simulators employ XML-based information storage or employ automated model generation. Hence, an open storage format that contains a supply chain description, rather than a specific model, is a step forward.

## 2.2.2. Architecture

Most simulators are based on commercial simulation languages and tools, such as Arena, Extend, ProModel, and SimProcess. Instead of a general purpose simulation language, Rossetti and Chan [13] developed their own Java-based simulation resources, and GenSym utilized its G2 modeling product for creating e-SCOR [8]. Many of underlying languages are object-oriented and confer advantages regarding reuse of components. However, even the simulators advertised as <sup>b</sup>objectoriented<sup>Q</sup> do not generate truly multi-threaded models that run each object in its own thread of execution. Thus, both object-orientation and multithreaded models are important in accurately representing a supply chain—to have each participant operating independently and concurrently with the other participants.

## 2.2.3. Ease of use

Almost all current simulators employ a GUI-based method of model construction, instead of requiring coding on the part of the modeler. Some, like in Ref. [10], are tabular because of their use of Microsoft Excel as a front-end, while others are flowchart-like in nature, such as Simulation Dynamics’ Supply Chain Builder. All focus on model building as the primary activity of the user. But increased use, as well as increased accuracy, can be obtained if the focus of the user is on describing the supply chain, not on building the model.

## 2.2.4. Model depth

There are several areas, such as lead times and costs, that many current simulators characterize deterministically, not stochastically. None of the simulators allows explicit definition of arcs (connections between locations, usually representing transportation); instead, they represent the arcs as time delays between points A and B. Regarding the modeling paradigm, current simulators focus on supply chain locations or modeling blocks. Additionally, Supply Chain Builder is the only tool that allows user-defined complex policies [14]. Allowing more supply chain factors to be characterized as stochastic, along with a better representation of supply chain inter-connections, is useful additions to supply chain simulation models.

## 2.2.5. Output

The output of these simulators is primarily dependent on the underlying simulation system used. These packages provide very good summary reports, but, in many cases, do not provide results of replications grouped together for further analysis. Some information is not reported, such as forecasting characteristics and order variability. And we are not aware of any existing simulators other than SISCO that provide time series data to allow analysts to inspect the behavior of the supply chain over time.

## 3. Overview of SISCO

## 3.1. Application structure

In Fig. 1, we present a graphic overview of SISCO, which involves four stages: input, model generation, model execution, and output. SISCO is comprised of two modules:

<sup>!</sup> TheVisual Supply Chain Editor (VSCE)

<sup>!</sup> The SISCO Engine.

The VSCE and the SISCO Engine are individual, stand-alone applications, whose components are not only useful as part of the SISCO system, but also in conjunction with other supply chain modeling software. These pieces may be incorporated into a multitool analysis workbench, allowing modular tools to be attached to create an integrated supply chain analysis system. Additionally, by separating SISCO into modules, we allow distributed usage where the user invokes the VSCE locally and submits the model information to a remotely served SISCO Engine. By separating the Java-based Engine from the rest of the system, this architecture admits the possibility of Web-based distributed processing.

At the input stage, the users describe the supply chain as well as the experimental conditions. The VSCE allows a user to build a supply chain through a graphic user interface (GUI) and then specify relevant logical and descriptive information. The result is a supply chain description, not a model, stored in an open, XML-based format we call SCML (Supply Chain Modeling Language). See Ref. [5] for visuals and details of the VSCE. Simulation-specific information, such as run length or the number of replications, is stored separately in an experiment file (EXP), using the standard comma-separated value format. The experiment file may be created in a text editor, spreadsheet or other application that can output comma-separated data.

![](/api/attachments/FD6FS55Z/fulltext/images/ed1f4b83f485d3d0b8717cc9142c8ec541dea3c9cc94eb20198c7b9e894ae6d8.jpg)  
Fig. 1. SISCO System overview.

At the model generation stage, the supply chain description (SCML file) is translated by the SISCO Engine into an equivalent Java-based object-oriented simulation model. The SISCO Engine maps the SCML file contents to the SISCO Library, a Java library of supply chain simulation building blocks, creating the appropriate Java objects that form a simulation model. Model execution is performed by the SISCO Engine in conjunction with a Java compiler. The experiment information contained in the EXP file is utilized at execution time. The output of the SISCO system is extensive and could be used for various types of analysis. The user is presented with a simulation summary detailing the performance characteristics for each node and arc over all replications. The user is also provided with a data file containing the performance characteristics for each individual replication, and another file containing time series data.

The SISCO Engine uses the SCML and EXP files as input, processes the information contained in those files to automatically build a Java-based supply chain simulation model, and outputs a simulation summary, individual replications, and time series data.

## 3.2. Silk

To provide SISCO’s basic simulation capabilities we employ Silkk, a Java-based, multi-threaded, discrete-event simulation framework created by ThreadTec [9]. It consists of a set of Java classes that provide low-level, core simulation constructs from which users create simulation models. Examples of these constructs include entities, resources, queues, statistical tracking variables, the system clock, random number generators, and other fundamental pieces of discrete-event simulation. Users build a Silkk simulation model by developing a Java program that uses the Silkk simulation classes. Users can extend the Silkk classes, as well as include any custom logic, by creating additional Java routines. Utilizing the lowlevel simulation classes provided by Silkk gives SISCO several advantages over simulators using general simulation languages. First, Silkk allows

SISCO to create truly object-oriented, multi-threaded simulation models, which is important in capturing the nature of supply chain operations. Second, it allows greater flexibility, because we are able to use the capabilities of Java when creating SISCO. Third, it improves SISCO’s extensibility and makes userextensions easier.

## 4. Input

## 4.1. Model storage

A fundamental difference between SISCO and other simulators is that SISCO does not store a supply chain model per se. Instead, it stores a supply chain description in an open, XML-based, methodologyindependent format. When needed, the simulation model is generated by SISCO. Several advantages result. First, if we store a supply chain description, then the user will concentrate on creating an accurate supply chain description, and not on modeling issues. We allow the user to focus on the primary issue and let SISCO handle the modeling tasks.

Second, the absence of an open, standardized method of storing a representation of supply chain structure and operations hampers supply chain research and modeling. For modeling and analysis of supply chains, a <sup>b</sup>toolbox<sup>Q</sup> approach is appropriate. A single format that stores a supply chain description with sufficient detail to support quantitative modeling will encourage multi-method analysis and make the development of multi-tool supply chain analysis workbench systems more feasible. If the same description can be used to build various models, it would be helpful to supply chain analysts. Consequently, it is important to use a general, structured representation of supply chain information storage in SISCO. We employ the Supply Chain Modeling Language [5] as a standard method for describing the structure and policies of a supply chain. Note that we designated it as a <sup>b</sup>modeling<sup>Q</sup> language to indicate that it is utilized for modeling, not that it stores a model.

## 4.2. Modeling language

SCML is an XML-based, platform and methodology-independent means of storing the structural and managerial information that describes a supply chain’s layout and operational characteristics. It is a set of elements, attributes, and document rules that create a systematic format for a supply chain representation. SCML is defined by a document type definition (DTD), written in XML. Much as HTML is a set of elements, attributes, and rules for describing how hypertext is to be displayed by a browser, SCML is a set of elements, attributes, and rules for representing a supply chain. SCML provides a universal language with which users can store and exchange supply chain information, primarily for quantitative modeling. We created the VSCE as a graphic SCML editor to let the user define a supply chain’s structure and characteristics and then save this information as an SCML file. That done, the information can be used by any SCMLcompliant application [5].

## 4.3. Supply chain information

In order to adequately describe a supply chain for purposes of creating a quantitative model, both the physical and logical design aspects of the supply chain must be defined. We divide the supply chain into five types of constructs: nodes, arcs, components, actions, and policies. The nodes, arcs, and components constitute the physical aspects of the supply chain.

Nodes represent locations within the supply chain, such as a factory. We allow a user to create suppliers, production facilities, warehouses, distributors, retailers, and customers. The basic supply chain layout is built in a drag-and-drop fashion, resulting in a set of nodes and arcs that define the general supply chain topology. Beyond that, it is necessary to define the properties of each node and arc within the supply chain. The node properties include inputs and outputs, order and shipment routings, independent demands, storage capacities and costs, overhead costs, actions that can occur at a node, and policies, such as those for inventory.

Arcs represent the connections between nodes and are defined by their endpoints. We define the arc’s mode (land, rail, air, water, or telecommunications), capacity, container size, transportation rates and costs, maintenance and expansion costs, as well as the policies that may control the arc’s actions. Components include materials, finished goods, labor, currency, and other items that are consumed, transported, created, or otherwise used in the supply chain. The value, physical characteristics, and the methods of creation must also be defined.

Beyond the physical aspects, the actions and controlling logic of the supply chain must be entered. Actions include demand or replenishment order placement, order processing, transportation, receiving, or shipping. Also included are policies that define conditions under which actions occur by describing circumstances that trigger the actions or by defining goals that are to be met. Finally, the policies of the supply chain describe relationships between supply chain participants, and the controls or logic under which actions occur.

## 4.4. Experimental information

Experimental control information is needed to create an executable simulation. This information includes information regarding environmental variables, such as the number of replications, animation settings, and output statistics, and is specified in an experiment (EXP) file.

## 5. Simulation model generation

SISCO translates the supply chain description into an equivalent Silkk-based supply chain simulation model via the SISCO Engine. To accomplish this, a mapping scheme and a set of specially-designed supply-chain-oriented Silkk compatible Java classes are used to create a Java representation of the supply chain. The SISCO Engine is composed of

<sup>!</sup> The SISCO Library,

<sup>!</sup> The SISCO Automated Model Mapper (SAMM),

<sup>!</sup> Simulation management routines.

The SISCO Library and SAMM are described in Sections 5.3 and 5.4. The simulation management routines handle Java and Silkk housekeeping, provide the GUI for the SISCO Engine, compile statistics, create other output files, and provide a container for the SISCO Engine routines.

## 5.1. Modeling paradigm

Most current simulators concentrate on blocks or supply chain locations. Ours, by contrast, creates autonomous units representing each node or arc within the supply chain. These objects interact with each other, performing the basic actions an order undergoes during its processing, and we approach the modeling of a supply chain from the perspective of an order’s life cycle, to provide greater model depth. The order life cycle we employ is the following:

<sup>!</sup> order creation (occurring at the origin node)

<sup>!</sup> order placement (origin node)

<sup>!</sup> order transport (information arc)

<sup>!</sup> order processing (target node)

<sup>!</sup> order shipping (target node)

<sup>!</sup> filled order transport (shipment arc)

<sup>!</sup> order receiving (origin node).

## 5.2. Representing the life cycle

Of the seven actions in the order life cycle, five occur at nodes: order creation, order placement, order processing, order shipping, and order receiving. These actions may be performed differently depending on the type of node (supplier, production point, warehouse, distributor, retailer, or customer). The remaining two actions (order transport and filled order transport) occur at arcs. We begin by describing the actions that occur at the nodes.

Order creation involves the creation and initialization of a production lot, and orders are initially created by an inventory rule or by an external demand generated by a customer node. At the time of creation, an order is a request for an item. To act upon that request, the order must be placed.

Order placement makes the order known to the supply chain; it is not the same as the initial creation of the order. Order placement prepares an order for transport to its target, which is the node that will fill it. The placement process may include processing delays and costs and is also where the routing of the order may be determined.

Order processing attempts to meet the needs or demands of the order. Fulfillment of an order is attempted from the finished goods inventory at the node. If finished goods inventory cannot meet the order’s needs, the order waits until more goods arrive. Finished goods arrive as a result of a processing delay (for suppliers), a production process (for production nodes), or the placement of an order (stocking point nodes). The completion of the order processing action is the point at which the order begins the return trip to its origin.

Order shipping is the process of preparing the filled order for transport back to its origin node and may involve grouping of certain orders together, prioritizing orders, or the handling and processing of goods to be shipped. As with order processing, there may be costs and delays associated with shipping.

Order receiving is the process of accepting an order that has been filled. Orders received are those that were placed in the past and have traversed their life cycle. The receiving process serves to organize the receipt of goods and ensures they are accounted for in inventory ledgers or customers-served tallies.

Movement of an order is also an important part of the life cycle. Arcs represent the movement of an order in a single direction between two nodes. Arcs can be for information (unfilled order), or delivery (filled order). SISCO allows the explicit definition of events that occur during transport, such as time delays, costs, and product transformations. Since an order may take multiple arcs to complete its life, these transportation processes may be performed multiple times during the life of a single order.

Finally, other operations, such as inventory management, are also represented. Such processes are generally <sup>b</sup>owned<sup>Q</sup> by a node and are controlled by <sup>b</sup>managers<sup>Q</sup> who coordinate the logic and actions necessary to implement the process.

## 5.3. The SISCO library

The implementation of the modeling approach described above is based on a specialized set of Java classes known as the SISCO Library. By utilizing the Silkk primitive classes as a basis, we develop a library of specialized, Silkk-compatible Java classes that represent the various pieces of a supply chain.

## 5.3.1. X-Classes

The first part of the SISCO Library is a set of approximately 50 Java classes, known as <sup>b</sup>x-classes,<sup>Q</sup> <sup>b</sup>x<sup>Q</sup> standing for XML focus. The x-classes are dataonly classes that provide a means of representing the supply chain contained in an SCML file as a set of Java classes with the same hierarchical structure.

## 5.3.2. Operational classes

Whereas the x-classes are data storage, the operational classes represent object types that perform operations and interact with each other in a manner that simulates a supply chain. The operational classes represent the nodes, arcs, and orders of the supply chain, as well as the managers and actors that control and perform tasks within these elements. The operational classes of the SISCO Library include the following: Order, Node, Arc, and multiple Manager and Actor classes.

Our modeling paradigm focuses on the life cycle of an order, so a well-designed representation of an order is important. The most important part of the Order class is its guidance of the order through the life cycle. The order controls its own sequence of actions, but the nodes determine the details of where and how those actions will occur.

Besides accurately representing an order, we need to represent the nodes and arcs that define the structure of the supply chain. The Node and Arc classes are templates for the creation of objects that represent the nodes and arcs. These classes contain routines that enable the creation and control of Managers, variables, arrays, queues, resources, statistical tracking variables, and others necessary to simulate the operation of the node or arc. The most important part of the Node class involves the coordination of actions that occur at a node: order creation, order placement, order processing, shipping, and receiving. The Arc class is similar to the Node class, except it is much simpler because arcs only perform order transport.

The Manager classes include the OrderPlacement-Manager, OrderProcessingManager, ReceivingManager, ShippingManager, TransportationManager, InventoryManager, and DemandGenerator classes that form the basis for objects that control the actions occurring at the nodes and arcs. The Manager classes contain the monitoring, logic, and actor creation routines necessary for a Manager object to independently monitor and control one of the basic life cycle actions and to create an appropriate actor object when that action needs to occur.

The Actor classes define templates for finite lifespan objects created to allow multiple, independent, simultaneous actions. The actor objects are created to perform a specific action one time, after which they are destroyed. The Actor classes include the Order-PlacementActor, OrderProcessingActor, ReceivingActor, ShippingActor, and TransportationActor. The relationships between the Nodes and Arcs, the Managers, and the Actors is fundamental to the way SISCO operates.

## 5.3.3. Owner–manager–actor structure

We wish to build supply chain simulation models that allow the various actions of participants to occur concurrently. Utilizing an object-oriented, multithreaded environment gives us the capability to do this; however, we must ensure that our modeling structure would not cause interference by allowing actions that should be performed simultaneously to preempt one another. To ensure this, the operational classes follow a fundamental structure that we refer to as <sup>b</sup>owner–manager–actor.<sup>Q</sup> This approach computationally separates the management, monitoring, and task-oriented operations of the supply chain by creating distinct objects to perform each.

The <sup>b</sup>owner<sup>Q</sup> is the object representing the place in the supply chain where tasks are occurring, such as a node. <sup>b</sup>Manager<sup>Q</sup> objects implement tasks, usually policy-related, that the owner must continuously perform, such as constantly checking a queue for orders. When a manager determines that an action needs to be performed, an <sup>b</sup>actor<sup>Q</sup> object is created to perform the action. Thus, to prevent preempting a manager’s monitoring activities, <sup>b</sup>actor<sup>Q</sup> objects are created as needed to handle the actions. The <sup>b</sup>owner– manager–actor<sup>Q</sup> structure, coupled with the multithreading capabilities of Silkk, allows us to create simulation models that operate as in reality, with processing occurring independently and simultaneously. See Fig. 2 for a representation of the owner– manager–actor architecture.

## 5.4. SISCO Automated model mapper (SAMM)

The SISCO Automated Model Mapper (SAMM) is responsible for converting the user’s description of the supply chain and experimental conditions into a working simulation model. Model generation involves transforming the user input into an equivalent Silkk simulation model by creating instances of the appropriate SISCO Library classes. The process involves parsing the SCML file to identify the various supply chain constructs, mapping these constructs to the appropriate classes in the SISCO Library, and initializing these constructs.

![](/api/attachments/FD6FS55Z/fulltext/images/035734553a5b1a92035230d0e7bcc35797811bdd3120963a8d4b336147c14d79.jpg)  
Fig. 2. Owner–manager–actor modeling architecture.

The SCML file stores the supply chain information in elements and attributes according to a structure defined by the SCML document type definition (DTD) and by XML conventions. By knowing the elements, attributes, and the rules of their structure, we can identify the supply chain constructs in the SCML file and then create an equivalent set of Java objects.

To process the SCML file and identify the various structures within it, we utilize an XML parser to read the SCML document serially. The XML parser executes event procedures when it encounters certain general structures within an XML file.

The SAX API (Simple API for XML Application Programmer Interface) provides an efficient manner for processing XML-based files in a sequential, onepass fashion. The SAX parser reads through the XML file sequentially and triggers events when certain structures, such as the start of an element, are identified [12]. Event procedures contain code that performs the desired information processing as the structures of interest are identified. The process of reading the SCML file and creating instances of the appropriate SISCO Library classes is well-suited for a SAX parsing procedure. We must identify structures of interest, perform tasks, and then move on to the next piece of the supply chain.

When the parser identifies the beginning of a supply chain construct, it creates an object based on the corresponding SISCO Library class and begins to complete the details with the information that follows in the SCML file. When the parser identifies the end of a construct’s description, the object is placed in an array with similar objects for future access, it is initialized if necessary, and the parser continues on to the next supply chain construct in the SCML file.

The initialization process varies, based on the type of object. Non-operational objects, such as components, actions, and policies, have a simple initialization that includes creation of arrays or other organizational aids to make access to the information easier. On the other hand, the initialization of nodes and arcs is extensive. The initialization of a node or arc creates the appropriate Manager and Demand Generator objects, as well as all the necessary Silkk resources, queues, and state and statistical tracking variables. The initialization of a node or an arc object begins a hierarchical initialization that results in the creation of all necessary Silkk components, Java objects, and their associated routines.

The parsing procedure contained in SAMM ensures that the various simulation entities are initialized in the correct order, as laid out hierarchically in the SCML file. Therefore, an element is never initialized before any of its sub-elements, and an entity is never started before all the elements it contains are initialized. When the SCML file has been processed, the entire supply chain is now represented as a set of Java and Silkk simulation objects that are ready to execute.

## 6. Model execution and output

The SAMM maps the contents of the SCML file to a Silkk simulation model. After model generation, the SISCO Engine reads the experimental information, such as the number of replications, from the EXP file. Then the SISCO Engine, particularly the simulation management routines, the Silkk system, and a Java compiler combine to begin execution of the model. The model sits in a state of suspended animation because the simulation clock is not advancing, but held at time 0.0 until the user starts the simulation run. The user starts the simulation by clicking the <sup>b</sup>run<sup>Q</sup> button in the control console dialog that appears when model generation is finished.

The results of a SISCO simulation run are contained in three files: a summary text file, a replications file, and a time series file. The summary file contains performance characteristics over all replications for the system as well as each node and arc and includes both observational data (e.g., average order cycle time) and time-weighted characteristics (e.g., average number of orders waiting to be processed). In addition to total supply chain costs, the following are collected for each node:

<sup>!</sup> time orders spent in each of the <sup>b</sup>action<sup>Q</sup> queues,

<sup>!</sup> length of the queues,

<sup>!</sup> time spent performing each action,

<sup>!</sup> utilization of the action resources,

<sup>!</sup> costs incurred for each of the actions,

<sup>!</sup> inventory and shortage levels,

<sup>!</sup> inventory and shortage costs,

<sup>!</sup> inter-order times,

<sup>!</sup> order lead times,

<sup>!</sup> order sizes and variances,

<sup>!</sup> lead-time demand,

<sup>!</sup> forecasts of demand and lead time,

<sup>!</sup> service levels and other related information.

The following data are collected for each arc in the supply chain:

<sup>!</sup> the time that orders spend in the transport queue,

<sup>!</sup> the length of the queue,

<sup>!</sup> the time spent in transit,

<sup>!</sup> the utilization of the transportation resources and the associated costs.

The replication file contains the mean performance value for each node or arc over all replications for a set of chosen metrics. The replication data are useful for further statistical analysis. The time series file contains order amounts, inventory levels, forecasts, and other characteristics and consists of a complete set of values for one replication of the simulation.

## 7. Analysis and discussion

## 7.1. Advantages

SISCO offers a number of advantages over current supply chain simulators. We discuss these advantages according to model storage, architecture, ease of use, model depth, and output.

## 7.1.1. Model storage

The difference between SISCO and previous simulators is the method of storing the model. Whereas others store the model, we store the supply chain description and generate the simulation model in passing when running the simulation. We chose to develop a generalized, methodology-independent, XML-based format we call SCML, a storage method offering a number of advantages.

Using the SCML format allows users to create supply chain descriptions without attending to the modeling issues. This allows for more accurate descriptions and opens the door to utilizing several modeling styles from the same description. The SCML format is designed to be a general, quantitative modeling-oriented supply chain description format. Using this format encourages problem exchange and makes it easier to develop supply chain analysis <sup>b</sup>toolboxes<sup>Q</sup> that employ several methodologies, but utilize a common problem description.

Another general supply chain description format is the SCOR model, developed by the Supply Chain Council. SCOR’s representation of supply chain processes takes on the form of <sup>b</sup>plan, source, make, and deliver<sup>Q</sup> [15]. This format is simple to grasp, but may leave out actions and issues we wish to account for in a supply chain simulation model. SCOR was designed for process documentation and benchmarking, not for quantitative modeling, and thus does not contain detailed data and descriptions. SCOR is not a quantitative modeling format, nor is it an openstandards electronic document type, and although others have tried to adapt the SCOR model to simulation model storage, we did not deem it appropriate for storage of information or quantitative model building. As a result, we built SCML from the ground up as a tool to store supply chain information to support quantitative modeling.

Finally, the open standards of SCML allow other developers to utilize this format for their supply chain modeling and analysis. To assist in this, we have developed the VSCE, parsing routines, and userdefined data types in Microsoft Visual Basic 6, as well as class libraries and parsing routines for Java and Visual Basic .NET programming environments.

## 7.1.2. System architecture

Several aspects of SISCO’s architecture make it more suitable for supply chain simulation. Many current simulators are built from standard, general purpose simulation tools, which, while powerful and refined, lack some characteristics that are important to supply chain simulation. To best represent the operations of a supply chain with simulation, an objectoriented, multi-threaded, agent-style model must be built. Many other simulators claim to be <sup>d</sup>objectoriented,<sup>T</sup> but in most cases the term is thrown loosely to refer to reusable supply chain constructs. What is desired is an object-based model where each participant is represented by a separate object operating in accordance to its logic and communicating with other objects. Our use of Silkk, coupled with our Owner– Manager–Actor modeling structure, allows this.

Silkk provides extra benefits, such as removing a layer of complexity in the system by permitting the design of SISCO with a standard programming language, into which the Silkk classes and capabilities can be integrated. Thus, we do not have to work within, around, or add to a proprietary simulation tool. We use Java and make use of Silkk simulation classes to provide simulation functionality to the components we construct, which permits greater extensibility, since extensions to SISCO will be Java procedures and can make use of all the capabilities of that language. At the same time, it provides for easier integration of the extensions, because we only need to interface them with the Java-based SISCO application, not with a third-party tool.

The modular structure of SISCO is an advantage. The VSCE may be used within other systems that wish to include the SCML creation capability, or if the SISCO user desires a different SCML editor, another editor may be substituted for the VSCE. Because they are separate modules, VSCE or the SISCO Engine can be more easily integrated within a larger framework to form a supply chain analysis toolbox or suite of modeling tools. The Java-basis of the SISCO Engine and the modular structure of the system beckon the prospect of distributed processing, with the front-end (VSCE) and processing (SISCO Engine) running on different machines, with a Webbased connection.

## 7.1.3. Ease of use

The GUI-based VSCE allows the user to define the supply chain topology in a drag-and-drop fashion, with further details specified through a series of dialog boxes. Though the GUI-driven environment is not novel, the focus on a supply chain description is. SISCO makes the model-building process easier by allowing users to focus on the supply chain information. By relieving users from modeling tasks, we encourage them to create better, more accurate supply chain descriptions that would project the actual supply chain.

## 7.1.4. Model depth

SISCO provides extensive advantages with regard to model depth. The order life cycle, which is the modeling paradigm of SISCO, allows for a more detailed representation of all actions that occur in a supply chain, from order inception to fulfillment and finally delivery. This paradigm is more detailed than those that focus on <sup>b</sup>blocks<sup>Q</sup> or supply chain locations. We allow full specification of supply chain arcs, whereas other simulators model them as gaps between various locations.

SISCO allows practically any action that occurs in the supply chain to be represented stochastically. It is not just demands that are variable. Yields, transport times, processing times, costs, and exchange rates may be variable as well. Simulation modeling strives to allow analysts to view a system dynamically, so it makes sense that a supply chain simulator should allow users to define in stochastic terms as many aspects of the supply chain as they wish.

## 7.1.5. Output

Due to its architecture and modeling depth, SISCO can report information that other simulators cannot. We worked to create output for both non-technical as well as analytical users. Current simulators, which are based on general simulation languages, generate summary reports. SISCO was designed with the recognition that more than summaries are required.

## 7.2. Disadvantages

Not using a full-fledged simulation environment has disadvantages. These simulation environments generally provide automatic animation capabilities, which SISCO currently lacks. Also, simulation environments may provide built-in control for batch runs or scenario management facilities, which Silkk (and SISCO) also lacks. Additionally, some simulation environments include simulation-optimization algorithms, which SISCO does not have.

The use of the supply chain descriptions in SCML format, instead of model files, has some shortcomings. For very simple supply chains, the process of describing the supply chain may be more timeconsuming than describing the model that one would like to build. But for more complex systems this disadvantage disappears. Also, XML-based file formats are <sup>b</sup>dual-tag<sup>Q</sup> and can result in larger file sizes than some more succinct format. Since the files are ASCII text, which is very compressible (10 to 1 compression is not uncommon), we do not view this as a major concern.

Related to the use of supply chain descriptions is the <sup>b</sup>black box<sup>Q</sup> issue and the misperceptions that may result. Novices could develop simulation models without understanding the underlying concepts, because SISCO removes the user from the actual model building.

## 8. Conclusions and extensions

Supply chain simulators have progressed greatly since their inception ten years ago, but there is still room for further advancement. By addressing aspects of model storage, system architecture, ease of use, model depth, and output, we show that SISCO can improve the current state of supply chain simulation and modeling. SISCO incrementally improves supply chain simulation effectiveness by creating agent-style, object-oriented models, by improving the ease of use, and by producing a greater variety of output than current simulators. SISCO also incorporates some fundamentally new ideas, the foremost being the storage of a supply chain description in an open storage format. Coupled with a method to generate the simulation model from the description, this creates a new type of simulation system. In SISCO, we approach the simulation modeling of the supply chain from a new perspective, that of the order life cycle.

The future of modeling for supply chain research and decision support lies in supply chain analysis workbenches or toolkits that incorporate several analytical toolkits of different types, and many of the ideas incorporated into SISCO are hence applicable. The open, general supply chain description, automated model generation, modular structure, and object-oriented design are all applicable to general supply chain analysis workbenches.

To extend SISCO, we plan to develop a Java version of the Visual Supply Chain Editor (VSCE) and create a Web-distributed implementation of the system. We also plan to develop a framework for a general supply chain modeling workbench that uses SCML as a standard storage format and allows various tools (SISCO being one) to attach themselves to that framework.

## Acknowledgments

We thank the Center for Supply Chain Research at Penn State University for partial funding of this project. We also thank ThreadTec for permission to use Silkk.

## References

[1] S. Bagchi, S. Buckley, M. Ettl, G. Lin, Experience using the IBM supply chain simulator, Proceedings of the 1998 Winter Simulation Conference, 1998.

[2] S. Biswas, Y. Narahari, Object oriented modeling and decision support for supply chains, European Journal of Operational Research 153 (2004) 704– 726.

[3] D. Chatfield, SISCO and SCML—Software tools for supply chain simulation modeling and information sharing. Unpub-

lished Ph.D. Dissertation, Department of Management Science and Information Systems, Penn State University, University Park, PA, 2001.

[4] D. Chatfield, J. Kim, T. Harrison, J. Hayya, Order flow in serial supply chains, Working Paper, Department of Supply Chain and Information Systems, Penn State University, University Park, PA, 2002.

[5] D. Chatfield, T. Harrison, J. Hayya, The supply chain modeling language (SCML), Working Paper, Department of Supply Chain and Information Systems, Penn State University, University Park, PA, 2003, Also available at http://filebox. vt.edu/users/dchatfie/papers/scml<sup>\_</sup>workingpaper.pdf [As of September, 27, 2004].

[6] D. Chatfield, T. Harrison, J. Hayya, SISCO: the simulator for integrated supply chain operations, Working Paper, Department of Supply Chain and Information Systems, Penn State University, University Park, PA, 2003, Also available at http://filebox.vt.edu/users/dchatfie/papers/sisco<sup>\_</sup>workingpaper. pdf [As of September 27, 2004].

[7] R. Ganeshan, Analytical essays in supply chain management, Unpublished Doctoral Dissertation, Department of Management Science and Information Systems, The Smeal College of Business Administration, The Pennsylvania State University, 1997.

[8] GenSym Corporation, e-SCOR Overview, 2004, Available at http://www.gensym.com/?p=g2\_e-SCOR\_forsupplychain.

[9] K. Healy, R. Kilgore, Introduction to Silkk. ThreadTec Incorporated, 1998, Available online http://www.threadtec.com.

[10] J. Herrmann, E. Lin, G. Pundoor, Supply chain simulation modeling using the supply chain operations reference model, Proceedings of the ASME 2003 Design Engineering Technical Conference, September 2–6, 2003, Chicago, Illinois, USA, 2003.

[11] LlamaSoft Incorporated, Supply Chain Guru, 2004, Available at http://www.llamasoft.com/Software/index.htm [As of September 8, 2004].

[12] P. Mosenhi, An introduction to XML for Java programmers, Java Pro, vol. 3, no. 3, Fawcette Technical Publications, Palo Alto, CA, 1999, pp. 48 – 52.

[13] M. Rossetti, H. Chan, A prototype object-oriented supply chain simulation framework, in: S. Chick, P.J. Sanchez, D. Ferrin, D.J. Morrice (Eds.), Proceedings of the 2003 Winter Simulation Conference, Institute of Electrical and Electronics Engineers, Piscataway, NJ, 2003, pp. 1612– 1620.

[14] Simulation Dynamics Incorporated, Supply Chain Builder, 2004, Available at http://www.simulationdynamics.com product/modeling<sup>\_</sup>tools/sc<sup>\_</sup>builder.asp [As of September 8, 2004].

[15] Supply Chain Council, Supply chain operations reference model overview version 6.1, 2004, At http://www.supply-chain. org/SCOR/SCOR<sup>\_</sup>Overview<sup>\_</sup>6.1.pdf [As of September 8, 2004].

[16] J. Swaminathan, Haas School of Business, University of California at Berkeley, 1998, Personal Communication.

[17] J. Swaminathan, C. An, T. Levas, R. Petrakian, B. Tuskie, A library of simulation software objects for supply chain analysis, Presentation at the Fall 1995 Conference of the

Institute for Operations Research and the Management Sciences, New Orleans, LA, 1995.

[18] J.M. Swaminathan, S.F. Smith, N.M. Sadeh, Modeling supplychain dynamics: a multi-agent approach, Decision Sciences 29 (3) (1998) 607– 632.

[19] J. Zhang, I. Hunt, J. Browne, The development of an extended enterprise supply chain management simulator, Computer Integrated Manufacturing Research Unit, The National University of Ireland, Galway. Proceedings of the Advanced Summer Institute Conference, 1998 (May).

![](/api/attachments/FD6FS55Z/fulltext/images/37ee65586d0b611bba6af0abdf6ec70f8bc70e303d65b3bee656a1c3e73da254.jpg)

Technology at Virginia Tech in Blacksburg, VA. He received his Ph.D. in Management Science from Penn State University, an M.S. in Management Information Systems and an MBA, also from Penn State University. He holds a B.S. in Management Systems from Rensselaer Polytechnic Institute. His research interests include supply chain design and operation, simulation modeling of production and service systems, the application of meta-heuristics,

and Visual Basic software development. He is a member of the Decision Sciences Institute (DSI), the Institute for Operations Research and the Management Sciences (INFORMS), and the Production and Operations Management Society (POMS).

## Terry P. Harrison is Professor of Supply Chain and Information

![](/api/attachments/FD6FS55Z/fulltext/images/2de876a642f87b80a201e66d0a90059a5aa187c2a1c1e6cecc2734b4f6449d1c.jpg)

Systems at Penn State University. He holds a B.S. in Forest Management from Penn State, and an M.S. and Ph.D. in Management Science from the University of Tennessee. His research and teaching interests are focused on models and quantitative methods for managing supply chains. He is a member of the Institute for Operations Research and the Management Sciences (INFORMS), the Decision Sciences Institute (DSI), and the Production and Oper-

ations Management Society (POMS). He is a former Editor-in-Chief of Interfaces.

Jack C. Hayya is Professor Emeritus of Management Science at

![](/api/attachments/FD6FS55Z/fulltext/images/7759329e6a569ed6e70c7976fe41451afcba2fbc7952b9053d3d0d5174d8aadb.jpg)

Penn State University. He holds a B.S. in Civil Engineering from the University of Illinois, an M.S. in Business Administration from California StateNorthridge, and a Ph.D. in Business Administration from UCLA. His research interests lie in the areas of production and inventory management, applied statistics, and supply chain management. He has been an Associate Editor of the Decision Sciences journal (1984 – 1995) and Area Editor (1990 –

2000) for Production and Operations Management. He is a Fellow of the Decision Sciences Institute.
