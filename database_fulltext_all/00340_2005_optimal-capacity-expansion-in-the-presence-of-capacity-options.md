---
otero_id: 340
otero_key: "2BEWTDBJ"
title: "Optimal capacity expansion in the presence of capacity options"
authors: "D.J. Wu; Paul R. Kleindorfer; Yanjun Sun"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.09.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Optimal capacity expansion in the presence of capacity options

D.J. Wu<sup>a,\*</sup>, Paul R. Kleindorfer<sup>b</sup>, Yanjun Sun<sup>c</sup>

<sup>a</sup>College of Management, Georgia Institute of Technology, Atlanta, GA 30332, United States <sup>b</sup>The Wharton School, University of Pennsylvania, Philadelphia, PA 19104, United States <sup>c</sup>School of Economics and Management, Tsinghua University, Beijing, 10084, PRC

Available online 28 October 2004

## Abstract

This paper studies optimal long-term electric power capacity strategies with capacity options. Gencos (Generation Companies) can sign contracts with Discos (Distribution Companies), where such contracts take the form of capacity options that may or may not be executed by Discos at some prespecified maturation date. Capacity not offered in the options market, or for which options by Discos are not executed, can then be offered in the spot market. The purpose of this paper is to derive the optimal capacities for Gencos in the long-run given full knowledge of the short-term equilibria as characterized by previous literature. We determine the best response strategies for each Genco in the game derived from the short-term outcome resulting from capacity decisions. We then characterize the long-run equilibrium and derive an efficient algorithm to compute it when it exists. This also allows us important insights into the nature of technologies that can survive in the long-run. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

## 1. Introduction

Consider an electricity market in which Discos can reserve capacity through options obtained from individual Gencos, and output on the day can be either obtained through executing such options or in a spot market. Previous work has characterized the necessary and sufficient conditions for the existence and structure of short-term equilibrium. By <sup>b</sup>short term,<sup>Q</sup> we mean the equilibrium to a Bertrand–Nash pricing game among Gencos, perfectly informed about Discos’ demands and with fixed capacity for every Genco (e.g., [12]).<sup>1</sup> In this paper, we extend these short-term equilibrium results to determine optimal capacity strategies and study the equilibrium issues related to these strategies. To make this paper manageable in size, we will rely entirely on the framework and notation of Wu and Kleindorfer [12].

Linking capacity expansion games with short-term pricing has been an important area of study in industrial organization with major contributions coming in [3,8], showing that precommitments of capacity followed by Bertrand competition can give rise to a range of outcomes between Cournot and competitive outcomes. This paper enriches these same results in the context of the more complicated arena of interest here in which competition occurs in an integrated contract-spot market setting. The results obtained reflect the interaction of these two markets.

It is important to note that the options of interest here include not only standard energy options, which imply the right but not the obligation to buy (call) or sell (put) output at a specified price and with a specified delivery point, but also exotic options [6] and other derivatives [1], such as the weather derivatives recently introduced in the energy sector [10]. For a review of options thinking in capital-intensive industries such as energy, see Ref. [7]. In our model, forwards are included as a special case where the execution price of the option is zero, and all fees are collected as part of the reservation price [12]. The use of options in electric power has grown considerably as the trading market has matured [1]. Besides supporting wholesale energy transactions, such options have also been discussed as a key element to support the markets and ISO (Independent System Operator) regulation of operating reserves and ancillary services. In this latter context, a Disco can demonstrate to the ISO that it has arranged for appropriate operating reserves in, say, the month-ahead market to assure its ability to meet specific reserve margins given its historical loads. These options can then be called either on the day or just prior to it, depending on ISO regulations concerning the temporal resolution of

A further issue of some interest in the present context is the characterization of efficient technology mixes in long-run equilibrium, e.g., Refs. [2,5]. The conditions characterizing the efficient mix are extended here to account for the integration of the two markets of interest. The usual cost conditions (indicating tradeoffs between unit capacity costs and unit variable costs across different technologies) need to be extended in the present context to account for the interaction of each technology with the characteristics (especially the volatility) of the spot market.

We proceed as follows. In Section 2, we first set up the base model and review what has been established in the short-term equilibrium. In Section 3, building on these short-term results, we structure the long-term capacity game among Gencos. This game is determined by the expected profits for each Genco in the short-term game of participating in the combined contract-spot markets. These profits, of course, depend on the capacity decisions made by Gencos prior to the play of this game. We determine best response and equilibrium strategies for this game and show some properties of the price and capacities that result in equilibrium. We then consider the characteristics of efficient technology mixes in the long-run equilibrium. Finally, we further characterize the longrun market segmentation for Gencos. In Section 4, we give some numerical examples to illustrate key insights derived in this paper. Section 5 concludes the paper, with directions for future research.

## 2. Basic model and literature review

There are I Gencos and only one (aggregate) Disco interacting in a wholesale ISO-controlled market, selling and buying electric power. Let N be the set of all Gencos who are available to participate both in the contract and the spot market (of course, there may be many Gencos who are outside of this set and who only participate in the spot market). The heterogeneous technologies of the Gencos are characterized by the triple (b, b, K), where b is Genco’s short-run marginal cost of providing a unit, b is Genco’s unit capacity cost per period, and K is Genco’s total available capacity. In the short-run, these technologies are assumed to be fixed. Here, we are interested in what happens in the long-run, where these could well be strategic decision variables with technology investment, i.e., when capacity K is viable. Let $\scriptstyle b = ( b _ { 1 } , \ldots ,$ $b _ { I } ) , \ \beta { = } ( \beta _ { 1 } , . . . , \beta _ { I } )$ and, $K { = } ( K _ { 1 } , . . . , K _ { I } )$

The decision variables to the (expected-profit-maximizing) Gencos are the optimal contract $[ s , g ]$ to offer to the Disco, where s is the reservation cost per unit of capacity, and g is the execution cost per unit of output.

The decision variables for the (expected-utilitymaximizing) Discos are how much to contract $\boldsymbol { Q }$ at period 1 with the Gencos and, at a later period 2, how much to execute from the contract $q { \leq } Q$ and how much to procure from the spot market x. The Disco’s total demand on the day (at period 2) is assumed to be common knowledge, where $P _ { \mathrm { ~ s ~ } }$ is spot market price. Buyer’s willingness-to-pay (WTP) $U ( \cdot )$ is assumed to be strictly concave and increasing so that $U ^ { \prime } ( \cdot ) { > } 0$ $U ^ { \prime \prime } ( \cdot ) { < } 0$ . The assumed decreasing marginal utility in consumption $( U ^ { \prime \prime } ( \cdot ) { < } 0 )$ simply means that the Buyer’s normal demand curve $D _ { \mathrm { s } } ( \cdot )$ is downward sloping, where $D _ { \mathrm { s } } ( \cdot ) { = } U ^ { \prime - 1 } ( \cdot )$

