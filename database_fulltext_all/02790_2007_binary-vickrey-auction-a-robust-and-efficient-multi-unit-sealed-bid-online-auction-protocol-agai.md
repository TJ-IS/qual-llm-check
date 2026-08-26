---
otero_id: 2790
otero_key: "YH2Q49K5"
title: "Binary Vickrey auction — A robust and efficient multi-unit sealed-bid online auction protocol against buyer multi-identity bidding"
authors: "Zoltán Hidvégi; Wenli Wang; Andrew B. Whinston"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.09.013"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Binary Vickrey auction — A robust and efficient multi-unit sealed-bid online auction protocol against buyer multi-identity bidding

Zoltán Hidvégi <sup>a,⁎</sup>, Wenli Wang <sup>b,1</sup>, Andrew B. Whinston <sup>a,2</sup>

<sup>a</sup> Center for Research on Electronic Commerce Department of Information, Risk,

and Operations Management The University of Texas at Austin, Austin, TX 78712, United State

<sup>b</sup> Department of Management Information Systems College of Business University of Nevada at Las Vegas Las Vegas, NV, 89154, United States

Received 28 July 2006; accepted 17 September 2006 Available online 15 December 2006

## Abstract

The multi-unit Vickrey–Clark–Groves (VCG) mechanism has two major weaknesses: it has high computational complexity and monotonicity problems [Paul Milgrom. Putting Auction Theory to Work. Cambridge University Press, Cambridge, UK, 2004] such that if goods are not substitutes for all bidders and if a bidder can submit bids under multiple identities, then the VCG is no longer strategy-proof. To address these two weaknesses, we introduce a Binary Vickrey Auction (BVA) where goods are allocated in bundles of sequentially-decreasing power-of-two items in multiple rounds. Because of the discrete allocation operations, the BVA is computationally efficient. It is also robust against buyer multi-identity bidding by discouraging a bidder splitting his single bid for a larger bundle into several bids under multiple bidder identities for smaller bundles because the BVA favors bids for larger bundles with earlier considerations and cheaper prices. © 2006 Elsevier B V All rights reserved

Keywords: Auctions; Multi-unit auctions; False-name bids; Identity theft; Electronic commerce; Mechanism design; Vickrey auctions; Double auctions

## 1. Introduction

Internet auctions have become a powerful engine of electronic commerce. But the ease of creating multiple screen-names has allowed false-name bids – bids made under fictitious names [21] – to unlawfully alter auction outcomes. False-name bidding has two possible sources, the seller or a buyer. Seller false-name bidding, i.e., shill bidding, are studied in Refs. [6,17,14] <sup>3</sup>. This paper studies buyer false-name bidding, i.e., multi-identity bidding, in sealed-bid multi-unit online auctions, and recommends a protocol for such an auction that is computationally efficient and buyer-false-name-proof (i.e., for each buyer truth-telling without using falsename bids is a dominant strategy [21]).

Multi-unit auctions are widely practiced. They are used to auction off financial instruments, electricity, and spectrum, or to sell overstocked merchandise and assets of bankrupt firms. In a discriminatory multi-unit sealedbid auction, bidders bid the quantity and the unit price, and the winning bidders pay their bids (i.e., one's payment is monotonic to one's bids). This creates an incentive for bidders to bid less than their valuations. Therefore, it is desirable to design incentive-compatible multi-unit auctions, such as to extend single-unit Vickrey auctions. The simplest extension of single-unit Vickrey auctions to multi-unit is to use a uniform pricing where winning bidders pay a uniform price equal to the highest losing bid<sup>4</sup>. Unfortunately, in this simple generalization, truth-telling is no longer a dominant strategy for a bidder who buys multiple units; since they are more likely to become pivotal bidders, they have an incentive to bid less than their valuations or to reduce their demand [3]. The Vickrey–Clark–Groves (VCG) auction mechanism [7,9,15] has been designed to overcome this problem, where bidders submit bids for all possible subsets of the items for sale<sup>5</sup> and the items are allocated to maximize the sum of the winning bids. Each winning bidder pays his bid minus his contribution to the social surplus, and his contribution is how much the sum of the winning bids would be reduced if this particular winning bidder were not present. The VCG auction achieves socially optimal allocations, and truth-telling is a dominant strategy for all bidders when there are no bidder collusions.

Unfortunately, the VCG auction suffers from monotonicity problems [11], that is, a bidder's payment is a non-monotonic function of other bidders' payments, and this leads to cases where adding bidders can reduce the equilibrium revenues. When there are bidder collusions, the VCG auction is no longer dominant strategy incentive compatible. In online auctions, bidder collusion has become a serious problem; the anonymity of the Internet has enabled a large scope of bidder self-collusion via multi-identity bidding, i.e., a bidder submits multiple bids under both the legitimate and false identities in the same auction. As we will show later, if there are buyer false-name bids, and goods are not substitutes for all buyers, i.e., some buyers have complementary valuations where the value of a bundle is greater than the sum of the value of the individual items, in certain cases a bidder can increase his utility by splitting a single bid for a larger bundle into multiple bids under false identities for smaller bundles. In this way, truth-telling in the VCG is no longer a dominant strategy. Another weakness of the VCG, which is more well-known than its vulnerability to buyer collusion, is that its allocation has an NP-hard computational complexity—it is practically impossible to compute when the number of bidders and items for sale is large because the time required to calculate the optimal allocation increases exponentially with the number of bidders and items. An additional unfavorable feature of the VCG is that it requires bidders to reveal their complete demand functions to the auctioneer, but bidders may be reluctant to provide this private information.

To address the weaknesses in the VCG auction, we aim to design an auction protocol that is buyer-falsename-proof, computationally efficient, and yet does not require bidders to fully disclose their demand functions.

In the design, we need to consider the trade-off between optimization results and added constraints. Traditional mechanisms discussed in economic theories are often the best choices; they are based on mathematical optimization, abstract from execution environment and applied technology. Consideration of the trading environments in practice will lead to sacrifices in objectives, such as the reduction in social surplus, efficiency, or simplicity. This is because the added constraints often worsen the optimization results. Hence, our design goal is to search for the second-best mechanism that is still nearly optimal, but resilient to online fraud.

The possibility of creating false identities adds new moves to the strategy space of the existing mechanisms. These moves have not been widely considered in auction literature and can break the equilibria of the games. In fact, it has been proved that if there is complementarity among auctioned units and buyers can submit false-name bids, then there is no auction mechanism with a dominant strategy equilibrium that satisfies individual rationality, incentive compatibility, and Pareto efficiency [21,13]. An auction mechanism that makes buyer false-name bids uneconomical has to sacrifice one of these conditions. Since individual rationality is necessary to guarantee that buyers do not lose by participating in the auction, our goal is to design a false-name-proof mechanism that can achieve a reasonably efficient allocation. The Revelation Principle holds in any auction even if false-name bids are present; it remains true that even with fictitious players for any equilibrium in any game, there is an equivalent false-name-proof game [13]. This means that our search for a reasonably efficient mechanisms that are falsename-proof can be simplified to truthful mechanisms, but the incentive compatibility condition must be extended to ensure that there is no incentive to make falsename bids.

In the limited literature on multi-unit auctions, complementarity among goods has not been studied well. Most papers assume decreasing demand functions when the unit price that a buyer is willing to pay decreases with the number of units [3,12,8,1]. This assumption eliminates most of the incentives for buyer false-name bids. Many papers have an even more restrictive assumption that the valuation of a bundle is the sum of the valuations of the elements in the bundle [4]. Unfortunately, complementarity often exists, when a single unit may have little or no value to the buyer, but multiple units are quite valuable. Ref. [20] argues that if the number of units desired becomes very large, the marginal utility of a unit tends to decrease, but, if the number of units desired is relatively small, complementarity often exists and the marginal utility of a unit may actually increase. The sale of tickets (e.g., opera tickets for a group or airline tickets for a family trip) is a familiar example of an all-or-nothing case. The allocation of computing resources (e.g., bandwidth), electronic power, and the wireless communication spectrum also prefers the consideration of complementarity among multiple units.

