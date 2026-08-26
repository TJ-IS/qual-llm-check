---
otero_id: 19600
otero_key: "3Q4YMA3U"
title: "A decision support system tool for the transportation by barge of import containers: A case study"
authors: "Stefano Fazi; Jan C. Fransoo; Tom Van Woensel"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.08.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support system tool for the transportation by barge of import containers: A case study

Stefano Fazi <sup>a,</sup>⁎, Jan C. Fransoo <sup>b</sup>, Tom Van Woensel <sup>b</sup>

<sup>a</sup> University of Groningen, Faculty of Economics and Business, Nettelbosje 2, 9747 AE Groningen, The Netherlands

<sup>b</sup> Eindhoven University of Technology, School of Industrial Engineering, PO BOX 513, Pav F, NL-5600MB, Eindhoven, The Netherlands

## a r t i c l e i n f o

Article history: Received 4 November 2014 Received in revised form 27 July 2015 Accepted 2 August 2015 Available online 6 August 2015

Keywords: Inland transport Routing Mode selection Container Decision support system

## a b s t r a c t

In this paper, we present a DSS that generates schedules for the transportation of containers by barge in the hinterland, in particular from sea terminals to an inland terminal. As a case study, we propose the transportation from the ports of Rotterdam and Antwerp to a terminal in the south of the Netherlands, where the problem is typical. This problem is modeled as a heterogeneous fleet vehicle routing problem. The main decision is based on the trade-off of either consolidating containers to generate economies of scale with barges or alternatively dispatch, expensively and quickly, single containers by truck. The DSS is flexible as it can be applied to different settings by properly tuning the several parameters in the model. With numerical experiments, based on real world data, we evaluate the effectiveness of this system and its applicability.

© 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

In recent years, traffic of containers has increased considerably. Global trade favors the use of containers, as standardized handling units are necessary for the different logistic systems worldwide, and lead to a lower cost of transportation [2]. One of the main advantages of this standardization is the encouragement of multimodal transport, that favors economies of scale in transport, and can reduce congestion and emissions [12].

Recently, the transportation of containers in the hinterlands is drawing considerable attention for several reasons. This transportation leg has been acknowledged to be the most costly in many container supply chains; 40% to 70% of the total transportation cost is in the hinterland [26]. Moreover, an excessive use of trucks between sea ports and hinterland causes issues of congestion and pollution [38]. Promoting the use of alternative modes of transport is one of the primary measures to decrease the drawbacks of inland transportation and generate economies of scale [12,15].

In Europe, especially in the Northwestern area where the flow of containers is the highest, the problem is relevant [22]. The hinterland is mostly affected by import container flows; the imbalance with the outbound traffic has been estimated to be in the ratio of 2:1 [32]. Therefore, inbound road traffic around the sea ports is becoming unsustainable and several expedients are being considered. Trains and barges are favored for the fact that they can generate economies of scale and can push large bundles far in the hinterland. Also port authorities and governments are supporting their use. For instance, the Port of Rotterdam defined a target for the 2035 modal split. The goal is to transport at least 45% of the volumes by barge, at least 20% by train, and at most 35% by truck. The modal shift will not be achieved easily and will require increasing performance from barge and train services [22].

In the Netherlands, many inland terminals provide transport services to and from the Port of Rotterdam and Antwerp. In the Brabant region (Southern Netherlands), tributaries of the river Meuse can connect the hinterland with the sea ports and also provide connections with other waterways. These geographical conditions are considerably favorable to the use of barges, such that inland terminals are providing their customers regular barge services in addition to trucks. For instance, this is the case for a terminal located in Veghel, which is the case study of this research. Additionally, many receivers prefer barge transport not only for its lower costs, but also for facilitation at customs and more flexibility in terms of dwelling time at the terminal premises [13]. Finally, the barge service is becoming more and more reliable due to new bundling policies within the ports that can limit complex routes among quays [27].

As the competitiveness of barge transport is increasing in this region, its demand has grown substantially. By the Port of Rotterdam, it is estimated that from 1985 to 1995 barge traffic grew from 200,000 TEU to about 1 million TEU; in 2005 the volume was about 2 million TEU, approximately a market share of 31% [21]; in 2014, a share of 36% against 53% of truck and only 11% of rail [30]. While trains are usually utilized for long distances and their services are mostly pre-scheduled, for barges planners have to deal with large and complex scheduling problems. The challenge is to consolidate containers with different necessities related to time. In fact, time constraints, such as due dates and different release dates, make the consolidation complex. Besides, other factors, as multiple quays, where to pick up containers and minimum utilization level, increase the complexity for the scheduler. All these components can somehow limit the use of barges and favor the use of trucks.

The aim of this paper is to develop a DSS for the optimal allocation of import containers to a heterogeneous fleet composed by barges and trucks; besides the paper aims to explore different aspects in this decision making process and to give managerial insights. The validity of the model is supported by a case study conducted at an inland terminal in the Netherlands. The DSS eases the creation of the schedules. It takes data concerning the availability, due dates and locations from the internal data base. Then, it feeds the algorithm which computes the schedule. Besides, different parameters can be adjusted by the planner to generate schedules with different features. Finally, the output is translated and made readable to the planner. The research questions we want to address are: How to model and solve the transportation of import containers in the hinterland? What is the incidence of due dates in the planning process? To what extent the level of barge utilization affects the allocation and the total cost? To what extent is it possible to reduce multiple visits of port quays in each tour? How the availability of information in the time horizon can affect the planning process?

This paper is organized as follows: Section 2 provides the related literature; Section 3 presents the problem and the case study; Section 4 formulates the mathematical model and a relaxed version; Section 5 describes the heuristic used to generate the schedules; Section 6 presents numerical experiments based on instances drawn from real data; finally Section 7 concludes the paper with our final recommendations.

## 2. Related literature

Relevant literature with concern to container supply chain systems and the development of DSS's can be grouped into two main areas: operations at container terminals and transportation. As the traffic of containers has grown exponentially in the last two decades worldwide, and the related supply chains have become more and more complex, it is crucial to make effective decisions. Therefore, the topic caught the interest of many researchers to develop decision support tools for different aspects of the supply chain.

With concern to the first area, operations at container terminals, some main problems arise: berth, yard and crane allocation at the quay side and container packing. We refer to [5] for a thorough review of typical problems and related scientific papers. With a DSS point of view, we can find several papers treating the topic. In [36], Ursavas proposed a DSS to optimally allocate berths and cranes considering two conflicting parties: shipping companies and terminal operators. The author provides a multi-objective integer programming model that aims to achieve acceptable service level for the shipping companies and lower operational costs for terminal operators. Murty et al. [24] developed a DSS to analyze a set of inter-related daily operational decisions at a container terminal. The goal is to optimize berthing times of vessels, resources for handling operations, waiting times of trucks and to make the best use of the storage space. Ngai et al. [25] proposed a radio frequency identification (RFID) prototype system that is integrated with mobile commerce in a container depot. The system is implemented to keep track of the locations of stackers and containers, to provide greater visibility of the operations data, and to improve the control over the process. Finally, Chien and Deng [6] proposed a container packing support system. The system incorporates an algorithm, a graphic interface and a simulation program that guides the user step by step in the packing process.

The second area, related to transportation, has mainly tackled the problem of empty container management (ECM). We refer to [33] for a review. In [31], Shen and Khoong developed a DSS to solve empty container repositioning for a shipping company, using a network optimization model. The system considers demand and supply of empty containers over a multiperiod planning horizon and optimizes the flows of containers both on a local and regional level. In [2], Bandeira et al. integrated decisions upon flows of full and empty containers in a single system. They consider a network of suppliers, demand points, harbors and warehouses, and the problem is modeled as a Multiple Depot Vehicle Scheduling Problem; the aim is to minimize global distribution costs. The DSS is composed of a static and dynamic model. The static model optimizes a network flow problem and considers the input given by the dynamic model, which heuristically selects the containers and gives them priority according to transportation times and original dates of order.

Specific literature related to barge transport has recently seen a moderate growth due to the increasing predominance of this modality in some regions, especially Northwestern Europe. In [9], Douma et al. developed a Multi-Agent system to improve the coordination between barge and terminal operators for the Port of Rotterdam. After a sequence of terminals to visit, so-called rotation (which is tackled in our paper), is decided by barge operators, the terminal operator receives the appointments and has to schedule the visit of barges at the quays considering practical constraints. The system is meant to align such activities in an optimal way for both parties. In [13], Frémont and Franc conducted a study on the competitiveness of barge transport for the Port of Le Havre. They claim that in such a setting with lower volumes than Rotterdam and Antwerp, competitiveness can be achieved with additional logistic services to make the barge more appealing: more flexibility with the custom, warehousing and extended detention free periods. Other relevant studies have a simulation perspective and aim to give insights on the network of the ports. In [22], Konings et al. pointed out that a hub-and-spoke network can be beneficial for ports such as Rotterdam as to decrease the number of calls and waiting times. They show with a simulation study that with such a network improvements can be achieved when the cross-docking hub is located at a greater distance, as this can favor economies of scale. Finally, Caris et al. [4] proposed a simulation study that analyzes the impact of different cross-docking facilities on waiting times and capacity utilization for the Port of Antwerp.

To the best of our knowledge literature related to the treated problem is quite scarce, as it mainly focuses on the ECM problem. Somehow, ECM drew more attention to the detriment of the study of the full transportation leg, as this is seen by most as a mere allocation model [2]. As a consequence, we are not able to find any relevant literature that addresses our problem and emphasizes the complexity of the consolidation with a time perspective and also considers the features of barge transport. Somehow, this is surprising. The full container management puts a lot of pressure on planners as the need of respecting deadlines on one hand and the need to consolidate containers to generate economies of scale on the other hand clash with each other. Therefore, this paper aims to fill this gap and the case study is meant to provide an actual motivation for this DSS.

To model this particular hinterland transportation of containers, we need to address the heterogeneous fleet vehicle routing problem (HVRP); while, for a relaxation of the problem, we address the variable size bin packing problem (VS-BPP), see [19] for definitions and [16] for a comparison of different solution methods. With concern to the HVRP, we refer to [1] for a review and to [17] for a survey of its industrial applications. On this problem the literature is indeed quite scarce [11]. Two main variants have been proposed, with a limited and unlimited number of vehicles. As stated by Baldacci et al. [1], for HVRP exact methods have not been developed yet. All the existing studies have focused on developing heuristics. The best performing heuristics appear to be a tabu search algorithm developed in [14], a heuristic column generation method in [34] and a threshold accepting algorithm in [35].

## 3. Problem description

We define hinterland transportation as the movement of containers from a sea port to the hinterland (inbound) and vice versa (outbound). In the Northwestern Europe supply chain, there is an imbalance between import and export containers [32]; inbound flows are dominant in such a supply chain and they drive the scheduling decisions.

