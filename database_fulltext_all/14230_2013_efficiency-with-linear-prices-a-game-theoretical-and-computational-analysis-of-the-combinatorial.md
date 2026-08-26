---
otero_id: 14230
otero_key: "MTTYMXJP"
title: "Efficiency with Linear Prices? A Game-Theoretical and Computational Analysis of the Combinatorial Clock Auction"
authors: "Martin Bichler; Pasha Shabalin; Georg Ziegler"
year: "2013"
journal: "Information Systems Research"
doi: "10.1287/isre.1120.0426"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/MTTYMXJP/fulltext/images/f72b4bed144600a3bdc61ab932f9537ba9f6788c35f42186141d96f275d403a6.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Efficiency with Linear Prices? A Game-Theoretical and Computational Analysis of the Combinatorial Clock Auction

Martin Bichler, Pasha Shabalin, Georg Ziegler,

To cite this article:

Martin Bichler, Pasha Shabalin, Georg Ziegler, (2013) Efficiency with Linear Prices? A Game-Theoretical and Computationa Analysis of the Combinatorial Clock Auction. Information Systems Research 24(2):394-417. http://dx.doi.org/10.1287/ isre.1120.0426

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2013, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/MTTYMXJP/fulltext/images/513a2cf9496c8301e6f73e8843d558584a49d903bec4021d10577d07ad4c0f6a.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Efficiency with Linear Prices? A Game-Theoretical and Computational Analysis of the Combinatorial Clock Auction

Martin Bichler, Pasha Shabalin, Georg Ziegler Department of Informatics, TU München, Germany {bichler@in.tum.de, shabalin@in.tum.de, zieglerg@in.tum.de}

ombinatorial auctions have been suggested as a means to raise efficiency in multi-item negotiations with complementarities among goods because they can be applied in procurement, energy markets, transportation, and the sale of spectrum auctions. The combinatorial clock (CC) auction has become very popular in these markets for its simplicity and for its highly usable price discovery, derived by the use of linear prices. Unfortunately, no equilibrium bidding strategies are known. Given the importance of the CC auction in the field, it is highly desirable to understand whether there are efficient versions of the CC auction providing a strong game theoretical solution concept. So far, equilibrium strategies have only been found for combinatorial auctions with nonlinear and personalized prices for very restricted sets of bidder valuations. We introduce an extension of the CC auction, the CC+ auction, and show that it actually leads to efficient outcomes in an ex post equilibrium for general valuations with only linear ask prices. We also provide a theoretical analysis on the worst case efficiency of the CC auction, which highlights situations in which the CC leads to highly inefficient outcomes. As in other theoretical models of combinatorial auctions, bidders in the field might not be able to follow the equilibrium strategies suggested by the game-theoretical predictions. Therefore, we complement the theoretical findings with results from computational and laboratory experiments using realistic value models. The experimental results illustrate that the CC+ auction can have a significant impact on efficiency compared to the CC auction.

Key words: electronic market; combinatorial auction; allocative efficiency

History: Chris Dellarocas, Senior Editor; Gediminas Adomavicius, Associate Editor. This paper was received October 10, 2010, and was with the authors for 6 months for 3 revisions. Published online in Articles in Advance July 27, 2012.

## 1. Introduction

The development of the Internet allowed for the exchange of complex preference profiles and laid the foundation for the design of new market mechanisms. The promise of these mechanisms is that by allowing market participants to reveal more comprehensive information about cost structures or utility functions, they can increase allocative efficiency and lead to higher economic welfare. In recent years, a growing body of literature in the management sciences is devoted to the design of such smart markets (McCabe et al. 1991, Gallien and Wein 2005), with combinatorial auctions (CAs) emerging as a pivotal example (Cramton et al. 2006b). In CAs, multiple items are sold simultaneously and they allow bids on packages of items. Nowadays, CAs are being used for the sale of spectrum licenses in Europe and the United States (Cramton 2009), for transportation (Caplice and Sheffi 2006), and in industrial procurement (Bichler et al. 2006, Sandholm et al. 2006). Much recent research in information systems (IS) is devoted to the design and analysis of CAs and respective decision support tools (Adomavicius and Gupta 2005, Xia et al. 2004, Bapna et al. 2007, Guo et al. 2007, Bichler et al. 2009, Scheffel et al. 2011). A summary of recent and emerging research in IS can be found in Bichler et al. (2010).

Although CAs yield higher levels of efficiency in the lab in the case of complementarities compared to simultaneous auctions without package bids, equilibrium strategies are unknown for many CA formats used in the field. The exponential number of possible package bids leads to high strategic complexity for bidders. The bidding strategies observed in the lab are diverse, with some bidders bidding on many and others bidding on only a few packages of interest in each round (Goeree and Holt 2010, Scheffel et al. 2011). Developing efficient CA designs that satisfy a strong game-theoretical solution concept can help reduce the strategic complexity and lead to higher efficiency. Even if the assumption for such equilibrium strategies is not given in particular applications, it helps to understand the sources of inefficiency observed in the lab or in the field.

Green and Laffont (1977) already proved that an efficient mechanism in which honest revelation is a dominant strategy for each agent is necessarily a Vickrey-Clarke-Groves (VCG) mechanism. Although this initially appeared to be the silver bullet for the design of CAs, VCG mechanisms turned out to be impractical in most applications (Ausubel and Milgrom 2006b, Rothkopf 2007). For single-item auctions, not only the Vickrey auction but also the ascending Clock auction (aka Japanese auction) is individually rational, efficient, and has a dominant strategy (i.e., it is strategy-proof). Iterative CA (ICA) formats do not require bidders to submit all their valuations in a single round. In addition, Milgrom and Weber (1982) show for single-item auctions that if there is affiliation in the values of bidders, then sealedbid auctions are less efficient than iterative auctions.

For situations with multiple items but unit demand (Demange et al. 1986) and for multiple homogeneous goods with marginal decreasing values (Green and Laffont 1979, Holmstrom 1979), it has been shown that there are generalizations that can be used to implement efficient, strategy-proof mechanisms. Finding efficient auctions with strong incentive properties turns out to be much harder for CAs with general valuations. Although “strategy proofness” might not be possible, researchers have been trying to find iterative CAs that still satisfy a strong solution concept, such as an ex post equilibrium, for restricted types of valuations. For the design of electronic multiitem markets, it is of significant interest whether such auction designs exist at all and which assumptions they require. Ex post equilibria in particular avoid speculation about other bidders’ valuations and could therefore reduce the strategic complexity for bidders considerably, leading to higher efficiency and also an increased adoption of CAs. Ex post equilibria can be considered a strong solution concept (Nisan 2007), and they are practically attractive because Bayes-Nash equilibria require prior distributional assumptions on the bidders’ types, which might be impractical in combinatorial auctions with an exponential number of possible packages.

## 1.1. Iterative Combinatorial Auctions

So far, the ascending proxy auction (Ausubel and Milgrom 2006a), iBundle(3) (Parkes and Ungar 2000), and the dVSV auction (de Vries et al. 2007) are the only known ICAs that achieve full efficiency for restricted types of bidder valuations. If the buyer submodularity condition<sup>1</sup> is satisfied, straightforward bidding is a best-response strategy that leads to an ex post equilibrium and the auction results in the

VCG outcome (Ausubel and Milgrom 2002). Straightforward bidding means that bidders only bid on those packages that maximize their payoff based on current ask prices. These auction formats are based on nonlinear and personalized prices<sup>2</sup> and can be modeled as an algorithm (primal-dual or subgradient) to solve the corresponding linear program. We refer to these auction formats as nonlinear personalized price auctions (NLPPAs) in the following.

If the bidders’ valuations in an NLPPA are not buyer submodular, bidders have an incentive to shade their bids and deviate from the straightforward strategy. The buyer submodularity condition causes that the VCG outcome lies in the core for any set of bidders, which is often not given for realistic value models (Bichler et al. 2009). Even if bidders knew that their valuations are buyer submodular and they would not need to speculate about other bidders’ types, it is not obvious that other bidders are able to follow the straightforward strategy in such an environment. Both computational and lab experiments have illustrated the large number of auction rounds necessary for these NLPPAs (Schneider et al. 2010), in which nearly all valuations have to be elicited to achieve efficiency.

As an alternative, linear-price CAs have been suggested resembling the fictitious Walrasian tâtonnement. Linear prices are desirable for their simplicity and the reduced communication complexity in real-world applications. Porter et al. (2003) suggest a simple mechanism with ascending linear ask prices, called the combinatorial clock (CC) auction. The mechanism has achieved high levels of efficiency in the lab (Porter et al. 2003, Kagel et al. 2010, Scheffel et al. 2011) and has a number of obvious advantages. It maintains strictly ascending, linear ask prices and limits the computational burden on the auctioneer because he only has to solve the NP-complete winner determination problem in the last rounds if there is excess supply. Also, the limited information revelation between rounds makes it quite robust against collusion and reduces the bidder’s possibilities for signaling. For these reasons, The Netherlands and the United Kingdom have recently started to use a version of the CC auction for price discovery in the sale of spectrum licenses (Cramton 2009). It is also being used in electricity markets and other high-stakes auctions, in which anonymous linear prices are often an important requirement (Cramton et al. 2006a). Unfortunately, no equilibrium strategy is known, and it is unclear for bidders which strategy they should follow.

Apart from a few lab experiments, little theoretical research has focused on the CC auction yet. Ausubel et al. (2006) argue that anonymous linear prices are not generally rich enough to yield efficient outcomes. The arguments are based on Ausubel and Milgrom (2002), who show that with linear prices bidders have an incentive to engage in demand reduction to favorably impact prices, which implies that the auction outcome is not fully efficient. Therefore, the version of the CC auction used for spectrum auctions in Europe and the clock-proxy design extend the clock auction by an additional phase, in which sealed bids can be submitted (Cramton 2009, Ausubel et al. 2006) and a payment rule is defined with the intention of providing incentives for truthful bidding. So far, no formal equilibrium analysis for such two-phased auctions has been available, and the theoretical efficiency results only consider the auction format in the second phase, where the bids are typically restricted by an activity rule and the bids submitted in the clock phase.

## 1.2. Contributions

Ausubel et al. (2006, p. 117) write that “in environments with complementary goods, a clock auction with a separate price quoted for each individual item cannot by itself generally avoid inefficiency.” It is has been shown that anonymous linear competitive equilibrium prices are not rich enough to yield efficient outcomes with general bidder valuations (Kelso and Crawford 1982). For the CC auction we make an interesting observation: The ask prices in the CC auction are not necessarily what the winners have to pay because the winner determination can select bids from previous rounds. In other words, ask prices in the CC auction are not competitive equilibrium prices. This is a way around the negative results on CAs with linear competitive equilibirum prices, which might allow for full efficiency. In this paper, we show under which circumstances the CC auction can achieve full efficiency and even allow for an ex post equilibrium strategy. Although this new auction format (called CC+ auction) needs to elicit all valuations through a restrictive price update rule, relaxations of this rule can easily be implemented in practical applications. The incentives for speculation even under this relaxed version are low.

In the CC+ auction, described in this paper, bidders have an ex post equilibrium strategy to bid on all packages with a positive valuation in each round. Even though this is a strong solution concept with strong incentives to follow this strategy, we cannot assume that bidders are able to submit enough bids or follow enough auction rounds in all but small combinatorial auctions with only a few items. Also game-theoretical models of other ICA formats such as the ascending proxy auction, iBundle(3), or dVSV are based on strong assumptions in order to achieve a proofable ex post equilibrium outcome (Schneider et al. 2010). It is interesting to undestand how relaxations of these assumptions impact efficiency.

Therefore, we also describe the results of computational experiments with different value models from the Combinatorial Auctions Test Suite (CATS Leyton-Brown et al. 2000) and analyze the impact of bidding strategies, which we observed in the lab. For example, we look at bidders who are limited in the number of bids they can provide in each round or who randomly select some packages from those with the highest payoff. We show that all auction formats achieve high levels of efficiency beyond 90% in smaller value models. It is interesting to focus on the comparison of the CC and the CC+ auction and those strategies in which bidders are restricted in the number of bids (up to 10) they can submit in each round. For smaller value models with bidders interested in up to 129 packages, the CC+ auction yields a significantly higher efficiency than the CC auction, beyond 98%. In larger value models with bidders interested in 443 or 32,767 packages, this advantage vanishes and there is no longer a significant difference between the efficiency of the CC and the CC+ auction. Still, the average efficiency in this Real Estate 5 × 3 model is beyond 92% with restricted bidders. This explains the high efficiency results observed in lab experiments (Porter et al. 2003, Scheffel et al. 2011, Kagel et al. 2010).

The simulations also highlight some virtues of the CC and the CC+ auction compared to nonlinear and personalized price auctions such as iBundle. The number of auction rounds of the CC and the CC+ auction are similar but much lower than those of the iBundle auction. The number of bids submitted in iBundle is orders of magnitude higher than in the CC+ auction, although the efficiency is not worse. This might well make a difference in practical applications.

Lab experiments add a different perspective on auctions and insights into how bidders behave in CAs, but they are costly and limited to a small number of experiments. In our experiments, we have selected a real-world scenario, the sale of spectrum licenses in the 2.6 GHz band in Europe. It shows that the rules of the CC+ auction can actually make a difference in a realistic value model. We observed bidders reduce their demand early in the CC auctions, leading to significantly lower efficiency than in the CC+ auctions, whereas bidders almost followed their equilibrium strategy in the CC+ auction.

## 1.3. Composition of this Paper

In §2 we summarize related literature on linear competitive equilibrium prices. In §3 we present analytical results on the worst-case efficiency of the CC auction assuming straightforward bidding. As an alternative, we evaluate a powerset strategy in which bidders bid on all possible packages with positive payoff in each round. We show, however, that even if bidders reveal as much information in each round, the efficiency of the CC auction can also decrease to 0%. This analysis helps us understand situations in which the CC auction is inefficient.

Based on these results, in §4 we identify properties of an auction mechanism that satisfy efficiency with a strong game-theoretical solution concept. We suggest a variation of the CC auction, the CC+ auction, which leads to full efficiency with powerset bidding. First, we modify the price update rule to allow for full efficiency. Second, we introduce a VCG payment rule to ensure incentives for truthful bidding. Then, we show that powerset bidding becomes an ex post equilibrium strategy for general valuations in the CC+ auction. Full efficiency with linear prices is not obvious, given the negative results in the literature (Gul and Stacchetti 1999). It is, however, possible because of the distinction between final ask prices and payments in the CC auction.

Some assumptions of the CC+ auction are strong and might not be given in the field. In particular, a powerset equilibrium bidding strategy is only viable for smaller instances with a few items. Therefore, in §5 we provide results of computational experiments of iBundle, the clock-proxy, the CC, and the CC+ auction and restrict bidders in the number of package bids they can submit in each round. In §6 we analyze human bidder behavior and its impact on efficiency in the CC and CC+ auctions in a series of lab experiments.

## 2. Related Theory and Definitions

Achieving efficiency in markets when economic agents strategically pursue their individual selfinterest is a fundamental problem in economics. General equilibrium models showed that in a market with multiple products, the Walrasian price mechanism with item-level prices leads to efficient allocations (Arrow and Debreu 1954) while communicating as little information as possible (see Mount and Reiter 1974 and Hurwicz 1977). Furthermore, Jordan (1982) shows that the Walrasian mechanism is a unique voluntary mechanism with this property. However, all these results assume that all production sets and preferences are convex and do not apply to nonconvex economies with indivisible goods, such as combinatorial auctions. Also, it is essentially a proof of existence providing little guidance for practical auction design. As already discussed, such neoclassical general equilibrium models have often been criticized for their strong assumptions (Georgescu-Roegen 1979).

Bikhchandani and Mamer (1997) show that without convexity assumptions full efficiency cannot be achieved with linear competitive equilibrium (CE) prices for general valuations (see Nisan and Segal 2006 for an overview). Bikhchandani and Ostroy (2002) prove that only with personalized nonlinear prices does a CA always achieve a CE.

In most practical applications of ICAs, linear and anonymous ask prices are essential. For example, day-ahead markets for electricity sacrifice efficiency for the sake of having linear prices (Meeus et al. 2009). Also, the main auction formats that have been used or discussed for selling spectrum in the United States use linear prices (Brunner et al. 2010). The CC auction is probably the most widespread ICA format, but the negative results by Gul and Stacchetti (1999) seem to indicate that there is no hope of making the CC auction fully efficient for general valuations.

A notable difference between the CC auction and the efficient ICAs (ascending proxy auction, iBundle, dVSV) is that bidders need not pay the ask prices of the final round. The winner determination in the final round can select a bid and the corresponding ask price from a previous round, so there is a distinction between final ask prices and payments. This distinction opens up the possibility of achieving efficiency with linear ask prices and a strong game-theoretical solution concept for general valuations in the CC auction. The latter is important because any restriction on the valuations is typically unknown.

<sup>Definition</sup> <sup>1.</sup> Final ask prices are the ask prices of the last round of an iterative auction.

<sup>Definition</sup> <sup>2.</sup> A payment is the amount of money a bidder has to pay for his winning items.

