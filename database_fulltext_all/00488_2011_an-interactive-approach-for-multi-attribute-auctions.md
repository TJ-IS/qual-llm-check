---
otero_id: 488
otero_key: "RCHDFAAB"
title: "An interactive approach for multi-attribute auctions"
authors: "Gülşah Karakaya; Murat Köksalan"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.11.023"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An interactive approach for multi-attribute auctions

Gülşah Karakaya, Murat Köksalan ⁎

Department of Industrial Engineering, Middle East Technical University, 06531 Ankara, Turkey

a r t i c l e i n f o

Available online 25 November 2010

Keywords: Online auctions Multi-attribute auctions Interactive approach

## a b s t r a c t

Auction processes are commonly employed in many environments. With rapid advances in Internet and computing technologies, electronic auctions have become very popular. People sell and buy a wide range of goods and services online. There is a growing need for the proper management of online auctions and for providing support to parties involved. In this paper, we develop an interactive approach supporting both the buyer and the bidders in a multi-attribute, single-item, multi-round, reverse auction environment. We demonstrate the algorithm on a number of problems.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

Information and communication technologies (ICT) make life easier in terms of reaching and sharing information. As Koppius et al. [10] state, these new technologies led to some changes in business and made electronic markets commonly used platforms. The developments in ICTs have affected traditional auction processes drastically. With the rapid development of technological infrastructure and invent of the internet, online auctions have become very popular. There is a growing amount of literature about online auctions [1,6,14].

With the help of the ICT applications, online auctions have broadened enabling people to sell and buy a wide range of goods and services on the internet. Auctions are commonly used by companies and governments. Some large scale applications are reported in [5,7,13,15].

Fig. 1 provides a classi<sup>fi</sup>cation of auctions based on the number of sellers and buyers.

If there is one buyer and one seller, the process is called negotiation, whereas if there are many buyers and many sellers it is called a double auction. A good example for the double auction process is a stock market. The reverse auction where the buyer is the auctioneer and the sellers are the bidders is the most common auction type in the literature. The last type is the forward auction where the seller is the auctioneer and the buyers are the bidders. A typical example of a forward auction is the auction for antiques or art objects. The number of different items and the number of units for each item auctioned are also main identi<sup>fi</sup>ers of the auction types. There may be single or multiple items auctioned, and each item may be bought or sold in single or multiple units.

The number of attributes in the auction process is another dimension. If there is only one attribute, typically the price, taken into consideration, then we have a single-attribute auction. Multiattribute auction processes, on the other hand, consider attributes such as quality, lead time, etc., in addition to the price. For these auctions, typically a value or a scoring function is used to evaluate bids. Commonly, weighted linear functions are used as value functions for multi-attribute auctions. To determine the winner of the auction, the Winner Determination Problem (WDP) that maximizes the value/ scoring function is solved.

In the literature, most of the studies on multi-attribute auctions are on reverse auctions. Bichler and Kalagnanam [4] suggest a weighted sum scoring function to evaluate bids. However, as Bellosta et al. [3] state, although using such functions is very common, it has some drawbacks such as the dif<sup>fi</sup>culty of determining weights. Also the solutions that can be found are limited with a weighted-sum scoring function. Another approach to multi-attribute auctions is using the ‘pricing out’ technique as in [17]. This case is similar to the value function case. All attributes are converted into monetary values [8] and the resulting single-attribute problem is solved. Leskelä et al. [12] formulate a single attribute auction problem and they argue that the formulation can be extended to the multi-attribute case by the pricing out approach. They develop a Quantity Support Mechanism (QSM) that provides bidders not only the ‘suggested price’ for a new bid, but also ‘quantity decision support.’ Köksalan et al. [9] improve the QSM and develop a Group Support Mechanism (GSM) where they provide support to all bidders simultaneously. Talluri et al. [16] use data envelopment analysis (DEA) to propose a decision support system tool for a multi-item, singleround auction. All the above approaches that try to estimate value functions have the drawback of combining multiple criteria with rather simplistic functions. Determining the weights and converting all attributes into a composite value are not easy. Furthermore, the capability of such functions to represent the decision maker's (DM's) preferences is highly questionable as have been discussed in the multicriteria literature extensively.

Bellosta et al. [3] suggest a multi-criteria model based on reference points for a single item auction. Baykal [2] studies combinatorial auctions and applies a variation of Korhonen and Laakso's [11] approach to the multi-attribute, multi-item combinatorial auctions. By using this method, she tries to <sup>fi</sup>nd the best combination of bids for a single round. These approaches require the DM to specify aspiration and/or reference points. Determination of such points is not an easy task for the DM. Consequently, the resulting functions of aspiration and/or reference points that are used by these methods may not represent the preferences of the DM well.

In this paper we introduce an interactive approach to provide aid both to the buyer and the sellers for a multi-attribute, single-item, multi-round, reverse auction. In our approach, we estimate the preference function of the buyer using his/her past preferences and inform the sellers about our estimations at each round to facilitate them to update their bids to be competitive in the next round. The preference information the DM provides is simply selecting the best of several bids, which is a relevant task for the DM.

We organize the paper as follows: in Section 2 we give some de<sup>fi</sup>nitions and develop the approach. We provide the problem structures we solve in Section 3 and demonstrate the performance of the approach on these problems in Section 4. We present our concluding remarks in Section 5.

## 2. The approach

In our approach, we aim to aid both the buyer and the sellers (bidders). We try to provide information to the sellers regarding the preferences of the buyer so that they can place more informed bids. Speci<sup>fi</sup>cally, we estimate the preference function of the buyer (DM) using his/her past preferences in a multi-attribute, single-item, multiround, reverse auction environment. Then, we inform the sellers about our estimations at each round to update their bids to be competitive in the next round. This process help improve the bids in line with the preferences of the buyer.

In the following we provide some de<sup>fi</sup>nitions for multi-objective problems.

![](/api/attachments/RCHDFAAB/fulltext/images/13bee95caab3b6a9e3a5141f1cad21cd1f82d49dcd1bd59d0c22e0a2d6941104.jpg)  
Fig. 1. Auction types with respect to the number of sellers and buyers.

## 2.1. Definitions

The general multi-objective problem can be de<sup>fi</sup>ned as

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
“Maximize” $\left\{z_{1}(\mathbf{x}), z_{2}(\mathbf{x}), \ldots, z_{p}(\mathbf{x})\right\}$ 
subject to
 $x \in X$ 
where,
x decision variable vector
X feasible decision space
 $z_{j}$  jth objective function
</div>

and the quotation marks are used to emphasize that the maximization of a vector is not a well-de<sup>fi</sup>ned mathematical operation.

