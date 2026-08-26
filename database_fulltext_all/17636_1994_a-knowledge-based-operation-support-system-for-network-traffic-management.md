---
otero_id: 17636
otero_key: "Z4KUR9XA"
title: "A knowledge-based operation support system for network traffic management"
authors: "Chen-Yuan Chang; Chyan-Goei Chung"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90062-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A knowledge-based operation support system for network traffic management

Chen-Yuan Chang

Telecommunications Laboratories, Chung-Li Taiwan, ROC, and National Chiao Tung University, Hsinchu, Taiwan, ROC

Chyan-Goei Chung

National Chiao Tung University, Hsinchu, Taiwan, ROC

The operation of a telephone network is subject to unexpected contingencies such as facilities impairments, trunk congestion, and focused overload. When contingencies happen in the network, the proper control actions must be taken promptly within a short period of time (e.g. 5 minutes); otherwise, the serious congestion will soon spread to the other parts of network. Until now, there has been a lack of an automated approach to generate a contingency routing plan to prevent network degradation. In this paper, a knowledge-based traffic control support system (TRACOSS) is proposed for network traffic management. TRACOSS not only contains four knowledge bases to accumulate the domain expertise used for contingencies detection, diagnosis, affected traffic estimation and control commands generation, but also contains a multicommodity network flow model to formulate the operation of telephone network. Based on this model, a heuristic algorithm is developed to design the contingency routing plan. TRACOSS has the following advantages: (1) The acceptable contingency plan can be obtained by the heuristic algorithm within the fixed time constraint. (2) Four knowledge bases can be used to accumulate the domain expertise to automate the network traffic management. (3) When new network components are installed, knowledge bases can be easily upgraded to adapt new technologies.

Keywords: Telephone network; Network traffic management; Operation support system; Multicommodity network flow model; Knowledge-based approach.

## 1. Introduction

Due to the rapid progress in Taiwan's telecommunication network construction in recent years, many types of transmission and switching facilities are provided and installed by different vendors to form a heterogeneous long distance telephone network. However, this long distance network is subject to many potential damages such as facilities impairments, trunk congestion, and focused overloads [1]. Facilities impairments mean that switching nodes or trunks malfunction because of complete or partial facility failures. Trunk congestion is a phenomenon that is caused by periodic daily increases in traffic to heavily used routes. Focused overloads are characterized by surges of traffic from many parts of the network to a single exchange or a single customer number; it is motivated by mass media advertising, accident event inquiries or natural disasters [2]. The contingencies caused by these unexpected damages will result in unwanted disturbance to the

![](/api/attachments/Z4KUR9XA/fulltext/images/e4fa90edfea4fc334daf4044127b537af3b118b946d0cda04e084b7948fe0f77.jpg)

Chen-Yuan Chang received the B.S. and the M.S. degree in Electronic Engineering from Taiwan Institute of Technology and the Ph.D. degree in Computer Science and Information Engineering from Chiao Tung University. He is currently a researcher in Telecommunication Laboratories. Taiwan, Republic of China. His research interests include network management decision support system, algorithm, software engineering and expert system.

![](/api/attachments/Z4KUR9XA/fulltext/images/f407c23d6b660e0aa45a2c74bc5dd02e6979e6ab1ae918ec44ac0b57771c2611.jpg)

Chyan-Goei Chung received the B.S. degree in Control Engineering, the M.S. degree and the Ph.D. degree in Computer Science from Chiao Tung University, Hsinchu, Taiwan. In 1969, 1974, and 1981, respectively. Since 1975 he has been with the Department of Computer Science and Information Engineering at National Chiao Tung University of Taiwan, where he is currently a professor. His research interests include software engineering, distributed system design, protocol verification, and expert system. Dr. Chung is a member of the IEEE Computer Society, and the Association for Computer Machinery.

traffic pattern of the normal network operation. If the network manager does not take proper control actions within a short period of time (e.g. 5 minutes), the serious congestion will soon spread to other parts of network.

At present, a preplanned strategy is the only way to inhibit the spread of contingencies to other parts of the network. The network manager must prepare a set of contingency routing plans for every possible situation before network contingencies occur. Under network contingencies, after the affected network components are detected and identified, the network manager then selects a contingency routing plan to rearrange the traffic flow to maximize the network throughput. With the rapid progress in telecommunication construction, the network has become more and more complex. It becomes impossible for the network manager to design the contingency routing plan manually before unpredictable contingencies occur due to the following reasons:

(1) Traffic control commands provided by different types of switching systems may differ dramatically. Upgrading of a switching system will introduce some new knowledge, which in turn affects the design of the traffic control plan.

(2) Fact knowledge of telecommunication components is constantly changing. For instance, transmission facilities constantly upgrade, e.g., from analog to digital, from copper wire to optical fiber. So do the switching systems, e.g., from analog to digital, and from cross-bar to fully electronic. The upgrading frequency is surprisingly often.

(3) Different types of network components need different domain expertise to detect the abnormal contingencies of the nodes or links identification. It is more difficult to predict all contingencies before they occur.

