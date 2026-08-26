---
otero_id: 8426
otero_key: "VT5BAAVK"
title: "Mitigating bankruptcy propagation through contractual incentive schemes"
authors: "Yanhong Sun; Xiaoyan Xu; Zhongsheng Hua"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.02.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Mitigating bankruptcy propagation through contractual incentive schemes

Yanhong Sun <sup>1</sup>, Xiaoyan Xu <sup>1</sup>, Zhongsheng Hua ⁎

School of Management, University of Science & Technology of China, Hefei, Anhui 230026, People's Republic of China

a r t i c l e i n f o

Article history: Received 15 October 2009 Received in revised form 22 December 2011 Accepted 9 February 2012 Available online 17 February 2012

Keywords: Supply chain Multi-agent systems Bankruptcy propagation Contractual incentive schemes Simulation

## a b s t r a c t

With the increasing interdependence among supply chain members on material, information and capital, interactions and decisions characterized by operational parameters are important causes of bankruptcy propagation in supply chain. This paper investigates the methods for mitigating bankruptcy propagation through supply chain coordination. Based on a two-stage supply chain network that consists of multiple upstream manufacturers and multiple downstream retailers, the effectiveness of some typical contractual incentive schemes, including revenue sharing, price discount and quantity <sup>fl</sup>exibility contracts, in mitigating bankruptcy propagation among supply chain members is examined. Through agent-based simulation experiments, it has been revealed that: 1) the three typical supply chain contracts with properly designed contract parameters are effective in mitigating bankruptcy propagation, but their effectiveness depends on operational parameters of the supply chain; 2) horizontal competition among retailers is an important factor in determining the effectiveness of these contracts; 3) revenue sharing contract turns out to be more effective in mitigating bankruptcy propagation than the other two contracts. By comparing the optimal contract parameters with and without considering bankruptcy risks, it has also been found that, a set of contract parameters that can maximize the pro<sup>fi</sup>t of the supply chain may increase the occurrence of bankruptcy in supply chain, leading to the phenomenon of a risk–pro<sup>fi</sup>t tradeoff.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

With the increasing interdependence of supply chain members on material, information and capital, bankruptcy of a supply chain member may lead other member <sup>fi</sup>rms getting into <sup>fi</sup>nancial dif<sup>fi</sup>culties. This phenomenon is termed bankruptcy propagation in network economy [2,9]. An intuitive explanation for bankruptcy propagation is the avalanche of debt chain or credit chain in the supply chain network [2,5,6,9,11]. Recent researches reveal that interactions among supply chain members and decisions made by supply chain members are important causes of the occurrence and propagation of bankruptcy in the supply chain. For a simple three-echelon supply chain that consists of a retailer, a distributor, and a manufacturer, Xu et al. [25] found that demand forecasting methods, market demand characteristics (uncertainty of demand in each period and auto-correlation of demands in consecutive periods) and thus service levels required by the supply chain members, have signi<sup>fi</sup>cant impacts on the occurrence of bankruptcy at each stage of the supply chain. For a two-echelon supply chain network that consists of multiple retailers and manufacturers, Hua et al. [10] investigated impacts of various operational parameters of the supply chain, such as horizontal competition among retailers, order allocation strategies of retailers, wholesale price of manufacturers, characteristics of market demand and number of retailers, on bankruptcy propagation. They found that interactions and decisions characterized by these operational parameters are important causes of the occurrence and propagation of bankruptcy in the supply chain.

Bankruptcy propagation is an important type of <sup>fi</sup>nancial risk in supply chain operations. However, in the previous literature of supply chain risk management, researches are mainly focused on exposure to adverse events [16] and supply chain disruptions caused by natural disasters, strikes and terrorist attacks [20]. Based on speci<sup>fi</sup>c methods of risk assessment and identi<sup>fi</sup>cation, risk mitigation is usually achieved through structure redesign of supply chains [12,15]. In these researches, operational risk is the main topic, while <sup>fi</sup>nancial risk draws little attention. Among the few researches related to <sup>fi</sup>nancial risk of supply chain, Tsai [22] investigated cash <sup>fl</sup>ow risk in a three-tier supply chain, which was measured by the standard deviations of cash in<sup>fl</sup>ows. Through simulation experiments, Tsai [22] established the relationship between the physical <sup>fl</sup>ow and cash <sup>fl</sup>ow, measured the supply chain cash <sup>fl</sup>ow risks with respect to a few time related risk factors, and recommended the best policy of using Asset-Backed Securities (ABS) to <sup>fi</sup>nance accounts receivable as a means to lower the cash in<sup>fl</sup>ow risk. In other words, the risk mitigation policy was suggested from <sup>fi</sup>nancial perspective, rather from operational perspective.

This paper investigates the methods for mitigating bankruptcy propagation through supply chain coordination. Hua et al. [10] reveal that, 1) horizontal competition among retailers could decrease both the average retail price and the average market demand, and thus decrease sales revenue of supply chain, leading to the collapse of supply chain; 2) bankruptcy at retailers could be increased if manufacturers require a high proportion of up-front payment of retailers. Overall, bankruptcy propagation is the result of ineffective control of material <sup>fl</sup>ow and capital <sup>fl</sup>ow along the supply chain. Therefore, it may be possible to mitigate the risk of bankruptcy propagation through vertical coordination between supply chain members. In supply chain management, many contractual incentive schemes (also termed as supply chain contracts, or simply termed as contracts) have been proposed to coordinate the operations of member <sup>fi</sup>rms in a supply chain (e.g., quantity discount contract [24], revenue sharing contract [8], quantity <sup>fl</sup>exibility contract [23], buy back contract [18], sales rebate contract [21], and price discount contract [4]). These contracts have been proven to be effective in improving operational performance of supply chain members under various problem backgrounds [7], whereas, the effectiveness of these contracts in mitigating bankruptcy risks in supply chains has yet been examined. Xu et al. [25] made a pioneering attempt to verify the effectiveness of two collaborative mechanisms in reducing the probability of bankruptcy occurrence at each stage of a supply chain. However, the occurrence of bankruptcy at each stage of a supply chain does not imply the tendency of bankruptcy propagation along the supply chain.

For a two-echelon supply chain network that consists of multiple manufacturers and retailers, the effectiveness of some typical contractual incentive schemes, including revenue sharing, price discount and quantity <sup>fl</sup>exibility contracts, in mitigating bankruptcy propagation is examined. Results of agent-based simulation reveal that: the three typical supply chain contracts are conditionally effective in mitigating bankruptcy propagation, whose effectiveness depends on the operational parameters of the supply chain. By comparing the optimal contract parameters with and without considering bankruptcy risks, it has also been found that, a set of contract parameters that can maximize the pro<sup>fi</sup>t of the supply chain may increase the occurrence of bankruptcy, leading to the phenomenon of a risk– pro<sup>fi</sup>t tradeoff.

Main contributions of this paper are two folds. First, an agentbased simulation model is built to investigate the relationship between supply chain contracts and the <sup>fi</sup>nancial status of <sup>fi</sup>rms in the supply chain network. Second, the effectiveness of some typical supply chain contracts in mitigating bankruptcy propagation is examined. Impacts of operational parameters on the effectiveness of these contracts are also investigated, which signi<sup>fi</sup>cantly contributes to the research of mitigating <sup>fi</sup>nancial risks of supply chains from the operational perspective.

The remainder of this paper is organized as follows. In Section 2, we brie<sup>fl</sup>y describe the supply chain model. In Section 3, some typical supply chain contracts are described. The simulation model is developed in Section 4. Effectiveness of supply chain contracts in mitigating bankruptcy propagation is examined in Section 5. Section 6 presents the conclusions.

## 2. The supply chain model

Consider a supply chain network consisting of $I \left( I { \geq } 1 \right)$ upstream manufacturers and $I \left( J { \ge } 1 \right)$ downstream retailers. The I manufacturers produce a single product to ful<sup>fi</sup>ll orders placed by the retailers, and the J retailers procure the product from the manufacturers to meet the market demand in discrete time periods $\cdot ( t = 1 , 2 , . . . , T )$ . Because J retailers sell the same product to the market, demand of each retailer depends not only on the retail price of itself, but also on the retail prices of other retailers. Denote by $\mathbf { p ^ { t } } { = } ( p _ { 1 } ^ { \ t } , p _ { 2 } ^ { \ t } { , . . . , p _ { j } ^ { \ t } } { , . . . , p _ { J } ^ { \ t } } )$ the price vector of J retailers in period t, and $d _ { j } ^ { . t } ( \pmb { \mathrm { p } } ^ { . } )$ the elastic demand of retailer j, we assume [4]

$$
d _ {j} ^ {t} = a _ {j} - b _ {j} \left(p _ {j} ^ {t} - \sum_ {l = 1, l \neq j} ^ {J} \theta_ {j l} p _ {l} ^ {t}\right)\tag{1}
$$

with $a _ { j } { > } 0$ and $b _ { j } > 0 .$ . Parameter $\theta _ { j l } \left( \theta _ { j l } \ge 0 \right.$ and $\sum _ { l = 1 , l \neq j } ^ { J } \theta _ { j l } { \le } 1 ; l , j , \in \{ 1 , 2 , \ldots J \}$ and $l \neq j )$ describes the degree of competition between retailer j and retailer l. The larger the value of $\theta _ { j l } ,$ the more intensive the competition between retailer j and retailer l [13]. The demand of retailer $\dot { } ( j = 1$ $2 , . . . , J )$ in period $t , D _ { j } ^ { t } ,$ is assumed to be of the additive form

$$
D _ {j} ^ {t} = d _ {j} ^ {t} + \varepsilon_ {j} ^ {t},\tag{2}
$$

where parameter ${ \varepsilon _ { j } } ^ { t }$ is a random term, which represents the uncertainty of the demand market.

## 2.1. Operation process of the supply chain

At the beginning of each period, retailers receive market demand, review their inventory positions of the product, and make procurement decisions about how much to order from their upstream manufacturers. Similarly, manufacturers receive orders from their downstream retailers at the beginning of each period, review their inventory positions of the material, and make procurement decisions about how much to order from the suppliers outside of the supply chain. In any period, if the realized demand of a supply chain member is larger than its on-hand inventory, the stockouts are backordered. To simplify the description of interactions between manufacturers and retailers in the operation processes, we make the following assumptions: (1) all manufacturers sell the product to the retailers at the same unit price $w ; ( 2 )$ different manufacturers (or retailers) have the same production (or replenishment) lead time of one period.

In period $t \left( t { = } 1 , 2 , . . . , T \right)$ , the sequence of events followed by supply chain member x $( x = i \mathrm { o r } j , i = 1 , 2 , . . . , I ; j = 1 , 2 , . . . , J )$ is outlined as follows:

(1) At the beginning of period t, member x reviews its inventory position and <sup>fi</sup>nancial situation, and decides how much to order from its immediate upstream members $( Q _ { x } ^ { ~ t } ) .$ . In case when the cash on hand of member x $( A _ { x } ^ { ~ t } )$ is insuf<sup>fi</sup>cient for product procurement, it can borrow ${ B _ { x } } ^ { t }$ from exogenous <sup>fi</sup>nancial institutions with a constant interest rate $r ( r > 0 )$

(2) Member x then receives products or materials $( I R _ { x } ^ { ~ t } )$ from its immediate upstream members, which was ordered at the beginning of period t or before period t (in case of backorders). If member x is a manufacturer, it receives materials from outside suppliers with ample raw material.

(3) At the end of period t, member x observes the realization of demand $( D _ { x } ^ { ~ t } )$ from its downstream members (or from the retail market). If $x = j ,$ , the realized demand of retailer j in period t, ${ D _ { j } } ^ { t } ,$ is described by Eq. $( 2 ) . \operatorname { I f } x = i ,$ the realized demand of manufacturer i in period $t , D _ { i } ^ { { t } } ,$ is the sum of the orders placed by all retailers to manufacturer i at the beginning of period t.

(4) Member x sells product to meet the demand, as well as backorders of the last period $( I B _ { x } ^ {  t - 1 } )$ if any, of its downstream members. The quantity of product that member x sells in period t, $I S _ { x } ^ { t }$ , is limited by its total demand $( D _ { x } { } ^ { t } + I B _ { x } { } ^ { t - 1 } )$ and its onhand inventory.

Note that when member x is the manufacturer $( x = i ) ,$ , it is possible that a manufacturer cannot meet its total demand. In this case, we assume that the manufacturer distributes the product to retailers in proportion to the total order quantities of retailers.

## 2.2. Order and financial decisions

In each period, a supply chain member makes operational and <sup>fi</sup>nancial decisions to determine the quantity of material (or product) to be ordered, and money to be borrowed from exogenous <sup>fi</sup>nancial institutions.

We assume linear cost functions of purchasing/selling, inventory holding and shortage penalty with the rates of $c _ { x } , h _ { x }$ and $s _ { x } ,$ respectively. We also assume a <sup>fi</sup>xed capital cost $F _ { x } ^ { ~ t }$ of member x in period t, which denotes the cost incurred by the purchase of land, buildings and equipment to be used in the production/selling of goods. Each member is assumed to make its ordering and borrowing decisions with the objective to maximize its own pro<sup>fi</sup>t. Denote by $\hat { \pi } _ { i } ^ { t }$ and $\hat { \pi } _ { j } ^ { t }$ the estimated pro<sup>fi</sup>ts of manufacturer i and retailer j in period t, respectively. Then we have

$$
\hat {\pi} _ {i} ^ {t} = (w - c _ {i}) \widehat {I S} _ {i} ^ {t} - r B _ {i} ^ {t} - F _ {i} ^ {t} - h _ {i} \widehat {I H} _ {i} ^ {t} - s _ {i} \widehat {I B} _ {i} ^ {t},\tag{3}
$$

$$
\hat {\pi} _ {j} ^ {t} = \left(p _ {j} ^ {t} - w - c _ {j}\right) \widehat {I S} _ {j} ^ {t} - r B _ {j} ^ {t} - F _ {j} ^ {t} - h _ {j} \widehat {I H} _ {j} ^ {t} - s _ {j} \widehat {I B} _ {j} ^ {t},\tag{4}
$$

with $\widehat { I S } _ { x } ^ { t } = \operatorname* { m i n } \Bigl \{ I R _ { x } ^ { t } + I H _ { x } ^ { t - 1 } , \hat { D } _ { x } ^ { t } + I B _ { x } ^ { t - 1 } \Bigr \} , \ : \ : \widehat { I H } _ { x } ^ { t } = \Bigl ( I R _ { x } ^ { t } + I H _ { x } ^ { t - 1 } - \widehat { I S } _ { x } ^ { t } \Bigr ) ^ { + }$ $\widehat { I B } _ { x } ^ { t } = \left( \hat { D } _ { x } ^ { t } + I B _ { x } ^ { t - 1 } - \widehat { I S } _ { x } ^ { t } \right) ^ { + }$ , and $\hat { D } _ { x } ^ { t }$ represents the forecasted demand of member x in period t.

We assume that each member uses an exponential smoothing method to forecast demand. Then

$$
\hat {D} _ {i} ^ {t} = \alpha_ {i} ^ {f} D _ {i} ^ {t - 1} + \left(1 - \alpha_ {i} ^ {f}\right) \hat {D} _ {i} ^ {t - 1},\tag{5}
$$

where $0 \leq \alpha _ { i } ^ { f } \leq 1$ denotes the smoothing constant of demand forecasting of manufacturer i.

