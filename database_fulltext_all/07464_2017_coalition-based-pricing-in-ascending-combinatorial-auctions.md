---
otero_id: 7464
otero_key: "BCHDEHUB"
title: "Coalition-Based Pricing in Ascending Combinatorial Auctions"
authors: "Martin Bichler; Zhen Hao; Gediminas Adomavicius"
year: "2017"
journal: "Information Systems Research"
doi: "10.1287/isre.2016.0681"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/BCHDEHUB/fulltext/images/18d043c25e60c0d7ccb6a27aa027f3a1220d5d29e349a24bf49f997e2fa0182e.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Coalition-Based Pricing in Ascending Combinatorial Auctions

Martin Bichler, Zhen Hao, Gediminas Adomavicius

To cite this article:

Martin Bichler, Zhen Hao, Gediminas Adomavicius (2017) Coalition-Based Pricing in Ascending Combinatorial Auctions. Information Systems Research

Published online in Articles in Advance 12 Jan 2017

http://dx.doi.org/10.1287/isre.2016.0681

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2017, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/BCHDEHUB/fulltext/images/4c6e5c013e72721596ab30406d68f80d186974f1ad964406df4a2e375202e3ab.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Coalition-Based Pricing in Ascending Combinatorial Auctions

Martin Bichler,<sup>a</sup> Zhen Hao,<sup>a</sup> Gediminas Adomavicius<sup>b</sup>

<sup>a</sup> Department of Informatics, Technical University of Munich, D-85748 Garching, Germany; <sup>b</sup> Carlson School of Management, University of Minnesota, Minneapolis, Minnesota 55455

Contact: bichler@in.tum.de (MB); hao@in.tum.de (ZH); gedas@umn.edu (GA)

Received: October 18, 2013 Accepted: October 3, 2016 Published Online in Articles in Advance: January 12, 2017

https://doi.org/10.1287/isre.2016.0681

Copyright: © 2017 INFORMS

Abstract. Bidders in larger ascending combinatorial auctions face a substantial coordination problem, which has received little attention in the literature. The coordination problem manifests itself by the fact that losing bidders need to submit nonoverlapping package bids that are high enough to outbid the standing winners. We propose an auction format, which leverages the information that the auctioneer collects throughout the auction about the preferences of individual bidders and suggests prices for the members of losing bidder coalitions, which in total would make a given coalition winning. We model the bidder’s bundle selection problem as a coordination game, which provides a theoretical rationale for bidders to agree to these prices, and highlights the role of the auctioneer in providing relevant information feedback. Results of extensive numerical simulations and experiments with human participants demonstrate that this type of pricing substantially reduces the number of auction rounds and bids necessary to find a competitive equilibrium, and at the same time significantly increases auction eficiency in the lab. This rapid convergence is crucial for the practical viability of combinatorial auctions in larger markets.

History: Sanjeev Dewan, Senior Editor; Subodha Kumar, Associate Editor.

Funding: The financial support from the Deutsche Forschungsgemeinschaft (DFG) [BI 1057/1-4] is gratefully acknowledged.

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2016.0681.

Keywords: multi-object auctions • coordination problem • coalition-based pricing • bidder behavior

## 1. Introduction

The need to buy or sell multiple objects arises in areas such as industrial procurement, logistics, and government allocation of spectrum licenses or other assets. It is a truly fundamental problem and, because of the advances in modern computing and communication capabilities that allow to adopt advanced auction mechanisms in increasingly broader and larger-scale online settings, the theory on how multiple indivisible objects should be allocated via an auction has enjoyed renewed interest in the past 10–15 years (Krishna 2002, Cramton et al. 2006, Bichler et al. 2010). One of the key goals in this research literature is to develop mechanisms that achieve high (allocative) eficiency. Allocative eficiency measures whether the auctioned objects end up with the bidders who have the highest valuations for them, representing a measure of social welfare.

In this paper we aim to design highly eficient ascending combinatorial auctions. Among the problems that make this goal hard to achieve, the coordination of bidders is a key problem that has been largely underexplored in prior work. Specifically, the currently losing bidders have a task of identifying individually profitable and collectively complementary item bundles to bid on from an exponentially sized set of all possible bundles (and determine appropriate bid prices for them), which together stand a chance of becoming a winning bid set in the next round. Identifying such bundle bids is possible either via a large number of auction rounds or requires a highly nontrivial coordination among coalitions of losing bidders, which is difficult without appropriate price feedback. We address this challenge by proposing a coalitional pricing rule, which is able to draw on the data that the auctioneer collects about bidders’ preferences throughout the auction and, as a result, helps currently losing bidders to coordinate. The proposed combinatorial auction mechanism exhibits substantially improved convergence and increased eficiency in lab experiments.

## 1.1. The Need for Ascending Combinatorial Auctions

Combinatorial auctions are among the most general types of multiobject market mechanisms, as they allow selling (or buying) a set of heterogeneous items to (or from) multiple bidders. Bidders can specify package (or bundle) bids, i.e., prices are defined individually for subsets of items that are auctioned (Cramton et al. 2006). The price is only valid for the entire bundle, and the bid is indivisible. For example, in a combinatorial auction a bidder might be willing to buy a bundle, consisting of items A and B, for a bundle price of e100, which might be more than the sum of the item prices for A (e30) and B (e50) that the bidder is willing to pay, if items are bought individually. The ability to submit bundle bids allows the bidders to express their economic preferences precisely, which is valuable in settings where bidders may have superadditive (or subadditive) valuations, i.e., when the bidder’s valuation of the entire bundle is higher (or lower) than the sum of individual item valuations, as in the above example. We will refer to a bidding language as a set of allowable bid types (e.g., bundle bids or bids on individual items only) in an auction. If bidders can win multiple bids, this is referred to as an OR bidding language. If they can only win a single bid at most, then it is an XOR bidding language.

In simultaneous multiobject auctions where only individual item bids are allowed, bidders incur the risk that they may end up winning only a subset of items from their desired bundle, and that they may end up paying too much for this subset. This is called the exposure problem (Rothkopf et al. 1998). While bidding on bundles in combinatorial auctions solves this problem, the design of these auctions leads to several types of complexity. One type of complexity is computational complexity when determining an optimal allocation. Other types of complexity are strategic complexity for bidders, and communication complexity. Strategic complexity describes the dificulty for bidders to find an optimal bidding strategy, while communication complexity describes the number of messages (i.e., price announcements and bid submissions) that need to be exchanged between the auctioneer and the bidders to determine the eficient allocation. It has been shown that the communication complexity to find the eficient solution in combinatorial auctions is exponential with respect to the number of items (Nisan and Segal 2006).

Computational complexity is manageable in realworld applications with a low number of items, bidders, and submitted bids; e.g., a winner determination problem with 20–30 items and 10 bidders can typically be solved in seconds. In terms of strategic complexity, one possible solution is to use the Vickrey–Clarke– Groves (VCG) mechanism, which achieves eficiency in dominant strategies, i.e., bidders cannot increase their payof by deviating from a truthful revelation of their valuations. Unfortunately, VCG is rarely used because of a number of practical problems (Ausubel and Milgrom 2006b). In particular, in many markets bidders are simply reluctant to reveal their true valuations to an auctioneer in a single-round sealed-bid auction, and they prefer an ascending (multiround) auction format that is more transparent and conveys information about the competition in the market. In a recent paper, Levin and Skrzypacz (2016) write that dynamic auctions have an advantage in multi-item settings, because bidders can gradually find out how their demands fit together. This property is important but not necessarily given in all multi-item auction designs.

## 1.2. Ineficiency in Ascending Combinatorial Auctions

As a result, much recent research has focused on ascending multiobject auctions, i.e., generalizations of the single-item English auction where bidders can outbid each other iteratively. However, it was recently shown that no ascending multiobject auction format can be incentive compatible for general types of bidder valuations when modeled as a Bayesian game (Sano 2012, Goeree and Lien 2016). In other words, with suficient prior information about other bidders and allowing any type of valuations, it is always possible that a bidder may profit from not bidding truthfully up to his valuation. Let us consider a simple example with two identical items and three bidders. One “global” bidder is only interested in the bundle of two items, while each of the two “local” bidders wants only one of the items. If the local bidders together are stronger than the global bidder (i.e., the sum of their one-item valuations is higher than the global bidder’s two-item valuation), then they could always try to free ride on each other. Suppose that the global bidder has a valuation of \$10 for the two-item bundle, and each local bidder has a valuation of \$8 for their item of interest. One local bidder could drop out at a price of \$2.50, such that the other local bidder is forced to bid up to \$7.50 to become winning. Sano (2012) has shown that, without complete information but having prior distributional information about bidder valuations in a Bayesian game, a local bidder might drop out too early resulting in the auction being ineficient in equilibrium. In any case, this and similar types of manipulations are only possible with suficient prior information about other bidders’ valuations.

In many real-world markets, the information set available to bidders is quite diferent from markets modeled under complete information or as Bayesian games with single-minded bidders. Bidders are interested in multiple packages, and it is unknown to a bidder which packages are of interest to his competitors. Also, the common prior assumption in Bayesian games, which has long been a concern in game theory (Wilson 1987), is particularly troublesome in combinatorial auctions with exponentially many possible packages a bidder can bid on. Bidders would need to have the same prior distributions for all possible packages, which is unrealistic in all but very small combinatorial auctions. In addition, in many auctions in procurement or on the Internet, the number of competitors is unknown, and there can always be a new bidder throughout the auction. Bid shading is less of a concern in such environments.

Even if bidders do not shade their bids because of a lack of prior information about others’ valuations, this does not automatically lead to eficient outcomes because of the communication complexity of combinatorial auctions. If bidders do not bid on all bundles of positive value to them, but only a small subset thereof, then the auction may not end with an eficient outcome. This restricted bundle selection has been experimentally shown to be the biggest barrier to eficiency across auction formats (Schefel et al. 2012).

Because of the exponential growth of possible bundles, even in combinatorial auctions with only 20 items bidders would not be able to reveal over a million possible bundle valuations, i.e., to submit all possible bundle bids. Recent combinatorial auctions used for spectrum sales had 100 licenses simultaneously on sale. It is clearly impossible to enumerate all of the exponentially many bundles for a bidder. Finding promising bundles, i.e., bundles that stand a chance of becoming winning when combined with the bids of other bidders, becomes the central strategic problem of bidders in such auctions, which has been largely ignored in the game-theoretical literature on combinatorial auctions. This coordination problem requires diferent theoretical models.

## 1.3. Contributions and Outline

The main contribution of this work is to propose an auction format that leverages the bidding information that the auctioneer collects throughout an ascending auction about losing, but high-revenue coalitions. We select such high-revenue coalitions and propose ask prices to the members of each coalition such that together they can outbid the current winning coalition. This new type of pricing rule is called the coalitional winning level (CWL). The auctioneer can provide such prices based on the bids that he collected in past rounds, and he can distribute the additional amount needed to make the losing coalition winning in a fair manner using the cost-sharing rule based on the Shapley value (SV) (Dehez 2007). In particular, we show that such a cost-sharing rule not only satisfies fairness axioms but also results in a cost sharing among the bidders in a coalition that is in the core, i.e., it does not create incentives to deviate for a subset of the bidder coalition.

In this work, we are focusing on markets where bidders typically do not have reliable prior information about other bidders’ valuations or the number of their competitors. The coordination problem introduced earlier is the central strategic challenge for bidders in such markets. Bidders have an exponential number of packages to choose from, but want to coordinate on competitive equilibrium in a low number of rounds.

We introduce a stylized game-theoretical model of the strategic problem of bidders, which helps understand the role of the auctioneer aiding coordination in a CWL auction. By contrast to earlier game-theoretical models in this field, we allow bidders to be interested in multiple packages. Thus, the assumptions in our model highlight the coordination problem of bidders rather than the free-rider problem. We focus on markets without reliable prior distributional information, so that we can restrict our attention to the bidder’s decision problem in a single bidding round. It can be shown that the auctioneer in this auction model acts like a third party in a correlated equilibrium. This analogy provides an explanation as to why rational bidders accept a CWL ask price for a package, even when the given package does not maximize absolute payof in the given round based on minimum bid prices. In other words, acting on the information feedback provided by the auctioneer is a rational strategy for bidders even in a complete information model, where bidders have full information about other bidders’ valuations that they could possibility use to manipulate. Also, in an online combinatorial auction in the field, without prior distributional valuation information and with hundreds of packages to bid on, the ask prices (CWLs) of the auctioneer provide a helpful recommendation of how complementary bids of losing bidders can become winning in the next round.

Our experimental results show that the CWL auction has significantly higher eficiency, and at the same time communication with the auctioneer is substantially reduced compared to ascending auction designs from prior literature. In our experiments we do not see free-riding behavior, i.e., the bidders indeed take advantage of ask prices to coordinate. This rapid convergence of the auction increases the practical applicability of the mechanism to a broad set of application settings.

