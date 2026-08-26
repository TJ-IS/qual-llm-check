---
otero_id: 7856
otero_key: "MKFNDPRA"
title: "Comparative study of adaptability and flexibility in distributed manufacturing supply chains"
authors: "H.K. Chan; F.T.S. Chan"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.09.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Comparative study of adaptability and <sup>fl</sup>exibility in distributed manufacturing supply chains

H.K. Chan <sup>a,</sup>⁎, F.T.S. Chan <sup>b</sup>

<sup>a</sup> Norwich Business School, University of East Anglia, Norwich, Norfolk, NR4 7TJ, UK

<sup>b</sup> Department of Industrial and Systems Engineering, The Hong Kong Polytechnic University, Hung Hom, Hong Kong

## a r t i c l e i n f o

Article history: Received 5 May 2008 Received in revised form 29 May 2009 Accepted 1 September 2009 Available online 11 September 2009

Keywords: Supply chain management Simulation Coordination Adaptability Flexibility

## a b s t r a c t

Supply chains need to be <sup>fl</sup>exible and adaptive because their operations are always subject to a variety of uncertainties like customer demand and supplier capacity, particularly for Make-to-Order (MTO) supply chains since their <sup>fl</sup>ow of materials is only triggered by customer orders. The main objective of this paper is to study how <sup>fl</sup>exibility and adaptability in delivery quantity and due date can improve the performance in a network of two-level multi-product MTO supply chains. Effect of uncertain customer demand and also supplier capacity, and supplier's capacity utilization are studied. Flexibility and adaptability are realized based on two proposed coordination mechanisms. Agent-based simulation is employed in this study to model the operations of supply chains. Performance of the system is measured in terms of a number of cost items and customer demand <sup>fi</sup>ll rate. Simulation results indicate that introduction of such <sup>fl</sup>exibility and adaptability can improve the aforementioned performance. However, there is a trade-off in selecting the coordination mechanism between adaptability and <sup>fl</sup>exibility subject to capacity utilization. Details and concluding remarks are discussed in this paper.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

Manufacturers are now operating as nodes in a network of suppliers, customers, and other specialized service functions. Independent companies usually work in a distributed or decentralized manner in such a complex network. These companies probably have no right to access sensitive information of the others. If any operational parameter, e.g. customer demand or supplier capacity studied in this paper, is uncertain, the situation becomes more complicated and traditional mathematical optimization techniques are unable to provide an optimal solution for such problems. There is a need for supply chain members to adapt to such uncertain environment in order to reduce any adverse impacts [24].

To accomplish this objective, information should be acquired, distributed, and interpreted [6]. However, information sharing is not always possible because it is not uncommon for companies to keep important information con<sup>fi</sup>dentially. In this connection, one key research motivation of this paper is to study the effect of adaptability without information sharing in distributed supply chains. Choi et al. [7] de<sup>fi</sup>ned adaptive behavior as the mechanism for assessing the current state of its external domain and incorporated this into its “decision” about future action in order to maintain autonomous and reasoning capabilities. In this paper, this is realized in terms of a coordination mechanism among supply chain members.

More speci<sup>fi</sup>cally, an adaptive coordination strategy (or sometimes referred to as a mechanism) with quantity <sup>fl</sup>exibility is proposed for distributed, multi-product manufacturing supply chain networks, subject to uncertainties in customer demand, supplier capacity and also supplier's capacity utilization. Quantity <sup>fl</sup>exibility is a coordination mechanism that allows a buyer to place an order earlier, or to make a commitment for a minimum quantity to be purchased from the supplier, who then provides the buyer with <sup>fl</sup>exibility to adjust the order quantity later, subject to the most updated and accurate demand information [30]. On the other hand, the proposed adaptability coordination mechanism allows a supplier to plan for production by adapting to the most recent information. A comparative study is conducted to contrast the two approaches.

In this study, agent-based simulation is employed to model the operations of the supply chain under study. Section 2 reviews related literature. A theoretical model with multiple suppliers and multiple customers in a multi-product supply chain network is formulated in Section 3. The two coordination mechanisms with quantity <sup>fl</sup>exibility and adaptability are also discussed in Section 3. Section 4 summarizes the simulation results for a selected supply chain con<sup>fi</sup>guration. Section 5 is the concluding section.

## 2. Review of the literature

Coordination of activities across a network of suppliers is essential for reacting quickly to uncertain environments. Helo [11] advocates that manufacturing <sup>fi</sup>rms could gain such competitive advantage via <sup>fl</sup>exibility. It is particularly important for Make-to-Order (MTO) supply networks since their <sup>fl</sup>ow of materials is triggered by dynamic customer orders, and there is little buffer inventory to protect the system from coordination inef<sup>fi</sup>ciencies [20]. Generally, an MTO strategy can reduce inventory level (i.e. reduce safety stock) at the downstream, but it usually leads to higher average lateness (i.e. increased variability in the production plans) [21]. This shortcoming was revealed by Cakravastia et al. [1], who compared an MTO strategy with other strategies in decentralized supply chain networks and concluded that the MTO strategy requires longer delivery lead times. Hwarng et al. [13] also found that an MTO policy is not that effective when realistic demand, which is obtained from a case study, is considered in a simulation study. In fact, supply chain performance entails a trade-off between cost and service (which can also be veri<sup>fi</sup>ed in the simulation results presented later), when service is measured in terms of <sup>fi</sup>ll rates [12], the fraction of demand that a supply chain can satisfy immediately [25].

Therefore, the main shortcomings of the reported literature can be broadly summarized as follows:

(i) if mathematical programming techniques are employed (e.g. [1,15,10], etc.), deterministic parameters (e.g. demand) are usually assumed in order to <sup>fi</sup>nd an optimal solution. In other words, system dynamics has not been studied, and uncertainty is not included in the analysis. Although it is possible to derive expected solution if the stochastic variables follow certain probabilistic distribution in some cases, strong assumptions on the distributions need to be made and the solution is just an expected solution, not really a closed form optimal solution;

(ii) more speci<sup>fi</sup>cally, if stochastic demand (or other parameters) is assumed, no optimal solution regarding inventory decision (and hence total system cost) could be found. Only approximate solutions can be found through other methodologies, like heuristic (i.e. stochastic optimization), by modeling some variables using probabilistic functions and global optimal solution may not be guarantee (e.g. [22,26,23,27], etc.);

(iii) the majority of the literature assumes that suppliers have in<sup>fi</sup>nite capacity utilization, which is not quite realistic (e.g. [15,10,22], etc.). The physical meaning of the capacity utilization is the ratio of average demand to the average capacity level of suppliers.

In this connection, this study aims at introducing coordination with <sup>fl</sup>exibility and adaptability in distributed supply chains in order to improve their performance subject to uncertainties. In response to (i), uncertainties in customer demand and supplier capacity are incorporated in this research. Like most studies in (ii), we are not aiming at <sup>fi</sup>nding the optimal solution of the problem under study, because it is virtually non-existent. In contrast with the studies in (ii), however, a coordination mechanism is proposed whereby the <sup>fi</sup>nal solution is determined dynamically based on the real-time information. The difference between this study and those under (ii) is that the solution of the latter is static in nature and is not responsive to uncertain environments. Finally, the effect of capacity utilization is also studied in this paper so that (iii) is addressed.

For coordinating decentralized plans, agent technology has attracted the attention of many researchers in recent years (e.g. [20,27,8,31,19,29], etc.). Nevertheless, many agent-based research areas have concentrated mainly on non-adaptive technology [16]. One way that such agents can be adaptive is to consider multiple ways to solve their sub-problems so that they can adjust their solution to produce the best possible result, subject to the restrictions on available processing, communication, and information resources, etc. For example, Calosso et al. [2] developed a negotiation model between a supplier and a customer for MTO operations, which is actually an agent-based system. They developed an analytical model for the problem and showed how the Pareto optimal solution among two <sup>fi</sup>rms may be identi<sup>fi</sup>ed. In fact, quantity <sup>fl</sup>exibility as proposed in this study is one of the possible ways to provide agents with a set of possible solutions so that the best solution could be <sup>fi</sup>nalized dynamically through the proposed coordination mechanism. Chan and Chan [4] applied an agent-based framework they developed earlier [3,5] to introduce quantity <sup>fl</sup>exibility approach in a distributed supply chain with single product type, and veri<sup>fi</sup>ed the effectiveness of the proposed approach in a simulation study. They also made use of the framework to conclude that, based on a simulation study, the <sup>fl</sup>exible approach can performance relatively well with respect to full information sharing [6], although they did not take adaptability into account.

