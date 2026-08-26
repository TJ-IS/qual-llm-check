---
otero_id: 13428
otero_key: "6NU3KFHD"
title: "A DSS for integrated distribution of empty and full containers"
authors: "Denise Lindstrom Bandeira; João Luiz Becker; Denis Borenstein"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.04.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A DSS for integrated distribution of empty and full containers

Denise Lindstrom Bandeira ⁎, João Luiz Becker, Denis Borenstein

Management School, Federal University of Rio Grande do Sul, R. Washington Luiz 855, Porto Alegre, RS, 90010-460, Brazil

## a r t i c l e i n f o

Article history: Received 5 March 2007 Received in revised form 1 January 2009 Accepted 3 April 2009 Available online 9 April 2009

Keywords: Container Integrated distribution Transshipment Heuristics Decision support system

## a b s t r a c t

A DSS integrating empty and full containers transshipment operations is presented, addressing the typically unbalanced export/import containers trading problem. The problem is modeled as a network, where nodes represent customers, leasing companies, harbors and warehouses, while arcs represent transportation routes. The underlying mathematical model operates in stages, <sup>fi</sup>rst prioritizing and adjusting full containers demands considering available empty containers supplies, and then statically optimizing costs. Transportation routes are registered and dynamically controlled, cyclically, for a given time horizon. The DSS is <sup>fl</sup>exible, allowing several parameters to be con<sup>fi</sup>gured. Experimental examples using randomly generated parameters were conducted to evaluate the effectiveness of the system.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

The container has revolutionized cargo transportation. From the introduction of containers, in the 1960's, containerization has become the most signi<sup>fi</sup>cant mode of merchandise transportation [26]. Containers produced a huge reduction in port and other transfer points handling costs, signi<sup>fi</sup>cantly lowering freight charges. Containerization has made transportation faster and more ef<sup>fi</sup>cient, and has allowed multiple units of cargo to be handled simultaneously. It can be considered one of the most important innovations in freight handling in the 20th century.

Containerization brings several advantages, among which the standardization of loading practices, increased safety, and ease of handling for intermodal transportation. On the other hand, the use of containers involves speci<sup>fi</sup>c problems, such as <sup>fl</sup>eet dimensioning and management, the choice between owning or leasing containers, repositioning of containers that have been released, and container pre-loading preparation. The high cost of container acquisition, maintenance, handling and transportation makes container management a highly relevant problem [7].

Starting in the 1990's, the globalization of world economy has accelerated the containerization of sea trade [4]. Today over 60% of the world's maritime cargo is transported in containers, while some routes among economically strong countries are containerized up to 100% [25]. However, international trade is typically uneven: certain areas are predominantly exporting areas, whereas others are mainly importing areas. This unbalance generates certain logistical challenges to the management of empty containers [12].

Although full containers have allocation priority, empty containers cannot stay idle, as they will be necessary for new shipments. The problem of the dynamic allocation of empty containers lies in reallocating available containers and determining the number of containers to be further leased in order to meet customers demand within a certain period of time [4]. In the case of international maritime shipping companies, this problem arises in the context of the management of land distribution and transportation operations. The problem involves dispatching empty containers in response to requests by export customers, and repositioning other containers to storage depots or harbors in anticipation of future demands [6].

The problem of full containers movements can be treated as a simple transshipment model. In other words, at the moment the harbors of origin and destination are de<sup>fi</sup>ned, the problem is to <sup>fi</sup>nd the most convenient (the least expensive or the shortest time) route between these points. The problem of empty container movement is far more complex, as it involves, besides the movement itself, the dynamic allocation of empty containers to points of merchandise exportation. As a consequence, the challenge is to create a distribution planning that takes into account the integrated <sup>fl</sup>ow of empty and full containers, since both are strongly related.

While the empty and full container distribution planning problems are not new [4–6,11,14–16,17,22–24,27,28] the existing literature has considered the two problems isolated and unconnected from each other. Connecting both problems brings about the issues of reusing containers and allocating empty containers, making the problem far more complex. To the best of our knowledge there is no available optimal solution for the integrated problem of full and empty container distribution and allocation in the literature. Crainic, Gendreau and Dejax [6] state the need for such formulation, but perhaps due to the complexity of the problem no optimal solution was presented so far. Some researchers present mathematical formulations [4,6,16] to solve the empty container problem. Moreover, there are few works approaching normal and reverse distribution simultaneously, with integration of both channels only been considered during the network project stage [9].

A decision support system (DSS) addressing the problem of empty container allocation associated to an ef<sup>fi</sup>cient distribution of full containers is proposed in this paper. Several DSSs have already been developed in the literature to deal with the operations and planning of containers [11,18,19,22]. The DSS is based on a heuristic procedure, as usually done in complex and combinatorial problems [13,14,16,22], being designed to be used by shipping companies to carry out a “good” integrated plan concerning the <sup>fl</sup>ow of full and empty containers. The proposed heuristic adopts a number of operational research methods, more speci<sup>fi</sup>cally a model of static transshipment, with the inclusion of priority and <sup>fl</sup>ow balancing rules seeking the scaling and dynamic integration of the <sup>fl</sup>ow of full and empty containers.

The main contribution of this work is the development of a management procedure for distribution and allocation of full and empty containers, in which the distribution planning is treated in an integrated, systemic, and user-friendly manner.

The work is organized as follows: Section 2 presents the conceptual model concerning allocation and movement of empty and full containers; Section 3 formulates a linear integer programming model for this problem; Section 4 brings a description of the integrated model and procedures for dynamic execution; Section 5 brie<sup>fl</sup>y describes the proposed Decision Support System; Section 6 explores computational experiments; whereas Section 7 concludes the paper, highlighting its contributions.

## 2. The conceptual model

To better describe the integrated model in detail, we turn our attention to the <sup>fl</sup>ow of empty containers (from their unloading on the receivers' premises until they are available again for other customers), and of full containers (from their loading at customers' site until their delivering to receivers). These <sup>fl</sup>ows should be integrated, observing the balancing between normal and reverse <sup>fl</sup>ows.

To represent the movement of containers, empty or full, the routing model was derived from the classic transshipment problem [1]. Containers are not directly sent from origin to destination, as they must circulate through other intermediate points (harbors and warehouses), which also act as storage points, before a container reaches its <sup>fi</sup>nal destination. Empty containers may be shipped from any origin to any destination, according only to the demand at destinations and the supply levels at the origins. The objective of the movement of empty or full containers is to transport them according to the demand in each of the model nodes, aiming at the least possible cost (or time) in global transportation.

The <sup>fl</sup>ows of both full and empty containers are intertwined, though, since a demand for full containers of a certain customer will make this customer to request empty containers from other locations, in case of unavailability. The model of empty containers allocation is embedded in the movement network, where nodes represent demand and supply points, as well as transshipment points (inland depots and harbor depots), while arcs represent paths between these points. The model to allocate empty containers was inspired by the work developed by Crainic et al. [6] with the aim at presenting a better distribution of empty containers to respond to customers' demands at the least possible cost. Dynamic and deterministic, this model considers only one type of container and uses linear cost functions for ownership, replacement, leasing and transportation, disregarding handling costs. The model proposed here includes transportation, storage and handling costs of empty and full 20-foot containers, corresponding to one TEU (Twenty-foot Equivalent Unit).

Movement models for empty and full containers and allocation models for empty containers are integrated in a uni<sup>fi</sup>ed network model, taking into consideration the balance between normal and reverse <sup>fl</sup>ow. The analysis of the network results in a route plan to redistribute containers, satisfying the demand for empty and full containers, minimizing the totals costs of transportation, storage and handling of full and empty containers, from origin to destination, considering the available supply and total demand.

Fig. 1 depicts a schematic and static representation of the conceptual integrated model with the movement network for empty and full containers. Nodes represent customers (suppliers and demanders of empty and full containers), harbors, warehouses and a pool of container leasing companies. Arcs represent possible routes between these entities, which may be terrestrial (trucks or trains) or maritime. Customer representation is decomposed into four nodes, each one representing the different roles played by a customer at different instants of time, namely suppliers of full containers, suppliers of empty containers, demanders of empty containers and demanders of full containers. A particular customer can play several roles during the planning time horizon. Customers can generate demand or supply of both full and empty containers. A given customer's demand for empty containers may be ful<sup>fi</sup>lled by any customer with supply, always through nodes connected to both customers. Harbors and warehouses process and might temporarily store containers in their yards. Direct transportation routes among customers, being unrealistic, are not allowed. The integration of empty and full containers <sup>fl</sup>ows is done in the customers' premises, while stuf<sup>fi</sup>ng containers and unloading cargo from them. The dynamics of such integration is better described in Section 4.2.

![](/api/attachments/6NU3KFHD/fulltext/images/0a3afdc0c7bcb8fe43142ec670a6f13e6a9ac7e644ecd2bc6a0fe8f6ba615015.jpg)  
Fig. 1. Conceptual integrated model.

## 3. Mathematical formulation

Before presenting a mathematical formulation for the problem of empty container allocation associated to an ef<sup>fi</sup>cient distribution of full containers, we introduce some de<sup>fi</sup>nitions and notations. We de<sup>fi</sup>ne the movement of empty containers as usually treated in the literature as a deadheading trip. Consider a given set $L = \{ 1 , 2 , . . . , n \}$ of container loads as well as a set $K = \{ 1 , 2 , . . . , m \}$ of depots in the $k ^ { \mathrm { { t h } } }$ of which $\boldsymbol { v _ { k } }$ containers are stored. Each container load represents a single unit of cargo for which an empty container should be allocated and transported as a full container. Without any loss of generality we will assume that $m \leq n ,$ . For each container load $i \in L$ it is possible to identify its origin and destination as well as its requesting time $o _ { i } .$ For the sake of simplicity, we will assume that the shortest route in the network between any pair of customers can be determined in advance, ignoring network capacities. Let $t _ { i }$ be the transportation time of container load $i \in L$ using the shortest route from its origin to its destination. Let $t t _ { i j }$ be the deadheading transportation time of a container between the destination of container load $i \in L$ and the origin of container load $j { \in } L$ using the shortest route between them. An ordered pair of container loads $( i , j )$ is said to be compatible if and only if they can be transported by the same container (that $\mathrm { i } s , o _ { i } + t _ { i } +$ $t t _ { i j } \le o _ { j } )$ . For each compatible pair of container loads $( i , j ) ,$ , let $e _ { i j }$ be the <sup>fi</sup>nite cost incurred if a container performs container load $j { \in } L$ right after container load $i \in L .$ The problem consists of <sup>fi</sup>nding a minimal cost assignment of container loads to containers in such a way that each container load is covered by exactly one container, each container covers a feasible duty (i.e., a sequence of pairwise compatible container loads), and the number of containers leaving depot $k \in K$ does not exceed $\nu _ { k } ( K { = } 1 , 2 , . . . . , m )$ . This problem can be formulated as the well-known Multiple Depot Vehicle Scheduling Problem [8], in which each vehicle (in this case, container) does not need to return to its original depot. Several authors, including Bertossi et al. [3], Forbes et al. [10], and Ribeiro and Soumis [21] have formulated the MDVSP as an integer multi-commodity network <sup>fl</sup>ow model. We formulate the problem following Pepin et al. [20].

