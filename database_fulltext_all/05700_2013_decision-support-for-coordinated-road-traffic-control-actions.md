---
otero_id: 5700
otero_key: "JJ8NKGHW"
title: "Decision support for coordinated road traffic control actions"
authors: "Keshav Dahal; Khaled Almejalli; M. Alamgir Hossain"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.10.022"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision support for coordinated road traf<sup>fi</sup>c control actions

Keshav Dahal <sup>a,</sup>⁎, Khaled Almejalli <sup>a</sup>, M. Alamgir Hossain

<sup>a</sup> AI Research Group, Department of Computing, University of Bradford, BD7 1DP, UK

<sup>b</sup> Computational Intelligence Group, University of Northumbria at Newcastle, NE1 8ST, UK

## a r t i c l e i n f o

Article history: Received 12 January 2012 Received in revised form 3 July 2012 Accepted 2 October 2012 Available online 11 October 2012

Keywords: Intelligent Traf<sup>fi</sup>c Control System Coordinated-agent Fuzzy neural networks (FNNs) Decision support system

## a b s t r a c t

Selection of the most appropriate traf<sup>fi</sup>c control actions to solve non-recurrent traf<sup>fi</sup>c congestion is a complex task, which requires signi<sup>fi</sup>cant expert knowledge and experience. Also, the application of a control action for solving a local traf<sup>fi</sup>c problem could create traf<sup>fi</sup>c congestion at different locations in the network because of the strong interrelations between traf<sup>fi</sup>c situations at different locations of a road network. Therefore, coordination of control strategies is required to make sure that all available control actions serve the same objective. In this paper, an Intelligent Traf<sup>fi</sup>c Control System (ITCS) based on a coordinated-agent approach is proposed to assist the human operator of a road traf<sup>fi</sup>c control centre to manage the current traf<sup>fi</sup>c state. In the proposed system, the network is divided into sub-networks, each of which has its own associated agent. The agent of the sub-network with an incident reacts with other affected agents in order to select the optimal traf<sup>fi</sup>c control action, so that a globally acceptable solution is found. The agent uses an effective way of calculating the control action <sup>fi</sup>tness locally and globally. The capability of the proposed ITCS has been tested for a case study of a part of the traf<sup>fi</sup>c network in the Riyadh city of Saudi Arabia. The obtained results show its ability to identify the optimal global control action.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

When non-recurrent congestion happens, the operator at the traf<sup>fi</sup>c control centre has to assess quickly the severity of the situation, predict the most probable evolution of the state of the network, and select the most appropriate control actions [8,9]. There are a large number of traf-<sup>fi</sup>c factors and possible control actions that need to be considered during the decision making process. Also, the operator should consider the interrelations between traf<sup>fi</sup>c situations and the traf<sup>fi</sup>c control actions at different locations in the network. The traf<sup>fi</sup>c control actions in<sup>fl</sup>uencing a traf<sup>fi</sup>c situation in one area of a road network can also impact the traf<sup>fi</sup>c situation in neighbouring areas. The identi<sup>fi</sup>cation of suitable control actions for a given non-recurrent traf<sup>fi</sup>c congestion situation can be dif<sup>fi</sup>cult, even for experienced operators [7]. Therefore, an advanced traf<sup>fi</sup>c control system is needed that integrates the traf<sup>fi</sup>c state data with traf<sup>fi</sup>c monitoring and control software to help operators in decision making. Road traf<sup>fi</sup>c simulation models are used in many cases. However, simulating different traf<sup>fi</sup>c scenarios for a number of control actions in a complicated situation can be very time-consuming [9,13].

Much attention has been paid to the study and development of road traf<sup>fi</sup>c control systems over the last 20 years, during which some operational knowledge-based expert systems have been developed, including traf<sup>fi</sup>c signal and traf<sup>fi</sup>c light control systems [3,4,16], traf<sup>fi</sup>c control decision support systems [8,13,14], ramp metering control systems [5,9,18] and transportation emergency/accident response decision support systems [10,17]. Arti<sup>fi</sup>cial Intelligence (AI)-based systems have been investigated for the development of intelligent road traffic control systems using approaches such as fuzzy logic [6,8,16], neural networks [3], evolutionary computation [5,16] and their hybrids [5,12]. Generally, traf<sup>fi</sup>c control decision support systems are part of large intelligent transportation systems that have not been very effective due to lack of autonomous and collaborative behaviour of the constituent traf<sup>fi</sup>c control entities [4,7]. Therefore, the use of multi-agent architecture has been proposed for coordination and collaboration between traf<sup>fi</sup>c control entities [3,4,6,7,11]. Many traf<sup>fi</sup>c management applications have been developed using mainly expert knowledge or case-bases. This knowledge may vary from person to person, and from time to time. The quality of their results depends on the quality of the knowledge bases and case-bases. Moreover, these systems will not be able to generate decisions in cases that are not explicitly covered by such knowledge bases and case-bases.

In this paper, we propose an Intelligent Traf<sup>fi</sup>c Control System (ITCS) for supporting decision makers in traf<sup>fi</sup>c management centres to identify coordinated control actions from a global view. The proposed system is a major extension and improvement of the approach we have presented in our previous works [1,2]. In [1], we developed an intelligent traf<sup>fi</sup>c control decision support system (ITC-DSS) to help the operator to select the best local control actions for a localised network. The ITC-DSS, which uses a fuzzy neural network (FNN) as its engine, was tested for a small-sized network with a limited number of traf<sup>fi</sup>c situations and control actions. However, a large network requires many traf<sup>fi</sup>c variables to characterise its traf<sup>fi</sup>c state, and the number of possible traf<sup>fi</sup>c control actions to control the current state can be large [7,13]. Using ITC-DSS with such large numbers of inputs is not ef<sup>fi</sup>cient because the training process of the fuzzy neural network is overloaded.

To overcome this problem, the concept of a multiple ITC-DSS for a road network was tested in a small case study in [1]. In this paper we have extended this concept by developing a coordinated approach where a large network is divided into a number of sub-networks, each of which has its own agent with its own ITC-DSS. We propose an effective method for predicting the <sup>fi</sup>tness of the local control actions, using control action data tables and a predicted traf<sup>fi</sup>c change of the boundary conditions of a sub-network. The coordination between agents is achieved through a high level agent called a coordinator. The coordinator receives proposed local control actions from the agent of the incident's subnetwork, resolves con<sup>fl</sup>icts between other affected agents, and sends the globally acceptable solution back to that agent. The decision making process in the proposed ITCS uses a general framework with two AI techniques, namely fuzzy logic systems and neural networks. Using fuzzy techniques both numerical data and expert knowledge are used to build the structure of the system. The learning capability of neural networks updates the fuzzy rule base and the structure of the system when new data (or knowledge) become available. Moreover, the system applies adaptable factors in the calculation of the global performance of the control actions, which allows the human operators to <sup>fi</sup>nd the global control action that optimises the desired objectives in a large network.

## 2. The proposed Intelligent Traf<sup>fi</sup>c Control System

## 2.1. Structure

The overall structure of the proposed Intelligent Traf<sup>fi</sup>c Control System (ITCS) is depicted in Fig. 1, and the <sup>fl</sup>owchart of the decision process is illustrated in Fig. 2. Consider a traf<sup>fi</sup>c network consisting of several highway (motorway/freeway) links. Traf<sup>fi</sup>c enters the network via the origin of links (e.g. on-ramps or highway links coming from outside the network), and leaves the network via destination links (e.g. off-ramps or highway links going out of the network). The given traf<sup>fi</sup>c network is divided into overlapping regions, called sub-networks, and each sub-network is supervised and controlled by an agent. Each agent has three traf<sup>fi</sup>c subsystems (see Fig. 1).

In order to achieve effective coordinated performance between the agents and faster data <sup>fl</sup>ow, we propose the use of a control actions data-table $\left( C A _ { t a b l e } \right)$ for each of the sub-networks. This control actions table is constructed with all possible traf<sup>fi</sup>c control actions that can be applied on a sub-network. A traf<sup>fi</sup>c control action can be one control measure such as lane closure, ramp metering, variable message signs etc., or a combination of several control actions. The control actions data-table is generated for a given sub-network off-line using the available road control facilities, traf<sup>fi</sup>c operator's experience, and historical traf<sup>fi</sup>c data. This also takes into consideration the interrelations between the traf<sup>fi</sup>c control actions at different locations in the network.

![](/api/attachments/JJ8NKGHW/fulltext/images/0ce2b8cdad95880d18cdc5d894dc9365bab5a2a67609c3cd0929a2eaaeaa88bf.jpg)  
Fig. 1. The overall structure of the proposed Intelligent Traf<sup>fi</sup>c Control System (ITCS).

The structure of $C A _ { t a b l e }$ is illustrated in Table 1. Considering subnetwork $Z ,$ each record in $C A _ { t a b l e }$ is characterised by the following parameters:

• Traf<sup>fi</sup>c control action (ca ): name (or description) of the traf<sup>fi</sup>c control action that can be applied on the sub-network Z.

• Affected sub-networks (sn ): all sub-networks that might be in<sup>fl</sup>uenced by traf<sup>fi</sup>c control action $c a _ { i } .$ This <sup>fi</sup>eld is characterised by the following:

– Agent-ID (g<sub>j</sub>): the identity (or name) of the agent that controls the affected sub-network (sn<sub>j</sub>).

– In<sup>fl</sup>uence rates $( Y _ { j } ^ { i }$ and R<sup>i</sup> ), where $Y _ { j } ^ { i }$ represents percentage change (positive or negative) that may happen in the traf<sup>fi</sup>c <sup>fl</sup>ows from sub-network $Z$ to the affected sub-network (sn ) (i.e. sn traf<sup>fi</sup>c demand) due to the application of the traf<sup>fi</sup>c control action ca , and $R _ { j } ^ { i }$ representing the out<sup>fl</sup>ow restrictions for the affected subnetwork $( s n _ { j } )$ due to the application of the traf<sup>fi</sup>c control action ca . The value of $R _ { j } ^ { i }$ is given as a percentage and it means that the maximum out<sup>fl</sup>ow capacity will be reduced by $R _ { j } ^ { i }$ during the application of $c a _ { i } .$ The values of $Y _ { j } ^ { i }$ and $R _ { j } ^ { i }$ can be estimated using the historical data or alternatively using a traf<sup>fi</sup>c simulation program.

## 2.2. Operation

Once the control actions data-tables have been constructed for all sub-networks, they are used by the coordinator to identify the optimal global control actions as follows. A simple <sup>fl</sup>owchart of this process is illustrated in Fig. 2. Suppose there are 4 traf<sup>fi</sup>c agents (A, B, C, and D), which control 4 sub-networks $( s n _ { 1 } , s n _ { 2 } , s n _ { 3 } , s n _ { 4 } )$ , respectively. When a traf<sup>fi</sup>c problem is detected by the monitoring subsystem controlled by agent A, it runs its intelligent traf<sup>fi</sup>c control decision support system (ITC-DSS) to produce a ranked list of optimal local control actions (S) for the coordinator (see next section for a brief overview of ITC-DSS).

