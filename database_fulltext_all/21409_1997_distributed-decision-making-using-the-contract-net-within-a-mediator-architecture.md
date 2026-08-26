---
otero_id: 21409
otero_key: "FYTTTQBY"
title: "Distributed decision-making using the contract net within a mediator architecture"
authors: "F.P. Maturana; D.H. Norrie"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)00076-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Distributed decision-making using the contract net within a mediator architecture

F.P. Maturana \*, D.H. Norrie

Division of Manufacturing Engineering, The University of Calgary, 2500 University Drive NW, Calgary, Alta., Canada T2N 1N4

## Abstract

Manufacturing industries are facing increasing competitive challenges in both maintaining their existing markets and improving their capability to respond efficiently to marketplace needs. New architectures are required for next generation of manufacturing systems which must be developed to meet these challenges. This paper introduces a novel approach for dynamically creating and managing agent communities or virtual clusters. These virtual clusters use Contract Net bidding for multi-agent negotiation and Mediator agents to co-ordinate their actions. The manufacturing system is thus populated by heterogeneous agents and structures of control which operate autonomously during the planning and execution periods of the manufacturing tasks. © 1997 Elsevier Science B.V.

Keywords: Agents; Clusters; Cloning; Co-ordination; Mediator; Planning and scheduling

## 1. Introduction

Multi-agent systems $[1,2]$ offer a new dimension for manufacturing enterprise integration. Incorporating autonomous agents into the manufacturing environment allows improved co-ordination of user-defined tasks both independently of the user and of the manufacturing device under control. Under a multi-agent system, the manufacturing shop-floor becomes populated by a number of heterogeneous intelligent agents with diverse goals and capabilities $[3]$ . These agents perform design, planning, and execution tasks in a dynamically adaptive fashion when pre-established conditions are met. These manufacturing agents also adapt themselves to the changes occurring within the manufacturing shop-floor. Manufacturing devices or other physical resources are interconnected with the multi-agent system through intelligent agent interfaces subsequently called Resource agents. These Resource agents are designed according to generic models defined in terms of the functionality required in different areas of the manufacturing shop-floor. Generic models allow the information processing requirements to be satisfied, for each individual type of agent, at a higher level of abstraction. Each Resource agent requires, at least, two levels of functionality to represent the activity of the manufacturing entity. The higher-level functions include planning and asynchronous cooperative decision-making. The lower-level functions relate to the execution of tasks defined in the planning level of the agent. These tasks involve communication both with the physical device and other lower-level agents, synchronously, to co-ordinate manufacturing actions. Manufacturing information is concurrently processed in a distributed manner through the processes carried out by the Resource and other intelligent agents in the system.

Such a manufacturing system can expand its capabilities for concurrent information processing, since the manufacturing system is provided with incremental information processing resources. Additional manufacturing devices and Resource agents are incorporated in the production environment without operational disruption, since the multi-agent system supports fundamental mechanisms for rapid assimilation of new processing entities.

In a multi-agent manufacturing system, intelligent agents react according to information received from their peers or other agents including humans within the manufacturing environment, thereby creating local plans and assuming commitments with their counterparts. Intelligent agents use their knowledge about the external domain and their internal rules to determine their responsibilities for local and global production goals.

The multi-agent system provides a platform for co-ordination and cooperation, within which its agents can work collectively to solve specific problems. Groups of agents are identified to perform specific reasoning for a given task and decision-making responsibilities are delegated to co-ordination groups (teams) [4] made up of these agents. Using this approach, the manufacturing system can thus be integrated through a harmonious association of individual agents and resources found at different places within the factory or in remote organizations [5]. This conceptualization of the manufacturing enterprise involves new paradigms for agent communities, for building the next generation of manufacturing systems [6–10]. Collaborative behavior among the agents [11] can be enhanced by incorporating Mediator agents to support multi-agent co-ordination. Such Mediator agents have meta-level rules and higher order priorities for managing the behavior of the agents.

This paper describes a Mediator architecture for an Intelligent Manufacturing System which incorporates a new approach to creating agent communities and co-ordinating their activity. These communities (virtual co-ordination clusters) are created by static Mediator agents and co-ordinated by distributed dynamic Mediator agents. The co-ordination clusters incorporate Clone agents which duplicate the reasoning behavior of the Resource agents, thus providing concurrent information processing.

The architecture incorporates mechanisms for creating agent communities and co-ordinating their actions during higher-level planning (such as manufacturability evaluation, machine routing, and scheduling). During higher-level planning, the involved agents use asynchronous message communication. Following higher-level planning, the planned tasks and sub-tasks are implemented through lower-level control agents using synchronous communication and interlocking of processes among the agents.

During planning and execution, the agents can be involved in individual tasks or collective tasks. The former case is less common on the typical manufacturing shop-floor; the latter is more common and more complex to manage. For collective task activity, top-level static Mediator agents have been implemented with capability of initially selecting and virtual clustering those agents potentially suitable for a planned task. This initial clustering involves identifying the most suitable agents and provides the starting point for an economical detailed searching process. It will obviously be inefficient to broadcast a task request to every agent in the system when selective broadcasting can accelerate the identification of the best candidate agents. The initial selection of candidate agents for such selective broadcasting is performed by the static Mediator agents which maintain global registers of the organizational entities and virtual clusters formed.

