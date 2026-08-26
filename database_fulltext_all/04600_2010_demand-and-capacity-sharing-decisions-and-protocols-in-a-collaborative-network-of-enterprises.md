---
otero_id: 4600
otero_key: "3NEUTDGN"
title: "Demand and capacity sharing decisions and protocols in a collaborative network of enterprises"
authors: "Sang Won Yoon; Shimon Y. Nof"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.05.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Demand and capacity sharing decisions and protocols in a collaborative network of enterprises

Sang Won Yoon <sup>a,</sup>⁎, Shimon Y. Nof <sup>b</sup>

<sup>a</sup> Department of Systems Science and Industrial Engineering, State University of New York at Binghamton, Binghamton, NY, 13902-6000, USA <sup>b</sup> School of Industrial Engineering, Purdue University, West Lafayette, IN, 47906, USA

## a r t i c l e i n f o

Article history: Received 14 October 2008 Received in revised form 3 April 2010 Accepted 4 May 2010 Available online 24 May 2010

Keywords: Enterprise collaboration Collaborative decision making Demand-capacity sharing protocol Information sharing Order acceptance decision

## a b s t r a c t

This research is motivated by the arbitrary nature of customer orders and dynamic changes of demand patterns and the ability to overcome such uncertainty by enterprise collaboration. Such collaboration is an attractive strategy, and a set of enterprises can form a bene<sup>fi</sup>cial collaborative network. In a collaborative network of enterprises (CN), each enterprise is a self-operative organization, and enterprise collaboration needs to be carefully controlled to achieve mutual bene<sup>fi</sup>ts. In this research, therefore, demand and capacity sharing protocols have been designed to <sup>fi</sup>nd ef<sup>fi</sup>cient demand and capacity sharing decisions in the CN. New protocol models are developed and numerical examples indicate that enterprise collaboration by the proposed demand and capacity sharing decisions and protocols can signi<sup>fi</sup>cantly increase the demand ful<sup>fi</sup>llment rate and the total pro<sup>fi</sup>t of the CN. While complete collaboration can increase the demand ful<sup>fi</sup>llment rate, partial collaboration by design is preferred in terms of the total pro<sup>fi</sup>t of the CN under certain conditions. It is found that a certain level of enterprise collaboration is required to maximize the total pro<sup>fi</sup>t of the CN.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

In modern manufacturing enterprises, the random nature of customer behaviors and dynamic changes of demand patterns are inevitable attributes, and enterprise collaboration is an attractive strategy. A set of enterprises forms a bene<sup>fi</sup>cial collaborative network of enterprises (CN), and the impacts of market <sup>fl</sup>uctuation and dynamic operational behavior can be minimized by effective enterprise collaboration and coordination [3,10]. In the CN, an enterprise is generally a self-operative organization, and a set of enterprises forms a CN when mutual bene<sup>fi</sup>ts are expected. Therefore, local and global decision making processes need to be designed and controlled by well-de<sup>fi</sup>ned coordination protocols [12,14,15]. In this research, a set of collaborating enterprises, having their own customer orders and limited capacities, is considered. When a customer order from an enterprise cannot be ful<sup>fi</sup>lled by the local capacity, the demand will be shared with other collaborating enterprises which have excess capacities. As a result, the possibly unful<sup>fi</sup>lled demand can be delivered by the enterprise and the remaining capacity of collaborating enterprises can be utilized, such that mutual bene<sup>fi</sup>ts can be achieved. Demand and Capacity Sharing Protocols (DCSP) in the CN have been designed to coordinate demand and capacity sharing and allocation decisions.

The rest of the paper is organized as follows. The background of the proposed research is presented in Section 2. The general order acceptance decision model and decision making processes in the CN are presented in Section 3. The details of demand and capacity sharing protocols are presented in Section 4. Finally, numerical examples and analyses are presented and discussed in Section 5.

## 2. Background

Manufacturing and supply systems can no longer be viewed in isolation; they must be managed in the context of the total business and the associated key linkages of the business: back through the supplier chain, and forward into the distribution and customer chain. When such business collaboration is formed, formal modeling and performance analysis from economic perspectives need to be studied. For example, three dimensional performance analysis approach for collaborative network organizations has been proposed to determine Join/Leave/Remain decisions [7]. The success of any business integration is a function of the degree of cooperation among the integrated sub-systems. Especially for complex, highly distributed and collaborative sub-systems, integration and cooperation become more necessary, and the merits of cooperative coordination have been discussed in the literature [1,4].

Several streams of supply network research in the context of coordinated decision making, such as coordinated planning in inventory–distribution systems, production–distribution systems, and buyer–vendor relationship, were identi<sup>fi</sup>ed [16]. Also, vertical and horizontal supply network collaboration and a demand sharing methodology was proposed [6]. Their study proposed a framework of a central coordination system, which is equipped with a multi-criterion genetic optimization feature. Because of highly distributed nature of a collaborative network of enterprises (CN), however, the solutions need to rely on distributed coordination and task administration protocols [13]. An extensive review of information sharing and coordination mechanism can be found in the literature [2,5]. They addressed the multi-agent system approach using information sharing and coordination, concluding that it can reduce the computation effort dramatically.

The information sharing can also signi<sup>fi</sup>cantly reduce the total costs in the supply chain, thus improving its global (as opposed with local) ef<sup>fi</sup>ciency [8]. For example, customer order coordination between a supplier and multiple retailers in a decentralized inventory system with price discount strategy was studied [11]. Most researchers, however, focused on collaboration and coordination studies within a supply network with centralized authority and coordination. Centralized models have usually emphasized coordination under allowance of clear and complete information sharing among members, which is impractical to apply in any given distributed manufacturing and supply systems. As a result, enterprise collaboration has been studied in the context of enterprise integration, and an extensive literature review of enterprise collaborations can be found in Ref. [10].

Following the need to design effective protocols for noncentralized, highly distributed networks in enterprise collaboration in this research, collaborative enterprises are assumed to share their own demands and capacities with other collaborative enterprises by de<sup>fi</sup>ned protocols and decision making processes. The CN is characterized by a heterarchical framework, such that an enterprise does not have total control over the other collaborating enterprises. The collaborating enterprises achieve their goals only through decision making processes, the exchange of information, negotiation, and coordination [9]. Through information sharing, local objectives can be optimized with respect to global objectives, such that the mutual bene<sup>fi</sup>ts of the collaborative enterprises can be achieved.

The proposed demand and capacity sharing protocols and decision making processes when determining the acceptability of customer orders in demand and capacity sharing context have been de<sup>fi</sup>ned as described and analyzed in the following sections.

## 3. Collaborative order acceptance decision model

Given a set of collaborative enterprises $E = \{ e _ { 1 } , . . . , e _ { i } \}$ where each enterprise receives its own customer orders, a customer order o is composed of order quantity q and due date $t ^ { d }$ information; $o = \{ q , t ^ { d } \}$ Suppose kth customer order $O _ { k } = \{ q _ { k } , ~ t _ { k } ^ { d } \}$ is received. $o _ { k }$ needs to be evaluated whether $q _ { k }$ can be delivered within $t _ { k } ^ { d } ,$ , based on the enterprise capacity constraints. If a capacity constraint is violated, $o _ { k }$ cannot be accepted by the enterprise. Suppose that $o _ { k }$ can be ful<sup>fi</sup>lled by a set of collaborative enterprises, which have excess capacities during [0, t<sup>d</sup>]. By sharing their demands and capacities among collaborative enterprises dynamically, $o _ { k }$ becomes acceptable, such that the mutual bene<sup>fi</sup>ts can be achieved; the demand sharing enterprise ful<sup>fi</sup>lls its own customer request, and the capacity sharing enterprise (or enterprises) receives the additional demand. Therefore, the proposed study is to design an effective protocol for demand and capacity sharing coordination in the collaborative network of enterprises (CN). The collaborative order acceptance decision model in the CN is shown in Fig. 1.

3.1. General order acceptance decision model for any given enterprise in a CN

When determining the acceptability of $O _ { k } = \{ q _ { k } , ~ t _ { k } ^ { d } \}$ in any given $e _ { i } \in E ,$ the commitment of $( k - 1 )$ earlier customer orders must not be violated. The set of committed customer orders is denoted by $O = \{ o _ { 1 } , o _ { 2 } ,$ ..., $O _ { k - 1 } \}$ . The acceptability of $o _ { k }$ can be determined by

![](/api/attachments/3NEUTDGN/fulltext/images/cb2a4655305d46f9d41639ee13fe3d81ef7b96393e0c6ba6a6bcec535f50e76d.jpg)  
Fig. 1. Collaborative order acceptance decision process in a CN

