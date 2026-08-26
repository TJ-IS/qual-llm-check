---
otero_id: 8462
otero_key: "3DGHKB6M"
title: "Supply chain formation using agent negotiation"
authors: "Hyun Soo Kim; Jae Hyung Cho"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.01.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Supply chain formation using agent negotiation

Hyun Soo Kim <sup>a</sup>, Jae Hyung Cho <sup>b,</sup>⁎

<sup>a</sup> Department of MIS, Dong-A University, 1 Bumin-dong 2-ga, Seo-gu, Busan 602-760, South Korea

<sup>b</sup> School of International Business and Area Studies, Pusan University of Foreign Studies, Busan 608-738, South Korea

## a r t i c l e i n f o

Article history: Received 11 September 2007 Received in revised form 31 December 2009 Accepted 20 January 2010 Available online 28 January 2010

Keywords: Agent negotiation Allocation problem Dynamic supply chain

## a b s t r a c t

This study has used agent negotiation as a way to allocate numerous orders to many participants for supply chain formation. In order to build a strategic cooperative relationship based on information sharing, agent negotiation provides a coordination mechanism in which all the participants, including buyers, manufacturers, and suppliers, are able to attain their own pro<sup>fi</sup>ts. It also provides a Pareto optimal solution from the viewpoint of a whole supply chain. This study has taken into consideration the fact that both tardiness and earliness production costs occur in the Single Machine Earliness/Tardiness (SET model) scheduling and that participating members are in a competitive relationship. We have explored and experimented to prove that agent negotiation leads to a Pareto optimal solution in a dynamic supply chain environment. This study has built a mathematical model to test the performance of agent negotiations, while making a comparison with a heuristic approach.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

One of the core problems in the dynamic supply chain is to implement supply chain formation, that is to say, the problem of selecting supply chain members to form supply chains to realize the goal of the whole supply chain. This problem refers to how to allocate orders to the multiple members in a supply chain environment.

Related to the topic, several research studies have been conducted with concepts such as supply chain collaboration, supply chain coalition, and supply chain con<sup>fi</sup>guration. Moyaux et al. [15] experimented with three levels of collaboration schemes regarding demand information transmission among supply chain members to reduce the bullwhip effect. They adopted game theory with multiagent simulation and showed that they can reach Nash equilibrium and minimum supply chain cost. Nagarajan and Sosic [16] reviewed coalition formation models in a supply chain from the viewpoint of game theory. They suggested new ideas such as foresightedness among supply chain players and future research in applying cooperative game theory to supply chain management. Smirnov et al. [22] applied soft-computing technologies such as genetic algorithms to the problem of dynamic con<sup>fi</sup>guration of a cooperative supply chain.

As a solution to the problems of supply chain formation, this study has used agent negotiation. Due to dynamic changes in the internal and external environments, it is not easy to coordinate the con<sup>fl</sup>icts of interests among supply chain members. What's more, quick response to those dynamic changes is required. Coordination of activities across a network of suppliers is essential for reacting quickly to uncertain environments [5]. For this reason, the use of an agent system has come to the fore. An agent system uses a coordination mechanism to approach a global optimization, along with the local objective of each agent. In addition, negotiations are widely being used as a coordination mechanism [8].

The use of intelligent software agents along the supply chain has been investigated by a number of researchers. The bene<sup>fi</sup>ts of adopting agent technology in supply chains have been recognized in an increasingly wide variety of applications involving inter-enterprise collaboration, extending the boundaries of strategic partnership to wherever the network technologies can reach. One way that such agents can be adaptive is to consider multiple ways to solve their subproblems so that they can adjust their solution to produce the best possible result, subject to the restrictions on available processing, communications and information resources, etc. [12]. A number of recent studies have led to signi<sup>fi</sup>cant advances by placing more emphasis on complexity and dynamics of supply chains [3]. Monteiro et al. [14] addressed a hierarchical architecture to integrate individual planner agent, negotiator agent, and mediator agent with a decentralized control for achieving robustness and <sup>fl</sup>exibility of the supply chain network. To model and simulate complex supply chains in a mass customization context, Labarthe et al. [10] proposed a methodological framework based on an agent paradigm. Forget et al. [7] explored a framework to design multi-agent behavior in a supply chain planning system, where agents were able to dynamically change their planning and coordination mechanism and, ultimately increase overall performance. Min and Bjornsson [13] presented a conceptual model of agent-based supply chain automation, in which a project agent gathers actual construction progress information and sends to subcontractor agents and supplier agents, respectively, over the Internet. They evaluated an agent-based SCM model compared with traditional SCM practice through simulation.

The multi-agent system (MAS) technology facilitates the integration of the entire supply chain as a networked system of independent echelons, each of which utilizes its own decision-making procedure. Kwon and Lee [9] believe that a multi-agent system, where multiple agents work collectively to solve speci<sup>fi</sup>c interorganization problems, provides an effective platform for coordination across organizations in the supply chain. Sadeh et al. [21] have developed an agent-based architecture for a dynamic supply chain called MASCOT. The MASCOT is a recon<sup>fi</sup>gurable, multilevel, agent-based architecture for a coordinated supply chain. Petersen et al. [18] have proposed a multi-agent architecture, called AGORA, for modeling and supporting cooperative work among distributed entities in virtual enterprises. Chaharsooghi et al. [4] have suggested a new approach to decide on ordering policies of supply chain members. In this paper, supply chain is considered as a combination of various multi-agent systems collaborating with each other. This paper has focused on the ordering agents of the supply chain and aims to make a proper learning mechanism for these agents. Liang and Huang [11] have developed a multi-agent system to simulate a supply chain, where agents operate these entities with different inventory systems. Agents are coordinated to control inventory and minimize the total cost of a supply chain by sharing information and forecasting knowledge.

Most work in this area is concerned with distributed planning and scheduling system that models the supply chain as a set of semiautonomous and collaborative entities acting together to coordinate their decentralized plans.

Typically, supply chain optimization efforts make use of models designed to represent how the internal and external factors relate to the company's desired objectives. A decision model is developed that aids decision makers in optimizing the appropriate mix of internal and external supply chain functionality over a given planning horizon. An internal factor could be one that stems from decisions that the supply chain planner has to make, such as when to order and how to schedule considering resource availability. An external supply chain factor, on the other hand, is one that stems from the supply chain itself, such as industry competitiveness, product characteristics, or a lag-time in the distribution network.

This study presents a concrete method as a solution to the supply chain formation problem by using agent negotiation based on a SET model (Single Machine Earliness/Tardiness model). In particular, through information sharing, both internal and external factors are considered when making a decision. In addition, by capitalizing on agent negotiation, all members are rewarded simultaneously, consequently accelerating performance of the whole supply chain. This agent negotiation model ensures a high degree of <sup>fl</sup>exibility; it encourages the parties' willingness to a compromise. Therefore, this study has suggested a new negotiation mechanism for achieving coordination and coherence of individual decisions in a supply chain, thus enabling resource allocation and pricing to be made more ef<sup>fi</sup>ciently and transparently.

This paper is organized as follows. Section 2 explains dynamic supply chain formation problems based on a SET model. Section 3 presents a heuristic Branch-and-Bound method, a kind of centralized method, which has been used as an alternative for comparison. Section 4 deals with an agent negotiation for supply chain formation, the main theme of this study. To this end, the structure of mediating agents, negotiation basics, and agent negotiation algorithms are explained. Section 5 explains the tests conducted to prove whether or not agent negotiation can lead to the optimization of a supply chain, to evaluate its performance, and to make a comparison with a heuristic Branch-and-Bound method and a mathematical model. In the conclusion, we have commented on contributions and the direction of future research.

## 2. De<sup>fi</sup>nition of problems

## 2.1. SET model-based dynamic supply chain formation problems

This study focuses on a dynamic supply chain formation problem (DSCFP) based on the SET model (Single Machine Earliness/Tardiness model). The SET model refers to a scheduling model that takes into consideration the earliness production cost and tardiness production cost of the single machine [1]. The scheduling problems can diversely be categorized as a single machine, parallel machine, <sup>fl</sup>ow shop, and job shop. With regard to the scheduling problems, this study, however, has focused on a single machine, because the SET model is widely used due to the advantage that it incurs the least tardiness production cost and earliness production cost when a due date is not met [19].

The dynamic supply chain means an environment in which a large number of orders can be carried out by numerous manufacturers, previous orders can be canceled, and new orders can be added. Moreover, since multiple manufacturers are in a competitive relationship, it is possible for all the orders to go to one manufacturer, or no orders to go to a certain manufacturer.

As shown in Fig. 1, a number of buyers place their orders with manufacturers, and the manufacturers also place orders with suppliers for components. That is to say, a three-layered supply chain is the scope of this study. In addition, this study deals with a make-to-order production system, and so both manufacturers and suppliers have no inventory. In essence, optimal supply chain formation problems can be summarized as follows: how to allocate n number of orders among m number of manufacturers and p number of suppliers in order to minimize the total cost of a whole supply chain.

This study assumes that the manufacturing cost of each manufacturer and each supplier is based on the SET model. Therefore, the total manufacturing costs involving earliness production cost and tardiness production cost can be changed according to which order is placed with which member. In other words, we assume that the manufacturing cost can be changed according to what orders can be placed together.

