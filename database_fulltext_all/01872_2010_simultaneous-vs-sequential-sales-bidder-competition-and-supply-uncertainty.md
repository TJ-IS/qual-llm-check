---
otero_id: 1872
otero_key: "ERDR7JKF"
title: "Simultaneous vs. sequential sales: Bidder competition and supply uncertainty"
authors: "Juan Feng; Kalyan Chatterjee"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.02.011"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Simultaneous vs. sequential sales: Bidder competition and supply uncertainty

Juan Feng <sup>a,</sup>⁎, Kalyan Chatterjee <sup>b</sup>

<sup>a</sup> College of Business, City University of Hong Kong, Hong Kong

<sup>b</sup> Department of Economics, Penn State University, State College, PA, USA

## a r t i c l e i n f o

Article history: Received 18 April 2009 Received in revised form 8 December 2009 Accepted 25 February 2010 Available online 10 March 2010

Keywords: Sequential auction Simultaneous auction Competition intensity supply uncertaint Forward-looking

## a b s t r a c t

Under what circumstances will a seller be better off selling the inventory sequentially, rather than selling it all in a single auction? Does it bene<sup>fi</sup>t the seller to reveal how many auctions there will be? We study a uniform-price auction, in which bidders demand no more than one item, and have independent, private values. We show that even (1) when all buyers are present at the beginning of the auction, and (2) when both the seller and the buyers are impatient, a sequential sale can still bene<sup>fi</sup>t the seller as it stimulates competition among forward-looking bidders. This result depends on: (1) the bidder competition intensity, which is characterized by the difference between the number of items available and the number of buyers; and (2) the impatience levels of the auctioneer and the bidders. We also show that when there is uncertainty about the quantity supplied, a high-inventory auctioneer may bene<sup>fi</sup>t from using sequential auctions by pretending to be a low-inventory one initially.

Published by Elsevier B.V.

## 1. Introduction

Auctioning off a large number of identical items is often observed when selling consumer products in both internet auctions (eBay.com, samsclub.com, onsale.com) and physical auction houses, not to mention the transactions of production supplies in B2B procurement markets such as Ariba.com. This brings up several important questions: First, when selling multiple items, should the seller sell all the items together in one auction, or split them up and sell them off sequentially? Auctioning off a large number of similar items simultaneously may lead to some of them being sold for very low prices due to a lack of competition. For example, Christie's in New York hosted an auction of 600 Picasso lithographs in April 2003. In an article on Christie's web site,<sup>1</sup> Jonathan Rendell, the Deputy Chairman of the auction house, mentioned that the consignor had decided to sell with no reserve price, and that the estimated prices were as low as <sup>fi</sup>ve hundred dollars. A sequential sale, however, may not be appealing when either the auctioneer or the bidders are impatient. Second, should the seller inform bidders as to the number of items available for sale, or, equivalently, how many auctions will there be? Both information policies are observed in practice. For example, at auctions. samsclub.com, while Fig. 1 shows that the auctioneer (Sambsclub. com) sells the 50-inch Samsung Plasma 720p HDTV using sequential auctions, it is not clear from Fig. 2 whether there will be a future sale for the 32-inch Sharp Aquos 1080p HDTV.<sup>2</sup>

In this paper we study whether a sequential sale is more pro<sup>fi</sup>table than a simultaneous sale when both the auctioneer and bidders are impatient, and if so, under what conditions. More importantly, we study the auctioneer's decision as to whether to inform bidders about the number of items available for sale. Not revealing a future auction may promote competition among bidders when the auctioneer has a large inventory, which increases the auctioneer's expected pro<sup>fi</sup>t. Anticipating a future auction when there is actually none may, however, lower the current-period bids of the bidders, thus reducing the payoff to the auctioneer. In the Sam's Club example (of Fig. 2), it is not clear whether comparable items are being kept off the market for a future auction. Bidders in our stylized model have independent, private values and demand no more than one item. They are also strategic, forward-looking players who can predict the auctioneer's optimal strategy.

Our analysis identi<sup>fi</sup>es three important factors that affect the pro<sup>fi</sup>tability of a sequential auction: (1) the bidder competition intensity (characterized by the difference between the number of items for sale and the number of bidders); (2) the impatience levels of the auctioneer and the bidders; and (3) the auctioneer's information policy with respect to the number of items available for sale. More speci<sup>fi</sup>cally, we show that a sequential sale can help promote competition among impatient bidders when the intensity of bidder competition is low. When there exists uncertainty about the quantity supplied, a high-inventory auctioneer may bene<sup>fi</sup>t from using sequential auctions by pretending to be a low-inventory auctioneer in the <sup>fi</sup>rst auction. We further examine a high-inventory auctioneer's optimal timing as to when to reveal the true inventory information in a T-period setting.

![](/api/attachments/ERDR7JKF/fulltext/images/fdbe6dcac8d8486739c49edb20235f5540a296d8db22008e0ae531c4b2c21186.jpg)  
Fig. 1. Sequential auctions at Samsclub.com.

The remainder of the paper is organized as follows. In the next section we brie<sup>fl</sup>y survey the previous literature. Section 3 introduces the environment and notation, presents the benchmark case in which the auctioneer's inventory is common knowledge, and studies the auctioneer's revenue-maximizing choice between a simultaneous sale and a sequential sale.

Section 4 extends the analysis to acknowledge the fact that the auctioneer's inventory is not publicly available, but rather that it is the auctioneer's choice as to whether to reveal the inventory information. Section 5 discusses the optimal timing for the auctioneer to reveal this information in a T-period setting. Finally, Section 6 concludes the paper and discusses future extensions.

## 2. Literature review

Auction mechanisms have attracted a lot of academic attention in the recent years. Previous literature in sequential auctions ([21], later summarized by [12]) has found that when the values of the bidders are independent and private, and each bidder demands only one item, the auctioneer's expected payoff is the same from selling all the items in one period, or one in each period. Moreover, the expected winning prices are constant in each period. However, [21] assumes that both the bidders and the auctioneer do not discount time.

![](/api/attachments/ERDR7JKF/fulltext/images/37acac224a653d78f88f2a6e708f91a01549218071bf60fd7cd7d533f0428b70.jpg)  
Fig. 2. A “single” auction at Samsclub.com.

Table 1

<table><tr><td></td><td>Seq. auction</td><td>Seq. vs.sim auction</td><td>Discount/ delay cost</td><td>Forward- looking bidders</td><td> $\geq 2$  bidders</td><td>Information policy</td></tr><tr><td>[21]</td><td>N</td><td>Y</td><td>N</td><td>Y</td><td>Y</td><td>N</td></tr><tr><td>[1,11,17,20]</td><td>Y</td><td>N</td><td>N</td><td>N</td><td>Y</td><td>N</td></tr><tr><td>[23]</td><td>Y</td><td>Y</td><td>N</td><td>Y</td><td>Y</td><td>N</td></tr><tr><td>[10,14]</td><td>Y</td><td>N</td><td>Y</td><td>Y</td><td>Y</td><td>N</td></tr><tr><td>[4,5,9,16]</td><td>N</td><td>Y</td><td>N</td><td>N</td><td>N</td><td>N</td></tr><tr><td>[6]</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>Y</td><td>Y</td></tr><tr><td>This paper</td><td>Y</td><td>Y</td><td>Y</td><td>Y</td><td>Y</td><td>Y</td></tr></table>

[14] studies a sequential auction of stochastically-equivalent items when the bidders incur a <sup>fi</sup>xed cost of delay. [10] <sup>fi</sup>nds that depending on the information about the supply after the <sup>fi</sup>rst auction, the bidding prices in a sequential auction may either increase or decline. Neither paper compares the pro<sup>fi</sup>tability of a sequential auction to that of a simultaneous one. [9], by contrast, compares a sequential sale to a simultaneous one in a two-object, two-bidder setting. As each bidder demands more than one item, they may learn the value of the objects from previous auctions. Both [16] and [4] <sup>fi</sup>nd that the number of bidders is critical in determining whether bundling two non-identical items for sale generates more revenue than does selling the items separately. [5] further considers the effect of entry cost. In these papers each bidder demands multiple items, which is different from our setting. Moreover, these papers do not consider whether the auctioneer should reveal how many auctions there will be, and this is one focus of our paper, which is one important measure for market transparency [8].

Many papers studying optimal lot sizing in sequential auctions assume that bidders arrive sequentially but are myopic, that is, they only participate in the current auction and do not care about future auctions (e.g. [1,17] and [11]). [20] consider an optimal dynamic auction in which both the number of bidders and their valuations are stochastic. The existence of strategic bidders who respond to the optimal strategy of the auctioneer may, however, change the equilibrium outcome [18]. For example, [23] <sup>fi</sup>nds that forward-looking buyers underbid when they anticipate another auction in the near future. But in his model there is no uncertainty about the auctioneer's inventory. [6] <sup>fi</sup>nds that an auctioneer has an incentive to release less information than is ef<sup>fi</sup>cient in order to promote competition. By contrast, in our model we consider a different kind of information, namely, information with regard to the available inventory. Table 1 summarizes the differences between our paper and the existing literature.

## 3. The benchmark model with commonly-known inventory information

