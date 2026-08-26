---
otero_id: 8276
otero_key: "SMAPMR22"
title: "Ascending Combinatorial Auctions with Allocation Constraints: On Game Theoretical and Computational Properties of Generic Pricing Rules"
authors: "Ioannis Petrakis; Georg Ziegler; Martin Bichler"
year: "2013"
journal: "Information Systems Research"
doi: "10.1287/isre.1120.0452"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/SMAPMR22/fulltext/images/12fb09b48c4ef396724744b6e734c7af66428ed81b53fe7e602f8b5e84fd61c0.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Ascending Combinatorial Auctions with Allocation Constraints: On Game Theoretical and Computational Properties of Generic Pricing Rules

Ioannis Petrakis, Georg Ziegler, Martin Bichler

## To cite this article:

Ioannis Petrakis, Georg Ziegler, Martin Bichler (2013) Ascending Combinatorial Auctions with Allocation Constraints: On Game Theoretical and Computational Properties of Generic Pricing Rules. Information Systems Research 24(3):768-786. http:// dx.doi.org/10.1287/isre.1120.0452

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2013, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/SMAPMR22/fulltext/images/54f08600c778082416579e58bc93717f27d32188f023e94d5f89a3642ea0176d.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Ascending Combinatorial Auctions with Allocation Constraints: On Game Theoretical and Computational Properties of Generic Pricing Rules

Ioannis Petrakis, Georg Ziegler, Martin Bichler

Decision Sciences and Systems, Department of Informatics, Technische Universität München, 80333 Munich, Germany {petrakis.ioannis@mytum.de, zieglerg@in.tum.de, bichler@in.tum.de}

ombinatorial auctions are used in a variety of application domains, such as transportation or industrial procurement, using a variety of bidding languages and different allocation constraints. This flexibility in the bidding languages and the allocation constraints is essential in these domains but has not been considered in the theoretical literature so far. In this paper, we analyze different pricing rules for ascending combinatorial auctions that allow for such flexibility: winning levels and deadness levels. We determine the computational complexity of these pricing rules and show that deadness levels actually satisfy an ex post equilibrium, whereas winning levels do not allow for a strong game theoretical solution concept. We investigate the relationship of deadness levels and the simple price update rules used in efficient ascending combinatorial auction formats. We show that ascending combinatorial auctions with deadness level pricing rules maintain a strong game theoretical solution concept and reduce the number of bids and rounds required at the expense of higher computational effort. The calculation of exact deadness levels is a ç<sup>P</sup> -complete problem. Nevertheless, numerical experiments show that for mid-sized auctions this is a feasible approach. The paper provides a foundation for allocation constraints in combinatorial auctions and a theoretical framework for recent Information Systems contributions in this field.

Key words: electronic markets and auctions; economics of IS; electronic commerce; decision support systems History: Chris Dellarocas; Senior Editor; Karthik Kannan, Associate Editor. This paper was received on July 27, 2011, and was with the authors 7 weeks for 2 revisions. Published online in Articles in Advance December 20, 2012.

## 1. Introduction

Combinatorial auctions (CAs) allow selling to or buying from a set of heterogeneous items to or from multiple bidders. Bidders can specify package bids; i.e., a bid price is defined for a subset of the items for auction (Cramton et al. 2006). The price is only valid for the entire package and the package is indivisible. For example, in a CA a bidder might want to buy items x, y, and z for a package price of \$100, which might be more than the total of the prices for the items sold individually. CAs can be seen as generic mechanisms for multi-object markets because they allow expressing complex preferences such as items being substitutes or complements for bidders. They have found application in a variety of domains such as the auctioning of spectrum licenses (Cramton 2009), truck load transportation (Caplice 2007), bus routes (Cantillon and Pesendorfer 2006), or industrial procurement (Bichler et al. 2006).

The design of efficient CAs has drawn considerable attention because they raise fundamental questions on pricing and efficiency in multi-object markets. If bidders revealed their preferences truthfully, the auctioneer only had to solve an optimization problem to find the efficient allocation. Typically bidders have incentives to speculate and deviate from truthful bidding. The Vickrey-Clarke-Groves (VCG) mechanism has therefore been a significant contribution in auction theory. Green and Laffont (1977) proved that the sealed-bid VCG mechanism is the unique auction mechanism in which truthful bidding is a dominant strategy. In spite of this powerful result, this mechanism has a number of practical problems when used in multi-object markets (Ausubel and Milgrom 2006b, Rothkopf 2007). Also, many auctioneers want to have a transparent open-cry bidding process rather than a sealed-bid format. For example, almost all spectrum auctions organized throughout the world are iterative auctions with multiple rounds.

It is interesting to understand whether there are also iterative CA formats, which also satisfy strong game theoretical solution concepts, that limit incentives for speculation. Preference elicitation in iterative auctions can invalidate dominant strategy equilibria existing in a single-step version of a mechanism (Conitzer and Sandholm 2002), but ex post equilibria can be achieved that also do not require agents to speculate about other bidders’ valuations (Shoham and Leyton-Brown 2009). Much progress has been made on this question in the theoretical literature in the recent years. iBundle (Parkes and Ungar 2000), the Ascending Proxy Auction (APA; Ausubel and Milgrom 2002), and dVSV (de Vries et al. 2007) lead to an efficient allocation, if bidders bid straightforwardly,<sup>1</sup> which is an ex post equilibrium as long as the buyer submodularity condition holds for all valuations. Buyer submodularity is a restriction on the valuations of bidders; it defines that bidders are more valuable when added to a smaller coalition. It is interesting that such a strong solution concept is possible in iterative CAs, even though the result does not hold for general valuations. This line of work is heavily based on duality theory in linear programming.

All these auction formats use nonlinear and personalized ask prices and increase these ask prices for losing bids by a minimum increment, which causes a large number of auction rounds (Schneider et al. 2010).<sup>2</sup> The APA uses proxy bidders in order to cope with the large number of auction rounds and to make sure that bidders follow the straightforward strategy, which turns the mechanism into a sealed bid auction. Apart from these theoretical advances, a number of linear or item-price auction formats have been developed. These include versions of the combinatorial clock auction (Porter et al. 2003, Bichler et al. 2011), where item-level ask prices rise whenever there is overdemand on an item, and also the family of auction formats with pseudo-dual linear ask prices (Kwasnica et al. 2005, Bichler et al. 2009). As of yet, there is little theory on equilibrium bidding strategies in such auctions, although lab experiments yielded high levels of allocative efficiency.

Adomavicius and Gupta (2005) introduce different pricing rules for CAs. Pricing rules refer to functions by which the auctioneer determines ask prices based on bids submitted in the auction. Winning levels (WLs) describe the lowest possible bid that would win if no other bids are submitted, whereas deadness levels (DLs) are a lower bound to bids that still can become winning in the course of the auction. DLs and WLs describe natural bounds and interesting feedback for a losing bidder. Although there is no rationale to bid below the DL, bidding at the WL could be rational in some situations, where a bidder is the only one able to outbid a winning coalition of bidders. WLs are equivalent to the minimal winning bids described by Rothkopf et al. (1998). These pricing rules are independent of the allocation rules, and laboratory experiments with respective auction formats yielded high levels of efficiency (Adomavicius et al. 2012). They are very generic and can be considered a fundamental contribution in the emerging Information Systems literature on decision support in smart markets (Xia et al. 2004, Bapna et al. 2007, Guo et al. 2007, Bichler et al. 2009, Scheffel et al. 2011, Bichler et al. 2010) and in the general literature on CAs.

The analysis in Adomavicius and Gupta (2005) is focused on a pure OR bidding language and assumes no substitutes valuations. OR bids can represent only bids that do not have any substitutabilities, i.e., purely additive and superadditive valuations (Nisan 2006). Also, this initial work did not analyze equilibrium strategies in such auctions. However, DLs and WLs introduce a very generic concept that can be applied to any bidding language. It is natural to ask how these generic pricing rules can be defined for auctions with XOR bidding languages and other types of allocation constraints as well and which game theoretical solution concepts can be satisfied. Auctions with strong game theoretical solution concepts are strategically easier for bidders because there is no need to speculate about other bidders’ valuations. This makes bidding strategically easy and respective auction formats are more likely to lead to high efficiency.

In this paper, we introduce WLs and DLs for general CAs, which allow for XOR bids and other constraints. Auctioneers use various types of allocation constraints to limit the number of winners or the number of items allocated to one bidder or to a group of bidders. Such constraints are actually the rule rather than the exception in application domains such as industrial procurement (Bichler et al. 2006, Sandholm and Suri 2006) or transportation (Caplice 2007). But they are typically not considered in the literature on iterative CAs. The beauty of DLs and WLs is that their definition is independent of the type of allocation constraints used in the winner determination. The resulting theory is applicable to a much broader set of real-world applications, where allocation constraints play a considerable role. We will refer to ascending CAs allowing for different types of allocation constraints as flexible combinatorial auctions (FCAs) in this text. Such constraints might be added by the auctioneer and the bidders, which allows for considerably more flexibility in the specification of the preferences of market participants.

Although generic pricing rules for different CAs with allocation constraints would also have significant practical importance, we show that these pricing rules bear significant theoretical challenges. The main goal of this paper is not to introduce a new auction format but to define and analyze computational and game theoretical properties of WLs and DLs for FCAs. In particular, we want to understand which pricing rules allow for ex post equilibria and how these pricing rules relate to the theoretical framework on efficient and ascending CAs (Parkes and Ungar 2000, de Vries et al. 2007). This connects also recent IS contributions to the game theoretical literature in this field.

The paper is structured as follows: In §2, we briefly discuss allocation constraints in CAs. We define winning and deadness levels and describe respective algorithms in §3. In §4 we determine the computational complexity for these pricing rules. In §5 we analyze the impact of allocation constraints on efficient CAs and perform an equilibrium analysis of ascending CAs using either winning or deadness levels as ask prices in §6. In §7 we report on our computational experiments before we provide conclusions in §8.

## 2. Allocation Constraints in Combinatorial Auctions

Allocation constraints specify limits on the allocation of the available items to the bidders without explicitly limiting bid prices or revenue of a bidder or a group of bidders. On the other hand, price constraints set price limits on items, packages, a bidder’s budget, or auctioneer revenue. It has been shown that incentive-compatible auctions are impossible in general if there are private budget limits (Dobzinski et al. 2008) and also that reserve prices by the auctioneer increase expected revenue at the expense of efficiency (Myerson 1981). Table 1 provides an overview of allocation and price constraints in CAs, subsumed by the term side constraints. We focus on efficient auctions and therefore will limit ourselves to allocation constraints. One can also divide side constraints into bidder specific ones (bidder level) and those that concern more than a single bidder (group level). The latter are typically specified by the auctioneer, whereas bidder specific constraints could be imposed by the bidder or the auctioneer, especially when the OR bidding language is used.

