---
otero_id: 8892
otero_key: "5ZA3QZ4K"
title: "Agile Integration Modeling Language (AIML): A conceptual modeling grammar for agile integrative business information systems"
authors: "Hong Zhang; Rajiv Kishore; Raj Sharman; Ram Ramesh"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.04.009"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Decision Support Systems 44 (2007) 266– 284

www.elsevier.com/locate/dss

# Agile Integration Modeling Language (AIML): A conceptual modeling grammar for agile integrative business information systems ☆

Hong Zhang <sup>a,1</sup>, Rajiv Kishore <sup>b,⁎,2</sup>, Raj Sharman <sup>b,2,3</sup>, Ram Ramesh <sup>b,4</sup>

<sup>a</sup> Computer Information Systems, Glass Hall 376, Missouri State University, 901 S National Ave, Springfield, Missouri 65897, United States <sup>b</sup> Department of Management Science and Systems, School of Management, The State University of New York at Buffalo, Buffalo, NY 14260-4000, United States

Received 7 February 2006; received in revised form 16 March 2007; accepted 23 April 2007 Available online 13 May 2007

## Abstract

The proliferation of newer agile integrative business information systems (IBIS) environments that use the software agent and the multiagent systems paradigms has created the need for a common and well-accepted conceptual modeling grammar that can be used to efficiently, precisely, and unambiguously, model agile IBIS systems at the conceptual level. In this paper, we propose a conceptual modeling grammar termed Agile Integration Modeling Language (AIML) based on established ontological foundation for the multiagent-based integrative business information systems (MIBIS) universe. The AIML grammar provides adequate and precise constructs and semantics for modeling agile integration among participating work systems in terms of quickly building and dismantling dynamic collaboration relationships among them to respond to fast-changing market needs. The AIML grammar is defined as a formal model using Extended BNF and first order logic, and is elaborated using a running example in the paper. The grammar is also evaluated in terms of its syntactic, semantic, and pragmatic qualities and is found to exhibit a high degree of quality on all these three dimensions. In particular, the pragmatic quality of AIML measured in terms of grammar complexity evaluated using complexity metrics indicates that AIML is much easier to learn and use as compared to the Unified Modelin Language (UML) for modeling agile integration of work systems in organizations. © 2007 Elsevier B V All rights reserved

Keywords: Conceptual modeling grammar; Systems modeling; Requirements specifications; Role-based modeling; Multiagent systems modeling; Integrative business information systems modeling

## 1. Introduction

Information systems have been playing an important role in supporting business integration. Traditional integrative business information systems (IBIS) [18,19] such as ERP, EAI, and workflow management systems have brought significant benefits to businesses in terms of improved planning, timely deliveries, reduced inventories, reduced costs, and responsive and improved customer service [19]. However, they take significant amounts of time and effort to develop as all their component work systems<sup>5</sup> are tightly coupled to each other. Tight coupling also results in difficulties in adding new and modifying or deleting existing collaborative relationships among participating work systems. On the other hand, current hypercompetitive business environment requires business organizations to quickly build as well as dismantle dynamic collaboration relationships among various participating work systems, both internally and externally, to respond to fast-changing market needs.

Consequently, newer agile IBIS systems<sup>6</sup> should allow participating work systems to integrate with each other while preserving their local autonomy and coordinating in a decentralized manner. In an agile IBIS system, we envision no overall control over participating work systems and integration occurs through dynamic coordination among the participating work systems, in addition to the necessary integration at the technology and data levels [19]. In such a scenario, business processes are rather dynamic and emergent, relying on the judgments and decisions of individual work systems. To achieve this type of integration, an IBIS system should allow participating work systems to reach agreements about service contracts on their own without central control. Further, users and developers should be able to configure various business processes and collaboration relationships among work systems dynamically as the goals and needs of the organization change.

Recently, multiagent systems comprising of collaborating software agents have emerged as a new technology to solve complex problems in a distributed environment [40]. A software agent is “a computer system that is situated in some environment, and that is capable of autonomous action in this environment in order to meet its design objectives” [41]. An intelligent software agent within a multiagent system is autonomous (i.e., it acts without human intervention), reactive (i.e., it responds to events in the environment), proactive (i.e., it is goaldirected), and social (i.e., it interacts with other software agents to get what it needs) [41].

The multiagent systems paradigm has a number of parallels with the IBIS paradigm as noted in earlier work [19]. Further, due to their dynamic coordination and collaboration capabilities, software agents in multiagent systems are uniquely capable of supporting integration in agile IBIS systems as they provide flexibility in resolving inconsistencies and dependencies involved in work systems coordination. Further, software agent as a modeling paradigm minimizes the semantic gap between work system coordination and information system modeling [14]. As a result, software agents have been adopted by a number of researchers in various IBIS applications such as e-commerce [e.g., [16,28]], business process management [e.g., [15,21]], supply chains management [e.g., [12,33]], enterprise integration [e.g., [22,32]], and manufacturing [e.g., [10,20]] to create more agile integrative environments.

This proliferation of newer agile IBIS environments that use the software agent and the multiagent systems paradigms has created the need for a common and wellaccepted conceptual modeling grammar that can be used to efficiently, precisely, and unambiguously, model agile IBIS systems. This is because existing modeling grammars such as ERD, object-oriented techniques, and business process modeling techniques lack requisite capabilities to model autonomy, intelligence, and agile coordination and collaboration that are central to agile IBIS systems. Most agent-oriented systems development methodologies also do not have conceptualmodeling-level constructs formally defined with unambiguous semantics. Further, researchers and designers that apply the software agent principles and concepts in various agile IBIS applications have defined their own unique and application-specific constructs and rules for conceptual modeling of agile IBIS systems which limits knowledge sharing and reuse in the agile IBIS community and may result in compatibility issues among future IBIS systems. In response to this state of craftsmanship, Kishore et al. [19] synthesized literature in the areas of IBIS systems and multiagent systems with the intent of developing a comprehensive foundation ontology for the universe of Multiagent-based Integrative Business Information Systems (MIBIS) that can become the basis for a sound conceptual modeling grammar for a variety of agile IBIS systems.

We extend Kishore et al.'s work and develop a formal conceptual modeling grammar termed Agile Integration

Modeling Language (AIML)<sup>7</sup> for modeling of agile IBIS systems that belong to the MIBIS universe and utilize the notions and principles of multiagent systems for agile integration. This grammar is defined in ISO/ IEC 14977 Extended BNF [13] and formally specified in first-order logic. AIML facilitates MIBIS modeling in several ways. First, AIML serves as a foundation ontology for MIBIS knowledge representation, which can be shared and reused during the process of system analysis and design. Second, the formally defined AIML constructs serve as templates to be customized and enhanced for individual MIBIS applications. Finally, the rigorous formalism of AIML serves as an analytical tool for developers to detect and avoid possible conflicts in MIBIS modeling.

The paper is organized as follows. In Section 2, we summarize the conceptual framework for the MIBIS universe described by Kishore et al. [19] and discuss the need for a conceptual modeling grammar for this universe. In Section 3, the AIML grammar is elaborated, formally defined, and explained through examples. In Section 4, we evaluate the quality of the AIML grammar. Finally, Section 5 concludes the paper with remarks on some future research directions.

## 2. The MIBIS conceptual framework

MIBIS is an information system that uses software agents to support coordination among multiple work systems. Coordination is defined as “managing dependencies between activities” [24]. In MIBIS, dependencies are resolved through interactions between agents.

Fig. 1 describes the conceptualization of a MIBIS system. Multiple work systems are brought together by a MIBIS to form a business enterprise<sup>8</sup> so they all can contribute to and benefit from the accomplishment of various business goals. Each work system is composed of software agents and information resources. Some agents work as interfaces to interact with other work systems and to exchange information with users and other entities in the MIBIS environment. Agents in MIBIS are intelligent in the sense that they make realtime decisions based on their own knowledge and information. They control what information to share, who to interact with, and how to negotiate in order to maximize their own benefits.

Kishore et al. [19] investigated various modeling paradigms in the IBIS domain and systems development methodologies in the multiagent systems domain to assess their suitability for modeling of MIBIS systems, as conceptualized above. Based on this review and synthesis, they identified a set of eight ontological constructs for MIBIS modeling that are minimally required to model a system efficiently, precisely, and unambiguously in the MIBIS universe. These eight constructs are agent, role, goal, interaction, task, resource,<sup>9</sup> information, and knowledge. Due to length limitations, we only provide a brief discussion about these constructs and a detail elaboration can be found in [19].

Agent is a central construct in MIBIS modeling. From a modeling perspective, agent provides a much higher-level abstraction than the traditional object concept for modeling human actors in business organizations. Unlike objects, agents are able to control their behaviors through their “mentalistic” components such as knowledge, belief, intention, and obligation. In addition, agents engage in conversations instead of singlemessage exchanges in object communications. From a system architecture perspective, multiagent systems provide excellent support for the distributed, decentralized, and complex IBIS environment. As a result, a MIBIS system can mimic the social system to a great extent by introducing the notion of agent into MIBIS modeling.

While agents are transient both in organizations as well as on computer network in the sense that they may join (appear) and leave (disappear), role is a more enduring concept that introduces the organizational view into MIBIS. Business organizations define roles, such as that of a purchase manager, a master technician, etc., as templates for the work these abstract entities will perform and goals they will achieve. In systems modeling, role has been used to decouple business process definitions from concrete resources such as physical individual actors [3], and provides “a new abstraction that can unify diverse aspects of a system” [42]. In this sense, inclusion of the role concept in MIBIS modeling provides the advantages of design focus, reusability, and flexibility. Further, the notion of autonomous and loosely-coupled roles with their own set of tasks provides the necessary capability for achieving agile integration as roles can be added, modified, or removed as necessary to meet dynamic business needs.

![](/api/attachments/5ZA3QZ4K/fulltext/images/6590e8aa76c52c89bf4f9e1f769a8a49900e51de7588f485c465b29431f36e79.jpg)  
Fig. 1. The conceptualization of MIBIS (adapted from Kishore et al. [19]).