(4) It is always necessary to use several large-scale database to design a contingency routing plan. If the contingency plan is designed manually by the network manager, it is prone to mistakes at the time the network contingencies occur.

Until now, there has been a lack of an automated approach to detect the network contingencies and to generate a real-time contingency plan to maximize the network throughput at the time the contingencies occur. Since the knowledge to detect network contingencies heavily depends on human experts and the network management expertise, in this paper a knowledge-based traffic control support system (TRACOSS) is proposed for network traffic management. It contains not only four knowledge bases to accumulate the domain expertise used for contingencies detection, diagnosis, affected traffic estimation and control commands generation, but also a multi-commodity network flow model to formulate the operation of telephone network. Based on this model, a heuristic algorithm is developed to design the contingency routing plan. This heuristic algorithm will first find an initial solution, then, iteratively improve the solution found. When the time has expired, an acceptable contingency routing plan will be generated, providing the best solution among the earlier solutions.

In this paper, the related works of network traffic management will first be surveyed in Section 2. Then, the architecture of TRACOSS is proposed for network traffic management in Section 3. A multicommodity network flow model which is proposed to formulate the operation of telephone network is found in Section 4. In Section 5, a heuristic algorithm is developed to generate the contingency routing plan. Finally, a conclusion is given in Section 6.

## 2. Network traffic management

When the contingencies happen in a network, the proper traffic control actions must be taken promptly in a short period of time; otherwise, the serious congestion will soon spread to the other parts of network. To prevent degeneration of the network contingencies, a set of real-time surveillance and control actions must be applied to minimize network performance degradation. In general, this is defined as Network Traffic Management (NTM) [3]. Through investigating the publications in [2, 3, 4, 5, 6, 7], the complete procedure for the network traffic management is proposed as shown in Figure 1, in which the activities of each step can be summarized as follows:

## (1) Contingencies detection and identification.

The network state is changing fast. To monitor the operating conditions of the network, some instruments are used for timely detection of the status of links and nodes. These stated data can be used to indicate whether a contingency occurred. For instance, Attempts per Circuit per Hour (ACH), Connections per Circuit per Hour (CCH) and Overflow percentage (%OFL) can be used as the thresholds to determine whether the contingency is a mass calling event or a facility failure, and to pinpoint the failure locations in the network [1]. The measure data of all links or nodes must be collected and transferred to the network management center for detection of abnormal nodes and to identify failure locations.

![](/api/attachments/Z4KUR9XA/fulltext/images/112330c4965dd9aa698acd4a6401317737ed0ff8f0399e88505566d891e957f8.jpg)  
Fig. 1. Network traffic management procedure.

## (2) Traffic estimation.

Once abnormal nodes or links have been identified, the amount of remaining traffic capacity in every link and the amount of traffic demand in any node pair should be further estimated. In the normal situation, the traffic capacity in the link can be calculated by the familiar Erlang B formula [8]. However, in network contingencies, the reattempts of blocking calls may randomly increase the traffic demand on every node pair and the remaining traffic capacity of the links will become more difficult to estimate. Fortunately, Robert E. McGorman [9] proposed a methodology for designing a survivable telephone network, which can be applied to estimate the amount of traffic demand and remaining traffic capacity at the time of contingencies.

## (3) Real-time traffic routing.

After the remaining traffic capacity of every link and the real traffic demand of every node pair have been estimated, the amount of traffic flow on every route should be rearranged to inhibit the spread of congestion and to maximize the network throughput. In general, the automatic traffic controls are referred to as dynamic routing. However, we refer it to as “real-time traffic routing (RTR)” since the network conditions are changing fast and the design of these traffic control actions must be carried out in “real-time” to keep pace with changing data.

## (4) Traffic control commands generation.

Switching systems provide a set of commands to control the traffic flow of the network. The traffic control actions designed in the stage of real-time traffic routing must be transformed into a set of commands to control the traffic flow to minimize network performance degradation.

## 3. Architecture of TRACOSS

Based on the NTM procedure described above, a knowledge-based TRACOSS is proposed to automate NTM as shown in Figure 2, which is composed of the following four subsystems: (1) a real-time traffic acquisition subsystem for timely monitoring and collection of the traffic surveillance data in the switching system, (2) four knowledge bases to accumulate network management expertise, (3) an inference engine to detect network contingencies and to estimate the affected traffic, and (4) a heuristic algorithm to generate a contingency plan.

AT & T's Multifunction Operations System (MFOS) [10] can achieve timely collection of the traffic surveillance data from all switches. As it can directly be applied in Part 1 of TRACOSS to monitor the overall network view of the switch and trunk performance, Part 1 will be ignored in introducing the TRACOSS.

![](/api/attachments/Z4KUR9XA/fulltext/images/5df68d4b2f8d76968f2caf49ec5c9c9ccf5e3f2362fc9ad40a12493a1ed32e16.jpg)  
Fig. 2. The data flow diagram of TRACOSS.

Part 2 of TRACOSS contains four knowledge bases to accumulate the domain expertise. These knowledge bases are briefly introduced as follows:

