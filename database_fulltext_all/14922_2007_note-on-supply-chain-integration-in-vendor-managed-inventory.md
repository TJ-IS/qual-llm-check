---
otero_id: 14922
otero_key: "DMPX9SAY"
title: "Note on supply chain integration in vendor-managed inventory"
authors: "Piet van der Vlist; Roelof Kuik; Bas Verheijen"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.03.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Note on supply chain integration in vendor-managed inventory

Piet van der Vlist <sup>⁎</sup>, Roelof Kuik, Bas Verheijen

RSM Erasmus University, Rotterdam, The Netherlands

Received 23 October 2006; accepted 12 March 2007 Available online 21 March 2007

## Abstract

In a recent paper Yao et al. present a single-buyer-single-supplier model to explore the effects of collaborative supply-chain initiatives such as vendor managed inventory (VMI). Several conclusions drawn from their model are arguable as (i) the model ignores the costs of shipments from the supplier to the buyer and (ii) the model times the incoming and outgoing flows at the supplier in a manner that overstates the inventory needed at the supplier. © 2007 Elsevier B.V. All rights reserved.

Keywords: Vendor managed inventory; Supply chain integration; Supply chain synchronization; Information sharing

## 1. Introduction

The model developed in Yao et al. [2] explores the cost savings to be realized from collaborative initiatives such as vendor-managed inventory (VMI). The system modeled is that of a supply chain for a single item with two parties, where the downstream party (the buyer) faces demand at a constant rate r. The buyer is replenished by the upstream party (the supplier). Two situations are modeled: no-VMI and VMI. These two situations differ in the way the item flow is managed. In the no-VMI situation each of the parties optimizes his own ordering strategy ignoring costs borne by the partner. In the VMI situation the supplier, as an omnipotent manager, optimizes the ordering process at both the supplier and the buyer so as to minimize the total costs of the supply chain.

We find the outcomes of their model, which will be referred to as the Yao-model, arguable for two reasons.

(1) The model ignores costs borne by the supplier for shipping goods to the buyer.

(2) The model manages the incoming and outgoing flows at the supplier in the worst-case manner, thus overstating the inventory kept at the supplier.

Either one of these criticisms contests main conclusions in [2]. In particular, this note shows that under VMI:

(1) Shipment sizes from supplier to buyer increase.

(2) Inventory at the supplier goes down.

(3) Inventory at the buyer goes up.

This note follows [2] in notation. Uppercase characters represent variables and parameters that affect the supplier and lowercase characters are used to denote quantities that affect the buyer. Symbols are primed in the VMI situation, whenever their value differs from that in the no-VMI situation. See Fig. 1.

## 2. Extending the Yao-model with delivery cost

In the models of Yao et al. the delivery costs T and t are overlooked. Because delivery costs to the customers of the buyer cannot be impacted by the buyer's ordering pattern and therefore in the model represent sunk costs, t indeed can be ignored. The costs T of the outgoing shipments at the supplier however cannot be disregarded, as they are impacted by the buyer's ordering decisions. These costs, comprising of costs for order picking, shipping and transportation can be considerable; they can run to over 50% of the supplier's logistics costs as we found in several cases in the Dutch food retail sector. So, in the remainder of this note we extend the Yao-model with the delivery costs T. This extended model is referred to as Yao<sup>+</sup>. The Yao-model is recovered when setting T = 0.

## 3. Case descriptions

This section gives an overview of 5 possible cases; two cases in the no-VMI situation and three cases in the VMI situation. The two cases in the no-VMI situation differ in the way the buyer is charged by the supplier and the three cases for the VMI situation differ in the timing of replenishment orders at the supplier. Values pertinent to a certain case are subscripted with the case's number.

## 3.1. No-VMI

In the no-VMI situation decisions on the optimal order size are made by the two parties independently. The buyer finds the optimal order size q from an analysis using the EOQ-model. The demand at the supplier then occurs in sizes of q. Approximating this demand pattern by a constant demand rate, necessarily of intensity r, renders the analysis of the optimal order size amenable by EOQ for the supplier as well.

To recoup his cost, the supplier factors the delivery costs T into the pricing scheme. Two cases can be distinguished:

• The supplier applies unit pricing by setting an all inclusive fixed price per unit bought by the buyer. No charge is made for the delivery as such. In some way the unit price covers the delivery costs, but the unit price does not depend on the ordering strategy of the buyer.

• The supplier applies service based pricing, meaning that on top of a base price per unit the supplier charges a fee for each delivery made.

The pricing arrangement affects the values for the unit holding costs and the costs incurred per order at the buyer.

![](/api/attachments/DMPX9SAY/fulltext/images/806857654a368fe0c2a726cfef1f3655a4e4cfee43b207591ab1c6e547d9795c.jpg)  
H, h, h'= inventory carrying charge  
C, c, c' = cost of placing an order  
T. T', t = cost of delivering an order  
Q, Q', q, q' = order quantity  
Upper case and lower cases represent the supplier and buyer, respectively.

Fig. 1. Modeling framework.

## 3.1.1. Case 1 — No-VMI fixed unit price $( F u p )$

Applying nonzero delivery costs does not affect the optimal order sizes $q ^ { * }$ at the buyer and $Q ^ { * }$ at the supplier

$$
q _ {1} ^ {*} = \sqrt {\frac {2 c r}{h}} \text {   and   } Q _ {1} ^ {*} = Q ^ {*} \equiv \sqrt {\frac {2 C r}{H}}
$$

Indeed, the delivery costs, being borne by the supplier, do not affect the buyer's decision. But the delivery costs do affect the total costs per unit of time. Under optimal order quantities the total costs rate, $\mathrm { T C } _ { 1 } ^ { * }$ has the following expression.

$$
\mathrm{TC} _ {1} ^ {*} = \sqrt {2 r} (\sqrt {C H} + \sqrt {\mathrm{ch}}) + T \sqrt {\frac {h r}{2 c}}
$$

Here $T \sqrt { h r / 2 c }$ are the delivery costs per unit of time. For $T { = } 0$ these results are in Eqs. (1), (2), and (3) in [2].

## 3.1.2. Case 2 — No-VMI service based pricing (Sbp)

With service based pricing, the supplier charges the buyer, on top of a base price, the delivery costs T per order. The cost rate function then is

$$
\mathrm{TC} _ {2} = \frac {C r}{Q} + \frac {H Q}{2} + \frac {(c + T) r}{q} + \frac {h q}{2}\tag{1}
$$

Consequently optimal order sizes are determined from

$$
q _ {2} ^ {*} = \sqrt {\frac {2 (c + T) r}{h}}
$$

and $Q _ { 2 } ^ { * } { = } Q ^ { * }$ with the total costs per time unit equal to

$$
\mathrm{TC} _ {2} ^ {*} = \sqrt {2 r} \left(\sqrt {\mathrm{CH}} + \sqrt {(c + T) h}\right)
$$

## 3.2. VMI

Inventory at the supplier is managed differently under the three VMI-cases. The inventory patterns that result for the three cases have been drawn in Fig. 2 with a ratio of the supplier's order size to the buyer's order size of five. The details on how the patterns come about are given in the subsections below.

## 3.2.1. Case 3 — VMI Yao+

The VMI total cost analysis carried out by Yao et al., assumes that the buyer's order size and the supplier's order size are chosen such that $k { = } Q / q$ is a natural number in order to set up a function for the costs per unit of time. In the process of arriving at their solution Yao et al. relax the condition that k be a natural number.

As for the timing of the replenishment orders at the supplier Yao et al. assume an order is issued the instant the supplier's inventory hits zero. The expected inventory at the supplier can be computed for this replenishment policy as

$$
I _ {s, 3} = \frac {1}{k} \sum_ {i = 1} ^ {k} (Q - (i - 1) q) = Q - \frac {k - 1}{2} q = \frac {Q + q}{2}
$$

and the cost rate function becomes

$$
\mathrm{TC} _ {3} = \frac {C r}{Q} + H \left(\frac {Q + q}{2}\right) + \frac {(c ^ {\prime} + T ^ {\prime}) r}{q} + \frac {h ^ {\prime} q}{2}
$$