For inbound flows, containers usually arrive at the sea ports by means of ocean vessels. After the containers are unloaded from the ships, they are temporarily stacked on the quay and subsequently they are moved to the hinterland. With regard to the case study, two main options are available for this transportation leg: trucks and barges. The transport planner decides how to pick up containers from the sea terminal considering the following information: release dates and due dates; composition of the fleet and transport capacity; travel times and costs. In general, the planner tries to reduce transportation costs by preferring barges to trucks. However, this entails more complex planning. The barges should be filled to a high percentage of their capacity in order to achieve an economy of scale. Besides, the planner will prefer to bundle containers located at the same quay in order to limit the number of calls, additional handling operations, and transportation time. In fact, a routing problem has to be considered. We refer to this operational problem as hinterland allocation problem (HAP).

## 3.1. A simpler plan due to new port strategies

Port competition is moving from competition between ports to competition between transport chains. As a consequence, ports increasingly aim to improve the quality of hinterland transport services and the access to the hinterland [37]. Coordination among ports and inland terminals, together with new bundle strategies within the ports, lead to a leaner system. As described in [22], a hub-and-spoke network for hinterland services would change the current situation in the sea port – consisting of separate collection and distribution – into a system where barges need to visit only one terminal. Containers would first be collected from different sea terminals and second grouped according to their destinations. This hub-and-spoke setting would generate transport services focused on a small set of terminals and would lead to simpler routes with few stops. Since barges would shuttle between the inland terminal and a dedicated hub, the routing problem could be neglected and HAP would change into a variable size bin packing problem (VS-BPP) with time features.

In this study, we propose a relaxation of the basic planning problem, where the barge is allowed to visit only one dock where all the containers are assumed to be located. As the network under study is dense with few main clusters, we expect a fair approximation. Moreover, when a hub-and-spoke strategy will be fully applied in the future this relaxed model can replace the HAP based on routings.

## 3.2. Time horizon and scheduling against available information

Decisions are made considering the available information. As the container system is highly dynamic and the exchange of actual information between sea terminals and planning systems is not always in real time, the planner faces critical decisions in a planning horizon window.

A planning horizon window means that the planner uses the data that cover a certain time window to make the plan. Therefore, the availability and the accuracy of advanced information play a crucial role to determine good schedules. When information does not cover large windows, the planner can miss opportunities for bundling. Clearly, also the time when the planner decides to close a scheduling process is critical.

In the numerical section, some results for the HAP compared with the real planning show these particular drawbacks. Moreover, we solve a set of instances with planning horizon windows to show how information from extensive coverage of time can contribute, generally, to better schedules.

## 3.3. Case study management and related assumptions

The case study has been conducted on a close collaboration with Inland Terminal Veghel (ITV), its managers and its planners. ITV was established in 2004 and since 2009 is part of the joint venture Brabant Intermodal, where a set of inland terminals in the Brabant region are cooperating. The analysis of the system was first conducted on site for a period of two months, on average 3 days per week. Afterward, weekly meetings were held for complementary information and data sharing.

Considering solely the Dutch territory, it is possible to find at least 20 inland terminals with the same features in terms of provided services, destinations and connection with the ports; see [29] for a list of inland terminals and a description of services and links. This demonstrates the validity of this study and its relevance and applicability for many different contexts.

According to the information obtained from ITV, we are able to make the following assumptions for our model:

(i) A sea terminal is defined as a cluster. Within a cluster all the quays are equidistant from each other (1 h). The distance from any quay of a cluster to the inland terminal or to another sea terminal is defined as the distance from the cluster itself.

(ii) Barges depart from the inland terminal only when every allocated container is released at the sea terminals.

(iii) The inland terminal is considered the final destination for both trucks and barges.

(iv) Due dates are defined at the inland terminal.

(v) The fleet is limited and immediately available for transportation.

With the first assumption, the routing problem becomes trivial to solve (see Section 4). The model is not much affected in comparison to reality. This is a consequence of a system that is composed of dense clusters and is quite flexible in terms of time. Delays of hours are a matter of course. Hence, planners are used to estimating average times by rule of thumb.

With regard to the second assumption, barges are not allowed to sojourn at the sea terminal waiting for containers to be released. Besides, it is common practice that containers are booked when they are physically available and the booking is made before the barge sails to the port. In order to ensure this, we require barges to depart only when all allocated containers are available for pick-up.

With respect to the third assumption, a container can be either picked up by the customer at the inland terminal or an additional short leg must be performed by a truck. In this study, we assume the inland terminal is the final destination.

Regarding the fourth assumption, the definition of due dates can be ambiguous. Usually, they are not very rigid and can be negotiated by the transport providers. Moreover, they can be defined either at the inland terminal or at the customer site. This depends on whether the receiver is picking up the container or the terminal is responsible for bringing it to the customer premises. In this study, we define all the due dates at the inland terminal.

With the fifth assumption, we impose a limited fleet. For trucks we assume an amount equal to the number of containers. For barges, we find the amount by dividing the total load of containers to be processed by the minimum convenient load (see Section 6).

## 4. Mathematical model

We study the allocation of containers to a heterogeneous fleet for transportation from the seaside to the hinterland. The objective is to minimize the cost for transportation. We formulate the HAP as a classic HVRP, given that the inland terminal serves as a depot and the containers as nodes of a network each to be visited exactly once, The proposed HVRP formulation is favorably adapted to the network under study. Then, we relax it in order to provide a lower bound.

![](/api/attachments/3Q4YMA3U/fulltext/images/3498872943f8b36a5799832a756df08c97cc5b3960e49fbc34d142773baeafd7.jpg)  
Fig. 1. Maasvlakte and Rotterdam city terminal are two of the major sea terminals in the Port of Rotterdam and they have several quays, as well as the Port of Antwerp. The case study provides in total 36 possible quays, where containers are picked up.

## 4.1. Tailoring the HVRP formulation for the network under study

We define the Hinterland Allocation Problem (HAP) on a complete graph $G = ( \mathcal { N } , E )$ , with N the set of vertices and E the set of arcs. G consists of three main clusters (i.e. sea terminals) each containing a set of quays where containers are located, see Fig. 1. The specific network under study can be used advantageously to develop a formulation that avoids the typical sub-tour elimination constraints of the HVRP [7]. Due to the particular network being divided in clusters and the assumption (i) of equidistance between the quays of each cluster, we can push the route to follow a pre-determined master route that visits all the quays, sorted per cluster.

Let $N = 0 . . . I$ define the set of nodes of the network; where 0 represents the inland terminal and indexes from 1 to I represent the containers.<sup>1</sup> Let $V _ { i , j }$ be the travel time between nodes $i , j \in { \mathcal { N } } .$ Hence, we order the set N by non-decreasing values of $V _ { 0 , j }$ and we sort the containers by sea terminal and quay. Specifically, we build the set N such that

• Containers belonging to the same sea terminal are contiguous.

• The sequence of the sea terminals in the list is from the closest to the farthest from the inland terminal.

• Containers belonging to the same quay are contiguous.

We can now build a master route that follows the order of containers of the set . Such a master route is then short-cut according to the con-<sup>N</sup>tainers belonging to the route and can be shown to be optimal in this setting. In order to show the optimality, let us define a two layer graph (see Fig. 2). In the first layer, we have three nodes representing each sea terminal. An optimal route through these nodes can be found by enumeration; in the case study, the optimal sequence is from the closest to the farthest. In the second layer, we need to find the optimal route within each sea terminal. Due to the equidistance assumption (assume a value L) within a cluster (i), when some containers belonging to the same sea terminal are allocated to a barge, there is no specific optimal path needed to visit their quays. This is because every path within quays of a sea terminal would have the same length. The proof is trivial, as every path between |δ| quays is composed of $\left. \delta \right. - 1$ edges, the total length is necessarily $L ( | \delta | - 1 )$ for every path. Hence, every possible path between a subset of quays within a sea terminal is optimal. Therefore, a route that follows a sequence of allocated containers according to the order of set N is necessarily optimal.

Although we cannot claim this result to be generally applicable, it is particularly relevant for the container system under study, where sea ports usually have a dense network [28] and inland terminals deal with a very limited number of sea terminals.

## 4.2. Model formulation

With the results provided in the previous section, we can now present a mathematical formulation adapted to the case study.

Consider a set $\boldsymbol { \mathcal { T } } = \{ 1 , . . . , I \}$ of containers with the ith with size $w _ { i } ,$ release date at the port $A _ { i } ,$ and due date at the inland terminal $D _ { i } .$ Let $K = \{ 1 , . . . , K \}$ be a set of means of transport, each one with a certain <sup>K ¼</sup>capacity $Q _ { k } > 0$ and cost per hour of traveling $C _ { k } > 0 ( \in / \mathrm { h } )$ and let be the set of barges with ⊂ . In $G = ( \mathcal { N } , E )$ <sup>B</sup>the nodes represent both the <sup>B K ¼ ðN Þ</sup>locations of the containers and the inland terminal. Hence, the set of nodes $\mathcal { N }$ has size $N = I + 1 .$ . Let $V _ { i , j }$ be the travel time – expressed in barge travel times – for each pair i ${ \bf { \bar { \rho } } } _ { j \in \mathcal { N } . \phi _ { i , j } ^ { k } }$ is a constant converting V to truck travel times for edge $( i , j ) .$ <sup>N</sup>. When the containers are located on the same quay, their nodes overlap and, consequently, the travel time between them is 0. We define a binary parameter $Z _ { i , j } , i , j \in \mathcal { T } ,$ that equals 1 when containers i and j are on different quays, 0 otherwise. Let α be the time required to dock/park at a quay, and let L be the time needed to load each container.

To characterize the allocation, let $X _ { i , k }$ be the binary decision variable, with i ∈ and $k \in \mathcal { K } ,$ that indicates whether container i is assigned to a <sup>I K</sup>certain means of transport k; moreover, let $u _ { k } ,$ with k ∈ , denote the bi-<sup>K</sup>nary variable that equals 1 if k is used, 0 otherwise. The variable $t _ { k }$ keeps track of the time when a barge k is back to the inland terminal after its tour. When a means of transport is used to pick up containers, it covers a cycle that starts/ends from/to the inland terminal and goes only through the selected containers (nodes). A tour is defined by the binary variable $e _ { i , j } ^ { k } ,$ with $i , j \in \mathcal { N }$ and k ∈ ; we set it to 1 when a means of <sup>N K</sup>transport k covers the edge (i, j). The travel time to cover the edges of the route of a means $k \in \mathcal { K }$ is represented by $P _ { k } .$

