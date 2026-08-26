---
otero_id: 16102
otero_key: "AFXNQRAJ"
title: "Policies for a single-vendor multi-buyer system with finite production rate"
authors: "Beatriz Abdul-Jalbar; José M. Gutiérrez; Joaquín Sicilia"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.05.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Policies for a single-vendor multi-buyer system with <sup>fi</sup>nite production rate

Beatriz Abdul-Jalbar ⁎, José M. Gutiérrez, Joaquín Sicilia

Dpto. de Estadística, Investigación Operativa y Computación, Universidad de La Laguna, Tenerife, Islas Canarias, Spain

## a r t i c l e i n f o

Article history: Received 26 May 2006 Received in revised form 5 May 2008 Accepted 25 May 2008 Available online 24 July 2008

Keywords: Inventory control Multi-echelon inventory systems Integer-ratio policies

MSC: 90B05 90B30

## a b s t r a c t

We deal with a multi-echelon inventory system in which one vendor supplies an item to multiple buyers. The vendor produces the item at a <sup>fi</sup>nite rate and customer demand occurs at each buyer at a constant rate. There is a holding cost per unit stored per unit time at the vendor and at each buyer. Each time a production is carried out the vendor incurs a setup cost. Moreover, placing an order at a buyer entails a <sup>fi</sup>xed ordering cost. Shortages are not allowed. The goal is to determine the order quantities at the buyers and the production and shipment schedule at the vendor in order to minimize the average total cost per unit time. We formulate the problem in terms of integer-ratio policies and we develop a heuristic procedure. We also show how the problem should be addressed in case of independence among the vendor and the buyers. Both solution procedures are illustrated with a numerical example. Finally, we present the results of a numerical study which illustrates the performance of the heuristic for computing integer-ratio policies. Additionally, we compare the integer-ratio policies with the decentralized policies, and a sensitivity analysis of parameters is also reported.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

An interesting decision problem arises whenever a product needs to be supplied by a vendor to multiple buyers. This inventory/distribution system is commonly referred to as the single-vendor multi-buyer problem and it has been analyzed extensively in the literature considering in<sup>fi</sup>nite production rate. See for example [20,13,26,27,19,1,2,29,30] and [22].

However, when the production rate is <sup>fi</sup>nite most contributions simply consider a single buyer. For instance, Banerjee [5] analyzed the integrated vendor–buyer model where the vendor produces the items at a <sup>fi</sup>nite rate. He examined a lotfor-lot model in which the vendor manufactures each buyer shipment as a separate batch.

Goyal [8] further generalized Banerjee's model by relaxing the assumption of lot-for-lot policy for the vendor. He showed that manufacturing a batch which is made up of an integral number of equal shipments generally produced a lower cost solution. Goyal's model was derived based on the assumption that the vendor can supply to the buyer only after completing the entire lot size. A review of contributions related to vendor– buyer coordination models is given in [11].

Lu [18] relaxed the assumption of Goyal [8] about completing a batch before starting shipments and gave an optimal solution to the single-vendor single-buyer problem assuming equal shipments. This strategy is an improvement over the policies earlier proposed by [5] and [8].

Goyal [9] considered that the shipments could be made before completion of the whole lot. He also incorporated an alternative policy in which the quantity to be delivered from the vendor is not identical at every replenishment. Instead, at each delivery all the available inventory is supplied to the buyer. This policy was based on a preceding argument proposed by [7] for solving a single-vendor single-buyer system with in<sup>fi</sup>nite production rate at the vendor. This new policy involves successive shipment sizes within a batch which are increased by a factor equal to the ratio between the vendor's production rate and the demand rate on the buyer. Goyal [9] used the numerical example given in [18] to show that this form of policy can result in joint total costs lower than those associated with the equal shipment size policy.

Viswanathan [21] identi<sup>fi</sup>ed problem parameters under which the equal shipment size policy in [18] and the increasing shipment policy in [9] are optimal. He found that policy in [9] has lower cost only if the holding cost at the buyer is not much larger than the holding cost at the vendor. This is because as the holding cost at the buyer increases, it is better to hold inventory at the vendor than at the buyer. In addition, [21] also shows that the production rate at the vendor has a signi<sup>fi</sup>cant in<sup>fl</sup>uence on which policy is better. In particular, if the production rate decreases relative to the demand rate, the policy provided by [9] becomes more attractive. This is due to the fact that as the production rate decreases, the vendor would <sup>fi</sup>nd more dif-<sup>fi</sup>cult to cope up with the demand, and therefore, it makes more sense to deliver whatever inventory is available at each replenishment.

Hill [14] showed that neither the equal shipment size policy in [18] nor the increasing shipment size policy in [9] are always optimal. He took Goyal's idea a stage further by considering successive shipment sizes which are increased by a general <sup>fi</sup>xed factor. This factor ranges from 1 to an upper bound which coincides with the quotient between the production rate and the demand rate. Therefore, both the equal shipment size policy and Goyal's policy represent special cases of this new policy. The equal shipment size policy is obtained when the factor is equal to 1. Additionally, when the factor coincides with the quotient between the production rate and the demand rate the policy provided by [9] is achieved. It is not surprising that this new class of policies obtained by [14] provides a total cost lower than those obtained by [18] and [9]. However, these policies could not be optimal policies for the single-vendor and single-buyer problem with <sup>fi</sup>nite production rate at the vendor. The form of the global optimal policies for this problem was derived in a later work by Hill [16]. He showed that in the optimal policy the sizes of the <sup>fi</sup>rst shipments increase by a <sup>fi</sup>xed factor and the last shipments are of equal size.

Although the problem has already been optimality solved by [16], we can <sup>fi</sup>nd new papers dealing with the singlevendor and single-buyer problem. For example, [10] suggested an improvement over the policy of [14]. Moreover, [12] introduced a policy in which the batch quantity is received by the buyer in different shipments. Speci<sup>fi</sup>cally, the size of the <sup>fi</sup>rst shipment is the smallest, and the next deliveries are equal to the size of the <sup>fi</sup>rst shipment multiplied by the ratio between the production rate and the demand rate.

It is worth noting that in practice the vendor usually supplies to multiple buyers. Nevertheless, we <sup>fi</sup>nd few references in the literature considering the multiple buyers case with <sup>fi</sup>nite production rate at the vendor. Lu [18] studied the model assuming that each buyer orders a different item from the vendor. Moreover, [18] considered that the objective consists of minimizing the total cost at the vendor subject to the maximum cost that the buyers may be prepared to incur. Recently, in [28] it is proposed a heuristic for the single-vendor multi-buyer problem considering the same assumptions that those in [18].

Extensions to this model are introduced by [17,25] and $[ 3 ] .$ In particular, [17] and [25] studies a three-echelon system with multiple <sup>fi</sup>rms at each echelon which can supply to two or more customers. In addition, [17] assumes that the whole lot has to be produced before delivering the batch. However, [25] considers that the replenishment interval at the retailer is smaller than the replenishment interval at its distributor, which in turn, is smaller than the replenishment interval at the producer.

In [3] the single-vendor two-buyer problem assuming that both buyers order the same item from the vendor is addressed. They propose a solution method which combines the Karush– Kuhn–Tucker (KKT) conditions with a branch and bound scheme.

In this paper we deal with the model proposed by [3] but considering multiple buyers. Unlike [17] our model considers that the shipments can be made before the whole lot is produced. Moreover, in contrast to [25], we allow the replenishment interval at any buyer to be greater than the replenishment interval at the vendor. Under these assumptions, we derive the formulation of the single-vendor multi-buyer problem in terms of the integer-ratio policies. Besides, we develop a heuristic procedure which computes effective integer-ratio policies.

In addition to the analysis of the centralized policies, we also show how the problem should be handled if the vendor and the buyers were not treated jointly but in isolation. Finally, we carry out a computational experiment in order to illustrate the performance of both procedures.

The remainderof this paper is organized as follows. Section 2 introduces the notation and assumptions required to state the problem. In Section 3 we formulate the problem in terms of integer-ratio policies and in Section 4 we develop a heuristic procedure. We discuss in Section 5 how to solve the problem if the vendor and the buyers are treated separately. In Section 6 we introduce a numerical example in order to illustrate both solution procedures. In Section $^ { 7 , }$ computational results and sensitivity analysis of parameters are reported. Finally, we conclude with some remarks in Section 8.

## 2. Notation and problem statement

We study the single-vendor multi-buyer system where the vendor produces a single item at a <sup>fi</sup>nite rate which is shipped to the buyers. It is assumed that customer demand occurs at each buyer at a constant rate. There is a holding cost per unit stored per unit time at the vendor and at each buyer. The vendor incurs a setup cost associated with each shipment. Furthermore, each time that a buyer places an order it incurs a <sup>fi</sup>xed ordering cost. The input data associated with the buyers are $d _ { j }$ , $k _ { j }$ and $h _ { j }$ which represent the constant and continuous demand rate, the <sup>fi</sup>xed order cost and the inventory holding cost per unit time at buyer $j , j { = } 1 , { \ldots } , N ,$ respectively. The <sup>fi</sup>xed production setup cost and the inventory holding cost per unit time at the vendor are denoted by $k _ { 0 }$ and $h _ { 0 } ,$ respectively. Additionally, P represents the continuous production rate for the vendor.

The decision variables are the replenishment intervals at the buyers, $\displaystyle t _ { j } , j { = } 1 , . . . , N ,$ , and the time interval between two consecutive setups at the vendor, $t _ { \nu \cdot }$ . The total costs per unit time incurred by buyer $j , j { = } 1 , . . . , N$ , the vendor and the system are $C _ { j } , C _ { \vee }$ and $C _ { \mathrm { T } } ,$ respectively.

In the formulation of the problem we use the following notation. Let $\mathrm { I V } ^ { t }$ <sub>and IV be the inventory at instant</sub>¯ <sub>t at the</sub> vendor and the average inventory at the vendor, respectively. <sub>Similarly, we denote by IB</sub>t <sub>and IB</sub>¯ <sub>the inventory at buyer j at</sub> instant t and the average inventory at buyer j, respectively. Finally, IT<sup>t</sup> represents the total inventory in the system at instant <sub>t and IT the average total inventory in the system.</sub>¯

The stock value normally increases as a product moves down the distribution chain, and therefore, the associated holding costs also increase. Taking this into account, we assume that $h _ { j } \geq h _ { 0 } , ~ j = 1 , \ldots ,$ N. As a consequence of these inequalities the stock should be retained by the vendor until a buyer needs another shipment.

The goal consists of determining the order quantities at the buyers and the production and shipment schedule at the vendor so that the average total cost per unit time is minimized.

## 3. Model formulation

Previous works mostly focused on the single-vendor multibuyer problem assuming in<sup>fi</sup>nite production rate. Under this assumption, work [19] is the most relevant paper. In [25] it is shown that optimal policies for this problem can be very complex and he introduced the class of integer-ratio policies to facilitate both computation and implementation. Regarding the model assuming <sup>fi</sup>nite production rate, most contributions are con<sup>fi</sup>ned to consider a single buyer. However, in practice, the vendor usually supplies to multiple buyers. Accordingly, the main goal in this paper is to extend Roundy's model [19] to the case of <sup>fi</sup>nite production rate.

Roundy stated that a policy is integer-ratio policy if the replenishment interval at the vendor, $t _ { \nu }$ , and the replenishment interval at buyer $i , t _ { i } ,$ satisfy the integer-ratio constraint, i.e., either $\frac { t _ { i } } { t _ { v } } \ 0 \Gamma \ \frac { t _ { v } } { t _ { i } }$ <sup>v</sup> should be a positive integer. In particular, [19] focuses on a subclass into the integer-ratio policies called powers-of-two policies, where the replenishment intervals are powers-of-two multiples of a base planning period. He proved that the cost of an optimal powers-of-two policy is at most 2% above the cost of an optimal policy. Taking into account the good performance of such policies for Roundy's model, many authors have studied their behavior in other multi-echelon systems.

In this section we formulate the single-vendor multibuyer problem with <sup>fi</sup>nite production rate at the vendor in terms of integer-ratio policies. In particular, we con<sup>fi</sup>ne ourselves to study those integer-ratio policies where the quotients $\begin{array} { r } { \frac { t _ { j } } { t _ { j - 1 } } , j = { \hat { 2 } } , . . . , N , } \end{array}$ are positive integers. These con-<sup>¼</sup>straints ensure that $t _ { 1 } \le t _ { 2 } \le . . . \le t _ { N }$ and that each time a buyer with replenishment interval $t _ { j }$ orders, the remaining buyers with replenishment interval t ≤t also order. Consequently, there will be points in time where the vendor should supply to all the buyers simultaneously, and others where it only supplies to some of the buyers. Therefore, in the latter case, the vendor should start the production later than when the vendor supplies to all the buyers. Hence, we let the time interval between two consecutive setups to be non-constant. Remark that this class of policies is a generalized case of the powers-of-two policies proposed by [19].

![](/api/attachments/AFXNQRAJ/fulltext/images/9c2d84713c019f505374ba14660db2d475f5f676bbb708913a0c966d5696c08e.jpg)

![](/api/attachments/AFXNQRAJ/fulltext/images/812d1e8960604984854a83001b4a478eda0ea040657fd893d6fefd7e960117db.jpg)

![](/api/attachments/AFXNQRAJ/fulltext/images/373f0e943a005d300c10a589221710bb02d5e203dd3a0847fa39cc8f2488bd2f.jpg)

![](/api/attachments/AFXNQRAJ/fulltext/images/3ba18de8188c1f617ae40b887793a293fc0d670131284c49b3b00207bd60f45a.jpg)  
Fig. 1. Inventory <sup>fl</sup>uctuations at the vendor and at the buyers considering tha $\mathrm { ~ : ~ } t _ { \nu } 1$ is constant. Buyer 1 and buyer 2 belongs to set $E \cup L ,$ and buyer 3 and buyer 4 are in set G. The dotted line represents the production rate.

Let us consider the example illustrated in Figs. 1 and 2 consisting of one vendor and four buyers. The <sup>fl</sup>uctuations of inventories at the buyers, IB , i=1, 2, 3, 4, and at the vendor, IV, when we force the time interval between two consecutive setups to be constant, are depicted in Fig. 1. In this case, the vendor anticipates the production that will be withdrawn later, and hence it unnecessarily holds inventory. However, as it can be seen in Fig. 2, if we allow the time interval between two consecutive setups to be non-constant the holding cost at the vendor can be reduced. In this case, it is important to note that if we only consider buyer 1 and buyer 2, and we assume that the vendor <sup>fi</sup>rst produces the units which will be sent to such buyers, then the time interval between two consecutive setups is constant. In what follows we will denote this time interval by $t _ { 0 } .$ That is, in general, $t _ { 0 }$ represents the time interval between two consecutive setups when it is only considered the buyers with replenishment interval $t _ { i } \le t _ { v }$ Moreover, if we take into account all the buyers, including those with replenishment interval $t _ { i } > t _ { v _ { i } }$ the time interval between two consecutive setups can be easily obtained from $t _ { 0 } .$