Consider a network $G ^ { k } = ( V ^ { k } , A ^ { k } )$ for each depot $k \in K ,$ where $V ^ { k }$ and $A ^ { k }$ denote its node and arc sets, respectively. Set $V ^ { k }$ contains one node for each container load iaL and a set of pairs of nodes, $o ( k )$ and $d ( k )$ , representing the start and the end of a container schedule associated with depot k. Thus, $V ^ { k } { = } \{ o ( k ) , d ( k ) \} \cup L$ . Set $A ^ { k }$ contains two types of arcs: pull-out, pull-in, and connection arcs. There is a pullout arc $( o ( k ) , i )$ for each container load node iaL. Symmetrically, there is a pull-in arc $( i , d ( k ) )$ for each container load $i \in L .$ . Finally, there is a connection arc $( i , j )$ for each pair of compatible pair of container loads $( i , j ) , i , j \in L$ . The cost of all arcs $( i , d ( k ) ) { \in } A ^ { k }$ is zero, since the container does not need to return to its origin. The cost of an arc $( i , j ) \in$ $A ^ { k } , i , j \in V ^ { k } \backslash \{ d ( k ) \}$ , denoted $e _ { i j } ,$ is equal to the travel and waiting costs associated with it. It is easy to observe that there is a one-to-one correspondence between the paths from $o ( k )$ to $d ( k )$ in $G ^ { k }$ and the feasible container schedules for depot k. In the following, we refer to this type of network as a connection network.

The proposed formulation involves the binary variables $X _ { i j } ^ { k } , ( i , j ) \in$ $A ^ { k } , k \in K$ . Such a variable indicates the <sup>fl</sup>ow of commodity k on the arc (i,j). Using this notation, the problem of allocating containers to container loads can be formulated as follows:

$$
M i n \sum_ {k \in K} \sum_ {(i, j) \in A} e _ {i j} X _ {i j} ^ {k}\tag{1}
$$

St

$$
\sum_ {k \in K} \sum_ {j: (i, j) \in A ^ {k}} X _ {i j} ^ {k} = 1 \quad \text {   for   any   } i \in V ^ {k}\tag{2}
$$

$$
\sum_ {j: (o (k), j) \in A ^ {k}} X _ {o (k) j} ^ {k} \leq v _ {k} \quad \text {   for   any   } k \in K\tag{3}
$$

$$
\sum_ {j: (i, j) \in A ^ {k}} X _ {j i} ^ {k} - \sum_ {j: (i, j) \in A ^ {k}} X _ {i j} ^ {k} = 0 \quad \text { for   any } i \in V ^ {k} \setminus \{o (k), d (k) \}, k \in K\tag{4}
$$

$$
X _ {i j} ^ {k} \in \{0, 1 \} \quad \text {   for   any   } (i, j) \in A ^ {k}, k \in K.\tag{5}
$$

The objective function (1) seeks to minimize deadheading costs. Constraints (2) ensure that each container load is executed exactly once by a container. Constraints (3) limit the number of containers that can be used from each depot, while constraints (4) are <sup>fl</sup>ow conservation constraints which de<sup>fi</sup>ne a multiple-path structure for each depot. Finally, variable binary requirements are provided by Eq. (5).

The MDVSP has been shown NP-hard when m≥2 [3]. Several heuristic methods have been developed to solve this problem. Pepin et al. present a survey of the heuristic and optimization approaches developed. However, the majority of these algorithms are computationally intensive, requiring a lot of CPU time to solve instances involving hundreds of trips and dozen of depots. As a consequence, it is unclear whether they can be directly applied to the problem addressed in this paper, which can involve thousands of trips and hundreds of depots (in our case, ports, warehouses, customers are considered depots). Besides, this formulation and its solution methods are only applied to simpli<sup>fi</sup>ed versions of the container allocation and transportation problem. The given formulation does not take into account important aspects related to container allocation, such as waiting costs and incurred delays due to excessive demands. An alternative method for solving this problem is presented in the next section. Several characteristics of real world problems are considered, optimality being relaxed.

## 4. The network model

In order to overcome the computational dif<sup>fi</sup>culties associated with producing an acceptable solution, we propose to decompose the problem into two interconnected sub-models, namely:

(1) Static model. The static model is responsible for the movement and allocation of full and empty containers, based on the transshipment model formulation, for each instant time t. This model is formulated based on information provided by the dynamic model, concerning on: going and future demands, full and empty container positioning, and full and empty container inventories at each customer.

(2) Dynamic model. Based on the results of the static model, the dynamic model controls and updates the demands and supplies of full containers at future time units. This model also de<sup>fi</sup>nes how the several full containers demands are prioritized, dispatching empty containers in several nodes of the network. The dynamic model is based on heuristic methods.

We <sup>fi</sup>rst introduce some de<sup>fi</sup>nitions and notation to describe the relationship between the two sub-models. At each instant of time t, there are four attributes that need to be controlled in the system: demands and supplies of full and empty containers. Let DF<sup>i</sup> represent the demand of full containers of customer i at time t, DE<sup>i</sup> represent the demand of empty containers of customer i at time t, SF<sup>i</sup> represent the supply of full containers of customer i at time t, and SE<sup>i</sup> represent the supply of empty containers of customer i at time t. It is important to notice that demand of empty containers refers to the need of a customer for a container to be stuffed with goods which are demanded by some other customer. The supply of empty containers, by its turn, refers to the availability of empty containers located in some customer premises and ready to be transported to another customer to be stuffed. The model is integrated by acknowledging that a container unit dynamically changes its status, driven by customers' needs

The dynamics of the model can be explained taking a cycle in a container unit status. Consider an ‘empty’ container unit in customer i premises at time t. This unit adds up to the attribute SE<sub>t</sub><sup>i</sup>. The container might be moved to the premises of another customer to be stuffed, say customer j, ful<sup>fi</sup>lling part of DE<sup>j</sup> (actually DE<sup>j</sup> is determined by the demand of full containers from other customers, represented by attributes $D F _ { t ^ { \prime } } ^ { k }$ , for $k \neq j$ and $t ^ { \prime } \leq t )$ . After some time σ, due to transportation, storing, and stuf<sup>fi</sup>ng, the container is ready to be embarked to some other customer k as a ‘full’ container, adding up to the attribute $S F _ { t + \sigma } ^ { j } .$ After some time λ, due to transportation, storing and unloading, the container changes again its status to ‘empty’, adding up to the attribute $S E _ { t + \sigma + \lambda } ^ { k } .$

The integrated model is solved dynamically in stages. In a given time t, customers' demand of full containers $( D F _ { t } ^ { i } ,$ for $i \in C ,$ C being the set of customers) is checked. As already mentioned, actually the demand is for goods to be transported in containers. The supplier of goods, actually the supplier of full containers (SF <sup>j</sup>, for $i { \in } C )$ in our model, veri<sup>fi</sup>es if they have empty containers available to be stuffed with goods to satisfy the requests, generating, if necessary, demand of empty containers $( D E _ { t } ^ { i } ,$ , for $i \in C )$ . The availability of empty containers (SE<sup>i</sup>, for $i \in C )$ is then veri<sup>fi</sup>ed. Next, the model allocates emptycontainers to be transported from emptycontainer suppliers to emptycontainer demanders in order to meet the demand at the least possible transportation cost. Within the same period, the allocation problems can be represented by traditional transshipment models [1]. The SE<sup>i fl</sup>ow towards DE<sup>j</sup> corresponds to a (static) transshipment problem; from SF<sup>i</sup> to $D _ { } ^ { j } { } _ { t } ,$ the transshipment problem becomes more complex since full containers have predetermined origin and destination. The allocated empty containers will be routed together with full containers, satisfying the transshipment model's constraints and aiming at minimizing the global transportation cost, as well as storage and handling costs. All routes are recorded and will be dynamically controlled in future times $t ^ { \prime } > t$ until the movements are fully accomplished.

After containers are allocated and shipped (at time t), new demand for full containers are incorporated in the model at the next time unit $( t + 1 )$ , which will generate new demand for empty containers, executing the static sub model again, and so on, successively. As soon as full containers are delivered and unloaded or empty containers are delivered and stuffed, changing their status from ‘full’ to ‘empty’ or vice-versa, the demands and supplies of full and empty containers attributes are updated.

In this way, allocation and movement models for empty and full containers have their <sup>fl</sup>ux and behavior uni<sup>fi</sup>ed in a single network and simultaneously dealt with in an integrated manner. Next, each sub model is described in detail.

## 4.1. Description of the static model

An integer linear programming formulation is used to represent the problem of integrated allocation and movement of empty and full containers. The model follows:

## 4.1.1. Parameters

N set of nodes, $N { = } H \cup W \cup S \cup D$

H set of harbors, $H \subset N$

W set of warehouses, $W { \subset } N$

S set of supply customers, $S \subset N$

D set of demand customers, $D \subset N$

$G$ set of arcs, in particular, $( i , i ) \not \in G , \forall i \in N ; ( i , j ) \not \in G ,$ for $i \in S$ and $j \in D$

$e _ { i j }$ the unit empty container transportation cost from node i to node $j , ( i , j ) \in G$

$f _ { i j }$ the unit full container transportation cost from node i to node j, $( i , j ) \in G$

$p _ { i }$ the unit container handling cost in node $i , i { \in } W \cup H$

$a _ { i }$ the unit container storage cost in node $i , i \in W \cup H .$

Costs are speci<sup>fi</sup>c for full and empty containers, although they might have the same value. Processing costs (handling) and storage costs per container are charged at each transshipment point.

$X _ { s }$ the number of empty containers available at customer $s , s { \in } S$

$Z _ { d }$ the number of empty containers required by customer d, $d \in D$

$Y _ { s d }$ the number of full containers required by customer d from customer $s , s \in S , d \in D$

## 4.1.2. Decision variables

