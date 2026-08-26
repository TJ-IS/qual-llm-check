---
otero_id: 6394
otero_key: "2HSHG4V3"
title: "A strategic analysis of inter organizational information sharing"
authors: "Jingquan Li; Riyaz Sikora; Michael J. Shaw; Gek Woo Tan"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.12.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A strategic analysis of inter organizational information sharing

Jingquan Li<sup>a</sup>, Riyaz Sikora<sup>b,\*</sup>, Michael J. Shaw<sup>a</sup>, Gek Woo Tan<sup>c</sup>

<sup>a</sup>University of Illinois at Urbana-Champaign, United States

<sup>b</sup>University of Texas at Arlington, Department of Information Systems and OM, P.O. Box 19437, Arlington, TX 76019 , United States <sup>c</sup>National University of Singapore, Singapore

Available online 25 January 2005

## Abstract

In this paper we study the effect of inter organizational information sharing strategies on firm level performance under both stable as well as volatile market conditions. We use information exchange in a supply chain as a representation of inter organizational information sharing, and study five strategies for information sharing that range from minimal to near-complete information exchange. We present analytical evaluation of the relative performance of these strategies and experimental results from a proof-of-concept system. Our results show that near-complete information sharing that combines more than one type of information being shared has better performance in volatile market conditions. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Information sharing; Supply chain management; E-commerce; Electronic markets

## 1. Introduction

Corporate strategy is increasingly focused on the efficient exchange of information between business partners. It is widely known that Wal-Mart and Proctor & Gamble (P&G) share information regarding the retail sales of P&G products at Wal-Mart stores. This information enables P&G to do a better job of managing its production of these products and provides Wal-Mart with greater <sup>b</sup>in store<sup>Q</sup> availabilities. Furthermore, companies such as Dell and Whirlpool are sharing information with suppliers and customers to decrease costs and improve customer service. The flow of information through their supply chains enables them to match supply closely to consumer demand and to anticipate changes in the marketplace. In fact, the justification for the growth of inter organizational information systems (IOISs, e.g., electronic data interchange (EDI), enterprise resource planning (ERP), supply-chain applications, and emarketplaces) is based on the growing awareness that leveraging information can be beneficial to all parties involved.

The study of inter organizational information sharing has been a growing interdisciplinary research area actively studied in both information systems research and operations research. The information systems researchers focus mainly on the electronic flow of information. The research on the potential benefits of EDI is voluminous ([3,10,23,29,30] and others). [23] analyzed the benefits of improved information exchanges between Chrysler and its suppliers that result from using EDI. [15] analyzed a number of information technology initiatives in the Dutch flower markets and found that information technology-enabled process innovations change the information available to different stakeholders. Based on a case study of the development of the inter organizational information systems in the aircraft parts industry, [9] found that two sets of transaction characteristics–demand uncertainty and market uncertainty–influence the choice of IOISs. [27] treated the level of information sharing not based on its exact content, but rather, based on the impact it has on the parties that contract to share the information. [25] provided an integrated perspective of supply chain management and inter organizational systems and showed that all organizations in the supply chain could gain from sharing information by the reduction of supply and demand uncertainties.

In contrast, the operations and logistics researchers focus mainly on movement of materials and inventory cost savings. [17,18] found that sharing real demand information across the supply chain members reduces the bullwhip effect. [6] studied the relative benefits of echelon-stock policies over those of installation stock policies in a multi-echelon environment. [7,8] quantified the bullwhip effect for multiple-stage supply chains with and without centralized demand information and demonstrated that centralizing demand information can significantly reduce but not completely eliminate the bullwhip effect. [12] analyzed information flow between a supplier and a retailer in a two-echelon model of capacitated supply chain. [19] studied how to use shared information to improve the supplier’s order quantity decisions with a known autoregressive demand process. [26] suggested that the supplier can reduce its uncertainty further by using the entire retailer order history. [5] investigated a supply chain model with one supplier, and N retailers, stochastic consumer demand, and batch ordering. They showed analytically how the manufacturer can benefit from using information about the retailer’s inventory levels when the retailers use a batch ordering policy. [22] considered a similar setting with one supplier and N identical retailers, but focused on the impact of using information by the supplier to improve its replenishment/ordering decisions. They showed how the supplier can benefit from using information about the retailer’s inventory levels.

Despite the increasing number of cases on inter organizational coordination and information sharing, there has not been a representational framework of inter organizational information sharing. Building on the transaction costs, inventory theory, and information systems literatures, we analyze the relationship between coordination structures and information sharing and propose a strategic analysis framework of inter organizational information sharing based on two dimensions: levels of information sharing (transactional, operational, and strategic) and coordination structures (electronic hierarchies, electronic markets). We use a supply chain as a representative case for investigating the behaviors of different forms of information sharing and how the strategic choices of information sharing depend on demand patterns and the supply chain structure. We present the results of an extensive simulation study to further validate the findings from our strategic analysis framework.

The rest of the paper is organized as follows. Section 2 describes the two basic coordination structures: electronic hierarchies and electronic markets. Section 3 provides a classification of inter organizational information sharing. Section 4 describes the information sharing models and the impact of demand patterns on the strategies. Section 5 presents the results of a simulation study. Section 6 concludes and identifies opportunities for future research.

## 2. Inter organizational coordination structures

The flow of goods and services across organizations can be coordinated through markets or hierarchies. Since information and communication technologies (ICTs) are facilitating inter organizational coordination and thus making both markets and hierarchies more efficient, reference to electronic hierarchies and electronic markets can be made [1,20,21].

In an electronic hierarchy, the organizations involved have a long-term contact and align their internal processes with one another. An example is series of legally separated firms along a supply chain that are electronically connected to the neighboring nodes. The primary reason for establishing an electronic hierarchy is to improve the efficient exchange and sharing of information between firms.

An electronic market is designed to match buyers and sellers who generally do not share a long-term relationship. Markets can be centralized or decentralized. Centralized markets use one or more intermediaries such as distributors or brokers. Buyers and sellers need only connect to one or more of these intermediaries to carry out a transaction; a stock exchange is a good example. In a decentralized market, all the participants can contact one another directly, and no intermediaries are present. An example of a decentralized market would be one that uses intelligent agents to carry out transactions.

Despite the challenge of categorizing the relationships between organizations as markets, hierarchies, or a hybrid of both, each of these two types of coordination structures between buyers and sellers has distinct characteristics with regard to its cost structure. Transaction cost theory divides the costs of acquiring physical goods and associated services into produc tion and transaction costs [11,31,32].

In hierarchies, the production costs are higher because of the lack of economies of scale, and the transaction costs are lower because of limited coordination and less risk. Previous studies on the effects of IOISs on the performance of organizations typically applied transaction costs and agency theory to predict shifts from hierarchies toward markets [2,14,21]. A central argument of these articles was that IOISs would improve communications, searches, matching, negotiating, monitoring, and contracts to reduce transaction costs. This would allow buyers to take advantage of production economics available in markets and allow sellers to reach a wider variety of buyers. A critical drawback of this analysis was that it focused on the <sup>b</sup>classical<sup>Q</sup> benefits of inter organizational systems: efficient transaction processing and better monitoring and information processing capacity. However, after a few years of trial-and-error in electronic commerce, many firms now realize that the real gains from IOISs come not only from efficient trading but also from better access to and the sharing of critical business information.

