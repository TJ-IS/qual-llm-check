---
otero_id: 7396
otero_key: "3DJUTZEE"
title: "A pragmatic stochastic decision model for supporting goods trans-shipments in a supply chain environment"
authors: "H.C.W. Lau; Dilupa Nakandala"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.04.012"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A pragmatic stochastic decision model for supporting goods trans-shipments in a supply chain environment

H.C.W. Lau ⁎, Dilupa Nakandala

Centre for Industry and Innovation Studies Research Group, School of Business, University of Western Sydney, Locked Bag 1797, Penrith South DC, New South Wales 2751, Australi

## a r t i c l e i n f o

Article history: Received 15 June 2011 Received in revised form 27 March 2012 Accepted 29 April 2012 Available online 7 May 2012

Keywords: Lateral trans-shipments Stochastic demand Wholesaler operations Inventory replenishment

## a b s t r a c t

This paper develops a set of decision rules to assist wholesalers to decide whether it is more cost effective to trans-ship urgent outstanding retailer orders from other wholesalers, very fast but at a higher purchase cost, or to order from their suppliers. By considering the uncertainty in demand, it models the total cost encountered by wholesalers, including purchasing, backordering and holding costs in the inventory replenishment process. Unlike previous models that are complex, highly mathematical and dif<sup>fi</sup>cult to apply, this model provides a pragmatic and less complex method adoptable by ordinary logistics managers and requires input data that are accessible from the previous transaction records of an organization. The application of the proposed decision rules are illustrated considering different scenarios of wholesaler–supplier combinations.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Ever increasing market competition forces wholesalers to be ever cost conscious and responsive to the changing needs of the market. A consequence is that wholesalers maintain a low inventory for the purpose of buffering in order to minimize the possible costs. However, the criticality of losing the sales due to stock outages with consequent possible lost pro<sup>fi</sup>t and decreased customer satisfaction are no less important. To manage these potentials, wholesalers adopt a mix of urgent order lateral trans-shipments from other wholesalers at a higher cost, while at the same time backordering from their usual suppliers to meet the continuing stochastic retailer demands — this produces <sup>fl</sup>exibility in the inventory system. Rules that assist wholesalers' decision making processes have practical importance for inventory management.

Supply chain management concepts that streamline the <sup>fl</sup>ow of goods have been the focus of research for a considerable time. Previous research into wholesaler inventory management has presented complex criteria drawn from diverse information sources that are problematic to adopt in real-world practice. There remains a need for simpler and more readily applicable rules for lateral transshipment decisions. In a multi-location setting under a continuous review (R,Q) ordering policy Axsäter [3] considers a decision rule for determining how many units should be trans-shipped, depending on the complete state of the system. The decision is optimal and can be repeatedly used as a heuristic. He puts a signi<sup>fi</sup>cant focus on future cost difference for a certain initial state and the highly mathematical analysis and probability assumptions may not be easily understood by ordinary managers. The models proposed by Evers [9] and Minner et al. [18] consider the case of lost sales rather than backordering under (R,Q) policies. Olsson [21] has considered an optimal (R,Q) ordering policy under complete pooling but due to the problem complexities the optimal solution is restricted to systems with only two locations. Chiu and Huang [6] considered a system with more than two echelons. However, they then restricted focus to a single location of each echelon. Our study considering a multi-location setting, develops decision rules for reactive lateral trans-shipments of urgent demands that cannot be satis<sup>fi</sup>ed from the stock on hand. The decision rules for determining whether it is more cost effective to trans-ship urgent orders or to backorder all outstanding orders from suppliers, the size of trans‐shipment, the favorite wholesaler and the favorite supplier. Our approach handles the cost difference issue raised above using an alternative approach mainly based on predicted holding and backorder costs in different time periods. We <sup>fi</sup>nd that the total cost function against the number of units trans-shipped has a linear relationship and presents a close estimation re<sup>fl</sup>ecting the cost variations, in real case, it is not a completely linear relation though. This new approach does not undervalue previous scholarly work, it builds on it by proposing a more pragmatic decision model for supply chain environment in wholesaler system. The model can be applied to a real context with multiple wholesalers, and multiple suppliers with variable lead times. It is less complex in calculations and the data requirement that can be ful<sup>fi</sup>lled with previous transaction records data of the organization enables adoption of this model by an ordinary manager. The proposed approach is validated through the illustration of a practical application of the model in different scenarios.

The next section reviews the relevant literature, Section 3 then goes on to describe and develop the proposed mathematical model for total costs, including purchasing costs, backordering costs and holding costs that are encountered in inventory replenishment by wholesalers and develops the decision rules for trans-shipments. Section 4 shows how these decision rules could be applied in practice and implications for management. Section 5 concludes with a discussion of the effectiveness and limitations of the decision model, with suggestions for further research.

## 2. Literature review

Thomas and Grif<sup>fi</sup>n [25] reviewed the literature addressing coordinated planning between two or more stages of the supply chain, placing particular emphasis on models that would lend themselves to a total supply chain model. Even if a given supply chain network is under a single ownership and centralized control, the integrative view of supply chain management obligates its managers to solve multiple stage inventory problems of a scale for which researchers have yet to identify consistently ef<sup>fi</sup>cient solution procedures [7,8]. While Köchel et al. [13] stressed the importance of organizing shipments of resource units between the nodes of the logistics network; Weber [26] provided complementarity and substitutability in the shipment related problem. Burton and Banerjee [5] examined the cost effects of two lateral trans-shipment approaches in a twoechelon supply chain network and discovered that a lateral shipment approach was considerably superior to a policy of no such shipments, albeit at the expense of increased transportation activity. Minner and Silver [17] evaluated two simple extreme trans-shipment strategies and developed an analytical approach for estimating the approximate total expected costs. The majority of research papers that deal with goods replenishment issues assume a decision rule is applied when asking for a shipment from other wholesalers [7,14,19].

In organizations, high quality information that is accurate, timely, complete, and consistent and supported by the appropriate analytic tools is critical for managerial decision making [16]. For example, information technology has a signi<sup>fi</sup>cant role to play and appropriate evaluation and decision tools need to be provided for decisions on ef-<sup>fi</sup>cient product development. Taking into account the trend of customer demands and supply of goods for production purpose. Xu et al. [27] proposed a decision model to support product design and indicated the importance of a reliable forecast related to future demands in determining the design criteria. The data repositories, data warehousing and enterprise resource planning implementations improve the potential of decision support capabilities and decision support bene<sup>fi</sup>ts [11]. In an enterprise value chain that comprises suppliers and customers, integrated information systems are required among the partners in order to deal with the market demand in a responsive way. The importance of a responsive decision model is that it is able to forecast the expected cost of the goods covering inventory and backorder cost [22]. Kimbrough, Wu and Zhong [12] investigated the deployment of arti<sup>fi</sup>cial agents to manage the <sup>fl</sup>ow of goods across the supply chain, minimizing bull-whip effect which can be detrimental to the ef<sup>fi</sup>ciency in performance of the whole logistics systems. However, it is mainly based on deterministic demand and <sup>fi</sup>xed lead-time and the stochastic phenomenon has been less considered. Reliable information sharing and information quality play an important role in securing performance and achieving total lowest cost in the entire network [15]. Ef<sup>fi</sup>cient and real-time information sharing can enhance the development of a responsive decision support model and decision models based on mathematical calculations have the potential to support managers in making critical decisions. This paper considered the impact of uncertainty in logistics systems and develops a decision support model for wholesale inventory man agers in making lateral trans-shipment decisions in a pragmatically easy method.