Ref. [18] were the first to introduce a buyer-falsename-proof combinatorial sealed-bid<sup>6</sup> auction protocol called the Leveled Division Set (LDS). The LDS uses predefined division sets of the auctioned goods to restrict the possible allocations. The division sets are arranged into levels with each level being a “refinement” of the previous one. The first level that allows for the allocation of some goods is chosen to compute the auction outcome. The LDS guarantees that bidders cannot benefit from submitting several bids under multiple identities. To achieve this robustness, the LDS drastically reduces the social surplus by discriminating against bids for small bundles and it often ends with unsold units even when there are valid bids that could be fulfilled with the remaining units.

Both the economic and computational efficiency of the LDS depends heavily on the choice of leveled division sets and reserve prices. Moreover, the choice of division sets depends on the bidders' value distribution, and therefore an inefficient allocation is always possible when the bidders' value distribution is an unfavorable one. Ref. [16] introduced the Leveled Partition Set (LPS) protocol derived from the LDS for auctioning multi-unit identical items. The LPS is also buyer-falsename-proof and is computationally more efficient than the LDS, but it has the same weakness in the reduction of social surplus. Ref. [20] proposed an Iterative Reducing (IR) protocol also derived from the LDS. Unlike the LDS, the IR protocol no longer requires the choice of leveled division sets. However, the IR can still be very inefficient because the auction may terminate even when there are a large number of unsold items and, at the same time, there are buyers with valuations above the reserve price.

In this paper, we design a multi-unit, sealed-bid auction mechanism called the Binary Vickrey Auction (BVA) protocol. It is called a “binary” protocol because both the bids and the allocation of goods are in various bundles of power-of-two items. Bidders submit their sealed bids for bundles of power-of-two items simultaneously and the auctioneer calculates the allocation in multiple steps with sequentially-decreasing power-oftwo bundle sizes. In the first step, only a single largest possible bundle of goods is allocated if a valid bid for such a bundle exists. In each subsequent step, the bundle size is halved. The allocation ends when the demand exceeds the supply or the bundle size of one is allocated.

In the BVA auction, the restriction of bids to bundles of power-of-two items is necessary to achieve robustness against buyer false-name bids. Allocating goods in a sequential order with decreasing power-of-two bundle sizes gives a single bid for a large bundle a one-step earlier consideration than two bids for two bundles with a halved size. Because of the discrete computation, the computational complexity of the BVA is linear in the number of bids submitted, and the allocation problem requires minimal computing resources. In contrast, the allocation in the VCG, LDS, LPS, and IR auctions can be computationally infeasible sometimes. In addition, if the number of items for auction is exactly an integer of power-of-two (an auction seller may conveniently determine such a lot size), the BVA, unlike the LDS, LPS, or IR, guarantees the sales of all goods when there are enough bidders whose valuations are above the reserve price. Otherwise, a partial bundle in the final allocation step may remain unsold if the auction ends before reaching the step of allocating items in the bundle size of one.

The BVA mechanism favors volume buyers. This is a desirable feature in many auction markets, especially for business-to-business (B2B) transactions. Although a BVA auction can allocate the goods to volume buyers at a lower price even if there are buyers with demand for small quantities willing to pay more per unit, a seller may still prefer the BVA because she can lower transaction costs and get quicker profits.

The article proceeds as follows. In Section 2, we analyze some weaknesses in running the traditional VCG auction over the Internet when it is possible for buyers to submit false-name bids. In Section 3, we define the BVA and analyze its pros and cons through proofs and examples. In Section 4, we extend our design concept in the BVA auction protocol into a buyer-false-name-proof exchange market mechanism. Section 5 concludes the paper.

## 2. Effects of buyer false-name bids in the VCG auction

In the VCG mechanism, bidders submit bids for all possible subsets of the items for sale, and the mechanism selects an allocation of a set of goods to bidders. Its objective function is to maximize social surplus, which is calculated as the sum of the bids for the set of goods obtained by bidders and is equivalent (because of incentive compatibility) to maximizing the sum of utilities of the participating agents, including the seller and bidders. The seller's utility is the winning bidders' payments. A bidder's utility is his valuation for the goods he wins minus his actual payment. For each bidder, we calculate how much he contributes to the social surplus by calculating the difference between the optimal social surplus and the surplus that would have been achieved in his absence. Each bidder gets credit for his contribution to the social surplus and only pays his bid minus this credit. The auctioneer only knows the bids of the participants but not their true willingness to pay, i.e., their valuations. However, to calculate the social surplus and payments, the auctioneer assumes that bidders bid their true valuations. This is a proper assumption because in the VCG it is a dominant strategy for each bidder to bid his valuation. For each subset of the goods, each bidder must submit the maximum bid he is willing to pay for that set.

Formally, let M be the set of goods to be auctioned, let $N { = } \left\{ 1 { , } . . . , n \right\}$ be the set of buyers, let 0 denote the seller, let G: M → N ⋃ {0} be an allocation of goods to agents, and $\nu _ { x } ( G )$ be the bid of agent x for the set of goods allocated to him $G ^ { - 1 } ( \{ x \} )$ . The allocation under the VCG is the optimal allocation $G ^ { * }$ whichmaximizes $\scriptstyle \sum _ { x = 1 } ^ { n } \nu _ { x } ( G )$ . The payment of agent x is:

$$
\begin{array}{l} p _ {x} = v _ {x} (G ^ {*}) - \left(\sum_ {y} v _ {y} (G ^ {*}) - \sum_ {y} v _ {y} (G _ {\sim_ {x}} ^ {*})\right) \\ = \sum_ {y \neq x} v _ {y} (G _ {\sim_ {x}} ^ {*}) - \sum_ {y \neq x} v _ {y} (G ^ {*}) \end{array}\tag{1}
$$

where $G _ { \sim x } ^ { * }$ is the optimal allocation when assuming that agent x is absent in the auction.

The VCG mechanism is equivalent to the classic second-price Vickrey auction when there is only a single item for sale. The VCG can be also modified to add reserve prices. In a reserve-price VCG, the social surplus of an allocation is calculated as the sum of bids corresponding to the allocation minus the reserve price for the set of goods allocated to bidders. Similarly, each bidder's payment is discounted by his contribution to the modified social surplus. Note that the VCG without a reserve price is only a special case of the VCG with a reserve.

The VCG assumes that each agent maximizes his own utility without colluding with other agents. When there is no bidder collusion, the VCG mechanism is an incentive compatible, direct mechanism. Truth-telling is an optimal, dominant strategy in the VCG, that is, one always gain maximum advantage by declaring one's true valuation, regardless of the valuations and strategies of other bidders. It is clearly shown in Eq. (1) that for a given allocation each agent's payment is independent of his own valuation in private-value auctions.

But the assumption that no bidder colludes may no longer hold when the VCG is conducted over the Internet where a bidder can easily self-collude by creating fictitious identities. The VCG is no longer incentive compatible because a buyer can reduce his payment by submitting false-name bids: even though agent $x ' s$ valuation does not appear in Eq. (1), x can still manipulate his payment through the bids submitted under agent y, y ≠x in the allocation calculation but in fact y is x's false identity(identities).

Ref. [18] has shown a simple example demonstrating that the VCG is not robust against buyer false-name bids. We introduce two examples to compare the effects of buyer false-name bids on the VCG allocation. In both examples, the reserve price for a single item is r.

Example 1. In a reserve-price VCG auction where $r { < } \$ 10$ , there are two tickets for sale and two bidders, Alice and Bob. Alice would like to buy two tickets for \$30 or one ticket for \$15. Bob would like to buy two tickets for \$20 but does not want to buy a single ticket.

