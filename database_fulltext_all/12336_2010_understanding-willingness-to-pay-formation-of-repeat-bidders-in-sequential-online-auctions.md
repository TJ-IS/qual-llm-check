---
otero_id: 12336
otero_key: "9SJEPD4Q"
title: "Understanding Willingness-to-Pay Formation of Repeat Bidders in Sequential Online Auctions"
authors: "Paulo B. Goes; Gilbert G. Karuga; Arvind K. Tripathi"
year: "2010"
journal: "Information Systems Research"
doi: "10.1287/isre.1080.0216"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/9SJEPD4Q/fulltext/images/e3a0d00d7b6d991fa0b514ff01429a4766f50a8453c28282cce4d0504c5477f3.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Understanding Willingness-to-Pay Formation of Repeat Bidders in Sequential Online Auctions

Paulo B. Goes, Gilbert G. Karuga, Arvind K. Tripathi,

## To cite this article:

Paulo B. Goes, Gilbert G. Karuga, Arvind K. Tripathi, (2010) Understanding Willingness-to-Pay Formation of Repeat Bidders in Sequential Online Auctions. Information Systems Research 21(4):907-924. http://dx.doi.org/10.1287/isre.1080.0216

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2010, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/9SJEPD4Q/fulltext/images/93741561412f881e0184f115dc093ed0f4b68cb9969f0387c4fed3ea0def6eed.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Understanding Willingness-to-Pay Formation of Repeat Bidders in Sequential Online Auctions

Paulo B. Goes

Management Information Systems, Eller College of Management, University of Arizona, Tucson, Arizona 85721, pgoes@eller.arizona.edu

Gilbert G. Karuga

Accounting and Information Systems Area, University of Kansas, Lawrence, Kansas 66045, gkaruga@ku.edu

Arvind K. Tripathi Information Systems and Operations Management, Michael G. Foster School of Business, University of Washington, Seattle, Washington 98195, tripathi@u.washington.edu

growing number of vendors are using a sequence of online auctions to sell large inventories of identical items. Although bidding strategies and bidder behavior in single auctions have been extensively studied, limited research exists on bidding in sequential auctions. We seek to explain how bidders in such an environment learn from the information, and form and update their willingness to pay (WTP). Using a large data set from an online auction retailer, we analyze the evolution of the bidders’ WTP as well as the effect of auction design on bidders’ WTP in sequential auctions. We see our study in the context of a longitudinal field experiment, in which we were able to track actions of repeat bidders over an extended period of time. Our results show that bidders WTP in sequential auctions can be explained from their demand characteristics, their participation experience in previous auctions, outcomes in previous auctions, and auction design parameters. We also observe, characterize, and measure what we call a modified demand reduction effect exhibited across different auctions, over time, by multiunit demand bidders. Our findings are important to enable better auction mechanism design, and more sophisticated bidding tools that explore the rich information environment of sequential auctions.

Key words: sequential online auctions; bidding behavior; willingness to pay; demand reduction History: Sumit Sarkar, Senior Editor; Waleel Muhauna, Associate Editor. This paper was received on April 5, 2006, and was with the authors 14 <sup>3</sup> months for 4 revisions. Published online in Articles in Advance May 12, 2009.

## 1. Introduction

Online auctions have been a key driver to the growth of e-commerce during the last decade. Realizing unprecedented opportunities provided by online auctions, such as wider market reach, low cost of selling, and opportunity to learn market trends by observing and analyzing historical bidding data, traditional online retailers are increasingly using this distribution channel. Some retailers (for example—Sears<sup>1</sup> and Dell) have opened stores on eBay to host their auctions, whereas others such as Sam’s Club<sup>2</sup> and Dell<sup>3</sup> run their own auctions.

Sequential auctions are often used to off-load the inventory in several smaller lot-size auctions. This method of organizing these auctions exploits the nature of the online auctions distribution channel to meet the retailers’ objectives. These are aimed at minimizing inventory holding costs and maximizing revenues by selling the items in a price-discriminating environment under a compressed time frame (Tripathi et al. 2008). Inventory holding costs can be minimized by offering the total inventory in a single auction. However, the continuous nature of demand accrual at online auction sites (Bapna et al. 2001) would marginalize the net revenues because of the resultant time-variant oversupply. These considerations rationalize the use of sequential online auctions to distribute large inventories.

Auctions are dynamic price-setting mechanisms in which bidders’ valuations and demands determine prices. Sequential auctions create an opportunity for bidders to learn market trends and going prices of the item. Unlike isolated online auctions, bidders in sequential auctions can participate in many auctions of the same item (Pinker et al. 2003). Price-sensitive consumers may take this unique opportunity to assess demand and supply patterns by observing winning bids in the sequence of auctions. Exposure to these auctions helps these bidders gain more information about the availability of the same item in subsequent auctions. Auction literature shows conflicting price trends in sequential auctions: the “morning effect” (Gandal 1997), where prices increase as sequential auctions progress; the “afternoon effect” (McAfee and Vincent 1993, Beggs and Graddy 1997), where prices decline as the auction sequence progresses; and inconclusive price trends where increasing as well as declining trends are observed (Jeitschko 1998). The information effect that underlies the strategies adopted by bidders in sequential auctions leads bidders to trade-off an increased probability of winning in earlier auctions for more information and increase expected payoffs in later auctions (Jeitschko 1998). Price trends in sequential online auctions are partly a manifestation of changes in the participating bidders’ willingness to pay (WTP). Understanding how bidders in sequential auctions learn and update their WTP can explain the consequent variation in auction price trends.

Repeat bidders gain experience and observe the WTP of other bidders through participation. The pool of competing bidders is comprised of new and experienced bidders. This mix of experienced and inexperienced bidders results in experiencebased heterogeneity among bidders and weakens the assumption of common knowledge in classical auction theory (Pinker et al. 2003). Figure 1 shows the proportion of repeat bidders in a sequence of identical item auctions contained in our data set. We later discuss the data in detail, but at this point, a quick reflection shows how the proportion of repeat bidders increases as the sequence of auctions progresses. The proportion of repeat bidders increases to about 40% of all bidders. If indeed bidders learn from participating and revising their bidding behavior, we can expect heterogeneous bidding behavior in sequential auctions.

Figure 1 Fraction of Repeat Bidders in Sequential Auctions  
![](/api/attachments/9SJEPD4Q/fulltext/images/071650a0854b472fa6f9f7e4f40ddc84282b45f4505ddbea084c225e16b8ae62.jpg)

In the studies referenced above, equilibrium auction outcomes are derived under a constrained assumption about the effect of sequential auctions bidders WTP. In Jeitschko (1998), for example, bidders are assumed to be of two types, and the seller is assumed to have two items for sale. In this research, we empirically show that bidders’ WTP evolves in different stages of participation in sequential online auctions, a phenomenon that confounds the determination of equilibria in such environments.

We contribute to the literature of online auctions in many ways. Using real data from an online retailer, we detect and empirically measure the evolution of bidders’ WTP in sequential online auctions. The unique characteristics of the data set provide the necessary background of a longitudinal field experiment that enabled us to track the repeat bidders and their actions. By considering the environment of multiple sequential auctions of the same item and its unique information characteristics, we investigate how bidders progressively refine their WTP in stages. Using the bidding history of individual bidders over the entire sequence of auctions, we develop longitudinal models to explain how their WTP evolve. We demonstrate heterogeneity in bidders’ learning and updating of their WTP in sequential auctions. We further investigate the key drivers that determine bidders’ WTP commitments in sequential online auctions. These drivers include demand differences, bidding experience, winning experience, and specific auction design parameters. Among bidders with multiunit demand, we observe, characterize, and measure what we term a modified demand reduction phenomenon spread over multiple auctions.

Aside from contributions to economics and the field of consumer behavior, an in-depth knowledge of bidding dynamics is important in many practical ways. First, understanding the factors behind changes in bidders’ WTP helps managers get better knowledge of evolving demand patterns, which in turn paves the way for efficient design of sequential auctions to maximize revenues. Second, the mechanics behind bidding behavior form the basis for developing computational simulation tools that can be used to study consumer behavior and decisions in sequential online auctions. These tools help managers with selecting optimal auction design parameters to maximize revenues. Bapna et al. (2003) develop one such approach for Yankee auctions. Third, understanding the nature of repeated visits and the evolution of WTP of these bidders will aid in the development of more effective promotional campaigns or advertising strategies through the customization of marketing efforts. Wang and Montgomery (2003) argue that because the winning price in online auctions increases with number of bidders, intense advertising campaigns to reach a larger population of buyers (Bajari and Hortaçsu 2002) are needed to increase the customer base for revenue maximization.

The rest of the paper is organized as follows. Section 2 summarizes the relevant literature on bidding behavior and sequential auctions. Section 3 presents a conceptual model and derives testable hypotheses. Section 4 overviews our data collection effort from a popular retailer site. Section 5 presents results and discussions, whereas §6 concludes with directions for future research.

## 2. Literature Review

Literature in marketing and economics argues that in a dynamic setting, consumers’ WTP changes as a consumer is able to postpone the buying decision to gain/learn more information such as market prices to reduce the risk of a bad purchase (Zhao and Kling 2004). Sequential online auctions provide a dynamic environment where a consumer can postpone his purchase and update his WTP to maximize his payoff.

Many scholars (e.g., Milgrom and Weber 1982, McAfee and Vincent 1993) have probed into issues pertaining to sequential auctions. However, much of the literature is comprised of normative models with limiting assumptions about consumer valuation and bidding behavior (e.g., assumption of bidder symmetry), and focusing on equilibrium prices considering a known number of identical items being auctioned in sequence to a group of bidders (Weber 1983, McAfee and Vincent 1993). Of particular importance to our work is the study by Jeitschko (1998). He examines how bidders with independent private values (IPV) learn about valuations of other participants in sequential auctions and investigates the impact of this information transmission and learning on their bidding behavior. Using a classical gametheoretic model for two auctions and three bidders, he concludes that participants learn about valuations of other bidders and use this information when bidding in subsequent auctions. He contends that sequential auctions exhibit two learning effects not present in static (isolated) auctions—a direct effect in which information gleaned from earlier rounds is used to formulate current bids and an anticipation effect in which bidders incorporate the impact of their earlier bids on the direct effects in future rounds.

