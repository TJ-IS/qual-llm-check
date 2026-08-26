---
otero_id: 22001
otero_key: "VFN667DU"
title: "A federation–agent–workflow simulation framework for virtual organisation development"
authors: "Hai Zhuge; Jian Chen; Yulin Feng; Xiaoqing Shi"
year: "2002"
journal: "Information & Management"
doi: "10.1016/s0378-7206(01)00100-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A federation–agent–workflow simulation framework for virtual organisation development<sup>\$</sup>

Hai Zhuge<sup>a,b,c,\*</sup>, Jian Chen<sup>a</sup>, Yulin Feng<sup>c</sup>, Xiaoqing Shi<sup>d</sup>

<sup>a</sup>School of Economics and Management, Tsinghua University, Beijing 100084, PR China

<sup>b</sup>Software Division, Institute of Computing Technology, Chinese Academy of Sciences, Beijing 100080, PR China

<sup>c</sup>Laboratory of Computer Science, Institute of Software, Chinese Academy of Sciences, Beijing 100085, PR China

<sup>d</sup>Department of Systems Ecology, Centre of Eco-Environment Science, Chinese Academy of Sciences, Beijing 100080, PR China

Received 10 January 1999; received in revised form 20 December 2000; accepted 11 April 2001

## Abstract

Traditional information system development approaches separate the domain model from the system model and then focus on the transformation between them. They are not, however, useful in rapid development of virtual organisations. This paper proposes a simulation-based development framework for establishing such organisations. It consists of a federation–agent– workflow (FAW) model, a set of rules for establishing the mapping from the domain into the virtual organisation, a set of management services, and a macro development process. Basic elements of the model are agents, which can perform active domain behaviour, and they are organised as autonomous federations. Agents within the same federation perform relevant tasks according to an overall workflow. Domain organisation is simulated by the multi-level agents whose behaviour are driven by a nested-workflow mechanism. The framework unifies the traditional domain organisation and information system model into a virtual organisation model, and this allows users to develop intuitive virtual organisations from the viewpoint of the domain. A comparison between the framework and the traditional information system approaches shows that the framework provides a simpler development process, so it meets the needs of virtual organisations for rapid and mobile development. <sup>#</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Agent; Domain modelling; Federation; Information system development; Virtual organisation

## 1. Introduction

Currently, enterprises are facing the challenges from a fast changing production environment (due to such factors as market, technology, etc.), needs to reducing costs, globalisation of mass customisation, visualised management, and a move to individualised and conceptualised products [20]. With the rapid development of the Internet, the demands for establishing virtual organisations are increasing [9,10,23]. A virtual organisation can be described as a group of network-based systems that can simulate the structure and behaviour of the real domain organisations, and quickly and actively exploit fast-changing business opportunities. The domain organisation herein refers to either a real-world organisation or a conceptual organisation that did not exists in the real world before development. Compared with conventional information systems, virtual organisations have the following main characteristics: (1) autonomous management, virtual organisation can run according to predefined tasks and management rules; (2) active behaviour, any member can actively perform its task according to their own decision; (3) intuitiveness, virtual organisation is the simulation of the domain organisation; (4) adaptability and agility, virtual organisation can adapt to the changes in the domain organisation.

The information infrastructure framework for virtual organisation management provides information exchange among the virtual organisation, its customers, and the general support techniques and approaches [21]. Besides the information structure, the system architecture and the development approaches are the keys to the implementation of a virtual organisation. The strategies for planning the information system of decentralised organisations with autonomous subdivisions and functional units were investigated in [24].

The traditional information system development approaches are the ways to develop a virtual organisation, but these approaches model the domain business from the (software or hardware) system point of view, and it requires the users and the developers to be familiar with the domain, the development approach used, and the software system. The prototyping approach focuses on the evolution of the system from the system point of view. But users have to understand the system architecture, concepts, functions, and evolution from the system point of view. The structured approach separates the domain model from the system model and then focuses on the transformation between them through several stages; this results in a long development period, rigid development process, high cost, and the difficulty of understanding the specifications at different stages and the transformations between the specifications.

Object-oriented approach uses an uniform ‘‘object’’ point of view to conceptualise the domain and the software systems. Graphical notation languages, such as UML [4], are used for establishing the domain model. Unfortunately, these languages are more suitable for developers. Domain users are seldom familiar with them. Besides, software tools are needed to assist the transformation from the system specification into an operational system.

