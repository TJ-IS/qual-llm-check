---
otero_id: 10640
otero_key: "43RGFYTA"
title: "Operational causes of bankruptcy propagation in supply chain"
authors: "Zhongsheng Hua; Yanhong Sun; Xiaoyan Xu"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.03.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Operational causes of bankruptcy propagation in supply chain

Zhongsheng Hua ⁎, Yanhong Sun <sup>1</sup>, Xiaoyan Xu <sup>1</sup>

School of Management, University of Science & Technology of China, Hefei, Anhui 230026, People's Republic of China

## a r t i c l e i n f o

Article history: Received 21 July 2009 Received in revised form 18 February 201 Accepted 21 March 2011 Available online 26 March 2011

Keywords: Supply chain Multi-agent systems Bankruptcy propagation Operational decision Financial decision

## a b s t r a c t

With the increasing interdependence among supply chain members, bankruptcy of a supply chain member may be caused by operational decisions of other members. To investigate how bankruptcy occurs and propagates in supply chain networks, we build a multi-agent simulation model for a two-stage supply chain that consists of multiple upstream manufacturers and multiple downstream retailers. Based on the developed simulation model, we study impacts of various operational parameters and decisions, such as horizontal competition among retailers, order allocation strategies of retailers, wholesale price of manufacturers, characteristics of market demand and number of retailers, on bankruptcy propagation. Since many operational decisions of a <sup>fi</sup>rm are made under <sup>fi</sup>nancial constraints, we also investigate the linkage between <sup>fi</sup>rm's operational risks and <sup>fi</sup>nancial decisions (e.g., the maximal risk of cash <sup>fl</sup>ow that a member is willing to take, and the up-front payment proportion of retailers in a two-period payment policy). Experimental results reveal that operational interactions between supply chain members and operational decisions made by supply chain members are important causes of bankruptcy propagation, but impacts of these operational parameters and decisions depend on <sup>fi</sup>nancial decisions. These observations indicate that supply chain members can moderately hedge their operational risk through <sup>fi</sup>nancial decisions.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Corporate bankruptcy occurs when a <sup>fi</sup>rm has chronic and serious losses and/or when a <sup>fi</sup>rm becomes insolvent with liabilities that are disproportionate to assets. Traditionally, bankruptcy of a <sup>fi</sup>rm is attributed to the <sup>fi</sup>rm's own poor management and autocratic leadership [19]. With the increasingly intensive interactions among supply chain members, bankruptcy of a supply chain member may cause other member <sup>fi</sup>rms to get into <sup>fi</sup>nancial dif<sup>fi</sup>culties. In network economy, this phenomenon is termed bankruptcy propagation or <sup>fi</sup>nancial contagion [6,16].

An intuitive explanation of bankruptcy propagation is the avalanche of debt chain or credit chain [10,16,23]. The current <sup>fi</sup>nancial crisis triggered by the 2008 sub-prime crisis is a typical evidence of this viewpoint. Because of the bankruptcy of sub-prime lending institutions, many investment banks (e.g., Lehman Brothers Holdings Inc.) have been <sup>fi</sup>led for bankruptcy. The companies that own Lehman Brothers' securities also suffer big losses on their investments, and more companies are then expected to be bankrupt.

In network economy, companies are not only connected by the capital market, but may also have operational interactions. A supply chain is a network of <sup>fi</sup>rms interacting to transform raw material into <sup>fi</sup>nished product for customers [24]. Since interactions among supply chain members on material, information and cash <sup>fl</sup>ow are becoming increasingly intensive, <sup>fi</sup>nancial status of a <sup>fi</sup>rm in a supply chain depends not only on its own management, but also on the decisions and management of other supply chain members. Intuitively, one expects that upstream manufacturers will bene<sup>fi</sup>t from horizontal competition among downstream retailers. However, as we will show in this paper that, intensive horizontal competition among retailers may cause decreases in pro<sup>fi</sup>t and liquidity of manufacturers and retailers in the long run. As a consequence, the risk of bankruptcy propagation in the supply chain increases. Despite the fact that bankruptcy propagation frequently appears in the network economy, the problem of how various operational decisions of a supply chain member and interactions among supply chain members affect bankruptcy propagation has drawn little attention in the researches of supply chain management.

For a two-echelon supply chain network that consists of multiple manufacturers and retailers, this paper systematically investigates the impacts of various operational decisions/interactions of/between supply chain members, such as horizontal competition among retailers, order allocation strategies of retailers, wholesale price of manufacturers, production uncertainty of manufacturers, characteristics of market demand and number of retailers, on bankruptcy propagation in supply chain.

Bankruptcy, which refers to an unhealthy <sup>fi</sup>nancial status, is the result of the operations of all members in the supply chain over multiple periods [37]. Because of the complex linkages among supply chain members and the dynamically uncertain nature of revenues, <sup>fi</sup>nancial status of the supply chain members is hard to be investigated by any analytical supply chain model. Similarly, empirical questionnaire review or case study can hardly relate <sup>fi</sup>nancial performance of a supply chain member with a speci<sup>fi</sup>c operation or decision made by a supply chain member. Based on these considerations, this paper investigates <sup>fi</sup>nancial status of supply chain members through agent-based simulation experiments. Agent-based simulation is an effective approach for its encapsulation of the complex internal behaviors of the members [31] and thus has been extensively used in the <sup>fi</sup>eld of supply chain modeling (e.g., [27,28,38]).

Main contributions of this paper are three folds. First, an agentbased simulation model is <sup>fi</sup>rstly built to investigate the relationship between the operational decisions/interactions and bankruptcy propagation in a supply chain network. Second, through extensive simulation experiments, impacts of various operational parameters and decisions on occurrence and propagation of bankruptcy have been analyzed, which provide a solid foundation for the research of mitigating bankruptcy propagation in supply chain networks. Third, the linkage between <sup>fi</sup>rms' operational decisions and <sup>fi</sup>nancial decisions is analyzed, which suggests hedging supply chain member's operational risk through <sup>fi</sup>nancial decisions.

The remainder of this paper is organized as follows. In Section 2, we review the literatures related to bankruptcy propagation and its causes. In Section 3, we make a description of the supply chain model. Section 4 clari<sup>fi</sup>es the methodology and development of the simulation model. Simulation results and analyses are presented in Sections 5. Section 6 provides a conclusion remark of this study.

## 2. Literature review

With the increasing interdependence and interaction among <sup>fi</sup>rms, bankruptcy propagation has become an important cause for <sup>fi</sup>rms' bankruptcies. Many researchers and practitioners have observed this phenomenon. The previous academic researches about bankruptcy propagation mainly focus on the following three aspects: 1) the mechanisms of <sup>fi</sup>nancial contagion in <sup>fi</sup>nancial systems; 2) bankruptcy propagation in production networks owing to <sup>fi</sup>nancial interactions between general <sup>fi</sup>rms; 3) bankruptcy propagation in production networks owing to operational interactions between <sup>fi</sup>rms. The next three paragraphs successively review the researches on these three aspects.

The phenomena of bankruptcy propagation were <sup>fi</sup>rstly observed in banking system. By modeling <sup>fi</sup>nancial contagion as an equilibrium phenomenon, Allen and Gale [2] analyzed how bank crisis spreads by contagion, and put forward a theory of “<sup>fi</sup>nancial contagion” in a network model of the inter-bank market. They emphasized the role of inter-bank credit in determining <sup>fi</sup>nancial contagion. Rijckeghem and Weder [34] provided empirical evidence in support of the view that spillovers through common bank lenders were important in transmitting currency crises. Dary and Shãna [13] demonstrated that there is a signi<sup>fi</sup>cant relationship between <sup>fi</sup>nancial contagion and the in<sup>fl</sup>ation rate and between <sup>fi</sup>nancial contagion and <sup>fi</sup>nancial liquidity. Using a model with banking and insurance sectors, Allen and Carletti [1] argued that credit risk transfer can also lead to <sup>fi</sup>nancial contagion between the two sectors and increase the risk of crises. These researches focused on the causes of <sup>fi</sup>nancial contagion among <sup>fi</sup>nancial institutions.

The research on financial contagion has also been extended from banking system to general inter-<sup>fi</sup>rm situation. Based on the background of the slump in Japan in the 1990s, Kiyotaki and Moore [23] examined two mechanisms through which bankruptcy propagation among <sup>fi</sup>rms may occur: First, the propagation may be caused by the effects that <sup>fl</sup>uctuations in asset prices have on collateral values; second, the propagation can also be caused by the effects that default on or postponement of debt payments have when there are chains of credit. According to Gatti et al. [18], bankruptcy propagation among <sup>fi</sup>rms can be induced by the indirect interaction among <sup>fi</sup>rms that takes place through the endogenous determination of the interest rate on bank loans. That is, bankruptcy of one <sup>fi</sup>rm may induce banks restraining the supply of credit and pushing up the interest rate, which may trigger more <sup>fi</sup>rms to go bankruptcy. Bradley and Rubach [11] examined the relationship between trade credit and the <sup>fi</sup>ling for bankruptcy by 131 US small businesses. They found that 31% of the 131 entrepreneurs consider non-payments of trade credit as the most important cause for their bankruptcy. Boissay [10] also emphasized the role of trade credit in inducing bankruptcy propagation. By developing a theoretical model that <sup>fi</sup>rms are linked by trade credit, they found that when customers of a sound <sup>fi</sup>rm are <sup>fi</sup>nancially distressed, then this <sup>fi</sup>rm gets into <sup>fi</sup>nancial dif<sup>fi</sup>culties with probability that ranges from 4.1% to 12.8% (depending on the business cycle and the underlying economic scenario). Gatti et al. [16] modeled a network economy with three sectors: downstream <sup>fi</sup>rms, upstream <sup>fi</sup>rms, and banks. Through agent-based simulations, they found that credit/loan inter-linkages among agents and the <sup>fi</sup>nancial policies of the banks are important sources of bankruptcy propagation across different sectors. The above research indicated that, the interdependence and interaction between <sup>fi</sup>rms are important causes for bankruptcy propagation. However, the above researches mainly attribute bankruptcy propagation to <sup>fi</sup>nance-related causes, e.g., bank loans, trade credit and the endogenous determined interest rate.

The effect of operational decisions of a supply chain member or interactions among supply chain members on bankruptcy propagation has rarely been investigated. Among the few researches, Battiston et al. [6] presented a simple model of a production network in which <sup>fi</sup>rms are linked by supplier–customer relationship. Through simulation analyses, they identi<sup>fi</sup>ed roles of some factors on bankruptcy propagation, e.g., trade credit, interest rate and costs due to supply failure. However, they ignored the relationship between operational decisions (e.g., inventory decisions, cooperation and competition) and these factors. Similar to Battiston et al. [6], by highly simplifying and abstracting operations of <sup>fi</sup>rms and interactions among <sup>fi</sup>rms, Gatti et al. [17] examined the impacts of supply chain structures, i.e., static or evolving, on bankruptcy avalanches. Based on the review of 1695 bankruptcy <sup>fi</sup>lings between 1978 and 2004 from Bankruptcy DataSource Index, Hertzel et al. [22] investigated how <sup>fi</sup>nancial distress and bankruptcy affect a <sup>fi</sup>ling <sup>fi</sup>rm's customers and suppliers, and found that distress related to bankruptcy <sup>fi</sup>lings is associated with negative and signi<sup>fi</sup>cant stock price effects for suppliers. For a simple three-echelon supply chain that consists of a retailer, a distributor, and a manufacturer, Xu et al. [39] found that demand forecasting methods, market demand characteristics (uncertainty of demand in each period and auto-correlation of demands in consecutive periods) and thus service levels required by the supply chain members, have signi<sup>fi</sup>cant impacts on the occurrence of bankruptcy at each stage of the supply chain. By using the recent 10 years data of bankruptcy in Japan, Fujiwara [15] showed that the causes of bankruptcy propagation (e.g., secondary effect from bankruptcy of customer, failure of business-related <sup>fi</sup>rms and failure of accounts receivable) are by no means negligible. These researches have not established the relationship between operational decisions made by supply chain members and bankruptcy propagation appeared in the supply chain.

Many theoretical and practical evidences have proven that business success of a supply chain member depends not only on its own competence, but also on the competence of its partners in the supply chain and on the cooperative interactions between the supply chain members [35]. However, we still know little about how an operational decision of a supply chain member affects the <sup>fi</sup>nancial status of other members of the supply chain. We also have little knowledge about the effect of operational interactions among supply chain members on bankruptcy propagation. Therefore, there is a gap between supply chain operations and bankruptcy propagation in the research of supply chain management, which is the reason for the present paper.

## 3. Description of the supply chain model