Suppose that retail price of any retailer in period $t - 1$ is known by other $J { - } 1$ retailers at the end of period $t - 1$ . Thus the elastic demand of retailer j in period $t { - } 1 \ ( { d _ { i } } ^ { t - 1 } ( { \bf p } ^ { \mathrm { t - } 1 } ) ^ { \mathrm { \bullet } }$ ) can be computed at the end of period $t - 1$ according to $\operatorname { E q . } \ ( 3 )$ , and then the realized random demand in period $t - 1 \ ( \varepsilon _ { j } ^ { \ t - 1 } )$ can be computed at the end of period t−1 according to $\operatorname { E q . } \left( 2 \right)$ . Following the simple exponential smoothing method, the forecasted random demand in period $t , \hat { \varepsilon } _ { j } ^ { t } ,$ is

$$
\hat {\varepsilon} _ {j} ^ {t} = \alpha_ {j} ^ {f} \varepsilon_ {j} ^ {t - 1} + \left(1 - \alpha_ {j} ^ {f}\right) \hat {\varepsilon} _ {j} ^ {t - 1},\tag{6}
$$

where $\alpha _ { j } ^ { f } ( 0 \leq \alpha _ { j } ^ { f } \leq 1 )$ is the smoothing constant of demand forecast ing of retailer j.

At the beginning of period t, to determine $\hat { d } _ { j } ^ { t } ,$ , retailer j $( j = 1 , 2 , . . . , J )$ should determine ${ p _ { j } } ^ { t }$ at <sup>fi</sup>rst. Suppose that all retailers determine their retail prices to maximize their own pro<sup>fi</sup>ts, which is termed the “best response dynamic policy” in the related literature [3,19]. Denote by p $- \mathbf { j } ^ { \mathbf { t } - 1 }$ the retail-price vector of all J retailers except retailer j in period $t - 1 , \mathrm { i } . e . ,$ 1 $\mathbf { \widetilde { \mathbf { \Lambda } } } _ { \mathbf { - j } } \mathbf { \widetilde { \mathbf { \Lambda } } } ^ { \mathbf { t } - 1 } = \mathbf { \widetilde { ( } } p _ { 1 } ^ { \ t - 1 } , . . . , p _ { j - 1 } \mathbf { \widetilde { \Lambda } } ^ { t - 1 } , p _ { j + 1 } \mathbf { \widetilde { \Lambda } } ^ { t - 1 } , . . . , \mathbf { \widetilde { \mathbf { p } } } _ { J } ^ { t - 1 } )$ . According to the “best response dynamic policy”, retailer j determines a retail price at the beginning of period $t , p _ { j } ^ { . t } ,$ , and estimates the elastic demand $\hat { d } _ { j } ^ { t }$ based on ${ p _ { j } } ^ { t }$ and $\bar { \mathbf { p } _ { - \mathbf { j } } } ^ { \mathbf { t } - \mathbf { \hat { 1 } } }$ . Then we have

$$
\hat {d} _ {j} ^ {t} \left(p _ {j} ^ {t}, \mathbf {p} _ {- \mathbf {j}} ^ {\mathbf {t} - \mathbf {1}}\right) = a _ {j} - b _ {j} \left(p _ {j} ^ {t} - \sum_ {l = 1, l \neq j} ^ {J} \theta_ {j l} p _ {l} ^ {t - 1}\right),\tag{7}
$$

In Eq. $( 7 ) , \hat { d } _ { j } ^ { t } \Big ( p _ { j } ^ { t } , \mathbf { p } _ { - \mathbf { j } } ^ { \mathbf { t } - 1 } \Big )$ indicates that $\hat { d } _ { j } ^ { t }$ is a function of ${ p _ { j } } ^ { t }$ and p<sub>−</sub> $\mathbf { - j } ^ { \mathbf { t } - 1 }$

After retailer j has determined total order quantity in period $t \left( Q _ { j } ^ { ~ t } \right)$ , a followed decision is to split the total order quantity among manufacturers. We assume that order of a retailer is allocated to manufacturers according to their service levels in the previous periods. Denote by ${ \chi _ { j i } } ^ { t } \left( 0 \le \chi _ { j i } ^ { { \mathrm { ~ } } t } \le 1 \right)$ the proportion of orders allocated by retailer j to manufacturer i in period t. Then the order quantity received by manufacturer i from retailer j is ${ Q _ { j i } } ^ { t } { = } { \chi _ { j i } } ^ { t } { Q _ { j } } ^ { t }$ . Denote by ${ \gamma _ { i j } } ^ { t }$ ${ ( 0 \leq \gamma _ { i j } } ^ { t } \leq 1 )$ ) the percentage of the allocated order of retailer j to manufacturer $i \ ( \mathrm { i . e . , } \ \chi _ { j i } { } ^ { t } Q _ { j } ^ { \ t } )$ ful<sup>fi</sup>lled by manufacturer i in period t, and de<sup>fi</sup>ne ${ \gamma _ { i j } } ^ { t }$ as the service level of manufacturer i perceived by retailer j in period t. Then, for all $t \geq 1$

$$
\chi_ {j i} ^ {t + 1} = \alpha_ {j} ^ {O A} \gamma_ {i j} ^ {t} \chi_ {j i} ^ {t} \Big / \sum_ {i = 1} ^ {I} \gamma_ {i j} ^ {t} \chi_ {j i} ^ {t} + \left(1 - \alpha_ {j} ^ {O A}\right) \chi_ {j i} ^ {t},\tag{8}
$$

where $\alpha _ { j } ^ { O A } ( 0 \leq \alpha _ { j } ^ { O A } \leq 1 )$ is the smoothing factor of order allocation of retailer j, and the superscript OA denotes order allocation. $\chi _ { j i } { } ^ { 1 } = 1 / I$ for all i and j.

## 2.3. Profits, cash flow and bankruptcy

According to the operation process of the supply chain, the pro<sup>fi</sup>t and net cash in<sup>fl</sup>ow of retailer ${ j \ ( j = 1 , 2 , . . . , J ) }$ at the end of period t, $\pi _ { j } ^ { \ : t }$ and ${ v _ { j } } ^ { t }$ , are calculated by

$$
\pi_ {j} ^ {t} = \left(p _ {j} ^ {t} - w - c _ {j}\right) I S _ {j} ^ {t} - r B _ {j} ^ {t} - F _ {j} ^ {t} - h _ {j} I H _ {j} ^ {t} - s _ {j} I B _ {j} ^ {t} + \sum_ {i = 1} ^ {I} s _ {i} I B _ {i j} ^ {t},\tag{9}
$$

$$
\boldsymbol {v} _ {j} ^ {t} = p _ {j} ^ {t} I S _ {j} ^ {t} - \left(w + c _ {j}\right) I R _ {j} ^ {t} - r B _ {j} ^ {t} - F _ {j} ^ {t} - h _ {j} I H _ {j} ^ {t} - s _ {j} I B _ {j} ^ {t} + \sum_ {i = 1} ^ {I} s _ {i} I B _ {i j} ^ {t}.\tag{10}
$$

Similarly, the pro<sup>fi</sup>t and net cash in<sup>fl</sup>ow of manufacturer i $( i = 1 , 2 ,$ $\ldots , I )$ at the end of period t, π <sup>t</sup> and $v _ { i } ^ { { t } } ,$ , are calculated by

$$
\pi_ {i} ^ {t} = (w - c _ {i}) I S _ {i} ^ {t} - r B _ {i} ^ {t} - F _ {i} ^ {t} - h _ {i} I H _ {i} ^ {t} - s _ {i} I B _ {i} ^ {t} - B D _ {i} ^ {t},\tag{11}
$$

$$
v _ {i} ^ {t} = w I S _ {i} ^ {t} - c _ {i} I R _ {i} ^ {t} - r B _ {i} ^ {t} - F _ {i} ^ {t} - h _ {i} I H _ {i} ^ {t} - s _ {i} I B _ {i} ^ {t} - B D _ {i} ^ {t}.\tag{12}
$$

The net assets of member x at the end of period t is assumed to include three parts: cash on hand $( A _ { x } ^ { ~ t } )$ , overstock inventory $( c _ { x } I H _ { x } ^ { ~ t } )$ and long-term investment $( { \eta _ { x } } ^ { t } )$ . Long-term investment of member x is the investment of the member on other products or projects. We assume that, if ${ \pi _ { x } } ^ { t } \mathrm { > } 0$ , then a proportion $\delta _ { x } ~ ( 0 \leq \delta _ { x } \leq 1 )$ of the pro<sup>fi</sup>t of member x at the end of period $t , \pi _ { x } ^ { \ t } ,$ is retained to increase its net assets; otherwise, a negative pro<sup>fi</sup>t directly decreases its net assets. Then the updating process of the net assets of member x at the end of period t can be formulated as

$$
A _ {x} ^ {t} + c _ {x} I H _ {x} ^ {t} + \eta_ {x} ^ {t} = \left\{ \begin{array}{l l} \delta_ {x} \pi_ {x} ^ {t} + A _ {x} ^ {t - 1} + c _ {x} I H _ {x} ^ {t - 1} + u _ {x} ^ {\eta} \eta_ {x} ^ {t - 1}, & \text { if } \pi_ {x} ^ {t} > 0 \\ \pi_ {x} ^ {t} + A _ {x} ^ {t - 1} + c _ {x} I H _ {x} ^ {t - 1} + u _ {x} ^ {\eta} \eta_ {x} ^ {t - 1}, & \text { otherwise } \end{array} \right.,\tag{13}
$$

where ${ u _ { x } } ^ { \eta }$ is a random variable which represents the return uncertainty of the long-term investment of member x in each period.

The net cash in<sup>fl</sup>ow of member x in each period could increase or decrease its cash on hand. We assume that if the net cash in<sup>fl</sup>ow of member x in period $\mathbf { \nabla } \cdot \left( v _ { x } ^ { \phantom { } } \right)$ plus its cash on hand at the end of period $t - 1 ( A _ { x } ^ { \ t - 1 } )$ is smaller than $\overset { \vartriangle } { \boldsymbol { A } _ { \boldsymbol { x } } : \boldsymbol { \mathbf { \ell } } }$ , then the cash on hand of member x at the end of period t $( A _ { x } ^ { ~ t } )$ equals the sum of ${ v _ { x } } ^ { t }$ and $A _ { x } ^ { t - 1 } ;$ otherwise, ${ A _ { x } } ^ { t }$ is set at the level of $A _ { x } ^ { \bar { 0 } }$ , and the rest part of the net cash in<sup>fl</sup>ow is used as long-term investment. That is,

$$
A _ {x} ^ {t} = \min \left\{A _ {x} ^ {t - 1} + v _ {x} ^ {t}, A _ {x} ^ {0} \right\},\tag{14}
$$

$$
\text { and } \eta_ {x} ^ {t} = \left\{ \begin{array}{l l} u _ {x} ^ {\eta} \eta_ {x} ^ {t - 1} + \left(A _ {x} ^ {t - 1} + v _ {x} ^ {t} - A _ {x} ^ {0}\right) ^ {+} - (1 - \delta_ {x}) \pi_ {x} ^ {t}, & \text { if } \pi_ {x} ^ {t} > 0 \\ u _ {x} ^ {\eta} \eta_ {x} ^ {t - 1} + \left(A _ {x} ^ {t - 1} + v _ {x} ^ {t} - A _ {x} ^ {0}\right) ^ {+}, & \text { otherwise } \end{array} \right..\tag{15}
$$

In Eq. $( 1 5 ) , ( 1 - \delta _ { x } ) \pi _ { x } ^ { \phantom { } t }$ is the dividends distributed by member x at the end of period t.

Member x is de<sup>fi</sup>ned to fall into the state of financial distress at the end of period t if its cash on hand becomes negative at the end of this period, i.e., $A _ { x } ^ { ~ t } { < } 0$ . Once a <sup>fi</sup>rm falls into <sup>fi</sup>nancial distress at the end of period t, a <sup>fi</sup>nancial cost ${ C _ { x } } ^ { t }$ is incurred, which is determined by its total assets and its <sup>fi</sup>nancial leverage. Speci<sup>fi</sup>cally, we assume

$$
C _ {x} ^ {t} = \left\{ \begin{array}{l l} \lambda e ^ {2 l e v _ {x} ^ {t}} \Big (B _ {x} ^ {t} + A _ {x} ^ {t} + c _ {x} I H _ {x} ^ {t} + \eta_ {x} ^ {t} \Big), & i f \mathrm{FD} _ {x} ^ {t} = t r u e \\ 0, & o t h e r w i s e \end{array} \right.,\tag{16}
$$

where parameter λ $( 0 \leq \lambda \leq 1 )$ is the <sup>fi</sup>nancial distress cost rate, ${ l e { v _ { x } } ^ { t } }$ is the <sup>fi</sup>nancial leverage of member x at the end of period t, and FD-$_ x ^ { t } = t r u e$ represents that member x falls into <sup>fi</sup>nancial distress at the end of period t.

We assume that manufacturers offer a two-period payment policy for retailers. That is, retailer j pays a proportion ϕ<sub>j</sub> $( 0 \leq \phi _ { j } \leq 1 )$ of payment to manufacturers at the beginning of period t when the orders is placed, and gives the rest proportion $( 1 - \phi _ { j } )$ of payment to manufacturers at the end of period t. Once a retailer falls into <sup>fi</sup>nancial distress at the end of period t, the retailer can still place orders to manufacturers at the beginning of period $t + 1$ , but need to pay for all its orders when the orders are placed.

Member x is de<sup>fi</sup>ned to be bankrupt at the end of period t if its net assets falls below zero at the end of the period, i.e., ${ A _ { x } } ^ { t } + c _ { x } I { H _ { x } } ^ { t } + { \eta _ { x } } ^ { t }$ $- { C _ { x } } ^ { t } { < } 0 .$ . Once a <sup>fi</sup>rm goes bankruptcy at the end of period t, it gives no-payment to its upstream members at the end of the period, and will stop supplying its downstream members (or market demands) in the next period. So the bad debt of manufacturer i in period t caused by retailers' bankruptcies is $B D _ { i } ^ { t } = w \sum _ { i = 1 } ^ { J } \left( I R _ { j i } ^ { t } { - } f \Bigl ( \phi _ { j } \Bigr )  Q _ { j i } ^ { t } \right) ^ { + }$ sgn<sup>t</sup>, where $\mathrm { s g n } _ { j } ^ { t }$ equals 1 if retailer j goes bankruptcy at the end of period t and equals 0 otherwise. Parameter $f ( \phi _ { j } )$ equals 1 when retailer j falls into <sup>fi</sup>nancial distress at the end of period t−1 and equals ϕ $( \phi _ { j } < 1 )$ ) otherwise. The bankrupt <sup>fi</sup>rm is assumed to be replaced by a new <sup>fi</sup>rm at the beginning of the next period. For a newly entered retailer, it has to establish links with upstream manufacturers. We assume the probability that a newly entered retailer $j \left( 1 \leq j \leq J \right)$ establishes a link with manufacturer $( i = 1 , 2 , . . . , I ) , P \{ L _ { i j } = 1 \}$ , is a random variable on the support of [0,1]. Parameter L<sub>ij</sub> equals 1 if there is a link between retailer j establishes a link with manufacturer i, and 0 otherwise.

## 3. Typical supply chain contracts

Researches in supply chain management have developed numerous types of supply chain contracts. These contracts have been proved to be effective in improving operational performance of supply chain under various problem backgrounds. With the objective to coordinate the operations of member <sup>fi</sup>rms in the supply chain that consists of multiple competing retailers, we choose three typical contracts: revenue sharing, price discount and quantity flexibility. Next, we brie<sup>fl</sup>y characterize these contracts in the context of a simple two-stage supply chain (an upstream manufacturer and some downstream retailers).

1) Revenue sharing contract (abbreviated as RS hereafter). Revenue sharing contract is a supply chain contract in which the manufacturer charges low wholesale price to the retailer and shares a fraction of revenue generated by the retailer. For a general supply chain model with revenues determined by each retailer's purchase quantity and price, RS can coordinate the supply chain with retailers competing in quantities [8].

2) Price discount contract (abbreviated as PD hereafter). The payment arrangement that the manufacturer commits to adjust the buyback and wholesale price in response to any price chosen by the retailer is termed a PD contract [4]. Under an endogenously determined retail price, PD contract can coordinate the supply chain that demand of a retailer depends on its own price as well as those of the other competing retailers [4].

3) Quantity flexibility contract (abbreviated as QF hereafter). To reconcile manufacturing/procurement time lags with a need for timely response to the uncertain market, supply chains often must commit resources to production quantities based on forecasted rather than realized demand. The QF contract can couple the retailer's commitment to purchase no less than a certain percentage below the forecast with the manufacturer's guarantee to deliver up to a certain percentage above [23].

