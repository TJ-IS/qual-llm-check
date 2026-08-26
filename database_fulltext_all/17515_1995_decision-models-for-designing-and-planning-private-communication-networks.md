---
otero_id: 17515
otero_key: "GAZYEFFG"
title: "Decision models for designing and planning private communication networks"
authors: "Sik Choi; Abraham Seidmann; Myung W. Suh"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00048-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision models for designing and planning private communication networks

Sik Choi $^{a,*}$ , Abraham Seidmann $^{b}$ , Myung W. Suh $^{c}$

$^{a}$ School of Business Economics, Kookmin University, Seoul 136-702, Korea $^{h}$ William E. Simon Graduate School of Business Administration, University of Rochester, Rochester, NY 14627, USA $^{c}$ Department of Administrative Science, Naval Postgraduate School, Monterey, CA 93943, USA

## Abstract

We consider the recently developed reconfigurable digital data networks consisting of T1/T3 circuits and Digital Crossconnect Systems (DCSs). A DCS is a device to patch base channels electronically from one T1/T3 circuit to another with a negligible queuing delay at the connecting node. We present new decision models for the design and circuit leasing policies of such digital backbone networks. Our model takes advantage of the special capabilities of the DCS technology and is likely to result in remarkable economic gains for the private network users. The formulation and analyses presented here simultaneously address the following problems: physical link and capacity selection, logical network configuration and channel assignment, and traffic routing on the logical network. The problem formulation results in a large-scale non-linear mixed integer program, and we propose an efficient solution methodology employing Lagrangean relaxation and subgradient optimization. Several numerical results illustrate the utility of our approach for these complex problems. We show that the economies of scale built into the tariff structure of these digital networks can be successfully exploited, and that the inherent flexibility of DCSs leads to logical networks that are dramatically different from their underlying physical topologies.

Keywords: Private networks; Data networks; Communication networks; Digital crossconnect systems; Reconfigurable networks; Topology design; Decision support systems

## 1. Introduction

In a world of dynamic markets and global competition, corporations need to be highly flexible in order to capture rapidly changing opportunities. To meet this challenge, “just-in-time” partnerships of independent companies that bring their respective core competencies together to meet a specific market opportunity have emerged; partnerships of this nature are now referred to as virtual corporations. This new business model requires an efficient global telecommunication infrastructure to provide information exchange capabilities to every participant. For example, an American design firm must be able to exchange engineering drawings and specifications with an Asian manufacturer in real time and in a transparent manner. This global telecommunication infrastructure may be established either by relying on public networks or by building a private network. Public networks have largely been unable to deliver the kind of services a virtual corporation would need: that is, (a) the bandwidth of public networks is often insufficient for multimedia traffic such as engineering drawings embedded with audio/video annotations; (b) most public networks do not provide truly global connectivity. (Though telecommunication carriers have recently introduced broadband services that can support multimedia information transfer and strive to accomplish international connectivity, it will be some time before these services are widely available for production use.) Hence corporations participating in global collaborations have been forced to build and operate their own private networks.

Today's private networks are based on digital technology and employ digital circuits such as T1 and T3. A T1 is a digital circuit with a bandwidth of 1.544 Mb/s, which is equivalent to 24 DS-0 channels. (DS-0 is the baseline of the North American Digital Hierarchy and defined as 64 Kb/s.) A T3 is a digital circuit with a capacity of 44.736 Mb/s, the equivalent of 672 DS-0 channels. T1/T3 circuits are either used for point-to-point connections or, more often, interconnected via DCSs to form a T1/T3 network, with DCSs serving as the nodes of the network. A DCS is a device to patch DS-0 channels electronically from one T1/T3 circuit to another with no queuing delay; it thereby allows the bypass, broadcast, and reconfiguration of DS-0 channels.

Fig. 1 illustrates the crossconnect function of DCSs and shows how a packet-switched network is defined as a logical network over a physical network. Suppose that one needs a fully-connected packet-switched network, where each pair of packet switches is connected using a single DS-0 channel, as shown in Fig. 1(b). To create this network, one must install packet switches at the four nodes and then provide DS-0 channels to fully connect them. How many circuits are to be procured? The answer may be as few as three, not the six shown in Fig. 1(b). Consider the physical network in Fig. 1(a), which has three T1 circuits linearly connected through DCSs at nodes A and C. On this physical network, one can easily define DS-0 channels to fully connect all four packet switches. Fig. 1(c) shows how each of the needed DS-0 channels of Fig. 1(b) is defined via DCSs. For example, a DS-0 channel to link packet switches at B and C is obtained through a DCS at A that patches a DS-0 channel from the T1 circuit of AB to the T1 circuit of AC without terminating at the packet switch of node A.

One of the successful dynamic or reconfigurable networks is the ACCUNET family of digital services offered by AT and T [19]. ACCUNET services are based on DCSs like AT&T's Digital Access and Cross-Connect Systems (DACS). The ACCUNET service is a dedicated full-time digital service using T1 circuits on terrestrial facilities. For a T1 digital service using DACS with customer control capabilities named Customer Controlled Reconfiguration (CCR), the status and all interconnections of the dedicated links in the network are controlled from a customer location via a dedicated terminal [1,19,30]. Other applications of DCSs to make reconfigurable networks can be found in [17,21,30]. Siller et al. [28] describe the DCS's role in private network operation, focusing on its rapid reconfigurability.

Digital circuits such as T1 and T3 are normally leased from common carriers such as AT&T, MCI, or Bell Operating Companies, and the circuit lease costs represent the most important cost component for private networks. Network managers must strive to minimize these costs by achieving as high a utilization as possible. On the other hand, another important cost involved in telecommunication networks, often overlooked, is the users' delay cost due to traffic congestion. This cost may include an opportunity cost, the cost of lost goodwill, etc. [8]. Network designers thus tend to maintain low utilization of communication circuits by providing circuits with ample bandwidth. Network managers are faced with the tradeoff between the cost of delay and the cost of leasing added capacity for their circuits. Finding the optimal tradeoff point between these two cost components is an important decision problem and has been addressed in several papers [15,20,25,29].

![](/api/attachments/GAZYEFFG/fulltext/images/787182ea3d51860124677be45a2fb80030c8876e728b456326279e160d90967c.jpg)  
(a)