The spot market price $P _ { \mathrm { ~ s ~ } }$ is uncertain; before it is revealed in period $^ { 2 , }$ it is assumed to be exogenous; that is, an open spot market, reflecting a global commodity market where no particular Genco has the market power to influence spot price. The cumulative distribution function of the spot price is $F ( P _ { \mathrm { s } } )$ with a density function of $f ( P _ { \mathrm { s } } )$ and a mean value of $\mu ;$ these are also assumed to be common knowledge.

The objective of the Disco is to maximize a given utility or profit function subject to available option contracts. The objective of each Genco is to maximize own expected profit, jointly obtained from both the contract market and the spot market.

Define, G(v), the effective price function as $G ( \nu ) { = } E$ {min( $P _ { \mathrm { s } } , \nu ) \}$ }. Denote $G ^ { - 1 }$ as the inverse function of G. Under the above setting, Wu and Kleindorfer [12] show that the structure of the optimal portfolio of the Disco follows a single index $s { + } E$ min $\{ P _ { \mathrm { s } } , g \} { = } s { + } G ( g )$ . The Genco’s optimal strategy is to bid its unit production cost $( g { = } b )$ by maximizing its profit via the optional subscription charge (s) that is proportional to its opportunity cost and inversely proportional to demand elasticity.

Let $D ( \cdot ) { = } D _ { \mathrm { s } } ( G ^ { - 1 } ( \cdot ) )$ . Denote $D ^ { - 1 }$ as the inverse function of $D ( \cdot )$ . Assume Seller k participates in the equilibrium bid $p _ { k }$ as a final unit provider; assume also all other bidders keep their bids constant. Then, Seller k’s own profit function for increases in price $p _ { k }$ is given by $\bar { \mathrm { E } \pi _ { k } ( p _ { k } ) } \mathrm { = } [ p _ { k } - c _ { k } ] Q _ { k } ( p _ { k } ) \mathrm { = } [ p _ { k } - c _ { k } ] [ \bar { D ( p _ { k } ) } - \bar { \sum _ { i = 1 } ^ { k - 1 } }$ $K _ { i } ]$ , where $c _ { k }$ is defined below. Assuming pseudoconcavavity of $[ p _ { k } { - } c _ { k } ] D ( p _ { k } )$ as in standard economics $\left( \mathrm { e . g . , [ 4 ] } \right)$ , then $\mathrm { E } \pi _ { k } ( p _ { k } )$ is also pseudoconcave.

Previous literature has characterized the short-term equilibrium as the following. We distinguish results for a singleton and nonsingleton equilibrium set. Define $c _ { i } { = } s _ { i } { + } G ( b _ { i } )$ , where $s _ { i } – E \{ m _ { i } ( P _ { \mathrm { s } } ) ( P _ { \mathrm { s } } \ – b _ { i } ) ^ { + } \}$ , and $m _ { i }$ is the last-minute spot market access probability.

Theorem 1. (Wu and Kleindorfer [12]; Bertrand–Nash Equilibrium): Let (K, p, M) be any short-term equilibrium, where $M \subseteq \Xi i s$ the equilibrium set of all Gencos having positive capacity contracts, that $i s ,$ $Q _ { i } ( p ) { > } 0 ,$ , i<sup>a</sup>M and $Q _ { k } ( p ) { = } 0 ,$ $k { \in } E { \mid } M .$ Let $c _ { I } { = } m i n$ $\{ c _ { i } | i { \in } \Xi \}$ so that Genco 1 has the lowest $c _ { i }$ index among all Gencos. $\mathit { I f c } _ { I } { \ge } G ( U ^ { \prime } ( \theta ) )$ , then no Genco will participate in the contract market. Thus, suppose $c _ { I } { < } G ( U ^ { \prime } ( \theta ) )$ . Then, the necessary and sufficient conditions for a short-term equilibrium p to exist are

SC1

