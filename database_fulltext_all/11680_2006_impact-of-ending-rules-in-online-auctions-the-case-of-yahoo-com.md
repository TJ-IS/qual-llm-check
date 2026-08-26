---
otero_id: 11680
otero_key: "8TZQHNM6"
title: "Impact of ending rules in online auctions: The case of Yahoo.com"
authors: "Ilke Onur; Kerem Tomak"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.03.010"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Impact of ending rules in online auctions: The case of Yahoo.com

Ilke Onur <sup>a,1</sup>, Kerem Tomak <sup>b,⁎,2</sup>

<sup>a</sup> TOBB Economics and Technology University, Ankara, Turkey b University of Texas at Austin, Austin, 78712, TX, United States

Received 23 November 2004; received in revised form 28 February 2006; accepted 8 March 2006 Available online 27 June 2006

## Abstract

This paper examines the impact of sellers' choice of auction parameters on the level of their revenues using data from Yahoo.com's Playstation 2 system auctions. Our study specifically highlights the impact of the ending rule. We introduce a new variable called Winning Bid Ratio (WBR), and use it as a proxy for seller revenues. WBR is the ratio of the winning bid of an auction to the buy price offered by the seller. We find that choosing a high bid increment and including a shipping price decreases the WBR. Alternatively, lower number of bids and choosing a shorter auction length have a positive effect on the WBR. On the whole, the ending rule has a negative effect on the WBR, which is in accord with the theoretical predictions in the literature. However, we also find variations in the results for the effect of ending rule when we divide the data into two groups consisting of high and low-value auctions. © 2006 Published by Elsevier B.V.

Keywords: Online auctions; Electronic markets; Auction ending rules

## 1. Introduction

Online auctions not only provide an outlet but also a myriad of auction mechanism design choices for merchants. Internet has increased both the variety of goods and services sold via auction mechanisms and introduced new ways in which auctions can be conducted. While the bidders devise technology enabled “last-minute bidding” strategies for eBay auctions, sellers can choose between different auction mechanisms on Yahoo.com's site. In this paper, we provide empirical evidence, using data from Yahoo.com auction site, on the impact of the auction ending rule and several other options on sellers revenue. In order to achieve this, we introduce a new variable called Winning Bid Ratio (WBR), which we use as a proxy for seller revenues.<sup>3</sup> WBR is the ratio of the winning bid of an auction to the buy price offered by the seller.

Although merchants have been using auctions to sell their products for centuries, accessibility to this buying mechanism was limited to those who could bear the transaction costs involved in participating in them. The selection of products was also limited to unique items in the business-to-consumer (e.g., used cars) or consumerto-consumer (e.g., antiques) auctions and wholesale or bulk items (e.g., produce, fish and timber) in the businessto-business auctions. Online auction sites such as Yahoo. com and eBay.com provide a platform to expand this traditional sales channel to the Internet. eBay is currently the dominant player in the United States in the area of consumer-to-consumer online auctions although Yahoo. com is the leader in the business-to-consumer auctions in Japan. Auction sites use the Web's unique characteristics such as chat, email, dynamic content, to allow individuals and businesses all around the world to essentially sell anything.

MIS literature focuses primarily on bidder behavior in online auctions. One of the earlier papers studying online auctions is that of Beam and Segev [5] who classify auction businesses by the breadth of merchandise offered, whether the goods are information or physical, and whether they are new or old/used. Bapna et al. [1,2] study multiunit B2C auctions, characterizing bidders in these auctions as being one of three types, depending on how they time their bids and how often they bid. Evaluators are identified as early, one-time, high bidders who have a clear idea of their valuation. They bid early and submit a high value. Participators in contrast derive some utility from participating in the auction. They start with a low bid and increase it towards the end of the auction. Finally, opportunists look out for bargains and submit bids just before the auction ends. Bapna et al. [2] demonstrate that bidding increments play an important role in English auction outcomes. They conclude that setting a high bid increment raises bids, as the lowest winning bid must be higher than the valuation of the bidder with the next highest valuation by the amount of the bid increment. They also argue that it reduces participation and overall bidding activity, because it effectively raises the minimum required bid at every point. Snir and Hitt [18] develop a theoretical model of an auction for IT knowledge that involves a stated price and an unobserved quality attribute. They use data from RentACoder.com, an IT expert auction website, to investigate the behavior of markets for professional services. They find that in such markets, there may be excessive bidding for high-value projects, raising transaction costs for participants, and potentially lowering the quality of the services purchased. Unlike the papers cited above, our paper studies (i) Yahoo.com auctions which have significant structural differences than eBay.com auctions; (ii) revenue impact of an auction ending format chosen by a seller for various item valuations.