$\mathbf { x } \in \mathbf { X }$ is said to be efficient, if and only if there does not exist $\mathbf { x } ^ { \prime } \in \mathbf { X }$ such that ${ \bf { z } } _ { \mathrm { { j } } } ( { \bf { x } } ^ { \prime } ) { \geq } { \bf { } } { \bf { } } \mathrm { { j } } ( { \bf { x } } )$ for all j and ${ \bf { \Theta } } _ { \mathrm { { J } } } ( { \bf { x } } ^ { \prime } ) { \bf { \Theta } } > { \bf { \Theta } } _ { \mathrm { { J } } } ( { \bf { x } } )$ for at least one j. Otherwise, x is said to be inefficient. If x is ef<sup>fi</sup>cient, then ${ \pmb z } ( { \bf x } ) = ( { \bf z } _ { 1 } ( { \bf x } )$ ${ \sf z } _ { 2 } ( { \bf x } ) , . . . , { \sf z } _ { \mathrm { p } } ( { \bf x } ) )$ is said to be nondominated, whereas if x is inef<sup>fi</sup>cient, then ${ \pmb z } ( { \bf x } )$ is said to be dominated.

Within the context of an auction, from a buyer's perspective, ${ \bf \delta } _ { \bf { \vec { J } } _ { j } } ( { \bf \vec { x } } )$ refers to the value of attribute j of bid x. The buyer's problem, then, is to choose the bid that maximizes his/her underlying utility among the ef<sup>fi</sup>cient bids.

## 2.2. The algorithm

We consider a problem where there are I sellers, J attributes, and a single buyer. Each seller places one bid at each round. We represent seller i's bid in the current round as $s _ { i } { = } ( a _ { i 1 } , a _ { i 2 } { , } { \ldots } , a _ { i j } { , } { \ldots } , a _ { i J } )$ where $a _ { i j }$ stands for the level of attribute j offered by seller i. Once the sellers place their bids for the current round, the buyer chooses the most preferred bid. Based on the buyer's all past preferences, we estimate a preference function, u, for the buyer as we do not know the underlying preference function of the buyer. We approximate this function with a weighted $\mathrm { L } _ { \alpha }$ metric. At each round, we update the estimates of the parameters α and $\mathrm { w _ { j } j } = 1 , . . . , \mathrm { ] }$ J of the $\mathrm { L } _ { \alpha }$ metric in order to provide more accurate information to the bidders. We represent the preference value of the bid of seller i with $\mathsf { u } ( s _ { \mathrm { i } } )$

$$
u (s _ {i}) = \left[ \sum_ {j = 1} ^ {J} \left(w _ {j} \left(a _ {i j} - z _ {j} ^ {*}\right)\right) ^ {\alpha} \right] ^ {1 / \alpha}
$$

where

$$
\begin{array}{l l} \mathrm {w_ {j}} & \text {weight of attribute j} \\ z _ {j} ^ {*} & \text {ideal level of attribute j} \\ \alpha & \text {parameter of the L_{\alpha} metric} \end{array}
$$

Note that smaller values of this function are preferred since it measures a weighted distance from the ideal point. $\mathrm { L } _ { \alpha }$ metric is quite <sup>fl</sup>exible in the sense that it can represent a variety of preference structures with different values of α and $\mathsf { W } _ { \mathrm { j } } .$ If an attribute is of maximization type, we simply replace $a _ { i j } - z _ { j } ^ { * }$ with $z _ { j } ^ { * } - a _ { i j }$ in the distance function. Without loss of generality, we assume here that all attributes are of minimization type.

We use a small positive constant threshold, $" \Delta "$ , to represent a minimum preference percentage difference by which the buyer can distinguish between bids. For instance if the buyer prefers A to B, then we require $\mathsf { u } ( \mathsf { B } ) { \geq } \mathsf { u } ( \mathsf { A } ) ( 1 + \Delta )$ . Alternatively, we may choose an additive threshold, $\Delta ^ { \prime } .$ , and require $\mathsf { u } ( \mathsf { B } ) \geq \mathsf { u } ( \mathsf { A } ) + \Delta ^ { \prime }$

At each round, we expect the sellers to improve their bids by a predetermined “100γ” percent of the estimated value of the best bid of the current round. Therefore, after estimating a preference function based on the past preferences of the buyer, we improve the estimated preference function and inform the sellers about our estimations. According to these estimations and their cost functions, sellers update their bids for the next round. The estimation of the preference function and improvement procedures will be explained in detail later.

Let P and NP denote the sets of preferred and not preferred bids of the current round, respectively. Let $\mathrm { X _ { h } }$ denote the set of constraints derived from the preferences of the buyer in round h where $\mathrm { X } _ { 0 } = \phi .$

The algorithm can be summarized as follows:

Step 1. Sellers place initial bids. Set the round counter $\mathrm { h } = 0$

Step 2. Let $\displaystyle \mathrm { P } = \mathrm { N P } = \phi .$ Present the buyer all bids and ask him/her to choose the most preferred bid(s). Place the preferred bid(s) in set P and the remaining bids in set NP.

If at least one seller has bid pro<sup>fi</sup>tably (i.e. improved the buyer's estimated value by 100γ%), go to Step 3. Otherwise go to Step 5.

Step 3. Update the preference constraint set;

$$
X _ {h} = X _ {h - 1} \cup \{u (s _ {m}) \geq u (s _ {p}) (1 + \Delta) \forall m \in N P \text {   and   } p \in P \}.
$$

Fit a preference function that satis<sup>fi</sup>es the constraint set $\mathrm { X _ { h } }$ for the smallest positive integer α value. Let the estimated preference function value of the best bid of the current round be $\mathrm { u } ^ { \ast }$

Step 4. Move to a 100γ% improved contour with a preference function value of $\mathtt { u } ^ { \mathrm { ( h ) } }$ <sup>)</sup>, i.e.,

$$
u ^ {(h)} = u ^ {*} (1 - \gamma).
$$

Recommend all sellers to move onto this contour by providing them with the current α, w and u<sup>(h)</sup> values together with the form of the preference function. Let sellers update their bids and set h=h+1. Go to Step 2.

Step 5. Stop. $s _ { \mathrm { p } }$ is (are) the winning seller(s) for p ∈ P. If there are more than one winning sellers, the buyer selects one of them, possibly using additional information about these sellers or their bids.

In Step 2, we ask the buyer the bid he/she likes most. Alternatively, we could ask the buyer the bid he/she likes the least. Technically, we could still use the resulting preference information to estimate the preference function of the buyer. However, we believe that this information would be less powerful in estimating the function and this could lead to an extended number of rounds.

In Step 4, the preference function value of the 100γ% improved contour at iteration $\boldsymbol { \mathrm { h } } , \boldsymbol { \mathrm { u } } ^ { ( \mathrm { h } ) }$ , is found as $\boldsymbol { \mathbf { u } } ^ { ( \mathrm { h } ) } { = } \boldsymbol { \mathbf { u } } ^ { * } ( 1 { - } \gamma )$ where $\mathbf { u } ^ { * }$ is the estimated preference function value of the best bid of the current round. As smaller values of u are preferred, we multiply $\mathrm { u } ^ { \ast }$ with (1−γ) to obtain improved bids for the buyer. In this step, sellers <sup>fi</sup>rst try to compose bids on the estimated contour. Those who cannot achieve this pro<sup>fi</sup>tably, compose bids that are as close to the estimated contour as possible with zero pro<sup>fi</sup>t. In our study, we assume that sellers <sup>fi</sup>nd it bene<sup>fi</sup>cial even if they bid with zero pro<sup>fi</sup>ts. We also assume that sellers do not place bids leading to losses. The algorithm continues even when some sellers place bids with zero pro<sup>fi</sup>t.