Each cluster is co-ordinated by dynamic Mediator agents which create the necessary links among the agents for forming well-organized decision-making trees (dynamic hierarchies) and manage their cooperative activity within and across virtual clusters. Message exchange protocols will determine how information is exchanged once a suitable receptor agent is found and how to maintain this exchange after the link has been established. Problems such as these have also been addressed by other projects that have implemented Mediator oriented architectures $[12–16]$ . Establishing a common language among the intelligent processes removes many difficulties in the communication of intelligent agents. For the present application, this common language is provided by the Knowledge Query Manipulation Language (KQML) [17].

Introducing multi-agent system models into the manufacturing organization is a very challenging endeavor that requires the definition of rules for agent inter-operability. Issues such as co-ordination and collaboration must be agreed upon so that the agents behave transparently with each other and operate coherently according to unified goals. Common protocols for creating intelligent agents and facilitating their inter-operation within agent communities help in providing flexibility to react to the rapidly changing manufacturing environment.

## 2. Next-generation multi-agent manufacturing systems

The Intelligent Manufacturing Systems (IMS) international research program $[18,19]$ was established to develop next-generation manufacturing systems and there are already several studies under this program focusing on intelligent agents development. For example, intelligent agents of Holonic Manufacturing Systems (HMS) work autonomously and cooperatively in an open, distributed, and intelligent manufacturing system $[20]$ . In holonic systems, intelligent agents called “holons” are allowed to have a physical part as well as a software part. The holonic architecture allows integration of the most appropriate elements of hierarchical and hierarchical systems into an intelligent and open-ended structure. HMS research is directed towards open, distributed, intelligent, autonomous, cooperating systems for applications in Intelligent Manufacturing Systems. A number of critical factors were identified $[21]$ which have to be satisfied if such systems are to successfully meet the technological challenge of the 21st century manufacturing. These critical factors include:

\- Reliability

• Real-time planning and control

\- Stability

\- Maintainability

• Standardized communications

\- Inherent flexibility

\- Graceful fault recovery

The following outlines how an appropriately designed multi-agent system addresses these factors:

## 2.1. Reliability

Reliability is here interpreted to mean that the designed level of functionality of a system is maintained over some specified period. This implies that the system be robust i.e. can maintain functionality despite component failures. A agent system is inherently an adaptive system and can be designed to adapt to specified failures using alternate-role or backup agent capability.

## 2.2. Maintainability

User-friendly systems interfaces can provide diagnostic or reconfigurability access to different areas of the agent system for maintainability. There is no need for a complete shutdown of the system to reconfigure components or lockout or replace dysfunctional components. Additional requirements can be added in the system without major disruption of operations, through reconfiguration or incorporation of additional agents.

## 2.3. Inherent flexibility

The inherent modularity of agent systems, in conjunction with distributed information processing units, allows rapid response to new system requirements through the addition of new modules and units or reconfiguration of existing ones. If the physical manufacturing machines are similarly modular and reconfigurable, this will allow the desired flexibility also in the manufacturing process capability.

## 2.4. Real-time planning and scheduling

Two major areas of activity in manufacturing are concentrated in planning and scheduling of operations. The planning process considers the technological capabilities of the system at a given time to accommodate production orders. During the planning period, new production requirements are created for which the production resources are subsequently scheduled. During the scheduling period, the system can be affected by unforeseen disturbances which may invalidate a considerable portion of the pre-planned activity. It has been shown [22] that a multi-agent approach can integrate these two major activities in real-time, through inter-related concurrent processes.

## 2.5. Standardized communications

A common communication language is required to facilitate the sharing of information among heterogeneous agents. The agents in a manufacturing system need standardization to not only be able to communicate with their peers using similar communication protocols but also to communicate with peers using different ontologies. Standardization of these and other communication levels needs to be considered a priori during the design of the manufacturing facility and its multi-agent system.

## 2.6. Graceful fault recovery

In an agent-based manufacturing system, the malfunctioning of a component device is kept at a local level. The interface agent connected to such a physical device is provided with sufficient knowledge to respond appropriately to a malfunction alarm. This alarm can be initiated by the device itself before complete unit shutdown or by the interface agent when validation data or monitoring indicates that the device is not performing normally. In a malfunction situation, the interface agent initiates fault recovery action, including the redistribution of conflicting plans.

## 2.7. Stability

The system's behavior can be monitored by higher-level agents for inappropriate responses or performance and appropriate corrective action taken. Data integrity is secured at the local level by each agent, since any distortion in the data is detected at the single-agent level. This synergy of higher-level monitoring and lower level of detection provides a hybrid model (top-down and bottom-up) for maintaining the system's integrity.

## 3. Virtual organization of a next-generation manufacturing system

