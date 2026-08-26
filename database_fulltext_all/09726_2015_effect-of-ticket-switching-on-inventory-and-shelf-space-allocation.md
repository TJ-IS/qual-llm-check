---
otero_id: 9726
otero_key: "6YNH64PE"
title: "Effect of ticket-switching on inventory and shelf-space allocation"
authors: "Wei Zhou; Selwyn Piramuthu"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.11.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Wei Zhou <sup>a,c</sup>, Selwyn Piramuthu <sup>b,c,</sup>⁎

<sup>a</sup> Information & Operations Management, ESCP Europe, Paris, France

<sup>b</sup> Information Systems and Operations Management, University of Florida, USA

<sup>c</sup> RFID European Lab, Paris, France

## a r t i c l e i n f o

Article history: Received 24 February 2014 Received in revised form 14 September 2014 Accepted 30 November 2014 Available online 5 December 2014

Keywords: Ticket-switching Inventory information accuracy Retailer Shelf-space allocation

## a b s t r a c t

Ticket-switching incidents simultaneously and directly affect the actual and store information system inventory of multiple products. We model the discrepancy in inventory information stored in the retailer's information system vs. reality and related consequences for the customer and the retail store. We also consider a retail store with constrained shelf-space availability and study how this retailer should optimally allocate shelf-space between these products when ticket-switching is present. We model this by taking into account the customer arrival sequence. For customers who use online store inventory information, our results indicate that in the presence of ticket-switching, an item can be guaranteed to be in-stock at the store for immediate pick-up only for ‘cheap’ items. The results from this study also have policy implications for retail stores in terms of computing bene<sup>fi</sup>t estimates as well as shelf-space allocation.

© 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

Inventory shrinkage, a signi<sup>fi</sup>cant issue in retail stores, arises due to several sources that include employee-theft [10], shoplifting [6], process errors, vendor errors, item misplacement [14], spoilage of perishables [15], breakage during handling, ticket-switching [26], among others. Among these, employee-theft and shoplifting are generally considered to be major contributors that add to about 80% of the overall inventory shrinkage [5].

Several forms of shrinkage and related effects on retailing have been studied by researchers. A common denominator in a majority of shrinkage cases is that each such incident affects only one product. For example, when a camera is stolen from a retail store, the store experiences all related losses due entirely to just this item. While this loss can be significant to the retailer, the effect of this loss is isolated. However, to our knowledge, only one type of shrinkage simultaneously and directly affects multiple items. Ticket-switching is the deliberate act of switching the (price) identi<sup>fi</sup>er or ticket on an item with the explicit intention of paying less than the item's retailer-set price. Oftentimes, the perpetrator switches the (price) identi<sup>fi</sup>er or ticket on an item that sells for a (much) higher price (‘expensive’ item) with that of an item that sells for a lower price (‘cheap’ item). For example, a hanging bar code on an expensive item is replaced by one from a cheap item before check-out, with the intended outcome that the customer pays only the cheap item's price to ‘purchase’ the expensive item. When such an incident occurs, two items are simultaneously affected: the expensive item is gone while the cheap item is left without a price tag or identi<sup>fi</sup>er. When this cheap item is the last item in stock of this type or SKU, it is often dif<sup>fi</sup>cult for the store personnel to reestablish its identity (i.e., generate another identi<sup>fi</sup>er, bar code, or price tag for this cheap item) and the item stays in limbo.

To our knowledge, statistics on retailer loss due to ticket-switching is hard to come by simply because of its nature as well as the simultaneous presence of other types of shrinkage. Based on our discussions with major retailers both in the US (e.g., Target, Wal-Mart, and others) and Europe (e.g., Carrefour, Groupe Beaumanoir, Marks & Spencer, Metro, and others), although widespread existence of ticket-switching is acknowledged, none of the retailers we contacted were able to provide speci<sup>fi</sup>c data on ticket-switching incidents. However, several of these retailers have initiatives in place that involve training store personnel to be aware of ticket-switching (e.g., ensure that shoes and the corresponding shoe boxes indeed match, ensure that scanned item information on the checkout terminal display matches the scanned item, among others). While such initiatives are a good <sup>fi</sup>rst step, retailers acknowledge that expectations with respect to their implementation are rather low due to (a) the heavy workload already faced by these store personnel, (b) process slow-down when such an initiative is strictly followed, (c) the similarity of the ticket-switched items (e.g., organic vs. conventional apple), (d) the existence of employee complicity, among others.

According to a recent study [8], Electronic Article Surveillance (EAS) was found to be quite effective in reducing shrinkage. The Food Marketing Institute (FMI) estimates that retailers with sales of more than US\$3 billion per year experienced lower shrinkage due to better process management and signi<sup>fi</sup>cant investments in loss prevention measures such as video surveillance, EAS/RFID (Radio-Frequency IDenti<sup>fi</sup>er)/ sensor systems [17], exception reporting, access control and intrusion systems, social media, among others.

Based on a survey of 1187 retailers in 43 countries world-wide, the Global Retail Theft Barometer found that retail shrinkage in 2011 cost the industry an estimated US\$119 billion, which is about 1.45% of overall sales. Among different retail categories, apparel, health/beauty and DIY (Do-it-Yourself) experienced the highest shrinkage. While this percentage appears to be rather small, it should be noted that even a 2 to 3% loss of sales can translate to about 25% loss in pro<sup>fi</sup>t in this industry with tight pro<sup>fi</sup>t margins [19]. Moreover, in terms of pro<sup>fi</sup>t, shrinkage reduction from 2% to 1% is tantamount to sales increase of 40% (e.g., [1,4]). Therefore, the importance of shrinkage reduction cannot be overstated.

A ticket-switching event could easily be misinterpreted and counted as a combination of other types of shrinkage. It is also dif<sup>fi</sup>cult to determine which items comprise a ticket-switched pair from aggregate shrinkage data. Given that theft is a large part of shrinkage, it is reasonable to assume that ticket-switching is signi<sup>fi</sup>cant even if it's a small fraction of the overall theft statistic. Moreover, based on our knowledge of publicly-available ticket-switching incidents and the fact that several of these required only the use of cheap and readily available devices (e.g., bar code printers), we can reasonably assume that such incidents are not uncommon.

Given the existence of ticket-switching in retail store environments and their peculiar dynamic with respect to the inventory level of multiple items, there is a surprising lack of research literature that consider this phenomenon. We attempt to address this gap in extant published literature. We consider ticket-switching from a shelf-space allocation perspective and associated dynamics of information generated by the store inventory information system as well as the actual state of affairs. Speci<sup>fi</sup>cally, we consider the existence of two products — one ‘cheap’ and the other ‘expensive’ — and the switching of the expensive product's ticket with that from the cheap product. We then consider the effect of ticket-switching on shelf-space allocation (e.g., [9]) and possible in<sup>fl</sup>ation/de<sup>fl</sup>ation of information due to its invisibility to the store's inventory information system until its synchronization with actual store inventory. To our knowledge, this is the <sup>fi</sup>rst paper to consider store inventory dynamics and shelf-space allocation in the presence of ticket-switching behavior. For the remainder of the paper, we use ‘information system’ to refer to the store's inventory information system.

We study a few facets of the dynamics of ticket-switching incidents that are novel to existing literature. Based on these, the contributions of this paper are three-fold: (a) we model the bene<sup>fi</sup>ts to the retailer and suggest associated policy implications when ticket-switching behavior is present, (b) we model shelf-space allocation in the presence of ticket-switching behavior and suggest related policy implications and (c) we suggest implications for the customer when ticket-switching behavior is known to exist.

