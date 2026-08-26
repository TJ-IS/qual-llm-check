---
otero_id: 4452
otero_key: "RWBTZAVT"
title: "Risk aversion and loss aversion in core-selecting auctions"
authors: "Mark Schneider; Robert Day; Robert Garfinkel"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.08.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Mark Schneider ⁎, Robert Day, Robert Garfinkel

OPIM Department, School of Business, University of Connecticut, Storrs, CT 06269-1041, United State

## a r t i c l e i n f o

Article history: Received 23 April 2014 Received in revised form 13 August 2015 Accepted 15 August 2015 Available online 28 August 2015

Keywords: Auctions/bidding Core-selecting auctions Loss aversion Risk aversion Combinatorial auctions

## a b s t r a c t

Core-selecting combinatorial auctions have been introduced as an alternative to the Vickrey–Clarke–Groves (VCG) mechanism because VCG can result in payments that are not in the core with respect to bids, leading to unfair payments, unacceptably low revenues, and unstable outcomes. This raises an auction selection problem for an auctioneer deciding whether to employ a core-selecting auction or VCG mechanism in practice. The downside of a core-selecting auction is that it is not incentive compatible, as bidders have an incentive to reduce (shade) their bids below their true values. It has been argued that such bid shading in core-selecting auctions may lead to lower efficiency, lower revenue, and outcomes that are, on average, farther from the core with respect to true values, than the VCG mechanism. Using a much-studied auction environment, we address the auction selection problem faced by an auctioneer and obtain Bayes–Nash equilibrium bidding strategies when bidders are loss averse. We also bound the equilibrium strategies when bidders are risk-averse. This analysis demonstrates that when bidders are risk-averse or loss-averse, core-selecting auctions outperform the VCG mechanism in terms of revenue and stability, while yielding ef cient allocations with high probability.

© 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

With the increasing popularity of combinatorial auctions (in which bidders can place bids on combinations or packages of items), new pricing rules have been proposed which seek to find an acceptable tradeoff between criteria such as the revenue, efficiency, stability, and fairness of the auction mechanism. As a benchmark, the Vickrey–Clarke–Groves (VCG) mechanism is well-known to guarantee truthful bidding as a weakly dominant strategy in combinatorial settings. However, unless bidder submodularity holds<sup>1</sup> (for example, when goods are substitutes) VCG can yield unacceptably low revenues, unfair payments, and unstable outcomes (see [4,31,32]). These problems arise because VCG outcomes may not be in the “core.” This means that after final payments and allocations have been announced, a subset of bidders (called a coalition) would prefer to pay more than the winners paid for the same items. To mitigate these limitations of VCG, several authors have advocated the use of core-selecting auctions (see [1,14–16,28]). These auctions yield outcomes in the core when bids are treated as values, and have been used in recent spectrum auctions in Europe.

One limitation of core-selecting auctions, noted by Goeree and Lien [19], is that they are not incentive compatible. Using a simple twoitem, three-bidder auction environment, in which bidders are riskand loss-neutral, they argue that core-selecting auctions lead to lower efficiency, lower revenue, and outcomes that are, on average, farther from the core with respect to values, than those of VCG.

Goeree and Lien raise a fundamental question regarding which auction format is best suited for combinatorial auction environments, such as those for spectrum auctions, airport landing slots, or oil drilling rights. Goeree and Lien argue that in such settings the VCG mechanism is at least as desirable with respect to efficiency, revenue, and stability as core-selecting auctions.

In this work, the decision problem facing an auctioneer of whether to employ VCG or a core-selecting auction is addressed. The ‘auction–selection problem’ is a fundamental issue, both in theory and in public policy decisions. Some comparative analyses of different auction mechanisms have been conducted by Bichler [7] for multi-attribute auctions, by Bapna et al. [5] for multi-item online auctions, and by Cai et al. [8] for auctions with a proxy versus non-proxy setting. In addition to Goeree and Lien, Ausubel and Baranov [1] also compare core-selecting auctions to the VCG benchmark. Using the same setting as Goeree and Lien, but assuming correlated values, Ausubel and Baranov [1] study the role of correlation in bidder values on auction revenue and efficiency. They found that core-selecting auctions can yield greater revenue than VCG, while achieving similar levels of efficiency as the level of correlation increases.

In addressing the auctioneer's dilemma of whether or not to use a core-selecting auction, it is shown in this work in the same setting as Goeree and Lien, that even for the independent values case, if bidders are mildly risk-averse or loss-averse, core-selecting auctions significantly outperform VCG in terms of revenue and stability, while yielding efficient allocations with high probability.

The remainder of this paper is organized as follows. Section 2 provides background on core-selecting auctions and introduces the setting for the analysis to follow. Section 3 computes Bayes–Nash equilibrium bidding strategies when bidders are loss-averse. Section 4 computes an upper bound on the amount that bidders shade their bids in equilibrium when bidders are risk-averse. Sections 5, 6, and 7 explore the effect of risk aversion and loss aversion on efficiency, revenue, and stability of a core-selecting auction. Section 8 introduces an algorithm for computing approximate Bayes–Nash equilibria in combinatorial auctions and applies the algorithm to a setting previously not considered in the literature, in which there are three items and seven bidders. Section 9 concludes.

## 2. Background

## 2.1. Combinatorial extensions of the second-price single-item auction

In the second-price sealed-bid auction for a single item, bidders submit sealed bids, the highest bid wins the auction, and the winner pays an amount equal to the second-highest bid. In this single-item setting, the second-price sealed-bid auction is well-known to satisfy the properties of: individual rationality (IR), where each bidder is guaranteed a non-negative payoff; weakly-dominant-strategy incentive compatibility (IC), where each bidder has an incentive to bid her true value; bid efficiency (BE), in which the highest bid wins; and the core property (CORE), in which no coalition of players can propose a mutually beneficial alternative to the outcome prescribed by the auction mechanism

For many auction environments, such as auctions for spectrum licenses, there are several items for sale, and bidders often desire to submit bids on packages or combinations of items, for example, to avoid the risk of winning an incomplete set of complements. This concern has motivated the study of combinatorial auctions, where package bids are allowed. For a comprehensive study of combinatorial auctions see Cramton, et al. [12].

## 2.2. A simple combinatorial auction: The LLG setting

In a combinatorial auction, there are m bidders and n items, and each bidder, $B _ { i } ,$ can submit bids on subsets of items (also called packages.) Let $s$ be the set of available items. Each B has a valuation function, v (S) for any subset of items S ⊆ S, and in the most general setting can submit a bid $b _ { i } \left( S \right)$ on any or all non-empty subsets of . As in much of the related literature, we focus here on the setting of single-minded bidders, where each B is only interested in one particular $S _ { i } ,$ so we simply use v and $b _ { i }$ in place of v (S) and $b _ { i } ( S )$ . Likewise, the payment of $B _ { i }$ is denoted p . A summary of the notation used in this paper is provided in Table 1.

Summary of notation.

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $\mathcal{S}$ </td><td>Set of available items</td></tr><tr><td> $S$ </td><td>Subset of  $\mathcal{S}$ </td></tr><tr><td> $B_i$ </td><td>Bidder  $i, i = 1,2,...,m$ </td></tr><tr><td> $v_i(S)$ </td><td>Bidder  $i$ &#x27;s valuation for  $S$ </td></tr><tr><td> $b_i(S)$ </td><td>Bidder  $i$ &#x27;s bid for  $S$ </td></tr><tr><td> $p_i$ </td><td>Payment for bidder  $i$ </td></tr><tr><td> $p_i^{VCG}$ </td><td>VCG Payment for bidder  $i$ </td></tr><tr><td> $p_i^*$ </td><td>Expected payment of bidder  $i$  conditional on  $i$  winning.</td></tr><tr><td> $q_i$ </td><td>Probability that bidder  $i$  is in a winning coalition.</td></tr><tr><td> $c_i$ </td><td>Bidder  $i$ &#x27;s cost of not winning items</td></tr><tr><td> $\delta_i(v_i)$ </td><td>Bidder  $i$ &#x27;s shading given his valuation</td></tr><tr><td> $\alpha$ </td><td>Coefficient of relative risk aversion</td></tr><tr><td> $U_i$ </td><td>Expected utility for bidder  $i$ </td></tr><tr><td> $\theta_i$ </td><td>Average efficiency loss when bidder  $i$  wins</td></tr><tr><td> $E$ </td><td>Efficient Allocation</td></tr><tr><td> $R$ </td><td>Revenue</td></tr></table>

In contrast to the full-information analysis in Day and Milgrom [15], we assume that bidders' values are private, but are drawn from a commonly known distribution. Furthermore we analyze a simple setting, in which one “global” and two “local” bidders compete for two items. By “global bidder” we mean a bidder who bids only on the package of all items for sale, whereas a local bidder is interested only in a particular strict subset. This setup captures effects that were relevant, for example, in the recent Canadian spectrum auction where regional spectrum providers competed with national firms.