The outcome of Example 1 is summarized in Table 1. The optimal allocation gives both of the two tickets to Alice and achieves a social surplus of $\$ 30-2 r .$ If Alice had not bid, the optimal allocation would have given two tickets to Bob for a social surplus of \$20 − 2r. Alice's bid improves the social surplus by \$10. Therefore, Alice's payment is \$20.

Example 2 shows how Alice, still obtaining the same number of goods, can reduce her payment by colluding with herself through the use of a false identity.

Example 2. In a reserve-price VCG auction where r b \$10, there are two tickets for sale and three bidders, Alice, Fanny and Bob. Both Alice and Fanny would each like to buy one ticket for \$15. Bob would like to buy two tickets for \$20 but does not want to buy a single ticket.

The outcome of Example 2 is summarized in Table 2. The optimal allocation gives one ticket to Alice and one to Fanny and achieves \$30 − 2r social surplus. If Alice had not bid, there would have been two possible allocations: 1) give one ticket to Fanny for \$15 − r social surplus; 2) give two tickets to Bob for \$20 − 2r social surplus. If $\mathbb { S } 2 0 - 2 r \mathbb { \geq } \mathbb { S } 1 5 - r ,$ which happens if $r \leq \$ 5$ the optimal allocation would have given two tickets to Bob. In this case, Alice's bid improves the social surplus by \$10 and her payment is \$5 (so is Fanny's). Otherwise, if r N \$5, Alice's payment is $\ S 1 5 - ( \mathbb { S } 1 5 - r ) = r$ (so is Fanny's).

In fact Fanny is a false identity created by Alice. By doing so, Alice obtains two tickets for max{\$10,2r} (r b \$10), which is less than her payment of \$20 in Example 1 even though the valuations of Alice and Bob remain the same. Alice has reduced her payment by creating a false identity and splitting her bid for two tickets into two bids for one ticket each.

Table 1  
Example: a VCG auction without buyer false-name bids

<table><tr><td>Bidder</td><td>Qty.</td><td>Bid</td></tr><tr><td>Alice</td><td>2</td><td>$30</td></tr><tr><td>Bob</td><td>2</td><td>$20</td></tr><tr><td>Alice</td><td>1</td><td>$15</td></tr><tr><td>Bob</td><td>1</td><td>-</td></tr><tr><td rowspan="2">Allocation</td><td>Alice</td><td>2</td></tr><tr><td>Bob</td><td>0</td></tr><tr><td rowspan="2">Payment</td><td>Alice</td><td>$20</td></tr><tr><td>Bob</td><td>$0</td></tr><tr><td rowspan="3">Utility</td><td>Alice</td><td>$10</td></tr><tr><td>Bob</td><td>$0</td></tr><tr><td>Seller</td><td>$20-2r</td></tr><tr><td>Social surplus</td><td></td><td>$30-2r</td></tr></table>

Table 2  
Example: a VCG auction with buyer false-name bid

<table><tr><td>Bidder</td><td>Qty.</td><td>Bid</td></tr><tr><td>Alice</td><td>2</td><td>-</td></tr><tr><td>Fanny</td><td>2</td><td>-</td></tr><tr><td>Bob</td><td>2</td><td>$20</td></tr><tr><td>Alice</td><td>1</td><td>$15</td></tr><tr><td>Fanny</td><td>1</td><td>$15</td></tr><tr><td>Bob</td><td>1</td><td>-</td></tr><tr><td rowspan="3">Allocation</td><td>Alice</td><td>1</td></tr><tr><td>Fanny</td><td>1</td></tr><tr><td>Bob</td><td>0</td></tr><tr><td rowspan="3">Payment</td><td>Alice</td><td>max{$5,r}</td></tr><tr><td>Fanny</td><td>max{$5,r}</td></tr><tr><td>Bob</td><td>$0</td></tr><tr><td rowspan="4">Utility</td><td>Alice</td><td>min{$10,$15-r}</td></tr><tr><td>Fanny</td><td>min{$10,$15-r}</td></tr><tr><td>Bob</td><td>$0</td></tr><tr><td>Seller</td><td>max{$10-2r,$0}</td></tr><tr><td>Social surplus</td><td></td><td>$30-2r</td></tr></table>

## 3. The Binary Vickrey Auction (BVA) protocol

In this section, we introduce the Binary Vickrey Auction (BVA) protocol designed to be robust against buyer false-name bids as illustrated in Example 2.

## 3.1. Rules of the BVA auction

The main feature of the BVA is that it favors selling large bundles. The allocation starts by allocating the goods to the bids for large bundles. If any item remains unsold after the allocation for large bundles, the bundle size is halved and the allocation procedure is repeated.

## Definition 3. (BVA)

The seller has M identical goods for auction with the reserve price r for each item. Before the auction closes, each bidder submits a package of sealed-bids with at most one sealed-bid for each bundle size of $2 ^ { m - i }$ , where $i { = } 0 , . . . , m ,$ and $2 ^ { m } \leq M < 2 ^ { m + 1 }$ . Each bid is labelled either “conditional” or “unconditional,” except that a bid for a single item is by default “unconditional”. The auctioneer calculates the allocation in at most $m + 1$ steps, starting with step 0. At step $i ( i { = } 0 , . . . , m )$ , the auctioneer only considers bids for the bundle size of $2 ^ { m - i }$ . “Unconditional” bids are always considered; but “conditional” bids are considered only if the “unconditional” demand exceeds the supply at the given bundle size. Let $I _ { i } { = } [ { \frac { M _ { i } } { { 2 ^ { m - i } } } } ]$ denote the number of unallocated bundles for step $i ,$ where [x] denotes the largest integer not greater than x. By definition, $M _ { 0 } { = } M$ and $I _ { 0 } { = } 1$

The allocation in step i is calculated as follows:

(1) Only bids for the bundle size of $2 ^ { m - i }$ goods are considered.

(2) If $I _ { i } { = } 0 $ , the allocation proceeds to step i + 1 or terminates if $i { = } m$

(3) If there are more than $I _ { i }$ “unconditional” bids at or above the reserve price, both the “unconditional” and “conditional” bids are sorted in a decreasing bid order. Each of the $I _ { i }$ highest bidders gets $2 ^ { m - i }$ items and pays the $( I _ { i } + 1 ) \mathrm { t h }$ highest bid. The auction terminates.

(4) If there are $I _ { i }$ or less “unconditional” bids at or above the reserve price, each of these bidders gets $2 ^ { m - i }$ goods at the reserve price. “Conditional” bids are not considered. If i = m or if there are no goods left for step i + 1, the auction terminates. Otherwise, the allocation proceeds to step $i + 1$

In the BVA the seller always has non-negative utility because each bidder pays at least the reserve price. Only bidders who win in the last allocation step will pay more than the reserve.

## 3.2. Robustness against Buyer False-name Bids

First, let us return to Examples 1 and 2 to see why the BVA is robust against buyer false-name bids (see Examples 4 and 5 as illustrated in Tables 3 and 4).

Example 4. In a reserve-price BVA auction where $r <$ \$10, there are two tickets for sale and two bidders, Alice and Bob. Alice would like to buy two tickets for \$30 or one ticket for \$15. Bob would like to buy two tickets for \$20 but does not want to buy a single ticket.

Table 3  
Example: a BVA auction without buyer false-name bids

<table><tr><td>Bidder</td><td>Qty.</td><td>Bid</td></tr><tr><td>Alice</td><td>2</td><td>$30,U</td></tr><tr><td>Bob</td><td>2</td><td>$20,U</td></tr><tr><td>Alice</td><td>1</td><td>$15,U</td></tr><tr><td>Bob</td><td>1</td><td>-</td></tr><tr><td rowspan="2">Allocation</td><td>Alice</td><td>2</td></tr><tr><td>Bob</td><td>0</td></tr><tr><td rowspan="2">Payment</td><td>Alice</td><td>$20</td></tr><tr><td>Bob</td><td>$0</td></tr><tr><td rowspan="3">Utility</td><td>Alice</td><td>$10</td></tr><tr><td>Bob</td><td>$0</td></tr><tr><td>Seller</td><td>$20-2r</td></tr><tr><td>Social surplus</td><td></td><td>$30-2r</td></tr></table>