The optimal order sizes that result from minimization of this cost rate function are

$$
q _ {3} ^ {*} = \sqrt {\frac {2 (c ^ {\prime} + T ^ {\prime}) r}{h ^ {\prime} + H}}
$$

and $Q _ { 3 } ^ { * } { = } Q ^ { * }$

3.2.2. Case $4 \mathrm { ~  ~ { ~ \stackrel { ~ \textstyle ~ 4 ~ } { ~  ~ } } ~ } T M I$ with unlinked timing of replenishment orders (Unl)

In the case of unlinked timing of replenishment orders the supplier orders at a random moment within the time window between the buyer's order that exhausts the supplier's inventory and the next order from the buyer which happens $q / r$ time periods later. The average inventory level at the supplier in this case is in between the level for the ${ \mathrm { Y a o } } ^ { + }$ — case and the synchronized case discussed in the next subsection where replenishment is postponed until the next order of the supplier is due. The average inventory at the supplier thus is $\mathcal { Q } / 2$ with unlinked timing of replenishment orders.

The cost rate function then is a simple sum of EOQtype costs rates as

$$
\mathrm{TC} _ {4} = \frac {C r}{Q} + \frac {H Q}{2} + \frac {(c ^ {\prime} + T ^ {\prime}) r}{q} + \frac {h ^ {\prime} q}{2}\tag{2}
$$

Consequently optimal order sizes are calculated from

$$
q _ {4} ^ {*} = \sqrt {\frac {2 (c ^ {\prime} + T ^ {\prime}) r}{h ^ {\prime}}}
$$

and $Q _ { 4 } ^ { * } { = } Q ^ { * }$ with an implied total costs per time unit of

$$
\mathrm{TC} _ {4} ^ {*} = \sqrt {2 r} \left(\sqrt {C H} + \sqrt {\left(c ^ {\prime} + T ^ {\prime}\right) h ^ {\prime}}\right)
$$

![](/api/attachments/DMPX9SAY/fulltext/images/e9f95e4e0da1d748269bef9f2e2c5b1786ddffbb7468a14fc34a0568704be56c.jpg)  
Note. The supplier's stock pattern for unlinked ordering has been drawn for two realizations, $\tau _ { a }$ and $\tau _ { b } ,$ of the length of time elapsing between the time of the buyer's order that exhausts the supplier's inventory and reordering at the supplier. Under unlinked reordering this length of time is random, taking arbitrary values between 0 and $q / r$  
Fig. 2. Stock patterns.

Note that the average supplier's inventory incorporated in Eq. (2) is Q/2 and so is independent of q and k. This contrasts with Case 3, see Eq. (4) in [2]) and with Case 5 below, see Eq. (4).

## 3.2.3. Case 5 — VMI synchronized (Syn)

When the supplier's inventory hits zero, in a deterministic setting the next requirement from the buyer is not due until $q / r$ time periods later. So any replenishment order of the supplier can be delayed by that length of time, cf. [Silver and Peterson [1], Page 484 and following]. Call the new VMI strategy that delays the supplier's order the synchronized strategy. The synchronized strategy yields as the supplier's average inventory:

$$
I _ {s, 5} = \frac {1}{k} \sum_ {i = 1} ^ {k} (Q - i q) = Q - \frac {k + 1}{2} q = \frac {Q - q}{2}\tag{3}
$$

Based on this, the cost-rate function for the synchronized case becomes

$$
\mathrm{TC} _ {5} = \frac {C r}{Q} + H \left(\frac {Q - q}{2}\right) + \frac {(c ^ {\prime} + T ^ {\prime}) r}{q} + \frac {h ^ {\prime} q}{2}\tag{4}
$$

Minimization of this function while relaxing that $\varrho / q$ be a natural number gives

$$
q _ {5} ^ {*} = \sqrt {\frac {2 (c ^ {\prime} + T ^ {\prime}) r}{h ^ {\prime} - H}}
$$

and $Q _ { 5 } ^ { * } { = } Q ^ { * }$ with an implied total costs per time unit of

