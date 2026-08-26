---
otero_id: 8522
otero_key: "JG33DN7U"
title: "Agent-enabled service-oriented decision support systems"
authors: "Ching-Shen James Dong; Ananth Srinivasan"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.05.047"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Agent-enabled service-oriented decision support systems

Ching-Shen James Dong, Ananth Srinivasan ⁎

The University of Auckland Business School, OGG Building, 12 Grafton Road, Private Bag 92019, Auckland, New Zealand

a r t i c l e i n f o

Available online 30 May 2012

Keywords: Decision making processes Service delivery Decision support systems Services Software agents

## a b s t r a c t

The design of Decision Support Systems have recently emphasized web enablement as the next step in design improvements for this class of applications. We argue that these approaches fail to address the key notion of adaptability in the support for decision makers. Instead of focusing exclusively on automation in decision making, we believe it is also necessary to pay attention to the interplay between decision makers and organizational processes. The service oriented view of organizations recognizes the need to accommodate the changing reality of organizational dynamics. For example, the service science approach focuses on interactions between service providers, their clients, and consumers as important interacting components of a service system. Current approaches to DSS design are constrained in terms of their ability to adapt to changes in user requirements and to provide support for the evolution of systems. This situation worsens when resources are distributed at different locations across organizations, decision making processes are required to be integrated at different points in time, and when collaboration is needed among decision makers. However, this typically characterizes the needs of collaborative decision making in networked organizations as exempli<sup>fi</sup>ed by systems used for supply chain management. To address these problems we leverage the power of services for designing a framework that explicitly recognizes the need for design based on service delivery. We develop an agent-enabled service-oriented architecture to realize the proposed framework with service and agent paradigms. The architecture is re<sup>fi</sup>ned and validated with an implementation in the supply chain context.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Organizations, large and small, local and global increasingly de<sup>fi</sup>ne their primary purpose as ‘service’ rather than products [10,17]. In both global and local contexts, for <sup>fi</sup>rms of all sizes, the delivery of service increasingly relies upon both intra- and inter-organizational connectivity that includes social and technical connections, which are effective and ef<sup>fi</sup>cient. Systems to support organizational decision making has been discussed in the literature for several years. Two important trends motivate us to rethink fundamental design issues pertaining to implementing such systems. First is the development of tools and methodologies that take a service oriented view of design. Business processes need to be supported by clearly acknowledging the need for a collaborative environment amongst organizational units to deliver solutions. A useful way to address this issue is to build the notion of service delivery directly into design implementations. Second is the recognition at an organizational level that service interactions are key functions of successful modern organizations — the ubiquity of supply chains in organizations being a good case in point. We discuss these issues and link them to the objectives of our work.

Current research perceives service as the foundation for all economic exchange [40,41]. Markets and corporations have shifted toward a service-oriented environment, which raises the need for new approaches towards service research. Palmisano [33], Maglio and Spohrer [29], Spohrer et al. [37] and others have called for a “science of service”, aiming to provide new theories and practical advice for service <sup>fi</sup>rms. The role of information technology in this process has subsequently become a research priority for service science [32].

Every service system relies on the interaction and sharing of information with customers during service engagements. Customer involvement is generally seen as a prerequisite for successful service engagements and value co-creation. Driven by technological changes, service engagements have shifted into virtual realms, resulting in so called technology-enabled value co-creation. Traditional approaches to studying the services theme have differentiated tangible products from intangible services in order to clearly articulate the point of differentiation for items with economic value and their interaction with markets [27]. The emphasis of this work is on examining a particular characterization of service delivery — one that leverages the use of IT to achieve this objective. The particular issues that we attempt to look at revolve around a better understanding of business process de<sup>fi</sup>nitions, distributed project compositions, and coordination amongst project teams.

The phenomenon of service systems as enablers of business innovation has been discussed by various researchers. Conceptually, we can envision three components of the service framework. The <sup>fi</sup>rst is a service provider that could be a combination of individuals, organizations, and technologies. The second is a service client that could be a combination of individuals and organizations. The third is the object or target of the service — the entity that will be transformed by the application of the service. This could be a combination of people, organizations, processes, technologies, information, etc. Fig. 1 below (adapted from the work of [29]) highlights the key aspects of thinking about service systems and the issues that arise when we want to study such entities.

Such a framework enables us to de<sup>fi</sup>ne a set of interesting research issues around the interaction between the components of the framework, including an emphasis on intra- and inter-organizational connectivity.

Organizational decision making is a dynamic and complex process. Decision making requirements are constantly changing over time and vary from person to person. They are made at different levels of an organization, and involve many people from different locations with different business orientations towards the decision making process [9]. This variation in terms of organizational level and orientation makes collaboration among the decision makers vital. The decision making process, whether it be structured, semi structured or unstructured, requires data and information from a multiplicity of sources. Decision makers need to quickly get to the essence of the underlying data/information by going through a gathering, accessing, integrating, transforming, discovering and learning cycle. The application of this cycle gradually <sup>fi</sup>ne tunes the decision scope either by continuous inputs over a period of time or through the decision maker's insightful inputs at speci<sup>fi</sup>c points in the decision making process.

Systems to support decision makers in the decision making process have been formally recognized as a separate class of systems since the 1970s. Decision support systems (DSS) [6,36], have been formally de<sup>fi</sup>ned as interactive computer based systems [1,4,38] that support decision making processes for decision makers to solve semi-structured and/or unstructured problems [19]. In the current organizational context, such systems need to be adaptive in order to obtain the various resources needed in the decision making process [2] and to cope with changing decision making requirements for different people. Adaptive systems must have the capability to support users at different locations to access various resources across networks to enable them to participate in synchronous or asynchronous decision making processes. Decision oriented systems must also provide iterative methods such as what-if analysis to help users <sup>fi</sup>ne-tune their decision making. They must be able to adapt to changes in the external, internal, and system environments, as well as in the users themselves. Furthermore, these systems should enable the <sup>fl</sup>exible manipulation of components and processes. For example, there should be no restrictions imposed by the system on users for the selection/integration of decision making components, nor should there be restrictions on acquiring the necessary resources from heterogeneous distributed systems. Equally, the architecture should allow the addition of new components into the system at run time.

