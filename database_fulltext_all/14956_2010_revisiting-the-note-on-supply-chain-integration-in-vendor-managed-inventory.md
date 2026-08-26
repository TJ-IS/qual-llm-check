---
otero_id: 14956
otero_key: "R88ZDUNE"
title: "Revisiting the note on supply chain integration in vendor-managed inventory"
authors: "Wan-Tsu Wang; Hui-Ming Wee; H.-S. Jacob Tsao"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/i.dss.2009.08.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Revisiting the note on supply chain integration in vendor-managed inventory

Wan-Tsu Wang <sup>a</sup>, Hui-Ming Wee <sup>a,b,</sup>⁎, H.-S. Jacob Tsao b

<sup>a</sup> Department of Industrial & Systems Engineering, Chung Yuan Christian University, Chungli 32023, Taiwan, ROC

<sup>b</sup> Department of Industrial & Systems Engineering, San Jose State University, CA, USA

## a r t i c l e i n f o

Article history: Received 18 November 2008 Received in revised form 7 April 2009 Accepted 2 August 2009 Available online 12 August 2009

Keywords: Vendor-managed inventory Information sharing Supply chain integration

## a b s t r a c t

This note investigates a recent paper by Yao et al. and a critique by van der Vlist et al. Both papers presented interesting arguments to show their <sup>fi</sup>ndings and conclusions. However, their conclusions about the buyer's order sizes seem to con<sup>fl</sup>ict with each other. Revisiting both papers, we come to the conclusion that both papers are valid within the scopes and assumptions of their studies. Our paper summarizes the factors that must be stated clearly to resolve the con<sup>fl</sup>ict and to avoid the confusion.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