The decision variables of the model are the amount of empty and full containers that must be transported in each network arc. The variables referring to full containers keep their addressing tag (initial origin and <sup>fi</sup>nal destination).

$x _ { i j }$ the number of empty containers shipped from node i to node $j , ( i , j ) \in G$

$y _ { i j q r }$ the number of full containers shipped from node i to node j, whose initial origin is q and <sup>fi</sup>nal destination is $r , ( i , j ) \in A , q \in S , r \in D .$

## 4.1.3. Objective function

The objective function to be minimized is the total operation cost of the distribution and transportation of empty and full containers.

$$
\left. \right.\begin{array}{l}\sum_ {s \in S} \sum_ {w \in W} e _ {s w} x _ {s w} + \sum_ {s \in S} \sum_ {h \in H} e _ {s h} x _ {s h} + \sum_ {w \in W} \sum_ {d \in D} (e _ {w d} + p _ {w} + a _ {w}) x _ {w d} + \sum_ {h \in H} \sum_ {d \in D} (e _ {h d} + p _ {h} + a _ {h}) x _ {h d} +\\\sum_ {w \in W} \sum_ {w ^ {\prime} \in W | w \neq w ^ {\prime}} (e _ {w w ^ {\prime}} + p _ {w} + a _ {w}) x _ {w w ^ {\prime}} + \sum_ {w \in W} \sum_ {h \in H} (e _ {w h} + p _ {w} + a _ {w}) x _ {w h} +\\\sum_ {h \in H} \sum_ {h ^ {\prime} \in H | h \neq h ^ {\prime}} (e _ {h h ^ {\prime}} + p _ {h} + a _ {h}) x _ {h h ^ {\prime}} + \sum_ {h \in H} \sum_ {w \in W} (e _ {h w} + p _ {h} + a _ {h}) x _ {h w} +\\\text {Min} \quad \sum_ {q \in S} \sum_ {r \in D} \left[ \sum_ {s \in S} \sum_ {w \in W} f _ {s w} y _ {s w q r} + \sum_ {s \in S} \sum_ {h \in H} f _ {s h} y _ {s h q r} + \sum_ {w \in W} \sum_ {d \in D} (f _ {w d} + p _ {w} + a _ {w}) y _ {w d q r} + \right.\\\left. \sum_ {h \in H} \sum_ {d \in D} (f _ {h d} + p _ {h} + a _ {h}) y _ {h d q r} + \sum_ {w \in W} \sum_ {w ^ {\prime} \in W | w \neq w ^ {\prime}} (f _ {w w ^ {\prime}} + p _ {w} + a _ {w}) y _ {w w ^ {\prime} q r} + \right.\\\left. \sum_ {w \in W} \sum_ {h \in H} (f _ {w h} + p _ {w} + a _ {w}) y _ {w h q r} + \sum_ {h \in H} \sum_ {h ^ {\prime} \in H | h \neq h ^ {\prime}} (f _ {h h ^ {\prime}} + p _ {h} + a _ {h}) y _ {h h ^ {\prime} q r} + \sum_ {h \in H} \sum_ {w \in W} (f _ {h w} + p _ {h} + a _ {h}) y _ {h w q r} ]\right) f u l l\end{array}\tag{6}
$$

The total cost in Eq. (6) was obtained by the sum of the total container movement (empty and full) from supply customers to depots (in harbors or warehouses), from depots to demand customers, and between depots, plus storage and handling costs. Storage and handling costs are charged at the end of each arc (transportation interval).

## 4.1.4. Constraints

Supply constraints are indicated as follows:

$$
\sum_ {j \in W \cup H} x _ {s j} \leq X _ {s} \quad \text { for   any } s \in S\tag{7}
$$

$$
\sum_ {j \in W \cup H} y _ {s j s d} \leq Y _ {s d} \quad \text { for   any } s \in S, d \in D.\tag{8}
$$

Constraint (7) establishes that the shipment of empty containers from each customer (point of origin) to all warehouses and harbors (intermediate destination points) is limited by the number of empty containers available in that customer. Similarly, constraint (8) puts a limit i the shipment of full containers from each customer (note the addressing tag in the variables).

Demand constraints are represented by:

$$
\sum_ {j \in W \cup H} x _ {j d} \geq Z _ {d} \quad \text { for   any } d \in D\tag{9}
$$

$$
\sum_ {j \in W \cup H} y _ {j d s d} \geq Y _ {s d} \quad \text { for   any } d \in D, s \in S.\tag{10}
$$

Constraint (9) ensures that each customer (point of destination) gets at least the required number of empty containers with shipments coming from all warehouses and harbors (intermediate points). Constraint (10) does the same for full containers (note the addressing tag in the variables) Balancing <sup>fl</sup>ows are expressed by:

$$
\sum_ {s \in S} x _ {s j} = \sum_ {d \in D} x _ {j d} \quad \text { for   any } j \in W \cup H\tag{11}
$$

$$
\sum_ {s \in S} y _ {s j s d} = \sum_ {d \in D} y _ {j d s d} \quad \text { for   any } j \in W \cup H.\tag{12}
$$

Those constraints ensure the balancing <sup>fl</sup>ow of all empty containers (11) and all full containers (12) that pass through all warehouses and harbors.

Finally, we must impose that all decision variables are non-negative integers.

$$
x _ {i j} \in \{0, 1, 2, \dots \} \quad \text { for   any } (i, j) \in G\tag{13}
$$

$$
y _ {i j s d} \in \{0, 1, 2, \dots \} \quad \text { for   any } (i, j) \in G, s \in S, d \in D.\tag{14}
$$

Let |N| be the cardinality of the set N; the quantity of variables of the static ILP formulation is given by the expression $( | W | + | H | ) [ ( | W | + | H | + 1 )$ $( | S | | D | + 1 ) + | S | + | D | - 2 ]$ . The number of constraints is given by $( | W | + | H | ) ( | S | | D | + 1 ) + 2 | S | | D | + | S | + | D |$ . See Appendix A for details

## 4.2. Description of the dynamic model

While modeling static allocation of containers is somehow straightforward, since it ignores the elapsed time spent in transportation, dynamic implementation poses a more dif<sup>fi</sup>cult task, as it requires that demands and supplies of containers are updated, balanced and transferred to future time units, actually taking into account transportation times between nodes. In this way the static and dynamic stages are interconnected, as described in the beginning of Section 4. Besides, as time goes by new transportation orders might arrive from customers, adding complexity to the model. One of the <sup>fi</sup>rst noticeable consequences of the passage from a static to a dynamic framework is the emergence of backlogs, as it is usually the case in complex scheduling problems. In our case empty and full containers are routed together in the static model (6)–(14), and full containers must actually be stuffed before being shipped, using empty containers that might still be in transit from other nodes. As optima solutions for problems with such degree of complexity are virtually impossible to get, heuristic procedures were used to accomplish the task.

## 4.3. Heuristic solution procedures

Real life container transportation problems are typically unbalanced — total amounts of supply and demands are normally uneven — which might make the static model (6)–(14) unfeasible. In order to avoid infeasibility, at each time period t, it is necessary to adjust demand and supply of both empty and full containers. There is no way of achieving that unless postponing some demands to the next time period unit (t+1). The major problem is to decide which of these demands from the total set should be postponed. Prioritization was performed following heuristic procedures for each type of demand.

## 4.3.1. Full container demand prioritization

Establishing priorities to satisfy backlogs was one of the main challenges faced during the phase of system development and testing. Here we must achieve an adequate balance between cost minimization and quality in service, measured by the difference between the time of request and the actual arrival of an empty container (to be stuffed). As unful<sup>fi</sup>lled orders are postponed, they will compete with future arriving orders for scheduling. Simply prioritizing older demands will make the solution above optimum (in terms of cost minimization), new orders will be temporarily neglected, and new backlogs might appear. Not prioritizing older demands might keep total cost at its minimum but those demands might never be scheduled, damaging the level of service. Therefore, the heuristic procedures used in the system focused primarily on cost minimization, although not ignoring the service level.

For each transportation order a lexicographic decision rule with the following criteria of demand priority is used:

(1) Original date of order (ODD) — older orders have priority, since successive postponements jeopardize the service level;

(2) Estimated transportation cost (ETC) — orders with lower estimated transportation cost between origin and destination have priority, since the main goal is cost reduction;

(3) Estimated transportation time (ETT) — orders with lower estimated transportation time between origin and destination have priority, since SPT (Shortest Processing Time) rule is optimal to minimize <sup>fl</sup>ow.

The unful<sup>fi</sup>lled demand is passed over to the next time unit.

Estimated transportation costs and times used in ETC and ETTabove are taken as the shortest routes between any pair of customers, either considering cost or time as minimization criterion, respectively. Actual costs and times will be known only after transportation routes are actually determined.

When rules ETC or ETT are used to prioritize full container demands for a pair of customers, the computed shortest route is <sup>fi</sup>xed as the only possible path for that pair. As a consequence, the number of variables and constraints in the static model is reduced, reducing the space of possible solutions and thus reducing the solution time of the linear programming formulation. For instance, in a problem composed of 20 customers, 8 depots, 50 time units horizon example, we achieved a <sup>fi</sup>ve fold reduction (30,000 to 6200 variables and 4000 to 800 constraints).

## 4.3.2. Empty container demand prioritization

It is not possible to apply the same priority rule used for full containers (lower cost or lower time) to empty containers, since there are no pre established paths (origins and destinations) to be analyzed. The criterion of prioritizing higher demands was chosen. The unful<sup>fi</sup>lled demand fo empty containers at a given time will be incorporated to the demand in the next time unit, when the demand is recalculated by adding new customer needs, and subtracting the amount of full and empty containers that are about to arrive (the look ahead window is a parameter set by the user). This method also seems adequate, yielding a fair ful<sup>fi</sup>llment of demands among customers.

## 4.4. Solution procedures of the integrated model

The scheme used to incorporate the “time” factor in the model is to decompose the problem in stages, connecting its results, according to the steps described in Fig. 2.

Step 2 in Fig. 2 performs a resource balancing, in a static way, analyzing the demands with respect to the available supplies in each unit, reevaluating the transshipment node capacities and prioritizing service quality. From the demands and supplies resulting from Step 2, Step 3 allocates the empty and full containers, in a static way, prioritizing the minimal cost using a routing problem solution. Step 4 follows the obtained routes in Step 3, also controlling the utilization from the warehouses storage capacity. After Step 5, the model returns to Step 2 to process the next time unit, and so on, until the informed time horizon $\left( t _ { \operatorname* { m a x } } \right)$ is reached.

## 5. The decision support system

