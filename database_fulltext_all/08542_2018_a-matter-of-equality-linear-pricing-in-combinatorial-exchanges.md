---
otero_id: 8542
otero_key: "GVY7EETH"
title: "A Matter of Equality: Linear Pricing in Combinatorial Exchanges"
authors: "Martin Bichler; Vladimir Fux; Jacob Goeree"
year: "2018"
journal: "Information Systems Research"
doi: "10.1287/isre.2017.0766"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [130.63.180.147] On: 19 December 2018, At: 16:24 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

![](/api/attachments/GVY7EETH/fulltext/images/13d4a0014c469f6791c532d0e88e808312d084d4f6835f687833cacb27de6e41.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# A Matter of Equality: Linear Pricing in Combinatorial Exchanges

Martin Bichler, Vladimir Fux, Jacob Goeree

To cite this article: Martin Bichler, Vladimir Fux, Jacob Goeree (2018) A Matter of Equality: Linear Pricing in Combinatorial Exchanges. Information Systems Research

Published online in Articles in Advance 19 Dec 2018

https://doi.org/10.1287/isre.2017.0766

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2018, INFORMS

Please scroll down for article—it is on subsequent pages

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics. For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# A Matter of Equality: Linear Pricing in Combinatorial Exchanges

Martin Bichler,<sup>a</sup> Vladimir Fux,<sup>a</sup> Jacob Goeree<sup>b</sup>

<sup>a</sup> Department of Informatics, Technical University of Munich, 80333 Munich, Germany; <sup>b</sup> Department of Economics, University of New South Wales, Kensington, New South Wales 2052, Australia

Contact: bichler@in.tum.de, http://orcid.org/0000-0001-5491-2935 (MB)

Received: June 13, 2016 Revised: November 29, 2016; July 25, 2017; October 30, 2017 Accepted: November 2, 2017 Published Online in Articles in Advance: December 19, 2018

https://doi.org/10.1287/isre.2017.0766

Copyright: © 2018 INFORMS

Abstract. Combinatorial exchanges that allow for package ofers to address nonconvexities in demand or supply typically employ linear and anonymous prices because they are simple, tractable, and fair. Despite their prevalence, linear anonymous prices do not necessarily correspond to Walrasian competitive equilibrium prices in such settings, and their impact is not well understood. This paper is the first to analyze the efect of diferent pricing rules on the eficiency of combinatorial exchanges, using both analytic methods and numerical experiments. Our analysis is motivated by a combinatorial fishery-rights exchange designed to reform the fishing industry in New South Wales (NSW), Australia. We find that when linearity and anonymity are required for only one side of the market, the average eficiency loss is negligible. In contrast, with a single linear price vector for both sides, the eficiency loss is substantial, especially when the market is small. In a formal model, we show that eficiency losses decrease when the number of buyers grows or the size of the submitted packages decreases. Besides the reform of the NSW fishing industry, our results have important implications for other cap-and-trade programs as well as other industries where demand or cost complementarities play a role.

History: Giri Kumar Taji, Senior Editor; Sanjukta Smith, Associate Editor.

Funding: Financial support from the Technical University of Munich Institute of Advanced Study and the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) [Grant 391769402] is gratefully acknowledged.

Keywords: combinatorial exchange • payment rules • market design

## 1. Introduction

This paper is motivated by the design of a combinatorial exchange to facilitate the reform of the fishing industry in New South Wales (NSW), Australia. This reform is needed because the NSW fishing industry sufers from overfishing that jeopardizes its long-run commercial viability. The industry is characterized by the familiar 80–20 rule, that is, fewer than 20% of the fishing businesses do more than 80% of the catching. Furthermore, there are no measures to prevent overfishing: anyone with a business license is allowed to catch any amount and type of fish.

To ensure ecological sustainability and improve the industry’s profitability, the NSW government decided to link (efort to) catch to fishery access rights, or “shares.” Some 20 years ago, these shares were distributed evenly among more than 1,100 commercial fishers, but they were never efectuated, that is, all that was needed to fish was a business license. Under the government’s recent “linkage program,” however, shares have become binding and are directly tied to possible catch (eforts). There are over a hundred different share classes describing diferent types of access rights across several regions. A share class may determine a permission to catch certain types and quantities of fish, or stipulate allowed eforts (e.g., maximum number of days of fishing per week, or the number of hooks per line, the number of nets, etc.).

A consequence of the linkage program is that the top 20% most active fishers face an immediate deficit of shares. They were originally given the same number of shares as other fishers but need far more to accommodate their high volumes of catch. To cover their deficits, active fishers will need to purchase shares from less active fishers who, in some cases, will wish to sell their entire business and leave the industry. The question is how to best accomplish this transfer of shares, taking into account institutional details and constraints.

Decentralized bargaining would certainly not work. Fishers are geographically dispersed across the state, making it very costly to find all eficient buyer–seller matches. Moreover, exiting fishers would have to sell their shares separately, exposing them to the risk that they sell some, but not all, of their shares. This exposure problem may cause exiting fishers to be left with a fragmented portfolio of shares and little proceeds. Finally, regulation requires those fishers that remain in the industry to hold a minimum number of shares in a given share class, which creates additional exposure problems: if fishers purchase additional shares but are unable to meet the threshold, then their investments are lost.

This paper analyzes centralized exchanges designed to overcome these problems. In practice, centralization can be accomplished by running an electronic market over the Internet, thus minimizing participation costs. The market format, however, has to be nonstandard in that it should allow for combinatorial buy and sell ofers. A fisher wishing to exit the industry should be able to specify an “all-or-nothing” sell ofer that includes all the shares he holds (typically involving several share classes) at a single total price. Likewise, a fisher wishing to buy additional shares should be able to specify the minimum and maximum quantities he would accept at the per-unit price he specifies.<sup>1</sup>

While a combinatorial exchange avoids exposure problems, it introduces several design complexities. One issue is computational tractability: in a combinatorial exchange, the winner-determination problem is a generalization of the combinatorial allocation problem, which is NP-complete.<sup>2</sup> In addition, there are the usual desiderata that apply to combinatorial and noncombinatorial markets alike, that is, incentive-compatibility, individual rationality, eficiency, and budget balance.<sup>3</sup> Finally, there is the question of how and what to price in a combinatorial exchange: Should items and packages be priced separately? Can prices be discriminatory, or should prices be linear and anonymous as in standard markets? We next discuss how we addressed these issues and what questions remain.

Because of computational complexities, the exchanges we analyze are not run in continuous time, but instead have a “call” structure. This means that participants can submit ofers until a preannounced time when the market clears. There could be a single call or several; for example, the exchange could be repeated for a fixed number of rounds where after each round, the market clears to determine provisional allocations and prices, which become final after the last round.

A seminal contribution by Myerson and Satterthwaite (1983) shows there exists no incentive-compatible and individually-rational mechanism that is fully eficient and budget balanced. The well-known Vickrey– Clarke–Groves (VCG) mechanism, for instance, is fully eficient, individually rational, and (dominant-strategy) incentive compatible (Green and Lafont 1977), but it is not budget balanced, and its deficit can be substantial. In contrast, the exchanges we explore are budget balanced, individually rational, and incentive compatible, but not necessarily fully eficient. One possible source of ineficiency stems from the use of linear and anonymous prices, that is, share prices are the same for all buyers and sellers, and the price of a package is simply the sum of prices of the shares it contains. The reason for using linear prices is that they are intuitive and tractable. (With over a hundred diferent share classes there would be over 2<sup>100</sup> diferent prices in the market if packages were priced separately.) The reason for using anonymous prices is that they are “fair.” Especially in the context of the fisheries share market, it would cause political stir if fishers learned they paid more (received less) than a rival for the shares they bought (sold).

The possibility that linear anonymous prices may cause ineficiencies in combinatorial exchanges contrasts with well-known results for standard markets. Arrow and Debreu (1954) and McKenzie (1959) show that when preferences are convex and goods are divisible, there exist linear and anonymous prices that “clear the market” for every commodity in the economy. In other words, when buyers and sellers maximize their utility at those prices, the resulting aggregate demand will equal the aggregate supply. Such market-clearing prices are known as Walrasian competitive-equilibrium prices, and the first welfare theorem implies that the associated allocation is eficient (Arrow and Debreu 1954). Unfortunately, it is not always possible to find Walrasian prices to support the eficient allocation when there are nonconvexities in supply or demand (as is the case in the fishery application).<sup>4</sup>

Suppose, for instance, that a single seller ofers a package of three shares at a total price of \$9. Buyer 1 wants two shares and ofers to pay \$8, while buyer 2 wants one share and ofers \$2. Collectively, the buyers value the three shares more than the seller. However, supply is three at any price above \$3, while demand is three for prices lower than \$2 and demand is two for prices between \$2 and \$4. There is no Walrasian equilibrium price that clears the market and supports the eficient allocation.<sup>5</sup>

Besides eficiency losses, linear anonymous prices may also cause some ofers to be “paradoxically rejected.” Suppose, for instance, that a single seller ofers two items at a per-unit price of \$1. Buyer 1 wants two items and ofers to pay \$5, while buyer 2 wants one item and ofers \$3. Supply is two at any price above \$1, while demand is three for prices between \$1 and \$2.50, and demand is one for prices between \$2.50 and \$3. An exchange that maximizes total surplus, that is, the total gains from trade, will assign two units to buyer 1 at a price of, say, \$1.75. But this means that buyer 2’s ofer is paradoxically rejected.

This paper provides a thorough analysis of the impact of linear anonymous prices in combinatorial exchanges. We introduce alternative ways to compute linear anonymous prices in a combinatorial exchange for fishery access rights. We discuss important elements of the bid language, alternative optimization formulations, and diferent ways to compute linear prices for one or both sides of the market. Our key question is about the eficiency loss that can be attributed to linear prices. In other words, which percentage of the overall gains from trade in the welfare-maximizing allocation is lost due to the use of linear and anonymous prices?

This question is central in all applications of combinatorial exchanges, for example, day-ahead energy markets, but it has received little attention so far.

First, we show that the welfare loss due to linear anonymous prices can be 100% in the worst case. Second, we discuss a stochastic model related to the worstcase result, which shows that the welfare loss goes to zero with an increasing numbers of bidders and low package size. Finally, we provide the results of numerical experiments based on field data, which helps to estimate welfare losses due to linear anonymous pricing under realistic assumptions.

We also show that the bid language and the pricing rule interact in important ways, which is interesting beyond the exchange of fishery access rights. For example, it is beneficial for the eficiency of a combinatorial exchange to have a weak demand–supply constraint such that a package can be traded, even if there is no buyer for every object in that package, as long as there are positive gains from trade. Excess shares would be deleted by the government in our example. However, with a single linear price vector, the requirement of a balanced budget implies a strict demand–supply constraint unless the price of a share class is zero, with a substantial negative efect on the welfare gains in the market. Only if prices are zero can the government delete excess shares at zero cost.

The bid language is important for eficiency. A flexible bid language, as it is described in this paper for buyers, reduces the number of bids a buyer has to specify and makes it much easier to match supply and demand in cases when there are gains from trade.

In the next section, we provide an overview of the relevant literature. Section 3 introduces the bidding language and winner-determination problem. In Section 4, we analyze diferent linear and anonymous payment rules. Section 5 provides the results of numerical experiments with a focus on welfare losses and computation time. Section 6 concludes.

## 2. Related Literature and Related Applications

The research reported in this paper belongs to the area of market design, an emerging interdisciplinary field that studies what makes institutions work and how to fix them if they do not. Market design has had some marked successes, for example, improving the matching of interns to hospitals, students to schools, and organ donors to patients—work that was awarded the Nobel Prize in Economic Sciences in 2012.

Besides matching institutions, market design has influenced the design of one-sided combinatorial markets—also known as combinatorial auctions. Such auctions are used in a variety of applications (Cramton et al. 2006), including the sales of highly valuable spectrum for wireless and mobile-phone applications.<sup>6</sup> Information systems has made substantial contributions to this literature, in particular the design of bid languages and appropriate pricing rules for combinatorial auctions (Xia et al. 2004, Schefel et al. 2011, Adomavicius and Gupta 2005, Cason et al. 2011, Ketter et al. 2012, Adomavicius et al. 2012, Petrakis et al. 2013).

However, most of the literature is focused on auctions (i.e., one-sided markets). The few papers that address the design of combinatorial exchanges mostly focus on VCG-type mechanisms and their problems (e.g., the lack of budget balance or the violation of core constraints).<sup>7</sup> Combinatorial exchanges with linear anonymous prices have largely been ignored despite advances in algorithms and computing power that allow running large-scale two-sided markets over the Internet.<sup>8</sup>

The NSW market for fishery access rights is a prominent example of a combinatorial exchange with substantial industry impact. Besides its importance for the reform of the NSW fishing industry, the exchange can potentially be applied in other Australian states or elsewhere in the world. Furthermore, it can be adapted for other cap-and-trade systems such as pollution rights. More broadly, our results generalize to other markets where synergistic values or cost nonconvexities play a role, for example, energy markets and financial markets. While the bid languages used across these various applications may difer, the key results of this paper regarding the impact of linear anonymous prices on the eficiency of combinatorial exchanges generalize.

Electricity production, for instance, exhibits substantial cost nonconvexities due to start-up costs and the minimum power output of power plants. Nonconvexities are also present on the demand side, as buyers are typically interested in purchasing a certain quantity of electricity for several consecutive hours. This is why day-ahead energy markets allow for so called “block bids” that demand multiple units of singlehour supply. While allowing for package demands, day-ahead markets typically use linear anonymous prices even though Walrasian prices cannot necessarily be attained and bids may be “paradoxically” rejected (Meeus et al. 2009, Van Vyve et al. 2011). Similar considerations apply to markets for transportation and logistics<sup>9</sup> (Wang and Kopfer 2014) or vegetation ofset schemes (Nemes et al. 2008). The results of this paper provide guidance for market designers and regulators with respect to the welfare losses of linear pricing rules in large-scale combinatorial exchanges.

## 3. The Allocation Rule

Let us now introduce the specifics of the bid language and the resulting winner determination problem (WDP) or allocation rule for a combinatorial exchange, using the fishery rights exchange as a leading example. Because of the large number of fishers participating, the exchange is organized as a sealed-bid auction, a clearinghouse where allocation and prices are computed in one shot.

## 3.1. Bid Language

It is important to provide participants with a bid language that lets them express their preferences adequately using a low number of parameters. Buyers and sellers have diferent requirements for the bid language.

First, there is a need for all-or-nothing package bids for sellers. Active fishers typically possess shares in three to six share classes. Many fishers are hardly profitable and they want to quit business. For them it is important to sell their entire endowment as a package and not be left with parts of their endowment. If a fisher sells all access rights, he can also return his fishing license, for which he gets compensated. If a fisher sold only a part of his endowment, this might make it even harder or even impossible for him to be profitable, and he could not return his license. The auctioneer cannot assign more shares to a buyer than he wants, because shares come with additional obligations. However, a partial sale can be possible under certain circumstances. For example, it is possible to return excess supply for free to the government, who can then delete these excess shares if they come at no cost. This will play a role in the diferent payment rules later on. Overall, sellers typically have one all-or-nothing package bid to submit in this market, which includes their endowment in various share classes. This ask has a single price, which represents the least amount the seller wants to get for his endowment. Figure 1(a) illustrates an all-or-nothing sell-side bid for shares in three share classes.