Allocation constraints are important in many domains. Spectrum auctions, which have been the driving application for much research in this area, regularly face spectrum caps (max # items/bidder; Seifert and Ehrhart 2005). In industrial procurement or the auction for transportation services allocation, constraints are the rule rather than the exception (Caplice 2007, Bichler et al. 2006, Sandholm 2003, Sandholm and Suri 2006). Buyers need to specify lower or upper bounds on the number of suppliers overall or per group (min/max # winning bidders): lower bounds in order to hedge the risk that some suppliers fail to deliver and upper bounds in order to avoid administrative expenses. Market share constraints are defined on a group of bidders. For example, because of corporate requirements at least one minority supplier must be included in the set of winners on a particular set of items. Auctioneers also need to impose lower or upper bounds on the number of items (min/max # items/bidder) that can be awarded to a particular bidder or a group of bidders. Exclusive disjunction describes constraints such that a bidder is allowed to win one set of items or another set but not both. For example, an auctioneer allows a bidder to win one of two different regions A and B but not both. Such constraints can also be specified on a group of bidders. The XOR language can be seen as a separate bidder specific allocation constraint.

Table 1 Side Constraints

<table><tr><td>Side constraint</td><td>Allocation constraint</td><td>Price constraint</td></tr><tr><td>Bidder level</td><td>Min/max # items/bidderExclusive disjunction</td><td>Budget</td></tr><tr><td>Group level</td><td>Min/max # winning biddersMarket shareExclusive disjunction</td><td>Reserve prices budget</td></tr></table>

Although the XOR language already captures many further allocation constraints, experimental analysis has shown that OR bidding languages are often more efficient than XOR languages because of the reduced number of package bids that need to be submitted (Brunner et al. 2010). OR bids can represent only bids that do not have any substitutabilities, i.e., purely additive and superadditive valuations (Nisan 2006). If a bidder uses an OR bidding language, it might also be useful to specify constraints on the number of items (min/max # items/bidder) or budget awarded in order to avoid the exposure problem, which can occur with substitute valuations (e.g., a bidder is winning packages AB and CD but only wants two lots at a maximum) or to express his capacity constraints in case he is a supplier in a procurement auction. Constraints of exclusive disjunction are relevant to the auctioneer in case of an OR bidding language, when a bidder is allowed to win one set of items or another one but not both. Carriers in a transportation auction use such disjunctive constraints to communicate the message “give me this set of lanes or this set of lanes but not both” (Caplice 2007).

Having flexibility in the bidding language and the allocation constraints used by the auctioneer and the bidders allows for a much broader applicability of CAs, and this can be considered a prerequisite for most applications in transportation and industrial procurement.

## 3. Pricing Rules

Before we provide a formal definition, we will first provide an example to informally introduce the pricing rules DL and WL. We will contrast these with pricing rules as they are used in iBundle or in auction formats with pseudo-dual linear ask prices, such as RAD (Kwasnica et al. 2005), to highlight the connections among these different pricing rules.

Table 2 Example with Six Bids and Different Ask Prices

<table><tr><td>Packages</td><td>AB</td><td>BC</td><td>AC</td><td>B</td><td>C</td></tr><tr><td>Bids</td><td> $22_{1}^{*}, 16_{2}$ </td><td> $24_{3}$ </td><td> $20_{4}$ </td><td> $7_{5}$ </td><td> $8_{6}^{*}$ </td></tr><tr><td>RAD</td><td>22</td><td>24</td><td>14</td><td>16</td><td>8</td></tr><tr><td>iBundle</td><td> $22_{1}, 17_{2}$ </td><td> $25_{3}$ </td><td> $21_{4}$ </td><td> $8_{5}$ </td><td> $8_{6}$ </td></tr><tr><td>DL</td><td>22</td><td>24</td><td>20</td><td>7</td><td>8</td></tr><tr><td>WL</td><td>22</td><td>30</td><td>23</td><td>10</td><td>8</td></tr></table>

The upper part of Table 2 describes six bids from different bidders B1 to B6, submitted on subsets of three items A, B, and C, and the lower part shows the resulting prices in various auction formats. Subscripts indicate bidders, i.e., 22 indicates a bid of \$22 from bidder B1. Prices have subscripts only if they are personalized. Asterisks denote the provisional winning bids.

The calculation of RAD prices requires solving a number of linear programs. Note that these linear prices can be lower than a losing bid (see the bid on AC of bidder B4). Other problems with pseudodual ask prices are that they can also decrease if the competition shifts and that the calculation does not take into account allocation constraints explicitly. This makes it difficult to define an equilibrium analysis and as of now there is little theory. Bichler et al. (2009) analyze the problems in defining pseudo-dual linear ask prices.

For the rest of the paper, we will focus on the family of efficient and ascending auctions (iBundle, APA, and dVSV). Apart from the use of proxy agents, APA and iBundle are equivalent and follow a subgradient algorithm, whereas dVSV uses a primal-dual approach (de Vries et al. 2007). Line 4 in our example shows a new set of ask prices in iBundle. The auction format increases the bids of all losing bidders by a minimum bid increment (\$1 in this example; Parkes and Ungar 2000). DLs and WLs describe generic pricing rules; i.e., they are independent of the allocation constraints used by the auctioneer. DLs describe deadness level ask prices, which are simply the bids of all bidders in the last round in this example without any constraints. In this case, DLs do not need to be personalized. Losing bidders need to bid higher than this by a minimum bid increment. With a minimum bid increment of one, the DL would be at the iBundle ask price for the losing bidders B3, B4, and B5. In the presence of allocation constraints, DL ask prices can be much higher than the ones of iBundle, as we will see later.

The WL describes the lowest bid prices, at which a single bid would become a winning one without a new complementary bid of another bidder. Bidders B4 and B5 could become winning bidders at a lower price if they would form a coalition. A known problem with package bidding is the threshold problem, in which bidders seeking larger packages may be favored because small bidders do not have the incentive or capability to top the tentative winning bids of the large bidder. In such a problem, the WL for a small bidder might be way too high to outbid a winning bidder unilaterally, and with only WL ask prices, it will become difficult for bidders to coordinate. The spread between DLs and WLs can often be quite large in realistic value models.

Of course, one can also think of personalized and nonlinear ask prices inbetween DLs and WLs. The coalition of B4 and B5 in our example would need to increase their bids by a combined \$3 plus increment in order to become winning. Both bidders would become winning if bidder B4 bid \$21.5 and bidder B5 bid \$8.5, for example. We refer to such prices as coalitional winning levels (CWLs). A CWL could provide an alternative to linear-price auction formats and help mitigate threshold problems and coordinate bidders. However, computing CWLs turns out to be challenging. First, the number of losing coalitions can grow very fast with the number of items and bids in the auction. Second, and more importantly, there are many ways how the costs to outbid the winning coalition can be shared among the bidders in a losing coalition. One can think about cost sharing that is proportional to the bids in the previous round or a cost sharing that satisfies certain fairness criteria. Independent of how CWLs are set, there will be incentives to free ride on other bidders in a losing coalition. Because of the ambiguities in the definition of CWLs, we will focus on DLs and WLs in this paper, which describe natural upper and lower bounds for bids in an ascending auction, and leave the analysis of CWLs for future research.

## 3.1. Winning Levels

We first introduce the necessary terminology. Let K denote the set of items and I the set of bidders. A subauction on itemset $S \subseteq { \mathcal { K } }$ refers to an auction where only items l ∈ S are auctioned. Auction state $k \in \mathbb N$ refers to the auction after the first k bids are submitted. A bid is a tuple $b = ( S , v , k , i )$ where S denotes the package the bid refers to, v the amount bid, k the auction state after the bid submission,<sup>3</sup> and i the bidder. Given bid b, we use the notation S4b5, $v ( b ) , k ( b )$ , and i4b5 to refer to its respective elements. A bid $b = ( S , v , k , j )$ is foreign with respect to bidder i if $j \neq i . \mathrm { ~ } B _ { S , k } \stackrel { \cdot } { = } \{ ( T , v , k ^ { \prime } , i ) | T \subseteq S , \hat { k ^ { \prime } } \leq k \}$ is the set of all bids in S and $B _ { S , k , - i } = \{ b \in B _ { S , k } \mid i ( b ) \neq i \}$ is the set of all bids in S that are foreign to bidder i. An allocation C of packages to bidders is a set of nonoverlapping bids; i.e., for every $b , b ^ { \prime } \in C , b \neq b ^ { \prime } \Rightarrow$ $S ( b ) \cap S ^ { \prime } ( \bar { b ^ { \prime } } ) \bar { = } \bar { \otimes }$ . An allocation constraint is a function $C  \{ 0 , 1 \}$ where the value 1 indicates fulfillment of the constraint. Our analysis applies to every possible allocation constraint in this form that can be verified in polynomial time.<sup>4</sup> An allocation C is feasible only if it satisfies every allocation constraint, in which case we write $f e a s ( C ) = 1$ . The set of all feasible allocations is denoted by $\mathbb { C } _ { k } = \{ C \subseteq B _ { \mathcal { K } , k } \mid b , b ^ { \prime } \in C , b \neq b ^ { \prime } \Rightarrow S ( b ) \cap$ $S ^ { \prime } ( b ) = \emptyset , f e a s ( C ) = 1 \}$ . The combinatorial allocation problem (CAP), also known as winner determination problem, solves $\begin{array} { r } { \operatorname* { m a x } _ { C \in \mathbb { C } _ { k } } \sum _ { b \in C } v ( b ) . \operatorname { C A P } ^ { k } ( \mathcal { K } ) } \end{array}$ denotes the maximum value of this optimization problem (henceforth we will refer to it simply as value) and $W I N _ { k } ( \mathcal { K } ) \in \mathbb { C } _ { k }$ the value-maximizing allocation at state $k . ^ { 5 } \dot { C } \mathrm { A P } ( S )$ is the value of subauction S.

The winning level of a package S for bidder i at auction state $k , \check { \mathsf { W L } } _ { k } ( S , i ) .$ , is the minimal price i must bid to win S at auction state $k + 1$

<sup>Definition</sup> <sup>1.</sup> WL<sub>k</sub>4S1 i5 = arg min<sub>v</sub>: 4S1 v1 k + 11 i5 $\in W I N _ { k + 1 } ( \mathcal { K } )$

Adomavicius and Gupta (2005) define the anonymous WL of package S at auction state k by<sup>6</sup>

$$
\mathrm{WL} _ {k} ^ {\mathrm{OR}} (S) = \mathrm{CAP} ^ {k} (\mathscr {K}) - \mathrm{CAP} ^ {k} (\mathscr {K} \backslash S).\tag{1}
$$

Intuitively, a bid on S can only win if the bid price together with the value of the complementary set of items $\mathcal { K } \backslash S$ exceeds the actual value of the whole auction. Implicitly, the following assumptions are made: (i) OR bidding language and (ii) absence of allocation constraints. When these assumptions are relaxed, the calculation of WLs as in Equation (1) is inappropriate. A first reason is that allocation constraints, which are not bidder specific, cannot be globally validated when solving subauction CAP4K\S5. In addition, WLs must be personalized, as the following example demonstrates.

<sup>Example</sup> <sup>1.</sup> Consider an auction with items A, B, and $C ;$ bidders B1, B2, and B3; and the constraint that each bidder cannot win more than two items. Bidder B1 bids at k = 1 \$5 on AB, B2 at k = 2 \$1 on AB and at k = 3 \$2 on C, and B3 bids at k = 4 \$3 on AB. WL4C5 is for B1 \$4 whereas for B2 it is only \$2.

We introduce the following formula to calculate personalized WLs that takes XOR bidding and allocation constraints into account:

Proposition 1.

$$
\mathrm{WL} _ {k} (S, i) = \mathrm{CAP} ^ {k} (\mathcal {K}) - \mathrm{CAP} ^ {k} (\mathcal {K}, S _ {i}).\tag{2}
$$

The proof is relegated to Appendix A. $\mathsf { C A P } ^ { k } ( \mathcal { K } , S _ { i } )$ denotes the value of the whole auction provided that bidder i wins package S for free. Thus the auction value $\mathsf { C A P } ^ { k } ( \mathcal { K } , ^ { \bullet } S _ { i } )$ is raised from the items in ${ \mathcal { K } } \backslash S ,$ as it is the case in $\operatorname { C A P } ( { \mathcal { K } } \backslash S )$ . If the OR bidding language is used and no allocation constraints exist, the computation in (2) yields the same WLs as (1).

## 3.2. Deadness Levels

The deadness level of package S at auction state $k ,$ $\mathrm { D L } _ { k } ( S , i )$ , is the minimal price a bidder must bid to have a chance to win S in any future auction state.

Definition 2. $\begin{array} { r } { \mathrm { D L } _ { k } ( S , i ) = \arg \operatorname* { m i n } _ { v } : \exists k ^ { \prime } > k \colon ( S , \ v , } \end{array}$ $k + 1 , i ) \in W I N _ { k ^ { \prime } } ( \mathcal { K } )$

DLs constitute lower bounds on bid prices and all future bids below are “dead”; i.e., they cannot win no matter which bids are submitted in future auction states $k ^ { \prime } > k$ . This implies that ${ \mathrm { D L } } _ { k } ( S , i )$ is monotonically increasing through the progress of any iterative auction.<sup>7</sup>

$$
\begin{array}{l} \text { PROPOSITION   2. } \\ \text {(a) } \mathrm{DL} _ {k} (S, i) \leq \mathrm{DL} _ {k + 1} (S, i); \\ \text {(b) } \mathrm{DL} _ {k} (S, i) \leq \mathrm{WL} _ {k} (S, i); a n d \\ \text {(c) } \mathrm{DL} _ {k} (\mathscr {K}, i) = \mathrm{WL} _ {k} (\mathscr {K}, i). \end{array}
$$

The proofs are based on the definitions of the metrics and are given in Appendix A.

Adomavicius and Gupta (2005) define the anonymous DL of a package S by

$$
\mathrm{DL} _ {k} ^ {\mathrm{OR}} (S) = \mathrm{CAP} ^ {k} (S).\tag{3}
$$

In words, a bid on S cannot be part of the winning allocation if it is below the value of subauction $S \ { \mathrm { ( i . e . , } } \quad$ CAP4S5). For example if $S = A B$ and there are already bids $A = \$ 10$ and $B = \$ 15$ , then any bid on AB below \$25 is dead.

The DL in Equation (3) is not valid if there are allocation constraints or any of the bidders uses an XOR bidding language. In these cases DLs must be personalized. We also need to understand what influence the additional allocation constraints might have in future auction states. For instance, consider again Example 1. B3 loses AB at current state $k = 4$ . But if in the future state k = 5 B1 bids \$8 on C, then his previous winning bid on AB loses because of the allocation constraint.<sup>8</sup> Thus B3 can win AB for \$3 and his personal DL at k = 4 is \$3. We say that the bid of B1 on AB has been ”blocked” at $k = \bar { 5 }$ because of the constraint.

A bid on package S loses in an auction with allocation constraints if at least one of the following conditions is met: (i) There exists a higher bid or bid combination in subauction S that wins in the whole auction (without violating allocation constraints). (ii) S is not part of the value maximizing allocation. (iii) The bid in interaction with other bids that win in the whole auction violates an allocation constraint.

The first two conditions are common for every $\mathrm { C A , }$ with or without constraints. The third one leads us to the definition of blocked bids, which we use later on; a bid b is blocked if it does not win because of allocation constraints. In this case, one or more winning bids in the complementary subauction, which we denote by $B ^ { \prime } ,$ prevent the blocked bid from winning. If the bids in $B ^ { \prime }$ had not existed, b would have won. The winning bids after the removal of a bid set B<sup>0</sup> are denoted by $W I N _ { k } ^ { - B ^ { \prime } } ( \mathcal { K } )$ . In the context of Example 1 extended by a bid of \$8 of bidder B1 on item C and of \$8 of B1 on additional item $D ,$ the bid set $B ^ { \prime }$ comprises these two bids. The removal of both bids in $B ^ { \prime }$ would turn the bid b of B1 on AB into winning. Because $b \in W I N _ { k } ^ { - B ^ { \prime } } ( \mathcal { K } )$ , b is blocked by $B ^ { \prime }$ and does not win because of allocation constraints.

Definition 3. <sub>Bid</sub> $b = ( S , v , k ^ { - } , i )$ is blocked at state $\bar { k } \ge k ^ { - } \ \mathrm { i f } b \notin W I N _ { \bar { k } } ( \mathcal { K } )$ and $\exists B ^ { \prime } \subseteq B _ { \mathcal { K } \backslash S , \bar { k } }$ with $b \in$ $W I N _ { \bar { k } } ^ { - B ^ { \prime } } ( \mathcal { K } )$

Computing ${ \mathrm { D L } } _ { k } ( S , i )$ requires knowing which currently winning bids in S can be blocked in future auction states. We call these bids blockable.

Definition 4. <sub>Bid</sub> $b = ( S , v , k ^ { - } , i )$ is blockable at state k if $b \in W I N _ { k } ( \mathcal { K } )$ with $k \geq k ^ { \prime }$ <sup>−</sup> and $\exists \bar { k } > k$ so that b is blocked at state <sup>¯</sup>k.

Removing a blockable foreign to i bid in S causes another lower foreign bid (or bids) in S to win. If a distinct future state <sup>¯</sup>k can be reached where both the second and the first bid are blocked, then the $\mathrm { D L } _ { k } ( S , i )$ becomes even lower because i does not have to overbid any of them. We will say that the two bids are simultaneously blockable at current state k and simultaneously blocked at $\bar { k } > k .$ To see this happen, consider again Example 1 with an additional item D and seek for DL4AB1 B25. We have already argued that the highest bid on AB by B1 is blockable. Removing it causes the bid of B3 to win. This second bid is also blockable because of a similar reason as the first blockable bid (B3 may bid high on D). More importantly, these two bids are simultaneously blockable because there is a future state with both bids blocked (see Table 3). Had item D not existed, this would not have been possible. Only one of the bids would have been blockable, but the two of them would not have been simultaneously blockable.

Table 3 Bids in Bold Block Crossed Out Bids and DL4AB1 B25 = 1, k is Denoted as Superscript

<table><tr><td></td><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td> $B1$ </td><td> $5^{1}$ </td><td></td><td> $8^{5}$ </td><td>0</td></tr><tr><td> $B2$ </td><td> $1^{2}$ </td><td></td><td> $2^{3}$ </td><td>0</td></tr><tr><td> $B3$ </td><td> $3^{4}$ </td><td></td><td>0</td><td> $8^{6}$ </td></tr></table>

We just highlighted the central role of simultaneously blockable bid sets in computing $\mathrm { D L } _ { k } ( S , i )$ . These are bids by rivals of $i ,$ thus foreign to him, submitted in S. We denote a simultaneously blockable bid set in subauction S at state k comprising bids foreign to bidder i as $B _ { S , k , - } ^ { \mathrm { b l o c k } }$ . Undoubtedly, foreign bids on packages that overlap with S but are not entirely in S are also preventing i to win S but these bids are not relevant at the most favorable future state for i that DL4S1 i5 represents. The reason is that in this most favorable state the value of subauction $\mathcal { K } \backslash S$ is high enough such that S is part of the winning allocation. Before providing the formal definition for $B _ { S , k , - i } ^ { \mathrm { b l o c k } } ,$ it is meaningful to sketch the algorithm that utilizes these sets to compute DL4S1 i5.

The algorithm identifies all simultaneously blockable bid sets. In our running example there was only one set when item D was present, comprising the bids of B1 and B3 on AB, and two single-item sets when D was not present, which were the two bids separately. The algorithm removes each identified set in turn and computes the value of CAP4S5. The lowest value is DL4S1 i5 because DL4S1 i5 represents the most favorable future state for i to win S.

Having outlined the algorithm, we can state the conditions a set must fulfill in order to be declared as simultaneously blockable at current state $k ,$ with <sup>¯</sup>k being the future state where the set will be actually blocked. We begin with the indispensable conditions and continue with conditions that only accelerate the sketched algorithm. Their enumeration and motivation precedes the formal description given in Definition 5. We have already discussed that going from k to <sup>¯</sup>k in order to block bids in $S ,$ we add only bids in $\mathcal { K } \backslash S$ because if they would overlap with $S ,$ they would prevent i from winning S. Their set is $B ^ { \prime } { = } \tilde { B _ { \mathcal { \pi } , \bar { k } } } \backslash B _ { \mathcal { \pi } , k } , \mathrm { \bar { i } . e . } ,$ all bids between k and <sup>¯</sup>k. Bids in $B ^ { \prime }$ must be winning else they cannot block any bids or generally impact the allocation or prices. The first condition states that after the submission of B<sup>0</sup> it must be feasible that i wins S (condition i). Second, inherent to the definition of a blocked bid is the condition that every bid in $B _ { S , k , - i } ^ { \mathrm { b l o c k } }$ must be losing at <sup>¯</sup>k (condition ii).

Moving to conditions that only accelerate the sketched algorithm, we observe that if all bids in the simultaneosuly blockable set are losing at $k ,$ their removal will not lower the price i has to pay for $S ;$

hence, at least one of them must be winning at k (condition iii). In Table 3 removing only bid 4 has no impact. Furthermore, it is not meaningful that a blockable bid set contains a bid that never wins, even after the removal of the rest bids of the set. As we begin to block some bids, previously losing bids turn to winning and these are the ones that lower the price of S if blocked. Hence we demand $b \in B _ { S , k , - i } ^ { \mathrm { b l o c k } } \Rightarrow$ $\bar { b } \in W I N _ { k } ^ { - ( B _ { S , k , - i } ^ { \mathrm { b l o c k } } \backslash b ) } ( \mathcal { K } )$ (condition iv). Furthermore, we observe that it is redundant to block a foreign bid on $T \subseteq S$ if it is lower than a bid already submitted by i on $T ^ { \prime } \subseteq T$ because i can never pay less than his own bid. The set of all these bids, which we call non-i-dominated, is denoted by $B _ { S , \bar { k } , - i } ^ { \mathrm { n d o m } }$ , and the corresponding condition states that all bids in $B _ { s , \bar { k } , - i } ^ { \mathrm { b l o c k e d } }$ are non-i-dominated (condition v). The concluding condition specifies that simultaneously blockable bid sets must be maximal (condition vi) because blocking and removing an extra bid can only lower the value of $\mathrm { C A P } ( S )$ . A set is defined as maximal if it satisfies a property (in our case the property is the satisfaction of conditions i to v) and there exists no strict superset of it that also satisfies the property. Hence adding an item in a maximal set causes violation of the property. In Table 3 bid 1 is not identified as simultanoeously blockable only because it is not maximal.

Definition 5. <sub>Bid</sub> <sub>set</sub> $B _ { S , k , - } ^ { \mathrm { b l o c k } }$ is simultaneously blockable at state k if $\exists B ^ { \prime } { = } ( B _ { \mathcal { K } , \bar { k } } \backslash \overset { \sim } { B } _ { \mathcal { K } , k } ) { \subseteq } ( B _ { \mathcal { K } \backslash S , \bar { k } } \cap W I N _ { \bar { k } } ( \mathcal { K } ) )$ :

(i) $f e a s ( W I N _ { \bar { k } } ( { \mathcal K } \backslash S ) \cup { \dot { b } } ) = 1 _ { \cdot }$ , where $\begin{array} { r } { { S } ( b ) = S , i ( b ) = i ; } \end{array}$

(ii) $B _ { S . k . - i } ^ { \mathrm { b l o c k } } \cap W I N _ { \bar { k } } ( \mathcal { K } ) = \emptyset ;$

(iii) $\bar { B } _ { S , k , - i } ^ { \mathrm { { b i o c k } } } \cap W I N _ { k } ( \mathcal { K } ) \neq \emptyset ;$

(iv) $b \in B _ { S , k , - i } ^ { \mathrm { b l o c k } } \Rightarrow b \in W I N _ { k } ^ { - ( B _ { S , k , - i } ^ { \mathrm { b l o c k } } \backslash b ) } ( \mathcal { K } ) ;$

(v) $B _ { S , k , - i } ^ { \mathrm { b l o c k } } \subseteq B _ { S , k , - i } ^ { \mathrm { n d o m } } ; a n d$

(vi) $\sharp B ^ { \prime \prime } \supset B _ { S , k , - i } ^ { \mathrm { b l o c k } }$ with $B ^ { \prime \prime }$ satisfying conditions (i) to (v).

With this definition we can introduce the general method to compute ${ \mathrm { D L } } _ { k } ( S , i )$ for arbitrary allocation constraints.

General Method to Compute $\mathrm { D L } _ { k } ( S , i )$ . In the first phase, the method takes as input all bids that are candidates to form simultaneously blockable bid sets. These are the bids in $B _ { S , k , - i } ^ { \mathrm { n d o m } } .$ The output of the first phase is the set of all simultaneously blockable bid sets in S. We can represent the first phase as a function f with argument $\bar { B } _ { S , k , - 1 } ^ { \mathrm { n d o m } }$ and value the output of this phase; i.e., $, \ f \colon B _ { S , k , - i } ^ { \mathrm { n d o m } ^ { - \prime \prime \prime } }  \{ B _ { S , k , - i } ^ { \mathrm { b l o c k } } \}$ . We consider here $f$ as a black box because for the general description of the method only $f ^ { \prime } \mathbf { s }$ argument and value matters. In the second phase each of the identified sets $B _ { S , k , - i } ^ { \mathrm { b l o c k } } \in$ $f ( B _ { S , k , - i } ^ { \mathrm { n d o m } } )$ is removed consecutively and the value of subauction S, denoted as $\mathsf { C A } \bar { \mathsf { P } } ^ { k } ( S , B _ { S , k } \backslash B _ { S , k , - i } ^ { \mathrm { b l o c k } } ) .$ is computed. The lowest of these values equals to DL4S1 i5. It is not always necessary to compute all these values. If we encounter a value not greater than the value of the bids of i in S, we do not need to continue because i must overbid its own bids. Equation (4) summarizes the general two-phase method.

Proposition 3.

$$
\begin{array}{c} \mathrm{DL} _ {k} (S, i) = \min _ {B _ {S, k, - i} ^ {\text {block}}} \bigl \{\mathrm{CAP} ^ {k} (S, B _ {S, k} \backslash B _ {S, k, - i} ^ {\text {block}}): \\ B _ {S, k, - i} ^ {\text {block}} \in f (B _ {S, k, - i} ^ {\text {ndom}}) \bigr \}. \end{array}\tag{4}
$$

<sup>Proof.</sup> The proof draws on the definition of ${ \mathrm { D L } } _ { k } ( S , i )$ and of simultaneously blockable bid sets. Let c be the right side of Equation (4) and $B _ { * } ^ { \mathrm { b l o c k } }$ the argument of the minimum. First we show that for $b =$ $( S , c , k ^ { - } , i ) \ \exists k ^ { * } > k ^ { - } : \ b \in W I N _ { k ^ { * } } ( \mathcal { K } )$ . We define $k ^ { * }$ as the state at which (a) the bids in $B _ { * } ^ { \mathrm { b l o c k } }$ are actually blocked and do not win because of condition i; (b) a bid set B<sup>0</sup> in $\mathcal { K } \backslash S$ is submitted so that $B ^ { \prime } \subseteq W I N _ { k ^ { * } } ( \mathcal { K } ) .$ and $( \mathbf { c } ) \forall b$ with $k ( b ) \in ( k , k ^ { * } ] , i ( b ) \neq i , S ( b ) \subseteq \mathcal { K } \backslash \backslash \ S \ ( \mathrm { i . e . } ,$ no new foreign bids overlapping with S are submitted). We can ensure that the bids in $B _ { * } ^ { \mathrm { b l o c k } }$ lose at $k ^ { * }$ without the need of submission of overlapping bids at states in $( k , k ^ { * } ]$ because of condition ii. Thus the bid b<sup>∗</sup> with value $c \doteq \mathrm { C A P } ^ { k } ( S , B _ { S , k } \backslash B _ { * } ^ { \mathrm { b l o c k } } )$ is part of the winning allocation (because of condition i and that the winning allocation maximizes CAP over all feasible allocations). Similarly it can be argued that for $b ^ { \prime } =$ $( S , c - \epsilon , \dot { k } , i ) \nexists k ^ { \prime } > \dot { k } \colon b \in W I N _ { k } ^ { \prime } ( \mathfrak { K } )$ : After removing each simultaneously blockable bid set $B _ { S , k , - i } ^ { \mathrm { b l o c k } } ,$ there is a feasible allocation that includes the bids which maximize $\mathrm { C A P } ^ { k } ( S , B _ { S , k } \backslash B _ { S , k , - i } ^ { \mathrm { b l o c k } } )$ and have a value at least c. Thus b<sup>0</sup> cannot be part of the winning allocation. Collectively, we showed that $c = \arg \operatorname* { m i n } _ { v } \colon \exists k ^ { \prime } > k \colon$ $( S , v , k + \bar { 1 } , i ) \in W I N _ { k ^ { \prime } } ( \mathcal { K } )$ . This is the definition of ${ \mathrm { D L } } _ { k } ( S , i )$ Q.E.D.

With an OR bidding language and without allocation constraints (4) reduces to (3) because without these constraints, there are no blockable bids and thus $\mathrm { D L } _ { k } ( S , i ) = \mathrm { C A P } ^ { k } ( S , B _ { S , k } \backslash B _ { S , k , - i } ^ { \mathrm { b l o c k } } ) = \mathrm { C A P } ^ { k } ( S , B _ { S , k } \backslash \emptyset ) =$ $\mathrm { C A P } ^ { k } ( S , B _ { S , k } ) = \mathrm { C A P } ^ { k } ( S )$

<sup>Example</sup> <sup>2.</sup> Consider an auction with items A, B, $C ,$ and D; bidders B1 to B5; and the XOR bidding language. The bids in AB are 4AB, \$9, 1, B15, 4A1 \$51 2, B25, 4B1 \$8, 3, B25, 4A1 \$10, 4, B35, 4AB1 \$15, 5, B45, and 4AB, \$19, 6, B55 (see Table 4). We compute ${ \mathrm { D L } } _ { 6 } ( A B , B 1 )$ using the above formula. Function $\mathbf { \bar { \boldsymbol { f } } ^ { \prime } } \mathbf { s }$ argument $B _ { A B , 6 , - B 1 } ^ { \mathrm { n d o m } }$ contains all bids except the bid of $\mathbf { \bar { \boldsymbol { B 1 , f } } }$ returns all simultaneously blockable sets $B _ { A B , 6 , - B 1 } ^ { \mathrm { b l o c k } } ,$ , and

$$
f \big (B _ {A B, 6, - B 1} ^ {\mathrm{ndom}} \big) = \big \{\{2, 3, 6 \}, \{4, 6 \}, \{5, 6 \} \big \}.
$$

Bids are referred by their state. Bids $\{ 2 , 3 , 6 \}$ are blockable because of XOR bidding if B2 and B5 win C and D, respectively; bids $\{ 4 , 6 \}$ if B3 and B5 win C and D, respectively; and bids 851 69 if B4 and B5 win C and D, respectively. Note that condition iv of Definition 5 is the only optional condition that may lead to siginficant computational effort to check it and it is not considered in this example with XOR bidding. Sets without bid $^ { 6 , }$ like $\{ 2 , \bar { 3 , 4 } \} , \{ 2 , 3 , 5 \} , \{ 4 , 5 \}$ violate condition iii because none of their bids currently wins. The sets 831 69 and 821 69 are not maximal because their superset 821 31 69 is simultaneously blockable. Subsequently we remove each simultaneously blockable set from subauction AB and compute CAP. After removing the first set, $\mathbf { C A P } = \$ 15;$ after the second one, ${ \mathrm { C A P } } = { \bar { \$ } } 1 5 ;$ and after the third one, \$18. The minimum CAP is \$15; thus $\mathrm { D L } _ { 6 } ( A B , B 1 ) = \$ 15$ B1 could win AB for \$15 in a future state in which B2 wins C and B5 wins D.

<table><tr><td colspan="5">Table 4 Bids of Five Bidders on Items A, B, C, and D</td></tr><tr><td></td><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td>B1</td><td colspan="2"> $9^1$ </td><td colspan="2">0</td></tr><tr><td>B2</td><td> $5^2$ </td><td> $8^3$ </td><td colspan="2">0</td></tr><tr><td>B3</td><td> $10^4$ </td><td></td><td colspan="2">0</td></tr><tr><td>B4</td><td colspan="2"> $15^5$ </td><td colspan="2">0</td></tr><tr><td>B5</td><td colspan="2"> $19^{6*}$ </td><td colspan="2">0</td></tr></table>

Notes. The superscript denotes k and <sup>∗</sup> denotes currently winning. What is the DL of the package AB for bidder B1?

Function $f$ is specific to allocation constraints and the bidding language, which determine whether a bid set is simultaneously blockable or not. In Appendix B we provide an algorithm to calculate DLs for the XOR bidding language without additional allocation constraints. The XOR bidding language is fully expressive (Nisan and Segal 2006), and it is used in high-stakes applications such as in spectrum auctions across Europe nowadays.

## 4. Computational Complexity

Computational complexity has turned out to be a practically relevant topic for the winner determination problem in CAs. We show that computational complexity is also a problem when computing pricing rules and that the computation of DLs is even one of the rare examples of a $\mathbf { \dot { I } } \mathbf { I } _ { 2 } ^ { P }$ -complete problem.

The CAP is a well-known NP-complete problem in its decision version. The NP -completeness is proven for a variety of cases and bidding languages. Lehmann et al. (2006) prove the NP-completeness of CAP for the OR and XOR bidding language by reducing from the independent set problem (Garey and Johnson 1972) using intersection graphs. Sandholm and Suri (2001) prove the completeness for numerous cases dealing with side constraints such as bounds on the maximal number of winners. It is easy to see that the computation of WLs must be at least as hard as CAP.

<sup>Proposition</sup> <sup>4.</sup> Deciding WL4S1 i5 is NP-complete.

<sup>Proof.</sup> Every instance of CAP can be viewed as an instance of WL for $S = { \mathcal { K } } .$ . For $S = \mathcal { K } _ { i }$ , Equation (2) yields $\operatorname { W L } ( K , i ) = \operatorname { C A P } ( \mathcal { K } ) - \operatorname { C A P } ( \mathcal { K } , \mathcal { K } _ { i } ) \overset { \cdot } { = } \operatorname { C A P } ( \mathcal { K } )$ Thus WL contains CAP as a special case that is NP-complete. Q.E.D.

Interestingly, the DL problem (Equation (4)) is even harder to solve. It requires solving one CAP for every simultaneously blockable bid set. The number of bids in S is ${ \dot { O } } ( 2 ^ { | S | } | { \mathcal { I } } | )$ . Hence the number of bid sets is $O ( 2 ^ { | S | } | \mathcal { I } | )$ . Because of the set maximality property, many of these double exponential bid sets need not be evaluated. That means in the worst case only $\big ( _ { \lfloor ( 2 ^ { \vert S \vert } \vert \mathcal { I } \vert ) / 2 \rfloor } ^ { 2 ^ { \vert S \vert } \vert \mathcal { I } \vert } \big )$ CAPs need to be solved (Engel 1997), which is still super exponential to the number of items in S. The actual number of blockable bid sets depends strongly on the allocation constraints.

Obviously the problem belongs to a higher complexity class than NP . This class is ç<sup>P</sup> if the decision version is formulated as DL $( S , i ) > c$ and $\Sigma _ { 2 } ^ { P }$ if $\operatorname { D L } ( S , i ) \leq c .$ Completeness in these classes informs what can (or cannot) be done in polynomial time with access to an NP oracle,<sup>9</sup> i.e., an oracle that is able to decide the decision version of the winner determination problem in a single operation. Every CA employs a method to solve CAP. If we assume the presence of such an efficient method, completeness in these classes plays exactly the role of $N \dot { P } .$ -completeness for “ordinary” optimization problems—it distinguishes the intractable from the efficiently solvable (Umans 2000). $\Pi _ { 2 } ^ { P } = c o N P ^ { N P }$ and $\Sigma _ { \gamma } ^ { P } = N P ^ { N P }$

We first show $\mathrm { D L } ( S , i ) \in \Pi _ { 2 } ^ { P }$ with the decision problem DL $( S , i ) > c$

<sup>Lemma</sup> <sup>1.</sup> DL4S1 i5 is in $\Pi _ { 2 } ^ { P }$

<sup>Proof.</sup> We show that there exists a polynomially balanced, polynomial-time decidable 3-ary relation R such that $\mathbf { \bar { D L } } = \{ x \colon \forall y _ { 1 } \exists y _ { 2 }$ such that $( x , y _ { 1 } , y _ { 2 } \in R ) \}$ x represents the graph containing all bids in S. Each node in x represents a \$1 bid and nodes are connected if and only if the bids they represent are compatible (e.g., do not overlap). $y _ { 1 }$ represents a subgraph of x that is induced according to function f (i.e., each subgraph represents a bid set after removing a simultaneously blockable bid set). $y _ { 2 }$ is an independent set of $y _ { 1 }$ . Note that its cardinality equals the value of the auction. Relation R decides in polynomial time that $y _ { 1 }$ is a subgraph of $x , y _ { 2 }$ an independent set of $y _ { 1 } ,$ and $y _ { 2 }$ contains more than c nodes. Thus $R$ is polynomially decidable. Furthermore $R$ is polynomially balanced (because the lengths of $y _ { 1 }$ and $y _ { 2 }$ are bounded by a polynomial in the length of x). Q.E.D.

Intuitively, the DL is greater than c if all bid combinations prescribed by f result in a subauction value greater than c. In graph terms, all of the induced subgraphs must have an independent set of cardinality greater than c. Remember that DL is a minimization problem, and if one subgraph with value not greater than c exists, then the answer to the question becomes negative. That explains the necessity of the first quantifier ∀ and is central for the complexity of the problem, which is a min–max optimization problem (Ko and Lin 1995).

We now prove the completeness of DL4S1 i5 in $\Pi _ { 2 } ^ { P }$ We make use of the structures of a fairly restrictive case of the problem because it is common ground in such proofs (Lehmann et al. 2006) to reduce from the minmax-Clique problem defined in Ko and Lin (1995).

Definition 6 (Minmax-Clique). <sub>Given</sub> <sub>is</sub> <sub>a</sub> <sub>graph</sub> $G = ( V , E )$ with its vertices V partitioned into subsets $V _ { i , j } , 1 \le i \le I , 1 \le j \le J$ . For any function t2 $\{ 1 , \ldots , I \} $ $\{ 1 , \ldots , J \}$ , G denotes the induced subgraph of G on the vertex set $V _ { t } = \cup _ { i = 1 } ^ { I } V _ { i , t ( i ) }$ . Find ${ \hat { f } } _ { \mathrm { C l i q u e } } ( G ) =$ min $\operatorname* { m a x } _ { Q } \{ | Q | \colon Q \subset V$ is a clique in $G _ { t } \}$

Intuitively the graph represents a network with I components, with each component $V _ { i }$ having J subcomponents $V _ { i , 1 } , \ldots , V _ { i , { J } }$ . At any time t only one subcomponent $V _ { i , t ( i ) }$ of each $V _ { i }$ is active, and the problem is to find the maximum clique size of all possible active subgraphs $G _ { t }$ . The minmax-Clique problem is $\Pi _ { 2 } ^ { P } \mathrm { - c o m p l e t e }$ by reduction from SAT . The completeness is shown for $J = 2$ and subsets $V _ { i , j }$ of same cardinality.

<sup>Theorem</sup> <sup>1.</sup> Deciding DL4S1 i5 is $\Pi _ { 2 } ^ { P }$ -complete.

<sup>Proof.</sup> We reduce from minmax-Clique. For each subcomponent $V _ { i , j }$ we create a bidder who participates in subauction S. Because $J = 2 ,$ , each component corresponds to a pair of bidders. We introduce the allocation constraint that no two bidders belonging to the same pair are allowed to win together in ${ \check { \mathcal { K } } } \backslash { \check { S } } .$ For each node we create a \$1 bid on T with $T \subseteq S$ submitted from the bidder associated to the subcomponent the node belongs to. Whenever two nodes in G are connected, their associated bids are compatible.<sup>10</sup> It can be observed now that $f _ { \mathrm { C l i q u e } } ( G ) = { \mathrm { D L } } ( { \dot { S } } , i )$ There is a one-to-one correspondence between the $2 ^ { | I | }$ possible active subgraphs $\bar { G _ { t } }$ and the bidder (bid) sets that remain after removing each of the $2 ^ { | I | }$ simultaneously blockable bidder (bid) sets of cardinality I because of the constraint in $\mathcal { K } \backslash S$ . Furthermore, the max-Clique problem on the complementary intersection graphs is equivalent to the maximum independent set problem on the actual intersection graph and thus equivalent to CAP. Q.E.D.

An interpretation of the constraint we introduced to prove completeness is that the auctioneer is not willing to deal with more than a single winner from a region, assuming that bidders are paired according to their region. We conjecture that the DL problem without such constraints cannot be easier because the number of the simultaneously blockable bidders and thus the number of CAPs that must be solved becomes much greater. To see this, consider an example with eight foreign bidders in S and $| { \mathcal { K } } \backslash S | = 4$ . Without the constraint the bidder sets amount to $\binom { 8 } { 4 }$ , whereas with the constraint only $2 ^ { 4 }$ bidder sets need to be evaluated.

## 5. Allocation Constraints and Their Impact on Equilibrium Strategies in Efficient Auction Designs

In what follows, we want to understand equilibrium strategies in CAs with allocation constraints. In order to analyze such CAs with respect to efficiency and incentive compatibility, we first need to understand the impact of allocation constraints on those CA formats that are known to be efficient with a strong game theoretical solution concept. First, we analyze the VCG auction, which is known to be the unique CA format that is strategy proof, efficient, and individually rational (Green and Laffont 1977). Second, we focus on ascending CAs as iBundle, the APA, and dVSV in which straightforward bidding is an ex post equilibrium for buyer submodular valuations. The analysis integrates the auction mechanisms in Adomavicius and Gupta (2005) in this game theoretical framework and provides conditions when this auction format leads to an ex post Nash equilibrium.

<sup>Definition</sup> <sup>7.</sup> A strategy profile $s ^ { * } = ( s _ { 1 } ^ { * } , \ldots , s _ { n } ^ { * } )$ is an ex post Nash equilibrium iff the utility functions $u _ { i }$ satisfy

$$
u _ {i} (s ^ {*}, t) \geq u _ {i} (s _ {i} ^ {\prime}, s _ {- i} ^ {*}, t) \quad \forall s _ {i} ^ {\prime}, t, i.
$$

In other words, truthful bidding in every round of an auction is an ex post (Nash) equilibrium, if for every bidder $i \in \mathcal { I } .$ , if all other bidders follow the truthful bidding strategy, then bidder i maximizes his payoff in the auction by following the truthful bidding strategy independent of the type t of other bidders (Mishra and Parkes 2007). Ex post equilibria avoid speculation about other bidders’ valuations or types and could therefore reduce the strategic complexity for bidders considerably, leading to higher efficiency and also an increased adoption of ascending CAs. Note that this is weaker than a dominant strategy equilibrium, where bidders do not have to speculate about other bidders’ valuations and strategies. In contrast to dominant strategy and ex post equilibria, Bayes-Nash equilibria do always exist, but they require bidders to speculate on both the type and the strategy of others. We refer to dominant and ex post equilibria as strong solution concepts. For ascending auctions we focus on ex post equilibria because preference elicitation in an indirect mechanism typically does not allow for dominant strategy equilibria (Conitzer and Sandholm 2002).

Let us first introduce two definitions to describe bidder valuations before we discuss individual auction formats.

<sup>Definition</sup> <sup>8.</sup> A coalitional value function V maps a set of bidders J to a real number $\overset { \cdot } { V } ( J )$ , equal to the total value created from trade among these bidders and the auctioneer.

CAP implements a coalitional value function in the context of CAs. Bidder submodularity describes a property of the coalitional value function, which allows for strong solution concepts in ascending CAs and core outcomes in the VCG auction, as we will see below.

Definition 9 (Bidder Submodular (BSM) Condi-<sup>tion).</sup> A coalitional value function V is bidder submodular if bidders are more valuable when added to smaller coalitions: for all $i \in \mathcal { I }$ and all coalitions J and J <sup>0</sup> satisfying $J \subset J ^ { \prime } , V ( J \cup \{ i \} ) - V ( J ) \geq V ( J ^ { \prime } \cup \{ i \} ) - V ( \dot { J } ^ { \prime } )$

Because allocation constraints may alter (lower) $V ( J )$ , imposing them may turn a coalitional value function from not BSM to BSM or vice versa.<sup>11</sup> The simplest example to see this is to impose the allocation constraint “max one winner.” Any function will then turn into BSM. The constraint “min three winners” turns any function into not BSM. In the following, when we refer to $V ( J )$ or BSM, these are computed by taking into account present allocation constraints.

## 5.1. The VCG Mechanism

The VCG outcome serves as a baseline for all other efficient auction formats. For example, under BSM valuations APA, iBundle, and dVSV terminate with VCG prices that are in the core, eliminating incentives for speculation. Core prices have the property that no coalition of bidders can renegotiate the outcome with the auctioneer in order to increase everyone’s payoff in this coalition.

The VCG auction is a sealed bid auction allowing for package bids on all combinations of items. Bidders place sealed XOR bids on their desired packages without getting any feedback from the auctioneer or knowing bids of other bidders. The auctioneer calculates a feasible allocation $X ^ { \ast }$ that maximizes the sum of bid prices. Bidders’ payments $p _ { i } ( S )$ are calculated in a second step. Winning bidders pay their bid prices $b _ { i } ( S )$ reduced by a discount that is equal to their marginal contribution to the whole economy. Hence, $p _ { i } ( \boldsymbol { S } ) = b _ { i } ( \boldsymbol { S } ) - ( V ( \mathcal { I } ) - V ( \mathcal { I } \backslash i ) ) \forall \boldsymbol { S } \in X ^ { \ast }$ and zero otherwise.

We concentrate on allocation constraints in this paper. Although Ausubel and Milgrom (2006b) show that budget constraints can lead to inefficiency in the VCG mechanism, allocation constraints do not affect its properties. However, the calculation of the VCG prices and in particular of the coalitional value from $V ( J )$ with $J \subset { \mathcal { I } }$ has to consider the allocation constraints because otherwise the auctioneer could suffer a negative payoff and participation would not be individually rational.

Definition 10 (Shoham and Leyton-Brown 2009). An environment exhibits the no-single-agent effect if $\forall i , \forall v _ { - i } , \forall X$ there exists an allocation X<sup>0</sup> that is feasible without i and $\begin{array} { r } { \sum _ { j \not = i } v _ { j } ( X ^ { \prime } ) \geq \sum _ { j \not = i } v _ { j } ( X ) } \end{array}$

A mechanism is weakly budget balanced when it will not lose money; this means if the mechanism is not weakly budget balanced, the auctioneer might be confronted with a negative payoff, which would contradict individual rationality of the mechanism.

Theorem 2 (Shoham and Leyton-Brown 2009). The VCG mechanism is weakly budget balanced when the no single agent effect property holds.

CAs without allocation constraints are always weakly budget balanced because the no single agent effect property always holds (Shoham and Leyton-Brown 2009). The theorem extends to VCG auctions with allocation constraints, but in this case the no single agent effect property may not hold. Hence these auctions are not always weakly budget balanced.

<sup>Corollary</sup> <sup>1.</sup> The VCG mechanism with allocation constraints is not always weakly budget balanced.

<sup>Proof.</sup> It may happen that $V ( \mathcal { I } \backslash i )$ in the VCG payment computation is zero because of allocation constraints. Consider an example where the auctioneer requires two winning bidders and only two bidders participate, such that the no single agent effect does not hold. Bidder B1 values item A at \$10 and B2 values B at \$10. The Vickrey payments are $p _ { 1 } ( A ) =$ $p _ { 2 } ( B ) = 1 0 - ( 2 0 - 0 ) = - 1 0 \leq 0$ , and the auctioneer loses money. Q.E.D.

If the no single agent effect does not hold, the auctioneer might want to consider bids by bidders $i \notin J$ to assure a feasible allocation while maximizing $V ( J )$

## 5.2. Efficient Ascending CAs

The recent game theoretical research has led to a coherent theoretical framework and a family of ascending CAs (iBundle, APA, dVSV) that satisfy an ex post equilibrium under BSM. These efficient ascending CAs use personalized and nonlinear prices. They calculate a provisional value maximizing allocation at the end of every round and increase the prices for a certain group of bidders. The different approaches can be interpreted as implementations of primal dual algorithms (dVSV) or subgradient algorithms (iBundle, APA) to solve an underlying linear programming problem (de Vries et al. 2007). This linear program $( \mathrm { C A P } _ { 3 } )$ always yields integral solutions and the dual variables have a natural interpretation as nonlinear and personalized ask prices (Bikhchandani and Ostroy 2002).

We want to understand whether additional allocation constraints have an impact on equilibrium strategies and efficiency in these auction formats. For this reason, we analyze the impact of allocation constraints on $\mathrm { C A P } _ { 3 }$ . The original $\mathrm { C A P } _ { 3 }$ formulation changes with additional allocation constraints. An arbitrary allocation constraint can make certain allocations infeasible. Rather than modeling specific allocation constraints, we keep our analysis general and partition the set of all allocations into two subsets: the feasible allocations  and the infeasible ones $\mathbb { C } _ { u } ,$ which turn infeasible because of the violation of certain allocation constraints (e.g., the maximum number of winners). This extends $\mathrm { C A P } _ { 3 }$ by constraint set (LP4):

$$
\max _ {x _ {i} (S)} \sum_ {S \subseteq \mathscr {K}} \sum_ {i \in \mathscr {I}} x _ {i} (S) v _ {i} (S)
$$

$$
\text { s.t. } \sum_ {S \subseteq \mathscr {K}} x _ {i} (S) \leq 1 \quad \forall   i, \quad (\pi_ {i})\tag{LP1}
$$

$$
x _ {i} (S) \leq \sum_ {X \in \mathbb {C} \cup \mathbb {C} _ {u}: S _ {i} \in X} y (X)
$$

$$
\forall i, S, (p _ {i} (S))\tag{5}
$$

4LP25

$$
\sum_ {X \in \mathbb {C} \cup \mathbb {C} _ {u}} y (X) \leq 1,\tag{\((\pi_s)\}
$$

4LP35

$$
y (X) \leq 0 \quad \forall X \in \mathbb {C} _ {u},\tag{\( (t(X)) \}
$$

$$
\begin{array}{c} x _ {i} (S), y (X) \geq 0 \\ \forall i, S, X \in \mathbb {C} \cup \mathbb {C} _ {u}. \end{array}\tag{LP4}
$$

The dual to the extended $\mathrm { C A P } _ { 3 }$ in (5) is:

$$
\min _ {\pi_ {i}, \pi_ {s}} \sum_ {i \in \mathcal {I}} \pi_ {i} + \pi_ {s}
$$

$$
\mathrm{s.t.} \pi_ {i} + p _ {i} (S) \geq v _ {i} (S) \quad \forall i, S,\tag{\((x_{i}(S))\) (DLP1}
$$

$$
\pi_ {s} - \sum_ {S _ {i} \in X} p _ {i} (S) \geq 0 \quad \forall X \in \mathbb {C},\tag{\((y(X))\}
$$

4DLP2a5

(6)

$$
\pi_ {s} + t (X) - \sum_ {S _ {i} \in X} p _ {i} (S) \geq 0\tag{\((y(X))\}
$$

$$
\pi_ {i}, \pi_ {s}, p _ {i} (S) \geq 0 \quad \forall i, S.\tag{DLP2b}
$$

The decision variables of the primal are $x _ { i } ( S )$ denoting whether bidder i wins package S and y4X5 denoting whether allocation X is realized or not. In the dual, $\pi _ { s }$ and $\pi _ { i }$ denote the auctioneers’ and bidder $i \prime \mathrm { s }$ profit, respectively, whereas $p _ { i } ( S )$ denotes the ask price for the package S and bidder i. Prices are summarized by $p .$ . Theorem 3.1 in Bikhchandani and Ostroy (2002) shows that allocation X and prices $p$ form a competitive equilibrium (CE) if X is an optimal solution to the primal $\mathrm { C A P } _ { 3 }$ and $( p , \pi _ { i } , \pi _ { S } )$ , where $\pi _ { i } , \pi _ { S }$ are payoffs resulting from X and prices p are an optimal solution to the corresponding dual linear program. Their proof is based on the resulting complementary slackness conditions. We show that additional allocation constraints causing additional infeasible solutions do not impact the theorem and the equivalence between competitive equilibrium and optimal solution to (5) is still given. Let us first enumerate the complementary slackness (CS) conditions:

$$
\left(\sum_ {S} x _ {i} (S) - 1\right) \pi_ {i} = 0 \quad \forall i,\tag{CS1}
$$

$$
\bigg (x _ {i} (S) - \sum_ {S _ {i} \in k} y (X) \bigg) p _ {i} (S) = 0 \quad \forall i, S,\tag{CS2}
$$

$$
\left(\sum_ {X} y (X) - 1\right) \pi_ {s} = 0,\tag{CS3}
$$

$$
y (X) t (X) = 0 \quad \forall X \in \mathbb {C} _ {u},\tag{CS4}
$$

$$
(\pi_ {i} + p _ {i} (S) - v _ {i} (S)) x _ {i} (S) = 0 \quad \forall i, S,\tag{CS5}
$$

$$
\bigg (\pi_ {s} - \sum_ {S _ {i} \in X} p _ {i} (S) \bigg) y (X) = 0 \quad \forall X \in \mathbb {C},\tag{CS6}
$$

$$
\bigg (\pi_ {s} + t (X) - \sum_ {S _ {i} \in X} p _ {i} (S) \bigg) y (X) = 0 \quad \forall   X \in \mathbb {C} _ {u}.\tag{CS7}
$$

The CE conditions are

$$
\pi_ {i} = \max _ {S} (v _ {i} (S) - p _ {i} (S)) \quad \forall i,\tag{CE1}
$$

$$
\pi_ {S} = \max _ {X \in \mathbb {C}} \sum_ {S _ {i} \in X} p _ {i} (S).\tag{CE2}
$$

Lemma 2. $( X ^ { * } , p ^ { * } )$ is a CE if and only if the integral solution dictated by $X ^ { \ast }$ is an optimal solution to primal $\mathrm { C A P } _ { 3 } \ ( 5 )$ and $( p ^ { * } , \pi _ { i } ^ { * } , \pi _ { S } ^ { * } )$ is an optimal solution to dual $\mathrm { C A P } _ { 3 }$ (6).

<sup>Proof.</sup> We follow the proof of Theorem 3.1 by Bikhchandani and Ostroy (2002) and show that the additional infeasible allocations due to additional allocation constraints do not violate the equivalence of competitive equilibrium and optimality of the winner determination problem. Due to the allocation constraints, additional complementary slackness conditions (CS4) and (CS7) do always hold because $y ( X ) = 0$ for the infeasible allocations (compare (LP4) and $y ( X ) \ge 0 )$ . Denote with S<sup>∗</sup> the package bidder i is assigned under allocation $X ^ { \ast }$

Sufficiency: Suppose the LP (5) has an integral solution $X ^ { \ast }$ with $x _ { i } ( \bar { S } ) ^ { \bar { } } = 1$ iff $S = S _ { i } ^ { * }$ and $y ( X ) = \overset { \vartriangle } { 1 }$ iff $X =$ $X ^ { \ast }$ . Let $( \pi _ { s } ^ { * } , \pi _ { i } ^ { * } , p ^ { * } , t ( X ^ { * } ) )$ be an optimal solution of the DLP $\begin{array} { r } { ( 6 ) . \ t ( X ^ { * } ) \geq \sum _ { S _ { i } \in X } p _ { i } ( S ) } \end{array}$ because it does not appear anywhere else than in (DLP2b) and the program minimizes $\pi _ { s }$ . (CS5) and (DLP1) imply the first CE condition (CE1). (DLP2a) and (DLP2b) imply

$$
\pi_ {s} \geq \max \left\{\max _ {X \in \mathbb {C}} \sum_ {S _ {i} \in X} p _ {i} (S), \max _ {X \in \mathbb {C} _ {u}} \sum_ {S _ {i} \in X} \left(p _ {i} (S) - t (X)\right) \right\}.
$$

Because $\begin{array} { r } { t ( X ^ { * } ) \geq \sum _ { S _ { i } \in X } p _ { i } ( S ) } \end{array}$ , the last term is always smaller or equal to zero, whereas the first term is always greater than or equal to zero. Because of (CS6) the above inequality implies the second CE condition (CE2). Hence $\hat { ( } X ^ { * } , \bar { p ^ { * } } )$ is a CE.

Necessity: Let $( X ^ { * } , p ^ { * } )$ be a CE. Therefore, by definition

$$
\pi_ {i} ^ {*} \equiv v _ {i} (S ^ {*}) - p _ {i} (S _ {i} ^ {*}) = \max _ {S} (v _ {i} (S) - p _ {i} (S)) \quad \forall i,\tag{CE1}
$$

$$
\pi_ {s} ^ {*} \equiv \sum_ {S _ {i} \in X ^ {*}} p _ {i} (S) = \max _ {X \in \mathbb {C}} \sum_ {S _ {i} \in X} p _ {i} (S).\tag{CE2}
$$

Let $x _ { i } ( S ) = 1$ iff $S = S _ { i } ^ { * }$ and $y ( X ) = 1$ iff $X = X ^ { * } .$ else 0. $X ^ { * }$ is a feasible solution to LP (5) because the allocation is supported in a CE equilibrium. Similarly, $( \pi _ { s } ^ { * } , \pi _ { i } ^ { * } , p ^ { * } , \bar { t } ( X ^ { * } ) )$ is feasible to DLP (6). The dual variable $t ( X )$ does not impact this equivalence. The remaining proof showing that the integral solution we just constructed is optimal is identical to the proof of Theorem 3.1 in Bikhchandani and Ostroy (2002). Q.E.D.

<sup>Definition</sup> <sup>11.</sup> A straightforward bidder bids only for those packages that maximize his payoff given the current ask prices.

<sup>Corollary</sup> <sup>2.</sup> The CAP formulation with allocation constraints (5) yields integral solutions and thus the efficient ascending CAs (iBundle, APA, dVSV ) terminate at a CE even if allocation constraints are present and bidders follow the straightforward bidding strategy.

This follows directly from Lemma 2 and the original proofs of the efficiency of iBundle (Parkes and Ungar 2000) and dVSV (de Vries et al. 2007). Parkes and Ungar (2000) show that all complementary slackness conditions except (CS1) are satisfied in each round of the iBundle auction. (CS1) states that every bidder with a positive utility for some packages at the current prices must receive a package in the allocation. Only in the last round is this condition satisfied for all bidders. The new complementary slackness conditions (CS4) and (CS7) due to allocation constraints are trivially satisfied because $y ( X )$ is null and do not impact the proof. Although the price updates in dVSV follow a primal dual algorithm, iBundle and APA can be considered subgradient algorithms (de Vries et al. 2007).

Ausubel and Milgrom (2006a) show that the APA (and therefore iBundle) terminates with an efficient solution and straightforward bidding is an ex post Nash equilibrium strategy when the BSM condition holds. The proof is defined on some coalitional value function, which might be implemented by $\mathrm { C A P } _ { 3 }$ but also a $\mathrm { C A P } _ { 3 }$ with additional allocation constraints, and it is therefore not affected by allocation constraints. In summary, allocation constraints neither have an impact on the efficiency of the family of efficient ascending CAs nor on the incentive properties. Although iBundle, the APA, and dVSV allow for allocation constraints, they do not explicitly take them into account in the pricing rule but implement simple price increments for subsets of bidders.

## 6. Efficiency and Equilibrium Analysis of FCAs

In what follows, we want to understand economical characteristics of FCAs and whether pricing rules such as WL and DL can also achieve 100% efficiency with a strong solution concept and how they relate to other efficient ascending CAs such as iBundle, APA, and dVSV introduced earlier. Except for the ask price calculation $( \mathrm { i . e . , }$ pricing rules), the following auctions $( \mathrm { F C A } _ { \mathrm { W L } }$ and $\mathrm { F C } \bar { \mathbf { A } } _ { \mathrm { D L } } )$ are equivalent to APA and iBundle. As in all other efficient ascending CAs, we will first assume a straightforward bidding strategy where the bidders only have to reveal their demand set in each round. We will show that whereas $\mathrm { F C A } _ { \mathrm { W L } }$ does not even lead to an efficient solution with this bidding strategy, $\mathrm { F C A _ { D L } }$ leads to an efficient outcome and straightforward bidding is an ex post equilibrium with buyer submodular valuations. Throughout we will assume an XOR bidding language.

## 6.1. FCA<sub>WL</sub>

In the $\mathrm { F C A } _ { \mathrm { W L } }$ auction, losing bidders in a round get an ask price of ${ \mathrm { W L } } ( S , i ) + \epsilon$ for a package S. In each round WLs for losing bids of losing bidders have to be calculated. This causes the $\mathrm { F C A } _ { \mathrm { W I } }$ to be an ascending CA, although generally WLs are not monotonically increasing as DLs are (see §3, Proposition 2).

Proposition 5. $\mathrm { F C A } _ { \mathrm { W L } }$ is an ascending CA.

<sup>Proof.</sup> It is more convenient to speak of auction rounds r than of states here. ${ \mathrm { W L } } _ { r } ( S , i )$ is only updated right after the submission of a bid $( S , v , r - 1 , \bar { i } )$ , and therefore ${ \mathrm { W L } } _ { r } ( S , i )$ can never be lower than the bid’s value $v .$ But v is equal to the ${ \mathrm { W L } } _ { r ^ { \prime } } ( S , i )$ presented to the bidder before the submission; hence, for any $r ^ { \prime } < r$ it holds ${ \mathrm { W L } } _ { r ^ { \prime } } ( S , i ) \leq { \mathrm { W L } } _ { r } ( S , i )$ (the round $r ^ { \prime }$ is either the previous round the bidder had bid on S or the first round). Q.E.D.

Table 5 Demand Masking Set of Bidder Valuations

<table><tr><td></td><td> $\mathcal{K}$ </td><td>Item  $I$ </td><td>Item  $I' \neq I$ </td></tr><tr><td>/th bidder</td><td> $V_b$ </td><td> $V_s$ </td><td>0</td></tr></table>

The efficiency of an $\mathrm { F C A } _ { \mathrm { W L } }$ can be as low as 0% if the bidders bid straightforwardly and valuations are demand masking.

<sup>Definition</sup> <sup>12.</sup> A demand masking set of bidder valuations is given if the following properties are fulfilled. For each item, there is one bidder. Each lth bidder values the big package that contains all items with $V _ { b }$ and the lth single item with $V _ { s } .$ All other package valuations are zero (see Table 5). We set m $\bar { V _ { s } } > \bar { V _ { b } } > \bar { V _ { s } }$ so that at the efficient allocation every bidder wins a single item.

Let $m = | \mathcal { K } |$ be the number of items. We will first provide an example with $m = 4 , \ V _ { s } = \mathfrak { H } 2$ , and $V _ { b } = \$ 5$ where $\mathrm { F C A } _ { \mathrm { W L } }$ is inefficient.

<sup>Example</sup> <sup>3.</sup> There are four bidders, B1 to $B 4 ,$ and four items, A to D. Table 6 indicates the auction progress. Prices are initialized to \$0. At the beginning, all bidders bid on the big package. When its price increases to \$3, then the losing bidders bid also on the single items because their payoff is \$2; i.e., it equals the payoff of the big package. Their bids on the single items are unsuccessful and the prices are updated to \$4. These updated prices exceed their valuations $V _ { s } = \$ 2;$ therefore, they never bid again on the single items and the auction fails to reach the efficient solution.

<sup>Theorem</sup> <sup>3.</sup> If bidder valuations are demand masking, the efficiency of $\operatorname { F C A } _ { \operatorname { W I } }$ with straightforward bidding converges to $2 / m$ in the worst case with $m > 1$

<sup>Proof.</sup> We distinguish two cases:

$$
V _ {b} \geq 2 V _ {s}.\tag{7}
$$

If inequality (7) holds, $\mathrm { F C A } _ { \mathrm { W L } }$ is inefficient. At the beginning, all bidders bid on the big package K. They do so until the round r at which its winning level exceeds $V _ { b } - V _ { s }$ and thus its payoff falls below the payoff of a single item. Denote with w the winner of the big package at this round. All other bidders lose. Their payoffs are higher for the single items than the big package and therefore they bid on them at the current price 0 (payoff4item $l ) = \bar { V } _ { s } - 0 > \mathrm { p a y o f f } ( \mathcal { K } ) = V _ { b } -$ $( V _ { b } - \bar { V } _ { s } + \delta ) \bar { = } \bar { V } _ { s } - \delta _ { \iota }$ , whereby  denotes a small constant). These bids of zero value are unsuccessful and the single item prices $( \mathrm { i . e . , }$ winning levels) for the next round amount to the winning bid of w, which was $V _ { b } - V _ { s }$ . Their payoff4item $l ) \stackrel { \smile } { = } V _ { s } - V _ { b } + V _ { s } = 2 V _ { s } - V _ { b }$ and payo $\mathsf { f } ( \mathcal { K } ) \stackrel { \cdot } { = } V _ { b } - V _ { b } + V _ { s } = V _ { s } >$ payoff4item l5 since $\dot { V _ { b } _ { b } } > V _ { s }$ . Thus they bid again on the big package. Furthermore, because of (7) their payoffs for the single items (equal to $2 V _ { s } - V _ { b } )$ are negative and they will never bid on them again. The auction ends by assigning the big package to an arbitrary bidder. The efficiency is $V _ { b } / ( \bar { m } \bar { V } _ { s } )$ and for $V _ { b } = 2 V _ { s } + \mathbf { \bar { \alpha } }$ , it becomes $( 2 + \delta ^ { \prime } ) / m$ . Thus for a large $m ,$ it converges to 0%. On the contrary, if (7) does not hold, the bidders will bid again on the small items at price $V _ { b } - V _ { s }$ when the payoff of the big package falls below $\mathrm { p a y o f f } ( \mathrm { i t e m } \ l ) =$ $\dot { 2 } \dot { V _ { s } } - V _ { b }$ . They win the single items and the auction ends with the efficient outcome. Note also that for $m = 2$ the reverse inequality (7) cannot be satisfied because of requirement m $\ d _ { 1 } V _ { s } > V _ { b } ,$ and hence the auction is efficient for $m = 2$ and inefficient for $m > 2 .$ Q.E.D.

Table 6 $\mathsf { F C A } _ { \mathsf { W L } }$ Process

<table><tr><td rowspan="2">Packages</td><td colspan="6"> $FCA_{WL}$ </td></tr><tr><td>A</td><td>B</td><td>C</td><td>D</td><td>ABCD</td><td>∅</td></tr><tr><td>Valuations</td><td> $2_1$ </td><td> $2_2$ </td><td> $2_3$ </td><td> $2_4$ </td><td> $5_1, 5_2, 5_3, 5_4$ </td><td></td></tr><tr><td>Round 1</td><td></td><td></td><td></td><td></td><td> $0_1^*, 0_2, 0_3, 0_4$ </td><td></td></tr><tr><td>Round 2</td><td></td><td></td><td></td><td></td><td> $0_1, 1_2^*, 1_3, 1_4$ </td><td></td></tr><tr><td>Round 3</td><td></td><td></td><td></td><td></td><td> $2_1^*, 1_2, 2_3, 2_4$ </td><td></td></tr><tr><td>Round 4</td><td></td><td> $0_2$ </td><td> $0_3$ </td><td> $0_4$ </td><td> $2_1, 3_2^*, 3_3, 3_4$ </td><td></td></tr><tr><td>Round 5</td><td> $0_1$ </td><td></td><td></td><td></td><td> $3_2, 4_3^*, 4_4$ </td><td></td></tr><tr><td>Round 6</td><td></td><td></td><td></td><td></td><td> $5_1^*, 5_2, 4_3, 5_4$ </td><td> $0_1, 0_2^*, 0_4^*$ </td></tr><tr><td>Round 7</td><td></td><td></td><td></td><td></td><td> $5_1^*, 5_2, 5_3, 5_4$ </td><td> $0_1, 0_2^*, 0_3^*, 0_4^*$ </td></tr><tr><td colspan="7">Termination</td></tr></table>

Although there might also be other bidder valuations leading to low efficiency, it is sufficient for our purposes to show that the efficiency of $\mathrm { F C A } _ { \mathrm { W L } }$ can actually be as low.

## 6.2. FCA<sub>DL</sub>

Contrary to the negative results on $\mathrm { F C A } _ { \mathrm { W L } }$ , we show that $\mathrm { F C A _ { D I } }$ leads to full efficiency with straightforward bidding, but it requires fewer rounds and fewer bids than iBundle and the APA. The only difference between $\mathrm { F C A _ { D L } }$ and $\operatorname { F C A } _ { \operatorname { W L } }$ is that in $\mathrm { F C A } _ { \mathrm { D L } }$ , ask prices are updated to ${ \mathrm { D L } } ( S , i ) + \epsilon$

<sup>Lemma</sup> <sup>3.</sup> DL ask prices are always higher than or equal to iBundle prices given the same bids.

Proof. <sub>Let</sub> $p _ { i } ^ { k } ( S )$ be the iBundle price after k bids are submitted. iBundle uses an XOR bidding language, and let $\mathrm { C A P } _ { k } ( S , i )$ denote the highest bid of i in S (bids of one bidder cannot be combined because of XOR): ${ \mathrm { C A P } } _ { k } ( S , i ) = \operatorname* { m a x } \{ v \mid ( T , v , k ^ { \prime } , i ) , T \subseteq S , k ^ { \prime } \leq$ k9. Equation (4) implies D $_ { \cdot _ { k } } ( S , i ) \geq \mathbf { C A P } _ { k } ( S , i )$ . The price update rules in iBundle ensure that in each round $\hat { p } _ { i } ^ { k } ( S ) = \operatorname* { m a x } \{ v \mid ( T , v , k ^ { \prime } , i ) , \ T \subseteq S , k ^ { \prime } \leq k \} + \epsilon$ (Parkes and Ungar 2000).<sup>12</sup> Thus $\mathrm { C A P } _ { k } ( S , i ) + \epsilon = p _ { i } ^ { k } ( S )$ and $\mathrm { { D L } } _ { k } ( S , i ) + \check { \epsilon } \geq p _ { i } ^ { k } ( S )$ . Q.E.D.

To prove the efficiency of $\mathrm { F C A } _ { \mathrm { D L } } ,$ we draw on the proof of optimality by Parkes and Ungar (2000) and show that optimality is not affected by the requirement to bid DLs +  instead of only an  above the last losing bid. Their proof works on a primal and a dual version of CAP, due to Bikhchandani and Ostroy (2002). This version is known as $\mathrm { C A P } _ { 2 }$ and is very similar to $\mathrm { C A P } _ { 3 }$ . The main difference is that its prices are anonymous and it corresponds to the auction iBundle(2). To prove the efficiency of iBundle(2), it is assumed that no single bidder bids on two nonoverlapping packages (safety condition). The efficiency of iBundle(3) or simply iBundle follows then directly from iBundle(2) (Parkes and Ungar 2000), and it can be dispensed with the safety condition.

Lemma 4. $\mathrm { F C A _ { D L } }$ terminates with the efficient solution and with CE prices if bidders bid straightforwardly.

<sup>Proof.</sup> The only modification of $\mathrm { F C A _ { \mathrm { D L } } }$ , i.e., to quote DLs instead of simple price updates, only affects the proof with respect to the complementary slackness condition (CS6). We only need to show that (CS6), which states that “the allocation must maximize the auctioneer’s profit at prices $p ( S )$ over all possible allocations and irrespective of bids received by agents,” is satisfied by $\mathrm { F C A _ { \mathrm { D L } } }$ too. Replace $p ( S )$ by DL4S5. From the DL computation follows that there is always a bidder or group of bidders willing to pay DL4S5 for every package in the valuemaximizing allocation $X _ { \mathrm { D L } } ^ { * }$ that is computed based on the prices (DLs) and irrespective of the bids. For this, observe that the highest possible DL4S5, which is the case when no bids are blockable, is equal to CAP4S5 considering all submitted bids. Hence there is always a bidder or a group of bidders willing to pay DL4S5. Therefore, allocation $X _ { \mathrm { D L } } ^ { * }$ with auctioneer’s profit $\sum _ { S ^ { * } \in X _ { \mathrm { D I } } ^ { * } }$ DL4S<sup>∗</sup>5 can be realized by assigning each $S ^ { * }$ to a subset of bidders $J ( S ^ { * } )$ $J ( S ^ { * } ) \subseteq { \mathcal { F } }$ with $\cap { \bar { J ( S ^ { * } ) } } = \emptyset$ . Every bidder receives at most one package, and hence the XOR constraint is not violated. The reason is that packages $S ^ { * }$ form a feasible allocation and are obviously nonoverlapping, and no single bidder bids on nonoverlapping packages because of the bid safety condition. In summary, we showed that it is always possible for the auctioneer to realize the profit maximizing allocation at prices DL4S5 irrespective of bids received because the computation of DLs ensures there are always bidders willing to take these prices.<sup>13</sup> Q.E.D.

Theorem 4. <sub>FC</sub> $\mathrm { \Delta A _ { D L } }$ is efficient if bidders follow the straightforward bidding strategy. This strategy is an ex post Nash equilibrium if the BSM condition holds.

Table 7 iBundle and $\mathsf { F C A } _ { \mathsf { D L } }$ Process

<table><tr><td rowspan="2">Packages</td><td colspan="4">iBundle</td><td colspan="4"> $FCA_{DL}$ </td></tr><tr><td>A</td><td>B</td><td>C</td><td>ABC</td><td>A</td><td>B</td><td>C</td><td>ABC</td></tr><tr><td>Valuations</td><td> $5_1$ </td><td> $5_2$ </td><td> $5_3$ </td><td> $8_4$ </td><td> $5_1$ </td><td> $5_2$ </td><td> $5_3$ </td><td> $8_4$ </td></tr><tr><td>Round 1</td><td> $1_1^*$ </td><td> $1_2^*$ </td><td> $1_3^*$ </td><td> $1_4$ </td><td> $1_1^*$ </td><td> $1_2^*$ </td><td> $1_3^*$ </td><td> $1_4$ </td></tr><tr><td>Round 2</td><td> $1_1^*$ </td><td> $1_2^*$ </td><td> $1_3^*$ </td><td> $2_4$ </td><td> $1_1$ </td><td> $1_2$ </td><td> $1_3$ </td><td> $4_4^*$ </td></tr><tr><td>Round 3</td><td> $1_1^*$ </td><td> $1_2^*$ </td><td> $1_3^*$ </td><td> $3_4$ </td><td> $2_1^*$ </td><td> $2_2^*$ </td><td> $2_3^*$ </td><td> $4_4$ </td></tr><tr><td>Round 4</td><td> $1_1$ </td><td> $1_2$ </td><td> $1_3$ </td><td> $4_4^*$ </td><td> $2_1$ </td><td> $2_2$ </td><td> $2_3$ </td><td> $7_4^*$ </td></tr><tr><td>Round 5</td><td> $2_1^*$ </td><td> $2_2^*$ </td><td> $2_3^*$ </td><td> $4_4$ </td><td> $3_1^*$ </td><td> $3_2^*$ </td><td> $3_3^*$ </td><td> $7_4$ </td></tr><tr><td>Round 6</td><td> $2_1^*$ </td><td> $2_2^*$ </td><td> $2_3^*$ </td><td> $5_4$ </td><td> $3_1^*$ </td><td> $3_2^*$ </td><td> $3_3^*$ </td><td> $∅_4^*$ </td></tr><tr><td>Round 7</td><td> $2_1^*$ </td><td> $2_2^*$ </td><td> $2_3^*$ </td><td> $6_4$ </td><td colspan="4">Termination</td></tr><tr><td>Round 8</td><td> $2_1$ </td><td> $2_2$ </td><td> $2_3$ </td><td> $7_4^*$ </td><td></td><td></td><td></td><td></td></tr><tr><td>Round 9</td><td> $3_1^*$ </td><td> $3_2^*$ </td><td> $3_3^*$ </td><td> $7_4$ </td><td></td><td></td><td></td><td></td></tr><tr><td>Round 10</td><td> $3_1^*$ </td><td> $3_2^*$ </td><td> $3_3^*$ </td><td> $8_4, ∅_4^*$ </td><td></td><td></td><td></td><td></td></tr><tr><td colspan="9">Termination</td></tr></table>

Theorem 4 follows directly from Lemma 4 and Ausubel and Milgrom (2006a).

$\mathrm { F C A _ { \mathrm { D L } } }$ can reduce the number of auction rounds, which is a considerable problem of iBundle as shown by Scheffel et al. (2011) and Schneider et al. (2010). The reason is that dead bids in iBundle, which will never be part of the winning allocation, are skipped and prices increase faster. We provide a simple example that $\mathrm { F C A } _ { \mathrm { D I } }$ can terminate with strictly less rounds than iBundle can.

<sup>Example</sup> <sup>4.</sup> Consider items A, $B ,$ and C are auctioned among bidders B1 to B4 in iBundle and $\mathrm { F C A } _ { \mathrm { D I } }$ using an increment of $\epsilon = 1$ . Bidders bid straightforwardly and are single minded, which means they value only one package positively and all others with zero. The exact valuations of each bidder and the auction rounds are described in Table 7. Ties are broken in favor of more winners.

The example illustrated in Table 7 shows that $\mathrm { F C A _ { D L } }$ reduces the number of auction rounds, the communication effort (because dead bids are not submitted), and also the computational effort. In general the reduction of auction rounds and communication effort comes at the price of higher computational effort because the $\Pi _ { 2 } ^ { P }$ -hard DL determination problem has to be solved several times.

In what follows, we introduce two economically motivated value models to demonstrate the benefits of $\mathrm { F C A } _ { \mathrm { D L } }$ concerning the number of auction rounds and the communication effort. Let RRR = 4rounds\_ iBundle − rounds $\mathrm { F C A } _ { \mathrm { D L } } ) /$ rounds\_iBundle denote the round reduction rate. Let C denote the communication effort measured as the number of all bids and ask prices exchanged. CRR = 4C\_iBundle $- \ C _ { - } \mathrm { F C A _ { D L } } ) /$ C\_iBundle is the corresponding reduction rate.

<sup>Definition</sup> <sup>13.</sup> Value model VM1 comprises m sin-$\mathrm { g l e }$ minded regional bidders who value pairwise nonoverlapping packages to at least \$ and one global bidder who values package K of all items to at least the sum of the valuations of the regional bidders.

<sup>Definition</sup> <sup>14.</sup> Value model VM2 comprises m single minded bidders with identical valuations for a specific package S, with $| S | > m - | \mathcal { K } | + 1 ; \mathrm { i . e . } $ , the complementary to S subauction is not too large and ensures the existence of blockable bids and thus high DL.

Theorem 5. <sub>In VM1</sub> $R R R = ( m - 1 ) / ( m + 1 )$ and $C R R = 1 / 2 - 1 / ( 2 m )$ . In VM2 RRR = CRR = 1/m.

The proofs are in Appendix A. It follows that in VM1 RRR → 100% and CRR → 50% for $m \to \infty$ . Surprisingly, in a realistic value model with regional and global bidders, which resembles the setting of FCC spectrum auctions, $\mathrm { F C A _ { \mathrm { D L } } }$ can substantially decrease the number of rounds and communication effort. In more generic VM2, which is the case when many bidders have homogeneous valuations, $R R R  5 0 \%$ and CRR → 50% for m = 2.

## 7. Numerical Experiments

The computational complexity results for exact DLs suggest that the computational costs outweigh the benefits. We supplement the theoretical analysis with an experimental comparison of $\mathrm { F C A _ { \mathrm { D L } } }$ and iBundle. Because there are hardly any real-world CA data sets available, we have adopted value models of the Combinatorial Auctions Test Suite (CATS; Leyton-Brown et al. 2000). In addition to CATS value models, we have used an extended version of the Pairwise Synergy value model from An et al. (2005). A more detailed description of the value models is provided in Appendix C, and the computation of DLs is described in Appendix B. For each value model we created 30 auction instances with different valuations and ran each of them with both auction formats. All auctions used a bid increment of 1. Table 8 depicts the results for small and medium sized auctions. We used the Symphony MIP solver (http://www.coin -or.org/SYMPHONY/) and computers with an Intel Core 2 CPU with 2.67 GHz and 4 GB main memory. Efficiency and final pay prices of both auction formats were the same (in accordance with §6.2). Hence, we report only on the reduction in rounds RRR, communication effort CRR, and the computation times.

In small size auctions (see Table 8) we observe a considerable reduction of the auction rounds across all value models and particularly in Pairwise Synergy+, where the maximum over the 30 auctions $( \dot { R } R R _ { \mathrm { m a x } } )$ is 47.945%. This is due to the existence of two bidder segments, regional and global, which leads to high RRR. The average CRR is greater than 30% in all value models except the Transportation value model, where bidders are only interested in a very limited set of packages. RF is the ratio of total run time of $\mathrm { F C A _ { \mathrm { D L } } }$ to iBundle. Surprisingly, despite the high computational complexity of ${ \mathrm { D L s } } ,$ the run times of $\mathrm { F C A } _ { \mathrm { D L } } ^ { - }$ are sometimes even lower than that of iBundle (see 8 where $R F < 1 )$ . The reason is the lower number of bids submitted, which shortens the winner determination in each round. The average computation time of a DL, denoted as PCT, ranges from 1.0 to 3.4 milliseconds only.

The mid-sized auctions with up to nine items led to higher computation times than iBundle because many more DLs had to be computed. Also in these experiments, computing a DL took between 1 ms and 170 ms only. The communication between auctioneer and bidders (CRR) was reduced substantially in all value models, but the total runtime RF increased.

Table 8 Comparison of $\mathsf { F C A } _ { \mathsf { D L } }$ to iBundle

<table><tr><td></td><td colspan="2">iBundle(3)</td><td colspan="2">DL</td><td colspan="2">iBundle(3)</td><td>DL</td></tr><tr><td rowspan="2">Real estate</td><td></td><td> $RRR_{max}$ </td><td>7.547%</td><td>Real estate</td><td></td><td> $RRR_{max}$ </td><td>1.190%</td></tr><tr><td></td><td> $CRR_{max}$ </td><td>49.222%</td><td></td><td></td><td> $CRR_{max}$ </td><td>49.029%</td></tr><tr><td>2 × 2 items</td><td>∅ R = 43.8</td><td>∅ RRR</td><td>3.395%</td><td>3 × 3 items</td><td>∅ R = 96.3</td><td>∅ RRR</td><td>0.513%</td></tr><tr><td rowspan="3">10 bidders</td><td>∅ C = 3,943.1</td><td>∅ CRR</td><td>44.995%</td><td>12 bidders</td><td>∅ C = 341,261.6</td><td>∅ CRR</td><td>45.976%</td></tr><tr><td></td><td>∅ RF</td><td>1.425</td><td></td><td></td><td>∅ RF</td><td>30.756</td></tr><tr><td></td><td>∅ PCT</td><td>3.402 ms</td><td></td><td></td><td>∅ PCT</td><td>169.377 ms</td></tr><tr><td rowspan="2">Transportation</td><td></td><td> $RRR_{max}$ </td><td>17.021%</td><td>Transportation</td><td></td><td> $RRR_{max}$ </td><td>0.000%</td></tr><tr><td></td><td> $CRR_{max}$ </td><td>13.584%</td><td></td><td></td><td> $CRR_{max}$ </td><td>19.790%</td></tr><tr><td>4 items</td><td>∅ R = 108.4</td><td>∅ RRR</td><td>5.333%</td><td>9 items</td><td>∅ R = 104.7</td><td>∅ RRR</td><td>0.000%</td></tr><tr><td rowspan="3">10 bidders</td><td>∅ C = 842.2</td><td>∅ CRR</td><td>5.635%</td><td>12 bidders</td><td>∅ C = 1,448.4</td><td>∅ CRR</td><td>4.519%</td></tr><tr><td></td><td>∅ RF</td><td>0.986</td><td></td><td></td><td>∅ RF</td><td>1.094</td></tr><tr><td></td><td>∅ PCT</td><td>1.252 ms</td><td></td><td></td><td>∅ PCT</td><td>1.596 ms</td></tr><tr><td rowspan="2">Pairwise synergy+</td><td></td><td> $RRR_{max}$ </td><td>47.945%</td><td>Pairwise synergy+</td><td></td><td> $RRR_{max}$ </td><td>29.132%</td></tr><tr><td></td><td> $CRR_{max}$ </td><td>39.447%</td><td></td><td></td><td> $CRR_{max}$ </td><td>24.314%</td></tr><tr><td>3 items</td><td>∅ R = 110.9</td><td>∅ RRR</td><td>36.625%</td><td>8 items</td><td>∅ R = 302.5</td><td>∅ RRR</td><td>5.001%</td></tr><tr><td rowspan="3">9 bidders</td><td>∅ C = 1,055.9</td><td>∅ CRR</td><td>30.028%</td><td>12 bidders</td><td>∅ C = 115,947.0</td><td>∅ CRR</td><td>21.022%</td></tr><tr><td></td><td>∅ RF</td><td>0.714</td><td></td><td></td><td>∅ RF</td><td>5.467</td></tr><tr><td></td><td>∅ PCT</td><td>1.025 ms</td><td></td><td></td><td>∅ PCT</td><td>8.862 ms</td></tr></table>

Notes. Left part for small size and right part for medium size auctions. $R R R _ { \mathrm { { m a x } } } = { \sf m a x }$ round reduction rate, $C R R _ { \mathrm { m a x } } = \mathfrak { m a x }$ communication reduction rate,  RRR = average round reduction rate,  CRR = average communication reduction rate,  $R F = \mathsf { a v e r a g e }$ runtime factor,  PCT = average price calculation time.

We conducted additional experiments with 10 items and 9 bidders in different value models, where bidders submit bids on every possible package. Also in these larger instances, the computation lasted only 1.48 seconds on average. Obviously, the computation time depends on many parameters such as the package size, the size of the complementary subauction, the number of bidders, and their bids. However, our results indicate that computing DLs in ascending auctions might well be used in practical applications.

## 8. Conclusion

Designing efficient combinatorial auctions turned out to be a challenging task. A few recent papers have described efficient and ascending combinatorial auctions that satisfy strong game theoretical solution concepts. In many applications the consideration of additional allocation constraints and flexibility in the choice of the bidding language are essential. These requirements have not been considered in the design of price feedback in the theoretical literature so far. It is important to extend the theory. This could increase the applicability of ascending combinatorial auctions in domains such as transportation or industrial procurement considerably and bear significant practical potential.

We consider ascending combinatorial auctions allowing for side constraints and OR as well as XOR bidding languages. We draw on the work by Adomavicius and Gupta (2005) and define winning and deadness levels (WLs and DLs) as a general pricing rule for ascending combinatorial auctions, which allow for different bidding languages and allocation constraints. This extension leads to a number of theoretical challenges. We show that straightforward bidding is an ex post equilibrium in ascending combinatorial auctions with $\mathrm { \hat { D } I s }$ and how this pricing rule can be integrated in the theoretical framework of efficient and ascending combinatorial auctions.

Although both iBundle and the $\mathrm { F C A _ { D L } }$ allow for allocation constraints, DLs take allocation constraints into account and actually lead to a lower number of auction rounds and bids that need to be submitted. The high number of auction rounds turned out to be one of the main obstacles for efficient ascending combinatorial auctions such as iBundle, APA, and dVSV. DLs come at a computational cost, however. The computation is a $\Pi _ { 2 } ^ { P }$ -complete problem. We show, however, that such ask prices can be calculated for up to 10 items and 9 bidders with realistic value models in less than 1.5 seconds in experiments, which suggests that these approaches might well be used in applications. Approximations to the exact computation of DLs could potentially be an area of future research.

These results provide a theoretical foundation for practical auction design. Such designs can leverage different pricing rules. Experimental research is required to gain insights on bidding behavior and efficiency in complex markets with allocation constraints.

## Acknowledgments

The financial support from the Deutsche Forschungsgemeinschaft [BI 1057/3-1] is gratefully acknowledged. The authors also thank Christian Kroemer and the anonymous reviewers.

## Appendix A. Proofs

Proposition 1.

$$
\mathrm{WL} _ {k} (S, i) = \mathrm{CAP} _ {k} (\mathcal {K}) - \mathrm{CAP} _ {k} (\mathcal {K}, S _ {i}).
$$

<sup>Proof.</sup> We give a self-contained proof that is based on the proof of Theorem $2$ of Adomavicius and Gupta (2005). We introduce the symbol $\mathbb { C } _ { k } ^ { E } ( S ) = \{ C ^ { \prime } \in C \cup E \mid \hat { C } \in \mathbb { C } _ { k } , E \in$ $\cup _ { i = 1 } ^ { I } ( S , 0 , 0 , i ) \cup \emptyset \} ^ { 1 \bar { 4 } }$ to denote the set of feasible allocations that can also include bids of zero value on $S . ^ { 1 5 }$ We define a binary relation ≺ on bid allocations to compare the values of two allocations: $C ^ { \prime } \prec C ^ { \prime \prime } \Rightarrow v ( C ^ { \prime } ) < v ( C ^ { \prime \prime } )$ where $v ( C ) =$ $\textstyle \sum _ { b \in C } v ( b )$ is the value of the allocation $\begin{array} { r } { C . \ S ( C ) = \bigcup _ { b \in C } S ( b ) } \end{array}$ denotes the items covered in allocation C. $W I N _ { k } ^ { E } ( \mathcal { K } , \bar { S } , i ) =$ max<sub>≺</sub> $\{ C \in \mathbb { C } _ { k } ^ { E } ( \mathcal { K } ) \mid ( S , 0 , 0 , i ) \in C \}$ represents the winning allocation of the whole auction at state k subject to the condition that bidder i wins S for free. We consider a new bid $b _ { k + 1 }$ of bidder i on package S at state $k + 1$ . Let $C _ { 1 } = \{ C \in$ $\mathbb { C } _ { k + 1 } ( \mathcal { K } ) \mid b _ { k + 1 } \in C \}$ and $\bar { C _ { 2 } } ^ { - } \bar { \{ C \in \mathbb { C } _ { k + 1 } } ( \mathcal { K } ) \mid b _ { k + 1 }  \notin C \}$ be the set of all allocations with and without $b _ { k + 1 } ,$ respectively. It holds $C _ { 1 } \cap C _ { 2 } = \mathcal { O }$ because they cannot share a common allocation (every allocation in $\dot { C _ { 1 } }$ contains $b _ { k + 1 }$ and every allocation in $C _ { 2 }$ does not) and $C _ { 1 } \cup C _ { 2 } = \mathbb { C } _ { k + 1 } ( \mathcal { K } )$ . Therefore,

$$
\begin{array}{c} W I N _ {k + 1} (\mathcal {K}) = \underset {\prec} {\max} \{C \in \mathbb {C} _ {k + 1} (\mathcal {K}) \} = \underset {\prec} {\max} \{C _ {1} \cup C _ {2} \} \\ = \underset {\prec} {\max} \Bigl \{\underset {\prec} {\max} C _ {1}, \underset {\prec} {\max} C _ {2} \Bigr \}, \end{array}\tag{A1}
$$

and because $b _ { k + 1 } \notin C \forall C \in C _ { 2 } ,$ it follows $C _ { 2 } = \mathbb { C } _ { k } ( \mathcal { K } )$ and

$$
\max _ {\prec} C _ {2} = \max _ {\prec} \mathbb {C} _ {k} (K) = W I N _ {k} (\mathscr {K}).\tag{A2}
$$

Furthermore,

$$
\begin{array}{l} \underset {\prec} {\max} C _ {1} = \underset {\prec} {\max} \bigl \{C \in \mathbb {C} _ {k + 1} (K) \mid b _ {k + 1} \in C \bigr \} \\ \qquad = \{b _ {k + 1} \} \cup \underset {\prec} {\max} \bigl \{C \backslash \{b _ {k + 1} \} \mid C \in \mathbb {C} _ {k + 1}, b _ {k + 1} \in C \bigr \} \\ \qquad = \{b _ {k + 1} \} \cup \underset {\prec} {\max} \bigl \{C \mid C \in \mathbb {C} _ {k} (K), S (C) \cap S (b _ {k + 1}) = \varnothing \bigr \} \\ \qquad = \{b _ {k + 1} \} \cup \underset {\prec} {\max} \bigl \{C \in \mathbb {C} _ {k} ^ {E} (\mathcal {K}), (S (b _ {k + 1}), 0, 0, i (b _ {k + 1})) \in C \bigr \} \\ \qquad = \{b _ {k + 1} \} \cup W I N _ {k} ^ {E} \bigl (\mathcal {K}, S (b _ {k + 1}), i (b _ {k + 1}) \bigr). \end{array}
$$

<sup>14</sup> In the referenced proof $\mathbb { C } _ { k } ( S )$ denotes the set of feasible allocations for subauction S. In our setting, note that $B _ { 1 } \in \mathbb { C } _ { k } ( S )$ and $B _ { 2 }$ ∈ $\mathbb { C } _ { k } ( \mathcal { K } \backslash S )$ does not imply that $B _ { 1 } \cup B _ { 2 } \in \mathbb { C } _ { k } ( \mathcal { K } )$ 5 because of allocation constraints. Thus, generally $\mathbb { C } _ { k } ( S )$ where $S \subset K$ is not defined.

The last equation together with (A1) and (A2) imply

$$
\begin{array}{l} W I N _ {k + 1} (\mathcal {K}) \\ \qquad = \max _ {\prec} \bigl \{W I N _ {k} (\mathcal {K}), \{b _ {k + 1} \} \cup W I N _ {k} ^ {E} \bigl (\mathcal {K}, S (b _ {k + 1}), i (b _ {k + 1}) \bigr) \bigr \} \text { and } \\ b _ {k + 1} \in W I N _ {k + 1} \iff v (W I N _ {k}) <   v (b _ {k + 1}) \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad + v \bigl (W I N _ {k} ^ {E} \bigl (\mathcal {K}, S (b _ {k + 1}), i (b _ {k + 1}) \bigr) \bigr). \end{array}
$$

Thus, for a new bid $b _ { k + 1 }$ to win, its value $v ( b _ { k + 1 } )$ together with $v ( W I N _ { k } ^ { E } ( \mathcal { K } , S ( b _ { k + 1 } ) , i ( b _ { k + 1 } ) ) )$ which is the value of CAP subject to the constraint that the bidder $i ( b _ { k + 1 } )$ wins $S ( b _ { k + 1 } )$ for free (we denoted this CAP as $\mathsf { C A P } ^ { k } ( \mathcal { K } , S _ { i } ) )$ must exceed $v ( W I N _ { k } )$ , which is the current value $\mathbf { C A P } ^ { k } ( { \mathcal { K } } )$ . This completes the proof. Q.E.D.

Proposition 2.

(b) DL 4S1 i5 ≤ WL 4S1 i5; and

<sup>Proof.16</sup> (a) Assume $\mathrm { D L } _ { k + 1 } ( S , i ) < \mathrm { D L } _ { k } ( S , i )$ . Denote with  a very small positive number. Then $\mathrm { D L } _ { k } ( S , i )$ implies that $\vec { \mathbb { d } } k ^ { \prime } > k \colon ( \mathring { S , } \mathrm { D L } _ { k } ( S , i ) - \varepsilon , k ^ { \prime } , i ) \in W I N _ { k ^ { \prime } } ( \mathcal { K } ) \Rightarrow \vec { \mathbb { d } } k ^ { \prime } >$ $k \colon ( S , \mathrm { D L } _ { k + 1 } ( S , i ) , k ^ { \prime } , i ) \in W I N _ { k ^ { \prime } } ( \mathcal { K } )$ (because we assumed $\mathrm { D L } _ { k + 1 } ( S , i ) < \mathrm { D L } _ { k } ( S , i ) )$ . But $\mathrm { D L } _ { k + 1 } ( S , i )$ implies that $\exists k ^ { \prime } >$ $k + 1 \colon ( S , \mathrm { D L } _ { k + 1 } ( S , i ) , k ^ { \prime } , i ) \in W I N _ { k ^ { \prime } } ( \mathcal { K } )$ . Contradiction.

In words, all bids below ${ \mathrm { D L } } _ { k } ( S , i )$ are destined to lose whatever happens in future auction states. But in the future state $k + 1$ a bid amounting to $\mathrm { D L } _ { k + 1 } ( S , i )$ and thus below $\mathrm { D L } _ { k }$ has a chance to win in a state greater than $k + 1$ . Therefore ${ \mathrm { D L } } _ { k } ( S , i )$ is not minimal and by definition not a DL.

(b) Assume $\mathrm { D L } _ { k } ( S , i ) > { \mathrm { W L } } _ { k } ( { \bar { S , \ i } } )$ . The WL definition implies that the bid $( S , \mathrm { W L } _ { k } ( S , i ) , k + 1 , i ) \in W I N _ { k + 1 } ( \mathcal { K } )$ The DL definition together with the assumption $\mathrm { D L } _ { k } ( S , i ) >$ ${ \mathrm { W L } } _ { k } ( S , i )$ implies that $\nexists k ^ { \prime } \ > \ k : ( S , \bar { \mathsf { W L } } _ { k } ( S , i ) , k ^ { \prime } , i ) \ \in$ $W I N _ { k ^ { \prime } } ( \mathcal { K } )$ . Contradiction.

In words, the DL is the minimal price to win the item in a possible future auction state. The WL is the minimal price to win it at the next state; thus, it cannot be lower.

(c) $( \mathcal { K } , v , k + 1 , i ) \in W I N _ { k + 1 } ( \mathcal { K } ) \Rightarrow v \geq \mathbf { C A P } _ { k } ( \mathcal { K } )$ . Thus the minimum v, i.e., the WL, is ${ W \mathrm { L } } _ { k } ( \mathcal { K } ) = { \mathrm { C A P } } _ { k } ( \mathcal { K } )$ . Furthermore if $v < \mathrm { C A P } _ { k } ( \mathcal { K } ) \Rightarrow \exists k ^ { \prime } > k \colon ( S , v , k + 1 , i ) \in W I N _ { k ^ { \prime } } ( \mathcal { K } )$ because by $\mathrm { C A P \ d e f i n i t i o n \ } k ^ { \prime } > k \Rightarrow \mathrm { C A P } _ { k ^ { \prime } } ( \mathcal { K } ) \geq \mathrm { C A P } _ { k } ( \mathcal { K } )$ Thus $\mathrm { D L } _ { k } ( \mathcal { K } , i ) = \mathrm { C A P } _ { k } ( \mathcal { K } ) = \mathsf { W L } _ { k } ( \mathcal { K } , i )$

In words, to win in the next auction state all auctioned items, a bidder must bid at least the current auction value. Every lower bid will not be winning in any future auction state because the auction value will not sink. Q.E.D.

Theorem 5. <sub>In</sub> $V M { 1 } ~ R R R = ( m - 1 ) / ( m + 1 )$ and $C R R =$ $1 / 2 - 1 / ( 2 m )$ . In VM2 $R R R = C R R = 1 / m .$

<sup>Proof.</sup> VM1: In each round, either the coalition of the global bidder alone wins or the coalition of all regional bidders. Denote a round as G if the global bidder wins, else as S. We consider the sequence of rounds that comprises two consecutive winning rounds for the global bidder. In $\mathrm { F C A } _ { \mathrm { D L } }$ the coalitions win alternately; thus, the sequence is GSG. After a $G ,$ each regional bidder increases his bid by $\epsilon ,$ and after an $S ,$ the global bidder by m because his DL increases by this amount. In $\mathrm { F C A _ { \mathrm { D L } } }$ the sequence is m

GSG, whereas in iBundle $G { \overbrace { S \cdots S } } ^ { \longleftrightarrow } G$ . RRR and CRR equal to the reductions rates of this cyclical sequence, excluding the last G. Thus $R R R = ( m + 1 - \dot { 2 } ) / ( m + 1 ) \dot { = } ( m - 1 ) / ( m + \ddot { 1 } )$ and $C R R = ( 2 m - ( m + 1 ) ) / ( 2 m ) = 1 / 2 - 1 / ( 2 m )$

VM2: Every bidder bids on the same package. Let $p _ { r }$ denote its highest price over all bidders at round r. In $\mathrm { F C A _ { \mathrm { D L } } }$ $p _ { r }$ increases by  after each round. In iBundle it can be easily seen that in every m consecutive rounds, there is one round where $p _ { r }$ remains unchanged because all losing bidders just level the price of the previously winning bid; thus, on average, the price increase is $( 1 - 1 / m ) \epsilon$ . The number of rounds is equal to the final price $p ^ { T }$ divided by the average price increase; thus $R R R = ( 1 - \dot { 1 } / m ) ( \epsilon - \epsilon ) / ( \bar { ( 1 - 1 / m ) } \epsilon ) \stackrel {  } { = }$ $( m - 1 ) / ( m + 1 )$ . Regarding CRR, in iBundle each bidder submit $( p ^ { f i n a l } ) / \epsilon ^ { - } + 1$ bids. In $\mathrm { F C A } _ { \mathrm { D L } } ,$ without loss of generality, we assume that all but two bidders always lose (tie breaking). These two bidders alternately increase their bids by $2 \epsilon ,$ and the computational effort for these two is equal to the effort for one of the always losing bidders. Thus $C R R = ( m ( p ^ { T } / \epsilon + 1 ) - ( m - 1 ) ( p ^ { T } / \dot { \epsilon } + 1 ) ) / \nonumber$ $( \breve { m } ( p ^ { T } / \epsilon + 1 ) ) = 1 / m . \mathrm { Q . E . D }$

## Appendix B. Computation of DLs for an XOR Bid Language

We proceed according to the two-phase method and first seek for simultaneously blockable bid sets. We observe that a winning bid of bidder j on a single item $l \in \mathcal { K } \backslash S$ suffices to simultaneously block all his bids in S. Consequently, the number of foreign bidders, whose bids in S are simultaneously blockable, amounts to K\S. If this number is greater than or equal to the number of all foreign bidders in S who have a least one non-i-dominated bid in S, denoted as $n _ { S } ,$ we are done. All of them can be blocked and DL is equal to the highest bid of i in S; i.e., he must overbid only his own bids. Otherwise we proceed to phase 2 and determine which bidder set leads, if removed from subauction $S ,$ to the minimum CAP value in $S . ^ { 1 7 } \mathrm { ~ I f ~ } \left| S \right| = 1$ or if all bids in S are overlapping, it is easy to find which bidders should be removed: the ones with the highest bids. But the general case is obviously combinatorial and requires solving the CAP for each of the $\binom { n _ { S } } { n _ { S } - | \mathcal { K } \backslash S | } = \binom { n _ { S } } { | \mathcal { K } \backslash S | }$ bidder sets remaining after removing the blockable ones. The pseudocode is given in 1.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1 (DL XOR algorithm)
Input: Package S, bidder i
Set of bids  $B_{S,k,-i}^{ndom}$ 
Output: DL(S, i)
1: lowerBound ←  $\max_{b}\{v(b): i(b) = i, S(b) \subseteq S\}$ 
2: DL(S, i) ← ∞
3: F ← getForeignBiddersOnPackage(S, i)
4: if |F| ≤ |K\S| then
</div>

5: DL4S1 i5 ← lowerBound 6: else 7: for all $\mathcal { F } _ { i } \subset \mathcal { F } \colon | \mathcal { F } _ { i } | = | \mathcal { K } \backslash S |$ do 8: $t h i s P r i c e \longleftarrow \mathrm { C A P } ( S , B _ { S , k } \backslash \{ b ^ { \prime } \mid b ^ { \prime } \in B _ { S , k , - i } ^ { \mathrm { n d o m } } , i ( b ^ { \prime } ) \in \mathcal { F } _ { i } \} )$ 9: if $t h i s P r i c e < \mathrm { D L } ( S , i )$ 10: $\operatorname { D L } ( S , i )  t h i s P r i c e$ 11: end if 12: if DL4S1 i5 = lowerBound then 13: break for 14: end if 15: end for 16: end if 17: return DL4S1 i5.

The outlined calculation of XOR DL can serve as a basis to calculate DL for a number of other constrained cases, surprisingly even for cases with the OR bidding language. We provide an example because this cannot be claimed for every conceivable case.

<sup>Proposition</sup> <sup>6.</sup> The DL4S1 i5 for the OR bidding language in presence of the constraint “max a winners” can be calculated as XOR DL.

<sup>Proof.</sup> The most opportune case for bidder i to win S is when he places a huge bid on a item of the complementary subauction K\S so that he is surely among the a winners<sup>18</sup> and additionally some bidders leading to the highest $\mathrm { C A P } ( S )$ are not among the a winners because other $^ { \prime \prime } \mathrm { l o w } ^ { \prime \prime }$ bidders in S place huge bids in K\S. Together with bidder i, min4a − 11 K\S − 15 foreign bidders can win in ${ \mathcal { K } } \backslash S$ and all other max $( n _ { S } - \operatorname* { m i n } ( a - 1 , | \mathcal { K } \backslash S | - 1 ) , 0 )$ foreign bidders in S can be simultaneously blocked. Knowing this, we can proceed to calculate DL4S1 i5 as in the XOR DL case by solving one CAP for each bidder set of the derived cardinality. Q.E.D.

## Appendix C. Value Models

The Real Estate value model is based on the Proximity in Space model from CATS (Leyton-Brown et al. 2000). Items sold in the auction are the real estate lots l, which have valuations $v _ { l }$ drawn from the same normal distribution for each bidder. Adjacency relationships between two pieces of land m and n $( e _ { m n } )$ are created randomly for all bidders. There is a 90% probability of a vertical or horizontal edge and an 80% probability of a diagonal edge. Edge weights $w _ { m n }$ are then generated randomly for each bidder (mean 0.4, deviation 0.2), and they are used to determine package valuations of adjacent pieces of land: $\begin{array} { r } { v ( S ) = ( 1 + \sum _ { e _ { m n } : m , n \in S } w _ { m n } ) \sum _ { l \in S } v _ { l } } \end{array}$

The Transportation value model uses the Paths in Space model from CATS (Leyton-Brown et al. 2000). It models a nearly planar transportation graph in Cartesian coordinates, where each bidder is interested in securing a path between two randomly selected vertices (cities). The items traded are edges (routes) of the graph. Parameters for the Transportation value model are the number of items (edges) m and graph density $\rho ,$ which defines an average number of edges per city, and is used to calculate the number of vertices as $( m * 2 ) / \rho .$ . The bidder’s valuation for a path is defined by the Euclidean distance between two nodes multiplied by a random number drawn from a uniform distribution. Consequently, only a limited number of packages, which represent paths between both selected cities, are valuable for the bidder. This allows us to consider even larger transportation networks in a reasonable time. In our simulations we set the mean of $\rho$ to 1.8 and 2.5 for the small and medium size auctions, respectively. The standard deviation was set to 0.25.

The Pairwise Synergy value model in An et al. (2005) is defined by a set of valuations of individual items 8v 9 and a matrix of pairwise item synergies $\{ \mathrm { s y n } _ { k , l } \colon k , l \in \mathcal { K } , \mathrm { s y n } _ { k , l } =$ $\mathbf { s y n } _ { l , k } , \mathbf { s y n } _ { k , k } = 0 \}$ . The valuation of a package S is then calculated as

$$
v (S) = \sum_ {k = 1} ^ {| S |} v _ {k} + \frac {1}{| S | - 1} \sum_ {k = 1} ^ {| S |} \sum_ {l = k + 1} ^ {| S |} \operatorname{syn} _ {k, l} (v _ {k} + v _ {l}).
$$

A synergy value of 0 corresponds to completely independent items, and the synergy value of 1 means that the package valuation is twice as high as the sum of the individual item valuations. The relevant parameters for the Pairwise Synergy value model are the interval for the randomly generated item valuations, set to 60001 30007, and the interval for the randomly generated synergy values, set to 60001 2007. In Pairwise Synergy +we specified additionally two bidder segments. In small size auctions, six bidders were interested in packages of cardinality 1 and three bidders of cardinality 3. In medium size auctions, eight bidders were interested in packages of cardinality in the interval 611 37 and four in the interval 671 87.

## References

Adomavicius G, Gupta A (2005) Toward comprehensive real-time bidder support in iterative combinatorial auctions. Inform. Systems Res. 16(2):169–185.

Adomavicius G, Curley S, Gupta A, Sanyal P (2012) A data-driven exploration of bidder strategies in continuous combinatorial auctions. Management Sci. 58(4):811–830.

An N, Elmaghraby W, Keskinocak P (2005) Bidding strategies and their impact on revenues in combinatorial auctions. J. Revenue Pricing Management 3(4):337–357.

Ausubel L, Milgrom P (2002) Ascending auctions with package bidding. Frontiers Theoret. Econom. 1:1–42.

Ausubel L, Milgrom P (2006a) Ascending proxy auctions. Cramton P, Shoham Y, Steinberg R, eds. Combinatorial Auctions (MIT Press, Cambridge, MA), 79–98.

Ausubel L, Milgrom P (2006b) The lovely but lonely vickrey auction. Cramton P, Shoham Y, Steinberg R, eds. Combinatorial Auctions (MIT Press, Cambridge, MA), 17–40.

Bapna R, Das S, Garfinkel R, Stallaert J (2007) A market design for grid computing. INFORMS J. Comput. 20(1):100–111.

Bichler M, Gupta A, Ketter W (2010) Designing smart markets. Inform. Systems Res. 21(4):688–699.

Bichler M, Shabalin P, Pikovsky A (2009) A computational analysis of linear-price iterative combinatorial auctions. Inform. Systems Res. 20(1):33–59.

Bichler M, Shabalin P, Ziegler G (2011) Efficiency with linear prices? A theoretical and experimental analysis of the combinatorial clock auction. TUM Technical report, Munich.

Bichler M, Davenport A, Hohner G, Kalagnanam J (2006) Industrial procurement auctions. Cramton P, Shoham Y, Steinberg R, eds. Combinatorial Auctions (MIT Press), 593–612.

Bikhchandani S, Ostroy JM (2002) The package assignment model. J. Econom. Theory 107(2):377–406.

Brunner C, Goeree JK, Ch. Holt, Ledyard J (2010) An experimental test of flexible combinatorial spectrum auction formats. Amer. Econom. J.: Micro-Econom. 2(1):39–57.

Cantillon E, Pesendorfer M (2006) Auctioning bus routes: The London experience. Cramton P, Shoham Y, Steinberg R, eds. Combinatorial Auctions (MIT Press, Cambridge, MA), 573–592.

Caplice C (2007) Electronic markets for truckload transportation. Production Oper. Management 16(4):423–436.

Conitzer V, Sandholm T (2002) Vote elicitation: Complexity and strategy-proofness. AAAI 392–397.

Cramton P (2009) Spectrum auction design. Technical report, University of Maryland, Department of Economics, College Park, http://ideas.repec.org/p/pcc/pccumd/09sad.html.

Cramton P, Shoham Y, Steinberg R, eds. (2006) Combinatorial Auctions (MIT Press, Cambridge, MA).

de Vries S, Schummer J, Vohra R (2007) On ascending Vickrey auctions for heterogeneous objects. J. Econom. Theory 132(1):95–118.

Dobzinski S, Lavi R, Nisan N (2008) Multi-unit auctions with budget limits. Foundations of Computer Science (Philadelphia), 260–269.

Engel K (1997) Sperner Theory (Cambridge University Press).

Garey MR, Johnson DS, eds. (1972) Computers and Intractability— A Guide to the Theory of NP-Completeness (W. H. Freeman and Company, New York).

Green J, Laffont J-J (1977) Characterization of satisfactory mechanisms for the revelation of preferences for public goods. Econometrica 45:427–438.

Guo Z, Koehler GJ, Whinston AB (2007) A market-based optimization algorithm for distributed systems. Management Sci. 53(8):1345–1358.

Ko KI, Lin CL (1995) On the complexity of min–max optimization problems and their approximation. Du DZ, Pardalos PM, eds. Minimax and Applications (Kluwer Academic Publishers), 219–240.

Kwasnica T, Ledyard JO, Porter D, DeMartini C (2005) A new and improved design for multi-objective iterative auctions. Management Sci. 51(3):419–434.

Lehmann D, Mueller R, Sandholm T (2006) The winner determination problem. Cramton P, Shoham Y, Steinberg R, eds. Combinatorial Auctions (MIT Press, Cambridge, MA), 297–318.

Leyton-Brown K, Pearson M, Shoham Y (2000) Towards a universal test suite for combinatorial auction algorithms. ACM Conf. Electronic Commerce, 66–76.

Mishra D, Parkes D (2007) Ascending price Vickrey auctions for general valuations. J. Econom. Theory 132(1):335–366.

Myerson RB (1981) Optimal auction design. Math. Oper. Res. 6:58–73.

Nisan N (2006) Bidding languages. Cramton P, Shoham Y, Steinberg R, eds. Combinatorial Auctions (MIT Press, Cambridge, MA), 215–252.

Nisan N, Segal I (2006) The communcation requirements of efficient allocations and supporting prices. J. Econom. Theory 129:192–224.

Papadimitriou CH, ed. (1993) Computational Complexity (Addison Wesley).

Parkes D, Ungar LH (2000) Iterative combinatorial auctions: Theory and practice. 17th National Conf. Artificial Intelligence (AAAI-00).

Porter D, Rassenti S, Roopnarine A, Smith V (2003) Combinatorial auction design. Proc. Natl. Acad. Sci. USA 100: 11153–11157.

Rothkopf MH (2007) Thirteen reasons why the Vickrey-Clarke-Groves process is not practical. Oper. Res. 55:191–197.

Rothkopf MH, Pekec A, Harstad RM (1998) Computationally manageable combinatorial auctions. Management Sci. 44:1131–1147.

Sandholm T (2003) Making markets and democracy work: A story of incentives and computing. Proc. Internat. Joint Conf. Artificial Intelligence, 1649–1671.

Sandholm T, Suri S (2001) Market clearability. Proc. Internat. Joint Conf. Artificial Intelligence (IJCAI).

Sandholm T, Suri S (2006) Side constraints and non-price attributes in markets. Games Econom. Behav. 55:321–330.

Scheffel T, Pikovsky A, Bichler M, Guler K (2011) An experimental comparison of linear and non-linear price combinatorial auctions. Inform. Systems Res. 22(2):346–368.

Schneider S, Shabalin P, Bichler M (2010) On the robustness of nonlinear personalized price combinatorial auctions. Eur. J. Oper. Res. 206(1):248–259.

Seifert S, Ehrhart KM (2005) Design of the 3G spectrum auctions in the UK and Germany: An experimental investigation. German Econom. Rev. 6(2):229–248.

Shoham Y, Leyton-Brown K (2009) Multiagent Systems: Algorithmic, Game-Theoretic, and Logical Foundations (Cambridge University Press).

Umans C (2000) Approximability and completeness in the polynomial hierarchy. Ph.D. thesis, University of California at Berkeley.

Xia M, Koehler GJ, Whinston AB (2004) Pricing combinatorial auctions. Eur. J. Oper. Res. 154(1):251–270.