Readers can refer to Lee and Kim's review [18] for a general review of more applications of multi-agent systems in manufacturing and supply chain applications. Agents can also be more adaptive if they are not restricted to solve one goal at a time, but are able to arrange their activities <sup>fl</sup>exibly to solve multiple goals concurrently. This is exactly the idea of the proposed adaptive coordination mechanism in this study. In this connection, agent-based simulation is employed to model supply chain members in this paper. More speci<sup>fi</sup>cally, the delivery quantity and due date in this study are “soft” requirements, represented by a window of allowable solution [14]. The <sup>fi</sup>nal solution can be adjusted dynamically through a series of coordination so that the <sup>fi</sup>nal delivery quantity and due date can be determined.

Based on the <sup>fi</sup>ndings above, it could be observed that:

(i) agent technology is a potentially useful tool to model and to analyze the behavior of supply chains; and

(ii) although an MTO production system could be a preferable strategy over other strategies, it does not outperform other strategies in terms of <sup>fi</sup>ll rate at the customer level (‘customer demand <sup>fi</sup>ll rate’ hereafter). More speci<sup>fi</sup>cally, the performance of an MTO strategy is not always the best in uncertain environments.

These observations lead to two research questions: (1) what kind of coordination mechanism should be employed in MTO-based supply chains; and (2) how should customer demand <sup>fi</sup>ll rate be improved in supply chains? In this connection, agent-based coordination mechanisms with <sup>fl</sup>exibility and adaptability have been developed and are tested on a supply chain subject to uncertainty in demand and supply capacity, for various levels of capacity utilization.

The objective of this paper is not to <sup>fi</sup>nd the optimal solution of supply chains through mathematical programming, since no optimal solution could be found when the system is subject to uncertainty. On the contrary, the main contribution of this paper is to study the usefulness, and to provide managerial insights, of adding <sup>fl</sup>exibility and adaptability through the proposed coordination mechanisms with respect to system dynamics. Another contribution is to study the effects of capacity utilization of suppliers (i.e. this is an independent parameter) in order to investigate its impact on the proposed coordination mechanisms.

## 3. Problem formulation

Two-echelon supply chain with multiple suppliers and customers is studied in this paper. The customers face uncertain demand as well as uncertain supply (see discussion later). In the model without coordination, the customers needs to make an inventory replenishment order based on stochastic order-up-to policy while the suppliers bid for an order based on their own capacity (which is not known to the customers) at the time the order is announced. Expected lead time is then reported to the customer who then makes a decision (select a supplier) based on expected cost subject to the reported lead time. On the other hand, the suppliers use MTO policy for production planning. This study mainly focuses on two coordination mechanisms: <sup>fl</sup>exible coordination and adaptive coordination. The former allows the customers to adjust the delivery quantity <sup>fl</sup>exibly based on the actual demand appear at the customers side when certain criteria are met. On the other hand, the latter allows the suppliers to adapt their production planning to the environment based on a coordination mechanism. This may create slack capacity arti<sup>fi</sup>cially. Details of the two mechanisms are discussed later. Notations used in this paper are listed in Table 1.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Indices
i = Index of suppliers,  $i \in \{1, 2, \ldots, I\}$ 
j = Index of customers,  $j \in \{1, 2, \ldots, J\}$ 
p = Index of product types,  $p \in \{1, 2, \ldots, P\}$ 
t = Index of periods,  $t \in \{1, 2, \ldots, T\}$ 

Parameters
 $b_{jp}$  = Unit backorder cost per period of customer j for product p
 $b_{ip}$  = Unit backorder cost per period of supplier i for product p
 $h_{jp}$  = Unit inventory holding cost per period of customer j for product p
 $S_{jip}$  = Setup cost per order, charge to customer j to order product p from supplier i
 $S_{jp}$  = Setup cost per order, charge to supplier i to produce product p
 $\mu_{jp}$  = Mean of demand function of product p of customer j
 $\sigma_{jp}$  = Standard deviation of demand function of product p of customer j
 $v_{jp}$  = Service level of product p that customer j would like to achieve

Variables
 $B_{ipt}$  = Backorder level of product type p of customer j at period t
 $C_{ipt}$  = Capacity limit (i.e. max daily capacity) of supplier i of product p at period t
 $d_{ipt}$  = Demand of product type p at customer j at period t,  $\in N(\mu_{jp}, \sigma_{jp})$ $I_{ipt}$  = Inventory level of product type p of supplier i at period t
 $I_{jpt}$  = Inventory level of product type p of customer j at period t
 $IP_{jpt}$  = Inventory position of product type p of customer j at period t
 $L_{jipt}$  = Order lead time of product p of customer j from supplier i
 $O_{jipt}$  = 1 if an order is established at period t between customer j and supplier i to produce product p; 0 otherwise.
 $OO_{ipt}$  = Outstanding orders of product p form supplier i at period t
 $OQ_{ipt}$  = Order quantity of product p in a bid from supplier j at period t
 $Q_{ijpt}$  = Quantity of product type p receives at period t from supplier i to customer j
 $S_{jp}$  = Order-up-to quantity of product p of customer j
 $SO_{ijpt}$  = Shortage quantity of product type p from supplier i to customer j at period t
 $T_{jp}$  = Review period of product p of customer j
Z = Total system cost over a period of time T
 $Z_{supplier}(i)$  = Total cost of supplier i over a period of time T
 $Z_{customer}(j)$  = Total cost of customer j over a period of time T
</div>

Each customer, j, sells a set of products which consists of at most P products. Customers place an order invitation according to some inventory replenishment policy (e.g. the stochastic order-up-to policy to be discussed in the next sub-section). Suppliers are invited to submit a bid for the customer's consideration for winning an offer. Bids are prepared subject to each supplier's inventory level of that product and its production planning based on outstanding order(s). The capacity of each supplier, i, is limited, i.e. they are capacitated. A setup cost for each order of product $p , S _ { j i p } ,$ is incurred whenever an order is established between customer j and supplier i, and it is charged to customer j. On the other hand, a setup cost, $S _ { i p } ,$ is also incurred and charged to the supplier in order to produce product $p .$ The event that an order is established is represented by the binary function $O _ { j i p t }$ in the model as discussed below. In this connection, the total cost for customer j, $Z _ { \mathrm { c u s t o m e r } } ( j )$ , over a period T can be calculated by Eq. (1):

$$
Z _ {\text { customer }} (j) = \sum_ {t = 1} ^ {T} \left[ \sum_ {p} \left(h _ {j p} I _ {j p t} + b _ {j p} B _ {j p t}\right) + \sum_ {i} S _ {j i p} O _ {j i p t} \right]\tag{1}
$$

subject to:

$$
I _ {j p (t - 1)} - B _ {j p (t - 1)} + \sum_ {i} Q _ {i j p t} - I _ {j p t} + B _ {j p t} = d _ {j p t}\tag{2}
$$

$$
I _ {j p t} B _ {j p t} = 0\tag{3}
$$

$$
O _ {j i p t} \in \{0, 1 \}\tag{4}
$$

$$
I _ {j p t}, B _ {j p t}, Q _ {i j p t} \geq 0 \forall i, j, p, \text { and } t\tag{5}
$$

The <sup>fi</sup>rst two items of Eq. (1) represent total inventory holding cost and backorder cost. $I _ { j p t }$ and $B _ { j p t }$ are inventory level and backorder level of product type p of customer j at period t respectively. The terms $h _ { j p }$ and $b _ { j p }$ are unit inventory holding cost per period and unit backorder cost per period of customer j for product p, respectively. The last item of Eq. (1) is the total setup cost, which includes the ordering cost. The demand, $d _ { j p t } ,$ in Eq. (2) is modeled by a Normal distribution, which is one of the independent variables (to be discussed in a later section). Demand occurs at the beginning of a period. Constraint (2) balances the inventory level, $I _ { j p t } ,$ at the end of period t. Any un<sup>fi</sup>lled demand is backordered. Constraint (3) ensures the inventory level and backorder level cannot simultaneously exceed zero. Constraints (4) and (5) are technological constraints.