To examine the potential of these contracts in mitigating bankruptcy propagation, we <sup>fi</sup>rst describe the operations and decisions of supply chain members under these contracts. Since the operation process under different contracts is essentially the same as those described in Section 2, we then describe these contracts by simply illustrating the impacts of these contracts on the decisions of supply chain members, pro<sup>fi</sup>ts and cash <sup>fl</sup>ows.

## 3.1. Revenue sharing contract

A RS contract can be speci<sup>fi</sup>ed by two parameter $, \tau ^ { \mathrm { R S } }$ and $\xi ^ { { \tt R S } } .$ . That is, in each period, retailer j pays manufacturer i a wholesale price $\tau ^ { \mathrm { R } S } w$ $( 0 \leq \tau ^ { \mathrm { R S < 1 } } )$ for each unit purchased from manufacturer i plus a percentage $\xi ^ { \dot { \mathrm { R S } } } \left( 0 { < } \xi ^ { \mathrm { R S } } { \le } 1 \right)$ of the revenue it generates from the product that is received from manufacturer i. Following Cachon and Lariviere [8], we assume that the revenue shared by retailers to manufacturers is computed based on a constant retail price, i.e., the retail price of retailers in period 1, i.e., ${ p _ { j } } ^ { 1 } ( j = 1 , 2 , . . . , J ) .$ . For simplicity, we assume that all retailers' retail prices in period 1 equal to $p ^ { 0 } , \mathrm { i } . \mathrm { e } . , { p _ { 1 } } ^ { 1 } = . . . =$ ${ p _ { j } } ^ { 1 } { = } { \bf . . . } { = } { p _ { J } } ^ { 1 } { = } { p ^ { 0 } } .$

At the beginning of period t, manufacturer i determines its order quantity ${ Q _ { i } } ^ { t , { \widetilde { \mathrm { R S } } } }$ to maximize its estimated pro<sup>fi</sup>t in period t,

$$
\hat {\pi} _ {i} ^ {t, \mathrm{RS}} = \left(\xi^ {\mathrm{RS}} p ^ {o} + \tau^ {\mathrm{RS}} w - c _ {i}\right) \widehat {I S} _ {i} ^ {t, \mathrm{RS}} - r B _ {i} ^ {t, \mathrm{RS}} - F _ {i} ^ {t} - h _ {i} \widehat {I H} _ {i} ^ {t, \mathrm{RS}} - s _ {i} \widehat {I B} _ {i} ^ {t, \mathrm{RS}}.\tag{17}
$$

Similarly, retailer j determines its retail price $p _ { j } ^ { { t , \mathrm { R S } } }$ and order quantity $Q _ { j } ^ { t , \mathrm { R S } }$ to maximize its estimated pro<sup>fi</sup>t in period t,

$$
\hat {\pi} _ {j} ^ {t, \mathrm{RS}} = \left(p _ {j} ^ {t, \mathrm{RS}} - \xi^ {\mathrm{RS}} p ^ {o} - \tau^ {\mathrm{RS}} w - c _ {j}\right) \widehat {I S} _ {j} ^ {t, \mathrm{RS}} - r B _ {j} ^ {t, \mathrm{RS}} - F _ {j} ^ {t} - h _ {j} \widehat {I H} _ {j} ^ {t, \mathrm{RS}} - s _ {j} \widehat {I B} _ {j} ^ {t, \mathrm{RS}}.\tag{18}
$$

The pro<sup>fi</sup>t and net cash in<sup>fl</sup>ow of retailer j and manufacturer i in period t can be computed as

$$
\begin{array}{l} \pi_ {j} ^ {t, \mathrm{RS}} = \Big (p _ {j} ^ {t, \mathrm{RS}} - \xi^ {\mathrm{RS}} p ^ {0} - \tau^ {\mathrm{RS}} w - c _ {j} \Big) I S _ {j} ^ {t, \mathrm{RS}} - r B _ {j} ^ {t, \mathrm{RS}} - F _ {j} ^ {t} - h _ {j} I H _ {j} ^ {t, \mathrm{RS}} - s _ {j} I B _ {j} ^ {t, \mathrm{RS}} \\ + \sum_ {i = 1} ^ {I} s _ {i} I B _ {i j} ^ {t, \mathrm{RS}}, \end{array}\tag{19}
$$

$$
\pi_ {i} ^ {t, \mathrm{RS}} = \left(\xi^ {\mathrm{RS}} p ^ {0} + \tau^ {\mathrm{RS}} w - c _ {i}\right) I S _ {i} ^ {t, \mathrm{RS}} - r B _ {i} ^ {t, \mathrm{RS}} - F _ {i} ^ {t} - h _ {i} I H _ {i} ^ {t, \mathrm{RS}} - s _ {i} I B _ {i} ^ {t, \mathrm{RS}} - B D _ {i} ^ {t, \mathrm{RS}},\tag{20}
$$

$$
\begin{array}{c} v _ {j} ^ {t, \mathrm{RS}} = p _ {j} ^ {t, \mathrm{RS}} I S _ {j} ^ {t, \mathrm{RS}} - \xi^ {\mathrm{RS}} p ^ {0} I S _ {j} ^ {t, \mathrm{RS}} - \left(\tau^ {\mathrm{RS}} w + c _ {j}\right) I R _ {j} ^ {t, \mathrm{RS}} \\ - r B _ {j} ^ {t, \mathrm{RS}} - F _ {j} ^ {t} - h _ {j} I H _ {j} ^ {t, \mathrm{RS}} - s _ {j} I B _ {j} ^ {t, \mathrm{RS}} + \sum_ {i = 1} ^ {I} s _ {i} I B _ {i j} ^ {t, \mathrm{RS}}, \end{array}\tag{21}
$$

$$
\begin{array}{l} v _ {i} ^ {t, \mathrm{RS}} = \xi^ {\mathrm{RS}} p ^ {0} \sum_ {j = 1} ^ {J} \varphi_ {j i} ^ {t, \mathrm{RS}} I S _ {j} ^ {t, \mathrm{RS}} + \tau^ {\mathrm{RS}} w I S _ {i} ^ {t, \mathrm{RS}} - c _ {i} I R _ {i} ^ {t, \mathrm{RS}} - r B _ {i} ^ {t, \mathrm{RS}} - F _ {i} ^ {t} \\ - h _ {i} I H _ {i} ^ {t, \mathrm{RS}} - s _ {i} I B _ {i} ^ {t, \mathrm{RS}} - B D _ {i} ^ {t, \mathrm{RS}}. \end{array}\tag{22}
$$

In Eq. (22), $\begin{array} { r } { \varphi _ { j i } ^ { t , \mathrm { R S } } = \frac { \varphi _ { j i } ^ { t - 1 , \mathrm { R S } } I H _ { j } ^ { t - 1 , \mathrm { R S } } + I R _ { j i } ^ { t , \mathrm { R S } } } { I H _ { i } ^ { t - 1 , \mathrm { R S } } + I R _ { i } ^ { t , \mathrm { R S } } } } \end{array}$ is the proportion of product quantity that is procured from manufacturer i and sold by retailer j in period t.

## 3.2. Price discount contract

We assume that different manufacturers provide retailer j the same linear PD contract in each period. That is, the wholesale price given to retailer j is a linear function of the retail price of retailer j, $w ^ { t , \mathrm { P D } } = \tau ^ { \mathrm { P D } } \frac { 1 } { J } \sum _ { i = 1 } ^ { J } p _ { j } ^ { t - 1 , \mathrm { P D } } + ( 1 - \tau ^ { \mathrm { P D } } ) c ^ { 0 } ,$ , and $c ^ { 0 }$ is the base of unit production cost. The PD contract is combined with a traditional buy-back arrangement, and the buy-back rate given to retailer j is a linear function of the wholesale price, $\begin{array} { r } { \Delta ^ { t , \mathrm { P D } } = \xi ^ { \mathrm { \check { P D } } } w ^ { t , \mathrm { P D } } + ( 1 - \xi ^ { \mathrm { \check { P D } } } ) c ^ { 0 } } \end{array}$

At the beginning of period t, manufacturer i determines its order quantity $Q _ { i } ^ { t , \breve { \mathrm { P D } } }$ to maximize its estimated pro<sup>fi</sup>t in period t,

$$
\hat {\pi} _ {i} ^ {t, \mathrm{PD}} = \left(w ^ {t, \mathrm{PD}} - c _ {i}\right) \widehat {I S} _ {i} ^ {t, \mathrm{PD}} - r B _ {i} ^ {t, \mathrm{PD}} - F _ {i} ^ {t} - h _ {i} \widehat {I H} _ {i} ^ {t, \mathrm{PD}} - s _ {i} \widehat {I B} _ {i} ^ {t, \mathrm{PD}}.\tag{23}
$$

Similarly, retailer $j$ determines its retail price $p _ { j } ^ { { t , \mathrm { P D } } }$ and order quantity $Q _ { j } ^ { \mathsf { \bar { t } } , \mathsf { P D } }$ to maximize its estimated pro<sup>fi</sup>t in period t,

$$
\begin{array}{c} \hat {\pi} _ {j} ^ {t, \mathrm{PD}} = \Big (p _ {j} ^ {t, \mathrm{PD}} - w ^ {t, \mathrm{PD}} - c _ {j} \Big) \widehat {I S} _ {j} ^ {t, \mathrm{PD}} - r B _ {j} ^ {t, \mathrm{PD}} - F _ {j} ^ {t} \\ - \Big (w _ {j} ^ {t, \mathrm{PD}} - \varDelta_ {j} ^ {t, \mathrm{PD}} \Big) \widehat {I H} _ {j} ^ {t, \mathrm{PD}} - s _ {j} \widehat {I B} _ {j} ^ {t, \mathrm{PD}}. \end{array}\tag{24}
$$

The pro<sup>fi</sup>t and net cash in<sup>fl</sup>ow of retailer j and manufacturer i in period t can be computed as

$$
\begin{array}{l} \pi_ {j} ^ {t, \mathrm{PD}} = \Big (p _ {j} ^ {t, \mathrm{PD}} - w ^ {t, \mathrm{PD}} - c _ {j} \Big) I S _ {j} ^ {t, \mathrm{PD}} - r B _ {j} ^ {t, \mathrm{PD}} - F _ {j} ^ {t} - \Big (w _ {j} ^ {t, \mathrm{PD}} - \Delta_ {j} ^ {t, \mathrm{PD}} \Big) I H _ {j} ^ {t, \mathrm{PD}} \\ \qquad - s _ {j} I B _ {j} ^ {t, \mathrm{PD}} + \sum_ {i = 1} ^ {I} s _ {i} I B _ {i j} ^ {t, \mathrm{PD}}, \end{array}\tag{25}
$$

$$
\begin{array}{l} \pi_ {i} ^ {t, \mathrm{PD}} = \Big (w ^ {t, \mathrm{PD}} - c _ {i} \Big) I S _ {i} ^ {t, \mathrm{PD}} - r B _ {i} ^ {t, \mathrm{PD}} - F _ {i} ^ {t} - h _ {i} I H _ {i} ^ {t, \mathrm{PD}} - b _ {i} I B _ {i} ^ {t, \mathrm{PD}} - B D _ {i} ^ {t, \mathrm{PD}} \\ \qquad - \Big (\varDelta^ {t, \mathrm{PD}} - c _ {i} \Big) \sum_ {j = 1} ^ {J} \varphi_ {j i} ^ {t, \mathrm{PD}} I H _ {j} ^ {t, \mathrm{PD}}, \end{array}\tag{26}
$$

$$
\begin{array}{c} v _ {j} ^ {t, \mathrm{PD}} = p _ {j} ^ {t, \mathrm{PD}} I S _ {j} ^ {t, \mathrm{PD}} - \Big (w ^ {t, \mathrm{PD}} + c _ {j} \Big) I R _ {j} ^ {t, \mathrm{PD}} - r B _ {j} ^ {t, \mathrm{PD}} - F _ {j} ^ {t} - s _ {j} I B _ {j} ^ {t, \mathrm{PD}} \\ + \sum_ {i = 1} ^ {I} s _ {i} I B _ {i j} ^ {t, \mathrm{PD}} + \varDelta_ {j} ^ {t, \mathrm{PD}} I H _ {j} ^ {t, \mathrm{PD}}, \end{array}\tag{27}
$$

$$
\begin{array}{c} v _ {i} ^ {t, \mathrm{PD}} = w ^ {t, \mathrm{PD}} I S _ {i} ^ {t, \mathrm{PD}} - c _ {i} I R _ {i} ^ {t, \mathrm{PD}} - r B _ {i} ^ {t, \mathrm{PD}} - F _ {i} ^ {t} - h _ {i} I H _ {i} ^ {t, \mathrm{PD}} - s _ {i} I B _ {i} ^ {t, \mathrm{PD}} \\ - B D _ {i} ^ {t, \mathrm{PD}} - \sum_ {j = 1} ^ {J} \Delta_ {j} ^ {t, \mathrm{PD}} \varphi_ {j i} ^ {t, \mathrm{PD}} I H _ {j} ^ {t, \mathrm{PD}}. \end{array}\tag{28}
$$

At the end of period t, the on-hand inventory of supply chain members under the PD contract are updated as follows: $\bar { I } \bar { H _ { j } } ^ { t , \mathrm { P D } } = 0$ and $I H _ { i } ^ { t , \mathrm { P D } } = I H _ { i } ^ { t , \mathrm { P D } } + \sum _ { j = 1 } ^ { J } \varphi _ { j i } ^ { t , \mathrm { P D } } I H _ { j } ^ { t , \mathrm { P D } }$

## 3.3. Quantity flexibility contract

With QF contract, a manufacturer charges a wholesale price per unit the retailer purchased but compensates the retailer for his losses on unsold units. Denote by $I H _ { j i } { } ^ { t , \mathrm { Q F } }$ the on-hand inventory of retailer j at the end of period t that are procured from manufacturer i. A QF contract can be speci<sup>fi</sup>ed by two parameters, $\tau ^ { \mathrm { Q F } }$ and $\xi ^ { \mathrm { Q F } }$ . Under this contract, manufacturer i charges a wholesale price $\tau ^ { \mathrm { Q F } } w \left( \tau ^ { \mathrm { Q F } } \geq 1 \right)$ for each unit retailer j purchased, and refunds retailer j up to $\xi ^ { \mathrm { Q F } } I H _ { j i } ^ { \ t , \mathrm { Q F } }$ at the end of period $t , x ^ { \mathrm { Q F } } \in [ 0 , 1 )$

At the beginning of period t, manufacturer i determines its order quantity $Q _ { i } ^ { t , \breve { \mathrm { Q F } } }$ to maximize its estimated pro<sup>fi</sup>t in period t,