![](/api/attachments/3DGHKB6M/fulltext/images/4881fd9947d9b924b90c4a08b6bb244d028ff43eaac979dea312566c8af07604.jpg)  
Fig. 1. The placement of orders in the supply chain

Table 1 shows a good example. It assumes that there are three supply chain members and three orders, and it shows how orders are allocated to supply chain members. The manufacturing cost can be changed according to how the orders are allocated to the supply chain members.

Let's assume that we know each member's least manufacturing cost for each order combination as illustrated in Table 1. In this case, Order 1 and Order 3 will be allocated to Manufacturer B, and Order 2 will be allocated to Manufacturer C, and as a result, the total cost of the whole supply chain becomes the least possible cost.

With regard to this allocation problem, it is possible that a number of orders can go to a speci<sup>fi</sup>c member and/or no order can go to a certain member. If there are n number of orders and m number of members, the number of possible order combinations totals $( m ) ^ { n } .$ . The more the number of orders and members, the signi<sup>fi</sup>cantly longer it takes to calculate. For this reason, Fischer et al. (1996) proved that this allocation problem is an NP-hard problem [2,6,20].

## 2.2. Scheduling in a make-to-order manufacturing system

First of all, a manufacturer can receive many requests for estimates from a number of buyers, and these requests for estimates at this stage are considered provisional orders. At this point, the manufacturer makes an estimate of each order on an independent basis. As shown in Fig. 2, based on a SET model, the estimates are suggested according to the due date of each order.

After this, the Buyer places his definite order with the manufacturer that has provided the least expensive estimate. If many orders from buyers are simultaneously placed with a manufacturer, the manufacturing cost for those orders should be based on rescheduling in which earliness and tardiness production cost is taken into account. As a result, the manufacturing cost will be more than initially estimated. The additional cost comes from early and tardy production increases according to the variance between the due date and job completion time. Fig. 3 shows how rescheduling is conducted when more than two de<sup>fi</sup>nite orders are simultaneously placed with one manufacturer.

This study assumes that there is no difference in the product quality between manufacturers, but there can be differences in the manufacturing cost according to the CTP (Capable-to-Promise) function. The Capable-to-Promise function is generally de<sup>fi</sup>ned as taking into account the current status of production and the <sup>fi</sup>nite capacity of resources for <sup>fi</sup>guring production cost when promising to produce a new order. Let's also assume that all orders from buyers are placed in the same time frame. The time frame in this study means the period during which the orders from buyers are allowed to be placed. Therefore, manufacturing scheduling is to be conducted for the orders placed only in this period.

This study assumes that multiple orders with similar due dates can be placed simultaneously in the same time frame, and so overlapping orders can occur. As mentioned above in the SET model, overlapping orders can incur tardiness production cost and earliness production cost. In this case, if the number of simultaneous orders increases, the manufacturing cost, including earliness and tardiness cost, increases just like a convex increasing function.

Order allocation problem for supply chain members to minimize the total manufacturing cost for supply chain formation.

<table><tr><td>Order combination</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{1,2}</td><td>{1,3}</td><td>{2,3}</td><td>{1,2,3}</td></tr><tr><td>Member (manufacturer)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>A</td><td>80</td><td>60</td><td>50</td><td>150</td><td>160</td><td>150</td><td>220</td></tr><tr><td>B</td><td>30</td><td>90</td><td>20</td><td>130</td><td>60</td><td>140</td><td>200</td></tr><tr><td>C</td><td>80</td><td>40</td><td>40</td><td>140</td><td>130</td><td>100</td><td>210</td></tr></table>

![](/api/attachments/3DGHKB6M/fulltext/images/1a2ab067cecb176422063bf9172db3ffc6418b4c94a3030e1c586f7424dd1e7d.jpg)  
Fig. 2. Scheduling for each individual order.

## 2.3. Definition of an objective function

This section focuses on minimizing the manufacturing cost of both manufacturers and suppliers from the viewpoint of a whole supply chain. The manufacturing cost for one order is composed of variable costs and <sup>fi</sup>xed costs. In particular, the delay or early completion of a job would mean extra cost, and that should be added to the manufacturing cost. The extra cost is an earliness production cost or a tardiness production cost. To this end, the objective function for this problem solution, constraints, and de<sup>fi</sup>nition of variables is as follows. The objective function (Eq. (1)) below aims to minimize the total manufacturing cost of both a manufacturer and a supplier considering earliness production cost and tardiness production cost. In the following formula, as $T _ { i j k } ^ { s }$ and $I _ { i j k } ^ { s }$ vary according to the combination of $x _ { i j k } ,$ and $T _ { i j } ^ { m }$ and $I _ { i j } ^ { m }$ vary according to the combination of $y _ { i j } ,$ the objective function (Eq. (1)) cannot be a linear function, thus making it impossible to solve this problem by linear programming.

$$
\begin{array}{l} \text {Min} \sum_ {i = 1} ^ {s} \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {n _ {j}} \left(\mathrm{mc} _ {i j k} ^ {s} + \mathrm{fc} _ {i j k} ^ {s} + \operatorname{tard} _ {j} ^ {s} \times T _ {i j k} ^ {s} + \operatorname{earl} _ {j} ^ {s} \times I _ {i j k} ^ {s}\right) x _ {i j k} \\ \quad + \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {n} \left(\mathrm{mc} _ {i j} ^ {m} + \mathrm{fc} _ {i j} ^ {m} + \operatorname{tard} _ {j} ^ {m} \times T _ {i j} ^ {m} + \operatorname{earl} _ {j} ^ {m} \times I _ {i j} ^ {m}\right) y _ {i j} \\ s. t \quad \sum_ {i = 1} ^ {m} y _ {i j} = 1, \forall j \\ \quad \sum_ {i = 1} ^ {s} x _ {i k j} = 1, \forall k, \forall j \\ \quad x _ {i k j} = 0 \text {or} 1, y _ {i j} = 0 \text {or} 1 \end{array}\tag{1}
$$

$x _ { i k j }$ if supplier i produces the components k for order j, it becomes 1, otherwise 0

$y _ { i j }$ if manufacturer i produces order $j ,$ it becomes 1, otherwise 0 m the number of manufacturers

s the number of suppliers

n the number of orders

$n _ { j }$ the number of the components for order j

$m c _ { i j k } ^ { s }$ supplier i's manufacturing cost for the components k for order j

$\mathrm { f c } _ { i j k } ^ { s }$ supplier i's <sup>fi</sup>xed cost for the components k of order j tard<sub>j</sub><sup>s</sup> supplier's marginal tardiness production cost for order j earl<sub>j</sub><sup>s</sup> supplier's marginal earliness production cost for order j $T _ { i j k } ^ { s }$ with regard to supplier i's production of the components k of order j, the interval between its due date and the job completion date

![](/api/attachments/3DGHKB6M/fulltext/images/2a292199393b50d6bcb19429129f9ac286aa8a142aa2a8d5a44811a4c1c7d554.jpg)  
Fig. 3. SET model-based sequential scheduling considering simultaneous orders.

$I _ { i j k } ^ { s }$ with regard to supplier i's production of the components k for order j, the plus time interval between the job completion date and its due date

$\mathrm { m c } _ { i j } ^ { m }$ manufacturer i's manufacturing cost for order

$\mathrm { f c } _ { i j } ^ { m }$ manufacturer i's <sup>fi</sup>xed cost for order j

$\mathrm { t a r d } _ { i } ^ { m }$ manufacturer's marginal tardiness production cost for order j ${ \mathrm { e a r l } } _ { j } ^ { \bar { m } }$ manufacturer's marginal earliness production cost for order j $T _ { i j } ^ { m }$ with regard to manufacturer $i \prime s$ production for order j, the plus time interval between its due date and the job completion date

$I _ { i j } ^ { m }$ with regard to manufacturer i's production for order j, the plus time interval between the job completion date and its due date

## 3. Heuristic Branch-and-Bound for DSCFP

As a way to solve an optimal supply chain formation problem, we can also use the Branch-and-Bound method. In this case, as we mentioned in the previous section, the supply chain meets the dynamic environmental changes and has a competitive relationship among supply chain members. Therefore, one member (manufacturer or supplier) can carry out all the orders, or orders can be distributed among its members. That ${ \mathrm { i } } s ,$ how to allocate those orders among members is very important [17].

A Branch-and-Bound method remembers all the routes and continues to branch along the least expensive value route, and the least value becomes its bound. Accordingly, if the value of the lower branch is larger than this least value, branching stops at this point. However, this study assumes that even if the value of the lower branch is larger than that of an upper branch, the lower branch can produce the least value in the next-stage lower branch. In essence, this means that a full search has to be conducted.

In the case of Table 1, considering the number of members and order combinations, iterative allocation has to be conducted 21 times in total. Under the assumption that we know all the costs, each cost table by branch should be made. However, in an effort to overcome a full search, this study has introduced a newly developed heuristic Branch-and-Bound method. This has the following strategies that do not depend on a full search.

• Strategy 1: The total manufacturing cost in the optimal solution is at least the same or less than that of all the orders placed with one manufacturer. In the <sup>fi</sup>rst branch, the manufacturer that has the least cost for all the orders will be the <sup>fi</sup>rst starting point in branching. This manufacturing cost is the <sup>fi</sup>rst bound.