$$
p = \left\{ \begin{array}{l l} \max \bigl \{\arg \max _ {v} (v - c _ {1}) D (v), D ^ {- 1} (K _ {1}) \bigr \} & i f | M | = 1, \\ D ^ {- 1} (X (M)) & i f | M | > 1, \end{array} \right.
$$

$$
S C 2 \quad \frac {\partial E \pi_ {k} (p _ {k})}{\partial p _ {k}} \leq 0, i f p _ {k} > p, \forall_ {k} \in M,
$$

$$
S C 3 \quad \forall k \in \Xi \backslash M, p <   c _ {k}.
$$

where |M| means the number of elements in set $M , X ( M ) { = } \Sigma _ { i \in M } K _ { i }$

We note here that all proofs can be found in the Appendix.

## 3. Optimal capacity expansion

The outcome of the short-term options-pricing game in the integrated contract and spot markets leads to the following profit function for any Genco k:

$$
E \pi_ {k} (p, K) = [ p - c _ {k} ] Q _ {k} + [ c _ {k} - \beta_ {k} - G (b _ {k}) ] K _ {k}
$$

Genco $k \mathrm { { s } }$ problem is to choose an optimal capacity $K _ { k } ^ { * }$ to maximize $k \mathrm { { : } }$ long-run expected profit, i.e.,

Lemma 1. Let $p ( K )$ be the short-run equilibrium price and let M(K) be the set of Gencos in the contract–market equilibrium. Assume M(K) is nonsingleton. Then, the best response capacity strategy for each Genco $k { \in } M ( K )$ is

$$
K _ {k} ^ {*} = \max \left\{\frac {p - \beta_ {k} - G (b _ {k})}{p - c _ {k}} X (M), 0 \right\}.\tag{1}
$$

We note that the proof in the Appendix takes the equilibrium set $M ( K )$ as given and determines the best response strategy for every Genco in M(K), assuming that the set $M ( K )$ does not change as K is adjusted. In the long-term equilibrium, where K is adjustable, what is required is that all best capacity responses $K ^ { * }$ given $M ( K ^ { * } )$ , result in a short-run equilibrium $p ^ { * }$ with $p ^ { * } { = } p ( K ^ { * } )$ and $M ^ { * }$ with $M ^ { * } { = } M ( K ^ { * } )$ . Thus, the longrun equilibrium we seek to characterize is defined as follows.

Definition. A long-run nonsingleton contract market equilibrium $( K ^ { * } , ~ p ^ { * } , ~ M ^ { * } )$ is a vector such that $p ^ { * } { = } p ( K ^ { * } )$ and $M ^ { * } { = } M ( K ^ { * } )$ and such that $K _ { k } ^ { * } { > } 0$ for all $k { \in } M ^ { * }$ , where $K _ { k } ^ { * }$ satisfies the best-response condition (1), i.e.,

$$
K _ {k} ^ {*} = \frac {p ^ {*} - \beta_ {k} - G (b _ {k})}{p ^ {*} - c _ {k}} X ^ {*} (M ^ {*})\tag{2}
$$

Definition. A long-run singleton contract market equilibrium $( K _ { 1 } ^ { * } , p ^ { * } , M ^ { * } )$ is a triple such that the following conditions are satisfied: ${ \mathrm { ( i ) } p ^ { * } \mathrm { = a r g m a x } ( p - }$ $\beta _ { 1 } { - } G ( b _ { 1 } ) ) D ( p )$ ; (ii) $K _ { 1 } ^ { * } { = } D ( p ^ { * } )$ ; (iii) $c _ { 1 } { < } \beta _ { 1 } { + } G ( b _ { 1 } ) ;$ $( \mathrm { i v } ) \beta _ { 1 } { + } G ( b _ { 1 } ) { < } p ^ { * } { < } \mathrm { m i } 1$ n{max $\{ c _ { i } , \beta _ { i } { + } G ( b _ { i } ) \} | i { \in } \Xi \backslash \{ 1 \} \}$ Definition. Define $\zeta _ { k }$ as:

$$
\zeta_ {k} = \frac {\partial \left((p - c _ {k}) D (p) \frac {K _ {k}}{X}\right) / \partial K _ {k}}{\partial ((\beta_ {k} + G (b _ {k}) - c _ {k}) K _ {k}) / \partial K _ {k}}\tag{3}
$$

Corollary 1. Let $( K ^ { * } , p ^ { * } , ~ M ^ { * } )$ be a long-run equilibrium solution. Then, $f o r$ any Genco $k { \in } M ^ { * }$ $\zeta _ { k } ^ { * } { = } l ,$ , and this holds whether $M ^ { * }$ is singleton or not.

Corollary 2. For any Genco $k { \in } M ^ { * }$ , whether M\* is singleton or not, $i f \exists K _ { k } ^ { * } > 0 ,$ , then $p ^ { * } { > } \beta _ { k } { + } G ( b _ { k } ) { > } c _ { k }$

It should be noted that the above lemma and corollaries characterize capacity conditions only for the long-term contract market. It may very well be the case that some Gencos build capacity and only participate in the spot market. Corollary 2 says that, for those who participate in the contract market in the long-run, $\beta _ { k } { + } G ( b _ { k } ) { > } c _ { k }$ or equivalently $\beta _ { k } { > } s _ { k }$ . This implies that, in any long-term contract market equilibrium, every Genco (with positive capacity) satisfies $\beta _ { k } { + } m G ( b _ { k } ) { > } m \mu .$ , where $\mu$ is the mean of the spot market price. This is very intuitive. As $\mu$ increases, or access conditions to the spot market improve (m increases), Gencos are less interested in participating in the contract market and more interested in participating in the spot market.

Corollary 3. Let $( K ^ { * } , p ^ { * } , M ^ { * } )$ be a long-run equilibrium solution. Assume $| M ^ { * } | { > } I ,$ , then $p ^ { * }$ must satisfy (in addition to being a short-run equilibrium price corresponding to $K ^ { * } )$

$$
\sum_ {i \in M ^ {*}} \frac {p ^ {*} - \beta_ {i} - G (b _ {i})}{p ^ {*} - c _ {i}} = 1\tag{4}
$$

or equivalently,

$$
\sum_ {i \in M ^ {*}} \frac {\beta_ {i} + G (b _ {i}) - c _ {i}}{p ^ {*} - c _ {i}} = | M ^ {*} | - 1.\tag{5}
$$

Lemma 2. If there exists any equilibrium set $M ( p ^ { * } ) \subseteq \Xi _ { }$ , it must be unique.

Theorem 2. The long-term equilibrium set $M ^ { * } \subseteq \Xi ,$ whether it exists or not, is characterized by the following algorithm. Index Gencos in the order of $\dot { \mathbf { \zeta } } _ { c _ { i } , \mathbf { \zeta } }$ $i . e . , \ c _ { I } { \leq } c _ { 2 } { \leq } . \ . { \leq } c _ { I } . \ M ^ { * } { = } \phi$

(i) $p ^ { * } { = } a r g m a x ( p { - } \beta _ { I } { - } G ( b _ { I } ) ) D ( p )$ . If $c _ { I } { > } \beta _ { I } { + }$ $G ( b _ { I } ) _ { \ l }$ , then exit; else $i f p ^ { * } { \leq } c _ { 2 } ,$ , then $M ^ { * } { = } \langle I \rangle$ exit; else $M ^ { * } { = } \langle I \rangle$ and i=2.

(ii) Loop while $( ( p ^ { * } { > } \beta _ { i } { + } G ( b _ { i } ) )$ and $( \beta _ { i } { + } G ( b _ { i } ) { > }$ $c _ { i } ) )$ begin

$$
M ^ {*} = M ^ {*} \cup \{i \}.
$$

compute $p ^ { * } ( M ^ { * } )$ via (5).

if i<sup>b</sup>I, then $\scriptstyle i = i + l ,$ , else exit.

end.

(iii) $\forall i { \in } M ^ { * } , ~ i f ~ ( ( p ^ { * } { > } c _ { i } )$ and $( c _ { i } { \ge } \beta _ { i } { + } G ( b _ { i } ) ) )$ , then $M ^ { * } { = } \phi .$

(iv) $\forall i { \in } M ^ { * } , i f \in \mathbb { Z } E { \pi } _ { i } ( p _ { i } , K ^ { * } ) / \partial { p _ { i } } { \geq } 0$ and $p _ { i } { > } p ^ { * }$ , then $M ^ { * } { = } \phi$

(v) $\forall i { \in } M ^ { * } , K _ { i } ^ { * }$ can be computed via(2).

The above algorithm generates the equilibrium essentially by testing, in increasing order of $c _ { i } ,$ the compatibility between the short-run pricing equilibrium and the long-run capacity equilibrium at the best-response strategies characterized in Lemma 1. An equilibrium can, of course, fail to exist. As embodied in the above algorithm, this occurs when adding a further Genco k to the contract market, at the longterm capacities implied by the best-response capacity strategies, the short-term equilibrium price drops below the required feasibility index $c _ { k }$ for Genco k. Thus, without Genco k in the contract market, Disco’s demand intensity signals that entry is desirable beyond the current participants in the contract market. But adding k drops the price below that which is sustainable in this market. In the next section, we consider some examples to illustrate these points.

Theorem 3. Assume a long-term equilibrium $( K ^ { * } , p ^ { * }$ M\*) exists. This equilibrium implies a market segmentation of Gencos in the long-run as follows: (i) $\forall k { \in } M ^ { * }$ with $\underline { s } _ { k } { < } \beta _ { k } ,$ , k participates both in the con tract and in the spot market; $( i i ) \quad \forall k { \in } \Xi ^ { } \backslash M ^ { * }$ with $\underline { s } _ { k } { > } \beta _ { k } ,$ k participates only in the spot market; (iii) 8k<sup>a</sup>N\ M\* with $\underline { s } _ { k } { \le } \beta _ { k } ,$ , k participates in neither market, that is, k will be <sup>b</sup>out of business<sup>Q</sup> in the longrun.

Note that, if $k , \ k { + } 1 { \in } \Xi { \backslash } M ^ { * }$ and if $\underline { s } _ { k + 1 } > \beta _ { k } ,$ then $\underline { s } _ { k + 1 } > \beta _ { k + 1 }$ implies $\underline { s } _ { k } { > } \beta _ { k } . ^ { 5 }$ This means that, if k is not in set $M ^ { * }$ (w.r.t. the contract market) but still competes in the spot market, then every other Genco not in set $M ^ { * }$ with lower capacity costs than k will also participate in the spot market alone.

Theorem 3 implies that the index line of $c _ { 1 } { < } c _ { 2 } { < } . . . { < } c _ { I }$ can be used to identify the unique group of Gencos who participate both in the contract and in the spot market, and a further disjoint and unique group of Gencos who only participate in the spot market, and lastly, the remaining unique group of Gencos who will be <sup>b</sup>out of business<sup>Q</sup> in the long-run.

Unsurprisingly, the nature of the spot market (volatility and price level) as well as both variable and capital costs and the access parameter (m) are factors affecting which technologies survive in the long-run. The above results provide the key insights on how these cost and market factors interact strategically to determine which markets will exist in the long-run and which Gencos will be able to survive in each respective market.

## 4. Numerical examples

## 4.1. Numerical example 1

Assume there are five Gencos with technology parameters $( G ( b ) , \beta , K )$ , as shown in Table 1, and the risk factor $m { = } 0 . 5 .$ We can compute (s, c, $\beta \mathrm { + } G ( b ) )$ , as shown in Table 1. Suppose the spot market price follows an exponential distribution, $f ( y ) { = } ( 1 / 3 0 ) e ^ { - y / 3 0 }$ so the mean of the spot market price is $\mu { = } 3 0$ . Then, the effective price function is $G ( x ) { = } { - } 3 0 ( e ^ { - x / 3 0 } { - } 1 )$ , where $0 { \le } x { < } \infty$ , and thus, we have $G ^ { - 1 } ( p ) { = } 3 0 l n ~ \left( 3 0 / ( 3 0 { - } { \mathrm { p } } ) \right)$ , where $0 { \leq } p { < } 3 0 .$ Suppose the WTP function is $U ( z ) { = } 3 0 z ( l n ( 3 0 /$ $z ) { + } 1 )$ , where $0 { < } z { \leq } 3 0$ . It is obvious that this function satisfies Assumption 1 as follows: ${ \cal U } ^ { \prime } ( z ) { = } 3 0 l n ( 3 0 /$ $z ) { \geq } 0$ and $U ^ { \prime \prime } ( z ) { = } { - } 3 0 / { \mathrm { z } } { < } 0 ;$ thus, we have $D _ { \mathrm { { s } } } ( x ) =$ $( U ^ { \prime } ) ^ { - 1 } ( x ) { = } 3 0 e ^ { - x / 3 0 }$ , where $0 { \le } x { < } \infty$ . So the contract market demand function is $D ( p ) { = } D _ { \mathrm { s } } ( G ^ { - 1 } ( p ) ) { = }$ $( U ^ { \prime } ) ^ { - 1 } ( G ^ { - 1 } ( p ) ) { = } 3 0 { - } p$ , where $\scriptstyle p \in [ 0 , 3 0 )$ . It is straightforward to compute that, in the short term, four Gencos, namely, 1, 2, 3, and 4, achieve an equilibrium at a price $\scriptstyle { p = 2 6 }$ . Genco 5 is not in the short-term equilibrium, although 5 has strong incentives to participate as 5 cannot make any money on the spot market due to very high short-run marginal cost $G ( b _ { 5 } ) { = } 3 0$ . Using the above Theorem 2, we can compute that there are only two survivors in the long-run, namely, 1 and 2, with the equilibrium price $p ^ { * } { = } 2 3 . 2 3 6$ . The optimal capacity investments for these two Gencos are $K _ { 1 } ^ { * } { = } 4 . 1 8 0$ and $K _ { 2 } ^ { * } { = } 2 . 5 8 4 .$ Genco 3 and Genco 4 find themselves out of the contract market, and both participate only in the spot market. Genco 5 is <sup>b</sup>out of business<sup>Q</sup> in the long-run and is better off by shutting down all its plants, illustrating Theorem 3.

Summary of parameters and results for Numerical example 1

<table><tr><td> $i$ </td><td> $G(b_{i})$ </td><td> $\beta_{i}$ </td><td> $K_{i}$ </td><td> $s_{i}$ </td><td> $c_{i}$ </td><td> $\beta_{i}+G(b_{i})$ </td><td> $p$ </td><td> $p^{*}$ </td><td> $\pi_{i}$ </td><td> $\pi_{i}^{*}$ </td><td> $K_{i}^{*}$ </td></tr><tr><td>1</td><td>6</td><td>14</td><td>1</td><td>12</td><td>18</td><td>20</td><td>26</td><td>23.2</td><td>6</td><td>13.4</td><td>4.2</td></tr><tr><td>2</td><td>10</td><td>12</td><td>1</td><td>10</td><td>20</td><td>22</td><td>26</td><td>23.2</td><td>4</td><td>3.1</td><td>2.6</td></tr><tr><td>3</td><td>18</td><td>4</td><td>1</td><td>6</td><td>24</td><td>22</td><td>26</td><td>-</td><td>4</td><td>-</td><td>-</td></tr><tr><td>4</td><td>20</td><td>2</td><td>1</td><td>5</td><td>25</td><td>22</td><td>26</td><td>-</td><td>4</td><td>-</td><td>-</td></tr><tr><td>5</td><td>30</td><td>1</td><td>1</td><td>0</td><td>30</td><td>31</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr></table>

m=0.5, l=30, D( p)=30p.

The following example illustrates a case in which the equilibrium does not exist.

## 4.2. Numerical example 2

Assume there are three Gencos in the contract market. The technology parameters and all the other market conditions of Genco 1 and Genco 2 are the same as in Numerical example 1, except that Genco 3’s $G ( b _ { 3 } ) { = } 1 6$ and $\beta _ { 3 } { = } 6 ,$ , as in Table 2. The short-term equilibrium price is 27. However, there is no longterm equilibrium in this example because the longterm contract price formed by Genco 1 and 2, 23.2, is higher than Genco 3’s index $c _ { 3 } { = } 2 3$ at this contract market price $p { = } 2 3 . 2 ,$ , Genco 3 finds participation in the contract market is more profitable than staying in the spot market per unit capacity as $p - ( \beta _ { 3 } + G ( b _ { 3 } ) ) =$ $2 3 . 2 - 2 2 = 1 . 2 > \underline { { { s } } } _ { 3 } - \beta _ { 3 } = 7 - 6 = 1$ . However, if Genco 3 does participate in the contract market, the contract market price drops to 22.2, this makes participation undesirable as net profit per unit capacity is less than staying in the spot market, that is, $p - ( \beta _ { 3 } + G ( b _ { 3 } ) ) =$ $2 2 . 2 - 2 2 = 0 . 2 < s _ { 3 } - \beta _ { 3 } = 7 - 6 = 1$ . This is an example that shows there need be no long-term equilibrium in the contract market.

## 4.3. Numerical example 3

It is interesting now to conduct a game–theoretic analysis of the investment game in Numerical example 1. Assume Gencos 3, 4, and 5 do not invest, and their capacity will be fixed throughout, that is, $K _ { 3 } { = } K _ { 4 } { = }$ $K _ { 5 } { = } 1$ . Genco 1 and Genco 2 each has to decide whether to invest or not. Genco 3, 4, and 5 decide whether or not to participate in the contract market based on the resulting contract equilibrium price due to the capacity adjustment of Gencos 1 and 2.

Table 2  
Summary of parameters and results for Numerical example 2

<table><tr><td> $i$ </td><td> $G(b_{i})$ </td><td> $\beta_{i}$ </td><td> $K_{i}$ </td><td> $\underline{s_{i}}$ </td><td> $c_{i}$ </td><td> $\beta_{i}+G(b_{i})$ </td><td> $p$ </td><td> $K_{i}^{*}$ </td><td> $p,$ without Genco 3</td><td> $p,$ with Genco 3</td></tr><tr><td>1</td><td>6</td><td>14</td><td>1</td><td>12</td><td>18</td><td>20</td><td>27</td><td>4.2</td><td>23.2</td><td>22.2</td></tr><tr><td>2</td><td>10</td><td>12</td><td>1</td><td>10</td><td>20</td><td>22</td><td>27</td><td>2.6</td><td>23.2</td><td>22.2</td></tr><tr><td>3</td><td>16</td><td>6</td><td>1</td><td>7</td><td>23</td><td>22</td><td>27</td><td>1</td><td>23.2</td><td>22.2</td></tr></table>

m=0.5, l=30, D( p)=30p.

Table 3  
A two-Genco investment game

<table><tr><td></td><td> $K_{2}$  (don’t invest)</td><td> $K_{2}^{*}$  (invest)</td></tr><tr><td> $K_{1}$  (don’t invest)</td><td>6, 4</td><td>5, 9</td></tr><tr><td> $K_{1}^{*}$  (invest)</td><td>16, 2</td><td>13.4, 3.1</td></tr></table>

In the above Numerical example 1, we computed the profits for both parties in short-term equilibrium $( K _ { 1 } , K _ { 2 } )$ and in long-term equilibrium $( K _ { 1 } ^ { * } , K _ { 2 } ^ { * } )$ . Now, we compute the profits of both parties when only one Genco is using the best response strategy, $( K _ { 1 } ^ { * } , K _ { 2 } )$ and $( K _ { 1 } , K _ { 2 } ^ { * } )$ . When Genco 1 expands its capacity to $K _ { 1 } ^ { * } { = } 4$ but Genco 2 does not, $p { = } 2 4 .$ , so Genco 4 is out, Genco 1’s profit increases, while Genco ${ 2 \mathrm { { } s } }$ profit decreases. Genco 3 is indifferent between participating in the contract market or in the spot market. On the other hand, when Genco 2 raises his capacity level to $K _ { 2 } ^ { * } { = } 3$ while Genco 1 does not, $p { = } 2 5 ,$ , Genco 4 is indifferent between participating in the contract market and in the spot market. However, Genco 3 now finds the contract market more profitable than the spot market alone. Genco $2 \mathrm { { : } } \mathrm { { s } }$ profit increases while Genco 1’s profit decreases due to Genco 2’s capacity expansion. Table 3 contains the payoff matrix for Gencos 1 and 2. Clearly, the Nash equilibrium of this investment game is that both Gencos 1 and 2 choose to invest, as characterized in our Theorem 2.

## 5. Future research

The above characterizes long-run equilibrium in the usual <sup>b</sup>putty-putty<sup>Q</sup> world of completely flexible capacity investments or investments at least which could be evaluated and changed to any level before the fact. In many markets, capacity is a <sup>b</sup>putty-clay<sup>Q</sup> investment, i.e., irreversible. In such markets, it would be interesting to characterize the long-run equilibria that would result if the only capacity choice options were complete withdrawal from the market or expansion of capacity.

## Acknowledgement

An earlier version of this paper appeared in the Proceedings of the Thirty-Fifth Annual Hawaii International Conference on Systems Sciences (HICSS-35) in January 2002, Big Island, HI. For helpful discussions and comments on previous drafts, we thank Tim Mount, Shmuel Oren, John Ning, and other participants for the mini-track of electricity markets and regulation (complex systems track) of HICSS-35.

## Appendix

Proof of Lemma 1

Proof. Take any capacity vector K and let $M ( K )$ be the short-term equilibrium set (assuming it exists and is nonsingleton). Substituting $Q _ { k } { = } D ( p ) ( K _ { k } / X ( M ) )$ into the profit function, we obtain the following expression for the profit function for Genco $k { \in } M ( K ) .$

$$
\begin{array}{c} \operatorname{E} \pi_ {k} (p, K) = (p - c _ {k}) D (p) \frac {K _ {k}}{X (M)} \\ + (c _ {k} - \beta_ {k} - G (b _ {k})) K _ {k}. \end{array}
$$

The FOC condition for maximizing $\mathrm { E } \pi _ { k } ( p , ~ K )$ gives

$$
K _ {k} ^ {*} = X (M) - \left(X (M)\right) ^ {2} \frac {\beta_ {k} + G \left(b _ {k}\right) - c _ {k}}{\left(p - c _ {k}\right) D (p)}.
$$

From Wu and Kleindorfer [12], we know that a necessary condition (SC1) in equilibrium is that $D ( p ) { = } X ( M )$ . This, coupled with the above FOC, results in the identity (1). It is straightforward to check that the Genco’s profit function w.r.t. $K _ { k }$ is concave, as we see from the SOC

$$
- 2 (p - c _ {k}) D (p) \frac {X (M) - K _ {k}}{X (M) ^ {3}} <   0.
$$

Given this concavity, if the first term in (1) is negative, then the optimal capacity choice is $K _ { k } ^ { * } { = } 0$ Hence, the above solution is indeed optimal. 5

Proof of Corollary 1

Proof. (a) First, we show the claim is true in the singleton case when $| M ^ { * } | { = } 1$ . Since $p ^ { * } { = } { \mathrm { a r g m a x } } ( p -$ $\beta _ { 1 } { - } G ( b _ { 1 } ) ) D ( p )$ , we have the FOC

$$
\left(p ^ {*} - \beta_ {1} - G (b _ {1})\right) \frac {\partial D}{\partial K _ {1}} D = 0,
$$

as $p ^ { * } \mathrm { = } \mathrm { D } ^ { - 1 } ( K _ { 1 } )$ , we have

$$
\frac {D}{\partial D / \partial K _ {1}} = \beta_ {1} + G (b _ {1}) - p ^ {*} = \beta_ {1} + G (b _ {1}) - D ^ {- 1}.\tag{6}
$$

Thus,

$$
\begin{array}{l} \zeta_ {1} = \frac {\partial ((p ^ {*} - c _ {1}) K _ {1}) / \partial K _ {1}}{\partial ((\beta_ {1} + G (b _ {1}) - c _ {1}) K _ {1}) / \partial K _ {1}} \\ = \frac {\partial ((D ^ {- 1} (K _ {1}) - c _ {1}) K _ {1}) / \partial K _ {1})}{\partial ((\beta_ {1} + G (b _ {1}) - c _ {1}) K _ {1}) / \partial K _ {1}} \\ = \frac {D ^ {- 1} - c _ {1} + \frac {\partial D ^ {- 1}}{\partial K _ {1}} K _ {1}}{\beta_ {1} + G (b _ {1}) - c _ {1}} = \frac {D ^ {- 1} - c _ {1} + \frac {\partial D ^ {- 1}}{\partial K _ {1}} D}{\beta_ {1} + G (b _ {1}) - c _ {1}}. \end{array}\tag{7}
$$