![](/api/attachments/GAZYEFFG/fulltext/images/c3730a823aab0abd7f63b8b5be818b0443c7bd8c96ce38e1f22cf7b38a0b0e78.jpg)  
(b)

Fig. 1. Physical network vs. logical network.  
![](/api/attachments/GAZYEFFG/fulltext/images/50f6f858b70ea73a1e801a95ad5f8f2d0965024dd600779994756abed58364f9.jpg)

Our paper extends previous studies by viewing modern data networks, such as packet-switched networks, as logical networks over a reconfigurable private network of T1/T3 circuits. Traditional topology design $[2,5,16,27]$ and capacity and flow assignment $[15,25,26]$ studies solve a static network case, ignoring the reconfigurability of private networks. This reconfigurability based on DCSs implies that the capacity of a link between a pair of packet switches – in terms of the number of DS-0 channels – can be expanded without leasing additional circuits to meet increased traffic volume on that link. Traditional topological design problems determine the minimum cost topology of a network, with the capacities of candidate links given and fixed. Capacity and flow assignment problems strive to determine the link capacities and the routing policy in an optimal way. Following the link costs used by those studies will overlook the fact that the bandwidths in our T1/T3 networks are bought in bulk (i.e., in the form of batches of T1s or T3s) and the marginal cost of link capacity is thus sometimes zero. Thus using traditional topological design or capacity and flow assignment studies for DCS networks will result in sub-optimal performance.

Several papers have also been published on the design of reconfigurable networks. Monteiro and Gerla [23] address the topological reconfiguration of an Asynchronous Transfer Mode (ATM) network embedded in a backbone facility network using DCSs. They conclude that reconfigurability substantially reduces traffic congestion. Doverspike and Jha [9] use data from Bellcore to show that network capacity can be reduced by 14% using reconfigurable DCS networks as compared with conventional hierarchical routing. Lee and Yee [22] solve the joint optimization of the logical network topology design and capacity assignment problems for reconfigurable data networks. By minimizing the average delay of a packet, they model this problem using non-linear integer programming. These papers, however, assume that the physical topology and the link capacities are given. Chari and Dutta [3,4] model the private backbone network design problem without exploiting the economies of scale in the lease cost structure of digital circuits.

Our paper is the first to integrate the topological design and physical link capacity allocation problems with traffic routing for a reconfigurable network. This integration takes advantage of the special capabilities of the recently developed DCS technologies and is likely to result in remarkable economic savings for the users. Our model also captures the predominant features of this technology: we explicitly acknowledge that the capacity of the physical links is discrete in the multiple of 24 DS-0 channels (one T1), and that there are economies of scale in leasing T1 or T3 circuits. Modelling the details of these decision problems leads to a large-scale mixed integer program. We provide a novel Lagrangean relaxation method for computing lower bounds and heuristics leading to feasible solutions which are very close to optimal.

The next section provides a formulation for the decision model and outlines the solution procedure. Section 3 presents the results of several numerical experiments. The final section offers a summary and concluding analysis.

## 2. Formulation of the decision model

The decision model presented in this section determines the topology of a private network of T1/T3 circuits – the physical network – and the type (or quantity) of circuits (e.g., null, one T1, two T1s, etc.) for each of the network's candidate links. A “null” implies that the network topology will not include this physical link.

The decision model also determines the configuration of the logical network along with the number of DS-0 channels to be used for linking each pair of packet switches in the logical network. Conceptually, the logical network operates like a conventional packet-switched network, so the traffic routing of all O-D pairs must be defined on it. Our model provides the traffic routing on the logical network as well. Our paper simultaneously formulates and then solves the following subproblems:

\- the physical link and capacity selection of the physical network;

\- the logical network configuration and channel assignment;

\- the traffic routing on the logical network.

The objective is to minimize the combined lease and queuing delay costs; similar objective functions were used by $[15,25]$ .

## 2.1. Notations and assumptions

The set of locations where DCSs and packet switches are collocated is given a priori. A user accesses a packet switch at one of these locations for long-haul packet-switched data communication. All origin-destination (O-D) pairs are given, along with their traffic requirements (in packets per second). Following $[5,13,22,23,26]$ , we assume that traffic requirements for all O-D pairs follow a Poisson arrival process with known arrival rates.

N denotes the set of nodes and P the set of candidate links for the physical network, or the physical link set; each physical link consists of T1 or T3 circuits. L represents the set of candidate links for the logical network, or the logical link set.

![](/api/attachments/GAZYEFFG/fulltext/images/451dc12cadf215415fefff6d683b37624b39815521e86e3ec7bc0b8c39b39e34.jpg)  
(a) Physical Network

To facilitate subsequent discussion, an example of a 5-node physical network and its logical network is provided in Fig. 2. Fig. 2(a) shows a set of six physical candidate links, arbitrarily selected from a complete set of ten possible links. Fig. 2(b) shows a set of ten logical links. Each logical link consists of one or more DS-0 channel(s).

A c-sequence is defined as a sequence of physical links crossconnected via DCSs to provide a logical link. We use two kinds of sets for the c-sequences. $C_{l}^{L}$ is defined as the set of c-sequences that provide logical link $l \in L$ . For example, the logical link AC in Fig. 2(b) can be obtained by a set of different c-sequences (denoted by $C_{AC}^{L}$ ), {ABC, AEDC, AEBC, ABEDC} on the physical network of Fig. 2(a). The capacity of a logical link is determined by the number of DS-0 channels assigned for that logical link along its c-sequences. $C_{p}^{P}$ is defined as the set of c-sequences that use physical link $p \in P$ . For example $C_{AB}^{P}$ is defined as a set of c-sequences, {AB, ABC, ABEDC, ABCD, ABED, ABCDE, BAEDC, BAED, BAE, CBAED, CBAE, DCBAE}.

An l-route is a simple route (path) on the logical network that carries packet-switched traffic for a certain O-D pair. We use two kinds of sets for the l-routes. $R_{s}^{S}$ is defined as the set of candidate l-routes for O-D pair $s \in S$ . For example, in Fig. 2(b), the set of l-routes for the O-D pair A and C (denoted by $R_{AC}^{S}$ ) is {AC, ABC, ADC, AEC, ABDC, ABEC, ADBC,

![](/api/attachments/GAZYEFFG/fulltext/images/2f0e0daa3c63dd12ab28bb7c79349be736d44b62bafa40361a57190375488ae1.jpg)  
Fig. 2. A sample network of five nodes.  
(b) Logical Network

ADEC, AEBC, AEDC, ABEDC, ABDEC, ADBEC, ADEBC, AEBDC, AEDBC}. $R_{l}^{L}$ is defined as the set of l-routes that use $l \in L$ . For example, $R_{AB}^{L} = \{AB, BAC, ABDC, ABEC, ABD, ABCD, ABED, ABE, ABCE, ABDE, BAC, BADC, BAEC, BAD, BACD, BAED, BAE, BACE, BADE, CABD, CBAD, CABE, CBAE, DABE, DBAE\}$ .