Our results have practical and policy implications for both customers as well as retail stores when ticket-switching is present. For customers who use the store's online inventory checker to ensure that an item is in stock for in-store pick-up, the in-store-stock guarantee can be provided only for the ‘cheap’ items. The store inventory manager must allocate more space to the ‘expensive’ items, especially those with more unit revenue and stock-out cost. When computing revenue estimates based on information from the store information system, care should be taken to consider de<sup>fl</sup>ation in the estimated results.

The remainder of the paper is organized as follows: We brie<sup>fl</sup>y discuss ticket-switching and some recent ticket-switching incidents that gained wide-spread media-attention in Section 2. In Section 3, we model disparities in information from the information system and actual inventory in the presence and absence of ticket-switching incidents. We model shelf-space allocation when ticket-switching is present in Section 4. We conclude the paper in Section 5 with a brief discussion on <sup>fi</sup>ndings and possible extensions to this study.

## 2. Ticket-switching

Although there is no publicly-available statistic or historical data on ticket-switching incidents, ticket-switching cannot occur in the absence of price tag or identi<sup>fi</sup>er/ticket. Moreover, ticket-switching requires the simultaneous existence of a ‘cheap’ and an ‘expensive’ item at a retail store. It is, therefore, reasonable to assume that the origin of ticket-switching incidents dates back only as far in time as the introduction of item-level price tags [25] or some form of item-level identi<sup>fi</sup>er/ ticket in retail environments. In principle, while it is possible to ticketswitch items with the same price, we are not aware of any such reported incidents. Nevertheless, our developed model implicitly includes this case.

As the number of items sold at a single retailing environment grew, it most likely became relatively dif<sup>fi</sup>cult to deter and/or prevent ticketswitching behavior. Retailers' introduction and use of item-level price stickers presumably facilitated ticket-switching behavior. About four decades ago, the introduction of automatic identi<sup>fi</sup>cation technology such as bar code, which enables relatively ef<sup>fi</sup>cient inventory-taking and check-out, facilitated successful ‘purchase’ of ticket-switched items. This is readily accomplished since the check-out person may not necessarily be vigilant to match each purchased item with information associated with the scanned bar code and the item's price.

Among different price-/item- identi<sup>fi</sup>cation technologies, price stickers are the easiest to switch since they generally don't have any information about the associated item. On the other hand, bar codes have relevant information (e.g., the item's identity) stored in database(s) that are readily accessible by check-out personnel. At this point in time, bar codes are the most commonly used technology for check-out information in retail settings. Price stickers are not that uncommon while RFID (Radio-Frequency IDenti<sup>fi</sup>cation) tags are slowly being introduced [24], albeit primarily for inventory management purposes at present.

Although not presumed to be uncommon, ticket-switching behavior is rarely caught by retailers who bear all related losses. While the primary effect of ticket-switching is the capital loss associated with the difference in price of the cheap and expensive items, the retailer suffers additional consequences. These consequences depend on the frequency at which the information system is synchronized with actual inventory at the store. When ticket-switching occurs, the information system incorrectly registers the existence of a larger number of expensive items and fewer cheap items than the actual state of inventory. When several ticket-switching incidents occur at the same store, this accumulated mismatch between actual and information system based inventory levels could wreak havoc with effective inventory management. The consequences of such a mismatch include stock-outs of expensive items (that generally have higher margins), excessive inventory of the cheap item that is invisible to the information system, and increased inventory and storage cost of cheap items. When the cheap item is perishable, its increased inventory has the potential to result in higher loss due to ‘unsalables’.

A majority of ticket-switching cases go unreported. The news media generally pick up such incidents only when a large number of items, high monetary value, celebrity, or some bizarre person/modus operandi is involved. For example, a customer at a San Francisco Bay Area Target store was caught af<sup>fi</sup>xing home-made bar codes to packages of LEGOs that allowed him to purchase expensive sets at substantial discounts [13]. He apparently then sold these items through eBay and made about \$30,000 per year from these sales. In another case, two couples were charged with defrauding Wal-Mart stores about \$1.5 million across 19 states over the last decade where a home computer was used to print bar codes of cheaper items meant to be ticket-switched [18]. The suspects then allegedly either sold the merchandise elsewhere or returned them for store gift cards. These suspects apparently avoided detection in part by visiting stores during the busiest periods. A Colorado University freshman used bar codes printed in his dorm room with ‘Barcode magic’ to buy big-ticket electronic gadgets cheap at a local Target store. For example, with a home-made bar code for a CD player that costs \$4.99, he bought a system for using iPods valued at \$149.99 [27]. A customer at a Leclerc supermarket in Trélisssac, Dordogne was caught during check-out for replacing the labels on two 2300 bottles of Petrus with 2.50 labels [20]. Recently [2], four men were indicted for ticket-switching scheme committed at Home Depot stores that spread over a dozen states. These men allegedly returned the fraudulently purchased merchandise without receipt to the store for refund credit cards.

From the customer's perspective, a simple (sticker) price tag is the easiest to switch but dif<sup>fi</sup>cult to check-out while an RFID tag is the most dif<sup>fi</sup>cult to switch and easiest to check-out of the store. Since the price tag is af<sup>fi</sup>xed or attached on the item, it is easy to switch but the price-switched item has a positive probability of being discovered by knowledgeable check-out personnel. Ticket-switching is dif<sup>fi</sup>cult to accomplish with RFID since (a) unlike printing a cheap item's bar code, it is dif<sup>fi</sup>cult to copy/clone [12] the content of the cheap item's RFID tag and (b) the tag may be embedded in the item. Moreover, the customer cannot switch the RFID tag from an already-purchased cheap item since the system knows that that tagged item was already purchased from the store — i.e., can't buy the same (unique coded) item more than once. However, after successful ticket-switching, it is relatively easy to remove an RFID-tagged item from a store with automated check-out. It is relatively easy to ticket-switch items with bar codes since bar codes are always af<sup>fi</sup>xed on the item. However, it is relatively dif<sup>fi</sup>cult to pay the ticket-switched price for this item since a vigilant check-out personnel could verify that the result from bar code scan re<sup>fl</sup>ects information on the exact physical item that is being purchased.

In general, ticket-switching is carried out by customers without the knowledge of store personnel. A variant of ticket-switching is ‘sweethearting’ (e.g., [3,4]), where a cashier scans a cheap (e.g., pack of chewing gum) item's bar code (that's taped on his/her wrist to fool an overhead surveillance camera) in order to help someone (e.g., a friend) purchase an expensive item for the price of the cheap item.

The research publications that discuss and/or model ticketswitching or sweethearting behavior, that we are aware of, include [3, 4,12] and [26]. All of these consider means to address ticket-switching through deterrence, prevention, or recognition as it occurs. For example, using a 6000 class database. [3] consider self-checkout at retail stores and develop a system that uses each item's visual appearance to ensure that the correct item's code was registered for each order-line in a transaction. Through experiments, they provide evidence for increased security need and convenience and even argue for the complete elimination of the scale. Camera-based applications are commonly used for loss-prevention in retail stores. However, a majority of these are manual systems that comprise cameras and video displays that are infrequently monitored by store security personnel. These are extremely ineffective systems since they require continual observation of every customer at the store. Over the past several years, such camera-based applications have witnessed the incorporation of computer-vision intelligence and automation. In addition to providing an excellent overview of such systems, [4] presents promising technical directions in retail video analytics. The only published research papers, to our knowledge, that speci<sup>fi</sup>cally consider ticket-switching are [12] and [26]. Both these papers develop cryptographic authentication protocols that attempt to address ticket-switching incidents. Both these papers are related in a sense since [26] extends [12] with the introduction of several different scenarios and related authentication protocols.

## 3. Modeling the ticket-switching problem