Table 4  
Example: a BVA auction with buyer false-name bids

<table><tr><td>Bidder</td><td>Qty.</td><td>Bid</td></tr><tr><td>Alice</td><td>2</td><td>$15, U</td></tr><tr><td>Fanny</td><td>2</td><td>$15, U</td></tr><tr><td>Bob</td><td>2</td><td>$20, U</td></tr><tr><td>Alice</td><td>1</td><td>$15, U</td></tr><tr><td>Fanny</td><td>1</td><td>$15, U</td></tr><tr><td>Bob</td><td>1</td><td>-</td></tr><tr><td rowspan="3">Allocation</td><td>Alice</td><td>0</td></tr><tr><td>Fanny</td><td>0</td></tr><tr><td>Bob</td><td>2</td></tr><tr><td rowspan="3">Payment</td><td>Alice</td><td>$0</td></tr><tr><td>Fanny</td><td>$0</td></tr><tr><td>Bob</td><td>max{$15,2r}</td></tr><tr><td rowspan="4">Utility</td><td>Alice</td><td>$0</td></tr><tr><td>Fanny</td><td>$0</td></tr><tr><td>Bob</td><td>min{$5, $20-2r}</td></tr><tr><td>Seller</td><td>max{$15-2r, $0}</td></tr><tr><td>Social surplus</td><td></td><td>$20-2r</td></tr></table>

Table 3 shows that when using the BVA in the same setting as in Example 1, Alice bids \$30 unconditionally for two tickets and \$15 unconditionally for one ticket. Bob bids \$20 unconditionally for two tickets. Alice wins two tickets, and pays the second highest bid, \$20, thus the outcome and payment are the same as in Example 1 with the VCG.

Example 5. In a reserve-price BVA auction where $r <$ \$10, there are two tickets for sale and three bidders, Alice, Fanny and Bob. Both Alice and Fanny would each like to buy one ticket for \$15. Bob would like to buy two tickets for \$20 but not want to buy a single ticket.

Table 4 shows that when using the BVA in the same setting as in Example 2, Bob bids \$20 unconditionally for two tickets, while Alice creates a false identity Fanny and twice bids \$15 unconditionally for one ticket. Alice and Fanny also bid \$15 unconditionally for two tickets as well because in the BVA bids for two tickets are considered earlier than bids for one ticket, and for each of them two tickets are worth the same as one ticket. In the BVA allocation, Bob win. The only way Alice can win for two tickets is to submit an unconditional bid for two tickets higher than Bob's \$20 bid. Alice cannot win by creating a false identity and splitting her bid for two tickets into two bids for one ticket as in Example 2.

Comparing Tables 2 and 4, we can also see that, although the BVA reduces social surplus, the seller's utility in fact can be increased. It is not surprising because buyer false-name bidding is a fraud conducted by bidders who try to steal utility from the seller, hence eliminating the negative effects of this fraud provides the seller the level of utility she deserves. The BVA is beneficial to the auction seller as well as to the auctioneer because the auctioneer is paid by the seller. In a BVA auction, bidders are unlikely to conduct false-name bidding because they cannot benefit from it.

## 3.3. Proof of incentive compatibility

Theorem 6. The BVA is incentive-compatible even $i f$ bidders can submit false-name bids.

To simplify, in our further discussion, we assume that there is no bid below the reserve price because such a bid can never affect the outcome of the auction. To prove Theorem 6 we use the following lemmas:

Lemma 7. In the BVA, a bidder cannot increase his utility by submitting false-name bids.

Proof. Let $2 ^ { m - i }$ be the largest bundle size (smallest i) for which some bidder A has submitted $f { > } 1$ winning bids. Among them one bid is legitimate and $f - 1$ bids are false-name bids. Let $2 ^ { m - i \prime }$ ， $i ^ { \prime } { < } i$ be the smallest bundle size for which A has not submitted any unconditional bid. The total number of goods allocated to A between steps $i ^ { \prime }$ and i (including steps $i ^ { \prime }$ and i) is

$$
\begin{array}{c} \sum_ {i ^ {\prime} <   j <   i} 2 ^ {m - j} + 2 ^ {m - i} f = 2 ^ {m - i ^ {\prime}} - 2 ^ {m - i + 1} + 2 ^ {m - i} f \\ = 2 ^ {m - i ^ {\prime}} + 2 ^ {m - i} (f - 2) \geq 2 ^ {m - i ^ {\prime}}. \end{array}\tag{2}
$$

This means that there were less than $I _ { i ^ { \prime } }$ unconditional bids for a bundle size of $2 ^ { m - i ^ { \prime } }$ . Therefore A should have obtained the same or even better utility by bidding unconditionally for the bundle of $2 ^ { m - i ^ { \prime } }$ , not bidding for bundle sizes between $2 ^ { m - i ^ { \prime } }$ and $2 ^ { m - i }$ , and submitting only $f { - } 2$ bids for the bundle size of $2 ^ { m - i }$ goods (see Eq. (2)). If so, A's unconditional bid for $2 ^ { m - \widetilde { i ^ { \prime } } }$ goods would have won and he would have paid only the reserve price. $I _ { i }$ is reduced by 2 and the number of winning bids considered at step i is also reduced by 2, since A submits f − 2 bids instead of $f .$ Therefore, the sale price for the goods allocated at step i does not change. A is better off since he gets the same number of goods, but for $2 \cdot 2 ^ { m - i }$ goods he only pays the reserve instead of the price at step i (which can be higher than the reserve). For the rest of the goods allocated to him he pays the same.

Repeating this procedure we can see that A is better off submitting at most one bid for all bundle sizes. □

Based on this lemma we subsequently assume that each bidder submits zero or one bid at each bundle size. We now proceed to prove incentive compatibility.

Lemma 8. A bidder can never increase his utility by not submitting a bid for a bundle of $2 ^ { m - i }$ goods when his valuation for the bundle exceeds $2 ^ { m - i } r$

Proof. We will show that a bidder A is not worse off by submitting his valuation as a bid for a bundle of $2 ^ { m - i }$ goods when his valuation for the bundle exceeds $2 ^ { m - i } r .$ Assume A submits a bid for $2 ^ { m - i }$ goods. Consider two cases:

Case One i is not the final allocation step. If the bid is a conditional bid, then it is ignored and the outcome is the same as if A had not bid. If the bid is an unconditional bid, it will win and A obtains either positive or zero utility, which is not worse off than the zero utility that would have occurred if A had not bid.

Case Two i is the final allocation step. If A had not bid, all the goods would have been allocated to other bidders and A would have received nothing. Therefore, A is better off by submitting his valuation as either an unconditional or a conditional bid for $2 ^ { m - i }$ items. If A does not win, he does not pay anything, but if he wins, he pays at most his bid (i.e., his valuation). In either scenario A cannot lose if he bids. □

Lemma 9. A bidder can never increase his utility by bidding below or above his valuation.

Proof. Since in all but the last allocation steps winning bidders only pay the reserve price, the actual value of a bid is only considered in the last allocation step where winning bidders pay the highest losing bid. Therefore, by bidding below his valuation, a bidder can only reduce his chance of winning but not decrease his payment. On the other hand, by bidding above his valuation, he would not be better off if a truthful bid had won, since he would still pay the value of the highest losing bid. He would have to pay more than his valuation if a truthful bid had not won, but the increase in the bid makes him a winning bidder. □

Theorem 6 immediately follows from the previous lemmas.