Other index sets and parameters used in the model are the following:

$T_{p}$ : the set of possible circuit types for physical link $p \in P$ , i.e., {T1, T3} and an integral number of each circuit;

$K_{pt}$ : the cost of leasing circuit type $t \in T_p$ to link $p \in P$ (\$/month);

S: the set of all O-D pairs;

$W_{s}$ : average traffic arrival rate on O-D pair $s \in S$ (packets/sec);

$M_{pt}$ : the number of DS-0 channels in circuit type $t \in T_p$ for physical link $p \in P$ ;

C: the set of all possible c-sequences.

The cost of leasing a particular circuit of type $t \in T_p$ , $K_{pt}$ , depends on distance. For example, according to AT&T Tariff No. 9 [11], the lease rate for one T1 circuit consists of a fixed charge of \$2,600 and about \$15 per mile per month. For T3 circuits, there is a fixed charge of \$6,000 per month and a mileage charge based on airline miles between cities. The mileage charge for a T3 varies from \$180 per month for a one-year contract to \$130 per month for five years. The economies of scale are evident in the tariff structure for digital circuits, as shown in Fig. 3. For example, the cost of a T3 circuit is comparable with the cost of as few as four T1 circuits for a distance of less than 50 miles, i.e., much cheaper than 28 T1s, the equivalent of one T3 in capacity. The set $T_p$ also depends on the length of physical link $p$ . If the length of the physical link $p$ is 500 miles, the economic set is defined as {1 T1, 2 T1s, 3 T1s, 4 T1s, 5 T1, 6 T1, 7 T1, 8 T1s, 9 T1s, 1 T3}, since the cost of 10 T1s is higher than 1 T3, while 1 T3 has much more capacity. If the distance is 100 miles, the economic set is defined as {1 T1, 2 T1s, 3 T1s, 4 T1s, 5 T1, 1 T3}. Other examples of this notation can be found in the section on numerical results.

To summarize, our decision variables are:

physical link and capacity selection:

$y_{pt}$ , which is defined as 1 if circuit type $t \in T_{p}$ is leased to link $p \in P$ and 0 otherwise (e.g., $y_{AB} = 1$ if the link AB is chosen for the physical network);

\- logical network configuration and channel assignment:

$n_{c}$ , the number of DS-0 channels assigned along c-sequence $c \in C$ (e.g., $n_{ABC} = 50$ if 50 DS-0 channels are assigned to c-sequence ABC, which supports the logical link AC);

![](/api/attachments/GAZYEFFG/fulltext/images/713984f9f40b291992087823313fdcf9afba545653db0b71cdfb069891efdf04.jpg)  
Fig. 3. Break-even point between T1 and T3 circuits.

\- traffic routing on the logical network: $x_r$ , the packet (flow) rate on $l$ -route $r \in R_s^S$ , $s \in S$ (packets/sec) (e.g., $x_{ABD} = 500$ if the traffic rate through the logical route $ABD$ for O-D pair $AD$ is 500 packets per second).

## 2.2. Mathematical formulation

The formulation of the decision model is as follows:

Problem (P)

$$
Z _ {P} = \min \left\{D \sum_ {l \in L} \frac {q _ {l} f _ {l}}{Q q _ {l} - f _ {l}} + \sum_ {p \in P} \sum_ {t \in T p} K _ {p t} y _ {p t} \right\}\tag{1}
$$

subject to:

$$
\sum_ {r \in R _ {s} ^ {S}} x _ {r} = W _ {s} \forall s \in S\tag{2}
$$

$$
\sum_ {t \in T _ {p}} y _ {p t} \leq 1 \forall p \in P\tag{3}
$$

$$
\sum_ {c \in C _ {p} ^ {P}} n _ {c} \leq \sum_ {t \in T _ {p}} M _ {p t Y p t} \forall p \in P\tag{4}
$$

$$
\sum_ {r \in R _ {l} ^ {L}} x _ {r} = f _ {l} \forall l \in L\tag{5}
$$

$$
\sum_ {c \in C _ {l} ^ {L}} n _ {c} = q _ {l} \forall l \in L\tag{6}
$$

$$
y _ {p t} \in \{0, 1 \} \forall p \in P, \forall t \in T _ {p}\tag{7}
$$

$$
n _ {c} = 0, 1, 2, 3 \dots \forall c \in C\tag{8}
$$

$$
x _ {r} \geq 0 \forall r \in R _ {s} ^ {S}, \forall s \in S\tag{9}
$$

Eq. (2) verifies that the sum of traffic flows over all the l-routes for a specific O-D pair is equal to the traffic requirements for that O-D pair. Eq. (3) indicates that at most one circuit type can be assigned to each candidate physical link. Note that the inequality implies that some of the candidate physical links may not be chosen in the optimal solution. The constraints in (4) guarantee that the sum of the number of DS-0 channels over all c-sequences that use physical link p $\in P$ must be less than or equal to the capacity of physical link p. No c-sequence can use a physical link to which a null circuit is assigned. Eq. (5) defines the aggregate flows on logical link $l(f_{l})$ by summing all traffic flows over all l-routes that use logical link l, and (6) defines the total number of DS-0 channels assigned to logical link $l(q_{l})$ by summing the number of channels over the c-sequences that comprise the logical link l. The variables $f_{l}$ and $q_{l}$ are intermediate quantities introduced for convenience in notation and computation. The remaining constraints are integrality and a nonnegativity constraint for each variable.