The DSS is an integrated prototype software designed to run in a PC environment under Microsoft® Windows. The software system uses several programming languages. Lindo® is used as the integer programming solver. An executable model was developed to represent the different entities and their interaction. Microsoft® Access was used for the database and VBA (Visual Basic for Applications) for procedures, interacting with Lindo® API (Application Programming Interface). Fig. 3 depicts the main components of the DSS.

The model was developed aiming at great <sup>fl</sup>exibility, with the highest possible number of parameters, therefore making it easy to perform sensitivity analysis. Table 1 shows the principal entities of the database model and their attributes and parameters. Additionally, there are a number of globally de<sup>fi</sup>ned parameters, such as time horizon, look ahead time (checking future arrivals of full containers before requesting empty containers), option of leasing utilization, and leasing triggering (time delay of unful<sup>fi</sup>lled demand for empty containers).

Notice that changes in one or more of these parameters affect the dynamics of the whole system. Brie<sup>fl</sup>y stated, the input of the DSS is composed of information about customers, depots, leasing companies, <sup>fl</sup>ows, full containers demands and containers supply. Output comprises container's routes, customers, depots and leasing operations statistics, and the cost of operations (transportation, handling and storage) for full and empty containers.

![](/api/attachments/6NU3KFHD/fulltext/images/716c68a7790cd112dcf109bebaebbacdfcd7885b4899ae8f0dbc180ded01b4f7.jpg)  
Fig. 2. Integrated model solution algorithm.

## 6. Computational experiments

A case study illustrates the potentiality of the DSS developed. The main objective of the case study is to demonstrate the DSS capabilities as an effective and ef<sup>fi</sup>cient operational planning tool for shipping line companies.

The examples depicted here are all related to a case of four depots (inland and harbor). Data representing demand of full containers were randomly generated using a multilevel scheme using Bernoulli and Uniform distributions. Given a set of customers, it is possible to gather past data consisting of a sequence of numbers along time for each ordered pair of customers, representing the actual demand for full containers between that pair of customers. Let $d _ { i j t }$ represent the actual demand for full containers from customer i to customer j (i≠j) at time t. A sequence of matrices of zeros and ones can be generated, representing the existence of a request of full containers between i and j at time t, say $e _ { i j t } .$ That is, $e _ { i j t } { = } 1 \mathrm { i f } d _ { i j t } { > } 0 ,$ and $e _ { i j t } { = } 0 \operatorname { i f } d _ { i j t } { = } 0 .$ . Time averaging $e _ { i j t }$ will produce a fair estimate of the probability of the existence of a non zero demand of full containers from a particular customer (origin) to a particular other customer (destination) in a particular time unit. Let $\begin{array} { r } { p _ { i j } = \frac { 1 } { n } \displaystyle \sum _ { t = 1 } ^ { n } } \end{array}$ e<sub>ijt</sub> represent such estimate, where n represents the number of time units in the database. In our case study we arbitrarily used a randomly generated U(0,0.2) distribution. That is, for each ordered pair of customers $( i , j ) , i \neq j ,$ we set the probability of having a request of full containers from i to j, $p _ { i j } ,$ such that $p _ { i j } { \sim } U ( 0 , 0 . 2 )$ . Although it is possible to recognize some dependencies among these probabilities in a realistic setting, which is far beyond the scope of this paper, here we just assumed independency among different $p _ { i j } .$ Using matrix $P \left( p _ { i j } \right)$ , we simulated the existence of non zero demands for full containers from i to j for any particular time unit simply generating a Bernoulli distribution with parameter $p _ { i j } .$ Given that there is a request for full containers from i to j at a given time unit (i.e. given that the value of the simulated Bernoulli variable equals one), one can simulate the amount of full containers requested using any distribution that <sup>fi</sup>ts the data in matrices $d _ { i j t } .$ Here, for the sake of simplicity, we just used independent Discrete Uniform distributions, with different parameters for each ordered pair of customers.

![](/api/attachments/6NU3KFHD/fulltext/images/67a8ebea9c9c180287095300ce6a03aa76bd97747d6e76ec48017faf35aaee87.jpg)  
Fig. 3. DSS architecture.

Entities and their attributes and parameters.

<table><tr><td>Entity</td><td>Attributes and parameters</td></tr><tr><td>Customer</td><td>Container stuffing timeContainer emptying timeMinimum number of empty containers to be kept on premisesAdditional number of containers to be added to each empty container request</td></tr><tr><td>Depot</td><td>Number of full and empty containers at each periodStorage capacityContainer handling times (loading and unloading)Estimated container storage time (maximum and minimum)Unit handling costUnit storage cost</td></tr><tr><td>Flow</td><td>Estimated transportation time at each arc in the networkUnit transportation cost at each arc in the network</td></tr><tr><td>Demand</td><td>Requested quantityRequest timeOrder fulfillment timeEmpty container supply customerFull container supply and demand customers</td></tr><tr><td>Route</td><td>Origin customerDestination customerContainer type (empty or full)QuantityInitial operation timeCumulative handling and storage times and costs</td></tr><tr><td>Leasing company</td><td>Number of containers available at each timeUnit leasing cost</td></tr><tr><td>Leasing operation</td><td>Leasing companyRequest timeTime for returning leased containers (minimum and maximum)Number of leased containersNumber of returned containersEffective end of operation</td></tr></table>

The transportation time between two distinct nodes in the network was <sup>fi</sup>xed as 3 time units. Customer orders were dispatched as soon as possible, even partially, if not enough containers was available. The handling time of an order (including the storage of a container in any transshipment point, and the loading and unloading of a container in a ship) was <sup>fi</sup>xed at 1 time unit. Transportation costs, handling costs and storage costs per container were <sup>fi</sup>xed at \$ 5.00, \$ 3.00 and \$ 2.00, respectively. For simplicity, we consider in<sup>fi</sup>nite capacities for vessels and inland and outland harbors.

The main focus of analysis is on the required number of containers that the shipping line should have (we do not consider here the possibility of leasing) to attend a stochastic demand with a good compromise between operational costs and service level to customers. Eight discrete alternatives for the number of containers (NC) were analyzed (NC in {48, 72, 96, 120, 144, 168, 192, 216}). Since decision analysis is concerned with an uncertain future, there might be some variations in relevant parametric values of the system. Sensitivity analyses of these decision parameters are indispensable during the choice phase, as they will provide the decision makers with valuable information about the system performance under different operational contexts. This study considered two factors as follows: (i) the impact of different number of clients in the system (three conditions were analyzed, 4, 6, and 8 clients); and (ii) the effect of different order sizes, modeled as three IID discrete uniform distributions, namely DU(1,3), DU(2,6), and DU(3,9). Therefore, considering all different levels, 72 (8×3×3) different scenarios were modeled and analyzed. As the DSS incorporates graphical facilities for the creation of different decision scenarios, it was relatively easy to create them.

Although we do not claim that ODD priority rule (see Section 4.3.1) is the most suitable for any case, running tests (see Appendix B) have shown that it seems adequate, providing a satisfying compromise between cost and service level.

To evaluate the scenarios, we used the following performance measures related to operational costs and customers' service level: total transportation costs, segmented in full and empty container transportation costs, full order lead times, weighted average order response lateness (WRL), and container utilization. As each order (with size O ) might be ful<sup>fi</sup>lled partially in lots (with sizes $L _ { i j } ,$ where $O _ { i } = \sum _ { i } L _ { i j } )$ as

free containers become available, we de<sup>fi</sup>ne WRL of order i as follows:

$$
W R L _ {i} = \frac {\sum_ {j} T D _ {i j} L _ {i j}}{O _ {i}} - T O _ {i}
$$

where $T D _ { i j }$ is the dispatching time of $L _ { i j } ,$ and $T O _ { i }$ is the placement time of order i. This measure does not contemplate transportation times, as they are constant between any two nodes of the network. It evaluates the impact of the lack of empty containers in the service level of the company. Container utilization refers to the proportion of time that the container is loaded with cargo. For each scenario,10 replications of length 50 weeks (time units) were run, roughly representing one year of continuous operation. Data were collected until all demands generated within the 50 weeks were ful<sup>fi</sup>lled. The actual simulation length depends on the relation between total demand and the number of containers in the system. Some experiments took over 300 time periods to terminate. Common random numbers were used to reduce variance while maintaining batch independence [15]. Additionally, it was assumed that at the start of the simulation of all scenarios, the containers were empty and equally distributed among customers, and there were no backlog orders in the system.

Table 2 summarizes the results obtained for each scenario. As a consequence of the current limitation of the integrated model of considering in<sup>fi</sup>nite capacities for vessels and inland and outland harbors, and the use of constant traveling time between two nodes of the network, lead time and WRL are highly correlated $( r = 0 . 9 9 9 9 6 )$ Thus, lead time will not be further considered on our analysis.

As expected, our results show that the dynamic behavior of the system is highly affected by all analysis variables and parameters. All performance variables suffer great variability as the system becomes more complex in terms of the number of clients and the average container size of each order. For instance, as the number of containers increases from 48 to 216, WRL decreases from 20.4 weeks to 0.9 weeks, from 71.2 weeks to 3.5 weeks, and from 162.7 weeks to 21.7 weeks, considering the highest average demand size analyzed (DU(3,9)), and the number of customers equal to 4, 6, and 8 respectively (scenarios 3 and 24; 27 and 48; and 51 and 72 in Table 2). Fixing the number of containers and customers in a pairwise comparison, the total transportation costs increases 117.74% on average when the average demand size increases from 2 to 4 (DU(1,3) and DU(2,6), respectively), and 52.01%, when the average demand increases from 4 to 6 (DU(2,6) to DU(3,9)), considering all replications of all scenarios. The increases in container utilization are 62.60% and 19.72%, for the correspondent situations. Pairing the replications <sup>fi</sup>xing all parameters but the number of customers, gives us an average increase in the total transportation costs of 159.26% and 89.83%, when the number of customers changes from 4 to 6 and from 6 to 8, respectively, while container utilization correspondently increases on average 93.89% and 32.81%. These examples, although simple, illustrate the importance of having available a reasonable sophisticated tool to predict the dynamic behavior of such systems, justifying its development.

Table 2 Experimental results (for 50 time units).

