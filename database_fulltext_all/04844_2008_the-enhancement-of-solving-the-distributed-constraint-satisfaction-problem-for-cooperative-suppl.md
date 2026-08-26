---
otero_id: 4844
otero_key: "X72FQ6H2"
title: "The enhancement of solving the distributed constraint satisfaction problem for cooperative supply chains using multi-agent systems"
authors: "Fu-ren Lin; Hui-chun Kuo; Shyh-ming Lin"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.02.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The enhancement of solving the distributed constraint satisfaction problem for cooperative supply chains using multi-agent systems

Fu-ren Lin <sup>a,⁎</sup>, Hui-chun Kuo <sup>b</sup>, Shyh-ming Lin <sup>b</sup>

<sup>a</sup> Institute of Technology Management, National Tsing Hua University, Hsinchu City 300, Taiwan Department of Information Management, National Sun Yat-sen University, Kaohsiung City 804, Taiwan

Received 15 February 2006; received in revised form 2 February 2008; accepted 7 February 2008 Available online 15 February 2008

## Abstract

Facing global and dynamic competition, companies need to coordinate with supply chain partners to effectively fulfill customer orders. Considering the risk of exposing trade secrets and the cost of gathering information, the centralized constraint optimization mechanism is infeasible when it comes to handling distributed scheduling problems in a real-world environment. This paper proposes an agent-based distributed coordination mechanism that integrates negotiation techniques with genetic algorithm to plan quasi-optimal order fulfillment schedules to meet customers' demands. In this study, to evaluate the performance and feasibility of our proposed mechanism, experiments are conducted using a mold manufacturing supply chain as an example. The experimental results reveal that the proposed distributed coordination mechanism is a feasible approach to resolving the order fulfillment conflicts in a supply chain.

© 2008 Elsevier B.V. All rights reserved.

Keywords: Supply chain management; Multi-agent systems; Distributed constraint satisfaction problem; Automated negotiation; Genetic algorithm; Distributed scheduling problem

## 1. Introduction

In today's globally and dynamically competitive environment, companies collaborate with their supply chain partners to reach optimum performance. However, due to uncertainties from demand, manufacturing, and supply sides [21], traditional supply chains, in which companies operate based on the push model with traditional media to interact with each other, are unable to agilely respond to these uncertainties. In a supply chain with push model, products are pushed from upstream suppliers to downstream customers. Since push model is not customer oriented, the changes of market demands may render long order fulfillment cycle time, delayed delivery, overstocking, and in turn, low customer satisfaction. In order to satisfy customer demands with controlled cost and time, companies need to effectively coordinate with supply chain partners to promptly respond to variations of outside world.

The increase of information sharing among supply chain partners has been effectively used for improving supply chain performance [1–3,5,10,11]. Companies share information with their supply chain partners via electronic data interchange or advanced XML-based information exchange to aid managers in coordinating supply chain activities. The inter-organizational information systems are usually equipped with coordination mechanisms to enhance the supply chain performance in business processes [22], e.g., order fulfillment, product development, and customer service. Guo, Fang and Whinston [8] built a macro prediction market into organizations' supply chain information system to align different supply chain partners' self-interests and to enable more effective information sharing and better decision-making.

Recently, the multi-agent system (MAS) emerged and has been viewed as a new information platform for managing supply chains. Caridi and Cavalieri reviewed the MAS related literatures and found that the MAS is broadly applied in supply chains ranging from order quotation to distribution. Among these applications, 20% are in the scheduling domain [4]. A MAS models participant companies in a supply chain as agents [7,21], which interact and cooperate with each other to achieve the global performance of the supply chain [4]. Agents possessing such characteristics as autonomy, reactivity, pro-activeness and social ability [23] can autonomously and intelligently execute complicated tasks. Swaminathan and his coauthors [21] proposed a multi-agent based framework using modeling and simulation approaches to enable rapid development of customized decision support for supply chain management. Sadeh and his coauthors [20] provided a multi-agent supply chain coordination tool, called MASCOT, to help companies in supply chain plan order fulfillment schedules and coordinate their activities. Lin and his colleagues [12] proposed an integrated multi-agent framework which integrated simulated and physical agents to enable companies to form dynamic business processes in a supply chain. With the integrated multiagent system, conflicts among companies can be well handled through information exchange and coordination. Intelligent agents, embedded into companies to upgrade a business into e-business, are coined as intelligent business agents [17].

In a supply chain, companies allocate resources to fulfill the incoming customer orders. The resource allocation, a scheduling problem, is constrained by resources available in a distributed environment. An order fulfillment process thus can be modeled as a distributed constraint satisfaction problem (DCSP) [13,26].

A DCSP is defined as a problem where variables and constraints are distributed among involved agents. To solve a DCSP is to find a set of values for variables to satisfy inter-agent constraints to reach consensus among agents [25]. Unlike the centralized optimization problem, in a DCSP, no agent has a complete view of the states of participant agents; thus, an agent merely maintains its own perspective on its cognitive world.

This study develops a distributed coordination mechanism via sharing necessary individual information to coordinate with each other to obtain an optimal solution for a DCSP in resolving the conflicts of order fulfillment schedules in a supply chain, The coordination mechanism comprises two elements: a multi-agent system which improves the information transparency of supply chain, and a revised DCSP solving method which generates an optimal order fulfillment schedule in a distributed scheduling environment.

The revised method differs itself from other previously proposed DCSP solving methods. Those proposed methods prior to this study focus on finding a globally feasible solution which may not guarantee to be optimal [13]. The revised method aims at finding an approximately optimal solution for a DCSP. This study integrates a negotiation technique with genetic algorithm (GA), called NegoGA, to plan the order fulfillment process in a supply chain.

The negotiation technique in NegoGA helps companies in the supply chain make a series of decisions to reach a mutually acceptable solution, and the GA leads the compromise to reach approximate optimality. GA is an evolutionary learning technique applied to search for near optimal solutions. Three reasons explain why GA is adopted in this study. First, GA is suitable for solving such large sized optimization problem [16] as the negotiation problem in a supply chain. Second, GA is suitable for solving a problem with four characteristics: (1) the problem can be described as a sequence of moves; (2) the sequence may converge towards a final state when all states are comparable regarding their contributions to a certain goal; (3) moves that contribute to the achievement of a given result can be identified; (4) the credit for good results can be attributed to contributing moves [14]. The coordination problem in a supply chain possesses the aforementioned four characteristics. Finally, GA is suitable for working with a multi-agent system [18].

The distributed coordination mechanism can obtain a global optimal schedule by iteratively helping supply chain partners find their optimal local schedules and then allowing them to negotiate with their partners to resolve conflicts. A company can obtain an optimal schedule to fulfill orders using the distributed coordination mechanism right after receiving a customer order.

This study designs two sets of experiments to demonstrate the quality of optimal solution found by

Table 1  
Methods for solving DCSP

<table><tr><td rowspan="2">Problem solving technique</td><td colspan="3">Problem type</td></tr><tr><td>Single local variable problem</td><td>Multiple local variable problem</td><td>Distributed partial CSP</td></tr><tr><td>Backtracking</td><td>Asynchronous backtracking</td><td></td><td>Asynchronous incremental relaxation</td></tr><tr><td>Iterative improvement</td><td>Distributed breakout</td><td></td><td>Incremental distributed breakout</td></tr><tr><td>Hybrid</td><td>Asynchronous weak-commitment</td><td>AWC+AP Multi-AWC</td><td></td></tr><tr><td>Consistency algorithm</td><td>Distributed consistency algorithm</td><td></td><td></td></tr></table>

NegoGA to assess the performance of the distributed coordination mechanism within different order demand environments. The proposed distributed coordination mechanism is evaluated by comparing its performance with two benchmark mechanisms: a centralized optimization mechanism, which gathers all distributed information of a supply chain to obtain optimal solutions, and a DCSP solving method, called asynchronous weakcommitment search (AWC) [16]. The experimental results show that the distributed coordination mechanism can effectively enhance the supply chain performance in raising fulfillment rate, reducing cost of inventories and shortening order fulfillment cycle time.