The objective function consists of two terms: a delay cost term and a lease cost term. We assume that the packet transmission time is exponentially distributed with a mean of Q packets/sec. Q is arbitrarily set to 64 packets per second by assuming the average packet size is 1000 bits (the capacity of one DS-0 channel is 64 Kbps). Packets are randomly routed with equal probability over any one of the channels connecting two nodes on this logical link. Thus the packet arrival rate on each channel is $f_l / q_l$ , since $f_l$ is the aggregate flow on logical link $l$ . We also assume Kleinrock's independence assumption so that packet transmission times on each link along the transmission path are independent. The resulting network is a queuing network with independent $M / M / 1$ queues. If $Qq_l - f_l > 0$ , then the average number of packets waiting and being transmitted on each channel on logical link $l$ is $\{f_l\} / \{Qq_l - f_l\}$ , and the average total number of packets waiting on $l$ is $\{q_l f_l\} / \{Qq_l - f_l\}$ . The constraint $Qq_l - f_l > 0$ for each logical link can be omitted; this term never approaches zero or negative values once we start solving this problem with a feasible solution. Employing Little's formula, the expected delay per packet on the network is

$$
\frac {1}{\sum s \in S W _ {s}} \sum_ {l \in L} \frac {q _ {l} f _ {l}}{Q q _ {l} - f _ {l}}\tag{10}
$$

This delay cost occurs for every packet all day for all O-D pairs. Since we use monthly leasing rates for the T1/T3, we must also use monthly sums for the queuing delay costs; however, assuming a time horizon of one month, the unit delay cost would be very large. To simplify this objective function, we let D = unit delay cost $\Sigma_{s \in S} W_{s}$ ; a similar delay function has been used in recent papers by [22,26].

![](/api/attachments/GAZYEFFG/fulltext/images/694ac14efabf2ded295bbef04bf8d2a8adee236ff192d76d47236efc954491a2.jpg)  
Fig. 4. Flow chart of the solution procedure.

## 2.3. Solution procedure

The solution procedure for problem (P) is based on the Lagrangean relaxation and subgradient optimization method. Our solution procedure finds both the near-optimal feasible solution and a lower bound of the solution. By providing a lower bound, we can prove the quality of the feasible solution.

Fig. 4 shows the flow chart of the solution procedure. We begin by creating the input files for the model: distance between nodes, traffic requirements between all O-D pairs, and the candidate topology of the physical network. At this stage, we also determine the economic break-even point for using T1s or a T3, and calculate the cost of leasing possible line types ( $K_{pt}$ ) and the capacity of each line type ( $M_{pt}$ ).

The c-sequences and l-routes for each O-D pair must also be given as input data. Since the number of all possible c-sequences and l-routes increases with the network size, a preprocessing step for generating all c-sequences and l-routes is required.

Next, we use a Lagrangean relaxation approach to relax the physical capacity constraints (4) and divide the original formulation into two subproblems which are easier to solve. We solve these subproblems using greedy search and another newly developed algorithms based on the theorems we presented earlier [6]. The objective value of the relaxed problem sets a lower bound on the optimal solution and provides a measure of quality for the solution. The relaxed problem is solved iteratively by the subgradient optimization technique until the solution reaches a predetermined threshold; a feasible solution is obtained by perturbing the solution of each iteration of the subgradient optimization procedure. The final solution provides the topology of the physical network, the configuration and channel assignments of the logical network, and traffic routing on the logical network. We then compute other performance statistics, such as average delay per packet, queuing and lease cost, utilization of logical links, and upper and lower bound of the solution. Details of the solution procedure can be found in [6,7].

## 3. Numerical experiments

In this section, we apply the decision model to several test cases in order to illustrate how a private network is designed under various scenarios and investigate the performance of the proposed solution procedure. Two groups of test cases are used: one group involves five cities and the other group ten cities, and the cities have been arbitrarily chosen from across the United States. Each of these cities serves as a node for the private network to be designed and thus hosts both a DCS and a packet switch.

The capacity of line type t if used for link p. $M_{pt}$ in number of DS-0 channels

<table><tr><td>p\t</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td></tr><tr><td>(1,2)</td><td>24</td><td>48</td><td>72</td><td>96</td><td>120</td><td>144</td><td>168</td><td>192</td><td>216</td><td>240</td><td>672 *</td><td>-</td></tr><tr><td>(1,5)</td><td>24</td><td>48</td><td>72</td><td>96</td><td>120</td><td>144</td><td>168</td><td>192</td><td>216</td><td>240</td><td>264</td><td>672</td></tr><tr><td>(2,3)</td><td>24</td><td>48</td><td>72</td><td>96</td><td>120</td><td>144</td><td>168</td><td>192</td><td>216</td><td>240</td><td>264</td><td>672</td></tr><tr><td>(2,5)</td><td>24</td><td>48</td><td>72</td><td>96</td><td>120</td><td>144</td><td>168</td><td>192</td><td>216</td><td>240</td><td>672 *</td><td></td></tr><tr><td>(3,4)</td><td>24</td><td>48</td><td>72</td><td>96</td><td>120</td><td>144</td><td>168</td><td>192</td><td>216</td><td>672 *</td><td>-</td><td>-</td></tr><tr><td>(4,5)</td><td>24</td><td>48</td><td>72</td><td>96</td><td>120</td><td>144</td><td>168</td><td>192</td><td>216</td><td>240</td><td>264</td><td>672 *</td></tr></table>

\* Number of DS-0 channels of one T3 circuit link p.

Table 2  
The monthly cost of leasing a type t line if used for link p, $K_{pt}$ in \$/month

<table><tr><td>p\t</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td></tr><tr><td>(1,2)</td><td>14735</td><td>29470</td><td>44205</td><td>58940</td><td>73675</td><td>88410</td><td>103145</td><td>117880</td><td>132615</td><td>147350</td><td>151620 *</td><td>-</td></tr><tr><td>(1,5)</td><td>26750</td><td>53500</td><td>80250</td><td>107000</td><td>133750</td><td>160500</td><td>187250</td><td>214000</td><td>240750</td><td>267500</td><td>294250</td><td>295800 *</td></tr><tr><td>(2,3)</td><td>35195</td><td>70390</td><td>105585</td><td>140780</td><td>175975</td><td>211170</td><td>246365</td><td>281560</td><td>316755</td><td>351950</td><td>387145</td><td>397140 *</td></tr><tr><td>(2,5)</td><td>18950</td><td>37930</td><td>56895</td><td>75860</td><td>94825</td><td>113790</td><td>132755</td><td>151720</td><td>170685</td><td>189650</td><td>202380 *</td><td></td></tr><tr><td>(3,4)</td><td>8405</td><td>168150</td><td>25215</td><td>33620</td><td>42025</td><td>50430</td><td>58835</td><td>67240</td><td>75645</td><td>75660 *</td><td>-</td><td>-</td></tr><tr><td>(4,5)</td><td>25715</td><td>51430</td><td>77145</td><td>102860</td><td>128575</td><td>154290</td><td>180005</td><td>205720</td><td>231435</td><td>257150</td><td>282865</td><td>283380 *</td></tr></table>