As $\begin{array} { r } { \frac { \partial D ^ { - 1 } } { \partial K _ { 1 } } \frac { \partial D } { \partial K _ { 1 } } = 1 } \end{array}$ , (7) can be rewritten as

$$
\zeta_ {1} = \frac {D ^ {- 1} - c _ {1} + \frac {D}{\partial D / \partial K _ {1}}}{\beta_ {1} + G (b _ {1}) - c _ {1}}.\tag{8}
$$

Substitute (6) into (8), and we get

$$
\zeta_ {1} ^ {*} = \frac {D ^ {- 1} - c _ {1} + \beta_ {1} + G (b _ {1}) - D ^ {- 1}}{\beta_ {1} + G (b _ {1}) - c _ {1}} = 1.
$$

(b) Second, we show the claim holds when $| M ^ { * } | { > } 1$ We can write $\zeta _ { \mathrm { k } }$ for each supplier $k { \in } M ^ { * }$ as:

$$
\zeta_ {k} = \frac {\partial \left((p ^ {*} - c _ {k}) D (p) \frac {K _ {k}}{X}\right) / \partial K _ {k}}{\partial ((\beta_ {k} + G (b _ {k}) - c _ {k}) K _ {k}) \partial / K _ {k}}
$$

$$
= \frac {(p ^ {*} - c _ {k}) D (p ^ {*}) \frac {X - K _ {k}}{X ^ {2}}}{\beta_ {k} + G (b _ {k}) - c _ {k}}.
$$