• Strategy 2: The series of branches that have generated the least value will be the same as the optimal solution or near to it. Therefore, a lower branch basically inherits the bounds of upper branches.

This strategy should be more ef<sup>fi</sup>cient than a full search algorithm. Therefore, branching starts from n number of simultaneous orders that have generated the <sup>fi</sup>rst bound, and the lower branch inherits the order combination of the upper branch. At this time, the lower branch will have one less order combination than the number of order combinations of the upper branch, i.e. n−1 order combinations. This new Branch-and-Bound method is a heuristic Branch-and-Bound. Therefore, it does not guarantee optimality but stops sooner than a full search. The algorithm of the heuristic Branch-and-Bound method is as follows.

\- Step 0: When each manufacturer has n number of orders placed, calculate each sum of the cost of orders assigned to each manufacturer. The order set assigned to a manufacturer i that has the least sum of cost becomes the starting order-manufacturer combination $T _ { s } .$ Name this starting set of orders as $O _ { i }$ for further consideration. Name the set of manufacturers that are not the i manufacturer as L.

\- Step 1: Remove each order from O and assign it to a manufacturer in L. Select the least cost manufacturer that can take the order. Compare the cost of all the selected manufacturers for each order removed from $O _ { i }$ and choose the least cost order k and its manufacturer j.

\- Step $_ { 2 : }$ If the sum of the cost of orders from $T _ { s }$ after removing the order k, and the cost of order k manufactured by j is smaller than or equal to that of $T _ { s } ,$ let $O _ { i } { = } O _ { i } { - } \{ { \mathrm { o r d e r } }$ k}, $T _ { s } = T _ { s } - \{ ( i , k ) \} + \{ ( j , k ) \}$ and go to Step 1. Otherwise, go to Step 4.

\- Step 3: If O<sub>i</sub> has only one order, go to Step 4.

\- Step 4: The $T _ { s }$ becomes a <sup>fi</sup>nal solution.

Fig. 4 shows an example of the heuristic Branch-and-Bound algorithm. Let's assume that there are three manufacturers (A, B, and C) and three orders (1, 2, and 3). To begin with, in the case in which each manufacturer accepts three simultaneous orders, A's manufacturing cost for simultaneous orders is $^ { 5 2 , }$ the least among the three. Therefore, according to Strategy 1, the <sup>fi</sup>rst branching begins with A. As the cost value in the <sup>fi</sup>rst branching is 52, the cost value in the second branching should be less than this.

Second, according to Strategy 2, A's second branching inherits the order combination of the cost value in the <sup>fi</sup>rst branching, but two orders' combination will be conducted. At this time, the removed order is to be combined with the other manufacturers. In the second branching, the order combination of A1–A2–B3 is 41, the least cost value, and the other order combinations in the second combination are to be removed (i.e. A1–A2–C3, A1–A3–B2, A1–A3–C2, A2–A3–B1, and A2–A3–C1).

Next, the third branching begins with A1–A2–B3. In the third branching, the order combination of A1 and A2 is divided into individual orders, and then they are combined with B3. B3 is not to be removed, and it continues to branch. The removed order is to be combined with the orders of other manufacturers. At this point, in case of A1–B3–B2 and A1–B3–B1, B's manufacturing cost increases due to the two simultaneous orders (A1–B3–B2 becomes 10+19+16 instead of 10+16+14, and A2–B3–B1 becomes 12+18+14 instead of 12+16+12). Because these two combinations exceed the cost value 41 of the second branching, they are to be removed. In the third branching, A2–B3–C1 becomes 41, thus being the cost value of the third branching. As a result, 41 is the least value among the order combinations in this example. The combinations with this value are A1–A2–B3 and A2–B3–C1.

![](/api/attachments/3DGHKB6M/fulltext/images/3b550e98d2ecc457e601d7a2a13ec5afb96611aee46a219d5e2b2b10013909eb.jpg)  
Fig. 4. Scenario of heuristic Branch-and-Bound method.

## 4. Agent negotiation

## 4.1. Agent negotiation structure

The main function of an agent in the supply chain is its mediatory role for order assignment. As illustrated in Fig. 5, a buyer requests a “manufacturer mediating agent” for an estimate for his order. The manufacturer mediating agent sends this estimate request to all the manufacturers in a supply chain. The manufacturers that want to respond to the order request a “supplier mediating agent” for a components estimate. The supplier mediating agent delivers this order information to all the suppliers. The suppliers that want to participate in the order will send their supplying costs to the agent, who will again resend them to each manufacturer.

The manufacturers that have received the estimates for components will select the lowest quoted cost for supplies among many suppliers. All the manufacturers in a supply chain are in a competitive relationship; they try to select the lowest quoted cost for supplies in order to reduce their manufacturing cost. Next, the manufacturers send their manufacturing cost for the order to the agent, who will again send this to the buyer. Finally, the buyer selects the lowest quoted manufacturing cost and places a de<sup>fi</sup>nite order with that manufacturer.

The manufacturer mediating agent is in charge of communications between a buyer and a manufacturer to help order assignment and to request estimates. Likewise, the supplier mediating agent takes charge of communicating between a manufacturer and a supplier to support the exchange of estimates for components. When a manufacturer that has received a de<sup>fi</sup>nite order accepts more than two orders whose due dates overlap, it has to conduct rescheduling for simultaneous orders, and because of simultaneous orders, its manufacturing cost will increase. Therefore, the next step, i.e. agent negotiation, must be taken.

## 4.2. Basic principles of agent negotiation

The basic principle of agent negotiation is based on assignment, i.e. the goal is how to assign all the orders to manufacturers (or many suppliers) on the basis of agent negotiation. In other words, when production costs rapidly increase because of simultaneous orders concentrated on a single manufacturer, those orders will be ef<sup>fi</sup>ciently reassigned among other participating manufacturers (suppliers) by using agent negotiation. If such simultaneous orders can be dispersed, tardiness or earliness production cost will also decrease. An easier explanation of the algorithms in this agent negotiation will be given along with Fig. 6. Fig. 6 refers to a situation in which 3 buyers are ordering from one manufacturer.

Agent negotiation is composed of two types of assignment. Assignment Type 1: Among a group of buyers that have simultaneously placed a de<sup>fi</sup>nite order with Manufacturer A, if one of the buyers (Buyer 1,

![](/api/attachments/3DGHKB6M/fulltext/images/4c4cdfa8b88366fbd3f60e89973b1b77e2b9eef743b588edc6b394c1392bf554.jpg)  
Fig. 5. Order placement and manufacturing process of mediator agent.

Negotiation leader) is able to place an exclusive order with Manufacturer A making the other orders recede from A, Buyer 1 would gain the largest pro<sup>fi</sup>t. So Buyer 1 requests the other buyers (Buyers 2 and 3, Negotiation partners) that have placed a de<sup>fi</sup>nite order with A to go to the other manufacturers. At this time, the other buyers will select the second-best manufacturer who has quoted the second-lowest manufacturing costs. Fortunately, if all the other buyers accept the suggestion of Buyer 1, he will make a pro<sup>fi</sup>t. Other buyers who go to the second best can either make a pro<sup>fi</sup>t or suffer a loss. The reason is because if many buyers go to the second best simultaneously, or if the second best has already had other de<sup>fi</sup>nite orders placed, the manufacturing cost will increase because of simultaneous orders. If all participating buyers can make a pro<sup>fi</sup>t by changing manufacturers, the negotiation will be easily conducted. However, if a buyer suffers a loss, compensation should be paid through negotiations. If there is still one party who suffers a loss after negotiations, the second type of assignment must be conducted.

In Assignment Type 2, Buyer 1 voluntarily goes to his second-best manufacturer to make a pro<sup>fi</sup>t. In this case, the remaining buyers pro<sup>fi</sup>t automatically, due to decreased simultaneous manufacturing cost. Of course, how much pro<sup>fi</sup>t they can make can be found out after Manufacturer A's rescheduling. If Buyer 1 goes to the second-best manufacturer, there is also the possibility that he can suffer a loss, because that manufacturer could have another de<sup>fi</sup>nite order.

Agent negotiation is conducted through the two types of negotiation mentioned above, and the success of a negotiation depends on the result of rescheduling. This agent negotiation is also used as a mechanism for selecting a supplier. Meanwhile, the negotiations among buyers and the negotiations among manufacturers are conducted independently. Therefore, whoever among the manufacturers is chosen in the negotiations among the buyers, the result in the selection of a supplier remains unchanged.

The core of the agent negotiation algorithm is the same as the negotiation algorithm between buyers and the negotiation algorithm between suppliers for manufacturer selection.

This agent negotiation system enables the losses of negotiation participants to be compensated within the bounds of pro<sup>fi</sup>ts, so that all negotiation participants (or supply chain members) can make a pro<sup>fi</sup>t. If the compensation cost is c, the pro<sup>fi</sup>t of negotiation leader is p and the loss of negotiation partner is l, then the scope of compensation is as follows: l≤c≤p, p−l≥0.

![](/api/attachments/3DGHKB6M/fulltext/images/ad751b843e0c4ef6412a1f7da4b603dd8954dfbabecce7eaa0ce0a9bdd1c1385.jpg)  
Fig. 6. The core of the agent negotiation algorithm (in case of three simultaneous orders)

