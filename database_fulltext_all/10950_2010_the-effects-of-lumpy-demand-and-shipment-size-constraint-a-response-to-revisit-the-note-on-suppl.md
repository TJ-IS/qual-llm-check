---
otero_id: 10950
otero_key: "8SWVY6NE"
title: "The effects of lumpy demand and shipment size constraint: A response to “Revisit the note on supply chain integration in vendor-managed inventory”"
authors: "Boray Huang; Zhisheng Ye"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.08.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The effects of lumpy demand and shipment size constraint: A response to “Revisit the note on supply chain integration in vendor-managed inventory”

Boray Huang ⁎, Zhisheng Ye

Department of Industrial and Systems Engineering, National University of Singapore, 117576, Singapore, Singapore

a r t i c l e i n f o

Available online 1 September 2009

Keywords: Vendor management inventory Supply chain integration Lumpy demand

## a b s t r a c t

This paper responds to a comment by Wang et al. [3] regarding the disagreement between Yao et al. [4] and van der Vlist et al. [2] on the impact of vender-managed-inventory (VMI). We explore the factors which affect the shipment size from the vendor to the buyer and identify the conditions where the shipment size will increase/decrease under VMI. A numerical example also shows when and how the inventory shifts between the supplier and the buyer.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

Wang et al. [3] try to resolve a disagreement between Yao et al. [4] and van der Vlist et al. [2] regarding the impact of vendor-managedinventory (VMI) on a supply chain. Yao et al. [4] use a two-tier EOQ model to investigate the costs and order behaviours of the supply chain members in both VMI and non-VMI scenarios. They <sup>fi</sup>nd some interesting analytical results and identify the distribution of the VMI bene<sup>fi</sup>t between the supplier and the buyer. van der Vlist et al. [2] argue that Yao et al. overstate the inventory needed at the supplier, and extend Yao et al.'s model to incorporate shipping costs. The <sup>fi</sup>ndings in Yao et al. [4] and van der Vlist et al. [2] are different in many ways. For example, Yao et al. assert that the buyer's order size shall decrease under VMI, but van der Vlist et al. have an opposite result. In their response [5], Yao et al. argue that van der Vlist et al. [2] make problematic assumptions on the shipping costs. Wang et al. [3] also support Yao et al.'s original results by studying a special case.

It is interesting to note that, while the arguments of Yao et al. [5] and Wang et al. [3] focus on the validity of van der Vlist et al.'s cost assumptions, some of the results in van der Vlist et al. do not rely on these assumptions. To clarify the causes of the disagreement, we relax all the extra assumptions in van der Vlist et al. [2], let the delivery cost be zero and revisit the original paper of Yao et al. [4]. In this note we discuss two important factors on the bene<sup>fi</sup>t of VMI: The lumpy demand at the suppliers and the shipment size constraint. Both are neglected in all these papers. Our study clearly shows how these two factors affect the optimal order quantities, and provides intuitive insights for the implementation of VMI.

## 2. The cost functions and the optimal solutions

We use the same models and notations in Yao et al. [4]. The supply chain consists of one buyer and one supplier. The buyer's order size is q and the supplier's order size is Q. From Crowston et al. [1] and Zipkin ([6], Theorem 5.3.2), it is obvious that the supplier's order pattern in van der Vlist et al.'s synchronized case is the optimal stationary pattern for both the supplier and the entire supply chain. In other words, the supplier's ordering pattern presumed in Yao et al. [4], which always keeps excessive q units on hand, is an inferior one.

With the order pattern in the synchronized case of van der Vlist et al., the total cost function for the entire system in the non-VMI (NV) case is

$$
T C _ {\mathrm{NV}} (Q, q) = T C _ {\mathrm{NV}} ^ {S} (Q, q) + T C _ {\mathrm{NV}} ^ {R} (q)\tag{1}
$$

where

$$
T C _ {\mathrm{NV}} ^ {S} (Q, q) = \frac {C r}{Q} + H \left(\frac {Q - q}{2}\right)\tag{2}
$$

$$
= \left[ \frac {C r}{Q} + H \left(\frac {Q}{2}\right) \right] - H \left(\frac {q}{2}\right)\tag{3}
$$