The following sections describe a multi-agent architecture designed for next-generation manufacturing, with a dynamic virtual organization based on virtual clusters of entities being created in response to changing task and sub-task requirements. These clusters exist for the duration of the task or sub-task and are destroyed when their activities have been completed. During the lifetime of a cluster, sub-task requirements may necessitate the creation of a child sub-cluster. The dynamic hierarchies of clusters and sub-clusters interacting and overlapping, in changing patterns according to the varying system and task requirements, form the ever-changing adaptive virtual organization of the manufacturing system.

Increasing the autonomy of individual components within the manufacturing shop-floor diminishes the number of levels of control compared with conventional hierarchical configurations $[23]$ . Instead of having a number of pre-established and rigid layers of control, the multi-agent system uses its configuration mechanisms to dynamically organize the manufacturing devices in cooperative virtual hierarchies. Structures of control are progressively created during the planning and execution periods of the plan tasks. These structures of control are active as long as required and destroyed when no longer needed. There are multiple structures of control (coordination clusters) operating concurrently, each of them supporting different tasks $[24]$ .

In this architecture, the manufacturing system is conceptually organized in three main levels: the Manufacturing Plant Level, the Communication Medium Level, and the Multi-Agent System Level (see Fig. 1).

![](/api/attachments/FYTTTQBY/fulltext/images/1cbfd0d811983bc8baa8c01a50b768d98c107ce0847935de965f2bbccd23c0b8.jpg)  
Fig. 1. Organization of the manufacturing system.

The Manufacturing Plant Level includes the manufacturing machines and other resources. The Communication Medium Level supports communication between the physical resources and the multi-agent system and provides communication control. It also supports communication with remotely located manufacturing systems. The Multi-Agent System Level comprises the Resource and other agents and coordination mechanisms. Using this manufacturing organization, there is no need for “pre-wired” connections between devices and the structures of control. The manufacturing system is dynamically configured through logical switching directed by Mediators and Resource agents.

Although the intelligent agents are built using generic models, they perform different activities. This difference among Resource agents is determined by the type of resource under their control in the factory. These physical resources are classified according to their importance in the planning and execution processes. For example, there are Primary, Secondary, and Tertiary resources. This classification relates to resources needed for primary operations (such as drilling), secondary operations (such as threading), and tertiary operations (such as grinding). This classification of resources is not unique and is regularly used in manufacturing planning.

The available resources in Manufacturing Plant Shop-Floor can be subdivided into the above or other different types of specialization, as can their associated agents. The shop-floor may be constituted of any number of primary, secondary, and tertiary machining resources, each of which has its associated Resource agent For illustration in the following, we will consider only four agent types X, Y, Z, and W (see Fig. 2). The architecture, however, is not restricted to these types of agents and other types would normally be included such as Transport agents.

![](/api/attachments/FYTTTQBY/fulltext/images/b3cde37d90ba67dbc70fcd3826500628dd818a14b67459038bee8b540cb0ba68.jpg)  
Fig. 2. Virtual cluster.

As planning and task activity develop, agents are dynamically grouped in clusters to facilitate coordination on the current plan or task. A virtual cluster (see Fig. 2), for example, might comprise machining resources (agent type X or type Y), tools (agent type Z), and one or more Mediator agents (agent type W) or other appropriate combinations of agents. Where such a cluster comprises production processing entities together with a co-ordination Mediator, it can be described as a “virtual manufacturing cell.”

## 3.1. Mediator agents

In the multi-agent manufacturing architecture described, the Mediator agents play a fundamental role. Individual agents work cooperatively to accomplish the requirements of tasks that initiate their collaboration. Such agents have limited knowledge about the organization and the existence of other agents. Mediator agents bridge the knowledge gap among those agents whose capabilities are restricted to a local area of expertise. They facilitate the gathering of agents into collaborative groups or clusters and coordinate their cooperative decision-making. In the coordination clusters, manufacturing constraints (technological and time-dependent constraints) are evaluated and the space of suitable solutions is explored concurrently. Co-ordination clusters provide the manufacturing system with robust decentralized reasoning and control infrastructures.

Mediator agents also provide communication services for brokering and recruiting and also provide matchmaking services between information processing units using a common ontology. In this architecture, all agents use the KQML protocol for encoding messages. Mediator agents are provided with sufficient organizational knowledge to match requests for services with appropriate agents and to create the necessary agent-to-agent relationships among Clone agents in co-ordination clusters. This agent-to-agent relationship allows for selective message broadcasting.

Agents and Mediators form the co-ordination tuples $\langle$ Agents, Mediators $\rangle$ . These organized communities form a dynamic virtual hierarchy which allows parallel search of the space of task and sub-task solutions. Using this approach, there is not need for pre-establishing the search domain or maintaining all search information globally.