The paper is structured as follows. In Section 2, we discuss related literature. In Section 3, we introduce the auction format and describe theoretical properties. Section 4 presents the experimental design, while Section 5 summarizes the results of the numerical simulations. These simulations provide an indicator for the outcome of such auctions with truthful bidders who bid on their payof-maximizing bundles in each round. In Section 6 we summarize and discuss the findings of our lab experiments, before concluding the article in Section 7.

## 2. Related Literature

Let us briefly survey the relevant literature in this section. As mentioned earlier, the well-known VCG mechanism achieves eficiency in dominant strategies. Its central limitation is that the auction outcome might not be in the core (Ausubel and Milgrom 2006b), i.e., the winning coalition of bidders might have to pay less than what a losing coalition of bidders was willing to pay. This is possible because of the Vickrey discount that the winning bidders are given (Goeree and Lien 2016). We provide a simple example with two items (A and B) and three bidders (1, 2, and 3) to make this apparent. Suppose bidder 1 only wants A for which he has bid his value of e7, bidder 2 only wants B for which he has bid his value of e8, and bidder 3 only wants the package AB with a value of e10. The auctioneer declares bidders 1 and 2 to be winners and the maximum total valuations of the sale to be e15. In a VCG mechanism the winners get a discount, which incentivizes truthful bidding. As a result, the Vickrey payment for bidder 1 is e10 <sup>−</sup> e8 <sup></sup> e2 and that of bidder 2 is e10 <sup>−</sup> e7 <sup></sup> e3. Consequently, the auction revenue is e5, although bidder 3 was willing to pay e10. In many applications, such as high-stakes government auctions, such an outcome might be dificult to justify. Therefore, such high-stakes auctions are typically conducted as open-cry ascending auctions, rather than sealed-bid events. For these reasons, during the past decade there has been an increasing interest in core-selecting auctions (Day and Milgrom 2008), i.e., auctions where there cannot be a losing coalition of bidders that together could have outbid the winners based on their submitted bids.

iBundle (Parkes and Ungar 2000), the ascending proxy auction (APA) (Ausubel and Milgrom 2006a), and the primal-dual auction by de Vries et al. (2007) are examples of ascending core-selecting auction formats that provide allocatively eficient solutions when bidders follow a straightforward bidding strategy, i.e., when they truthfully bid on their payof-maximizing bundle(s) in each round until the prices stop because a bidder becomes winning. If bidder valuations are buyer submodular, then this strategy is even an ex post Nash equilibrium, which is a strong solution concept where bidders do not need to reason about other bidders’ valuations. Buyer submodularity requires that, if a bidder is added to a smaller coalition, then he adds more to the overall revenue than if added to a larger coalition with more bidders (Parkes 2006).

Note that superadditive valuations violate buyer submodularity. In the above example with three bidders, the third bidder has superadditive valuations since both items are complements for him (i.e., he does not want each item individually, only their combination), thus violating buyer submodularity. Also, it is easy to see that it is not an ex post Nash equilibrium strategy to bid truthfully until the price clock stops or the valuation is reached in this example. Bidder 1 might drop out before his price for one unit stops increasing for his one item and he might free ride on bidder 2, who then needs to outbid bidder 3 in an ascending auction. In such cases, only a Bayesian Nash equilibrium is possible, which requires prior distributional information about other bidders’ valuations. In this market, when bidders only have prior distributions about the valuations, the Bayes–Nash equilibrium strategy can even lead to nonbidding of the local bidders, and consequently, to ineficient outcomes (Sano 2012, Guler et al. 2016). We will refer to the family of eficient ascending multiobject auctions, which allow for an ex post Nash equilibrium at least for buyer submodularity, as bidder-optimal ascending core-selecting (BACS) auctions.

Adomavicius and Gupta (2005) introduce deadness (DLs) and winning levels (WLs) both as pricing rules and information feedback to bidders in combinatorial auctions and evaluate them in the lab (Adomavicius et al. 2013). Deadness levels are the lowest prices above which a bid can still potentially become winning in any future auction state (depending on the arrival of complementary bids from other bidders), winning levels are prices above which a bid would immediately become winning. Petrakis et al. (2013) showed that ascending combinatorial auctions with deadness levels as ask prices (the DL auction) belong to the above family of BACS auctions and share the same ex post Nash equilibrium strategy as BACS auctions.

BACS auctions can be thought of as algorithms designed to provide an exact solution to a hard computational problem. However, they typically lead to a huge number of auction rounds (Schneider et al. 2010), and lab experiments provide evidence that human bidders substantially deviate from straightforward bidding (Schefel et al. 2011) so that eficiency is no longer guaranteed. More recent experimental research shows that restricted bundle selection due to the exponential growth of bundles is the main reason for ineficiency in combinatorial auctions (Schefel et al. 2012, Bichler et al. 2013), while bid shading is less of an issue. Rather than shading their bids optimally, bidders in such auctions are primarily concerned with finding the right bundle, which, together with the bids of other bidders, will end up in a winning coalition. We will refer to this problem as the “coordination problem” and to markets with little or no distributional information about bidder valuations as “online” markets. We use the term online markets related to the concept of online algorithms or online mechanisms from the literature in computer science (Parkes 2007).

Our proposed combinatorial auction mechanism is diferent from the ones mentioned above. In particular, the auctioneer targets losing coalitions by proposing coalitional winning levels (CWLs) as ask prices to the members of these coalitions, which would allow them to jointly outbid the currently winning coalition. The semantics of CWLs is intuitive for bidders and provides guidance in what is arguably the central problem that bidders face in each round of a combinatorial auction with many items: the selection of promising bundles, which stand a chance of becoming winning together with the bids of other bidders.

## 3. The Auctions

In what follows, we will briefly describe the DL auction as a representative of BACS auctions. We will then introduce the proposed CWL auction and discuss some theoretical underpinnings of such an auction. Before we do this, we provide an example of diferent pricing rules as they have been discussed in the literature to better illustrate the diferent approaches.

## 3.1. An Introductory Example with Diferent Pricing Rules

The following example extends the one used by Petrakis et al. (2013) to illustrate DLs. We compare CWLs with iBundle, DLs, WLs, and an auction format with linear ask prices, the Resource Allocation Design (RAD) (Kwasnica et al. 2005).

The top two rows of Table 1 describe six bids from diferent bidders (i.e., bidders 1 to 6), submitted on subsets of three items (A, B, and C). In this example we will assume that at this point in the auction, bidders are only interested in those bundles for which they have submitted bids so far.

The bottom five rows of Table 1 describe bundle prices in diferent auction formats at this stage in the auction (i.e., after six bids have been submitted). Subscripts indicate bidders, i.e., 22 indicates a bid of e22 from bidder 1. Ask prices have subscripts only if they difer among bidders in this example. Asterisks denote the provisional winning bids. In this example, we assume an XOR bid language, where each bidder can win at most one bundle. For such languages, it is known that DLs and WLs for a given bundle may have diferent values for diferent bidders, i.e., their computation needs to be personalized (Petrakis et al. 2013). Losing bidders need to bid higher than these values by a minimum bid increment. As mentioned earlier, the WL for a given bundle describes the lowest bid price above which a submitted bid would instantly become winning, i.e., without needing any new complementary bids from other bidders. However, it is clear from the example that bidders 4 and 5 could possibly become winning even at lower prices than their current WLs, if they coordinate and form a coalition, indicated by prices in bold type. Ask prices in iBundle (Parkes and Ungar 2000) are in line with DLs, but they add a bid increment (e1) for losing bids. Linear programming-based heuristics for computing linear prices (i.e., where a bundle price is simply a sum of individual item prices) such as RAD (Kwasnica et al. 2005) are an alternative. Unfortunately, RAD prices can be lower than a losing bid (see the RAD ask price on AC for bidder 4) or unnecessarily much higher than the suficient winning bid (see the RAD ask price on B for bidder 5) (Bichler et al. 2009).

Table 1. Example with Six Bids and Diferent Ask Prices

<table><tr><td>Bundles</td><td> $AB$ </td><td> $BC$ </td><td> $AC$ </td><td> $B$ </td><td> $C$ </td></tr><tr><td>Bids</td><td> $22_{1}^{*}, 16_{2}$ </td><td> $24_{3}$ </td><td> $20_{4}$ </td><td> $7_{5}$ </td><td> $8_{6}^{*}$ </td></tr><tr><td>DL</td><td> $22_{1}, 16_{2}$ </td><td> $24_{3}$ </td><td> $20_{4}$ </td><td> $7_{5}$ </td><td> $8_{6}$ </td></tr><tr><td>WL</td><td> $22_{1}, 22_{2}$ </td><td> $30_{3}$ </td><td> $23_{4}$ </td><td> $10_{5}$ </td><td> $8_{6}$ </td></tr><tr><td>iBundle</td><td> $22_{1}, 17_{2}$ </td><td> $25_{3}$ </td><td> $21_{4}$ </td><td> $8_{5}$ </td><td> $8_{6}$ </td></tr><tr><td>RAD</td><td>22</td><td>24</td><td>14</td><td>16</td><td>8</td></tr><tr><td>CWL</td><td> $22_{1}, 22_{2}$ </td><td> $30_{3}$ </td><td> $\mathbf{21.5}_{4}$ </td><td> $\mathbf{8.5}_{5}$ </td><td> $8_{6}$ </td></tr></table>

In an online market, bidders typically start out bidding on their highest valued packages to find out if this package can become winning together with the bids of others. After the winner determination, the auctioneer can evaluate which losing bidders would, in combination, achieve high revenue and have a potential to outbid the current winning coalition. A CWL price can be seen as a way to derive personalized and nonlinear ask prices in-between DLs and WLs designed to quickly find a competitive equilibrium, i.e., a state where there is no coalition of bidders that can outbid the currently winning coalition of bidders at these ask prices, as defined below.

Definition 1 (Competitive Equilibrium, CE (Parkes 2006)). Prices α and allocation $X ^ { \ast }$ are in competitive equilibrium if allocation $X ^ { \ast }$ maximizes the payof of every bidder and the auctioneer revenue given prices α. The allocation X<sup>∗</sup> is said to be supported by prices α in CE.

It has been shown that competitive equilibrium and the core, mentioned in Section 2, refer to the same concept in multiobject auctions (Bikhchandani and Ostroy 2002). CWLs are a way to find such prices such that, at the end of an ascending auction, there is no coalition of losing bids who could make themselves better of. CWLs leverage the information that is available about losing coalitions during the auction and provide tailor-made prices to bidders in these coalitions, i.e., proposals on how they can jointly outbid the currently winning coalition. The coalition of bidders 4 and 5 in our example would only need to increase their bids by a combined e3 plus increment to become winning. Both bidders would become winning, if bidder 4 bids above e21.5 and bidder 5 bids above e8.5, for example. The proposed CWL feedback is designed to help coordinating bidders who form a high-revenue coalition, and it is particularly useful if bidders are interested in many packages. In what follows, we will describe DLs and WLs in a more formal way before we introduce CWLs and their properties.

## 3.2. The DL Auction

We will first introduce the necessary notation and then describe the DL auction as an example of a BACS auction. There is a set K of m indivisible items indexed with $k ,$ which are auctioned among a set I of n bidders. Let $i , j \in \mathcal { I }$ denote the bidders and $v _ { i } \colon 2 ^ { \mathcal { K } } $  denote a value function of bidder i, which assigns a real value to every subset $S \subseteq \mathcal { K }$ of items. The bundle that is assigned to bidder i in allocation X is denoted as $X _ { i } \subseteq { \mathcal { K } }$ . We denote $X = ( X _ { 1 } , \ldots , X _ { n } )$ as an allocation of the m items among bidders, with $X _ { i } \cap X _ { j } = \emptyset$ for every $i \neq j$ , with $i , j \in \mathcal { I } . \operatorname { A }$ coalition is defined as a set of bidders whose bids constitute a feasible allocation. A winning coalition is the coalition of bidders whose bids constitute the revenue maximizing allocation, and a losing coalition is any coalition except the winning coalition. In other words, a bidder can be a member of the winning coalition and, at the same time, be a member of multiple losing coalitions, based on the bids he submitted. We denote a losing coalition as $L ,$ and the set of all losing coalitions as L. Let Γ denote the set of all possible allocations, then $X ^ { L } \in \Gamma$ denotes an allocation of items among a losing coalition $L \in { \mathcal { L } } .$

The social welfare of an allocation $X = \left( X _ { 1 } , \ldots , X _ { n } \right)$ is $\textstyle \sum _ { i \in { \mathcal { I } } } v _ { i } ( X _ { i } ) .$ , and an eficient allocation $X ^ { \ast }$ maximizes social welfare among all allocations $X , \mathrm { i . e . , } X ^ { \ast } \in$ arg $\begin{array} { r } { \operatorname* { m a x } _ { \boldsymbol { X } } \sum _ { i \in \mathcal { I } } v _ { i } ( X _ { i } ) } \end{array}$ . The revenue maximizing allocation, ${ \bar { X } } ,$ , is such that X<sup>¯</sup> <sup>∈</sup> arg max $\textstyle . \sum _ { i \in { \mathcal { I } } } b _ { i } ( X _ { i } )$ , where $b _ { i }$ is the bid price of bidder i for the bundle assigned to him in allocation X.