In the simulation field, a general high-level architecture (HLA) has been proposed for developing the simulation systems [13]. A federation concept is defined as an autonomous domain object set that is to be used to simulate the real-world organisation. The behaviour simulation is supported by a run-time infrastructure. The purpose of the HLA is to facilitate the inter-operability between the simulation components and to promote their reusability. However, the objectbased federation mechanism cannot reflect the active behaviour and the dynamic relationships between the behaviour.

An agent technique can be used to simulate the active behaviour. Besides its object-orientation, an agent can actively perform tasks. Agent was formally described as automata in [11]. Communication languages like KQML were proposed for communicating between multiple agents [7,18]. The co-operations and negotiations in the multi-agent environments as well as the time constraints have been investigated [12]. Agents can also be used to model qualitative decisionmakers [6]. The temporal coherence problems in the multi-agent systems have been investigated [5]. In the software development field, the agent concept has also been used to establish a dynamic system model [16], but such development models are defined from the viewpoint of software.

The main intent of this paper is to form a framework that can support the rapid, intuitive, and mobile development of virtual organisations from the domain point of view. We use a federation hierarchy to model the domain organisation architecture, use the agent mechanism to model the active domain behaviour, and use the workflow mechanism to model the control of the domain behaviour. Every basic federation consists of a set of related agents. Any agent actively performs its task according to the federation task, the intra-federation (inter-agent) workflow, and the intraagent workflow. A nest-workflow is used to reflect the different-level work co-operation of the virtual organisation, and it is responsible for driving the multilevel virtual organisation to implement the tasks in the predefined logical order and temporal order.

## 2. Federation–agent–workflow virtual organisation

## 2.1. Model description

The federation–agent–workflow (FAW) virtual organisation model aims at the modelling of the architecture and the execution of the domain organisation, where the organisation members are tightly coupled. The FAW virtual organisation carries out the federation level management modelling, the agent-level behaviour modelling, and the object-level structure modelling from high to low. The federation herein refers to the large-granularity and autonomous unit of the virtual organisation. The federation members have interdependent tasks, and share common interests, a common communication language, and common play-rules.

The federation level is the modelling of the multilevel organisation management. It is a hierarchy of federations. Each basic federation of the hierarchy consists of a federation manager, a set of member agents, and a set of federation responsibilities. The federation manager is a kind of agent that is responsible for: communicating with the other federations, planning the federation task, managing the member agents, and monitoring the member agents’ behaviour according to the federation responsibility. The federation responsibility is defined at the design stage and contains the scope of the federation task, the autonomous rules, and the restraints. The federation responsibility should be accessible to the federation manager and every member agent. The high-level federation manager is responsible for the task planning, the behaviour coordination, and the membership management of its member federations. The restraints on the high-level federation should be compatible with that of its member federations.

The agent level is the modelling of the active domain objects. A basic federation consists of a group of agents, each of which simulates a set of active behaviour. An agent has an interface, a reasoning mechanism, a rule set, and an agent-responsibility set. The interface is a mapping from input to output. The agent receives tasks through its input. The output is a set of behaviour related to the following: the input, the reasoning result, and the agent-responsibility. The agent-responsibility set defines its task scope, which should be compatible with the responsibilities of its federation. A responsibility can be described by a mapping: ConditionSet ! BehaviourSet, where the involved condition and behaviour include a time interval restraint [14]. The agent’s reasoning mechanism will check whether a task to be received is within the scope of its responsibility. Once a task is accepted, the agent needs to declare this to its manager.

The object level is the modelling of the domain passive objects (e.g. the office facilitates). The passive objects are organised as classes. Inheritance relationships form the inheritance hierarchy between the classes [26]. To reflect the time factor, the attributes of a class can be represented as $( \mathrm { A } _ { 1 } ( t _ { \mathrm { b } } , t _ { \mathrm { e } } ) , \ldots ,$ $\mathbf { A } _ { n } \big ( t _ { \mathrm { b } } , t _ { \mathrm { e } } \big ) \big )$ , where $t _ { \mathrm { b } }$ and $t _ { \mathrm { e } }$ denote the beginning and the ending of an effective time interval. An agent can own several passive objects, and the ownership can be transferred from one agent to another within the same federation by the federation manager.