The problem that we address in this paper therefore can be captured as follows. We propose that current organizational realities necessitate an extension of conventional thinking about decision support systems along multiple dimensions. First, collaborative decision making among organizations requires effective exchange of information among them. Second, such exchange can be usefully facilitated through proper systems design that views information exchange as the provision of appropriate services. Third, systems must be adaptive to accommodate the needs of dynamic and heterogeneous organizational entities. These problems and the issues that arise from them motivate us to propose a high level service oriented decision support conceptual framework. In this paper, we outline the development of an agent-enabled framework and architecture to support the service oriented requirements of modern collaborative organizations. We adopt a design science paradigm [20] to develop a framework and implement a prototype that emphasizes service delivery as a key guiding principle for DSS development.

## 2. Design issues

The recent literature on developments in DSS design recognizes the need for building on early design proposals to accommodate a new technical landscape. For example, Bhargava, Power, and Sun [5] review DSS design developments that are web enabled and note that while the use of the web as an interface has been embraced, more complex designs are still lacking. The need for supporting distributed decision making is a major development in DSS design. They also note that discussions about design architectures and guidelines are scarce in the academic literature on DSS design. A discussion about design architecture by Zhang and Goddard [43] outlines a layered software architecture for building web based distributed DSS with a data oriented emphasis. Several authors have embraced the web services idea to propose different approaches to DSS design. Madhusudan and Uttamsingh [28] advocate a largely automated process for web service composition as an approach to overcome human intervention in decision processes. The automation of decision processes is also offered as a design principle in conjunction with the application semantic web based designs. Bose and Sugumaran [7] propose that semantic web based designs would be a generic approach to building intelligence into automated decision making. The semantic web based design approach is also proposed by Deokar and El-Gayar [13,14] for building intelligence into automated decision processes as well as exploiting the web services approach to design. These representative design approaches emphasize distributed decision making, intelligence, and automation as key aspects of DSS design while mainly relying on the web as the supporting infrastructure. Complex decision aiding systems represent only a small fraction of the software systems used in a business organization. The availability of timely information from a variety of organizational system sources is critical for decision makers to make the best decision at the right time. One of the key requirements of DSS design should be the integration of multiple enterprise systems (that are potentially heterogeneous) for supporting decision making. Very often decision makers must gather data/information/ models/knowledge from various systems within and outside their organization in an ad-hoc manner. This inef<sup>fi</sup>cient retrieval process adversely affects the overall quality of the decision making process and subsequent decisions. We believe that the key to successful DSS design lies in the ability of these systems to adapt appropriately to a dynamic decision making environment. Explicitly addressing this notion of adaptive design is central to what we propose.

![](/api/attachments/JG33DN7U/fulltext/images/eda402a69d3367fd0f06d0ab32f2ee2fc4a0969177e64388d42b93105ab63a93.jpg)  
Fig. 1. Characterizing service systems. Adapted from [29].

The problems and issues discussed above can be grouped into four dimensions: resource, location, lifecycle and time. The resource dimension refers to components and/or services used to build DSS such as models, data, solvers and visualizations. The location dimension refers to the distribution of resources, such as components, among heterogeneous systems across networks. The lifecycle dimension deals with the sequence of procedures or activities used to support the entire decision making process. The time dimension refers to the fact that decisions are interwoven over time sequentially and laterally. The integration of these dimensions in an appropriate manner is the essence of what we refer to as the adaptive nature of decision oriented systems. For current systems to be successful, building recognition of the need for adaptive behavior into the design is an essential step.

Although many frameworks and architectures have been proposed by researchers very few of these address all four dimensions equally well. For an adaptive system these problems and issues must be addressed and resolved in an integrated and holistic fashion. Opportunities can be found by redesigning frameworks and architectures with the reuse of existing and emerging technologies. Our focus on a design approach is to build our proposal around these four requisite fundamental dimensions. In our approach, integration of DSS component services is fully controlled by users based on their needs and is adaptable to dynamic decision making processes. This support is very dif<sup>fi</sup>cult, if not impossible, to achieve by the web services architectures using service buses. User collaboration is achieved by moving DSS component services dynamically to where and when they are needed. This is a more <sup>fl</sup>exible approach to dealing with the location dimension than a purely web based approach that generally relies on <sup>fi</sup>xed URLs. The basic notion of intelligence is incorporated as a DSS component service to be managed and utilized by users like any other service in the design framework. Our emphasis on the intelligence issue is to provide maximal support for the lifecycle dimension of our framework. As opposed to complete automation for process execution, we believe that the opportunity for the user to provide guidance for the execution is crucial in complex decision making environments.

## 3. Decision support systems (DSS)

The origins of decision aiding systems lie in the literature pertaining to DSS design and development. DSS are interactive computer-based information systems, which help decision makers utilize data, models, solvers, visualization and the user interface to solve structured, semistructured or unstructured problems. They are built by different levels of system developers to support different levels of decision maker users. DSS that are used to support decision makers can be built from assembling components or through systems called DSS generators (DSSG). Typical DSS building blocks (components) are data, models, solvers, user interface and visualization. Generators assist in assembling components appropriately to realize speci<sup>fi</sup>c implementations that address a particular organizational problem — a speci<sup>fi</sup>c DSS (SDSS). We de<sup>fi</sup>ne a DSS scenario as a snapshot of a decision making process at a speci<sup>fi</sup>c point in time. The relationship between DSS components, DSSG, SDSS and scenarios is depicted in Fig. 2.