The cost to a supplier $, Z _ { s u p p l i e r } ( i )$ , over T periods is given by Eq. (6):

$$
Z _ {\text { supplier }} (i) = \sum_ {t = 1} ^ {T} \left[ \sum_ {p} h _ {i p} I _ {i p t} + \sum_ {j} S _ {i p} O _ {j i p t} \right]\tag{6}
$$

subject to:

$$
I _ {i p t} - I _ {i p (t - 1)} + \sum_ {j} Q _ {i j p t} \leq C _ {i p t}\tag{7}
$$

$$
O _ {j i p t} \in \{0, 1 \}\tag{8}
$$

$$
I _ {i p t}, C _ {i p t}, Q _ {i j p t} \geq 0 \forall i, j, p, \text {   and   } t\tag{9}
$$

The <sup>fi</sup>rst item of Eq. (6) represents the total inventory holding cost of the supplier and the second term represents the total setup cost. The variable $h _ { i p }$ is the unit inventory holding cost per period of supplier i for product p. Unlike the case for the customer, there is no backorder cost involved in the above cost function. Constraint (7) bounds the inventory level of product type p of supplier i for period t, $I _ { i p t } ,$ while $C _ { i p t }$ is the capacity limit of supplier i for product type p at the end of period t. In this paper, this parameter, $C _ { i p t } ,$ is normally distributed and is another independent variable of the simulation study. Constraints (8) and (9) are technological constraints. The total system cost of the supply chain is thus given by Eq. (10):

$$
\begin{array}{l} Z = \sum_ {i} Z _ {\text { supplier }} (i) + \sum_ {j} Z _ {\text { customer }} (j) \\ = \sum_ {t = 1} ^ {T} \left\{\sum_ {i} \left[ \sum_ {p} h _ {i p} I _ {i p t} + \sum_ {j} S _ {i p} O _ {j i p t} \right] \right. \\ \left. + \sum_ {j} \left[ \sum_ {p} \left(h _ {j p} I _ {j p t} + b _ {j p} B _ {j p t}\right) + \sum_ {i} S _ {j i p} O _ {j i p t} \right] \right\} \end{array}\tag{10}
$$

The above mathematical model could be further re<sup>fi</sup>ned as a mathematical programming model (e.g. mixed integer programming). However, it is not feasible to <sup>fi</sup>nd an optimal solution to the problem because of the reasons discussed in Section 2. Coordination among decentralized entities is proposed instead to <sup>fi</sup>nd a “good” solution as compared to the stochastic model which is described below.

## 3.1. Stochastic order-up-to policy

The previous section describes the operations of the model mathematically. Under a distributed and uncertain environment, customers could make use of an order-up-to policy for inventory replenishment. On the other hand, suppliers could use MTO strategy for production planning. Otherwise, the risk of excessive inventory is very high. In a multi-product environment, Viswanathan [28] proposed a periodic review order-up-to policy, which is implemented on each individual product. This forms the basis of the stochastic model in this study which is considered as the benchmark of the proposed coordination mechanisms. A brief description of the model is presented below.

Subject to stochastic demand, customers monitor their own inventory position of each product type p periodically, in order to place an order. The inventory position of product type p of customer j at period t (i.e. $I P _ { j p t } )$ is de<sup>fi</sup>ned as the sum of existing inventory $( \mathrm { i } . \mathrm { e } . I _ { j p t } )$ backorders at period t (i.e. $B _ { j p t } ) _ { \ l }$ , and all outstanding orders from all suppliers i at period $t ( O O _ { i p t } ) , \mathrm { i . e . }$

$$
I P _ {j p t} = I _ {j p t} - B _ {j p t} + \sum_ {i} O O _ {i p t}\tag{11}
$$

The customer updates its inventory level every period according to Eq. (2). Basically a customer issues an invitation periodically to suppliers for submitting bids for a product type $p .$ The order quantity, $O Q _ { j p t } ,$ , is the difference between the inventory position of product type p and the order-up-to quantity, $S _ { j p } ,$ , of product p at period t as follows:

$$
O Q _ {j p t} = S _ {j p} - I P _ {j p t}\tag{12}
$$

In Eq. (12), $S _ { j p }$ is calculated by Eq. (13) in the stochastic model:

$$
S _ {j p} = \mu_ {j p} \left(T _ {j p} + L _ {j i p}\right) + v _ {j p} \sigma_ {j p} \sqrt {\left(T _ {j p} + L _ {j i p}\right)}\tag{13}
$$

The last term of Eq. (13) (i.e. $v _ { j p } \sigma _ { j p } \sqrt { \left( T _ { j p } + L _ { j i p } \right) ) }$ is known as safety stock, which serves as a buffer to uncertainties. In Eq. (13), $L _ { j i p }$ does not take the uncertainty of supplier capacity into consideration. This is because customers cannot know the variability of suppliers' capacity as sharing of information is not allowed in the supply chains. In practice, customers may multiply the (expected) lead time $L _ { j i p }$ by a safety factor to add safety margin. In general, the higher the service level, the larger is the size of the safety stock. The service level of product type p of customer j, ${ v } _ { j p } ,$ is given by the following equation:

$$
v _ {j p} = \Phi^ {- 1} \left[ \frac {b _ {j p}}{b _ {j p} + h _ {j p}} \right]\tag{14}
$$

where $\phi ( . )$ is the probability density function of the normal distribution.

Suppliers reply to the customer based on their own capacity utilization and outstanding orders. All suppliers can submit a bid but the proposed lead time is different for different suppliers since each supplier has different outstanding orders. Without loss of generality, transportation lead time is incorporated in the production lead time so that the former is assumed to be zero. This is a common assumption in the literature. After the customer has received all the bids, the one with the shortest delivery due date is selected. The reason that price is not taken into consideration is because competition among supply chain members is not assumed in this study. In other words, supply chain members are cooperation-oriented with respect to the coordination mechanism so that the price is <sup>fi</sup>xed due to the noncompetition-based market. If price is taken into account, then noncooperative mechanisms have to be developed, which is outside the scope of this paper.

In the mean time, suppliers update their inventories according to their daily capacity, which is modeled by a normal distribution, if there is any outstanding order. Production is scheduled according to the due date of the outstanding bids: the one with the earliest due date is processed <sup>fi</sup>rst. Subject to uncertain production capacity, it is possible that the supplier does not have suf<sup>fi</sup>cient inventory for a particular product type when the due date of the corresponding order is reached. The quantity is represented by the variable $S O _ { i j p t } .$ In such a case, a penalty which is equal to the backorder cost due to this shortage, if any, is charged by the customer to the supplier. This cost does not affect the total system cost because it is just a “zero-sum” penalty. However, this action is necessary because the individual cost of the supplier and customer are also examined in this study (see Section 4.5). Therefore, this penalty cost which stems from the supplier's uncertainty is incurred. Eqs. (1) and (6) can then be rewritten as Eqs. (1a) and (6a) respectively in calculating the customers' cost and the suppliers' cost:

$$
Z _ {\text { customer }} (j) = \sum_ {t = 1} ^ {T} \left[ \sum_ {p} \left(h _ {j p} I _ {j p t} + b _ {j p} B _ {j p t}\right) + \sum_ {i} S _ {j i p} O _ {j i p t} - \sum_ {p} \sum_ {i} b _ {j p} S O _ {i j p t} \right]\tag{1a}
$$

$$
Z _ {\text { supplier }} (i) = \sum_ {t = 1} ^ {T} \left[ \sum_ {p} h _ {i p} I _ {i p t} + \sum_ {j} S _ {i p} O _ {j i p t} + \sum_ {p} \sum_ {j} b _ {j p} S O _ {i j p t} \right]\tag{6a}
$$

The inventory cost, backorder cost, and penalty cost of each entity are updated at the end of each period.

## 3.2. The MTO coordination mechanism

Chan and Chan [4] discussed how to make use of quantity <sup>fl</sup>exibility in a contract to react to uncertainties. The concept is to make use of the safety stock in the stochastic order-up-to policy as a window of possible delivery quantity (called a quantity range hereafter) to be shipped from a supplier to a customer. In other words, the order quantity is not a <sup>fi</sup>xed quantity for each order as described in Eq. (12) in Section 3.1 (i.e., this parameter is not adjusted based on the latest information). Instead, a range of quantity is set up with a width equal to double of the safety stock. Sensitivity analysis of this width is conducted and results subject to ranges of different window are quite consistent as long as this range is wide enough for the coordination to take place. Therefore, a one-side width equivalent to the value of the safety stock is chosen so that it is fair to make a comparison with the stochastic model of the same safety stock. In other words, the upper bound of this range is equal to the one used in the stochastic model. The actual quantity to be shipped is determined through a coordination mechanism.

