---
otero_id: 15938
otero_key: "M4EDFF7V"
title: "On financial transmission rights and market power"
authors: "Geoffrey Pritchard; Andy Philpott"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.09.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# On financial transmission rights and market power

Geoffrey Pritchard<sup>a</sup>, Andy Philpott<sup>b,\*</sup>

<sup>a</sup>Department of Statistics, University of Auckland, Private Bag 92019, New Zealand <sup>b</sup>Department of Engineering Science, University of Auckland, Private Bag 92019, New Zealand

Available online 30 October 2004

## Abstract

This paper studies financial transmission rights in electricity pool markets with nodal pricing, when these rights are to be allocated by an auction mechanism. A market distribution function approach is used to investigate the effects on electricity offering behaviour when participants hold financial transmission rights, and the implications of this for the auction design are discussed.

<sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Financial transmission rights; Electricity markets; Nodal pricing

## 1. Introduction

Electricity pool markets based on nodal pricing have emerged in a number of regions of North and South America, Australia, New Zealand, and the Nordic countries. In an electricity pool with a single node, all market participants trade (at any one point in time) at a single system marginal price. In a full nodal pricing model, the price depends on location. In the absence of constraints and losses the price at every node is identical to the system marginal price. In practice thermal constraints on the power flow in the lines, and power losses due to line impedance, result in a set of prices that vary with location. The variation of electricity spot prices with location in these markets has resulted in the development of market instruments to hedge the volatility in these price differences.

Financial transmission rights (FTRs) are one approach to solving this problem. An FTR is a financial instrument held by a market participant that pays an income stream based on the nodal prices observed in the transmission system over the course of the contract. An FTR can be specified by a vector of nodal loads and injections (where the loads are taken as positive) and the coupon payment at any time is equal to the inner product of the nodal price vector with the FTR. (In practice, most FTRs involve only two nodes). FTRs were first proposed by Hogan [5], and have received a lot of attention in the literature under various names (they are called fixed transmission rights in the PJM market, transmission congestion contracts or TCCs in New York, and financial congestion contracts, or FCCs in New England).

Our purpose in this paper is to provide a framework in which to study some of the effects on participant behaviour in pool markets, when some of them hold FTR contracts. One approach to investigating these effects is to model electricity markets as a Nash–Cournot game in which each generator offers a single quantity of energy assuming zero conjectural variations. It is possible to construct Nash equilibria for these models, and use these to investigate the effects of FTRs on agent behaviour. By restricting attention to single offers facing a known elastic demand function, the Nash–Cournot model has some deficiencies in representing the true situation, in that generators in most pool markets typically offer supply functions rather than single offers, and demand is uncertain. One approach to reflect the first of these features of pool markets is to optimize over a parametrized family of supply functions (see Ref. [4] for a linear supply function model of this type). However, as observed in Ref. [1], the real advantage of supply function offers in practice comes from their ability to optimize over a range of uncertain demands, and this flexibility will only be represented for highdimensional parametrizations resulting in considerable computational effort. On the other hand, the construction of general supply–function equilibria in a network setting seems to be very difficult.

A compromise is to use the market distribution approach of Anderson and Philpott [2], which treats competitors as if they offered supply functions drawn from a suitable probability distribution, called the market distribution. Since demand shocks can be modelled as vertical shifts in a competitor’s supply function, the market distribution can be constructed so that it also incorporates uncertainty in demand. We present several examples to illustrate the power of the market distribution approach in evaluating the effects of FTRs on competitor behaviour.

The paper is laid out as follows. In the next section, we give a formal definition of financial transmission rights, and state the revenue adequacy theorem. In Section 3, we discuss the effect of FTRs on generators who already have some degree of market power. We show by example that FTRs may encourage the use of this power or discourage it depending on the location of the generator in the network. These examples have their origins in the work of Joskow and Tirole [8]. Section 4 discusses the design of an auction for the creation and allocation of FTRs, and the behaviour of strategic bidders with market power in the energy market. We conclude the paper with a general discussion in Section 5.

## 2. Financial transmission rights

The coupon payment for an FTR contract comes from a linear combination of nodal electricity prices. In pool markets, these are computed by the Independent System Operator (ISO) who solves an optimal dispatch problem. In most market situations, this problem can be formulated as some version of the following convex optimization problem.

$$
\begin{array}{l l} P: & \text { minimize } \\ & \text { subject   to } \\ & g _ {i} (f) + \sum_ {j \in O (i)} x _ {j} - z _ {i} = d _ {i}, \quad i = 1, 2, \ldots , n \\ & z _ {i} \geq 0, \quad \quad \quad \quad \quad \quad \quad \quad \quad i = 1, 2, \ldots , n \\ & x \in X \\ & f \in U \end{array}
$$