Archibald et al. [1] proposed using a stochastic dynamic program to optimize the decision of whether to laterally trans-ship. A simulation with a heuristics approach was evaluated by Tagaras and Cohen [24]. According to Axsäter [2], when a wholesaler cannot supply goods to a retailer, lateral trans-shipment can take place and he proposed a method for optimizing the control policy of inventory replenishment. His model developed decision rules for lateral transshipments, aiming to evolve an integrated approach for supporting decisions regarding trans-shipment of goods. The underlying concept of the proposed decision rule by Axsäter ([3]: 1174) is dif<sup>fi</sup>cult to visualize and adopt practically.

Numerical investigations for small networks show that the rule substantially outperforms the no pooling and complete pooling policies. We have looked at other similar models such as those models considered by Evers [9] and Minner et al. [19] but they examine the case of lost sales. Evers [9] restricts his analysis to two locations only and Minner et al. [19] propose a more <sup>fl</sup>exible heuristic for a multi-location setting, but assume that demand has to be satis<sup>fi</sup>ed only just before the new replenishment order arrives. For (R,Q) ordering policies it is often dif<sup>fi</sup>cult to optimize both ordering parameters and the trans-shipment policy. Also, the method is found to be conservative in its results. Considering an optimal (R,Q) ordering policy under complete pooling Olsson [21] analyzed the steady state nature of the system by assuming that the lead time for an order to arrive is exponentially distributed. However, due to the problem complexities the optimal solution is restricted to systems with only two locations. Chiu and Huang [6] considers a system with more than two echelons but they then restrict focus to a single location of each echelon and assume that unmet demand can be satis<sup>fi</sup>ed through trans-shipments if required. Grahovac and Chakravarty [10] propose the base stock level for the replenishments and created the K threshold for triggering trans-shipment requests. When the inventory level of a retailer drops below K, they <sup>fi</sup>rst try to receive an emergency order with a shorter lead time from the upper echelon, and only use a lateral trans-shipment if this is not possible. However, evaluation of this K threshold approach shows that it is not that reliable and depends largely on whether they are identical and nonidentical retailers.

In summary, the extant literature has to some extent dealt with inventory replenishment policies and decisions for wholesaler operations, however, there are limitations that hinder the application of most of them. Consequently, wholesaler inventory managers still use ad hoc methods to make decisions and there is still a need for a practical decision support system to support effective and informed decisions. This paper studies the sourcing decisions of a wholesaler in ful<sup>fi</sup>lling retailer demand and provides a pragmatic approach deriving simple decision rules that are conveniently adoptable by wholesaler inventory management.

## 3. Model development

When a wholesaler maintains a limited inventory in order to be cost competitive, it constantly needs to externally source to ful<sup>fi</sup>ll retailer demand and avoid inventory shortage. We consider a context where there are a <sup>fi</sup>nite number of wholesalers operating autonomously in a local region. Following Axsäter [4], we assume that the retailer demand from these wholesalers follows a Compound Poisson distribution. The wholesalers usually replenish their stocks from suppliers, requiring a lead time in order to supply the goods. They may also opt to purchase laterally from other wholesalers in the same cost center which, for the purpose of the model, we assume, due to their close proximity, will provide an instant supply of goods. Such transactions among wholesalers are called lateral trans-shipments and they are more expensive than the usual supplier's prices.

We assume that all wholesalers apply a periodic review policy described by Rosenshine and Obee [23] to replenish from external suppliers. To formulate the periodic review policy, we review the unsatis<sup>fi</sup>ed demands in the previous period, the inventory position, and the expected demand in the current period, and then make the order at the beginning of this period. Unsatis<sup>fi</sup>ed demands or surplus orders in this period will be regarded as initial demands or will be added to the inventory position of the next period. If the wholesaler does not employ a (R,Q) review policy, its inventory position could be lower than R of (R,Q) policy or even close to zero, which can decrease the holding costs of the wholesaler. However, the wholesaler that uses a periodic policy has the possibility that its inventory position may be lower than zero. This potentially increases the backorder cost. One possible solution is to make trans-shipment from other wholesalers so as to make the inventory position of the wholesaler non-negative as soon as possible.

We de<sup>fi</sup>ne the following notation used in the model development.

$W _ { i }$ the ith wholesaler,

$N _ { i }$ the total number of suppliers to the wholesaler $W _ { i } ,$

$S _ { i j }$ the jth supplier of the wholesaler $W _ { i } ,$

$p _ { i j }$ the unit selling price by $S _ { i j }$ to $W _ { i } ,$

$q _ { i k }$ the unit intra-shipment cost for $W _ { i }$ to intraship from $W _ { k } ,$ $b _ { i }$ unit back-order cost at $W _ { i }$ per unit time,

$h _ { i }$ unit holding cost for $W _ { i }$ per unit time,

$t _ { 0 }$ start of the scheduling period, $t = 0 ,$

$g _ { i j } ( t )$ delivery lead time probability mass function of $S _ { i j } ,$ $L _ { i j }$ lead time of $S _ { i j }$ with duration equal to $L _ { i j }$ times unit time interval,

$L _ { i j } ^ { m a x }$ the maximal lead time of $S _ { i j } ,$

$d _ { i } ( 0 )$ the initial retailer demand at t=0 appearing at $W _ { i } ,$ $\lambda _ { i } ( t )$ the retailer arrival intensity during the tth time interval at $W _ { i } ,$

$f _ { i , m } ^ { n }$ the probability of n retailers arriving at $W _ { i }$ with a total demand of m,

$\hat { d } _ { i } ( t )$ the expected retailer demand at wholesaler $W _ { i }$ in the tth time interval,

$\hat { D } _ { i j }$ the expected retailer demand at wholesaler $W _ { i }$ over $L _ { i j } ^ { m a x } ,$

Following Axsäter [3], we assume retailer demand is a Compound Poisson process and retailers arrive at the wholesaler at an arrival intensity of λ. Assuming the probability of n number of retailers arriving at $W _ { i }$ wholesaler during a time interval of length t is $P _ { d _ { i , t } } ( n )$

