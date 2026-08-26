---
otero_id: 13988
otero_key: "XYUH9623"
title: "Knowledge flow network planning and simulation"
authors: "Hai Zhuge"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.03.007"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Knowledge flow network planning and simulation<sup>B</sup>

Hai Zhuge

Hunan Knowledge Grid Lab, Hunan University of Science and Technology, China, China Knowledge Grid Research Group, Key Lab of Intelligent Information Processing, P.O. Box 2704-28, Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China

Available online 23 May 2005

## Abstract

Organizations and communities are held together by knowledge flow networks whether people are aware of them or not. To plan such a network is to describe a formal and optimal flow of knowledge as the basis for effective teamwork. The difficulty is that the result of such planning depends greatly on the planners’ experience. This paper proposes a pattern-based approach to knowledge flow design for more effective and efficient planning. The approach starts from basic concepts, uses a knowledge spiral to model knowledge flow patterns and operations, and lays down principles for knowledge flow network composition and evolution. Tools for planning, simulation and management of resource-mediated knowledge flow have been developed and experimentally applied to the work of research teams. The planning tool can help users to define, modify and verify a knowledge flow network and to integrate its components. The simulation tool enables users to study knowledge flow in a visualized network and to develop strategies for adapting networks to changing conditions. The basic idea is to adapt and control logistical processes for knowledge flow within teams. <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Knowledge flow; Knowledge logistics; Knowledge management; Knowledge grid; Teamwork

## 1. Introduction

With the development of information technology, many organizations are becoming more intent on knowledge than on labor. For such organizations, knowledge has become their most precious asset and their crucial competitive ability [24]. The focus of corporate managers has evolved from work process management to knowledge management. However, the question of how best to exploit knowledge to raise the productivity of teams has puzzled many researchers and managers [8,27]. Knowledge management has become an important research area of both management science and information science. Knowledge management research is concerned with knowledge itself—its creation, acquisition, transfer, and evaluation—and with its role in teamwork and other alliances, where human and social factors play an important part [29,31].

Two strategies for managing knowledge are codification and personalization. The codification strategy, a person-to-document approach, encodes and stores knowledge in online databases and various repositories where it can be easily used by any team member. Some organizations, such as Anderson Consulting and Ernst and Young, adopt mainly this strategy [14]. The personalization strategy, a person-toperson approach, creates, uses and shares knowledge peer-to-peer, supported by appropriate communication facilities [35].

Some researchers have focused on the relationship between knowledge management and work processes in knowledge-intensive teamwork [6,21]. The processes of task and knowledge sharing can be further integrated to achieve effective teamwork [34]. Process management approaches (for example, workflow management systems) have been used in the management of knowledge-intensive teamwork [20,37,38].

An emerging topic in the knowledge management area is knowledge logistics, which is concerned with methods and procedures for providing the right knowledge to the right person at the right time, especially when the Internet is used. The production and propagation of knowledge in an organization constitutes knowledge flow. The larger a geographically-dispersed and time-critical team is, the more it depends on the timely and effective flow of knowledge [26].

A logistic knowledge process takes place in a knowledge service chain or network, where the nodes are team members, software agents or knowledge portals that provide services, and the links are flows of knowledge between nodes. Ref. [32] discusses the integration of knowledge networks and the characteristics of two types of knowledge networking: direct knowledge sharing where knowledge is passed between nodes in a pure peer-to-peer networking mode, and hybrid knowledge sharing where all flow is through a central repository.

Planning the knowledge flow network for an organization means describing and designing the network to be free of unnecessary flows so that the logistic processes are efficient and effective [35]. Success in planning knowledge flow networks depends on the experience of the planner. Planning a large network is time-consuming and may need a team of planners. Without an agreed abstraction method, planners will find it hard to work together to come up with an integrated plan. These difficulties are the main obstacles to planning successful networks for large teams.

The codification strategy is supported by information technologies such as databases, data warehouses, group support systems, Web browsers, search engines, knowledge bases, workflow management systems, and knowledge interchange formats [10,27]. Knowledge management can be supported by technologies such as knowledge mining, knowledge capture and discovery, knowledge filtering, knowledge warehousing, ontology establishment and development, and intelligent agents [4,23,30]. Better worldwide knowledge sharing and management approaches are being sought by investigating future interconnection environments to overcome shortcomings of the current World Wide Web [15,34].

The knowledge flow network approach proposed here combines the codification and the personalization strategies. The main motive is to establish an effective modeling approach for knowledge flow management in teams. This paper introduces the concepts behind the approach, proposes a spiral model of knowledge flows within networks, describes the operations of flows, investigates principles for the composition of flow operations and the evolution of networks, invokes flow patterns as the basic units of analysis and planning, and describes a knowledge flow planning and simulation tool.

## 2. Knowledge flow networks: the concept and the spiral model

## 2.1. Fundamental concepts

A knowledge flow is the passing of knowledge between nodes according to certain rules and principles. A knowledge node is a team member or role, or a knowledge portal or process. A knowledge flow starts and ends at a node. A node can generate, learn, process, understand, synthesize, and deliver knowledge.

A knowledge flow has three crucial attributes: direction, content, and carrier. These are the sender/receiver (provider/consumer) node pair, the knowledge communicated, and the medium transmitting the content. Knowledge usually flows by means of communication facilities, especially the Internet. Knowledge flows from node to node in a knowledge flow network, helping people to solve problems and work in cooperation.

The concepts of connectivity, completeness, and minimum completeness of knowledge flow networks have been introduced in Ref. [35]. Each flow contains fields that locate knowledge in a knowledge space. An approach for determining the fields of the flows within a composed knowledge flow network, as well as the four types of composition of flows and nodes, were also introduced: sequential, join, split and broadcast. Knowledge content of fields can be represented in natural language, markup language, meta-concepts, and formal language.

An important property of a node of a knowledge flow network is its knowledge energy, which reflects its cognitive and creative ability, and thus determines the node’s <sup>b</sup>rank<sup>Q</sup> or <sup>b</sup>reputation<sup>Q</sup> relative to other nodes in the network. The knowledge energy is the power to drive knowledge flow, so it is also called knowledge power or knowledge intensity [38]. The total energy of the nodes in a team’s network reflects the team’s ability to solve problems and accomplish tasks. The effectiveness of teamwork requires the energy differences between nodes. The knowledge energy of a node can be measured in two ways:

(1) estimated through question-and-answer tests; or

(2) computed from the energy of its predecessor and successor nodes according to the principle:

the more nodes it passes knowledge to, the greater its energy; and, the more nodes it receives knowledge from, the greater its potential energy.

The energy of a node may change through learning. The relationship among team members, roles (nodes), knowledge energy, flows, and spaces is shown in Fig. 1.

Team members pass knowledge to each other when carrying out their tasks. Each node has some <sup>b</sup>fields<sup>Q</sup>, each of which corresponds to a subspace of the knowledge space containing and organizing knowledge according to the classification of the knowledge area dimension (denoted by $A _ { j } )$ and the classification of the knowledge level dimension (denoted by $L _ { i } ) _ { \ l }$ . The notation $\mathrm { \mathrm { ~ \right. ~ } } ^ { \left. } \mathrm { K S } _ { 1 } \Rightarrow \mathrm { K S } _ { 2 } \Rightarrow \mathrm { ~ \varepsilon ~ . ~ . \Rightarrow ~ }$ $\mathrm { K S } _ { n } \mathrm { \Delta } ^ { \mathrm { \infty } }$ represents a macro knowledge flow chain whose direction is determined by the overall energy of these nodes. The notation $\begin{array} { l l } { ^ { \mathrm { \left. \right.} } \mathrm { K S } _ { 1 } ( L _ { i } , } & { A _ { j } ) } \end{array} $ $\mathrm { K S } _ { 2 } ( L _ { i } , \ A _ { j } ) \ \longrightarrow \ . . . \ \longrightarrow \ \mathrm { K S } _ { n } ( L _ { i } , \ A _ { j } ) ^ { * }$ represents a sequential micro knowledge flow chain between these subspaces.

## 2.2. The knowledge spiral process model

Knowledge spirals are formed when knowledge flows in networks. A node can deliver knowledge to its successors either

![](/api/attachments/XYUH9623/fulltext/images/017c7873c32bcaf8be34f417f668d622b0e9c6198953efa897308f4ad0a1b661.jpg)  
Fig. 1. Relationship among roles and knowledge spaces, flows and energy.

![](/api/attachments/XYUH9623/fulltext/images/b315a0942f967101a398e777d14d69bc65d5e142589c9a279b359f80ead73b3d.jpg)  
Fig. 2. The knowledge spiral process model.

(1) by forwarding knowledge it received from a predecessor, or

(2) by passing on its own knowledge.

Fig. 2 depicts a knowledge spiral, which consists of nodes and two types of flow: external knowledge passing between nodes, and internal knowledge creation in a node, for example through abstraction, analogy, synthesis or reasoning.

Our knowledge spiral model is very similar to the hypercycle model [28]. The self-replication arc and the catalytic-support arc of the hypercycle correspond to the knowledge passing link and the knowledge processing link respectively. The differences are twofold: self-replication in the hypercycle is carried out within a node but the knowledge passing is between nodes; and the catalytic-support in a hypercycle happens between nodes but the knowledge processing happens within a node.

An effective knowledge spiral should maintain the energy differences between nodes and guarantee that only necessary knowledge is passed between nodes. The processing at a node can be modeled by an automaton CM [33]. Let KE (i, t) be the knowledge energy of the node i at time t. The knowledge flow from node i + 1 to i + 2 at time t + 1 can be expressed by the following formula:

where F is a function that transforms the state of the automaton from Sit (t) to Sit (t + 1) such that Sit $( t + 1 ) = F ( K F ( < i , i + 1 > , t ) ,$ Sit (t)).

If a knowledge process is to be carried out on multiple fields, KE (s, i, t) can be used to denote the energy in the knowledge subspace s, which relates to the content of the knowledge being passed. For simplicity, the rest of this paper focuses only on knowledge flowing between nodes.

## 2.3. Correspondence between knowledge flow and workflow

In general, a workflow executes with a relevant knowledge flow network of a team as shown in Fig. 3. A team member can take on one or more roles, and a role can also be part of other roles. Some roles take part in flow spirals and others carry out the tasks specified in work lists. A knowledge flow spiral can have instances, each of which can have one of these four states:

(1) static, defining and storing knowledge;

(2) active, fulfilling roles;

(3) suspension, waiting for something; or

(4) termination, reaching either the successful or the unsuccessful exit node.