We focus on ascending combinatorial auctions (CAs), which consist of diferent rounds and where an ask price $\alpha _ { i } ( S )$ is available for each bundle S and each bidder i in each round. A round defines a certain time period during which the auctioneer collects new bids from bidders and at the end of which a new allocation and new ask prices for the next round are computed. The DL auction uses the XOR bidding language, $\mathrm { i . e . , }$ at most one bundle bid from a given bidder could be winning at any given time. Let $\Breve { B ^ { t } }$ denote the bids submitted in round $t \in \mathbb { N } ,$ and ${ \bar { X } } ^ { t }$ denote the revenue maximizing allocation after round $t ,$ based on the set of all bids B submitted in the auction thus far. Note that in theory a round could close after each new bid submitted, such that t may also refer to a single bid. In our experiments, each bidder can submit multiple bids in a round. Variable $B _ { l } ^ { t }$ denotes the set of all losing bundle bids, even losing bids from a winning bidder (because a winning bidder can only win at most one bundle, but may well submit multiple bids in each round), after round t. Variable  describes a minimum bid increment per round. We next define deadness levels as ask prices:

Definition 2. The deadness level, ${ \mathrm { D L } } ,$ of a bundle S for bidder i in round $t , \mathrm { D L } ^ { t } ( i , S )$ , is the minimal price that bidder i has to overbid to maintain a chance to win S at some future round $t ^ { \prime } > t$

So DLs are the highest prices at or below which a bid cannot become winning in any future auction state. Therefore, they constitute a lower bound for acceptable new bids. The DL auction uses only DL ask prices $( \mathrm { i . e . , }$ $\mathrm { D L } + \epsilon )$ and belongs to the family of BACS auctions, as was shown in Petrakis et al. (2013). Algorithm 1 outlines the DL auction.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1 (The DL auction algorithm)
Result: $\bar{X}$ and bid prices $b_i(\bar{X}_i)$

1 Initialization
2    for $i = 1$ to $n$ do
3    for each $S$ do $\alpha_i(S) \leftarrow \epsilon$
4    $X_i \leftarrow \emptyset$
5    end
6    termination $\leftarrow$ false
7    $t \leftarrow 0$
8    $B \leftarrow \emptyset$
9 while ($\neg$ termination) do
10    $t \leftarrow t + 1$
11    Bidders submit bids $B^t$ where each $b_i(S) \in B^t$ satisfies $b_i(S) \geq \alpha_i(S)$
12    if ($B^t = \emptyset$) then termination $\leftarrow$ true
13    else
14    $B \leftarrow B \cup B^t$
15    Compute $\bar{X}^t \in \arg \max_X \sum_{i \in \mathcal{I}} b_i(X_i)$
16    for each $b_i(S) \in B_l^t$ do
17    $\alpha_i(S) \leftarrow \mathrm{DL}^t(i, S) + \epsilon$
18    end
19 end
</div>

As shown in Algorithm 1, the DL auction is conducted in a round-based ascending format. The auction begins with ask prices of 0. At the start of each subsequent round, each bidder is given the following information: ask prices on all bundles he has bid on so far in the auction (but can request ask prices of any other bundles on demand, if desired) and information whether he is currently winning any bundle he has previously bid on. This is the only information made available to each bidder, and he does not know anything else about other bidders, including the bundles they have bid on so far, or if they are winning some bundles. A bidder can then submit as many bids as he likes in this round. However, the bids need to be higher than or equal to the respective ask prices. A bid higher than the ask price is called a jump bid. When all bidders finish submitting new bids, the round closes and a new allocation with the current winning coalition as well as new ask prices are computed. The auction terminates when no new bid is submitted in a round, and winning bidders pay what they bid.

We have also implemented two additional auction rules: an activity rule to incentivize bidders to stay active from the start, and the possibility for bidders to submit a so-called “last-and-final $b i d , ^ { \prime \prime }$ which helps to avoid small eficiency losses due to bid increments.

Both are described below and complete our description of the DL auction.

In general, ascending multiobject auctions can enforce diferent types of activity rules. In our experiments, we used an activity rule in line with earlier experiments in the combinatorial auction literature (Schefel et al. 2012). If a currently losing bidder in round t does not submit any new bids in round $t + 1 ,$ then he is not allowed to bid in any future rounds $t ^ { \prime } > t$ All his previous active bids will still be considered relevant for the auction, but he may not submit any new bid again for the auction. This activity rule does not apply to currently winning bidders, as their inactivity does not necessarily imply that they are not interested in the auction any more. We have used this soft activity rule in both the DL and the proposed CWL auction.

In addition, it is possible to have a situation, where the new ask price $\alpha _ { i } ( S )$ is too high for a bidder because the bid increment was too big. In this case, the DL auction allows for a last-and-final bid between these bounds (i.e., between the bidder’s last bid on the package and the new ask price $\alpha _ { i } ( S ) )$ (Parkes 2006). Suppose bidder i has submitted a bid of e18 on bundle AB in round t. In the next round $t + 1 ,$ , he sees that he has not won AB, and the new ask price for AB, based on the DL plus an increment, is e22. Assuming the bidder’s true valuation for AB is e20, then he can now submit a last-and-final bid of $\epsilon 2 0 - \epsilon ,$ where  is a profit margin he wants to achieve. However, after this round he would not be able to bid on AB anymore.

We described the key details of the DL auction, and will now turn to one of the main properties satisfied by the DL auction, as it is related to the straightforward bidding strategy.

Definition 3. A straightforward bidder i only bids ask prices on his demand set $D _ { i } = \{ S \subseteq { \mathcal { K } } \colon v _ { i } ( S ) - \alpha _ { i } ( S ) \geq$ $\mathsf { \tilde { v } } _ { i } ( S ^ { \prime } ) - \alpha _ { i } ( S ^ { \prime } ) , \forall S ^ { \prime } \subseteq \mathcal { K } \}$ in each round, i.e., on those bundles that maximize his payof, based on given ask prices.

Importantly, in the DL auction format, straightforward bidding is an ex post equilibrium if bidders’ valuations are submodular (Parkes 2006, Petrakis et al. 2013). This is because with such valuations the auctions end up in VCG prices for the winners, and bidders do not have an incentive to shade their bids (Parkes 2006). Unfortunately, straightforward bidding also leads to a large number of auction rounds as all losing package valuations get elicited from all bidders via minimum bid increments in each round. While this process allows to prove eficiency of the allocation, the number of bids that need to be submitted by bidders is beyond what human bidders can be expected to do, except in auctions with only very few items. Schneider et al. (2010) have shown, using numerical simulations, that, with straightforward bidding, even small auctions with only 9 items can easily lead to 150 or more auction rounds. With 10 minutes per round this would lead to 25 hours, which would be unacceptable in most applications.

## 3.3. Coalitional Winning Levels

In addition to deadness levels (DLs), Adomavicius and Gupta (2005) also defined winning levels (WLs) as a form of information feedback to bidders. Amount ${ \mathrm { W L } } + \epsilon$ represents the minimum bid price for a bidder on a bundle, such that this bundle bid becomes winning at round t <sup>+</sup> 1, if no other bid was submitted. As indicated in Section 1, WLs can be prohibitively high for small bidders in larger auctions with many items, since WLs reflect an amount a bidder needs to bid to become winning unilaterally, i.e., without the help of any new bids of other bidders.

The coalitional winning level (CWL) extends the concept of a WL ask price from an individual bidder to a group of losing bidders. It is an ask price that would make a losing coalition winning, if accepted by all members of the coalition. This is valuable feedback for overcoming coordination problems inherent to all combinatorial auctions, as illustrated in the following example.

Example 1. Consider four small bidders, each one bidding e10 on a diferent single item, and a large bidder bidding e100 on the bundle containing all four of these items. The valuation of each small bidder for their respective single item is e50. By definition, the WL ask price faced by each small bidder is $\epsilon 7 0 + \epsilon$ for the desired item, indicating the scenario where each small bidder competes with the large bidder individually. The WL-based ask price is higher than the small bidders’ valuations; as a result, the small bidders would not bid anymore, and the eficient allocation is not achieved. For comparison, the CWL for the losing coalition is e100 in total. So if, for example, each small bidder in the coalition receives an individual CWL ask price of $\epsilon 2 5 + \epsilon$ and bids on it, the coalition would outbid the large bidder. Finally, the DL of each bidder would be e10 only, as each bidder could become winning at e10 if the other small bidders outbid the large bidder.

Example 1 illustrates that the spread between DLs (here e10) and WLs (here e70) can be very large. In examples with many items and bidders being interested in many bundles, CWLs can give bidders useful information about bundles for which complementary bids exist. In addition, they can help bidders focus on a few (rather than all) of their bundles with positive valuations (i.e., where the bidder valuation for a bundle is higher than its current ask price).

Let L denote a coalition of losing bidders, where bidder i desires the bundle $S _ { i } ,$ with $S _ { i } \cap S _ { j } = \emptyset$ for all $i , j \in L$ . Denote the collection of the desired bundles as $\textstyle S ^ { \dot { L } } = \bigcup _ { i \in L } S _ { i }$

Definition 4. The coalitional winning level, CWL, of coalition L for the desired bundles $\mathbf { \bar { \mathbf { \nabla } } } S ^ { L }$ at a particular round t is the minimal price that the coalition must bid in aggregate to win these bundles at auction state $t + 1 \colon$ $\begin{array} { r } { \mathrm { C W L } ^ { \mathrm { { \smile } } } ( L , S ^ { L } ) = \operatorname* { m i n } \sum _ { i \in L } b _ { i } ( S _ { i } ) } \end{array}$ , so that ${ \cal S } _ { i } \in \bar { X } ^ { t + 1 } \forall i \in { \cal L } .$ assuming all new bids of this coalition come in the next round, i.e., t <sup>+</sup> 1.

In this definition we assume that only the losing bidders $i \in L$ submit bids in round $t + 1$ , so that $\bar { X } ^ { t + 1 }$ describes the revenue maximizing allocation in round $t + 1$ . The CWL value for any losing coalition L can be computed as follows:

$$
\operatorname{CWL} ^ {t} (L, S ^ {L}) = \operatorname{CAP} ^ {t} (\mathscr {K}) - \operatorname{CAP} ^ {t} (\mathscr {K}, S ^ {L}).\tag{1}
$$

$C A P ^ { t } ( { \mathcal { K } } )$ denotes the optimal value of the winner determination problem $( { \dot { C } } A P ) $ , and $C A P ^ { t } ( \mathcal { K } , S ^ { L } )$ the optimal value of CAP in which each bidder $i \in L$ wins his desired bundle $S _ { i } \in S ^ { L }$ for free. There is substantial literature on the computational hardness of CAP (Leyton-Brown et al. 2006), but instances of up to 20–30 items and 10 bidders can typically be solved in seconds. The computation of CWLs in Equation (1) can easily be derived from the proof for $\begin{array} { r } { \dot { \mathrm { W L } } ^ { t } ( i , S ) = C A P ^ { t } ( \mathcal { K } ) \dot { - } } \end{array}$ $C A P ^ { t } ( \mathcal { K } , S _ { i } )$ in Petrakis et al. (2013), where the desired bundles $S ^ { L }$ of all bidders $i \in L$ are treated as if they were one single bundle $S _ { i }$ of one single losing bidder i. Similar computations have also been described by Adomavicius and Gupta (2005).

## 3.4. Computing Individual CWLs

Once $\mathsf { C W L } ^ { t } ( L , S ^ { L } )$ is computed for losing coalition $L ,$ we still face the question of how to distribute this price among members of L. Let us denote CWL $\mathbf { \Omega } _ { \mathfrak { i } } ^ { t } ( L , S _ { i } )$ as the amount that transforms the $\mathsf { C W L } ^ { t } ( L , S ^ { L } )$ to individual ask prices for every member i of losing coalition $L$ ${ \mathrm { H e r e } } , S _ { i }$ describes the package assigned to bidder $i \in L$ There are diferent ways how bidders in a coalition can share the additional amount ${ \Delta } ^ { t } = \mathrm { C W L } ^ { t } ( L , S ^ { L } ) -$ $\textstyle \sum _ { i \in L } b _ { i } ( S _ { i } )$ <sup>)</sup> that is needed to outbid the current winning coalition. One could think of many cost sharing functions $\Delta _ { i } ^ { t } = g _ { i } ( \Delta ^ { t } )$ to distribute $\Delta ^ { t }$ among the bidders i <sup>∈</sup> L such that $\textstyle \sum _ { i \in L } \Delta _ { i } ^ { t } = \Delta ^ { t }$ . For example,