Finally, we define a penalty $G ^ { B }$ for every time a barge arrives at a new quay and a penalty γ for unused capacity of the barges. With these penalties we model elements of the cost structure of the transportation system that are outside the exact modeling scope, but still impact the solution. For instance, the penalty for multiple stops, $G ^ { B }$ , leads the barge to visit fewer quays to load its bundle. Hence, this represents the costs for setting up quay-cranes and may reduce queuing issues at the docks. The penalty for unused capacity, $\gamma ,$ may reduce the number of barges sent to the terminals by increasing their level of utilization. This may lead to less congestion at the sea terminal on water, fewer setups required for the quay-cranes and a more efficient use of the fleet as barges entail a higher fixed cost than trucks with regard to fuel, personnel, and administration. All sets, data, parameters and variables are summarized respectively in Table 1.

We propose the following HVRP formulation:

$$
\operatorname{Min} \sum_ {k \in \mathcal {K}} C _ {k} P _ {k} + \sum_ {k \in \mathcal {B}} G ^ {\mathcal {B}} \left(\sum_ {i \in \mathcal {I}} \sum_ {j \in \mathcal {I}; j \neq i} e _ {i, j} ^ {k} Z _ {i, j}\right) + \gamma \sum_ {k \in \mathcal {B}} \left(Q _ {k} u _ {k} - \sum_ {i \in \mathcal {I}} w _ {i} X _ {i, k}\right)\tag{1}
$$

$$
\sum_ {k \in \mathcal {K}} X _ {i, k} = 1 \quad \forall i \in \mathcal {I}
$$

2

![](/api/attachments/3Q4YMA3U/fulltext/images/07ce7ca0d423f835b03258c976c81ab08d66d2860b3c4f7ba428a40a3abe2b26.jpg)  
Fig. 2. A two layer graph. In the first layer, we show the optimal route through the sea terminals found by enumeration. In the second layer, the optimal route through the quays; due to the equidistance assumption any path is optimal.

$$
\sum_ {i \in \mathcal {I}} w _ {i} X _ {i, k} \leq Q _ {k} u _ {k} \quad \forall k \in \mathcal {K}\tag{3}
$$

$$
\sum_ {j \in \mathcal {N}; j > i} e _ {i, j} ^ {k} = \sum_ {j \in \mathcal {N}; j <   i} e _ {j, i} ^ {k} = X _ {i, k} \quad \forall i \in \mathcal {I}; \forall k \in \mathcal {K}\tag{4}
$$

$$
\sum_ {j \in \mathcal {I}} e _ {0, j} ^ {k} = u _ {k} \quad \forall k \in \mathcal {K}\tag{5}
$$

$$
\sum_ {j \in \mathcal {I}} e _ {j, 0} ^ {k} = u _ {k} \quad \forall k \in \mathcal {K}\tag{6}
$$

$$
P _ {k} \geq \sum_ {i \in \mathcal {N}} \sum_ {j \in \mathcal {N}; j \neq i} \phi_ {i, j} ^ {k} V _ {i, j} e _ {i, j} ^ {k} \quad \forall k \in \mathcal {K}\tag{7}
$$

## Table 1

Elements of the model.

Sets:

Set of containers 1,…,I

$\mathcal { N }$ Set of nodes $0 , . . . , I$

$\kappa$ Set of means of transport 1,…,K

<sup>K</sup> Set of barges $1 , \ldots , B$

Data:

$w _ { i }$ Size of container i (TEU), ∀ i ∈

$D _ { i }$ Due date of container $i , \forall i \in \mathcal { T }$

$A _ { i }$ <sup>I</sup>Release date of container i, ∀ i ∈

$V _ { i , j }$ <sup>I</sup>Travel distances considering barge travel times, ∀i; j ∈

$\phi _ { i , j } ^ { k }$ Constant converting $V _ { i , j }$ <sup>N</sup>to truck travel times for arc (i,j), ∀k ∈ , ∀i; j ∈

$Z _ { i , j }$ <sup>K N</sup>Takes value 1 when containers i and j are on different quays, 0 otherwise, ∀ i, j ∈

$C _ { k }$ Transportation cost for means of transport k (€/h), ∀k ∈

$Q _ { k }$ Capacity of means of transport k (TEU), ∀k ∈

$\alpha$ Fixed setup time when a quay is reached

L Time for loading each container

Parameters:

$\gamma$ Cost for unused capacity $G ^ { B }$ Docking cost for barges (sea terminal site)

M A large value

Variables:

$X _ { i , k }$ Binary decision variable, set to 1 if container i is allocated to k, ∀ i ∈ , ∀k ∈ $u _ { k }$ Binary variable, set to 1 if means of transport k is used 0 otherwise, ∀k ∈ K $t _ { k }$ Arrival time of barge k back at the inland terminal, ∀ k ∈ $P _ { k }$ Travel time of means of transport k to cover the edges of the route, ∀k ∈ $e _ { i , j } ^ { k }$ Binary variable; Set to 1 if means k goes from i to j, 0 otherwise, ∀i; j ∈ , k ∈

$$
t _ {k} \geq A _ {\omega} X _ {\omega , k} + \alpha \left(u _ {k} + \sum_ {i \in \mathcal {I}} \sum_ {j \in \mathcal {I}; j \neq i} e _ {i, j} ^ {k} Z _ {i, j}\right) + L \sum_ {i \in \mathcal {I}} X _ {i, k} + P _ {k}\tag{8}
$$

$$
t _ {k} \leq D _ {i} + (1 - X _ {i, k}) M \quad \forall i \in \mathcal {I}; \forall k \in \mathcal {B}\tag{9}
$$

$$
u _ {k} \in \{0, 1 \} \quad \forall k \in \mathcal {K}\tag{10}
$$

$$
X _ {i, k} \in \{0, 1 \} \quad \forall i \in \mathcal {I}; \forall k \in \mathcal {K}\tag{11}
$$

$$
e _ {i, j} ^ {k} \in \{0, 1 \} \quad \forall i, j \in \mathcal {N}; \forall k \in \mathcal {K}.\tag{12}
$$

The objective function (1) minimizes the cost for transportation (first term), the penalty for docking a barge at more than one quay (second term), and the penalty for under-utilization of barges (last term). Analogously to bin packing constraints, inequalities (2) ensure that each container i is loaded, while Eq. (3) impose that the capacities of the means of transport are not exceeded. Inequalities (4), (5) and (6) are the flow conservation constraints. In particular, constraints (4) relate $X _ { i , k }$ with $e _ { i , j } ^ { k }$ and they impose the route to follow the master route described in the previous section. For example, in the first term we impose that in the route all successors j of i respect $j > i ,$ with $i , j \in \mathcal { N }$

<sup>N</sup>With Eq. (7) we calculate the travel time according to the routing. With constraints (8), we construct the return time $t _ { k }$ of barges according to assumptions (ii) and (iii). Specifically, we impose that the return time is greater than the latest release date of the allocated containers summed up to the transportation time to visit them $( P _ { k } ) ;$ ; moreover, for each stop at a quay, we wait a time α to dock/park and a time L to load each container. Inequalities (9) impose that the containers are delivered on time when transported by barge. Constraints (8) and (9) are defined only for barges, as trucks are expected to deliver containers on time.

## 4.3. A lower bound for HAP

The lower bound consists of assigning to each barge (i.e. bin) a certain delivery time $t _ { k } ;$ this will correspond to the time to reach one of the allocated container and come back; the chosen container is the farthest one. Due to the particular network under study, being made of few clusters containing nodes, we expect an accurate approximation.

Table 2  
Parameters for the instances

<table><tr><td colspan="2">Parameters:</td></tr><tr><td> $G^{B}$ </td><td>€50</td></tr><tr><td> $\gamma$ </td><td>€100</td></tr><tr><td> $w_{i}$ </td><td>2 for 2 TEU containers, 1.01 for 1 TEU containers</td></tr><tr><td> $D_{i}$ </td><td>From data set</td></tr><tr><td> $A_{i}$ </td><td>From data set</td></tr><tr><td> $V_{i,j}$ </td><td>0 h for same quay, 1 h within same sea terminal4 h between Maasvlakte and Rotterdam City Terminal16 h from Antwerp to the other 2 sea terminals13 h from Veghel to Antwerp11 h from Veghel to Maasvlakte and Rotterdam City Terminal</td></tr><tr><td> $C_{k}$ </td><td>74 €/h for trucks, 80 €/h for barges</td></tr><tr><td> $Q_{k}$ </td><td>2 TEU for trucks (no combination of two 1 TEU containers allowed),28.3 TEU for barges</td></tr><tr><td> $\alpha$ </td><td>10 min</td></tr><tr><td>L</td><td>6 min</td></tr><tr><td> $\phi_{i,j}^{k}$ </td><td>1 for barges, 0.2 for trucks  $\forall i, j \in \mathcal{N}$ </td></tr></table>

Specifically, the lower bound is obtained by relaxing constraints (8) with

$$
t _ {k} \geq (A _ {i} + 2 (V _ {0, i})) X _ {i, k} \quad \forall i \in \mathcal {I}; \forall k \in \mathcal {B}.\tag{13}
$$

The routing cost is computed again by following the master route; nevertheless, the exact calculation for the respect of the due dates – constraints (9) – is affected, as $t _ { k }$ is now independent from the routings. This approximation can reduce the number of trucks, when these are needed for HAP to avoid relatively small delays. Moreover, the model becomes less accurate in case of routes that require the visit of multiple quays and, even less, in case of multiple sea terminals. However, the largest gap between arrival times in HAP and its relaxed version can occur when all sea terminals need to be visited in a route. In the case study this can bring a maximum difference of around 20 h. Besides, it is clear that when all the containers are grouped in one quay and if we consider the time for docking and loading negligible, the proposed lower bound would match the HAP.

The reason we propose this lower bound is twofold. First of all, we want to provide a benchmark bound to assess the performances of the heuristic we develop for HAP. Second, such an approximation fits in those settings where the nodes of the graph are not scattered, as VRP instances found in the literature, but grouped in main clusters; it can even match when the collection is concentrated in one single node. Indeed, as the new trend in container hinterland chains is toward a more centralized collection (hub-and-spoke) [22] – with one main collection point – such a lower bound can emerge as a valid future model for practice.

![](/api/attachments/3Q4YMA3U/fulltext/images/ecee56dc5e1594500cdb7b41b08d60d055b261cf5368bb62e994f35bd4435387.jpg)

In fact, from a modeling perspective, the transportation time would be a fixed quantity, $\overline { { P } } _ { k } ,$ independent from the transported containers. As a consequence, there would be a fixed cost, ${ \overline { { C } } } _ { k } ,$ to be paid when a means of transport is used. Hence, constraints (4), (5), (6) and (7) can be removed and the minimization of the travel cost in the objective function becomes $M i n \sum _ { k \in \mathcal { K } } \overline { { C } } _ { k } u _ { k } ,$ in the same way as bin packing problems.

## 5. The solution method

For the proposed model, we develop a Metropolis algorithm. The Metropolis algorithm [23], is a methodology very similar to Simulated Annealing (SA) and Threshold Acceptance algorithms (see [20]). SA has been widely used in the literature for many combinatorial optimization problems and it is a practical tool for industrial applications, due to the ease of its parametrization and fast and effective performance [18].