(1) Contingency detection rule: Once Part 1 collects the surveillance data from the switches, the raw data must be processed to calculate the usage of the trunk group or the usage of the switch. Then, compares quantities to thresholds which are predefined by the network administrator to determine exceptions. For example, Attempts per Circuit per Hour (ACH), Connections per Circuit per Hour (CCH) and Overflow percentage (%OFL) can be used as the thresholds for detection of exceptions. When the calculated quantity exceeds the threshold, an exception condition is detected. However, the thresholds are always defined by some equations, and the expertise to compare thresholds to determine exceptions can be represented by some rules. Therefore, this knowledge base contains two parts: one defines the thresholds for exceptions detection, the other contains the rules to determine exceptions. Although many thresholds should be defined for exception detection, to make the concept clear, some of the thresholds in this knowledge base are listed below:

Seizures = Attempt Peg Count-Overflow Peg Count

%OFL = (Overflow Peg Count/Attempt Peg Count)\*100

Attempts per Circuit per Hour (ACH):

Circuits Outgoing (CO) = 1/2 number of active and maintenance busy 2-way + number of active and maintenance busy 1-way out circuits

Circuits Incoming (CI) = 1/2 number of active and maintenance busy 2-way + number of active and maintenance busy 1-way out circuits

ACH = (Attempts Peg Count \*60)/(CO\*5)

Outgoing Connections per Circuit per Hour (OCCH):

OCCH = (Seizures\*60)/(CO\*5)

Incoming Connections per Circuit per Hour (ISCH):

ISCH = (Seizures\*60)/(CI\*5)

Usage in Erlang = Usage in CCS/36

1 CCS (Hundred Call Seconds Per Hour) = Continuous Load for 100 seconds

Mean Holding Time (MHT) to the nearest tenth of a minute:

MHT = (Usage in Erlang)\*100/((Seizure + Incoming Seizures)\*60)

Based on the thresholds defined above, some rules can be used to detect network contingencies, so the other part of the knowledge base contains the rules to determine exceptions. Some of them are listed as follows:

C1: If $10 \leq OCCH \leq 15$ and $5 \leq \%OFL \leq 15$ , OK! the outgoing trunk group is in normal operation.

C2: If OCCH < 15 and ACH < 15, the trunk group is in normal operation.

C3: If 15 < OCCH ≤ 20 and 15% < \%OFL, the outgoing trunk group may have bad trunks or distance office trouble, checking Holding Time.

C4: ...

(2) Diagnostic rules: Once the contingencies were detected by the above detection rules, additional analysis is required to trouble shoot the problem and to identify the fault location. However, this expertise can be acquired from the technical manuals or experienced network managers. Although the expertise should be upgraded to adapt new network components, it can always be represented by some rules, so a rules knowledge based is used to collect this expertise. Some of the rules in this knowledge base are listed as follows:

D1: If OCCH > 60 and ACH > 60 and 0.5 < MHT ≤ 1, the first choice trunk group may be bad trunks.

D2: If OCCH > 36 and ACH > 36, but MHT <

0.4, the trunk group may be a mass calling network event.

D3: If $15 < ACH \leq 20$ and $6 < OCCH \leq 8$ and $7 < MHT \leq 8$ , this is a typical peak period calling trunk group characteristics.

D4: If 10 < ACH ≤ 15 and 10 < OCCH ≤ 15 and MHT ≤ 2.5, it indicates normal group performance with 15–20% overflow and ISCH of 9–10.

D5: ...

(3) Traffic estimation rules: When a network contingency occurs, reattempts of blocked calls will substantially increase blocking, causing the real traffic demand of each node pair, and the amount of affected traffic will become more difficult to estimate. Once a network contingency has been detected and identified, the real traffic demand of each node pair and the amount of affected traffic should be estimated by special methodologies. For example, the methodology in [9] can be applied to estimate the blocking rate and the affected traffic percentage of the failed trunk group. To adapt the new telecommunication service and technologies, these methodologies may be modified. However, they always contain some equations, which can be represented by some rules. So a rules knowledge base is proposed to represent these methodologies. Some of the rules in this knowledge base are listed as follows:

T1: If the capacity loss in a trunk group affected by a failure is F and the reattempt probability is R, then the upper limit blocking on this trunk group is $B = F / (1 - R + R * F)$ .

T2: If the affected route is a high usage route, then the actual affected traffic percentage is $HCT = (Ha-Hr)/Ha$ , where Ha is the busy hour traffic, and Hr is the overall outgoing traffic.

T3: If the mean traffic load is M, then the average efficiency of the trunk group is $E = \mathbf{M}/(\mathbf{M} + 2.33^{*}(\mathbf{M}^{**}(1/2)))$ .

T4: ...

(4) Traffic control commands: After estimating the affected traffic and applying the real-time traffic routing algorithm to obtain a contingency plan, the designed contingency plan should be transformed into a set of traffic control commands. However, the telephone network consists of multi-vendor switch products, in which each switch has different network management capabilities built into its product. For example, if the contingency is focused overload and the affected switching is 4ESS, Call Gapping command can be used to restrict the call attempts with percentages from 0 to 100 in increments of 12.5 percent. But, if the affected switching is C400, the overflow calls can only be restricted by six grades: GN25%, GN50%, GN75%, GN100%, GN + UR100% and GN + UR + SBD100%. So it is more difficult to transform the contingency plan into the appropriate actions. Fortunately, the generation of traffic control commands depends on the types of switching system and the control commands included in each switching system. Since different types of contingencies need different commands to perform traffic control actions, this knowledge base represents the expertise for control commands generation in the frame structure as shown in Figure 3, in which the relations among the types of contingencies, the types of switching system, and the traffic control commands are represented by a tree structure, and the usage of each command is represented by some rules attached to each slot.