In this model, each generator offers a piecewise constant nondecreasing supply function, made up of a finite set of tranches of power. The variable $x _ { j }$ is the level of dispatch of offer tranche $\mathrm { \Sigma } _ { j \in O \left( i \right) }$ where $O ( i )$ is the set of tranches offered at node $i ,$ and each tranche $\mathrm { \Sigma } _ { j \in O \left( i \right) }$ is offered at price $c _ { j }$ . We require that x lies in the convex set $X ,$ which defines the tranche levels. Although the problem P assumes (as in most electricity pool markets) that generators offer supply curves that are step functions, in what follows the analysis will hold for any nondecreasing supply function.

The first set of constraints in $P$ represents conservation of flow at the nodes, where $d _ { i }$ is the demand at node i, and the variable $f$ is a vector of branch flows. The electricity price $\pi _ { i }$ at node i is then taken to be the Lagrange multiplier of the ith constraint.

The function $g _ { i } ( f )$ is a general concave function giving the amount of power flow entering node i when the link flows are $f .$ Approximations based on DC load flow define $g _ { i } ( f )$ to be a concave quadratic function, meaning that branch losses are a quadratic function of power flow. Alternatively, a linear programming representation of $P$ treats $g _ { i } ( f )$ as a concave piecewise linear function. Both of these models (as well as a model without losses) are special cases of the general framework we use. We require the vector of flows f to lie in the convex set $U ,$ which represents any flow bounds on f as well as any electrical constraints (such as loop flow constraints) that the flows must satisfy.