To address the need for systems to be adaptive, end user development as a methodology emerged (e.g. [39]). In the context of DSS, end-user developers are decision makers with superior domain knowledge and some system knowledge (Fig. 3). They replace DSS builders to develop DSS for themselves or other end-users.

There are tradeoffs between SDSS and DSS. We can use versatility (i.e. the range of domains and types of decision making problems) and autonomy (i.e. the degree of freedom from human direction) to explain the tradeoffs. SDSS are less versatile, owing to their greater reliance on domain knowledge speci<sup>fi</sup>c to a more focused task. However, they provide more autonomy through reduced human intervention. Designed to work across broader domains, DSS are more versatile and generally have a wider range of techniques but they provide less autonomy because of their complex functionality.

## 3.1. Implementing DSS using services and software agents

Our approach to DSS design is to view business process requirements in terms of service exchange which are enabled through the deployment of corresponding software agents that implement the provision of such services. The bene<sup>fi</sup>ts of generalized approaches of complex agent based designs are well laid out by Juan, Sterling, and Winikoff [21]. Silva and Lucina [12] further explore modeling issues when multiple agents need to be built into a single design product. Nissen and Sengupta [31] present results from an experimental study where they assess the use of agents in a supply chain context. Agent based implementation seems to offer a bene<sup>fi</sup>cial design approach that addresses the four underlying dimensions that are necessary for systems to be adaptive. We de<sup>fi</sup>ne services as an abstraction service layered between the business process and software application (component) service layers. Services and service oriented architectures support business processes with <sup>fl</sup>exibility and agility for integration [15]. In the context of DSS, services are de<sup>fi</sup>ned by interfaces, bound by system components and used to support decision making processes and such services are delivered by software agents. In this paper, we focus on the use of these software agents to deliver requisite services necessary of decision making.

Franklin and Graesser [16] provide several de<sup>fi</sup>nitions for agents used in research. A software agent is a computer program but the term ‘agent’ and its classi<sup>fi</sup>cation have different meanings depending on what is central to the agent system(s). We de<sup>fi</sup>ne a software agent (simply referred to as ‘agent’) as a special computer program that is designed with special function(s) to execute prede<sup>fi</sup>ned task(s) for its owner. The key function of software agents is to support collaboration through communication in an agent community [42]. Software agents, as discussed in this paper can conceivably be stationary or mobile with respect to the location dimension while playing the role of intelligent agents [3,8,11,22].

![](/api/attachments/JG33DN7U/fulltext/images/eddf910056b63c9e3bba0745c4c48ef6f28ff3650cf34c4126526cf26e4e0216.jpg)  
Fig. 2. Decision support systems.

![](/api/attachments/JG33DN7U/fulltext/images/d6c48aeec125c97a5fd11c3fa23ef50179a9e71a7a8f0e1198d67e63f4075a2b.jpg)  
Fig. 3. The role of end-user developers and DSS.

## 4. Service-oriented decision support systems: a conceptual framework

The design of these systems needs to address the four key underlying dimensions discussed earlier: resource, location, lifecycle and time. To aid our discussions in this context we de<sup>fi</sup>ne a service oriented system as an interactive computerized system that uses services to <sup>fl</sup>exibly integrate components between service providers and service clients across a network to help decision makers solve semi-structured and unstructured problems. To support this emphasis on systems being adaptive, we propose an abstract service-oriented framework (Fig. 4) that consists of services to support resource, location, lifecycle, time and core DSS functions.

The support for location, resource, lifecycle and time dimensions in our abstract service-oriented framework is summarized as follows:

Location — resources are made available to decision support systems or the users at different locations. Location can refer to computers at any node across the networks and organizations. Mobility can be used to describe the ability of the resources to move, or not move, across the networks. In this framework, the decision support systems can be constructed from components at local and/or remote locations.

Resource — components such as data, models, solvers, component interfaces, etc., are the resources in decision support systems. The design of these building blocks can be simple, or complex, to meet the requirements for adaptability. The resources can be used by a single user or shared among multiple users. Resource encompasses the availability, persistency and independence of the components.

Lifecycle — the process in the decision support system lifecycle can be performed in two stages: DSS–SDSS lifecycle — this is the process of assembling components into speci<sup>fi</sup>c decision support systems (SDSS), which is done by the DSS builders. The speci<sup>fi</sup>c DSS generated can be executed in either the same design or a separate execution environment. SDSS can be saved as scenarios during decision making.

![](/api/attachments/JG33DN7U/fulltext/images/982a6ca1107a837a0eb993434868421e9cd9ea0b1f4882cb54a84023550fccd5.jpg)  
Fig. 4. An abstract service-oriented decision support system framework.

Model lifecycle — this is the process to support decision making for end-users. Decision support processes do such things as create models, query data, instantiate models [18,26,35], apply solvers to models and integrate models to provide informed knowledge to the decision makers; they can also save and terminate models.

Time — multiple decision making processes can occur at the same time or at different points in time, and by the same or different decision makers. For example, decision making processes A and B may need to execute in parallel for ef<sup>fi</sup>ciency reasons; decision making processes C and D may need to execute in sequential order (use output as input) for collaboration reasons.

The core of the framework lies in the provision of services. Services in the framework can be components such as models, data, solver and visualizations or applications. The features of the services in the framework are independence, extensibility, <sup>fl</sup>exibility, mobility, visibility, collaboration, and ultimately adaptability. This high level adaptive framework is used to guide researchers to embrace the concepts of resource, location, lifecycle and time dimensions. A more detailed level of the adaptive architecture is proposed and described in the next section.

## 5. Service orientation: a system framework

The proposed service-oriented framework (Fig. 5), components are represented by component services.

The framework consists of structure, component services, fourdimension support, system support and user interface. Speci<sup>fi</sup>c decision support systems are built from component services or from the DSS. Component services and/or systems are integrated from components and composed to support decision makers to solve complex problems. Component services such as data, models, solvers, visualization and scenarios are collected and integrated to support users (system builders and decision makers). Component services are used to build generators at design time by builders. These generators in turn are used to generate task speci<sup>fi</sup>c systems for end users. Component services, generators and general purpose systems are distributed across intra, extra and inter layers to provide support from the perspective of resource, location, lifecycle and time dimensions.