$$
\begin{array}{c} \hat {\pi} _ {i} ^ {t, \mathrm{QF}} = \left(\tau^ {\mathrm{QF}} w - c _ {i}\right) \widehat {I S} _ {i} ^ {t, \mathrm{QF}} - r B _ {i} ^ {t, \mathrm{QF}} - F _ {i} ^ {t} - h _ {i} \widehat {I H} _ {i} ^ {t, \mathrm{QF}} - s _ {i} \widehat {I B} _ {i} ^ {t, \mathrm{QF}} \\ - \tau^ {\mathrm{QF}} w \xi^ {\mathrm{QF}} \sum_ {j = 1} ^ {J} \widehat {I H} _ {j i} ^ {\mathrm{QF}}, \end{array}\tag{29}
$$

Retailer j determines its retail price $p _ { j } ^ { { t , \mathrm { Q F } } }$ and order quantity $Q _ { j } ^ { t , \mathrm { Q F } }$ to maximize its estimated pro<sup>fi</sup>t in period t,

$$
\begin{array}{l} \tilde {\pi} _ {j} ^ {t, \mathrm{QF}} = \Big (p _ {j} ^ {t, \mathrm{QF}} - \tau^ {\mathrm{QF}} w - c _ {j} \Big) \widehat {I S} _ {j} ^ {t}, \mathrm{QF} - r B _ {j} ^ {t, \mathrm{QF}} - F _ {j} ^ {t} - h _ {j} \widehat {I H} _ {j} ^ {t, \mathrm{QF}} - s _ {j} \widehat {I B} _ {j} ^ {t, \mathrm{QF}} \\ + \tau^ {\mathrm{QF}} w \xi^ {\mathrm{QF}} \widehat {I H} _ {j} ^ {t, \mathrm{QF}}. \end{array}\tag{30}
$$

The pro<sup>fi</sup>t and net cash in<sup>fl</sup>ow of retailer j and manufacturer i in period t can be computed as

<sub>ð</sub><sup>31</sup><sub>Þ</sub>

$$
\begin{array}{c} \pi_ {i} ^ {t, \mathrm{QF}} = \left(\tau^ {\mathrm{QF}} w - c _ {i}\right) I S _ {i} ^ {t, \mathrm{QF}} - r B _ {i} ^ {t, \mathrm{QF}} - F _ {i} ^ {t} - h _ {i} I H _ {i} ^ {t, \mathrm{QF}} - s _ {i} I B _ {i} ^ {t, \mathrm{QF}} - B D _ {i} ^ {t, \mathrm{QF}} \\ - \tau^ {\mathrm{QF}} w \xi^ {\mathrm{QF}} \sum_ {j = 1} ^ {J} I H _ {j i} ^ {t, \mathrm{QF}}, \end{array}\tag{32}
$$

$$
\begin{array}{c} v _ {j} ^ {t, \mathrm{QF}} = p _ {j} ^ {t, \mathrm{QF}} I S _ {j} ^ {t, \mathrm{QF}} - \Big (\tau^ {\mathrm{QF}} w + c _ {j} \Big) I R _ {j} ^ {t, \mathrm{QF}} - r B _ {j} ^ {t, \mathrm{QF}} - F _ {j} ^ {t} \\ - h _ {j} I H _ {j} ^ {t, \mathrm{QF}} - s _ {j} I B _ {j} ^ {t, \mathrm{QF}} + \sum_ {i = 1} ^ {I} s _ {i} I B _ {i j} ^ {t, \mathrm{QF}} + \tau^ {\mathrm{QF}} w \xi^ {\mathrm{QF}} I H _ {j} ^ {t, \mathrm{QF}}, \end{array}\tag{33}
$$

$$
\begin{array}{c} v _ {i} ^ {t, \mathrm{QF}} = \tau^ {\mathrm{QF}} w I S _ {i} ^ {t, \mathrm{QF}} - c _ {i} I R _ {i} ^ {t, \mathrm{QF}} - r B _ {i} ^ {t, \mathrm{QF}} - F _ {i} ^ {t} - h _ {i} I H _ {i} ^ {t, \mathrm{QF}} - s _ {i} I B _ {i} ^ {t, \mathrm{QF}} - B D _ {i} ^ {t, \mathrm{QF}} \\ - \tau^ {\mathrm{QF}} w \xi^ {\mathrm{QF}} \sum_ {j = 1} ^ {J} I H _ {j i} ^ {t, \mathrm{QF}}. \end{array}\tag{34}
$$

## 3.4. Properties of the three contracts

In this subsection, we make some analyses on the properties of the three contracts to observe their potential in mitigating bankruptcy risks. Based on the de<sup>fi</sup>nitions of <sup>fi</sup>nancial distress and bankruptcy in Subsection 2.3, we have the following observations.

Lemma 1. When $A _ { x } ^ { ~ 0 } \to + \infty$ , the bankruptcy probability of firm x in period t decreases in the value of its net cash inflow in period $t ( v _ { x } ^ { ~ t } )$ , but increases in the value of its debt in period t $ { \mathbf { \ddot { \rho } } } ( B _ { x } ^ { \ t } )$

Proofs of Lemma 1 and the subsequent propositions can be found in Appendix A.

Lemma 1 demonstrates the relationship between the bankruptcy probability of <sup>fi</sup>rm x and its <sup>fi</sup>nancial indicators. Following Lemma 1 we can conclude that, the <sup>fi</sup>nancial indicator ${ v _ { x } } ^ { t } / { B _ { x } } ^ { t }$ re<sup>fl</sup>ects the capability of <sup>fi</sup>rm x in hedging bankruptcy risk in period t. That ${ \mathrm { i } } s ,$ the higher the value of ${ v _ { x } } ^ { t } / { B _ { x } } ^ { t }$ , the lower the bankruptcy probability of <sup>fi</sup>rm x in period $t ,$ and vice versa.

Next, we further examine the impact of incentive contracts (RS, PD and QF) on member <sup>fi</sup>rms' <sup>fi</sup>nancial indicators. For the simplicity of analyses, the following assumptions are made: (1) we consider a simple supply chain with one manufacturer (manufacturer i) and two retailers (retailer j and $l , j \neq l ) ; ( 2 )$ there is no random demand, inventory holding cost, shortage penalty cost, <sup>fi</sup>xed cost or interest rate $( { \varepsilon _ { j } } ^ { t } = { \varepsilon _ { l } } ^ { t } = h _ { x } = { s _ { x } } = { F _ { x } } ^ { t } = r = 0 , x = i , j \mathrm { o r } l ) ; ( 3 )$ there is no cash on hand, surplus inventory or backorder at the end of period t−1 $( { A _ { x } } ^ { t - 1 } { = } I { H _ { x } } ^ { t - 1 } { = } I { B _ { x } } ^ { t - 1 } { = } 0 )$ ; (4) the retail price of retailer j in period t−1 equals to that of retailer l in period $\stackrel { \cdot } { t } - 1 ( { p _ { j } } ^ { t - 1 } = { p _ { l } } ^ { t - 1 } ) ;$

(5) each retailer's selling cost is zero but is its private information $( { c _ { i } } ^ { t } { = } { c _ { l } } ^ { t } { = } 0 ) ;$ ; and (6) the manufacturer can exactly meet its demand $( \bar { Q } _ { i } ^ { \ t } { = } Q _ { j } ^ { \ t } { + } Q _ { l } ^ { \ t } )$ . Based on the above assumptions and Eq. (10) we can see that, if a retailer sells out its inventory in period t, then its net cash in<sup>fl</sup>ow in this period is positive and it will not fall into <sup>fi</sup>nancial distress, as a result, the risk of bankruptcy at the retailer is low. In the following analyses, we just consider the case that the retailer cannot sell out its inventory in period t (i.e., $Q _ { j } ^ { t } { > } D _ { j } ^ { t } )$

Let Pr{y} represents the probability of event $y ,$ and $P B _ { j } { } ^ { t } { = } t r u e$ represents that retailerj goes bankruptcy at the end of period t. We have the following results.

Proposition 1. For the RS contract between manufacturer i and retailer $j , i f$ the contract parameters $\tau ^ { \mathrm { R S } }$ and $\xi ^ { \tt R S }$ satisfy the condition $\xi ^ { \mathrm { R S } } p ^ { 0 } =$ $( 1 - \tau ^ { \mathrm { R S } } ) w ,$ then we have: $\begin{array} { r } { \begin{array} { r } { 1 ) \frac { v _ { j } ^ { t , \mathtt { R S } } } { B _ { j } ^ { t , \mathtt { R S } } } > \frac { v _ { j } ^ { t } } { B _ { j } ^ { t } } ; a n d 2 ) \frac { v _ { i } ^ { t , \mathtt { R S } } } { B _ { i } ^ { t , \mathtt { R S } } } \left| _ { P B _ { j } ^ { t , \mathtt { R S } } = t r u e } > \frac { v _ { i } ^ { t } } { B _ { i } ^ { t } } \right| _ { P B _ { j } ^ { t } = t r u e } } \end{array} } \end{array}$

In Proposition 1, result 1) indicates that the RS contract has the potential to reduce the bankruptcy probability of retailer j in period t. When retailer j goes bankruptcy at the end of period t, it gives nopayment to its upstream members at the end of this period, which leads to the increase of the manufacturer's bad debt, and the decrease of the manufacturer's net cash in<sup>fl</sup>ow and pro<sup>fi</sup>t. As a result, the probability of bankruptcy at the manufacturer increases.

Result 2) in Proposition 1 shows that, when retailer j goes bankruptcy at the end of period t, the ratio of net cash in<sup>fl</sup>ow and debt of the manufacturer under the RS contract is higher than that without incentive contract. That is, the impact of retailer j's bankruptcy on manufacturer i's <sup>fi</sup>nancial status under the RS contract is smaller than that without incentive contract. Therefore, the risk of bankruptcy propagation from retailer j to manufacturer i under RS contract is lower than that without incentive contract.

When $\xi ^ { \mathrm { R S } } p ^ { 0 } = ( 1 - \tau ^ { \mathrm { R S } } ) w ,$ we have $p _ { j } ^ { { t , \mathrm { R S } ^ { * } } } = { p _ { j } ^ { ~ t ^ { * } } } , D _ { j } ^ { { t , \mathrm { R S } ^ { * } } } = D _ { j } ^ { ~ t ^ { * } }$ and $Q _ { j } ^ { t , \mathrm { R S ^ { * } } } = Q _ { j } ^ { \check { t } ^ { * } }$ <sup>\*</sup>. Then the total pro<sup>fi</sup>t of the supply chain (not including the interest of borrowing) under the RS contract equals to that without incentive contract. Thus Proposition 1 also shows that, when the contract parameters $\tau ^ { \mathrm { R S } }$ and $\xi ^ { \mathrm { R S } }$ satisfy the condition $\xi ^ { { \tt R S } } p ^ { 0 } =$ $( 1 - \tau ^ { \mathrm { R S } } ) w ,$ , the RS contract can reduce bankruptcy risks but cannot increase pro<sup>fi</sup>t of the supply chain. We term this phenomenon a risk–profit tradeoff.

Proposition 2. For the PD contract between manufacturer i and retailer j, the contract parameters $\tau ^ { \mathrm { P D } }$ and $\xi ^ { \mathrm { P D } }$ that satisfy $\frac { v _ { i } ^ { t , \mathrm { P D } } } { B _ { i } ^ { t , \mathrm { P D } } } \left| P B _ { j } ^ { t , \mathrm { P D } } = t r u e \right. >$ $\frac { v _ { i } ^ { t } } { B _ { i } ^ { t } } \bigg | _ { P B _ { j } ^ { t } = t r u e }$ can lead to the result that $\frac { v _ { j } ^ { t , \mathrm { P D } } } { B _ { j } ^ { t , \mathrm { P D } } } < \frac { v _ { j } ^ { t } } { B _ { j } ^ { t } } ;$ and vice versa.

Proposition 2 shows that, the PD contract also has the potential to reduce bankruptcy risks. However, it is also indicated that, the contract parameters that mitigate bankruptcy propagation from the retailer to the manufacturer will increase the occurrences of bankruptcy at the retailers. If the contract parameters mitigate the risk of bankruptcy propagation by increasing the occurrences of bankruptcy, we term this phenomenon a propagation–occurrence tradeoff. This type of tradeoff can also be observed under the QF contract.

Proposition 3. For the QF contract between manufacturer i and retailer $j , \mathrm { P r } \left\{ \frac { v _ { j } ^ { t , \mathrm { Q F } } } { B _ { j } ^ { t , \mathrm { Q F } } } > \frac { v _ { j } ^ { t } } { B _ { j } ^ { t } } \right\}$ and P $\Gamma \left\{ \frac { v _ { i } ^ { t , \mathrm { Q F } } } { B _ { i } ^ { t , \mathrm { Q F } } } \bigg | _ { P B _ { j } ^ { t , \mathrm { Q F } } = t r u e } > \frac { v _ { i } ^ { t } } { B _ { i } ^ { t } } \bigg | _ { P B _ { j } ^ { t } = t r u e } \right\}$ both increase in $\theta _ { j l } .$

We can observe from Proposition 3 that, the more intensity of horizontal competition among retailers $\left( \theta _ { j l } \right)$ , the larger the potential of QF contract in reducing bankruptcy risks. Therefore, Proposition 3 indicates that, the effectiveness of a contract in reducing bankruptcy risks is affected by operational parameters, like horizontal competition among retailers.

Through theoretical analyses, we verify that the three contracts (RS, PD and QF) all have the potential of reducing bankruptcy risks.

However, it is dif<sup>fi</sup>cult to theoretically <sup>fi</sup>nd the optimal set of contract parameters that minimize the bankruptcy risks. In the following sections, simulation experiments are designed to further examine the effectiveness of each contract in mitigating bankruptcy risks and to <sup>fi</sup>nd the corresponding optimal contract parameters.

## 4. Design of simulation experiment

Because of the complex linkages and interactions among supply chain members, bankruptcy propagation is dif<sup>fi</sup>cult to be further investigated through analytical model. Agent-based simulation is an effective approach for its encapsulation of the complex internal behaviors of the members [17], and has been extensively used in the <sup>fi</sup>eld of supply chain modeling (e.g., [14,15]). Thus we further investigate the effectiveness of supply chain contracts in mitigating bankruptcy risks through agent-based simulation experiments. The simulation experiments are designed and implemented on the Swarm platform. Swarm is a multi-agent simulation platform designed by Santa Fe Institute for studying complex adaptive system (CAS), which has been shown effective in its applications in the <sup>fi</sup>elds of supply chain management (e.g., [14]). We next brie<sup>fl</sup>y describe the simulation model, and then design the simulation experiments.

## 4.1. The simulation mode

A Swarm-based simulation model is built to simulate the operations of the supply chain network (SCN) under various supply chain contracts. The built simulation model is composed of a SCN Observer Swarm, which entails all the graphical interfaces as well as a SCN Model Swarm, initiates and controls the whole simulation. The SCN Model Swarm schedules movements, information exchanges and in its turn entails the basic obiects. In our simulation model. the SCN Model Swarm is composed of N independent identical SCN Entities with the same parameters and actions. When N is suf<sup>fi</sup>ciently large, the average value of an output index over the N SCN Entities can be used to evaluate the impacts of operations on SCN. Each SCN Entity is composed of I manufacturer agents and J retailer agents, which are endowed with their own properties, actions and other related information as described in Section 2.

## 4.2. Setting of operational parameters

Research results in Hua et al. [10] reveal that, operational parameters, such as the scale of supply chain network (I and J), horizontal competition between retailers $\left( \theta _ { j l } \right)$ and order allocation coef<sup>fi</sup>cient of retailers $( \alpha _ { j } ^ { \mathrm { O A } } )$ , are important causes of bankruptcy risks in supply chain. In this paper, we set the values of <sup>fi</sup>ve parameters (I, J, P $\{ L _ { i j } = 1 \} , \theta _ { j l }$ and $\bar { \alpha _ { j } } ^ { \bar { \mathrm { O A } } } )$ at different levels (as shown in Table 1) to create various supply chain settings characterized by the combinations of the values of these operational parameters. We assume that the supply chain network has three or six manufacturers $( I { = } 3 \mathrm { o r } 6 )$ , and the number of retailers is two times of that of manufacturers $( \mathrm { i } . \mathrm { e } . , J { = } 6$ or 12).