The first equality is the definition of $\zeta _ { k }$ . The second equality is simply the result of taking derivatives w.r.t.

$\begin{array} { r l } & { \frac { K _ { \ast k \cdot } \mathrm { ~  ~ A s ~ } _ { \mathrm { ~ a ~ } } } { p ^ { \ast } - \beta _ { k } - G ( b _ { k } ) } } \\ & { \frac { p ^ { \ast } - c _ { k } } { \mathrm { ~  ~ a b o v e ~ a s ~ } } } \end{array}$ t equilibrium $D ( p ^ { * } ) { = } X ^ { * }$ and $\begin{array} { r } { \frac { K _ { k } ^ { * } } { X ^ { * } } = } \end{array}$ (from Lemma 1), we can rewrite the

$$
\begin{array}{l} \zeta_ {k} ^ {*} = \frac {(p ^ {*} - c _ {k}) \left(1 - \frac {K _ {k} ^ {*}}{X ^ {*}}\right)}{\beta_ {k} + G (b _ {k}) - c _ {k}} \\ = \frac {(p ^ {*} - c _ {k}) \left(1 - \frac {p ^ {*} - \beta_ {k} - G (b _ {k})}{p ^ {*} - c _ {k}}\right)}{\beta_ {k} + G (b _ {k}) - c _ {k}} \\ = \frac {(p ^ {*} - c _ {k}) \frac {\beta_ {k} + G (b _ {k}) - c _ {k}}{p ^ {*} - c _ {k}}}{\beta_ {k} + G (b _ {k}) - c _ {k}} = 1. \end{array}
$$