The setting will thus be referred to as LLG (for “Local–Local–Global”) and is the same format studied in all of the previous literature on private-value core-selecting auctions, including Goeree and Lien [19], Ausubel and Baranov [1], Beck and Ott [6] and Sano [33]. In the LLG setting, there are two items, ${ \mathcal { S } } = \{ { \sf X } , { \sf Y } \}$ , and three bidders, $\{ B _ { 1 } , B _ { 2 } , B _ { 3 } \}$ , with $S _ { 1 } = \{ X \} , S _ { 2 } = \{ Y \} , S _ { 3 } = \{ X , Y \}$ . As noted by Ausubel and Baranov [1], one can think of this scenario as an auction for spectrum licenses over the eastern and western regions of a country, with local bidders $B _ { 1 }$ and $B _ { 2 }$ each bidding only on the eastern or western region, respectively, and the global bidder ${ \sf B } _ { 3 }$ interested only in winning both.

Let $\nu _ { 1 }$ and $\nu _ { 2 }$ be independently uniformly distributed over [0,1], and let $\nu _ { 3 }$ be uniformly distributed over [0, 2]. If all bids are truthful, each bidder has ex ante a 50% chance of winning. Since $B _ { 1 }$ and $B _ { 2 }$ are symmetric in their valuations and utility functions, all results stated in this paper for $B _ { 1 }$ also hold for $B _ { 2 } ,$ except Proposition 2.

The results of Sections 3–7 apply directly only to this setting, but may shed intuition for more complex scenarios. The setting is chosen to facilitate comparisons to the findings of Goeree and Lien by introducing risk and loss aversion, and to offer insight about bidder behavior in core-selecting auctions. In some sense, the LLG setting may serve as a worst case analysis for core-selecting auctions since local bidders do not face competition from other local bidders, and competition serves to drive up bids, while the problems indicated by Goeree and Lien stem from low bids. Here we investigate the extent to which risk and loss aversion lead to increased bids, thereby mitigating those problems. It is also noted that equilibrium analysis in combinatorial auctions can quickly become computationally intractable, even for simple scenarios. Therefore in the early analysis of bidding behavior in core-selecting auctions, understanding simple situations such as LLG may also serve as a foundation for modeling situations of greater complexity. We explore one such extension to a more complex setting in Section 8.

## 2.3. The VCG mechanism

No combinatorial auction can simultaneously guarantee the four desirable properties of the second price, sealed-bid auction for a single item listed in Section 2.1. In particular, VCG is the unique combinatorial auction which satisfies properties IR, IC, and BE [21]. Thus VCG is one natural extension of the second-price sealed-bid auction in the combinatorial setting. However, VCG does not satisfy CORE

To achieve BE in a general combinatorial auction the NP-Hard “winner determination problem” (WDP), must be solved to find the bidmaximizing combination of non-overlapping bids. WDP is typically modeled as an integer program, and formulations abound in the literature. Since we focus here on the LLG setting in which WDP is quite simple, we omit a formal specification to conserve space. For LLG, WDP simply asks if $b _ { 1 } + b _ { 2 } \geq b _ { 3 } .$ , in which case $B _ { 1 }$ and $B _ { 2 }$ win, otherwise $B _ { 3 }$ wins.

Given a solution to WDP, VCG gives each winning bidder a discount equal to the difference between the total amounts of accepted bids from solving WDP with and without that bidder. For example, suppose $( b _ { 1 } , b _ { 2 } , b _ { 3 } ) = ( \mathbb { S } 1 1 , \mathbb { S } 1 0 , \mathbb { S } 1 5 )$ . Then $B _ { 1 }$ and $B _ { 2 }$ win with a combined bid of \$21. If $\overline { { B } } _ { 1 }$ did not participate, $B _ { 3 }$ would win with a bid \$5 higher than $b _ { 2 }$ Thus, by participating, $B _ { 1 }$ imposes a ‘cost’ of \$5 on $B _ { 3 }$ and $\mathsf { P } _ { 1 } ^ { \mathsf { V C G } } =$ \$5. Analogously, $\mathsf { P } _ { 2 } ^ { \mathsf { V C G } } = \bar { \mathbb { S } } 4 .$

Next consider what happens if $\dot { \boldsymbol { b } } _ { 3 }$ were reduced to \$8. Then $B _ { 2 }$ would win, whether or not $B _ { 1 }$ participates, and therefore $B _ { 1 }$ imposes no cost on

$B _ { 3 } .$ Thus, if $b _ { 3 } = \$ 8$ , we have $p _ { 1 } ^ { V C G } = p _ { 2 } ^ { V C G } = 0$ , since $B _ { 1 }$ and $B _ { 2 }$ each win regardless of whether the other participates. In this case, $B _ { 1 }$ and $B _ { 2 }$ would pay nothing for their items, despite the fact that $B _ { 3 }$ is willing to pay \$8. This situation illustrates the low-revenue problem of VCG that occurs because VCG does not satisfy the core property, motivating $B _ { 3 }$ to claim that the outcome is unfair. Ausubel and Milgrom [4] also show that this problem can lead to false-name bidding and collusion.

## 2.4. Core-selecting mechanisms

Limitations of VCG, as illustrated in the above example, have motivated an alternative approach to generalizing the second-price sealedbid auction for a single item. In particular, it has been proposed [14–16] that IR, BE, and CORE should be maintained strictly, while minimizing the deviation from IC.

In this work we demonstrate that “natural forces” that drive behavior such as risk aversion (due to the probability of not winning the auction) and loss aversion (due to an intrinsic cost of going home emptyhanded) can lead to highly efficient outcomes, even without designing a mechanism that is incentive compatible. (Much of mechanism design theory, on the other hand, does insist that IC be includEd.) An advantage of retaining IC is that it simplifies the bidding strategies for the bidders, who need only report their true valuations. Sacrificing IC increases the complexity of determining a bidder's equilibrium strategy, but as noted by Rothkopf et al. [32] and Ausubel and Milgrom [4], the IC property is often sacrificed in practice as the VCG mechanism is rarely employed. One practical consideration that government regulators face with implementing the VCG mechanism is the possibility of being sued by losing bidders who bid more for a collection of items than the winning bidders actually pay. This concern is alleviated if the auction employed is a core-selecting mechanism.

Day and Milgrom defined a core-selecting mechanism to be any mechanism which satisfies CORE when bids are treated as true values. Thus allocations are said to be “in the core with respect to bids.” An assignment of packages to bidders together with assigned payments (i.e., an outcome) is unblocked, if no losing coalition (i.e., subset of bidders) could suggest an alternative outcome preferred by every member of the coalition and the seller. An allocation is in the core with respect to bids if it is (bid) efficient and unblocked with respect to bids as opposed to values. We distinguish between BE, in which the packages maximize the total amount of winning bids, and (Pareto) efficiency which requires that final allocations maximize the total valuations of winning bidders.

## 2.4.1. The BCV auction

A core-selecting auction which minimizes total deviations from VCG payments was proposed by Day and Cramton [14]. As in Goeree and Lien [19], we refer to this auction as the BCV (bidder-optimal coreselecting VCG-nearest) auction. For a given VCG outcome, BCV yields the unique bidder-optimal core selecting allocation that minimizes the Euclidean distance from the VCG outcome in the payment space. BCV payments maximize bidders' total profits among all core-selecting payment rules, thereby minimizing the maximum possible total gains from deviating from truthful bidding subject to CORE. In addition to this desirable property, BCV payments have also become the first combinatorial core-selecting payment rules to be used in practice, having been applied in spectrum auctions for the United Kingdom and other European countries [11].

The payment rule in BCV is not the only attractive pricing method for core-selecting auctions. Others include “pay-as-bid” (which is selleroptimal and thus has the worst incentives for bidders), the iBundle of Parkes [29], the proxy auction of Ausubel and Milgrom [2], the iterative core-selecting auctions of Othman and Sandholm [28], and the reference rule auctions of Erdil and Klemperer [18] which minimize the Euclidean distance to a vector of reference prices. The BCV payment rule is a particular case of a reference rule with VCG payments as the reference vector. Others may select zero payments or some vector of reserve prices as the reference vector.

## 2.4.2. BCV payments in the LLG setting