Retail stores use inventory information from their information systems to make critical decisions (e.g., order placement). It is widely acknowledged that even a minor inaccuracy in this information translates to disruptions in replenishment process and severe stock-out situations (e.g., [11]). Inaccuracies can arise due to several factors that include shrinkage in its various forms. To rectify any difference between actual inventory and those inventory values that are stored in the information system, most stores take manual inventory of their entire store and then make appropriate adjustments to the data stored in their information systems. While this is acceptable, in principle, the low frequencies $( \mathrm { e . g . }$ , once in more than 3 months is not uncommon) at which manual inventory is taken lead to unnecessary loss for the retailer. It should be noted that the process of manually taking the inventory of the entire store is resource-intensive and certainly not trivial. We consider inventory level disparities between data stored in the information system and reality due only to ticket-switching incidents.

## 3.1. Notations

We use the following notations throughout the rest of the paper:

• C, E: Cheap and expensive items respectively

$i \in \{ C , E \}$

• $\lambda _ { i } \dot { \cdot }$ Arrival rate for customers of type i items;

$\lambda = \lambda _ { C } + \lambda _ { E }$

• α: Proportion of $\lambda _ { E }$ who are honest E customers $( 0 \leq \alpha \leq 1 )$

• ρ : Arrival probability for customers of type i items

$\begin{array} { r } { \rho _ { i } = \frac { \lambda _ { i } } { \lambda } } \end{array}$

• c : Stocking cost per type i item

• q<sub>i</sub>: Quantity of type i item stocked by retailer

• Q: Available shelf-space; assume: $Q = q _ { C } + q _ { E }$

• P (n|N): Probability that n out of N customer arrivals are for item

$P _ { i } ^ { I } ( . ) { \ ; }$ Probability that a customer for item i <sup>fi</sup>nds at least one available item i

$P _ { i } ^ { I } ( n , q _ { C } , q _ { E } ) \colon P _ { i } ^ { I } ( . )$ for the $n ^ { t h }$ customer under $q _ { C }$ and $q _ { E }$

$P _ { i } ^ { O } ( . ) { \mathrm { : } }$ Probability that a customer for item i <sup>fi</sup>nds item i out of stock

$P _ { i } ^ { o } ( n , q _ { C } , q _ { E } ) \colon P _ { i } ^ { O } ( . )$ for the $n ^ { t h }$ customer under $q _ { C }$ and $q _ { E }$

• r : revenue from sale of a unit of i

• s : Stock-out cost associated with i

$P ( D ) , P ( D ^ { T } )$ : Probability of D unit demand without and with ticketswitching respectively

$B ^ { T } ( n , q _ { C } , q _ { E } ) , B ( n , q _ { C } , q _ { E } )$ : Expected bene<sup>fi</sup>t of $n ^ { t h }$ customer w/ and w/o ticket-switching

$B ( q _ { C } , q _ { E } ) \colon$ The expected bene<sup>fi</sup>t of stocking $q _ { C }$ and $q _ { E }$ units of C and E respectively

$\Pi ( q _ { C } , q _ { E } ) \colon$ The expected pro<sup>fi</sup>t of stocking $q _ { C }$ and $q _ { E }$ units of C and E respectively.

## 3.2. Assumptions

We assume that the store sells only two types of items: cheap and expensive. Customers, who buy only one type of item, know what item they want before they visit the store. If the item they want (e.g., cheap item) is unavailable on the store shelf, they leave without making a purchase. We assume that the customers who arrive at the store with the intention of purchasing a cheap item will not participate in ticket-switching. However, among those who purchase the expensive item, only a small fraction (1 − α) participate in ticket-switching.

We assume that every (cheap and expensive) item instance requires the same amount of shelf-space and the retailer uses the entire available shelf-space (Q) as per the data stored in the information system. We assume that $r _ { E } > r _ { C } , s _ { E } > s _ { C } , r _ { E } \gg s _ { E } ,$ and $r _ { C } \gg s _ { C } .$ The latter assumptions arise from the observation that if unit revenue is less than unit stockout cost, it's preferable to facilitate the occurrence of more stock-outs than sales.

We use ‘actual’ to represent the reality $- \mathrm { i } . \mathsf { e } .$ , the actual inventory level of items at the store — in the remainder of this paper. We also interchangeably use ‘item’ and ‘product’ to represent an entity instance.

## 3.3. Actual vs. information system record

Shrinkage occurs both at the retail store and in the supply chain even before items reach the store. The latter arise either due to vendor error or theft. Of the items that arrive at the store, a signi<sup>fi</sup>cant number disappear either temporarily (e.g., misplaced inside the store) or permanently (e.g., theft), invariably resulting in lost sales due to their unavailability on the retail store shelf. Since demand for a product is known to be directly related to the number of facings of that item (e.g., [21,23]), any reduction in the number of facings is likely to result in a reduction in demand for that item. The ‘number of facings’ is the number of instances of a given item that are at the edge of the shelves that face the customer. In more general terms, however, the number of facings includes all instances that are on the shelf regardless of their orientation with respect to customers. In addition to direct loss of the item, the retailer also experiences related consequences including lost sale of that as well as complementary items, loss of customer goodwill due to stock-out situations, and ineffective inventory management when erroneous inventory information from the information system is used to make decisions.

Given that demand directly depends on the number of facings (e.g., [16] and the references therein), ticket-switching has different effects on expensive and cheap items. The number of facings and demand for the item determines the replenishment frequency and associated number of items per replenishment cycle. It is not uncommon to use data from the information system as the only source of information for replenishing items on shelves. Therefore, when ticket-switching occurs, the number of facings of the expensive items is less than that which is determined from the information system. Similarly, under ticket-switching conditions, the actual number of facings of the cheap item is more than that from the information system. Since demand is directly related to the number of facings, the expensive item experiences a decrease in demand (vs. what's expected if there are more of this item on the shelf when ticket-switching is absent) and the cheap item experiences an increase in demand (vs. what's expected if ticket-switching is absent and there are fewer of this cheap item on the store shelf). We conclude from such a dynamic that $P ( D _ { E } ^ { T } ) < P ( D _ { E } )$ and $P ( D _ { C } ^ { T } ) > P ( D _ { C } )$ When ticket-switching is absent, $\alpha = 1$

The probability that d out of D customer arrivals are of type i is:

$$
P _ {i} (d | D) = \binom{D}{d} P _ {i} ^ {d} (1 - P _ {i}) ^ {1 - d}.\tag{1}
$$

The next arriving customer observes one of two states: the item is available or the item is unavailable. We now consider these two scenarios from the perspective of actual information as well as information from the information system.

## 3.3.1. Item available

3.3.1.1. Actual data

$$
P _ {C} ^ {I} (n, q _ {C}, q _ {E}) = \rho_ {C} \left(\sum_ {d = 0} ^ {q _ {C} - 1} P _ {C} (d | (n - 1))\right)\tag{2}
$$

$$
P _ {E} ^ {I} (n, q _ {C}, q _ {E}) = \rho_ {E} \left(\sum_ {d = 0} ^ {q _ {E} - 1} P _ {E} (d | (n - 1)) \left[ \alpha - (1 - \alpha) \sum_ {j = q _ {E} - d} ^ {n - d - 1} P _ {E} (j | (n - d - 1)) \right]\right)\tag{3}
$$

where the <sup>fi</sup>rst term represents all cases of realization of primary demand and the second term represents the remaining Es that have not been ticket-switched. We can write the remainder of the probabilities in a similar manner.

3.3.1.2. Information system data

$$
\begin{array}{c} P _ {C} ^ {I} (n, q _ {C}, q _ {E}) = \rho_ {C} \sum_ {d = 0} ^ {q _ {C} - 1} P _ {C} (d | (n - 1)) \\ - \rho_ {E} (1 - \alpha) \sum_ {d = 0} ^ {q _ {E} - 1} P _ {E} (d | (n - 1)) \sum_ {j = q _ {E} - d} ^ {n - d - 1} P _ {E} (j | (n - d - 1)) \end{array}\tag{4}
$$