Second, buyers want to win shares in one or more share classes, but the synergies across share classes for additional shares to their endowment are not strong. Therefore, they can submit several bids on multiple shares in a share class. Buyers can bid a unit price for a quantity interval. For example, a fisher may want to buy shares from share class A. He needs at least 125 units and at most 250 units, and is willing to pay up to 3\$ for each unit in this quantity interval. Figure 1(b) shows an example of a set of buy-side bids from one buyer. This keeps the bid language simple with a low number of parameters that bidders need to specify. The flexibility in the bid language is particularly important when using linear and anonymous prices, as we will discuss in Section 4.

We do not allow buyers to submit exclusive-or (XOR) package bids across multiple share classes for several reasons. As indicated, such synergies do not seem to be a big concern for buyers, and they find it easier to quote share prices for individual share classes rather than a bid for a package. If a fisher is interested in three share classes and he would only win shares in two classes, this would be acceptable and the exposure risk is considered low. Second, package bids across share classes would lead to significant complexities for bidders and the auctioneer. There is a combinatorial explosion of possible packages for buyers, and fishers interested in k share classes cannot be expected to submit their interests for $2 ^ { k } - 1$ packages. If bidders submit only a few of their packages of interest, this leads to eficiency losses and is known as the missing bids problem (Bichler et al. 2014). This is not an issue for the sell side, because sellers are only allowed to sell a single package bid, their endowment or a part of it, on this market. Package bids for buyers and sellers would also make the allocation problem harder to solve and significantly limit the problem sizes that can be solved optimally as numerical experiments showed.

## 3.2. The Winner Determination Problem

In what follows, we introduce some necessary notation to formulate the winner determination problem. (A list of symbols can be found in Appendix D.) We have a set of share classes L (also known as lots), indexed by l. We consider a set of auction participants I, which consists of sellers and buyers $\mathcal { I } = \mathcal { I } _ { S } \cup \mathcal { I } _ { B } ,$ with $\mathcal { I } _ { S } \cap \mathcal { I } _ { B } = \emptyset$ Each seller wants to sell a certain set of units in some or all of his share classes and submits a single bid $s \in \mathcal { S } _ { \mathbf { \Delta } }$ , with $\mathcal { S }$ being the set of all sell-side bids. The bid corresponds to the bidding language described in the previous section; a sell-side bid is a tuple $s =$ $\langle Q _ { s } ^ { 1 } , \ldots , Q _ { s } ^ { | \mathcal { L } | } , A _ { s } \rangle$ , in which a seller specifies the number of units $Q _ { s } ^ { l }$ he wants to sell in share class $l \in \mathcal { L }$ together with an ask price $A _ { s }$ for the whole package.

Figure 1. (Color online) Examples for Buy-Side and Sell-Side Bids  
![](/api/attachments/GVY7EETH/fulltext/images/3ad2a3d11eb9d0ca27f656ae7867e214b244b8526d69b91f2718c1366563950d.jpg)

Each buyer can submit multiple bids for diferent share classes, and any combination of these bids can become winning. Each bid $b \in { \mathcal { B } }$ is a tuple $\boldsymbol { b } = \langle \boldsymbol { l } _ { b } , \boldsymbol { Y } _ { b } , \bar { Y } _ { b } , \boldsymbol { D } _ { b } \rangle ,$ where $l _ { b } \in \mathcal { L }$ is a lot for which the <sup>¯</sup>bid applies; $\underline { { Y } } _ { b } , \bar { Y } _ { b }$ are the lower and upper bounds <sup>¯</sup>on the number of desired units in the corresponding lot $l _ { b } ;$ and $D _ { b }$ is the bid price per unit in this share class within the bounds specified. Sometimes we will write ${ \mathcal { B } } _ { i } \subset { \mathcal { B } }$ to denote the set of the bids of a buyer $i \in \mathcal { I } _ { B }$

We further define by $\boldsymbol { x } = \{ x _ { s } \} _ { s \in \mathcal { S } }$ the vector of seller allocations, such that $x _ { s } = 1$ when bid s is accepted and $x _ { s } = 0$ otherwise, and by $y = \{ y _ { b } \} _ { b \in \mathcal { B } }$ the vector of buyer allocations, with $y _ { b } \in Z ^ { + }$ being the number of units allocated to a buy-side bid b. Then the auction allocation (or just allocation) is a vector $a = ( x , y ) \in R ^ { | \mathcal { S \cup B } | }$ <sup>|</sup>. The allocation is feasible if for every winning buy-side bid $b \in \mathcal { W } _ { B } ,$ the number of allocated units lies in the interval $[ \underline { { Y } } _ { b } , \bar { Y } _ { b } ] ,$ , and for each lot the number of units sold is greater than or equal to the number of units bought (weak supply-demand constraint), with $\mathcal { W } _ { B }$ being the set of winning buy-side bids.

Definition 1 (Gains from Trade). An allocatively eficient assignment maximizes the gains from trade, that is, it solves the following problem:

$$
\text { maximize } \sum_ {s \in \mathscr {S}} - A _ {s} x _ {s} + \sum_ {b \in \mathscr {B}} y _ {b} D _ {b}\tag{WDP}
$$

$$
\text { s.t. } \sum_ {s \in \mathscr {S}} - Q _ {s} ^ {l} x _ {s} + \sum_ {b \in \mathscr {B}: l _ {b} = l} y _ {b} \leq 0, \quad \forall   l \in \mathscr {L},\tag{1}
$$

$$
y _ {b} \leq \bar {Y} _ {b} z _ {b}, \quad \forall b \in \mathcal {B},\tag{2}
$$

$$
\underline {{Y}} _ {b} z _ {b} \leq y _ {b}, \quad \forall   b \in \mathscr {B},\tag{3}
$$

$$
x _ {s} \in \{0, 1 \}, y _ {b} \in Z ^ {+}, z _ {b} \in \{0, 1 \}.
$$

Here constraint (1) ensures that the number of licenses bought in each share class is less than or equal to the number of licenses sold (weak supply-demand constraint). Note that this equilibrium constraint does not require strict equality. In other words, some shares might be sold in a package, although only a subset of the shares in the package are assigned to buyers. We will need a strict equality for some pricing rules later. Constraints (2) and (3) ensure that the number of licenses allocated to each buy-side bid $b \in { \mathcal { B } }$ is either 0 or belongs to range $[ \underline { { Y } } _ { b } , \bar { Y } _ { b } ]$ . To make sure that this is the case, we introduce a binary variable $z _ { b }$ for each buy bid $b ,$ which indicates whether buyer b is winning or not. This means $z _ { b }$ equals 1 if and only if there where units allocated for this bid $y _ { b } > 0 .$ . This program describes the basic winner determination problem, which we will refer to as WDP.

We will also talk about welfare maximization in situations where the gains from trade are maximized in a market, because the items end up in the hands of those with the highest valuation. In other words, welfare describes the sum of valuations of all agents who own objects either before or after the auction. An $e f f i -$ ciency loss (also called deadweight loss or allocative ineficiency) is a loss of allocative eficiency that can occur when equilibrium for a good or service is not achieved or is not achievable. It compares the possible gains from trade, that is, buyer and seller profit, in the welfare-maximizing solution with the gains from trade in an ineficient allocation (see Example 1).

Example 1. Suppose there is a seller selling a single object and having a valuation of \$12 for this object, and a buyer with a valuation of \$20. If a trade takes place, welfare is increased from \$12 to \$20, leading to an \$8 gain from trade. If the trade takes place, we have an allocatively eficient or welfare-maximizing outcome. If no trade takes place for some reason, we have zero gains from trade, or a 100% eficiency loss.

It is straightforward to extend the bid language with additional features such as exit-or-stay bids; a fisher in a new set $i \in \mathcal { E } \subset \mathcal { F }$ with ${ \mathcal { E } } \cap { \mathcal { S } } \cap { \mathcal { B } } = 0$ wants to either buy new shares $( y _ { b } > 0 )$ or sell all his shares as a package $( x _ { i } = 1 )$ :

$$
1 - x _ {i} \geq z _ {b}, \quad \forall b \in \mathcal {B} _ {i}, i \in \mathcal {E}.
$$

For the remainder, we will ignore exit-or-stay bids and focus on the WDP introduced previously.

## 4. Payment Rules

Let us now discuss diferent possibilities to compute linear and anonymous prices. We aim for prices, which are considered fair in the sense of proportional fairness and equity. In the fishery rights exchange, it is considered important that sellers, who exit their business, receive the same payment for the same package of shares.

In the introduction, we discussed that linear and anonymous competitive equilibrium prices are typically infeasible with package bids and general valuations. Therefore, we also allow for paradoxically rejected bids, that ${ \mathrm { i } } s ,$ bids that should be accepted at the prices, but they are not in the allocation. Let us now introduce a definition of linear and anonymous package prices in a combinatorial auction, which follows the glossary of Cramton et al. (2006).

Definition 2 (Linear and Anonymous Package Price). The price for any package is the sum over all items in the package of the price of each item times the quantity of the item in the package. Anonymous prices do not depend on the identity of the bidder.

The definition of a linear package price implies that (1) a package is either sold or not, but there is no partial sale of a package, and (2) winning sellers get the price of the quantities sold in each component of the package bid times the linear price vector $\textstyle ( \sum _ { l \in \mathcal { L } } Q _ { s } ^ { l } p ^ { l } )$ This notion of linear and anonymous package prices is used in day-ahead energy markets (Van Vyve et al. 2011) and in the literature on ascending combinatorial auctions (Kwasnica et al. 2005, Xia et al. 2004, Schefel et al. 2011). It is simple and intuitive, but it can lead to nonobvious issues in diferent payment rules that we discuss below in Section 4.1.

## 4.1. Anonymous and Linear Prices

There are diferent ways that linear and anonymous prices can be computed and they difer in their eficiency loss. For example, there can be a single linear (1L) price vector, or one side of the market has a payas-bid price while the other side gets linear prices. Linear prices are most important for sellers who want to exit the market, as they demand equitable prices once they quit business. We start with an allocation problem that yields seller-linear (SL) prices. For the sake of completeness, we also provide a formulation for buyerlinear (BL) prices next. Then we combine both formulations into one that yields a single linear price vector for both sides of the market. Before we discuss these payment rules, we introduce three natural requirements, which are important in the market for fishery access rights and also in many other markets:

1. The prices should be individually rational, where no participant incurs a loss with respect to his reported valuation.

2. We require linear and anonymous package prices for at least one side of the market.

3. The outcome should be strictly budget balanced.

The government must not subsidize the market; thus, the fishery rights exchange requires at least a weak budget balance (WBB; i.e., the government can make a profit, but not a loss). In addition, the government should not make a profit from the auction, because fishers do not want to see the platform as a means for the government to raise money.

Note that with a single linear price vector and a weak demand–supply constraint (i.e., demand not exceeding supply in each share class) there can only be strict budget balance (SBB): for each unit sold, one has to pay the linear price, which is the same for sellers and buyers. Since demand cannot be higher than supply, the budget balance cannot be positive.

For buyer-linear or seller-linear prices, a weak budget balance is possible, because buyers can have diferent prices than the sellers. If buyers are willing to pay a price that is high enough to clear the market, then the auctioneer can set a price high enough such that suppliers get compensated for their entire supply. However, instead of allowing the auctioneer to make a profit (which is seen undesirable by the fishers), we will set the prices such that they are strictly budget balanced. This also allows us to better compare the outcomes of the three payment rules. Let us add an example to better illustrate the diferences between single linear prices and buyer- or seller-linear prices, respectively.

Example 2. Suppose there are sellers S1 and S2, both asking for \$3 for three shares. Buyer B1 wants to buy four shares of this type for \$5 in total, and buyer B2 is willing to pay up to \$5 for one share.

• With a single linear price, demand needs to equal supply such that the auctioneer has a (strictly) balanced budget. If we charged \$1 per share, then the two sellers would ask for \$6 in total, but the buyers would only pay \$5 for the five shares in total. The auctioneer would need to buy the extra share, but he is not allowed to subsidize the market, and there would be no trade in this share class.

• With buyer-linear prices, the auctioneer could set the price at \$1.2 per share and the two buyers could buy the five shares for a total of \$1 $. 2 * 5 = \dot { \mathbb { S } } \dot { 6 }$ . The two sellers would get \$3 each for their packages and the government could delete one of the shares (at no cost to the government). Similarly, the auctioneer could also set the price for the sellers to \$(10/6) for the six shares with seller-linear prices. The two buyers would pay \$10 in total (pay-as-bid), and the extra share would get deleted.

This explains additional ineficiencies that arise with single linear prices. We allow deletion of shares in our experiments with buyer- and seller-linear prices as long as the auctioneer does not have to pay for these shares. In other words, deletion of shares can occur under the BL or SL payment rule when prices are nonzero, but not under the 1L payment rule.

4.1.1. Linear Prices for Sellers Only (SL). We start discussing a price vector for the sellers only, where the buyers submit pay-as-bid prices. Such prices can be computed by extending the WDP via additional constraints:

$$
\mathrm{extendWDP}\tag{SL WDP}
$$

$$
\sum_ {s \in \mathcal {S}} \sum_ {l \in \mathcal {L}} - Q _ {s} ^ {l} \lambda_ {s} ^ {l} + \sum_ {b \in \mathcal {B}} y _ {b} D _ {b} = 0,\tag{SBB}
$$

$$
\sum_ {l \in \mathscr {L}} \lambda_ {s} ^ {l} Q _ {s} ^ {l} \geq A _ {s} x _ {s}, \quad \forall s \in \mathscr {S},\tag{4}
$$

$$
\lambda_ {s} ^ {l} \leq \bar {P} ^ {l} x _ {s}, \quad \forall s \in \mathscr {S}, l \in \mathscr {L},\tag{5}
$$

$$
\lambda_ {s} ^ {l} \leq p ^ {l}, \quad \forall s \in \mathcal {S}, l \in \mathcal {L},\tag{6}
$$

$$
\lambda_ {s} ^ {l} \geq p ^ {l} - (1 - x _ {s}) \bar {P} ^ {l}, \quad \forall s \in \mathscr {S}, l \in \mathscr {L},\tag{7}
$$

$$
\lambda_ {s} ^ {l} \geq 0, p ^ {l} \geq 0.
$$

First, we introduce a new SBB constraint, which makes sure that the auctioneer does not make a loss nor gain. All payment rules lead to nonlinear terms and require us to linearize the product of variables. For the SL WDP, we introduce a variable, $\lambda _ { s } ^ { l } ,$ that replaces the product $p ^ { l } x _ { s } .$ , where $p ^ { l }$ is the linear price per share l. Constraint (4) ensures individually rational payments for sellers; that is, no seller will receive less than their ask price. Constraints (5)–(7) linearize the product of $x _ { s } p ^ { l }$ , where $x _ { s } \in \{ 0 , 1 \}$ and $p ^ { l } \ge 0 .$ . The parameter $\bar { P } ^ { l }$ describes the upper bound for price, such that $\lambda _ { s } ^ { l }$ is not constrained by the binary variable $x _ { s }$ in constraint (5). Constraint (7) then limits $p ^ { l } \leq \bar { P } ^ { l }$ . In our Example 2, the formulation would determine a sellerlinear price of \$1.6(6) per share. Note that with multiple share classes, the prices in the SL WDP are not yet unique. We will discuss the computation of unique linear prices in Section 4.2.