SA makes use of a single parameter, called temperature, that varies throughout the procedure according to a cooling scheme. A Metropolis algorithm can be defined as SA with a fixed temperature, and it has been applied satisfactorily for many combinatorial problems, see [10]. In general, the higher the temperature, the more likely a move to a worse solution is accepted. Alternatively, a too low temperature could lead to local minima, though the convergence to these minima is really fast. Such a characteristic of the Markov Chain is well-known in the literature as the metastability problem, see [3]. At the moment, there is no strong evidence of the superiority of one method over another; besides, there is no theoretical method to find an optimal cooling scheme or constant temperature.

The choice for a Metropolis algorithm is driven by its ease of parametrization and is motivated by the well performing Threshold Accepting local search heuristic developed in [35] for the HVRP, which provides a similar mechanism. Another motivation comes from the deployment of the DSS for a real world application. Planners need a tool able to give good solutions for large scale problems in relatively little time, with an easy parametrization; this heuristic fulfills such an important requirement.

## 5.1. A metropolis algorithm for HAP

The algorithm starts by generating an initial feasible solution with a greedy procedure. Then, a set of temperatures are tried in parallel. At the end of the parallel runs, the best result from those is given as output. See Section 6.1 for more details on the parametrization.

## 5.1.1. Generating the initial solution: greedy algorithm

Let K be a list of means of transport sorted by decreasing values of their capacity. Let I be a list of containers sorted according to the order of N. Then the algorithm selects the first container and the first means on the list. The selected container is inserted in the selected means, if it fits. Otherwise, the algorithm chooses the next on the list of means of transport until the container fits.

![](/api/attachments/3Q4YMA3U/fulltext/images/677573038f131717235c2509958db2217f2a78383302ea9399f9cae364d31282.jpg)  
Fig. 3. Trends of the different temperatures in each run for the rst 1,000,000 iterations. The x-axis represents the iterations, the y-axis represents the current solution. The graph on the left depicts the trend of the smallest and the largest temperatures.

Table 3 Results for HAP/0/0/0/.

<table><tr><td rowspan="2">Instance</td><td rowspan="2">N</td><td colspan="3">Heuristic</td></tr><tr><td>Value</td><td># Barges</td><td># Trucks</td></tr><tr><td>1</td><td>28</td><td>3920</td><td>2</td><td>0</td></tr><tr><td>2</td><td>41</td><td>6470</td><td>3</td><td>1</td></tr><tr><td>3</td><td>42</td><td>6960</td><td>3</td><td>0</td></tr><tr><td>4</td><td>47</td><td>7700</td><td>3</td><td>2</td></tr><tr><td>5</td><td>47</td><td>6880</td><td>3</td><td>0</td></tr><tr><td>6</td><td>50</td><td>7160</td><td>2</td><td>8</td></tr><tr><td>7</td><td>58</td><td>8620</td><td>4</td><td>0</td></tr><tr><td>8</td><td>68</td><td>9900</td><td>4</td><td>6</td></tr><tr><td>9</td><td>90</td><td>13,360</td><td>7</td><td>0</td></tr><tr><td>10</td><td>109</td><td>14,150</td><td>7</td><td>2</td></tr></table>

The greedy algorithm is meant to allocate all containers to the barges. As we seek to transport containers primarily by barge, this type of solution is necessary because the ratio between the costs of barges and trucks is large: about 6:1. In fact, moving a container from a truck to an empty barge entails a very large “opening” cost that is unlikely to be accepted by the heuristic; according to our data, the cost increases by about 1400: the cost of the barge to visit one container minus the cost of the removed truck. On the other hand, moving a container from a barge to a truck should be accepted either when the container has a delay or when the barge can be emptied because of a small carried load.

## 5.1.2. Local search

After obtaining an initial solution s, the algorithm starts a local search in the neighborhood of $s ,$ by using two operators to generate new solutions, $\mathcal { O } _ { 1 }$ and $\mathcal { O } _ { 2 }$ , which are selected randomly in every <sup>O O</sup>iteration. Starting from solution s, we find s′ either by switching the allocation of a single randomly selected container to a different means of transport $\left( \mathcal { O } _ { 1 } \right)$ or swapping two randomly selected containers assigned to different means $( \mathcal { O } _ { 2 } ) . ^ { 2 }$

<sup>O</sup>When a new solution is found and it is feasible for the capacity constraints (3), we need to find an optimal tour. This is calculated by generating a route that follows the sequence of allocated containers according to the order of set ${ \mathcal { N } } ,$ as previously described. As the new <sup>N</sup>solution s′ is created and calculated, we accept it according to the probability $\begin{array} { r } { P ( T ) = \operatorname* { m i n } \{ e ( \frac { f ( s ) - f ( s ^ { \prime } ) } { T } ) , 1 \} } \end{array}$ [18]. During the local search we allow the algorithm to go through infeasible solutions with late containers on barges. Such infeasibility is punished in the objective function by a cost greater than the dispatch by truck of the container. Hence, in case of a late container, the algorithm is driven to move it to a truck in order to avoid the delay.

## 6. Numerical analysis and tests on case study data

In this section we present numerical experiments on a set of instances drawn from real data. The data set dates from July 2011 to September 2011. The actual schedules made by the planner were also available in the data set. The planner was not assisted by any decision support system. We test four scenarios in order to evaluate the decisions of the model from a practical perspective, to get insights for the real world application and to compare the solutions of the model with the actual decisions of the planner. The instances were tested with the parameters that are summarized in Table 2, obtained from the case study.

Regarding transport capacity, inland terminals can deal with a variety of different barges. However, larger barges cannot always be processed due to physical limitations of canals and locks. For instance, the inland terminal under study can receive barges with capacity up to 28 TEU, due to canal restrictions. For trucks, the terminal policy is to carry one container each time, either a 1 TEU container or a 2 TEU container. In order to avoid a truck carrying two 1 TEU containers, we parameterize the weight of 1 TEU containers as 1.01 and truck capacity as 2. Hence, in order to allow any possible combination of 1 TEU containers and 2 TEU containers for barges, we parameterize barge capacity as 28.3.

With regard to costs, the exact cost for a barge is tricky to estimate due to different rental agreements with barge providers. As trucks are owned by the terminal, their cost is more transparent. Specifically, it is estimated by the company that an amount of €330 is needed to make a round trip by truck, passing through the port of Rotterdam. On average, a truck takes 4.5 h to cover the distance, incurring a cost of 74 €/h. Planners of the terminal assume that an amount of six containers shipped by barge competes with six trucks. As a barge takes about 22 h for a round trip visiting a single quay, we assume for the barges a cost of 80 €/h in order to ensure a minimum load of six containers. Note that no constraints are generated in the model to force such a minimum level, which is therefore an output of the model. Moreover, the cost is expressed in $\epsilon / \mathrm { h } ,$ so such a minimum level can vary according to the locations of the containers. If more locations are visited, a larger consolidation is needed.

We could not base our analysis on real values for $G ^ { B }$ and γ as they describe aspects of the decision process related to common practices, rather than real costs. However, we tried several values for every instance and we considered as maximum possible value the average cost for transporting a container by truck; as a result, the parameters do not make the cost for barging too expensive when compared to trucking. We report here the two values that, overall, produced tangible and sensible results on the solutions.

From a DSS perspective, the user can interactively set the parameters of the models to get different solutions. Besides, D can change overtime as the containers are subject to continuous bargains between planners and customers. Other parameters are more related to the preference of the planners or to a particular situation. In case of a congested terminal, the planner would prefer less stops (increasing $G ^ { B } )$ .

The four scenarios derive from the combination of the hard constraints (9) on the due dates and the different costs in the objective function (1); we use the following notation $\ ^ { \cdot \cdot } \mathrm { H A P } / D / G ^ { B } / \gamma / ^ { \prime }$ . Specifically, we first solve HAP without any accessory cost but the transportation one and without hard constraints on delays; we denote this as “HAP/ 0/0/0/”. We then solve $\ " \mathrm { H A P } / D / 0 / 0 / "$ $\ " \mathrm { H A P } / D / G ^ { B } / 0 / "$ , and “HAP/D/0/γ/”.

The numerical section is composed as follows. In Section 6.1, we give details on the parameterizations of the heuristic, on the performances, and on the quality of the lower bound. In Section 6.2, we show several experiments on 10 real world instances. In Section 6.3, we give an example of how this algorithm can be implemented in planning horizon

Table 4 Results for HAP/D/0/0/.

<table><tr><td rowspan="2">Inst.</td><td rowspan="2">I</td><td colspan="3">Heuristic</td><td colspan="4">Planner</td></tr><tr><td>Value</td><td># B</td><td># T</td><td>Value</td><td>Gap %</td><td># B</td><td># T</td></tr><tr><td>1</td><td>28</td><td>3930</td><td>2</td><td>1</td><td>4970</td><td>26</td><td>2</td><td>4</td></tr><tr><td>2</td><td>41</td><td>8180</td><td>2</td><td>12</td><td>9750</td><td>19</td><td>2</td><td>16</td></tr><tr><td>3</td><td>42</td><td>13,760</td><td>2</td><td>28</td><td>14,460</td><td>5</td><td>0</td><td>42</td></tr><tr><td>4</td><td>47</td><td>12,190</td><td>2</td><td>21</td><td>16,050</td><td>31</td><td>0</td><td>47</td></tr><tr><td>5</td><td>47</td><td>12,620</td><td>2</td><td>24</td><td>16,290</td><td>29</td><td>0</td><td>47</td></tr><tr><td>6</td><td>50</td><td>12,130</td><td>3</td><td>17</td><td>15,070</td><td>24</td><td>3</td><td>27</td></tr><tr><td>7</td><td>58</td><td>11,370</td><td>3</td><td>13</td><td>14,590</td><td>28</td><td>2</td><td>32</td></tr><tr><td>8</td><td>68</td><td>10,390</td><td>4</td><td>7</td><td>14,840</td><td>42</td><td>5</td><td>16</td></tr><tr><td>9</td><td>90</td><td>16,850</td><td>5</td><td>20</td><td>20,540</td><td>21</td><td>6</td><td>27</td></tr><tr><td>10</td><td>109</td><td>16,940</td><td>7</td><td>6</td><td>28,700</td><td>69</td><td>7</td><td>44</td></tr></table>

Table 5

windows. All experiments were run on an Intel(R)Core(TM)i3-3220 CPU machine with 3.30 GHz and 8.00 GB RAM memory and the algorithm is coded in C with a limit of 20 million iterations. We calculated lower bounds by means of CPLEX 12.6 and with a time limit of 4 h.

## 6.1. Settings for the heuristic and performances