eBay auctions have received a substantial attention in the economics literature as well. Earlier empirical work in economics focused on bidder strategies in this novel trading platform on the Internet. Lucking-Reiley [10] uses eBay data on trading cards to test the revenue equivalence between auction formats. He finds that the Dutch<sup>4</sup> auction produces 30% higher revenues than the first-price auction format, and that the English and second-price formats produce roughly equivalent revenues. In a sequential work, he reports that individual's first-unit bids are significantly higher in the uniformprice than in the Vickrey treatment [11]. In addition, the bid differences are large enough to affect the allocation of goods, as split allocations result significantly more often in the uniform-price treatment and there is no significant difference in revenues across auction formats.

There are relatively less papers analyzing Yahoo.com auctions although the differences are substantial. On both eBay and Yahoo.com, sellers have the option to list their auctions with a posted price option. In such auctions the seller sets a buy price at which a bidder may purchase the item immediately and end the auction. In the eBay version of an auction with the buy-it-now (BIN) option, the BIN opportunity disappears as soon as a bid is placed, while in the Yahoo.com version of the auction, the buynow option remains in effect throughout the auction. Reynolds and Wooders [15] report on the frequency of buy prices in Yahoo.com and eBay auctions. The categories sampled on March 27, 2002, are automobiles, clothing, DVD players, VCRs, digital cameras and TV sets. They sample a total of 1248 auctioned items from Yahoo.com, of which 842 had a buy price posted by the seller (roughly, 66%). They also analyze 31,142 auctioned items from eBay, of which 12,480 have a buy price posted by the seller (roughly, 40%). They show that when bidders are risk neutral then both auction formats are revenue equivalent to the standard English ascending bid auction, so long as the buy-now price is not too low. They also find that while the Yahoo.com format raises more revenue than the eBay format (when the buy-now price is the same in both auctions), the auctions are payoff equivalent from the bidders' perspective. Our paper addresses the complementary problem of the impact of auction ending rule on the revenue of the sellers.

One of the main differences between Yahoo.com and eBay auctions is that eBay auctions have hard-close time. In hard-close auctions the ending time of the auction is set by the seller and the auction ends exactly at the pre-determined time. Yahoo.com auctions give the choice of the closing time to the sellers. Sellers can choose between hard-close, like in eBay, versus a softclose time which is like Amazon.com's auction rule that extends the ending time if there is bidding activity in the last 10 min of the auction. Submitting a bid in a matter of seconds before the close of an auction is called sniping. Sniping is a strategic tool available for the bidders primarily due to the hard-close rule as it does not allow bidders time to counter bid.

Impact of seller reputation in online auctions captured wide attention in both MIS and economics fields.<sup>5</sup> Empirical studies show that seller feedback has a significant yet small and positive effect on the winning bid. Our data set does not include information on seller reputation. However we do not believe this variable would have a significant effect on the main focus of our paper, the ending rules in Yahoo.com auctions.

Schindler [17], studies bidding in Yahoo.com auctions for computer, art and cars. In these auctions, the sellers can choose to have a hard- or soft-close. She finds that, the winning bidder tends to arrive later in the auctions with a hard ending for all three product categories while sellers should prefer soft ending auctions. She also shows that sellers in art and cars categories prefer soft ending auctions as predicted. However, sellers in the computer category strictly prefer hard ending auctions. Complementary to these results, in our analysis, we find that the significant impact of the auction format on seller revenues depends on the value of the item offered.

In summary, our main research questions in this paper are the following:

• Does the online auction ending rule (hard-close versus soft-close) make a difference in sellers' revenues?

• Do the sellers choose ending rules strategically based on the value of the products they sell?

• What are the additional effects from other auction parameters at Yahoo.com site on the seller revenues?

We find that, on the whole, the hard-close ending rule affects the seller revenues negatively. However, we also observe variations in the results for the effect of ending rule when we divide the data into two groups based on whether the products are high- or low-value. Additionally, we show that choosing a high bid increment and including a shipping price decreases, longer auction length and larger number of bids increase the revenue of the auction.

## 2. Theoretical model

In economic theory and practice, there are primarily four main auction formats which are widely used: English, Dutch, first-price sealed-bid and Vickrey auctions. English auction is an ascending bid auction. As the price increases bidders continue to drop out of the auction as soon as the price meets their reservation price. This continues until a single bidder is left. The Dutch auction is the descending version of the English auction. The auction starts at a very high price so that no bidder is interested in buying the object at that price and then the auctioneer lowers the amount until a bidder agrees to pay the current price. In the first-price sealed-bid auction, each bidder privately submits a single bid in an envelope. At the end of the submission process, the auctioneer opens each envelope and the person submitting the highest bid wins the object by paying what s/he bid. Finally, Vickrey auction, also called second-price sealed bid auction, is similar to the first-price sealed-bid auction in that the highest bidder wins the auction but ends up paying the amount submitted by the second-highest bidder.