A system that supports business integration brings together work systems that share the same overall business goals and contribute towards achieving those goals. In other words, goals provide the raison d'etre for coordination among work systems and, thus, for MIBIS systems. In view of its importance, goal has been identified as an essential concept for capturing user requirements in systems modeling. It is capable of aiding in the elicitation and elaboration of requirements, relating system requirements to organizational and business contexts, clarifying requirements, and dealing with conflicts [43]. Accordingly, information systems developed based on goals are more stable than those based on functions, processes or information structures that often change with time [7]. At the same time, the notion of goals provides another mechanism for achieving integration agility as it is business goals that change in dynamic environments.

One of the central problems in work systems integration is to resolve inconsistencies or conflicts caused by goal dependencies, task dependencies, and resource dependencies. Interaction is one of the basic means for managing and resolving dependencies. Through interactions, agents are able to communicate with each other for sharing resources, checking for task/goal accomplishment, checking for availability of other agents for performing certain tasks, negotiating prices and timelines, subcontracting tasks to other agents, deciding upon future courses of action, and constructing dynamic business processes to reach system goals, etc.

Task is fundamental to business integration and practically all IBIS modeling techniques provide for modeling of tasks, activities, or processes. It is also an essential concept in multiagent systems. Each agent is responsible for performing some tasks to solve problems. Therefore, task is included as a foundation construct for MIBIS modeling.

A variety of information is required by work systems to perform their tasks in order to accomplish their goals. Information exchanges also take place between work systems in integrative business systems to coordinate their activities and resources. Agents require information as inputs in order to make context-dependent realtime decisions to manage and resolve interdependencies. Therefore, information is fundamental to MIBIS modeling.

Knowledge is a personal justified belief of an entity (a human actor or software agent) rather than an absolute and static true belief (for all entities at all times), following recent and prominent viewpoints about organization knowledge [11,26]. Knowledge is fundamental to MIBIS modeling because it represents “mentalistic” characteristics of software agents. Software agents can possess declarative knowledge (know-that) and/or procedural (know-how). Declarative knowledge is what an agent believes about itself, other agents, and its environment, while procedural knowledge represents business rules that control how the agent performs its tasks and interactions. Knowledge is different from information in several perspectives. First, declarative knowledge is context-related, run-time data internal to an agent. Agents have full control of their declarative knowledge. Information on the other hand is external to the agent. Second, through incoming information agents may revise their current beliefs and form new beliefs, thereby adding to, restructuring, or changing their current declarative knowledge. Further, agents make decisions based on their knowledge and not simply based on information. For example, with incomplete information on a competitor's pricing strategy, a sales agent may form a belief that the current price is the lowest price that its competitor will offer and may, thus, offer a 5% discount on the current price to attract a customer. Third, unlike procedural knowledge, information cannot govern agents' behaviors.

As mentioned earlier, in order to model a MIBIS system efficiently, precisely, and unambiguously as well as to facilitate MIBIS knowledge sharing and reuse, there is a need for a formal conceptual modeling grammar that has adequate power to capture and represent the above MIBIS foundational constructs and their semantics. However, there is currently a lack of such a conceptual modeling grammar in the literature. Traditional general-purpose modeling grammars do not capture all the constructs and their semantics that are necessary for the MIBIS universe. Traditional modeling techniques such as ERD and DFD focus only on limited information and process perspectives but ignore a number of behavioral and coordination perspectives. Processoriented techniques such as Petri-nets are primarily oriented towards analysis of task timing and conflict resolution considerations in stable business processes but do not consider interaction and coordination that are essential in agile integrative business systems. Objectoriented modeling techniques may be useful for defining MIBIS specifications in terms of objects, but they provide no explicit support for the agent, role, knowledge, and extended agent interaction concepts. It is, therefore, difficult to model agent knowledge and interactions inherent to MIBIS systems. While several methodologies (e.g., Gaia, MaSE, etc.) exist for multiagent systems analysis and design, they all utilize unique constructs with unique semantics leaving little room for knowledge sharing and knowledge reuse. Further, these methodologies also do not explicitly define the constructs underlying their models and their semantics in a formal manner. Similarly, in the context of IBIS systems, most enterprise and workflow models have been criticized for the lack of essential constructs and semantics to concisely and precisely represent specific activities, tasks, business processes, business goals, and organization structures of a business [29,38]. Thus, there is a need for a new conceptual modeling grammar that can be used to efficiently, precisely, and unambiguously analyze and model at the conceptual level an agile IBIS system in the MIBIS universe. Such a grammar termed Agile Integration Modeling Language (AIML) is formally developed and discussed next.

## 3. The AIML Grammar

The AIML grammar is a further refinement and extension of the MIBIS foundational constructs discussed in §2 above. This grammar formalizes the constructs and defines their representation schema in ISO IEC 14977 Extended BNF and first order logic. Relationships among the constructs and the various constraints are established in the grammar as well. We also provide a simple but comprehensive example of an agile IBIS system for a fictitious online retailer that sells made-to-order computers. We intersperse the example throughout the section to illustrate the grammar. The IBIS systems involves three participating work systems: Sales (for managing orders), Factory (for PC assembly), and Shipping (for order delivery). When the Sales work system receives an order from a customer, it tries to assess from the Factory and Shipping work systems whether they will be able to satisfy the customer’s requirements. If Factory and Shipping systems indicate that the order is not possible to be met, the Sales work system will decline the customer's order. The Sales work system is also responsible for tracking the order status once it is accepted. Our simplified example demonstrates how AIML can help capture and model the agile integration of these three work systems at the conceptual level.

## 3.1. The AIML Fundamentals

As conceptualized in §2 above, the AIML grammar regards a MIBIS system as a goal-oriented, role-centric, and agent-based information system. Corresponding to system development stages, the AIML grammar uses the notion of goal to capture system requirements, uses the notion of role to assign responsibilities for the identified goals and to define coordination mechanisms between work systems to accomplish those goals, and uses the notion of agent to implement roles in MIBIS applications.

As a central concept in MIBIS conceptual modeling, role is the focus of the AIML grammar. In the classic role theory, a role is defined as “a collection of duties and rights” [4]. In AIML, a role is also a collection of duties and rights. Duties of a role in AIML involve performing tasks and interactions. A task is a series of processing acts performed by a single role alone to pursue its goals while an interaction is a series of communicative acts that form a conversation between at least two roles to resolve interdependencies. Where there is no need to differentiate between these two types of acts, we refer to both tasks and interactions as activities. Each role, thus, performs tasks individually and interacts with one or more roles in the system. The rights of a role in AIML pertain to access rights for information that may be required for performing tasks and interactions. A role in AIML also possesses knowledge so it can make decisions that are necessary for the tasks and interactions at hand and thereby achieve its goal. The notion of information is used to model inputs required and outputs generated during the course of task performance by a role. The notion of knowledge is used to represent a role’s, and thereby an agent's, internal beliefs and business rules that govern its behaviors. Fig. 2 depicts these fundamentals in a meta-model of the AIML grammar. In essence, a role provides the complete contextual knowledge and relationship of an agent with all other entities within a MIBIS system. A roles is an abstraction for the tasks it needs to perform and the interactions it needs to have with other roles to achieve its individual goal, the information that it needs to access or it will generate during the course of performance of its tasks and interactions, and the knowledge that it needs for the successful execution of its tasks and interactions and for the successful achievement of its assigned goal. The key features of the AIML grammar are, therefore, role centricity, goal orientation, interaction focus (for coordination), and knowledge encapsulation (for autonomous behavior) and it is these features that allow AIML with the necessary capabilities for modeling agile integration in an effective manner.

Table 1  
Convention of notations used in AIML specifications

<table><tr><td></td><td>Individual</td><td>Collection</td></tr><tr><td>Type</td><td>Bolded lower case letter(s)</td><td>Bolded upper case letter/(s)</td></tr><tr><td>Instances</td><td>Lower case letter(s)</td><td>Upper case letter/(s)</td></tr></table>

## 3.2. Formal Specification of AIML

In this section, we define the AIML constructs as a set of schemas using ISO/IEC 14977 Extended BNF [13]. The relationships, axioms, and constraints which govern the usage of the AIML constructs are defined in first order predicate logic. Table 1 presents the conventions adopted for the notations and symbols used in specifying the AIML grammar. These conventions apply to all the symbols used to explicate the various ontological categories that arise during the specification, namely: instance, collections, types, and collection of types. Table 2 provides an explanation of the symbols used in specifying the AIML grammar. This grammar consists of a collection of (a) AIML constructs (Ψ), and (b) constraints (T). Table 3 unambiguously defines the key AIML constructs in BNF and Table 4 provides a list of predicates that are used in specifying constraints. In the rest of this section, we provide a more detailed explanation of the fundamental AIML constructs along with their constraints and relationships based on theories in both the IBIS and multiagent literatures. During our discussion, we have attempted to avoid trivial axioms and constraints that can be easily reasoned.

![](/api/attachments/5ZA3QZ4K/fulltext/images/9a3f8606192355aed7af604dcaeb5276f4ac85076546740f25c74a1e858abed6.jpg)  
Fig. 2. The AIML fundamental constructs and their relationships.

Table 2  
Symbols used in AIML specifications