As we make use of a single temperature throughout the local search, we run simultaneously the algorithm with different temperatures, multiples of 10, in the range from 10 to 100; then, we repeat this process 5 times.<sup>3</sup> The range of temperatures was preliminarily tested and found sensible for the treated problem. At the end of each process, we keep the best solution found and the time needed to find it. After the 5 processes are performed, we calculate standard deviation, average of the best solutions found and average time to find them; these statistics can be found in Appendix A (Table A.1), while the best solutions are reported in the tables in Section 6.2.

In general, each temperature shows a different trend. As described by [8], when applying the Metropolis algorithm to the Quadratic Assignment Problem:“…if the system is kept too ‘hot’ then too many bad uphill moves are accepted for any good solution to be reached while if it is too ‘cold’ then the scheme will quickly drop into a local optimum and the remainder of the search will be a fruitless attempt to escape from it”. See Fig. 3 for an example of the trends for a set of temperatures. The different trends are displayed in distinct graphs for better visualization.

Concerning the performances of the heuristic and the quality of the lower bound, we report in Appendix B a summary of the results. We solve the relaxed model both with the heuristic and CPLEX and we compare the results in order to assess the performance of the algorithm. Then we report the results of the heuristic on HAP in order to evaluate the quality of the bounds. For CPLEX, we provide the best integer (upper bound) and best node (lower bound) found and the time when computation was stopped by the solver.<sup>4</sup> The results show that the heuristic provides good performance in terms of: average gap with the best nodes found by CPLEX, standard deviation and time. The maximum average gap is 2.7%. However, for all the experimentation the gap is spoiled by the results of instance 10, whose gap between best integer and best node is, in some cases, large to provide an accurate benchmark. Therefore, we report also the gap considering only those instances for which CPLEX found the optimal solution. In those cases the maximum average gap is 1%. Concerning speed, the algorithm obviously outperforms CPLEX, especially for the largest instances. Finally, we can appreciate that the relaxed model provide a fair approximation for HAP; the maximum gap with the heuristic, performed on HAP, is 4.9%, and 3.4% when not considering instance 10. For “HAP/D/0/0/” the gaps are respectively 3.1% and 1.9%. In the following section, we provide the details of the solutions of the heuristic performed on HAP.

## 6.2. Results based on real-world instances

We now show the results of the experiments performed on real world instances, provided by ITV.

## 6.2.1. Solving “HAP/0/0/0/”

We propose this experiment to show that without constraints (9) the solutions will be mainly composed by barges in order to generate economies of scale. This is evident from the results shown in Table 3 when compared with the results of the other scenarios (for example see Table 4).

Results for “HAP/D/G /0/”.

<table><tr><td rowspan="2">Instance</td><td rowspan="2">I</td><td colspan="5">Heuristic</td></tr><tr><td>Value</td><td># B</td><td># T</td><td># Stops</td><td># Stops HAP/D/0/0/</td></tr><tr><td>1</td><td>28</td><td>3980</td><td>2</td><td>1</td><td>3</td><td>3</td></tr><tr><td>2</td><td>41</td><td>8430</td><td>2</td><td>12</td><td>7</td><td>7</td></tr><tr><td>3</td><td>42</td><td>14,010</td><td>2</td><td>28</td><td>7</td><td>7</td></tr><tr><td>4</td><td>47</td><td>12,640</td><td>2</td><td>21</td><td>11</td><td>11</td></tr><tr><td>5</td><td>47</td><td>12,870</td><td>2</td><td>24</td><td>7</td><td>7</td></tr><tr><td>6</td><td>50</td><td>12,680</td><td>3</td><td>17</td><td>14</td><td>14</td></tr><tr><td>7</td><td>58</td><td>12,170</td><td>3</td><td>14</td><td>14</td><td>15</td></tr><tr><td>8</td><td>68</td><td>10,640</td><td>4</td><td>9</td><td>7</td><td>11</td></tr><tr><td>9</td><td>90</td><td>17,430</td><td>5</td><td>21</td><td>13</td><td>15</td></tr><tr><td>10</td><td>109</td><td>17,880</td><td>7</td><td>7</td><td>24</td><td>27</td></tr></table>

In some instances, trucks are still used and the reason is twofold; firstly, if the majority of the cargo is picked up in Rotterdam, it is not convenient to pick up few containers in Antwerp; secondly, if some barges are full and there are not enough containers left for bundling – in order to generate an economy of scale by barge – these would be trucked.

## 6.2.2. Solving “HAP/D/0/0/”

In this experimentation we test the model that considers transportation costs and hard constraints on the delays. In Table 4, we show the results of the experimentation and the actual solutions of the planner. By comparing these results with the ones of Table 3, we can notice that HAP/D/0/0/ makes use of more trucks. The planner solutions always have higher costs and make use of more trucks.

The results show an average improvement in the cost of 31% using the heuristic. The 10th instance is the one with the largest gap. From an analysis of this instance, we can understand that the containers were located on many different quays. We conducted an interview at the terminal planning board and we learned that the common behavior of the planner is to avoid the bundling of containers when these are stored in many different locations. Sometimes this way of scheduling is preferred to facilitate the trip, as well as the complexity of the allocation and the routing. As a consequence, this attitude produced a schedule with many barges under-utilized but with few stops: 61% average utilization and a total of 12 stops. Both the utilization and the number of stops in the heuristic solution are much higher (respectively 94.7% and 27). We encountered a similar issue for instances 3, 4 and 5, although the loss in terms of costs is less evident due to the smaller sizes of the instances.

Some discrepancies were also due to deficiencies of the information system used by the planner. Sometimes, either wrong or late information is the cause of poor schedules. For example, in instance 1, three containers could easily be bundled. Due to scarce information on their availability, the planner decided to eventually dispatch them by truck. Roughly €1000 could have been saved with better information in this case.

Table 6Results “HAP/D/0/γ/”.

<table><tr><td rowspan="2">Instance</td><td rowspan="2">I</td><td colspan="5">Heuristic</td></tr><tr><td>Value</td><td># B</td><td># T</td><td>%</td><td>% with HAP/D/0/0/</td></tr><tr><td>1</td><td>28</td><td>4241</td><td>2</td><td>1</td><td>94</td><td>94</td></tr><tr><td>2</td><td>41</td><td>8180</td><td>2</td><td>12</td><td>100</td><td>100</td></tr><tr><td>3</td><td>42</td><td>14,460</td><td>0</td><td>42</td><td>-</td><td>37</td></tr><tr><td>4</td><td>47</td><td>13,480</td><td>2</td><td>21</td><td>78.5</td><td>75</td></tr><tr><td>5</td><td>47</td><td>13,340</td><td>1</td><td>32</td><td>100</td><td>69.6</td></tr><tr><td>6</td><td>50</td><td>15,118</td><td>2</td><td>25</td><td>55.3</td><td>48.8</td></tr><tr><td>7</td><td>58</td><td>12,300</td><td>3</td><td>15</td><td>91</td><td>91</td></tr><tr><td>8</td><td>68</td><td>10,390</td><td>4</td><td>7</td><td>100</td><td>100</td></tr><tr><td>9</td><td>90</td><td>18,270</td><td>5</td><td>20</td><td>97.85</td><td>97.85</td></tr><tr><td>10</td><td>109</td><td>18,058</td><td>7</td><td>6</td><td>94.9</td><td>94.9</td></tr></table>

Table 7  
Comparison of the results for the different models.

<table><tr><td rowspan="2">Instance</td><td rowspan="2">I</td><td colspan="4">Heuristic</td></tr><tr><td>HAP/0/0/0/</td><td>HAP/D/0/0/</td><td> $HAP/D/G^{\mathcal{R}}/0/$ </td><td> $HAP/D/0/\gamma/$ </td></tr><tr><td>1</td><td>28</td><td>3920</td><td>3930</td><td>3930</td><td>3930</td></tr><tr><td>2</td><td>41</td><td>6470</td><td>8180</td><td>8180</td><td>8180</td></tr><tr><td>3</td><td>42</td><td>6960</td><td>13,760</td><td>13,760</td><td>14,460</td></tr><tr><td>4</td><td>47</td><td>7700</td><td>12,190</td><td>12,190</td><td>12,270</td></tr><tr><td>5</td><td>47</td><td>6880</td><td>12,620</td><td>12,620</td><td>13,340</td></tr><tr><td>6</td><td>50</td><td>7160</td><td>12,130</td><td>12,130</td><td>12,610</td></tr><tr><td>7</td><td>58</td><td>8620</td><td>11,370</td><td>11,620</td><td>11,710</td></tr><tr><td>8</td><td>68</td><td>9900</td><td>10,390</td><td>10,490</td><td>10,390</td></tr><tr><td>9</td><td>90</td><td>13,360</td><td>16,850</td><td>17,030</td><td>17,100</td></tr><tr><td>10</td><td>109</td><td>14,150</td><td>16,940</td><td>17,030</td><td>17,020</td></tr></table>

## 6.2.3. Solving $\ ^ { \prime \prime } H A P / D / G ^ { B } / { \cal O } / ^ { \prime \prime }$

We now test the model by penalizing multiple visits of barges to different quays. This behavior is limited by the parameter $G ^ { B }$ . The objective function we minimize is

$$
\operatorname{Min} \sum_ {k \in \mathcal {K}} C _ {k} P _ {k} + \sum_ {k \in B} G ^ {\mathcal {B}} \left(\sum_ {i \in \mathcal {I}} \sum_ {j \in \mathcal {I}; j \neq i} e _ {i, j} ^ {k} Z _ {i, j}\right).\tag{14}
$$