$$
P _ {d _ {i, t}} (n) = e x p ^ {- \lambda_ {i} t} \frac {\{\lambda_ {i} t \} ^ {n}}{n !}.\tag{1}
$$

If the conditional probability of n number of retailers requires m demand is given by $P _ { d _ { i , t } } ( m | n ) = f _ { 1 , m } ^ { n }$ then the probability of retailer demands at the $W _ { i }$ wholesaler during the time interval t is,

$$
\begin{array}{l} P _ {d _ {i, t}} (m) = \sum_ {n = 1} ^ {m} P _ {d _ {i, t}} (m | n) P _ {d _ {i, t}} (n) \\ = \sum_ {n = 1} ^ {m} e ^ {- \lambda_ {i} t} f _ {1, m} ^ {n} (n) \frac {\{\lambda_ {i} t \} ^ {n}}{n !}. \end{array}\tag{2}
$$

The expected retailer demand at $W _ { i }$ wholesaler during a time t is given by

$$
\hat {d} _ {i} (t) = \sum_ {m = 1} ^ {\infty} m P _ {d _ {i, t}} (m).
$$

Applying the function of $P _ { d _ { i , t } } ( m )$ from Eq. (2),

$$
\hat {d} _ {i} (t) = \exp^ {- \lambda_ {i} t} \sum_ {m = 1} ^ {+ \infty} \sum_ {n = 1} ^ {m} \frac {\{\lambda_ {i} t \} ^ {n}}{n !} m f _ {1, m} ^ {n} (n).\tag{3}
$$

![](/api/attachments/3DJUTZEE/fulltext/images/b9677248993d04307745957cf7075bcd42c992b13596b2de8cad8b2b8ff30e11.jpg)  
Expected demand during t = 5 and $\mathbf { t } = \mathbf { 0 } , \hat { d } _ { i } ( 5 ) - \hat { d } _ { i } ( 0 )$ Expected demand during t = 4 and t = 0 , $\hat { d } _ { i } ( 4 ) - \hat { d } _ { i } ( 0 )$  
Fig. 1. Diagram of expected demand at the wholesaler Wi.

$\operatorname { A t } t = 0 ,$ , demand with the wholesaler $W _ { i , } d _ { i } ( 0 )$ is the outstanding demand carried forward from the previous scheduling period and that needs to be urgently ful<sup>fi</sup>lled.

If the supplier, $S _ { i j }$ of the wholesaler $W _ { i }$ takes $L _ { i j }$ lead time to deliver the order and assuming that the probability mass function of delivery lead time of $S _ { i j }$ is $g _ { i j } ( t )$ then the expected lead time of $E ( L _ { i j } )$ is given by

$$
E \left(L _ {i j}\right) = \int_ {t = 0} ^ {L _ {i j}} t g _ {i j} (t) d t.
$$

Let's consider that one scheduling period is the maximum lead time o $\mathrm { f } { S _ { i j } } , { L _ { i j } ^ { m a x } }$ . Then the expected demand at $W _ { i }$ during one scheduling period is

$$
\hat {D} _ {i j} = \sum_ {k = 1} ^ {L _ {i j} ^ {m a x}} \hat {d} _ {i} (k).
$$

From Eq. (3),

$$
\hat {D} _ {i j} = \sum_ {k = 1} ^ {L _ {i j} ^ {m a x}} e ^ {- \lambda_ {i} k} \sum_ {m = 1} ^ {+ \infty} \sum_ {n = 1} ^ {m} \frac {\{\lambda_ {i} k \} ^ {n}}{n !} m f _ {1, m} ^ {n} (n).\tag{4}
$$

Fig. 1 presents a schematic diagram of the expected retailer demand at wholesaler $W _ { i }$ and Table 1 presents the expected demand for each time period. The calculations in the following sections refer back to these for better understanding.

## 3.1. Costs of supply

Inventory costs of a wholesaler consist of three components: purchasing costs of $P _ { i j k }$ of the orders to suppliers and intra-shipments from the other wholesalers, backordering costs of $B _ { i j k }$ for unful<sup>fi</sup>lled retailer demands and holding costs of $H _ { i j k }$ for carrying inventory for potential demands.

$$
C _ {i j k} (x) = P _ {i j k} (x) + B _ {i j k} (x) + H _ {i j k} (x)\tag{5}
$$

Expected demand at the wholesaler $W _ { i } .$

<table><tr><td>Time period</td><td>Expected demand</td></tr><tr><td> $[t_0 - t_1]$ </td><td> $\hat{d}_i(1)$ </td></tr><tr><td> $[t_1 - t_2]$ </td><td> $\hat{d}_i(2) - \hat{d}_i(1)$ </td></tr><tr><td> $[t_2 - t_3]$ </td><td> $\hat{d}_i(3) - \hat{d}_i(2)$ </td></tr><tr><td> $[(L_{ij}^{max} - 2) - (L_{ij}^{max} - 3)]$ </td><td> $\hat{d}_i(L_{ij}^{max} - 1) - \hat{d}_i(L_{ij}^{max} - 2)$ </td></tr><tr><td> $[(L_{ij}^{max} - 1) - (L_{ij}^{max})]$ </td><td> $\hat{d}_i(L_{ij}^{max}) - \hat{d}_i(L_{ij}^{max} - 1)$ </td></tr></table>

![](/api/attachments/3DJUTZEE/fulltext/images/2eb4d867b0a6c0481f14b8b90362239eb132c03fcff8a1f41bca911cd1de747e.jpg)  
Fig. 2. A schematic diagram of the supply chain of wholesalers, retailers and suppliers

We consider that the maximum lead time taken by the supplier is the scheduling period for the wholesaler's decision. In our model, the period to update the wholesaler is set to the maximal lead time of the given supplier. So all the orders made should be received in the period. $W _ { i }$ therefore there will be no outstanding orders from its suppliers at the initial point of a new period, which will simplify the total cost model and decision rules for intra-shipment. So the inventory level of the wholesaler is equal to its inventory position.

The context of the wholesale operation consists of multiple retailers, wholesalers and suppliers as shown in Fig. 2. All the wholesalers belong to the same cost center. The dashed black lines represent possible intra-shipments within the cost center. For simplicity of this decision model, we assume that when the wholesaler, $W _ { i }$ makes intra-shipments, this involves a selected single another wholesaler. Similarly, W places orders with a single supplier instead of using multiple suppliers.

## 3.1.1. Purchasing costs