$\Delta _ { i } ^ { t } = \dot { \Delta ^ { t } } \times ( | S _ { i } | / | S ^ { L } | )$ based on the bundle size $\lvert S _ { i } \rvert$ of a bundle $S _ { i }$ within a coalition;

$\Delta _ { i } ^ { t } = \Delta ^ { t } \times ( b _ { i } ( S ) / ( \sum _ { i \in L } b _ { i } ( S ) ) )$ based on the level of the bid prices $b _ { i } ( S )$ within a coalition;

$\Delta _ { i } ^ { t } \bar { = } \Delta ^ { t } \times ( 1 / | L | )$ based on the number of members in a coalition (aka uniform distribution).

These heuristic cost-sharing functions are simple because their calculations require only a few simple arithmetic operations. Aside from computational simplicity, $\mathsf { a } f a i r$ division of ∆<sup>t</sup> among the bidders $i \in L$ would be a natural design goal. The Shapley value is arguably the most well-known solution concept for coalitional games (Dehez 2007), and it is considered fair, as it satisfies a number of fairness axioms including symmetry and additivity (Shoham and Leyton-Brown 2009).

Let us briefly review the Shapley value. Let L be a coalition of $| L |$ bidders, and $M \subseteq L$ be some subcoalition. Let $w ( M )$ denote the coalitional value of M that needs to be distributed among its members. Coalitional value can also be the cost that a coalition has to bear. The Shapley value $\theta _ { i }$ provides a unique distribution (among the players) of the value generated by the coalition of all bidders $i \in L$ and is defined as

$$
\theta_ {i} = \sum_ {M \subseteq L \backslash \{i \}} \frac {| M | ! (| L | - | M | - 1) !}{| L | !} (w (M \cup \{i \}) - w (M)).\tag{2}
$$

Overall, the Shapley value has a number of general properties, which are desirable. For example, it distributes the total value of a coalition. Bidders with the same contribution to the coalitional value get the same Shapley value. Bidders who do not contribute to the coalitional value get a zero Shapley value. However, if designed appropriately as a convex game, there are two properties of our coalitional game that make the Shapley value particularly desirable.

In superadditive games with $w ( L \cup L ^ { \prime } ) \geq w ( L ) + w ( L ^ { \prime } )$ and $L \cap L ^ { \prime } = \emptyset$ , where L and L are two losing coalitions, the Shapley value guarantees each participant a payof of at least the amount that he could achieve by not forming a coalition. An important subclass of superadditive games are convex games. A game is convex if $w ( L \cup \bar { L ^ { \prime } } ) \geq w ( L ) + w ( L ^ { \prime } ) \bar { - w } ( L \cap L ^ { \prime } )$ . For every convex game, the core is nonempty, and the Shapley value is also in the core for convex games. This means that, based on the Shapley value, there cannot be a losing subcoalition of $M \subset L$ that can make themselves better of as compared to a situation where all members of the coalition L accepted the Shapley value. In other words, subcoalitions do not have an incentive to deviate, and the coalition can be considered stable as neither individuals nor groups of bidders in L have an incentive to deviate.

Note that sharing a given $\Delta ^ { t } \ = \ \mathrm { C W L } ^ { t } ( L , S ^ { L } ) \ -$ $\textstyle \sum _ { i \in L } b _ { i } ( S _ { i } )$ in a round among a losing coalition of bidders is neither a convex nor a superadditive game. However, instead of distributing $\Delta ^ { t } ,$ , one can distribute the overall savings that the coalition experiences compared to the sum of the winning levels of each bidder: $\begin{array} { r } { \Psi ^ { t } = \sum _ { i \in L } { \mathsf { W L } } ^ { t } ( i , S ) - { \mathsf { C W L } } ^ { t } ( \breve { L } , S ^ { L } ) = } \end{array}$ $\begin{array} { r } { \sum _ { i \in L } { \mathsf { W L } } ^ { t } ( i , S ) - \sum _ { i \in L } { \mathsf { C W L } } _ { i } ^ { t } ( L , S _ { i } ) } \end{array}$ . We require that $\mathrm { W L } ^ { t } ( i , S ) \geq \mathrm { C W L } _ { i } ^ { t } ( L , S _ { i } )$ for all $i \in L$ for sharing functions, where this is not always satisfied. We can now use the Shapley value to derive $\Psi _ { i } ^ { t }$ from $\Psi ^ { t }$ , and this game is superadditive and convex as the following results show.

## Lemma 1. The game of distributing

$$
\Psi^ {t} (L) = \sum_ {i \in L} \mathrm{WL} ^ {t} (i, S) - \mathrm{CWL} ^ {t} (L, S ^ {L})
$$

to individual bidders $i \in L$ is superadditive.

Lemma 2. The game of distributing

$$
\Psi^ {t} (L) = \sum_ {i \in L} \mathrm{WL} ^ {t} (i, S) - \mathrm{CWL} ^ {t} (L, S ^ {L})
$$

to individual bidders $i \in L$ is convex.

The proofs for both lemmata can be found in Online Appendix A. Let us now define the Shapley valuebased computation of individual CWLs.

Definition 5. A Shapley value-based $\mathrm { C W L } _ { i , \mathrm { S V } } ^ { t } ( L , S _ { i } )$ is defined as $\mathsf { W L } ^ { t } ( i , S ) \mathsf { - } \dot { \Psi } _ { i , \mathrm { S V } } ^ { t } ,$ , where

$$
\Psi_ {i, \mathrm{SV}} ^ {t} = \sum_ {M \subseteq L \setminus \{i \}} \frac {| M | ! (| L | - | M | - 1) !}{| L | !} (\Psi^ {t} (M \cup \{i \}) - \Psi^ {t} (M)).\tag{3}
$$

In this definition, $\Psi ^ { t } ( M )$ is the total coalitional value or savings of coalition M. This leads to the following proposition.

Proposition 1. Consider only the members $i \in L$ of a losing coalition, who need to derive individual CWLs from $\mathsf { C W L } ^ { t } ( L , S ^ { L } )$ <sup>)</sup>. No subcoalition $M \subset L$ can make itself better of as compared to when all members of the coalition accepted $\mathrm { C W L } _ { i , S V } ^ { \dot { t } } ( L , S _ { i } )$ given that $v _ { i } ( S _ { i } ) \geq \dot { \mathrm { C W L } } _ { i , S V } ^ { t } ( L , S _ { i } )$ for all $i \in { \mathcal { I } } .$

Proof. Lemma 2 shows that the computation of $\mathrm { C W L } _ { i , \mathrm { S V } } ^ { t } ( L , S ^ { L } )$ constitutes a convex coalitional game. Every convex game has a nonempty core, and in every convex game the Shapley value is in the core (Shoham and Leyton-Brown 2009, p. 394). Q.E.D.

Explaining the Shapley value and its properties to subjects in the lab takes a substantial amount of time. Since it is important in an economic experiment that subjects fully understand the mechanism, in our experiments, we have therefore decided to use a cost-sharing rule based on a uniform distribution for simplicity.

## 3.5. The CWL Auction

Based on the definition of CWLs, we will now describe the CWL auction. The auction process is identical to Algorithm 1 and the DL auction, including the availability of last-and-final bids and the activity rule. However, the ask prices are diferent. Instead of the computation of the DLs on line 16 in Algorithm $^ { 1 , }$ CWLs are computed for some of the highest revenue coalitions that are currently losing.

In case some members of a losing coalition do not accept the CWL, then this coalition would also not become winning in the very next round, but the members (other than the ones who submitted a last-andfinal bid on a relevant package) can always update their bids in a new round. All new bids from the previous round are taken into account at the end of the round, and they can be the foundation for new coalitions to be built. Therefore, this process implicitly supports the collaborative search for a competitive equilibrium.

There are some degrees of freedom in how the auctioneer selects losing coalitions. The auctioneer could only select one or also a few disjoint losing coalitions in each round from the list of those losing coalitions with high revenue. How many losing coalitions are selected in each round depends on the size of the auction. Another implementation choice for the auctioneer is whether bidders are required to respond to a CWL immediately (i.e., in the next round) or not. For example, to proactively discourage free-riding behavior, the auctioneer may choose to select one losing coalition in each round, and require a response from each member of this coalition. This strict rule was not used in our experiments.

If more coalitions are provided with a CWL, we find that this can further reduce the number of auction rounds. In our experiments, where we are restricted to smaller auctions, we computed a CWL for every losing $b _ { i } ( S ) \in B _ { l } ^ { t }$ . This specific implementation leads to the fact that sometimes a given bid can be part of multiple coalitions. To determine minimal core prices and avoid coalitions having to pay too much, conservatively we selected the minimum across these ask prices across diferent coalitions: $\begin{array} { r } { \alpha _ { i } ( S _ { i } )  \operatorname* { m i n } _ { L \in \mathcal { L } } { \mathbf { C W L } _ { i } ^ { t } ( L , S _ { i } ) } + \epsilon . } \end{array}$

It is interesting to point out that finding the minimum $\mathrm { { m i n } } _ { L \in \mathcal { L } } \mathrm { { C W L } } _ { i } ^ { t } ( L , S _ { i } )$ can be directly computed as part of the computation of winning levels ${ \mathrm { W L } } ^ { t } ( i , \stackrel { \cdot } { S } ) = C A P ^ { t } ( { \mathcal { K } } ) - \hat { C } A P ^ { t } ( { \mathcal { K } } , S _ { i } )$ . The result of $C A P _ { i } ^ { t } ( \mathcal { K } , S _ { i } )$ returns the highest-revenue coalition with bidder i winning $S _ { i }$ . This provides all of the information necessary to compute the min $\mathsf { \Omega } _ { \mathsf { L } \in \mathcal { L } } \mathsf { C W L } _ { i } ^ { t } ( L , S _ { i } )$ for any of the cost-sharing functions to compute individual CWLs described in Section 3.4.

Selecting the lowest possible $\mathrm { C W L } _ { i } ^ { t }$ for each bidder comes at a cost. In some cases, a coalition might not win even if all members agree to the CWL ask prices. In other words, we intentionally avoid that bidders pay more than what would have been necessary to win at the potential expense of additional auction rounds. By contrast, if the highest CWL for a bundle across all coalitions, i.e., $\mathrm { m a x } _ { L \in \mathcal { L } } \mathrm { C W L } _ { i } ^ { t } ( L , S _ { i } ^ { L } )$ , was selected, then it could happen that members of the coalition pay more than what is necessary to become winning. In the simulations, the additional number of auction rounds caused by our proposed conservative pricing rule was very low, which is why we use it in our experiments.

## 3.6. Bidding Strategy and Bundle Selection

A bidding strategy in an auction involves two decisions in each round: which packages to bid on and how high a bidder should bid on the selected packages. Straightforward bidding (see Definition 3) is one such strategy, where bidders always bid on the package maximizing (absolute) payof at the ask prices. We have discussed that in a DL auction straightforward bidding is an ex post equilibrium at least for some types of valuations. Bidding straightforwardly would take hundreds of auction rounds (Schneider et al. 2010), and bidders with a positive cost for participating in a round are unlikely to bid straightforwardly. Moreover, straightforward bidding was not reported in earlier experiments (Schefel et al. 2012, Adomavicius et al. 2013); by contrast, the authors describe jump bidding and diferent forms of bundle selection.

In a CWL auction, an auctioneer aids the coordination of bidders by adequate information feedback. Although this coordination avoids unnecessary auction rounds, a losing coalition needs to outbid the winning coalition such that the process still leads to a competitive equilibrium. First, let us provide an illustrative example on how the information feedback in a CWL auction can help reduce the number of auction rounds.

Example 2. Consider the sale of 18 pieces of land (A–R) on a shoreline. One developer (bidder 1) needs three adjacent pieces of land for a small hotel, while the other developer (bidder 2) plans for a large resort and needs 15 adjacent pieces. Both compete against bidder 3, who is interested in all 18 pieces of land. Let us assume that, in the first round, bidder 1 submits XOR bids of e3 on bundles A–C, D–F, G–I, J–L, M–O, and P–R for which he has the same preference, while bidder 2 bids on A–O for e9, and bidder 3 on A–R for e20. The CWL for bidder 1’s bid on P–R will be e7, while the CWL for bidder 2’s bid will be e13 (using the uniform distribution sharing rule for simplicity). By contrast, the CWL for all other bundle bids for bidder 1 will be e20. Therefore, the CWL information can serve as a signal that, right now, bidder 1 can focus on bundle P–R. By contrast, with only DLs available, bidder 1 could not see the diference of P–R to his other five bundles of interest and might bid on other bundles (i.e., all DLs would be e3), which cannot become winning given the valuations. He could be trying to bid on these other packages over multiple rounds and increase the ask prices, but the allocation would not change. Furthermore, if WL information is available, the WL for P–R on the other hand would be e11, which indicates the entire cost that is needed to outbid bidder 3 without taking into account possible coalitions.