Consider a supply chain network consisting of $I \left( I { \geq } 1 \right)$ upstream manufacturers and $J \ ( J { \ge } 1 )$ downstream retailers. The I manufacturers produce a single product, and the J retailers procure the product from the manufacturers to meet random market demand of the product in discrete time periods $t ~ ( t { = } 1 , 2 , . . . , T )$ . Denote by index $i ( i { = } 1 , 2 , . . . , I )$ the ith manufacturer, index j $( j = 1 , 2 , . . . , J )$ the jth retailer. Since the supply chain network has two stages, and each stage has multiple members, we describe the operation process of the network from three aspects: i) horizontal interactions among retailers, ii) vertical interactions between manufacturers and retailers, and iii) operational and <sup>fi</sup>nancial decisions of manufacturers and retailers. To facilitate the description, some notations are de<sup>fi</sup>ned in Table 1.

## 3.1. Horizontal interactions among retailers

Since J retailers sell the same product to the market, demand of each retailer depends not only on its own price, but also on the retail prices of other retailers. Denote by $\mathbf { p } ^ { \mathbf { t } } { = } ( \bar { p } _ { 1 } ^ { t } , p _ { 2 } ^ { t } { , . . . , p _ { j } ^ { t } } { , . . . , p _ { J } ^ { t } } )$ the price vector of J retailers in period $t , d _ { j } ^ { t } ( \mathbf { p } ^ { \mathbf { t } } )$ the elastic demand of retailer j $( j = 1 , 2 , . . . , J )$ . When $d _ { j } ^ { \bar { t } } ( \mathbf { p } ^ { \mathbf { t } } )$ is differentiable, we have [8,9]

$$
\frac {\partial d _ {j} ^ {t} \left(\mathbf {p} ^ {\mathbf {t}}\right)}{\partial p _ {j} ^ {t}} \leq 0 \text { and } \frac {\partial d _ {j} ^ {t} \left(\mathbf {p} ^ {\mathbf {t}}\right)}{\partial p _ {l} ^ {t}} \geq 0 \text { for } l, j \in \{1, 2,..., J \}, l \neq j.\tag{1}
$$

$\operatorname { E q . }$ (1) indicates that the elastic demand of each retailer is decreasing in its own retail price and increasing in or independent of other retailers' sale prices.

The demand of retailer j in period t, D<sup>t</sup>, is assumed to be of the additive form [8]

$$
D _ {j} ^ {t} = d _ {j} ^ {t} \left(\mathbf {p} ^ {\mathbf {t}}\right) + \varepsilon_ {j} ^ {t}.\tag{2}
$$

In Eq. $( 2 ) , \varepsilon _ { j } ^ { t }$ is a random term, and its distribution is independent of the retail price vector $\mathbf { p ^ { t } } .$

Table 1 De<sup>fi</sup>nition of notations.

<table><tr><td>Notations</td><td>Description</td></tr><tr><td> $p_{j}^{t}$ </td><td>Unit retail price of retailer j in period t.</td></tr><tr><td>w</td><td>Unit wholesale price of manufacturers in each period.</td></tr><tr><td> $c_{x}$ </td><td>Unit purchasing/selling cost of member x (x=i or j) in each period.</td></tr><tr><td> $h_{x}$ </td><td>Unit inventory holding cost of member x over one period.</td></tr><tr><td> $s_{x}$ </td><td>Shortage penalty cost rate of member x in each period.</td></tr><tr><td> $k_{x}$ </td><td>Unit cost of capacity investment of member x in each period.</td></tr><tr><td> $D_{x}^{t}$ </td><td>Demand of member x occurred in period t.</td></tr><tr><td> $y_{x}^{t}$ </td><td>Amount of capacity investment of member x at the beginning of period t.</td></tr><tr><td> $Q_{x}^{t}$ </td><td>Order quantity placed by memberxat the beginning of period t.</td></tr><tr><td> $IR_{x}^{t}$ </td><td>Amount of materials/products received by member x in period t.</td></tr><tr><td> $Y_{i}^{t}$ </td><td>Amount of products produced by manufacturer i in period t.</td></tr><tr><td> $u_{i}^{Y}$ </td><td>Quality level of product of manufacturer i.</td></tr><tr><td> $S_{x}^{t}$ </td><td>Maximal amount of products member x can provide in period t.</td></tr><tr><td> $IS_{x}^{t}$ </td><td>Amount of goods sold by member x in period t.</td></tr><tr><td> $IH_{x}^{t}$ </td><td>Overstock of member x at the end of period t.</td></tr><tr><td> $IB_{x}^{t}$ </td><td>Backorders of member x at the end of period t.</td></tr><tr><td> $\pi_{x}^{t}$ </td><td>Realized profit of member x in period t.</td></tr><tr><td> $v_{x}^{t}$ </td><td>Net cash inflow of member x in period t.</td></tr><tr><td> $A_{x}^{t}$ </td><td>Cash on hand of member x at the end of period t.</td></tr><tr><td> $K_{x}^{t}$ </td><td>Capacity level of member x at the end of period t.</td></tr></table>

For the sake of description brevity, we con<sup>fi</sup>ne ourselves to the case where all the elastic demand functions are linear. In particular, we assume

$$
d _ {j} ^ {t} \left(\mathbf {p} ^ {\mathbf {t}}\right) = a _ {j} - b _ {j} \left(p _ {j} ^ {t} - \sum_ {l = 1, l \neq j} ^ {J} \theta_ {j l} p _ {l} ^ {t}\right)\tag{3}
$$

with $a _ { j } { > } 0$ and $b _ { j } { > } 0$ . Parameter $\theta _ { j l }$ denotes the degree of substitutability/complementarity between retailer j and retailer l. Because the product is assumed to be substitutable for customers, following [9], we have $\theta _ { j l } \geq 0$ for all $l , j { \in } \{ 1 , 2 , . . . , J \} , l { \ne } j$ and $\sum _ { l = 1 , l \neq j } ^ { J } \ \theta _ { j l } \leq 1$ . Parameter $\theta _ { j l } = 0$ if demand of retailer j is independent of demand of retailer l; $\theta _ { j l } { > } 0$ if the product is substitutable and there is competition on the market demand between retailer j and retailer l. The larger the value of $\theta _ { j l } ,$ the more intensive the competition between retailer j and retailer l [26]. Therefore, parameter $\theta _ { j l }$ can be interpreted as a measure of horizontal competition between retailer j and retailer l.

## 3.2. Vertical interactions between retailers and manufacturers

At the beginning of each period, retailers receive market demand, review their inventory positions of the product, and make procurement decisions about how much to order from their upstream manufacturers. Similarly, manufacturers receive orders from their downstream retailers at the beginning of each period, then review their inventory positions of the material, and make procurement decisions about how much to order from the suppliers outside of the supply chain. In any period, if the realized demand of a supply chain member is larger than its on-hand inventory, the stockouts are backordered. To simplify the description of interactions between manufacturers and retailers in the operation processes, we make the following assumptions: (1) All manufacturers sell the product to the retailers at the same unit price w; (2) different manufacturers (or retailers) have the same production (or replenishment) lead time of one period; (3) overstock material of a manufacturer at the end of each period can be returned to the suppliers; (4) producing (or selling) one unit product requires one unit capacity; (5) capacity of each member deteriorates with time at a constant rate $\left. \left. 0 < \delta \leq 1 \right. ; ( 6 ) \right.$ each member has a chance of capacity investment at the beginning of each period.

In period $t ~ ( t { = } 1 , 2 , . . . , T )$ , the sequence of events followed by supply chain member x (x=i or $j , \ i = 1 , \ 2 , \ . . . , \ I ; \ j = 1 , \ 2 , \ . . . , \ J )$ is outlined as follows.

Step 1. At the beginning of period t, member x reviews its inventory position and <sup>fi</sup>nancial situation, and decides how much to order from its immediate upstream members $( Q _ { x } ^ { t } )$ , how much capacity to invest (y<sup>t</sup>). After capacity investment, capacity of member x at the beginning of period t is $\bar { K _ { x } ^ { t - 1 } } + y _ { x } ^ { t } \ : ( y _ { x } ^ { t } + K _ { x } ^ { t - 1 } \geq 0 )$ . In case when member x has insuf<sup>fi</sup>cient money for capacity investment, it can borrow $B _ { x } ^ { t }$ from exogenous <sup>fi</sup>nancial institutions with a constant interest rate $r ( r { > } 0 )$

