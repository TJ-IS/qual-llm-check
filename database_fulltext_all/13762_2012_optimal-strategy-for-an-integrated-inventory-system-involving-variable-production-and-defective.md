---
otero_id: 13762
otero_key: "VTJZ47U3"
title: "Optimal strategy for an integrated inventory system involving variable production and defective items under retailer partial trade credit policy"
authors: "Hardik N. Soni; Kamlesh A. Patel"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.05.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Optimal strategy for an integrated inventory system involving variable production and defective items under retailer partial trade credit policy

Hardik N. Soni <sup>a,</sup>⁎, Kamlesh A. Patel <sup>b</sup>

<sup>a</sup> Chimanbhai Patel Post Graduate Institute of Computer Applications, Gujarat, Ahmedabad, 380015, India

<sup>b</sup> Mathematics Department, Shri U. P. Arts & Smt. M. G. Panchal Science & Shri V. L. Shah Commerce College, Gujarat, Pilvai, India

## a r t i c l e i n f o

Article history: Received 11 September 2011 Received in revised form 19 April 2012 Accepted 14 May 2012 Available online 23 May 2012

Keywords: Supplier–retailer inventory system Trade credit Defective items Variable production

## a b s t r a c t

This paper investigates an integrated inventory model with variable production rate and price-sensitive demand rate under two-level trade credit. The model considers two-level trade credit policy in which the retailer receives a full trade credit from its supplier, and offers partial trade credit to its customers. It is assumed that an arrival order lot may contain some defective items and the number of defective items is a random variable. This study attempts to offer a best policy for retail price, the replenishment cycle, and the number of shipment from the supplier to the retailer in one production run that aims at maximizing the joint expected total pro<sup>fi</sup>t per unit time. An algorithm is designed to identify the optimum solution of the proposed model. Numerical examples are included to illustrate the algorithmic procedure and the effect of key parameters is studied to analyze the behavior of the model.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Due to globalization of market and increased competition, organizations adopt trade credit policy to boost sales, promote market share, and reduce on-hand stock levels. As a result, trade credit <sup>fi</sup>nancing plays an important role, as it can serve the source of business <sup>fi</sup>nancing after bank or other <sup>fi</sup>nancial institute, in business transactions. In commercial practice, the supplier usually offers a credit period to the retailer such that it allows the retailer to raise the <sup>fl</sup>exibility in capital allocation. Accordingly, inventory models under trade credit have been studied extensively. Goyal [11] <sup>fi</sup>rst derived an economic order quantity (EOQ) model under the conditions of permissible delay in payments. Aggarwal and Jaggi [2] then extended Goyal's model for deteriorating items. Jamal et al. [23] and Chang and Dye [5] extended Goyal [11] to the case for deterioration and allowable shortages. Teng [33] assumed that selling price is not equal to the purchasing price to modify Goyal [11]. Chung and Huang [10] extended Goyal [11] to consider the case that the units are replenished at a <sup>fi</sup>nite rate under permissible delay in payments. Since it is beyond the scope of this paper to discuss all contributions in detail we suggest to refer Soni et al. [30] for a comprehensive and up-to-date review on inventory models under trade credit.

The common characteristic in the above mentioned articles is that the supplier offers a delayed payment period to the retailer, but the retailer fails to offer the delayed payment to its customers, which is quite unrealistic. Huang [16] and Biskup et al. [4] have established an inventory model assuming that the retailer also offers a credit period to the customer which is shorter than the credit period offered by the supplier, in order to stimulate his demand. Huang [17,18] further extended Huang [16] by considering the limited storage space and <sup>fi</sup>nite replenishment rate, respectively. Later, Teng and Goyal [36] proposed a generalized formulation of Huang's models [16,17] and Teng and Chang [35] modi<sup>fi</sup>ed Huang [18] by relaxing the assumption that the trade credit offered by supplier is longer than trade credit offered by retailer. Liao [27] developed an economic production quantity (EPQ) model with non-instantaneous receipt and exponentially deteriorating items under the two-level trade credit policy. Chang et al. [6] modi<sup>fi</sup>ed Liao [27] by relaxing the assumption that the trade credit offered by supplier is longer than trade credit offered by retailer. In reality, the marginal effect of credit period on sales is proportional to the unrealized potential of the market demand. Incorporating this phenomenon, Jaggi et al. [21] formulated an EOQ model under two-level trade credit policy with credit‐linked demand. Thangam and Uthayakumar [38] extended Jaggi et al. [21] for perishable items when demand depends on both selling price and credit period under two-level trade credit policy. Recently, Kreng and Tan [25] developed a production model for a lotsize inventory system with <sup>fi</sup>nite production rate and defective items which involve imperfect quality and scrap items under the condition of two-level trade credit policy. In practice, to reduce non-payment risks, a retailer frequently offers a partial trade credit to its credit risk customer who must pay a portion of the purchase amount at the time of placing an order and then avail a permissible delay on the rest of the outstanding amount. Huang and Hsu [19] developed an EOQ model in which retailer gets full trade credit but offers partial trade to the customer. Teng [34] explored optimal ordering policies for a retailer who offers distinct (i.e. full or partial trade credit) trade credits to its good and bad customers. Notice that the above studies based on twolevel trade credit focused only on the retailer's optimal solution, but not on both parties.

The trade credit concept on an integrated inventory model was initiated by Abad and Jaggi [1]. They considered supplier–retailer integrated system in which the supplier offers trade credit to the retailer; and determines the optimal strategies under non-cooperative and cooperative relationships for both parties. Subsequently, numerous researchers such as Chen and Kang [7,8], Ho et al. [15], Ouyang et al. [28], Teng et al. [37], Yang and Wee [39] have extended integrated inventory model in several different directions. Several interesting articles addressing the issue of supply chain management under variety of conditions are Guardiola et al. [12], Hung et al. [20], Jalbar et al. [22], Kristianto et al. [26], Sana [29], Szmerekovsky et al. [32], Yoon et al. [40], Zhang et al. [41], and others. From literature survey, there are few literatures considering integrated inventory system under two-level trade credit. For instance, Su et al. [31] presented a stylized model to determine the optimal strategy for the integrated supplier–retailer inventory model with credit-linked demand rate under the condition that both the supplier and retailer have adopted a trade credit strategy. They assumed that the retailer obtained a longer trade credit period from the supplier and provides a shorter trade credit period to customers. Generally, high selling price makes a negative impact on a major part of the customers to buy the products. That is, the market demand is inversely related to selling price. Thus, change in price affects the demand, which in turn affects the decisions on production, shipping and inventory policies. In this context, Chen and Kang [9] investigated three models considering the two-level trade credit policy with pricesensitive demand, namely a non-integrated model, integrated model and integrated vendor-buyer model with a negotiation scheme. Re cently, Ho [14] extended Su et al. [31] by relaxing the assumption that the trade credit offered by supplier is longer than trade credit offered by retailer. In [14], demand rate is linked both to the retail price and the credit period offered by the retailer to the customers. In aforesaid integrated inventory models under the two-level trade credit, there are some implicit assumptions like that the <sup>fi</sup>x production rate, and all the items replenished by the retailer are of perfect quality, and so on. However, those assumptions may not be <sup>fi</sup>t for the real environments, and the collaborative problem with two-level trade credit needs to be addressed in a more comprehensive sense.

In this study, we develop a more general integrated supplier–retailer inventory model with a demand rate that is sensitive to the customer's price. We assume that the supplier adopts a full trade credit strategy whereas the retailer adopts a partial trade credit strategy. Besides, the production cost is assumed to be a convex function of the production rate. Additionally, it is assumed that an arrival order lot may contain some defective items and the number of defective items is a random variable. Such considerations make this paper more advantageous as compared to the existing literature. The goal of this research is to determine optimal retail price, the replenishment order, and number of shipment from the supplier to the retailer in one production run in order to maximize the joint expected total pro<sup>fi</sup>t per unit time. An algorithm is developed to determine the optimal solution. The model is illustrated with numerical examples and sensitivity analysis with respect to key parameters is carried out.

## 2. Notation and assumptions

To develop the mathematical model, the following assumptions and notations are used

## 2.1. Assumptions

1. There is a single-supplier and single-retailer and they deal with a single product.

2. The market demand for the item is assumed to be sensitive to the customer's retail price s and is de<sup>fi</sup>ned as $D ( s ) = a s ^ { - b }$ , where a (>0) is a scaling factor and $b ( > 1 )$ is a price elasticity. For notational simplicity, D (s) and D will be used interchangeably in this paper.

3. The capacity utilization, $\rho ,$ is the ratio of the demand rate, $D ,$ to the production rate, K; it is always less than 1. $( { \mathrm { i } } . { \mathsf { e } } . \rho = D / K$ and $\rho { < } 1 )$

4. The same assumption used in Khouja [24] is used here. The unit production cost $\textsf { c } ( K )$ is the convex function of $K .$ That is, $c \ ( K ) =$ $c _ { 0 } + c _ { 1 } / \mathrm { K } + c _ { 2 } \mathrm { K } ,$ , where $c _ { 0 } , c _ { 1 } ,$ , and $c _ { 2 }$ are non-negative real numbers to be set to best <sup>fi</sup>t the estimated unit production cost function. The <sup>fi</sup>xed cost $c _ { 0 }$ can be regarded as the raw material cost whereas $c _ { 1 }$ is the direct cost like labor and energy costs and $c _ { 2 }$ is tool wear and tear cost. For notational simplicity, $c \left( K \right)$ and c will be used interchangeably in this paper (cf. [28]).

5. An arrival may contain some defective items. The number of defective items in an arriving order of size Q is a binomial random variable with parameters Q and $p .$ . Upon arrival of an order, all the items are inspected and defective items in each lot will be returned to the vendor at the time of delivery of the next lot (cf. [3]).

6. Inspection is non-destructive and error-free. The inspection process is considered promptly and gives the retailer the ability to scan an entire lot ef<sup>fi</sup>ciently and effectively. From this perspective, length of inspection period is neglected here (cf. [13])

7. The two-level trade credit policy is adopted. The supplier provides a full trade credit period M to the retailer to settle the entire purchase cost while the retailer offers a partial trade credit period N to its credit-risk customers.

8. Fraction (α) of the purchase cost in which the customer must pay the retailer at the time of placing an order, with $0 { \le } \alpha { \le } 1$ . Hence, (1 − α) is the portion of the purchase cost in which the retailer offers its customer a permissible delay of N periods.

9. Before the settlement of an account, the retailer can use sales revenue to earn the interest with an annual rate Ie up to the end of period M. At time t=M, the credit is settled and the retailer starts to pay the interest at rate Ic for the items in stock. During the period of delayed payment, the supplier has an opportunity interest loss with the annual rate Iv.

10. Shortages are not allowed and lead time is negligible.

11. The system operates for an in<sup>fi</sup>nite planning horizon.

Some additional notations are as follows:

m Number of shipment from supplier to retailer.

s Per unit maximum retail price (MRP) of non-defective items.

For Supplier:

$A _ { s }$ Set-up cost.

$w _ { s }$ Unit treatment cost (include warranty cost) of defective goods. $r _ { I }$ Holding cost rate excluding interest charge per unit per unit time.

For Retailer:

$A _ { r }$ Ordering cost.

$\nu$ Procurement cost per unit item. $( s > \nu > c )$

$r _ { 2 }$ Holding cost rate excluding interest charge per unit per unit time for non-defective item.

$r _ { 3 }$ Holding cost rate excluding interest charge per unit per unit time for defective item $\left( r _ { 3 } < r _ { 2 } \right)$

$p$ Defective rate in an order lot, $p { \in } [ 0 , 1 )$ , a random variable. $f ( p )$ The probability density function (p.d.f.) of p with <sup>fi</sup>nite mean E (p) and variance $V _ { p } ,$ where $E ( p ) = \int _ { 0 } ^ { 1 } p f ( p ) d p$

$c _ { s c }$ The screening cost per unit.

$c _ { t }$ Fix transportation cost per shipment.

$T$ Replenishment cycle time.

$Q$ Order quantity.

$E ( \cdot )$ Expected value operator.

## 3. Mathematical modeling

## 3.1. Model for individual management

In this supplier–retailer problem of defective items, when the retailer places an order of size Q the supplier produces mQ units with a <sup>fi</sup>- nite production rate at one set‐up to reduce the production cost. During the production period, as soon as the <sup>fi</sup>rst Q units have been produced, the supplier will deliver them to the retailer to reduce the inventory holding cost. Subsequently, the supplier makes a delivery on average every $Q ( 1 - E ( p ) ) / D$ units of time until the inventory level drops to zero. In the real world, the defective items may result from imperfect production process and/or damage in transit. Therefore, it is assumed that an arriving order items may contain some defective items with defective rate, $p .$ Upon each arrival of shipment the retailer inspects an entire lot at a <sup>fi</sup>xed cost per unit $\left( c _ { s c } \right)$ . When screening process is completed the defective goods will be discovered and returned to the supplier at the time the next lot is delivered. Note that the length of one cycle for the retailer and the supplier are respectively $Q ( 1 - E ( p ) ) / D = T \mathrm { a n d } m Q ( 1 - E ( p ) ) / D = m T .$

## 3.1.1. Supplier's total profit per unit time

In the production period, when the <sup>fi</sup>rst Q units have been produced, the supplier delivers them to the retailer, and thereafter the supplier makes the delivery on an average of every $( 1 - p ) Q / D$ unit time until the inventory level diminishes to zero. Consequently, the total inventory per cycle for the supplier is

$$
\begin{array}{l} \left[ m Q \left\{\frac {Q}{K} + (m - 1) \frac {(1 - p) Q}{D} \right\} - \frac {m ^ {2} Q ^ {2}}{2 K} \right] - \left\{\frac {(1 - p) Q}{D} Q (1 + 2 + \dots + (m - 1)) \right\} \\ = \frac {m Q ^ {2}}{K} + \frac {m (m - 1) Q ^ {2} (1 - p)}{2 D} - \frac {m ^ {2} Q ^ {2}}{2 K} \end{array}
$$

The supplier's pro<sup>fi</sup>t per production cycle is the composed of revenue, production cost, set-up cost, inventory holding cost, defective item treatment cost and the opportunity cost. These components are evaluated as follows:

(1) Sales revenue=v m Q

(2) Production cost=c m Q

(3) Set-up cost=A (3) Set-up cost=A

(4) Holding cos $\stackrel { = } { \left. \sum \right.} _ { \bf { \Phi } } = c ( r _ { 1 } + I \nu ) m Q ^ { 2 } \left[ \frac { 1 } { K } + \frac { ( m - 1 ) ( 1 - p ) } { 2 D } - \frac { m } { 2 K } \right] $

(5) Defective items treatment cost=w p m Q

(6) Opportunity $\mathtt { c o s t } { = } \nu I \nu m Q M$

Symbolically, the supplier's total pro<sup>fi</sup>t per production cycle can be expressed as:

$$
\begin{array}{l} T P (m, Q) = (v - c) m Q \\ \quad - \left\{ \begin{array}{l} A _ {s} + c (r _ {1} + I v) m Q ^ {2} \left[ \frac {1}{K} + \frac {(m - 1) (1 - p)}{2 D} - \frac {m}{2 K} \right] + w _ {s} p m Q \\ + v I v m Q M \end{array} \right\} \end{array}\tag{1}
$$

Substituting $Q = { \frac { D T } { 1 - E ( p ) } }$ in Eq. (1) then it reduces to

$$
\begin{array}{l} T P (m, T) = \frac {(v - c) m D T}{(1 - E (p))} - A _ {s} - \frac {c (r _ {1} + I v) m D T ^ {2}}{2 (1 - E (p)) ^ {2}} [ (2 - m) \rho + (m - 1) (1 - p) ] \\ \qquad - \frac {w _ {s} p m D T}{(1 - E (p))} - \frac {v I v M m D T}{(1 - E (p))}. \end{array}
$$

Therefore, the total expected pro<sup>fi</sup>t per unit time for the supplier is given by,

$$
\begin{array}{l} T E P S (m, T) = \frac {E [ T P (m , T) ]}{m T} \\ \qquad = \frac {D}{(1 - E (p))} \left[ (v - c) - \frac {c Y T}{2} - w _ {s} E (p) - v I v M \right] - \frac {A _ {s}}{m T} \\ \text { where } Y = \frac {(r _ {1} + I v) [ (2 - m) \rho + (m - 1) (1 - E (p)) ]}{(1 - E (p))}. \end{array}
$$

Therefore, the supplier's problem can be formulated as

Maximize TEPS  m; T

Subject to $K > D$

ð<sup>2</sup>Þ

3.1.2. Retailer's total profit per unit time

Since D is the demand per unit time for non-defective items, and $( 1 - p )$ Q is the quantity of non-defective in each shipment, the length of cycle time approximates $\left( 1 - p \right) { \cal Q } / { \cal D }$ . Hence, the average level for non-defective and defective items is respectively $( 1 - p ) ^ { \bar { 2 } } Q ^ { 2 } / 2 D$ and $p ( 1 - p ) Q ^ { 2 } / D$

The retailer's pro<sup>fi</sup>t per shipping cycle is the composed of revenue, purchase cost, ordering cost, holding cost, screening cost, transportation cost, interest earned and interest charged. These components are evaluated as follows:

(1) Sales revenue=s (1−p) Q

(2) Purchase cost = v Q

(3) Ordering cost = A<sub>r</sub>

(4) Holding cost=[vr (1−p)Q/2+vr pQ](1−p)Q/D

(5) Screening cost $= c _ { s c } \times Q$

(6) Transportation cost = c

Next, based on the values of M and N, two cases viz., $N { \le } M$ and $N { \ge } M$ are to be explored for interest earned and interest charged. The calculation for interest earned (IE) and interest charges (IC) for each case are presented in Appendix A. Symbolically, the retailer's total pro<sup>fi</sup>t per shipping cycle can be expressed as:

$$
\begin{array}{c} T P _ {i} (s, Q) = (s - v) Q - s p Q - A _ {r} - [ v r _ {2} (1 - p) Q / 2 + v r _ {3} p Q ] (1 - p) Q / D \\ - c _ {s c} Q - c _ {t} + I E _ {i} - I C _ {i} \end{array}
$$

where