$$
P _ {E} ^ {I} (n, q _ {C}, q _ {E}) = \alpha \rho_ {E} \left(\sum_ {d = 0} ^ {q _ {E} - 1} P _ {E} (d | (n - 1))\right)\tag{5}
$$

3.3.2. Item out-of-stock

3.3.2.1. Actual data

$$
P _ {E} ^ {O} (n, q _ {C}, q _ {E}) = \rho_ {E} \left[ \sum_ {d = 0} ^ {q _ {E} - 1} P _ {E} (d | (n - 1)) \left((1 - \alpha) \sum_ {j = q _ {E} - d} ^ {n - d - 1} P _ {E} (j | (n - d - 1))\right) + \sum_ {d = q _ {E}} ^ {n - 1} \alpha P _ {E} (d | (n - 1)) \right]\tag{6}
$$

$$
P _ {C} ^ {0} (n, q _ {C}, q _ {E}) = \rho_ {C} \left[ \sum_ {d = q _ {C}} ^ {n - 1} P _ {C} (d | (n - 1)) - \sum_ {d = 0} ^ {q _ {C} - 1} P _ {C} (d | (n - 1)) \left((1 - \alpha) \sum_ {j = q _ {E} - d} ^ {n - d - 1} P _ {E} (j | (n - d - 1))\right) \right].\tag{7}
$$

3.3.2.2. Information system data

$$
P _ {E} ^ {O} (n, q _ {C}, q _ {E}) = \alpha \rho_ {E} \sum_ {d = 0} ^ {n - 1} P _ {E} (d | (n - 1))\tag{8}
$$

$$
\begin{array}{l} P _ {C} ^ {O} (n, q _ {C}, q _ {E}) = \rho_ {C} \sum_ {d = q _ {C}} ^ {n - 1} P _ {C} (d | (n - 1)) \\ \qquad + \alpha \rho_ {E} \sum_ {d = 0} ^ {q _ {E} - 1} P _ {E} (d | (n - 1)) \sum_ {j = q _ {E} - d} ^ {n - d - 1} P _ {E} (j | (n - d - 1)). \end{array}\tag{9}
$$

Based on these probabilities, we now derive results for the considered scenarios.

Lemma 3.1. The probability that an arriving cheap (expensive) item customer finds the item in stock is higher (lower) based on actual inventory than on information system inventory.

Proof. We now provide proof for the cheap item case, and the one for expensive item can be similarly shown using Eqs. (3) and (5).

The result for the cheap item case follows from Eqs. (2) and (4) since

$$
\begin{array}{l} \text {[information\_system]} P _ {C} ^ {I} (n, q _ {C}, q _ {E}) - [ \text {actual} ] P _ {C} ^ {I} (n, q _ {C}, q _ {E}) = \\ - \rho_ {E} (1 - \alpha) \sum_ {d = 0} ^ {q _ {E} - 1} P _ {E} (d | (n - 1)) \sum_ {j = q _ {E} - d} ^ {n - d - 1} P _ {E} (j | (n - d - 1)), \end{array}
$$

which is negative since the probability terms, $\rho _ { E }$ and $( 1 - \alpha )$ are all positive. □

In essence, whereas the information system is not aware of ticketswitching, it is aware of pseudo-demand for cheap items generated due to ticket-switching of the corresponding expensive items. In other words, the cheap item's ‘ticket’ that is used to check-out an expensive item generates its fake demand.

Lemma 3.2. The probability that an arriving expensive (cheap) item customer finds the item out-of-stock is higher (lower) based on actual inventory than on information system inventory.

Proof. We provide proof for the expensive item case, and the one for cheap item can be similarly shown using Eqs. (7) and (9).

The result for the expensive item case follows from Eqs. (6) and (8) since

$$
\begin{array}{l} \text {[information\_system]} P _ {E} ^ {0} (n, q _ {C}, q _ {E}) - [ \text {actual} ] P _ {E} ^ {0} (n, q _ {C}, q _ {E}) = \\ \rho_ {E} \sum_ {d = 0} ^ {q _ {E} - 1} P _ {E} (d | (n - 1)) \left(\alpha - (1 - \alpha) \sum_ {j = q _ {E} - d} ^ {n - d - 1} P _ {E} (j | (n - d - 1))\right) \end{array}
$$

which is negative.

The actual inventory of expensive item is depleted at least as fast as the information system inventory of the expensive item. For the cheap item case, ticket-switching affects (here, lowers) the inventory level of the cheap item in the information system while leaving the actual cheap item inventory untouched.

Several major retailers (e.g., Sears, K-Mart) have online inventory checkers that allow customers to check for the existence of in-store stock of an item of interest. This convenient feature allows customers to decide to go to a B&M (Brick & Mortar) store only if it has the desired item in stock. In addition to the individual store Web sites, there are portals that aggregate information from several retailers. For example, http://checkinventory.home.comcast.net/\~checkinventory/ facilitates inventory checking at Home Depot, Staples, Target, and Wal-Mart. Another such Web site is: http://thedisplayrack.com.

Clearly, there is demand for such information. However, these inventory checkers are useful only when the information they provide are accurate. In a majority of cases, in-stock inventory displayed in these store inventory checkers is generated from the store's inventory database, which may not necessarily re<sup>fl</sup>ect actual in-store inventory status. As per Lemmas 3.1–3.2, the customer can trust in-store inventory information only for cheap items and not for expensive items. Since cheap and expensive are relative terms (e.g., item A is cheaper than item B, which in turn is cheaper than item C; Between B and C, B is the cheap item but between A and B, B is the expensive item), in the presence of ticket-switching incidents, in-store inventory information of only the cheapest items can be guaranteed to be true. On the other hand, in-store inventory information for the most expensive items cannot be guaranteed. The in-store inventory information for the ‘middle’ (i.e., those that are priced higher than the cheap items, and lower than the expensive items carried at a given retail store) priced items can be trusted more than that of the expensive items and less than that of the cheap items.

We now consider the expected bene<sup>fi</sup>t of stocking $q _ { C }$ and $q _ { E }$ respectively of cheap and expensive items under various scenarios.

3.4. Effect of ticket-switching on benefit

The expected bene<sup>fi</sup>t of the $n ^ { t h }$ customer is:

$$
\begin{array}{l} B (n, q _ {C}, q _ {E}) = r _ {C} P _ {C} ^ {I} (n, q _ {C}, q _ {E}) \\ \qquad + r _ {E} P _ {E} ^ {I} (n, q _ {C}, q _ {E}) - s _ {C} P _ {C} ^ {O} (n, q _ {C}, q _ {E}) - s _ {E} P _ {E} ^ {O} (n, q _ {C}, q _ {E}). \end{array}\tag{10}
$$

The expected bene<sup>fi</sup>t of stocking $q _ { C }$ and $q _ { E }$ units of the two products

$$
B (q _ {C}, q _ {E}) = \sum_ {D = 1} ^ {D = \infty} \left(P (D) \sum_ {n = 1} ^ {D} B (n, q _ {C}, q _ {E})\right).\tag{11}
$$

Shelf space is then allocated to these two products by maximizing the expected pro<sup>fi</sup>t.

$$
\Pi (q _ {C}, q _ {E}) = B (q _ {C}, q _ {E}) - c _ {C} q _ {C} - c _ {E} q _ {E}\tag{12}
$$

Eq. (12) can be written in terms of either q or q since for a given $Q _ { ☉ }$ $Q = q _ { C } + q _ { E }$ so that the maximum expected pro<sup>fi</sup>t can be computed by <sup>fi</sup>xing either q<sub>C</sub> or q<sub>E</sub> and then maximizing the function in Eq. (12) with respect to the other (respectively, q<sub>E</sub> or q<sub>C</sub>).