In our experiments, we consider sellers whose cost functions are rather different, making them competitive at different ranges of attribute values. In case some sellers have very similar or even identical cost functions, these sellers would behave very similar to each other. If at the end of the auction, some of these sellers simultaneously give similar “best” bids, then the buyer has to make a decision between them using some additional information about these sellers or their bids, as it would be the case in real life auctions.

## 2.3. The parameter estimation model

After obtaining the preferences of the buyer, we solve the following nonlinear (WALFA) problem to estimate the buyer's preference function.

## Parameters

α estimated parameter of the $\mathrm { L } _ { \alpha }$ metric

$\Delta$ predetermined threshold level by which the buyer can distinguish between bids

$\mathsf { W } _ { \mathrm { l } }$ lower bound for estimated weights of attributes

$\mathrm { w _ { u } }$ upper bound for estimated weights of attributes

$a _ { i j }$ level of attribute j given by seller i

$z _ { j } ^ { * }$ ideal level of attribute j

We use $\mathsf { W } _ { 1 }$ and ${ \sf W } _ { \mathrm { u } }$ restrictions in order to prevent using extreme weights. If one wishes to allow extreme weights, these restrictions can be relaxed.

## Decision variables

ε minimum difference between the preference function values of the preferred bid and the other bids

$\mathsf { W } _ { \mathrm { j } }$ estimated weight of attribute j

Problem (WALFA)

Max ε

1

s.to

$$
\sum_ {j = 1} ^ {J} w _ {j} = 1\tag{2}
$$

$$
w _ {l} \leq w _ {j} \leq w _ {u}
$$

$$
\forall j\tag{3}
$$

$$
u (s _ {i}) = \left[ \sum_ {j = 1} ^ {J} \left(w _ {j} \left(a _ {i j} - z _ {j} ^ {*}\right)\right) ^ {\alpha} \right] ^ {1 / \alpha} \quad \forall i\tag{4}
$$

$$
u (s _ {m}) \geq u \Big (s _ {p} \Big) (1 + \varepsilon) \forall s _ {p} \text {   preferred   to   } s _ {m} \text {   in   all   rounds   so   far }\tag{5}
$$

ε≥Δ

6

For simpli<sup>fi</sup>cation we do not use any subscripts to indicate rounds. The objective (1) is to <sup>fi</sup>nd the maximum ε value satisfying the constraints. We use normalized weights (2) and to avoid extreme values of weights, we set upper and lower bounds (3). Bids are evaluated in terms of a weighted $\mathrm { L } _ { \alpha }$ preference function (4). All past preferences of the buyer are re<sup>fl</sup>ected by (5). We enforce a threshold preference level, Δ, by constraint (6). This indicates that the minimum difference between the preference function values of the preferred bid and the other bids (ε) should be at least Δ, since the buyer has distinguished between these bids.

In (WALFA), we maximize the minimum difference between the preference function values of the preferred bid and the other bids while estimating the parameter values of the preference function of the buyer. Our aim here is to obtain a big separation between the estimated preference function values of the preferred bid and the other bids.

At each round, for given α values we solve (WALFA) using GAMS 22.5 and the global optimization solver, BARON. We take the smallest positive integer α value that yields a feasible solution for the weight values satisfying the constraints. The reason for taking the smallest α value is that we want to <sup>fi</sup>t a function that satis<sup>fi</sup>es all constraints but has the least curvature. Therefore we start with a linear preference function case (α = 1) and increase α by 1 if necessary.

We use α and the corresponding weight values found by (WALFA) to <sup>fi</sup>t the preference function. Let the estimated preference function value of the best bid (preferred by the buyer) in the current round be $\mathfrak { u } ^ { * }$ . We de<sup>fi</sup>ne the estimated desirable value (contour) of the buyer for the current round as $\boldsymbol { \mathbf { u } } ^ { ( \mathrm { h } ) } { = } \boldsymbol { \mathbf { u } } ^ { * } ( 1 { - } \gamma )$ which provides an estimated improvement of $100 \%$ over the previous round. We provide this information to the sellers and expect them to move onto or as close as possible to this contour. We assume that at each round, sellers give their most pro<sup>fi</sup>table bids using the available information and their individual cost functions. Each seller <sup>fi</sup>rst tries to <sup>fi</sup>nd pro<sup>fi</sup>table bids on the estimated contour. If he/she cannot compose a pro<sup>fi</sup>table bid on the estimated contour, he/she moves to a point on his/her cost curve that is closest to the estimated contour.

## 2.4. Sellers' models

The cost of a bid to seller i is a function, f (s ), of the attributes in the bid. We assume that sellers have different cost functions and at each round they update their bids according to their cost functions. Seller i <sup>fi</sup>rst solves Problem (P\_SEL ) to update his/her bid. By solving this, he/ she tries to compose a bid on the estimated contour with maximum pro<sup>fi</sup>t. If the objective function value of (P\_SEL ) is negative, indicating a loss, then he/she solves $( \mathsf { Z } _ { - } \mathsf { S E L } _ { \mathrm { i } } )$ and updates his/her bid.

## Parameters

$\mathsf { W } _ { \mathrm { j } }$ the weight of attribute j found from (WALFA)

α the parameter of the $\mathrm { L } _ { \alpha }$ metric used in (WALFA)

$z _ { j } ^ { * }$ ideal level of attribute j

$\mathbf { \chi } _ { \mathrm { u } } ^ { \mathrm { ( h ) } }$ preference function value of the estimated contour in round h $\mathrm { f _ { i } }$ the cost function of seller i

${ z _ { j } } ^ { * }$ values are typically the best attainable values for each objective and can usually be extracted from the problem context.

Decision variables

$a _ { i 1 }$ price seller i offers

$a _ { i j }$ level of attribute j to be offered by seller $\mathrm { i } , \mathrm { j } \geq 2$ ${ \mathrm { d } } _ { \mathrm { i } }$ the difference corresponding to the preference function value of the bid of seller i, u(s ), and the contour, $\mathtt { u } ^ { \mathrm { ( h ) } }$ suggested to all sellers in round h

Price is a typical attribute in auctions and we de<sup>fi</sup>ne it as attribute 1 for convenience of notation.

Problem (P\_SEL )

$$
\operatorname{Max} z _ {i} = a _ {i 1} - f _ {i} (s _ {i})\tag{7}
$$

s.to