$$
\begin{array}{l l} K F (<   i + 1, i + 2 >, t + 1) \\ = \left\{ \begin{array}{l l} \text { NULL }, & \text { if } K E (i + 1, t + 1) \leq K E (i + 2, t + 1); \\ K F (<   i, i + 1 >, t) \lor C M (K F (<   i, i + 1 >, t), S i t (t + 1), F), & \text { if } K E (i + 1, t + 1) > K E (i + 2, t + 1); \end{array} \right. \end{array}
$$

## 3. Composition of knowledge flow networks

## 3.1. Composition operations

A knowledge flow network can be made from two or more existing networks by using the following composition operations.

(1) Merge: overlay nodes common to different networks.

(2) Add flow: connect nodes of different networks.

(3) Add condition: add a join or split to express the relationship between flows related to the same node [35].

(4) Embed: put a knowledge flow network entirely within a node.

(5) Graph operations: combine with union $^ { 6 6 } \cup ^ { 9 } ,$ intersection <sup>b</sup>\<sup>Q</sup>, or minus <sup>b</sup>-<sup>Q</sup>.

Adding flows should handle the case where the nodes have knowledge fields in common. Adding conditions should handle the case where a node is itself a knowledge flow network. The algorithms for implementing the graph operations, which are too lengthy to be given here, are based on matching subnetworks. Fig. 4 shows an example of composition using two different operations.

Knowledge flow networks are composed by composing their roles. Let $R e l _ { i }$ be the relationship between the roles in the role set $R o l e S e t _ { i } ,$ let $R o l e s _ { 1 } =$ $< R o l e S e t _ { 1 } , \ R e l _ { 1 } >$ and $R o l e s _ { 2 } { = } { < } R o l e S e t _ { 2 } , R e l _ { 2 } { > }$ be the role models of two networks $K F N _ { 1 }$ and $K F N _ { 2 }$ of the same team (they may be created by different planners), and let KFN be the union of $K F N _ { 1 }$ and $K F N _ { 2 }$ (that is, $K F N _ { 1 } \cup K F N _ { 2 } )$ . The role model of KFN can be obtained by using the following union opera-

![](/api/attachments/XYUH9623/fulltext/images/c3630633524607e4c289f2a22d774f0c5a09ca4a800468dd7b133a52145eeaab.jpg)  
Fig. 3. Relationships between workflows, team members, roles and knowledge flows.

$$
\begin{array}{l} \text {tion: } R o l e s = R o l e s _ {1} \cup R o l e s _ {2} = <   R o l e S e t _ {1} \cup R o l e S e t _ {2}, \\ R e l _ {1} \cup R e l _ {2} >. \end{array}
$$

People, organizations and tasks are the three main considerations in building a knowledge flow network. Composition of networks should heed principles relating to these aspects, otherwise the resulting network may not be effective even though its components are effective.

## 3.1.1. The flow effectiveness principle

Composition of knowledge flow networks should guarantee the effectiveness of the composed network. Effectiveness will be achieved if

(1) knowledge flows in the same flow chain share the same knowledge space or subspace so that appropriate knowledge can be delivered to the right person, and so that the content of the flow can be stored in the right location in the space, and

(2) knowledge energy differences exist between nodes, because effective flow is only from a node with high energy to one with lower energy, much as water flows from a point of high pressure to one at a lower pressure.

## 3.1.2. The organizational effectiveness principle

Composition of knowledge flow networks will not be effective unless the result obeys the regulations and meets the targets of the organization, for example with respect to profit, security and copyright, particularly if the composition requires the team to expand.

## 3.1.3. The task relevancy principle

Knowledge gained by composing the team should help it complete its tasks, otherwise the composition is ineffective.

## 3.1.4. The mutual benefit principle

All members of the composed team should benefit from the composition, for example by gaining helpful knowledge or by an increase in reward. Otherwise, the team may cooperate less in the long term.

## 3.1.5. The minimum coverage principle

The composed knowledge flow network should be the smallest network that includes all the nodes and flows of the original networks. In other words, there must be no redundant flows or nodes. Otherwise effective knowledge sharing cannot be assured.

## 3.1.6. The trust principle

Effective cooperation requires that team members trust each other as much as possible. This principle encourages team members to contribute useful knowledge and to use the knowledge of others with confidence.

## 4. Knowledge flow patterns and the evolution of knowledge flow networks

A basic knowledge flow pattern is an abstraction of a category of knowledge flow networks. Using known and well-understood patterns can help planners compose new networks effectively in the same way that using design patterns leads to effective software engineering [12]. It can also promote understanding between planners.

## 4.1. Authority, peer-to-peer and hybrid patterns

The authority knowledge flow network pattern is a tree or star, as shown in Fig. 5. A knowledge flow chain is a special case of the tree pattern. The root node of the tree and the core node of the star pattern act as the leader of all the other nodes. The knowledge energy of the root and core nodes should be higher than that of all other nodes. The root and core node is called the knowledge authority of the team.

![](/api/attachments/XYUH9623/fulltext/images/83ad43778a120d5346df8a92371ace85041ba19ba363acbcb7ea3d808a3b1a4d.jpg)  
Fig. 4. Composition of knowledge flow networks.

![](/api/attachments/XYUH9623/fulltext/images/12a3f32e513434ea8267c19557213f8015e4b2130d5c19e599abfe2d74c9d7bf.jpg)  
(a) Tree pattern.

![](/api/attachments/XYUH9623/fulltext/images/046ea5cd67511a6feb82b8f6c5c4163e6a869943c0d4fb393fb48adcfd43498e.jpg)  
(b) Star pattern.  
Fig. 5. Authority pattern.

In the peer-to-peer network pattern, every node can be reached from any other node via a path consisting of nodes and links under certain constraints. Its flow characteristic is peer-to-peer, i.e., there is no authority node in the network. Fig. 6 (a) is an example of the peer-to-peer network pattern. The loop pattern is a special case of the network pattern in which each node has only one input and one output link as shown in Fig. 6 (b).

Routing strategy, like those used in peer-to-peer network [2], can be adopted to raise the efficiency of a large knowledge flow network. The strategy helps a node to target its out flows according to the energy difference between nodes and an effective locating approach.

The hybrid pattern is the composition of the authority pattern and the peer-to-peer pattern. In Fig. 7, node G of (a) is the authority node in the peer-to-peer network although it does not emit flows to all of the other nodes, and (b) is the composition of the star pattern and the loop pattern. The thicker arrows represent much knowledge flow. Further, each node can connect with a tree pattern to form a new hybrid pattern.

## 4.2. The resource-mediated pattern

The resource-mediated pattern is a network in which there is no direct flow between knowledge nodes. Any knowledge flow is between a knowledge node and a resource node. Here resources are blackboards, knowledge bases, knowledge portals, data tables, files of any form, and even soft-devices a uniform resource model [36].

![](/api/attachments/XYUH9623/fulltext/images/6286dad1a6ac265d7d7a507100dd92e6de601572f0bf191368218a730b6ac206.jpg)  
(a)

![](/api/attachments/XYUH9623/fulltext/images/02f47c78bf5c634d7d5cbd42b1ede44ff3d2f9e0545eae6e9002c0d109e156af.jpg)  
(b)  
Fig. 6. Peer-to-peer network patterns.

(b)  
![](/api/attachments/XYUH9623/fulltext/images/dd47938254de624f605f518ea058372b01f3f00a87fbd2c9a369a77d18744af5.jpg)

![](/api/attachments/XYUH9623/fulltext/images/a4238a9e5aa417b1c7e2479d594ff67fea5005c2c6045f46335b253239d22446.jpg)  
Fig. 7. Hybrid pattern.

Fig. 8 shows an example of this pattern, where circular nodes denote resources, square nodes denote knowledge nodes, downward arrows denote knowledge flows of the writing kind (that is, expression), and upward arrows denote knowledge flows of the reading kind (that is, acquisition). Flows between knowledge nodes (the dotted lines in Fig. 8) can be derived from the flows between knowledge nodes and resource nodes. For example, the knowledge flow from A to B (denoted as AYB) in Fig. 8 can be derived from A Y Resource and Resource Y B.

Constraints are imposed for control of knowledge flow in this pattern according to

(1) topic relevancy: resource providers and consumers (knowledge nodes) must be interested in the same topic,

(2) cooperation: there is cooperation between knowledge nodes, and

(3) access privilege: only qualified consumers can use certain resources.

## 4.3. The split–join pattern

The split–join pattern is based on knowledge flow composition as introduced in [35]. This pattern has an initial node with N (N 1) output flows under a condition denoted as CON , a final node with M (M 1) input flows under a condition denoted as CON , and a black box that receives the flows from the initial node and sends its own output flows to the final node, as shown in Fig. 9.

For the pattern to be logically consistent the two conditions must be reconciled according to the following four rules.

![](/api/attachments/XYUH9623/fulltext/images/7ac8b4f894927bb301208e84022070c63da95efecb43bf11a66455c05d6d9fd4.jpg)  
Fig. 8. Resource-mediated knowledge flow pattern.

Rule 1. IF $\mathrm { C O N _ { 1 } } \mathrm { = } \mathrm { ^ { \cdot } a n d \mathrm { - } s p l i t ^ { \cdot } \mathrm { ~ \ T H E N ~ \ C O N _ { 2 } } } \mathrm { = } \mathrm { ^ { \cdot } a n d } \mathrm { - }$ join’ or $\mathrm { C O N } _ { 2 } { = } ^ { \cdot } \mathrm { o r - j o i n } ^ { \cdot } ;$

Rule 2. IF $\mathrm { C O N _ { 1 } } \mathrm { = } \mathrm { ^ { \circ } o r { \mathrm { - } } s p l i t ^ { \prime } \ T H E N \ C O N _ { 2 } } \mathrm { = } \mathrm { ^ { \circ } o r { \mathrm { - } } j o i n { ' } j }$

Rule 3. IF $\mathrm { C O N } _ { 1 } { = } ^ { \mathrm { 3 } } \mathrm { x o r - s p l i t } ^ { \mathrm { 3 } }$ THEN $\mathrm { C O N } _ { 2 } { = } ^ { \circ } \mathrm { x o r } { - }$ $\mathrm { j o i n ^ { \prime } \ o r \ C O N } _ { 2 } { = } ^ { \prime } \mathrm { o r { - } j o i n ^ { \prime } } ;$

Rule 4. IF $\mathrm { C O N } _ { 2 } { = } ^ { \cdot } \mathrm { a n d } { \mathrm { - } } \mathrm { j o i n } ^ { \cdot }$ THEN $\mathrm { C O N } _ { 1 } { = } ^ { \circ } \mathrm { a n d } -$ split’.

## 4.4. Evolution of a team’s network

A team’s knowledge flow network may change as work proceeds to adapt it to change in the team and to raise the efficiency of knowledge flow. Such network evolution should not disturb team members work modes and should not interrupt their current work.

The example of Fig. 10 shows how a research team’s knowledge flow network might evolve. In the first stage, the team has a tree-like pattern with a leader and three members working in separate areas. These three are expected to learn for themselves at this stage and only communicate with their leader. In the second stage, team members are allowed to learn from each other. The pattern unites the existing pattern and the loop pattern. In the third stage, new members are added to the team to work on the three areas. The pattern now unites the prior pattern and three tree-like patterns. In the fourth stage, these new members are

![](/api/attachments/XYUH9623/fulltext/images/48d1e4efd0057a2f29f7483e0dbdc3d6825edae814bc383ad38c74843a291a11.jpg)  
Fig. 9. <sup>d</sup>Split–join’ pattern.

![](/api/attachments/XYUH9623/fulltext/images/771adf62b06f33769080449155803b5b2e71c51f6acaa5fb3b1205ebae2a9fc2.jpg)  
Fig. 10. Evolution of a research team’s knowledge flow network.

allowed to learn from each other. The new pattern thus unites the prior pattern and the loop pattern. This example shows that a knowledge flow network can evolve through applying a set of operations to knowledge flow patterns.

## 4.5. Examples

An example of using knowledge flow patterns with roles is the university research and teaching team shown in Fig. 11. Member <sup>b</sup>Hai<sup>Q</sup> can take on three roles:

(1) The teacher, as a node in a tree-like broadcasting pattern.

(2) The supervisor, as a node in the union of a tree-like broadcasting pattern and a loop pattern.

(3) The department head, as a node in a tree-like broadcasting pattern.

![](/api/attachments/XYUH9623/fulltext/images/255fcbf7d2c2c89a328d3c263bf46ebb2701a0c203021cea15c5da95c1a79cb8.jpg)  
Fig. 11. Example of using knowledge flow patterns through roles.

A software development team is a typical knowl edge organization. Beyond traditional technical aspects like software tools and development methodologies, effective knowledge management is an important way to raise the efficiency of software development by teams. Knowledge management in a software team has two main aims:

(1) effective sharing of software experience and resources, and

(2) appropriate organization of the team.

The first aim can be met by using Internetbased advanced platform like the Knowledge Grid [34]. The software tool KCB, which will be described in Section 6, can be used as the human– computer interface for collecting raw knowledge and experience.

![](/api/attachments/XYUH9623/fulltext/images/8559f86088f5c9af66af14007b63f9c5411b0420b7df7428c23c71c30a4d22b6.jpg)  
Fig. 12. Using knowledge flow components to construct an agile software development team

The second aim can be met by using knowledge flow components to construct a network for an agile software development team. As shown in Fig. 12 a software development process usually takes five steps: analysis, design, programming, testing and maintenance. Workflow sets out the tasks included in each step. Using Workflow, the team organizer can select knowledge flow components suited to constructing the team’s knowledge sharing model. Roles are assigned to knowledge nodes.

A software team is organized according to the requirements of the roles. Using a knowledge flow network in this way means that

(1) team members can work in different regions, and

(2) a team member can take on more than one role at different times and can effectively share knowledge, software experiences, and resources such as software components.

A knowledge flow network for a new agile software development team can be rapidly formed by composing existing flow patterns or by reusing and adapting existing networks.

## 5. A knowledge flow network planning and simulation tool

## 5.1. Knowledge flow network components

A large building block used in the design of knowledge flow networks is the knowledge flow component, which has the following three characteristics:

(1) Relative independence. Processing within a component should be relatively independent of that in other components. Consequently the density of knowledge flows within a component is usually higher than that between components.

(2) Encapsulation. It can itself be used as a knowledge node. A knowledge flow component can be normalized to have just one initial node and one successful final node. Any external flow can only use the component through its input and output nodes.

(3) Internal process completeness. The knowledge flow process is complete in both build-time (definition phase) and run-time (execution phase).

A component is called definition complete if:

(1) every internal node has at least one input and one output flow,

(2) every internal flow except from the final node goes to an internal node,

(3) the final node can be reached from the initial node, and

(4) there is no isolated node or subnetwork.

Execution completeness requires that all restrictions and conditions be met during execution, and that the execution of the component can be treated as that of a single knowledge node.

In summary, a knowledge flow component is a network that describes a complete knowledge flow process, and that is independent, encapsulated, and complete.

## 5.2. Planning

Ordinary information systems process and manage information, so their analysis and design focus on information structure and information flow. Cooperative information systems use the same technologies for delivering information but they typically use different representation technologies so as to support mutual understanding. The planning of a knowledge flow network focuses on the analysis of cooperation and its knowledge flow. The two kinds of system have enough in common for the approaches and strategies used in the analysis of information systems and in workflow systems to be adapted for use in component-based knowledge flow design [37].

The general strategy is the incorporation of the topdown refinement and bottom-up verification strategies, like those in requirement analysis, design and verification suggested in software engineering methodology [17]. The planning of knowledge flow network is accomplished through the incorporation of the designer and the tool. Fig. 13 depicts the following planning process.

(1) Analyze the cooperation and workflow within the team according to task and organization structure, and the information flow between team members. The planning tool can help with this step by recording and analyzing the task relevant information flows from file transmission and e-mails between members.

(2) Lay out the initial knowledge flow network.

(3) Construct the componential knowledge flow network by defining components according to the designer’s experience and discussed patterns.

(4) Find useful components or patterns in the component repository, and design components that are not to be found there. Newly designed components will be put into the component repository. Remote storage and retrieval of components should be provided if the network is geographically dispersed.

(5) Compose the selected components to form the final knowledge flow network.

![](/api/attachments/XYUH9623/fulltext/images/19ef276002090ac13a41b66f6b8d18dec26803b77b375d8cac439e1a178dfa43.jpg)  
Fig. 13. A reference planning process.

(6) Use the planning tool to specify the features of each node and flow for each component from the top down.

(7) Verify the whole network with the help of the planning tool and remove any errors. The general strategy used in this step is bottom-up.

## 5.3. A planning tool

We have used Java to develop a prototype tool for component-based planning. The tool can help planners to define a complex top-level knowledge flow network and then to refine it by expanding nodes into components that ensure the best cooperation between team members. During definition, high priority should be given to reusing existing patterns and components.

Fig. 14 shows the main interface of the tool. The network is defined by clicking on the buttons in the upper part of the interface and drawing in the middle part. The hierarchy of nodes, where the high-level nodes can be expanded, is shown to the left. The network being defined is shown in the middle. Planners can edit the network by using <sup>b</sup>cut<sup>Q</sup> and <sup>b</sup>add<sup>Q</sup> operations. The properties of the nodes and flows can be specified by clicking on nodes and flows in the display and filling out the fields then shown at the bottom of the interface. At any time the tool can check for correctness according to the logical structure, conditions and principles.

## 5.4. A team organization principle

Trust between team members is an important factor that affects cooperation. The planning tool includes a special matrix TRUST that records the need for and level of trust between team members and supports reasoning for finding out the implied trust relationship. Each element in TRUST is a function of time $t r u s t _ { i j } ( t )$ , which represents the degree to which member i trusts member j at time t. The elements can be initialized by the tool or the team leader and then adjusted according to each team members’ feedback scores about the effectiveness of cooperation during work. A vector records the evolution of $t r u s t _ { i j } ( t )$ in the lifetime of cooperation. The tool computes the average trust degree at any time and can display its evolution curve to help analyze the development trend. The team leader has the privilege of seeing the trust degrees between team members.

![](/api/attachments/XYUH9623/fulltext/images/c111c6e56c99c4fbf6825f5d4a5946e392d646e2d0a2d57bae4a202222cde159.jpg)  
Fig. 14. A component-based knowledge flow definition tool.

Trust levels of individuals will reflect feedback about their effectiveness in teamwork. The levels are used in selecting team members when planning knowledge flow networks. People more trusted by current team members will be preferred when adding new members.

![](/api/attachments/XYUH9623/fulltext/images/60a8f956bd9a05a1fc66cd9efeca979c6941f6076140ba1ea70b93e6ff2cb1ab.jpg)  
Fig. 15. Simulation interface: the window showing the change of knowledge energy.

The distribution of page ranks of the Web obeys the <sup>b</sup>power-law<sup>Q</sup> and <sup>b</sup>the rich get richer<sup>Q</sup> rules, and so do many other networks with scale-free and competitive characteristics [1]. However, knowledge tends to level off like water, a <sup>b</sup>the poor get richer<sup>Q</sup> rule, because a node with less knowledge can gain from nodes with more (that is, knowledge intensities always tend to equilibrium). The distribution of trust levels is somewhat similar to Web page ranks because nodes with high trust levels have more opportunities to cooperate than nodes with low trust levels. From the above discussion we draw the following principle.

## Principle for selecting team members

A team should select the person who has more knowledge and is more highly trusted by team members.

## 5.5. Simulation

A knowledge flow network can be simulated to examine its dynamic features under all conditions.

Fig. 15 shows the simulation interface, where the background displays the network being simulated. Users can click on any node or flow to be shown its data. The front window shows the knowledge space of the node that the user has clicked on and the evolution of its knowledge content. The contrasting rectangle moves around as the subspace of the current active flow changes. The window behind the front one displays the change in the knowledge content of all nodes as they evolve.

Users can watch the distribution of knowledge around the nodes during simulation so that they can adjust the network when an ineffective flow is revealed. Fig. 16 shows the interface that displays the changing subspaces of a selected flow and its direction.

Using this simulation, a planner can get a feel for how knowledge accumulates and flows within a network, can check whether the network is working properly with respect to trust and knowledge level differences within the network, and can verify that its structure satisfies the composition principle (note that here we do not show trust level differences).

Rules of thumb for adjusting the knowledge flow network can be gained from experience with simulation of different networks. These rules are important assets that can help an organization adapt to changes in its environment.

![](/api/attachments/XYUH9623/fulltext/images/dee9a9a32f1a4ce014a48a163422af0e02629c7f540094eaadff2284027f8e3b.jpg)  
Fig. 16. Simulation interface: visualizing the changes of knowledge flows.

## 6. Team-KCB: a resource-mediated knowledge flow management tool

Knowledge flow management tools can help team members record and receive knowledge. A good graphical user interface in such a tool can help team members make their tacit knowledge explicit so that it can then become tacit for other team members. Research into the art, culture and psychology of such interfaces is beyond the scope of this paper.

We have developed two types of knowledge flow management interface: one uses an orthogonal classification semantic space (Resource Space Model), and the other is team-KCB (Knowledge Collection Board). Prototypes are shown in http://kg.ict.ac.cn. The main reason for adopting the former is that knowledge can be effectively and efficiently organized because the interface matches the stored data structure [34]. The reason for adopting the latter is its utility—many users are quite familiar with bulletin boards.

Team-KCB supports resource-mediated knowledge flow management. Fig. 17 shows four interfaces provided by the tool. Interface (a) is a bulletin board, where team members can post and read knowledge from subspaces that interest them. Interface (b) lists questions and answers from team members. Interfaces (c) and (d) provide for posting and answering questions. Any team member can attach reference files to knowledge posted through interface (d).

In bulletin board mode, knowledge flows by asking and answering; from the person/role answering to the person/role asking. The knowledge energy of a node is roughly proportional to the number of its outgoing flows.

Some relationships between resources reflect knowledge flows between their authors. For example, citation relationships between scientific papers reflect knowledge flows from the author(s) being cited to the author(s) doing the citing. A citing paper is the confluence of the cited incoming knowledge and the innovation of its author(s). So a resource-mediated knowledge flow management tool can be very useful in managing knowledge and in exploring the rules of innovation in scientific research.

Hyperlinks between resources are a kind of weak citation. Some semantic relationships between resources can be established to refine the citation relationship by using text-mining approaches. Resource-mediated knowledge flows through four types of links: question answering links, information flows, citation links, hyperlinks, and semantic links, as shown by the dotted arrows in Fig. 18.

The rank of a resource in a network can be calculated by combining:

(1) its rank in the citation network,

(2) its rank in the hyperlink network,

(3) its rank in the semantic link network, and

(4) its rank in the information flow network.

These three networks are all scale-free and competitive, so algorithms for computing these ranks can be designed with reference to the PageRank algorithm [18]. The reputation of the knowledge nodes in networks is reflected to a certain extent by their ranks in the question-answering network and by the mediating resources’ ranks.

A background system (a Knowledge Grid) classifies, stores, and refines the raw knowledge collected from the KCB. The Knowledge Grid uses the resource space model to share knowledge efficiently. Team-KCB analyzes text to find hyperlink and citation relationships between text resources.

## 7. Related work, discussion and implications

## 7.1. On epistemology and organizational learning

Epistemology is about knowledge and knowing, and can be traced back to the days of Plato and Aristotle. Empiricismregards knowledge as the prod uct of sensory perception, while rationalismregards it as the product of rational reflection. Recent stud ies show that knowledge can be transmitted from one person to another and can even actively pursue goals of its own (this idea matches the ideal of knowledge logistics, Knowledge Grid and softdevices [34,36]), so it loses dependence on any individual person. Researchers have also noticed the importance of communication and social processes in the development of knowledge. Some researchers even believe that knowledge processes construct social systems [16].

![](/api/attachments/XYUH9623/fulltext/images/548ac9f47bba1eef6684bab1ac46a97ee197dfe2e6566c555986d74d884cb954.jpg)  
Fig. 17. Team KCB—a tool managing resource-mediated knowledge flow networks.

In organizational learning, a two-dimensional space for describing knowledge has been suggested [25]. The epistemological dimension classifies knowledge into explicit knowledge, which can be formally expressed, and tacit knowledge, which is hard to formalize. The ontological dimension classifies knowledge that is shared among the members of an organization. Knowledge flows within dimensions in four ways other than those introduced in this paper: 1) social, in which knowledge moves socially from the individual to the organization (from small to large); 2) externalisation, in which knowledge moves from tacit to explicit; 3) combination, in which knowledge of small teams is combined and coordinated to become the knowledge of a large team; and, 4) internalization, in which an organization’s knowledge is transformed from explicit to tacit. A third dimension of the knowledge life cycle is suggested to reflect the evolution of knowledge [26].