Although the papers above addressed important issues, their assumptions about auction design do not carry over to the typical online environment. For example, in the referenced studies, repeat bidding is limited to a captive pool of bidders with a fixed number of potential bidders, whereas the online environment attracts a mix of experienced and new bidders in a noncaptive environment.

Some empirical studies have found that bidding behavior in online auctions departs from theoretical predictions (Chakraborty and Kosmopoulou 2001). Bapna et al. (2004) challenged bidders’ homogeneity assumptions of classical auction theory and showed that significant heterogeneity exists in bidders’ participatory behavior in online auctions. Bajari and Hortasçu (2003) find that bidders’ entry is endogenous to an auction, which casts doubts on exogenous determination of number of bidders in classical auction theory. Wilcox (2000) examines whether bidders’ participatory behavior in online auctions adheres to the norms of game-theoretic equilibrium prediction models. He investigates the impact of winning experience on bidding time (late or early) and number of bid revisions in a future auction. Wilcox observes that experienced bidders (those who won more than others) are more likely to bid late and do fewer bid revisions than their counterparts. This result is also supported by Roth and Ockenfels (2002). Whereas Wilcox (2000) looked at effect of winning in auctions on bidders’ participatory behavior (entry and exit time), we investigate the effect of winning on bidders’ WTP.

In the next section, we develop a conceptual model for sequential auctions bidding that focuses on the heterogeneity of bidders related to how they learn and form their WTP estimates.

## 3. Conceptual Model and Hypothesis Development

We have observed that bidders in online sequential auctions are heterogeneous with respect to their demand characteristics. The very nature of these auctions attracts both single-unit demand bidders (SU bidders hereafter) and multiunit demand bidders (MU bidders hereafter). There is also evidence that regular MU bidders in sequential auctions are themselves resellers (retailers), while SU buyers are individuals looking for bargains in these auctions (Vincent and Chanel 2007).

Ausubel and Crampton (2002) found that in multiitem isolated (nonsequential) auctions, MU bidders have incentive to reduce bids for additional items and termed this as demand reduction effect. In the sequential auctions we study, the auctioneer chooses to run many auctions with small lot sizes instead of conducting one auction with a large lot size. In this environment, MU bidders can also spread their demand over multiple auctions, thus bidding in multiple auctions to satisfy their demand in lieu of submitting “lumpy bids” (Tenorio 1999) in a single multi-item auction. This behavior supports the existence of a modified type of demand reduction phenomenon, different from the demand reduction observed in a single multi-item auction (Ausubel and Crampton 2002). In sequential auctions, where bidders can postpone their buying decision to learn more information so as to reduce the risk of a bad purchase (Zhao and Kling 2004), both SU and MU bidders have the opportunity to learn and update their WTP to maximize their surplus, but in their own different ways, with different motivations. These motivations are driven in part by heterogeneity of bidders’ participation cost, psychology, and social dynamics (Cheema et al. 2005).

In sequential auctions of identical items, bidders are likely to bid based on their observation of winning bids in the previous auctions. Studies in consumer behavior have shown that prior sale prices of an item affects the offers received in the current negotiations (Diekmann et al. 1996). Jeitschko (1998) argues that similar phenomenon exists in sequential auctions. He analytically shows a direct learning effect in sequential auctions where bidders use the information gleaned from earlier rounds to formulate their bids in current auction. Thus, one can conclude that the price information feedback can be crucially relevant for understanding bidders’ WTP in sequential auctions (Neugebauer 2004). It has been suggested that repeat bidders in sequential auctions who are considered bargain hunters (Pinker et al. 2003) factor in the prices (winning bids) from previous auctions to estimate the going price of an item in the current auction. In addition, by directly participating or monitoring auctions of interest, bidders gain important information about supply and demand in sequential auctions.

We contend that in sequential auctions, participating bidders are at different stages: some who have just started participating in these auctions and others who have observed/participated in many auctions of the same item. Because the information set of a particular bidder depends on the auctions he observed or participated in, bidders are likely to be heterogeneous in their information set. Hence, we posit that heterogeneity among online bidders in sequential auctions is not limited to the bidding strategies, as characterized by previous researchers (Bapna et al. 2004, Wilcox 2000, Roth and Ockenfels 2002). Rather, the experience they gain through participation or monitoring of multiple sequential auctions infuses heterogeneity among bidders in how they learn and update their WTP.

Wilcox (2000) showed that bidders change their bid placement strategies after winning. They start submitting fewer bid revisions and engage in late bidding in subsequent auctions. Note that Wilcox relates late bidding to the common value component. In other words, he argues that expert bidders (bidders who participate after winning in previous auctions) want to learn from other bids before placing their own bids in isolated online auctions. Along the same lines, Roth and Ockenfels (2002) also find that in isolated auctions, expert bidders do not enter until the last minute to avoid early price wars. These studies observe that bidders who have won earlier change their participation behavior (timing and revisions of bids) to maximize their payoffs. We extend this notion and examine whether winning can explain the heterogeneity in how bidders learn and update their WTP in sequential online auctions.

Figure 2 Bidding Behavior for Repeat Bidders in Sequential Online Auctions  
![](/api/attachments/9SJEPD4Q/fulltext/images/a23c07387cf042cab4cfc644eeeb1b86bcb7b8f6c67fd89293a497d459570032.jpg)

Consider an auction sequence of N auctions of identical items and bidder i who first comes for the kth auction (k < N ) at time $t _ { 1 }$ . We posit that when this bidder comes back again for the k jth auction (k j < N ) at time $t _ { 2 } ,$ he updates his WTP (see Figure 2) based on his own demand characteristics, the information he acquired during the process: winning bids and his own bids from the auctions he participated between kth and $( k + j ) \mathrm { t h } ,$ the outcome of these auctions and possibly those auctions he observed without active participation during the period $( t _ { 2 } - t _ { 1 } )$ , and the auction design parameters.

Using data that are accessible to bidders, we explore if significant heterogeneity exists in the way bidders learn and update their WTP. We use theoretically grounded measures to develop a model that characterizes bidders’ evolving adjustments to their WTP in sequential auctions (Figure 2). Similar to Jeitschko (1998), we use the term bidding behavior when referring to bidders’ updating of WTP in sequential auctions.

## 3.1. Understanding What Drives the WTP Formation

3.1.1. Demand Heterogeneity. We posit that sequential auctions provide an opportunity for both SU and MU bidders to participate in multiple auctions of identical items, and in the process, refine their bidding WTP to maximize their utility. However, SU and MU bidders are fundamentally different in their motivations. SU bidders demand at most one unit, whereas MU bidders demand multiple units. Owing to their different demand characteristics and motivations, the strategy space and consequent behavior of SU and MU bidders are likely to be different. For example, sequential auctions allow MU bidders to spread their demand over multiple auctions. Whereas both SU and MU bidders come to these liquidation auctions to find bargains, MU bidders are in general associated with resellers (Vincent and Chanel 2007).

Because the bargain-hunting motivation for participating in these auctions applies to both SU and MU bidders, one can argue that both types of bidders are exposed to a similar information-gathering process about the item for sale before participating in the first auction of an auction sequence. However, because of differences in their demand objectives, we conjecture that SU and MU bidders display different bidding behavior in how they bid in their first auction. The WTP of MU bidders is influenced by the possible rent they can realize by reselling the item in a secondary market and the type of other bidders participating in the auction (Wang 2003). This relates to a common value component. We posit that SU bidders are not constrained by a reselling price and are willing to pay a premium for the value derived from their consumption, which relates to a private value component above the common value component. Formally, we hypothesize that

Hypothesis 1 (H1). In sequential auctions, singleunit demand bidders will have a higher WTP than MU bidders in the initial auction that they participate in.

3.1.2. Experience Effect Before Winning. A study by Lohse et al. (2000) highlights heterogeneity in buyers. They categorize buyers into four different categories based on their experience levels: (1) “Never Buy,” (2) “Dropouts,” (3) “Newbies,” and (4) “Steadfast Buyers;” and reported significant differences in their buying behavior. Although buyers in auctions are price setters rather than price takers as in the study conducted by Lohse et al. (2000), there is evidence that experience brings heterogeneity among bidders in online auctions. Pinker et al. (2003) conjecture about asymmetries between experts (experienced) and novice bidders, contending that experts may have specialized knowledge about the valuation of the product. We extend their question and ask the following—Does experience experience effect explain observed heterogeneity in bidder’s learning and updating their WTP in sequential auctions?

Inexperienced bidders learn about other bidders’ values and winning bids by merely participating in or observing these auctions. Through this learning process, these bidders gain information with which update their WTP in subsequent auctions. We argue that bidders with extended experience also learn, and update their WTP. We also believe that experienced bidders are likely to change their WTP differently than those who have less information about price distribution, pattern of price history, and changing demand in these auctions.

We argue that, having seen many auctions of the same item one after another, experienced bidders are likely to have better estimates of auctioneer’s inventory, and hence are likely to devise their bidding behavior based on their estimate of future supply of items. Neugebauer and Pezanis-Christou (2007) have argued that sequential auctions create supply uncertainties, and bidder strategies are formulated on the basis of supply estimates. Furthermore, we argue that by participating in many auctions, experienced bidders can observe price trends such as declining prices (Bernhardt and Scoones 1994), which are not observable to inexperienced bidders in short term. Experienced bidders will be more informed about the supply trends and can use such information to forecast future supply. If no significant changes in demand are observed, such bidders are likely to bet on price decline in the future auctions based on fundamental principles of supply and demand. Telser (1973) argued that as consumers search more, they are better able to construct a price distribution. We also argue that bidders with more experience have more information with which construct a better winning bid distribution, which helps them update their WTP over time. Zeithammer (2002) showed that bidders take future auctions into account when bidding in current auctions. Wang (2003) also argues that in any auction, a bidder’s maximum WTP depends on others’ type (other bidders’ WTP), which introduces a common value component to the private value environment. He further claims that for two identical auctions conducted in a row (sequence), bidders’ WTP in the first auction is not equal to their true valuation. Hence, we argue that WTP of experienced bidders is different from that of inexperienced bidders.