<table><tr><td>Scenario</td><td># of customers</td><td>Order size</td><td># of containers</td><td>Full container transportation cost</td><td>Empty container transportation cost</td><td>Total cost</td><td>Full order lead time</td><td>WRL</td><td>Container utilization</td></tr><tr><td>1</td><td>4</td><td>2</td><td>48</td><td>1124</td><td>158</td><td>1282</td><td>11.7</td><td>1.5</td><td>0.36</td></tr><tr><td>2</td><td>4</td><td>4</td><td>48</td><td>2298</td><td>589</td><td>2887</td><td>18.7</td><td>8.0</td><td>0.60</td></tr><tr><td>3</td><td>4</td><td>6</td><td>48</td><td>3375</td><td>830</td><td>4205</td><td>32.5</td><td>20.4</td><td>0.67</td></tr><tr><td>4</td><td>4</td><td>2</td><td>72</td><td>1146</td><td>48</td><td>1194</td><td>10.5</td><td>0.4</td><td>0.28</td></tr><tr><td>5</td><td>4</td><td>4</td><td>72</td><td>2302</td><td>539</td><td>2841</td><td>13.2</td><td>3.0</td><td>0.50</td></tr><tr><td>6</td><td>4</td><td>6</td><td>72</td><td>3492</td><td>821</td><td>4313</td><td>18.6</td><td>7.6</td><td>0.62</td></tr><tr><td>7</td><td>4</td><td>2</td><td>96</td><td>1152</td><td>44</td><td>1196</td><td>10.5</td><td>0.4</td><td>0.17</td></tr><tr><td>8</td><td>4</td><td>4</td><td>96</td><td>2258</td><td>430</td><td>2688</td><td>12.3</td><td>1.9</td><td>0.37</td></tr><tr><td>9</td><td>4</td><td>6</td><td>96</td><td>3478</td><td>918</td><td>4396</td><td>15.0</td><td>4.3</td><td>0.51</td></tr><tr><td>10</td><td>4</td><td>2</td><td>120</td><td>1181</td><td>0</td><td>1181</td><td>10.0</td><td>0.0</td><td>0.20</td></tr><tr><td>11</td><td>4</td><td>4</td><td>120</td><td>2307</td><td>442</td><td>2749</td><td>12.4</td><td>1.9</td><td>0.29</td></tr><tr><td>12</td><td>4</td><td>6</td><td>120</td><td>3367</td><td>560</td><td>3927</td><td>12.1</td><td>1.8</td><td>0.43</td></tr><tr><td>13</td><td>4</td><td>2</td><td>144</td><td>1089</td><td>9</td><td>1098</td><td>10.1</td><td>0.1</td><td>0.11</td></tr><tr><td>14</td><td>4</td><td>4</td><td>144</td><td>2362</td><td>196</td><td>2558</td><td>11.2</td><td>0.9</td><td>0.26</td></tr><tr><td>15</td><td>4</td><td>6</td><td>144</td><td>3506</td><td>776</td><td>4282</td><td>12.7</td><td>2.3</td><td>0.37</td></tr><tr><td>16</td><td>4</td><td>2</td><td>168</td><td>1125</td><td>0</td><td>1125</td><td>10.0</td><td>0.0</td><td>0.12</td></tr><tr><td>17</td><td>4</td><td>4</td><td>168</td><td>2197</td><td>179</td><td>2376</td><td>11.0</td><td>0.8</td><td>0.22</td></tr><tr><td>18</td><td>4</td><td>6</td><td>168</td><td>3100</td><td>405</td><td>3505</td><td>11.8</td><td>1.4</td><td>0.28</td></tr><tr><td>19</td><td>4</td><td>2</td><td>192</td><td>1157</td><td>0</td><td>1157</td><td>10.0</td><td>0.0</td><td>0.10</td></tr><tr><td>20</td><td>4</td><td>4</td><td>192</td><td>2666</td><td>108</td><td>2774</td><td>10.5</td><td>0.4</td><td>0.23</td></tr><tr><td>21</td><td>4</td><td>6</td><td>192</td><td>3567</td><td>154</td><td>3721</td><td>10.7</td><td>0.5</td><td>0.28</td></tr><tr><td>22</td><td>4</td><td>2</td><td>216</td><td>1068</td><td>0</td><td>1068</td><td>10.0</td><td>0.0</td><td>0.10</td></tr><tr><td>23</td><td>4</td><td>4</td><td>216</td><td>2142</td><td>83</td><td>2225</td><td>10.5</td><td>0.4</td><td>0.15</td></tr><tr><td>24</td><td>4</td><td>6</td><td>216</td><td>3130</td><td>235</td><td>3365</td><td>11.1</td><td>0.9</td><td>0.23</td></tr><tr><td>25</td><td>6</td><td>2</td><td>48</td><td>2819</td><td>625</td><td>3444</td><td>23.2</td><td>12.7</td><td>0.68</td></tr><tr><td>26</td><td>6</td><td>4</td><td>48</td><td>5899</td><td>1047</td><td>6946</td><td>57.3</td><td>45.3</td><td>0.74</td></tr><tr><td>27</td><td>6</td><td>6</td><td>48</td><td>7933</td><td>1705</td><td>9638</td><td>85.2</td><td>71.2</td><td>0.74</td></tr><tr><td>28</td><td>6</td><td>2</td><td>72</td><td>2762</td><td>586</td><td>3348</td><td>13.9</td><td>3.6</td><td>0.56</td></tr><tr><td>29</td><td>6</td><td>4</td><td>72</td><td>5716</td><td>976</td><td>6692</td><td>32.9</td><td>21.6</td><td>0.69</td></tr><tr><td>30</td><td>6</td><td>6</td><td>72</td><td>8789</td><td>1593</td><td>10,382</td><td>57.9</td><td>45.3</td><td>0.72</td></tr><tr><td>31</td><td>6</td><td>2</td><td>96</td><td>2725</td><td>455</td><td>3180</td><td>12.3</td><td>2.0</td><td>0.44</td></tr><tr><td>32</td><td>6</td><td>4</td><td>96</td><td>5451</td><td>1309</td><td>6760</td><td>22.7</td><td>11.7</td><td>0.63</td></tr><tr><td>33</td><td>6</td><td>6</td><td>96</td><td>8229</td><td>1658</td><td>9887</td><td>37.0</td><td>25.6</td><td>0.71</td></tr><tr><td>34</td><td>6</td><td>2</td><td>120</td><td>2665</td><td>296</td><td>2961</td><td>11.5</td><td>1.3</td><td>0.34</td></tr><tr><td>35</td><td>6</td><td>4</td><td>120</td><td>5841</td><td>1337</td><td>7178</td><td>17.0</td><td>6.3</td><td>0.61</td></tr><tr><td>36</td><td>6</td><td>6</td><td>120</td><td>8674</td><td>1734</td><td>10,408</td><td>29.0</td><td>17.8</td><td>0.69</td></tr><tr><td>37</td><td>6</td><td>2</td><td>144</td><td>2858</td><td>187</td><td>3045</td><td>10.9</td><td>0.8</td><td>0.30</td></tr><tr><td>38</td><td>6</td><td>4</td><td>144</td><td>5634</td><td>1353</td><td>6987</td><td>14.8</td><td>4.3</td><td>0.54</td></tr><tr><td>39</td><td>6</td><td>6</td><td>144</td><td>8540</td><td>1788</td><td>10,328</td><td>22.5</td><td>11.7</td><td>0.66</td></tr><tr><td>40</td><td>6</td><td>2</td><td>168</td><td>2805</td><td>84</td><td>2889</td><td>10.5</td><td>0.4</td><td>0.26</td></tr><tr><td>41</td><td>6</td><td>4</td><td>168</td><td>5370</td><td>976</td><td>6346</td><td>12.7</td><td>2.3</td><td>0.48</td></tr><tr><td>42</td><td>6</td><td>6</td><td>168</td><td>8471</td><td>1615</td><td>10,086</td><td>17.6</td><td>7.0</td><td>0.64</td></tr><tr><td>43</td><td>6</td><td>2</td><td>192</td><td>2731</td><td>46</td><td>2777</td><td>10.3</td><td>0.2</td><td>0.22</td></tr><tr><td>44</td><td>6</td><td>4</td><td>192</td><td>5865</td><td>891</td><td>6756</td><td>12.4</td><td>1.9</td><td>0.47</td></tr><tr><td>45</td><td>6</td><td>6</td><td>192</td><td>8567</td><td>1859</td><td>10,426</td><td>16.1</td><td>5.5</td><td>0.59</td></tr><tr><td>46</td><td>6</td><td>2</td><td>216</td><td>2744</td><td>33</td><td>2777</td><td>10.2</td><td>0.1</td><td>0.20</td></tr><tr><td>47</td><td>6</td><td>4</td><td>216</td><td>5703</td><td>637</td><td>6340</td><td>11.7</td><td>1.3</td><td>0.40</td></tr><tr><td>48</td><td>6</td><td>6</td><td>216</td><td>8226</td><td>1734</td><td>9960</td><td>13.9</td><td>3.5</td><td>0.56</td></tr><tr><td>49</td><td>8</td><td>2</td><td>48</td><td>5242</td><td>906</td><td>6148</td><td>48.5</td><td>37.3</td><td>0.72</td></tr><tr><td>50</td><td>8</td><td>4</td><td>48</td><td>11,099</td><td>1674</td><td>12,773</td><td>121.2</td><td>105.9</td><td>0.79</td></tr><tr><td>51</td><td>8</td><td>6</td><td>48</td><td>15,904</td><td>2378</td><td>18,282</td><td>179.8</td><td>162.7</td><td>0.78</td></tr><tr><td>52</td><td>8</td><td>2</td><td>72</td><td>5163</td><td>848</td><td>6011</td><td>27.0</td><td>16.6</td><td>0.70</td></tr><tr><td>53</td><td>8</td><td>4</td><td>72</td><td>10,473</td><td>1671</td><td>12,144</td><td>70.6</td><td>57.6</td><td>0.77</td></tr><tr><td>54</td><td>8</td><td>6</td><td>72</td><td>15,304</td><td>2600</td><td>17,904</td><td>108.6</td><td>95.0</td><td>0.78</td></tr><tr><td>55</td><td>8</td><td>2</td><td>96</td><td>5547</td><td>940</td><td>6487</td><td>20.4</td><td>9.9</td><td>0.67</td></tr><tr><td>56</td><td>8</td><td>4</td><td>96</td><td>10,363</td><td>1702</td><td>12,065</td><td>48.3</td><td>36.6</td><td>0.72</td></tr><tr><td>57</td><td>8</td><td>6</td><td>96</td><td>16,685</td><td>2571</td><td>19,256</td><td>84.5</td><td>71.7</td><td>0.78</td></tr><tr><td>58</td><td>8</td><td>2</td><td>120</td><td>5323</td><td>947</td><td>6270</td><td>14.7</td><td>4.4</td><td>0.60</td></tr><tr><td>59</td><td>8</td><td>4</td><td>120</td><td>10,802</td><td>1629</td><td>12,431</td><td>37.8</td><td>26.5</td><td>0.70</td></tr><tr><td>60</td><td>8</td><td>6</td><td>120</td><td>15,943</td><td>2747</td><td>18,690</td><td>62.9</td><td>50.6</td><td>0.74</td></tr><tr><td>61</td><td>8</td><td>2</td><td>144</td><td>5039</td><td>865</td><td>5904</td><td>12.6</td><td>2.4</td><td>0.52</td></tr><tr><td>62</td><td>8</td><td>4</td><td>144</td><td>9747</td><td>1774</td><td>11,521</td><td>26.8</td><td>15.8</td><td>0.69</td></tr><tr><td>63</td><td>8</td><td>6</td><td>144</td><td>16,757</td><td>2663</td><td>19,420</td><td>52.6</td><td>40.7</td><td>0.74</td></tr><tr><td>64</td><td>8</td><td>2</td><td>168</td><td>5276</td><td>680</td><td>5956</td><td>12.0</td><td>1.7</td><td>0.48</td></tr><tr><td>65</td><td>8</td><td>4</td><td>168</td><td>10,776</td><td>1949</td><td>12,725</td><td>23.7</td><td>13.2</td><td>0.68</td></tr><tr><td>66</td><td>8</td><td>6</td><td>168</td><td>17,119</td><td>2386</td><td>19,505</td><td>44.5</td><td>32.8</td><td>0.73</td></tr><tr><td>67</td><td>8</td><td>2</td><td>192</td><td>5115</td><td>549</td><td>5664</td><td>11.6</td><td>1.3</td><td>0.39</td></tr><tr><td>68</td><td>8</td><td>4</td><td>192</td><td>10,055</td><td>1809</td><td>11,864</td><td>18.0</td><td>7.5</td><td>0.65</td></tr><tr><td>69</td><td>8</td><td>6</td><td>192</td><td>16,786</td><td>2503</td><td>19,289</td><td>35.6</td><td>24.4</td><td>0.73</td></tr><tr><td>70</td><td>8</td><td>2</td><td>216</td><td>5325</td><td>491</td><td>5816</td><td>11.4</td><td>1.1</td><td>0.35</td></tr><tr><td>71</td><td>8</td><td>4</td><td>216</td><td>10,773</td><td>2208</td><td>12,981</td><td>17.6</td><td>7.0</td><td>0.62</td></tr><tr><td>72</td><td>8</td><td>6</td><td>216</td><td>17,648</td><td>2579</td><td>20,227</td><td>33.0</td><td>21.7</td><td>0.71</td></tr></table>

