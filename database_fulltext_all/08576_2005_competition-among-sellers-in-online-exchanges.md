---
otero_id: 8576
otero_key: "V7HARU3S"
title: "Competition Among Sellers in Online Exchanges"
authors: "Subhajyoti Bandyopadhyay; John M. Barron; Alok R. Chaturvedi"
year: "2005"
journal: "Information Systems Research"
doi: "10.1287/isre.1050.0043"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## 6SR

![](/api/attachments/V7HARU3S/fulltext/images/04c4346e2365b4128336bed70781a22d5608ed2f3d9ee591863a949bb0783473.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Competition Among Sellers in Online Exchanges

Subhajyoti Bandyopadhyay, John M. Barron, Alok R. Chaturvedi,

## To cite this article:

Subhajyoti Bandyopadhyay, John M. Barron, Alok R. Chaturvedi, (2005) Competition Among Sellers in Online Exchanges. Information Systems Research 16(1):47-60. http://dx.doi.org/10.1287/isre.1050.0043

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 2005 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/V7HARU3S/fulltext/images/d7aa9db7a2d72d0c4bc8b5fbd7a9257cbda71f0576381e604e38c556824a7a49.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Competition Among Sellers in Online Exchanges

Subhajyoti Bandyopadhyay

Warrington School of Business, University of Florida, Gainesville, Florida 32611, shubho.bandyopadhyay@cba.ufl.edu

John M. Barron, Alok R. Chaturvedi Krannert Graduate School of Management, Purdue University, West Lafayette, Indiana 47907 {barron@mgmt.purdue.edu, alok@mgmt.purdue.edu}

to join an exchange, the number of sellers who can qualify and participate in online exchanges is greatly increased. We model the competition between two sellers with different unit costs and production capacities responding to a buyer demand. The resulting mixed-strategy equilibrium shows that one of the sellers has a normal high price with random sales, while the other seller continuously randomizes its prices. It also brings out the inherent advantages that sellers with lower marginal costs or higher capacities have in joining these exchanges, and provides a theoretical basis for understanding the relative advantages of various types of sellers in such exchanges.

Key words: online exchanges; reverse auctions; pricing power; mixed-strategy equilibria History: Tridas Mukhopadhyay, Senior Editor; H. R. Rao, Associate Editor. This paper was received on December 20, 2002, and was with the authors 11 months for 2 revisions.

## Introduction

Online exchanges for business-to-business (or B2B) transactions have become ubiquitous in industries ranging from automotive to retailing.<sup>1</sup> The Wall Street Journal (Angwin 2003) mentions the remarkable turnaround of the B2B Internet commerce sector, and that U.S. businesses spent \$482 billion in B2B transactions, up 242% from two years earlier. The online research and consulting firm Jupiter Media Metrix predicts \$5.4 trillion in goods and services will be transacted online among businesses by 2006, and a more optimistic Gartner Group forecast estimates worldwide B2B commerce to swell to \$5.9 trillion by the end of 2004. Forrester Research indicates that in the third quarter of 2001, 49% of organizations that buy more than \$1 billion per year reported using an online auction, with most of them subsequently increasing their usage of these venues.

An example of a successful exchange is ChemConnect, a consortia-backed exchange connecting buyers and sellers in industries such as chemicals, plastics, pharmaceuticals, paper, and so on. In 2002, its transaction volume exceeded \$8.8 billion. Another prominently mentioned example is Covisint, the online marketplace formed by the Big Three automakers. In the first six months of 2001, the founders of Covisint had channeled \$33 billion, or 13% of their annual purchase transactions, through the exchange (Helper and MacDuffie 2001).<sup>2</sup> A research report by Roland Berger (2000), a specialized automotive industry consulting firm, estimates that 33% of the cost savings in the North American auto industry will come from purchase-related savings fueled by Internet technologies.

Three prominent and successful private exchanges that are worth mention in the present context are GE Global eXchange Services (GXS), with 100,000 trading partners (Tomak and Xia 2002), Dow Chemical Co. (which now conducts 15% of its business online, a five-fold increase over 2,000 levels) (Angwin 2003), and Wal-Mart, which started its own private exchange in 2001. Another growing trend is to use specialized B2B software for private auctions. For example, Gateway Inc. has extensively used Spend Management Solutions from Ariba, one of the largest B2B solutions providers, to procure its components from Asian manufacturers for its home electronics business.<sup>3</sup>

Carrier Corp., the world’s largest manufacturers of air conditioners and one of the pioneers of using online exchanges, quantified its own benefits of using this mechanism. By putting its requirements online through FreeMarkets, and thereby getting a larger number of sellers to bid for the requirements, the company realized average savings of 15% on the cost of components, amounting to more than \$100 million (Fast Company 2001) of savings in the year 2000. The company firmly believes that the online exchanges can be a powerful cost-cutting tool when there are several vendors from which to choose, especially in the current environment of worldwide sourcing for components in the manufacturing sector. ChemConnect provides the example of Sunoco Inc., a leading manufacturer and marketer of petroleum and petrochemical products, which expanded its universe of sellers by two and realized cost savings of 12%.<sup>4</sup>

B2B exchanges reduce transaction costs, add product and pricing transparency, generate market liquidity, and facilitate bidding by a broad spectrum of potential suppliers in a standardized platform (Zhu 2002). In this paper, we analyze the competition between sellers who are bidding for the business of large buyers. This sort of competition is common in online exchanges that are called “buy-centric markets” or “procurement hubs” in industry parlance. (All the previously mentioned exchanges are examples of such buy-centric markets.) Although raw materials and components seem to be natural candidates to be traded on such exchanges, as the example of Wal-Mart’s private exchange shows, any large buyer of relatively homogeneous goods will have significant interests in joining an exchange. This homogeneity might come about in two ways: (1) where the buyer firm is chiefly concerned with lowering costs of the final product so that price becomes the primary differentiator, and (2) where after meeting the other criteria for selection (quality control, delivery times, reliability, and so on), price remains as the surviving differentiator. Thanks to the open standards of these online technologies, the barrier to entry for a new seller has become very low, compared with the extremely costly interorganizational systems (or IOSs) that were common a few years back. One result is the increasing diversity of the sellers that compete for a request for proposal online.

Most B2B auctions are used to transact huge quantities of homogeneous goods (Katok and Roth 2004). We analyze the case of competition between heterogeneous sellers of a single raw material or component vying for business from a single large buyer within a buy-centric B2B exchange framework. We concentrate on the mechanism of a one-sided, sealed-bid reverse auction. We assume that open standards eliminate a capacity constraint in that all sellers combined can supply the entire demand. Individual firms, however, cannot fulfill the entire market’s demand. This means that although there is a competition between the firms to be the low-price bidder (for prices above a firm’s marginal cost), it is not as extreme as a

Bertrand game<sup>5</sup> that results in prices equal to marginal cost. As the nature of the equilibrium shows, however, there remains an incentive to be the lowprice bidder and to have the first invitation to supply a requirement.

Our prior analysis (Bandyopadhyay and Barron 2004) considers the competition among sellers with the same marginal costs of production and capacities. Although the analysis shows the basic nature of the equilibrium (for example, the existence of a mixedstrategy equilibrium for the sellers that randomize their prices in an interval), it does not consider the characteristics of equilibrium when sellers differ, a key feature of B2B exchanges because they allow participation by a variety of sellers. In this paper, we arrive at an explicit characterization of an equilibrium where the sellers have different marginal costs and capacities, and can affect changes to both these strategic variables to compete effectively in this new market environment. The results provide a theoretical basis for understanding the effect of these two variables in electronic transactions.

## Literature Review

Electronic exchanges can be thought of as intermediaries that bring together buyers and sellers. Intermediaries have been analyzed in the economics literature variously as time-saving agents, value-added agents, and experts (see, for example, Rubinstein and Wolinsky 1987, Biglaiser 1993, and Boyd and Prescott 1986). Bhargava et al. (2000) analyzes the aggregation benefit that consumers derive from having access to multiple providers through an intermediary.

The modern B2B electronic exchange can be considered under a broad class of technology called IOS, the most common among them being the electronic data interchange (EDI). Several papers have studied the effect of EDI (see, for example, Barua and Lee 1997, Riggins et al. 1994, Wang and Seidmann 1995, Zhu 1999, and Zhu and Weyant 2003). However, the modern-day exchange differs significantly from EDI systems in terms of unprecedented data transparency and open standards that make it easier for suppliers to join the exchange (Zhu 2004).

Zhu (2004) looks at the effect of information transparency in electronic markets. As the results of the analysis show, it is this information transparency that suppliers perceive as a threat to joining the online exchanges (Jap 2000). Conversely, the decreasing cost of hardware and software (an Internet-enabled personal computer and a secure web browser are perhaps the absolute minimum requirements) and the extensive use of open standards in developing the electronic exchanges of today have ensured the growth in B2B marketplaces. Dai and Kauffman (2003) argue that in contrast to closed extranets, which were popular among large organizations and their sellers, today’s electronic markets are open networks where sellers have reduced information on buyers.<sup>6</sup> In this context, the characteristics of other sellers become relatively more important in determining seller strategy. It is therefore important for the sellers to understand the dynamics of the competition in an online exchange, and the impact of different production costs and capacities of the sellers. Prior research has analyzed several variations of competition under capacity constraints. We refer to that research in the next section.

## Model Environment and Assumptions

Dai and Kauffman (2003) point out that, unlike closed extranets, open electronic markets expose sellers to increased competition from diverse competitors. It is this competition that we model in this paper. In the process, we look at a competitive game that is special in several respects. First, the demand for materials posted on the exchange will tend to be inelastic. The buyer decides on the quantity and the reservation price below which it is ready to buy the entire quantity.<sup>7</sup> Furthermore, any seller meeting the basic requirements of the buyer is qualified to bid.<sup>8</sup> With the advent of the online exchange, buyers put their requirements on the exchange only once, instead of contacting the sellers individually. Sellers look at this entire requirement, and then decide to quote their prices. The sellers are also given a date (usually several weeks in the future) by which they are expected to place their bids. Sellers bid their selling prices, all of which are opened at a later date. The seller with the lowest-bid price gets the first invitation to cater to the demand, followed by the seller with the secondlowest bid price, and so on, until the entire demand is met.<sup>9</sup>

From the modeling point of view, it is immaterial whether the sellers respond to an aggregate demand of several buyers (which might raise an antitrust issue), or one single demand from a buyer.<sup>10</sup> The entire requirement is auctioned to the sellers, and a lower-priced bidder has the first turn to satisfy any unfulfilled demand.<sup>11</sup>

With unlimited capacity, the sellers respond with a Bertrand competition in prices wherein the seller or sellers with the lowest marginal cost outbid the others.<sup>12</sup> This is not to the advantage of the sellers.

Kreps and Scheinkman (1983), and several variants of the original model, such as Allen et al. (1992), show that if sellers could limit capacity, then a quantity precommitment and Bertrand competition yield Cournot outcomes that have equilibrium prices above marginal cost. At the other end of the spectrum, if the total capacity of the sellers is so limited as to be less than the total demand, the sellers can sell their entire capacities at the buyer’s reservation price.<sup>13</sup>

Our model is different from either of these cases. It is realistic to think of sellers having limited capacities so that any one seller cannot meet market demand. In our setting, however, we add the condition that the aggregate output of the sellers exceeds total quantity demanded and that a firm sells all it can produce only if it is the low-price seller. That is, the lowest-priced seller sells to capacity, but a higherpriced seller only sells to a residual demand. Sellers, therefore, are pulled by two opposing forces; on the one hand, higher prices fetch higher margins, but on the other, higher prices bring about increased chances of being underbid by competition and thus selling a lesser amount.

Our analysis proceeds in three steps. First, we consider the equilibrium obtained when both the sellers have the same capacity and different marginal costs. We then repeat the analysis for the same marginal costs and different capacities. These two analyses provide the intuition behind the results of the model with asymmetric costs and capacities.

## The Model

Our earlier paper (Bandyopadhyay and Barron 2001) analyzes the equilibrium where two sellers have equal capacity k that is individually less than the buyer’s total requirement Q (the specific functional form of the demand is suggested in Varian 1980), but the combined capacity exceeds total demand so that 2k > Q > k. In such a setting, the lower-priced seller is invited first to sell the required quantity, and after it has supplied its total capacity k, the other seller can then sell the residual demand Q  k. Both sellers have a common fixed marginal cost of production, c. There exists a mixed-strategy equilibrium for this game (the existence of a mixed-strategy game with discontinuous payoffs is proved in Dasgupta and Maskin 1986), with both sellers randomizing their prices based on the probability distribution

$$
F (p) = \frac {(p - c) k - (r - c) (Q - k)}{(p - c) (2 k - Q)}\tag{1}
$$

between the interval $( p _ { 1 } , r )$ , where $p _ { 1 }$ is given by

$$
p _ {1} = \frac {(r - c) (Q - k)}{k} + c,\tag{2}
$$

and r is the buyer $\cdot \prime _ { \mathrm { { S } } }$ reservation price.

Because diversity among sellers is an important aspect of B2B exchanges, we now look at the generalized two-seller game where the sellers $i = 1 , 2 $ , can have different marginal costs or capacities, or both. We assume, without loss of generality, that $c _ { 1 } \leq c _ { 2 } ,$ and that $k _ { 2 } = \theta k _ { 1 }$ , where $\theta$ is any positive real number. We retain the assumption that $k _ { i } < Q , i = 1 , 2$ , but that

$$
\sum_ {i = 1, 2} k _ {i} = (1 + \theta) k _ {1} > Q.
$$

If sellers charge the same price, following the convention of Deneckere and Kovenock (1996), the one with the lower cost sells its capacity. If sellers charge the same price and sellers have the same cost, we arbitrarily have Seller 1 sell its capacity.

As Sinha (2000) points out, the use of reverse-auction bidding, XML mapping, and so on allow participants in these exchanges to see the price floors of the various players more easily than is possible in traditional markets. Therefore, the assumption of the various costs and capacities as common knowledge seems reasonable.

For seller $i ,$ define $p _ { i } ^ { * }$ as the minimum price it will set to sell its capacity $k _ { i }$ given the alternative of selling the residual $Q - k _ { i }$ at the maximum price r. Neither seller has an incentive to price below $p _ { i } ^ { * } = ( ( r - c _ { i } )$ $( Q - k _ { j } ) / k _ { j } ) + c _ { i } ,$ which we call the seller’s indifference price.

Seller 1, the low-cost seller, will have $p _ { 1 } ^ { * } < p _ { 2 } ^ { * }$ if and only if

$$
(c _ {1} - c _ {2}) ((Q - (1 + \theta) k _ {1}) / k _ {1}) > (1 - \theta) r.\tag{3}
$$

If the two sellers have the same capacity $( \theta = 1$ , such that $k _ { 1 } = k _ { 2 } = k )$ , then Seller 1 will have a lower minimum price $( p _ { 1 } ^ { * } < p _ { 2 } ^ { * } )$ , given that the residual demand is less than capacity $( 2 k > Q > k )$ . If the two sellers have the same cost $( c _ { 1 } = c _ { 2 } = c )$ , then the seller with the higher capacity will have a lower minimum price. Below we reconsider the equilibrium with heterogeneous sellers. We begin our analysis by focusing on the case where capacities are identical $( k _ { 1 } = k _ { 2 } = k )$ but Seller 1 has a lower marginal cost $\left( c _ { 1 } < c _ { 2 } \right)$

The analysis extends the existence results of Deneckere and Kovenock (1996), which focuses on how the costs or capacity differences can lead to different characterizations of equilibrium—pure strategy versus mixed—in a Bertrand-Edgeworth framework. Our specification of the functional form of the demand allows us to present explicit solutions for the mixed-strategy equilibrium price distributions of heterogeneous sellers who differ in their marginal costs as well as production capacities. These explicit solutions allow one to generate testable implications regarding the effect of changes in the magnitude of cost or capacity differences on parameters of the distributions. In doing so, we offer specific guidance to researchers pursuing empirical analysis in this area. In addition, our explicit results for the special cases of cost differences only and capacity differences only provide the intuition behind the general theory, and thus make the general theory more accessible.

## Heterogeneity in Cost

We first establish the general character of the equilibrium, if it exists, as a mixed-strategy equilibrium. Thus we have the following proposition.

Proposition 1. There can be no pure strategy in prices.

Suppose the low-cost seller (Seller 1) charges a single price. In this case, the best response of the highcost seller (Seller 2) is to charge a price an infinitesimal amount  lower and sell to capacity to obtain the highest profits if the price is in the interval $( p _ { 2 } ^ { * } , r ]$ , or if the price is equal to or below $p _ { 2 } ^ { * } ,$ charge a price equal to the maximum price r and sell the residual demand to obtain the highest profits. Now suppose the highcost seller charges a single price. In this case, the best response of the low-cost seller is to charge the same price and sell to capacity to obtain the highest profits if the price is in the interval $[ p _ { 1 } ^ { * } , r ]$ . If the price is below $p _ { 1 . } ^ { * }$ , the best response of the low-cost seller to charge a price equal to the maximal price r and sell the residual demand to obtain the highest profits.<sup>14</sup>

At any set of prices $( p _ { 1 } , p _ { 2 } )$ set by the two sellers, the above characterization of the best response for each seller ensures that at least one seller would seek to change the price. In particular, any time the low-cost seller matches the high-cost seller’s price, the high-cost seller has the incentive to charge a different price. Thus, there is no pure-strategy equilibrium. Let the mixed strategy in prices for seller i be represented by $F _ { i } ( p )$

We now use the ordering of the $p _ { i } ^ { * }$ to present a key feature of the mixed-strategy equilibrium: The lower support for both sellers is equal to the higher of the two indifference prices.

Proposition 2. $I f p _ { i } ^ { * } < p _ { j } ^ { * }$ , the minimum support price for $F _ { i } ( p ) , \ i = 1 , 2 ,$ , is the higher of the two indifference prices $( p _ { j } ^ { * } )$

The above follows from the fact that seller i has no incentive to price below $p _ { i } ^ { * }$ , the seller’s indifference price, because the seller always have the higher-profit alternative of selling at least to residual demand at price r. This $p _ { i } ^ { * }$ is the price at which the seller i makes the same profit by supplying its entire capacity as by supplying the residual demand at r.

Proposition 3. For any $p \in ( p ^ { * } , r ) , F _ { i } ( p )$ is strictly increasing.

If this is not the case, let there be an interval $( p ^ { \prime } , p ^ { \prime \prime } )$ where $f ( p ) = 0$ . For any $\hat { p }$ where $p ^ { \prime } < \hat { p } < p ^ { \prime \prime } ,$ , seller i can get the same outcome of either selling to capacity $k _ { i } ,$ or by selling the residual $( Q - k _ { j } ) _ { \ l }$ , as by pricing at the lower $p ^ { \prime } ,$ , but get a higher payoff.

We now provide a characterization of equilibrium for the case of different costs $\left( c _ { 1 } < c _ { 2 } \right)$ but identical capacities $( k _ { 1 } = k _ { 2 } = k )$ when $p _ { 1 } ^ { * } < p _ { 2 } ^ { * }$ . Although the proposed characterization is proved to be a valid and plausible equilibrium of the game $G ( k _ { 1 } , k _ { 2 } , c _ { 1 } , c _ { 2 } )$ there might be other Nash equilibria to the game.

We denote the profit of any seller i at a price $p$ to be $\Pi _ { i } ( p )$ . The profit realized by the seller if it wins the bid at price $p$ (an event we call a success) is given by $\Pi _ { s i } ( p )$ , whereas the profit realized by the seller if it loses the bid at price $p$ (a failure) is given by $\Pi _ { f i } ( p )$ In general, if a mixed-strategy equilibrium exists, it must provide for each seller identical profits at all prices charged. We now have the following characterization of the equilibrium price density functions. For seller $i ,$ profits at all prices must equal the profit level at $r ,$ such that

$$
\Pi_ {i} (p) = \Pi_ {i} (r), \quad i = 1, 2,\tag{4}
$$

where

$$
\Pi_ {i} (p) = \Pi_ {s i} (p) (1 - F _ {j} (p)) + \Pi_ {f i} (p) F _ {j} (p),\tag{5}
$$

$$
\Pi_ {s i} (p) = (p - c _ {i}) k,\tag{6}
$$

$$
\Pi_ {f i} (p) = (p - c _ {i}) (Q - k),\tag{7}
$$

$$
\Pi_ {1} (r) \equiv \Pi_ {s 1} (r) (1 - F _ {2} (r)) + \Pi_ {f 1} (r) F _ {2} (r),\tag{8}
$$

and

$$
\Pi_ {2} (r) \equiv \Pi_ {f 2} (r).\tag{9}
$$

Proposition 4. If a mixed-strategy equilibrium exists, the pricing strategy of the low-cost seller, Seller 1, is defined by a continuous distribution over the range $[ p _ { 2 } ^ { * } , r ]$ with no $\dot { m } a s s ^ { 1 5 }$ at any price. High-cost Seller $2 \mathit { ^ { \prime } s }$ pricing strategy is also defined by a continuous distribution over the range $[ p _ { 2 } ^ { * } , r ]$ , but Seller 2 now places a positive mass at the upper bound of the distribution r.

The above characterization has Seller 1’s pricing strategy similar to the characterization we obtained for the symmetric case. However, unlike the symmetric case, Seller $2 ^ { \prime } \mathrm { s }$ pricing strategy now has first-order stochastic dominance over Seller 1’s pricing strategy, such that $F _ { 2 } ( p ) < F _ { 1 } ( p )$ for all $p < r .$ . The interpretation of this outcome is that the high-cost seller has a normal price equal to the $r ,$ but engages in random sales. The low-cost seller engages in sales (price below r) almost always, and thus is more likely to sell to capacity.

A key feature of the above equilibrium, a positive mass at r for the high-cost seller, ensures profits for the low-cost seller at r that exceed what could be obtained by simply selling to the residual demand. The higher profits for Seller 1 are achieved with a mass by Seller 2 at r, because there now exists a positive probability that Seller 1 will not be the highpriced seller at $r ,$ and thus (as the low-cost producer), can sell capacity at r with positive probability. This higher level of profits for the low-cost seller holds at all other prices as well, and in particular at the lower bound $p _ { 2 } ^ { * } ,$ given that $p _ { 1 } ^ { * } < p _ { 2 } ^ { * }$

Using (5) through (9), we therefore have

$$
F _ {1} (p) = \frac {\Pi_ {s 2} (p) - \Pi_ {f 2} (r)}{\Pi_ {s 2} (p) - \Pi_ {f 2} (p)}\tag{10}
$$

and

$$
F _ {2} (p) = \frac {\Pi_ {s 1} (p) - \Pi_ {f 1} (r) - (1 - F _ {2} (r)) (\Pi_ {s 1} (r) - \Pi_ {f 1} (r))}{\Pi_ {s 1} (p) - \Pi_ {f 1} (p)}.\tag{11}
$$

To assume identical profits for the high-cost seller at all prices in the range $[ p _ { 2 } ^ { * } , r ]$ , the distribution of prices for the low-cost Seller 1 must take the form

$$
\begin{array}{c} F _ {1} (p) = \frac {\Pi_ {s 2} (p) - \Pi_ {f 2} (r)}{\Pi_ {s 2} (p) - \Pi_ {f 2} (p)} \\ F _ {1} (p) = 1 - \frac {(r - p) (Q - k)}{(p - c _ {2}) (2 k - Q)}. \end{array}\tag{12}
$$

Note that $F _ { 1 } ( r ) = 1$ . Given $p _ { 2 } ^ { * } = ( ( r - c _ { 2 } ) ( Q - K ) / K ) + c _ { 2 } ,$ at $F _ { 1 } ( p _ { 2 } ^ { * } )$ we have

$$
F _ {1} (p _ {2} ^ {*}) = 0.\tag{13}
$$

The above distribution for Seller 1 is similar to the equilibrium distribution characterization in the symmetric case. However, that is not the case for Seller 2. Recall that Seller 2 places mass places at r to ensure that the profits for Seller 1 at r equal those at p∗. Noting that $\Pi _ { 1 s } ( p _ { 2 } ^ { * } ) = ( p _ { 2 } ^ { * } - c ) k$ , we thus have the following condition:

$$
\Pi_ {1 s} (p _ {2} ^ {*}) = \Pi_ {1} (r),\tag{14}
$$

which determines that $1 - F _ { 2 } ( r ) > 0 .$ . The mass the high-cost seller places on the highest price r to ensure that the low-cost seller achieves profits commensurate with profits at the lowest price p∗ given that $p _ { 2 } ^ { * } > p _ { 1 } ^ { * }$ implies $\Pi _ { s 1 } ( p _ { 2 } ^ { * } ) > \Pi _ { s 1 } ( p _ { 1 } ^ { * } )$

We thus have two conditions that define the distribution of prices for Seller 2. The first is derived from the equal-profit condition for Seller 1 at any p given the potential for a mass point at r for Seller 2:

$$
\begin{array}{c} F _ {2} (p) = \frac {\Pi_ {s 1} (p) - \Pi_ {f 1} (r) - (1 - F _ {2} (r)) (\Pi_ {s 1} (r) - \Pi_ {f 1} (r))}{\Pi_ {s 1} (p) - \Pi_ {f 1} (p)} \\ F _ {2} (p) = 1 - \frac {(r - p) (Q - k)}{(p - c _ {1}) (2 k - Q)} - \frac {(1 - F _ {2} (r)) (r - c _ {1})}{(p - c _ {1})}. \end{array}\tag{15}
$$

To determine the mass as $r \ ( 1 - F _ { 2 } ( r ) > 0 )$ , we then use the condition that profits for Seller 1 are the same at r and at the indifference price for Seller 2:

$$
\begin{array}{c} \Pi_ {1 s} (p _ {2} ^ {*}) = \Pi_ {1} (r) \\ (p _ {2} ^ {*} - c _ {1}) k = (r - c _ {1}) k (1 - F _ {2} (r)) + (r - c _ {1}) (Q - k) F _ {2} (r) \\ \Rightarrow F _ {2} (r) = \frac {(r - p _ {2} ^ {*}) k}{(2 k - Q) (r - c _ {1})}. \end{array} \tag {1.6}\tag{16}
$$

Given $p _ { 1 } ^ { * } = ( ( r - c _ { 1 } ) ( Q - k ) / k ) + c _ { 1 } < p _ { 2 } ^ { * } ,$ we can rearrange this expression to obtain $r - p _ { 1 } ^ { * } = ( ( r - c _ { 1 } )$ $( 2 k - Q ) / k )$ . Substituting into the above, we have

$$
F _ {2} (r) = (r - p _ {2} ^ {*}) / (r - p _ {1} ^ {*}).\tag{17}
$$

It follows that, given $p _ { 2 } ^ { * } > p _ { 1 } ^ { * } ,$ it is the case that $F _ { 2 } ( r ) < 1$

Now we can obtain a general expression for the price distribution of the high-cost seller (Seller 2). Substituting the expression for $F _ { 2 } ( r )$ obtained from condition (17) into condition (15) as well as the expressions for profits when a sale is or is not successful (Equations (6) and (7)), we have

$$
\begin{array}{c} F _ {2} (p) = 1 - \frac {(r - p) (Q - k)}{(p - c _ {1}) (2 k - Q)} - \frac {(r - c _ {1})}{(p - c _ {1})} \\ + \frac {(r - p _ {2} ^ {*}) k}{(p - c _ {1}) (2 k - Q)}, \end{array}\tag{18}
$$

where $p _ { 2 } ^ { \ast } = ( ( r - c _ { 2 } ) ( Q - k ) / k ) + c _ { 2 }$ . Substituting in the expression for $p _ { 2 } ^ { * } ,$ we obtain

$$
F _ {2} (p) = 1 - \frac {(r - p) (Q - k)}{(p - c _ {1}) (2 k - Q)} - \frac {(c _ {2} - c _ {1})}{(p - c _ {1})}.\tag{19}
$$

Note that if $c _ { 1 } = c _ { 2 } ,$ then at $r , \ F _ { 2 } ( r ) = 1$ and there we have the symmetric outcome, with neither seller placing positive mass at r. However, given $c _ { 1 } < c _ { 2 }$

we have

$$
F _ {2} (r) = 1 - \frac {(c _ {2} - c _ {1})}{(p - c _ {1})} <   1.\tag{20}
$$

Thus, in summary, if a mixed-strategy equilibrium exists, the characterization of the distribution functions for the high- and low-cost sellers are given by Equations (12) and (19), respectively.

We now turn to the case where sellers differ in capacity rather than in cost.

## Heterogeneity in Capacity

Consider the case where $c _ { 1 } = c _ { 2 } = c$ but $k _ { 1 } \neq k _ { 2 } .$ . Without loss of generality, let $k _ { 2 } = \theta k _ { 1 } ,$ with $\theta < 1$ , such that Seller 1 has the larger capacity. Recall that if the two sellers have the same cost, then the seller with the higher capacity will have a lower minimum price, which means that $p _ { 1 } ^ { * } < p _ { 2 } ^ { * }$ . As before, and arguing similarly, we focus on a mixed-strategy equilibrium, with each seller’s distribution of prices defined over the common, continuous range p∗ r. We obtain the following proposition.

Proposition 5. If a mixed-strategy equilibrium exists, the pricing strategy of high-capacity Seller 1 is defined by a continuous distribution over the range $[ p _ { 2 } ^ { * } , r ]$ with no mass at any price. Low-capacity Seller 2’s pricing strategy is also defined by a continuous distribution over the range $[ p _ { 2 } ^ { * } , r ] ,$ , but Seller 2 now places a positive mass at the upper bound of the distribution r.

The above characterization has Seller 1’s pricing strategy similar to the one obtained for heterogeneous costs, but now the seller with the larger capacity behaves similar to the low-cost seller, whereas the seller with the smaller capacity behaves similar to the high-cost seller. We thus have a similar interpretation of this outcome: The low-capacity seller has a normal price equal to the r, but engages in random sales. The high-capacity seller almost always engages in sales (price below r) and thus is more likely to sell to capacity.

We now have the following characterization of the equilibrium price density functions. As before, if a mixed-strategy equilibrium exists, it must provide identical profits for each seller at all prices. To assume identical profits for the low-capacity seller at all prices in the range p∗ r, the distribution of prices for the high-capacity Seller 1 must takes the form

$$
\begin{array}{c} F _ {1} (p) = \frac {\Pi_ {s 2} (p) - \Pi_ {f 2} (r)}{\Pi_ {s 2} (p) - \Pi_ {f 2} (p)} \\ = \frac {- (r - p) (Q - k _ {1}) + (p - c) (Q - k _ {1} - k _ {2})}{(p - c) (Q - k _ {1} - k _ {2})} \\ F _ {1} (p) = 1 - \frac {(r - p) (Q - k _ {1})}{(p - c) (Q - k _ {1} - k _ {2})}. \end{array}\tag{21}
$$

Note that $F _ { 1 } ( r ) = 1$ . Given $p _ { 2 } ^ { * } = ( ( r - c ) ( Q - k _ { 1 } ) / k _ { 2 } ) + c ,$ at $F _ { 1 } ( p _ { 2 } ^ { * } )$ we have

$$
\begin{array}{c} F _ {1} (p _ {2} ^ {*}) = 1 - \frac {(r - c) (Q - k _ {1}) - (r - c) (Q - k _ {1}) (Q - k _ {1}) / k _ {2}}{((r - c) (Q - k _ {1}) / k _ {2}) (Q - k _ {1} - k _ {2})} \\ F _ {1} (p _ {2} ^ {*}) = 0. \end{array}
$$

The above distribution for Seller 1 is similar to the equilibrium distribution characterization in the symmetric case. However, that is not the case for Seller 2. Recall that for Seller 2 it is necessary to place mass at r to ensure that the profits for Seller 1 at r equal its profits at $p _ { 2 } ^ { * }$ . Noting that $\Pi _ { 1 s } ( p _ { 2 } ^ { * } ) = ( p _ { 2 } ^ { * } - c ) k _ { 1 }$ , we thus have the following condition:

$$
\Pi_ {1 s} (p _ {2} ^ {*}) = \Pi_ {1} (r),
$$

which determines $1 - F _ { 2 } ( r ) > 0$ . The mass the lowcapacity seller places on the highest price r to ensure the high-capacity seller achieves profits commensurate with profits at the lowest price p∗ given that $p _ { 2 } ^ { * } > p _ { 1 } ^ { * }$ , implies that $\Pi _ { s 1 } ( p _ { 2 } ^ { * } ) > \Pi _ { s 1 } ( p _ { 1 } ^ { * } )$

We thus have two conditions that define the distribution of prices for Seller 2. The first is derived from the equal-profit condition for Seller 1 at any p given the potential for a mass point at r for Seller 2:

$$
F _ {2} (p) = \frac {\Pi_ {s 1} (p) - \Pi_ {f 1} (r) - (1 - F _ {2} (r)) (\Pi_ {s 1} (r) - \Pi_ {f 1} (r))}{\Pi_ {s 1} (p) - \Pi_ {f 1} (p)}\tag{22}
$$

$$
F _ {2} (p) = 1 - \frac {(r - p) (Q - k _ {2})}{(p - c) (k _ {1} + k _ {2} - Q)} - \frac {(1 - F _ {2} (r)) (r - c)}{(p - c)}.\tag{23}
$$

To determine the mass as $r \ ( 1 - F _ { 2 } ( r ) > 0 )$ , we then use the condition that profits for Seller 1 are the same at r and at the indifference price for Seller 2:

$$
\begin{array}{c} \Pi_ {1 s} (p _ {2} ^ {*}) = \Pi_ {1} (r) \\ (p _ {2} ^ {*} - c) k _ {1} = (r - c) k _ {1} (1 - F _ {2} (r)) + (r - c) (Q - k _ {2}) F _ {2} (r) \\ F _ {2} (r) = (r - p _ {2} ^ {*}) k _ {1} / ((k _ {1} + k _ {2} - Q) (r - c)). \end{array}\tag{24}
$$

Given $p _ { 1 } ^ { * } = ( ( r - c ) ( Q - k _ { 2 } ) / k _ { 1 } ) + c < p _ { 2 } ^ { * } .$ , we can rearrange this expression for $p _ { 1 } ^ { * }$ to obtain $r - p _ { 1 } ^ { * } =$ $( ( r - c ) ( k _ { 1 } + k _ { 2 } - Q ) / k _ { 1 } )$ . Substituting into the above, we have

$$
F _ {2} (r) = \left(r - p _ {2} ^ {*}\right) / \left(r - p _ {1} ^ {*}\right).\tag{25}
$$

It follows that given $p _ { 2 } ^ { * } > p _ { 1 } ^ { * } , F _ { 2 } ( r ) < 1$

Now we can obtain a general expression for the price distribution of the high-cost seller (Seller 2). Substituting the expression for $F _ { 2 } ( r )$ obtained from Equation (25) into (23), we have

$$
\begin{array}{c} F _ {2} (p) = 1 - \frac {(r - p) (Q - k _ {2})}{(p - c) (k _ {1} + k _ {2} - Q)} - \frac {(r - c)}{(p - c)} \\ + \frac {(r - p _ {2} ^ {*}) k _ {1}}{(p - c) (k _ {1} + k _ {2} - Q)}, \end{array}\tag{26}
$$

where $p _ { 2 } ^ { * } = ( ( r - c ) ( Q - k _ { 1 } ) / k _ { 2 } ) + c$ . Substituting in the expression for $p _ { 2 } ^ { * } ,$ we obtain

$$
\begin{array}{c} F _ {2} (p) = 1 - \frac {(r - p) (Q - k _ {2})}{(p - c) (k _ {1} + k _ {2} - Q)} - \frac {(r - c)}{(p - c)} \\ + \frac {(r - c) k _ {1} - (r - c) (Q - k _ {1}) k _ {1} / k _ {2}}{(p - c) (k _ {1} + k _ {2} - Q)} \end{array}\tag{27}
$$

$$
F _ {2} (p) = 1 - \frac {(r - p) (Q - k _ {2})}{(p - c) (k _ {1} + k _ {2} - Q)} - \frac {(r - c) (k _ {1} - k _ {2})}{(p - c) k _ {2}}.
$$

Note that if $k _ { 1 } = k _ { 2 }$ , then at $r , F _ { 2 } ( r ) = 1$ and we have the symmetric outcome, with neither seller placing positive mass at r. However, given $k _ { 1 } > k _ { 2 } ,$ we have

$$
F _ {2} (r) = 1 - \frac {(k _ {2} - k _ {1}) (r - c)}{(p - c)} <   1.\tag{28}
$$

Thus, in summary, if a mixed-strategy equilibrium exists, the characterization of the distribution functions for the high- and low-capacity sellers is given by (21) and (27), respectively.

## Heterogeneity in Both Costs and Capacity

Finally, consider the case where $c _ { 1 } \neq c _ { 2 }$ and $k _ { 1 } \neq k _ { 2 } ,$ , so the sellers differ in both costs and capacities. Unlike the previous two cases, the relative values of the indifference prices depend on both $c _ { i }$ and $k _ { i } ,$ and being either the low-cost or the high-capacity seller does not inherently determine the lower of the indifference prices, although being the lower-cost or the highercapacity seller makes it relatively easier to have a lower indifference price. However, note that we can still define the higher of the indifference prices as minimum of the support of the strategies of both sellers. As before, we focus on a mixed-strategy equilibrium, with each seller’s distribution of prices defined over the common range p∗ r. We obtain the following proposition.

Proposition 6. If a mixed-strategy equilibrium exists, the pricing strategy of the seller with the lower indifference price (that we call $P _ { L } )$ is defined by a continuous distribution over the range p∗ r with no mass at any price. The other seller (or $P _ { H } )$ has a pricing strategy that is also defined by a continuous distribution over the range $[ p _ { 2 } ^ { * } , r ]$ but $P _ { H }$ now places a positive mass at the upper bound of the distribution $( r )$ . In the equations that follow, the $s u b \_$ scripts H and L refer to sellers $P _ { H }$ and $P _ { L } ,$ , respectively.

We can easily show that

$$
p _ {L} ^ {*} = \frac {(r - c _ {L}) (Q - k _ {H})}{k _ {L}} + c _ {L}, \quad \text { and }\tag{29}
$$

$$
p ^ {*} = p _ {H} ^ {*} = \frac {(r - c _ {H}) (Q - k _ {L})}{k _ {H}} + c _ {H}.\tag{30}
$$

If a mixed-strategy equilibrium exists, it must provide identical profits for each seller at all prices charged. To assume identical profits for $P _ { H }$ at all prices in the range $[ p _ { 2 } ^ { * } , r ]$ , the distribution of prices for $P _ { L }$ must take the form

$$
\begin{array}{r} F _ {L} (p) = \frac {\Pi_ {s H} (p) - \Pi_ {f H} (r)}{\Pi_ {s H} (p) - \Pi_ {f H} (p)} \\ = \frac {(p - c _ {H}) k _ {H} - (r - c _ {H}) (Q - k _ {L})}{(p - c _ {H}) (k _ {L} + k _ {H} - Q)}. \end{array}\tag{31}
$$

(32)

Note that $F _ { L } ( p ^ { * } ) = 0 ,$ , and $F _ { L } ( r ) = 1$ . For $P _ { H }$ to develop a best response to the above response of $P _ { L } ,$ , it is necessary to place mass at r to ensure that the profits of $P _ { L }$ at r is equal to the profits at $p ^ { * }$ . With $\Pi _ { L s } ( p _ { H } ^ { * } ) =$ $( p _ { H } ^ { * } - c ) k _ { L } ,$ we thus have the following condition:

$$
\Pi_ {L s} (p _ {H} ^ {*}) = \Pi_ {L} (r).\tag{33}
$$

Equation (33) ensures that $P _ { H }$ places mass at $r ,$ which in turn ensures that $P _ { L }$ achieves profits commensurate with profits at the lowest price $p _ { 2 } ^ { * }$ (because $p _ { H } ^ { * } > p _ { L } ^ { * }$ implies $\Pi _ { s L } ( p _ { H } ^ { * } ) > \Pi _ { s L } ( p _ { L } ^ { * } ) )$

We thus have two conditions that define the distribution of prices for Seller 2. The first is derived from

Figure 1 Graph of $F _ { \cal H } ( p )$ and $F _ { L } ( p )$

$$
\begin{array}{r l} F _ {H} (p) & = \frac {\Pi_ {s L} (p) - \Pi_ {f L} (r) - (1 - F _ {H} (r)) (\Pi_ {s L} (r) - \Pi_ {f L} (r))}{\Pi_ {s L} (p) - \Pi_ {f L} (p)} \\ F _ {L} (p) & = \frac {\Pi_ {s H} (p) - \Pi_ {f H} (r)}{\Pi_ {s H} (p) - \Pi_ {f H} (p)} \\ 1 - F _ {H} (r) & = \frac {(r - p _ {H} ^ {*})}{(r - p _ {L} ^ {*})} \\ p ^ {*} & = \frac {1}{p ^ {*}} \end{array}
$$

the equal profit condition for Seller 1 at any p, given the potential for a mass point at r for Seller 2:

$$
F _ {H} (p) = \frac {\Pi_ {s L} (p) - \Pi_ {f L} (r) - (1 - F _ {H} (r)) (\Pi_ {s L} (r) - \Pi_ {f L} (r))}{\Pi_ {s L} (p) - \Pi_ {f L} (p)}.\tag{34}
$$

The second condition is arrived at by using condition (33) and rearranging, whereby we obtain the expression for $F _ { H } ( r )$

$$
F _ {H} (r) = \frac {(r - p _ {H} ^ {*})}{(r - p _ {L} ^ {*})},\tag{35}
$$

which can be inserted in the Equation (34) to get the complete characterization of $F _ { H } ( p )$

To summarize, a crucial difference between the previous two cases is that the lowest support price is not determined solely by the relative costs or capacities, but is rather a function of the lower of the indifference prices, which is dependent on both the costs and capacities. If we substitute the different capacities and costs with the same costs and capacities for both sellers, the equilibrium reduces to that derived for the symmetric case.

Generalizing all three cases, we can state that the lowest support price in the case of asymmetric costs and capacities of a two-seller model depend on the relative rankings of the indifference prices. Both sellers have two strategic variables to consider to establish the lower indifference price (remember that the seller with the lower indifference price can, probabilistically, set higher prices and get higher payoffs).

A relative disadvantage with one can be compensated with the other. A graphic representation of the two cumulative distributions is shown in Figure 1.

## Extensions to the n-Seller Case

The analysis becomes more complex for more than two sellers, but we nevertheless can gain some intuition regarding the effect of an increase in the number of sellers by analyzing the specific case of an increase in market size with the number of sellers increasing, such that the sellers (a) have the same capacity as before, (b) remain in the same proportion with respect to type, and (c) provide the same aggregate excess capacity, such that there remains a single seller with the highest price who will sell below capacity by the same amount as in the smaller market. If such is the case, then the bounds for the price distribution and the accompanying profits at the lowest price (where capacity is sold with probability one) are unchanged for each type. It is now more likely, however, that a price above this lowest price will not be the highest price at the former distribution of prices. Thus, the original distribution of prices will be too high to ensure identical profits at all prices. The result will be a shift downward in the price distribution with an increase in the number of sellers.

To show this most easily, consider the symmetric case when costs and capacities are the same across all sellers. With n sellers, n <sub>−</sub> 1 sellers supply to capacity and the last seller supplies to the residual demand $( ( n K - Q ) > 0 )$ . A seller now fails if his price turns out to be the highest price among all the sellers (an event that happens with a probability of $( F ( p ) ) ^ { n - 1 } )$ and succeeds otherwise (an event that occurs with a probability of $( 1 - ( F ( p ) ) ^ { n - 1 } ) )$ . Using similar arguments as before, we have the expected profits  given by

$$
\Pi = \Pi_ {f} (F (p)) ^ {n - 1} + \Pi_ {s} (1 - (F (p)) ^ {n - 1}),\tag{36}
$$

which implies a price distribution $F _ { n } ( p )$ for the symmetric n-seller case as

$$
F _ {n} (p) = \left(\frac {\Pi_ {s} - \Pi}{\Pi_ {s} - \Pi_ {f}}\right) ^ {1 / (n - 1)}.\tag{37}
$$

In (37), we introduce the subscript n to differentiate the number of sellers for the particular price distribution under consideration. It is important to note that to have a valid comparison across markets of different numbers of sellers, we specify that $\Pi _ { s } ( p )$ and $\Pi _ { f } ( p )$ are invariant to changes in the number of sellers. The support of the price distribution remains unchanged as well. From Equation (37), given $\Pi _ { s } > \Pi > \Pi _ { f } ,$ it follows that

$$
F _ {n} (p) > F _ {n - j} (p)\tag{38}
$$

(that is, $F _ { n - j } ( p )$ stochastically dominates $F _ { n } ( p ) )$ for all $p ,$ with $n > 2$ and $n - 1 > j > 1$ . The implication is that as n goes up, the distribution shifts mass to the lower prices, and the average price falls. Whether this result holds in more general settings with more than one type of sellers or with disproportionate changes in the types of sellers remains an open question.

## Managerial Insights

The inherent attraction of B2B marketplaces lies in their promise of bringing efficiency to the supply chain. Buyers can get better prices from sellers from the effects of increased liquidity, and therefore from the increased competition among sellers. Our paper analyzes this competition, keeping in mind seller heterogeneity.

The competitive status of a seller, and in particular the advantages to cost cutting or capacity growth, can be clearly identified from our analysis. The equilibrium result of the two-seller heterogeneous costs model is as expected—the lower-cost producer has an inherent advantage in its pricing strategies. What is more interesting is the result of the heterogeneouscapacities model, where the results support the notion of bigger is better. This result flows directly from the fact that the high-capacity seller has a lower indifference price; to compensate for that fact, the low-capacity seller must allow a higher profit to the high-capacity seller in equilibrium at all prices in the support. Note that this behavior, and the resulting higher average sales by the seller with the larger capacity, does not rely on advantages the larger sellers may have with respect to customer demand (such as would exist if, for instance, buyers view largercapacity sellers as more reliable, or think it advantageous to do business with fewer sellers).

As the generalized heterogeneous-cost-and-capacities model shows, the manager of a seller firm has two strategic variables with which to play. Lower costs of production give inherent benefits to a seller, as do larger capacities. Thus, a seller relatively disadvantaged in terms of marginal costs might want to increase its production capacity. If the industry is fragmented, with no single overwhelmingly large seller, a move toward online exchanges by the original equipment manufacturers (OEMs) might trigger a wave of consolidation among several sellers, because increasing capacities in this fashion is an easier strategic variable to manipulate, at least in the short run, than lowering marginal costs of production. In a report on the automotive industry, McKinsey & Company (2000) notes that industry has seen a large amount of consolidation among OEMs in recent years, and that this trend is expected to continue.

It is also conceivable that a seller with superior efficiencies of production can, over time, price its competitor out of the market by ratcheting up production capacity. Such behavior is seen in real life, though there are conceivably factors other than increased capacity or cost efficiencies at work. For example, in the personal computers industry the cost leader, Dell Computer, has over the years become the largest producer in the world. In fact, after the second quarter of 2003, it announced that it would reduce the prices of its computers by an average of around 20%, even as the nearest competitor, Hewlett-Packard, announced that its personal computing division is deeply in the red as a result of severe price wars (CNet News 2003).<sup>16</sup>

## Future Directions of Research

We are currently trying to implement a B2B reverse auction in a synthetic environment, where semiintelligent sellers learn over time to converge on an optimum strategy. Some questions that we hope to answer include: Can such agents learn over time to converge to an optimal game-theoretic equilibrium? If yes, how fast do they converge to that equilibrium? How does increasing the memory of the past results increase the speed to convergence toward the equilibrium? The results will hold much more interest for the heterogeneous costs and capacities model, because the artificial agents are expected to understand over time that (a) it makes no sense to price in the interval of the two indifference prices, and (b) the agent with the higher indifference price has a positive probability of pricing at the reservation price r. We briefly describe our approach in the next paragraph.

We modeled software agents that use reinforcement learning (specifically Q-learning) algorithms (for a background on the use of reinforcement learning in game theory, see Oliver (1996), Rapaport et al. (1998), Roth and Erev (1995), and Sandholm and Crites (1996) to learn the ideal behavior over time (the agents start off initially without bias)). We then compare the prices chosen for various combinations of demand, capacities, and marginal costs to the theoretical cumulative distributions for goodness of fit. Our initial algorithms worked well for similar sellers (see Bandyopadhyay et al. 2003, Bandyopadhyay et al. 2005), but not for dissimilar sellers. A modified algorithm has given very promising results (for example, the agents quickly learn not to price below the higher of the indifference prices, and the agent with the higher indifference price places a positive probability for bidding at r), but we have yet to test it rigorously for various combinations of Q, K, and c.

We also explore the value of information in this setting: By how much do the average profits go up when the agents start with the initial knowledge about the suboptimality of pricing below the higher indifference point? Considering the recent work in understanding game-theoretic behavior in experimental settings, these experiments with continuous strategy spaces and complicated equilibrium solutions would be of considerable interest to researchers and practitioners alike. Extensions of such research can have useful implications in the implementation of automated mechanisms by buyers and sellers in transactions of this kind.

## Conclusion

The Internet and the subsequent development of open standards are making the concept of a buy-centric online exchange increasingly popular in a variety of industries. Sellers of a component or raw material can be situated anywhere in the world, thus increasing the universe of sellers from whom an organization can buy its products. We have analyzed the competition between these sellers in an online sealed-bid reverse auction. The equilibria for the various models show the effects of the two strategic variables—cost and capacity—in a manager’s decision-making model.

The model captures some of the unique features that we can expect to see in an exchange (limited number of sellers with huge buying power, modified capacity constraints, inelastic demand function below reservation price), and shows how competition in those environments can reduce the overall price paid by the buyers, as well as how operating costs and capacities affect the strategies of the competing sellers.

We are currently researching whether synthetic agents can learn from experience to implement our results. With the ubiquity of online transactions, such automated handling of transactions can potentially be very beneficial.

## Acknowledgments

This research is partially funded by the National Science Foundation Grant DMI-0122214. The authors are indebted to several observations, suggestions, and corrections by three anonymous referees and Professor Ira Horowitz of the University of Florida in earlier versions of the paper. The authors also acknowledge crucial input from Mr. Antonio Benecchi, Project Manager at Roland Berger Strategy Consultants, and executives at Indiamarkets.com for sharing some of their live auction data and their observations.

## Appendix. A B2B RFQ at IndiaMarkets.com, India’s Largest B2B Portal

<table><tr><td colspan="10">Source Bid Information:</td></tr><tr><td colspan="10">Source Bid Number: 15299 Source Bid Name: Aluminium</td></tr><tr><td colspan="10">Source Bid Start Date: 07/06/2001 05:00:00 (US-EST) Source Bid End Date: 07/06/2001 08:15:00 (US-EST)</td></tr><tr><td>Display</td><td>Show Low Bid Price and Rank</td><td>Package Type</td><td>Split Lot</td><td>Automatic Extension</td><td>Enabled</td><td>Allow Bidprice</td><td colspan="3">&lt;=starting price</td></tr><tr><td colspan="10">Part Information: Currency: INR</td></tr><tr><td>Part Number</td><td>Biddable</td><td>Part Description</td><td></td><td>Source Bid Qty</td><td>UoM</td><td>Drawing Start Bid Price</td><td>Minimum Decrement</td><td>Adder</td><td>S&amp;P</td></tr><tr><td>Al-Ingot 01</td><td></td><td>Pure Aluminium Ingots, Electrical grade, 99.6 % Purity, Specs attached-Delivery at Faridabad</td><td></td><td>360000</td><td>kg</td><td>Picture</td><td>85.1000</td><td>0.1</td><td></td></tr><tr><td>Busbar-GEPC</td><td></td><td>EC Grade Aluminium Busbar Flat Having Square Edges conforming to IS:5082-1981 as per alloy &amp; temper E91EWP, Sizes as per attachment.-Delivery at Bangalore</td><td></td><td>80000</td><td>kg</td><td>Picture</td><td>96.7500</td><td>0.1</td><td></td></tr><tr><td>GEL-01</td><td></td><td>Grade-L8S/ Soft, Gauge 0.36 mm+/-0.02mm, Width-96.0 mm+/-0.30mm (For GLS Bulbs)-Delivery at Nadiad, Gujarat</td><td></td><td>36000</td><td>kg</td><td>Picture</td><td>106.0000</td><td>0.2</td><td></td></tr><tr><td>GEL-02</td><td></td><td>Grade-AA/8011/98S/Soft, Gauge-0.32mm+/-0,02 mm, Width-76mm+/-0.20mm (For Tubelights)</td><td></td><td>60000</td><td>kg</td><td>Picture</td><td>106.0000</td><td>0.2</td><td></td></tr><tr><td>GEMS-01</td><td></td><td>Aluminium Extrusion- Grade 6061 T6, Size details as per attachment.-Delivery at Bangalore</td><td></td><td>10000</td><td>kg</td><td>Picture</td><td>136.0500</td><td>0.2</td><td></td></tr><tr><td>GEMS-02</td><td></td><td>Aluminium Extrusion- Grade 6061T6, Special size, drawing attached, Delivery at Bangalore</td><td></td><td>2500</td><td>kg</td><td>Picture</td><td>179.1000</td><td>0.2</td><td></td></tr><tr><td>GEMS-03</td><td></td><td>Aluminium Extrusion- Grade 6061 T6 , Special Size as per attached drawing, Delivery at Bangalore</td><td></td><td>6600</td><td>kg</td><td>Picture</td><td>140.9000</td><td>0.2</td><td></td></tr><tr><td>GEMS-04</td><td></td><td>Aluminium- Plates/ Flats/Rod Grade-6351 T6, Item details as per attachment, Delivery at Bangalore</td><td></td><td>6200</td><td>kg</td><td>Picture</td><td>170.0000</td><td>0.2</td><td></td></tr><tr><td>GEMS-05</td><td></td><td>Aluminium -Rod, grade 6351 T6</td><td></td><td>270</td><td>kg</td><td>Picture</td><td>163.2000</td><td>0.2</td><td></td></tr><tr><td>GEMS-06</td><td></td><td>Aluminium- Sheets, Grade 5052 H32, Size &amp; qty as per attachment, Delivery at Bangalore</td><td></td><td>34600</td><td>kg</td><td>Picture</td><td>114.7000</td><td>0.2</td><td></td></tr><tr><td>GEMS-07</td><td></td><td>Aluminium- Plates, Grade 6082, Size &amp; qty as per attachment, Delivery at Bangalore</td><td></td><td>36000</td><td>kg</td><td>Picture</td><td>218.5000</td><td>0.2</td><td></td></tr><tr><td>GEMS-08</td><td></td><td>Aluminium Extrusion, Special Size as per drawing attached , Delivery at Bangalore</td><td></td><td>200</td><td>kg</td><td>Picture</td><td>147.6500</td><td>0.2</td><td></td></tr><tr><td>GEMS-09</td><td></td><td>Aluminium Extrusion, Special Size as per attached drawing, delivery at Bangalore</td><td></td><td>270</td><td>kg</td><td>Picture</td><td>149.6000</td><td>0.2</td><td></td></tr><tr><td>GEMS-10</td><td></td><td>Aluminium Alloy LM 4 T6 for casting, Delivery at Chennai</td><td></td><td>14000</td><td>kg</td><td>Picture</td><td>107.7000</td><td>0.2</td><td></td></tr><tr><td>GEMS-11</td><td></td><td>Aluminium Alloy LM25 for casting, Delivery at Bangalore</td><td></td><td>8750</td><td>kg</td><td>Picture</td><td>121.5000</td><td>0.2</td><td></td></tr></table>

## Comments :

Yes, I will participate in this Source Bid.

No, I will not participate in this Source Bid!

## References

Allen, B., R. Deneckere, T. Faith, D. Kovenock. 1992. Capacity precommitment as a barrier to entry: A Bertrand-Edgeworth approach. North Amer. Winter Meetings Econometric Soc. (January).

Angwin, Julia. 2003. Renaissance in cyberspace. The Wall Street J. (November 20) B1.

Baer, M., J. Davis. 2001. Some assembly required. Business 2.0 (February 20) 76–85.

Bandyopadhyay, S., J. M. Barron. 2004. A generalized model of competition among sellers in a B2B exchange. Working paper, Krannert Graduate School of Management, Purdue University, West Lafayatte, IN.

Bandyopadhyay, S., J. M. Rees, J. M. Barron. 2005. Simulating sellers in online exchanges. Decision Support Systems. Forthcoming.

Bandyopadhyay, S., A. Chaturvedi, J. Barron, J. Rees, S. Mehta. 2003. Simulating sellers’ behavior in a reverse auction B2B exchange. P. M. A. Sloot et al., eds. Internat. Conf. Comput. Sci., Lecture Notes Comput. Sci., No. 2660, 365–374.

Barlas, D. 2003. The value of reverse auctions. Line56 (July) http:// www.line56.com/articles/default.asp?articleid=4788.

Barua, A., B. Lee. 1997. An economic analysis of the introduction of an electronic data interchange system. Inform. Systems Res. 8(4) 398–422.

Bhargava, H. K., V. Choudhary, R. Krishnan. 2000. Pricing and product design: Intermediary strategies in an electronic market. Internat. J. Electronic Commerce 5(5) 37–56.

Biglaiser, G. 1993. Middlemen as experts. RAND J. Econom. 24(2) 212–223.

Boyd, J. H., E. C. Prescott. 1986. Financial intermediary coalitions. J. Econom. Theory 38 211–232.

CNet News. 2003. Dell cuts prices across range of products. (August) http://news.com.com/2100-1003\_3-5066500.html?tag =fd\_top.

Dai, Q., R. J. Kauffman. 2003. To B2B or not to B2B: An evaluative model for e-procurement adoption. Working paper, MIS Research Center, Carlson School of Management, University of Minnesota, Minneapolis, MN.

Dasgupta, P., E. Maskin. 1986. The existence of equilibrium in discontinuous economic games, II: Applications. Rev. Econom. Stud. 53(1) 27–41.

Deneckere, Raymond J., D. Kovenock. 1996. Bertrand-Edgeworth duopoly with unit cost asymmetry. Econom. Theory 8 1–25.

Fast Company. 2001. How I saved \$100 million on the Web. 43(February) 174.

Helper, S., J. P. MacDuffie. 2001. B2B and modes of exchange: Evolutionary and transformative effects. Bruce Kogut, ed. The Global Internet Economy.

Jap, S. D. 2000. The impact of online, reverse auctions on buyersupplier relationships. Working paper, EBusiness@MIT Center, Leaders for Manufacturing Program and MIT-Ford Alliance.

Katok, E., A. E. Roth. 2004. Auctions of homogeneous goods with increasing returns: Experimental comparison of alternative “Dutch” auctions. Management Sci. 50(8) 1044–1063.

Kreps, D., J. Scheinkman. 1983. Quantity precommitment and Bertrand competition yield Cournot outcomes. Bell J. Econom. 326–337.

McKinsey & Company. 2000. The automotive industry: A new model to be invented! (August).

Oliver, J. 1996. A machine learning approach to automated negotiation and prospects for electronic commerce. J. Management Inform. Systems 13(3) 83–112.

Rapoport, A., T. E. Daniel, D. A. Searle. 1998. Reinforcement-based adaptive learning in asymmetric two-person bargaining with incomplete information. Experiment. Econom. 1 221–253.

Riggins, F. J., C. Kriebel, T. Mukhopadhyay. 1994. The growth of interorganizational systems in the presence of network externalities. Management Sci. 40 984–998.

Roland Berger Strategy Consultants and Deutsche Bank. 2000. Automotive e-commerce: A (virtual) reality check. (June) http:// www.rolandberger.com.

Roth, A. E., I. Erev. 1995. Learning in extensive-form games: Experimental data and simple dynamic models in the intermediate

term. Games Econom. Behavior 8(1, Special Issue: Nobel Symposium) 164–212.

Rubin, P. A., W. C. Benton. 1993. Jointly constrained order quantities with all-units discounts. Naval Res. Logist. 40 255–278.

Rubinstein, A., A. Wolinsky. 1987. Middlemen. Quart. J. Econom. 102(3) 581–594.

Sandholm, T. W., R. H. Crites. 1996. Multiagent reinforcement learning in the iterated prisoner’s dilemma. BioSystems 37 147–166.

Sinha, I. 2000. Cost transparency: The net’s real threat to prices and brands. Harvard Bus. Rev. 78(March–April) 3–8.

Tomak, K., M. Xia. 2002. Evolution of B2B marketplaces. Electronic Markets 12(2).

Varian, H. 1980. A model of sales. Amer. Econom. Rev. 70(4) 651–659.

Waltner, C. 1999. Procurement pays off—Companies are finding that procurement software comes with a quick ROI. Inform. Week 745(July 26) http://www.informationweek.com/745/ procure.htm.

Zhu, K. 1999. Strategic investment in information technologies: A real-options and game-theoretic approach. Doctoral dissertation, Stanford University, Stanford, CA.

Zhu, K. 2002. Information transparency in electronic marketplaces: Why data transparency may hinder the adoption of B2B exchanges. Electronic Markets 12(2, Special Issue on B2B E-Commerce) 92–99.

Zhu, K. 2004. Information transparency of business-to-business electronic markets: A game-theoretic analysis. Management Sci. 50(5) 670–685.

Zhu, K., J. Weyant. 2003. Strategic decisions of new technology adoption under asymmetric information. Decision Sci. 34(4) 643–675.