Theorem 3.3. When ticket-switching is present, the expected benefit estimates based on information system generated information is deflated (vs. reality).

Proof. From Eq. (11) and Lemmas (3.1–3.2), the difference in expected bene<sup>fi</sup>t estimated through information system and actual inventory information of stocking $q _ { C }$ and $q _ { E }$ units of the two products is:

$$
\begin{array}{c} [ \text {information\_system} ] B ^ {T} (q _ {C}, q _ {E}) - [ \text {actual} ] B ^ {T} (q _ {C}, q _ {E}) = \\ \sum_ {D = 1} ^ {D = \infty} \left[ P \Big (D ^ {T} \Big) \sum_ {n = 1} ^ {D ^ {T}} \left(- \rho_ {C} \sum_ {d = 0} ^ {q _ {C} - 1} P _ {C} (d | (n - 1)) \left(\sum_ {j = q _ {E} - d} ^ {n - d - 1} P _ {E} (j | (n - d - 1))\right) + \right. \right. \\ ((1 - \alpha) (r _ {E} - r _ {C} + s _ {E}) - \alpha (s _ {C} + s _ {E})) \rho_ {E} \sum_ {d = 0} ^ {q _ {E} - 1} P _ {E} (d | (n - 1)) \left. \sum_ {j = q _ {E} - d} ^ {n - d - 1} P _ {E} (j | (n - d - 1))\right) \Bigg ]. \end{array}
$$

Since this difference is negative, the result follows.

A majority of existing inventory management systems depend solely on information generated by their information systems. Any deviation of stored values in the information system from reality is, therefore, a cause for concern. The policy implication of Theorem 3.3 is that care should be taken when expected bene<sup>fi</sup>t is computed based on (possibly incorrect) data from the information system. Theorem 3.3 states that in the presence of ticket-switching, estimated (de<sup>fl</sup>ated) bene<sup>fi</sup>t based on information system generated information must be appropriately in-<sup>fl</sup>ated to account for the difference.

We now consider the effect of ticket-switching on the bene<sup>fi</sup>t of expensive and cheap items together as well as individually vs. the case where no ticket-switching occurs $( \mathrm { i } . \mathsf { e } . , \alpha = 0 )$ . We consider the use of information system data for both the cases.

Theorem 3.4. When ticket-switching is present, the expected benefit estimates based on information system generated information is deflated (vs. when ticket-switching is absent).

Proof. From Eqs. (4), (5), (8), and (9), the difference in expected bene-<sup>fi</sup>t estimated through information system inventory information of stocking $q _ { C }$ and q units of the two products when ticket-switching is present and absent is:

$$
\begin{array}{c}\text {[information\_system]} B ^ {T} (q _ {C}, q _ {E}) - \text {[information\_system]} B (q _ {C}, q _ {E}) =\\\sum_ {D = 1} ^ {D = \infty} \left[ P \Big (D ^ {T} \Big) \sum_ {n = 1} ^ {D ^ {T}} \left((r _ {C} + s _ {C}) (1 - \alpha) \rho_ {E} \sum_ {d = 0} ^ {q _ {E} - 1} P _ {E} (d | (n - 1)) \sum_ {j = q _ {E} - d} ^ {n - d - 1} P _ {E} (j | (n - d - 1)) + \right. \right.\\\left.\left. (1 - \alpha) \rho_ {E} \sum_ {d = 0} ^ {q _ {E} - 1} P _ {E} (d | (n - 1)) \left[ s _ {E} \sum_ {d = q _ {E}} ^ {n - 1} P _ {E} (d | (n - 1)) - r _ {E} \right]\right)\right)\left. \right],\end{array}
$$

which is negative.

When computing the difference, we implicitly considered the differential effect of demand increase or decrease with an increase or decrease, respectively, in the number of facings. Theorem 3.4 states that data from the information system under-estimates the bene<sup>fi</sup>t when ticket-switching is present. Theorems 3.3 & 3.4, when considered together, tell us that the data from the information system underestimates the bene<sup>fi</sup>t when ticket-switching is present vs. both data from the same information system when ticket-switching is absent as well as actual data.

We now consider the expensive and cheap item cases separately.

Lemma 3.5. When ticket-switching is present, the expected benefit estimates for the expensive item based on information system generated information is deflated (vs. when ticket-switching is absent).

Proof. For the $n ^ { t h }$ customer, from Eqs. (5) and (8)

$$
\begin{array}{c} [ \text {information\_system} ] B _ {E} ^ {T} (q _ {C}, q _ {E}) - [ \text {information\_system} ] B _ {E} (q _ {C}, q _ {E}) = \\ \sum_ {D = 1} ^ {D = \infty} \left[ P \Big (D ^ {T} \Big) \sum_ {n = 1} ^ {D ^ {T}} \left((1 - \alpha) s _ {E} \rho_ {E} \sum_ {d = 0} ^ {n - 1} P _ {E} (d | (n - 1)) - (1 - \alpha) r _ {E} \rho_ {E} \sum_ {d = 0} ^ {q _ {E} - 1} P _ {E} (d | (n - 1))\right) \right] \\ = \sum_ {D = 1} ^ {D = \infty} \left[ P \Big (D ^ {T} \Big) \sum_ {n = 1} ^ {D ^ {T}} \left((1 - \alpha) \rho_ {E} \sum_ {d = 0} ^ {q _ {E} - 1} P _ {E} (d | (n - 1)) \left[ s _ {E} \sum_ {d = q _ {E}} ^ {n - 1} P _ {E} (d | (n - 1)) - r _ {E} \right]\right) \right], \end{array}
$$

which is negative since the term in the square bracket is negative. □

Similar to Theorem 3.4 where both expensive and cheap items are simultaneously considered, the dynamic is the same for just the expensive item as shown in Lemma 3.5. We now consider the same scenario but for only the cheap item.

Lemma 3.6. When ticket-switching is present, the expected benefit estimates for the cheap item based on information system generated information is deflated (vs. when ticket-switching is absent).

Proof. For the $n ^ { t h }$ customer, from Eqs. (4) and (9)

$$
\begin{array}{c} \text {[information\_system]} B _ {C} ^ {T} (q _ {C}, q _ {E}) - \text {[information\_system]} B _ {C} (q _ {C}, q _ {E}) = \\ \sum_ {D = 1} ^ {D = \infty} \left[ P \Big (D ^ {T} \Big) \sum_ {n = 1} ^ {D ^ {T}} \left((1 - \alpha) (s _ {C} - r _ {C}) \rho_ {E} \sum_ {d = 0} ^ {q _ {E} - 1} P _ {E} (d | (n - 1)) \left(\sum_ {j = q _ {E} - d} ^ {n - d - 1} P _ {E} (j | (n - d - 1))\right)\right) \right], \end{array}
$$

which is negative since $\left( s _ { C } - r _ { C } \right)$ is negative.

Like Lemma 3.5, the implication of Lemma 3.6 is that for cheap items, using information from the information system, the result when ticketswitching occurs is under-estimated. This is similar to the result when only the expensive item is considered as well as when both cheap and expensive items are simultaneously considered.

The policy implication based on the discussion in this sub-section is that when ticket-switching is present, the expected bene<sup>fi</sup>t estimates using information system generated information is de<sup>fl</sup>ated for all possible combinations (i.e., only cheap, only expensive, both cheap and expensive) of items. When both items are considered, the expected bene<sup>fi</sup>t estimation based on information system (vs. actual inventory) data may be used as a readily available lower bound for estimated bene<sup>fi</sup>ts. Although such lower bounds may in fact turn out to be rather conservative, it is better to use this information for its intended purpose when there is reason to believe that ticket-switching incidents are present.

## 4. Implications for shelf-space allocation

We use a similar setup as in [7] and consider the effect of a ticketswitching incident.