![](/api/attachments/Z4KUR9XA/fulltext/images/7d84c605e971c0d80b4a26fc3f4d8478d04915497a32cc42bfa8315f978bb286.jpg)  
Fig. 3. A frame structure for representing traffic commands.

![](/api/attachments/Z4KUR9XA/fulltext/images/ce61b52684d8d69ff8ccbb97563db92df6cfcc65190845e4954b9f8ecf488c12.jpg)  
Fig. 4. The inference engine of TRACOSS.

According to the four knowledge bases proposed above, the inference engine of TRACOSS is designed as shown in Figure 4. The inference engine begins with detection of contingencies. Once the contingencies are detected, it then checks Diagnostic and Traffic estimation rules to diagnose network contingencies and to estimate the affected traffic. To refer the types of contingencies, the failed locations and the amount of affected traffic, Part 4 of TRACOSS then generates a contingency routing plan. Finally, based on this contingency plan, the inference engine generates a set of traffic control commands to rearrange the traffic flow of the network to maximize the network throughput.

Since the generation of traffic control commands depends on the contingency routing plan and it must be obtained within a short period of time (e.g. 5 minutes) to inhibit serious congestion spreading to other parts of network, the real-time traffic routing is a critical problem in TRACOSS. However, the real-time traffic routing is an NP-complete problem $[14]$ . The optimal contingency routing plan can not be obtained in a short period. So a multicommodity network flow model is proposed to formulate the operation of a telephone network and a heuristic algorithm is developed to find an acceptable routing plan in the next sections.

![](/api/attachments/Z4KUR9XA/fulltext/images/dece57516a85942699c8fa06abcefbe6796d220deaedcd0d6005fe42868828da.jpg)  
Fig. 5. A multicommodity flow model for telephone network.

## 4. Multicommodity Telephone Network Model

To formulate the operation of the telephone network, a multicommodity flow model [11] is proposed in the following. Let telephone network be a graph $G = (\mathbb{N}, \mathbb{L})$ as shown in Figure 5, where N is a set of nodes and L is a set of links to connect these nodes. To give an identification for each node, a set N contains n numbers defined to represent each element in the set N. N can be partitioned into two subsets $N_{t}$ and $N_{e}$ , where $N_{t}$ represents the set of nodes that are not connected to subscribers and $N_{e}$ represents the set of nodes directly connected to subscribers. For example, if there are n number of nodes in the network and k of them are end nodes which are connected with the subscribers, the end nodes are indexed as $1, 2, \ldots, k$ and the tandem nodes are indexed as $k + 1, k + 2, \ldots, n$ in the figure. N, $N_{t}$ and $N_{e}$ can be formally defined as follows:

$$
N = \{i \mid 1 \neq i \neq n, n = \text { number   of   nodes }
$$

$$
\text { in   the   network } \},\tag{4.1}
$$

$$
N _ {e} = \{i \mid 1 \leq i \leq k <   n, k = \text { number   of   nodes }
$$

$$
\text { connected   with   subscriber } \},\tag{4.2}
$$

$$
N _ {t} = \left\{i \mid k <   i \leq n \right\}.\tag{4.3}
$$

Then the links of $\mathbb{L}$ are represented by a set of $L$ defined as follows:

$$
\boldsymbol {L} = \left\{\left(i, j\right) \mid i, j \in N \right\},\tag{4.4}
$$

where $(i, j)$ represents a link from node i to node j. For each link $(i, j)$ on the long distance circuit-switched network, there are many circuits connected from node i to node j. Based on the number of circuits connected from node i to node j, the equipment traffic capacity $E_{ij}$ of link $(i, j)$ can be estimated [8,12]. In Figure 5, the equipment traffic capacity of a link is represented by a number in the arrowhead of the link.

For each end node directly connected with subscribers, there are one or more paths to connect any other end nodes so that each end node can initiate the calls to any other end node and can receive calls from any other end node. For convenient discussion, in this research a virtual original node $S_{\mu\nu}$ is used to represent the calling subscribers which initiate the call from node $\mu$ to node $\nu$ , and a virtual destination node $T_{\nu\mu}$ is used to represent the called subscribers in node $\mu$ which receives the call from node $\nu$ , where $\mu, \nu = 1, 2, \ldots, k$ and $\nu \neq \mu$ . $S_{\mu\nu}$ and $T_{\nu\mu}$ are connected to end node $\mu$ by dummy links with infinite traffic capacity. Although local calls in the end node $\mu$ can be represented as $T_{\mu\mu}$ and $S_{\mu\mu}$ , they are not included in the graph since only global network management is considered in this research.