$$
A (o _ {k}) (= \left\{ \begin{array}{l l} 1 & \text { if } q _ {k} \leq \sum_ {t = 0} ^ {t _ {k} ^ {d}} C A (t) - \sum_ {\kappa = 1} ^ {k - 1} \sum_ {t = 0} ^ {t _ {k} ^ {d}} C S _ {\kappa} (t) \\ 0 & \text { otherwise } \end{array} \right.\tag{1}
$$

where $\mathsf { A } ( \mathsf { o } _ { k } )$ is the acceptability of $o _ { k } \left( \mathrm { i . e . } \right.$ , 1: accept and 0: reject), CA(t) is the available capacity at time t, and $C S _ { \kappa } ( t )$ is the assigned capacity for $o _ { k } { \in } O { = } \{ o _ { 1 } , . . . , o _ { k - 1 } \}$ at time t. If $A ( o _ { k } ) = 1$ $o _ { k }$ can be accepted by the given enterprise $e _ { i \cdot }$ . If $A ( o _ { k } ) = 0 , \ o _ { k }$ cannot be ful<sup>fi</sup>lled by the given enterprise $e _ { i \cdot }$ In such case, the demand and capacity sharing protocols need to be activated to determine whether $o _ { k }$ can be met by a subset of collaborative enterprises. The demand and capacity sharing protocols include the demand sharing decision and the capacity sharing decision as follows.

## 3.2. Demand sharing decision for a possible rejected order

When $o _ { k }$ becomes a possible rejected order of $e _ { i } \in E ,$ the maximum available capacity for $O _ { k } = \{ q _ { k } , t _ { k } ^ { d } \}$ can be calculated as

$$
m _ {i} (o _ {k}) = \sum_ {t = 0} ^ {t _ {k} ^ {d}} C A (t) - \sum_ {\kappa = 1} ^ {k - 1} \sum_ {t = 0} ^ {t _ {k} ^ {d}} C S _ {\kappa} (t)\tag{2}
$$

where $m _ { i } ( o _ { k } )$ is the maximum available capacity for $o _ { k }$ in $e _ { i } ; m _ { i } ( o _ { k } ) < q _ { k }$ when $o _ { k }$ is a possible rejected order. Therefore, the requisite capacity r to ful<sup>fi</sup>ll $o _ { k }$ from collaborative enterprises' capacities can be de<sup>fi</sup>ned as

$$
r _ {i} (o _ {k}) = q _ {k} - m _ {i} (o _ {k}) > 0\tag{3}
$$

Suppose the shared capacities can be acquired from a subset of collaborative enterprises. The necessary condition to accept $o _ { k }$ can be de<sup>fi</sup>ned as

$$
r _ {i} (o _ {k}) \leq \sum_ {e _ {j} \in Z} \omega_ {j} (o _ {k})\tag{4}
$$

where $\omega _ { j } ( o _ { k } )$ denotes a shared capacity for $o _ { k }$ from $e _ { j } { \in } Z$ and $Z = \{ e _ { 1 } , . . . ,$ e } is the subset of collaborative enterprises, which propose their shared capacities to $e _ { i } ; Z \subset E .$ . Therefore, Eqs. (3) and (4) imply that $r _ { i } ( o _ { k } ) = q _ { k } -$ $m _ { i } ( o _ { k } )$ is required to meet $o _ { k } .$ When $\sum _ { e _ { i } \in Z } \mathbf { { c o } } _ { j } ( o _ { k } ) > r _ { i } ( o _ { k } )$ , however, e needs to allocate $o _ { k }$ to $\exists e _ { j } \in Z$ by the demand and capacity allocation protocol as explained in Section 4.3.

## 3.3. Capacity sharing decision process in collaborating enterprises

When a demand sharing proposal is received at a capacity sharing enterprise, $e _ { j } \in Z ,$ the maximum available capacity of $e _ { j } , m _ { j } ( o _ { k } )$ , can be calculated as shown in Eq. (2). Suppose $m _ { j } ( \boldsymbol { o } _ { k } )$ becomes the shared capacity of $e _ { j \cdot }$ Future customer orders of e<sub>j</sub> cannot be accepted during $[ 0 , t _ { k } ^ { d } ]$ since total capacity during $[ 0 , t _ { k } ^ { d } ]$ can be occupied by the shared demand from $e _ { i \cdot }$ It implies that total capacity sharing can sometimes prevent the collaborating enterprises from accepting their own customer orders. Therefore, to maximize the expected pro<sup>fi</sup>t of $e _ { j } ,$ $\omega _ { j } ( o _ { k } )$ should be

$$
0 <   \omega_ {j} (o _ {k}) \leq m _ {j} (o _ {k})\tag{5}
$$

Assuming the collaborating unit price for the shared demand is <sup>fi</sup>xed among collaborative enterprises, to determine the optimal capacity sharing proposal $\omega _ { j } ( o _ { k } )$ , the pro<sup>fi</sup>t function π<sub>j</sub> for $e _ { j } { \in } Z$ can be

$$
\pi_ {j} = \left\{ \begin{array}{l l} \left(P _ {j} - c _ {j}\right) R _ {j} + \left(C P - c _ {j}\right) \left(m _ {j} (o _ {k}) - R _ {j}\right) - c _ {j} ^ {s} \left(x _ {j} - R _ {j}\right) & \text {if x_{j} \geq R_{j}} \\ \left(P _ {j} - c _ {j}\right) x _ {j} + \left(C P - c _ {j}\right) \left(m _ {j} (o _ {k}) - R _ {j}\right) - c _ {j} ^ {u} \left(R _ {j} - x _ {j}\right) & \text {if x_{j} <   R_{j}} \end{array} \right.
$$

Therefore, the expected value of π<sub>j</sub> can be de<sup>fi</sup>ned as

ð<sup>6</sup>Þ

$$
\begin{array}{l} E \left[ \pi_ {j} \right] = \int_ {R _ {j}} ^ {\infty} \left(\left(P _ {j} - c _ {j}\right) R _ {j} + (C P - c _ {j}) \left(m _ {j} \left(o _ {k}\right) - R _ {j}\right) - c _ {j} ^ {s} \left(x _ {j} - R _ {j}\right)\right) f \left(x _ {j}\right) d x _ {j} \\ \quad + \int_ {0} ^ {R _ {j}} \left(\left(P _ {j} - c _ {j}\right) x _ {j} + (C P - c _ {j}) \left(m _ {j} \left(o _ {k}\right) - R _ {j}\right) - c _ {j} ^ {u} \left(R _ {j} - x _ {j}\right)\right) f \left(x _ {j}\right) d x _ {j} \\ = (C P - c _ {j}) m _ {j} \left(o _ {k}\right) \int_ {R _ {j}} ^ {\infty} f (x _ {j}) d x _ {j} + (P _ {j} - C P + c _ {j} ^ {s}) \int_ {R _ {j}} ^ {\infty} R _ {j} f (x _ {j}) d x _ {j} \\ \quad - c _ {j} ^ {s} \int_ {R _ {j}} ^ {\infty} x _ {j} f (x _ {j}) d x _ {j} + (C P - c _ {j}) m _ {j} \left(o _ {k}\right) \int_ {0} ^ {R _ {j}} f (x _ {j}) \\ \quad - (C P - c _ {j} + c _ {j} ^ {u}) \int_ {0} ^ {R _ {j}} R _ {j} f (x _ {j}) d x _ {j} + (P _ {j} - c _ {j} + c _ {j} ^ {u}) \int_ {0} ^ {R _ {j}} x _ {j} f (x _ {j}) d x _ {j} \end{array}\tag{7}
$$

Then, the <sup>fi</sup>rst and second derivatives of Eq. (7) can be written as

$$
\begin{array}{r l} \frac {d E [ \pi_ {j} ]}{d R _ {j}} & = (P _ {j} - C P + c _ {j} ^ {s}) \int_ {R _ {j}} ^ {\infty} f (x _ {j}) d x _ {j} - (C P - c _ {j} + c _ {j} ^ {u}) \int_ {0} ^ {R _ {j}} f (x _ {j}) d x _ {j} \\ & = (P _ {j} - C P + c _ {j} ^ {s}) (1 - F (R _ {j})) - (C P - c _ {j} + c _ {j} ^ {u}) F (R _ {j}) \\ & = (P _ {j} - C P + c _ {j} ^ {s}) + (c _ {j} - c _ {j} ^ {s} - c _ {j} ^ {u} - P _ {j}) F (R _ {j}) \\ \frac {d ^ {2} E [ \pi_ {j} ]}{d R _ {j} ^ {2}} & = (c _ {j} - c _ {j} ^ {s} - c _ {j} ^ {u} - P _ {j}) f (R _ {j}) \end{array}\tag{8}
$$

ð<sup>9</sup>Þ

Then, $E [ \pi _ { j } ]$ is a concave function since $\begin{array} { r } { \frac { d ^ { 2 } E [ \pi _ { j } ] } { d R _ { i } ^ { 2 } } = \left( c _ { j } - c _ { j } ^ { s } - c _ { j } ^ { u } - P _ { j } \right) \times } \end{array}$ $f ( R _ { j } ) { < } 0 ; c _ { j } , c _ { j } ^ { s } , c _ { j } ^ { u }$ , and $f ( R _ { j } )$ are non-negative values, and $\begin{array} { r } { P _ { j } { > } C _ { j } . } \end{array}$ Therefore, the suf<sup>fi</sup>cient optimality condition to maximize $E [ \pi _ { j } ]$ ] for $e _ { j } { \in } Z$ is

$$
F \left(R _ {j} ^ {*}\right) = \frac {C P - P _ {j} - c _ {j} ^ {s}}{c _ {j} - c _ {j} ^ {s} - c _ {j} ^ {u} - P _ {j}}\tag{10}
$$

Then, the optimal reserved capacity $\vec { R _ { j } ^ { * } }$ for $e _ { j } { \in } Z$ should satisfy Eq. (10). Assume that $F ( x _ { j } )$ follows normal distribution, Eq. (10) can be written

$$
F \left(R _ {j} ^ {*}\right) = \Phi \left(\frac {R _ {j} ^ {*} - \mu_ {j}}{\sigma_ {j}}\right) = \frac {C P - P _ {j} - c _ {s}}{\left(c _ {j} - c _ {j} ^ {s} - c _ {j} ^ {u} - P _ {j}\right)}\tag{11}
$$

where Φ is the cumulative distribution function of the standard normal distribution. As a result, $R ^ { * }$ can be found that

$$
R _ {j} ^ {*} = \mu_ {j} + z \sigma_ {j}, \Phi (z) = \frac {C P - P _ {j} - c _ {j} ^ {s}}{\left(c _ {j} - c _ {j} ^ {s} - c _ {j} ^ {u} - P _ {j}\right)}\tag{12}
$$

Therefore, to maximize the expected pro<sup>fi</sup>t for $e _ { j } \in Z ,$ regarding the demand sharing proposal, the capacity sharing proposal $\omega _ { j } ( o _ { k } )$ should be

$$
\omega_ {j} (o _ {k}) = m _ {j} (o _ {k}) - R _ {j} ^ {*}\tag{13}
$$

To coordinate the demand and capacity sharing proposals in the CN, coordination mechanism needs to be designed.

## 4. Demand and capacity sharing protocols (DCSP)

In this research, each enterprise plays the role of either a demand sharing enterprise or a capacity sharing enterprise dynamically since each enterprise is a member of the CN. The demand sharing enterprise requires additional capacity to ful<sup>fi</sup>ll a customer order when the customer order cannot be ful<sup>fi</sup>lled by its own capacity before its due date. On the other hand, the capacity sharing enterprise holds excess capacities to be shared with collaborative enterprises. The framework of demand and capacity sharing protocols is illustrated as shown in Fig. 2.

For demand and capacity sharing decisions, let the demand sharing enterprise follow the demand sharing protocol, the capacity sharing enterprise follow the capacity sharing protocol, and demands and capacities will be dynamically allocated by demand and capacity allocation protocol. The details of these protocols are followed.

## 4.1. Demand sharing protocol

The demand sharing protocol is triggered by the arrival of a new customer order, $O _ { k } = \{ q _ { k } , t _ { k } ^ { d } \}$ . When $o _ { k }$ cannot be ful<sup>fi</sup>lled by the local capacity by Eq. (1), the requisite capacity, $r _ { i } ( \boldsymbol { o } _ { k } )$ , can be identi<sup>fi</sup>ed as shown in Section 3.2. Suppose $r _ { i } ( \boldsymbol { o } _ { k } )$ is shared in the CN. Entire $m _ { i } ( o _ { k } )$ should be utilized for $o _ { k } ,$ and the acceptability of the next customer order, $o _ { k + 1 } ,$ will be minimized. Therefore, $q _ { k } \big ( > r _ { i } \big ( 0 _ { k } \big ) \big )$ should be shared in the CN to increase the shared demands for the future customer orders. The demand sharing proposal includes the identi<sup>fi</sup>cation of the initiatory enterprise and the customer order information as follows.

![](/api/attachments/3NEUTDGN/fulltext/images/113b74abd2441cfe223e09f70ddd7097904ddbd244a624ddef781bb09882ff27.jpg)  
Fig. 2. Illustration of demand and capacity sharing protocols (DCSP) in a collaborative network (CN).

Summary of parameter setting.

<table><tr><td>Parameter [unit]</td><td>Value</td></tr><tr><td>Number of collaborative enterprises</td><td> $E = \{1, 2, 3, 4\}$ </td></tr><tr><td>Demand distribution of a customer order</td><td> $N\{\mu(q_k) = 150, \sigma(q_k) = 30\}$ </td></tr><tr><td>Due date of a customer order</td><td> $t_k^d = 2$ </td></tr><tr><td>Available capacity at time  $t$ </td><td> $CA(t) = 100$ </td></tr><tr><td>Product unit price [\$/unit]</td><td> $P_j = 10$ </td></tr><tr><td>Collaborative unit price [\$/unit]</td><td> $CP = 8$ </td></tr><tr><td>Production unit cost [\$/unit]</td><td> $c_j = 5$ </td></tr><tr><td>Demand opportunity loss cost [\$/unit]</td><td> $c_j^s = 2$ </td></tr><tr><td>Capacity under-utilization cost [\$/unit]</td><td> $c_j^u = 3$ </td></tr><tr><td>Coordination unit cost [\$/unit]</td><td> $\beta = 2$ </td></tr><tr><td>Simulation time and replication</td><td>1000 and 100</td></tr></table>

$$
\Delta_ {i} = \left\{e _ {i}, o _ {k} = \left\{q _ {k}, t _ {k} ^ {d} \right\} \right\}\tag{14}
$$

Then, the demand sharing proposal will be sent to collaborating enterprises in the CN, and receiving a demand sharing proposal by an enterprise will activate the capacity sharing protocol. As a result, ω $\left( \boldsymbol { o } _ { k } \right)$ from candidate collaborating enterprises will be received. When $\omega _ { j } ( o _ { k } )$ is received, the acceptability of $o _ { k }$ is evaluated by

$$
D S _ {i} (o _ {k}) = \left\{ \begin{array}{l l} q _ {k} & \text { if } q _ {k} <   \sum_ {e _ {j} \in Z} \omega_ {j} (o _ {k}) \\ \sum_ {e _ {j} \in Z} \omega_ {j} (o _ {k}) & \text { if } (q _ {k} - r _ {i} (o _ {k})) <   \sum_ {e _ {j} \in Z} \omega_ {j} (o _ {k}) <   q _ {k} \\ \text { reject } o _ {j} & \text { otherwise } \end{array} \right.\tag{15}
$$

where $\mathsf { D S } _ { i } ( o _ { k } )$ is the maximum demand sharing quantity in $o _ { k } .$ If $o _ { k }$ can be accepted by enterprise collaboration, a demand from $o _ { k }$ will be dynamically allocated to $\exists e _ { j } \in Z ,$ which have proposed their shared capacity, by demand and capacity allocation protocol. Otherwise, $o _ { k }$ will be permanently rejected.

## 4.2. Capacity sharing protocol

The capacity sharing protocol is triggered by receiving a demand sharing proposal. When the demand sharing proposal $\varDelta _ { i }$ is received by $e _ { j } \in Z ,$ the maximum available capacity $m _ { j } ( \boldsymbol { o } _ { k } )$ needs to be evaluated as shown in Eq. (2). Since total capacity sharing prevents from accepting other future customer orders, a certain level of capacity should be reserved for the expected future demands. As shown in Eqs. (10) and (13), the capacity sharing proposal to maximize the expected pro<sup>fi</sup>t of $e _ { j } { \in } Z$ should be determined based on the demand distribution. After determining $\omega _ { j } ( o _ { k } )$ by Eq. (13), the capacity sharing proposal will be sent to the demand sharing enterprise $e _ { i \cdot }$ The capacity sharing proposal includes the identi<sup>fi</sup>cation of collaborating $e _ { j }$ and the quantity of the available capacity for $o _ { k }$ as follows.

$$
\Lambda_ {j} = \left\{e _ {j}, \omega_ {j} (o _ {k}) \right\}\tag{16}
$$

When the capacity sharing proposals are received by the demand sharing enterprise, the demand and capacity allocation decision can be determined.

## 4.3. Demand and capacity allocation protocol

Dynamic demand and capacity allocation decision needs to be determined when $\omega _ { j } ( o _ { k } )$ from a subset of collaborating enterprises are received by the demand sharing enterprise $e _ { i \cdot }$ Suppose that demand and capacity allocation between collaborative enterprises requires additional coordination cost per unit β and it is assumed to be <sup>fi</sup>xed among collaborative enterprises. Then, the coordination cost per demand and capacity sharing transaction becomes only dependent on the shared demands and capacities, such that the minimum number of demand and capacity sharing participants is preferred. Therefore, to <sup>fi</sup>nd the optimal solution of demand and capacity allocation decision, the greedy algorithm has been proposed as follows.

1. Sort the capacity sharing proposals by $\omega _ { j } ( o _ { k } )$

$$
\Theta = \left\{\theta_ {j} = \omega_ {j} (o _ {k}) | \theta_ {1} <   \theta_ {2} <  ,..., <   \theta_ {j} \right\}\tag{17}
$$

2. Let $\omega _ { j } ( o _ { k } )$ be allocated where max $\{ \theta _ { j } \in \Theta \}$ . Then, Θ\max{θ<sub>j</sub>}.

3. If Eq. (18) holds, go to Step 4. Otherwise, go to Step 1.

$$
\sum_ {e _ {j} \in Z ^ {*}} \omega_ {j} (o _ {k}) > r _ {i} (o _ {k})\tag{18}
$$

where $Z ^ { * }$ is the set of collaborating enterprises, which are selected for this demand and capacity sharing collaboration.

4. The optimal demand and capacity allocation decision will be $\forall e _ { j } \ Z ^ { * }$ , and the demand ful<sup>fi</sup>lled by $e _ { i }$ for $o _ { k }$ can be calculated by

$$
\max \left\{0, q _ {k} - \sum_ {e _ {j} \in Z ^ {*}} \omega_ {j} (o _ {k}) \right\}
$$

After determining $e _ { j } { \in } Z ^ { * }$ , the demand sharing enterprise $e _ { i }$ will send the demand and capacity allocation decisions to the capacity sharing enterprises. Then, the capacity sharing enterprises will con<sup>fi</sup>rm acceptance of the additional demand to the demand sharing enterprise.

Summary of enterprise collaboration model behaviors when 10≤σ(q )≤50

<table><tr><td rowspan="2"> $\sigma(q_k)$ </td><td colspan="2"> $M_1$ </td><td colspan="4"> $M_2$ </td><td colspan="4"> $M_3$ </td></tr><tr><td> $\gamma_t$ </td><td> $TP(\times 10^6)$ </td><td> $\gamma_l$ </td><td> $\gamma_c$ </td><td> $\gamma_t$ </td><td> $TP(\times 10^6)$ </td><td> $\gamma_l$ </td><td> $\gamma_c$ </td><td> $\gamma_t$ </td><td> $TP(\times 10^6)$ </td></tr><tr><td>10</td><td>0.591</td><td>1.1430</td><td>0.126</td><td>0.541</td><td>0.667</td><td>0.9529</td><td>0.554</td><td>0.049</td><td>0.603</td><td>1.1587</td></tr><tr><td>15</td><td>0.590</td><td>1.1410</td><td>0.122</td><td>0.545</td><td>0.667</td><td>0.9474</td><td>0.551</td><td>0.051</td><td>0.602</td><td>1.1531</td></tr><tr><td>20</td><td>0.590</td><td>1.1392</td><td>0.120</td><td>0.547</td><td>0.667</td><td>0.9454</td><td>0.547</td><td>0.057</td><td>0.604</td><td>1.1533</td></tr><tr><td>25</td><td>0.587</td><td>1.1207</td><td>0.126</td><td>0.541</td><td>0.667</td><td>0.9536</td><td>0.539</td><td>0.065</td><td>0.603</td><td>1.1465</td></tr><tr><td>30</td><td>0.580</td><td>1.0820</td><td>0.136</td><td>0.532</td><td>0.667</td><td>0.9645</td><td>0.523</td><td>0.081</td><td>0.603</td><td>1.1261</td></tr><tr><td>35</td><td>0.571</td><td>1.0259</td><td>0.143</td><td>0.524</td><td>0.667</td><td>0.9731</td><td>0.508</td><td>0.095</td><td>0.601</td><td>1.1101</td></tr><tr><td>40</td><td>0.561</td><td>0.9617</td><td>0.153</td><td>0.515</td><td>0.668</td><td>0.9860</td><td>0.494</td><td>0.108</td><td>0.602</td><td>1.0754</td></tr><tr><td>45</td><td>0.547</td><td>0.8821</td><td>0.160</td><td>0.507</td><td>0.667</td><td>0.9929</td><td>0.475</td><td>0.123</td><td>0.598</td><td>1.0392</td></tr><tr><td>50</td><td>0.535</td><td>0.8070</td><td>0.166</td><td>0.502</td><td>0.667</td><td>0.9998</td><td>0.456</td><td>0.141</td><td>0.597</td><td>1.0099</td></tr><tr><td>μ</td><td>0.572</td><td>1.0336</td><td>0.139</td><td>0.528</td><td>0.667</td><td>0.9684</td><td>0.516</td><td>0.086</td><td>0.602</td><td>1.1070</td></tr><tr><td>σ</td><td>0.0207</td><td>0.1245</td><td>0.0172</td><td>0.0171</td><td>0.0003</td><td>0.0205</td><td>0.0356</td><td>0.0333</td><td>0.0027</td><td>0.05469</td></tr></table>

Table 3  
γ (y, x) t-test results when $1 0 \leq \sigma ( q _ { k } ) \leq 5 0 .$

<table><tr><td rowspan="2"></td><td colspan="2"> $10 \leq \sigma (q) \leq 50$ </td></tr><tr><td> $M_2$ </td><td> $M_3$ </td></tr><tr><td> $M_1$ </td><td>*</td><td>*</td></tr><tr><td> $M_2$ </td><td>-</td><td>*</td></tr></table>

\* Statistically signi<sup>fi</sup>cant difference at $\alpha { = } 0 . 0 1$

Table 4  
TP(y, x) t-test results when 10≤σ(q )≤50.

<table><tr><td rowspan="2"></td><td colspan="2"> $10 \leq \sigma(q) \leq 35; 40 \leq \sigma(q_k) \leq 50$ </td></tr><tr><td> $M_2$ </td><td> $M_3$ </td></tr><tr><td> $M_1$ </td><td>*</td><td>*</td></tr><tr><td> $M_2$ </td><td>-</td><td>*</td></tr></table>

\* Statistically signi<sup>fi</sup>cant difference at $\alpha { = } 0 . 0 1$

## 5. Numerical examples and analyses

In this section, numerical examples of enterprise collaboration are given to illustrate and analyze the performance of the proposed demand and capacity sharing decisions and protocols. Three types of enterprise collaboration models have been identi<sup>fi</sup>ed; (1) No collaboration model $\left( M _ { 1 } \right)$ ), (2) Complete collaboration model (M ), and (3) Partial collaboration model $\left( M _ { 3 } \right)$

1. No collaboration (M ): Each enterprise deals with their own customer orders, but there is no demand and capacity sharing with other enterprises. This model is interesting for comparing the relative value of complete or partial collaborations, and for temporary periods during which some enterprises may prefer to “turn off” their collaborative participation in relations to Join/Leave/Remain decisions as proposed by Ref. [7].

2. Complete collaboration (M ): This model assumes total demand and capacity sharing among collaborative enterprises. When each enterprise has a possible rejected order or excess capacities, total demand and capacity are shared with a set of collaborative enterprises when excess capacity is available to share. In this model, the shared capacity is calculated by

$$
\omega_ {j} (o _ {k}) = m _ {j} (o _ {k})\tag{19}
$$

![](/api/attachments/3NEUTDGN/fulltext/images/b24932691db5c90a7b126046660a0516d344172ec5bf324538d9223bc986212d.jpg)  
Fig. 3 $\cdot \gamma _ { t } ( M _ { 1 } , M _ { 2 } , M _ { 3 } )$ when 10≤σ(q )≤50.

![](/api/attachments/3NEUTDGN/fulltext/images/33a15273aadb832ed27180a53d643eabbf4087556f7fa40cc4912f0250320686.jpg)  
Fig. 4. TP(M , M , M ) when $1 0 \leq \sigma ( q _ { k } ) \leq 5 0 .$

3. Partial collaboration $\left( M _ { 3 } \right)$ : This model assumes partial demand and capacity sharing among collaborative enterprises. Shared demand and capacity are dynamically calculated by the decision processes explained in Section 3. In this model the shared capacity is calculated by

$$
\omega_ {j} (o _ {k}) = m _ {j} (o _ {k}) - R _ {j} ^ {*}\tag{20}
$$

where $\vec { R _ { j } ^ { * } }$ is the reserved capacity at $e _ { j } \in Z .$ Therefore, only limited portion of available capacity is shared with other collaborative enterprises.

For $M _ { 2 }$ and $M _ { 3 } ,$ shared demands and capacities among collaborating enterprises are allocated as explained in Section 4.3.

## 5.1. Parameter setting

Four independent enterprises are simulated as a CN. The demand distribution of a set of collaborative enterprises at time t is modeled as Normal distribution, and the available capacity of each enterprise at time t is assumed to be <sup>fi</sup>xed. The details of parameter setting are summarized in Table 1.

To validate the performance of the proposed demand and capacity sharing coordination, two performance measures are de<sup>fi</sup>ned;

![](/api/attachments/3NEUTDGN/fulltext/images/24c5ebec107ad5604b6a85f416454322e54bad2edf920a6840f230a30f07783b.jpg)

![](/api/attachments/3NEUTDGN/fulltext/images/a42ff4804721ccc99f10bc52c9ba3b78f925a710d65d517e5a5702ca71357bb6.jpg)

![](/api/attachments/3NEUTDGN/fulltext/images/010cb92e61bda466964db1374a8f717d0e88b9e97a762bbb7db2cb44c6ef7ef1.jpg)

![](/api/attachments/3NEUTDGN/fulltext/images/e55184af2462b78ded9531ed9dbfd743dd989a5aca361fa5d98cb84b55b48ac4.jpg)  
Fig. 5. The ratio of $\frac { \Upsilon _ { l } } { \Upsilon _ { t } } ( M _ { 2 } , M _ { 3 } ) , \frac { \Upsilon _ { c } } { \Upsilon _ { t } } ( M _ { 2 } , M _ { 3 } )$ when 10≤σ(q )≤50.

Table 6  
Summary of enterprise collaboration model behaviors when $5 . 5 { \le } C P { \le } 9 . 5 $

<table><tr><td rowspan="2">CP</td><td colspan="2"> $M_1$ </td><td colspan="4"> $M_2$ </td><td colspan="4"> $M_3$ </td></tr><tr><td> $\gamma_t$ </td><td> $TP(\times 10^6)$ </td><td> $\gamma_l$ </td><td> $\gamma_c$ </td><td> $\gamma_t$ </td><td> $TP(\times 10^6)$ </td><td> $\gamma_l$ </td><td> $\gamma_c$ </td><td> $\gamma_t$ </td><td> $TP(\times 10^6)$ </td></tr><tr><td>5.5</td><td>0.580</td><td>1.0805</td><td>0.134</td><td>0.533</td><td>0.667</td><td>0.9628</td><td>0.563</td><td>0.033</td><td>0.596</td><td>1.1344</td></tr><tr><td>6.0</td><td>0.580</td><td>1.0798</td><td>0.134</td><td>0.534</td><td>0.667</td><td>0.9620</td><td>0.558</td><td>0.039</td><td>0.597</td><td>1.1353</td></tr><tr><td>6.5</td><td>0.580</td><td>1.0801</td><td>0.134</td><td>0.532</td><td>0.667</td><td>0.9619</td><td>0.551</td><td>0.047</td><td>0.598</td><td>1.1314</td></tr><tr><td>7.0</td><td>0.580</td><td>1.0784</td><td>0.135</td><td>0.533</td><td>0.667</td><td>0.9636</td><td>0.544</td><td>0.056</td><td>0.600</td><td>1.1305</td></tr><tr><td>7.5</td><td>0.579</td><td>1.0809</td><td>0.134</td><td>0.533</td><td>0.667</td><td>0.9627</td><td>0.535</td><td>0.067</td><td>0.601</td><td>1.1280</td></tr><tr><td>8.0</td><td>0.580</td><td>1.0755</td><td>0.133</td><td>0.532</td><td>0.667</td><td>0.9609</td><td>0.522</td><td>0.081</td><td>0.603</td><td>1.1241</td></tr><tr><td>8.5</td><td>0.579</td><td>1.0801</td><td>0.135</td><td>0.532</td><td>0.667</td><td>0.9641</td><td>0.508</td><td>0.099</td><td>0.607</td><td>1.1237</td></tr><tr><td>9.0</td><td>0.579</td><td>1.0770</td><td>0.135</td><td>0.533</td><td>0.667</td><td>0.9630</td><td>0.487</td><td>0.125</td><td>0.611</td><td>1.1195</td></tr><tr><td>9.5</td><td>0.580</td><td>1.0763</td><td>0.134</td><td>0.533</td><td>0.667</td><td>0.9617</td><td>0.461</td><td>0.156</td><td>0.617</td><td>1.1159</td></tr><tr><td>μ</td><td>0.580</td><td>1.0787</td><td>0.134</td><td>0.533</td><td>0.667</td><td>0.9625</td><td>0.525</td><td>0.078</td><td>0.603</td><td>1.1270</td></tr><tr><td>σ</td><td>0.0004</td><td>0.0020</td><td>0.0006</td><td>0.0005</td><td>0.00002</td><td>0.0010</td><td>0.0343</td><td>0.0415</td><td>0.0071</td><td>0.0067</td></tr></table>

demand ful<sup>fi</sup>llment rate, γ, and total pro<sup>fi</sup>t of the CN, TP. For the demand ful<sup>fi</sup>llment rate, the local demand ful<sup>fi</sup>llment rate, γ , collaborative demand ful<sup>fi</sup>llment rate from collaborating enterprises, $\gamma _ { c } ,$ and total demand ful<sup>fi</sup>llment rate of the $\mathrm { C N } , \gamma _ { t } ,$ have been defined as

$$
\gamma_ {l} = \frac {\sum_ {e _ {i} \in E} D _ {i}}{D ^ {T}}\tag{21}
$$

$$
\gamma_ {c} = \frac {\sum_ {e _ {j} \in Z} D _ {j}}{D ^ {T}}\tag{22}
$$

$$
\gamma_ {t} = \gamma_ {l} + \gamma_ {c}\tag{23}
$$

where $D _ { i }$ and $D ^ { T }$ are the demand ful<sup>fi</sup>lled by e and the total demand during the simulation experiment. $\gamma _ { l } , \gamma _ { c }$ address the demand ful<sup>fi</sup>llment rate by the local capacity and the shared capacity respectively. The simulation experiments have been conducted using Matlab with the given parameter setting as shown in Table 1. Three enterprise collaboration models $( M _ { 1 } ;$ No collaboration, M : Complete collaboration, $M _ { 3 } { \mathrm { : } }$ Partial collaboration) have been analyzed with variable order quantities, collaborative unit prices, and coordination unit costs. The experimental results are illustrated as follows.

γ (y, x) t-test results when 5.5 CP 9.5.

<table><tr><td></td><td colspan="2">5.5≤CP≤9.5</td></tr><tr><td> $\frac{y}{x}$ </td><td> $M_2$ </td><td> $M_3$ </td></tr><tr><td> $M_1$ </td><td>*</td><td>*</td></tr><tr><td> $M_2$ </td><td>-</td><td>*</td></tr></table>

Statistically signi<sup>fi</sup>cant difference at α = 0.01.

Table 7  
TP(y, x) t-test results when 5.5 CP 9.5.

<table><tr><td rowspan="2"></td><td colspan="2">5.5≤CP≤9.5</td></tr><tr><td> $M_2$ </td><td> $M_3$ </td></tr><tr><td> $M_1$ </td><td>*</td><td>*</td></tr><tr><td> $M_2$ </td><td>-</td><td>*</td></tr></table>

\* Statistically signi<sup>fi</sup>cant difference at α = 0.01.

5.2. Behavior of enterprise collaboration models under variable order quantities

The behavior of enterprise collaboration models is analyzed to examine the impact of random demand patterns when $\sigma ( q _ { k } )$ is varied. The rest of the simulation parameters are <sup>fi</sup>xed as shown in Table 1. The summary of simulation analysis results is shown in Tables 2, 3, 4 and Figs. 3, 4.

Tables 2, 3 and Fig. 3 indicate that: (1) M yields the best γ when $1 0 { \le } \sigma ( q _ { k } ) { \le } 5 0 ;$ the means of the resulting $\gamma _ { t } ( y , x )$ are signi<sup>fi</sup>cantly different at $\alpha { = } 0 . 0 1 . \left( 2 \right)$ Tables 2, 4 and Fig. 4 indicate that M yields the best TP when $1 0 \leq \sigma ( q _ { k } ) \leq 5 0 ;$ the means of $T P ( y , \ x )$ are signi<sup>fi</sup>cantly different at $\alpha { = } 0 . 0 1$ . (3)When $1 0 { \le } \sigma ( q _ { k } ) { \le } 5 0 , T P ( M _ { 1 } )$ $T P ( M _ { 3 } )$ decrease by over 29% and 12% respectively, but $T P ( M _ { 2 } )$ increases by almost 5%. This observation can be explained as follows.

When $\sigma ( q _ { k } )$ is increased, the simulation analysis results indicate that the enterprises applying $M _ { 1 }$ are unable to ful<sup>fi</sup>ll their customer orders, since only local capacities are available for their customer orders. When $1 0 { \le } \sigma ( q _ { k } ) { \le } 5 0$ both $\gamma _ { t } ( M _ { 1 } ) , T P ( M _ { 1 } )$ decrease by over 9% and 29%, respectively. $\gamma _ { t } ( M _ { 2 } , M _ { 3 } )$ , however, tend to be stable; $\gamma _ { t } ( M _ { 2 } , M _ { 3 } )$ decrease by only 0%, 1% respectively when $1 0 { \le } \sigma ( q _ { k } ) { \le } 5 0$ as shown in Table 2 and Fig. 3. This behavior of $M _ { 2 } , M _ { 3 }$ can be explained by analyzing local and collaborative demand ful<sup>fi</sup>llment rates over total demand ful<sup>fi</sup>llment rate as shown in Fig. 5.

Fig. 5 indicates that $\gamma _ { c } ( M _ { 2 } )$ decreases by almost 7%, but $\gamma _ { l } ( M _ { 2 } )$ increases by over 31%. On the other hand, while $\gamma _ { l } ( M _ { 3 } )$ decreases by almost $7 \% , \gamma _ { c } ( M _ { 3 } )$ increases by 187%. This result indicates that since $M _ { 2 } ,$ $M _ { 3 }$ models can dynamically adjust and respond with the demand and capacity sharing decisions in the CN, it implies that collaborative demand and capacity sharing models $\left( \mathrm { i } . \mathbf { e } . , M _ { 2 } , M _ { 3 } \right)$ can be the preferred models under random demand patterns in terms of $\gamma _ { t } . \ T P ( M _ { 2 } , M _ { 3 } )$ however, tend to vary when $\sigma ( q _ { k } )$ is varied, as shown in Table 2 and Fig. 4. Due to the coordination and transaction cost, it is assumed that the demand ful<sup>fi</sup>lled by local capacity $( \mathrm { i } . \mathrm { e } . , \gamma _ { l } )$ relatively yields higher pro<sup>fi</sup>t than the demand ful<sup>fi</sup>lled by collaborating enterprises $( \mathrm { i } . \mathrm { e } . , \gamma _ { c } )$ . For instance, under complete collaboration, $a m m a _ { c } ( M _ { 2 } )$ decreases by over

![](/api/attachments/3NEUTDGN/fulltext/images/53cea824d27579f3263328cb90f8197896134025bf1cc82e21c613bac7805a9e.jpg)  
Fig. ${ \bf 6 } . \gamma _ { t } ( M _ { 1 } , M _ { 2 } , M _ { 3 } )$ when 5.5≤CP≤9.5.

![](/api/attachments/3NEUTDGN/fulltext/images/4b6ecaac6359b4599061552309f513c5cf1dd67292898e48b7bf9cb8690ffc46.jpg)  
Fig. 7. TP(M , M , M ) when $5 . 5 { \le } C P { \le } 9 . 5 .$

![](/api/attachments/3NEUTDGN/fulltext/images/a20754422ddb13d24f03f86db16b6100742f3ba50b1b5e5e0eb2f7b0a8867b24.jpg)

![](/api/attachments/3NEUTDGN/fulltext/images/df0a0f0644f759fad36234ed46630e608bad69364c118586be85e9dcb2e0ad84.jpg)

![](/api/attachments/3NEUTDGN/fulltext/images/b1931f563461f46e68d1c662128c22cb2c8c1584096b115a7902458b412d6a20.jpg)

![](/api/attachments/3NEUTDGN/fulltext/images/19ca5f70a8e8a8300375e4d6fcc0d0d2172930749e8852c225f80bfed105185e.jpg)  
Fig. 8. The ratio of $\begin{array} { r } { \frac { \cdot \Upsilon _ { l } } { \Upsilon _ { t } } ( M _ { 2 } , M _ { 3 } ) , \frac { \Upsilon _ { c } } { \Upsilon _ { t } } ( M _ { 2 } , M _ { 3 } ) } \end{array}$ when $5 . 5 { \le } C P { \le } 9 . 5 .$

$7 \% , T P ( M _ { 2 } )$ increases by almost 5% due to the increase of $\gamma _ { l } ( M _ { 2 } )$ when $1 0 { \le } \sigma ( q _ { k } ) { \le } 5 0$ . On the other hand, under partial collaboration, $T P ( M _ { 3 } )$ decreases by almost 13% although $a _ { c } ( M _ { 2 } )$ increases by 187% due to the decrease of $\gamma _ { l } ( M _ { 2 } )$ . As a result, $M _ { 3 } { \mathrm { i } } !$ s preferable in terms of TP when σ(q ) varies. Based on the performance measures, different demand and capacity sharing models can be determined to maximize the CN objectives, depending on the relative collaborating unit prices.

## 5.3. Behavior of enterprise collaboration models under variable collaborating unit prices

The behavior of enterprise collaboration models is next analyzed to examine the sensitivity to the collaborating unit price, CP. The rest of simulation parameters kept the same, as show in Table 1. The summary of simulation analysis results is shown in Tables $5 , 6 , 7$ and Figs. $6 , 7 .$

Tables 5, 6 and Fig. 6 indicate that: (1) $M _ { 2 }$ yields the best γ when $5 . 5 { \le } C P { \le } 9 . 5 ;$ ; the means of $\gamma _ { t } ( y , x )$ are signi<sup>fi</sup>cantly different at $\alpha { = } 0 . 0 1 . \left( 2 \right)$ Tables 5, 7 and Fig. 7 indicate that $M _ { 3 }$ yields the best $T P$ when $5 . 5 { \le } C P { \le } 9 . 5 ;$ the means of $T P ( y , x )$ are signi<sup>fi</sup>cantly different at $\alpha { = } 0 . 0 1$ . This observation can be explained as follows.

CP is the price negotiated among collaborating enterprises when demand and capacity sharing is applied, and $C P$ is used for $M _ { 3 }$ to determine the reserved capacity, $R _ { j } ,$ and the shared capacity, $\omega _ { j } ,$ as explained in Section 3.3. As a result, $\gamma _ { t } ( M _ { 1 } , M _ { 2 } )$ and $T P ( M _ { 1 } , M _ { 2 } )$ have not been signi<sup>fi</sup>cantly changed when $C P$ is varied. $\gamma _ { t } ( M _ { 3 } )$ , however, increases by 3.5% and $T P ( M _ { 3 } )$ decreases by less than 1%; $r _ { l } ( M _ { 3 } )$ decreases by 18%, but $r _ { c } ( M _ { 3 } )$ increases by 372%. The behaviors of local and collaborative demand ful<sup>fi</sup>llment rates over total demand ful<sup>fi</sup>llment rate are depicted in Fig. 8.

Fig. 8 indicates that when CP is varied, $\frac { \gamma _ { l } } { \gamma _ { t } } ( M _ { 2 } ) , \frac { \gamma _ { c } } { \gamma _ { t } } ( M _ { 2 } )$ have not been changed since $M _ { 2 }$ simulates complete enterprise collaboration. The demand and capacity sharing decisions at $M _ { 2 }$ are not affected by the variations of CP. When $C P$ is increased, however, $\frac { \mathbb { Y } _ { l } } { \mathbb { Y } _ { t } } ( M _ { 3 } )$ decreases by 15% while $\frac { \gamma _ { c } } { \gamma _ { t } } ( M _ { 3 } )$ increases by 18%. This result indicates that the increment of CP increases demand and capacity sharing transactions in the CN by maximizing the shared capacity, $\omega _ { j } ,$ at $M _ { 3 }$ as calculated by Eqs. ((10), (12)). $T P ( M _ { 3 } )$ , however, decreases by 0.016% when CP is increased due to the coordination and transaction costs. As a result, TP $\left( M _ { 3 } \right)$ decreases at a higher $C P$ although $\gamma _ { t }$ increases. It implies that $M _ { 3 }$ can dynamically adjust the level of enterprise collaboration based on the collaborating unit price, but to maximize the total pro<sup>fi</sup>t of the CN, the coordination cost needs to be considered.

## 5.4. Behavior of enterprise collaboration models under variable coordination unit costs

The behavior of enterprise collaboration models is next analyzed to examine the sensitivity to the coordination unit cost, $\beta ,$ among the collaborating enterprises. The rest of the simulation parameters are kept the same in Table 1. The summary of simulation analysis results is shown in Tables 8, 9, 10 and Figs. 9, 10.

Summary of enterprise collaboration model behaviors when $0 . 5 \leq \beta \leq 4 . 0 .$

<table><tr><td rowspan="2"> $\beta$ </td><td colspan="2"> $M_1$ </td><td colspan="4"> $M_2$ </td><td colspan="4"> $M_3$ </td></tr><tr><td> $\gamma_t$ </td><td> $TP(\times 10^6)$ </td><td> $\gamma_l$ </td><td> $\gamma_c$ </td><td> $\gamma_t$ </td><td> $TP(\times 10^6)$ </td><td> $\gamma_l$ </td><td> $\gamma_c$ </td><td> $\gamma_t$ </td><td> $TP(\times 10^6)$ </td></tr><tr><td>0.5</td><td>0.580</td><td>1.0798</td><td>0.134</td><td>0.533</td><td>0.667</td><td>1.4424</td><td>0.522</td><td>0.082</td><td>0.604</td><td>1.1984</td></tr><tr><td>1.0</td><td>0.580</td><td>1.0790</td><td>0.134</td><td>0.533</td><td>0.667</td><td>1.2847</td><td>0.523</td><td>0.081</td><td>0.604</td><td>1.1747</td></tr><tr><td>1.5</td><td>0.580</td><td>1.0813</td><td>0.134</td><td>0.533</td><td>0.668</td><td>1.1231</td><td>0.523</td><td>0.082</td><td>0.604</td><td>1.1506</td></tr><tr><td>2.0</td><td>0.579</td><td>1.0751</td><td>0.134</td><td>0.533</td><td>0.667</td><td>0.9614</td><td>0.521</td><td>0.082</td><td>0.604</td><td>1.1234</td></tr><tr><td>2.5</td><td>0.580</td><td>1.0798</td><td>0.134</td><td>0.533</td><td>0.667</td><td>0.8031</td><td>0.523</td><td>0.081</td><td>0.604</td><td>1.1019</td></tr><tr><td>3.0</td><td>0.580</td><td>1.0786</td><td>0.135</td><td>0.532</td><td>0.667</td><td>0.6435</td><td>0.522</td><td>0.082</td><td>0.603</td><td>1.0747</td></tr><tr><td>3.5</td><td>0.580</td><td>1.0810</td><td>0.135</td><td>0.532</td><td>0.667</td><td>0.4846</td><td>0.522</td><td>0.081</td><td>0.604</td><td>1.0512</td></tr><tr><td>4.0</td><td>0.579</td><td>1.0756</td><td>0.133</td><td>0.534</td><td>0.667</td><td>0.3204</td><td>0.522</td><td>0.081</td><td>0.603</td><td>1.0246</td></tr><tr><td> $\mu$ </td><td>0.580</td><td>1.0788</td><td>0.134</td><td>0.533</td><td>0.667</td><td>0.8826</td><td>0.522</td><td>0.082</td><td>0.604</td><td>1.1124</td></tr><tr><td> $\sigma$ </td><td>0.0005</td><td>0.0023</td><td>0.0005</td><td>0.0003</td><td>0.0005</td><td>0.3919</td><td>0.0005</td><td>0.0005</td><td>0.0004</td><td>0.0608</td></tr></table>

Table 9  
γ (y, x) t-test results when $0 . 5 \leq \beta \leq 4 . 0 .$

<table><tr><td></td><td> $M_2$ </td><td> $M_3$ </td></tr><tr><td> $M_1$ </td><td>&lt;0.001*</td><td>&lt;0.001*</td></tr><tr><td> $M_2$ </td><td>-</td><td>&lt;0.001*</td></tr></table>

Statistically signi<sup>fi</sup>cant difference with $\alpha { = } 0 . 0 0 1$

Table 10  
TP(y, x) t-test results when 0.5 ≤ β ≤ 4.0.

<table><tr><td rowspan="2"></td><td colspan="2"> $0.5<\beta<3.0; 3.0<\beta<4.0$ </td><td colspan="2"> $\beta=3.0$ </td></tr><tr><td> $M_2$ </td><td> $M_3$ </td><td> $M_2$ </td><td> $M_3$ </td></tr><tr><td> $M_1$ </td><td>*</td><td>*</td><td>*</td><td>**</td></tr><tr><td> $M_2$ </td><td>-</td><td>*</td><td>-</td><td>*</td></tr></table>

Statistically signi<sup>fi</sup>cant difference with $\alpha { = } 0 . 0 1$  
⁎⁎ Statistically signi<sup>fi</sup>cant difference with $\begin{array} { r } { \alpha { = } 0 . 0 5 . } \end{array}$

The simulation analysis results indicate that: (1) $\gamma _ { t } ( M _ { 1 } , M _ { 2 } , M _ { 3 } )$ have not been changed when $0 . 5 \leq \beta \leq 4 . 0$ as shown in Tables $^ { 8 , }$ 9 and Fig. 9. (2) TP(M ) is greater than $T P ( M _ { 1 } , M _ { 3 } )$ when $\beta { < } 1 . 5 . ~ ( 3 )$ When $\beta { \geq } 1 . 5 ,$ however, TP(M ) has decreased signi<sup>fi</sup>cantly, compared to when $\beta { < } 1 . 5 ; \mathsf { i . e . }$ , when $\beta = 0 . 5$ and 1.5 are compared, TP $\left( M _ { 2 } \right)$ has decreased by over 22%. As a result, $T P ( M _ { 2 } )$ becomes less than TP(M , M ) when $\beta { \geq } 1 . 5 .$ (4) When $1 . 5 { \le } \beta { \le } 3 . 0 , ~ T P ( M _ { 3 } )$ is greater than $T P ( M _ { 1 } , M _ { 2 } )$ as shown in Table 8 and Fig. 10. (5) When $b e t a { > } 3 . 0 , T P ( M _ { 3 } )$ becomes less than TP(M ); i.e. when $\beta { = } 4 . 0 ,$ , TP $\left( M _ { 3 } \right)$ is almost 5% less than $T P ( M _ { 1 } )$ . TP(y, x) t-test results when $0 . 5 \leq \beta \leq 4 . 0$ are summarized in Table 10. This observation can be explained as follows.

Since $M _ { 1 }$ simulates no collaboration in the $\mathsf { C N } , \gamma ( M _ { 1 } )$ and $T P ( M _ { 1 } )$ are not affected by the coordination unit cost, $\beta , \ M _ { 2 } ,$ however, simulates complete demand and capacity sharing in the CN, which requires frequent coordinations and transactions among collaborating enterprises. As shown in Table 8 and Fig. 10, therefore, $T P ( M _ { 2 } )$ signi<sup>fi</sup>cantly decreases with the increment of β. On the other hand, M can eliminate excessive demand and capacity sharing transactions in the CN since the shared capacity, $\omega _ { j } ,$ is determined when there is a feasible, globally pro<sup>fi</sup>table collaboration. Table 8 and Fig. 10 indicate that $T P ( M _ { 3 } )$ cannot be signi<sup>fi</sup>cantly affected by the increment of $\beta .$ This behavior of $M _ { 2 } , \ M _ { 3 }$ can be explained by analyzing total coordination cost $T C ( M _ { 2 } , M _ { 3 } )$ and total pro<sup>fi</sup>t, $T P ( M _ { 2 } , M _ { 3 } )$ , as shown in Fig. 11.

![](/api/attachments/3NEUTDGN/fulltext/images/6ed8aa36b90de84a7773dff59fa26a3ec24b0dd8a90aa315f5e56b8d56a8fc93.jpg)  
Fig. 9. $\gamma _ { t } ( M _ { 1 } , M _ { 2 } , M _ { 3 } )$ when 0.5≤β≤4.0.

![](/api/attachments/3NEUTDGN/fulltext/images/461fb3f125b561e1e3f055ef84dc611c32e5f1322f2d7a19298650ba788ccbef.jpg)  
Fig. 10. $T P ( M _ { 1 } , M _ { 2 } , M _ { 3 } )$ when 0.5≤β≤4.0.

Both $T C ( M _ { 2 } , ~ M _ { 3 } )$ increase by almost 700% when $0 . 5 { \le } \beta { \le } 4 . 0 .$ $T P ( M _ { 2 } , ~ M _ { 3 } )$ , however, decrease by 77% and 14%, respectively. This result indicates that $M _ { 3 }$ can maximize total pro<sup>fi</sup>t of the CN by minimizing excessive demand and capacity sharing when the coordination cost is signi<sup>fi</sup>cant in the enterprise collaboration. It implies that a certain level of enterprise collaboration can minimize the impacts of the coordination cost. The derivation of their optimal collaboration level can be considered in the future research.

## 6. Conclusion

To overcome the arbitrary nature of customer orders and dynamic changes of demand patterns, enterprise collaboration is an attractive strategy. Enterprise collaboration needs to be carefully coordinated to achieve mutual bene<sup>fi</sup>ts. In this research, demand and capacity sharing decisions and protocols in the CN have been designed to determine if and when ef<sup>fi</sup>cient demand and capacity sharing and allocation decisions can be justi<sup>fi</sup>ed. The objective of demand and capacity sharing decisions and protocols is dynamically to share their demands and capacities at their preference to increase demand ful<sup>fi</sup>llment or total pro<sup>fi</sup>t or both. Numerical examples and analyses indicate that enterprise collaboration under the proposed demand and capacity sharing protocols can increase demand ful<sup>fi</sup>llment rate or total global pro<sup>fi</sup>t of a CN, and that a partial collaboration protocol is under certain conditions preferred to complete collaboration protocol in regard to total global pro<sup>fi</sup>t since the partial collaboration protocol can eliminate excessive enterprise collaboration transactions. As a result, a certain level of enterprise collaboration is preferred to maximize their global, mutual bene<sup>fi</sup>ts. In addition, the analyses indicate that a partial collaboration protocol can minimize the impacts of the coordination cost. Future research will study how to minimize the number of coordination transactions, interactive effects of different cost and incentive structures, dynamic order arrivals and different order processing (i.e., batch processing) among collaborating enterprises, and possible errors in the CN. In addition, the economical reorganization processes when forming and re-forming CNs will be investigated.

![](/api/attachments/3NEUTDGN/fulltext/images/0c40f6444922383db16c496a688e7130bcf9553a46d5806ecbda23d91920f05b.jpg)

![](/api/attachments/3NEUTDGN/fulltext/images/92c72247b586c24eac03fb4d521a15ea1e0362f88a8bbfd01a6c429513eafce6.jpg)

![](/api/attachments/3NEUTDGN/fulltext/images/58d322f828c2451d6a33e3505266ed192e27649022aedd27580ff738154a1299.jpg)

![](/api/attachments/3NEUTDGN/fulltext/images/85c39e398c1dea3931f6aa3805e4688062a5252d0e202bd000220d74d1a63e12.jpg)  
Fig. 11. The ratio of $T C ( M _ { 2 } , M _ { 3 } )$ and $T P ( M _ { 2 } , M _ { 3 } )$ when $0 . 5 { \le } \beta { \le } 4 . 0 .$

## Acknowledgments

This study was supported by the PRISM Center at Purdue University and by Kimberly Clark's project on distributed decision network and protocols. The authors also wish to thank several colleagues who have given valuable comments to improve this study.

## References

[1] P. Anussornnitisarn, S.Y. Nof, O. Etzion, Decentralized control of cooperative and autonomous agents for solving the distributed resource allocation problem, International Journal of Production Economics 98 (2) (2005) 114–128.

[2] R. Bhatnagar, P. Chandra, S.K. Goyal, Models for multi-plant coordination, European Journal of Operational Research 67 (1993) 141–160.

[3] A. Braganza, Enterprise integration: creating competitive capabilities, Integrated Manufacturing Systems 13 (8) (2002) 562–572.

[4] J.A. Ceroni, S.Y. Nof, Task parallelism in distributed supply organizations: a case study in the shoe industry, Production Planning and Control 16 (5) (2005) 500–513.

[5] F.T.S. Chan, H.K. Chan, The future trend on system-wide modeling in supply chain studies, International Journal of Advanced Manufacturing Technology 25 (7–8) (2005)820–832

[6] F.T.S. Chan, S.H. Chung, S. Wadhwa, A heuristic methodology for order distribution in a demand driven collaborative supply chain, International Journal of Production Research 42 (1) (2004) 1-19.

[7] C.-M. Chituc, S.Y. Nof, The Join/ Leave/ Remain (JLR) decision in collaborative networked organizations, Computers and Industrial Engineering 53 (1) (2007) 173–195.

[8] S. Gavirneni, Information <sup>fl</sup>ows in capacitated supply chains with <sup>fi</sup>xed ordering costs, Management Science 48 (5) (2002) 644–651.

[9] C.Y. Huang, Y.W. Wu, Decision model for partnership development in virtual enterprise, International Journal of Production Research 41 (9) (2003) 1855-1872.

[10] H.S. Jagdev, K.-D. Thoben, Anatomy of enterprise collaborations, Production Planning and Control 12 (5) (2001) 437–451.

[11] T.D. Klastorin, K. Moinzadeh, J. Son, Coordination orders in supply chains through price discounts, IIE Transactions 34 (8) (2002) 679–689.

[12] F.P. Maturana, D.H. Norrie, Distributed decision-making using the contract net within a mediator architecture, Decision Support Systems 20 (1) (1997) 53–64.

[14] J.D. Papastavrou, S. Nof, Analytic procedures for optimizing engineering task integration topologies, Decision Support Systems 17 (3) (1996) 159–182.

[15] A.A. Pereria Klen, R.J. Rabelo, A. Campos Ferreiran, L.M. Spinosa, Managing distributed business processes in the virtual enterprise, Journal of Intelligent Manufacturing 12 (2) (2001) 185–197.

[16] D.J. Tomas, P.M. Grif<sup>fi</sup>n, Coordinated supply chain management, European Journal of Operational Research 94 (1996) 1–15.

## Glossary

## Set and element

E: Set of collaborative enterprises Z: Subset of collaborative enterprises e : Demand sharing enterprise (a E) e<sub>j</sub>: Capacity sharing enterprise (a Z)

## Demand

o : kth customer order at any given enterprise q : Order quantity of kth customer order t<sub>k</sub><sup>d</sup>: Due date of kth customer order x<sub>j</sub>: Random demand quantity at e<sub>j</sub> f(x<sub>j</sub>): Probability density function of x<sub>j</sub> F(x<sub>j</sub>): Cumulative density function of x<sub>j</sub> D : Demand ful<sup>fi</sup>lled by e D<sup>T</sup>: Total demand

## Capacity

CA(t): Available capacity at time t CS (t): Available capacity for o at time t m<sub>i</sub>(o<sub>k</sub>): Maximum available capacity for o<sub>k</sub> at e<sub>i</sub> r<sub>i</sub>(o<sub>k</sub>): Requisite capacity to ful<sup>fi</sup>ll o<sub>k</sub> ω (o ): Shared capacity for o at e θ<sub>j</sub>: Collaborating capacity for e<sub>j</sub>

## Cost and profit Cost and profit

P : Product unit price at e CP: Collaborating unit price c : Production unit cost at e c<sub>j</sub><sup>s</sup>: Demand opportunity loss cost per unit at e<sub>j</sub> c<sub>j</sub><sup>u</sup>: Capacity under-utilization cost per unit at e β: Coordination unit cost π : Pro<sup>fi</sup>t function for e

## Proposals

Δ : Demand sharing proposal of e Λ : Capacity sharing proposal of e

Decision variables A(o ): Acceptability of o R : Reserved capacity at e DS (o ): Maximum demand sharing quantity in o

## Models

M : No collaboration model M : Complete collaboration model M : Partial collaboration model

## Performance measures

γ : Local demand ful<sup>fi</sup>llment rate γ : Collaborative demand ful<sup>fi</sup>llment rate γ : Total demand ful<sup>fi</sup>llment rate TC: Total coordination cost of the CN TP: Total pro<sup>fi</sup>t of the CN

Sang Won Yoon is a Research Scientist in the Department of Systems Science & Industrial Engineering at the State University of New York at Binghamton. He received his Ph. D. in Industrial Engineering from Purdue University in August 2009. His research interests are in the areas of enterprise collaboration, production and operations management, information system integration, decision support systems, and healthcare services. He has worked on various industry projects including total quality management, enterprise resource planning, enterprise information management, transportation safety and security, and healthcare systems.

Shimon Y. Nof is a Professor of Industrial Engineering at Purdue University, has held visiting positions at MIT and universities in Chile, EU, Hong Kong, Israel, Japan, and Mexico. Director of the NSF-industry-supported PRISM Center for Production, Robotics and Integration Software for Manufacturing and Management; he is a Fellow of IIE, Secretary General of IFPR, and current Chair of IFAC CC—Manufacturing and Logistics Systems. He has published over 250 articles on production engineering and information/robotics engineering and management, and is the author/editor of nine books in these areas. In 1999 he was elected to the Purdue Book of Great Teachers, and in 2002 he was awarded the Engelberger Medal for Robotics Education. Professor Nof has also had over eight years of experience in industry positions.