![](/api/attachments/XYUH9623/fulltext/images/e7e1a9c3351249d719869421cdc9f3bdae77e36135d27e351ef29bdb1e0d555c.jpg)  
Fig. 18. Multiple types of links reflect resource-mediated knowledge flows.

## 7.2. On research scope, method and technical feasibility

Isolating an object for research is important to modelling. External knowledge acquisition increases nodes’ energy, which makes knowledge flows more effective. This paper mainly discusses the propagation of external and explicit knowledge that can be formalized, transmitted via communication media, and stored in digital machinery. The planning of knowledge flow networks seeks to formalize and optimise logistic processes. The network itself is a kind of organizational knowledge, which is relevant to the roles in an organization but not to the individuals.

Here we are more concerned with the content and effective sharing of knowledge in distributed teams, especially in agent-based virtual organizations [22]. A number of approaches in the AI field can be used to express the content of knowledge. Content can be layered as concepts, axioms, rules and methods, can be classified according to its application domains, can be identified according to its locations, and thus can be organized in a three-dimensional knowledge space [34]. Our work also considers a uniform resource model that encapsulates internal flows and activity processes to actively provide appropriate on-demand knowledge services [36].

We have not so far seen any other tools that support knowledge flow network planning and management. However, some knowledge management tools have been developed and used. For example, the IBM’s <sup>b</sup>Intelligent Miner<sup>Q</sup> and <sup>b</sup>Web fountain<sup>Q</sup> are knowledge capturing and understanding tools [5], and the Lotus Notes based <sup>b</sup>Knowledge Xchange<sup>Q</sup> is for knowledge sharing and is used by Andersen Consulting professionals.