Proof of Corollary 2

Proof. This is a direct consequence of Lemma 1 and the definition of singleton contract market equilibrium. 5

Proof of Corollary 3

Proof. Summing over $M ^ { * }$ on both sides of (2) results in (4). It is straightforward to get (5) from (4). 5

Proof of Lemma 2

Proof. It is trivial for the case when $| M ^ { * } | { = } 1$ . Suppose $| M ^ { * } | { > } 1$ . We prove this in two steps: (a) Given any set $M ^ { * } \subseteq E , \ p ^ { * }$ is unique; then we show (b) that $M ^ { \ast } ( p ^ { \ast } ) \subseteq \Xi$ is unique.

First, we prove (a) is true. Take any subset of $M ^ { * } \subseteq \Xi$ . Assume (a) is not true, that is, there are at least two pricing equilibria $p _ { 1 } ^ { * }$ and $p _ { 2 } ^ { * }$ corresponding to M\* satisfying (4) or (5). W.l.o.g. assume that $p _ { 2 } ^ { * } { > } p _ { 1 } ^ { * } { > } \mathrm { m a x } \left\{ c _ { i } | i { \in } M ^ { * } \right\}$ . From (5) of Corollary 3, we know that

$$
\sum_ {i \in M ^ {*}} \frac {\beta_ {i} + G (b _ {i}) - c _ {i}}{p _ {1} ^ {*} - c _ {i}} = | M ^ {*} | - 1.
$$