$$
\left[ \sum_ {j = 1} ^ {J} \left(w _ {j} \left(a _ {i j} - z _ {j} ^ {*}\right)\right) ^ {\alpha} \right] ^ {1 / \alpha} \leq u ^ {(h)}\tag{8}
$$

Problem (Z\_SEL )

Min d<sub>i</sub>

9

s.to

$$
\left[ \sum_ {j = 1} ^ {J} \left(w _ {j} \left(a _ {i j} - z _ {j} ^ {*}\right)\right) ^ {\alpha} \right] ^ {1 / \alpha} - d _ {i} \leq u ^ {(h)}\tag{10}
$$

$$
a _ {\mathrm{i} 1} - \mathrm{f} _ {\mathrm{i}} (s _ {\mathrm{i}}) \geq 0\tag{11}
$$

In (P\_SEL<sub>i</sub>), the objective is to maximize the pro<sup>fi</sup>t by composing a bid on the estimated contour while satisfying the constraints according to seller i's cost function. If all sellers can compose their bids on the estimated contour, then all bids will be ef<sup>fi</sup>cient bids since this contour minimizes a weighted $\mathrm { L } _ { \alpha }$ distance from the ideal point. On the other hand, (Z\_SEL ) is solved for the sellers who cannot bid with at least zero pro<sup>fi</sup>t on the estimated contour, and the objective is to move to a point that minimizes the difference between the estimated contour and the seller's cost function. There is no guarantee that these bids will be ef<sup>fi</sup>cient as they could be dominated by some bids that are on the estimated contour.

In implementing this phase of the algorithm, the sellers may be directly provided with the parameters of the estimated function as well as the value of the contour they are recommended to reach with their bids. Then each seller may solve the resulting optimization model(s). In addition to providing the above information to sellers, a web based optimization capability can also be provided. A seller who chooses to utilize this capability may enter his/her cost function into the optimization model(s) and <sup>fi</sup>nd his/her bid solving the model(s).

## 2.5. Discussion

Our algorithm can be employed within the auction processes of single-item, multi-unit or single-unit auctions. It can be implemented for the procurement of goods such as computers or a <sup>fl</sup>eet of vehicles for an organization. It can also be implemented for purchasing a service such as transportation, construction, or catering for an organization. A natural way would be to implement the auction process electronically, where the sellers would be invited to place their bids for each round by a certain deadline. The buyer would select the provisional winner of that round and our algorithm would then update the estimated preference function, provide the information and invite the sellers to update their bids for the next round.

## 2.6. A numerical example

In this example, we consider two attributes, price and defect rate, where both are to be minimized. We assume that the buyer's underlying preference function is as follows:

$$
u = \left(\left(0. 6 \left(a _ {p} - z _ {p} ^ {*}\right)\right) ^ {4} + \left(0. 4 (a _ {d} - z _ {d} ^ {*})\right) ^ {4}\right) ^ {1 / 4}
$$

where,

$a _ { p }$ is the price value and $a _ { d }$ is defect rate value.

Consider seven sellers and their initial bids given in Table 1. We round the values to four signi<sup>fi</sup>cant digits. We use the buyer's true preference function to report the true preferences and an equal weighted $\mathrm { L } _ { \alpha }$ function with α=1 to report the estimated preferences in Table 1.

<table><tr><td colspan="6">Round 0</td></tr><tr><td>Seller</td><td>Price</td><td>Defect Rate</td><td>Pref. Fn_Buyer</td><td>Pref. Fn_Estimated</td><td>Zero profit frequency</td></tr><tr><td>S1</td><td>12.5431</td><td>1.2</td><td>5.0173</td><td>8.0040</td><td>0</td></tr><tr><td>S2</td><td>10.2344</td><td>1.7</td><td>4.0946</td><td>6.5668</td><td>0</td></tr><tr><td>S3</td><td>10.0751</td><td>2.2</td><td>4.0323</td><td>6.4909</td><td>0</td></tr><tr><td>S4</td><td>8.6518</td><td>2.7</td><td>3.4689</td><td>5.6145</td><td>0</td></tr><tr><td>S5</td><td>7.7999</td><td>3.2</td><td>3.1418</td><td>5.0999</td><td>0</td></tr><tr><td>S6</td><td>8.1535</td><td>3.7</td><td>3.2955</td><td>5.3489</td><td>0</td></tr><tr><td>S7</td><td>7.2629</td><td>4.2</td><td>2.9832</td><td>4.8099</td><td>0</td></tr></table>

The provisional winner and the corresponding bid is highlighted in bold.

Table 5  
Table 2 Bids for round 1.

<table><tr><td colspan="6">Round 1</td></tr><tr><td>Seller</td><td>Price</td><td>Defect rate</td><td>Pref. Fn_Buyer</td><td>Pref. Fn_Estimated</td><td>Zero profit frequency</td></tr><tr><td>S1</td><td>7.9232</td><td>3.1208</td><td>3.1882</td><td>4.8479</td><td>1</td></tr><tr><td>S2</td><td>7.3235</td><td>3.6174</td><td>2.9720</td><td>4.6282</td><td>1</td></tr><tr><td>S3</td><td>6.8897</td><td>4.1182</td><td>2.8399</td><td>4.4977</td><td>0</td></tr><tr><td>S4</td><td>6.8493</td><td>4.6297</td><td>2.8727</td><td>4.5790</td><td>0</td></tr><tr><td>S5</td><td>6.8099</td><td>5.1285</td><td>2.9207</td><td>4.6582</td><td>0</td></tr><tr><td>S6</td><td>6.7711</td><td>5.6202</td><td>2.9846</td><td>4.7363</td><td>0</td></tr><tr><td>S7</td><td>6.7311</td><td>6.1266</td><td>3.0682</td><td>4.8167</td><td>0</td></tr></table>

The provisional winner and the corresponding bid is highlighted in bold.

We highlight the provisional winner and the corresponding bid in bold. In Round 0, the buyer selects seller 7 (S7). Based on this information we estimate the parameters of the buyer's preference function. Let $\mathsf { W } _ { \mathrm { p } }$ and $\mathsf { W } _ { \mathrm { d } }$ denote the estimated weights for the price and defect rate attributes, respectively.

We start with α=1 and <sup>fi</sup>nd the following values by solving the (WALFA) problem.

$$
w _ {p} = 0. 9 5 \mathrm{and} w _ {d} = 0. 0 5
$$

$$
u ^ {*} = 4. 8 0 9 9
$$

$$
u ^ {(0)} = 4. 8 0 9 9 (1 - 0. 0 5) = 4. 5 6 9 4.
$$

In the tables, the estimated preference function values are given under “Pref. Fn\_Estimated” column, and the “Zero Pro<sup>fi</sup>t Frequency” column represents how many times each seller has bid unpro<sup>fi</sup>tably up to that round. If all sellers have positive values in this column at any round, indicating all sellers bid unpro<sup>fi</sup>tably, the algorithm stops.