A significant problem in markets is the information asymmetry between the market participants [13]. The sellers do not have perfect information on the demand. Similarly, the buyers do not have perfect information on the supply. This information asymmetry leads to uncertainties and market inefficiency. The basic strategy to deal with the uncertainties is to improve communication and the information available. Therefore, the role of IOISs is not only to improve the trading efficiency in order to reduce the transaction costs but also to facilitate inter organizational information sharing that creates further transaction-processing efficiencies and/or delivers a higher level of service.

## 3. Information sharing in a supply chain

An important characteristic of any buyer–supplier relationship is the amount and type of information that is exchanged between the trading partners. Supply chain networks are characterized by greater information exchange than arm’s length transactions. Innovative supply chain networks are examining the value of information sharing not only for opportunities to reduce transaction costs but also for opportunities to reduce inventory costs and serve their customers better.

However, a critical issue is how much information can be shared between business partners. Although IOISs provide the ability to share information easily, firms may not share information for various reasons. Information sharing brings concerns of security, privacy, and intellectual property. In addition, significant investments are required to allow information to be shared across entities so that the benefits realized from obtaining or sharing information must be greater than the costs involved.

## 3.1. A classification of information sharing

Building on the categorization of inter organizational linkages [4], we develop a systematic classification of information sharing strategies (Fig. 1) based on two dimensions of levels of information sharing (transactional, operational, and strategic) and areas where these information sharing are conducted (elec tronic hierarchies or electronic markets). We identify three different levels of information sharing between organizations: (1) exchanging transactional information (order quantities, prices, sales, product specifications, quality, and delivery specifications etc.), where information technology automates routine transactions between specific buyers and sellers; (2) sharing operational information (inventory levels, costs and schedules, production and transportation capacities, lead times, and shipments etc.), where operational data is shared only by two adjacent players, buyer and seller, at each stage of the supply chain; (3) sharing strategic information (point-of-sale information, realtime demand, understanding of market trends, the things customers value most, and product designs etc.), where one organization possesses the proprietary information, while all the participants can use this information to generate strategic benefits. On the other dimension, the information sharing may be undertaken in either electronic hierarchies or electronic markets.

<table><tr><td colspan="4">Location</td></tr><tr><td rowspan="2">Electronic markets</td><td>Electronic catalogues</td><td>Collaborative marketplaces</td><td>Perfect marketplaces</td></tr><tr><td>Cell 2</td><td>Cell 4</td><td>Cell 6</td></tr><tr><td rowspan="3">Electronic hierarchies</td><td>Electronic beer Games</td><td>Business partnerships</td><td>Virtual enterprises</td></tr><tr><td>Cell 1</td><td>Cell 3</td><td>Cell 5</td></tr><tr><td>Transactional information</td><td>Operational information</td><td>Strategic information</td></tr></table>

Fig. 1. Classification of inter organizational information sharing systems.

These categories constitute a wide range of levels of information sharing in both hierarchies and markets. The sharing of transactional information can be thought of as a minimal information sharing case because transactional information is public information that can be observed or acquired via search. The sharing of strategic information can be considered as a near-complete information sharing case because this involves very sensitive information that is shared among all participants. The sharing of operational information, where a firm only looks at the neighboring partners, is a partial information sharing case.

## 3.2. Information sharing in a supply chain

In this section, we analyze information sharing in the context of a supply chain. A supply chain can be a representative case for any buyer–supplier relationship, either an electronic hierarchy or an electronic market.

In the traditional buyer–supplier relationship, firms communicate demand information exclusively in the form of orders. Since orders are the result of <sup>b</sup>processed<sup>Q</sup> information by the retailers, order information often distorts the real consumption of the marketplace. One example is the so-called bullwhip effect, where slight variations in demand at the consumer end results in wild swings at the supplier end [17]. This study shows that enhancing the value of information sharing across organizations can greatly reduce the uncertainty related to the distortion of information and product variety.

We study the effects of sharing of transactional, operational, and strategic information on supply chain performance by using transaction-processing efficiency (inventory costs and fill rate) as performance metrics. Fig. 2 shows the flow of information in a typical serial supply chain. We model the transactional information sharing strategy by sharing of order information between the adjacent stages of the supply chain (Model 0). We model the strategic information sharing strategy by sharing of timely demand information across the chain (Model 1). We give two examples of the operational information sharing strategy: sharing of inventory data (Model 2) and shipment data (Model 3) between the adjacent stages of the supply chain.

![](/api/attachments/2HSHG4V3/fulltext/images/ef9a4289a4dcb0ac3d06801239012ccc9d7da747e4c6d8ee8581650eaeea97e2.jpg)  
Fig. 2. Information sharing.

## 4. Models

In this section, we first discuss our model formulation and performance metrics. We then analyze the four basic models in the context of a supply chain of a single product. We further consider a supply chain of customizable products and investigate a hybrid model.

Consider a linear supply chain with N stages. For a given stage k, stage k-1 is its customer and stage k+1 is its supplier. The end customer in the supply chain is called the consumer. The end demands, which are independent and identically distributed (i.i.d.) from a normal distribution, arise at stage 1, stage 1 orders from stage 2, etc., and stage N orders from an outside supplier. This triggers material flows in the opposite direction. Each stage has a fixed lead time and makes its own decisions based on available information. We assume that each stage maintains a high service level so that each of the N stages can control its inventory <sup>b</sup>locally<sup>Q</sup>. Such an assumption is reasonable when the service level at each stage is very high. We feel that a high service level at each stage is a reasonable assumption as firms, driven by competition, strive to maintain a high level of customer service.

We model the inventory system at each stage as a periodic review, order-up-to system with a fixed review time of one period. Within each period, for a given stage k, the following sequence of events occur: (1) demand is forecasted, the inventory decision is made with a target inventory level, and an order is placed to its supplier; (2) demand is realized and outbound shipments are released; (3) inbound shipments are received and inventory cost and fill rate are assessed. We assume that each stage uses the typical moving average forecasting method. When the demand in a period exceeds the on-hand inventory, the excess is backordered. The objective is to find out how information sharing affects the performance of the supply chain.

We make use of two subscripts and one superscript in the model. The first subscript refers to the echelon, the second to the time epoch, and the superscript to the model number. Thus $X _ { k t } ^ { 1 }$ will be the value of variable X at stage k in period t in Model 1. For stationary parameters, we omit the time period. For each stage and period, define: L=lead time plus 1 (review period), h=unit holding cost rate, D=real consumer demand with a mean of $\dot { \mathbf { \Omega } } _ { \mu }$ and a variance of $\sigma ^ { 2 } ,$ , S=the estimated target inventory level, Q=the quantity of stock ordered, lˆ =forecast demand, rˆ =standard deviation of errors of forecasts.