$$
(I E _ {i}, I C _ {i}) = \left\{ \begin{array}{l l} (I E _ {1}, I C _ {1}), & \text { if } N \leq M \text { and } 0 <   T \leq M - N \\ (I E _ {2}, I C _ {2}), & \text { if } N \leq M \text { and } M - N <   T \leq M \\ (I E _ {3}, I C _ {3}), & \text { if } N \leq M \text { and } T \geq M \\ (I E _ {4}, I C _ {4}), & \text { if } M \leq N \text { and } T \leq M \\ (I E _ {5}, I C _ {5}), & \text { if } M \leq N \text { and } T \geq M \end{array} \right.
$$

Since the defective rate, $p ,$ in a shipping lot is random variable, the total expected pro<sup>fi</sup>t per shipping cycle for the retailer is

$$
\begin{array}{l} T E P _ {i} (s, Q) = (s - v) Q - s Q \int_ {0} ^ {1} p f (p) d p - A _ {r} - v r _ {2} Q ^ {2} / 2 D \int_ {0} ^ {1} (1 - p) ^ {2} f (p) d p \\ \qquad - v r _ {3} Q ^ {2} / D \int_ {0} ^ {1} p (1 - p) f (p) d p - c _ {s c} Q - c _ {t} + I E _ {i} - I C _ {i} \\ T E P _ {i} (s, Q) = (s - v) Q - s Q E (p) - A _ {r} - X Q ^ {2} / 2 D - c _ {s c} Q - c _ {t} + I E _ {i} - I C _ {i} \\ \text { where } X = v r _ {2} \int_ {0} ^ {1} (1 - p) ^ {2} f (p) d p + 2 v r _ {3} \int_ {0} ^ {1} p (1 - p) f (p) d p \\ \qquad = v r _ {2} + 2 v (r _ {2} - r _ {3}) E (p) + v (r _ {2} - 2 r _ {3}) \left([ E (p) ] ^ {2} + V _ {p}\right) > 0, \\ V _ {p} = E \left(p ^ {2}\right) - [ E (p) ] ^ {2}. \end{array}\tag{3}
$$

Substituting $Q = { \frac { D T } { 1 - E ( p ) } }$ in Eq. (3) then it reduces to $T E P _ { i } ( s , T ) =$ $\frac { ( s - v ) D T } { 1 - E ( p ) } - \frac { s D T E ( p ) } { 1 - E ( p ) } - A _ { r } - \frac { X D T ^ { 2 } } { 2 ( 1 - E ( p ) ) } - \frac { c _ { s c } D T } { 1 - E ( p ) } - c _ { t } + I E _ { i } - I C _ { i } .$ : Therefore, the total expected pro<sup>fi</sup>t per unit time for the retailer is given by,

$$
\begin{array}{l} T E P R _ {i} (s, T) = \frac {T E P _ {i} (s , T)}{T} \\ = \frac {(s - v) D}{1 - E (p)} - \frac {s D E (p)}{1 - E (p)} - \frac {A _ {r} + c _ {t}}{T} - \frac {X D T}{2 (1 - E (p))} \\ - \frac {c _ {s c} D}{1 - E (p)} + \frac {I E _ {i}}{T} - \frac {I C _ {i}}{T}. \end{array}\tag{4}
$$

## 3.2. Model for joint management

Once the supplier and retailer have built up long-term cooperative relationship, they will jointly determine the best policy for the mutual bene<sup>fi</sup>ts. Accordingly, the joint expected pro<sup>fi</sup>t per unit time for the integrated system is

$$
Z (m, s, T) = \left\{ \begin{array}{l} Z ^ {(1)} (m, s, T) \text {   if   } N \leq M \\ Z ^ {(2)} (m, s, T) \text {   if   } N \geq M \end{array} \right.\tag{5}
$$

where $Z ^ { ( 1 ) } ( m , s , T )$

$$
= \left\{ \begin{array}{l} Z _ {1} (m, s, T) = T E P S (m, T) + T E P R _ {1} (s, T), \text {   if   } N \leq M \text {   and   } 0 <   T \leq M - N \\ Z _ {2} (m, s, T) = T E P S (m, T) + T E P R _ {2} (s, T), \text {   if   } N \leq M \text {   and   } M - N <   T \leq M \\ Z _ {3} (m, s, T) = T E P S (m, T) + T E P R _ {3} (s, T), \text {   if   } N \leq M \text {   and   } T \geq M \end{array} \right.\tag{6}
$$

$$
Z ^ {(2)} (m, s, T) = \left\{ \begin{array}{l} Z _ {4} (m, s, T) = T E P S (m, T) + T E P R _ {4} (s, T), \text {   if   } M \leq N \text {   and   } T \leq M \\ Z _ {5} (m, s, T) = T E P S (m, T) + T E P R _ {5} (s, T), \text {   if   } M \leq N \text {   and   } T \geq M \end{array} \right.\tag{7}
$$

and

$$
\begin{array}{l} Z _ {1} (m, s, T) = (s - c) D \left[ 1 - \frac {E (p)}{1 - E (p)} \right] \\ - \frac {D}{1 - E (p)} \left[ \frac {(X + c Y) T}{2} + w _ {s} E (p) + v I v M + c _ {s c} \right] - \frac {1}{T} \left[ \frac {A _ {s}}{m} + A _ {r} + c _ {t} \right] \\ + \frac {s I e D}{2} [ T + 2 \alpha (M - T) + 2 (1 - \alpha) (M - T - N) ] \end{array} \tag {8}
$$

$$
\begin{array}{l} Z _ {2} (m, s, T) = (s - c) D \left[ 1 - \frac {E (p)}{1 - E (p)} \right] \\ - \frac {D}{1 - E (p)} \left[ \frac {(X + c Y) T}{2} + w _ {s} E (p) + v I v M + c _ {s c} \right] - \frac {1}{T} \left[ \frac {A _ {s}}{m} + A _ {r} + c _ {t} \right] \\ + \frac {s I e D}{2 T} \left[ \alpha T ^ {2} + 2 \alpha T (M - T) + (1 - \alpha) (M - N) ^ {2} \right] \\ - \frac {v I c D}{2 T} (1 - \alpha) (T + N - M) ^ {2} \end{array} \tag {9}
$$

$$
\begin{array}{l} Z _ {3} (m, s, T) = (s - c) D \left[ 1 - \frac {E (p)}{1 - E (p)} \right] \\ \quad - \frac {D}{1 - E (p)} \left[ \frac {(X + c Y) T}{2} + w _ {s} E (p) + v I v M + c _ {s c} \right] - \frac {1}{T} \left[ \frac {A _ {s}}{m} + A _ {r} + c _ {t} \right] \\ \quad + \frac {s I e D}{2 T} \left[ \alpha M ^ {2} + (1 - \alpha) (M - N) ^ {2} \right] \\ \quad - \frac {v I c D}{2 T} \left[ \alpha (T - M) ^ {2} + (1 - \alpha) (T + N - M) ^ {2} \right] \end{array} \tag {10}
$$

$$
\begin{array}{l} Z _ {4} (m, s, T) = (s - c) D \left[ 1 - \frac {E (p)}{1 - E (p)} \right] \\ - \frac {D}{1 - E (p)} \left[ \frac {(X + c Y) T}{2} + w _ {s} E (p) + v I v M + c _ {s c} \right] - \frac {1}{T} \left[ \frac {A _ {s}}{m} + A _ {r} + c _ {t} \right] \\ + \frac {\alpha s I e D}{2} [ T + 2 (M - T) ] - \frac {(1 - \alpha) v I c D}{2} [ T + 2 (N - M) ] \end{array} \tag {11}
$$

$$
\begin{array}{l} Z _ {5} (m, s, T) = (s - c) D \left[ 1 - \frac {E (p)}{1 - E (p)} \right] \\ \quad - \frac {D}{1 - E (p)} \left[ \frac {(X + c Y) T}{2} + w _ {s} E (p) + v I v M + c _ {s c} \right] - \frac {1}{T} \left[ \frac {A _ {s}}{m} + A _ {r} + c _ {t} \right] \\ \quad + \frac {\alpha s I e D M ^ {2}}{2 T} - \frac {\alpha v I c D}{2 T} (T - M) ^ {2} - \frac {(1 - \alpha) v I c D}{2} [ T + 2 (N - M) ]. \end{array} \tag {12}
$$

It is to be noted that, for <sup>fi</sup>xed m and $s , Z _ { 1 } ( m , s , M - N ) { = } Z _ { 2 } ( m , s ,$ $M - N ) , \ Z _ { 2 } ( m , s , M ) = Z _ { 3 } ( m , s , M )$ and $Z _ { 4 } ( m , s , M ) = Z _ { 5 } ( m , s , M )$ Hence, for <sup>fi</sup>xed m and $s , Z ^ { ( i ) } ( m , s , T )$ is a continuous function on $T { > } 0 ,$ , for i = 1, 2.

## 4. Solution methodology

We pursue Ho's [14] approach to identify the optimum solution. We <sup>fi</sup>rst take the second-order partial derivative of Eq. (5) with respect to m, to obtain

$$
\frac {\partial^ {2} Z (m , s , T)}{\partial m ^ {2}} = \frac {\partial^ {2} Z _ {i} (m , s , T)}{\partial m ^ {2}} = \frac {- 2 A _ {s}}{m ^ {3} T} <   0 (\text { for } i = 1, 2, 3, 4, 5).
$$

The results identify $Z ( m , s , T )$ as a concave function in m for <sup>fi</sup>xed s and T. Thus, the search for the optimal shipment number, $m ^ { * }$ , is reduced to <sup>fi</sup>nding a local optimal solution.

4.1. Determination of the optimal replenishment cycle length T for any given m and s

Case 1. $N { \leq } M .$

For <sup>fi</sup>xed m and s, the <sup>fi</sup>rst-order and second-order partial derivatives of $Z _ { i } ( m , s , T ) ~ ( i = 1 , 2 , 3 )$ with respect to T are as follows:

$$
\frac {\partial Z _ {1} (m , s , T)}{\partial T} = \frac {\bar {A}}{T ^ {2}} - \frac {D}{2} \left[ \frac {(X + c Y)}{1 - E (p)} + s I e \right]\tag{13}
$$

$$
\frac {\partial^ {2} Z _ {1} (m , s , T)}{\partial T ^ {2}} = \frac {- 2 \bar {A}}{T ^ {3}}\tag{14}
$$

$$
\begin{array}{c} \frac {\partial Z _ {2} (m , s , T)}{\partial T} = \frac {1}{T ^ {2}} \left[ \overline {{A}} + \frac {D (1 - \alpha) (M - N) ^ {2} (v I c - s I e)}{2} \right] \\ - \frac {D}{2} \left[ \frac {(X + c Y)}{1 - E (p)} + s I e + (1 - \alpha) v I c \right] \end{array}\tag{15}
$$

$$
\frac {\partial^ {2} Z _ {2} (m , s , T)}{\partial T ^ {2}} = \frac {- 1}{T ^ {3}} \left[ 2 \bar {A} + D (1 - \alpha) (M - N) ^ {2} (\nu I c - s I e) \right]\tag{16}
$$

$$
\begin{array}{r l} \frac {\partial Z _ {3} (m , s , T)}{\partial T} = & \frac {1}{T ^ {2}} \left[ \bar {A} + \frac {D [ \alpha M ^ {2} + (1 - \alpha) (M - N) ^ {2} ] (v I c - s I e)}{2} \right] \\ & - \frac {D}{2} \left[ \frac {(X + c Y)}{1 - E (p)} + v I c \right] \end{array}\tag{17}
$$

$$
\frac {\partial^ {2} Z _ {3} (m , s , T)}{\partial T ^ {2}} = \frac {- 1}{T ^ {3}} \left[ 2 \bar {A} + D \left[ \alpha M ^ {2} + (1 - \alpha) (M - N) ^ {2} \right] (v I c - s I e) \right]\tag{18}
$$

where $\bar { \boldsymbol { A } } = \left[ \frac { \boldsymbol { A } _ { s } } { m } + \boldsymbol { A } _ { r } + \boldsymbol { c } _ { t } \right]$

The necessary condition for $Z _ { 1 } ( m , s , T )$ to be maximized is $\partial Z _ { 1 } ( m , s ,$ $T ) / \partial T = 0 .$ . By solving Eq. (13) for T, we can obtain the unique value of T (denoted by T\*) as

$$
T _ {1} ^ {*} = \sqrt {\frac {2 \bar {A}}{D [ (X + c Y) / (1 - E (p)) + s I e ]}}.\tag{19}
$$

Note that the value of $T _ { 1 } ^ { * }$ is depend on m and s. For notational convenience, we let

$$
\Delta_ {1} = 2 \bar {A} - D \left[ \frac {(X + c Y)}{1 - E (p)} + s I e \right] (M - N) ^ {2}.\tag{20}
$$

Then we have following lemma to describe the property of $\yen 123,456,7$

Lemma 1. For fixed m and s,

(a) If $\varDelta _ { 1 } \leq 0$ then the joint expected profit function $Z _ { 1 } ( m , s , \ T )$ is concave and reaches its maximum at point $T = T _ { 1 } ^ { * }$

(b) $I f \varDelta _ { 1 } > 0$ then the joint expected profit function $Z _ { 1 } ( m , s , T )$ has a maximum value at point $T = M - N .$

Proof. See Appendix B for detail.

Next, the necessary condition for $Z _ { 2 } ( m , s , T )$ to be maximized is $\partial Z _ { 2 } ( m , s , T ) / \partial T = 0$ . By solving Eq. (15) for T, we can obtain the unique value of T (denoted by T\*) as

$$
T _ {2} ^ {*} = \sqrt {\frac {2 \bar {A} + D (1 - \alpha) (M - N) ^ {2} (v I c - s I e)}{D [ (X + c Y) / (1 - E (p)) + \alpha s I e + (1 - \alpha) v I c ]}}.\tag{21}
$$

Note that the value of T\* is depend on m and s.

For notational convenience, we let $\varDelta _ { 1 }$ be de<sup>fi</sup>ned as in Eq. (20) and

$$
\Delta_ {2} = 2 \bar {A} - D \left\{\left[ \frac {(X + c Y)}{1 - E (p)} + \alpha s I e + (1 - \alpha) v I c \right] M ^ {2} - (1 - \alpha) (M - N) ^ {2} (v I c - s I e) \right\}.\tag{22}
$$

Then we have following lemma to describe the property of $Z _ { 2 } ( m , s , T )$

Lemma 2. For fixed m and s,

(a) I $\ C _ { \mathrm { { \Delta } } 2 } { \leq } 0 { \leq } \Delta _ { 1 }$ then the joint expected profit function $Z _ { 2 } ( m , s , T )$ is concave and reaches its maximum at point $T = T _ { 2 } ^ { * }$

(b) $I f \Delta _ { 1 } { < } 0$ then the joint expected profit function $Z _ { 2 } ( m , s , T )$ has a maximum value at point $T = M - N$

(c) If $\ \cdot \ \varDelta _ { 2 } > 0$ then the joint expected profit function $Z _ { 2 } ( m , s , T )$ has a maximum value at point T=M.

Proof. See Appendix C for detail.

Similarly, the necessary condition for $Z _ { 3 } ( m , s ,$ T)to be maximized is $\partial Z _ { 3 } ( m , s , T ) / \partial T = 0$ . By solving Eq. (17) for T, we can obtain the unique value of T (denoted by T\*) as

$$
T _ {3} ^ {*} = \sqrt {\frac {2 \bar {A} + D [ \alpha M ^ {2} + (1 - \alpha) (M - N) ^ {2} ] (v I c - s I e)}{D [ (X + c Y) / (1 - E (p)) + v I c ]}}.\tag{23}
$$

By using similar arguments as earlier, we can easily obtain the following lemma.

Lemma 3. For fixed m and s,

(a) If $\varDelta _ { 2 } \geq 0$ then the joint expected profit function $Z _ { 3 } ( m , s , T )$ is concave and reaches its maximum at point $T = T _ { 3 } ^ { * }$

(b) $I f \ : \Delta _ { 2 } < 0$ then the joint expected profit function $Z _ { 3 } ( m , s , T )$ has a maximum value at point T=M.

We summarize our findings in the next lemma.

Lemma 4. For fixed m and s

(a) $I f \Delta _ { 1 } \leq 0$ then the retailer's optimal replenishment cycle length is $T = T _ { 1 } ^ { * }$

(b) $I f \ \Delta _ { 2 } { \leq } 0 { \leq } \Delta _ { 1 }$ then the retailer's optimal replenishment cycle length is $T = T _ { 2 } ^ { * }$

(c) $I f \varDelta _ { 2 } \geq 0$ then the retailer's optimal replenishment cycle length is $T = T _ { 3 } ^ { * }$

Proof. It immediately follows from the fact $\Delta _ { 1 } > \Delta _ { 2 }$ , Lemmas 1–3, and continuity of $Z ^ { ( 1 ) } ( m , s , T )$ at T=M−N and T=M.

Case 2. M≤N.

For <sup>fi</sup>xed m and s, the <sup>fi</sup>rst-order and second-order partial derivatives of $Z _ { i } ( m , s , T ) ( i = 4 , 5 )$ with respect to T are as follows:

$$
\frac {\partial Z _ {4} (m , s , T)}{\partial T} = \frac {\bar {A}}{T ^ {2}} - \frac {D}{2} \left[ \frac {(X + c Y)}{1 - E (p)} + \alpha s I e + (1 - \alpha) v I c \right]\tag{24}
$$

$$
\frac {\partial^ {2} Z _ {4} (m , s , T)}{\partial T ^ {2}} = \frac {- 2 \bar {A}}{T ^ {3}}\tag{25}
$$

$$
\frac {\partial Z _ {5} (m , s , T)}{\partial T} = \frac {1}{T ^ {2}} \left[ \bar {A} + \frac {\alpha D M ^ {2} (v I c - s I e)}{2} \right] - \frac {D}{2} \left[ \frac {(X + c Y)}{1 - E (p)} + v I c \right]\tag{26}
$$

$$
\frac {\partial^ {2} Z _ {5} (m , s , T)}{\partial T ^ {2}} = \frac {- 1}{T ^ {3}} \left[ 2 \bar {A} + \alpha D M ^ {2} (\nu I c - s I e) \right]\tag{27}
$$

By solving $\partial Z _ { i } ( m , s , T ) / \partial T { = } 0 ( i { = } 4 , 5 )$ the values of T (denoted by T<sub>4</sub>\* and T<sub>5</sub>\*) are respectively as follows:

$$
T _ {4} ^ {*} = \sqrt {\frac {2 \bar {A}}{D [ (X + c Y) / (1 - E (p)) + \alpha s I e + (1 - \alpha) v I c ]}}\tag{28}
$$

$$
\text { and } T _ {5} ^ {*} = \sqrt {\frac {2 \bar {A} + \alpha D M ^ {2} (v I c - s I e)}{D [ (X + c Y) / (1 - E (p)) + v I c ]}}.\tag{29}
$$

For notational convenience, we let

$$
\Delta_ {3} = 2 \bar {A} - D \left[ \frac {(X + c Y)}{(1 - E (p))} + \alpha s I e + (1 - \alpha) v I c \right] M ^ {2}.\tag{30}
$$

Using the analogous arguments as in Case 1, we can easily derive the following result. Therefore, we state the result without proof.

Lemma 5. For fixed m and s

(a) $I f \varDelta _ { 3 } { \leq } 0$ then the retailer's optimal replenishment cycle length is $T = T _ { 4 } ^ { * } .$

(b) $I f \varDelta _ { 3 } > 0$ then the retailer's optimal replenishment cycle length is $T = T _ { 5 } ^ { * } .$

4.2. Determination of the optimal retail price s for any given m

Case 1. $N { \leq } M .$

Lemma 4 indicates that the retailer's optimal replenishment cycle length is $T _ { i } ^ { * } \left( i = 1 , 2 , 3 \right)$ . For <sup>fi</sup>xed m, motivated by Eqs. (20) and (22), we let $g _ { 1 } ( s ) = \Delta _ { 1 }$ and $g _ { 2 } ( s ) = \Delta _ { 2 }$

Since $c = c \left( K \right) = c _ { 0 } + c _ { 1 } / { K } + c _ { 2 }$ K and $K = D / \rho ,$ then g<sub>1</sub>(s) and g<sub>2</sub>(s) can be expressed as

$$
g _ {1} (s) = 2 \bar {A} - a s ^ {- b} \left[ \frac {X}{1 - E (p)} + \left(c _ {0} + \frac {c _ {1} \rho}{a s ^ {- b}} + \frac {c _ {2} a s ^ {- b}}{\rho}\right) \frac {Y}{1 - E (p)} + s I e \right] (M - N) ^ {2}\tag{31}
$$

$$
\begin{array}{l} g _ {2} (s) = 2 \overline {{A}} - a s ^ {- b} \Bigg \{\left[ \frac {X}{1 - E (p)} + \left(c _ {0} + \frac {c _ {1} \rho}{a s ^ {- b}} + \frac {c _ {2} a s ^ {- b}}{\rho}\right) \frac {Y}{1 - E (p)} \right. \\ \left. + \alpha s I e + (1 - \alpha) v I c \right] M ^ {2} - (1 - \alpha) (M - N) ^ {2} (v I c - s I e) \Bigg \}. \end{array}\tag{32}
$$

Lemma 6. For fixed m, let \~s and $\tilde { s } _ { 2 }$ are values for which $g _ { 1 } ( \tilde { s } _ { 1 } ) = 0$ and $g _ { 2 } ( \tilde { s } _ { 2 } ) = 0$ then

(a) $\varDelta _ { 1 } \leq 0$ if and only $i f s \le \tilde { s } _ { 1 }$

(b) $\Delta _ { 2 } { \leq } 0 { \leq } \Delta _ { 1 }$ if and only $i f \tilde { s } _ { 1 } { \le } s { \le } \tilde { s } _ { 2 }$

(c) $\Delta _ { 2 } \ge 0 \ i f$ and only $i f s \ge \tilde { s } _ { 2 }$

Proof. See Appendix D for detail.

From the above Lemma, it follows that there exist unique values $\tilde { s } _ { i }$ $( i = 1 , 2 )$ such that

$$
\begin{array}{l} g _ {1} \left(\tilde {s} _ {1}\right) = 2 \bar {A} - a \tilde {s} _ {1} ^ {- b} \left[ \frac {X}{1 - E (p)} + \left(c _ {0} + \frac {c _ {1} \rho}{a \tilde {s} _ {1} ^ {- b}} + \frac {c _ {2} a \tilde {s} _ {1} ^ {- b}}{\rho}\right) \frac {Y}{1 - E (p)} + \tilde {s} _ {1} I e \right] \\ \times (M - N) ^ {2} = 0 \end{array} \tag {3}\tag{33}
$$

$$
\begin{array}{l} \text { and } g _ {2} (\tilde {s} _ {2}) = 2 \bar {A} - a \tilde {s} _ {2} ^ {- b} \Bigg \{\left[ \frac {X}{1 - E (p)} + \left(c _ {0} + \frac {c _ {1} \rho}{a \tilde {s} _ {2} ^ {- b}} + \frac {c _ {2} a \tilde {s} _ {2} ^ {- b}}{\rho}\right) \frac {Y}{1 - E (p)} \right] M ^ {2} \\ \qquad + \tilde {s} _ {2} l e \Big [ \alpha M ^ {2} + (1 - \alpha) (M - N) ^ {2} \Big ] + (1 - \alpha) v l c \Big [ M ^ {2} - (M - N) ^ {2} \Big ] \Bigg \} = 0. \end{array}\tag{34}
$$

Combining Lemmas 4 and $6 ,$ we have following theorem.

Theorem 1. For any m and s,

(a) $I f s \le \tilde { s } _ { 1 }$ then the retailer's optimal replenishment cycle length is $T = T _ { 1 } ^ { * }$

(b) $I f \tilde { s } _ { 1 } \leq s \leq \tilde { s } _ { 2 }$ then the retailer's optimal replenishment cycle length is $T = T _ { 2 } ^ { * }$

(c) $I f s \geq \tilde { s } _ { 2 }$ then the retailer's optimal replenishment cycle length is $T = T _ { 3 } ^ { * }$

## Proof. It immediately follows from Lemmas 4 and 6.

Consequently, when m and s are known, we can obtain maximum joint total expected pro<sup>fi</sup>t per unit time for Case 1 as follows:

$$
Z ^ {(1)} (m, s) = \left\{ \begin{array}{l} Z _ {1} (m, s), \text {   if   } s \leq \tilde {s} _ {1} \\ Z _ {2} (m, s), \text {   if   } \tilde {s} _ {1} \leq s \leq \tilde {s} _ {2} \\ Z _ {3} (m, s), \text {   if   } s \geq \tilde {s} _ {2} \end{array} \right.\tag{35}
$$

Where

$$
\begin{array}{l} Z _ {1} (m, s) = (s - c) D \left[ 1 - \frac {E (p)}{1 - E (p)} \right] - \frac {D}{1 - E (p)} \left[ w _ {s} E (p) + v I v M + c _ {s c} \right] \\ \quad + s I e D [ \alpha M + (1 - \alpha) (M - N) ] - \sqrt {2 \bar {A} D [ (X + c Y) / (1 - E (p)) -} \end{array}\tag{-sle]}
$$

<sub>ð</sub><sup>36</sup><sub>Þ</sub>

$$
\begin{array}{l} Z _ {2} (m, s) = (s - c) D \left[ 1 - \frac {E (p)}{1 - E (p)} \right] - \frac {D}{1 - E (p)} [ w _ {s} E (p) + v I v M + c _ {s c} ] \\ \quad + D [ \alpha s I e M + (1 - \alpha) v I c (M - N) ] \\ \quad - \sqrt {2 \bar {A} + D (1 - \alpha) (v I c - s I e) (M - N) ^ {2}} \\ \quad \times \sqrt {D [ (X + c Y) / (1 - E (p)) + \alpha s I e + (1 - \alpha) v I c ]} \end{array}\tag{37}
$$

$$
\begin{array}{l} Z _ {3} (m, s) = (s - c) D \left[ 1 - \frac {E (p)}{1 - E (p)} \right] - \frac {D}{1 - E (p)} [ w _ {s} E (p) + v I v M + c _ {s c} ] \\ \qquad + v I c D [ \alpha M + (1 - \alpha) (M - N) ] \\ \qquad - \sqrt {2 \bar {A} + D [ \alpha M ^ {2} + (1 - \alpha) (M - N) ^ {2} ] (v I c - s I e)} \\ \qquad \times \sqrt {D [ (X + c Y) / (1 - E (p)) + v I c ]}. \end{array}\tag{38}
$$

Now, for <sup>fi</sup>xed m, out task is to determine the optimal retail price s which maximizes $Z _ { i } ( m , s ) , ( i = 1 , 2 , 3 )$ . Equivalently, to determine the value of s which satis<sup>fi</sup>es $\partial Z _ { i } ( m , s ) / \partial s = 0$ and $\partial ^ { 2 } Z _ { i } ( \dot { m } , s ) / \partial s ^ { 2 } < 0 ( i = 1 , 2 ,$ 3) for concavity. As a result, we have following trivial theorem similar to [14].

## Theorem 2. For fixed m, we have

(a) If there exist a value $s _ { 1 }$ which satisfies $\partial Z _ { 1 } ( m , s ) / \partial s = 0 , \partial ^ { 2 } Z _ { 1 } ( m , s ) /$ $\partial s ^ { 2 } < 0$ and $\boldsymbol { s } _ { 1 } \le \tilde { { s } } _ { 1 }$ , then $s _ { 1 }$ is the optimal retail price and $Z _ { 1 } ( m , s _ { 1 } )$ is the maximum value o $\because \boldsymbol { Z } ^ { ( 1 ) } ( \boldsymbol { m } , s )$

(b) If there exist a value $s _ { 2 }$ which satisfies $\partial Z _ { 2 } ( m , s ) / \partial s = 0 , \partial ^ { 2 } Z _ { 2 } ( m , s ) /$ $\partial s ^ { 2 } < 0$ and $\tilde { s } _ { 1 } \le s _ { 2 } \le \tilde { s } _ { 2 }$ , then $s _ { 2 }$ is the optimal retail price and $Z _ { 2 } ( m , s _ { 2 } )$ is the maximum value of $Z ^ { ( 1 ) } ( m , s )$

(c) If there exist a value $s _ { 3 }$ which satisfies $\partial Z _ { 3 } ( m , s ) / \partial s = 0 , \partial ^ { 2 } Z _ { 3 } ( m , s ) /$ $\partial s ^ { 2 } < 0$ and $s _ { 3 } \geq \tilde { s } _ { 2 }$ , then s is the optimal retail price and $Z _ { 3 } ( m , s _ { 3 } )$ is the maximum value o $\mathcal { Z } ^ { ( 1 ) } ( m , s )$

Case 2. $M \leq N .$

Proceeding in the same manner as in Case 1, motivated by Eq. (30), for <sup>fi</sup>xed m, we let,

$$
\begin{array}{l} g _ {3} (s) = \Delta_ {3} = 2 \bar {A} - a s ^ {- b} \left[ \frac {X}{1 - E (p)} + \left(c _ {0} + \frac {c _ {1} \rho}{a s ^ {- b}} + \frac {c _ {2} a s ^ {- b}}{\rho}\right) \frac {Y}{1 - E (p)} \right. \\ \left. + \alpha s I e + (1 - \alpha) v I c \right] M ^ {2} \end{array}\tag{39}
$$

$$
\text { as   } c = c (K) = c _ {0} + c _ {1} / K + c _ {2} K \text {   and   } K = D / \rho .
$$

Lemma 7. For fixed m, let ${ \tilde { s } } _ { 3 }$ is the value for which $g _ { 3 } ( \tilde { s } _ { 3 } ) = 0$ then

(a) $\varDelta _ { 3 } \leq 0$ if and only $i f s \le \tilde { s } _ { 3 }$

(b) $\varDelta _ { 3 } \geq 0$ if and only $i f s \geq \tilde { s } _ { 3 }$

Proof. See Appendix E for detail

From the above Lemma, it follows that there exist unique value ${ \tilde { s } } _ { 3 }$ such that

$$
\begin{array}{l} g _ {3} (\tilde {s} _ {3}) = 2 \bar {A} - a \tilde {s} _ {3} ^ {- b} \left[ \frac {X}{1 - E (p)} + \left(c _ {0} + \frac {c _ {1} \rho}{a \tilde {s} _ {3} ^ {- b}} + \frac {c _ {2} a \tilde {s} _ {3} ^ {- b}}{\rho}\right) \frac {Y}{1 - E (p)} \right. \\ \left. + \alpha \tilde {s} _ {3} I e + (1 - \alpha) v I c \right] M ^ {2} = 0. \end{array}\tag{40}
$$

Combining Lemmas 5 and 7, we have following theorem.

Theorem 3. For any m and s,

(a) $I f s \le \tilde { s } _ { 3 }$ then the retailer's optimal replenishment cycle length is $T = T _ { 4 } ^ { * } .$

(b) $I f s \geq \tilde { s } _ { 3 }$ then the retailer's optimal replenishment cycle length is $T = T _ { 5 } ^ { * }$

Consequently, when m and s are known, we can obtain maximum joint total expected pro<sup>fi</sup>t per unit time for Case 2 as follows:

$$
Z ^ {(2)} (m, s) = \left\{ \begin{array}{l} Z _ {4} (m, s), \text {   if   } s \leq \tilde {s} _ {3} \\ Z _ {5} (m, s), \text {   if   } s \geq \tilde {s} _ {3} \end{array} \right.\tag{41}
$$

Where

$$
\begin{array}{l} Z _ {4} (m, s) = (s - c) D \left[ 1 - \frac {E (p)}{1 - E (p)} \right] - \frac {D}{1 - E (p)} [ w _ {s} E (p) + v I v M + c _ {s c} ] \\ \quad + D [ \alpha s I e M - (1 - \alpha) v I c (N - M) ] \\ \quad - \sqrt {2 \bar {A} D [ (X + c Y) / (1 - E (p)) + \alpha s I e + (1 - \alpha) v I c ]} \end{array}\tag{42}
$$

$$
\begin{array}{l} Z _ {5} (m, s) = (s - c) D \left[ 1 - \frac {E (p)}{1 - E (p)} \right] - \frac {D}{1 - E (p)} \left[ w _ {s} E (p) + v I v M + c _ {s c} \right] + v I c D \\ \times [ \alpha M - (1 - \alpha) (N - M) ] - \sqrt {2 \bar {A} + \alpha D M ^ {2} (v I c - s I e)} \\ \times \sqrt {D [ (X + c Y) / (1 - E (p)) + v I c ]}. \end{array} \tag {43}\tag{43}
$$

Next, for <sup>fi</sup>xed m, the value of s which satis<sup>fi</sup>es $\partial Z _ { i } ( m , s ) / \partial s = 0$ and $\partial ^ { 2 } Z _ { i } ( m , s ) / \partial s ^ { 2 } < 0 ( i = 4 , 5 )$ for concavity, maximizes $Z _ { i } ( m , s ) , ( i = 4 , 5 )$ Therefore, we have following trivial theorem similar to [14].

## Theorem 4. For fixed m, we have

(a) If there exist a value $s _ { 4 }$ which satisfies $\partial Z _ { 4 } ( m , s ) / \partial s = 0 , \partial ^ { 2 } Z _ { 4 } ( m , s ) /$ $\partial s ^ { 2 } < 0$ and $S _ { 4 } \leq \tilde { s } _ { 3 } ,$ , then $s _ { 4 }$ is the optimal retail price and $Z _ { 4 } ( m , s _ { 4 } )$ is the maximum value o $f Z ^ { ( 2 ) } ( m , s )$

(b) If there exist a value $s _ { 5 }$ which satisfies $\partial Z _ { 5 } ( m , s ) / \partial s = 0 , \partial ^ { 2 } Z _ { 5 } ( m , s ) /$ $\partial s ^ { 2 } < 0$ and $s _ { 5 } \geq \tilde { s } _ { 3 }$ , then $s _ { 5 }$ is the optimal retail price and $Z _ { 5 } ( m , s _ { 5 } )$ is the maximum value o $\Sigma ^ { ( 2 ) } ( m , s )$ .

Based on the concavity behavior of objective function with respect to the decision variables the following algorithmic procedure, analogous to Ho [14], was developed to identify optimal values for the number of shipment, retail price and replenishment cycle time.

Algorithm:

Step 1: Set $m = 1 , Z ^ { ( 1 ) } ( m , s ) = 0 , \mathrm { a n d } Z ^ { ( 2 ) } ( m , s ) = 0 .$

Step 2: Compare the values of M and N. If $N { \leq } M ,$ , then go to Step 3 otherwise, go to Step 4.

Step 3: Execute Algorithm 1.

## Algorithm 1

Step 1.1: Determine $\tilde { s } _ { 1 } ^ { ( m ) }$ and $\tilde { s } _ { 2 } ^ { ( m ) }$ from Eqs. (33) and (34) respectively.

Step 1.2: Fo $\cdot i = 1 , 2 , \cdot$ 3, obtain $s _ { i } ^ { ( m ) }$ by solving $\partial Z _ { i } ( m , s ) / \partial s = 0$

Step 1.3: $\mathrm { I f } s _ { 1 } ^ { ( m ) } { \le } \tilde { s } _ { 1 } ^ { ( m ) }$ <sup>Þ</sup> and $[ \partial ^ { 2 } Z _ { 1 } ( m , s ) / \partial s ^ { 2 } ] _ { s = s _ { 1 } ^ { ( m ) } } < 0 ,$ then substitute the value $s \bar { \mathrm { f } } ^ { ( m ) }$ into Eqs. (19) and (36) to obtain the values of $T _ { 1 } ^ { ( m ) }$ and $Z _ { 1 } ( m , s )$ respectively. Otherwise, $\yen 123,456$

Step 1.4: I $\textbf { f } \tilde { s } _ { 1 } ^ { ( m ) } { \le } s _ { 2 } ^ { ( m ) } { \le } \tilde { s } _ { 2 } ^ { ( m ) }$ and $[ \partial ^ { 2 } Z _ { 2 } ( m , s ) / \partial s ^ { 2 } ] _ { s = s _ { 2 } ^ { ( m ) } } < 0 ,$ , then substitute the value $s _ { 2 } ^ { ( m ) }$ into Eqs. (21) and (37) to obtain the values of $T _ { 2 } ^ { ( m ) }$ and $Z _ { 2 } ( m , s )$ respectively. Otherwise, set $Z _ { 2 } ( m , s ) = 0$

Step 1.5: $\mathrm { I f ~ } \varsigma _ { 3 } { } ^ { ( m ) } \ge \tilde { s } _ { 2 } { } ^ { ( m ) }$ and $[ \partial ^ { 2 } Z _ { 3 } ( m , s ) / \partial s ^ { 2 } ] _ { s = s _ { 3 } ^ { ( m ) } } < 0 ,$ , then substitute the value $s _ { 3 } ^ { ( m ) }$ into Eqs. (23) and (38) to obtain the values of $T _ { 3 } ^ { ( m ) }$ and $Z _ { 3 } ( m , s )$ respectively. Otherwise, set $Z _ { 3 } ( m , s ) = 0$

Step 1.6: Set $Z ^ { ( 1 ) } \big ( \dot { m } , s ^ { ( m ) } \big ) ^ { - } = \operatorname* { m a x } _ { i = 1 , 2 , 3 } Z _ { i } \Big ( m , s _ { i } ^ { ( m ) } \Big )$ , then $( s _ { i } ^ { ( m ) }$ $T _ { i } ^ { ( m ) } )$ is the optimal solution and ${ \cal Z } ^ { ( 1 ) } ( m , s ^ { ( m ) } , T ^ { ( m ) } )$ is maximum value of the objective function for <sup>fi</sup>xed m.

Step 1.7: Set $m ^ { \prime } = m + 1$ and repeat Steps 1.1–1.6 to get $Z ^ { ( 1 ) } ( m$ $s ^ { ( m ^ { \prime } ) } , T ^ { ( m ^ { \prime } ) } )$ and go to Step 1.8.

Step 1.8: If $Z ^ { ( 1 ) } ( m ^ { \prime } , s ^ { ( m ^ { \prime } ) } , T ^ { ( m ^ { \prime } ) } ) { \geq } Z ^ { ( 1 ) } ( m , s ^ { ( m ) } , T ^ { ( m ) } )$ then set $m = m ^ { \prime }$ and go to Step 1.7, otherwise go to Step 5. Step 4: Execute Algorithm 2.

## Algorithm 2

Step 2.1: Determine ${ \tilde { s } } _ { 3 } ^ { ( m ) }$ from $\operatorname { E q . } \left( 4 0 \right)$

Step 2.2: For $j = 4 , 5$ obtain $s _ { i } ^ { ( m ) }$ by solving $\partial Z _ { i } ( m , s ) / \partial s = 0 .$

Step 2.3: If ${ S _ { 4 } } ^ { ( m ) } { \le } \tilde { s } _ { 3 } ^ { ( m ) }$ and $\bar { [ \partial ^ { 2 } Z _ { 4 } ( m , s ) / \partial s ^ { 2 } ] _ { s = s _ { 4 } ^ { ( m ) } } } < 0$ , then substitute the value $s _ { 4 } ^ { ( m ) }$ into Eqs. (28) and (42) to obtain the values of $T _ { 4 } ^ { ( m ) }$ and $Z _ { 4 } ( m , \ s )$ respectively. Otherwise, set $Z _ { 4 } ( m , s ) = 0$

Step 2.4: $\mathrm { I f } s _ { 5 } ^ { ( m ) } \ge \tilde { s } _ { 3 } ^ { ( m ) }$ and $[ \partial ^ { 2 } Z _ { 5 } ( m , s ) / \partial s ^ { 2 } ] _ { s = s _ { 5 } ^ { ( m ) } } < 0$ , then substitute the value $s _ { 5 } ^ { ( m ) }$ into Eqs. (29) and (43) to obtain the values of $T _ { 5 } ^ { ( m ) }$ and $Z _ { 5 } ( m , s )$ respectively. Otherwise, set $Z _ { 5 } ( m , s ) = 0 .$

Step 2.5: Set $\begin{array} { r } { \dot { Z ^ { ( 2 ) } } ( m , s ^ { ( m ) } ) = \operatorname* { m a x } _ { j = 4 , 5 } Z _ { j } \left( m , s _ { j } ^ { ( m ) } \right) } \end{array}$ , then $( s _ { j } ^ { ( m ) } ,$ $T _ { j } ^ { ( m ) } )$ is the optimal solution and $Z ^ { ( 2 ) } ( \dot { m } , s ^ { ( m ) } , T ^ { ( m ) } )$ is maximum value of the objective function for <sup>fi</sup>xed m.

Step 2.6: $\mathsf { S e t } m ^ { \prime } = m + 1$ and repeat Steps 2.1–2.5 to get $Z ^ { ( 2 ) } ( m ,$ $s ^ { ( m ^ { \prime } ) } , T ^ { ( m ^ { \prime } ) } )$ and go to Step 2.7.

Step 2.7: If $Z ^ { ( 2 ) } ( m ^ { \prime } , s ^ { ( m ^ { \prime } ) } , T ^ { ( m ^ { \prime } ) } ) { \ge } \dot { Z } ^ { ( 2 ) } ( m , s ^ { ( m ) } , T ^ { ( m ) } )$ then set $m = m ^ { \prime }$ and go to Step 2.6, otherwise go to Step $5 .$

Step 5: Set $( m ^ { * } , s ^ { * } , T ^ { * } ) = ( m , s ^ { ( m ) } , T ^ { ( m ) } )$ , then $( m ^ { * } , s ^ { * } , T ^ { * } )$ is the optimal solution.

## 5. Numerical examples

Example 1. In order to illustrate the above solution procedure, let us consider an inventory system with the data: $a = 2 . 5 \times 1 0 ^ { 6 }$ units/year, $b = 2 . 5 , \ \rho = 0 . 8 , A _ { v } = \xi 1 0 0 0 / s \mathrm { e t } \cdot \mathrm { u p } , \ w _ { s } = \xi 0 . 8 / \mathrm { u n i t } , \ A _ { r } = \xi 8 0 $ /per order, c =\$0.05/unit, c =\$120/shipment, $c _ { 0 } = 1 , ~ c _ { 1 } = 1 . 5 \times 1 0 ^ { 4 } , ~ c _ { 2 } = 1 . 5 \times$ $1 0 ^ { - 5 } , \ v = \ S 3 / \mathrm { u n i t } , \ r _ { 1 } = 0 . 1 , \ r _ { 2 } = 0 . 2 , \ r _ { 3 } = 0 . 0 5 , \ I v = 0 . 0 4 , \ I c = 0 . 1 2 , \ I e =$ 0.08. Besides, the defective rate p has a Beta distribution with parameters x=1 and $y = 7 ;$ that is, the p.d.f. of p is given by $f ( p ) { = } 7 ( 1 - p ) ^ { 6 }$ $0 < p < 1$ . Hence $E ( p ) = x / ( x + y ) = 1 / 8$ , and $V _ { p } = x y / [ ( x + y ) ^ { 2 } ( x + y +$ $1 ) ] = 7 / 5 7 6$

Applying the procedure of the proposed algorithm for $\alpha { = } 0 , 0 . 5$ and 0.9, we summarize the computational results for different values of M by varying N in Tables 1, 2 and 3 respectively.

Based on the computational results we can obtain the following managerial insights:

(a) For <sup>fi</sup>xed α, it can be observed that when M=10 or 15, the optimal length of replenishment cycle (T\*) and optimal retail price $( s ^ { * } )$ increase, whereas supplier's expected pro<sup>fi</sup>t, retailer's expected pro<sup>fi</sup>t and the joint expected pro<sup>fi</sup>t $( Z ^ { * } )$ decrease, when the customer credit period N increases. For $M { \geq } 3 0$ , with increase in N and $N { \leq } M ,$ the optimal length of replenishment cycle $( T ^ { * } ) _ { }$ , and optimal retail price $( s ^ { * } )$ increase, whereas supplier's expected pro<sup>fi</sup>t, retailer's expected pro<sup>fi</sup>t and the joint expected pro<sup>fi</sup>t $( Z ^ { * } )$ decreases. This result reveals that if trade credit offered by supplier is longer than trade credit offered by retailer, a higher retail price is set which results in a decrease in both demand and in the supplier's production size and hence reduces the joint expected pro<sup>fi</sup>t. On the other hand, optimal length of replenishment cycle (T\*) and optimal retail price (s\*) decrease, whereas supplier's expected pro<sup>fi</sup>t, retailer's expected pro<sup>fi</sup>t and the joint expected pro<sup>fi</sup>t $( Z ^ { * } )$ increases, when the customer credit period N increases and $M { < } N .$ . This result indicates that if trade credit offered by supplier is shorter than trade credit offered by retailer, the retailer shortens the replenishment cycle to take advantage of the trade credit more frequently. Furthermore, a lower retail price is set which in turn increase in both

Computational results for different values of M and N when α=0.0.

<table><tr><td rowspan="2">M(days)</td><td rowspan="2">N(days)</td><td rowspan="2"> $m^*$ </td><td rowspan="2"> $s^*$ </td><td rowspan="2"> $c (K^*)$ </td><td rowspan="2"> $T^*(days)$ </td><td rowspan="2"> $Q^*$ </td><td colspan="3">Profit ($)</td></tr><tr><td>Retailer</td><td>Supplier</td><td>System</td></tr><tr><td rowspan="5">10</td><td>10</td><td>16</td><td>4.9848</td><td>2.1112</td><td>28.38</td><td>3503.91</td><td>57,992.54</td><td>38,344.40</td><td>96,336.94</td></tr><tr><td>15</td><td>16</td><td>4.9888</td><td>2.1101</td><td>28.41</td><td>3500.76</td><td>57,789.34</td><td>38,325.57</td><td>96,114.91</td></tr><tr><td>30</td><td>16</td><td>5.0009</td><td>2.1066</td><td>28.51</td><td>3491.29</td><td>57,184.39</td><td>38,267.11</td><td>95,451.50</td></tr><tr><td>45</td><td>16</td><td>5.0131</td><td>2.1032</td><td>28.60</td><td>3481.82</td><td>56,586.39</td><td>38,205.71</td><td>94,792.10</td></tr><tr><td>60</td><td>16</td><td>5.0253</td><td>2.0998</td><td>28.70</td><td>3472.33</td><td>55,995.27</td><td>38,141.42</td><td>94,136.69</td></tr><tr><td rowspan="5">15</td><td>10</td><td>16</td><td>4.9824</td><td>2.1119</td><td>28.35</td><td>3504.69</td><td>58,205.85</td><td>38,270.80</td><td>96,476.65</td></tr><tr><td>15</td><td>16</td><td>4.9863</td><td>2.1108</td><td>28.39</td><td>3502.71</td><td>57,999.64</td><td>38,252.67</td><td>96,252.31</td></tr><tr><td>30</td><td>16</td><td>4.9984</td><td>2.1073</td><td>28.49</td><td>3493.25</td><td>57,392.74</td><td>38,195.33</td><td>95,588.07</td></tr><tr><td>45</td><td>16</td><td>5.0105</td><td>2.1039</td><td>28.58</td><td>3483.77</td><td>56,792.79</td><td>38,135.05</td><td>94,927.84</td></tr><tr><td>60</td><td>16</td><td>5.0227</td><td>2.1005</td><td>28.68</td><td>3474.29</td><td>56,199.76</td><td>38,071.85</td><td>94,271.61</td></tr><tr><td rowspan="5">30</td><td>10</td><td>16</td><td>4.9765</td><td>2.1137</td><td>28.18</td><td>3493.11</td><td>58,876.61</td><td>38,044.41</td><td>96,921.01</td></tr><tr><td>15</td><td>16</td><td>4.9798</td><td>2.1127</td><td>28.26</td><td>3498.07</td><td>58,654.61</td><td>38,029.18</td><td>96,683.79</td></tr><tr><td>30</td><td>16</td><td>4.9909</td><td>2.1095</td><td>28.43</td><td>3499.11</td><td>58,020.81</td><td>37,977.98</td><td>95,998.79</td></tr><tr><td>45</td><td>16</td><td>4.9789</td><td>2.1129</td><td>28.33</td><td>3508.56</td><td>58,633.57</td><td>38,031.95</td><td>96,665.52</td></tr><tr><td>60</td><td>16</td><td>4.9669</td><td>2.1165</td><td>28.24</td><td>3518.01</td><td>59,253.36</td><td>38,082.91</td><td>97,336.27</td></tr><tr><td rowspan="5">45</td><td>10</td><td>16</td><td>4.9725</td><td>2.1148</td><td>28.01</td><td>3479.67</td><td>59,592.21</td><td>37,807.77</td><td>97,399.98</td></tr><tr><td>15</td><td>16</td><td>4.9751</td><td>2.1141</td><td>28.03</td><td>3477.42</td><td>59,356.11</td><td>37,796.86</td><td>97,152.97</td></tr><tr><td>30</td><td>16</td><td>4.9843</td><td>2.1114</td><td>28.30</td><td>3494.41</td><td>58,674.55</td><td>37,754.88</td><td>96,429.43</td></tr><tr><td>45</td><td>16</td><td>4.9955</td><td>2.1081</td><td>28.47</td><td>3495.50</td><td>58,041.83</td><td>37,704.02</td><td>95,745.86</td></tr><tr><td>60</td><td>16</td><td>4.9835</td><td>2.1116</td><td>28.37</td><td>3504.96</td><td>58,653.46</td><td>37,757.59</td><td>96,411.05</td></tr><tr><td rowspan="5">60</td><td>10</td><td>16</td><td>4.9691</td><td>2.1158</td><td>27.99</td><td>3482.54</td><td>60,320.41</td><td>37,565.47</td><td>97,885.88</td></tr><tr><td>15</td><td>16</td><td>4.9718</td><td>2.1150</td><td>28.01</td><td>3480.29</td><td>60,083.51</td><td>37,555.11</td><td>97,638.62</td></tr><tr><td>30</td><td>16</td><td>4.9797</td><td>2.1127</td><td>28.06</td><td>3473.54</td><td>59,374.93</td><td>37,523.07</td><td>96,898.00</td></tr><tr><td>45</td><td>16</td><td>4.9964</td><td>2.1100</td><td>28.40</td><td>3485.96</td><td>58,733.58</td><td>37,451.85</td><td>96,185.43</td></tr><tr><td>60</td><td>16</td><td>5.0001</td><td>2.1068</td><td>28.50</td><td>3491.89</td><td>58,062.71</td><td>37,430.80</td><td>95,493.51</td></tr></table>

demand and the supplier's production size. Therefore, total expected pro<sup>fi</sup>t for entire supply chain increases. Besides, with an increase in the value of the parameter α, optimal length of replenishment cycle (T\*) and optimal retail price (s\*) decrease, whereas supplier's expected pro<sup>fi</sup>t, retailer's expected pro<sup>fi</sup>t and the joint expected pro<sup>fi</sup>t (Z\*) increases. The feature of optimal retail price (s\*) and joint expected pro<sup>fi</sup>t (Z\*) with respect to α and N for <sup>fi</sup>xed value of M is depicted in Fig. 1(a) and (b) respectively. It can be observed from the <sup>fi</sup>gures that if the retailer encourages the customer to raise the part payment of purchase cost and offers longer credit period to its customer, then he can stimulate the demand by reducing the retail price and thereby raise the joint expected pro<sup>fi</sup>t.

(b) For <sup>fi</sup>xed values of N and α, it can be noted that optimal length of replenishment cycle (T\*) and optimal retail price (s\*) decrease, whereas retailer's expected pro<sup>fi</sup>t and the joint expected pro<sup>fi</sup>t (Z\*) increase with an increase in retailer's credit period M and NbM. From the retailer's point of view, it represents that a longer credit period offered by supplier cause the retailer to shorten the replenishment cycle length to take bene<sup>fi</sup>t of trade credit more frequently which in turn raise the retailer's expected pro<sup>fi</sup>t. It may be interesting to observe that, for N=60 and α=0 or 0.5,

Computational results for different values of M and N when α=0.5.

<table><tr><td rowspan="2">M(days)</td><td rowspan="2">N(days)</td><td rowspan="2"> $m^*$ </td><td rowspan="2"> $s^*$ </td><td rowspan="2"> $c (K^*)$ </td><td rowspan="2"> $T^*(days)$ </td><td rowspan="2"> $Q^*$ </td><td colspan="3">Profit ($)</td></tr><tr><td>Retailer</td><td>Supplier</td><td>System</td></tr><tr><td rowspan="5">10</td><td>10</td><td>16</td><td>4.9810</td><td>2.1123</td><td>28.33</td><td>3504.73</td><td>58,201.24</td><td>38,362.24</td><td>96,563.48</td></tr><tr><td>15</td><td>16</td><td>4.9830</td><td>2.1117</td><td>28.35</td><td>3503.15</td><td>58,099.17</td><td>38,353.03</td><td>96,452.20</td></tr><tr><td>30</td><td>16</td><td>4.9890</td><td>2.1100</td><td>28.40</td><td>3498.40</td><td>57,794.12</td><td>38,324.90</td><td>96,119.02</td></tr><tr><td>45</td><td>16</td><td>4.9950</td><td>2.1083</td><td>28.44</td><td>3493.66</td><td>57,490.82</td><td>38,296.02</td><td>95,786.84</td></tr><tr><td>60</td><td>16</td><td>5.0011</td><td>2.1065</td><td>28.49</td><td>3488.91</td><td>57,189.27</td><td>38,266.41</td><td>95,455.67</td></tr><tr><td rowspan="5">15</td><td>10</td><td>16</td><td>4.9788</td><td>2.1130</td><td>28.29</td><td>3503.19</td><td>58,419.85</td><td>38,287.65</td><td>96,707.50</td></tr><tr><td>15</td><td>16</td><td>4.9808</td><td>2.1124</td><td>28.31</td><td>3502.19</td><td>58,316.30</td><td>38,278.78</td><td>96,595.08</td></tr><tr><td>30</td><td>16</td><td>4.9868</td><td>2.1107</td><td>28.36</td><td>3497.42</td><td>58,010.33</td><td>38,251.19</td><td>96,261.52</td></tr><tr><td>45</td><td>16</td><td>4.9928</td><td>2.1089</td><td>28.40</td><td>3492.66</td><td>57,706.12</td><td>38,222.85</td><td>95,928.97</td></tr><tr><td>60</td><td>16</td><td>4.9988</td><td>2.1072</td><td>28.45</td><td>3487.89</td><td>57,403.65</td><td>38,193.78</td><td>95,597.43</td></tr><tr><td rowspan="5">30</td><td>10</td><td>16</td><td>4.9735</td><td>2.1145</td><td>28.08</td><td>3487.08</td><td>59,106.59</td><td>38,058.03</td><td>97,164.62</td></tr><tr><td>15</td><td>16</td><td>4.9752</td><td>2.1140</td><td>28.13</td><td>3489.48</td><td>58,995.22</td><td>38,050.59</td><td>97,045.80</td></tr><tr><td>30</td><td>16</td><td>4.9807</td><td>2.1124</td><td>28.21</td><td>3489.78</td><td>58,676.14</td><td>38,025.96</td><td>96,702.10</td></tr><tr><td>45</td><td>16</td><td>4.9747</td><td>2.1142</td><td>28.16</td><td>3494.69</td><td>58,984.71</td><td>38,051.97</td><td>97,036.68</td></tr><tr><td>60</td><td>16</td><td>4.9687</td><td>2.1159</td><td>28.12</td><td>3499.60</td><td>59,295.03</td><td>38,077.24</td><td>97,372.27</td></tr><tr><td rowspan="5">45</td><td>10</td><td>16</td><td>4.9699</td><td>2.1156</td><td>27.99</td><td>3481.92</td><td>59,828.67</td><td>37,818.53</td><td>97,647.19</td></tr><tr><td>15</td><td>16</td><td>4.9712</td><td>2.1152</td><td>28.00</td><td>3480.80</td><td>59,710.40</td><td>37,813.17</td><td>97,523.56</td></tr><tr><td>30</td><td>16</td><td>4.9757</td><td>2.1139</td><td>28.13</td><td>3488.99</td><td>59,368.00</td><td>37,792.92</td><td>97,160.92</td></tr><tr><td>45</td><td>16</td><td>4.9813</td><td>2.1122</td><td>28.21</td><td>3489.30</td><td>59,048.36</td><td>37,768.95</td><td>96,817.31</td></tr><tr><td>60</td><td>16</td><td>4.9753</td><td>2.1140</td><td>28.17</td><td>3494.21</td><td>59,357.54</td><td>37,794.25</td><td>97,151.79</td></tr><tr><td rowspan="5">60</td><td>10</td><td>16</td><td>4.9665</td><td>2.1166</td><td>27.97</td><td>3484.78</td><td>60,557.66</td><td>37,575.68</td><td>98,133.34</td></tr><tr><td>15</td><td>16</td><td>4.9678</td><td>2.1162</td><td>27.98</td><td>3483.66</td><td>60,438.99</td><td>37,570.60</td><td>98,009.59</td></tr><tr><td>30</td><td>16</td><td>4.9718</td><td>2.1150</td><td>28.01</td><td>3480.29</td><td>60,083.51</td><td>37,555.11</td><td>97,638.62</td></tr><tr><td>45</td><td>16</td><td>4.9815</td><td>2.1122</td><td>28.18</td><td>3484.63</td><td>59,769.30</td><td>37,517.62</td><td>97,286.92</td></tr><tr><td>60</td><td>16</td><td>4.9819</td><td>2.1121</td><td>28.22</td><td>3488.82</td><td>59,420.44</td><td>37,512.09</td><td>96,932.53</td></tr></table>

Computational results for different values of M and N when $\alpha { = } 0 . 9 .$

<table><tr><td rowspan="2">M(days)</td><td rowspan="2">N(days)</td><td rowspan="2"> $m^*$ </td><td rowspan="2"> $s^*$ </td><td rowspan="2"> $c (K^*)$ </td><td rowspan="2"> $T^*(days)$ </td><td rowspan="2"> $Q^*$ </td><td colspan="3">Profit ($)</td></tr><tr><td>Retailer</td><td>Supplier</td><td>System</td></tr><tr><td rowspan="5">10</td><td>10</td><td>16</td><td>4.9779</td><td>2.1132</td><td>28.30</td><td>3505.40</td><td>58,368.71</td><td>38,376.30</td><td>96,745.01</td></tr><tr><td>15</td><td>16</td><td>4.9783</td><td>2.1131</td><td>28.30</td><td>3505.08</td><td>58,348.22</td><td>38,374.49</td><td>96,722.71</td></tr><tr><td>30</td><td>16</td><td>4.9795</td><td>2.1128</td><td>28.31</td><td>3504.13</td><td>58,286.80</td><td>38,369.04</td><td>96,655.84</td></tr><tr><td>45</td><td>16</td><td>4.9808</td><td>2.1124</td><td>28.32</td><td>3503.18</td><td>58,225.45</td><td>38,363.55</td><td>96,589.00</td></tr><tr><td>60</td><td>16</td><td>4.9820</td><td>2.1121</td><td>28.33</td><td>3502.23</td><td>58,164.17</td><td>38,358.04</td><td>96,522.21</td></tr><tr><td rowspan="5">15</td><td>10</td><td>16</td><td>4.9759</td><td>2.1138</td><td>28.24</td><td>3502.02</td><td>58,591.53</td><td>38,300.92</td><td>96,892.45</td></tr><tr><td>15</td><td>16</td><td>4.9763</td><td>2.1137</td><td>28.24</td><td>3501.81</td><td>58,570.75</td><td>38,299.18</td><td>96,869.93</td></tr><tr><td>30</td><td>16</td><td>4.9775</td><td>2.1133</td><td>28.25</td><td>3500.86</td><td>58,509.16</td><td>38,293.83</td><td>96,802.99</td></tr><tr><td>45</td><td>16</td><td>4.9787</td><td>2.1130</td><td>28.26</td><td>3499.90</td><td>58,447.63</td><td>38,288.46</td><td>96,736.09</td></tr><tr><td>60</td><td>16</td><td>4.9799</td><td>2.1126</td><td>28.27</td><td>3498.94</td><td>58,386.17</td><td>38,283.05</td><td>96,669.23</td></tr><tr><td rowspan="5">30</td><td>10</td><td>16</td><td>4.9712</td><td>2.1152</td><td>28.01</td><td>3482.44</td><td>59,290.99</td><td>38,068.73</td><td>97,359.72</td></tr><tr><td>15</td><td>16</td><td>4.9715</td><td>2.1151</td><td>28.02</td><td>3482.91</td><td>59,268.66</td><td>38,067.27</td><td>97,335.92</td></tr><tr><td>30</td><td>16</td><td>4.9726</td><td>2.1148</td><td>28.04</td><td>3482.93</td><td>59,204.49</td><td>38,062.49</td><td>97,266.99</td></tr><tr><td>45</td><td>16</td><td>4.9714</td><td>2.1151</td><td>28.03</td><td>3483.94</td><td>59,266.56</td><td>38,067.54</td><td>97,334.10</td></tr><tr><td>60</td><td>16</td><td>4.9702</td><td>2.1155</td><td>28.02</td><td>3484.95</td><td>59,328.69</td><td>38,072.56</td><td>97,401.25</td></tr><tr><td rowspan="5">45</td><td>10</td><td>16</td><td>4.9678</td><td>2.1162</td><td>27.98</td><td>3483.72</td><td>60,018.09</td><td>37,827.02</td><td>97,845.10</td></tr><tr><td>15</td><td>16</td><td>4.9680</td><td>2.1161</td><td>27.98</td><td>3483.49</td><td>59,994.40</td><td>37,825.96</td><td>97,820.36</td></tr><tr><td>30</td><td>16</td><td>4.9689</td><td>2.1159</td><td>28.00</td><td>3485.09</td><td>59,925.66</td><td>37,822.03</td><td>97,747.69</td></tr><tr><td>45</td><td>16</td><td>4.9700</td><td>2.1156</td><td>28.02</td><td>3485.11</td><td>59,861.21</td><td>37,817.47</td><td>97,678.68</td></tr><tr><td>60</td><td>16</td><td>4.9688</td><td>2.1159</td><td>28.01</td><td>3486.12</td><td>59,923.59</td><td>37,822.29</td><td>97,745.88</td></tr><tr><td rowspan="5">60</td><td>10</td><td>16</td><td>4.9644</td><td>2.1172</td><td>27.95</td><td>3486.57</td><td>60,747.72</td><td>37,583.73</td><td>98,331.45</td></tr><tr><td>15</td><td>16</td><td>4.9647</td><td>2.1171</td><td>27.95</td><td>3486.35</td><td>60,723.95</td><td>37,582.73</td><td>98,306.68</td></tr><tr><td>30</td><td>16</td><td>4.9655</td><td>2.1169</td><td>27.96</td><td>3485.68</td><td>60,652.66</td><td>37,579.72</td><td>98,232.38</td></tr><tr><td>45</td><td>16</td><td>4.9664</td><td>2.1166</td><td>27.99</td><td>3487.26</td><td>60,583.69</td><td>37,575.96</td><td>98,159.65</td></tr><tr><td>60</td><td>16</td><td>4.9675</td><td>2.1163</td><td>28.00</td><td>3487.28</td><td>60,518.95</td><td>37,571.61</td><td>98,090.56</td></tr></table>

increasing M causes the replenishment cycle time and retail price to decrease up to certain value of M and then subsequently increases. Hence, the retailer's expected pro<sup>fi</sup>t increases up to certain value of M and then subsequently decreases. Therefore, retailer should set his trade credit parameters carefully to ensure the optimal outcome. The characteristic of optimal retail price (s\*) and joint expected pro<sup>fi</sup>t (Z\*) with respect to α and M for <sup>fi</sup>xed value of N is depicted in Fig. 2(a) and (b) respectively.

![](/api/attachments/VTJZ47U3/fulltext/images/8049ac3d5dd7ac115d5fd92f27d4ded6a0a152b75269a883142917074be6d619.jpg)

![](/api/attachments/VTJZ47U3/fulltext/images/67a59771d4920a87631e2c5602ff91859998cbe93f45d0a2e663f975fc6a2850.jpg)  
Fig. 1. Variation of price and joint pro<sup>fi</sup>t with respect to N when M=30 (Example 1).

Example 2. In this example, we study the effect of variable capacity utilization $\rho ,$ and defective rate, p. All the parameters are identical to those in Example 1 except α=0.5, M=30 and N=15. Computational results are summarized in Table 4 for $\rho { \in } \{ 0 . 3 , 0 . 5 , 0 . 8 , 0 . 8 5 , 0 . 9 5 \}$ and various set of parameters x=1 and y∈{5, 7, 9, 11} of Beta distribution. Based on the computational results we can obtain the following managerial insights:

![](/api/attachments/VTJZ47U3/fulltext/images/4799851e748e5790a9d3590492e60c4da981ad4f0e1918c7f1fbc6a542e1d9dc.jpg)

![](/api/attachments/VTJZ47U3/fulltext/images/d95414b700f5e5d304ea389041691acb20ea86925f73a7b0721901865bb77f2d.jpg)  
Fig. 2. Variation of price and joint pro<sup>fi</sup>t with respect to M when N=30 (Example 1).

Table 5  
Table 4  
Computational results for Example 2.

<table><tr><td rowspan="2">y</td><td rowspan="2">ρ</td><td rowspan="2"> $m^*$ </td><td rowspan="2"> $s^*$ </td><td rowspan="2"> $c (K^*)$ </td><td rowspan="2"> $T^*(days)$ </td><td rowspan="2"> $Q^*$ </td><td colspan="3">Profit ($)</td></tr><tr><td>Retailer</td><td>Supplier</td><td>System</td></tr><tr><td rowspan="5">5</td><td>0.3</td><td>5</td><td>6.4318</td><td>2.3803</td><td>42.35</td><td>2765.11</td><td>55,070.59</td><td>10,210.73</td><td>65,281.32</td></tr><tr><td>0.5</td><td>7</td><td>5.6581</td><td>2.2134</td><td>33.78</td><td>3038.51</td><td>54,151.06</td><td>22,079.94</td><td>76,231.00</td></tr><tr><td>0.8</td><td>24</td><td>5.0293</td><td>2.0986</td><td>27.25</td><td>3290.34</td><td>49,263.19</td><td>38,447.34</td><td>87,710.54</td></tr><tr><td>0.85</td><td>94</td><td>4.9275</td><td>2.0934</td><td>34.83</td><td>4425.81</td><td>48,047.17</td><td>43,015.97</td><td>91,063.15</td></tr><tr><td>0.95</td><td>15</td><td>4.8066</td><td>2.0680</td><td>37.91</td><td>5125.87</td><td>45,719.01</td><td>46,634.96</td><td>92,353.97</td></tr><tr><td rowspan="5">7</td><td>0.3</td><td>5</td><td>6.3705</td><td>2.4047</td><td>42.90</td><td>2868.56</td><td>62,074.17</td><td>10,136.38</td><td>72,210.55</td></tr><tr><td>0.5</td><td>6</td><td>5.5972</td><td>2.2342</td><td>36.36</td><td>3359.59</td><td>62,472.91</td><td>21,903.02</td><td>84,375.93</td></tr><tr><td>0.8</td><td>16</td><td>4.9752</td><td>2.1140</td><td>28.13</td><td>3489.48</td><td>58,995.21</td><td>38,050.59</td><td>97,045.80</td></tr><tr><td>0.85</td><td>28</td><td>4.8969</td><td>2.1020</td><td>27.29</td><td>3521.85</td><td>58,147.23</td><td>40,923.42</td><td>99,070.64</td></tr><tr><td>0.95</td><td>24</td><td>4.7464</td><td>2.0840</td><td>37.55</td><td>5240.89</td><td>56,018.59</td><td>47,203.20</td><td>103,221.78</td></tr><tr><td rowspan="5">9</td><td>0.3</td><td>5</td><td>6.3404</td><td>2.4171</td><td>43.27</td><td>2927.80</td><td>65,943.44</td><td>10,137.19</td><td>76,080.63</td></tr><tr><td>0.5</td><td>6</td><td>5.5679</td><td>2.2447</td><td>36.56</td><td>3423.29</td><td>67,149.05</td><td>21,876.40</td><td>89,025.45</td></tr><tr><td>0.8</td><td>14</td><td>4.9478</td><td>2.1222</td><td>28.60</td><td>3597.39</td><td>64,445.00</td><td>37,892.73</td><td>102,337.73</td></tr><tr><td>0.85</td><td>20</td><td>4.8713</td><td>2.1095</td><td>27.78</td><td>3633.11</td><td>63,710.64</td><td>40,615.10</td><td>104,325.73</td></tr><tr><td>0.95</td><td>36</td><td>4.7173</td><td>2.0922</td><td>37.14</td><td>5263.54</td><td>61,815.51</td><td>47,441.30</td><td>109,256.82</td></tr><tr><td rowspan="5">11</td><td>0.3</td><td>5</td><td>6.3224</td><td>2.4246</td><td>43.53</td><td>2966.30</td><td>68,397.44</td><td>10,152.78</td><td>78,550.22</td></tr><tr><td>0.5</td><td>6</td><td>5.5504</td><td>2.2511</td><td>36.71</td><td>3464.49</td><td>70,124.66</td><td>21,869.39</td><td>91,994.05</td></tr><tr><td>0.8</td><td>13</td><td>4.9313</td><td>2.1272</td><td>28.95</td><td>3671.41</td><td>67,926.27</td><td>37,806.20</td><td>105,732.47</td></tr><tr><td>0.85</td><td>17</td><td>4.8555</td><td>2.1142</td><td>28.26</td><td>3726.45</td><td>67,263.88</td><td>40,465.12</td><td>107,729.00</td></tr><tr><td>0.95</td><td>54</td><td>4.7001</td><td>2.0972</td><td>36.84</td><td>5268.72</td><td>65,523.14</td><td>47,586.72</td><td>113,109.86</td></tr></table>

(a) For <sup>fi</sup>xed defective rate p, it can be observed that as ρ increases, the retail price is substantially lower which causes in a substantial increase in demand. It is interesting to note that the supplier's production size (m\*Q\*), the expected pro<sup>fi</sup>t and the joint expected pro<sup>fi</sup>t (Z\*) increase while supplier's production cost decreases with an increase in ρ. As a result, if the production rate is closer to the demand rate then the gain in integrated mode is greater.

(b) For <sup>fi</sup>xed value of ρ, the retailer's expected pro<sup>fi</sup>t and the joint expected pro<sup>fi</sup>t (Z\*) increase as the mean defective rate decreases. This result indicates that if the defective rate reduced effectively then the channel's pro<sup>fi</sup>t will improve which is quite rational.

Example 3. This example was carried out to evaluate the relative performance for various values of the price elasticity b. All the parameters are identical to those in Example 1 except α=0.5, M=30 and N=15. Computational results are summarized in Table 5 for b ∈{2.3, 2.5, 2.8, 3}.

Table 5 shows that, as the parameter b increases, optimal retail price (s\*), optimal order quantity (Q\*), supplier's expected pro<sup>fi</sup>t, retailer's expected pro<sup>fi</sup>t and the joint expected pro<sup>fi</sup>t (Z\*) decrease. As elasticity of price b increases, the demand rate decreases. With reduction in demand rate, the total expected pro<sup>fi</sup>t of the retailer as well as the entire channel shrinks signi<sup>fi</sup>cantly.

Computational results for Example 3.

<table><tr><td rowspan="2">b</td><td rowspan="2">m*</td><td rowspan="2">s*</td><td rowspan="2">c (K*)</td><td rowspan="2">T*(days)</td><td rowspan="2">Q*</td><td colspan="3">Profit ($)</td></tr><tr><td>Retailer</td><td>Supplier</td><td>System</td></tr><tr><td>2.3</td><td>16</td><td>5.5253</td><td>2.1642</td><td>25.55</td><td>3536.49</td><td>87,969.72</td><td>38,470.43</td><td>126,440.15</td></tr><tr><td>2.5</td><td>16</td><td>4.9752</td><td>2.1140</td><td>29.19</td><td>3439.38</td><td>58,997.59</td><td>38,059.44</td><td>97,057.04</td></tr><tr><td>2.8</td><td>16</td><td>4.3642</td><td>2.0544</td><td>29.20</td><td>3292.66</td><td>30,487.08</td><td>36,616.18</td><td>67,103.26</td></tr><tr><td>3.0</td><td>16</td><td>4.0529</td><td>2.0237</td><td>32.85</td><td>3196.08</td><td>17,829.35</td><td>35,313.27</td><td>53,142.61</td></tr></table>

Example 4. In this example, we compare an independent and coordinated decision on supply chain performance. Using the same data as in Example 1 except α=0.5, (M, N)= {(30, 45), (45, 30)} and applying similar procedure (interested reader can derive the results for independent system analogously) we list the optimal solutions in Table 6.

Table 6 shows that independent optimization model requires the retailer to raise the retail price and to order in smaller lot size. Reduction in lot size reduces the expected pro<sup>fi</sup>t of the supplier as well as the entire supply chain signi<sup>fi</sup>cantly. Hence, the lot size coordination can signi<sup>fi</sup>cantly improve the pro<sup>fi</sup>t of the entire supply chain.

## 6. Conclusion

This paper examined the defective goods effect on an integrated inventory model with two-level trade credit. We assumed the market demand is sensitive to the retail price and the production rate will react to the market demand rate. Besides, we assumed the retailer receives a full trade credit from its supplier, and offers partial trade credit to its customers. Such considerations in this paper are seldom studied in the existing literature. Considering the two-level trade credit policy, we exploited structural properties of joint pro<sup>fi</sup>t function and utilize it to derive theoretical results. An algorithmic procedure is developed to determine the optimal length of replenishment cycle, retail price and the number of shipments per production run from the supplier to the retailer. Finally, we provided numerical examples to illustrate the proposed model, and perform a sensitivity analysis with respect to key parameters.

In future research, one could potentially consider other inspection policies for imperfect items. Another extension of this work may be set in the direction of considering more general demand risk and environment risk in the supply chain. At last, it would be interesting to incorporate the <sup>fi</sup>nancial strategies such as quantity discount, cash discount, and so forth.

## Acknowledgments

The Authors wish to express their gratitude to the editors and referees for their valuable suggestions and comments which signi<sup>fi</sup>cantly improved the original paper.

Table 6 Computational results for Example 4.

<table><tr><td rowspan="2">(M, N)</td><td rowspan="2">Decision</td><td rowspan="2"> $m^*$ </td><td rowspan="2"> $s^*$ </td><td rowspan="2"> $c (K^*)$ </td><td rowspan="2"> $T^*$ (days)</td><td rowspan="2"> $Q^*$ </td><td colspan="3">Profit ($)</td></tr><tr><td>Retailer</td><td>Supplier</td><td>System</td></tr><tr><td rowspan="2">(30, 45)</td><td>Individual</td><td>15</td><td>5.6620</td><td>2.0216</td><td>36.68</td><td>3304.76</td><td>61,330.83</td><td>31,218.14</td><td>92,545.67</td></tr><tr><td>Coordinated</td><td>16</td><td>4.9747</td><td>2.1142</td><td>28.16</td><td>3494.69</td><td>58,984.71</td><td>38,051.97</td><td>97,036.68</td></tr><tr><td rowspan="2">(45, 30)</td><td>Individual</td><td>15</td><td>5.6362</td><td>2.0215</td><td>35.95</td><td>3286.01</td><td>61,570.67</td><td>31,340.54</td><td>92,906.04</td></tr><tr><td>Coordinated</td><td>16</td><td>4.9757</td><td>2.1139</td><td>28.13</td><td>3488.99</td><td>59,368.00</td><td>37,792.92</td><td>97,160.92</td></tr></table>

Appendix A. Calculation for interest earned (IE) and interest charged (IC)

Note that many researchers used different ways to calculate the interest earned and interest charged. In this paper, we have used the Teng [34] approach throughout this article.

Case 1. $N { \leq } M .$

Based on the values of M (i.e. the time at which the retailer must pay the supplier to avoid interest charge), T (i.e. the replenishment cycle time), and T+N (i.e. the time at which the retailer receives the payment from the last customer), we have to examine following three situations: (1) 0bT+N≤M (2) T≤M≤T+N (3) M≤T.

Situation 1: 0bT+N≤M (i.e. 0bTbM−N)

In this case, the retailer receives the all returns from customer before paying the purchase amount to the supplier. Consequently,

$$
I C _ {1} = 0\tag{A.1}
$$

On the other hand, following Teng [34], interest earned at a rate of Ie is

$$
I E _ {1} = s I e D \left[ T ^ {2} / 2 + \alpha T (M - T) + (1 - \alpha) T (M - T - N) \right]\tag{A.2}
$$

Situation 2: $T \le M \le T + N$ (i.e. $M - N { \leq } T { \leq } M )$

By the time M, the retailer has two sources to accumulate revenue in an account that earns Ie per dollar per year: (1) from the portion of partial payment (starting 0 through M), and (2) from the portion of delayed payment (starting N through M). Therefore, the interest earned is

$$
I E _ {2} = \frac {s I e D}{2} \left[ \alpha T ^ {2} + 2 \alpha T (M - T) + (1 - \alpha) (M - N) ^ {2} \right]\tag{A.3}
$$

Since $M { \leq } T { \ + } N ,$ , the retailer has to <sup>fi</sup>nance all the items sold after M−N at an interest charged Ic per dollar per year. Consequently, interest paid will be

$$
I C _ {2} = \frac {v I c D}{2} (1 - \alpha) (T + N - M) ^ {2}\tag{A.4}
$$

Situation 3: M T

Again, the retailer can accumulate revenue from two sources: (1) from the portion of partial payment (starting 0 through M), and (2) from the portion of delayed payment (starting N through M). Therefore, the interest earned is

$$
I E _ {3} = \frac {s I e D}{2} \left[ \alpha M ^ {2} + (1 - \alpha) (M - N) ^ {2} \right]\tag{A.5}
$$

As $M \leq T ,$ the retailer needs to <sup>fi</sup>nance the rest of the inventory, which is divided into two parts, <sup>fi</sup>rstly all items sold after M for the portion of immediate payment and secondly all items sold after M−N for the portion of credit payment. Hence, the interest paid will be

$$
I C _ {3} = \frac {v I c D}{2} \left[ \alpha (T - M) ^ {2} + (1 - \alpha) (T + N - M) ^ {2} \right]\tag{A.6}
$$

Case 2. N≥M.

Based on the values of M and T, we have to explore following two situations: (1) T≤M and (2) M≤T.

Situation 1: T≤M

During [0, M], the retailer accumulates his revenue in interest bearing account at the rate Ie per dollar per year. As a result, the interest earned by the retailer is

$$
I E _ {4} = \frac {\alpha s I e D}{2} \left[ T ^ {2} + 2 T (M - T) \right]\tag{A.7}
$$

The retailer must arrange the <sup>fi</sup>nance for (1) paying the supplier at the end of trade credit M, and (2) the items already sold but not paid for till T+N. The resultant interest charged will be

$$
I C _ {4} = \frac {(1 - \alpha) v I c D}{2} \left[ T ^ {2} + 2 T (N - M) \right]\tag{A.8}
$$

Situation 2: M≤T

In this case, the retailer can accumulate interest for portion of the partial payment till M at the rate Ie per dollar per year. Therefore, the interest earned will be

$$
I E _ {5} = \frac {\alpha s I e D M ^ {2}}{2}\tag{A.9}
$$

The retailer must <sup>fi</sup>nance for (1) the items sold after M, (2) the entire amount of the delayed payment at the end of the trade credit M, and (3) the items already sold but not yet paid for till T+N. So, the interest charged will be

$$
I C _ {5} = \frac {\alpha v I c D}{2} (T - M) ^ {2} + \frac {(1 - \alpha) v I c D T}{2} [ T + 2 (N - M) ]\tag{A.10}
$$

Appendix B. Proof of Lemma 1

(a) If $\varDelta _ { 1 } \leq 0$ then $2 \bar { A } \leq D \left[ \frac { ( X + c Y ) } { 1 - E ( p ) } + s I e \right] ( M - N ) ^ { 2 }$ which implies from Eq. (19) that $T _ { 1 } ^ { * } \leq M - N .$ It is clear from Eq. (14) that $Z _ { 1 } ( m , s , T )$ is strictly concave function in T. Thus $Z _ { 1 } ( m , s , T )$ is concave and reaches its maximum at point $T = T _ { 1 } ^ { * }$

(b) If $\varDelta _ { 1 } > 0$ then $2 \bar { A } > D \left[ \frac { ( X + c Y ) } { 1 - E ( p ) } + s I e \right] \left( M - N \right) ^ { 2 }$ . Hence, from $\operatorname { E q . } \left( 1 3 \right)$ we have

$$
\frac {\partial Z _ {1} (m , s , T)}{\partial T} > D \left[ \frac {(X + c Y)}{1 - E (p)} + s I e \right] \frac {\left[ (M - N) ^ {2} - T ^ {2} \right]}{2 T ^ {2}} > 0 \text {   for   } T \in (0, M - N)
$$

Consequently, $Z _ { 1 } ( m , s , T )$ is strictly increasing function of $T \in ( 0 ,$ $M - N ]$ . Hence, the maximum value of $Z _ { 1 } ( m , s , T )$ occurs at point $T = M - N .$

This completes the proof of Appendix B.

## Appendix C. Proof of Lemma 2

It is easy to see that $\Delta _ { 1 } > \Delta _ { 2 } .$

(a) If $\Delta _ { 2 } { \leq } 0 { \leq } \Delta _ { 1 }$ then we have:

$$
D \left[ \frac {(X + c Y)}{1 - E (p)} + s I e \right] (M - N) ^ {2} \leq 2 \bar {A} \leq D \left\{ \begin{array}{l} \left[ \frac {(X + c Y)}{1 - E (p)} + \alpha s I e + (1 - \alpha) v I c \right] M ^ {2} \\ - (1 - \alpha) (M - N) ^ {2} (v I c - s I e) \end{array} \right\}\tag{C.1}
$$

It follows from (C.1)

$$
0 <   D \left[ \frac {(X + c Y)}{1 - E (p)} + s I e \right] (M - N) ^ {2} \leq 2 \bar {A} + D (1 - \alpha) (M - N) ^ {2} (v I c - s I e)\tag{C.2}
$$

which indicates T\* in (21) is well-de<sup>fi</sup>ned. Combining (C.1) and Eq. (21) it follows that $M - N { \leq } T _ { 2 } ^ { * } { \leq } M .$ Furthermore,

$$
\frac {\partial^ {2} Z _ {2} (m , s , T)}{\partial T ^ {2}} <   \frac {- D}{T ^ {3}} \left[ \frac {(X + c Y)}{1 - E (p)} + s I e \right] (M - N) ^ {2} <   0\tag{C.3}
$$

Consequently, $Z _ { 2 } ( m , \ s , \ T )$ has maximum value at point $T = T _ { 2 } ^ { * } \in [ M - N , M ]$

(b) If $\varDelta _ { 1 } < 0$ then

$$
2 \overline {{A}} <   D [ (X + c Y) / (1 - E (p)) + s I e ] (M - N) ^ {2}\tag{C.4}
$$

Combining Eqs. (C.4) and (15) we have for $T \in ( M - N , M )$

$$
\frac {\partial Z _ {2} (m , s , T)}{\partial T} <   D \left[ \frac {(X + c Y)}{1 - E (p)} + \alpha s I e + (1 - \alpha) v I c \right] \left[ (M - N) ^ {2} - T ^ {2} \right] <   0\tag{C.5}
$$

Thus, $Z _ { 2 } ( m , s , T )$ is strictly decreasing function of $T \in [ M - N , M ]$ and thereby $Z _ { 2 } ( m , s , T )$ has maximum value at boundary point $T = M - N .$

(c) If $\varDelta _ { 2 } > 0$ then

$$
2 \bar {A} > D \left\{\left[ (X + c Y) / (1 - E (p)) + \alpha s I e + (1 - \alpha) v I c \right] M ^ {2} - (1 - \alpha) (M - N) ^ {2} (v I c - s I e) \right\}\tag{C.6}
$$

Combining Eqs. (C.6) and (15) we have

$$
\frac {\partial Z _ {2} (m , s , T)}{\partial T} > D \left[ \frac {(X + c Y)}{1 - E (p)} + \alpha s I e + (1 - \alpha) v I c \right] \left[ M ^ {2} - T ^ {2} \right] > 0 \text {   for   } T \in (M - N, M)
$$

Thus, $Z _ { 2 } ( m , s , T )$ is strictly increasing function o $\because T \in [ M - N , M ]$ and thereby $Z _ { 2 } ( m , s , T )$ has maximum value at boundary point $T = M ,$ . This completes the proof of Appendix C.

## Appendix D. Proof of Lemma 6

Taking derivative of $g _ { i } ( s ) \ ( i = 1 , 2 )$ in Eqs. (31) and (32) respec tively with respect to s, we have

$$
\frac {d g _ {1} (s)}{d s} = a b s ^ {- b - 1} \left[ \frac {X}{1 - E (p)} + \left(c _ {0} + \frac {2 c _ {2} a s ^ {- b}}{\rho}\right) \frac {Y}{1 - E (p)} + \frac {s l e (b - 1)}{b} \right] (M - N) ^ {2} > 0
$$

$$
\begin{array}{l} \frac {d g _ {2} (s)}{d s} = a b s ^ {- b - 1} \left\{\left[ \frac {X}{1 - E (p)} + \left(c _ {0} + \frac {2 c _ {2} a s ^ {- b}}{\rho}\right) \frac {Y}{1 - E (p)} \right] M ^ {2} \right. \\ \left. + \frac {s I e (b - 1)}{b} \left[ \alpha M ^ {2} + (1 - \alpha) (M - N) ^ {2} \right] + (1 - \alpha) v I c \left[ M ^ {2} - (M - N) ^ {2} \right] \right\} > 0 \end{array}
$$

So $g _ { i } ( s ) \ ( i = 1 , 2 )$ are strictly increasing functions of s. Since $\varDelta _ { 1 } > \varDelta _ { 2 }$ we can see that $g _ { 1 } ( s ) > g _ { 2 } ( s )$ for all $s \in ( 0 , \infty )$ . Moreover, for $i = 1 , 2 ,$ $\operatorname* { l i m } _ { s \to 0 + } g _ { i } ( s ) = - \infty$ and $\operatorname* { l i m } _ { { \mathfrak { c } } \to \infty } g _ { i } ( s ) = 2 { \overline { { A } } } > 0$ . Therefore, by Intermediate Value Theorem, we can <sup>fi</sup>nd unique values $\widetilde s _ { i } ( i = 1 , 2 )$ such that

$$
\begin{array}{l} g _ {1} (\tilde {s} _ {1}) = 2 \bar {A} - a \tilde {s} _ {1} ^ {- b} \left[ \frac {X}{1 - E (p)} + \left(c _ {0} + \frac {c _ {1} \rho}{a \tilde {s} _ {1} ^ {- b}} + \frac {c _ {2} a \tilde {s} _ {1} ^ {- b}}{\rho}\right) \frac {Y}{1 - E (p)} + \tilde {s} _ {1} I e \right] \\ \times (M - N) ^ {2} = 0 \end{array}
$$

and

$$
\begin{array}{l} g _ {2} (\tilde {s} _ {2}) = 2 \bar {A} - a \tilde {s} _ {2} ^ {- b} \left\{\left[ \frac {X}{1 - E (p)} + \left(c _ {0} + \frac {c _ {1} \rho}{a \tilde {s} _ {2} ^ {- b}} + \frac {c _ {2} a \tilde {s} _ {2} ^ {- b}}{\rho}\right) \frac {Y}{1 - E (p)} \right] M ^ {2} \right. \\ \left. + \tilde {s} _ {2} l e [ \alpha M ^ {2} + (1 - \alpha) (M - N) ^ {2} ] + (1 - \alpha) v l c [ M ^ {2} - (M - N) ^ {2} ] \right\} = 0 \end{array}
$$

From the above discussion and $\Delta _ { 1 }$ and $\Delta _ { 2 }$ be de<sup>fi</sup>ned as in (20) and (22) respectively, we can easily derive $( \mathsf { a } ) \ \Delta _ { 1 } { \leq } 0$ if and only if $s { \le } \tilde { s } _ { 1 }$ $( \mathsf { b } ) \ \Delta _ { 2 } { \leq } 0 { \leq } \Delta _ { 1 }$ if and only $\mathrm { i f } \ \tilde { s } _ { 1 } \le s \le \tilde { s } _ { 2 } , ( \mathrm { c } ) \ \Delta _ { 2 } \ge 0$ if and only if $s \geq \tilde { s } _ { 2 }$ This completes the proof of Appendix D.

## Appendix E. Proof of Lemma 7

Taking derivative of $g _ { 3 } ( s )$ in Eq. (40) with respect to s, we have

$$
\begin{array}{l} \frac {d g _ {3} (s)}{d s} = a b s ^ {- b - 1} \left[ \frac {X}{1 - E (p)} + \left(c _ {0} + \frac {2 c _ {2} a s ^ {- b}}{\rho}\right) \frac {Y}{1 - E (p)} \right. \\ \left. + \frac {\alpha s I e (b - 1)}{b} + (1 - \alpha) v I c \right] M ^ {2} > 0 \end{array}
$$

So $g _ { 3 } ( s )$ is strictly increasing functions of s.

Moreover, lim $g _ { 3 } ( s ) = - \infty$ and lim $g _ { 3 } ( s ) = 2 \bar { A } > 0$ . Therefore, by s→0+ S→∞ Intermediate Value Theorem, we can <sup>fi</sup>nd unique value ${ \tilde { s } } _ { 3 }$ such that

$$
\begin{array}{l} g _ {3} \left(\tilde {s} _ {3}\right) = 2 \bar {A} - a \tilde {s} _ {3} ^ {- b} \left[ \frac {X}{1 - E (p)} + \left(c _ {0} + \frac {c _ {1} \rho}{a \tilde {s} _ {3} ^ {- b}} + \frac {c _ {2} a \tilde {s} _ {3} ^ {- b}}{\rho}\right) \frac {Y}{1 - E (p)} \right. \\ \left. + \alpha \tilde {s} _ {3} I e + (1 - \alpha) v I c \right] M ^ {2} = 0 \end{array}
$$

Now, it is easy to show that $( { \bf a } ) \Delta _ { 3 } \le 0$ if and only $\mathrm { i f } s \le \widetilde { s } _ { 3 } \left( \mathrm { b } \right) \Delta _ { 3 } \ge 0$ if and only $\mathrm { i f } s { \ge } \tilde { s } _ { 3 }$

This completes the proof of Appendix E.

## References

[1] P.L. Abad, C.K. Jaggi, A joint approach for setting unit price and the length of the trade credit period for a seller when end demand is price sensitive, International Journal of Production Economics 83 (2003) 115–122

[2] S.P. Aggarwal, C.K. Jaggi, Ordering policies of deteriorating items under permissible delay in payments, Journal of the Operational Research Society 46 (1995) 658–662.

[3] K. Annadurai, R. Uthayakumar, Controlling setup cost in (Q, r, L) inventory model with defective items, Applied Mathematical Modelling 34 (2010) 1418–1427.

[4] D. Biskup, D. Simon, H. Jahnke, The effect of capital lockup and customer trade credits on the optimal lot size – a con<sup>fi</sup>rmation of the EPQ, Computers and Operations Re search 30 (2003) 1509–1524.

[5] H.J. Chang, C.Y. Dye, An inventory model for deteriorating items with partial backlogging and permissible delay in payments, International Journal of Systems Science 32 (2001) 345–352.

[6] C.T. Chang, J.T. Teng, M.S. Chern, Optimal manufacturer's replenishment policies for deteriorating items in a supply chain with up-stream and down-stream trade credits, International Journal of Production Economics 127 (2010) 197–202

[7] L.H. Chen, F.S. Kang, Integrated vendor-buyer cooperative inventory models with variant permissible delay in payments, European Journal of Operational Research 183 (2007) 658–673.

[8] L.H. Chen, F.S. Kang, Coordination between vendor and buyer considering trade credit and items of imperfect quality, International Journal of Production Economics 123 (2010) 52–61.

[9] L.H. Chen, F.S. Kang, Integrated inventory models considering the two-level trade credit policy and a price-negotiation scheme, European Journal of Operationa Research 205 (2010) 47–58.

[10] K.J. Chung, Y.F. Huang, The optimal cycle time for EPQ inventory model under permissible delay in payments, International Journal of Production Economics 84 (2003) 307–318.

[11] S.K. Goyal, Economic order quantity under conditions of permissible delay in payments, Journal of the Operational Research Society 36 (1985) 335–338.

[12] L.A. Guardiola, A. Meca, J. Timmer, Cooperation and pro<sup>fi</sup>t allocation in distribution chains, Decision Support Systems 44 (2007) 17–27.

[13] C.H. Ho, A minimax distribution free procedure for an integrated inventory model with defective goods and stochastic lead time demand, International Journal of Information and Management Sciences 20 (2009) 161–171.

[14] C.H. Ho, The optimal integrated inventory policy with price-and-credit-linked demand under two-level trade credit, Computers and Industrial Engineering 60 (2011) 117–126.

[15] C.H. Ho, L.Y. Ouyang, C.H. Su, Optimal pricing, shipment and payment policy for an integrated supplier–buyer inventory model with two-part trade credit, European Journal of Operational Research 187 (2008) 496–510.

[16] Y.F. Huang, Optimal retailer's ordering policies in the EOQ model under trade credit <sup>fi</sup>nancing, Journal of the Operational Research Society 54 (2003) 1011–1015.

[17] Y.F. Huang, An inventory model under two levels of trade credit and limited storage space derived without derivatives, Applied Mathematical Modelling 30 (2006) 418–436.

[18] Y.F. Huang, Optimal retailer's replenishment decisions in the EPQ model under two levels of trade credit policy, European Journal of Operational Research 176 (2007) 1577–1591.

[19] Y.F. Huang, K.H. Hsu, An EOQ model under retailer partial trade credit policy in supply chain, International Journal of Production Economics 112 (2008) 655–664.

[20] S.Y. Hung, S.I. Chang, D.C. Yen, T.C. Kang, C.P. Kuo, Successful implementation of collaborative product commerce: an organizational fit perspective. Decision Support Systems 50 (2011) 501–510.

[21] C.K. Jaggi, S.K. Goyal, S.K. Goel, Retailer's optimal replenishment decisions with credit-linked demand under permissible delay in payments, European Journal of Operational Research 190 (2008) 130–135.

[22] B.A. Jalbar, J.M. Gutiérrez, J. Sicilia, Policies for a single-vendor multi-buyer system with <sup>fi</sup>nite production rate, Decision Support Systems 46 (2008) 84–100.

[23] A.M.M. Jamal, B.R. Sarker, S. Wang, An ordering policy for deteriorating items with allowable shortage and permissible delay in payment, Journal of the Operational Research Society 48 (1997) 826–833.

[24] M. Khouja, The economic production lot size model under volume <sup>fl</sup>exibility Computers and Operations Research 22 (1995) 515–523.

[25] V.B. Kreng, S.J. Tan, Optimal replenishment decision in an EPQ model with defective items under supply chain trade credit policy, Expert Systems with Applications 38 (2011) 9888–9899.

[26] Y. Kristianto, A. Gunasekaran, P. Helo, M. Sandhu, A decision support system for integrating manufacturing and product design into the recon<sup>fi</sup>guration of the supply chain networks, Decision Support Systems 52 (2012) 790–801.

[27] J.J. Liao, An EOQ model with noninstantaneous receipt and exponentially deteriorating items under two-level trade credit, International Journal of Production Economics 113 (2008) 852–861.

[28] L.Y. Ouyang, C.H. Ho, C.H. Su, Optimal strategy for an integrated system with variable production rate when the freight rate and trade credit are both linked to the order quantity, International Journal of Production Economics 115 (2008) 151–162.

[29] S.S. Sana, A production-inventory model of imperfect quality products in a three-layer supply chain, Decision Support Systems 50 (2011) 539–547.

[30] H. Soni, N.H. Shah, C.K. Jaggi, Inventory models and trade credit: a review, Control and Cybernetics 39 (2010) 867–882.

[31] C.H. Su, L.Y. Ouyang, C.H. Ho, C.T. Chang, Retailer's inventory policy and supplier's delivery policy under two-level trade credit strategy, Asia-Paci<sup>fi</sup>c Journal of Operational Research 24 (2007) 613–630.

[32] J.G. Szmerekovsky, V. Tilson, J. Zhang, Analytical model of adoption of item level RFID in a two-echelon supply chain with shelf-space and price-dependent demand, Decision Support Systems 51 (2011) 833–841.

[33] J.T. Teng, On the economic order quantity under conditions of permissible delay in payments, Journal of the Operational Research Society 53 (2002) 915–918.

[34] J.T. Teng, Optimal ordering policies for a retailer who offers distinct trade credits to its good and bad credit customers, International Journal of Production Economics 119 (2009) 415–423.

[35] J.T. Teng, C.T. Chang, Optimal manufacturer's replenishment policies in EPQ model under two levels of trade credit policy, European Journal of Operational Research 195 (2009) 358–363.

[36] J.T. Teng, S.K. Goyal, Optimal ordering policy for a retailer in a supply chain with up-stream and down-stream trade credits, Journal of the Operational Research Society 58 (2007) 1252–1255.

[37] J.T. Teng, C.T. Chang, M.S. Chern, Vendor-buyer inventory models with trade credit <sup>fi</sup>nancing under both non-cooperative and integrated environments, International Journal of Systems Science (in press) http://dx.doi.org/10.1080/00207721.2011. 564322.

[38] A. Thangam, R. Uthayakumar, Two-echelon trade credit <sup>fi</sup>nancing for perishable items in a supply chain when demand depends on both selling price and credit period, Computers and Industrial Engineering 57 (2009) 773–786.

[39] P.C. Yang, H.M. Wee, A collaborative inventory system with permissible delay in payments for deteriorating items, Mathematical and Computer Modelling 43 (2006) 209–221.

[40] S.W. Yoon, S.Y. Nof, Demand and capacity sharing decisions and protocols in a collaborative network of enterprises, Decision Support Systems 49 (2010) 442–450.

[41] J. Zhang, G.V. Frazier, Strategic alliance via co-opetition: supply chain partnership with a competitor, Decision Support Systems 51 (2011) 853–863.

Hardik N Soni is an Associate Professor at Chimanbhai Patel Post Graduate Institute of Computer Applications, Ahmedabad, India. He received his BSc and MSc in Mathematics from Guiarat University, Ahmadabad, Guiarat, India. He received his PhD in Mathematics from Gujarat University. His major research interests are in inventory control/optimization and cooperation and coordination within supply chains. He has published his research works in refereed journals.

Kamlesh A Patel received his MSc degree from Sardar Patel University, India. Presently, he is working as an Assistant Professor in Mathematics department at Shri U. P. Arts & Smt. M. G. Panchal Science & Shri V. L. Shah Commerce College, Pilvai, Gujarat, India. He is also a PhD candidate of Kadi Sarva VishwaVidvalava. His research interests are in inventory control/optimization in uncertain environments.