Along with the rules, the structure of the bidder valuations is an important dimension of auctions. The uncertainty about the product values is an inherent characteristic of auctions. A private value environment occurs if each bidder knows the value of the object to him/herself and not the values attached by other bidders. Furthermore, knowing other bidders' valuations would not change the valuation assigned by him/her.

In general, for single item auctions, bidder $i , i { = } 1 , . . . , n$ assigns a value $\nu _ { i }$ to the object auctioned. Within the independent and identically distributed (i.i.d.) private values setup, each $\nu _ { i }$ is i.i.d. distributed on some interval [0, v] by a distribution function F which has a continuous density and full support. Each bidder i knows the realization of $\nu _ { i }$ and that other bidders' valuations are drawn from the distribution $F .$ They are risk neutral and expected utility maximizers with no budget constraints. F and the number of bidders are common knowledge.

Let $B _ { i } : [ 0 , \nu ] { \longrightarrow } \Re _ { + }$ be the bidding function for all bidders $i { \in } \{ 1 , 2 , . . . n \}$ . For second-price auctions, we know that $B _ { i } ( \nu _ { i } ) { = } \nu _ { i }$ is a weakly dominant strategy for each potential buyer, regardless of their beliefs about other potential buyers' valuations.<sup>6</sup>

<sup>Proposition.</sup> In a second-price sealed-bid auction, it is a weakly dominant strategy to bid according to $B _ { i } ( \nu _ { i } ) { = } \nu _ { i } .$

Following Roth and Ockenfels [16], we identify Yahoo.com Playstation 2 auctions as second-price auctions with independently and identically distributed private values. Accordingly, the bidders in our dataset should be submitting their own valuations at any time during the auction. An interesting question is when it is equilibrium for a bidder to wait until the last minute of the auction to submit her bid. Roth and Ockenfels [16] offer an explanation for this phenomenon. Their explanation depends on the existence of a probability $p \in ( 0 , 1 )$ which represents the probability that the bid will be recorded when it is submitted at the last minutes of the auction. Furthermore, this probability is the same for all bidders submitting their bids at the last-minute. Their explanation is the congestion at the closing minutes of the auction. As a result, they present the following equilibrium as one of many possible equilibria.

<sup>Theorem.</sup> There can exist equilibria in which bidders do not bid their true values until the last moment, at which time there is only probability p b 1 that the bid will be transmitted.

Their explanation is the following: “The intuition behind last-minute bidding at equilibrium in a private value auction will be that there is an incentive not to bid too high when there is still time for other bidders to react, to avoid a bidding war that will raise the expected final transaction price. And mutual delay until the last minute can raise the expected profit of all bidders, because of the positive probability that another bidder's last-minute bid will not be successfully transmitted. Thus at such an equilibrium, expected bidder profits will be higher (and seller revenue lower) than at the equilibrium at which everyone bids true values early.”

The revenue in the automatically extended auction is equal to the revenue in the hard-close auction when all bidders bid truthfully. It is shown that at least bidders in the hard-close auction will engage in sniping, which lowers seller revenue. In turn, the hard-close auction leads to lower seller revenue than the automatically extended auction. eBay auctions can thus be expected to yield lower seller revenue than the Amazon auctions. Within the Yahoo auctions context, we expect to see the same results for hard-close auctions when compared to soft-close auctions.

## 3. Empirical specification

## 3.1. Data

We collected data for the Playstation 2 (PS2) items from online auctions on Yahoo.com which started as early as on June 17, 2003 and which ended as late as

December 20, 2003. Our dataset comprises 761 auctions of the PS2 item and the bids submitted in those auctions. Playstation 2 is a game console that is easily available in the stores for a single price all around the U.S. One of the few aspects we could not control for is the specifics of the item being auctioned. Most of the auctions are PS2 hardware auctions but some come with small additions like a game, a memory card or a second controller. A few PS2 consoles are used while others are brand new in a factory sealed box. Therefore, while collecting our data we tried to minimize heterogeneity by collecting items which are listed under the same title.