$$
\sum_ {i \in M ^ {*}} \frac {\beta_ {i} + G (b _ {i}) - c _ {i}}{p _ {2} ^ {*} - c _ {i}} = | M ^ {*} | - 1.\tag{9}
$$

However, inasmuch as $\forall i \in M ^ { * } , p _ { 2 } ^ { * } > p _ { 1 } ^ { * } >$ max $\{ c _ { i } | i \in M ^ { * } \}$ by assumption and $\beta _ { i } { + } G ( b _ { i } ) { - } c _ { i } { > } 0$ by Corollary 2, we have

$$
\sum_ {i \in M ^ {*}} \frac {\beta_ {i} + G (b _ {i}) - c _ {i}}{p _ {1} ^ {*} - c _ {i}} > \sum_ {i \in M ^ {*}} \frac {\beta_ {i} + G (b _ {i}) - c _ {i}}{p _ {2} ^ {*} - c _ {i}} = | M ^ {*} | - 1.
$$

This contradicts the assumption that $p _ { 1 } ^ { * }$ is an equilibrium inasmuch as (9) is violated. Thus, we must have ${ p } _ { 1 } ^ { * } { = } { p } _ { 2 } ^ { * }$ , as asserted in claim (a).

Second, we show (b) is true. First, we note that, from Wu and Kleindorfer [12], for any equilibrium set (short-run or long-run) $M ^ { * } , \mathrm { i f } j { \in } M ^ { * }$ and $c _ { i } { \leq } c _ { j } .$ , then $i { \in } M ^ { * } ,$ , so that any equilibrium set for the long-term contract market consists of Gencos with contiguous indices $c _ { i } .$ . Now, assume there are two equilibrium sets $M _ { 1 } ^ { * } ~ = \{ 1 , . . . , ~ l \}$ and $M _ { 2 } { ^ * } { = } \{ 1 { , } { \ldots } , l , \ l { + } 1 { , } { \ldots } n \}$ with respective equilibrium prices $p _ { 1 } ^ { * } , \ p _ { 2 } ^ { * }$ . Moreover, ${ \boldsymbol { p } } _ { 1 } ^ { * } { \le } { \boldsymbol { c } } _ { l + 1 }$ because otherwise l+1 would have an incentive to participate in the contract market and $\boldsymbol { M } _ { 1 } ^ { * }$ would not be an equilibrium set. From (5) of Corollary 3,

$$
\sum_ {i \in M _ {1} ^ {*}} \frac {\beta_ {i} + G (b _ {i}) - c _ {i}}{p _ {1} ^ {*} - c _ {i}} = | M _ {1} ^ {*} | - 1;\tag{10}
$$

$$
\sum_ {k \in M _ {2} ^ {*}} \frac {\beta_ {k} + G (b _ {k}) - c _ {k}}{p _ {2} ^ {*} - c _ {k}} = | M _ {2} ^ {*} | - 1.\tag{11}
$$

Subtract (11) from (10) and rearrange terms, we get

$$
\begin{array}{l} \sum_ {i \in M _ {1} ^ {*}} (\beta_ {i} + G (b _ {i}) - c _ {i}) \frac {p _ {1} ^ {*} - p _ {2} ^ {*}}{(p _ {1} ^ {*} - c _ {i}) (p _ {2} ^ {*} - c _ {i})} \\ = | M _ {2} ^ {*} | - | M _ {1} ^ {*} | - \sum_ {k \in M _ {2} ^ {*} \setminus M _ {1} ^ {*}} \frac {\beta_ {k} + G (b _ {k}) - c _ {k}}{p _ {2} ^ {*} - c _ {k}}. \end{array}\tag{12}
$$

Since from Corollary 1, we know that $\forall k { \in } M _ { 2 } ^ { * } \backslash M _ { 1 } ^ { * }$ $p _ { 2 } ^ { * } > \beta _ { k } { + } G ( b _ { k } ) > c _ { k }$ , we have

$$
\sum_ {k \in M _ {2} ^ {*} \setminus M _ {1} ^ {*}} \frac {\beta_ {k} + G (b _ {k}) - c _ {k}}{p _ {2} ^ {*} - c _ {k}} <   | M _ {2} ^ {*} | - | M _ {1} ^ {*} |
$$

or

$$
| M _ {2} ^ {*} | - | M _ {1} ^ {*} | - \sum_ {k \in M _ {2} ^ {*} \setminus M _ {1} ^ {*}} \frac {\beta_ {k} + G (b _ {k}) - c _ {k}}{p _ {2} ^ {*} - c _ {k}} > 0.
$$

Thus, the LHS of (12) must be positive, that is,