In Table 5, we report the number of stops for this scenario and for the model $\ " \mathrm { H A P } / D / 0 / 0 / "$ (column “# Stops $\mathrm { H A P } / D / 0 / 0 / " )$ . We can notice that the number of stops reduces only for four instances. This is not surprising because multiple visits are already penalized in the basic formulation for the distance to be covered between the quays. Note that the parameter $G ^ { B }$ limits the visit to multiple quays but it does not take into account the distance between them. Therefore, this cost can be related to the will of the planner to avoid multiple dockings for the barge. As there is no practical limit for the number of stops considered by the planner, we prefer this approach rather than constraining a maximum number of stops allowed.

## 6.2.4. Solving “HAP/D/0/γ/”

The results of Table 6 show how the parameter γ changes the solutions. The column “%” shows the average utilization of the barges, while in “% with $\mathrm { H A P } / D / 0 / 0 / "$ we report the percentages of model $\ " \mathrm { H A P } / D / 0 / 0 / "$ from Table 4. The objective function we minimize is

$$
\operatorname{Min} \sum_ {k \in \mathcal {K}} C _ {k} P _ {k} + \gamma \sum_ {k \in \mathcal {I}} \left(Q _ {k} u _ {k} - \sum_ {i \in \mathcal {I}} w _ {i} X _ {i, k}\right).\tag{15}
$$

In general, γ forces the removal of barges which are not fully utilized. Heuristically, the algorithm tries to remove a barge – assigning to trucks all its containers – when the level of utilization is lower than 50%. The result of instance 3 is peculiar; all the containers are trucked, while in the model $\ " \mathrm { H A P } / D / 0 / 0 / "$ , the barges are highly under-utilized. However, if we look at the solution of the planner in Table 4, we can notice that the containers were also all trucked. Hence, γ can help in reproducing this planning strategy.

## 6.2.5. Summarizing the results

In Table 7, we show a comparison between the different perspectives of the model we proposed in this numerical section. We remove from the numerical solutions the extra costs we added to the transportation cost in order to get a fair detail. We observe how the three models that consider the hard constraints on delays produce similar results. The $\ " \mathrm { H A P } / 0 / 0 / 0 / "$ model has the lowest transportation cost but the allocation is made without considering due dates. Due to the small difference between the models “HAP/D/0/0/”, $\ " \mathrm { H A P } / D / 0 / \gamma / "$ , and $\ ^ { \cdot \cdot } \mathrm { H A P } / D / G ^ { \ B } / 0 / ^ { \prime }$ we are inclined to suggest the latter for practical purposes, as the attitude to avoid multiple stops is meant to reduce the possibility of technical problems while docking and to increase security and reliability in the barge transport. Moreover, it is interesting to notice that by trying to follow common guidelines that planners use, namely reducing number of stops or increasing utilization levels, the solutions are at most equal or worse than $\ " \mathrm { H A P } / D / 0 / 0 / "$ . This can show that by scheduling containers according to their locations and by trying to achieve certain targets of the utilization, there is a risk of obtaining more costly schedules.

## 6.3. A planning horizon window optimization

As we are not aware of the exact information that the planner had at the time of his decision, the actual results could be actually better than the ones reported, in the case of complete information. Therefore, the aim of this section is to show how the availability of the information can affect the quality of the schedules.

We present the results for instance 10. We take the earliest time a container is available as point 0 in time. We then make the hypothesis that the planner decides the schedules every Δ hours and that the information covers exclusively the next Δ hours. For instance, when $\Delta = 4 8$ the planner every 48 h makes a decision of the upcoming containers in the system. In the remaining experiments we extend the horizon to 72 h, 96 h and 120 h. We test according to scenario $\mathrm { H A P } / D / 0 / 0 / ;$ the results are shown in Table 8.

In the instances previously shown (Table 4). the information was complete; therefore, the planner is aware of all coming containers. In that case the total cost was €16,940. With a planning horizon window perspective, information is partial and the total cost will always be higher. However, we can notice from the experimentation that, in some cases, shorter time spans can result in better schedules. For instance, a time span of 72 h produces a better schedule than a span of 96 h. This can be explained by the fact that different time spans cut the total information at different points. In the example, the time span of 96 h does not consider containers that are available right after the end of a cut, and that can be successfully bundled with the ones in the range before. Consequently, this can be translated to the fact that the moment when planning is “closed” plays a critical role. In Appendix C, Table C.1, we report the results for the other instances. In general, the largest time span produces better results; however, intermediate ones can again generate ambiguous results as shown for instance 10.

Results for the planning horizon window experimentation, with instance 10.  
Table 8

<table><tr><td>Sub</td><td colspan="4">Information Span 48 h</td><td colspan="4">Information Span 72 h</td><td colspan="4">Information Span 96 h</td><td colspan="4">Information Span 120 h</td></tr><tr><td>Instance</td><td>I</td><td>Value</td><td># B</td><td># T</td><td>I</td><td>Value</td><td># B</td><td># T</td><td>I</td><td>Value</td><td># B</td><td># T</td><td>I</td><td>Value</td><td># B</td><td># T</td></tr><tr><td>1</td><td>3</td><td>1170</td><td>0</td><td>3</td><td>6</td><td>2080</td><td>1</td><td>0</td><td>19</td><td>5100</td><td>2</td><td>2</td><td>31</td><td>6860</td><td>3</td><td>2</td></tr><tr><td>2</td><td>16</td><td>4770</td><td>1</td><td>3</td><td>30</td><td>5090</td><td>2</td><td>3</td><td>23</td><td>4310</td><td>2</td><td>1</td><td>32</td><td>6460</td><td>2</td><td>6</td></tr><tr><td>3</td><td>17</td><td>2830</td><td>1</td><td>3</td><td>7</td><td>2430</td><td>0</td><td>7</td><td>57</td><td>9040</td><td>3</td><td>8</td><td>46</td><td>6470</td><td>3</td><td>1</td></tr><tr><td>4</td><td>6</td><td>2040</td><td>0</td><td>6</td><td>56</td><td>8650</td><td>3</td><td>7</td><td>10</td><td>2080</td><td>1</td><td>0</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>5</td><td>21</td><td>4730</td><td>1</td><td>7</td><td>10</td><td>2080</td><td>1</td><td>0</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>6</td><td>36</td><td>4630</td><td>2</td><td>1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>7</td><td>10</td><td>2080</td><td>1</td><td>0</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total</td><td>109</td><td>22,250</td><td>6</td><td>23</td><td>109</td><td>20,330</td><td>7</td><td>17</td><td>109</td><td>20,530</td><td>8</td><td>11</td><td>109</td><td>19,790</td><td>8</td><td>9</td></tr></table>

Finally, with these experiments, we aim to emphasize that advanced information is crucial to generate good schedules. This implies that information sharing between sea terminals and transport providers must be strengthened. Sea terminals are aware for in advance of incoming vessels, but the data are often shared just a few hours before their arrival. Improving the global information system is necessary to promote multimodality and make it more efficient in such a setting.

## 7. Conclusions

In the last decade, global trade and the movement of large quantities of goods are more and more associated with container supply chains. In some crucial logistic areas of the world, the increase of container flows has generated drawbacks related to $C O _ { 2 }$ emissions, traffic jams around port areas and shortage of capacity. These issues are interrelated. It has been acknowledged that an effective use of high capacity means of transport, as barges, can simultaneously relieve traffic jams [38] and reduce $C O _ { 2 }$ due to intensive trucking [13], limit the need of additional capacity and finally, provide good accessibility to the hinterland of sea ports [37].

In this paper, we developed a DSS that facilitates the creation of schedules for barges by means of a heuristic approach. Planners can set different parameters to drive the decision and create schedules with certain features, such as increasing the level of utilization of barges or reducing the number stops at the quays. In order to assess the performance of the algorithm within the DSS, we compared the results of the system with the schedules generated by the planners. We tested real world instances under four scenarios that showed some features of the planning process. We observed that logistic planners try to avoid routes visiting many quays. As further evidence of this fact, the planners do not often consider the available containers as a whole, but they sort them according to their location and then they make a separate optimization. This evidently leads to fewer chances for bundling and, as a consequence, using barges in a less efficient way.

The contribution of this paper to the literature is twofold. Firstly, the paper gives an emphasis to the full transportation leg and to the importance, from an operational point of view, of certain factors that we showed are accounted for in the planning: due dates, utilization level and number of stops. In fact, most of the literature is focused on empty container management and does not address in detail the complexity of planning for inbound containers. Secondly, we integrate a set of studies on barge transport that focus mainly on strategical and tactical level decisions. In fact, this paper gives an emphasis on the operational aspects and on the complexity of the bundling process when a set of different containers with different needs must be processed. Besides, the paper dovetails with these studies as it provides an additional model that can be implemented with the proposed networks, such as hub-and-spoke

An important issue is the exchange of information between sea ports and inland terminals. It is crucial for transport providers to have advanced and accurate information. Lack of information can result in failing good opportunities for bundling, as a certain utilization level for barges must be reached. Sea terminals should unveil their data earlier, in order to provide accurate information for the planners. Therefore the stakeholders should also consider investments on information systems, data sharing, on-line databases and forecasting systems. Besides, a better coordination between these parties, as also suggested by [9], can be beneficial in terms of water congestion at the sea terminals. In fact, this may lead to routes for barges with fewer stops and less delays, as sea terminals could move in advance cargoes to specific docks. Finally, as the access of sea ports to the hinterland has become a crucial point of competition between ports [37], a smart and quick planning is required to improve performances and flexibility of the transport chain. We believe the proposed DSS is a first step toward an easier, faster and more automatic way to generate schedules for the proposed setting.

## Acknowledgments

This paper is a partial result of the project ULTIMATE (2010-1-012R), which is supported by Dinalog, Dutch Institute for Advanced Logistics, where several companies related to the hinterland transportation of containers were involved, including major terminals in the Port of Rotterdam and Dutch transport providers. We would like to thank Brabant Intermodal for providing the data set and being the subject of this case study.

## Appendix A. Results and statistics for the heuristic on HAP

Table A.1  
Statistics for the different models.

<table><tr><td rowspan="2">Instance</td><td rowspan="2">I</td><td colspan="3">HAP/0/0/0</td><td colspan="3">HAP/D/0/0</td><td colspan="3"> $HAP/D/G^B/0/$ </td><td colspan="3">HAP/D/0/γ/</td></tr><tr><td>Average</td><td>St. dev.</td><td>Time (s)</td><td>Average</td><td>St. dev.</td><td>Time</td><td>Average</td><td>St. dev.</td><td>Time</td><td>Average</td><td>St. dev.</td><td>Time</td></tr><tr><td>1</td><td>28</td><td>3920</td><td>0</td><td>0.1</td><td>3930</td><td>0</td><td>0.1</td><td>3930</td><td>0</td><td>0.1</td><td>3930</td><td>0</td><td>0.1</td></tr><tr><td>2</td><td>41</td><td>6470</td><td>0</td><td>0.1</td><td>8180</td><td>0</td><td>0.43</td><td>8180</td><td>0</td><td>0.1</td><td>8180</td><td>0</td><td>0.1</td></tr><tr><td>3</td><td>42</td><td>6960</td><td>0</td><td>0.1</td><td>13,760</td><td>0</td><td>1.2</td><td>13,760</td><td>0</td><td>0.5</td><td>14,460</td><td>0</td><td>3.1</td></tr><tr><td>4</td><td>47</td><td>7700</td><td>0</td><td>0.1</td><td>12,190</td><td>0</td><td>0.1</td><td>12,190</td><td>0</td><td>0.1</td><td>12,270</td><td>0</td><td>0.1</td></tr><tr><td>5</td><td>47</td><td>6880</td><td>0</td><td>1.1</td><td>12,620</td><td>0</td><td>0.1</td><td>12,620</td><td>0</td><td>0.1</td><td>13,340</td><td>0</td><td>0.1</td></tr><tr><td>6</td><td>50</td><td>7160</td><td>0</td><td>4.1</td><td>12,130</td><td>0</td><td>0.1</td><td>12,130</td><td>0</td><td>0.1</td><td>12,610</td><td>0</td><td>0.1</td></tr><tr><td>7</td><td>58</td><td>8620</td><td>0</td><td>14</td><td>11,370</td><td>0</td><td>4.1</td><td>11,620</td><td>0</td><td>27.7</td><td>11,710</td><td>0</td><td>6</td></tr><tr><td>8</td><td>68</td><td>9900</td><td>0</td><td>19.2</td><td>10,390</td><td>0</td><td>2.3</td><td>10,490</td><td>0</td><td>4.1</td><td>10,390</td><td>0</td><td>0.5</td></tr><tr><td>9</td><td>90</td><td>13,360</td><td>0</td><td>0.2</td><td>16,850</td><td>0</td><td>0.1</td><td>17,030</td><td>0</td><td>6</td><td>17,100</td><td>0</td><td>0.1</td></tr><tr><td>10</td><td>109</td><td>14,316</td><td>178</td><td>35</td><td>17,182</td><td>207</td><td>5.6</td><td>17,142</td><td>156</td><td>17.2</td><td>17,152</td><td>164</td><td>29.8</td></tr></table>

## Appendix B. Heuristic performances against lower bound solutions and assessment of lower bound approximation

Results for HAP/0/0/0/. With “Average †” we calculate the averages considering only the instances for which the optimal solution was found by CPLEX. The gaps are related to the averages of CPLEX. The time limit is set to 14,400 s. CPLEX can stop beforehand in case the optimal solution is found (Best integer(UB) = Best node(LB); if so, both are reported in boldface) or in case of an out-of-memory status. (\*) indicates that the heuristic found an optimal solution. In the column “Heuristic on HAP” we report the results previously shown of the heuristic performed on HAP, in order to assess the quality of the bound.

<table><tr><td rowspan="2">Inst.</td><td rowspan="2">I</td><td colspan="3">CPLEX on the relaxed model</td><td colspan="3">Heuristic on the relaxed model</td><td>Heuristic on HAP</td></tr><tr><td>Best integer</td><td>Best Node</td><td>Time (s)</td><td>Value</td><td>Time</td><td>St. dev.</td><td>Value</td></tr><tr><td>1</td><td>28</td><td>3920</td><td>3920</td><td>1</td><td>3920*</td><td>0.1</td><td>0</td><td>3920</td></tr><tr><td>2</td><td>41</td><td>6470</td><td>6470</td><td>19</td><td>6470*</td><td>0.1</td><td>0</td><td>6470</td></tr><tr><td>3</td><td>42</td><td>6960</td><td>6960</td><td>23</td><td>6960*</td><td>0.1</td><td>0</td><td>6960</td></tr><tr><td>4</td><td>47</td><td>7700</td><td>7700</td><td>31</td><td>7700*</td><td>1.1</td><td>0</td><td>7700</td></tr><tr><td>5</td><td>47</td><td>6880</td><td>6880</td><td>40</td><td>6880*</td><td>0.1</td><td>0</td><td>6880</td></tr><tr><td>6</td><td>50</td><td>7160</td><td>7160</td><td>29</td><td>7160*</td><td>0.1</td><td>0</td><td>7160</td></tr><tr><td>7</td><td>58</td><td>8540</td><td>8540</td><td>80</td><td>8620</td><td>0.1</td><td>0</td><td>8620</td></tr><tr><td>8</td><td>68</td><td>9900</td><td>9900</td><td>3432</td><td>9900*</td><td>2.7</td><td>0</td><td>9900</td></tr><tr><td>9</td><td>90</td><td>13,440</td><td>12,502.5</td><td>6258</td><td>13,360</td><td>1.4</td><td>0</td><td>13,360</td></tr><tr><td>10</td><td>109</td><td>14,150</td><td>13,982.2</td><td>2764</td><td>14,150</td><td>45.5</td><td>121</td><td>14,150</td></tr><tr><td>Average</td><td></td><td></td><td>8401</td><td></td><td>8512 (0.1% gap)</td><td></td><td></td><td>8512 (0.1% gap)</td></tr><tr><td> $Average^†$ </td><td></td><td></td><td>7781</td><td></td><td>7885 (0.1% gap)</td><td></td><td></td><td>7885 (0.1% gap)</td></tr></table>

## Table B.2

Results for HAP/D/0/0/.

<table><tr><td rowspan="2">Inst.</td><td rowspan="2">I</td><td colspan="3">CPLEX on the relaxed model</td><td colspan="3">Heuristic on the relaxed model</td><td>Heuristic on HAP</td></tr><tr><td>Best integer</td><td>Best node</td><td>Time (s)</td><td>Value</td><td>Time</td><td>St. dev.</td><td>Value</td></tr><tr><td>1</td><td>28</td><td>3930</td><td>3930</td><td>1</td><td>3930*</td><td>0.1</td><td>0</td><td>3930</td></tr><tr><td>2</td><td>41</td><td>8030</td><td>8030</td><td>30</td><td>8180</td><td>0.1</td><td>0</td><td>8180</td></tr><tr><td>3</td><td>42</td><td>13,620</td><td>13,620</td><td>3</td><td>13,760</td><td>1</td><td>0</td><td>13,760</td></tr><tr><td>4</td><td>47</td><td>11,610</td><td>11,610</td><td>34</td><td>11,940</td><td>0.1</td><td>0</td><td>12,190</td></tr><tr><td>5</td><td>47</td><td>12,620</td><td>12,620</td><td>18</td><td>12,620*</td><td>0.1</td><td>0</td><td>12,620</td></tr><tr><td>6</td><td>50</td><td>12,130</td><td>12,130</td><td>90</td><td>12,130*</td><td>0.1</td><td>0</td><td>12,130</td></tr><tr><td>7</td><td>58</td><td>10,800</td><td>10,800</td><td>46</td><td>11,210</td><td>1.2</td><td>0</td><td>11,370</td></tr><tr><td>8</td><td>68</td><td>9980</td><td>9980</td><td>45</td><td>10,390</td><td>0.8</td><td>0</td><td>10,390</td></tr><tr><td>9</td><td>90</td><td>16,770</td><td>16,770</td><td>8731</td><td>16,770*</td><td>65</td><td>0</td><td>16,850</td></tr><tr><td>10</td><td>109</td><td>16,780</td><td>15,224</td><td>2221</td><td>15,940</td><td>24</td><td>169.89</td><td>16,940</td></tr><tr><td>Average</td><td></td><td></td><td>11,471</td><td></td><td>11,687 (0.1% gap)</td><td></td><td></td><td>11,836 (3.1% gap)</td></tr><tr><td>Average†</td><td></td><td></td><td>11,054</td><td></td><td>11,214 (0.1% gap)</td><td></td><td></td><td>11,268 (1.9% gap)</td></tr></table>

## Table B.3

Results for HAP/0/G /0/.

<table><tr><td rowspan="2">Inst.</td><td rowspan="2">I</td><td colspan="3">CPLEX on the relaxed model</td><td colspan="3">Heuristic on the relaxed model</td><td>Heuristic on HAP</td></tr><tr><td>Best integer</td><td>Best node</td><td>Time (s)</td><td>Value</td><td>Time</td><td>St. dev.</td><td>Value</td></tr><tr><td>1</td><td>28</td><td>3980</td><td>3980</td><td>2</td><td>3980*</td><td>0.1</td><td>0</td><td>3980</td></tr><tr><td>2</td><td>41</td><td>8430</td><td>8430</td><td>125</td><td>8430*</td><td>0.1</td><td>0</td><td>8430</td></tr><tr><td>3</td><td>42</td><td>13,920</td><td>13,920</td><td>50</td><td>13,920*</td><td>0.1</td><td>0</td><td>14,010</td></tr><tr><td>4</td><td>47</td><td>12,071</td><td>12,071</td><td>112</td><td>12,440</td><td>1.7</td><td>0</td><td>12,640</td></tr><tr><td>5</td><td>47</td><td>12,870</td><td>12,870</td><td>45</td><td>12,870*</td><td>0.1</td><td>0</td><td>12,870</td></tr><tr><td>6</td><td>50</td><td>12,680</td><td>12,680</td><td>28</td><td>12,680*</td><td>1.1</td><td>0</td><td>12,680</td></tr><tr><td>7</td><td>58</td><td>11,400</td><td>11,400</td><td>200</td><td>11,710</td><td>2.3</td><td>0</td><td>12,170</td></tr><tr><td>8</td><td>68</td><td>9980</td><td>9980</td><td>2021</td><td>10,480</td><td>0.1</td><td>0</td><td>10,640</td></tr><tr><td>9</td><td>90</td><td>17,230</td><td>17,230</td><td>5312</td><td>17,410</td><td>43.1</td><td>52</td><td>17,430</td></tr><tr><td>10</td><td>109</td><td>18,590</td><td>15,433</td><td>2703</td><td>16,540</td><td>10.3</td><td>38</td><td>17,880</td></tr><tr><td>Average</td><td></td><td></td><td>11,799</td><td></td><td>12,046 (2% gap)</td><td></td><td></td><td>12,273 (4% gap)</td></tr><tr><td> $Average^†$ </td><td></td><td></td><td>11,395</td><td></td><td>11,546 (1.3% gap)</td><td></td><td></td><td>11,650 (2.2% gap)</td></tr></table>

## Table B.4

Results for HAP/0/0/γ/.

<table><tr><td rowspan="2">Inst.</td><td rowspan="2">I</td><td colspan="3">CPLEX on the relaxed model</td><td colspan="3">Heuristic on the relaxed model</td><td>Heuristic on HAP</td></tr><tr><td>Best integer</td><td>Best node</td><td>Time (s)</td><td>Value</td><td>Time</td><td>St. dev.</td><td>Value</td></tr><tr><td>1</td><td>28</td><td>4230</td><td>4230</td><td>1</td><td>4230*</td><td>0.1</td><td>0</td><td>4241</td></tr><tr><td>2</td><td>41</td><td>8180</td><td>8180</td><td>10</td><td>8180*</td><td>1</td><td>0</td><td>8180</td></tr><tr><td>3</td><td>42</td><td>14,460</td><td>14,460</td><td>23</td><td>14,460*</td><td>0.1</td><td>0</td><td>14,460</td></tr><tr><td>4</td><td>47</td><td>12,321</td><td>12,321</td><td>25</td><td>12,950</td><td>0.5</td><td>0</td><td>13,480</td></tr><tr><td>5</td><td>47</td><td>13,340</td><td>13,340</td><td>34</td><td>13,340*</td><td>0.1</td><td>0</td><td>13,340</td></tr><tr><td>6</td><td>50</td><td>15,110</td><td>15,110</td><td>37</td><td>15,110*</td><td>0.1</td><td>0</td><td>15,118</td></tr><tr><td>7</td><td>58</td><td>11,300</td><td>11,300</td><td>187</td><td>11,820</td><td>1.4</td><td>0</td><td>12,300</td></tr><tr><td>8</td><td>68</td><td>10,280</td><td>10,280</td><td>1036</td><td>10,390</td><td>1.4</td><td>0</td><td>10,390</td></tr><tr><td>9</td><td>90</td><td>16,870</td><td>16,870</td><td>5973</td><td>16,870*</td><td>1.8</td><td>0</td><td>18,270</td></tr><tr><td>10</td><td>109</td><td>17,860</td><td>15,667</td><td>2974</td><td>17,738</td><td>20.5</td><td>32</td><td>18,058</td></tr><tr><td>Average</td><td></td><td></td><td>12,176</td><td></td><td>12,508 (2.7% gap)</td><td></td><td></td><td>12,783 (4.9% gap)</td></tr><tr><td>Average†</td><td></td><td></td><td>11,787</td><td></td><td>11,927 (1.1% gap)</td><td></td><td></td><td>12,197 (3.4% gap)</td></tr></table>

## Appendix C. Planning horizon window

Table C.1  
Results for the planning horizon window experimentation.

<table><tr><td>Inst.</td><td>Information span 48 h</td><td>Inf. span 72 h</td><td>Inf. span 96 h</td><td>Inf. span 120 h</td><td>Complete inf.</td></tr><tr><td>1</td><td>4590</td><td>3930</td><td>3930</td><td>3930</td><td>3930</td></tr><tr><td>2</td><td>9030</td><td>9020</td><td>8180</td><td>8210</td><td>8180</td></tr><tr><td>3</td><td>13,950</td><td>14,010</td><td>13,760</td><td>14,010</td><td>13,760</td></tr><tr><td>4</td><td>15,100</td><td>13,120</td><td>13,020</td><td>12,770</td><td>12,190</td></tr><tr><td>5</td><td>13,780</td><td>13,030</td><td>13,120</td><td>12,620</td><td>12,620</td></tr><tr><td>6</td><td>14,200</td><td>12,960</td><td>13,870</td><td>12,130</td><td>12,130</td></tr><tr><td>7</td><td>12,310</td><td>12,840</td><td>11,900</td><td>11,650</td><td>11,370</td></tr><tr><td>8</td><td>12,620</td><td>11,490</td><td>11,240</td><td>11,560</td><td>10,390</td></tr><tr><td>9</td><td>19,700</td><td>19,290</td><td>18,520</td><td>17,610</td><td>16,850</td></tr><tr><td>10</td><td>22,250</td><td>20,330</td><td>20,530</td><td>19,790</td><td>16,940</td></tr></table>

## References

[1] R. Baldacci, M. Battarra, D. Vigo, Routing a heterogeneous fleet of vehicles, The Vehicle Routing Problem: Latest Advances and New Challenges, Springer 2008, pp. 3–27.

[2] D.L. Bandeira, J.L. Becker, D. Borenstein, D.L. Bandeira, J.L. Becker, D. Borenstein, A dss for integrated distribution of empty and full containers, Decision Support Systems 470 (4) (2009) 383–397.

[3] A. Bovier, M. Eckhoff, V. Gayrard, M. Klein, Metastability in stochastic dynamics of disordered mean-field models, Probability Theory and Related Fields 1190 (1) (2001) 99-161.

[4] A. Caris, C. Macharis, G.K. Janssens, Network analysis of container barge transport in the port of Antwerp by means of simulation, Journal of Transport Geography 190 (1) (2011) 125–133.

[5] H.J. Carlo, I.F.A. Vis, K.J. Roodbergen, Transport operations in container terminals: Literature overview. trends. research directions and classification scheme. European Journal of Operational Research 2360 (1) (2014) 1–13.

[6] C.-F. Chien, J.-F. Deng, A container packing support system for determining and visualizing container packing patterns, Decision Support Systems 370 (1) (2004) 23–34.

[7] N. Christofides, A. Mingozzi, P. Toth, Exact algorithms for the vehicle routing problem, based on spanning tree and shortest path relaxations, Mathematical Programming 200 (1)(1981) 255-282

[8] D.T. Connolly, An improved annealing scheme for the QAP, European Journal of Operational Research 46 (1990) 93–100.

[9] A.M. Douma, J. van Hillegersberg, P.C. Schuur, Design and evaluation of a simulation game to introduce a multi-agent system for barge handling in a seaport, Decision Support Systems 530 (3) (2012) 465–472.

[10] K.A. Dowsland, J.M. Thompson, Simulated annealing, Handbook of Natural Computing, Springer 2012, pp. 1623–1655.

[11] C. Duhamel, C. Gouinaud, P. Lacomme, C. Prodhon, A multi-thread GRASPxELS for the heterogeneous capacitated vehicle routing problem, Hybrid Metaheuristics, Springer 2013, pp. 237–269.

[12] J.C. Fransoo, C.-Y. Lee, The critical role of ocean container transport in global supply chain performance, Production and Operations Management 220 (2) (2013) 253–268.

[13] A. Frémont, P. Franc, Hinterland transportation in Europe: combined transport versus road transport, Journal of Transport Geography 180 (4) (2010) 548–556.

[14] M. Gendreau, G. Laporte, C. Musaraganyi, E.D. Taillard, A tabu search heuristic for the heterogeneous fleet vehicle routing problem, Computers & Operations Research 33 (2006) 595–619.

[15] H.-O. Günther, K.-H. Kim, Container terminals and terminal operations, OR Spectrum 280 (4) (2006) 437–445.

[16] V. Hemmelmayr, V. Schmid, C. Blum, Variable neighbourhood search for the variable sized bin packing problem, Computers & Operations Research 390 (5) (2012) 1097–1108.

[17] A. Hoff, H. Andersson, M. Christiansen, G. Hasle, A. Lokketangen, Industrial aspects and literature survey: fleet composition and routing, Computers & Operations Research 26 (1999)1153-1173

[18] M. Jerrum, A. Sinclair, The Markov chain Monte Carlo method: an approach to approximate counting and integration, Approximation Algorithms for NP-Hard Problems 482–520 (1996).

[19] D.S. Johnson, Fast algorithms for bin packing, Journal of Computer and System Sciences 80 (3) (1974) 272-314

[20] S. Kirkpatrick, C.D. Gelatt, M.P. Vecchi, Optimization by simulated annealing, Science 2200 (4598) (1983) 671–680.

[21] R. Konings, Opportunities to improve container barge handling in the port of Rotterdam from a transport network perspective, Journal of Transport Geography 150 (6) (2007) 443-454

[22] R. Konings, E. Kreutzberger, V. Maraš, Major considerations in developing a huband-spoke network to improve the cost performance of container barge transport in the hinterland: the case of the port of Rotterdam, Journal of Transport Geography 29 (2013) 63–73.

[23] N. Metropolis, A.W. Rosenbluth, M.N. Rosenbluth, A.H. Teller, E. Teller, Equation of state calculations by fast computing machines, The Journal of Chemical Physics 21 (1953) 1087.

[24] K.G. Murty, J. Liu, Y. Wan, R. Linn, A decision support system for operations in a container terminal. Decision Support Systems 390 (3) (2005) 309–332.

[25] E.W.T. Ngai, T.C.E. Cheng, S. Au, K.-H. Lai, Mobile commerce integrated with RFID technology in a container depot, Decision Support Systems 430 (1) (2007) 62–76.

[26] T. Notteboom, Container shipping and ports: an overview, Review of Network Economics 30 (2) (2004)

[27] T. Notteboom, Bundling of freight flows and hinterland network developments, The Future of Intermodal Freight Transport 66 (2008).

[28] T. Notteboom, J.-P. Rodrigue, Port regionalization: towards a new phase in port development, Maritime Policy & Management 320 (3) (2005) 2005–2313.

[29] Havenbedrijf Rotterdam NV. List of Inland Terminalsaccessed July 21st, 2015 a) https://www.inlandlinks.eu/en2015.