This paper is organized in the following sequence. Section 2 reviews up-to-date approaches to solving DCSP. Section 3 details how the proposed distributed coordination mechanism and NegoGA plan order fulfillment schedules. Section 4 designs experiments to evaluate the proposed NegoGA method, and compares its performance with those of other methods. The experimental results are analyzed and explained in Section 5. Finally, Section 6 concludes this study with implications from findings and suggests future research directions.

## 2. Review of methods for solving DCSP

A DCSP (distributed constraint satisfaction problem) is a constraint satisfaction problem with distributed variables and constraints. In a DCSP, no agents can control or are aware of the domains of all variables. Consistent values of variables for a feasible solution can only be obtained through agents' message exchanges and distributed problem solving methods. Yokoo [24] proposed a communication protocol for agents' message exchanges. Problem solving methods for DCSP have been developed in the past decade, which can be classified according to two dimensions [24]: the basic algorithm it applies and the type of problem it deals with as listed in Table 1.

In this study, the supply chain problem in fulfilling orders is treated as a DCSP. The policy to solve a DCSP, using AWC integrated with GA, optimally plans the order fulfillment schedule. In AWC, an agent is allowed to concurrently and asynchronously exchange messages $( e . g .$ , variables and values) with its relevant agents and to check the consistency of variables and values with its own view. There are two types of messages, $o k ?$ and nogood, exchanged among agents. $o k ?$ is used to communicate the current value of a variable and nogood is used to communicate a new constraint. All agents are ordered by a dynamically adjustable priority. The priority is changed based on the min-conflict heuristic. A higher priority agent can tentatively deliver the feasible value of its own variable to its neighboring lower priority agents by sending ?ok message. A lower priority agent, once receiving ?ok message, will record received variable values in its agent\_view which is a local memory to store its up-to-date perspective of outside world, adjust its own variable value, and check whether consistent values exist with its agent\_view. If consistency exists, the lower priority agent will act as a high priority agent, and send ?ok messages to its lower priority neighboring agents. Otherwise, the lower priority agent will send a nogood message back to its linked higher priority agent. A higher priority agent updates its agent\_view and tries to issue some other values again after it receives nogood message. If the partially satisfied solution cannot be further improved, AWC will restart the search process. AWC is guaranteed to be complete, namely, if there is a solution for the DCSP, AWC will find it [24].

The main characteristics of AWC search algorithm are listed as follows:

(1) A non-negative integer value, also called priority value, which represents the priority order of the variable/agent, is dynamically changed. The larger the priority value, the higher the agent's priority. The priority value, as well as the variable values, is communicated through $o k ?$ message.

(2) If an agent receives the $o k ?$ message and the variable assignment of the higher priority agent does not consist with its agent\_view, the agent changes its variable values to not only make values consistent with its agent\_view but also minimize the number of constraint violations with lower priority agents.

(3) If no other possible values exist with the agent\_view, the agent will send a nogood message to the higher priority agent, and meanwhile, its priority value will be changed to max+1, where max is the largest priority value of the involved agents.

## 3. Distributed coordination mechanism

This section proposes a distributed coordination mechanism to find optimal solution for a DCSP and demonstrates how the mechanism helps firms in a supply chain plan order fulfillment schedules once they receive customer orders.

In a real world supply chain environment, a company is likely to have more than one alternative supplier. Besides, firms are likely to simultaneously concern about more than one issue, e.g., duration (to complete a supply chain activity), manufacturing quality and production cost, when they negotiate the schedule of fulfilling orders between each other. The proposed distributed coordination mechanism supports one-to-many multi-attribute negotiation, for agents having more than one alternative supplier agents to take multiple issues into consideration, during the negotiation process in order to approximate to the practical operation of a supply chain. With the distributed coordination mechanism, an agent starts multiple parallel negotiations with prospect supplier agents, and chooses the best acceptable commitment from the negotiation results when contracting out is needed. Agents conduct negotiations by exchanging their proposals/counter proposals on their order fulfillment schedules.

To elaborate the proposed distributed coordination mechanism, this section first formulates the supply chain scheduling problem into a distributed constraint satisfaction model in Section 3.1. Afterwards, Section 3.2 proposes a multi-attribute utility function for companies to evaluate their received proposals/counter proposals, and then Section 3.3 introduces a search approach NegoGA, which integrates a negotiation technique with genetic algorithm. Section 3.4 explains how the distributed coordination mechanism supports oneto-many multi-attribute negotiation.

## 3.1. Distributed constraint satisfaction mode

In supply chain, an incoming order is accomplished by distributed companies which work out an optimal fulfillment schedule and then perform tasks accordingly to fulfill the order. It is a distributed scheduling problem to work out an optimal order fulfillment schedule. In this study, the distributed scheduling problem is modeled as a distributed constraint satisfaction problem.

This study builds a multi-agent system to simulate a DCSP for a supply chain. Each agent serves as a company involved in the supply chain. In the DCSP, each agent controls their own variables, including the duration, quality and cost. Constraints of the DCSP are formed by combining distributed agents' variables. Agents' tasks are described by the TÆMS modeling language [15]. TÆMS, standing for Task Analysis, Environmental Modeling and Simulation, is a modeling language designed for describing the task structure of agents. The TÆMS task modeling framework is a hierarchical task representation language that describes alternative ways of accomplishing tasks and the interrelationships between tasks.

Fig. 1 shows an example of agent's TÆMS task structure, which is an example of mold manufacturing. In this task structure, A (mold manufacturing) is a task group, B (parts machining) is a task and A1 (mold design), A2 (surface treatment), A3 (assembly and testing), B1 (wire cutting), B2 (EDM), B3 (milling), C (heat treatment), and D (finishing), are subtasks. In Fig. 1, A1, A2 and A3 are local tasks (in-house activities) of task A, while B1, B2, and B3 are local tasks (in-house activities) of task B. Task B is a non-local task to task A, while tasks C and D are non-local tasks to task B. Namely, task B is the outsourcing activity of task A, and tasks C and D are the outsourcing activities of task B. Subtasks B1, C, B2, B3 and D are performed sequentially to accomplish task B. Similarly, subtasks A1, B, A2 and A3 are performed sequentially to accomplish task A. The list q/c/d below a subtask (or task) in Fig. 1 describes the potential outcome of the quality, cost, and duration respectively after the subtask (or task) is completed. Quality q is a unit-less abstract property that represents the expected quality after the subtask is executed. Cost c is also a unit-less property that defines the amount of tangible or intangible resource that will be consumed after the subtask is completed. The seq\_sum in Fig. 1 denotes that the quality of a task is calculated as the sum of its subtasks' qualities. For example, Fig. 1 shows $q _ { \mathrm { B } } { = } q _ { \mathrm { B } 1 } { + } q _ { \mathrm { C } } { + } q _ { \mathrm { B } 2 } { + } q _ { \mathrm { B } 3 } { + } q _ { \mathrm { D } }$ and $q _ { \mathrm { A } } { = } q _ { \mathrm { A } 1 } { + } q _ { \mathrm { B } } { + } q _ { \mathrm { A } 2 } { + } q _ { \mathrm { A } 3 }$ . The cost of a super task is also the sum of its subtasks' costs; for example, Fig. 1 shows $c _ { \mathrm { B } } = c _ { \mathrm { B } 1 } + c _ { \mathrm { C } } + c _ { \mathrm { B } 2 } + c _ { \mathrm { B } 3 } + c _ { \mathrm { D } }$ and $c _ { \mathrm { A } } { = } c _ { \mathrm { A 1 } } { + } c _ { \mathrm { B } } { + } c _ { \mathrm { A } 2 } { + } c _ { \mathrm { A } 3 }$

![](/api/attachments/X72FQ6H2/fulltext/images/756ceb8db8e327e3ec7ac0addd96c38317e7fd8926fb63ea96ba7532cddf8565.jpg)  
Fig. 1. An example of TÆMS task structure.