Parameters considered in the experiments and their levels.

<table><tr><td rowspan="2">Parameters</td><td rowspan="2">Description</td><td colspan="2">Levels</td></tr><tr><td>1</td><td>2</td></tr><tr><td> $I$ </td><td>Number of manufacturers</td><td>3</td><td>6</td></tr><tr><td> $P\{L_{ij}=1\}$ </td><td>Probability that there is a link between manufacturer  $i$  and retailer  $j$ </td><td>0.50</td><td>0.80</td></tr><tr><td> $\theta_{jl}$ </td><td>Retail competition coefficient between retailer  $j$  and retailer  $l$ </td><td> $\frac{0.20}{j-1}$ </td><td> $\frac{0.80}{j-1}$ </td></tr><tr><td> $\alpha_{j}^{\text{OA}}$ </td><td>Order allocation coefficient of retailer  $j$ </td><td>0.30</td><td>0.70</td></tr></table>

In all simulation experiments, values of other parameters are set as follows:

(1) Market demand parameters: $a _ { j } = 1 0 0 + b _ { j } ( 1 0 0 - 1 0 0 ( J - 1 ) \theta _ { j l } )$ $b _ { j } = 1 2$ and $\varepsilon _ { j } ^ { ~ t } { \sim } N ( 0 , 3 0 ^ { 2 } )$ . If a generated market demand is negative, we truncate it as zero

(2) Cost parameters: $\begin{array} { r } { p _ { j } ^ { \circ } = 1 0 0 , \ : w = 7 0 , \ : \ : c _ { x } ^ { t } = \left\{ \begin{array} { l l } { 5 5 . 0 + \tilde { c } , \mathrm { i f } \ : x = i } \\ { 1 2 . 5 + \tilde { c } , \mathrm { i f } \ : x = j } \end{array} \right. } \end{array}$ $\boldsymbol { F } _ { x } ^ { t } = \left\{ \begin{array} { l } { 7 5 0 + \tilde { f } , \mathrm { ~ i f ~ } x = j } \\ { 7 5 0 J / I + \tilde { f } , \mathrm { ~ i f ~ } x = i } \end{array} \right. ;$ operating cost parameters:

$\begin{array} { r } { h _ { x } ^ { t } = \{ \begin{array} { l l } { 3 . 0 + \tilde { h } , \mathrm { ~ i f ~ } x = i } \\ { 5 . 0 + \tilde { h } , \mathrm { ~ i f ~ } x = j } \end{array} , s _ { x } = \{ \begin{array} { l l } { 1 2 , \mathrm { ~ i f ~ } x = i } \\ { 2 0 , \mathrm { ~ i f ~ } x = j } \end{array}  ; } \end{array}$ where parameters

$\tilde { c } , ~ \tilde { f }$ and <sup>\~</sup>h are uniformly distributed over the support of $( - 2 . 5 , 2 . 5 ) , ~ ( - 5 0 , 5 0 )$ and $( - 0 . 5 , 0 . 5 )$ , respectively. That is, $\tilde { c } { \sim } U ( - 2 . 5 , 2 . 5 ) , \tilde { f } { \sim } U ( - 5 0 , 5 0 )$ and $\tilde { h } { \sim } U ( - 0 . 5 , 0 . 5 )$

<sup>e e</sup>(3) Exponential smoothing parameter: $\alpha _ { x } ^ { f } { = } 0 . 3 .$

(4) Pro<sup>fi</sup>t and bankruptcy related parameter $\mathfrak { s } { : } \delta _ { x } = 2 \lambda = 0 . 3 , \phi _ { j } =$ $1 0 r = 0 . 5 , ~ { u _ { x } } ^ { \eta } { \sim } N ( 1 . 0 5 , 0 . 3 5 ^ { 2 } )$ . Endowed cash on hand of newly entered agent is set as: $A _ { x } ^ { \mathrm { e n t r y } } = A _ { x } ^ { 0 } = \left\{ { 2 0 0 0 , \qquad x = j } \atop { 2 0 0 0 J / I , ~ x = i }  \right.$

## 4.3. Output indexes

In simulation experiments, we observe two kinds of output of the SCN: 1) occurrences of bankruptcy at each agent; 2) bankruptcy propagation in the SCN. We set the length of simulation as 400 periods $( T { = } 4 0 0 )$ , and the number of SCN entities as 10 $( N = 1 0 )$ . Following [9] and [10], bankruptcy propagation is measured by the cross correlation coef<sup>fi</sup>cient between the occurrence of bankruptcy at the retailers and that at the manufacturers in each period. De<sup>fi</sup>ne $A N R _ { t }$ as the average number of occurrences of bankruptcy over J retailer agents in period $t , A N M _ { t }$ as the average number of occurrences of bankruptcy over I manufacturer agents in period t. Then {ANR | $t { = } 1 , 2 , . . . , T \}$ and $\{ A N M _ { t } | t = 1 , 2 , . . . , T \}$ can be viewed as two series of bankruptcy occurred at the retailers and manufacturers, respectively. We use cross correlation coef<sup>fi</sup>cient between series {ANR } and {ANM } as the output index (termed CCC indexes hereafter) to describe bankruptcy propagation, and de<sup>fi</sup>ne three CCC indexes as follows:

CCC $\begin{array} { r } { ( \mathrm { L a g } = - 1 ) \ \mathrm { c r o s s } \ \mathrm { c o r r } } \\ { \{ A N M _ { t - 1 } \} , } \end{array}$ elation coef<sup>fi</sup>cient between {ANR } and

CCC (Lag=0) cross correlation coef<sup>fi</sup>cient between {ANR } and {ANM<sub>t</sub>},

CCC (Lag=+1) cross correlation coef<sup>fi</sup>cient between {ANR } and {ANM<sub>t + 1</sub>}.

The CCC (Lag=−1) index is used to describe the bankruptcy propagation from manufacturers to retailers; the CCC $( \mathrm { L } \mathrm { a g } = + 1 )$ index is used to describe the bankruptcy propagation from retailers to manufacturers; the CCC (Lag=0) index is also interpreted as a measure of bankruptcy propagation from retailers to manufacturers owing to bad debt.

We also calculate the expected number of occurrences of bankruptcy at each agent over N SCN entities during T periods, and de<sup>fi</sup>ne the three output indexes (termed AN indexes hereafter): ANR, ANM, and ANSC. The AN indexes are computed as $\begin{array} { r } { \mathrm { f o l l o w s : } A N R = \sum _ { t = 1 } { ^ { T } A N R _ { t } } } \end{array}$ $\begin{array} { r } { A N M { = } \sum _ { t = 1 } ^ { T } A N M _ { t } , \mathrm { a n d } A N S C { = } \sum _ { t = 1 } ^ { T } ( J \times A N R _ { t } + I \times A N M _ { t } / ) ( I + J ) } \end{array}$

## 4.4. Intermediate terms

To further examine why and how coordination contracts may reduce bankruptcy risks, we de<sup>fi</sup>ne three intermediate terms: the average retail price during T periods (p), the average received market demand during T periods $\left( D _ { r } \right)$ , and the average ratio of net cash in<sup>fl</sup>ow and debt during T periods (υ/B). The <sup>fi</sup>rst two intermediate terms are introduced to demonstrate the impact of incentive contracts on member <sup>fi</sup>rms' decision behaviors, and the last term indicates the robustness of member <sup>fi</sup>rms against <sup>fi</sup>nancial distress and bankruptcy.

The three intermediate terms are calculated as follows: $\begin{array} { r } { p = \frac { 1 } { T J } } \end{array}$ $\begin{array} { c }  { \displaystyle { \sum _ { t = 1 } ^ { T } \sum _ { j = 1 } ^ { J } p _ { j } ^ { t } , D _ { r } = \frac { 1 } { T J } \sum _ { t = 1 } ^ { T } \sum _ { j = 1 } ^ { J } D _ { j } ^ { t } , \frac { v _ { r } } { B _ { r } } = \frac { 1 } { T J } \sum _ { t = 1 } ^ { T } \sum _ { j = 1 } ^ { J } \frac { v _ { j } ^ { t } } { B _ { j } ^ { t } } } } \end{array}$ and $\begin{array} { r } { \frac { v _ { m } } { B _ { m } } = \frac { 1 } { T I } \displaystyle \sum _ { t = 1 } ^ { T } \sum _ { i = 1 } ^ { I } \frac { v _ { i } ^ { t } } { B _ { i } ^ { t } } . } \end{array}$ The subscripts r and m in the above equations denote retailers and manufacturers, respectively.

## 5. Simulation results

To verify and compare the effectiveness of the three contracts in mitigating bankruptcy propagation, we perform experiments and observe the CCC indexes and the AN indexes under each contract. Recall that a contract is usually characterized by some contract parameters. We <sup>fi</sup>rst describe the method of determining contract parameters.

## 5.1. Determining contract parameters

To examine the effectiveness of a contract in mitigating bankruptcy propagation in supply chain, we <sup>fi</sup>rst need to specify contract parameters in experiments. Because of the existence of risk–profit tradeoff and propagation–occurrence tradeoff described in Subsection 3.4, we set contract parameters at the values that the CCC indexes are minimized without sacri<sup>fi</sup>cing the AN indexes.

The veri<sup>fi</sup>cation of risk–profit tradeoff is signi<sup>fi</sup>cant to the researches of supply chain risk management, and the propagation–occurrence tradeoff of bankruptcy manifests the main research contributions of this paper compared with Xu et al. [25]. Given operational parameters of the supply chain, if we can <sup>fi</sup>nd a set of contract parameters that minimize the CCC indexes without sacri<sup>fi</sup>cing the performance of the supply chain on the AN indexes, we say that the contract is effective under the operational parameters. Because of the existence of the two types of tradeoff, it is quite possible that we cannot <sup>fi</sup>nd any set of contract parameters that makes the contract effective. In this case, we say that the contract is ineffective under the operational parameters. Once contract parameters are speci<sup>fi</sup>ed at the beginning of a simulation experiment, they will not be changed over the planning horizon.

Speci<sup>fi</sup>cally, the RS contract is characterized by contract parameters $\mathbf { \hat { \rho } } ( \tau ^ { \mathrm { R S } } , \xi ^ { \mathrm { R S } } )$ . We search the effective sets of parameters $\dot { ( \tau ^ { \mathrm { R S } } , \xi ^ { \mathrm { R S } } ) }$ by varying the value of $\tau ^ { \mathrm { R S } }$ in the interval [0.00,1.00) and the value of $\cdot \xi ^ { \mathrm { R S } }$ in the interval $[ 0 . 0 0 , 1 . 0 0 )$ ; contract parameters $( \tau ^ { \mathrm { { P D } } } , \Delta ^ { \mathrm { { P D } } } )$ characterize the PD contract, which are speci<sup>fi</sup>ed by varying the value of $\tau ^ { \mathrm { P D } }$ in (0.00,1.00] and the value of $\xi ^ { \mathrm { P D } }$ in (0.00, 1.00]; contract parameters $( \tau ^ { \mathrm { Q F } } , \xi ^ { \mathrm { Q F } } )$ characterize the QF contract, which are speci-<sup>fi</sup>ed by varying the value of $\tau ^ { \mathrm { Q F } }$ in (1.00,1.20] and the value of $\xi ^ { \mathrm { Q F } }$ in (0.000,1.000].

## 5.2. Verification of risk–profit tradeoff

In this subsection, we present some experiment results to verify the risk–profit tradeoff. We vary the value of $\tau ^ { \mathrm { R S } }$ from 1.00 to 0.00, and $\xi ^ { \mathrm { R S } }$ from 0.00 to 1.00, respectively. Part of the simulation results is reported in Table 2. In Table 2, π-<sup>t</sup>, π-<sup>t</sup> and $\bar { \pi } _ { i + j } ^ { t }$ represent the average pro<sup>fi</sup>t of J retailers, I manufacturers and $I + J$ supply chain members in period t, respectively. Decrease percentage of an index is computed by (the value of an index under a contract−the corresponding value of the index under benchmark)/the corresponding value of the index under benchmark×100%.

Simulation results under the RS contract in Exp. #1.

<table><tr><td rowspan="2"> $\tau^{RS}$ </td><td rowspan="2"> $\xi^{RS}$ </td><td colspan="3">Decrease percentage of average profit (%)</td><td colspan="3">Decrease percentage of AN indexes (%)</td></tr><tr><td> $\bar{\pi}_{j}^{t}$ </td><td> $\bar{\pi}_{i}^{t}$ </td><td> $\bar{\pi}_{i+j}^{t}$ </td><td>ANR</td><td>ANM</td><td>ANSC</td></tr><tr><td>0.50</td><td>0.350</td><td>-26.1</td><td>-116.2</td><td>-132.5</td><td>91.4</td><td>94.5</td><td>92.9</td></tr><tr><td>0.40</td><td>0.400</td><td>-80.2</td><td>-113.3</td><td>-135.5</td><td>91.4</td><td>92.3</td><td>91.9</td></tr><tr><td>0.30</td><td>0.500</td><td>-11.1</td><td>-118.0</td><td>-132.7</td><td>91.4</td><td>94.5</td><td>92.9</td></tr><tr><td>0.20</td><td>0.550</td><td>-64.3</td><td>-115.5</td><td>-136.0</td><td>92.7</td><td>92.7</td><td>92.7</td></tr><tr><td>0.10</td><td>0.600</td><td>-121.2</td><td>-111.9</td><td>-138.6</td><td>91.4</td><td>83.4</td><td>87.4</td></tr><tr><td>0.00</td><td>0.600</td><td>-336.4</td><td>-92.4</td><td>-141.4</td><td>89.2</td><td>-937.0</td><td>-438.0</td></tr></table>

As shown in Table 2, the optimal RS contract with the pro<sup>fi</sup>tmaximizing objective is the set of contract parameters with $\tau ^ { \mathrm { R S } } = 0 . 0 0$ and $\xi ^ { \mathrm { R S } } = 0 . 6 0 0$ . However, when $\tau ^ { \mathrm { R S } } = 0 . 0 0$ and $\xi ^ { \mathrm { R S } } = 0 . 6 0 0$ , the average occurrence of bankruptcy at the supply chain is greatly increased.

This type of tradeoff can also be veri<sup>fi</sup>ed from another perspective. Fig. 1 shows the average decrease percentage of output indexes under RS contract in Exp. #1. Notations from X1 to X10 on the abscissa of Fig. 1 denote that $( \tau ^ { \mathrm { R S } } , \xi ^ { \mathrm { R S } } )$ equals (0.90, 0.075), (0.80, 0.125), (0.70, 0.200), (0.60, 0.300), (0.50, 0.350), (0.40, 0.400), (0.30, 0.500), (0.20, 0.550), (0.10, 0.600) and (0.00, 0.650), respectively. It can be observed from Fig. 1 that, when $\tau ^ { \mathrm { R S } } = 0 . 6 0$ and $\xi ^ { \hat { \mathrm { R S } } } = 0 . 3 \bar { 0 0 }$ , the CCC indexes are minimized and the AN indexes are also decreased. However, the pro<sup>fi</sup>t is decreased.

The risk–profit tradeoff can also be observed under the QF and PD contracts. This phenomenon indicates that, on one hand, if a <sup>fi</sup>rm ignores <sup>fi</sup>nancial risks in operational decision-making, the resulted operational decisions may lead to poor performance (this observation has been made by Babich and Sobel [1]); on the other hand, if a <sup>fi</sup>rm overemphasizes <sup>fi</sup>nancial risks, the resulted operational decisions may greatly reduce its pro<sup>fi</sup>tability.

## 5.3. Verification of propagation–occurrence tradeoff

We next present some experiment results to verify the propagation–occurrence tradeoff of bankruptcy. Under the PD contract, we set $\xi ^ { \mathrm { P D } } = 0 . 0 5 0$ and vary the value of $\cdot ^ { \mathrm { P D } }$ from 0.250 to 0.350 with step 0.025. The simulation results are shown in Fig. 2. It can be observed from Fig. 2 that, the PD contract can effectively reduce the CCC indexes, meanwhile, the AN indexes increase.

Similarly, as shown in Fig. 3, the QF contract can reduce the AN indexes, but increase the CCC indexes. Notations from X1 to X5 on the abscissa of Fig. 3 denote that the set of contract parameter $( \tau ^ { \mathrm { Q F } } , \xi ^ { \mathrm { Q F } } )$ equals (1.01, 0.040), (1.02, 0.080), (1.03, 0.095), (1.04, 0.110) and (1.05, 0.110), respectively.

## 5.4. Effectiveness of the three contracts

## 5.4.1. Benchmark

Before investigating the effectiveness of the three contracts, we <sup>fi</sup>rst simulate the supply chain when no contract is applied, and summarize the corresponding CCC indexes and AN indexes under various combinations of the four parameters (listed in Table 1) as benchmarks (detailed results are available from the authors upon request).

We make regression analyses on the benchmark data and <sup>fi</sup>nd that, bankruptcy risks in supply chain depend on supply chain setting that is characterized by operational parameters $( I , J , P \{ L _ { i j } = 1 \} ,$ $\theta _ { j l } ,$ $\alpha _ { j } ^ { O A } )$ . Speci<sup>fi</sup>cally, bankruptcy risks can be reduced through the design of supply chain structure, i.e., increasing the scale of supply chain network (I and J), or increasing links between upstream and downstream members $( P \{ L _ { i j } = 1 \} )$ ). However, for a given structure of supply chain, bankruptcy risks in supply chain increases in the intensity of horizontal competition $\left( \theta _ { j l } \right)$

![](/api/attachments/VT5BAAVK/fulltext/images/48245200080153c9becf4e571055061bfd00a78e5651da509ae973ee62a6bed0.jpg)  
Fig. 1. Average decrease percentage of output indexes under RS contract in Exp. #1.

![](/api/attachments/VT5BAAVK/fulltext/images/15dfdfb8299ee1d87a6f3e078ee0e347b5e854206b0c53fb320778cf65594aac.jpg)  
Fig. 2. Average decrease percentage of output indexes under PD contract in Exp. #3

We next verify the effectiveness of the three contracts in reducing the bankruptcy risks caused by horizontal competition. In the following experiments, we set $I = 3 , J { = } 6$ , and $P \{ L _ { i j } = 1 \} = 0 . 5$ . Given the values of parameters $\theta _ { j l }$ and $\alpha _ { j } ^ { O A }$ , a contract is effective if the CCC indexes are improved and the AN indexes are not worsened compared with the corresponding benchmarks.

## 5.4.2. RS contract

Given three combinations of operational parameters $\theta _ { j l }$ and $\alpha _ { i } ^ { O A }$ when the RS contract is applied, the simulation results are shown in Table 3. Please note in Table 3 that the contact parameters $\tau ^ { \mathrm { R S } }$ and $\xi ^ { \mathrm { R S } }$ in each combination are determined according the method described in Section 5.1.

It can be observed from Table 3 that, the RS contract can effectively mitigate the bankruptcy propagation in supply chain; meanwhile, the probability of occurrence of bankruptcy at each stage of the supply chain is also reduced.

## 5.4.3. PD contract

The simulation results under the PD contract are reported in Table 4.

It can be observed from Table 4 that, the PD contract is effective in reducing the occurrence and propagation of bankruptcy when competition between retailers is relatively mild. However, when competition between retailers is relatively intensive, the PD contract cannot reduce bankruptcy propagation without increasing the occurrence of bankruptcy at the supply chain members (bold in Table 4). By comparison, when the PD contract is effective, it is less effective than the RS contract in mitigating the occurrence and propagation of bankruptcy in supply chain.

## 5.4.4. $Q F$ contract

Given three combinations of operational parameters $\theta _ { j l }$ and $\alpha _ { j } ^ { O A } ,$ when the QF contract is applied, the simulation results are shown in Table 5.

![](/api/attachments/VT5BAAVK/fulltext/images/3d8465a542b3d8b8145308d1c976f485f13585319fcefe46b1fc9cac5dbc0571.jpg)  
Fig. 3. Average decrease percentage of output indexes under QF contract in Exp. #4.

Table 4  
Table 5  
Table 3  
Comparison between the output indexes of the RS contract and benchmarks.

<table><tr><td> $\theta_{jl}$ </td><td> $\alpha_j^{OA}$ </td><td> $\tau^{RS}$ </td><td> $\xi^{RS}$ </td><td>CCC(Lag = -1)</td><td>CCC(Lag = 0)</td><td>CCC(Lag = +1)</td><td>ANR</td><td>ANM</td><td>ANSC</td></tr><tr><td rowspan="2"> $\frac{0.20}{J-1}$ </td><td rowspan="2">0.30</td><td>0.60</td><td>0.300</td><td>-0.050</td><td>-0.050</td><td>0.155</td><td>0.65</td><td>0.33</td><td>0.54</td></tr><tr><td colspan="2">Benchmark</td><td>0.090</td><td>0.298</td><td>0.250</td><td>3.72</td><td>7.83</td><td>5.09</td></tr><tr><td rowspan="2"> $\frac{0.80}{J-1}$ </td><td rowspan="2">0.30</td><td>0.10</td><td>0.600</td><td>-0.060</td><td>0.088</td><td>-0.023</td><td>1.00</td><td>12.50</td><td>4.83</td></tr><tr><td colspan="2">Benchmark</td><td>0.162</td><td>0.470</td><td>0.381</td><td>8.68</td><td>14.27</td><td>10.54</td></tr><tr><td rowspan="2"> $\frac{0.80}{J-1}$ </td><td rowspan="2">0.70</td><td>0.30</td><td>0.450</td><td>-0.013</td><td>0.020</td><td>0.053</td><td>0.50</td><td>9.63</td><td>3.54</td></tr><tr><td colspan="2">Benchmark</td><td>0.073</td><td>0.374</td><td>0.301</td><td>8.43</td><td>20.17</td><td>12.34</td></tr></table>

Results in Table 5 show that, the QF contract is effective in mitigating bankruptcy propagation when competition between retailers is relatively intensive and the smoothing factor of order allocation of retailers is relatively small (e.g., $\begin{array} { r } { \theta _ { j l } = \frac { 0 . 8 } { J - 1 } } \end{array}$ and $\alpha _ { j } { } ^ { O A } = 0 . 3 0 )$ . When competition between retailers is relatively intensive and the order allocation coef<sup>fi</sup>- cient of retailers is relatively large, the QF contract can reduce the occurrence of bankruptcy at supply chain members, however, it cannot effectively reduce the CCC indexes (bold in Table 5). When competition between retailers is relatively mild, the QF contract is ineffective. Comparatively, when the QF contract is effective, it is less effective than the RS contract in mitigating bankruptcy risks in supply chain.

Based on the above experiments, we can draw the following conclusions:

(1) The existence of risk–profit tradeoff and propagation–occurrence tradeoff causes some contracts to be ineffective under certain settings of operational parameters of the supply chain.

(2) Horizontal competition between retailers is an important factor in determining the effectiveness of a contract in mitigating bankruptcy propagation. When competition between retailers is relatively mild, the RS and PD contracts are effective; when competition between retailers is relatively intensive, the QF and RS contracts are veri<sup>fi</sup>ed to be effective.

(3) When competition between retailers is mild or not so intensive, the RS contract, among the two effective contracts (RS and PD), is more effective in mitigating bankruptcy propagation. When competition between retailers is relatively intensive, the QF contract, among the two effective contracts (QF and RS), is less effective than the RS contract.

(4) Order allocation coef<sup>fi</sup>cient of retailers affects the effectiveness of some contracts, e.g., the QF contract. When competition between retailers is relatively intensive, QF can effectively mitigate bankruptcy propagation if the order allocation coef<sup>fi</sup>cient of retailers is relatively small, and cannot effectively mitigate bankruptcy propagation if the order allocation coef<sup>fi</sup>cient is relatively high.

Table 6  
Comparisons of intermediate terms under the setting with $\begin{array} { r } { \theta _ { j l } = \frac { 0 . 2 } { J - 1 } } \end{array}$ and $\alpha _ { j } ^ { O A } = 0 . 3 .$

<table><tr><td></td><td></td><td>Benchmark</td><td>RS</td><td>PD</td><td>QF</td></tr><tr><td rowspan="2"> $p$ </td><td>Mean</td><td>97.28</td><td>97.75</td><td>95.00</td><td>99.34</td></tr><tr><td>C.I. $^{a}$ </td><td>[97.26, 97.31]</td><td>[97.72, 97.78]</td><td>[94.98, 95.03]</td><td>[99.31, 99.36]</td></tr><tr><td rowspan="2"> $D_{r}$ </td><td>Mean</td><td>126.5</td><td>121.8</td><td>147.6</td><td>106.6</td></tr><tr><td>C.I.</td><td>[126.1, 126.9]</td><td>[121.4, 122.3]</td><td>[147.2, 148.1]</td><td>[106.2, 107.0]</td></tr><tr><td rowspan="2"> $\frac{v_{r}}{B_{r}}$ </td><td>Mean</td><td>0.105</td><td>0.140</td><td>0.152</td><td>0.035</td></tr><tr><td>C.I.</td><td>[0.099, 0.112]</td><td>[0.130, 0.150]</td><td>[0.148, 0.156]</td><td>[0.028, 0.041]</td></tr><tr><td rowspan="2"> $\frac{v_{m}}{B_{m}}$ </td><td>Mean</td><td>0.033</td><td>0.163</td><td>0.079</td><td>0.022</td></tr><tr><td>C.I.</td><td>[0.026, 0.040]</td><td>[0.158, 0.169]</td><td>[0.075, 0.083]</td><td>[0.014, 0.031]</td></tr><tr><td> $\frac{v_{m}}{B_{m}} / \frac{v_{r}}{B_{r}}$ </td><td>Mean</td><td>0.314</td><td>1.164</td><td>0.520</td><td>0.629</td></tr></table>

<sup>a</sup> C.I. is the abbreviation of Con<sup>fi</sup>dence Interval, with the probability of 95%.

## 5.5. Comparisons of intermediate terms

To explain how and why the three contracts can reduce bankruptcy risks, we compare of the changes of intermediate terms (described in Subsection 4.4) between with and without considering incentive contracts. We perform the simulation experiments under the parameter setting that $\textstyle \theta _ { j l } = \frac { 0 . 2 } { I - 1 } , \alpha _ { j } ^ { O A } = 0 . 3$ , and the contract parameters are set at their optimal values. Speci<sup>fi</sup>cally, $( \tau ^ { \mathrm { R S } } , \xi ^ { \mathrm { R S } } ) = ( 0 . 6 0 , 0 . 3 0 )$ $( \tau ^ { \mathrm { { P D } } } , \xi ^ { \mathrm { { P D } } } ) = ( 0 . 3 \dot { 0 } , 1 . 0 0 )$ and $( \tau ^ { \mathrm { Q F } } , \xi ^ { \mathrm { Q F } } ) = ( \bar { 1 } . 0 5 , 0 . 1 \bar { 5 } )$ . The obtained results are reported in Table 6.

Table 6 shows that, the value of $v _ { r } / B _ { r }$ under the RS and PD contracts is higher than the corresponding benchmark; but that under the QF contract is lower than the corresponding benchmark. Additionally, the value o $\frac { v _ { m } } { B _ { m } } \Big / \frac { v _ { r } } { B _ { r } }$ under each contract is higher than the corresponding benchmark. If the retailer goes bankruptcy, then the manufacturer's bad debt increases $( \mathrm { i } . \mathsf { e } . , v _ { m } / B _ { m }$ decreases), and the bankruptcy risk of the manufacturer also increases. Thus the indicator $\frac { v _ { m } } { B _ { m } } \Big / \frac { v _ { r } } { B _ { r } }$ evaluates the manufacturer's robustness against bankruptcy in the case when the retailer goes bankruptcy.

Therefore, results in Table 6 indicate that, under the supply chain setting with $\theta _ { j l } = \frac { 0 . 2 } { J - 1 }$ and $\alpha _ { j } ^ { O A } = 0 . 3 , 1 )$ the bankruptcy probability of the retailer can be reduced by RS and PD contract, but may be increased by QF contract; 2) the three contracts all have the potential of reducing bankruptcy propagation risk in supply chain. The above observations coincide with the results in Tables 3–5.