The Internet provides the communication facility needed for globally distributed knowledge management. The setting up of Web-based knowledge portals and workplaces has been investigated [21]. The future interconnection environment will provide better support for the knowledge logistic processes of geographically distributed teams [3,11]. The Knowledge Grid provides for organizing and sharing knowledge at several levels so that members of a team can solve problems or accomplish tasks efficiently [34]. A prototype of the Knowledge Grid based on a multi-dimensional knowledge space has been implemented based on the

Semantic Web representation, which provides the basis for understanding the communication between roles (team members and software mechanisms) [9,25,19]. The future intelligent Grid environment will provide a better platform for the Knowledge Grid.

## 7.3. On knowledge flow patterns and organizational structure

Grady Booch pointed out in the foreword of [12] that all well-structured object-oriented architectures are full of patterns. Using software design patterns promotes mutual understanding between designers and increases the reusability of software components. The knowledge flow network patterns introduced in this paper have the same advantages in planning team networks.

What is a well-structured knowledge organization? Drucker believes that the ideal management patterns of knowledge organizations already exist in entities such as orchestras and hospitals [8]. This suggests that a well-structured knowledge team has fewer control nodes. Any team member can directly communicate with the leader and with other members who work on the same task. The proposed knowledge flow patterns have the same properties.

## 7.4. Implications