Duration d is the time spent to complete a subtask (or task). A task's time schedule $t s ( b , f )$ is scheduled by its beginning time b, finishing time f, and $f = b + d .$ The interdependencies of the beginning and finishing times among subtasks and tasks in Fig. 1 can be described as $f _ { \mathrm { B } 1 } \leq b _ { \mathrm { C } } , f _ { \mathrm { C } } \leq b _ { \mathrm { B } 2 } , f _ { \mathrm { B } 2 } \leq b _ { \mathrm { B } 3 } , f _ { \mathrm { B } 3 } \leq b _ { \mathrm { D } } , b _ { \mathrm { B } } = b _ { \mathrm { B } 1 } , f _ { \mathrm { B } } = f _ { \mathrm { D } } ,$ $f _ { \mathrm { A l } } \leq b _ { \mathrm { B } } , f _ { \mathrm { B } } \leq b _ { \mathrm { A } 2 } , f _ { \mathrm { A } 2 } \leq b _ { \mathrm { A } 3 } , b _ { \mathrm { A } } { = } b _ { \mathrm { A l } } , { \mathrm { a n d } } f _ { \mathrm { A } } { = } f _ { \mathrm { A } 3 }$

Fig. 2 demonstrates an example of mapping the task structure in Fig. 1 into a four echelon distributed supply chain structure. In Fig. 2, each box with a symbol inside represents a company in the supply chain. a1, a2 and a3 are alternative mold manufacturers to the customer. b1, b2, b3 and b4 are alternative parts machining suppliers to the mold manufacturers. $c I , c 2 , c 3$ and c4 are alternative heat treatment suppliers, while d1, d2, d3 and d4 alternative finishing suppliers to the parts machining suppliers.

In a distributed supply chain environment, a company takes charge of its own local task structure which is a portion of the global task structure. For example, in Fig. 1, agent's local task structure of company a1 contains tasks A1, B, A2 and A3; likewise, agent's local task structure of company b1 contains subtasks B1, C, B2, B3 and D. Based on the predefined task structure and supply chain structure, once a customer order arrives, related companies in the supply chain will negotiate to generate an optimal schedule to satisfy the requirements of the order.

## 3.2. Multi-attribute utility function

In this study, quality, cost, and duration time are three criteria used for agents to measure the utility of a feasible schedule. This study uses a multi-attribute utility function [27] for agents to evaluate and make comparison among received proposals/counter proposals during the negotiation process. The multi-attribute utility function is formulated in Eqs. (1)–(5) as follows.

$$
u _ {x} (s) = q g _ {x} (s) ^ {*} q w _ {x} + c g _ {x} (s) ^ {*} c w _ {x} + t g _ {x} (s) ^ {*} t w _ {x}\tag{1}
$$

$$
q w _ {x} + c w _ {x} + t w _ {x} = 1\tag{2}
$$

$$
q g _ {x} (s) = q (s) / q _ {\mathrm{th}}\tag{3}
$$

$$
c g _ {x} (s) = \left(c _ {1} - c (s)\right) / c _ {1}\tag{4}
$$

$$
t g _ {x} (s) = \left(d _ {1} - d (s)\right) / d _ {1}\tag{5}
$$

In the aforementioned equations, $u _ { x } ( s )$ is the multiattribute utility function for agent x. qg (s), cg (s), and $t g _ { x } ( s )$ denote the gains from time, cost, and quality, respectively. $q ( s ) , c ( s )$ and $d ( s )$ are the achieved quality, spent cost and duration time of schedule s. $d _ { \mathrm { l } }$ and $c _ { 1 }$ are the duration and cost limits which agent x wants to spend on a subtask. $q _ { \mathrm { t h } }$ is the quality threshold. $q _ { \mathrm { t h } }$ specifies the quality objective which agent x wants to achieve from the subtask. $t w _ { x } , \ c w _ { x } ,$ and $q w _ { x }$ are the relative importance of time, cost and quality attributes, respectively. The sum of relative importance is equal to 1.

![](/api/attachments/X72FQ6H2/fulltext/images/047ea4e0951f727901e947b08243cb608ebaf98a400c48efb91ea4246cb9ea0f.jpg)  
Fig. 2. An example of mapping the task structure in Fig. 1 into a distributed supply chain structure.

## 3.3. NegoGA

To search for an optimal solution for the distributed constraint satisfaction problem in a supply chain, this study proposes NegoGA as the problem solving technique for supply chain partners to cooperatively generate an optimal order fulfillment schedule. NegoGA integrates such negotiation techniques as AWC search algorithm, multi-agent technologies and constraint synchronization strategy, with genetic algorithm. Negotiation techniques are applied, for each company, to coordinating with each other and learning the supply chain environment. Genetic algorithm is applied, for each company, to generating optimal proposal/counter proposal subject to known constraints.

A negotiation is a process of mutual concessions. A negotiation is successful when the concessions are in a balanced state. To accelerate a successful negotiation, this study defines two rules to motivate companies to show their benevolence in concessions during their negotiation process. The first rule is that the larger the concession is offered by a company, the larger power the company gains in the next negotiation round. An agent, representing a certain company, with larger power owns higher priority in delivering its optimal proposal to its counterpart agent and the counterpart agent is likely to accept the proposal. In this study, the relative power represents the priority value in AWC search algorithm. Such priority value is somewhat like a bargaining power that is the relative power of a company to ask other companies to change their plans to fulfill an arrived customer order. This rule guides companies in a supply chain, especially a fragmented supply chain, to resolve their conflicts to obtain a workable order fulfillment schedule. The fragmented supply chain is the one in which most companies are small and medium sized, maintain only short term relations, and no single company dominates the market. Companies in the fragmented supply chain must cooperate with others to fulfill customers' orders.

Based on the first rule, a company's bargaining power is subject to change in the negotiation process.

The change process is called the bargaining power shift. Formally, this study defines the bargaining power shift for companies x and y, from company $x ' s$ standpoint, as follows:

$$
\begin{array}{l} b p x ^ {n + 1} = (c s x q ^ {n} / (c s x q ^ {n} + c s y q ^ {n})) ^ {*} w _ {q} \\ \quad + (c s x c ^ {n} / (c s x c ^ {n} + c s y c ^ {n})) ^ {*} w _ {c} \\ \quad + (c s x d ^ {n} / (c s x d ^ {n} + c s y d ^ {n})) ^ {*} w _ {d} \end{array}\tag{6}
$$

$$
\begin{array}{l} b p y ^ {n + 1} = (c s y q ^ {n} / (c s x q ^ {n} + c s y q ^ {n})) ^ {*} w _ {q} \\ \quad + (c s y c ^ {n} / (c s x c ^ {n} + c s y c ^ {n})) ^ {*} w _ {c} \\ \quad + (c s y d ^ {n} / (c s x d ^ {n} + c s y d ^ {n})) ^ {*} w _ {d} \end{array}\tag{7}
$$

$$
w _ {d} + w _ {q} + w _ {c} = 1\tag{8}
$$

In Eqs. (6) and $( 7 ) , \ b p x ^ { n + 1 }$ and $b p y ^ { n + 1 }$ are two bargaining powers of agents x and y respectively in the $( n + 1 ) ^ { \mathrm { t h } }$ negotiation round. $c s x d ^ { n }$ and $c s y d ^ { n }$ are the proportion of the duration concession offered by agents $x$ and y respectively between the $n ^ { t h }$ and $( n ^ { - } 1 ) ^ { t h }$ negotiation round. Similarly, $c s x q ^ { n }$ , csyq<sup>n</sup>, csxc<sup>n</sup>, and $c s y c ^ { n }$ denote quality and cost concession offered by agents x and y respectively between the $n ^ { t h }$ and $\left( n - 1 \right) ^ { \hat { t h } }$ negotiation round. $w _ { d } , \ w _ { q } ,$ and $w _ { c }$ indicate the relative importance of duration, quality, and cost attributes for agent x. The sum of $w _ { d } , w _ { q } ,$ and $w _ { c }$ should be 1.

If two agents' bargaining powers are equal, $e . g .$ $b p x ^ { n + 1 } { = } b p y ^ { n + 1 }$ , agents' priority values will be assigned by the 2nd rule that an agent for a downstream company, $e . g .$ , a customer, is prioritized higher than that for an upstream company, $e . g .$ , a supplier, since the downstream company places orders to the upstream company. Applying these rules, the AWC search algorithm enables distributed agents to coordinate with each other and updates their agent views.

Fig. 3 shows the process of NegoGA that is followed by agents when they are negotiating with each other in a negotiation round. In a negotiation round, an agent with a higher priority can send its proposal to its counterpart, whereas an agent with a lower priority can just wait for its counterpart's proposal. The lower priority agent, once receiving proposal, will update its agent view and assess the proposed order fulfillment schedule. If an agent with a lower priority accepts the proposal, it will turn the proposal into a mutually acceptable task fulfillment schedule, and terminates the negotiation process. Otherwise, the agent with a lower priority will use GA to generate a counter proposal and send it back to the agent with a higher priority.