<table><tr><td>Notation</td><td>Description</td></tr><tr><td colspan="2">General</td></tr><tr><td> $\Omega$ </td><td>MIBML Grammar where  $\Omega = \{ \Psi, T \}$ </td></tr><tr><td> $\Psi$ </td><td>Collection of AIML constructs  $\Psi = \{ \psi_i : i, ..., n \}$ </td></tr><tr><td> $\psi$ </td><td>AIML Construct</td></tr><tr><td> $T$ </td><td>Collection of constraints  $T = \{ \tau_i | i=1,...,n \}$ </td></tr><tr><td> $\tau$ </td><td>Constraints</td></tr><tr><td> $C_{attributes}$ </td><td>Common attributes</td></tr><tr><td> $a_t$ </td><td>Activity (a task or an interaction)</td></tr><tr><td colspan="2">Goal</td></tr><tr><td> $g$ </td><td>Goal</td></tr><tr><td>status</td><td>Goal status</td></tr><tr><td> $c$ </td><td>Completed</td></tr><tr><td> $e_x$ </td><td>Executing</td></tr><tr><td> $w$ </td><td>Waiting</td></tr><tr><td> $s$ </td><td>Suspended</td></tr><tr><td colspan="2">Role</td></tr><tr><td> $r_{general}$ </td><td>Generic roles</td></tr><tr><td> $r$ </td><td>Normal roles</td></tr><tr><td> $r_{coordinator}$ </td><td>Special role to maintain goal status</td></tr><tr><td> $d$ </td><td>Duties of a role</td></tr><tr><td> $p$ </td><td>Privilege</td></tr><tr><td colspan="2">Interaction</td></tr><tr><td> $i$ </td><td>Interactions</td></tr><tr><td>msg</td><td>Communication from initiator role to responder role</td></tr><tr><td>resp</td><td>Response to a message</td></tr><tr><td>speech</td><td>Communicative act</td></tr><tr><td> $speech_{Act}$ </td><td>Action verb for communicationExample: Assertion, Query, etc.</td></tr><tr><td>content</td><td>Actual message</td></tr><tr><td colspan="2">Task</td></tr><tr><td> $t$ </td><td>Tasks</td></tr><tr><td> $\phi$ </td><td>Property / Logic / Subcomponent.</td></tr><tr><td>input</td><td>Represents input to a task</td></tr><tr><td>output</td><td>Represents output of a task</td></tr><tr><td> $<i/o>$ </td><td>Represents both input and output</td></tr><tr><td colspan="2">Knowledge</td></tr><tr><td> $k$ </td><td>Knowledge</td></tr><tr><td> $k_d$ </td><td>Declarative Knowledge</td></tr><tr><td> $k_p$ </td><td>Procedural knowledge</td></tr><tr><td> $w_p$ </td><td>Workflow patterns</td></tr><tr><td> $f$ </td><td>Facts</td></tr><tr><td> $rule_d$ </td><td>Deduction rule</td></tr><tr><td> $x_{structure}$ </td><td>Execution structure</td></tr><tr><td> $x_{order}$ </td><td>Execution order</td></tr><tr><td> $x_{constraint}$ </td><td>Execution constraint</td></tr><tr><td> $ev$ </td><td>Event</td></tr><tr><td> $ev_{external}$ </td><td>External event</td></tr><tr><td> $ev_{temporal}$ </td><td>Temporal event</td></tr><tr><td> $ev_{state}$ </td><td>State event</td></tr><tr><td colspan="2">Information</td></tr><tr><td> $i'$ </td><td>Information</td></tr><tr><td> $i'_f$ </td><td>Information flow</td></tr></table>

Table 2 (continued)

<table><tr><td>Notation</td><td>Description</td></tr><tr><td colspan="2">Information</td></tr><tr><td> $i'_{e}$ </td><td>Information entity</td></tr><tr><td> $e$ </td><td>Information entity instance</td></tr><tr><td> $\mathbf{e}$ </td><td>Information entity type</td></tr><tr><td> $e_{\text{info}}$ </td><td>Internal entity information</td></tr><tr><td> $i'_{\text{flow-control-info}}$ </td><td>Metadata for information flow</td></tr><tr><td> $c$ </td><td>control</td></tr><tr><td> $i'_{\text{flow-source}}$ </td><td>Source from which an information flow emanates</td></tr><tr><td> $i'_{\text{flow-sink}}$ </td><td>Entity receiving the information flows</td></tr><tr><td> $i'_{\text{data}}$ </td><td>Actual data with flow</td></tr><tr><td> $i'_{\text{flow-external}}$ </td><td>External source/sink for information flow</td></tr><tr><td> $i'_{\text{flow-frequency}}$ </td><td>Information flow frequency</td></tr><tr><td colspan="2">Agent</td></tr><tr><td> $a_{g}$ </td><td>Agent</td></tr></table>

## 3.2.1. Goal dependency model

Goal dependencies are captured by the goal construct in terms of a goal tree. The business goals identified during business analysis are organized into a goal tree to represent user requirements at different levels of detail. In the goal tree, a goal is decomposed iteratively until it reaches a collection of individual goals (g ) at the leaf goal level. For ease of discussion, we refer to the collection of all individual goals (g ) as a goal-set (G). The individual goals (g ) are mutually exclusive and collectively exhaustive of the MIBIS system goals. As a result, the goal-set (G) forms a whole-part relationship in which an individual goal $( g _ { i } )$ is a component of the goalset (G).

```verilog
Table 3
The AIML conceptual modeling grammar in BNF

ψ: := G|R|I|T|I'|K|A;
(* Upper case letters represent collections — see Table 1 for details *)
C_attributes: := "id", "name", "description";

Goal:
g = C_attributes, status;
status = "c" | "e_x" | "w" | "s";

Role:
r_General = r|r_coordinator;
(* A role is either a role that is regular role (one that is assigned to a leaf goal or a goal that updates the status of goals. If the duty is to update the status of a goal we call it the coordinator role*)
r_General = C_attributes, k, d;
d = a|d, a;
(* duties of a role may consist or single activity or a sequence of activities *)
a = {t|i}^-|a, {t|i};
(* In Extended BNF, - implies symbols repeated one or more times *)
Interaction:
i = C_attributes, Speech;
Speech = Msg|Speech, Resp;
(* The symbol Message is used to express both Msg and Resp as they have the same format. *)
Message = initiator, responder, speech_Act, content
(* initiator is a role that initiates a communication and responder is also a role with responds to the message*)
(* Assertion, Query, Request, Perform, Commitment, Denial, etc represent speech acts *)
speech_Act = "Assertion" | "Query" | "Request" | "Perform" | "Commitment" | "Denial";
(* content represents the actual message communicated during the interaction *)
Task:
A = a|A, a;
a = t| i;
i = C_attributes, input, output, method;
(* The symbol <i'o> is used to express both <input> and <output> as they have the same format *)
<i'o> = k_d|i'f | <i'o>, k_d | <i'o> i'f;
method = Φ;
Φ = φ | Φ, φ;
(* φ is one of the methods or properties *)
Information:
i' = i'e|i'f;
i'e = C_Attributes, input, output, method;
(* e_info includes semantic, syntactic and structural information about the entity *)
(* e represents the data associated with the entity instance *)
i'f = C_Attributes, i'flow_control_info, i'flow_data_info, i'data;
i'flow_control_info = i'flow-source, i'flow-sink, i'flow-frequency, i'flow-response_time;
i'flow-source = r; i'e, i'flow-external | i'flow-source, r; i'e, i'flow-external;
i'flow-sink = r; i'e, i'flow-external | i'flow-sink, r; i'e, i'flow-external;
(* i'flow-external is either an end user, or MIBIS entity or a non-MIBIS entity i'flow-externa = "End_USer" | MIBIS_entity" | "Non_MIBIS_entity")
(* i'flow_data_info is a data structure or format information *)
```

```txt
Table 3 (continued)

Information:
(*i'data is instance data *)
i'chunk="Entity"|"Entity_instance"|Entity_attribute"|Entity_instance_attribute_value"
P="Read"|"Write"|"View"|"Grant"|"Print"|P,"Read"|"Write"|"View"|"Grant"|"Print";

Knowledge:
k=k_d|k_p|k,k_d|k,k_p;
k_d=C_Attributes,F|C_Attributes,RULE_d|k_d,F|k_dRULE_d;
F=f|F,f;
(*f is simply a context relevant assertion *)
RULE_d=rule_d|RULE_d, rule_d;
(*rule_d is a deduction rule *)
k_p=C_Attributes, w_p|k_p,w_p;
w_p=x_structure|x_constraints;
(*x_structure is either a sequence, parallel split, exclusive choice, etc *)
x_structure="sequence)|("parallel_split"|"exclusive_choice"|...
x_constraint="ev_external"|"ev_temporal"|"ev_state"|"ev_resource"
Agent:
(* Agent is assigned a role using a predicate function defined in Table 4. *)
```

The highest level of the goal tree indicates the work system that is involved in business integration at the conceptual level. Goal decomposition can be performed using existing approaches for goal-oriented requirement engineering [e.g., [6,17]]. Fig. 3 describes a simplified goal tree for an integrative business system to provide made-to-order PC service to customers. The goal tree indicates that it requires coordination from 3 work systems: customer service as an interface for customer to request, change, or cancel an order, PC assembly to assemble a PC as requested, and PC deliver to deliver PC to customers. The goal tree has 4 individual goals (G1.1.1, G1.1.2, G1.2, and G1.3), each of which has to be completed in order for the overall goal (G1) to be completed.

The implication that all the individual goals $( g _ { i } )$ have to be accomplished in order to satisfy the overall goals of the system leads to Axiom 1.

Axiom 1. System goals are accomplished if and only if all individual goals are accomplished.

$$
(\forall g) \text { has\_state } (g, c) \to \text { has\_state } (G, c)\tag{1}
$$

In order to ensure the enforcement of Axiom 1 in the process of system development, we include an attribute called status in the goal schema (as shown in Table 3) in addition to the attributes that are common to all AIML constructs. The attribute is used to maintain the state of a goal. An individual goal can be in one of the following states: completed (c), executing (e), waiting (w), or suspended (s). Although the attribute status is a design consideration, we include it in the goal schema to facilitate the transition from conceptual models to design models in system development.

Table 4  
List of predicates used to specify the AIML grammar