We inform sellers about the estimated preference curve by providing its form and parameters α, $\mathsf { W } _ { \mathrm { p } } , \mathsf { W } _ { \mathrm { d } } .$ Also, we recommend each seller to try to move onto the contour having value 4.5694 with his/her updated bid in order to be competitive based on the estimated preference function.

At this point, each seller solves his/her own (P\_SEL ) problem and it turns out that all sellers except S1 and S2, can bid pro<sup>fi</sup>tably. S1 and S2 solve $\mathrm { ( Z _ { - } S E L _ { i } ) }$ and the resulting bids are provided in Table 2.

In Round 1, the buyer selects S3 and for α=1 we <sup>fi</sup>nd $\mathrm { w _ { p } } = 0 . 7 9 9 1$ and $\mathrm { w _ { d } } = 0 . 2 0 0 9$ by solving (WALFA). The estimated preference values of the bids using the new weights in Round 1 are also given in Table 2.

For the next round, the sellers are again provided with the information of the estimated α and weight values. They are also given the preference function value of the estimated contour after improvement. The updated bids can be seen in Table 3.

Bids for round 2.

<table><tr><td colspan="6">Round 2</td></tr><tr><td>Seller</td><td>Price</td><td>Defect rate</td><td>Pref. Fn_Buyer</td><td>Pref. Fn_Estimated</td><td>Zero profit frequency</td></tr><tr><td>S1</td><td>8.1501</td><td>1.8513</td><td>3.2622</td><td>3.6852</td><td>2</td></tr><tr><td>S2</td><td>7.5452</td><td>2.3644</td><td>3.0253</td><td>3.4541</td><td>2</td></tr><tr><td>S3</td><td>6.9494</td><td>2.8533</td><td>2.7993</td><td>3.2394</td><td>1</td></tr><tr><td>S4</td><td>6.7549</td><td>3.3563</td><td>2.7422</td><td>3.2104</td><td>0</td></tr><tr><td>S5</td><td>6.5659</td><td>3.8574</td><td>2.7013</td><td>3.1941</td><td>0</td></tr><tr><td>S6</td><td>6.3773</td><td>4.3576</td><td>2.6798</td><td>3.1887</td><td>0</td></tr><tr><td>S7</td><td>6.1882</td><td>4.8590</td><td>2.6829</td><td>3.1941</td><td>0</td></tr></table>

The provisional winner and the corresponding bid is highlighted in bold.

Table 4 Bids for round 3.

<table><tr><td colspan="6">Round 3</td></tr><tr><td>Seller</td><td>Price</td><td>Defect rate</td><td>Pref. Fn_Buyer</td><td>Pref. Fn_Estimated</td><td>Zero profit frequency</td></tr><tr><td>S1</td><td>8.0032</td><td>2.4302</td><td>3.2080</td><td>3.3403</td><td>3</td></tr><tr><td>S2</td><td>7.4331</td><td>2.7688</td><td>2.9875</td><td>3.1205</td><td>3</td></tr><tr><td>S3</td><td>6.8663</td><td>3.1227</td><td>2.7754</td><td>2.9121</td><td>2</td></tr><tr><td>S4</td><td>6.3034</td><td>3.4888</td><td>2.5785</td><td>2.7203</td><td>1</td></tr><tr><td>S5</td><td>6.1455</td><td>3.9002</td><td>2.5523</td><td>2.7024</td><td>0</td></tr><tr><td>S6</td><td>5.9883</td><td>4.3206</td><td>2.5433</td><td>2.6987</td><td>0</td></tr><tr><td>S7</td><td>5.8076</td><td>4.7465</td><td>2.5475</td><td>2.7024</td><td>0</td></tr></table>

The provisional winner and the corresponding bid is highlighted in bold.

In Round 2, the buyer selects S6. For α=1 we cannot <sup>fi</sup>nd a feasible solution to (WALFA). We increase α to 2 and <sup>fi</sup>nd $\mathrm { w _ { p } } = 0 . 6 6 8 8$ and $\mathrm { w } _ { \mathrm { d } } = 0 . 3 3 1 2 .$

The updated bids for Round 3 are given in Table 4.

Again S6 is selected in Round 3. We cannot <sup>fi</sup>nd a feasible solution for α=2. We set α=3 and <sup>fi</sup>nd $\mathrm { w _ { p } } = 0 . 6 2 1 7$ and $\mathsf { w } _ { \mathrm { d } } = 0 . 3 7 8 3$

The updated bids for Round 4 are given in Table 5.

S6 is selected in Round 4 again and the estimated parameter values are α=4, $\mathrm { w _ { p } } = 0 . 6 0 0 1$ , and $\begin{array} { r } { \mathsf { w } _ { \mathrm { d } } = 0 . 3 9 9 9 . } \end{array}$

Sellers update their bids with the given information. In Round 5, only S6 and S7 give pro<sup>fi</sup>table bids. The updated bids for Round 5 are given in Table 6.

In Round 5, the buyer is indifferent between S6 and S7 because the preference function values of the buyer for the two sellers are within the small threshold Δ value we use. We still write constraints indicating the preference of the bids of S6 and S7 over the remaining bids. These, however, do not provide us any new information, i.e. when we solve (WALFA), we <sup>fi</sup>nd the same α and weight values as in Round 4. There are still two pro<sup>fi</sup>table sellers, thus the algorithm continues. To support sellers for the next iteration, we improve the estimated contour and tell the sellers that their preference function for their updated bids should be on 2.1802 (2.2949×0.95) to be competitive. The estimated α and weight values of Round 4 are again used for Round 5.

The updated bids for Round 6 are given in Table 7.

In this round, the buyer selects S7. When we check the “Zero Pro<sup>fi</sup>t Frequency” column, we see that all values are positive indicating that there is no seller bidding pro<sup>fi</sup>tably. Therefore, the algorithm stops and the winning bidder is seller 7.

## 3. Experiments

We consider two and three-attribute cases. We use price and defect rate as the two attributes in both cases, and add lead time as the third attribute for the second case. We minimize all attributes. We denote price, defect rate, and lead time of the bid of seller i in the current round by p , q , and $\mathsf { l t } _ { \mathrm { i } } ,$ respectively.

Bids for round 4.

<table><tr><td colspan="6">Round 4</td></tr><tr><td>Seller</td><td>Price</td><td>Defect rate</td><td>Pref. Fn_Buyer</td><td>Pref. Fn_Estimated</td><td>Zero profit frequency</td></tr><tr><td>S1</td><td>7.9442</td><td>2.8844</td><td>3.1914</td><td>3.1917</td><td>4</td></tr><tr><td>S2</td><td>7.3763</td><td>3.1083</td><td>2.9735</td><td>2.9738</td><td>4</td></tr><tr><td>S3</td><td>6.8168</td><td>3.3525</td><td>2.7657</td><td>2.7660</td><td>3</td></tr><tr><td>S4</td><td>6.2679</td><td>3.6164</td><td>2.5739</td><td>2.5741</td><td>2</td></tr><tr><td>S5</td><td>5.7643</td><td>3.9017</td><td>2.4182</td><td>2.4184</td><td>0</td></tr><tr><td>S6</td><td>5.6230</td><td>4.2628</td><td>2.4156</td><td>2.4157</td><td>0</td></tr><tr><td>S7</td><td>5.4416</td><td>4.6318</td><td>2.4188</td><td>2.4188</td><td>0</td></tr></table>