![](/api/attachments/AFXNQRAJ/fulltext/images/d9d3f8757ff252daccd1fdf5655c5f6ee0bb580378bb698595a4ee79df42ac2d.jpg)

![](/api/attachments/AFXNQRAJ/fulltext/images/1502b20dedd8da101a6a9d60e9826843f037cd6eb2d8e0311f4a4566f90c9c5e.jpg)

![](/api/attachments/AFXNQRAJ/fulltext/images/4c59d58d063184f68b2f3400d110202cf421869d91c63c330983e56f6f1c0352.jpg)

![](/api/attachments/AFXNQRAJ/fulltext/images/55c871b2a784cb0d14b08b4fdf95c20b26b89b490b1ccee4114b4c721eb3bddd.jpg)  
Fig. 2. Inventory <sup>fl</sup>uctuations at the vendor and at the buyers considering that t is non-constant. Buyer 1 and buyer 2 belongs to set E∪L, and buyer 3 and buyer 4 are in set G. The dotted line represents the production rate. At instants A, B, C and D the vendor begins the production of the items which will be shipped to buyer 1 and buver 2

The key idea to formulate the problem consists of classifying the buyers into three sets, denoted by $G ,$ L and $E _ { * }$ In [19], those buyers with $t _ { i } > t _ { \nu }$ are allocated to set G. Set E contains those buyers with $t _ { i } = t _ { v } ,$ and <sup>fi</sup>nally, those buyers with $t _ { i } < t _ { v }$ belong to set L. As we have commented before, when the production rate is <sup>fi</sup>nite, we allow the time interval between two consecutive setups to be non-constant. Hence, sets $G ,$ L and E cannot be de<sup>fi</sup>ned as in [19]. However, we can use $t _ { 0 }$ to de<sup>fi</sup>ne sets $G ,$ , L and E similarly to those in [19]. In particular, we set $G = \{ i | t _ { i } > t _ { 0 } \} , E = \{ i | t _ { i } = t _ { 0 } \}$ and $L = \{ i | t _ { i } < t _ { 0 } \}$ }.

In the next subsection we focus on computing the average inventory at the vendor and at the buyers. For the singlevendor single-buyer problem, both inventories are easily computed. However, computing the average inventory at the vendor get complicated for the multi-buyer case.

## 3.1. Stock holding cost

We <sup>fi</sup>rst state the production-inventory patterns. The cycle length is $T { = } \operatorname* { m a x } _ { j { = } 1 , \ldots , \ N } \ \left\{ t _ { j } \right\}$ , and it starts with the <sup>fi</sup>rst production setup.

For the previous example, Fig. 3 illustrates the inventory pattern within a typical production cycle for the vendor, for the buyers and for the total system. Remark that buyer 1 and buyer 2 are in set E∪L and buyer 3 and buyer 4 are in set G. Since the buyers follow the classical EOQ pattern, the holding cost per unit time at the buyers is directly obtained. On the other hand, the average inventory at the vendor cannot be computed so easily. For the single-vendor single-buyer problem, [16] shows that the average total inventory is directly derived. Thus, he computed the average inventory at the vendor as the average total inventory less the average inventory at the buyer. Unfortunately deriving the average total inventory with N buyers is much more complex. We illustrate in Fig. 3 the pattern of total inventory (plotted as a dotted line), which differs from the model with a single buyer. It is important to note that the differences between both patterns are caused by buyers in set G.

![](/api/attachments/AFXNQRAJ/fulltext/images/295887ce3a8b4be5807a6d1689b375b41e88d62c76b68458e7008103950e437c.jpg)

![](/api/attachments/AFXNQRAJ/fulltext/images/7a8314efa7908381d4b894b56f61f83f363c264b19c3bca896b981e45d989d01.jpg)

![](/api/attachments/AFXNQRAJ/fulltext/images/c2ecc619ed60bb39c1a532988888ef1401676e5e2dd2f1449a92027edb68ede6.jpg)

![](/api/attachments/AFXNQRAJ/fulltext/images/aea485e3dc795f0d501eedc68bc027267883e78f3a79dcf0c87b5aff69229e5f.jpg)  
Fig. 3. Inventory <sup>fl</sup>uctuations at the vendor and at the buyers when t is non-constant, which are used to compute the inventory <sup>fl</sup>uctuations for the total system, IT, given by the dotted line.