4.1.2. Linear Prices for Buyers Only (BL). Before we introduce a single linear price vector for both sides, we discuss a formulation where buyers pay linear anonymous prices and sellers get paid what they bid. The budget-balance constraint can now be written as

$$
\sum_ {s \in \mathcal {S}} - A _ {s} x _ {s} + \sum_ {b \in \mathcal {B}} y _ {b} p ^ {l} = 0,\tag{BB'}
$$

where the second summation corresponds to the amount paid by buyers with linear prices.

Unfortunately, this would be a quadratic constraint where we have the product of continuous $( p ^ { l } )$ and integer variables $\left( y _ { b } \right)$ . This requires a more sophisticated reformulation to cast it as a linear program. Let us first make the following observation, which will help us in reformulating the budget-balance constraint:

Proposition 1. Every feasible allocation for which strictly budget-balanced buyer-linear prices exist also supports weakly budget-balanced buyer-linear prices where the price equals the lowest winning bid in each share class or zero if no buy-side bids are accepted.

The proof can be found in the Appendix A. This proposition allows us to decompose the computation of strictly budget-balanced prices into two steps:

1. We determine an optimal allocation with weakly budget balanced buyer-linear prices, at which prices equal the lowest winning bids.

2. We fix the allocation and solve for buyer-linear prices, which are strictly budget balanced.

Let us look again at Example 2, where the total sum of ask prices is \$6 and there is a demand for five shares. With a strict budget-balance constraint, the buyer-linear price that every winning buyer needs to pay is \$1.2. The lowest winning bidder has a unit price of \$1.25, however. We can now compute a weakly budget-balanced allocation and set the initial buyerlinear price to \$1.25. In a second step, we fix the allocation and lower the price to \$1.2 such that strict budget balance is satisfied (described in Section 4.2).

We can now introduce the formulation as a mixedinteger program BL WDP:

extend WDP

(BL WDP)

$$
\sum_ {s \in \mathscr {S}} - A _ {s} x _ {s} + \sum_ {b \in \mathscr {B}} \sum_ {b ^ {\prime} \in \mathscr {B}: l _ {b ^ {\prime}} = l _ {b}} D _ {b ^ {\prime}} \eta_ {b, b ^ {\prime}} \geq 0,\tag{WBB}
$$

$$
\sum_ {b \in \mathcal {B}: l _ {b} = l _ {b ^ {\prime}}} D _ {b} u _ {b} \leq z _ {b ^ {\prime}} D _ {b ^ {\prime}} + \bar {P} ^ {l} (1 - z _ {b ^ {\prime}}),
$$

$$
\forall l \in \mathscr {L}, \forall b ^ {\prime} \in \mathscr {B}: l _ {b ^ {\prime}} = l,\tag{8}
$$

$$
u _ {b} \leq z _ {b}, \quad \forall b \in \mathcal {B},\tag{9}
$$

$$
\sum_ {b \in \mathcal {B}: l _ {b} = l} u _ {b} \leq 1, \quad \forall l \in \mathcal {L},\tag{10}
$$

$$
\eta_ {b, b ^ {\prime}} \leq y _ {b}, \quad \forall   b, b ^ {\prime} \in \mathcal {B}: l _ {b ^ {\prime}} = l _ {b},\tag{11}
$$

$$
\eta_ {b, b ^ {\prime}} \leq \bar {Y} _ {b} u _ {b ^ {\prime}}, \quad \forall   b, b ^ {\prime} \in \mathcal {B} \colon l _ {b ^ {\prime}} = l _ {b},\tag{12}
$$

$$
\eta_ {b, b ^ {\prime}} \geq y _ {b} - (1 - u _ {b ^ {\prime}}) \bar {Y} _ {b}, \quad \forall   b, b ^ {\prime} \in \mathcal {B} \colon l _ {b ^ {\prime}} = l _ {b},\tag{13}
$$

$$
\eta_ {b, b ^ {\prime}} \in \mathbb {Z} ^ {+}; u _ {b} \in \{0, 1 \}.
$$

We introduce a binary variable, $\boldsymbol { u } _ { b }$ , indicating whether bid b is the lowest winning buy-side bid and thus determines the price in share class $l _ { b }$ . Now we can describe the weak budget balance constraint in BL WDP as

$$
\sum_ {s \in \mathscr {S}} - A _ {s} x _ {s} + \sum_ {b \in \mathscr {B}} \sum_ {b ^ {\prime} \in \mathscr {B}: l _ {b ^ {\prime}} = l _ {b}} D _ {b ^ {\prime}} u _ {b ^ {\prime}} y _ {b} \geq 0.\tag{BB''}
$$

The second term represents the payments made by buyers according to the linear prices. In each share class, all buyers pay the price equal to the lowest winning bid $b ^ { \prime } ,$ which is $\begin{array} { r } { \sum _ { b ^ { \prime } \in \mathcal { B } : l _ { b ^ { \prime } } = l _ { b } } ^ { - } \mathbf { \bar { D } } _ { b ^ { \prime } } u _ { b ^ { \prime } } . } \end{array}$ , where at most one $\boldsymbol { u } _ { b ^ { \prime } }$ is positive (if none, the price is zero). This new constraint, (BB ), is still not linear, because we have to multiply binary variables $\left( \boldsymbol { u } _ { b ^ { \prime } } \right)$ indicating the lowest winning bid, and integer variables $( y _ { b } )$ determining quantity. However, we can linearize this product with new variables $\eta _ { b , b ^ { \prime } }$ and constraints (8)–(13). Variable $\eta _ { b , b ^ { \prime } }$ describes the amount paid by buyer b if buyer $b ^ { \prime }$ is the bidder with the lowest winning bid.

Constraint (8) is introduced for each lot $l \in \mathcal { L }$ and every buy-side bid on this lot b<sup>0</sup> <sup>∈</sup> B: $l _ { b ^ { \prime } } = l .$ It selects from all winning bids (i.e., with $z _ { b } = 1 )$ ) the ones with the lowest unit price $( D _ { b ^ { \prime } } )$ . This means, if for some accepted bid b the corresponding indicator variable $u _ { b }$ is positive, then this bid has to be less than all other accepted buy bids. At most one $u _ { b }$ in each share class can assume a value of 1 because of constraint (10). Constraint (9) guarantees that only winning bids can have positive $u _ { b }$ and thus influence the price. Constraints (11) to (13) just linearize the product of $u _ { b } ^ { \prime } y _ { b }$ in (BB ), similar to the linearization we used in the SL WDP.

The previous discussion of Example 2 showed that a strong budget-balance constraint would typically lead to infeasibility, because no set of ask prices might exactly match a particular set of bid prices in the winning allocation. The WBB constraint in the BL WDP allows for prices such that there is a positive surplus.

We get strict budget balance in a second step. For this, we fix the allocation $a ^ { * } = \left( x ^ { * } , y ^ { * } \right)$ <sup>)</sup> and then recompute the prices by replacing $\begin{array} { r } { \sum _ { b \in \mathcal { B } } \sum _ { b ^ { \prime } \in \mathcal { B } : l _ { b ^ { \prime } } = l _ { b } } D _ { b ^ { \prime } } \eta _ { j , b ^ { \prime } } } \end{array}$ with $\begin{array} { r } { \sum _ { b \in \mathcal { B } : l \in \mathcal { L } } p _ { l } y _ { b } ^ { \ast } , } \end{array}$ where $p _ { l }$ is the price a buyer has to pay, and $y _ { b } ^ { * }$ is the quantity allocated to buyers in the first step. Constraints (8)–(13) can now be removed, but one needs to restrict prices to be lower or equal to the winning bids $( p _ { l } y _ { b } ^ { * } \le D _ { b } y _ { b } ^ { * } )$ for each share class l and each winning buyer $b ^ { * }$ . The exact computation is described in Section 4.2.

4.1.3. A Single Linear Price Vector. We now introduce a model that determines an allocation with a single linear price vector:

extend WDP

(1L WDP)

$$
\sum_ {s \in \mathcal {S}} Q _ {s} ^ {l} x _ {s} = \sum_ {b \in \mathcal {B}: l _ {b} = l} y _ {b} + \delta^ {l}, \quad \forall   l \in \mathcal {L},\tag{DS}
$$

$$
\delta^ {l} \leq (1 - k ^ {l}) M, \quad \forall l \in \mathcal {L},\tag{14}
$$

$$
p ^ {l} \leq k ^ {l} \bar {P} ^ {l}, \quad \forall l \in \mathscr {L},\tag{15}
$$

$$
\sum_ {l \in \mathscr {L}} Q _ {s} ^ {l} p ^ {l} \geq A _ {s} x _ {s}, \quad \forall s \in \mathscr {S},\tag{16}
$$

$$
p ^ {l} \leq D _ {b} + \bar {P} ^ {l} (1 - z _ {b}), \quad \forall b \in \mathcal {B},\tag{17}
$$

$$
k ^ {l} \in \{0, 1 \} \quad \forall b \in \mathcal {B}, l \in \mathcal {L},
$$

$$
\delta^ {l} \in Z ^ {+} \quad \forall l \in \mathscr {L}.
$$

The 1L WDP formulation shares the dificulties that we already saw for buyer-linear prices: if we introduce the budget-balance constraint in a straightforward manner, we get the product of integer and continuous variables. Here we use a diferent modeling approach, which is faster for the 1L WDP. With 1L prices, we can achieve budget balance by using a strict demand–supply constraint (DS). This is because prices are the same for both buyers and sellers, and these prices are positive. In some cases the auctioneer may decide to step in as a buyer and bid for share classes that are not demanded to facilitate a trade. The auctioneer would not need to pay for such shares, and they are used just to satisfy the demand–supply constraint. Let us illustrate this again via a small example.

Example 3. Seller 1 wants to sell a package of A and B for 10\$, and there is only a buyer 1, who is willing to acquire a single A for 20\$. The auctioneer would like to match buyer and seller, but with a strict demand– supply constraint, such a trade would be impossible. The auctioneer, however, can cover the missing demand for B for a price of zero to facilitate the trade.

In our model, we introduce a new variable, $\delta ^ { l } ,$ that facilitates trades with package bids where demand does not meet supply. The variable $\delta ^ { l }$ can assume only a positive value, when the price in share class l is zero; that is, the government can acquire the shares at no cost. Variable $k ^ { l }$ is binary and equals zero when $\delta ^ { l }$ has positive value because of constraint (14). If $\delta ^ { l }$ is positive, then the price in share class l should be zero, which is guaranteed by constraint (15). Constraints (17) guarantee individual rationality for winning buyers $( z _ { b } = 1 )$ : the unit price is lower than an accepted buyside bid price. Prices can be higher than the bids of losing buyers with this constraint $( z _ { b } = 0 )$ . Constraint (16) guarantees individual rationality for winning sellers. Constraints (16) and (17) are binding only for winning bidders. In other words, the prices might not be compatible with the allocation for losing bidders, and there can be paradoxically rejected bids. In other words, bidders lose although their bid price was better than the market price. If constraints (16) and (17) were binding also for losing bidders, then this would result in Walrasian prices. Unfortunately, there is typically no set of Walrasian prices such that all losing sell-side package bids are higher and all losing buy-side bids are lower than these prices, and such constraints regularly lead to infeasibilities. In our experiments, we do not consider Walrasian prices for this reason.

Let us first proof that the 1L WDP is strictly budget balanced. Even without a separate constraint, the outcome of the 1L WDP always balances the budget.

Proposition 2. The outcome of the 1L WDP is strictly budget balanced.

Proof. In all share classes where demand equals supply, the auctioneer does not experience a loss due to the unique price for all trades. If supply equals demand, the number of units bought equals the number of units sold, and the unit price is the same for buyers and sellers. For those share classes where demand does not equal supply, variable $\delta ^ { l }$ assumes positive values, which forces price in these share classes to be zero (constraints (14) and (15)). In these trades, there can also be no budget loss or gain. <sup></sup>

But let us briefly discuss Example 4 at this point and analyze consequences of single linear package prices on eficiency, which might not be obvious.

Example 4. Suppose there is one buyer trying to purchase exactly three identical shares with a total bid of \$30 (\$10 per unit), and three sellers. Seller 1 wants to sell one share for \$8, sellers 2 and 3 want to sell a package of two shares for a package price of \$2. The solution of the 1L WDP is to match seller 1 and seller 3 with buyer 1.

Matching sellers 2 and 3 to buyer 1 could lead to welfare gains. However, this solution would not allow for single linear package prices, because demand does not equal supply. One possibility is to allow for partial sales of a package. For example, one of the sellers, say, seller $^ { 3 , }$ gets to sell only one share, and seller 2 sells the package. This might be perceived as unfair by seller $^ { 3 , }$ whose profit will be lower. The other possibility is to determine two price vectors, one for the seller and one for the buyer. This would, however, lead to two price vectors, and it is unclear how they relate to each other. In addition, respective optimization models have a number of nonlinear terms incurring many additional variables in a mixed-integer program, which makes these problems significantly harder to solve.

It is also interesting to mention that the bid language and the payment rule interact in nonobvious ways. If bidders are restricted to package bids on both sides of the market, buyers might not be willing or able to enumerate all exponentially many packages of interest (see Section 3.1). In multiunit, multi-item markets such as our fishery access rights exchange, it would often be the case that demand does not exactly match supply with XOR package bids from buyers and sellers, which can have a detrimental efect on the number of trades and the gains from trade generated. The flexible bid language on the buy side with lower and upper bounds on quantity alleviates bidders from having to enumerate all possible packages of interest and makes it much easier for the auctioneer to match supply and demand whenever the buyer’s willingness to pay exceeds the valuation of the seller.

## 4.2. Unique Prices

The prices determined in the previous sections (1L, SL, BL) are linear for at least one side of the market but not yet unique. Since there are some degrees of freedom, we determine unique prices such that two design goals are satisfied as far as possible. First, we want to set the linear prices such that the number of paradoxically rejected bids is minimized. Such prices are still not unique. As a secondary policy goal, the government wants to help eficient buyers, who demand additional shares, and a lower price will aid the buyers. Therefore, we minimize the sum of squared prices to keep prices low for buyers. Minimizing the sum of squared prices also balances prices across share classes. These two steps are added after an allocation problem is solved, which allows for easier comparison among the allocations. One could think of alternative design goals such as the maximization of prices. We want to have the same ex post price computations for 1L, BL, and SL, to compare the outcomes.

At first we fix the allocation $a ^ { * } = \left( x ^ { * } , y ^ { * } \right)$ resulting from the one of the allocation and payment rules ${ \mathrm { ( B L , } }$ SL, or 1L) but keep the prices as variables. Our goal is to minimize those buy (sell) bids that are rejected and for which the market price is higher (lower) than the bid price. For the 1L formulation, we introduce two new sets of variables $( o _ { b }$ and $o _ { s } ) _ { \scriptscriptstyle s }$ , which take into account the number of paradoxically rejected bids (PRB) for buyers (PRBB) and sellers (PRBS):