[30] Havenbedrijf Rotterdam NV. Port of Rotterdam: Modal Splitaccessed July 21st, 2015 b) https://www.portofrotterdam.com/sites/default/files/Modal itieme2015.

[31] W.S. Shen, C.M. Khoong, A dss for empty container distribution planning, Decision Support Systems 150 (1) (1995) 75–82.

[32] K. Shintani, R. Konings, A. Imai, The impact of foldable containers on container fleet management costs in hinterland transport Transportation Research Part E: Logistics and Transportation Review 460 (5) (2010) 750–763.

[33] D.-P. Song, J.-X. Dong, Empty container repositioning, Handbook of Ocean Container Transport Logistics, Springer 2015, pp. 163–208.

[34] E.D. Taillard, A heuristic column generation method for the heterogeneous fleet VRP, RAIRO — Operations Research 33 (1999) 1–14.

[35] C.D. Tarantilis, C.T. Kiranoudis, V.S. Vassiliadis, A threshold accepting metaheuristic for the heterogeneous fixed fleet vehicle routing problem, European Journal of Operational Research 152 (2004) 148–158.

[36] E. Ursavas, A decision support system for quayside operations in a container terminal Decision Support Systems 59 (2014) 312–324.

[37] M.R. Van Der Horst, P.W. De Langen, Coordination in hinterland transport chains: a major challenge for the seaport community, Maritime Economics & Logistics 100 (1) (2008) 108–129.

