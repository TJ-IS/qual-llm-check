---
otero_id: 1522
otero_key: "JZ7MQ9XP"
title: "A production-inventory model of imperfect quality products in a three-layer supply chain"
authors: "Shib Sankar Sana"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.11.012"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A production-inventory model of imperfect quality products in a three-layer supply chain

Shib Sankar Sana ⁎

Department of Mathematics, Bhangar Mahavidyalaya, University of Calcutta, Bhangar-743502, 24PGS (South), West Bengal, India

a r t i c l e i n f o

Article history: Received 4 November 2010 Accepted 6 November 2010 Available online 11 November 2010

AMS mathematics subject classification: 90B05

Keywords: Inventory Supply chain Imperfect Production

## a b s t r a c t

In this paper an integrated production-inventory model is presented for supplier, manufacturer and retailer supply chain, considering perfect and imperfect quality items. This model considers the impact of business strategies such as optimal order size of raw materials, production rate and unit production cost, and idle times in different sectors on collaborating marketing system. The model can be used in industries like textile and footwear, chemical, food, etc. An analytical method is employed to optimize the production rate and raw material order size for maximum expected average pro<sup>fi</sup>t. An example is illustrated to study the behavior and application of the model.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

Researchers as well as practitioners in manufacturing industries have given importance to develop inventory control problems in supply chain management. Speci<sup>fi</sup>cally, the competitive framework stipulates that <sup>fi</sup>rms tend to emphasize certain competitive dimensions and develop manufacturing capabilities to achieve the chosen dimensions to enhance their market position. The competitive dimensions are cost, quality, delivery and <sup>fl</sup>exibility. These dimensions relate to production process and control, technology, capacity, facilities, workforce, planning, etc. This research assesses the impact of product rate, production run time, idle time of the systems, inventory level and order <sup>fi</sup>ll rates. Order <sup>fi</sup>ll rate is de<sup>fi</sup>ned as order <sup>fi</sup>lled complete as a fraction of the total number of orders. In traditional economic order quantity (EOQ) and economic production quantity (EPQ) model, all items are perfect. It is common to all industries that a certain percent of produced/ordered items are non-conforming (imperfect) quality. Among other researchers, Salameh and Jaber [31] developed an inventory model which accounted for imperfect quality items using the EPQ/EOQ formulae. They assumed defective items are sold as a single batch at the end of the total screening process. Cardenas-Barron [4] made a correction of the formula in Salameh and Jaber's [31] model and showed that the error only effects the optimum value of the order size. Goyal and Cardenas-Barron [15] extended Salameh and Jaber's [31] model and proposed a practical approach to determine EPQ for items with imperfect quality. Goyal et al. [17] investigated the model of Goyal and Cardenas-Barron [15], considering vendor–buyer integration. Chung and Hou [12] developed a model to obtain an optimal run time for a deteriorating production system with shortages. Yu et al. [45] generalized the models of Salameh and Jaber [31], considering deterioration and partial backordering. They showed in their study that the in<sup>fl</sup>uence of imperfect quality, deterioration and partially backordering were signi<sup>fi</sup>cant in the supplier selection.

Zang and Gerchak [46] considered a joint lot sizing and inspection policy with a random proportion of defective units where the defective units were replaced by non-defective ones. Liu and Yang [26] investigated a single stage production system with imperfect process delivering two types of defects: reworkable and non-reworkable items. The reworkable items are sent for reworking, whereas non-reworkable items are immediately discarded from the system. They determined the optimal lot size that maximized the expected total pro<sup>fi</sup>t over the expected time length of the production cycle. Konstantaras et al. [25] developed a production-inventory model for defective items: sell them to a secondary shop as a single batch and at a price lower to that of new ones, or rework them at some cost to restore its original quality. Huang [21] studied the model of Salameh and Jaber [31] in an integrated production and shipping context; while Wee et al. [40] and Eroglu and Ozdemir [13] extended it independently, allowing shortages. Maddah and Jaber [28] analyzed the effect of screening speed and variability of the supply process on the order quantity, and showed the order quantity in their model was larger than that of the classical EOQ (economic order quantity) model when the variability of the yield rate was reasonable low. Cardenas-Barron [6] presented a simple derivation to <sup>fi</sup>nd out optimal manufacturing batch size with rework process at single stage production system. Cardenas-Barron [7] developed an EPQ model with planned backorders for determining the production lot size and the size of backorders in an imperfect production process where all defective items were reworked at the same cycle. In practical production environments, the imperfect quality items could be reworked and repaired (Sana and Chaudhuri [34]; Sana [32,33]; Sarkar et al. [35]); hence, overall production-inventory costs can be reduced signi<sup>fi</sup>cantly (Hayek and Salameh [18]; Chiu [9]; Chiu et al. [10,11]).

Generally speaking, a good management is trying to align and coordinate the business process and activities of the channel members to improve the overall performance and effectiveness of supply chain. All steps from supply of raw materials to <sup>fi</sup>nished products can be included into a supply chain, connecting raw materials supplier, manufacturer, retailer and <sup>fi</sup>nally customers. Supply chain coordination depends on the development and implementation of various strategies to ensure better supply chain performance in terms of cost, timely supply, quantity discount, buyback/return policies, quantity <sup>fl</sup>exibility, commitment of purchase quantity, <sup>fi</sup>ll rate order size, etc. Weng [41] considered both all unit and incremental quantity discount policy under price sensitive demand. He showed the bene<sup>fi</sup>t for the buyer and supplier by maximizing the supplier's pro<sup>fi</sup>t and the joint pro<sup>fi</sup>t respectively. Lu [27] obtained a heuristic solution for the single vendor multiple buyer problem. Goyal [14] incorporated a policy where size of successive shipments from manufacturer to customer within a production cycle increased by a factor equal to the ratio of production rate and the demand rate. Goyal and Gunasekaran [16] developed an integrated production-inventory-marketing model for determining the EPQ (economic production quantity) and EOQ for raw materials in a multi-stage production system. This model considered the effect of different marketing policies such as the price per unit product and the advertisement frequency on the demand of a perishable item. Aderohunmu et al. [1] achieved cost savings of both the vendor and buyer when they followed a cooperative batching policy and shared cost information along with other information in time. Banerjee and Kim [2] developed an integrated inventory model of the buyer, manufacturer and the raw materials supplier in a JIT (Just-in-Time) environment. Thomas and Gri<sup>fi</sup>n [36] observed that ef<sup>fi</sup>cient supply chain management requires planning and coordination among the various channel members including manufacturers, retailers and intermediaries if any. Hill [19] discussed a generalized policy for <sup>fi</sup>nding the value of the factor by which to increase the shipment sizes. According to Narasimhan and Carter [30], a wellintegrated supply chain involves coordinating the <sup>fl</sup>ows of materials and information between suppliers, manufacturers and customers. Hill [20] derived a global optimal batching and shipment policy for single vendor and single buyer integrated problem, combining increasing shipment size policy of Goyal [14] and an equal shipment size policy. Munson and Rosenblatt [29] extended two level supply chain to a three level supply chain, considering a supplier, a manufacturer and a retailer where manufacturer was a dominant member in the channel. Yang and Wee [43] developed a three-stage supply chain model, integrating producer, distributor and retailer. They showed that integrated approach results in a signi<sup>fi</sup>cant cost reduction compared to the independent decision making by each individual entity of the chain. Woo et al. [42] derived an optimal investment and replenishment decisions for both vendor and buyer by reducing joint ordering cost. Boyaci and Gallego [3] focused on inventory and pricing policies that maximized the pro<sup>fi</sup>t of the channel consisting of one wholesaler and one or more retailers under deterministic price sensitive customer demand. Khouja [24] assumed three coordination mechanisms between the members of the supply chain and showed that some coordination mechanisms lead to signi<sup>fi</sup>cant reduction in total cost. Cardenas-Barron [5] extended the model of Khouja [24] by algebraic method, considering n-stage multi-customer supply chain inventory system. Viswanathan and Wang [38] investigated single vendor–buyer distribution channel coordination, incorporating quantity discount and volume discount. It is common to all enterprises that inventory reductions and cost savings can be reached by implementing collaborative initiatives such as vendor managed inventory (VMI), continuous replenishment, and just-in-time purchasing that allow for information sharing and integration among the enterprises in the supply chain. In this direction, Yao et al. [44] developed an analytical model that helps to provide a better understanding of how important supply chain parameters, namely ordering costs and carrying charges, affect the inventory cost savings. van der Vlist et al. [37] extended the model of Yao et al. [44] with the delivery costs. This extended model is referred to as Yao <sup>+</sup>. In the model of Chaharsooghi et al. [8], the supply chain ordering management (SCOM) problem has been addressed. They proposed <sup>fi</sup>rst an agent-based supply chain ordering management in which agents manage ordering system of decentralized supply chain, in an integrated manner. In the next, they modeled SCOM as a reinforcement learning problem. They showed also that their proposed model is ef<sup>fi</sup>cient and can <sup>fi</sup>nd good policies under complex scenarios where analytical solutions are not available. The note of Wang et al. [39] investigated a paper by Yao et al. [44] and a critique by van der Vlist et al. [37]. According to them, their conclusions about the buyer's order sizes seem to con<sup>fl</sup>ict with each other. Their paper summarized the factors that must be stated clearly to resolve the con<sup>fl</sup>ict and to avoid the confusion. Huang and Ye [22] resolved the disagreement between Yao et al. [44] and van der Vlist et al. [37] without extra assumptions and special cases. They provided also an intuitive view of the cost functions so that most optimal quantities could be derived from the properties of the EOQ model. Jalbar et al. [23] investigated a multi-echelon inventory system in which one vendor supplies an item to multiple buyers. They formulated the problem in terms of integer-ratio policies and developed a heuristic procedure also.

