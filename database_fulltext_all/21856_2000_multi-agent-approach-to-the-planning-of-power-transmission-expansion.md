---
otero_id: 21856
otero_key: "HX6P8Q4Z"
title: "Multi-agent approach to the planning of power transmission expansion"
authors: "Jerome Yen; Yonghe Yan; Javier Contreras; Pai-Chun Ma; Felix F. Wu"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00092-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Multi-agent approach to the planning of power transmission expansion

Jerome Yen <sup>a,)</sup>, Yonghe Yan <sup>b</sup>, Javier Contreras <sup>c</sup>, Pai-Chun Ma <sup>d</sup>, Felix F. Wu <sup>e</sup>

<sup>a</sup> Department of Systems Engineering and Engineering Management, Chinese UniÕersity of Hong Kong, Hong Kong SAR, People’s Republic of China

<sup>b</sup> Department of Computer Science and Information Systems, The UniÕersity of Hong Kong, Hong Kong SAR, People’s Republic of China <sup>c</sup> Escuela Tecnica Superior de Ingenieros Industriales, UniÕersidad de Castilla — La Mancha, Campus UniÕersitario s<sup>r</sup>n, 13071 Ciudad Real, Spain

<sup>d</sup> Department of Computer Information Systems, Zicklin School of Business, Baruch College, City UniÕersity of New York, New York, NY, USA

<sup>e</sup> Department of Electrical and Electronic Engineering, UniÕersity of Hong Kong, Hong Kong SAR, People’s Republic of China

## Abstract

Deregulation and restructuring have become unavoidable trends to the power industry recently in order to increase its efficiency, to reduce operation costs, or to provide customers better services. The once centralized system planning and management must be remodeled to reflect the changes in the market environment. We have proposed and developed a multi-agent-based system to assist players, such as owners of power generation stations, owners of transmission lines, and groups of consumers, in the same market to select partners to form coalitions. The system provides users with a cooperation plan and its associated cost allocation plan for the users to support their decision-making process. Bilateral Shapley Value Ž . BSV was selected as the theoretical foundation to develop the system. The multi-agent system was developed by the combination of IDEAS M. Klusch, Utilitarian coalition formation between autonomous agents for cooperative information<sup>w</sup> gathering, in: S. Krin, G. O’hare Eds. , Cooperative Knowledge Processing. Springer, London, 1996 and Tcl Ž .  <sup>r</sup>Tk. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Software agent; Intelligent agent; Bilateral Shapley Value; Cooperative game theory

## 1. Introduction

Since the late 1980s, electric utility industry has been facing the pressure of deregulation and restructuring. Two of the major changes were that the owners of the transmission lines could participate in the market to make decision on behalf of themselves and that the old boundary lines have been removed to offer consumers more alternatives, for example, consumers were allowed to purchase electricity from the power stations located in other states.

As deregulation and restructuring have become inevitable trends in the modern utility industries, there is a need for more efficient methods or systems to facilitate a just and stable searching for new partners for formation of coalition as well as aŽ . fair system to identify the contribution from each participant for profits or costs allocation . Fortunately,Ž . there are many game theory models that we can borrow to develop the theoretical foundation for the multi-agent system.

Deregulation and restructuring have been adopted in several states, for example, California, and countries, for example, Australia. Market structure of such states or countries have been changed significantly. In most cases, a more decentralized system or negotiation infrastructure has replaced the original system. Since this issue was very important, Wu and Varaiya 22 have developed a decentralized algo- <sup>w</sup> <sup>x</sup> rithm to optimize multilateral trading among the participants. For transmission planning, Bushnell and Stoft 3 , and Chao and Peck 4 have shown that <sup>w x</sup> <sup>w x</sup> investment incentives and market mechanisms have been important to guarantee a fair and just outcome.

Planning for expansion in power industry, either adding new power stations or new transmission lines, is a very significant decision. The costs involved, in the first case, can reach several billion US dollars. In this paper, we assume that there are a fixed number of power generation units and consumer groups. However, after deregulation or restructuring, the original boundary lines have been removed. Therefore, the consumers, owners of power stations, and owners of transmission lines have to work together to search for new coalitions to guarantee that their long-term interests can be protected.

Adding new power units costs more and takes longer, therefore, the core of the planning problem is modified or limited to the determination of the optimal number of lines to add to the existing system.

Planning for transmission expansion involves the decisions from the players, based on some scenarios, which include the network topology, suppliers, customers, and<sup>r</sup>or owners of transmission line. It is common that when adding a new transmission line, costs should be shared by all the players who will be benefited. The decision about whether to add one more line or not, and how to allocate costs is still an open research area.

This problem is very similar to the logistics planning problem in which the number and locations of manufacturing plants, warehouses, and retail stores are fixed. Therefore, to design the new logistics system, which include decision of the routing of transportation and number of trucks, has become the core of the problem. In other words, to satisfy the demands of the new set of consumers with the lowest costs to both owners of the transmission lines and owners of power units is the goal of solving such problem. To solve such problems, the solutions also need to guarantee that the other operational constraints, such as capacity of power transmission, can be satisfied 15 .<sup>w</sup> <sup>x</sup>

Several techniques have been used to assist the planning of transmission expansion. For example, techniques based on mathematical programming, such as Branch-and-Bound 5,7,13 , techniques that<sup>w</sup> <sup>x</sup> based on sensitivity analysis 2,16 , and techniques <sup>w</sup> <sup>x</sup> that uses hybrids of neural networks and genetic algorithms 23 . Normally, the planning for expan-<sup>w</sup> <sup>x</sup> sion is combinatorial complicated and that makes it very difficult to find reasonable solutions within short computational time if the number of nodes or number of participants is large.