Let $S_{\mu}$ be the set of all virtual origin nodes in the end node $\mu$ , and $T_{\nu}$ be the set of all virtual destination nodes in the end node $\nu$ , then $S_{\mu}$ and $T_{\nu}$ can be defined as follows:

$$
S _ {\mu} = \left\{S _ {\mu \nu} \mid \nu \in N _ {e}, \mu \neq \nu \right\}, \mu \in N _ {e};\tag{4.5}
$$

$$
\boldsymbol {T} _ {\nu} = \left\{T _ {\mu \nu} \mid \mu \in N _ {e}, \mu \neq \nu \right\}, \nu \in N _ {e}.\tag{4.6}
$$

If an $S_{\mu\nu}$ exists, a corresponding $T_{\mu\nu}$ must exist. Thus an origin-destination node pair is defined as $(S_{\mu\nu}, T_{\mu\nu})$ . To describe the origin-destination node pairs in the network, the set of OD is defined to represent all possible node pairs as follows:

$$
\mathbf {O D} = \left\{\left(S _ {\mu \nu}, T _ {\mu \nu}\right) \mid S _ {\mu \nu} \in S _ {\mu}, T _ {\mu \nu} \in T _ {\nu} \right\}, \mu , \nu \in N _ {e}.\tag{4.7}
$$

The number of in-chains routes between any node pair is fixed. To describe the network topology, let $n_{\mu\nu}$ represent the number of in-chain routes between node pairs $(S_{\mu\nu}, T_{\mu\nu})$ , we can define $\zeta^{\mu\nu}$ to represent the set of all in-chain routes from node $\mu$ to node $\nu$ as follows:

$$
\zeta^ {\mu \nu} = \left\{\zeta_ {m} ^ {\mu \nu} \mid 1 \leq m \leq n _ {\mu \nu} \right\},\tag{4.8}
$$

where $\zeta_{m}^{\mu\nu}$ represents the m the in-chain route from node m to node n. Usually, the number of links included in each in-chain route will not be greater than nine [13]. Let $v_{1}, v_{2}, \ldots, v_{\theta}$ represent the intermediate nodes on $\zeta_{m}^{\mu\nu}, \zeta_{m}^{\mu\nu}$ can be expressed as

$$
\begin{array}{r l} \zeta_ {m} ^ {\mu \nu} = & \Big \{\big (S _ {\mu \nu}, v _ {1} \big), (v _ {1}, v _ {2}), \ldots , (v _ {\theta - 1}, v _ {\theta}), \\ & (v _ {\theta}, T _ {\mu \nu}) | v _ {\sigma} \in N _ {t}, \\ & (v _ {\sigma - 1}, v _ {\sigma}) \in L, 1 \leq \sigma \leq \theta \Big \}. \end{array}\tag{4.9}
$$

Based on the above definitions, the topology of a telephone network can be represented by an arc-path incidence matrix A [11] as follows:

$$
A = \left[ a _ {i j} ^ {\mu \nu m} \right],\tag{4.10}
$$

where $a_{ij}^{\mu\nu m}$ represents the in-chain route $\zeta_{m}^{\mu\nu}$ passes the link $(i, j)$ or not. Each row corresponds to one in-chain route. $a_{ij}^{\mu\nu m}$ is 1 if the link $(i, j)$ is included in $\zeta_{m}^{\mu\nu}$ ; otherwise, it is 0. For example, the arc-path incidence matrix of the network in Figure 5 can be represented by the matrix shown in Table 1.

Since the traffic demand of node pair $(S_{\mu\nu}, T_{\mu\nu})$ must be delivered by its in-chain routes, the amount of traffic which flows on any in-chain route must be not less than zero and not more than the total amount of traffic demand. Let $P_{m}^{\mu\nu}$ represent the percentage of traffic demand flowing from origin node $S_{\mu\nu}$ to a destination node $T_{\mu\nu}$ through the m-th in-chain route $\zeta_{m}^{\mu\nu}, P_{m}^{\mu\nu}$ must be equal to or greater than zero and total amount of $P_{m}^{\mu\nu}$ must be less than 1, so it can obtain the following equations:

Arc-path incidence matrix for the network shown in Figure 5

<table><tr><td>Routes</td><td>Links</td></tr><tr><td></td><td>1 4 8 5 4 7 4 9 6 8 2 5 5 7 4 8 5 6 6 9 6 3 7</td></tr><tr><td></td><td>4 8 5 2 7 8 9 6 3 9 5 8 7 4 1 7 9 8 9 8 5 6 5</td></tr><tr><td> $\zeta_{1}^{12}$ </td><td>1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0</td></tr><tr><td> $\zeta_{2}^{12}$ </td><td>1 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1</td></tr><tr><td> $\zeta_{3}^{12}$ </td><td>1 0 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0</td></tr><tr><td> $\zeta_{1}^{13}$ </td><td>1 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0</td></tr><tr><td> $\zeta_{2}^{13}$ </td><td>1 1 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0</td></tr><tr><td> $\zeta_{3}^{13}$ </td><td>1 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0</td></tr><tr><td> $\zeta_{1}^{21}$ </td><td>0 0 0 0 0 0 0 0 0 0 1 0 1 1 1 0 0 0 0 0 0 0</td></tr><tr><td> $\zeta_{2}^{21}$ </td><td>0 0 0 0 0 0 0 0 0 0 1 1 0 1 1 1 0 0 0 0 0 0</td></tr><tr><td> $\zeta_{1}^{23}$ </td><td>0 0 0 0 0 0 0 1 1 0 1 0 0 0 0 0 1 0 0 0 0 0</td></tr><tr><td> $\zeta_{2}^{23}$ </td><td>0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 0</td></tr><tr><td> $\zeta_{1}^{31}$ </td><td>0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 1 0 0 0 1</td></tr><tr><td> $\zeta_{2}^{31}$ </td><td>0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 1 1 0 1</td></tr><tr><td> $\zeta_{1}^{32}$ </td><td>0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1</td></tr><tr><td> $\zeta_{2}^{32}$ </td><td>0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1</td></tr><tr><td> $\zeta_{3}^{32}$ </td><td>0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 1</td></tr></table>