Purchasing costs are incurred when the wholesaler does not have suf<sup>fi</sup>cient stock to ful<sup>fi</sup>ll the retailer demand and place the orders for the unful<sup>fi</sup>lled demand from another supplier or another wholesaler. Hence, the purchasing cost has two components depending on the source of supply: supplier or another wholesaler. If the unit cost of purchasing from the supplier $S _ { j }$ is $p _ { i j } ,$ the unit cost of trans-shipping from the wholesaler $W _ { k }$ is $q _ { i k }$ and the trans-shipped quantity is x units then the purchasing cost of $P _ { i j k } \left( x \right)$ is given by

$$
P _ {i j k} (x) = p _ {i j} \left(d _ {i} (0) - l _ {i} (0) + \hat {D} _ {i j} - x\right) + q _ {i k} (x)\tag{6}
$$

where $d _ { i } ( 0 )$ and $l _ { i } ( 0 )$ are the outstanding order quantity and the inventory level of the W at t=0.

## 3.1.2. Backordering costs

The backordering cost is incurred when the excess retailer orders that cannot be ful<sup>fi</sup>lled immediately are held on the books until the next shipment arrives [20]. As Axsäter [3], we assume that excessive retailer demands that cannot be ful<sup>fi</sup>lled by the stock in hand and transshipments (if decided,) are backordered. For the initial back-ordered quantity of $( d _ { i } ( 0 ) - \updownarrow _ { i } ( 0 ) - x )$ the back-ordering time is the expected ar-<sup>ð Þ l ð Þ</sup>rival time of order from the supplier. We assume that intra-shipping cost from another wholesaler is signi<sup>fi</sup>cantly higher than the purchasing cost from suppliers. Hence, only the urgent orders are intra-shipped and others are sourced from suppliers. We also assume that intra-shipped orders have zero lead time. Hence, at the beginning of the scheduling period, any outstanding order that cannot be ful<sup>fi</sup>lled by the local inventory and intra-shipped orders, generate backordering costs, until the expected supplier order supply entry day. Subsequent retailer demands expected to arrive during the time range of $0 \leq \mathrm { t } \leq E ( L _ { i j } ) - 1$ are not ful-<sup>fi</sup>lled due to stock-out status and consequently they generate back ordering cost depending on the back-order time.

Based on the expected retailer demand as shown in Fig. 1 and Table 1, the following Table 2 presents the back-order time for the unful<sup>fi</sup>lled demand at the wholesaler, W .

If $B _ { i j k }$ is the backorder cost for the wholesaler W for the orders placed with the supplier $S _ { i j }$ after the intrashipments from the $W _ { k }$ and $b _ { i j }$ is the unit back-order cost then,

$$
B _ {i j k} (x) = b _ {i j} \left(d _ {i} (0) - l _ {i} (0) - x\right) E \left(L _ {i j}\right) + b _ {i j} \int_ {t = 1} ^ {E \left(L _ {i j}\right) - 1} \left\{\hat {d} (t) - \hat {d} (t - 1) \right\} \left\{E \left(L _ {i j}\right) - t \right\} d t.\tag{7}
$$

As shown in Eq. (7), the two components of the backordering cost are the back-order cost at t=0 and the backorder cost for the expected demand until one period before the expected lead time of the supplier. The expected demand at the period of expected lead time can be ful<sup>fi</sup>lled with the received supply from the supplier. Any retailer demands arriving after the expected lead time of supplier do not incur any backordering cost but will generate holding costs that will be discussed separately below.

Table 3  
Backorder time period for the unful<sup>fi</sup>lled demand.

<table><tr><td>Time period of demand</td><td>Demand</td><td>Backorder period (e.g. number of days)</td></tr><tr><td>at  $t_0$ </td><td> $(d_i(0)-l_i(0)-x)$ </td><td> $E(L_{ij})$ </td></tr><tr><td> $[t_0-t_1]$ </td><td> $\hat{d}_i(1)$ </td><td> $E(L_{ij})-1$ </td></tr><tr><td> $[t_1-t_2]$ </td><td> $\hat{d}_i(2)-\hat{d}_i(1)$ </td><td> $E(L_{ij})-2$ </td></tr><tr><td> $[t_2-t_3]$ </td><td> $\hat{d}_i(3)-\hat{d}_i(2)$ </td><td> $E(L_{ij})-3$ </td></tr><tr><td> $[\{E(L_{ij})-2\}-\{E(L_{ij})-3\}]$ </td><td> $\hat{d}_i(E(L_{ij})-2)-\hat{d}_i(E(L_{ij})-3)$ </td><td>2</td></tr><tr><td> $[\{E(L_{ij})-1\}-\{E(L_{ij})-2\}]$ </td><td> $\hat{d}_i(E(L_{ij})-1)-\hat{d}_i(E(L_{ij})-2)$ </td><td>1</td></tr></table>

## 3.1.3. Holding costs

Holding cost is the inventory carrying cost which consists of the costs of providing physical space to store items, taxes and insurance, breakage and other damages and opportunity cost of alternative investment [20]. During the scheduling period, holding costs are incurred after the order is received at the expected lead time of the supplier and the outstanding demands are delivered i.e. during the time period of $E ( L _ { i j } ) + 1 \le t \le L _ { i j } ^ { m a x }$ . Based on the expected demand as shown in Fig. 1 and Table 1, the following Table 3 presents the holding cost for the stock received from the supplier at $E ( L _ { i j } )$

If the total holding cost of $H _ { i j k }$ during the scheduling period and the unit holding cost of the $W _ { i }$ wholesaler is $h _ { i }$ then,

$$
H _ {i j k} (x) = \int_ {t = E \left(L _ {i j}\right) + 1} ^ {L _ {i j} ^ {\max}} \left\{\hat {d} (t) - \hat {d} (t - 1) \right\} \left\{t - E \left(L _ {i j}\right) \right\} h _ {i j} d t\tag{8}
$$

## 3.2. Decision rule for intra-shipment orders

By substituting the functions of purchasing costs, backordering costs and holding costs in Eq. (5), the total cost during the scheduling period is given by,

$$
\begin{array}{l} _ {C i j k} (x) = p _ {i j} \left(d _ {i} (0) - l _ {i} (0) + \hat {D} _ {i j} - x\right) + q _ {i k} (x) \\ \qquad + (d (0) - l (0) - x) E L _ {i j} b _ {i} + b _ {i} \int_ {t = 0} ^ {E \left(L _ {i j}\right) - 1} \hat {d} (t) - \hat {d} (t - 1) \Bigl \{E \left(L _ {i j}\right) - t \Bigr \} d t \\ \qquad + \int_ {t = E \left(L _ {i j}\right) + 1} ^ {L _ {i j} ^ {m a x}} \Bigl \{\hat {d} (t) - \hat {d} (t - 1) \Bigr \} \Bigl \{t - E \left(L _ {i j}\right) \Bigr \} h _ {i} d t \end{array}
$$