In this new configuration, the interconnection among the agents is loosely coupled. This facilitates a rapid adaptation of the system to normal and unforeseen situations. For example, new physical manufacturing resources may be added to the system for expanding production. These devices need to be registered in the manufacturing organization and represented by Resource agents. During the registration process of a resource in the shop-floor, a number of KQML messages are broadcast between the device and the multi-agent system. New resources are registered in one or more shop-floor communities and notified to the static Mediator agents. To provide the necessary data on the device's functionality, Mediator agents use this knowledge to establish the required agent-to-agent relationship during negotiation and co-ordination tasks.

## 3.2. Distributed manufacturing and agent communities

With distributed manufacturing, the “shop-floor” will actually be a number of production shop-floors, geographically separated. Here, these shop-floors will also be described as “communities”. Each comprises physical production resources and the associated agents which form its agent community.

These communities are the static members of the structure of control, since their basic configuration is not changed unless a higher priority order modifies their structure. These communities are intended to assume individual and collective tasks. Individual tasks are assumed when the local resources are sufficient to achieve every aspect of the tasks. When the local resources are not sufficient, collective activity among the communities is required. Both types of activity are supervised by a Mediator agent (static member) and the subsequently created distributed Mediator agents (dynamic members).

Design and high-level production planning and control functions (e.g., orders commitment) form a necessary part of a distributed manufacturing system. These will be called respectively Design and Production Management sub-systems or modules. A coordinator is needed between these sub-systems and the shop-floor communities and this module is denoted as the Shop-Floor Manager. Fig. 3 illustrates a simplified distributed manufacturing system with these components.

![](/api/attachments/FYTTTQBY/fulltext/images/af99649c82e3b8b40fa0df882517a62feee7ce1e232ebf627a20f2f3ba5c933b.jpg)  
Fig. 3. Distributed intelligent manufacturing system.

## 3.3. Contract net bidding

The agent communities receive their production related orders as Contract Net bids from the Design or Production Management sub-systems. These requests are broadcast to the agent communities through the Shop-Floor Manager which initially plays the role of message re-director. The request includes the preferred type of resources to be contacted in the shop-floor domain for the task. This initial interpretation of the message is carried out by the static Mediator agent for the shop-floor. The request is then redirected to suitable agents within the shop-floor community. At this stage, a number of pre-selected agents are gathered in a primary-level coordination cluster which is supervised by dynamic Mediators. The co-ordination cluster then initiates the needed information processing and negotiation to satisfy the task requirements.

Each Resource agent consists of a reasoning sub-agent and an execution sub-agent. The reasoning sub-agent planning task activities but cannot finally commit the resource to a specific task and schedule. This latter function is carried out by the execution sub-agent. To enable an Resource agent for a physical resource to participate concurrently in more than one cluster, its reasoning sub-agent is replicated as one or more Clone agents which can be gathered into clusters as needed.

Each Clone agent in a co-ordination cluster analyzes requested operations, establishes precedence constraints, and contacts additional resources as needed. The Clone agent uses its heuristic rules and cost-based models in establishing a task bid, which is then announced to the other agents in the cluster. The bid can be any of three types: total satisfaction, incomplete satisfaction, or rejected satisfaction. Total satisfaction corresponds to a bid in which all requirements are satisfied exactly (parameters such as cutting speed, tools, tolerances, and due-dates are precisely satisfied). Incomplete satisfaction includes those bids which can satisfy the basic requirements but not to the specified level. Rejected satisfaction includes those bids for which at least one requirement cannot be satisfied at any level. Depending on their bid type, Clone agents are retained or dismissed from the clusters. Clone agents may also dismiss themselves from the clusters. The final agents in the cluster will be those in the first and second bidding categories.

Clone agents also initiate sub-contracting with other clones that may exist within the same virtual cluster or in a remote organization. When this happens, the Clone agents are supported by Mediator agents to find the needed sub-contractors. In this case, communication is established among Mediator agents which manage the organization knowledge. This activity is hidden from the Design or Production Management modules, where users or agents wait for the answer to the initial request which initiated this negotiation activity.

The sub-contracting process concludes when the Mediator agents (local or remote) find a new set of potential candidate agents and connect them to the contractor agent. Agents then establish direct communication, and a series of KQML messages are interchanged through localized communication. Using this approach, the risk of creating bottleneck processes is avoided. The decision-making responsibilities are, during this time, given to the co-ordination clusters. The Mediator agents can be integrated into the decisions, but their participation is delayed to the last moment and oriented to solve conflicts among plans. Such Mediator agents are customized with heuristic strategies to cope with different situations arising from the decisions at the cluster levels. Mediator agents avoid deadlock events and facilitate a consistent plan generation within the communities.

The message communication among the co-ordination clusters and the creation of new sub-communities continues until a solution is found. The solution is expressed as a set of partial plans offered by agents in different virtual clusters. These partial plans are finally unified into a global plan. As the decision-making progresses, co-ordination clusters and Clones are created and destroyed. This creation and destruction of cluster and clone agents constitutes an innovative attribute of this architecture.

The organization, as described above, itself creates the structure of control as needed. The system never lacks for supervision. Real-time constraints (such as limited slots of time to allocate operations, machine failures, changes in production strategies) are considered during the planning and execution of tasks.