## 3.4. Economic efficiency

In order to achieve the buyer-false-name-proof property, the BVA mechanism often results in an inefficient allocation, because bids for large bundles always win over small bundle bids even if the smallbundle bids offer significantly higher unit prices. But in all but a few special cases BVA allocates all goods to bidders.

One special case occurs when step i is the final allocation step but $M _ { i }$ is not a multiple of $2 ^ { m - i }$ , and this happens if and only if M is not a multiple of $2 ^ { m - i }$ . An auction seller can easily avoid this case if she has flexibility determining lot sizes. If it is not avoidable, then some goods will stay with the auctioneer even though there might be bidders who have submitted bids for smaller bundles above the reserve price. One may suggest that the BVA can be improved if the allocation continues for smaller bundles. If so, however, Lemma 7 would still hold but Lemma 8 would not. Hence, the incentive compatibility of the BVA is violated. For example: if the reserve price is \$1 and bidder A's valuation for a single item is \$3 but any additional item is worthless for him, A would not bid \$3 for two goods if there is odd number of items for sale even though his valuation for two items exceeds the reserve. This is because A knows that his bid for a single item will sooner or later be considered, and, if his bid for two items wins, he will have to pay at least \$2, resulting in at most \$1 utility, but he still has opportunities to get one item for less than \$2, resulting in more than \$1 utility.

Another rare source of inefficiency comes from the preferential treatment of unconditional bids: it occurs is when step i has exactly $I _ { i }$ unconditional bids and $M _ { i } =$ $2 ^ { m - i } I _ { i } .$ In this case, the unconditional bidders get all the goods at the reserve price even though there may be conditional bidders who bid higher than the unconditional bidders. This problem might be fixed by considering the conditional bids when determining the allocation if there are exactly $I _ { i }$ unconditional bids. However, such modification would break Lemma 7 and thus compromise the robustness against false-name bids.

As we have mentioned earlier, we sometimes need to sacrifice the efficiency of a mechanism in special cases as a trade-off for security and incentive compatibility. All of the existing protocols against false-name bids [18,16,21,20,17] as well as BVA sacrifice efficiency to various degrees.

## 3.5. Proof of computational efficiency

Theorem 10. The BVA is computationally efficient because the allocation of a BVA auction can be determined in only O(b log M) time, where M is the total number of goods for auction and bis total the number of bids.

Proof. Since the number of allocation steps is at most $1 +$ log<sub>2</sub> $M ,$ it is enough to show that the allocation in each step, that is, selecting the $I _ { i }$ highest bidders, can be decided in $O ( b )$ time. This is true because there is a wellknown algorithm [5] to select the i largest elements from a totally ordered set of K elements in O(K) time. □

## 3.6. Bidding strategies

## 3.6.1. Labeling a bid “unconditional” or “conditional?”

Even though the BVA protocol is incentive-compatible in the sense that a bidder's best strategy is to bid his true valuation, it is not clear whether he should submit an “unconditional” or a “conditional” bid in each situation. The bidder's best strategy depends on other bidders valuations.

Example 11. There are 2 tickets for sale, with a \$10 reserve price for each, and two bidders, Alice and Bob. Each ticket is worth \$15 to Alice, who is indifferent between obtaining either one or two tickets.

Clearly, Alice bids \$15 per item for both the bundle of 2 tickets and for a single ticket. The only question is whether to bid conditionally or unconditionally. Table 5 shows that Alice should always bid unconditionally because the number of tickets for sale is a multiple of each bundle size at both of the allocation steps. Note that in this and the following examples each column under the “bid type” header depicts a separate case.

To generalize, if A's marginal valuation for each item is at least the reserve and the number of goods unallocated before step i is exactly $2 ^ { m - i } I _ { i } ,$ which happens if and only if M is a multiple of $2 ^ { m - i }$ , then bidder $\boldsymbol { A } ^ { * } \boldsymbol { \mathrm { s } }$ best strategy is to always bid unconditionally for bundle sizes

Here is an example of the BVA auction where a bidder's best strategy is to always submit an “unconditional” bid for step i

<table><tr><td>Bidder</td><td>Qty.</td><td>Bid</td><td colspan="2">Bid type</td><td>Bid</td><td colspan="2">Bid type</td></tr><tr><td>Alice</td><td>2</td><td>$30</td><td>U</td><td>C</td><td>$30</td><td>U</td><td>C</td></tr><tr><td>Bob</td><td>2</td><td>-</td><td>-</td><td>-</td><td>$28</td><td>U</td><td>U</td></tr><tr><td>Alice</td><td>1</td><td>$15</td><td>-</td><td>U</td><td>$15</td><td>U</td><td>-</td></tr><tr><td>Bob</td><td>1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td rowspan="2">Alloc.</td><td>Alice</td><td></td><td>2</td><td>1</td><td></td><td>2</td><td>0</td></tr><tr><td>Bob</td><td></td><td>0</td><td>0</td><td></td><td>0</td><td>2</td></tr><tr><td rowspan="2">Payment</td><td>Alice</td><td></td><td>$20</td><td>$10</td><td></td><td>$28</td><td>$0</td></tr><tr><td>Bob</td><td></td><td>$0</td><td>$0</td><td></td><td>$0</td><td>$20</td></tr><tr><td rowspan="3">Utility</td><td>Alice</td><td></td><td>$10</td><td>$5</td><td></td><td>$2</td><td>$0</td></tr><tr><td>Bob</td><td></td><td>$0</td><td>$0</td><td></td><td>$0</td><td>$8</td></tr><tr><td>Seller</td><td></td><td>$0</td><td>$0</td><td></td><td>$8</td><td>$0</td></tr><tr><td colspan="2">Social surplus</td><td></td><td>$10</td><td>$5</td><td></td><td>$10</td><td>$8</td></tr></table>

In general, when the number of tickets unallocated before step i is exactly a multiple of the bundle size in step i, and a bidder's marginal valuation for each item meets the reserve, then his best strategy is to always submit an “unconditional” bid for the bundle allocated in step i.

$2 ^ { m - i }$ or smaller. If there are less than $I _ { i }$ unconditional bidders other than A and A bids unconditionally, he will get 2<sup>m−i</sup> goods at the reserve price. This is the best deal he can get because he cannot get anything below the reserve, and he still makes a profit (or at least breaks even) on every item he obtains since his marginal valuation of each item is at least the reserve price. If there are more than $I _ { i }$ unconditional bidders other than A, case 3 of the auction rules will be applied and it makes no difference whether A bids conditionally or unconditionally. If there are exactly $I _ { i }$ unconditional bidders other than A and A only bids conditionally, all unallocated goods will be sold to these unconditional bidders and none will be left for A, and so, again, he has to bid unconditionally.

Example 12. There are 3 tickets for sale, with a \$10 reserve price for each, and two bidders, Alice and Bob. Each ticket is worth \$15 to Alice, who is indifferent between obtaining either one or two tickets.

Table 6 shows that when the number of tickets for allocation before step 0 (i.e., 3) is not a multiple of the bundle size 2, whether Alice can obtain optimal utility from a conditional or unconditional bid depends on Bob's bids. If Bob's bid is high, Alice is better off bidding conditionally in order to get one ticket for \$10. If, however, Bob's bid for two tickets is low, Alice can obtain better utility by bidding unconditionally and paying Bob's bid.

To generalize, if the number of items unallocated before step i is not exactly $2 ^ { m - i } I _ { i } ,$ which happens if and only if M is not a multiple of $2 ^ { m - i }$ , it is unclear whether bidder $\boldsymbol { A } ^ { * } \boldsymbol { \mathrm { s } }$ best strategy is to bid conditionally or unconditionally. If the number of unconditional bidders except for A at step i is exactly $I _ { i } ,$ A's unconditional bid would cause the allocation to terminate at step i, and if there are at least $I _ { i }$ bids (considering conditional bids as well) above $\boldsymbol { A } ^ { * } \boldsymbol { \mathrm { s } }$ bid, A will not get anything. If A only submits a conditional bid, however, the auction would continue, and A might get a chance to obtain some goods.