$$
P _ {m} ^ {\mu \nu} \geq 0 \text {   for   any   } a _ {i j} ^ {\mu \nu m} = 1 \text {   and   } \sum_ {m = 1} ^ {n _ {\mu \nu}} P _ {m} ^ {\mu \nu} \leq 1.\tag{4.11}
$$

Let $d_{\mu\nu}$ be the amount of the real traffic demand at the time contingencies occur from $S_{\mu\nu}$ to $T_{\mu\nu}$ . The network throughput can be obtained by the following equation:

$$
\sum_{\substack{\mu ,  \nu = 1\\ \mu \neq \nu}}^{K}\sum_{m = 1}^{n_{\mu \nu}}P_{m}^{\mu \nu}d_{\mu \nu}.\tag{4.12}
$$

Since the amount of traffic flow to be controlled in each in-chain route allows specification of percentages from 0 to 100 in increments of 12.5% [1], the set P can be defined to represent the traffic flow on every in-chain route in the following:

$$
\boldsymbol {P} = \left\{\boldsymbol {P} ^ {\mu \nu} \mid \left(S _ {\mu \nu}, T _ {\mu \nu}\right) \in \mathbf {O D} \right\},\tag{4.13}
$$

where $P^{\mu \nu}$ is defined as

$$
\begin{array}{l} \boldsymbol {P} ^ {\mu \nu} = \left\{\left(P _ {1} ^ {\mu \nu}, P _ {2} ^ {\mu \nu}, \dots , P _ {m} ^ {\mu \nu}, P _ {m + 1} ^ {\mu \nu}, \dots , P _ {n _ {\mu \nu}} ^ {\mu \nu}\right) \right| \\ P _ {m} ^ {\mu \nu} = \alpha \times 12.5\%, \alpha \text { is an integer, and } \\ 0 \leq \alpha \leq 8, 1 \leq m \leq n _ {\mu \nu} \Bigg \}. \end{array} \tag{4.}\tag{4.14}
$$

The purpose of real-time traffic routing is to design a set of traffic control actions to rearrange the traffic flow of every in-chain route to minimize the network performance degradation. Since the network throughput can be defined in (4.12), the problem of real-time traffic routing can be formulated to find a set P to satisfy the following equations:

$$
\max \sum_{\substack{\mu ,\nu = 1\\ \mu \neq \nu}}^{K}\sum_{m = 1}^{n_{\mu \nu}}P_{m}^{\mu \nu}d_{\mu \nu},\tag{4.15}
$$

subject to

$$
(1) 0 <   \sum_ {m = 1} ^ {n _ {\mu \nu}} P _ {m} ^ {\mu \nu} \leq 1, \text {   for   any   } (S _ {\mu \nu}, T _ {\mu \nu}) \in \mathbf {O D}.\tag{4.16}
$$

Since $P_{m}^{\mu\nu}$ represents the amount of traffic which will flow in $\zeta_{m}^{\mu\nu}$ and it must ensure that no node pair will be completely blocked, the total of these percentages will be bound by interval $(0, 1]$ .

$$
\begin{array}{l} (2) \sum_ {\substack {\mu , \nu = 1 \\ \mu \neq \nu}} ^ {K} \sum_ {m = 1} ^ {n _ {\mu \nu}} a _ {i j} ^ {\mu \nu m} d _ {\mu \nu} P _ {m} ^ {\mu \nu} \leq C _ {i j} \\ \text {for any} (i, j) \in L. \end{array}\tag{4.17}
$$

The amount of the offered traffic from every node pair to the link $(i, j)$ can not be greater than the remaining capacity of the link $(i, j)$ estimated at the time of network contingencies.

## 5. A heuristic algorithm for real-time traffic routing

After formulating the RTR problem as the multicommodity telephone network model in the previous section, the modified simplex methods – resource-directive decomposition, price-directive decomposition, and partitioning technique [11] – can be applied to find an optimal solution. Unfortunately, several test examples in [11] show that the optimal solution can not be obtained within a short period, especially in the practical telephone network, where the number of node pairs or links is greater than 100.