With the above assumptions, the demands seen by each upstream stage are normally distributed. For simplicity, we shall restrict our attention to the case in which the service levels for different stages are the same. But the same approach can be easily adapted to the case in which the service levels are different for different stages. Let $\mu _ { k }$ and $\sigma _ { k } ,$ respectively, be the mean and standard deviation of the demand faced by stage k. Safety stocks can be based on either service considerations or a common time supply. Based on service considerations, the expected safety stock at stage k is equal to $z \sqrt { L _ { k } } \sigma _ { k }$ , where z is the safety-stock factor associated with the customer service level [24]; based on the use of a common time supply, the expected safety stock at stage k, can be expressed in units of the expected demand. Many companies use the latter. For a given stage k, we define ${ \mathrm { S S } } _ { k }$ as the expected common factor that satisfies:

$$
z \sqrt {L _ {k}} \sigma_ {k} = \mathrm{SS} _ {k} \mu_ {k}.\tag{1}
$$

A periodic inventory policy requires each stage of the supply chain to raise its inventory level up to a given target level in each period. One common form of this policy is to set the approximately optimal target inventory level at stage k in period $t , S _ { k t } ,$ as given by [16]:

$$
S _ {k t} = L _ {k} \hat {\mu} _ {k t} + z \sqrt {L _ {k}} \hat {\sigma} _ {k t},\tag{2}
$$

where $L _ { k }$ is the lead time plus 1, $\hat { \mu } _ { k t }$ is an estimate of $\mu _ { k }$ and $\hat { \sigma } _ { k t }$ is an estimate of $\sigma _ { k }$ .

Using a common time supply to plan the safety stock, this paper, however, uses a simplified order-upto policy where the target inventory level is of the form:

$$
S _ {k t} = (L _ {k} + \mathrm{SS} _ {k}) \hat {\mu} _ {k t},\tag{3}
$$

where ${ \mathrm { S S } } _ { k }$ is the common safety factor defined by Eq. (1).

Note that Eq. (2) is similar to Eq. (3) with the safety stock $z { \sqrt { L _ { k } } } { \hat { \sigma } } _ { k t }$ replaced by $\mathrm { S S } _ { k } \hat { \mu } _ { k t } .$ , that is, the safety stock is expressed in units of the forecasted average demand rather than the forecasted standard deviation of the forecast errors over the lead time.

We use the following performance measurements to evaluate the information sharing models:

Inventory cost. Inventory is the key driver to the supply chain cost. Let $\mu _ { k }$ and $\sigma _ { k } ,$ be the mean and standard deviation, respectively, of the demand faced by stage k. The average inventory level per period is the sum of safety and average cycle stock, and is given by $z \sqrt { L _ { k } } \sigma _ { k } + \mu _ { k } / 2$ . The average on-order inventory is $L _ { k } \mu _ { k }$ . Since we assume complete backordering, and hence no demand is lost in the system, so $\mu _ { k }$ is equal to $\mu .$ For simplicity, we shall assume that the inventories are valued as the same as the output of each stage. The approximation formula for the total supply chain inventory cost per period is given by

$$
\sum_ {k = 1} ^ {N} h _ {k} \left(L _ {k} \mu + \mu / 2 + z \sigma_ {k} \sqrt {L _ {k}}\right).\tag{4}
$$

Fill rate. The fill rate measures the proportion of demands that are met from the inventory on hand. We use the average fill rate across all stages as an important indicator of service level. This is reasonable especially when management is concerned about stockout at each stage. The long-run relationship between the safety-stock factor and fill rate is $\beta _ { k } = 1 - \sqrt { L _ { k } } \sigma _ { k } G _ { u } ( z ) / \mu$ , where $G _ { u } ( z )$ is the standardized loss function [28]. The approximation expression for the average fill rate over all stages can be expressed as

$$
\frac {1}{N} \sum_ {k = 1} ^ {N} \left(1 - G _ {u} (z) \sigma_ {k} \sqrt {L _ {k}} / \mu\right).\tag{5}
$$

Note that Eqs. (4) and (5) are approximations. As shown in Eqs. (4) and (5), for a fixed service level, lower order variance allows each stage to carry less safety stock on average and thus reduces the total inventory cost; for a fixed service level, lower order variance increases the overall fill rate. Hence the performance of the supply chain squarely relies on demand uncertainty seen by each stage. Inventories are often used to protect the supply chain from uncertainties, but it is an expensive solution. In the following subsections, we will demonstrate how information sharing can reduce order uncertainty at each stage of the supply chain and hence improve the performance of the supply chain.

## 4.1. Transactional information (order data): Model 0

In Model 0, every stage of the supply chain only knows the orders from its adjacent downstream stage and demand forecasts that are based only on local <sup>d</sup>demand<sup>T</sup> information, i.e., the orders from its immediate downstream stage (Fig. 2). We assume that each stage uses the simple moving average forecast method with n observations to estimate the mean of demand, i.e.,

$$
\hat {\mu} _ {1 t} = \sum_ {i = 1} ^ {n} D _ {t - i} / n,\tag{6}
$$

and

$$
\hat {\mu} _ {k t} = \sum_ {i = 1} ^ {n} Q _ {k - 1, t - i} / n, \quad k = 2, \dots , N,
$$

where $\mathcal { Q } _ { k - 1 , t - i }$ is the order placed by stage $k { - } 1$ in period $t { - } i .$

Suppose that each stage, k, follows a period review policy where the target inventory level is given by Eq. (3) and the safety stock, $\mathrm { S } { \mathrm { S } } _ { k } ,$ is chosen to buffer against the order variability from stage $k { - } 1$ At stage k, we can determine the variance of $Q _ { k t }$ relative to the variance of its demand, $\mathcal Q _ { k - 1 , t } .$ . So we write $\mathcal { Q } _ { k t }$ as

$$
Q _ {k t} = S _ {k t} - \left(S _ {k, t - 1} - Q _ {k - 1, t - 1}\right).
$$

Note that $Q _ { k t }$ may be negative, in which case we assume that the excess inventory is returned without cost. Using Eqs. (3) and (6), we can write the order quantity $\mathcal { Q } _ { k t }$ as

$$
\begin{array}{l} Q _ {k t} = (L _ {k} + \mathrm{SS} _ {k}) \hat {\mu} _ {k t} - (L _ {k} + \mathrm{SS} _ {k}) \hat {\mu} _ {k, t - 1} + Q _ {k - 1, t - 1} \\ = (1 + (L _ {k} + \mathrm{SS} _ {k}) / n) Q _ {k - 1, t - 1} \\ \quad - ((L _ {k} + \mathrm{SS} _ {k}) / n) Q _ {k - 1, t - n - 1}. \end{array}
$$

The demands seen by stage k are assumed to be independent across periods. Taking the variance of $\mathcal { Q } _ { k t } ,$ , we get

$$
\begin{array}{l} \operatorname{Var} (Q _ {k}) = \left[ 1 + 2 (L _ {k} + \mathrm{SS} _ {k}) / n + 2 (L _ {k} + \mathrm{SS} _ {k}) ^ {2} / n ^ {2} \right] \\ \times \operatorname{Var} (Q _ {k - 1}). \end{array} \tag {7}
$$

Hence we can deductively derive the following expression for the variance of the orders placed by stage k for Model $0 , \ Q _ { k } ^ { 0 }$ , relative to the variance of real demand