Each control action of S has a <sup>fi</sup>tness value calculated by agent A (i.e. local aggregated performance $P ^ { i } ) . \operatorname { L e t } S = \{ c a _ { 1 } , c a _ { 2 } , c a _ { 3 } \}$ . Next, all agents that will be affected by any control action of the proposed $S ,$ are determined by the coordinator using $C A _ { t a b l e } .$ Let Agent B be affected by $c a _ { 1 }$ and $c a _ { 2 } ,$ , Agent D be affected by ca and ca , and Agent C be not affected (i.e. its traf<sup>fi</sup>c state will not be affected by any control action of S). In this case, the coordinator will send $c a _ { 1 }$ and $c a _ { 2 }$ with their associated in<sup>fl</sup>uence rates $( Y _ { B } ^ { 1 }$ and $Y _ { B } ^ { 2 } )$ to Agent B to calculate their <sup>fi</sup>tness. Similarly, $c a _ { 1 }$ and $c a _ { 3 } ,$ , with their associated in<sup>fl</sup>uence rates $( Y _ { D } ^ { 1 }$ and $Y _ { D } ^ { 3 } )$ , will be sent to Agent D to calculate their <sup>fi</sup>tness.

The affected agents (B and D) will calculate the <sup>fi</sup>tness of the proposed control actions using the in<sup>fl</sup>uence rates, as we will see in Section 2.4, then will return the results to the coordinator. The global performance of each control action of S is predicted by the coordinator using the <sup>fi</sup>tness of the control actions received from agent A and the affected agents. The process of calculating the global performance of the control actions is explained in Section 2.5. Finally, the proposed control actions of agent A (S) will be re-ranked by the coordinator based on their global performance and returned to agent A. In some cases, agent A may need to use a traf<sup>fi</sup>c simulation program to effectively compare the best two (or more) control actions before applying them. If, for example, $c a _ { 1 }$ has been selected by agent A as an optimal global control action, the coordinator is responsible for informing agents B and D to guarantee that all applied control actions at that time serve the same objective. Thus, agents B and D can apply their selected local control actions (if any) simultaneously.

![](/api/attachments/JJ8NKGHW/fulltext/images/8f83520c56e3d16b6ac894beb78255a84dd65221c4cbc1fce41fbb09759409e0.jpg)  
Fig. 2. Flowchart of the process of the proposed ITCS.

## 2.3. Intelligent Traffic Control DSS (ITC-DSS)

As discussed earlier, an agent runs its Intelligent Traf<sup>fi</sup>c Control DSS (ITC-DSS) to assess the performance of a control action in local area. This section gives a brief overview. The overall structure of the ITC-DSS framework is depicted in Fig. 3. Further details about ITC-DSS including the training process have been reported in [1].

ITC-DSS is an intelligent system to assist the human operator of the traf<sup>fi</sup>c control centre to select the most promising traf<sup>fi</sup>c control action in real-time. ITC-DSS receives the current traf<sup>fi</sup>c state which is characterised by the average state (consisting of, e.g. day time, traf<sup>fi</sup>c densities, <sup>fl</sup>ows, speeds, in<sup>fl</sup>ow demands, out<sup>fl</sup>ow restrictions, incidents status) and all possible control actions. Then it produces a ranked list of the best control actions. ITC-DSS employs a pre-trained fuzzy-neural network tool (FNN-Tool) to predict the performance of each control action.

The structure of the fuzzy neural network tool (FNN-Tool) used in ITC-DSS is similar to the structure proposed in [12]. It is a <sup>fi</sup>ve-layer structure, as shown in Fig. 4, where each layer performs an operation for building the fuzzy system.

## 2.3.1. Layer 1 (input layer)

Nodes at this layer are input nodes which represent input linguistic variables such as “speed”, “traf<sup>fi</sup>c demand” and “incident severity”, and

## Table 1

The structure of the proposed control actions data-table $C A _ { t a b l e } .$

<table><tr><td rowspan="2">Traffic control action</td><td colspan="6">Affected sub-networks</td></tr><tr><td colspan="2"> $sn_1(g_1)$ </td><td colspan="2"> $sn_2(g_2)$ </td><td>...</td><td> $sn_j(g_j)$ </td></tr><tr><td> $ca_1$ </td><td> $Y_1^1$ </td><td> $R_1^1$ </td><td> $Y_2^1$ </td><td> $R_2^1$ </td><td>...</td><td> $Y_j^1$ </td></tr><tr><td> $ca_2$ </td><td> $Y_1^2$ </td><td> $R_1^2$ </td><td> $Y_2^2$ </td><td> $R_2^2$ </td><td>...</td><td> $Y_j^2$ </td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td> $ca_i$ </td><td> $Y_1^i$ </td><td> $R_1^i$ </td><td> $Y_2^i$ </td><td> $Y_2^i$ </td><td>...</td><td> $Y_j^i$ </td></tr></table>

directly transmit non-fuzzy input values to the next layer. Each node in this layer is connected to only those nodes of Layer 2, which represent the linguistic values of corresponding linguistic variables. The link weights between this layer and the next layer is unity.

## 2.3.2. Layer 2 (condition layer)

This layer de<sup>fi</sup>nes the fuzzy sets and membership functions for each of the input factors. Nodes in this layer act as a membership function and represent the terms of the respective linguistic variable, such as “low”, “medium”, or “high”. The input values are fed to this layer that calculates the membership degree. The connection weights in this layer are unity. The output $o _ { n , m } ^ { ( 2 ) ^ { \smile } }$ of input-label node $I L _ { n , m } ^ { ( \overline { { 2 } } ) }$ is given by $\begin{array} { r l } { e } & { { } - \frac { \left( o _ { n } ^ { ( 1 ) } - c _ { n , m } ^ { ( 2 ) } \right) ^ { 2 } } { \left( \sigma _ { n , m } ^ { ( 2 ) } \right) ^ { 2 } } } \end{array}$ where $c _ { n , m } ^ { ( 2 ) }$ and $\sigma _ { n , m } ^ { ( 2 ) }$ are the centres (or means) and the widths (or variances) of the membership function for the input-label node $I L _ { n , m } ^ { ( 2 ) }$ respectively, where ${ { I L } _ { n , m } }$ denotes the mth input label of the linguistic node n.

## 2.3.3. Layer 3 (fuzzy-rules layer)

This layer de<sup>fi</sup>nes all possible fuzzy rules to specify qualitatively how the output parameter is determined for various instances of the input parameters. Each node in this layer represents a fuzzy rule. The nodes in this layer perform the AND operation. The output $o _ { u } ^ { ( 3 ) }$ of a rule node $R L _ { u }$ at the layer 3 is given by $\bar { m } i n _ { i \in U } ( o _ { i } ^ { ( 2 ) } )$ , where U is the set of indices of the nodes in layer 2 that are connected to node $R L _ { u }$ in layer 3.

## 2.3.4. Layer 4 (consequence layer)

Each node in the consequence layer represents a possible consequent part of a fuzzy rule (such as “low” and “high”). The connection weights $W _ { u , n m }$ of the links connecting nodes $R L _ { u }$ in Layer 3 to $O L _ { n , m }$ in layer 4 represent certainty factors of the corresponding fuzzy rules when inferring fuzzy output values. Each node of this layer performs the fuzzy OR operation to integrate the <sup>fi</sup>eld rules leading to the same output linguistic variables. The initial values $W _ { u , n m }$ are set to unity. The output $o _ { n , m } ^ { ( 4 ) }$ of a consequence node $O L _ { n , m }$ in Layer 4 is given by ma $\mathfrak { X } _ { u \in G } \big ( O _ { u } ^ { ( 3 ) } W _ { u , n m } \big )$ , where G is the set of indices of the nodes $R L _ { u }$ in Layer 3 that are connected to node $O L _ { n , m }$ in Layer 4.

![](/api/attachments/JJ8NKGHW/fulltext/images/3c3285cde2d5c8ceda7549023783df5c364b2e0a7fc38917d4a1ef6cb50e573d.jpg)  
Fig. 3. The overall structure of ITC-DSS.

## 2.3.5. Layer 5 (output layer)

This layer is the defuzzi<sup>fi</sup>cation layer, where each node at this layer represents a single output variable. In this layer, either the Center of Gravity (COG) or Center of Area (COA) method can be used to compute a crisp output signal for each node. In our experiment, we used COG; the output $y _ { n } ^ { ( 5 ) }$ of an output node $D _ { n }$ in Layer 5 is given by $\begin{array} { r } { \sum _ { k \in F } \Bigl ( O _ { u , n m } ^ { ( 4 ) } \times C _ { u , n m } ^ { ( 4 ) } \times \sigma _ { u , n m } ^ { ( 4 ) } \Bigr ) } \end{array}$

, where H is the set of indices of the $\begin{array} { r } { \overline { { \sum _ { u \in H } \left( o _ { u , n m } ^ { ( 4 ) } \times \sigma _ { u , n m } ^ { ( 4 ) } \right) } } } \end{array}$

nodes $O L _ { n , m }$ in Layer 4 which are connected to node $D _ { n }$ in Layer 5 and $c _ { u , n m } ^ { ( 4 ) }$ and $\sigma _ { u , n m } ^ { ( 4 ) }$ are respectively, the centre and width of the membership function of the output linguistic value represented by $O L _ { n , m }$ in Layer 4. The weights of links from the nodes in Layer 4 to the nodes in Layer 5 are unity.

The inputs of FNN-Tool (i.e. X1,X2,..Xn) are the characteristics of the average current state, and a possible control action. The outputs of

FNN-Tool (i.e. Y1,Y2,..Yn) are the evaluation of that control action for the current traf<sup>fi</sup>c state over a number of performance criteria. There are a range of traf<sup>fi</sup>c performance criteria such as queue lengths at the origins of the network, total travel times, total distances travelled, number of vehicles entering the network, the number of vehicles leaving the network, etc [8]. These can be considered to assess the performance of a control action. The aggregated performance of each control action ca can be calculated by considering one or more of the performance criteria, or by using a weighted sum approach:

$$
P ^ {i} = \frac {\sum_ {d = 1} ^ {N} W _ {C _ {d}} E _ {C _ {d}} ^ {i}}{\sum_ {d = 1} ^ {N} W _ {C _ {d}}}\tag{1}
$$

where $0 { \le } P ^ { i } { \le } 1$ represents the aggregated performance of control action $c a _ { i }$ for the given traf<sup>fi</sup>c state; $w _ { C _ { d } }$ is the weight of the performance criterion $C _ { d } ;$ and N is the number of performance criteria considered. These weights $( w _ { C _ { d } } )$ are usually selected by the operators based on current traf<sup>fi</sup>c management policies and other considerations; $E _ { C _ { d } } ^ { i }$ is the evaluation of control action ca over the performance criterion $C _ { d }$ for the given traf<sup>fi</sup>c state $\left( E _ { C _ { d } } ^ { i } \right)$ is in the range [0,1], where a low value of

![](/api/attachments/JJ8NKGHW/fulltext/images/3b1cf97e4b4298c1be29af2b64cd998e0d660bc71cdbcfb17f3ccbc36e28b6f2.jpg)  
Fig. 4. Structure of the fuzzy neural network-tool (FNN-Tool).

![](/api/attachments/JJ8NKGHW/fulltext/images/3f32fc47461f9b569769d473cd3c07c69b26e3b0eb1c98f19a8d8ba0a49ee39e.jpg)  
Fig. 5. The Riyadh traf<sup>fi</sup>c network considered in the case study.

$E _ { C _ { d } } ^ { i }$ indicates a low performance of ca over the performance criterion C ). $E _ { C _ { d } } ^ { i }$ is calculated for control action ca as follow:

$$
E _ {C _ {d}} ^ {i} = 1 - \left(\frac {C _ {d} - C _ {d} ^ {\min}}{C _ {d} ^ {\max} - C _ {d} ^ {\min}}\right)\tag{2}
$$

where $C _ { d } ^ { \mathrm { m i n } }$ and $C _ { d } ^ { \mathrm { m a x } }$ are the minimum and the maximum values of $C _ { d } .$

## 2.4. Calculation of control action fitness

Once the affected agents receive the proposed local control actions (ca ) with their associated in<sup>fl</sup>uence rates $( Y _ { j } ^ { i }$ and $R _ { j } ^ { i } )$ from the coordinator, they run their ITC-DSS subsystems to calculate their <sup>fi</sup>tness for the proposed control actions. Referring to our example, A is the agent which detected the problem and B is the agent which is affected by the control action $c a _ { 1 }$ and $c a _ { 2 } .$ To calculate the <sup>fi</sup>tness of $c a _ { 1 } ,$ agent B runs its pre-trained ITC-DSS. In this case, the input of ITC-DSS will be the current traf<sup>fi</sup>c state of sub-network $\left( s n _ { 2 } \right)$ (including any current traf<sup>fi</sup>c accidents, the predicted traf<sup>fi</sup>c demand, and the out<sup>fl</sup>ow restrictions due to the application of $( c a _ { 1 } )$ and only the internal control actions that mainly in<sup>fl</sup>uence the traf<sup>fi</sup>c <sup>fl</sup>ows within its network (such as shoulder lane opening or variable speed limits). The main reason behind agent B using only the internal control actions is to ensure that the nominated control actions will not have the negative knock on effect by creating a new problem for one or more of its neighbours.

The considered traf<sup>fi</sup>c states of the three sub-networks.

<table><tr><td>Traffic variables</td><td>King Fahad sub-network</td><td>Olaya sub-network</td><td>Takhassusi sub-network</td></tr><tr><td>TDm</td><td>6800</td><td>7500</td><td>4000</td></tr><tr><td>TDn</td><td>32</td><td>24</td><td>9</td></tr><tr><td>IS</td><td>75%</td><td>0%</td><td>0%</td></tr><tr><td>OFR</td><td>0%</td><td>0%</td><td>0%</td></tr></table>

The predicted traf<sup>fi</sup>c demand of the sub-network associated with agent B (i.e. sn ) coming from the sub-network associated with agent $A \ ( { \mathrm { i . e . } } \ s n _ { 1 } )$ due to the application of $c a _ { 1 } ,$ can be calculated by using the in<sup>fl</sup>uence rate $( Y _ { B } ^ { 1 } )$ as follows:

$$
P \_ D e m _ {j} ^ {i} = C \_ D e m _ {j} + \left(C \_ D e m _ {j} * ^ {Y _ {j} ^ {i}} / _ {1 0 0}\right)\tag{3}
$$

where $P _ { - } D e m _ { j } ^ { i }$ and $C _ { - } D e m _ { j }$ denote the predicted and the current traf-<sup>fi</sup>c demand of the affected sub-network associated with agent g coming from the sub-network $s n _ { 1 }$ associated with agent A respectively.

Finally, the best internal control action will be selected by agent B and its aggregated performance will be sent as agent B's <sup>fi</sup>tness $\left( F _ { B } ^ { 1 } \right)$ of ca to the coordinator. The <sup>fi</sup>tness of a control action (F<sup>i</sup>) is in the range of [0,1]. When $F _ { j } ^ { i }$ equals zero, the control action $c a _ { i }$ is totally unsuitable for agent g (i.e. for sub-network sn ). In contrast, when F<sup>i</sup> equals 1, the control action $c a _ { i }$ is totally suitable.

## 2.5. Calculation of control action global performance

The process of calculating the global performance of a control action is performed by the coordinator. All affected agents will calculate the <sup>fi</sup>tness of the proposed control actions received from the coordinator according to their traf<sup>fi</sup>c states, and then return the results to the coordinator. The global performance $p _ { g } ^ { i }$ for each proposed local control action $c a _ { i }$ is now determined as:

The current and the maximum possible traf<sup>fi</sup>c demands (C \_Dem and Max \_OF ) of Olaya and Takhassusi sub-networks coming from King Fahad sub-network.

<table><tr><td>Traffic variables</td><td>Olaya sub-network</td><td>Takhassusi sub-network</td></tr><tr><td> $C\_Dem_{j}$ </td><td>943.4</td><td>809.84</td></tr><tr><td> $Max\_OF_{j}$ </td><td>4000</td><td>4000</td></tr></table>

The performance evaluation of the control actions $c a _ { 1 } ,$ ca , ca , $, c a _ { 4 } ,$ , and $c a _ { 5 }$ on the selected traf<sup>fi</sup>c state

<table><tr><td>Control actions (ranked)</td><td>TTT</td><td> $E_{TTT}$ </td><td>TDT</td><td> $E_{TDT}$ </td><td> $P^i$ </td></tr><tr><td> $ca_3$ </td><td>3101.56</td><td>0.99</td><td>201,913.5</td><td>0.28</td><td>0.81</td></tr><tr><td> $ca_1$ </td><td>4484.64</td><td>0.79</td><td>173,100.2</td><td>0.45</td><td>0.70</td></tr><tr><td> $ca_4$ </td><td>5483.23</td><td>0.65</td><td>166,845.7</td><td>0.49</td><td>0.61</td></tr><tr><td> $ca_5$ </td><td>7007.4</td><td>0.43</td><td>111,118.8</td><td>0.82</td><td>0.53</td></tr><tr><td> $ca_2$ </td><td>7013.02</td><td>0.43</td><td>111,606.7</td><td>0.81</td><td>0.52</td></tr></table>

$$
p _ {g} ^ {i} = \frac {p _ {l} ^ {i} + \sum_ {j = 1} ^ {N} \left(F _ {j} ^ {i} w _ {j} \mu_ {j} ^ {i}\right)}{1 + \sum_ {j = 1} ^ {N} \left(w _ {j} \mu_ {j} ^ {i}\right)}\tag{4}
$$

where p<sup>i</sup> is the aggregated performance of the control action ca which is calculated by agent A (i.e. the local <sup>fi</sup>tness of ca of agent $A ) ;$ N is the number of affected agents; F<sup>i</sup> is the <sup>fi</sup>tness of ca which is provided by the affected agent $g _ { j }$ (according to our example g {B,D}); the weights $w _ { j } { > } 0$ represent the relative importance of agent g . The weights (w ) are not necessarily <sup>fi</sup>xed, but can be changed on-line by the coordinator, depending on the current traf<sup>fi</sup>c management policies and other considerations; and u<sup>i</sup> is a measure that shows how much impact the traf<sup>fi</sup>c control action ca is having on the affected sub-network associated with agent $g _ { j } .$ When u<sup>i</sup> is high, ca has a high impact on the traf<sup>fi</sup>c state of the sub-network associated with agent g . When u<sup>i</sup> is low, ca has a low impact on the traf<sup>fi</sup>c state of the sub-network associated with agent $g _ { j } .$ u<sup>i</sup> is calculated by the coordinator using in<sup>fl</sup>uence rates (Y and R ) from $C A _ { t a b l e }$ as follows :

$$
\mu_ {j} ^ {i} = \left\{ \begin{array}{l} \left(Y _ {j} ^ {i} / 1 0 0 * \frac {P - D e m _ {j} ^ {i}}{\text { Max } _ {O F _ {j}}}\right) + R _ {j} ^ {i} / 1 0 0 \text {   if   } Y _ {j} ^ {i} > 0 \\ \hline R _ {j} ^ {i} / 1 0 0 \end{array} \right. \text {   otherwise }\tag{5}
$$

where P \_Dem<sup>i</sup> is the predicted traf<sup>fi</sup>c in<sup>fl</sup>ow into the affected subnetwork associated with agent g coming from the sub-network associated with agent A due to the application of ca (i.e. traf<sup>fi</sup>c demand of agent j). P \_Dem<sup>i</sup> can be calculated by using Eq. (3). Max \_OF is the maximum possible traf<sup>fi</sup>c in<sup>fl</sup>ow into the affected sub-network associated with agent g coming from the sub-network associated with agent A (e.g. the maximum capacity of the links between two sub-networks).

When two or more traf<sup>fi</sup>c problems are detected by different agents, the coordinator is responsible for ranking those agents based on their importance at that time, with the most important one being considered <sup>fi</sup>rst. Other agents with lower priority will consider their traf<sup>fi</sup>c problems as a part of current traf<sup>fi</sup>c states when they use their ITC-DSS to calculate the <sup>fi</sup>tness of the local control actions proposed by the most important agent.

CA for the King Fahd sub-network with the <sup>fi</sup>ve control actions.

<table><tr><td rowspan="4">Control actions</td><td colspan="5">Affected sub-networks</td></tr><tr><td colspan="3">Olaya sub-network r (agent B)</td><td colspan="2">Takhassusi sub-network (agent C)</td></tr><tr><td rowspan="2"> $Y_B^i$ </td><td colspan="2"> $R_B^i$ </td><td rowspan="2"> $Y_C^i$ </td><td rowspan="2"> $R_C^i$ </td></tr><tr><td>L1</td><td>L2</td></tr><tr><td> $ca_1$ </td><td>+207.6%</td><td>0%</td><td>0%</td><td>-24.2%</td><td>0%</td></tr><tr><td> $ca_2$ </td><td>+76.3%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td> $ca_3$ </td><td>+283.9%</td><td>0%</td><td>0%</td><td>-24.2%</td><td>0%</td></tr><tr><td> $ca_4$ </td><td>-8.7%</td><td>0%</td><td>0%</td><td>+225.1%</td><td>0%</td></tr><tr><td> $ca_5$ </td><td>+76.3%</td><td>30%</td><td>0%</td><td>0%</td><td>0%</td></tr></table>

The values of ${ w _ { C _ { d } } } , { C _ { d } ^ { m i n } }$ and $C _ { d } ^ { m a x }$ used by agents B and C to calculate the aggregated performance of each control action.

<table><tr><td rowspan="2">Traffic sub-networks</td><td colspan="3">TTT</td><td colspan="3">TDT</td></tr><tr><td> $w_{TTT}$ </td><td> $TTT_{min}$ </td><td> $TTT_{max}$ </td><td> $w_{TDT}$ </td><td> $TDT_{min}$ </td><td> $TDT_{max}$ </td></tr><tr><td>King Fahad sub-network</td><td>1.5</td><td>3000</td><td>10,000</td><td>0.5</td><td>80,000</td><td>250,000</td></tr><tr><td>Olaya sub-network</td><td>1.0</td><td>3300</td><td>8800</td><td>0</td><td>150,000</td><td>300,000</td></tr><tr><td>Takhassusi sub-network</td><td>1.5</td><td>1800</td><td>7000</td><td>0.5</td><td>180,000</td><td>250,000</td></tr></table>

## 3. The application and experiments

## 3.1. Riyadh traffic case study

In order to assess the technical feasibility of the proposed Intelligent Traf<sup>fi</sup>c Control System (ITCS), a traf<sup>fi</sup>c case-study was considered for a part of the traf<sup>fi</sup>c network in the city of Riyadh in Saudi Arabia (see Fig. 5). The selected network consists of three parallel highways (the Olaya highway, the King Fahad highway, the Takhassusi highway) connected via several on- and off-ramps. In this case study, we only consider traf<sup>fi</sup>c going from the south to the north (i.e. towards the city centre). Traf<sup>fi</sup>c enters the network from <sup>fi</sup>ve origins (O1, O2, O3, O4, and O5) and leaves the network through six destinations (D1, D2, D3, D4, D5, and D6). We have divided the network into three subnetworks King Fahad, Olaya, and Takhassusi (see Fig 5), controlled and managed by three agents A, B, and C, respectively.

The sub-networks have been simulated separately using METANET [15] for several traf<sup>fi</sup>c states and different control actions with the following parameters:

• Incidents vary in severity from 20% to 80% of reduction in link capacity;

• Simulated time period two hours (e.g. from 9:00 am to 11:00 am);

• The traf<sup>fi</sup>c state has been represented by: average traf<sup>fi</sup>c demand (TDm), average traf<sup>fi</sup>c density (TDn), incident severity (IS), and out-<sup>fl</sup>ow restrictions (OFR). The generated data has been used to train the ITC-DSS and to create a $C A _ { t a b l e }$ for each sub-network.

Note that the results presented in this section are not intended to verify the ability of ITC-DSS to correctly predict the optimal local control actions, because this has already been done in [1]. The aim is to demonstrate the technical feasibility of ITCS, and to show how the traf<sup>fi</sup>c agents react with the coordinator in order to effectively identify the optimal global control action from optimal local control actions.

## 3.2. Applying ITCS

To apply the proposed coordinated approach in ITCS, we have considered the following frequent traf<sup>fi</sup>c status as a case study:

The predicted performance of the <sup>fi</sup>ve control actions for agent B.

<table><tr><td>Control actions</td><td>TTT</td><td> $E_{TTT}$ </td><td>TDT</td><td> $E_{TDT}$ </td><td>Aggregated performance (fitness)</td></tr><tr><td> $ca_1$ </td><td>7500.35</td><td>0.24</td><td>237,209.50</td><td>0.42</td><td>0.24</td></tr><tr><td> $ca_2$ </td><td>4771.25</td><td>0.73</td><td>235,074.10</td><td>0.43</td><td>0.73</td></tr><tr><td> $ca_3$ </td><td>8796.80</td><td>0.00</td><td>232,126.80</td><td>0.45</td><td>0.00</td></tr><tr><td> $ca_4$ </td><td>3373.71</td><td>0.99</td><td>247,009.50</td><td>0.35</td><td>0.99</td></tr><tr><td> $ca_5$ </td><td>5935.66</td><td>0.52</td><td>222,331.50</td><td>0.52</td><td>0.52</td></tr></table>

Table 8  
The predicted performance of the <sup>fi</sup>ve control actions for agent C.

<table><tr><td>Control actions</td><td>TTT</td><td> $E_{TTT}$ </td><td>TDT</td><td> $E_{TDT}$ </td><td>Aggregated performance (fitness)</td></tr><tr><td> $ca_{1}^{A}$ </td><td>1792.28</td><td>1.00</td><td>180,820.40</td><td>0.99</td><td>1.00</td></tr><tr><td> $ca_{2}^{A}$ </td><td>1871.61</td><td>0.99</td><td>187,451.30</td><td>0.89</td><td>0.97</td></tr><tr><td> $ca_{3}^{A}$ </td><td>1792.28</td><td>1.00</td><td>180,820.40</td><td>0.99</td><td>1.00</td></tr><tr><td> $ca_{4}^{A}$ </td><td>2753.42</td><td>0.82</td><td>248,387.90</td><td>0.02</td><td>0.62</td></tr><tr><td> $ca_{5}^{A}$ </td><td>1871.61</td><td>0.99</td><td>187,451.30</td><td>0.89</td><td>0.97</td></tr></table>

• The traf<sup>fi</sup>c entering the King Fahad sub-network is divided as follows: 20% goes to destination D1 (97% uses the King Fahad highway, and 3% uses the Olaya highway), 55% goes to destination D2 (90% uses the King Fahad highway, 6% uses the Takhassusi highway, and 4% uses the Olaya highway), while the rest goes to destinations D3 (5%), D4 (10%), D5 (5%), and D6 (5%);

• The traf<sup>fi</sup>c entering the Olaya sub-network is divided as follows: 20% goes to destination D3, 60% goes to destination D4, and the rest goes to destinations D1 (10%) and D2 (10%);

• The traf<sup>fi</sup>c entering the Takhassusi sub-network is divided as follows: 70% goes to destination D6, 20% goes to destination D5, and the rest goes to destinations D2 (10%);

• There are <sup>fi</sup>ve possible local traf<sup>fi</sup>c control actions selected by agent A based on their local performances to solve the incident problem in King Fahad sub-network :

ca1: Using VMS at point A to direct traf<sup>fi</sup>c that goes to D2 to use the Olaya highway.

ca2: Using VMS at point A to direct traf<sup>fi</sup>c that goes to D1 to use the Olaya highway.

ca3: Using VMS at point A to direct traf<sup>fi</sup>c that goes to D1 and traf<sup>fi</sup>c that goes to D2 to use the Olaya highway.

ca4: Using VMS at point A to direct traf<sup>fi</sup>c that goes to D2 to use the Takhassusi highway.

ca5: Using VMS at point A to direct traf<sup>fi</sup>c that goes to D1 to use the Olaya highway and on Ramp Metering at point B.

• The aggregated performance of the control actions is calculated using two evaluation criteria:

– Total Travel Time (TTT).

– Total Distance Travelled (TDT).

The considered current traf<sup>fi</sup>c states of the three sub-networks are summarised in Table 2. In this part of the experiment, we have assumed a heavy traf<sup>fi</sup>c state in the Olaya sub-network, and a smooth traf<sup>fi</sup>c state in the Takhassusi sub-network. The current and the maximum possible traf<sup>fi</sup>c demands (C \_Dem and Max \_ $. O F _ { j } )$ of Olaya and Takhassusi sub-networks coming from King Fahad sub-network are shown in Table 3.

Table 9  
Summary of the <sup>fi</sup>nal results of the proposed coordinated approach of the ITCS.

<table><tr><td rowspan="3">Control action (ranked)</td><td rowspan="3">Local aggregated performance</td><td colspan="2">Olaya sub-network</td><td colspan="2">Takhassusi sub-network</td><td rowspan="3">Global aggregated performance</td></tr><tr><td colspan="2"> $w_B$ : 1</td><td colspan="2"> $w_C$ : 0.5</td></tr><tr><td>Fitness (F)</td><td>μ</td><td>Fitness (F)</td><td>μ</td></tr><tr><td> $ca_4$ </td><td>0.61</td><td>0.99</td><td>0.00</td><td>0.62</td><td>1.48</td><td>0.61</td></tr><tr><td> $ca_2$ </td><td>0.52</td><td>0.73</td><td>0.32</td><td>0.96</td><td>0.00</td><td>0.57</td></tr><tr><td> $ca_5$ </td><td>0.53</td><td>0.52</td><td>0.62</td><td>0.96</td><td>0.00</td><td>0.52</td></tr><tr><td> $ca_1$ </td><td>0.70</td><td>0.24</td><td>1.51</td><td>1.00</td><td>0.00</td><td>0.42</td></tr><tr><td> $ca_3$ </td><td>0.81</td><td>0.00</td><td>2.57</td><td>1.00</td><td>0.00</td><td>0.23</td></tr></table>

Table 10  
Brief description of the ten control actions considered in this part of the experiment.

<table><tr><td>Control action</td><td>Description</td><td>Control action</td><td>Description</td></tr><tr><td> $ca_0$ </td><td>Doing nothing</td><td> $ca_5$ </td><td>Using VMS at point A to direct traffic that goes to D1 to use the Olaya highway and traffic that goes to D2 to use the Takhassusi highway.</td></tr><tr><td> $ca_1$ </td><td>Using VMS at point A to direct traffic that goes to D2 to use the Olaya highway.</td><td> $ca_6$ </td><td>Using VMS at point A to direct traffic that goes to D2 to use the Olaya highway&amp; on ramp metering at point B.</td></tr><tr><td> $ca_2$ </td><td>Using VMS at point A to direct traffic that goes to D1 to use the Olaya highway.</td><td> $ca_7$ </td><td>Using VMS at point A to direct traffic that goes to D1 to use the Olaya highway and applying Lane Closure on points C&amp;D.</td></tr><tr><td> $ca_3$ </td><td>Using VMS at point A to direct traffic that goes to D1&amp;D2 to use the Olaya highway.</td><td> $ca_8$ </td><td>Shoulder Lane Opening on section (S1–S2) on the King Fahad highway and on ramp metering at points B, C &amp; D.</td></tr><tr><td> $ca_4$ </td><td>Using VMS at point A to direct traffic that goes to D2 to use the Takhassusi highway</td><td> $ca_9$ </td><td>Using VSL at point A to reduce the speed limit from 90 k/h to 60 k/h, and Shoulder Lane Opening on section (S1–S2) on the King Fahad highway.</td></tr></table>

## 3.3. Calculation of control actions local performance

The local performance of the <sup>fi</sup>ve control actions (ca , ca , ca , ca and ca ) were predicted by ITC-DSS of agent A, as explained in Section 2.3.Table 4 illustrates the <sup>fi</sup>nal results of this stage. The predicted TTT and TDT of the <sup>fi</sup>ve control actions on the traf<sup>fi</sup>c state under consideration obtained by ITC-DSS of agent A, are summarised in columns 2 and 4. For each control action, $E _ { T T T }$ and $E _ { T D T }$ have been calculated using Eq. (2) and summarised in columns 3 and 5. The aggregated performance $P ^ { i }$ of each control action has been calculated using Eq. (1) and summarised in column 6 (the values of $w _ { C _ { d } }$ are shown in Table 6). As can be seen, agent A recommends $c a _ { 3 }$ as an optimal solution to control the traf<sup>fi</sup>c state under consideration with aggregated performance (0.81), while it does not recommend $c a _ { 2 }$ with aggregated performance (0.52). Note that the obtained results of this stage only represent the local performance of the control actions which were proposed by Agent A to solve its traf<sup>fi</sup>c problem. In the following sections we will see how ITCS can be applied to identify the optimal global control action from those <sup>fi</sup>ve control actions.

Table 11  
The $C A _ { t a b l e }$ for the King Fahad sub-network with the ten control actions

<table><tr><td rowspan="4">Control actions</td><td colspan="5">Affected sub-networks</td></tr><tr><td colspan="3">Olaya sub-network (agent B)</td><td colspan="2">Takhassusi sub-network (agent C)</td></tr><tr><td rowspan="2"> $Y_B^i$ </td><td colspan="2"> $R_B^i$ </td><td rowspan="2"> $Y_C^i$ </td><td rowspan="2"> $R_C^i$ </td></tr><tr><td>L1</td><td>L2</td></tr><tr><td> $ca_0$ </td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td> $ca_1$ </td><td>+207.6%</td><td>0%</td><td>0%</td><td>-24.2%</td><td>0%</td></tr><tr><td> $ca_2$ </td><td>+76.3%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td> $ca_3$ </td><td>+283.9%</td><td>0%</td><td>0%</td><td>-24.2%</td><td>0%</td></tr><tr><td> $ca_4$ </td><td>-8.7%</td><td>0%</td><td>0%</td><td>+225.1%</td><td>0%</td></tr><tr><td> $ca_5$ </td><td>+68%</td><td>0%</td><td>0%</td><td>+255.1%</td><td>0%</td></tr><tr><td> $ca_6$ </td><td>+76.3%</td><td>30%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td> $ca_7$ </td><td>+207.6%</td><td>0%</td><td>25%</td><td>-24.2%</td><td>25%</td></tr><tr><td> $ca_8$ </td><td>0%</td><td>30%</td><td>30%</td><td>0%</td><td>30%</td></tr><tr><td> $ca_9$ </td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr></table>

![](/api/attachments/JJ8NKGHW/fulltext/images/00ee5c9a61ca5fb8ab101550863955066f78ab75ab008ee0089e0dd2550462d4.jpg)  
Fig. 6. The <sup>fi</sup>rst traf<sup>fi</sup>c scenario for the three traf<sup>fi</sup>c sub-networks.

As we mentioned before, a $C A _ { t a b l e }$ can be created using historical traf-<sup>fi</sup>c data or a traf<sup>fi</sup>c simulation model. In this experiment we have used the METANET program. Table 5 shows the $C A _ { t a b l e }$ for the King Fahad sub-network with the <sup>fi</sup>ve control actions $( c a _ { 1 } , c a _ { 2 } , c a _ { 3 } , c a _ { 4 }$ and ca ). Due to the fact that the Olaya sub-network is connected with the King Fahad sub-network via two out<sup>fl</sup>ow links L1 and L2 (see Fig. 5), the restriction of the out<sup>fl</sup>ow capacity $( R _ { j } ^ { i } )$ <sup>fi</sup>eld is represented by two columns (columns $3 \ \& \ 4 ) .$ . For example, as can be seen from the table, the traf<sup>fi</sup>c control $c a _ { 1 }$ affects the traf<sup>fi</sup>c demand on the Olaya sub-network negatively by 207.6% and the traf<sup>fi</sup>c demand on the Takhassusi sub-network positively by 24.2%. That is, $c a _ { 1 }$ increases the traf<sup>fi</sup>c in<sup>fl</sup>ow into the Olaya sub-network from the King Fahad sub-network by 207.6%, and decreases the traf<sup>fi</sup>c in<sup>fl</sup>ow into the Takhassusi sub-network from the King Fahad sub-network by 24%. This is because 55% traf<sup>fi</sup>c that enters the King Fahad sub-network and needs to go to D2 is directed by $c a _ { 1 } ^ { A } .$

## 3.4. Creating $C A _ { t a b l e }$ for the King Fahd sub-network

Table 5 also shows that only ca reduces the maximum out<sup>fl</sup>ow capacity L1 of the Olaya sub-network by 30%, while there is no negative effect on the out<sup>fl</sup>ow of the Takhassusi sub-network from any control action. It is worth noting that the restriction of out<sup>fl</sup>ow capacity of a link does not have that much of a negative impact if the traf<sup>fi</sup>c out-<sup>fl</sup>ow in that link is low. For example, if the maximum capacity of a link is 4000 vehicles/hour, 30% restriction mainly affects the subnetwork out<sup>fl</sup>ow when the traf<sup>fi</sup>c out<sup>fl</sup>ow of that link is more than 2800 vehicles/hour.

## 3.5. Calculation of control action fitness

Agents B and C (the affected agents) calculate the local <sup>fi</sup>tness of ca , $c a _ { 2 } , c a _ { 3 } , c a _ { 4 }$ and $c a _ { 5 }$ using their ITC-DSS, as explained earlier. Table 6 summarises the values of ${ w _ { C } } _ { d } , C _ { d } ^ { m i n }$ and $C _ { d } ^ { m a x }$ used by agents A, B and C to calculate the aggregated performance (<sup>fi</sup>tness) of each control action. The table shows that $w _ { T D T }$ is assigned 0 by agent B, indicating that TTT is the only considered performance criterion at that time. As mentioned before, the values of $w _ { C _ { d } } , C _ { d } ^ { m i n }$ and $C _ { d } ^ { m a x }$ are not <sup>fi</sup>xed. They are assigned by the operator based on the traf<sup>fi</sup>c state or other policies.

Agents B and C (the affected agents) calculate the local <sup>fi</sup>tness of ca , $c a _ { 2 } , c a _ { 3 } , c a _ { 4 }$ and $c a _ { 5 }$ using their ITC-DSS, as explained earlier. Table 6 summarises the values of ${ w _ { C } } _ { d } , C _ { d } ^ { m i n }$ and $C _ { d } ^ { m a x }$ used by agents A, B and C to calculate the aggregated performance (<sup>fi</sup>tness) of each control action. The table shows that w is assigned 0 by agent B, indicating that TTT is the only considered performance criterion at that time. As mentioned before, the values of $\bar { w } _ { C _ { d } } , C _ { d } ^ { m i n }$ and $C _ { d } ^ { m a x }$ are not <sup>fi</sup>xed. They are assigned by the operator based on the traf<sup>fi</sup>c state or other policies.

Tables 7 and 8 summarise the best performance of the <sup>fi</sup>ve control actions $c a _ { 1 } , c a _ { 2 } , c a _ { 3 } , c a _ { 4 }$ and $c a _ { 5 }$ predicted by agents B and C respectively after considering the traf<sup>fi</sup>c demands and the out<sup>fl</sup>ow restrictions imposed by agent A, and their internal control actions. In this part of the experiment we have considered two internal control actions for Agent B: 1) doing nothing; 2) shoulder lane opening on section (S3–S4); and two internal control actions for agent C: 1) doing nothing; 2) reduce the speed limit from 90 k/h to 60 k/h using VSL at point E (see Fig. 5). For each control action, $E _ { T T T }$ and $E _ { T D T }$ have been calculated using Eq. (2) and summarised in columns 3 and 5. The aggregated performances (<sup>fi</sup>tness) of the control actions, which will be returned to the coordinator, are calculated using Eq. (1) and listed in column 6 of each table.