The agent with a higher priority will check whether the counter proposal is acceptable once receiving the counter proposal. If the counter proposal is accepted, a mutually acceptable task fulfillment schedule is formed, and the negotiation succeeds. Otherwise, both of the agents' priority values will be re-estimated for the next negotiation round. In the next round, agents continue the negotiation by following the aforementioned process. The unacceptable proposals and counter proposals, which have been communicated in the preceding negotiation rounds, will be memorized in individual agent\_views to avoid being repeatedly proposed in the succeeding negotiation rounds.

![](/api/attachments/X72FQ6H2/fulltext/images/43ad3c5e2c345818901eb6f59bdb3b6957180c51ab5b0486659c803bcb655cc0.jpg)  
Fig. 3. Process of NegoGA in a negotiation round.

During a negotiation round as shown in Fig. 3, every proposal proposed by an agent to its counterpart is an optimal schedule for one subtask subject to the capacity constraint of the upstream agent and the sequence constraint of the predetermined agent's task structure. In the process of generating a subtask schedule, as shown in Fig. 3, GA is applied to generate optimal schedule.

In NegoGA, a subtask schedule can be encoded into a chromosome as shown in Figs. 4 and 5. Fig. 4 shows the chromosome of an upstream agent's subtask schedule, and Fig. 5 shows that of a downstream agent's. In Fig. 4, a chromosome is composed of two sub-chromosomes. The first sub-chromosome denotes the policy adopted to fulfill a subtask, and the second sub-chromosome denotes the beginning time to start the schedule. In the first sub-chromosome, the policy is a manufacturing method provided by the upstream company. Each policy maps to a quality level an agent will achieve, a cost value that it may spend, and the duration time that it may consume to finish the subtask based on the company's expertise and past experiences. The duration time in the first sub-chromosome, the order quantity of the subtask, and the beginning time in the second sub-chromosome will determine the time schedule of the subtask. In Fig. 5, a chromosome is composed of three subchromosomes which respectively represent the features of a subtask schedule: quality, cost, and time schedule. The chromosome describes the features of a proposal/ counter proposal.

In the initial negotiation round during a negotiation process, a subtask's initial schedule is generated by a higher priority agent. The agent plans the schedule by

![](/api/attachments/X72FQ6H2/fulltext/images/2277e4d95b8ef534444b3af2d1e2f7d2fa548fe93b81baa050c5acd3ec0f047c.jpg)  
Fig. 4. An example of encoded subtask schedule (upstream supplier).

considering the characteristics of the subtask and the agent's view, past experiences and current state. The initial planned schedule will be encoded into a seed chromosome for generating the initial population of NegoGA. After the initial round, in the following negotiation rounds for upstream and downstream agents, not only the proposal but also the counter proposal will be encoded as the initial population of NegoGA. The proposal/counter proposal from an upstream agent may not exactly match any of the downstream agent's policies. Under such circumstance, a downstream agent will first find a policy which resembles the received proposal/counter proposal most, and then encode the found policy as an initial chromosome. The proposal and counter proposal contribute to influence the searching direction to generate the optimal schedule in the negotiation process [18].

![](/api/attachments/X72FQ6H2/fulltext/images/1a1335f38473f4805e90ef68acea98b1aca36ab8dd2c6989866bdb5d0cfb751c.jpg)  
Fig. 5. An example of encoded subtask schedule (downstream customer).

A chromosome corresponding to a task schedule, as shown in Figs. 4 or 5, is assessed by fitness function to show how good the task schedule is. In this study, the utility function u(s) in Eq. (1) serves as a fitness function for NegoGA. Chromosomes with higher utility values will survive in the next generation to produce new population through genetic operators.

Genetic operators in Fig. 3 include reproduction, crossover, and mutation. The reproduction operation sorts the population by fitness, selects a percentage of the top ranked chromosomes from the sorted population, and reproduces the selected chromosomes into crossover pool for the crossover operation. The crossover operation pairwisely chooses chromosomes from the crossover pool to make single-point crossover at a random point to generate new chromosomes. In the crossover pool, the higher the fitness value of a reproduced chromosome is, the higher probability that the chromosome is chosen. The mutation operation is performed on every chromosome generated by the crossover operation. NegoGA adopts one-point mutation method to first randomly decide whether to mutate the chromosome and then if mutation is permitted, the chromosome will be mutated at a random gene. The decision to or not to mutate a chromosome is made by generating a random value between 0 and 1. The mutation operation is performed if the random value is larger than a preset mutation probability. Otherwise, the mutation is not permitted. The mutation is to change the value of the random gene from 0 to 1 or 1 to 0.

A chromosome will further be examined after mutation to check whether it is a valid chromosome. A valid chromosome must meet the following three conditions: (1) A valid chromosome satisfies all the schedule constraints; (2) A valid chromosome is unique in the new population; and (3) A valid chromosome is not a memorized unacceptable proposal/counter proposal in an agent's view. A valid chromosome, after the examination, will be put into the new population whereas an invalid chromosome will be disposed.

For a new generation, the crossover and mutation operators will be performed iteratively until the number of new chromosomes equals the preset population size or the computation time exceeds a preset time period. These GA operations, which evolve generation by generation to get optimal task schedule, will be terminated once the number of its evolutional generations outnumbers the preset number. Once these GA operations are terminated, the best chromosome, with the highest utility value in the population, will be picked up and decoded into a new proposal/counter proposal.

Agents in the distributed coordination mechanism interact with each other by using the negotiation performatives. The negotiation performatives are the communicative acts which are embedded in agents communication messages to express agents' intentions when they are negotiating with each other. There are five types of performatives used in the distributed coordination mechanism, including Call for Proposal, Propose, Accept Proposal, Reject Proposal, and Cancel. The Call for Proposal is used when a customer agent delivers an order to its upstream company and desires that the receiver agent makes a proposal. The Propose is used when an agent sends a proposal or a counter proposal. The Accept Proposal is used when an agent accepts the received proposal. The Reject Proposal is used when an agent is not satisfied with the received proposal. The Cancel is used to terminate a negotiation once an agent wants to cancel the negotiation. These five performatives comply with the FIPA ACL (Agent Communication Language) specification [6].

An initialized negotiation continues until the termination condition is met. The termination condition is met when a proposal/counter proposal from an agent is accepted by another agent; that is, an agreement between agents is reached, either agent cancels the negotiation, or the negotiation exceeds a preset time limit. A proposal/counter proposal will be accepted by an agent if the utility value of the received proposal/ counter proposal is higher than the agent's currently planned schedule.

A negotiation succeeds if agents reach an agreement on task schedule; otherwise, the negotiation fails. Fig. 6(a) shows an example of successful multi-attribute negotiation between agents x and y. In Fig. 6(a), the circled areas $\mathrm { S } _ { x }$ and $\mathrm { S } _ { y }$ are the feasible solution regions for agents x and y, respectively. Agents x and $y$ don't know each other's feasible solution regions. The points inside the feasible regions are the candidate task schedules. Among the candidate task schedules, $s _ { x } ^ { * }$ is the optimal planned task schedule of agent $x ,$ and $s _ { y } ^ { * }$ is that of agent y. The points, in the feasible regions marked with $^ \times ,$ are the unacceptable proposals/counter proposals. In the negotiation process, agents x and $y$ uses

![](/api/attachments/X72FQ6H2/fulltext/images/c0169ed49f520b07b32efdca077e204f31238d02e339a0f670d294cd965b1091.jpg)  
Fig. 6. Examples of multi-attribute one-to-one negotiations.

NegoGA to generate new proposals/counter proposals based on the received proposals/counter proposals to negotiate with each other. Through several negotiation rounds, a mutually acceptable task schedule $s _ { x y } ^ { * }$ for agents x and y is generated. Fig. 6(b) shows an example of failed negotiation in which no agreement is reached.

## 3.4. One-to-many negotiation