$$
\begin{array}{r l} \operatorname{Var} \left(Q _ {k} ^ {0}\right) & = \left\{\prod_ {j = 1} ^ {k} \left[ 1 + 2 \left(L _ {j} + \mathrm{SS} _ {j}\right) / n + 2 \left(L _ {j} + \mathrm{SS} _ {j}\right) ^ {2} \right. \right. \\ & \quad \left. / n ^ {2} \right] \Bigg \} \operatorname{Var} (D), \quad k = 1, \dots , N. \end{array} \tag {8}
$$

The increase in demand variability is an increasing function of $L _ { k } ,$ , the lead times, and ${ \mathrm { S S } } _ { k } ,$ , the safety stocks, and a decreasing function of $n ,$ the number of observations used in demand forecasting. More importantly, the variance increases multiplicatively at each stage of the supply chain. Empirical evidence also shows that the orders placed by a retailer tend to be more variable than the end demand seen by that retailer [18]. This conclusion does not depend on a specific forecasting technique.

According to Eqs. (4) and (5), the increased demand variability requires each stage to increase its safety stock in order to maintain a given service level and consequently increases the total inventory cost. It also decreases the fill rates at the upstream stages and thus decreases the overall fill rate of the supply chain. We use Model 0 as a base case to examine other models.

## 4.2. Strategic information (demand data): Model 1

Model 1 assumes that the first stage (i.e., the retailer) shares its sensitive demand information with each of the upstream stages (Fig. 3). Since each stage has real demand information, each stage will use the same estimate of the mean demand, i.e.,

$$
\hat {\mu} _ {t} = \left(\sum_ {i = 1} ^ {n} D _ {t - i}\right) / n,\tag{9}
$$

When demand information is shared among stages, an echelon inventory policy is used. For a given stage $k ,$ the lead time is the echelon lead time, i.e., the accumulation of the local lead time and all the downstream lead times; the echelon inventory is the inventory position of the subsystem consisting of stage k itself and all its downstream stages. Consider an echelon inventory policy where the target inventory level is given by

$$
S _ {k t} = \left(\sum_ {i = 1} ^ {k} \left(L _ {i} + \mathrm{SS} _ {i}\right)\right) \hat {\mu} _ {t}, \quad k = 1, \dots , N,\tag{10}
$$

where the safety stock, ${ \mathrm { S S } } _ { i } ,$ is chosen to buffer against the end demand uncertainty.

According to Eqs. (7), (9), and (10), we have the following expression for the variance of the orders placed by stage $k , \mathcal { Q } _ { k } ^ { 1 }$ , relative to the variance of the end demand.

$$
\begin{array}{l} \operatorname{Var} \left(Q _ {k} ^ {1}\right) = \left[ 1 + 2 \sum_ {j = 1} ^ {k} \left(L _ {j} + \mathrm{SS} _ {j}\right) \right. \\ \left. / n + 2 \left(\sum_ {j = 1} ^ {k} \left(L _ {j} + \mathrm{SS} _ {j}\right)\right) ^ {2} / n ^ {2} \right] \operatorname{Var} (D), \\ k = 1, \dots , N. \end{array} \tag {11}
$$

In comparison with Eqs. (8) and (11) demonstrates that the increase in demand variability at each stage of the supply chain is additive instead of multiplicative. Hence the demand information sharing model minimizes both the bullwhip effect and the safety stock.

## 4.3. Operational information (inventory data): Model 2

In Model 2, each stage shares its inventory information with its adjacent upstream stage (Fig. 4). Suppose stage k-1 shares its actual demand and inventory status with stage k period by period. For any period $t ,$ the following are defined for stage k-1 after an order is placed and demand occurs: on-hand inventory $I _ { k - 1 , t } ;$ backorders, $B _ { k - 1 , t } ;$ on-order inventory, $\begin{array} { r l } {  { \operatorname { O I } _ { k - 1 , t } ; } } & { { } } \end{array}$ inventory position, $\mathrm { I P } _ { k - 1 , t } = I _ { k - 1 , t } - B _ { k - 1 , t } + \mathrm { O I } _ { k - 1 , t } ;$ and target inventory level, $S _ { k - 1 , t } .$ By knowing this information, stage k can derive the orders to stage k-1,

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Step 1: Shipping
Entity agent $E_j^i$ with ID j at tier i:
for each output product y,
    for each customer $E^{i-1_k}$
    ship quantity to $E^{i-1_k}$'s input product y.
    reduce current inventory level of y.

Source agent:
for each output product x,
    ship order to $E^n_k$ where n = most upstream tier

Step 2: Bookkeeping
Entity agent $E_j^i$:
for each input product x (if any)
    forward enterprise's in-transit shipment of x
    reduce backlog of x and increase current inventory of x accordingly
    reset information sharing parameters
for each output product y
    compute total backlog (accumulated from all customers)
    forward 10-period demand array
    convert information sharing parameters from output to input product.
    update latest 10-period demand array based on information sharing policy
    calculate stock level for y, using (2), (6), (9), or (12) from section 4.

Step 3.1 Generate order
Customer agent:
for each product y
    generate demand to each upstream customer $E_j^i$.

Step 3.2 Calculate production quantity and place order
Entity agent $E_j^i$:
for each output product y:
    receive order from downstream customer $E^{i-1_k}$
    convert the customer order to its corresponding input component's order
    compute inventory position of y
    based on stock level, compute production quantity of y
    if tier i ≠3, place order with $E^{i+1_m}$ where $E^{i+1_m}$ is the upstream supplier of
    else
    convert production quantity of y into input component x
    for each output product y:
    compute corresponding required quantity for input component x
    for each input product x
    compute fillrate of x
    for each output product y
    find the minimum fillrate among its input components
    quantity of y manufactured, Q = fillrate*production quantity of y
    increase current inventory of y by Q
    decrease inv. of x by Q*units required to make a unit of y
compute quantity of input product x to place with upstream supplier
for each input product x
    compute stock level for x
    compute inventory position of x
    based on stock level of x, compute production quantity of x
    place order with $E^{i+1_m}$ where $E^{i+1_m}$ is the upstream supplier of $E_j^i$
</div>

Fig. 3. Simulation algorithm.

$Q _ { k - 2 , t - 1 } = S _ { k - 1 , t - 1 } - I P _ { k - 1 , t } ,$ , and the orders placed by stage k-1, $Q _ { k - 1 , t } = S _ { k - 1 , t } - \mathrm { I P } _ { k - 1 , t } .$ . Two distinct characteristics of this relationship are the following. First, because stage k knows the demand to stage $k { - } 1$ , both stage k and stage k-1 can forecast the mean of demand based on the orders of stage $k { - } 2$ in n periods.

![](/api/attachments/2HSHG4V3/fulltext/images/f706e374af91980cf807ac40fa436b7e039ea81561dc78823dc35daf56787365.jpg)  
Fig. 4. Benefits comparing Models 1–3 with Model 0 for low demand variability.

$$
\hat {\mu} _ {1 t} = \hat {\mu} _ {2 t} = \sum_ {i = 1} ^ {n} D _ {t - i} / n, \quad k = 1, 2,
$$

and

$$
\hat {\mu} _ {k t} = \hat {\mu} _ {k - 1, t} = \sum_ {i = 1} ^ {n} Q _ {k - 2, t - i} / n, k = 3, \dots , N,\tag{12}
$$