$$
\begin{array}{l} _ {C i j k} (x) = \Big \{- p _ {i j} - E \Big (L _ {i j} \Big) b _ {i j} + q _ {i k} \Big \} x \\ \qquad + p _ {i j} \left(d _ {i} (0) - l _ {i} (0) + \hat {D} _ {i j}\right) + \{d _ {i} (0) - l _ {i} (0) \}   E \Big (L _ {i j} \Big) b _ {i} \\ \qquad + b _ {i} \int_ {t = 1} ^ {E (L _ {i j}) - 1} \Big \{\hat {d} (t) - \hat {d} (t - 1) \Big \} \Big \{E \Big (L _ {i j} \Big) - t \Big \} d t \\ \qquad + \int_ {t = E (L _ {i j}) + 1} ^ {L _ {i j} ^ {m a x}} \Big \{\hat {d} (t) - \hat {d} (t - 1) \Big \} \Big \{t - E \Big (L _ {i j} \Big) \Big \} h _ {i}   d t. \end{array}\tag{9}
$$

Holding period of the stock received from the supplier.

<table><tr><td>Time period of demand</td><td>Demand</td><td>Holding period (e.g. in number of days)</td></tr><tr><td> $\{E(L_{ij}) + 1\} - E(L_{ij})$ </td><td> $\hat{d}_{i}(E(L_{ij}) + 1) - \hat{d}_{i}E(L_{ij})$ </td><td>1</td></tr><tr><td> $\{E(L_{ij}) + 2\} - \{E(L_{ij}) + 1\}$ </td><td> $\hat{d}_{i}(E(L_{ij}) + 2) - \hat{d}_{i}(E(L_{ij}) + 1)$ </td><td>2</td></tr><tr><td> $\{E(L_{ij}) + 3\} - \{E(L_{ij}) + 2\}$ </td><td> $\hat{d}_{i}(E(L_{ij}) + 3) - \hat{d}_{i}(E(L_{ij}) + 2)$ </td><td>3</td></tr><tr><td> $\{L_{ij}^{max} - 1\} - \{L_{ij}^{max} - 2\}$ </td><td> $\hat{d}_{i}(L_{ij}^{max} - 1) - \hat{d}_{i}(L_{ij}^{max} - 2)$ </td><td> $E(L_{ij}^{max} - 1) - E(L_{ij})$ </td></tr><tr><td> $L_{ij}^{max} - \{L_{ij}^{max} - 1\}$ </td><td> $\hat{d}_{i}(L_{ij}^{max}) - \hat{d}_{i}(L_{ij}^{max} - 1)$ </td><td> $E(L_{ij}^{max}) - E(L_{ij})$ </td></tr></table>

With respect to the quantity of trans-shipment (x), the total cost function as shown in Eq. (9) is linear. When the tangent of the above linear function $( - p _ { i j } - E ( L _ { i j } ) b _ { i } + q _ { i k } )$ is negative the total cost decreases with the increasing number of trans-shipments.

Hence the decision rule for intra-shipments is

$$
\begin{array}{l} - p _ {i j} - E \Big (L _ {i j} \Big) b _ {i} + q _ {i k} <   0 \\ q _ {i k} <   p _ {i j} + E \Big (L _ {i j} \Big) b _ {i}. \end{array}\tag{10}
$$

In summary, if the above decision rule shown in Eq. (10) is satis-<sup>fi</sup>ed, the higher the quantity of trans-shipment the lower the total cost for the wholesaler $W _ { i } .$ In other words, the wholesaler W should decide to ful<sup>fi</sup>ll the demand by ordering only from the supplier $S _ { i j }$ if the above decision rule is not satis<sup>fi</sup>ed.

3.3. Decision rules for the favorite wholesaler and the optimum size of trans-shipment

According to the total cost function shown in Eq. (9), if the wholesaler $W _ { i }$ satis<sup>fi</sup>ed the decision rule in Eq. (10), the higher the transshipment quantity, the lower the total cost to the wholesaler $W _ { i \cdot }$ . Furthermore, it suggests the preference for the lowest unit cost of transshipment, $q _ { i k }$ and in turn trans-ship from the wholesaler $W _ { k }$ who provides at the lowest cost.

We only order the initial outstanding urgent demand at $t = 0$ which is $d _ { i } ( 0 )$ from another wholesaler due to the increased unit cost of trans-shipment from another wholesaler compared with the unit purchasing cost from suppliers. Even though the maximum bene<sup>fi</sup>ts are received when the highest quantity is trans-shipped, this maximum quantity of trans-shipment has a practical limitation — the available stock with the wholesaler $W _ { k } .$ . For simplicity of the model, we assume that the preferred other wholesaler, has suf<sup>fi</sup>cient stock to deliver the trans-shipment. Hence the limiting parameter of the trans-shipment order is the outstanding demand at $t = 0 .$ . The optimum size of the trans-shipment, $\mu _ { k }$ is given by

$$
\mu_ {k} = d _ {i} (0) - l _ {i} (0).\tag{11}
$$

Therefore, in this model the size of the trans-shipment can be either 0 or $\mu _ { k } .$ When the decision rule in $\operatorname { E q . }$ (10) is not satis<sup>fi</sup>ed there will not be any trans-shipment and the maximum of $\mu _ { k }$ when it is satis<sup>fi</sup>ed.

## 3.4. Decision rule for the selection of the supplier

According to Fig. 1, the wholesaler $W _ { i }$ is able to purchase from any one of its suppliers. The selection decision is derived by the global minimization of the total cost function in Eq. (9) with a <sup>fi</sup>xed x $( x \neq 0 )$ and a known $W _ { k } .$

Hence, the decision rule is given by the condition that satis<sup>fi</sup>es

$$
C _ {i} = \min \left(C _ {i 1}, C _ {i 2}, \dots , C _ {i j} \dots , C _ {i N _ {i}}\right)\tag{12}
$$

Where $N _ { i }$ is the number of suppliers of the wholesaler $W _ { i } .$

## 4. Scenario analysis and discussion

In order to illustrate the pragmatic use of the decision rules derived above, let's consider the decision making process of the wholesaler XYZ. Due to intense competition in the market, accessing con<sup>fi</sup>dential business information such as order and procurement data is extremely dif<sup>fi</sup>cult to obtain. We consider therefore, a hypothetical wholesaler of XYZ and assume it has a constant retailer arrival intensity so $\lambda ( t ) = \lambda$ for any t. The probability of n number of retailers arriving at the wholesaler XYZ with demand m, $f _ { 1 , m } ^ { n }$ can be calculated mathematically by using the method proposed by Axsäter ([4]: 80–83). According to Axsäter [4], the probability distribution of demand, $D ( t )$ can be shown by a negative binomial distribution as shown below.