Observe that the vendor only holds inventory for the buyers in set G during the production time, but not after the shipment. Accordingly, we distinguish two types of inventory at the vendor: the inventory which will be used to satisfy the demand of buyers in set $E \cup L , \boldsymbol { \mathrm { I V } } _ { E \cup L }$ , and the inventory which will be shipped to buyer $j , j { \in } G , \operatorname { I V } _ { j }$ . Thus, the total inventory at the vendor at instant t is given by $\begin{array} { r } { \mathrm { I V } ^ { t } = \mathrm { I V } _ { E \cup L } ^ { t } + \sum _ { i \in G } \mathrm { I V } _ { j } ^ { t } } \end{array}$ . In addition, we denote by $\Pi _ { E \cup L } ^ { t }$ and $\overline { { \Pi _ { E \cup L } } }$ <sup>[ 2</sup>the total inventory in <sup>[ [</sup>the system for buyers in set E∪L at instant t, and the average total inventory for buyers in set E∪L during a cycle, respectively. Similarly, $\overline { { \mathsf { I V } _ { E \cup L } } }$ and $\overline { { \operatorname { I V } _ { j } } } , j \in G ,$ ; represent the average inventory at the vendor during a cycle for buyers in set E∪L and for buyer $j , j \in G ,$ respectively.

Then, the average inventory at the vendor, IV, can be computed as $\begin{array} { r } { \overline { { \mathbb { V } } } = \overline { { \mathbb { V } _ { E \cup L } } } + \sum _ { i \in G } \overline { { \mathbb { V } _ { j } } } } \end{array}$ : Moreover, in Fig. 4, we plot $\begin{array} { r } { \begin{array} { r } { \mathrm { I V } _ { E \cup L } ^ { t } + \sum _ { j \in E \cup L } \mathrm { I B } _ { j } ^ { t } , t \in [ 0 , T ) , } \end{array} } \end{array}$ <sup>2</sup>which yields a pattern equal to that <sup>[ 2 [</sup>obtained for the one buyer case. Thus, $\overline { { \mathrm { I V } _ { E \cup L } } } = \overline { { \Pi _ { E \cup L } } } - \sum _ { i \in E \cup L } \overline { { I B _ { j } } }$

<sup>[</sup>We can use Fig. 4 to illustrate how $\overline { { \Pi _ { E \cup L } } }$ <sup>[ 2 [</sup>can be determined. When production starts $\Pi _ { E \cup L } ^ { 0 }$ <sup>[</sup>is minimum and the <sup>[</sup>inventory at the vendor is equal to zero. Moreover, the inventories at buyers in set E ∪ L are just enough to satisfy their demands until the next deliveries arrive. The quantity ordered by buyer j is $d _ { j } t _ { j }$ and hence the time required to produce the quantities ordered by all buyers in set E ∪ L is $\Sigma _ { i \in E \cup L } d _ { i } t _ { i } / P .$ Therefore, when the production starts, inventory levels $\begin{array} { r } { \begin{array} { r l } { \mathrm { I B } _ { i } ^ { 0 } , \ j \in E \cup L } \end{array} } \end{array}$ and $ { \Pi } _ { E \cup L } ^ { 0 }$ should be $d _ { j } \ \Sigma _ { i \in E \cup L } \ d _ { i } t _ { i } / P$ and $\begin{array} { r } { \Sigma _ { j \in E \cup L } \bar { d _ { j } } \ \bar { \Sigma } _ { i \in E \cup L } d _ { i } t _ { i } / P , } \end{array}$ <sup>[</sup>respectively. Then, from the latter value $ { \Pi } _ { E \cup L } ^ { 0 } ,  { \Pi } _ { E \cup 1 } ^ { t }$ keeps on increasing at a rate of $P - \Sigma _ { j \in E \cup L } d _ { j }$ <sup>[ [</sup>during the time needed to manufacture $t _ { 0 } \Sigma _ { j \in E \cup L } d _ { j }$ units. This value represents the sum of the quantities demanded by buyers in set E∪L during a cycle $t _ { 0 } .$ We can also see in Fig. 4 that $\Pi _ { E \cup L }$ reaches its maximum at the instant $t ^ { \prime } { = } t _ { 0 } ~ \Sigma _ { j \in E \cup L } ~ d _ { j } / P$ which coincides with the moment when the production <sup>fi</sup>nishes. Thus, the maximum value for $\Pi _ { E \cup L }$ is

$$
\frac {\sum_ {j \in E \cup L} d _ {j} \sum_ {i \in E \cup L} d _ {i} t _ {i}}{P} + \left(1 - \frac {\sum_ {j \in E \cup L} d _ {j}}{P}\right) t _ {0} \sum_ {j \in E \cup L} d _ {j}
$$

Accordingly, $\overline { { \Pi _ { E \cup L } } }$ can be written as follows

$$
\begin{array}{l} \overline {{\mathrm{IT} _ {E \cup L}}} = \frac {1}{t _ {0}} \left[ \frac {\sum_ {j \in E \cup L} d _ {j} \sum_ {i \in E \cup L} d _ {i} t _ {i}}{P} t _ {0} + t _ {0} \left(1 - \frac {\sum_ {j \in E \cup L} d _ {j}}{P}\right) \frac {t _ {0} \sum_ {j \in E \cup L} d _ {j}}{2} \right] \\ = \frac {\sum_ {j \in E \cup L} d _ {j} \sum_ {i \in E \cup L} d _ {i} t _ {i}}{P} + \left(1 - \frac {\sum_ {j \in E \cup L} d _ {j}}{P}\right) \frac {t _ {0} \sum_ {j \in E \cup L} d _ {j}}{2} \end{array}
$$

Observe that this expression is very similar to the average cost in the classical EPQ model. It only differs from the typical EPQ expression in the <sup>fi</sup>rst term which is the value of $\Pi _ { E \cup L }$ when production starts, that is, $ { \mathrm { I T } } _ { E \cup . } ^ { 0 }$ <sub>L</sub>.

Once $\overline { { \Pi _ { E \cup L } } }$ <sup>[</sup>is obtained, we can compute $\overline { { \mathrm { I V } _ { E \cup L } } }$ from the following expression

$$
\begin{array}{l} \overline {{\mathrm{IV} _ {E \cup L}}} = \overline {{\mathrm{IT} _ {E \cup L}}} - \sum_ {j \in E \cup L} \overline {{I B _ {j}}} = \frac {\sum_ {j \in E \cup L} d _ {j} \sum_ {i \in E \cup L} d _ {i} t _ {i}}{P} \\ + \left(1 - \frac {\sum_ {j \in E \cup L} d _ {j}}{P}\right) \frac {t _ {0} \sum_ {j \in E \cup L} d _ {j}}{2} - \sum_ {j \in E \cup L} \frac {d _ {j} t _ {j}}{2} \end{array}
$$

Now we focus on determining $\overline { { \mathsf { I V } _ { j } } }$ , for each buye $\cdot j \in G .$ As it can be seen in Fig. 5, for buyers in set G the vendor only holds inventory during the production time, but not after the shipment. Since a buyer $j { \in } G$ always orders $d _ { j } t _ { j }$ units every $t _ { j } ,$ the vendor requires $d _ { j } t _ { j } / P$ units of time to produce them. Moreover, recall that we are assuming that $t _ { j } / t _ { j - 1 }$ is a positive integer fo $\cdot j = 2 , . . . , N .$ Hence, it holds that $t _ { 1 } \le t _ { 2 } \le . . . \le t _ { N }$ and that each time a buyer with replenishment interval $t _ { j }$ orders, the remaining buyers with replenishment interval $t _ { i } \leq t _ { j }$ also order. Therefore, when a buyer $j { \in } G$ places an order all buyers ibj also order. In this case, Fig. 5 shows that the units produced at the vendor for buyer $j { \in } G$ are held during the time that the vendor needs to produce the units for all buyers $i , i { < } j ,$ that is, during $\textstyle \sum _ { i = 1 } ^ { j - 1 } d _ { i } t _ { i } / \bar { P }$ units of time. Taking this concern into account, the <sup>¼</sup>average inventory at the vendor which will be shipped to buyer $j { \in } G$ can be computed as follows

![](/api/attachments/AFXNQRAJ/fulltext/images/7a597743dc0718fc49eaa995b5082e3e37bee3b2f74e653cb2839dc6f50e4122.jpg)  
Fig. 4. Inventory at buyer 1 and buyer 2, and inventory located at the vendor which will be used to satisfy the demand at buyer 1 and buyer 2, namely, $\mathrm { I V } _ { E \cup L }$

![](/api/attachments/AFXNQRAJ/fulltext/images/bdf4c8d92e0f8480d4a5623df10adca4064b4fe27a37d60eeaf867d2d77464be.jpg)  
Fig. 5. Inventory at buyer 3 and buyer 4, and inventory located at the vendor which will be shipped to buyer $3 , \mathrm { { I V } } _ { 3 } ,$ and to buyer 4, $\mathrm { { I V } } _ { 4 } .$

$$
\overline {{\mathrm{IV} _ {j}}} = \frac {1}{t _ {j}} \left[ \frac {d _ {j} t _ {j}}{P} \frac {d _ {j} t _ {j}}{2} + \frac {d _ {j} t _ {j} \sum_ {i = 1} ^ {j - 1} d _ {i} t _ {i}}{P} \right] = \frac {d _ {j} t _ {j} d _ {j}}{2 P} + \frac {d _ {j} \sum_ {i = 1} ^ {j - 1} d _ {i} t _ {i}}{P}
$$

Thus, the average total inventory at the vendor is

$$
\begin{array}{l} \overline {{\mathrm{IV}}} = \overline {{\mathrm{IV} _ {E \cup L}}} + \sum_ {j \in G} \overline {{\mathrm{IV} _ {j}}} = \frac {\sum_ {j \in E \cup L} d _ {j} \sum_ {i \in E \cup L} d _ {i} t _ {i}}{P} + \left(1 - \frac {\sum_ {j \in E \cup L} d _ {j}}{P}\right) \frac {t _ {0} \sum_ {j \in E \cup L} d _ {j}}{2} \\ - \frac {\sum_ {j \in E \cup L} d _ {j} t _ {j}}{2} + \sum_ {j \in G} \left(\frac {d _ {j} t _ {j} d _ {j}}{2 P} + \frac {d _ {j} \sum_ {i = 1} ^ {j - 1} d _ {i} t _ {i}}{P}\right) = \frac {\sum_ {j \in E \cup L} d _ {j} \sum_ {i \in E \cup L} d _ {i} t _ {i}}{P} + \sum_ {j \in G} \frac {d _ {j} t _ {j} d _ {j}}{2 P} \\ + \sum_ {j \in G} \frac {d _ {j} \sum_ {i \in E \cup L} d _ {i} t _ {i}}{P} + \sum_ {j \in G} \frac {d _ {j} \sum_ {i \in G \cap \{i / i <   j \}} d _ {i} t _ {i}}{P} + \left(1 - \frac {\sum_ {j \in E \cup L} d _ {j}}{P}\right) \frac {t _ {0} \sum_ {j \in E \cup L} d _ {j}}{2} - \frac {\sum_ {j \in E \cup L} d _ {j} t _ {j}}{2} \end{array}
$$

which can be rewritten as follows

$$
\begin{array}{l} \overline {{\mathrm{IV}}} = \sum_ {i \in E \cup L} \frac {d _ {i} t _ {i}}{P} \sum_ {j = 1} ^ {N} d _ {j} + \sum_ {j \in G} \frac {d _ {j} t _ {j}}{P} \left(\frac {d _ {j}}{2} + \sum_ {i = j + 1} ^ {N} d _ {i}\right) \\ \quad + \left(1 - \frac {\sum_ {j \in E \cup L} d _ {j}}{P}\right) \frac {t _ {0} \sum_ {j \in E \cup L} d _ {j}}{2} - \frac {\sum_ {j \in E \cup L} d _ {j} t _ {j}}{2} \end{array}\tag{1}
$$

Once we have derived the average total inventory at the vendor, in the next subsection we focus our attention on obtaining the average total cost.

## 3.2. Average total cost

Since the buyers follow an EOQ pattern, the average total cost for a buyer j is given by $C _ { j } { = } k _ { j } / t _ { j } { + } h _ { j } d _ { j } t _ { j } / 2$

On the other hand, the average total cost $C _ { \mathrm { V } }$ for the vendor is the sum of the average holding cost, that is, $h _ { 0 } \overline { { \mathrm { I V } } }$ , where IV is given by Eq. (1), plus the average setup cost, that is $k _ { 0 } / t _ { 0 } .$ Therefore, $C _ { \mathrm { V } }$ can be formally expressed as follows

$$
\begin{array}{l} C _ {V} = \frac {k _ {0}}{t _ {0}} + h _ {0} \left[ \sum_ {i \in E \cup L} \frac {d _ {i} t _ {i}}{P} \sum_ {j = 1} ^ {N} d _ {j} + \sum_ {j \in G} \frac {d _ {j} t _ {j}}{P} \left(\frac {d _ {j}}{2} + \sum_ {i = j + 1} ^ {N} d _ {i}\right) \right] \\ + h _ {0} \left[ \left(1 - \frac {\sum_ {j \in E \cup L} d _ {j}}{P}\right) \frac {t _ {0} \sum_ {j \in E \cup L} d _ {j}}{2} - \frac {\sum_ {j \in E \cup L} d _ {j} t _ {j}}{2}) \right] \end{array}
$$

Then, the total cost per unit time is

$$
C _ {\mathrm{T}} = C _ {\mathrm{V}} + \sum_ {j = 1} ^ {N} C _ {j} = \frac {k _ {0}}{t _ {0}} + h _ {0} \left[ \sum_ {i \in E \cup L} \frac {d _ {i} t _ {i}}{P} \sum_ {j = 1} ^ {N} d _ {j} + \sum_ {j \in G} \frac {d _ {j} t _ {j}}{P} \left(\frac {d _ {j}}{2} + \sum_ {i = j + 1} ^ {N} d _ {i}\right) \right] (2)
$$

$$
+ h _ {0} \left[ \left(1 - \frac {\sum_ {j \in E \cup L} d _ {j}}{P}\right) \frac {t _ {0} \sum_ {j \in E \cup L} d _ {j}}{2} - \frac {\sum_ {j \in E \cup L} d _ {j} t _ {j}}{2}) \right] + \sum_ {j = 1} ^ {N} \left(\frac {k _ {j}}{t _ {j}} + \frac {h _ {j} d _ {j} t _ {j}}{2}\right)
$$

Since $t _ { j } = \mathrm { t } _ { 0 } , j \in E ,$ we can rearrange $\operatorname { E q . } \left( 2 \right)$ to give

$$
C _ {\mathrm{T}} = \frac {K _ {0}}{t _ {0}} + \frac {t _ {0} H _ {0}}{2} + \sum_ {j \in L \cup G} \left[ \frac {k _ {j}}{t _ {j}} + \frac {t _ {j} H _ {j}}{2} \right]\tag{3}
$$

where

$$
K _ {0} = k _ {0} + \sum_ {j \in E} k _ {j}
$$

$$
H _ {0} = h _ {0} \left(1 - \frac {\sum_ {j \in E \cup L} d _ {j}}{P}\right) \sum_ {j \in E \cup L} d _ {j} + h _ {0} \frac {2 \sum_ {j \in E} d _ {j}}{P} \sum_ {j = 1} ^ {N} d _ {j} + \sum_ {j \in E} d _ {j} (h _ {j} - h _ {0})
$$

$$
H _ {j} = \left\{ \begin{array}{l l} d _ {j} (h _ {j} - h _ {0}) + \frac {2 h _ {0} d _ {j}}{P} \sum_ {i = 1} ^ {N} d _ {i} & \text { if } j \in L \\ d _ {j} h _ {j} + \frac {2 h _ {0} d _ {j}}{P} \left(\frac {d _ {j}}{2} + \sum_ {i = j + 1} ^ {N} d _ {i}\right) & \text { if } j \in G \end{array} \right.
$$

It is worth noting that the vendor holds inventory not only during the time until the buyers place an order but also while the whole lot is produced. Hence the expression $H _ { j }$ consists of two parts. Speci<sup>fi</sup>cally, the <sup>fi</sup>rst term $d _ { j } ( h _ { j } - h _ { 0 } ) , { \mathrm { i f } } j { \in } \bar { L }$ , or $d _ { j } h _ { j } , \operatorname { i f } j \in G ,$ represents the echelon cost and the classical holding cost at buyer j, respectively. The second terms correspond to the holding cost incurred by the vendor during the time needed to produce the units required by the buyers. Moreover, the expressions for $H _ { 0 }$ and H<sub>j</sub> are consistent with those obtained by [19] for the case where the production is instantaneous, that is, $P \longrightarrow \infty$

## 3.3. The constraints

The cost formulation in Eq. (3) is based on the integer-ratio constraints, i.e., both $t _ { j } / t _ { 0 } , j \in G ,$ ; and $t _ { 0 } / t _ { j } , j \in L ,$ should be a positive integer. Furthermore, we also assume that each time a buyer places an order those buyers with smaller replenishment interval also order, that is, the quotients $t _ { j } / t _ { j - 1 } , j = 2 , \dots N$ ; are positive integers. However, it is easy to see that some of the constraints can be dropped because they are obtained from two other constraints. Accordingly, if we assume that $L = \{ 1 , . . . , l \}$ $E = \{ l { + } 1 , . . . , e \}$ and $G = \{ e + 1 , . . . , N \}$ , then, it suf<sup>fi</sup>ces to consider the following constraints

$$
t _ {j} = r _ {j - 1} t _ {j - 1}, r _ {j - 1} \text {   a   positive   integer,   } j \in \{2,..., l \}
$$

$t _ { 0 } = r _ { l } t _ { l } , r _ { l } \mathrm { ~ \boldsymbol { \mathsf { i } } ~ }$ a positive integer

<sup>¼</sup>t r t ; r a positive integer

$$
t _ {j} = r _ {j} t _ {j - 1}, r _ {j} \text {   a   positive   integer, } \quad j \in \{e + 2,..., N \}
$$

Moreover, to ensure the feasibility of a solution we require that the vendor delivers the orders on time. Remark that the vendor supplies to all the buyers only at the beginning of each cycle. Then, we should guarantee that the time needed to produce $\textstyle \sum _ { j = 1 } ^ { N } d _ { j } t _ { j }$ units of item is smaller than the replenish-<sup>¼</sup>ment intervals at the buyers. That is, $\sum _ { j = 1 } ^ { N } d _ { j } t _ { j } / P { \le } t _ { i } , i = 1 , \ldots N .$

Therefore, the single-vendor multi-buyer problem can be formulated as follows

$$
C _ {\mathrm{T}} = \frac {K _ {0}}{t _ {0}} + \frac {t _ {0} H _ {0}}{2} + \sum_ {j \in L \cup G} \left[ \frac {k _ {j}}{t _ {j}} + \frac {t _ {j} H _ {j}}{2} \right]\tag{4}
$$

s.t.

$$
t _ {j} = r _ {j - 1} t _ {j - 1}, r _ {j - 1} \text {   a   positive   integer, } \quad j \in \{2,..., l \}\tag{5}
$$

$$
t _ {0} = r _ {l} t _ {l}, r _ {l} \text {   a   positive   integer   }\tag{6}
$$

$$
t _ {e + 1} = r _ {e + 1} t _ {0}, r _ {e + 1} \text {   a   positive   integer   }\tag{7}
$$

$$
t _ {j} = r _ {j} t _ {j - 1}, r _ {j} \text {   a   positive   integer }, \quad j \in \{e + 2,..., N \}\tag{8}
$$

$$
\frac {\sum_ {j = 1} ^ {N} d _ {j} t _ {j}}{P} \leq t _ {i}, \quad i \in \{1, \dots , N \}\tag{9}
$$

We outline below the procedure to compute sets $G ,$ L and E, which is based on the algorithm proposed by [19].

## 3.4. Algorithm for computing sets $G ,$ L and E

Step 1. Set $E { = } G { = } \emptyset , L { = } \{ 1 , { \ldots } , N \}$ . Then $C _ { \mathrm { T } }$ can be written as

$$
C _ {\mathrm{T}} = \frac {K _ {0}}{t _ {0}} + \frac {t _ {0} H _ {0}}{2} + \sum_ {j \in L \cup G} \left[ \frac {k _ {j}}{t _ {j}} + \frac {t _ {j} H _ {j}}{2} \right]
$$

$$
\text { where } H _ {0} = h _ {0} \left(1 - \frac {\sum_ {j \in L} d _ {j}}{P}\right) \sum_ {j \in L} d _ {j}
$$

and $\begin{array} { r } { H _ { j } = d _ { j } ( h _ { j } { - } h _ { 0 } ) + \frac { 2 h _ { 0 } d _ { j } } { P } \sum _ { i = 1 } ^ { N } d _ { i } . } \end{array}$

Differentiating $C _ { \mathrm { T } }$ with respect to $t _ { 0 }$ and the t s we obtain the following replenishment intervals

$$
t _ {0} = \left[ \frac {2 k _ {0}}{H _ {0}} \right] ^ {1 / 2}
$$

$$
t _ {j} = \left[ \frac {2 k _ {j}}{H _ {j}} \right] ^ {1 / 2}, \quad j \in \{1, \dots , N \}\tag{10}
$$

11

Now, we should sort the values t s to give a nondecreasing sequence. Without loss of generality we can assume that $t _ { 1 } \leq t _ { 2 } \leq . . . \leq t _ { N } . \mathsf { S e t } i = N$

Step $2 . \mathrm { ~ I f ~ } t _ { i } { \geq } t _ { 0 } ,$ update E and L as follows: $E  E \cup \{ i \}$ and $L \gets L | \{ i \}$

Since sets E and L have changed, $H _ { 0 }$ and $K _ { 0 }$ should be recalculated.

Assuming that $i \in G ,$ we compute the replenishment interval at the vendor and at buyer i, and we denote them by $t _ { 0 } ^ { \prime }$ and $t _ { i } ^ { \prime } ,$ respectively.

Afterward, if $t _ { i } ^ { \prime } { > } t _ { 0 } ^ { \prime }$ sets E and G are to be updated as follows: $E  E \backslash \{ i \}$ and $G  G \cup \{ i \}$

Consequently, $H _ { 0 } , K _ { 0 }$ and $H _ { i }$ have to be updated and $t _ { 0 }$ is set to $t _ { 0 } ^ { \prime } .$

Set $i { = } i { - } 1 . \operatorname { I f } i { > } 0$ go to Step 2. Otherwise, go to Step 3.

Step 3. Using sets $G , L$ and E we can compute the <sup>fi</sup>nal values of $H _ { 0 } , K _ { 0 }$ and $H _ { j } , j = 1 , . . . , N .$ Then,

$$
t _ {0} = \left[ \frac {2 K _ {0}}{H _ {0}} \right] ^ {1 / 2}\tag{12}
$$

$$
t _ {j} = t _ {0}, \quad j \in E\tag{13}
$$

$$
t _ {j} = \left[ \frac {2 k _ {j}}{H _ {j}} \right] ^ {1 / 2}, \quad j \in \{1, \dots , N \}\tag{14}
$$

For notational convenience we relabel the buyers again, so that, $L = \{ 1 , . . . , l \} , E = \{ l + 1 , . . . , e \}$ and $G = \{ e + 1 , . . . , N \}$

Since the expression of the replenishment interval at a buyer $i \in G$ involves the parameters of other buyers $j \in G ,$ we cannot guarantee that this approach for sorting the buyers yields an optimal classi<sup>fi</sup>cation.

In most cases, obtaining the total average cost for the singlevendor multi-buyer problem with <sup>fi</sup>nite production rate is an arduous task. However, applying integer-ratio policies yields the expression of the total average cost to be quite simple. Thus, the problem can be formulated as in Eqs. (4)–(9). Nevertheless, this problem is a nonlinear mixed integer programming problem and obtaining its optimal solution could be computationally inef<sup>fi</sup>cient when the number of buyers is large. Hence, in the next section, we introduce a heuristic procedure to compute near-optimal integer-ratio policies with reasonable running times.

## 4. Heuristic for computing integer-ratio policies

In this section, we develop a heuristic method based on an iterative approach for solving problem $( 4 ) - ( 9 )$ . Once sets $L =$ $\{ 1 , . . . , l \} , E = \{ l + 1 , . . . , e \}$ and $G = \{ e + 1 , . . . , N \}$ are computed, we determine the replenishment intervals t<sub>i</sub>s given by Eqs. (12)– (14). Obviously, these replenishment intervals only solve the relaxed problem, which is, dropping the constraints $( 5 ) \AA - \left( 9 \right)$ . If these replenishment intervals do not satisfy the constraint set in Eq. (9), then we add such a set into the objective function using Lagrange multipliers and we solve the dual problem. Thus, we have an initial solution which minimizes Eq. (4) subject to Eq. (9). A scheme of the Lagrangian relaxation is described in Appendix A.

Next, we compute the optimal values $r _ { i } , i = 1 , . . . l , e + 1 , . . . , N ,$ substituting the replenishment intervals corresponding to the initial solution into constraints given in Eqs. $( 5 ) \AA { - } \left( 8 \right)$ . However, in most cases, these values are not integers. Hence, we will use an iterative approach to determine near-optimal integer values $\boldsymbol { r } _ { i } ^ { * } , i = 1 , . . . l , e + 1 , . . . , N$ . This approach can be implemented using a decision tree with $N - | E |$ levels. where at each level two possible integer values for $r _ { i } , i { = } 1 , . . . l , e { + } 1 , . . . , N$ are considered. Remark that values $r _ { i } , i = l + 1 , . . . , e ,$ , are not included in the formulation of problem (4)–(9) because they correspond to buyers in set E.

At each iteration we use one of the constraints in Eqs. (5)–(8) to isolate the corresponding replenishment interval as a function of the value $r _ { i \cdot }$ Thus, we can express the cost function in terms of the value $r _ { i \cdot }$ In order to decide which branch of the decision tree should be explored in the next iteration, we compute the total cost for the two values that we analyze for r . Accordingly, the node with the greatest cost associated will be discarded.

Since there are four kind of constraints, and at each iteration we use one of them to compute a value $r _ { i } ^ { * } ,$ we should distinguish the following cases:

Case 1. If $i { \in } \{ 1 , { \dotsc } , l { - } 1 \}$

In this iteration, the values $r _ { 1 } ^ { * } , \ldots , r _ { i - 1 } ^ { * }$ have been already calculated and we want to compute the value r<sup>⁎</sup>. Moreover, we know the values $t _ { j } s$ and it holds that $t _ { j } = r _ { j }$ <sub>− 1</sub>t<sub>j</sub> $\cdot _ { 1 } , j { \in } \{ 2 , . . . , i \}$ . In this iteration we introduce the constraint $t _ { i + 1 } = r _ { i } t _ { i }$ which can be applied to obtain the real value r′ as $r _ { i } ^ { \prime } { = } t _ { i + 1 } / t _ { i }$

Then, depending on the value of the cost function, we will choose between $\dot { r } _ { i } ^ { * } { = } \lceil r _ { i } ^ { \prime } \rceil$ and $\dot { r _ { i } } ^ { * } { = } \lfloor r _ { i } ^ { \prime } \rfloor$ . If $\cdot r _ { i } ^ { \prime } { < } 1$ we set $\stackrel { * } { r _ { i } } = 1$

Now, taking into account that $t _ { j } = r _ { j - 1 } t _ { j - 1 } , \ j \in \{ 2 , . . . , i + 1 \}$ the total cost $C _ { \mathrm { T } }$ given in Eq. (4) can be reformulated in terms of $t _ { 0 } , \ t _ { j } ,$ with $j { \in } \{ i { + } 1 , { \ldots } , \ l \} \cup \{ e { + } 1 , { \ldots } , \ N \}$ and $r _ { i \cdot }$ Notice that values $\bar { r } _ { j } ^ { * } s , j { \in } \{ 1 , . . . , i - 1 \}$ , have been already determined and therefore they are <sup>fi</sup>xed values. Thus, the total cost (4) can be stated as follows

$$
C _ {\mathrm{T}} = \frac {K _ {0}}{t _ {0}} + \frac {t _ {0} H _ {0}}{2} + \frac {K _ {i + 1} ^ {\prime}}{t _ {i + 1}} + \frac {t _ {i + 1} H _ {i + 1} ^ {\prime}}{2} + \sum_ {j \in \{i + 2, \dots , l \} \cup G} \left[ \frac {k _ {j}}{t _ {j}} + \frac {t _ {j} H _ {j}}{2} \right]\tag{15}
$$

$$
K _ {i + 1} ^ {\prime} = k _ {i + 1} + \sum_ {j = 1} ^ {i} \left(\Pi_ {u = j} ^ {i - 1} r _ {u} ^ {*}\right) r _ {i} k _ {j}
$$

$$
\text { and } H _ {i + 1} ^ {\prime} = H _ {i + 1} + \sum_ {j = 1} ^ {i} \left(\Pi_ {u = j} ^ {i - 1} \frac {1}{r _ {u} ^ {*}}\right) \frac {1}{r _ {i}} H _ {j}.
$$

Then, taking the derivative of Eq. (15) with respect to $t _ { i + 1 }$ and setting it equal to zero, we obtain the expression of the new replenishment interval at buyer i+1, for known values $\boldsymbol { r } _ { j } ^ { * } \boldsymbol { s } , j \in \{ 1 , . . . , i - 1 \}$

That is,

$$
t _ {i + 1} = \left[ \frac {2 K _ {i + 1} ^ {\prime}}{H _ {i + 1} ^ {\prime}} \right] ^ {1 / 2}\tag{16}
$$

It is worth noting that the replenishment intervals $t _ { 0 }$ and $t _ { j } s , j { \in } \{ i { + } 2 , . . . , l \} \cup G ,$ do not change.

On the other hand, for each buyer $j { \in } \{ 1 , . . . , i \} ,$ the replenishment interval can be recalculated using constraints in Eq. (5).

Thus, the cost function in Eq. (15) can be rearranged using Eq. (16) to give

$$
C _ {\mathrm{T}} \left(r _ {i}\right) = \sqrt {2 K _ {0} H _ {0}} + \sqrt {2 K _ {i + 1} ^ {\prime} H _ {i + 1} ^ {\prime}} + \sum_ {j \in \{i + 2, \dots , l \} \cup G} \sqrt {2 k _ {j} H _ {j}}\tag{17}
$$

At this point, we compute $C _ { \mathrm { T } } \left( r _ { i } { = } \lfloor r _ { i } ^ { \prime } \rfloor \right)$ and $C _ { \mathrm { T } } \left( r _ { i } { = } [ r _ { i } ^ { \prime } ] \right)$ . We set $\begin{array} { r } { \dot { r _ { i } ^ { * } } = \lfloor r _ { i } ^ { \prime } \rfloor \operatorname { i f } C _ { \mathrm { T } } \left( r _ { i } { = } \lfloor r _ { i } ^ { \prime } \rfloor \right) { < } C _ { \mathrm { T } } \left( r _ { i } { = } \lceil r _ { i } ^ { \prime } \rceil \right) } \end{array}$ . Otherwise, we set $\begin{array} { r } { \dot { r } _ { i } ^ { * } { = } \lceil r _ { i } ^ { \prime } \rceil . } \end{array}$ If r′b 1 we set $\begin{array} { r } { \dot { r } _ { i } = 1 . } \end{array}$

Once the value r<sup>⁎</sup> is determined, we calculate the new replenishment interva $t _ { i + 1 }$ from Eq. (16). The replenishment intervals $\quad t _ { j } s , j = 1 , . . . , i ,$ , are also updated using constraints in Eq. (5), that is, $t _ { j } = t _ { j + 1 } / r _ { j } ^ { * } , j = 1 , \ldots i$

Case 2. If i = l.

In this case, the values $r _ { 1 } ^ { * } { \xrightarrow [ { \cdots } ] { * } } r _ { l - { \mathrm { ~ } } 1 } ^ { * }$ are already known and we use the constraint $t _ { 0 } = r _ { l } t _ { l }$ to determine the real value $r _ { l } ^ { \prime } .$ That is, $r _ { l } ^ { \prime } = t _ { 0 } / t _ { l } .$

Moreover, since $t _ { j } = r _ { j - 1 } t _ { j - 1 } ,$ for those buyers $j { \in } \{ 2 , . . . , l \}$ and $t _ { 0 } = r _ { l } t _ { l }$ , it is easy to see that the cost function given in Eq. (4) can be reformulated in terms of $t _ { 0 } , t _ { j } , j { \in } \{ e + 1 , . . . , N \}$ and $r _ { l }$ to give

$$
C _ {\mathrm{T}} = \frac {K _ {0} ^ {\prime}}{t _ {0}} + \frac {t _ {0} H _ {0} ^ {\prime}}{2} + \sum_ {j = e + 1} ^ {N} \left[ \frac {k _ {j}}{t _ {j}} + \frac {t _ {j} H _ {j}}{2} \right]\tag{18}
$$

where $K _ { 0 } ^ { ' } = K _ { 0 } + \sum _ { j = 1 } ^ { l } \Big ( \Pi _ { u = j } ^ { l - 1 } r _ { u } ^ { * } \Big ) r _ { l } k _ { j }$

$$
\text { and } H _ {0} ^ {\prime} = H _ {0} + \sum_ {j = 1} ^ {l} \left(\Pi_ {u = j} ^ {l - 1} \frac {1}{r _ {u} ^ {*}}\right) \frac {1}{r _ {l}} H _ {j}.
$$

Taking the derivative of Eq. (18) with respect to $t _ { 0 }$ and setting it equal to zero, we have that the expression for the new replenishment interval $t _ { 0 }$ is given by

$$
t _ {0} = \left[ \frac {2 K _ {0} ^ {\prime}}{H _ {0} ^ {\prime}} \right] ^ {1 / 2}\tag{19}
$$

Substituting Eq. (19) into Eq. (18), the total cost $C _ { \mathrm { T } }$ in Eq. (18) can be formulated as follows

$$
C _ {\mathrm{T}} \left(r _ {l}\right) = \sqrt {2 K _ {0} ^ {\prime} H _ {0} ^ {\prime}} + \sum_ {j \in G} \sqrt {2 k _ {j} H _ {j}}\tag{20}
$$

Now, if $C _ { \mathrm { T } } \ ( r _ { l } { = } \lfloor r _ { l } ^ { \prime } \rfloor ) { < } C _ { \mathrm { T } } \ ( r _ { l } { = } \lceil r _ { l } ^ { \prime } \rceil )$ we set $\dot { r } _ { l } ^ { * } { = } \lfloor r _ { l } ^ { \prime } \rfloor$ . Otherwise, we set $\vec { r } _ { l } ^ { * } = [ r _ { l } ^ { \prime } ] . \mathrm { A g a i n } , \mathrm { i f } r _ { l } ^ { \prime } < 1$ we set $r _ { l } ^ { * } { = } 1 .$

Afterward, the new replenishment interval $t _ { 0 }$ is computed using Eq. (19). The replenishment interval $t _ { l }$ is updated taking into account constraint (6), i.e., $t _ { l } = t _ { 0 } / r _ { l } ^ { * }$ , and the values $t _ { j } s ,$ $j = 1 , . . . , l - 1$ <sup>¼</sup>, are recalculated using constraints in Eq. (5).

Case 3. If i=e+1.

Recall that values $r _ { i } ^ { * } , \ i { = } l { + } 1 , . . . , \ e ,$ , are not considered because they correspond to buyers belonging to set E.

Now, we have already computed the values $r _ { 1 } ^ { * } , . . . , r _ { l } ^ { * }$ , and the objective is to determine the value $r _ { e + 1 } ^ { * } .$ . In this case, the real value $r _ { e + 1 } ^ { \prime }$ <sup>þ</sup>is obtained from the constraint $t _ { e + 1 } = r _ { e } .$ <sub>+ 1</sub>t<sub>0</sub>. <sup>þ</sup>Thus, we have $r _ { e + 1 } ^ { \prime } = t _ { e + 1 } / t _ { 0 } .$

<sup>þ ¼ þ</sup>Similarly to the previous cases, we can reformulate the cost function given in Eq. (4) to depend only on the values t s with $j { \in } \{ e \colon 1 , . . . , N \}$ and $r _ { e + 1 } .$ . That is, C can be written as follows

$$
\begin{array}{l} C _ {\mathrm{T}} = \frac {K _ {e + 1} ^ {\prime}}{t _ {e + 1}} + \frac {t _ {e + 1} H _ {e + 1} ^ {\prime}}{2} + \sum_ {j = e + 2} ^ {N} \left[ \frac {k _ {j}}{t _ {j}} + \frac {t _ {j} H _ {j}}{2} \right] \\ \text { where } K _ {e + 1} ^ {\prime} = k _ {e + 1} + r _ {e + 1} K _ {0} + \sum_ {j = 1} ^ {l} \left(\Pi_ {u = j} ^ {l} r _ {u} ^ {*}\right) r _ {e + 1} k _ {j} \\ \text { and } H _ {e + 1} ^ {\prime} = H _ {e + 1} + \frac {H _ {0}}{r _ {e + 1}} + \sum_ {j = 1} ^ {l} \left(\Pi_ {u = j} ^ {l} \frac {1}{r _ {u} ^ {*}}\right) \frac {1}{r _ {e + 1}} H _ {j}. \end{array}\tag{21}
$$

Therefore, from Eq. (21) we obtain that the new replenishment interval at buyer e+1 is given by the following expression

$$
t _ {e + 1} = \left[ \frac {2 K _ {e + 1} ^ {\prime}}{H _ {e + 1} ^ {\prime}} \right] ^ {1 / 2}\tag{22}
$$

Next, similar to Case 1 and Case 2, Eq. (21) can be reformulated using Eq. (22) to give

$$
C _ {T} \left(r _ {e + 1}\right) = \sqrt {2 K _ {e + 1} ^ {\prime} H _ {e + 1} ^ {\prime}} + \sum_ {j \in G} \sqrt {2 k _ {j} H _ {j}}\tag{23}
$$

$$
\lceil r _ {e + 1} ^ {\prime} \rceil)
$$

$$
r _ {e + 1} ^ {*} = \left\lfloor r _ {e + 1} ^ {\prime} \right\rfloor \text {if} C _ {T} \left(r _ {e + 1} = \left\lfloor r _ {e + 1} ^ {\prime} \right\rfloor\right) <   C _ {T} \left(r _ {e + 1} = \right.
$$

$$
r _ {e + 1} ^ {*} = \left[ r _ {e + 1} ^ {\prime} \right]. \text {   If   } r _ {e + 1} ^ {\prime} <   1
$$

$$
r _ {e + 1} ^ {*} = 1
$$

<sup>þ Þ þ ¼</sup>Finally, substituting the value $r _ { e + 1 } ^ { * }$ <sup>þ þ ¼</sup>into Eq. (22) we have the new replenishment interval $t _ { e + 1 } .$ <sup>þ</sup>Moreover, from Eq. (7) we determine the new replenishment interval $t _ { 0 }$ as $t _ { 0 } = t _ { e + 1 } / r _ { e + 1 } ^ { \ast } ,$ and the replenishment intervals $t _ { l }$ and $\begin{array} { r } { t _ { j } s , j = 1 , . . . , l - 1 , } \end{array}$ <sup>þ</sup>, are also updated using constraint (6) and constraints in Eq. (5), respectively.

Case 4. If $i { \in } \{ e { + } 2 , . . . , N \}$

We must compute the value $r _ { i } ^ { * }$ taking into account that values $r _ { 1 } ^ { * } , . . . , r _ { l } ^ { * }$ and values $r _ { e + 1 } ^ { * } , \ldots , r _ { i - 1 } ^ { * }$ have been already <sup>þ</sup>calculated. Furthermore, constraints $( 5 ) – ( 7 )$ ) hold, and also $t _ { j } =$ $r _ { j } t _ { j - 1 } , j { \in } \{ e + 2 , . . . , i - 1 \} ,$ . In this iteration we introduce the constraint $t _ { i } = r _ { i } t _ { i - 1 }$ , which is used to determine the real value $r _ { i } ^ { \prime }$ as follows $r _ { i } ^ { \prime } { = } t _ { i } / t _ { i }$ <sub>− 1</sub>.

Thus, the total cost given in Eq. (4) can be expressed in the following way

$$
C _ {\mathrm{T}} = \frac {K _ {i} ^ {\prime}}{t _ {i}} + \frac {t _ {i} H _ {i} ^ {\prime}}{2} + \sum_ {j = i + 1} ^ {N} \left[ \frac {k _ {j}}{t _ {j}} + \frac {t _ {j} H _ {j}}{2} \right]\tag{24}
$$

$$
\begin{array}{l} \text { where } K _ {i} ^ {\prime} = k _ {i} + \left(\prod_ {u = e + 1} ^ {i - 1} r _ {u} ^ {*}\right) r _ {i} K _ {0} + \sum_ {j = e + 1} ^ {i - 1} \left(\prod_ {u = j + 1} ^ {i - 1} r _ {u} ^ {*}\right) r _ {i} k _ {j} \\ \qquad + \sum_ {j = 1} ^ {l} \left(\prod_ {u = j} ^ {l} r _ {u} ^ {*}\right) \left(\prod_ {u = e + 1} ^ {i - 1} r _ {u} ^ {*}\right) r _ {i} k _ {j} \\ \text { and } H _ {i} ^ {\prime} = H _ {i} + \left(\prod_ {u = e + 1} ^ {i - 1} \frac {1}{r _ {u} ^ {*}}\right) \frac {1}{r _ {i}} H _ {0} + \sum_ {j = e + 1} ^ {i - 1} \left(\prod_ {u = j + 1} ^ {i - 1} \frac {1}{r _ {u} ^ {*}}\right) \frac {1}{r _ {i}} H _ {j} \\ \qquad + \sum_ {j = 1} ^ {l} \left(\prod_ {u = j} ^ {l} \frac {1}{r _ {u} ^ {*}}\right) \left(\prod_ {u = e + 1} ^ {i - 1} \frac {1}{r _ {u} ^ {*}}\right) \frac {1}{r _ {i}} H _ {j}. \end{array}
$$

In this case, the above expressions seem to be more complex than those obtained in the previous iterations. This is due to the fact that in this case the four kinds of constraints are involved in the formulation of the cost.

Then, taking the derivative of Eq. (24) with respect to $t _ { i }$ and setting it equal to zero, we obtain the expression of the new replenishment interval $t _ { i }$

$$
t _ {i} = \left[ \frac {2 K _ {i} ^ {\prime}}{H _ {i} ^ {\prime}} \right] ^ {1 / 2}\tag{25}
$$

and, then, using Eq. (25) the total cost (24) can be written as follows

$$
C _ {\mathrm{T}} (r _ {i}) = \sqrt {2 K _ {i} ^ {\prime} H _ {i} ^ {\prime}} + \sum_ {j = i + 1} ^ {N} \sqrt {2 k _ {j} H _ {j}}\tag{26}
$$

Now we compute $C _ { \mathrm { T } } \left( r _ { i } { = } [ r _ { i } ^ { \prime } ] \right)$ and $C _ { \mathrm { T } } \left( r _ { i } { = } [ r _ { i } ^ { \prime } ] \right) . \mathrm { I f } C _ { \mathrm { T } } \left( r _ { i } { = } [ r _ { i } ^ { \prime } ] \right) { < }$ $C _ { \mathrm { T } } \ ( r _ { i } { = } [ r _ { i } ^ { \prime } ] )$ , then, $\ddot { r _ { i } } { = } \lfloor r _ { i } ^ { \prime } \rfloor$ and $r _ { i } ^ { * } { = } [ r _ { i } ^ { \prime } ] ,$ , otherwise. Again, if $r _ { i } ^ { \prime } < 1$ we set $\boldsymbol { r } _ { i } ^ { * } { = } 1$

Once the value $r _ { i } ^ { * }$ is determined, we compute the new replenishment interval t from Eq. (25). Likewise to the above cases, the other replenishment intervals are recalculated using constraints in (5)–(8).

After computing the corresponding replenishment intervals we should check if they satisfy the constraint set in Eq. (9). If at any level of the decision tree this set of constraints does not hold, then we add such a set into the objective function using Lagrange multipliers and we solve the dual problem. A sketch of the heuristic procedure is given in Algorithm 1.

## Algorithm 1. Heuristic for computing integer-ratio policies

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Step 1
Compute the values $t_{js}$ using Eqs. (12)-(14) and check if constraints (9) hold.
If these constraints are not satisfied, then add them into the objective function using the Lagrange multipliers and solve the dual problem. A scheme of the Lagrangian relaxation is described in Appendix A.
Set $s = 1$ and go to Step 2.
Step 2
if $s \in \{1, \dots, l-1\}$ (Case 1), then
    recalculate the replenishment intervals using Eq. (5)
end if
if $s = l$ (Case 2), then
    compute the new replenishment intervals from Eqs. (5) and (6)
end if
if $s \in \{l+1, \dots, e\}$ then
    go to Step 4
end if
if $s = e + 1$ (Case 3), then
    update the replenishment intervals using Eqs. (5)-(7)
end if
if $s \in \{e+2, \dots, N\}$ (Case 4), then
    determine the new replenishment intervals from Eqs. (5)-(8)
</div>

If constraints in Eq. (9) are satis<sup>fi</sup>ed go to Step 4. Otherwise, go to Step 3. Step 3

Add the constraints into the objective function using the Lagrange multipliers and solve the dual problem. Go to Step 4.

Set s=s+1. If sb=N go to Step 2. Otherwise all the replenishment intervals have been already computed. Stop.

## 5. Decentralized policies

In this section we show how the problem should be addressed in case of independence among the vendor and the buyers. Under this situation, we propose a two-level optimization approach consisting of computing <sup>fi</sup>rst the order quantities at the buyers, and then, determining the shipment schedule at the vendor. Accordingly, since the buyers follow an EOQ pattern, the total cost at buyer j can be easily obtained as $C _ { j } = k _ { j } / t _ { j } + h _ { j } d _ { j } t _ { j } / 2$ . Moreover, the optimal replenishment intervals at the buyers are given by the following expression

$$
t _ {j} ^ {*} = \sqrt {\frac {2 k _ {j}}{h _ {j} d _ {j}}}, \quad j \in \{1, \dots , N \}\tag{27}
$$

Since there is no relationship among these replenishment intervals, it seems obvious that the vendor behaves as an inventory systemwith time-varying demand. When the demand rate varies with time, the most widely known procedure for deriving the optimal solution is that credited to Wagner and Whitin [24], although other more ef<sup>fi</sup>cient approaches have been developed, for example, by [23], [6] and [4]. However, all these approaches consider in<sup>fi</sup>nite production rate, hence we cannot directly apply them in our case. Fortunately, [15] shows how a dynamic lot-sizing problem with <sup>fi</sup>nite production rate can be reformulated to take the same form as the corresponding in<sup>fi</sup>nite production rate problem. Therefore, the Wagner and Whitin algorithm or any of the other techniques currently available, can be applied to the new reformulated problem.

The main problem is to determine the demand vector at the vendor. It is worth noting that the optimal replenishment intervals at the buyers are real values. Therefore, we cannot assure that a point in time exists where all the buyers order simultaneously. Hence, the number of periods of the demand vector at the vendor could not be <sup>fi</sup>nite. To overcome this problem we propose an approach which consists of either truncating or rounding up the real replenishment intervals to rational times. It is clear that the solution provided by this method is not the actual optimal plan but it is quite a good approximation. A detailed explanation of this approach can be found in [1]. Once the demand vector is obtained, we should apply Hill's approach to obtain the optimal shipment schedule at the vendor.

## 6. Numerical example

In order to illustrate the solution procedures developed in Sections 4 and 5, let us consider a single-vendor three-buyer system with the input data given in Table 1. Below we solve this problem using the procedures commented in the previous sections.

Input data for an instance of the single-vendor three-buyer problem

<table><tr><td></td><td>Vendor</td><td>Buyer 1</td><td>Buyer 2</td><td>Buyer 3</td></tr><tr><td> $h_j$ </td><td>46</td><td>79</td><td>84</td><td>55</td></tr><tr><td> $k_j$ </td><td>48</td><td>36</td><td>25</td><td>62</td></tr><tr><td> $d_j$ </td><td>44</td><td>5</td><td>5</td><td>34</td></tr><tr><td>P</td><td>2853</td><td></td><td></td><td></td></tr></table>

## 6.1. Integer-ratio policy

First, we have to compute sets G, L and E using the algorithm given in Section 3.4. The steps involved in computing such sets are given below.

Step 1. Set $E = G = 0$ and $\boldsymbol { L } = \left\{ 1 , . . . , N \right\}$ . Then, from Eqs. (10) and (11) we have $t _ { 0 } = 0 . 2 1 9 4$ $t _ { 1 } = 0 . 6 4 6 8 , t _ { 2 } = 0 . 5 0 3 6$ and $t _ { 3 } = 0 . 5 9 1 6$ . Relabel the buyers so that, $t _ { 1 } \leq t _ { 2 } \leq t _ { 3 } .$ Thus, buyer 1=buyer 2, buyer 2=buyer 3 and buyer 3=buyer 1, and t =0.5036, t =0.5916 and $t _ { 3 } = 0 . 6 4 6 8$

Set i = 3. Go to Step 2.

Step 2. Iteration 1. Since $t _ { 3 } = 0 . 6 4 6 8 > t _ { 0 } = 0 . 2 1 9 4 ,$ update sets E and L so that, E={3} and $L = \{ 1 , 2 \}$ . Moreover, since $t _ { 3 } ^ { \prime } =$ $0 . 4 2 6 7 > t _ { 0 } ^ { \prime } = 0 . 2 3 2 9$ , we conclude that buyer 3∈G. Hence, set E=Ø, L={1, 2}, G={3}, t =0.4267, $t _ { 0 } { = } 0 . 2 3 2 9$ and i=2.

Iteration 2. Since $t _ { 2 } { = } 0 . 5 9 1 6 { > } t _ { 0 } { = } 0 . 2 3 2 9 ,$ , sets E and L are updated to give E={2} and L={1}. Then, $t _ { 0 } = t _ { 2 } = 0 . 3 2 1 8 .$ . Now, t′= $0 . 2 5 5 8 < t _ { 0 } ^ { \prime } = 0 . 6 4 6 6 ,$ so we cannot move buyer 2 to set G. Set i=1.

Iteration 3. Since $t _ { 1 } = 0 . 5 0 3 6 > t _ { 0 } = 0 . 3 2 1 8 ,$ we update sets E and L so that, E={1, 2} and L=Ø. Moreover, as $t _ { 1 } ^ { \prime } { = } 0 . 3 4 4 5 { > } t _ { 0 } ^ { \prime } { = }$ 0.3403, we conclude that buyer 1∈G. Then, set $E = \{ 2 \} , \ G =$ {3, 1}, t =0.3445, t =0.3403 and i=0. Go to Step 3.

Step 3. The <sup>fi</sup>nal sets are L=Ø, E={2} and $G = \{ 1 , 3 \} ,$ . For notational convenience we relabel the buyers again, so that buyer 1=buyer 2 and buyer 2=buyer 1. Then, $L = \emptyset , E = \{ 1 \}$ and $G = \{ 2 , 3 \}$ , and t =t =0.3403, t =0.3445 and $t _ { 3 } = 0 . 4 2 6 7 .$

After determining sets G, L and E, the problem can be stated as follows

$$
\min \frac {K _ {0}}{t _ {0}} + \frac {t _ {0} H _ {0}}{2} + \frac {k _ {2}}{t _ {2}} + \frac {t _ {2} H _ {2}}{2} + \frac {k _ {3}}{t _ {3}} + \frac {t _ {3} H _ {3}}{2}
$$

subject to

$$
\begin{array}{l} t _ {2} = r _ {2} t _ {0}, \\ t _ {3} = r _ {3} t _ {2}, \end{array}
$$

$$
\frac {d _ {1} t _ {0} + d _ {2} t _ {2} + d _ {3} t _ {3}}{P} \leq t _ {0}\tag{28}
$$

$$
\frac {d _ {1} t _ {0} + d _ {2} t _ {2} + d _ {3} t _ {3}}{P} \leq t _ {2}\tag{29}
$$

$$
\frac {d _ {1} t _ {0} + d _ {2} t _ {2} + d _ {3} t _ {3}}{P} \leq t _ {3}\tag{30}
$$

where

$$
\begin{array}{l} K _ {0} = k _ {0} + k _ {1} = 1 1 0, \\ H _ {0} = h _ {0} \left(1 - \frac {d _ {1}}{P}\right) d _ {1} + h _ {0} \frac {2 d _ {1}}{P} \sum_ {j = 1} ^ {3} d _ {j} + d _ {1} (h _ {1} - h _ {0}) = 1 8 9 9. 6 0 2 5, \\ H _ {2} = d _ {2} h _ {2} + \frac {2 h _ {0} d _ {2}}{P} \left(\frac {d _ {2}}{2} + d _ {3}\right) = 4 2 1. 2 0 9 2 \\ H _ {3} = d _ {3} h _ {3} + \frac {h _ {0} d _ {3} d _ {3}}{P} = 3 9 5. 4 0 3 0. \end{array}
$$

The next steps of the heuristic approach can be summarized as follows.

Step 1. The initial order intervals satis<sup>fi</sup>ed the feasibility constraints (28)–(30). Therefore, set s=1 and go to Step 2.

Average and maximum deviations of the integer-ratio policies from the lower bound, and average number of times that the heuristic needs to use the Lagrangian relaxation

<table><tr><td rowspan="2">N</td><td colspan="3"> $P \sim {U}_{P1}$ </td><td colspan="3"> $P \sim {U}_{P2}$ </td><td colspan="3"> $P \sim {U}_{P3}$ </td></tr><tr><td>Average deviation (%)</td><td>Maximum deviation (%)</td><td>Average Lagrangian</td><td>Average deviation (%)</td><td>Maximum deviation (%)</td><td>Average Lagrangian</td><td>Average deviation (%)</td><td>Maximum deviation (%)</td><td>Average Lagrangian</td></tr><tr><td>5</td><td>0.905</td><td>2.599</td><td>0.14</td><td>1.052</td><td>4.395</td><td>0</td><td>1.050</td><td>4.407</td><td>0</td></tr><tr><td>10</td><td>0.641</td><td>5.212</td><td>5.71</td><td>0.973</td><td>2.633</td><td>0.51</td><td>1.562</td><td>3.499</td><td>0</td></tr><tr><td>15</td><td>0.351</td><td>1.675</td><td>12.40</td><td>0.508</td><td>3.696</td><td>3.12</td><td>0.635</td><td>3.687</td><td>1.09</td></tr><tr><td>20</td><td>0.209</td><td>0.814</td><td>20.12</td><td>0.285</td><td>1.563</td><td>5.32</td><td>0.324</td><td>2.093</td><td>3.16</td></tr></table>

Step 2. Since $s { = } e \ g _ { 0 }$ to Step 4.

Step 4. Set $s = 2$ and go to Step 2.

Step 2. From Eq. (23), it follows that

$$
C _ {T} (r _ {2}) = \sqrt {2 (k _ {2} + r _ {2} K _ {0}) \left(H _ {2} + \frac {H _ {0}}{r _ {2}}\right) + \sqrt {2 k _ {3} H _ {3}}}.
$$

Since $\begin{array} { r } { r _ { 2 } ^ { \prime } = \frac { t _ { 2 } } { t _ { n } } = \frac { 0 . 3 4 4 5 } { 0 . 3 4 0 3 } = 1 . 0 1 2 3 . } \end{array}$ we choose between $r _ { 2 } ^ { * } = 1$ and $r _ { 2 } ^ { * } = 2 . \mathrm { ~ A s ~ } \stackrel { \sim } { C } _ { \mathrm { T } } ( r _ { 2 } = 1 ) = 9 6 0 . 3 2 0 3 < C _ { \mathrm { T } } ( r _ { 2 } = 2 ) = 9 8 8 . 3 5 8 6 ,$ , we set $r _ { 2 } ^ { * } = 1$ . Now, using Eq. (22) we recalculate $t _ { 2 }$ to give $t _ { 2 } { = } 0 . 3 4 1 0$ . Hence, $\begin{array} { r } { t _ { 1 } = t _ { 0 } = \frac { t _ { 2 } } { r _ { \ast } ^ { \ast } } = 0 . 5 9 7 8 } \end{array}$ : Moreover, it is easy to see that the feasibility constraints (28)–(30) hold, and hence we proceed to go to Step 4.

Step 4. Set s= 3 and go to Step 2.

Step 2. Now Eq. (26) yields

$$
C _ {\mathrm{T}} \left(r _ {3}\right) = \sqrt {2 \left(k _ {3} + r _ {3} k _ {2} + r _ {3} r _ {2} ^ {*} K _ {0}\right) \left(H _ {3} + \frac {H _ {2}}{r _ {3}} + \frac {H _ {0}}{r _ {3} r _ {2} ^ {*}}\right)}.
$$

Since $\begin{array} { r } { r _ { 3 } ^ { \prime } = \frac { t _ { 3 } } { t _ { 7 } } = \frac { 0 . 4 2 6 7 } { 0 . 3 4 1 0 } = 1 . 2 5 1 3 } \end{array}$ ; we should choose between $r _ { 3 } ^ { * } = 1$ and $r _ { 3 } ^ { * } { = } \tilde { 2 } .$ <sup>¼ ¼</sup>Given that $C _ { \mathrm { T } } \ ( r _ { 3 } = 1 ) = 9 6 3 . 8 1 8 1 < C _ { \mathrm { T } } \ ( r _ { 3 } = 2 ) =$ 975.7843, we set $r _ { 3 } ^ { * } { = } 1 .$ . Next, from Eq. (25) we recalculate t to give $t _ { 3 } = 0 . 3 5 4 8$ . Hence, $\begin{array} { r } { t _ { 2 } = \frac { t _ { 3 } } { r _ { 2 } } = 0 . 3 5 4 8 } \end{array}$ and $\begin{array} { r } { t _ { 1 } = t _ { 0 } = \frac { t _ { 2 } } { r _ { 7 } } = } \end{array}$ <sup>¼ ¼ ¼ ¼ ¼</sup>0:3548: Note that these replenishment intervals are feasible, and hence the procedure goes to Step 4.

Step 4. Set s = 4. Since s N N, stop.

The integer-ratio policy is given by the following replenishment intervals $t _ { 0 } = t _ { 1 } = t _ { 2 } = t _ { 3 } = 0 . 3 5 4 8$ , and the cost incurred by this policy is 963.8181 \$/time unit.

## 6.2. Decentralized policy

We <sup>fi</sup>rst should compute the optimal replenishment intervals at the buyers using Eq. (27). Thus, we obtain $t _ { 1 } = 0 . 4 2 6 9 ,$ t =0.3450 and $t _ { 3 } = 0 . 2 5 7 5$ . Next, these values t s are rounded off to obtain the following order intervals, $t _ { 1 } = 0 . 4 , \ t _ { 2 } = 0 . 3$ and $t _ { 3 } = 0 . 3 ,$ . Consequently, the time cycle for the vendor is 1.2.

Moreover, the order quantities at the buyers are $Q _ { 1 } = 2 ,$ $Q _ { 2 } = 1 . 5$ and $Q _ { 3 } = 1 0 . 2$

Now, it can be easily determined that the instants of time where the vendor receives an order are given by the following time vector (0.0, 0.3, 0.4, 0.6, 0.8, 0.9).

In addition, the quantities which are ordered at each instant, that is, the vector of demands at the vendor is (13.7, 11.7, 2, 11.7, 2, 11.7).

We apply now the procedure devised in [15] to obtain the quantities that the vendor should order at each instant. For this example, the solution provided by Hill's approach is the following (13.7, 13.7, 0, 13.7, 0, 11.7).

The cost incurred by the vendor when this policy is applied is 186.9660 \$/time unit, and the overall cost including the costs at the buyers and at the vendor is 989.4660 \$/time unit.

As you can see, in this instance the integer-ratio policy outperforms the decentralized strategy. However, the computational experiment shows that there are examples where just the opposite happens. Consequently, the computational results also evidence that the decision about which policy must be chosen depends on the values of the parameters.

## 7. Computational results

In order to illustrate the performance of the procedures introduced in Sections 4 and 5 we have carried out a numerical study. The results of this computational experiment are reported in Tables 2–9.

First, we evaluate the effectiveness of the integer-ratio policies computed by the heuristic. Then, we compare these integer-ratio policies with the decentralized strategies. Finally, we analyze the effect of the different parameters of the problem on the total cost for both strategies.

7.1. Performance of the heuristic for computing integer-ratio policies

The parameters considered in the problem are the following. The number of buyers N is 5,10,15 and 20. The values for $h _ { 0 } , k _ { 0 } , k _ { j }$ and $d _ { j }$ are taken from a uniform distribution U[1, 100]. The parameter $h _ { j }$ has been chosen from a uniform distribution $U [ h _ { 0 } , \ 1 0 0 + h _ { 0 } ]$ . Finally, the production rate at the vendor is randomly generated from three uniform distributions U [100+D, $5 0 0 + { \cal D } ] \equiv U _ { P 1 } ,$ $U [ 1 0 0 0 + D ,$ $5 0 0 0 + D ] \equiv U _ { P 2 }$ , and U $[ 1 0 , 0 0 0 + D , 2 0 , 0 0 0 + D ] \equiv U _ { P 3 } ,$ , where $\begin{array} { r } { D = \sum _ { j = 1 } ^ { N } d _ { j } } \end{array}$ : The possible <sup>¼ ¼</sup>combinations of N and P give a total of 12 sets of problems and for each we carried out 100 instances. Therefore, 1200 instances have been solved and the results are summarized in Tables 2–4.

Let $C _ { \mathrm { I R } }$ denote the cost of the integer-ratio policy computed by the heuristic and let LB be the lower bound for the problem de<sup>fi</sup>ned by Eqs. (4)–(9). This lower bound is simply obtained solving the relaxed problem, dropping the constraints $( 5 ) \AA { - } \left( 8 \right)$

In Table 2 we compare the cost of the integer-ratio policy provided by the heuristic with the lower bound. The <sup>fi</sup>rst column contains the number of buyers. In columns two, <sup>fi</sup>ve and eight we show the average percentage deviation of the cost of the integer-ratio solution from the lower bound for when $P { \sim } U _ { P 1 } , \ P { \sim } U _ { P 2 }$ and $P { \sim } U _ { P 3 }$ , respectively. Similarly, columns three, six and nine contain the maximum percentage deviation of the cost of the integer-ratio solution from the lower bound. Finally, in the rest of columns we show the average number of times that the heuristic needs to use the Lagrangian relaxation to compute a feasible solution (Av. Lag.).

Table 3  
Comparison between integer-ratio and decentralized policie

<table><tr><td rowspan="2">N</td><td colspan="2"> $P \sim {U}_{P1}$ </td><td colspan="2"> $P \sim {U}_{P2}$ </td><td colspan="2"> $P \sim {U}_{P3}$ </td></tr><tr><td> ${C}_{\mathrm{{IR}}} < {C}_{\mathrm{D}}$ </td><td> ${C}_{\mathrm{{IR}}} > {C}_{\mathrm{D}}$ </td><td> ${C}_{\mathrm{{IR}}} < {C}_{\mathrm{D}}$ </td><td> ${C}_{\mathrm{{IR}}} > {C}_{\mathrm{D}}$ </td><td> ${C}_{\mathrm{{IR}}} < {C}_{\mathrm{D}}$ </td><td> ${C}_{\mathrm{{IR}}} > {C}_{\mathrm{D}}$ </td></tr><tr><td>5</td><td>38</td><td>62</td><td>86</td><td>14</td><td>90</td><td>10</td></tr><tr><td>10</td><td>36.9</td><td>63.1</td><td>58</td><td>42</td><td>79</td><td>21</td></tr><tr><td>15</td><td>0</td><td>100</td><td>11.4</td><td>88.6</td><td>45.7</td><td>54.3</td></tr><tr><td>20</td><td>-</td><td>-</td><td>33.3</td><td>66.7</td><td>44.4</td><td>55.6</td></tr></table>

Table 4  
Percentage difference between the costs of the integer-ratio and the decentralized policies

<table><tr><td rowspan="2">N</td><td colspan="2"> $P \sim {U}_{P1}$ </td><td colspan="2"> $P \sim {U}_{P2}$ </td><td colspan="2"> $P \sim {U}_{P3}$ </td></tr><tr><td> $\overline{\text{Gap}}_{\left( {{C}_{D} - {C}_{IR}}\right) }$ </td><td> $\overline{\text{Gap}}_{\left( {{C}_{IR} - {C}_{D}}\right) }$ </td><td> $\overline{\text{Gap}}_{\left( {{C}_{D} - {C}_{IR}}\right) }$ </td><td> $\overline{\text{Gap}}_{\left( {{C}_{IR} - {C}_{D}}\right) }$ </td><td> $\overline{\text{Gap}}_{\left( {{C}_{D} - {C}_{IR}}\right) }$ </td><td> $\overline{\mathrm{{Gap}}}_{\left( {{C}_{IR} - {C}_{D}}\right) }$ </td></tr><tr><td>5</td><td>1.472</td><td>2.627</td><td>3.180</td><td>0.863</td><td>4.035</td><td>0.666</td></tr><tr><td>10</td><td>0.956</td><td>2.454</td><td>1.767</td><td>1.374</td><td>2.153</td><td>0.848</td></tr><tr><td>15</td><td>-</td><td>-</td><td>2.034</td><td>2.450</td><td>1.657</td><td>1.550</td></tr><tr><td>20</td><td>-</td><td>-</td><td>0.985</td><td>0.986</td><td>1.539</td><td>0.067</td></tr><tr><td>Average</td><td>1.214</td><td>2.540</td><td>1.991</td><td>1.418</td><td>2.346</td><td>0.782</td></tr></table>

Table 5  
Sensitivity analysis with respect to $d _ { j }$

<table><tr><td rowspan="2"> $d_j$ </td><td colspan="2"> $P\sim U_{P1}$ </td><td colspan="2"> $P\sim U_{P2}$ </td><td colspan="2"> $P\sim U_{P3}$ </td></tr><tr><td> $C_{\text{IR}}< C_{\text{D}}$ </td><td> $C_{\text{IR}}>C_{\text{D}}$ </td><td> $C_{\text{IR}}< C_{\text{D}}$ </td><td> $C_{\text{IR}}>C_{\text{D}}$ </td><td> $C_{\text{IR}}< C_{\text{D}}$ </td><td> $C_{\text{IR}}>C_{\text{D}}$ </td></tr><tr><td>U[100,500]</td><td>-</td><td>-</td><td>0</td><td>100</td><td>61</td><td>39</td></tr><tr><td>U[1000,5000]</td><td>-</td><td>-</td><td>50</td><td>50</td><td>13</td><td>87</td></tr><tr><td>U[10,000,20,000]</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr></table>

Table 6  
Sensitivity analysis with respect to $k _ { j }$

<table><tr><td rowspan="2"> $k_j$ </td><td colspan="2"> $P \sim U_{P1}$ </td><td colspan="2"> $P \sim U_{P2}$ </td><td colspan="2"> $P \sim U_{P3}$ </td></tr><tr><td> $C_{\text{IR}} < C_{\text{D}}$ </td><td> $C_{\text{IR}} > C_{\text{D}}$ </td><td> $C_{\text{IR}} < C_{\text{D}}$ </td><td> $C_{\text{IR}} > C_{\text{D}}$ </td><td> $C_{\text{IR}} < C_{\text{D}}$ </td><td> $C_{\text{IR}} > C_{\text{D}}$ </td></tr><tr><td>U [100, 500]</td><td>0</td><td>100</td><td>0</td><td>100</td><td>22</td><td>78</td></tr><tr><td>U [1000, 5000]</td><td>0</td><td>100</td><td>0</td><td>100</td><td>0</td><td>100</td></tr><tr><td>U [10,000, 20,000]</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr></table>

Table 7  
Sensitivity analysis with respect to h

<table><tr><td rowspan="2"> $h_j$ </td><td colspan="2"> $P \sim U_{P1}$ </td><td colspan="2"> $P \sim U_{P2}$ </td><td colspan="2"> $P \sim U_{P3}$ </td></tr><tr><td> $C_{\text{IR}} < C_{\text{D}}$ </td><td> $C_{\text{IR}} > C_{\text{D}}$ </td><td> $C_{\text{IR}} < C_{\text{D}}$ </td><td> $C_{\text{IR}} > C_{\text{D}}$ </td><td> $C_{\text{IR}} < C_{\text{D}}$ </td><td> $C_{\text{IR}} > C_{\text{D}}$ </td></tr><tr><td>U [100, 500]</td><td>0</td><td>100</td><td>44</td><td>56</td><td>77</td><td>23</td></tr><tr><td>U [1000, 5000]</td><td>5</td><td>95</td><td>25</td><td>75</td><td>28</td><td>72</td></tr><tr><td>U [10,000, 20,000]</td><td>79</td><td>21</td><td>39</td><td>61</td><td>39</td><td>61</td></tr></table>

Sensitivity analysis with respect to $k _ { 0 }$

<table><tr><td rowspan="2"> $k_0$ </td><td colspan="2"> $P\sim U_{P1}$ </td><td colspan="2"> $P\sim U_{P2}$ </td><td colspan="2"> $P\sim U_{P3}$ </td></tr><tr><td> $C_{\text{IR}}<C_{\text{D}}$ </td><td> $C_{\text{IR}}>C_{\text{D}}$ </td><td> $C_{\text{IR}}<C_{\text{D}}$ </td><td> $C_{\text{IR}}>C_{\text{D}}$ </td><td> $C_{\text{IR}}<C_{\text{D}}$ </td><td> $C_{\text{IR}}>C_{\text{D}}$ </td></tr><tr><td>U[100,500]</td><td>35</td><td>65</td><td>95</td><td>5</td><td>99</td><td>1</td></tr><tr><td>U[1000,5000]</td><td>64</td><td>36</td><td>96</td><td>4</td><td>96</td><td>4</td></tr><tr><td>U[10,000,20,000]</td><td>76</td><td>24</td><td>97</td><td>3</td><td>98</td><td>2</td></tr></table>

Sensitivity analysis with respect to $h _ { 0 }$ and $h _ { j }$

<table><tr><td rowspan="2"> $h_0$ </td><td rowspan="2"> $h_j$ </td><td colspan="2"> $P \sim U_{P1}$ </td><td colspan="2"> $P \sim U_{P2}$ </td><td colspan="2"> $P \sim U_{P3}$ </td></tr><tr><td> $C_{\text{IR}} < C_{\text{D}}$ </td><td> $C_{\text{IR}} > C_{\text{D}}$ </td><td> $C_{\text{IR}} < C_{\text{D}}$ </td><td> $C_{\text{IR}} > C_{\text{D}}$ </td><td> $C_{\text{IR}} < C_{\text{D}}$ </td><td> $C_{\text{IR}} > C_{\text{D}}$ </td></tr><tr><td>U[100,500]</td><td>U[100+h0,500+h0]</td><td>0</td><td>100</td><td>58</td><td>42</td><td>85</td><td>15</td></tr><tr><td>U[1000,5000]</td><td>U[100+h0,5000+h0]</td><td>14</td><td>86</td><td>60</td><td>40</td><td>87</td><td>13</td></tr><tr><td>U[10,000,20,000]</td><td>U[100+h0,20000+h0]</td><td>0</td><td>100</td><td>62</td><td>38</td><td>91</td><td>9</td></tr></table>

From Table 2, we can see that the average percentage deviation of the integer-ratio solution from the lower bound for all problem sets is lower than 1.6%. Moreover, the maximum percentage deviation obtained is lower than 5.5%. From these results, we can conclude that the heuristic provides good integer-ratio policies in comparison with the lower bound. In addition, the average number of times that the heuristic needs to use the Lagrangian relaxation to compute a feasible solution is smaller than 6. It is worth noting that only when $P { \sim } U _ { P 1 }$ and $N { > } 1 0$ the number of times that the Lagrangian relaxation is required increases.

## 7.2. Integer-ratio policies vs. decentralized policies

Below we compare the integer-ratio policies with those obtained by using the decentralized approach. Let $C _ { \mathrm { D } }$ denote the cost of the policy computed by the procedure to obtain decentralized policies. Then, for each problem set we report in Table 3 the percentage of instances where the integer-ratio heuristic provides both better and worse policies than the decentralized procedure, respectively.

The results in Table 3 show that as the number of buyers increases so does the percentage of instances where the decentralized policy is better. On the other hand, another parameter which has a signi<sup>fi</sup>cant effect is the production rate at the vendor. When the production rate is selected from $U _ { P 1 } ,$ in most cases it is preferable to follow the decentralized strategy instead of the integer-ratio policy. However, when the production rate is taken from either $U _ { P 2 }$ or $U _ { P 3 } ,$ , only when the number of buyers is greater than 10, the decentralized procedure provides better policies than those given by the integer-ratio heuristic. In our opinion, this is due to the fact that as the production rate for the vendor increases, the coordination of the orders for all buyers becomes easier. Therefore, the integerratio policies can be more effective than the decentralized ones.

It is worth noting that for some problem sets there are instances for which one of the procedures cannot generate a feasible solution. Moreover, there are problem sets which yield infeasible solutions for all their instances, mainly when $P \sim U _ { P 1 } .$ The reason is that the production rate is not high enough to satisfy all the buyers at the beginning of the cycle. However, in most cases the infeasibility occurs for the decentralized case. Remark that in the integer-ratio policies, the replenishment intervals at the warehouse and at the retailers are computed in a centralized manner, that ${ \mathrm { i } } s ,$ all the locations are simultaneously taken into account. In contrast, in the decentralized case, the retailers independently compute their replenishment plans, and then the warehouse should determine the best policy to satisfy its demand vector. That is, the retailers determine their optimal order plans regardless of the production capacity at the warehouse. Therefore, in this case, the warehouse probably cannot satisfy the demand at speci<sup>fi</sup>c time instants.

We also evaluate the difference between both costs, $C _ { \mathrm { I R } }$ and $C _ { \mathrm { D } } .$ Accordingly, in case of $C _ { \mathrm { I R } } { > } C _ { \mathrm { D } }$ we compute $\mathrm { G a p } _ { ( C _ { \mathrm { l R } } - C _ { \mathrm { D } } ) } =$ $( C _ { \mathrm { I R } }  – C _ { \mathrm { D } } ) / C _ { \mathrm { D } } \times$ 100 Otherwise, if $C _ { \mathrm { D } } \geq C _ { \mathrm { I R } }$ <sup>ð Þ</sup>, we calculate $\mathrm { G a p } _ { ( C _ { \mathrm { D } } - C _ { \mathrm { I R } } ) } = ( C _ { \mathrm { D } } { - } C _ { \mathrm { I R } } ) / C _ { \mathrm { I R } } \ \times$ 100: For each problem set the ave-<sup>ð Þ</sup>rage percentages $\mathsf { G a p } _ { ( C _ { \mathrm { l R } } - C _ { \mathrm { D } } ) }$ and $\overline { { \mathrm { G a p } } } _ { ( C _ { \mathrm { D } } - C _ { \mathrm { I R } } ) }$ are presented in <sup>ð Þ ð Þ</sup>Table 4. The following conclusions can be extracted from Table 4.

When the production rate is selected from $U _ { P 1 }$ and $C _ { \mathrm { D } } 2 C _ { \mathrm { I R } } ,$ the average value of $\overline { { \mathbf { G a p } } } _ { ( C _ { \mathrm { D } } - C _ { \mathrm { I R } } ) }$ is equal to 1.214. However, when $C _ { \mathrm { D } } { < } C _ { \mathrm { I R } } ,$ <sup>ð Þ</sup>the average value of $\overline { { \mathbf { G a p } } } _ { ( C _ { \mathrm { I R } } - C _ { \mathrm { D } } ) }$ increases to $2 . 5 4 0$ <sup>ð Þ</sup>. Therefore, under this situation when decentralized strategies provide better schedules than the corresponding integer-ratio policies, the difference between the costs is approximately twice as large as the opposite case. In contrast, when the production rate is taken from either U<sub>P2</sub> or $U _ { P 3 }$ the value of $\overline { { \mathrm { G a p } } } _ { ( C _ { \mathrm { I R } } - C _ { \mathrm { D } } ) }$ is generally tighter than the value of $\overline { { { \mathrm { G a p } } } } _ { ( C _ { \mathrm { D } } - C _ { \mathrm { l R } } ) } ,$ <sup>ð Þ</sup>: This difference is even more remarkable when <sup>ð Þ</sup>N≤10. This yields the integer-ratio policies to be a good compromise solution when $P { \sim } U _ { P 2 }$ or $P { \sim } U _ { P 3 }$

It is worth noting that results in Tables 2 and 4 suggest that the cost of the decentralized strategies is occasionally below the lower bound for the integer-ratio policies. Recall that [19] proves that under in<sup>fi</sup>nite production rate the lower bound for the class of integer-ratio policies is also a lower bound on the average cost of any feasible solution for the problem. However, this assertion cannot be extended to the case with <sup>fi</sup>nite production rate.

## 7.3. Sensitivity analysis

We have carried out a sensitivity analysis involving parameters $h _ { 0 } , k _ { 0 } , k _ { j } , d _ { j } ,$ and $h _ { j }$ to assess their impact on our results. The number of buyers has been <sup>fi</sup>xed to 10 and we have varied the ranges of the uniform distributions from which we select the above parameters. Speci<sup>fi</sup>cally, we have analyzed 45 new problem sets. Some of the new problem sets are obtained by varying only the uniform distributions for one of the following parameters: $d _ { j } , k _ { j } , h _ { j }$ and $k _ { 0 } ,$ while the rest of parameters are selected from their initial distributions. In other problem sets we vary the uniform distributions for both $h _ { 0 }$ and $h _ { j } .$ For each new problem set we generate 100 instances and the results are summarized in Tables 5–8.

In Table $5 ,$ if $P { \sim } U _ { P 1 }$ there are always instances where at least one of the procedures provides infeasible solutions, with independence of the value of the demand. When $P { \sim } U _ { P 2 }$ and $P \sim U _ { P 3 } ,$ we can conclude that as the quotient $\frac { D } { P }$ decreases, namely, when the production rate is signi<sup>fi</sup>cantly greater than the total demand, the percentage of instances where the integer-ratio policies are better than the decentralized strategies increases. Regarding parameters $k _ { j }$ and $h _ { j }$ we can conclude from Tables 6 and 7 that if the replenishment or holding costs at the buyers increase, then, in most instances, it is preferable that the buyers make decisions independently.

It is important to remark that the integrated models reduce the costs for the vendor, but increase the costs for the buyers. Thus, if the replenishment and holding costs at the buyers increase considerably, then the total cost at the buyers increases in an amount that is greater than that in which the cost at the vendor is reduced. Hence, under this situation it is better to follow a decentralized policy. In contrast, the results in Table 8 show that if the setup cost at the vendor increases then the integer-ratio policies are better than those provided by the decentralized procedure, mainly when $P { \sim } U _ { P 2 } \thinspace 0 \Gamma P { \sim } U _ { P 3 } .$

Finally, as it can be seen in Table 9, if we simultaneously vary $h _ { 0 }$ and $h _ { j }$ the results are very similar to those shown in Table $3 .$

## 8. Conclusions and <sup>fi</sup>nal remarks

We address the single-vendor multi-buyer system in which the vendor supplies an item to several buyers at a <sup>fi</sup>nite production rate. Besides, it is assumed that customer demand occurs at each buyer at a constant rate. Previous works mostly focused on the single-vendor single-buyer problem or on the single-vendor multi-buyer system in which the vendor supplies a different item to each buyer. In this paper, we assume that the buyers order the same item from the vendor. Moreover, we allow the replenishment interval at any buyer to be greater than the replenishment interval at the vendor.

We develop the formulation of the problem in terms of integer-ratio policies and we propose a heuristic procedure. Additionally, we also show how the problem should be handled if the vendor and the buyers were considered as independent installations. In this case we propose an algorithm which assumes that the vendor behaves as an inventory system with time-varying demand.

We have implemented both procedures and the computational results show that either the integer-ratio policies or the decentralized policies can be effective strategies, that is, no policy dominates the other.

We have carried out a sensitivity analysis to analyze the effect of the different parameters of the problem on the total cost for both strategies. The results suggest that as either the quotient <sup>D</sup> decreases or the setup cost at the vendor increases the integer-ratio policies are more effective than the decentralized policies. In contrast, as the replenishment or the holding costs at the buyers increase so does the percentage of instances where it is preferable to apply a decentralized policy.

In conclusion, depending on the parameter values we should choose the solution approach for solving the problem. Nevertheless, in most cases it is recommendable to apply integer-ratio policies since the gap in the instances where the decentralized strategies dominate the integer-ratio policies is tighter than the gap in the reverse case.

It is also important to remark that optimal policies for this problem are generally very complex and hence they could become unattractive even when they are ef<sup>fi</sup>ciently computed. Consequently, we have focused our attention on the integerratio policies due to its signi<sup>fi</sup>cant practical importance, which can be successfully implemented without excessive computation. This latter aspect is mainly important and attractive for small and medium size companies that generally prefer to schedule their operations by using simple replenishment rules

This paper provides some insights into the possible strategies that could be analyzed when more general assumptions are considered. Concretely, we are interested in extending the model to include assumptions such as timevarying demand, delivery constraint on the maximum quantity which can be shipped at any time, storage constraint on the buyers or production rates at each buyer.

## Acknowledgments

We would like to thank the anonymous referees for their valuable comments and suggestions. This work is partially supported by Spanish Ministry of Education and Science, Research Projects MTM2004-07550 and MTM2007-60928, from National Plan of Scienti<sup>fi</sup>c Research, Technological Development and Innovation.

## Appendix A

In this Appendix we present a sketch of the Lagrangian relaxation which is used in Section 4 to minimize the total cost (4) subject to Eq. (9). Let $\mu _ { 1 } , \mu _ { 2 } , . . . , \mu _ { N }$ be the Lagrange multipliers associated with the constraints in $\operatorname { E q . } ( 9 )$ . Then the Lagrangian function can be written as

$$
L (t _ {0}, \dots , t _ {N}, \overline {{\mu}}) = C _ {\mathrm{T}} (t _ {0}, \dots , t _ {N}) + \overline {{\mu}} A \overline {{t}} ^ {\prime}
$$

where

$$
A = \left( \begin{array}{c c c c} d _ {1} - P & d _ {2} & .. & d _ {N} \\ d _ {1} & d _ {2} - P & .. & d _ {N} \\ . & . & . & . \\ . & . & . & . \\ d _ {1} & d _ {2} & .. & d _ {N} - P \end{array} \right), \quad \overline {{\mu}} = (\mu_ {1}, \mu_ {2}, \dots , \mu_ {N}) \text {   and   }
$$

$$
\bar {t} = (t _ {1}, t _ {2}, \ldots , t _ {N}).
$$

It is important to note that at each iteration of the heuristic we isolate one value $t _ { i } , i = 0 , 1 , \ldots N - 1$ , in terms of other value $t _ { j } .$ Taking this into account, the set of constraints in Eq. (9) changes at each iteration, and so, A has to be updated.

Now, the dual problem can be expressed as follow

$$
\max _ {\overline {{\mu}}} \theta (\overline {{\mu}})
$$

where $\theta ( \bar { \mu } )$ =min $L ( t _ { 0 } , . . . , t _ { N } , \bar { \mu } ) .$

In order to solve it, we will apply a standard subgradient method. Accordingly, we need to compute an upper bound UB. In this case UB is obtained by solving the problem assuming that all the buyers use the same replenishment interval, that is, $t _ { j } = t , j \in \{ 1 , . . . , N \}$ , and also that $t _ { 0 } = n t ,$ , with n a positive integer. Under this situation, the cost function is reduced to

$$
C _ {T} = \frac {k _ {0}}{t _ {0}} + \frac {t _ {0} h _ {0} D}{2} \left(1 - \frac {D}{P}\right) + \frac {1}{t} \sum_ {j = 1} ^ {N} k _ {j} + \frac {t}{2} \sum_ {j = 1} ^ {N} d _ {j} (h _ {j} - h _ {0}) + \frac {2 h _ {0}}{P} D ^ {2}
$$

where $\begin{array} { r } { D = \sum _ { j = 1 } ^ { N } d _ { j } . } \end{array}$

<sup>¼ ¼</sup>Besides, it is easy to see that $\textstyle \sum _ { j = 1 } ^ { N } d _ { j } t _ { j } / P \le t _ { i } , i \in \{ 1 , \dotsc , N \}$ is equivalent to consider $D { \leq } P .$

Therefore, the optimal $t _ { 0 }$ is given by

$$
t _ {0} = \left[ \frac {2 k _ {0}}{h _ {0} D \left(1 - \frac {D}{P}\right)} \right] ^ {1 / 2}
$$

and the optimal t is computed as follows

$$
t = \left[ \frac {2 \sum_ {j = 1} ^ {N} k _ {j}}{\sum_ {j = 1} ^ {N} d _ {j} \left(h _ {j} - h _ {0}\right) + \frac {2 h _ {0}}{P} D ^ {2}} \right] ^ {1 / 2}.
$$

Now, we can determine the optimal real value n as $n =$ $t _ { 0 } / t ,$ ; and taking into account that $t = t _ { 0 } / n$ <sup>¼</sup>the cost function <sup>¼</sup>can be formulated by the following expression

$$
C _ {T} = \frac {k _ {0} + n \sum_ {j = 1} ^ {N} k _ {j}}{t _ {0}} + \frac {t _ {0}}{2} \left[ h _ {0} D \left(1 - \frac {D}{P}\right) + \frac {1}{n} \left(\sum_ {j = 1} ^ {N} d _ {j} (h _ {j} - h _ {0}) + \frac {2 h _ {0}}{P} D ^ {2}\right) \right]
$$

Taking the derivative of $C _ { \mathrm { T } }$ with respect to $t _ { 0 }$ and setting it equal to zero we obtain that

$$
t _ {0} = \left[ \frac {2 \left(k _ {0} + n \sum_ {j = 1} ^ {N} k _ {j}\right)}{h _ {0} D (1 - \frac {D}{P}) + \frac {1}{n} \left(\sum_ {j = 1} ^ {N} d _ {j} (h _ {j} - h _ {0}) + \frac {2 h _ {0}}{P} D ^ {2}\right)} \right] ^ {1 / 2}
$$

and then, we can reformulate the cost function to give

$$
C _ {\mathrm{T}} (n) = \sqrt {2 \left(k _ {0} + n \sum_ {j = 1} ^ {N} k _ {j}\right) \left[ h _ {0} D \left(1 - \frac {D}{P}\right) + \frac {1}{n} \left(\sum_ {j = 1} ^ {N} d _ {j} \left(h _ {j} - h _ {0}\right) + \frac {2 h _ {0}}{P} D ^ {2}\right) \right]}
$$

At this point, we compute $C _ { \mathrm { T } } \ ( n { = } \lfloor n \rfloor )$ and $C _ { \mathrm { T } } \ ( n { = } \lceil n \rceil )$ . If $C _ { \mathrm { T } } ( n { = } \lfloor n \rfloor ) { < } C _ { \mathrm { T } } \left( n { = } \lceil n \rceil \right)$ ) we set $n ^ { * } { = } \lfloor r$ ⌋ and $\mathrm { U B } _ { 0 } { = } C _ { \mathrm { T } } ( n { = } \lfloor n \rfloor ) .$ . Otherwise, we set $n ^ { * } { = } \lceil n \rceil$ and $\mathrm { U B } _ { 0 } { = } C _ { \mathrm { T } } \left( n { = } [ n ] \right)$ . If nb1 we set $n ^ { * } { = } 1 .$

In addition to the upper bound, we also have to choose an initial multiplier vector, ${ \bar { \mu } } _ { 0 } ,$ and determine the step size, θ. In particular, we set $\bar { \mu } _ { 0 }$ equal to the zero vector and the step size at iteration j is given by the following expression

$$
\theta_ {j} = \frac {\lambda_ {j} \mathrm{UB} _ {j} - L (\overline {{\mu}} _ {j})}{\| \overline {{\mu}} _ {j + 1} - \overline {{\mu}} _ {j} \| ^ {2}}
$$

where $\lambda _ { j }$ is a scalar which initially is set to 2. Then, it is reduced by a factor of 2 whenever the best Lagrangian objective function value found so far has failed to increase in three iterations. A scheme of the subgradient method is given in Algorithm 2.

## Algorithm 2. Subgradient method

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Initialization
Consider an initial upper bound  $UB_{0}$ 
Fix an initial multiplier vector  $\bar{\mu}_{0}\geq0$ 
Set an initial factor  $\lambda_{0}\leftarrow2$ 
for j=0, 1,..., do
    $\theta_{j}=\frac{\lambda_{j}\mathrm{UB}_{j}-L(\bar{\mu}_{j})}{\|\bar{\mu}_{j+1}-\bar{\mu}_{j}\|^{2}}\{\text{step size}\}$ $\bar{\mu}_{j+1}=\max\{0,\bar{\mu}_{j}+\theta_{j}At\}$ 
    if  $\|\bar{\mu}_{j+1}-\bar{\mu}_{j}\|&lt;\varepsilon$  then
    Stop
    end if
    if No improvements in more than three iterations then
    $\lambda_{j+1}=\lambda_{j}/2$ 
    end if
    $j\leftarrow j+1$ 
end for
</div>

## References

[1] B. Abdul-Jalbar, J. Gutiérrez, J. Puerto, J. Sicilia, Policies for inventory/ distribution systems: the effect of centralization vs. decentralization International Journal of Production Economics 81–82 (2003) 281–293.

[2] B. Abdul-Jalbar, J. Gutiérrez, J. Sicilia, Integer-ratio policies for distribution/inventory systems, International Journal of Production Economics 93–94 (2005) 407–415.

[3] B. Abdul-Jalbar, J. Gutiérrez, J. Sicilia, An integrated inventory model for the single- vendor two-buyer problem, International Journal of Production Economics 108 (1-2) (2007) 246–258

[4] A. Aggarwal, J.K. Park, Improved algorithms for economic lot size problems, Operations Research 41 (3) (1993) 549–571

[5] A. Banerjee, A joint economic lot size model for purchaser and vendor, Decision Sciences 17 (1986) 292–311.

[6] A. Federgruen, M. Tzur, A simple forward algorithm to solve general dynamic lot sizing models with n periods in O(n log n) or O(n), Management Science 37 (8) (1991) 909–925.

[7] S.K. Goyal, An integrated inventory model for a single supplier-single customer problem, International Journal of Production Research 15 (1) (1976) 107–111.

[8] S.K. Goyal, Joint economic lot size model for purchaser and vendor: a comment, Decision Sciences 19 (1988) 236–241.

[9] S.K. Goyal, A one-vendor multi-buyer integrated inventory model: a comment, European Journal of Operational Research 82 (1995) 209–210.

[10] S.K. Goyal, On improving the single-vendor single-buyer integrated production inventory model with a generalized policy, European Journal of Operational Research 125 (2) (2000) 429–430.

[11] S.K. Goyal, Y.P. Gupta, Integrated inventory models: the vendor–buyer coordination, European Journal of Operational Research 41 (1989) 261–269.

[12] S.K. Goyal, F. Nebebe, Determination of economic production–shipment policy for a single-vendor–single-buyer system, European Journal of Operational Research 121 (1) (2000) 175–178.

[13] S.C. Graves, L.B. Schwarz, Single cycle continuous review policies for arborescent production / inventory systems, Management Science 23 (1977) 529–540.

[14] R.M. Hill, The single-vendor single-buyer integrated production inventory model with a generalized policy, European Journal of Operational Research 97 (1997) 493–499.

[15] R.M. Hill, Note: dynamic lot sizing for a <sup>fi</sup>nite rate input process, Naval Research Logistics 44 (1997) 221–228.

[16] R.M. Hill, The optimal production and shipment policy for the singlevendor single-buyer integrated production–inventory problem, Inter national Journal of Production Research 37 (1999) 2463–2475

[17] M. Khouja, Optimizing inventory decisions in a multi-stage multicustomer supply chain, Transportation Research Part E: Logistics and Transportation Review 39 (3) (2003) 193–208.

[18] L. Lu, A one-vendor multi-buyer integrated inventory model, European Journal of Operational Research 81 (1995) 312–323.

[19] R.O. Roundy, 98% Effective integer-ratio lot sizing for one-warehouse multi-retailer systems, Management Science 31 (11) (1985) 1416–1430.

[20] L.B. Schwarz, A simple continuous review deterministic one-warehouse N-retailer inventory problem, Management Science 19 (1973) 555–566

[21] S. Viswanathan, Optimal strategy for the integrated vendor–buyer inventory model, European Journal of Operational Research 105 (1998) 38–42

[22] P. Van der Vlist, K. Roelof, R.K. Bas Verheijen, Note on supply chain integration in vendor-managed inventory, Decision Support Systems 44 (1) (2007) 360–365.

[23] A. Wagelmans, S. Van Hoesel, A. Kolen, Economic lot sizing: an O(nlogn) algorithm that runs in linear time in the Wagner–Whitin case, Management Science 40 (1992) 145–156.

[24] H. Wagner, T.M. Whitin, Dynamic version of the economic lot size model, Management Science 5 (1958) 89–96.

[25] H.M. Wee, P.C. Yang, The optimal and heuristic solutions of a distribution network, European Journal of Operational Research 158 (2004) 626–632.

[26] J.F. Williams, Heuristic techniques for simultaneous scheduling of production and distribution in multi-echelon structures: theory and empirical comparisons, Management Science 27 (1981) 336–352.

[27] J.F. Williams, A hybrid algorithm for simultaneous scheduling of production and distribution in multi-echelon structures, Management Science 29 (1983) 77-105

[28] M. Yao, C. Chiou, On a replenishment coordination model in an integrated supply chain with one vendor and multiple buyers, European Journal of Operational Research 159 (2) (2003) 406419.

[29] Y. Yao, P.T. Evers, M.E. Dresner, Supply chain integration in vendormanaged inventory, Decision Support Systems 43 (2) (2007) 663–674.

[30] Y. Yao, P.T. Evers, M.E. Dresner, Response to Note on supply chain integration in vendor managed inventory, Decision Support Systems 44 (1) (2007) 366–367.

![](/api/attachments/AFXNQRAJ/fulltext/images/e2d91d24d3fc23b80afc7a0312e7bc1894b5dc7ce7850909274f8d8edb570783.jpg)  
Beatriz Abdul-Jalbar is Assistant Professor of Statistics and Operations Research at the University of La Laguna, Spain. She received her Mathematics degree and her Statistical Sciences and Techniques degree from the University of La Laguna. She has a PhD in Mathematics from the University of La Laguna, Her main research interests lie in the area of supply chain management and inventory control.

![](/api/attachments/AFXNQRAJ/fulltext/images/fb6d77707024d3846edbfb0a838050ffbe2527bc4e81ca2cfccf0c424c04c88b.jpg)  
José M. Gutiérrez is Associate Professor of Operations Research at the University of La Laguna. He received his BS in Computer Science from the University of Las Palmas de G.C. and his PhD in Mathematics (European Doctorate mention) from the University of La Laguna (Tenerife-Spain). His main research interests lie in the area of supply chain management and inventory control.

![](/api/attachments/AFXNQRAJ/fulltext/images/72d36d6337502c0cf785e6bc93bd52bc56bc655f3a4a2579ad824f53bc45dbe8.jpg)

Joaquín Sicilia is Professor of Operations Research at the University of La Laguna (Tenerife, Spain). He received a B.S. from the Complutense University of Madrid (Spain) and a Ph.D in Mathematics from the University of La Laguna. He has published over thirty articles in several Operations Research journals (Omega, European Journal of Operational Research, Journal of Operational Res. Society, Computers and Operations Research, Applied Mathematics and Computation, Journal Optimization Theory and Applications, Annals of Operations Research, Optimization, Applied Mathematical

Modeling, Computational Optimization and Applications, International Journal of Production Economics, Asia-Paci<sup>fi</sup>c Journal of Operationa Research,...). His current research interest is in Inventory Control, Production Planning, Scheduling Theory and Location Theory.