The proposed model considers a three-layer supply chain involving supplier, manufacturer and retailer who are responsible for performing the raw materials into <sup>fi</sup>nished product and make them available to satisfy customers' demand in time. Inventory and production decisions are made at the supplier, manufacturer and retailer levels. The problem is to coordinate production and inventory decisions across the supply chain so that the total expected pro<sup>fi</sup>t of the chain is maximized.

The rest of the paper is organized as follows: Section 2 provides fundamental assumptions and notation. Section 3 describes the formulation of the model. Numerical examples are illustrated in Section 4. Section 5 concludes the paper. A list of references is also provided.

## 2. Fundamental assumptions and notation

The following assumptions and notation are considered to develop the model:

## Assumptions:

1. Model is developed for single item products.

2. Lead time is negligible.

3. Demand rate is constant.

4. Replenishment rate of manufacturer is instantaneously in<sup>fi</sup>nite but it's size is <sup>fi</sup>nite.

5. Production rate is a decision variable.

6. Unit production cost is a function of production rate.

7. Joint effect of supplier, manufacturer and retailer is considered in a supply chain management.

8. Defective items at supplier and manufacturer are considered which follow different probability distribution functions.

9. Cost of Idle times at supplier and manufacturer are also assumed.

## Notation:

R Replenishment lot size of supplier.

P Production rate of manufacturer that is equal to the demand rate at supplier, i.e., replenishment rate of manufacturer.

α Proportional probability of defective items at supplier with probability density function f(α). $A _ { s }$ Set up cost of supplier. $r _ { s }$ Screening rate per unit time at supplier. $S _ { s }$ Screening cost per unit item at supplier. $h _ { s }$ Holding cost per unit per unit time at supplier. $I _ { s }$ Cost per unit idle time of supplier. $C _ { s }$ Purchasing cost per unit item of supplier. $w _ { s }$ Selling price per unit good item at supplier. $\tilde { w } _ { s }$ Selling price per unit defective item of supplier. $E ( x )$ Expectation of variable x. $A P S$ Average pro<sup>fi</sup>t of supplier. $E A P S$ Expected average pro<sup>fi</sup>t of supplier. $\beta$ Proportional probability of defective items at manufacturer with probability density function $g ( \beta )$ $A _ { m }$ Set up cost of manufacturer. $r _ { m }$ Screening rate per unit time at manufacturer. $S _ { m }$ Screening cost per unit item at manufacturer. $h _ { m }$ Holding cost per unit per unit time at manufacturer. $I _ { m }$ Cost per unit idle time of manufacturer. $C ( P )$ Production cost per unit item. $w _ { m }$ Selling price per unit good item of manufacturer. $\tilde { w } _ { m }$ Selling price per unit defective item of manufacturer. $A P M$ Average pro<sup>fi</sup>t of manufacturer. EAPM Expected average pro<sup>fi</sup>t of manufacturer. $D _ { c }$ Demand rate of the customers. $D _ { r }$ Demand rate of retailer. $A _ { r }$ Set up cost of the retailer. $h _ { r }$ Holding cost per unit per unit time at retailer. $w _ { r }$ Selling price per unit item of retailer. $A P R$ Average pro<sup>fi</sup>t of retailer. EAPR Expected average pro<sup>fi</sup>t of retailer. $T$ Cycle length of retailer.

## 3. Formulation of the model

In the proposed model, supplier supplies the raw materials at rate P to the manufacturer up to production run time $t _ { 1 } .$ . The defective items at supplier are sent back after completion of inspection at one lot with sales price $\tilde { w } _ { s }$ per unit item to the outside supplier where the raw materials are purchased. The manufacturer meets the demand of retailer at a rate $D _ { r }$ up to time kT (kb1). During production run time $( 0 , t _ { 1 } ) .$ , inventory of good items piles up with rate $[ ( 1 - \beta ) P - D _ { r } ]$ The accumulated inventory $[ ( 1 - \beta ) P - D _ { r } ] t _ { 1 }$ satis<sup>fi</sup>es the demand of retailer during $[ t _ { 1 } , k T ]$ . The defective items $\beta P$ are accumulated at time $t _ { 1 }$ those are sold at a lower price in one lot. So, inventory cost for defective items up to time $t _ { 1 }$ is considered. The demand of customers is met with rate $D _ { c }$ by retailer where the supply rate of manufactured items is continued up to time kT. The accumulated inventory at time kT is $( D _ { r } - D _ { c } ) K T$ that satis<sup>fi</sup>es the demand for the period [kT,T] (see Fig. 1). The governing differential equations at supplier, manufacturer and retailer are as follows:

## 3.1. Supplier's individual average profit

$Q _ { s } ( t )$ is an inventory of good items. In this case, the lot size R is screened with rate $r _ { s }$ at cost $S _ { s }$ per unit item, after completion of screening, the total defective items are sent back to the vendors where supplier purchased at a price $\tilde { w } _ { s }$ per unit item. The governing differential equation, in this stage, is

$$
\frac {d Q _ {s} (t)}{d t} = - P, 0 \leq t \leq t _ {1}\tag{1}
$$

$$
\text { with } Q _ {s} (0) = (1 - \alpha) R \text { and } Q _ {s} (t _ {1}) = 0.
$$

From Eq. (1), we have

$$
Q _ {s} (t) = (1 - \alpha) R - P t, 0 \leq t \leq t _ {1}.\tag{2}
$$

Now, $Q _ { s } ( t _ { 1 } ) = 0$ implies

$$
t _ {1} = \frac {(1 - \alpha) R}{P}.\tag{3}
$$

The inventory cost of good items is

$$
\begin{array}{c} h _ {s} \int_ {0} ^ {t _ {1}} Q _ {s} (t) d t = h _ {s} \int_ {0} ^ {t _ {1}} \{(1 - \alpha) R - P t \} d t \\ = h _ {s} \bigg \{(1 - \alpha) R t _ {1} - \frac {1}{2} P t _ {1} ^ {2} \bigg \} \\ = \frac {1}{2} h _ {s} \frac {(1 - \alpha) ^ {2} R ^ {2}}{P}. \end{array}
$$

The inventory cost of defective items is

$$
h _ {s} \alpha R \left(\frac {R}{r _ {s}}\right) = \frac {h _ {s} \alpha R ^ {2}}{r _ {s}}.
$$

The screening cost is $S _ { c } R .$ The income from selling the good and defective items is

$$
(w _ {s} (1 - \alpha) R + \tilde {w} _ {s} \alpha R).
$$

The purchasing cost of R items is $C _ { s } R .$

$$
A _ {s}.
$$

The cost for idle time is $I _ { s } ( T - t _ { 1 } ) .$

The average pro<sup>fi</sup>t of supplier is, using $\begin{array} { r } { t _ { 1 } = \frac { ( 1 - \alpha ) R } { P } , } \end{array}$

$$
\begin{array}{l} A P S = \frac {1}{T} \left[ w _ {s} (1 - \alpha) R + \tilde {w} _ {s} \alpha R - A _ {s} - h _ {s} \left\{\frac {(1 - \alpha) ^ {2} R ^ {2}}{2 P} + \frac {\alpha R ^ {2}}{r _ {s}} \right\} - (S _ {s} + C _ {s}) R - I _ {s} (T - t _ {1}) \right] \\ = \frac {1}{T} \left[ w _ {s} (1 - \alpha) R + \tilde {w} _ {s} \alpha R - A _ {s} - h _ {s} \left\{\frac {(1 - \alpha) ^ {2} R ^ {2}}{2 P} + \frac {\alpha R ^ {2}}{r _ {s}} \right\} - (S _ {s}, C _ {s}) R - I _ {s} \left(T - \frac {(1 - \alpha) R}{P}\right) \right]. \end{array}\tag{4}
$$