$$
P (D (t) = k) = \frac {r (r + 1) \dots (r + k - 1)}{k !} (1 - p) ^ {r} p ^ {k},
$$

where r can be any positive number and $0 < p < 1$

Alternatively, the probabilities can also be calculated by using historical retailer demand records of XYZ from their inventory management. In addition, using the historical retailer orders, sales, procurement and inventory accounting records of XYZ, the values of retailer arrival intensity $( \lambda ) ,$ , unit holding cost $\left( h _ { 1 } \right)$ and the backordering cost $\left( b _ { 1 } \right)$ can be estimated. Let's take $\lambda { = } 3 , h _ { 1 } { = } 2$ , and $b _ { 1 } = 2$ for the wholesaler XYZ. Since the retailer demand is essentially <sup>fi</sup>nite we set the upper bound of the retailer demand at the wholesaler XYZ as $d _ { i } ^ { m a x } = 3 0$

4.1. Case 1 — wholesaler XYZ operating with one supplier and one other wholesaler

First, we consider a somewhat limited context where wholesaler XYZ having one other wholesaler $W _ { 2 }$ and one supplier $S _ { 1 } ,$ , let's assume the maximum lead time of $L _ { 1 1 } ^ { m a x } = 1 0 ,$ , unit purchasing cost from the supplier 1, $p _ { 1 1 }$ is 2.2 and the inventory level of XYZ at $t = 0 , l _ { 1 } ( 0 ) =$ 0 and the sudden demand at $t = 0 , d _ { 1 } ( 0 ) = 6$

Table 4 presents the decision making process of the wholesaler XYZ for different values of the unit intra-shipment cost from the other wholesalers, $q _ { 1 k }$ and the expected lead time from the supplier 1, $E ( L _ { 1 1 } )$

Fig. 3 and Table 5 show the cost function for those different values of $q _ { 1 k }$ and $E \left( L _ { 1 1 } \right)$ and indicate that only when the decision rule applies the total cost decreases with the increasing size of trans-shipment from the other wholesaler. The total cost functions of $\mathsf { C } _ { 1 4 4 }$ and $\mathsf C _ { 1 2 2 }$ demonstrate a scenario in which trans-shipments should not be made by the wholesaler XYZ and the other ${ \mathsf { C } } _ { 1 1 1 }$ and $\mathsf { C } _ { 1 3 3 }$ satisfy the decision rule to choose to trans-ship from another wholesaler.

4.2. Case 2 — wholesaler, XYZ operating with one supplier and multiple other wholesalers

When the decision for trans-shipments is made, the immediate following decision that needs to be made is with which other wholesaler to place the intra-shipment order. Considering a scenario where the wholesaler, XYZ operates in a system with one chosen supplier and multiple other wholesalers, we can demonstrate the application of the decision for the favorite other wholesaler following the rule in Eq. (12).

Table 6 shows calculated values for the total cost and Fig. 4 demonstrates how this decision rule, derived earlier, works. In a context with one supplier, $S _ { 1 }$ and four other wholesalers, $W _ { 1 } , W _ { 2 } , W _ { 3 } ,$ the graph shows the total cost functions for varying values for $q _ { i j k }$ for 4 different other wholesalers.

![](/api/attachments/3DJUTZEE/fulltext/images/62881659410c7ea0a4e4a4dee0cabbc5beabd50175db534dca38733fef3d6b0d.jpg)  
Fig. 3. Total cost and trans‐shipped units for different q and $E ( L _ { i j } ) .$

The total cost function of $\mathsf { C } _ { 1 1 4 }$ is increasing with the size of transshipments thus omitted because that does not satisfy the primary decision rule. From the others, $\mathsf { C } _ { 1 1 4 }$ at the bottom gives the minimum cost for any amount of trans-shipped units which makes $W _ { 4 }$ the favorite wholesaler for XYZ in alignment with the corollary decision presented in Eq. (12).

4.3. Case 3 — wholesaler, XYZ operating with multiple suppliers and mul tiple other wholesalers

Considering a more general scenario of wholesaler XYZ operating in a system with multiple wholesalers and suppliers, the decision for the favorite supplier and wholesaler that provides the minimum total cost is critical. Such decisions are more complicated in an environment as shown in Fig. 2. Fig. 5 plots the total cost function for different values of $q _ { i j k }$ and $p _ { i j }$ representing different wholesalers and suppliers and Table 7 presents the corresponding values. Since the total cost functions of ${ \sf C } _ { 1 1 5 } , { \sf C } _ { 1 2 5 }$ and $\mathsf { C } _ { 1 3 5 }$ increase with the size of trans-shipment, they are excluded from further consideration. The remaining cost functions satisfy the primary decision rule for transshipment by XYZ. If the outstanding demand at $t = 0 \mathrm { i s } 6 , \mathsf C _ { 1 1 1 }$ at the bottom provides the lowest cost for the quantity of 6 units of transshipment. Therefore, XYZ should trans-ship 6 units from the other wholesaler 1 and backorder $D _ { m a x }$ of 30 units from the supplier 1.

This approach has implications for managers in logistics operations. The pragmatic adoptability is important in development of theoretical models. For inventory management, the decisions on lateral trans-shipments are needed to be made systematically without following ad hoc methods and the above three case scenarios represent how the proposed model may be applied in different real situations in logistics operations. The less complexity of data requirements and mathematical calculations and the visualization of the underlying concepts of this approach through the graphical plots show the pragmatic bene<sup>fi</sup>ts of this approach in real contexts. In particular, the calculations can be done using commonly used spreadsheet software such as MS Excel and Fig. 6 presents a screenshot of how MS Excel is used to make the decision for the complex scenario of XYZ operating in a context of multiple suppliers and wholesalers.

Decision rule for the wholesaler XYZ in a context with one other wholesaler and one supplier.

<table><tr><td></td><td> $q_{11}=5,E(L_{11})=3$ </td><td> $q_{12}=9,E(L_{11})=2$ </td><td> $q_{13}=6,E(L_{11})=4$ </td><td> $q_{14}=7,E(L_{11})=2$ </td></tr><tr><td>Total cost function</td><td> $C_{111}$ </td><td> $C_{122}$ </td><td> $C_{133}$ </td><td> $C_{144}$ </td></tr><tr><td>Testing the decision rule</td><td> $q_{12}<p_{11}+E(L_{11})b_{1}$ decision rule satisfied</td><td> $q_{12}>p_{11}+E(L_{11})b_{1}$ decision rule dissatisfied</td><td> $q_{12}<p_{11}+E(L_{11})b_{1}$ decision rule satisfied</td><td> $q_{12}>p_{11}+E(L_{11})b_{1}$ decision rule dissatisfied</td></tr><tr><td>Decision</td><td>Maximum quantity of 6 units to be trans-shipped from the wholesaler  $W_{2}$ </td><td>No trans-shipments. All ordered from the supplier  $S_{1}$ </td><td>Maximum quantity of 6 units to be trans-shipped from the wholesaler  $W_{2}$ </td><td>No trans-shipments. All ordered from the supplier  $S_{1}$ </td></tr></table>