Theorem 4.1. In the presence of ticket-switching, based on data from the information system, the rate of profit increase increases with respect to the number of expensive items.

Proof. When ticket-switching occurs, the information system registers one less unit of the cheap item with no change to the number of expensive items. We operationalize the proof by considering one less unit of the cheap item $( q _ { C \mathrm { ~ + ~ } 1 }  q _ { C } )$ and the same number of units of the expensive item $( q _ { E }  q _ { E } )$ . Let $p _ { i } ( i = 1 . . 4 )$ represent the probability of the four possible cases for this scenario. Table 1 lists the four possible cases that arise when one unit of the cheap item (C) is removed while keeping the number of expensive items (E) the same.

Table 1 [Information system inventory data] impact of ticket-switching.

<table><tr><td rowspan="2">One less unit of C</td><td colspan="2">Same number of E</td></tr><tr><td>Not sold</td><td>Sold</td></tr><tr><td>Not sold</td><td> $case_{1}^{IS}$ </td><td> $case_{2}^{IS}$ </td></tr><tr><td>Sold</td><td> $case_{3}^{IS}$ </td><td> $case_{4}^{IS}$ </td></tr></table>

The expected impact on pro<sup>fi</sup>t is:

$$
\begin{array}{c} \Pi (q _ {E} + 1) - \Pi (q _ {E}) = - p _ {1} (c _ {E} - c _ {C}) + p _ {2} (r _ {E} + s _ {E}) - p _ {2} (c _ {E} - c _ {C}) \\ \qquad \qquad \qquad - p _ {3} (r _ {C} + s _ {C}) - p _ {3} (c _ {E} - c _ {C}) + p _ {4} (r _ {E} + s _ {E}) \\ \qquad \qquad \qquad - p _ {4} (r _ {C} + s _ {C}) - p _ {4} (c _ {E} - c _ {C}), \end{array}
$$

which simpli<sup>fi</sup>es to:

$$
\begin{array}{c} \Pi (q _ {E} + 1) - \Pi (q _ {E}) = (p _ {1} + p _ {2}) (r _ {C} + s _ {C}) - (p _ {1} + p _ {3}) (r _ {E} + s _ {E}) \\ \qquad + (r _ {E} + s _ {E} - r _ {C} - s _ {C} - c _ {E} + c _ {C}). \end{array}\tag{13}
$$

The last term in Eq. (13) is a positive constant. We need to show that as $q _ { E }$ increases, $\mathbf { \beta } ( \mathsf { a } ) \left( p _ { 1 } + p _ { 2 } \right)$ is non-decreasing and $\left( \boldsymbol { \mathsf { b } } \right) \left( p _ { 1 } + p _ { 3 } \right)$ decreases. For cas $\mathfrak { z } _ { 1 } ^ { I S } , p _ { 1 } = p ( D _ { E } \le q _ { E } \& D _ { C } < q _ { C } + 1 )$ and for case<sup>IS</sup>, $p _ { 2 } =$ $p ( D _ { E } \geq q _ { E } \& D _ { C } < q _ { C } + 1 )$ . Similarly, for case<sub>3</sub><sup>IS</sup>, $p _ { 3 } = p ( D _ { E } \leq q _ { E } \ \&$ $D _ { C } \geq q _ { C } )$ and for $\mathopen : \mathrm { a s e } _ { 4 } ^ { I S } , p _ { 4 } \mathopen = p ( D _ { E } \mathclose | q _ { E } \& D _ { C } \mathclose | q _ { C } )$ . Since $D _ { E } < q _ { E }$ is unique to $p _ { 1 } + p _ { 3 }$ and $D _ { E } = q _ { E }$ is shared among the different cases, an increase in q would essentially decrease $p _ { 1 } + p _ { 3 }$ . However, $p _ { 1 } + p _ { 2 }$ is unaffected by an increase in $q _ { E } .$ □

Theorem 4.2. In the presence of ticket-switching, based on data from the information system, the rate of profit increase decreases with respect to the number of cheap items.

Proof. The proof for this follows a similar logic as in Theorem 4.1. □

Although the rate of pro<sup>fi</sup>t increases in both the cases considered in Theorems 4.1 & 4.2, the effect is more pronounced with expensive items since the information system does not register ticket-switching incidents from the expensive item's perspective. The policy implication of Theorems 4.1 & 4.2 is that when ticket-switching is present, when only the data from the information system is used to make decisions, it is better to increase the number of expensive items.

We now consider the case where the actual data (vs. that from the information system) is considered.

Theorem 4.3. In the presence of ticket-switching, based on actual data, the rate of profit increase decreases with respect to the number of expensive items.

Proof. When ticket-switching occurs, there is one less unit of the expensive item $( q _ { E \mathrm { ~ + ~ } 1 }  q _ { E } )$ with no change to the number of cheap items $( q _ { C } \to q _ { C } )$ in reality. We therefore consider the addition of one less unit of the expensive item and the same number of units of the cheap item. Table 2 lists the four possible cases that arise when one less unit of the expensive item (E) and the same number of cheap items (C) are present after ticket-switching.

The expected impact on pro<sup>fi</sup>t is the same as that given in Eq. (13). We need to show that as $q _ { E }$ increases, $\left( \mathsf { a } \right) \left( p _ { 1 } + p _ { 2 } \right)$ is non-decreasing and $\left( \boldsymbol { \mathsf { b } } \right) \left( p _ { 1 } + p _ { 3 } \right)$ increases. For case $\mathbb { 1 } , p _ { 1 } = p ( D _ { E } \leq q _ { E } \& D _ { C } \leq q _ { C } )$ and for case<sub>2</sub><sup>A</sup>, $p _ { 2 } = p ( D _ { E } > q _ { E } \& D _ { C } \leq q _ { C } )$ . Similarly, for case<sup>A</sup>, $p _ { 3 } =$ $p ( D _ { E } \leq q _ { E } \& D _ { C } > q _ { C } )$ and for case $^ 4 _ { 4 } , p _ { 4 } = p ( D _ { E } > q _ { E } \& D _ { C } > q _ { C } )$ . Here, $p _ { 1 } + p _ { 2 }$ is unaffected by an increase in $q _ { E } .$ Since $D _ { E } \leq q _ { E }$ is speci<sup>fi</sup>c to $p _ { 1 } + p _ { 3 } ,$ an increase in $q _ { E }$ would essentially increase $p _ { 1 } + p _ { 3 } .$ □

Table 2 [Actual inventory data] impact of ticket-switching.

<table><tr><td rowspan="2">Same number of C</td><td colspan="2">One less unit of E</td></tr><tr><td>Not sold</td><td>Sold</td></tr><tr><td>Not sold</td><td> $case_{1}^{A}$ </td><td> $case_{2}^{A}$ </td></tr><tr><td>Sold</td><td> $case_{3}^{A}$ </td><td> $case_{4}^{A}$ </td></tr></table>

Theorem 4.4. In the presence of ticket-switching, based on actual data, the rate of profit increase increases with respect to the number of cheap items.

Proof. The proof for this follows a similar logic as in Theorem 4.3. □

Similar to the cases considered in Theorems 4.1 & 4.2, the rate of pro<sup>fi</sup>t increases in both the cases considered in Theorems 4.3 & 4.4 when decisions are made using just the actual (vs. information system) data. Unlike the case with information system data, the rate of pro<sup>fi</sup>t increase decreases with respect to the number of expensive items in the presence of ticket-switching incidents. The policy implication of Theorems 4.3 & 4.4 is that when ticket-switching is present, when only the actual data is used to make decisions, it is better to increase the number of cheap items. This is somewhat nonintuitive and stems from the fact that the existence of more number of the expensive item allows for the possibility of ticket-switching incidents to occur. Since, in reality, ticket-switching incidents show an increase in the number of cheap items sold, this result follows.