## 4. The architecture of a virtual cluster

In the previous section, both static and dynamic members of the overall structure of control were identified. We mean by a static member a tuple $\langle$ Mediator agent, Resource agents $\rangle$ , and by a dynamic member a tuple $\langle$ Mediator agent, Clone agents $\rangle$ . In the static member case, there are static Mediator agents which operate as meta-level agents to co-ordinate the physical resources and the Resource agents of specific classes. In the dynamic member case, there are two types of Mediator coordinator: Data-Agent Manager (DAM) and Active Mediator (AM). Clone agents (CA) are replications of the Resource agents. A co-ordination cluster is a tuple $\langle$ DAM, AM, CA $\rangle$ having an organizational structure with three hierarchical levels (see Fig. 4).

The structure of a cluster provides the decision-making environment for a particular task and allows for the search domain to be extended as needed. This approach will create overlapping search layers. Within the clusters, the Clone agents represent the corresponding Resource agents in multiple and concurrent decision-making activities. This architecture can thus support multiple tasks in parallel fashion. In a manufacturing system in which the decision-making processes can provoke an expanding search there are definite advantages in providing such support for concurrent activities.

![](/api/attachments/FYTTTQBY/fulltext/images/bdf7b8a3aab159e96520faf14e2121ecd8c2b84bdf1a6ad4ef817908dbd80df2.jpg)  
Fig. 4. Virtual co-ordination cluster.

In manufacturing systems, planning and scheduling are difficult tasks that may provoke large searches for optimal solutions. This architecture provides a framework for supporting these tasks (planning, scheduling, and execution) concurrently.

## 4.1. Communication within a cluster

In the co-ordination cluster, Clone agents communicate through asynchronous messaging, using the KQML protocol to wrap the content of the information. The KQML wrapper contains a declarative layer (performatives) in which the intention of the message is indicated. This declarative layer is combined with the language used for encoding of the content of the message. The content layer is filled with short statements indicating further actions to be carried out with the data included in this layer. The multi-agent system is also provided with a common ontology for coding and decoding of messages.

The communication status of a Clone agent has two states: the sender state and the receiving state. In the sender state, the agent writes a KQML message and gives it to the local co-ordinator Active Mediator for broadcasting (see Fig. 5). The Active Mediator uses the declarative layer and communication layer of the message to redirect the message or to apply a new action. The Active Mediator does not inspect the content layer of the message, since this is only required for planning. Clone agents broadcast messages concurrently within each co-ordination cluster. A Clone agent may change its status to a wait mode, until the reply for the message is received. A Clone agent may also continue its operation and wait for the replied message using a background process.

A receiving Clone agent decodes the input message and uses the performatives (Recommend-all, Tell, Dismiss) to further analyze the content data.

![](/api/attachments/FYTTTQBY/fulltext/images/9d24a4981e9b2d26a77b6ee194af21ef4a480c44669243245a60a8176e942044.jpg)  
Fig. 5. Asynchronous communication.

Conventional distributed planning studies have proposed four states through which an agent reacts to an external communication. The agent may decide to create a plan (Plan), modify a current plan (Re-plan), inform private data (Inform), or to proceed with execution (Execution). Performatives such as Recommend-all, Tell, and Dismiss have been customized to help agent communication in the manufacturing application. The Recommend-all performative is used to initiate contracting and sub-contracting among agents. The Tell performative is used to share data. The Dismiss performative has been created for this application and is used for dismissing agent from the co-ordination clusters.

## 5. Distributed concurrent decision-making

In this architecture, the Contract Net protocol $[25]$ has been extended to support concurrent decision-making for manufacturing application. The protocol now includes cloning and clustering mechanisms implemented within a Mediator architecture. These mechanisms are now described.

The manufacturing system supports multiple Design and Production Management modules for concurrent engineering requirements. Tasks are originally broadcast by the Design and Production Management sub-systems to the Shop-Floor Manager which distributes these among the static Mediator agents in the shop-floor communities. The static Mediator agents communicate with Resource agents to initiate a new set of clones and co-ordination clusters. The Clone agents initiate their planning and progressively advance into a solution plan. Each Clone agent offers a primary partial plan to other Clone agents in the cluster. This includes an operation cost that considers both technological and time constraints (for example, accuracy of the manufacturing operations and the scheduling availability). Every agent has different policies and different values for costing operations. The initial planning may be accomplished if all needed operations and resources are available in the first-level cluster. However, the usual case requires several levels of sub-contract among the resources.

To fulfill a task's further requirements, Clone agents will request additional resources by sending KQML messages to their Active Mediators to find suitable agents which can supply these additional resources. The Active Mediator (AM) then contacts its Data-Agent Manager (DAM) which subsequently establishes inter-agent communication with suitable resources. It should be noted that the new resource may be found in a remote shop-floor, as the DAM will contact the static Mediator for its own shop-floor community if it cannot locate suitable local resources. This initiates higher-level contracting which is performed among the static Mediators of the shop-floors involved. The Contract Net sub-contracting continues to propagate, generating further clusters and sub-clusters until all requirements are met. A snapshot of this cluster structure resembles a complicated tree or web, with multiple branching of different sizes. As the multi-agent planning progresses, branches are both being created and destroyed.