where $\mathcal { Q } _ { k - 2 , t - i }$ is the order placed by stage k-2 and received by stage k-1 in period t.

Moreover, stage k can plan its safety stock based on the orders of stage k-1 in order to provide a given customer service level. Thus, by knowing its downstream inventory information, stage k can implement the 2-stage echelon-based inventory control. Similar to the derivation of Eq. (11), we can derive the variance of the orders placed by stage k:

$$
\begin{array}{l} \operatorname{Var} \left(Q _ {k} ^ {2}\right) = \left[ 1 + 2 \sum_ {j = 1} ^ {k} \left(L _ {j} + \mathrm{SS} _ {j}\right) \right. \\ \left. / n + 2 \left(\sum_ {j = 1} ^ {k} \left(L _ {j} + \mathrm{SS} _ {j}\right)\right) ^ {2} / n ^ {2} \right] \operatorname{Var} (D), \end{array}
$$

$$
k = 1, 2,
$$

and

$$
\begin{array}{l} \operatorname{Var} \left(Q _ {k} ^ {2}\right) = \left[ 1 + 2 \sum_ {j = 1} ^ {k} \left(L _ {j} + \mathrm{SS} _ {j}\right) \right. \\ \left. / n + 2 \left(\sum_ {j = 1} ^ {k} \left(L _ {j} + \mathrm{SS} _ {j}\right)\right) ^ {2} / n ^ {2} \right] \operatorname{Var} \left(Q _ {k - 2} ^ {2}\right), \end{array}\tag{13}
$$

where the safety stock, SS , is based on the variability of the orders from stage j-1.

In comparison with Eqs. (8) and (13) demonstrates that the increase in demand variability between stage k and stage k-1 is additive not multiplicative. Stage k uses the orders to stage k-1, which is less variable than the orders placed by stage k-1, to create more accurate forecasts. Thus, Model 2 eliminates one stage of information distortion, i.e., stage k-1, and consequently reduces some degree of the bullwhip effect. It can be further shown that compared with Model 0, sharing of inventory information not only improves supply chain fill rate but also reduces a certain degree of supply chain inventory. Compared with Model 1, this model increases inventory cost when the variability of the end demand is high.

## 4.4. Operational information (shipment data): Model 3

In Model 3, each stage of the supply chain knows its downstream customer’s outbound shipment data (Fig. 5). A shipment represents the amount of a product each stage immediately ships to its customer in response to a customer order after previous backorders are met. Suppose stage k-1 shares its shipment data with stage k. Let $W _ { k - 1 , t }$ and $I _ { k - 1 , t } ,$ respectively, be stage k-1’s outbound shipment and on-hand inventory in period t. We have $W _ { k - 1 , t } { = } \mathrm { m i n } \left\{ I _ { k - 1 , t } , \ Q _ { k - 2 , t } \right\}$ . If each stage maintains a high fill rate, the downstream shipments are very close to the orders to the downstream stage. In this case, we use the variance of downstream shipments to approximate that of the orders to the downstream stage. It follows from Eq. (13)

![](/api/attachments/2HSHG4V3/fulltext/images/0e06011c34fcdfd258a17be17c8d8c3e9bb5c379a427e7bc04466ff9642caac3.jpg)  
Fig. 5. Benefits comparing Models 1–3 with Model 0 for high demand variability.

that the variance of the orders placed by stage k can be expressed as:

$$
\begin{array}{l} \operatorname{Var} \left(Q _ {k} ^ {3}\right) \approx \left[ 1 + 2 \sum_ {j = 1} ^ {k} \left(L _ {j} + \mathrm{SS} _ {j}\right) / n + 2 \right. \\ \times \left(\sum_ {j = 1} ^ {k} \left(L _ {j} + \mathrm{SS} _ {j}\right)\right) ^ {2} / n ^ {2} \Bigg ] \operatorname{Var} \left(W _ {1} ^ {3}\right), \end{array}
$$

k ¼ 1; 2;

and

$$
\begin{array}{l} \operatorname{Var} \left(Q _ {k} ^ {3}\right) \approx \left[ 1 + 2 \sum_ {j = 1} ^ {k} \left(L _ {j} + \mathrm{SS} _ {j}\right) / n + 2 \right. \\ \times \left(\sum_ {j = 1} ^ {k} \left(L _ {j} + \mathrm{SS} _ {j}\right)\right) ^ {2} / n ^ {2} \Bigg ] \operatorname{Var} \left(W _ {k - 1} ^ {3}\right), \\ k = 3, \dots , N, \end{array} \tag {14}\tag{14}
$$

where the safety stock, ${ \mathrm { S S } } _ { j } ,$ is based on the variability of the shipments of stage $j - 1$

Like Model 2, this model eliminates one stage of distortion since the shipment data, unlike the downstream orders, are not subject to the bullwhip distortion. However, when stockouts occur at the downstream stage, the outbound shipments underrepresent the demand to the downstream stage and consequently underestimate the safety stock needed to buffer against demand uncertainty.

A simple method to adjust the downstream shipments to better reflect the customer’s true demand is that each stage tries to capture information on backorders (also including lost sales) and share this information with its supplier. Suppose stage k knows stage k-1’s shipments and backorders. It can estimate stage k-1’s real demand by adding its backorders to its shipments. Let $B _ { k - 1 , t }$ be stage k-1’s backorder in period t. We have

$$
Q _ {k - 2, t} = W _ {k - 1, t} + B _ {k - 1, t}\tag{15}
$$

With this equation, each stage of the supply chain can derive the demand to the downstream stage from its historical shipments and backorders data.

## 4.5. A hybrid information sharing strategy: Model 4

We have presented four information sharing models in a linear supply chain of a single product. In practice, a supply chain may carry a variety of products. Many firms have mass-customized their products to meet the requirements of different markets. The demand mix of a customizable product may change widely while the total demand remains the same. Moreover, different parts of the supply chain may have their own characteristics and may each require a different information sharing strategy. Hence we need to consider the effects of the supply chain structure and the demand patterns on information sharing for managing a supply chain with volatile demand mix.

A typical supply chain can be divided into a supplier network (upstream of final assembly) and a distribution network. The supplier network, in which products are in the raw or semi-finished states to be transformed and assembled at the manufacturer, is further away from consumers. Its inventories, including parts, components and subassemblies, have less value, greater commonality, and greater flexibility than finished products. So the objective of the supplier network is to improve service level to the manufacturer. On the other hand, the distribution network is close to consumers. Finished products have a much higher value, greater differentiation, and less flexibility than components. So the objective of the distribution network is to convey the right demand and lower inventories through reducing the distortion of demand information.

The supplier network and the distribution network may therefore require different information sharing strategies. In a volatile market place, the inventory information sharing strategy may be good for the supplier network because it offers the best customer service. The demand information sharing strategy, on the other hand, may be good for the distribution network because it provides each stage with real demand information and reduces the distortion of demand information. In Model 4 we combine the sharing of the strategic information (demand information) with the sharing of the operational information (inventory levels).

Let stage m be the manufacturing stage in a serial supply chain with N stages. In Model 4, Model 1 is used among stages m to 1 and Model 2 is used in the remaining stages. It follows from Eqs. (11) and (13)