The execution of the virtual organisation is controlled by three inter-related workflows. An interfederation workflow defines and controls the process logic of the implementation of the federation tasks. An inter-agent workflow defines and controls the process logic of the implementation of the agent-tasks. An intra-agent workflow defines and controls the agent’s activities for implementing its task. The basic FAW virtual organisation can be described as

FAWVirtualOrganisation::¼hFederationSet, Inter-FederationWorkflowi;

FederationSet::¼{hBasicFederationi}|

(FederationManager, FederationSet, ObjectSet, FederationResponsibilitySet, InterFederation-Workflow, RestraintSet);

BasicFederation::¼(FederationManager, AgentSet, ObjectSet, FederationResponsibilitySet, InterAgentWorkflow, RestraintSet);

Agent::¼(Interface, ReasoningMechanism, Rules, AgentResponsibilitySet, IntraAgentWorkflow, RestraintSet).

## 2.2. Mapping from domain organisation into virtual organisation

Both the real-world domain organisation and the conceptual organisation can be generalised as a multidivisional hierarchy architecture. The left portion of Fig. 1 shows such a architecture. A high-level division manages several low-level divisions. The basic divisions manage the active objects (shown as $\mathbf { A } _ { i }$ in Fig. 1), which can own the passive objects like tools, machines, and office facilities (shown as $\mathrm { P } _ { i }$ in Fig. 1).

The difference between a real domain organisation and its computerised virtual organisation involves a mapping. This is carried out at the same abstraction level, and keeps the virtual organisation architecture and the domain organisation architecture in synchronisation. The rules for establishing the mapping can help the designers to describe the virtual organisation. Six basic elements of the rule set are as follows.

![](/api/attachments/VFN667DU/fulltext/images/3ef1529fdb61c088290f40f205f996ee15afea812bdd2570f71ac1051b113265.jpg)  
Fig. 1. Mapping from domain organisation into FAW virtual organisation (D: division; A<sub>i</sub>: active object; P<sub>i</sub>: passive object; F: federation; SF: super-federation; —: ownership; : mapping).

M\_Rule 1: Map the passive objects of the domain organisation into the object classes of the virtual organisation.

M\_Rule 2: Map the active objects and their active behaviour of the domain organisation into agents and behaviour.

M\_Rule 3: Map basic divisions and their responsibilities of the domain organisation into basic federations and their responsibilities.

M\_Rule 4: Map the divisional hierarchy of the domain organisation into the federation hierarchy of the virtual organisation. If a federation F is the mapping image of a division D, then the direct member of F should be the mapping images of the direct members governed by D. M\_Rule 5: Map the business processes of the divisions of the domain organisation into the federation workflows of the virtual organisation.

M\_Rule 6: Map the ownership relationship between the active object and the passive object of the domain organisation into the ownership relationship between the corresponding agent and the object class of the virtual organisation.

Fig. 1 shows a mapping from the domain organisation into the FAW virtual organisation. The arrows denote that the mapping satisfy the mapping rules.

A proper mapping must satisfy the mapping restraint set. The six basic elements of the set are as follows.

M\_Restraint 1: A member agent can only interact with agents within the same federation. Every member agent can receive the tasks through its manager.

M\_Restraint 2: A federation manager can only manage its member agents.

M\_Restraint 3: A federation manager can only interact with the other federation managers in the same uplevel federation.

M\_Restraint 4: Passive object classes should be related by the inheritance relationships.

M\_Restraint 5: Every domain organisation division should have a corresponding federation image in the virtual organisation.

M\_Restraint 6: The construction of a FAW virtual organisation should be carried out top–down.

The first three of these guarantee the autonomous character of the federation.

## 2.3. Implementation architecture

The implementation architecture of the virtual organisation consists of an operational virtual level and a virtual-support level as shown in Fig. 2. The operational virtual level consists of the GUI of the federation organisation, the class repository, and the communication medias. Every federation of the virtual organisation consists of several member agents or several low-level federations. The class repository can be classified into several categories such as the passive object, the interaction, and the common rules. The ownership is denoted as the solid lines marked ‘own’ in Fig. 2. The communication between the agents is realised through ‘publish’ and ‘subscribe’ behaviour. Any agent can subscribe to suitable medias so as to read the required messages during the task implementation process; it can also publish messages in the predefined medias (such as magazine structure and table structure) according to its responsibility. The magazine structure can be described as follows:

![](/api/attachments/VFN667DU/fulltext/images/fdfb4a2e3c07595a94ed670af2f2087c9edab228792f7183f269002d89574fe9.jpg)  
Fig. 2. Architecture of a FAW virtual organisation (F: federation; FO: federation organisation; A : agent; : work relationship; : logical dependence relationship).

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Magazine::=(Version, Chapter);
Chapter::={Message} $^{+}$ ;
Message::=(Title, Author, Task, TimeStamp, Status).
</div>

The virtual-support level supports the execution and the management of the federation organisation. It consists of a run-time support mechanism and a behaviour service repository. The commonly used services that implement the agents’ behaviour are stored in the behaviour service repository. Behaviour is managed and performed by the run-time support mechanism, which consists of mechanisms for driving, monitoring, and managing the virtual organisation like the workflow engine [25]. These mechanisms allow the system designers to concentrate on the virtual-level design. To increase the reusability, the agent behaviour is implemented with the support of the existing services in the repository. The new service design is carried out at the design stage. Any agent needs to declare to the runtime support mechanism (the solid arrow marked ‘declare’ in Fig. 2) and get its grant before it can behave.

Task representation can help a federation manager to plan tasks and to distribute the sub-tasks to its members, and then to monitor the implementation of these sub-tasks. A task can be described by a form with the following features: the TaskName reflecting the appropriate task category [3]; the ‘Signature representing the mapping between the input and output of the task, where the input and output type can take the form of the Cartesian product of n types; the ‘Behaviour’ describing: the general function of the task, the background and the purpose of the task, and a set of behaviour identifiers; the ‘SubTask’ representing the list of SubFrames(SubFrameIDList); the ‘Condition’ representing the pre-condition of implementing the task; and, the ‘Restraint’ representing a set of equations about the variables appearing in the signature and in the time restraint.

TaskName: [Signature: InputType ! OutputType; Behaviour: (TextDescription, BehaviourSet); SubTask: SubFrameIDList;

Condition: Condition $_ 1 \wedge \cdots \wedge$ Condition<sub>n</sub>; Restraint: I/O and time restraint].

The structure of the complex task can be represented by a hierarchy of such frames. The root of the hierarchy describes the general task, and the different level nodes of the hierarchy describe the different level sub-tasks. The restraints of the general task should be compatible with those of its sub-tasks.

## 3. Management mechanism

## 3.1. Nest-workflow drive

To manage the inter-related workflows of the virtual organisation, we herein extend the concept of the task (activity) node of the conventional workflows [15] to a kind of ‘nest’ node, which can be either an agent or a workflow. Such a workflow is called nest-workflow. A nest-workflow consists of multiple workflow levels corresponding to the FAW virtual organisation. In case of multiple federation levels, every node within a high-level federation corresponds to a low-level workflow. The execution of the virtual organisation is distributed onto different level federation workflows. Fig. 3 shows an example of a threelevel nest-workflow.

A nest-workflow should guarantee three kinds of consistency. The first is temporal consistency, i.e. the time restraint of a nest-node should be consistent with its direct low-level workflow. This implies that the duration of the nest-node execution should be the same as that of its direct low-level workflow, and the restraint of the beginning and end times of a node execution should be consistent with those of its low-level workflow. The second is consistency between the responsibility and the task. A task can only be assigned to the member agent or to the federation whose responsibility is compatible with the restraint of that task. The third is I/O consistency. The initial input flow and the final output flow of a low-level workflow should be the same as the input flow and the output flow of its direct up-level node.

## 3.2. Time management

The time management of the nest-workflow concerns the virtual and run-time support level. At the virtual level, any agent needs to regularly check the current standard time and to compare it with the system’s logical time. The agent will start to plan its behaviours for implementing the task only when the logical time is consistent with the standard time and satisfies the time restraint. The federation manager needs to check the time duration of its workflow during the run-time [28].