[38] W.-J. Van Schijndel, J. Dinwoodie, Congestion and multimodal transport: a survey of cargo transport operators in the Netherlands, Transport Policy 70 (4) (2000) 231–241.

Dr Stefano Fazi, Stefano Fazi is currently appointed as assistant professor at the faculty of Business and Economics at University of Groningen. During his PhD, he was part of the “Ultimate” project promoted by Dinalog. His main findings concern the transportation of containers in the hinterland. From a practical perspective, he developed models and algorithms for decision support systems. Brabant Intermodal, a joint venture of inland terminals, was part of his research.

Prof Jan Fransoo, Jan Fransoo is a Professor of Operations Management and Logistics in the School of Industrial Engineering at Eindhoven University of Technology in the Netherlands, and a member of the research school Beta. He holds an MSc in Industrial Engineering and a PhD in Operations Management & Logistics from Eindhoven University of Technology. Following the completion of his PhD Thesis, he was awarded a fellowship by the Royal Netherlands Academy of Sciences (Akademie-onderzoeker). He specializes in Operations Planning and Supply Chain Management in the process, pharma, food, and retail industries, and recently set up research groups in Supply Chain Carbon Emissions and Supply Chain Finance.

Prof Tom Van Woensel, Tom Van Woensel is Professor of Freight Transport and Logistics at the department of Industrial Engineering and Innovation Sciences at the Technische Universiteit Eindhoven in the Netherlands. He also heads the Smart Logistics Lab, a joint effort of around 15 people doing research in transport and logistics. At the TU/e, Van Woensel is also member of the Strategic Area Smart Mobility. Prof. Van Woensel also serves as Academic Director of the Global Supply Chain Management program at the Antwerp Management School, Belgium. His research is mainly focused on Freight Transport and Logistics.