Let us first introduce the necessary notation and review relevant theory on linear-price CAs. There is a set K of m indivisible items indexed with k that are auctioned among n bidders. Let $i , j \in \mathcal { I }$ denote the bidders and $v _ { i } \colon S \to  { \mathbb { R } }$ denote a value function of bidder i that assigns a real value to every subset $S \subseteq { \mathcal { K } }$ of items. An allocation $X \in \Gamma$ of the m items among bidders is $X = \{ X _ { 1 } , \ldots , X _ { n } \}$ , with $X _ { i } \cap X _ { j } = 0$ for every $i \neq j . ~ X _ { i }$ is the package of items assigned to bidder $\mathsf { \overline { { \Omega } } } _ { i }$ The social welfare of an allocation X is $\textstyle \sum _ { i \in { \mathcal { I } } } v _ { i } ( X _ { i } )$ and an efficient allocation $X ^ { \ast }$ maximizes social welfare among all allocations X, such that $\begin{array} { r } { \forall X , \sum _ { i \in \mathcal { I } } v _ { i } ( X _ { i } ^ { * } ) \geq } \end{array}$ $\textstyle \sum _ { i \in { \mathcal { I } } } v _ { i } ( X _ { i } )$ 5.

We focus on linear-price CAs, in which an ask price $\beta _ { k }$ for each of the m items is available; the price of a package S is the sum of the prices of the items in this package. We assume that the demand of each bidder are the packages that maximize his utility.

Definition 3 (Blumrosen and Nisan 2007). <sub>For</sub> a given bidder valuation $v _ { i }$ and given item prices $\beta _ { 1 } , \ldots , \beta _ { m } ,$ a package $R \subseteq { \mathcal { K } }$ is called a demand of bidder i if for every other package $S \subseteq \mathcal { K }$ we have that $\begin{array} { r } { v _ { i } ( S ) - \sum _ { k \in S } \beta _ { k } \dot { \le } v _ { i } ( R ) - \dot { \sum } _ { k \in R } \bar { \beta } _ { k } } \end{array}$

A feasible allocation X and a price vector $\beta _ { k }$ are in CE when the allocation maximizes the payoff of every bidder and the auctioneer given the prices. A Walrasian equilibrium can then be described as a vector of item prices.

<sup>Definition</sup> <sup>4.</sup> A Walrasian equilibrium is a set of nonnegative prices $\beta _ { 1 } , \ldots , \beta _ { m }$ and an allocation $X$ if for every player $i , X _ { i }$ is the demand of bidder i at those prices and for any item k that is not allocated $\beta _ { k } = 0 .$

Simple examples illustrate that Walrasian equilibria do not exist for general valuations in CAs if goods are indivisible; in other words, for certain types of bidder valuations it is impossible to find linear CE prices that support the efficient allocation $X ^ { \ast }$ (Blumrosen and Nisan 2007). The economic goods are substitutes property is a sufficient condition for the existence of Walrasian equilibrium prices (Kelso and Crawford 1982). Later, Gul and Stacchetti (1999) proved that for all bidders it is almost necessary that goods are substitutes to ensure efficiency with linear CE prices. Intuitively, this property implies that every bidder continues to demand the items that do not change in price, even if the prices on other items increase. Overall, the goods are substitutes condition is very restrictive because most known practical applications of CAs deal more with complementary goods.

Actually, Gul and Stacchetti (2000) show that even if bidders’ valuation functions satisfy the goods are substitutes condition, no ascending CA exists that uses anonymous linear prices and arrives at the VCG solution. This means that bidders may have an incentive to demand smaller packages of items in order to lower their payments.

## 3. The CC Auction

We concentrate on the CC auction as introduced by Porter et al. (2003) and give a precise description in Algorithm 1. Prices for all items are initially zero. In every round bidders identify a package of items, or several packages, that they offer to buy at current prices. If two or more bidders demand an item, then its price is increased by a fixed bid increment in the next round. This process iterates. The bids that correspond to the current ask prices are called stand-$i n g ,$ , and a bidder is standing if he has at least one standing bid. In a simple scenario in which supply equals demand, the auction terminates and the items are allocated according to the standing bids. If at some point there is excess supply for at least one item and no item is overdemanded, the auctioneer determines the winners to find an allocation of items that maximizes his revenue by considering all submitted bids. If the solution displaces a standing bidder, the prices of items in the corresponding standing bids rise by the bid increment and the auction continues. The auction ends when no prices are increased and bidders finally pay their bid prices for winning packages. We analyze a version that uses an XOR bidding language.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1 (CC Auction)
Data: package bids $\beta_{i}(S)$
Result: allocation $\bar{X}$ and prices $\beta_{i}(\bar{X}_{i})$
initialization
    for $k = 1$ to $m$ do $\beta_{k} \leftarrow 0$
    for $i = 1$ to $n$ do $X_{i} \leftarrow \emptyset$
repeat
    overdemand $\leftarrow$ FALSE; oversupply $\leftarrow$ FALSE
    for $i = 1$ to $n$ do
    bidders submit bids $\beta_{i}(S)$
    for $k = 1$ to $m$ do
    if $\geq 2$ bidders $i \neq j$ demand item $k$ $\beta_{k} \leftarrow \beta_{k} + \epsilon$
    overdemand $\leftarrow$ TRUE
    end
    if item $k$ is not part of a bid $\beta_{i}(S)$ then
    oversupply $\leftarrow$ TRUE
    if overdemand = TRUE then exit iteration
    else if oversupply = FALSE then exit loop
    else
    for $k = 1$ to $m$ do
    Assign $\beta_{i}(S)$ with $k \in S$ to the set of
    standing bids $\mathcal{B}$
    Calculate $\bar{X}$ based on all bids submitted
    in the auction
    if a bidder holding a bid in $\mathcal{B}$ is displaced,
    i.e., no bid by this bidder is in $\bar{X}$, then
    foreach item $k$ which was displaced: do
    $\beta_{k} \leftarrow \beta_{k} + \epsilon$
    end
    else $\bar{X}$ is the final allocation
    end
until stop
</div>

## 3.1. Efficiency of the CC Auction

We analyze the worst-case efficiency of the CC auction with bidders following the straightforward strategy, which is typically assumed in game-theoretical models of ICAs. We also evaluate a powerset strategy, which describes the situation in which bidders reveal all packages with a positive valuation at the current prices. We draw on this strategy in subsequent sections.

<sup>Definition</sup> <sup>5.</sup> A straightforward bidder bids only for his demand in each round at the current ask prices $\beta _ { 1 } , \ldots , \beta _ { m }$

Note that a straightforward bidder might bid on several packages in a round if they apply to the definition of demand (see Definition 3).

<sup>Definition</sup> <sup>6.</sup> The powerset bidder bids on all packages $S$ with a nonnegative value $\begin{array} { r } { v _ { i } ( S ) - \sum _ { k \in S } \beta _ { k } \overset { - } { = } 0 } \end{array}$ at the current set of ask prices $\beta _ { 1 } , \ldots , \beta _ { m }$

We show that if all bidders follow the straightforward strategy, the efficiency of the CC auction can be as low as 0%. For this, we refer to a recent theorem by Kagel et al. (2010) on the efficiency of auctions that maximize the auctioneer’s revenue based on bid prices.

A standard package auction is defined such that it selects an allocation X<sup>¯</sup> to maximize the auctioneer’s revenue $\bar { X } \in$ arg max $_ X \sum _ { i \in { \mathcal { I } } } \beta _ { i } ( X _ { i } )$ and has bidder i pay $\beta _ { i } ( { \bar { X } } _ { i } ) . \beta _ { i } ( X _ { i } )$ denotes the highest price that i bids for a package $X _ { i }$ during the course of the auction.

A standard package auction can be modeled as a cooperative game with transferable utility, in which the payoff vector or imputation $\pi$ is given by the auctioneer’s revenue $\begin{array} { r } { \pi _ { 0 } \stackrel { - } { = } \sum _ { i \in \mathcal { I } } \beta _ { i } ( X _ { i } ) } \end{array}$ , and bidder $i \prime \mathrm { s }$ payoff $\pi _ { i } = v _ { i } ( X _ { i } ) - \beta _ { i } ( X _ { i } )$ . The value of a coalition including the auctioneer and the bidders in $T \subseteq { \mathcal { F } }$ is $\begin{array} { r } { w ( T ) = \breve { \sum } _ { i \in T } v _ { i } ( X _ { i } ^ { * } \mid _ { T } ) } \end{array}$

A feasible allocation X with prices $\beta$ and a corresponding imputation  is a core allocation if for every set of bidders $T \subseteq { \mathcal { I } } ,$ the imputation satisfies $\pi _ { 0 } +$ $\begin{array} { r } { \sum _ { i \in T } \pi _ { i } \geq w ( T ) } \end{array}$ . A set of bidders T is relevant if there is some imputation such that $\textstyle { \boldsymbol { \pi } } _ { 0 } + \sum _ { i \in T } { \boldsymbol { \pi } } _ { i } = w ( T )$ The package $X _ { i }$ is the respective efficiency-relevant package.

Theorem 1 (Kagel et al. 2010). <sub>In</sub> <sub>a</sub> <sub>standard</sub> <sub>pack-</sub> age auction, let $\beta$ denote the final bids and X<sup>¯</sup> the final allocation in the auction. If for all bidders $i , \ v _ { i } ( \dot { X } _ { i } ) -$ $\beta _ { i } ( X _ { i } ) \leq v _ { i } ( \bar { X } _ { i } ) - \beta _ { i } ( \bar { X } _ { i } )$ , then the allocation $\bar { X }$ is efficient: $\begin{array} { r } { \sum _ { i \in \mathcal { I } } v _ { i } ( \bar { X } _ { i } ) = w ( \mathcal { I } ) } \end{array}$ . If the efficient allocation is unique, then the condition $\dot { v _ { i } } ( \dot { X _ { i } } ) - \beta _ { i } \ddot { ( X _ { i } ) } \leq v _ { i } ( \bar { X } _ { i } ) - \beta _ { i } ( \bar { X } _ { i } )$ is necessary as well as sufficient for X<sup>¯</sup> to be efficient.

To promote these results, the auction mechanism must encourage bidders to bid aggressively all the way up to their full values $( \beta _ { i } ( X _ { i } ) = v _ { i } \mathbf { \bar { ( } } X _ { i } ) )$ for efficiency-relevant packages, i.e., packages that may become winning packages.

## 3.2. Worst-Case Efficiency of the CC Auction with Straightforward Bidders

If a bidder follows the straightforward strategy in the CC auction, he does not bid on all relevant packages in the course of the auction. The example in Table 1 illustrates a characteristic situation that we refer to as demand masking set. The upper part of the table describes valuations of $2 m - \bar { 1 }$ bidders for m items, and the lower part shows both ask prices for items and corresponding package bids in individual rounds t. The indices of the bid prices for different packages indicate which straightforward bidder submits the bid on the respective package. There is one bidder called bidder 1 and for each $h \in \{ 2 , \ldots , m \}$ there are two bidders $h _ { a }$ and $h _ { b } .$ Bidder 1 values item 415 at a value of 10 and does not value any other item. For $h = 2 , \ldots , m _ { \astrosun }$ , bidders $h _ { a }$ and $h _ { b }$ value the package 411 h5 at 10 and bidders $h _ { a }$ value the item $( \hat { h } ) $ at 4 and are not interested in any other package. Without loss of generality, we assume a bid increment of 1. Straightforward bidders $h _ { a }$ and $h _ { b }$ demand the package 411 h5 until round $^ { 6 , }$ at which point they demand nothing. After round 6 there is excess supply and the auctioneer solves the winner determination problem, which displaces the sole remaining standing bidder, who bids on item 415. Thus the price on item 415 further increases until bidder 1 wins item 415 in round 10, and the auction terminates with a social surplus of 10. However, the efficient allocation assigns item 415 to bidder 1 and item 4h5 to bidder $h _ { a }$ for a social welfare of $1 0 + 4 ( m - 1 )$ . The expression $1 0 / ( 1 0 + 4 ( m - 1 ) )$ converges to zero as m approaches infinity.

Table 1 Example of a Demand Masking Set of Bidder Valuations and CC Auction Process Assuming Straightforward Bidders

<table><tr><td></td><td> $\beta_{(1)}$ </td><td> $\beta_{(2)}$ </td><td> $\beta_{(3)}$ </td><td> $\cdots$ </td><td>(1)</td><td>(2)</td><td>(3)</td><td> $\cdots$ </td><td>(1,2)</td><td>(1,3)</td><td> $\cdots$ </td></tr><tr><td> $V_1$ </td><td></td><td></td><td></td><td></td><td>10*</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $V_{2_a}$ </td><td></td><td></td><td></td><td></td><td></td><td>4*</td><td></td><td></td><td>10</td><td></td><td></td></tr><tr><td> $V_{2_b}$ </td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>10</td><td></td><td></td></tr><tr><td> $V_{3_a}$ </td><td></td><td></td><td></td><td></td><td></td><td></td><td>4*</td><td></td><td></td><td>10</td><td></td></tr><tr><td> $V_{3_b}$ </td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>10</td><td></td></tr><tr><td> $\cdots$ </td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td> $\cdots$ </td><td></td><td></td><td> $\cdots$ </td></tr><tr><td>t=1</td><td>1</td><td>1</td><td>1</td><td> $\cdots$ </td><td>1 $_1$ </td><td></td><td></td><td></td><td>2 $_{2a,2b}$ </td><td>2 $_{3a,3b}$ </td><td> $\cdots$ </td></tr><tr><td>t=2</td><td>2</td><td>2</td><td>2</td><td> $\cdots$ </td><td>2 $_1$ </td><td></td><td></td><td></td><td>4 $_{2a,2b}$ </td><td>4 $_{3a,3b}$ </td><td> $\cdots$ </td></tr><tr><td>t=3</td><td>3</td><td>3</td><td>3</td><td> $\cdots$ </td><td>3 $_1$ </td><td></td><td></td><td></td><td>6 $_{2a,2b}$ </td><td>6 $_{3a,3b}$ </td><td> $\cdots$ </td></tr><tr><td>t=4</td><td>4</td><td>4</td><td>4</td><td> $\cdots$ </td><td>4 $_1$ </td><td></td><td></td><td></td><td>8 $_{2a,2b}$ </td><td>8 $_{3a,3b}$ </td><td> $\cdots$ </td></tr><tr><td>t=5</td><td>5</td><td>5</td><td>5</td><td> $\cdots$ </td><td>5 $_1$ </td><td></td><td></td><td></td><td>10 $_{2a,2b}$ </td><td>10 $_{3a,3b}$ </td><td> $\cdots$ </td></tr><tr><td>t=6</td><td>6</td><td>6</td><td>6</td><td> $\cdots$ </td><td>6 $_1$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>t=7</td><td>7</td><td>6</td><td>6</td><td> $\cdots$ </td><td>7 $_1$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $\cdots$ </td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>t=10</td><td>10</td><td>6</td><td>6</td><td> $\cdots$ </td><td>10 $_1$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

We provide a formal definition of a demand masking set and derive a worst-case bound for these situations as a function of m.

<sup>Definition</sup> <sup>7.</sup> A demand masking set of bidder valuations is given if the following properties are fulfilled. There is a set of bidders I with $\left| { \mathcal { I } } \right| \geq 3 ,$ a set of items $\mathcal { K } = \{ 1 , \dots , m \}$ with $R \subseteq { \mathcal { K } } ,$ , and a partition H of ${ \mathcal { K } } \backslash R .$ . Let $S _ { h }$ be the elements of H with $h \in \{ 2 , \dots , | \mathcal { H } | + 1 = g \}$ . For each $S _ { h }$ there are two bidders $h _ { a }$ and $h _ { b } .$ . Bidder 1 values package R with $\xi .$ For $h \in \{ 2 , \ldots , g \}$ bidders $h _ { a }$ value the packages $S _ { h }$ with $\nu _ { h }$ and $R \dot { \cup } S _ { h }$ with $\mu$ and bidders $h _ { b }$ value only package $R \dot { \cup } S _ { h }$ with $\mu .$ . No bidders are interested in the other packages; i.e., the marginal value of winning any additional item to the positively valued packages is zero.

Note that the valuations of zero as shown in Table 2 do not need to be strictly zero, but rather sufficiently small so as not to influence the economy.

Table 2 Demand Masking Set of Bidder Valuations

<table><tr><td></td><td> $R$ </td><td> $\{S_h\}$ </td><td> $\{R \dot{\cup} S_h\}$ </td></tr><tr><td> $v_1$ </td><td> $\xi$ </td><td>0</td><td> $\xi$ </td></tr><tr><td> $\{v_{h_a}\}$ </td><td>0</td><td> $v_h$ </td><td> $\mu$ </td></tr><tr><td> $\{v_{h_b}\}$ </td><td>0</td><td>0</td><td> $\mu$ </td></tr></table>

<sup>Proposition</sup> <sup>1.</sup> If bidder valuations are demand masking and all bidders follow the straightforward strategy in the CC auction, then the efficiency converges to $2 / ( m + 1 )$ in the worst case.

The proof is provided in Appendix A.