It is observed from Table 7 that $c a _ { 4 }$ is recommended by agent B (with <sup>fi</sup>tness 0.99) because the application of ca does not increase the traf<sup>fi</sup>c in-<sup>fl</sup>ow to Olaya sub-network, while $c a _ { 3 }$ is completely rejected (with <sup>fi</sup>tness 0.0) because it increases the Olaya sub-network in<sup>fl</sup>ow which affects the sub-network traf<sup>fi</sup>c state very negatively. $c a _ { 5 }$ has a moderately negative impact on the in<sup>fl</sup>ow and the out<sup>fl</sup>ow of the Olaya sub-network and has 0.52 <sup>fi</sup>tness. On the other hand, Table 8 shows that agent C strongly recommends all control actions except $c a _ { 4 } ,$ which increases the traf<sup>fi</sup>c in<sup>fl</sup>ow to the Takhassusi sub-network. However, $c a _ { 4 }$ is still accepted by agent C (with <sup>fi</sup>tness 0.62), because the traf<sup>fi</sup>c <sup>fl</sup>ow in the Takhassusi subnetwork at that time is smooth.

## 3.6. Calculation of control action global performance

Table 9 summarises the <sup>fi</sup>nal results of the proposed coordinated approach for calculating the global performance for the <sup>fi</sup>ve control actions. The table shows that the Olaya sub-network is assigned a larger weight, $w = 1$ , than the Takhassusi sub-network $( w = 0 . 5 )$ , indicating the high importance of the Olaya sub-network at that time. The μ value of each sub-network, which indicates how the sub-network was affected by the control actions, are computed for each control action using Eq. (5) and summarised in columns 4 and 6. The local and the global performance of the control actions are given in the second and the last columns of the table, respectively.