Every task generates its own unique branching of co-ordination clusters. A shop-floor community may be hosting many of these branches in real-time. A branch grows until all resources needed for the tasks are found. In each successive cluster, Clone agents then concentrate the decisions from their lower-level clusters. The composite decision concentrated at the final top-level cluster provides the optimal combination of resources for the task, under the current condition of the system. This planning activity includes all technical evaluation needed for production (process planning, machine routing, and scheduling). At the higher-level clusters, during final concentration of plans, it may be found that sub-clusters may have provisionally allocated different sub-tasks in the same slot of time to the same resource. At this higher level, the clusters involved resolve this conflict through the cooperative action of their DAM.

![](/api/attachments/FYTTTQBY/fulltext/images/288e9625dba9c2576830b6ce51edfb5ba0e33a3e1c99770cec8f8aacd5a853aa.jpg)  
Fig. 6. Multi-agent search.

For a particular task, Fig. 6 illustrates the bidding process and the multi-dimensional tree or web of co-ordination clusters, Clone agents and Mediator agents. Here, the co-ordination Cluster-1 involving Clone agents of type-X requests the local Machine Static Mediator to find additional resources for tooling and machining. The Machine Static Mediator then finds suitable agents (here assumed to be all type-Y) and creates Cluster-2. Subsequently, the Machine Static Mediator send a resource request to the Tool Mediator and Cluster-3 for tool agents type-Z is created. Cluster-2 then requests additional machining resources and Cluster-4 is created. Subsequently, Cluster-4 requests for tools and Cluster-5 is created. Each cluster recognizes its owner cluster and dependent clusters. This facilitates direct communication among related planning groups without the intervention of a centralized manager.

## 5.1. Inter-cluster planning and scheduling

A manufacturing system has numerous constraints involving technological and time-dependent variables which cannot be satisfied through one single step of negotiation. Consider the following situation in which a static Mediator has received a request for routing and scheduling a job order involving two individual part types named Task $_{1}$ and Task $_{2}$ . For this example, we consider a batch size of one element for each part type. Task $_{1}$ has two operations (op $_{11}$ and op $_{12}$ ) and Task $_{2}$ has two operations (op $_{21}$ and op $_{22}$ ). These operations can be processed in any of the primary resources R $_{1}$ , R $_{2}$ , R $_{3}$ , or R $_{4}$ . The static Mediator then broadcast requests to those shop-floor communities that contain these resource types to establish virtual clusters for these tasks. The resource agents in the clusters perform their initial bid evaluation and decide to participate or drop out of in the subsequent routing and scheduling negotiation. Once the primary-level resources in the cluster are thus selected, new co-ordination clusters are initiated involving dynamic Mediators and Clone agents for these resources. At this stage, it will be assumed that the two tasks are thus assigned to two clusters (Cluster $_{1}$ and Cluster $_{2}$ ) involving all of the resources R $_{1}$ , R $_{2}$ , R $_{3}$ , or R $_{4}$ as shown in Fig. 7.

![](/api/attachments/FYTTTQBY/fulltext/images/525f65c3918ac930d5d2a41d45cdf55dfce6692edc658cf1c318abf2eae33941.jpg)  
Fig. 7. Sub-level cluster.

It will be seen that the initial task requests created a two-level dynamic hierarchy. It should be noted that the hierarchy has been simplified for illustration purposes. Additional levels would be created if subcontracting clusters are needed. A more detailed description would normally include Tool clusters and Transportation clusters. Once the task requirements are fulfilled, the clusters and their virtual hierarchy are destroyed.

Each cluster has a DAM and an AM agent for inter and intra co-ordination respectively. The DAM agent is used to control the communication among the clusters, especially during the terminal stages of negotiation. If a cluster sub-contracts with other clusters, it is responsibility of the respective DAM agents to pass the messages to and from the clusters. The AM agent is used to co-ordinate message passing among the Clone agents of the cluster and to check for deadlock situations.

Each Clone agent in a cluster analyzes requested operations, establishes precedence constraints, and contacts additional resources as needed. A Clone agent uses its heuristic rules and cost-based models in establishing a bid. The bid is then announced to the other agents in the cluster. The bid can be any of the three following varieties: (1) total satisfaction, (2) incomplete satisfaction, or (3) rejected satisfaction.

Total satisfaction corresponds to a bid in which all requirements are satisfied exactly (parameters such as cutting speed, tools, tolerances, and due-dates are precisely satisfied). Incomplete satisfaction includes those bids which can satisfy the requirements but not exactly. Rejected satisfaction includes those bids for which at least one requirement cannot be satisfied at any level. Depending on their bid type, Clone agents are retained or dismissed from the clusters. Clone agents may also dismiss themselves from the clusters. The final agents in the cluster will be those in the first and second bidding categories.