In the absence of reliable prior distributional information about the valuations of competitors in an online market, a rational bidder will not submit a last-andfinal bid below the CWL, because he does not have suficient information to decide whether the bid is just high enough such that he becomes winning in expectation.

To further emphasize this issue, in this section we use a simple complete-information model that highlights the strategic problem of bidders within a single round. The coordination problem for bidders within a round is far from trivial if the auctioneer just provides DL prices, as we have shown in Example 2. We use our stylized model to highlight (and provide the intuition for) the key strategic dificulty that bidders face in these auctions, and the role that the auctioneer plays in a CWL auction in aiding coordination of losing bidders.

3.6.1. A Complete Information Model. We model the strategic situation as a complete-information coordination game (Cooper 1999),<sup>1</sup> where bidders need to bid on complementary packages that together are high enough to outbid the current set of winners. In other words, bidders can realize mutual gains, but only by making mutually consistent decisions. As is typical in the auction literature, we assume a trusted auctioneer and refer to this environment as the complete information CWL auction model. Example 3 with two bidders and three items helps us illustrate the model.

Example 3. Suppose that the auctioneer in a CWL auction selects a single losing coalition L with two losing bidders 1 and 2 (row and column players, respectively, in Table 2) and three items (A, B, C). Both bidders are symmetric in that they are interested in the same two packages AB and C, and have identical valuations for them: e8 for AB and e4 for C. The losing bidders are interested to become winning in the next round. The two bidders have both bid on AB for e4 and C for e1 in previous rounds, but have been outbid by bidder 3 with a bid in round t on ABC for e8, which is his valuation. In this auction the losing bidders can either submit a minimum bid, which is their last bid on a package plus a bid increment (i.e., the DL auction ask price), or they bid on the CWL recommended by the auctioneer. With a bid increment of e0.5, both bidders need to bid at a minimum e4.5 for AB and e1.5 for C, which would not make them winning in the next round.

Table 2 shows the payof matrix of the normal-form game with complete information in round t. If the two losing bidders do not outbid the winning coalition with their bids, the payof in the next round is zero. If both bidders increase their bid by e2 there are two Nash equilibria with a positive payof. Without coordination, there is a mixed Nash equilibrium in this round, in which each player bids on AB with a probability of 2/3 and C with a probability of 1/3. The expected payof for each bidder is e2/3 as a result. Note that if the row bidder selects a strategy of one equilibrium and the column bidder selects the strategy of another equilibrium, then the bids will not constitute an equilibrium.

Table 2. Payof Matrix of a Normal-Form Coordination Game with Two Losing Bidders and Two Packages in Round t

<table><tr><td></td><td> $b(AB)=6$ </td><td> $b(C)=3$ </td><td> $b(AB)=5$ </td><td> $b(C)=2$ </td><td> $\cdots$ </td></tr><tr><td> $b(AB)=6$ </td><td>0,0</td><td>2,1*</td><td>0,0</td><td>0,0</td><td></td></tr><tr><td> $b(C)=3$ </td><td>1,2</td><td>0,0</td><td>0,0</td><td>0,0</td><td></td></tr><tr><td> $b(AB)=5$ </td><td>0,0</td><td>0,0</td><td>0,0</td><td>0,0</td><td></td></tr><tr><td> $b(C)=2$ </td><td>0,0</td><td>0,0</td><td>0,0</td><td>0,0</td><td></td></tr><tr><td> $\cdots$ </td><td></td><td></td><td></td><td></td><td></td></tr></table>

The auctioneer in a CWL auction resolves this equilibrium selection problem. For example, he provides a CWL price (including the increment of e0.5) of e6 for AB to bidder 1 (the row player), and e3 for C for bidder 2 (the column player). The cell is marked with $^ { \prime \prime \ast \prime \prime } \mathrm { i n }$ Table 2. So, in this coordination game, the auctioneer randomizes over both pure Nash equilibria and selects one equilibrium from the set of all equilibria. If both players accept the CWL, then the payof of the row player is e2 and the payof of the column player is e1, which is higher for both players than their payof in the mixed Nash equilibrium without the auctioneer. Therefore, it is in the interest of bidder 2 to bid on $C ,$ although his absolute payof would be higher in the equilibrium with him bidding on AB. Of course, there can also be situations where there is a unique Nash equilibrium such that this equilibrium maximizes payof for all participants. In those cases it is even easier to propose a CWL to a losing coalition.

The example only shows a part of the payof matrix assuming bidders are only interested in two packages and two prices. However, the payof matrix would grow very large for any auctions except small ones. The number of packages a bidder can bid on grows exponentially, and a bidder could submit many prices for each of these packages starting with the DL ask price. This would lead to a huge equilibrium selection problem, which further illustrates the dificulty of coordination in ascending combinatorial auctions with DLs only. McLennan and Berg (2005) showed that the mean number of all Nash equilibria in a bi-matrix game with only two players and z pure strategies for each player grows exponentially in z. With more bidders and items and no prior knowledge about the competitors, the likelihood of coordinating with all other bidders in a round goes to zero with a growing number of bidders and items. If bidders want to become winning in the next round, accepting a CWL maximizes their chances, because there are complementary bids of others.

3.6.2. Expected Payof Maximization and Coordinated Equilibria. We will now formalize the insights from Example 3 and show that the example describes a correlated equilibrium, a solution concept introduced by

Aumann (1987), where the auctioneer fulfills the role of a trusted party.

Definition 6 (Correlated Equilibrium). A correlated equilibrium is a probability distribution $\{ p _ { s } \}$ on the space of strategy profiles that obeys the following conditions: For each player i, and any two diferent strategies $b ,$ $b ^ { \prime }$ of $i ,$ conditioned on the event that a strategy profile with b as a strategy was drawn from the distribution, the expected utility of playing b is no smaller than that of playing b

$$
\sum_ {s \in S _ {- i}} (\pi_ {s b} ^ {i} - \pi_ {s b ^ {\prime}} ^ {i}) p _ {s b} \geq 0.
$$

A strategy profile is a vector of strategies (i.e., bids) of all players. By $S _ { - i }$ we denote the set of strategy profiles of all players except for $i . \operatorname { I f } s \in S _ { - i } ,$ sb denotes the strategy profile in which player i plays b and all other players play s. The inequalities show that if a strategy profile is drawn from the distribution $\{ p _ { s } \}$ and each player is told, privately, his own component of the outcome, and if furthermore all players assume that the others will follow the signal, then the expected profit of player i cannot be increased by switching to a diferent strategy $b ^ { \prime } .$

In the complete information CWL auction model the auctioneer is a trusted party who randomizes over the pure Nash equilibria, i.e., draws from the distribution $\{ p _ { s } \}$ in a correlated equilibrium. For instance, this probability distribution could be 0.5 for each of the two Nash equilibria described in Example 3. We draw on the correlated equilibrium concept in our model to show that a CWL maximizes expected payof for a bidder in this model (see Online Appendix A for the proof).

Proposition 2. Suppose a bidder wants to become a winner in a given round of the complete information CWL auction model, then accepting a CWL for a package maximizes expected payof in a given round.

There might be packages with higher absolute payof for a bidder in a round based on the minimum bid price (i.e., based on the standard DL ask price), but the likelihood of winning them is very low because of exponentially many packages and numerous possible prices for each package the bidders can chose from.

The complete-information model is an abstraction to highlight the central strategic problem, and is not meant to fully describe CWL auctions in reality. In the lab or in the field, the auctioneer does not have complete information. However, the auctioneer can select high-revenue coalitions based on estimates from the bid history, and historical bids often provide auctioneers with good signals about the preferences bidders have for diferent bundles. Also, in our experiments, we implemented the auctioneer to select more than a single coalition in each round to further speed up the auction. Still, the correlated equilibrium is a useful analogy when thinking about the role of an auctioneer and the value of the information he provides to the bidders throughout in a CWL auction.

As outlined in Section 1, straightforward bidders are also able to coordinate in a DL auction, and a competitive equilibrium arises. However, such a competitive equilibrium comes at the cost of a huge number of auction rounds. In DL auctions with straightforward bidders, all package values of losing bidders need to be revealed, and this might be an unrealistic assumption given the exponential number of packages bidders can bid on. By contrast, CWL auctions can lead to high eficiency in markets with many more objects, because bidders are able to coordinate more efectively.

In Section 4, we provide experimental results that demonstrate that bidders accept CWLs and, as a consequence, the number of auction rounds is reduced substantially, while eficiency is significantly higher than in a DL auction in the lab.

## 4. Experimental Design

Several ascending combinatorial auction formats have been analyzed in the past (see discussion in Section 2). An experimental comparison with all of these formats would be beyond the scope of a single paper. Because BACS auctions satisfy a strong solution concept (at least for a restricted set of bidder preferences) and, in particular, because the DL auction is a BACS auction that has been the focus of much recent research in information systems, the DL auction represents a natural candidate to compare against. In addition, the proposed CWL auction is an extension of the literature on DL auctions (Adomavicius and Gupta 2005, Petrakis et al. 2013, Adomavicius et al. 2013).

In what follows, we will introduce three diferent bidder value models for which we compare the DL and CWL auction formats. Another set of value models and the respective simulations are described in Online Appendix D. They yield the same results and, because of space constraints, in the main paper we only included those value models for which we conducted both computational simulation and lab experiments with human participants.

## 4.1. Value Models

We use three diferent value models (VMs) in our experiments. These are the Threshold (Thr) VM, the Mix VM, and the Symmetry (Sym) VM. The Sym VM is based on an earlier work by Adomavicius et al. (2013) in their experimental studies on DL and WL. We added the Thr VM and the Mix VM to understand if the results carry over to other environments. The Thr VM models a threshold problem with a single global bidder and several local bidders only interested in small packages. Such environments have received much attention, as they could lead to free-riding behavior as outlined in Section 1.

In addition to the value models described in this section, in Online Appendix D we provide numerical simulations with three additional value models, two with 18 and one with 9 items, which resemble the ones used in lab experiments by Schefel et al. (2011) and Goeree and Holt (2010). These value models are modeled after spectrum auction markets with regional licenses and real-estate markets. There is no significant diference in eficiency between the simulations, while the eficiency of the CWL auctions is significantly higher than that of the DL auctions in the lab experiments. In the lab and in simulations the number of bids and the number of auction rounds in CWL auctions are substantially reduced.

4.1.1. The Threshold Value Model. In this value model, we consider a market with a single global bidder and two local bidders facing a threshold problem. They compete for six items labeled A to F. The global bidder is defined to be single minded and has interest only in the bundle containing all six items. Each of the local bidders is interested in various bundles of smaller sizes, but the experimental subjects did not know the specific bundles that were of interest to other bidders. Bidders also did not have distributional information about the other bidders’ valuations before the auction. They only knew that two local bidders were competing against a global bidder. The bidder valuations for the individual bundles are drawn from uniform distributions based on prespecified intervals, which was not known by the bidders. Table 3 represents the basic bidder preferences and value distributions for all bundles. This model is designed in such a way that the local bidders could potentially overcome the threshold posed by the global bidder if they could coordinate and form a coalition containing either the bundles ABCD from bidder 1 and EF from bidder 2, or the bundles CDEF from bidder 1 and AB from bidder 2. Other combinations of package bids from bidder 1 and bidder 2 did not stand a chance of winning if the global bidder bids up to his true valuation.

4.1.2. The Mix Value Model. Similar to the threshold model, the mix value model was designed to analyze the ability of two local bidders to enter into a successful winning coalition that can outbid the global bidder. Compared to the threshold value model, the two local bidders have more bundles of interest, making a successful coalition more challenging.

In particular, we again have six items labeled A to F. The global bidder is only interested in the bundle containing all six items. The local bidders are interested in all six items and all bundles of size up to four items. For each local bidder, there exists a “preferred item”

Table 3. Preference Structure of the Threshold VM  
![](/api/attachments/BCHDEHUB/fulltext/images/1777fd4940679b3e96fce416f4fae31340a00769c2b29f3b5dbf1a63d4a85f28.jpg)  
Note. The global bidder is interested in one bundle only, while local bidder 1 and local bidder 2 are both interested in five diferent bundles each.

(which is chosen randomly) that has a higher value for that bidder than other items. We introduce local complementarities by implementing an additional (i.e., bonus) value of 10% for each adjacent item in a bundle.