Using game theory to assist in the formation of coalitions is one of approaches to solve such problems. Gately 8 used Shapley Value to set up re- <sup>w</sup> <sup>x</sup> gional cooperation for investment in expansion and cost allocation. Gately’s approach is a centralized one, where a central planner is needed to be in charge of cost allocation.

Recently, researchers in Distributed Artificial Intelligence DAI have started to study how coalitionsŽ . were formed and what negotiation or bargaining algorithms were useful in helping people to better understand the process of coalition formation and design better negotiation strategy. Again, cooperative game theories have been proved to be useful. However, a lot of work is still required to build systems which can support the negotiation or formation of coalition in fully decentralized environments 10– 12,18 . DAI approaches address and solves some<sup>x</sup> pending issues in deregulated power transmission markets. For example,

<sup>Ø</sup> Determining the members of coalitions and which coalition will be formed,

<sup>Ø</sup> Implementing a protocol to support bargaining and negotiation,

<sup>Ø</sup> Allocating total expansion costs to all the players Ž . agents of the expansion game.

In this paper, we propose and have developed a multi-agent system to prove that some of the above issues can be solved by such multi-agent approach. The multi-agent system simulates the power industry and models each player, such as, an owner of a power station, an agent. In the system, agents communicate with each other, based on Bilateral Shapley Value BSV to search for potential partners to formŽ . coalitions where they can protect their long-term interests.

The agents of this system have to work collaboratively to finish certain tasks, for example, determining the new transmission lines to add to the system and forming coalitions to reduce the overall costs. Each agent is assumed to be rational, that is, maximizing its own utility, and to be an independent and autonomous agent, who is not willing to accept any plan generated by a centralized planner 10 . <sup>w</sup> <sup>x</sup>

In Section 2, we will briefly introduce the software agents and multi-agent systems. The network expansion model, which governs the network expansion of electricity transmission will be discussed in Section 3. Coalitions in network expansion planning will be discussed in Section 4. The process of decentralized coalition formation among agents will be discussed in Section 5. Implementation of the multiagent system will be discussed in Section 6. This paper is concluded with a discussion about the limitations of the multi-agent approaches and recommendation for future research.

## 2. Software agent and multi-agent system

The advances in Internet technologies, growing complexity and decentralization of the utility markets, the increasing pressure to lower costs, and the demand for better and more stable services from the customers have pushed the development of new tools and systems to support the decision-making in the utility markets. One of such applications is the software agent. If software agents do have additional capabilities, such as perception, learning and communication, they can be called intelligent agents. Detailed discussion about software agents can be seen, for example, in Refs. 14,21 .<sup>w</sup> <sup>x</sup>

Multi-agent systems are special type of agents, which focus on the coordination and the communication among agents to collaboratively accomplish tasks <sup>w</sup> <sup>x</sup> 10–12 . The agents in our system are owners of power stations, groups of customers and coordinators, such as independent system operators ISOs .Ž . The coordinator is a special type of agent who coordinates and synchronizes the collaboration among agents. The objective of the multi-agent system is, therefore, to derive a workable and profitable coalition under the fair play practice subject to the constraints and requirements of power generation and transmission.

Communication and cooperation are two most important capabilities of multi-agent systems. Multiagent systems are designed to have the capability to either, collaborate, for example, to decompose a problem and jointly solve the problem, or compete, such as, search for the best deal for the users. The term cooperation used in this paper is assumed to include both collaboration and competition. Communication is vitally important by which relevant information to support cooperation is exchanged. KQML Ž . Knowledge Query and Manipulation Language is a language that supports the communication among agents 6 . However, agents must do more than just <sup>w</sup> <sup>x</sup> communication. Rational agents must be able to cooperate and negotiate with each other. Design of the communication and negotiation protocols is important. However, so far there is no protocol that dominates this field. One language developed by Barbuceanu and Fox 1 is called COOL, which is an<sup>w</sup> <sup>x</sup> extension of KQML, which allows agents to be developed with the capability to make proposals and counter-proposals, accept and reject goals, notify the other agents of goal cancellation or creation.

## 3. Network expansion model

We used a simple example, a six-bus system, to illustrate the planning process of network expansion as shown in Fig. 1. The limits of power transmission and power generation are provided on the same figure. The details of the model and example can be found in Refs. 7,20 .<sup>w</sup> <sup>x</sup>

There are several techniques that can be used to rank the possible locations to add new lines to an existing system. For this study, we followed the heuristic approach suggested by Refs. 15,20 , which <sup>w</sup> <sup>x</sup> is a quadratic linear programming problem, to identify whether a solution is feasible or not. The general formulation can be expressed as:

$$
\min \frac {1}{2} \sum_ {j = 1} ^ {M} c _ {j} P _ {j} ^ {2}\tag{1}
$$

subject to

$$
\mathbf {B} \boldsymbol {\Theta} + \mathbf {K} ^ {\mathrm{T}} \boldsymbol {P} _ {\mathrm{D}} = \boldsymbol {P}\tag{2}
$$

$$
\left| \mathbf {B} _ {\mathrm{L}} \mathbf {A} \boldsymbol {\Theta} \right| \leq \overline {{\boldsymbol {P}}} _ {\mathrm{L}}\tag{3}
$$