$$
\mathrm{TC} _ {5} ^ {*} = \sqrt {2 r} \left(\sqrt {C H} + \sqrt {\left(c ^ {\prime} + T ^ {\prime}\right) \left(h ^ {\prime} - H\right)}\right)
$$

Note that $h ^ { \prime } { - } H$ is the added (echelon) holding costs upon transferring a unit from the supplier to the buyer. If $h ^ { \prime } \leq H$ then $q = Q$

## 4. Analyses

Minimizing the total cost functions and relaxing the requirement that k be an integer, leads for the various cases, to the values as listed in Table 1.

Note that for all cases $Q ^ { * } = \sqrt { 2 C r / H }$

Table 1  
Overview of the optimal values

<table><tr><td>Case</td><td>Total cost TC per time unit</td><td>q*</td></tr><tr><td>1. No-VMI Fup</td><td> $\sqrt{2r}\left(\sqrt{CH} + \sqrt{ch}(1 + \frac{T}{2c})\right)$ </td><td> $\sqrt{\frac{2cr}{h}}$ </td></tr><tr><td>2. No-VMI Sbp</td><td> $\sqrt{2r}\left(\sqrt{CH} + \sqrt{(c + T)h}\right)$ </td><td> $\sqrt{\frac{2(c + T)r}{h}}$ </td></tr><tr><td>3. VMI Yao+</td><td> $\sqrt{2r}\left(\sqrt{CH} + \sqrt{(c' + T')(h' + H)}\right)$ </td><td> $\sqrt{\frac{2(c' + T')r}{h' + H}}$ </td></tr><tr><td>4. VMI Unl</td><td> $\sqrt{2r}\left(\sqrt{CH} + \sqrt{(c' + T')h'}\right)$ </td><td> $\sqrt{\frac{2(c' + T')r}{h'}}$ </td></tr><tr><td>5. VMI Syn</td><td> $\sqrt{2r}\left(\sqrt{CH} + \sqrt{(c' + T')(h'-H)}\right)$ </td><td> $\sqrt{\frac{2(c' + T')r}{h' - H}}$ </td></tr></table>

To juxtapose the various cases, we have to further detail the relationship between parameter values in the no-VMI situation and the VMI situation.

• Consider, as in [2],

$$
c \gg c ^ {\prime}\tag{5}
$$

The values c and $c ^ { \prime }$ represent the buyer's ordering costs in the no-VMI situation and in the VMI situation, respectively. As already remarked by [2] under VMI the buyer does not need to place orders with the supplier. Consequently $c ^ { \prime }$ will be much smaller than c.

• Consider

$$
c + T \approx c ^ {\prime} + T ^ {\prime}\tag{6}
$$

The value $c + T$ represents the total costs of placing and delivering an order between the buyer and the supplier. Under VMI the responsibility of placing the buyer's orders is assumed by the supplier. The reduction in ordering cost at the buyer results in an almost equal augmentation of the delivery cost at the supplier and the sum of the ordering and delivery costs per order/shipment remains more or less the same.

• Consider

$$
h ^ {\prime} \leq h\tag{7}
$$

The value of the unit holding cost rates h and $h ^ { \prime }$ at the buyer depend upon the valuation of the goods. In the no-VMI situation the value of the goods is determined by the commercial transaction between supplier and buyer. In the VMI situation:

· supplier and buyer either have made an arrangement with a lower transaction price in order to let the buyer benefit from the overall lower costs under VMI

· or the supplier still owns the inventory at the buyer (consignment stock) in which case he might value the goods at production costs.

## 5. Comparisons

Comparisons will be made now for the cost rate, the shipment size from supplier to buyer, the inventory at the buyer and the inventory at the supplier while considering parameter values in no-VMI and VMI situations as considered in the foregoing subsection.

## 5.1. Costs rate

The total cost, ${ \mathrm { T C } } _ { 3 } ^ { * }$ , in the Yao<sup>+</sup>-scenario (see Case 3 in Table 1) put side by side with the costs rates in the VMI Cases 4 and 5 renders:

$$
\mathrm{TC} _ {5} ^ {*} \leq \mathrm{TC} _ {4} ^ {*} \leq \mathrm{TC} _ {3} ^ {*} f o r H > 0\tag{8}
$$

## 5.2. Shipment size supplier–buyer

It is immediately clear from Table 1 that

$$
q _ {5} ^ {*} \geq q _ {4} ^ {*} \geq q _ {1} ^ {*}\tag{9}
$$

The conclusion $q _ { 5 } ^ { * } { > } q _ { 1 } ^ { * }$ continues to hold as long as $( c ^ { \prime } + T ^ { \prime } ) h { > } ( h ^ { \prime } { - } H ) c$ . Furthermore it can be concluded that

$$
q _ {5} ^ {*} \geq q _ {4} ^ {*} \geq q _ {3} ^ {*}\tag{10}
$$

Note that $h ^ { \prime } \leq H$ results in $q ^ { * } { = } Q ^ { * }$ . So unlike ${ \mathrm { Y a o } } ^ { + } { \mathrm { , } }$ 9 we find that VMI both in case of unlinked and in case of synchronized ordering will increase the shipment size from supplier to buyer.

## 5.3. Inventory at buyer

Let $I _ { b } ^ { * }$ be the average stock at the buyer under an optimal strategy. This inventory is half the shipment size $q ^ { * }$ . So, from the shipment sizes one immediately has

Table 2  
Differences between Yao and our findings

<table><tr><td rowspan="2">Compared to No-VMI (Fup)</td><td colspan="3">VMI</td></tr><tr><td>Yao $(T=0)$ </td><td>Unl</td><td>Syn</td></tr><tr><td>Shipment size supplier-buyer</td><td>Down</td><td>Up</td><td>Up</td></tr><tr><td>Inventory at supplier</td><td>Up</td><td>Unchanged</td><td>Down</td></tr><tr><td>Inventory at buyer</td><td>Down</td><td>Up</td><td>Up</td></tr></table>

$$
I _ {b, 5} ^ {*} > I _ {b, 4} ^ {*} > I _ {b, 1} ^ {*}\tag{11}
$$

Yao et al. find that inventory at the buyer decreases, whereas we find that VMI, whether synchronized or not, raises this inventory.

## 5.4. Inventory at supplier

Let $I _ { s } ^ { * }$ be the average stock at the supplier under an optimal strategy.

$$
I _ {s, 5} ^ {*} <   I _ {s, 4} ^ {*} = I _ {s, 1} ^ {*}\tag{12}
$$

Yao et al. find that inventory at the supplier increases, whereas we find that VMI, whether synchronized or not, reduces this inventory.

## 6. Conclusion

Table 2 lists the difference in conclusions in our analysis with those in [2] when comparing VMI with No-VMI (Fup).

Our conclusions challenge the conclusions made in [2].

We hasten to add that the VMI analysis presented is limited in that it only considers and models effects that are a consequence of considering total costs in the optimization or that are a consequence of the coordinated inventory management at the supplier. Effects of VMI that are produced by considering

• the redistribution of risk (such as consignment, or take back arrangements)

• coordination of replenishment for multiple buyers (consolidation and accumulation)

• information sharing of down stream demand data (when demand is subject to variation and uncertainty)

• choice in (safety) stock positioning

• latitude for the supplier to shift delivery moments

• authority to adjust delivery quantities in response to inventory developments.

• remain undiscussed.

## References

[1] Edward A. Silver, Rein Peterson, Decision Systems for Inventory Management and Production Planning, JohnWiley and Sons, 1985.

[2] Yuliang Yao, Philip T. Evers, Martin E. Dresner, Supply chain integration in vendor-managed inventory, Decision Support Systems 43 (2007) 663–674.

Piet van der Vlist is adjunct professor of Supply Chain Management at the Erasmus University's Rotterdam School of Management. He holds an MSC in Electronic engineering from Delft University of Technology and an MBA from the University of Twente.

Roelof Kuik is associate professor of Logistics and Simulation at RSM Erasmus University. He holds an Msc and a PhD in Physics from the University of Groningen.

Bas Verheijen is a PhD candidate in the department of Decision Sciences and Information Technology at RSM Erasmus University in Rotterdam. He holds an MSc in Applied Physics from Eindhoven University of Technology.