$$
\text { minimize } \sum_ {s \in \mathscr {S}} o _ {s} + \sum_ {b \in \mathscr {B}} o _ {b} \quad (\text { Min   PRB   1L   WDP })
$$

$$
o _ {s} \sum_ {l \in \mathscr {L}} Q _ {s} ^ {l} \bar {P} ^ {l} \geq \sum_ {l \in \mathscr {L}} Q _ {s} ^ {l} p ^ {l} - A _ {s}, \quad \forall s \in \mathscr {S}: x _ {s} ^ {*} = 0,\tag{PRBS}
$$

$$
o _ {b} D _ {b} \geq D _ {b} - p ^ {l}, \quad \forall b \in \mathcal {B}: y _ {b} ^ {*} = 0,\tag{PRBB}
$$

$$
\sum_ {l \in \mathscr {L}} Q _ {s} ^ {l} p ^ {l} \geq A _ {s}, \quad \forall s \in \mathscr {S}: x _ {s} ^ {*} = 1,\tag{IRS}
$$

$$
p ^ {l} \leq D _ {b}, \quad \forall b \in \mathcal {B}: y _ {b} ^ {*} > 0,\tag{IRB}
$$

$$
p ^ {l} \geq 0, \quad \forall l \in \mathscr {L},
$$

$$
o _ {s} \in \{0, 1 \}, \quad \forall s \in \mathcal {S}.
$$

The constraints (IRS) and (IRB) are individual rationality constraints introduced only for accepted bids. Constraints (PRBS) and (PRBB) make sure that the variables $o _ { b } \ ( o _ { s } )$ can be zero only if the corresponding bid $\textit { b } \left( s \right)$ is lower (higher) than the market price. Therefore, the variables $o _ { b }$ and $o _ { s }$ are zero only if the bid is not paradoxically rejected. In the objective function, we have the total number of paradoxically rejected bids. Related models for seller- and buyer-linear prices can be found in Appendix B.1.

In a second step, we minimize prices to aid buyers who need more shares. More specifically, we take the allocation computed by a corresponding formulation $a ^ { * } = \left( x ^ { * } , y ^ { * } \right)$ and consider the outcome of the previous step to minimize paradoxically rejected bids $o ^ { * } = \left( { o _ { b } } ^ { * } , { o _ { s } } ^ { * } \right) :$

$$
\min \sum_ {l \in \mathscr {L}} p ^ {l ^ {2}} \quad (\text { Unique   prices   1L   WDP })
$$

$$
A _ {s} \geq \sum_ {l \in \mathcal {L}} Q _ {s} ^ {l} p ^ {l}, \quad \forall s \in \mathcal {S}: x _ {s} ^ {*} = 0, o _ {s} ^ {*} = 0,\tag{PRBS}
$$

$$
p ^ {l} \geq D _ {b}, \quad \forall b \in \mathcal {B}: y _ {b} ^ {*} = 0, o _ {b} ^ {*} = 0,\tag{PRBB}
$$

$$
\sum_ {l \in \mathscr {L}} Q _ {s} ^ {l} p ^ {l} \geq A _ {s}, \quad \forall s \in \mathscr {S}: x _ {s} ^ {*} = 1,\tag{IRS}
$$

$$
p ^ {l} \leq D _ {b}, \quad \forall   b \in \mathscr {B}: y _ {b} ^ {*} > 0,\tag{IRB}
$$

$$
p ^ {l} \geq 0, \quad \forall l \in \mathscr {L}.\tag{18}
$$

In this formulation, we keep the individual rationality constraints (IRS) and (IRB) for accepted bids and add the (PRBS) and (PRBB) constrains to consider the previous step where the paradoxically rejected bids are minimized. This means, for those bids that were not paradoxically rejected, rejected buy (sell) bids should be lower (higher) than the market price. The corresponding models for seller- and buyer-linear prices can be found in Appendix B.2.

## 4.3. Linear Prices and Eficiency

Linear and anonymous prices are simple and intuitive for bidders in noncombinatorial markets. Unfortunately, their extension to combinatorial auctions is challenging. Definition 2 implies that every package bid is sold in total or not at all; there is no partial sale of a package. In addition, a winning bidder can expect a total price that is the product of the quantity and price per component of a package bid. With single linear prices, this definition leads to ineficiencies.

Let us consider a modified version of Example 2. We keep sellers 1 and 2 with an ask price of \$3 for three shares each, but on the buy side we have only one buyer with a demand of five units and a total bid price of \$12 (\$2.4 per share). With Definition 2 and anonymous single linear prices and package bids, no trade will happen, because there must not be a budget deficit. This is ineficient, because the buyer wants to pay more than the sellers ask for.

The impact of nonconvexities in economics has received significant attention in the last century, as we discussed in Section 2. The literature suggests that nonconvexities become less of a concern in large markets, and with some assumptions a Walrasian equilibrium exists regardless of the nature of the bundle preferences in large markets (Azevedo et al. 2013). Unfortunately, even for our combinatorial fishery exchange with 1,000 fishers, we cannot find Walrasian prices. It is important to understand the losses in allocative eficiency that can be attributed to linear and anonymous prices, even if we allow for paradoxically rejected bids. Note that we assume that all bidders are truthful, and we aim to study the impact of linear prices, ignoring gaming by bidders. We use the following definition of eficiency loss:

Definition 3. The <sup>(</sup>relative<sup>)</sup> eficiency loss due to linear prices can be defined as the ratio

$$
l o s s = \left\{ \begin{array}{l l} \frac {G _ {D P} - G _ {L P}}{G _ {D P}} & \text { if } G _ {D P} > 0, \\ 0 & \text { otherwise }, \end{array} \right.\tag{19}
$$

where $G _ { D P }$ represents gains from trade with discriminatory prices, and $G _ { L P }$ represents gains from trade with linear and anonymous prices. $G _ { D P }$ is equal to the WDP solution, and $\dot { G _ { L P } }$ will take on each of the corresponding WDP values for SL, BL, and 1L.

Unfortunately, eficiency loss can be up to 100% in the worst case, as the next proposition shows.

Proposition 3. The eficiency loss with single linear prices in the 1L WDP is 100% in the worst case.

Proof. Suppose there is a buyer 1 who wants to buy one unit of a good for $\$ \varepsilon,$ , where ε is a small number. Another buyer, buyer $^ { 2 , }$ is willing to pay \$M for one unit, where M is a large number. In addition, there is a seller who wants to sell a package of two units for $\$ 3\varepsilon$ The gains from trade in the welfare-maximizing allocation are $M - 2 \varepsilon$ . As in the Proposition 2 proof, we know that supply needs to equal demand in a share class with a positive single linear price. Therefore, with single linear prices it is impossible to charge a higher price for buyer 2 and discard the second object. As a result, linear prices need to be less or equal to $\varepsilon ,$ such that there would be no trade. The eficiency loss is $M - 2 \varepsilon$ or 100%. <sup></sup>

If there are only two buy-side bids and one sell-side bid as in the proof of Proposition 3, then we cannot match supply and demand, because otherwise budget balance would not be satisfied in the 1L WDP. With a single linear price, the same quantity needs to be available for the buy side and the sell side to satisfy budget balance. The buyer with the high bid M could approach the seller of the package after the auction, buy both units, and then resell one of the units to the second buyer at a lower price. However, this would introduce personalized prices after the auction, which is what we do not want to allow in the auction.

Unfortunately, the worst-case eficiency loss with linear prices for one side of the market can also be 100%, as we show in the following two corollaries.

Corollary 1. The eficiency loss for buyer-linear prices in BL WDP is 100% in the worst case.

Proof. Suppose there is a buyer 1 who wants to buy one unit of a good for $\$ { M -\varepsilon },$ where ε is a small number and M is a large number. Another buyer, buyer 2, is willing to pay $\bar  \$ 123,456$ for one unit. In addition, there is a seller who wants to sell a package of two units for \$M. The gains from trade in the eficiencymaximizing allocation are $\$ 3$ . With buyerlinear prices, the price must not exceed $\$ { M } / { 2-\varepsilon }$ such that there will be no trade, and the eficiency loss is $\$ 3,456,7$ or 100%. <sup></sup>

Corollary 2. The eficiency loss for seller-linear prices in SL WDP is 100% in the worst case.

Proof. Suppose there is a seller 1 who wants to sell one unit of a good for $\$ { M } +\varepsilon$ , where ε is a small number and M is a large number. Another seller, seller $^ { 2 , }$ asks for $\$ { M } / { 2+ \varepsilon }$ for one unit. In addition, there is a buyer who wants to buy two units for \$M per unit. The gains from trade in the eficiency-maximizing allocation are $\$ 3,4$ . With seller-linear prices, the price must not be less than $\$ { M } +\varepsilon$ , resulting in a negative budget. Thus, there will be no trade, and the eficiency loss is $\$ 3,456$ , or 100%. <sup></sup>

The proof of Proposition 3 for single linear prices constructs a worst-case setting with only one seller and two buyers. This negative result is in contrast to the low eficiency losses that we find in our experimental results. In Proposition $^ { 4 , }$ we show that even in a setting with one package bid, as was used in the previous proofs, eficiency losses vanish in expectation as the number of buyers grows large, but the package size is small. This helps us understand the experimental results in the paper.

For the proof, let us introduce some additional notation. Suppose, we have one truthful seller $s \in \mathcal { I } _ { S }$ submitting a package of size k and $n = \lvert \mathcal { I } _ { B } \rvert$ truthful buyers $b \in \mathcal { I } _ { B } \rvert$ with unit demands. We denote the value of a seller per unit by $X ,$ which is a random variable with a continuous probability density function $f _ { X } ( x )$ and a cumulative distribution function of $F _ { X } ( x )$ . Similarly, the value that a buyer b has for a single unit is a random variable, $Y _ { b } , b \in \mathcal { I } _ { B } ^ { \cdot } ,$ following a continuous probability density function $f _ { Y } ( y )$ and a cumulative distribution function $F _ { Y } ( y )$

Let $P ( D P )$ be the probability of an eficiency-maximizing solution with discriminatory prices and positive gains from trade. This is the same as the probability that the sum of the valuations $Y _ { b }$ of the highest k bidders $b \in \mathcal { I } _ { B }$ is higher than kX. Let $P ( L P )$ describe the probability of a trade with linear and anonymous prices, that is, the probability that k times the single linear price of the kth highest bidder is higher than X. In contrast, $P ( \overline { { L P } } )$ denotes the probability that there is no trade with positive gains due to linear prices. Note that in this simplistic scenario the eficiency loss can be either 100% or 0%. This means the expected eficiency loss is $P ( { \overline { { L P } } } \cap D P )$ , the probability that there is an eficiency-maximizing solution with discriminatory prices and the probability that there is no trade with linear prices.

Definition 4. The expected eficiency loss due to linear prices can be computed as

$$
\begin{array}{c} E [ l o s s ] = P (\overline {{L P}} \cap D P) = P (D P) - P (L P \cap D P) \\ = P (D P) - P (L P). \end{array}\tag{20}
$$

Proposition 4. Suppose we have a multiunit market with one seller selling a package of k units and n unit-demand buyers, and the valuations of the buyers and the seller are drawn from the same distribution, $f _ { Y } = f _ { X }$ . Then, the expected eficiency loss due to linear prices is less than $( \dot { k } - 1 ) / ( n + 1 )$

From Proposition 4 we learn that with $k = 1$ , there is no eficiency loss. With $k = n _ { \mathrm { . } }$ , the eficiency loss is upper bounded by $1 - 2 / ( n + 1 )$ , and a very high eficiency loss can be expected with $n \to \infty$ . The simple formula $( k - 1 ) / ( n + \bar { 1 } )$ relies on the assumption that $f _ { Y } = f _ { X }$ . We can also look at parametric cases, where $f _ { Y } \neq f _ { X } ,$ to get succinct closed form solutions.

Corollary 3. Suppose we have a multiunit market with one seller selling a package of k units and n unit-demand buyers, and the valuations of the buyers and the seller are drawn from diferent uniform distributions, $f _ { Y } \sim U ( a _ { Y } , b _ { Y } )$ and $f _ { X } \sim U ( a _ { X } , b _ { X } )$ and $b _ { Y } \geq b _ { X }$ . The expected eficiency loss due to linear prices is bounded by

$$
\frac {b _ {Y} - a _ {Y}}{b _ {X} - a _ {X}} \frac {k - 1}{n + 1}.
$$

With $f _ { Y } \sim U ( 0 , 1 )$ and $f _ { X } \sim U ( 0 , 1 )$ , we get an upper bound of $( k - 1 ) / ( n + 1 )$ for expected eficiency loss. The number of possible combinations of package bids in a combinatorial auction makes it dificult to derive more general analytical bounds. We focus on numerical experiments based on field data in this paper, but the analysis of the analytical model already provides useful insights beyond the worst-case analysis only.

## 4.4. Incentives in Large Markets

So far, we have assumed truthful bidding and focused on eficiency losses due to linear and anonymous prices. Incentives for truthful bidding in two-sided markets are a truly fundamental problem, and one that is beyond this paper. Myerson and Satterthwaite (1983) already showed that there is no mechanism that is eficient, Bayesian Nash incentive compatible, individually rational, and at the same time balances the budget. It is straightforward to come up with small complete-information examples where some bidders could manipulate profitably.

Several authors study the incentives of bidders in large markets. For example, Roberts and Postlewaite $( 1 9 { \bar { 7 } } 6 )$ showed that in large markets the ability of an individual player to influence the market is minimal, so agents should behave as price-taking agents. Later, Rustichini et al. (1994) showed that in a multiunit call market, the ineficiency asymptotically disappears when the number of market participants becomes large.

In summary, in large markets, such as our fishery rights exchange, where we can expect many bidders and high uncertainty about others’ valuations, the incentives for strategic manipulation are quite limited. Participants are inexperienced, and they are cautious and probably risk averse, as this is a one-shot market. More importantly, the benefits and risks of manipulation are far from obvious in such an environment.

## 5. Experimental Evaluation

Our theoretical results are independent of a specific domain. In our experimental evaluation, we want to analyze the average eficiency losses incurred by linear prices, the payof distribution between buyers and sellers for single linear prices, the average proportion of paradoxically rejected bids in diferent pricing schemes, and the computational hardness of the allocation problem for the market for fishery access rights. Here we can consider the details of the environment, which gives us a good estimate of what can be expected in a real-world market. We are fortunate to have a data set from an Australian fishery market available, which allows us to generate realistic problem instances.

## 5.1. Data and Bid Generation

Let us first summarize the available field data and describe the bid generation for our experiments. Our data set provides information about the fishing licenses (share classes) each registered fishing business possesses. Moreover, the data show how many shares in each share class the fishers have and the revenue the businesses generates from the licenses (estimated based on landings and fish market prices). We can also learn from the data which share classes are owned by fishers, indicating synergies. The data contain records of about 100 share classes distributed among more than 1,000 fishers.

The revenue of a fisher per share class and overall allows us to estimate which fishing businesses are profitable and whether a business needs more licenses or wants to sell either low-revenue shares or a package of all shares, that ${ \mathrm { i } } \mathbf { s } ,$ whether the fisher wants to stop operating. The revenue values vary significantly in the data: some fishers have no revenue from their shares, while the largest business managed to earn several millions of dollars over five years. On average a fishing business has a revenue of around \$60’000 per year.

Our bid generation algorithm is based on these data, and it consists of two parts: a package generator decides which of the fishers participate as buyers or sellers of certain shares, and which fishers do not participate. It also chooses which shares each participant would like to buy or to sell. The valuation generator estimates the value of a certain package (or individual share class) for a fisher. The package generator randomly chooses fishers to participate in the auction via a participation probability $\rho .$ . Then, with probability α a participant will act as a seller, and with probability 1 <sup>−</sup> α he will be a buyer. We assume that fishers want to either grow their business or sell shares; that is, they are either sellers or buyers on the market.

For each sell-side bid we analyze whether a fisher is profitable. If not, we consider this fisher to be willing to quit the market and construct a package containing all (if package size is not constrained) shares he currently possesses. If a fisher has positive revenue, he still may want to sell unused licenses. Hence, we include all licenses with low profit in the package. Each share class l owned by a fisher can be selected for sale with a probability $1 - r _ { l } / r _ { \operatorname* { m a x } } ,$ where $r _ { l }$ is the revenue per share that a bidder has from share class l, and $r _ { \mathrm { m a x } }$ is the maximum revenue per share among all his possessions. To control for diferent package sizes, we also introduce the parameter $\kappa ,$ which defines the maximum number of diferent share classes a sell bid can contain.

Each buyer can submit multiunit bids for diferent share classes. For our simulation, we assume that each buyer is submitting at most five bids: this is in accordance with the field data, which show that fishers rarely use more than five share classes simultaneously. Here we consider two scenarios: (1) the fisher has highly profitable licenses and wants to acquire additional units in these share classes, and (2) the fisher wants to purchase fishing rights in an adjacent region. For the first scenario, we retrieve all share classes owned by a fisher with a respective revenue per catch being higher than the mean revenue from the same class among along fishers. Then we construct a bid with a random number of units below the current number of units the fisher has in the share class. For the second scenario, we analyze all profitable share classes that a fisher has and select adjacent high-revenue share classes he may be interested in.

The bid language allows buyers to submit flexible bids: they can specify a lower bound and an upper bound for number of shares they want to acquire. However, some of the buyers may be specific in their desires, and instead of a flexible bid they can submit a fixed bid, where upper and lower bounds coincide. The ratio of fixed bids can strongly impact the computation time, and we decided to control the number of these bids through a parameter, $f ,$ that determines the probability of submitting a fixed bid.

The valuation generator assumes that each share class has some common value (which depends on how profitable this class is on average among all active fishers), and then each fisher can over- or underestimate this common value. To compute the percentage at which each bidder deviates from the common value, we use two normal distributions for sellers and buyers, which are parameterized by mean values $\mu _ { S } \geq 1$ and $\mu _ { B } \leq 1$ and standard deviation $\sigma \in ( 0 , 1 )$ . This means that if the common value for a share class is $V ,$ then the value for a particular seller is taken from a Normal distribution with $\mathcal { N } ( V \mu _ { s } , V ^ { 2 } \sigma ^ { 2 } )$ . Furthermore, we denote the diference between deviation means of buyers and sellers by a spread parameter, $\Delta _ { \mu } = \mu _ { S } - \mu _ { B }$ (see Figure 2), and use it as a treatment variable. For example, we can simulate markets where buy- and sell-side valuations difer (which implies a lower social welfare) or where they are alike $\bigl ( \Delta _ { \mu } \bigr ) ^ { - } = 0 \bigr )$