Comparison between the output indexes of the PD contract and benchmarks.

<table><tr><td> $\theta_{jl}$ </td><td> $\alpha_j^{OA}$ </td><td> $\tau^{PD}$ </td><td> $\xi^{PD}$ </td><td>CCC (Lag = -1)</td><td>CCC (Lag = 0)</td><td>CCC (Lag = +1)</td><td>ANR</td><td>ANM</td><td>ANSC</td></tr><tr><td rowspan="2"> $\frac{0.20}{J-1}$ </td><td rowspan="2">0.30</td><td>0.300</td><td>1.000</td><td>-0.045</td><td>0.082</td><td>0.040</td><td>0.25</td><td>0.93</td><td>0.48</td></tr><tr><td>Benchmark</td><td></td><td>0.090</td><td>0.298</td><td>0.250</td><td>3.72</td><td>7.83</td><td>5.09</td></tr><tr><td rowspan="2"> $\frac{0.80}{J-1}$ </td><td rowspan="2">0.30</td><td>0.300</td><td>1.000</td><td>-0.031</td><td>0.184</td><td>0.042</td><td>16.22</td><td>33.37</td><td>21.93</td></tr><tr><td>Benchmark</td><td></td><td>0.162</td><td>0.470</td><td>0.381</td><td>8.68</td><td>14.27</td><td>10.54</td></tr><tr><td rowspan="2"> $\frac{0.80}{J-1}$ </td><td rowspan="2">0.70</td><td>0.250</td><td>1.000</td><td>0.007</td><td>0.221</td><td>0.017</td><td>7.12</td><td>43.80</td><td>19.34</td></tr><tr><td>Benchmark</td><td></td><td>0.073</td><td>0.374</td><td>0.301</td><td>8.43</td><td>20.17</td><td>12.34</td></tr></table>

Comparison between the output indexes of the QF contract and benchmarks