where $c _ { j }$ is the cost of adding line j to the network, $P _ { J }$ is the active power in p.u. flowing through theŽ . added line j, i.e., the jth element of $P _ { \mathrm { { D } } }$ , and $P _ { \mathrm { { D } } }$ is the flow vector for the possible lines. Also, M is the number of possible new lines, B is the matrix, whose elements are the imaginary parts of the nodal admittance matrix of the existing network,  is the phase angle vector, $\mathbf { K } ^ { \mathrm { T } }$ is the transpose of the node–branch connection matrix, P is the nodal injection power for the overall network, $\mathbf { B } _ { \mathrm { L } }$ is a diagonal matrix whose elements are branch admittance, $\overline { { P } } _ { \mathrm { L } }$ is the branch active power vector, and A is the network incidence matrix.

Data for the Garver’s six-bus problem are presented in Fig. 1 and Table 1. The solid lines and dotted lines in Fig. 1 represent the exiting lines and candidate lines, respectively. The minimization algorithm is run recursively until there are no overloads, $P _ { j }$ , in the system. Although the optimum value is not always guaranteed, the simplicity of the heuristic algorithm makes it a valid first approach to solve a highly combinatorial complicated problem like this one.

![](/api/attachments/HX6P8Q4Z/fulltext/images/f66d443cc984bebce3ce89bb661be79edcc98b88b9340dce43b415d5ebe0f671.jpg)  
Fig. 1. Six-bus problem.

Table 1  
Six-bus problem

<table><tr><td>Bus (from/to)</td><td>Cost (units)</td><td>Susceptance (1/Ω)</td><td>Capacity (MW)</td></tr><tr><td>1/2</td><td>40</td><td>2.50</td><td>100</td></tr><tr><td>1/4</td><td>60</td><td>1.67</td><td>80</td></tr><tr><td>1/5</td><td>20</td><td>5.00</td><td>100</td></tr><tr><td>2/3</td><td>20</td><td>5.00</td><td>100</td></tr><tr><td>2/4</td><td>40</td><td>2.50</td><td>100</td></tr><tr><td>2/6</td><td>30</td><td>3.33</td><td>100</td></tr><tr><td>3/5</td><td>20</td><td>5.00</td><td>100</td></tr><tr><td>4/6</td><td>30</td><td>3.33</td><td>100</td></tr><tr><td>5/6</td><td>61</td><td>1.64</td><td>78</td></tr></table>

Since the objective function 1 has taken intoŽ . account the effect of the power transmission cost, the candidate line with the largest power flow is the most effective in the expanded network.<sup>1</sup> Constraint Ž . 2 expresses the total nodal injection power as a function of the existing and the potential network Ž . after adding new lines parameters, and constraint Ž . 3 reflects the thermal limits of the existing network lines.

## 4. Coalitions in expansion planning

To solve the transmission expansion planning problem in a decentralized environment, we treat it as a cooperative game. The purpose of the game is to expand the transmission grid with the minimum possible costs, subject to constraints 2 and 3 , as wellŽ . Ž . as with a ‘‘fair’’ allocation of total costs among the players based on their contributions.

By DAI terminology, a player is called an agent. An agent in the game can be either a generator aŽ power station , a load a group of consumers , or an . Ž . independent third party for example, an ISO . A Ž . typical agent in this research is considered to be an independent entity: a customer load or a set of customer loads, a generator or a set of generators, or a combination of both. For simplicity, we do not consider fractional bus loading or fractional generator output. We also assume that any set of generation units and loads attached to the same bus belong to a single agent. Therefore, we cannot have two agents sharing the same bus. Therefore, we have a maximum of six agents in the expansion game corresponding to the six-bus example as shown in Fig. 1.

A coalition in this paper is defined to be a set of agents and their associated transmission line s whichŽ . connect these agents. They must satisfy the four conditions:

1. There must be at least one generator, one load, and one transmission line included in the agents.

2. Generators have to meet the total demand, i.e., the loads have to be always satisfied by the outputs from generation stations plus the losses due to transmission.

3. Existing line s thermal limits cannot be ex- Ž . ceeded.

4. There must be one or more transmission lines Ž . either existing or possible candidates which connect all the agents.

A self-contained single agent can also be regarded as a coalition, called a trivial coalition. Such trivial coalition need not meet all the four conditions.

Once a coalition is formed, then it will be represented by one autonomous agent. Within each coalition, it can develop its own expansion plan and the expansion plan of this coalition can be determined again by the minimum algorithm described by Eqs. Ž . Ž . 1 – 3 . Fig. 2 shows two examples of feasible coalitions in the Garver test case.

When we allow generation rescheduling, that is, the real power generation output can be ranged form 0 to the maximum capacity 150, 360, and 600 MW,Ž respectively in Fig. 1 , the optimal solution of the . minimum algorithm for the grand coalition has a cost of 130 units, and circuit additions are $n _ { 2 6 } = 3$ circuits, and $n _ { 3 5 } = 2$ circuits.

We will use the bus notation when referring to coalitions. For example, when we say coalition 1,2 4 we are referring to a coalition that combines all generators and loads on buses 1 and 2, and all the lines that interconnect these buses.

![](/api/attachments/HX6P8Q4Z/fulltext/images/f131a99bd0f378d95bf15307e7258c1a1fd17dcdb0d7024db861b3952781e229.jpg)