It is observed from Table 9 that the optimal global control action is $c a _ { 4 }$ which can reduce the congestion in the King Fahad sub-network and also improve the overall traf<sup>fi</sup>c state in the network. Although ca has the best local performance to solving the traf<sup>fi</sup>c congestion in the King Fahad sub-network, it is not the optimal global control action.

That is simply because ca passes a large number of vehicles from the King Fahad sub-network to the Olaya Sub-network at a time when the Olaya sub-network is suffering from bad traf<sup>fi</sup>c, which will not improve the overall traf<sup>fi</sup>c state in the network overall.

## 3.7. Validation of the results

The performance of the proposed ITCS for this case study (Fig. 5) has been evaluated by comparing with the simulation model, the results of the ITCS and the results obtained by the traf<sup>fi</sup>c simulation model METANET [15]. In order to validate the results obtained from the proposed ITCS, the case study has been simulated as one large traf<sup>fi</sup>c network using the METANET simulation model for the same traf<sup>fi</sup>c state given in Tables 2 and 3. METANET has then been run <sup>fi</sup>ve times to predict the performance of the <sup>fi</sup>ve control actions $c a _ { 1 } , c a _ { 2 } , c a _ { 3 } , c a _ { 4 }$ and $c a _ { 5 }$ separately. The output shows that the METANET simulation model indicates the same ranking order for the <sup>fi</sup>ve control actions as of the proposed ITCS given in Table 9, with ca as the best global control action. This con<sup>fi</sup>rms the validity of the ITCS in predicting the performance of control actions.

The proposed ITCS is much faster in comparison with the simulation model when it is used to rank several control actions, as all training processes at the local ITC-DSS (which employs FNN-Tool) and the creation o $\dot { \cdot } C A _ { t a b l e }$ are done off-line. The simulation model, however, needs to run for each control action individually to assess the performance. For example, METANET needs about 1 min to evaluate one control action (about 5 min for the <sup>fi</sup>ve control actions), while our proposed system can evaluate and rank <sup>fi</sup>ve different traf<sup>fi</sup>c control actions in under 1 second.

It is noted that the proposed system is more manageable for a large network as the system divides it into sub-networks, each of which is

![](/api/attachments/JJ8NKGHW/fulltext/images/d1a886878082e48ae8d205343fc1dfd60f80755417e1c9138542287850056b86.jpg)  
Fig. 7. The second traf<sup>fi</sup>c scenario for the three traf<sup>fi</sup>c sub-networks.

![](/api/attachments/JJ8NKGHW/fulltext/images/783d21b4add990ef070206c222937d6b3dffa9d9a19ae4d4b37aff47886db658.jpg)  
Fig. 8. The third traf<sup>fi</sup>c scenario for the three traf<sup>fi</sup>c sub-networks.

managed by a local agent, whereas the simulation model needs to be built for a single large network. Furthermore, the proposed system uses the weights (w ), which represent the relative importance of sub-networks and can be changed on-line depending on the current traf<sup>fi</sup>c management policy and issues.

## 4. Different traf<sup>fi</sup>c scenarios

After demonstrating the technical feasibility of the proposed ITCS for identifying the best global control action, this section demonstrates the capability of the coordinated approach with different traf-<sup>fi</sup>c scenarios. Also this part of the experiment shows how the weights w play an important role for the operator in identifying the optimal global control action. In this experiment we have increased the number of control actions to ten controls and used the ITCS to predict their global performance for four different traf<sup>fi</sup>c scenarios. Table 10 shows a brief description of the ten control actions considered in this part of the experiment, while Table 11 displays $C A _ { t a b l e }$ for the King Fahad sub-network with these control actions. Since the previous section showed the application of all steps of the proposed coordinated approach, the rest of this section only discusses the <sup>fi</sup>nal results of the ITCS for each traf<sup>fi</sup>c scenario.