The integration of independent component services in a distributed environment provides the key foundation for supporting resource, location, lifecycle and time dimensions in the abstract service-oriented framework. The distributed structure in the framework is discussed in Section 5.1. The decision support systems are assembled with component services and integrated through service binding. Component service binding is discussed in Section 5.2. Model is the central component service and its lifecycle is vital in design; model lifecycle and model integration are discussed in Sections 5.3 and 5.4.

![](/api/attachments/JG33DN7U/fulltext/images/bd0fdf6362f8e0b2e25b77f5337551c889bc731ff8a40a62491c60b0dbff2dfd.jpg)  
Fig. 5. A service-oriented DSS system framework

## 5.1. Distributed structure

Distributed problem solving is necessary to address physically distributed problems across different locations or across many servers. The component services, generators, SDSS and scenarios can be distributed across intra-layers for departments within organizations, extra-layers for business partners between organizations and interlayers for the general public.

To support resource and location dimensions, component services can be collected from many locations at different layers and integrated into one generator. The SDSS generated from the generator can be saved as scenarios. To support the lifecycle dimension, full model lifecycle from creation through termination is supported. Scenarios can be used to re<sup>fi</sup>ne SDSS and in turn to re<sup>fi</sup>ne the generator itself. To support the time dimension, component services can be shared between users for performing sequential or parallel decision making across time. The integration of component services is achieved through binding, a vital process supported in this framework.

## 5.2. Component service binding

In order to make component services work together, binding is required. Binding is a process of linking independent component services (Fig. 6) to perform an integration of service functions. Binding also refers to the passing of data values between component services.

It is required for maintaining the proper state of participating component services, such as model-data binding for model instantiation, and model-solver binding for model execution. Performing binding (either manual or automatic) is vital since it will affect the <sup>fl</sup>exibility and extensibility of the component services. If the required type and size of data are speci<sup>fi</sup>c in binding, the binding is tightly coupled; otherwise it is loosely coupled. Loosely coupled binding is preferred for generators. In the binding process, the model is the central component service in the distributed structure. In the context of decision support systems, <sup>fl</sup>exible model management is vital to support reuse, sharing, and integration [30]; this framework uses the model lifecycle to realize model management.

## 5.3. Model lifecycle

At different stages of supporting the decision making process, models exist in different forms in their lifecycle, from their creation to their termination. For a service-oriented system, we propose that the phases of the full model lifecycle are creation, instantiation, realization, execution, relocation, sharing, integration, modi<sup>fi</sup>cation, what-if analysis, storage, retrieval, cloning and termination. There are also some instances where the full model lifecycle is not required to support decision making. Different model phases used at various stages of decision making processes, to support decision makers, are managed by DSS model management.

![](/api/attachments/JG33DN7U/fulltext/images/b710dcacb287306ae837c51edcc7d6cc378ff935b04f311afa5d3dee3e239eb6.jpg)  
Fig. 6. Binding between DSS component services.

## 5.4. Multiple model usage

An important aspect of the use of models that has been discussed in the literature is the issue of multiple model deployment whereby one model needs to work with others for supporting decision making (e.g. see [30] and [23]). The basic assumption of using multiple components to solve one problem is that a complex problem can be decomposed into several smaller ones. The combination of solutions to the smaller problems can provide a complete solution to the original problem. The speci<sup>fi</sup>c variations that we consider are:

Aggregation — several models are grouped to one model. The aggregation produces an ‘is part of’ relationship; for example, Model A is the aggregation of Models B and C; Model B is part of Model A; Model C is also a part of Model A.

Classi<sup>fi</sup>cation — several models can be classi<sup>fi</sup>ed to one model. This classi<sup>fi</sup>cation produces an ‘is kind of’ relationship; for example, Models E and F are classi<sup>fi</sup>ed to Model D; Model E is a kind of Model D; Model F is also a kind of Model D.

Pipelining — pipelining means that the output of one model is used as the input of another model or models. It is a way of combining various components such as data, models and solvers to solve complex problems.

Splicing — the data of one model is used by another. Note that the data of the source model is the data being processed and not the output.

New service creation — component services, whether they are data centric or model centric can be combined on the <sup>fl</sup>y to create new ad-hoc services as required.

This model lifecycle framework supports component integration to enable the con<sup>fi</sup>guration of solutions to complex problems. The architecture used to realize our proposed frameworks as discussed in the next section.

## 6. Agent-enabled service-oriented decision support: a system architecture

The architecture proposed in this section is used to realize our proposed frameworks (conceptual and system). An agent-enabled service-oriented DSS (ASDSS) architecture is a multi layered, multi faceted, components and role based architecture that bridges the gap from concept to architecture. Fig. 7 illustrates the creation of ASDSS through the integration of DSS component services distributed across networks.

Software agents are used as component services, decision support systems and/or scenarios used by decision makers. More speci<sup>fi</sup>cally, the agents are created by performing the functions of a component through services available through service providers. Components such as models of data analytics, data from data warehouses, solvers, visualizations and scenarios are collected from service providers and integrated into decision support systems to support users by service clients. The integration of independent components in a distributed environment provides the key foundation for supporting the resource, location, lifecycle and time dimensions described in the previous section.

ASDSS are used to support users for distributed problem solving over space (across organization boundaries) and time. Distributed problem solving addresses problems that are physically distributed across different locations or across many systems. To support resource and location dimensions, the component services can be collected from many service providers at different locations by one service client. One service provider can provide services to multiple service clients. To support the lifecycle dimension, full model lifecycle from creation through termination is supported. Scenarios can be used to re<sup>fi</sup>ne ASDSS. To support the time dimension, the component services can be shared between users for performing sequential or parallel decision making across time. The integration of component services is achieved through binding, a vital process supported in this architecture.