A negative plan relation could be originated if, for example, two operations scheduled within the same resource had overlapping time slots. This situation would be resolved by the agents in the involved clusters using their heuristics to determine the order in which these operations should be performed or whether re-allocation to another resource is desirable. In a case such as this, to determine the final allocation, the Clone agents involved need to share their plans across the co-ordination clusters. The result might be the allocation of one of operations into another resource.

In the routing and scheduling phases, the Resource agents involved provide planned commitments and operation costs. Each commitment includes an operation time slot which satisfies the required precedence constraints. By having local control upon their scheduled and unscheduled times, the Resource agents can preempt or re-schedule tasks according to job priorities or changing shop-floor situations (e.g., machine failure).

## 5.2. Execution commitment communication protocol

Each Resource agent has the same number of primary communication links as it has Clone agents, at any stage of the negotiation process. The status of a link depends on the temporal states of the Resource agent. The possible temporal states are: Acceptance, Temporal, and Blocked. In the Acceptance state, the agent is idle and does not have active Clone agents. In the Temporal state, the Resource agent has been replicated and its new Clone allocated in a co-ordination cluster. This Clone agent would be currently bidding or receiving commitment offers from remote agents. In the Blocked state of a Resource agent, it has a Clone agent defining a plan and the communication and acceptance of new commitments is temporarily locked out. These dynamic states allow any Resource agent to control its commitment behavior during critical periods of the negotiation process (see Fig. 8).

![](/api/attachments/FYTTTQBY/fulltext/images/36564950e43884480adb4c51152bee41987e023d5e2dafd2ffda5367a256a3bd.jpg)  
Fig. 8. Communication links for temporal state.

In the Acceptance state, a requester agent has a high probability of concluding a favorable negotiation with the Resource agent (considering that the Resource has the availability, capability, and capacity needed to assume the commitment). During the Temporal state, a Resource agent will be communicating with other agents “wishing” to allocate operations to this resource. This period corresponds to the planning period. In the Blocked state, a Resource agent has reached a final planning stage and is preparing for execution transactions. This last phase concludes when the Resource agent has finished the negotiation and a contract has been committed.

## 6. Conclusions

In this paper, we have presented a multi-agent Mediator architecture for facilitating cooperation and co-ordination among agent communities in a distributed manufacturing system. This provides both virtual organization through virtual clustering and distributed decision-making through Contract Net bidding. A system of this type can respond in real-time to changing or unforeseen situations. This approach, therefore, provides a robust platform for Intelligent Manufacturing System applications.

Two key properties of the architecture developed are: integration of activities across heterogeneous environments and real-time self-adaptation of the Mediator organization to environmental variations. This architecture can be used in applications beyond the manufacturing one for which has been initially developed, since it provides a generalized protocol for enterprise integration which is an important application field for multi-agent systems.

The Mediator architecture provides further opportunities for studying and understanding the behavior of intelligent agents in a complex distributed manufacturing system. It can also assist in validating decentralized approaches for problem solving and multi-agent co-ordination.

## References

[1] M.P. Singh, Multiagent systems, Lectures in Artificial Intelligence 799 (1994) 81–113.

[2] M. Wooldridge, N.R. Jennings, Intelligent agents: theory and practice, The Knowledge Engineering Review 10 (2) (1995) 115–152.

[3] Y. Shoham, Agent-oriented programming, Artificial Intelligence 60 (1993) 51–92.

[4] K.M. Carley, Z. Lin, Organizational designs suited to high performance under stress, IEEE Transactions on Systems, Man. and Cybernetics 25 (2) (1995) 221–230.

[5] S. Kirn, J. Schneider, STRICT: selecting the right architecture, industrial and engineering applications of artificial intelligence and expert systems, Lectures in Artificial Intelligence 604 (1992) 390–400.

[6] M. Barbuceanu, M. Fox, The information agent: an infrastructure for collaboration in the integrated enterprise, in: Proceedings of the Second International Working Conference on Cooperating Knowledge Based Systems, University of Keele, 14–17 June 1994, pp. 257–294.

[7] D.H. Norrie, An integrated object-oriented architecture for manufacturing knowledge systems, in: Proceedings of the IJCAI-89 Workshop on Integrated Architectures for Manufacturing, Eleventh International Joint Conference on Artificial Intelligence, Detroit, 20–25 August 1989, 4p.

[8] D.H. Norrie, A.D. Kwok, Object-oriented distributed artifi-

cial intelligence, in: Proceedings of International Symposium on New Results and New Trends in Computer Science, Graz, Austria, June 20–21, 1991, LNCS 555, Springer, Berlin, 1992, pp. 225–242.

[9] A.D. Kwok, Information Systems Architecture for Intelligent Manufacturing, PhD Thesis, Department of Mechanical Engineering, Division of Manufacturing Engineering, University of Calgary, 1993.

[10] D.H. Norrie, O.R. Fauvel, B.R. Gaines, Object-Oriented Management Planning Systems for Advanced Manufacturing, Symposium on AI and Manufacturing, American Association for Artificial Intelligence, Stanford University, 28–30 March 1989, pp. 75–79.