![](/api/attachments/HX6P8Q4Z/fulltext/images/1fe0cea0f072e3c9a66c64270eec43d14c20e724e5792340a75fc72e28b39637.jpg)  
Coalition of agents 2, 4, and 6  
Fig. 2. Two examples of coalitions.

## 5. Decentralized coalition formation between transmission expansion agents

The use of decision techniques to analyze DAI problems, like the one discussed in Section 3, started in the early 1990s. However, the Shapley Value has been widely used in solving such problems 17 .<sup>w</sup> <sup>x</sup> Shapley Value calculates a fair division of the utility, based on individuals’ contributions, among the members in a coalition. It is a solution concept for an n-person cooperative game. Shapley Value can be considered as a weighted average of marginal contributions of a member to all the possible coalitions in which it may participate. It assumes that the game is super-additive and the grand coalition is possible to be formed. Readers are referred to Refs. 9,17 for a<sup>w</sup> <sup>x</sup> more detailed explanation about how calculate Shapley Value. The mathematical expression of the Shapley Value, is given by:

$$
\begin{array}{l} \phi_ {i} = \sum_ {S, i \in S \subset N} \frac {(| S | - 1) ! (n - | S |) !}{n !} \\ \times [ v (S) - v (S - \{i \}) ] \end{array}\tag{4}
$$

where, i is a player, S is a coalition of players, <sup><</sup> <sup><</sup> S is the number of players in coalition S, n is the total number of players, N is the set of all players, and $v ( S )$ is the characteristic function associated with coalition S.

Ketchpel 10 introduced the BSV. Klusch and<sup>w</sup> <sup>x</sup> Shehory 11,12 adapted this approach for a com- <sup>w</sup> <sup>x</sup> pletely decentralized and bilateral negotiation process among rational agents. In particular, the algorithm for coalition formation they provided is also useful in power transmission planning 12 .

Let $S \subseteq P ( A )$ be a coalition structure on a given set of agents $A = \{ a _ { 1 } , \ldots , a _ { m } \}$ , where

$$
C = C _ {i} \cup C _ {j} \subseteq A, \text {   and   } C _ {i} \cap C _ {j} = \phi .
$$

Therefore, C is a bilateral coalition of disjointŽ . Ž .n-agent coalitions of $C _ { i }$ and $C _ { j } \left( n \geq 0 \right)$ . The BSV for coalition $C _ { i }$ in the bilateral coalition C is defined by:

$$
\varphi_ {C} (C _ {i}) = \frac {1}{2} v (C _ {i}) + \frac {1}{2} (v (C) - v (C _ {j}))\tag{5}
$$

Both coalition $C _ { i } , ~ C _ { j }$ are called founders of $C ,$ Ž .and Õ C denotes the self-value of coalition $C . ^ { 2 }$ Both coalition $C _ { i } , C _ { j }$ are willing to form coalition C, if

$$
v \left(C _ {i}\right) \leq \varphi_ {C} \left(C _ {i}\right) \text {   and   } v \left(C _ {j}\right) \leq \varphi_ {C} \left(C _ {j}\right)\tag{6}
$$

In fact, a super-additive cooperative game is played between $C _ { i }$ and $C _ { j }$ Eq. 6 reflects the Ž . individual rationality and Eq. 5 implies the collec-Ž . tive rationality.

It can be seen that the founders will get half of their local contributions, and the other half obtained from cooperative work with the other entity. The second term of the BSV expression, as in Eq. 5 ,Ž . reflects the strength of each agent based on its contribution. Therefore, it can remove the ‘‘freerider’’<sup>3</sup> problem, which is common in value allocation in transmission expansion.

In summary, the process of coalition formation among agents is based on the approach of Klusch and Shehory in Ref. 12 . The process has the follow- <sup>w</sup> <sup>x</sup> ing four steps.

## 5.1. Step 1: Self-Õalue calculation

Each bus is represented by one agent. Each individual agent collects and analyzes information to determine its initial self-value. Calculation of the self-value determines the costs of line expansion. The self-value of an individual agent should be the minimum cost for the agent to achieve its goal. If the agent is not willing to join a coalition, such as agents 1 and 3 in Fig. 1, the self-value is set to zero. If the agent must form a coalition to achieve its goal, such as agents 2, 4, 5, and 6, the self-value of agent $a _ { i }$ can be chosen as:

$$
v \big (\{a _ {i} \} \big) = \max _ {j} v \big (\{a _ {i}, a _ {j} \} \big).\tag{7}
$$

For simplicity, we assume that an individual agent can be included in some two-entity coalitions. Eq. Ž . 7 reflects what initially agent $a _ { i }$ will pay for all the construction costs of the coalition $\{ a _ { i } , a _ { j } \}$ to encourage the formation of a coalition. There are other values for an agent to choose as its self-value. However, the lower boundary of the self-value for agent $a _ { i }$ is:

$$
\min _ {a _ {i} \in S} v (S)\tag{8}
$$

If the value of Eq. 8 is set as its self-value,Ž . every coalition $S - \{ a _ { i } \} , S \subset A$ is willing to form coalition S with $a _ { i }$ . No matter what self-value is chosen, the algorithm cannot guarantee that an agent with non-zero self-value will be included in a coalition.

## 5.2. Step 2: Communication and security check