In our experiments, we assume that bidders submit their valuations truthfully to learn the average eficiency loss, which can be attributed to the pricing rule only. Of course, bidders with a pay-as-bid payment rule will shade their bids in the field, which will lead to additional eficiency losses. We decided to limit our report of the experimental results to truthful bidding, which does not require additional assumptions about bidder behavior and is therefore easier to interpret.

Figure 2. (Color online) Value Generation from Distribution  
![](/api/attachments/GVY7EETH/fulltext/images/ede6ccdcaf70003ce8619a4fc144f04f46f762b2a59bc06afd7be79f4abdc105.jpg)

## 5.2. Experimental Design

Overall, we have the following treatment variables for our numerical experiments:

• Prices: We analyze SL, BL, and 1L payment rules, described in Section 4. The eficient allocation without pricing (WDP) serves as the baseline.

• Participation probability $\rho \colon$ This determines the ratio of the total number of fishers to participate in the auction. When $\rho = 1 . 0 ,$ , this means that all 1,000 fishers (from our data set) submit bids. A value of $\rho = 0 . 5$ means that only half the fishers participate in the market. With participation probability $\rho = 1 . 0 _ { \cdot }$ , we get around 1,300 bids (each buyer can submit up to five bids).

• Sell bid probability α: This determines the ratio between buyers and sellers. We consider values 0.3 and 0.5.

• Probability of fixed buy-side bid $f \colon$ This determines the ratio of buyers who submit a buy-side bid for a specific quantity only rather than a range, that is, $\bar { Y } _ { b } = \underline { { \hat { Y } } } _ { b }$ . All others specify flexible bids with range of $\bar { Y } _ { b } > \underline { { Y } } _ { b }$ . We allow for two possible values. A value of $f = 0$ <sup>¯</sup>means that no bidder submits a fixed buy-side bid, and a value of $f = 0 . 5$ means that half of the bids have fixed quantities.

• Maximum package size κ: This determines the maximum amount of share classes that a sell bid may contain. We use the values 2 and 4.

• Spread of mean values $\Delta _ { \mu } .$ : This determines relative diference in the mean values of the buy-side and sell-side value distributions. We use the values 0.3 and $0 . 5 ;$ that is, on average, buyers (sellers) tend to overestimate (underestimate) the common value by 0.15% (0.25%).

• Standard deviation σ: This determines the standard deviation for the two value distributions. We use the values 0.2 and 0.4.

Of course, the number of shares included will also have an impact on the problem size, and a decreasing the number of shares will make it easier to solve. We decided to limit the number of treatment variables and rather use participation probability as a parameter to control problem size. Based on the underlying data about initial endowments of shares to fishers and diferent values for these treatment variables, we generate problem instances. Overall, we have seven treatment variables and a full factorial $4 \times 2 \times 2 \times 2 \times 2 \times$ $2 \times 2 = 2 5 6$ design with the response variables eficiency loss, w; payof share of sellers, $( \pi _ { S } ) ;$ proportion of paradoxically rejected bids, <sup>(</sup>e<sup>)</sup>; run time, <sup>(</sup>t<sup>)</sup>;

integrality gap or mixed-integer programming (MIP) gap, <sup>(</sup>g<sup>)</sup>; and average package size, <sup>(</sup>v<sup>)</sup>. The MIP gap is the bound between the best feasible integer solution and the best linear programming relaxation in the branch-and-bound tree, and it provides a bound on how far away the currently best feasible integer solution is from the optimal solution in the worst case. We report the results of 15 experiments of each of the 256 treatment combinations, that is, 3,840 experiments in total.

## 5.3. Experimental Results

Let us first provide an overview of the results. Table 1 shows a summary of the experimental results for the welfare-maximizing solution (without pricing constraints; the WDP) and 1L, SL, and BL prices. It shows that BL and SL prices lead to almost no eficiency loss on average, but 1L pricing incurs an average eficiency loss of 6.2% across all treatment combinations. As we will see in the detailed results, the worst-case eficiency loss can also be higher, and there is a trade-of that regulators face between the benefits of a single linear price and the eficiency loss it causes. In summary, however, the average case eficiency loss in the experiments is much lower than what the worst-case analysis might suggest.

The mean seller payof ratio $\left( \hat \pi _ { S } \right)$ is only of interest for the 1L prices, and Table 1 shows that around 39% of gains from trade are allocated to sellers on average. If an equal split of the gains from trade were desirable, this could be considered in the price computation. Computation was rarely an issue, even though the highest MIP gap found for BL prices was 36% with a timeout of 500 seconds. The average MIP gap is negligible for all pricing rules, which is remarkable given the problem sizes, and it provides evidence that combinatorial exchanges of this size can be organized nowadays.

We also computed the outcome of the VCG mechanism for a number of instances. However, the budget deficit of the auctioneer was around 50% of the gains from trade generated by the auction, which would not be acceptable in the field. This is why we do not report VCG results. Let us now discuss the results for the different focus variables in more detail.

Table 1. Overall Comparison of Pricing Rules: Mean Social Welfare Loss w¯ , Mean Seller Payof Ratio ${ \bar { \pi } _ { S } } ,$ Mean Computation Time <sup>¯</sup>t, Mean MIP Gap g¯, Maximum MIP Gap max<sup>(</sup>g<sup>)</sup>, and Average Ratio of Paradoxically Rejected Bids e¯ Within a Run Time of 500 Seconds

<table><tr><td>Pricing</td><td> $\bar{w}$ </td><td> $\bar{\pi}_{S}$ </td><td> $\bar{t}$ </td><td> $\bar{g}$ </td><td> $\max(g)$ </td><td> $\bar{e}$ </td></tr><tr><td>WDP</td><td>0</td><td>0</td><td>0.28</td><td>0</td><td>0</td><td>0</td></tr><tr><td>BL</td><td>0.0039</td><td>0</td><td>11.3</td><td>0.00058</td><td>0.36074</td><td>0.022</td></tr><tr><td>SL</td><td>0</td><td>1</td><td>0.69</td><td>1.00E-05</td><td>1.00E-04</td><td>0.030</td></tr><tr><td>1L</td><td>0.0618</td><td>0.39</td><td>8.95</td><td>6.00E-05</td><td>0.03626</td><td>0.018</td></tr></table>

Table 2. Run Time: Average Time to Solve in Seconds ${ \bar { t } } ,$ Standard Deviation of Time $\sigma _ { t } ,$ , Maximum Time Used max<sup>(</sup>t<sup>)</sup>, and Maximum MIP Gap max<sup>(</sup>g<sup>)</sup> for Full Participation $\rho = 1$

<table><tr><td>Pricing</td><td> $\Delta_{\mu}$ </td><td> $\sigma$ </td><td> $f$ </td><td> $\alpha$ </td><td> $\bar{t}$ </td><td> $\sigma_t$ </td><td> $\max(t)$ </td><td> $\max(g)$ </td></tr><tr><td>BL</td><td>0.3</td><td>0.2</td><td>0</td><td>0.3</td><td>20.5</td><td>4.42</td><td>29.29</td><td>0</td></tr><tr><td>BL</td><td>0.3</td><td>0.2</td><td>0.5</td><td>0.3</td><td>26.69</td><td>8.02</td><td>48.33</td><td>0</td></tr><tr><td>BL</td><td>0.5</td><td>0.2</td><td>0</td><td>0.3</td><td>38.61</td><td>89.81</td><td>511.37</td><td>0.08</td></tr><tr><td>BL</td><td>0.5</td><td>0.2</td><td>0.5</td><td>0.3</td><td>46.85</td><td>86.49</td><td>500.52</td><td>0.08</td></tr><tr><td>BL</td><td>0.5</td><td>0.2</td><td>0.5</td><td>0.5</td><td>30.97</td><td>91.91</td><td>500.34</td><td>0.01</td></tr><tr><td>BL</td><td>0.5</td><td>0.4</td><td>0.5</td><td>0.3</td><td>22.49</td><td>6.04</td><td>33.34</td><td>0</td></tr><tr><td>1L</td><td>0.3</td><td>0.2</td><td>0.5</td><td>0.3</td><td>39.33</td><td>99.66</td><td>500.2</td><td>0.04</td></tr><tr><td>1L</td><td>0.3</td><td>0.2</td><td>0.5</td><td>0.5</td><td>34.92</td><td>99.06</td><td>500.26</td><td>0.01</td></tr><tr><td>1L</td><td>0.3</td><td>0.4</td><td>0.5</td><td>0.3</td><td>46.59</td><td>120.38</td><td>500.2</td><td>0</td></tr><tr><td>1L</td><td>0.5</td><td>0.4</td><td>0.5</td><td>0.3</td><td>54.42</td><td>143.47</td><td>500.29</td><td>0</td></tr><tr><td>1L</td><td>0.5</td><td>0.4</td><td>0.5</td><td>0.5</td><td>39.71</td><td>78.35</td><td>283.9</td><td>0</td></tr></table>

5.3.1. Computational Analysis. The winner determination problem in our combinatorial exchanges is an NP-hard problem. This is straightforward to see, because the combinatorial auction problem where the buyers $\mathcal { I } _ { B }$ want to purchase one share each and the sellers $\mathcal { I } _ { S }$ ofer packages of shares is a special case (de Vries and Vohra 2003). It is therefore not obvious that relevant problem sizes with hundreds of fishers can be solved to optimality. Interestingly, because of our bid language, even large scenarios can be solved in less than a minute to optimality (on average) on a laptop with an Intel Core i7-4712HQ processor and 16.0 GB of RAM. For all numerical experiments, we used a branch-and-cut implementation of the Gurobi mixed-integer programming solver, version 7.0. Table 2 shows the average results for all treatment combinations with $\rho = 1$ where the maximum run time was greater than 20 seconds. The eficient solution without pricing (WDP) can always be computed in a few seconds. The same is true for seller-linear prices.

Two features of the bid language appear decisive for these results: First, only one side of the market is allowed to place package bids. Actually, in the fishery market, only the sellers who want to exit the market have a strong need for package bids. They want to leave the market and not end up with part of their shares, which would render the business unprofitable. With package bids on both sides of the market, initial experiments already showed that the problems become much harder to solve, and problem sizes of less than 200 bidders would already be intractable. If package bids were needed on both sides of the market, the auctions would need to be smaller to compute results that were suficiently close to optimality. Second, buyers specify a quantity range for which they are interested. In a regression where we control for the participation probability $\rho ,$ the mean spread $\Delta _ { \mu } ,$ the payment rule, and the deviation $\sigma ,$ we find that an increase of $f$ (ratio of buyers with fixed buy bids) significantly increases the run time for 1L and BL prices and causes higher MIP gaps after 500 seconds.

Table 3. Eficiency Loss: Mean Eficiency Loss w¯ , Standard Deviation $\sigma _ { w } ,$ and Maximum Value of Eficiency Loss max<sup>(</sup>w<sup>)</sup>