The tools introduced in this paper are prototypes demonstrating the feasibility of the proposed approach. Application to research teams has led us to the following conclusions:

<sup>!</sup> Clarifying the scope and intention of knowledge sharing makes it more effective. Task-oriented knowledge flow network construction can achieve better sharing. The network of a knowledge team should adapt to change in a task. The difficulty lies in adapting the network as the team evolves.

<sup>!</sup> The simpler a knowledge flow network is the better its sharing. Pattern-based network construction can simplify the structure of a network by reusing wellunderstood components.

<sup>!</sup> Getting team members to make their tacit knowledge explicit is very important in making sharing more effective. A well-designed and friendly interface for this process can make members more willing to contribute.

<sup>!</sup> The higher a team member’s knowledge level and trust rank is, the more important is his/her role in carrying out a task. The member of highest rank should be placed at the root of a knowledge flow tree.

<sup>!</sup> The more relevant the content of knowledge flow is to the task, the more effective the teamwork.

## 7.5. Ongoing work

Effective knowledge sharing also has to do with humanity, psychology, organization regulation, law and so on [7]. Belief and trust of team members affect knowledge sharing, particularly in relation to copyright. Ongoing research concerns the following aspects:

(1) distributed cooperative planning of knowledge flow networks;

(2) value chains in knowledge flow networks;