Each agent sends its self-value and the candidate coalition to an independent coordinator. The coordinator will check the security of the coalition according to the security constraints. If a candidate coalition is identified to be detrimental to the security of the system, the independent coordinator informs the founders of the coalition to cancel the candidate coalition. After security check, the coordinator broadcasts the information of each coalition to all the agents.

## 5.3. Step 3: BSV calculation

After receiving messages from the coordinator, each agent proceeds to calculate BSVs to rank the order of forming coalition with other agents. Then each agent determines individually a rational list, $L ,$ of preferred agents to form coalitions, i.e., an ordered list of local agent’s BSVs for two-entity coalition.

Table 2 Coalition expansion costs

<table><tr><td>Coalition</td><td>Value</td><td>Coalition</td><td>Value</td></tr><tr><td>1</td><td>0</td><td>{2, 5, 6}</td><td>-334</td></tr><tr><td>2</td><td>-90</td><td>{3, 5, 6}</td><td>-101</td></tr><tr><td>3</td><td>0</td><td>{4, 5, 6}</td><td>-304</td></tr><tr><td>4</td><td>-60</td><td>{1, 2, 3, 6}</td><td>-30</td></tr><tr><td>5</td><td>-40</td><td>{1, 2, 4, 6}</td><td>-120</td></tr><tr><td>6</td><td>-60</td><td>{1, 2, 5, 6}</td><td>-273</td></tr><tr><td>{2, 6}</td><td>-90</td><td>{1, 4, 5, 6}</td><td>-243</td></tr><tr><td>{3, 5}</td><td>-40</td><td>{2, 3, 4, 6}</td><td>-120</td></tr><tr><td>{4, 6}</td><td>-60</td><td>{2, 3, 5, 6}</td><td>-100</td></tr><tr><td>{5, 6}</td><td>-183</td><td>{3, 4, 5, 6}</td><td>-161</td></tr><tr><td>{1, 2, 6}</td><td>-60</td><td>{1, 2, 3, 4, 6}</td><td>-90</td></tr><tr><td>{1, 3, 5}</td><td>-20</td><td>{1, 2, 3, 5, 6}</td><td>-80</td></tr><tr><td>{1, 4, 6}</td><td>-60</td><td>{1, 2, 4, 5, 6}</td><td>-272</td></tr><tr><td>{1, 5, 6}</td><td>-183</td><td>{2, 3, 4, 5, 6}</td><td>-160</td></tr><tr><td>{2, 3, 4}</td><td>-60</td><td>{1, 2, 3, 4, 5, 6}</td><td>-130</td></tr><tr><td>{2, 4, 6}</td><td>-150</td><td></td><td></td></tr></table>

## 5.4. Step 4: Bilateral negotiation

For each agent: initially, set i <sup>s</sup> 1.

1. Sends an offer to the ith agent in the agent’s preference list, i.e., L iŽ ..

2. Waits for replies and offers from other agents.

3. If an offer from the agent $L ( j ) , j \leq i$ is received, i<sup>s</sup>j. If an offer from the agent $L ( j ) , \ j > i$ or from an agent outside the preference list L has been received, replies a dissent message to that agent. If no more offer from other agents has been received, replies a consent message to agent $L ( j )$ and informs coordinator the candidate coalition with agent $L ( j )$

4. If a consent message from agent L iŽ . has been received, informs coordinator the candidate coalition with agent L iŽ .. If a dissent message from agent L iŽ . Ž . has been received and L i is not the last agent in the preference list, $i = i + 1$ and go to 2 .Ž .

For coordinator.

When the coordinator receives messages from both founders of a candidate coalition, informs every agent to stop negotiation and removes from its own preference list the agents within the candidate coalition, and then go to Step 2.

When every agent reach the end of the list L and no coalition is possible, the process terminates.

It is perfectly possible that two agents reach an agreement that is satisfactory to both of them, but which may be detrimental to the security of the system. This is the reason why an independent coordinator is needed to check and to guarantee that the reliability of the system and quality of service can be achieved. The coordinator is assigned other duties in the process. It is responsible for gathering information of the network and sending the information to all the agents. In the process, the synchronization in the multi-agent system is actually done by the coordinator.

![](/api/attachments/HX6P8Q4Z/fulltext/images/07cae422ccc78693ee190a44613892e35c8213b4e2c438d2eea928b51a3193fb.jpg)  
Fig. 3. The user agent manager of IDEAS.

![](/api/attachments/HX6P8Q4Z/fulltext/images/aecc8a8edb69ac4207b095ba7576369378d75bf7af5e25f5eee55020a43f5688.jpg)  
Fig. 4. Result of cost allocation.

The process produces a coalition structure that is a set of coalition trees in which the founders of a coalition are the sons of the coalition. The coalition structure is not unique for a given power expansion planning. If grand coalition is formed, the coalition structure will only contain a single tree.

For power expansion planning, the grand coalition will not necessarily be formed. However, the process does not guarantee that any individual agent is contained in a coalition in the coalition structure.

Cost allocation according to coalition structure is given by:

1. if SA and S is a root of a coalition tree, the cost shared by coalition S is

$$
\varphi (S) = v (S)
$$

2. if $S _ { i } , S _ { j } A$ and $S _ { i } , S _ { j }$ are the founders of coalition S, the cost shared by coalition $S _ { i }$ is

$$
\varphi (S _ {i}) = \frac {1}{2} v (S _ {i}) + \frac {1}{2} [ \varphi (S) - v (S _ {j}) ]
$$

Note that cost allocation is different from Eq. 5 andŽ . the values are also different.