We also aim to investigate the impact of the experience on SU and MU bidders’ WTP. To provide a comparison between SU and MU bidders, we look at this impact before the bidders’ first win. Based on analysis of eBay rare coins auctions, Kauffman and Wood (2004) suggest that bidders are likely to increase their bids after losing in the previous auction of the same item. We argue that such increase in WTP is differentiated by the bidders’ demand characteristics. MU bidders can increase their WTP to secure a first win because they have an opportunity for demand reduction (Ausubel and Crampton 2002) in future auctions of identical items. However, the increase of WTP of MU bidders will be moderated by the demand and prices in the secondary markets (common value effect). In contrast to MU bidders, SU bidders can bid higher to fulfill their demand. We posit that increase in WTP of SU bidders is higher than that of MU bidders because SU bidders are willing to pay for the value they derive from consumption, over and above the resale value of the item (private value effect). Based on these arguments, we hypothesize that

Hypothesis 2A (H2A). As an auction sequence progresses, SU bidders will increase their WTP.

Hypothesis 2B (H2B). As an auction sequence progresses, the WTP of MU bidders will also increase, but at a lower rate than SU bidders.

3.1.3. Winning Effect. Bidders, who come back after winning in previous auctions of the same item, show that they have MU demand. Wilcox (2000) showed that winning has a significant effect in changing bidders’ participatory behavior. List and Lucking-Reiley (2000) examined bidding behavior in a single MU sealed bid auction where units were identical (i.e., perfect substitutes), and found that bidders post “lumpy bids” (Tenorio 1999) with a higher bid for the first item but a lower bid for the second unit of the item. Menezes and Monteiro (1995) allow winners to participate after winning and argue that their WTP in the next auction would be less than or equal to that of first auction. Economic theory also suggests that consumers’ reservation price for the second unit of the same item decreases. After purchasing an item, a consumer will be willing to pay less for the second unit of the same item. Wilcox (2000) argues that in the context of online auctions, where similar products are repeatedly auctioned, bidders who have won in past may develop more accurate priors of the bid necessary to win the item. We argue that these bidders, who have won earlier, realize that their WTP is at the higher end of the other bidders’ WTP, are aware of winner’s curse, and are likely to reduce their

WTP in subsequent auctions to increase their surplus. Demand reduction (Ausubel and Crampton 2002) also implies that after securing one object, the bidder’s valuation for additional objects falls. Hence, we conjecture about the existence of a modified demand reduction effect over time in which successful MU bidders are likely to reduce their WTP in future auctions to realize higher surplus. We now hypothesize that:

Hypothesis 3 (H3). After winning, MU bidders decrease their WTP in subsequent auctions.

3.1.4. Marginal Effect of Winning. For MU bidders, partial satisfaction of the demand can affect their WTP. We argue that sequential online auctions present a unique opportunity, compared to isolated online auctions or sealed bid auction, to access the demand and supply of the item. MU bidders can avail this opportunity and spread their demand over multiple auctions while observing market demand that reinforces the modified demand reduction phenomenon, unique to sequential online auctions environment. Hence, we argue that MU bidders who come back after winning may update their WTP differently from those MU bidders who are new to the auction sequence or have previously participated in the sequence but have not won. Wilcox (2000) measured bidders experience as number of wins and showed that number of wins affect bidders’ participation behavior. We extend that investigation and ask if the number of wins also affects how bidders update their WTP. We aim to investigate the marginal effect of each win. Do bidders change their bidding behavior with multiple wins or do they remain consistent irrespective of their wins? The modified demand reduction argument also points to possible WTP decrease in the sequential auction environment, where MU bidders spread their demand fulfillment over several auctions. We set out to test this modified demand reduction phenomenon by testing the following hypothesis.

Hypothesis 4 (H4). After each additional win, MU bidders further reduce their WTP in subsequent auction.

## 3.2. Impact of Auction Design Parameters on WTP Formation

So far, we have developed hypotheses to test the impact of winning and experience on bidders’ WTP in sequential auctions. We now examine the effect of auction design parameters on bidders’ bidding behavior. Articles in trade journals and popular press have pointed out that retailers resort to sequential auctions when they have a large inventory to clear off. Retailers may want to sell off their inventory as quickly as possible to hedge against possible decline in demand over time for various reasons. Selling these items quickly also reduces the holding cost of this inventory. To achieve this objective, the following two auction design parameters are relevant (Pinker et al. 2003): lot size and auction duration. For example, a higher lot size and smaller auction duration may expedite the inventory clearance, but may also signal declining demand, which may decrease bidders’ WTP. From the auctioneer’s revenue point of view, it is important to determine the impact of these auction design parameters on bidders’ learning and updating their WTP.

In this research we investigate the impact of the lot size on the WTPs of the participants. A reduction in winning bid as a function of the decrease of bidders’ WTP with the lot size may impact the profits for the auctioneer when other factors such as holding costs and demand uncertainty are taken into account. In sequential auctions, where bidders learn from publicly available information and update their WTP in subsequent auctions, the seller’s decision to change auction offerings (such as changing the lot size offered) may also affect bidders’ WTP in future auctions. It has been observed that sequential auctions with equal-sized lots generate higher revenues than those with varying lot sizes (Ginsburgh and van Ours 2007). Although we underscore the significance of this finding, note that there are significant differences between the formats of the auctions studied by Ginsburgh and van Ours (2007) and the online ascending price auctions that we study. We also conjecture that the seller’s decision to increase lot size in any auction might be interpreted by repeat bidders as a signal for possible declining demand and a desire to dispose of the remaining inventory rapidly. The signal of declining demand may affect MU bidders more severely than SU bidders because it affects prices in their secondary market. We argue that as the auctioneer increases lot size, the repeat bidders are likely to reduce their bid. Hence, bidders in sequential auctions are likely to reduce their WTP in an attempt to strike significant bargains on these items. Formally,

Hypothesis 5A (H5A). WTP of SU bidders will decrease with an increase in the lot size.

Hypothesis 5B (H5B). WTP of MU bidders will decrease at a faster rate than that of SU bidders, with an increase in the lot size.

Online auctions provide a noncaptive forum for bidders. This is a marked difference between online auctions and their traditional counterparts. To capitalize on this feature, online auctions are designed to run for a longer duration. A longer auction duration is likely to increase the number of participating bidders (Pinker et al. 2003), which may lead to higher profits. Lucking-Reiley et al. (2000) and Reiley et al. (2007) found evidence in coin auctions on eBay that longer auctions lead to higher prices, yet they argue that there are costs associated with longer auction duration. Scholars argue that Internet auctions typically take longer than traditional auctions and hence present a different bidding-cost structure that needs to be taken into consideration in design of online auctions. We investigate the effect of auction duration on bidders’ WTP in sequential auctions.

We contend that a repeat bidder facing an auction with longer duration than previous ones he participated in will associate it with higher monitoring costs and will adjust his WTP accordingly. Thus, we argue that their WTP is likely to decrease with auction duration. Formally,

Hypothesis 6 (H6). The WTP of both SU and MU bidders will decrease with an increase in auction duration.

## 4. Method

## 4.1. Data Collection