## 3.2. Manufacturer's individual average profit

$Q _ { m } ( t )$ is on-hand inventory of good items. In this stage, manufacturer produces P items per unit time where raw material is supplied with P rate up to the production run time t . Then, the differential equations are:

$$
\begin{array}{l} \frac {d Q _ {m} (t)}{d t} = (1 - \beta) P - D _ {r}, 0 \leq t \leq t _ {1} \\ \text { with } Q _ {m} (0) = 0 \end{array}\tag{5}
$$

and

$$
\frac {d Q _ {m} (t)}{d t} = - D _ {r}, t _ {1} \leq t \leq k T
$$

with $Q _ { m } ( k T ) = 0 .$

6

From Eqs. (5) and (6), we have

$$
Q _ {m} (t) = \{(1 - \beta) P - D _ {r} \} t, 0 \leq t \leq t _ {1}\tag{7}
$$

and $Q _ { m } ( t ) = \{ ( 1 - \beta ) P - D _ { r } \} t _ { 1 } - D _ { r } ( t - t _ { 1 } ) , ~ t _ { 1 } \le t \le k T$ respectively: 8

Now, Q (kT)=0 implies

$$
\begin{array}{l} D _ {r} k T = (1 - \beta) P t _ {1} \\ \text { i.e., } T = \frac {(1 - \alpha) (1 - \beta) R}{D _ {r} k}. \end{array}\tag{9}
$$

The set up cost is $A _ { m } .$

![](/api/attachments/JZ7MQ9XP/fulltext/images/54ae03030b507769a1ad933be155e7647bc794d340fd52fc12802a60acb78a58.jpg)  
Fig. 1. Logistic diagram of the model

The income from selling the good and defective items is

$$
\{w _ {m} (1 - \beta) P t _ {1} + \tilde {w} _ {m} \beta P t _ {1} \} = \bigg (w _ {m} + \tilde {w} _ {m} \frac {\beta}{1 - \beta} \bigg) D _ {r} k T.
$$

The screening cost is

$$
S _ {m} P t _ {1} = \frac {S _ {m} D _ {r} k T}{(1 - \beta)}.
$$

The inventory cost of good items is

$$
\begin{array}{l} H G _ {m} = h _ {m} \Big [ \int_ {0} ^ {t _ {1}} Q _ {m} (t) d t + \int_ {t _ {1}} ^ {k T} Q _ {m} (t) d t \Big ] \\ \qquad = h _ {m} \Big [ \int_ {0} ^ {t _ {1}} \{(1 - \beta) P - D _ {r} \} t d t + \int_ {t _ {1}} ^ {k T} \{(1 - \beta) P t _ {1} - D _ {r} t \} d t \Big ] \\ \qquad = h _ {m} \Big [ \frac {1}{2} \{(1 - \beta) P - D _ {r} \} t _ {1} ^ {2} + (1 - \beta) P t _ {1} (k T - t _ {1}) - \frac {1}{2} D _ {r} \Big (k ^ {2} T ^ {2} - t _ {1} ^ {2} \Big) \Big ] \\ \qquad = \frac {1}{2} h _ {m} \bigg (1 - \frac {D _ {r}}{(1 - \beta) P} \bigg) D _ {r} k ^ {2} T ^ {2}. \end{array}
$$

The inventory cost of defective items is

$$
\begin{array}{r l} & H D _ {m} = h _ {m} \bigg [ \int_ {0} ^ {t _ {1}} \beta P (t _ {1} - t) d t + \beta P t _ {1} \bigg (\frac {P}{r _ {m}} \bigg) \bigg ] \\ & \qquad = h _ {m} \bigg [ \frac {1}{2} \beta P t _ {1} ^ {2} + \frac {\beta P ^ {2}}{r _ {m}} t _ {1} \bigg ] \\ & \qquad = h _ {m} \bigg [ \frac {D _ {r} k T \beta}{2 P (1 - \beta) ^ {2}} + \frac {P \beta}{r _ {m} (1 - \beta)} \bigg ] D _ {r} k T. \end{array}
$$

The total production cost is

$$
C (P) P t _ {1} = C (P) \left(\frac {D _ {r} k T}{1 - \beta}\right)
$$

Here, the unit production cost of <sup>fi</sup>nished product is (Sana [32,33])

$$
C (P) = w _ {s} + \delta_ {m} + \frac {L}{P} + \gamma P.
$$

where $w _ { s }$ is the purchasing cost per unit raw material from the supplier which is <sup>fi</sup>xed. $\delta _ { m }$ is the <sup>fi</sup>xed cost per unit <sup>fi</sup>nished product.

(L/P) is the labor/energy cost which is equally distributed over production size (P). γP is the tool/die cost per unit <sup>fi</sup>nished product which is proportional to the size of production rate (P).

The average pro<sup>fi</sup>t of manufacturer is

$$
\begin{array}{c} A P M = \frac {1}{T} \bigg [ \bigg \{w _ {m} + \tilde {w} _ {m} \bigg (\frac {\beta}{1 - \beta} \bigg) \bigg \} D _ {r} k T - A _ {m} - S _ {m} \bigg (\frac {D _ {r} k T}{1 - \beta} \bigg) - \frac {1}{2} h _ {m} \bigg (1 - \frac {D _ {r}}{(1 - \beta) P} \bigg) D _ {r} k ^ {2} T ^ {2} \\ - h _ {m} \bigg \{\frac {D _ {r} k T \beta}{2 P (1 - \beta) ^ {2}} + \frac {P \beta}{r _ {m} (1 - \beta)} \bigg \} D _ {r} k T - C (P) \bigg (\frac {D _ {r} k T}{1 - \beta} \bigg) - I _ {m} (T - t _ {1}) \bigg ]. \end{array}\tag{10}
$$

## 3.3. Retailer's individual average profit

$Q _ { r } ( t )$ is on-hand inventory where manufacturer supply at rate $D _ { r }$ to the retailer up to time kT. After meeting the demand of customers at rate $D _ { c } ,$ inventory piles up with rate $( D _ { r } - D _ { c } )$ up to time kT. The accumulated inventory at time kT depletes and reaches to zero level at time T. Then, the governing differential equations are

$$
\begin{array}{l} \frac {d Q _ {r} (t)}{d t} = D _ {r} - D _ {c}, 0 \leq t \leq k T \\ \text { with } Q _ {r} (0) = 0 \end{array}\tag{11}
$$

and

$$
\begin{array}{l} \frac {d Q _ {r} (t)}{d t} = - D _ {c}, k T \leq t \leq T \\ \text { with } Q _ {r} (T) = 0. \end{array}\tag{12}
$$

From Eqs. (11) and (12), we have

$$
Q _ {r} (t) = (D _ {r} - D _ {c}) t, 0 \leq t \leq k T\tag{13}
$$

and

$$
Q _ {r} (t) = D _ {r} k T - D _ {c} t, k T \leq t \leq T.\tag{14}
$$

Now, $\textstyle Q _ { r } ( T ) = 0$ implies $k = ( D _ { c } / D _ { r } ) < 1$ as $D _ { r } { > } D _ { c }$ . For feasibility of the model, $t _ { 1 } \leq k T < T$ must be satis<sup>fi</sup>ed. As mentioned, kTbT holds as $k { < } 1$ . Now, $t _ { 1 } \leq k T$ implies

$$
\begin{array}{l} t _ {1} \leq \frac {(1 - \beta) P t _ {1}}{D _ {r}} \\ \text {i.e.,} (1 - \beta) P \geq D _ {r} \\ \text {i.e.,} E (1 - \beta) P \geq D _ {r} \end{array}\tag{15}
$$

$$
\begin{array}{l} \text { The   set   up   cost   is } A _ {r}. \\ \text { The   income   from   sales   items   is } w _ {r} D _ {c} T. \\ \text { The   purchasing   cost   is } w _ {m} D _ {c} T. \\ \text { The   inventory   cost   is } \end{array}
$$

$$
\begin{array}{l} H _ {r} = h _ {r} \left[ \int_ {0} ^ {k T} (D _ {r} - D _ {c}) t d t + \int_ {k T} ^ {T} \{(D _ {r} - D _ {c}) k T - D _ {c} (t - k T) \} d t \right] \\ = h _ {r} \left[ \frac {1}{2} (D _ {r} - D _ {c}) k ^ {2} T ^ {2} + D _ {r} k T (T - k T) - \frac {1}{2} D _ {c} \left(T ^ {2} - k ^ {2} T ^ {2}\right) \right] \\ = \frac {1}{2} h _ {r} \left(1 - \frac {D _ {c}}{D _ {r}}\right) D _ {c} T ^ {2}. \end{array}
$$