The design concept of the architecture is to use a software agent as a service to enable <sup>fl</sup>exible integration of components to support decision making. The principal components in the main ASDSS architecture (Fig. 7) are component services and software agents. The component services represent independent objects such as data, models, solvers, visualization, scenarios, etc., and are distributed across the network. Message passing among interactive agents can be used to facilitate integration, e.g. passing the object reference in order to share component objects.

The software agents are intelligent and mobile agents. Software agents exist in, and are supported by, agent hosts located on user computers. The agents play different roles, such as data service agent, model service agent, solver service agent, scenario service agent, directory service agent, broker service agent, manager service agent, etc. The mobility of mobile agents can be used to move components across the network of an organization to facilitate the integration of various components.

Although lifecycle issues can be addressed by generators, agents enable the performance of the lifecycle process more effectively. A host is used to represent a generator; it can also be used as a place in which to store data, model and solver resources. Mobile agents move component services across the network for generators. Interactive agents pass the component object references to let generators share component services among users. Deliberative agents help the decision maker choose the right solvers and reactive agents detect changes of <sup>fi</sup>les on a computer to trigger execution of scenarios for automation.

Software agents can be distributed to computers with an organization or across multiple organizations to help decision makers solve problems in real time. Mobile agents can travel across networks to solve problems sequentially. Message passing among agents can help decision makers solve problem in a synchronous and/or asynchronous way.

To build an SDSS, component services are composed in the ASDSS. The agents provide the support for the integration of component services by moving them between computers, or by sending messages between agents. The software agent and the component service can be combined as one entity. For example, different mobile agents can be used to represent problems (i.e. models) and solvers. The problems can move to the solver or solvers and the solvers can in turn move to the problem or problems. Using mobile agents removes time and space limitations, and provides <sup>fl</sup>exibility and extensibility to the problem solving process. Some possible scenarios are: one solver service is used to solve similar problems at different locations; several solver services are moved to solve one complicated problem at one location; many solver services move to solve problems at different locations (Fig. 8).

## 6.1. Agent shell

An agent shell is a basic entity that provides fundamental functions for an agent to perform tasked services. An agent shell consists of communicator, socket connector, plug-in sockets, message controller, actions and event handler. The communicator is responsible for sending and receiving messages from other services or agents. The socket connector provides a low level communication facility, especially good for communication between heterogeneous agent systems [12,34,42]. Plug-in sockets are the access points where functional objects can be added to the agent. The message controller receives inputs and/or generates outputs. Proper actions are based on messages received from the message controller, while the event handler manages the events generated from the environment or the agents.

![](/api/attachments/JG33DN7U/fulltext/images/df1367f3e51d022b7f119155a822a615a89c71a05b87bd8301d90e0f394587c3.jpg)  
Fig. 7. An agent-enabled service-oriented DSS architecture.

## 6.2. Agent-enabled component services

The basic building blocks of decision support systems are component services. We identify some main services that are used to build systems such as data, models, solvers, visualization and scenarios. Data services are the data, information or knowledge used by other component services. Model services are used to represent the problems in the real world, and solver services to provide solutions to the models; visualization services are visual representations of components, such as graphs for data, and scenario objects are a snapshot of the SDSS at a particular point in time.

![](/api/attachments/JG33DN7U/fulltext/images/e16e26e41d5673f73cc53d4ae94b9b32119bc4f29af5b82acdc0278c5691552f.jpg)  
Fig. 8. DSS component services, DSS agents, locations and problem solving.

In the agent-enabled service-oriented architecture, component services representing components exist independently or are attached to and used by the agents. When the services are composed into a system for supporting decision making, the process of binding is required.

Component services cannot perform too many useful functions if they cannot be inter-connected. Binding is the process of connecting the component services by passing parameter values between them and can be carried out manually or automatically. The process of manual bindings can be saved and re-executed later, a process referred to as automation. In binding two component services, the less restriction the better. Typical restrictions of binding are the different data types of the parameters. Less restriction for mapping means the two component services are loosely coupled and more restriction means that they are tightly coupled. For object-to-object binding, we can use ‘type widening’ techniques in OOP to provide buffers between the data types of the mapped parameters, but the bene<sup>fi</sup>ts of using these are rather limited. Object-to-object-to-object and object-toagent-to-object binding provide better mechanisms for improving extensibility. In the object-to-object-to-object binding, extensibility can be achieved by using the re<sup>fl</sup>ection functions in OOP and/or introspection in Java Beans. In the object-to-agent-to-object, extensibility can be achieved by proper manipulation of the procedures in agent messages. A good example of implementing component binding is the pipelining of component services. Different component services such as data, models and solvers are composed to form systems for supporting decision making.

## 6.3. Agent communication

The main difference between agents and objects is that the former work together by talking (communicating) with each other and the latter work together by calling each other's methods. To process a message, a message protocol for the message format is required. To understand the contents of the message, an agreement for a common set of terms, ontology, is needed. Agent communication can be implemented by messaging and broadcasting. One agent can send messages to another and receive replies; one can broadcast messages to selected agents or all the agents on a host; an agent can subscribe to speci<sup>fi</sup>c types of messages broadcast by other agents.

In the ASDSS architecture, agents work with component services. An agent lifecycle supports the lifecycle concepts proposed in the service-oriented DSS framework (Fig. 5) and the ASDSS architecture (Fig. 7). The model lifecycle is supported through various phases in the agent lifecycle.

## 6.4. Agent lifecycle

In the ASDSS architecture, the structure of mobile agents [24] is used for the agent. Different agents are designed to perform different tasks in the ASDSS architecture. The ASDSS agents work together with DSS components, to support the distributed decision making process described in Section 4. In general, ASDSS agents have the following phases in their lifecycle: creation — agent can be created from the agent environment, instantiation — agent is instantiated with component services, cloning — agent can be reproduced with component services embedded, dispatching — agent can be dispatched from one host to another, retracting — agent can be retracted after it has been dispatched, deactivation — agent can be saved and stored in secondary storage, activation — agent can be activated from the saved agent object, and disposal — agent can be disposed of.