In the original data set, we had winning bids varying between 0.99 dollars and around 480 dollars. After reviewing some auctions with very low values we observe that these auctions list primarily non-physical goods. Examples include information on how to get cheap PS2, and information on how to modify the hardware so that the buyer can play pirated games. Another problem we faced with this data of non-physical goods was the low sales price of the item. Since our benchmark item is sold everywhere in the U.S. for the price of 179.99 dollars, looking at items that are sold for low prices might affect our findings due to the resulting bias. Thus, we divide the dataset into two parts; lowvalue and high-value items. We label the auctions that ended with a winning bid that is lower than 25 dollars as low-value auctions.

In this study we show how sellers behave strategically when they make their choices while creating the auction. If the item is not a physical one then it has a marginal cost close to zero and if it is a very low-value item, then sellers may not put much effort in designing the auction and this may affect our findings. Thus, having the cut-off price helps us differentiate among sellers who act strategically and those that are less likely to do so.

We choose the cut-off price of 25 dollars both by studying the data and also by looking at the pricing schedule of Yahoo.com. When the seller posts his/her item on Yahoo.com and if the item is sold, s/he has to pay Yahoo.com a fee depending on the closing price (i.e. winning bid). This fee is determined by a step function. One of the jump points of this step function is at the price point of 25 dollars. Additionally, it is also reasonable to think that sellers start selling physical goods and start caring for the revenue they will receive from the auction when the value of the item is above 25 dollars.

Another change we adopt in this study is the attempt to normalize the diversity of winning bids due to different characteristics of the items being sold. Therefore, we only include the auctions with a buy price and use this information to create a new variable we call the Winning Bid Ratio (WBR):

$$
\text { Winning   Bid   Ratio } = \frac {\text { Winning   Bid }}{\text { Buy   Price }}
$$

Effectively, buy price is nothing but a limit on the winning bid since the item cannot be sold for a value higher than the buy price. Thus, our new variable, the Winning Bid Ratio (WBR), provides us with a number between 0 and 1, indicating what portion of the maximum possible bid the seller expects to receive as the resulting winning bid. We use this new variable as a proxy for seller revenue. It is a crucial part of our paper since we utilize it as the dependent variable of our regressions.

Including only the auctions with a buy price is not too limiting since we still maintain most of our initial dataset for our regressions; 80% of the PS2 auctions contain a buy price. We study 761 unique auctions that attracted 8320 bids. Among these 761 auctions, 539 of them fall under the high-value category and the rest, 222 of them, under the low-value category. Tables 1 and 2 present descriptive statistics for both high-value and low-value auctions.

In addition to the Winning Bid, which is the price that the highest bidder pays the seller at the end of the auction, we have the Bid Increment which is the value that the seller sets indicating the minimum amount of bid that is possible in that particular auction. Setting a high Bid Increment may scare away some bidders from the auction whereas having it too little may give a wrong signal about the quality of the good. Thus, the seller must be careful while setting this number.

Another value that the seller has to decide on while setting up an auction is the Shipping Price. It indicates how much it will cost to the winner of the auction to have the item shipped. Since sellers do not have to determine Shipping Price while setting their auction sites, only 425 out of 761 have actually specified a number. Thus, in our regressions, instead of using the Shipping Price itself, we employ a dummy variable for it. This variable equals to one when there exists a ship price and zero otherwise. Hence we observe the effect of including a Shipping Price on the revenue of the auction.

Table 1  
Descriptive statistics for high-value auctions

<table><tr><td rowspan="2">Variables</td><td colspan="5">High-value items</td></tr><tr><td>Obs.</td><td>Mean</td><td>Std. dev.</td><td>Min</td><td>Max</td></tr><tr><td>Winning bid</td><td>539</td><td>134.65</td><td>67.26</td><td>25</td><td>480</td></tr><tr><td>Bid increment</td><td>539</td><td>1.88</td><td>1.03</td><td>0.05</td><td>5</td></tr><tr><td>Shipping price</td><td>313</td><td>17.34</td><td>17.72</td><td>5</td><td>310</td></tr><tr><td>Closing dummy</td><td>539</td><td>0.67</td><td>0.47</td><td>0</td><td>1</td></tr><tr><td>Buy price</td><td>539</td><td>151.4</td><td>86.48</td><td>25</td><td>799.95</td></tr><tr><td>Auction length</td><td>539</td><td>2.36</td><td>2.49</td><td>0.0007</td><td>10.33</td></tr><tr><td>Buy-now execution dummy</td><td>539</td><td>0.69</td><td>0.46</td><td>0</td><td>1</td></tr><tr><td>Number of bids</td><td>539</td><td>14.31</td><td>29.99</td><td>1</td><td>257</td></tr><tr><td>Number of bidders</td><td>539</td><td>2.57</td><td>2.5</td><td>1</td><td>15</td></tr></table>