that the variance of the orders placed by stage k can be expressed as:

$$
\begin{array}{l} \operatorname{Var} \left(Q _ {k} ^ {4}\right) = \left[ 1 + 2 \sum_ {j = 1} ^ {k} \left(L _ {j} + \mathrm{SS} _ {j}\right) / n + 2 \right. \\ \times \left(\sum_ {j = 1} ^ {k} \left(L _ {j} + \mathrm{SS} _ {j}\right)\right) ^ {2} / n ^ {2} \Bigg ] \operatorname{Var} (D), \end{array}
$$

$$
k = 1, \dots , m,
$$

where ${ \mathrm { S S } } _ { j }$ is chosen to buffer against the end demand variability and

$$
\begin{array}{l} \operatorname{Var} \left(Q _ {k} ^ {4}\right) = \left[ 1 + 2 \sum_ {j = 1} ^ {k} \left(L _ {j} + \mathrm{SS} _ {j}\right) / n + 2 \right. \\ \times \left(\sum_ {j = 1} ^ {k} \left(L _ {j} + \mathrm{SS} _ {j}\right)\right) ^ {2} / n ^ {2} \Bigg ] \operatorname{Var} \left(Q _ {k - 2} ^ {4}\right), \\ k = m + 1, \dots , N, \end{array} \tag {16}\tag{16}
$$

where ${ \mathrm { S S } } _ { j }$ is based on the variability of the orders received by stage j-1.

It can be shown that compared with the order information sharing strategy, the hybrid scheme not only improves fill rate but also greatly decreases supply chain inventory. Therefore, when demand mix uncertainty is high in the supply chain of multiple customized products, a hybrid information sharing scheme, which applies appropriate information sharing strategies to different parts of the supply chain, can reduce inventory costs and improve service level.

## 5. Simulation results

Section 4 has shown that information sharing can reduce the demand variability, which is caused by the information gaps among channel players and the resulting need for the safety stocks in the supply chain. The reduction in demand variability allows the supply chain to operate at high service levels with low inventories. In order to further validate the above analytical results, we conduct an extensive simulation study by using a multi-agent platform called Swarm. This section gives a brief introduction about Swarm and reports on several simulation experiments that illustrate the effects of information sharing strategies on supply chain performance.

## 5.1. SWARM simulation toolkit

Conventional simulation tools using the discrete event simulation approach with centralized control are not suitable for simulating multi-agent systems (MAS). In typical MAS agents are distributed, are autonomous but interdependent, are embedded with self-organization capability, and are adaptive to changes in their environment. Some of the requirements for a simulation system to model the above features are: (1) object-oriented (OO) capability for agent formation, so that agents can be created with internal state, behavior, and knowledge, (2) communication facility between agents for simulating information exchange (e.g., message passing), (3) ability to simulate different degrees of autonomy for agents (e.g., decentralized control and parallelism), and (4) visualization capability for monitoring the agents.

Swarm, a multi-agent simulation software platform developed at the Santa Fe Institute, satisfies all the above requirements. It consists of an OO framework for defining the behavior of agents and other objects that interact during a simulation. An agent in Swarm consists of a data structure containing the internal state of the agent, a step function for an active agent to initialize action, and action functions which are triggered by the messages received from its environment (from other agents or simulation control objects). Swarm uses the individual-based modeling approach allowing each agent to have its own internal state affected by its past experience and determining its future actions. It is more realistic to model agents that have local view of the world, combinations of which produce the collective behavior of the whole group. Furthermore, Swarm allows for different granularity of agents whereby an agent can itself be a swarm of sub-agents providing for the creation of nested inherent hierarchy of schedules. It supports an entire spectrum of time and synchrony management ranging from strict, top-down, lock-step synchrony managed by a single sequential executor to loose asynchrony with effective parallelism. Finally, it uses Tcl scripting language and Tk widget set to define batch-oriented and graphical interfaces for providing visualization capability.

Table 1

Swarm uses a hybrid of both the discrete event and time stepped simulation schedules. During execution, the kernel scheduler traverses the scheduler list to inform agents to act by sending them messages at specified time. Agents that receive a message perform actions according to their action models. The action may generate another state which is inserted in the schedule list. In this way Swarm works as a discrete event simulator. Swarm also allows users to design agents with fixed schedules that continue to repeat the same actions, which works as a time-stepped simulator.

## 5.2. Simulation design

The simulation design of a linear supply chain in Swarm used for our experiments contains three basic types of agents: entity, customer, and source agents. The entity agent models the behavior of an enterprise. Its basic functions are to receive orders from and ship them to its downstream customer, forecast the production quantity, and order and receive input components from its supplier accordingly. It also has manufacturing capabilities, which can transform an input component into a new output product, or assemble several input components into a product. The supply chain has four tiers: retailer (tier 1), distributor (tier 2), manufacturer (tier 3), and supplier (tier 4).

For simplicity, in our experiments we allow multiple entities in tiers 1 and 4, but only one manufacturer and one distributor. We also limit production to be performed by the manufacturer only although the simulation program can be used to test postponement strategies that require manufacturing at the other tiers. The customer agent and the source agent are environmental agents that generate the exogenous and endogenous variables to the supply chain. The customer agent generates the demand to each tier 1 entity agent and consumes the product shipped by tier 1 entity agents. The source agent receives orders from the most upstream enterprise agent and ships products to it accordingly.

A typical cycle in the execution of the simulation starts with the entity agents and the source agents shipping the orders received in the previous cycle to their customers. The entity agents then calculate their stock level. At the same time, the various state variables of entity agents are reset or updated. Starting from the customer agent, for each output product, a demand is generated and placed with the tier 1 entity agents. Upon receiving the order from its customer, each entity agent then calculates its production quantity based on its desired stock level, and places an order with its upstream supplier. This execution goes from tier 1 entities to tier 4 entities and ends when the source agent receives the order. The cycle repeats starting with the shipping action.

The role of the information sharing policy is to enable the enterprise to forecast more accurately by setting the stock level appropriately. Depending on the information sharing policy used, the stock level of each enterprise is calculated based on the equations given in Section 4. The details about the simulation algorithm are presented in Fig. 3.

## 5.3. Experimental design and results

In our first experiment, we study the behaviors of the four basic models under low consumer demand variability. We make the following assumptions in designing our simulation experiments: each enterprise has only one supplier per product, but a supplier may supply more than one product. The end-demand process is normally distributed with $\mu { = } 1 0 { , } 0 0 0$ and r=866. The replenishment lead time for each stage is 3 periods. The inventory and backorder costs used in the experiments are listed in Table 1. Fixed costs are expressed as a constant cost per unit of inventory and variable cost as a percentage of the value of the product. Inventory cost is lowest at the supplier and increases towards downstream. Since manufacturing takes place only at tier 3, it is the only tier that has input inventory costs. Backorder cost is the cost incurred when inventory out-of-stock occurs and is expressed as a percentage of the value of output product. Manufacturing cost is fixed at \$5 per unit and the production cost (material cost+manufacturing cost) is fixed at \$15 per unit.

Inventory and backorder costs