For the six-bus problem, the cost function ÕŽ . S of all valid coalitions and the self-value of each individual agent is given in Table 2. The values are negative to reflect that the utility of expansion is a cost.

<table><tr><td>coordinator</td><td>Agent 1</td><td>Agent 2</td><td>Agent 3</td><td>Agent 4</td><td>Agent 5</td><td>Agent 6</td></tr><tr><td>start</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>complete</td><td></td><td></td><td>complete</td><td>require</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>require</td><td></td><td></td><td></td></tr><tr><td></td><td>complete</td><td></td><td></td><td></td><td>refuse</td><td></td></tr><tr><td></td><td></td><td>complete</td><td></td><td>require</td><td></td><td></td></tr><tr><td>start</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>complete</td><td>require</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>complete</td><td>complete</td><td>require</td><td></td><td></td><td></td><td></td></tr><tr><td>start</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>complete</td><td>require</td><td></td><td></td><td></td><td></td><td></td></tr></table>

Fig. 5. The negotiation procedure of the six-bus problem.

![](/api/attachments/HX6P8Q4Z/fulltext/images/10d59f15c33aa7f87533ae6cce47345561a98c90e8cb4f4acf445d8cd48cd13b.jpg)  
Fig. 6. The log window of agent 2.

## 6. Implementation

Integrated DeÕelopment EnÕironment for Agent Systems Ž . IDEAS 11 has been selected to imple-<sup>w</sup> <sup>x</sup> ment the multi-agent system to support coalition formation. IDEAS is implemented in Tcl Tool Com-Ž mand Language with the Tk Toolkit for the X. Windows System running on UNIX platforms. An agent in IDEAS runs as a separate process in UNIX. The internal links among the local agents are made possible via UNIX pipes while the agents establish their communication with other known agents at remote sites for cooperative works by TCP-sockets via the Internet.

The User Agent Manager Ž . UAM is the user interface of IDEAS that the user can use to input parameters or view the outcomes, as shown in Fig. 3. Each line in the Local Agent List illustrates the address<sup>r</sup>specification<sup>r</sup>status of an independent agent. Each agent can be activated or deactivated by the UAM. UAM can send a message to each agent. Fig. 4 shows the final allocation of BSV for each agent.

The negotiation procedure of the six-bus problem is illustrated Fig. 5. When the coordinator sends the START message to all six agents, agents begin to negotiate with each other. For example, preference list of agent 1 is empty, therefore it sends COM-PLETE message to the coordinator. Agent 4 sends REQUIRE message to agent 6 and it also receives REQUIRE message from agent 6. After calculating BSVs and identifying that the condition of super-additive is satisfied, agents 4 and 6 form a coalition.

After the coalition is formed, agent 4 becomes the representative of the coalition, and it sends a COM-PLETE message to the coordinator. After that, agent 2 sends REQUIRE message to agent 6. Since agent 6 has already agreed to form a coalition with agent 4, it has to turn down the invitation from agent 2 by sending a REFUSE message to agent 2. The other reason is that agent 4 is before agent 2 in the preference list of agent 6. When the coordinator receives COMPLETE messages from all the agents, the process stops. The coordinator updates the information in its own belief base and sends another START message to kick off the next round of negotiations.

![](/api/attachments/HX6P8Q4Z/fulltext/images/36d27f504eed6a153647689b32e9f90fc8a9957ea81ca1b27d1ba8a48aaec57f.jpg)  
Fig. 7. Result of coalition formation.

![](/api/attachments/HX6P8Q4Z/fulltext/images/5c660e6cfbcdfec1d5d73d63a50b7aa4cf508ef1c6dff9e34b1d969a7ce9c8e8.jpg)  
Fig. 8. Simplified structure of an agent system in IDEAS.

The log file of the communication messages that agent 2 has received are presented in Fig. 6. From the log file, it is easy to see that each message contains the information about the sender and the receiver, the message type, the message reference number and the priority of the message, etc. Fig. 7 shows the final results of the coalition formation. From Fig. 7, we can see the sequence of coalition formation. In the beginning, agent 3 and agent 5, as well as agent 4 and agent 6, form the first two two-agent coalitions. Then each two-agent coalition in the second round joins another agent to form a three-agent coalition. Finally, both three-agent coalitions join together to form the grand coalition.

![](/api/attachments/HX6P8Q4Z/fulltext/images/cce7a03cdc8452ea054c14e94296bf332d5691a9f293a20417e6c7642160c36d.jpg)  
Fig. 9. Coalition structure, 3, 5 1 4, 6 2 , with cost alloca-  4  44 44 tion.

Notice here that no global agent or central mediator exists. Each agent in IDEAS is autonomous and works in a completely decentralized environment. For belief representation and reasoning, each agent maintains his own belief base, which is written in BinProlog 19 . Agent<sup>w</sup> <sup>x</sup> plans can be specified by the appropriate developed rules for message evaluation. Actions can be defined in Tcl as well as in C. IDEAS provides some predefined standard actions for communication and managing the agents belief base, etc. Fig. 8 shows a simplified structure of a multi-agent agent system in IDEAS. For further details, please refer to Ref. 11 .<sup>w</sup> <sup>x</sup>