The provisional winner and the corresponding bid is highlighted in bold.

Table 6 Bids for round 5.

<table><tr><td colspan="6">Round 5</td></tr><tr><td>Seller</td><td>Price</td><td>Defect rate</td><td>Pref. Fn_Buyer</td><td>Pref. Fn_Estimated</td><td>Zero profit frequency</td></tr><tr><td>S1</td><td>7.9132</td><td>3.2559</td><td>3.1877</td><td>3.1880</td><td>5</td></tr><tr><td>S2</td><td>7.3432</td><td>3.3942</td><td>2.9703</td><td>2.9705</td><td>5</td></tr><tr><td>S3</td><td>6.7840</td><td>3.5537</td><td>2.7633</td><td>2.7635</td><td>4</td></tr><tr><td>S4</td><td>6.2399</td><td>3.7362</td><td>2.5726</td><td>2.5728</td><td>3</td></tr><tr><td>S5</td><td>5.7180</td><td>3.9426</td><td>2.4067</td><td>2.4069</td><td>1</td></tr><tr><td>S6</td><td>5.2776</td><td>4.1875</td><td>2.2948</td><td>2.2949</td><td>0</td></tr><tr><td>S7</td><td>5.0870</td><td>4.5101</td><td>2.2949</td><td>2.2949</td><td>0</td></tr></table>

The provisional winner and the corresponding bid is highlighted in bold.

For our example problems, we generate seven sellers each having his/her own continuous cost function. The cost function of seller i for the two attribute case is constructed in the following form:

$$
\operatorname{cost} _ {\mathrm{i}} = \mathrm{f} _ {\mathrm{i}} (q _ {i}) = \left(\frac {1}{(q _ {i} - c) ^ {2}} + (6. 5 - c)\right) 1. 2
$$

where,

$$
c = 0. 5 (i - 1) \text {   is   a   constant   } i = 1, 2,..., 7.
$$

We generate a cost function in such a way that cost and defect rate has a negative relation, i.e., as the defect rate decreases (or quality increases) the cost increases. With such cost functions, each seller is competitive for different defect rate ranges. For instance, seller 1 has minimum cost for defect rates of approximately up to 1.54, whereas seller 2 has best cost performance for defect rates between 1.54 and 2.04. We experimented with various cost functions in order to come up with a mechanism to make the problem more interesting. This facilitates the sellers to be competitive for different attribute combinations.

We exploit the properties of these cost functions while assigning initial defect rates to generate nondominated bids. We take the maximum defect rate as 10. Then we calculate initial cost values using sellers' cost functions mentioned above. After <sup>fi</sup>nding the cost values, we assign a pro<sup>fi</sup>t rate to each seller and calculate price values for the initial round. We take the minimum pro<sup>fi</sup>t rate as 20% and the maximum pro<sup>fi</sup>t rate as 50%. We randomly generate values between 1.2 and 1.5 from a uniform distribution for each seller and multiply these with sellers' cost values to assign initial prices. With this, we assign defect rates and price values to sellers to compose bids for the initial round.

For the three attribute case the cost function is as follows:

$$
\mathrm{f} _ {i} (q _ {i}, l t _ {i}) = \left(\frac {1}{(q _ {i} - c) ^ {2}} + (6. 5 - c)\right) 1. 2 + \left(\frac {1 5}{l t _ {i} ^ {2}}\right)
$$

Table 7  
Bids for round 6.

<table><tr><td colspan="6">Round 6</td></tr><tr><td>Seller</td><td>Price</td><td>Defect rate</td><td>Pref. Fn_Buyer</td><td>Pref. Fn_Estimated</td><td>Zero profit frequency</td></tr><tr><td>S1</td><td>7.9132</td><td>3.2559</td><td>3.1877</td><td>3.1880</td><td>6</td></tr><tr><td>S2</td><td>7.3432</td><td>3.3942</td><td>2.9703</td><td>2.9705</td><td>6</td></tr><tr><td>S3</td><td>6.7840</td><td>3.5537</td><td>2.7633</td><td>2.7635</td><td>5</td></tr><tr><td>S4</td><td>6.2399</td><td>3.7362</td><td>2.5726</td><td>2.5728</td><td>4</td></tr><tr><td>S5</td><td>5.7180</td><td>3.9426</td><td>2.4067</td><td>2.4069</td><td>2</td></tr><tr><td>S6</td><td>5.2270</td><td>4.1764</td><td>2.2773</td><td>2.2774</td><td>1</td></tr><tr><td>S7</td><td>4.7779</td><td>4.4410</td><td>2.1970</td><td>2.1970</td><td>1</td></tr></table>

The provisional winner and the corresponding bid is highlighted in bold.

Table 8  
The results of the algorithm.

<table><tr><td>Seller</td><td>Price</td><td>Defect rate</td><td>Pref. Fn_Buyer</td></tr><tr><td>S1</td><td>7.9132</td><td>3.2559</td><td>3.1877</td></tr><tr><td>S2</td><td>7.3432</td><td>3.3942</td><td>2.9703</td></tr><tr><td>S3</td><td>6.7840</td><td>3.5537</td><td>2.7633</td></tr><tr><td>S4</td><td>6.2399</td><td>3.7362</td><td>2.5726</td></tr><tr><td>S5</td><td>5.7180</td><td>3.9426</td><td>2.4067</td></tr><tr><td>S6</td><td>5.2270</td><td>4.1764</td><td>2.2773</td></tr><tr><td>S7</td><td>4.7779</td><td>4.4410</td><td>2.1970</td></tr></table>

The provisional winner and the corresponding bid is highlighted in bold.

We construct a cost function in such a way that improved defect rate and lead time both increase the cost in different magnitudes. The relation of the defect rate with cost is the same as that in the two attribute case. We take the minimum value of lead time as 3 and the maximum value of lead time as 10.

We use the same initial defect rates as in the two attribute case. Then we randomly generate the lead time values and calculate the cost values according to the cost function constructed for the three attribute case. The price calculation is the same for both cases. We use these initial bids in our experiments.

We take the maximum price value as 15 and scale it between 0 and 10 to bring it roughly to a similar scale with the defect rate and lead time. Since we minimize all attributes, we take the ideal point where all attributes are zero.