\* Cost of leasing one T3 circuit for link p

![](/api/attachments/GAZYEFFG/fulltext/images/8fd17334bc8a37181800a514be87b042d3c81a968594bc8c9089c4542ac1c974.jpg)  
Fig. 5. The five-node network structure. The numbers indicate the distance in miles.

## 3.1. Five-node test cases

The locations for the five cities selected and the candidate physical links are shown in Fig. 5. The length of each of the candidate physical links, as measured in airline mileage, is also shown. (The five cities in Fig. 5 represent New York, Chicago, San Francisco, Los Angeles, and Houston.)

The parameters $K_{pt}$ , the lease cost of using link type t per month for the physical link p, are calculated in Table 2, based on the tariff structure presented in Fig. 3. The parameters $M_{pt}$ , the capacity in units of the number of DS-0 channels of line type t for physical link p, are also presented in Table 1. The row and column headings of these tables represent the physical link set and the line types for a given physical link.

Table 2 shows that the cost of a single T3 circuit is comparable to the cost of 10 to 12 T1 circuits, depending on the distance between nodes. For example, consider link $p = (1,2)$ , with a length of 809 miles. The monthly rate for leasing 6 T1s is \$88,410 per month. This table also shows that the cost of leasing 11 T1 circuits for physical link $(1,2)$ is higher than the cost of leasing a single T3 circuit. (The cost of leasing 11 T1s for link $(1,2) = (2600 + 15 \times 809) \times 11 = \$162,085$ , and the cost of leasing 1 T3 = $6000 + 180 \times 809 = \$151,620$ . Hence, the lease of 1 T3 is cheaper than that of 11 T1s.) Yet a single T3 provides significantly more capacity, so the network design algorithm is expected to exploit the economies of scale by using a T3 circuit that brings extra capacity for other crossconnections with no additional cost. Table 2 shows that the economic break-even points for using a T3 for physical links $(1,2)$ , $(1,5)$ , $(2,3)$ , $(2,5)$ , $(3,4)$ , and $(4,5)$ are 11, 12, 12, 11, 10, and 12 T1 circuits, respectively.

Given the five-node setting, different test cases were created by varying either the level of traffic volumes between cities or the delay cost parameter (D). We started with D = 1500 and varied the volume of traffic as shown in Table 3, which shows the arbitrary O-D pair traffic data for three different cases. For example, the traffic requirement for O-D pair (2,5) for case 2 is 3500 packets/sec. Case 1 shows evenly high traffic volumes between all O-D pairs. Case 2 traffic shows an uneven pattern; i.e., the first five have a low volume traffic and the latter five pairs have a high volume. Case 3 has a low volume of traffic throughout the network. We used these traffic patterns to explore their impact on the resulting topology and channel assignment and the robustness of our solution procedure.

Table 3  
Traffic requirement for each O-D pair (packets/sec)

<table><tr><td>O-D</td><td>(1,2)</td><td>(1,3)</td><td>(1,4)</td><td>(1,5)</td><td>(2,3)</td><td>(2,4)</td><td>(2,5)</td><td>(3,4)</td><td>(3,5)</td><td>(4,5)</td></tr><tr><td>case 1</td><td>3000</td><td>4000</td><td>3500</td><td>3000</td><td>4000</td><td>5000</td><td>3500</td><td>4000</td><td>4500</td><td>3500</td></tr><tr><td>case 2</td><td>300</td><td>400</td><td>350</td><td>300</td><td>400</td><td>5000</td><td>3500</td><td>4000</td><td>4500</td><td>3500</td></tr><tr><td>case 3</td><td>600</td><td>800</td><td>700</td><td>600</td><td>800</td><td>1000</td><td>700</td><td>800</td><td>900</td><td>700</td></tr></table>

![](/api/attachments/GAZYEFFG/fulltext/images/211078a2db678205307015010fd5ab2f29c99e737e16d644f278eccd910d57cb.jpg)  
Fig. 6. Physical network designs for the three traffic volume scenarios.

The solution for each case is shown in Fig. 6. In case 1, all candidate links except link (1,5) are selected. Four of the selected physical links are given single T3 circuits and one is given five T1s. Although T3 circuits seem to have excess capacity, they provide the least expensive configuration due to the economies of scale built into the cost structure for T1 and T3 circuits. In case 2, only four of the six candidate physical links are selected. Physical links (3,4), (4,5), and (2,5) consist of single T3 circuits, and physical link (1,2) is assigned two T1 circuits. Finally, in case 3, all candidate links are selected, and each is assigned one to five T1 circuits. In this case, traffic volumes are too low to justify the cost of a T3 circuit.

The crossconnect sequences and the number of channels assigned for each logical link in the best solutions are summarized in Table 4; these actually define the logical network. The logical networks in these cases are fully connected networks similar to Fig. 2(b) with the capacities shown in this table. Note that the physical networks shown in Fig. 6 are totally different from their logical networks. In case 1, for example, the O-D traffic between nodes 1 and 4 uses physical links (1,2), (2,3), and (3,4) to make a crossconnect sequence and is supported by 111 DS-0 channels. The total number of channels used by crossconnections should approach but cannot exceed the maximum capacity of the physical links. For example, physical link (2,3) has a capacity of 672 DS-0 channels, and only 128 channels are assigned to the direct logical link (2,3). The other 544 channels are assigned to logical links (1,3), (1,4), (2,4), and (3,5) by crossconnection. The crossconnections shown in the table do not always take the shortest physical path. For example, logical link (3,5) in case 1 uses physical links (3,2) and (2,5) even though the shortest path consists of physical links (3,4) and (4,5). Selecting a longer path can reduce total lease costs by exploiting the economies of scale through using the larger capacity of a T3. The packet routing on the logical network is always determined by selecting the single-link l-route path from the logical network, as proved by [6,7].

Logical links, their crossconnect circuits, and number of DS-0 channels assigned