<table><tr><td>Setup</td><td> $\rho$ </td><td> $f$ </td><td> $\kappa$ </td><td> $\bar{w}$ </td><td> $\sigma_w$ </td><td> $\max(w)$ </td></tr><tr><td>BL</td><td>0.5</td><td>0</td><td>2</td><td>0.002</td><td>0.011</td><td>0.087</td></tr><tr><td>BL</td><td>0.5</td><td>0</td><td>4</td><td>0.001</td><td>0.006</td><td>0.042</td></tr><tr><td>BL</td><td>0.5</td><td>0.5</td><td>2</td><td>0.005</td><td>0.019</td><td>0.135</td></tr><tr><td>BL</td><td>0.5</td><td>0.5</td><td>4</td><td>0.021</td><td>0.117</td><td>1</td></tr><tr><td>BL</td><td>1</td><td>0</td><td>2</td><td>0.001</td><td>0.008</td><td>0.082</td></tr><tr><td>BL</td><td>1</td><td>0</td><td>4</td><td>0</td><td>0</td><td>0.004</td></tr><tr><td>BL</td><td>1</td><td>0.5</td><td>2</td><td>0</td><td>0.002</td><td>0.018</td></tr><tr><td>BL</td><td>1</td><td>0.5</td><td>4</td><td>0.001</td><td>0.009</td><td>0.082</td></tr><tr><td>1L</td><td>0.5</td><td>0</td><td>2</td><td>0.047</td><td>0.06</td><td>0.385</td></tr><tr><td>1L</td><td>0.5</td><td>0</td><td>4</td><td>0.058</td><td>0.068</td><td>0.403</td></tr><tr><td>1L</td><td>0.5</td><td>0.5</td><td>2</td><td>0.096</td><td>0.112</td><td>0.544</td></tr><tr><td>1L</td><td>0.5</td><td>0.5</td><td>4</td><td>0.129</td><td>0.147</td><td>1</td></tr><tr><td>1L</td><td>1</td><td>0</td><td>2</td><td>0.026</td><td>0.031</td><td>0.273</td></tr><tr><td>1L</td><td>1</td><td>0</td><td>4</td><td>0.024</td><td>0.02</td><td>0.115</td></tr><tr><td>1L</td><td>1</td><td>0.5</td><td>2</td><td>0.062</td><td>0.055</td><td>0.345</td></tr><tr><td>1L</td><td>1</td><td>0.5</td><td>4</td><td>0.053</td><td>0.048</td><td>0.301</td></tr></table>

5.3.2. Eficiency Losses. Table 3 reports those treatment combinations where there was an eficiency loss. In all treatment combinations, even with 1L prices, the average eficiency loss was below 13%. However, there was one instance where the eficiency loss was 100% for BL and 1L prices. This instance was very small: it had only four buy bids and two sell bids in the eficient solution. With SL prices, the individual rationality constraint is weaker, as it concerns a package of shares and not individual share classes. Therefore, the eficiency losses are lower. Remember that, in our simulations, we assume that those bidders with BL or SL prices with a pay-as-bid payment rule bid truthfully. Of course, bidders will shade their bids to some extent in the field. In the field, there will be eficiency losses due to bid shading by bidders with a pay-as-bid rule.

A linear regression model allows us to estimate the impact of diferent pricing rules but control for $\rho , f ,$ $\Delta _ { \mu } ,$ and $\sigma$ (see Appendix C for details). The regression yields a multiple $R ^ { 2 }$ of 0.36 and shows a significant negative efect of the 1L payment rule on eficiency with the WDP as a baseline, while the SL and BL payment rules have no significant efect on eficiency. Also, an increase in the probability of a fixed quantity <sup>(</sup> f <sup>)</sup> and an increase in $\Delta _ { \mu }$ have negative impacts. Finally, an increase of the participation probability ρ from 0.5 to 1.0 has a significant positive impact on relative eficiency.

Figure 3(a) shows how the number of participants impacts eficiency loss for 1L prices. (For the other two pricing schemes, the efect is not so significant.) We observe that the 1L rule may lead to significant eficiency losses when the number of participants is low.

Figure 3. (Color online) Eficiency Loss for Varying Participation ρ and Fixed Bid Probability f for $\alpha = 0 . 3 , \Delta = 0 . 3 , \sigma = 0 . 2 ,$ and an Average of 30 Runs  
![](/api/attachments/GVY7EETH/fulltext/images/982656a11b40af2a839621cf4b728dd5f94b303347b14c1e9415df5811ebb649.jpg)  
Figure 3(b) shows how an increase in the probability of buy-side bids with fixed quantity ( f ) impacts eficiency loss for 1L. The curve consists of the average eficiency values for each x point from 30 runs and the regression curve (for all data). Bidding only for specific quantities rather than quantity ranges has a negative impact on eficiency, because it becomes harder to match buyand sell-side bids. There is no significant impact of BL and SL on eficiency. In our theoretical model in Section 4.3, the package size also had an impact on the eficiency loss. However, we analyzed a model where

Table 4. Paradoxically Rejected Bids: Mean and Maximum of Percentage of Paradoxically Rejected Bids e¯ and max<sup>(</sup>e<sup>)</sup>

<table><tr><td>Prices</td><td>ρ</td><td>Δ</td><td>f</td><td>ē</td><td>max(e)</td></tr><tr><td>BL</td><td>0.5</td><td>0.3</td><td>0</td><td>0.02</td><td>0.05</td></tr><tr><td>BL</td><td>0.5</td><td>0.3</td><td>0.5</td><td>0.03</td><td>0.11</td></tr><tr><td>BL</td><td>0.5</td><td>0.5</td><td>0</td><td>0.01</td><td>0.05</td></tr><tr><td>BL</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.02</td><td>0.07</td></tr><tr><td>BL</td><td>1</td><td>0.3</td><td>0</td><td>0.02</td><td>0.05</td></tr><tr><td>BL</td><td>1</td><td>0.3</td><td>0.5</td><td>0.03</td><td>0.07</td></tr><tr><td>BL</td><td>1</td><td>0.5</td><td>0</td><td>0.02</td><td>0.06</td></tr><tr><td>BL</td><td>1</td><td>0.5</td><td>0.5</td><td>0.03</td><td>0.08</td></tr><tr><td>SL</td><td>0.5</td><td>0.3</td><td>0</td><td>0.04</td><td>0.08</td></tr><tr><td>SL</td><td>0.5</td><td>0.3</td><td>0.5</td><td>0.04</td><td>0.09</td></tr><tr><td>SL</td><td>0.5</td><td>0.5</td><td>0</td><td>0.03</td><td>0.06</td></tr><tr><td>SL</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.02</td><td>0.07</td></tr><tr><td>SL</td><td>1</td><td>0.3</td><td>0</td><td>0.04</td><td>0.06</td></tr><tr><td>SL</td><td>1</td><td>0.3</td><td>0.5</td><td>0.03</td><td>0.06</td></tr><tr><td>SL</td><td>1</td><td>0.5</td><td>0</td><td>0.03</td><td>0.05</td></tr><tr><td>SL</td><td>1</td><td>0.5</td><td>0.5</td><td>0.02</td><td>0.06</td></tr><tr><td>1L</td><td>0.5</td><td>0.3</td><td>0</td><td>0.02</td><td>0.04</td></tr><tr><td>1L</td><td>0.5</td><td>0.3</td><td>0.5</td><td>0.03</td><td>0.06</td></tr><tr><td>1L</td><td>0.5</td><td>0.5</td><td>0</td><td>0.01</td><td>0.04</td></tr><tr><td>1L</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.02</td><td>0.06</td></tr><tr><td>1L</td><td>1</td><td>0.3</td><td>0</td><td>0.02</td><td>0.04</td></tr><tr><td>1L</td><td>1</td><td>0.3</td><td>0.5</td><td>0.03</td><td>0.06</td></tr><tr><td>1L</td><td>1</td><td>0.5</td><td>0</td><td>0.01</td><td>0.04</td></tr><tr><td>1L</td><td>1</td><td>0.5</td><td>0.5</td><td>0.02</td><td>0.05</td></tr></table>

![](/api/attachments/GVY7EETH/fulltext/images/97a2e06ef51e369fd47644be43f029856e6f84c7329212f5a004d687cb152e2a.jpg)

bidders could even have packages covering all shares. This is not the case in the field data, where most sellers are small with shares in only a few share classes, but not in all 100. We limited the number of share classes that fishers where interested to sell, but this had no significant efect on eficiency in a regression analysis. We did not run simulations with larger package sizes beyond what we found in the field data to keep the simulations as realistic as possible. Package size might, however, matter in other markets where there are very large package bids.

5.3.3. Paradoxically Rejected Bids. Buy (sell) bids of losing bidders might actually be higher (lower) than the market prices (see Section 4.1). These bids are paradoxically rejected and can be hard to explain to participants. In this section, we measure the ratio of paradoxically rejected bids for diferent linear prices. Obviously, for SL and BL prices, only one side of the market can have paradoxically rejected bids, while with 1L prices, both buyers and sellers can be paradoxically rejected. Table 4 shows that this can be the case for up to 11% of the bids submitted for BL prices in the worst case.

Table 1 shows the ratio of paradoxically rejected bids, which was on average lower for 1L prices than for onesided linear prices (SL and BL). A regression yields an impact of 2.65% for BL, 2.71% for SL, and 1.74% for 1L prices. One explanation is that with BL and SL prices, the total gains from trade need to be distributed among one side of the market because of the strict budgetbalance constraint, while for the 1L prices, both sides of the market make a profit.

## 6. Summary

Can we have eficient combinatorial exchanges with linear and anonymous prices, or do such prices counter the eficiency of such markets? This is the key question of our paper. The theoretical worst-case analysis shows that the eficiency loss with linear prices can be 100%. However, these results might be too pessimistic for practical market design, as they describe small and specific situations. We were fortunate to have detailed data about a market for fishery access rights, which allowed us to conduct numerical experiments providing estimates for the welfare loss a market designer can expect in a realistic environment. This market is of independent interest, because very similar environments can be found for such markets in other regions of the world. It also provides a real-world grounding for our more general questions about the impact of pricing rules on eficiency.

Interestingly, our numerical experiments based on the data from the fishery rights exchange show that eficiency losses are low on average. While welfare losses for single linear prices in experiments are not negligible for smaller markets, they are very small with buyer-linear and seller-linear prices independent of the market size. In large markets, such as the market for fishery access rights, single linear prices also lead to only small eficiency losses. We also provide a formal model of a combinatorial exchange showing that the ineficiencies decrease with increasing market size and decreasing package size. The analytic results help us understand the main reasons for high average eficiency in the presence of linear and anonymous prices, and they are independent of the market for fishery access rights.

Obviously, single linear package prices constrain the allocation more than a market where linearity only needs to be enforced for one side of the market. With single linear package prices as they are defined in this paper, supply needs to equal demand in all share classes where there is a strictly positive market price. If sellers are willing to accept partial sales of a package bid, this can lead to eficiency gains, but such outcomes might be considered unfair and they are computationally very challenging. Buyer-linear and seller-linear prices allow for more flexibility and excess supply in cases where buyers are willing to pay more than the sellers ask for.

We also contribute to the literature on bid languages for combinatorial markets and find that the flexible bid language described in this paper positively impacts eficiency and computational tractability of the allocation and pricing problem, especially for single linear prices. We highlight dependencies between the flexibility of the bid language and the gains from trade, which are also relevant beyond the market for fishery access rights. In particular, the availability of quantity ranges that a buyer wants to purchase makes the problems easier to solve and allows for much larger allocation problems to be solved.

## 7. Conclusions

The design of electronic markets has been an important field of research in the management sciences. In particular, pricing and the design of bid languages have been key concerns adding to game-theoretical and purely algorithmic questions discussed in economics and computer science, respectively. Combinatorial exchanges are now possible because of the advances in information technology and efective methods to solve large integer programming problems. However, there is still little research on pricing and bid languages for combinatorial exchanges. This paper contributes to the growing information systems literature on electronic market design. This market design, and the environment, is interesting on its own, with applications also in other areas of the world and other domains.

Linear and anonymous prices are often a requirement in two-sided markets, motivated by equitable treatment of all buyers and sellers in a market. In combinatorial markets with package bids, it is typically impossible to compute Walrasian, that is, linear and anonymous, competitive equilibrium prices. Simple linear and anonymous prices are used on energy markets, but they can lead to welfare losses because they lead to additional constraints in the respective winner determination problems. In addition, there will be paradoxically rejected bids, that is, bids that are better than the market price but still rejected. So far, not much is known about combinatorial exchanges with linear prices, even though such prices are a requirement in many markets. For market designers, it is important to understand the order of magnitude of the eficiency losses due to linear and anonymous prices and the proportion of paradoxically rejected bids. We provide evidence that such markets are tractable for realistic problem sizes and that the eficiency losses due to linear prices are surprisingly small.

## Acknowledgments

The authors are grateful to the review team for very valuable comments.

## Appendix A. Proofs

## A.1. Proof of Proposition 1

Proof. Let us consider an allocation with strictly budgetbalanced buyer-linear prices: $\begin{array} { r } { \sum _ { s \in \mathcal { S } } A _ { s } x _ { s } = \sum _ { b \in \mathcal { B } } \dot { y _ { b } } p ^ { l _ { b } } } \end{array}$ . If in share class l at least one buy-bid is accepted, we charge a price equal to the lowest winning bid, and such a price must be individually rational for all winners, because other buy-side bids are at least as high. If there is no winning buy-side bid in a share class l, then all shares are bought by the government and thus can be zero-priced, that is, $p ^ { \check { l } } = 0 .$ 

## A.2. Proof of Proposition 3