We set the threshold, $\Delta { = } 0 . 0 0 1$ and interpret the buyer's preference of A over B, to imply $\mathsf { u } ( \mathsf { B } ) \geq \mathsf { u } ( \mathsf { A } ) ( 1 + \Delta )$ . Although it causes an additional nonlinearity in the model, we use it in the experiments as it is more realistic to make Δ a proportion of the preference value. However, for larger problems taking a threshold, Δ′, and requiring $\mathsf { u } ( \mathsf { B } ) \geq \mathsf { u } ( \mathsf { A } ) + \Delta ^ { \prime }$ could be a suf<sup>fi</sup>ciently good approximation leading to a simpler model. In some of our problems we applied both methods by setting Δ and Δ′ to the same constant. The results turned out to be roughly the same.

We set $\gamma { = } 0 . 0 5$ leading to a required improvement of 5% in each round. We used a lower bound $\mathsf { w } _ { 1 } = 0 . 0 5$ and an upper bound ${ \mathrm { w } } _ { \mathrm { u } } = 0 . 9 5$ for the weights in the (WALFA) problem to avoid extreme values of weights.

We use the following function as the buyer's underlying preference function.

$$
u = \left(\sum_ {j = 1} ^ {J} \left(\lambda_ {j} \left(a _ {j} - z _ {j} ^ {*}\right)\right) ^ {t}\right) ^ {1 / t}
$$

where

$$
\begin{array}{l l} \lambda_ {j} & \text {the weight of attribute j} \\ a _ {j} & \text {level of attribute j} \\ z _ {j} ^ {*} & \text {the ideal value of attribute j} \\ t & \text {the parameter of the underlying L_{\alpha} metric} \end{array}
$$

Table 9  
The results found with exact values of parameters.

<table><tr><td>Seller</td><td>Price</td><td>Defect rate</td><td>Pref. Fn_Buyer</td></tr><tr><td>S1</td><td>7.9132</td><td>3.2554</td><td>3.1877</td></tr><tr><td>S2</td><td>7.3433</td><td>3.3937</td><td>2.9703</td></tr><tr><td>S3</td><td>6.7841</td><td>3.5532</td><td>2.7633</td></tr><tr><td>S4</td><td>6.2400</td><td>3.7358</td><td>2.5726</td></tr><tr><td>S5</td><td>5.7181</td><td>3.9422</td><td>2.4067</td></tr><tr><td>S6</td><td>5.2272</td><td>4.1760</td><td>2.2773</td></tr><tr><td>S7</td><td>4.7781</td><td>4.4407</td><td>2.1970</td></tr></table>

The provisional winner and the corresponding bid is highlighted in bold.

Table 11  
Table 10  
% deviations between the results of the algorithm and exact solutions for two attribute case.

<table><tr><td>t=1</td><td>t=2</td><td>t=3</td><td></td><td></td><td>t=4</td><td></td><td></td><td></td><td></td></tr><tr><td> $\lambda_p=0.8$ </td><td> $\lambda_p=0.5$ </td><td> $\lambda_p=0.8$ </td><td> $\lambda_p=0.5$ </td><td> $\lambda_p=0.3$ </td><td> $\lambda_p=0.8$ </td><td> $\lambda_p=0.6$ </td><td> $\lambda_p=0.5$ </td><td> $\lambda_p=0.4$ </td><td> $\lambda_p=0.2$ </td></tr><tr><td> $\lambda_d=0.2$ </td><td> $\lambda_d=0.5$ </td><td> $\lambda_d=0.2$ </td><td> $\lambda_d=0.5$ </td><td> $\lambda_d=0.7$ </td><td> $\lambda_d=0.2$ </td><td> $\lambda_d=0.4$ </td><td> $\lambda_d=0.5$ </td><td> $\lambda_d=0.6$ </td><td> $\lambda_d=0.8$ </td></tr><tr><td>0.0000</td><td>0.0013</td><td>0.0311</td><td>0.0000</td><td>0.3072</td><td>0.1033</td><td>0.0000</td><td>0.0209</td><td>0.0142</td><td>0.1308</td></tr></table>

We test the algorithm on 17 problems for different combinations of t and $\lambda _ { \mathrm { j } }$ values for both two and three attribute cases.

## 4. Results

To test the performance of the algorithm, we compare the results of the algorithm with the ones found using the exact parameter values. We want to see what the results would be if we knew the preference function of the buyer explicitly assuming that the sellers would bid with zero pro<sup>fi</sup>t. Thus we solve the following (EX\_PAR ) problem with known parameter values and <sup>fi</sup>nd the best possible attribute level combinations that the sellers can give with zero pro<sup>fi</sup>t to maximize the bene<sup>fi</sup>t of the buyer.

The parameters and the decision variables are the same as before and the model is as follows:

Problem (EX\_PAR<sub>i</sub>)

Min u s<sub>i</sub>

12

s.to

$$
u (s _ {i}) = \left[ \sum_ {j = 1} ^ {J} \left(\lambda_ {j} \left(a _ {i j} - z _ {j} ^ {*}\right)\right) ^ {t} \right] ^ {1 / t}\tag{13}
$$

$$
a _ {i 1} - f _ {i} (s _ {i}) \geq 0\tag{14}
$$

In (EX\_PAR ), the objective is to <sup>fi</sup>nd a bid for seller i that minimizes the distance from the ideal point in terms of the $\mathrm { L } _ { \alpha }$ metric while avoiding any loss.

In Tables 8 and 9, the results of the algorithm and the ones found by EX\_PAR for the example problem in Section 2.6 are given respectively. When we look at the results, we see that our estimations are close to the true values and we guide the sellers well. The last rows of Tables 8 and 9 in bold show that the winning bidders are the same (seller 7 for both) and the preference function values of the buyer are the same for both cases except for small differences that have been eliminated due to rounding off. Also the preference function value of the buyer for all bids and the attribute values are almost the same for the corresponding entries of Tables 8 and 9.

In all problems for both two and three attribute cases, the winning bidder(s) found with the algorithm and (EX\_PAR ) problem with exact parameter values are the same. We also compare the preference function values of the buyer for the winning bidders found with the algorithm and with (EX\_PAR ). To evaluate the performance of the algorithm for these values we use % deviations:

% deviations between the results of the algorithm and exact solutions for three attribute case.

<table><tr><td>t=1</td><td>t=2</td><td>t=3</td><td></td><td></td><td>t=4</td><td></td></tr><tr><td> $\lambda_{p}=0.3$ </td><td> $\lambda_{p}=0.2$ </td><td> $\lambda_{p}=0.7$ </td><td> $\lambda_{p}=0.2$ </td><td> $\lambda_{p}=0.3$ </td><td> $\lambda_{p}=0.7$ </td><td> $\lambda_{p}=0.2$ </td></tr><tr><td> $\lambda_{d}=0.4$ </td><td> $\lambda_{d}=0.1$ </td><td> $\lambda_{d}=0.2$ </td><td> $\lambda_{d}=0.1$ </td><td> $\lambda_{d}=0.4$ </td><td> $\lambda_{d}=0.2$ </td><td> $\lambda_{d}=0.1$ </td></tr><tr><td> $\lambda_{lt}=0.3$ </td><td> $\lambda_{lt}=0.7$ </td><td> $\lambda_{lt}=0.1$ </td><td> $\lambda_{lt}=0.7$ </td><td> $\lambda_{lt}=0.3$ </td><td> $\lambda_{lt}=0.1$ </td><td> $\lambda_{lt}=0.7$ </td></tr><tr><td>0.6995</td><td>0.0000</td><td>0.1457</td><td>0.0519</td><td>0.0199</td><td>0.0041</td><td>0.0001</td></tr></table>