![](/api/attachments/Z4KUR9XA/fulltext/images/ae704c8e130a29031e64b9f3521c39866c1a0b16a3c26b15e1c3f8ce44fd49c6.jpg)  
Fig. 6. A heuristic algorithm to generate a contingency plan.

Nevertheless, some special properties in the RTR problem still can be applied to propose a heuristic algorithm to find an acceptable solution. Although the details of this algorithm are described in another paper [16], to give an overview of TRACOSS, only the general concept of the algorithm is introduced here. Because this heuristic algorithm is designed based on the problem's special properties, the properties in the RTR problem are first listed as follows:

(1) To prevent the call looping phenomenon, only a few routes between the specific node pair are allowed to pass its traffic demand [13], and the number of the links included in the routes between any node pairs will be not greater than nine.

(2) The amount of traffic flow to be controlled in each route can allow specification of percentages from 0 to 100 in increments of 12.5 percent. For example, 4ESS can only have nine percentages such as 0%, 12.5%, 25%, 37.5%, 50%, 62.5%, 75%, 87.5%, and 100% [1].

(3) In order to avoid the contingencies spreading to other parts of the network, each node pair must pass at least 12.5% of its traffic demand. Otherwise, the calls in the related node pair will be blocked completely and the reattempted calls will add to the congestion. Therefore, each node pair should distribute at least 12.5% of its traffic demand.

(4) Each link may be shared by two or more routes of different node pairs. If route $\zeta_{A}$ has only one link shared by another route $\zeta_{B}$ on the different node pair, when we decrease some traffic flow of $\zeta_{A}$ , although that of $\zeta_{B}$ may be increased, the amount of traffic increased in $\zeta_{B}$ will not be greater than that decreased in $\zeta_{A}$ . However, if $\zeta_{A}$ has two links shared by routes $\zeta_{B}$ and $\zeta_{C}$ on two different node pairs, in which we say $\zeta_{B}$ and $\zeta_{C}$ are the related routes of $\zeta_{A}$ , decreasing traffic flow of $\zeta_{A}$ will increase that of $\zeta_{B}$ and $\zeta_{C}$ , resulting in the total amount of traffic demand passed being increased.

According to the properties described above, a heuristic algorithm is designed to generate a contingency plan as shown in Figure 6, which consists of the following procedures: (1) All in-chain routes are sorted into decreasing order by their traffic demands. (2) Each node pair is allocated a minimum amount of traffic demand. Then, the residual capacities of links are sequentially allocated to the node pairs with larger demands. (3) Sequentially rearrange the traffic allocations among the routes which share the same links to improve the cost function of the solution found. Each step is described in detail below:

## (1) Sort all in-chain routes into decreasing order by their traffic demand.

First, all node pairs are sorted into decreasing order by their traffic demand (i.e. $d_{1} \geq d_{2} \ldots \geq d_{q}$ and $d_{i}$ is the traffic demand of node pair i), and all in-chain routes in the network are reindexed as 1, 2, ..., $\chi$ so that the j-the in-chain route of node pair $\omega$ is indexed as $(n_{1} + n_{2} \ldots + n_{\omega-1} + j)$ , where q is the number of node pairs in the network, $\chi$ is the number of in-chain route in the network and $n_{\omega}$ represents the number of in-chain routes in node pair $\omega$ .

## (2) Applying first-fit decreasing strategy to find an initial GFS.

According to properties (1) and (3), few routes between any node pair are allowed to pass its traffic demand and each node pair must pass at least 12.5% of its traffic demand. So the capacities of links should be allocated to pass 12.5% of the demand of the node pair with the largest traffic demand. Then, subtract the amount of the link capacity which has been allocated and try to allocate remaining capacities of links to pass 12.5% of the demand of the node pair with the second largest traffic demand, and so on, to find a global feasible solution (GFS). If 12.5% of the traffic demand of any node pair can not be distributed, the search for a solution can be stopped because no GFS can be found in this situation; otherwise, the residual capacities of links can be further allocated to the node pair with the largest traffic demand. Then, repeat the same way to allocate the residual capacities of links to the node pair with the second largest traffic demand, and so on to find an initial GFS.

(3) Iteratively reallocate the traffic flow on the related routes to find a better GFS.

The links in the network may be shared by several different node pairs. Based on property (4), we can iteratively decrease the traffic flow on every route and then try to increase those on their related routes to improve the cost function of the initial GFS. However, the links shared by any route are fixed in the network design stage. To speed up the solution finding, we will first list the related routes of each in-chain route as a related table before contingencies occur. At the time of contingencies, we then iteratively reallocate the traffic flow on the related routes to find a better GFS until there is no route to which the traffic allocation can be reallocated.

To find an acceptable solution by the above method, the traffic flow of the failed link can be rerouted by an alternative path with more than two links. However, in the existing dynamic routing methods $[15]$ , only the two-link path can be used to reroute the failed link. Furthermore, steps 1 and 2 in the above method are simple and easy to calculate and an initial GFS can be obtained in a short period of time. Although step 3 is a time-consuming step, the related routes can be found before network operation. Based on the related routes found before, step 3 can be applied to iteratively improve the cost value of Equation (4.15). In each iteration, the newly found GFS is better than the previous one. When the time has expired, an acceptable GFS can be obtained; this will be the best solution among the GFSs found.