From Tables 10 and 11, it can be seen that control actions ca and ca are local control actions because they do not have any impact on the traf<sup>fi</sup>c state in the Olaya and Takhassusi sub-networks. Also we can observe that the average traf<sup>fi</sup>c demand $( Y _ { j } ^ { i } )$ of the Olaya sub-network is affected negatively by the control actions $c a _ { 1 } , c a _ { 2 } , c a _ { 3 } , c a _ { 4 } , c a _ { 5 } , c a _ { 6 }$ and ca , while only the control actions ca , ca and ca reduce the out<sup>fl</sup>ow capacity of the Olaya sub-network out links. On the other hand, only ca and ca have negative impacts on the average traf<sup>fi</sup>c demand (Y<sup>i</sup>) of the Takhassusi sub-network, while the out<sup>fl</sup>ow capacity of the sub-network out links are only reduced by ca and ca .

The four traf<sup>fi</sup>c scenarios considered in this experiment represent four different traf<sup>fi</sup>c states in the King Fahad, Olaya and Takhassusi sub-networks. Figs. 6–9 show the <sup>fi</sup>ve scenarios:

1) The <sup>fi</sup>rst scenario (Fig. 6) represents a smooth traf<sup>fi</sup>c state in all subnetworks (i.e. there are no traf<sup>fi</sup>c incidents in any of the subnetworks).

2) The second scenario (Fig. 7) represents a congestion traf<sup>fi</sup>c state in all sub-networks (i.e. there are traf<sup>fi</sup>c incidents in all sub-networks simultaneously).

3) The third scenario (Fig. 8) shows a traf<sup>fi</sup>c state with two simultaneous traf<sup>fi</sup>c incidents in the King Fahad and Olaya sub-networks.

4) The fourth scenario (Fig. 9) shows two simultaneous traf<sup>fi</sup>c incidents in the King Fahad and Takhassusi sub-networks.

Note that in scenarios 1 and 2, the weights (w ) will mainly affect the process of ranking the control actions, because the traf<sup>fi</sup>c state in the Olaya and the Takhassusi sub-networks are similar.

## 4.1. First scenario

Table 12 summarises the <sup>fi</sup>nal results obtained by the proposed ITCS for the <sup>fi</sup>rst scenario. Since the <sup>fi</sup>rst scenario represents a smooth traf<sup>fi</sup>c state in all sub-networks, including the King Fahad subnetwork, it is observed from Table 12 that the global aggregated performance of the control actions are almost similar to the local aggregated performance. Moreover, since the King Fahad sub-network does not have any traf<sup>fi</sup>c congestion, $c a _ { 0 }$ has high local and global performance, indicating that there is no need for applying any control action. However some control actions can cause adverse effects such as $c a _ { 4 }$ and $c a _ { 5 } .$ . Table 12 also shows that all sub-networks in this scenario have the same importance $( w _ { j } = 1 )$ . The optimal global control action in the <sup>fi</sup>rst scenario is $c a _ { 8 } ,$ because it further improves the traf<sup>fi</sup>c state of the King Fahad sub-network by opening shoulder lanes, and its side effect is not felt by the affected agents (B and C).

![](/api/attachments/JJ8NKGHW/fulltext/images/57024dbb15c2958504f3b968e84d5e20d0c8f3ccf747691ebc9332fe604f4aab.jpg)  
Fig. 9. The fourth traf<sup>fi</sup>c scenario for the three traf<sup>fi</sup>c sub-networks

Table 12  
Summary of the <sup>fi</sup>nal results of the proposed ITCS for the <sup>fi</sup>rst scenario.

<table><tr><td rowspan="3">Control action</td><td rowspan="3">Local aggregated performance (King Fahad sub-network)</td><td colspan="2">Olaya sub-network</td><td colspan="2">Takhassusi sub-network</td><td rowspan="3">Global aggregated performance</td></tr><tr><td colspan="2"> $w_B$ : 1</td><td colspan="2"> $w_C$ : 1</td></tr><tr><td>Fitness (F)</td><td>μ</td><td>Fitness (F)</td><td>μ</td></tr><tr><td> $ca_0$ </td><td>0.94</td><td>0.99</td><td>0.00</td><td>0.98</td><td>0.00</td><td>0.94</td></tr><tr><td> $ca_1$ </td><td>0.90</td><td>0.82</td><td>1.51</td><td>1.00</td><td>0.00</td><td>0.85</td></tr><tr><td> $ca_2$ </td><td>0.91</td><td>0.96</td><td>0.32</td><td>0.98</td><td>0.00</td><td>0.93</td></tr><tr><td> $ca_3$ </td><td>0.87</td><td>0.76</td><td>2.57</td><td>1.00</td><td>0.00</td><td>0.79</td></tr><tr><td> $ca_4$ </td><td>0.78</td><td>1.00</td><td>0.00</td><td>0.79</td><td>1.48</td><td>0.79</td></tr><tr><td> $ca_5$ </td><td>0.76</td><td>0.97</td><td>0.27</td><td>0.79</td><td>1.48</td><td>0.80</td></tr><tr><td> $ca_6$ </td><td>0.92</td><td>0.94</td><td>0.62</td><td>0.98</td><td>0.00</td><td>0.93</td></tr><tr><td> $ca_7$ </td><td>0.91</td><td>0.73</td><td>1.63</td><td>1.00</td><td>0.25</td><td>0.82</td></tr><tr><td> $ca_8$ </td><td>1.00</td><td>0.99</td><td>0.30</td><td>0.98</td><td>0.30</td><td>0.99</td></tr><tr><td> $ca_9$ </td><td>0.92</td><td>0.99</td><td>0.00</td><td>0.98</td><td>0.00</td><td>0.92</td></tr></table>

## 4.2. Second scenario

Table 13 demonstrates the output of the system for the second sce nario, where all sub-networks have incidents. It is observed from the table that all control actions that negatively affect a sub-network are given a low <sup>fi</sup>tness by that sub-network. This is simply because all sub-networks have traf<sup>fi</sup>c congestion and they try to avoid any more aggravation. For example, the Olaya sub-network gives the control action $c a _ { 3 }$ the lowest <sup>fi</sup>tness (0.07) because $c a _ { 3 }$ directs all traf<sup>fi</sup>c that goes to D1 and D2 to use the Olaya sub-network, while $c a _ { 4 }$ has the highest <sup>fi</sup>tness (0.69), because it does not have any negative impact. In addition, it reduces the traf<sup>fi</sup>c in<sup>fl</sup>ow to the Olaya sub-network by 8.7% (see Table 11).

Table 13  
Summary of the <sup>fi</sup>nal results of the proposed ITCS for the second scenario.

<table><tr><td rowspan="3">Control action</td><td rowspan="3">Local aggregated performance (King Fahad sub-network)</td><td colspan="2">Olaya sub-network</td><td colspan="2">Takhassusi sub-network</td><td rowspan="3">Global aggregated performance</td></tr><tr><td colspan="2"> $w_B$ : 1</td><td colspan="2"> $w_C$ : 0.5</td></tr><tr><td>Fitness (F)</td><td>μ</td><td>Fitness (F)</td><td>μ</td></tr><tr><td> $ca_0$ </td><td>0.08</td><td>0.68</td><td>0.00</td><td>0.78</td><td>0.00</td><td>0.08</td></tr><tr><td> $ca_1$ </td><td>0.78</td><td>0.24</td><td>1.51</td><td>0.82</td><td>0.00</td><td>0.46</td></tr><tr><td> $ca_2$ </td><td>0.31</td><td>0.54</td><td>0.32</td><td>0.78</td><td>0.00</td><td>0.37</td></tr><tr><td> $ca_3$ </td><td>0.87</td><td>0.07</td><td>2.57</td><td>0.82</td><td>0.00</td><td>0.29</td></tr><tr><td> $ca_4$ </td><td>0.56</td><td>0.69</td><td>0.00</td><td>0.08</td><td>1.48</td><td>0.36</td></tr><tr><td> $ca_5$ </td><td>0.82</td><td>0.56</td><td>0.27</td><td>0.08</td><td>1.48</td><td>0.51</td></tr><tr><td> $ca_6$ </td><td>0.31</td><td>0.49</td><td>0.62</td><td>0.78</td><td>0.00</td><td>0.38</td></tr><tr><td> $ca_7$ </td><td>0.78</td><td>0.24</td><td>1.63</td><td>0.82</td><td>0.25</td><td>0.46</td></tr><tr><td> $ca_8$ </td><td>0.25</td><td>0.68</td><td>0.30</td><td>0.72</td><td>0.30</td><td>0.38</td></tr><tr><td> $ca_9$ </td><td>0.20</td><td>0.68</td><td>0.00</td><td>0.78</td><td>0.00</td><td>0.20</td></tr></table>

Table 15  
Table 14  
Summary of the <sup>fi</sup>nal results of the proposed ITCS for the third scenario.

<table><tr><td rowspan="3">Control action</td><td rowspan="3">Local aggregated performance (King Fahad sub-network)</td><td colspan="2">Olaya sub-network</td><td colspan="2">Takhassusi sub-network</td><td rowspan="3">Global aggregated performance</td></tr><tr><td colspan="2"> $w_B$ : 1.0</td><td colspan="2"> $w_C$ : 1.0</td></tr><tr><td>Fitness (F)</td><td>μ</td><td>Fitness (F)</td><td>μ</td></tr><tr><td> $ca_0$ </td><td>0.08</td><td>0.66</td><td>0.00</td><td>0.98</td><td>0.00</td><td>0.08</td></tr><tr><td> $ca_1$ </td><td>0.78</td><td>0.18</td><td>1.51</td><td>1.00</td><td>0.00</td><td>0.42</td></tr><tr><td> $ca_2$ </td><td>0.31</td><td>0.49</td><td>0.32</td><td>0.98</td><td>0.00</td><td>0.35</td></tr><tr><td> $ca_3$ </td><td>0.87</td><td>0.00</td><td>2.57</td><td>1.00</td><td>0.00</td><td>0.24</td></tr><tr><td> $ca_4$ </td><td>0.56</td><td>0.65</td><td>0.00</td><td>0.79</td><td>1.48</td><td>0.70</td></tr><tr><td> $ca_5$ </td><td>0.82</td><td>0.51</td><td>0.27</td><td>0.79</td><td>1.48</td><td>0.78</td></tr><tr><td> $ca_6$ </td><td>0.31</td><td>0.43</td><td>0.62</td><td>0.98</td><td>0.00</td><td>0.36</td></tr><tr><td> $ca_7$ </td><td>0.78</td><td>0.18</td><td>1.63</td><td>1.00</td><td>0.25</td><td>0.46</td></tr><tr><td> $ca_8$ </td><td>0.25</td><td>0.64</td><td>0.30</td><td>0.98</td><td>0.30</td><td>0.46</td></tr><tr><td> $ca_9$ </td><td>0.20</td><td>0.64</td><td>0.00</td><td>0.98</td><td>0.00</td><td>0.20</td></tr></table>

In this scenario the Olaya sub-network is assigned a larger weight $( w _ { j } =$ 1) than the Takhassusi sub-network $( w _ { j } = 0 . 5 )$ , indicating the high im portance of that part of the network at that time. Thus, the output ranked list is mainly affected by the <sup>fi</sup>tness obtained from the Olaya sub-network. For example, although control action $c a _ { 3 }$ has a high local <sup>fi</sup>tness (0.87) and it is recommended by the Takhassusi sub-network (with <sup>fi</sup>tness 0.82), it has very low global performance (0.29) because it is given a very low <sup>fi</sup>tness (0.07) by the Olaya sub-network.

The optimal global control action in the second scenario is $c a _ { 5 } ,$ because it has high local performance and its negative side effects on the Olay sub-network is relatively not very high.