The average pro<sup>fi</sup>t of retailer is

$$
A P R = \frac {1}{T} \left[ w _ {r} D _ {c} T - A _ {r} - w _ {m} D _ {c} T - \frac {1}{2} h _ {r} D _ {c} \left(1 - \frac {D _ {c}}{D _ {r}}\right) T ^ {2} \right].\tag{16}
$$

## 3.4. Leader–follower relationship

In this case, manufacturer is the leader, supplier and retailer are the followers. The manufacturer offers their followers to (i) buy back of the defective items, (ii) <sup>fi</sup>nite replenishment rates with one time ordering cost, (iii) negotiate purchasing prices, (iv) reckon the idle times of members of the chain and (v) continue their contract of supply at each stage. From $\operatorname { E q . } \left( 1 0 \right)$ , using $t _ { 1 } = ( 1 - \alpha ) R / P , D _ { r } = k D _ { c }$ and $T = ( 1 - \alpha ) ( 1 - \beta ) R / ( D _ { r } k )$ , the expected average pro<sup>fi</sup>t of the manufacturer is

$$
\begin{array}{l} E A P M (R, P) = E [ A P M ] \\ = \left\{w _ {m} + \tilde {w} E \left(\frac {\beta}{1 - \beta}\right) \right\} D _ {c} - S _ {m} D _ {c} E \left(\frac {1}{1 - \beta}\right) - \frac {1}{2} h _ {m} \left\{E (1 - \alpha) E (1 - \beta) \right. \\ \left. - \frac {D _ {r}}{P} E (1 - \alpha) \right\} \left(D _ {c} / D _ {r}\right) R - h _ {m} \left\{\frac {R}{2 P} E (1 - \alpha) E \left(\frac {\beta}{1 - \beta}\right) \right. \\ \left. - \frac {P}{r _ {m}} E \left(\frac {\beta}{1 - \beta}\right) \right\} D _ {c} - \left(w _ {s} + \delta_ {m} + \frac {L}{P} + \gamma P\right) D _ {c} E \left(\frac {1}{1 - \beta}\right) \\ - I _ {m} \left(1 - \frac {D _ {c}}{P} E \left(\frac {1}{1 - \beta}\right)\right) - A _ {m} \left(D _ {c} / R\right) E \left(\frac {1}{1 - \alpha}\right) E \left(\frac {1}{1 - \beta}\right) \\ = Z _ {0 m} + Z _ {1 m} / P + Z _ {2 m} P - Z _ {3 m} - R \left(Z _ {4 m} + Z _ {5 m} / P\right) - Z _ {6 m} / R \end{array} \tag {17}
$$

where

$$
\begin{array}{l} Z _ {0 m} = \left\{w _ {m} + \tilde {w} _ {m} E \left(\frac {\beta}{1 - \beta}\right) \right\} D _ {c} - S _ {m} D _ {c} E \left(\frac {1}{1 - \beta}\right) - (w _ {s} + \delta_ {m}) D _ {c} E \left(\frac {1}{1 - \beta}\right) \\ Z _ {1 m} = - L D _ {c} E \left(\frac {1}{1 - \beta}\right) + I _ {m} D _ {c} E \left(\frac {1}{1 - \beta}\right) \\ Z _ {2 m} = - h _ {m} E \left(\frac {\beta}{1 - \beta}\right) D _ {c} / r _ {m} - \gamma D _ {c} E \left(\frac {1}{1 - \beta}\right) \\ Z _ {3 m} = I _ {m} \\ Z _ {4 m} = \frac {1}{2} h _ {m} (D _ {c} / D _ {r}) E (1 - \alpha) E (1 - \beta) \\ Z _ {5 m} = - \frac {1}{2} h _ {m} D _ {c} \left[ 1 - E \left(\frac {\beta}{1 - \beta}\right) \right] E (1 - \alpha) \\ Z _ {6 m} = A _ {m} D _ {c} E \left(\frac {1}{1 - \alpha}\right) E \left(\frac {1}{1 - \beta}\right) \end{array}
$$

From Eq. (4), using $t _ { 1 } = ( 1 - \alpha ) R / P , D _ { r } = k D _ { c }$ and $T = ( 1 - \alpha ) ( 1 - \beta ) R /$ $( D _ { r } k ) ,$ , the expected average pro<sup>fi</sup>t of the supplier is

$$
\begin{array}{l} E A P S (R, P) = E [ A P S ] \\ \quad = w _ {s} D _ {c} E \left(\frac {1}{1 - \beta}\right) + \tilde {w} _ {s} D _ {c} E \left(\frac {\alpha}{1 - \alpha}\right) E \left(\frac {1}{1 - \beta}\right) - \left(S _ {s} + C _ {s}\right) D _ {c} E \left(\frac {1}{1 - \alpha}\right) E \left(\frac {1}{1 - \beta}\right) \\ \quad - h _ {s} \left\{\frac {R}{2 P} D _ {c} E (1 - \alpha) E \left(\frac {1}{1 - \beta}\right) + \frac {R}{r _ {s}} D _ {c} E \left(\frac {\alpha}{1 - \alpha}\right) E \left(\frac {1}{1 - \beta}\right) \right\} \\ \quad - I _ {s} \left\{1 - \frac {D _ {c}}{P} E \left(\frac {1}{1 - \beta}\right) \right\} - A _ {s} \left(D _ {c} / R\right) E \left(\frac {1}{1 - \alpha}\right) E \left(\frac {1}{1 - \beta}\right) \\ = Z _ {0 s} + Z _ {1 s} / P - Z _ {3 s} - R \left(Z _ {4 s} + Z _ {5 s} / P\right) - Z _ {6 s} / R \end{array} \tag {18}
$$

where

$$
\begin{array}{l} Z _ {0 s} = D _ {c} \bigg \{w _ {s} E \Big (\frac {1}{1 - \beta} \Big) + \tilde {w} _ {s} E \Big (\frac {\alpha}{1 - \alpha} \Big) E \Big (\frac {1}{1 - \beta} \Big) \bigg \} - (S _ {s} + C _ {s}) D _ {c} E \Big (\frac {1}{1 - \alpha} \Big) E \Big (\frac {1}{1 - \beta} \Big) \\ Z _ {1 s} = D _ {c} I _ {s} E \Big (\frac {1}{1 - \beta} \Big) \\ Z _ {3 s} = I _ {s} \\ Z _ {4 s} = \frac {h _ {s}}{r _ {s}} D _ {c} E \Big (\frac {\alpha}{1 - \alpha} \Big) E \Big (\frac {1}{1 - \beta} \Big) \\ Z _ {5 s} = \frac {1}{2} h _ {s} D _ {c} E (1 - \alpha) E \Big (\frac {1}{1 - \beta} \Big) \\ Z _ {6 s} = A _ {s} D _ {c} E \Big (\frac {1}{1 - \alpha} \Big) E \Big (\frac {1}{1 - \beta} \Big). \end{array}
$$

The expected average pro<sup>fi</sup>t of the retailer is

$$
\begin{array}{l} E A P R (R) = E [ A P R ] \\ \qquad = w _ {r} D _ {c} - w _ {m} D _ {c} - \frac {1}{2} h _ {r} R (1 - D _ {c} / D _ {r}) E (1 - \alpha) E (1 - \beta) \\ \qquad - A _ {r} (D _ {c} / R) E \bigg (\frac {1}{1 - \alpha} \bigg) E \bigg (\frac {1}{1 - \beta} \bigg) \\ \qquad = Z _ {0 r} - Z _ {4 r} R - Z _ {6 r} / R \end{array}\tag{19}
$$

where

$$
\begin{array}{l} Z _ {0 r} = (w _ {r} - w _ {m}) D _ {c} \\ Z _ {4 r} = \frac {1}{2} h _ {r} (1 - D _ {c} / D _ {r}) E (1 - \alpha) E (1 - \beta) \\ Z _ {6 r} = A _ {r} D _ {c} E \bigg (\frac {1}{1 - \alpha} \bigg) E \bigg (\frac {1}{1 - \beta} \bigg). \end{array}
$$

For optimum value of EAPM(R,P), $\begin{array} { r } { \frac { \partial E A P M } { \partial R } = 0 = \frac { \partial E A P M } { \partial P } } \end{array}$ give us

$$
R ^ {*} (P) = \left(\frac {Z _ {6 m}}{Z _ {4 m} + Z _ {5 m} / P}\right) ^ {1 / 2}\tag{20}
$$

and