$$
\sum_ {i \in M _ {1} ^ {*}} (\beta_ {i} + G (b _ {i}) - c _ {i}) \frac {p _ {1} ^ {*} - p _ {2} ^ {*}}{(p _ {1} ^ {*} - c _ {i}) (p _ {2} ^ {*} - c _ {i})}
$$

$$
= (p _ {1} ^ {*} - p _ {2} ^ {*}) \sum_ {i \in M _ {1} ^ {*}} \frac {\beta_ {i} + G (b _ {i}) - c _ {i}}{(p _ {1} ^ {*} - c _ {i}) (p _ {2} ^ {*} - c _ {i})} > 0
$$

Inasmuch as $\forall i \in M _ { 1 } ^ { * } , \ \beta _ { i } { + } G ( b _ { i } ) { - } c _ { i } { > } 0$ , and $p _ { 2 } ^ { * } -$ $c _ { i } { > } 0$ also $p _ { 1 } ^ { * } { > } c _ { i } ,$ the above inequality implies ${ p } _ { 2 } ^ { * } { < } { p } _ { 1 } ^ { * }$ Thus, $p _ { 2 } ^ { * } { \leq } c _ { l + 1 }$ as (as noted above) $p _ { 1 } ^ { * } { \leq } c _ { l + 1 }$ . This contradicts the fact that Genco l+1 is a member of M\*, so that claim (b) holds. Coupling (a) and (b), we have the uniqueness of $M ^ { * } ( p ^ { * } )$ . 5

Proof of Theorem 2

Proof. This is direct consequence of Lemmas 1 and 2 and Corollary 3. 5

Proof of Theorem 3

Proof. From Corollary 2, we know that, for any Genco $k { \in } M ^ { * } , ~ \beta _ { k } { + } G ( b _ { k } ) { > } c _ { k }$ , inasmuch as by definition $c _ { k } { = } _ { \underline { { { S _ { k } } } } } { + } G ( b _ { k } )$ , we have $\beta _ { k } { > } _ { \underline { { S } } k }$ , thus claim (i) holds. Claim (ii) holds inasmuch as, for any Genco $k { \in } \Xi { \backslash } M ^ { * }$ , the necessary and sufficient condition for k to participate in the spot market is $p ^ { * } { < } c _ { k } { > } \beta _ { k } { + } G ( b _ { k } )$ Claim (iii) holds inasmuch as, for any Genco $k { \in } \Xi { \backslash } M ^ { * }$ , if $p ^ { * } { < } c _ { k }$ and $\underline { { s _ { k } } } \le \beta _ { k }$ , thus $p ^ { \ast } { < } c _ { k } { = } s _ { k } { + }$ $G ( b _ { k } ) { \le } { \beta } _ { k } { + } G ( b _ { k } )$ , then k can make money neither in the contract market nor in the spot market; k is better off by closing its business. 5

## References

[1] L. Clewlow, C. Strickland, Energy Derivatives: Pricing and Risk Management, Lacima Publications, London, 2000.

[2] M. Crew, P. Kleindorfer, Peak load pricing with a diverse technology, The Bell Journal of Economics 7 (1) (1976) 207 – 231.

[3] C. Davidson, R. Deneckere, Long-term competition in capacity, short-run competition in price, and the Cournot model, Rand Journal of Economics 17 (1986) 404–415.

[4] J. Friedman, On the strategic importance of prices versus quantities, Rand Journal of Economics 19 (4) (1988) 607– 622.

[5] D.T. Gardner, J.S. Rogers, Planning electric power systems under demand uncertainty with different technology lead times, Management Science 45 (10) (1999) 1289– 1306.

[6] R. Kamat, S. Oren, Exotic options for interruptible electricity supply contracts, Operations Research 50 (5) (2002) 835 – 850.

[7] P. Kleindorfer, D.J. Wu, Integrating long- and short-term contracting via business-to-business exchanges for capitalintensive industries, Management Science 49 (11) (2003) 1597– 1615.

[8] D. Kreps, J. Scheinkman, Quantity precommitment and Bertrand competition yield Cournot outcomes, Bell Journal of Economics 14 (1983) 326 – 337.

[9] V. Martı´nez-de-Albe´niz, D. Simchi-Levi, Competition in supply option market, Working paper, Operations Research Center, Massachusetts Institute of Technology, Cambridge, MA, 2003.

[10] T. Mount, Using weather derivatives to improve the efficiency of forward markets for electricity, in: R.H. Sprague Jr. (Ed.), Proceedings of the Thirty-Fifth Annual Hawaii International Conference on System Sciences (HICSS-35 CD ROM), IEEE Computer Society Press, Los Alamitos, CA, 2002.

[11] O.E. Williamson, The Economic Institutions of Capitalism, The Free Press, New York, 1985.

[12] D.J. Wu, P. Kleindorfer, Competitive options, supply contracting and electronic markets, Management Science 51 (Forthcoming, Spring 2005).

[13] D.J. Wu, P. Kleindorfer, J.E. Zhang, Optimal bidding and contracting strategies for capital-intensive goods, European Journal of Operational Research 137 (3) (2002) 657–676.

![](/api/attachments/2BEWTDBJ/fulltext/images/2525b36a2e50c251fb75f3f5751370ee03677629c2427538e22bbf80b11791cc.jpg)

D.J. Wu is an Associate Professor of Information Technology Management at the College of Management, Georgia Institute of Technology. His current research interests include business value of ERP/IT investment, ERP/IT outsourcing contracts, options-based contracting in electronic markets, and multiagent learning. Dr. Wu’s most recent work has appeared in Management Science, Journal of Management Information Systems, European Journal of

Operational Research, Decision Support Systems, among others. Dr. Wu obtained his MA and PhD from the Wharton School, University of Pennsylvania; his BE in Computer Engineering and BE in Management Engineering were from Tsinghua University in Beijing, China.

![](/api/attachments/2BEWTDBJ/fulltext/images/ab7efc5ab6e09e9deeadb75c32ff5f1a2dd72c4dd9b031a01f52c086879d42d3.jpg)

Paul R. Kleindorfer is the Anheuser Busch Professor of Management Science, Economics and Public Policy at the Wharton School of the University of Pennsylvania. Dr. Kleindorfer graduated with distinction (BS) from the U.S. Naval Academy in 1961. He received his PhD in 1970 in Systems and Communication Sciences at the Graduate School of Industrial Administration, Carnegie Mellon University. Dr. Kleindorfer is Co-Director of the

Wharton Center for Risk Management and Decision Processes, where he conducts research on risk management and regulation, with special focus on energy and environment.