The values for the individual bundles are randomly determined from diferent intervals, depending on the baseline draws for single-item valuations. In particular, for each bidder, we first determined the “preferred item,” for which the baseline draw is uniform from the range <sup>[</sup>90, 110<sup>]</sup>. The adjacent items to this preferred item then had valuations drawn uniformly in the range <sup>[</sup>40, 60<sup>]</sup>. Their neighboring items next had valuations drawn uniformly in the range <sup>[</sup>20, 30<sup>]</sup>, while the last remaining item, i.e., the item with the greatest distance from the preferred item, had a valuation drawn uniformly from <sup>[</sup>7, 17<sup>]</sup>. Once these single-item valuations were drawn for each bidder, the bundle valuations were computed, and a list of all valuations was provided to the subjects privately. Figure 1 shows an example of baseline draws for a local bidder in this setting. In this example, the bidder has a valuation of <sup>(</sup>90 <sup>+</sup> 45 <sup>+</sup> 20<sup>)</sup> <sup>·</sup> 1.2 <sup></sup> 155 <sup>·</sup> 1.2 <sup></sup> 186 for the bundle BCD, as this bundle contains two adjacent neighbors and, therefore, gets a 20% bonus. The number of bidders and the fact that there are two local and a global bidder were common knowledge among bidders. However, bidders did not know the preferred item for the other local bidders.

4.1.3. The Symmetry Value Model. This was one of the value models (setup 1) used by Adomavicius et al. (2013) to test and evaluate the impact of deadness and winning levels as price feedback in the lab. It allows us to compare our result to theirs, as it does not include random draws. In the Sym VM, bidders have equal strength in their valuations and there is no threshold problem as in Thr VM and Mix VM.

Figure 1. An Example for the Item Valuations for a Local Bidder in the Mix VM  
![](/api/attachments/BCHDEHUB/fulltext/images/d95d2e3ca35273249234f128ea723fe6d4f4924176bac3097a482995d5253a24.jpg)

There are again six items labeled A to F, which need to be auctioned among three bidders. A distinct item, designated the “preferred item,” is identified for each bidder participating in the auction. This item has the highest value (100 monetary units) for the bidder, with the value of each remaining item decreasing by 50% the further the item is from the preferred item. There are complementarities among items by creating superadditive valuations for bundles with adjoining items in them. This is accomplished by adding 10% to the additive valuation of the items for each adjoining item in the bundle, as in the Mix VM. Adomavicius et al. (2013) motivated this setting with the real-world scenario of real-estate properties around a lake, where local complementarities arise. To preserve the symmetry between bidders, we picked the items A, C, and E as preferred items for each of the three bidders, respectively, as in Adomavicius et al. (2013).

The identity of the preferred item is private information to each bidder. Bidders were not told how many other participants were in their specific auction, as in Adomavicius et al. (2013). Furthermore, while the rules for generating the valuations of the items were common knowledge, and each bidder in an auction knew the distribution of his own values, participants had no explicit knowledge of the valuations of other bidders as they did not know the respective preferred items of other bidders. Figure 2 shows an example for the private valuations for all bidders. In this example, bidder 1 has a valuation of <sup>(</sup>100 <sup>+</sup> 50<sup>)</sup> <sup>·</sup> 1.1 <sup>+</sup> 25 <sup></sup> 190 for the bundle ABE, as the bundle contains only one adjacent neighbor, and therefore gets a 10% bonus.

## 4.2. Treatments

We have used a fully factorial design with the two treatment variables, the auction format and the value model. Six sessions were conducted for each auction format in the Threshold, Symmetry, and Mix value model. Every session only used one auction format, and every session consisted of two waves with different value draws. During a session, the two waves were run in parallel with two groups of students. Each wave consisted of three auctions, one for each of the value models (i.e., Thr, Sym, and Mix). These three auctions were conducted sequentially, and in each wave we used a diferent sequential order of these three auctions to level out learning aspects. We used the same 12 waves for the first 6 sessions testing the DL auctions and for the last 6 sessions testing the CWL auctions to allow for better comparison. Table 4 provides an overview of the sessions and waves in the experiments. In this table we consider the three VMs (Thr, Sym, and Mix) together, as the respective auctions are always conducted together in a wave. Overall, there were 12 auctions per treatment combination (72 auctions in 6 treatments) and 72 total participants, each of which having participated in 3 auctions.

Figure 2. An Example for the Item Valuations for All Bidders in the Symmetry VM, Where the Preferred Item for Bidder 1 is A, for Bidder 2 is C, and for Bidder 3 is E  
![](/api/attachments/BCHDEHUB/fulltext/images/4ef2958719fecd52a71b35c20d03f3c48652af4a1bf79140b196d44dad2e3123.jpg)

The DL and CWL auction formats have been implemented as described in the previous section. In all experiments we used the same user interface and round-based auction process. We displayed WLs in the DL auction as additional information feedback (i.e., in addition to the ask prices based on DLs) to allow for better comparison to Adomavicius et al. (2013). We used a round-based auction process and did not determine the winners after every single submitted bid. Also, we used an XOR bid language throughout, because this bid language is able to express any valuations, i.e., it is fully expressive compared to an

OR bid language (Nisan 2006). The bid increment was 15 francs per item in the mix and symmetry VMs, and 3 francs per item in the threshold VM. We used francs as a name for our experimental currency. A bid increment of three francs per item means a bundle increment for a bundle containing three items is nine francs. We used a per-item bid increment rather than a bundle bid increment because a per-item bid increment takes bundle sizes into account when raising prices. Therefore, a per-item bid increment can help bidders more efectively to focus on smaller and, thus, more coalition-prone bundles during an auction. Also, as valuations in the threshold VM are generally smaller than those in the other two VMs, we scaled down the increment appropriately.

## 4.3. Procedures for Human Subject Experiments

All experiments were conducted from November 2012 to July 2013 with students at a major European university. Each session started with a presentation in which we explained the auction format to be used, the pricing rules, and the diferent value models in detail. This presentation was also provided to students as a handout. Then, subjects participated in one training auction to get to know the auction environment, the software, and the user interface. Afterward, we repeated the main rules, and subjects were asked questions in a quiz to make sure they understood all rules and were familiar with the auction procedure.

Table 4. Treatments, Sessions, and Participants for the Diferent Test Combinations

<table><tr><td>Treatment</td><td>AF</td><td>VM No. of sessions</td><td>Auctions per session</td><td>No. of auctions</td><td>No. of participants per auction</td><td>No. of participants</td></tr><tr><td>1</td><td>DL</td><td>Thr</td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>DL</td><td>Sym</td><td>6</td><td>6</td><td>36</td><td>3</td></tr><tr><td>3</td><td>DL</td><td>Mix</td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>CWL</td><td>Thr</td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>CWL</td><td>Sym</td><td>6</td><td>6</td><td>36</td><td>3</td></tr><tr><td>6</td><td>CWL</td><td>Mix</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>72</td><td></td><td>72</td></tr></table>

The number of auctions was announced in advance. The first auction round was not time restricted and only ended when every bidder announced they were ready to enter into the second round. In all subsequent rounds, bidders had at most five minutes to place their bids. This was perceived to be suficient by the participants. Bidder roles (e.g., global versus local) were randomly assigned for each auction to alleviate earning diferences across diferent bidders. Earnings were calculated by converting the experimental payof amounts to e by 3:1, i.e., bidders were paid on their economic performance in the auctions. The resulting earnings were between the minimum of e5 (i.e., showup fee) and the maximum of e50 per subject across all waves. Average earnings were e29, and the average duration of a wave was 1 hour and 19 minutes without the introductory part and without the training auction. This includes the time for breaks between auctions. In Online Appendix E, we provide screenshots of the web-based system used for the auction.

## 5. Simulation Results

In this section we present the results of numerical simulations based on two diferent bidding strategies: (i) straightforward bidders (s), as described earlier in the paper, and (ii) heuristic bidders (h). Heuristic bidders bid on 5 bundles in each round, where these bundles are randomly chosen from among their 10 best (i.e., payof-maximizing) bundles at that time. Heuristic bidders model bidder behavior that is based on observations from lab experiments reported in prior literature (Schefel et al. 2012). It models a “trembling hand,” where bidders want to bid on their best bundles by payof, but they make small mistakes. We have chosen 10 bundles, because in Schefel et al. (2012) it was shown that bidders typically focus on a small set of bundles, independent of the number of possible bundles in an auction. We have analyzed variations of these bidders, e.g., bidders who bid on their best three packages, but the diferences were minor. For our analysis, these artificial bidders serve as a baseline. In the lab experiments in Section 6, we analyze whether the differences between DL and CWL auctions carry over to the lab, where bidders are heterogeneous and follow diferent strategies on how they select packages or how they use jump bids.

Throughout, we use allocative eficiency E as a primary aggregate measure for comparing diferent auction mechanisms.<sup>2</sup> In addition, we measure an auctioneer’s revenue share R, which shows how the resulting total surplus is distributed between the auctioneer and the bidders.<sup>3</sup>

Optimal surplus describes the resulting revenue of the winner-determination problem if all valuations of all bidders were available, while actual surplus considers the true valuations for those packages of bidders selected by the auction. By contrast, auctioneer’s revenue used in the revenue distribution describes the sum of the bids selected by the auction, not their underlying valuations.

Table 5. Average Eficiency Achieved for All Simulated Bidder Behavior and Lab Results

<table><tr><td>Efficiency</td><td>AF</td><td>Strategy</td><td>Threshold VM (%)</td><td>Mix VM (%)</td><td>Symmetry VM (%)</td></tr><tr><td rowspan="4">Simulation results</td><td>DL</td><td>s</td><td>100.0</td><td>100</td><td>100.0</td></tr><tr><td>DL</td><td>h</td><td>100.0</td><td>99.1</td><td>100.0</td></tr><tr><td>CWL</td><td>s</td><td>100.0</td><td>99.8</td><td>100.0</td></tr><tr><td>CWL</td><td>h</td><td>100.0</td><td>98.9</td><td>100.0</td></tr><tr><td rowspan="2">Lab results</td><td>DL</td><td></td><td>96.3</td><td>97.2</td><td>98.3</td></tr><tr><td>CWL</td><td></td><td>100.0</td><td>98.1</td><td>100.0</td></tr></table>

Table 5 shows the eficiency results, averaged over all auction instances used in the lab experiments. In particular, we simulated the two diferent agent bidding strategies described above for each auction instance, which was later used in the lab. The average of these simulated values is then compared to results of the lab experiments using the three value models.

Overall, eficiency was very high in both the simulations and the lab experiments. Only the average eficiency in the Mix VM simulation was lower, as bidders had up to 56 bundles of interest, which makes the coordination problem harder. The Symmetry and the Threshold VM had 100% eficiency throughout, with the single exception of the DL auction in which the eficiency was significantly worse in the lab for the Threshold and the Mix VMs, as compared to the simulations, which might be due to the bundle selection and the jump bidding of bidders in the lab, which will be described in Section 6.

Table 5 provides an initial comparison of eficiency results between all simulated agent behaviors and real bidder behaviors in the lab. Although there are differences between the simulation and the lab, these diferences are minor at an aggregate level. As we will show, at an individual level, bidder behavior with respect to bundle selection and jump bidding exhibit some diferences compared to the simulations. Table 6 shows a comparison of all aggregate simulation results including the auctioneer revenue share, the number of rounds, and the number of bids submitted.

The diferences in eficiency between DL and CWL auctions across all simulations were insignificant (t-test, α <sup></sup> 0.05). Diferences in revenue were mostly significant but small. Most importantly, however, is that although there are only small diferences in eficiency and revenue between the DL and CWL auctions, the communication between the auctioneer and the bidders in the CWL auction is substantially reduced.

Table 6. Average Measures of Auction Performance: Aggregate and for Each of the Three Value Models: Threshold, Mix, and Symmetry

<table><tr><td>VM</td><td>AF</td><td>Strategy</td><td>Efficiency (%)</td><td>Revenue share (%)</td><td>No. of rounds (%)</td><td>No. of bids (%)</td></tr><tr><td>All</td><td>DL</td><td>s</td><td>100.0</td><td>97.3</td><td>100.0</td><td>100.0</td></tr><tr><td>All</td><td>CWL</td><td>s</td><td>99.9</td><td>98.1</td><td>37.0</td><td>45.3</td></tr><tr><td>All</td><td>DL</td><td>h</td><td>99.6</td><td>96.4</td><td>28.3</td><td>93.6</td></tr><tr><td>All</td><td>CWL</td><td>h</td><td>99.5</td><td>97.8</td><td>16.2</td><td>44.3</td></tr><tr><td>Threshold</td><td>DL</td><td>s</td><td>100.0</td><td>99.1</td><td>100.0</td><td>100.0</td></tr><tr><td>Threshold</td><td>CWL</td><td>s</td><td>100.0</td><td>99.7</td><td>40.9</td><td>48.4</td></tr><tr><td>Threshold</td><td>DL</td><td>h</td><td>100.0</td><td>98.5</td><td>32.0</td><td>98.1</td></tr><tr><td>Threshold</td><td>CWL</td><td>h</td><td>100.0</td><td>99.1</td><td>23.8</td><td>58.5</td></tr><tr><td>Mix</td><td>DL</td><td>s</td><td>100.0</td><td>97.4</td><td>100.0</td><td>100.0</td></tr><tr><td>Mix</td><td>CWL</td><td>s</td><td>99.8</td><td>98.0</td><td>31.8</td><td>42.9</td></tr><tr><td>Mix</td><td>DL</td><td>h</td><td>99.1</td><td>96.5</td><td>22.6</td><td>90.1</td></tr><tr><td>Mix</td><td>CWL</td><td>h</td><td>98.9</td><td>97.8</td><td>8.3</td><td>30.6</td></tr><tr><td>Symmetry</td><td>DL</td><td>s</td><td>100.0</td><td>74.3</td><td>100.0</td><td>100.0</td></tr><tr><td>Symmetry</td><td>CWL</td><td>s</td><td>100.0</td><td>79.6</td><td>50.8</td><td>35.7</td></tr><tr><td>Symmetry</td><td>DL</td><td>h</td><td>100.0</td><td>71.3</td><td>51.7</td><td>82.2</td></tr><tr><td>Symmetry</td><td>CWL</td><td>h</td><td>100.0</td><td>82.6</td><td>19.2</td><td>38.9</td></tr></table>