$$
B _ {x} ^ {t} = \left\{ \begin{array}{l l} \big (c _ {i} Q _ {i} ^ {t} + k _ {i} y _ {i} ^ {t} - A _ {i} ^ {t - 1} \big) ^ {+}, & \text {if x = i} \\ \big (\big (f \big (\phi_ {j} \big) w + c _ {j} \big) Q _ {j} ^ {t} + k _ {j} y _ {j} ^ {t} - A _ {j} ^ {t - 1} \big) ^ {+}, & \text {if x = j}. \end{array} \right.\tag{4}
$$

In Eq. $( 4 ) , \phi _ { j } \ ( 0 \leq \phi _ { j } \leq 1 )$ is the proportion of payment paid by retailer j to manufacturers when the order is placed at the beginning of period $t , f ( \phi _ { j } ) = 1$ when retailer j is in <sup>fi</sup>nancial distress at the end of period $t - 1$ and $f ( \phi _ { j } ) = \phi _ { j } < \mathbf { \bar { \phi } }$ 1 otherwise. We term ϕ as the proportion of up-front payment [4]. Eq. (4) indicates that the amount of money to be borrowed depends on the difference between the total costs of procurement and capacity investment $( \mathrm { i . e . , } c _ { i } Q _ { i } ^ { t } + k _ { i } y _ { i } ^ { t }$ or $( f ( \phi _ { j } ) w + c _ { j } )$ $Q _ { j } ^ { t } + k _ { j } y _ { j } ^ { t } )$ and the cash on hand $( \mathrm { i } . \mathrm { e } . , A _ { x } ^ { t - 1 } )$ . Decisions on $Q _ { x } ^ { t }$ and $y _ { x } ^ { t }$ will be elaborated in the next subsection.

Step 2. Member x then receives products or materials from its immediate upstream members, which was ordered at the beginning of period t or before period t (in case of backorders).

If member x is the manufacturer $( x = i )$ , it receives materials from outside suppliers with ample raw material, and the received quantity equals the ordered quantity. If member x is the retailer $\left( x = j \right)$ , the received quantity may not equal the ordered quantity. That is,

$$
I R _ {x} ^ {t} = \left\{ \begin{array}{l l} Q _ {i} ^ {t}, & \text { if } x = i \\ \sum_ {i = 1} ^ {I} I S _ {i j} ^ {t}, & \text { if } x = j \end{array} \right.,\tag{5}
$$

where $I S _ { i j } ^ { t }$ denotes the quantity of product received by retailer j from manufacturer i in period t.

Step 3. At the end of period t, member x observes demand realization from its immediate downstream members (or from the retail market).

$\operatorname { I f } x = j ,$ the realized demand of retailer j in period t $D _ { j } ^ { t } ,$ is described by Eq. $( 2 ) . \operatorname { I f } x = i ,$ , the realized demand of manufacturer i in period t, $D _ { i } ^ { t } ,$ is the sum of the orders placed by all retailers to manufacturer i at the beginning of period t. Denote by $Q _ { j i } ^ { t }$ the quantity of order placed by retailer j to manufacturer i in period t, then we have $D _ { i } ^ { t } = \sum _ { j = 1 } ^ { J } \ Q _ { j i } ^ { t } .$

Step 4. Member x then sells product to meet demand, as well as backorders if there is any, of its downstream members. Note that the maximal quantity of product member x can provide in period $t , S _ { x } ^ { t } ,$ is limited by its capacity and the on-hand inventory received from its upstream partners, i.e.,

$$
S _ {x} ^ {t} = \left\{ \begin{array}{l l} Y _ {i} ^ {t} + I H _ {i} ^ {t - 1}, & \text { if } x = i \\ m i n \Bigl \{I R _ {j} ^ {t} + I H _ {j} ^ {t - 1}, K _ {j} ^ {t - 1} + y _ {j} ^ {t} \Bigr \}, & \text { if } x = j \end{array} \right.,\tag{6}
$$

where $Y _ { i } ^ { t } { = } u _ { i } ^ { Y } \operatorname* { m i n } \{ I R _ { i } ^ { t } , \ K _ { i } ^ { t - 1 } { + } y _ { i } ^ { t } \} , \ u _ { i } ^ { Y }$ is a random variable on the support of $[ 0 , \ 1 ] .$ . Here we assume that production quality of a manufacturer is not zero-defect, and we use $u _ { i } ^ { Y }$ to describe quality level of product of manufacturer i.

The quantity of product that member x sells in period $t , I S _ { x } ^ { t } ,$ is limited by its total demand (i.e., $D _ { x } ^ { t } + I B _ { x } ^ { t - 1 } )$ and $S _ { x } ^ { t } .$ So we have

$$
I S _ {x} ^ {t} = \min \left\{D _ {x} ^ {t} + I B _ {x} ^ {t - 1}, S _ {x} ^ {t} \right\}.\tag{7}
$$

$$
I H _ {x} ^ {t} = \left(S _ {x} ^ {t} - D _ {x} ^ {t} - I B _ {x} ^ {t - 1}\right) ^ {+},\tag{8}
$$

$$
I B _ {x} ^ {t} = \left(D _ {x} ^ {t} + I B _ {x} ^ {t - 1} - S _ {x} ^ {t}\right) ^ {+}.\tag{9}
$$

The overstock inventory (described by Eq. (7)) is assumed to be hold to the next period, and the stockout (described by Eq. (8)) is backordered. In Eqs. (7) and $( 8 ) , ( u ) ^ { + } = \operatorname* { m a x } \{ 0 , u \}$

Note that when member x is the manufacturer $( x = i )$ , it is possible that a manufacturer cannot meet its total demand $( \mathrm { i . e . , } D _ { i } ^ { t } + I B _ { i } ^ { t - 1 } )$ from all retailers. In this case, following [20] we assume that the manufacturer distributes the product to retailers in proportion to the total demands of retailers.

## 3.3. Order and financial decisions

In each period, a supply chain member makes operational and <sup>fi</sup>nancial decisions to determine the quantity of material (or product) to be ordered, capacity investment, and money to be borrowed from exogenous <sup>fi</sup>nancial institutions. We next respectively describe the decision processes of manufacturers and retailers.

## 3.3.1. Decision of manufacturer

Denote by $\hat { D } _ { i } ^ { t }$ the forecasted demand of member i in period t. When market demand is a stationary time series, the demand faced by each manufacturer is also a stationary time series. For a stationary time series, simple exponential smoothing is a commonly used forecast technique [30]. According to the simple exponential smoothing method, the current forecast is the weighted average of the current value of demand and the last forecast, that is,

$$
\hat {D} _ {i} ^ {t} = \alpha_ {i} ^ {f} D _ {i} ^ {t - 1} + \left(1 - \alpha_ {i} ^ {f}\right) \hat {D} _ {i} ^ {t - 1},\tag{10}
$$

where $0 \leq \alpha _ { l } ^ { f } \leq 1$ denotes the smoothing constant of demand fore casting of manufacturer i.

In determining the order quantity, the traditional decision-making criteria focus on optimizing cost or pro<sup>fi</sup>t while ignoring <sup>fi</sup>nancial constraints. It is pointed out by Babich & Sobel [5] that, this kind of criteria can encourage poor performance of entrepreneurial <sup>fi</sup>rm, because the <sup>fi</sup>rm may suffer cash <sup>fl</sup>ow risk and incur substantial <sup>fi</sup>nancial cost. Based on the optimization model in [5] and the observations in [21], we assume that a <sup>fi</sup>rm determines order quantity to maximize its estimated pro<sup>fi</sup>t when the cash <sup>fl</sup>ow risk is low, but to maximize its estimated net cash <sup>fl</sup>ow when the cash <sup>fl</sup>ow risk is high.

Denote by $\mathbf { \hat { \boldsymbol { \pi } } } _ { i } ^ { t }$ and $\hat { \mathrm { \mathbf { v } } } _ { i } ^ { t }$ the estimated pro<sup>fi</sup>t and the estimated net cash in<sup>fl</sup>ow of manufacturer i in period t. Then we have

$$
\begin{array}{l} \widehat {\pi} _ {i} ^ {t} = (w - c _ {i}) \widehat {I S} _ {i} ^ {t} - \delta_ {i} k _ {i} \left(K _ {i} ^ {t - 1} + y _ {i} ^ {t}\right) - c _ {i} \left(\min \left\{Q _ {i} ^ {t}, K _ {i} ^ {t - 1} + y _ {i} ^ {t} \right\} - E \left(Y _ {i} ^ {t}\right)\right) \\ - r B _ {i} ^ {t} - h _ {i} \widehat {I H} _ {i} ^ {t} - s _ {i} \widehat {I B} _ {i} ^ {t}, \end{array} \tag {11}\tag{11}
$$

$$
\widehat {v} _ {i} ^ {t} = w \widehat {I S} _ {i} ^ {t} - c _ {i} \min \left\{Q _ {i} ^ {t}, K _ {i} ^ {t - 1} + y _ {i} ^ {t} \right\} - k _ {i} y _ {i} ^ {t} - r B _ {i} ^ {t} - h _ {i} \widehat {I H} _ {i} ^ {t} - s _ {i} \widehat {I B} _ {i} ^ {t},\tag{12}
$$

with $\widehat { I S } _ { i } ^ { t } = m i n \Big \{ E \Big ( Y _ { i } ^ { t } \Big ) + I H _ { i } ^ { t - 1 } , \widehat { D } _ { i } ^ { t } + I B _ { i } ^ { t - 1 } \Big \} , \widehat { I H } _ { i } ^ { t } = ( E ( Y _ { i } ^ { t } ) + I H _ { i } ^ { t - 1 } -$ $\widehat { I S } _ { i } ^ { t } ) ^ { + } , \widehat { I B } _ { i } ^ { t } = \left( \hat { D } _ { i } ^ { t } + \check { I B } _ { i } ^ { t - 1 } - \widehat { I S } _ { i } ^ { t } \right) ^ { + }$ þ. In Eqs. (11) and (12), parameter $\delta _ { i }$ $( 0 < \delta _ { i } < 1 )$ denotes the deterioration rate of capacity of manufacturer i, $k _ { i }$ denotes the unit cost of capacity investment of manufacturer i in each period, and E(Y<sup>t</sup>) is the expectation value of $Y _ { i \cdot } ^ { t }$

We assume that manufacturer i has a threshold level about the estimated net cash <sup>fl</sup>ow, $- ( 1 - \omega _ { i } ) A _ { i } ^ { 0 }$ , in determining its order quantity (Q<sup>t</sup>) and capacity investment (y<sup>t</sup>): if problem max πˆ <sup>t</sup> has optimal Q <sup>t</sup> ;y<sup>t</sup>

solutions in the feasible set $\left\{ \left( Q _ { i } ^ { t } , y _ { i } ^ { t } \right) | \hat { \mathbf { v } } _ { i } ^ { t } { \geq } - ( 1 - \mathbf { \omega } _ { \omega _ { i } } ) A _ { i } ^ { 0 } \right\}$ , then manufac-<sup>j ð Þ</sup>turer i makes decisions on Q<sup>t</sup> and y<sup>t</sup> to maximize $\hat { \boldsymbol { \pi } } _ { i } ^ { t } ;$ otherwise, manufacturer i makes decisions on $Q _ { i } ^ { t }$ and $y _ { i } ^ { t }$ to maximize $\hat { \mathbf { v } } _ { i } ^ { t }$ instead. Parameter $\omega _ { i }$ in the threshold level describes the maximal risk of cash <sup>fl</sup>ow that manufacturer i is willing to take in maximizing its estimated pro<sup>fi</sup>t: a larger value of ω implies a low cash-<sup>fl</sup>ow risk that manufacturer i is willing to take, and vice versa.

## 3.3.2. Decision of retailer

In addition to the similar operational and <sup>fi</sup>nancial decisions described above, a retailer needs a schema to split its total order quantity among manufacturers in each period. This schema describes the requirement of a retailer on manufacturers, which may induce the competition among manufacturers in ful<sup>fi</sup>lling the retailer's order. Since demand of a retailer is a function of the retail prices of all retailers, retail price is also an important decision to be made.

3.3.2.1. Demand forecasting. Recall that we assume that demand of retailer j in period $t , D _ { j } ^ { t } ,$ , is elastic in the retail prices of all retailers, so we separate $D _ { j } ^ { t }$ into two parts, i.e., the random demand $\varepsilon _ { j } ^ { t }$ and the elastic demand $d _ { j } ^ { t } ,$ where $\varepsilon _ { j } ^ { t }$ is independent of $d _ { j } ^ { t } .$ . Consequently, the random demand and the elastic demand can be forecasted separately. Denote by $\hat { \varepsilon } _ { j } ^ { t }$ and $\hat { d } _ { j } ^ { t }$ the forecasted random demand and the forecasted elastic demand of retailer j in period t, respectively. Then the forecasted demand of retailer j in period $t , \hat { D } _ { i } ^ { t } ,$ is

$$
\hat {D} _ {j} ^ {t} = \hat {d} _ {j} ^ {t} + \hat {\varepsilon} _ {j} ^ {t}.\tag{13}
$$

In Eq. (13), $\hat { d } _ { i } ^ { t }$ and $\hat { \mathbf { g } } _ { j } ^ { t }$ can be computed separately.

3.3.2.1.1. Process of computing $\hat { \varepsilon } _ { j } ^ { t } .$ Suppose that retail price of any retailer in period $t - 1$ is known by other $J - 1$ retailers at the end of period $t - 1$ . Thus the elastic demand of retailer j in period $t - 1 ( d _ { j } ^ { t - 1 }$ $( \mathbf { p } ^ { \mathbf { t } - \mathbf { 1 } } ) )$ can be computed at the end of period $t - 1$ according to Eq. (3), and then the realized random demand in period $t - 1 \ ( \varepsilon _ { j } ^ { t - 1 } )$ can be computed at the end of period t−1 according to Eq. (2). Following the simple exponential smoothing method, the forecasted random demand in period $t , \hat { \mathbf { g } } _ { j } ^ { t } ,$ is

$$
\hat {\varepsilon} _ {j} ^ {t} = \alpha_ {j} ^ {f} \varepsilon_ {j} ^ {t - 1} + (1 - \alpha_ {j} ^ {f}) \hat {\varepsilon} _ {j} ^ {t - 1},\tag{14}
$$

where α<sub>j</sub> $\stackrel { \cdot } { ( 0 \leq \alpha _ { j } ^ { f } \leq 1 ) }$ is the smoothing constant of demand forecasting of retailer j.

3.3.2.1.2. Process of determining $\hat { d } _ { j } ^ { t }$ . The elastic demand of retailer j in period $; d _ { j } ^ { t } ,$ is a function of all retailers' retail price in period t. Thus, to forecast $d _ { j } ^ { t } ,$ retailer j needs <sup>fi</sup>rst to estimate p<sup>t</sup> $( l = 1 , 2 , . . . , J )$ of all retailers' retail price at the beginning of period t. Suppose all retailers determine their retail prices under their own decision criteria to optimize their own decision objectives (e.g., pro<sup>fi</sup>t maximization or cash <sup>fl</sup>ow maximization). The decision process is complicated by the facts that cost parameters of retailers are their private information, and that demand of each retailer in each period depends not only on its own retail price but also on the retail prices of other retailers. As a result, it is a challenging problem for each retailer to decide its retail price before knowing the retail prices of other retailers. One approach for solving this problem is: retailer j determines its retail price in period t by assuming that other retailers maintain their retail prices in period t as those in period t−1, then retailer j determines a retail price by optimizing its own decision objective in period t (this method of determining the retail price is termed the “best response dynamic policy” [33]).

Denote by $\mathbf { p _ { - j } ^ { t _ { - 1 } } }$ the retail-price vector of all J retailers except retailer j in period $t - 1 , \mathrm { i . e . , } \ \mathbf { p . \bar { 5 } _ { j } } ^ { \bar { 6 } - 1 } = ( p _ { 1 } ^ { t - 1 } , . . . , p _ { j - 1 } ^ { t - } , p _ { j + 1 } ^ { t - 1 } , . . . , p _ { J } ^ { t - } { } ^ { \bar { 1 } } )$ According to the decision method described above, retailer j determines a retail price at the beginning of period $t , p _ { j } ^ { t } ,$ , and estimates the elastic demand $\hat { d } _ { j } ^ { t }$ based on p<sup>t</sup> and $\mathbf { p _ { - j } ^ { t _ { - 1 } } }$ . Then we have

$$
\hat {d} _ {j} ^ {t} \left(p _ {j} ^ {t}, \mathbf {p} _ {- \mathbf {j}} ^ {\mathbf {t} - 1}\right) = a _ {j} - b _ {j} \left(p _ {j} ^ {t} - \sum_ {l = 1, l \neq j} ^ {J} \theta_ {j l} p _ {l} ^ {t - 1}\right),\tag{15}
$$

In Eq. (15), $\hat { d } _ { j } ^ { t } \left( p _ { j } ^ { t } , \mathbf { p } _ { - \mathbf { j } } ^ { \mathbf { t } - 1 } \right)$ indicates that $\hat { d } _ { j } ^ { t }$ is a function of $p _ { j } ^ { t }$ and $\mathbf { p _ { - j } ^ { t - 1 } }$

3.3.2.2. Pricing, ordering and capacity investment. Denote by $\hat { \boldsymbol { \pi } } _ { i } ^ { t }$ and $\hat { \mathbf { v } } _ { i } ^ { t }$ the estimated pro<sup>fi</sup>t and net cash in<sup>fl</sup>ow of retailer j in period t. Then we have

$$
\hat {\pi} _ {j} ^ {t} = \left(p _ {j} ^ {t} - w - c _ {j}\right) \widehat {I S} _ {j} ^ {t} - \delta_ {j} k _ {j} \left(K _ {j} ^ {t - 1} + y _ {j} ^ {t}\right) - r B _ {j} ^ {t} - h _ {j} \widehat {I H} _ {j} ^ {t} - s _ {j} \widehat {I B} _ {j} ^ {t},\tag{16}
$$

$$
\hat {v} _ {j} ^ {t} = p _ {j} ^ {t} \widehat {I S} _ {j} ^ {t} - (w + c _ {j}) Q _ {j} ^ {t} - k _ {j} y _ {j} ^ {t} - r B _ {j} ^ {t} - h _ {j} \widehat {I H} _ {j} ^ {t} - s _ {j} \widehat {I B} _ {j} ^ {t},\tag{17}
$$

with $\widehat { I S } _ { j } ^ { t } = m i n \Big \{ S _ { j } ^ { t } , \widehat { D } _ { j } ^ { t } + I B _ { j } ^ { t - 1 } \Big \} , \widehat { I H } _ { j } ^ { t } = \Big ( S _ { j } ^ { t } - \widehat { D } _ { j } ^ { t } - I B _ { j } ^ { t - 1 } \Big ) ^ { + } , \widehat { I B } _ { j } ^ { t } = \Big ( \widehat { D } _ { j } ^ { t } + I B _ { j } ^ { t - 1 } - S _ { j } ^ { t } \Big ) ^ { + }$ 4 and $S _ { j } ^ { t }$ is described in Eq. (6). Parameter $\delta _ { j } \ : \ : \left( 0 < \delta _ { j } < 1 \right)$ denotes the deterioration rate of capacity of retailer j, and $k _ { j }$ is the unit cost of capacity investment of retailer j in each period.

Similar to the manufacturer, retailer j is also assumed to have a threshold level about the estimated net cash <sup>fl</sup>ow, $- ( 1 - \omega _ { j } ) A _ { j } ^ { 0 }$

$$
\hat {\pi} _ {j} ^ {t}
$$

$$
\left(p _ {j} ^ {t}, Q _ {j} ^ {t}, y _ {j} ^ {t}\right)
$$

$\left\{ \left( p _ { j } ^ { t } , Q _ { j } ^ { t } , y _ { j } ^ { t } \right) | \hat { \mathbf { v } } _ { j } ^ { t } { \geq } - ( 1 - \omega _ { j } ) A _ { j } ^ { 0 } \right\}$ , then retailer j makes decisions on $p _ { j } ^ { t } ,$ $\grave { Q } _ { j } ^ { t }$ and $y _ { j } ^ { t }$ to maximize πˆ <sup>t</sup>; otherwise, retailer j makes decisions on p<sup>t</sup>, $Q _ { j } ^ { t }$ and y<sub>j</sub><sup>t</sup> to maximize $\hat { \mathrm { \mathbf { v } } } _ { j } ^ { t } .$ . Parameter ω<sub>j</sub> describes the maximal risk of cash <sup>fl</sup>ow that retailer j is willing to take in maximizing its estimated pro<sup>fi</sup>t.

Denote by $p _ { j } ^ { t ^ { * } }$ the retail price that is obtained by solving problem max $\hat { \boldsymbol { \pi } } _ { j } ^ { t }$ or max $\hat { \mathrm { \mathbf { v } } } _ { j } ^ { t } ,$ . By substituting $p _ { j } ^ { t ^ { * } }$ into Eq. (15), $\hat { d } _ { j } ^ { t } \left( p _ { j } ^ { t } , \mathbf { p } _ { - \mathbf { j } } ^ { \mathbf { t } - 1 } \right)$ is $\begin{array} { r } { \left( p _ { j } ^ { t } , Q _ { j } ^ { t } , y _ { j } ^ { t } \right) \qquad J ^ { \prime } \qquad \left( p _ { j } ^ { t } , Q _ { j } ^ { t } , y _ { j } ^ { t } \right) } \end{array}$ +\*

$$
B _ {j} ^ {t},
$$

$$
Q _ {i} ^ {t ^ {*}}
$$

$$
y _ {j} ^ {t ^ {*}}
$$

3.3.2.3. Order allocation scheme. In ordering decision, after retailer j has determined total order quantity in period t (i.e., Q<sub>j</sub><sup>t</sup>), a followed decision is to split the total order quantity among manufacturers. We assume that order of a retailer is allocated to manufacturers according to their service levels in the previous periods. This kind of order allocation scheme has been widely used in the multiple-supplier inventory literature (e.g., [7,12]).

Denote by $\chi _ { j i } ^ { t } ~ ( 0 \leq \chi _ { j i } ^ { t } \leq 1 )$ the proportion of orders allocated by retailer j to manufacturer i in period t. Then the order quantity received by manufacturer i from retailer j is $Q _ { j i } ^ { t } { = } \chi _ { j i } ^ { t } Q _ { j } ^ { t }$ . According to this allocation scheme, $Q _ { j i } ^ { t }$ depends on the service level of manufacturer i in the previous periods. Denote by γ<sup>t</sup> $( 0 \leq \gamma _ { i j } ^ { t } \leq 1 )$ the percentage of the allocated order of retailer j to manufacturer $i \ ( \mathrm { i . e . }$ $\chi _ { j i } ^ { t } Q _ { j } ^ { t } )$ ful<sup>fi</sup>lled by manufacturer i in period t, and de<sup>fi</sup>ne γ<sup>t</sup> as the service level of manufacturer i perceived by retailer j in period t. Then, for all $t \geq 1$

$$
\chi_ {j i} ^ {t + 1} = \alpha_ {j} ^ {O A} \gamma_ {i j} ^ {t} \chi_ {j i} ^ {t} \Bigg / \sum_ {i = 1} ^ {I} \gamma_ {i j} ^ {t} \chi_ {j i} ^ {t} + \left(1 - \alpha_ {j} ^ {O A}\right) \chi_ {j i} ^ {t},\tag{19}
$$

where $\alpha _ { j } ^ { O A } ~ ( 0 { \leq } \alpha _ { j } ^ { O A } { \leq } 1 )$ is the smoothing factor of order allocation, and the superscript OA denotes order allocation. $\chi _ { j i } ^ { 1 } = 1 / 1$ I for all i and j.

## 3.4. Financial status and bankruptcy

From the perspective of <sup>fi</sup>nancial management, <sup>fi</sup>nancial status of a <sup>fi</sup>rm can be qualitatively classi<sup>fi</sup>ed into three states [32]: (1) sound, a situation when cash <sup>fl</sup>ow of a <sup>fi</sup>rm generated by its operating activities is high enough to pay its due debt; (2) <sup>fi</sup>nancial distress, a situation when cash <sup>fl</sup>ow of a <sup>fi</sup>rm generated by operating activities is too low to compensate its due debt, i.e., a low cash-<sup>fl</sup>ow state; and (3) bankrupt, a situation when total assets of a <sup>fi</sup>rm is lower than its total debt, i.e., the net assets falls below zero.

Before giving de<sup>fi</sup>nitions of <sup>fi</sup>nancial status and bankruptcy, we <sup>fi</sup>rst describe members' asset updating process. According to the operation process of supply chain members described above, the pro<sup>fi</sup>t and net cash in<sup>fl</sup>ow of retailer $i ~ ( j = 1 , 2 , . . . , J )$ at the end of period t can be computed by

$$
\pi_ {j} ^ {t} = \left(p _ {j} ^ {t} - w - c _ {j}\right) I S _ {j} ^ {t} - \delta_ {j} k _ {j} \left(K _ {j} ^ {t - 1} + y _ {j} ^ {t}\right) - r B _ {j} ^ {t} - h _ {j} I H _ {j} ^ {t} - s _ {j} I B _ {j} ^ {t} + \sum_ {i = 1} ^ {I} s _ {i} I B _ {i j} ^ {t},\tag{20}
$$

$$
v _ {j} ^ {t} = p _ {j} ^ {t} I S _ {j} ^ {t} - \left(w + c _ {j}\right) I R _ {j} ^ {t} - k _ {j} y _ {j} ^ {t} - r B _ {j} ^ {t} - h _ {j} I H _ {j} ^ {t} - s _ {j} I B _ {j} ^ {t} + \sum_ {i = 1} ^ {I} s _ {i} I B _ {i j} ^ {t}.\tag{21}
$$

In Eq. (20), the pro<sup>fi</sup>t of retailer j at the end of period t is calculated by (sales revenue−purchasing and selling costs of sold goods−deterioration cost of capacity−cost of interest−inventory holding cost−shortage penalty cost+shortage penalty costs paid by the manufacturers). For retailer $j ,$ the cash in<sup>fl</sup>ow at the end of period t is the sum of realized profit, the purchasing cost of sold goods in the period and shortage penalty costs paid by the manufacturers; the cash out<sup>fl</sup>ow at the end of period t equals the sum of purchasing cost it paid to its upstream manufacturers for the goods it received in period t, the selling cost incurred in the process of goods selling, the cost of capacity investment and the cost of interest. As shown in Eq. (21), the net cash in<sup>fl</sup>ow of retailer j at the end of period t equals the difference between cash in<sup>fl</sup>ow and cash out<sup>fl</sup>ow.

Similarly, the pro<sup>fi</sup>t and net cash in<sup>fl</sup>ow of manufacturer $i ( i = 1$ $2 , . . . , I )$ at the end of period t are calculated by

$$
\begin{array}{l} \pi_ {i} ^ {t} = (w - c _ {i}) I S _ {i} ^ {t} - \delta_ {i} k _ {i} \left(K _ {i} ^ {t - 1} + y _ {i} ^ {t}\right) - \left(1 - u _ {i} ^ {Y}\right) c _ {i} \min \left\{I R _ {i} ^ {t}, K _ {i} ^ {t - 1} + y _ {i} ^ {t} \right\} \\ - r B _ {i} ^ {t} - h _ {i} I H _ {i} ^ {t} - s _ {i} I B _ {i} ^ {t} - B D _ {i} ^ {t}, \end{array} \tag {2}\tag{22}
$$

$$
v _ {i} ^ {t} = w I S _ {i} ^ {t} - c _ {i} \min \left\{I R _ {i} ^ {t}, K _ {i} ^ {t - 1} + y _ {i} ^ {t} \right\} - k _ {i} y _ {i} ^ {t} - r B _ {i} ^ {t} - h _ {i} I H _ {i} ^ {t} - s _ {i} I B _ {i} ^ {t} - B D _ {i} ^ {t}.\tag{23}
$$

In Eqs. (22) and (23), $( 1 - u _ { i } ^ { Y } ) c _ { i } \ \operatorname * { m i n } \{ I R _ { i } ^ { t } , \ K _ { i } ^ { t - 1 } + y _ { i } ^ { t } \}$ is the purchasing cost of manufacturer i for the product that has defect in period t. BD<sub>i</sub><sup>t</sup> is the bad debt of manufacturer i in period t caused by retailers' bankruptcies, which will be further elaborated after the de<sup>fi</sup>nition of bankruptcy.

The net assets of member x at the end of period t is assumed to include four parts: cash on hand $\left( A _ { x } ^ { t } \right)$ , overstock inventory $( c _ { x } I H _ { x } ^ { t } )$ capacity $( k _ { x } K _ { x } ^ { t }$ , where $K _ { x } ^ { t } \mathbf { = } ( 1 - \delta _ { x } ) ( \overset { \cdot } { K } _ { x } ^ { t - 1 } + y _ { x } ^ { t } ) )$ ), and long-term investment $( \eta _ { x } ^ { t } )$ . Long-term investment of member x is the investment of the member on other products or projects. We assume that a proportion $\tau _ { x } \left( 0 \leq \tau _ { x } \leq 1 \right)$ of the pro<sup>fi</sup>t of member x at the end of period $t , \pi _ { x } ^ { t } ,$ , is retained to increase its net assets i $\mathrm { \Delta } \mathrm { f } \pi _ { x } ^ { t } { > } 0 ;$ ; otherwise, a negative pro<sup>fi</sup>t directly decreases its net assets. Then the updating process of the net assets of member x at the end of period t can be formulated as follows,

$$
A _ {x} ^ {t} + c _ {x} I H _ {x} ^ {t} + k _ {x} K _ {x} ^ {t} + \eta_ {x} ^ {t} = \left\{ \begin{array}{l l} \tau_ {x} \pi_ {x} ^ {t} + A _ {x} ^ {t - 1} + c _ {x} I H _ {x} ^ {t - 1} & \text { if } \pi_ {x} ^ {t} > 0 \\ \quad + k _ {x} K _ {x} ^ {t - 1} + u _ {x} ^ {\eta_ {1}} \eta_ {x} ^ {t - 1}, \\ \pi_ {x} ^ {t} + A _ {x} ^ {t - 1} + c _ {x} I H _ {x} ^ {t - 1} & \text { otherwise }, \\ \quad + k _ {x} K _ {x} ^ {t - 1} + u _ {x} ^ {\eta_ {1}} \eta_ {x} ^ {t - 1}, \end{array} \right.\tag{24}
$$

where $u _ { x } ^ { \eta }$ is a random variable which represents the return uncertainty of the long-term investment of member x in each period.

The net cash in<sup>fl</sup>ow of member x in each period could increase or decrease its cash on hand. We assume that member x sets an upper threshold level about its cash on hand at the end of each period, $( 1 + \omega _ { x } )$ $A _ { x } ^ { 0 . } { \mathrm { i f } }$ the net cash in<sup>fl</sup>ow of member x in period t (υ<sup>t</sup>) plus its cash on hand at the end of period $t - 1 ~ ( A _ { x } ^ { t - 1 } )$ is smaller than $( 1 + \omega _ { x } ) A _ { x } ^ { 0 }$ , then the cash on hand of member x at the end of period $t \left( A _ { x } ^ { t } \right)$ equals the sum of $v _ { x } ^ { t } \mathrm { a n d } A _ { x } ^ { t - 1 } ;$ otherwise, $A _ { x } ^ { t }$ is set at the level of $( 1 + \omega _ { x } ) A _ { x } ^ { 0 }$ , and the rest part of the net cash in<sup>fl</sup>ow, $A _ { x } ^ { t - 1 } + v _ { x } ^ { t } - ( 1 + \omega _ { x } ) A _ { x } ^ { 0 }$ , is used as long-term investment. Based on the above assumption, we have

$$
A _ {x} ^ {t} = \min \left\{A _ {x} ^ {t - 1} + v _ {x} ^ {t}, (1 + \omega_ {x}) A _ {x} ^ {0} \right\},\tag{25}
$$

and

$$
\eta_ {x} ^ {t} = \left\{ \begin{array}{l l} u _ {x} ^ {\eta} \eta_ {x} ^ {t - 1} + \left(A _ {x} ^ {t - 1} + v _ {x} ^ {t} - (1 + \omega_ {x}) A _ {x} ^ {0}\right) ^ {+} - (1 - \tau_ {x}) \pi_ {x} ^ {t}, & \text { if } \pi_ {x} ^ {t} > 0 \\ u _ {x} ^ {\eta} \eta_ {x} ^ {t - 1} + \left(A _ {x} ^ {t - 1} + v _ {x} ^ {t} - (1 + \omega_ {x}) A _ {x} ^ {0}\right) ^ {+}, & \text { otherwise } \end{array} \right.\tag{26}
$$

In Eq. $( 2 6 ) , ( 1 - \tau _ { x } ) \pi _ { x } ^ { t }$ is the dividends distributed by member x at the end of period t.

Member x is de<sup>fi</sup>ned to fall into the state of financial distress at the end of period t if its cash on hand becomes negative at the end of this period, $\mathrm { i } . \mathrm { e } . , A _ { x } ^ { t } { < } 0 .$ . Once a <sup>fi</sup>rm falls into <sup>fi</sup>nancial distress at the end of a period, deadweight losses will be imposed in the form of accelerated debt repayment, increased <sup>fi</sup>nancing costs for raising money, managerial time and resources spent on negotiations with the lenders, etc. [32]. Andrade and Kaplan [3] estimated the cost of <sup>fi</sup>nancial distress as 10– 20% of <sup>fi</sup>rm value. Based on the existing literature, we assume that if member x falls into <sup>fi</sup>nancial distress at the end of period t, it will incur a <sup>fi</sup>nancial cost that is proportional to its total assets, and is also affected by its <sup>fi</sup>nancial leverage [32]. That is,

$$
C _ {x} ^ {t} = \lambda e ^ {2 l e v _ {x} ^ {t}} \left(B _ {x} ^ {t} + A _ {x} ^ {t} + c _ {x} I H _ {x} ^ {t} + k _ {x} K _ {x} ^ {t} + \eta_ {x} ^ {t}\right).\tag{27}
$$

In $\operatorname { E q . } \left( 2 7 \right)$ , parameter $\lambda \left( 0 \leq \lambda \leq 1 \right)$ is the <sup>fi</sup>nancial distress cost rate, $l e { v } _ { x } ^ { t }$ is the <sup>fi</sup>nancial leverage of member x at the end of period t, which equals the proportion of its debt amount and its total assets, i.e., $l e \bar { \nu } _ { x } ^ { t } { = } B _ { x } ^ { t } / ( B _ { x } ^ { \bar { t } } { + } \bar { A } _ { x } ^ { t } + c _ { x } I H _ { x } ^ { t } + k _ { x } K _ { x } ^ { t } + \eta _ { x } ^ { t } )$

It has been assumed that, 1) when a retailer falls into <sup>fi</sup>nancial distress at the end of period t, the retailer can still place orders to manufacturers at the beginning of period t+1, but need to pay for all its orders when the orders are placed; and 2) if a manufacturer falls into <sup>fi</sup>nancial distress and cannot ful<sup>fi</sup>ll the order of a retailer, the retailer can adjust its order allocation scheme considering the service levels of manufacturers. Following these assumptions, the order received by manufacturers from a distressed retailer can be reduced since the distressed retailer may have insuf<sup>fi</sup>cient capital to pay for all its orders when the orders are placed. Similarly, the order placed by retailers to a distressed manufacturer may also decrease as a result of the decline of the distressed manufacturer's service level. Therefore, the above assumptions implicitly serve as warnings for member <sup>fi</sup>rms to do business with a member that is in the state of <sup>fi</sup>nancial distress.

Member x is de<sup>fi</sup>ned to be bankrupt at the end of period t if its net assets falls below zero at the end of the period $[ 3 2 ] , \mathrm { i } . \mathrm { e } . , A _ { x } ^ { t } + c _ { x } I H _ { x } ^ { t } .$ + $k _ { x } K _ { x } ^ { t } + \eta _ { x } ^ { t } < 0$ . Note that if member x falls into the state of <sup>fi</sup>nancial distress at the end of period t, its net assets at the end of the period will be $A _ { x } ^ { t } + c _ { x } I H _ { x } ^ { t } + k _ { x } \bar { K } _ { x } ^ { t } + \eta _ { x } ^ { t } - C _ { x } ^ { t } .$

Once a <sup>fi</sup>rm goes bankruptcy at the end of period t, it gives nopayment to its upstream members at the end of the period, and will stop supplying its downstream members (or market demands) in the next period [6]. So the bad debt of manufacturer i in period t caused by retailers' bankruptcies, BD<sup>t</sup>, can be expressed as $B D _ { i } ^ { t } = w \sum _ { j = 1 } ^ { J }$ $\left( I R _ { j i } ^ { t } { - } f ( \Phi _ { j } ) Q _ { j i } ^ { t } \right) ^ { + }$ sgn<sup>t</sup>, where $\mathsf { s g n } _ { j } ^ { t } = 1$ if retailer j goes bankruptcy at the end of period t and $\mathsf { s g n } _ { j } ^ { t } \mathop { = } 0$ otherwise. In the next period, the bankrupt <sup>fi</sup>rm is assumed to be replaced by a new <sup>fi</sup>rm with the same links as its predecessor.

## 4. Design of simulation experiments

In this section, we investigate the properties of bankruptcy occurrence and bankruptcy propagation in supply chain network through simulation experiments. The simulation experiments are designed and implemented on the SWARM platform. SWARM is a multi-agent simulation platform designed for studying complex adaptive system (CAS) developed by Santa Fe Institute, which has been shown effective in its applications in the <sup>fi</sup>elds of supply chain management (e.g., [29,38]). We next brie<sup>fl</sup>y describe the simulation model, and then design the simulation experiments.

## 4.1. The simulation model

A SWARM based simulation model is built to simulate the impact of operations on supply chain network (SCN). The SCN Observer Swarm, which entails all the graphical interfaces as well as the SCN Model Swarm, initiates and controls the whole simulation. The SCN Model Swarm schedules movements, information exchanges and in its turn entails the basic objects. In our simulation model, the SCN Model Swarm is composed of N independent identical SCN Entities with the same parameters and actions. The average value of an output index over the N SCN Entities is used to evaluate the impact of operations on SCN. Each SCN Entity is composed of I manufacturer agents and J retailer agents, which are endowed with their own properties, actions and other related information as described in the previous section.

## 4.2. Parameters setting

We assume that the supply chain network has three manufacturers (I=3) and three or six or even nine retailers $( J = 3 , 6 \ \mathrm { o r } \ 9 )$ . It is also assumed that the random demand, $\varepsilon _ { j } ^ { t } ,$ is independent and identically normally distributed with mean $\mu \left( \mu 2 0 \right)$ and variance $\sigma _ { D } ^ { 2 } ( \sigma _ { D } { \geq } 0 )$ . In the simulation experiments, we mainly investigate impacts of nine parameters (including both operational and <sup>fi</sup>nancial parameters), i.e., number of retailers (J), retail competition coef<sup>fi</sup>cient $\left( \theta _ { j l } \right)$ , market demand uncertainty (σ<sub>D</sub>), price elasticity coef<sup>fi</sup>cient of the elastic demand $( b _ { j } )$ , order allocation coef<sup>fi</sup>cient of retailers $( \alpha _ { j } ^ { O A } )$ , wholesale price of manufacturers (w), quality level of product of manufacturers $\bar { ( u _ { i } ^ { Y } ) }$ , maximal risk of cash <sup>fl</sup>ow member x is willing to take in maximizing its pro<sup>fi</sup>t $( \omega _ { x } )$ , and the up-front payment proportion of retailers $\left( \phi _ { j } \right)$ , on bankruptcy propagation. Quality level of product of manufacturers u<sup>Y</sup> $( i = 1 , 2 , . . . , I )$ is assumed to be independent and identically normally distributed with mean 0.85 and variance $\sigma _ { u } ^ { 2 }$ $\left( \sigma _ { u } \ge 0 \right)$ on the support of [0, 1]. That is, if a generated value of u<sup>Y</sup> is negative, we truncate it as zero; if a generated value of u<sup>Y</sup> is larger than one, we truncate it as one. In experiments, we set the nine parameters at different levels, as shown in Table 2.

In all simulation experiments, values of other parameters are set as follows:

(1) Market demand parameters: $a _ { j } = 1 0 0 + b _ { j } ( 1 0 0 - 1 0 0 ( J - 1 ) \theta _ { j l } ) ,$ $\mu { = } 0 .$ . If a generated market demand is negative, we truncate it as zero.

(2) Cost parameters: $p _ { j } ^ { 0 } { = } 1 0 0 , c _ { x } ^ { t } = \left\{ \begin{array} { l l } { 4 5 . 0 + \tilde { c } , } & { \mathrm { i f } x = i } \\ { 5 . 0 + \tilde { c } , } & { \mathrm { i f } x = j } \end{array} \right.$ ; operating cost parameters: $\begin{array} { r } { h _ { x } ^ { t } = \left\{ \begin{array} { l l } { 2 . 2 5 + \tilde { h } , } & { \mathrm { i f } x = i } \\ { 2 . 7 5 + \tilde { h } , } & { \mathrm { i f } x = j } \end{array} , \ s _ { x } = 4 h _ { x } ; \right. } \end{array}$ capacity investment parameter: $k _ { x } ^ { t } = { \left\{ \begin{array} { l l } { 3 0 . 0 + { \tilde { k } } , } & { { \mathrm { i f } } x = i } \\ { 2 5 . 0 + { \tilde { k } } , } & { { \mathrm { i f } } x = j } \end{array} \right. }$ where parameters c̃ and <sup>˜</sup>k are uniformly distributed over the support of (−2.5, 2.5), parameter h<sup>˜</sup> is uniformly distributed over the support of (−0.5, 0.5). That is, c̃ U −2:5; 2:5 , <sup>˜</sup>k U −2:5; 2:5 and h<sup>˜</sup> U −0:5; 0:5 .

<sup>e ð Þ</sup>(3) Exponential smoothing parameter: $\alpha _ { x } ^ { f } { = } 0 . 1$

(4) Return uncertainty of long-term investment: u<sup>η</sup> \~N(1.05, 0.35<sup>2</sup>).

(5) Pro<sup>fi</sup>t, cash and bankruptcy related parameters: $\tau _ { x } = 2 \lambda = 0 . 3$ and $\delta _ { x } = 1 0 r = 0 . 5 .$ . Endowed cash on hand of newly entered agent is set as: $A _ { x } ^ { \mathrm { e n t r y } } = A _ { x } ^ { 0 } = \left\{ \begin{array} { l l } { 1 0 0 0 J , } & { x = i } \\ { 1 0 0 0 I , } & { x = j } \end{array} \right.$

Table 2  
Parameters considered in the experiments and their levels.

<table><tr><td rowspan="2">Parameters</td><td rowspan="2">Description</td><td colspan="3">Levels</td></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td> $J$ </td><td>Number of retailers</td><td>3</td><td>6</td><td>9</td></tr><tr><td> $\sigma_{D}$ </td><td>Standard deviation of the random demand</td><td>30</td><td>40</td><td>50</td></tr><tr><td> $\theta_{jl}$ </td><td>Retail competition coefficient</td><td>0.20 $J-1$ </td><td>0.50 $J-1$ </td><td>0.80 $J-1$ </td></tr><tr><td> $b_{j}$ </td><td>Price elasticity coefficient of demand</td><td>10</td><td>11</td><td>12</td></tr><tr><td> $\alpha_{j}^{OA}$ </td><td>Order allocation coefficient of retailer  $j$ </td><td>0.20</td><td>0.50</td><td>0.80</td></tr><tr><td> $w$ </td><td>Wholesale price of manufacturers</td><td>69.5</td><td>70.0</td><td>70.5</td></tr><tr><td> $\sigma_{u}$ </td><td>Standard deviation of quality level of product of manufacturers</td><td>0.09</td><td>0.10</td><td>0.11</td></tr><tr><td> $\omega_{x}$ </td><td>Risk of cash flow member  $x$  is willing to take</td><td>0.00</td><td>0.20</td><td>0.40</td></tr><tr><td> $\phi_{j}$ </td><td>Up-front payment proportion of retailer  $j$ </td><td>0.20</td><td>0.50</td><td>0.80</td></tr></table>

## 4.3. Output indexes

In simulation experiments, we observe two kinds of output of SCN: 1) occurrences of bankruptcy at each agent; 2) bankruptcy propagation in SCN. We set the length of simulation as 400 periods (T=400), and the number of SCN entities as 10 $( N { = } 1 0 )$ . To measure the occurrences of bankruptcy at each agent, we calculate the expected number of occurrences of bankruptcy at each agent over 10 SCN entities during 400 periods, and de<sup>fi</sup>ne the following output indexes (termed AN indexes hereafter):

ANR Average number of occurrences of bankruptcy over J retailer agents in 400 periods,

ANM Average number of occurrences of bankruptcy over I manufacturer agents in 400 periods,

ANSC Average number of occurrences of bankruptcy over I+J agents in the supply chain in 400 periods.

To measure bankruptcy propagation, we de<sup>fi</sup>ne $A N R _ { t }$ as the average number of occurrences of bankruptcy over J retailer agents in period t, ANM as the average number of occurrences of bankruptcy over I manufacturer agents in period t. It is obvious that $\begin{array} { r } { A N R = \sum _ { t = 1 } ^ { T } A N R } \end{array}$ <sub>t</sub> and $\begin{array} { r } { A N M = \sum _ { t = 1 } ^ { T } A N M _ { t } . } \end{array}$ . We view ANR and ANM $( t = 1 , . . . , 4 0 0 )$ as two bankruptcy series of retailers and manufacturers, respectively. Then we use Cross Correlation Coef<sup>fi</sup>cient between series ANR and ANM as the output index (termed CCC index hereafter) to describe bankruptcy propagation [16,17]. Since bankruptcy of a member in one period may have impacts on the occurrence of bankruptcy of other members in different periods, three CCC indexes are de<sup>fi</sup>ned as follows:

CCC (Lag=−1)

Cross Correlation Coef<sup>fi</sup>cient between ANR and $A N M _ { t - 1 }$

CCC (Lag= 0) Cross Correlation Coef<sup>fi</sup>cient between $A N R _ { t }$ and ANM<sub>t</sub>, CCC (Lag=+1)

Cross Correlation Coef<sup>fi</sup>cient between ANR and $A N M _ { t + 1 }$ <sub>1</sub>,

It is clear that the CCC (Lag=−1) index can be used to describe bankruptcy propagation from manufacturers to retailers; the CCC $( \mathrm { L } \mathrm { a g } = + 1 )$ index can be used to describe bankruptcy propagation from retailers to manufacturers; and the CCC (Lag=0) index can also be interpreted as a measure of bankruptcy propagation from retailers to manufacturers caused by bad debt.

## 5. Simulation results

Given the model parameters, we run the simulation model and obtain the corresponding AN indexes and CCC indexes to investigate impacts of various operational parameters and decisions (listed in Table 2) on bankruptcy propagation. Since many operational decisions of supply chain members are made under <sup>fi</sup>nancial constraints, we also study the linkage between supply chain member's operational decisions and <sup>fi</sup>nancial decisions (e.g., the maximal risk of cash <sup>fl</sup>ow that a member is willing to take, and the up-front payment proportion of retailers in a two-period payment policy) to examine whether operational risks can be hedged through <sup>fi</sup>nancial decisions.

## 5.1. Impacts of operational parameters

To investigate the impacts of operational parameters on bankruptcy propagation, we <sup>fi</sup>rst do experiments by varying levels of seven operational parameters (the <sup>fi</sup>rst seven parameters listed in Table 2). Since there are too many combinations of the parameter levels $( 3 ^ { 7 } = 2 1 8 7 )$ , we use the method of uniform experiment design [14,25] to reduce the number of combinations. According to [14], 39 experiments, which are listed in the website [36], are enough to investigate the impacts of the seven parameters on bankruptcy risks in supply chain. In all of the 39 experiments, we set $\omega _ { x } = 0 . 2$ and $\phi _ { j } = 0 . 5$

Based on the outputs of the 39 experiments, we use linear regression model to investigate impacts of the seven operational parameters on each output index. Let $X _ { 1 } , X _ { 2 } , X _ { 3 } , X _ { 4 } , X _ { 5 } , X _ { 6 }$ and $X _ { 7 }$ denote the seven input indexes J, $\theta _ { j l } , \sigma _ { D } , b _ { j } , \alpha _ { j } ^ { O A }$ , w and $\sigma _ { u }$ respectively, and $\Upsilon _ { 0 } , \Upsilon _ { - 1 } , \Upsilon _ { 1 } , \Upsilon _ { \mathrm { A N R } }$ and $\boldsymbol { \Upsilon } _ { \mathrm { A N M } }$ denote the output indexes CCC (Lag=0), CCC (Lag=−1), CCC (Lag=+1), ANR and ANM, respectively. The following regression models are recommended,

$$
\Upsilon_ {0} = 6. 4 9 3 + 0. 1 1 1 X _ {2} + 0. 0 3 0 X _ {4} - 0. 1 0 1 X _ {6} + 4. 6 0 4 X _ {7},\tag{28}
$$

with R= 0.817, F= 8.909, t<sub>X</sub> = 3.135, t<sub>X</sub> = 2.790, t<sub>X</sub> =−4.772, t<sub>X</sub> =4.334;

$$
\Upsilon_ {- 1} = - 0. 1 5 7 + 0. 0 0 8 X _ {1} + 0. 0 9 2 X _ {2} + 0. 1 3 0 X _ {5},\tag{29}
$$

$$
\text { with } R = 0. 7 0 2, F = 4. 3 0 6, t _ {X _ {1}} = 2. 3 9 6, t _ {X _ {2}} = 2. 7 7 1, t _ {X _ {3}} = 3. 9 2 5;
$$

$$
\Upsilon_ {1} = 1. 9 3 1 + 3. 6 6 5 X _ {7},\tag{30}
$$

$$
\text { with } R = 0. 6 1 7, F = 2. 6 6 0, t _ {X _ {7}} = 3. 1 2 8;
$$

$$
\begin{array}{c} \Upsilon_ {\mathrm{ANR}} = 7 5 4. 1 8 7 + 1 3. 7 1 1 X _ {2} + 0. 2 1 7 X _ {3} + 3. 1 6 0 X _ {4} \\ + 7. 8 5 3 X _ {5} - 1 2. 1 5 8 X _ {6} + 5 8 9. 1 6 7 X _ {7}, \end{array}\tag{31}
$$

$$
\begin{array}{l} \text { with } R = 0. 8 8 0, F = 1 5. 2 3 2, t _ {X _ {2}} = 3. 9 3 9, t _ {X _ {3}} = 2. 0 8 1, t _ {X _ {4}} = 3. 0 2 6, \\ t _ {X _ {5}} = 2. 2 5 6, t _ {X _ {6}} = - 5. 8 2 6 \text { and } t _ {X _ {7}} = 5. 6 4 7; \end{array}
$$

$$
\begin{array}{c} \Upsilon_ {\mathrm{ANM}} = 1 2 4 0. 2 1 0 - 1. 2 2 5 X _ {1} + 2 0. 9 6 1 X _ {2} + 2 1. 0 7 8 X _ {5} \\ - 1 8. 9 2 5 X _ {6} + 6 5 7. 9 6 9 X _ {7}, \end{array}\tag{32}
$$

$$
\begin{array}{l} \text { with } R = 0. 9 2 6, F = 2 6. 8 1 3, t _ {X _ {1}} = - 3. 2 1 7, t _ {X _ {2}} = 5. 5 0 4, t _ {X _ {5}} = 5. 5 3 4, t _ {X _ {6}} = \\ - 8. 2 8 7 \text { and } t _ {X _ {7}} = 5. 7 6 3. \end{array}
$$

In Eqs. (28)–(32), R is the correlation between the observed and predicted values of the dependent variable. The F statistic is the regression mean square divided by the residual mean square, which is used to examine whether the obtained regression model is signi<sup>fi</sup>cant. The $t _ { X }$ statistic is the t-value of the t-test of the regression coef<sup>fi</sup>cient of X, which is used to examine whether the independent variable X has signi<sup>fi</sup>cant linear impact on each output index. All the F-tests and t-tests above are signi<sup>fi</sup>cant at the signi<sup>fi</sup>cant level of 0.05.

Several conclusions can be drawn from the above results:

(1) Parameter $\theta _ { j l }$ has signi<sup>fi</sup>cant impact on both the CCC indexes and the AN indexes. With the increase in $\theta _ { j l } ,$ bankruptcy occurrence and bankruptcy propagation monotonically increase. Thus horizontal competition among retailers is one of the main sources of bankruptcy occurrence and bankruptcy propagation in the supply chain network.

(2) Demand related parameters $( \sigma _ { D }$ and $b _ { j } )$ have signi<sup>fi</sup>cant positive impacts on the ANR index. That is, with the increase in $\sigma _ { D }$ and $b _ { j } ,$ bankruptcy occurrences at the retailers increase. Thus high uncertainty in market demand and high price elasticity of market demand are important causes of bankruptcy occurrence at the retailers.

(3) Parameter J has signi<sup>fi</sup>cant negative impact on the ANM index. It indicates that, with the increase of the number of retailers in the supply chain network, the number of occurrence of bankruptcy at the manufacturers can be reduced.

(4) Parameter $\alpha _ { j } ^ { O A }$ has signi<sup>fi</sup>cant impacts on the CCC $( \mathrm { L } \mathrm { a g } = - 1 )$ index and all the AN indexes, With the increase in $\alpha _ { j } ^ { O A } ,$ bankruptcy occurrence at all supply chain members and bankruptcy propagation from manufacturers to retailers increase. It is also observed that, the increase of $\alpha _ { j } ^ { O A }$ has larger impact on ANM index than on ANR index. Thus the decision made by a retailer has larger impacts on manufacturers than on itself.

(5) Parameter w has signi<sup>fi</sup>cant negative impacts on CCC (Lag=0) index and all AN indexes. That is, with the increase of the wholesale price of manufacturers, occurrence of bankruptcy at all supply chain members and bankruptcy propagation from the retailers to the manufacturers can be decreased.

(6) Parameter $\sigma _ { u }$ has signi<sup>fi</sup>cant positive impact on both two CCC indexes (CCC (Lag=0) and CCC (Lag=+1)) and all AN indexes. Thus with the increase of the production uncertainty of manufacturers, occurrence of bankruptcy at all supply chain members and bankruptcy propagation from retailers to manufacturers could increase.

To explain how the operational parameters and decisions affect the occurrence and propagation of bankruptcy in the supply chain network, we de<sup>fi</sup>ne three intermediate quantities: the bad debt that will not be paid by downstream retailers because of their bankruptcies (abbreviate as BD), the operating cost that includes inventory holding cost and shortage penalty cost (abbreviated as OC), and the average number of occurrences of <sup>fi</sup>nancial distress over I manufacturers (or J retailers) during T periods (abbreviated as ANF). The three intermediate quantities BD, OC and ANF are calculated by

$$
B D = \frac {1}{T I} \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {I} B D _ {i} ^ {t},\tag{33}
$$

$$
O C _ {r} = \frac {1}{T I} \sum_ {t = 1} ^ {T} \sum_ {j = 1} ^ {J} \left(h _ {j} I H _ {j} ^ {t} + s _ {j} I B _ {j} ^ {t}\right) \text {and} O C _ {m} = \frac {1}{T I} \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {I} \left(h _ {i} I H _ {i} ^ {t} + s _ {i} I B _ {i} ^ {t}\right),\tag{34}
$$

$$
A N F _ {r} = \frac {1}{J} \sum_ {j = 1} ^ {J} N F _ {j} ^ {T} \text { and } A N F _ {m} = \frac {1}{I} \sum_ {i = 1} ^ {I} N F _ {i} ^ {T},\tag{35}
$$

$$
\text { with } N F _ {x} ^ {t} = \left\{ \begin{array}{l l} N F _ {x} ^ {t - 1} + 1, & \text { if } F D _ {x} ^ {t} = t r u e \\ N F _ {x} ^ {t - 1}, & \text { otherwise } \end{array} \right. (x = i \text { or } j; i = 1,..., I; j = 1,
$$

…, J), FD<sup>t</sup> =true denotes member x falls into the state of <sup>fi</sup>nancial distress at the end of period t. The subscripts r and m in Eqs. (34) and (35) denote the retailers and the manufacturers, respectively.

To show the importance of the three intermediate quantities in establishing relationship between operational parameters and bankruptcy propagation, we <sup>fi</sup>rst redo the 39 simulation experiments by setting one or all of the three intermediate quantities as zero. The obtained results indicate that BD, OC and ANF are important causes of the occurrence and propagation of bankruptcy in the supply chain network (detailed results are available from the authors upon request).

We then investigate the impacts of the seven operational parameters on BD, OC and ANF. We redo the 39 experiments and obtain the outputs of BD, OC and ANF under each experiment. Then we evaluate the impacts of each operational parameter on the three intermediate quantities through partial correlation analysis. The results of partial correlation analysis are shown in Table 3.

Partial correlations between operational parameters and output indexes.

<table><tr><td rowspan="2"></td><td colspan="5">Coefficients of partial correlations</td></tr><tr><td>BD</td><td> $OC_r$ </td><td> $ANF_r$ </td><td> $OC_m$ </td><td> $ANF_m$ </td></tr><tr><td>J</td><td>0.833</td><td>-0.515</td><td>-0.329</td><td>0.985</td><td>-0.506</td></tr><tr><td> $\theta_{jl}$ </td><td>0.690</td><td>0.950</td><td>0.600</td><td>0.807</td><td>0.708</td></tr><tr><td> $\sigma_D$ </td><td>0.512</td><td>0.785</td><td>0.329</td><td>0.126</td><td>0.260</td></tr><tr><td> $b_j$ </td><td>0.680</td><td>0.273</td><td>0.491</td><td>0.230</td><td>0.271</td></tr><tr><td> $\alpha_{j}^{OA}$ </td><td>0.430</td><td>0.363</td><td>0.381</td><td>0.672</td><td>0.708</td></tr><tr><td>w</td><td>-0.803</td><td>-0.851</td><td>-0.724</td><td>-0.758</td><td>-0.827</td></tr><tr><td> $\sigma_u$ </td><td>0.814</td><td>0.718</td><td>0.710</td><td>0.675</td><td>0.711</td></tr></table>

From the results in Table 3 and the simulation process, we observe that:

(1) With the increase in $\theta _ { j l } ,$ more intensive horizontal competition among retailers results in the decrease in average retail price and average market demand of retailers. Thus the pro<sup>fi</sup>t and liquidity of retailers and manufacturers are decreased, which further leads to the increase in non-payment of the retailers to the manufacturers (BD) and the increase of the number of the occurrence of <sup>fi</sup>nancial distress (ANF) at the retailers and the manufacturers.

(2) With the increase of $\sigma _ { D } ,$ the overstock and stockout phenomena occur more frequently at the retailers. As a result, operating cost (OC) and the number of the occurrence of <sup>fi</sup>nancial distress (ANF) at the retailers are increased, and these further increase the number of occurrence of bankruptcy at the retailers. Similarly, with the increase of $b _ { j } ,$ higher price elasticity may cause the increase of the <sup>fl</sup>uctuations in market demand and the decrease of the average market demand, which further leads to the decrease of the pro<sup>fi</sup>t and liquidity of retailers and manufacturers. As a result, bad debt (BD) and the number of the occurrence of <sup>fi</sup>nancial distress (ANF) are increased.

(3) With the increase $\mathrm { o f } J ,$ , the average bad debt (BD) caused by one retailer is reduced. That is, the bad debt caused by one retailer's bankruptcy has relatively smaller impact on manufacturers, thus the number of the occurrence of <sup>fi</sup>nancial distress (ANF) at the manufacturers is decreased. As a result, bankruptcy propagation from retailers to manufacturers caused by bad debt can be mitigated, and the number of occurrence of bankruptcy can also be reduced.

(4) With the increase of $\alpha _ { j } ^ { O A }$ , uncertainty of the demand received by each manufacturer in each period would be increased. This would increase of the overstock and stockout phenomena at the manufacturers, which further increase the operating cost (OC) and the number of the occurrence of <sup>fi</sup>nancial distress (ANF) at the manufacturers. As a consequence, the decision made by a retailer may have larger impacts on the manufacturers than on itself.

(5) With the increase of manufacturers' wholesale price w, the average retail price of retailers is increased and the average market demand is decreased. Thus the average order quantity and the borrowing amount of money are both reduced, which further reduces the cash <sup>fl</sup>ow risk of supply chain members and the stockout phenomenon in the supply chain. As a result, the number of the occurrence of <sup>fi</sup>nancial distress (ANF) and the operating cost (OC) are reduced.

(6) With the increase of $\sigma _ { u } ,$ higher production uncertainty of manufacturers increases the stockout phenomenon at the manufacturers, which further increases the cash <sup>fl</sup>ow risk at both the manufacturers and the retailers. As a result, the operating cost (OC) and the number of the occurrence of <sup>fi</sup>nancial distress (ANF) are increased.

## 5.2. Effectiveness of financial decisions

In our model, there are two main factors that are related to <sup>fi</sup>nancial decisions, the maximal risk of cash <sup>fl</sup>ow that member x is willing to take in maximizing its estimated pro<sup>fi</sup>t $( \omega _ { x } )$ , and the upfront payment proportion of retailers (ϕ ). To investigate the linkage between these <sup>fi</sup>nancial decisions and the bankruptcy risks caused by various operational parameters and decisions, we <sup>fi</sup>rst vary the values of parameter $\omega _ { x }$ from 0.00 to 0.40. For each given value of $\dot { } \omega _ { x }$ , we redo the 39 experiments by varying levels of the seven operational parameters listed in Table 2. In each experiment, We set $\phi _ { j } = 0 . 5$

The outputs of the 39 experiments under each level of ω (i.e., $\omega _ { x } = 0 . 0 0 , 0 . 4 0 )$ are <sup>fi</sup>rst examined through linear regression analysis (RS). By comparing the result of RS under $\omega _ { x } = 0 . 0 0$ and that under $\omega _ { x } { = } 0 . 2 0$ , we <sup>fi</sup>nd that, with the decrease of the value of $\dot { } \omega _ { x }$ from 0.20 to 0.00, the impacts of parameters $\theta _ { j l }$ and w on CCC $( \mathrm { L } \mathrm { a g } = + 1 )$ become signi<sup>fi</sup>cant, whereas the impacts of parameters $\sigma _ { D }$ and $\alpha _ { i } ^ { O A }$ on ANR become insigni<sup>fi</sup>cant. Similarly, with the increase of the value of $\omega _ { x }$ from 0.20 to 0.40, the impacts of parameter $\alpha _ { i } ^ { O A }$ on $\mathbf { C C } \left( \mathrm { L a g } = 0 \right)$ parameter J on CCC (Lag=+1) and parameter w on CCC $( \mathrm { L } \mathrm { a g } = - 1 )$ become signi<sup>fi</sup>cant, whereas the impacts of parameter $\sigma _ { u }$ on CCC $( \mathrm { L } \mathsf { a g } = + 1 )$ and parameters $\sigma _ { D }$ and $\alpha _ { j } ^ { \hat { O } A }$ on ANR become insigni<sup>fi</sup>cant. This observation indicates that, the impact of operational parameters and decisions on bankruptcy propagation depend on the <sup>fi</sup>nancial decisions, and bankruptcy risks caused by operational parameters and decisions can be mitigated through <sup>fi</sup>nancial decisions.

To examine the effectiveness of these <sup>fi</sup>nancial decisions in hedging against bankruptcy risks, we <sup>fi</sup>rst compute the increase percentage of the values of the output indexes under ${ \omega } _ { x } = 0 . 0 0$ and $\omega _ { x } { = } 0 . 4 0$ , compared with those under $\omega _ { x } = 0 . 2 0 .$ The increase percentage of each output index (ANR for example) under $\omega _ { x } = 0 . 0 0$ or 0.40 is compute by (ANR under $\omega _ { x } = 0 . 0 0$ or $0 . 4 0 { \mathrm { - } } { \mathrm { A N R } }$ under $\omega _ { x } { = } 0 . 2 0 ) / ( \mathrm { A N R }$ under ${ \omega _ { x } } = 0 . 2 0 )$ 100%. The average increase percentage of the value of each output index under ${ \omega } _ { x } = 0 . 0 0$ and $\omega _ { x } { = } 0 . 4 0$ over the 39 experiments are shown in Table 4.

It can be observed from Table 4 that, when the value of $\omega _ { x }$ decreases from 0.20 to 0.00, three CCC indexes and two AN index (ANM and ANSC) can be increased. With the increase of the value of ω from 0.20 to 0.40, the average values of all CCC indexes and all AN indexes are also increased. This observation is insightful: on one hand, if a <sup>fi</sup>rm ignores the risk of cash <sup>fl</sup>ow (a <sup>fi</sup>nancial risk) in operational decision-making, the resulted operational decisions may lead to poor performance (this observation has been made by Babich and Sobel [5]); on the other hand, if a <sup>fi</sup>rm overemphasizes the risk of cash <sup>fl</sup>ow, the resulted operational decisions may also lead to high risk of bankruptcy.

The impact of parameter $\phi _ { j }$ on bankruptcy risks is investigated by varying the value of $\phi _ { j }$ from 0.20 to 0.80. For each given value of $\mid \phi _ { j } ,$ we also redo the 39 experiments by varying levels of the seven operational parameters listed in Table 2. In each experiment, We set $\omega _ { x } { = } 0 . 2 0$

The outputs of the 39 experiments under each level of $\phi _ { j }$ (i.e., $\phi _ { j } = 0 . 2 0 , 0 . 8 0 )$ are also examined through linear regression analysis (RS). By comparing the result of RS under $\phi _ { j } = 0 . 2 0$ and that under $\phi _ { j } = 0 . 5 0$ , it is found that, with the decrease of the value of $\dot { \phi } _ { j }$ from 0.50 to 0.20, all seven parameters have signi<sup>fi</sup>cant impacts on CCC (Lag=0), the impacts of w on CCC (Lag=−1) and CCC $( \mathrm { L } \mathrm { a g } = + 1 )$ also become signi<sup>fi</sup>cant; whereas the impacts of parameter σ on CCC (Lag=+1), $\theta _ { j l }$ on CCC (Lag=−1) become insigni<sup>fi</sup>cant. With the increase of the value of $\dot { \phi } _ { j }$ from 0.50 to 0.80, only parameters J and $\alpha _ { j } ^ { O A }$ have signi<sup>fi</sup>cant impacts on CCC $( \mathrm { L } \mathsf { a g } = 0 ) ;$ ; whereas all seven parameters have signi<sup>fi</sup>cant impacts on ANR.

To examine the effectiveness of parameter $\phi _ { j }$ in hedging against bankruptcy occurrence and propagation, the average increase percentage of the values of the output indexes under $\phi _ { j } = 0 . 2 0$ and $\phi _ { j } = 0 . 8 0$ , compared with those under $\phi _ { j } = 0 . 5 0 ,$ , are also calculated and are shown in Table 5.

Increase percentage of the values of output indexes under $\omega _ { x } = 0 . 0 0$ and $\omega _ { x } = 0 . 4 0 .$

<table><tr><td rowspan="3"></td><td colspan="4">Percentage of increase on the output indexes (%)</td></tr><tr><td colspan="2"> $\omega_x=0.00$ </td><td colspan="2"> $\omega_x=0.40$ </td></tr><tr><td>Mean</td><td>95% Confidence Interval</td><td>Mean</td><td>95% Confidence Interval</td></tr><tr><td>CCC (Lag = -1)</td><td>-8.04</td><td>[-27.71, 11.63]</td><td>31.64</td><td>[-7.24, 70.52]</td></tr><tr><td>CCC (Lag = 0)</td><td>-8.38</td><td>[-13.68, 6.91]</td><td>34.29</td><td>[17.08, 51.50]</td></tr><tr><td>CCC (Lag = +1)</td><td>-5.01</td><td>[-34.79, 24.78]</td><td>36.09</td><td>[-7.85, 80.04]</td></tr><tr><td>ANR</td><td>-17.19</td><td>[-20.68, -13.70]</td><td>77.37</td><td>[68.53, 86.21]</td></tr><tr><td>ANM</td><td>15.32</td><td>[12.17, 18.47]</td><td>6.66</td><td>[-0.57, 13.90]</td></tr><tr><td>ANSC</td><td>-1.44</td><td>[-4.28, 1.41]</td><td>40.48</td><td>[32.95, 48.00]</td></tr></table>

Table 5  
Increase percentage of the values of output indexes under $\phi _ { j } = 0 . 2 0$ and $\phi _ { j } = 0 . 8 0 .$

<table><tr><td rowspan="3"></td><td colspan="4">Percentage of increase on the output indexes (%)</td></tr><tr><td colspan="2"> $\phi_j=0.20$ </td><td colspan="2"> $\phi_j=0.80$ </td></tr><tr><td>Mean</td><td>95% Confidence Interval</td><td>Mean</td><td>95% Confidence Interval</td></tr><tr><td>CCC (Lag = -1)</td><td>8.16</td><td>[-17.19, 33.52]</td><td>8.72</td><td>[-12.59, 30.03]</td></tr><tr><td>CCC (Lag = 0)</td><td>43.70</td><td>[23.78, 63.61]</td><td>-12.31</td><td>[-23.08, -1.54]</td></tr><tr><td>CCC (Lag = +1)</td><td>1.74</td><td>[-48.29, 51.78]</td><td>-11.07</td><td>[-37.63, 15.48]</td></tr><tr><td>ANR</td><td>11.31</td><td>[1.18, 21.45]</td><td>13.71</td><td>[7.18, 20.24]</td></tr><tr><td>ANM</td><td>43.43</td><td>[31.06, 55.80]</td><td>-24.35</td><td>[-27.23, -21.48]</td></tr><tr><td>ANSC</td><td>27.39</td><td>[17.03, 37.75]</td><td>-5.35</td><td>[-8.98, -1.72]</td></tr></table>

It can be observed from Table 5 that, with the increase of the value of $\phi _ { j }$ from 0.20 to 0.80, the average values of two CCC indexes (CCC $( \mathrm { L } \mathrm { a g } = 0 )$ and $\complement C C ( \mathrm { L a g } = + 1 ) )$ and of two AN indexes (i.e., ANM and ANSC) are decreased, whereas the average value of ANR index is increased. This observation indicates that, manufacturers can reduce the occurrence and propagation of bankruptcy in supply chain by increasing the value of $\phi _ { j }$ (i.e., the up-front payment proportion of retailers). However, this would lead more retailers to go bankrupt. Therefore, vertical interaction among supply chain members, and the effects of various coordination contracts in mitigating the occurrence and propagation of bankruptcy in supply chains are important problems to be further investigated.

## 6. Conclusion

In this paper we have developed a general modeling framework for supply chain networks to explore the impacts of operational interactions among member <sup>fi</sup>rms on occurrence and propagation of bankruptcy. This study makes a signi<sup>fi</sup>cant contribution to the supply chain management and <sup>fi</sup>nancial management literature by identifying the operational causes of bankruptcy propagation in supply chains.

The results of this paper provide several important managerial insights for reducing bankruptcy propagation in supply chain:

1) First, horizontal competition between retailers is an important reason for the collapse of debt chain, which causes bankruptcy propagation from retailers to manufacturers; whereas the increase of the number of retailers could reduce bankruptcy risks in supply chain. These conclusions indicate that, when faced with intensively competitive retailers, the manufacturer may reduce bankruptcy risks by increasing the number of retailers in supply chain.

2) Second, operational decisions made by supply chain members (e.g., wholesale price of manufacturers, order allocation scheme of retailers) are also important causes of bankruptcy propagation in supply chain. This observation, along with the results in 1), imply that, when the retail price and market demand are both decreased as a result of intensive horizontal competition between retailers, the manufacturer can stimulate the increase of retail price and reduce bankruptcy risks by setting a relatively high wholesale price.

3) Third, impact of operational parameters and bankruptcy propagation depend on <sup>fi</sup>nancial decisions, and thus bankruptcy risk caused by operational parameters and decisions can be moderately hedged through <sup>fi</sup>nancial decisions. In addition, impact of <sup>fi</sup>nancial parameter $\phi _ { j }$ (the up-front payment proportion of retailers) on output indexes also indicates that, the research methodology and the simulation model developed in this paper lay a solid base for the further research of mitigating bankruptcy propagation through vertical interaction and coordination among supply chain members.

This paper investigates operational causes of bankruptcy propagation in supply chain networks with a relatively simple relationship between manufacturers and retailers. That is, we assume exogenous wholesale price and no explicit competition between manufacturers. If there exists explicit horizontal competition among manufacturers (for example, wholesale price competition), the conclusions in this paper need to be re-speculated. In addition, different supply chain scenarios characterized by different supply chain parameters (e.g., different replenishment lead times) and various kinds of coordination mechanisms (e.g., vertical information sharing and vendor managed inventory), also deserve further investigation.

## Acknowledgments

The authors would like to thank the anonymous referees and the editors for their insightful comments and suggestions, which signi<sup>fi</sup>cantly improved the paper. This research was supported by NSFC under Grants Nos. 70725001, 70821001, 70772025 and NSFC major program (Grant No. 71090401/71090400).

## References

[1] F. Allen, E. Carletti, Credit risk transfer and contagion, Journal of Monetary Economics 53 (2006) 89–111.

[2] F. Allen, D. Gale, Financial contagion, Journal of Political Economy 108 (1) (2000) 1–33.

[3] G. Andrade, S. Kaplan, How costly is <sup>fi</sup>nancial (not economic) distress? Evidence from highly leveraged transactions that became distressed, Journal of Finance 53 (1998) 1443–1493.

[4] V. Babich, A.N. Burnetas, P.H. Ritchken, Competition and diversi<sup>fi</sup>cation effects in supply chains with supplier default risk, Manufacturing & Service Operations Management 9 (2) (2007) 123–146.

[5] V. Babich, M. Sobel, Pre-IPO operational and <sup>fi</sup>nancial decisions, Management Science 50 (7) (2004) 935–948.

[6] S. Battiston, D.D. Gatti, M. Gallegati, B. Greenwald, J.E. Stiglitz, Credit chains and bankruptcy propagation in production networks, Journal of Economic Dynamics & Control 31 (2007) 2061–2084.

[7] S. Benjaafar, E. Elahi, K. Donohue, Outsourcing via service quality competition, Management Science 53 (2007) 241–259.

[8] F. Bernstein, A. Federgruen, Decentralized supply chains with competing retailers under demand uncertainty, Management Science 51 (1) (2005) 18–29

[9] F. Bernstein, A. Federgruen, Pricing and replenishment strategies in a distribution system with competing retailers, Operations Research 51 (3) (2003) 409–426

[10] F. Boissay, Credit Chains and the Propagation of Financial Distress, vol. 573, European Central Bank, January 2006.

[11] D.B. Bradley, M. J. Rubach, Trade credit and small businesses: a cause of business failures? mimeo, University of Central Arkansas, 2002.

[12] M. Dada, N.C. Petruzzi, L.B. Schwarz, A newsvendor's procurement problem when suppliers are unreliable, Manufacturing & Service Operations Management 9 (2007) 9–32.

[13] C. Daryl, G. Shãna, Channels of <sup>fi</sup>nancial market contagion, Applied Economics 36 (21) (2004) 2461–2469.

[14] K.T. Fang, C.X. Ma, Orthogonal and Uniform Experimental Design (in Chinese), Science Press. China, 2001.

[15] Y. Fujiwara, Chain of <sup>fi</sup>rms' bankruptcy: a macroscopic study of link effect in a production network, Advances in Complex System 11 (5) (2008) 703–717.

[16] D.D. Gatti, M. Gallegati, B. Greenwald, A. Russo, J.E. Stiglitz, Business <sup>fl</sup>uctuations in a credit-network economy, Physica A 370 (2006) 68–74.

[17] D.D. Gatti, M. Gallegati, B.C. Greenwald, A. Russo, G.E. Stiglitz, Financially Constrained Fluctuations in an Evolving Network Economy, vol. W14112, National Bureau of Economic Research, 2008.

[18] D.D. Gatti, C.D. Guilmi, E. Gaffeo, G. Giulioni, M. Gallegati, A. Palestrini, A new approach to business <sup>fl</sup>uctuations: heterogeneous interacting agents, scaling laws and <sup>fi</sup>nancial fragility, Journal of Economic Behavior and Organization 56 (4) (2005) 489–512.

[19] T.V. Gestel, B. Baesens, J.A.K. Suykens, D.V. Poel, D.E. Baestaens, M. Willekens, Bayesian kernel based classi<sup>fi</sup>cation for <sup>fi</sup>nancial distress detection, European Journal of Operational Research 172 (2006) 979–1003

[20] S. Gottlich, M. Herty, C. Ringhofer, Optimization of order policies in supply networks, European Journal of Operational Research 202 (2010) 456–465.

[21] C.V. Helliar, A.A. Lonie, D.M. Power, C.D. Sinclair, Managerial attitudes to risk: a comparison of Scottish chartered accountants and U.K. managers, Journal of International Accounting, Auditing & Taxation 11 (2002) 165–190.

[22] M.G. Hertzel, Z. Li, M.S. Of<sup>fi</sup>cer, K.J. Rodgers, Inter-<sup>fi</sup>rm linkages and the wealth effects of <sup>fi</sup>nancial distress along the supply chain, Journal of Financial Economics 87 (2008) 374–387.

[23] N. Kiyotaki, J. Moore, Balance-Sheet contagion, The American Economic Review 92 (2) (2002) 46–50.

[24] H.L. Lee, C. Billington, Material management in decentralized supply chains, Operations Research 41 (5) (1993) 835–847.

[25] Y.W. Leung, Y.P. Wang, Multi-objective programming using uniform design and genetic algorithm, IEEE Transactions on Systems, Man, and Cybernetics, Part C 30 (3) (2000) 293–304.

[26] L. Li, H. Zhang, Con<sup>fi</sup>dentiality and information sharing in supply chain coordination, Management Science 54 (8) (2008) 1467–1481.

[27] W.Y. Liang, C.C. Huang, Agent-based demand forecast in multi-echelon supply chain, Decision Support Systems 42 (2006) 390–407.

[28] F.R. Lin, H.C. Kuo, S.M. Lin, The enhancement of solving the distributed constraint satisfaction problem for cooperative supply chains using multi-agent systems Decision Support Systems 45 (2008) 795–810.

[29] F.R. Lin, Y.H. Pai, Using multi-agent simulation and learning to design new business process, IEEE Transactions on Systems, Man, and Cybernetics, Part A 30 (3) (2000) 380–384.

[30] S. Nahmias, Production and Operations Analysis, <sup>fi</sup>fth edition, Irwin/McGraw-Hill Homewood, IL, 2005.

[31] H.V.D. Parunak, R. Savit, R.L. Riolo, Agent-based modeling vs. equation-based modeling: a case study and users' guide, Conference Proceedings, Multi-agent Systems and Agent Based Simulation, First International Workshop, vol. 1534, 1998, pp. 10–25.

[32] A. Purnanandam, Financial distress and corporate risk management: theory and evidence, Journal of Financial Economics 87 (2008) 706–739.

[33] S. Rassenti, S.S. Reynolds, V.L. Smith, F. Szidarovszky, Adaptation and convergence of behavior in repeated experimental Cournot games, Journal of Economic Behavior & Organization 41 (2000) 117–146.

[34] C.V. Rijckeghem, B. Weder, Sources of contagion: is it <sup>fi</sup>nance or trade? Journal of International Economics 54 (2001) 293–308

[35] SCC, SAP Supply Chain Performance Management, http://www.supply-chain.org 2010.

![](/api/attachments/43RGFYTA/fulltext/images/948f7c117a62162da6961bacae6cba972563bb6273f75e5c37151a4d7599d1df.jpg)

[36] The Uniform Design, http://www.math.hkbu.edu.hk/UniformDesign/ 2010.

![](/api/attachments/43RGFYTA/fulltext/images/743dffe05606e5efb44e8f99fb5b84b654e8c09d85cf958abd2cfb5d586fdb55.jpg)

[37] C.Y. Tsai, On supply chain cash <sup>fl</sup>ow risks, Decision Support Systems 44 (2008) 1031–1042.

[38] A. Valluri, D.C. Croson, Agent learning in supplier selection models, Decision Support Systems 39 (2005) 219–240.

[39] X.Y. Xu, Y.H. Sun, Z.S. Hua, Reducing the probability of bankruptcy through supply chain coordination, IEEE Transactions on Systems, Man, and Cybernetics-Part C: Applications and Reviews 40 (2) (2010) 201–215.

![](/api/attachments/43RGFYTA/fulltext/images/2f2197c1df0ba7e4cd3e5de83a9dc6a1dd9c746e7408c31ce4ade7084528667b.jpg)  
Dr. Zhongsheng Hua received the Ph.D. degree in Computer Science from the University of Science and Technology of China (USTC) in 2000. He currently is a professor and associate dean of School of Management, USTC. His research interests include decision analysis, production and operations management, and supply chain management. He has published academic papers in many journals, such as IEEE Transactions on Systems, Man, and Cybernetics, European Journal of Operational Research, Omega Journal of the Operational Research Society, Expert Systems with Applications, Computers & Operations Research, Information Science, International Journal of Production Research, and International Journal of Production Economics. He has also published three books.

Dr. Yanhong Sun received her bachelor degree from the Department of Information Management, Xi'an University of Technology, China, 2006. She received her Ph.D. degree in Management Science from the University of Science and Technology of China (USTC) in 2010. She currently works in the Department of Management Science, School of Management, USTC. Her research interests are in multiagent systems and supply chain management. She has published academic papers in several journals, including IEEE Transactions on System, Man, and Cybernetics.

Dr. Xiaoyan Xu received the Ph.D. degree in Management Science from the University of Science and Technology of China (USTC) in 2006. She currently is a professor of School of Management, USTC. Her research interests include multi-agent systems, supply chain management and <sup>fi</sup>nance management. She has published academic paper in many journals, such as IEEE Transactions on Systems, Man, and Cybernetics, International Journal of Production Economics, Expert systems with applications.