## 4.3. Third scenario

In the third scenario, all sub-networks are assigned the same weight $( w _ { j } = 1 )$ to show how the proposed system can recommend the optimal control action that improves the overall traf<sup>fi</sup>c state in the network. Table 14 summarises the results of the third scenario, where both the King Fahad and the Olay sub-networks have traf<sup>fi</sup>c incidents. As can be seen from Table 14, although $c a _ { 1 }$ and $c a _ { 3 }$ have a high local performance (0.78 and 0.87 respectively) to solve the traf<sup>fi</sup>c incident in the King Fahad sub-network, they have a low global performance (0.42 and 0.24 respectively) because these control actions increase the severity of the traf<sup>fi</sup>c incident in the Olaya sub-network, which does not improve the overall performance of the network. Control action ca is the optimal global control action in the third scenario, because it has high local performance and its negative side effect is relatively not very high on the Olay sub-network.

## 4.4. Fourth scenario

The fourth scenario also uses a same weight $( w _ { j } = 1 )$ for all subnetworks, as in the third scenario. The fourth scenario represents the traf<sup>fi</sup>c state where both the King Fahad and the Takhassusi sub-networks have traf<sup>fi</sup>c incidents simultaneously. The <sup>fi</sup>nal results obtained by the proposed ITCS for the fourth scenario are summarised in Table 15. The results show that $c a _ { 4 }$ and $c a _ { 5 }$ are not recommended as optimal global control actions (with 0.27 and 0.44 respectively), because they have a negative effect on the Takhassusi sub-network which does not improve the overall performance of the network. Since, the Olay sub-network has not any traf<sup>fi</sup>c problems at this time, the optimal local control action $c a _ { 3 }$ (with 0.87), which negatively affects the Olay sub-network and positively affects the Takhassusi sub-network (see Table 11), is selected by the ITCS as the optimal global control action (with 0.86).

## 5. Cross-scenario analysis

In Sections 3 and 4, <sup>fi</sup>ve different traf<sup>fi</sup>c scenarios (Figs. 5–9) were considered to represent <sup>fi</sup>ve different traf<sup>fi</sup>c states in the King Fahad, Olaya and Takhassusi sub-networks and ten traf<sup>fi</sup>c control actions with different impacts on the traf<sup>fi</sup>c state of those sub-networks were proposed. According to Tables 10 and 11 the traf<sup>fi</sup>c control actions considered in this experiment can be classi<sup>fi</sup>ed based on their impact into four groups: 1) internal control actions that do not have any impact on the traf<sup>fi</sup>c state in the Olay and Takhassusi sub-networks $( c a _ { 0 }$ and $c a _ { 9 } ) ; 2 )$ control actions that affect the traf<sup>fi</sup>c states in the Olay and Takhassusi sub-networks (ca , ca and ca ); 3) control actions that affect only the traf<sup>fi</sup>c state in the Olay sub-network $( c a _ { 1 } , c a _ { 2 } , c a _ { 3 }$ and ca ) 4) control actions that affect only the traf<sup>fi</sup>c state in the Takhassusi sub-network (ca ).

In general, the results of the traf<sup>fi</sup>c scenarios demonstrate that the global performances of the traf<sup>fi</sup>c control actions are not <sup>fi</sup>xed in all <sup>fi</sup>ve traf<sup>fi</sup>c scenarios but <sup>fl</sup>uctuate according to the traf<sup>fi</sup>c states in all sub-networks. For example, the best global traf<sup>fi</sup>c control actions in the <sup>fi</sup>rst scenario, when the traf<sup>fi</sup>c state in all sub-networks is a smooth (i.e. there are no traf<sup>fi</sup>c incidents in any of the sub-networks), are different from the best ones in the second scenario, when there is a congestion traf<sup>fi</sup>c state in all sub-networks. The global performance of each control action is in<sup>fl</sup>uenced by its local performance (King Fahad traf<sup>fi</sup>c state) and the traf<sup>fi</sup>c state in the affected sub-network(s). For example, the global performances of the control actions $c a _ { 1 } , c a _ { 2 } , c a _ { 3 }$ and $c a _ { 6 }$ are in<sup>fl</sup>uenced by their local performances and the traf<sup>fi</sup>c states in the Olay and Takhassusi sub-networks, while the global performances of the control actions $c a _ { 4 }$ is in<sup>fl</sup>uenced by its local performances and the traf<sup>fi</sup>c states in the Takhassusi subnetwork only. The global performances of the internal control actions (i.e. ca<sub>0</sub> and ca<sub>9</sub>) are only in<sup>fl</sup>uenced by King Fahad traf<sup>fi</sup>c state, so in the second, third and fourth scenarios, where King Fahad sub-network had the same traf<sup>fi</sup>c state, the global performances of those control actions were the same.

## 5.1. Local and global aggregated performances

It is observed from the analysis of the results of the <sup>fi</sup>ve traf<sup>fi</sup>c scenarios that there are two different aggregated performances for each traf<sup>fi</sup>c control action: the local aggregated performance and the global aggregated performance. The local aggregated performance of a control action represents its local impact on the King Fahad sub-network only, i.e. the <sup>fi</sup>tness of a control action, which is provided by agent A, to solve the current traf<sup>fi</sup>c congestion in the King Fahad sub-network. For calculating the local aggregated performance of a traf<sup>fi</sup>c control action, only the traf<sup>fi</sup>c state of the King Fahad sub-network is considered without taking into account any change that may happen in the traf<sup>fi</sup>c <sup>fl</sup>ow of the affected sub-networks due to the application of that traf<sup>fi</sup>c control action.

Summary of the <sup>fi</sup>nal results of the proposed ITCS for the fourth scenario.

<table><tr><td rowspan="3">Control action</td><td rowspan="3">Local aggregated performance (King Fahad sub-network)</td><td colspan="2">Olaya sub-network</td><td colspan="2">Takhassusi sub-network</td><td rowspan="3">Global aggregated performance</td></tr><tr><td colspan="2"> $w_B: 1.0$ </td><td colspan="2"> $w_C: 1.0$ </td></tr><tr><td>Fitness (F)</td><td>μ</td><td>Fitness (F)</td><td>μ</td></tr><tr><td> $ca_0$ </td><td>0.08</td><td>0.99</td><td>0.00</td><td>0.78</td><td>0.00</td><td>0.08</td></tr><tr><td> $ca_1$ </td><td>0.78</td><td>0.89</td><td>1.51</td><td>0.82</td><td>0.00</td><td>0.84</td></tr><tr><td> $ca_2$ </td><td>0.31</td><td>0.97</td><td>0.32</td><td>0.78</td><td>0.00</td><td>0.47</td></tr><tr><td> $ca_3$ </td><td>0.87</td><td>0.86</td><td>2.57</td><td>0.82</td><td>0.00</td><td>0.86</td></tr><tr><td> $ca_4$ </td><td>0.56</td><td>1.00</td><td>0.00</td><td>0.08</td><td>1.48</td><td>0.27</td></tr><tr><td> $ca_5$ </td><td>0.82</td><td>0.98</td><td>0.27</td><td>0.08</td><td>1.48</td><td>0.44</td></tr><tr><td> $ca_6$ </td><td>0.31</td><td>0.96</td><td>0.62</td><td>0.78</td><td>0.00</td><td>0.56</td></tr><tr><td> $ca_7$ </td><td>0.78</td><td>0.86</td><td>1.63</td><td>0.82</td><td>0.25</td><td>0.83</td></tr><tr><td> $ca_8$ </td><td>0.25</td><td>0.99</td><td>0.30</td><td>0.78</td><td>0.30</td><td>0.49</td></tr><tr><td> $ca_9$ </td><td>0.20</td><td>0.99</td><td>0.00</td><td>0.78</td><td>0.00</td><td>0.20</td></tr></table>

Therefore, it is observed from Tables 12–15 that the control actions with the higher local aggregated performance are the control actions that mainly reduce the traf<sup>fi</sup>c congestion severity in the King Fahad sub-network. For example, in the second scenario, the control actions $c a _ { 3 }$ and $c a _ { 5 }$ have the higher local aggregated performance (0.87 and 0.82) because they pass the most of the traf<sup>fi</sup>c in<sup>fl</sup>ow of the King Fahad subnetwork to the other subnetworks (Olaya and Takhassusi) which subsequently reduce the traf<sup>fi</sup>c congestion in the King Fahad sub-network, while the control action $c a _ { 0 }$ has the lower local aggregated performance because $c a _ { 0 }$ does improve the traf<sup>fi</sup>c state in the King Fahad subnetwork.

The global aggregated performance of a control action represents how good (or bad) the control action to solve the current traf<sup>fi</sup>c congestion in the King Fahad sub-network with taking into consideration the traf<sup>fi</sup>c state on the network level (i.e. its performance on all sub-networks). As explained in the previous sections, the traf<sup>fi</sup>c state of all affected sub-networks and the change that may happen in the traf<sup>fi</sup>c <sup>fl</sup>ow of those sub-networks due to the application of a traf<sup>fi</sup>c control are considered in the calculation of the global aggregated performance of that control action. So, it is observed from the analysis of the results of the <sup>fi</sup>ve traf<sup>fi</sup>c scenarios that the <sup>fi</sup>tness of a control action provided by the affected sub-networks in<sup>fl</sup>uences the global aggregated performance of that control action. For example, in the third scenario, when the Olay sub-network has traf<sup>fi</sup>c congestion, the Olay sub-network's <sup>fi</sup>tness of the control actions $c a _ { 1 } , \ c a _ { 3 }$ and $c a _ { 7 }$ is very low (0.18, 0.00 and 0.18 respectively), because those control actions have negative impacts on the Olay sub-network. Subsequently, the global aggregated performances of those control actions are low (0.42, 0.24 and 0.46 respectively), although their local aggregated performance are high (0.78, 0.87 and 0.78 respectively).

## 5.2. w and u<sup>i</sup> parameters

Two weighting parameters $( w _ { j }$ and $u _ { j } ^ { i } )$ are used in the calculation of the global aggregated performances of the traf<sup>fi</sup>c control actions (see Eqs. (4) and (5)). The results analysis of the <sup>fi</sup>ve traf<sup>fi</sup>c scenarios shows how these weighting parameters play an important role in ranking the control actions in each scenario. The w parameter represents the relative contribution of sub-network j to the global aggregated performances of the traf<sup>fi</sup>c control actions. For example, in the second scenar-${ \mathrm { i } } 0 ,$ when the Olaya sub-network was assigned a larger weight $( w _ { B } = 1 )$ than the Takhassusi sub-network $( w _ { C } = 0 . 5 )$ , indicating the high importance of that part of the network at that time, the contribution of the Takhassusi sub-network (i.e. the <sup>fi</sup>tness of the traf<sup>fi</sup>c control actions provided by the Takhassusi sub-network) had less impact on the global aggregated performances than the contribution of the Olaya sub-network (i.e. the <sup>fi</sup>tness of the control actions provided by the Olaya subnetwork). The $w _ { j }$ parameter has been employed in the calculation of the global aggregated performances of the control actions in the proposed coordinated approach to increase the <sup>fl</sup>exibility by allowing the operator, depending on the current traf<sup>fi</sup>c management policies and other consideration, to increase or decrease the relative importance (contribution) of a part of the network.