## 3.3. The adaptive MTO coordination mechanism

This section summarizes the principle of the adaptive MTO coordination mechanism. As described in Section 3.2, suppliers are allowed to complete an order with a delivery quantity which falls within a pre-de<sup>fi</sup>ned quantity range. Compared with a <sup>fi</sup>xed quantity of each order in the stochastic order-up-to policy, suppliers in fact have the <sup>fl</sup>exibility to allocate slack capacity for producing the next order to be processed in the queue. The rationale behind the proposed adaptive MTO coordination mechanism is to “create” slack capacity according to the actual demand and supply requirements (i.e. adapt to the situations). In other words, the production process of a product would stop before the maximum quantity is produced and switch to produce the product of the next planned order. One may argue that it would induce more slack capacity if the supplier stops production of the current order at the minimum quantity of the range. However, this would only result in shorter and shorter ordering cycles because customers keep receiving less quantity in each cycle. This also makes the <sup>fl</sup>exible nature of the proposed coordination mechanism useless. Therefore, a balanced scheme has to be designed in order to come up with a compromise between the production quantity of the current order and the slack capacity for the next order.

In other words, the adaptive MTO coordination mechanism helps customers and suppliers to make the following decision: When should a supplier stop production for a product and then switch to the production for the next order after the lower bound of the quantity range of the current order has attained? In the original coordination scheme, the customer takes the initiative to request completion of an order, unless the deadline of a contract is due. In the adaptive MTO coordination mechanism, this assumption is relaxed so that suppliers can send a message to the customer in order to $" \mathrm { a s k } "$ for “advice” whether or not the production can be stopped. Note that suppliers need to send a message to obtain feedback from a customer because no information sharing is assumed. Details of operations are discussed below. De<sup>fi</sup>nitions of additional symbols that are used in the adaptive coordination mechanism can be found in Table 2.

Whenever a supplier has produced at least the lower bound of the quantity range with respect to a contract, and provided that the supplier has another outstanding order in the future (remark: MTO is still the dominant strategy and the supplier does not want to make any inventory solely for buffering uncertainties), the supplier is allowed to send a request to the retailer. In fact, the request is a signal to the customer that the supplier would like to stop production of the current order at a quantity lower than the upper bound of the contract quantity. Mathematically, once the inventory level of a product $p$ of supplier i at time $t , \ I _ { i p t } ,$ satis<sup>fi</sup>es the inequality (15), the adaptive coordination mechanism is triggered:

$$
I _ {i p t} \geq C Q _ {l b} + A (C Q _ {h b} - C Q _ {l b})\tag{15}
$$

This is the <sup>fi</sup>rst constraint that is added to the original coordination mechanism. Upon receipt of this message, the customer has to make a decision to accept this request or not. Since the customer does not know the exact inventory which has been produced by supplier i (remark: information is not shared explicitly as assumed), the customer can only estimate the variable A from a rational expectation point of view as a fraction of quantity range with respect to the fraction of due date elapsed as stated in Eq. (16):

$$
A ^ {\prime} = \frac {t - D D _ {l b}}{D D _ {h b} - D D _ {l b}}\tag{16}
$$

By taking this estimation into account, the customer is able to estimate the date of delivery (counting from this period), t′, according to its inventory level, $I _ { j p t } ,$ as stated in $\operatorname { E q . }$ (17). The quantity to be shipped from supplier $i , Q _ { i j p t } ^ { \prime }$ , can also be estimated from Eq. (18):

$$
t ^ {\prime} = I _ {j p t} / \mu_ {j p}\tag{17}
$$

$$
Q _ {i j p t} ^ {\prime} = C Q _ {l b} + A ^ {\prime} (C Q _ {h b} - C Q _ {l b})\tag{18}
$$

Additional variables in the adaptive coordination mechanism.

<table><tr><td colspan="2">Additional variables</td></tr><tr><td>A</td><td>= Fraction of quantity range to be produced in order to trigger the proposed adaptive mechanism, A∈[0,1]</td></tr><tr><td>A&#x27;</td><td>= Estimated value of A by a customer, A&#x27;∈[0,1]</td></tr><tr><td>Cost(x)</td><td>= Expected cost if the expected quantity to be shipped by the supplier is x</td></tr><tr><td>COST</td><td>= Set of Cost(x)</td></tr><tr><td>CQlb</td><td>= Lower bound of the contract quantity in a particular contract</td></tr><tr><td>CQhb</td><td>= Higher bound of the contract quantity in a particular contract</td></tr><tr><td>Dlb</td><td>= Lower bound of the contract due date in a particular contract</td></tr><tr><td>Dhb</td><td>= Higher bound of the contract due date in a particular contract</td></tr><tr><td>Qijpt&#x27;</td><td>= Estimated value of Qijpt by a customer</td></tr><tr><td>t&#x27;</td><td>= Estimated value of the date of delivery of a particular contract (this is an offset value which is counting from the current period)</td></tr></table>

Customer j needs to estimate t′ because even if supplier i can stop production of the existing contract for product p for customer j, the customer can request the supplier to ship the product within the due date range according to the contract. In other words, the supplier is still liable to keep the inventory until the contract is <sup>fi</sup>nished according to the original coordination mechanism. In fact, sensitivity analysis on different values of A yields similar results when A is around 0.5. Therefore, the simulation results presented in this paper use $A = 0 . 5$ (in fact, if A is a random variable, the expected value of it is 0.5).