[11] S.D. Bird, G.M. Kasper, Problem formalization techniques for collaborative systems, IEEE Transactions on Systems, Man, and Cybernetics 25 (2) (1995) 231–234.

[12] G. Wiederhold, Mediators in the architecture of future information systems, IEEE Transaction on Computer (1992) 38–48.

[13] B.J. Dorr, L. Raschid, Information Mediation Techniques for Problem Solving with Multiple Knowledge Servers, Computer Science Department, Institute for Advanced Computer Studies, University of Maryland, 1992.

[14] S. Adali, V.S. Subrahmanian, Amalgamating Knowledge Bases, II: Distributed Mediators, Department of Computer Science, Institute for Advanced Computer Studies, University of Maryland, CS-TR-3124, August 1994.

[15] M.R. Genesereth, S.P. Ketchpel, Software agents, Communications of the ACM 37 (7) (1994) 48–53; 147.

[16] M. Jarke, M.T. Jelassi, M.F. Shakun, Mediator: Toward a Negotiation Support System, Evolutionary Systems Design: Policy Making Under Complexity and Group Decision Support Systems, Holden-Day Inc., Oakland, CA, 1988, pp. 152–181.

[17] T. Finin, J. Weber, G. Wiederhold, M. Genesereth, R. Fritzson, D. McKay, J. McGuire, P. Pelavin, S. Shapiro, C. Beck, Specification of the KQML Agent-Communication Language, Enterprise Integration Technologies, Palo Alto, CA, Technical Report EIT TR 92-04, 1992.

[18] T. Tomiyama, The Technical Concept of IMS, RACE Discussion Paper, No. RA-DP2, Research into Artifacts, Center for Engineering, The University of Tokyo, 1992.

[19] B.R. Gaines, D.H. Norrie, Knowledge systematization in the international IMS research program, in: Proceedings of IEEE Computer Systems, Man and Cybernetics, Vancouver, Canada, 22–25 October 1995, pp. 958–963.

[20] T. Hasegawa, L. Gou, S. Tamura, P.B. Luh, J.M. Oblak, Holonic planning and scheduling architecture for manufacturing, in: Proceedings of the Second International Working Conference on Cooperating Knowledge Based Systems, June 14–17, University of Keele, 1994, pp. 125–139.

[21] J.H. Christensen, O.J. Struger, D.H. Norrie, C. Schaeffer, Material handling requirements in holonic manufacturing systems, in: Proceedings of the 1994 International Material Handling Research Colloquium, 13–15 June, Grand Rapids, MI, published by the Material Handling Industry of America, 1994, 22p.

[22] S. Balasubramanian, F.P. Maturana, D.H. Norrie, Multi-agent planning and coordination for distributed concurrent engineering, International Journal of Cooperative Information Systems (1996), 5, 153–179.

[23] A.R. Chaturvedi, R. Gulati, G. Koehler, Computational Ecology of Manufacturing Systems, AAAI-94 Workshop Program Reasoning about the Shop Floor (SIGMAN), July 31–August 4 1994, Seattle, Washington.

[24] F.P. Maturana, D.H. Norrie, A generic mediator for multiagent co-ordination in a distributed manufacturing system, in: Proceedings of IEEE Computer Systems, Man and Cybernetics, Vancouver, Canada, 22–25 October 1995, pp. 952–957.

[25] R.G. Smith, R. Davis, Frameworks for cooperation in distributed problem solving, IEEE Transactions on Systems, Man, and Cybernetics SMC-11 (1) (1981) 61–69.

![](/api/attachments/FYTTTQBY/fulltext/images/4854070ad6f980a420fa13a068a9cbb7a03aba292bad1ae1d4ab40c08f751e3c.jpg)

Douglas H. Norrie currently holds the Nortel Chair in Intelligent Manufacturing at The University of Calgary, Alberta, Canada. Formerly, he was Head of the Division of Manufacturing Engineering at the University of Calgary. He is also Professor of Mechanical Engineering and Adjunct Professor of Computer Science at the same institution. His research interests are in Intelligent Systems and, in particular, in Multi-Agent Applications in Manufacturing.

![](/api/attachments/FYTTTQBY/fulltext/images/164785232342eed7445d02d7a8447f0b2200ba7124a2d2c00f0f276345b1d5cd.jpg)

Francisco P. Maturana received his B.S. degree in Mechanical Engineering in 1990 from the University of Santiago, Chile and his M.S. degree in Simulation Sciences and Mechanical Engineering in 1993 from the California State University, Chico. He has been a Visiting Research Associate at the Chico Centre of the McLeod Institute of Simulation Science (1991–1993). He is currently a doctoral candidate in Manufacturing Engineering at the University of Calgary,

where his research activities have been in the areas of Distributed Artificial Intelligence, Intelligent Manufacturing Systems, and Simulation Testbeds for Multi-Agent System Applications in Manufacturing. He is a member of the IEEE Society and the SCSI.