![](/api/attachments/VFN667DU/fulltext/images/a5fb0ca86bdad714f7e2a8d87336cd61d4f231f5049646497cc4c4957f458039.jpg)  
Fig. 3. A three-level nest-workflow $( \mathrm { A } _ { i j } { \mathrm { : } }$ agent belongs to $\operatorname { F } _ { i } ; \operatorname { F } _ { i } :$ federation; $\operatorname { S F } _ { i } \colon$ super-federation; : logical dependence relationship; —: nest relationship).

At the run-time support level, the time management is realised through four kinds of services. The first is time planning services, which support the time duration computation before and during the task implementation so as to guarantee that a task will finish within the time duration restraint. The second is time advancement control services, which are responsible for driving the behaviour of the virtual organisation and for changing the state of the classes. The third is message ordering and synchronisation services. The fourth is time monitoring services, which work during the whole execution process of the virtual organisation. The timed workflow model [17] provides a basis for the computation of the time duration of a nest-workflow.

A time management restraints set specifies the time restraints of the virtual level and the run-time support level. In the following, we show four restraints of the set. The first two specify the agent behaviours, while the next two specify the behaviour of the run-time support mechanism.

TM\_Restraint 1: All the agents of the virtual organisation should obey the unified time advancement.

TM\_Restraint 2: An agent starts to implement its task only after receiving permission from the run-time support mechanism.

TM\_Restraint 3: The run-time support mechanism should grant permission for a time advancement T only when it can guarantee all the timed messages with the time stamps less than T have been delivered to the agent.

TM\_Restraint 4: The run-time support mechanism must compute the low-bound of the time stamp for future messages that will be received by the agent. This can guarantee that the timed messages are delivered to the agent in the time stamp order.

## 4. The development of the virtual organisation

## 4.1. The development process

The process of developing a virtual organisation includes the following steps.

Step 1: Define the domain organisation as a multidivisional organisation. Organisation optimisation is encouraged at this step.

Step 2: Map the domain organisation into the FAW virtual organisation according to the mapping rule set. Step 3: Define the media structure (can be the magazine, the blackboard, or the table structure) for establishing the communication relationship between the agents.

Step 4: Design the agents of every federation. Since agents can have the same internal structure, a new agent can be generated through inheriting its attributes from a general agent frame structure and then appending the individual contents. An agent’s individual content includes: the time regular behaviour, the ECA (event–condition–action) rules, the restraints, and the responsibilities.

Step 5: Design the specific services, and then append them to the run-time support mechanism.

The design of the virtual organisation should obey a set of design rules. Two basic elements of the set are as follows.

Design rule 1: The interface design of the behaviour services should follow a unified specification (e.g. HLA [2]). The rationale is to raise the reusability of the services.

Design rule 2: The time advancement step should be fixed during the life cycle of the virtual organisation development and cannot be changed by any agents.

## 4.2. Application

The proposed framework can be used to establish the virtual organisations of many fields, for example, (1) it can be used to expand a small company to a large Internet-based virtual company with more business without increasing its employees and office facilities, (2) it can be used to set up a temporary joint virtual company controlled by several companies to rapidly catch business opportunities, (3) it can be used to simulate production operations when planning a new plant, (4) it can be used to establish an unified global company, e.g. a virtual global company for raising the production rate has been set up and is in operation [22], (5) it can be used as a tool for domain organisation re-engineering and (6) it can be used to simulate inter-organisational supply chain modelling.

Example. The conceptual organisation consists of a group of sellers and a group of customers. The sellers can look for the customers. Any seller can negotiate the price with the buyer. The buyers can look for the suitable sellers and then make the buying contracts. Any buyer will compare the prices of the goods sold by different sellers before making the contract. The development process of the corresponding virtual organisation mainly consists of the following five steps.

Step 1: Define the conceptual domain organisation as shown in the left part of Fig. 4. It consists of a shop and several customers. The shop has a manager and several sellers. The customers buy goods from the sellers at the negotiable prices. The two-way arrows in Fig. 4 represent the negotiation.

Step 2: Map the conceptual organisation into the virtual organisation as shown in the right part, and then establish the agent-frames for the buyer and the seller. We herein discuss the case of having one buyer and a stable seller federation with two sellers and a manager.

Step 3: Establish the tables for the inter-operation among the agents. Any buyer can publish the customers’ requirements in the requirement table that records the message about the customers’ name, the required goods, the acceptable prices, the producers, and the time restriction. Any seller can publish the selling information in a selling-table. The buyer defines this table, and the seller provides the requirementtable.