Then, the customer makes use of their expected inventory level to calculate a set of expected short term costs from Eq. (1) by varying $Q _ { i j p t }$ from $Q _ { j j p t } { ' }$ to $C Q _ { h b }$ until the next review period:

$$
\operatorname{COST} = \left\{\operatorname{Cost} \left(Q _ {i j p t} ^ {\prime}\right), \operatorname{Cost} \left(Q _ {i j p t} ^ {\prime} + 1\right), \dots , \operatorname{Cost} \left(C Q _ {h b}\right) \right\}\tag{19}
$$

where Cost(x) is the expected cost if the expected quantity to be shipped by the supplier is x. De<sup>fi</sup>nition of cost items are the same as discussed in the previous sub-sections.

The customer then takes one of the following actions:

(i) If the minimum value of the set COST is equal to $\cos \mathrm { t } ( Q _ { i j p t } ^ { \prime } )$ , i.e. min $( \mathsf { C O S T } ) { = } \mathsf { C o s t } ( Q _ { i j p t } ^ { } ^ { \prime } )$ , implying that customer's short term inventory level is high enough to cover the short term demand if the supplier stops production, the customer would accept the supplier's request. However, as discussed previously, shipment is not made instantly. It still follows the original coordination mechanism because the customer still has the <sup>fl</sup>exibility to request for shipment later. In other words, the supplier making the request suffers from inventory cost for a short period of time.

(ii) In contrast, $\operatorname { i f } \operatorname* { m i n } ( \mathrm { C O S T } ) \neq \mathrm { C o s t } ( Q _ { i j p t ^ { ' } } ) ,$ , the customer is suffering from low short term inventory if the supplier produces less and the customer would thus refuse the request. The supplier is responsible to carry out production for the original contract, i.e. make product p for customer j.

This is an iterative process until the contract is completed. This scheme is adaptive because decisions are based on real-time information, rather than on the planned schedule. Together with the quantity <sup>fl</sup>exibility proposed in this paper, the overall scheme is <sup>fl</sup>exible and adaptive. In the subsequent discussion, when the phase “adaptive coordination mechanism” is addressed, it refers to the <sup>fl</sup>exible and adaptive coordination mechanism as discussed in this section and the word <sup>fl</sup>exible is, for simplicity, not stated explicitly.

The <sup>fl</sup>exible MTO and adaptive MTO strategies originate from the same quantity <sup>fl</sup>exibility philosophy. Both strategies make use of the <sup>fl</sup>exibility that is introduced through the coordination mechanism so that delivery quantity and due date are determined subject to uncertain demand and supply, which are uncontrollable factors of suppliers and customers. However, the major difference between them is that the adaptive MTO searches for “slack capacity” for the next order, which is for another product type in most cases. This is crucial in a multi-product environment subject to limited capacity as on one hand the supplier should produce suf<sup>fi</sup>cient quantities for the existing order for a product type; in the mean time she wants to start production for the next order as early as possible subject to an uncertain environment. In this connection, the adaptive MTO strategy helps the supplier resolve this dilemma through the proposed coordination mechanism. By adopting the proposed adaptive MTO strategy, a more accurate production planning can be achieved.

## 4. Results and discussions

A simulation study has been carried out to verify the usefulness of the proposed supply chain coordination with <sup>fl</sup>exibility and adaptability, and to provide a comparative study to show whether <sup>fl</sup>exibility alone, or both <sup>fl</sup>exibility and adaptability would be better. The simulation program is written in JAVA. In order to improve the robustness of the simulation results, a number of precautions have been carried out before actual measurements have been recorded.

Firstly, each simulation setting is run with 10 different random seeds and the average is reported in order to minimize the random effect [17]. Together with the 144 sets of independent variables (to be discussed), a total of 1440 simulation runs are carried out for each strategy. Since there are 3 sets of strategy, the total number of simulation runs is $1 4 4 0 \times 3 = 4 3 2 0$ sets. Secondly, in order to determine the run length and the warm up period (i.e. transient behavior) of the simulation study, the output stochastic process has been analyzed as suggested by Law and Kelton [17]. It is found that, with some safety margin, the warm up period and the run length of each simulation run are 100 periods and 465 periods respectively. The <sup>fi</sup>nal performance measures are based on the last 365 periods (i.e. $T = 3 6 5 )$ . If one period is equal to 1 day, then the effective length of the simulation run is 1 year. Finally, in order to minimize the effect of inventory shortage during the warm up period, initial inventory is added at the customer end so that each customer has an inventory equal to the mean daily demand and the mean ordering plus delivery lead time for the next order. Since the production environment is MTO, no initial inventory is provided for suppliers.

In order to simplify the discussion, the three strategies are referred to as follows:

Stochastic order-up-to policy—stochastic model;

MTO coordination with quantity <sup>fl</sup>exibility—<sup>fl</sup>exible MTO;

Adaptive MTO coordination with quantity <sup>fl</sup>exibility—adaptive MTO.

## 4.1. The supply chain

In the simulation study, there are three customers $\left( J = 3 \right)$ and four suppliers $( I { = } 4 )$ . The total number of product types is three $( P { = } 3 ) . \mathsf { A }$ number of combinations of product types, customers, and suppliers were studied. However, it is found that the behavior subject to the three strategies is quite independent of the combinations. Different combinations will of course lead to results of different magnitude but the same conclusion and discussion in later sections are still applicable. The reason behind this is the cooperative nature of the supply chain, which is discussed in Section 3.1. In this connection, only one setting is presented here, i.e. each customer sells only one of the product types, and all the four suppliers are able to produce all these three products.

## 4.2. Dependent variables

Total system cost, and a variety of components such as inventory cost, backorder costs, and supplier costs, etc., along with customer demand <sup>fi</sup>ll rate are recorded as performance measures (i.e. dependent variables) for comparing the MTO coordination mechanism and the adaptive MTO coordination mechanism, against the stochastic model. Customer demand <sup>fi</sup>ll rate is used as a measure to re<sup>fl</sup>ect customer satisfaction [12]. These two variables (total system cost and <sup>fi</sup>ll rate) normally con<sup>fl</sup>ict with each other as a good <sup>fi</sup>ll rate could be achieved by employing more safety stock, which incurs cost. A balance of these two variables is needed but mathematical modeling usually can optimize one of them while leaving the other unattended. In fact, it is found that with <sup>fl</sup>exibility and adaptability, the two performance measures can be improved simultaneously.

## 4.3. Independent variables

There are three sets of independent variable in this study. Demand uncertainty and supply uncertainty (i.e. variation of capacity of each supplier) are two of them. Each of these variables is modeled by varying the variance of the corresponding normal distribution at four levels. Therefore, there are 16 sets (4×4) of different simulation runs for each strategy as summarized in Table 3.

Different settings of the simulation study.

<table><tr><td rowspan="2">Setting</td><td>Demand uncertainty (see Note)</td><td>Supply uncertainty (see Note)</td></tr><tr><td>In percentage</td><td>In percentage</td></tr><tr><td>1</td><td>10%</td><td>10%</td></tr><tr><td>2</td><td>10%</td><td>20%</td></tr><tr><td>3</td><td>10%</td><td>30%</td></tr><tr><td>4</td><td>10%</td><td>40%</td></tr><tr><td>5</td><td>20%</td><td>10%</td></tr><tr><td>6</td><td>20%</td><td>20%</td></tr><tr><td>7</td><td>20%</td><td>30%</td></tr><tr><td>8</td><td>20%</td><td>40%</td></tr><tr><td>9</td><td>30%</td><td>10%</td></tr><tr><td>10</td><td>30%</td><td>20%</td></tr><tr><td>11</td><td>30%</td><td>30%</td></tr><tr><td>12</td><td>30%</td><td>40%</td></tr><tr><td>13</td><td>40%</td><td>10%</td></tr><tr><td>14</td><td>40%</td><td>20%</td></tr><tr><td>15</td><td>40%</td><td>30%</td></tr><tr><td>16</td><td>40%</td><td>40%</td></tr></table>

Note: level of uncertainty is modeled by varying the standard deviation of the norma distribution, which is expressed as a percentage of the mean (i.e. coef<sup>fi</sup>cient of variation) in the table.

In addition, capacity utilization is the third independent variable. It can be varied at three levels: high, medium, and low, which are set as a percentage relative to the average demand in the simulation settings. For each level, three sub-levels are presented so that it acts as sensitivity analysis and to strengthen the conclusions of this simulation study. This is illustrated in Table 4. In other words, there are 9 capacity utilizations to be studied for each strategy. Altogether, there are $9 \times 1 6 = 1 4 4$ settings of independent variables. In the simulation, total average demand is set equal to the total average supply capacity. Since they are stochastic variable, the actual number per unit of each agent is different. As a matter of fact, a number of combination by varying this setting (e.g. mean demand higher than mean capacity, different agent has different settings, etc.) are studied, the general behavior is the same (but with different magnitude, of course) so only the aforementioned setting is presented in this paper.

## 4.4. Total system cost

Figs. 1 and 2 summarize the simulation results in terms of percentage improvement in total system costs against the stochastic model for the <sup>fl</sup>exible MTO and adaptive MTO, respectively. Percentage improvement of a variable is given by Eq. (20):

$$
\text { Percentage   Improvement } = - \frac {\text { Cost } _ {\mathrm{MTO}} - \text { Cost } _ {\mathrm{STO}}}{\text { Cost } _ {\mathrm{STO}}} \times 1 0 0\tag{20}
$$

where ${ \mathrm { C o s t } } _ { \mathrm { M T O } }$ is the cost of either the MTO or the adaptive MTO strategy, and $\mathtt { C o s t } _ { \mathtt { S T O } }$ is the cost from the stochastic model. A negative sign is inserted in order to ease the readability of the graph. Therefore, the more positive the percentage improvement, the better the system behaves. The same formula is applied to both <sup>fl</sup>exible MTO and adaptive MTO.

Different capacity utilizations of the simulation study.

<table><tr><td>Capacity utilization</td><td>Setting (see Note)</td></tr><tr><td>Low</td><td>L1, L2, L3</td></tr><tr><td>Medium</td><td>M1, M2, M3</td></tr><tr><td>High</td><td>H1, H2, H3</td></tr></table>

Note: capacity utilization can be ranked in the following orders $\mathrm { L } 1 < \mathrm { L } 2 < \mathrm { L } 3 < \mathrm { M } 1 < \mathrm { M } 2 <$ $\mathrm { M } 3 < \mathrm { H } 1 < \mathrm { H } 2 < \mathrm { H } 3 ,$ , regardless of their category as low, medium, or high.

![](/api/attachments/MKFNDPRA/fulltext/images/ca8c4121b6b78297dfa72c76842f48ab12a7445215ac14502fa48e2b82db34b3.jpg)  
(a) Low capacity utilizations

![](/api/attachments/MKFNDPRA/fulltext/images/f0bb5e5b6a1fc480d33740f6cefaa4f7f90323fb33ba83f6d8acc384155fc9a6.jpg)  
(b) Medium Capacity utilizations

![](/api/attachments/MKFNDPRA/fulltext/images/9da00b994d10af8575dcba30b641f5cc76723fbd4290d74d4dd968d39718b697.jpg)  
(C) High Capacity utilizations  
Fig. 1. Percentage improvements in total system cost at different capacity utilizations— <sup>fl</sup>exible MTO against stochastic model.

Fig. 1 shows that <sup>fl</sup>exible MTO can save a large portion of cost when compared with the stochastic model at low and medium capacity utilizations (Fig. 1(a) and (b) respectively). However, this is not true at high capacity utilization (Fig. 1(c)). A t-test is conducted to verify this observation and the results are summarized in Table 5. As from Table 5, the alternative hypothesis that the percentage improvement in total cost of <sup>fl</sup>exible MTO as compared with stochastic model is higher than zero (i.e. positive as in the Fig. 1) at low and medium capacity utilizations is highly signi<sup>fi</sup>cant, as the p-value of various simulations settings are 0, which is in effect valid for any con<sup>fi</sup>dence interval. On the other hand, we cannot reject the null hypothesis at any reasonable level of signi<sup>fi</sup>cance when the capacity utilization is high (i.e. levels H1 to H3). Similar statistical output analysis has been conducted for different simulation settings to verify the <sup>fi</sup>ndings. However, they are not reproduced here to simplify the discussions below.

The reason behind this observation is explained below. If the capacity utilization is much higher than the average demand requirement, a direct consequence is that the supplier is able to shorten the delivery cycle because more capacity could be allocated to produce a certain product. In other words, the response of the whole system is speeded up by the excess capacity, which diminishes the effect of the <sup>fl</sup>exibility. The <sup>fl</sup>exible coordination mechanism would work well at tight capacity utilization environment, which is true for most manufacturing companies as few would invest for over-capacity requirement.

![](/api/attachments/MKFNDPRA/fulltext/images/e7cba7dd426746f1fa306ff91c6cd25e683995398ae3f201c9fcdafe815d9939.jpg)  
(a) Low capacity utilizations

![](/api/attachments/MKFNDPRA/fulltext/images/6e1c4afaba1afa0362791cfedb4e33f35a587aeb5bb63dea56a4cda4a61c3f89.jpg)  
(b) Medium Capacity utilizations

![](/api/attachments/MKFNDPRA/fulltext/images/287554e71059feb0ea3fe58ae7e31004a9ce6400896a852f380d9f38a989ea70.jpg)  
(c) High Capacity utilizations  
Fig. 2. Percentage improvements in total system cost at different capacity utilizations— adaptive MTO against stochastic model.

On the contrary, Fig. 2 shows that improvement in total system cost could be obtained by employing adaptive MTO for all three capacity utilizations. The adaptability feature of the coordination mechanism helps to allocate the capacity in a better manner than the <sup>fl</sup>exible MTO at high capacity utilizations. This is because the former looks for re-allocation of resource according to the actual environment. In other words, adaptive MTO can gain the bene<sup>fi</sup>ts of <sup>fl</sup>exibility in the coordination mechanism at low to medium capacity utilizations (as shown in Fig. 1) and can improve the poor performance of the <sup>fl</sup>exible MTO at high capacity utilizations.

Table 5  
t-test on the percentage improvement in total cost.

<table><tr><td rowspan="2">Capacity utilization</td><td rowspan="2">Mean percentage improvement</td><td rowspan="2">t-value</td><td rowspan="2">p-value</td><td colspan="2">Reject  $H_o?$ </td></tr><tr><td>At 95% confidence interval</td><td>At 99% confidence interval</td></tr><tr><td>L1</td><td>0.674</td><td>18.02</td><td>0.000</td><td>Yes</td><td>Yes</td></tr><tr><td>L2</td><td>1.089</td><td>13.37</td><td>0.000</td><td>Yes</td><td>Yes</td></tr><tr><td>L3</td><td>2.678</td><td>22.72</td><td>0.000</td><td>Yes</td><td>Yes</td></tr><tr><td>M1</td><td>4.224</td><td>21.81</td><td>0.000</td><td>Yes</td><td>Yes</td></tr><tr><td>M2</td><td>6.732</td><td>14.93</td><td>0.000</td><td>Yes</td><td>Yes</td></tr><tr><td>M3</td><td>13.017</td><td>7.52</td><td>0.000</td><td>Yes</td><td>Yes</td></tr><tr><td>H1</td><td>-3.607</td><td>-0.62</td><td>0.727</td><td>No</td><td>No</td></tr><tr><td>H2</td><td>-15.175</td><td>-2.09</td><td>0.973</td><td>No</td><td>No</td></tr><tr><td>H3</td><td>6.038</td><td>0.87</td><td>0.200</td><td>No</td><td>No</td></tr></table>

Note: FMTO= Percentage improvement in total cost of the <sup>fl</sup>exible MTO as compared with the stochastic model.  
Null hypothesis, H :  
Alternative hypothesis, $\mathrm { H } _ { 1 } { : }$  
FMTO= 0 (equivalently, FMTO≤0).  
FMTON0.

Following this line of thought, it is interesting to consider whether the adaptive MTO is better than the <sup>fl</sup>exible MTO in reducing total system cost. The answer can be found in Fig. 3, which illustrates the difference in the percentage improvement in total system cost of the two systems. Positive results mean that the adaptive MTO performs better than the <sup>fl</sup>exible MTO. It is clear that the <sup>fl</sup>exible MTO outperforms adaptive MTO at low to medium capacity utilizations. As the capacity utilization is increasing from low to high (i.e. from L1 to H3), the trend is reverse. That is, <sup>fl</sup>exible MTO works well at low capacity utilization but adaptive MTO works well at high capacity utilization.

## 4.5. Other cost components

If more cost components, such as inventory cost, backorder cost, etc., are investigated, similar trends as discussed in Section 4.4 can be found. Hence, other graphs are omitted here for simplicity. Of course, different magnitudes as compared to Figs. 1 and 2 are expected. As a matter of fact, the majority of the saving is originated from the saving in backorder cost. Stochastic inventory policy, which is static in nature, is not able to react with the actual (or real-time) situation. Subject to such policy, even if suppliers have produced a certain amount of products, they are not allowed to ship the products to customers to cover any backorder. On the contrary, the <sup>fl</sup>exible MTO and adaptive MTO coordination mechanism can provide elasticity for both suppliers and customers regardless of the uncertainties they are facing. They can adjust the <sup>fi</sup>nal quantity to be supplied, and the production quantity to be produced respectively. Therefore, cost saving is signi<sup>fi</sup>cant when the supply chain suffers from uncertainties.

## 4.6. Fill rate

Fig. 4 summarizes the results of percentage improvement in demand <sup>fi</sup>ll rate. The <sup>fi</sup>ll rate is calculated by Eq. (21) and the percentage improvement is given by Eq. (22),

$$
\text { Fill   Rate } = \left(1 - \frac {\sum_ {t = 1} ^ {T} B _ {j p t}}{\sum_ {t = 1} ^ {T} d _ {j p t}}\right) \times 1 0 0\tag{21}
$$

$$
\text { Percentage   Improvement } = \frac {\text { Fill   Rate } _ {\mathrm{MTO}} - \text { Fill   Rate } _ {\mathrm{STO}}}{\text { Fill   Rate } _ {\mathrm{STO}}} \times 1 0 0\tag{22}
$$

where Fill ${ \sf R a t e } _ { \mathrm { M T O } }$ and Fill $\boldsymbol { \mathrm { R a t e } } _ { s \mathrm { t o } }$ are the <sup>fi</sup>ll rate from the <sup>fl</sup>exible or adaptive MTO system and stochastic model, respectively. Negative sign as in Eq. (20) is removed because the larger the <sup>fi</sup>ll rate, the better the performance of the system. In other words, positive values as shown in the graphs means improvement is obtained when compared with the stochastic model.

![](/api/attachments/MKFNDPRA/fulltext/images/9432a7b020ccfbbe9396857f8f0ee429393bc5919e90e9db7897deca97677d9e.jpg)  
(a) Low capacity utilizations

![](/api/attachments/MKFNDPRA/fulltext/images/ba0f5848ddd10a53204c086bcbbf8d7240bb5939f95cbf3e12ae2efbe28e88c9.jpg)  
(b) Medium Capacity utilizations

![](/api/attachments/MKFNDPRA/fulltext/images/ad892521cf8e0f03113fcb06ce1610997d326c9a6cd4e45d01434dea87472707.jpg)  
(c) High Capacity utilizations  
Fig. 3. Difference in percentage improvements in total system cost at different capacity utilizations—adaptive MTO against <sup>fl</sup>exible MTO.

In terms of <sup>fi</sup>ll rate, the trend between <sup>fl</sup>exible MTO and adaptive MTO at different capacity utilizations is similar. Therefore, results from one capacity utilization are discussed but the arguments apply to all capacity utilizations. Fig. 4(a) depicts the demand <sup>fi</sup>ll rate for individual products, while Fig. 4(b) records the aggregate demand <sup>fi</sup>ll rate by assuming all the products are of equal importance. In other words, this is the overall demand <sup>fi</sup>ll rate. From Fig. 4, the results are obviously unsatisfactory in the <sup>fl</sup>exible MTO strategy. There are many negative values (except two settings only with minor improvement) for different product types as re<sup>fl</sup>ected by Fig. 4(a), which mean <sup>fi</sup>ll rate is not as good as for the stochastic model. The reason for the poor performance in terms of <sup>fi</sup>ll rate is due to the fact that when suppliers make the production planning according to the upper bound of the quantity range, they are actually making too much product and part of the production capacity is just a waste of resource. This leads to poor performance of other products while a certain order has not been completed yet.

![](/api/attachments/MKFNDPRA/fulltext/images/1bae65bd93a780dd554bdb99d6beb34fe4c196a5ea0b960f916a41678fd3ab72.jpg)  
(a) Individuals products

![](/api/attachments/MKFNDPRA/fulltext/images/9f455dbe80292c3ff8c195224b80e9ecb9aa32b42c4f3a49c6e04507f85e9b96.jpg)  
(b) Aggregate fill rate  
Fig. 4. Percentage improvements in demand <sup>fi</sup>ll rate—<sup>fl</sup>exible MTO against stochastic model.

Individual <sup>fi</sup>ll rates of different products and the aggregate <sup>fi</sup>ll rates using the adaptive coordination mechanism are depicted in Fig. 5. Obviously, the adaptive MTO coordination mechanism could improve the <sup>fi</sup>ll rate as compared with the stochastic model.

From Figs. 2 and 3, we have already recognized that cost savings can be gained by adopting the two coordination mechanisms. Therefore, Fig. 5 together with Figs. 2 and 3 further verify that the adaptive MTO coordination mechanism can improve the cost and <sup>fi</sup>ll rate of the system simultaneously for most situations under the simulation study. This is something mathematical programming techniques cannot achieve.

## 4.7. Managerial implications

As reported from the simulation results, both the <sup>fl</sup>exible MTO and the adaptive MTO can improve the system performance in terms of costs, and the adaptive MTO can also improve the <sup>fi</sup>ll rate of the system. However, there is a trade-off in choosing between these different strategies as illustrated in Fig. 6. As shown in Fig. 6(a), <sup>fl</sup>exible MTO should be employed when the capacity utilization is low. On the other hand, adaptive MTO should be used when the capacity utilization is high. This implication also <sup>fi</sup>lls the gap in the literature in which unlimited supplier capacity is assumed. The importance of supplier capacity utilization cannot be ignored. Fig. 6(b) further illustrates which strategy should be employed under various situations in this study. It means that whenever the industry encounters low demand uncertainty, the strategy to be chosen is quite obviously, which in line with above discussion regardless of the degree of uncertainty of supply. On the other hand, manufacturers have more freedom in selecting which strategy when the demand uncertainty is high. Fig. 6(b) is not a generalization of different industries, but serves as a guideline whenever a decision has to be made between <sup>fl</sup>exibility and adaptability.

![](/api/attachments/MKFNDPRA/fulltext/images/b913746c618b4ea181048d3fefe6d0d12291b954b2c76b647193a55bb81e88fd.jpg)  
(a) Individuals products

![](/api/attachments/MKFNDPRA/fulltext/images/cea4101e46e49318c33a6bb09806bfbabb05411a406242cbfe2b320f2eb67863.jpg)  
(b) Aggregate fill rate  
Fig. 5. Percentage improvements in demand <sup>fi</sup>ll rate—adaptive MTO against stochastic model.

On top of this <sup>fi</sup>nding, it can be observed that percentage improvement in total system cost is more consistent for different settings under the adaptive MTO as shown in Fig. 2, in spite of the fact that the improvement is not as good as the <sup>fl</sup>exible MTO at low to medium capacity utilizations. The implication from these <sup>fi</sup>ndings is that the proposed adaptive coordination mechanism is more reliable and performance is better than the <sup>fl</sup>exible MTO with <sup>fl</sup>exibility alone subject to variations in capacity utilization. If capacity utilization is unclear, adaptive MTO should be employed.

In fact, these <sup>fi</sup>ndings support the result of a survey conducted by Fynes et al. [9]. They revealed that adaptability could reduce the cost of dynamic supply chains. However, their empirical results also indicated that adaptability has no effect on <sup>fl</sup>exibility. This is probably due to the fact that the targets of the survey come from the industry where those companies normally would not invest for over-capacity. That means they are con<sup>fi</sup>gured at low to medium capacity utilizations with reference to this simulation study. Therefore, adaptability has no effect on <sup>fl</sup>exibility, as shown in Fig. 3(a) and (b).

## 5. Conclusion

To remain competitive, organizations must be able to move fast and quickly adapt to change. Moreover, they must be able to recon<sup>fi</sup>gure their key business processes with changing market conditions. Enterprises must respond to new requirements quickly without interrupting the course of business. Such changes must be mapped to the business object level and related to existing enterprise models. As product life cycles are shortening, adoption of MTO production strategy is inevitable. However, a pure MTO strategy may not be dynamic enough to react to external stimuli, especially in more realistic settings like the multi-product environment in this study.

Simulation results indicate that both the said <sup>fl</sup>exibility approach (<sup>fl</sup>exibility alone) and the proposed adaptive mechanism (both (b) An overview of using which strategy under different situations

![](/api/attachments/MKFNDPRA/fulltext/images/8601df09f37bfcd2cf98fc2bf7ccebda5a72f22802867b83a6c7463601e41ed1.jpg)  
(a) Adaptive coordination against flexibility coordination at different capacity utilizations

<table><tr><td>Demand Uncertainty</td><td colspan="4">High</td><td colspan="4">Low</td></tr><tr><td>Supply Uncertainty</td><td colspan="2">High</td><td colspan="2">Low</td><td colspan="2">High</td><td colspan="2">Low</td></tr><tr><td>Capacity Utilization</td><td>High</td><td>Low</td><td>High</td><td>Low</td><td>High</td><td>Low</td><td>High</td><td>Low</td></tr><tr><td>Flexible Approach</td><td></td><td>*</td><td></td><td>*</td><td></td><td>**</td><td></td><td>**</td></tr><tr><td>Adaptable Approach</td><td>**</td><td>*</td><td>**</td><td>*</td><td>**</td><td></td><td>**</td><td></td></tr></table>

Remark:  
\*\* - Highly confident  
\* - Confident

Fig. 6. Trade-off in total cost improvement.

<sup>fl</sup>exibility and adaptability) can reduce the total system cost as compared with a stochastic model. Furthermore, the proposed adaptive mechanism can also improve the demand <sup>fi</sup>ll rate of the system, which is one of the weaknesses of traditional MTO production system. On top of adding such <sup>fl</sup>exibility and adaptability to the system, variations in suppliers' capacity utilization have been investigated as an independent variable so that its impacts on the proposed coordination mechanism could be visualized. Based on the simulation results, it is found that there is a trade-off for decision makers to choose between <sup>fl</sup>exibility alone or to adopt the proposed adaptive mechanism at different capacity utilizations.

To extend the discussion of this paper, it is worth using real data which can be obtained in real-life applications to verify the achieved simulation as a future work. Another possible future research is to study the impacts of information sharing on the systems. In this paper, the adaptive mechanism works without information sharing. With information sharing, the system may be expected to react with uncertainties better. However, information sharing is not costless. In this connection, future study should be more focused on the improvement against investment by employing information sharing. Finally, non-cooperative element can be added in the coordination mechanism. This could be implemented as another form of uncertainty.

## References

[1] A. Cakravastia, I.S. Toha, N. Nakamura, A two-stage model for the design of supply chain networks, International Journal of Production Economics 80 (3) (2002) 231–248.

[2] T. Calosso, M. Cantamessa, M. Gualano, Negotiation support for make-to-order operations in business-to-business electronic commerce, Robotics and Computer-Integrated Manufacturing 20 (5) (2004) 405–416.

[3] F.T.S. Chan, H.K. Chan, A new model for manufacturing supply chain networks: a multiagent approach, Proceedings of the Institution of Mechanical Engineers Part B: Journal of Engineering Manufacture 218 (4) (2004) 443–454.

[4] H.K. Chan, F.T.S. Chan, A simulation study with quantity <sup>fl</sup>exibility in a supply chain subjected to uncertainties, International Journal of Computer Integrated Manufacturing 19 (2) (2006) 148–160.

[5] H.K. Chan, F.T.S. Chan, Early order completion contract approach to minimise the impact of demand uncertainty on supply chains, IEEE Transactions on Industrial Informatics 2 (1) (2006) 48–58

[6] H.K. Chan, F.T.S. Chan, Effect of information sharing in supply chain with <sup>fl</sup>exibility, International Journal of Production Research 47 (1) (20o9) 213–232

[7] H.R. Choi, H.S. Kim, Y.J. Park, K.H. Kim, M.H. Joo, H.S. Sohn, A sales agent for part manufacturers: VMSA, Decision Support Systems 28 (4) (2000) 333–346.

[8] Y.C. Fan, C. Huang, Y. Wang, L. Zhang, Architecture and operational mechanisms of networked manufacturing integrated platform, International Journal of Production Research 43 (12) (2005) 2615–2629.

[9] B. Fynes, C. Voss, S. Búrca, The impact of supply chain relationship dynamics on manufacturing performance, International Journal of Operations and Production Management 25 (1) (2005) 6–19.

[10] S. Ghose, J.J. Liu, A. Bhatnagar, H. Kurata, Modeling the role of retail price formats, and retailer competition types on production schedule strategy, European Journa of Operational Research 164 (1) (2005) 173–184

[11] P.T. Helo, Dynamic modelling of surge effect and capacity limitation in supply chains, International Journal of Production Research 38 (17) (2000) 4521–4522

[12] Y.T. Herer, M. Tzur, E. Yücesan, Transshipments: an emerging inventory recourse to achieve supply chain legality, International Journal of Production Economics 80 (3) (2002) 201–212.

[13] H.B. Hwarng, C.S.P. Chong, N. Xie, T.F. Burgess, Modelling a complex supply chain: understanding the effect of simpli<sup>fi</sup>ed assumptions, International Journal of Production Research 43 (13) (2005) 2829–2872.

[14] A. Janiak, M.Y. Kovalyov, M. Marek, Soft due window assignment and scheduling on parallel machines, IEEE Transactions on Systems, Man and Cybernetics-Part A: Systems and Humans 37 (5) (2007) 614–620.

[15] R. Kolisch, Integration of assembly and fabrication for make-to-order production, International Journal of Production Economics 68 (3) (2000) 287–306.

[16] R.Y.K. Lau, Y. Li, D. Song, R.C.W. Kwok, Knowledge discovery for adaptive negotiation agents in e-marketplaces, Decision Support Systems 45 (2) (2008) 310–323.

[17] A.M. Law, W.D. Kelton, Simulation Modeling and Analysis, McGraw-Hill, USA, 1991.

[18] J.-H. Lee, C.-O. Kim, Multi-agent systems applications in manufacturing systems and supply chain management: a review paper, International Journal of Production Research 46 (1) (2009) 233–265.

[19] F.-R. Lin, H.-C. Kuo, S.-M. Lin, The enhancement of solving the distributed constraint satisfaction problem for cooperative supply chains using multi-agent systems, Decision Support Systems 45 (4) (2008) 795–801.

[20] P.B. Luh, M. Ni, H. Chen, L.S. Thakur, Price-based approach for activity coordination in a supply network, IEEE Transactions on Robotics and Automation 19 (2) (2003) 335–346.

[21] J. Ma, L.K. Nozick, J.D. Tew, L.T. Truss, T. Costy, Modelling the effect of custom and stock orders on supply-chain performance, Production Planning and Control 15 (3) (2004) 282-291

[22] M. Moses, S. Seshadri, Policy mechanisms for supply chain coordination, IIE Transactions 32 (3) (2000) 245-262

[23] S. Rajagopalan, Make to order or make to stock: model and application, Management Science 48 (2)(2002) 241–256

[24] F. Ren, M. Zhang, K.M. Sim, Adaptive conceding strategies for automated trading agents in dynamic, open markets, Decision Support Systems 46 (3) (2009) 704–716.

[25] M.J. Sobel, Fill rates of single-stage and multi-stage supply systems, Manufacturing & Service Operations Management 6 (1) (2004) 41–52.

[26] N.R. Srinivasa Raghavan, N. Viswanadham, Generalized queuing network analysis of integrated supply chains, International Journal of Production Research 39 (2) (2001) 205-224

[27] T.J. Strader, F.R. Lin, M.J. Shaw, Information infrastructure for electronic virtual organization management, Decision Support Systems 23 (1) (1998) 75–94.

[28] S. Viswanathan, Periodic review (s, S) policies for joint replenishment inventory systems, Management Science 43 (10) (1997) 1447–1454.

[29] J. Wang, K. Gwebu, M. Shanker, M.D. Troutt, An application of agent-based simulation to knowledge sharing, Decision Support Systems 46 (2) (2009) 532–541.

[30] Q. Wang, D. Tsao, Supply contract with bidirectional options: the buyer's perspective, International Journal of Production Economics 101 (1) (2006) 30–52.

[31] D.Z. Zhang, A. Anosike, M.K. Lee, Dynamically integrated manufacturing systems (DIMS)—a multiagent approach, IEEE Transactions on Systems, Man and Cybernetics Part A: Systems and Humans 37 (5) (2007) 824–850.

![](/api/attachments/MKFNDPRA/fulltext/images/f4f91ac940ebaffef9f40466deed789f322f7e8564ff4e4fbd2c63cd051b77e2.jpg)

Hing Kai Chan received his BEng degree in Electrical and Electronic Engineering, MSc degree in Industrial Engineering and Industrial Management, PhD degree, all from the University of Hong Kong. He also earned a bachelor degree in Economics and Management from London School of Economics and Political Science, He is now a lecturer in the Norwich Business School, University of East Anglia, UK. Prior to joining the school in 2007, he was a project leader (carrying the title of research associate) of a government funded research project at Hong Kong Polytechnic University. His current research interests include industrial informatics, supply chain modeling and simulation, advanced industrial or manufacturing systems, and applications of soft computing on intelligent industrial systems and supply chains. He is also keen on research topics related to manufacturing or operations strategy like scheduling of <sup>fl</sup>exible manufacturing systems, which are his early research interests.

![](/api/attachments/MKFNDPRA/fulltext/images/d798c211ddc976922abb8c6a4b041a0aa4be3bf7d9f77e671cadfcf9adae4bfa.jpg)

Felix Chan received his BSc in Mechanical Engineering with First Class Honour at Brighton Polytechnic (now University). He obtained his MSc in Advanced Applied Mechanics and PhD at Imperial College of Science and Technology, University of London. He was a research fellow for 2 years in the Department of Design, Manufacture and Engineering Management, University of Strathclyde, then a senior lecturer at the School of Manufacturing and Mechanical Engineering, University of South Australia. Prior to joining the Department of Industrial and Systems Engineering of the Hong Kong Polytechnic University in 2009, Dr. Chan was an Associate Professor at the Department of Industrial and Manufacturing Systems Engineering, the University of Hong

Kong. His research areas cover modeling and simulation in advanced manufacturing systems and supply chain networks, supply chain performance measurement systems, intelligent distribution methodology with multicriterion decision-making approach for logistics, and supply chain management