The assignment mechanism in this study clearly shows the pro<sup>fi</sup>ts and losses of negotiation participants, thus making their negotiations successful. Mediating agents and the assignment technique of using reliable resources encourage and guarantee autonomous coordination and cooperation, consequently leading to a Pareto optimal solution from the viewpoint of the whole supply chain.

Most negotiation systems generally pay attention to price coordination through an offer and a counter-offer. However, the agent negotiation in this paper puts emphasis on an automatic negotiation, paying compensation for the loss of negotiation participants within the bounds of negotiation leader's pro<sup>fi</sup>ts. In particular, through an automatic negotiation, this method can show that current resources assignment is a Pareto optimal solution.

## 4.3. A mathematical model of agent negotiation

This study presents the above-mentioned agent negotiation as a mathematical model. This mathematical model is based on heuristics, which aims to minimize an additional manufacturing cost when order p and order q, both of which have a similar due date and an overlapping process period, have been placed with the same manufacturer. The constraints in Eqs. (C1) and (C2) are necessary because if p and q $( p \neq q )$ are carried out by the same manufacturer j, the constraints in Eqs. (C1) and (C2) should become: $x _ { p } ^ { j } = 1 , x _ { q } ^ { j } = \dot { 1 }$ and $z _ { e } ^ { j } = 1$ . This mathematical model minimizes simultaneous manufacturing cost. So additional cost $o _ { e } ^ { j }$ is combined with $z _ { e } ^ { j } .$ The objective function, constraints, and variables are as follows.

![](/api/attachments/3DGHKB6M/fulltext/images/6e2543165dc79e404b352064f46b0a201e3504778cc1b664cc4ab4404ff12795.jpg)  
Fig. 7. Agent negotiation algorithm for optimal supply chain formation

$$
\text { Min } \sum_ {p \in M} \sum_ {j \in N} c _ {p} ^ {j} x _ {p} ^ {j} + \sum_ {j \in N} \sum_ {e \in E} o _ {e} ^ {j} z _ {e} ^ {j}\tag{2}
$$

$$
z _ {e} ^ {j} \leq x _ {p} ^ {j}, z _ {e} ^ {j} \leq x _ {q} ^ {j} \text { for } e = (p, q) \in E\tag{C1}
$$

$$
z _ {e} ^ {j} \geq x _ {p} ^ {j} + x _ {q} ^ {j} - 1 \text { for } e = (p, q) \in E\tag{C2}
$$

$$
x _ {p} ^ {j} \in \{0, 1 \} \text { for } p \in M, j \in N\tag{C3}
$$

$$
z _ {e} ^ {j} \in \{0, 1 \} \text {   for   } j \in N, e = (p, q) \in E\tag{C4}
$$

Set of orders $M = \{ 1 , 2 , . . . , m \}$

Set of manufacturers $N = \{ 1 , 2 , . . . , n \}$

$c _ { p } ^ { j }$ the lowest manufacturing cost in which $j \in N$ can carry out $p { \in } M$

E set of $p { \in } M$ and $q \in M \ ( p \neq q )$ that have a similar due date and an overlapping manufacturing process period

$o _ { e } ^ { j }$ the additional manufacturing cost required when j∈N carries out $( p , q ) \in E$ simultaneously

$x _ { p } ^ { j }$ $\mathrm { i f } j \in N$ carries out $p \in M ,$ it becomes 1, otherwise 0 z<sub>e</sub><sup>j</sup> if $j \in N$ carries out $p \in M$ and $q \in M ( p \neq q )$ simultaneously, it becomes 1, otherwise 0.

This formula can be solved by integer programming; so along with the heuristic Branch-and-Bound, it will be used as a way of testing the optimization and the performance of agent negotiation developed in this study.

## 4.4. Definition of negotiation factors and algorithm

The agent negotiation is based on mediating agents. Negotiation participants have only to respond to the request of a mediating agent. Negotiation participants form a strategic cooperation through those negotiations, trying to make a pro<sup>fi</sup>t, leading to selecting an optimal negotiation participant and forming an optimal supply chain. We provide more detailed description of negotiation factors in Appendix A, but we illustrate in Fig. 7 on the <sup>fl</sup>ow of algorithm for optimal supply chain formation.

## 5. Evaluation of optimization and performance

## 5.1. Evaluation environment set-up

Prior to the evaluation of the optimal solution and performance, let's see the evaluation environment set-up in this study. The algorithm of both a heuristic Branch-and-Bound and agent negotiation has been transcribed into the programming language of C/C++. The integer programming for a speci<sup>fi</sup>c case has been conducted through CPLEX 6.0, in a Pentium IV 2.80 GHz and 512 M memory hardware environment. In addition, diverse scenarios have been used for our evaluation.

The evaluation in this study is composed of the evaluation for an optimal solution and the evaluation for algorithm performance. In the case of the optimal solution evaluation, an evaluation environment is again divided into two: a random cost function and a given cost function. In the random cost function, the number of orders and the number of members are 3 and 4 respectively, and the manufacturing cost for simultaneous orders changes on a real-time basis. In order to test the reliability of an optimal solution by agent negotiation, a comparison has been made with the optimal solution by the heuristic Branch-and-Bound and by integer programming.

Next, in the given cost function, the number of an order and the number of members have been expanded: $1 0 \times 1 0 \times 1 0 , 1 0 \times 8 \times 8 ,$ $8 \times 8 \times 8 , 6 \times 1 0 \times 1 0$ , and $1 0 \times 6 \times 6$ . In addition, in order to test the reliability of an optimal solution by agent negotiation, a comparison has been made with the heuristic Branch-and-Bound and full enumeration program. Here, it must be mentioned that the given cost function alone has been used to compare the optimal solution by agent negotiation with the optimal solution by full enumeration. The reason is because a comparison can be made only when each algorithm produces the same manufacturing cost for simultaneous order combinations. Table 2 gives a brief explanation of the evaluation environment set-up.

## 5.2. Optimal solution evaluation

## 5.2.1. Optimal solution evaluation by random cost function

In order to test whether agent negotiation can minimize the cost for dynamic supply chain formation, optimal solution evaluation has been conducted through a random cost function. In addition, to test the reliability of the optimal solution by agent negotiation, a comparison has been made with the heuristic Branch-and-Bound and integer programming. The integer programming follows the formulation in Eq. (2).

In the random cost function, the three algorithms use random cost <sup>fi</sup>gures. The condition for generating a random <sup>fi</sup>gure is that the manufacturing cost for simultaneous orders is larger than that for an individual order, and that random cost varies according to the number of simultaneous orders. At this time, the scope of random <sup>fi</sup>gure generation is independent of manufacturers and suppliers. In addition, the same generated random <sup>fi</sup>gures are used for each algorithm to validly compare the result.

Table 2  
Evaluation environment for an optimal solution and computing.

<table><tr><td>Evaluation factor</td><td>Evaluation environment</td><td>Number of orders × number of members (manufacturer, supplier)</td><td>Comparison algorithm</td></tr><tr><td rowspan="2">Optimal evaluation</td><td>Random cost function</td><td>4 × 3 × 3</td><td>Agent negotiation Heuristic Branch-and-Bound Integer programming</td></tr><tr><td>Given cost function</td><td>10 × 10 × 10, 10 × 8 × 8, 8 × 8 × 8, 6 × 10 × 10, 10 × 6 × 6</td><td>Agent negotiation Heuristic Branch-and-Bound Full enumeration</td></tr><tr><td>Computing Test</td><td>Given cost function</td><td>10 × 10 × 10, 10 × 8 × 8, 8 × 8 × 8, 6 × 10 × 10, 10 × 6 × 6</td><td>Agent negotiation Heuristic Branch-and-Bound Full enumeration</td></tr></table>

In the random cost function, data formation and the process for optimal solution evaluation are as follows. The supply chain has four orders, three manufacturers, and three suppliers. In addition, the simultaneous orders occur more than once. The evaluation is based on the following three scenarios.

• Scenario 1: manufacturer's simultaneous orders: 2; supplier's simultaneous orders: 3

• Scenario 2: manufacturer's simultaneous orders: 2; supplier's simultaneous orders: 2

• Scenario 3: manufacturer's simultaneous orders: 3; supplier's simultaneous orders: 2

Each manufacturer's initial manufacturing cost and each supplier's initial supply cost in the three scenarios are shown in Tables 3 and 4. The initial input data is the individual order cost of each manufacturer and each supplier.

Table 5 shows the estimated costs for the provisional orders from the buyers. At this time, the manufacturers that have selected the lowest supply cost among many supply costs, as shown in Table 4, have already added this to their manufacturing cost, and suggested it to the buyers. The buyers select the lowest manufacturing cost and send a de<sup>fi</sup>nite order (the shaded area in Table 5). As illustrated in Table 6, the de<sup>fi</sup>nite orders cause simultaneous orders. Simultaneous orders have occurred in the manufacturing cost in Table 3 and in the supply cost in Table 4. Because of this, the cost for a de<sup>fi</sup>nite order has increased from the initial cost for a provisional order in Table 5.