We now consider the stocking level of the expensive item.

Corollary 4.5. In the presence of ticket-switching, the optimal stocking level of the expensive item weakly increases with:

a. the unit revenue of the expensive item

b. the stock-out cost of the expensive item

c. the unit cost of the cheap item.

Proof. This follows from the four possible cases considered in Theorem 4.1 and Eq. (13). Rearranging terms in Eq. (13), we get:

$$
\begin{array}{c} \Pi (q _ {E} + 1) - \Pi (q _ {E}) = (\mathbf {p _ {2}} + \mathbf {p _ {3}}) \mathbf {r _ {E}} + (\mathbf {p _ {2}} + \mathbf {p _ {4}}) \mathbf {s _ {E}} \\ + \mathbf {c _ {C}} - c _ {E} - (p _ {3} + p _ {4}) r _ {C} - (p _ {3} + p _ {4}) s _ {c}. \end{array}\tag{14}
$$

The positive terms support the observation.

Corollary 4.6. In the presence of ticket-switching, the optimal stocking level of the expensive item weakly decreases with:

a. the unit cost of the expensive item

b. the unit revenue of the cheap item

c. the stock-out cost of the cheap item.

Proof. This follows from the proof presented in Corollary 4.5. The negative terms in Eq. (14) support this observation. □

Everything else being the same, together Corollary 4.5 and Corollary 4.6 show that more shelf-space should be allocated to the expensive item with a relative (vs. that of the cheap item) increase in the unit revenue and stock-out cost. Similarly, shelf-space allocated to the expensive item should be decreased with an increase in the difference in unit cost of cheap and expensive items.

## 5. Discussion

Shrinkage is a common occurrence and is a signi<sup>fi</sup>cant concern for inventory management as well as to maintain pro<sup>fi</sup>t in retail stores. Among various forms of shrinkage, ticket-switching has not received its fair share of attention in the academic research literature although it is widely discussed by practitioners and in retailing-related trade publications. While an isolated ticket-switching incident may not necessarily cause a tangible disruption, the aggregate or cumulative effect of several ticket-switching incidents is a complex phenomenon. This creates inaccuracies in the information system, which oftentimes is the store's only decision-making information source. Such inaccuracies have the potential to cause inef<sup>fi</sup>ciencies in a store's inventory management and replenishment processes as well as generate stock-out situations.

We attempted to <sup>fi</sup>ll the gap in published research literature by considering some of the dynamics of ticket-switching as related to inventory management. Speci<sup>fi</sup>cally, we considered (a) the accuracy of inventory information from the information system vs. reality (i.e., actual in-store inventory) when ticket-switching is present, (b) the presence/absence of ticket-switching incidents and related effects on expected bene<sup>fi</sup>t computations, (c) the number of facings and their effect on demand forecasts, and (d) shelf-space allocation in the presence of ticket-switching incidents at a store that stocks two types of items — one cheap and the other an expensive item. To account for reality in such retail settings, we considered data stored in the store's inventory system as well as the actual inventory data.

In principle, although the actual in-store inventory data and inventory data stored in the information system must be the same at all times, this is generally an exception rather than a rule. The data in the information system are generally updated upon order arrival as well as in response to sales events. While absolutely necessary, it is uncommon for shrinkage events to trigger a concomitant update in the information system. Since this divergence over time of actual inventory data and data stored in the information system is a known phenomenon, retail stores attempt to reconcile the difference by taking manual inventory of the entire store. However, the frequency of such manual inventorytaking in a majority of stores leaves much to be desired. As item-level RFID tags are slowly introduced in retail stores (e.g., American Apparel, Trasluz, Macy's, Kohl's), (a) there is a precipitous drop in the difference between actual vs. information system inventory information when inventory is taken every day and (b) the shrinkage-deterrence capability of item-level RFID tags does seem to have an appreciable effect, based on anecdotal evidence from large retailers.

While technologies (e.g., item-level RFID) exist for complete realtime inventory visibility [24], retailers have been rather reluctant/slow in their adoption. Even when RFID adoption decisions are made, they are limited to a select few items (e.g., Wrangler jeans at Wal-Mart, Levis jeans at Kohl's, shoes at Macy's) that are only inventoried a few times per day at best, although there are exceptions (e.g., American Apparel, Trasluz). We believe that there is an urgent need to study the differential effects of actual vs. information system data — especially in the presence/absence of ticket-switching. This is highlighted by the fact that although retailers have been aware of ticket-switching as a phenomenon for a long time, these incidents are rather dif<sup>fi</sup>cult to control in large retail environments.

Our <sup>fi</sup>ndings shed light on several facets of ticket-switching dynamics. For example, under ticket-switching conditions, the probability that a customer with the intention to purchase the expensive item <sup>fi</sup>nds this item to be in-stock based on data from the information system is higher than that based on actual data. On the other hand, the probability is higher for a customer intending to purchase the cheap item to <sup>fi</sup>nd this item to be in-stock based on actual data than data from the information system. Ultimately, the actual data is all that matters. The policy implication is that when using inventory information provided online by some retail stores (e.g., Target stores), it pays for the customer to check this information before going to the store only if this is the cheap item and not the expensive item. The data generated by the information system under-estimates reality for the cheap item and over-estimates that for the expensive item. Therefore, when a customer's online search for a cheap item (at, for example, target.com) reveals that the item is in-stock. it is almost certainly in stock at the store. However, for the expensive item, if the online search reveals that the item is in stock, it may well be likely that the store does not have the item in stock. These policy implications can be incorporated in a knowledge-based system that's used for decision support in these environments, to facilitate both the retailer and the customer who make informed decisions. For example, the retailers who generate and display instantaneous inventory information through online inventory checkers could provide some variant of probability information (e.g., there is a 62% probability that this item is in stock at Store-A) to enable the customers to make their decisions. Although the placement of disclaimers as to the verity of this information is appropriate, customers who repeatedly experience stock-outs of items that were claimed to be in stock (by inventory checker systems) may be dissuaded from such systems and may consider other stores for their purchase decisions.

From the store's perspective, an overwhelming majority take complete inventory only a few (generally, one or two) times a year. After manual inventory check, retail stores generally reconcile differences so that both the actual inventory and that in the information system are in sync. Between manual inventory checks, this difference only diverges with time, as various forms of shrinkage (e.g., broken items, misplaced items, process errors, spoilage, theft, ticket-switching, unsalables) seep in. Since bene<sup>fi</sup>t estimates are conducted more frequently than complete store inventory checks, most stores resort to the use of information available in the information system for lack of a better alternative. However, the use of incorrect information has its consequence — in this case, the resulting estimates may not necessarily be valid. With ticket-switching as the only source of shrinkage, our analysis provides expressions for differences in computed estimates. Under ticketswitching conditions, results from this study indicate that the retail store is expected to <sup>fi</sup>nd de<sup>fl</sup>ated bene<sup>fi</sup>t estimates with the use of data from its information system rather than reality. Moreover, when using only data from the information system, the bene<sup>fi</sup>t estimate when ticket-switching is present is de<sup>fl</sup>ated than otherwise. This result holds for both expensive and cheap items when individually considered. Note that the results on de<sup>fl</sup>ated/in<sup>fl</sup>ated forecasts under ticketswitching are in part due to demand forecasts that depend on the number of facings, and not just on the sales recorded in the information system. In the presence of ticket-switching, when using data from the information system to compute bene<sup>fi</sup>t estimates, care should be taken to account for the de<sup>fl</sup>ation in the estimated results. A policy implication of this result to the retail store is that although revenue forecast estimates may not necessarily be accurate in the presence of ticket-switching incidents, these estimates are guaranteed to not be in<sup>fl</sup>ated. In other words, such bene<sup>fi</sup>t estimates can be used as a lower bound for accurate bene<sup>fi</sup>t estimates.