Components such as data, models, solvers and visualization are the building blocks of the ASDSS architecture. SDSS, built by the ASDSS, can be saved as scenarios at different points in time. The basic working unit in the ASDSS architectures is the agent host, on which agents are supported. An agent is made of an agent shell and component services, with different agent shells being designed for different component services. Agents support the ASDSS architecture to address resource, lifecycle, location and time issues.

The ASDSS architecture addresses the resource issue by using independent component services such as data, models, solvers and visualizations to build DSS, SDSS and scenarios. Component services used in the systems could be from local or remote resources. The architecture addresses the location issue by using software agents to move the distributed components to locations where decision support is needed. The architecture addresses the lifecycle issue by using an object oriented paradigm to support model and DSS–SDSS– Scenario lifecycles. The architecture addresses the time issue by using the mobility and messaging of software agents to integrate component services to support sequential and parallel decision making.

A prototypical ASDSS was implemented with software agent technology — IBM [24,25]. This implementation was used as a proof of concept for the proposed conceptual framework, system framework and architecture.

## 7. Implementation

To highlight the potential of the service-oriented framework and ASDSS architecture, the Collaborative Planning, Forecasting and Replenishment (CPFR) problem in Supply Chain Management (SCM) was employed to explore the details of components, model lifecycle, software agents, DSS, SDSS and scenarios. The implementation is used to validate the frameworks and architectures that have the ability to address the problems, issues and requirements of the resource, location, lifecycle and time dimensions. The ASDSS implementation (Fig. 9) is used for enabling the collaboration of retailer and manufacturer to exchange information/knowledge and collaborate in executing plans across organizational boundaries.

The basic infrastructure uses combined technologies of services and agents under a service oriented architecture for business collaboration between business partners. Different model service agents, data service agents, solver service agents and other service agents are deployed and move to various locations (Fig. 9) across organizational boundaries to perform the designated services. The result is to make the members of the supply chain more effective in meeting customer needs, and more ef<sup>fi</sup>cient in reducing the overall costs in the supply chain. A brief scenario can be described as below:

![](/api/attachments/JG33DN7U/fulltext/images/452b333daf607b178feddf3e7f99818ae26b8d94440c5b6557d763d50476f0bf.jpg)  
Fig. 9. The ASDSS implementation.

Step 1 The retailer chain stores use forecast model service, data service and solver service agents to produce their sales forecast based on the sales records (resource and lifecycle dimensions leveraged).

Step 2 The retailer's sales department obtains the sales forecast reports received from its stores and uses its promotion plans to generate its aggregated sales forecast plans (location dimension leveraged).

Step 3 The manufacturer's sales department uses forecast model service, data service and solver service agents to generate its forecast based on its sales records and other information obtained from suppliers, etc. (time dimension leveraged).

Step 4 The sales forecasts from the retailer chain and manufacturer are compared by a sale forecast reconciliation service agent to identify the variances and the variances are reconciled. The decision makers are informed if the variances are signi<sup>fi</sup>- cant (resource, location and lifecycle dimension leveraged).

Step 5 The reconciled sales forecast is used by the retailer chain and manufacturer to produce their order forecasts based on their inventory and product schedule by an order forecast reconciliation service agent. The order forecast results from the two parties are reconciled again by an order forecast reconciliation service agent. The decision makers are informed if the variances are signi<sup>fi</sup>cant and <sup>fi</sup>nal adjustments are made by other parties (resource, location and lifecycle dimension leveraged).

The sales forecast in this implementation involves the integration of model, data, solver and visualization services in the data mining service repository. The forecast model service is a construct used to represent the forecast problem in an organization. The data service can be obtained from the database stored within the organization. The instantiated model needs to execute an algorithm to calculate the forecast. This algorithm, or solver service, can exist as an independent entity. The results of the execution of the algorithm are put into the forecast model. The data stored in the model can be visualized using a visualization service.

Using the service components described above the forecasting decision process is as follows. A forecast model service is invoked to represent the forecast problem (Fig. 10). The model is then instantiated with the data service for historical sales and the preliminary forecast (Fig. 10). The model is executed by passing the data to a solver service and receiving a result (Fig. 11). The model uses visualization service to display its historical sales and forecast data (Fig. 12). Different solver services are used to conduct what-if analysis on the forecast results. Different alpha, beta and gamma parameter values in the solver (triple exponential smoothing forecast method) are used. The forecast model is saved to a <sup>fi</sup>le and terminated as and used as a service when required.

## 8. Discussion

Decision support systems are designed to support decision makers for solving unstructured or semi-structured problems in business organizations. Decision makers are often geographically distributed and their decision making can affect each other when solving problems within a complex environment. Many systems are de<sup>fi</sup>cient in providing support for such complex decision making because they lack the capacity of integration with other enterprise systems. These and other problems can be mapped into the issues of resource, location, lifecycle and time in DSS design. To address these problems we propose the abstract distributed decision support framework. Our framework is predicated on a contemporary interpretation of organizational work where collaboration between organizations is vital for the delivery of high level services such as data analytics. This abstract framework is able to adapt to changes in its environment to support any decision maker using any system platform, at anytime and anywhere inside/outside of an organization. This motivated us to propose a distributed decision making process to support complex decision making in organizations keeping in mind the four dimensions. A distributed DSS framework and an agent-enabled distributed DSS architecture were designed to support this decision making process.

The proposed service-oriented framework was designed with the main concepts of components, mapping, DSS, SDSS and scenario in a distributed environment. Components such as data, models, solvers, visualization and scenarios are collected and integrated into decision support systems to support users (system builders and decision makers). DSS components and DSS are distributed across intra, extra and inter layers to address the resource, location, lifecycle and time dimensions.