To illustrate the construction of BCV prices we provide an example. Suppose $( b _ { 1 } , b _ { 2 } , b _ { 3 } ) = ( 0 . 7 5 , 0 . 5 , 1 )$ . I $\mathsf { f } B _ { 1 }$ were not present, $p _ { 3 } = 0 . 5$ making the VCG payment of $B _ { 1 }$ equal 0.5. Similarly, $p _ { 2 } ^ { V \bar { C } G } = 0 . 2 \bar { 5 }$ . However, to maintain CORE, $p _ { 1 } + p _ { 2 } \ge 1$ to satisfy $B _ { 3 } .$ Under the BCV rule, each local bidder pays his VCG payment, plus an equal share<sup>2</sup> of the remaining payments necessary for the outcome to satisfy CORE. Thus, under $\mathtt { B C V } , p _ { 1 } = 0 . 6 2 5$ , and $p _ { 2 } = 0 . 3 7 5$ (an equal amount of 0.125 above the VCG payment for each winner.) The VCG and BCV payments are represented in Fig. 1.

The closed form of $\dot { p } _ { 1 }$ under BCV pricing in the LLG setting, can be expressed as [19]:

$$
p _ {1} = \max (0, b _ {3} - b _ {2}) + 0. 5 (b _ {3} - \max (0, b _ {3} - b _ {1}) - \max (0, b _ {3} - b _ {2})).\tag{1}
$$

The single Eq. (1) can alternatively be expressed as a piecewise linear function of bids over four regions as follows:

$$
\begin{array}{l l} \text {I.} & p _ {1} = 0. 5 (b _ {3} + b _ {1} - b _ {2}) \quad \text {when} b _ {3} \geq b _ {2}, b _ {3} \geq b _ {1}, \text {and} b _ {1} + b _ {2} \geq b _ {3}, \\ \text {II.} & p _ {1} = 0. 5 b _ {1} \quad \text {when} b _ {3} <   b _ {2}, b _ {3} \geq b _ {1}, \\ \text {III.} & p _ {1} = 0. 5 b _ {3} \quad \text {when} b _ {3} <   b _ {2}, b _ {3} <   b _ {1}, \\ \text {IV.} & p _ {1} = b _ {3} - 0. 5 b _ {2} \quad \text {when} b _ {3} \geq b _ {2}, b _ {3} <   b _ {1}. \end{array}
$$

These regions, defined by the various possible expressions for VCG payments, are illustrated in Fig. 2. For a given $b _ { 1 } ,$ , Fig. 2 displays the different payment regions for $B _ { 1 } ,$ , with axes given by b and $b _ { 3 } .$

Definitions of b can be written analogously, with the roles of $B _ { 1 }$ and $B _ { 2 }$ reversed. In cases where $B _ { 3 }$ wins, on the other hand, the BCV outcome is in the core with respect to bids i $\dot { \boldsymbol { p } } _ { 3 } = b _ { 1 } + b _ { 2 } = p _ { 3 } ^ { V C G }$ , allowing us to assume for the remainder that $b _ { 3 } = \nu _ { 3 } .$

## 3. Loss aversion in core-selecting auctions

Two of the most robust and widespread behavioral principles in decision making are risk aversion and loss aversion. The idea behind loss aversion [25] is that “losses loom larger than gains,” or, more precisely, the utility of a loss is greater in magnitude than the utility of a comparable gain. In Kahneman and Tversky [25] utility is a function of changes in wealth rather than absolute wealth levels, and thus outcomes are judged as losses or gains relative to a reference point. The determinants of the reference point may be based on expectations or aspirations, as well as actual losses [34].

The impact of losing an auction and coming home empty-handed may be a strong motivation behind real-world decisions. In the context of combinatorial auctions, for instance, bidders in spectrum auctions are typically ordered by the executive board of a telecommunications firm to return with spectrum licenses in hand. Firms make planning decisions based on spectrum licenses or other goods which they expect to procure at auction. There may thus be a very real cost involved when bidders return without goods they were expected to win. In this section, we operationalize the concept of loss aversion by supposing that bidders set their expectations or aspirations on winning. From this reference point, losing carries with it negative (rather than zero) utility. This negative utility may be viewed as a cost of going home emptyhanded, and in this respect, our characterization of loss aversion differs from the more common formulation in which losses are measured as real monetary losses, relative to the status quo.

![](/api/attachments/RWBTZAVT/fulltext/images/b0557172084c077138e87ab7de116145e2c5eeb6f5fa4206ac6ac944ae13f6b2.jpg)  
Fig. 1. Construction of BCV prices in the LLG setting.

Let $q _ { 1 }$ be the probability that $B _ { 1 }$ wins. Also, let $p _ { 1 } ^ { * }$ be the expected payment of $B _ { 1 }$ conditional on $B _ { 1 }$ winning. Let $c _ { 1 }$ and $c _ { 2 }$ be the ‘costs of losing’ for $B _ { 1 }$ and $B _ { 2 } ,$ respectively, with $c _ { i } \geq 0 , i = 1 , 2$ , and let these costs be common knowledge. Giving $B _ { 1 }$ a linear utility function, as in Goeree and Lien [19] and Ausubel and Baranov [1], we can express the expected utility of $B _ { 1 }$ as:

$$
U _ {1} = \left(v _ {1} - p _ {1} ^ {*}\right) q _ {1} - c _ {1} (1 - q _ {1}).\tag{2}
$$

Proposition 1. $I f B _ { 1 }$ and $B _ { 2 }$ are loss-averse, with possibly different costs of losing, the Bayes–Nash equilibrium strategies are for $B _ { 1 }$ to bid $\nu _ { 1 } - \delta _ { 1 }$ , and for B to bid $\nu _ { 2 } - \delta _ { 2 }$ where:

$$
\delta_ {1} = 0. 2 5 - c _ {1} - 0. 5 \delta_ {2} + 0. 2 5 \delta_ {2} ^ {2}
$$

$$
\delta_ {2} = 0. 2 5 - c _ {2} - 0. 5 \delta_ {1} + 0. 2 5 \delta_ {1} ^ {2}.
$$

![](/api/attachments/RWBTZAVT/fulltext/images/0229585e5ed5362198d8fcaab5d213d09f32a592465dafb4b5b860bab91dfc07.jpg)  
Fig. 2. Different regions for $p _ { 1 }$ with BCV pricing.

All proofs are given in Online Appendix A. The parameter $\delta _ { i } , i = 1 , 2$ can be interpreted as a bidder's ‘minimum profit margin’ conditional on winning, which he reserves for himself. Should he win the auction, he will always receive at least a profit of $\delta _ { i } .$

Although Proposition 1 leads to a 4th order polynomial in $\delta _ { 1 }$ when substituting for $\delta _ { 2 }$ , we can solve for $\delta _ { 1 }$ numerically, given $c _ { 1 }$ and $c _ { 2 } .$ Values of $\delta _ { 1 }$ are given to the nearest two decimal places for different combinations of $c _ { 1 }$ and $c _ { 2 }$ in Table 2.

An interesting observation that emerges is that if $c _ { 2 }$ is very small (e.g., as would be the case if $B _ { 2 }$ is a standard expected utility maximizer), then $B _ { 1 }$ bids much closer to $\nu _ { 1 } ,$ , relative to the case where $c _ { 1 } = c _ { 2 } .$ In contrast, $\operatorname { i f } c _ { 1 } < c _ { 2 }$ , then $B _ { 1 }$ shades more, relative to the case $c _ { 1 } = c _ { 2 }$ . Our subsequent analysis of efficiency and revenue uses the benchmark case $c _ { 1 } = c _ { 2 }$

Proposition 2. $I f B _ { 1 }$ and $B _ { 2 }$ are equally loss-averse, (i.e., $c _ { 1 } = c _ { 2 } = c )$ , the Bayes–Nash equilibrium bid for $B _ { 1 } i s b _ { 1 } = \nu _ { 1 } - \delta ,$ where:

$$
\delta = 3 - 2 \sqrt {2 + c}.
$$

Observe that when $c = 0 .$ , the equilibrium strategy for $B _ { 1 }$ is to “shade” by $_ { 3 - 2 \sqrt { 2 } }$ which is again the solution obtained by Goeree and Lien [19]. When $c = 0 . 2 5 , b _ { 1 } = \nu _ { 1 }$ in equilibrium. All of our results stated for $B _ { 1 }$ hold analogously for $B _ { 2 } .$

## 4. Risk aversion in core-selecting auctions

The present work is also among the first to consider risk-averse behavior in a combinatorial core-selecting auction. Risk aversion is also investigated in the work of Guler et al. [22], but in the context of ascending core-selecting auctions. While intuition suggests that bidders with higher levels of risk aversion should bid closer to their true values, it is not clear whether a plausible, or even a low level of risk aversion can lead to substantially less shading in equilibrium.

The expected utility to $B _ { 1 }$ is given by: $E U _ { 1 } = E [ u ( \nu _ { 1 } - p _ { 1 } ) 1 _ { ( b _ { 1 } + b _ { 2 } \geq b _ { 3 } ) } ] ,$ where $u ( \nu _ { 1 } \textrm { -- } p _ { 1 } )$ ) is the utility function for $B _ { 1 }$ , defined over nonnegative monetary payoffs.