In the example of Table $1 , \nu _ { h }$ is smaller than 5 for all h. With $m = 3$ and $\nu _ { h } = \nu = 5 - \rho$ for all h, efficiency is approximately $5 0 \% = 1 0 / ( 1 0 + \nu ( m - 1 ) )$ , which is equal to $2 / ( m { \stackrel { \cdot } { + } } 1 )$ in the worst case. Obviously if the number of items m and the corresponding number of bidders increase to fulfill the requirements of a demand masking set, efficiency converges to 0% in the worst case. Although such a situation that leads to 0% efficiency can be considered a degenerated case that does not happen that often in practice, we found regular situations in simulations with realistic value models in which the case of $m = 2$ or $m = 3$ occurred, which still leads to efficiencies of $6 7 \%$ or 50% in the worst case. Note that these are not necessarily the only characterizations of value models in which such low efficiency can occur.

## 3.3. Worst-Case Efficiency of the CC Auction with Powerset Bidders

One of the reasons for the popularity of ascending auctions is that they require only partial revelation of the private information (Blumrosen and Nisan 2007). In a CA this is less of an advantage because it is still necessary to elicit all valuations except those of the winning bids in the efficient allocation in the worst case. This means that if there are z winning package bids in an efficient allocation, $n 2 ^ { m } - z$ valuations need to be elicited by the auctioneer to guarantee full efficiency. For example, ascending auctions with nonlinear personalized prices such as iBundle, the ascending proxy auction, or dVSV are protocols that in each round elicit the demand set of each bidder and provably find an efficient solution at the expense of an exponential number (in m) of auction rounds (Blumrosen and Nisan 2007). In such an NLPPA with straightforward bidders, at least all valuations of all losing bidders are elicited.

As an alternative to straightforward bidding, the auctioneer can try to encourage bidders to bid on many packages from the start. In the best case, bidders reveal all packages with positive payoff; i.e., they follow a powerset strategy. Unfortunately, even if bidders follow the powerset strategy, the CC auction does not necessarily terminate with an efficient solution.

<sup>Proposition</sup> <sup>2.</sup> If all bidders follow the powerset strategy, the efficiency of the CC auction converges to 0% in the worst case.

The proof and an example are provided in Appendix A.

Inefficiencies in the CC auction with powerset bidders occur if there are two overlapping packages by the winning bidder and there is only competition on the package with the lower valuation. This drives up the prices only on the lower valued package, which is finally sold, although the bidder has a higher valuation for the other package, for which he cannot increase his bid.

## 3.4. Modifications of the CC Auction

The analysis in §3.3 shows that even if bidders reveal all profitable packages in each round, the CC auction can be inefficient. However, a small change in the price update rule allows all losing package valuations to be elicited and makes the CC auction fully efficient with powerset bidders.

<sup>Definition</sup> <sup>8.</sup> A partial revelation price update rule in the CC auction also increases prices for each overdemanded item and in addition for each item of a standing bid that is displaced by the winner determination.

The difference to the original price update rule is very small. Although the original CC auction terminates if all bidders holding a standing bid get any package in the final allocation (not necessarily one of their standing bids), the partial revelation price update rule requires a bidder to get exactly his standing bid allocated. Thus one bidder holding two or more standing bids causes prices to increase and the auction to continue.

<sup>Corollary</sup> <sup>1.</sup> If all bidders follow the powerset strategy, the CC auction with the partial revelation price update rule and sufficiently small bid increments terminates with an efficient outcome.

The proof is provided in Appendix A.

The auction can still suffer from small inefficiencies due to the minimal bid increment. Last-and-final bids have been suggested as a means to get rid of these inefficiencies (Parkes 2006). They allow bidders to submit a final bid on a package that is above the ask price of the previous round but below the current ask price for a package. For the sake of clarity, we omit this rule in our analysis.

## 4. The CC+ Auction

Even if the powerset strategy leads to full efficiency in a modified CC auction with linear ask prices, it is not obvious why a bidder should follow the powerset strategy. We show that the powerset strategy is an ex post equilibrium, but that it requires an even stronger price-update rule and a VCG payment rule (Ausubel and Milgrom 2006b). We refer to this auction design as a CC+ auction. A description of the CC+ auction with powerset bidders is provided in Algorithm 2. Modifications to the original CC auction are underlined.

<sup>Definition</sup> <sup>9.</sup> A full revelation price update rule in the CC+ auction increases prices on items as long as at least a single bidder bids on the item.

We aim for a strong game-theoretical solution concept. A desirable property is a profile of strategies with an ex post equilibrium, in which a bidder does not regret his bid even when he is told what everyone’s type is after the auction. Note that we are not attempting to achieve a dominant strategy equilibrium because preference elicitation in an indirect mechanism can invalidate dominant strategy equilibria existing in a single-step version of a mechanism (Conitzer and Sandholm 2002). We discuss the types of speculation that are possible in a CC+ auction with full information in Appendix B. It illustrates that ex post equilibria are not as strong as dominant strategy equilibria, but they are much stronger than Bayesian Nash equilibria because they do not require agents to speculate on other bidders’ types or valuations. When iterative preference elicitation is used to implement a mechanism that is a dominant-strategy direct-revelation mechanism in a sealed-bid version, then each agent’s best (even in hindsight) strategy is to act truthfully if the other agents act truthfully (Conen and Sandholm 2001).

<sup>Definition</sup> <sup>10.</sup> Truthful bidding in every round of an auction is an ex post equilibrium if for every bidder $i \in { \mathcal { I } } ;$ if bidders in $\dot { \mathcal { I } _ { - i } }$ follow the truthful bidding strategy, then bidder i maximizes his payoff in the auction by following the truthful bidding strategy (Mishra and Parkes 2007).

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 2 (CC+ Auction with Powerset Bidding)
Data: package bids $\beta_{i}(S)$
Result: efficient allocation $X^{*}$ and prices $\beta_{i}(X_{i}^{*})$
initialization
    for $k = 1$ to $m$ do $\beta_{k} \leftarrow 0$
    for $i = 1$ to $n$ do $X_{i} \leftarrow \emptyset$
repeat
    overdemand $\leftarrow$ FALSE; oversupply $\leftarrow$ FALSE
    for $i = 1$ to $n$ do
    submit a bid $\beta_{i}(S)$ on each package $S$, which applies to $v_{i}(S) - \sum_{k \in S} (\beta_{k}) \geq 0$
    for $k = 1$ to $m$ do
    if $\geq 1$ bidders demand item $k$ then
    $\beta_{k} \leftarrow \beta_{k} + \epsilon$
    overdemand $\leftarrow$ TRUE
    end
    if item $k$ is not part of a bid $\beta_{i}(S)$ then
    oversupply $\leftarrow$ TRUE
    end
    if overdemand = TRUE then exit iteration
    else if oversupply = FALSE then exit loop
    else
    Calculate the final allocation $X^{*}$ based on all
</div>

submitted bids exit loop until true Calculate VCG prices $\beta _ { V C G } ^ { * }$ based on all submitted bids

## 4.1. Efficiency and Incentive Compatibility of the CC+ Auction

We show that the CC+ auction maintains linear ask prices and achieves an efficient solution while being incentive compatible. Note that we do not need to make any restrictive assumptions on the bidders’ valuations. To prove the efficiency already, the slightly weaker partial revelation price update rule is sufficient (see the proof for Corollary 1).

<sup>Corollary</sup> <sup>2.</sup> A powerset strategy is an ex post equilibrium in the CC+ auction with the full revelation price update rule.

The proof is provided in Appendix A.

As all bidders reveal all valuations, a bidder cannot improve his payoff by unilaterally deviating from the truthful powerset strategy in a respective CC+ auction or influence whether the other bidders reveal their valuations truthfully. Therefore, the bidder’s truthful powerset strategy is independent of the other bidders’ types. This result shows what types of price update and payment rules are sufficient for a powerset strategy to satisfy an ex post equilibrium. Whereas the partial revelation price update rule is sufficient for efficiency, when all bidders follow a powerset strategy, a full revelation price update rule is necessary to achieve an ex post equilibrium.

However, the type of speculation that the partial revelation price update rule allows is extremely unlikely in practical situations and would only make sense under full information, which is never the case in auctions.

## 4.2. Communication Complexity of the CC+ Auction

Nisan and Segal (2006) show that determining an optimal allocation requires an exponential number of queries from the auctioneer to the bidders. There are subtle differences, however, in the amount of information that is elicited by different auction formats. A VCG auction and a $\dot { C } C +$ auction ask bidders to reveal all $n 2 ^ { m }$ valuations to the full extent. In a $\mathrm { C C + }$ auction, a bidder sees the price clock increase on various items and learns at which prices nobody demands a particular item any more. In a VCG auction, bidders only know that a bid on a particular package was lost. In both cases, the auctioneer learns all valuations of all bidders. Using the partial revelation price update rule in the CC+ auction with z winning bids, only $n 2 ^ { m } - z$ losing valuations are elicited.

In NLPPAs such as the ascending proxy auction, iBundle(3), or dVSV, the auctioneer elicits $n 2 ^ { m } - z$ preferences in the worst case. It might also be that the winners do not need to reveal all valuations on losing packages. However, a strong solution concept is only satisfied if buyer submodularity is given. Clearly, communication complexity will always remain a stumbling block for any of the theoretical models in situations with more than a few items only. The assumption of following a straightforward strategy in exponentially many auction rounds only holds in automated settings with proxy agents. The same is true for the powerset strategy, even if the number of auction rounds is much lower. We address this issue and the robustness of the efficiency results with respect to deviations from the powerset strategy in §5.

Similar to work on NLPPAs, the CC+ auction is, however, of theoretical value because it shows sufficient rules and assumptions to design an ascending CA that uses linear ask prices and achieves an efficient outcome with a strong solution concept for general valuations. This provides a theoretical foundation for combinatorial clock auctions.

## 4.3. Alternative Payment Rules in the CC+ Auction

The CC+ auction suffers from some of the problems of the VCG design, in particular that the outcome might not be in the core (Ausubel and Milgrom 2006b). In other words, there are some bidders who could make a counteroffer to the auctioneer that both sides would prefer to the VCG outcome. In such situations, the auctioneer can increase his sales revenue by excluding certain bidders, which is also referred to as revenue nonmonotonicity. The bidders could also increase their payoff through shill bidding. These vulnerabilities of VCG outcomes are considered serious problems for applications in the field. In some settings, it is sufficient to have a mechanism that is in the core but as close to incentive compatibility as possible.

Day and Raghavan (2007) have recently suggested bidder-Pareto-optimal prices in the core as an alternative to VCG prices. An outcome of an auction is bidder-Pareto-optimal in the core if no Pareto improvement is possible within the core. This means that if we lower one bidder’s payment, some other bidder’s payment must increase to remain in the core. Such an outcome minimizes the total payments within the core.

Definition 11 (Day and Raghavan 2007). <sub>An</sub> outcome is bidder-Pareto-optimal if there is no other core outcome weakly preferred by every bidder and strictly preferred by at least one bidder in the winning coalition.

Note that if items are complements, core prices exceed VCG prices strictly. Day and Milgrom (2007) show that a core-selecting auction provides minimal incentives for bidders to deviate from truthful reporting, if it chooses a bidder-Pareto-optimal outcome. Day and Raghavan (2007) also describe a constraint generation approach that generates bidder-Paretooptimal core prices rapidly for sealed-bid auctions. The payment scheme minimizes the total availability of gains from unilateral strategic manipulation. The final bids of each bidder on all packages in a CC+ auction can also be used to calculate bidder-Paretooptimal core prices.

<sup>Corollary</sup> <sup>3.</sup> The CC+ auction with powerset bidders terminates with a core outcome if it charges bidder-Paretooptimal prices as payments instead of VCG prices.

The proof is provided in Appendix A.

Note that even with the weaker partial revelation price update rule, Corollary 3 holds. In contrast to the clock-proxy auction (Ausubel et al. 2006), bidders in the CC+ auction do not need to type in valuations to a proxy agent after the CC auction has finished, and the bidder-Pareto-optimal prices are calculated right away.

## 5. Computational Experiments

Computational experiments provide additional insight and complement the game-theoretical analysis of the first sections. They can show the robustness of a design against deviations from equilibrium strategies. In the previous section, we show that the powerset strategy leads to efficiency in the CC+ auction. Powerset bidding is typically not viable for bidders except for small CAs. So far, only a few papers provide results on individual bidding behavior in CAs. Scheffel et al. (2011) report that lab subjects submit around 10 to 12 bids per round in linear-price auctions independent of the number of packages with a positive valuation. Kagel et al. (2010) report that bidders bid only on a fraction of the profitable packages in the CC auction. Global bidders bid between 12% and 14% of the profitable packages in one treatment with six items and 21%–28% in a treatment with four items.

This section describes the results of computational experiments and analyzes efficiency, revenue, number of auction rounds, and the number of submitted bids with artificial bidders in the CC and variations of the CC+ auction with respect to deviations from the powerset strategy. The bidding agents follow either the straightforward or the powerset strategy, plus we also implement agents with restrictions on the number of packages submitted in each round.

## 5.1. Experimental Setup

The experimental setup is based on three treatment variables, namely the auction formats, the value model, and the bidding strategy.

5.1.1. Auction Formats. Apart from the CC and the CC+ auction, we analyze iBundle and clock-proxy auction formats in our experiments. Our implementation of iBundle follows the description in Parkes and Ungar (2000). iBundle is fully efficient given that bidders follow a straightforward bidding strategy. The clock-proxy auction has been described in Ausubel et al. (2006). It consists of a CC auction in the first phase with an XOR bidding language and a second stage sealed-bid phase. The second phase is then implemented following the rules of iBundle or the ascending proxy auction (Ausubel and Milgrom 2006a), with automated proxy bidders who follow a straightforward bidding strategy.

In our implementation, the clock phase of the clockproxy auction terminates as soon as there is no overdemand in an auction round any more. In contrast, the standalone CC auction will not terminate after a round with excess supply. If the winner determination displaces a bidder who was active in the last round, the auction continues. The winner determination after the clock phase of the clock-proxy auction is necessary to determine the minimum bid prices for proxy bids. These prices are set to the prices of the winning bids of the clock phase. All bids submitted in the clock phase are automatically submitted to the proxy phase independent of the prices. Note that we assume bidders in the proxy phase actually submit bids on all possible packages with a positive payoff given the clock prices. This is a very favorable assumption because we assume that bidders are restricted in the clock phase in some treatments. However, this provides a reasonable upper bound on the efficiency of the clock-proxy auction. Of course, restrictions on the number of package bids submitted will also hold in the proxy phase in any but small value models.

5.1.2. Value Models. Because there are hardly any real-world CA data sets available, we base our experiments on synthetic valuations generated with CATS (Leyton-Brown et al. 2000).

The Transportation value model uses the Paths in Space model from CATS. It models a nearly planar transportation graph in Cartesian coordinates, in which each bidder is interested in securing a path between two randomly selected vertices (cities). The items traded are edges (routes) of the graph. Parameters for the Transportation value model are the number of items (edges) m and graph density $\eta ,$ which defines an average number of edges per city and is used to calculate the number of vertices as $( 2 m ) / \eta$ The bidder’s valuation for a path is defined by the Euclidean distance between two nodes multiplied by a random number drawn from a uniform distribution. Consequently only a limited number of packages, which represent paths between both selected cities, are valuable for the bidder. This allows the consideration of even larger transportation networks in a reasonable time. In this work we use a value model with 25 items and 15 bidders. Every bidder has interest in 16 different packages on average.

The Real Estate $3 \times 3$ value model is based on the Proximity in Space model from the CATS. Items sold in the auction are the real estate lots k, which have valuations $v ( k )$ drawn from the same normal distribution for each bidder. Adjacency relationships between two pieces of land $p$ and q $( e _ { p q } )$ are created randomly for all bidders. Edge weights $r _ { p q } \in [ 0 , 1 ]$ are then generated for each bidder, and they are used to determine package valuations of adjacent pieces of land:

$$
v (S) = \left(1 + \sum_ {e _ {p q}: p, q \in S} r _ {p q}\right) \sum_ {k \in S} v (k).
$$

In this work we use the Real Estate $3 \times 3$ value model with nine lots for sale. Individual item valuations have a normal distribution with a mean of 10 and a variance of 2. There is a 90% probability of a vertical or horizontal edge and an 80% probability of a diagonal edge. Edge weights have a mean of 0.5 and a variance of 0.3. All experiments with the Real Estate $3 \times 3$ value model are conducted with five bidders, who are interested in a maximum package size of three because large packages are always valued more highly than small ones. This is also motivated by realworld observations by An et al. (2005) in which bidders typically have an upper limit on the number of items they are interested in. Without this limitation, the auction easily degenerates into a scenario with a single winner for the package containing all items.