The average number of rounds is significantly smaller in the CWL auction, and so is the number of bids submitted throughout the auction. We normalized the numbers so that the DL auction with straightforward bidders describes 100% of the rounds and number of bids. Using these results as a conjecture, in Section 6 we investigate whether the same pattern of auction outcomes emerges in the lab experiments. Online Appendix D presents the results of a number of additional numerical simulations on larger value models, which are in line with the results presented in this section.

## 6. Experimental Results

Next, we will present our results of the lab experiments. First, we will look at the results at an aggregate level, concentrating on the comparison of the two auction formats DL and CWL, using metrics such as allocative eficiency and auctioneer’s revenue share as well as the number of bids submitted and rounds required by the bidders. For the pairwise comparisons of aggregate metrics we use the Wilcoxon rank sum test. In the second phase, we will analyze the bidders’ bundle selection and jump bidding behavior during the auctions.

Result 1 (High Eficiency of the Proposed CWL Auctions). The allocative eficiency of the CWL auction is significantly higher than that of the DL auction.

It is interesting to see that the eficiency of the CWL auction tends to be even higher than the already high eficiency of the DL auction. We have fitted a regression model with eficiency as the dependent variable and control for auction format, session, and value model. The coeficient for the DL auction format is actually significant (p-value 0.003) and negative, while the different value models did not have a significant influence on eficiency.

While we did not find signs of fatigue among the subjects in their responses after the auction or in the bid data, an influence of fatigue on the results can always be an issue. Fatigue could help explain lower eficiency in the DL auction, but the long auction durations in the DL auction are actually also a concern for applications in the field.

The auctioneer’s revenue share of the CWL auction equals that of the DL auction in the Thr VM, but is lower than the DL auction for the Mix and Sym VM. In the Sym VM bidders did not have to outbid a large bidder and the preferred items were disjoint, such that they could coordinate faster at lower prices. The aggregate results are presented in Table 7. Figure 3 provides box plots of the eficiency and revenue share.

The auctioneer’s revenue share is higher in the numerical simulations compared to those in the lab. This is because of the fact that, in the simulation, straightforward bidders reveal all valuations of all losing bundle bids truthfully, often using last-and-final bids. Also, heuristic bidders in the simulation reveal their preferences to a large degree. In the lab, subjects typically want to get a payof and sometimes drop out of the bidding process for a bundle before they reveal their true valuation.

Note that the revenue share in the Sym VM is lower than in the other two value models. In the Thr and Mix VMs, the smaller bidders need to outbid the global bidder, who drives up prices, which leads to a higher revenue share. By contrast, in the Sym VM, it can happen that bidders coordinate very early leading to low prices and consequently a low revenue for the auctioneer. This is also a reason for the higher variance in revenue in the Sym VM.

Table 7. Average Aggregate Measures of Auction Performance in All Eight Combinations of Auction Formats and Value Models

<table><tr><td>AF</td><td>VM</td><td>E (%)</td><td>R (%)</td><td>Avg. no. of all bids</td><td>Avg. bundles</td><td>Avg. bid improvements</td><td>Avg. time (min.)</td><td>Avg. no. of rounds</td></tr><tr><td>DL</td><td>Thr</td><td>96.3</td><td>80.8</td><td>30.0</td><td>4.9</td><td>8.5</td><td>14.7</td><td>8.3</td></tr><tr><td>CWL</td><td>Thr</td><td>100.0</td><td>80.8</td><td>19.2</td><td>4.9</td><td>3.1</td><td>10.6</td><td>5.4</td></tr><tr><td>DL</td><td>Mix</td><td>97.2</td><td>89.8</td><td>114.0</td><td>29.3</td><td>25.7</td><td>37.0</td><td>15.3</td></tr><tr><td>CWL</td><td>Mix</td><td>98.1</td><td>88.4</td><td>83.8</td><td>29.3</td><td>10.9</td><td>25.3</td><td>9.4</td></tr><tr><td>DL</td><td>Sym</td><td>98.3</td><td>78.4</td><td>166.6</td><td>31.4</td><td>22.6</td><td>45.8</td><td>13.6</td></tr><tr><td>CWL</td><td>Sym</td><td>100.0</td><td>63.8</td><td>116.6</td><td>29.7</td><td>8.8</td><td>28.7</td><td>10.5</td></tr><tr><td> $DL^A$ </td><td>Sym</td><td>93.5</td><td>65.3</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td></tr></table>

Note. Superscript A refers to results from Adomavicius et al. (2013).

We have included the eficiency and revenue results from setup 1 (Sym VM) in the experiments by Adomavicius et al. (2013). Note that even though we used the same value model, the experiments are not fully comparable because Adomavicius et al. (2013) used a continuous auction and a bid increment of one monetary unit, i.e., not a round-based format with a bid increment of 15 monetary units and lastand-final bids. They also used an OR bidding language instead of an XOR bid language, but this should not matter in the experiments as the valuations in the Sym VM are superadditive. We conjecture that the round-based auction process has advantages for convergence, because bidders do not get updates in the prices and allocations continuously. Instead, they receive new prices after each round. As this information does not change until the round is over, this might lead to a more structured way of decision making. Adomavicius et al. (2013) analyzed an online environment where bidders join throughout the auction and such a round-based mechanism might not be possible. Detailed results of individual auctions can be found in Online Appendix B.

Result 2 (Fast Convergence of the Proposed CWL Auctions). In the CWL auction, the number of bids submitted, the time to finish the auction, and the number of rounds was substantially lower than in the DL auction.

As in the numerical simulations, significantly less communication was required to achieve high eficiency. We provide the average number of all bids per auction in Table 7. In addition, we provide the average number of bundles that the small bidders bid on (avg. bundles), and their average number of bundle bids improving a starting bundle bid throughout the auction (avg. bid improvements). We exclude the big bidder, as he is only interested in one bundle and, thus, only bids on and improves this one bundle. Interestingly, the number of average bundles is identical or similar in all value models, meaning that in both auction formats small bidders bid on a similar number of new bundles, mostly in the first rounds of the auctions. By contrast, the number of average bid improvements was much lower in the CWL auction than in the DL auction across all three value models, suggesting that the CWL format enabled small bidders to improve their bundle bids in a much more structured and focused way. Finally, we report the average auction duration time in minutes and the average number of bidding rounds required—these numbers are significantly higher in the DL auction. It is particularly interesting to see that the savings in the average time increase with the complexity of the value models; i.e., the CWL format saves 4.1 minutes on average in the Thr VM, 11.7 minutes in the more complex Mix VM, and 17.1 minutes in the Sym VM.

Figure 3. Distribution of Allocative Eficiency in Diferent Treatment Groups (Left Panel); Distribution of Revenue Share in Diferent Treatment Groups (Right Panel)  
![](/api/attachments/BCHDEHUB/fulltext/images/ef267aed081897acb416dd7a32971bf3d3b498544bd81701c1bde95475e8a1ff.jpg)

![](/api/attachments/BCHDEHUB/fulltext/images/acb4f1c19e2cebc8bce8dfc0228cb235429824461b142c9690100a4b131ea1b9.jpg)

In the simulations, the number of bids in the CWL auctions was mostly less than half of those submitted in the DL auction. The number of bids was also reduced substantially in the CWL auctions in the lab, and CWL auctions took 64%–74% of the bids in the DL auction. Diferences from the simulation can be explained by the use of jump bids in the DL auction and the deviations from straightforward bidding—these characteristics are representative of human bidding behavior. In both the numerical simulations and the lab experiments we used the same bid increments, and lastand-final bids were available to mitigate the potential eficiency losses due to bid increments.

Finally, we look at the threshold problem posed by the big bidder in the value models Thr and Mix.

Result 3. In the Thr VM, small bidders always find the eficient allocation in a CWL auction in those auctions where a coalition of small bidders is eficient. By contrast, in the DL auction 40% of these auctions are not eficient, i.e., in 40% of the DL auctions where a coalition of small bidders should have won in the eficient allocation, the big bidder won instead. In the Mix VM, there was no significant diference among the auction formats.

In Figure 4 we show the percentage of auctions where an eficient allocation favored a coalition of small bidders. Of those auctions, we show the percentage where a coalition of small bidders won with the 100% eficient allocation or with an allocation that was not 100% eficient, and where the threshold bidder (“big” bidder) won instead. There was a large number of possible allocations with the small bidders winning in the Mix VM compared to the Thr VM. This is the reason why the auctions never resulted in the 100% optimal solution in the Mix VM, but only in the solutions that were close to optimal.

We will also report on bundle selection and jump bidding, because both describe bidder strategies and both can influence the eficiency and revenue of an auction. Bundle selection in the lab varied a lot across

Figure 4. Auctions Where the Small Bidders Won in a 100% Eficient or an Ineficient Allocation, or They Lost to the Large Bidder, as Percentages of the Number of Auctions Where the Small Bidders Should Have Won in an Eficient Allocation  
![](/api/attachments/BCHDEHUB/fulltext/images/f7c51911e4762a9c70417fcc3fe04ed4427f45c397a9abf3694776551d49efed.jpg)  
bidders and was diferent from straightforward or heuristic bidder strategies used in the simulations.

Result 4. In the Mix and Sym VMs with more than 50 or 60 bundles of interest, respectively, bidders submitted bids on 20 to 25 packages in the auctions (median). The number of packages varied significantly across bidders. A high payof and a high valuation of a package relative to other bundles have a positive impact on the likelihood of a bidder selecting relevant bundles in both auction formats.

Figure 5 shows the number of bundles on which bidders submitted bids in all value models. While in the Thr VM there are only 5 bundles of interest for the small bidders, and they typically bid on all of them, the number of possible bundles of interest for small bidders in the Mix VM is 56, and in the Sym VM it is 63 for all bidders, and bidders typically bid only on a subset of possible bundles.

We also analyzed significant covariates for bundle selection using a logistic regression. For this, we generated a table of all bundles with a positive payof (i.e., relevant bundles) that a bidder could have bid on in each round. The dependent variable describes whether a given relevant bundle has been selected by the bidder or not (i.e., whether the bidder submitted a bid

Figure 5. Average Number of Bundles Evaluated by Small Bidders Relative to All Possible Numbers of Bundles for Them, Indicated by Numbers in Parentheses  
![](/api/attachments/BCHDEHUB/fulltext/images/8dee81c9e55248dee45b382f54b7fced4359b596ada24f7bd0ae0ab100e213cb.jpg)

on a given bundle with a positive payof). The model includes covariates such as the auction format, rank of a bundle by valuation, and rank of a bundle by payof in a round. We used bidder ID dummy variables to control for fixed efects. We also control for the round of the auction, the number of the auction within an experimental session, and the value model. All covariates were significant. The probability of a bundle being selected decreases with a lower rank by payof or a lower rank by valuation (Table 8). In the Thr VM bidders have a higher likelihood to bid on a bundle, while in the Sym VM bidders have a lower likelihood, compared to the Mix VM. This is induced by the comparatively low number of bundles of interest (i.e., five) in the Thr VM, and vice versa, in the Sym VM. Most importantly, there are also significant bidder-specific idiosyncrasies, as the dummy variables for Bidder ID revealed. Overall, payof influenced the bid selection, but the analysis indicates that pure straightforward bidding cannot fully explain the bidding behavior, and bidder idiosyncrasies matter. This is in line with earlier experimental work on bidder idiosyncrasies in the bundle selection in BACS auctions and the various factors influencing this selection (Schefel et al. 2012).

Table 8. Logistic Regression of the Bidder’s Likelihood to Bid on a Bundle