<table><tr><td></td><td>Tier 1</td><td>Tier 2</td><td>Tier 3</td><td>Tier 4</td></tr><tr><td>Variable output inv holding (%)</td><td>15</td><td>12</td><td>8</td><td>4</td></tr><tr><td>Fixed output inv holding ($)</td><td>1</td><td>0.6</td><td>0.4</td><td>0.2</td></tr><tr><td>Variable input inv holding (%)</td><td></td><td></td><td>7</td><td></td></tr><tr><td>Fixed input inv holding ($)</td><td></td><td></td><td>0.3</td><td></td></tr><tr><td>Backorder cost (%)</td><td>25</td><td>20</td><td>15</td><td>10</td></tr></table>

We ran the simulation for 150 periods per run and averaged the statistics over 150 periods. Then we repeated 10 runs and averaged the statistics over ten runs. Using Model 0 as a base case, we evaluate the relative performance of the other models by looking at the percentage improvement in inventory costs and fill rate over the base case. Since the goal of the experiments is to study the behavior of information sharing policies and not optimization, we ignore costs related to transportation, coordination, technology, and negotiation.

Fig. 4 reports the simulation estimates of these percentage benefits. The demand information sharing strategy experiences 74.75% decrease in inventory costs and a slight increase in fill rate. The inventory information sharing strategy experiences 5.79% increase in fill rate while its inventory savings of 34.32% are not as significant as that of the demand information sharing strategy. The shipment information sharing strategy experiences 52.73% decrease in inventory costs while there is 6.53% decrease in fill rate. The pattern depicted in Fig. 4 is consistent with the analytical findings presented in Section 4. When demand is relatively stable, information sharing can significantly reduce information distortion and order variability. The reduction of order variability both reduces inventory and improves fill rate.

In our second experiment, we study the behaviors of these models under high consumer demand variability. This experiment considers a single product with a demand fluctuating between two processes. The high-range demand is specified by $\mu { = } 1 5 { , } 0 0 0$ and r=1299, the low-range demand is specified by l=5000 and r=433, and the high or low range is randomly selected every simulation cycle. Other parameters are the same as those in previous experiment. Fig. 5 presents the simulation estimates of the percentage benefits realized through information sharing under volatile demand. Compared with the order information sharing strategy, the demand information sharing strategy experiences 18.74% decrease in fill rate; the inventory information sharing strategy experiences 3.96% increase in fill rate but its inventory savings are less than that of the demand information sharing strategy; the shipment information sharing strategy experiences 6.32% decrease in fill rate. The pattern depicted in Fig. 5 also is consistent with the findings presented in Section 4. When the variance of consumer demand is high, each stage of the supply chain needs to keep enough safety stock to buffer against high order variability. The demand information sharing strategy lowers supply chain inventory by planning its safety stock based on consumer demand, but the resulting lower buffer gives a lower fill rate. The inventory information sharing strategy, on the other hand, gives the best customer service, but may drive inventory up when consumer demand has high variance. Under the shipment information sharing strategy, each stage under-estimates the downstream demand and results in a low fill rate.

Finally, we study the behavior of the hybrid information sharing strategy when product mix is volatile. This experiment considers the scenario that four end products are customized from a generic platform in a linear supply chain. One product dominates 70% of the market while the remaining three take 10% of the demand each. The dominating product is randomly selected and changes every cycle. Although the total demand is constant, the demand for each product changes randomly.

Our simulation results indicate that the hybrid information strategy is a powerful strategy (see Fig. 6). The results show that the hybrid information sharing strategy experiences 20% decrease in inventory costs and 3.45% increase in fill rate. The hybrid strategy offers better customer service than other information sharing models while reducing the inventory considerably. While the demand information sharing strategy dramatically lowers the supply chain inventory, the reduced inventory jeopardizes customer service under a volatile demand mix. Although the inventory information sharing strategy gives good customer service, the bullwhip effect may drive the inventory up.

![](/api/attachments/2HSHG4V3/fulltext/images/aa80639481d93f493efa42bd2ba8ef12012a3cd21814d386d1649ef6f00f4726.jpg)  
Fig. 6. Benefits comparing Models 1–4 with Model 0 for volatile product mix.

## 6. Conclusions and future work

Both electronic markets and electronic hierarchies require effective sharing of information across organizations in order to reduce transaction costs, inventory costs, and serve their customer better. Since information flows are characterized by the type of information shared and areas where the information flows are conducted, the categorization of inter organizational information sharing proposed in this paper will lead to a greater understanding of business dynamics.

We use the supply chain system as a representative case for both electronic hierarchies and electronic markets to illustrate the effects of information sharing on the system performance. Our supply chain example offers the following insights. First, information sharing helps counter the phenomenon of demand variability amplification, mainly caused by the time lag between channel partners in the supply chain. The sharing of demand information reduces the information distortion to a large extent while the sharing of inventory data and shipment data reduces at least one level of information distortion.

Second, the impact of information sharing on supply chain performance largely depends on demand patterns and the supply chain structure. No information sharing strategy is uniformly superior because each supply chain has its unique characteristics. We find that various information-sharing schemes consistently improve supply chain performance under relatively stable demand. When the variance of consumer demand is high, however, the performance of information sharing strategies varies.

We further consider a hybrid scheme that utilizes the strengths of both the demand information sharing strategy and the inventory information sharing strategy for managing the supply chain with volatile product mix. Results show that the hybrid scheme is a powerful concept for managing product mix uncertainty.

The adoption of information sharing policies in the industry is widespread. There are many case studies about how enterprises dramatically improve in performance after adopting variations of information sharing policies like continuous replenishment program and vendor managed inventory. Most of these studies center on the <sup>b</sup>before and after<sup>Q</sup> performance due to information sharing. There is very little study in understanding how these policies behave and how they interact with other supply chain parameters.

For example, Boeing models the assembly of aircraft for each link in the supply chain and communicates to each supplier what parts are needed and when. This communication is done quickly and seamlessly through EDI links or directly from one database to another. With information sharing Boeing was able to cut its cycle times in half and reduce parts defects by 56%. Thomson Consumer Electronics gives its suppliers access to forecast information, inventory levels, and customer orders. Its global suppliers post their shipping information and order status on the Thomson extranet site. As a result, lead times and planning cycles have come down from as long as 4 weeks to as little as 1 week. Dell Computer now shares demand forecasts and other customersensitive information with its top suppliers. As a result, suppliers can more easily match their production schedules to Dell’s—making only what is needed, when it is needed. Dell is also passing on data about its defect rates, engineering changes, and product enhancements to these suppliers. Similar benefits from information sharing in their supply chains have been realized by such diverse firms as Dayton Hudson, Home Depot, and Eastman Chemical.

As part of our future work, we would like to investigate the application of the policies discussed in this paper in real world situations and validate the simulation results with real world case studies. There are also many open research issues that remain to be examined. First, while this paper focuses on the study of information sharing in supply chains, more studies are needed to look into the information sharing issues in the context of general electronic marketplaces. An important issue not addressed in this paper is how firms can leverage the value of information sharing and the reduced switching costs without losing the benefits of price competition. Certainly electronic marketplaces must be adaptive and flexible enough to exploit the benefits of competition. But do buyers really benefit by changing suppliers for every transaction or product run? In most situations, the answer may be no. Second, for hierarchical supply chains, more studies are needed to look into matching the demand process, production and distribution process, and supply chain structure with the right information sharing strategies.