The result of an optimal solution through agent negotiation is shown in Tables 7–9. Table 7 shows the reselected manufacturers and their manufacturing costs that have been chosen through negotiations between buyers. Table 8 shows the reselected suppliers and their supplying costs that have been chosen through negotiations between reselected manufacturers. Finally, Table 9 shows total costs of Tables 7 and 8, i.e. total supply chain costs after negotiations. Fig. 8 illustrates the results of three tests, proving that total supply chain costs have been decreased in all the tests after negotiations.

Table 3  
Initial manufacturing cost of manufacturers.

<table><tr><td rowspan="2" colspan="2">Manufacturing cost</td><td colspan="4">Manufacturer 1</td><td colspan="4">Manufacturer 2</td><td colspan="4">Manufacturer 3</td></tr><tr><td>01</td><td>02</td><td>03</td><td>04</td><td>01</td><td>02</td><td>03</td><td>04</td><td>01</td><td>02</td><td>03</td><td>04</td></tr><tr><td>Scenario 1</td><td>Input data 1</td><td>10</td><td>9</td><td>8</td><td>7</td><td>12</td><td>15</td><td>7</td><td>10</td><td>9</td><td>8</td><td>10</td><td>11</td></tr><tr><td>Scenario 2</td><td>Input data 2</td><td>15</td><td>19</td><td>25</td><td>16</td><td>14</td><td>22</td><td>17</td><td>20</td><td>17</td><td>18</td><td>19</td><td>23</td></tr><tr><td>Scenario 3</td><td>Input data 3</td><td>18</td><td>16</td><td>15</td><td>23</td><td>19</td><td>22</td><td>20</td><td>19</td><td>18</td><td>21</td><td>22</td><td>20</td></tr></table>

\*O: order; shade: the lowest cost.

Table 8  
Table 6  
Table 4  
Initial supplying cost of suppliers.

<table><tr><td rowspan="2" colspan="2">Supplying cost</td><td colspan="4">Supplier a</td><td colspan="4">Supplier b</td><td colspan="4">Supplier c</td></tr><tr><td>O1</td><td>O2</td><td>O3</td><td>O4</td><td>O1</td><td>O2</td><td>O3</td><td>O4</td><td>O1</td><td>O2</td><td>O3</td><td>O4</td></tr><tr><td>Scenario 1</td><td>Input data 1</td><td>5</td><td>7</td><td>9</td><td>6</td><td>4</td><td>8</td><td>6</td><td>7</td><td>6</td><td>6</td><td>5</td><td>4</td></tr><tr><td>Scenario 2</td><td>Input data 2</td><td>7</td><td>5</td><td>6</td><td>3</td><td>4</td><td>6</td><td>7</td><td>4</td><td>5</td><td>7</td><td>5</td><td>5</td></tr><tr><td>Scenario 3</td><td>Input data 3</td><td>6</td><td>5</td><td>4</td><td>4</td><td>7</td><td>6</td><td>8</td><td>3</td><td>4</td><td>7</td><td>7</td><td>6</td></tr></table>

\*O: order; shade: the lowest cost.

Table 5  
Manufacturing cost plus supplying cost for a provisional order.

<table><tr><td rowspan="2" colspan="2">Provisional orders: mc + sc(the lowest cost)</td><td colspan="4">Manufacturer 1</td><td colspan="4">Manufacturer 2</td><td colspan="4">Manufacturer 3</td></tr><tr><td>01</td><td>02</td><td>03</td><td>04</td><td>01</td><td>02</td><td>03</td><td>04</td><td>01</td><td>02</td><td>03</td><td>04</td></tr><tr><td>Scenario 1</td><td>mc + sc</td><td>14</td><td>15</td><td>13</td><td>11</td><td>16</td><td>21</td><td>12</td><td>14</td><td>13</td><td>14</td><td>15</td><td>15</td></tr><tr><td>Scenario 2</td><td>mc + sc</td><td>19</td><td>24</td><td>30</td><td>19</td><td>18</td><td>27</td><td>22</td><td>23</td><td>21</td><td>23</td><td>24</td><td>26</td></tr><tr><td>Scenario 3</td><td>mc + sc</td><td>22</td><td>21</td><td>19</td><td>26</td><td>23</td><td>27</td><td>24</td><td>22</td><td>24</td><td>26</td><td>26</td><td>23</td></tr></table>

mc: manufacturing cost; sc: supplying cost.

In addition, the test results have been compared with integer programming and the heuristic Branch-and-Bound. We have checked to what extent the results of both agent negotiation and the heuristic Branch-and-Bound are similar to the integer programming solution.

In Fig. 9, we can examine the solutions generated from integer programming, agent negotiation, and heuristic Branch-and-Bound based on the three scenarios. The three solutions have shown a very similar result. In Scenario 1 and Scenario 3, the agent negotiation and integer programming have generated the same result, and only the heuristic Branch-and-Bound has generated a higher cost in Scenario 3. In Scenario 2, agent negotiation has generated a slightly higher cost solution (+1) compared with the integer programming that follows the formula in Eq. (2). These tests in the random cost function prove that agent negotiation can generate a better or as good a solution as other methods.

Moreover, in contrast to the heuristic Branch-and-Bound and integer programming, agent negotiation can show the pro<sup>fi</sup>ts and losses generated in the process of negotiations on a real-time basis. Because of this, supply chain members can strategically cooperate. Table 9 shows the pure pro<sup>fi</sup>ts and losses without compensation amount of supply chain members through agent negotiation. While every other member pro<sup>fi</sup>ts, in Scenario 2, Order 1 (Buyer 1) suffers a loss of −1. This is because Buyer 1 moved to Manufacturer 3 at the suggestion of Buyer 3, who has gained a pro<sup>fi</sup>t of +2. However, Buyer 1 receives compensation from Buyer 3 (Order 3). Therefore, Buyer 1 doesn't suffer a loss, but the pro<sup>fi</sup>t of Buyer 3 decreases to +1. All losses were able to be compensated by the negotiation leader when the pro<sup>fi</sup>t of negotiation leader is larger than the loss of the negotiation partner(s). If any buyers suffer a loss after negotiations, the negotiation will be canceled. The sum pro<sup>fi</sup>t of all buyers is still +4 in Scenario 2. The next section has expanded the number of orders and supply chain members to conduct optimal solution evaluation in the given cost functions.

Manufacturing cost plus supplying cost for a de<sup>fi</sup>nite order.

<table><tr><td rowspan="2" colspan="2">Definite orders: mc + sc</td><td colspan="4">Manufacturer 1</td><td colspan="4">Manufacturer 2</td><td colspan="4">Manufacturer 3</td></tr><tr><td>01</td><td>02</td><td>03</td><td>04</td><td>01</td><td>02</td><td>03</td><td>04</td><td>01</td><td>02</td><td>03</td><td>04</td></tr><tr><td>Scenario 1</td><td>mc + sc</td><td>-</td><td>-</td><td>-</td><td>16</td><td>-</td><td>-</td><td>16</td><td>-</td><td>17</td><td>22</td><td>-</td><td>-</td></tr><tr><td>Scenario 2</td><td>mc + sc</td><td>-</td><td>-</td><td>-</td><td>23</td><td>22</td><td>-</td><td>27</td><td>-</td><td>-</td><td>27</td><td>-</td><td>-</td></tr><tr><td>Scenario 3</td><td>mc + sc</td><td>27</td><td>33</td><td>29</td><td>-</td><td>-</td><td>-</td><td>-</td><td>22</td><td>-</td><td>-</td><td>-</td><td>-</td></tr></table>

Table 7  
Reassignment of de<sup>fi</sup>nite orders to the manufacturers after buyer's negotiations.

<table><tr><td rowspan="2" colspan="2">Manufacturing cost</td><td colspan="4">Manufacturer 1</td><td colspan="4">Manufacturer 2</td><td colspan="4">Manufacturer 3</td></tr><tr><td>01</td><td>02</td><td>03</td><td>04</td><td>01</td><td>02</td><td>03</td><td>04</td><td>01</td><td>02</td><td>03</td><td>04</td></tr><tr><td rowspan="2">Scenario 1</td><td>Input data 1</td><td>10</td><td>9</td><td>8</td><td>7</td><td>12</td><td>15</td><td>7</td><td>10</td><td>9</td><td>8</td><td>10</td><td>11</td></tr><tr><td>Cost after negotiation</td><td>11</td><td>-</td><td>-</td><td>9</td><td>-</td><td>-</td><td>7</td><td>-</td><td>-</td><td>8</td><td>-</td><td>-</td></tr><tr><td rowspan="2">Scenario 2</td><td>Input data 2</td><td>15</td><td>19</td><td>25</td><td>16</td><td>14</td><td>22</td><td>17</td><td>20</td><td>17</td><td>18</td><td>19</td><td>23</td></tr><tr><td>Cost after negotiation</td><td>-</td><td>-</td><td>-</td><td>16</td><td>-</td><td>-</td><td>17</td><td>-</td><td>19</td><td>20</td><td>-</td><td>-</td></tr><tr><td rowspan="2">Scenario 3</td><td>Input data 3</td><td>18</td><td>16</td><td>15</td><td>23</td><td>19</td><td>22</td><td>20</td><td>19</td><td>18</td><td>21</td><td>22</td><td>20</td></tr><tr><td>Cost after negotiation</td><td>21</td><td>-</td><td>18</td><td>-</td><td>-</td><td>-</td><td>-</td><td>19</td><td>-</td><td>21</td><td>-</td><td>-</td></tr></table>