In order to analyze a value model with many items, a very large number of possible packages for each bidder, and the impact of the threshold problem, we also use a Real Estate $3 \times 5$ value model. This model contains two different bidder types: one big bidder interested in all 15 items and five smaller bidders. Each small bidder is interested in a randomly determined preferred item, all horizontally and vertically adjacent items, and the items adjacent to those. This means that a small bidder is typically interested in 6 to 11 items with local proximity to its preferred item. For each bidder we draw the baseline item valuation $v _ { i } ( k )$ from a uniform distribution separately. Complementarities occur upon vertical and horizontal adjacent items based on a logistic function to determine package valuations: $\begin{array} { r } { v _ { i } ( \tilde { S ) } = \sum _ { C \in P } ( ( 1 + a / ( 1 0 0 ( 1 + e ^ { b - | \hat { C } | } ) ) ) } \end{array}$ ∗ $\bar { \sum _ { k \in C } { v _ { i } ( k ) } } )$ , with P being the partition of S containing maximal connected packages C. For our simulations we choose $a = 3 4 0$ and $b = 8$ for the big bidder and $a = 1 6 0$ and b = 4 for all small bidders and draw the baseline valuations for the big bidder on the range 631 97 and for the small bidders on the range 631 207.

The size of a value model describes the number of possible bids that a bidder can evaluate. Whereas in the Transportation value model, bidders are interested in only 16 packages on average and in the Real Estate $3 \times 3$ value model in 129, small bidders in the Real Estate $3 \times 5$ value model are interested in 443 packages on average and the big bidder is interested in $2 ^ { 1 5 } - 1 = 3 2 , 7 6 7$ packages. We find that the size of the value model has an impact on the average efficiency achieved if bidders do not reveal all their valuations throughout the auction, as is the case with a straightforward strategy in iBundle or a powerset strategy in the CC+ auction.

Because we find similar results in other models, we concentrate only on the ones described above for clarity and move the others to Appendix E.

5.1.3. Bidding Agents. In our theoretical analysis, we introduce the straightforward and the powerset strategies. The powerset bidder evaluates all possible packages in each round and submits bids for all packages that are profitable given current prices. In addition to the powerset bidder, we analyze bidders that are restricted to bid only on the best 6 or the best 10 packages in each round, similar to bidders in the lab. These bidders choose those packages with the highest payoff. Inspired by observations in the lab, we also model a Heuristic 5 of 20 bidder. This bidder randomly selects 5 out of his 20 best packages based on his payoff in a round. This bidder allows the evaluation of the robustness of the auction against randomness in the bidding strategies.

In contrast, the straightforward bidder only bids on his demand in each round, i.e., on those package(s) that maximize his payoff given current prices.

5.1.4. Treatment Structure. We use a $7 \times 7 \times 5$ factorial design (see Table 3) in which all value models are analyzed in different auction formats with all of the above bidding strategies. Each treatment is repeated 50 times with different random seeds for value models and bidding strategies, resulting in 11,750 auctions. The auctions use a minimum increment of 1 and the XOR bidding language.

Table 3 Treatment Factors

<table><tr><td>Value model</td><td>Auction format</td><td>Bidding strategy</td></tr><tr><td>Transportation</td><td>CC</td><td>Straightforward</td></tr><tr><td>Real estate  $3 \times 3$ </td><td>CC+ (partial, core)</td><td>Heuristic 5 of 20</td></tr><tr><td>Real estate  $5 \times 3$ </td><td>CC+ (full, core)</td><td>Powerset6</td></tr><tr><td>Transportation large (Appendix E) ×</td><td>CC+ (partial, VCG) ×</td><td>Powerset10</td></tr><tr><td>Pairwise synergy low (Appendix E)</td><td>CC+ (full, VCG)</td><td>Powerset</td></tr><tr><td>Pairwise synergy high (Appendix E)</td><td>iBundle</td><td></td></tr><tr><td>Airports (Appendix E)</td><td>Clock-proxy</td><td></td></tr></table>

## 5.2. Experimental Results

We present the aggregate results of our computational experiments with the three different value models.<sup>3</sup> We evaluate straightforward and powerset bidders but also bidders following heuristic bidding strategies in order to provide an indication of the impact on efficiency of heuristic bidding strategies as they can be found with human bidders in the lab or in the field.

The results are presented in Tables 4 to 6 and in Appendix E. We measure mean and minimum efficiency and mean revenue to characterize the auction outcome. Furthermore, we compare number of rounds and total number of bids submitted by the bidders. iBundle leads to a very large number of auction rounds in all but small value models. For the Real Estate $5 \times 3$ value model the computation time was such that only a single auction took more than 60 hours and 500 rounds as the winner determination takes increasing amounts of time. We decided not to report iBundle results on this value model because such auctions would not be conducted with human bidders in the field. For similar reasons we also do not report on the results of the clock-proxy auction in the Real Estate 5 × 3 value model, in which essentially the proxy phase is equivalent to iBundle with powerset bidders.

Result 1 (Mean Efficiency Across Auction For-<sup>mats</sup> <sup>and</sup> <sup>Bidder</sup> <sup>Types).</sup> The mean efficiency for the CC and the CC+ auction is higher than 96.9% for all restricted bidder types (Heuristic 5 of 20, Powerset6, and Powerset10) and all tested value models, except the Real Estate $5 \times 3$ value model, where the bidders were interested in a very large number of packages. In the Real Estate $5 \times 3$ model, the CC and the CC+ auction yielded an average efficiency of 91.9% to 94% for restricted bidder types, which is because a smaller proportion of the valuations are elicited in larger value models if bidders are restricted to fewer than 10 bids per round. If all bidders follow a powerset strategy, the CC+ auction is almost fully efficient. Small inefficiencies of less than 0.3% in some cases are due to the minimum bid increment. With an  bid increment and m items, the outcome of a CC+ auction without last-and-final bids can be 4m − 15 away from full efficiency. An unrestricted powerset strategy in the CC auction leads to 96.8% efficiency on average for all value models that we analyzed, illustrating the robustness of this simple auction format.

iBundle achieves full efficiency with straightforward bidders as predicted by the theory. With Heuristic 5 of 20, Powerset6, and Powerset10 bidders, the average efficiency results are in most instances significantly worse, but in the Real Estate $3 \times 3$ value model also better than the CC+ auction for Powerset6 and Powerset10 bidders.

Table 4 Transportation with 25 Items and 15 Bidders (VCG Bidder Gain 37.25%)

<table><tr><td rowspan="2">Measure</td><td colspan="5">Bidder type</td></tr><tr><td>Straightforward</td><td>5 of 20</td><td>Powerset6</td><td>Powerset10</td><td>Powerset</td></tr><tr><td>Mean efficiency in %</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CC</td><td>99.48</td><td>97.02</td><td>97.38</td><td>96.96</td><td>96.83</td></tr><tr><td>CC+ (partial)</td><td>99.52</td><td>99.87</td><td>99.86</td><td>99.85</td><td>99.92</td></tr><tr><td>CC+ (full)</td><td>99.62</td><td>99.88</td><td>99.84</td><td>99.87</td><td>99.93</td></tr><tr><td>iBundle</td><td>100.00</td><td>93.74</td><td>97.54</td><td>97.89</td><td>97.22</td></tr><tr><td>Clock-proxy</td><td>99.96</td><td>99.93</td><td>99.95</td><td>99.95</td><td>99.96</td></tr><tr><td>Min. efficiency in %</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CC</td><td>94.81</td><td>84.65</td><td>86.71</td><td>83.22</td><td>83.15</td></tr><tr><td>CC+ (partial)</td><td>94.81</td><td>96.69</td><td>96.69</td><td>96.69</td><td>98.60</td></tr><tr><td>CC+ (full)</td><td>94.81</td><td>96.69</td><td>96.69</td><td>96.69</td><td>98.60</td></tr><tr><td>iBundle</td><td>100.00</td><td>74.72</td><td>85.71</td><td>89.44</td><td>74.56</td></tr><tr><td>Clock-proxy</td><td>97.90</td><td>98.60</td><td>98.60</td><td>98.60</td><td>99.48</td></tr><tr><td>Mean rounds</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CC</td><td>29.10</td><td>25.36</td><td>25.22</td><td>25.10</td><td>24.96</td></tr><tr><td>CC+ (partial)</td><td>29.04</td><td>31.22</td><td>31.40</td><td>31.10</td><td>30.90</td></tr><tr><td>CC+ (full)</td><td>44.78</td><td>37.80</td><td>37.94</td><td>37.50</td><td>37.26</td></tr><tr><td>iBundle</td><td>77.08</td><td>277.84</td><td>193.48</td><td>130.44</td><td>75.86</td></tr><tr><td>Clock-proxy*</td><td>24.24</td><td>23.54</td><td>23.30</td><td>23.30</td><td>23.02</td></tr><tr><td>Mean no. of bids</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CC</td><td>295.18</td><td>452.50</td><td>479.92</td><td>562.50</td><td>805.88</td></tr><tr><td>CC+ (partial)</td><td>295.12</td><td>475.72</td><td>505.56</td><td>586.30</td><td>828.92</td></tr><tr><td>CC+ (full)</td><td>332.88</td><td>471.36</td><td>501.08</td><td>582.22</td><td>825.44</td></tr><tr><td>iBundle</td><td>7,785.48</td><td>5,791.42</td><td>5,051.68</td><td>4,941.52</td><td>6,440.32</td></tr><tr><td>Mean revenue in %</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CC</td><td>69.43</td><td>83.74</td><td>83.30</td><td>84.23</td><td>84.30</td></tr><tr><td>CC+ (partial, core)</td><td>55.34</td><td>58.80</td><td>58.23</td><td>58.67</td><td>58.77</td></tr><tr><td>CC+ (full, core)</td><td>55.02</td><td>56.31</td><td>55.83</td><td>56.33</td><td>56.31</td></tr><tr><td>CC+ (partial, VCG)</td><td>49.19</td><td>52.77</td><td>52.64</td><td>52.78</td><td>52.76</td></tr><tr><td>CC+ (full, VCG)</td><td>46.32</td><td>47.29</td><td>46.87</td><td>47.41</td><td>47.40</td></tr><tr><td>iBundle</td><td>59.58</td><td>56.01</td><td>53.84</td><td>54.18</td><td>54.14</td></tr><tr><td>Clock-proxy</td><td>58.74</td><td>58.42</td><td>58.40</td><td>58.40</td><td>58.24</td></tr></table>

<sup>∗</sup>Clock phase only.

Table 5 Real Estate 3 × 3 with 9 Items and 5 Bidders (VCG Bidder Gain 15.31%)

<table><tr><td rowspan="2">Measure</td><td colspan="5">Bidder type</td></tr><tr><td>Straightforward</td><td>5 of 20</td><td>Powerset6</td><td>Powerset10</td><td>Powerset</td></tr><tr><td>Mean efficiency in %</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CC</td><td>96.52</td><td>98.00</td><td>96.99</td><td>97.97</td><td>99.03</td></tr><tr><td>CC+ (partial)</td><td>96.37</td><td>99.04</td><td>97.47</td><td>98.15</td><td>100.00</td></tr><tr><td>CC+ (full)</td><td>96.47</td><td>99.04</td><td>97.47</td><td>98.15</td><td>100.00</td></tr><tr><td>iBundle</td><td>100.00</td><td>93.92</td><td>98.91</td><td>99.30</td><td>43.02</td></tr><tr><td>Clock-proxy</td><td>97.87</td><td>99.16</td><td>98.35</td><td>98.35</td><td>100.00</td></tr><tr><td>Min. efficiency in %</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CC</td><td>71.85</td><td>85.63</td><td>80.64</td><td>75.18</td><td>90.02</td></tr><tr><td>CC+ (partial)</td><td>71.85</td><td>93.17</td><td>80.64</td><td>75.18</td><td>99.90</td></tr><tr><td>CC+ (full)</td><td>71.85</td><td>93.17</td><td>75.18</td><td>75.18</td><td>99.90</td></tr><tr><td>iBundle</td><td>100.00</td><td>81.05</td><td>92.74</td><td>96.04</td><td>14.40</td></tr><tr><td>Clock-proxy</td><td>71.85</td><td>93.17</td><td>75.18</td><td>75.18</td><td>99.95</td></tr><tr><td>Mean rounds</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CC</td><td>288.44</td><td>270.04</td><td>269.88</td><td>268.44</td><td>264.36</td></tr><tr><td>CC+ (partial)</td><td>291.44</td><td>293.64</td><td>295.10</td><td>291.70</td><td>287.38</td></tr><tr><td>CC+ (full)</td><td>329.02</td><td>299.14</td><td>300.00</td><td>295.72</td><td>294.82</td></tr><tr><td>iBundle</td><td>1,537.18</td><td>19,951.04</td><td>16,176.36</td><td>9,756.16</td><td>1.00</td></tr><tr><td>Clock-proxy*</td><td>274.76</td><td>268.42</td><td>264.26</td><td>264.26</td><td>263.24</td></tr><tr><td>Mean no. of bids</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CC</td><td>1,914.74</td><td>5,421.78</td><td>6,397.74</td><td>10,061.70</td><td>80,269.48</td></tr><tr><td>CC+ (partial)</td><td>1,922.86</td><td>5,484.46</td><td>6,467.54</td><td>10,127.52</td><td>80,337.72</td></tr><tr><td>CC+ (full)</td><td>1,995.94</td><td>5,484.72</td><td>6,465.74</td><td>10,126.56</td><td>80,340.70</td></tr><tr><td>iBundle</td><td>484,560.06</td><td>452,946.94</td><td>4,022,475.72</td><td>414,268.22</td><td>645.00</td></tr><tr><td>Mean revenue in %</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CC</td><td>87.12</td><td>96.02</td><td>94.38</td><td>95.71</td><td>97.07</td></tr><tr><td>CC+ (partial, Core)</td><td>68.02</td><td>84.20</td><td>75.40</td><td>82.21</td><td>86.60</td></tr><tr><td>CC+ (full, Core)</td><td>67.80</td><td>83.46</td><td>74.77</td><td>81.56</td><td>85.91</td></tr><tr><td>CC+ (partial, VCG)</td><td>56.68</td><td>82.98</td><td>71.87</td><td>80.45</td><td>85.89</td></tr><tr><td>CC+ (full, VCG)</td><td>55.84</td><td>81.52</td><td>70.55</td><td>79.45</td><td>84.79</td></tr><tr><td>iBundle</td><td>86.07</td><td>81.46</td><td>83.72</td><td>84.14</td><td>0.00</td></tr><tr><td>Clock-proxy</td><td>73.60</td><td>83.49</td><td>82.00</td><td>82.00</td><td>85.92</td></tr></table>

<sup>∗</sup>Clock phase only.

Table 6 Real Estate 5 × 3 with 15 Items and 5 + 1 Bidders (VCG Bidder Gain 15.5%)

<table><tr><td rowspan="2">Measure</td><td colspan="5">Bidder type</td></tr><tr><td>Straightforward</td><td>5 of 20</td><td>Powerset6</td><td>Powerset10</td><td>Powerset</td></tr><tr><td>Mean efficiency in %</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CC</td><td>83.01</td><td>93.80</td><td>90.19</td><td>92.09</td><td>99.29</td></tr><tr><td>CC+ (partial)</td><td>83.17</td><td>93.93</td><td>90.09</td><td>91.93</td><td>99.87</td></tr><tr><td>CC+ (full)</td><td>83.09</td><td>93.90</td><td>90.09</td><td>91.93</td><td>99.86</td></tr><tr><td>Min. efficiency in %</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CC</td><td>60.78</td><td>74.32</td><td>74.32</td><td>74.32</td><td>89.61</td></tr><tr><td>CC+ (partial)</td><td>60.78</td><td>74.32</td><td>74.32</td><td>74.32</td><td>99.07</td></tr><tr><td>CC+ (full)</td><td>60.78</td><td>74.32</td><td>74.32</td><td>74.32</td><td>99.07</td></tr><tr><td>Mean rounds</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CC</td><td>42.34</td><td>40.98</td><td>40.04</td><td>39.58</td><td>38.40</td></tr><tr><td>CC+ (partial)</td><td>42.62</td><td>42.64</td><td>43.10</td><td>42.78</td><td>42.58</td></tr><tr><td>CC+ (full)</td><td>44.70</td><td>43.36</td><td>43.66</td><td>43.40</td><td>43.06</td></tr><tr><td>Mean no. of bids</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CC</td><td>247.74</td><td>919.22</td><td>1,099.54</td><td>1,780.52</td><td>368,823.10</td></tr><tr><td>CC+ (partial)</td><td>248.10</td><td>929.68</td><td>1,109.38</td><td>1,795.28</td><td>369,040.14</td></tr><tr><td>CC+ (full)</td><td>251.16</td><td>929.74</td><td>1,109.30</td><td>1,795.32</td><td>369,040.14</td></tr><tr><td>Mean revenue in %</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CC</td><td>78.79</td><td>89.67</td><td>85.94</td><td>88.29</td><td>96.93</td></tr><tr><td>CC+ (partial, core)</td><td>64.93</td><td>77.47</td><td>74.09</td><td>76.86</td><td>87.50</td></tr><tr><td>CC+ (full, core)</td><td>64.75</td><td>77.36</td><td>73.99</td><td>76.76</td><td>87.35</td></tr><tr><td>CC+ (partial, VCG)</td><td>59.49</td><td>70.16</td><td>67.88</td><td>70.41</td><td>84.23</td></tr><tr><td>CC+ (full, VCG)</td><td>58.25</td><td>69.90</td><td>67.82</td><td>70.23</td><td>83.89</td></tr></table>