## References

[1] K.S. Anand, H. Mendelson, Information and organization for horizontal mulitmarket coordination, Management Science 43 (12) (1997 Dec.) 1609–1627.

[2] J.Y. Bakos, Information links and electronic marketplaces: the role of interorganizational information systems in vertical market, Journal of Management Information Systems 8 (2) (1991 Fall) 31– 52.

[3] A. Barua, B. Lee, An economic analysis of the introduction of an electronic data interchange system, Information Systems Research 8 (4) (1997 Dec.) 398–422.

[4] R.I. Benjamin, D.W. deLong, S.M. Morton, Electronic data interchange: how much competitive advantage, Long-Range Planning 23 (4) (1990 Feb.) 29–40.

[5] G. Cachon, M. Fisher, Supply chain inventory management and the value of shared information, Management Science 46 (8) (2000 Aug.) 1032– 1048.

[6] F. Chen, Echelon reorder points, installation reorder points, and the value of centralized demand information, Management Science 44 (12) (1998 Dec.) S221–S234.

[7] F.Y. Chen, Z. Drezner, J.K. Ryan, D. Simchi-Levi, The bullwhip effect: managerial insights on the impact of forecasting and information on variation in a supply chain, in: S. Tayur, R. Ganeshan, M.J. Magazine (Eds.), Quantitative Models for Supply Chain Management, 1999, Kluwer Academic Publishers, Norwell, MA, pp. 417– 439.

[8] F.Y. Chen, Z. Drezner, J.K. Ryan, D. Simchi-Levi, Quantifying the bullwhip effect in a simple supply chain: the impact of forecasting lead times and information, Management Science 46 (3) (2000 Mar.) 436–443.

[9] V. Choudhury, Strategic choices in the development of interorganizational information systems, Information Systems Research 8 (1) (1997 Mar.) 1 – 24.

[10] P. Chwelos, I. Benbasat, A.S. Dexter, Research report: empirical test of an EDI adoption model, Information Systems Research 12 (3) (2001 Sept.) 304– 321.

[11] R.H. Coase, The nature of the firm, Economica 4 (16) (1937 Nov.) 385–405.

[12] S. Gavirneni, R. Kapuscinski, S. Tayur, Value of information in capacitated supply chains, Management Science 45 (1) (1999 Jan.) 14– 24.

[13] F.A. Hayek, Individualism and economic order, University of Chicago Press, Chicago, IL, 1948.

[14] R. Johnston, P.R. Lawrence, Beyond vertical integration<sub>U</sub>the rise of the value-adding partnership, Harvard Business Review 66 (4) (1988 Jul.) 94–101.

[15] A. Kambil, E. Heck, Reengineering the Dutch flower auctions: a framework for analyzing exchange organizations, Information Systems Research 9 (1) (1998 Jul.) 1 – 19.

[16] H.L. Lee, C. Billington, Material management in decentralized supply chain, Operations Research 41 (5) (1993) 835– 847.

[17] H.L. Lee, P. Padmanabhan, S. Whang, Information distortion in a supply chain: the bullwhip effect, Management Science 43 (4) (1997 Apr.) 546– 558.

[18] H.L. Lee, P. Padmanabhan, S. Whang, The bullwhip effect in supply chains, Sloan Management Review 38 (3) (1997 Spring) 93– 102.

[19] H.L. Lee, K.C. So, C.S. Tang, The value of information sharing in a two-level supply chain, Management Science 46 (5) (2000 May) 626– 643.

[20] T.W. Malone, K. Crowston, The interdisciplinary study of coordination, ACM Computing Surveys 26 (1) (1994 Mar.) 87– 119.

[21] T.W. Malone, J. Yates, R.I. Benjamin, Electronic markets and electronic hierarchies, Communications of the ACM 30 (6) (1987 Jun.) 484– 497.

[22] K. Moinzadeh, A multi-echelon inventory system with information exchange, Management Science 48 (3) (2002 Mar.) 414– 426.

[23] T. Mukhopadhyay, S. Kekre, S. Lalathur, Business value of information technology: a study of electronic data interchange, MIS Quarterly 19 (2) (1995 Jun.) 137– 156.

[24] S. Nahmias, Production and Operations Analysis, Richard Irwin, Homewood, IL, 1989.

[25] G. Premkumar, Interorganization systems and supply chain management: an information processing perspective, Information Systems Management 17 (3) (2000 Jun.) 56–68.

[26] S. Raghunathan, Information sharing in a supply chain: a note on its value when demand is nonstationary, Management Science 47 (4) (2001 Apr.) 605 – 610.

[27] T. Seidmann, A. Sundararajan, Sharing logistics information across organizations: technology, competition and contracting, in: C.F. Kemerer (Ed.), Information Technology and Industrial Competitiveness: How IT Shapes Competition, 1998, Kluwer Academic Publishers, Boston, pp. 107– 136.

[28] E.A. Silver, R. Peterson, Decision Systems for Inventory Management and Production Planning, 1985, John Wiley, New York.

[29] K. Srinivasan, S. Kekre, T. Mukhopadhyay, Impact of electronic data interchange technology on JIT shipments, Management Science 40 (10) (1994 Oct.) 1291–1304.

[30] E.T.G. Wang, A. Seidmann, Electronic data interchange: competitive externalities and strategic implementation policies, Management Science 4 (3) (1995 Mar.) 410 – 418.

[31] O.E. Williamsom, Markets and Hierarchies, MacMillan, New York, 1975.

[32] O.E. Williamsom, Economic Organization, Firms, Markets and Policy Control, 1986, Wheatsheaf Books, United Kingdom.

Jingquan Li is a doctoral student in the Department of Business Administration at University of Illinois. His research interests include privacy protection and fraud detection in data mining, economics of IT, supply chain management, and IT strategy.

Riyaz Sikora is an Associate Professor of Information Systems at the College of Business at the University of Texas at Arlington. Dr. Sikora has published refereed scholarly papers in journals such as Management Science, Information Systems Research, INFORMS Journal of Computing, IEEE Transactions on Engineering Management, and IEEE Transactions on Systems, Man, and Cybernetics. His current research interests include multi-agent systems and data mining. He is on the editorial board of the Journal of Information Systems and e-Business Management and the Journal of Database Management. He is a co-founder and co-chair of the AIS SIG on Agent-based Information Systems.

Michael Shaw is a Professor/Hoeft Endowed Chair of Information Technology and Management, the Director of Center for Information Systems and Technology Management, and the Director of Graduate Studies at the University of Illinois at Urbana-Champaign. He has published more than a hundred research papers in academic journals and proceedings on topics focused on intelligent systems, decision support, network theory, complex systems, electronic commerce, and information technology. Dr. Shaw has edited five books and is currently on the editorial board of more than ten journals. He is the co-editor of the journal Information Systems and e-Business Management.

Gek Woo Tan is a faculty member at the National University of Singapore. She holds a PhD in MIS from University of Illinois at Urbana-Champaign. Her research interests include Data Mining and Knowledge Discovery, Supply Chain Network, and Information Retrieval on the Web.