<table><tr><td> $\theta_{jl}$ </td><td> $\alpha_{j}^{OA}$ </td><td> $\tau^{QF}$ </td><td> $\xi^{QF}$ </td><td>CCC (Lag = -1)</td><td>CCC (Lag = 0)</td><td>CCC (Lag = +1)</td><td>ANR</td><td>ANM</td><td>ANSC</td></tr><tr><td rowspan="2"> $\frac{0.20}{J-1}$ </td><td rowspan="2">0.30</td><td>1.05</td><td>0.150</td><td>0.019</td><td>0.174</td><td>0.072</td><td>12.62</td><td>7.23</td><td>10.82</td></tr><tr><td>Benchmark</td><td></td><td>0.090</td><td>0.298</td><td>0.250</td><td>3.72</td><td>7.83</td><td>5.09</td></tr><tr><td rowspan="2"> $\frac{0.80}{J-1}$ </td><td rowspan="2">0.30</td><td>1.04</td><td>0.305</td><td>0.094</td><td>0.271</td><td>0.235</td><td>7.05</td><td>13.07</td><td>9.06</td></tr><tr><td>Benchmark</td><td></td><td>0.162</td><td>0.470</td><td>0.381</td><td>8.68</td><td>14.27</td><td>10.54</td></tr><tr><td rowspan="2"> $\frac{0.80}{J-1}$ </td><td rowspan="2">0.70</td><td>1.03</td><td>0.095</td><td>0.109</td><td>0.349</td><td>0.317</td><td>8.18</td><td>14.17</td><td>10.18</td></tr><tr><td>Benchmark</td><td></td><td>0.073</td><td>0.374</td><td>0.301</td><td>8.43</td><td>20.17</td><td>12.34</td></tr></table>

Based on the simulation process and the properties of the three contracts, we further examine and explain how these contracts change <sup>fi</sup>rms' <sup>fi</sup>nancial indicators and reduce bankruptcy risks:

1) Compared with the benchmark case, the manufacturer under the RS contract offers a lower wholesale price to the retailer. As a result, the debt (i.e., the borrowed money) of the retailer is reduced, and the cost of <sup>fi</sup>nancial distress if any can also be reduced. Meanwhile, since the manufacturer under RS contract shares a proportion of the retailer' sales revenue, it also shares a proportion of the market demand risk. As a result, the bankruptcy risk of the retailer can be reduced by RS contract. On the other hand, with a lower wholesale price, the manufacturer's accounts receivable also decrease, thus bad debt of the manufacturer caused by the bankruptcy of retailers can be reduced. As a result, the RS contract can also reduce bankruptcy propagation in supply chain.

2) Hua et al. [10] pointed out that, the decrease of sales revenue is an important operational cause of bankruptcy propagation in supply chain. From Table 6 we can see that, by decreasing the retail price, the PD contract can stimulate the large increase of market demand, and thus can increase sales revenue of the supply chain with competing retailers. With the large increase of market demand, the manufacturer's sales quantity of product also increases. As a result, the risks of bankruptcy in supply chain can be reduced by PD contract.

3) When $\begin{array} { r } { \theta _ { j l } = \frac { 0 . 2 } { J - 1 } } \end{array}$ , the QF contract would cause the decrease of sales revenue. As a result, the net cash in<sup>fl</sup>ow of the retailer is reduced, which increases its risk of bankruptcy. However, in the case when the retailer goes bankruptcy, the manufacturer under QF can reduce its bad debt by charging a higher wholesale price and by reducing the refund for the retailer's leftover inventory. As a result, the impact of retailer's bankruptcy on the manufacturer can be reduced. When $\theta _ { j l } = \frac { 0 . 8 } { J - 1 }$ , we <sup>fi</sup>nd that the QF contract can increase the sales revenue of supply chain, and thus reduce both bankruptcy occurrence and bankruptcy propagation in supply chain.

The above observations indicate that, when a manager chooses a contract to improve the performance of a supply chain, he should consider the properties of the contract in hedging <sup>fi</sup>nancial risks under various supply chain settings, as well as its effectiveness in improving the pro<sup>fi</sup>t of the supply chain.

## 6. Conclusions

In this paper we have developed a general modeling framework to explore methods for mitigating bankruptcy propagation through supply chain coordination. The described method provides the possibility of connecting the <sup>fi</sup>nancial risk in supply chain to the operational interactions among supply chain members and to the operational decisions made by supply chain members. This study makes a signi<sup>fi</sup>cant contribution to the supply chain risk management and the <sup>fi</sup>nancial management literature by examining the effectiveness of typical supply chain contracts (including revenue sharing, price discount and quantity <sup>fl</sup>exibility) in mitigating bankruptcy propagation in supply chain. Our research results suggest that, supply chain contracts are conditionally effective in mitigating bankruptcy propagation, and their effectiveness depends on the operational parameters of supply chain; horizontal competition between retailers is an important factor in determining the effectiveness of a contract. This research is signi<sup>fi</sup>cant to the area of supply chain risk management because it provides a new research perspective of mitigating bankruptcy propagation through operational interactions among supply chain members and decisions made by supply chain members.

This paper investigates the effectiveness of some typical supply chain contracts in mitigating bankruptcy propagation with a relatively simple relationship between the supply chain members. That is, we assume exogenous wholesale price and no explicit competition between manufacturers. If there exists explicit horizontal competition among manufacturers (e.g., wholesale price competition), the conclusions in this paper need to be re-speculated, which will be the topic of future research.

## Acknowledgements

The authors would like to thank the anonymous referees and the editors for their insightful comments and suggestions, which signi<sup>fi</sup>cantly improved the paper. The <sup>fi</sup>rst author was supported by the National Natural Science Foundation of China (NSFC) under Grants Nos. 71101135 and 70821001. The second author was supported by the NSFC under Grant No. 70772025. The third author was supported by the NSFC under Grants Nos. 70725001 and 71090401/71090400.

## Appendix A. Proofs of Lemma and Propositions

## Proof of Lemma 1

Based on the de<sup>fi</sup>nition of <sup>fi</sup>nancial distress $( A _ { x } ^ { ~ t } < 0 )$ , the level of cash on hand $( A _ { x } ^ { ~ t } )$ determines the risk of <sup>fi</sup>nancial distress of <sup>fi</sup>rm x in period t. When ${ A _ { x } } ^ { 0 } \to + \infty ,$ , the net cash in<sup>fl</sup>ow of member x in each period directly increase or decrease its cash on hand as described in Eq. (14), thus the level of net cash in<sup>fl</sup>ow $( v _ { x } ^ { ~ t } )$ determines the risk of <sup>fi</sup>nancial distress of <sup>fi</sup>rm x in period t. That is, the higher the level of ${ v _ { x } } ^ { t } ,$ the higher the risk of <sup>fi</sup>nancial distress of <sup>fi</sup>rm x in period t.

If <sup>fi</sup>rm x falls into <sup>fi</sup>nancial distress in period t, <sup>fi</sup>nancial distress cost (C <sup>t</sup>) will be incurred following Eq. (16). We can see from Eq. (16) that, <sup>fi</sup>nancial distress cost $( C _ { x } ^ { \ t } )$ is an increasing function of the <sup>fi</sup>rm's debt level $( B _ { x } ^ { ~ t } )$ . Also, we can see from the de<sup>fi</sup>nition of bankruptcy $( { A _ { x } } ^ { t } + { c _ { x } } { I } { H _ { x } } ^ { t } + { \eta _ { x } } ^ { t } - { C _ { x } } ^ { t } < 0 )$ that, the bankruptcy probability of <sup>fi</sup>rm x in period t is an increasing function of the <sup>fi</sup>nancial distress cost $( C _ { x } ^ { t } )$ Therefore, when $A _ { x } ^ { 0 } \to + \infty$ the bankruptcy probability of <sup>fi</sup>rm x in period t decreases in ${ v _ { x } } ^ { t } ,$ , but increases in $B _ { x } ^ { ~ t } . \sqsupset$

## Proofs of Propositions 1–3

We <sup>fi</sup>rst consider the case without incentive contract, which is considered as the benchmark.

## (0) Benchmark

Under the assumptions described in Subsection 3.4, the estimated pro<sup>fi</sup>t of retailer j under the case without incentive contract (the benchmark case) can be described as $\hat { \pi } _ { j } ^ { t } = \Big ( p _ { j } ^ { t } { - } w \Big ) \hat { D } _ { j } ^ { t }$ with $\hat { D } _ { j } ^ { t } = a _ { j } - b _ { j } \Big ( p _ { j } ^ { t } - \theta _ { j l } p _ { l } ^ { t - 1 } \Big )$ . With the objective to maximize its estimated pro<sup>fi</sup>t, the optimal price of retailer j in period t is determined as $\begin{array} { r } { p _ { j } ^ { t * } = \frac { a + b _ { j } \left( \theta _ { j l } p _ { l } ^ { t - 1 } + w \right) } { 2 b _ { i } } } \end{array}$ , the optimal order quantity is $Q _ { j } ^ { t * } = \hat { D } _ { j } ^ { t } \ = a _ { j } -$ $b _ { j } ( { p _ { j } } ^ { t } - \theta _ { j l } { p _ { l } } ^ { \dot { t } - 1 } )$ , and the realized demand is ${ D _ { j } } ^ { t ^ { * } } = a - { b _ { j } } ( { p _ { j } } ^ { t ^ { * } } -$ $\theta _ { j l } p _ { l } ^ { ~ t ^ { * } } )$ . Then we can compute the net cash in<sup>fl</sup>ow and the debt of member <sup>fi</sup>rms in period t following Eqs. (9)–(12).

Similar to the benchmark case, we compute the optimal retail price, order quantity and realized demand of retailer j under the three contracts. Speci<sup>fi</sup>cally, $\begin{array} { r } { p _ { j } ^ { t , \mathtt { R S } _ { * } } = \frac { a + b _ { j } \left( \theta _ { j l } p _ { l } ^ { t - 1 } + \xi ^ { \mathtt { R S } } p ^ { 0 } + \tau ^ { \mathtt { R S } } w \right) } { 2 b _ { i } } , \quad p _ { j } ^ { t , \mathtt { P D } _ { * } } = } \end{array}$ $\frac { a + b _ { j } \left( \theta _ { j l } p _ { l } ^ { t - 1 } + w ^ { t , \mathrm { P D } } \right) } { 2 b _ { j } }$ and $\begin{array} { r } { p _ { j } ^ { t , \mathrm { Q F * } } = \frac { a + b _ { j } \left( \dot { \theta _ { j l } } p _ { l } ^ { t - 1 } + \tau ^ { \mathrm { Q F } } w \right) } { 2 b _ { i } } . } \end{array}$ . The net cash inflow and the debt of member <sup>fi</sup>rms under contracts can be computed following Eqs. $( 1 9 ) - ( 3 4 )$ . Then we can obtain the value of <sup>fi</sup>nancial indicator $( v _ { x } ^ { ~ t } / B _ { x } ^ { ~ t } )$ as summarized in Table A.1.

## (1) Proof of Proposition 1

$\begin{array} { r } { \operatorname { I f } \xi ^ { \mathrm { R } S } p ^ { 0 } = ( 1 - \tau ^ { \mathrm { R } S } ) w , } \end{array}$ then $p _ { j } ^ { { t , \mathrm { R S } } } { = } p _ { j } ^ { { t } }$ and $Q _ { j } ^ { t , \mathrm { R S } } = Q _ { j } ^ { ~ t }$ . Thus we have

$$
\begin{array}{l} \frac {v _ {j} ^ {t , \mathrm{RS}}}{B _ {j} ^ {t , \mathrm{RS}}} - \frac {v _ {j} ^ {t}}{B _ {j} ^ {t}} = \frac {\left(1 - \tau^ {\mathrm{RS}}\right) \left(p _ {j} ^ {t} - w\right) D _ {j} ^ {t}}{\tau^ {\mathrm{RS}} \phi_ {j} w Q _ {j} ^ {t}} > 0, \text { and } \\ \frac {v _ {i} ^ {t , \mathrm{RS}}}{B _ {i} ^ {t , \mathrm{RS}}} \Bigg | _ {P B _ {j} ^ {t, \mathrm{RS}} = t r u e} - \frac {v _ {i} ^ {t}}{B _ {i} ^ {t}} \Bigg | _ {P B _ {j} ^ {t} = t r u e} = \frac {\left(1 - \tau^ {\mathrm{RS}}\right) \left(1 - \phi_ {j}\right) w Q _ {j} ^ {t}}{c _ {i} Q _ {i} ^ {t}} > 0 \text { for } \tau^ {\mathrm{RS}} <   1 \end{array}
$$

Thus Proposition 1 holds

## (2) Proof of Proposition 2

For simplicity, we consider the case that $c ^ { 0 } = 0 .$ . Then

$$
\frac {v _ {j} ^ {t , \mathrm{PD}}}{B _ {j} ^ {t , \mathrm{PD}}} - \frac {v _ {j} ^ {t}}{B _ {j} ^ {t}} = \frac {1}{\phi_ {j}} \left(\frac {p _ {j} ^ {t , \mathrm{PD}} D _ {j} ^ {t , \mathrm{PD}}}{w ^ {t , \mathrm{PD}} Q _ {j} ^ {t , \mathrm{PD}}} - \frac {p _ {j} ^ {t} D _ {j} ^ {t}}{w Q _ {j} ^ {t}} + \xi^ {\mathrm{PD}} \left(1 - \frac {D _ {j} ^ {t , \mathrm{PD}}}{Q _ {j} ^ {t , \mathrm{PD}}}\right)\right).
$$

When $p _ { j } ^ { { t , \mathrm { P D } } } \to p _ { j } ^ { { t } }$ , that is $w ^ { t , \mathrm { P D } } { = } \tau ^ { \mathrm { P D } } p _ { j } ^ { { \mathrm { \Omega } } t - 1 } { \to } w$ , then $\frac { v _ { j } ^ { t , \mathrm { P D } } } { B _ { j } ^ { t , \mathrm { P D } } } - \frac { v _ { j } ^ { t } } { B _ { j } ^ { t } } \longrightarrow$ $\frac { \xi ^ { \mathrm { P D } } } { \phi _ { j } } \left( 1 - \frac { D _ { j } ^ { t , \mathrm { P D } } } { Q _ { j } ^ { t , \mathrm { P D } } } \right) > 0 .$ . Therefore, there exists $\beta > 0 ,$ , when $p _ { j } ^ { { t , \mathrm { { P D } } } } \in ( p _ { j } ^ { { t } }$ $\begin{array} { r } { - \beta , { p _ { j } } ^ { t } + \beta ) , \frac { v _ { j } ^ { t , \mathtt { P D } } } { B _ { i } ^ { t , \mathtt { P D } } } - \frac { v _ { j } ^ { t } } { B _ { j } ^ { t } } > 0 . } \end{array}$ . Moreover, the higher the value of $\xi ^ { \mathrm { P D } }$ , the higher the probability that $\frac { v _ { i } ^ { t , \mathrm { P D } } } { B _ { i } ^ { t , \mathrm { P D } } } - \frac { v _ { i } ^ { t } } { B _ { i } ^ { t } } > 0 .$

Similarly $\cdot _ { B _ { i } ^ { t , \mathrm { P D } } } ^ { v _ { i } ^ { t , \mathrm { P D } } } \bigg | P B _ { j } ^ { t , \mathrm { P D } } = t r u e ^ { - } \frac { v _ { i } ^ { t } } { B _ { i } ^ { t } } \bigg | P B _ { j } ^ { t } = t r u e ^ { } = \frac { \left( 1 + \phi _ { j } - \xi ^ { \mathrm { P D } } \right) w ^ { t , \mathrm { P D } } Q _ { j } ^ { t , \mathrm { P D } } } { 2 c _ { i } Q _ { i } ^ { t , \mathrm { P D } } } + \frac { \xi ^ { \mathrm { P D } } w ^ { t , \mathrm { P D } } D _ { j } ^ { t , \mathrm { P D } } } { c _ { i } Q _ { i } ^ { t , \mathrm { P D } } } -$ $\frac { \left( 1 + \phi _ { j } \right) w } { 2 c _ { i } } .$ . It is easy to observe that, when $w ^ { t , \mathrm { P D } } > w$ and $\xi ^ { \mathrm { P D } } \to 0 ,$ $\left. \frac { v _ { i } ^ { t , \mathrm { P D } } } { B _ { i } ^ { t , \mathrm { P D } } } \right| _ { P B _ { j } ^ { t , \mathrm { P D } } = t r u e } - \frac { v _ { i } ^ { t } } { B _ { i } ^ { t } } \left| _ { P B _ { j } ^ { t } = t r u e } > 0 \right.$ since $D _ { j } ^ { t , \mathrm { P D } } { < } Q _ { j } ^ { { t } , \mathrm { P D } }$ . Moreover, the lower the value of $\xi ^ { \mathrm { P D } }$ , the higher the probability that $\frac { v _ { i } ^ { t , \mathrm { P D } } } { B _ { i } ^ { t , \mathrm { P D } } } \left| { P B } _ { j } ^ { t , \mathrm { P D } } \right.$ true $\left. - \frac { v _ { i } ^ { t } } { B _ { i } ^ { t } } \right| _ { P B _ { j } ^ { t } = t r u e } > 0 .$