Table 2  
Descriptive statistics for low-value auctions

<table><tr><td rowspan="2">Variables</td><td colspan="5">Low-value items</td></tr><tr><td>Obs.</td><td>Mean</td><td>Std. dev.</td><td>Min</td><td>Max</td></tr><tr><td>Winning bid</td><td>222</td><td>8.22</td><td>5.74</td><td>0.99</td><td>24.99</td></tr><tr><td>Bid increment</td><td>222</td><td>0.35</td><td>0.17</td><td>0.05</td><td>0.5</td></tr><tr><td>Shipping price</td><td>112</td><td>6.73</td><td>3.93</td><td>0.01</td><td>16</td></tr><tr><td>Closing dummy</td><td>222</td><td>0.67</td><td>0.47</td><td>0</td><td>1</td></tr><tr><td>Buy price</td><td>222</td><td>11.03</td><td>8.06</td><td>0.99</td><td>49.95</td></tr><tr><td>Auction length</td><td>222</td><td>3.67</td><td>3.4</td><td>0.012</td><td>10.46</td></tr><tr><td>Buy-now execution dummy</td><td>222</td><td>0.63</td><td>0.49</td><td>0</td><td>1</td></tr><tr><td>Number of bids</td><td>222</td><td>2.73</td><td>5.89</td><td>1</td><td>59</td></tr><tr><td>Number of bidders</td><td>222</td><td>1.36</td><td>0.91</td><td>1</td><td>9</td></tr></table>

Sellers also have the option of choosing the Auction Length. Auction can last anywhere between 2 to 10 days. The bidder traffic reflected by the Number of Bids submitted and Number of Bidders participating at an auction is also an important aspect of online auctions. Below, we analyze these variables and their effects in more detail.

We next introduce a key variable for auction design. Yahoo.com gives the sellers an option for the ending time of their auctions. The seller can choose between a hardclose auction and a soft-close one. In soft-close auctions, on the other hand, the closing time of the auction is automatically extended for 10 min if a bid is placed within the last 5 min of the auction. This may sound like a small distinction but the effect of it is very critical. As mentioned earlier, in the case of a hard-close auction some bidders find it more rewarding to wait until the last minutes of the auction and then submit their valuations. They hope that there will be at least one bidder whose bid will not get recorded due to congestion on the network and they will end up winning the item for a cheaper price. This is not possible in soft-close auctions because the auction will be postponed until all the bids are recorded. In our dataset we use a dummy variable to capture this distinction (Closing Dummy). A value of 1 indicates that the auction is hard-close and a value of 0 implies that it is a soft-close auction. Thus, in accordance with the theoretical studies mentioned above, we expect to observe lower WBR as the value of the dummy variable switches to one since the bidders employ a last-minute bidding strategy.

The final auction parameter is the Buy Price, which is effectively the highest bid that can be submitted in a given auction. If a bid that matches or exceeds the Buy Price is submitted then the auction ends and the highest bidder wins the item for the Buy Price. There are only a few auctions in our original data set that do not contain a Buy Price. Thus, instead of estimating the effect of including a Buy Price, we choose to utilize it to calculate a new variable, WBR, which helps us to normalize the winning bids for each auction.

Next, we consider auctions in four different categories depending on their closing rule and their valuations. Then, we study the average number of bids and bidders under these four categories.

1) Number of bids:

<table><tr><td>Average number of bids</td><td>Low-value</td><td>High-value</td></tr><tr><td>Hard-close</td><td>2.44 (4.44)</td><td>15.01 (31.93)</td></tr><tr><td>Soft-close</td><td>3.34 (8.1)</td><td>12.89 (25.64)</td></tr><tr><td colspan="3">Note: Standard deviations are in parenthesis.2) Number of bidders:</td></tr><tr><td>Average number of bidders</td><td>Low-value</td><td>High-value</td></tr><tr><td>Hard-close</td><td>1.34 (0.72)</td><td>2.57 (2.36)</td></tr><tr><td>Soft-close</td><td>1.47 (1.25)</td><td>2.65 (2.82)</td></tr></table>

Note: Standard deviations are in parenthesis.

We see that the main variation is due to the valuation of the auction rather than the closing type of the auction. It is also interesting to see that in high-value auctions bidders are much more active in terms of bidding than in low-value auctions. For example, in hard-close auctions, when the valuation is low, 1.34 bidders submitted 2.44 bids on average. On the other hand, when the valuation is high, there is a 92 percent increase (2.57) in the number of bidders but more than 500% increase in the number of bids submitted (15.01). Similar trend can be observed for soft-close auctions. Thus, we detect quite a substantial increase in bidding activity as we move from low-value to high-value auctions.