Table 5  
Total cost for different trans‐shipment unit cost and expected lead time of the supplier.

<table><tr><td>Size of trans-shipment, x</td><td>0</td><td>10</td><td>20</td><td>30</td><td>40</td></tr><tr><td> $C_{111}$  for  $q_{11}=5,E(L_{11})=3$ </td><td>2592.88</td><td>2560.88</td><td>2528.88</td><td>2496.88</td><td>2464.88</td></tr><tr><td> $C_{122}$  for  $q_{12}=9,E(L_{11})=2$ </td><td>2737.82</td><td>2765.82</td><td>2793.82</td><td>2821.82</td><td>2849.82</td></tr><tr><td> $C_{133}$  for  $q_{13}=6,E(L_{11})=4$ </td><td>2447.94</td><td>2405.94</td><td>2363.94</td><td>2321.94</td><td>2279.94</td></tr><tr><td> $C_{144}$  for  $q_{14}=7,E(L_{11})=2$ </td><td>2882.76</td><td>2910.76</td><td>2938.76</td><td>2966.76</td><td>2994.76</td></tr></table>

Calculated values for total cost for XYZ having one supplier and multiple other wholesalers

<table><tr><td>Size of trans-shipment, x</td><td>0</td><td>2</td><td>4</td><td>6</td><td>8</td></tr><tr><td> $C_{111}$ </td><td>2592.88</td><td>2590.48</td><td>2588.08</td><td>2585.68</td><td>2583.28</td></tr><tr><td> $C_{112}$ </td><td>2592.88</td><td>2587.48</td><td>2582.08</td><td>2576.68</td><td>2571.28</td></tr><tr><td> $C_{113}$ </td><td>2592.88</td><td>2588.48</td><td>2584.08</td><td>2579.68</td><td>2575.28</td></tr><tr><td> $C_{114}$ </td><td>2592.88</td><td>2589.48</td><td>2586.08</td><td>2582.68</td><td>2579.28</td></tr></table>

## 5. Conclusion

The decision support system developed in this article serves the inventory management of wholesaler operations in making decisions on whether to trans-ship outstanding urgent retailer demands or back order from suppliers in full. The main advantage of this decision support system is the ease of application by wholesaler inventory management. The decision is driven by the important cost minimization objectives, the simplicity of the rules and the need for less cumbersome data inputs to the model, underpin the ease of adoption. The main decision rule needs only the unit purchasing cost from suppliers, unit trans-shipment cost from another wholesaler, own unit backordering cost, and the expected lead time from its suppliers. The corollary decisions on deciding the favorite other wholesaler and supplier, derived in this article can also be easily adopted by inventory management without performing complex mathematical calculations. Moreover, common spreadsheet software such as MS Excel can be used for these calculations as shown above.

We are aware of the limitations of this study. First, we approximated that the probability distribution of retailer arrival at the wholesaler has a Compound Poisson distribution. Second, the suggested method of estimating backorder costs and holding costs was based on previous cost records. We assumed that the estimates based on old records would hold true during the forecasting period but the current dynamic business environment challenges that assumption. Furthermore, we assumed that the selected other wholesaler is able to supply the trans-shipment order in full thus no partial orders with multiple wholesalers were considered. However, wholesalers can place partial orders of trans-shipments with multiple other wholesalers for reasons of risk mitigation. Future research has the opportunity to accommodate the situation of partial orders with multiple suppliers and other wholesalers and to further develop the proposed decision support system in the present study.

![](/api/attachments/3DJUTZEE/fulltext/images/4d30549ba734e65b31ce64df2936f3967abcf9d361fc87b479014c87c029184b.jpg)  
Fig. 4. Total cost functions — XYZ operating in a system with one supplier and multiple other wholesalers

There is potential for developing this model into a software program for wide adoption by logistics organizations. In a standalone program, the user interface should allow the input <sup>fi</sup>elds for organization-speci<sup>fi</sup>c dynamic parameters such as previous demand records, unit backordering, holding and purchasing costs and supplier lead times etc. In a wider scale, the proposed decision rule algorithm can be integrated as a module of the existing enterprise resource planning applications with the capability of extracting data from previous transaction records in the internal databases, thereby extending the capability of achieving more reliable and accurate expected costs in inventory management operations. Such extended software applications should be scalable to handle different scenarios and upgradable to accommodate the intended potential future developments of this approach covering partial order situations.

![](/api/attachments/3DJUTZEE/fulltext/images/423e58eaf2944b1071a532f13f352bcbc36162c6cfc3dd6754e68510a7dbf806.jpg)  
Fig. 5. Total cost functions for XYZ in a system with multiple suppliers and multiple wholesalers.

Table 7  
Calculated values of total cost for the wholesaler for different options in a multi supplier and multiple wholesaler system.

<table><tr><td>Size of trans-shipment, x</td><td>0</td><td>2</td><td>4</td><td>6</td></tr><tr><td> $C_{111}$ </td><td>6217.09</td><td>6213.69</td><td>6210.29</td><td>6206.89</td></tr><tr><td> $C_{121}$ </td><td>6226.09</td><td>6222.09</td><td>6218.09</td><td>6214.09</td></tr><tr><td> $C_{131}$ </td><td>6232.09</td><td>6227.69</td><td>6223.29</td><td>6218.89</td></tr><tr><td> $C_{112}$ </td><td>6217.09</td><td>6214.69</td><td>6212.29</td><td>6209.89</td></tr><tr><td> $C_{122}$ </td><td>6226.09</td><td>6223.09</td><td>6220.09</td><td>6217.09</td></tr><tr><td> $C_{132}$ </td><td>6232.09</td><td>6228.69</td><td>6225.29</td><td>6221.89</td></tr><tr><td> $C_{113}$ </td><td>6217.09</td><td>6215.69</td><td>6214.29</td><td>6212.89</td></tr><tr><td> $C_{123}$ </td><td>6226.09</td><td>6224.09</td><td>6222.09</td><td>6220.09</td></tr><tr><td> $C_{133}$ </td><td>6232.09</td><td>6229.69</td><td>6227.29</td><td>6224.89</td></tr><tr><td> $C_{114}$ </td><td>6217.09</td><td>6216.69</td><td>6216.29</td><td>6215.89</td></tr><tr><td> $C_{124}$ </td><td>6226.09</td><td>6225.09</td><td>6224.09</td><td>6223.09</td></tr><tr><td> $C_{134}$ </td><td>6232.09</td><td>6230.69</td><td>6229.29</td><td>6227.89</td></tr><tr><td> $C_{115}$ </td><td>6217.09</td><td>6218.69</td><td>6220.29</td><td>6221.89</td></tr><tr><td> $C_{125}$ </td><td>6226.09</td><td>6227.09</td><td>6228.09</td><td>6229.09</td></tr><tr><td> $C_{135}$ </td><td>6232.09</td><td>6232.69</td><td>6233.29</td><td>6233.89</td></tr></table>