The proposed distributed coordination mechanism supports one-to-many negotiation by decomposing it into many one-to-one sub-negotiations [19]. In this mechanism, an agent is able to negotiate with more than one opponent by creating a number of sub-negotiating agents to conduct sub-negotiations simultaneously and respectively. An agent as a coordination agent creates sub-negotiating agents and initializes sub-negotiations. Sub-negotiating agents negotiate with their opponent agents. A sub-negotiation continues until it meets the termination condition. Therefore, a one-to-many negotiation will be terminated when all sub-negotiations are completed or canceled, or when the one-to-many negotiation is conducted beyond a preset time limit. Once a one-to-many negotiation is terminated, the coordination agent will evaluate all the available negotiation results, and then choose the best one. Fig. 7 shows an example of the one-to-many negotiation which is a partial portion of the supply chain example shown in Fig. 2. In Fig. 7, $a _ { a I }$ is the coordinating agent of company a1. $a _ { a I I } , \ a _ { a I 2 } , \ a _ { a I 3 }$ and $a _ { a l 4 }$ are the subnegotiating agents created by $a _ { a l } . \ : a _ { b l } , a _ { b 2 } , a _ { b 3 }$ and $a _ { b 4 } ,$ the representative agents of companies b1, b2, b3 and b4 separately, are the opponent agents of $a _ { a I }$

## 4. Experiments