Definition 1. $B _ { 1 }$ is risk-averse if and only if $\iota ( \nu _ { 1 } - p _ { 1 } )$ ) is strictly concave in $\nu _ { i } - p _ { i } .$ . In contrast, $B _ { i }$ is risk-neutral if $u ( \nu _ { i } - p _ { i } ) = \nu _ { i } - p _ { i } .$

The analysis to follow considers the case of constant relative risk aversion $( { \mathrm { C R R A } } ) ^ { 3 }$ which is frequently used in economics—especially in the areas of investment behavior in finance and bidding behavior in auctions. The unique (up to affine transformation) utility function exhibiting constant relative risk aversion is given by:

$$
u (x) = \left\{ \begin{array}{l l} \frac {x ^ {1 - \alpha}}{1 - \alpha} & \alpha \neq 1, \\ l n (x) & \alpha = 1 \end{array} \right.\tag{3}
$$

where α is the coefficient of relative risk aversion, and in this paper, $x = \nu _ { i } - p _ { i } .$

In determining the validity of the assumption of CRRA, Dalal and Arshanapalli [13] analyzed investment data over a forty-year period, to test whether the fraction of wealth allocated to a riskless asset supported either the hypothesis of constant absolute risk aversion (CARA) or of CRRA. An investor exhibits CARA if the amount of wealth allocated to risky investments (in absolute dollars) is constant as wealth increases. An investor exhibits CRRA if the fraction of wealth allocated to risky investments does not change as total wealth increases. The authors rejected the hypothesis of CARA, but found support for CRRA. Evidence that relative risk aversion is constant is also provided by Chiappori and Paiella [10]. Quiggin [30] similarly favored the use of CRRA utility functions, at least as an approximation of empirical observations. In our analysis we use CRRA.

Table 2 δ as a function of c and $c _ { 2 } .$

<table><tr><td> $c_1 \backslash c_2$ </td><td>0</td><td>0.02</td><td>0.04</td><td>0.06</td><td>0.08</td><td>0.10</td><td>0.12</td><td>0.14</td></tr><tr><td>0</td><td>0.17</td><td>0.18</td><td>0.19</td><td>0.20</td><td>0.21</td><td>0.23</td><td>0.24</td><td>0.25</td></tr><tr><td>0.02</td><td>0.15</td><td>0.16</td><td>0.17</td><td>0.18</td><td>0.19</td><td>0.20</td><td>0.21</td><td>0.22</td></tr><tr><td>0.04</td><td>0.12</td><td>0.13</td><td>0.14</td><td>0.15</td><td>0.17</td><td>0.18</td><td>0.19</td><td>0.20</td></tr><tr><td>0.06</td><td>0.10</td><td>0.11</td><td>0.12</td><td>0.13</td><td>0.14</td><td>0.15</td><td>0.16</td><td>0.18</td></tr><tr><td>0.08</td><td>0.07</td><td>0.08</td><td>0.09</td><td>0.10</td><td>0.12</td><td>0.13</td><td>0.14</td><td>0.15</td></tr><tr><td>0.10</td><td>0.05</td><td>0.06</td><td>0.07</td><td>0.08</td><td>0.09</td><td>0.10</td><td>0.11</td><td>0.12</td></tr><tr><td>0.12</td><td>0.03</td><td>0.03</td><td>0.04</td><td>0.06</td><td>0.07</td><td>0.08</td><td>0.09</td><td>0.10</td></tr><tr><td>0.14</td><td>0.00</td><td>0.01</td><td>0.02</td><td>0.03</td><td>0.04</td><td>0.05</td><td>0.06</td><td>0.07</td></tr></table>

In concurrent work, Lubin et al. [26] considers other splits between bidders which can be accommodated by adding different weights into the quadratic optimization. In our analysis, we focus on the simplest case, following Day and Cramton [14] in which the weights are equal.

## 4.1. Bayes–Nash equilibrium analysis for risk-averse bidders

The equilibrium bidding strategies for $B _ { 1 }$ can be determined by the solution to the first order condition, $\frac { \partial E U _ { i } } { \partial b _ { i } } = 0$ . Unfortunately, applying the BCV payment rule to the LLG setting, results in a first order condition which is not amenable to a closed form solution under CRRA. However, through analyzing the first order condition, it is possible to bound the amount the bidder will deviate from truthful bidding in equilibrium. To do this, we first obtain bounds on $p _ { i }$ in the event that $B _ { i }$ deviates from her current bid, $b _ { i }$ by a small amount, $\epsilon \boldsymbol { b } _ { i } ^ { \dagger } .$ In Online Appendix A, we prove the following result:

Proposition 3. Denote the equilibrium bidding strategy for $B _ { 1 }$ in general as $b _ { 1 } ^ { * } = \nu _ { 1 } - \delta _ { 1 } ( \nu _ { 1 } )$ . Given CRRA utility functions (3) with $0 \leq \alpha < 1$ , an upper bound on $\delta _ { 1 } ( \nu _ { 1 } )$ in equilibrium is

$$
\overline {{\delta}} _ {1} = \frac {(1 - \alpha) \overline {{E (b _ {2})}}}{2}
$$

where $\overline { { E ( b _ { 2 } ) } }$ is an upper bound on $E ( b _ { 2 } )$ in equilibrium, generated by computing all values of $\dot { p } _ { 1 } \in [ \frac 1 2 b _ { 1 } , b _ { 1 } ]$

In Online Appendix B, we also discuss how to obtain $\overline { { E ( b _ { 2 } ) } }$ numerically (Fig. 5). Denote the lower bound on $b _ { 1 } ^ { * }$ in Proposition 3 by $\underline { { b } } _ { 1 } = \nu _ { 1 } - \overline { { \delta } } _ { 1 }$ We make two observations:

Observation 1. When $\alpha = 0 , \ \underline { { b } } _ { 1 } = b _ { 1 } ^ { * } = 3 \mathrm { - } 2 \sqrt { 2 }$ . Thus, under riskneutrality, the upper bound on the equilibrium bidding strategy coincides with the equilibrium strategy of Goeree and Lien.

In Proposition $^ { 3 , }$ an upper bound on equilibrium shading was found to be a constant-shading strategy (Fig. 6). Note that for the case where $\alpha = 0 ,$ , we have:

$$
\overline {{\delta}} _ {1} = \frac {\overline {{E (b _ {2})}}}{2}.
$$

Note that for $\alpha = 0 ,$ , we can determine the unique value of $E ( b _ { 2 } )$ , in which case $\overline { { E ( b _ { 2 } ) } } = E ( b _ { 2 } )$ . Thus, under risk-neutrality, we can solve for the exact equilibrium shading value, which yields precisely the result obtained in Goeree and Lien [19].

Observation 2. li $\begin{array} { r } { \boldsymbol { \mathfrak { n } } _ { \alpha \to 1 } \underline { { b } } _ { 1 } = \nu _ { 1 } } \end{array}$ : In the limit as α approaches 1, local bidders bid truthfully.

![](/api/attachments/RWBTZAVT/fulltext/images/f388c391f0c5ee4cc46a6529f74c26e149d5a7c686df438711af7b1a768ac1cf.jpg)  
Fig. 3. Lower bound on percent change in BCV revenue relative to VCG as a function of α.

## 4.2. Classifying risk preferences

Table 3 shows how δ changes as α increases. It also includes a practical classification of risk attitudes based on Holt and Laury [23]. Given the relationship between α and δ in Table 3, it would be useful to know which levels of relative risk aversion are typically observed. Although, the measurement of α has varied widely in empirical studies. Quiggin [30] observes, “Empirical research, such as that reported by Day and Cramton [14,27], suggests that the appropriate range (for α) is a neighborhood of 1.” For commonly observed levels of risk aversion, equilibrium shading is considerably reduced and approaches zero as α approaches 1.

## 5. Efficiency in core-selecting auctions

In this section, we consider the implications of our results for Pareto efficiency. The most important advantage of VCG is not that it guarantees truthful bidding, but rather that it always guarantees efficient allocations. Indeed, one may ask why it matters if bidders shade their bids if the outcome remains efficient. While the VCG mechanism is unique in its ability to guarantee efficiency, the cost of achieving full efficiency via IC is not small and includes low revenues, unstable outcomes, and unfair payments.

We note that an allocation is (Pareto) efficient if it maximizes the total valuations of all winners. In the LLG setting, efficiency occurs when $B _ { 1 }$ and $B _ { 2 }$ win and $\nu _ { 1 } + \nu _ { 2 } \ge \nu _ { 3 }$ or $B _ { 3 }$ wins and $\nu _ { 1 } + \nu _ { 2 } < \nu _ { 3 } .$ . In our analysis, we assume that ties are decided in favor of the local bidders.

Proposition 4. Let $b _ { i } = \nu _ { i } - \delta , i = 1 , 2$ . The probability of efficiency is $\begin{array} { r } { P ( E ) = \frac { 1 + ( \delta - 0 . 5 \delta ^ { 2 } ) \left( 1 - \delta \right) ^ { 2 } } { 1 + 2 \delta - \delta ^ { 2 } } } \end{array}$

Table 4 displays the equilibrium shading values for $B _ { 1 }$ for different values of the ‘cost’ of losing, c, and for the corresponding values of δ obtained in Proposition 2. The first and third columns of Table 4 show how P(E) changes for different values of c. From Table 4, we observe that when $c = 0 . 1$ 1, the BCV auction yields over 90% efficiency, and 100% when c = 0.25.

Since δ is a function of $\alpha _ { \ast }$ Table 5 shows $P ( E )$ against α. We find that moderate levels of risk aversion yield a 90% probability of efficiency. For $\alpha = 0 . 8 ,$ , a plausible level of risk aversion, $P ( E ) \ge 0 . 9 5$ and revenue is 12% higher than VCG. Note that as α goes to $1 , P ( E ) \to 1$ and the BCV auction approaches over 20% higher revenue than VCG. These results indicate that when bidders are risk-averse or loss-averse, the BCV auction achieves a high degree of efficiency.

![](/api/attachments/RWBTZAVT/fulltext/images/f8d0db57614aa16f5b9010ce6eac26bef5bcf59009601003cebdaeca0a14b9fb.jpg)  
Fig. 4. Percent change in BCV revenue relative to VCG as a function of loss aversion

Table 4  
![](/api/attachments/RWBTZAVT/fulltext/images/33e7fc0b7a27fefd1f527fb4eee8b240b4bc775c2546fb244f3b06e92da13082.jpg)  
Fig. 5. E(b ) as a function of k for different levels of risk aversion.

## 5.1. Efficiency loss in core-selecting auctions

Efficiency is often discussed in binary terms: either an outcome is efficient, or it is not. Here we consider how close an outcome is to efficiency. For example, when $( \nu _ { i } , b _ { i } ) = ( 1 5 , 1 2 ) , ( 1 0 , 9 ) , ( 2 4 , 2 4 )$ for $i =$ {1, 2, 3}, respectively, $B _ { 3 }$ wins even though $\nu _ { 1 } + \nu _ { 2 } > \nu _ { 3 } ,$ since $B _ { 1 }$ and B collectively shade their bids by more than 1. Now consider a variant of the above example: $( \nu _ { i } , b _ { i } ) = ( 1 5 , 6 ) , ( 1 0 , 3 ) , ( 1 0 , 1 0 ) \mathrm { f o r } i = \{ 1 , 2 , 3 \}$

In both examples the outcomes are inefficient. $B _ { 3 }$ wins in each case, even though $\nu _ { 1 } + \nu _ { 2 } > \nu _ { 3 } .$ But we may be tempted to view the outcome in the first example to be more efficient than in the second, since the valuation difference between the winning and losing coalition is smaller.

For an inefficient outcome, define the efficiency loss to be the amount by which the value of the efficient allocation exceeds that of the actual allocation. For LLG, we define the average efficiency loss when $B _ { 3 }$ wins, $\theta _ { 3 }$ as:

$$
\theta_ {3} = E \left[ v _ {1} + v _ {2} - v _ {3} \mid b _ {3} > b _ {1} + b _ {2}, v _ {1} + v _ {2} > v _ {3} \right] P \left[ b _ {3} > b _ {1} + b _ {2}, v _ {1} + v _ {2} > v _ {3} \right].
$$

Similarly, when the local bidders win:

$$
\begin{array}{l} \theta_ {1} = \theta_ {2} \\ \quad = E [ v _ {3} - v _ {1} - v _ {2} | b _ {3} <   b _ {1} + b _ {2}, v _ {1} + v _ {2} <   v _ {3} ] P [ b _ {3} <   b _ {1} + b _ {2}, v _ {1} + v _ {2} <   v _ {3} ]. \end{array}
$$

We ran a simulation of 5000 runs, where each run consisted of a randomly drawn value for each bidder with local bidder values drawn from a distribution that is uniform over the interval [0,1], and global bidder values drawn from a distribution that is uniform over [0,2]. Using the randomly drawn values and the bounds on equilibrium shading in Table $6 ,$ we computed an upper bound on the average efficiency loss for different degrees of risk aversion. Table 6 shows that, even as a worst-case, when outcomes are inefficient under BCV, they will not be “very inefficient.”

Shading as a Function of Payment Rule (Alpha = 0.2)  
![](/api/attachments/RWBTZAVT/fulltext/images/3cde801a2da2d320c6b56e5f2817c7cad88ddbfb3d62c26a5bad0667e65b3a59.jpg)  
Fig. 6. Upper bound on shading for $B _ { 1 }$ as a function of k and $\nu _ { 1 } .$

Table 3  
Upper bound on equilibrium shading as a function of risk aversion.

<table><tr><td>Risk preference classification1</td><td> $\alpha$ </td><td> $\overline{\delta}$ </td></tr><tr><td rowspan="2">Approximately risk-neutral</td><td>0</td><td>0.172</td></tr><tr><td>0.2</td><td>0.154</td></tr><tr><td>Slightly risk-averse</td><td>0.4</td><td>0.127</td></tr><tr><td rowspan="2">Risk-averse</td><td>0.6</td><td>0.094</td></tr><tr><td>0.8</td><td>0.049</td></tr><tr><td>Very risk-averse</td><td>1</td><td>0</td></tr></table>

<sup>1</sup> Risk preference classification for CRRA utility based on [23].

## 6. Revenue in core-selecting auctions

While BCV yields comparable levels of efficiency to VCG under typical levels of risk aversion, BCV performs better than VCG with regard to revenue in such cases. When bidders are risk-neutral, VCG yields approximately 9% higher revenue than BCV. However, this picture changes significantly for commonly observed levels of α. Fig. 3 shows the percentage deviation in revenue for BCV relative to VCG, as a worst-case scenario, for different levels of α. The formula used to obtain the expected revenue results for the BCV auction in the LLG setting is given below:

$$
E [ R ] = (1 7 / 2 4) + (2 / 3) \delta^ {3} - (1 / 8) \delta^ {4} - (1 / 4) \delta^ {2} - \delta .
$$

This formula is a special case (in which bidder values are independent) of the revenue result for the BCV auction in the LLG setting from Ausubel and Baranov [1].

Note that, for α = 0.7, BCV yields at least 9% greater revenue than VCG. Furthermore, in the limit as α goes to 1, BCV approaches over 20% higher revenue than VCG. Similar results were obtained for loss aversion. For c = 0.15, BCV yields over 8% greater revenue than VCG. When c = 0.25, BCV yields 20% higher revenue than VCG. For loss aversion, the BCV percentage deviation in revenue from VCG is illustrated in Fig. 4.

## 7. Distance from the core for VCG and BCV auctions

In this section we use average Euclidean distance from the core with respect to values as a proxy for stability, and show how risk aversion affects this distance for BCV as compared to VCG. We first note that stability is always achieved in BCV if bidders bid truthfully. In Sections 3–5, we found that local bidders bid truthfully when one of the following conditions hold:

I. Local bidders are risk-averse in the limit as α approaches 1. II. Local bidders are loss-averse with $c = 0 . 2 5$

Equilibrium strategies, Pareto efficiency and revenue as a function of loss aversion.

<table><tr><td>c</td><td>δ</td><td>P (efficiency)</td><td>% deviation from VCG revenue</td></tr><tr><td>0</td><td>0.171</td><td>0.84</td><td>-0.094</td></tr><tr><td>0.05</td><td>0.136</td><td>0.87</td><td>-0.032</td></tr><tr><td>0.10</td><td>0.102</td><td>0.90</td><td>0.028</td></tr><tr><td>0.15</td><td>0.067</td><td>0.94</td><td>0.089</td></tr><tr><td>0.20</td><td>0.033</td><td>0.97</td><td>0.148</td></tr><tr><td>0.25</td><td>0</td><td>1</td><td>0.204</td></tr></table>

Table 5  
Lower bound on efficiency and revenue as a function of risk aversion.

<table><tr><td>α</td><td> $\overline{\delta}$ </td><td>P (efficiency)</td><td>% deviation from VCG revenue</td></tr><tr><td>0</td><td>0.172</td><td>0.84</td><td>-0.094</td></tr><tr><td>0.2</td><td>0.154</td><td>0.86</td><td>-0.063</td></tr><tr><td>0.4</td><td>0.127</td><td>0.88</td><td>-0.016</td></tr><tr><td>0.6</td><td>0.094</td><td>0.91</td><td>0.042</td></tr><tr><td>0.8</td><td>0.049</td><td>0.95</td><td>0.120</td></tr><tr><td>1.0</td><td>0</td><td>1.00</td><td>0.205</td></tr></table>

Each of these conditions is sufficient to guarantee that BCV will always select core outcomes with respect to values. This is in contrast to VCG which has a 50% probability of yielding a core outcome with respect to values under LLG, despite being incentive compatible. However, there is no guarantee that conditions (i) or (ii) will hold in practice.

More importantly, we note that even when an auction mechanism does not select an outcome in the core with respect to values, it may select allocations which are very close to the core. Goeree and Lien [19] found that when bidders are risk-neutral, VCG is, on average, closer to the core with respect to values than BCV. We show that this result does not hold in general, when bidders are risk-averse. We further find that for typical levels of risk aversion, the BCV outcome is, on average, very close to the core.

Within the same simulation noted in Section 5, we computed the Euclidean distance between the BCV outcome and the core with respect to values, and between the VCG outcome and the core, for each of 5000 runs. We obtained an upper bound on the average distance from the core for the BCV mechanism and compared it to the exact solution for the VCG mechanism. These results are shown in Table 7 for different degrees of risk aversion. Note that even in this worst-case scenario for the BCV auction, outcomes are closer to the core than VCG for commonly observed levels of α. We note that an advantage of being closer to the core with respect to values is that the outcome may be viewed as relatively more stable.

## 8. Beyond LLG

In this section, an algorithm for computing approximate Bayes–Nash equilibria in combinatorial auctions is applied to extend our analysis from Section 4, and to study free-riding effects in environments which are too complex to obtain analytical solutions. In the LLG setting, the algorithm converges to equilibrium strategies consistent with the analytical result of Goeree and Lien [19]. The algorithm can also be used as a practical tool for bidder support in combinatorial auctions.

## 8.1. Summary of algorithm

The algorithm computes approximate equilibrium bidding strategies in combinatorial auctions. Under the algorithm, equilibrium bids are determined using an iterative best response procedure. The algorithm has been programmed in C++ using a Visual Studio platform.

The overall structure of the algorithm allows for the treatment of a variety of payment rules and bidding environments with different coalitional structures, parametric bidding strategies and arbitrary distributions of bidder valuations. An overview of the algorithm is given below:

Table 6  
Upper bound on average efficiency loss as a function of risk aversion

<table><tr><td>α</td><td> $\overline{\delta}$ </td><td>Average efficiency loss</td></tr><tr><td>0</td><td>0.172</td><td>0.0263</td></tr><tr><td>0.2</td><td>0.154</td><td>0.0214</td></tr><tr><td>0.4</td><td>0.127</td><td>0.0154</td></tr><tr><td>0.6</td><td>0.094</td><td>0.0081</td></tr><tr><td>0.8</td><td>0.049</td><td>0.0023</td></tr><tr><td>1</td><td>0</td><td>0</td></tr></table>

Table 7  
Upper bound on the average distance from the core in the BCV auction.

<table><tr><td>α</td><td> $\overline{\delta}$ </td><td>VCG distance from core</td><td>BCV distance from core</td></tr><tr><td>0</td><td>0.172</td><td>0.0907</td><td>0.112</td></tr><tr><td>0.2</td><td>0.154</td><td>0.0907</td><td>0.100</td></tr><tr><td>0.4</td><td>0.127</td><td>0.0907</td><td>0.082</td></tr><tr><td>0.6</td><td>0.094</td><td>0.0907</td><td>0.062</td></tr><tr><td>0.8</td><td>0.049</td><td>0.0907</td><td>0.033</td></tr><tr><td>1</td><td>0</td><td>0.0907</td><td>0</td></tr></table>

Step 1: The algorithm reads in the following information:

1) A csv file of randomly generated values according to some distribution for each bidder