IDEAS provides a full range of features, supported by a set of components, which are needed for building comprehensive and decentralized multiagent systems. Such ability to support decentralized decision-making is the most important issue for selecting IDEAS to implement the multi-agent system to support coalition formation. The ability to support decentralized decision-making is the most important issue to develop systems to simulate the restructured or deregulated markets in which the players should have the rights to evaluate and select partners to form coalitions, as well as to determine how to allocate profits or costs among themselves. Therefore, determination of coalition formation and allocation of costs in the new market are better locally.

![](/api/attachments/HX6P8Q4Z/fulltext/images/a4b6acc5bfc3af552e6f1175a0a635b8c10eb98e8f40424180343c056aba26b4.jpg)  
Fig. 10. Coalition structure, 1 3, 5 2 4, 6 , with cost alloca-   44  444 tion.

The result of the cost allocation can also be represented by a coalition structure, as shown in Fig. 9. However, the process of coalition formation that leads to the final grand coalition may not be unique and another solution is given in Fig. 10.

## 7. Conclusions

The multi-agent system developed for this project was proved to be able to assist in the decision-making for coalition formation and cost allocation for electric utility industry. The multi-agent is capable of making decisions for coalition formation and cost allocation, with very limited coordination and synchronization provided by the coordinator, in a fully decentralized environment. Furthermore, it is easy to implement and to run on the Internet. Therefore, the users do not need to rent dedicated lines to support the communications. We could see that such multiagent systems can easily be applied to solve the problems where formation of coalition is essential and the environment is geographically dispersed, for example, global logistics planning or coalition formation of shipping and transportation firms.

The coalition formation in the multi-agent system is a hill climbing process. In each step of the coalition formation, the payoff for each agent should not be worse than the payoff of the previous step. However, such requirement may not be able to find the best solution for all the participants, it may get trapped in local minimum. In our future research, we will test other algorithms, such as, simulated annealing, to give the system greater flexibility.

When the negotiation process reaches the end, the cost or payoff for each agent must be allocated by a recursive algorithm, which is based on the coalition structure and the contribution from each agent that led to the final grand coalition. However, such negotiation may not consider all the possible coalitions. Therefore, an agent who is willing to form a coalition with some particular partner may not be guaranteed to be feasible. How to give agents additional flexibility, so that they can select partners not purely based on the profits or sharing of costs will be one of the items for us to improve our system.

## References

<sup>w</sup> <sup>x</sup> 1 M. Barbuceanu, M.X. Fox, Cool: a language for describing coordination in multi-agent systems, in: Proceedings of the First International Conference on Multi-Agent Systems Ž . ICMAS-95 , San Franscisco. pp. 17–24.

<sup>w</sup> <sup>x</sup> 2 R.J. Bennon, J.A. Juves, A.P. Melioppoulos, Use of sensitivity analysis automated transmission planning, IEEE Transactions on Power Apparatus and Systems PAS-101 1 1982Ž . Ž . IEEE, New York.

<sup>w</sup> <sup>x</sup> 3 J. Bushnell, S. Stoft, Transmission and Generation Investment in a Competitive Electric Power Industry, PWP-030,1995, May.

<sup>w</sup> <sup>x</sup> 4 H. Chao, S. Peck, A market mechanism for electric power transmission, Journal of Regulatory Economics 10 1996 Ž . 25–59.

<sup>w</sup> <sup>x</sup> 5 Y.P. Dusonchet, A.H. El-Abiad, Transmission planning using discrete dynamic optimization, in: IEEE Transactions on Power Apparatus and Systems PAS-89 IEEE, New York, 1973.

<sup>w</sup> <sup>x</sup> 6 T. Finin, R. Fritzson, D. McKay, R. McEntire, KQML as an agent communication language, in: Proceedings of the Third International Conference on Information and Knowledge Management CIKM’94, Gaithersburg, ACM Press, New York, 1994, pp. 456–463, November.

<sup>w</sup> <sup>x</sup> 7 L.L. Garver, Transmission net estimation using linear programming, IEEE Transactions on Power Apparatus and Systems PSA-89 7 1970 SeptŽ . Ž . <sup>r</sup>Oct.

<sup>w</sup> <sup>x</sup> 8 D. Gately, Sharing the gains from regional cooperation: a game theoretic application to planning investment in electric power, International Economic Review 15 1 1974 Febru-Ž . Ž . ary.

<sup>w</sup> <sup>x</sup> 9 L.A. Petrosjan, Game Theory, World Scientific Publishing Co., Singapore, 1996.

<sup>w</sup> <sup>x</sup> 10 S.P. Ketchpel, Coalition formation among autonomous agents, Proceedings of MAAMAW-93.

<sup>w</sup> <sup>x</sup> 11 M. Klusch, Utilitarian coalition formation between autonomous agents for cooperative information gathering, in: S. Krin, G. O’hare Eds. , Cooperative Knowledge Processing, Ž . Springer-Verlag, London, 1996, pp. 230–257.

<sup>w</sup> <sup>x</sup> 12 M. Klusch, O. Shehory, A polynomial kernel-oriented coalition algorithm for rational information agents, in: Proc. 2. International Conference on Multi-agent Systems ICMAS-96, Kyoto, Japan, AAAI Press, Menlo Park, Calif., 1996.

<sup>w</sup> <sup>x</sup> 13 S.T.Y. Lee, K.L. Hocks, E. Hnyilicza, Transmission expansion of branch-and-bound integer programming with optimal cost–capacity curves, IEEE Transactions on Power Apparatus and Systems PAS-93 5 1974 1390–1400, IEEE, NewŽ . Ž . York.