![](/api/attachments/JG33DN7U/fulltext/images/6b252e54419393c8b512717e8b3d7277e64a797d01021b2cddb5b098b4ac4ae6.jpg)  
Fig. 10. Invoking services from agents.

![](/api/attachments/JG33DN7U/fulltext/images/4a789d9606a77eab57b7ec520f64c1936d73416e04b9a44c9395717d69162981.jpg)  
Fig. 11. Parameter mapping between model and solver services.

The ASDSS architecture was introduced to realize the concepts in the frameworks. Data, model, solver and visualization concepts were realized by component objects in an OOP paradigm. Mapping was realized with OOP technology. The intra and extra, and inter layers in a distributed structure were realized by the Intranet, Extranet and Internet systems. The agents were used in the ASDSS architecture to realize the concepts of resource, location, lifecycle and time dimensions. To support resource and location dimensions, the construction of agent shells and DSS components gives the agents the capacity to carry components. To support the lifecycle dimension, the agent lifecycle facilitates the component lifecycle. To support the time dimension, the agents work as a team in the agent community, sharing the objects for parallel or sequential decision making processes. A prototype in the CPFR domain was built to implement, assess and re<sup>fi</sup>ne the process, frameworks and architecture introduced in this paper.

A key issue that usually arises with respect to design oriented work is the validation or evaluation of the design framework. In this paper, we propose that the design product is a proof-of-concept of our generalizable framework for DSS implementation. Our design approach is built fundamentally on four key dimensions: resource, location, lifecycle, and time. For the resource dimension, our design shows that it has addressed the key issues of independence, integration, sharing and extensibility, all of which are essential in the collaborative service oriented organizational structure. For the location dimension, we focus on mobility, reach, and communicability as the key necessary functionalities for DSS design. For the lifecycle dimension, the design emphasizes scenario lifecycles, model lifecycles, and automation as important considerations. Finally for the time dimension, the design provides support for synchronous and asynchronous functioning as well as sequential and parallel execution. Section 7 provides one approach to validation through example where the various functionalities are demonstrated. This may be seen as one of the limitations of the work. Further validation may be carried out in simulated organizational environments or through the use of action research by embedding the implementation in an organization [20]. The design approach that we propose, while robust in terms of functionality, needs implementation based <sup>fi</sup>ne tuning before such organizationally based validation exercises are possible. Situating complex technology based organizational interventions in an organization is an elaborate but essential exercise; however in this paper, we offer the <sup>fi</sup>rst step necessary before such an exercise can be undertaken.

![](/api/attachments/JG33DN7U/fulltext/images/8ea1a68f66aa03409839110ff34127807d80ac1ac51ffd2266042114e7424521.jpg)  
Fig. 12. Displaying forecast results by visualization service.

Our approach to design for supporting inter-organizational decision making offers potentially practical solutions for managing complex collaborative business processes. We do not believe that a technical solution alone will be successful in managing such processes. However, proper designs can go a long way in supporting decision making processes that are contemporary and relevant. This work offers a signi<sup>fi</sup>cant potential to enhance the effectiveness of the use of technology in a decision making context in dynamic organizational environments. While the notion of supporting decision makers has existed for a number of years, two fundamental and signi<sup>fi</sup>cant shifts have necessitated a rethinking of design principles of such systems. The <sup>fi</sup>rst is the evolution of the underlying technologies that incorporate better design practices, tools, and methodologies and the accompanying growth of technological awareness of decision makers as individuals. The second is the service orientation of design methodologies that recognizes the complexities of modern organizations the need for collaborative design implementations. This is a re<sup>fl</sup>ection of the broader notion of collaborative organizations that are well served by a service orientation. Our work addresses the issue of decision support for organizations by incorporating the service orientation directly into design processes.

## References

[1] A.A. Angehrn, H.-J. Luthi, Intelligent decision support systems: a visual interactive approach, Interfaces 20 (6) (1990) 17–28.

[2] C. Argyris, Single-loop and double-loop models in research on decision making, Administrative Science Quarterly 21 (1976) 363–375.

[3] M. Baldi, S. Gai, G.P. Picco, Exploiting code mobility in decentralized and <sup>fl</sup>exible network management, Lecture Notes in Computer Science, Proceedings of the First International Workshop on Mobile Agents, 1219, Springer-Verlag, London 1997, pp. 13–26.

[4] H.K. Bhargava, R. Krishnan, R. Muller, Decision support on demand: emerging electronic markets for decision technologies, Decision Support Systems 19 (1997) 193–214.

[5] H.K. Bhargava, D.J. Power, D. Sun, Progress in web based decision support technologies, Decision Support Systems 43 (2007) 1083–1095.

[6] R. Bonczek, C. Holsapple, A. Whinston, Foundations of Decision Support Systems, Academic Press, New York, 1981.

[7] R. Bose, V. Sugumaran, Semantic Web Technologies for Enhancing Intelligent DSS Environments, in: U. Kulkarni, D.J. Power, R. Sharda (Eds.), Decision Support fo Global Enterprises, Springer, 2007, pp. 221–238.

[8] W. Brenner, R. Zarnekow, H. Wittig, Intelligent Software Agents: Foundations and Applications, Springer-Verlag, Berlin Heidelberg, 1998.

[9] T. Bui, J. Lee, An agent-based framework for building decision support systems, Decision Support Systems 25 (1999) 225–237.

[10] P.A. Cartwright, Only converge: networks and connectivity in the information economy, Business Strategy Review 13 (2) (2002) 59–64.

[11] U. Cortes, M. Sanchez-Marre, L. Ceccaroni, I.R. Roda, M. Poch, in: M.A. Hingham (Ed.), Arti<sup>fi</sup>cial Intelligence and Environmental Decision Support Systems, Kluwer Academic Publishers 2000.