<table><tr><td></td><td>Estimate</td><td>Std. error</td><td>z value</td><td>Pr(&gt;|z|)</td></tr><tr><td>(Intercept)</td><td>-0.011</td><td>0.151</td><td>-0.075</td><td>0.940</td></tr><tr><td>DL auction</td><td>-0.747</td><td>0.197</td><td>-3.786</td><td>0.000</td></tr><tr><td>Rank by value</td><td>-0.018</td><td>0.001</td><td>-17.344</td><td>0.000</td></tr><tr><td>Rank by payoff</td><td>-0.010</td><td>0.001</td><td>-7.396</td><td>0.000</td></tr><tr><td>Auction round</td><td>-0.219</td><td>0.005</td><td>-40.596</td><td>0.000</td></tr><tr><td>Auction no. in session</td><td>-0.073</td><td>0.027</td><td>-2.704</td><td>0.007</td></tr><tr><td>Sym VM</td><td>-0.231</td><td>0.045</td><td>-5.152</td><td>0.000</td></tr><tr><td>Thr VM</td><td>1.055</td><td>0.077</td><td>13.664</td><td>0.000</td></tr><tr><td>Bidder ID</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>Null deviance</td><td>35,533</td><td colspan="3">on 68,386 deg. of freedom</td></tr><tr><td>Residual deviance</td><td>29,451</td><td colspan="3">on 68,303 deg. of freedom</td></tr><tr><td>AIC</td><td>29,619</td><td></td><td></td><td></td></tr></table>

Result 5. Bidders in the CWL auction explore more bundles in the initial rounds of the auctions, but they submit fewer bids in later rounds.

Table 7 includes statistics on the average number of bundles that small bidders bid on (avg. bundles) and the number of bundle bids improving a starting bundle bid throughout the auction (avg. bid improvements). Figure 6 shows the average submissions of new bids and improved bids for all three value models over time. This figure shows a consistent progress for bid submissions both for the new bundles and the improved bids on the previous bundles. In all value models, new bids are mostly submitted during the first 10%–20% of the auction process, with bidders generally submitting new bids for more rounds in the CWL auction compared to the DL auction. Much of the coordination takes place in these initial rounds. By contrast, bidders in the CWL auction need to submit fewer bids on bundles that they have already bid on (i.e., improved bids “Imp”) and bidding is more focused.

Bidders were allowed to submit bids that are higher than the ask price in both auctions. Such jump bids represent a possibility to signal about high-valued packages, which can become part of a coalition of winning bidders. We wanted to understand how bidders use jump bidding (because high jump bids could impact revenue and also eficiency) and whether we can find diferences between the two auction formats.

Result 6. Bidders submitted most jump bids in the first half of the auction rounds. There was no significant diference in the proportion of jumps in both auction formats across the value models.

The bar chart in Figure 7 provides an overview regarding what proportion of jump bids was submitted in the first, second, third, and fourth quarter of the auctions on average. It shows that in both auction formats the majority of jump bids are submitted in the first quarter of the auction. We conjecture that bidders try to signal packages of high value in the early rounds and find bidders interested in complementary packages this way. They submit fewer jump bids toward the end, where bidders only focus on a few bundles that they are trying to win.

Overall, there was heterogeneity in the number of package bids a bidder selected in each round and in the number of jump bids. The high eficiency in the auctions can be seen as an indicator for robustness against these diferences in bidding behavior.

Figure 6. Average Bid Submission Progress During the Auction in the Thr, Mix, and Sym VM  
![](/api/attachments/BCHDEHUB/fulltext/images/9f7135934b0f2ded50dffa511b3b73f0bc3a6fa2ee09cd219404e609e759fffc.jpg)

![](/api/attachments/BCHDEHUB/fulltext/images/a3920f6baff62284ec88c6cf1262171901b8445d70fd445cc039af3c6ca1b435.jpg)

![](/api/attachments/BCHDEHUB/fulltext/images/d54b2f7bc6cf4cfb60d810720a22e8ffa364d0ca680d5ab5107a8ab3fefb867b.jpg)

Figure 7. Number of Jumps in the First to Fourth Quarter of the Auction Rounds  
![](/api/attachments/BCHDEHUB/fulltext/images/1c7182ee48121ebaa5ac26c75a8f7480f4d4696cc61c1689053cfe6a88812338.jpg)

We also ran some lab experiments with instances of a large value model with 18 items and found qualitatively similar results. Eficiency was higher than 99% for the DL and CWL auctions, but the number of bids and rounds in the latter were substantially reduced. Results are reported in Online Appendix C.

## 7. Conclusions

The design of eficient multiobject auctions is a fundamental problem with many applications in e-sourcing and other domains. Ascending combinatorial auctions do not require bidders to reveal valuations on exponentially many packages as in sealed-bid auctions, but rather allow bidders to discover winning packages iteratively, which is preferred to sealed-bid auctions (such as the Vickrey–Clarke–Groves mechanism) in many online markets. The main strategic challenge in ascending combinatorial auctions is coordination: How can bidders find the right packages from a large set of possible alternative packages, which together with bids of other bidders could become a winning coalition? This type of coordination among losing bidders has largely been ignored, but it is arguably a pivotal problem for bidders in larger online combinatorial auctions.

Our approach leverages information about losing coalitions, which can be collected by the auctioneer throughout the auction. Coalitional winning levels are provided in each auction round to help losing bidders coordinate implicitly and outbid a coalition of standing winners. They provide an implicit proposal on how much to bid to become winning jointly. Aside from a theoretical characterization of this auction format using intuitions from a complete information model and the correlated equilibrium concept, the results of the numerical simulations and the corresponding lab experiments with realistic value models indicate substantial savings in the number of auction rounds and bids, and even higher eficiency in the lab. This type of information feedback helps bidders coordinate with much less communication, which makes combinatorial auctions a viable mechanism in many more practical applications. The results provide substantial contributions to a recent stream of information systems literature focusing on information feedback design in multiobject auctions.

We would like to note that the proposed auction mechanism has been designed with online markets in mind, i.e., markets with little or no distributional information available publicly about other bidders valuations and where rational bidders typically do not have incentives to deviate from truthful bidding. The empirical performance of this auction format in numerous experiments with real bidders provides evidence that the proposed coalition-based pricing mechanism indeed facilitates the intended performance improvements, e.g., substantially accelerated convergence with high eficiency. However, it has been well documented that strategic bidder behavior does occur in numerous settings (free riding, jump bids, sniping, etc.), especially where some information about valuations of other bidders is available or can be learned through repeated interactions. For example, if bidders had precise information about the preferences of their competitors, then strategic bidders have incentives to manipulate (unless the auctioneer uses a VCG mechanism). However, in a combinatorial auction with exponentially many packages and many bidders, this would presume the availability of a lot of information. In summary, it is important for an auctioneer to understand the information available to bidders in a market before deciding on a specific auction format.

## Acknowledgments

The authors thank Markus Kraft and Christian Kroemer for valuable help on the paper.

## Endnotes

<sup>1</sup> Multiobject auctions are often modeled as complete information games to understand the special case where a bidder has all possible information to manipulate auction outcomes (Bernheim and Whinston 1986, Ausubel 2006, Day and Milgrom 2008).

<sup>2</sup> We measure eficiency as E <sup></sup> (actual surplus/optimal surplus) <sup>×</sup> 100%.

<sup>3</sup> We measure auction revenue share as R <sup></sup> (auctioneer’s revenue/ optimal surplus) <sup>×</sup> 100%.

## References

Adomavicius G, Gupta A (2005) Toward comprehensive real-time bidder support in iterative combinatorial auctions. Inform. Systems Res. 16(2):169–185.

Adomavicius G, Curley S, Gupta A, Sanyal P (2013) Impact of information feedback in continuous combinatorial auctions: An experimental study of economic performance. MIS Quart. 37(1): 55–76.

Aumann RJ (1987) Correlated equilibrium as an expression of Bayesian rationality. Econometrica: J. Econometric Soc. 57(1):1–18.

Ausubel L (2006) An eficient dynamic auction for heterogeneous commodities. Amer. Econom. Rev. 96(3):602–629.

Ausubel L, Milgrom P (2006a) Ascending proxy auctions. Cramton P, Shoham Y, Steinberg R, eds. Combinatorial Auctions (MIT Press, Cambridge, MA), 79–98.

Ausubel L, Milgrom P (2006b) The lovely but lonely Vickrey auction. Cramton P, Shoham Y, Steinberg R, eds. Combinatorial Auctions (MIT Press, Cambridge, MA), 17–40.

Bernheim BD, Whinston MD (1986) Menu auctions, resource allocation, and economic influence. Quart. J. Econom. 101(1):1–31.

Bichler M, Gupta A, Ketter W (2010) Designing smart markets. Inform. Systems Res. 21(4):688–699.

Bichler M, Shabalin P, Pikovsky A (2009) A computational analysis of linear-price iterative combinatorial auctions. Inform. Systems Res. 20(1):33–59.

Bichler M, Shabalin P, Wolf J (2013) Do core-selecting combinatorial clock auctions always lead to high eficiency? An experimental analysis of spectrum auction designs. Experiment. Econom. 16(4):511–545.

Bikhchandani S, Ostroy JM (2002) The package assignment model. J. Econom. Theory 107(2):377–406.

Cooper R (1999) Coordination Games (Cambridge University Press, Cambridge, UK).

Cramton P, Shoham Y, Steinberg R, eds. (2006) Combinatorial Auctions (MIT Press, Cambridge, MA).

Day R, Milgrom P (2008) Core-selecting package auctions. Internat. J. Game Theory 36(3):393–407.

de Vries S, Schummer J, Vohra R (2007) On ascending Vickrey auctions for heterogeneous objects. J. Econom. Theory 132(1):95–118.

Dehez P (2007) Fair division of fixed costs defines the Shapley value. Technical report, University of Louvain, Louvain-la-Neuve, Belgium. http://dx.doi.org/10.2139/ssrn.970910.

Goeree J, Holt C (2010) Hierarchical package bidding: A paper and pencil combinatorial auction. Games Econom. Behav. 70(1): 146–169.

Goeree J, Lien Y (2016) On the impossibility of core-selecting auctions. Theoret. Econom. 11(1):41–52.

Guler K, Bichler M, Petrakis I (2016) Ascending combinatorial auctions with risk averse bidders. Group Decision Negotiation 25(3):609–639.

Krishna V, ed. (2002) Auction Theory (Elsevier Science, San Diego).

Kwasnica T, Ledyard JO, Porter D, DeMartini C (2005) A new and improved design for multiobjective iterative auctions. Management Sci. 51(3):419–434.

Levin J, Skrzypacz A (2016) Properties of the combinatorial clock auction. Amer. Econom. Rev. 106(9):2528–2551.

Leyton-Brown K, Nudelman E, Shoham Y (2006) Empirical hardness models for combinatorial auctions. Cramton P, Shoham Y, Steinberg R, eds. Combinatorial Auctions (MIT Press, Cambridge, MA), 479–504.

McLennan A, Berg J (2005) Asymptotic expected number of Nash equilibria of two-player normal form games. Games Econom. Behav. 51(2):264–295.

Nisan N (2006) Bidding languages. Cramton P, Shoham Y, Steinberg R, eds. Combinatorial Auctions (MIT Press, Cambridge, MA), 215–232.

Nisan N, Segal I (2006) The communication requirements of eficient allocations and supporting prices. J. Econom. Theory 129(1): 192–224.

Parkes D (2006) Iterative combinatorial auctions. Cramton P, Shoham Y, Steinberg R, eds. Combinatorial Auctions (MIT Press, Cambridge, MA), 41–78.

Parkes D (2007) Online mechanisms. Nisan N, Roughgarden T, Tardos E, Vazirani V, eds. Algorithmic Game Theory (Cambridge University Press, New York), 411–439.

Parkes D, Ungar LH (2000) Iterative combinatorial auctions: Theory and practice. Kautz H, Porter B, eds. 17th Natl. Conf. Artificial Intelligence <sup>(</sup>AAAI-00<sup>)</sup> (AAAI Press, Austin, TX), 74–81.

Petrakis I, Ziegler G, Bichler M (2013) Ascending combinatorial auctions with allocation constraints: On game-theoretical and computational properties of generic pricing rules. Inform. Systems Res. 24(3):768–786.

Rothkopf MH, Pekeč A, Harstad RM (1998) Computationally manageable combinatorial auctions. Management Sci. 44(8): 1131–1147.

Sano R (2012) Non-bidding equilibrium in an ascending coreselecting auction. Games Econom. Behav. 74(2):637–650.

Schefel T, Ziegler A, Bichler M (2012) On the impact of package selection in combinatorial auctions: An experimental study in the context of spectrum auction design. Experiment. Econom. 15(4): 667–692.

Schefel T, Pikovsky A, Bichler M, Guler K (2011) An experimental comparison of linear and non-linear price combinatorial auctions. Inform. Systems Res. 22(2):346–368.

Schneider S, Shabalin P, Bichler M (2010) On the robustness of nonlinear personalized price combinatorial auctions. Eur. J. Oper. Res. 206(1):248–259.

Shoham Y, Leyton-Brown K (2009) Multiagent Systems: Algorithmic, Game-Theoretic, and Logical Foundations (Cambridge University Press, Cambridge, UK).

Wilson R (1987) Game-theoretic analyses of trading processes. Advances in Economic Theory: Fifth World Congress (Cambridge University Press, Cambridge, UK).