The effect of closing type on how bidders submit their bids is interesting to analyze. Soft-close auctions tend to attract more bidders regardless of the auction value. For low-value items, more bidders in soft-close auctions submit more bids as well. But, surprisingly, for highvalue auctions, even though hard-close auctions attract fewer bidders, they submit more bids than the bidders in soft-close auctions. Thus, we see that in high-value auctions the bidders tend to be more active in terms of submitting bids when the auction is a hard-close one.

In summary, soft-close auctions attract more bidders and more bids when the auction is a low-value one.

Thus, we expect to see a significant effect of the closing type on WBR, whereas in the high value case, soft-close auctions attract more bidders but less bids than hardclose auctions. Thus, the effect of the closing choice is not straightforward for high-value auctions.

Following Roth and Ockenfels' [16] equilibrium of last-minute bidding, we can say that high bidding activity for hard-close auctions means that bidders usually start a bidding war, thus causing all the bidders submit their bids early on during the auction. This implies that in our dataset, for high-value auctions, there is almost no lastminute bidding taking place since bidding wars are being started. Thus, we do not expect not to see any significant effect of the closing type on WBR in our estimation results when focusing on high-value auctions.

## 3.2. Estimation results

We estimate three different specifications using three separate datasets. We make use of high-value auctions, low-value auctions and the combination of the two. Model I includes only the Closing Dummy and the constant (plus Low-Value Dummy when studying all auctions). Model II introduces three additional variables: Bid Increment, Shipping Dummy and Auction Length. In the end, we add Number of Bids for Model III. In all these models the dependent variable is WBR. All specifications are estimated using a least squares model (Table 3).

The results for all auctions and low-value auctions yield that the coefficient on the Closing Dummy is negative and statistically significant across models II and III. Furthermore, the coefficient magnitudes are very close for both models. In contrast, the coefficients for the high-value auctions carry the same signs but are

Table 3  
Estimation results for all auctions

<table><tr><td>Variable</td><td>I</td><td>II</td><td>III</td></tr><tr><td>Closing dummy</td><td>0.012(0.85)</td><td>-0.044 * (3.23)</td><td>-0.037 * (2.80)</td></tr><tr><td>Bid increment</td><td></td><td>-0.015 * (2.44)</td><td>-0.016 * (2.57)</td></tr><tr><td>Shipping dummy</td><td></td><td>-0.071 * (5.53)</td><td>-0.067 * (5.23)</td></tr><tr><td>Auction length(days)</td><td></td><td>-0.024 * (9.16)</td><td>-0.021 * (8.11)</td></tr><tr><td>Number of bids</td><td></td><td></td><td>-0.001 * (5.12)</td></tr><tr><td>Low-valuedummy</td><td>-0.092 * (5.01)</td><td>-0.089 * (4.53)</td><td>-0.110 * (5.59)</td></tr><tr><td>Constant</td><td>0.914 * (83.84)</td><td>1.077 * (59.12)</td><td>1.084 * (60.13)</td></tr><tr><td>R-squared</td><td>0.05</td><td>0.2335</td><td>0.2690</td></tr><tr><td>Prob&gt;F</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>Observations</td><td>761</td><td>761</td><td>761</td></tr></table>

Notes: The dependent variable is WBR. T-statistics are in parentheses. ⁎ Indicates significance at 1% level.

Table 5

not statistically significant. Therefore, the effect of the Closing Dummy on the WBR depends on the value of the item. Setting a hard-close auction affects the WBR significantly and negatively for low-value items. However, we are not able to find a similar relation when we consider high-value ones (Table 4).

The insignificance of the Closing Dummy for highvalue items can be explained by the number of bidders and bids in an auction. As discussed by Schindler [17], hardclose option is seen as an incentive for one experienced bidder to choose that particular auction over a very similar one. This is precisely the case in our dataset. We observe significantly more bidders and bids in hard-close auctions when compared to soft-close ones. Moreover, Ockenfels and Roth [16] have shown that a single early bid is sufficient to start a bidding war. As a result, most hardclose auctions attract early bids, causing bidding wars and eliminating the possibility of last-minute bidding. In addition, we observe that in all auctions switching from soft-close to hard-close lowers the WBR by around 4%.