As for shelf-space allocation in the presence of ticket-switching, when only the information system data is used to make (e.g, replenishment) decisions, it is better to appropriately increase the number of expensive items. In the presence of ticket-switching incidents, since the expensive items are ‘purchased’ without the knowledge of the information system, the likelihood of in-store stock-outs of the expensive items is increased due to the fact that most order placements are based on information generated through the information system. Since these items generally tend to have higher pro<sup>fi</sup>t margins and higher stock-out costs, it is safer to have an appropriately large safety buffer of these items. The complement is true for the cheap items, which may start accumulating over time since the ticket-switched ‘purchased’ cheap items trigger associated replacements in the form of new order placements. Our results indicate that more shelf-space should be allocated to the expensive item that has relatively more unit revenue and stock-out cost to prevent stock-outs and to prevent associated customer satisfaction issues. Our results also indicate that the proportion of expensive item should be decreased as the difference between the unit cost of cheap and expensive item converges. As the unit cost of expensive and cheap item converges, the impact generated by ticketswitching is muted to a certain extent and the concomitant need to compensate with an increase in the number of expensive item on the store shelf decreases.

We considered a few different facets of ticket-switching dynamics in this paper. Given the non-existence of published results on ticketswitching in extant literature, several interesting questions still remain. For example, although it is known that the number of facings by itself generates demand, we did not explicitly consider its dynamic in detail under ticket-switching conditions. We implicitly considered endogenous demand through appropriate probability inequalities, and have partially modeled related dynamics by considering the basic interdependencies between ticket-switching, facings, and demand forecasts. Our rationale for this is that since the ‘expensive’ item is the prime entity, fewer facings of this item would result in its decreased demand, which does not directly affect ticket-switching behavior. A related issue is, when ticket-switching is known to exist, to determine the optimal point at which reality and data in the information system must be reconciled. Moreover, among the expensive items, ticket-switching most likely affects the fast moving expensive items (e.g., the ‘A’ class items in ABC analysis [22]). Therefore, those expensive items that are not ‘fast moving’ may remain unaffected by ticket-switching incidents. We consider these in another study.

Under ticket-switching conditions, a missing (expensive) item that is not deemed to be missing by the store's information system results in loss of sale of that (or its replacement) item until inventory data is reconciled with reality. We consider this in another study.

## Acknowledgments

We are grateful to the two reviewers for providing an extensive set of constructive comments that have helped improve the content and presentation of this paper.

## References

[1] P. Abell, B. Ream, Reaping pro<sup>fi</sup>t through loss prevention technology, AMR Research report2001.

[2] Atlanta Journal Constitution, http://www.ajc.com/news/news/4-charged-in-homedepot-ticket-switching-scheme/nfjDP/.

[3] R. Bobbit, J. Connell, N. Haas, C. Otto, S. Pankanti, J. Payne, Visual item veri<sup>fi</sup>cation for fraud prevention in retail self-checkout, IEEE Workshop on Applications of Computer Vision (WACV), 2011, pp. 585–590.

[4] J. Connell, Q. Fan, P. Gabbur, N. Haas, S. Pankanti, H. Trinh, Retail video analytics: an overview and survey, Proceedings of the SPIE Video Surveillance and Transportation Imaging Applications, 2013, p. 8663.

[5] R.L. DiLonardo, The economic bene<sup>fi</sup>t of electronic article surveillance, in: R.V. Clarke (Ed.) Situational Crime Prevention: Successful Case Studies 2 Harrow and Heston Guilderland NY.1997 pp. 122-131

[6] R.L. DiLonardo, R.V. Clarke, Reducing the rewards of shoplifting: an evaluation of ink tags, Security Journal 7 (1) (1996) 11–14.

[7] W.G. Gilland, H.S. Heese, Sequence matters: shelf-space allocation under dynamic customer-driven substitution, Production and Operations Management 22 (4) (2013) 875-887

[8] L. Hand, EAS study: shrinkage reduced with minimal cost, White Paper, Tyco/IDC Retail Insights #GRI2415332013. (June)

[9] P. Hansen, H. Heinsbroek, Product selection and space allocation in supermarkets, European Journal of Operational Research 3 (6) (1979) 474–484 (November).

[10] T.L. Johns, M.J. Scicchitano, Research by retailers: understanding loss and the effectiveness of loss prevention strategies, Security Journal 19 (2006) 216–227

[11] Y. Kang, S. Gershwin, Information inaccuracy in inventory systems: stock loss and stockout, IIE Transactions 37 (2005) 843–859.

[12] S. Mauw, S. Piramuthu, A PUF-based authentication protocol to address ticketswitching of RFID-tagged items, Proceedings of the 8th International Workshop on Security and Trust Management (STM), Springer LNCS2012.

[13] R. McMillan, Tech. Exec. Built Stolen ‘Legoland’ in \$2M Home, Wired2012. (25 May).

[14] D. Papakiriakopoulos, K. Pramatari, G. Doukidis, A decision support system for detecting products missing from the shelf based on heuristic rules, Decision Support Systems 46 (3) (2009) 685–694.

[15] S. Piramuthu, P. Farahani, M. Grunow, RFID-generated traceability for contaminated product recall in perishable food supply networks, European Journal of Operational Research 225 (2) (2013) 253–262.

[16] S. Piramuthu, W. Zhou, RFID and perishable inventory management with shelfspace and freshness dependent demand, International Journal of Production Economics 144 (2013) 635–640.

[17] S. Piramuthu, S. Wochner, M. Grunow, Should retail stores also RFID-tag ‘cheap items? European Journal of Operational Research 233 (1) (2014) 281–291.

[18] E. Schuman, Wal-Mart stung in \$1.5 million bar-code scam, eWeek2005. (January 5).

[19] J. Shapland, Preventing retail-sector crimes, in: M. Tonry, D. Farrington (Eds.), Building a Safer Society: Strategic Approaches to Crime Prevention, Crime and Justice, vol 19, University of Chicago Press1995.

[20] Agence France Press, http://www.intothewine.fr/tags/trelissac-vin 2011.

[21] T. Urban, Inventory models with inventory-level-dependent demand: a comprehensive review and unifying theory, European Journal of Operational Research 162 (2005) 792-804

[22] T. Vollmann, Manufacturing Planning and Control Systems for Supply Chain Management, McGraw-Hill Professional, 2005.

[23] H.B. Wolfe, A model for control of style merchandise, Industrial Management Review 9 (2) (1968) 69–82.

[24] W. Zhou, RFID and item-level information visibility, European Journal of Operational Research 198 (1) (2009) 252–258

[25] W. Zhou, Y.-J. Tu, S. Piramuthu, RFID-enabled item-level retail pricing, Decision Support Systems 48 (1) (2009) 169–179.

[26] W. Zhou, S. Piramuthu, Preventing ticket-switching of RFID-tagged items in apparel retail stores, Decision Support Systems 55 (3) (2013) 802–810 (June).

[27] A. Zimmerman, As shoplifters use high-tech scams, retail losses rise, Wall Street Journal 25 (2006) A1 (October).

Wei Zhou is an Associate Professor of Information Systems at ESCP-Europe in Paris and a member of the RFID European Lab in Paris. He received his Ph.D. in Information Systems from the University of Florida. His research interests include RFID-enabled item-level information visibility, Internet advertising, and knowledge-based learning systems. His work has appeared in Decision Support Systems, European Journal of Information Systems, European Journal of Operational Research, IEEE Transactions on Geosciences and Remote Sensing, International Journal of Electronic Commerce, and Optical Engineering.

Selwyn Piramuthu is Professor of Information Systems at the University of Florida and a member of the RFID European Lab in Paris. His interests include RFID/IoT systems, data analytics, and recommender systems