$$
R ^ {* *} (P) = \frac {Z _ {1 m} - Z _ {2 m} P ^ {2}}{Z _ {5 m}}\tag{21}
$$

Now, solving $\boldsymbol { R } ^ { * } ( P ) = \boldsymbol { R } ^ { * * } ( P )$ , we have the optimum values of $\cdot _ { P _ { m } ^ { * } }$ and $R _ { m } .$ Again,

$$
\begin{array}{l} \frac {\partial^ {2} E A P M}{\partial R ^ {2}} = - 2 \frac {Z _ {6 m}}{R ^ {3}} \\ \frac {\partial^ {2} E A P M}{\partial P ^ {2}} = 2 \frac {Z _ {1 m}}{P ^ {3}} - 2 R \frac {Z _ {5 m}}{P ^ {3}} \\ \frac {\partial^ {2} E A P M}{\partial R \partial P} = \frac {Z _ {5 m}}{P ^ {2}} \end{array}
$$

$\begin{array} { r } { \mathrm { I f } \ \frac { \partial ^ { 2 } E A P M } { \partial R ^ { 2 } } < 0 , \frac { \partial ^ { 2 } E A P M } { \partial P ^ { 2 } } < 0 } \end{array}$ and $\begin{array} { r } { \left( \frac { \partial ^ { 2 } E A P M } { \partial R ^ { 2 } } \right) \left( \frac { \partial ^ { 2 } E A P M } { \partial P ^ { 2 } } \right) - \left( \frac { \partial ^ { 2 } E A P M } { \partial P \partial R } \right) ^ { 2 } > 0 } \end{array}$ hold at $( { R _ { m } ^ { * } } , { P _ { m } ^ { * } } )$ satisfying inequality (15), then $E A P M ( { R _ { m } } ^ { * } , { P _ { m } } ^ { * } )$ is maximum. The corresponding maximum expected average pro<sup>fi</sup>ts of supplier, manufacturer and retailer are

$$
\begin{array}{l} E A P S = Z _ {0 s} + Z _ {1 s} / P _ {m} ^ {*} - \frac {1}{R _ {m} ^ {*}} \bigg \{(R _ {m} ^ {*}) ^ {2} (Z _ {4 s} + Z _ {5 s} / P _ {m} ^ {*}) + Z _ {6 s} \bigg \} \\ \qquad = Z _ {0 s} + Z _ {1 s} / P _ {m} ^ {*} - Z _ {3 s} - \Big (\frac {Z _ {4 m} + Z _ {5 m} / P _ {m} ^ {*}}{Z _ {6 m}} \Big) ^ {1 / 2} \bigg \{\frac {(Z _ {4 s} + Z _ {5 s} / P _ {m} ^ {*}) Z _ {6 m}}{Z _ {4 m} + Z _ {5 m} / P _ {m} ^ {*}} + Z _ {6 s} \bigg \}, \\ E A P M = Z _ {0 m} + Z _ {1 m} / P _ {m} ^ {*} + Z _ {2 m} P _ {m} ^ {*} - Z _ {3 m} - 2 \sqrt {Z _ {6 m} (Z _ {4 m} + Z _ {5 m} / P _ {m} ^ {*})} \end{array}
$$

and

$$
\begin{array}{c} E A P R = Z _ {0 r} - \frac {1}{R _ {m} ^ {*}} \Big (Z _ {4 r} (R _ {m} ^ {*}) ^ {2} + Z _ {6 r} \Big) \\ = Z _ {0 r} - \Big (\frac {Z _ {4 m} + Z _ {5 m} / P _ {m} ^ {*}}{Z _ {6 m}} \Big) ^ {1 / 2} \Bigg \{\frac {Z _ {4 r} Z _ {6 m}}{Z _ {4 m} + Z _ {5 m} / P _ {m} ^ {*}} + Z _ {6 r} \Bigg \} \end{array}
$$

3.5. Integrated expected average profit

The integrated expected average pro<sup>fi</sup>t of the supply chain is

$$
\begin{array}{l} E I A P (R, P) = D _ {c} \left[ w _ {s} E \left(\frac {1}{1 - \beta}\right) + \tilde {w} _ {s} E \left(\frac {\alpha}{1 - \alpha}\right) E \left(\frac {1}{1 - \beta}\right) + \tilde {w} _ {m} E \left(\frac {\beta}{1 - \beta}\right) \right. \\ \quad + w _ {r} - \left(S _ {s} + C _ {s}\right) E \left(\frac {1}{1 - \alpha}\right) E \left(\frac {1}{1 - \beta}\right) - S _ {m} E \left(\frac {1}{1 - \beta}\right) + \left(\frac {I _ {s} + I _ {m}}{P}\right) E \left(\frac {1}{1 - \beta}\right) \\ \quad - \frac {h _ {m} P}{r _ {m}} E \left(\frac {\beta}{1 - \beta}\right) - \left(w _ {s} + \delta_ {m}\right) E \left(\frac {1}{1 - \beta}\right) - \frac {L}{P} E \left(\frac {1}{1 - \beta}\right) - \gamma P E \left(\frac {1}{1 - \beta}\right) ] \\ \quad - \left(I _ {s} + I _ {m}\right) - R \left[ h _ {s} D _ {c} \left\{\frac {1}{2 P} E (1 - \alpha) E \left(\frac {1}{1 - \beta}\right) + \frac {1}{r _ {s}} E \left(\frac {\alpha}{1 - \alpha}\right) E \left(\frac {1}{1 - \beta}\right) \right\} \right. \\ \quad + \frac {h _ {m} D _ {c}}{2 D _ {r}} \left\{E (1 - \alpha) E (1 - \beta) - \frac {D _ {r}}{P} E (1 - \alpha) \right\} + \frac {h _ {m} D _ {c}}{2 P} E (1 - \alpha) E \left(\frac {\beta}{1 - \beta}\right) \\ \quad + \frac {1}{2} h _ {r} \left(1 - \frac {D _ {c}}{D _ {r}}\right) E (1 - \alpha) E (1 - \beta) ] - \frac {1}{R} (A _ {s} + A _ {m} + A _ {r}) D _ {c} E \left(\frac {1}{1 - \alpha}\right) E \left(\frac {1}{1 - \beta}\right) \\ = Z _ {0 c} + \frac {Z _ {1 c}}{P} + Z _ {2 c} P - Z _ {3 c} - R (Z _ {4 c} + \frac {Z _ {5 c}}{P}) - \frac {Z _ {6 c}}{R} \\ (2 2) \end{array}
$$

where

$$
\begin{array}{l} Z _ {0 c} = D _ {c} \bigg [ \tilde {w} _ {s} E \Big (\frac {\alpha}{1 - \alpha} \Big) E \Big (\frac {1}{1 - \beta} \Big) + \tilde {w} _ {m} E \Big (\frac {\beta}{1 - \beta} \Big) \\ \qquad + w _ {r} - (S _ {s} + C _ {s}) E \Big (\frac {1}{1 - \alpha} \Big) E \Big (\frac {1}{1 - \beta} \Big) - S _ {m} E \Big (\frac {1}{1 - \beta} \Big) - \delta_ {m} E \Big (\frac {1}{1 - \beta} \Big) \bigg ], \\ Z _ {1 c} = D _ {c} [ (I _ {s} + I _ {m}) - L ] E \Big (\frac {1}{1 - \beta} \Big), \\ Z _ {2 c} = - D _ {c} \bigg [ \frac {h _ {m}}{r _ {m}} E \Big (\frac {\beta}{1 - \beta} \Big) + \gamma E \Big (\frac {1}{1 - \beta} \Big) \bigg ], \\ Z _ {3 c} = (I _ {s} + I _ {m}), \\ Z _ {4 c} = \frac {h _ {s} D _ {c}}{r _ {s}} E \Big (\frac {\alpha}{1 - \alpha} \Big) E \Big (\frac {1}{1 - \beta} \Big) + \frac {h _ {m} D _ {c}}{2 D _ {r}} E (1 - \alpha) E (1 - \beta) + \frac {h _ {r}}{2} \Big (1 - \frac {D _ {c}}{D _ {r}} \Big) E (1 - \alpha) E (1 - \beta), \\ Z _ {5 c} = \frac {h _ {s} D _ {c}}{2} E (1 - \alpha) E \Big (\frac {1}{1 - \beta} \Big) - \frac {h _ {m} D _ {c}}{2} \Bigg \{1 - E \Big (\frac {\beta}{1 - \beta} \Big) \Bigg \} E (1 - \alpha), \\ Z _ {6 c} = (A _ {s} + A _ {m} + A _ {r}) D _ {c} E \Big (\frac {1}{1 - \alpha} \Big) E \Big (\frac {1}{1 - \beta} \Big). \end{array}
$$