Step 4: Design agents. Depending on the different behaviour requirements, agents can be created by appending the individual contents to a frame that is a copy of the general agent frame. A buyer can buy goods for multiple customers, negotiate the prices with the seller, make decisions, and then form the contracttable. Any seller agent can publish the sold information in a sold-table that has the same structure as the selling-table. The solid lines and the dashed lines between the agents and the tables represent the ‘publish’ and the ‘subscribe’ relationship, respectively.

Step 5: Design the special services and append them to the behaviour repository at the implementation level. The design of the services should make full use of the existing methods, e.g. the negotiation service can be realised by using the conflict analysis approach [8].

![](/api/attachments/VFN667DU/fulltext/images/49f7c5c2dc8380513a8c0e048d590981382852fcd8324667602f5b6c00b57da2.jpg)  
Fig. 4. The virtual organisation development example (- - -: publish or subscribe operation; : negotiation).

![](/api/attachments/VFN667DU/fulltext/images/22baf7b46a91e06c7af322c251be7267fbd42f44a516711f02249f229becf538.jpg)  
Fig. 5. Comparison between the proposed approach and the traditional approach ( : work relationship; : transformation between specifications; : inter-operation; : mapping).

## 5. Comparison and discussion

## 5.1. Comparison

The comparison between the proposed approach and the traditional information system development approach is graphically shown in Fig. 5. The traditional approach can be generalised as a multi-step transformation process from the domain requirement specification into the final system shown on the right side. The final system has to use computerised concepts and process controls, which are quite different from the domain concepts and business processes. Since the system architecture is different from the domain organisation architecture, users need to consult the designers frequently to be able to understand the system concepts and to know how to operate the system. Designers have to work at four levels: the domain, the requirement specification, the design specification, and the system implementation. Five dashed two-way arrows represent these work relationships. On the other hand, the traditional approaches are too rigid to adapt to the changes of the domain business. Once the domain business has changed, the system has to be re-designed.

The proposed approach concerns three levels: the domain, the virtual, and the implementation shown in the left part. The virtual level is the direct simulation of the domain organisation. The architecture of the virtual organisation is isomorphic to the architecture of the domain organisation, and the concepts and the processes used in the virtual organisation are the same as or similar to these domain concepts and processes. So users can easily understand the concepts and architecture of the virtual organisation, and can operate the system without the need to frequently consult the designers. The virtual level is separated from the implementation level that consists of a runtime support mechanism and a behaviour repository. The designers can concentrate on the analysis of the domain organisation and the mapping from it into a virtual organisation. Users (or designers) can edit the FAW virtual organisation when necessary and can execute it to check the organisation behaviour intuitively. Usually, the designers only need to work with the domain level and the virtual level from the domain viewpoint. At the implementation level, only the domain-specific services need to be designed. Three dashed two-way arrows in the left part represent the works related to the designers. The implementation level supports the execution of the virtual-level organisation. On the other hand, the proposed virtual organisation is adaptive. In case of change of domain businesses, only the relevant (intra-federation) workflows need to be updated by making the mapping again at the virtual level. The other parts of the virtual organisation and the implementation level can be kept unchanged.

The comparison shows two results: one is that the proposed approach needs less design work than the traditional approaches do, another is that the proposed approach can adapt more easily to the changes of the domain business.

## 5.2. Discussion

The virtual organisation development process involves human cognitive and problem-solving. People have the tendency to use existing methods to solve new problems. Unfortunately, the role of human cognition is often neglected in traditional software development approaches. A cognitive-based software process model can unify the software process and the developers’ cognitive process [27]. The model provides a way to improve the software process through enhancing the cognitive skill. The framework can be regarded as a kind of component-based development [3]. Virtual components (refer to the federations and agents of the proposed framework) are used for simulating the architecture and the behaviour of the domain organisation.

The loosely coupled inter-organisational workflow has been investigated in [1]. The framework of this paper used the nest-workflow to describe the dynamic behaviour of the multi-level virtual organisation. Since the federations are autonomous, there does not exist such a flow across two federations at the same level. The development of a virtual organisation should also consider the following: the operational cost characteristics, the software environment characteristics, the simulation software output characteristics, the organisational support characteristics, the initial investment cost characteristics, and the task characteristics as discussed in [19].