$$
T C _ {\mathrm{NV}} ^ {\mathrm{R}} (q) = \frac {c r}{q} + h \left(\frac {q}{2}\right)\tag{4}
$$

$$
Q \geq q > 0.
$$

$\mathrm { T C } _ { \mathrm { N V } } ^ { S }$ and $\mathrm { T C } _ { \mathrm { N V } } ^ { R }$ are respectively the cost functions of the supplier and of the buyer. Our cost function $\mathrm { T C } _ { \mathrm { N V } }$ is different from the ones in [2] and [4] for the non-VMI case (e.g., Eq. (1) of [2] when T=0 and Eq. (3) of [4].) The difference is due to the fact that both [2] and [4] overlook the effect of lumpy demand (i.e., the last term in (3)) faced by the supplier. Interestingly, this effect is included in the supplier's cost functions of their VMI models.

<sup>1</sup>Note that the lumpy demand from the buyer does not affect the supplier's optimal decision of the order size Q unless the buyer's order size is suf<sup>fi</sup>ciently large (that is, when the condition $Q { \geq } q$ is concerned.) However, it does affect the supplier's cost performance. Thus the effect of lumpy demand at the supplier becomes an important factor for the decision of the shipment size in the VMI case.

Go back to the non-VMI (NV) case, the optimal order quantities can be determined directly from the classic EOQ solution to (3) and (4). That is,

$$
q ^ {*} = \sqrt {\frac {2 c r}{h}}\tag{5}
$$

$$
Q ^ {*} = \sqrt {\frac {2 C r}{H}}.\tag{6}
$$

When $q ^ { * } > Q ^ { * } ,$ , the supplier's order size will be raised to $q ^ { * }$ because, as shown in the proof of Proposition 1, it is never optimal for the supplier to have an order size Q<q. As a result, we have the optimal order quantities and the optimal cost functions for the non-VMI case: (All the proofs in this note are shown in Appendix.)

Proposition 1. In the non-VMI (NV) case, the optimal order quantities $Q _ { \mathrm { N V } } ^ { * }$ and $q _ { \mathrm { N V } } ^ { * }$ under the condition $q _ { \mathrm { N V } } ^ { * } { \leq } Q _ { \mathrm { N V } } ^ { * }$ are

$$
\begin{array}{l} q _ {\mathrm{NV}} ^ {*} = \sqrt {\frac {2 c r}{h}} \\ Q _ {\mathrm{NV}} ^ {*} = \max \left\{q _ {\mathrm{NV}} ^ {*}, \sqrt {\frac {2 C r}{H}} \right\} \end{array}
$$

The optimal cost function of the entire system without VMI is