Reassignment of de<sup>fi</sup>nite orders to the suppliers after manufacturer's negotiations.

<table><tr><td rowspan="2" colspan="2">Supplying cost</td><td colspan="4">Supplier a</td><td colspan="4">Supplier b</td><td colspan="4">Supplier c</td></tr><tr><td>01</td><td>02</td><td>03</td><td>04</td><td>01</td><td>02</td><td>03</td><td>04</td><td>01</td><td>02</td><td>03</td><td>04</td></tr><tr><td rowspan="2">Scenario 1</td><td>Input data 1</td><td>5</td><td>7</td><td>9</td><td>6</td><td>4</td><td>8</td><td>6</td><td>7</td><td>6</td><td>6</td><td>5</td><td>4</td></tr><tr><td>Cost after negotiation</td><td>-</td><td>7</td><td>-</td><td>-</td><td>4</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>7</td><td>6</td></tr><tr><td rowspan="2">Scenario 2</td><td>Input data 2</td><td>7</td><td>5</td><td>6</td><td>3</td><td>4</td><td>6</td><td>7</td><td>4</td><td>5</td><td>7</td><td>5</td><td>5</td></tr><tr><td>Cost after negotiation</td><td>-</td><td>5</td><td>-</td><td>-</td><td>4</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>8</td><td>6</td></tr><tr><td rowspan="2">Scenario 3</td><td>Input data 3</td><td>6</td><td>5</td><td>4</td><td>4</td><td>7</td><td>6</td><td>8</td><td>3</td><td>4</td><td>7</td><td>7</td><td>6</td></tr><tr><td>Cost after negotiation</td><td>-</td><td>-</td><td>4</td><td>-</td><td>-</td><td>-</td><td>-</td><td>3</td><td>6</td><td>9</td><td>-</td><td>-</td></tr></table>

## 5.2.2. Optimal solution evaluation in a given cost function

By using a random cost function in the previous section, we have tested the optimal solution of an agent negotiation algorithm. Next, we have expanded the number of orders and the number of members in the given cost functions to test the optimal solution of an agent negotiation algorithm. The scenarios for this optimal solution evaluation are as follows.

• Scenario 1: 10 orders, 10 manufacturing/supply members

• Scenario 2: 10 orders, 8 manufacturing/supply members

• Scenario 3: 8 orders, 8 manufacturing/supply members

• Scenario 4: 6 orders, 10 manufacturing/supply members

• Scenario 5: 10 orders, 6 manufacturing/supply members

Table 9  
Optimal solution combinations for de<sup>fi</sup>nite orders and pro<sup>fi</sup>ts after negotiations.

<table><tr><td rowspan="2" colspan="2">Definite orders (optimal value): mc + sc</td><td colspan="4">Manufacturer 1</td><td colspan="4">Manufacturer 2</td><td colspan="4">Manufacturer 3</td></tr><tr><td>01</td><td>02</td><td>03</td><td>04</td><td>01</td><td>02</td><td>03</td><td>04</td><td>01</td><td>02</td><td>03</td><td>04</td></tr><tr><td rowspan="2">Scenario 1</td><td>Cost after negotiation</td><td>15</td><td>-</td><td>-</td><td>15</td><td>-</td><td>-</td><td>14</td><td>-</td><td>-</td><td>15</td><td>-</td><td>-</td></tr><tr><td>Profit after negotiation</td><td>+2</td><td></td><td></td><td>+1</td><td></td><td></td><td>+2</td><td></td><td></td><td>+7</td><td></td><td></td></tr><tr><td rowspan="2">Scenario 2</td><td>Cost after negotiation</td><td>-</td><td>-</td><td>-</td><td>22</td><td>-</td><td>-</td><td>25</td><td>-</td><td>23</td><td>25</td><td>-</td><td>-</td></tr><tr><td>Profit after negotiation</td><td></td><td></td><td></td><td>+1</td><td></td><td></td><td>+2</td><td></td><td>-1</td><td>+2</td><td></td><td></td></tr><tr><td rowspan="2">Scenario 3</td><td>Cost after negotiation</td><td>27</td><td>-</td><td>22</td><td>-</td><td>-</td><td>-</td><td>-</td><td>22</td><td>-</td><td>30</td><td>-</td><td>-</td></tr><tr><td>Profit after negotiation</td><td>0</td><td></td><td>+7</td><td></td><td></td><td></td><td></td><td>0</td><td></td><td>+3</td><td></td><td></td></tr></table>

![](/api/attachments/3DGHKB6M/fulltext/images/f0e5ac1b74c903bf7a61df7b0cdf83394f57be3dc8239536bdd383b75334e87d.jpg)  
Fig. 8. Difference in the supply chain cost before and after negotiations.

First, we assume that the costs for simultaneous orders of all order combinations follow a clique model. Therefore, if the number of simultaneous orders increases, the cost also increases. Second, as the production capacity among manufacturers (or suppliers) is different, the costs for an individual order or for simultaneous orders are different.

Based on this data con<sup>fi</sup>guration, the three algorithms have been executed, and the results of their optimal solutions are illustrated in Fig. 10 above. In the case of Scenario 1 $( 1 0 \times 1 0 \times 1 0 )$ , Scenario 3 $( 8 \times 8 \times 8 )$ , and Scenario 4 $( 6 \times 1 0 \times 1 0 )$ , the optimal solutions of full enumeration and of agent negotiation coincide, thus proving that agent negotiation has generated an optimal solution. Scenario 2 $( 1 0 \times 8 \times 8 )$ and Scenario 5 $( 1 0 \times 6 \times 6 )$ have generated an error range of +2 and +3, respectively. Heuristic Branch-and-Bound has also generated a similar result.

The reason for errors in agent negotiation is, in case of Scenario 2 $( 1 0 \times 8 \times 8 )$ and Scenario $5 \left( 1 0 \times 6 \times 6 \right)$ , as the number of orders exceeds the number of members, many more simultaneous orders have occurred, and because of this, some partial combinations have been omitted in the process of agent negotiations. For example, in a case in which there are two second bests that have the same pro<sup>fi</sup>t of +2, the agent negotiation has considered only one second-best manufacturer. Because of this, the other second-best manufacturer has been omitted.

Therefore, for a more accurate test, these 3 scenarios—Scenario 1 $( 1 0 \times 1 0 \times 1 0 )$ , Scenario 4 $( 6 \times 1 0 \times 1 0 )$ , and Scenario 5 $( 1 0 \times 6 \times 6 ) -$ have been diversi<sup>fi</sup>ed with their data, and then a comparison has been made with a full enumeration. In addition, each algorithm per scenario has been performed ten times. Table 10 shows the average value and error rate of the optimal solutions of agent negotiation and the heuristic Branch-and-Bound, which have been compared with the optimal solution of a full enumeration.

Table 10 shows that 10 tests per scenario, for a total of 30 tests, have been performed. When agent negotiation has been compared with a full enumeration, the average error rate is 1.4%, and the largest error range is +4%. In addition, its optimal solution has been generated 13 times among a total of 30 times, thus producing optimal solutions of 43%. Next, the heuristic Branch-and-Bound has produced an average error rate of 1.9%, an error range of +6%, and optimal solutions of 10 times (33%) among a total of 30 tests.

![](/api/attachments/3DGHKB6M/fulltext/images/1f999472523a94f7f62eb86a017e414b81aafff1765d371b57ee17f4c069d836.jpg)  
Fig. 9. Comparison of optimal solutions in the random cost function.

![](/api/attachments/3DGHKB6M/fulltext/images/db85a5b99d88cd83918a14121196dc65dfe350424854dac20e5c2c689924f8de.jpg)  
Fig. 10. Comparison of optimal solutions in a given cost function

## 5.3. Computing test

Next, the computing tests for each algorithm have been conducted. For these computing tests, the computing time (milliseconds) for each scenario has been measured with a given cost function. The average computing time in the 10 tests for each of the 5 scenarios are summarized in Table 11.

Optimal solutions and error rates in a given cost function.

