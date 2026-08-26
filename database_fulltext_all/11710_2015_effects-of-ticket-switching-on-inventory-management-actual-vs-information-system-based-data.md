---
otero_id: 11710
otero_key: "EFVKBD7B"
title: "Effects of ticket-switching on inventory management: Actual vs. information system-based data"
authors: "Wei Zhou; Selwyn Piramuthu"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.05.010"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Effects of ticket-switching on inventory management: Actual vs. information system-based data

Wei Zhou <sup>a,c</sup>, Selwyn Piramuthu <sup>b,c,</sup>⁎

<sup>a</sup> Information & Operations Management, ESCP Europe, Paris, France

<sup>b</sup> Information Systems and Operations Management, University of FL, USA

<sup>c</sup> RFID European Lab, Paris, France

## a r t i c l e i n f o

Article history: Received 2 December 2014 Received in revised form 19 March 2015 Accepted 12 May 2015 Available online 21 May 2015

Keywords: Ticket-switching Retail store Information system-based inventory Actual inventory

## a b s t r a c t

Inventory inaccuracies in retail stores result from a combination of controllable and uncontrollable factors such as theft, damage, spoilage, misplacement, process errors, ticket-switching, among others. While most shrinkage types affect only one (type of) item, ticket-switching simultaneously affects the inventory of multiple items. Ticket-switching is the process of switching the identifier or ticket of an expensive item with that from a (relatively) cheap item with the explicit intent of purchasing the expensive item by paying the cheap item's price. Ticket-switching incidents distort inventory records in store information systems. Inventory management decisions based on such data from store information systems are therefore sub-optimal. We study the effects of ticket-switching on optimal order quantity of the involved items and the resulting profit. Under uniformly distributed demand and yield conditions, we find that ticket-switching increases (decreases) the optimal order quantity of the expensive (cheap) items. Surprisingly, results from our analysis indicate that profit on expensive (cheap) items is higher (lower) in the presence of ticket-switching behavior than otherwise.

© 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

Global Retail Theft Barometer surveyed 1187 retailers in 43 countries world-wide and found that retail shrinkage in 2011 cost the industry an estimated US\$ 119 billion, which is about 1.45% of overall sales. The highest proportion of shrinkage were reported by retail categories that include apparel, health/beauty and DIY. This should not be dismissed as an insignificant proportion based purely in terms of the absolute percentage, since even a 2 to 3% sales loss can amount to about 25% loss in profit in this industry with tight profit margins (e.g., [21]). Moreover, reduction due to shrinkage from 2% to 1% is tantamount to about 40% increase in sales (e.g., [1,5]).

The increased use of EAS (Electronic Article Surveillance) over the years has reduced the occurrence of shrinkage in retail store settings [6,9]. A general consequence of a shrinkage event is the loss or disappearance of items. While the source of shrinkage can take many forms such as damage, misplacement (e.g., [17]), process error, shop-lifting (e.g., [7]), spoilage (e.g., [18]), theft (e.g., [9]) and ticket-switching [25, 26], the loss per shrinkage incident depends on the number and type of items involved, the short-term demand for such items and their substitutes, the temporal aspect of that item (e.g., fashion apparel, perishables), and the complexity of the item's replenishment process. Regardless, while a majority of shrinkage incidents affect only one (type of) item (e.g., a pair of jeans), some simultaneously involve multiple items per incident. Ticket-switching is one such type of shrinkage.

Ticket-switching is the process of switching the ticket or item identifier on an expensive item with that from a (relatively) cheap item with the explicit intention of ‘purchasing’ the expensive item but paying only the cheap item's price [14,25]. A ticket-switching incident manifests different impacts on actual in-store inventory and the retail store's inventory information system. From an actual inventory perspective, the store is out of the expensive item but receives a smaller (i.e., price of the cheap item) payment in return. From the store information system's perspective, the customer purchased a cheap item by paying its price. While this may not seem like a major loss for the store since the store only lost the price difference between the expensive and the cheap item, the overall loss to the store due to such incidents is indeed significant. This significance is a direct consequence of information disparity between actual inventory and that in the retail store information system. Since retail stores generally place replenishment orders based on remaining inventory from the perspective of their information systems, any disparity in such information could have deleterious consequences. For example, since ticket-switching of the expensive item is invisible to the store information system, this could ultimately result in the store bearing witness to stock-out situations (e.g., [16]) of the expensive item and excessive inventory and related inventory cost of the cheap item. When the cheap item is a perishable, excessive inventory of perishables that are invisible to the store information system has the potential to precipitate in unnecessary waste due to spoilage.

While there is no dearth of publicly available statistics related to shrinkage in general, it is difficult to determine specific percentage values for individual types of shrinkage. The availability of ticketswitching statistics is even rarer due to its very nature (of simultaneously affecting the actual and information system inventory levels of multiple items) and the existence of other types of shrinkage mechanisms. To add to this complexity of distinguishing different types of incidents that comprise overall shrinkage, ticket-switching events are vulnerable to misinterpretation as other types of shrinkage. For example, a ticket-switching incident can be misconstrued as the combination of a (price or identifier) tag detachment incident for the cheap item, loss (e.g., theft or misplacement) of an expensive item and sale of an imaginary cheap item. Regardless, theft accounts for the largest proportion of shrinkage in a majority of cases, and it is reasonable to assume that ticket-switching is significant even if it's a small fraction of the overall theft statistic.