Lemma. If $\left( \left( Z _ { 1 c } - Z _ { 2 c } P _ { c } ^ { 2 } \right) / Z _ { 5 c } \right) - \sqrt { \left( Z _ { 6 c } \right) / \left( Z _ { 4 c } + Z _ { 5 c } / P _ { c } \right) } = 0$ has a solution $P ^ { * } \in ( M _ { 1 } , M _ { 2 } )$ , satisfying inequality (15), such that $\tau ( P _ { c } ^ { * } ) { < } 0 ,$ then $E A I P ( R ( P _ { c } ^ { * } ) , P _ { c } ^ { * } )$ is maximum.

Proof. Now, differentiating EAIP(R,P) partially, we have

$$
\begin{array}{l} \frac {\partial}{\partial R} \{E A I P (R, P) \} = - (Z _ {4 c} + Z _ {5 c} / P) + Z _ {6 c} / R ^ {2}, \\ \frac {\partial^ {2}}{\partial P \partial R} \{E A I P (R, P) \} = Z _ {5 c} / P ^ {2}, \\ \frac {\partial^ {2}}{\partial R ^ {2}} \{E A I P (R, P) \} = - 2 Z _ {6 c} / R ^ {3} <   0, \text { because } Z _ {6 c} > 0 \text { and } R > 0, \\ \frac {\partial}{\partial P} \{E A I P (R, P) \} = - Z _ {1 c} / P ^ {2} + Z _ {2 c} + Z _ {5 c} R / P ^ {2}, \\ \frac {\partial^ {2}}{\partial P ^ {2}} \{E A I P (R, P) \} = 2 Z _ {1 c} / P ^ {3} - 2 Z _ {5 c} R / P ^ {3} \end{array}
$$

For optimum values of $\begin{array} { r } { E A I P ( R , P ) , \frac { \partial } { \partial R } \{ E A I P ( R , P ) \} = 0 = \frac { \partial } { \partial P } } \end{array}$ EAIP R; P gives us $R ^ { 2 } { = } Z _ { 6 c } / ( Z _ { 4 c } { + } Z _ { 5 c } / P )$ <sup>f</sup>and $P ^ { 2 } = ( Z _ { 1 c } - Z _ { 5 c } R ) / Z _ { 2 c } ^ { * }$

Since $P ^ { 2 } = ( Z _ { 1 c } - Z _ { 5 c } R ) / Z _ { 2 c }$ implies $R = ( Z _ { 1 c } - Z _ { 2 c } P ^ { 2 } ) / Z _ { 5 c }$ . Also, $\{ \left( Z _ { 1 c } - Z _ { 2 c } P ^ { 2 } \right) / Z _ { 5 c } \} = \sqrt { Z _ { 6 c } / \left( Z _ { 4 c } + Z _ { 5 c } / P \right) }$ . Here, $\begin{array} { r l r } {  { } } & { { } } & { \frac { \partial ^ { 2 } } { \partial P ^ { 2 } } \{ E A I P ( R , P ) \} = } \end{array}$ $2 Z _ { 1 c } / P ^ { 3 } - 2 Z _ { 5 c } R / P ^ { 3 } = 2 \left( Z _ { 1 c } - Z _ { 5 c } R \right) / P ^ { 3 } = 2 Z _ { 2 c } / P < 0$ because $Z _ { 2 c } < 0$ Now,

$$
\begin{array}{r l r} & & {\left(\frac {\partial^ {2} E A I P}{\partial R ^ {2}}\right) \left(\frac {\partial^ {2} E A I P}{\partial P ^ {2}}\right) - \left(\frac {\partial^ {2} E A I P}{\partial R \partial P}\right) ^ {2} = - \frac {4 Z _ {6 c}}{R ^ {3} P ^ {3}} (Z _ {1 c} - Z _ {5 c} R) - \left(\frac {Z _ {5 c}}{P ^ {2}}\right) ^ {2}} \\ & & {= - \frac {1}{P ^ {4} R ^ {3}} \left[ 4 Z _ {2 c} Z _ {6 c} P ^ {3} + Z _ {5 c} ^ {2} R ^ {3} \right].} \end{array}
$$