## 6. Summary

The proposed virtual organisation development framework consists of the FAW virtual organisation model, the rule set for establishing the mapping between the domain organisation and the virtual organisation, the implementation architecture of the virtual organisation, the virtual organisation management service set, and the macro development process. The main contribution includes three aspects. First, we unify the domain model and the system model into the virtual organisation model through simulation. This can bring four advantages: (1) the development process is simpler than the traditional information system development process; (2) the development work can be raised from the system (software and hardware) level up to the domain level, domain users can easily understand the concepts, the architecture, and the execution process of the system being developed, this can reduce the difficulty of the communication between the domain users and the designers during the development process, such a difficulty often occurs when using the traditional approaches; (3) the virtual organisation provides an intuitive vehicle for studying the domain organisation such as organisation optimisation and re-engineering, behaviour verification, evaluation, and estimation and (4) the virtual organisation can adapt to the changes of the domain business. Second, we proposed a new approach for domain modelling through integrating the federal management approach, the nestworkflow, and the agent mechanism. This enables the virtual organisation model to simulate the autonomous characteristic of domain organisations, the active individual behaviour, the temporal order and dependence order relationships between the behaviour. Third, we established the development framework to support the rapid and mobile development of the virtual organisation.

## Acknowledgements

The authors thank the editor and the anonymous referees for their helpful comments on the earlier version of this paper.

## References

[1] W.V.D. Aalst, Loosely coupled inter-organisational workflows, Information and Management 37 (2), 2000, pp. 67–75.

[2] L. Baekgaard, J.C. Godskesen, Real-time event control in active databases, The Journal of Systems and Software 42, 1998, pp. 263–271.

[3] D. Batory, S. O’Malley, The design and implementation of hierarchical software systems with reusable components, ACM Transaction Software Engineering and Methodology 1 (4), 1992, pp. 355–398.

[4] G.Booch, J. Rumbaugh, Unified Method for Object-Oriented Development, http://www.rational.com/ot/uml.html.

[5] V. Botti, F. Barber, A. Crespo, Towards a temporal coherence management in real-time knowledge-based systems, Data & Knowledge Engineering 25, 1998, pp. 247–266.

[6] R.I. Brafman, M. Tennenholtz, Modelling agents as qualitative decision makers, Artificial Intelligence 94, 1997, pp. 217–268.

[7] M.A. Covington, Speech acts, electronic commerce, and KQML, Decision Support Systems 22, 1998, pp. 203–211.

[8] N.M. Fraser, K.W. Hipel, Conflict Analysis: Model and Resolution, Elsevier, New York, 1984.

[9] R. Grenier, G. Metes, Going Virtual: Moving Your Organisation into the 21st Century, Prentice-Hall, Englewood Cliffs, NJ, 1995.

[10] R. Kalakota, A.B. Whinston, Intraorganisational Electronic Commence, Frontiers of Electronic Commence, Addison-Wesley, Reading, MA, 1996.

[11] S. Kraus, Negotiation and cooperation in multi-agent environments, Artificial Intelligence 94, 1997, pp. 79–97.

[12] S. Kraus, J. Wilkenfeld, G. Zlotkin, Multiagent negotiation under time constraints, Artificial Intelligence 75, 1995, pp. 297–345.

[13] DoD (Department of Defense, USA), HLA Standard, http:// www.dod.dmo.hla, 1998.

[14] J.Y. Lee, R. Elmasri, J. Won, An integrated temporal data model incorporating time series concept, Data & Knowledge Engineering 24, 1998, pp. 257–276.

[15] F. Leymann, D. Roller, Workflow-based applications, IBM Systems Journal 36 (1), 1997, pp. 102–122.

[16] Q. Li, F.H. Lochovsky, ADOME: an advanced object modelling environment, IEEE Transactions on Knowledge and Data Engineering 10 (2), 1998, pp. 255–276.

[17] O. Marjanovic, M.E. Orlowska, On modelling and verification of temporal constraints in production workflows, Knowledge and Information Systems 1 (2), 1999, pp. 157– 192.

[18] J. Mayfield, Y. Labrou, T. Finin, Evaluation of KQML as an Agent Communication Language, http://www.cs.umbc.edu.