[12] V.T. da Silva, C.J.P. de Lucena, Modeling multi-agent systems, Communications of the ACM 50 (5) (2007) 103–108.

[13] A.V. Deokar, O.F. El-Gayar, A semantic web services based architecture for model management, Proceedings of the 41st Hawaii International Conference on Systems Sciences, IEEE Computer Society, 2008.

[14] A.V. Deokar, O.F. El-Gayar, A.V. Deokar, O.F. El-Gayar, Enabling distributed model management using semantic web technologies, Proceedings of the 42nd Hawaii International Conference on Systems Sciences, IEEE Computer Society, 2009.

[15] T. Erl, Service-Oriented Architecture: Concepts, Technology, and Design, Prentice Hall PTR, 2005.

[16] S. Franklin, A. Graesser, Is it an agent, or just a program?: A taxonomy for autonomous agents, Proceedings of the Third International Workshop on Agent Theories, Architectures, and Languages, Springer-Verlag, Berlin Heidelberg, 1996.

[17] J. Frauendorf, Customer Processes in Business to Business Service Transactions, Gabler, Wiesbaden, 2006

[18] A. Geoffrion, An introduction to structured modeling, Management Science 33 (5) (1987) 547–588.

[19] G.A. Gorry, M.S.C. Morton, A framework for management information systems, Sloan Management Review 13 (1) (1971) 55–70.

[20] A.R. Hevner, S.T. March, J. Park, S. Ram, Design science in information systems research, MIS Quarterly 28 (1) (2004) 75–105.

[21] T. Juan, L. Sterling, M. Winikoff, Assembling agent oriented software engineering methodologies from features, Lecture Notes in Computer Science, AOSE, 2585/2003, 2003, pp. 198–209.

[22] D. Kotz, F. Mattern, Agent Systems, Mobile Agents, and Applications, Springer, Zurich, 2000.

[23] R. Krishnan, K. Chari, Model management: survey, future research directions and a bibliography, Interactive Transactions of OR/MS 3 (2000).

[24] D. Lange, M. Oshima, Programming and Deploying Java Mobile Agents with Aglets, Addison-Wesley Professional, 1998.

[25] B. Liberman, F. Griffel, M. Merz, M. Lamersdorf, Java-based mobile agents — how to migrate, persist, and interact on electronic service markets, Proceedings of MA97 Workshop, Springer-Verlag, Berlin, 1997.

[26] A. Liew, D. Sundaram, Flexible modelling and support of interrelated decisions, Decision Support Systems 46 (4) (2009) 786–802.

[27] R.F. Lusch, S.L. Vargo, The Service-dominant Logic of Marketing: Dialog, Debate, and Directions, M.E. Sharpe, Armonk, USA, 2006.

[28] T. Madhusudan, N. Uttamsingh, A declarative approach to composing to composing web services in dynamic environments, Decision Support Systems 41 (2006) 325–357.

[29] P.P. Maglio, J. Spohrer, Fundamentals of service science, Journal of the Academy of Marketing Science 36 (2008) 18–20.

[30] W.A. Muhanna, SYMMS: a model management system that supports reuse, sharing, and integration, European Journal of Operational Research (1994) 1l093–1123.

[31] M.E. Nissen, K. Sengupta, Incorporating software agents into supply chains: experimental investigation with a procurement task, MIS Quarterly 30 (1) (2006) 145–166.

[32] A.L. Ostrom, M.J. Bitner, S.W. Brown, K.A. Burkhard, M. Goul, V. Smith-Daniels, H. Demirkan, E. Rabinovich, Moving forward and making a difference: research priorities for the science of service, Journal of Service Research (2010) (Online First January 18th).

[33] S.J. Palmisano, The globally integrated enterprise, Foreign Affairs 85 (3) (2006) 127–136.

[34] A. Park, S. Leuker, A multi-agent architecture supporting service accesses, mobile agents'97, Lecture Notes in Computer Science, 1219, Springer-Verlag, Berlin Heidelberg, 1997, pp. 62–73.

[35] A.E. Rizzoli, J.R. Davis, D.J. Abel, Model and data integration and re-use in environmental decision support systems. Decision Support Systems 24 (1998) 127–144.

[36] M.S. Silver, Systems that Support Decision Makers, John Wiley, New York, 1991.

[37] J. Spohrer, L.C. Anderson, N.J. Pass, D. Gruhl, Service science, Journal of Grid Computing 6 (3) (2007) 313–324.

[38] R.H. Sprague, A framework for the development of DSS, MIS Quarterly 4 (4) (1980) 1–26.

[39] A. Sutcliffe, N. Mehandjiev, End-user development, Communications of the ACM 47 (9) (2004).

[40] S. Vargo, R.F. Lusch, Service-dominant logic: what it is, what it is not, what it might be, in: R.F. Lusch, S.L. Vargo (Eds.), The Service-Dominant Logic Of Marketing: Dialog, Debate and Directions, M. E. Sharpe, Armonk, US, 2006, pp. 1–10.

[41] S.L. Vargo, R.F. Lush, Evolving a services dominant logic for marketing, Journal of Marketing 68 (2004) 1–17.

[42] M. Wooldridge, An Introduction to Multi Agent Systems, John Wiley, New York, 2002.

[43] S. Zhang, S. Goddard, A software architecture and framework for web based distributed decision support systems, Decision Support Systems 43 (2007) 1133–1150.

Dr. Ching-Shen (James) Dong is a lecturer of Information Systems and Operations Management at The University of Auckland Business School. His main research areas are in service science, adaptive systems, decision support Systems and enterprise architectures.

Prof. Ananth Srinivasan is Professor of Information Systems and Digital Commerce at the University of Auckland Business School, He also serves as a Co-Director of the Centre for Digital Enterprise (CODE) which focuses on research related to technology enablement in organizations. His current research interests are in the areas of decision analytics, internet auction platform design, and technology enabled services.