<table><tr><td></td><td>logical links</td><td>(1,2)</td><td>(1,3)</td><td>(1,4)</td><td>(1,5)</td><td>(2,3)</td><td>(2,4)</td><td>(2,5)</td><td>(3,4)</td><td>(3,5)</td><td>(4,5)</td></tr><tr><td rowspan="2">case 1</td><td rowspan="2">Cross-connection# of channels</td><td>(1,2)</td><td>(1,2,3)</td><td>(1,2,3,4)</td><td>(1,2,5)</td><td>(2,3)</td><td>(2,3,4)</td><td>(2,5)</td><td>(3,4)</td><td>(3,2,5)</td><td>(4,5)</td></tr><tr><td>235</td><td>128</td><td>111</td><td>198</td><td>128</td><td>161</td><td>330</td><td>400</td><td>144</td><td>120</td></tr><tr><td rowspan="2">case 2</td><td rowspan="2">Cross-connection# of channels</td><td>(1,2)</td><td>(1,2,5,4,3)</td><td>(1,2,5,4)</td><td>(1,2,5)</td><td>(2,5,4,3)</td><td>(2,5,4)</td><td>(2,5)</td><td>(3,4)</td><td>(3,4,5)</td><td>(4,5)</td></tr><tr><td>10</td><td>13</td><td>12</td><td>10</td><td>19</td><td>242</td><td>279</td><td>334</td><td>217</td><td>169</td></tr><tr><td rowspan="2">case 3</td><td rowspan="2">Cross-connection# of channels</td><td>(1,2)</td><td>(1,2,3)</td><td>(1,5,4)</td><td>(1,5)</td><td>(2,3)</td><td>(2,3,4)</td><td>(2,5)</td><td>(3,4)</td><td>(3,4,5)</td><td>(4,5)</td></tr><tr><td>29</td><td>23</td><td>20</td><td>24</td><td>24</td><td>29</td><td>24</td><td>44</td><td>27</td><td>21</td></tr></table>

![](/api/attachments/GAZYEFFG/fulltext/images/762e48ae088cd145b6e47a8d80ebb1a2661693be7289b41acceb1c608e374ff4.jpg)  
Fig. 7. Physical network designs with various delay costs.

To analyze the effect of different delay cost values on network design, we varied the value of D from 1000 to 4000 with an increment of 500. The traffic pattern follows that of case 1 above. Fig. 7 shows the network designs for the seven values of D. Obviously, as the users' delay cost increases, more candidate physical links are selected and more T3 circuits are used. When D =

4000, the delay cost dominates the lease cost, and therefore all candidate physical links are selected and assigned T3 circuits in order to keep the delay cost as low as possible. On the other hand, when D = 1000, the lease cost is the dominant cost component, and the best solution is one that achieves high circuit utilization.

Table 5 summarizes the performance of our solution procedure as well as some results found in the best solutions. It shows the lower and upper bounds for the optimal solutions, the relative gap between the two bounds [defined as (upper bound - lower bound)/upper bound], the average delay per packet in seconds, and the average utilization of the logical links. The cost term is separated into two parts: queuing cost and lease cost.

Table 5  
Numerical results for five-node example

<table><tr><td> $D^a$ </td><td>Upper bound</td><td>Lower bound</td><td> $Gap^b$ </td><td>Queuing Cost</td><td>Lease cost</td><td>Avg delay/packet  $^c$ </td><td>Avg util  $^d$ </td></tr><tr><td>1000</td><td>1918319</td><td>1731218</td><td>0.097</td><td>1205279</td><td>713040</td><td>0.032</td><td>0.46</td></tr><tr><td>1500</td><td>2464305</td><td>2209467</td><td>0.103</td><td>1508930</td><td>955375</td><td>0.026</td><td>0.37</td></tr><tr><td>2000</td><td>2894552</td><td>2660409</td><td>0.081</td><td>1784372</td><td>1110180</td><td>0.023</td><td>0.33</td></tr><tr><td>2500</td><td>3340745</td><td>3095150</td><td>0.073</td><td>2230468</td><td>1110180</td><td>0.023</td><td>0.33</td></tr><tr><td>3000</td><td>3735013</td><td>3519218</td><td>0.058</td><td>2531413</td><td>1203600</td><td>0.022</td><td>0.29</td></tr><tr><td>3500</td><td>4102190</td><td>3937017</td><td>0.040</td><td>2898590</td><td>1203600</td><td>0.022</td><td>0.27</td></tr><tr><td>4000</td><td>4635052</td><td>4350129</td><td>0.061</td><td>3229073</td><td>1405980</td><td>0.021</td><td>0.26</td></tr></table>

$^{a}$ Unit delay cost per second.  
$^{b}$ The gap is defined as (upper bound-lower bound)/upper bound.  
$^{c}$ In seconds.  
$^{d}$ Utilization of logical links.

![](/api/attachments/GAZYEFFG/fulltext/images/c77c8f96347128e37d00fc8a8a07614bc0a5243091ec2cbf91e3b95a761d535f.jpg)  
Fig. 8. The ten-node network structure. The numbers indicate the distance in miles.

![](/api/attachments/GAZYEFFG/fulltext/images/be35b398c501357dab047fbacb7a8c78818d48a4a77530ad7fad0da00b50b0ab.jpg)  
(a) $\mathbf{D} = 1000$

![](/api/attachments/GAZYEFFG/fulltext/images/82aabce35e97ba14ed5d08bfd0a8d02d584e769a4b34fdbdfe9f9920c8dd9d9f.jpg)  
(b) D=2000

![](/api/attachments/GAZYEFFG/fulltext/images/d2804f3b4b43166fc47b6da7a149af60ec6be4e332f6c7109a86323f4ec90a81.jpg)  
(c) D=3000

![](/api/attachments/GAZYEFFG/fulltext/images/5216ccdd77bd20fc33a6ba4b73c5dd0c3caf5372bc1664c30409feb54b40c175.jpg)  
(d) D=4000  
Fig. 9. Topologies for different value of D for 10-node network example.

Table 6  
Numerical results for ten-node example