<table><tr><td rowspan="2" colspan="2">Number of order × number of manufacturers × number of suppliers</td><td rowspan="2">Times of test</td><td>Full enumeration</td><td colspan="3">Agent negotiation</td><td colspan="3">Heuristic Branch-and-Bound</td></tr><tr><td>Optimal solution</td><td>Result</td><td>Error range</td><td>Error rate</td><td>Result</td><td>Error range</td><td>Error rate</td></tr><tr><td rowspan="12">Scenario 1</td><td rowspan="12"> ${10} \times {10} \times {10}$ </td><td>1st</td><td>54</td><td>54</td><td>0</td><td>0.0%</td><td>55</td><td>+1</td><td>2.0%</td></tr><tr><td>2st</td><td>59</td><td>59</td><td>0</td><td>0.0%</td><td>60</td><td>+1</td><td>2.0%</td></tr><tr><td>3st</td><td>68</td><td>70</td><td>+2</td><td>3.0%</td><td>69</td><td>+1</td><td>1.0%</td></tr><tr><td>4st</td><td>49</td><td>50</td><td>+1</td><td>2.0%</td><td>49</td><td>0</td><td>0.0%</td></tr><tr><td>5st</td><td>53</td><td>55</td><td>+2</td><td>4.0%</td><td>53</td><td>0</td><td>0.0%</td></tr><tr><td>6st</td><td>62</td><td>63</td><td>+1</td><td>2.0%</td><td>64</td><td>+2</td><td>3.0%</td></tr><tr><td>7st</td><td>55</td><td>56</td><td>+1</td><td>2.0%</td><td>57</td><td>+2</td><td>4.0%</td></tr><tr><td>8st</td><td>49</td><td>49</td><td>0</td><td>0.0%</td><td>50</td><td>+1</td><td>2.0%</td></tr><tr><td>9st</td><td>45</td><td>45</td><td>0</td><td>0.0%</td><td>45</td><td>0</td><td>0.0%</td></tr><tr><td>10st</td><td>51</td><td>52</td><td>+1</td><td>2.0%</td><td>53</td><td>+2</td><td>4.0%</td></tr><tr><td>Average</td><td>54.5</td><td>55.3</td><td>+0.8</td><td>1.5%</td><td>55.5</td><td>+1</td><td>1.8%</td></tr><tr><td>Maximum error</td><td></td><td></td><td>+2</td><td>4.0%</td><td></td><td>+2</td><td>4.0%</td></tr><tr><td rowspan="12">Scenario 4</td><td rowspan="12"> $6 \times {10} \times {10}$ </td><td>1st</td><td>50</td><td>51</td><td>+1</td><td>2.0%</td><td>50</td><td>0</td><td>0.0%</td></tr><tr><td>2st</td><td>48</td><td>48</td><td>0</td><td>0.0%</td><td>48</td><td>0</td><td>0.0%</td></tr><tr><td>3st</td><td>49</td><td>49</td><td>0</td><td>0.0%</td><td>49</td><td>0</td><td>0.0%</td></tr><tr><td>4st</td><td>39</td><td>40</td><td>+1</td><td>3.0%</td><td>40</td><td>+1</td><td>3.0%</td></tr><tr><td>5st</td><td>62</td><td>63</td><td>+1</td><td>2.0%</td><td>64</td><td>+2</td><td>3.0%</td></tr><tr><td>6st</td><td>43</td><td>43</td><td>0</td><td>0.0%</td><td>44</td><td>+1</td><td>2.0%</td></tr><tr><td>7st</td><td>46</td><td>46</td><td>0</td><td>0.0%</td><td>46</td><td>0</td><td>0.0%</td></tr><tr><td>8st</td><td>51</td><td>51</td><td>0</td><td>0.0%</td><td>52</td><td>+1</td><td>2.0%</td></tr><tr><td>9st</td><td>50</td><td>51</td><td>+1</td><td>2.0%</td><td>50</td><td>0</td><td>0.0%</td></tr><tr><td>10st</td><td>52</td><td>52</td><td>0</td><td>0.0%</td><td>53</td><td>+1</td><td>2.0%</td></tr><tr><td>Average</td><td>49</td><td>49.4</td><td>+0.4</td><td>0.9%</td><td>49.6</td><td>+0.6</td><td>1.2%</td></tr><tr><td>Maximum error</td><td></td><td></td><td>+1</td><td>3.0%</td><td></td><td>+2</td><td>3.0%</td></tr><tr><td rowspan="12">Scenario 5</td><td rowspan="12"> ${10} \times 6 \times 6$ </td><td>1st</td><td>66</td><td>68</td><td>+2</td><td>3.0%</td><td>69</td><td>+3</td><td>5.0%</td></tr><tr><td>2st</td><td>69</td><td>72</td><td>+3</td><td>4.0%</td><td>73</td><td>+4</td><td>6.0%</td></tr><tr><td>3st</td><td>72</td><td>72</td><td>0</td><td>0.0%</td><td>74</td><td>+2</td><td>3.0%</td></tr><tr><td>4st</td><td>76</td><td>77</td><td>+1</td><td>1.0%</td><td>77</td><td>+1</td><td>1.0%</td></tr><tr><td>5st</td><td>82</td><td>83</td><td>+1</td><td>1.0%</td><td>82</td><td>0</td><td>0.0%</td></tr><tr><td>6st</td><td>84</td><td>84</td><td>0</td><td>0.0%</td><td>84</td><td>0</td><td>0.0%</td></tr><tr><td>7st</td><td>79</td><td>79</td><td>0</td><td>0.0%</td><td>80</td><td>+1</td><td>1.0%</td></tr><tr><td>8st</td><td>84</td><td>86</td><td>+2</td><td>2.0%</td><td>86</td><td>+2</td><td>2.0%</td></tr><tr><td>9st</td><td>86</td><td>89</td><td>+3</td><td>3.0%</td><td>89</td><td>+3</td><td>3.0%</td></tr><tr><td>10st</td><td>89</td><td>93</td><td>+4</td><td>4.0%</td><td>94</td><td>+5</td><td>6.0%</td></tr><tr><td>Average</td><td>78.7</td><td>80.3</td><td>+1.6</td><td>1.8%</td><td>80.8</td><td>+2.1</td><td>2.7%</td></tr><tr><td>Maximum error</td><td></td><td></td><td>+4</td><td>4.0%</td><td></td><td>+5</td><td>6.0%</td></tr><tr><td rowspan="2" colspan="4">Total Error range and error rate</td><td>Average</td><td>+0.93</td><td>1.4%</td><td>Average</td><td>+1.23</td><td>1.9%</td></tr><tr><td>Maximum</td><td>+4</td><td>4%</td><td>Maximum</td><td>+5</td><td>6%</td></tr><tr><td colspan="4">Generation times and rate of optimal solution</td><td>13 times/43%</td><td></td><td></td><td>10 times/33%</td><td></td><td></td></tr></table>

Table 11  
Average computing time in a given cost function.

<table><tr><td colspan="2">Number of orders × number of manufacturers × number of suppliers</td><td>Full enumeration</td><td>Agent negotiation</td><td>Heuristic Branch-and-Bound</td></tr><tr><td>Scenario 1</td><td>10×10×10</td><td>4,200,000 ms</td><td>289 ms</td><td>612 ms</td></tr><tr><td>Scenario 2</td><td>10×8×8</td><td>337,000 ms</td><td>291 ms</td><td>599 ms</td></tr><tr><td>Scenario 3</td><td>8×8×8</td><td>687 ms</td><td>189 ms</td><td>472 ms</td></tr><tr><td>Scenario 4</td><td>6×10×10</td><td>312 ms</td><td>161 ms</td><td>262 ms</td></tr><tr><td>Scenario 5</td><td>10×6×6</td><td>21,564 ms</td><td>194 ms</td><td>512 ms</td></tr></table>

As illustrated in Table 11, as the number of orders and the number of members increase, agent negotiation has performed much faster than a full enumeration. It also has performed slightly faster than a heuristic Branch-and-Bound. In the case of a full enumeration, when the number of orders and members has increased, its performance time has grown exponentially. However, it doesn't have much effect on the agent negotiation. In a case in which the number of orders is larger than the number of members, as in Scenarios 2 and 5, the performance time of agent negotiation has increased slightly because of increasing simultaneous orders. The heuristic Branch-and-Bound is also slightly affected by the number of orders and members, but it has performed much faster than a full enumeration.

Based on this test, the graph of computing time is as shown in Fig. 11. The computing time of a full enumeration has been excluded in Fig. 11, because in the case of Scenario 1 $( 1 0 \times 1 0 \times 1 0 )$ and Scenario $2 \left( 1 0 \times 8 \times 8 \right)$ , the computing time of a full enumeration is 20,000 ms, which is 1600 times longer than agent negotiation, and so it is impossible to be expressed in the graph. As illustrated in Fig. 11, the performance velocity of agent negotiation is about 3 times faster than a heuristic Branch-and-Bound. Through these tests, we can <sup>fi</sup>nd out that the performance of an agent negotiation algorithm is the best.

## 6. Conclusion

Information sharing in the supply chain enables supply chain members to seek superior competitiveness, to broaden the understanding of a systematic supply chain, and to become the starting point for mutual cooperation.

For transparent and reliable information sharing, this study has tried to develop agent negotiation as an optimal solution for allocating numerous orders to multiple members for supply chain formation. Multiple supply chain member's participation in the negotiations brings a pro<sup>fi</sup>t not only to the individual members but also a minimum cost to the whole supply chain. This is possible because all the changing costs coming from changing trade partners in the dynamic supply chain can be re<sup>fl</sup>ected in the negotiations. Agent negotiation makes it possible to calculate all the pro<sup>fi</sup>ts and losses in the process of negotiations on a real-time basis, thus providing the lowest cost for each member, with proper compensation. In this study, we have taken into consideration the earliness production and tardiness production cost based on a SET model, showing that the agent negotiation method achieves a superior supply chain formation compared to the heuristic and enumeration methods.

However, the limitations of calculations of the earliness production cost and tardiness production cost are considered the limitations of this research. Even though the random cost function and the given cost function have been used to calculate the manufacturing cost including above two cost, more accurate cost may be calculated when taking into consideration more detail factors such as the machine's capacity and inventory cost in order to obtain various applications in the supply chain problems.