![](/api/attachments/6NU3KFHD/fulltext/images/6cc46581bc7aed5329fbc65d5a441ed8ff87b464ad06072cf5ab301d41eef7f3.jpg)  
Fig. 4. Transportation costs.

The analysis is now focused on the main objective of the case study, the de<sup>fi</sup>nition of the number of containers. Table 2 presents the behavior of the average performance measurements over the discrete number of containers analyzed. The average total transportation cost is virtually insensitive to variations in the number of containers in the system, which might be surprising (see Fig. 4). Although the transportation cost of empty containers slightly declines as the number of containers in the system increases, this is compensated by a slight increase in the transportation cost of full containers. Additionally, keeping all other parameters <sup>fi</sup>xed, transportation cost of empty containers should decrease to zero as the number of containers increases inde<sup>fi</sup>nitely, and the system becomes so unrestrained that there is no need to transport empty containers. In the limit, demand and supply become so unbalanced that there is no need to transport empty containers. This is con<sup>fi</sup>rmed in our study: additional experiments runwith thousands of containers led to zero empty container transportation costs. This by its turn indicates that full container transportation cost should have an asymptotic behavior as the number of containers in the system increases, as well as the total transportation cost. Therefore the gap between the corresponding lines in the graph could be used as a measure of the looseness of the system.

On the other hand, looseness is better represented by the container utilization ratio. As expected, this ratio decreases as the number of containers in the system increases (see Fig. 5). From a managerial perspective, this measure is also a measure of ef<sup>fi</sup>ciency, the decision maker wishing to get marks as high as possible. Thus, a manager looking for ef<sup>fi</sup>ciency wouldn't hesitate in choosing 48 containers as the best solution in the case study.

However, wise managers would balance service level against ef<sup>fi</sup>ciency to take decisions. The graph in Fig. 6 shows the system poor average performance on WRL when only 48 containers are in the system. As can be seen, WRL is highly sensitive to variations in the number of containers in the system, with an asymptotic behavior, converging to zero as the number of containers increases. The convergence rate depends on the number of customers (see Fig. 7) and average demand sizes (see Fig. 8), as one can conclude from Table 2.

Summing up, as expected, there is a trade-off between cost and service level related measures. As the number of containers increases, transportation costs increases, but WRL and container utilization decreases. It seems that there is a compensation effect between empty and full container transportation costs. As the system becomes heavy, in terms of demand requests and number of customers, full container transportation costs slightly decrease and empty containers transportation costs increase. There is a clear indication that the system need to transport empty containers from a customer to another to ful<sup>fi</sup>ll demand requests, since the available number of full containers becomes insuf<sup>fi</sup>cient. This is an unwished situation for a shipping line, indicating inef<sup>fi</sup>ciencies that cannot be charged to customers.

![](/api/attachments/6NU3KFHD/fulltext/images/3d3562db559fa2e3d54b38719ee81293eaa45e438a42f5cc92858b886be0f3cb.jpg)  
Fig. 5. Container utilization.

![](/api/attachments/6NU3KFHD/fulltext/images/3df0f7cc7f83010cf9ee08c98908384f60698085e8d500a7047aeaf57253173b.jpg)  
Fig. 6. WRL.

Overall, the decision of the suitable number of containers is highly dependent on the situations analyzed. The variables and parameters are highly related, and unexpected effects can arise, making this decision very dif<sup>fi</sup>cult and risky to make. For this particular case study, if the decision maker considers six customers as a good starting point, 168 containers could be a good compromise solution, with an average total transportation cost of 6440, an average WRL of 3.23, and an average container utilization of 46%. If the decision maker is risk averse, not compromising the company's service level, the number of containers should be above 216. Further analysis should therefore be carried out to properly address the issue. The results obtained show that there is no de<sup>fi</sup>nitive answer, but several possible ones. The DSS seems a very powerful tool to help shipping lines in such decisions.

In terms of computation times, we did not perform precise measurements on the test problems, as this was not our main objectives. Based on approximate estimates, the DSS requires 9–8800 CPU seconds to run in an Intel Core Duo 1.66 GHz with 1 GB of memory, depending on the scenario being solved. These times can be considered acceptable given the complexity of the problem and the off-line planning aim of the DSS.

## 7. Concluding remarks

Container allocation in real life is extremely dif<sup>fi</sup>cult, particularly if we want to consider both cost and service level of operations. The interaction between normal and return <sup>fl</sup>ows, modeled in reverse logistics systems, increases the complexity of the model, since these <sup>fl</sup>ows have to be simultaneously considered. Models usually present a combinatory nature with huge numbers of variables and constraints, and the use of heuristics and decomposition strategies to solve them is advisable.

The strategy used to tackle the problem was to break it in two, solving a simpli<sup>fi</sup>ed version without considering transportation times, but minimizing total costs (transportation, storage and handling) and then unfolding the obtained static solution in a time schedule. All routes obtained in the solution of minimum cost (static solution) are registered and dynamically controlled until containers arrive at <sup>fi</sup>nal destinations. The system proceeds sequentially, processing each unit of time, updating data incorporating backlogs and future transportation requests from customers.

![](/api/attachments/6NU3KFHD/fulltext/images/2f3ad4620a707018279fc2a68109c7a0e8d79c607c9cb26ccaf236c05c20fb2c.jpg)  
Fig. 7. WRL related to number of customers.

![](/api/attachments/6NU3KFHD/fulltext/images/559c5e4f5d629d880a86df7a0b9b41ede80a0f661499e03c75f693d18686a000.jpg)  
Fig. 8. WRL related to average order size.

Network performance measurements, such as transportation time and time of order completion, were used to evaluate the service quality to customers. To implement and solve the model, we integrated mathematical programming techniques, stochastic models, simulation, and heuristic technique, using a DSS framework. The system has a good level of parameterization, offering many possibilities for tests and analyses. The model allows the assessment of different policies of container allocation, thus assuring a proper service level, by identifying forms of reducing <sup>fi</sup>xed and variable costs related to naval trade. It is important to point out that several con<sup>fi</sup>gurations were tested in different executions, out of which just a few examples are presented here. Some heuristic procedures had to be used to reduce the number of variables in the model to allow the utilization of the available software.

It was possible to devise a satisfactory prediction scheme for empty containers availability, by computing empty containers arriving and full containers being emptied and becoming available in the near future. The inclusion of other modeling capabilities, such as minimum stock of empty containers at each customer and the addition of a security margin to each order (to reduce the number of orders), proved worthy, offering more <sup>fl</sup>exibility to operators and bringing the model closer to reality.

The system not only determines the minimum cost routing of containers, but also keeps record of the entire trip of each container, updated at each unit of time. To deal with container routing, to reallocate empty containers considering supply and demand, to re-evaluate backlog orders, to accomplish requests of full containers — at the same time unit — is quite a complex duty, which demands exhaustive tests and system performance assessments. Moreover, the algorithm has to be <sup>fl</sup>exible to include or modify constraints and to change its criteria of cost veri<sup>fi</sup>cation.

In the test bed examples the choice of the planning horizon was arbitrary. Executions with 20, 100, 200 and even 1000 time units were explored [2]. At <sup>fi</sup>rst, there is no limit for the planning horizon, due to the fact that the model managed to absorb new orders between the static and the dynamic stages. Therefore, the limitation is determined only by the capacity of the available computational system and by the situation to be modeled, which may include critical points that cause loss of system performance.

We believe that the major contribution of this paper and its underlying research is the uni<sup>fi</sup>cation of models that are usually treated separately. The development of a new model integrating the <sup>fl</sup>ow of full containers with the <sup>fl</sup>ow of empty containers allowed the implementation of a DSS with good potential for being used by transportation and logistic companies to help in their operational planning.

## Acknowledgement

The authors would like to thank CNPq and CAPES, two Brazilian governmental agencies, for supporting the research on which this work was based. Additional thanks are due to the anonymous referee and the Editor for their valuable comments which greatly improved the quality of the paper.