The concept of Vendor-Managed Inventory (VMI) has received much research attention, and its implementation has led to successful collaborative efforts in supply chain integration. However, conditions under which VMI produces bene<sup>fi</sup>ts and the distribution of bene<sup>fi</sup>ts between the supplier and the buyer have been illusive, open questions. The recent papers by van der Vlist et al. [2] and Yao et al. [3] explored some innovative ideas for answering these questions in the context of determining the economic order quantities (EOQ) of a single commodity for a single supplier and a single buyer to satisfy a known demand with constant rate and instantaneous replenishment. Yao et al. [3] investigated how the replenishment strategies in the VMI model generated bene<sup>fi</sup>ts in the forms of inventory reductions and cost savings from supply chain integration. They concluded that implementing VMI leads to smaller replenishment quantities between the supplier and the buyer (the buyer's optimal order/ shipment sizes). van der Vlist et al. [2] extended the work of Yao et al. [3] by considering the delivery cost and particularly the distribution of <sup>fi</sup>xed-cost portion of the delivery between the supplier and the buyer in non-VMI and by allowing the supplier to replenish its inventory at later times for on-time delivery to the buyer. However, they concluded that the shipment sizes from the supplier to the buyer increase after implementing VMI. The conclusion also does not agree with the result of a survey of the Taiwanese grocery industry conducted by Tyan and Wee [1], where VMI system with Just-in-Time was shown to reduce lot sizes and maximize the competitiveness of the chain. Yao et al. [4] pointed out that the conclusions of van der Vlist et al. [2] were derived from two assumptions that are not in Yao et al. [3].

We follow the notations de<sup>fi</sup>ned in van der Vlist et al. [2]. It is noted that not all costs involved in purchasing are explicitly considered in Yao et al [3], van der Vlist et al. [2] and this paper. Only the <sup>fi</sup>xed cost of replenishment or shipment is considered. The corresponding variable cost, e.g., the unit transportation charge, is ignored due to a known demand. The inventory carrying costs, however, are variable costs, and they should be considered as such. van der Vlist et al. [2] considered <sup>fi</sup>ve cases for study and comparison. Case 1 (No-VMI <sup>fi</sup>xed unit price or No-VMI Fup) is a model in which the delivery cost is borne by the supplier; this case effectively features non-VMI with free deliver for the buyer. Case 2 (No-VMI service based pricing or No-VMI Sbp) derives the buyer optimal order size with the delivery cost borne by the buyer; this is the non-VMI model of Yao et al. [3]. Case 3 (VMI extended model of Yao et al. or VMI Yao+) is actually Yao et al.'s VMI model [3] but with delivery cost separated from the rest of the ordering cost. In Case 3, the supplier places an order when the buyer's order reduces the supplier's inventory to zero. Case 4 (VMI with unlinked timing of replenishment orders or VMI Unl) and Case 5 (VMI synchronized or VMI Syn) discuss two new supplier's replenishment strategies that place an order later than Case 3. In Case 5, the later time is when the buyer places the next order, and it is the latest possible time for the supplier's instantaneous replenishment in order to satisfy the buyer's order on time; in Case 4, the later time is randomly distributed between this latest time and the earlier supplier replenishment time of Case 3.

In van der Vlist et al. [2] and Yao et al. [3], one can see that their conclusions about the buyer's optimal order/shipment sizes are in con<sup>fl</sup>ict with each other. A main difference in these two papers is that van der Vlist et al. [2] considered explicitly the delivery cost between the supplier and the buyer in their inventory modeling while Yao et al. [3] did not. The following explanations may shed light on the cause of the con<sup>fl</sup>ict.

van der Vlist et al. [2] only compared their new VMI models with delivery cost (i.e. VMI Unl and VMI Syn or their Cases 4 and 5) with the non-VMI model with free delivery for the buyer (i.e. No-VMI Fup or their Case 1). Note that all these three cases were developed by van der Vlist et al. and were not considered in Yao et al. [3]. van der Vlist et al. [2] should not have contrasted their conclusions with those of Yao et al. [3]. Because the buyer's optimal order size of the No-VMI Fup model is derived without delivery cost to the buyer, the buyer's optimal order size of No-VMI Fup looks the same as the classic economic order quantity (EOQ) derived for non-VMI by Yao et al. [3], with the delivery cost implicitly subsumed in the ordering cost. But, they only look the same in form but are actually different. It would have been more logical for van der Vlist et al. [2] to compare their VMI models with the base non-VMI case of Yao et al., i.e., their non-VMI model with delivery cost, No-VMI Sbp case, or Case 2.

## 2. Modi<sup>fi</sup>ed comparisons

From van der Vlist et al. [2], the buyer's optimal order sizes for VMI Yao +and No-VMI Sbp are $q _ { 3 } ^ { * }$ and $q _ { 2 } ^ { * }$ respectively. We use No-VMI Sbp as a base model and compare the following ratio between these two sizes:

$$
\frac {q _ {3} ^ {*}}{q _ {2} ^ {*}} = \sqrt {\frac {c ^ {'} + T ^ {'}}{\frac {c + T}{\frac {h ^ {'}}{h} + \frac {H}{h}}}}\tag{1}
$$

where T, c and h denote for the case of non-VMI, the cost of delivering an order to the buyer, the rest of the ordering cost and the buyer's inventory carrying charge respectively; $T ^ { \prime } , c ^ { \prime }$ and h′ denote their VMI counterparts; H denotes the supplier's inventory carrying charge.

$\frac { q _ { 3 } ^ { * } } { q _ { 2 } ^ { * } }$ decreases when both $\frac { h ^ { \prime } } { h }$ and $\frac { \bar { H } } { h }$ increase, and increases when $\frac { c ^ { \prime } + \stackrel {  } { T } } { c + T }$ increases. If the dichotomy of “greater and equal than $\mathrm { o n e " }$ or “less than $\mathrm { o n e " }$ is used for sorting h<sup>′</sup> H $\overline { { h } } ^ { \prime } \overline { { h } }$ and $\frac { c ^ { \prime } + T } { c + T }$ and for studying their impact on the value of $\frac { q _ { 3 } ^ { * } } { q _ { 2 } ^ { * } } ,$ there are eight combinations. To simplify the analysis, we also assume that $c + T { \approx } c ^ { \prime } + T ^ { \prime }$ and $h ^ { \prime } \leq h$ as in van der Vlist et al. [2] but not in Yao et al. [3]. We make two observations.

1. When $\frac { c ^ { ' } + T ^ { ' } } { c + T } { \approx } 1$ and $\begin{array} { l } { \displaystyle { \frac { h ^ { \prime } } { h } \approx 1 , \frac { q _ { 3 } ^ { * } } { { q } _ { 2 } ^ { * } } } } \end{array}$ would be less than or equal to one, with its exact value depending on the value of ${ \frac { H } { h } } .$ . That is, the order <sup>h</sup>size with VMI would be less than or equal to that without VMI. We note that h≫H would result in $q _ { 3 } ^ { * } \approx \bar { q } _ { 2 } ^ { * }$

2. When $\frac { c ^ { ' } + T ^ { ' } } { c + T } { \approx } 1$ and $\begin{array} { r } { \frac { h ^ { \prime } } { h } { < } 1 , \frac { q _ { 3 } ^ { * } } { q _ { 2 } ^ { * } } } \end{array}$ would be less than, equal to or greater <sup>2</sup>than one depending on the values $\operatorname { o f } { \frac { h ^ { \prime } } { h } } \mathrm { a n d } { \frac { H } { h } } .$ That is, the order size with VMI would be more uncertain than that of non-VMI.

From the above, under the assumptions o $\frac { \ d { } \cdot \ b { c } ^ { \prime } + \ b { T } ^ { \prime } } { \ d { c } + \ b { T } } \approx 1$ and $\scriptstyle { \frac { h ^ { \prime } } { h } } \approx 1$ , the buyer can certainly bene<sup>fi</sup>t from VMI through reduced order sizes. The buyer's optimal order sizes of the other two VMI cases, namely VMI Unl and VMI Syn of van der Vlist et al. [2], can be analyzed similarly (with No-VMI Sbp used as a base model). We can also see that the buyer's order sizes of VMI Unl and VMI Syn would be equal to or greater than that of No-VMI Sbp depending on the values of $\frac { \mathit { h } ^ { \prime } } { \mathit { h } }$ and $H$ $\overline { { h } } ^ { . }$

We summarize the comparisons between VMI and non-VMI in Table 1. Since Yao et al. [3] did not separate the delivery cost from the rest of the ordering cost, and did not use the assumptions of $c + T { \approx } c ^ { \prime } + T ^ { \prime }$ and $h ^ { \prime } { \leq } h ,$ their conclusions would differ from those shown in Table 1. Moreover, relaxing $c + T { \approx } c ^ { \prime } + T ^ { \prime }$ and $h ^ { \prime } \leq h$ may result in more complicated conclusions about the impact of VMI on the buyer's order.

Buyer's order sizes of VMI cases compared to the base case of No-VMI Sbp (case 2) non-VMI under $c + T { \approx } c ^ { \prime } + T ^ { \prime }$ and h′ h.

<table><tr><td>VMI cases</td><td>VMI Yao+</td><td>VMI Unl</td><td>VMI Syn</td></tr><tr><td>Buyer&#x27;s order quantity (with respect to non-VMI)</td><td>Uncertain</td><td>Up</td><td>Up</td></tr></table>

## 3. Conclusion

This note revisits the paper by Yao et al. [3] and the note by van der Vlist et al. [2]. The conclusion about the impact of VMI on the buyer's optimal order size reached in van der Vlist et al. [2] seems to con<sup>fl</sup>ict with its counterpart in Yao et al. [3]. The comparisons in van der Vlist et al. [2] should not be interpreted as invalidating the conclusions reached by Yao et al. [3]. This is because van der Vlist et al. [2] mainly compared the new cases they created, and used two assumptions that are not in Yao et al. [3]. In their base case, i.e., Case 1 (No VMI Fup), the delivery cost associated with an order is assumed to be borne by the supplier; in Yao et al.'s base case of non-VMI, the delivery cost is borne by the buyer instead. Under the assumptions of $c + T { \approx } c ^ { \prime } + T ^ { \prime }$ and $h ^ { \prime } \leq h$ , we presented modi<sup>fi</sup>ed comparisons about the impact of VMI on the buyer's optimal order size.

## References

[1] Jonah Tyan, Hui-Ming Wee, Vendor Managed Inventory (VMI): a survey of the Taiwanese grocery industry, Journal of Purchasing and Supply Management 9 (2003) 11–18.

[2] Piet van der Vlist, Roelof Kuik, Bas Verheijen, Note on supply chain integration in vendor-managed inventory, Decision Support Systems 44 (2007) 360–365

[3] Yuliang Yao, Philip T. Evers, MartinE. Dresner, Supply chain integration in vendor managed inventory, Decision Support Systems 43 (2007) 663–674.

[4] Yuliang Yao, Philip T. Evers, MartinE. Dresner, Response to “Note on supply chain integration in vendor managed inventory”, Decision Support Systems 44 (2007) 366–367.

![](/api/attachments/R88ZDUNE/fulltext/images/931625b2ff5f01564d0d5541cba9382d309de062078f31f918d0adbecba00af2.jpg)  
Wan-Tsu Wang is a PhD candidate in The Department of Industrial and Systems Engineering at Chung Yuan Christian University in Taiwan. His research interests include production/inventory control and supply chain management. He has published in Computers & Operations Research, Journal of the Chinese Institute of Industrial Engineering and European Journal of Operational Research.

![](/api/attachments/R88ZDUNE/fulltext/images/a16a27a5220e6deab30f0bf8a9fb5ee9a82543fa7e6394ed99abc20d21882fe9.jpg)

Hui -Ming Wee is a Professor in The Department of Industrial and Systems Engineering at Chung Yuan Christian University in Taiwan. He received his BSc (Hons) in Electrical and Electronic Engineering from Strathclyde University (UK), MEng in Industrial Engineering and Management from Asian Institute of Technology (AIT) and PhD in Industrial Engineering from Cleveland State University, Ohio (USA). His research interests are in the <sup>fi</sup>eld of production/inventory control, optimization and supply chain management. His publications include three books and 170 refereed journal papers.

![](/api/attachments/R88ZDUNE/fulltext/images/e9a438351c92861a15ad0eaa4a6399ab9e4b81e3d4b38e49b91797de4f51765c.jpg)

Dr. H.-S. Jacob Tsao is a Professor of Industrial and Systems Engineering at San Jose State University (SJSU). He received his B.S. in Applied Mathematics from National Chiao-Tung University in Taiwan in 1976, M.S. in Mathematical Statistics from The University of Texas at Dallas in 1980 and Ph.D. in Operations Research from The University of California at Berkeley in 1984. He worked for AT&T Bell Laboratories, Bell Communication Research and University of California at Berkeley before joining SJSU in 1999. His publications include two books entitled “Entropy Optimization and Mathematical Programming” (1997) and “Testing and Quality Assurance for Component-based Software” (2003) and 40 refereed journal papers. Further details can be found at http://www.engr.sjsu.edu/jtsao.