<sup>w</sup> <sup>x</sup> 14 M. Minsky, A conversation with Marvin Minsky about agents, Communications of ACM 37 7 1994 23–29, July.Ž . Ž .

<sup>w</sup> <sup>x</sup> 15 A. Monticelli, A. Santos, Jr., M.V.F. Pereira, S.H. Cunha, B.J. Parker, J.C.G. Praca, Interactive transmission network

planning using a least-effort criterion, IEEE Transactions on Power Apparatus and Systems, vol. PAS-101 No. 10, pp. 3919–3925, IEEE, New York, October, 1982.

<sup>w</sup> <sup>x</sup> 16 G.C. Oliveira, A.P.C. Costa, S. Binato, Large scale transmission network planning using optimization and heuristic techniques, IEEE Transactions on Power Systems, vol. 10, No. 4, pp. 1828–1834, IEEE, New York, November 1995

<sup>w</sup> <sup>x</sup> 17 L.S. Shapley, The value of an n-person game, in: H.W. Kuhn, A.W. Tucker Eds. , Contributions to the Theory ofŽ . Games II Princeton University Press, Princeton, 1953, pp. 307–317.

<sup>w</sup> <sup>x</sup> 18 O. Shehory, S. Kraus, A kernel-oriented model for coalition formation in general environments: implementation and results, in: Proceedings AAAI-96, Portland, OR, 1996.

<sup>w</sup> <sup>x</sup> 19 P. Tarau, BinProlog 3.0, User Guide, Universite de Moncton, Mocton, Canada.

<sup>w</sup> <sup>x</sup> 20 X. Wang, J.R. McDonald, Modern Power System Planning, McGraw-Hill, London, 1994.

<sup>w</sup> <sup>x</sup> 21 M.J. Woodridge, N.R. Jennings, Agent theories, architectures, and languages: a survey, in: M.J. Woodridge, N.R. Jennings Eds. , Intelligent Agents, Springer-Verlag, Berlin,Ž . 1995, pp. 1–22.

<sup>w</sup> <sup>x</sup> 22 F.F. Wu, P. Varaiya, Coordinated Multi-lateral Trades for Electric Power: Theory and Implementation, PWP-031,1995, June.

<sup>w</sup> <sup>x</sup> 23 K. Yoshimoto, K. Yasud, R. Yokohanma, Transmission expansion planning using neuro-computing hybridized with genetic algorithm, in: Proceedings of the 1995 International Conference on Evolutionary Computing, ICEC’95, pp. 126– 131.

Jerome Yen is an associate professor of the Department of Systems Engineering and Engineering Management at the Chinese University of Hong Kong and also an adjunct associate professor of the School of Computer Science at the Carnegie Mellon University. He received his PhD degree in Systems Engineering and Management Information Systems from the University of Arizona in 1992. His current research interests include digital library, information economics, information retrieval, intelligent agents, and financial engineering. He has published more than 20 journal articles in international journals, such as Journal of Management Information Systems, IEEE Computer, JASIS, Journal of Mathematical Economics, and International Review of Economics and Finance. He is the recipient of the best paper award at the 28th Hawaii International Conference on System Sciences. He is the Program Chair of the First Asia Digital Library Workshop.

Yonghe Yan is a doctoral student in Computer Science and Information Systems at the University of Hong Kong. His advisor is Dr. Jerome Yen. Mr. Yan received his BS in Computer Engineering and M.Eng. in Computer Science from the University of Electronic Science and Technology of China.

JaÕier Contreras received his PhD from the Department of Electrical Engineering and Computer Sciences of the University of California at Berkeley in May 1997. His thesis advisor was Professor Felix Wu currently on leave from University of Califor-Ž nia at Berkeley to the University of Hong Kong . His thesis topic. was ‘‘Power Systems Transmission Planning using cooperative game theory and decentralized optimization in power systems using the Ptolemy platform’’. He currently is teaching at the Universidad de Castilla — La Mancha, Spain.

Pai-Chun Ma was an assistant professor of Management Information Systems at the University of Delaware, DE, USA 1987–Ž 1994 , and a visiting scholar . <sup>r</sup>assistant professor of Information and Systems Management at the Hong Kong University of Science and Technology, Hong Kong 1994–1997 , before he joined Ž . the Baruch College, the City University of New York in 1997 prior to his graduate study at SUNY Buffalo MBA, 1982 andŽ . New York University PhD in I.S., 1988 in US. Dr. Ma’sŽ . research interest includes concept space based information retrieval for the digital library of financial disclosure documents of public firms in Hong Kong, negotiation support systems, scenario management for mathematical programming systems, semantic data modeling support systems, and metagraph applications.

Prof. Felix F. Wu is currently the Chair Professor of Electrical Engineering, the Director of Centre for Electrical Energy Systems, and also the Pro-Vice-Chancellor research of the University ofŽ . Hong Kong. He graduated from the National Taiwan University with a BS in 1965. In 1969, he received his MSc from the University of Pittsburgh and his PhD from the University of California, Berkeley in 1972. Prof. Wu has been an IEEE Fellow since 1989 for his contributions to the development of theory and computation methods for power system planning and operation. He was also the TEPCO Tokyo Electric Power Chair of ‘‘Fron-Ž . tier Technology for the Future Electric Energy System’’ in 1991. He has served as the Associate Editor of the IEEE Transactions on Circuits and Systems and the Guest Editor of the Proceedings of the IEEE. He has been the Visiting Professor of the Tsinghua University and University of Tokyo.