The clock-proxy auction achieves the highest levels of efficiency regardless of the bidding strategy. This is because the bidding agents were not restricted in the proxy phase and submitted bids on all packages, for which their valuation exceeded the ask prices of the clock phase. Not only that, the second core-selecting proxy phase requires an elaborate software infrastructure, and bidders in the field are not likely to submit as many bids in the second phase for the same reasons as we assumed restricted bidding in the clock phase. The reason that the clock-proxy auction was not 100% efficient is that bidders cannot submit bids on all possible packages but just on those where the valuation is higher than the bid price in the last clock round. Note that the efficiency gains over the CC+ auction were small. We did not report on experiments with restricted bidders in the proxy phase because this would require additional assumptions. However, if also we enforced strong restrictions in the Proxy phase, the efficiency of the clock-proxy auction was at or below the level of the CC+ auction.

In the following, we refer to the Real Estate $5 \times 3$ value model as a large value model because bidders are interested in 443 or even 32,767 packages. All other value models are referred to as small. Note that in realistic applications, we do not expect bidders to have several hundred or thousands of positive valuations for packages, and the ”small”

value models describe realistic problem sizes with up to 129 packages with a positive valuation.

Result 2 (Efficiency of the CC and the CC<sub>+</sub> Auction in Small and Large Value Models). <sub>In</sub> <sub>the</sub> small value models, the CC+ auction achieves significantly higher efficiency than does the CC auction $( \mathrm { C C } + \mathrm { ~ \succ ~ } ^ { \cdot * * * } \mathrm { ~ \ " C C ~ o r ~ \ : C C } + \mathrm { ~ \ ` * ~ } \mathrm { C C } ,$ depending on the value model and on the type of the powerset bidder). In the large Real Estate $5 \times 3$ value model with powerset bidders, the CC+ auction has significantly higher efficiency $( \mathrm { C C } + \succ ^ { * * * } \mathrm { C C } )$ , but there are no significant differences for restricted bidding strategies.

In small value models, Powerset6 and Powerset10 bidders reveal a larger proportion of their valuations, which has a positive effect on the efficiency. In the larger Real Estate $5 \times 3$ value model, a smaller proportion of the valuations are revealed in each round and the advantages of the CC+ auction compared to the CC auction vanish. Note that even for such a large value model, the mean efficiency is around 92% even for powerset bidders, who are restricted to 6 or 10 bids per round, and almost 94% for Heuristic 5 of 20 bidders.

From our theoretical treatment, we know that the efficiency of the CC auction can be almost 0% in the worst case. In the following, we take a look at the lowest efficiency, which has been achieved in experiments with different CATS value models.

Result 3 (Minimum Efficiency for Restricted and Unrestricted Powerset Bidders). <sub>In</sub> <sub>Airport,</sub> Transportation, and Pairwise Synergy value models, the CC auction and iBundle have significantly lower minimum efficiency than does the CC+ auction for restricted and unrestricted powerset bidders (see also Appendix E). In the Real Estate 3 × 3 and $5 \times 3$ value models, the minimum efficiency goes down to 74% for restricted bidders. With powerset bidders, the minimum efficiency in the CC auction was always significantly lower than in the CC+ auction, which was almost fully efficient also in the worst case (CC+ $\succ ^ { \ast \ast \ast } \ \mathrm { C C } )$ . Despite straightforward bidding strategies in some value models, in which the clock-proxy auction outperforms the CC+ auction, minimum efficiency is similiar in both auction formats.

Result 4 (Number of Rounds and Bids). <sub>The</sub> <sub>dif-</sub> ference in the number of rounds and bids between CC and CC+ is always significant $( \mathrm { C C } + \succ ^ { * * * } \mathrm { C C } )$ but rather small. Note that the number of rounds of a CC+ auction with full revelation price update rule is not necessarily higher than in the CC+ auction with a partial revelation price update rule because prices on more items are increased by the CC+ auction with full revelation price update rule. The number of rounds in iBundle is orders of magnitude higher than in the CC or the CC+ auction. With powerset bidders iBundle terminates prematurely because of the termination rule, which can result in low revenue and number of rounds, as for example in the Real Estate 3 × 3 value model. In this value model, there were several thousand auction rounds in iBundle. The rounds of the clock-proxy auction were below that of the CC auction because the auction stops as soon as there is no overdemand on any of the items. The statistic does not reflect the number of rounds in the proxy phase.

We always used a minimum bid increment of 1. Clearly, the number of auction rounds can be decreased by increasing the bid increment, but at the expense of efficiency. Note that the valuations in the Real Estate $3 \times 3$ value model were determined in a very different way from the Real Estate 5 × 3 model, as was explained in §5.1. The valuations for items and packages were on different levels, leading to a different number of auction rounds and a different number of bids submitted.

Result 5 (Average Revenue). <sub>The</sub> <sub>average</sub> <sub>auc-</sub> tioneer revenue is the highest in the CC auction and decreases significantly with the introduction of bidder-Pareto-optimal core prices and even more so with VCG prices $( \mathrm { C C ~ } \succ ^ { * * * } \ \mathrm { C C } + \ ( \mathrm { C o r e } ) \ \succ ^ { * * * } \ \mathrm { C C } +$ (VCG)). The revenue of iBundle with straightforward bidders is significantly higher than that of the CC+ auction with powerset bidders and a VCG rule. The revenue generated by the clock-proxy auction is similar to that of the CC+ auction with bidder optimal core prices, except from straightforward bidding agents, where the clock-proxy auction achieves higher revenue.

Note that iBundle is always in the core with straightforward bidders, whereas the VCG mechanism is not, which can lead to lower revenue if valuations are not buyer submodular.

## 5.3. Summary

As theory predicts, iBundle is fully efficient in the computational experiments with straightforward bidders, and so is the CC+ auction with powerset bidders. This full efficiency comes at a cost in both auction formats. The number of auction rounds in the CC+ auction is only slightly increased compared to the CC auction, but the number of bids submitted by powerset bidders was much higher, in particular with the large Real Estate 5 × 3 value model. Note that the number of bids revealed in iBundle with straightforward bidders was an order of magnitude higher than the number of bids submitted by a fully efficient CC+ auction with powerset bidders in all value models. For example, in the Transportation value model, the fully efficient CC+ auction led to 825.44 bids on average, whereas iBundle led to 7,785.48 bids. This was even worse in the case of the Real Estate 3 × 3 value model (80,340.70 in CC+ versus 484,560.00 bids on average in iBundle) and the Real Estate 5 × 3 value model, where more than 4.8 million bids were submitted in the experiments that we ran.

If bidders are not able to follow such equilibrium strategies, either for the number of rounds or the number of bids that need to be submitted, and are restricted in the number of bids submitted in each round, full efficiency can no longer be reached. To gain an understanding of how such restrictions impact efficiency, we have run simulations with the Heuristic 5 of 20, Powerset6, and Powerset10 bidders. Interestingly, the auctions still yield fairly high levels of efficiency on average, mostly higher than 90%. Note, however, that the number of rounds and the number of bids submitted in iBundle is much higher than in the CC or the CC+ auctions. In most applications with human bidders, more than 50 auction rounds would not be acceptable, and the auctioneer would have to increase the minimum bid increment significantly in iBundle, which can lead to additional inefficiencies. The clock-proxy auction yielded higher levels of efficiency, but only under the assumption that bidders submitted bids on all packages with positive payoff in the second phase. In the field, bidders will likely bid on a subset of these packages. We found that in simulations where the restrictions of the clock phase also hold in the proxy phase, the efficiency of the CC+ auction was higher than that of the clock-proxy auction.

## 6. Human Subject Experiments

In addition to the computational experiments we analyze the impact that the CC+ auction has on efficiency as compared to the traditional CC auction in human subject experiments. Our experimental setup is aligned at spectrum auctions for the 2.6 GHz band conducted in several European countries. The strategic situation in these markets is such that it would make sense to reduce demand in a CC auction, whereas these incentives are reduced in a CC+ auction with a VCG payment rule. We decided to implement the CC+ version with a partial revelation price update rule because we believe that this auction format could be agreeable in practice. Although the main contribution of this paper is theoretical, this small set of experiments should highlight that there are realworld markets where the CC+ auctions can actually increase efficiency as compared to the CC auction.

## 6.1. The Value Model

In the value model, we used the 2.6 GHz FDD spectrum band plan as it is available in many European countries. There are 14 paired blocks (or items), which are of main interest to telecoms as they allow for implementation of the long-term-evolution (LTE) standard. There are also up to 10 unpaired blocks, which typically are of much lower interest, drawing only little competition. Therefore, we focus on the 14 pairs of spectrum blocks.

Bidders had a positive valuation for up to six items with free disposal for packages greater than that. Each bidder received a base valuation $v _ { A }$ for the single item, which is drawn randomly from a uniform distribution in the range of 61201 2007. In an attempt to reflect the technical properties of LTE, we modeled ascending complementarities in the valuation of packages of several items. A package of two items received a value of $1 . 2 * 2 * v _ { A } ,$ i.e., a complementarity bonus of 20% on top of the base valuations. In reality, four blocks allow for peak performance rates with LTE. Thus the complementarity in the value model rose with the number of items in the package. A package of three items had a complementarity of 40% and a package of four items a bonus of 80%. There was no additional bonus for the fifth and sixth item. In most European countries there are four competitors.

Because there are 14 blocks to be sold and each bidder has the highest per item valuation for 4 blocks, this creates a specific strategic situation. It is possible that either two or three bidders obtain a package of four blocks, whereas the other bidders win only two or three blocks. We assumed item valuations to be bidder specific but the synergy structure of packages to be the same for all bidders because they lead to similar benefits on the telecommunication market.

## 6.2. Lab Procedures and Organization

The experiments were conducted at our university in 2011. Valuations were drawn for four waves (A through D) randomly. Each wave consisted of four different auctions that were conducted in the lab within one session. In a session either the CC or the CC+ auction was used, resulting in 16 CC auctions and 16 CC+ auctions. Subjects were recruited from the departments of Mathematics and Computer Science. In total, 32 students participated in the experiments. Each lab subject participated either in one CC or in one CC+ session but never in both. One session lasted an average of 100 minutes.

All the information and training required was provided to the participants at the beginning of each session. Subjects were made familiar with the auction software through a demo auction. Before each auction all subjects received the individual valuation, the distribution of valuations, and information about the complementarity structure. Each round took three minutes. The subjects could ask for more time if required. The bid increment of 20 francs (the lab currency) per item was the same for each session. Bidders had to place at least one bid at current prices to stay eligible for bidding in the next round.

After each session subjects were compensated financially. The total compensation resulted from their gain in the auction. The auction gain consisted of a 12 euro participation fee plus the payoff of the auctions converted from francs into euro by a 50:1 ratio. Negative payoffs were deducted from the participation fee. On average each subject received 30 euro.

## 6.3. Results

We were mainly interested in efficiency and revenue of the two auctions and in bidder behavior. In particular, we wanted to understand for which packages bidders submitted bids. Some of the main metrics are summarized in Table 7.

Result 6 (Bidder Behavior). <sub>Bidders</sub> <sub>in</sub> <sub>the</sub> <sub>CC+</sub> auction followed almost a powerset strategy, whereas bidders in the CC auction reduced their demand early in the auction.

Support: Although bidders in the CC+ auction did not follow a full powerset strategy, they bid on average on 501 of the 6 distinct packages and they bid on average in 1403 rounds until the weakest bidder had reached his valuation and dropped out of the auction. In contrast to the bidder behavior in the CC+ auctions, bidders in CC reduced their demand early in the auction, aiming for an allocation at low prices (in 13 out of 16 auctions all four bidders won a package). This means that the strongest bidder reduced his demand from the most valuable package of six items often to four items while weaker bidders frequently submitted bids for two or three items only.

Table 7 Average Aggregate Measures of Auction Performance

<table><tr><td>Auction format</td><td>Efficiency (%)</td><td>Revenue (%)</td><td>Rounds</td><td>Number of winning bidders</td><td>Bids on distinct packages</td><td>Number of bids</td></tr><tr><td>CC</td><td>89.9</td><td>39.9</td><td>5.5</td><td>3.8</td><td>2.8</td><td>41.7</td></tr><tr><td>CC+</td><td>97.7</td><td>67.7</td><td>14.3</td><td>3.2</td><td>5.1</td><td>164.2</td></tr></table>

The CC auctions terminated on average after 505 auction rounds, and bidders only submitted bids on 208 distinct packages. Overall, the CC+ auction elicited many more packages and we did not observe the level of demand reduction as in the CC auction.

<sup>Result</sup> <sup>7</sup> <sup>(Efficiency).</sup> Efficiency in the CC+ auction was significantly higher than in the CC auction.

Support: The nonparametric Wilcoxon rank sum test (Hollander and Wolfe 1973) shows a significant difference in efficiency on a 1% level (W = 59, p-value = 000098). The observed demand reduction (see Result 6) in the CC auctions caused a low number of bids (41.7 in CC auctions on average) and low allocative efficiency. In the CC+ auction this phenomenon vanished, and bidders submitted more bids (164.2 on average) on different packages.

<sup>Result</sup> <sup>8</sup> <sup>(Revenue).</sup> Although bidders received a VCG discount, in the CC+ auction revenue was significantly higher than in the CC auction. The bidder payoffs were higher in the CC auction than in the CC+ auction.

Support: The demand reduction and the early termination of the CC auctions led to low item prices and thus a low auctioneer revenue in this value model. In the CC+ auction, bid prices were high and the VCG discounts rather small, resulting in a significantly higher auctioneer revenue compared to the CC auction. Because of the aggressive demand reduction and the low item prices, bidders in the CC auction received a significantly higher payoff in the CC auction.

The CC auction often led to high levels of efficiency and revenue in the lab. The specific value model here set incentives for demand reduction in the CC auction. The VCG payment rule is the main explanation for different bidding behavior in the CC+ auction. In other experiments with different value models, the CC+ price update rule might matter. Note that the focus of this paper is the theoretical analysis and the intention of these experiments was not to provide a comprehensive study of bidder behavior in the CC auction but to illustrate that there are realistic environments where the rules of the CC+ auction can have a significant positive impact on efficiency.

## 7. Conclusions

Combinatorial auctions have led to a substantial amount of research and found a number of applications in high-stakes auctions for industrial procurement, logistics, energy trading, and the sale of spectrum licenses. Anonymous linear ask prices are very desirable and sometimes even essential for many of these applications (Meeus et al. 2009). Unfortunately, Walrasian equilibria with linear prices are only possible for restricted valuations. Already Kelso and Crawford (1982) showed that the goods are substitutes property (aka gross substitutes) is a sufficient and an almost necessary condition for the existence of linear competitive equilibrium prices. Later, Gul and Stacchetti (2000) found that even if bidders’ valuation functions satisfy the restrictive goods are substitutes condition, no ascending VCG auction exists that uses anonymous linear prices. Bikhchandani and Ostroy (2002) show that personalized nonlinear competitive equilibrium prices always exist. Several auction designs are based on these fundamental theoretical results and use nonlinear personalized prices. Although these NLPPAs achieve efficiency, they only satisfy an ex post equilibrium if the valuations meet buyer submodularity conditions, and they lead to a very large number of auction rounds requiring bidders to follow the straightforward strategy throughout.

These theoretical results assume final ask prices and the payments of bidders to be equivalent. The CC auction differentiates, which is also a way around the negative theoretical results. Still, the CC auction (Porter et al. 2003) cannot be fully efficient. We provide worst-case bounds on the efficiency of the CC auction with straightforward bidders and propose an extension of the CC auction, the CC+ auction design, which achieves full efficiency with bidders following a powerset strategy. This design modifies the price update rule of the CC auction and adds a VCG payment rule. We show that with these new rules, a clock auction can achieve full efficiency in an ex post equilibrium. Note that there are no restrictions on the type of valuations of bidders, which is important for any application. The discussion also shows that the number of ask prices that need to be communicated by the auctioneer, as well as the number of bids required by bidders, is significantly lower than in NLPPAs.

This paper provides theory on combinatorial clock auctions that has been missing in the literature so far. In particular, we show under which conditions full efficiency with a strong solution concept for general valuations is possible with a clock auction. This theory helps understand possible sources of inefficiency in the field, where bidders might not be able to follow their equilibrium strategy or some rules of the CC+ auction might not be applicable. If we aim for a proofable ex post equilibrium, the CC+ auction can be described as a VCG mechanism in multiple rounds. A CC+ auction with a partial revelation price update rule might well be used in practice. Although such a relaxation would not satisfy an ex post equilibrum any more, speculation is still very hard for bidders and requires almost complete information about bidder valuations.

Communication complexity is a problem in all efficient combinatorial auctions. In the CC+ auction bidders might not be willing or able to follow a powerset strategy. Therefore, we also analyzed the CC and the CC+ auction in computational experiments to understand how robust the CC+ auction is against deviations from the powerset equilibrium strategy. Interestingly, even if the number of bids submitted in each round is severely restricted or bidders heuristically select some of their “best” package bids in each round, both the CC and the CC+ auction achieved very high levels of efficiency, providing evidence for the robustness of clock auctions against different types of bidding strategies. Robustness is an important criterion in the field. Finally, a lab experiment illustrated that such rules can well have an impact on efficiency in small but realistic environments with human bidders.

## Acknowledgments

The financial support from the German Science Foundation (DFG) (BI 1057/3-1) is gratefully acknowledged. The authors also thank Felix Brandt for valuable feedback on this paper.

## Appendix A. Proofs

<sup>Proposition</sup> <sup>1.</sup> If bidder valuations are demand masking and all bidders follow the straightforward strategy in the CC auction, then the efficiency converges $\scriptstyle { \log 2 / ( m + 1 ) }$ in the worst case.

<sup>Proof.</sup> The following proof is provided for two or more items for sale and 2m − 1 bidders. With less than 2m − 1 bidders and XOR bidding, efficiency can only increase. Without loss of generality, we assume item-level bid increments of $\epsilon = 1$ in each round $t \in \mathcal { T } \subset \mathbb { N } .$ . We consider the value  as given and determine  and $\nu _ { h }$ such that efficiency decreases to the worst case of 0%.

Case (a) $\mu \geq \xi + \sum _ { h } \nu _ { h } \mathrm { . }$ : The efficient solution is to sell R ∪ $S _ { h }$ to one of the bidders $h _ { a }$ or $h _ { b }$ . The CC auction terminates with the efficient outcome in this case.

Case (b) $\begin{array} { r } { \mu < \xi + \sum _ { h } \nu _ { h } \wedge \xi = \mu ; } \end{array}$ The proof is by showing that a straightforward bidder $h _ { a }$ cannot bid on ${ \dot { S _ { h } } }$ throughout the auction in a demand masking set of valuations. For this, the payoff $\pi _ { h _ { a } } ( R { \dot { \cup } } S _ { k } )$ must be higher than $\pi _ { h _ { a } } ( S _ { h } )$ for each bidder $h _ { a }$ in each round of the auction $t \in { \mathcal { T } }$

$$
\begin{array}{l} v _ {h _ {a}} (R \dot {\cup} S _ {h}) - \beta_ {h _ {a}, t} (R \dot {\cup} S _ {h}) \\ > v _ {h _ {a}} (S _ {h}) - \beta_ {h _ {a}, t} (S _ {h}) \quad \forall   h \in \{2, \ldots , g \},   \forall   t \in \mathcal {T}. \end{array}\tag{A1}
$$

Because we know that $v _ { h _ { a } } ( R \dot { \cup } S _ { h } ) = v _ { h _ { b } } ( R \dot { \cup } S _ { h } ) = \mu ,$ and all bidders bid straightforward, we know that the price for all the items in $\mathcal { K }$ rises in each round by . Therefore, inequality (1) can be rewritten as

$$
\begin{array}{c} \mu - | R \dot {\cup} S _ {h} | t \epsilon > \nu_ {h} - | S _ {h} | t \epsilon \stackrel {{\epsilon = 1}} {{\Longrightarrow}} t <   \frac {\mu - \nu_ {h}}{| R |} \\ \forall h \in \{2, \ldots , g \}, \forall t \in \mathcal {T}. \end{array}\tag{A2}
$$

Inequality (2) shows that as long as t is smaller than the right-hand side, a straightforward bidder always bids on the package $R \dot { \cup } S _ { h }$ . We can now determine a round $t _ { \mathrm { m i n } } =$ min $\mathsf { i } \bar { \{ t | t \geq ( \mu - \nu _ { h } ) / | R | , \forall h _ { a } \} }$ , in which the payoff $\pi _ { h _ { a } } ( R { \dot { \cup } } S _ { h } )$ is for the first time smaller or equal to the payoff $\pi _ { h _ { a } } ( S _ { h } )$ We call $t _ { \mathrm { m i n } }$ the decisive round. If either the right side or both sides of inequality (1) become negative in round $t _ { \mathrm { m i n } } ,$ bidder $h _ { a }$ cannot bid on $S _ { h }$ or the auction ends for bidder $h _ { a }$ because the ask price for $R \dot { \cup } S _ { h }$ is also higher than $v _ { h _ { a } } ( R \dot { \cup } S _ { h } )$ . If straightforward bidder $h _ { a }$ does not reveal his preferences for $S _ { h }$ throughout the auction, then the auctioneer in a class A auction selects any of the other bids with a revenue of $\mu ,$ resulting in an efficiency of $\mu / ( \xi + \textstyle \sum _ { h } \nu _ { h } )$

We determine maximal $\nu _ { h }$ such that in round $t _ { \mathrm { m i n } }$ the payoff of bidder $h _ { a }$ on package $S _ { h }$ is negative, which minimizes efficiency. We know that as long as bidder $h _ { a } ^ { \prime } \mathbf { s }$ payoff is negative in the decisive round $t _ { \mathrm { m i n } } , \mathrm { i . e . , } \nu _ { h } - | S _ { h } | t _ { \mathrm { m i n } } < 0 ,$ then bidder $h _ { a }$ does not bid on $S _ { h }$ . We also know that $t _ { \mathrm { m i n } } =$ $\lceil ( \mu - \nu _ { h } ) / | R | \rceil$ is the decisive round. We can now maximize $\nu _ { h }$ such that $\nu _ { h } - | S _ { h } | \lceil ( \mu - \nu _ { h } ) / | R | \rceil < 0$ , resulting in $\nu _ { h _ { \mathrm { m a x } } } =$ max $\{ \nu _ { h } | \nu _ { h } < | S _ { h } | \mu / ( | R | + | S _ { h } | ) \}$ . In order to maximize $\sum _ { h } \nu _ { h }$ and so minimize the efficiency $\textstyle \mu / ( \xi + \sum _ { h } \nu _ { h } )$ , we set $| R | = 1$ and $| S _ { h } | = 1$ for all $h \in \{ 2 , \ldots , \overset { } { g } \}$ . This results in an efficiency of $\begin{array} { r } { E ( X ) = \mu / ( \xi + \sum _ { h } { ( \mu / 2 - \rho ) } ) } \end{array}$ with $\rho > 0$ . With $\rho \to 0$ and $\xi = \mu$ efficiency decreases to $2 / ( g + 1 )$ , which is $2 / ( m + 1 )$ in the worst case. Note that it does not matter if $\xi$ is smaller or larger than $\sum _ { h } \nu _ { h }$

Case (c) $\begin{array} { r } { \mu < \xi + \sum _ { h } \nu _ { h } \wedge \mu \neq \xi ; } \end{array}$ : Efficiency can only increase compared to case (b) considering the worst case. Either the enumerator of $\begin{array} { r } { E ( X ) = ( \operatorname* { m a x } \{ \xi , \mu \} ) / ( \operatorname* { m a x } \{ \xi + \sum _ { h } \nu _ { h } , \mu + } \end{array}$ $\textstyle \sum _ { h } \nu _ { h } \operatorname { j } )$ increases or the denominator decreases.

$\xi > \mu ; \Rightarrow E ( X ) = \xi / ( \xi + \sum _ { h } \nu _ { h } ) = ( \mu + \delta ) / ( \mu + \delta + \sum _ { h } \nu _ { h } )$ with $\delta > 0$ is always greater than the efficiency E4X5 in case (b).

— either $\begin{array} { r } { E ( X ) = \mu / ( \xi + \sum _ { h } \nu _ { h } ) } \end{array}$ , which is greater than $\begin{array} { r } { E ( X ) = \mu / ( \mu + \sum _ { h } \nu _ { h } ) } \end{array}$ , the efficiency of case (b).

$- \mathrm { o r } E ( X ) = \mu / ( \mu + \textstyle \sum _ { h = 2 } ^ { g - 1 } \nu _ { h } )$ , which is also greater than $\begin{array} { r } { E ( X ) = \mu / ( \mu + \sum _ { h = 2 } ^ { g } \nu _ { h } ) } \end{array}$ , the efficiency of case (b). <sup></sup>

<sup>Proposition</sup> <sup>2.</sup> If all bidders follow the powerset strategy, the efficiency of the CC auction converges to 0% in the worst case.

Table A.1 Valuations that Lead to Inefficiencies in the CC Auction with Assuming Powerset Bidders

<table><tr><td></td><td>(1,2)</td><td>(2,3)</td></tr><tr><td> $V_1$ </td><td>4</td><td> $\mu$ </td></tr><tr><td> $V_2$ </td><td>2</td><td>0</td></tr></table>

<sup>Proof.</sup> Because efficiency cannot be negative, it is sufficient to present an example in which the efficiency is almost 0%. Assume two bidders and three items for sale. The two bidders have valuations for packages as shown in Table A.1. They value all other packages at zero. The final ask prices are $\begin{array} { r } { \dot { \boldsymbol { \beta } } _ { ( 1 ) } = 2 , \beta _ { ( 2 ) } = 2 , } \end{array}$ and $\beta _ { ( 3 ) } = 1 ,$ and the final allocation assigns package 411 25 to bidder 1, which is inefficient if $\mu > 4$ . Efficiency decreases to 0% if $\mu \to \infty$ 

We assume no free disposal concerning the valuations in Table A.1. For example, if an auction is used to procure raw materials, extra quantity can lead to inventory costs. For the sale of property rigths, extra rights might lead to additional obligations of the owner, which come at a cost. Sometimes such costs are negligible, but this is not always the case. Otherwise, bidder 1 has a valuation of  also for package $( 1 , 2 , 3 )$ , and this would be sold to bidder 1 for a price of 5. The payoff for bidder 1 in this allocation would be $\mu - 5 ,$ which would be efficient because the sum of the bidders’ payoffs and the auctioneer revenue is maximized. Free disposal can lead to situations in which powerset bidding drives up prices to very high levels and reduces bidders’ utility. It can also lead to high inefficiency (see Appendix C). Consequently, powerset bidding is even more unlikely in a CC auction with free disposal.

<sup>Corollary</sup> <sup>1.</sup> If all bidders follow the powerset strategy, the CC auction with the partial revelation price update rule and sufficiently small bid increments terminates with an efficient outcome.

<sup>Proof.</sup> Based on the statement of Theorem 1, we only need to show that the valuations of relevant packages are revealed with powerset bidders in the modified CC auction. Through the construction of the partial revelation price update rule, powerset bidders who are not part of the efficient allocation reveal all their valuations. But the rule also ensures that all the bidders in the efficient allocation reveal their valuations on all packages except the ones that are in the winning allocation. As long as a bidder bids on a package that is not winning, prices increase and he can keep bidding. Thus the CC auction with the partial price update rule elicits all valuations except the ones of winning packages and terminates with an efficient allocation. <sup></sup>

<sup>Corollary</sup> <sup>2.</sup> A powerset strategy is an ex post equilibrium in the CC+ auction with the full revelation price update rule.

<sup>Proof.</sup> The proof for the ex post equilibrium strategy is from the VCG mechanism. Let $t _ { j }$ denote the type of bidder j. We look at the bidder j and assume all other bidders follow the truth revealing powerset strategy. Bidder j receives a payment of $\begin{array} { r } { \sum _ { i \ne j } \overline { { u } } _ { i } ( t _ { i } ^ { \prime } , X ) - \sum _ { i \ne j } u _ { i } \overline { { ( t _ { i } ^ { \prime } , { X } _ { - j } ) } } } \end{array}$ from the center. The final payoff to bidder j reporting type t<sup>0</sup>, an allocation $X ,$ and a VCG payment rule is $\begin{array} { r } { u _ { i } ( t _ { i } , X ) + \sum _ { i \neq j } u _ { i } ( t _ { i } ^ { \prime } , X ) - \sum _ { i \neq j } u _ { i } ( t _ { i } ^ { \prime } , X _ { - j } ) } \end{array}$ . A bidder in this payment rule cannot affect the choice of $X _ { - j } .$ Hence, j can focus on maximizing $\begin{array} { r } { u _ { j } ( t _ { j } , X ) + \sum _ { i \neq j } u _ { i } ( t _ { i } ^ { \prime } , X ) , \mathrm { i . e . , } } \end{array}$ , his utility and the sum of the other’s utilities. Because the auction will maximize $\begin{array} { r } { \sum _ { i } u _ { i } ( t _ { i } ^ { \prime } , X ) , j ^ { \prime } \mathrm { s } } \end{array}$ utility will be maximized, $\mathrm { i f } \ t _ { j } ^ { \prime } = t _ { j }$

Table A.2 Valuations that Do Not Lead to an Ex Post Equilibrium with Powerset Bidders when Using the Partial Revelation Price Update Rule in the CC+ Auction

<table><tr><td></td><td>(1)</td><td>(2)</td></tr><tr><td> $V_1$ </td><td>0</td><td>3</td></tr><tr><td> $V_2$ </td><td>3*</td><td>0</td></tr><tr><td> $V_3$ </td><td>2</td><td>7*</td></tr></table>

The partial revelation price update rule is not sufficient for an ex post equilibrium: In the example in Table A.2, the CC+ auction with a partial revelation price update rule ends up with final ask prices of $\beta _ { ( 1 ) } = 3$ and $\beta _ { ( 2 ) } = 4$ before the VCG prices are calculated. If the auctioneer calculates VCG prices based on the submitted bids, then bidder 2 pays $3 - ( { \bar { 7 } } - 5 ) = 1$ for the item 415. If bidder 2 knew $v _ { 3 } ( 2 )$ , he could have bid up to 6 on item 425. This would increase the final ask price for 425 to 7 and lead to a new VCG price of $3 - ( 1 0 - { \mathsf { \bar { 7 } } } ) = 0$ for 415 for bidder 2. In a VCG mechanism, bidder 2 could not influence the bid submission of bidder 3 in a similar way, which is why the VCG mechanism has a dominant strategy. Therefore, in the CC+ auction with a partial revelation price update rule, the strategy of bidder 2 is not independent of other bidders’ types. Even if the other bidders bid truthfully, a bidder could improve his payoff by deviating from a truth revealing powerset strategy if he knew the other bidders’ types and the other bidders truthfully follow the powerset strategy. <sup></sup>

<sup>Corollary</sup> <sup>3.</sup> The CC+ auction with powerset bidders terminates with a core outcome if it charges bidder-Pareto-optimal prices as payments instead of VCG prices.

<sup>Proof.</sup> Because the CC+ auction elicit all valuations from all bidders and the algorithm from Day and Raghavan (2007) calculates core prices upon the submitted bids, the statement is shown. <sup></sup>

## Appendix B. Ex Post Equilibrium of the CC+ Auction

Does the CC+ auction satisfy a dominant strategy or an ex post equilibrium? In the single-unit case, there has been an interesting recent discussion on the types of ascending auctions that actually satisfy a dominant strategy equilibrium. Isaac et al. (2007) have shown that although the clock version of an ascending single-item auction has a dominant strategy, the widespread English auction, which allows jump bids, has not.

The CC+ auction can be seen as a multi-item generalization of the ascending clock auction. Also, the VCG auction can be thought of as a single-round version of the CC+ auction in which the bidder’s dominant strategy is to bid truthfully on all possible packages, similar to a powerset strategy. Both auctions satisfy a dominant strategy equilibrium. Does the CC+ auction also satisfy a dominant strategy, or is it restricted to an ex post equilibrium? In the following, we provide an example in which signals revealed throughout the $\mathrm { C C + }$ auction can make it beneficial for a bidder to deviate from his truth-telling powerset strategy when others deviate also from this strategy.

Table B.1 Example of the Difference Between the VCG Auction and the CC+ Auction

<table><tr><td></td><td>(1)</td><td>(2)</td><td>(1, 2)</td></tr><tr><td> $v_1$ </td><td>2*</td><td>0</td><td>0</td></tr><tr><td> $v_2$ </td><td>0</td><td>3*</td><td>0</td></tr><tr><td> $v_3$ </td><td>0</td><td>0</td><td>4</td></tr></table>

The valuations for three bidders and two items are given in Table B.1. The VCG price of bidder 1 is $2 - ( 5 - 4 ) = 1$ for item 415, and his payoff is 1. Now, assume that bidder 1 knows that bidder 2 will increase his bid on 425 to 4 if the ask price for 415 was 3. In round 2, the price clock ticks to 2 for each item and all three bidders signal demand at these prices. In round $^ { 3 , }$ prices are 3 for both items and again bidders 1 and 2 will signal demand. This will encourage bidder 2 to signal demand even in round 4 for item 425, when bidder 1 drops out. Now, bidder 1 gets a VCG price of $3 - ( 7 - 4 ) = 0$ and consequently increased his true payoff from 1 to 2. Bidder 2 learns through the course of the CC+ auction that there is a demand for 415 at a price of 3, which would not be possible in a direct revelation VCG auction.

This cannot happen in a clock auction with only a single item because the bidders can only drop out or continue to signal demand on a single item. This illustrates that the dominant strategy equilibrium does not extend from the single-item clock auction to its multiitem generalization. The powerset strategy in a multiitem CC+ auction is therefore an ex post equilibrium and not a dominant strategy equilibrium.

Table C.1 Valuations in an Economy with Powerset Bidders and Free Disposal

<table><tr><td></td><td>(1)</td><td>(2)</td><td> $\cdots$ </td><td>(m)</td></tr><tr><td> $v_1$ </td><td> $\mu$ </td><td>0</td><td> $\cdots$ </td><td>0</td></tr><tr><td> $v_2$ </td><td>0</td><td> $(\mu/m)-\epsilon$ </td><td> $\cdots$ </td><td>0</td></tr><tr><td> $\cdots$ </td><td> $\cdots$ </td><td> $\cdots$ </td><td> $\cdots$ </td><td> $\cdots$ </td></tr><tr><td> $v_m$ </td><td>0</td><td>0</td><td> $\cdots$ </td><td> $(\mu/m)-\epsilon$ </td></tr></table>

## Appendix C. Powerset Strategies in a CC Auction with Free Disposal

In the following, we describe an economy with powerset bidders and free disposal. We show that the CC auction leads to very high prices, thus reducing the bidders’ utility, even in cases where there is no competition. The example shows that the inefficiency in these situations can be almost as low as 50%.

Given the valuations in Table C.1 and an economy without free disposal, the bidders would all bid on a single item only, and the CC auction would stop after the first round at a price of the minimum bid increment . In an example, assume $m = n = 1 0 0 , \epsilon = 1 _ { \it { \cdot } }$ , and $\mu \geq 2 0 0$ . The allocation assigning bidder i item 4i5 is efficient and would maximize overall welfare. Bidder 1 would get a payoff of $\pi - 1 ,$ , and all other bidders achieve a payoff of $( \mu / 1 0 \dot { 0 } ) - 1$ With an auctioneer revenue of 100, the social welfare is $1 9 9 \pi / 1 0 0 .$ . If we assume m is the number of items, then the social welfare would be maximized at $( 2 m - 1 ) \mu / m .$

Now, with free disposal, bidder 1 would bid on all $2 ^ { ( m - 1 ) }$ packages that enfold the item 415 in each round until a price of $\mu / m$ is reached and he wins all items. His payoff would be 0 and the auctioneer would make a revenue of $\scriptstyle \mu ,$ which is inefficient. With $m \to \infty$ efficiency converges to 50%.

Appendix D. Auction Results of the Lab Experiments

<table><tr><td>Auction format</td><td>Auction number</td><td>Wave</td><td>Efficiency</td><td>Revenue</td><td>Rounds</td><td>Unsold items</td></tr><tr><td>CC</td><td>1</td><td>A</td><td>0.91</td><td>0.62</td><td>8</td><td>0</td></tr><tr><td>CC</td><td>2</td><td>A</td><td>1.00</td><td>0.44</td><td>6</td><td>0</td></tr><tr><td>CC</td><td>3</td><td>A</td><td>0.91</td><td>0.07</td><td>1</td><td>0</td></tr><tr><td>CC</td><td>4</td><td>A</td><td>0.99</td><td>0.51</td><td>7</td><td>0</td></tr><tr><td>CC</td><td>1</td><td>B</td><td>0.99</td><td>0.89</td><td>12</td><td>0</td></tr><tr><td>CC</td><td>2</td><td>B</td><td>0.70</td><td>0.07</td><td>1</td><td>1</td></tr><tr><td>CC</td><td>3</td><td>B</td><td>0.98</td><td>0.79</td><td>11</td><td>0</td></tr><tr><td>CC</td><td>4</td><td>B</td><td>0.86</td><td>0.20</td><td>3</td><td>1</td></tr><tr><td>CC</td><td>1</td><td>C</td><td>0.73</td><td>0.08</td><td>1</td><td>2</td></tr><tr><td>CC</td><td>2</td><td>C</td><td>0.91</td><td>0.37</td><td>5</td><td>0</td></tr><tr><td>CC</td><td>3</td><td>C</td><td>1.00</td><td>0.89</td><td>12</td><td>0</td></tr><tr><td>CC</td><td>4</td><td>C</td><td>0.88</td><td>0.27</td><td>4</td><td>1</td></tr><tr><td>CC</td><td>1</td><td>D</td><td>0.93</td><td>0.07</td><td>1</td><td>0</td></tr><tr><td>CC</td><td>2</td><td>D</td><td>0.79</td><td>0.14</td><td>2</td><td>1</td></tr><tr><td>CC</td><td>3</td><td>D</td><td>0.93</td><td>0.82</td><td>12</td><td>0</td></tr><tr><td>CC</td><td>4</td><td>D</td><td>0.88</td><td>0.15</td><td>2</td><td>1</td></tr><tr><td>CC+</td><td>1</td><td>A</td><td>0.99</td><td>0.78</td><td>13</td><td>0</td></tr><tr><td>CC+</td><td>2</td><td>A</td><td>1.00</td><td>0.71</td><td>16</td><td>0</td></tr><tr><td>CC+</td><td>3</td><td>A</td><td>1.00</td><td>0.79</td><td>17</td><td>0</td></tr><tr><td>CC+</td><td>4</td><td>A</td><td>0.99</td><td>0.80</td><td>16</td><td>0</td></tr><tr><td>CC+</td><td>1</td><td>B</td><td>0.99</td><td>0.30</td><td>14</td><td>0</td></tr><tr><td>CC+</td><td>2</td><td>B</td><td>0.97</td><td>0.73</td><td>12</td><td>0</td></tr><tr><td>CC+</td><td>3</td><td>B</td><td>0.95</td><td>0.66</td><td>13</td><td>1</td></tr><tr><td>CC+</td><td>4</td><td>B</td><td>0.99</td><td>0.54</td><td>13</td><td>0</td></tr><tr><td>CC+</td><td>1</td><td>C</td><td>1.00</td><td>0.90</td><td>13</td><td>0</td></tr><tr><td>CC+</td><td>2</td><td>C</td><td>0.97</td><td>0.78</td><td>17</td><td>0</td></tr><tr><td>CC+</td><td>3</td><td>C</td><td>0.97</td><td>0.78</td><td>13</td><td>0</td></tr><tr><td>CC+</td><td>4</td><td>C</td><td>0.90</td><td>0.57</td><td>12</td><td>0</td></tr><tr><td>CC+</td><td>1</td><td>D</td><td>0.99</td><td>0.47</td><td>15</td><td>0</td></tr><tr><td>CC+</td><td>2</td><td>D</td><td>0.95</td><td>0.66</td><td>16</td><td>0</td></tr><tr><td>CC+</td><td>3</td><td>D</td><td>1.00</td><td>0.80</td><td>15</td><td>0</td></tr><tr><td>CC+</td><td>4</td><td>D</td><td>0.98</td><td>0.55</td><td>13</td><td>0</td></tr></table>

## Appendix E. Further Computational Experiments

## E.1. Value Models

We also test a Transportation Large value model with 50 items and 30 bidders (Table E.1). The other characteristics are as described in §5.

The Airports value model is an implementation of the matching scenario from CATS (Table E.2). It models the four largest airports in the United States, each having a predefined number of departure and arrival time slots. For simplicity there is only one slot for each time unit and airport available. Each bidder is interested in obtaining one departure and one arrival slot (i.e., item) in two randomly selected airports. His valuation is proportional to the distance between the airports and reaches maximum when the arrival time matches a certain randomly selected value. The valuation is reduced if the arrival time deviates from this ideal value or if the time between departure and arrival slots is longer than necessary.

The Pairwise Synergy value model from An et al. (2005) is defined by a set of valuations of individual items v4k5 with $k \in \mathcal { K }$ and a matrix of pairwise item synergies $\{ s y n _ { k , l } \colon k ,$ $l \in \mathcal { K } , s y n _ { k , l } = s y n _ { l , k } , s y n _ { k , k } = 0 \}$ . The valuation of a package S is then calculated as

$$
v (S) = \sum_ {k = 1} ^ {| S |} v (k) + \frac {1}{| S | - 1} \sum_ {k = 1} ^ {| S |} \sum_ {l = k + 1} ^ {| S |} s y n _ {k, l} (v (k) + v (l)).
$$

A synergy value of 0 corresponds to completely independent items, and the synergy value of 1 means that the package valuation is twice as high as the sum of the individual item valuations. The model is very generic because it allows different types of synergistic valuations, but it was also used to model valuations in transportation auctions (An et al. 2005). We use the pairwise synergy value model with seven items; item valuations are drawn for each auction independently from a uniform distribution between 4 and 12. The synergy values are drawn from a uniform distribution between 1.5 and 2.0. The auctions with the pairwise synergy value model have five bidders each. We use a high synergy and low synergy setting (Tables E.3 and E.4).

Table E.1 Transportation Large with 50 Items and 30 Bidders (VCG Bidder Gain 37.25%)

<table><tr><td rowspan="2">Measure</td><td colspan="5">Bidder type</td></tr><tr><td>Straightforward</td><td>5 of 20</td><td>Powerset6</td><td>Powerset10</td><td>Powerset</td></tr><tr><td colspan="6">Mean efficiency in %</td></tr><tr><td>CC</td><td>98.48</td><td>97.94</td><td>98.04</td><td>97.86</td><td>98.07</td></tr><tr><td>CC+ (partial)</td><td>98.19</td><td>99.17</td><td>99.25</td><td>99.33</td><td>99.27</td></tr><tr><td>CC+ (full)</td><td>98.11</td><td>99.14</td><td>99.19</td><td>99.29</td><td>99.26</td></tr><tr><td>iBundle</td><td>100.00</td><td>86.95</td><td>94.22</td><td>94.74</td><td>95.89</td></tr><tr><td>Clock-proxy</td><td>99.83</td><td>99.56</td><td>99.72</td><td>99.72</td><td>99.64</td></tr><tr><td colspan="6">Min. efficiency in %</td></tr><tr><td>CC</td><td>90.74</td><td>85.00</td><td>85.00</td><td>85.00</td><td>85.00</td></tr><tr><td>CC+ (partial)</td><td>90.74</td><td>95.29</td><td>95.29</td><td>95.29</td><td>95.29</td></tr><tr><td>CC+ (full)</td><td>90.74</td><td>96.10</td><td>95.35</td><td>96.47</td><td>96.13</td></tr><tr><td>iBundle</td><td>100.00</td><td>69.62</td><td>76.03</td><td>76.40</td><td>84.24</td></tr><tr><td>Clock-proxy</td><td>97.69</td><td>95.18</td><td>96.47</td><td>96.47</td><td>95.18</td></tr><tr><td colspan="6">Mean rounds</td></tr><tr><td>CC</td><td>17.80</td><td>17.08</td><td>14.00</td><td>13.82</td><td>13.62</td></tr><tr><td>CC+ (partial)</td><td>16.90</td><td>14.90</td><td>14.86</td><td>14.60</td><td>14.40</td></tr><tr><td>CC+ (full)</td><td>21.48</td><td>18.14</td><td>18.14</td><td>18.00</td><td>17.88</td></tr><tr><td>iBundle</td><td>57.18</td><td>1,222.42</td><td>860.08</td><td>534.06</td><td>58.14</td></tr><tr><td>Clock-proxy*</td><td>13.68</td><td>11.66</td><td>11.78</td><td>11.78</td><td>11.52</td></tr><tr><td>Mean no. of bids</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CC</td><td>234.04</td><td>376.20</td><td>406.68</td><td>496.66</td><td>1,201.30</td></tr><tr><td>CC+ (partial)</td><td>226.76</td><td>375.90</td><td>407.26</td><td>496.76</td><td>1,201.30</td></tr><tr><td>CC+ (full)</td><td>227.40</td><td>373.66</td><td>404.74</td><td>494.50</td><td>1,199.88</td></tr><tr><td>iBundle</td><td>34,968.16</td><td>35,673.06</td><td>31,686.36</td><td>30,947.04</td><td>25,136.04</td></tr><tr><td>Mean revenue in %</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CC</td><td>83.80</td><td>89.11</td><td>89.27</td><td>89.21</td><td>89.32</td></tr><tr><td>CC+ (partial, day)</td><td>67.62</td><td>69.97</td><td>69.95</td><td>70.28</td><td>70.39</td></tr><tr><td>CC+ (full, day)</td><td>67.81</td><td>69.43</td><td>69.34</td><td>69.76</td><td>69.82</td></tr><tr><td>CC+ (partial, VCG)</td><td>56.30</td><td>60.70</td><td>60.95</td><td>61.54</td><td>61.68</td></tr><tr><td>CC+ (full, VCG)</td><td>54.67</td><td>57.78</td><td>58.33</td><td>58.69</td><td>58.72</td></tr><tr><td>iBundle</td><td>76.92</td><td>64.32</td><td>64.91</td><td>65.43</td><td>66.99</td></tr><tr><td>Clock-proxy</td><td>75.11</td><td>74.73</td><td>74.94</td><td>74.94</td><td>73.94</td></tr></table>

<sup>∗</sup>Clock phase only.

In the Real Estate and Pairwise Synergy value models, bidders are interested in a maximum package size of 3 because in these value models large packages are always valued more highly than are small ones. This is also motivated by real-world observations (An et al. 2005) in which bidders typically have an upper limit on the number of items they are interested in. Without this limitation, the auction easily degenerates into a scenario with a single winner for the package containing all items.

## E.2. Experimental Results

Table E.2 Airports with 84 Items and 40 Bidders (VCG Bidder Gain 57.76%)

<table><tr><td rowspan="2">Measure</td><td colspan="5">Bidder type</td></tr><tr><td>Straightforward</td><td>5 of 20</td><td>Powerset6</td><td>Powerset10</td><td>Powerset</td></tr><tr><td>Mean efficiency in %</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CC</td><td>98.62</td><td>97.18</td><td>97.23</td><td>97.10</td><td>97.17</td></tr><tr><td>CC+ (partial)</td><td>98.60</td><td>98.74</td><td>98.71</td><td>98.71</td><td>98.71</td></tr><tr><td>CC+ (full)</td><td>98.74</td><td>98.75</td><td>98.62</td><td>98.76</td><td>98.73</td></tr><tr><td>iBundle</td><td>100.00</td><td>95.50</td><td>98.93</td><td>98.13</td><td>97.87</td></tr><tr><td>Clock-proxy</td><td>99.77</td><td>99.72</td><td>99.66</td><td>99.66</td><td>99.64</td></tr><tr><td>Min. efficiency in %</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CC</td><td>95.39</td><td>92.63</td><td>93.42</td><td>93.57</td><td>93.73</td></tr><tr><td>CC+ (partial)</td><td>95.04</td><td>96.57</td><td>96.57</td><td>97.06</td><td>96.86</td></tr><tr><td>CC+ (full)</td><td>96.10</td><td>97.06</td><td>95.74</td><td>97.06</td><td>96.86</td></tr><tr><td>iBundle</td><td>100.00</td><td>88.50</td><td>96.57</td><td>93.00</td><td>92.55</td></tr><tr><td>Clock-proxy</td><td>97.92</td><td>98.96</td><td>98.60</td><td>98.60</td><td>98.60</td></tr><tr><td>Mean rounds</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CC</td><td>10.94</td><td>8.48</td><td>8.28</td><td>8.20</td><td>8.20</td></tr><tr><td>CC+ (partial)</td><td>13.58</td><td>11.80</td><td>11.40</td><td>11.28</td><td>11.36</td></tr><tr><td>CC+ (full)</td><td>17.82</td><td>11.86</td><td>11.48</td><td>11.46</td><td>11.42</td></tr><tr><td>iBundle</td><td>27.30</td><td>48.98</td><td>41.58</td><td>33.82</td><td>33.68</td></tr><tr><td>Clock-proxy*</td><td>10.06</td><td>8.78</td><td>8.18</td><td>8.18</td><td>8.02</td></tr><tr><td>Mean no. of bids</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CC</td><td>472.72</td><td>721.44</td><td>786.74</td><td>957.68</td><td>993.40</td></tr><tr><td>CC+ (partial)</td><td>511.22</td><td>758.20</td><td>819.98</td><td>989.44</td><td>1,025.66</td></tr><tr><td>CC+ (full)</td><td>527.80</td><td>734.16</td><td>798.52</td><td>969.44</td><td>1,004.22</td></tr><tr><td>iBundle</td><td>6,364.38</td><td>6,262.72</td><td>5,522.90</td><td>6,364.66</td><td>7,095.52</td></tr><tr><td>Mean revenue in %</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CC</td><td>82.75</td><td>91.30</td><td>91.33</td><td>91.67</td><td>91.75</td></tr><tr><td>CC+ (partial, core)</td><td>41.02</td><td>44.45</td><td>43.91</td><td>44.24</td><td>44.09</td></tr><tr><td>CC+ (full, core)</td><td>41.43</td><td>43.31</td><td>42.90</td><td>43.36</td><td>43.13</td></tr><tr><td>CC+ (partial, VCG)</td><td>35.17</td><td>38.61</td><td>38.54</td><td>38.91</td><td>38.64</td></tr><tr><td>CC+ (full, VCG)</td><td>36.35</td><td>38.04</td><td>38.08</td><td>38.54</td><td>38.38</td></tr><tr><td>iBundle</td><td>49.02</td><td>48.51</td><td>47.88</td><td>46.74</td><td>47.25</td></tr><tr><td>Clock-proxy</td><td>46.10</td><td>46.98</td><td>46.40</td><td>46.40</td><td>46.34</td></tr></table>

<sup>∗</sup>Clock phase only.

Table E.3 Pairwise Synergy High with 7 Items and 5 Bidders (VCG Bidder Gain 12.97%)

<table><tr><td rowspan="2">Measure</td><td colspan="5">Bidder type</td></tr><tr><td>Straightforward</td><td>5 of 20</td><td>Powerset6</td><td>Powerset10</td><td>Powerset</td></tr><tr><td>Mean efficiency in %</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CC</td><td>99.16</td><td>99.06</td><td>99.15</td><td>99.02</td><td>99.29</td></tr><tr><td>CC+ (partial)</td><td>99.09</td><td>99.83</td><td>99.72</td><td>99.74</td><td>100.00</td></tr><tr><td>CC+ (full)</td><td>99.26</td><td>99.83</td><td>99.72</td><td>99.74</td><td>100.00</td></tr><tr><td>iBundle</td><td>100.00</td><td>97.93</td><td>99.33</td><td>99.14</td><td>39.52</td></tr><tr><td>Clock-proxy</td><td>99.95</td><td>99.86</td><td>99.77</td><td>99.77</td><td>100.00</td></tr><tr><td>Min. efficiency in %</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CC</td><td>86.52</td><td>94.22</td><td>96.32</td><td>94.22</td><td>94.22</td></tr><tr><td>CC+ (partial)</td><td>86.52</td><td>97.79</td><td>97.20</td><td>96.22</td><td>99.95</td></tr><tr><td>CC+ (full)</td><td>94.53</td><td>97.79</td><td>97.20</td><td>96.22</td><td>100.00</td></tr><tr><td>iBundle</td><td>100.00</td><td>94.19</td><td>94.99</td><td>93.36</td><td>10.90</td></tr><tr><td>Clock-proxy</td><td>97.94</td><td>97.79</td><td>96.66</td><td>96.66</td><td>99.95</td></tr><tr><td>Mean rounds</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CC</td><td>323.66</td><td>321.60</td><td>325.50</td><td>322.94</td><td>321.84</td></tr><tr><td>CC+ (partial)</td><td>336.72</td><td>353.24</td><td>356.12</td><td>352.24</td><td>352.00</td></tr><tr><td>CC+ (full)</td><td>367.12</td><td>355.56</td><td>358.74</td><td>355.44</td><td>354.52</td></tr><tr><td>iBundle</td><td>1,596.30</td><td>13,220.48</td><td>11,009.38</td><td>6,821.48</td><td>1.00</td></tr><tr><td>Clock-proxy*</td><td>311.16</td><td>320.60</td><td>321.50</td><td>321.50</td><td>321.16</td></tr><tr><td>Mean no. of bids</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CC</td><td>2,068.46</td><td>6,976.56</td><td>8,337.60</td><td>13,368.04</td><td>63,268.94</td></tr><tr><td>CC+ (partial)</td><td>2,106.56</td><td>7,074.98</td><td>8,440.68</td><td>13,468.12</td><td>63,377.04</td></tr><tr><td>CC+ (full)</td><td>2,165.84</td><td>7,069.80</td><td>8,429.24</td><td>13,463.68</td><td>63,371.72</td></tr><tr><td>iBundle</td><td>332,557.40</td><td>311,450.98</td><td>287,116.04</td><td>303,880.26</td><td>315.00</td></tr><tr><td>Mean revenue in %</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CC</td><td>89.76</td><td>97.01</td><td>96.84</td><td>97.20</td><td>97.46</td></tr><tr><td>CC+ (partial, core)</td><td>73.42</td><td>87.68</td><td>83.20</td><td>86.81</td><td>88.53</td></tr><tr><td>CC+ (full, core)</td><td>72.87</td><td>87.06</td><td>82.54</td><td>86.13</td><td>87.95</td></tr><tr><td>CC+ (partial, VCG)</td><td>69.93</td><td>86.87</td><td>81.42</td><td>85.71</td><td>87.85</td></tr><tr><td>CC+ (full, VCG)</td><td>69.33</td><td>85.95</td><td>80.39</td><td>84.71</td><td>86.96</td></tr><tr><td>iBundle</td><td>88.07</td><td>86.20</td><td>85.90</td><td>87.08</td><td>0.00</td></tr><tr><td>Clock-proxy</td><td>83.91</td><td>87.14</td><td>86.38</td><td>86.38</td><td>87.96</td></tr></table>

<sup>∗</sup>Clock phase only.

Table E.4 Pairwise Synergy Low with 7 Items and 5 Bidders (VCG Bidder Gain 13.43%)

<table><tr><td rowspan="2">Measure</td><td colspan="5">Bidder type</td></tr><tr><td>Straightforward</td><td>5 of 20</td><td>Powerset6</td><td>Powerset10</td><td>Powerset</td></tr><tr><td colspan="6">Mean efficiency in %</td></tr><tr><td>CC</td><td>98.22</td><td>98.80</td><td>98.44</td><td>98.98</td><td>99.16</td></tr><tr><td>CC+ (partial)</td><td>97.80</td><td>99.76</td><td>98.96</td><td>99.56</td><td>100.00</td></tr><tr><td>CC+ (full)</td><td>97.76</td><td>99.77</td><td>98.96</td><td>99.56</td><td>100.00</td></tr><tr><td>iBundle</td><td>100.00</td><td>97.66</td><td>98.78</td><td>99.28</td><td>52.88</td></tr><tr><td>Clock-proxy</td><td>99.80</td><td>99.79</td><td>99.56</td><td>99.56</td><td>100.00</td></tr><tr><td colspan="6">Min. efficiency in %</td></tr><tr><td>CC</td><td>88.28</td><td>93.18</td><td>91.81</td><td>93.18</td><td>93.18</td></tr><tr><td>CC+ (partial)</td><td>88.28</td><td>96.61</td><td>91.81</td><td>96.26</td><td>99.95</td></tr><tr><td>CC+ (full)</td><td>88.28</td><td>96.61</td><td>91.81</td><td>96.26</td><td>99.95</td></tr><tr><td>iBundle</td><td>100.00</td><td>93.36</td><td>92.76</td><td>95.63</td><td>22.32</td></tr><tr><td>Clock-proxy</td><td>96.31</td><td>96.61</td><td>96.26</td><td>96.26</td><td>99.96</td></tr><tr><td colspan="6">Mean rounds</td></tr><tr><td>CC</td><td>368.54</td><td>349.38</td><td>351.72</td><td>350.40</td><td>348.78</td></tr><tr><td>CC+ (partial)</td><td>395.12</td><td>388.88</td><td>386.72</td><td>386.70</td><td>384.04</td></tr><tr><td>CC+ (full)</td><td>418.10</td><td>390.20</td><td>390.98</td><td>389.58</td><td>388.76</td></tr><tr><td>iBundle</td><td>1,694.72</td><td>13,613.30</td><td>11,696.20</td><td>6,971.54</td><td>1.00</td></tr><tr><td>Clock-proxy*</td><td>345.78</td><td>347.70</td><td>348.52</td><td>348.52</td><td>347.48</td></tr><tr><td>Mean no. of bids</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CC</td><td>2,295.56</td><td>7,401.86</td><td>8,800.06</td><td>14,070.80</td><td>68,422.96</td></tr><tr><td>CC+ (partial)</td><td>2,381.44</td><td>7,519.58</td><td>8,919.26</td><td>14,186.08</td><td>68,541.52</td></tr><tr><td>CC+ (full)</td><td>2,392.08</td><td>7,504.12</td><td>8,903.12</td><td>14,176.12</td><td>68,533.64</td></tr><tr><td>iBundle</td><td>358,160.68</td><td>325,568.06</td><td>304,894.88</td><td>312,606.56</td><td>315.00</td></tr><tr><td>Mean revenue in %</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CC</td><td>88.38</td><td>96.85</td><td>95.84</td><td>96.89</td><td>97.23</td></tr><tr><td>CC+ (partial, core)</td><td>73.14</td><td>87.11</td><td>83.27</td><td>86.70</td><td>88.26</td></tr><tr><td>CC+ (full, core)</td><td>73.29</td><td>86.42</td><td>82.34</td><td>85.81</td><td>87.44</td></tr><tr><td>CC+ (partial, VCG)</td><td>69.57</td><td>86.29</td><td>81.85</td><td>85.65</td><td>87.69</td></tr><tr><td>CC+ (full, VCG)</td><td>68.53</td><td>85.16</td><td>80.20</td><td>84.30</td><td>86.55</td></tr><tr><td>iBundle</td><td>87.54</td><td>83.86</td><td>85.09</td><td>85.04</td><td>0.00</td></tr><tr><td>Clock-proxy</td><td>83.12</td><td>86.37</td><td>85.89</td><td>85.89</td><td>87.44</td></tr></table>

<sup>∗</sup>Clock phase only.

## References

Adomavicius G, Gupta A (2005) Toward comprehensive real-time bidder support in iterative combinatorial auctions. Inform. Systems Res. 16(2):169–185.

An N, Elmaghraby W, Keskinocak P (2005) Bidding strategies and their impact on revenues in combinatorial auctions. J. Revenue Pricing Management 3(4):337–357.

Arrow KJ, Debreu G (1954) Existence of an equilibrium for competitive economy. Econometrica 22(3):265–290.

Ausubel L, Milgrom P (2002) Ascending auctions with package bidding. Frontiers of Theoretical Econom. 1(1):1–42.

Ausubel L, Milgrom P (2006a) Ascending proxy auctions. Cramton P, Shoham Y, Steinberg R, eds. Combinatorial Auctions (MIT Press, Cambridge, MA), 79–98.

Ausubel L, Milgrom P (2006b) The lovely but lonely Vickrey auction. Cramton P, Shoham Y, Steinberg R, eds. Combinatorial Auctions (MIT Press, Cambridge, MA), 17–40.

Ausubel L, Cramton P, Milgrom P (2006) The clock-proxy auction: A practical combinatorial auction design. Cramton P, Shoham Y, Steinberg R, eds. Combinatorial Auctions (MIT Press, Cambridge, MA), 115–138.

Bapna R, Das S, Garfinkel R, Stallaert J (2007) A market design for grid computing. INFORMS J. Comput. 20(1):100–111.

Bichler M, Gupta A, Ketter W (2010) Designing smart markets. Inform. Systems Res. 21(4):688–699.

Bichler M, Shabalin P, Pikovsky A (2009) A computational analysis of linear-price iterative combinatorial auctions. Inform. Systems Res. 20(1):33–59.

Bichler M, Davenport A, Hohner G, Kalagnanam J (2006) Industrial procurement auctions. Cramton P, Shoham Y, Steinberg R, eds. Combinatorial Auctions (MIT Press), 593–612.

Bikhchandani S, Mamer JW (1997) Competitive equilibrium in an exchange economy with indivisibilities. J. Econom. Theory 74(2):385–413.

Bikhchandani S, Ostroy JM (2002) The package assignment model. J. Econom. Theory 107(2):377–406.

Blumrosen L, Nisan N (2007) Combinatorial auctions. Nisan N, Roughgarden T, Tardos E, Vazirani V, eds. Algorithm Game Theory (Cambridge University Press, New York), 267–300.

Brunner C, Goeree JK, Holt Ch, Ledyard J (2010) An experimental test of flexible combinatorial spectrum auction formats. Amer. Econom. J.: Micro-Econom. 2(1):39–57.

Caplice Y, Sheffi C (2006) Combinatorial auctions for truckload transportation. Cramton P, Shoham Y, Steinberg R, eds. Combinatorial Auctions (MIT Press, Cambridge, MA), 539–572.

Conen W, Sandholm T (2001) Preference elicitation in combinatorial auctions. ACM Conf. Electronic Commerce, Tampa, FL (ACM, New York), 256–259.

Conitzer V, Sandholm T (2002) Vote elicitation: Complexity and strategy-proofness. Proc. 18th Nat. Conf. Artificial Intelligence (AAAI, Menlo Park, CA), 392–397.

Cramton P (2009) Auctioning the Digital Dividend (Karlsruhe Institute of Technology, Germany).

Cramton P, Shoham Y, Steinberg R, eds. (2006a) Combinatorial Auctions (MIT Press, Cambridge, MA).

Cramton P, Shoham Y, Steinberg R (2006b) Introduction to combinatorial auctions. Cramton P, Shoham Y, Steinberg R, eds. Combinatorial Auctions (MIT Press, Cambridge, MA), 1–14.

Day R, Milgrom P (2007) Core-selecting package auctions. Internat. J. Game Theory 36(3–4):393–407.

Day R, Raghavan S (2007) Fair payments for efficient allocations in public sector combinatorial auctions. Management Sci. 53(9):1389–1406.

de Vries S, Schummer J, Vohra R (2007) On ascending Vickrey auctions for heterogeneous objects. J. Econom. Theory 132(1):95–118.

Demange G, Gale D, Sotomayor M (1986) Multi-item auctions. J. Political Econom. 94(4):863–872.

Gallien J, Wein L (2005) A smart market for industrial procurement with capacity constraints. Management Sci. 51(1):76–91.

Georgescu-Roegen N (1979) Methods in economic science. J. Econom. Issues 13(2):317–328.

Goeree J, Holt C (2010) Hierarchical package bidding: A paper and pencil combinatorial auction. Games Econom. Behav. 70(1):146–169.

Green J, Laffont J-J (1977) Characterization of satisfactory mechanisms for the revelation of preferences for public goods. Econometrica 45(2):427–438.

Green J, Laffont J (1979) Incentives in Public Decision Making (North-Holland, Amsterdam).

Gul F, Stacchetti E (1999) Walrasian equilibrium with gross substitutes. J. Econom. Theory 87(1):95–124.

Gul F, Stacchetti E (2000) The English auction with differentiated commodities. J. Econom. Theory 92(1):66–95.

Guo Z, Koehler GJ, Whinston AB (2007) A market-based optimization algorithm for distributed systems. Management Sci. 53(8):1345–1358.

Hollander M, Wolfe DA (1973) Nonparametric Statistical Inference (John Wiley & Sons, New York).

Holmstrom B (1979) Groves’ scheme on restricted domains. Econometrica 47(5):1137–1144.

Hurwicz L (1977) On the dimensional requirements of informationally decentralized pareto-satisfactory processes. Arrow KJ, Hurwicz L, eds. Studies in Resource Allocation Processes (Cambridge University Press, New York), 413–467.

Isaac M, Salmon T, Zillante A (2007) A theory of jump bidding in ascending auctions. J. Econom. Behav. Organ. 62(1):144–164.

Jordan JS (1982) The competitive allocation process is informationally efficient uniquely. J. Econom. Theory 28(1):1–18.

Kagel J, Lien Y, Milgrom P (2010) Ascending prices and package bids: An experimental analysis. Amer. Econom. J.: Microeconomics 2(3):160–185.

Kelso AS, Crawford VP (1982) Job matching, coalition formation, and gross substitute. Econometrica 50(6):1483–1504.

Leyton-Brown K, Pearson M, Shoham Y (2000) Towards a universal test suite for combinatorial auction algorithms. ACM Conf. Electronic Commerce (ACM, New York), 66–76.

McCabe K, Rassenti S, Smith V (1991) Smart computer-assisted markets. Science 254(5031):534–538.

Meeus L, Verhaegen K, Belmans R (2009) Block order restrictions in combinatorial electric energy auctions. Eur. J. Oper. Res. 196(3):1202–1206.

Milgrom PR, Weber RJ (1982) A theory of auctions and competitive bidding. Econometrica 50(5):1089–1122.

Mishra D, Parkes D (2007) Ascending price Vickrey auctions for general valuations. J. Econom. Theory 132(1):335–366.

Mount K, Reiter S (1974) The informational size of message spaces. J. Econom. Theory 8(2):161–192.

Nisan N (2007) Introduction to mechanism design (for computer scientists). Nisan N, Roughgarden T, Tardos E, Vazirani V, eds. Algorithm Game Theory (Cambridge University Press, New York), 209–242.

Nisan N, Segal I (2006) The communcation requirements of efficient allocations and supporting prices. J. Econom. Theory 129(1):192–224.

Parkes D (2006) Iterative combinatorial auctions. Cramton P, Shoham Y, Steinberg R, eds. Combinatorial Auctions (MIT Press, Cambridge, MA), 41–78.

Parkes D, Ungar LH (2000) Iterative combinatorial auctions: Theory and practice. Proc. 17th Nat. Conf. Artificial Intelligence (AAAI, Menlo Park, CA), 74–81.

Porter D, Rassenti S, Roopnarine A, Smith V (2003) Combinatorial auction design. Proc. National Academy Sci. 100(19):11153–11157.

Rothkopf MH (2007) Thirteen reasons why the Vickrey-Clarke-Groves process is not practical. Oper. Res. 55(2):191–197.

Sandholm LD, Martyn CM, Hughes P, Jacobs JR, Begg TD (2006) Changing the game in strategic sourcing at Proctor and Gamble: Expressive competition enabled by optimization. Interfaces 36(1):55–68.

Scheffel T, Pikovsky A, Bichler M, Guler K (2011) An experimental comparison of linear and non-linear price combinatorial auctions. Inform. Systems Res. 22(2):346–368.

Schneider S, Shabalin P, Bichler M (2010) On the robustness of nonlinear personalized price combinatorial auctions. Eur. J. Oper. Res. 206(1):248–259.

Xia M, Koehler GJ, Whinston AB (2004) Pricing combinatorial auctions. Eur. J. Oper. Res. 154(1):251–270.