<table><tr><td> $D^{a}$ </td><td>Upper bound</td><td>Lower bound</td><td> $Gap^{b}$ </td><td>Queuing cost</td><td>Lease cost</td><td>Avg delay/packet  $^c$ </td><td>Avg util. $^d$ </td></tr><tr><td>1000</td><td>4548401</td><td>4017102</td><td>0.117</td><td>2260541</td><td>2287860</td><td>0.025</td><td>0.37</td></tr><tr><td>1500</td><td>5771206</td><td>5147337</td><td>0.108</td><td>3372191</td><td>2399015</td><td>0.025</td><td>0.37</td></tr><tr><td>2000</td><td>6927873</td><td>6212636</td><td>0.103</td><td>4501518</td><td>2426355</td><td>0.025</td><td>0.37</td></tr><tr><td>2500</td><td>7928486</td><td>7235505</td><td>0.087</td><td>5421201</td><td>2507285</td><td>0.024</td><td>0.33</td></tr><tr><td>3000</td><td>9057723</td><td>8229726</td><td>0.091</td><td>5940458</td><td>3117265</td><td>0.022</td><td>0.29</td></tr><tr><td>3500</td><td>10084978</td><td>9202517</td><td>0.087</td><td>6727733</td><td>3357245</td><td>0.021</td><td>0.26</td></tr><tr><td>4000</td><td>10945168</td><td>101557929</td><td>0.072</td><td>7645483</td><td>3299685</td><td>0.021</td><td>0.26</td></tr></table>

$^{a}$ Unit delay cost per second.  
$^{b}$ The gap is defined as (upper bound-lower bound)/upper bound.  
$^{c}$ In seconds.  
$^{d}$ Utilization of logical links.

## 3.2. Ten-node test cases

A second group of test cases were created using ten cities across the United States as nodes for the private data network. (The cities selected are Seattle, San Francisco, Los Angeles, Kansas City, Houston, Chicago, Atlanta, Boston, New York, and Miami.) Fig. 8 shows the locations of these cities and twenty-one candidate physical links connecting them. The length of each of the candidate physical links, as measured in airline mileage, is also shown. The average traffic load between all O-D pairs is 2000 packets/s.

As in the five-node example, different test cases were created by varying the delay cost parameter. The topologies generated for the cases D = 1000, 2000, 3000, and 4000 are shown in Fig. 9. As expected, as the value of D increases, more candidate physical links are selected, and each link is more likely to use a T3. The topologies chosen for smaller delay cost parameters are sparser. For example, Fig. 9(a) shows that twelve links with single T3 circuits are selected from the twenty-one candidate links. For the D = 2000 case shown in Fig. 9(b), three additional T1s are selected for the links (3,5), (5,10), and (8,10). More links are selected when D = 3000 and most when D = 4000; these networks employ both T1s and T3s.

The numerical results for the various scenarios are summarized in Table 6. For the five-node example, the best solutions found were within $4.0\% - 10.3\%$ of the optimal solutions; on the other hand, the accuracy of the ten-node example ranges between $8.7\%$ and $11.7\%$ . These relative gaps are somewhat common in this type of large-scale and non-linear mixed integer problem [10,12]. The average utilization in both cases is around $35\%$ , which is close to the desired utilization level in practice. As expected, the average delay is greater when delay costs are lower. These results show that the resulting physical topology is sensitive to the users' delay costs (or to the desired average delay per packet).

The numerical results for both five and ten-node examples were tested on an IBM PC 486 machine. The five-node example included 270 variables with 36 constraints and the results were obtained within 2 minutes. The ten-node network example included about 1000 variables and 200 constraints and the results were obtained within 60–100 minutes.

## 4. Summary and conclusions

Today's private networks are based on digital technology and typically use T1 and T3 circuits to exploit the economies of scale built into the tariff structure for these digital circuits. T1 and T3 circuits form a reconfigurable network through DCSs, and data networks are defined as logical networks over a reconfigurable T1/T3 network. This paper presents a decision model for the minimum cost design of both a T1/T3 network and its logical data network (i.e., the packet-switched network). Specifically, the proposed formulation simultaneously solves the following decision problems: (i) the topology design and capacity allocation of the physical network; (ii) the logical network configuration and channel assignment; and (iii) the traffic routing problem on the logical network.

The decision model was formulated as a large-scale non-linear mixed integer program. We developed an efficient solution procedure based on Lagrangean relaxation of certain inequality constraints and subgradient optimization. Our test cases show that changes in traffic load or delay costs have a significant impact on the optimal physical and logical design. In addition, we find that the logical network topology differs from the physical one; some logical circuits may not reside in the shortest physical paths in order to take advantage of the economies of scale and avoid congested links. Our procedure obtained solutions within 4.0%-11.7% of the optimal solution.

Incorporating our computerized solution methodology into an interactive Decision Support System will enable network managers to explore the robustness of the optimal results. It will also facilitate sensitivity analysis with respect to major cost or traffic load assumptions. The decision models presented in this paper can be extended in a number of ways. One possible extension needs to consider the case of several logical networks – including packet-switched and circuit-switched networks – operating over a single physical network. Other extensions should deal with the design and planning of international networks that incorporate several national tariff structures and more specialized technological constraints.

## References

[1] H. Amirazizi, Controlling Synchronous Networks with Digital Cross-connect Systems, IEEE GLOBECOM, Hollywood, Florida, (1988), pp. 1560–1563.

[2] R. Boorstyn and H. Frank, Large-scale Network Topo-

logical Optimization, IEEE Trans. on Comm., 25(1), (1977), pp. 29–47.

[3] K. Chari and A. Dutta, Design of Private Backbone Networks – I: Time Varying Traffic, European Journal of Operations Research, 67(3), (1993), pp. 428–442.

[4] K. Chari and A. Dutta, Design of Private Backbone Networks – II: Time Varying Grouped Traffic, European Journal of Operations Research, 67(3), (1993), pp. 443–452.

[5] N. Chattopaphyay, T. Morgan, and A. Rachuram, An Innovative Technique for Backbone Network Design, IEEE Trans. on Systems, Man and, Cybernetics, 19(5), (1989), pp. 1122–1132.

[6] H. Choi, A. Seidmann, and M. Suh, Private Data Network Design Using Digital Cross-connect Systems: Reconfigurable Network Design, Proceedings of the Second Annual Workshop on Information Technologies \ and Systems, Dallas, Texas (1992).

[7] H. Choi, A. Seidmann, and M. Suh, Backbone Network Design of Reconfigurable Private Data Networks, Working paper, William E. Simon Graduate School of Business Administration, University of Rochester (1993).