(3) knowledge logistic strategies and applications in distributed research teams;

(4) approaches for dynamically forming and adapting knowledge flow networks;

(5) approaches that incorporate the factors of intention, trust and belief [13], and the relevant reasoning for forming effective teams;

(6) good graphical user interfaces that can encourage users to express knowledge and help users understand displayed information;

(7) algorithms that match patterns and components and find matches in a repository;

(8) investigating the primitive patterns of networks and proving the sufficiency of the patterns; and,

(9) applications in e-business and e-science, especially in real peer-to-peer network platforms.

## 8. Conclusion

Knowledge growth and effective knowledge sharing are the main objectives in organizing knowledge teams. This paper proposes an approach to knowledge flow planning based on patterns, and tools for such planning based on our investigation of the processes, principles and rules of team knowledge sharing.

The approach has the following major advantages:

(1) It simplifies large-scale knowledge flow network planning by using patterns, components, composition, top–down refinement, and bottom–up verification;

(2) It raises the reliability of knowledge flow management by localizing flows within components, just as software components localize errors and raise the reliability of software;

(3) It raises the understandability of knowledge flow networks by establishing common component patterns;

(4) Knowledge flow components help a large team work in small units, which usually leads to better innovation than in large units because of the great reduction in the need for communication [3]; and,

(5) It raises the adaptability and mobility of knowledge management.

Component-based knowledge flow management can prevent change in a part from affecting the whole, and adapt well to any change in flow patterns caused by organizational changes.

The proposed approach and tools are techniques for planning and simulating the knowledge flow networks of large teams, strategic alliances, or virtual organizations, which can be either centralized or decentralized. Successful use of the planning tool depends on the analysis of the organization’s architecture and management regulations, the balance of efficiency, mobility and creativity, and also on social and human factors. This paper takes a small but important step towards the goal of efficient and effective knowledge flow network planning.

## Acknowledgement

The author thanks Neville Holmes for his constructive comments. Thanks also go to our team members, especially L. Ding, J. Bi, W. Guo and R. Jia for their assistance in implementing the software prototypes.

## References

[1] L.A. Adamic, B.A. Huberman, Power-law distribution of the world wide web, Science 287 (24) (2000) 2115.

[2] H. Balakrishnan, et al., Looking up data in P2P systems, Communications of the ACM 46 (2) (2003) 43–48.

[3] T. Berners-Lee, J. Hendler, O. Lassila, Semantic web, Scientific American 284 (5) (2001) 34– 43.

[4] J.M. Bradshaw, M. Greaves, H. Holmback, Agents for the masses? IEEE Intelligent Systems 14 (2) (1999) 53 – 63.

[5] S. Cass, A fountain of knowledge, IEEE Spectrum 41 (1) (2004 Jan.) 60–67.

[6] T.H. Davenport, S.L. Jarvenpaa, M.C. Beer, Improving knowledge work process, Sloan Management Review 34 (4) (1996) 53– 65.

[7] K.C. Desouza, Facilitating tacit knowledge exchange, Communications of the ACM 46 (6) (2003) 85– 88.

[8] P.F. Drucker (Ed.), Harvard Business Review on Knowledge Management, Harvard Business School Press, Boston, MA, 1998.

[9] D. Fensel, et al., OIL: an ontology infrastructure for the semantic web, IEEE Intelligent Systems 16 (2) (2001) 38 – 45.