The data used in this study was collected from Sam’s club auctions (http://auctions.samsclub.com/), where bidder registration and validation are mandatory to participate. This allows us to track and relate unique bidders and their bidding patterns across multiple auctions. Furthermore, by using data from Sam’s Club auctions, we controlled for the sellers’ reputation because all the items are sold by the same seller. In other words, the impact that trust in the seller could have (Ba and Pavlou 2002) is removed.

Samsclub.com conducts open ascending uniform price auctions. In uniform price auctions, multiple units of the same item can be offered in a single auction, and all the winners pay the same price. This price is equal to the marginal bid, defined as the lowest winning bid. The auction format used by Samsclub.com is open in that bidders can observe the bids of their competing bidders, and they can enter the auction at any stage of the auction. Bid submission is governed by the minimum bid increment rule, which stipulates the minimum amount by which new bids are required to exceed the existing minimum winning bid. Thus, the auction price progressively ascends during the auction.

We programmed an automated agent that periodically (every 10 minutes) downloaded bidding activity from the Sam’s Club auction website, and recorded the bidding activity in a database. Our agent downloaded HTML data that was parsed using a back-end parsing module. We compiled a data set of about 30 items consisting of electronics and hardware products. Samsclub.com conducted multiple auctions for the same item one after another in what we define as an auction sequence. The number of auctions in a sequence varied because of the number of units in stock for each item. We use only auction sequences that began and concluded within our data collection period. Summary statistics of the data are reported in Table 1.

As expected, bidders participate in many auction sequences for different items. For each bidder, we retain the participation records for only one auction sequence. For example, if a bidder participated in 10 auctions for a VCR and 8 auctions for a digital camera, we randomly picked one out of these two auction sequences (10 auctions for VCR or 8 auctions for digital camera) for each bidder. Furthermore, to avoid potential bias in results, we filtered our data set and retained only those bidders who placed at least one serious<sup>4</sup> bid in all the auctions in which they participated (Bapna et al. 2004). On average, as shown in Figure 1, the proportion of repeat bidders in any auction was about 30%–40% of total number of bidders, which underscores the fact that sequential auctions attract a significant number of repeat bidders.

Table 1 Overall Summary Statistics of the Data Set

<table><tr><td>Statistic</td><td>Value</td></tr><tr><td>Total number of different products sold</td><td>29</td></tr><tr><td>Average number of auctions per product</td><td>72.9</td></tr><tr><td>Average number of bidders per auction</td><td>12.34</td></tr><tr><td>Average lot size per auction</td><td>1.75</td></tr><tr><td>Total number of unique bidders</td><td>774</td></tr><tr><td>Average number of auctions in which a bidder participated</td><td>5.3</td></tr></table>

This analysis is ex post, and bidders are placed in categories based on their bidding behavior in all the auctions in which they participated. In our setting, for an auction sequence that entails 100 (say) auctions, the winning bids in these auctions represent the path of equilibrium prices over time. We categorized bidders as SU (single-unit demand) or MU (multiunit demand) based on their revealed demand related to these equilibrium prices. Bidders who bid for at most one unit and drop out of the auction sequence after winning are categorized as single-unit (SU) demand bidders. Bidders who continue participating in the sequence after winning reveal their demand for multiple units, and are thus multiunit (MU) demand bidders. Because it is an ex post analysis, a bidder who, for example, comes for 20 auctions of identical items, wins in the 10th auction, and continues to bid in subsequent auctions after winning is categorized as MU in his very first auction when he hasn’t won yet. We are confident that by carefully analyzing exhibited behavior of serious repeat bidders over relatively long sequences in an ex post fashion, we can operationalize the classification of bidders according to their displayed demands.

## 4.2. Measures

Following previous research, we assume that a bidder’s maximum bid in any auction represents his WTP in that auction and bidders’ WTP bounds their valuations from below (Bapna et al. 2008, Jeitschko 1998). However, like these researchers, we also recognize that the winner’s bid does not represent an adequate estimate for the winners’ WTP. Consequently, our analysis of WTP formation focuses on the maximum (nonwinning) bids by each bidder.

We collect data at the bidder level. For each bidder, we track all the auctions in a sequence in which he or she participated. Consider a bidder i who participates in a total of J auctions. Then, for the jth auction $( j \in J )$ in this bidder’s sequence, we record the following variables: the bidder’s final bid $( B i d _ { i j } ) _ { , }$ , bidding time $( B i d d i n g T i m e _ { i j } ) _ { , }$ , auction duration $( A u c t i o n D u r a t i o n _ { i j } ) .$ lot size $( L o t S i z e _ { i j } ) _ { . }$ , total number of bidders $( N B _ { i j } ) ,$ , and the winning bid $( P _ { i j } )$ . In our data analysis, we normalize bids using the bidder’s maximum WTP across all the auctions in which he participated, and scale them on a 0–10 scale. Normalized bids are computed as Normalize $l B i d _ { i j } = ( B i d _ { i j } / M a x B i d _ { i } ) * 1 0$ , where $M a x B i d _ { i } = \operatorname* { m a x } ( B i d _ { i 1 } , B i \dot { d } _ { i 2 } , \dots , B i d _ { i J } )$

Online buying behavior and the importance of buyer learning during shopping time is highlighted by Leornard (2005), who shows that although the number of times that an online shopper abandons a shopping cart before the actual purchase is important in studying online buying behavior, the overall time spent shopping has a significant impact on the final purchase decision that a buyer makes. Although Leornard’s study is based on a fixed-price mercantile process, we can draw support from it to consider time elapsed since first auction participation to measure bidders’ experience. We define a variable to capture the passage of time in our model as $T i m e _ { i j } =$ $B i d d i n g T i m e _ { i j } - B i d d i n g T i m e _ { i 1 } .$ In essence, $T i m e _ { i j }$ measures the experience level of a bidder i in the jth auction. The higher the value of $T i m e _ { i j } ,$ the longer time a bidder had for learning (by direct participation and observing other auctions) and thus, more experience. $T i m e _ { i j }$ is measured in days.<sup>5</sup>

We hypothesized that a larger lot size in an auction provides more information on supply and demand of the item being auctioned and thus is likely to influence bidders’ WTP. Considering unit lot size as the base case, we defined a variable $C L o t S i z e _ { i j } ,$ computed as $C L o t S i z e _ { i j } = ( L o t S i z e _ { i j } - 1 )$ , and intended to capture the effect of larger lot sizes on WTP.

Auctions with longer duration are likely to pose a higher participation cost on bidders, and hence it seems intuitive that variation in auction duration may affect bidders’ WTP. Auction durations in our data set varied widely. In our model, we investigate the effect of auction duration on change in bidders’ WTP over time. The variable $A u c t i o n D u r a t i o n _ { i j }$ captures the auction duration of the jth auction participated in by the ith bidder.

Literature on consumer behavior has shown that prevailing market prices (Zhao and Kling 2004) influence the formation of consumers’ WTP. We capture the bidder’s knowledge of the prevailing market prices (prevailing winning bids) by the minimum of all winning bids in the auctions in which he participated. We argue that repeat bidders are likely to use $P _ { i j } ^ { \mathrm { m i r } }$ defined as $P _ { i j } ^ { \operatorname* { m i n } } = \operatorname* { m i n } ( P _ { i 1 } , P _ { i 2 } , \dots , P _ { i j - 1 } )$ as a reference price when they form their own WTP. To capture the effect of $P _ { i j } ^ { \mathrm { m i n } }$ relative to their previous bid, we define Minimu $m \dot { W } i n B i d _ { i j } = 1 i f ( P _ { i j - 1 } ^ { \mathrm { m i n } } > B i d _ { i j - 1 } ) $ 0 otherwise.

Our data set has auction sequences of different products to make sure that the observed differences in WTP trajectories of SU and MU bidders are not because of the nature of the product sold in the sequential auctions, we control for product heterogeneity. We categorize our products in two categories—electronic and nonelectronic products, and define a control variable ProductCategory.

## 5. Analysis and Results

5.1. Measuring Experience Effect Before Winning The first analysis we present uses bids from SU and MU bidders before they win in any auction. Because bidders’ WTP is measured over time, the error terms for bidders are likely to be autocorrelated and heteroscedastic, not independent as required by traditional OLS regressions. To address the research questions at hand with the issues presented by the longitudinal data set, we opted to use a multilevel longitudinal modeling approach (Rogosa and Willett 1985, Singer 1998, Singer and Willett 2003).

In our case, we have two levels. Level 1, also known as the individual growth model with random coefficients, models the WTP evolution at the individual level. It models within-person changes and is intended to address the question of how each bidder’s WTP change over time as he/she participates in sequential auctions of identical items. Level 2 models the differences in trajectories (the random coefficients) between

SU and MU bidders. To categorize a bidder i based on his demand, we define a variable IndividualDemand and set it to zero for SU bidders and one for MU bidders. Our level 1 model is as follows:

$$
\begin{array}{r l} \text { NormalizedBid } _ {i j} & = \pi_ {0 i} + \pi_ {1 i} \text { Time } _ {i j} + \pi_ {2 i} \text { AuctionDuration } _ {i j} \\ & + \pi_ {3 i} \text { CLotSize } _ {i j} + \pi_ {4 i} \text { MinimumWinBid } _ {i j} \\ & + \pi_ {5 i} \text { ProductCategory } _ {i j} + \varepsilon_ {i j}. \end{array} \tag {1a}
$$

The random coefficients  not only depend on population mean and residual, but may also depend on each bidders’ IndividualDemand. The level 2 sub models, which relate the random coefficients to the demand variable, are given as—

$$
\pi_ {0 i} = \gamma_ {0 0} + \gamma_ {0 1} I n d i v i d u a l D e m a n d _ {i} + \zeta_ {0 i}\tag{1b}
$$

$$
\pi_ {1 i} = \gamma_ {1 0} + \gamma_ {1 1} I n d i v i d u a l D e m a n d _ {i} + \zeta_ {1 i}\tag{1c}
$$

$$
\pi_ {2 i} = \gamma_ {2 0} + \zeta_ {2 i}\tag{1d}
$$

$$
\pi_ {3 i} = \gamma_ {3 0} + \gamma_ {3 1} I n d i v i d u a l D e m a n d _ {i}\tag{1e}
$$

$$
\pi_ {4 i} = \gamma_ {4 0}\tag{1f}
$$

$$
\pi_ {5 i} = \gamma_ {5 0},\tag{1g}
$$

where $\varepsilon _ { i j } \sim N ( 0 , \sigma _ { \varepsilon } ^ { 2 } )$ and

$$
\left[ \begin{array}{c} \zeta_ {0 i} \\ \zeta_ {1 i} \\ \zeta_ {2 i} \end{array} \right] \sim N \left(\left[ \begin{array}{c} 0 \\ 0 \\ 0 \end{array} \right], \left[ \begin{array}{c c c} \sigma_ {0} ^ {2} & \sigma_ {0 1} ^ {2} & \sigma_ {0 2} ^ {2} \\ \sigma_ {1 0} ^ {2} & \sigma_ {1} ^ {2} & \sigma_ {1 2} ^ {2} \\ \sigma_ {2 0} ^ {2} & \sigma_ {2} ^ {2} & \sigma_ {2 2} ^ {2} \end{array} \right]\right).
$$

It is not necessary for each level 2 sub model to have both fixed and random effects. Note that for some of the parameters, we consider only fixed effects and no random effects. Additional residual terms increase the size of the covariance matrix and make the estimation of the model more challenging with available data, which is a limitation to this study.

Because we were unable to include all the random effects in our model, when trying different combinations to achieve numerical stability, we choose the random effects that can help us better explain evolution of bidders’ WTP over time and effect of auction design parameters on bidders’ WTP. Following our conceptual model, we chose the random effects for Time, which is a measure for bidders’ experience, and for AuctionDuration, which is an auction design parameter. Furthermore, a model with fewer random effects provides a more parsimonious representation and clearer substantive insights. In level 2, we chose to investigate the effect of the demand on the intercept (WTP in very first auction), and the coefficients (trajectories) associated with experience and lot size.

For estimation purposes, we now present our composite model (collapsing level 1 and level 2) of bidders’ WTP in sequential auctions.

NormalizedBid<sub>ij</sub>

$$
\begin{array}{l} = \gamma_ {0 0} + \gamma_ {0 1} I n d i v i d u a l D e m a n d _ {i} + \gamma_ {1 0} T i m e _ {i j} \\ \quad + \gamma_ {2 0} A u c t i o n D u r a t i o n _ {i j} + \gamma_ {3 0} C L o t S i z e _ {i j} \\ \quad + \gamma_ {1 1} (I n d i v i d u a l D e m a n d _ {i} \times T i m e _ {i j}) \\ \quad + \gamma_ {3 1} (I n d i v i d u a l D e m a n d _ {i} \times C L o t S i z e _ {i j}) \end{array}
$$

$$
+ \gamma_ {4 0} \text { MinimumWinBid } _ {i j} + \gamma_ {5 0} \text { ProductCategory } _ {i j}
$$

$$
+ \left[ \zeta_ {0 i} + \zeta_ {1 i} \text { Time } _ {i j} + \zeta_ {2 i} \text { AuctionDuration } _ {i j} + \varepsilon_ {i j} \right]\tag{1h}
$$

The above composite multilevel model can also be viewed as a mixed-effects model (Frees 2006, Singer 1998), and such a model can be estimated with GLS (generalized least squares) or maximum likelihood estimation method. Following Singer (1998), we opted to use SAS PROC MIXED, which uses maximum likelihood estimation method to estimate parameters. Maximum likelihood estimates are sometimes preferred because even without normality assumption, they are unbiased, efficient, and asymptotically normal with known variance (Singer 1998, Frees 2006).

In multilevel models, multicollinearity occurs when at least one eigenvector is negative in the correlation matrix of the predictor variables. In our analysis, we found that none of the eigenvectors were negative, which gave us confidence that our model doesn’t suffer from multicollinearity problems.

We first estimate the full model (Model A) as in Equation (1h) and then drop the insignificant terms of Model A and estimate Model B. Results of both models are shown in Table 2. Standard error values of the parameter estimates are reported in parentheses. Our results are robust, because we see that parameter estimates do not change from Model A to Model B. To test the goodness of the fit of our models, we report deviance, AIC, and BIC statistics. Lower values of AIC and BIC statistics mean a better fit for the model. Significance of fixed and random effects are also indicated in Table 2. Note that $\gamma _ { 0 0 }$ is the population average of level 1 parameter $\pi _ { 0 i }$ for SU bidders. Similarly, $\gamma _ { 0 0 } + \gamma _ { 0 1 }$ is the population average of level 1 parameter $\pi _ { 0 i }$ for MU bidders, and so on.

Table 2 SU and MU Bidders Before Win

<table><tr><td></td><td></td><td colspan="2">Model A</td><td colspan="2">Model B</td></tr><tr><td colspan="6">Fixed effects</td></tr><tr><td>Intercept</td><td> $\gamma_{00}$ </td><td>8.12***</td><td>(0.19+)</td><td>7.93***</td><td>(0.12)</td></tr><tr><td>Individual demand</td><td> $\gamma_{01}$ </td><td>-0.20</td><td>(0.22)</td><td></td><td></td></tr><tr><td>Time</td><td> $\gamma_{10}$ </td><td>0.043***</td><td>(0.01)</td><td>0.048***</td><td>(0.01)</td></tr><tr><td>AuctionDuration</td><td> $\gamma_{20}$ </td><td>-0.0005</td><td>(0.007)</td><td></td><td></td></tr><tr><td>Individual demand × Time</td><td> $\gamma_{11}$ </td><td>-0.032~</td><td>(0.018)</td><td>-0.0387*</td><td>(0.019)</td></tr><tr><td>CLotSize</td><td> $\gamma_{30}$ </td><td>-0.030</td><td>(0.03)</td><td></td><td></td></tr><tr><td>CLotSize × Individual demand</td><td> $\gamma_{31}$ </td><td>-0.13*</td><td>(0.05)</td><td>-0.16**</td><td>(0.05)</td></tr><tr><td>Minimum win bid</td><td> $\gamma_{40}$ </td><td>0.23*</td><td>(0.10)</td><td>0.23*</td><td>(0.10)</td></tr><tr><td>Product category</td><td> $\gamma_{50}$ </td><td>-0.16</td><td>(0.20)</td><td></td><td></td></tr><tr><td colspan="6">Variance components</td></tr><tr><td>Within-person</td><td> $\sigma_{\varepsilon}^{2}$ </td><td>1.99***</td><td>(0.12)</td><td>1.96***</td><td>(0.12)</td></tr><tr><td>In intercept</td><td> $\sigma_{0}^{2}$ </td><td>1.84***</td><td>(0.46)</td><td>2.40***</td><td>(0.30)</td></tr><tr><td>Variance for  $\zeta_{1i}$ </td><td> $\sigma_{1}^{2}$ </td><td>0.004*</td><td>(0.002)</td><td>0.006**</td><td>(0.002)</td></tr><tr><td>Covariance component</td><td> $\sigma_{01}$ </td><td>-0.059*</td><td>(0.03)</td><td>-0.07**</td><td>(0.02)</td></tr><tr><td>Variance for  $\zeta_{2i}$ </td><td> $\sigma_{2}^{2}$ </td><td>0.0001</td><td>(0.0004)</td><td></td><td></td></tr><tr><td>Covariance component</td><td> $\sigma_{20}$ </td><td>-0.02</td><td>(0.01)</td><td></td><td></td></tr><tr><td>Covariance component</td><td> $\sigma_{21}$ </td><td>-0.0002</td><td>(0.0007)</td><td></td><td></td></tr><tr><td colspan="6">Goodness-of-fit</td></tr><tr><td>Deviance</td><td></td><td>3,963.1</td><td></td><td>3,966.9</td><td></td></tr><tr><td>AIC (smaller is better)</td><td></td><td>3,995.1</td><td></td><td>3,984.9</td><td></td></tr><tr><td>BIC (smaller is better)</td><td></td><td>4,052.7</td><td></td><td>4,017.2</td><td></td></tr><tr><td colspan="6">Null model likelihood ratio test</td></tr><tr><td>Chi-square</td><td></td><td>277.86***</td><td></td><td>283.38***</td><td></td></tr></table>

∼p < 01; ∗p < 005; ∗∗p < 001; ∗∗∗p < 0001. +Standard error.

From our model, assuming unit lot-size auctions and a zero MinimumWinBid, the population averages of intercept and slope for SU bidders are <sub>00</sub>, <sub>10</sub>, respectively, and for MU bidders $\gamma _ { 0 0 } + \gamma _ { 0 1 } , \gamma _ { 1 0 } + \gamma _ { 1 1 } ,$ respectively. Note that some of the level 1 growth parameters have their own residual $( \mathrm { e . g . } , \zeta _ { 0 i }$ for $\pi _ { 0 i } )$ and this permits $\pi _ { 0 1 }$ of bidder 1 to differ stochastically from $\pi _ { 0 1 }$ of bidder 2. The residuals in the level 2 model $( \mathrm { e . g . } , \ \zeta _ { 0 i }$ for $\pi _ { 0 i }$ and $\zeta _ { 1 i }$ for $\pi _ { 1 i } )$ represent the unexplained part of individual growth parameters. We report the population variance and covariance of the residuals in Table 2. For example, $\sigma _ { 0 0 } ^ { 2 } , \sigma _ { 0 1 } ,$ and $\sigma _ { 1 } ^ { 2 }$ measure the population variance and covariance of residuals $\zeta _ { 0 i }$ and $\zeta _ { 1 i }$

The model results show that the slopes of WTP trajectories of SU and MU bidders are different (see

Figure 3 WTP of Bidders Over Time  
![](/api/attachments/9SJEPD4Q/fulltext/images/ed1c2982d69c85c0733d02f7a9324ea25cc2b6c281393274b8326ad0d0225e08.jpg)  
Figure 3), which supports Hypotheses H2A and H2B. Our findings show that SU and MU bidders are different in how they update their WTP over time in sequential auctions. We also find that the initial bid (bid in the first auction in which participated) of SU bidders is not significantly different from MU bidders; thus, our Hypothesis H1 is not supported.

To illustrate the findings of our analysis, in Figure 3 we plot expression (1h) of Model B, assuming zero MinimumWinBid and unit lot-size auctions for SU and MU bidders. We want to emphasize that the plots in Figure 3 are for population averages. WTP trajectory for individual bidders can be estimated by taking the residuals into account. In the figure we represent the relationship between bidders’ WTP, measured through their normalized bids, and their acquired experience measured by the time since first participation in an auction sequence for identical items. There are two plots for MU bidders: one for participants in auctions of lot size one, and the other (LS2) for participants in auctions of lot size two. Our results show that all the bidders change their WTP as they gain experience, which supports our Hypothesis H2. We observe that SU bidders don’t differ from MU bidders in their initial WTP estimate, but as bidders gain experience, their WTP follow different trajectories. Both SU and MU bidders increase their WTP with SU bidders increasing at a faster rate than MU bidders. These results support our Hypotheses H2A and H2B.

We find that SU bidders, who demand at most one item, do not decrease their WTP in larger lot-size auctions, which increases their likelihood of winning. This result also relates to H2A. Because SU bidders increase their WTP faster to secure a win, they do not want to lower their WTP when lot size is higher. MU bidders are willing to pay less in auctions of larger lot sizes. These bidders are likely to be resellers and may consider a larger lot size as a signal for higher inventory of the item. We learn from our model that the change in lot size affects WTP only of MU bidders.

We have reported random effects of the model in Table 2. $\sigma _ { 0 } ^ { 2 }$ represents the population residual variance in true initial bid estimate. We observe that a high value of $\sigma _ { 0 } ^ { 2 }$ represents bidders’ heterogeneity at the beginning, whereas a small $\sigma _ { 1 } ^ { 2 }$ explains that the slope of the WTP trajectories (learning over time) does not differ much across bidders, i.e., they do not differ much in how they change their WTP over time as they gain experience. $\sigma _ { 0 1 }$ summarizes the magnitude and direction of the association between true initial bid (bid in the first auction) and true rate of change in WTP after controlling for other predictors. Statistically significant negative value of $\sigma _ { 0 1 }$ explains that bidders with weaker initial WTP improve at a faster rate, on average, than others. We find that bidders who begin with low bids in their early auctions have higher chances of winning in later auctions as they gain experience. It is true that some bidders may not win even after increasing their WTP over time. Therefore, an interesting future research would be to investigate when and why bidders drop off from these sequential online auctions before they win.

Lot-size effect was not significant for SU bidders, and Hypothesis H5A is not supported. However, the results in Table 2 show that for a unit increase in lot size, WTP of MU bidders reduces by 16%, offering support to H5B. Because transaction costs in online markets are extremely low, it has been shown that individuals and small resellers often buy items at a discount from big retailers to sell them in secondary markets (Gopal et al. 2006). Gopal et al. (2006) show that increased supply of items from retailers has an adverse affect on prices these items can fetch in secondary markets. We argue that MU bidders, who are likely to be resellers, are more sensitive to the impact of increased supply on resale prices, and thus are willing to pay less.

We observe that effect of the lot size on WTP doesn’t change with bidders’ experience. We also find that minimum winning bid observed by the bidders in the previous auctions they participated, affects their WTP.

This supports the argument that lowest price observed in previous auctions serves as a reference price. A reference price is a price that consumers are assumed to form in their minds as a result of experience (Krishnamurthi et al. 1992). Prices above the reference price are perceived as losses and prices below the reference price are perceived as gains (Krishnamurthi et al. 1992). Because bidders in sequential auctions are bargain hunters, they are likely to use their reference price to calibrate their WTP.

An interesting observation from the results in Table 2 is that auction duration does not affect bidders’ WTP significantly. Hence, Hypothesis H6 is not supported. A closer look provides a possible explanation for this finding. Bapna et al. (2004) find that in online auctions, a majority of the bidders arrive at the beginning (Early Evaluators) or at the end (Opportunist) of the auction, and only a small fraction of bidders stay from beginning to end (Participators) of the auction. Because, most bidders do not stay from beginning to end of the auctions, increase in auction duration does not increase participation cost, and hence, it does not affect bidders’ WTP.

## 5.2. Measuring Winning Effect: A Modified Demand Reduction

Our first model validated that experience has a significant effect on both SU and MU bidders’ WTP in sequential auctions. It also showed that SU and MU bidders differ in how their WTP changes over time, before their first win. Next, we investigate if winning in sequential auctions affects bidders’ WTP in subsequent auctions. For this, we now focus only on MU bidders because they come back after winning, whereas SU bidders do not. The sample we use for this analysis consists of 221 MU bidders who have won at least once.

Most MU bidders remain unsuccessful in the first few auctions in which they participate. We first investigate whether there is any significant difference in bidding behavior of these successful and unsuccessful bidders, or in other words, whether an MU bidder’s first win makes any significant change in WTP trajectory over time. Many MU bidders win in multiple auctions and so we also investigate if each subsequent win has an effect on their WTP. We are basically verifying the existence of the demand reduction phenomenon spread over several sequential auctions. To measure such effects, we now define two variables WinningStatus and CumulativeNumberOfWins . WinningStatus for a bidder i is zero before win, becomes one after bidder clocks his first win, and remains one thereafter. CumulativeNumberOfWins shows the total number of wins for a bidder i in 1 to $j - 1$ auctions. It helps us measure the marginal impact of each win on change in WTP over time. We now propose our multilevel model for MU bidders. Our level 1 model is as follows:

$$
\begin{array}{l} = \pi_ {0 i} + \pi_ {1 i} \text { Time } _ {i j} + \pi_ {2 i} \text { CLotSize } _ {i j} + \pi_ {3 i} \text { WinningStatus } _ {i j} \\ \quad + \pi_ {4 i} \text { CumulativeNumberOfWins } _ {i j} \\ \quad + \pi_ {5 i} (\text { CLotSize } _ {i j} \times \text { Time } _ {i j}) \\ \quad + \pi_ {6 i} (\text { WinningStatus } _ {i j} \times \text { Time } _ {i j}) \\ \quad + \pi_ {7 i} \text { AuctionDuration } _ {i j} + \varepsilon_ {i j}. \end{array} \tag {2a}
$$

And our level 2 submodels are given as

$$
\pi_ {0 i} = \gamma_ {0 0} + \zeta_ {0 i}\tag{2b}
$$

$$
\pi_ {1 i} = \gamma_ {1 0} + \zeta_ {1 i}\tag{2c}
$$

$$
\pi_ {2 i} = \gamma_ {2 0} + \zeta_ {2 i}\tag{2d}
$$

$$
\pi_ {3 i} = \gamma_ {3 0} + \zeta_ {3 i}\tag{2e}
$$

$$
\pi_ {4 i} = \gamma_ {4 0}\tag{2f}
$$

$$
\pi_ {5 i} = \gamma_ {5 0}\tag{2g}
$$

$$
\pi_ {6 i} = \gamma_ {6 0}\tag{2h}
$$

$$
\pi_ {7 i} = \gamma_ {7 0},\tag{2i}
$$

where $\varepsilon _ { i j } \sim N ( 0 , \sigma _ { \varepsilon } ^ { 2 } )$ and

$$
\left[ \begin{array}{c} \zeta_ {0 i} \\ \zeta_ {1 i} \\ \zeta_ {2 i} \\ \zeta_ {3 i} \end{array} \right] \sim N \left(\left[ \begin{array}{c} 0 \\ 0 \\ 0 \\ 0 \end{array} \right], \left[ \begin{array}{c c c c} \sigma_ {0} ^ {2} & \sigma_ {0 1} & \sigma_ {0 2} & \sigma_ {0 3} \\ \sigma_ {1 0} & \sigma_ {1} ^ {2} & \sigma_ {1 2} & \sigma_ {1 3} \\ \sigma_ {2 0} & \sigma_ {2 1} & \sigma_ {2} ^ {2} & \sigma_ {2 3} \\ \sigma_ {3 0} & \sigma_ {3 1} & \sigma_ {3 2} & \sigma_ {3} ^ {2} \end{array} \right]\right).
$$

Combining level 1 and 2 models results in our composite model, given as

$$
\begin{array}{l} \text {NormalizedBid} _ {i j} \\ = \gamma_ {0 0} + \gamma_ {1 0} \text {Time} _ {i j} + \gamma_ {2 0} \text {CLotSize} _ {i j} + \gamma_ {3 0} \text {WinningStatus} _ {i j} \end{array}
$$

$$
\begin{array}{l} + \gamma_ {4 0} C u m u l a t i v e N u m b e r O f W i n s _ {i j} \\ + \gamma_ {5 0} (C L o t S i z e _ {i j} \times T i m e _ {i j}) \\ + \gamma_ {6 0} (W i n n i n g S t a t u s _ {i j} \times T i m e _ {i j}) \\ + \gamma_ {7 0} A u c t i o n D u r a t i o n _ {i j} + [ \zeta_ {0 i} + \zeta_ {1 i} T i m e _ {i j} \\ \quad + \zeta_ {2 i} C L o t S i z e _ {i j} + \zeta_ {3 i} W i n n i n g S t a t u s _ {i j} + \varepsilon_ {i j} ]. \end{array}\tag{2j}
$$

Similar to the previous model, here we do not consider random effects for all the parameters in the level 1 model to keep the model more parsimonious and estimable with the available data. This model was also estimated with full maximum likelihood method in SAS. The results are shown in Table 3.

For the purpose of illustrating key findings from model (2j) and the associated results in Table 3, we show in Figure 4 the evolution of WTP for successful MU bidders. As in Figure 3, we plot the results assuming unit lot-size auctions for MU bidders. Again, we caution that this plot represents average

## Table 3 MU Bidders

<table><tr><td></td><td colspan="3">Model A</td><td colspan="2">Model B</td></tr><tr><td colspan="6">Fixed effects</td></tr><tr><td>Intercept</td><td> $\gamma_{00}$ </td><td>8.10***</td><td>(0.15)</td><td>8.06***</td><td>(0.11)</td></tr><tr><td>Time</td><td> $\gamma_{10}$ </td><td>0.017*</td><td>(0.007)</td><td>0.018*</td><td>(0.008)</td></tr><tr><td>CLotSize</td><td> $\gamma_{20}$ </td><td>-0.10**</td><td>(0.03)</td><td>-0.12***</td><td>(0.03)</td></tr><tr><td>Winning status</td><td> $\gamma_{30}$ </td><td>-0.24</td><td>(0.21)</td><td></td><td></td></tr><tr><td>Cumulative number of wins</td><td> $\gamma_{40}$ </td><td>-0.188**</td><td>(0.06)</td><td>-0.188**</td><td>(0.06)</td></tr><tr><td>CLotSize × Time</td><td> $\gamma_{50}$ </td><td>-0.001</td><td>(0.001)</td><td></td><td></td></tr><tr><td>Winning status × Time</td><td> $\gamma_{60}$ </td><td>-0.028**</td><td>(0.009)</td><td>-0.033***</td><td>(0.009)</td></tr><tr><td>AuctionDuration</td><td> $\gamma_{70}$ </td><td>0.004</td><td>(0.006)</td><td></td><td></td></tr><tr><td colspan="6">Variance components</td></tr><tr><td>Within-person</td><td> $\sigma_{\varepsilon}^{2}$ </td><td>1.63***</td><td>(0.09)</td><td>1.63***</td><td>(0.09)</td></tr><tr><td>In intercept</td><td> $\sigma_{0}^{2}$ </td><td>2.36***</td><td>(0.39)</td><td>2.34***</td><td>(0.39)</td></tr><tr><td>Variance for  $\zeta_{1i}$ </td><td> $\sigma_{1}^{2}$ </td><td>0.001**</td><td>(0.0005)</td><td>0.001**</td><td>(0.00)</td></tr><tr><td>Covariance component</td><td> $\sigma_{01}$ </td><td>-0.03</td><td>(0.01)</td><td>-0.026</td><td>(0.01)</td></tr><tr><td>Variance for  $\zeta_{2i}$ </td><td> $\sigma_{2}^{2}$ </td><td>0.008</td><td>(0.008)</td><td>0.009</td><td>(0.008)</td></tr><tr><td>Covariance component</td><td> $\sigma_{20}$ </td><td>-0.02</td><td>(0.08)</td><td>-0.011</td><td>(0.09)</td></tr><tr><td>Covariance component</td><td> $\sigma_{21}$ </td><td>0.0014</td><td>(0.003)</td><td>0.0008</td><td>(0.003)</td></tr><tr><td>Variance for  $\zeta_{3i}$ </td><td> $\sigma_{3}^{2}$ </td><td>4.36***</td><td>(0.88)</td><td>4.35***</td><td>(0.87)</td></tr><tr><td>Covariance component</td><td> $\sigma_{30}$ </td><td>-1.75***</td><td>(0.51)</td><td>-1.75***</td><td>(0.50)</td></tr><tr><td>Covariance component</td><td> $\sigma_{31}$ </td><td>-0.008</td><td>(0.02)</td><td>-0.009</td><td>(0.02)</td></tr><tr><td>Covariance component</td><td> $\sigma_{32}$ </td><td>0.045</td><td>(0.09)</td><td>0.06</td><td>(0.10)</td></tr><tr><td colspan="6">Goodness-of-fit</td></tr><tr><td>Deviance</td><td></td><td>4,516.5</td><td></td><td>4,518.8</td><td></td></tr><tr><td>AIC (smaller is better)</td><td></td><td>4,554.5</td><td></td><td>4,550.8</td><td></td></tr><tr><td>BIC (smaller is better)</td><td></td><td>4,618.0</td><td></td><td>4,605.2</td><td></td></tr><tr><td colspan="6">Null model likelihood ratio test</td></tr><tr><td>Chi-square</td><td></td><td>409.5***</td><td></td><td>413.8***</td><td></td></tr></table>

∼p < 01; ∗p < 005; ∗∗p < 001; ∗∗∗p < 0001. +Standard error.

Figure 4 WTP of MU Bidders Over Time  
![](/api/attachments/9SJEPD4Q/fulltext/images/f554f5409db21a0d9a86fc96d78d64c0c30d60f415a978f16039045072e2f340.jpg)

trajectory. Consistent with the previous model (1h), we find that before winning, MU bidders begin with a low initial bid and then increase their WTP over time. Because the interaction term of winning status and time is significant, it explains that timing of first win affects the WTP trajectory of MU bidders. After the first win, however, the rate of decline in WTP (0.028) is higher than rate of increase in WTP over time (0.016), and thus there is a net decline in WTP. Figure 4 shows that there are two components that explain the decrease in WTP of the MU bidder after winning. One is the winning effect that increases with time, and the other is experience effect (that is measured by Time). We argue that the winning event signals to bidders that their WTP is high enough; because he has already won an item, the bidder has less pressure to bid high for another item because his valuation for a latter item drops. We continue to detect the same effect on WTP for each subsequent win. In essence, these findings present vivid evidence of the modified demand reduction phenomenon we identified in sequential auctions, spread over multiple auction participations.

A high value of $\sigma _ { 3 } ^ { 2 }$ also suggests that the effect of the first win varies significantly among MU bidders. The negative and significant value of $\sigma _ { 3 0 }$ shows that bidders’ with high initial WTP (in their first auction) reduce their WTP less after the first win compared to others. In Figure 4, we only report the WTP trajectory of MU bidders’ considering unit lot size. Trajectories for higher lot-size auctions can be plotted in a similar way. Consistent to the previous model, we find that MU bidders reduce their WTP with increase in lot size.

Even though the results in Table 3 are for the group of MU bidders, we still find a high value of $\sigma _ { 0 } ^ { 2 }$ representing bidders’ heterogeneity at the beginning. MU bidders are defined as any bidder who participates in an auction after winning the same item in previous auctions. In our data set, we found many bidders who came back after the first win to scoop bargains but did not win, along with other serious bidders, perhaps business resellers, who won in many auctions. We argue that the presence of these different types of MU bidders explains a higher value of $\sigma _ { 0 } ^ { 2 } .$ At the same time, a small $\sigma _ { 1 } ^ { 2 }$ supports the argument that MU bidders do not differ much in how they change their WTP over time as they gain experience.

Our results show that the winning effect is stronger than the experience effect on WTP revisions in sequential auctions. In both cases, we find a high value of $\sigma _ { 0 } ^ { 2 }$ that explains bidder heterogeneity at the beginning, and low value of $\sigma _ { 1 } ^ { 2 }$ that means that change trajectories do not differ much within bidder categories (SU and MU bidders).

## 5.3. Summary

Table 4 summarizes the findings of our hypotheses testing.

Ours is the first study to empirically detect demand heterogeneity in sequential online auctions and its effect on bidding behavior. We have clearly demonstrated that heterogeneity in demand enables different bidding behavior in terms of learning and updating WTP. We find that both winning and experience have significant effect on bidding behavior in sequential auctions. We find that bidders’ WTP for additional units of the item decreases significantly after securing a win in previous auctions. We argue that this reduction occurs because of winning effect and characterizes the demand reduction phenomenon in sequential auctions. Ausubel and Crampton (2002) theorized a demand reduction effect in multiunit sealed-bid auctions that was empirically validated by List and Lucking-Reiley (2000). Modified demand reduction effect that we hypothesize and empirically validate in this research is unique to sequential online auctions because bidders have an opportunity to observe supply and demand, which may not be the case in isolated sealed-bid auctions. The winning effect is stronger than the experience effect.

Table 4 Hypotheses Summary

<table><tr><td>Hypotheses</td><td>Result</td></tr><tr><td>H1: In sequential auctions, SU bidders will have a higher WTP than MU bidders in the initial auction that they participate in.</td><td>Not supported (results in Table 2)</td></tr><tr><td>H2A: As an auction sequence progresses, SU bidders will increase their WTP.</td><td>H2A is supported, H2B is supported (results in Tables 2, 3)</td></tr><tr><td>H2B: As an auction sequence progresses, the WTP of MU bidders will also increase, but at a lower rate than SU bidders.</td><td></td></tr><tr><td>H3: After winning, MU bidders decrease their WTP in subsequent auctions.</td><td>Supported (results in Table 3)</td></tr><tr><td>H4: After each additional win, MU bidders reduce their WTP in subsequent auction.</td><td>Supported (results in Table 3)</td></tr><tr><td>H5A: WTP of SU bidders will decrease with an increase in the lot size.</td><td>H5A not supported, H5B supported (results in Tables 2, 3)</td></tr><tr><td>H5B: WTP of MU bidders will decrease at a faster rate than SU bidders with an increase in the lot size.</td><td></td></tr><tr><td>H6: The WTP of both SU and MU bidders will decrease with increase in auction duration.</td><td>Not supported (results in Table 2)</td></tr></table>

Although not formally tested through a developed hypothesis, we also find that the minimum winning bid observed by the bidders in the previous auctions in which they participated, affects their WTP, which substantiates our claim that bidders do observe and learn from their participation. This observation, along with other findings that MU bidders’ WTP’s are affected by the lot size, provides additional justification for the modified demand reduction. MU bidders do use information about supply and previous prices that are unique to sequential online environments to spread their demand over multiple auctions.

Kauffman and Wood (2006) looked at collectible rare coin auctions at eBay and found that bidders are likely to increase their bids after losing in the previous auction for the same item. Our study looks at the bidding behavior in sequential online auctions of commodity items and refines their result by showing that both SU and MU bidders increase their bid until they secure their first win. After securing the first win, SU bidders don’t participate in any more auctions, whereas MU bidder do and the WTP trajectories of MU bidders assume a negative slope in bidders’ experience, and each additional win by MU bidders results in a decline in their WTP.

A trend of declining prices in sequential auctions has been reported (Beggs and Graddy 1997). This trend commonly referred to as the “afternoon effect,” results when prices in a sequential auctions progression decline relative to auctioneer estimates. Although the context of these studies is different in many ways to online auctions, our results of declining WTP commitments give empirical explanation for the “afternoon effect.”

## 6. Conclusions and Future Research

We have presented in this paper an empirical study of real sequential online auctions that confirms that bidders are heterogeneous and that they learn and update their WTP as they participate in more auctions of the same item. We identified and captured the heterogeneity of bidders in terms of demand characteristics, participation, experience, and winning status. Unlike previous online bidding behavior studies (Bapna et al. 2004) that focus on when people bid and number of bids, we focus on the WTP formation of the bidders. The model was tested and validated against a unique data set and environment of sequential auctions, which lent our study the flavor of a longitudinal field experiment.

We drew specific conclusions about how different categories of repeat bidders update their WTP, based on their demand, experience, observed winning prices from previous auctions and winning status in those auctions. One important contribution is the finding that both SU and MU bidders on average increase their WTP in subsequent auctions until they secure their first win. The rate of increase for single-unit bidders is higher than for MU bidders. Another important contribution is that we offer the first characterization of the demand reduction phenomenon in the context of sequential auctions.

From a practical viewpoint, our findings are also relevant to auctioneers. We have seen in Figure 1 that the overall percentage of repeat bidders participating in sequential auctions is very significant. We observe that about 40% of winners come from the pool of repeat bidders. Therefore, understanding the bidding behavior of these bidders is of fundamental importance. We envision several ways auctioneers can benefit from better understanding these repeat customers.

We have found that the WTP of repeat bidders tends to increase over time before their first win, more so for SU bidders than MU bidders. After the first win, MU bidders exhibit demand reduction, with their WTP decreasing over time. We have also found that lot size has a significant effect on reducing the WTP of MU bidders and that the lowest price observed in previous auctions serves as a reference price to repeat bidders. To help auctioneers design the sequence of auctions to be used to dispose of their inventory, they can incorporate these findings into simulation tools of the type developed by Bapna et al. (2003). By experimenting with specific “bidder loads,” their arrival patterns and their WTP evolution patterns, they can play out different scenarios for the design of the auction sequence.

Auctioneers have at their disposal massive amounts of historical data, from which they can develop and constantly refine machine-learning classification and prediction models to help them identify the different types of repeat bidders. In any auction, they can then infer in real time the mix of bidders that are demanding their products at different points of the auction. They can use this information to run special promotions during each auction or to adjust the design of the next auction in the sequence.

The key design parameters for sequential auctions that affect the auctioneer’s capabilities for clearing inventory are the lot size and the duration of each auction in the sequence. We do not find that auction duration affects bidders’ WTP in a significant way. One can investigate if shorter auction duration in sequential auctions may lead to substantial savings on inventory holding costs for the auctioneer. On the other hand, auction duration has another impact too, which is an increase in the number of bidders showing up for an auction. Future research needs to further investigate the impact of auction duration on number of bidders and their impact on clearing prices. Our study also finds that, bidders’ WTP increases over time prior to their first win and WTP of MU bidders’ declines after their first win. Auction sequences with smaller lot size take longer time to clear off the inventory, and auctioneers have to factor in the resultant implications of changing WTP of SU bidders and MU bidders, as well as the higher holding costs. Conversely, an auction sequence with higher lot size takes less time to clear inventory, hence lower holding costs, but higher lot sizes reduce WTP of MU bidders. In planning for sequential auctions, the auctioneer has to consider these trade-offs in maximizing their profit.

Our analysis is based on data from a uniform price multiunit open ascending price online auction. The findings of our study can be generalized to the B2C subsector of the online auction market. It would be interesting to investigate the differences in WTP revisions strategies for other auction formats, such as Yankee auctions. Some possible future research opportunities would be to investigate the changes in bidders’ WTP in sequential auctions on environments such as eBay. With numerous sellers disposing of identical items on eBay, a sequential auction market has evolved and is substantial. An obvious concern in doing such a study relates to the complexity of sequential auctions that are created by multiple sellers and buyers. Furthermore, the trust level that we now control by considering a one-seller B2C format can be relaxed in a general eBay-like setting, and the resultant WTP revision strategies investigated. Our findings provide a base for conceptualizing and benchmarking such a study.

## Acknowledgments

The authors are very grateful for the extremely valuable comments they received from the associate editor and the reviewers throughout the review rounds. They added substantial value that has considerably enhanced the authors work.

## References

Ausubel, L. M., P. Crampton. 2002. Demand reduction and inefficiencies of multi-unit auctions. Working paper, University of Maryland, College Park. http://www.cramton.umd.edu/ papers1995-1999/98wp-demand-reduction.pdf.

Ba, S., P. A. Pavlou. 2002. Evidence of the effect of trust building technology in electronic markets: Price premiums and buyer behavior. MIS Quart. 26(3) 243–268.

Bajari, P., A. Hortaçsu. 2002. Cyberspace auctions and pricing issues: A review of empirical findings. D. Jones, ed. The New Economy Handbook. Academic Press, San Diego.

Bajari, P., A. Hortaçsu. 2003. The winner’s curse, reserve prices, and endogenous entry: Empirical insights from eBay auctions. RAND J. Econom. 34(2) 329–355.

Bapna, R., P. Goes, A. Gupta. 2001. Insights and analysis of online auctions. Comm. ACM 44(11) 42–50.

Bapna, R., P. Goes, A. Gupta. 2003. Replicating online Yankee auctions to analyze auctioneers’ and bidders’ strategies. Inform. Systems Res. 14(3) 244–268.

Bapna, R., P. Goes, A. Gupta, Y. Jin. 2004. User heterogeneity and its impact on electronic auction market design: An empirical exploration. MIS Quart. 28(1) 21–43.

Bapna, R., P. Goes, A. Gupta, G. Karuga. 2008. Predicting bidders’ willingness to pay in online multi-unit ascending auctions: Analytical and empirical insights. Informs J. Comput. 20(3) 345–355.

Beggs, A., K. Graddy. 1997. Declining values and the afternoon effect: Evidence from art auctions. RAND J. Econom. 28(3) 544–565.

Bernhardt, D., D. Scoones. 1994. A note on sequential auctions. Amer. Econom. Rev. 84(3) 653–657.

Chakraborty, I., G. Kosmopoulou. 2001. Auctions with endogenous entry. Econom. Lett. 72(2) 195–200.

Cheema, A., P. T. L. P. Leszczyc, R. Bagchi, R. P. Bagozzi, J. C. Cox, U. M. Dholakia, E. A. Greenleaf, et al. 2005. Economics, psychology, and social dynamics of consumer bidding in auctions. Marketing Lett. 16 3–4.

Diekmann, K. A., A. E. Tenbrunsel, P. P. Shah, H. A. Schroth, M. H. Bazerman. 1996. The descriptive and prescriptive use of previous purchase price in negotiations. Organ. Behav. Human Decision Processes 66(2) 179–191.

Frees, E. W. 2006. Longitudinal and Panel Data Analysis and Appli cations in the Social Sciences. Cambridge University Press, New York.

Gandal, N. 1997. Sequential auctions of Israeli cable television licenses: The morning effect. J. Indust. Econom. 45(4) 227–244.

Ginsburgh, V. A., J. C. van Ours. 2007. On organizing sequential auctions: Results of a natural experiment by Christie’s. Oxford Econom. Papers 59(1) 1–15.

Gopal, R. D., B. Pathak, A. K. Tripathi, F. Yin. 2006. From Fatwallet to eBay: An investigation of the impact of virtual communities on sales promotion. J. Retailing 82(2) 155–164.

Jeitschko, T. D. 1998. Learning in sequential auctions. Southern Econom. J. 65(1) 98–112.

Kauffman, R. J., C. A. Wood. 2006. Doing their bidding: An empirical examination of factors that affect a buyer’s utility in Internet auctions. Inform. Tech. Management 7 171–190.

Krishnamurthi, L., T. Mazumdar, S. P. Raj. 1992. Asymmetric response to price in consumer choice and purchase quantity decisions. J. Consumer Res. 19(December) 387–400.

Leornard, K. 2005. A new era of digital window shopping: From shopping cart abandonment to purchase. Research report, ScanAlert, Inc. http://www.webhostgear.com/shopping\_habits .pdf.

List, J. A., D. Lucking-Reiley. 2000. Demand reductions in multiunit auctions: Evidence from a sportscard field experiment. Amer. Econom. Rev. 90(4) 961–972.

List, J. A., D. Lucking-Reiley. 2000. Bidding behavior and decision costs in field experiments. Econom. Inquiry 40(4) 611–619.

Lohse, G. L., S. Bellman, E. J. Johnson. 2000. Consumer buying behavior on the Internet: Findings from panel data. J. Interactive Marketing 14(1) 15–29.

McAfee, R. P., D. Vincent. 1993. The declining price anomaly. J. Econom. Theory 60(1) 191–212.

Menezes, F. M., P. K. Monteiro. 1995. Existence of equilibrium in a discriminatory price auction. Math. Soc. Sci. 30(3) 285–292.

Milgrom, P., R. J. Weber. 1982. A theory of auctions and competitive bidding. Econometrica 50(5) 1089–1122.

Neugebauer, T. 2004. Bidding strategies of sequential first price auctions programmed by experienced bidders. Cuadernos Economica 27 153–184.

Neugebauer, T., P. Pezanis-Christou. 2007. Bidding at sequential first-price auctions with(out) supply uncertainty: A laboratory analysis. J. Econom. Behav. Organ. 63(1) 55–72.

Pinker, E. J., A. Seidmann, Y. Vakrat. 2003. Managing online auctions: Current business and research issues. Management Sci. 49(11) 1457–1484.

Reiley, D., D. Bryan, N. Prasad, D. Reeves. 2007. Pennies from eBay: The determinants of price in online auctions. J. Indust. Econom. 55(2) 223–233.

Rogosa, D. R., J. B. Willett. 1985. Understanding correlates of change by modeling individual differences in growth. Psychometrika 50 203–228.

Roth, A. E., A. Ockenfels. 2002. Last minute bidding and rules for ending second-price auctions: Evidence from eBay and Amazon auctions on Internet. Amer. Econom. Rev. 92(4) 1093–1103.

Singer, J. D. 1998. Using SAS PROC MIXED to fit multilevel models, hierarchical models, and individual growth models. J. Educational Behavioral Statist. 24(4) 323–355.

Singer, J. D., J. Willett. 2003. Applied Longitudinal Data Analysis Modeling Change and Event Occurrence. Oxford University Press, New York.

Telser, L. G. 1973. Searching for the lowest price. Amer. Econom. Rev. 63(2) 40–49.

Tenorio, R. 1999. Multiple unit auctions with strategic pricequantity decisions. Econom. Theory 13(1) 247–260.

Tripathi, A. K., S. K. Nair, G. G. Karuga. 2008. Optimal lot sizing policies for sequential online auctions. IEEE Trans. Knowledge Data Engrg. 21(4) 554–567.

Vincent, S., O. Chanel. 2007. Retailers and consumers in sequential auctions of collectibles. Canadian J. Econom. 40(1) 278–295.

Wang, J. T.-Y. 2006. Is last minute bidding bad? Working paper, Department of Economics, UCLA, Los Angeles. http:// homepage.ntu.edu.tw/<sup>\~</sup>josephw/LMB10.pdf.

Wang, X., A. L. Montgomery. 2003. The effects of advertising on customer retention and the profitability of auctions. Working paper, GSIA, Carnegie Mellon University, Pittsburgh, PA.

Weber, R. J. 1983. Multiple object auctions. R. Engelbrecht-Wiggans, M. Shubik, R. M. Stark, eds. Auctions, Bidding and Contracting Uses and Theory. New York University Press, New York.

Wilcox, R. T. 2000. Experts and amateurs: The role of experience in Internet auctions. Marketing Lett. 11(4) 363–374.

Zeithammer, R. 2002. Sequential Auctions for Substitutes A Theory of Bargain-Hunting on eBay. MIT Sloan School of Management, Cambridge, MA.

Zhao, J., C. L. Kling. 2004. Willingness to pay, compensation variation, and the cost of commitment. Econom. Inquiry 22(3) 503–517.