In this framework, a financial transmission right contract (FTR) is defined to be a vector h(a) with n components. The contract with vector h(a) pays its holder $\textstyle \sum _ { i } \pi _ { i } h _ { i } ( \alpha )$ once the dispatch problem has been solved. (This is a fairly general notion of FTR; it includes the common <sup>b</sup>balanced<sup>Q</sup> FTR (in which there are nodes $i _ { 1 } , i _ { 2 }$ with $h _ { i , } ( \alpha ) { = } { - } h _ { i , } ( \alpha )$ and $h _ { j } ( \alpha ) { = } 0$ for all $j \not \in \{ i _ { 1 } , i _ { 2 } \} $ and <sup>b</sup>spot<sup>Q</sup> FTR (in which there is a node $i _ { 1 }$ with $h _ { j } ( \alpha ) { = } 0$ for all ${ j } { \neq } i _ { 1 } )$ as well as other types). Suppose that these are simultaneously feasible in the sense that there exist $y , z$ with

$$
\begin{array}{r c l l} S F: g _ {i} (y) - z _ {i} & = & \sum_ {\alpha} h _ {i} (\alpha), & i = 1, 2, \ldots , n \\ z _ {i} & \geq & 0, & i = 1, 2, \ldots , n \\ y & \in & U. \end{array}
$$

That is, $\textstyle \sum _ { \alpha } h ( \alpha )$ represents a vector of injections and offtakes which may be <sup>b</sup>dispatched through the grid<sup>Q</sup>. Note that it is permissible to shed power at nodes (i.e. to have $z _ { i } { > } 0 )$ .

Simultaneous feasibility for a set of FTRs is a desirable property due to the following well known result that states that rentals accrued by the ISO in a wholesale pool electricity market are sufficient to fund the coupon payments for FTRs, if the FTRs satisfy SF. This result was first proved by Hogan [5] for lossless networks, extended to quadratic losses by Bushnell and Stoft [3], and further generalised to smooth nonlinear constraints by Hogan [7]. A proof for the general convex case can be found in Ref. [9].

Theorem 1. When the extant FTR contracts are simultaneously feasible as above, the rentals earned by the ISO are sufficient to fund the coupon payments to the FTR holders.

## 3. FTRs and market power

This section explores the consequences of awarding financial transmission rights to electricity market participants large enough to influence market prices. It is well-understood that a generator with market power (i.e. a <sup>b</sup>price-maker<sup>Q</sup>) will engage in strategic offering in order to maximize its profit. In general, this means offering supply at a price above marginal cost, or withholding some supply, or both, in order to increase the price at which electricity can be sold.

Intuitively, it is clear that ownership of FTRs by a price maker will modify this behaviour, by increasing or decreasing the incentive to force up the price at the local node. Very simple economic models such as those to be found in Ref. [8] confirm that when an FTR over a line from an <sup>b</sup>upstream<sup>Q</sup> location to a <sup>b</sup>downstream<sup>Q</sup> location is awarded to a price making generator:

<sup>!</sup> If the generator is in the downstream location, its strategy will tend to become more <sup>b</sup>aggressive<sup>Q</sup> (i.e. even further removed from the competitive strategy of offering all available supply at its marginal cost), as there is now even more incentive to force up the local price.

<sup>!</sup> If the generator is in the upstream location, its strategy will tend to become less aggressive— there is now less incentive to force up the local price.

In a network with loop flow, either of the above effects is possible depending on the locations of the generator and the FTR. Finally, all of the above effects will be reversed if the FTR goes in the <sup>b</sup>wrong<sup>Q</sup> direction (e.g. from a downstream node to an upstream one). (Such an FTR may seem unlikely, but could arise if the FTR-holder made a wrong guess as to the direction of the flow on the line. For example, the line between the two islands of New Zealand usually carries the South Island’s abundant hydropower northwards, but in a dry year may find itself constrained in the opposite direction).

In the remainder of this section, we present two examples which illustrate in more detail how the problem of optimizing a price maker’s offer curve is affected by the presence of FTRs. We use the market distribution function methodology of Ref. [2], wherein a general theory is presented for constructing a legal (i.e. nondecreasing) offer curve in response to uncertain demand and competitor behaviour. The uncertainty and hence the need to consider complete offer curves rather than single offers is important, since one motivation for the existence of FTRs is to allow uncertain price differences to be hedged.

Example 1. FTR mitigating the effects of market power.

Consider a two-node electricity transmission network as shown in Fig. 1 in which <sup>b</sup>we<sup>Q</sup> are the only generator with market power.

A competitive fringe consisting of many smaller generators and demand side participants provides additional supply $^ { \circ } \mathrm { G } 1 ^ { \circ } { } ^ { \circ }$ and $^ { 6 6 } \mathrm { G } 2 ^ { \circ }$ , which is offered to the market via fixed aggregated offer curves. For simplicity, assume that these take the forms $q { = } \beta _ { 1 } p$ and $\scriptstyle q = \beta _ { 2 } p$ (with $\beta _ { 1 } { > } 0 , \ \beta _ { 2 } { > } 0 )$ at nodes 1 and 2, respectively. Demand D is located at node 2 and is random, with a probability density function $f .$ The transmission line is lossless, but has a maximum capacity L. Suppose that we can generate power at no marginal cost, and that we own a balanced FTR for quantity $q _ { f }$ from node 1 to node 2.

The FTR means that we are effectively selling part of our output (a quantity $q _ { f } )$ at the node 2 price $p _ { 2 } ,$ rather than the node 1 price $p _ { 1 }$ . Since we have less direct influence over $p _ { 2 }$ than over $p _ { 1 }$ , one might intuitively expect that the FTR will reduce our natural desire to force up $p _ { 1 }$ by withholding supply. One might also expect that the line capacity constraint will be more likely to be reached, since our ownership of the FTR incentivizes us to create this very outcome. Both of these things turn out to be the case, as the following analysis shows.

Our possible dispatches lie in the region depicted in Fig. 2.

We will be dispatched at a point $( q , p )$ on our offer curve, with the line not at capacity, whenever $q { + } \beta _ { 1 } p { < } L$ . This will be achieved for demand level $D { = } q { + } ( \beta _ { 1 } { + } \beta _ { 2 } ) p$ , since the two nodal prices will be equal. Alternatively, we may be dispatched at $( q , p )$ with the line at capacity, if $\cdot \ q + \beta _ { 1 } p { = } L$ . This will require $D { \ge } L { + } \beta _ { 2 } p$ , and the price at node 2 will then be $p _ { 2 } { = } \beta _ { 2 } ^ { - 1 } ( D { - } L )$ . A dispatch with $q { + } \beta _ { 1 } p { > } L$ is clearly not possible.

![](/api/attachments/M4EDFF7V/fulltext/images/95962b68371fd52c37309c438945cb16b7bf5a2988a81cbdd335a5697c352ee0.jpg)  
Fig. 1. Network for Example 1.

![](/api/attachments/M4EDFF7V/fulltext/images/e00861f3b72349b49ae2d648ffd44c44440d2c5c282fff22fb4a77309039422a.jpg)  
Fig. 2. Dispatch region for strategic generator in Example 1.

Letting $\psi ( q , p )$ denote the probability that we are dispatched at a point on our offer curve below $( q , p )$ (as in Ref. [2]), we have for $q { + } \beta _ { 1 } p { < } L$

$$
\begin{array}{l} \frac {\partial \Psi}{\partial q} (q, p) = f (q + (\beta_ {1} + \beta_ {2}) p) \\ \frac {\partial \Psi}{\partial q} (q, p) = f (q + (\beta_ {1} + \beta_ {2}) p) (\beta_ {1} + \beta_ {2}) \end{array}
$$

The expected revenue generated by an offer curve $T$ with endpoint $( q _ { T } , p _ { T } )$ is thus

$$
\begin{array}{l} \rho (T) = \int_ {T} q p f (q + (\beta_ {1} + \beta_ {2}) p) (\mathrm{d} q + (\beta_ {1} + \beta 2) \mathrm{d} p) \\ \quad + \int_ {q _ {T} + (\beta_ {1} + \beta_ {2}) p _ {T}} ^ {\infty} \left(q _ {T} p _ {T} + q _ {f} \left(\beta_ {2} ^ {- 1} (x - L) - p _ {T}\right)\right) \\ \times f (x) \mathrm{d} x \end{array} \tag {1}
$$

The optimum curve T (see Fig. 2) may be determined as follows. Fix the endpoint $( q _ { T } , p _ { T } )$ , and consider variations to the rest of T. Since the second term in $\operatorname { E q . }$ (1) is now constant, the arguments of Ref. [2] show that the optimum curve must at each point either be horizontal or vertical, or satisfy the equation $Z { = } 0 .$ where

$$
\begin{array}{l} Z = p (\partial \Psi / \partial p) - q (\partial \Psi / \partial q) \\ = ((\beta_ {1} + \beta_ {2}) p - q) f (q + (\beta_ {1} + \beta_ {2}) p). \end{array}
$$

From this it is not hard to see that the optimum T must resemble one of the two solid curves in Fig. 3.

(Note the role being played here by the requirement that the offer curve be monotone increasing in both $p$ and $q$ . If it were not for this constraint, the solution would be to choose $T$ to be the curve $q { = } ( \beta _ { 1 } { + } \beta _ { 2 } ) p$ , then discontinuously jump to whatever endpoint $( q _ { T } , p _ { T } )$ would optimize the second term of Eq. (1).

![](/api/attachments/M4EDFF7V/fulltext/images/feb8badfc74f53e870b7b7c778624e8c7d3f6da0dde37a3b5d6c3827340e620f.jpg)  
Fig. 3. Candidate optimal offer curves.

Assuming this form for $T ,$ it is possible to write the first integral in Eq. (1) as a function of $( q _ { T } , p _ { T } )$ . It then remains only to perform a one-dimensional optimization over $( q _ { T } , p _ { T } )$ to determine the optimal $T .$ The particular point $( q _ { T } , p _ { T } )$ which turns out to be optimal will, in general, depend on $f ,$ i.e. on the demand distribution, as well as on $q _ { f } .$

The effect of the FTR on this offer curve can easily be seen. The effect of $q _ { f }$ on $\rho ( T )$ is to contribute the term

$$
q _ {f} \int_ {L + \beta_ {2} p _ {T}} ^ {\infty} \left(\frac {x - L}{\beta_ {2}} - p _ {T}\right) f (x) d x
$$

which for $q _ { f } { > } 0$ is a decreasing function of $p _ { T } .$ (Its derivative with respect to $p _ { T }$ is $- q _ { f } P ( D \ge L + \beta _ { 2 } p _ { T } )$ The optimum curve when $q \mathrm { > } 0$ will therefore have smaller $p _ { T }$ than when $q _ { f } { = } 0$

In other words, our natural tendency to offer aggressively (withholding supply) will be reduced in the presence of the FTR. Observe, too, that this has the effects of reducing the expected price paid by consumers at node 2, and increasing the probability that the line constraint will become active.

If our FTR went in the other direction (from node 2 to node 1), it would instead lead to a more aggressive strategy. This can be seen by considering negative values of $q _ { f } .$

For a numerical example, suppose that $L { = } 1 0 0$ MW and $\beta _ { 1 } { = } \beta _ { 2 } { = } 1 ~ \mathrm { M W } ^ { 2 } / \mathbb { S }$ , while the demand D has a normal distribution with mean 150 MW and standard deviation 20 MW. Optimal offer curves for several values of $\dot { } q _ { f }$ are depicted in Fig. 4. When $q _ { f } { = } 1 0 0 \ \mathrm { M W }$ $( \mathrm { i . e }$ . the full capacity of the line) the optimal curve has $p _ { T } { = } \mathbb { S } 0 . 3 0 / \mathrm { M W } ,$ , which makes it hardly distinguishable from the $q$ axis. In this case, our strategy has been almost reduced to the competitive one, which is to offer at zero price.

![](/api/attachments/M4EDFF7V/fulltext/images/5fac4b8abcaba24f659d2276bfca4cfb139040df04ca837b3390750066b7a6b5.jpg)  
Fig. 4. Optimum offer curves for varying $q _ { f } .$

An interesting variant of this problem can be obtained by removing the competitive fringe at node 1. The dashed line is then replaced by a vertical one, so the monotonicity constraint allows a jump discontinuity at the endpoint of T. It turns out that in this case, the FTR does not affect our behaviour. A similar problem (though without the full supply curve) is worked out in Ref. [8].

Example 2. FTR exacerbating the effects of market power.

Consider the three-node network shown in Fig. 5, in which $\mathbf { \tilde { \Sigma } } ^ { \mathrm { s } } \mathbf { w } \mathbf { e } ^ { \mathbf { \Sigma } ^ { \ast } }$ are the only generator large enough to influence prices.

A competitive fringe consisting of many smaller generators provides additional supply $^ { 6 6 } \mathrm { G } 1 ^ { \circ }$ and $^ { \circ } \mathrm { G } 2 ^ { \circ }$ 4 which is offered to the market via fixed aggregated offer curves. For simplicity, assume that these take the forms $q { = } \beta _ { 1 } p$ and $\scriptstyle q = \beta _ { 2 } p$ at nodes 1 and 2, respectively. Demand $D$ is located at node 3 and is random, with a probability density function $f .$ There are no line losses, and no line capacity constraints other than the 100 MW limit on the line between nodes 2 and 3. The three lines have equal admittances. (The significance of this last point is that 1/3 of any power injected at node 1, and 2/3 of any power injected at node 2, must flow via the limited capacity line to reach the load). Suppose that we can generate power at no marginal cost, and that we own a balanced FTR for $q _ { f }$ megawatts from node 1 to node 3.

![](/api/attachments/M4EDFF7V/fulltext/images/b3a80a9cea6422dfa4762c1f5b5a84165714bd4371d589d61da46c1a7e133869.jpg)  
Fig. 5. Network for Example 2.

What supply curve should we offer, and how is this affected by the presence of the FTR? An analysis of the dispatch problem shows that the nodal prices $p _ { 1 }$ $p _ { 2 } .$ , and $p _ { 3 }$ will always satisfy $p _ { 3 } - p _ { 1 } = p _ { 1 } - p _ { 2 }$ . Thus, for a given value of $p _ { 2 } ,$ increasing $p _ { 1 }$ will also increase the difference $p _ { 3 } - p _ { 1 }$ and hence the revenue from the FTR. This suggests that the price-maker’s usual incentive to force up the local price by withholding supply will be reinforced by the presence of the FTR. The following analysis shows that this is indeed the case.

Consider a point $( q , p )$ through which our supply curve may pass. It may be that we are dispatched at the point $( q , p )$ without constraining the line between nodes 2 and 3; this is possible if and only if

$$
\frac {1}{3} (q + \beta_ {1} p) + \frac {2}{3} \beta_ {2} p <   1 0 0
$$

since in this case the price will be p at every node. The level of load which achieves this is $D { = } q { + } ( \beta _ { 1 } { + } \beta _ { 2 } ) p$

Now consider a point $( q , p )$ with $q \mathrm { + } ( \beta _ { 1 } \mathrm { + } 2 \beta _ { 2 } )$ $p { > } 3 0 0$ . It may still be possible to be dispatched at such a point, but only in a situation where the line between nodes 2 and 3 is at capacity, and the nodal prices are unequal. This requires

$$
\begin{array}{l} \frac {1}{3} (q + \beta_ {1} p _ {1}) + \frac {2}{3} \beta_ {2} p _ {2} = 1 0 0 \\ q + \beta_ {1} p _ {1} + \beta_ {2} p _ {2} = D \\ p _ {1} = p \\ p _ {3} - p _ {1} = p _ {1} - p _ {2}. \end{array}
$$

Solving, we find that $D { = } 1 5 0 { + } ( q { + } \beta _ { 1 } p ) / 2$ and $p _ { 2 } { = }$ $( 3 0 0 - q - \beta _ { 1 } p ) / 2 \beta _ { 2 }$ (hence $p _ { 3 } - p _ { 1 } = p _ { 1 } - p _ { 2 } = ( q +$ $( \beta _ { 1 } { + } 2 \beta _ { 2 } ) p { - } 3 0 0 ) / 2 \beta _ { 2 } )$ . Note that this is positive.

(In this model, every possible dispatch has $p _ { 1 } \geq p _ { 2 }$ and so our revenue from the FTR will never be negative). Such a dispatch is possible for any $( q , p )$

![](/api/attachments/M4EDFF7V/fulltext/images/f76eb3351247974857469a9bed93fdc645d6f2ae9ae4bfaf2e744f6bf1ff734d.jpg)  
Fig. 6. An offer curve for Example 2.

with $q { + } \beta _ { 1 } p { \le } 3 0 0$ . For $q { + } \beta _ { 1 } p { > } 3 0 0$ , the above equations are invalid, as they give $p _ { 2 } { < } 0$ , and in that case the generation at node 2 should be 0 rather than $\beta _ { 2 } p _ { 2 }$

In fact, it is never possible for us to be dispatched at a point $( q , p )$ with $q { + } \beta _ { 1 } p { > } 3 0 0$ , since in that case the generation at node 1 alone will already be enough to violate the line capacity constraint between nodes 2 and 3.

Our offer curve T must therefore pass through two distinct regions, labelled I and II as shown in Fig. 6. In region II, the line between nodes 2 and 3 will be at capacity; in region I, it will not.

Following Ref. [2], let $\psi ( q , p )$ denote the probability that we are dispatched at a point below $( q , p )$ on our offer curve. (Here $( q , p )$ is assumed to be a point on that curve). The above remarks imply that for $( q , p )$ in region I,

$$
\frac {\partial \Psi}{\partial q} (q, p) = f (q + (\beta_ {1} + \beta_ {2}) p)
$$

$$
\frac {\partial \Psi}{\partial q} (q, p) = f (q + (\beta_ {1} + \beta_ {2}) p) (\beta_ {1} + \beta_ {2}),
$$

while for $( q , p )$ in region II,

$$
\frac {\partial \Psi}{\partial q} (q, p) = f (1 5 0 + (q + \beta_ {1} p) / 2) / 2
$$

$$
\frac {\partial \Psi}{\partial q} (q, p) = f (1 5 0 + (q + \beta_ {1} p) / 2) \beta_ {1} / 2.
$$

If we are dispatched at $( q , p )$ , our total revenue is

$$
\begin{array}{l} R (q, p) = q p _ {1} + q _ {f} \left(p _ {3} - p _ {1}\right) \\ = \left\{ \begin{array}{l l} q p & \text { in   region   I } \\ q p + q _ {f} \left(q + \left(\beta_ {1} + 2 \beta_ {2}\right) p - 3 0 0\right) / 2 \beta_ {2} & \text { in   region   II } \end{array} \right. \end{array}
$$

![](/api/attachments/M4EDFF7V/fulltext/images/82b5632f81af9a4e472b425d0c7ff795b5d88dba9e0c8dd6e48fb91a0a6c5d98.jpg)  
Fig. 7. Optimum offer curves for varying $q _ { f } .$

According to Ref. [2], the optimal offer curve must at each point either be horizontal or vertical, or satisfy the equation $Z { = } 0$ , where

$$
\begin{array}{l} Z = \frac {\partial R}{\partial q} \frac {\partial \Psi}{\partial p} - \frac {\partial R}{\partial p} \frac {\partial \Psi}{\partial q} \\ = \left\{ \begin{array}{l l} ((\beta_ {1} + \beta_ {2}) p - q) f (q + (\beta_ {1} + \beta_ {2}) p) & \text { in   region   I } \\ (\beta_ {1} p - q - q _ {f}) \frac {1}{2} f (1 5 0 + (q + \beta_ {1} p) / 2) & \text { in   region   II } \end{array} \right. \end{array}
$$

The $Z { = } 0$ contour is thus $q { = } ( \beta _ { 1 } { + } \beta _ { 2 } ) p$ in region I and $q { = } \beta _ { 1 } p { - } q _ { f }$ in region II, independently of f. From this, it is not hard to see that the best offer curve must resemble the upper curve in Fig. 7. (The value of $q _ { T }$ will in general depend on f).

For comparison, the lower curve in Fig. 7 shows the offer curve we would submit if we did not own the FTR. Ownership of the FTR thus requires more aggressive strategic offering (with respect to both quantity and price) on our part. As a result of this, the line capacity constraint between nodes 2 and 3 is more likely to come into play, and the expected price $p _ { 3 }$ paid by consumers at node 3 is increased.

## 4. Allocating rights by auction

In this section, we consider the design of the auction mechanism by which the ISO creates FTRs and distributes them to market participants.

Note that there are many more possible types of FTRs (e.g. a balanced FTR between any pair of nodes in the network) than are likely to be needed in practice. The ISO must thus make two decisions: (i) which FTRs should exist; and (ii) who should own them. In an auction framework, both decisions are driven by the bids received, subject only to the requirement that all the FTRs created must be simultaneously feasible in the sense discussed in Section 2.

This line of thinking leads directly to an auction of the following kind. Suppose A bids are received, with bid $\alpha \ ( \alpha { = } 1 , . . . . , A )$ offering $F _ { \alpha }$ dollars in exchange for an FTR contract described by a vector $h ( \alpha )$ (i.e. one which pays $\textstyle \sum _ { i } \pi _ { i } h _ { i } ( \alpha ) )$ Then the auction is cleared by accepting a fraction $r _ { \alpha }$ of each bid a in such a way as to maximize the resulting revenue to the ISO. Formally, the auctioneer solves:

$$
\begin{array}{l l l l l} A P: & \text { maximize } & \sum_ {\alpha} F _ {\alpha} r _ {\alpha} \\ & \text { subject   to } & g _ {i} (y) - z _ {i} & = & \sum_ {\alpha} r _ {\alpha} h _ {i} (\alpha), \quad i = 1, 2, \ldots , n \\ & & r _ {\alpha} & \in & [ 0, 1 ] \qquad \qquad \qquad \alpha = 1, 2, \ldots , A \\ & & z _ {i} & \geq & 0, \qquad \qquad \qquad i = 1, 2, \ldots , n \\ & & y & \in & U, \end{array}
$$

where $g _ { i } , \ U$ are as in Section 2. The prices actually paid by the bidders are determined from the dual problem. This type of auction is discussed further by Hogan in Ref. [6].

However, this auction design may fail to capture all of the revenue opportunities available to the ISO when there are bidders who have market power in the electricity market. To see why, we must consider what an FTR is worth to such a bidder.

Suppose a large generator is such that when it chooses an offer curve T, the resulting nodal price at node i has expectation p¯ <sub>i</sub>(T). (Cf. the examples in the previous section). To this generator, the value of a fraction r of an FTR that pays $\sum _ { i } h _ { i } \pi _ { i }$ is

$$
F (r) = \max _ {T} \left(\rho (T) + r \sum_ {i} h _ {i} \bar {\pi} _ {i} (T)\right) - \max _ {T} \rho (T),
$$

where $\rho ( T )$ represents the value generated by all activities other than this fraction of this FTR (including energy trading, other FTRs, and perhaps a fixed further fraction $r _ { 0 }$ of this same FTR). If $\operatorname* { m a x } _ { T } \rho ( T )$ is attained for $T { = } T ^ { * }$ , then we have

$$
\begin{array}{l} F (r) \geq \rho (T ^ {*}) + r \sum_ {i} h _ {i} \bar {\pi} _ {i} (T ^ {*}) - \rho (T ^ {*}) \\ = r \sum_ {i} h _ {i} \bar {\pi} _ {i} (T ^ {*}) \end{array}
$$

From this it follows that $F$ is a convex function, and linear only when the $\pi _ { i }$ does not depend on T.

As an example, consider the large upstream generator in (the numerical specialisation of) Example 1. If this generator owns $q _ { f }$ megawatts of the FTR over the line, then its expected total revenue may be found from Eq. (1), and plotted in Fig. 8.

Note that the derivative of this function is at every point equal to the <sup>b</sup>investment<sup>Q</sup> value of a unit FTR, i.e. $E [ \pi _ { 2 } ( T ^ { * } ) - \pi _ { 1 } ( T ^ { * } ) ]$ , where $T ^ { * }$ is the optimal offer curve for the given value of $q _ { f } .$

The market for FTRs in the presence of such a strategic bidder is thus not dissimilar to the market for a public company’s shares in the presence of a strategic buyer to whom a large block of shares would have an enhanced value associated with control. To the strategic bidder, a small additional holding of FTRs has the same value as it would to anyone else, but a higher price can be paid for a large block. (One difference is that a shareholder’s control over a public company increases discontinuously at a shareholding level of 50%, while the value enhancement possible with FTRs increases continuously with the quantity held). This analogy was first made by Joskow and Tirole in Ref. [8].

In a simple auction of the type discussed above, the strategic bidder faces a difficult problem. If it bids $F _ { \alpha }$ for an FTR h(a), the bid will be scaled back by some factor $r _ { \alpha } .$ —which is unknown at the time the bid is made—so that the actual FTR purchased is $r _ { \alpha } h ( \mathbf { \Sigma } _ { \alpha } )$ , for an amount $r _ { \alpha } F _ { \alpha }$ The bidder will therefore not want to set $F _ { \alpha }$ to be the full amount that it perceives h(a) to be worth, since this is likely to result in it overpaying for the FTR eventually received. This will be especially so in a complex network, where the bid must compete against other participants’ bids for FTRs between many other pairs of nodes in order to maintain simultaneous feasibility overall, and the value of $r _ { \alpha }$ is thus especially uncertain in advance.

![](/api/attachments/M4EDFF7V/fulltext/images/63d6aaf9114769f19844c3de8ce2d341860ca3b513ba2c1303fe9ea9dd427af6.jpg)  
Fig. 8. Expected revenue from owning $q _ { f }$ MW of FTR.

A possible modification of the auction which would accommodate the strategic bidders (and therefore enhance the ISO’s likely revenue) would be to allow some bids to be conditional on others being fully accepted. A strategic bidder could then offer a higher price for further FTRs bought after a significant holding had already been acquired. However, this would make the auctioneer’s problem more complex—instead of a linear program, it would become a mixed integer linear program.

A more fundamental question here is whether it is appropriate to design the auction to accommodate strategic bidders—thereby maximizing the auction revenue—at all. In this context, one must re-examine the results of the previous section, in which it is shown that the effects of awarding large blocks of FTRs to price makers can have very mixed results. Another important question is whether it is even possible to thwart the strategic bidders through auction design. If, for example, there is a secondary market for FTRs, strategic bidders might still be able get the FTRs they want during post auction trading. The additional amount that strategic bidders are prepared to pay for FTRs could then be captured by intermediaries, instead of by the ISO.

## 5. Conclusion

As instruments for hedging nodal price differences, FTRs provide a valuable tool for market participants to use. This paper has illuminated some of the incentives that these instruments provide to market participants to enhance their profit. Like contracts for differences, FTRs may mitigate the market power of those holding them. However, they may also enhance this market power (just as a generator buying a contract for differences will have an incentive to set high spot prices). The increasing marginal value of FTRs poses problems for the auction mechanism, which implicitly treats this as constant for any level of the FTR held. To maximize the auction revenue, the auction might need to be run as a mixed integer program.

## Acknowledgement

This work has been supported by the New Zealand Public Good Science Fund under Contract UOAX0203.

## References

[1] E.J. Anderson, A.B. Philpott, Using supply functions for offering generation into an electricity market, Oper. Res. 50 (3) (2002) 477–489.

[2] E.J. Anderson, A.B. Philpott, Optimal offer construction in electricity markets, Math. Oper. Res. 27 (1) (2002) 82 – 100.

[3] J.B. Bushnell, S.E. Stoft, Electricity grid investment under a contract network regime, J. Regul. Econ. 10 (1996) 61– 79.

[4] B.F. Hobbs, C.B. Metzler, J.S. Pang, Strategic gaming analysis for electric power systems: an MPEC approach, IEEE Power Eng. Trans. 15 (2000) 638– 645.

[5] W.W. Hogan, Contract networks for electric power transmission, J. Regul. Econ. 4 (3) (1992) 211 – 242.

[6] W.W. Hogan. A concurrent auction model for transmission congestion contracts, J.F. Kennedy School of Government Technical Report (1997).

[7] W.W. Hogan. Flowgate rights and wrongs, J. F. Kennedy School of Government Technical Report (2000).

[8] P.L. Joskow, J. Tirole, Transmission rights and market power on electric power networks, Rand J. Econ. 31 (3) (2000) 450 – 487.

[9] A.B. Philpott, G. Pritchard, Financial transmission rights in convex pool markets, Oper. Res. Lett. 32 (2) (2004) 109 – 113.

Geoffrey Pritchard is a Senior Lecturer in the Department of Statistics at the University of Auckland in New Zealand. He obtained his PhD from the University of Wisconsin at Madison in 1995, and has been on the faculty of the University of Auckland since 1997. His research interests include stochastic processes and optimization, and their applications, with particular emphasis on modeling in electricity markets.

Andrew B. Philpott is a Professor in the Department of Engineering Science at the University of Auckland in New Zealand. His research interests include optimization models for application in electricity markets, focusing particularly on optimal behaviour for generators; stochastic programming; and yacht optimization models.