2) Risk aversion parameter $a _ { 1 }$ for each bidder $i = 1 , 2 , . . . , n .$ In addition, the following must be specified:

3) A functional form for the payment rule

4) A functional form for the bidding strategies

5) A bid increment used for discretizing the strategy space such that bidder $i = 1 , . . . ,$ n has m possible strategies.

6) An initial default strategy vector

Step 2: Given bidders $1 , . . . , n ,$ , the algorithm computes the expected utility for bidder 1 at each of his $m _ { 1 }$ strategies, holding all other bidding strategies fixed at the initial default strategy vector.

Step 3: Update the initial strategy vector with the strategy corresponding to bidder 1's highest expected utility in Step 2.

Step 4: Compute the expected utility for bidder 2 at each of his $m _ { 2 }$ strategies, holding all other bidding strategies fixed at the updated strategy vector in Step 3.

Step 5: Repeat steps 3 and 4 for bidders $_ { 3 , . . . , n }$ until the updated strategy vector does not change $f o r n + 1$ iterations.

The final strategy vector is an approximate equilibrium strategy profile.

In essence, the algorithm reads in the csv file of randomly generated values, and engages in an iterated best-response routine, calculating the strategy for each bidder which maximizes that bidder's expected utility, holding the bidding strategies of other bidders fixed. The algorithm iterates, finding the best-response for each bidder, until no bidder in the auction changes its bid within some level of discretization (e.g. 0.001). In our discussion below, all examples used a discretization of the strategy space and the type space (i.e., the space of bidder valuations) at increments of 0.01.