[10] R. Fikes, A. Farquhar, Distributed repositories of highly expressive reusable ontologies, IEEE Intelligent Systems 14 (2) (1999) 73– 79.

[11] I. Foster, Internet computing and the emerging Grid, Nature 7 (2000 December) (www.nature.com/nature/webmatters/grid/ grid.html).

[12] E. Gamma, R. Helm, R. Johnson, J. Vlissides, Design patterns: elements of reusable object-oriented software, Pearson Education, 1995.

[13] B.J. Grosz, S. Kraus, Collaborative plans for complex group action, Artificial Intelligence 86 (1996) 269 – 357.

[14] M. Hansen, N. Nohria, T. Tierney, What’s your strategy for managing knowledge? The knowledge management yearbook 2000–2001, Butterworth-Heinemann, Woburn, MA, 2000.

[15] J. Hendler, Agents and the semantic web, IEEE Intelligent Systems 16 (2) (2001) 30– 37.

[16] F. Heylighen, A cognitive–systemic reconstruction of Maslow’s theory of self-actualization, Behavioral Science 37 (1992) 39– 58.

[17] I. Jacobson, G. Booch, J. Rumbaugh, The Unified Software Development Process, Addison-Wesley, 1999.

[18] J. Kleinberg, S. Lawrence, The structure of the Web, Science 294 (30) (2001) 1849– 1850.

[19] M. Klein, XML, RDF, et al., IEEE Internet Computing 5 (2) (2001) 26– 28.

[20] F. Leymann, D. Roller, Workflow-based applications, IBM Systems Journal 36 (1) (1997) 102– 122.

[21] R. Mack, Y. Ravin, R.J. Byrd, Knowledge portals and the emerging knowledge workplace, IBM Systems Journal 40 (4) (2001) 925– 955.

[22] M. Maybury, Collaborative virtual environments for analysis and decision support, Communications of the ACM 14 (12) (2001) 51– 54.

[23] T. Nasukawa, T. Nagano, Text analysis and knowledge mining system, IBM Systems Journal 40 (4) (2001) 967– 984.

[24] I. Nonaka, The knowledge creating company, Harvard Busi ness Review 69 (1991) 96– 104.

[25] I. Nonaka, A dynamic theory of organizational knowledge creation, Organization Science 5 (1) (1994) 14 – 37.

[26] M.E. Nissen, An extended model for knowledge-flow dynamics, Communications of the Associations for Information Systems 8 (2002) 251– 266.

[27] D.E. O’Leary, Enterprise knowledge management, Computer 31 (3) (1998) 54 – 61.

[28] K. Oida, The birth and death process of hypercycle spirals, in: R.K. Standish, M.A. Bedau, H.A. Abbass (Eds.), Artificial life VIII, MIT Press, 2002.

[29] S. Parise, J.C. Henderson, Knowledge resource exchange in strategic alliances, IBM Systems Journal 40 (4) (2001) 908 – 924.

[30] W. Pohs, G. Pinder, C. Dougherty, M. White, The Lotus knowledge discovery system: tools and experiences, IBM Systems Journal 40 (4) (2001) 956– 966.

[31] J.C. Thomas, W.A. Kellogg, T. Erickson, The knowledge management puzzle: human and social factors in knowledge management, IBM Systems Journal 40 (4) (2001) 863–884.

[32] A. Tiwana, Affinity to infinity in peer-to-peer knowledge plat forms, Communications of the ACM 46 (5) (2003) 77– 80.

[33] H. Zhuge, Conflict decision training through multi-space coop eration, Decision Support Systems 29 (2) (2000) 111– 123.

[34] H. Zhuge, China’s e-science Knowledge Grid environment, IEEE Intelligent Systems 19 (1) (2004) 13–17.

[35] H. Zhuge, A knowledge flow model for peer-to-peer team knowledge sharing and management, Expert Systems with Applications 23 (1) (2002) 23– 30.

[36] H. Zhuge, Clustering soft-devices in the semantic grid, IEEE Computing in Science and Engineering 4 (6) (2002) 60–63.

[37] H. Zhuge, Component-based workflow systems design, Deci sion Support Systems 35 (4) (2003) 517– 536.

[38] H. Zhuge, The Knowledge Grid, World Scientific, 2004 (Singapore).

![](/api/attachments/XYUH9623/fulltext/images/4bf38648e0f0f18613fabe42b0dd1f1a384c3e181f66f570b54c9e43fbab5294.jpg)

Hai Zhuge is a professor at the Institute of Computing Technology, Chinese Academy of Sciences. He is the director of the Key Lab of Intelligent Information Processing, Chinese Academy of Sciences, and the founder of the China Knowledge Grid Research Group (http://kg.ict.ac.cn), which has 30 young researchers. Currently, he is the chief scientist of the China National Semantic Grid Project. He was a keynote speaker at the $2 ^ { \mathrm { n d } }$ International Conference on Grid

and Cooperative Computing, the $5 ^ { \mathrm { t h } }$ International Conference on Web-Age Information Management, the 1<sup>st</sup> International Workshop on Massive Multi-Agent Systems, and the 1<sup>st</sup> International Workshop on Autonomous Intelligent Systems—Agents and Data Mining. He was the Chair of the $2 ^ { \mathrm { n d } }$ International Workshop on Knowledge Grid and Grid Intelligence and will be the program co-chair of the $4 ^ { \mathrm { t h } }$ International Conference on Grid and Cooperative Computing. He has organized two special issues on Knowledge Grid. He is serving as the Area Editor of Journal of Systems and Software, the Associate Editor of Future Generation Computer Systems, the area editor of the Journal of Computer Science and Technology, and on the editorial boards of Information and Management and Electronic Commerce Research and Applications. His current research interest is the model and theory on future interconnection environment and conduct applications in China. His monograph The Knowledge Gridis the first book in the area. He is the author of over ninety papers which appeared mainly in leading international conferences and journals such as Communications of the ACM; IEEE Computer; IEEE Intelligent Systems; IEEE Computing in Science and Engineering; IEEE Transactions on Systems, Man, and Cybernetics; Information and Management; Decision Support Systems; Journal of Systems and Software; Concurrency and Computation: Experience and Practice; Knowledge-based Systems; and, Expert Systems with Applications. He is a senior member of IEEE.