$$
\% \text { deviation } = \left(\frac {u (\text { final\_bid }) - u (\text { optimal\_bid })}{u (\text { optimal\_bid })}\right) 100
$$

In the formula u(final \_bid)refers to the preference function value of the <sup>fi</sup>nal bid of seller i found by the algorithm whereas u(optimal \_bid) refers to the preference function value of the optimal solution found by (EX\_PAR<sub>i</sub>).

For each problem, we check the percent deviation of the buyer's preference function values of the winning bidders. As can be seen from Tables 10 and 11, the percent deviations are very small, i.e. for all problems the buyer's preference function found with the algorithm is close to that found by (EX\_PAR ) with the exact parameters. These imply that the estimation and guidance mechanisms of our approach worked well in all the test problems.

## 5. Conclusions

In this study we address the multi-attribute, single-item reverse auctions. We develop an interactive approach for a progressive auction environment. In our approach, we estimate the parameter values of the underlying preference function of the buyer using his/ her past preferences. At each iteration we improve the estimated preference function values and inform the sellers about our estimations. Then the sellers update their bids to be competitive and the auction continues until none of the sellers can bid pro<sup>fi</sup>tably. Our experiments show that the mechanism supports the sellers well and the winning bids are very close to the bids that would have been obtained under full information.

In our experiments, we consider few sellers and at each iteration we present all bids to the buyer. However, for larger auctions the buyer can be provided with a representative group of bids to choose the best one among them. Building the details and testing such a procedure awaits future experiments. Also, we assume that the buyer is consistent in his/her expressed preferences when choosing among bids. Another future research area may be to test the robustness of the algorithm to inconsistencies in the buyer's preferences.

Our results show that decision support tools have important potential bene<sup>fi</sup>ts for all parties participating in auctions. We believe that this is an important area for future studies, especially for more complex auction environments.

## References

[1] R. Bapna, W. Jank, G. Shmueli, Price formation and its dynamics in online auctions, Decision Support Systems 44 (3) (2008) 641–656.

[2] Ş. Baykal, Combinatorial Auction Problems, Master's Thesis, Department of Industrial Engineering, Middle East Technical University (2007).

[3] M.J. Bellosta, I. Brigui, S. Kornman, D. Vanderpooten, A multi-criteria model for electronic auctions, Proceedings of ACM Symposium on Applied Computing, Nicosia, Cyprus, March 14–17, 2004, pp. 759–765.

[4] M. Bichler, J. Kalagnanam, Con<sup>fi</sup>gurable offers and winner determination in multiattribute auctions, European Journal of Operational Research 160 (2) (2005) 380-394.

[5] J. Catalán, R. Epstein, M. Guajardo, D. Yung, C. Martínez, Solving multiple scenarios in a combinatorial auction, Computers & Operations Research 36 (10) (2009) 2752-2758

[6] M. Herschlag, R. Zwick, Internet auctions — popular and professional literature review, Quarterly Journal of Electronic Commerce 1 (2) (2002) 161–186.

[7] G. Hohner, J. Rich, E. Ng, G. Reid, A.J. Davenport, J.R. Kalagnanam, H.S. Lee, C. An, Combinatorial and quantity–discount procurement auctions bene<sup>fi</sup>t, Mars, incorporated and its suppliers Interfaces 33 (1) (2003) 23–35.

[8] R.L. Keeney, H. Raiffa, Decision Making with Multiple Objectives: Preferences and Value Tradeoffs, Cambridge University Press, Cambridge, 1993.

[9] M. Köksalan, R.L. Leskelä, H. Wallenius, J. Wallenius, Improving ef<sup>fi</sup>ciency in multiple-unit combinatorial auctions: bundling bids from multiple bidders, Decision Support Systems 48 (2009) 103–111.

[10] O.R. Koppius, E. van Heck, M.J.J. Wolters, The importance of product representation online: empirical results and implications for electronic markets, Decision Support Systems 38 (2) (2004) 161–169.

[11] P.J. Korhonen, J. Laakso, A visual interactive method for solving the multiple criteria problem, European Journal of Operational Research 24 (2) (1986) 277–287.

[12] R.L. Leskelä, J.E. Teich, H. Wallenius, J. Wallenius, Decision support for multi-unit combinatorial bundle auctions, Decision Support Systems 43 (2) (2007) 420–434.

[13] T. Metty, R. Harlan, Q. Samelson, T. Moore, T. Morris, R. Sorensen, A. Schneur, O. Raskina, R. Schneur, J. Kanner, K. Potts, J. Robbins, Reinventing the supplier negotiation process at Motorola, Interfaces 35 (1) (2005) 7–23.

[14] E.J. Pinker, Y. Seidman, Y. Vakrat, Managing online auctions: current business and research issues, Management Science 49 (11) (2003) 1457–1484.

[15] T. Sandholm, D. Levine, M. Concordia, P. Martyn, R. Hughes, J. Jacobs, D. Begg, Changing the game in strategic sourcing at Procter&Gamble: expressive competition enabled by optimization, Interfaces 36 (1) (2006) 55–68.

[16] S. Talluri, R. Narasimhan, S. Viswanathan, Information technologies for procurement decisions: a decision support system for multi-attribute e-reverse auctions, International Journal of Production Research 45 (11) (2007) 2615–2628.

[17] J.E. Teich, H. Wallenius, J. Wallenius, A. Zaitsev, A multi-attribute e-auction mechanism for procurement: theoretical foundations, European Journal of Operational Research 175 (2006) 90–100.

Gülşah Karakaya received her B.Sc. and M.Sc. degrees from the Department of Industrial Engineering, Middle East Technical University in 2007 and 2009, respectively. She is currently a Ph.D. candidate and has been working as a research assistant since 2007 in the same department. Her main research interests are multiple criteria decision making, decision support systems, and combinatorial optimization.

Murat Köksalan is a professor in the Department of Industrial Engineering, Middle East Technical University. He has been a visiting professor at SUNY Buffalo, Purdue University, Helsinki University of Technology, Helsinki School of Economics, and Aalto University on various occasions. He is the recipient of the young researcher award of the Scienti<sup>fi</sup>c and Technological Research Council of Turkey and The MCDM Gold Medal of the International Society on Multiple Criteria Decision Making. He is the founding president of INFORMS Section on MCDM. He won the <sup>fi</sup>rst prize at the INFORMS Case Competition with various co-authors three times. His academic interests include multiple criteria decision making, combinatorial optimization, heuristic search in general and evolutionary algorithms in particular, combinatorial auctions, and preparing teaching cases.