Here is an example of the BVA auction where a bidder is uncertain whether to submit a “conditional” bid or an “unconditional” bid for step i

<table><tr><td>Bidder</td><td>Qty.</td><td>Bid</td><td colspan="2">Bid type</td><td>Bid</td><td colspan="2">Bid type</td></tr><tr><td>Alice</td><td>2</td><td>$30</td><td>C</td><td>U</td><td>$30</td><td>C</td><td>U</td></tr><tr><td>Bob</td><td>2</td><td>$28</td><td>U</td><td>U</td><td>$22</td><td>U</td><td>U</td></tr><tr><td>Alice</td><td>1</td><td>$15</td><td>U</td><td>U</td><td>$15</td><td>U</td><td>U</td></tr><tr><td>Bob</td><td>1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td rowspan="2">Alloc.</td><td>Alice</td><td></td><td>1</td><td>2</td><td></td><td>1</td><td>2</td></tr><tr><td>Bob</td><td></td><td>2</td><td>0</td><td></td><td>2</td><td>0</td></tr><tr><td rowspan="2">Payment</td><td>Alice</td><td></td><td>$10</td><td>$28</td><td></td><td>$10</td><td>$22</td></tr><tr><td>Bob</td><td></td><td>$20</td><td>$0</td><td></td><td>$20</td><td>$0</td></tr><tr><td rowspan="3">Utility</td><td>Alice</td><td></td><td>$5</td><td>$2</td><td></td><td>$5</td><td>$8</td></tr><tr><td>Bob</td><td></td><td>$8</td><td>$0</td><td></td><td>$2</td><td>$0</td></tr><tr><td>Seller</td><td></td><td>$0</td><td>$8</td><td></td><td>$0</td><td>$2</td></tr><tr><td colspan="2">Social surplus</td><td></td><td>$13</td><td>$10</td><td></td><td>$7</td><td>$10</td></tr></table>

In general, when the number of tickets unallocated before step i is not exactly a multiple of the bundle size in step i, whether a bidder will benefit more from a “conditional” or an “unconditional” bid depends on other buyers' bids.

Clearly, when M is not a multiple of $2 ^ { m - i }$ , and a bidder's objective is to maximize his utility, his decision on submitting a conditional or unconditional bid depends on the bids of others.

## 3.6.2. Prisoner's dilemma

Example 13. There are 2 tickets for sale, with a \$10 reserve price for each, and three bidders, Alice, Bob and Carol. Both Alice and Bob would each like to buy one ticket for at most \$15 and are also willing to accept two tickets for \$22.50 or less. Carol only wants one ticket for at most \$14.

Table 7 shows the possible bid combinations and the resulting allocations, utilities, and social surpluses.

The bidding scheme resulting in the maximum social surplus shows that the optimal allocation should give each of Alice and Bob one ticket for \$14 and each of them has a \$1 utility. The optimal allocation is achieved if no one bids unconditionally for two tickets. For Alice and Bob, however, it is not a stable strategy to bid conditionally for two tickets at their valuations. In the case that one of them bids unconditionally and the other bids conditionally, one who bids unconditionally will get \$2.5 utility while the other will get \$0 utility. In the case that both of them bid unconditionally, there will be a random draw for the winner and both the winner and the loser get \$0 utility.

## 3.6.3. Potential violation of individual rationality for bidders

In the BVA, if a bidder wants to purchase a power-oftwo number of goods, his payment will never exceed his valuation. Otherwise, in extreme cases where there is a strong complementarity among a bidder's valuations of the desired non-power-of-two unit of goods, a bidder can be unlucky in that he may have to pay more than his valuation.

Example 14. There are 3 tickets for sale, with a \$10 reserve price for each, and two bidders, Alice and Bob. Alice wants to buy all 3 tickets together for \$12 each and will not buy less than 3 tickets. Bob wants to buy 2 tickets for \$12 each or 1 ticket for either \$15 (in cases 1 and 2) or \$17 (in cases 3 and 4).

Table 7  
Example: “prisoner's dilemma” in the BVA

<table><tr><td>Bidder</td><td>Qty.</td><td>Bid</td><td colspan="4">Bid type</td></tr><tr><td>Alice</td><td>2</td><td>$22.5</td><td>C</td><td>U</td><td>C</td><td>U</td></tr><tr><td>Bob</td><td>2</td><td>$22.5</td><td>C</td><td>C</td><td>U</td><td>U</td></tr><tr><td>Carol</td><td>2</td><td>$14.0</td><td colspan="4">Below the reserve</td></tr><tr><td>Alice</td><td>1</td><td>$15.0</td><td rowspan="3" colspan="4">All Bids are considered as unconditional</td></tr><tr><td>Bob</td><td>1</td><td>$15.0</td></tr><tr><td>Carol</td><td>1</td><td>$14.0</td></tr><tr><td rowspan="3">Alloc.</td><td>Alice</td><td></td><td>1</td><td>2</td><td>0</td><td>2/0</td></tr><tr><td>Bob</td><td></td><td>1</td><td>0</td><td>2</td><td>0/2</td></tr><tr><td>Carol</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td rowspan="3">Payment</td><td>Alice</td><td></td><td>$14</td><td>$20</td><td>$0</td><td>$22.5/$0</td></tr><tr><td>Bob</td><td></td><td>$14</td><td>$0</td><td>$20</td><td>$0/$22.5</td></tr><tr><td>Carol</td><td></td><td>$0</td><td>$0</td><td>$0</td><td>$0</td></tr><tr><td rowspan="4">Utility</td><td>Alice</td><td></td><td>$1</td><td>$2.5</td><td>$0</td><td>$0</td></tr><tr><td>Bob</td><td></td><td>$1</td><td>$0</td><td>$2.5</td><td>$0</td></tr><tr><td>Carol</td><td></td><td>$0</td><td>$0</td><td>$0</td><td>$0</td></tr><tr><td>Seller</td><td></td><td>$8</td><td>$0</td><td>$0</td><td>$2.5</td></tr><tr><td colspan="2">Social surplus</td><td></td><td>$10</td><td>$2.5</td><td>$2.5</td><td>$2.5</td></tr></table>

Table 8 shows the possible outcomes in different cases. Clearly, Alice can only get all 3 tickets if she is the only unconditional bidder for the bundle of 2 tickets because Bob's bid is higher than Alice's. Alice only bids the minimum (i.e., \$20) for the bundle, rather than any higher value (say \$24), because she can only make a profit if she buys the third ticket. The third ticket is allocated only if the unconditional demand for the bundle of 2 tickets is less than the supply (i.e., when Alice is the only unconditional bidder for 2 tickets). Alice only needs to bid at the reserve in order to win, and bids any higher would risk her winning over another unconditional bidder, in which case the third ticket would be unsold and Alice would lose money. With her \$20 bid for 2 tickets, Alice's bid for one ticket should be \$36, which would be her marginal valuation for the third ticket.

When Bob bids conditionally for 2 tickets and more than \$16 (say \$17) for 1 ticket, Alice's utility becomes negative: although Alice gets all 3 tickets, she has to pay altogether \$37 altogether, which is higher than her valuation.

Assume there are more than 3 tickets (say 4) for auction and Alice's valuation for 3 tickets is \$40. Alice may bid unconditionally for 4 tickets, in which case her utility would be \$0 if she wins. If she does not bid for 4 tickets, it is uncertain whether she would have higher or lower utility. Alice's best strategy depends on the distribution of other bidders' valuations, and Alice can use the distribution to calculate her expected utility and choose the best strategy.

## 4. The BVA market mechanism