As the Number of Bids and Number of Bidders are highly correlated, in order to prevent multicollinearity, we do not include the Number of Bidders in our model. Except for the Number of Bids, other variables have signs as expected and are generally statistically significant. Larger Number of Bids observed in an auction has a negative impact on the WBR when we obtain our estimates for all and high-value auctions. However, when we use the data from low-value auctions, the effect of Number of Bids on WBR reverses and it is not statistically significant. The reason for the negative impact is the WBR variable. When Buy Price is high, it is not executed and the Number of Bids is larger since the auction does not end early. Thus, we tend to observe a correlation between high Number of Bids and high Buy Prices which translates into lower WBR.

Table 4  
Estimation results for high-value auctions

<table><tr><td>Variable</td><td>I</td><td>II</td><td>III</td></tr><tr><td>Closing dummy</td><td>0.009 (0.71)</td><td>-0.019 (1.56)</td><td>-0.012 (1.03)</td></tr><tr><td>Bid increment</td><td></td><td>-0.015* (2.36)</td><td>-0.016* (2.65)</td></tr><tr><td>Shipping dummy</td><td></td><td>-0.042* (3.73)</td><td>-0.034* (3.13)</td></tr><tr><td>Auction length (days)</td><td></td><td>-0.023* (7.44)</td><td>-0.018* (6.06)</td></tr><tr><td>Number of bids</td><td></td><td></td><td>-0.002* (5.51)</td></tr><tr><td>Constant</td><td>0.915* (89.69)</td><td>1.04* (59.64)</td><td>1.04* (61.84)</td></tr><tr><td>R-squared</td><td>0.0009</td><td>0.2119</td><td>0.3134</td></tr><tr><td>Prob&gt;F</td><td>0.4749</td><td>0.00</td><td>0.00</td></tr><tr><td>Observations</td><td>539</td><td>539</td><td>539</td></tr></table>

Notes: The dependent variable is WBR. T-statistics are in parentheses. ⁎ Indicates significance at 1% level.

Estimation results for low-value auctions

<table><tr><td>Variable</td><td>I</td><td>II</td><td>III</td></tr><tr><td>Closing dummy</td><td>0.018 (0.51)</td><td>-0.109* (2.74)</td><td>-0.11* (2.76)</td></tr><tr><td>Bid increment</td><td></td><td>0.113 (0.88)</td><td>0.117 (0.91)</td></tr><tr><td>Shipping dummy</td><td></td><td>-0.15* (3.50)</td><td>-0.153* (3.49)</td></tr><tr><td>Auction length (days)</td><td></td><td>-0.027* (4.12)</td><td>-0.027* (4.18)</td></tr><tr><td>Number of bids</td><td></td><td></td><td>0.001 (0.46)</td></tr><tr><td>Constant</td><td>0.817* (28.47)</td><td>1.037* (27.99)</td><td>1.035* (27.57)</td></tr><tr><td>R-squared</td><td>0.0011</td><td>0.2149</td><td>0.2159</td></tr><tr><td>Prob&gt;F</td><td>0.6109</td><td>0.00</td><td>0.00</td></tr><tr><td>Observations</td><td>222</td><td>222</td><td>222</td></tr></table>

Notes: The dependent variable is WBR. T-statistics are in parentheses. ⁎ Indicates significance at 1% level.

Bid increment has a negative but small effect on the WBR. One unit change in the Bid increment has a 1.5 unit negative effect on the WBR. In addition, this effect is significant for high-value items but not for low-value ones. This is intuitive since low-value items tend to have low Bid increments and changes in them does not effect the bidding decisions of bidders (Table 5). On the other hand, higher Bid increments in high-value items would scare away bidders and thus lower the WBR.

The coefficient on Shipping Dummy is negative and significant. Its magnitude more than triples as we switch from high-value to low-value items. Thus, adding a shipping price has a negative effect on the WBR and this effect is much higher for low-value items. Additionally, we observe that Auction length also has a negative effect on the WBR. The coefficients are comparable among all three datasets. Thus, the effect of Auction length does not vary depending on the valuation of the items.

Note that the results are largely unaffected by alternative functional forms for the continuous variables. The signs and significance of all explanatory variables are unaffected by entering the continuous variables in logarithmic form. In addition, these results are solely for PS2 auctions and may differ for items with diverse demand structures.

## 4. Conclusion

In this paper, we study the relationship between the seller revenues and auction design parameters chosen by the sellers among Yahoo.com auctions. As opposed to eBay's exogenously set hard-close auctions, Yahoo.com provides an endogenous choice to the sellers on whether they would like to run hard-close or soft-close auctions. This creates a natural experiment environment for us to study the effect of these choices on the seller revenue. We collect and analyze data from Playstation 2 auctions listed on Yahoo.com's auction site. Our findings provide guidance to sellers planning to use online auctions provided by Yahoo.com as well as online auction site designers.