## 3.1. Model setup

In our benchmark model, a risk-neutral auctioneer has K identical items to sell, with a commonly-known reservation price of zero for the item. There are n symmetric risk-neutral bidders, each of whom seeks to purchase one item if the price is less than or equal to a private value, v, which is drawn identically and independently from a common, absolutely continuous distribution F. All K, n and $F \left( \cdot \right)$ are common knowledge

Bidders are assumed to be forward-looking in the sense that when they know that identical items will be offered in a future auction, their current-period bids will re<sup>fl</sup>ect their potential bene<sup>fi</sup>ts from losing out in the current auction and winning in the future. We use a commonly adopted auction format when studying sequential auctions: namely, a sealed-bid, uniform-price auction without a reservation price is held in each of the two periods,<sup>3</sup> and the bidders are present at the beginning of the <sup>fi</sup>rst auction [10,16]. In the uniform-price setting, all winners pay the bid from the highest rejected bidder. The simpli<sup>fi</sup>- cation that no additional bidders arrive for the second auction sets up a simplest scenario where a sequential sale is likely to be less pro<sup>fi</sup>table than a simultaneous one. This assumption is also common in of<sup>fl</sup>ine auctions. In the Picasso lithograph example, there was no evidence that a substantial number of potential buyers were not present at the time of the proposed auction. In procurement auctions, the buyer often has a short list of pre-quali<sup>fi</sup>ed bidders and it is a non-trivial task to get into this list.

Before the bidding starts, the bidders observe the number of items for sale and decide whether and how much to bid. While winners leave the scene after the <sup>fi</sup>rst auction, the rest of the bidders remain for any second auction and reconsider their bids. The auctioneer's problem is to choose whether to sell the inventory in one or two auctions, and when a sequential sale is used, the number of items to sell in the two auctions. We assume that the winning price in the <sup>fi</sup>rst period is revealed when a sequential sale is used. As in the lithographs example above, the seller in our model does not control the total number of items she has to sell. This distinguishes the problem from that of a monopolistic seller who can choose how many items to produce or acquire.

Assume both the auctioneer and the bidders are impatient, with a discount factor $\delta _ { 0 } \in [ 0 , 1 ]$ for the auctioneer, and $\delta \in [ 0 , 1 ]$ for the bidders. For example, a well-established, big-budgeted auctioneer might be more patient than the bidders, especially when selling a highly-popular good, such as Wii, which is almost always in short supply and is demanded by customers who want to get it home as soon as possible $\left( \delta _ { 0 } 2 \delta \right)$ . Similarly, bidders who are eager for a time-sensitive item, such as aluminum Christmas trees, may be more impatient than the auctioneer as the holiday season approaches. An auctioneer selling Evergreen trees that cannot be stored for “next” year is likely to be less patient than bidders $( \delta _ { 0 } \le \delta )$ . In addition, we only consider the case where the number of bidders is greater than the total number of items for sale, that is, nNK. In addition, the following notation is used in the analysis:<sup>4</sup>

1. $\beta ^ { t } ( \nu )$ : The $t ^ { \mathrm { t h } } .$ -period bidding function for a bidder with valuation v; 2. $Y _ { k } \mathrm { : }$ the $k ^ { \mathrm { { t h } } }$ highest valuation among $n - 1$ bidders;

3. $X _ { k } \colon$ : the $k ^ { \mathrm { { t h } } }$ highest valuation among all n bidders; and

4. E[·]: the expected value.

## 3.2. Sequential auction vs. simultaneous auction

First consider the bidder's strategy in a sequential auction in which the auctioneer sells $k _ { 1 }$ items in the <sup>fi</sup>rst auction, and the remaining $K - k _ { 1 }$ in the second. Using backward induction, we start with an analysis of the second auction, assuming that the $k _ { 1 }$ highest bidders win in the <sup>fi</sup>rst period and leave, and the remaining $n - k _ { 1 }$ bidders participate in what is known to be the second auction. By standard auction theory, truth telling is the weakly-dominant strategy for bidders with unit demand.

Now consider the <sup>fi</sup>rst auction. Since bidders have the option to participate in the second auction and win an item at a possibly lower price, their initial bid should make them indifferent between participating in the <sup>fi</sup>rst and the second auction. More speci<sup>fi</sup>cally, let $\beta ^ { t } ( \nu )$ denote the tth-period equilibrium bidding function that is continuous and monotonically increasing for a bidder with valuation v (we will later show that this is actually the case.) The expected payoff for a bidder of value v if participating in the <sup>fi</sup>rst auction is:

$$
\left\{ \begin{array}{l l} v - \beta^ {1} (Y _ {k _ {1}}) & \text { if } v \geq Y _ {k _ {1}}, \\ \delta   m a x \{E [ (v - Y _ {K}   |   v > Y _ {K} ], 0 \} & \text { otherwise }. \end{array} \right.\tag{1}
$$

Lemma 1 (Equilibrium Bidding Strategy in a Sequential Auction). In a sequential sale with $k _ { 1 }$ items for sale in the first auction, and the rest in the second auction, the equilibrium bidding strategy for a bidder with value of v is:

$$
\left\{ \begin{array}{l l} \beta^ {1} (v) & = (1 - \delta) v + \delta E \Big [ Y _ {K} | v = Y _ {k _ {1}} \Big ]; \\ \beta^ {2} (v) & = v. \end{array} \right.\tag{2}
$$

Note that when $\delta = 1$ and $k _ { 1 } = 1$ , we have $\beta ^ { 1 } ( \nu ) = E \ [ Y _ { 2 } | \nu = Y _ { 1 } ]$ which is the same as the standard results in [21]. The proof for this and all other major results is presented in the Appendix.

Lemma 1 shows that, a bidder's <sup>fi</sup>rst-period bid should be discounted by his expected gain in the second auction, which makes him indifferent between winning in the <sup>fi</sup>rst auction and the second. That is, a forwardlooking bidder should not bid too high in the <sup>fi</sup>rst auction, otherwise if he wins, he might “regret” that he did not wait and win in the second auction, for a possibly lower price; he should not bid too low, either, otherwise he could lose in the <sup>fi</sup>rst period and be forced to participate in the second auction and delay his consumption of the product.

It can be veri<sup>fi</sup>ed that the equilibrium bidding functions in both periods, $\beta ^ { 1 } ( \nu )$ and $\beta ^ { 2 } ( \nu ) ,$ , are both increasing in v, so we can conclude that the auction is ef<sup>fi</sup>cient in the sense that it allocates the item to the K bidders with the highest valuations. A sequential sale may be inefficient, however, when $\delta { < } 1 ,$ , because the consumption of the item is delayed for some bidders.

Given the equilibrium bidding strategy, the expected winning prices of the sequential auction, are the $k _ { 1 } +$ 1st highest ranked bid in the <sup>fi</sup>rst auction, and the K+1st highest ranked bid in the second auction. Let E[R2] represent the auctioneer's total revenue in the sequential auction, we have:

$$
E [ R 2 ] = (1 - \delta) k _ {1} E \left[ X _ {k _ {1} + 1} \right] + \delta k _ {1} E \left[ X _ {K + 1} \right] + \delta_ {0} (K - k _ {1}) E \left[ X _ {K + 1} \right],\tag{3}
$$

where the <sup>fi</sup>rst two terms on the right hand side represent the auctioneer's expected revenue from the <sup>fi</sup>rst auction, and the third term represents that from the second period.

Eq. (3) shows that the auctioneer's expected revenue depends on both the relative magnitudes of n and $K ,$ and on the difference between δ and $\delta _ { 0 } .$ Speci<sup>fi</sup>cally, δ and $\delta _ { 0 }$ affect the auctioneer's expected revenue in two opposing directions: the more impatient are the bidders (the smaller the $\delta ) _ { }$ , the more aggressively they bid in the <sup>fi</sup>rst auction in re<sup>fl</sup>ection of their impatience to acquire the item, which increases the auctioneer's expected revenue; while the more impatient is the auctioneer, the less she values the second auction. The result is summarized by Lemma 2.

Lemma 2 (Seller's Expected Revenue Using Sequential Auctions). The auctioneer's expected revenue using a sequential auction is determined by: $\begin{array} { r } { E [ R 2 ] = ( 1 - \delta ) k _ { 1 } E [ X _ { k _ { 1 } + 1 } ] + \delta k _ { 1 } E [ X _ { K + 1 } ] + \delta _ { 0 } ( K - k _ { 1 } ) E [ X _ { K + 1 } ] , } \end{array}$ which is increasing in $\delta _ { 0 }$ but decreasing in δ.

To illustrate, the market for Wii comprises mainly of young adults and teenagers, who are more likely to be impatient than consumers of everyday household items such as kitchen appliances. Thus, a single seller, such as overstock.com, may bene<sup>fi</sup>t more from hosting sequential auctions when offering Wii than when offering coffee machines.

Henceforth we proceed under the assumption that bidder valuations follow a uniform distribution over [0, 1]. Assume that the auctioneer is free to choose an optimal quantity $\boldsymbol { ( k _ { 1 } ^ { * } ) }$ to put on offer in the <sup>fi</sup>rst auction. De<sup>fi</sup>ne Int(x) as the closest integer to x, We now arrive at Lemma 3:

Lemma 3 (Optimal Quantity to Sell in the First period). The optimal quantity to sell in the first period is: $\begin{array} { r } { k _ { 1 } ^ { * } = m i n \Big \{ K , I n \ ' ( \frac { n } { 2 } + \frac { \hat { 8 } - \hat { 8 } _ { 0 } } { 1 - \hat { 8 } } ( n - K ) ) \Big \} } \end{array}$

Lemma 3 shows that the optimal quantity to offer in the <sup>fi</sup>rst auction is largely determined by the intensity of competition among the n bidders. That is, $n - K$ plays a critical role in determining $k _ { 1 } ^ { * }$ Intuitively, the more bidders chasing the limited number of K items, the higher they bid due to the competition, thus the more the auctioneer could put up to sell in the <sup>fi</sup>rst auction. The discount factors are also important in determining the optimal <sup>fi</sup>rst-auction quantity: the auctioneer should offer more in the <sup>fi</sup>rst auction when facing patient bidders, because the bene<sup>fi</sup>t of a sequential auction to raise bidders' <sup>fi</sup>rst-period bids is limited. A patient auctioneer, however, should offer less in the initial auction. When the auctioneer has the same patience level as the bidders, it is straightforward to see that the optimal quantity reduces to Int $( \frac { n } { 2 } )$ .

Now consider the case when the auctioneer decides to sell all of her items in a single period. By standard auction theory, the bidders equilibrium bidding strategies are to bid their true values. Let E[R1] represent the expected revenue of the auctioneer in such a simultaneous auction. Then,

$$
E [ R 1 ] = K \cdot E [ X _ {K} ].\tag{4}
$$

Comparing Eqs. (3) and $( 4 ) ,$ it can be shown that when $\delta = \delta _ { 0 } = 1$ $E [ R 2 ] = E [ R 1 ]$ . That is, when neither the auctioneer nor the bidders discount time, the sequential auction produces the same expected revenue as the simultaneous auction, which reduces to the standard result from Weber (1983).

Comparing the expected revenue from using a simultaneous auction and sequential auctions with $k _ { 1 } ^ { * }$ items for sale in the <sup>fi</sup>rst auction, we have:

Proposition 1 (Comparison of Simultaneous Auction and Sequential Auctions). A sequential auction generates more expected revenue than a simultaneous one when the bidder competition is weak. Speci<sup>fi</sup>cally, sequential auctions should be used when:

$$
\begin{array}{l} 1. n <   \min \Bigl \{2 K, \frac {2 - 2 \delta_ {0}}{1 + \delta - 2 \delta_ {0}} K \Bigr \} i f 1 + \delta - 2 \delta_ {0} > 0; \\ \text { or } \\ 2. n <   2 K i f 1 + \delta - 2 \delta_ {0} \leq 0. \end{array}
$$

Note that when $\delta _ { 0 } = \delta ,$ a sequential sale generate more revenue than a simultaneous auction when $n { < } 2 K .$ Proposition 1 shows that, a sequential sale may be more pro<sup>fi</sup>table than a simultaneous one even when both the auctioneer and the bidders are impatient, and when the bidders have independent, private values and demand only one unit. Sequential auctions can be used to heat up competition when bidder competition is weak in the market (when nbmin $\Big \{ 2 K , I n t ( \frac { 2 - 2 \delta _ { 0 } } { 1 + \delta - 2 \delta _ { 0 } } K ) \Big \} . )$ In addition, the patience levels of both the auctioneer and the bidders also affect the pro<sup>fi</sup>tability of a sequential auction. A low $\delta _ { 0 }$ reduces the auctioneer's future payoff, while a low δ encourages bidders to bid more aggressively in the <sup>fi</sup>rst auction, which is bene<sup>fi</sup>cial to the auctioneer. The more impatient are the bidders relative to the auctioneer (the smaller the δ relative to $\delta _ { 0 } )$ , the more likely is a sequential auction to be more pro<sup>fi</sup>table than a simultaneous auction. This suggests that, when selling highly popular and time-sensitive items, where bidders are likely to be less patient than is the auctioneer, a sequential auction may be a better choice; while a small-budgeted auctioneer, who is eager to clear inventory in order to gain early cash <sup>fl</sup>ow is likely to be less patient than bidders, may <sup>fi</sup>nd a simultaneous sale to be more rewarding.

## 4. Bidders uncertain about the number of auctions

We now consider the case in which the auctioneer does not announce how many auctions there will be, or equivalently, the auctioneer does not reveal her inventory information. Suppose that the auctioneer may be either a high-inventory type with $K _ { H }$ items for sale, or a low-inventory type with $K _ { L }$ items for sale, where $K _ { H } { > } K _ { L } { > } 0 .$ When the bidders come to the auction site and observe $k _ { 1 } < k _ { 1 } ^ { * }$ items for sale (recall $\begin{array} { r } { k _ { 1 } ^ { * } = m i n \Big \{ K _ { H } , I n t ( \frac { n } { 2 } + \frac { \delta - \delta _ { 0 } } { 1 - \delta } ( n - K _ { H } ) ) \Big \} } \end{array}$ , which refers to the optimal number of items for sale in the <sup>fi</sup>rst auction for the H type auctioneer, as speci<sup>fi</sup>ed in Section 3), they do not know whether there will be a future auction selling identical items. For example, many sellers on eBay sell goods sequentially, but the total inventory is not always revealed. Thus, the auctioneer must determine how much inventoryrelated information to reveal when a sequential auction is used. [15] indicate that in a single-unit auction where values of bidders are af<sup>fi</sup>liated, the auctioneer is always better off by providing bidders with as much value-related information as possible. Endogenizing competition might lead to different results (Ganuza (2004)). Communicating how many auctions there will be is a somewhat different kind of information. In this section we study the strategic decision of the auctioneer as to whether or not to reveal this information.

![](/api/attachments/ERDR7JKF/fulltext/images/0366ec7f6b8ea71cf7a9c70abc873087563eb9b1b54b2c714f6aac65239ac8bb.jpg)  
Fig. 3. Auctioneer's strategy.

Fig. 3 illustrates the following game: At the outset, “Nature” determines whether the auctioneer is a high type (H) who has $K _ { H }$ items on hand, or a Low type (L) who has only $K _ { L }$ items on hand, where $K _ { H } { > } K _ { L }$ and $K _ { L } { < } k _ { 1 } ^ { * }$ . With probability $\rho$ the auctioneer is a high type, and with $1 { - } \rho$ she is a low type. Both $K _ { H }$ and $K _ { L } ,$ , as well as the belief $\rho$ are common knowledge. The H auctioneer, then, has two choices: (a) to reveal her inventory information by selling $k _ { 1 } ^ { * }$ items in the <sup>fi</sup>rst auction and the remaining items (if any) in the second auction, or (b) to hide the inventory information by pretending to be an L type and selling $K _ { L }$ items in the <sup>fi</sup>rst period.

We consider equilibria in which the H type auctioneer pretends to be an L type in the <sup>fi</sup>rst auction with probability α [0, 1], and reveals her type by selling $k _ { 1 } ^ { * }$ with probability $1 - \alpha .$ Bidder beliefs are assumed to be the following: when $k { > } K _ { L }$ items are offered for sale in the <sup>fi</sup>rst auction, the auctioneer is believed to be an H type; when $k { \le } K _ { L } ,$ the auctioneer is believed to be an H type with probability of ${ \frac { \displaystyle \alpha \rho } { \displaystyle \alpha \rho + ( 1 - \rho ) } } ,$ and an L type with probability $1 - { \frac { \alpha \rho } { \alpha \rho + ( 1 - \rho ) } } .$ So, the L type <sup>ð Þ</sup>auctioneer will always sell all $K _ { L }$ <sup>ð Þ</sup>items in one auction because $K _ { L } < k _ { 1 } ^ { * } .$ Similarly, the H auctioneer has no incentive to sell $k { < } K _ { L }$ or $K _ { L } { < } k { < } k _ { 1 } ^ { * }$ items in the <sup>fi</sup>rst auction. Given bidders' belief, their equilibrium bidding strategies can be derived $\mathtt { a s }$ in Section 3. Based on these bidding strategies, Proposition 2 speci<sup>fi</sup>es the H type auctioneer's equilibrium strategy:

Proposition 2 (H's Choice between a Simultaneous Auction and Sequential Auctions). In equilibrium, in the <sup>fi</sup>rst auction, the H auctioneer pretends to be an L type by selling $K _ { L }$ items with probability $\alpha ,$ and selling $k _ { 1 } ^ { * }$ items with probability $1 - \alpha ,$ where

$$
\begin{array}{l} 1. \alpha = 0, \text {   if   } \tilde {\rho} \leq 0; \\ 2. \alpha \text {   satisfies   } \frac {\alpha \rho}{\alpha \rho + (1 - \rho)} = \tilde {\rho}, \text {   if   } \rho > \tilde {\rho} > 0; \\ 3. \alpha = 1, \text {   if   } \rho \leq \tilde {\rho}. \end{array}
$$

and

$$
\tilde {\rho} = \frac {K _ {L} (n - K _ {L}) + \delta_ {0} (K _ {H} - K _ {L} (n - K _ {H})) - E [ R 2 ^ {*} ]}{\delta K _ {L} (K _ {H} - K _ {L})},
$$

and

$$
E [ R 2 ^ {*} ] = \left\{ \begin{array}{l l} K _ {H} (n - K _ {H}), & \text {if} \quad K _ {H} \leq \frac {n}{2} + \frac {\delta - \delta_ {0}}{1 - \delta} (n - K _ {H}), \\ \frac {(1 - \delta) n ^ {2}}{4} + \frac {(\delta - \delta_ {0}) n (n - K _ {H})}{2} + \delta_ {0} K _ {H} (n - K _ {H}), & \text {if} \quad K _ {H} > \frac {n}{2} + \frac {\delta - \delta_ {0}}{1 - \delta} (n - K _ {H}). \end{array} \right.
$$

Proposition 2 shows that it is bene<sup>fi</sup>cial for a large-inventory auctioneer to initially hide this information by pretending to be an auctioneer with a limited inventory. Creating this uncertainty drives up competition among the bidders, and makes them bid more aggressively at the current auction. In the Sam's Club example, when customers are uncertain as to whether there will be future auctions of a 32-inch Sharp Aquos 1080p HDTV, their bids will be higher than when they are certain that this is not a one-time offer. This information or the lack thereof does not affect bidders' valuations; it does, however, affect their strategies. In this sense, it has an effect similar to an overall rise in bidder valuations.

Fig. 4 provides a numerical example that demonstrates how α, the probability that an H type auctioneer pretends to be an L type, changes with bidder competition intensity (that is, changing n with a <sup>fi</sup>xed K) and bidders' beliefs, where $K _ { h } = 5 , K _ { l } = 2 , \delta = 0 . 7$ , and $\delta _ { 0 } = 0 . 3$ . When varying n from 5 to 11, $\rho { = } 0 . 8 5$ ; while when varying ρ from 0 to 1, $n { = } 7 .$ [α changes with n] [α changes with $\rho ]$

Corollary 1. The probability (α) that the H type auctioneer pretends to be an L type is decreasing in both n and $\rho .$

Proposition 2 and Corollary 1 imply that when there is uncertainty about the amount of inventory, the H type auctioneer's choice between a simultaneous sale and a sequential sale, is largely affected by her decision as whether to reveal the inventory information, which in turn is determined by the intensity of bidder competition and how strongly bidders believe that the auctioneer is an H type:

![](/api/attachments/ERDR7JKF/fulltext/images/b22ad6976c3707640790bb644b7aced1ee85d60d48305e1d9107754a537babc4.jpg)  
(a) α changes with n

![](/api/attachments/ERDR7JKF/fulltext/images/dd1961a3774bc54aeaa5fe3d1e7502568b8d324d3f19af2ee7ad0c60486de8d1.jpg)  
(b)α changes with ρ  
Fig. 4. The change of α with respect to n, or ρ.

1. When the bidder competition is weak,<sup>5</sup> it is bene<sup>fi</sup>cial for the auctioneer to hide the information that there is more inventory available. Thus the auctioneer pretends to be an L type by using a sequential auction and sells the same number of items in the <sup>fi</sup>rst auction as does the L type (K );

2. When the bidder competition is in the middle range, the auctioneer reveals her type by selling In $\begin{array} { r } { \left( \frac { n } { 2 } \ + \frac { \delta - \delta _ { 0 } } { 1 - \delta } ( n - K ) \right) } \end{array}$ items in the <sup>fi</sup>rst auction, and uses a sequential auction;

3. When the bidder competition is strong, the auctioneer reveals her type by offering the entire inventory $\left( K _ { H } \right)$ in a single auction.

## 5. Optimal revealing time with strategic bidders

We now consider a T-period model in which the seller's inventory, determined by her production capacity, is her private information that is unavailable to the prospective buyers. Again, bidders are strategic who are able to calculate the auctioneer's optimal strategy. This problem appears to be similar to the one discussed in [22] as the “Picasso $\mathsf { p r o b l e m } ^ { * } . ^ { 6 }$ In that framework, Picasso as a monopolist producing paintings, maximizes his life-time revenue by deciding how many paintings to sell each year. Although bidders' valuations for Picasso's paintings are independent and will not change with the supply, the market prices for the paintings will be low even in his earlier years, if collectors anticipate that many paintings will be put on the market in the future market. Thus, a productive Picasso has an incentive to pretend to be a low-productivity type in his early years.

The idea that a seller can compete with himself in future periods is similar to that studied in a durable goods monopoly (e.g. [19,3,2,13,24]). Instead of studying dynamic pricing or leasing with effectively in<sup>fi</sup>nite capacity, we assume capacity is constrained and unknown to prospective bidders. Also there are a <sup>fi</sup>nite number of nN1 buyers and prices are set by auctions in each period, rather than posted by the seller. Our results may be different from one with a resale market where the incentive of low-valuation bidders for speculative buying may arise ([7]).

We simplify the problem by assuming that the auctioneer is a monopolist with a commonly-known time horizon of $T { > } 2$ periods. The producer can be an H type with a capacity to produce two items each period; or an L type with a capacity of one. We assume that no inventory or no free disposal is allowed, so the auctioneer has to sell whatever is produced.<sup>7</sup> With probability ρ the auctioneer is an H type who in each period needs to decide whether or not to pretend to be an L type by offering one item, or to reveal her type by offering two items. Once the auctioneer reveals her type, the bidders know the total number of items available in the T periods. There are n potential bidders present at the beginning of the auction. We only consider the case where $n { > } T .$ Otherwise, the auctioneer will surely pretend to be an L type till the last period. In each period there is a uniform-price auction selling that period's inventory. For simplicity, we assume that both the auctioneer and the bidders are patient; that is, ${ \delta \mathrm { = } } { \delta _ { 0 } } \mathrm { = } 1 . \mathrm { W e }$ are interested in the auctioneer's decision as to when to provide information regarding its capacity.

## 5.1. A traditional formulation

This problem can be formulated as a typical optimal stopping problem in dynamic programming, where the time that the auctioneer reveals her type is the time that the game “stops,” as the total number of items is then known. Traditional formulation assumes that the bidders are able to calculate their optimal bidding strategies based on their expectation about the total number of items available for sale, but not intelligent enough to predict the auctioneer's optimal strategy with respect to when $\mathrm { t } 0 \ ^ { \mathrm { * } } \mathrm { s t o p . } ^ { \mathrm { * } }$ In each period t, the H type auctioneer (if her type has not been revealed up to this point,) decides whether to (1) sell two items, so her type is revealed and bidders realize that there will be a total of $2 ( T - t + 1 ) + ( t - 1 )$ items; or $( 2 )$ sell only one item so that bidders still believe that she is an L type with probability $1 - \rho ,$ with an expected life-time capacity of $t + ( 2 \rho + 1 - \rho ) ( T - t )$ items. Speci<sup>fi</sup>cally, let $\beta ^ { t } ( \nu )$ represent the tth-period bidding function for a bidder with valuation of $\nu .$ From the analysis in Sections 3 and $^ { 4 , }$ we can determine that $\beta ^ { t } ( \nu ) =$ $E [ Y _ { k ( t ) } | \nu = Y _ { t } ]$ , where k(t) denotes the bidder's tth-period expectation about the total number of items available in the inventory.

Let S(t) represent the auctioneer's “stopping” payoff at period $t ,$ that is, the auctioneer's payoff if her type is revealed at period t. We have $S ( t ) = 2 ( T - t + 1 ) E [ X _ { 2 T - t + 2 } ] ,$ , because bidders know that there are altogether $2 T - t + 2$ items available, and there are $T - t + 1$ remaining periods. Let $g ( t )$ represent the auctioneer's current-period payoff if she decides to continue to hide her type. Then $g ( t ) = E [ X _ { ( 1 + \rho ) T - \rho t + 1 } ] .$ Thus the optimal stopping time, t\*, satis<sup>fi</sup>es $S ( t ^ { * } ) { \geq } g ( t ^ { * } ) + \bar { S } ( t ^ { * } + 1 )$ Again assuming that the valuations of bidders follow a uniform distribution on [0, 1], we have

Lemma 4 (Optimal Stopping Time under Traditional Formulation). In equilibrium, the H type auctioneer reveals her type at time $t ^ { * } ,$ where $t ^ { \ast } = { \min } \Big \{ { m a x } \Big \{ 0 , \lceil \frac { ( 5 \dot { - } \hat { \rho } ) T - n + 2 } { 4 - \rho } \rceil \Big \} , T \Big \}$

As in each period the bidders update their beliefs about the total number of items available, the winning prices are updated each period, too, until period $t ^ { * }$ when the type of the H auctioneer is revealed:

Lemma 5 (Equilibrium Price Path under Traditional Formulation). The expected winning prices are increasing when ${ \boldsymbol { t } } { < } { \boldsymbol { t } } ^ { * } ,$ , and remain constant when $t { \geq } t ^ { * } .$

Lemma 5 is intuitive: the winning prices increase when $t { < } t ^ { * }$ because the bidders realize that fewer items will be available each time they see only one item for sale; after t\* when the auctioneer's type is revealed, the total number of items becomes predictable and remains a constant, so the winning prices become a constant.

## 5.2. A formulation with strategic bidders

In this section we study the impact of strategic, forward-looking bidders, who are able to calculate the optimal stopping time $( t ^ { * } )$ and anticipate that an H type auctioneer will not reveal her type before t\*. So instead of being updated each period, their beliefs about the total number of items remain constant until period $t ^ { * } .$ . Consequently, the optimal stopping time $t ^ { * }$ obtained from Lemma 4 is no longer optimal, and the selling strategy of the auctioneer needs to be modi<sup>fi</sup>ed, too. We focus on a mixed strategy through which the H type auctioneer pretends to be an L type in period t with probability $\alpha _ { t } ,$ and reveals her type with probability $1 - \alpha _ { t }$ . Formally, let $( t ^ { * } , t _ { 2 } ^ { * } )$ denote the time interval within which $0 < \alpha _ { t } < 1$ 1(where $t ^ { * } < t _ { 2 } ^ { * } )$ . The beliefs of the bidders are assumed to be formulated as follows. When they observe two items for sale, they believe that the auctioneer is an H type with probability of one; when observing one item for sale, they believe that the auctioneer is an H type with probability of ρ if t b t\*, or with probability $0 \mathrm { f } \frac { \alpha _ { t } \rho } { \alpha _ { t } \mathrm { 0 } + 1 - \mathrm { 0 } } \mathrm { i f } t ^ { \ast } \leq t \dot { \leq } t _ { 2 } ^ { \ast } ,$ or with probability of 0 if $t { > } t _ { 2 } ^ { * } .$ Following Lemma 1, the bidders' equilibrium strategy in period t, if the type of the auctioneer has not yet been identi<sup>fi</sup>ed, can be summarized as follows:

1. When observing two items for sale for the <sup>fi</sup>rst time, the bidders realize that the auctioneer is of type H, thus $\beta ^ { t } ( \nu ) =$ $\begin{array} { r } { E \big [ Y _ { t - 1 + 2 ( T - t + 1 ) } \big | Y _ { t - 1 + 2 ( T - t + 1 ) } \leq \nu \big ] } \end{array}$ from period t on;

2. When observing one item on offer:

(a) If $t < t ^ { * } , \beta ^ { t } ( \nu ) = E [ Y _ { \tilde { t } ( t ) } | Y _ { \tilde { t } ( t ) } { \le } \nu ] ,$ , which is a constant with respect

to t, where $\begin{array} { r } { \tilde { t } ( t ) = 2 \mathsf { p } \big ( T { - } t _ { 2 } ^ { * } + 1 \big ) + ( 1 { - } \mathsf { p } ) T + \sum _ { t ^ { * } } ^ { t _ { 2 } ^ { * } } ( \alpha _ { t } \mathsf { p } + 1 ) ; } \end{array}$

( b ) I f $t ^ { * } \leq t \leq t _ { 2 } ^ { * } , \mathrm { \beta } ^ { t } ( \nu ) = E [ Y _ { \hat { t } ( t ) } | Y _ { \hat { t } ( t ) } { \leq } \nu ] ,$ <sup>Þ </sup>, w h e r e $\hat { t } ( t ) = 2 \mathrm { p }$

$$
(T - t _ {2} + 1) + (1 - \rho) T + (t - t ^ {*} + 1) + \sum_ {t} ^ {t _ {2} ^ {*}} (\alpha_ {t} \rho + 1);
$$

(c) If $t > t _ { 2 } ^ { * } ,$ <sup>Þ ð Þ ð Þ ð Þ</sup> realize that the auctioneer is type L with probability one, thus $\beta ^ { t } ( \nu ) = E [ Y _ { T } | Y _ { T } \leq \nu ] .$

3. In the last period, bidders bid their true values.

Based on the bidders' equilibrium bidding strategy, the auctioneer's optimal strategy is speci<sup>fi</sup>ed in Proposition 3:

Proposition 3 (Optimal Stopping Times Facing Intelligent Bidders). In equilibrium, there exists a time interval [t\*, t\*] such that the H type auctioneer will

• produce and sell one item when $t < t ^ { * } ;$

• produce and sell two items when $t > t _ { 2 } ^ { * } ;$

• produce and sell one item with probability $\alpha _ { t }$ and produce and sell two items with probability $1 - \alpha _ { t } ,$ when $t ^ { * } { \le } t { \le } t _ { 2 } ^ { * } ,$

where $\begin{array} { r } { t ^ { * } = m i n \Big \{ m a x \Big \{ [ \frac { ( 5 - \rho ) T - n + 2 } { 4 - \rho } ] , 0 \Big \} , T \Big \} , t _ { 2 } ^ { * } = m i n \Big \{ [ \frac { 5 T - n + 2 } { 4 } ] , T \Big \} } \end{array}$ and $\alpha _ { t } = { \frac { 1 - \rho } { \rho } } { \frac { { \dot { 5 } } T - n - \dot { 4 } t + 2 } { - 4 T + n + 3 t - 2 } } .$

It can be easily veri<sup>fi</sup>ed that $\alpha _ { t } = 1$ when $\begin{array} { r } { t = t ^ { \ast } - 1 = \lfloor \frac { ( 5 - \rho ) T - n + 2 } { ( 4 - \rho ) } \rfloor . } \end{array}$ Thus $t ^ { * }$ ð Þis the <sup>fi</sup>rst period in which the H auctioneer begins to use a nondegenerate mixed strategy; and α =0 at $\begin{array} { r } { t _ { 2 } ^ { * } + 1 = \lceil \frac { \bar { 5 } T - n + 2 } { 4 } \rceil . } \end{array}$ . Proposition 3 shows that, compared to the case of non-strategic bidders, the auctioneer's action before $t ^ { * }$ will not change the belief of bidders about the auctioneer's type. Moreover, because the bidders only update their beliefs after period $t ^ { * } ,$ , the identity of the auctioneer can be hidden with positive probability even after $t ^ { * }$ , until period t\* when there is absolutely no bene<sup>fi</sup>t to pretend. It also implies that the optimal timing for the H auctioneer to reveal her type is determined by the intensity of bidder competition, as well as their beliefs about the auctioneer's type. Fig. 5 provides a numerical example, where T=15, n=45 and $\rho { = } 0 . 9 .$ It shows that the probability that the H auctioneer pretends to be an L type (α ) is decreasing in time.

More speci<sup>fi</sup>cally,

Corollary 2. The more intense is the competition, the earlier the H auctioneer reveals her type. That is, both $t ^ { * }$ and $t _ { 2 } ^ { * }$ are decreasing in n.

The proof is straightforward and is thus omitted. Corollary 2 is intuitive: the more the bidders who demand the item, the less is the need for an H auctioneer to pretend to be an L type. As bidders' beliefs get updated only when $t ^ { * } \leq t \leq t _ { 2 } ^ { * }$ , the winning prices change accordingly:

![](/api/attachments/ERDR7JKF/fulltext/images/f866ad8c119cb8b322682b05d84f5ca69e188587da33d886d7d7386c4289490f.jpg)  
Fig. 5. How α changes in time.

Corollary 3 (Equilibrium Winning Price Path). The expected winning prices are constant when tbt\* or when $t > t _ { 2 } ^ { * } ,$ and weakly increasing when $t _ { 1 } ^ { * } { \leq } t { \leq } t _ { 2 } ^ { * } .$

Both Lemma 5 and Corollary 3 show that the winning prices in a sequential auction could increase over time during a given time interval, as long as there exists bidder uncertainty as to the total number of items for sale [10]. Even though the conditional probability that the H type auctioneer reveals her identity increases between [t\*, t\*] (conditional on she not having done so in the previous period), the prices are increasing during this period of time, because the fact that the auctioneer sells only one item in each period reduces the total number of items available over the relevant time horizon.

As the beliefs of the bidders about the total number of items available remain constant prior to period $t ^ { * } ,$ the winning prices remain constant before $t ^ { * } ,$ , too, which potentially leads to a lower expected revenue for the auctioneer when facing strategic bidders than when facing non-strategic ones:

Corollary 4. The H type auctioneer generates less expected revenue when facing strategic buyers than when facing non-strategic ones.

## 6. Conclusions and extensions

This paper considers the selling of K identical items by an auctioneer that is determined to sell them all. We study the auctioneer's choice between selling the items using a single auction or sequential auctions. More importantly, we examine whether the auctioneer should hide her inventory information, and if so, when is the optimal time to reveal it. Bidders in our model are forward-looking, who can predict the auctioneer's optimal strategy. We have shown that even when all bidders are present at the beginning of the auction, and when both the bidders and the auctioneer are impatient, a sequential sale can be more pro<sup>fi</sup>table as it heats up competition among those forward-looking bidders. We further investigate the conditions under which the auctioneer should hide her inventory information.

We have identi<sup>fi</sup>ed three factors that help increase the auctioneer's expected revenue from a sequential auction: (1) the intensity of bidder competition, as characterized by the total number of items for sale relative to the number of bidders; (2) the impatience levels of the auctioneer and the bidders; and (3) the auctioneer's information policy with regard to making known the size of its inventory. More speci<sup>fi</sup>cally, a sequential sale can help promote competition among the impatient bidders when bidder competition is weak, and when the bidders are relatively more impatient than the auctioneer. When the bidders are uncertain about the size of the inventory, it may be bene<sup>fi</sup>cial for a high-inventory auctioneer to hide this information and initially behaves if she were a low-inventory type. Such results hold in a T-period model in which these factors affect the H auctioneer's optimal timing to reveal her identity. As a result, the winning prices weakly increase over time. The timing of revelation depends again on the intensity of competition, where the presence of more bidders leads to earlier revelation.

Much future work, of course, remains to be done. One might, for instance, introduce a more realistic setting in which the bidders arrive at the auction site sequentially, so that the forward-looking bidders coexist with the “myopic” bidders. This would be especially relevant, if the number of new bidders is uncertain and both the auctioneer and the bidders are not sure about the future number of bidders when they make decisions in the earlier auction. Allowing competition among multiple auctioneers is another extension that would be interesting to consider. Speci<sup>fi</sup>cally, an auctioneer on eBay may face competition from other auctioneers selling identical items but with different ending times. It will be interesting to study the strategies of both the auctioneer and bidders in such a competitive setting. Finally, it is worthwhile to study a sequential auction with reserve prices in both periods. We believe that this paper provides a solid foundation to support these more complex structures.

## Acknowledgements

We thank Hemant Bhargava, Tony Kwasnica, Motty Perry, Tomas Sjostrom and Ira Horowitz for useful comments. Juan Feng's research is supported by the eBRC Doctoral Support Award.

## Appendix

## A.1. Benchmark case when the number of items is commonly known

Proof of Lemma 1. Let π (v) represent the expected pro<sup>fi</sup>t for a bidder with valuation v, and $P ( \cdot )$ denote the probability of the argument, and $\beta ^ { 1 } ( \cdot )$ represent the monotonic symmetric <sup>fi</sup>rst-period bidding function. Given that all the other bidders bid following the same bidding function for the <sup>fi</sup>rst auction, and all the bidders bid their true values in the second auction, for a bidder with valuation v to deviate to bid as a bidder of valuation r, his expected payoff can be represented as:

$$
\pi (r; v) = \pi^ {1} (v | r > Y _ {k _ {1}}) P (r > Y _ {k _ {1}}) + \pi^ {2} (v | r \leq Y _ {k _ {1}}, v \geq Y _ {K}) P (r \leq Y _ {k _ {1}}, v \geq Y _ {K}).
$$

First suppose $r \geq v$ (the case when $r { < } v$ can be derived similarly) Then π(v) can be written as:

$$
\begin{array}{l} \pi (r; v) = \int_ {0} ^ {r} (v - \beta^ {1} (y)) \frac {(n - 1) !}{(n - 1 - k _ {1}) ! (k _ {1} - 1)} F (y) ^ {n - 1 - k _ {1}} (1 - F (y)) ^ {k _ {1} - 1} f (y) d y \\ \qquad + \delta \bigg ((1 - F (r)) ^ {k _ {1}} \int_ {0} ^ {v} (v - y) \frac {(n - 1) !}{(n - 1 - K) (K - 1)} F (y) ^ {n - 1 - K} (1 - F (y)) ^ {k _ {1} - 1} \bigg) f (y) d y. \end{array}\tag{5}
$$

Taking the <sup>fi</sup>rst derivative of Eq. (5) with respect to r, we have:

$$
\begin{array}{l} \pi_ {r} (r; v) = (v - \beta^ {1} (r)) \frac {(n - 1) !}{(n - 1 - k _ {1}) ! (k _ {1} - 1)} F (r) ^ {n - 1 - k _ {1}} (1 - F (r)) ^ {k _ {1} - 1} f (r) \\ \qquad - \delta k _ {1} (1 - F (r)) ^ {k _ {1} - 1} f (r) \cdot \int_ {0} ^ {v} (v - y) \frac {(n - 1) !}{(n - 1 - K) ! (K - 1)} F (y) ^ {n - 1 - K} (1 - F (y)) ^ {k _ {1} - 1} f (y) d y. \end{array}\tag{6}
$$

Since in equilibrium the bidder with a valuation v has no incentive to deviate to bid as one with valuation of r, we set $\pi _ { r } ( r ; \nu ) = 0$ and $r = v ,$ and multiply both sides by $1 - F ( \nu )$

Then we have

$$
\begin{array}{l} (v - \beta^ {1} (v)) \frac {(n - 1) !}{(n - 1 - k _ {1}) ! k _ {1} !} F (v) ^ {n - 1 - k _ {1}} (1 - F (v)) ^ {k _ {1}} \\ = \delta \int_ {0} ^ {v} (v - y) \frac {(n - 1) !}{(n - 1 - K) ! (K - 1) !} F (y) ^ {n - 1 - K} (1 - F (y)) ^ {k _ {1} - 1} (1 - F (v)) ^ {k _ {1}} f (y) d y. \end{array}
$$

Thus, the equilibrium bidding function is:

$$
\begin{array}{l} \beta^ {1} (v) = v - \frac {\delta \int_ {0} ^ {v} (v - y) \frac {(n - 1) !}{(n - 1 - K) ! (K - 1) !} F (y) ^ {n - 1 - K} (1 - F (y)) ^ {k _ {1} - 1} (1 - F (v)) ^ {k _ {1}} f (y) d y}{\frac {(n - 1) !}{(n - 1 - k _ {1}) ! k _ {1} !} F (v) ^ {n - 1 - k _ {1}} (1 - F (v)) ^ {k _ {1}}} \\ = v - \delta \pi^ {2} (v | v = Y _ {k _ {1}}) \\ = (1 - \delta) v + \delta E [ Y _ {K} | v = Y _ {k _ {1}} ] \end{array} \tag {7}
$$

To con<sup>fi</sup>rm that the bidding strategy given by Eq. (7) is actually optimal, we need only show that π(v; v)≥π(r; v), ∀v, ∀x. According to the Lemma A1 in McAfee-Vincent-93 (which is shown in a more general setting), this requires the following three conditions: (1) π is a continuous, twice differentiable function; $( 2 ) , \pi _ { r } ( \nu ; \nu ) = 0$ (which is shown from our derivation); and $( 3 ) \pi _ { r \nu } ( r ; \nu ) { \geq } 0$ (which follows after differentiating the last line of Eq. (6) with respect to r).

It can be easily veri<sup>fi</sup>ed that the equilibrium bidding function $\beta ^ { 1 } ( \nu )$ is monotonically increasing. □

Proof of Lemma 3. By Lemma 2, the auctioneer's expected revenue using a sequential auction, E [R2], is determined by: $E \left[ R 2 \right] = ( 1 - \delta ) k _ { 1 } E$ $[ \mathrm { X } _ { k _ { 1 } + 1 } ] + \delta k _ { 1 } E [ \mathrm { X } _ { K + 1 } ] + \delta _ { 0 } ( K - k _ { 1 } ) E [ \mathrm { X } _ { K + 1 } ]$ . Assuming that bidders valuations following a uniform distribution over [0; 1], we can express the order statistics $\begin{array} { r } { \bar { X } _ { k } = \frac { n - k + 1 } { n + 1 } } \end{array}$ . Substituting these order statistics into the expression for $E [ R 2 ] ,$ we obtain:

$$
E [ R 2 ] = k _ {1} (1 - \delta) \frac {n - k _ {1}}{n + 1} + k _ {1} \delta \frac {n - K}{n + 1} + \delta_ {0} (K - k _ {1}) \frac {n - K}{n + 1}.
$$

By examining the <sup>fi</sup>rst order condition and con<sup>fi</sup>rm that this is a concave function, it is straightforward to show that the optimal $k _ { 1 } ^ { * }$ is given by $\begin{array} { r } { k _ { 1 } ^ { * } = \frac { n } { 2 } + \frac { \delta - \delta _ { 0 } } { 1 - \delta } ( n - K ) . } \end{array}$ A valid $k _ { 1 } ^ { * }$ should be less than the <sup>ð Þ</sup>number of total items available K and be an integer. De<sup>fi</sup>ne $I n t ( x )$ as the closest integer to x, that is, I $n t ( x ) = a r g m i n \left\{ x - \left\lfloor x \right\rfloor , \left\lceil x \right\rceil - x \right\}$ . Thus, $\begin{array} { r } { k _ { 1 } ^ { * } = \operatorname* { m i n } \left\{ K , \bar { I n t } \Big ( \frac { n } { 2 } + \frac { \delta - \delta _ { 0 } } { 1 - \delta } ( n - K ) \Big ) \right\} } \end{array}$ □

Proof of Proposition 1. Substituting $k _ { 1 } ^ { * }$ into Eq. (3) allow us to calculate the difference in the expected revenues that the auctioneer can obtain from a sequential auction and a simultaneous one:

$$
\begin{array}{r} E (R 2) - E [ R 1 ] = (1 - \delta) k _ {1} ^ {*} E [ X _ {k _ {1} ^ {*}} ] + [ \delta - \delta_ {0} k _ {1} ^ {*} - (1 - \delta) K ] E [ X _ {K} ] + _ {1} ] \\ = \frac {1 - \delta - 2 \delta_ {0}}{4} n ^ {2} - \frac {2}{2} n K + (1 - \delta_ {0}) K ^ {2}. \end{array}
$$

The two roots for $E [ R 2 ] - [ R 1 ] = 0$ are: $n { = } 2 K$ and $\begin{array} { r } { n = \frac { 2 - 2 \delta _ { 0 } } { 1 \mathrm { ~ + ~ } \delta - 2 \delta _ { 0 } } K . } \end{array}$

$[ { \mit \mathrm { f } } 1 - \delta - 2 \delta _ { 0 } > 0 , E [ R 2 ] - E [ R 1 ] > 0$ is obtained when nb min $\left\{ 2 K \frac { 2 - 2 \delta _ { 0 } } { 1 \mathrm { ~ + ~ } \delta - 2 \delta _ { 0 } } K \right\}$ , or n N max $\left\{ 2 K , \frac { 2 - 2 \delta _ { 0 } } { 1 \ + \ \delta - 2 \delta _ { 0 } } K \right\}$ . Since $\frac { 2 - 2 \delta _ { 0 } } { 1 + \delta - 2 \delta _ { 0 } }$ $K > 2 K$ implies $\delta _ { 0 } { > } \delta ,$ the solution $\begin{array} { r } { n > \frac { 2 - 2 \delta _ { 0 } } { 1 \mathrm { ~ + ~ } \delta - 2 \delta _ { 0 } } \dot { K } } \end{array}$ indicates that $\begin{array} { r } { k _ { 1 } ^ { * } = \frac { n } { 2 } + \frac { \delta - \delta _ { 0 } } { 1 - \delta } ( n - K ) < K < \frac { 1 + \delta - 2 \delta _ { 0 } } { 2 - 2 \delta _ { 0 } } r } \end{array}$ n. It can be shown, however, that $\begin{array} { r } { \frac { n } { 2 } + \frac { \delta - \delta _ { 0 } } { 1 - \delta } ( n - K ) > \frac { 1 { + } \delta - 2 \delta _ { 0 } } { 2 - 2 \delta _ { 0 } } n . } \end{array}$ . This contradiction implies the solution of $\begin{array} { r } { n > \frac { 2 - 2 \delta _ { 0 } } { 1 - \delta - 2 \delta _ { 0 } } K } \end{array}$ is invalid. For a similar reason, $n { > } 2 K$ is also invalid. So E $[ R 2 ] - \mathbb { E } [ R 1 ] > 0$ is obtained when nb min $\left\{ 2 K , \frac { 2 - 2 \delta _ { 0 } } { 1 - \delta - 2 \delta _ { 0 } } K \right\}$

$1 \mathrm { f } 1 - \delta \dot { - } 2 \delta _ { 0 } { < } 0 ,$ <sup>− 0</sup> , since $2 - 2 \delta _ { 0 } \ge 0 , \mathtt { E } [ R 2 ] - \mathtt { E } [ R 1 ] > 0$ is obtained when $n { < } 2 ~ K .$ □

## A.2. Bidders uncertain about the number of auctions

Proof of Proposition 2. Assuming bidders' value follows a uniform distribution over [0, 1], as $K _ { L } < k _ { 1 } ^ { * }$ the L auctioneer's best strategy is to sell $K _ { L }$ items in the <sup>fi</sup>rst auction. The H auctioneer can choose to pretend to be an L type by selling $K _ { L }$ items, or to reveal her type by selling $k _ { 1 } ^ { * }$ items in the <sup>fi</sup>rst auction. If the auctioneer attempts to mislead the bidders, the expected revenue will be:

$$
K _ {L} \{(1 - \delta \rho^ {\prime}) E [ x _ {K _ {L} + 1} ] + \delta \rho^ {\prime} E [ X _ {K _ {H} + 1} ] \} + (K _ {H} - K _ {L}) \delta_ {0} E [ X _ {K _ {H} + 1} ].\tag{8}
$$

If the auctioneer reveals the true status of the inventory at the <sup>fi</sup>rst auction, the expected revenue is:

$$
E [ R 2 ^ {*} ] = \left\{ \begin{array}{l l} K _ {H} (n - K _ {H}) & \text {if} \quad K _ {H} \leq \frac {n}{2} + \frac {\delta - \delta_ {0}}{1 - \delta} (n - K) \\ \frac {(1 - \delta) n ^ {2}}{4} + \frac {(\delta - \delta_ {0}) n (n - K _ {H})}{2} + \delta_ {0} K _ {H} (n - K _ {H}) \text {if} & K _ {H} > \frac {n}{2} + \frac {\delta - \delta_ {0}}{1 - \delta} (n - K). \end{array} \right.\tag{9}
$$

For the H auctioneer to be indifferent between these two options, $\rho ^ { \prime }$ should satisfy Eq. $\left( 8 \right) = \operatorname { E q . } \left( 9 \right)$ , which gives the threshold value

$$
\tilde {\rho} = \frac {K _ {L} (n - K _ {L}) + \delta_ {0} (K _ {H} - K _ {L} (n - K _ {H})) - E [ R 2 ^ {*} ]}{\delta K _ {L} [ K _ {H} - K _ {L} ]}.
$$

Thus, since $\delta K _ { L } ( K _ { H } - K _ { L } ) > 0$ and $\rho { < } \rho ^ { \prime }$

1. $\mathrm { I f } ~ \tilde { \rho } { \le } 0$ , the High type auctioneer will always reveal her type by selling $K _ { H }$ items in a single auction, thus $\alpha { = } 0 ;$

2. if $\rho { \le } \tilde { \rho } { > } 0$ , the high type auctioneer will pretend to be an L type with probability of 1 $( \alpha = 1 ) ;$

3. if $\rho { > } \tilde { \rho } ,$ there exists an α satisfying $\frac { \alpha \rho } { \alpha \rho + ( 1 - \rho ) } = \tilde { \rho } ,$ , which makes Eq. $( 8 ) = \operatorname { E q } . \ ( 9 )$ <sup>ð Þ</sup>. Thus the H auctioneer will follows a mixed strategy wherein it pretends to an L type auctioneer with probability α, and reveal her type with probability $1 - \alpha$ □

## Proof of Corollary 1. Since

$$
\delta K _ {L} (K _ {H} - K _ {L}) \frac {\partial \tilde {\rho}}{\partial n} = (1 - \delta_ {0}) K _ {L} - K _ {H}) <   0.
$$

It is straightforward that ρ̃ is decreasing in n.

The result with regards to bidder's beliefs, $\rho ,$ is straightforward since $\frac { \alpha \rho } { \alpha \rho + ( 1 - \rho ) }$ is increasing in $\rho .$ □

## A.3. Optimal revealing time with strategic bidders

Proof of Lemma 4. Assume that bidders' valuations follow a uniform distribution on $[ 0 , \ 1 ] ,$ then $\begin{array} { r } { E [ X _ { 2 T - t + 2 } ] ~ = ~ \frac { n - 2 T + t - 1 } { n + 1 } } \end{array}$ and $\begin{array} { r } { E \big [ X _ { ( 1 - \rho ) T - \rho t + 1 } \big ] = \frac { n - ( 1 + \rho ) T + \rho t - 1 } { n + 1 } . } \end{array}$ . After substituting this into $S ( t ^ { * } )$ $= \bar { g ( t ^ { * } ) } + S ( t ^ { * } \bar { + } 1 )$ , and following some straightforward algebra, we can obtain the optimal stopping time. □

Proof of Lemma 5. The winning price is a constant after period $t ^ { * } ,$ because since then the total number of items are commonly known, in addition, there is no time discounting $\left( \delta = \delta _ { 0 } = 0 . \right)$ Before period $t ^ { * } ,$ in each of the earlier period, bidders update their beliefs about the total items available over the time horizon of T period, which is $( 1 + \rho ) T _ { - } \rho t + 1$ . Thus the expected $t ^ { t h }$ period bid is $E [ X _ { ( 1 + \rho ) T - \rho t + 1 } ] .$ Assuming that bidders' valuations following U[0, 1], we have $\begin{array} { r } { E \big [ X _ { ( 1 - \rho ) T - \rho t + 1 } \big ] = \frac { n - ( 1 + \rho ) T + \rho t - 1 } { n + 1 } } \end{array}$ , which is increasing in t. □

Proof of Proposition 3. Let $t _ { 2 } ^ { * }$ represent the <sup>fi</sup>rst period in which the H type auctioneer is worse off from pretending to be an L type one, so that she will reveal her identity at $t _ { 2 } ^ { * }$ Since the H auctioneer uses a mixed strategy before $t _ { 2 } ^ { * }$ by pretending to an L type with probability α at period t and revealing with complementary probability, when observing 1 item for sale at period $t < t _ { 2 } ^ { * } ,$ bidders always anticipate that with probability $\begin{array} { r } { \rho _ { t } ^ { \prime } + 1 = \frac { \alpha _ { t } \rho _ { t } } { \alpha _ { t } \rho _ { t } + 1 - \rho _ { t } } } \end{array}$ the current auctioneer is an H type. Given this belief, the seller is indifferent between auctioneer is indifferent between revealing her true type at period t, or revealing it at period $t + 1$ , which is also known to the bidders. The bidding function for a bidder with valuation of v should take into account this potential gain (E[Y | $Y _ { T } < \nu ] - \rho _ { t + 1 } ^ { \prime } ( \nu - E [ Y _ { 2 T - t } | Y _ { 2 T - t } < \nu ] )$ if the auctioneer is an H type. Thus the auctioneer's current period payoff i $: g ( t ) = ( 1 - \rho _ { t + 1 } ^ { \prime } ) E [ X _ { T + 1 } ] +$ $\rho _ { t + 1 } ^ { \prime } E \left[ X _ { 2 T - t + 1 } \right]$ . Since the auctioneer is indifferent between hiding and revealing between period $t ^ { * }$ and $t _ { 2 } ^ { * } , S ( t ) = S ( t + 1 ) + g ( t )$ , that $\begin{array} { r } { \mathrm { i } s ; \frac { 2 ( T - t _ { 2 } + 1 ) ( n - 2 T + t _ { 2 } - 1 ) } { n + 1 } = \frac { 2 ( T - t _ { 2 } ) ( n - 2 T + t _ { 2 } ) + ( 1 - \rho ^ { \prime } ) ( n - T ) + \rho ^ { \prime } ( n - 2 T + t ) } { n + 1 } . } \end{array}$ From this we obtain $\begin{array} { r } { \alpha = \frac { 1 - \rho t } { \rho t } \frac { 5 T - n - 4 t + 2 } { - 4 T + n + 3 t - 2 } . } \end{array}$ As $\alpha _ { t } = 1$ when $\begin{array} { r } { t = \frac { ( 5 - \rho ) T - n + 2 } { ( 4 - \rho ) } } \end{array}$ , thus $\begin{array} { r } { t ^ { * } = \lceil \frac { ( 5 - \rho ) T - n + 2 } { ( 4 - \rho ) } \rceil } \end{array}$ is the <sup>fi</sup>rst period in which the high type auctioneer begins to use a non-degenerate mixed strategy; and $\begin{array} { r } { \alpha _ { t } { = } 0 \mathrm { a t } t _ { 2 } ^ { * } + 1 = \big \lceil \frac { 5 T - n + 2 } { 4 } \big \rceil , } \end{array}$ which con<sup>fi</sup>rms our results. □

Proof of Corollary 3. It is evident that the winning price when $t { < } t ^ { * }$ and $t \geq t _ { 2 } ^ { * }$ are constant, because bidders' belief beliefs as to the total number of items available is constant.

For $t ^ { * } < t < t _ { 2 } ^ { * } ,$ bidders update their beliefs each period, and expect there are $\begin{array} { r } { \langle ( t ) = 2 \mathsf { p } \big ( \Gamma - t _ { 2 } ^ { * } + 1 \big ) + ( 1 - \mathsf { p } ) T + ( t - t ^ { * } + 1 ) + \sum _ { t } ^ { \prime } ( \alpha _ { t } \rho + 1 ) } \end{array}$ items for sale. Compare k(t) and $k ( t + 1 )$ as $k ( t ) { > } k ( t { + } 1 )$ <sup>Þ</sup>, it is evident that the winning price at period $t , \ E [ X _ { k ( t ) } ]$ , is increasing in t. □

Proof of Corollary 4. The auctioneer's expected revenue when facing myopic bidders, $E [ R _ { m } ] ,$ , is the summations of expected winning prices in each period. According to Section 5.1, it can be expressed as:

$$
E [ R _ {m} ] = \sum_ {t} E \Big [ X _ {(1 + \rho) T - \rho t + 1} \Big ] + 2 (T - t ^ {*} + 1) S (t ^ {*}).\tag{10}
$$

When facing strategic bidde $\Gamma S ,$ as bidders' beliefs do not change before period $\bar { t ^ { * } } ,$ , the market clearing prices remain to be the same before $t ^ { * } ,$ , that is, $E \big [ X _ { ( 1 + \rho ) T - \rho ( t - 1 ) + 1 } \big ]$ for $t { < } t ^ { * }$ . After $t ^ { * } ,$ as the auctioneer feels indifferent between revealing her type at period t and t+1 until period $t _ { 2 } ^ { * } ,$ we only pick one realization, which is to reveal at period t\*. So, the auctioneer's expected revenue when facing strategic bidders $E [ R _ { s } ]$ , can be expressed as:

$$
E [ R _ {m} ] = (t ^ {*} - 1) E \left[ X _ {(1 + \rho) T - \rho t + 1} \right] + 2 (T - t ^ {*} + 1) S (t ^ {*}).\tag{11}
$$

It is then easily veri<sup>fi</sup>ed that $E [ R _ { m } ] { > } E [ R _ { s } ]$ by comparing Eqs. (10) and (11). □

## References

[1] Carrie Beam, Arie Segev, and George Shanthikumar. Electronic negotiation through internet-based auctions. CITM Working Paper 96-WP-1019. 1996

[2] David Besanko, Wayne L. Winston, Optimal price skimming by a monopolist facing rational consumers, Management Science 36 (5) (May 1990) 555–567.

[3] Jeremy Bulow, Durable-goods monopolists, Journal of Political Economy 90 (2) (April 1982) 314–332.

[4] Indranil Chakraborty, Bundling decisions for selling multiple objects, Economic Theory 13 (3) (1999) 723–733.

[5] Indranil Chakraborty, Bundle and separate sales in auctions with entry, Games and Economic Behavior 54 (1) (Jan 2006) 31–46.

[6] Juan-Jose Ganuza, Ignorance promotes competition: an auction model with endogenous private valuations, The Rand Journal of Economics 35 (3) (2004) 583–598 Autumn.

[7] Rod Garratt, Thomas Troger, Speculation in standard auctions with resale, Econometrica 74 (3) (May 2006) 753-769

[8] Nelson Granados, Alok Gupta, Robert J. Kauffman, Designing online selling mechanisms: Transparency levels and prices, Decision Support Systems 45 (4) (November 2008) 729–745.

[9] Donald B. Hausch, Multi-object auctions: Sequential vs simultaneous sales, Management Science 32 (12) (December 1986) 1599–1610.

[10] Thomas D. Jeitschko, Equilibrium price paths in sequential auctions with stochastic supply, Economics Letters 64 (1999) 67–72.

[11] Gilbert Karuga, Suresh Nair, and Arvind K.Tripathi. Sizing of lots in identical-item sequential online auctions. Working Paper, University of Connecticut, 2005.

[12] Vijay Krishna, Auction Theory, Elsevier Science, 2002.

[13] R. Preston McAfee, Daniel Vincent, Sequentially optimal auctions, Game and Economic Behavior 18 (Feb 1997) 246–276.

[14] Flavio M. Menezes, Sequential actions with delay costs, a two-period model, Economics Letters 42 (1993) 173–178.

[15] P.R. Milgrom, Robert J. Weber, A theory of auctions and competitive bidding, Econometrica 50 (1982) 1089–1122.

[16] Thomas R. Palfrey, Bundling decisions by a multiproduct monopolist with incomplete information, Econometrica 51 (2) (March 1983) 463–483.

[17] Edieal Pinker, Abraham Seidmann, and Yaniv Vakrat. Using transaction data for the design of sequential, multi-unit, online auctions. Working Paper CIS-00–3 Simon School, University of Rochester, 2000.

[18] Zuo-Jun Max Shen, Xuanming Su, Customer behavior modeling in revenue management and auctions: a review and new research opportunities, Production and Operations Management 16 (6) (December 2007) 713-728.

[19] Nancy L. Stokey, Intertemporal price discrimination, The Quarterly Journal of Economics 93 (3) (Aug 1979) 355-371.

[20] Gustavo Vulcano, Garrett van Ryzin, Costis Maglaras, Optimal dynamic auctions for revenue management, Management Science 48 (11) (November 2002) 1388–1407.

[21] Robert J. Weber, Multiple-object auctions, in: Frank Hahn (Ed.), Auctions, Bidding and Contracting: Uses and Theory, chapter 14, New York University Press, New York, 1983, pp. 165–191.

[22] Robert Wilson, Reputation in games and markets, in: Alvin E. Roth (Ed.), Game-Theoretic Models of Bargaining, Cambridge University Press, Cambridge, 1985.

[23] Robert Zeithammer, Forward-looking bidding in online auctions, Journal of Marketing Research 43 (3) (2006) 462–476.

[24] Dan Zhang, William L. Cooper, Managing clearance sales in the presence of strategic customers, Production and Operations Management 17 (4) (July-Augus 2008) 416–431.

Juan Feng is an assistant professor in the College of Business, City University of Hong Kong. Her general research topics of interest include: Performance based pricing, Economics of information gatekeepers, Game theory, E-business, etc. Dr. Feng has published in journals like: Informs Journal on Computing, Marketing Sciences, POM, etc

Kalyan Chatterjee is Distinguished Professor of Economics and Management Science in Penn State University. His research interests include Game Theory, Microeconomic Theory, and Industrial Organization. He has published in Econometrica, Rand Journal of Economics, Game and Economic Behavior, Management Science, Marketing Science, etc.