$$
T C _ {\mathrm{NV}} ^ {*} = \left\{ \begin{array}{c c} \sqrt {2 c r h} + \sqrt {2 C r H} - H \sqrt {\frac {c r}{2 h}} & ; \text {when} c \leq \frac {h}{H} C \\ \left(\frac {C}{2 c} + 1\right) \sqrt {2 c r h} & ; \text {when} c > \frac {h}{H} C. \end{array} \right.\tag{7}
$$

When VMI is implemented, the buyer's order cost c is replaced by $c ^ { \prime } ,$ where $c ^ { \prime } \leq c$ as assumed in Yao et al. [4]. The total cost function (1) can therefore be rewritten as

$$
T C _ {\mathrm{VMI}} (Q, q) = T C _ {\mathrm{VMI}} ^ {S} (Q, q) + T C _ {\mathrm{VMI}} ^ {R} (q)\tag{8}
$$

$$
= \left\{\frac {C r}{Q} + H \left(\frac {Q - q}{2}\right) \right\} + \left\{\frac {c ^ {\prime} r}{q} + h \left(\frac {q}{2}\right) \right\}\tag{9}
$$

$$
= \left[ \frac {C r}{Q} + H \left(\frac {Q}{2}\right) \right] + \left[ \frac {c ^ {\prime} r}{q} + (h - H) \left(\frac {q}{2}\right) \right]\tag{10}
$$

where $Q { \geq } q { > } 0$ . We de<sup>fi</sup>ne $\mathrm { T C } _ { \mathrm { V M I } } ^ { S }$ and $\mathrm { T C } _ { \mathrm { V M I } } ^ { R }$ as the total costs at the supplier's side and at the buyer's side, respectively. Within the <sup>fi</sup>rst square bracket of (10) we have a classic EOQ cost which depends only on Q. The second square bracket of (10) also contains a classic EOQ cost but depends only on q. When the decision making is centralized in the VMI case, the optimal order quantities and the optimal cost can be obtained by optimizing the two EOQ costs in the square brackets of (10) with respect to Q and q separately. We can immediately obtain

$$
Q ^ {*} = \sqrt {\frac {2 C r}{H}}\tag{11}
$$

$$
q ^ {*} = \sqrt {\frac {2 c ^ {'} r}{h - H}}\tag{12}
$$

when $c ^ { ' } { \leq } \frac { h - H } { H } C .$ . A tricky case occurs when $c ^ { ' } > \frac { h - H } { H } C ,$ , which is equivalent to $q ^ { * } { > } Q ^ { * }$ . van der Vlist et al. [2] indicates that we can let $q _ { \mathrm { V M I } } ^ { * } = Q _ { \mathrm { V M I } } ^ { * }$ whenever h≤H, but they do not solve the problem of the optimal order quantities in the more general situation of $\{ q ^ { * } > Q ^ { * } \}$ , nor do they provide exact expressions of $\{ Q _ { \mathrm { V M I } } ^ { * } , q _ { \mathrm { V M I } } ^ { * } \}$ when h≤H. We find $\left\{ Q = q = { \sqrt { \frac { 2 C r } { H } } } \right\}$ is not an optimal solution to $\mathrm { T C } _ { \mathrm { V M I } }$ whenever $c ^ { \prime } > \frac { h ^ { \setminus } - H } { H } C$ (including the case of $h { \le } H . )$ In fact, we have the following proposition:

Proposition 2. In the VMI case, the optimal order quantities $Q _ { \mathrm { V M I } } ^ { * }$ and $q _ { \mathrm { V M I } } ^ { * }$ under the constraint Q≥q are

$$
(Q _ {\mathrm{VMI}} ^ {*}, q _ {\mathrm{VMI}} ^ {*}) = \left\{ \begin{array}{l l} \left(\sqrt {\frac {2 C r}{H}}, \sqrt {\frac {2 c ^ {\prime} r}{h - H}}\right) & ; \text {   when   } c ^ {\prime} \leq \frac {h - H}{H} C \\ \left(\sqrt {\frac {2 (c ^ {\prime} + C) r}{h}}, \sqrt {\frac {2 (c ^ {\prime} + C) r}{h}}\right) & ; \text {   when   } c ^ {\prime} > \frac {h - H}{H} C. \end{array} \right.
$$

The optimal cost function under VMIis

$$
T C _ {\mathrm{VMI}} ^ {*} = \left\{ \begin{array}{c c} \sqrt {2 c ^ {\prime} r (h - H)} + \sqrt {2 C r H} & ; \text {when} c ^ {\prime} \leq \frac {h - H}{H} C \\ \sqrt {2 (c ^ {\prime} + C) r h} & ; \text {when} c ^ {\prime} > \frac {h - H}{H} C. \end{array} \right.\tag{13}
$$

## 3. The impact of VMI

The supplier's cost function $\mathsf { T C } ^ { S }$ provides a quick answer to the impact of lumpy demand. The last term of (3) is independent of Q and represents the impact of the lumpy demand in the non-VMI case. The total cost function of the VMI case has the same structure. It is then easy to obtain the following property which holds in both VMI and non-VMI cases.

Corollary 1. The cost at the supplier's side is non-increasing in the buyer's order size.

According to Corollary 1, the centralized decision maker in the VMI case may want to increase the buyer's order size from its non-VMI solution $\left( \sqrt { 2 c ^ { ' } r / h } \right)$ in order to bene<sup>fi</sup>t from the cost reduction at the supplier. In fact, the buyer's order size shall be set to a point where the marginal increase of the buyer's cost equals to the marginal saving of the supplier's cost if the $q \leq Q$ constraint is not concerned. That is, q should satisfy

$$
\frac {d}{d q} T C _ {\mathrm{VMI}} ^ {\mathrm{R}} = - \frac {c ^ {\prime} r}{q ^ {2}} + \frac {h}{2} = - \left(- \frac {H}{2}\right) = - \frac {\partial}{\partial q} T C _ {\mathrm{VMI}} ^ {\mathrm{s}}\tag{14}
$$

when $q = q _ { \mathrm { { V M I } } } ^ { * }$ and $c ^ { \prime } { \leq } \frac { h - H } { H } C .$ . As a result, we have

$$
q _ {\mathrm{VMI}} ^ {*} = \sqrt {\frac {2 c ^ {'} r}{h - H}}
$$

which is exactly the same result as (12).

To the contrary, the non-optimal ordering pattern in Yao et al. [4] causes the following cost function for the supplier:

$$
T C _ {S} ^ {\mathrm{Yao}} (Q, q) = \left[ \frac {C r}{Q} + H \left(\frac {Q}{2}\right) \right] + H \left(\frac {q}{2}\right)\tag{15}
$$

which owns the opposite property: The total cost at the supplier's side increases with the buyer's order size q. One of the reasons is the excessive inventory the supplier keeps. The larger is q, the higher is the supplier's inventory cost. Thus in the VMI case, it would be better off for the centralized decision maker to lower the buyer's order size from the classic EOQ solution in order to reduce the inventory cost at the supplier.

We now have the following proposition which corresponds to Proposition 1 of Yao et al. [4].

Proposition 3. When $c ^ { \prime } + c > c \geq c ^ { \prime } > { \frac { h - H } { h } } c ,$ the optimal shipment size $q _ { \mathrm { V M I } } ^ { * }$ from the supplier to the buyer increases in the VMI case. That is, $q _ { \mathrm { V M I } } ^ { \ast } > q _ { \mathrm { N V } } ^ { \ast }$

Note that we do not use the replenish frequency to describe the buyer's order behaviour in Proposition 3. Instead, we use the shipment sizes $q _ { \mathrm { N V } } ^ { * }$ and $q _ { \mathsf { V M I } } ^ { * }$ to demonstrate the real frequency of the buyer's orders. When the shipment size is smaller, the buyer places more orders within a <sup>fi</sup>xed duration.

From Corollary 1 and Proposition 3, we have a clear picture about the change of the shipment size when VMI is implemented. There are three driving forces which affect the optimal shipment size in the VMI case: First, the lumpy demand at the supplier. When the supplier's order pattern is optimal as in van der Vlist et al.'s synchronized case, the centralized decision maker under VMI tends to increase the shipment size q in order to bring more cost reduction at the supplier's side. Second, the buyer's ordering cost, which is usually lower under VMI and forms the opposite force to drag down the shipment size. When the buyer's order cost c′ is not low enough $( \mathrm { i . e . , } c ^ { ' } > ^ { ' } \frac { h - H } { h } c , )$ the optimal shipment size $q _ { \mathsf { V M I } } ^ { * }$ is larger than $q _ { \mathrm { N V } } ^ { * }$ (in the case where the constraint $q \leq Q$ is not a concern.) Otherwise, the centralized decision maker can take advantage of the low order cost at the buyer and reduce the shipment size. Third, the shipment size limitation $q { \leq } Q , \Lambda s$ shown in the proof, the condition $c ^ { \prime } + C > c$ in Proposition 3 is related to the constraint $q \leq Q ,$ When the supplier's order cost C is so small that $C \leq c - c ^ { \prime }$ , the constraint become a concern which may result in a upper bound for the shipment size q.

To demonstrate our results, we use the same numerical example from Figure 3 of Yao et al. [4]. In the <sup>fi</sup>gure of Yao et al., the supplier's total holding cost is always higher under VMI while the buyer always enjoys the bene<sup>fi</sup>t of reduced inventory. Yao et al. suggest that “VMI shifts inventory from the buyer to the supplier to take advantage of the lower carrying charge at the supplier's site.” However, this reason does not explain why the buyer's inventory holding cost is reduced the most (by shifting more inventory to the supplier?) when the supplier's holding cost rate is the highest $\textstyle ( d = H / h = 1 )$ in their <sup>fi</sup>gure.

Fig. 1 shows the revised version on the effect of the holding cost ratio d. In this case we <sup>fi</sup>nd the buyer's order size $q _ { \mathsf { V M I } } ^ { * }$ increases with d because it becomes more expensive to hold inventory at the supplier when d is high. When d is small (<0.5), which yield a higher threshold value of ${ \big . } { \frac { h - H } { h } } c$ in Proposition 3, q<sup>⁎</sup> is smaller than $\bar { q } _ { \mathrm { N V } } ^ { * }$ and the supplier has a higher inventory under VMI. On the other hand, the shipment size q<sup>⁎</sup> is larger than $q _ { \mathrm { N V } } ^ { * }$ when d is large (>0.5,) meaning more inventory is shifted from the supplier to the buyer. The increase of the buyer's inventory holding cost, however, has a limit due to the constraint $q \leq Q ,$ In addition, the optimal order sizes $Q _ { \mathrm { V M I } } ^ { * }$ and $q _ { \mathsf { V M I } } ^ { * }$ are equal when d≥2/3, which implies a crossdocking strategy (with 100% inventory holding cost saving) for the supplier if its inventory holding cost rates is not much lower than the buyer's.

![](/api/attachments/8SWVY6NE/fulltext/images/ab1612ac65c4edb2196bc594b7c2c6d5c45dcd798b8246ba09c7f1e41c524a7d.jpg)  
Fig. 1. Inventory holding cost savings under VMI (when $g = C / c = 1$ and $g ^ { \prime } { = } C / c ^ { \prime } { = } 2 )$

One more noteworthy issue is the supplier's order size Q. Yao et al. [4] and van der Vlist et al. [2] claim that the supplier's optimal order size remains the same when VMI is introduced. We <sup>fi</sup>nd that, as long as the shipment size constraint $q \leq Q$ is concerned, the optimal order size of the supplier may be greater than its classic EOQ solution ${ \sqrt { \frac { 2 C r } { H } } } .$

## 4. Conclusions

In this paper, we have shown that the original models in Yao et al. [4] are problematic in two ways: First, the supplier in their models adopts an order pattern which causes excessive inventory all the time. The amount of excessive inventory is proportional to the buyer's order size q. Second, while the lumpy demand at the supplier is modeled in the VMI case, it is overlooked in the non-VMI case. van der Vlist et al. [2] identify the <sup>fi</sup>rst drawback, but fail to <sup>fi</sup>nd the second one. In addition, van der Vlist et al. do not provide clear answers to the situation where the shipment size constraint $Q { \geq } q$ is concerned. While Yao et al. [5] and Wang et al. [3] focus their responses on the validity of van der Vlist et al.'s cost assumptions, we <sup>fi</sup>nd that these assumptions are not required for a different result from Yao et al.'s [4]. We then revisit the original paper of Yao et al. [4] to identify the dynamics of the order behaviour when VMI is implemented. By showing the conditions where $q _ { \mathrm { V M I } } ^ { * } > q _ { \mathrm { N V } } ^ { * }$ or $q _ { \mathrm { V M I } } ^ { * } \leq q _ { \mathrm { N V } } ^ { * }$ , we resolve the disagreement between Yao et al. [4] and van der Vlist et al. [2] without extra assumptions and special cases. We also provide an intuitive view of the cost functions so that most optimal quantities can be derived from the properties of the EOQ model (e.g., convexity), without going through the <sup>fi</sup>rst and second order conditions.

## Appendix A

Proof of Proposition 1. From (5) and $( 6 ) , q ^ { * } { > } Q ^ { * }$ implies $c > ( h / H ) C ,$ and the proposition follows. Note that it is never optimal for the supplier (and the supply chain) to have $Q _ { \mathrm { N V } } ^ { * } < q _ { \mathrm { N V } } ^ { * }$ . If $Q _ { \mathrm { N V } } ^ { * } < q _ { \mathrm { N V } } ^ { * }$ the supplier's order frequency is higher than the buyers'. Thus the supplier's inventory will accumulates over time before the arrival of the buyer's next order. Instead, the supplier can increase its order size to $q _ { \mathrm { N V } } ^ { * }$ so that the total ordering cost is lower (due to a larger order,) and the total holding cost is zero (since no inventory is accumulated.) As a result, we have

$$
Q _ {N V} ^ {*} = \left\{ \begin{array}{c c} \sqrt {\frac {2 C r}{H}} & ; \text { when } c \leq \frac {h}{H} C \\ q _ {N V} ^ {*} = \sqrt {\frac {2 c r}{h}} & ; \text { when } c > \frac {h}{H} C. \end{array} \right.\tag{16}
$$

The optimal cost function without VMI can then be obtained from (1) by letting $q = q _ { \mathrm { N V } } ^ { * }$ and $Q = Q _ { \mathrm { N V } } ^ { * }$

Proof of Proposition 2. We <sup>fi</sup>rst <sup>fi</sup>nd the optimal solution of $\mathrm { T C } _ { \mathrm { V M I } }$ under the condition $Q = q .$ . When $Q = q , \mathrm { T C } _ { \mathrm { V M I } } ( Q , q )$ in (9) becomes

$$
T C _ {\mathrm{VMI}} (q, q) = \frac {C r}{q} + \frac {c ^ {\prime} r}{q} + h \left(\frac {q}{2}\right) = \frac {(C + c ^ {\prime}) r}{q} + h \left(\frac {q}{2}\right)\tag{17}
$$

which is a classic EOQ cost with a ordering cost $( C + c ^ { \prime } )$ per order and a holding cost rate h. Let $q _ { \mathrm { e } } ^ { * }$ denote the optimal solution of (17). In other words,

$$
q _ {\mathrm{e}} ^ {*} = \sqrt {\frac {2 (C + c ^ {'}) r}{h}}.\tag{18}
$$

The proof of Proposition 1 has shown that any $( Q , q )$ with $Q < q$ is never the optimal solution to $\mathrm { T C } _ { \mathrm { V M I } }$ because we can always set Q to q and get a lower total cost. Therefore, with the condition $Q { \geq } q$ for ${ \mathrm { T C } } _ { \mathrm { V M I } }$ the following proof includes three parts:

1. $c ^ { ' } < \frac { h - H } { H } C .$ . The condition implies that h>H because $c ^ { \prime }$ cannot be negative. In this case, we have ${ \boldsymbol { Q } } ^ { * } { \ge } { \boldsymbol { q } } ^ { * }$ from (11) and (12). The constraint $Q { \ge } q$ is not a concern for $\mathrm { T C } _ { \mathrm { V M I } } ( \boldsymbol { Q } ^ { * } , \boldsymbol { q } ^ { * } )$ . Thus

$$
\{Q _ {\mathrm{VMI}} ^ {*}, q _ {\mathrm{VMI}} ^ {*} \} = \{Q ^ {*}, q ^ {*} \} = \left\{\sqrt {\frac {2 C r}{H}}, \sqrt {\frac {2 c ^ {\prime} r}{h - H}} \right\}
$$

2. $c ^ { ' } { \geq } \frac { h - H } { H } C$ and $h { \leq } H .$ . Because $h - H$ is negative, it is easy to see <sup>H</sup> from (10) that $\mathrm { T C } _ { \mathrm { V M I } }$ is decreasing in q. That is, for any $q \leq Q ,$ we have $\mathrm { T C } _ { \mathrm { V M I } } ( Q , \ q ) { \geq } \mathrm { T C } _ { \mathrm { V M I } } ( Q , Q ) { \geq } \mathrm { T C } _ { \mathrm { V M I } } ( q _ { \mathrm { e } } ^ { * } , \ q _ { \mathrm { e } } ^ { * } )$ . As a result, $q _ { \mathrm { e } } = \sqrt { 2 ( c ^ { \prime } + C ) r / }$ fifififih is the optimal solution of $Q _ { \mathrm { V M I } } ^ { * }$ and $q _ { \mathrm { V M I } } ^ { * }$

3. $c ^ { ' } { \geq } \frac { h - H } { H } C$ and $h { > } H .$ . Note that we can re-write the cost function ${ \mathrm { T C } } _ { \mathrm { V M I } } { \mathrm { ~ a s ~ } }$

$$
T C _ {\mathrm{VMI}} (Q, q) = T C _ {1} (Q) + T C _ {2} (q)
$$

4. where

$$
\begin{array}{l} T C _ {1} (Q) = \frac {C r}{Q} + H \left(\frac {Q}{2}\right) \\ T C _ {2} (q) = \frac {c ^ {\prime} r}{q} + (h - H) \left(\frac {q}{2}\right) \end{array}
$$

5. We now show the following equivalence when $h > H ;$

$$
\begin{array}{r l r} c ^ {'} \geq \frac {h - H}{H} C \Longleftrightarrow & (c ^ {'} + C) H \geq C h \\ \Longleftrightarrow & \frac {c ^ {'} + C}{h} \geq \frac {C}{H} \\ \Longleftrightarrow & q _ {e} ^ {*} \geq Q ^ {*} \end{array}
$$

6. where ${ Q } ^ { * }$ and $q _ { \mathrm { e } } ^ { * }$ represent respectively the optimal solution of $\mathrm { T C } _ { 1 }$ and the optimal order quantity under VMI if $Q = q .$ . They can be obtained from (11) and (18). In addition, we have

$$
\begin{array}{r c l} c ^ {'} \geq \frac {h - H}{H} C \Longleftrightarrow & (c ^ {'} + C) H \geq C h \\ \Longleftrightarrow & c ^ {'} h \geq (c ^ {'} + C) h - (c ^ {'} + C) H \\ \Longleftrightarrow & \frac {c ^ {'}}{h - H} \geq \frac {c ^ {'} + C}{h} \\ \Longleftrightarrow & q ^ {*} \geq q _ {\mathrm{e}} ^ {*} \end{array}
$$

7. where $q ^ { * }$ is the optimal solution of $\mathrm { T C } _ { 2 }$ and can be obtained from (12). As a result, we have $c ^ { \prime } { \geq } \frac { h - H } { H } C { \Leftarrow } { \Rightarrow } q ^ { \ast } { \geq } q _ { \mathrm { e } } ^ { \ast } { \geq } Q ^ { \ast }$ when $h > H .$ The inequalities among $q ^ { * } , q _ { \mathrm { e } } ^ { * }$ and $Q ^ { * }$ together with the convexity of $\mathrm { T C } _ { 1 }$ and $\mathrm { T C } _ { 2 }$ imply that, for any pair of order quantities (Q,q) and $Q { \geq } q ,$ we have: If 0> a\*

$$
f Q \geq q ^ {*}
$$

$$
\begin{array}{l} T C _ {\mathrm{VMI}} (Q, q) = T C _ {1} (Q) + T C _ {2} (q) \\ \geq T C _ {1} (q ^ {*}) + T C _ {2} (q ^ {*}) \\ = T C _ {\mathrm{VMI}} (q ^ {*}, q ^ {*}) \\ \geq T C _ {\mathrm{VMI}} (q _ {e} ^ {*}, q _ {e} ^ {*}) \end{array}\tag{19}
$$

<sub>ð</sub><sup>20</sup><sub>Þ</sub>

• The inequality (19) comes from the fact that ${ \cal Q } { \geq } q ^ { * } { \geq } 0 ^ { * }$ and $\mathrm { T C _ { 1 } }$ is convex in Q. In addition, $q ^ { * }$ is the optimal solution for $\mathrm { T C } _ { 2 } .$ The inequality (20) results from the optimality of $( q _ { \mathrm { e } } ^ { * } , q _ { \mathrm { e } } ^ { * } )$ ) for $\mathrm { T C } _ { \mathrm { V M I } }$ $( Q , q )$ when $Q = q .$

• I $\scriptstyle { \dot { Q } } < q ^ { * }$

$$
\begin{array}{l} T C _ {V M I} (Q, q) = T C _ {1} (Q) + T C _ {2} (q) \\ \geq T C _ {1} (Q) + T C _ {2} (Q) \\ = T C _ {V M I} (Q, Q) \\ \geq T C _ {V M I} (q _ {e} ^ {*}, q _ {e} ^ {*}) \end{array}\tag{21}
$$

• The inequality (21) comes from the fact that $q ^ { * } { \geq } Q { \geq } q$ and $\mathrm { T C } _ { 2 }$ is convex in q.

After all, we have $\mathrm { T C } _ { \mathrm { V M I } } ( \boldsymbol { Q } , \boldsymbol { q } ) \geq \mathrm { T C } _ { \mathrm { V M I } } ( q _ { \mathrm { e } } ^ { * } , q _ { \mathrm { e } } ^ { * } )$ for any $Q \geq q .$ . Thus $( q _ { \mathrm { e } } ^ { * } , q _ { \mathrm { e } } ^ { * } )$ is the optimal solution for $\mathrm { T C } _ { \mathrm { V M I } } (  { \mathcal { Q } } , q )$ when $c ^ { \prime } { \geq } \frac { h - H } { H } C$ and $h { > } H .$

The optimal cost $\mathrm { T C } _ { \mathrm { V M I } } ^ { * }$ can be obtained by letting $Q = Q _ { \mathrm { V M I } } ^ { \ast }$ and $q = q _ { \mathrm { { v M I } } } ^ { * }$ in (10). This concludes the proof.

Proof of Proposition 3. From Proposition 1 and Proposition 2, it is easy to check that $c ^ { \prime } + c > c \geq c ^ { \prime } > \frac { \mathbf { \bar { \phi } } h - H } { h }$ c is a necessary condition for $q _ { \mathrm { V M I } } ^ { * } > q _ { \mathrm { N V } } ^ { * }$ . Now we need to prove its suf<sup>fi</sup>ciency. We can compare q<sub>NV</sub><sup>⁎</sup> and $q _ { \mathrm { V M I } } ^ { * }$ in Proposition 1 and 2. There are only two cases in which $q _ { \mathrm { V M I } } ^ { \ast } > q _ { \mathrm { N V } } ^ { \ast }$

$c ^ { \prime } { \leq } \frac { h - H } { H } C$ and $c ^ { ' } > \frac { h - H } { h } c .$ . Note that the <sup>fi</sup>rst condition implies $h > H$ (because $c ^ { \prime }$ cannot be negative) and ${ \frac { h - H } { H } } C > { \frac { h - H } { h } } C .$ . We then have $C > \frac { H } { h } C$ and

$$
c ^ {\prime} + C > \frac {h - H}{h} c + \frac {H}{h} c = c
$$

$c ^ { ' } > \frac { h - H } { H } C$ and $c ^ { \prime } + C > c .$ . In this case, we also have

$$
c ^ {\prime} > \frac {h - H}{H} (c - c ^ {\prime})
$$

$$
\Rightarrow c ^ {\prime} + \frac {h - H}{H} c ^ {\prime} > \frac {h - H}{H} c
$$

$$
\Rightarrow \frac {h}{H} c ^ {\prime} > \frac {h - H}{H} c
$$

$$
\Rightarrow c ^ {\prime} > \frac {h - H}{h} c
$$

Combining these two cases, we have the necessary and suf<sup>fi</sup>cient condition $c ^ { ' } + C > c \geq c ^ { ' } > \frac { h - H } { h } C$ for $q _ { \mathrm { V M I } } ^ { \ast } > q _ { \mathrm { N V } } ^ { \ast }$

## References

[1] W.B. Crowston, M. Wagner, J.F. Williams, Economic lot size determination in multistage assembly systems, Management Science 19 (1973) 517–527.

[2] P. van der Vlist, R. Kuik, B. Verheijen, Note on supply chain integration in vendormanaged inventory, Decision Support Systems 44 (2007) 360–365.

[3] W. Wang, H. Wee, J. Tsao, Revisiting the note on supply chain integration in vendormanaged inventory, Decision Support Systems 48 (2010) 419–420.

[4] Y. Yao, P.T. Evers, M.E. Dresner, Supply chain integration in vendor-managed inventory, Decision Support Systems 43 (2007) 663–674.

[5] Y. Yao, P.T. Evers, M.E. Dresner, Response to “Note on supply chain integration in vendor-managed inventory”, Decision Support Systems 44 (2007) 366–367.

[6] P.H. Zipkin, Foundations of Inventory Management, McGraw Hill, 2000.