In answering the research questions in the beginning of the paper, we find that the online auction ending rule makes a difference in sellers' revenues. In particular, hard-close auctions yield lower revenue. This is especially the case for lower value items. For highvalue items, we observe more bidders and bids. This potentially causes a bidding war and eliminates any expected gains from last-minute bidding. As a result, overall, we observe a negative effect of the closing dummy on the sellers' revenues. This is not too surprising since on the one hand the seller revenues may increase due to the possibility of last-minute bidding activity which attracts more bidders and on the other hand the seller revenues may decrease if the last-minute bidding ends up in a lower winning bid. However, this result depends on whether the auctioned item is a high or low-value product. We also demonstrate that, from the sellers' perspective, placing a shipping price, setting an auction length, the number of bids and setting a bid increment significantly impact their revenues.

There are several ways this work can be extended by expanding on the limitations of this study. First, seller reputation information can be collected and included as an independent variable to test whether it has an impact on the WBR. Second, the design of the auction page itself such as availability of pictures and other product specific information can be coded and included in the model. We believe that Yahoo.com provides a sufficiently rich source of research questions as the basis of a series of future studies. As our future work, we will be focusing on studying various products offered in Yahoo.com auctions. One of the interesting questions is to compare highliquidity versus low-liquidity items to observe their effect on the last-minute bidding phenomenon.

## References

[1] R. Bapna, P. Goes, A. Gupta, A theoretical and empirical investigation of multi-item on-line auctions, Information Technology and Management 1 (1) (2000) 1–23.

[2] R. Bapna, P. Goes, A. Gupta, On-line auctions: insights and analysis, Communications of the ACM 44 (11) (2001) 42–50.

[5] C. Beam, A. Segev., Auctions on the Internet: A field study, working paper 1032, Haas School of Business, University of

California, Berkeley, CA, http://groups.haas.berkeley.edu/ citm/ publications/papers/wp-1032.pdf (1998).

[6] C. Dellarocas, The digitization of word of mouth: promise and challenges of online feedback mechanisms, Management Science 49 (10) (2003) 1407–1424.

[7] D. Houser, J. Wooders, Reputation in Auctions: Theory and Evidence from eBay, Journal of Economics and Management Strategy (in press).

[8] V. Krishna, Auction Theory, Academic Press (2002).

[9] J.A. Livingston, How valuable is a good reputation? A sample selection model of Internet auctions, The Review of Economics and Statistics 87 (3) (2005) 453–465.

[10] D. Lucking-Reiley, Using field experiments to test equivalence between auction formats: magic on the Internet, American Economic Review 89 (5) (1999) 1063–1080.

[11] D. Lucking-Reiley, Auctions on the Internet: what's being auctioned, and how? Journal of Industrial Economics 48 (3) (2000) 227–252.

[13] M.I. Melnik, J. Alm, Does a seller's ecommerce reputation matter? Evidence from Ebay auctions, The Journal of Industrial Economics L (3) (2002) 337–350.

[14] P. Resnick, R. Zeckhauser, Trust among strangers in Internet transactions: empirical analysis of eBay's reputation system, in: Michael R. Baye (Ed.), The Economics of the Internet and E-Commerce., Vol. 11 of Advances in Applied Microeconomics, Elsevier Science, Amsterdam (2002).

[15] S.S. Reynolds, J. Wooders, Auctions with a buy-now price, Working Paper, University of Arizona (2004).

[16] A.E. Roth, A. Ockenfels, Last-minute bidding and the rules for ending second-price auctions: evidence from eBay and Amazon auctions on the Internet, American Economic Review 92 (4) (2002) 1093–1103.

[17] J. Schindler, Late bidding on the internet, Working Paper, Vienna University of Economics and Business Administration (2003).

[18] E. Snir, L. Hitt, The emerging knowledge economy: exchange in Internet spot markets for IT expertise, Management Science 49 (11) (2003) 1504–1520.

[19] R.T. Wilcox, Expert and amateurs: the role of experience in Internet auctions, Marketing Letters 11 (4) (2000) 363–374.

Ilke Onur is currently an Assistant Professor in the Department of Economics at TOBB Economics and Technology University. He earned his Ph.D. in Economics from the University of Texas at Austin in 2005. His current research interests are industrial organization, game theory, auction theory, economics of information systems and electronic commerce.

Kerem Tomak is currently an Assistant Professor at the Department of Information, Risk and Operations Management at the University of Texas at Austin. His current research interests include pricing information goods, online auction design and firm level behavioral economics.