[19] R. McHaney, T.P. Cronan, Toward an empirical understanding of computer simulation implementation success, Information and Management 37 (3), 2000, pp. 135–151.

[20] T. Rose, Visual assessment of engineering processes in virtual enterprises, Communications of the ACM 41 (12), 1998, pp. 45–52.

[21] T.J. Strader, F.R. Lin, M.J. Shaw, Information Infrastructure for Electronic Virtual Organisation, Decision Support Systems 23, 1998, pp. 75–94.

[22] R. Vadon, P. Cutting, EDGE-Virtual Companies, VNU Business Publications, available from http://www.vnu.co.ulc/ hc/pvw/cut2 2.htm, 1996.

[23] M. Turoff, Virtuality, Communication of the ACM 40 (9), 1997, pp. 30–37.

[24] R.L. Wexelblat, N. Srinivasan, Planning for information technology in a federated organisation, Information and Management 35 (5), 1999, pp. 265–282.

[25] WfMC, The Workflow Reference Model, http:// www.wfmc.org.

[26] H. Zhuge, Inheritance rules for flexible model retrieval, Decision Support Systems 4 (22), 1998, pp. 379–390.

[27] H. Zhuge, J. Ma, X.Q. Shi, Abstraction and analogy in cognitive space: a software process model, Information and Software Technology 39 (7), 1997, pp. 463–468.

[28] H. Zhuge, T.Y. Cheung, H.K. Pung, A timed workflow process model, Journal of Systems and Software 55, 2001, pp. 231–243.

![](/api/attachments/VFN667DU/fulltext/images/1a839675866a82ae06d8814c68486107f42a997bcfb6513796abbd5681fa9993.jpg)

Hai Zhuge is a Professor at the Institute of Computing Technology, Chinese Academy of Sciences. He was a postdoctoral fellow and then the Associate Professor at the Institute of Software, Chinese Academy of Sciences. He received the PhD in Computer Science from Zhejiang University, China, in 1992. He had been worked in the City University of Hong Kong, the National University of Singapore, and the Tsin-

ghua University as a research fellow or a senior visiting fellow. His current research interests include: problem-oriented model base systems, component reuse, cognitive-based software process model, inter-operation model for group decision, and web-based workflow model. He is now the principle investigator of two NSF grants in China. His publications appeared mainly in IEEE Transactions on Systems, Man, and Cybernetics, Decision Support Systems, Information and Management, Journal of Systems and Software, Knowledge-Based Systems, Information and Software Technology, and Chinese Journal of Advanced Software Research.

![](/api/attachments/VFN667DU/fulltext/images/a5fee342084cdc80fa9726408f8a9c99b766ab28b7a597a634909c64dd331f6c.jpg)

Jian Chen is a Professor and the head of the Management Science Department, Tsinghua University. He received the PhD in Systems Engineering from Tsinghua University. He is a senior member of IEEE and serves as a member of the administrative committee of IEEE Systems, Man and Cybernetics Society. He was the co-chair of the IPC of the 1998 International Conference on Systems Science and Systems Engineering. Prof.

Chen has over 90 technical publications and has been a principal investigator for over 20 grants or research contracts with National Science Foundation of China, government, and companies. His research interests include supply chain management, E-commerce, modelling and control for complex systems, decision support systems and information systems, forecast and optimisation techniques.

Yulin Feng is the Director of the Institute of Software, Chinese Academy of Sciences. He received the PhD in Computer Science

from the Institute of Computing Technology, Chinese Academy of Sciences in 1982. He visited Stanford University and Carnegie Mellon University as a post-doctoral research scientist from 1982 to 1985. He was a professor at the Department of Computer Science, University of Science and Technology of China from 1986 to 1991. Currently, he is an Executive Director of China Computer Federation, Vice-Chairman of China Software Industry Association, and Editorin-Chief for Chinese Journal of Software. His research interests include object-oriented systems and languages, distributed network computing, mobile agents and computation, system specification and modelling, software engineering methods and environments.

Xiaoqing Shi is an Assistant Professor at the Department of Systems Ecology, Centre of Eco-Environment Science, Chinese Academy of Sciences. She has published seven papers in the refereed journals including Information and Software Technology, Information and Management, and IEEE Transactions on Systems, Man, and Cybernetics.