Proof. Let $Y _ { 1 } , Y _ { 2 } , \ldots , Y _ { n }$ denote a sequence of independent and identically distributed random variables with common distribution function $F _ { Y } .$ . We define the ordered sample of buyer valuations $Y _ { 1 , n } \leq \cdots \leq Y _ { n , n }$ and call $Y _ { n - k + 1 , n }$ the kth upper order statistic. The distribution of the highest order statistic is $F _ { Y _ { n . n } ( y ) } = F _ { Y } ( y ) ^ { n }$ , and the density is $f _ { Y _ { n , n } } ( y ) =$ $n F _ { Y } ( y ) ^ { n - 1 } f _ { Y } ( y ) ^ { " }$ <sup>)</sup>. The distribution function of the jth upper order statistic (with $j = n - k + 1 )$ is

$$
F _ {Y _ {j, n}} (y) = \sum_ {r = j} ^ {n} {\binom {n} {r}} [ F _ {Y} (y) ] ^ {r} [ 1 - F _ {Y} (y) ] ^ {n - r},\tag{A.1}
$$

with a continuous distribution function $F _ { Y }$ (Casella and Berger 2002, p. 229).

Let us first look at P<sup>(</sup>DP<sup>)</sup>. The probability that one random variable A is larger than B (given that they are independent) can be written as $\begin{array} { r } { P [ A > B ] = \int _ { - \infty } ^ { \infty } \int _ { b } ^ { \infty } f _ { A } ( \dot { a } ) f _ { B } ( b ) } \end{array}$ da db <sup></sup> $\textstyle \int _ { - \infty } ^ { \infty } ( 1 - F _ { A } ( b ) ) f _ { B } ( b ) \mathrm { d } b$ . We can now compute the probability that the package value of the seller is less than the sum of the k upper order statistics. Unfortunately, there might not be a closed form solution for the sum or average of the k upper order statistics. Therefore, we use the highest order statistic $Y _ { n , n }$ as an upper bound and compute the probability that the highest order statistic of the buyers is higher than the seller’s value:

$$
\begin{array}{l} P (D P) = P (Y _ {n - k + 1, n} + \dots + Y _ {n, n} > k X) \leq P (Y _ {n, n} > X) \\ \quad = \int_ {- \infty} ^ {\infty} \int_ {x} ^ {\infty} f _ {Y _ {n, n}} (y) f _ {X} (x)   \mathrm{d} x   \mathrm{d} y \\ \quad = 1 - \int_ {- \infty} ^ {\infty} F _ {Y _ {n, n}} (x) f _ {X} (x)   \mathrm{d} x = 1 - \int_ {- \infty} ^ {\infty} F _ {Y} (x) ^ {n} f _ {X} (x)   \mathrm{d} x. \end{array}
$$

Next, we define P<sup>(</sup>LP<sup>)</sup>. With a single linear price for both buyers and sellers we need to have equality of supply and demand. This price can be at most at the value of the kth highest buyer:

$$
\begin{array}{l} P (L P) = 1 - \int_ {- \infty} ^ {\infty} F _ {Y _ {n - k + 1, n}} (x) f _ {X} (x)   \mathrm{d} x \\ \qquad = 1 - \int_ {- \infty} ^ {\infty} \sum_ {r = n - k + 1} ^ {n} \binom {n} {r} [ F _ {Y} (x) ] ^ {r} [ 1 - F _ {Y} (x) ] ^ {n - r} f _ {X} (x)   \mathrm{d} x \\ \qquad = 1 - \sum_ {r = n - k + 1} ^ {n} \binom {n} {r} \int_ {- \infty} ^ {\infty} [ F _ {Y} (x) ] ^ {r} [ 1 - F _ {Y} (x) ] ^ {n - r} f _ {X} (x)   \mathrm{d} x. \end{array}
$$

Now, if $f _ { Y } = f _ { X } ,$ , we can get the closed form expression of the upper bound for $P ( D P )$ :

$$
\begin{array}{l} P (D P) \leq 1 - \int_ {- \infty} ^ {\infty} F _ {Y} (x) ^ {n} f _ {Y} (x) \mathrm{d} x = 1 - \frac {1}{n + 1} \left(F _ {Y} (x)\right) ^ {n + 1} \Bigg | _ {- \infty} ^ {\infty} \\ = 1 - \frac {1}{n + 1}. \end{array} \tag {A.}\tag{A.2}
$$

We can also simplify $P ( L P )$ considerably with $f _ { Y } = f _ { X }$ . Note that $\textstyle \int _ { 0 } ^ { 1 } t ^ { k } ( 1 - t ) ^ { n - k } d t$ is a Eulerian integral of the first kind (Whittaker and Watson 1990), and its solution is the beta function $B ( k + 1 , n - k + 1 ) = k ! ( n - k ) ! / ( n + 1 ) ! = ( n + 1 ) ^ { - 1 } { \binom { n } { k } } ^ { - 1 }$ We can substitute $t = F _ { Y } ( x )$ and then ${ \mathrm { d } } t = f _ { Y } ( x ) { \mathrm { d } } x$ The bounds of the integral become $t ( 0 ) = 0$ and $t ( \infty ) = 1 \colon$

$$
\begin{array}{c} P (L P) = 1 - \sum_ {r = n - k + 1} ^ {n} \binom {n} {r} \int_ {0} ^ {1} t ^ {r} (1 - t) ^ {n - r} d t \\ = 1 - \sum_ {r = n - k + 1} ^ {n} \frac {1}{n + 1} = 1 - \frac {k}{n + 1}. \end{array}\tag{A.3}
$$

Consequently, $E [ l o s s ] = P ( D P ) - P ( L P ) \leq ( k - 1 ) / ( n + 1 )$

## A.3. Proof of Corollary 4

Proof. We draw on the proof for Proposition 4. We can write the following bound for the probability of a trade with discriminatory prices:

$$
\begin{array}{l} P (D P) \leq 1 - \int_ {a _ {X}} ^ {b _ {X}} F _ {Y} (x) ^ {n} f _ {X} (x) \mathrm{d} x \\ = 1 - \int_ {\max (a _ {X}, a _ {Y})} ^ {\min (b _ {X}, b _ {Y})} F _ {Y} (x) ^ {n} f _ {Y} (x) \frac {f _ {X} (x)}{f _ {Y} (x)} \mathrm{d} x - \int_ {\min (b _ {X}, b _ {Y})} ^ {b _ {X}} f _ {X} (x) \mathrm{d} x \\ = 1 - \frac {1}{n + 1} \frac {b _ {Y} - a _ {Y}}{b _ {X} - a _ {X}} F _ {Y} (x) ^ {n + 1} \Bigg | _ {\max (a _ {X}, a _ {Y})} ^ {\min (b _ {X}, b _ {Y})} - 1 + F _ {X} (\min (b _ {X}, b _ {Y})) \\ = F _ {X} (\min (b _ {X}, b _ {Y})) \\ - \frac {1}{n + 1} \frac {b _ {Y} - a _ {Y}}{b _ {X} - a _ {X}} [ F _ {Y} (\min (b _ {X}, b _ {Y})) ^ {n + 1} - F _ {Y} (\max (a _ {X}, a _ {Y})) ^ {n + 1} ]. \end{array}
$$

Here the first equality explores the fact that for $x > b _ { \gamma } ,$ $F _ { Y } ( x ) = 1$ . Thus, we split the integral into a sum of two integrals, where the second summand is simplified with $F _ { Y } ( \bar { x } ) ^ { n } = 1$ . We use the same method for the case with linear prices. Note that for $x \in [ \operatorname* { m i n } ( b _ { X } , b _ { Y } ) , b _ { Y } ]$ , the expression under the integral sign is zero for all $r < n \colon$

$$
\begin{array}{l} P (L P) = 1 - \sum_ {r = n - k + 1} ^ {n} \binom {n} {r} \int_ {a _ {X}} ^ {b _ {X}} [ F _ {Y} (x) ] ^ {r} [ 1 - F _ {Y} (x) ] ^ {n - r} f _ {X} (x)   \mathrm{d} x \\ \qquad = 1 - \sum_ {r = n - k + 1} ^ {n} \binom {n} {r} \int_ {\max (a _ {X}, a _ {Y})} ^ {\min (b _ {X}, b _ {Y})} [ F _ {Y} (x) ] ^ {r} [ 1 - F _ {Y} (x) ] ^ {n - r} \\ \qquad \cdot f _ {Y} (x) \frac {f _ {X} (x)}{f _ {Y} (x)}   \mathrm{d} x - \binom {n} {n} \int_ {\min (b _ {X}, b _ {Y})} ^ {b _ {X}} f _ {X} (x)   \mathrm{d} x \\ \qquad = 1 - \frac {b _ {Y} - a _ {Y}}{b _ {X} - a _ {X}} \sum_ {r = n - k + 1} ^ {n} \binom {n} {r} \int_ {\max (F _ {Y} (a _ {X}), 0)} ^ {\min (F _ {Y} (b _ {X}), 1)} t ^ {r} (1 - t) ^ {n - r}   \mathrm{d} t \\ \qquad - 1 + F _ {X} (\min (b _ {X}, b _ {Y})) \\ \qquad \geq F _ {X} (\min (b _ {X}, b _ {Y})) - \frac {b _ {Y} - a _ {Y}}{b _ {X} - a _ {X}} \sum_ {r = n - k + 1} ^ {n} \frac {1}{n + 1} \\ \qquad = F _ {X} (\min (b _ {X}, b _ {Y})) - \frac {b _ {Y} - a _ {Y}}{b _ {X} - a _ {X}} \frac {k}{n + 1}. \end{array}
$$

Note that the latter expression can be negative when $b _ { X }$ is close to $b _ { Y }$ :

$$
\begin{array}{l} E [ l o s s ] \leq F _ {X} (\min (b _ {X}, b _ {Y})) \\ \quad - \frac {1}{n + 1} \frac {b _ {Y} - a _ {Y}}{b _ {X} - a _ {X}} \\ \quad \cdot [ F _ {Y} (\min (b _ {X}, b _ {Y})) ^ {n + 1} - F _ {Y} (\max (a _ {X}, a _ {Y})) ^ {n + 1} ] \\ \quad - \max \bigg (0, F _ {X} (\min (b _ {X}, b _ {Y})) - \frac {b _ {Y} - a _ {Y}}{b _ {X} - a _ {X}} \frac {k}{(n + 1)} \bigg). \end{array}\tag{A.4}
$$

If $b _ { Y } \geq b _ { X } ,$ we can write a simple bound:

$$
\begin{array}{l} E [ \text { loss } ] \leq \frac {b _ {Y} - a _ {Y}}{b _ {X} - a _ {X}} \frac {1}{n + 1} \left[ k - F _ {Y} (b _ {X}) ^ {n + 1} + F _ {Y} (\max (a _ {X}, a _ {Y})) ^ {n + 1} \right] \\ \leq \frac {b _ {Y} - a _ {Y}}{b _ {X} - a _ {X}} \frac {k - 1}{n + 1}. \quad \square \end{array} \tag {A.5}
$$

## Appendix B. Unique Prices for Buyer-Linear and Seller-Linear Payments

In this appendix, we provide the mathematical programs for the minimization of paradoxically rejected bids for buyerlinear and seller-linear prices, before we describe the optimization problems to minimize prices in both cases.

## B.1. Minimization of Paradoxically Rejected Bids Seller-linear prices:

$$
\min \sum_ {s \in \mathscr {S}} o _ {s}
$$

(Min PRB SL WDP)

$$
o _ {s} \sum_ {l \in I _ {s}} Q _ {s} ^ {l} \bar {P} \geq \sum_ {l \in I _ {s}} Q _ {s} ^ {l} p ^ {l} - A _ {s}, \quad \forall s \in \mathscr {S}: x _ {s} ^ {*} = 0\tag{PRBS}
$$

$$
- \sum_ {s \in \mathcal {S}} \sum_ {l \in L} Q _ {s} ^ {l} p ^ {l} x _ {s} ^ {*} + \sum_ {b \in \mathcal {B}} y _ {b} ^ {*} D _ {b} = 0, \quad \forall l \in \mathcal {L},\tag{BB}
$$

$$
\sum_ {l \in L} Q _ {s} ^ {l} p ^ {l} \geq A _ {s}, \quad \forall s \in \mathscr {S}: x _ {s} ^ {*} = 1\tag{IRS}
$$

$$
p ^ {l} \geq 0,
$$

$$
o _ {s} \in \{0, 1 \}, \quad \forall s \in \mathcal {S}.
$$

Buyer-linear prices:

$$
\sum_ {b \in \mathcal {B}} o _ {b}
$$

(Min PRB BL WDP)

$$
o _ {b} D _ {b} \geq D _ {b} - p ^ {l}, \quad \forall b \in \mathcal {B}: y _ {b} ^ {*} = 0,\tag{PRBB}
$$

$$
- \sum_ {s \in \mathcal {S}} A _ {s} x _ {s} ^ {*} + \sum_ {b \in \mathcal {B}} y _ {b} ^ {*} p ^ {l _ {b}} = 0,\tag{BB}
$$

$$
p ^ {l} \leq D _ {b}, \quad \forall b \in \mathcal {B}: y _ {b} ^ {*} > 0,\tag{IRB}
$$

$$
p ^ {l} \geq 0,
$$

$$
o _ {b} \in \{0, 1 \}, \quad \forall b \in \mathcal {B}.
$$

## B.2. Price Minimization

Seller-linear prices:

$$
\min \sum_ {l \in \mathscr {L}} p ^ {l ^ {2}} \quad (\text { Unique   prices   SL   WDP })
$$

$$
\sum_ {b \in \mathscr {B}: l _ {b} = l} y _ {b} ^ {*} D _ {b} - \sum_ {s \in S} \sum_ {l \in \mathscr {L}} p ^ {l} x _ {s} ^ {*} = 0\tag{BB}
$$

$$
A _ {s} \geq \sum_ {l \in L} Q ^ {l _ {s}} p ^ {l}, \quad \forall s \in \mathscr {S}: x _ {s} ^ {*} = 0, o _ {s} ^ {*} = 0\tag{PRBS}
$$

$$
\sum_ {l \in L} Q _ {s} ^ {l} p ^ {l} \geq A _ {s}, \quad \forall s \in \mathscr {S}: x _ {s} ^ {*} = 1\tag{IRS}
$$

$$
p ^ {l} \geq 0.
$$

Buyer-linear prices:

$$
\min \sum_ {l \in \mathscr {L}} p ^ {l ^ {2}} \quad (\text { Unique   prices   BL   WDP })
$$

$$
\sum_ {b \in \mathcal {B}: l _ {b} = l} y _ {b} ^ {*} p ^ {l} - \sum_ {s \in \mathcal {S}} A _ {s} x _ {s} ^ {*} = 0\tag{BB}
$$

$$
p ^ {l} \geq D _ {b}, \quad \forall   b \in \mathscr {B}: y _ {b} ^ {*} = 0, o _ {b} ^ {*} = 0,\tag{PRBB}
$$

$$
p ^ {l} \leq D _ {b}, \quad \forall b \in \mathcal {B}: y _ {b} ^ {*} > 0
$$

$$
p ^ {l} \geq 0.\tag{IRB}
$$

Appendix C. Results of a Regression Analysis with Eficiency as the Dependent Variable

<table><tr><td></td><td>Estimate</td><td>Std. error</td><td>t value</td><td>Pr(&gt;|t|)</td></tr><tr><td>(Intercept)</td><td>1.0097</td><td>0.0053</td><td>189.62</td><td>0.0000</td></tr><tr><td> $\rho$ </td><td>0.0176</td><td>0.0018</td><td>-9.94</td><td>0.0000</td></tr><tr><td> $\Delta_{\mu}$ </td><td>-0.0412</td><td>0.0044</td><td>-9.28</td><td>0.0000</td></tr><tr><td> $\sigma$ </td><td>0.0458</td><td>0.0044</td><td>10.34</td><td>0.0000</td></tr><tr><td>BL</td><td>-0.0019</td><td>0.0013</td><td>-1.51</td><td>0.1312</td></tr><tr><td>SL</td><td>-0.0000</td><td>0.0013</td><td>-0.01</td><td>0.9957</td></tr><tr><td>1L</td><td>-0.0585</td><td>0.0013</td><td>-46.64</td><td>0.0000</td></tr><tr><td>f</td><td>-0.0195</td><td>0.0018</td><td>-11.01</td><td>0.0000</td></tr><tr><td> $\kappa$ </td><td>-0.0015</td><td>0.0025</td><td>-0.60</td><td>0.5478</td></tr></table>

## Appendix D. List of Symbols

D.1. Sets

$\mathcal { L }$ Set of share classes

$\mathcal { I }$ Set of auction participants

$\mathcal { I } _ { S }$ Set of sellers

$\mathcal { I } _ { B }$ Set of buyers

$\mathcal { S }$ Set of sell bids

B Set of buy bids

## D.2. Bid Parameters

$Q _ { s } ^ { l }$ Number of units to sell in bid $s \in \mathcal { S }$ for share class $l \in \mathcal { L }$

$A _ { s }$ Total price asked for package in bid $s \in \mathcal { S }$

$\bar { Y } _ { b }$ Maximum number of units that can be allocated to bid b <sup>∈</sup> B

$\underline { { Y } } _ { b }$ Minimum number of units that can be allocated to bid $b \in { \mathcal { B } }$

$D _ { b }$ Unit price quoted in bid $b \in { \mathcal { B } }$

$l _ { b }$ Share class quoted in bid $b \in { \mathcal { B } }$

## D.3. Main Variables

$x _ { s }$ Binary variable corresponding to bid $s \in \mathcal { S } ;$ 1 if s was accepted and 0 if not

$y _ { b }$ Integer variable, denoting number of units allocated to bid b <sup>∈</sup> B

$z _ { b }$ Binary variable, corresponding to bid $b \in { \mathcal { B } } ; 1$ if b was accepted and 0 if not

$p ^ { l }$ Continuous variable, denoting linear price for share class $l \in \mathcal { L }$

## D.4. Auxiliary Variables and Parameters

$\lambda _ { s } l$ Continuous variable, used for linearization of $x _ { s }$ and $p ^ { l }$ product; used in SL formulation

$u _ { b }$ Binary variable, has a value of 1 only if the corresponding bid $b \in { \mathcal { B } }$ is the wining bid with the lowest bid price; used in BL formulation

$\eta _ { b , h }$ Integer variable, used for linearization of $y _ { b }$ and $u _ { h }$ product for bids $b , h \in { \mathcal { B } } ;$ used in BL formulation $\delta ^ { l }$ Integer variable, denoting units acquired by auction organizers for zero price in share class $l \in \mathcal { L } ;$ used in 1L formulation

$k ^ { l }$ Binary variable, used to force zero price in share class $l \in \mathcal { L } ,$ , where $\delta ^ { l }$ is positive; used in 1L formulation

$o _ { s }$ Binary variable, which can have zero value only if the corresponding bid $s \in \mathcal { S }$ is not paradoxically rejected; used in PRB minimization formulations

$o _ { b }$ Binary variable that can have zero value only if the corresponding bid b <sup>∈</sup> B is not paradoxically rejected; used in PRB minimization formulations

$\bar { P } ^ { l }$ Parameter; determines the upper bound for price in share class $l \in \mathcal { L }$

## D.5. Notation Used in Section 4.3 and Appendix A

$G _ { D P }$ Gains from trade with discriminatory prices

$G _ { L P }$ Gains from trade with linear anonymous prices

k Package size

n Number of unit-demand buyers

X Random variable with a continuous probability density function $f _ { X } ( x )$ and a cumulative distribution function of $F _ { X } ( x ) .$ , representing the seller’s value per unit

Y Random variable with a continuous probability density function $f _ { Y } ( y )$ and a cumulative distribution function of $F _ { Y } ( y )$ , representing the buyer’s value per unit

P<sup>(</sup>DP<sup>)</sup> Probability of an eficiency-maximizing solution with discriminatory prices and nonnegative gains from trade

P<sup>(</sup>LP<sup>)</sup> Probability of an eficiency-maximizing solution with linear anonymous prices and nonnegative gains from trade

U<sup>(</sup>a, b<sup>)</sup> Uniform distribution with a being minimum and b being maximum value

$Y$ Random variable

$F _ { Y }$ Distribution function of random variable Y

$Y _ { n - k + 1 , n }$ kth upper order statistic

$U ( a , b )$ Uniform distribution with range <sup>[</sup>a, b<sup>]</sup>

## D.6. Bid Generator Parameter Notation

ρ Participation probability

α Probability that a participant will act as a seller; ${ 1 - \alpha }$ is the probability of being a buyer

$r _ { l }$ Revenue per share the bidder has in share class l $r _ { \mathrm { m a x } }$ Maximum revenue per share the bidder has among all possessions

f Probability for the buyer to submit a fixed bid, that is, bid where minimum and maximum units caps are equal

$\mu _ { s }$ Mean value of value distribution for a seller, $\mu _ { s } \geq 1$

$\sigma _ { s }$ Standard deviation of value distribution for a sel

$\mu _ { b }$ Mean value of value distribution for a buyer, $\mu _ { s } \le 1$

$\sigma _ { s }$ Standard deviation of value distribution for a buyer

$$
\Delta_ {\mu}
$$

$$
\Delta_ {\mu} = \mu_ {s} - \mu_ {b}
$$

## D.7. Experimental Result Notation

w¯ Mean social

$\sigma _ { w }$ Standard deviation for welfare loss

$\bar { \pi } _ { S }$ Mean seller payof ratio, that is, percentage of all

gains from trade that sellers get

<sup>¯</sup>t Mean computation time

$\sigma _ { t }$ Standard deviation for computation time

g¯ Mean MIP gap

max<sup>(</sup>g<sup>)</sup> Maximum MIP gap

e¯ Average ratio of paradoxically rejected bids

## Endnotes

<sup>1</sup> A diferent motivation for using combinatorial buy ofers in onesided auctions for fishing shares can be found in, for example, Iftekhar and Tisdell (2012), Innes et al. (2014).

<sup>2</sup> In assignment markets, where each participant is assigned at most one item, the solution to the winner-determination problem is always integral, and the dual variables for the market-clearing constraints can be interpreted as market prices (Shapley and Shubik 1971). In contrast, winner-determination problems in combinatorial exchanges are (nonconvex) integer programs, and such dual prices are not always possible (Gomory and Baumol 1960). Wolsey (1981) gives a description of integer programming duality and shows that price-functions are needed to achieve computable duals. Unfortunately, these dual price functions are dificult to interpret.

<sup>3</sup> Incentive compatibility means that submitted ofers truthfully reflect participants’ private information if others act truthfully (Bayes– Nash incentive compatibility) or irrespective of others’ behavior (dominant-strategy incentive compatibility). Individual rationality means that participation in the exchange does not lead to a loss. The exchange is eficient if it maximizes the total gains from trade. Budget balance requires that the exchange does not insert or extract money. <sup>4</sup> Farrell (1959) shows that the impact of nonconvexities diminishes as the number of market participants increases. The Shapley–Folkman theorem (Starr 1969) places an upper bound on the size of the nonconvexities and can be used to show existence of an approximate competitive equilibrium in large economies with nonconvexities. These results suggest that, under certain assumptions, (approximate) Walrasian prices may exist in large markets with nonconvex preferences (Azevedo et al. 2013). Unfortunately, the fisheries application and day-ahead energy markets (Meeus et al. 2009) do not fit these assumptions. More generally, some economists contend that the convexity assumptions underlying general equilibrium models are rarely satisfied, for example, Georgescu-Roegen (1979). In particular, goods are typically not divisible, and the resulting allocation problems are often nonconvex, which is outside the scope of general equilibrium theory (O’Neill et al. 2005).

<sup>5</sup> A natural question is whether there are restrictions on preferences such that Walrasian prices exist. Gul and Stacchetti (1999) showed that if the bidders’ utility functions satisfy the gross substitutes condition (Kelso and Crawford 1982), a Walrasian (competitive) equilibrium exists. The gross substitutes condition says that if the price of item Y increases, then the demand for item X either remains constant or increases, but does not decrease. Unfortunately, the condition does not allow for complements. Milgrom (2000) shows that an economy may not have a Walrasian equilibrium if at least one agent has preferences that are complementary and all the others have preferences that satisfy the gross substitutes condition. Bikhchandani and Mamer (1997) and Baldwin and Klemperer (2018) provide alternative characterizations for the existence of Walrasian prices.

<sup>6</sup> There has been significant interest in ascending (single-sided) combinatorial auctions with linear prices (Kwasnica et al. 2005, Bichler et al. 2009, Brunner et al. 2010, Schefel et al. 2011). Even in singlesided combinatorial auctions there are paradoxically rejected bids (Bichler et al. 2009), which we discuss in more detail in Section 4.3. There is a growing literature on algorithmic mechanism design and approximation mechanisms for combinatorial auctions, but this literature typically focuses on strategy-proof mechanisms and does not consider linear prices (Blumrosen and Nisan 2007).

<sup>7</sup> Day (2013) analyzes payment rules that satisfy core constraints and budget balance and are close to VCG payments. Alternative payment rules in combinatorial exchanges can be found in Parkes et al. (2001).

<sup>8</sup> An exception is the work of Lubin et al. (2008), who introduced an iterative mechanism for a combinatorial exchange with linear prices and a flexible tree-based bidding language. See also the work of Guo et al. (2012), who discuss bundle-trading markets and provide a computational analysis of how diferent market design factors afect eficiency. The design questions in their paper are complementary to the ones discussed in our paper.

<sup>9</sup> In logistics auctions, package bids are important for carriers, who have synergies for specific packages of lanes in a transportation network, but they are typically less pronounced on the side of the procurement organization, who just needs their entire demand satisfied.

## References

Adomavicius G, Gupta A (2005) Toward comprehensive real-time bidder support in iterative combinatorial auctions. Inform. Systems Res. 16(2):169–185.

Adomavicius G, Curley S, Gupta A, Sanyal P (2012) Efect of information feedback on bidder behavior in continuous combinatorial auctions. Management Sci. 58(4):811–830.

Arrow KJ, Debreu G (1954) Existence of an equilibrium for a competitive economy. Econometrica 22(3)265–290.

Azevedo EM, Weyl EG, White A (2013) Walrasian equilibrium in large, quasilinear markets. Theoret. Econom. 8(2):281–290.

Baldwin E, Klemperer P (2018) Understanding preferences: “Demand types,” and the existence of equilibrium with indivisibilities. Accessed September 14, 2018, http://dx.doi.org/ 10.2139/ssrn.2643086.

Bichler M, Shabalin P, Pikovsky A (2009) A computational analysis of linear price iterative combinatorial auction formats. Inform. Systems Res. 20(1):33–59.

Bichler M, Goeree J, Mayer S, Shabalin P (2014) Spectrum auction design: Simple auctions for complex sales. Telecomm. Policy 38(7):613–622.

Bikhchandani S, Mamer JW (1997) Competitive equilibrium in an exchange economy with indivisibilities. J. Econom. Theory 74(2):385–413.

Blumrosen L, Nisan N (2007) Combinatorial auctions. Nisa N, Roughgarden T, Tardos E, Vazirani VV, eds. Algorithmic Game Theory (Cambridge University Press, New York), 267–300.

Brunner C, Goeree JK, Holt CA, Ledyard JO (2010) An experimental test of flexible combinatorial spectrum auction formats. Amer. Econom. J.: Microeconomics 2(1):39–57.

Casella G, Berger RL (2002) Statistical Inference, Vol. 2 (Duxbury, Pacific Grove, CA).

Cason T, Kannan K, Siebert R (2011) An experimental study of information revelation policies in sequential auctions. Management Sci. 57(4):667–688.

Cramton PC, Shoham Y, Steinberg R, eds. (2006) Combinatorial Auctions, Vol. 475 (MIT Press, Cambridge, MA).

Day R (2013) The division of surplus in eficient combinatorial exchanges. Accessed September 14, 2018, http://dx.doi.org/ 10.2139/ssrn.2207067.

de Vries S, Vohra R (2003) Combinatorial auctions: A survey. INFORMS J. Comput. 15(3):284–309.

Farrell MJ (1959) The convexity assumption in the theory of competitive markets. J. Political Econom. 67(4):377–391.

Georgescu-Roegen N (1979) Methods in economic science. J. Econom. Issues 13(2):317–328.

Gomory RE, Baumol WJ (1960) Integer programming and pricing. Econometrica 28(3):521–550.

Green J, Lafont J-J (1977) Characterization of satisfactory mechanisms for the revelation of preferences for public goods. Econometrica 45(2):427–438.

Gul F, Stacchetti E (1999) Walrasian equilibrium with gross substitutes. J. Econom. Theory 87(1):95–124.

Guo Z, Koehler G, Whinston A (2012) A computational analysis of bundle trading markets design for distributed resource allocation. Inform. Systems Res. 23(3-part-1):823–843.

Iftekhar MS, Tisdell JG (2012) Comparison of simultaneous and combinatorial auction designs in fisheries quota market. Marine Policy 36(2):446–453.

Innes J, Thébaud O, Norman-López A, Little LR, Kung J (2014) Evidence of package trading in a mature multi-species ITQ market. Marine Policy 46(May):68–71.

Kelso AS, Crawford VP (1982) Job matching, coalition formation, and gross substitute. Econometrica 50(6):1483–1504.

Ketter W, Collins J, Gini M, Gupta A, Schrater P (2012) Real-time tactical and strategic sales management for intelligent agents guided by economic regimes. Inform. Systems Res. 23(4):1263–1283.

Kwasnica T, Ledyard JO, Porter D, DeMartini C (2005) A new and improved design for multi-objective iterative auctions. Management Sci. 51(3):419–434.

Lubin B, Juda AI, Cavallo R, Lahaie S, Shneidman J, Parkes DC (2008) ICE: An expressive iterative combinatorial exchange. J. Artificial Intelligence Res. 33:33–37.

McKenzie LW (1959) On the existence of general equilibrium for a competitive market. Econometrica 27(1)54–71.

Meeus L, Verhaegen K, Belmans R (2009) Block order restrictions in combinatorial electric energy auctions. Eur. J. Oper. Res. 196(3): 1202–1206.

Milgrom P (2000) Putting auction theory to work: The simultaneous ascending auction. J. Political Econom. 108(21):245–272.

Myerson RB, Satterthwaite MA (1983) Eficient mechanisms for bilateral trading. J. Econom. Theory 29(2):265–281.

Nemes V, Plott CR, Stoneham G (2008) Electronic BushBroker exchange: Designing a combinatorial double auction for native vegetation ofsets. Accessed September 14, 2018, http://dx.doi .org/10.2139/ssrn.1212202.

O’Neill RP, Sotkiewicz PM, Hobbs BF, Rothkopf MH, Stewart WR (2005) Eficient market-clearing prices in markets with nonconvexities. Eur. J. Oper. Res. 1(164):269–285.

Parkes DC, Kalagnanam J, Eso M (2001) Achieving budget-balance with Vickrey-based payment schemes in exchanges. Proc. 17th Internat. Joint Conf. Artificial Intelligence (Morgan Kaufman, San Francisco), 1161–1168.

Petrakis I, Ziegler G, Bichler M (2013) Ascending combinatorial auctions with allocation constraints: On game-theoretical and computational properties of generic pricing rules. Inform. Systems Res. 24(3):768–786.

Roberts DJ, Postlewaite A (1976) The incentives for price-taking behavior in large exchange economies. Econometrica 44(1): 115–127.

Rustichini A, Satterthwaite MA, Williams SR (1994) Convergence to eficiency in a simple market with incomplete information. Econometrica 62(5):1041–1063.

Schefel T, Pikovsky A, Bichler M, Guler K (2011) An experimental comparison of linear and nonlinear price combinatorial auctions. Inform. Systems Res. 22(2):346–368.

Shapley LS, Shubik M (1971) The assignment game I: The core. Internat. J. Game Theory 1(1):111–130.

Starr RM (1969) Quasi-equilibria in markets with non-convex preferences. Econometrica 37(1):25–38.

Van Vyve M (2011) Linear prices for non-convex electricity markets: Models and algorithms. Report, Center for Operations Research and Econometrics, Université catholique de Louvain, Louvainla-Neuve, Belgium.

Wang X, Kopfer H (2014) Collaborative transportation planning of less-than-truckload freight. OR Spectrum 36(2):357–380.

Whittaker ET, Watson GN (1990) A Course of Modern Analysis (Cambridge University Press, Cambridge, UK).

Wolsey LA (1981) Integer programming duality: Price functions and sensitivity analysis. Math. Programming 20(1):173–195.

Xia M, Koehler GJ, Whinston AB (2004) Pricing combinatorial auctions. Eur. J. Oper. Res. 154(1):251–270.