<table><tr><td>Predicate</td><td>Meaning</td></tr><tr><td>accesses $(r,i'_{\text{chunk}})$ </td><td>Role  $r$  accesses the information  $i'_{\text{chunk}}$ </td></tr><tr><td>accomplish $(g,r)$ </td><td>Goal  $g$  is accomplished by role  $r$ </td></tr><tr><td>agent $(a_g)$ </td><td> $a_g$  is an agent</td></tr><tr><td>assign $(p,r,i'_{\text{chunk}})$ </td><td>Privilege  $p$ is assigned to role  $r$  for  $i'_{\text{chunk}}$ </td></tr><tr><td>assigned $(r,g)$ </td><td>Role  $r$  is assigned to goal  $g$ </td></tr><tr><td>changed_goal_stat $(r_{\text{coordinator}}, g, \text{status})$ </td><td>Role  $r_{\text{coordinator}}$  changes the state of goal  $g$  to status</td></tr><tr><td>concurrent $(a_{t1}, a_{t2})$ </td><td>Activity  $a_{t1}$  is in parallel with activity  $a_{t2}$ </td></tr><tr><td>execute $(r,a_t)$ </td><td>Role  $r$  performs activity  $a_t$ </td></tr><tr><td>frequency $(a_t,n)$ </td><td>Activity  $a_t$  must be performed with frequency  $n$ </td></tr><tr><td>goal $(g)$ </td><td> $g$  is a goal</td></tr><tr><td>has_goal $(a_g,g)$ </td><td>Agent  $a_g$  has a goal  $g$ </td></tr><tr><td>initiator $(i,r)$ </td><td>Role  $r$  is the initiator of an interaction</td></tr><tr><td>has_permission $(r,p,i'_{\text{chunk}})$ </td><td>Role  $r$  has permission  $p$  to access  $i'_{\text{chunk}}$ </td></tr><tr><td>has_properties $(t_1, \Phi)$ </td><td>Task  $t_i$  has a collection of Properties / Methods  $\Phi$ </td></tr><tr><td>responder $(i,r)$ </td><td>Role  $r$  is the responder of the interaction</td></tr><tr><td>has_state $(g, \text{status})$ </td><td>Goal  $g$  has state status</td></tr><tr><td>information $(i')$ </td><td> $i'$  is either an information entity or flow</td></tr><tr><td>interaction $(i)$ </td><td> $i$  is an interaction</td></tr><tr><td>isa_typeof $(t_i,t_j)$ </td><td>Task  $t_i$  is of type  $t_j$  and further task  $t_i$  inherits from task  $t_j$  collection of Properties/Methods  $\Phi$ </td></tr><tr><td>knowledge $(k)$ </td><td> $k$  is a knowledge nugget</td></tr><tr><td>fact $(f)$ </td><td> $f$  is a fact</td></tr><tr><td>deduction $(f)$ </td><td>Fact  $f$  is obtained by deduction</td></tr><tr><td>operate_on(rule $_d,F)$ </td><td>Deduction rule has to operate on facts</td></tr><tr><td>optional $(a_t)$ </td><td>Activity  $a_t$  is optional</td></tr><tr><td>overrides $(t_i,\phi_1,\phi_2)$ </td><td>Task  $t_i$  overrides property  $\phi_1$  with property  $\phi_2$ </td></tr><tr><td>partOf $(t_i,t_j)$ </td><td>Task  $t_i$  is a sub-task of part of task  $t_j$ </td></tr><tr><td>plays $(a_g,r)$ </td><td>Agent  $a_g$  plays role  $r$ </td></tr><tr><td>precedes $(at_1, at_2)$ </td><td>Activity  $a_{t1}$  is executed before activity  $a_{t2}$ </td></tr><tr><td>revoke $(p,r,i'_{\text{chunk}})$ </td><td>Privilege  $p$  is assigned to role  $r$  for  $i'_{\text{chunk}}$ </td></tr><tr><td>role $(r)$ </td><td> $r$  is a role</td></tr><tr><td>subordinate $(r_i,r_j)$ </td><td>Role  $r_i$  is subordinate to role  $r_j$ </td></tr><tr><td>task $(t)$ </td><td> $t$  is a task</td></tr><tr><td>trigger $(ev, a_t)$ </td><td>Activity  $a_t$  is triggered by event  $ev$ </td></tr></table>

## 3.2.2. Role determination

The AIML roles are design artifacts designed to accomplish individual goals at the leaf goal level of the goal tree. The relationship between the goal and role is bijective one-to-one mapping. It implies that an individual goal can be assigned to only one role, and a role is responsible for only one individual goal. Moreover, it indicates that the process of building goal tree and that of designing roles are interactive — the goal tree may need to be modified while roles are designed and vice versa. The bijective relationship between individual goals (g ) and individual roles $( r _ { i } )$ are expressed in Axiom 2.

Axiom 2. Each individual goal is assigned to a unique role, and each role is responsible for a unique individual goal.

$$
\begin{array}{c} \operatorname{goal} (g _ {k}) \wedge \operatorname{role} (r _ {i}) \wedge \operatorname{assigned} (r _ {i}, g _ {k}) \\ \to \neg \operatorname{assigned} (r _ {j}, g _ {k}) \wedge \operatorname{role} (r _ {j}) \wedge (r _ {i} \neq r _ {j}) \end{array}\tag{2}
$$

$$
\begin{array}{c} \operatorname{goal} (g _ {i}) \wedge \operatorname{role} (r _ {k}) \wedge \operatorname{assigned} (r _ {k}, g _ {i}) \\ \to \neg \operatorname{assigned} (r _ {k}, g _ {j}) \wedge \operatorname{goal} (g _ {j}) \wedge (g _ {I} \neq g _ {j}) \end{array}\tag{3}
$$

In our example, four distinct roles need to be designed to take responsibility for the four individual goals shown in Fig. 3 and these are described and mapped in Table 5.

Roles within AIML do not have any hierarchical relationships. Existence of a role hierarchy would imply master–slave relationships. In the current conceptualization, a MIBIS system is viewed as a collection of distributed autonomous agents without any central control. Incorporation of role hierarchies in AIML is beyond the current scope and is a significant area for future research. Therefore, all agents within a system are conceptualized to be in peer-to-peer relationships. Consequently, supervisory roles do not exist as reflected in Axiom 3.

Axiom 3. No role can control other roles in a MIBIS system.

$$
\operatorname{role} \left(r _ {i}\right) \wedge \operatorname{role} \left(r _ {j}\right) \wedge \left(r _ {i} \neq r _ {j}\right)) \rightarrow \neg \text { subordinazte } \left(r _ {i}, r _ {j}\right)\tag{4}
$$

Furthermore, in order to ensure the accomplishment of the overall systems goals in a peer-to-peer environment, AIML provides one special role termed coordinator to track goal accomplishment status of other roles. The task of the coordinator role $( r _ { \mathrm { c o o r d i n a t o r } } )$ is to update the status of all the goals in the system and ensure that every goal in the overall system goal tree is accomplished. Therefore, we have the following axiom:

Axiom 4. The state of the goal is changed by a special role called the coordinator role which possesses the necessary permission to change the status of goals in the MIBIS system.

$$
\begin{array}{l}\text { goal } (g) \wedge \text { role } (r _ {\text { coordinator }}) \wedge \text { changed\_goal\_stat } (r _ {\text { coordinator }}, g, \text { status })\\\rightarrow \text { has\_state } (g, \text { status })\end{array}\tag{5}
$$

where the status is set to either completed, executing waiting or suspended and $\exists ! r _ { \mathrm { c o o r d i n a t o r } } \mathrm { r o l e } ( r _ { \mathrm { c o o r d i n a t o r } } ) \in R$ where R is the collection of roles. Please note that we have used the notation ∃! to specify uniqueness quantification.

![](/api/attachments/5ZA3QZ4K/fulltext/images/10a83e2b682b6ddd8854f9182aa02d757db5977228832fbdcf2f74d5be43bbf0.jpg)  
Fig. 3. A goal tree for the online PC made-to-order system.

## 3.2.3. Interaction specification

Following the speech act theory, an interaction in AIML is defined as a coordinated sequence of speech acts [8,39]. Speech Acts (SA) are utterances that contain information needed to assert and perform actions and serve as building blocks of communication protocols. They define what people do while communicating [9,30]. Speech act verbs are used in speech act utterances, to perform actions such as booking, complaining, forgiving, etc. [34,35]. Therefore, the specification of an interaction in AIML includes initiator, responder, speech act, and message as defined in Table 3. The initiator starts an interaction by sending a message using a speech act. However, the message may or may not evoke a response from the responder. Likewise, the response from the responder may or may not evoke a new message from the initiator. Table 6 shows an example specification of the interaction for Sales to find a factory to assemble PCs for customers.

In MIBIS, not a single role has complete knowledge and capabilities to accomplish the overall system goal. That is, all roles need to interact with other roles. On the other hand, every interaction must involve at least two distinct roles.

Table 5  
The bijective mapping between goals and roles

<table><tr><td>Individual Goal</td><td>Role</td></tr><tr><td>G1.1.1 to acquire customers’ orders</td><td>R1.1 Sales</td></tr><tr><td>G1.1.2 to provide customer service</td><td>R1.2 Customer service</td></tr><tr><td>G1.2 to assemble PC</td><td>R2 Factory</td></tr><tr><td>G1.3 to deliver PC</td><td>R3 Shipping</td></tr></table>

Therefore, the relationship between the role and the interaction construct is governed by Axioms 5 and 6.

Axiom 5. Every role is involved in at least one interaction either as an initiator or a responder.

∀r role r →∃!i interaction i ∧ initiator i; r ∨responder i; r

6

Axiom 6. Every interaction involves an initiator role and a responder role.

$$
\begin{array}{c}(\forall i [ (\exists ! r _ {i}) \text { role } (r _ {i}) \land \text { interaction } (i) \land \text { initiator } (i, r _ {i}) ]\\\rightarrow (\exists ! r _ {j}) \text { role } (r _ {j}) \land \text { responder } (i, r _ {r}) \land (r _ {i} \neq r _ {j})\end{array}\tag{7}
$$

where R is the collection of roles in the MIBIS universe and $r _ { i } , r _ { j } { \in } R$

## 3.2.4. Task specification

A task can be as simple as a single activity or as complex as a business process or a workflow. AIML supports tasks to be decomposed recursively into two types of hierarchy: sub-activities and subtypes. The former is a decomposition of a task into AND/OR sub-activity components, while the latter represents an IS-A hierarchy. For example, as shown in Fig. 4, a parent task “process order” can be decomposed into the constituent sub-activities of “receive order”, “find factory”, “find shipping”, and “confirm order”; the activity “find shipping” can be further decomposed into specialized subtypes of “find ground shipping” and “find express shipping”. Similar conceptualization is also employed in Malone et al. [25].

Specification of the interaction “Find Factory”

<table><tr><td colspan="2">Interaction</td></tr><tr><td>Identifier</td><td>Inter1</td></tr><tr><td>Name</td><td>Find Factory</td></tr><tr><td>Description</td><td>Sales contacts possible factories and find an appropriate one for customer&#x27;s order</td></tr><tr><td>Initiator role</td><td>R1.1 Sales</td></tr><tr><td>Responder role</td><td>R2 Factory</td></tr><tr><td>speech act messages</td><td>Sales (Request) propose a contract for customer&#x27;s orderFactory (Acceptance)accept the contractSales (Assertion) confirm the contract</td></tr></table>

To support the task hierarchy, AIML provides two predicates: (a) $\mathrm { p a r t O f } ( t _ { i } , t _ { j } ) { - } \mathrm { t a s k } t _ { i }$ is considered a subpart of task $t _ { j } ;$ and (b) isa\_typeof(t ,t ) − task $t _ { i }$ is considered to be of type task $t _ { j } .$ Axiom 7 describes the non-reflexivity properties (C 8 and C 9) of task decomposition. These properties are important because they ensure task hierarchical structure to be represented as a Directed Acyclic Graph (DAG).

Axiom 7. A task and its sub-level tasks are non-reflexive.

$$
\operatorname{partOf} \left(t _ {i}, t _ {j}\right)\rightarrow \neg \operatorname{partOf} \left(t _ {j}, t _ {i}\right)\tag{8}
$$

$$
\text { isa\_typeof } (t _ {i}, t _ {j}) \to \neg \text { isa\_typeof } (t _ {j}, t _ {i})\tag{9}
$$

Partitioning along the dimension of subtypes (isa\_typeof relationships) allows for inheritance from a more generalized type to a more specialized type, in a manner that is similar to the type hierarchy considered in most objectoriented approaches. It is important to note that while the Part-Whole $( \mathrm { p a r t O f } ( t _ { i } , t _ { j } )$ is transitive (see Axiom 8 — C 10), the inheritance relationship (isa $\mathrm { t y p e o f } ( t _ { i } , t _ { j } ) )$ is not constrained to be so. The transitive closure in the inheritance relationship (isa $\mathrm { t y p e o f } ( t _ { i } , t _ { j } ) )$ is not enforced so that a task does not automatically inherit from ancestors properties and methods that the parent tasks have overridden.

Axiom 8. Transitive closure of part-whole relationship

$$
\operatorname{partOf} \left(t _ {i}, t _ {j}\right) \wedge \operatorname{partOf} \left(t _ {j}, t _ {k}\right)\rightarrow \operatorname{partOf} \left(t _ {i}, t _ {k}\right)\tag{10}
$$

Similar to the object-oriented approach, AIML allows for subtypes to override inherited properties as described by Axiom 9.

Axiom 9. A subtype is able to override the properties inherited from its parent.

$$
\begin{array}{l}\text { isa\_typeof } (t _ {i}, t _ {j}) \wedge \text { has\_properties } (t _ {j}, \Phi_ {1}) \wedge \text { overrides } (t _ {1}, \Phi_ {1}, \Phi_ {2})\\\rightarrow \text { has\_properties } (t _ {\mathrm{i}}, \Phi_ {2})\end{array}\tag {11}
$$

The task construct has been conceptualized to include the following attributes: Input, Output, Parent Tasks, Sub-Activities, $S u b \ – T y p e s ,$ and Method as defined in Table 3. Inputs are information required for task execution, while Outputs are information generated from the task; the Method metaphor embodies the procedural knowledge that specifies the detailed logic for execution of the task. A method can be described using different mechanisms, including structured English and pseudo code. Table 7 is an example specification for the task “receive order”.

## 3.2.5. Information modeling

Information refers to data resources available within a MIBIS application and may pertain to both the functional (business-aware) and the non-functional (business-unaware; IT system-specific) aspects of the MIBIS application. The information construct of AIML consists of information entities and information flows. The specifications of both information entities and information flows are detailed in Table 3.

![](/api/attachments/5ZA3QZ4K/fulltext/images/8cd4251b289dec4172787a3230b1a62dbb4f8ad6880661075da595c3333c294b.jpg)  
Fig. 4. an example of task decomposition.

Table 7  
Specification of task “Receive order”

<table><tr><td colspan="2">Task</td></tr><tr><td>Identifier</td><td>T1.1</td></tr><tr><td>Name</td><td>Receive order</td></tr><tr><td>Description</td><td>Capture customer&#x27;s order</td></tr><tr><td>Input</td><td>Customer informationOrder request</td></tr><tr><td>Output</td><td>Order</td></tr><tr><td>Parent Tasks</td><td>Process order</td></tr><tr><td>Sub-Activities</td><td>None</td></tr><tr><td>Sub-Types</td><td>None</td></tr><tr><td>Method</td><td>Do for each orderIf new customer, register new account, EndifGet customer account informationCreate orderEnddo</td></tr></table>

Information entities refer to internal data within the system that are part of data stores. They represent regular business objects (such as order, customer, etc.) and other materialized views of data. The schema of information entities includes the structure of tables, the relationships, entity integrity constraints, referential integrity constraints, cardinality constraints, etc. Information entities may be implemented using relational databases and the schema corresponds to items typically stored in database repositories. The specifications of information entities have no difference from those in traditional data modeling. Table 8 indicates that customer number, name, address, phone, and internal credit ranking must be recorded in the database.

Information flows represent data that are in transit; for example, data moving between external users and roles, between information entities and roles, or between other external systems and roles. Information flows are different from information entities in their time orientation [5]. Information flows are temporal. They cease to exist once they are acted upon by an agent or stored in a data store or provided to an entity external to the MIBIS system. Information flows represent data resources for agents to update their beliefs or for information entities to update their states. Table 9 describes the information flow from customers to make order requests.

Table 8  
Specification of information entity “Customer”

<table><tr><td colspan="2">Information entity</td></tr><tr><td>Identifier</td><td>INE1</td></tr><tr><td>Name</td><td>Customer</td></tr><tr><td>Description</td><td>Customer information and his/her credit status</td></tr><tr><td>Attributes</td><td>Customer number, name, address, phone, internal credit ranking</td></tr></table>

Table 9  
Specification of information flow “Customer order request”

<table><tr><td colspan="2">Information Flow</td></tr><tr><td>Identifier</td><td>INF1</td></tr><tr><td>Name</td><td>Customer order request</td></tr><tr><td>Description</td><td>Order request from customers to sales</td></tr><tr><td>Flow source</td><td>External entity Customer</td></tr><tr><td>Flow sink</td><td>R1.1 Sales</td></tr><tr><td>Flow frequency</td><td>When customers place orders</td></tr><tr><td>Flow response time</td><td>Synchronous</td></tr><tr><td>Flow data</td><td>Item number, quantities</td></tr></table>

All data resources and information available within the MIBIS application are protected and access is based on the privileges a role possesses. Privileges reflect authority of roles to view, manipulate, create, or take other alternative actions on information. Privilege to access information entities and flows are granted at various levels of granularity $( \dot { l } _ { \mathrm { c h u n k } } )$ as determined by business rules. A role has to be granted the privilege at the intended level of granularity if it has to be able to access information. Therefore, we have the following axiom.

Axiom 10. A role has to be granted a privilege in order to enable it to access necessary information.

$$
\begin{array}{l}(\forall r) \left(\forall i _ {\text { chunk }} ^ {\prime}\right) \left[ \text { role } (r) \wedge \text { information } \left(i _ {\text { chunk }} ^ {\prime}\right) \wedge \text { accesses } \left(r, i _ {\text { chunk }} ^ {\prime}\right) \right]\\\rightarrow \text { has\_permission } (r, p, i _ {\text { chunk }} ^ {\prime})\end{array}\tag {12}
$$

$$
\text { has\_permission } (r, p, i _ {\text { chunk }} ^ {\prime}) \to \text { assign } (p, r, i _ {\text { chunk }} ^ {\prime})\tag{13}
$$

## 3.2.6. Knowledge specification

Human knowledge resides in the mind of individuals [1] and not in the collection of information. Similarly, knowledge in AIML is conceptualized to exist within individual roles and is therefore private to the roles. Accordingly, a role must posses the needed knowledge in order to use it. This constraint is represented in Axiom 11.

Axiom 11. A role can only use its own knowledge.

$$
\begin{array}{l}(\forall r) (\forall k) [ \text { role } (r) \land \text { knowledge } (k) \land \text { uses\_knowledge } (r, k)\\\rightarrow \text { has\_knowledge } (r, k) ]\end{array}\tag {14}
$$

Individual and organizational knowledge are very broad constructs consisting of both explicit and tacit knowledge [1]. However, the knowledge construct in AIML is viewed from a somewhat narrower perspective, in that it captures and represents only computational knowledge that is explicitly defined.<sup>10</sup> Individual and organizational knowledge includes declarative (knowthat) or procedural (know-how). Correspondingly, explicit computational knowledge in AIML consists of both declarative knowledge $( d _ { k } )$ and procedural knowledge $( p _ { k } )$ Declarative knowledge is composed of facts and deduction rules. Facts are beliefs that a role keeps about itself, about other roles in the system, and about the environment it resides in. Deduction rules empower roles to engage in deductive reasoning with the constraint that at least two existing facts are needed to deduce a new fact. This is further elaborated in Axiom 12.

Axiom 12. A new fact can only be deducted from at least two existing facts using a deduction rule.

$$
\operatorname{fact} (f _ {k}) \vee \text { deduction } (f _ {k}) \to (\exists \text { rule } _ {d}) (\text { operates\_on } (\text { rule } _ {d}, F)\tag{15}
$$

where F is a collection of facts with the collection containing at least two elements i.e. $\exists ^ { \geq 2 } f \in F ,$ and the quantification expression $\exists ^ { \geq 2 }$ is used to indicate ‘there exists at least two’.

Procedural knowledge dictates issues relating to precedence, timing, frequency, etc. of activities, and is conceptualized to consist of activity execution structure and activity execution constraints. Activity execution structure relates to knowing the order in which activities need to occur. As discussed earlier, an activity can either be a task or an interaction. Activity execution structure also includes information regarding how frequently activities have to be performed and whether certain activities are optional. The predicates (precede $\left( { { a _ { t 1 } } , { a _ { t 2 } } } \right)$ , concurrent $\left( { { a _ { t 1 } } , \ { a _ { t 2 } } } \right)$ , frequency(a, n) and optional(a)) are used to express activity execution structure as shown in Table 4. Activity execution constraints determine the events that trigger activities. In AIML, an activity is always triggered by an event. The event can be an external event $( e \nu _ { \mathrm { e x t e r n a l } } ) ,$ a temporal event $( e \nu _ { \mathrm { t e m p o r a l } } )$ , or a state event $( e \nu _ { \mathrm { s t a t e } } )$ External events emanate either from the environment including other roles or from end-users (such as a customer placing an order). External events generated by another role in the system correspond to inter-role-task dependencies. For example, a role $r _ { 1 }$ may start executing a task $t _ { 1 }$ only when another role $r _ { 2 }$ completes a task $t _ { 2 } .$ In order to preserve the autonomy of roles and hence the agents playing the roles, AIML does not permit modeling such constraints as part of the task execution structure of the role $r _ { I } .$ However, such constraints can be modeled as an external event for role $r _ { I } .$ . Temporal events are constraints placed on the execution of tasks or interactions based on some time consideration such as the elapse of some time period. A state event is an event that occurs inside a role, and changes the state of the role, and accordingly triggers a task or a set of tasks. The requirements of activity execution constraints are expressed in Axiom 13.

Axiom 13. Activities in the MIBIS universe must be triggered by an event. When an event (external, temporal, state, etc) trigger an activity, a role executes the activity.

$$
(\forall a _ {t}) [ \operatorname{role} (r) \vee \operatorname{executor} (r, a _ {t}) \rightarrow (\exists e v) \operatorname{trigger} (e v, a _ {t}) ]\tag{16}
$$

Table 10 describes an example specification of knowledge for sales.

## 3.2.7. Agent modeling

In an organizational context, a role is assigned to one or more physical human actors to accomplish organizational goals. In a similar manner, an abstract role in the MIBIS universe is instantiated by autonomous component agent. The component agent is modeled as a system entity that is capable of sensing its environment and acting autonomously to meet its design objectives [41]. Axiom 14 and Axiom 15 describe the conceptualization of the relationship between a role and an agent.

<table><tr><td colspan="2">Specification of knowledge for Sales</td></tr><tr><td colspan="2">Knowledge</td></tr><tr><td>Identifier</td><td>K1</td></tr><tr><td>Name</td><td>Sales Knowledge</td></tr><tr><td>Description</td><td>Knowledge on pricing, credit ranking, financing, order rejection/approval policy, and constraints on performing tasks</td></tr><tr><td colspan="2">Declarative Knowledge</td></tr><tr><td rowspan="2">Facts</td><td>Reliable factories</td></tr><tr><td>Reliable shipping</td></tr><tr><td>Deduction rules</td><td>If no factory can be found to satisfy customer&#x27;s exact request, a comparable configuration is suggested.</td></tr><tr><td colspan="2">Procedural knowledge</td></tr><tr><td>Execution structure</td><td>T1.1 “receive order” precedes T1.2 “find factory” and T1.3 “find shipping”.T1.2 “find factory” and T1.3 “find shipping” are parallel.T1.2 “find factory” and T1.3 “find shipping” precedes T1.4 “confirm order”.</td></tr><tr><td>Execution constraints</td><td>T1 “process order” is triggered by receiving customer&#x27;s order request.</td></tr></table>

Axiom 14. Every role must be played by at least one agent.

$$
\forall r \operatorname{role} (r) \rightarrow \exists \operatorname{agent} \left(a _ {g}\right) \wedge \text { plays } \left(a _ {g}, r\right)\tag{17}
$$

Axiom 15. Every agent must play at least one role.

$$
\forall a _ {g} \text { agent } (a _ {g}) \rightarrow \exists \text { role } (r) \land \text { plays } (a _ {g}, r)\tag{18}
$$

It may be noted that for every role there is at least one agent that plays that role. However the agents are not constrained in any other way. This allows for the assignment of multiple agents to a role. Similarly we constrain using expression C20 that every agent must play a role. There are no further constraints and this essentially allows for the assignment of many roles to an agent.

## 4. AIML quality evaluation

AIML conceptual grammar is developed following the helix-spindle model for ontological engineering [18] to ensure a high quality of this grammar. Following this model, the development process goes through three major phases-a conception phase, an elaboration phase, and a definition phase. At each phase, the AIML constructs and their relationships are defined based on well-founded theories and tested by building an application domain framework. If any problems are detected during framework building, the AIML development slides back to the beginning of the phase to guarantee coherence and extendibility of the grammar.

Conceptual modeling is essentially making statements in some language and it is closely linked to linguistic concepts. In this section, we follow Lindland et al's framework [23] for discussing the quality of the AIML grammar in terms of syntactic, semantic, and pragmatic quality.

Syntactic quality deals with how well the conceptual models correspond to the modeling grammar. Its goal is to ensure syntactic correctness. There are three basic mechanisms for ensuring syntactic quality: error prevention, error detection, and error correction. Error prevention is the mechanism by which insertion of erroneous statements into the model is rejected. Error detection is finding errors after erroneous statements have been inserted into a model. Error correction deals with replacing a detected error with a correct statement. Obviously, AIML provides enough support for syntactic quality by defining AIML formally in Backus-Naur form (BNF) and firstorder logic. Conceptual models created in AIML can be easily analyzed to detect errors and inconsistencies. While it may be difficult to automate error correction, software tools may be developed to automate error prevention and error detection based on formally-defined AIML syntax.

Semantic quality deals with how well the conceptual models correspond to the problem domain. The more closely a conceptual model reflects the problem domain, the better the semantic quality of that conceptual model. There are two semantic quality goals: validity and completeness. Validity ensures that all statements made by a model are correct and relevant to the problem. Completeness means that the model contains all the statements about the domain. While it is impossible to achieve total validity and completeness for anything but extremely simple problems, the AIML grammar is designed to capture the semantics of the MIBIS universe in a consistent, comprehensive, and unambiguous manner with a minimum number of modeling constructs. In [19], Kishore et al investigate the characteristics of the MIBIS universe based on the literatures in both the IBIS and multiagent systems domains. After analyzing various concepts involved in modeling MIBIS, they propose 8 minimal ontological foundation constructs for the MIBIS universe, including goal, role, interaction, task, information, knowledge, resource, and agent. The semantics of these MIBIS ontological constructs were also evaluated by Zhang et al. using the Bunge-Wand-Weber framework [44] who found the grammar to be quite expressive and comprehensive. This paper extends [19] by formally defining the internal structure of these ontological constructs and their relationships. Axioms are included to ensure the semantic consistency of conceptual models. Table 11 indicates that the AIML grammar overcomes UML limitations in supporting agent-based information systems and fully supports software agent characteristics. Therefore, the AIML grammar is a good fit with the MIBIS universe. On the other hand, the AIML grammar also provides support for completeness by supporting modularity. The AIML constructs are self-contained and allow new specifications to be added without modifying existing part of conceptual models. Each AIML building block can be changed and replaced without much effect on others. For example, one can assign new roles to agents and remove ones with no effect on the internal model of the roles.

Pragmatic quality deals with how well a conceptual model corresponds to its audience interpretation. The goal of pragmatic quality is to improve users' understanding of a conceptual modeling grammar and reduce the misuse of the grammar in constructing conceptual models. Pragmatic quality of the AIML grammar was evaluated earlier through an ontological analysis using the Bunge-Wang-Weber (BWW) model [36] and we discuss it briefly below. It is also evaluated in the current paper through a complexity analysis using metrics proposed by Rossi and Brinkkemper [27] and this is also discussed below.

Table 11  
AIML support for agent-based information systems

<table><tr><td>Agent-based IS Characteristics [41]</td><td>AIML Support</td><td>UML Limitations</td></tr><tr><td>Autonomous</td><td>A role encapsulates its functionality (i.e., it is responsible for its interactions and tasks). This functionality is internal and is not affected by the environment; further a role also encapsulates internal knowledge that allows it to perform its tasks and interactions; these features of AIML represent the autonomy of a role.</td><td>Although an object encapsulates its functionality, it has no control on what actions to take. Its internal methods can only be initiated by external invocation. Further, an object cannot refuse an external request. In other words, UML lacks constructs to support the decision-making aspect of an agent&#x27;s autonomy.</td></tr><tr><td>Reactive</td><td>The knowledge construct captures the events that trigger interactions and tasks; thus, AIML supports reactivity for roles and agents that play those roles.</td><td>UML fully supports the reactive aspect of an agent by allowing object&#x27;s internal methods to be triggered by external events.</td></tr><tr><td>Proactive</td><td>The knowledge construct models possible activity execution paths and these allow the roles and agents in AIML to be proactive in decision making to accomplish goals specified in the goal construct.</td><td>UML has no explicit “mentalistic” constructs to support the agent&#x27;s proactive aspect. It does not support agent&#x27;s goal-oriented behaviors.</td></tr><tr><td>Social</td><td>The interaction construct models the protocols, the communication paths, and the speech acts of the messages, thus, giving roles and agents the social ability to interact.</td><td>While UML is able to model low-level message exchanging, it lacks capabilities to model agent conversations, which includes not only a sequence of messages but also semantics associated with communicative (speech) acts.</td></tr></table>

From an ontological analysis perspective, an information system is a representation of the perceived real-world system. Therefore, a good conceptual modeling grammar must manifest the meaning of the real-world to be represented. By mapping the grammatical constructs of a conceptual modeling grammar to the ontological constructs of an ontological model (such as BWW model) which represents the real-world situation, we are able to identify ontological deficiencies of the grammar. Such ontological deficiencies result in user confusion in interpreting and using the grammar. According to Wand & Weber [37], four ontological deficiencies may be found in a grammar: 1) ontological incompleteness occurs when ontological constructs do not have equivalent constructs in the modeling grammar; 2) construct redundancy occurs when several constructs of the conceptual modeling grammar map onto a single ontological construct; 3) construct overload occurs when several ontological constructs are mapped onto a single construct in the modeling grammar; and 4) construct excess occurs when a grammatical construct might not map to any ontological construct. Because the BWW ontology is one of the most used higher-level information systems ontologies for evaluating conceptual modeling grammars, we conducted an ontological analysis of the AIML grammar using the BWW ontology to remove ontological deficiencies before formally defining the grammar in this paper. This ontological analysis, details of which are available in [44], indicated that the ontological semantics of the AIML grammar are quite clear and that the grammar has the potential to enhance user communication. We also found that the AIML grammar may also benefit MIBIS system developers as they will be able to identify easily the correct AIML constructs to represent problem domain knowledge and to develop precise conceptual models for a MIBIS system.

The second evaluation of pragmatic quality of the AIML grammar was conducted through a complexity analysis of the AIML grammar using metrics proposed by Rossi and Brinkkemper [27]. Complexity is a key measure of the effectiveness of a language because complexity directly affects the learning ability and the ease-of-use of the language [31]. Rossi and Brinkkemper [27] proposed a set of seventeen complexity metrics to evaluate systems development methods and individual techniques within those methods. Considering that AIML is a conceptual modeling grammar that covers only the early stages of the systems development life cycle, we include only the independent measures and aggregate metrics for individual systems development techniques in our analysis. Following are the definitions of the metrics we used in our analysis.

Let the model of a modeling technique T be given as $M _ { T }$ its object types as $O _ { T }$ (object is a thing that exists on its own), its property types as $P _ { T }$ (properties are characteristics of other meta-types), its relationship types as $R _ { T }$ (relationship is an association between two or more objects), its role types as $X _ { T }$ (role is the name given to the link between an object and its connection with a relationship), and the function $\mathrm { n } ( \mathrm { A } )$ denotes the number of elements in the set of A.

Table 12  
Complexity metrics values for AIML and UML conceptual-level diagrams

<table><tr><td rowspan="2" colspan="2"></td><td rowspan="2">AIML</td><td colspan="6">UML Diagrams (see footnote 11)</td></tr><tr><td>Class</td><td>Activity</td><td>Sequence</td><td>Collaboration</td><td>StateChart</td><td>Aggregate</td></tr><tr><td>Metric 1</td><td> $n(O_T)$ </td><td>7</td><td>7</td><td>8</td><td>6</td><td>4</td><td>10</td><td>35</td></tr><tr><td>Metric 2</td><td> $n(R_T)$ </td><td>12</td><td>18</td><td>5</td><td>1</td><td>1</td><td>4</td><td>29</td></tr><tr><td>Metric 3</td><td> $n(P_T)$ </td><td>19</td><td>18</td><td>6</td><td>5</td><td>7</td><td>11</td><td>47</td></tr><tr><td>Metric 5</td><td> $P^{-}o(M_T)$ </td><td>2.71</td><td>1.71</td><td>0.75</td><td>0.67</td><td>1</td><td>1</td><td>5.13</td></tr><tr><td>Metric 7</td><td> $P^{-}_R(M_T)$ </td><td>3.33</td><td>1.22</td><td>0.20</td><td>6</td><td>8</td><td>0.5</td><td>15.92</td></tr><tr><td>Metric 9</td><td> $R^{-}_o(M_T)$ </td><td>2.86</td><td>2.57</td><td>0.63</td><td>0.17</td><td>0.25</td><td>0.40</td><td>4.02</td></tr><tr><td>Metric 11</td><td> $C^{-}(M_T)$ </td><td>0.52</td><td>0.10</td><td>0.13</td><td>0.13</td><td>0.14</td><td>0.09</td><td>0.59</td></tr><tr><td>Metric 12</td><td> $C'(M_T)$ </td><td>23.54</td><td>26.40</td><td>11.18</td><td>7.87</td><td>8.12</td><td>15.39</td><td>65.38</td></tr></table>

Metric 1 $n ( O _ { T } )$ is the count of object types per technique. This metric demonstrates the number of individual object types used to specify object systems. The metric values for various objectoriented techniques range from 1 to 10.<sup>11</sup>

Metric 2 $n ( R _ { T } )$ is the count of relationship types per technique. It indicates the number of concepts that are used for describing connections between objects. The metric values for various object-oriented techniques range from 1 to 18 (see footnote 11).

Metric 3 $n ( P _ { T } )$ is the count of property types per technique. The metric values for various objectoriented techniques range from 3 to 18 (see footnote 11).

Metric 4 $P _ { o } ( M _ { T } , \ o ) { = } n ( P _ { T } ( o ) )$ , where $o \in O _ { T }$ This metric counts the number of properties for a given object type.

Metric 5 $\begin{array} { r } { \overline { { P } } o ( M _ { \mathrm { T } } ) = \frac { 1 } { n ( O _ { \mathrm { T } } ) } \sum _ { o \in O _ { \mathrm { T } } } P _ { o } ( M _ { \mathrm { T } } , o ) } \end{array}$ This met-<sup>ð Þ ¼ ð Þ ð Þ</sup>ric is average number of properties per object type. The metric values for various objectoriented techniques range from 0.67 to 5 (see footnote 11).

Metric 6 $\begin{array} { r } { P _ { R } ( M _ { T } , e ) = n ( p _ { T } ( e ) ) + \sum _ { x \in r _ { T } ( e ) } n ( p ( \mathrm { r o l e } ( x ) ) ) , } \end{array}$ <sup>ð</sup>where $e \in R _ { T }$ <sup>ð ÞÞ þ ð Þ ð ð ð ÞÞÞ</sup>This metric is the number of properties of a relationship type and its accompanying role types.

Metric 7 $\begin{array} { r } { \overline { { P } } _ { R } ( M _ { T } ) = \frac { 1 } { n ( O _ { T } ) } \sum _ { r \in R _ { T } } P _ { R } ( M _ { T } , e ) } \end{array}$ This met-<sup>ð Þ</sup>ric counts the average number of properties per relationship type. It shows the complexity of the interface between object types. The metric values for various object-oriented techniques range from 0.20 to 8 (see footnote 11).

Metric 8 $R _ { o } ( M _ { T } , o ) \ : = \ : n \big ( \big \{ e \in R _ { T } \vert o \in \cup _ { x \in r _ { T } ( e ) }$ object x     , <sup>ð</sup>where $o \in O _ { T }$ <sup>j [ ð Þ ð Þ</sup>This metric gives the number of relationship types that can be connected to a certain object type.

Metric 9 $\begin{array} { r } { \overline { { R } } _ { o } ( M _ { T } ) = \frac { 1 } { n ( O _ { T } ) } \sum _ { o \in O _ { T } } R _ { o } ( M _ { T } , o ) } \end{array}$ This met-<sup>ð Þ ¼ ð</sup> <sup>Þ ð Þ</sup>ric gives the average number of relationship types that can be connected to a given object type. The metric values for various objectoriented techniques range from 0.17 to 5 (see footnote 11)

Metric 10 $C ( M _ { T } , o ) = \frac { P _ { o } ( M _ { T } , o ) } { \sum _ { c \in \cal A } P _ { R } ( M _ { T } , e ) } ,$ where $A \ = \ \{ x \in$ $R _ { T } | o { \in } \cup _ { x \in r _ { T } ( x ) }$ object y The quotient indi-<sup>ð Þ</sup>cates the division of work in this technique, i.e. are things described by their internal properties, or by external connections.

Metric 11 $\begin{array} { r } { \overline { { C } } ( M _ { T } ) = \frac { 1 } { n ( O _ { T } ) } \sum _ { o \in O _ { T } } C ( M _ { T } , o ) } \end{array}$ This metric <sup>ð Þ ¼ ð Þ ð Þ</sup>shows the average complexity for the whole technique. The metric values for various object-oriented techniques range from 0.09 to 3.

Metric 12 $C ^ { \prime } ( M _ { T } ) \ = \ \sqrt { n ( O _ { T } ) ^ { 2 } + n ( R _ { T } ) ^ { 2 } + n ( P _ { T } ) ^ { 2 } }$ <sup>ð Þ ¼ ð Þ þ ð Þ þ ð Þ</sup>This metric gives the total conceptual complexity of a technique. The metric values for various object-oriented techniques range from 3.32 to 26.40.

In our complexity analysis, we compare AIML complexity metrics with UML diagrams that are used in the early stages of system development to specify user requirements and capture similar types of constructs and relationships as AIML. We select UML as the reference grammar for our comparison because UML has become the de facto modeling grammar accepted widely for object-oriented systems analysis and design. Table 12 compares the complexity metrics values<sup>12</sup> of the AIML grammar with UML diagrams at the conceptual level. While UML class diagram captures data requirements, UML activity diagram, sequence diagram, collaboration diagram, and StateChart diagram capture and describe system requirements from a behavioral perspective. The real-world information captured in these UML models is similar to the real-world information that is captured through AIML constructs. Table 12, therefore, aggregates the metric values for the selected UML conceptual-level diagrams and compares it as a group with AIML metric values to provide an apples-to-apple comparison.

Table 12 shows that AIML has significantly lower values for all complexity metrics as compared to the aggregate UML metric values except for $\hat { C } ( M _ { T } )$ which is also lower for AIML indicating that AIML is much more intuitive, and easier to learn and use. This is very much in line with contemporary anecdotal evidence that suggests that UML is a fairly complex modeling formalism. The complexity of UML stems in part from the fact that it is a general purpose modeling formalism that caters to all kinds of object-oriented systems. AIML, on the other hand, is a special-purpose modeling formalism that is developed specifically for modeling the agile integration of work systems using the notions and principles of multiagent systems and has a much narrower focus. These complexity metrics provides further evidence about the high degree of pragmatic quality of AIML and its superiority over UML, the de facto standard for conceptual modeling, in terms of ease of learning and ease of use.

## 5. Conclusion

Large-scale use of multiagent technology in various integrative business information systems requires a special-purpose conceptual-modeling grammar to facilitate the analysis and design of MIBIS systems. In response to such needs, we have developed the AIML grammar for conceptual modeling and high-level design of agile IBIS systems in the MIBIS universe. The grammar provides formal definitions for constructs that form an ontological foundation for representing the MIBIS universe, and provides a starting point for ontologydriven MIBIS development. The grammar benefits both IBIS researchers and practitioners. On the one hand, it advances researchers' understanding of the MIBIS universe and thus forms a foundation for developing various methodologies for development of agile IBIS systems in the MIBIS universe. On the other hand, the formal definitions of the AIML constructs provide templates for IBIS practitioners to avoid developing individual applications from scratch each time, thereby facilitatating system development knowledge reuse.

There are several future research directions to further this study. First, in order to enhance the reuse of MIBIS domain-specific knowledge, lower-level ontological categories for the AIML foundation constructs need to be developed (e.g., an ontology of MIBIS roles, an ontology of MIBIS goals, etc.). Second, further elaboration of the AIML grammar and axiomatic proofs are needed to increase the rigor of this grammar. Third, interactions in current study are limited to direct interactions between a pair of roles. In future work, interactions should be extended to include those between more than two roles. Fourth, knowledge in this study is limited to deductive reasoning and it is possible to extend AIML to include other types of knowledge and reasoners, such as abductive, inductive, and case-based reasoning, etc. Last, but not the least, appropriate methodologies and software tools will also need to be developed to support the analysis, design, and development of agile IBIS systems in the MIBIS universe.

## References

[1] M. Alavi, D.E. Leidner, Knowledge management and knowledge management systems: conceptual foundations and research issues, MIS Quarterly 25 (1) (2001) 107–136.

[2] S. Alter, A general, yet useful theory of information systems, Communications of the Association for Information Systems 1 (13) (1999) 1–70.

[3] A. Basu, A. Kumar, Research commentary: workflow management issues in e-business, Information Systems Research 13 (1) (2002) 1–14.

[4] B.J. Biddle, E.J. Thomas, Role Theory: Concepts and Research, John Wiley & Son, Inc., 1966.

[5] S. Conger, The New Software Engineering, Wadsworth Series in Managment Information Systems, Wadsworth Publishing Company, Belmont, CA, 1994.

[6] A. Dardenne, A. van Lamsweerde, S. Fickas, Goal-directed requirements acquisition, Science of Computer Programming 20 (1993) 3–50.

[7] S.A. Deloach, M.F. Wood, C.H. Sparkman, Multiagent systems engineering, International Journal on Software Engineering and Knowledge Engineering 11 (3) (2001) 231–258.

[8] J.L.G. Dietz, DEMO: towards a discipline of organisation engineering, European Journal of Operational Research 128 (2) (2001) 351–363.

[9] J. Habermas, The Theory of Communicative Action, vol. I, Beacon Press, Boston, 1984.

[10] S.S. Heragu, R.J. Graves, B.-I. Kim, A. St Onge, Intelligent agent based framework for manufacturing systems control, IEEE

Transactions on Systems, Man and Cybernetics, Part A 32 (5) (2002) 560–573.

[11] G. Huber, Organizational learning: the contributing processes and the literatures, Organization Science 2 (1) (1991) 88–115.

[12] M.N. Huhns, L.M. Stephens, Automating supply chains, IEEE Internet Computing 5 (4) (2001) 90–93.

[13] ISO/IEC, Information technology-Syntactic metalanguage-Extended BNF, Published ISO standard 14977:1996(E), ISO/IEC, 1996).

[14] N.R. Jennings, An agent-based approach for building complex software systems, Communications of the ACM 44 (4) (2001) 35–41.

[15] N.R. Jennings, T.J. Norman, P. Faratin, P. O'Brien, B. Odgers, Autonomous agents for business process management, Journal of Applied Artificial Intelligence 14 (2) (2000) 145–189.

[16] N. Kang, S. Han, Agent-based e-marketplace system for more fair and efficient transaction, Decision Support Systems 34 (2) (2003) 157–165.

[17] E. Kavakli, Goal-Oriented Requirements Engineering: A Unifying Framework, Requirements Engineering 6 (4) (2002) 237–251.

[18] R. Kishore, H. Zhang, R. Ramesh, A helix-spindle model for ontological engineering, Communications of the ACM 47 (2) (2004) 69–75.

[19] R. Kishore, H. Zhang, R. Ramesh, Enterprise integration using the agent paradigm: foundations of multiagent-based integrative business information systems, Decision Support Systems 42 (1) (2006) 48–78.

[20] A.D. Kwok, D.H. Norrie, Intelligent agent systems for manufacturing applications, Journal of Intelligent Manufacturing 4 (4) (1993) 285–293.

[21] F.-R. Lin, Y.-H. Pai, Using multi-agent simulation and learning to design new business processes, IEEE Transactions on Systems, Man and Cybernetics, Part A 30 (3) (2000) 380–384.

[22] F.-R. Lin, G.W. Tan, M.J. Shaw, Multiagent enterprise modeling, Journal of Organizational Computing and Electronic Commerce 9 (1) (1999) 7–32.

[23] O.I. Lindland, G. Sindre, A. Solvberg, Understanding quality in conceptual modeling, IEEE Software 11 (2) (1994) 42–49.

[24] T.W. Malone, K. Crowston, The interdisciplinary study of coordination, ACM Computing Surveys 26 (1) (1994) 87–119.

[25] T.W. Malone, K. Crowston, J. Lee, B. Pentland, C. Dellarocas, G. Wyner, J. Quimby, C.S. Osborn, A. Bernstein, G. Herman, et al., Tools for inventing organizations: toward a handbook or organizational processes, Management Science 45 (3) (1999) 425–443.

[26] I. Nonaka, A dynamic theory of organizational knowledge creation, Organization Science 5 (1) (1994) 14–37.

[27] M. Rossi, S. Brinkkemper, Complexity metrics for systems development methods and techniques, Information Systems 21 (2) (1996) 209–227.

[28] A.F. Salam, L. Iyer, R. Singh, Intelligent agents in supporting information sharing in B2B eMarketplaces, Information Systems Management 22 (3) (2005) 37–49.

[29] A.-W. Scheer, ARIS-Business Process Modeling, Springer, Berlin, 1999.

[30] J.R. Searle, Speech Acts: An Essay in the Philosophy of Language, Cambridge University Press, 1969.

[31] K. Siau, Q. Cao, Unified Modeling Language (UML) — a complexity analysis, Journal of Database Management 12 (1) (2001) 26–34.

[32] R. Sikora, M. Shaw, Multi agent enterprise modeling, in: C. Holsapple, V. Jacob, H.R. Rao (Eds.), Business Modeling: A

Multidisciplinary Approach Essays in honor of Andrew B. Whinston, Kluwer Academic Press, 2002, pp. 169–185.

[33] R. Singh, A.F. Salam, L.S. Iyer, Agents in eSupply Chains, Communications of the ACM 48 (6) (2005) 108–115.

[34] J. Verschueren, The Analysis of Speech Act Verbs: Theoretical Preliminaries, Indiana University Linguistic Club, Bloomington, Indiana, 1977.

[35] J. Verschueren, On Speech Act Verbs, John Benjamins, Amsterdam, 1980.

[36] Y. Wand, R. Weber, An ontological model of an information system, IEEE Transactions on Software Engineering 16 (11) (1990) 1282–1292.

[37] Y. Wand, R. Weber, On the ontological expressiveness of information systems analysis and design grammars, Journal of Information Systems 3 (4) (1993) 217–237.

[38] H. Weigand, W.-J.v.d. Heuvel, Cross-organizational workflow integration using contracts, Decision Support Systems 33 (2002) 247–265.

[39] T. Winograd, A language/action perspective on the design of cooperative work, Journal of Human-Computer Interaction 3 (1) (1987-88) 3–30.

[40] M. Wooldridge, An Introduction to Multiagent Systems, John Wiley & Sons, Ltd., West Sussex, England, 2002.

[41] M. Wooldridge, N.R. Jennings, Intelligent agents: theory and practice, Knowledge Engineering Review 10 (2) (1995) 115–152.

[42] M. Wooldridge, N.R. Jennings, D. Kinny, The Gaia methodology for agent-oriented analysis and design, Autonomous Agents and Multi-Agent Systems 3 (3) (2000) 285–312.

[43] E. Yu, J. Mylopoulos, Why goal-oriented requirements engineering, Proceedings of 4th International Workshop on Requirements Engineering: Foundations of Software Quality, Pisa, Italy, Presses Universitaires de Namur, 1998, pp. 15–22.

[44] H. Zhang, R. Kishore, R. Ramesh, Semantics of the MibML conceptual modeling grammar: an ontological analysis using the Bunge–Wang–Weber framework, Journal of Database Management 18 (1) (2007) 1–19.

Hong Zhang is an Assistant Professor of Computer Information Systems at Missouri State University. His research interests are computational ontology, enterprise integration, system analysis & design, multi-agent systems, and service-oriented architecture. His papers have been published or accepted for publication in Communications of the ACM, Decision Support Systems, INFORMS Journal on Computing and Journal of Database Management. He is an executive committee member of AIS SIG on Ontology-Driven Information Systems (SIG-ODIS).

Rajiv Kishore is an Associate Professor in the School of Management at the State University of New York at Buffalo. His primary research interest is in improving organizational and IT performance through the effective management of global IT and business process outsourcing projects, agile methods for business process analysis and integration, and technology and innovation management. His papers have been published or accepted for publication in Journal of Management Information Systems, IEEE Transactions on Engineering Management, Communications of the ACM, Decision Support Systems, Information & Management, Information Systems Frontiers, Journal of Database Management, and Advances in Management Information Systems, among others. Rajiv has presented his research at ICIS, HICSS, AMCIS, SIM, etc. He received a best paper award at AMCIS

2001 and was nominated for a best paper award at AMCIS 2003 and HICSS 2004. He also received a multi-year National Science Foundation research grant as a co-principal investigator in the area of IT outsourcing. Rajiv has consulted with a number of large companies, some of which include BellSouth, Blue Cross Blue Shield of Minnesota, IBM, and Pioneer Standard Electronics.

Raj Sharman is an Assistant Professor in the School of Management at the State University of New York at Buffalo. He received his B. Tech and M. Tech degree from IIT Bombay, India and his M.S. degree in Industrial Engineering and Ph.D. in Computer Science from Louisiana State University. His research streams include Distributed Computing, Decision Support Systems, Information Assurance, and Disaster Response Management. His papers have been published in a number of national and international journals. He is also the recipient of several grants from the university as well as external agencies. Raj Sharman is the co-author of the Springer Verlag edited book entitled “Ontologies: A Handbook of Principles, Concepts and Applications in Information Systems” along with Rajiv Kishore and Ram Ramesh.

Ram Ramesh is a Professor in the School of Management at the State University of New York at Buffalo. His research streams include Conceptual Modeling (Ontologies, Connectionist Modeling and Nonmonotonic Reasoning), Economics and technologies of Internet Capacity Provision Networks (CPN), and Database systems and distributed computing frameworks. His research has been funded by several DoD organizations and contractors including Army Research Institute (ARI), Air Force Office of Scientific Research (AFOSR), USAF Airforce Research Laboratory, Naval Training Systems Center (NTSC), Westinghouse, Raytheon and Samsung among others. He currently serves as an Associate Editor for INFORMS Journal on Computing, Communications of the AIS, Journal of Semantic Web and Information Systems and Journal of Intelligent Information Technologies. He is a co-Editor-in-Chief of Information Systems Frontiers and has edited volumes in Annals of OR and CACM. He is currently guest-editing an issue of the Journal of AIS on Ontologies in the context of Information Systems. He has published extensively in the above streams of research. His publications appear in journals such as INFORMS Journal on Computing, Information Systems Research, IEEE/TKDE, ACM/TODS, IEEE/SMC, Naval Research Logistics, Management Science and Communications of the ACM to name a few.