In our examples, we consider constant-shading strategies of the form $b ( \nu ) = \nu - \delta . { \sf A }$ more general form can be used, but some parametric form is necessary. The restriction to some class of parametric bidding strategies is the cost for the increased complexity of combinatorial auction environments that the algorithm is able to handle. In addition to being a simple approximation, constant shading strategies have emerged in closed form analyses of equilibrium bidding behavior such as for the LLG setting of the BCV auction with risk-neutral bidders [19], and loss averse-bidders (as shown in Section 3), as well as a bound on equilibrium bidding strategies in the LLG, BCV environment when bidders are risk-averse (as shown in Section 4). Further, Day and Cramton [14] show these strategies eliminate ex-post envy. We recognize, however, that constant-shading strategies are by no means universal and in addition to the discretized nature of our results, we must issue the caveat that our approximate equilibria are determined under the restriction of the strategy space to these parametric bidding strategies.

## 8.2. Results from algorithm

For the BCV auction, the algorithm was run in two qualitatively different settings: the LLG auction, and a new larger environment involving three items and seven bidders. Since LLG has a known analytical solution, we turn to that case first before extending the algorithm to uncharted territory.

## 8.2.1. Case 1: The LLG setting

In Case 1, the algorithm read a csv file of 50,000 ‘auctions’ (i.e., 50,000 randomly generated value vectors, where a value vector contains one randomly generated value for each bidder in the auction). The default strategy vector was set at all bidders bidding truthfully.

Let $\{ \delta _ { 1 } , \delta _ { 2 } , \delta _ { 3 } \}$ denote the equilibrium shading vector for this auction. From the analysis of Goeree and Lien [19], we know that the exact equilibrium strategies are constant shading strategies with shading values: $\{ \delta _ { 1 } , \delta _ { 2 } , \delta _ { 3 } \} = \{ 3 - 2 \sqrt { 2 } , ~ 3 - 2 \sqrt { 2 } , ~ 0 \} \approx \{ 0 . 1 7 2 , 0 . 1 7 2 , 0 \} .$

Using the LLG setting with the BCV payment rule and risk-neutral bidders, the algorithm yielded the shading vector $\{ \hat { \delta } _ { 1 } , \hat { \delta } _ { 2 } , \hat { \delta } _ { 3 } \} = \{ 0 . 1 8 ,$ 0.17, 0.01}. The algorithm converged in 1 iteration on this approximate equilibrium strategy profile. As noted, the discretization level for determining convergence on an equilibrium is set at 0.01. While the correspondence is not exact, the approximate shading value for each bidder is within 0.01 of the analytical solution.

## 8.2.2. Case 2: A seven bidder format with the BCV auction

While LLG is the state of the art for analytical solutions of incomplete information combinatorial auctions, it is clearly a simplification of an actual combinatorial auction. One important feature of combinatorial auctions is that a given bidder may be on multiple coalitions, perhaps creating incentives to free-ride or to bid higher, depending on the structure of the particular coalitions. However, the LLG setting is not capable of capturing such important features of combinatorial auctions since each bidder is only on one coalition: The two local bidders form a coalition against a global bidder, and the global bidder is in a coalition by himself.

Here we introduce a more complex setting involving seven bidders, which allows for potentially richer behavioral patterns than can be observed in LLG. In particular, we consider a setting with three items, labeled A, B, and C, three local bidders (one bidding on each item), three ‘regional’ bidders (each bidding on a different pair of two items), and one global bidder who seeks to win A, B, and C. We let the local bidders have uniformly distributed values on $[ 0 , 1 ] ,$ regional bidders have uniformly distributed values on [0,2], and the global bidder's value is uniform on [0,3]. We define the following bidders and coalitions:

Bidders. Let $B _ { 1 }$ bid on $\mathsf { A } , B _ { 2 }$ bid on $\mathsf { B } , B _ { 3 }$ bid on $\phantom { + } C , B _ { 4 }$ bid on $\{ \mathsf { A } , \mathsf { B } \} , \mathsf { B } _ { 5 }$ bid on $\{ \mathsf { B } , \mathsf { C } \} , B _ { 6 }$ bid on {A,C} and $B _ { 7 }$ bid on {A,B,C}.

Coalitions. Coalition 1: $\{ B _ { 1 } , B _ { 2 } , B _ { 3 } \}$ ; Coalition $2 \colon \{ B _ { 3 } , B _ { 4 } \}$ ; Coalition 3: $\{ B _ { 1 } , B _ { 5 } \}$ ; Coalition 4: $\{ B _ { 2 } , B _ { 6 } \} ;$ Coalition 5: {B }.

Using the BCV payment rule, as outlined in Day and Cramton [14], we can obtain the form of this payment rule for the new setting with three items and seven bidders. We consider the case where bidders are either risk-neutral or risk-averse and use a constant shading strategy. The purpose of the algorithm is then to determine the constant shading amount, δ for each bidder $i = 1 , 2 , 3 , 4 , 5 , 6 , 7$ . In this setting, we ran 1000 ‘auctions’ for each of six cases, initializing the algorithm at truthful bidding in each case.

The cases run with the algorithm in this more complex setting are summarized in Table 8. Each row under the heading “risk preference” displays the risk-preference parameter, $\alpha _ { i } ,$ for a power utility function of the form $u _ { i } ( x ) = x ^ { \alpha _ { i } }$ for bidders $i = 1 , 2 , 3 , 4 , 5 , 6 , 7 .$ . The algorithm thus allows for bidders to differ in their degree of risk aversion. Analogously, each row under the heading “equilibrium shading” displays the corresponding shading amount for each bidder, given the vector of risk preferences in the same row.

We make a few remarks about the results in Table 8. First, when all bidders are risk-neutral (i.e., when $\alpha _ { i } = 1$ for all i), the algorithm converged to the approximate equilibrium shading vector: $\{ \hat { \delta } _ { 1 } , \hat { \delta } _ { 2 } , \hat { \delta } _ { 3 } , \hat { \delta } _ { 4 }$ $\hat { \delta } _ { 5 } , \hat { \delta } _ { 6 } , \hat { \delta } _ { 7 } \} = \{ 0 . 3 0 , 0 . 2 9 , 0 . 3 2 , 0 . 1 1 , 0 . 1 2 , 0 . 1 2 , 0 \}$ . The variation in shading values for each type of bidder reflects the stochastic nature of bidder valuations resulting from the simulated auction environment. Even so, the shading values are reasonably close for each type of bidder: the local bidders each shade near 0.30, the regional bidders each shade near 0.12, and the global bidder bids truthfully. Consistent with expectations, the local bidders shade more than the regional bidders since the local bidders are each on two coalitions (one coalition with the other local bidders and one coalition with a regional bidder), while each regional bidder is only on one coalition and so has less of an advantage from free-riding. As would be expected, the global bidder bids truthfully since he pays his VCG payment.

From Table 8, we also see that as bidder 1 becomes more risk averse (as $\alpha _ { 1 }$ decreases from 1 to 0.01), bidder 1's equilibrium shading decreases from 0.30 to 0.01, holding the other bidders fixed at riskneutrality. In addition, the shading increases for all other bidders who share a coalition with bidder 1 (i.e., for local bidders 2 and 3 and for regional bidder 5). This reflects an incentive to free-ride: Given that bidder 1 is bidding more, his coalition members can each bid less. Interestingly, there appears to be a residual effect on the other bidders not in a coalition with bidder 1. In particular, bidders 4 and 6 appear to maintain or even decrease their shading as bidder 1 bids more. Presumably this is due the fact that their coalition partners (bidders 2 and 3) are now bidding less, placing a burden on bidders 4 and 6 to bid higher. Finally, note that all bidders jointly reduce their shading when they are equally risk-averse, for a typical level of risk aversion [23], where $\alpha _ { i } = 0 . 5 ,$ , for all i.

Average revenue and the probability of an efficient allocation for the seven bidder case are given for different degrees of risk aversion in Table 9. Interestingly, we find that the probability of an efficient allocation is lower when bidder 1 is risk-averse and all other bidders are riskneutral than when all bidders are risk-neutral. The reason is that freeriding effects emerge as bidder 1 becomes increasingly risk-averse. In particular, as bidder 1 becomes more risk-averse and shades less, the local bidders and bidder 5, who are each on a coalition with bidder 1 can shade more.

Table 8  
Risk preferences and equilibrium shading strategies for the BCV auction with 7 bidders

<table><tr><td rowspan="2">Case</td><td colspan="7">Risk preference</td><td colspan="7">Equilibrium shading</td></tr><tr><td> $\alpha_1$ </td><td> $\alpha_2$ </td><td> $\alpha_3$ </td><td> $\alpha_4$ </td><td> $\alpha_5$ </td><td> $\alpha_6$ </td><td> $\alpha_7$ </td><td> $\delta_1$ </td><td> $\delta_2$ </td><td> $\delta_3$ </td><td> $\delta_4$ </td><td> $\delta_5$ </td><td> $\delta_6$ </td><td> $\delta_7$ </td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0.30</td><td>0.29</td><td>0.32</td><td>0.11</td><td>0.12</td><td>0.12</td><td>0</td></tr><tr><td>2</td><td>0.75</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0.25</td><td>0.44</td><td>0.34</td><td>0.07</td><td>0.15</td><td>0.12</td><td>0</td></tr><tr><td>3</td><td>0.5</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0.14</td><td>0.33</td><td>0.28</td><td>0.11</td><td>0.15</td><td>0.12</td><td>0</td></tr><tr><td>4</td><td>0.25</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0.05</td><td>0.42</td><td>0.38</td><td>0.08</td><td>0.19</td><td>0.09</td><td>0</td></tr><tr><td>5</td><td>0.01</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0.01</td><td>0.46</td><td>0.38</td><td>0.1</td><td>0.2</td><td>0.06</td><td>0</td></tr><tr><td>6</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.14</td><td>0.15</td><td>0.17</td><td>0.04</td><td>0.03</td><td>0.05</td><td>0</td></tr></table>

Table 9  
Risk preferences and equilibrium shading strategies for the BCV auction with 7 bidders

<table><tr><td rowspan="2">Case</td><td colspan="7">Risk preference</td><td colspan="3">Average revenue and probability of efficiency</td></tr><tr><td> $\alpha_1$ </td><td> $\alpha_2$ </td><td> $\alpha_3$ </td><td> $\alpha_4$ </td><td> $\alpha_5$ </td><td> $\alpha_6$ </td><td> $\alpha_7$ </td><td>BCV revenue</td><td>VCG revenue</td><td>BCV efficiency</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1.44</td><td>1.58</td><td>0.816</td></tr><tr><td>2</td><td>0.75</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1.41</td><td>1.58</td><td>0.779</td></tr><tr><td>3</td><td>0.5</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1.47</td><td>1.58</td><td>0.815</td></tr><tr><td>4</td><td>0.25</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1.45</td><td>1.58</td><td>0.788</td></tr><tr><td>5</td><td>0.01</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1.45</td><td>1.58</td><td>0.772</td></tr><tr><td>6</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5</td><td>1.62</td><td>1.58</td><td>0.888</td></tr></table>

Note also that if all bidders are moderately risk-averse $( \mathbf { e . g . } , \alpha _ { i } =$ $0 . 5 , i = 1 , 2 , 3 , 4 , 5 , 6 , 7 )$ , then BCV yields higher average revenue than VCG and 88.8% of all allocations are efficient. As a benchmark, if all bidders bid truthfully, BCV yields an average revenue of 1.81, compared to 1.58 for VCG, with both auctions yielding 100% efficient allocations.

## 9. Discussion

Auctions have recently proliferated as a cornerstone of market design and as a mechanism for government allocation of scarce public resources. Spectrum auctions have been among the most successful application areas, with hundreds of billions of dollars in government spectrum auctions worldwide. Indeed, the BCV core-selecting auction format discussed in this paper generated approximately \$19.5 billion in revenue in just ten spectrum auctions from 2012 to 2014. Thus the selection of the appropriate auction rules and format, and understanding the implications of behavioral phenomenon such as risk and loss aversion can have a tremendous impact on the economy. Combinatorial auctions in particular have also been used in the allocation of school-lunch contracts [17] and real-estate [20], among other areas, indicating that new developments in the theory of combinatorial auction pricing and bidding behavior can have broad impact for a number of applications, in addition to its deep impact in the spectrum area.