![](/api/attachments/3DJUTZEE/fulltext/images/1040e053c692b46940e8605c3d083fcbbaaad6237f721c70739bd24aaf6f9e2e.jpg)  
Fig. 6. MS Excel spreadsheet for calculating the favorite supplier in case 3.

## References

[1] T.W. Archibald, S.a.E. Sassen, L.C. Thomas, An optimal policy for a two depot inventory problem with stock transfer, Management Science 43 (2) (1997) 173–183.

[2] S. Axsäter, Modelling emergency lateral transshipments in inventory systemss, Management Science 36 (11) (1990) 1329–1338.

[3] S. Axsäter, A new decision rule for lateral transshipments in inventory systems, Management Science 49 (9) (2003) 1168–1179.

[4] S. Axsäter, Inventory Control, second ed. Springer, New York, 2006.

[5] J. Burton, A. Banerjee, Cost-parametric analysis of lateral transshipment policies in two-echelon supply chains, International Journal of Production Economics 93–94 (2005) 169–178.

[6] H.N. Chiu, H.L. Huang, A multi-echelon integrated JIT inventory model using the time buffer and emergency borrowing policies to deal with random delivery lead times, International Journal of Production Research 41 (13) (2003) 2911–2931

[7] R. De Koster, T. Le-Duc, K.J. Roodbergen, Design and control of warehouse order picking: a literature review, European Journal of Operational Research 182 (2) (2007) 481–501.

[8] S.S. Erengüç, N.C. Simpson, A.J. Vakharia, Integrated production/distribution planning in supply chains: an invited review, European Journal of Operational Research 115 (2) (1999) 219–236.

[9] P.T. Evers, Heuristics for assessing emergency transshipments, European Journa of Operational Research 129 (2) (2001) 311–316.

[10] J. Grahovac, A. Chakravarty, Sharing and lateral transshipment of inventory in a supply chain with expensive low-demand items, Management Science 47 (4) (2001).579-594

[11] C.W. Holsapple, M.P. Sena, ERP plans and decision-support bene<sup>fi</sup>ts, Decision Support Systems 38 (4) (2005) 575–590

[12] S.O. Kimbrough, D.J. Wu, F. Zhong, Computers play the beer game: can arti<sup>fi</sup>cial agents manage supply chains? Decision Support Systems 33 (3) (2002) 323–333.

[13] P. Köchel, S. Kunze, U. Nieländer, Optimal control of a distributed service system with moving resources: application to the <sup>fl</sup>eet sizing and allocation problem, International Journal of Production Economics 81–82 (2003) 443–459

[14] Y.H. Lee, J.W. Jung, Y.S. Jeon, An effective lateral transshipment policy to improve service level in the supply chain, International Journal of Production Economics 106 (1) (2007) 115-126

[15] S. Li, B. Lin, Accessing information sharing and information quality in supply chain management Decision Support Systems 42 (3) (2006) 1641–1656

[16] S.T. March, A.R. Hevner, Integrated decision support systems: a data warehousing perspective, Decision Support Systems 43 (3) (2007) 1031–1043.

[17] S. Minner, E.A. Silver, Evaluation of two simple extreme transshipment strategies, International Journal of Production Economics 93–94 (2005) 1–11.

[18] S. Minner, E.A. Silver, D.J. Robb, An improved heuristic for deciding on emergency transshipments, European Journal of Operational Research 148 (2) (2003) 384–400.

[19] G. Nagy, S. Salhi, Location-routing: issues, models and methods, European Journal of Operational Research 177 (2) (2007) 649–672.

[20] S. Nahmias, Production and Operations Analysis, sixth ed. The McGraw-Hill Companies, New York, 2009.

[21] F. Olsson, Optimal policies for inventory systems with lateral transshipments, International Journal of Production Economics 118 (1) (2009) 175–184.

[22] M.P. Papazoglou, P. Ribbers, A. Tsalgatidou, Integrated value chains and their implications from a business and technology standpoint, Decision Support Systems 29 (4) (2000) 323–342.

[23] M. Rosenshine, D. Obee, Analysis of a standing order inventory system with emergency orders, Operations Research 24 (6) (1976) 1143–1155.

[24] G. Tagaras, M.A. Cohen, Pooling in two-location inventory systems with non-negligible replenishment lead times, Management Science 38 (8) (1992) 1067–1083.

[25] D.J. Thomas, P.M. Grif<sup>fi</sup>n, Coordinated supply chain management, European Journal of Operational Research 94 (1) (1996) 1–15.

[26] C.E. Weber, More on complementarity and substitutability in the transshipment problem, European Journal of Operational Research 156 (1) (2004) 213–222.

[27] L. Xu, Z. Li, S. Li, F. Tang, A decision support system for product design in concurrent engineering, Decision Support Systems 42 (4) (2007) 2029–2042.

![](/api/attachments/3DJUTZEE/fulltext/images/503ed823f6b9267132302fed7aff82f723aad28cc1ce9a3f8a1c4e57dadfdee7.jpg)

![](/api/attachments/3DJUTZEE/fulltext/images/90216b9705a6a799e063862770656afdaf3224735a28b6a431d2d315fb343ea7.jpg)

Henry Lau is currently a senior lecturer of the School of Business at the University of Western Sydney. He received his Masters degree at Aston University in Birmingham in 1981, and his Doctorate at the University of Adelaide in 1995. His current research covers logistics and supply chain management, operations research, engineering management and arti<sup>fi</sup>cial intelligence systems. He has published more than 200 refereed journal papers, 10 book chapters, 1 textbook and attracted a total of HKD 20 million (about AUD 3 million) in research grants. In addition, he has in total been granted 4 patents and won 3 International awards for achievements in innovation.

Dilupa Nakandala is a postdoctoral research fellow at the Centre for Industry and Innovation Studies Research Group, University of Western Sydney, Australia. She obtained her BSc in Electrical and Electronics Engineering (Grade 1) at the University of Peradeniya in 1998, MBA at the University of Moratuwa in 2004 and PhD in innovation studies at the University of Western Sydney in 2010. Dilupa is a certi<sup>fi</sup>ed project management professional of the PMI, USA. She has over eight years of industry experience in project and business management. Her research interests are in innovation, innovation systems, decision support systems, <sup>fi</sup>rm learning and development and renewable energy technologies.