The u<sup>i</sup> parameter expresses how much impact the traf<sup>fi</sup>c control action $c a _ { i }$ has on the affected sub-network j. When u<sup>i</sup> is low, the global aggregated performances of control action i is meanly affected by the contribution (<sup>fi</sup>tness) of sub-network j. In contrast, when u<sup>i</sup> is high, the global aggregated performances of control action i is mainly affected by the contribution (<sup>fi</sup>tness) of sub-network j. Also, u<sup>i</sup> is used, when equals zero, to indicate irrelevant sub-networks. By using $u _ { j } ^ { i } ,$ we ensure that only the mainly affected sub-networks are considered in the identi<sup>fi</sup>cation of the global aggregated performances of the control actions. For example, since the internal control actions (ca and $c a _ { 9 } )$ do not have any impact on the Olay and Takhassusi sub-networks, the associated u<sup>i</sup> and u<sup>i</sup> are assigned zeros to disregard the contributions (<sup>fi</sup>tness) of these sub-networks in the global aggregated performances of $c a _ { 0 }$ and $c a _ { 9 } .$ While in the control actions $( c a _ { 1 } , c a _ { 2 } , c a _ { 3 }$ and $c a _ { 6 } ) ,$ , which affect only the traf<sup>fi</sup>c state in the Olay sub-network, the associated $u _ { C } ^ { i }$ are assigned zeros to only consider the contribution of the Olay sub-network, and the opposite in ca .

Based on this analysis of the results obtained from the <sup>fi</sup>ve traf<sup>fi</sup>c scenarios, it can be concluded that the proposed coordinated approach can be effectively used in ranking a number of control actions based on their global performance in different traf<sup>fi</sup>c states with different traf<sup>fi</sup>c management policies. It is observed how the proposed approach ef<sup>fi</sup>ciently consider the current traf<sup>fi</sup>c states of all parts of the network (i.e. King Fahad, Olaya and Takhassusi sub-networks) in the process of identifying the global performances of the control actions, and also how the proposed weighing parameters $( w _ { j }$ and $u _ { j } ^ { i } )$ play an effective role in this process.

We have demonstrated the applicability of the proposed system to a case study of the Riyadh traf<sup>fi</sup>c network. However, the proposed system is applicable for the potential use with the managed highway systems in other cities/networks. There is much research interest in creating system-to-system links that enable greater integration between different traf<sup>fi</sup>c sub-networks in the managed highway systems. The EU, USA and Japan are all exploring the potential of co-operative systems through a number of funded research projects. There are methods in place, such as the Urban Traf<sup>fi</sup>c Management and Control (UTMC) protocols in the UK and the Intelligent Traf<sup>fi</sup>c Systems protocols in the USA, that enable data to be shared between systems from multiple sources. In this paper we proposed the ITCS approach as a framework to scale up ITC-DSS to be used in one traf<sup>fi</sup>c control centre (e.g. one computer). Further work could be done to develop the multi-agent approach to be used at different traf<sup>fi</sup>c control centres. In this case, extensive work needs to be carried out to investigate the communications issues between control centres.

## 6. Conclusions

We have presented an Intelligent Traf<sup>fi</sup>c Control System based on a coordinated approach to assist the human operator of the road traf-<sup>fi</sup>c control centre to manage the current traf<sup>fi</sup>c state. The ITC-DSS has been extended from being used only for controlling a small-sized network to be used to control a large-sized network. We have opted for a coordinated approach where the total network was divided into a number of sub-networks, each of which has its own agent. The coordination between those agents was achieved through a high level agent called a coordinator, which receives proposed local control actions from the agent of the sub-network with regard to an incident, resolves con<sup>fl</sup>icts between other affected agents, and sends the globally acceptable solution back to that agent.

The key strength of the proposed ITCS is the use of an effective way for predicting the local performance of control actions for each subnetwork using an abstracted traf<sup>fi</sup>c data (i.e. control actions data tables) and the predicted traf<sup>fi</sup>c change of the boundary conditions. Another advantage of ITCS is the interpolation of adaptable factors (and) in the calculation of the global performance of the control actions to increase the manageability and to allow the human operators to specify the importance/preference of sub-networks for optimising the desired objectives.

In order to test the technical feasibility of the proposed ITCS, a case study of a large section of the ring-roads around Riyadh is presented and discussed. The results of ITCS have been compared with full METANET simulation model, and we found that ITCS indicates the same trend as METANET; however, ITCS is much faster than METANET. We also showed the capability of the proposed ITCS for controlling large networks through different traf<sup>fi</sup>c scenarios with different traf<sup>fi</sup>c policies. The obtained results demonstrate merits and capabilities of ITCS in order to help the operator in a traf<sup>fi</sup>c centre to identify the optimal global control actions.

The proposed ITCS approach divides a large network into a number of sub-networks to minimise the number of traf<sup>fi</sup>c variables that are required to characterise the current traf<sup>fi</sup>c (i.e. the inputs of the FNN-Tool), as well as to minimise the number of possible traf<sup>fi</sup>c control actions that can be applied to manage the traf<sup>fi</sup>c state. An investigation of an optimal way to split the network can be carried out. This should take into account some additional factors such as the topology of the network, the interrelations between the traf<sup>fi</sup>c control actions at different locations in the network, overlapping sections between subnetworks, etc. Finally, further investigation can also be carried out for the potential use of the system with the managed (and controlled) road traf<sup>fi</sup>c networks of developed countries using the same framework with local data and constraints.

## References

[1] K. Almejalli, K. Dahal, A. Hossain, Intelligent Traf<sup>fi</sup>c Control Decision Support System, Lecture Notes in Computer Science 4448 (2007) 688–701.

[2] K. Almejalli, K. Dahal, A. Hossain, An Intelligent Multi-agent Approach for Road Traf<sup>fi</sup>c Management Systems, in: the Proceedings of 18th IEEE International Conference on Control Applications (CCA), 2009.

[3] I. Arel, C. Liu, T. Urbanik, A.G. Kohls, Reinforcement learning-based multi-agent system for network traf<sup>fi</sup>c signal control, IET Intelligent Transport Systems 4 (2) (2010) 128–135.

[4] P.G. Balaji, X. German, D. Srinivasan, Urban traf<sup>fi</sup>c signal control using reinforcement learning agents, IET Intelligent Transport Systems 4 (3) (2010), pp. 177–188.

[5] K. Bogenberger, H. Keller, An Evolutionary Fuzzy System for Coordinated and Traf<sup>fi</sup>c Responsive Ramp Metering, in: the 34th Annual Hawaii International Conference on System Sciences, vol. 3, 2001, pp. 10–20.

[6] F. Daneshfar, J. RavanJamJah, F. Mansoori, H. Bevrani, B.Z. Azami, Adaptive Fuzzy Urban Traf<sup>fi</sup>c Flow Control Using a Cooperative Multi-Agent System based on Two Stage Fuzzy Clustering, in: IEEE 69th Vehicular Technology Conference, 2009, pp. 1–5.

[7] P. Desai, S.W. Loke, A. Desai, J. Singh, Multi-agent based vehicular congestion management, in: IEEE Intelligent Vehicles Symposium (IV), 2011, pp. 1031–1036

[8] A. Hegyi, et al., A Fuzzy Decision Support System for Traf<sup>fi</sup>c Control Centers, in: Proceedings IEEE Intelligent Transportation Systems, 2001, pp. 358–363.

[9] Y. Liu, G.-L. Chang, J. Yu, An integrated control model for freeway corridor under non-recurrent congestion, IEEE Transactions on Vehicular Technology 60 (4) (2011) 1404–1418.

[10] E.W.T. Ngai, T.K.P. Leung, Y.H. Wong, M.C.M. Lee, P.Y.F. Chai, Y.S. Choi, Design and development of a context-aware decision support system for real-time accident handling in logistics, Decision Support Systems 52 (4) (March 2012) 816–827.

[11] S. Ossowski, et al., Decision support for traf<sup>fi</sup>c management based on organisational and communicative multiagent abstractions, Transportation Research Part C: Emerging Technologies 13 (5-6) (2005) 272–298.

[12] C. Quek, M. Pasquier, B. Lim, POP-TRAFFIC: a novel fuzzy neural approach to road traf<sup>fi</sup>c analysis and prediction, IEEE Transactions on Intelligent Transportation Systems 7 (2) (Jun. 2006) 133–146.

[13] J.J. Ray, A web-based spatial decision support system optimizes routes for oversize/overweight vehicles in Delaware, Decision Support Systems 43 (4) (2007) 1171–1185.

[14] S.G. Ritchie, A knowledge-based decision support architecture for advanced traf-<sup>fi</sup>c management, Transportation Research Part A: General 24 (1) (1990) 27–37.

[15] Simulation-Laboratory, A. Messmer, METANET: A Simulation Program for Motorway Network, Technical University of Crete, Dynamic Systems, Jul. 2000.

[16] W. Wei, Y. Zhang, J. Mbede, Z. Zhang, J. Song, Traf<sup>fi</sup>c Signal Control Using Fuzzy Logic and MOGA, in: IEEE International Conference on Systems, Man, and Cybernetics, vol. 2, 2001, pp. 1335–1340.

[17] S.W. Yoon, J.D. Velasquez, B.K. Partridge, S.Y. Nof, Transportation security decision support system for emergency response: a training prototype, Decision Support Systems 46 (1) (December 2008) 139–148.

[18] H. Zhang, S. Ritchie, R. Jayakrishnan, Coordinated traf<sup>fi</sup>c-responsive ramp control via nonlinear state feedback, Transportation Research Part C: Emerging Technologies 9 (5) (2001) 337–352.

Dr. Keshav Dahal is a Reader (Associate Professor) in computation intelligence in the AI Research Centre at University of Bradford, UK. Prior to joining Bradford in 2002 he was a research fellow with the University of Strathclyde in Scotland, where he also obtained his PhD and MSc degrees. His research interests lie in the areas of decision support technologies, AI applications, Evolutionary computation. Dr. Dahal has extensively published in peer-reviewed journals and conferences proceeding; and edited three books published. He is a member, the Institute of Engineering Technology UK (IET), and IEEE. He has sat on the organising and programme committees of many international conferences. He has been a visiting professor to Chiang Mai University (Thailand), Kantipur Engineering College (Nepal) and Universite Lumiere Lyon 2 (France).

Dr Kahled Almejjali obtained PhD degree from the AI Research Centre at the University of Bradford in UK in 2011. He also did his masters study from the Department of Computing of the same university in 2007. Prior to his masters and PhD study he worked at the road traf<sup>fi</sup>c control department in Riyadh, Saudi Arabia. Dr. Khalid has returned back to manage the same department in Riyadh after completion of his study at the university of Bradford. His research interests lie in the areas of road traf<sup>fi</sup>c control applications, decision support systems, AI applications and software engineering.

Prof. Alamgir Hossain received the Dphil degree from the University of Shef<sup>fi</sup>eld, UK. His is a Professor of Computer Science in the School of Computing, Engineering and Information Sciences at the Northumbria University in UK. Before moving to Northumbria in 2011 he was at the University of Bradford, UK. He has extensive research experience in high performance computing, arti<sup>fi</sup>cial intelligence (AI), and system biology and adaptive control. In the past, he had joint research with companies, including Balfour Beaty Rail Goodrich Engine Design, Aramco etc, Prof, Hossain has published over 150 refereed research articles and 11 books. He received the “JEE-E C Williams" award for a research article in 1996 and the ‘Best Paper Award’ of the Computational Systems Biology conference in 2010. He is a member of the IEEE and Secretary of the CLAWAR Association.