## Appendix A. Derivation of formulae presented in Section 4.1.4 — Constraints

a) $^ { \mathfrak { a } } ( \dots )$ Let |N| be the cardinality of the set N; the quantity of variables of the static ILP formulation is given by the expression $( | W | + | H | ) [ ( | W | + | H | + 1 ) ( | S | | D | + 1 ) + | S | + | D | - 2 ] . ^ { , }$

The quantity of variables referring to empty containers is de<sup>fi</sup>ned by:

$$
(| W | + | H |) (| S | + | D | + | W | + | H | - 1).
$$

The quantity of variables referring to full containers is determined by:

$$
(| W | + | H |) (| W | + | H | + 1) | S | | D |.
$$

Merging the two expressions, after algebraic simpli<sup>fi</sup>cations, we get the quantity of variables from the integrated model (empty and full containers), presented bellow:

$$
\begin{array}{l} (| W | + | H |) (| S | + | D | + | W | + | H | - 1) + (| W | + | H |) (| W | + | H | + 1) | S | | D | \\ (| W | + | H |) (| S | + | D | + | W | + | H | - 1 + 1 - 1) + (| W | + | H |) (| W | + | H | + 1) | S | | D | \\ (| W | + | H |) (| S | + | D | + | W | + | H | + 1 - 2) + (| W | + | H |) (| W | + | H | + 1) | S | | D | \\ (| W | + | H |) (| W | + | H | + 1) + (| W | + | H |) (| S | + | D | - 2) + (| W | + | H |) (| W | + | H | + 1) | S | | D | \\ (| W | + | H |) (| W | + | H | + 1) (| S | | D | + 1) + (| W | + | H |) (| S | + | D | - 2) \\ . \\ (| W | + | H |) [ (| W | + | H | + 1) (| S | | D | + 1) + | S | + | D | - 2 ] \\ (| W | + | H |) [ (| W | + | H | + 1) | S | | D | + | W | + | H | + 1 + | S | + | D | - 2 ] \\ (| W | + | H |) [ | W | + | H | + S | + | D | - 1 + (| W | + | H | + 1) | S | | D ] \\ (| W | + | H |) [ \| W \| + \| H \| + \| S \| + \| D \| - 1 + 1 - 1 + (| W \| + \| H \| + 1) \| S \| \| D \| ] \end{array}
$$

From there, we get the expression:

$$
(| W | + | H |) [ (| W | + | H | + 1) (| S | | D | + 1) + | S | + | D | - 2 ]
$$

b) “(…) The number of constraints is given by (|W|+|H|)(|S||D| + 1) + 2|S||D|+|S|+|D|.” The quantity of constraints relative to empty containers, excluding the usual non-negative ones, is obtained by:

S + D + W  + H :

The constraints of the model of full containers transportation are represented by:

W + H + 2 S D :

When these expressions are combined, the quantity of constraints of the integrated model could be determined by:

$$
[ | S | + | D | + | W | + | H | ] + [ (| W | + | H | + 2) | S | | D | ]
$$

The simpli<sup>fi</sup>cation of this expression results in:

$$
(| W | + | H |) (| S | | D | + 1) + 2 | S | | D | + | S | + | D |.
$$

## Appendix B. Full container prioritization experiments

The main objective of the experiments described in this Appendix is to compare the performance of the DSS using different full container prioritization rules as presented in Section 4.3.1. The experiments were designed based on the case study presented in Section 6, introducing several random parameters (see Table B.1).

## Table B.1

Parameters de<sup>fi</sup>nition.

<table><tr><td>Parameter</td><td>Value or distribution</td></tr><tr><td>Number of warehouses</td><td>4</td></tr><tr><td>Probability of existence of demand between two clients at any period t</td><td>U(0,0.2)</td></tr><tr><td>Container processing time at a client or a warehouse</td><td>DU(1,2)</td></tr><tr><td>Transportation time between two nodes in the network</td><td>DU(DU(1,2),DU(5,6))</td></tr><tr><td>Storage time at a warehouse</td><td>1</td></tr><tr><td>Full container transportation cost (fij)</td><td>DU(3,10)</td></tr><tr><td>Empty container transportation cost</td><td>0.7*fij</td></tr><tr><td>Container processing cost at a warehouse</td><td>U(2,6)</td></tr><tr><td>Container storage cost at a warehouse</td><td>U(2,6)</td></tr></table>

We carried out three different experiments to compare the prioritization rules. Firstly, we <sup>fi</sup>xed the number of containers at 120 units and the number of clients at 4 clients, changing the order size using <sup>fi</sup>ve IID discrete uniform distributions, namely DU(1,3), DU(3,5), DU(5,7), DU(7,9), and DU(9,11), giving rise to <sup>fi</sup>ve scenarios. Secondly, we <sup>fi</sup>xed the order size distribution at DU(1,3) and the number of clients at 4 clients, changing the number of containers in {48, 72, 96, 120, 144, 168, 192, 216}, giving rise to other eight scenarios. Finally, we <sup>fi</sup>xed the number of containers at 120 units and the order size distribution at DU(1,3), changing the number of clients in {4, 6, 8}, adding three scenarios to our list of sixteen scenarios.

To compare the three prioritization rules (ODD, ETC, ETT) we used a simulation scheme using common random numbers (CRN) [15]. More speci<sup>fi</sup>cally, for each of the sixteen scenarios, 20 independent trios of simulations each using the same random-number streams and seeds across the three prioritization rules were run. All replications used a 100 week time horizon, running until all demands generated within the time horizon were fulfilled.

To evaluate the scenarios, we used the following performance measures related to operational costs and customers' service level: total transportation costs, weighted average order response lateness (WRL), WRL standard deviation, and maximum value of WRL. Tables B.2, B.3, and B 4 present the obtained results considering different order sizes different pumber of containers and different pumber of clients respectively.

Table B.2  
Simulation results — 120 containers and 4 clients — average over 20 independent replications.

<table><tr><td rowspan="2">Order size</td><td colspan="3">Average total transportation costs</td><td colspan="3">Average WRL</td><td colspan="3">Average WRL standard deviation</td><td colspan="3">Average maximum WRL</td></tr><tr><td>ODD</td><td>ETC</td><td>ETT</td><td>ODD</td><td>ETC</td><td>ETT</td><td>ODD</td><td>ETC</td><td>ETT</td><td>ODD</td><td>ETC</td><td>ETT</td></tr><tr><td>DU(1,3)</td><td>2424.05</td><td>2468.60</td><td>2419.00</td><td>0.89</td><td>0.95</td><td>0.86</td><td>2.13</td><td>2.72</td><td>2.56</td><td>9.9</td><td>18.2</td><td>16.9</td></tr><tr><td>DU(3,5)</td><td>5334.70</td><td>5449.85</td><td>5349.80</td><td>2.70</td><td>2.79</td><td>2.65</td><td>3.70</td><td>5.15</td><td>5.09</td><td>12.6</td><td>31.5</td><td>28.5</td></tr><tr><td>DU(5,7)</td><td>8441.15</td><td>8994.90</td><td>8825.40</td><td>4.62</td><td>6.55</td><td>6.20</td><td>4.68</td><td>9.07</td><td>8.39</td><td>16.9</td><td>46.6</td><td>40.6</td></tr><tr><td>DU(7,9)</td><td>10,990.70</td><td>11,303.40</td><td>11,687.65</td><td>11.21</td><td>13.16</td><td>14.25</td><td>9.03</td><td>16.29</td><td>17.54</td><td>33.7</td><td>76.3</td><td>76.0</td></tr><tr><td>DU(9,11)</td><td>12,645.50</td><td>13,195.95</td><td>12,942.40</td><td>19.08</td><td>22.11</td><td>21.40</td><td>16.06</td><td>25.49</td><td>24.99</td><td>57.4</td><td>102.3</td><td>97.7</td></tr></table>

Table B.3  
Simulation results — order size (DU(1,3)) and 4 clients — average over 20 independent replications.

<table><tr><td rowspan="2">Number of containers</td><td colspan="3">Average total transportation costs</td><td colspan="3">Average WRL</td><td colspan="3">Average WRL standard deviation</td><td colspan="3">Average maximum WRL</td></tr><tr><td>ODD</td><td>ETC</td><td>ETT</td><td>ODD</td><td>ETC</td><td>ETT</td><td>ODD</td><td>ETC</td><td>ETT</td><td>ODD</td><td>ETC</td><td>ETT</td></tr><tr><td>48</td><td>2787.15</td><td>2757.85</td><td>2705.90</td><td>3.35</td><td>3.15</td><td>3.04</td><td>3.97</td><td>5.16</td><td>4.96</td><td>14.3</td><td>28.9</td><td>27.5</td></tr><tr><td>72</td><td>2619.55</td><td>2674.50</td><td>2636.25</td><td>1.98</td><td>2.09</td><td>1.94</td><td>3.39</td><td>4.42</td><td>4.19</td><td>12.3</td><td>24.3</td><td>23.1</td></tr><tr><td>96</td><td>2511.15</td><td>2490.95</td><td>2469.95</td><td>1.49</td><td>1.38</td><td>1.43</td><td>2.88</td><td>3.37</td><td>3.59</td><td>10.8</td><td>20.8</td><td>24.5</td></tr><tr><td>120</td><td>2424.05</td><td>2468.60</td><td>2419.00</td><td>0.89</td><td>0.95</td><td>0.86</td><td>2.13</td><td>2.72</td><td>2.56</td><td>9.9</td><td>18.2</td><td>16.9</td></tr><tr><td>144</td><td>2335.35</td><td>2325.95</td><td>2336.30</td><td>0.31</td><td>0.33</td><td>0.36</td><td>1.08</td><td>1.29</td><td>1.33</td><td>6.0</td><td>9.0</td><td>9.5</td></tr><tr><td>168</td><td>2359.45</td><td>2371.55</td><td>2347.45</td><td>0.26</td><td>0.30</td><td>0.24</td><td>0.74</td><td>1.04</td><td>0.84</td><td>3.9</td><td>7.0</td><td>5.8</td></tr><tr><td>192</td><td>2167.05</td><td>2174.25</td><td>2181.10</td><td>0.15</td><td>0.14</td><td>0.16</td><td>0.56</td><td>0.59</td><td>0.63</td><td>3.1</td><td>3.9</td><td>4.2</td></tr><tr><td>216</td><td>2300.70</td><td>2332.40</td><td>2293.70</td><td>0.12</td><td>0.12</td><td>0.13</td><td>0.51</td><td>0.56</td><td>0.58</td><td>3.0</td><td>4.0</td><td>4.4</td></tr></table>