Hence Proposition 2 holds. □

(3) Proof of Proposition 3

Under the QF contract we have $p _ { j } ^ { { t , \mathrm { Q F } } } { > } p _ { j } ^ { { t } }$ , then it is easy to obtain $\frac { D _ { j } ^ { t , \mathrm { Q F } } } { Q _ { j } ^ { t , \mathrm { Q F } } } > \frac { D _ { j } ^ { t } } { Q _ { j } ^ { t } } .$ Thus we have

$$
\frac {v _ {j} ^ {t , \mathrm{QF}}}{B _ {j} ^ {t , \mathrm{QF}}} - \frac {v _ {j} ^ {t}}{B _ {j} ^ {t}} > \frac {\xi^ {\mathrm{QF}}}{\phi_ {j}} - \left[ \frac {\xi^ {\mathrm{QF}}}{\phi_ {j}} + \frac {\left(\tau^ {\mathrm{QF}} - 1 p _ {j} ^ {t}\right)}{\phi_ {j} \tau^ {\mathrm{QF}} w} \right] \frac {D _ {j} ^ {t}}{Q _ {j} ^ {t}}.
$$

We can see that $\frac { v _ { j } ^ { t , \mathrm { Q F } } } { B _ { i } ^ { t , \mathrm { Q F } } } - \frac { v _ { j } ^ { t } } { B _ { j } ^ { t } }$ decreases in $\tau ^ { \mathrm { Q F } } ;$ ; and when $\tau ^ { \mathrm { Q F } } \to 1$ $\frac { v _ { j } ^ { t , 0 \mathrm { F } } } { B _ { i } ^ { t , 0 \mathrm { F } } } - \frac { v _ { j } ^ { t } } { B _ { j } ^ { t } } > 0$ . Thus there exists $\bar { \tau } ^ { \mathrm { Q F } } \geq \frac { p _ { j } ^ { t } D _ { j } ^ { t } } { p _ { j } ^ { t } D _ { j } ^ { t } - \xi ^ { \mathrm { Q F } } w \left( Q _ { j } ^ { t } - D _ { j } ^ { t } \right) }$ , when $\tau ^ { \mathrm { Q F } } { \in } ( 1 , \bar { \tau } ^ { \mathrm { Q F } } )$ $\frac { \check { v } _ { j } ^ { t , 0 \mathrm { F } } } { B _ { i } ^ { t , 0 \mathrm { F } } } - \frac { v _ { j } ^ { t } } { B _ { j } ^ { t } } > 0 .$

Since $p _ { j } ^ { { t , \mathrm { Q F } } }$ increases in $\theta _ { j l } ,$ thus the higher the value of $\theta _ { j l } ,$ the higher the value of $\frac { D _ { j } ^ { t , \mathrm { Q F } } } { Q _ { i } ^ { t , \mathrm { Q F } } } - \frac { D _ { j } ^ { t } } { Q _ { i } ^ { t } } ,$ and the higher the value of $\frac { v _ { j } ^ { t , 0 \digamma } } { B _ { i } ^ { t , 0 \digamma } } - \frac { v _ { j } ^ { t } } { B _ { j } ^ { t } } .$ As a result, the higher the value of $\theta _ { j l } ,$ the higher the probability that $\frac { v _ { j } ^ { t , 0 \ F } } { B _ { i } ^ { t , 0 \ F } } - \frac { v _ { j } ^ { t } } { B _ { i } ^ { t } } > 0 ,$ . Similarly, the higher the value of $\theta _ { j l } ,$ the higher the value of $\left. \frac { v _ { i } ^ { t , \mathrm { 0 F } } } { B _ { i } ^ { t , \mathrm { Q F } } } \right| P B _ { j } ^ { t , \mathrm { 0 F } } = t r u e ^ { - \frac { v _ { i } ^ { t } } { B _ { i } ^ { t } } } \left| P B _ { j } ^ { t } = t r u e ^ { \right. }$ , and thus the higher the probability that $\frac { v _ { i } ^ { t , \mathrm { Q F } } } { B _ { i } ^ { t , \mathrm { Q F } } } \bigg | _ { P B _ { j } ^ { t , \mathrm { Q F } } = t r u e } > \frac { v _ { i } ^ { t } } { B _ { i } ^ { t } } \bigg | _ { P B _ { j } ^ { t } = t r u e } .$ . Hence Proposition 3 holds.

Table A.1  
The value of ${ v _ { x } } ^ { t } / { B _ { x } } ^ { t }$ under the case with and without incentive contracts.

<table><tr><td></td><td> $\frac{v_{j}^{t}}{B_{j}^{t}}$ </td><td> $\frac{v_{j}^{t}}{B_{j}^{t}}\left|PB_{j}^{t}=true\right.$ </td></tr><tr><td>Benchmark</td><td> $\frac{p_{j}^{t}}{\phi_{j}w}\cdot\frac{D_{j}^{t}}{Q_{j}^{t}}-\frac{1}{\phi_{j}}$ </td><td> $\frac{(1+\phi_{j})wQ_{j}^{t}}{c_{i}Q_{i}^{t}}-1$ </td></tr><tr><td>RS</td><td> $\frac{p_{j}^{t,RS}-\xi^{RS}p^{0}}{\phi_{j}\tau^{RS}w}\cdot\frac{D_{j}^{t,RS}}{Q_{j}^{t,RS}}-\frac{1}{\phi_{j}}$ </td><td> $\frac{[2\xi^{RS}p^{0}+(1+\phi_{j})\tau^{RS}w]Q_{j}^{t,RS}}{c_{i}Q_{i}^{t,RS}}-1$ </td></tr><tr><td>PD</td><td> $\frac{p_{j}^{t,PD}-\Delta^{t,PD}}{\phi_{j}w^{\tau,PD}}\cdot\frac{D_{j}^{t,PD}}{Q_{j}^{t,PD}}-(1-\xi^{PD})(w^{\tau,PD}-c^{0})\phi_{j}w^{\tau,PD}$ </td><td> $\frac{(1+\phi_{j}-\xi^{PD})w^{\tau,PD}Q_{j}^{t,PD}+\xi^{PD}w^{\tau,PD}D_{j}^{t,PD}}{c_{i}Q_{i}^{t,PD}}-1$ </td></tr><tr><td>QF</td><td> $\frac{p_{j}^{t,QF}-\xi^{QF}\tau^{QF}w}{\phi_{j}\tau^{QF}w}\cdot\frac{D_{j}^{t,QF}}{Q_{j}^{t,QF}}-\frac{1-\xi^{QF}}{\phi_{j}}$ </td><td> $\frac{(1+\phi_{j}-\xi^{QF})\tau^{QF}wQ_{j}^{t,QF}+\xi^{QF}\tau^{QF}wD_{j}^{t,QF}}{c_{i}Q_{i}^{t,QF}}-1$ </td></tr></table>

In addition, since $\frac { v _ { i } ^ { t , 0 \xi } } { B _ { i } ^ { t , 0 \xi } } \left| _ { P B _ { j } ^ { t , 0 \xi } = t r u e } - \frac { v _ { i } ^ { t } } { B _ { i } ^ { t } } \right| _ { P B _ { j } ^ { t } = t r u e } > \frac { \left( 1 + \phi _ { j } \right) \left( \tau ^ { 0 \xi } - 1 \right) w Q _ { j } ^ { t } - \xi ^ { 0 \xi } \tau ^ { 0 \xi } w \left( Q _ { j } ^ { t } - D _ { j } ^ { t } \right) } { c _ { i } Q _ { i } ^ { t } } ,$ thus when $\begin{array} { r } { \tau ^ { \mathrm { { Q F } } } > \frac { \left( 1 + \phi _ { j } \right) w Q _ { j } ^ { t } } { \left( 1 + \phi _ { j } \right) w Q _ { j } ^ { t } - \xi ^ { \mathrm { Q F } } w \left( Q _ { j } ^ { t } - D _ { j } ^ { t } \right) } , \frac { v _ { i } ^ { t , \mathrm { { Q F } } } } { B _ { i } ^ { t , \mathrm { { Q F } } } } \left| _ { P B _ { j } ^ { t , \mathrm { { Q F } } } = t r u e } - \frac { v _ { i } ^ { t } } { B _ { i } ^ { t } } \right| _ { P B _ { j } ^ { t } = t r u e } > 0 . } \end{array}$ . By comparing the condition of $\frac { v _ { j } ^ { t , \mathrm { Q F } } } { B _ { j } ^ { t , \mathrm { Q F } } } - \frac { v _ { j } ^ { t } } { B _ { j } ^ { t } } > 0$ and that of $\frac { v _ { i } ^ { t , \mathrm { 0 F } } } { B _ { i } ^ { t , \mathrm { 0 F } } } \left| _ { P B _ { j } ^ { t , \mathrm { 0 F } } = t r u e } - \frac { v _ { i } ^ { t } } { B _ { i } ^ { t } } \right| _ { P B _ { j } ^ { t } = t r u e } > 0 ,$ , we can also verify the propagation– occurrence tradeoff under the $\boldsymbol { \mathrm { Q F } }$ contract. □

## References

[1] V. Babich, M. Sobel, Pre-IPO operational and <sup>fi</sup>nancial decisions, Management Science 50 (7) (2004) 935–948.

[2] S. Battiston, D.D. Gatti, M. Gallegati, B. Greenwald, J.E. Stiglitz, Credit chains and bankruptcy propagation in production networks, Journal of Economic Dynamics & Control 31 (2007) 2061–2084.

[3] U. Berger, Best response dynamics for role games, International Journal of Game Theory 30 (2001) 527–538.

[4] F. Bernstein, A. Federgruen, Decentralized supply chains with competing retailers under demand uncertainty, Management Science 51 (1) (2005) 18–29.

[5] F. Boissay, Credit chains and the propagation of <sup>fi</sup>nancial distress, European Central Bank Working Paper, 573, January 2006.

[6] D.B. Bradley, M.J. Rubach, Trade credit and small businesses: a cause of business failures? mimeo, University of Central Arkansas, working paper, 2002

[7] G. Cachon, Supply chain coordination with contracts, in: S. Graves, T. de Kok (Eds.), Supply Chain Management—Handbook in OR/MS, 11, North-Holland, Amsterdam, The Netherlands, 2003.

[8] G.P. Cachon, M.A. Lairviere, Supply chain coordination with revenue-sharing con tracts: strength and limitations, Management Science 51 (1) (2005) 30–44.

[9] D.D. Gatti, M. Gallegati, B. Greenwald, A. Russo, J.E. Stiglitz, Business <sup>fl</sup>uctuations in a credit-network economy, Physica A 370 (2006) 68–74.

[10] Z.S. Hua, Y.H. Sun, X.Y. Xu, Operational causes of bankruptcy propagation in supply chain, Decision Support Systems 51 (3) (2011) 671–681.

[11] N. Kiyotaki, J. Moore, Balance-sheet contagion, The American Economic Review 92 (2) (2002) 46–50.

[12] P.R. Kleindorfer, G.H. Saad, Managing disruption risks in supply chains, Production and Operations Management Society 14 (1) (2005) 53–68.

[13] L. Li, H. Zhang, Con<sup>fi</sup>dentiality and information sharing in supply chain coordination, Management Science 54 (8) (2008) 1467–1481.

[14] F.R. Lin, Y.H. Pai, Using multi-agent simulation and learning to design new business process, IEEE Transactions on Systems, Man, and Cybernetics, Part A 30 (3) (2000) 380–384.

[15] F.R. Lin, H.C. Kuo, S.M. Lin, The enhancement of solving the distributed constraint satisfaction problem for cooperative supply chains using multi-agent systems, Decision Support Systems 45 (2008) 795–810.

[16] R. Narasimhan, S. Talluri, Perspectives on risk management in supply chains, Journal of Operations Management 27 (2009) 114–118.

[17] H.V.D. Parunak, R. Savit, R.L. Riolo, Agent-based modeling vs equation-based modeling: a case study and users' guide, Conference Proceedings, Multi-agent Systems and Agent Based Simulation. First International Workshop 1534 (1998 10–25.

[18] B. Pasternack, Optimal pricing and returns policies for perishable commodities, Marketing Science 4 (1985) 166–176.

[19] S. Rassenti, S.S. Reynolds, V.L. Smith, F. Szidarovszky, Adaptation and convergence of behavior in repeated experimental Cournot games, Journal of Economic Behavior & Organization 41 (2000) 117–146.

[20] C.S. Tang, Perspectives in supply chain risk management, International Journal of Production Economics 103 (2006) 451-488

[21] T.A. Taylor, Supply chain coordination under channel rebates with sales effort effects Management Science 48 (8) (2002) 992-1007.

[22] C.Y. Tsai, On supply chain cash <sup>fl</sup>ow risks, Decision Support Systems 44 (2008) 1031-1042

[23] A.A. Tsay, W.S. Lovejoy, Quantity–<sup>fl</sup>exibility contract and supplier–customer incentives, Management Science 45 (10) (1999) 1339–1558.

[24] Z.K. Weng, Channel coordination and quantity discount, Management Science 41 (9) (1995) 1509–1522.

[25] X.Y. Xu, Y.H. Sun, Z.S. Hua, Reducing the probability of bankruptcy through supply chain coordination, IEEE Transactions on Systems, Man, and Cybernetics—Part C: Applications and Reviews 40 (2) (2010) 201–215.

![](/api/attachments/VT5BAAVK/fulltext/images/1931eb8cb21501b6c5c0363c8b7f98a4c38965c2c5e1a0a440b10d1c1f3f323c.jpg)  
Dr. Yanhong Sun received the Ph.D. degree in Management Science from University of Science and Technology of China (USTC) in 2010. She currently works in the Department of Management Science, USTC. Her research interests are in multi-agent systems and supply chain management. She has published academic paper in several journals, including IEEE Transactions on Systems, Man, and Cybernetics, Decision Support Systems.

![](/api/attachments/VT5BAAVK/fulltext/images/f9751aaae3a92cf351f871931f870b466f92846b6057bcd83bda215340767294.jpg)

![](/api/attachments/VT5BAAVK/fulltext/images/b7b7700bc0104958a6e1dd6075e7dc8936f2f1a9e30aa737d74ec34737886770.jpg)

Dr. Xiaoyan Xu received the Ph.D. degree in Management Science from University of Science and Technology of China (USTC) in 2006. She currently is a professor of School of Management, USTC. Her research interests include multi-agent systems, supply chain management and <sup>fi</sup>nance management. She has published academic paper in many journals, such as IEEE Transactions on Systems, Man, and Cybernetics, International Journal of Production Economics, Decision Support Systems.

Dr. Zhongsheng Hua received the Ph.D. degree in Computer Science from University of Science and Technology of China (USTC) in 2000. He currently is a professor and associate dean of School of Management, USTC. His research interests include decision analysis, production and operations management, and supply chain management. He has published academic papers in many journals, such as Production and Operations Management, Marketing Science, European Journal of Operational Research, and International Journal of Production Research. He has also pub lished three books.