In any combinatorial auction environment where bidder submodularity may fail (including any domain with complementary goods), VCG is the only reasonable truth-inducing mechanism, but it experiences low revenue and unfair (i.e., non-core) allocations. Thus in any such environment the auctioning seller or government regulator has a difficult decision of which mechanism to employ. Here we sought to add evidence and analysis supporting the position that the BCV auction performs well and should be considered in realistic environments. Though our most thoroughly explored area concerned a small benchmark model from the literature, we extended the results to a broader context with more bidders and items in Section 8, showing that most of the intuition carries and that most of the relevant phenomena are apparent in even small problems. Coalitional structures matter, with some players facing VCG pricing from a personal perspective (thus having an incentive to bid truthfully) and others facing prices subject to core constraints (thus having incentives to shade their bids.) Though risk aversion and loss aversion provide pressure for a bidder to bid closer to the truth, one must also consider free-riding effects, where other members of a coalition anticipate the higher bids of a risk- or loss-averse competitor and respond by bidding lower. We showed that even in the presence of these countervailing effects, BCV performs quite well compared to VCG under realistic assumptions.

Indeed, if bidders are even mildly risk-averse, or face a cost of going home empty handed, then the BCV auction yields significantly better revenue than VCG with outcomes which are much closer to the core, while yielding high levels of efficiency, at least in the LLG setting. For instance, as a lower bound on efficiency and revenue, we observed that for $\alpha = 0 . 8$ (a typical level of risk aversion), BCV yields at least 95% efficient allocations, and 12% higher revenue than VCG. Also, when α = 0.8, BCV outcomes are, on average, at least three times closer to the actual core than outcomes generated by VCG. Thus, natural forces behind bidder behavior (such as risk aversion and loss aversion) strongly reverse the conclusion by Goeree and Lien [19] that, relative to VCG, the BCV auction “reduces efficiency, reduces revenue, and produces outcomes that are further away from the core.” Their argument relied on the assumption that bidders are risk-neutral and loss-neutral are unlikely to hold in practice, particularly given the extremely large stakes of real-world spectrum auctions. The results obtained for risk aversion and loss aversion, complement the results obtained when bidders' values are correlated [1], which collectively provide strong evidence in favor of core-selecting auctions under more realistic assumptions about bidder behavior.

Overall, we hope to have provided a glimpse of the relevant issues facing a decision maker when selecting a combinatorial auction format. The framework and methodology for exploring strategic behavior and equilibrium strategy will also shed light on future research in this area.

## Appendix A. Supplementary data

Supplementary data to this article can be found online at http://dx. doi.org/10.1016/j.dss.2015.08.007.

## References

[1] L.M. Ausubel, O. Baranov, Core-selecting Auctions With Incomplete Information, 2010 (Manuscript).

[2] L.M. Ausubel, P. Milgrom, Ascending auctions with package bidding, Frontiers of Theoretical Economics 1 (2002) 1–42.

[3] L.M. Ausubel, P. Milgrom, Ascending proxy auctions, SIEPR Discussion Paper No. 03– 35, 2004.

[4] L.M. Ausubel, P. Milgrom, The lovely but lonely Vickrey auction, in: P. Cramton, Y. Shoham, R. Steinberg (Eds.), Combinatorial Auctions, MIT Press, Cambridge, MA 2006, pp. 17–40.

[5] R. Bapna, P. Goes, A. Gupta, Comparative Analysis of Multi-item Online Auctions, 2001.

[6] M. Beck, M. Ott, Equilibria in Minimum-revenue Core-selecting Auctions, Stanford Univ, 2011.

[7] M. Bichler, An experimental analysis of multi-attribute auctions, Decision Support Systems 29 (2000) 249–268.

[8] G.G. Cai, Y.-J. Chen, X. Gong, Design of online auctions: proxy versus non-proxy settings, Decision Support Systems 52 (2012) 384–394.

[9] R.G. Chambers, J. Quiggin, Uncertainty, Production, Choice, and Agency. The Statecontingent Approach, Cambridge University Press, New York, NY, 2000.

[10] P. Chiappori, M. Paiella, Relative Risk Aversion is Constant: Evidence From Panel Data. 2011.

[11] P. Cramton, A Review of the 10–40 GHz Auction, Office of Communications, U.K., 2008

[12] P. Cramton, Y. Shoham, R. Steinberg (Eds.), Combinatorial Auctions, MIT Press, 2006.

[13] A.J. Dalal, B.G. Arshanapalli, Estimating the Demand for Risky Assets via the Indirect 1993.

[14] R. Day, P. Cramton, Quadratic core-selecting payment rules for combinatorial auctions. Operations Research 60 (2012) 588-603

[15] R. Day, P. Milgrom, Core-selecting package auctions. International, Journal of Game Theory 36 (2008) 393–407.

[16] R. Day, S. Raghavan, Fair payments for efficient allocations in public sector combinatorial auctions, Management Science 53 (2007) 1389–1406.

[17] R. Epstein, L. Henríquez, J. Catalán, G.Y. Weintraub, C. Martínez, A combinational auction improves school meals in Chile, Interfaces 32 (6) (2002) 1–14.

[18] A. Erdil, P. Klemperer, A new payment rule for core-selecting package auctions, Journal of the European Economic Association 8 (2010) 537–547.

[19] J.K. Goeree, Y. Lien, On the impossibility of core-selecting auctions, Institute for Em pirical Research in Economics, University of Zurich Working, 2009 Paper 452.

[20] D.R. Goossens, S. Onderstal, J. Pijnacker, F. Spieksma, Solids: a combinatorial auction for real estate, Interfaces 44 (4) (2014) 351–363.

[21] J. Green, J. Laffont, Incentives in Public Decision Making, North Holland, Amsterdam, 1979.

[22] K. Guler, I. Petrakis, M. Bichler, Core-selecting Auctions With Risk-averse Bidders. Manuscript, Technical University, Munich, 2012.

[23] C.A. Holt, S.K. Laury, Risk aversion and incentive effects, American Economic Review (2002) 1644–1655.

[25] D. Kahneman, A. Tversky, Prospect theory: an analysis of decision under risk, Econometrica 47 (1979) 264–291.

[26] B. Lubin, B. Bunz, S. Seuken, Fairness beyond the core, New Payment Rules for Combinatorial Auctions2015 (Manuscript).

[27] D.M. Newberry, J.E. Stiglitz, The Theory of Commodity Price Stabilization: a Study in the Economics of Risk Clarendon Press Oxford 1981

[28] A. Othman, T. Sandholm, Envy quotes and the iterated core-selecting combinatoria auction Proceedings 24th Conference on Artificial Intelligence 2010

[29] D. Parkes, iBundle: an efficient ascending price bundle auction, Proceedings, ACM Conference on Electronic Commerce 1999, pp. 148–157.

[30] J. Quiggin, Generalized Expected Utility Theory: the Rank Dependent Expected Utility Model, Kluwer-Nijhof, Amsterdam, 1993.

[31] M. Rothkopf, Thirteen reasons why the Vickrey–Clarke–Groves process is not practical, Operations Research 55 (2007) 191–197.

[32] M. Rothkopf, T. Teisberg, E. Kahn, Why are Vickrey auctions rare? Journal of Political Economy 98 (1990) 94–109.

[33] R. Sano, Non-bidding equilibrium in an ascending core-selecting auction, Games and Economic Behavior 74 (2012) 637–650.

[34] Loss aversion in riskless choice: a reference-dependent model, A. Tversky, D. Kahneman (Eds.),Quarterly Journal of Economics 106 (1991) 1039–1061.

Mark Schneider: Mark Schneider is a PhD candidate in the OPIM Department at the University of Connecticut, School of Business, with an undergraduate degree in Economics from Yale University. His research interests include analytical and experimental studies of decision making as well as the analysis of games and markets under incomplete or asymmetric information.

Robert Day: With a PhD in Applied Mathematics and Operations Research from the University of Maryland, Robert W. Day is a world-leader in auction design research, with several billions of dollars in revenue generated for government consulting clients in telecommunications regulation. His work emphasizes the synthesis of cutting-edge ideas from Computer Science, Economics, and Operations Research. With additional research in Hospital Management, Scheduling, Expected Utility Theory, and Grid Computing, his work has been recognized with the Dantzig Dissertation Award and the INFORMS Computing Society Prize.

Robert Garfinkel: Robert Garfinkel has a doctorate in Operations Research from the John Hopkins University and is the Robert Cizik Professor of Manufacturing and Technology Management in the School of Business at the University of Connecticut. His recent research interests are in utility theory as well as in applying operations research models to decision making in hospital administration and data security. His work has been applied to such other diverse areas as political districting, grid computing, testing of biochips, recommender systems, job scheduling, facility location, data imputation, and cartography.