Ticket-switching is not an unknown phenomenon in retail store environments. Retailers have been aware of its existence for a long time. Clearly, given a choice, retailers would prefer to prevent rather than to deal with the deleterious consequences of ticket-switching. While some retailers take additional and targeted precautions to guard specifically against ticket-switching and its variants (e.g., ensure that both the shoes and the shoe box do indeed belong together during check-out), resource constraints severely prevent complete elimination of ticketswitching incidents. For example, while it may seem relatively easy to identify ticket-switched items during check-out, several factors render this difficult. Some of these include (1) checking every scanned item with relevant information displayed on the screen drastically slows down the check-out process, (2) ticket-switched items may be difficult to differentiate (e.g., organic vs. conventional produce), (3) the lack of alertness of unconcerned check-out personnel possibly due to sheer laziness, and (4) complicity of the check-out person. The introduction of item-level RFID tags (e.g., [19]) could possibly reduce ticket-switching incidents as well as alleviate their consequences in terms of inventory management when store inventory are taken with high frequency. However, very few stores (e.g., Trasluz, American Apparel) currently have 100% store-wide item-level RFID tags in place, while several other retailers have only a few products (e.g., shoes at Macy's, Wrangler jeans at Wal-Mart, Levi's jeans at Kohl's) with item-level RFID tags. Nevertheless, complete store-wide item-level RFID tags may not necessarily eliminate ticket-switching incidents (e.g., [14]).

Given that ticket-switching is commonly known among retailers, what is surprising is the sheer lack of published research literature on ticket-switching and its related dynamics. We attempt to address this gap in extant literature. Specifically, we model ticket-switching with two items – one ‘cheap’ and the other ‘expensive’ – and the switching of the expensive item's ticket with that from the cheap item. Please note that expensive and cheap are relative terms whereby an expensive item in one ticket-switching incident could be a cheap item in another. For example, consider three items A, B and C that sell for \$1, \$50 and \$1000 respectively. While B is the expensive item for a ticketswitching incident involving items A and B, the same B is the cheap item when involved in a ticket-switching incident comprising items B and C. We do not concern ourselves with such relative differences since it's outside the scope of this paper. To our knowledge, this is among the few papers that consider ticket-switching and its effects on inventory management.

We study a few facets of the dynamics of ticket-switching incidents that are novel to existing research literature. Based on these, the contributions of this paper are three-fold: (a) we raise awareness for ticketswitching and its simultaneous effects on multiple items from an inventory management perspective, (b) we study optimal order quantity as well as retailer profit for both cheap and expensive items in the presence and absence of ticket-switching behavior, and (c) we develop associated policy implications for retailers in the presence of ticketswitching behavior.

The remainder of the paper is organized as follows: we briefly discuss ticket-switching and some ticket-switching incidents in Section 2. In Section 3, we model ticket-switching behavior in a system with two items – one expensive and the other cheap – and evaluate optimal order quantities and profit functions from different perspectives. We conclude the paper in Section 4 with a brief discussion on findings and possible extensions to this study.

## 2. Ticket-switching

Ticket-switching, by definition, requires the existence of at least two items with their own price or identity tags that are used to look up the price of the item in an associated database. Moreover, since ticketswitching incidents occur without implicit or explicit awareness/consent of the retail store personnel, the retailing environment must be conducive to such acts. This necessitates the simultaneous existence of several different items and a reasonably positive probability for a customer to successfully instantiate and complete a ticket-switching event without the knowledge of the store personnel. It can, therefore, be safely assumed that the origin of ticket-switching incidents dates back to the use of price or identity tags, which could be a bar code or an RFID (Radio Frequency IDentification) tag [23], in a retailing environment.

We believe that the origin of ticket-switching is relatively recent, perhaps as recent as the late nineteenth century, when price tags were introduced by John Wanamaker in retail store settings with the explicit purpose of replacing haggling with a fixed price for all customers. The relatively recent introduction of automated identification technology such as bar codes in retail settings about four decades ago, for efficient inventory-taking and check-out, most likely facilitated ticket-switching behavior. Unlike price tags in the form of stickers where the check-out personnel have an opportunity to verify the price sticker with the item, it is not common for check-out personnel to verify the item-description generated from the bar code scan with the actual item. Moreover, whereas the retail industry trend is moving toward more automation and fewer human touch points, manual verification of item-description with the actual item slows down the check-out process.

From a ticket-switching perspective, price stickers are the easiest, followed by bar codes and then RFID tags. Bar codes are currently the most commonly used price/item identification tag in retail environments, followed by price stickers and then by RFID tags. Item-level RFID tags are being used by a very small fraction of retail stores (e.g., Trasluz, American Apparel), primarily for inventory management purposes. It is relatively easy to ticket-switch bar codes as is evident from the few highly publicized incidents in the media. From the customer's perspective, a simple (sticker) price tag is the easiest to switch but difficult to check-out while an RFID tag is the most difficult to switch and easiest to check-out of the store. Since a price sticker is affixed or attached on the item, it is easy to switch, but the priceswitched item has a positive probability of being discovered by knowledgeable check-out personnel. Ticket-switching is difficult to accomplish with RFID since (a) unlike printing a cheap item's bar code, it is difficult to copy/clone (e.g., [14]) the content of the cheap item's RFID tag and (b) the tag may be embedded in the item. Moreover, the customer cannot switch the RFID tag from an already-purchased cheap item since the system knows that that tagged item was already purchased from the store — i.e., can't buy the same (unique coded) item more than once. However, after successful ticket-switching, it is relatively easy to remove an RFID-tagged item from a store with automated check-out.

Since ticket-switching incidents are difficult to identify using the retail store inventory information system or the actual store inventory, such incidents are generally not specifically targeted for consideration to be addressed. Moreover, based on our limited experience in such environments, we can state that not all retail stores are aware of when and how (i.e., modus operandi) ticket-switching incidents occur at their stores. It is, therefore, not surprising that ticket-switching does not get its due attention from retailers. However, ticket-switching incidents have periodically been reported by the news media especially when a large number of items, high monetary value, celebrity, or some bizarre modus operandi is involved. For example, a high-ranking executive at a well-known software firm was caught at a San Francisco Bay Area Target store affixing home-made bar codes to packages of LEGO sets that allowed him to purchase expensive LEGO sets at substantial discounts (e.g., [15]). He apparently visited several different Target stores to buy ticket-switched LEGO sets at substantial discounts and sold them through eBay to net a profit of about \$30,000 per year from these sales. Another well-publicized ticket-switching scenario involved two couples who were charged with defrauding Wal-Mart stores about \$1.5 million across 19 states over the last decade (e.g., [20]). They apparently used a home computer to print bar codes of cheaper items. The suspects then allegedly ticket-switched bar codes to buy expensive items, which they then sold elsewhere or returned for store gift cards. To avoid detection by check-out personnel, the suspects apparently conducted their ticket-switching operations by visiting stores during busy periods. In another case that garnered enough media attention, a Colorado University freshman printed bar codes with ‘Barcode Magic’ in his dorm room and used these to ticket-switch big-ticket electronic gadgets at a local Target store. For example, among other items, he bought a system valued at \$149.99 for using iPod ticket-switched with a home-made bar code for a CD player that costs \$4.99 (e.g., [27]). A customer at a Leclerc supermarket in Trélisssac, Dordogne was caught during check-out for replacing the labels on two 2300 bottles of Petrus with 2.50 labels (e.g., [2]). From these examples, it is clear that ticketswitching has the potential to create substantial loss to the retailer. With an increasing trend toward self-checkout as well as automation of the retail store check-out process, such as the Kroger's bar code Scan Tunnel (e.g., [13]), ticket-switching becomes even more salient.

When a customer carries out a ticket-switching process, it is generally done without the knowledge of the store personnel. However, there exists a variant of ticket switching that is known as sweethearting (e.g., [4,5]). Sweethearting occurs when a cashier scans a cheap (e.g., pack of chewing gum) item's bar code (taped on his/her wrist to fool an overhead surveillance camera) to help someone (e.g., a friend) purchase an expensive item for the price of the cheap item. Since both ticket-switching and sweethearting have the exact same dynamics from the perspective of the store's actual inventory, we refrain from discussing sweethearting in the remainder of this paper.

To our knowledge, there is a dearth of published research on ticketswitching and its effects on inventory management. The research publications that discuss ticket-switching that we are aware of include [4,5, 14,25,26]. However, all but the last of these publications consider different (e.g., video analysis, cryptography) means to address ticketswitching through deterrence, prevention, or recognition as it occurs. We believe that ticket-switching will continue to occur in the immediate foreseeable future, and there is a need to study its dynamics with respect to inventory management, among others. Zhou and Piramuthu [26] observe that in the presence of ticket-switching incidents, the store information system data under-estimates reality for the cheap item and over-estimates that for the expensive item. This effect is readily evident when a customer searches for a cheap item at a store's online inventory checker (e.g., target.com) and finds that the item is in-stock, it is almost certainly in stock at the store. On the other hand, for the expensive item, if the online search reveals that the item is in stock, it is likely that the store does not have the item in stock. From their analyses, Zhou and Piramuthu [26] also find that although revenue forecast estimates may not necessarily be accurate in the presence of ticketswitching incidents, these estimates are guaranteed to not be inflated. In other words, such benefit estimates can be used as a lower bound for accurate benefit estimates. Their results also suggest reduction of the proportion of expensive items as the difference between the unit cost of cheap and expensive item converges.

## 3. Inventory management under ticket-switching behavior

While inventory inaccuracy is known to be an issue in retail operations (e.g., [10,11]), the source for such inaccuracies vary across studies. We consider inaccuracy in inventory that arises primarily due to ticket-switching behavior. We use the familiar newsvendor model for our analysis with the assumption of zero starting inventory, We assume that there is a salvage value for leftover inventory whereby any leftovers are sold at a reduced price and that this leftover inventory is less than the optimal stocking quantity in the following period (e.g., [22]). As in existing literature, we assume that the unit salvage value of leftover inventory to be a composite of the discounted unit cost of this item in the next period as well as its holding cost during the current period. Although we consider a single-period model, it is readily extended to multiple periods since consecutive periods are decoupled through salvage value at the end of each period and zero starting inventory for each period

We consider a retail store setting that sells only two types of items: a cheap item and an expensive item, where the cost, price and salvage value of the cheap item (respectively, $c _ { c } , p _ { c } \mathrm { a n d } s _ { c } )$ are less than that of the expensive item (respectively, $c _ { e } , p _ { e }$ and $s _ { e } )$ . The analyses presented in this paper are generalizable to multiple simultaneous ticket-switching incidents in an additive fashion, with each ticket-switching incident considered independent of the others. We also assume the following relationship among salvage value, cost and price of the cheap and expensive items (respectively, $\displaystyle s _ { c } < c _ { c } < p _ { c }$ and $s _ { e } < c _ { e } < p _ { e } )$ . In the remainder of the paper, we use the subscripts c and e to represent cheap and expensive items respectively. Unlike ticket-switching incidents that simultaneously affect multiple items, a majority if not all, shrinkage in general results in affecting just that (type of) item. In that sense, these other types of shrinkage (e.g., theft, misplacement) can be modeled with a stochastic yield function. To account for the existence of non-ticket-switching-related shrinkage, we use a stochastic yield function $( y )$ , which we assume to be the same for both cheap and expensive items, with identical support on $[ 0 , y ^ { + } ]$ , a continuous probability density $f _ { y } ( . ) _ { \cdot }$ , distribution function $F _ { y } ( . )$ and mean $\mu _ { y } .$

We model demand for each period as independent random variables with identical support on $[ 0 , D ^ { + } ]$ , a continuous probability density function $f _ { D } ( . )$ with mean $\mu _ { D }$ and distribution function $F _ { D } ( . )$ . For tractability reasons, we consider uniformly distributed yield and demand.

We use the following notations:

• Q = overall order quantity

• q = proportion (of Q) for expensive item. $\begin{array} { r } { Q _ { e } = q Q \& Q _ { c } = ( 1 - q ) Q } \end{array}$

• q\* = optimal q

• q<sub>TS</sub><sup>⁎</sup> = optimal q when ticket-switching is present

• 1–θ = fraction of expensive items that are affected by ticket switching

• y = stochastic yield $( y \sim [ 0 , { \bf y } + ] ) ; { \mathsf { w e } }$ assume $y _ { c h e a p } = y _ { e x p e n s i v e } = y$

• D = demand ( $\mathrm { D c } \sim [ 0 , D _ { c } ^ { + } ] ; \mathrm { D e } \sim [ 0 , D _ { e } ^ { + } ] )$

• fx(.) = continuous probability density function of random variable $x \in \{ D , \theta , y \}$ with mean μx

Table 1  
Reality vs. information system perspectives of demand under ticket-switching.

<table><tr><td></td><td>Reality</td><td>Information system</td></tr><tr><td>Cheap item</td><td> $D_c$ </td><td> $D_c + (1 - \theta)qQy_e$ </td></tr><tr><td>Expensive item</td><td> $D_e + (1 - \theta)qQy_e$ </td><td> $D_e$ </td></tr></table>

$\operatorname { F x } ( . )$ = continuous probability distribution function of x  
• c = unit cost, with cc and ce for cheap and expensive items respectively  
• p = unit selling price $( p > c ) ,$ , with pc and pe for cheap and expensive items respectively  
• s = salvage value $( c > s ) ,$ , with sc and se for cheap and expensive items respectively  
• $\Pi ( . )$ = profit function  
• ΠTS(.) = profit function when ticket-switching is present  
$\Pi ^ { T S } ( . )$ = profit function when ticket-switching is absent.

Similar to most other types of shrinkage, the effect of ticket-switching is different on the actual state of affairs and that in the retail store informa tion system. For example, Table 1 illustrates the differential effects of ticket-switching from the perspective of demand for both cheap and expensive items. The demand for the expensive item is more based on actual (vs. retail store information system) inventory, while that for the cheap item is less based on actual (vs. retail store information system) inventory. Therefore, in the presence of ticket-switching behavior, inventory management would be different when considered from the perspective of data from the retail store information system vs. reality (e.g., manual inventory taking, followed by decision-making based on instantaneous demand, etc.).

We consider only the retail store's actual inventory data and not data from the retail store's information system. Our choice here is motivated by the fact that although most retail store-level decisions are made considering data from the store information system, ultimately the actual in-store inventory is what matters. In other words, regardless of what the store's information system inventory states, an item that is not on the retail store shelf will not be sold. On the other hand, an item on the retail store shelf has a positive probability of being sold even though the store inventory system shows that there is zero number of this item in stock.

Ideally, the actual data (e.g., actual inventory of items on store shelves) and data stored in the retail store information system must be the same at all times. However, this is generally an exception rather than a rule. The data in the retail store information system are generally updated upon orde arrival as well as in response to sale events. It is uncommon for shrinkage events to trigger a concomitant update in the information system. This may not necessarily be true for damaged or spoiled items since these incidents are known to the store personnel, who can then register these events in the store information system. The divergence over time of actual inventory data and the data stored in retail store information system is a known phenomenon, and retail stores attempt to reconcile the difference through periodic manual inventorving of the entire store. However, the frequency of such manual inventory-taking in a majority of retail stores leaves much to be desired. For example, it is not uncommon for large retail stores to do a complete and thorough in-store inventory check only twice or thrice per year. We assume that all items are moved to the store shelves immediately upon reception at the store and that the total shelf-space at the store is fixed. We also assume that the total store shelf-space is the same as the overal order quantity Q, which is fixed. We vary the number of expensive and cheap items through $q ,$ which is the decision variable. Since Q is fixed, we assume that the items are all of the same dimensions and that their proportions can be easily modified.

We first consider the effects of ticket-switching behavior from the expensive item's perspective followed by that from the cheap item's perspective. We distinguish the two cases [12] that arise due to the randomness in demand (a) Case A: inventory underage and overage occur as per demand ran domness as well as per the realization of the stochastic yield function, and (b) Case B: stock overage occurs with certainty regardless of the demand.

## 3.1. Expensive item

Case A.

$$
y ^ {+} \theta Q _ {e} \leq D _ {e} ^ {+}
$$

This case models the scenario where the demand for expensive items is more than the available number of expensive items, while considering effects due to ticket-switching and yield. The expected profit function for this scenario includes expected overage cost, expected underage cost, and production cost, and is written as:

$$
\begin{array}{l} \Pi_ {A} ^ {T S} (Q _ {e}) = - c _ {e} Q _ {e} + \int_ {0} ^ {y ^ {+}} f _ {y} (y) \int_ {0} ^ {1} f _ {\theta} (\theta) \int_ {0} ^ {y \theta Q _ {e}} (p _ {e} D _ {e} + s _ {e} (y \theta Q _ {e} - D _ {e})) f _ {D _ {e}} (D _ {e}) \mathrm{d} D _ {e} \mathrm{d} \theta \mathrm{d} y \\ \qquad + \int_ {0} ^ {y ^ {+}} f _ {y} (y) \int_ {0} ^ {1} f _ {\theta} (\theta) \int_ {y \theta Q _ {e}} ^ {D _ {e} ^ {+}} (p _ {e} y \theta Q _ {e}) f _ {D _ {e}} (D _ {e}) \mathrm{d} D _ {e} \mathrm{d} \theta \mathrm{d} y. \end{array}
$$

The expected profit function is strictly concave (e.g., [12,24]) and this property can be used to derive first-order conditions. It is also known (e.g., [8,12]) that analytical closed form expressions can be derived only for specific types of demand and yield distributions that include the expo nential and the uniform distributions. As per Inderfurth [12], we consider uniform distributions for demand and yield. The assumption of uniform distribution for both demand and yield results in:

$$
F _ {D _ {e}} (D _ {e}) = \frac {D _ {e}}{D _ {e} ^ {+}} \text {   for   } 0 \leq D _ {e} \leq D _ {e} ^ {+}\tag{1}
$$

$$
f _ {y} (y) = \frac {1}{y ^ {+}} \text {   for   } 0 \leq y \leq y ^ {+}.\tag{2}
$$

Incorporating the above in the profit function, we get:

$$
\begin{array}{c} \frac {\partial \Pi_ {A} ^ {T S} (Q _ {e})}{\partial q} = - c _ {e} Q + \frac {s _ {e} q Q ^ {2}}{3 D _ {e} ^ {+}} \int_ {0} ^ {y ^ {+}} y ^ {2} f _ {y} (y) \mathrm{d} y + p _ {e} \mu_ {\theta} Q \int_ {0} ^ {y ^ {+}} y f _ {y} (y) \mathrm{d} y \\ - \frac {p _ {e} q Q ^ {2}}{3 D _ {e} ^ {+}} \int_ {0} ^ {y ^ {+}} y ^ {2} f _ {y} (y) \mathrm{d} y \end{array}
$$

and, the optimal proportion of the expensive item when ticket-switching is present is:

$$
q _ {T S} ^ {*} = \frac {9 D _ {e} ^ {+} \left(p _ {e} \mu_ {\theta} \mu_ {y} - c _ {e}\right)}{Q (y ^ {+}) ^ {2} (p _ {e} - s _ {e})}.\tag{3}
$$

Case B.

$$
y ^ {+} \theta Q _ {e} > D _ {e} ^ {+}
$$

This case models the scenario where the demand for expensive items is at most equal to the available number of expensive items, while considering effects due to ticket-switching and yield. The expected profit function for this scenario is written as:

$$
\begin{array}{l} \Pi_ {B} ^ {T S} (Q _ {e}) = - c _ {e} Q _ {e} + \int_ {0} ^ {y ^ {+}} f _ {y} (y) \int_ {0} ^ {1} f _ {\theta} (\theta) \int_ {0} ^ {y \theta Q _ {e}} (p _ {e} D _ {e} + s _ {e} (y \theta Q _ {e} - D _ {e})) f _ {D _ {e}} (D _ {e}) d D _ {e} d \theta d y \\ \qquad + \int_ {0} ^ {y ^ {+}} f _ {y} (y) \int_ {0} ^ {1} f _ {\theta} (\theta) \int_ {0} ^ {D _ {e} ^ {+}} (p _ {e} D _ {e} + s _ {e} (y \theta Q _ {e} - D _ {e})) f _ {D _ {e}} (D _ {e}) d D _ {e} d \theta d y \\ \qquad + \int_ {0} ^ {y ^ {+}} f _ {y} (y) \int_ {0} ^ {1} f _ {\theta} ({\theta}) \int_ {y \theta Q _ {e}} ^ {D _ {e} ^ {+}} (p _ {e} y \theta Q _ {e}) f _ {D _ {e}} (D _ {e}) d D _ {e} d \theta d y \\ \frac {\partial \Pi_ {B} ^ {T S} (Q _ {e})}{\partial q} = - c _ {e} Q + \frac {s _ {e} q Q ^ {2}}{3 D _ {e} ^ {+}} \int_ {0} ^ {y ^ {+}} y f _ {y} (y) d y + s _ {e} \mu_ {\theta} Q \int_ {0} ^ {y ^ {+}} y f _ {y} (y) d y \\ \qquad + p _ {e} \mu_ {\theta} Q \int_ {0} ^ {y ^ {+}} y f _ {y} (y) d y - \frac {p _ {e} q Q ^ {2}}{3 D _ {e} ^ {+}} \int_ {0} ^ {y ^ {+}} y f _ {y} (y) d y. \end{array}
$$

With the uniform distribution assumption for both demand and yield, we get:

$$
q _ {T S} ^ {*} = \frac {3 D _ {e} ^ {+} \left[ (s _ {e} + p _ {e}) \mu_ {\theta} \mu_ {y} - c _ {e} \right]}{(p _ {e} - s _ {e}) Q \mu_ {y}}.\tag{4}
$$

From Eqs. $\left( 3 \right) \& \left( 4 \right)$ , we observe that the optimal order quantity of the expensive item is less when the average fraction of expensive items that are unaffected by ticket-switching is less

We now consider the cheap item and derive the optimal order quantities for the two cases.

3.2. Cheap item

Case A.

$$
y ^ {+} Q _ {c} + (1 - \theta) y ^ {+} Q _ {e} \leq D _ {c} ^ {+}
$$

This case models the scenario where the demand for cheap items is more than the available number of cheap items, while considering effects due to ticket-switching and yield. The effects due to ticket-switching materializes as virtual demand for the cheap item — i.e., even though the information system registers the ticket-switching event as the sale of a cheap item event, the actual cheap item remains unchanged after a ticket-switching event. The net effect on cheap item inventory is that in addition to its own inventory, the ticket-switched expensive items are sold off (from the retail store's perspective) as cheap items.

$$
\begin{array}{l} \Pi_ {A} ^ {T S} (Q _ {c}) = - c _ {c} Q _ {c} + \int_ {0} ^ {y ^ {+}} f _ {y} (y) \int_ {0} ^ {1} f _ {\theta} (\theta) \int_ {0} ^ {y Q _ {c} + (1 - \theta) y Q _ {e}} (p _ {c} D _ {c} + s _ {c} (y Q _ {c} - D _ {c})) f _ {D _ {c}} (D _ {c}) d D _ {c} d \theta d y \\ \quad + \int_ {0} ^ {y ^ {+}} f _ {y} (y) \int_ {0} ^ {1} f _ {\theta} (\theta) \int_ {y Q _ {c} + (1 - \theta) y Q _ {e}} ^ {D _ {c} ^ {+}} p _ {c} y Q _ {c} f _ {D _ {c}} (D _ {c}) d D _ {c} d \theta d y \end{array}
$$

Assuming uniform distribution for both demand and yield, we get:

$$
\begin{array}{l} \frac {\partial \Pi_ {A} ^ {T S} (Q _ {c})}{\partial q} = c _ {c} Q + \frac {(p _ {c} - s _ {c}) q Q ^ {2} (1 - q \mu_ {\theta})}{D _ {c} ^ {+}} \int_ {0} ^ {y ^ {+}} y ^ {2} f _ {y} (y) \mathrm{d} y - p _ {c} q Q \int_ {0} ^ {y ^ {+}} y f _ {y} (y) \mathrm{d} y \\ q _ {T S} ^ {*} = \frac {3 D _ {c} ^ {+} p _ {c} \mu_ {y} - (p _ {c} - s _ {c}) Q y ^ {+ 2} + \sqrt {\left[ (p _ {c} - s _ {c}) Q y ^ {+ 2} - 3 D _ {c} ^ {+} p _ {c} \mu_ {y} \right] ^ {2} + 1 2 c _ {c} Q (p _ {c} - s _ {c}) \mu_ {\theta} y ^ {+ 2} D _ {c} ^ {+}}}{2 (p _ {c} - s _ {c}) Q \mu_ {\theta} y ^ {+ 2}}. \end{array}\tag{5}
$$

Case B.

$$
y ^ {+} Q _ {c} + (1 - \theta) y ^ {+} Q _ {e} > D _ {c} ^ {+}
$$

This case models the scenario where the demand for cheap items is at most equal to the available number of cheap items, while considering effects due to ticket-switching and yield.

$$
\begin{array}{l} \Pi_ {B} ^ {T S} (Q _ {c}) = - c _ {c} Q _ {c} + \int_ {0} ^ {y ^ {+}} f _ {y} (y) \int_ {0} ^ {1} f _ {\theta} (\theta) \int_ {0} ^ {y Q _ {c} + (1 - \theta) y Q _ {e}} (p _ {c} D _ {c} + s _ {c} (y Q _ {c} - D _ {c})) f _ {D _ {c}} (D _ {c}) d D _ {c} d \theta d y \\ \quad + \int_ {0} ^ {y ^ {+}} f _ {y} (y) \int_ {0} ^ {1} f _ {\theta} (\theta) \int_ {0} ^ {D _ {c} ^ {+}} (p _ {c} D _ {c} + s _ {c} (y Q _ {c} - D _ {c})) f _ {D _ {c}} (D _ {c}) d D _ {c} d \theta d y \\ \quad + \int_ {0} ^ {y ^ {+}} f _ {y} (y) \int_ {0} ^ {1} f _ {\theta} (\theta) := \int_ {y Q _ {c} + (1 - \theta) y Q _ {e}} ^ {D _ {c} ^ {+}} p _ {c} y Q _ {c} f _ {D _ {c}} (D _ {c}) d D _ {c} d \theta d y \end{array}
$$

With the assumption uniform distribution for both demand and yield, we get:

$$
\begin{array}{c} \frac {\partial \Pi_ {B} ^ {T S} (Q _ {c})}{\partial q} = c _ {c} Q + \frac {s _ {c} Q ^ {2} (q \mu_ {\theta} - 1)}{D _ {c} ^ {+}} \int_ {0} ^ {y ^ {+}} y ^ {2} f _ {y} (y) \mathrm{d} y + s _ {c} Q \int_ {0} ^ {y ^ {+}} y f _ {y} (y) \mathrm{d} y \\ - \int_ {0} ^ {y ^ {+}} p _ {c} y Q \bigg (1 - \frac {y Q (1 - q \mu_ {\theta})}{D _ {c} ^ {+}} \bigg) f _ {y} (y) \mathrm{d} y \\ q _ {T S} ^ {*} = \frac {1}{\mu_ {\theta}} - \frac {3 D _ {c} ^ {+}}{(p _ {c} - s _ {c}) Q \mu_ {\theta} (y ^ {+}) ^ {3}} \Big [ (s _ {c} + p _ {c}) \mu_ {y} - c _ {c} \Big ]. \end{array}\tag{6}
$$

Similar to that with Eqs. $( 3 ) \& ( 4 )$ , from Eqs. $( 5 ) \& ( 6 )$ we observe that the optimal order quantity of the cheap item is less when the fraction of expensive items unaffected by ticket-switching is less.

We considered the two cases for both cheap and expensive items in the presence of ticket-switching behavior. To derive the expressions for the scenario where ticket-switching incidents are absent, we se $\begin{array} { r } { \mathbf { \rho } : \theta = \mu _ { \theta } = 1 } \end{array}$ in the expressions for $\Pi _ { A } ^ { T S } ( Q _ { e } ) , \bar { \Pi } _ { B } ^ { T S } ( Q _ { e } ) , \Pi _ { A } ^ { T S } ( Q _ { c } )$ and $\Pi _ { B } ^ { T S } ( Q _ { c } )$ respectively fo the following four cases. The resulting optimal order quantity (Case A) for the expensive item in the absence of ticket-switching behavior is:

$$
q ^ {*} = \frac {3 D _ {e} ^ {+} \left(p _ {e} \mu_ {y} - c _ {e}\right)}{Q (y ^ {+}) ^ {2} \left(p _ {e} - s _ {e}\right)}.\tag{7}
$$

Similarly, Case B for expensive item in the absence of ticket-switching behavior is:

$$
q ^ {*} = \frac {3 D _ {e} ^ {+} \left[ (s _ {e} + p _ {e}) \mu_ {y} - c _ {e} \right]}{(p _ {e} - s _ {e}) Q \mu_ {y}}.\tag{8}
$$

Case A for cheap item in the absence of ticket-switching incidents is:

$$
q ^ {*} = \frac {3 D _ {c} ^ {+} p _ {c} \mu_ {y} - (p _ {c} - s _ {c}) Q y ^ {+ 2} + \sqrt {\left[ (p _ {c} - s _ {c}) Q y ^ {+ 2} - 3 D _ {c} ^ {+} p _ {c} \mu_ {y} \right] ^ {2} + 1 2 c _ {c} Q (p _ {c} - s _ {c}) y ^ {+ 2} D _ {c} ^ {+}}}{2 (p _ {c} - s _ {c}) Q y ^ {+ 2}}.\tag{9}
$$

Case B for cheap item in the absence of ticket-switching incidents is:

$$
q ^ {*} = 1 - \frac {3 D _ {c} ^ {+}}{\left(p _ {c} - s _ {c}\right) Q \left(y ^ {+}\right) ^ {3}} \left[ \left(s _ {c} + p _ {c}\right) \mu_ {y} - c _ {c} \right].\tag{10}
$$

We now derive some results based on the above.

## 3.3. Optimal order quantity

Theorem 3.1. Everything else being the same, (a) Case A: the optimal order quantity of the expensive item when ticket-switching is present is more than that when ticket-switching is absent and (b) Case B: the optimal order quantity of the expensive item when ticket-switching is present is less than that when ticket-switching is absent.

Proof. We separately consider the Cases (A & B).

Case A. We use Eqs. $( 3 ) \& ( 7 )$ respectively for the presence and absence of ticket-switching incidents. The optimal order quantities when ticket switching is present and absent are given by:

$$
\frac {9 D _ {e} ^ {+} \left(p _ {e} \mu_ {\theta} \mu_ {y} - c _ {e}\right)}{Q (y ^ {+}) ^ {2} (p _ {e} - s _ {e})} \gtrless \frac {3 D _ {e} ^ {+} \left(p _ {e} \mu_ {y} - c _ {e}\right)}{Q (y ^ {+}) ^ {2} (p _ {e} - s _ {e})}
$$

which is the same as

$$
p _ {e} \mu_ {y} (3 \mu_ {\theta} - 1) \gtrless 2 c _ {e}.
$$

Since $( 3 \mu _ { \theta } - 1 ) \lessapprox 2$ and $p _ { e } \mu _ { y } > c _ { e } ,$ the LHS (left hand side) N RHS (right hand side), especially for higher μ<sub>y</sub> values.

Case B. Similar to Case A above, we use Eqs. (4) & (8) respectively for the presence and absence of ticket-switching incidents. The optimal order quantities when ticket-switching is present and absent are given by:

$$
\frac {3 D _ {e} ^ {+} \left[ (s _ {e} + p _ {e}) \mu_ {\theta} \mu_ {y} - c _ {e} \right]}{(p _ {e} - s _ {e}) Q \mu_ {y}} \gtrless \frac {3 D _ {e} ^ {+} \left[ (s _ {e} + p _ {e}) \mu_ {y} - c _ {e} \right]}{(p _ {e} - s _ {e}) Q \mu_ {y}}.
$$

The expression on the LHS is less than that on the RHS. □

Theorem 3.2. Everything else being the same, the optimal order quantity of the cheap item when ticket-switching is present is less than that whe ticket-switching is absent.

Proof. We separately consider the Cases (A & B).

Case A. We use Eqs. (5) & (9) respectively for the presence and absence of ticket-switching incidents.

The optimal order quantities when ticket-switching is present and absent are given by:

$$
\frac {\frac {3 D _ {c} ^ {+} p _ {c} \mu_ {y} - (p _ {c} - s _ {c}) Q y ^ {+ 2} + \sqrt {\left[ (p _ {c} - s _ {c}) Q y ^ {+ 2} - 3 D _ {c} ^ {+} p _ {c} \mu_ {y} \right] ^ {2} + 1 2 c _ {c} Q (p _ {c} - s _ {c}) \mu_ {\theta} y ^ {+ 2} D _ {c} ^ {+}}}{2 (p _ {c} - s _ {c}) Q \mu_ {\theta} y ^ {+ 2}}}{\frac {3 D _ {c} ^ {+} p _ {c} \mu_ {y} - (p _ {c} - s _ {c}) Q y ^ {+ 2} + \sqrt {\left[ (p _ {c} - s _ {c}) Q y ^ {+ 2} - 3 D _ {c} ^ {+} p _ {c} \mu_ {y} \right] ^ {2}} + 1 2 c _ {c} Q (p _ {c} - s _ {c}) y ^ {+ 2} D _ {c} ^ {+}}{2 (p _ {c} - s _ {c}) Q y ^ {+ 2}}}.
$$

The left hand side is greater than the right hand side. Since the optimal order quantity is $Q ( 1 - q )$ , we take the negation of this result.

Case B. The optimal order quantities when ticket-switching is present and absent are given by:

$$
\frac {1}{\mu_ {\theta}} - \frac {3 D _ {c} ^ {+}}{\left(p _ {c} - s _ {c}\right) Q \mu_ {\theta} \left(y ^ {+}\right) ^ {3}} \left[ \left(s _ {c} + p _ {c}\right) \mu_ {y} - c _ {c} \right] \geqslant 1 - \frac {3 D _ {c} ^ {+}}{\left(p _ {c} - s _ {c}\right) Q \left(y ^ {+}\right) ^ {3}} \left[ \left(s _ {c} + p _ {c}\right) \mu_ {y} - c _ {c} \right].
$$

Clearly, the LHS is greater than the RHS in the above. □

Similar to Case A, we use Eqs. (6) & (10) respectively for the presence and absence $( \theta = 1 \& \mu _ { \theta } = 1 )$ of ticket-switching incidents.

When ticket-switching is known to exist at a retail store, the retailer must take measures to discourage such incidents such as through verification of each item during check-out. However, this may not be entirely possible during busy time periods when several items have similar descriptions but have large variations in their price. Together, Theorems 3.1 & 3.2 state that when ticket-switching is known to be present, the retailer must order less of both the expensive and cheap items versus when ticket-switching is absent except when Case A is true for the expensive item. Preventive measures as well as ordering of cheap and expensive items in appropriate quantities would help improve retailer profit.

We now consider optimal order quantity of cheap and expensive items in the absence of other types of shrinkage, as modeled by perfect yield conditions in our study.

Corollary 3.3. Everything else being the same, under perfect yield conditions, (a) Case A: the optimal order quantity of the expensive item when ticket switching is present is more than that when ticket-switching is absent and (b) Case B: the optimal order quantity of the expensive item when ticket switching is present is less than that when ticket-switching is absent.

Proof. Since we defined yield to account for only other types of shrinkage, $\mu _ { y } = 1$ in the absence of these other types of shrinkage. The result follows from Theorem 3.1.

Corollary 3.4. Everything else being the same, under perfect yield conditions, the optimal order quantity of the cheap item when ticket-switching is present is less than that when ticket-switching is absent.

Proof. The argument is similar to that in Corollary 3.3 where $\mu _ { y } = 1$ in the absence of these other types of shrinkage. The result then follows from Theorem 3.2. □

Corollaries 3.3 & 3.4 state that the results from Theorems 3.1 & 3.2 are stronger in the absence of other (i.e., excluding those due to ticket switching incidents) types of shrinkage.

## 3.4. Profit in the presence/absence of ticket-switching behavior

We now consider the effect of ticket-switching behavior on retail store profit. To understand the dynamic from the perspective of expensive and cheap items when ticket-switching incidents are present or absent, we consider these scenarios separately for the expensive and cheap items.

Theorem 3.5. Everything else being the same, the expected profit due only to the expensive item when ticket-switching is present is more than that when ticket-switching is absent.

Proof. We consider the A and B cases separately.

Case A. Under ticket-switching conditions, the expected profit is:

$$
\Pi_ {A} ^ {T S} (Q _ {e}) = - c _ {e} Q _ {e} + p _ {e} Q _ {e} \mu_ {\theta} \mu_ {y} - \frac {(p _ {e} - s _ {e}) Q _ {e} ^ {2} (y ^ {+}) ^ {2}}{1 8 D _ {e} ^ {+}}.
$$

We similarly derive the profit expression for the scenario where ticket-switching behavior is absent.

$$
\Pi_ {A} ^ {\overline {{T S}}} (Q _ {e}) = - c _ {e} Q _ {e} + p _ {e} Q _ {e} \mu_ {y} - \frac {(p _ {e} - s _ {e}) Q _ {e} ^ {2} (y ^ {+}) ^ {2}}{6 D _ {e} ^ {+}}
$$

By substituting the optimal order quantities in the presence of ticket-switching as given by Eq. (3) and in the absence of ticket-switching as given by Eq. (7) into these profit functions, we get:

$$
3 \left(p _ {e} \mu_ {y} \mu_ {\theta} - c _ {e}\right) ^ {2} > \left(p _ {e} \mu_ {y} - c _ {e}\right) ^ {2}
$$

therefore, $\Pi _ { A } ^ { T S } ( Q _ { e } ) { > } \Pi _ { A } ^ { \overline { { { T S } } } } ( Q _ { e } )$

Case B. Under ticket-switching conditions, the expected profit is:

$$
\Pi_ {B} ^ {T S} (Q _ {e}) = - c _ {e} Q _ {e} + \frac {(p _ {e} + s _ {e}) (D _ {e} ^ {+}) ^ {2}}{1 8 y ^ {+} \theta^ {3} Q _ {e}} + \mu_ {D _ {e}} (p _ {e} - s _ {e}) \left(1 - \frac {1}{\theta Q _ {e}}\right) + \frac {s _ {e} Q _ {e} \mu_ {\theta} y ^ {+}}{2} - \frac {s _ {e} \mu_ {\theta} (D _ {e} ^ {+}) ^ {2}}{2 y ^ {+} \theta^ {2} Q _ {e}} + \frac {D _ {e} ^ {+}}{y ^ {+} \theta Q _ {e}} - \frac {\mu_ {\theta}}{y ^ {+}}
$$

and,

$$
\Pi_ {B} ^ {\overline {{T S}}} (Q _ {e}) = - c _ {e} Q _ {e} - \left(p _ {e} - s _ {e}\right) \left[ \frac {\left(D _ {e} ^ {+}\right) ^ {3}}{3 y ^ {+} Q _ {e}} - \mu_ {D _ {e}} \left(1 - \frac {D _ {e} ^ {+}}{y ^ {+} Q _ {e}}\right) - \frac {\left(D _ {e} ^ {+}\right) ^ {2}}{2 y ^ {+} Q _ {e}} \right] + s _ {e} Q _ {e} \mu_ {y}.
$$

Similar to Case A, we substitute the optimal order quantities in the presence of ticket-switching as given by Eq. (4) and in the absence of ticket switching as given by Eq. (8) into these profit functions, and observe that $\Pi _ { B } ^ { T S } ( Q _ { e } ) { > } T I _ { B } ^ { \overline { { { T S } } } } ( Q _ { e } )$ . □

Theorem 3.6. Everything else being the same, the expected profit due only to the cheap item when ticket-switching is present is less than that when ticket-switching is absent.

Proof. Again, we consider the A and B cases separately.

Case A. Under ticket-switching conditions, the expected profit is:

$$
\Pi_ {A} ^ {T S} (Q _ {c}) = - c _ {c} Q _ {c} - \frac {(p _ {c} - s _ {c}) (y ^ {+}) ^ {2} Q _ {e} ^ {2}}{3 D _ {c} ^ {+} q ^ {2}} \left(\frac {1}{2} - q\right) - \frac {(p _ {c} - s _ {c}) Q _ {e} ^ {2} (y ^ {+}) ^ {2}}{3 D _ {c} ^ {+}} \left(\mu_ {\theta} - \frac {1}{6}\right) + p _ {c} Q _ {c} \mu_ {y}.
$$

When ticket-switching is absent, the expected profit is:

$$
\Pi_ {A} ^ {\overline {{T S}}} (Q _ {c}) = - c _ {c} Q _ {c} - \frac {(p _ {c} - s _ {c}) (y ^ {+}) ^ {2} Q _ {c} ^ {2}}{6 D _ {c} ^ {+}} + p _ {c} Q _ {c} \mu_ {y}.
$$

After substitution of the optimal order quantities in the presence of ticket-switching as given by Eq. (5) and in the absence of ticket-switching as given by Eq. (9) into these profit functions, we observe that $\Pi _ { A } ^ { T S } ( Q _ { c } ) < T I _ { A } ^ { \overline { { { T S } } } } ( Q _ { c } )$ .

Case B. Under ticket-switching conditions, the expected profit $\Pi _ { B } ^ { T S } ( Q _ { c } ) =$

$$
\begin{array}{l} \left(\frac {D _ {c} ^ {+}}{Q _ {c} + (1 - \theta) Q _ {e}}\right) ^ {3} \left[ \frac {s _ {c} Q _ {c} (2 Q _ {c} + Q _ {e})}{6 D _ {c} ^ {+}} + \frac {(p _ {c} - s _ {c})}{6 D _ {c} ^ {+} y ^ {+}} \left(\frac {4 Q _ {e} ^ {2}}{3} - 2 Q _ {c} Q _ {e} \mu_ {\theta} - 2 Q _ {e} ^ {2} \mu_ {\theta}\right) + \frac {p _ {c} Q _ {c} (Q _ {e} - Q _ {c})}{6 D _ {c} ^ {+} y ^ {+}} - \frac {s _ {c} Q _ {c} (Q _ {c} + 2 Q _ {e})}{6 D _ {c} ^ {+} y ^ {+}} \right] - \\ c _ {c} Q _ {c} + \frac {(p _ {c} - s _ {c})}{y ^ {+}} \left(\frac {D _ {c} ^ {+}}{Q _ {c} + (1 - \theta) Q _ {e}}\right) \left[ \frac {Q _ {c} D _ {c} ^ {+}}{2 (Q _ {c} + (1 - \theta) Q _ {e})} - \mu_ {D _ {c}} \right] - (p _ {c} - s _ {c}) \mu_ {D _ {c}} + s _ {c} Q _ {c} \mu_ {y} \end{array}
$$

and, $\Pi _ { B } ^ { \overline { { { T S } } } } ( Q _ { c } ) =$

$$
- c _ {c} Q _ {c} + \frac {\left(p _ {c} + s _ {c}\right) Q _ {c} ^ {2}}{6 D _ {c} ^ {+} y ^ {+}} \left(\frac {D _ {c} ^ {+}}{Q _ {c}}\right) ^ {3} + \left(p _ {c} - s _ {c}\right) \mu_ {D _ {c}} \left(1 - \frac {D _ {c} ^ {+}}{y ^ {+} Q _ {c}}\right) + s _ {c} Q _ {c} \left(\mu_ {y} - \frac {D _ {c} ^ {+}}{y ^ {+} Q _ {c}}\right) + \frac {p _ {c} \left(D _ {c} ^ {+}\right) ^ {2}}{Q _ {c} ^ {2} y ^ {+}} - \frac {D _ {c} ^ {+} p _ {c}}{3 y ^ {+}}
$$

here, $\Pi _ { B } ^ { T S } ( Q _ { c } ) < T I _ { B } ^ { \overline { { { T S } } } } ( Q _ { c } )$ : □

Theorems (3.5 & 3.6) state that the profit for the retailer increases for expensive items and decreases for cheap items in the presence of ticketswitching behavior than otherwise. Although these are counter-intuitive from an actual inventory data perspective, actual retail store inventory data and the optimization of order quantity based on that data result in such outcomes. The profit decrease for the cheap item is counter-intuitive due to the fact that both cheap item inventory and the ticket-switched expensive item inventory contribute to profit associated with the cheap items since the sale of ticket-switched expensive items register as cheap item sales in the store's inventory information system. This could be explained by the difference between actual in-store data and store information system data in that ticket-switching assigns more profit based on the latter that are not actually realized in reality. On the other hand, profit increase for the expensive item is possible since the model acknowledges the existence of ticket-switching behavior and the optimal order quantity incorporates this dynamic.

## 4. Discussion

It is generally acknowledged that data from the retail store's inventory system does not necessarily strictly reflect reality and this divergence (from reality) only worsens with time. To address this disparity, retailers take manual inventory of their stores and reconcile any differences that they find in their store information system. However, in a majority of cases, such manual inventory is taken less than a handful of times per year. This allows enough time for the possibility of the information system to reflect information that is divergent from the store's actual in-store inventory. A primary cause for such disparity in retail store settings is shrinkage.

Unlike a majority of shrinkage that occur in retail store environments, ticket-switching is unique in that it simultaneously affects multiple (usually, two) items. The result of a ticket-switching event on in-store inventory is that there is one less inventory of the expensive item based on actual inventory and one less inventory of the cheap item based on the store's information system. The store also incurs a loss of at least the price difference between the expensive and cheap item, in addition to related costs due to inventory misalignment such as the potential for stockouts of the expensive item and excess inventory of the cheap item.

We considered a store that carries only two types of items – one cheap and the other (relatively) expensive – to illustrate the dynamics due to ticket-switching behavior on the store's inventory of these two types of items. For tractability purposes, we assumed demand and yield for these items to follow uniform distribution. Since we did not consider other distributions, the generalizability of these results to other distributions is not known. In order to remain true to the real state of affairs, we considered the actual store inventory (vs. data from the retail store's inventory information system) for our modeling purpose. We considered both optimal order quantity and store profit in the presence and absence of ticket-switching. Results from our analyses indicate that the optimal order quantity of the expensive item is more in the presence of ticket-switching behavior compared to that when ticket-switching behavior is absent in the retail store environment. Similarly, our results also indicate that the optimal order quantity of the cheap item is less in the presence of ticket-switching behavior than otherwise. These results are more salient in the absence of other types of shrinkage, as modeled by perfect yield as proxy. The policy implication here is that when ticket-switching behavior is known to be present, the optimal order quantity of the cheap and expensive items must be adjusted accordingly — i.e., increase the order quantity of expensive items and decrease the order quantity of cheap items.

Once the order quantity is optimized, we observe that the retail store profit in the presence of ticket-switching behavior is more (less, respectively) than that in the absence of ticket-switching behavior for expensive (cheap, respectively) items. This result signifies the importance of optimizing the order quantity of both cheap and expensive items with the incorporation of dynamics related to ticket-switching behavior. Clearly, if ticket-switching behavior can be reduced or eliminated altogether, that would certainly be in the store's best interest. However, we believe that with the complexities associated with managing a retail store environment that employs hundreds of store personnel and in which dozens of thousands of items are stocked for sale to thousands of customers, it is extremely difficult to completely eliminate ticketswitching behavior. On the other hand, we believe that it's better to allow for such events to occur at extremely low levels while allocating the retail store budget to other important services and products. In other words, it is a very expensive proposition to completely prevent ticket-switching behavior in large retail store environments.

Given the lack of published research literature on ticket-switching behavior as related to inventory management, we set out to create awareness for this phenomenon among researchers and to develop some insights into the dynamics of ticket-switching behavior. Given that data from the retail store information system is used in a majority of retail store decision-making situations, there is a need to ensure that such data reflects reality. In fact, as used daily in stores such as American Apparel, recent advances in automatic identification technology such as RFID allow for more frequent reconciliation of actual and information system inventory data. Discrepancy in inventory data may also create other issues. For example, the demand for an item is known to be directly proportional to its number of facings (e.g., [3]). When a store optimizes the number of facings for each item, any type of shrinkage that is not visible to the store's information system can wreak havoc with the store's inventory management and therefore its profit. We did not consider the effects of ticket-switching in creating (e.g., for the cheap item) or reducing (e.g., for the expensive item) demand. We also did not consider the loss of sale due to the (expensive) items that are ticket-switched. We considered actual data and not that from the store's information system, which the retail stores use to make decisions. An easy way to avoid ticket-switching is to drop the cheap product when only two items are present. However, given that most retail stores carry items at several price points, it is challenging to identify the ‘cheap’ item to discontinue.

One of the reviewers of this paper suggested the use of item's weight as a ticket-switching deterrence mechanism. We believe that this excellent suggestion could work in reducing the number of ticketswitching incidents when the item's weight is also verified during check-out. This necessitates the incorporation of item weight along with its price and other information in the check-out system. It also necessitates the check-out counter personnel to scan the item's bar code as well as place the item on the weighing machine for weight measurement. If the item's weight is incorporated in the check-out system, any significant deviation in actual and measured weight can be used to trigger an alarm. While this could work, in principle, we believe that this places additional burden on the check-out personnel and/or the check-out system since this additional information (item weight) has to be input for all SKUs (Stock Keeping Units) that are carried at the store. The onus placed on the check-out personnel is similar to that where the item's description is checked with the actual item that is being checked out. In our opinion, these definitely have the potential to reduce the number of ticket-switching incidents.

With the non-trivial amounts that are associated with recently exposed ticket-switching incidents and the thin margins with which these retail stores operate, there is an urgent need to study the underlying dynamics of ticket-switching behavior and related consequences to retail store operations. We sincerely hope that researchers in this area would take it upon themselves to study and understand this phenomenon with the ultimate goal to reduce, if not completely eliminate, ticketswitching incidents in retail environments.

## Acknowledgment

We thank the two reviewers for providing extensive constructive comments and suggestions that have helped improve the content and presentation of this paper.

## References

[1] P. Abell, B. Ream, Reaping profit through loss prevention technology, AMR Research Report 2001

[2] Agence France Press, http://www.intothewine.fr/tags/trelissac-vin2011.

[3] R. Bai, G. Kendall, A model for fresh produce shelf-space allocation and inventory management with freshness-condition-dependent demand, INFORMS Journal on Computing 20 (1) (2008) 78–85.

[4] R. Bobbit, J. Connell, N. Haas, C. Otto, S. Pankanti, J. Payne, Visual Item Verification for Fraud Prevention in Retail Self-Checkout, IEEE Workshop on Applications of Computer Vision (WACV)2011. 585 590.

[5] J. Connell, Q. Fan, P. Gabbur, N. Haas, S. Pankanti, H. Trinh, Retail video analytics: an overview and survey, Proceedings of the SPIE Video Surveillance and Transportation Imaging Applications 2013, p. 8663.

[6] R.L. DiLonardo, The economic benefit of electronic article surveillance, in: R.V. Clarke (Ed.). Situational Crime Prevention: Successful Case Studies. 2. Harrow and Heston. Guilderland, NY 1997, pp. 122–131

[7] R.L. DiLonardo, R.V. Clarke, Reducing the rewards of shoplifting: an evaluation of ink tags, Security Journal 7 (1) (1996) 11–14.

[8] Y. Gerchak, R. Vickson, M. Parlar, Periodic review production models with variable yield and uncertain demand, IIE Transactions 20 (1988) 144–150.

[9] L. Hand, EAS study: shrinkage reduced with minimal cost, White Paper, Tyco/IDC Retail Insights #GRI241533, 2013, June.

[10] H.S. Heese, Inventory record inaccuracy and RFID adoption, Production and Operations Management 16 (5) (2007) 542–553.

[11] E.E. Houseman, B. Lipstein, Observation and audit techniques for measuring retail sales, Agricultural Economics Research 12 (3) (1960) 61–70.

[12] K. Inderfurth, Analytical solution for a single-period production-inventory problem with uniformly distributed yield and demand, Central European Journal of Operations Research 12 (2004) 117–127.

[13] Kroger, RFID and AIDC News: New Kroger Bar Code Scan Tunnel Could Revolutionize Retail Checkout. Retail-it.info, 2011, January. 13.

[14] S. Mauw, S. Piramuthu, A PUF-based authentication protocol to address ticketswitching of RFID-tagged items, Proceedings of the 8th International Workshop on Security and Trust Management (STM), Springer LNCS 7783 2012, pp. 209–224.

[15] R. McMillan, Tech. exec. built stolen ‘Legoland’ in \$2 M home, Wired 25 (2012, May).

[16] W.H. Motes, S.B. Castleberry, A longitudinal field test of stockout effects on multibrand inventories, Journal of the Academy of Marketing Science 13 (4) (1985) 54–68.

[17] D. Papakiriakopoulos, K. Pramatari, G. Doukidis, A decision support system for detecting products missing from the shelf based on heuristic rules, Decision Support Systems 46 (3) (2009) 685–694.

[18] S. Piramuthu, P. Farahani, M. Grunow, RFID-generated traceability for contaminated product recall in perishable food supply networks, European Journal of Operational Research 225 (2) (2013) 253–262.

[19] S. Piramuthu, S. Wochner, M. Grunow, Should retail stores also RFID-tag ‘cheap’ items? European Journal of Operational Research 233 (1) (2014) 281–291.

[20] E. Schuman, Wal-Mart stung in \$1.5 million bar-code scam, eWeek (2005, January 5).

[21] J. Shapland, Preventing retail-sector crimes, in: M. Tonry, D. Farrington (Eds.), Building a Safer Society Strategic Approaches to Crime Prevention, Crime and Justice., vol. 19, University of Chicago Press, 1995.

[22] A. Veinott, Optimal policy for a multi-product, dynamic, nonstationary inventory problem, Management Science 12 (3) (1965) 206–222.

[23] S. Whang, Timing of RFID adoption in a supply chain, Management Science 56 (2) (2010) 343–355.

[24] C.A. Yano, H.L. Lee, Lot sizing with random yields: a review, Operations Research 43 (2) (1995) 311–334.

[25] W. Zhou, S. Piramuthu, Preventing ticket-switching of RFID-tagged items in apparel retail stores, Decision Support Systems 55 (3) (2013, June) 802–810.

[26] W. Zhou, S. Piramuthu, Effect of ticket-switching on inventory and shelf-space allocation. Decision Support Systems 69 (2015).31-39

[27] A. Zimmerman, As shoplifters use high-tech scams, retail losses rise, Wall Street Journal (2006 October 25) A1

Wei Zhou is an associate professor of information systems at ESCP-Europe in Paris and a member of the RFID European Lab in Paris. He received his Ph. D. in Information Systems from the University of Florida. His research interests include RFID-enabled item-level information visibility, Internet advertising, and knowledge-based learning systems. His work has appeared in Decision Support Systems, European Journal of Information Systems. European Journal of Operational Research, IEEE Transactions on Geosciences and Remote Sensing, International Journal of Electronic Commerce, and Optical Engineering.

Selwyn Piramuthu is professor of information systems at the University of Florida and a member of the RFID European Lab in Paris. His interests include RFID/IoT systems, data an alytics, and recommender systems.