[8] S. Dewan and H. Mendelson, User Delay Costs and Internal Pricing for a Service Facility, Management Science, 36(12), (1990), pp. 1502–1517.

[9] R. Doverspike and V. Jha, Comparison of Routing Methods for DCS-Switched Networks, Interfaces, 23(2), (1993), pp. 21–34.

[10] A. Dutta and J. Lim, A Multiperiod Capacity Planning Model for Backbone Computer Communication Networks, Operations Research, 40(4), (1992), pp. 689–705.

[11] Federal Communications Commission, Telecommunications Tariff 9, Washington D.C. (1989).

[12] P. Fetterolf and G. Anandalingam, A Lagrangean Relaxation Techniques for Optimizing Interconnection of Local Area Networks, Operations Research, 40(4), (1992), pp. 678–688.

[13] B. Gavish and K. Altinkemer, Backbone Network Design Tools with Economic Tradeoffs, ORSA J. on Computing, 2(3), (1990), pp. 236–252.

[14] B. Gavish and L. Hantler, An Algorithm for Optimal Route Selection in SNA Networks, IEEE Trans. on Comm., 31(10), (1983), pp. 1154-1161.

[15] B. Gavish and I. Neuman, A System for Routing and Capacity Assignment in Computer Communication Networks, IEEE Trans. on Comm., 31(4), (1989), pp. 360-366.

[16] M. Gerla and L. Kleinrock, On the Topological Design of Distributed Computer Networks, IEEE Trans. on Comm., 25(1), (1977), pp. 48–60.

[17] A. Graves, P. Littlewood, and S. Carlton, An Experimental Cross-connect Systems for Metropolitan Application, SAC-5(1), (1987), pp. 6–18.

[18] M. Held, P. Wolfe, and H.D. Crowder, Validation of Subgradient Optimization, Mathematical Programming, 6, (1974), pp. 62-88.

[19] W. Hutcheson and T. Snyder, Control Service Based on Digital Cross-connect Systems, IEEE J. on Selected Areas in Communications, SAC-5(1), (1987), pp. 33–37.

[20] L. Kleinrock, Queuing Systems: Volume I, New York, Wiley-Interscience (1975).

[21] H. Lemberg and M. Eiger, Fiber Hubbing Applications of High-speed Cross-connect Systems, Proceedings of the IEEE ICC, (1988), pp. 0340-0343.

[22] M. Lee and J.R. Yee, An Efficient Near-Optimal Algorithm for the Joint Traffic and Trunk Routing Problem in Self-Planning Networks, IEEE INFOCOM, (1989), pp. 127–135.

[23] J.A.S. Monteiro and M. Gerla, Topological Reconfiguration of ATM Networks, IEEE INFOCOM, (1990), pp. 207–214.

[24] N.J. Muller and R.P. Davidson, LANs to WANs: Network Management in the 1990s, Artech House (1990).

[25] I. Neuman, General Method for Computer Network Design, Ph.D. Dissertation, Ph.D.-25, William E. Simon Graduate School of Business Administration, Univ. of Rochester, (1987).

[26] M.J.T. Ng and D.B. Hoang, Joint Optimization of Capacity and Flow Assignment in a Packet Switched Communication Network, IEEE Tran. on Comm., COM-35, (1987), pp. 202–209.

[27] V. Saksena, Topological Analysis of Packet Networks, IEEE J. on Selected Areas in Communications, 7(8), (1989), pp. 1243–1252.

[28] C. Siller, M. Cohen, and T. Aprille, Digital Cross-connect Systems: Network-based vehicles for private T1 Resource Management, IEEE GLOBECOM, (1989), pp. 522–526.

[29] W. Stallings, Business Data Communication, Macmillan, (1990).

[30] P. Zanella, Customer Network Reconfiguration Application Utilizing Digital Cross-connect Systems, IEEE GLOBECOM, (1988), pp. 1538–1543.

[31] T.G. Zerbiec, Considering the Past and Anticipating the Future for Private Data Networks, IEEE Communication Magazine, March (1992), pp. 36-46.

![](/api/attachments/GAZYEFFG/fulltext/images/0e727024c200f7587392de29a28bf357f5964e800815bfcedd296db328fd259e.jpg)

Heung Sik Choi is an Assistant Professor of Management Information Systems at the School of Business Economics at Kookmin University, Seoul, Korea. He got his Ph.D. in Computers and Information Systems at the William E. Simon Graduate School of Business Administration at the University of Rochester. He has a master's degree in Management Science from the Korea Advanced Institute of Science and Technology. He

worked at one of the largest telecommunication companies in Korea on database implementation on value-added networks.

His current research interests include the design of public and private communication networks, multimedia communications, and a systems approach to network design support systems. He is also interested in database design and the economics of telecommunications systems.

![](/api/attachments/GAZYEFFG/fulltext/images/34fb3f12bf7cc305d03e2bbbeec6c8a51e2d44195fa04dc2b88e261ffc3ef70b.jpg)

Abraham Seidmann is the Xerox Professor and Areas Coordinator of Computers and Information Systems, Management Science and Operations Management at the William E. Simon Graduate School of Business Administration at the University of Rochester, Rochester, NY. He is a Department Editor on Interdisciplinary Management Research and Applications in Management Science. He is also an Associate or Area Editor

for IIE Transactions, Production Planning and Controls, Journal of Intelligent Manufacturing, Production and Operations Management and International Journal of Flexible Manufacturing Systems. Dr. Seidmann is the author of numerous research articles mostly published in such leading journals as Management Science, IIE Transactions, Operations Research, Decision Support Systems, International Journal of Production Research, and the IEEE Transactions. His current research and consulting activities include Strategic Business Information Systems, Information Economics, Management and Analysis of Service and Production Systems, Computer Integrated Manufacturing (CIM), and Stochastic Models for Scheduling and Control. He has consulted with many leading corporations and presented research or management seminars in four continents.

![](/api/attachments/GAZYEFFG/fulltext/images/541edeea813c9b1cda6d835bdb40704d0b943fd8db27a437a45b39ec14d0491e.jpg)

Myung W. Suh is an Assistant Professor of Information Systems at the Naval Postgraduate School. The focus of his research is the design and management of telecommunication systems, computer networks, distributed database, and information systems integration. He has taught, published, and consulted extensively in these areas. He earned his Ph.D from the Simon School of Business Administration of the University of Rochester

and M.B.A. from the University of Chicago.