The problem with buyer false-name bids in one-sided auctions can occur in on-line exchange markets as well. Unfortunately, the current exchange mechanisms in practice are not designed to handle this type of fraud. The “Threshold Price Double Auction Protocol” in Ref. [19] is the only attempt so far to address this issue. However, its requirement that the clearing price be chosen by the auctioneer even before the sellers and buyers submit their bids makes this mechanism questionable because it defeats one of the main features of exchange markets — price discovery.

The following market mechanism is our suggestion on how to handle buyer false-name bids in double auctions. Here we extend the BVA auction protocol to a BVA market mechanism with which multiple sellers can sell multi-units of identical goods (e.g., a particular stock) to multiple buyers. The robustness against buyer false-name bids is preserved.

## Definition 15. (The BVA Market Mechanism)

There are t ≥ 1 sellers. Seller s $( s = 1 , . . . , t )$ has M<sup>s</sup> items for sale with a reserve price $r _ { s }$ for each item. Sellers are ordered according to their reserve prices: $r _ { 1 } \le . . . \le r _ { t } .$ Let $\begin{array} { r } { M { = } \sum _ { s { = 1 } } ^ { t } M ^ { s } } \end{array}$ . Choose m to satisfy $2 ^ { m } \leq M < 2 ^ { m + 1 }$ For each bundle size of $2 ^ { m - i }$ goods $( i { = } 0 , . . . , m )$ , a bidder can submit at most one sealed-bid and label it either “conditional” or “unconditional”. Bids for a single item are by default “unconditional”. Bidders submit their sealed-bids before the market price-clearing time. The market clears in at most m + 1 steps, starting with step 0.

Table 8  
Example: a violation of individual rationality in the BVA

<table><tr><td>Bidder</td><td>Qty.</td><td>Bid</td><td colspan="2">Bid type</td><td>Bid</td><td colspan="2">Bid type</td></tr><tr><td>Alice</td><td>2</td><td>$20</td><td>U</td><td>U</td><td>$20</td><td>U</td><td>U</td></tr><tr><td>Bob</td><td>2</td><td>$24</td><td>C</td><td>U</td><td>$24</td><td>C</td><td>U</td></tr><tr><td>Alice</td><td>1</td><td>$36</td><td>U</td><td>U</td><td>$36</td><td>U</td><td>U</td></tr><tr><td>Bob</td><td>1</td><td>$15</td><td>U</td><td>U</td><td>$17</td><td>U</td><td>U</td></tr><tr><td rowspan="2">Alloc.</td><td>Alice</td><td></td><td>3</td><td>0</td><td></td><td>3</td><td>0</td></tr><tr><td>Bob</td><td></td><td>0</td><td>2</td><td></td><td>0</td><td>2</td></tr><tr><td rowspan="2">Payment</td><td>Alice</td><td></td><td>$35</td><td>$0</td><td></td><td>$37</td><td>$0</td></tr><tr><td>Bob</td><td></td><td>$0</td><td>$20</td><td></td><td>$0</td><td>$20</td></tr><tr><td rowspan="3">Utility</td><td>Alice</td><td></td><td>$1</td><td>$0</td><td></td><td>-$1</td><td>$0</td></tr><tr><td>Bob</td><td></td><td>$0</td><td>$4</td><td></td><td>$0</td><td>$4</td></tr><tr><td>Seller</td><td></td><td>$5</td><td>$0</td><td></td><td>$7</td><td>$0</td></tr><tr><td colspan="2">Social Surplus</td><td></td><td>$6</td><td>$4</td><td></td><td>$6</td><td>$4</td></tr></table>

At step $i ( i { = } 0 , . . . , m )$ , the market maker only considers bids for the bundle size of $2 ^ { m - i }$ goods. “Unconditional” bids are always considered, but “conditional” bids are considered only if the “unconditional” demand exceeds the supply at the given bundle size. Let $M _ { i } ^ { s }$ be the number of unallocated goods before step i from the seller s with the reserve price $r _ { s }$ and $\begin{array} { r } { M _ { i } = \sum _ { s = 1 } ^ { t } M _ { i } ^ { s } } \end{array}$ . Let $\begin{array} { r } { I _ { i } ^ { s } = \left\lceil \frac { M _ { i } ^ { s } } { 2 ^ { m - i } } \right\rceil } \end{array}$ denote the number of unallocated bundles for <sup>¼</sup>step i from the seller s and $\begin{array} { r } { I _ { i } = \sum _ { s = 1 } ^ { t } I _ { i } ^ { s } = \left| \frac { M _ { i } } { 2 ^ { m - i } } \right| } \end{array}$ , where <sup>¼ ¼ ¼</sup>[x] denotes the largest integer not greater than x. By definition, $M _ { 0 } { = } M$ and $I _ { 0 } { = } 1$

Let $D _ { i } ( p )$ be the number of unconditional bids for a bundle size of $2 ^ { m - i }$ that is at least $2 ^ { m - i } p$ (the demand function), where $p$ denotes price. Let $S _ { i } ( p )$ be the number of bundles with size $2 ^ { m - i }$ offered with the price at most $2 ^ { m - i } p$ (the supply function).

Note that $\begin{array} { r } { \begin{array} { l r } { S _ { i } ( p ) = \sum _ { r _ { s < n } } } & { { } I _ { i } ^ { s } . } \end{array} \begin{array} { l r } { D _ { i } ( p ) } \end{array} } \end{array}$ is monotone decreasing whereas $S _ { i } ( p )$ is monotone increasing. Define $P _ { i } = \{ p { \in } R { : } \mathrm { D } _ { \mathrm { i } } ( \mathfrak { p } ) \mathrm { N S } _ { \mathrm { i } } ( \mathfrak { p } ) \}$ as the set of prices <sup>¼ f ð Þ ð Þg</sup>at which the unconditional demand exceeds supply in step i.

Allocation step i is conducted as follows:

(1) Only bids for the bundle size of $2 ^ { m - i }$ goods are considered.

(2) If $I _ { i } { = } 0$ or $P _ { i }$ is empty, the allocation proceeds to step $i + 1$ or terminates if $i { = } m$

(3) If $\dot { \boldsymbol { r } } _ { t } { \in } P _ { i }$ (i.e., there are more than $I _ { i } ^ { \phantom { \dagger } } { } ^ { \bullet }$ “unconditional” bids at or above the highest reserve price), both the “conditional” and “unconditional” bids are sorted in a decreasing bid order. Each of the $I _ { i }$ highest bidders gets $2 ^ { m - i }$ goods and pays the $( I _ { i } + 1$ )th highest bid. The auction terminates.

(4) Otherwise, let $p _ { i } { = } \mathrm { s u p }$ P (i.e., the price where the demand and supply functions intersect). If $D _ { i }$ $( p _ { i } ) \leq S _ { i } ( p _ { i } )$ , the $D _ { i } ( p _ { i } )$ bidders who bid $p _ { i }$ or higher win. Any remaining goods with the reserve price at $p _ { i }$ or higher are carried over to step $i + 1$ unless $i { = } m$ . If $D _ { i } ( p _ { i } ) { > } S _ { i } ( p _ { i } )$ , the $S _ { i } ( p _ { i } )$ highest bidders win. Any remaining goods with the reserve prices strictly greater than $p _ { i }$ are carried over to step $i + 1$ unless $i { = } m$ . Each of the winning bidders pays $2 ^ { m - i } p _ { i }$ . “Conditional” bids are not considered. $\operatorname { I f } i = m$ or if there are no goods left for sale for step $i + 1$ , the auction terminates. Otherwise, the allocation proceeds to step $i + 1$

Note that in the case of a single seller, the BVA market mechanism is the same as the BVA one-sided auction protocol in Definition 3.

Next we show that the incentive compatibility theorem and all the lemmas that we have proved about the BVA one-sided auction protocol still hold in the BVA market mechanism. These proofs can be carried over based on the following lemma:

Lemma 16. In the BVA market mechanism, the payment for a single item is mono-tone increasing along the allocation steps, excluding the steps where no good is allocated.

Proof. By definition, in every step where goods are allocated, only the remaining goods with the reserve price no less than the sale price per item in the current step are carried over to subsequent steps. This guarantees that the payment for a single item is non-decreasing along the allocation steps. □

Hence, we have:

Theorem 17. The BVA market mechanism is incentivecompatible even if buyers can submit false-name bids.

Moreover, the BVA market mechanism is incentivecompatible for sellers as well in that, sellers truthfully disclose their reserve prices even though they can submit bids under false buyer identities for their own items. This is because each allocation step of the BVA market mechanism is a sealed-bid auction, in which submitting a shill bid has the same effect as setting the reserve at the shill bid level [17].

The following theorem states that the BVA market mechanism has a linear computational complexity.

Theorem 18. In a BVA market mechanism, let M be the total number of goods for sale, t be the number of sellers, and b be the total number of bids. The market clearing can be determined in $O ( ( t + b ) \log M )$ time.

Proof. Since the number of steps is at most log $M + 1$ it is enough to show that the allocation for each step can be decided in $O ( t + b )$ time.

$S _ { i } ( p )$ and $D _ { i } ( p )$ are stair-like functions. The value of $S _ { i } ( p )$ only jumps when p equals the reserve price of one of the sellers. Similarly, $D _ { i } ( p )$ only drops if p equals one of the unconditional bids. Therefore $S _ { i } ( p ) , D _ { i } ( p ) , P _ { i }$ and $p _ { i }$ can be calculated in $O ( t + b )$ time.

Theorem 18 immediately follows if we can select the $I _ { i }$ or $S _ { i } ( p _ { i } )$ highest bids in $O ( t + b )$ time. In fact, we can even do so in $O ( b )$ time because the number of bids is b. □

## 5. Concluding remarks

Changes in the commerce and business environments demand the modification or even an entirely new design of traditional market trading rules and business policies. Unlike in a fixed-price transaction where the structure of buying and selling is simple and hence easy to be transcribed into the digital market, the structure of auctions, where prices are determined dynamically and trades can be accessed by anyone from the globe, is much more complicated. This complexity leaves more room for fraud. In order for an auction mechanism to maintain itself in the new Internet trading environment, it is crucial to ensure that its structure fulfills the desired objectives of legitimate agents.

Our BVA auction protocol is designed to be computationally efficient and to have a structure robust against buyer false-name bids and hence protective to the social welfare in multi-unit sealed-bid online auctions. In a BVA auction, both the bids and the allocation of goods are in various bundles of power-of-two items. This binary operation makes the BVA computationally very efficient for auctioneers and sellers and also contributes to a systemic design that makes the BVA robust against buyer false-name bids. The BVA favors bids for larger bundles with earlier considerations and cheaper prices, which inhibits bidders' incentive to split a bid for a larger bundle into several bids for smaller bundles under false identities.

As we have mentioned before, in practical market design, we need to consider the trade-off between the mathematical optimization results abstract from the reality and the added constraints caused by trading environments and applied technology. Consideration of the practical trading environments will lead to sacrifices in objectives, such as the reduction in social surplus, efficiency, or simplicity. Hence, our design goal is to search for the second-best mechanism that is still nearly optimal, but resilient to online fraud. Based on buyers' value distribution, none of the existing multi-unit sealedbid auction protocols can achieve optimal performance. In some cases the existing buyer-false-name-proof multiunit sealed-bid protocols – LDS, LPS, and IR – significantly reduce the social surplus. Our BVA reduces social surplus as well, but not as much as in the LDS, LPS, and IR auctions. In extreme cases, the BVA may violate rationality, but its robustness against false-name bids is always achieved and the computational complexity of allocation is much reduced, making the BVA protocol easier to implement, compared to the VCG, LDS, LPS and IR protocols.

We also extend the BVA for double auctions. We believe the computational efficiency of our BVA market mechanism can especially benefit the large scale operation of B2B exchange markets.

## References

[1] Mark Armstrong, Optimal multi-object auctions, Working Paper, 1999.

[2] Lawrence M. Ausubel, An efficient ascending-bid auction for multiple objects, University of Maryland Working Paper, vol. 97-06, June 1997.

[3] Lawrence M. Ausubel, Peter Cramton, Demand reduction and inefficiency in multi-unit auctions, Working Paper, July 2002.

[4] Christopher Avery, Terrence Hendershott, Bundling and optimal auctions of multiple products, Review of Economic Studies 67 (2000) 483–497.

[5] Manuel Blum, Robert W. Floyd, Vaughan Pratt, Ronald L. Rivest, Robert E. Tarjan, Time bounds for selection, Journal of Computer and System Sciences 7 (August 1973) 448–461.

[6] Indranil Chakraborty, Georgia Kosmopoulou, Auctions with shill bidding, Economic Theory 24 (2) (August 2004) 271–287.

[7] Edward H. Clarke, Multipart pricing of public goods, Public Choice 11 (1971) 17–33.

[8] Richard Engelbrecht-Wiggans, Charles M. Kahn, Multi-unit auctions with uniform prices, Economic Theory 12 (1998) 227–258.

[9] Theodore Groves, Incentives in teams, Econometrica 41 (4) (July 1973) 617–631.

[10] Atsushi Iwasakia, Makoto Yokooa, Kenji Terada, A robust open ascending-price multi-unit auction protocol against false-name bids, Decision Support Systems 39 (1) (March 2005) 23–39.

[11] Paul Milgrom, Putting Auction Theory to Work, Cambridge University Press, Cambridge, UK, 2004.

[12] D. Nautz, Optimal bidding in multi-unit auctions with many bidders, Economics Letters 48 (1995) 301–306.

[13] Yuko Sakurai, Makoto Yokoo, Koji Kamei, A limitation of the generalized Vickrey auction in electronic commerce: Robustness against false-name bids, The Proceedings of the 16th National Conference on Artificial Intelligence (AAAI-99), 1999.

[14] Atanu R. Sinha, Eric A. Greenleaf, The impact of discrete bidding and bidder aggressiveness on sellers' strategies in open English auctions: reserves and covert shilling, Marketing Science 19 (3) (Summer 2000) 244–265.

[15] Hal R. Varian, Economic mechanism design for computerized agents, Proceedings of the First USENIX Workshop on Electronic Commerce, New York, New York, July 1995, pp. 13–21.

[16] Wenli Wang, Zoltán Hidvégi, Andrew B. Whinston, Designing mechanisms for e-commerce security: an example from sealedbid auctions, International Journal of Electronic Commerce 6 (2) (Winter 2001–2002) 113–130.

[17] Wenli Wang, Zoltán Hidvégi, Andrew B. Whinston, Shill-proof fee (spf) schedule: the sunscreen against seller self-collusion in online English auctions, Working Paper, October 2004.

[18] Makoto Yokoo, Yuko Sakurai, Shigeo Matsubara, Robust combinatorial auction protocol against false-name bids, The Proceedings of the 17th National Conference on Artificial Intelligence, August 2000, pp. 110–115.

[19] Makoto Yokoo, Yuko Sakurai, Shigeo Matsubara, Robust double auction protocol against false-name bids, The Proceedings of the 21st IEEE International Conference on Distributed Computing Systems (ICDCS-2001), 2001.

[20] Makoto Yokoo, Yuko Sakurai, Shigeo Matsubara, Robust multiunit auction protocol against false-name bids, The Proceedings of the 17th International Joint Conference on Artificial Intelligence (IJCAI-2001), 2001.

[21] Makoto Yokoo, Yuko Sakurai, Shigeo Matsubara, The effect of false-name bids in combinatorial auctions: new fraud in internet auctions, Games and Economic Behavior 46 (1) (January 2004) 174–188.