## 6. Conclusion

The importance of traffic management in long distance circuit-switched networks has been recognized in several research papers $[1, 2, 3, 4, 5]$ . However, the problem of network traffic management has not been thoroughly investigated and an efficient approach to solving the problem has been lacking. In this paper a knowledge-based traffic control support system (TRACOSS) is proposed to detect network contingencies and to generate a contingency plan. It contains not only four knowledge bases to accumulate the domain expertise, but also a multicommodity network flow model to formulate the operation of the telephone network. Based on this model, a heuristic algorithm is designed to generate a contingency routing plan to control the traffic flow to prevent the network degradation. The prototype of TRACOSS has been implemented and connected to Taiwan's long distance network. According to the practical operation experience, TRACOSS has the following distinguish features:

(1) The initial GFS can be first obtained in a short period of time, in which the traffic flow of the failed link can be rerouted by an alternative path with more than two links. According to the related routes found before network operation, the traffic reallocation scheme can be iteratively applied to another better GFS. In each iteration, the newly found GFS is better than the previous one. When the time has expired, an acceptable GFS is obtained to generate a set of corresponding traffic control commands.

(2) TRACOSS developed four knowledge bases to accumulate the domain expertise to automate the network traffic management. Even if the experienced manager is off duty, the network traffic management can still be operated effectively.

(3) When the new types of transmission or switching facilities are installed, the knowledge bases can be easily upgraded to adapt new technologies or components.

## Acknowledgement

The authors would like to thank Acting Director Dr. S.C. Lu of the Telecommunication Laboratories, R.O.C., and Deputy Director Dr. Jin-Tuu Wang. Further, they wish to acknowledge the substantial contributions of our co-workers: Sue-Fay Chuang, Rong-Ming Chen, Shion-Yi Yang, Shinggun Chen, and Fulin Hung. Our special thanks to Yen-Sung Lee and Mrs. Shirley Mattingly for their supports.

## References

[1] M.G. Andrews and N.S. Sanghavi, "Network traffic management in the 5ESS switch, Proceedings of International

Telecommunication Symposium, Taipei, Taiwan, R.O.C., pp. 371–376, Sep. 1988.

[2] Detlev G. Haenschke, David A. Kettler, and Eric Oberer, Network Management and Congestion in the U.S. Telecommunications Network, IEEE Transactions on Communications, Vol. Com-29, No. 4, April 1981, pp. 376–385.

[3] Don M. Tow, Network Management -- Recent Advances and Future Trends, IEEE Journal on Selected Areas in Communications, Vol. 6, No. 4, May 1988, pp. 732–741.

[4] Tatsuo Mikami and Tatsu Hirose, Introduction of the International Network Management Center -- Its Activity and System, IEEE Journal on Selected Areas in Communications, Vol. 6, No. 4, May 1988, pp. 751–759.

[5] Prosper Chemouil, Janusz Filipiak and Paul Gauthier, Analysis and Control and Traffic Routing in Circuit-Switched Networks, North-Holland Computer Networks and ISDN Systems 11 (1986) 203–217.

[6] Prosper Chemouil, Janusz Filipiak and Paul Gauthier, Performance Issues in the Design of Dynamically Controlled Circuit-Switched Networks, IEEE Communications Magazine, Oct. 1990, Vol. 28, No. 100, pp. 42.

[7] Claude Lemieux, Theory of Flow Control in Shared Networks and its Application in the Canadian Telephone Network, IEEE Transactions on Communications, Vol. Com-29, No. 4, April 1981, pp. 399-413.

[8] D.L. Jagerman, Some properties of the Erlang loss function, BSTJ, vol. 53, no. 3, March 1974.

[9] Robert E. McGorman, A Methodology for Designing Survivable Telephone Networks, IEEE International Conference on Communications, 1988.

[10] S. Daskalaki, G.D. Tsiotras, and R.C. Windecker, Network traffic management operations support for large telecommunications networks, Proceedings of International Telecommunication Symposium, Taipei, Taiwan, R.O.C., Sep. 1988, pp. 365–370.

[11] Jeff L. Kennington, A Survey of Linear Cost Multicommodity Network Flows, OPERATIONS RESEARCH Vol. 26, No. 2, March-April 1978, pp. 209–235.

[12] Roger I. Wilkinson, Theories for toll traffic engineering the U.S.A., BSTJ, March, 1956.

[13] M.T. Hills, Telecommunications Switching Principles, MIT Press, Cambridge, Massachusetts, and London, England, 1979.

[14] Michael R. Garey and David S. Johnson, Computers and Intractability, Bell Laboratories Murray Hill, New Jersey, 1979, p. 216.

[15] K. Mase and H. Yamamoto, Advanced Traffic Control Methods for Network Management, IEEE Communications Magazine. Oct. 1990, Vol. 28, No. 10, pp. 82–88.

[16] Chen-Yuang Chang and Chyan-Goei Chung, An Efficient Approach to Real-Time Traffic Routing for Telephone Network Management, has been accepted and will be published in the journal of Operation Research Society.