This study cites a mold manufacturing supply chain as an example and utilizes JADE (http://jade.tilab.com/) as a multi-agent platform to build a supply chain setting. The supply chain is composed of sixteen companies as shown in Fig. 2. Fig. 1 shows TÆMS task structure of sixteen companies. To assess the performance of the proposed distributed coordination mechanism of this study, we make comparisons among three mechanisms: (1) DCSM – the distributed coordination satisfaction mechanism with AWC, (2) NegoGA – the distributed coordination mechanism with NegoGA, and (3) COM – the centralized optimization mechanism. COM, which centralizes all information and controls all variables of a supply chain, has a global view of the supply chain to find the best solution. The performance of COM and DCSM are adopted as benchmarks to investigate NegoGA's performance.

In this section, the experimental settings are described first in Section 4.1, and then the customer order, characterizing the business environment, is modeled in Section 4.2. Section 4.3 demonstrates an example of how NegoGA works. Section 4.4 designs two sets of experiments, and metrics to measure the three aforementioned coordination mechanisms.

## 4.1. Experimental settings

In the experimental environment, it is supposed that the involved sixteen companies, as shown in Fig. 2, maintain a highly trusted relationship. Moreover, information technologies enable multiple agents to generate optimal fulfillment schedules for an incoming

![](/api/attachments/X72FQ6H2/fulltext/images/341f9db8fde527f04130daae81e06238bc9a8fbbf9907718e07bd6ccebcf17af.jpg)  
Fig. 7. An example of one-to-many negotiation.

![](/api/attachments/X72FQ6H2/fulltext/images/40410b19c6effc5d10b43075ff60b4e9a485d7957a21dce12fd5906b39a24cce.jpg)  
Fig. 8. Task structure for experiments.

customer order before the next order arrives. Each agent adopts the First-Come-First-Serve (FCFS) policy to plan the task schedules which can be successfully fulfilled. The experiment time unit is set to be one day and the daily capacity of every company is 1. Moreover, in order to observe the effects of controlled variables on the experimental results, it is supposed that the task structures of mold manufacturing in all experiments are identical, as shown in Fig. 8, during the experimental period. Fig. 8 symbolizes the task structure of Fig. 1. In Fig. 8, the values q/c/d, denoted under each task (or subtask) and shown in the table, are the quality threshold $q _ { \mathrm { t h } } ,$ cost limit $d _ { \mathrm { l } }$ and time limit $c _ { 1 }$ of the corresponding task (or subtask). Table 2 shows the relative importance, tw, cw and qw, of a company's multi-attribute utility function.

Relative importance of every company's utility function

<table><tr><td rowspan="2">Company</td><td colspan="3">Relative importance of u(s)</td></tr><tr><td>qw</td><td>cw</td><td>tw</td></tr><tr><td>Customer</td><td>0.3</td><td>0.2</td><td>0.5</td></tr><tr><td>a1</td><td>0.2</td><td>0.3</td><td>0.5</td></tr><tr><td>a2</td><td>0.3</td><td>0.3</td><td>0.4</td></tr><tr><td>a3</td><td>0.3</td><td>0.2</td><td>0.5</td></tr><tr><td>b1</td><td>0.4</td><td>0.1</td><td>0.5</td></tr><tr><td>b2</td><td>0.5</td><td>0.2</td><td>0.3</td></tr><tr><td>b3</td><td>0.4</td><td>0.3</td><td>0.3</td></tr><tr><td>b4</td><td>0.6</td><td>0.1</td><td>0.3</td></tr><tr><td>c1</td><td>0.5</td><td>0.3</td><td>0.2</td></tr><tr><td>c2</td><td>0.3</td><td>0.3</td><td>0.4</td></tr><tr><td>c3</td><td>0.2</td><td>0.3</td><td>0.5</td></tr><tr><td>c4</td><td>0.4</td><td>0.3</td><td>0.3</td></tr><tr><td>d1</td><td>0.2</td><td>0.3</td><td>0.5</td></tr><tr><td>d2</td><td>0.4</td><td>0.3</td><td>0.3</td></tr><tr><td>d3</td><td>0.6</td><td>0.1</td><td>0.3</td></tr><tr><td>d4</td><td>0.5</td><td>0.2</td><td>0.3</td></tr></table>

Taguchi method is effectively useful in NegoGA to obtain the optimal value combination of GA parameters, such as population size, crossover rate, mutation probability, and the reproduction percentage [9]. Based on Taguchi method, pilot experiments, designed with an orthogonal array L9 (four three-level factors), are performed and analyzed, and then the optimal value combination of GA parameters is obtained as listed in Table 3.

The relative importance $w _ { d } ,$ $w _ { q } ,$ and $w _ { c }$ to evaluate companies' relative bargaining powers in every negotiation round are set to 1/3, 1/3 and 1/3, respectively. Table 4 lists parameter values for NegoGA's termination conditions.

## 4.2. Customer order generation

The customer order in this study is modeled by two parameters: inter-order arrival time and order quantity. The customer order model determines the times and quantities of customer orders. The inter-order time, which determines the time span between consecutive arrivals of customer orders, is assumed to be an exponential distribution with rate λ, where 1/λ is the mean inter-order time. The order quantity is a normal distribution $N ( \mu , \sigma ^ { 2 } )$ , where $\mu$ is the mean quantity per order and $\sigma ^ { 2 }$ is the variance of order quantity.

Optimal value combination of NegoGA parameter

<table><tr><td>NegoGA parameter</td><td>Value</td></tr><tr><td>Population size</td><td>40</td></tr><tr><td>Crossover probability</td><td>0.95</td></tr><tr><td>Mutation probability</td><td>0.01</td></tr><tr><td>Reproduction percentage</td><td>50%</td></tr></table>

Table 4  
Parameter settings for NegoGA's termination conditions

<table><tr><td>Parameter of termination condition</td><td>Value</td></tr><tr><td>Number of generations in a negotiation round</td><td>30</td></tr><tr><td>Time limit for generating a new population</td><td>30 s</td></tr><tr><td>Time limit for a sub-negotiation</td><td>3 h</td></tr></table>

## 4.3. Demonstration of generating optimal subtask schedule in a sub-negotiation

This section demonstrates an example to explain how companies coordinate with each other to generate optimal subtask schedule. In this demonstration, two companies, b1 and c1, employ the distributed coordination mechanism to negotiate with each other in a distributed supply chain environment described in Section 4.1. Companies b1 and c1 negotiate with each other on quality, cost and finishing time to fulfill arrived orders. Company b1's acceptable quality, cost and duration are within the following ranges, $q \in [ 1 . 0 , 2 . 0 ] .$ $c \in [ 1 . 0 , 2 . 0 ] , d \in [ 1 . 0 , 2 . 0 ]$ . For b1, the subtask C's quality threshold $q _ { \mathrm { t h } } ,$ cost limit $c _ { 1 }$ and duration limit $d _ { \mathrm { l } }$ are all set to 2.0. For c1, $q _ { \mathrm { t h } } , c _ { \mathrm { l } } ,$ , and $d _ { \mathrm { l } }$ are all set to 2.0. c1's available policies, to carry out subtask C, are shown in Table 5.

This example begins with an order delivered from b1 to c1. The order quantity is 3 and it is constrained to be fulfilled after the 30th day. Around that time, c1's capacity is available. In b1's and c1's proposal or counter proposal, the cost and duration for the order must be tripled because of the order quantity. The details of the first two negotiation rounds are demonstrated in Table 6. b1's and c1's priorities in NegoGA are initially determined by the 2nd rule described in Section 3. According to the 2nd rule, b1 owns higher priority than c1. Therefore, in the first round, b1 searches for the optimal attribute values q = 2.0, c = 1.0 and $d { = } 1 . 0$ for the order and delivers its optimal proposal to c1. c1, after receiving the proposal, picks up the #5 policy from Table 5 which resembles the received proposal most. Because #5 policy is not $c 1 ^ { \prime } \mathbf { s }$ optimal policy, c1 sends its counter proposal, which is developed based on #1 policy, to b1. b1, after receiving the counter proposal, makes an assessment on the counter proposal by substituting it into b1's utility function. For the reason that the counter proposal (utility value = 0.519) is not better than its delivered proposal (utility value = 0.700), b1 does not accept the counter proposal. b1 then sends a Reject message to c1. The first round ends up with no agreement, and then the second round begins.

Since no concession is made in the first round, in the second round, b1 is still prioritized higher than c1. During the second round, b1 and c1 follow the NegoGA process as described in Section 3 to generate their proposal/counter proposals, and they assess their received proposal/counter proposal as in the first round. The second round fails again as shown in Table 6, and then the next negotiation round starts.

## 4.4. Experimental designs and performance metrics

Two experiments, A and B are designed in this study. Experiment A, containing four sub-experiments, A-1, A-2, A-3, and A-4, aims at investigating the respective performances of DCSM, NegoGA and COM within different customer order environments. Moreover, comparisons are made between NegoGA and DCSM, and COM and NegoGA. Experiment B aims at comparing the efficiency between DCSM and NegoGA when they are applied to resolve conflicts. In each experiment, 30 customer orders are generated and delivered to the supply chain during the experimental period.

In Experiment A, four different customer order patterns, as shown in Table 7, are set into the four sub-experiments. $\mathrm { A } { - } 1 \mathrm { \bar { s } }$ customer order is characterized as a long inter-order time and low order variance pattern; A-2 as short inter-order arrival time and low order variance; A-3 as short inter-order time and high order variance pattern; and A-4 as long inter-order time and high order variance. The pattern in A-1 is regarded as a stable customer demand environment and the pattern in A-3 is an unstable environment.

The performances of the three mechanisms, DCSM, NegoGA and COM, in Experiment A, are measured by four metrics: (1) order fulfillment rate $R _ { \mathrm { O F } } ,$ which is the ratio of the number of fulfilled orders to the number of total orders; (2) average order fulfillment cycle time $T _ { \mathrm { O F } } ,$ which is the average of fulfillment cycle times of all fulfilled orders; (3) average inventory cost of work-inprocess (WIP) C , which is the average of WIP inventory cost of all fulfilled orders; and (4) average inventory cost of finished products $C _ { \mathrm { F P } }$ which is the average of final product inventory cost of all fulfilled orders.

Table 5  
Company c1's available policies for subtask C

<table><tr><td></td><td>q</td><td>c/per unit</td><td>d/per unit</td></tr><tr><td>1</td><td>1.1</td><td>1.1</td><td>1.0</td></tr><tr><td>2</td><td>1.2</td><td>1.2</td><td>1.0</td></tr><tr><td>3</td><td>1.3</td><td>1.3</td><td>1.1</td></tr><tr><td>4</td><td>1.5</td><td>1.5</td><td>1.2</td></tr><tr><td>5</td><td>1.6</td><td>1.6</td><td>1.1</td></tr><tr><td>6</td><td>1.7</td><td>1.7</td><td>1.2</td></tr><tr><td>7</td><td>1.9</td><td>1.9</td><td>1.5</td></tr><tr><td>8</td><td>2.0</td><td>2.0</td><td>2.0</td></tr></table>

Table 6  
A demonstration of the first two negotiation rounds between b1 and c1

<table><tr><td></td><td></td><td></td><td>b1</td><td>c1</td></tr><tr><td rowspan="8"> $1^{st}$  negotiation round</td><td></td><td>Priority</td><td colspan="2">Priority $_{b1}$ &gt;priority $_{c1}$ </td></tr><tr><td>1</td><td>Attribute value &amp; utility value</td><td>q=2.0, c=1.0, d=1.0utility=0.700</td><td rowspan="2"></td></tr><tr><td>2</td><td>Optimal schedule /proposal</td><td>quality=2.0, cost=3.0,duration=3.0Time schedule=from 31 to 33</td></tr><tr><td>3</td><td>Policy resembles the received Proposal most</td><td rowspan="3"></td><td>no.5q=1.6, c=1.6, d=1.1utility=0.447</td></tr><tr><td>4</td><td>Optimal policy</td><td>no.1q=1.1, c=1.1, d=1.0utility=0.494</td></tr><tr><td>5</td><td>Counter proposal</td><td>quality=1.1, cost=3.3,duration=3.0Time schedule=from 31 to 33</td></tr><tr><td>6</td><td>Utility value of received counter proposal</td><td>quality=1.1, cost=3.3,duration=3.0Time schedule=from 31 to 33utility=0.519</td><td></td></tr><tr><td>7</td><td>Succeed?</td><td colspan="2">No</td></tr><tr><td rowspan="8"> $2^{nd}$  negotiation round</td><td></td><td>Priority</td><td colspan="2">Priority $_{b1}$ &gt;priority $_{c1}$ </td></tr><tr><td>8</td><td>Attribute value &amp; utility value</td><td>q=1.8, c=1.6, d=1.0utility=0.630</td><td rowspan="2"></td></tr><tr><td>9</td><td>Optimal schedule /proposal</td><td>quality=1.8, cost=4.8,duration=3.0Time schedule=from 31 to 33</td></tr><tr><td>10</td><td>Policy resembles the received proposal most</td><td rowspan="3"></td><td>no.6q=1.7, c=1.7, d=1.2utility=0.417</td></tr><tr><td>11</td><td>Optimal policy</td><td>No.2q=1.2, c=1.2, d=1.0utility=0.490</td></tr><tr><td>12</td><td>Counter proposal</td><td>quality=1.2, cost=3.6,duration=3.0Time schedule=from 31 to 33</td></tr><tr><td>13</td><td>Utility value of received counter proposal</td><td>quality=1.2, cost=3.6,duration=3.0Time schedule=from 31 to 33utility=0.550</td><td></td></tr><tr><td>14</td><td>Succeed?</td><td colspan="2">no</td></tr></table>

Experiment B makes a comparison between DCSM and NegoGA in an unstable customer demand environment which is the same as in Sub-experiment A-3. The metrics for Experiment B are: (1) average negotiation round NR; and (2) average computing time $T _ { \mathrm { { C } } } .$ The average negotiation round is the average of the cumulative negotiation rounds of all the successfully scheduled customer orders. The average computing time is the average of the total computing time of all the successfully scheduled customer orders. The computing time is defined as the time span from receiving an order to planning its schedule successfully. In this study, every experiment ran 5 times, and then the results from three different mechanisms were compared accordingly.

## 5. Experimental results and discussions

## 5.1. Experiment A

Table 8 shows the results from Experiment A. In Experiment A, NegoGA's performance is compared with DCSM's and COM's within different customer demand environments. In Table 8, the alternative hypotheses are tested by t test which yields the following results:

Table 7  
Experiment A

<table><tr><td>Sub-experiment</td><td>Customer order pattern</td><td>Inter-order time 1/λ (day)</td><td>Order quantity variance  $\sigma^{2}$ </td></tr><tr><td>A-1</td><td>Long inter-order time and low order quantity variance</td><td>10</td><td> $1^{2}$ </td></tr><tr><td>A-2</td><td>Short inter-order time and low order quantity variance</td><td>5</td><td> $1^{2}$ </td></tr><tr><td>A-3</td><td>Short inter-order time and high order quantity variance</td><td>5</td><td> $3^{2}$ </td></tr><tr><td>A-4</td><td>Long inter-order time and high order quantity variance</td><td>10</td><td> $3^{2}$ </td></tr></table>

In Sub-experiment A-1, NegoGA outperforms DCSM in $T _ { \mathrm { O F } }$ at highly significant level and COM outperforms NegoGA in $T _ { \mathrm { O F } }$ at significant level. Besides, in a stable demand environment, NegoGA does not significantly surpass DCSM in $R _ { \mathrm { O F } } , C _ { \mathrm { W I P } }$ and $C _ { \mathrm { F P } } . \mathrm { C O M }$ does not significantly excel NegoGA in $R _ { \mathrm { O F } } ,$ $C _ { \mathrm { W I P } }$ and $C _ { \mathrm { F P } } .$ The results from Sub-experiment A-1 reveal that NegoGA is applicable to the stable demand environment, and performs well in $R _ { \mathrm { O F } } , C _ { \mathrm { W I P } }$ and $C _ { \mathrm { F P } }$

In Sub-experiment A-2, NegoGA significantly outperforms DCSM in $T _ { \mathrm { O F } }$ and $C _ { \mathrm { W I P } } .$ NegoGA does not significantly surpass DCSM in $R _ { \mathrm { O F } }$ and $C _ { \mathrm { F P } } .$ Moreover, COM does not significantly surpass NegoGA in any of the four metrics; namely, NegoGA works well to plan task fulfillment schedules for supply chains under $\mathrm { A } { - } 2 \mathit { \Omega } ^ { \prime } \mathrm { s }$ settings. Comparing A-1 with A-2, we will find that NegoGA not only shortens the average order fulfillment time but also reduces the average WIP inventory cost under the condition that the inter-order arrival time is short and the variation of order quantity is slight. NegoGA is applicable to the demand environment as that of A-2.

In Sub-experiment A-3, NegoGA outperforms DCSM in the four metrics, $R _ { \mathrm { O F } } ,$ T<sub>OF</sub>, $C _ { \mathrm { W I P } }$ and $C _ { \mathrm { F P } } .$ COM does not significantly surpass NegoGA in any metrics. If comparisons are made between A-2 and $\mathrm { A } { - } 3 ,$ we will find that NegoGA improves the supply chain performance more in the environment of high variation of order quantity than in that of low variation when the inter-order time is short. NegoGA is applicable to the demand environment as that of A-3 which is highly dynamic. Since the pattern in A-3 is characterized as a dynamic and unstable demand environment, NegoGA is able to handle the complexity of supply chain scheduling problem and the dynamics of customer orders.

Table 8  
Experiment A results

<table><tr><td rowspan="2">Metric</td><td rowspan="2">Hypothesis</td><td colspan="4">p-value</td></tr><tr><td>A-1</td><td>A-2</td><td>A-3</td><td>A-4</td></tr><tr><td rowspan="4"> $R_{OF}$ </td><td> $R_{OF, NegoGA}>$ </td><td>0.175</td><td>0.153</td><td>0.031*</td><td>0.172</td></tr><tr><td> $R_{OF, DCSM}$ </td><td></td><td></td><td></td><td></td></tr><tr><td> $R_{OF, COM}>$ </td><td>0.172</td><td>0.363</td><td>0.286</td><td>0.095</td></tr><tr><td> $R_{OF, NegoGA}$ </td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="3"> $T_{OF}$ </td><td> $T_{OF, NegoGA}>$ </td><td>0.001**</td><td>0.036*</td><td>0.001**</td><td>0.019*</td></tr><tr><td> $T_{OF, DCSM}$ </td><td></td><td></td><td></td><td></td></tr><tr><td> $T_{OF, COM}>T_{OF, NegoGA}$ </td><td>0.032*</td><td>0.442</td><td>0.239</td><td>0.033*</td></tr><tr><td rowspan="4"> $C_{WIP}$ </td><td> $C_{WIP, NegoGA}>$ </td><td>0.218</td><td>0.030*</td><td>0.004*</td><td>0.000**</td></tr><tr><td> $C_{WIP, DCSM}$ </td><td></td><td></td><td></td><td></td></tr><tr><td> $C_{WIP, COM}>$ </td><td>0.477</td><td>0.277</td><td>0.101</td><td>0.429</td></tr><tr><td> $C_{WIP, NegoGA}$ </td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="3"> $C_{FP}$ </td><td> $C_{FP, NegoGA}>$ </td><td>0.136</td><td>0.053</td><td>0.009**</td><td>0.037*</td></tr><tr><td> $C_{FP, DCSM}$ </td><td></td><td></td><td></td><td></td></tr><tr><td> $C_{FP, COM}>C_{FP, NegoGA}$ </td><td>0.278</td><td>0.226</td><td>0.295</td><td>0.331</td></tr></table>

Significance leve $\alpha { = } 0 . 0 5 ^ { * } , 0 . 0 1 ^ { * * } .$  
Note. $R _ { \mathrm { O F } }$ denotes order fulfillment rate; $T _ { \mathrm { O F } }$ denotes average order fulfillment cycle time; $C _ { \mathrm { W I P } }$ denotes average inventory cost of workin-process (WIP); C denotes average inventory cost of finished products.

In Sub-experiment A-4, NegoGA outperforms DCSM in $C _ { \mathrm { W I P } }$ at highly significant level, and in $T _ { \mathrm { O F } }$ and $C _ { \mathrm { F P } }$ at significant level. COM significantly outperforms NegoGA only in $T _ { \mathrm { O F } } .$ Moreover, if A-4 is compared with A-1, the comparison shows that NegoGA significantly reduces the inventory costs of WIP and finished products, especially the WIP, when the customer demand varies more dynamically.

Comparing the experimental results of DCSM and NegoGA, we found that NegoGA significantly improves supply chain performance both in stable or dynamic environments. In a dynamic environment, NegoGA can raise the demand fulfillment rate, reduce the average demand fulfillment cycle time, average WIP inventory cost and average finished product inventory cost. NegoGA outperforms DCSM since DCSM just focuses on finding a globally executable order fulfillment schedule, and NegoGA tends to approximately find a global optimal solution.

Table 9  
Experiment B results

<table><tr><td>Metric</td><td>Hypothesis</td><td>p-value</td></tr><tr><td>NR</td><td> $\text{NR}_{\text{NegoGA}} > \text{NR}_{\text{DCSM}}$ </td><td> $7.82 \times 10^{-5}$ **</td></tr><tr><td> $C_{\text{T}}$  (s)</td><td> $C_{\text{T, NegoGA}} > C_{\text{T,DCSM}}$ </td><td> $1.52 \times 10^{-6}$ **</td></tr></table>

Significance level $\alpha { = } 0 . 0 1 ^ { * * } .$  
Note. NR denotes the number of negotiation rounds; $C _ { \mathrm { T } } \ ( \mathrm { s } )$ denotes average computing time.

The comparison between NegoGA and COM reveals that if inter-order arrival time of customer demand is long, COM outperforms NegoGA in $T _ { \mathrm { O F } } .$ The COM maintains a global view of the entire supply chain by frequently gathering up-to-date information from all supply chain partners. Based on the global view, COM is able to obtain the best schedule, but it is costly to do so and besides, supply chain partners are likely unwilling to expose their private information to others. The centralized mechanism therefore may be infeasible in real world supply chain. NegoGA, by contrast, is a practical problem solving technique to the distributed scheduling problem in a supply chain management.

## 5.2. Experiment B

The results of Experiment B are shown in Table 9. Table 9 reveals that NegoGA significantly requires more NR and $T _ { \mathrm { C } }$ than DCSM does. That is, NegoGA helps the supply chain partners enhance their performance at expense of spending more time to coordinate with each other, and using more computing resources to search for optimal subtask schedules. However, since the aforementioned costs are relatively lower than the reduced cost in inventory costs of WIP and final product, NegoGA is applicable in the distributed supply chain.

## 6. Conclusions and future work

This study proposes a distributed coordination mechanism to facilitate firms in a supply chain to plan order fulfillment schedules. The distributed coordination mechanism, developed based on multi-agent technologies, integrates negotiation techniques with genetic algorithm. The multi-agent techniques enable companies to communicate with each other through the Internet so as to increase information sharing and to coordinate with each other. The negotiation techniques enable companies in a supply chain to make a series of decisions to reach mutually acceptable order fulfillment schedules, and the GA leads to reach approximate optimality.

In order to evaluate the proposed distributed coordination mechanism, this study introduces three models, DCSM, NegoGA and COM, and makes comparisons among them by conducting two experiments. The first experiment shows that NegoGA significantly improves supply chain performance both in the stable and unstable demand environments. COM outperforms NegoGA in the average demand fulfillment cycle time at significant level only if the customer's inter-order time is long. NegoGA is more applicable and practical than COM since the centralized optimization mechanism may be infeasible in real world supply chains.

The second experiment shows that NegoGA sacrifices efficiency for effectiveness. Although NegoGA significantly improves the supply chain performance, it needs more negotiation rounds and computing time than DCSM does.

The distributed coordination mechanism can be further enhanced in the following directions. First, bring trust mechanisms into the distributed coordination mechanism to help supply chain companies select trustily potential partners. The enhanced coordination mechanism can make the order fulfillment schedule not only optimal but also reliable. Second, improve the efficiency of NegoGA. Third, extend the proposed mechanism to be usable for dynamic task structures and more complicated supply chain structures, and be broadly applicable to supply chains of different industries. Finally, embed other intelligent scheduling rules into the distributed coordination mechanism to enable NegoGA to flexibly and agilely handle complicated scheduling problems that arises in a distributed supply chain environment.

## Acknowledgement

This research was supported by the MOE Program for Promoting Academic Excellence of Universities under the grant number 91-H-FA08-1-4.

## References

[1] Y. Aviv, The effect of collaborative forecasting on supply chain performance, Management Science 47 (10) (2001) 1326–1343.

[2] P. Byrne, C. Heavey, The impact of information sharing and forecasting in capacitated industrial supply chains: a case study, International Journal of Production Economics 103 (2006) 420–437.

[3] G. Cachon, M. Fisher, Supply chain inventory management and the value of shared information, Management Science 46 (8) (2000) 1032–1048.

[4] M. CARIDI, S. Cavalieri, Multi-agent systems in production planning and control: an overview, Production Planning & Control 15 (2) (2004) 106–118.

[5] F. Chen, Z. Drezner, J. Ryan, D. Simchi-Levi, Quantifying the bullwhip effect in a simple supply chain: the impact of forecasting, lead times, and information, Management Science 46 (3) (2000) 436–443.

[6] FIPA Agent Communication Language Specification, Foundation for intelligent physical agents, http://www.fipa.org/specs/fipa00037/ SC00037J.html.

[7] M.S. Fox, M. Barbuceanu, R. Teigen, Agent-oriented supply-chain management, International Journal of Flexible Manufacturing Systems 12 (2000) 165–188.

[8] Z. Guo, F. Fang, A.B. Whinston, Supply chain information sharing in a macro prediction market, Decision Support Systems 42 (3) (2006) 1944–1958.

[9] C.-H. Hsieh, J.-H. Chou, Y.-J. Wu, Optimal grey-fuzzy gainscheduler design using Taguchi-HGA method, Journal of Intelligent and Robotic Systems 32 (3) (2001) 321–345.

[10] H.L. Lee, K.C. So, C.S. Tang, The value of information sharing in a two-level supply chain, Management Science 46 (5) (2000) 626–643.

[11] Y. Li, G.W. Tan, Information sharing in a supply chain with dynamic consumer demand pattern, Proceedings of the 37th Annual Hawaii International Conference on System Sciences (HICSS), Big Island, Hawaii, United States, 2004.

[12] F.-r. Lin, S.-m. Lin, P.-w. Hsueh, Dynamic business process formation by integrating simulated and physical agent systems, 37th Annual Hawaii International Conference on System Sciences, Hawaii, 2004.

[13] F.-r. Lin, Y.-y. Lin, Integrating multi-agent negotiation to resolve constraints in fulfilling supply chain orders, The Eighth Pacific-Asia Conference on Information Systems, Shanghai, China, 2004.

[14] S. Matwin, T. Szapiro, K. Haigh, Genetic algorithms approach to a negotiation support system, IEEE Transactions on Systems, Man and Cybernetics 21 (1) (1991) 102–114.

[15] Multi-agent System Lab, http://mas.cs.umass.edu/research/taems.

[16] I.-S. Oh, J.-S. Lee, B.-R. Moon, Hybrid genetic algorithms for feature selection, IEEE Transactions on Pattern Analysis and Machine Intelligence 26 (11) (2004) 1424–1437.

[17] M. Papazoglou, Agent oriented technology in support of e-business: enabling the development of intelligent business agents for adaptive, reusable software, Communications of the ACM 44 (4) (2001) 71–77.

[18] L. Ping, H. Yongtong, Y. Yuhong, Z. Danian, Y. Shiyuan, Using counter-proposal to optimize genetic algorithm based cooperative negotiation, Proc. of the 1997 IEEE International Conference on Intelligent Processing Systems, 1997, pp. 891–895.

[19] I. Rahwan, R. Kowalczyk, H. Pham, Intelligent agents for automated one-to-many e-commerce negotiation, Proc. of the 25th Australasian Computer Science Conference (ACSC-02), 2002, pp. 197–204.

[20] N.M. Sadeh, D.W. Hildum, D. Kjenstad, A. Tseng, MASCOT: an agent-based architecture for dynamic supply chain creation and coordination in the internet economy, Production Planning & Control 12 (3) (2001) 212–223.

[21] J.M. Swaminathan, S.F. Smith, N.M. Sadeh, Modeling supply chain dynamics: a multiagent approach, Decision Sciences 29 (3) (1998) 607–632.

[22] A. White, E.M. Daniel, M. Mohdzain, The role of emergent information technologies and systems in enabling supply chain agility, International Journal of Information Management 25 (5) (2005) 396–410.

[23] M. Wooldridge, N.R. Jennings, Agent theories, architectures, and languages: a survey. In intelligent agents – agent theories, architectures, and languages, ATAL 94 (890) (1994) 1–32.

[24] M. Yokoo, Distributed Constraint Satisfaction: Foundations of Cooperation in Multi-agent Systems, Springer-Verlag, Berlin, 2001.

[25] M. Yokoo, E.H. Durfee, T. Ishida, K. Kuwabara, Distributed constraint satisfaction for formalizing distributed problem solving, Proc. 12th IEEE Int'l Conf. Distributed Computing Systems, 1992, pp. 614–621.

[26] M. Yokoo, K. Hirayama, Algorithms for distributed constraint satisfaction: a review, Autonomous Agents and Multi-Agent Systems 3 (2) (2000) 198–212.

[27] X. Zhang, V. Lesser, R. Podorozhny, Multi-dimensional, multistep negotiation for task allocation in a cooperative system, Journal of Autonomous Agents and Multi-Agent Systems 10 (1) (2005) 5–40.

Dr. Fu-ren Lin received the Ph.D. degree in information systems from University of Illinois at Urbana-Champaign in 1996. He currently is a professor and chairman at the Graduate Institute of Technology Management of National Tsing Hua University (NTHU), Taiwan. Prior to joining NTHU in 2004, Professor Lin taught at the Department of Information Management, National Sun Yat-sen University since 1996, and was a Fulbright visiting scholar to his alma mater in 2002– 2003. His research interests include electronic commerce, e-business management, data/text mining, and knowledge management. He has published academic papers in many journals, such as International Journal of Electronic Commerce, Electronic Commerce Research and Applications, Decision Support Systems, IEEE Transactions on Engineering Management, IEEE Intelligent Systems, Journal of Organizational Computing and Electronic Commerce, and Information Processing and Management. He has served as a guest editor for journals, such as Information Systems and e-Business Management, and International Journal of Electronic Commerce Research and Applications.

Ms. Hui-chun Kuo received her master degree from the Department, of Information Management, National Sun Yat-sen University, Taiwan, 2003. Her research interests are in multi-agent systems and business process innovation.

Dr. Shyh-ming Lin received his Ph.D. degree from the Department of Information Management, National Sun Yat-sen University, Taiwan, 2007. He is now an assistant professor at the Department of Information Management, Meiho Institute of Technology. His research interests are in multi-agent systems, dynamic business process formation and mobile services.