In the future, the agent negotiation model used in this work can be extended to other <sup>fi</sup>eld of applications such as online ticket market and dynamic e-commerce as well, especially where the cost or price parameters vary according to coordination and environmental changes.

For further research, the negotiation mechanism can be restudied to <sup>fi</sup>nd new characteristics and axioms that can be used to build a new heuristic algorithm for variety of <sup>fi</sup>elds of resource allocation that should consider opportunity cost or compensation.

## Acknowledgments

This work was supported by the research fund of Dong-A University. We thank the anonymous reviewers for their helpful comments.

![](/api/attachments/3DGHKB6M/fulltext/images/61dcbeed640fa238b9c9214d31eb8d763dce6a354eca80b345edcd8da6931daa.jpg)  
Fig. 11. Performance velocity comparison between agent negotiation and heuristic Branch-and-Bound.

## Appendix A. De<sup>fi</sup>nition of negotiation factors

This section provides de<sup>fi</sup>nition of negotiation factors discussed in Section 4.4.

<table><tr><td>Negotiation factor</td><td>Definition</td></tr><tr><td>Current condition</td><td>An estimated cost for processing the order by initial scheduling of the manufacturers (or suppliers) that can accept the order</td></tr><tr><td>Best solution</td><td>The lowest value among the estimated producing cost quoted by the manufacturers</td></tr><tr><td>Simultaneous orders</td><td>More than two definite orders placed with a manufacturer (or a supplier); at this time, the manufacturer (or supplier) conducts rescheduling for simultaneous orders</td></tr><tr><td>Revised condition</td><td>A new estimated cost by rescheduling for simultaneous orders</td></tr><tr><td>Gross profit margin, negotiation leader, and negotiation partner</td><td>The margin between the current state and the revised state is called gross profit margin, and at this time, the negotiation participant who has the largest profit margin becomes the negotiation leader, and the rest become negotiation partners.</td></tr><tr><td>Second best and second-best profit margin</td><td>In the revised state, the lowest manufacturing cost among the manufacturers (or suppliers) except for the best solution. Second-best profit margin refers to the difference between the revised state and the second-best manufacturing cost.</td></tr><tr><td>Compensation for competitor</td><td>When a negotiation leader or a negotiation partner tries to go to the second-best manufacturer, it is possible that the said manufacturer already has a definite order placed; in this case, the manufacturer (or supplier) with a definite order becomes a competitor, and because of this definite order, simultaneous orders happen, consequently causing rescheduling for a new manufacturing cost, the revised state, which incurs additional cost to the competitor, referred to as compensation for competitor.</td></tr><tr><td>Compensation for transfer</td><td>This refers to the additional cost that is incurred when a negotiation partner transfers to the second-best manufacturer at the request of a negotiation leader.</td></tr><tr><td>Transfer cost</td><td>This refers to the additional cost that is incurred when a negotiation leader transfers to the second-best manufacturer.</td></tr><tr><td>Entry cost</td><td>Compensation for competitor + compensation for transfer</td></tr><tr><td>Negotiation leader&#x27;s negotiation amount</td><td>When an additional cost is incurred to a negotiation partner because of a negotiation leader&#x27;s request, the negotiation leader is to compensate him for the additional cost within his gross profit margin (or his second-best profit margin), referred to as negotiation amount.</td></tr><tr><td>Final profit margin</td><td>Final profit margin refers to a gross profit margin after all the negotiation steps</td></tr></table>

## References

[1] K.R. Baker, G.D. Scudder, Sequencing with earliness and tardiness penalties: a review, Operations Research Society of America 38 (1) (1990) 22–27.

[2] P.D. Bertsekas, The auction algorithm: a distributed relaxation method for the assignment problem, Annals of Operations Research 14 (1–4) (1988) 105–123.

[3] M. Caridi, S. Cavalieri, Multi-agent systems in production planning and control: an overview, Production Planning and Control 15 (2) (2004) 106–118.

[4] S.K. Chaharsooghi, J. Heydari, S.H. Zegordi, A reinforcement learning model for supply chain ordering management: an application to the beer game, Decision Support Systems 45 (Issue 4) (2008) 949–959.

[5] H.K. Chan, F.T.S. Chan, Comparative study of adaptability and <sup>fl</sup>exibility in distributed manufacturing supply chains, Decision Support Systems 48 (Issue 2) (2010) 331–341.

[6] K. Fischer, P. Jorg, M. Pischel, Cooperative transportation scheduling: an application domain for DAI, Journal of Applied Arti<sup>fi</sup>cial Intelligence, Special Issue on Intelligent Agents 10 (1) (1996) 1–31.

[7] P. Forget, S. D'Amours, J.M. Frayret, J. Gaudreault, Design of multi-behavior agents for supply chain planning: an application to the lumber industry, in: V. Kordic (Ed.), Supply Chain, Theory and Applications, I—Tech Education and Publishing, Vienna, Austria, 2008, pp. 558–568.

[8] Z. Guan, Application of decentralized cooperative problem solving in dynamic flexible scheduling, Proceedings of SPIE, vol, 2620, 1995, pp. 179–183, Bellingham. Wash.

[9] O.B. Kwon, K.C. Lee, MACE: multi-agents coordination engine to resolve con<sup>fl</sup>icts among functional units in an enterprise, Expert Systems with Applications 23 (1) (2002) 9–21.

[10] O. Labarthe, B. Espinasse, A. Ferrarini, B. Montreuil, Toward a methodological framework for agent-based modelling and simulation of supply chains in a mass customization context, Simulation Modeling Practice and Theory 15 (2) (2007) 113–136.

[11] W.Y. Liang, C.C. Huang, Agent-based demand forecast in multi-echelon supply chain, Decision Support Systems 42 (Issue 1) (2006) 390–407.

[12] F.R. Lin, H.C. Kuo, S.M. Lin, The enhancement of solving the distributed constraint satisfaction problem for cooperative supply chains using multi-agent systems, Decision Support Systems 45 (Issue 4) (2008) 795–810.

[13] J.U. Min, H. Bjornsson, Agent based supply chain management automation, Proceedings of the Eighth International Conference on Computing in Civil and Building Engineering (ICCCBE-VIII), 2000, pp. 1001–1006.

[14] T. Monteiro, D. Roy, D. Anciaux, Multi-site coordination using a multi-agents system, Computers in Industry 58 (4) (2007) 367–377.

[15] T. Moyaux, B. Chaib-draa, S. D'Amours, Multi-agent simulation of collaborative strategies in a supply chain, International Conference on Autonomous Agents, Proceedings of the Third International Joint Conference on Autonomous Agents and Multiagent Systems, vol. 1, 2004, pp. 52–59.

[16] M. Nagarajan, G. Sosic, Game-theoretic analysis of cooperation among supply chain agents: review and extensions, European Journal of Operational Research 187 (3) (2008) 719–745.

[17] C.C. Pei, A Branch-and-Bound approach for single-machine scheduling with earliness and tardiness penalties, Computers & Mathematics with Application 37 (10) (1999) 133–144.

[18] S.A. Petersen, M. Divitini, M. Matsken, An agent-based approach to modeling virtual enterprises, Production Planning and Control 12 (3) (2001) 224–233.

[19] M. Pinedo, Scheduling: Theory, Algorithms, and Systems, 2nd Edition, Prentice Hall 2001.

[20] C. Russ, G. Vierke, The matrix auction: a mechanism for the market-based coordination of enterprise networks, German Research Center for Arti<sup>fi</sup>cial Intelligence, Research Report RR-99-04, 1999.

[21] N.M. Sadeh, D.W. Hildum, D. Kjenstad, A. Tseng, MASCOT: an agent-based architecture for dynamic supply chain creation and coordination in the internet economy, Production Planning and Control 12 (3) (2001) 212–223.

[22] A.V. Smirnov, L.B. Sheremetov, N. Chilov, Soft-computing technologies for con<sup>fi</sup>g uration of cooperative supply chain, Applied Soft Computing 4 (1) (2004) 87–107.

![](/api/attachments/3DGHKB6M/fulltext/images/9d286121bcea48f2e21c5eacea18c414ebb9094cb30a4861e519ba02aefae9a2.jpg)  
Hyun Soo Kim is a Professor of Department of Management Information Systems at Dong-A University. He received his Ph.D. from Korea Advanced Institute of Science and Technology (KAIST) in 1992. He has been a visiting scholar in the MSIS Department at University of Texas at Austin (1997) and in the School of Computer Science at Carnegie Mellon University (2003). His primary research interests are agent systems, logistics information, and supply chain optimization. He has published papers in Decision Support Systems, Computers and Industrial Engineering, Journal of Organizational Computing and Electronic Commerce, and Fuzzy Sets and Systems. He has been listed in Marquis Who's Who in the world in the 2010 edition.

![](/api/attachments/3DGHKB6M/fulltext/images/b019914dab53c819fa6a5b7b34088fc71b6328e92f6a59ad188fc35958f3ea70.jpg)

Jae Hyung Cho is an Instructor of SIBAS (School of International Business and Area Studies) at Pusan University of Foreign Studies. He received his Ph.D. (2006) in Management Information Systems from Dong-A University, Korea. His current research interest includes Agent systems and negotiation in the e-Business and Logistics. He won the Best Paper award at the International Society of Applied Intelligence(IAE/EIA-2007).