Again, for feasibility of the model, $w _ { s } < C ( P ) < w _ { m }$ gives us $\gamma P ^ { 2 } - ( w _ { m } -$ $w _ { s } - \delta _ { m } ) P + L < 0$ . This holds if $P { \in } [ M _ { 1 } , M _ { 2 } ]$ where $M _ { 1 } = \ M a x \{ 0 , ( w _ { m } -$ $w _ { s } - \delta _ { m } - \sqrt { \left( w _ { m } - w _ { s } - \delta _ { m } \right) ^ { 2 } - 4 \gamma L ) / 2 \gamma } \up$ and $M _ { 2 } = \ M a x \{ 0 , ( w _ { m } - w _ { s } -$ $\delta _ { m } + \sqrt { ( w _ { m } - w _ { s } - \delta _ { m } ) ^ { 2 } - 4 \gamma L ) / 2 \gamma } \}$ Now, $\begin{array} { r } { \left( \frac { \partial ^ { 2 } E A I P } { \partial R ^ { 2 } } \right) \left( \frac { \partial ^ { 2 } E A I P } { \partial P ^ { 2 } } \right) - \left( \frac { \partial ^ { 2 } E A I P } { \partial R \partial P } \right) ^ { 2 } } \end{array}$ <sup>ð</sup>will be positive if

$$
\begin{array}{l} 4 Z _ {2 c} Z _ {6 c} P ^ {3} + Z _ {5 c} ^ {2} R ^ {3} <   0 \\ \text {i.e.,} \\ - \left[ \frac {Z _ {2 c} ^ {3}}{Z _ {5 c}} P _ {c} ^ {6} - \frac {3 Z _ {1 c} Z _ {2 c} ^ {2}}{Z _ {5 c}} P _ {c} ^ {4} - Z _ {2 c} Z _ {6 c} P _ {c} ^ {3} + \frac {3 Z _ {1 c} ^ {2} Z _ {2 c}}{Z _ {5 c}} P _ {c} ^ {2} - \frac {Z _ {1 c} ^ {3}}{Z _ {5 c}} \right] = \tau (P _ {c}) <   0 \\ \text {for} P _ {c} \in (M _ {1}, M _ {2}). \end{array}
$$

Hence the proof.

3.6. Comparison between Stakelberg approach and integrated expected average profit

Let, $\triangle = T o t a l$ expected average profit by Stakelberg approach− Total expected average profit of integrated approach, then

$$
\begin{array}{l} \triangle = E A I P - (E A P S + E A P M + E A P R) \\ = (Z _ {0 c} - Z _ {0 m}) + \left(\frac {Z _ {1 c}}{P _ {c} ^ {*}} - \frac {Z _ {1 m}}{P _ {m} ^ {*}} - \frac {Z _ {1 s}}{P _ {m} ^ {*}}\right) + \left(Z _ {2 c} P _ {c} ^ {*} - Z _ {2 m} P _ {m}\right) - (Z _ {3 c} - Z _ {3 m} - Z _ {3 s}) \\ \qquad - (Z _ {0 r} + Z _ {0 s}) - 2 \Bigg \{Z _ {6 c} (Z _ {4 c} + Z _ {5 c} / P _ {c} ^ {*}) \Bigg \} ^ {1 / 2} \\ \qquad + \left(\frac {Z _ {4 m} + Z _ {5 m} / P _ {m} ^ {*}}{Z _ {6 m}}\right) ^ {1 / 2} \bigg [ Z _ {6 m} \left(\frac {Z _ {4 s} + Z _ {4 r} + Z _ {5 s} / P _ {m} ^ {*}}{Z _ {4 m} + Z _ {5 m} / P _ {m} ^ {*}}\right) + Z _ {6 s} + Z _ {6 r} + 2 Z _ {6 m} \bigg ] \\ = \left(\frac {Z _ {1 c}}{P _ {c} ^ {*}} - \frac {Z _ {1 m}}{P _ {m} ^ {*}} - \frac {Z _ {1 s}}{P _ {m} ^ {*}}\right) + (Z _ {2 c} P _ {c} ^ {*} - Z _ {2 m} P _ {m} ^ {*}) - 2 \Bigg \{Z _ {6 c} (Z _ {4 c} + Z _ {5 c} / P _ {c} ^ {*}) \Bigg \} ^ {1 / 2} \\ \qquad + \left(\frac {Z _ {4 m} + Z _ {5 m} / P _ {m} ^ {*}}{Z _ {6 m}}\right) ^ {1 / 2}   \bigg [ Z _ {6 m} \left(\frac {Z _ {4 s} + Z _ {4 r} + Z _ {5 s} / P _ {m} ^ {*}}{Z _ {4 m} + Z _ {5 m} / P _ {m} ^ {*}}\right) + Z _ {6 s} + Z _ {6 r} + 2 Z _ {6 m} \bigg ] \end{array}
$$

If $\triangle < 0 ,$ then the total expected average pro<sup>fi</sup>t by Stakelberg approach is more than the total expected average pro<sup>fi</sup>t by integrated approach, otherwise, the total expected average pro<sup>fi</sup>t by integrated approach is more than the total expected average pro<sup>fi</sup>t by Stakelberg approach.

## 4. Numerical example

Example 1. The values of the parameters in appropriate units are considered as follows: $A _ { s } = \ S 4 0 0 , r _ { s } = 1 8 0 , 0 0 0$ units per unit time, $C _ { s } = \$ 25$ per unit, $S _ { s } = \$ 0.5$ per unit, $h _ { s } = \$ 3.0$ per unit per unit time, $I _ { s } = \$ 300$ per unit time, $w _ { s } = \$ 60$ per unit, $\tilde { w } _ { s } = \$ 20$ per unit, $D _ { r } { = } 4 0 0$ units, $A _ { m } = \mathbb { S } 5 0 0 , r _ { m } = 1 7 5 ,$ ,000 units per unit time, $S _ { m } = \mathbb { S } 0 . 5$ per unit, $h _ { m } = \$ 4.$ 0 per unit per unit time, $I _ { m } = \$ 200$ per unit time, $w _ { m } = \$ 100$ per unit, $\tilde { w } _ { m } = \mathbb { S } 6 0$ per unit, $D _ { c } { = } 3 0 0$ units, $A _ { r } = \ S 4 0 0 , h _ { r } = \ S 5 . 0$ per unit per unit time, $w _ { r } { = } \$ 120$ per unit, $\delta _ { m } = \$ 2$ per unit, $\gamma = \mathfrak { S } 0 . 0 1$ per u n i t , $\begin{array} { r } { L = \ S 4 0 0 0 , f ( \alpha ) = \frac { 1 } { 0 . 2 - 0 . 0 3 } , 0 . 0 3 < \alpha < 0 . 2 , g ( \beta ) = \frac { 1 } { 0 . 2 - 0 . 0 4 } } \end{array}$

![](/api/attachments/JZ7MQ9XP/fulltext/images/2d70e066c7302251f87bf47eba7b371a1d51d434f897664ec0603d2e18c01da0.jpg)  
Fig. 2. Comparison between the pro<sup>fi</sup>t by Stakelberg approach and integrated pro<sup>fi</sup>t versus production rate of Example 1. Here, EAIP(R\*, P) denotes expected average pro<sup>fi</sup>t of the chain by integrated approach and EASP(R\*, P) denotes expected average pro<sup>fi</sup>t of the chain by Stakelberg approach.

$0 . 0 4 { < } \mathrm { \beta } { < } 0 . 2 $ . Then, the optimal result for Stakelberg theory is $P _ { m } ^ { * } = 5 2 0 . 2 6$ units, $R ^ { * } { = } 7 0 0 . 1 6$ units, $E A P M ^ { * } = \ S 6 1 8 9 . 7 3 , E A P R ^ { * } =$ \$5382.50, $E A P S ^ { * } = \ S 1 0 , 6 0 4 . 5 0$ and the total pro<sup>fi</sup>t of the chain is \$22, 176.73. The optimal result for integrated/collaborating system is $P _ { c } ^ { * } { = } 5 9 1 . 1 0$ units, $\boldsymbol { R } ^ { * } = 5 5 2 . 8 1$ units and the total pro<sup>fi</sup>t of the chain is $\$ 22,319.40$

Example 2. The values of the parameters in Example 1 are same, except $I _ { s } = 0$ and $I _ { m } = 0$

Then, the optimal result for Stakelberg approach is $ { P _ { m } ^ { * } } = 5 4 5 . 5 3$ units, $\boldsymbol { R } ^ { * } = 7 6 \bar { 5 } . 4 8$ units, $E A P M ^ { * } = \ S 6 2 { \bar { 6 } } 7 . { \bar { 1 } } { \bar { 8 } } , \ E A P R ^ { * } = \ S 5 3 7 4 . 3 1$ $E A P S ^ { * } = \$ 10,699 .90$ and the total pro<sup>fi</sup>t of the chain is \$22,341.49. The optimal result for integrated/collaborating system is $P _ { c } ^ { * } = 6 3 1 . 9 7$ units, $\stackrel { - } { R } ^ { * } = 5 5 1 . 8 7$ units and the total profit of the chain is \$22. 539.90

In Examples 1 and 2, integrated approach is better than the Stakelberg approach as expected average pro<sup>fi</sup>t of the chain by integrated approach is more than the expected average pro<sup>fi</sup>t of the chain (see Fig. 2).

## 5. Conclusion

The joint economic lot sizing problem is growing interest in supply chain management. Several researchers focused on integrated vendor–buyer inventory models and the joint optimization of inventory policies in order to maximize total pro<sup>fi</sup>t for the supply chain. The collaboration between members of a supply chain involves commitment to long-term cooperation, shared costs, joint problem solving and even pro<sup>fi</sup>t sharing. Close cooperation can result in more cost-effective production and distribution as well as faster response to customer demand. Now-a-days, supply chain management has great impact on inventory control problem, as the market of industries becomes more competitive. The objective of this research is to develop a three-layer supply chain involving supplier, manufacturer and retailer. It is assumed that the cycle time at each stage is equal. The cost of idle time of supplier and manufacturer is also considered in their system costs. The inventory lots at each stage are sent to the adjacent downstream stage in unequal shipments. Shipments are sent as soon as they are available/produced and there is no need to wait until a whole lot is available. Also, the defective items at supplier and manufacturer are considered. At each stage, the defective items, after 100% screening test are buyback to their concerned sectors by one lot at a reduced price. The proportion factors of defective items follow a uniform distribution function (Salameh and Jaber [31]). The unit production cost is a function of production rate (Sana [32,33]). Finally, an average expected pro<sup>fi</sup>t function of the manufacturer is maximized by considering the manufacturer as leader (Stakelberg) of the chain and the supplier and retailer are the followers of that chain. The collaborating/integrating pro<sup>fi</sup>t function, combining the pro<sup>fi</sup>t of supplier, manufacturer and retailer, is also maximized. A numerical example is illustrated to test the model. In the numerical example, the integrated pro<sup>fi</sup>t function is more pro<sup>fi</sup>table compared to the pro<sup>fi</sup>t of the whole chain by Stakelberg approach.

The new major contribution of the proposed model are idle times, <sup>fi</sup>nite replenishment rates, variable production rates and effect of imperfect items on the chain compared to the existing literature.

In the proposed model, the author assumes the demand of the members of the chain is constant which is common in this direction, different demand functions could be considered, including nonlinear functional forms. The manufacturer has ignored the machine breakdown which disrupts the continuity of the production. The repairing costs of corrective and preventive maintenance should also be considered, because these costs increase the unit production cost. Another limitation of the model is that the stock out situations in each stage of the chain is neglected which are occur due to uncertainties of the delivery, production and demand of the end customers. Genetic Algorithm could solve the problem by random search techniques, while the proposed solution technique (analytical calculus method) fails to optimize the objective function for arbitrary set of data. Several possible extensions of the present model could constitute future research endeavors in this <sup>fi</sup>eld. One immediate extension could be to investigate the effect of multisupplier and multi-retailer with unequal cycle lengths. It might be interesting to consider the effect that only a percent of imperfect quality products could be reworked by manufacturer and the other scrap items must be eliminated immediately. In order to show the uncertainties, the present model could be extended applying stochastic demand and production rate in each member of the supply chain. These are some topics of ongoing future research, among others.

## Acknowledgements

The author wishes to express his gratitude to the editors and referees for their valuable corrections and suggestions to enhance the clarity of the present article.

## References

[1] R. Aderohunmu, A. Mobolurin, N. Bryson, Joint vendor buyer policy in JIT manufacturing, The Journal of the Operational Research Society 46 (1995) 375–385.

[2] A. Banerjee, L.S. Kim, An integrated JIT inventory model, International Journal of Operations and Production Management 15 (1995) 237–244.

[3] T. Boyaci, G. Gallego, Coordinating pricing and inventory replenishment policies for one wholesaler and one or more geographically dispersed retailers, International Journal of Production Economics 77 (2002) 95–111.

[4] L.E. Cardenas-Barron, Observation on: economic production quantity model for items with imperfect quality [Int. J. Production Economics 64 (2000) 59–64], International Journal of Production Economics 67 (20o0) 201.

[5] L.E. Cardenas-Barron, Optimizing inventory decisions in a multi-stage multicustomer supply chain: a note, Transportation Research. Part E 43 (2007) 647–654.

[6] L.E. Cardenas-Barron, Optimal manufacturing batch size with rework in a singlestage production system — a simple derivation, Computers & Industrial Engineering 55 (2008) 758-765.

[7] L.E. Cardenas-Barron, Economic production quantity with rework process at a single-stage manufacturing system with planned backorders, Computers & Industrial Engineering 57 (2009) 1105–1113.

[8] S.K. Chaharsooghi, J. Heydari, S.H. Zegordi, A reinforcement learning model for supply chain ordering management: an application to the beer game, Decision Support Systems 45 (2008) 949–959.

[9] Y.P. Chiu, Determining the optimal lot size for the <sup>fi</sup>nite production model with random defective rate, the rework process, and backlogging, Engineering Optimization 35 (2003) 427–437.

[10] S.W. Chiu, D.C. Gong, H.M. Wee, The effects of the random defective rate and the imperfect rework process on the economic production quantity model, Japan Journal of Industrial and Applied Mathematics 21 (2004) 375–389.

[11] Y.S.P. Chiu, S.W. Chiu, H.C. Chao, Numerical method for determination of reworking or scraping the defective items in a <sup>fi</sup>nite production rate model, Communications in Numerical Methods in Engineering 22 (2006) 377–386.

[12] K.J. Chung, K.L. Hou, An optimal production run time with imperfect production processes and allowable shortages, Computers & Operations Research 20 (2003) 483–490.

[13] A. Eroglu, G. Ozdemir, An economic order quantity model with defective items and shortages, International Journal of Production Economics 106 (2007) 544–549.

[14] S.K. Goyal, A one vendor multi buyer integrated inventory model: a comment, European Journal of Operational Research 82 (1995) 209–210.

[15] S.K. Goyal, L.E. Cardenas-Barron, Note on: economic production quantity model for items with imperfect quality—a practical approach, International Journal of Production Economics 77 (2002) 85–87.

[16] S.K. Goyal, A. Gunasekaran, An integrated production-inventory-marketing model for deteriorating items, Computers & Industrial Engineering 28 (1995) 755–762.

[17] S.K. Goyal, C.K. Huang, H.K. Chen, A simple integrated production policy of an imperfect item for vendor and buyer, Production Planning & Control 14 (2003) 596–602.

[18] P.A. Hayek, M.K. Salameh, Production lot sizing with the reworking of imperfect quality items produced, Production Planning & Control 12 (2001) 584–590.

[19] R.M. Hill, The single vendor, single buyer integrated production inventory model with a generalized policy, European Journal of Operational Research 97 (1997) 493–499.

[20] R.M. Hill, The optimal production and shipment policy for the single vendor single buyer integrated production inventory problem, International Journal of Production Research 37 (1999) 2463–2475.

[21] C.K. Huang, An optimal policy for a single-vendor single buyer integrated production — inventory problem with process unreliability consideration, International Journal of Production Economics 91 (2004) 91–98.

[22] B. Huang, Z. Ye, The effects of lumpy demand and shipment size constraint: a response to “Revisit the note on supply chain integration in vendor-managed inventory”, Decision Support Systems 48 (2010) 421–425.

[23] B.A. Jalbar, J.M. Gutiérrez, J. Sicilia, Policies for a single-vendor multi-buyer system with <sup>fi</sup>nite production rate, Decision Support Systems 46 (2008) 84–100.

[24] M. Khouja, Optimizing inventory decisions in a multistage multi customer supply chain, Transportation Research. Part E 39 (2003) 193–208

[25] I. Konstantaras, S.K. Goyal, S. Papachristos, Economic ordering policy for an item with imperfect quality subject to the in-house inspection, International Journal of Systems Science 38 (2007) 473–482.

[26] J.J. Liu, P. Yang, Optimal lot-sizing in an imperfect production system with homogeneous reworkable jobs, European Journal of Operational Research 91 (1996) 517–527.

[27] L. Lu, Theory and methodology: a one vendor multi buyer integrated inventory model, European Journal of Operational Research 81 (1995) 312–323.

[28] B. Maddah, M.Y. Jaber, Economic order quantity for items with imperfect quality: revisited, International Journal of Production Economics 112 (2008) 808–815.

[29] L.C. Munson, J.M. Rosenblatt, Coordinating a three level supply chain with quantity discounts, IIE Transactions 33 (2001) 371–384.

[30] R. Narasimhan, J.R. Carter, Linking business unit and material sourcing strategies, Journal of Business Logistics 19 (1998) 155–171.

[31] M.K. Salameh, M.Y. Jaber, Economic production quantity model for items with imperfect quality, International Journal of Production Economics 64 (2000) 59–64.

[32] S.S. Sana, A production-inventory model in an imperfect production process, European Journal of Operational Research 200 (2010) 451-464.

[33] S.S. Sana, An economic production lot size model in an imperfect production system, European Journal of Operational Research 201 (2010) 158–170.

[34] S.S. Sana, K.S. Chaudhuri, AN EMQ model in an imperfect production process, International Journal of Systems Science 41 (2010) 635–646.

[35] B. Sarkar, S.S. Sana, K.S. Chaudhuri, Optimal reliability, production lot size and safety stock in an imperfect production system, International Journal of Mathematics in Operational Research 2 (2010) 467–490.

[36] D.J. Thomas, P.J. Gri<sup>fi</sup>n, Coordinated supply chain management, European Journal of Operational Research 94 (1996) 1–15.

[37] P. van der Vlist, R. Kuik, B. Verheijen, Note on supply chain integration in vendormanaged inventory, Decision Support Systems 44 (2007) 360–365.

[38] S. Viswanathan, Q. Wang, Discount pricing decisions in distribution channels with price sensitive demand, European Journal of Operational Research 149 (2003) 571–587.

[39] W.T. Wang, H.M. Wee, H.S.J. Tsao, Revisiting the note on supply chain integration in vendor-managed inventory, Decision Support Systems 48 (2010) 419–420.

[40] H.M. Wee, J. Yu, M.C. Chen, Optimal inventory model for items with imperfect quality and shortage backordering, Omega 35 (2007) 7–11.

[41] Z.K. Weng, Channel coordination and quantity discounts, Management Science 41 (1995) 1509–1522.

[42] Y.Y. Woo, S.L. Hsu, S. Wu, An integrated inventory model for a single vendor and multiple buyers with ordering cost reduction, International Journal of Production Economics 73 (2001).203–215

[43] C.P. Yang, M.H. Wee, An arborescent inventory model in a supply chain system, Production Planning & Control 12 (2001) 728–735.

[44] Y. Yao, P.T. Evers, M.E. Dresner, Supply chain integration in vendor-managed inventory, Decision Support Systems 43 (2007) 663–674.

[45] J.C.P. Yu, H.M. Wee, J.M. Chen, Optimal ordering policy for a deteriorating item with imperfect quality and partial backordering, Journal of the Chinese Institute of Industrial Engineers 22 (2005) 509–520.

[46] X. Zang, Y. Gerchak, Joint lot sizing and inspection policy in an EOQ model with random yield, IIE Transactions 22 (1990) 41–47.

![](/api/attachments/JZ7MQ9XP/fulltext/images/2958847bb89bcafc0f0bae7e6df0d6d7c2bdbc9887e22e26c1e1c271004b931b.jpg)

Dr. Shib Sankar Sana is currently an Assistant Professor in the Department of Mathematics at Bhangar Mahavidyalaya under the University of Calcutta. He served at the Department of Applied Mathematics, BIT, Mesra, Ranchi as an Associate Lecturer during 1999–2001. His main area of research is the modeling of production planning and inventory control. He has published several papers in the European Journal of Operational Research, International Journal of Production Economics, Computers and Mathematics with Application, Mathematical and Computer Modelling, Applied Mathematics and Computation, American Journal of Mathematical and Management Sciences, International Journal of Systems Science, Far East Journal of

Applied Mathematics, Nonlinear Phenomena in Complex Systems, Advanced Modeling and Optimization, Vietnam Journal of Mathematics, Yugoslav Journal of Operational Research, International Journal of Operational Research, International Journal of Services Operations Management, International Journal of Modeling, Identi<sup>fi</sup>cation and Control, International Journal of Innovative Computing and Application, International Journal of Procurement Management, International Journal of Mathematics and Operations Research, IMA Journal of Management Mathematics, International Journal of Information and Decision Science, Indian Journal of Industrial and Applied Mathematics, International Journal of Management Science and Engineering Management, etc. He is a recipient of the International Einstein Award Icon Achiever by IBC Cambridge, UK, 2009.