Table B.4  
Simulation results — order size (DU(1,3)) and 120 containers — average over 20 independent replications.

<table><tr><td rowspan="2">Number of clients</td><td colspan="3">Average total transportation costs</td><td colspan="3">Average WRL</td><td colspan="3">Average WRL standard deviation</td><td colspan="3">Average maximum WRL</td></tr><tr><td>ODD</td><td>ETC</td><td>ETT</td><td>ODD</td><td>ETC</td><td>ETT</td><td>ODD</td><td>ETC</td><td>ETT</td><td>ODD</td><td>ETC</td><td>ETT</td></tr><tr><td>4</td><td>2424.05</td><td>2468.60</td><td>2419.00</td><td>0.89</td><td>0.95</td><td>0.86</td><td>2.13</td><td>2.72</td><td>2.56</td><td>9.9</td><td>18.2</td><td>16.9</td></tr><tr><td>6</td><td>6591.50</td><td>6539.55</td><td>6461.65</td><td>2.62</td><td>2.71</td><td>2.68</td><td>3.38</td><td>5.01</td><td>5.07</td><td>12.1</td><td>32.4</td><td>34.5</td></tr><tr><td>8</td><td>12,398.70</td><td>12,692.65</td><td>12,818.35</td><td>16.61</td><td>18.09</td><td>18.25</td><td>13.99</td><td>25.61</td><td>25.91</td><td>51.8</td><td>117.4</td><td>121.4</td></tr></table>

The results show that there is no noticeable difference in the values of the average total transportation costs among the three prioritization rules. The values are quite similar. However, the ODD rule presents better results concerning the performance measures related to level of service. Although the rule does not always obtain the best average WRI for all scenarios, it obtains the best average values for scenarios with high numbel of clients and high order sizes. Furthermore, this rule presents the lowest average WRL standard deviation and the lowest average maximum WRL for all scenarios. As the number of clients increases, the initial number of containers in the system decreases, and the order size increases (making the system tighter), this rule presents much better values for these two performance measures than the remaining ones. For the most complex analyzed scenarios, the use of the ODD rule results in decreases of around 50% in the value of the average maximum WRL, and around 40% in the average WRL standard deviation, when compared with the second best rule. Notwithstanding the limited experimentation executed, the tests demonstrated that ODD rule presents the best balance between costs and level of service for the experimental settings analyzed, thus justifying its incorporation in our heuristic procedure.

## References

[1] R.K. Ahuja, T.L. Magnanti, J.B. Orlin, Network Flows: Theory, Algorithms, and Applications, Prentice Hall, Englewood Cliffs, N J, 1993.

[2] D.L. Bandeira, Alocação e movimentação de contêineres vazios e cheios: um modelo integrado e sua aplicação, Doctoral thesis, Federal University of Rio Grande do Sul, Porto Alegre, Brazil (2005), in Portuguese.

[3] A.A. Bertossi, P. Carraresi, G. Gallo, On some matching problems arising in vehicle scheduling models, Networks 17 (1987) 271–281.

[4] R.K. Cheung, C. Chen, A two-stage stochastic network model and solution methods for the dynamic empty container allocation problem, Transportation Science 32 (2) (1998) 142–162.

[5] S.T. Choong, M.H. Cole, E. Kutanoglu, Empty container management for intermodal transportation networks, Transportation Research Part E 38 (6) (2002) 423–438.

[6] T.G. Crainic, M. Gendreau, P. Dejax, Dynamic and stochastic models for the allocation of empty containers, Operations Research 41 (1) (1993) 102–126.

[7] P.J. Dejax, T.G. Crainic, A review of empty <sup>fl</sup>ows and <sup>fl</sup>eet management models in freight transportation, Transportation Science 21 (1987) 227–247.

[8] M. Dell'Amico, M. Fischetti, P. Toth, Heuristic algorithms for the multiple depot vehicle scheduling problem, Management Science 39 (1993) 115–125.

[9] M. Fleischmann, J.M. Bloemhof-Ruwaard, R. Dekker, E. Van Der Laan, J.A.E.E. Van Nunen, L.N. Van Wassenhove, Quantitative models for reverse logistics: a review, European Journal of Operational Research 103 (1) (1997) 1–17

[10] M.A. Forbes, J.N. Holt, A.M. Watts, An exact algorithm for multiple depot bus scheduling, European Journal of Operational Research 72 (1994) 115–124.

[11] B. Jansen, P.C.J. Swinkels, G.J.A. Teeuwen, B.A. Fluiter, H.A. Fleuren, Operational planning of a large-scale multi-modal transportation system, European Journal of Operational Research 156 (1) (2004) 41–53.

[12] H. Jula, A. Chassiakos, P. Ioannou, Port dynamic empty container reuse, Transportation Research Part E 42 (2006) 43–60.

[13] K.K. Lai, K. Lam, W.K. Chan, Shipping container logistics and allocation, Journal of the Operational Research Society 46 (6) (1995) 687–697

[14] S.W. Lam, L.H. Lee, L.C. Tang, An approximate dynamic programming approach for the empty container allocation problem, Transportation Research. Part C, Emerging Technologies 15 (4) (2007) 265–277.

[15] A.M. Law, W.D. Kelton, Simulation Modeling and Analysis, 3rd ed.McGraw-Hill, Boston, 2000.

[16] J.A. Li, S.C.H. Leung, Y. Wu, K. Liu, Allocation of empty containers between multiports, European Journal of Operational Research 182 (1) (2007) 400–412.

[17] J.A. Li, K. Liu, S.C.H. Leung, K.K. Lai, Empty container management in a port with long-run average criterion, Mathematical and Computer Modelling 40 (2004) 85–100.

[18] K.G. Murty, J.Y. Liu, Y.W. Wan, et al., A decision support system for operations in a container terminal, Decision Support Systems 39 (3) (2005) 309–332.

[19] E.W.T. Ngai, T.C.E. Cheng, S. Au, et al., Mobile commerce integrated with RFID technology in a container depot, Decision Support Systems 43 (1) (2007) 62–76.

[20] A.S. Pepin, G. Desaulniers, A. Hertz, D. Huisman, A comparison of <sup>fi</sup>ve heuristics for the multiple depot vehicle scheduling problem, Journal of Scheduling 12 (1) (2009) 17–30.

[21] C. Ribeiro, F. Soumis, A column generation approach to the multiple depot vehicle scheduling problem, Operations Research 42 (1994) 41–52.

[22] W.S. Shen, C.M. Khoong, A DSS for empty container distribution planning, Decision Support Systems 15 (1) (1995) 75–82.

[23] K. Shintani, A. Imai, E. Nishimura, S. Papadimitriou, The container shipping network design problem with empty container repositioning, Transportation Research. Part E, Logistics and Transportation Review 43 (1) (2007) 39–59.

[24] D.P. Song, Characterizing optimal empty container reposition policy in periodic-review shuttle service systems, Journal of the Operational Research Society 58 (2007) 122–133.

[25] D. Steenken, S. Voß, R. Stahlbock, Container terminal operation and operations research — a classi<sup>fi</sup>cation and literature review, OR-Spectrum 26 (2004) 3–49.

[26] M. Taleb-Ibrahimi, B. Castilho, C.F. Daganzo, Storage space vs handling work in container terminals Transportation Research. Part B: Methodological 27 (1) (1993) 13–32

[27] B. Wang, Z. Wang, Research on the optimization of intermodal empty container reposition of land-carriage, Journal of Transportation Systems Engineering and Information Technology 7 (3) (2007) 29–33

[28] W.W. White, Dynamic transshipment networks: an algorithm and its application to the distribution of empty containers, Networks 2 (3) (1972) 211–236.

![](/api/attachments/6NU3KFHD/fulltext/images/099e028514b3080b5e6ee9248bb7faecc1505e25926d88d76474f450fa6137f9.jpg)

Denise Lindstrom Bandeira is an assistant professor in the School of Management, Federal University of Rio Grande do Sul Brazil. She received his Doctoral degree (2005) and M.Sc (2000) in the School of Management, Federal University of Rio Grande do Sul, Brazil and B.Sc degrees in Computer Science (1991) and Geology (1982) from the same university. Her interest in research includes decision support systems, operations research, logistic models, data analysis, simulation, as well as systems design and implementation. Her PhD dissertation was awarded the “2005 CAPES Dissertation Prize”, being honored with the title of Brazilian best dissertation of the year in the area of Management. Papers based on her dissertation have won best paper awards in international scienti<sup>fi</sup>c meetings. She has published in several Brazilian academic journals

![](/api/attachments/6NU3KFHD/fulltext/images/21e2fdf530aa9e35f2eb71a91a70398d59240f56d5194c65c54e29e7c2a63d4c.jpg)

João Luiz Becker is full professor of Production Management and Systems Analysis in the School of Management, Federal University of Rio Grande do Sul, Brazil. In the school he leads the Research Group on Information and Decision Support Systems, working mainly in its Decision and Modeling Laboratory. He received a PhD degree in Management Science from UCLA (1986), a M.Sc. degree in Applied Mathematics from Institute of Pure and Applied Mathematics, Brazil (1978), and B.S. degrees in Mathematics (1974) and Economics (1973) from the Federal University of Rio Grande do Sul, Brazil. His research interests encompass areas such as decision analysis, decision support systems, operations research, complex systems modeling, and Information

Technology impact on organizations. He has published in several journals including Management Science, Industrial management & Data Systems, International Journal of Operations & Production Management, International Journal of Computer Integrated Manufacturing, Journal of Risk and Uncertainty, and International Journal of Software Engineering and Knowledge Engineering.

![](/api/attachments/6NU3KFHD/fulltext/images/9e0067d6ec827faa75c3dd886ae644cfff80b5abe178b079b3b732c76218bdf5.jpg)

Denis Borenstein is an associate professor in the School of Management, Federal University of Rio Grande do Sul, Brazil. He received his PhD in Management Science from University of Strathclyde, UK, a M.Sc. in Management Science from Federal University of Rio Grande do Sul, and a B.Sc. in Marine Engineering from Federal University of Rio de Janeiro, Brazil. His research interests are in the areas of modelling and simulation of manufacturing/logistical systems, real time transportation logistics, mass customization, waste collection system operational planning, <sup>fl</sup>exible manufacturing systems, and decision support systems design, implementation and validation. He has published in several journals including Annals of Operations Research, European Journal

of Operational Research, International Journal of Production Research, Journal of the Operational Research Society, Decision Support Systems, Omega, and Networks. He has co-authored a chapter in “Handbook on Decision Support Systems 2”.
