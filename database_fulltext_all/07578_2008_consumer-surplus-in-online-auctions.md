---
otero_id: 7578
otero_key: "9DSHH9FF"
title: "Consumer Surplus in Online Auctions"
authors: "Ravi Bapna; Wolfgang Jank; Galit Shmueli"
year: "2008"
journal: "Information Systems Research"
doi: "10.1287/isre.1080.0173"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [128.122.253.228] On: 01 July 2015, At: 16:12 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

## 6SR

## Information Systems Research

![](/api/attachments/9DSHH9FF/fulltext/images/b007c7a43a35390eefaa133ff7ee89fc6f18ad49b45c76da317160ac43d62d6d.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Consumer Surplus in Online Auctions

Ravi Bapna, Wolfgang Jank, Galit Shmueli,

## To cite this article:

Ravi Bapna, Wolfgang Jank, Galit Shmueli, (2008) Consumer Surplus in Online Auctions. Information Systems Research 19(4):400-416. http://dx.doi.org/10.1287/isre.1080.0173

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2008, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/9DSHH9FF/fulltext/images/1e8c02da813f3d722aeadddfe8ab7c0ce46aaf3d63aebf384fc8333a410c1134.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Consumer Surplus in Online Auctions

Ravi Bapna

Information and Decision Sciences, University of Minnesota, Minneapolis, Minnesota 55455, and Centre for IT and Networked Economy, Indian School of Business, Hyderabad, India, ravi\_bapna@isb.edu

Wolfgang Jank, Galit Shmueli Robert H. Smith School of Business, University of Maryland, College Park, Maryland 20742 {wjank@rhsmith.umd.edu, gshmueli@rhsmith.umd.edu}

espite the growing research interest in Internet auctions, particularly those on eBay, little is known about quantifiable consumer surplus levels in such mechanisms. Using an ongoing novel field experiment that involves real bidders participating in real auctions, and voting with real dollars, we collect and examine a unique data set to estimate consumer surplus in eBay auctions. The estimation procedure relies mainly on knowing the highest bid, which is not disclosed by eBay but is available to us from our experiment. At the outset we assume a private value second-price sealed-bid auction setting, as well as a lack of alternative buying options within or outside eBay. Our analysis, based on a sample of 4,514 eBay auctions, indicates that consumers extract a median surplus of at least \$4 per eBay auction. This estimate is unbiased under the above assumptions; otherwise it is a lower bound. The surplus distribution is highly skewed given the diverse nature of the data. We find that eBay’s auctions generated at least \$7.05 billion in total consumer surplus in 2003 and could generate up to \$7.68 billion if the private value sealed-bid assumption does not hold. We check for the validity of our assumptions and the robustness of our estimates using an additional data set from 2005 and a randomly sampled validation data set from eBay.

Key words: eBay; sniping; highest bid; consumer surplus

History: Sumit Sarkar, Senior Editor; Michael Smith, Associate Editor. This paper was received on July 13, 2006, and was with the authors 8 <sup>1</sup> months for 2 revisions. Published online in Articles in Advance July 31, 2008.

## 1. Introduction

Internet-based electronic markets, such as eBay, exemplify how information technology (IT) can propel long-standing business processes, such as auctions, to an unprecedented scale and scope. eBay’s popularity is evident in the reported \$23.8 billion in gross merchandise sales for 2003, up from \$14.9 billion in 2002. Despite the vast amounts of economic activity carried out using the e-market IT artifact, very little has been said about the quantifiable benefits such markets provide to consumers. In this paper we report on consumer surplus levels in eBay auctions. Quantifying the consumer surplus in eBay is an important part of understanding its overall benefit to the economy.

Classical microeconomic theory uses the notion of consumer surplus as the welfare measure that quantifies benefits to a consumer from an exchange. Marshall (1920, p. 124) defined consumer surplus as “the excess of the price which he (a consumer) would be willing to pay rather than go without the thing, over that which he actually does pay  ” It is also traditional to visualize consumer surplus as the roughly triangular area lying under a downwardsloping demand curve and above the rectangle that represents actual money expenditure. Yet, despite its established theoretical standing, empirical studies of consumer surplus levels are not widely observed in the literature. Imagine a traditional retailer using the posted price selling format asking a consumer checking out, “By the way, how much were you really willing to pay for this item?”

Our approach at estimating consumer surplus in online auctions is based on novel data from a field experiment that allows bidders to use our web-based tool, Cniper (http://www.Cniper), to snipe eBay auctions. In using the tool, the bidders who win the auction reveal to us the otherwise unobserved, highest winning bid on eBay. To the best of our knowledge, this is the first attempt in information systems (IS) research to deploy an IS artifact (an eBay sniping agent, called Cniper, developed by us) publicly, and to derive hitherto unobservable insights from data generated by the use of the artifact.

While a variety of studies (Goolsbee and Petrin 2004, Nevo 2001) have measured consumer surplus in traditional markets, such measures are scarce in electronic markets. There are two exceptions. Brynjolfsson et al. (2003) demonstrate how new product introduction in electronic markets can lead to significant consumer welfare gains. There is also an emerging stream of work, exemplified by Ghose et al. (2004), that is looking closely at the welfare implications (including consumer welfare) of secondary markets for used books. Both studies devise econometric estimation procedures, based on Hausman (1981), to measure consumer welfare levels where they are not directly observable in posted price markets. Typically, in such markets, willingness to pay (WTP) has to be inferred indirectly through surveys, contingent valuation techniques, and price changing experiments such as promotions and discounts. Surveys of WTP have credibility issues and have led to a stream of research dealing with contingent valuation precision and bias reduction (see Diamond and Hausman 1994). We believe that more needs to be said and done in a wider context about quantifying consumer surplus.

In this paper we demonstrate the suitability of using direct mechanisms (Myerson 1981), such as auctions, to quantify consumer surplus. Auction theory is built on the fact that a consumer with a valuation for an item, strategizes and formulates a bid so as to maximize her surplus (McAfee and McMillan 1987). In the context of a second-price sealed-bid auction, Vickrey (1961) proved that truth-telling is a dominant strategy. Our work, which is empirical in nature, relies on this strong theoretical foundation to estimate a quantity that has so far been elusive.

Despite all the attention to eBay auctions (for a review see Bajari and Hortacsu 2004), there are as yet no published studies of consumer surplus generated in eBay. We are aware of two other groups of researchers currently involved in estimating these consumer surplus levels. Giray et al. (2005) study data from auctions of computer monitors on eBay and estimate bidding functions by maximum likelihood using five different assumptions about the underlying distribution (log-normal, Gamma, Weibull, Pareto, and logistic) of the independent private value.<sup>1</sup> Song (2004) develops a semi-parametric approach and applies it to auctions of university yearbooks. A key feature of this approach is that it relies on the secondand third-highest bids observed on eBay to estimate the highest bid. In contrast, our study is designed to rely on the revealed bid of the highest winning bidder.

Both (Giray et al. 2005 and Song 2004) studies assume a private value setting and provide valuable information for surplus levels in specific item categories of eBay. However, eBay is a generalized auction house, carrying auctions in 30 major categories ranging from antiques to video games. We view our work as providing an alternative broader view of consumer surplus generated in eBay. Our research objective is to present consumer surplus estimation procedures, as well as data, that reflect the wide variety of auctions on eBay.

We expect to contribute to this stream of research by addressing the following research questions:

(1) How can consumer surplus be estimated in eBay auctions?

(2) What is the level of consumer surplus in eBay auctions?

(3) How robust is the estimation procedure to challenges of its underlying assumptions?

We are motivated to quantify the level of consumer surplus not just to provide confidence intervals on the actual dollar levels, but also to establish robust benchmarks that can be used to measure the impact of future policy changes on consumer welfare. These policy changes could range from increased eBay fees<sup>2</sup> to, say, a new bid increment policy.<sup>3</sup>

We also discuss the usefulness and limitations of consumer surplus in informing us about the value of eBay as an exchange mechanism. Our analysis indicates that consumers extract a median surplus of at least \$4 per eBay auction, with a 95% confidence interval of -\$375 \$425. Given that the median transaction value is approximately \$14 in our data, this indicates that consumer surplus is on the order of 30% of the transaction value of eBay. This is consistent with previous research (Vakrat and Seidmann 1999) which found that online prices are often 25% lower than comparable items sold in retail channels. Clearly, the overall value of eBay as an exchange is equal to the buyer’s WTP minus the seller’s willingness to sell (WTS). As with every other eBay study we are aware of, we are limited by not having access to sellers’ WTS.<sup>4</sup> However, to the extent that sellers selling on eBay are behaving rationally, it is reasonable to assume that they have factored in their best outside option before deciding to sell on eBay. In equilibrium, this should be reflected in their hidden reservation price, as well as in eBay’s ability to charge for their services. If this is the case, consumer surplus can be added to the auction price to yield an upper bound on social welfare.<sup>5</sup>

The rest of the paper is organized as follows. Section 2 introduces the setup of the study, the assumptions, and the model. Section 3 describes the data. Section 4 presents our results on the levels of consumer surplus in eBay auctions. Section 5 is devoted to a series of robustness checks to validate the assumptions and adjust the estimates for potential biases. Section 6 concludes by pointing out limitations and directions for future research.

## 2. Setup

There have been several in-depth studies that describe eBay’s second-price ascending proxy-bid auction mechanism. A key feature is that at the termination of the auction, the highest bidder wins and pays a price equal to the second-highest bid plus one bid increment. The exceptions to this occur when (1) the

eBay posts almost the complete bid history after the auction closes, with the exception of the value of the highest bid. For instance, consider the bid history shown in Figure 1 for a Nokia 6610 GSM cell phone. Conspicuous by its absence is the exact amount bid by the winner “kanchenjunga.”<sup>7</sup> Because the winner’s bid is not disclosed by eBay, no direct measure of the revealed WTP of the winning bidder is publicly available. To overcome this limitation, we design an ongoing field experiment that allows real-world bidders to use Cniper, our web-based bidding agent, to snipe eBay auctions.

two highest bids are equal, wherein the earlier bidder is awarded the item at a price equal to her bid; (2) the two highest bids are less than an increment apart, wherein the higher bidder is awarded the item at a price equal to her bid; (3) if the reserve price is higher than the second-highest bid, wherein the higher bidder is awarded the item at the reserve price; and (4) if the buy-it-now price is accepted. Another established feature, resulting primarily from eBay’s hard closing time, is that last-minute bidding or sniping is widely prevalent. Roth and Ockenfels (2002) provide theoretical and empirical insights into sniping behavior on eBay. They observe that in 240 antiques auctions, 89 had bids in the last minute and 29 in the last 10 seconds.<sup>6</sup> Similar findings have been reported by Bajari and Hortaçsu (2003), Shmueli et al. (2007), and Schindler (2003). Explanations for late bidding range from tacit collusion against sellers to the presence of naïve bidders who do not understand proxy bidding, to a common value component in the items being auctioned. For this study, we make use of the fact that sniping is widely used on eBay.

Internet-based field experiments that deal with real bidders in real markets provide a contrast to the controlled environment of laboratory experiments with student subjects. This is evident in the work of Lucking-Reiley (1999) and List and Lucking-Reiley (2002). They show how age-old questions such as revenue equivalence and the importance of decision costs, respectively, can be examined using field experiments with real bidders and without any

Bidders: You can retract your bid under certain circumstances only Sellers: See how to cancel bids if vou need to

Figure 1 Almost Complete Bid History, the Exception Being the Highest Bid

<table><tr><td colspan="3">Bid History</td></tr><tr><td colspan="2">Brand New Nokia 6610 GSM GPRS Unlocked World Cell Phone</td><td>Item number: 3092620119</td></tr><tr><td>Currently: US $170.00</td><td>Quantity: 1</td><td></td></tr><tr><td>First Bid: US $130.00</td><td>Started: Apr-19-04 12:44:18 PDT</td><td></td></tr><tr><td># of bids: 13</td><td>Ends: Apr-22-04 12:44:18 PDT</td><td></td></tr><tr><td colspan="2">Time left: Auction has ended.</td><td></td></tr><tr><td colspan="2">Seller: malmonrode (2)</td><td></td></tr><tr><td colspan="2">View page with email addresses (Accessible by Seller only) Learn more.</td><td></td></tr><tr><td colspan="3">Bidding history (Highest bids first)</td></tr><tr><td colspan="3">If you and another bidder placed the same bid amount, the earlier bid takes priority</td></tr><tr><td>Date of Bid</td><td>Bid Amount</td><td>User ID</td></tr><tr><td>Apr-22-04 12:44:09 PDT</td><td>US $170.00</td><td>kanchenjunga (4)</td></tr><tr><td>Apr-22-04 12:44:06 PDT</td><td>US $167.50</td><td>ray7748 (6)</td></tr><tr><td>Apr-22-04 12:42:25 PDT</td><td>US $165.00</td><td>afuah25 (1)</td></tr><tr><td>Apr-22-04 12:39:39 PDT</td><td>US $162.50</td><td>ray7748 (6)</td></tr><tr><td>Apr-22-04 12:38:31 PDT</td><td>US $160.00</td><td>afuah25 (1)</td></tr><tr><td>Apr-22-04 12:29:27 PDT</td><td>US $157.50</td><td>ray7748 (6)</td></tr><tr><td>Apr-22-04 03:24:38 PDT</td><td>US $155.00</td><td>atul08101979 (1)</td></tr><tr><td>Apr-22-04 12:26:08 PDT</td><td>US $155.00</td><td>afuah25 (1)</td></tr><tr><td>Apr-19-04 18:37:50 PDT</td><td>US $150.00</td><td>afuah25 (1)</td></tr><tr><td>Apr-22-04 03:24:01 PDT</td><td>US $150.00</td><td>atul08101979 (1)</td></tr><tr><td>Apr-22-04 02:49:28 PDT</td><td>US $145.00</td><td>petesaboy78 (151 ★)</td></tr><tr><td>Apr-21-04 00:45:56 PDT</td><td>US $140.00</td><td>petesaboy78 (151 ★)</td></tr><tr><td>Apr-19-04 13:44:34 PDT</td><td>US $135.00</td><td>tanlerocky (4)</td></tr></table>

theoretical assumptions that would be enforced in the laboratory. Our study is designed in the spirit of the above-mentioned field experiments. Bidders using Cniper to bid on their behalf reveal their WTP to the agent. For auctions where our agent wins, we can measure surplus assuming the following conditions hold.

## 2.1. Assumptions

Given the nature of our data collection scheme we need to begin with the following four assumptions to estimate consumer surplus. We then conduct a series of robustness checks to validate these assumptions, and where necessary and feasible, we adjust the estimates for any potential biases.

(1) We assume that bidders are behaving consistent with an independent private value setting.

(2) We assume that our data reflect bidders treating the eBay auction mechanism as a sealed-bid secondprice auction.

(3) We assume that there is no particular selection bias and that the bidder and auction characteristics observed on Cniper are not significantly different from those observed on eBay in general.

(4) We assume the lack of other buying options within or outside eBay.

If any of these assumptions is violated, then our estimate represents a lower bound on consumer surplus. This is based on the fact that any deviation from the private value sealed-bid second-price auction setting would imply the breakdown of truthtelling as a dominant strategy. In that case we would not observe the true value but rather some fraction of it, resulting in a lower bound on surplus. A similar bid-shading logic leading to a lower bound applies to the assumption of no alternate buying options. In the presence of alternatives, the bidders might exercise an option value, thereby shading their bids. With respect to selection bias, if Cniper winners are more experienced, they might extract higher surplus (e.g., by targeting a more favorable auction to bid on than the average eBay user). Thus, our surplus estimate assuming no selection bias is a lower bound.

## 2.2. Model for Estimating Consumer Surplus

For completeness, we specify exactly how we measure surplus given the above assumptions. We consider the general setup described in Klemperer (1999) and

Krishna (2002), where bidder i has a signal denoted by $x _ { i }$ and a valuation $v _ { i } .$ . Following the notation of Klemperer, we have

$$
v _ {i} = \alpha x _ {i} + \beta \sum_ {j \neq i} x _ {j},\tag{1}
$$

where  and $\beta \left( \alpha \geq \beta \right)$ are weighting components that indicate the degree of private/common-value component. Given the assumption of independent private value, we note that $\beta = 0$ . In such models, bidders are concerned only about their own signals and not the signals of others. This indicates that bidder types can be represented by their valuations, thus $x _ { i } = v _ { i } .$ Let $v _ { ( 1 ) }$ denote the highest valuation among the pool of bidders in an auction. Let $p$ denote the auction closing price as observed on eBay. In second-price sealed-bid auctions, Vickrey (1961) proved that truthtelling is a dominant strategy. Thus, the eBay auction in this stage resembles a second-price sealed-bid auction, under which bidder i will have the incentive to bid $b _ { i } ( v _ { i } ) = v _ { i }$ . Thus consumer surplus $c s ^ { i p v }$ accrued to the winning bidder of an auction under the independent private value setting is

$$
c s ^ {i p v} = b (v _ {(1)}) - p = b _ {\mathrm{max}} - p,\tag{2}
$$

where $b _ { \mathrm { m a x } }$ is the highest winning bid. Note that $b _ { \mathrm { m a x } }$ is not directly observable on eBay, but it is available to us from our Cniper agent.

Appendix A extends the surplus analysis to the case where the bidders are under a common value informational setting and are adjusting their final bids downward to account for the winner’s curse, the phenomenon in which winners end up paying more than the item’s worth in a common market.

## 2.3. Description of the Bidding Agent

The prevalence of sniping on eBay has lead to the development of several independent third-party sniping agents that help bidders place last-second bids. The interested reader is referred to Bapna (2003) for a detailed review of sniping agents and their technology. This study uses data from one such agent, Cniper. In the design of the agent, we place our servers in close network proximity to eBay’s servers,<sup>8</sup> ensuring that bids are delivered in a timely manner. While most competing eBay sniping agents are fee based,<sup>9</sup> Cniper is a free service and has a growing user base of over 2,000 bidders. Between July 23, 2003<sup>10</sup> and June 24, 2004, Cniper placed 69,571 bids on eBay on behalf of its users. Cniper is developed using PHP<sup>11</sup> and MySQL<sup>12</sup> and is deployed on an Apache webserver sitting on a Unix box. The fact that Cniper is a free service ensures no incentive for any bid shading to account for bidding agent commissions. The lack of commissions also attracts entry for the tool, which in turn provides us with continuously richer observations of real economic agents acting in real markets.

While the full technical details of Cniper’s operation are beyond the scope of this paper, a brief overview of its usage is necessary to motivate its usefulness in measuring consumer surplus. Agents such as Cniper allow bidders to reveal (a) their WTP for a specific item being auctioned, and (b) the number of seconds before the close of the auction that they want their bid to be placed. For illustrative purposes, we continue with our earlier example of the Nokia 6610 GSM phone auction that was sniped and won by eBay user “kanchenjunga” using Cniper and whose bid history is displayed in Figure 1. We show the process of the bidder sniping and the actual winning bid placed in Figure 2.

Figure 2 reveals that bidder “kanchenjunga” submitted \$180 for the item and won the auction by outsniping bidder “ray7748” by 3 seconds. Recall from Figure 1 that the winning bid or price is \$170. Thus, under Assumptions 1–4 above, bidder “kanchenjunga” derived a surplus of \$10 from this auction.

## 3. Data

The data used in our analysis consist of 4,514 eBay auctions that took place between January 9, 2004 and April 21, 2004.<sup>13</sup> In all these auctions the winner was a Cniper user, and the auction was competitive (i.e., the number of bids was larger than 1). We included only competitive auctions because, for a single-bid auction, the surplus is equal to the difference between the bid and the seller’s opening bid. However, it is well established that opening bids are endogenous (Bajari and Hortacsu 2003) and that sellers use them as strategic tools by setting them artificially low to attract bidders. Therefore, including such auctions would add significant noise to our estimates of surplus.

Figure 2 Top Panel: Bidder Kanchenjunga Requests Cniper to Bid \$180 for eBay Item 092620119 Eight Seconds Before the Auction Closes. Bottom Panel: Row Two of Kanchenjunga’s Cniper Log Shows the \$180 Bid as Submitted and Successful  
![](/api/attachments/9DSHH9FF/fulltext/images/0a47d8e1c731ff8a24cf1af38ea72c47f20dfb3abd730775ac93796de03729f1.jpg)

![](/api/attachments/9DSHH9FF/fulltext/images/fea18ecad74768dfb0ee1645494a2929538ea09df71c98c3f0c7bc639727842d.jpg)

The auctions in our data were carried out in one of three major currencies: US dollar (USD), Great Britain pound (GBP), and the euro. The items auctioned were across a wide variety of categories, spanning most<sup>14</sup> of eBay’s 30 high-level categories.<sup>15</sup> To maintain a minimal cardinality level, we condensed eBay’s categories into 18 major categories. An additional 19th category was created for items in which the category description was missing.<sup>16</sup>

To the best of our knowledge, currency and category have not featured in the extant analysis of eBay data. In addition, we recorded from eBay the following information on each auction: Opening and closing prices in their original currency and their USD equivalent,<sup>17</sup> whether hidden reserve was used, the starting and ending time<sup>18</sup> and date, the number of bids placed in the auction, the number of unique bidders participating in the auction, and seller and winner ratings. From Cniper we obtained the winning bid. Surplus is then computed by subtracting the price from the winning bid (after converting into USD).

Table 1 Summary Statistics of Relevant Variables

<table><tr><td>Column</td><td>Avg.</td><td>Std. dev.</td><td>Min.</td><td>Max.</td><td>Median</td></tr><tr><td>Price (in USD)</td><td>60.78</td><td>229.39</td><td>0.08</td><td>7,600.00</td><td>14.82</td></tr><tr><td>Opening bid (in USD)</td><td>19.29</td><td>101.68</td><td>0.01</td><td>3,570.50</td><td>3.00</td></tr><tr><td>Seller rating</td><td>2,588.15</td><td>9,048.57</td><td>-1.00</td><td>170,889.00</td><td>339.50</td></tr><tr><td>Number of bids</td><td>6.72</td><td>5.46</td><td>2.00</td><td>50.00</td><td>5.00</td></tr><tr><td>Winner rating</td><td>229.40</td><td>390.29</td><td>-3.00</td><td>11,350.00</td><td>106.00</td></tr><tr><td>Number of bidders</td><td>4.26</td><td>2.55</td><td>2.00</td><td>29.00</td><td>3.00</td></tr><tr><td>Auction duration</td><td>6.66</td><td>2.10</td><td>1.00</td><td>10.00</td><td>7.00</td></tr><tr><td>Reserve</td><td>0.04</td><td>0.20</td><td>0.00</td><td>1.00</td><td>0.00</td></tr><tr><td>Surplus (in USD)</td><td>16.89</td><td>60.39</td><td>0.00</td><td>1,593.56</td><td>4.00</td></tr></table>

Table 1 describes summary statistics for each of the variables in our study. Seller and winner ratings are proxies for experience on eBay because they correlate highly with the number of the user’s transactions. Auction durations can vary between 1, 3, 5, 7, and 10 days. Reserve is a binary variable that denotes whether a hidden reserve was used. It is interesting to note that the empirical distribution of surplus is best approximated by a three-parameter Weibull distribution (see Bapna et al. 2007). We also note that 7% of the auctions have a zero surplus (Bapna et al. 2007). Zero surplus on eBay arises in two cases: when the two highest bids are equal, and when the difference between the two highest bids is smaller than the prevailing bid increment.

For our robustness checks we use two additional data sets, which will be described in §5.

## 4. Results: Estimating Total Surplus

We begin by estimating total surplus using our sample. Following the standard approach and for completeness, we use the overall mean surplus to derive the total consumer surplus estimate. A standard, albeit crude, approach is to use the overall mean surplus (\$16.89) multiplied by the estimated total number of 417.5 million<sup>19</sup> eBay auctions in 2003. This gives an estimate of \$7.05 billion (with a 95% confidence interval of $\$ 7.05\pm (1.96) (60 . 39 )\sqrt { 4 1 7 , 5 0 0 ,00 0 } =$ -\$7048 \$7053) in total consumer surplus in eBay in 2003. Note that the mean surplus and its variance vary significantly across categories, as shown in Table 2. The category-level breakdown should be useful to researchers studying eBay data in a particular category.

Table 2 Breakdown of Surplus by eBay Categories

<table><tr><td>Category</td><td>Percent of auctions in data (%)</td><td>Mean surplus ($)</td><td>Standard deviation ($)</td></tr><tr><td>Antique/art/crafts</td><td>2.35</td><td>37.55</td><td>74.25</td></tr><tr><td>Automotive</td><td>5.58</td><td>25.35</td><td>104.78</td></tr><tr><td>Books</td><td>5.85</td><td>6.08</td><td>9.07</td></tr><tr><td>Business/industrial</td><td>2.19</td><td>17.14</td><td>34.11</td></tr><tr><td>Clothing/accessories</td><td>3.61</td><td>7.68</td><td>13.17</td></tr><tr><td>Coins/stamps</td><td>3.48</td><td>9.09</td><td>15.11</td></tr><tr><td>Collectibles</td><td>11.17</td><td>26.53</td><td>93.51</td></tr><tr><td>Computer/network</td><td>5.47</td><td>17.28</td><td>62.69</td></tr><tr><td>Consumer electronics</td><td>4.54</td><td>23.82</td><td>101.41</td></tr><tr><td>Everything else</td><td>2.92</td><td>21.36</td><td>47.24</td></tr><tr><td>Health &amp; beauty</td><td>1.84</td><td>4.23</td><td>6.12</td></tr><tr><td>Home/garden</td><td>6.89</td><td>8.76</td><td>19.20</td></tr><tr><td>Jewelry</td><td>4.34</td><td>25.93</td><td>87.96</td></tr><tr><td>Missing</td><td>10.66</td><td>12.87</td><td>28.54</td></tr><tr><td>Music/movies/video games</td><td>10.97</td><td>5.54</td><td>25.06</td></tr><tr><td>Photography</td><td>3.35</td><td>24.67</td><td>45.90</td></tr><tr><td>Pottery/glass</td><td>1.04</td><td>21.91</td><td>39.03</td></tr><tr><td>SportingGoods</td><td>3.74</td><td>16.02</td><td>44.85</td></tr><tr><td>Toys/hobbies</td><td>10.01</td><td>22.08</td><td>63.15</td></tr><tr><td>Overall</td><td>100.00</td><td>16.89</td><td>60.39</td></tr></table>

Although we use surplus means for computing total surplus, means are not reliable measures of an auction’s typical surplus value. Surplus is extremely right-skewed and thus the mean does not describe the physical center of the surplus distribution well (for an analysis of surplus distribution see Bapna et al. 2007). We therefore use medians for reporting per-auction surplus levels, and totals for reporting overall social welfare.

First, we obtain a per-auction median surplus of \$4.00. Then, to measure the sampling error, we compute the 95% bootstrap confidence interval (based on 10,000 replications) of -\$375 \$425. We reiterate that our estimates of consumer surplus are unbiased if all the assumptions in §2.1 hold. Otherwise, they are a lower bound. This issue is further investigated in the next section.

## 5. Robustness Analysis

This analysis is designed to check the validity of the four assumptions underlying our surplus estimation. In the following we examine each of the assumptions; where needed, we adjust the surplus estimates for biases; and in the process we evaluate the tightness of the lower bound.

## 5.1. Assumptions 1, 2: Independent Private Value and Second-Price Sealed-Bid

Going purely by the current literature (Adams et al. 2006, Giray et al. 2005, Song 2004) the private value assumption is reasonable. Adams et al. (2006, p. 24) show that bidding data from the auctions of used Corvette cars in eBay conforms to a private value setting. They find little evidence that bidders are accounting for the winner’s curse, as they would be expected to under a common value setting. They state, “If there was a winner’s curse problem we would expect bidders to discount their bids more when they expected there to be a larger number of participants in the auction.” This is not evident in the bidding data.

However, given the diverse nature of our data spanning almost all of eBay’s major categories, we hesitate to rely purely on the existing literature to claim private values. We therefore start by applying the winner’s curse test to our data. Similar to Bajari and Hortaçsu (2003), we regress the normalized bids on the number of bidders, controlling for all other variables (product category, currency, auction duration, seller rating, and winner rating), and find no evidence of a negative correlation between the normalized bids and number of bidders. The coefficient estimated from the model is <sub>+</sub>0.04 and highly significant (p-value < 10E 16). This relationship is also confirmed by scatterplots and other supportive analyses.

Furthermore, there are additional behavioral reasons that might imply a private value second-price sealed-bid setting. Under such a setting we expect bidders to place a single early bid on Cniper, although bidders do have an option of revising their bids up until the last minute of the auction. For instance, consider a stylized setting where, in a 10-day eBay auction, the bidder visits Cniper on day 5, places a bid (that will be submitted by Cniper a few seconds before the auction ends), and does not return to Cniper to revise her bid. Bidders deviating from a private value second-price sealed-bid setting might be inclined to bid late and/or revise their initial bid if they are influenced by other bidders’ bids, as would be expected in a common value setting. This raises an interesting point that contrasts our approach with the methodology and findings of Zeithammer and Adams (2006). Using a limited (three-item) data set from eBay, they find that bidders are closer to an ascending price auction bidding strategy. Rather than developing a structural model such as theirs, we offer an alternative way of examining this empirically by studying the actual bid placement times on Cniper.

Although at the time of data collection the bid placement time on Cniper was not recorded, we are fortunate that this feature was added to the tool subsequently. We therefore collected an additional data set from Cniper, which includes 3,828 eBay auctions that took place between January 17, 2005 and April 2, 2005 (roughly a year after our original data set was collected). This data set includes all variables as in the original 2004 data set, and in addition the time stamps of each bid placed on Cniper. We use this new information to compute both the relative bid times and the number of bid revisions for each winner in a certain auction. The new 2005 data set is similar to the 2004 data set in most respects, aside from having a median surplus that is 20% higher (See more on the increased consumer surplus level in 2005 in §6). For a detailed description of this data set and a comparison with the 2004 data set, see Bapna et al. (2007).

Our new 2005 data set reveals that the majority of bidders tended to place only a single bid during the auction at a time much earlier than the last moments of the auction. The distribution of bid placement time on Cniper is shown in Figure 3. From the histogram in Figure 3 we see that only 22% of bids were placed after 97% of the auction duration had passed. In fact, the median relative bid time is 91.2, which means that 50% of bids were submitted before 91% of the auction had taken place. To see how this translates into actual hours, see the medians below the boxplots: For auctions of 3–7 days it is roughly equivalent to 12 hours before the auctions close, for 10-day auctions is it a day before the auction closes, and for 1-day auctions it is 2.5 hours.

Figure 3 Vast Majority of Bids Are Logged on Cniper Much Earlier Than the Auction’s Closing Time  
Distribution of relative bid placement time  
![](/api/attachments/9DSHH9FF/fulltext/images/8653864dff1cc3824cba75f984903336337f3c3cf02454d5a847e702348b8607.jpg)  
Relative bid placement time (48 bins)

Coupled with the fact that the majority of bidders do not revise their Cniper bids (see Table 3), we feel there is strong evidence to support our claim of a private value sealed-bid second-price setting, under which we observe a tight lower bound of the WTP (Vickrey 1961). Note that if the private value setting holds, auction theory (Krishna 2002) suggests that surplus levels should decrease in the number of bidders. In other words, as buyer competition increases, prices increase, and the seller extracts a larger portion of the total surplus. We can test this by specifying a regression of surplus on the number of bidders, controlling for auction, seller, and item characteristics. Table 4 shows that the coefficient for the number of bidders (lbidders) is negative and statistically significant. We also see, as expected, that surplus levels are increasing in bidder experience (proxied by winner rating, lwinrate) and decreasing in seller experience (proxied by seller rating, lsellerrate). The model controls for the dollar value of the item (proxied by price, lprice), the item category and the currency fixed effects.

Table 3 The Vast Majority of Bids Are Not Revised

<table><tr><td>Number of bid revisions</td><td>Frequency (%) of winners</td></tr><tr><td>0</td><td>3,688 (96.34%)</td></tr><tr><td>1</td><td>75 (1.96%)</td></tr><tr><td>2</td><td>4 (0.10%)</td></tr><tr><td>3+</td><td>61 (1.59%)</td></tr></table>

Bid placement time distribution by auction duration  
![](/api/attachments/9DSHH9FF/fulltext/images/8c1782faa8744f27652b651afbc1d34196262a65d295ffe8423ff864854a8e99.jpg)

5.1.1. Quantifying Tightness of the Lower Bound. While our estimates are based on the entire data set, it is possible to restrict the analysis to those bidders who placed a single, early bid. Such bidders exhibit a high degree of conformance to the private values information setting, where truth-telling in a second-price sealed-bid auction is a dominant strategy (Vickrey 1961). Hence, surplus estimates based solely on such bidders should be higher than on a general pool of bidders. A comparison of our original estimates with those derived from the restricted set would give an indication of the tightness of our lower bound on consumer surplus. To do that, we formally define an early-single-bid (ESB) bidder as one whose number of bid revisions is zero and the relative bid time is less that the 90th percentile of the auction’s duration. Given the auction durations in our data, this corresponds to approximately single bids that were placed before the last day. According to this criterion 50% of bidders in our data set are ESB bidders. Figure 4 shows that the surplus distribution of ESB winners and non-ESB winners is very similar, with a slightly higher frequency of zero surplus for non-ESB winners.

Table 4 Regression Analysis Shows That Surplus Decreases with the Number of Bidders

<table><tr><td colspan="5">The regression model</td></tr><tr><td>Input variables</td><td>Coefficient</td><td>Std. error</td><td>p-value</td><td>SS</td></tr><tr><td>Constant term</td><td>0.66627491</td><td>0.10663457</td><td>0</td><td>15,805.24707</td></tr><tr><td>CURRENCY_GBP</td><td>0.18178184</td><td>0.05617059</td><td>0.00129207</td><td>30.6573658</td></tr><tr><td>Days</td><td>0.03090316</td><td>0.00759501</td><td>0.00005495</td><td>24.18881416</td></tr><tr><td>Iprice</td><td>0.4913457</td><td>0.01859158</td><td>0</td><td>1,640.897827</td></tr><tr><td>lopenbid</td><td>-0.03155914</td><td>0.01277542</td><td>0.0138352</td><td>0.74278837</td></tr><tr><td>|bidders</td><td>-0.2400315</td><td>0.04333498</td><td>0.00000005</td><td>42.76245499</td></tr><tr><td>Iwinrate</td><td>0.02205114</td><td>0.01178509</td><td>0.06191905</td><td>5.78774643</td></tr><tr><td>Isellerrate</td><td>-0.03228449</td><td>0.00845586</td><td>0.00015157</td><td>6.00266027</td></tr><tr><td>High_Category</td><td>0.37143224</td><td>0.04085029</td><td>0</td><td>146.4749146</td></tr><tr><td>Low_Category</td><td>-0.19608299</td><td>0.03696761</td><td>0.00000017</td><td>31.17577362</td></tr><tr><td>Residual df</td><td></td><td colspan="3">4,504</td></tr><tr><td>Multiple R-squared</td><td></td><td colspan="3">0.278729179</td></tr><tr><td>Std. dev. estimate</td><td></td><td colspan="3">1.05266464</td></tr><tr><td>Residual SS</td><td></td><td colspan="3">4,990.89502</td></tr></table>

Note. Variable names starting with / are log-transformed, e.g., /price is . Vari

To quantify this difference, if any, and to account for other control factors, we estimate a regression model similar to the one in Table 4, using the 2005 data set that includes the ESB dummy variable. Table 5 gives the estimated model and shows that the coefficient for the ESB dummy is positive and statistically significant. Because surplus is logtransformed, this indicates that auctions with ESB winners generate a higher average surplus of 9% compared to non-ESB winners. This gives us a quantification of deviation from the private value sealed-bid second-price auction assumption. In other words, if all bidders were behaving as ESB bidders, all else being equal, our average surplus estimate would have been 9% higher. It means that our total surplus estimate of \$7.05 billion is a lower bound and that eBay might generate up to \$7.68 billion if the private value sealed-bid assumption does not hold.

Table 5 Surplus Is Higher by an Average of 9% for ESB Bidders

<table><tr><td colspan="5">The regression model</td></tr><tr><td>Input variables</td><td>Coefficient</td><td>Std. error</td><td>p-value</td><td>SS</td></tr><tr><td>Constant term</td><td>0.36445817</td><td>0.123481</td><td>0.00331174</td><td>13,982.99902</td></tr><tr><td>CURRENCY_GBP</td><td>0.32129583</td><td>0.05101016</td><td>0</td><td>95.18525696</td></tr><tr><td>CURRENCY_US</td><td>0.13543212</td><td>0.04425046</td><td>0.00232878</td><td>1.11509669</td></tr><tr><td>Days</td><td>0.03551869</td><td>0.00816652</td><td>0.00001659</td><td>35.95498657</td></tr><tr><td>Ibidders</td><td>-0.25830403</td><td>0.0460427</td><td>0.00000003</td><td>139.7454071</td></tr><tr><td>Iopenbid</td><td>-0.06621119</td><td>0.01319544</td><td>0.00000073</td><td>208.1359253</td></tr><tr><td>Iprice</td><td>0.45240551</td><td>0.02034435</td><td>0</td><td>611.4992065</td></tr><tr><td>Isellerrate</td><td>-0.02272111</td><td>0.00916732</td><td>0.01352552</td><td>7.23598337</td></tr><tr><td>Iwinrate</td><td>0.07692938</td><td>0.01358527</td><td>0.00000003</td><td>41.30053329</td></tr><tr><td>Early-single-bid?</td><td>0.08932343</td><td>0.0344597</td><td>0.00982016</td><td>8.19872093</td></tr><tr><td>High_Category</td><td>0.31303445</td><td>0.05353588</td><td>0.00000001</td><td>118.5448303</td></tr><tr><td>Low_Category</td><td>-0.17701921</td><td>0.04406511</td><td>0.00006802</td><td>17.02599907</td></tr><tr><td>Residual df</td><td></td><td colspan="3">3,814</td></tr><tr><td>Multiple R-squared</td><td></td><td colspan="3">0.24189736</td></tr><tr><td>Std. dev. estimate</td><td></td><td colspan="3">1.02714276</td></tr><tr><td>Residual SS</td><td></td><td colspan="3">4,023.854492</td></tr></table>

Further robustness of the overall estimation is evident from the close similarity between the 2004 and 2005 data sets in terms of the magnitude and significance of the different regression coefficients. In particular, note the striking similarity of the number of bidders, winner, and seller experience coefficients.

Figure 4 Surplus Distribution for ESB Bidders (Bottom) and Non-ESB Bidders (Top)  
![](/api/attachments/9DSHH9FF/fulltext/images/7a3b2b3f26ff0fffcc781400e65772ca4791f9212deeb91d1afdf173fe9a0058.jpg)

For completeness, note that in cases where the private value assumption does not hold, additional assumptions can be made about the distribution of signals (e.g., valuations belong to a uniform distribution and the number of bidders is perfectly observable) to back out the common value of the items sold (see Appendix A for the proof). Under these additional assumptions, the highest bidder’s bid should be scaled by a factor of n 1/n 2.

Overall, our empirical analysis suggests that the private value sealed-bid second-price assumption is reasonably satisfied in our data, and our lower bound of total surplus is no lower than approximately 9% of the real overall consumer surplus in eBay.

## 5.2. Assumption 3: Selection Bias and Generalizability

While there is academic and practitioner support of the notion that sniping is widespread, because our data set arises from a sniping web site, it raises questions about the generalizability of our results to the overall population of eBay auctions. It can also be argued that Cniper bidders are more experienced than the average eBay bidder. To validate this we need to establish whether the auction and the bidder characteristics we observe in our sample are significantly different from a randomly selected sample of auctions on eBay. To the best of our knowledge, no other study using eBay data has attempted to do this.

We address this empirically by testing whether a randomly drawn validation sample of 1,000 eBay auctions has similar distributions of key auction parameters as do our field experiment data. We find that in all auction parameters except user ratings, including item price, item categories, number of bidders, and opening bid, there is no significant difference between our validation and field data. The interested reader is referred to Appendix B for a detailed comparison on each of the auction variables.

With respect to the bidder experience, it is standard practice in the literature (Ba and Pavlou 2002) to use their total eBay feedback reputation score as a proxy for experience. From the boxplots of winner rating for Cniper versus general eBay winners (see Appendix B), we see that Cniper winners tend to be more experienced than the average eBay winner. However, when examining the impact of winner rating on surplus (see Table 4), we see that the winner rating coefficient is statistically insignificant at a 5% significance level. Note that the regression is based on a wide range of Cniper winner ratings. This indicates that even if Cniper winners are more experienced, the experience level should not affect surplus estimates.<sup>20</sup> Furthermore, we believe that the fact that our sample relies on experienced winners means that they are more likely to understand Vickrey (1961) and to behave close to what theory predicts, so that the high bid that we are observing is more likely to reflect their true WTP.

Finally, with respect to seller ratings, it appears that sellers in our Cniper sample tend to have lower ratings than those in general eBay auctions (see Appendix B). Together with the statistically significant (negative) effect of seller ratings on surplus (see Table 4), this means that our surplus estimates serve as a lower bound and are therefore conservative.

## 5.3. Assumption 4: Consideration of Alternative Buying Options

Our model does not consider the presence of ongoing simultaneous, overlapping, or sequential auctions within eBay that might be selling the identical product and attracting the attention of the bidder. In addition, bidders’ willingness to bid an amount in a given auction might also be influenced by other outside buying options. Unfortunately, our wide-ranging data from a variety of eBay categories does not allow for easy access to outside book values or for consideration of what is going on in non-eBay markets. If, indeed, bidders use outside price comparison sites to cap their WTP on eBay, then once again our consumer surplus measures are conservative. As pointed out by Zeithammer (2006), Snir (2005), and Bapna et al. (2007), if bidders were to factor the overlapping, simultaneous, or sequential nature of auctions into their equilibrium bidding strategies, then bid shading would occur, which would deem our current surplus estimates as conservative. Zeithammer (2006) estimates this bid shading amount to result in a downward pressure of approximately 2%–5.6% of the price. This is based on data for popular mainstream items (MP3 players and movies in DVDs). In contrast, our data span both popular mainstream items but also many unique and less popular item categories. This impacts the degree of overlap and sequential availability that one can expect for a given auction, with rarer items having a lower number of concurrent/sequential auctions.

Table 6 Median Surplus Adjusted for Alternate Buying Options (with 95% Bootstrap Confidence Interval)

<table><tr><td>Inflation factor</td><td>1%</td><td>2%</td><td>3%</td><td>4%</td><td>5%</td><td>6%</td><td>7%</td><td>8%</td><td>9%</td></tr><tr><td>Median surplus</td><td>4.37</td><td>4.74</td><td>5.03</td><td>5.34</td><td>5.60</td><td>5.86</td><td>6.13</td><td>6.41</td><td>6.70</td></tr><tr><td>95% CI, lower bound</td><td>4.11</td><td>4.42</td><td>4.816</td><td>5.1</td><td>5.366</td><td>5.61</td><td>5.9</td><td>6.1</td><td>6.31</td></tr><tr><td>95% CI, upper bound</td><td>4.64</td><td>4.92</td><td>5.253</td><td>5.6</td><td>5.959</td><td>6.22</td><td>6.5</td><td>6.81</td><td>7.07</td></tr></table>

To evaluate the impact of alternative buying options, we consider both Zeithammer’s 2%–5.6% bid adjustment factor and the 9% factor obtained from the ESB analysis. Table 6 shows the median surplus as a function of adjusting the high bid up by an amount ranging from 1%–9% (recall that without adjustment the median surplus is \$4.00). We see that surplus increases linearly, with each additional 1% increasing median surplus by approximately \$0.35.

While the magnitude of the figures in Table 6 might seem low, consider that the median item price in our data set is approximately \$15. The price varies widely across categories, thus suggesting that the impact of alternate buying options could be economically significant in some categories. Future research on the degree of overlap in the different eBay categories would help researchers choose the right categoryspecific adjustment.

## 6. Conclusions

eBay auctions are at the forefront of e-commerce, demonstrating how the Internet can remove spatial and temporal constraints to make economic exchange mechanisms, such as auctions, mainstream. In 2003, sellers through eBay sold \$23.8 billion worth of merchandise. While gains from such trades to sellers<sup>21</sup> and eBay, the market maker, are obvious, little is known about consumer welfare levels accrued to buyers in electronic markets.

Our work contributes to the IS literature by quantifying the benefits that accrue to users of IT artifacts such as online marketplaces. We show that these benefits are significant, amounting conservatively to \$7.05 billion for 2003 alone. The 2005 data set that we collected for the robustness analysis indicates that the surplus level has grown from a median of \$4 per auction to \$4.83 and from a total estimate of \$7.05 billion to \$8.39 billion. These high and growing consumer surplus levels are one reason that online auctions are an attractive retail channel for consumers.

In addition to characterizing the consumer surplus level, we contribute methodologically by showing how the robustness analysis (and the necessary adjustments to the estimates) can be done empirically using additional data.

We also contribute to the IS literature by demonstrating the value of deploying an IT artifact in the form of a bidding agent for the benefit of real-world users. As bidders use this tool to win auctions on eBay, they leave behind information that is otherwise hard to capture about their WTP for items they bid on.

## 6.1. Study Limitations

Our estimation relies on four assumptions, which we validate and, where necessary, adjust our estimates for potential biases. We use early single-bid bidding on Cniper as a behavioral indicator of conformance to a private value second-price sealed-bid auction setting. Relaxing this assumption gives us an estimate of 9% of the tightness of our estimated surplus lower bound. While we attempt to check the generalizability of our results by comparing the variables in our field data with those in a randomly selected test data of 1,000 auctions, we realize that this test data set is only a fraction of the auctions conducted by eBay on a given date. We are limited in this aspect by having only public access to eBay’s search engine, which is clearly not designed for such a purpose. In particular, our sample does not include single-bid auctions, so that we avoid unreliable surplus estimates arising from the related endogeneity issue. However, estimating the proportion of single-bid auctions on eBay and their surplus behavior is an interesting problem. Finally, the observation that sellers in the Cniper samples had overall lower ratings than the general eBay seller population makes our surplus estimate conservative.

Our study is further limited by the fact that we do not consider the time costs associated with using and submitting a bid on eBay, which are likely to be incurred by both winning and losing bidders. We also do not consider the issue of collusive bidding, which is unobservable. The direction of bias in surplus estimates would depend on the collusion strategy. Last, because of the sniping nature of the data, we do not consider auctions that close earlier due the exercise of the buy-it-now option. These promise to be interesting directions for future research.

## Acknowledgments

The second and third authors’ research was partially funded by National Science Foundation (NSF) Grant DMI-0205489. They also gratefully acknowledge support by the University of Maryland Center of Electronic Markets and Enterprises. The authors thank Joe Bailey, Dipak Dey, Robert Garfinkel, Alok Gupta, Ali Hortaçsu, Jim Marsden, Ivan Png, and Alex Tung for their feedback on earlier versions of this paper. The paper benefited from feedback received at the Workshop on Information System Economics (WISE) and at research seminars at the Indian School of Business, University of Connecticut’s Operations and Information Management (OPIM) department, University of Connecticut’s Statistics department, and at the University of Minnesota. The paper also benefited from discussions at the October 2005 Federal Trade Commission Internet Auction Roundtable. Author names are in alphabetical order.

## Appendix A. Pure Common Values Setting

While it is commonly agreed that most eBay auctions have elements of both private and common value components, Bajari and Hortacsu (2003) point out that current analytical work has yet to determine equilibrium bidding strategies under this complex informational setting. Thus, like them, we consider the case of the pure common values setting as the alternative to the private value setting. In the context of Equation (1) in §2.2, this is obtained by setting $\alpha = \beta .$ The equilibrium bidding strategy for second-price sealedbid auctions under the pure common value setting was derived by Milgrom and Weber (1982). The primary consideration here for bidders is to avoid the winner’s curse by shading their bids in an increasing fashion with the number of competing bidders. The pure common value, or the mineral rights setting, implies $v _ { i } = v ,$ the ex post common value, and that v is same across all the bidders, but the signals $x _ { i }$ are interdependent. Only after conditioning on v $( \mathrm { i . e . , ~ } x _ { i } \mid V = v )$ do they become independent. To estimate surplus we need to estimate v, because we already know the price $p .$ Observe that under the common value setting

$$
V = \alpha \left(x _ {i} + \sum_ {j \neq i} x _ {j}\right).\tag{A1}
$$

In a second-price sealed-bid auction, a bidder with signal $x _ { i }$ will be willing to pay anything up to her expected value, conditional on her winning the object but being tied with just one other bidder with the same signal. Thus, the bid function for bidder i is to bid

$$
b _ {i} (v _ {i}) = E (V \mid x _ {i}) = \alpha x _ {i} + \alpha \sum_ {j \neq i} E (x _ {j} \mid x _ {i}).\tag{A2}
$$

Following Klemperer (1999), we assume that signals are uniformly distributed $X _ { i } \sim U ( 0 , 2 V )$ , and therefore the conditional distribution of a signal, given that it is below $x _ { i }$ $( \mathrm { i . e . , } x _ { i } \mid x _ { j } < x _ { i } ) ,$ , is $U ( 0 , x _ { i } )$ . This implies $E ( x _ { j } \mid x _ { j } < x _ { i } ) = x _ { i } / 2$ which leads to the following bid function:

$$
b _ {i} (v _ {i}) = E (V | x _ {i}) = \alpha x _ {i} + \alpha x _ {i} + \alpha (n - 2) \frac {x _ {i}}{2} = \alpha \bigg (\frac {n + 2}{2} \bigg) x _ {i}.\tag{A3}
$$

Choosing $\alpha = 1 / n ,$ , where n is the number of bidders, reduces this to the “average model” formulation as in Goeree and Offerman (2003). For $\alpha = 1 / n$ , we have the bid function

$$
b _ {i} (v _ {i}) = E (V \mid x _ {i}) = \frac {n + 2}{2 n} \cdot x _ {i}.\tag{A4}
$$

Under the assumption $X _ { i } \sim U ( 0 , 2 V )$ each signal is unbiased for estimating V . However, the sufficient statistic for estimating V is the highest value $X _ { ( n ) } ,$ and the maximum likelihood estimator for V is a function only of $X _ { ( n ) } .$ We therefore need only recover the signal of the winner (which is available through Cniper). This is also very useful from a practical point of view because of the presence of spurious bids at the start of the auction and the fact that the auction turns into a sealed-bid second-price auction only during the last moments (Bajari and Hortacsu 2003). Using only the highest bid keeps us away from such problems.

To recover $x _ { ( n ) }$ , we use the inverse of the bid function from Equation (A4),

$$
x _ {i} = b _ {i} (v _ {i}) \frac {2 n}{n + 2}.\tag{A5}
$$

![](/api/attachments/9DSHH9FF/fulltext/images/983d4d01f137cb572ba997eb4157419cabe63f1797ca5a1e9267d5412b68893d.jpg)  
Note. All variables are log transformed; ratings are also shifted by four to the right.

Plugging in the highest bid $b _ { \mathrm { m a x } }$ in place of $b _ { i } ( v _ { i } )$ gives us an estimate for $x _ { ( n ) } .$ In the case of $n = 2$ bidders, according to this formulation (as well as the classical formulation) each bidder assumes that the other bidder has an equal signal $( x _ { 1 } = x _ { 2 } = x )$ , and therefore $v = x ,$ . In such a case each bidder should bid his/her signal, which results in no winner’s curse. In our surplus computations for $n = 2$ we therefore use the difference between the highest bid and the price, similar to the private value setting.

Finally, the maximum likelihood estimator for V based on $X _ { i } \sim U ( 0 , 2 V )$ is given by $x _ { ( n ) } / 2$ . Note, however, that this estimator is biased,

$$
E (X _ {(n)} / 2) = \frac {n}{n + 1} \cdot V.\tag{A6}
$$

A bias-corrected estimator for the common value (using $( \mathsf { A } 5 ) \ – ( \mathsf { A } 6 ) )$ is

$$
\widehat {V} = \frac {n + 1}{n} \cdot \frac {X _ {(n)}}{2} = \frac {n + 1}{n + 2} \cdot b _ {\mathrm{max}}.\tag{A7}
$$

Thus, consumer surplus $\boldsymbol { c s } ^ { c v }$ in common value settings can be estimated by

$$
c s ^ {c v} = \widehat {V} - p.\tag{A8}
$$

Note that (A8) allows for negative values of surplus, which in the context of common values would signal the occurrence of the winner’s curse.

## Appendix B. Validation Analysis

Our objective is to test whether the sample of auctions obtained from Cniper is different from a randomly selected

Figure B.1 Box Plots of Numerical Cniper Variables vs. Validation (eBay) Variables

Figure B.2 QQ Plots of Cniper Variable vs. Validation (eBay) Variable  
![](/api/attachments/9DSHH9FF/fulltext/images/9f8cbee7b4934f5a188fb24917845405da73d00d9f1cb3e9f1fc45f7d20d2f6f.jpg)

![](/api/attachments/9DSHH9FF/fulltext/images/f7324e0d84f833b25a66166bd2d47cc5a853e4ac4a49ab32f081de1e9de4ffc8.jpg)

![](/api/attachments/9DSHH9FF/fulltext/images/a16f645321be177dfc910e278e8b9399f824e09e1b53de496276a052ca5ec10e.jpg)

![](/api/attachments/9DSHH9FF/fulltext/images/a003da84fdfe82d15f9d271669fc2993486a77fd5dcd8cb4483f8e121a6187b4.jpg)

![](/api/attachments/9DSHH9FF/fulltext/images/a1d16ac5a676b7eda26d3a1689541206261cda6991b3cb63bc1ef6d3e130fd31.jpg)

![](/api/attachments/9DSHH9FF/fulltext/images/5c40b00f0075bf48b953d3a17c2f13d723429d9fd2565518a8a3382ad4dcc232.jpg)  
Notes, Plots the validation percentile on the vertical axis versus its matching Cniper percentile on the horizontal axis (median versus median, etc.) for each Plots the validation percentile on the vertical axis versus its matching Cniper percentile on the horizontal axis (median versus median, etc.) for each butions match. Note that most of the distributions closely match, and that discrepancies occur at the very top percentiles because of very right-skewed distributions.

sample of eBay auctions. To obtain the latter, we undertook a title and description advanced search of eBay auctions, in the three currencies, using a neutral phrase May-13- 04. The string representing this date returned the maximum number of listings in a period of plus or minus 15 days, which is approximately 10,000 listings.<sup>22</sup> Subsequently, after the last of these auctions closed, we obtained all the information by parsing the HTML pages of those auctions that had at least one bid submitted (1,077 auctions<sup>23</sup>) to form the validation data. The only data missing were the surplus values, because eBay does not provide access to the winning bids. Subsequently, we compared the distribution of each of the variables in the validation data and the Cniper data to test for any significant difference.

These comparative studies are presented as a series of box plots (Figure B.1) and QQ plots (Figure B.2) for the numerical variables, and as bar and pie charts for the categorical variables (Figure B.3). For most variables we found no significant difference between the Cniper data and the validation data, supporting the assumption that the Cniper data are no different than any other randomly drawn set of eBay data. Only winner experience appears higher in Cniper, as described in §5.2.

<sup>23</sup> A large percentage of eBay auctions get no bids at all. Secondary eBay data sites, such as http://www.andale.com and Hammertap.

Figure B.3 Bar and Pie Charts of Categorical Cniper Variables vs. Validation (eBay) Variables  
![](/api/attachments/9DSHH9FF/fulltext/images/90c12fa0149dfcc0445acdc94bd4ee005d014cd5b2c5d47719ea07ab8ff006e5.jpg)

![](/api/attachments/9DSHH9FF/fulltext/images/92c638ac096d1a7e8ca80ab451bf2c63bfb9821ac372dfdee8cffb499a7e57fd.jpg)  
Note. Grey bars represent Cniper data and black bars represent validation data

![](/api/attachments/9DSHH9FF/fulltext/images/003d8f0365cb2616c61b6bdbc85df12724bc2b7c39e14a54a328a269c09135e4.jpg)

## References

Adams, C. P., L. Hosken, P. Newberry. 2006. Vettes and lemons on eBay. Available at http://papers.ssrn.com/sol3/papers.cfm? abstract\_id 880780.

Ba, S., P. A. Pavlou. 2002. Evidence of the effect of trust building technology in electronic markets: Price premiums and buyer behavior. MIS Quart. 26(3) 269–289.

Bajari, P., A. Hortaçsu. 2003. The winner’s curse, reserve prices and endogenous entry: Empirical insights from eBay auctions. RAND J. Econom. 3(2) 329–355.

Bajari, P., A. Hortaçsu. 2004. Economic insights from Internet auctions. J. Econom. Literature 42(2) 457–486.

Bapna, R. 2003. When snipers become predators: Can mechanism design save online auctions? Comm. ACM 46(12) 152–158.

Bapna, R., W. Jank, G. Shmueli. 2007. Measuring consumer surplus on eBay: An empirical study. Technical report, Smith School of Business, University of Maryland, College Park.

Bapna, R., S.-J. Chang, P. Goes, A. Gupta. 2007. Overlapping liquidation auctions: Empirical characterization of bidder. MIS Quart. Available at http://www.isb.edu/faculty/ravibapna/ papers/Overlapping%20Liquidation%20Auctions\_MISQ.pdf

Broersma, M. 2005. Amid Customer Backlash, eBay Reduces Some Fees. eWeek.com. http://www.eweek.com/article2/0,1895, 1761416,00.asp.

Brynjolfsson, E., Y. Hu, M. D. Smith. 2003. Consumer surplus in the digital economy: Estimating the value of increased product variety at online booksellers. Management Sci. 49(11) 1580–1596.

Diamond, P. A., J. A. Hausman. 1994. Contingent valuation: Is some number better than no number? J. Econom. Perspectives 8(4) 45–64.

Ghose, A., M. D. Smith, R. Telang. 2004. Internet exchanges for used books: An empirical analysis of product cannibalization and welfare impact. Inform. Systems Res. 17(1) 3–19.

Giray, T., K. Hasker, R. C. Sickles. 2005. Estimating consumer surplus in eBay computer monitor auctions. Paper presented at Federal Trade Commission Roundtable on The Economics of Internet Auctions, October, Washington, D.C.

Goeree, J., T. Offerman. 2003. Competitive bidding in auctions with private and common values. Econom. J. 113 598–613.

Goolsbee, A., A. Petrin. 2004. The consumer gains from direct broadcast satellites and the competition with cable television. Econometrica 72(2) 351–381.

Hausman, J. A. 1981. Exact consumer’s surplus and deadweight loss. Amer. Econom. Rev. 71(4, September) 662–676.

Klemperer, P. 1999. Auction theory: A guide to literature. J. Econom. Surveys 13(3) 227–286.

Krishna, V. 2002. Auction Theory. Academic Press, San Diego.

List, J. A., D. Lucking-Reiley. 2002. Bidding behavior and decision costs in field experiments. Econom. Inquiry 40(44) 611–619.

Lucking-Reiley, D. 1999. Using field experiments to test equivalence between auction formats: Magic on the Internet. Amer. Econom. Rev. 89(5) 1063–1080.

Marshall, A. 1920. Principles of Economics, 8th ed. MacMillan and Company Ltd., London.

McAfee, R. P., J. McMillan. 1987. Auctions and bidding. J. Econom. Literature 25(2) 699–738.

Milgrom, P., R. Weber. 1982. A theory of auctions and competitive bidding. Econometrica 50 1089–1122.

Myerson, R. 1981. Optimal auction design. Math. Oper. Res. 6 58–73.

Nevo, A. 2003. New products, quality changes and welfare measures computed from estimated demand systems. Rev. Econom. Statist. 85(2) 266–275.

Roth, A., A. Ockenfels. 2002. Last minute bidding and rules for ending second-price auctions: Theory and evidence from a natural experiment on the Internet. Amer. Econom. Rev. 92(4) 1093–1103.

Schindler, J. 2003. Late bidding on the Internet. Working paper, Vienna University of Economics and Business Administration, Wien, Austria.

Shmueli, G., R. P. Russo, W. Jank. 2007. The BARISTA: A model for bid arrivals in online auctions. Ann. Appl. Statist. 1(2) 412–411.

Snir, E. M. 2006. Online auctions enabling the secondary computer market. Inform. Tech. Management. 7(3) 213–234.

Song, U. 2004. Nonparametric estimation of an eBay auction model with an unknown number of bidders. Available at: http://faculty.arts.ubc.ca/usong/eBay.pdf.

Vakrat, Y., A. Seidmann. 1999. Can online auctions beat online catalogs? Proc. 20th Internat. Conf. Inform. System. ICIS 1999 Conference, Charlotte, NC, 132–143.

Vickrey, W. 1961. Counterspeculation, auctions, and competitive sealed tenders. J. Finance 16 8–37.

Zeithammer, R. 2006. Forward-looking bidding in online auctions. J. Marketing Res. 43(3) 462–476.

Zeithammer, R., C. Adams. 2006. Modeling online auctions with proxy-bidding: Ascending versus sealed model. Working paper, University of Chicago, Chicago.
