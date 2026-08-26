---
otero_id: 2234
otero_key: "7D3AAWXJ"
title: "Exploring Bidder Heterogeneity in Multichannel Sequential B2B Auctions1"
authors: "Yixin Lu; Alok Gupta; Wolfgang Ketter; Eric van Heck"
year: "2016"
journal: "MIS Quarterly"
doi: "10.25300/misq/2016/40.3.06"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# EXPLORING BIDDER HETEROGENEITY IN MULTICHANNEL SEQUENTIAL B2B AUCTIONS<sup>1</sup>

Yixin Lu

Information Systems & Technology Management, School of Business, George Washington University, 2201 G Street NW, Washington, DC 20052 U.S.A. {yixinlu@gwu.edu}

Alok Gupta Information and Decision Sciences, Carlson School of Management, University of Minnesota, 321 19<sup>th</sup> Avenue South, Minneapolis, MN 55455 U.S.A. {alok@umn.edu}

Wolfgang Ketter and Eric van Heck Rotterdam School of Management, Erasmus University, PO Box 1738, 3000 DR Rotterdam, THE NETHERLANDS {wketter@rsm.nl} {evanheck@rsm.nl}

The proliferation of online auctions has attracted significant research interest in understanding real-life bidding behavior. However, most of the empirical work has focused on business-to-consumer (B2C) auctions. A natural question is whether the findings obtained from B2C auctions are applicable to business-to-business (B2B) auctions, which often involve much higher stakes. In this paper, we examine how professional bidders choose their bidding strategies in multichannel, sequential B2B auctions. Using an extensive data set from the world’s largest B2B market for cut flowers, we find a stable taxonomy of bidding behavior and identify five distinctive bidding strategies. In addition, we demonstrate that bidders’ choice of strategies is associated with their demand, budget constraint, and transaction cost. These findings challenge the conventional view that bidders’ bidding strategies will converge as they gain experience. We also analyze the economic impacts of different strategies. Our results provide useful implications for practical design of B2B auctions.

Keywords: Auction design, B2B auctions, bidder taxonomy, sequential auctions

## Introduction

The proliferation of online auctions has offered researchers a fertile ground to examine real-life bidding behavior (Ariely and Simonson 2003; Ba and Pavlou 2002; Bapna et al. 2009; Bapna et al. 2004; Goes et al. 2010, 2012; Kauffman and Wood 2006). However, most of the work has been restricted to auction-level outcomes in business-to-consumer (B2C) markets, which are characterized by well-understood products such as electronic devices. Comparatively, little attention has been paid to business-to-business (B2B) auctions, which are economically more significant.<sup>2</sup>

Despite the price discovery nature, there are systematic differences in the characteristics of B2B and B2C auctions. First, in B2B markets, firms typically only engage in exchange activities with a limited number of partners (Bakos and Brynjolfsson 1993). For example, in B2B procurement auctions, buyers often adopt a prescreening process to select the qualified suppliers that will later compete in the bidding process. As the result, transactions in these markets often involve high-level mutual trust and detailed product and quality requirements. This is quite different from B2C platforms such as eBay where bidders largely rely on the ratings of sellers. Second, bidders in B2B auctions are much more knowledgeable and experienced. They often participate in auctions repeatedly over a long time of period and know well their competitors and the goods on which they are bidding. In addition, since the majority of goods auctioned in B2B markets are not for personal consumption, bidders’ incentives are different from those competing in B2C markets. Third, bidders in B2B markets are often subject to hard budget constraints (Benoit and Krishna 2001).

To understand the implications of such differences on bidders’ bidding behavior, Mithas and Jones (2007) suggested that “future research should develop typologies of bidder heterogeneity in the B2B context similar to those that Bapna et al. (2004) developed in the B2C context” (p. 467). Bearing this in mind, we initiated the current study to examine competitive bidding in the world’s largest B2B flower trading market, the Dutch Flower Auctions (DFA). The DFA account for more than 60 percent of the global flower trade and generate over 4 billion euros in annual sales. Bidders in these auctions are experienced, knowledgeable, and have been participating in the bidding competitions repeatedly for many years. As such, the DFA provide an ideal setting to explore bidding strategies in B2B markets. Our main research questions are as follows:

(1) What bidding strategies do bidders adopt in B2B auctions? Are they different from the strategies found in B2C auctions and why?

(2) How do different bidding strategies affect bidders economic welfare?

(3) How can we incorporate bidders’ bidding strategies into practical design of B2B auctions?

Using an extensive data set that contains more than 250,000 transactions from both online and offline channels, we develop a stable taxonomy of bidding behavior and identify five distinctive bidding strategies. Since bidders have unique identities, we also track their bidding strategies across different auctions and examine the antecedents and consequences of their strategic choices. Specifically, drawing on economic theories and empirical evidence from prior research, we develop an explanatory model of bidders’ strategic choice. We further demonstrate that bidders’ choice of strategies have significant impact on the revenue generation potential of the market.

This paper makes several important contributions. To begin with, it is among the first to characterize bidding strategies pursued by professional bidders in B2B markets. As such, it complements previous studies (e.g., Bapna et al. 2004; Goes et al. 2012) that focus on bidding behavior in B2C contexts. In particular, our finding that despite bidders’ extensive experiences there are still theoretically meaningful and empirically robust clusters of bidding strategies in the B2B context challenges the conventional view that bidders’ strategies will eventually converge as they gain experience over time. Second, while most of the auction research in information systems (IS) and marketing has looked into bidding behavior in online markets, we investigate a single market where electronic (online) and traditional (offline) channels coexist. This allows us to empirically test the effects of channel affiliation on bidding strategies. Third, by analyzing the economic impacts of bidding strategies, our study sheds new light on price dispersion in auction markets. From the managerial perspective, the flower trading market (i.e., the DFA) examined in this research, given its sheer magnitude and economic importance, epitomizes the common challenges faced by practitioners (especially auctioneers) in B2B markets. Due to the limited availability of proprietary data, no prior research, to our knowledge, has studied bidder heterogeneity, or its impact on design of multichannel B2B markets. The results from the current study provide valuable insights for auctioneers to design and adapt policies to fit their needs.

The rest of the paper proceeds as follows. We first review the prior literature and introduce the empirical context. We then discuss the identification of bidding strategies. This is followed by the examination of bidders’ choice of different strategies. We continue with the outcome analysis of different strategies. Finally, we discuss the implications of our findings for both practitioners and scholars involved in the design of complex B2B auctions and conclude with an outline for future work.

## Prior Literature

In this section, we discuss two streams of literature that are closely related to the current study.

## Bidder Heterogeneity

Traditionally, auctions have largely been studied from the game-theoretic perspective. Bidders are assumed to be homogeneous and adopt the Bayesian-Nash equilibrium strategy (McAfee and McMillan, 1987; Milgrom, 1989; Myerson, 1981). While plausible in traditional face-to-face auctions, this assumption quickly breaks down in the online context (Ariely and Simonson, 2003; Bajari and Hortacsu 2004). This highlights the necessity of studies addressing the gap between the behavioral reality and the predictions from classical theory (Rothkopf and Harstad 1994).

Over the past decades, many researchers have pursued more accurate models to explain real-life bidding behavior. For example, Carare and Rothkopf (2005) develop theoretical models for the effect of transaction costs on winning bids in Dutch auctions. Park and Bradlow (2005) incorporate four key components of the bidding process (whether people bid on an auction, who bids, when they bid, and how much they bid in the auction) in their integrated model for bidding behavior in online auctions of computer notebooks. Aside from the theoretical work, researchers have also adopted a data-driven, inductive approach to understand why real bidders do things as they do (Engelbrecht-Wiggans 2000). For example, using transaction data from Yankee auctions, Bapna et al. (2004) identify five different bidding strategies that result in different winning likelihoods and consumer surplus. They also discuss the promises of such bidder taxonomy in guiding the development of user-centric bidding agents and facilitating real-time auction calibration. A more recent study by Goes et al. (2012) extends the research on bidder taxonomy to sequential auctions where bidders have the opportunity to participate in multiple auctions and learn from past experience. They find that bidders’ choice of bidding strategies are contingent on their demand, participation experience, and auction design parameters.

However, most of the empirical research on bidding behavior has exclusively focused on B2C auctions where bidding activities are predominantly associated with purchases for personal consumption and thereby a questionable assessment of valuation and willingness-to-pay (WTP). Additionally, bidders’ participation experience in these auctions can vary a lot. A natural question is whether the observed heterogeneity in B2C auctions will disappear when bidders have a strong sense of WTP and have gained sufficient experience. In other words, will bidders’ strategies converge if they repeatedly participate in the auctions for a long time? Besides the theoretical relevance, the answer to this question has important practical implications to auction design. As such, in the current study, we draw upon a unique B2B context and examine the bidding behavior of professional bidders.

## Market Channels

The increasing use of the Internet has fueled the adoption of online (electronic) channels in many markets (Kambil and

Van Heck 1998; Kuruzovich et al. 2008; Overby and Jap 2009). Compared to traditional offline channels, online channels offer many benefits to both buyers and sellers. For buyers, they can significantly reduce search costs (Bakos 1997) and switching costs (Devaraj et al. 2006). For sellers, they greatly increase market reach and reduce transaction costs (Kambil and Van Heck 1998).

Despite these advantages, however, the inherent information asymmetry between buyers and sellers in online channels may result in undesirable outcomes. For example, Koppius (2002) shows that the benefits from the reduced search costs can be mitigated substantially by the reduced market state information; thereby, buyers from online and offline channels would pay the same price. Dewan and Hsu (2004) also find a significant adverse selection discount (i.e., roughly 10 to 15 percent of the value of the goods) on eBay. In a more recent study, Ghose (2009) empirically demonstrates that the information asymmetry problem persists in online markets despite the presence of signaling mechanisms such as reputation systems and product condition disclosures.

Given such trade-off, researchers have examined multiple factors that may affect buyer’s and seller’s channel choices. Using an extensive data set that contains sales event of used vehicles for over two years, Overby and Jap (2009) find that transactions involving low quality uncertainty are more likely to occur in online channels, whereas those involving high quality uncertainty occur more in traditional offline channels. In addition, they also examine the interdependencies between buyers and sellers in the market and demonstrate that one party’s use of online channels will inevitably influence the other’s choice.

Unlike previous work, our current study does not specifically look into bidders’ choice of participation channels. Rather, we are interested in bidders’ behavioral characteristics across different channels, e.g., whether bidders using online channel are more likely to adopt certain strategies. Understanding the impact of channel adoption and usage on bidding behavior provides useful implications for the design and implementation of multichannel auction markets.

## The Dutch Flower Auctions

The Dutch flower network is the largest in the world (Kambil and van Heck, 1998). The Dutch Flower Auctions (DFA) play an important role in the global flower trade. They serve as efficient centers for the exchange of cut flowers and potted plants between buyers and sellers. In 2014, Royal FloraHolland,<sup>3</sup> the market leader that operates six auction centers strategically located across the country, reported trades of over 43 million cut flowers and 4 million potted plants per day, generating over 4 billion euros in annual sales.

![](/api/attachments/7D3AAWXJ/fulltext/images/5129c4e5db551cea95e47e3f49d6b4ca30cf3bfbea7babb4432da451c01b95fd.jpg)  
In addition to the current asking price, each clock also contains information about the current seller, the winning bidder, the type of flower being sold, the minimum purchase quantity, and the reserve price, among other things.  
Figure 1. A Set of Three Simultaneous Dutch Flower Auctions

## The Mechanism

The DFA are multiunit sequential Dutch auctions. They are implemented using fast-paced auction clocks (see Figure 1). The clocks initially start at a high price, and then rapidly tick down in a counterclockwise direction. As the price falls, each bidder can bid by pressing a button indicating the portion (which must exceed the minimum quantity set by the auctioneer) of the lot<sup>4</sup> he is willing to accept at the current price (which must exceed the seller’s reserve price, a price below which the seller is unwilling to part with the goods). The first bidder who makes a bid wins. If the winning bidder does not select the entire remaining quantity, the clock restarts at a high price and the auction continues. This process repeats until the entire lot is sold, or until the price falls below the seller’s reserve price, in which case any unsold goods in that lot are destroyed. It is noteworthy that only winning bids can be observed during the entire auction cycle. This is quite different from the mechanisms used in popular online auction sites such as eBay and Yahoo!.

From 6:30 a.m. to 10:00 a.m., up to 40 auction clocks run simultaneously. On average, each transaction takes only 4 seconds. Roughly 125,000 transactions take place daily. Given the extreme time pressure, bidding in the DFA is challenging, even for professional bidders with years of practice experience.

## The Online Bidding Channel

In June 1996, the DFA introduced the remote buying application (KOA),<sup>5</sup> an online bidding system that enables bidders to participate in auctions without being physically present in the auction halls. Initially, such online bidding channel only attracted large buyers.<sup>6</sup> The reason is twofold. On one hand, the KOA system requires a significant investment in hardware and software. This includes dedicated computers and the communication system between the auction hall and the computers used for bidding. On top of that, bidders also have to pay the monthly subscription fee of approximately 220 euros in order to use the system. On the other hand, large buyers have a strong incentive to adopt the remote bidding system. Traditionally, large buyers need to send several bidders to follow auctions that run in parallel. The adoption of KOA allows each bidder to effectively monitor several auction clocks at the same time, helping large buyers to reduce personnel costs.

Over the past few years, KOA has become increasingly popular. According to our interviews, the online channel has brought great benefits to buyers by reducing their travel costs and enhancing their monitoring capabilities. Some large buyers also point out that KOA allows them to better coordinate their purchases from the auctions and sales to end customers.

As noted above, the DFA are a clear example of dynamic, complex B2B markets. However, due to the limited availability of proprietary data, few empirical studies have examined the bidding dynamics. As a result, little is known about how to improve the design and operationalization of these auctions.

## Identification of Bidding Strategies

In this section, we begin with the description of the data set. We then discuss the classification method and empirical results.

## Data

Our data set contains transaction details of roses from June 1 to September 30, 2010 (88 auction days) at a major auction site where screen (image) auctioning has been implemented. This means, no actual flowers are shown in the auction hall; instead, they observe a picture of the flower from the current lot, together with the product information such as product category, characteristics (e.g., stem length), and quality, as well as supplier information. Prior research has shown that the use of screen auctioning leads to lower prices due to the reduced product quality information (Koppius et al., 2004). However, since both online and offline bidders receive the same product information, the effect of screen auctioning becomes irrelevant.

In total, we have 280,945 transactions from 38,848 lots. The size of a lot can vary from a few units to more than 100 units. Depending on the type and quality of the flower, each unit consists of 20 to 80 stems. A total of 593 bidders participated in these auctions, with 288 of them having adopted the online channel.

Table 1 gives a stylized example of a sequence of transactions that can be found in our data set. In this example, a lot containing 18 units is sold. At the beginning of each round, the auctioneer sets the starting price and minimum purchase quantity (italicized in the table). The sales prices are not monotonically decreasing or increasing.<sup>7</sup> Also, unlike the existing studies which focus on the situation where only one unit is sold in each round, in our case, the purchase quantity in each round can vary a lot. Because bidders do not know a priori whether there will be units left after the current round of auction, they face higher uncertainty in these auctions.

In order to control for the prescreening effects related to product category or quality, we created a subsample where the products are homogeneous with respect to their key characteristics such as stem length and bloom stage. The particular product we have chosen is Avalanche Rose, because its total transaction amount was the largest among the entire assort ment, and it was sold steadily throughout the four months.

After screening and preprocessing,<sup>8</sup> we are left with a total of 8,384 transactions from 998 auctions. The number of bidders participating in these auctions also reduces from the original 593 to 455. Nevertheless, the new data set is still rich enough for us to explore the bidding strategies pursued in these complex, sequential auctions. Table 2 provides a summary of the descriptive statistics. We can see that there is high variability in lot size, winning price, and purchase quantity.

We also examined the price dynamics during the four-month period using a series of boxplots. Figure 2 illustrates the daily price variation as well as the price trend. Despite the homo-

<sup>7</sup>Van den Berg et al. (2001) presented some empirical evidence of declining price in sequential rounds of the flower auctions; however, if we look at individual auctions, price trends are inconclusive.

Table 1. A Sample Entry of Logbook

<table><tr><td>Transaction Index</td><td>Flower ID</td><td>Seller ID</td><td>Available Quantity</td><td>Minimum Purchase Quantity</td><td>Starting Price (cent)</td><td>Bidder ID</td><td>Purchase Quantity</td><td> $Price^{\dagger}$ </td></tr><tr><td>171</td><td>12157</td><td>5547</td><td>18</td><td>1</td><td>100</td><td>439</td><td>2</td><td>22</td></tr><tr><td>172</td><td>12157</td><td>5547</td><td>16</td><td>3</td><td>41</td><td>395</td><td>5</td><td>20</td></tr><tr><td>173</td><td>12157</td><td>5547</td><td>11</td><td>4</td><td>39</td><td>439</td><td>7</td><td>21</td></tr><tr><td>174</td><td>12157</td><td>5547</td><td>4</td><td>4</td><td>40</td><td>563</td><td>4</td><td>20</td></tr></table>

<sup>†</sup>This is the price for a stem of the flower. The price for a unit varies from €4 to €16, depending on the number of stems per unit.

Table 2. Summary Statistics of the Subsample

<table><tr><td>Statistic</td><td>Number of Auctions per Day</td><td>Bidders per Auction</td><td>Number of Auctions a Bidder Participates per Day</td><td>Lot Size</td><td>Winning Price (cent)</td><td>Purchase Quantity</td></tr><tr><td>Mean</td><td>11.34</td><td>8.26</td><td>1.24</td><td>80.85</td><td>36.69</td><td>9.62</td></tr><tr><td>Median</td><td>11.00</td><td>7.00</td><td>1.00</td><td>72.00</td><td>37.00</td><td>6.00</td></tr><tr><td>Standard Deviation</td><td>1.99</td><td>5.72</td><td>0.54</td><td>59.95</td><td>13.39</td><td>13.94</td></tr><tr><td>Skewness</td><td>0.62</td><td>0.79</td><td>2.64</td><td>1.33</td><td>0.15</td><td>6.69</td></tr><tr><td>Minimum</td><td>8.00</td><td>1.00</td><td>1.00</td><td>5.00</td><td>7.00</td><td>1.00</td></tr><tr><td>Maximum</td><td>18.00</td><td>34.00</td><td>6.00</td><td>342.00</td><td>75.00</td><td>311.00</td></tr></table>

![](/api/attachments/7D3AAWXJ/fulltext/images/35c69ab5415de87a4feafe1ebebf5ced0b5b55b0a367033c6dd3f9343dfdf889.jpg)  
Figure 2. The Price Variation of Roses During the Period June 1 and September 30, 2010

geneity of the auctioned products, the transaction prices can still vary a lot even on the same day. Also, the periodic pattern of the daily average price suggests that there might be external market forces. In the next section, we will discuss the price dynamics in detail.

## Cluster Analysis and Results

We use cluster analysis to explore the structural differences in bidders’ bidding strategies. However, unlike previous studies by Bapna et al. (2004) and Goes et al. (2012), in the DFA, we cannot observe when a bidder enters an auction or drops out, because only winning bids (i.e., winners’ identities as well as their purchase quantities and winning prices) are revealed.

Using the rich transaction data that captures bidder’s winning bids across different auctions, we create four proxy variables—time of entry in an auction, time of entry on a day, time of exit on a day, and frequency of bid on a day—to characterize bidders’ bidding behavior.<sup>9</sup> Note that the introduction of day-level variables is a novel contribution to the characterization of bidding behavior in the B2B context. Given that bidders are participating in these auctions on a daily basis, the day-level variables can help us to better relate the observed bidding behavior with the business profiles and needs of different bidders. Next, we will describe how we construct and operationalize these proxy variables.

## Time of Entry in an Auction (TOE-A)

One of the key decisions for bidders in the DFA is to decide when to press the button. If it is too early, bidders may end up paying a higher price than necessary, whereas reacting too slow will result in forgoing the opportunity to obtain the auctioned product. Since the DFA operate in a multiunit, sequential manner, each auction usually consists of multiple rounds, although neither bidders nor auctioneers know a priori how many rounds it will take to finish the current auction. To account for the variability in the number of rounds of an auction, we define a bidder’s time of entry in an auction, TOE-A, as the ranking of the sub-auction where the bidder wins. For instance, if a bidder placed his bid in the second round and the entire auction lot took 10 rounds to finish, the TOE-A for this bidder in that specific auction is 2/10 = 0.2. Since bidders often participate in many auctions on a given day, we take the average of a bidders’ TOE-As across different auctions as his overall TOE-A on that day.

## Time of Entry on a Day (TOE-D)

Since there are multiple auctions for the same product on any given day<sup>10</sup> and the auction schedule is publicly announced, some bidders take such information into account and thus choose to act as observers in the first few auctions to learn about the market conditions, while others are bidding actively from the very beginning of the day. To capture such behavioral differences, we introduce the day-level proxy, TOE-D, which is defined as the ranking of the auction where a bidder first wins. For instance, if there were six auctions for the specific product on a given day, and a bidder’s first winning bid was in the third auction, the TOE-D for this bidder is 3/6 = 0.5.

## Time of Exit on a Day (TOX-D)

In addition to bidders’ day-level entry decisions, we also consider the timing when they drop out from the competition. Given that most bidders in the DFA are buying on order, their daily exist timings can reflect as much useful insights about their bidding strategies as their daily entry timings. Similar to TOE-D, we define TOX-D as the ranking of the auction where a bidder places his last winning bid.

## Frequency of Bid on a Day (FOB-D)

We define a bidders’ frequency of bid on a day (FOB-D) as the total number of winning bids he has placed on that day. Unlike the bidding frequency used in prior research of English auctions which indicates bidders’ involvement, in our case, FOB-D is closely related to bidders’ potential hedging behavior. That is, in order to avoid or compensate for the regret resulting from a suboptimal bidding decision, some bidders tend to spread their purchases across multiple auctions even if they can fulfill their total demand in one auction.

Using the four proxy variables defined above, we applied K-means clustering to identify bidders’ strategic bidding patterns. A major challenge in the application of the K-means method is to determine the number of clusters. Given the exploratory nature of this research, we followed the procedure suggested by Koehly (2001) and started with a hierarchical clustering to examine the cluster structure at different levels. Next, we repeated K-means clustering with a range of different values of K $( K _ { m i n } = 2 , K _ { m a x } = 1 0 )$ . According to the Calinski-Harabasz criterion (Milligan and Cooper 1985), the optimal number of clusters is five. We compared the cluster centers under hierarchical clustering and K-means clustering (K = 5), and found the results were very consistent. Note that good scores on an internal criterion (e.g., Calinski-Harabasz criterion) do not necessarily translate into the effectiveness of K-means clustering. An alternative, and perhaps better evaluation, is to look at the interpretability of the clustering results. This is often referred to as external validity. In our case, we used ANOVA to test whether there are significant differences between the cluster centroids. As shown in Table 3, the differences between the five clusters from K-means clustering are statistically significant.

Table 3. Cluster Result ANOVA

<table><tr><td>Cluster Attribute</td><td>Cluster Mean Square</td><td>Error Mean Square</td><td>F Mean Square</td><td>Sig.</td></tr><tr><td>TOE-A</td><td>88.855</td><td>0.022</td><td>3967.964</td><td>0.000</td></tr><tr><td>TOE-D</td><td>97.418</td><td>0.021</td><td>4650.953</td><td>0.000</td></tr><tr><td>TOX-D</td><td>100.998</td><td>0.022</td><td>4642.803</td><td>0.000</td></tr><tr><td>FOB-D</td><td>30.955</td><td>0.014</td><td>2265.796</td><td>0.000</td></tr></table>

Further, we also conducted a robustness test on the clustering results using cross validation. Specifically, we randomly split the observations<sup>11</sup> into two parts, one with two-thirds of the observations (training set) and the other with one-third of the observations (test set). We applied K-means clustering (K = 5) to the training set and used the identified cluster centers to label the observations from the test set. We then checked whether the labels of the observations in the test set are the same as the ones resulting from the K-means clustering on the whole data set. We repeated this process 100 times and found that 99.27 percent of the observations from the test set have the same label. This confirms that our clustering results are very stable.

We characterize the clusters identified from K-means clustering based on the features conveyed by the corresponding centroid values of the classification variables. As Table 4 shows, the five clusters identified by the K-means algorithm have a straightforward and meaningful interpretation in our sequential B2B auction context.

To begin with, based on the differences in the value of TOE-A (bidders’ time of entry in an auction), we have early bidders who bid early in an auction, opportunists who bid late and tend to look for good bargains in a given auction, and analyzers, those who bid in between the former two scenarios. The values of TOE-D (bidders’ time of entry on a day) are also informative. A small value of TOE-D, for a given bidder, suggests a high urgency of purchase, whereas a large value of TOE-D indicates a strategic consideration of upcoming auctions. With this in mind, we name the strategies with small values of TOE-D as conservative and the ones with large values as forward-looking.<sup>12</sup> It is noteworthy that, with the exception of analyzers, conservative bidders all have a small value of TOX-D, which means early dropout from the auctions on a day. Finally, if we look at FOB-D (bidders’ frequency of bid on a day), on average, the analyzers had more than twice the number of winning bids as others.

Given that all bidders in the DFA are professional and have more than sufficient bidding experience, the existence of these distinctive bidding strategies challenges the popular view that bidders’ strategies will converge as they gain experience (Goes et al. 2012), highlighting the fundamental differences between B2B and B2C contexts.

## Understanding Bidders’ Choice of Strategies

In order to understand the observed heterogeneity, we now examine the underlying drivers of bidders’ strategic choices. Auction researchers have found a variety of factors that affect bidders’ bidding behavior (Chakravarti et al. 2002). However, in many cases, it is difficult to quantify these factors (especially the psychological and social ones). Given that bidders in the DFA have more than sufficient experience with the empirical context, we argue that they are less susceptible to psychological and social effects such as herding bias (Dholakia and Soltysinski 2001) or addiction to excitement (Herschlag and Zwick 2000); instead, these bidders are acting as “utility maximizers,” in that they always choose the strategy that best fits their business constraints, needs, and preferences.<sup>13</sup> In the following, we first discuss the potential determinants of bidders’ strategic choices and describe how to operationalize them in our empirical context. We then develop an empirical model to explain bidders’ choice of bidding strategies on a given day.

<table><tr><td colspan="7">Table 4. Cluster Centers</td></tr><tr><td rowspan="2">Clusters/Strategies†</td><td colspan="2">Bidders Adopting the Strategy</td><td colspan="4">Mean (Standard Deviation) of Classification Variables</td></tr><tr><td>Cases</td><td>%</td><td>TOE-A</td><td>TOE-D</td><td>TOX-D</td><td>FOB-D</td></tr><tr><td colspan="7">Conservative</td></tr><tr><td>Early bidders (E-C)</td><td>1578</td><td>23.70</td><td>0.30 (0.14)</td><td>0.27 (0.13)</td><td>0.28 (0.14)</td><td>0.32 (0.10)</td></tr><tr><td>Opportunists (O-C)</td><td>1455</td><td>21.80</td><td>0.79 (0.14)</td><td>0.27 (0.13)</td><td>0.28 (0.14)</td><td>0.32 (0.10)</td></tr><tr><td>Analyzers (A-C)</td><td>833</td><td>12.50</td><td>0.57 (0.19)</td><td>0.28 (0.16)</td><td>0.76 (0.18)</td><td>0.73 (0.19)</td></tr><tr><td colspan="7">Forward-looking</td></tr><tr><td>Early bidders (E-F)</td><td>1388</td><td>20.80</td><td>0.31 (0.14)</td><td>0.76 (0.15)</td><td>0.77 (0.15)</td><td>0.33 (0.11)</td></tr><tr><td>Opportunists (O-F)</td><td>1411</td><td>21.20</td><td>0.81 (0.14)</td><td>0.76 (0.15)</td><td>0.78 (0.15)</td><td>0.33 (0.11)</td></tr></table>

<sup>†</sup>Strictly speaking, these are not real strategies pursued by bidders but proxy strategies. However, as discussed earlier, due to the nature of our empirical context, the latter ones can serve as good approximations of the former.

## Determinants of Bidders’ Strategic Choice

Drawing upon prior literature, we identify three economic factors that are critical to bidders’ strategic choices: budget constraint, demand, and transaction cost.

## Budget Constraint

Budget constraint is an important feature of real-world B2B auctions. Previous research in the context of privatization of high-value public goods (e.g., standard treasury, spectrum, or electricity auctions) has shown that in the presence of budget constraint, the revenue equivalence theorem no longer holds (Che and Gale 2000; Laffont and Robert 1996). When multiple objects are auctioned, Benoit and Krishna (2001) point out that it may be advantageous for a bidder to bid aggressively on one object to raise the price paid by his rivals and deplete their budgets so that the second object could be obtained at a lower price.

In the case of the DFA, bidders also face different levels of budget constraints.<sup>14</sup> Following the rationale of Benoit and Krishna, bidders with a high budget constraint (for example, small, family-run florists) would bid in later auctions on a day, in the hope that those who have already fulfilled their demand or consumed their budget in earlier auctions drop out from the market. In addition, unlike the classical setting of sequential auctions where only one unit is sold in each transaction, the purchase quantity in each round of the DFA has to meet a predetermined minimum amount. Currently, auctioneers usually set a low minimum purchase amount at the beginning and gradually increase it as the auction proceeds. As a result, if a bidder with a high budget constraint missed the first few rounds of an auction, he would not be able to afford purchasing the products in that auction any more. Therefore, we hypothesize that

H1a: Bidders with high budget constraints are more likely to choose an early bidding strategy over an opportunistic strategy.

H1b: Bidders with high budget constraints are more likely to choose a forward-looking, early bidding strategy over a conservative, early bidding strategy.

## Demand

Bidders in the DFA have, in general, multiunit demand for any given type of flower. Such demand could be orderdriven or speculation-based, that is, some bidders are exclusively purchasing on order while others may purchase an extra amount of products when they foresee a “hot” market for certain flowers.<sup>15</sup>

When bidders are buying on order, they typically receive a commission fee which varies from 10 to 15 percent of the purchase price. Thus they are less likely to shade their bids or reduce the demand (Ausubel and Cramton, 2002; List and Lucking-Reiley, 2000); in fact, they would bid aggressively to make sure they can fulfill the orders from their customers. However, when bidders have a large speculation-based demand, they are more likely to postpone their bidding in the first few rounds and wait for a bargain. Further, given that there are often multiple auctions with closely substitutable products, they may spread the demand over several auctions to maximize their expected payoff. This is also referred to as modified demand reduction (Goes et al. 2010). Given these considerations, we hypothesize that

H2a: Bidders are more likely to choose an opportunistic strategy over an early bidding strategy when they have large demand.

H2b: Bidders are more likely to choose an analytical strategy over an early bidding strategy when they have large demand.

## Transaction Cost

Bidders’ transaction cost refers to the time and effort invested in gathering information, preparing bids and participating in an auction. Carare and Rothkopf (2005) argue that bidders incur incremental transaction costs if they delay bidding in slow Dutch auctions. In the case of the DFA, given the high complexity and extreme time pressure, monitoring market dynamics and learning market trends are not only time-consuming but also cognitive-challenging.

The adoption of the online bidding channel (i.e., KOA) can virtually eliminate the opportunity cost of time and transportation cost associated with physical attendance at the auctions. Further, it allows bidders to easily switch from one auction to another, thereby enhances their monitoring capabilities and reducing their search costs. Given our previous discussion of different bidding strategies, such benefits are particularly attractive for opportunistic and forward-looking bidders. Therefore, we hypothesize that

H3a: Bidders in the online channel are more likely to choose an opportunistic strategy over an early bidding strategy.

H3b: Bidders in the online channel are more likely to choose a forward-looking, opportunistic strategy over a conservative, opportunistic strategy.

## Explanatory Model of Bidders’ Choice

To test our hypotheses, we develop an explanatory model of bidders’ strategic choices, using multinomial logistic regression (MNL). MNL has been used to model individual choice in a variety of social, economic, and political contexts (Greene 2008). In our case, we model the log odds of a bidder choosing strategy i relative to a baseline strategy on a given day as a linear combination of three explanatory variables that reflect bidders’ budget constraint, demand, and channel adoption. The generic model is specified as follows:<sup>16</sup>

$$
\begin{array}{l} \log \left(\frac {p (\text { strategy } = i)}{p (\text { referencestrategy })}\right) = \beta_ {0, i} + \beta_ {1, i} \text { BudgetConstraint } \\ + \beta_ {2, i} \text { Demand } + \beta_ {3, i} K O A \end{array}\tag{1}
$$

In Equation (1), is defined as a binary variable which takes a value of 1 if a bidder has a high budget constraint and 0 otherwise.<sup>17</sup> The variable measures a bidder’s daily demand and is calculated ex post by dividing the bidder’s total purchase quantity on a given day over the maximum of his daily purchase quantity during the four month period. The variable KOA indicates the bidder’s channel adoption; it takes a value of 1 if a bidder has adopted the online channel and 0 otherwise. The coefficients $\beta _ { 1 , i } , \beta _ { 2 , i } ,$ , and $\beta _ { 3 , \iota }$ can be interpreted as the increase in log odds of choosing strategy i over the reference strategy resulting from a one-unit increase in BudgetConstraint, Demand, and KOA, respectively, given the other variables are held constant.

<table><tr><td colspan="4">Table 5. Model Fitting Results</td></tr><tr><td colspan="4">Fit of the Model</td></tr><tr><td>Criterion</td><td>Intercept Only</td><td>MNL Model</td><td></td></tr><tr><td>AIC</td><td>6594.6</td><td>5557.4</td><td></td></tr><tr><td>-2Log-Likelihood</td><td>6586.6</td><td>5525.4</td><td></td></tr><tr><td colspan="4">Analysis of Effects</td></tr><tr><td>Effect</td><td>Chi-Square</td><td>Degrees of Freedom</td><td>Sig.</td></tr><tr><td>Intercept</td><td>941.8</td><td>4</td><td>0.000</td></tr><tr><td>BudgetConstraint</td><td>626.7</td><td>4</td><td>0.000</td></tr><tr><td>Demand</td><td>562.9</td><td>4</td><td>0.000</td></tr><tr><td>KOA</td><td>49.3</td><td>4</td><td>0.000</td></tr></table>

We first set E-C (conservative, early bidding strategy) as the reference strategy and conducted a likelihood ratio test to evaluate the overall relationship between the explanatory variables and the response variable. As shown in Table 5, all three explanatory variables (i.e., BudgetCostraint, Demand, and KOA), as well as their linear combination have statistically significant effects on bidders’ strategic choices.

We continued to run the MNL model with different reference strategies.<sup>18</sup> The parameter estimates are reported in Table 6. To begin with, we can see that when a bidder has a high budget constraint, he is more likely to choose the strategy E-C over strategy O-C and O-F (the estimated coefficients for the BudgetConstraint dummy are -1.39 and -1.37, respectively), while other conditions are kept constant. Similarly, the log odds of a bidder choosing the strategy E-F over strategy O-C and O-F also increases when he has a high budget constraint. This observation supports hypothesis H1a. However, it is unclear whether bidders with a high budget constraint would choose strategy E-F over strategy E-C, because the corresponding coefficient is insignificant. Thus H1b is not supported.

Further, we find that when bidders have large demand on a day, they are more likely to choose an analytical strategy (A-C) over opportunistic strategies (O-C and O-F), which in turn are more likely to be chosen over early bidding strategies (E-C and E-F). Therefore, both H2a and H2b are supported. Finally, we can see that the log odds of a bidder choosing opportunistic strategies (O-C and O-F) over early bidding strategies (E-C and E-F) increase significantly if the bidder has adopted the online channel. Between the two opportunistic strategies (i.e., O-C and O-F), an online bidder is more likely to choose the latter (the coefficient for the dummy is 0.23). Thus H3a and H3b are supported. Table 7 provides a summary of our hypothesis testing results.

## Outcome Analysis

Prior research (e.g., Bapna et al. 2004) has shown that different bidding strategies result in different winning likelihoods and payoffs. In our case, because all of the observed bids are winning bids, it is not possible to compare the winning likelihoods of different strategies. In light of this, we focus on the impact of bidding strategies on surplus extraction. Given that bidders’ valuations are unknown, we use loss-of-surplus, which is defined as the difference of a bidder’s winning price<sup>19</sup> in an auction and the lowest winning price within the same auction, to compare the magnitude of bidders’ surplus. Thus a bidder with the lowest loss-ofsurplus is considered to have extracted the highest surplus among all the bidders in the same auction.

Note that bidders in sequential auctions can learn the market dynamics and opponents’ profiles from previous rounds and update their willingness-to-pay to maximize their payoff (Goes et al. 2010; Jeitschko 1998). In our case, the clustering results in Table 4 have suggested that opportunists tend to be more patient and wait longer in an auction than other bidders. This allows them to acquire an informational advantage in the bidding process. Therefore, we hypothesize that

<table><tr><td colspan="7">Table 6. Parameter Estimates</td></tr><tr><td rowspan="2" colspan="2">Strategy</td><td rowspan="2">Variable</td><td colspan="4">Reference Strategy</td></tr><tr><td>Early Bidders (E-C)</td><td>Opportunists (O-C)</td><td>Analyzers (A-C)</td><td>Early bidders (E-F)</td></tr><tr><td rowspan="8">Conservative</td><td rowspan="4">Opportunists (O-C)</td><td>Intercept</td><td>-1.96***</td><td></td><td></td><td></td></tr><tr><td>BudgetConstraint</td><td>-1.39***</td><td></td><td></td><td></td></tr><tr><td>Demand</td><td>1.74***</td><td></td><td></td><td></td></tr><tr><td>KOA</td><td>0.09</td><td></td><td></td><td></td></tr><tr><td rowspan="4">Analyzers (A-C)</td><td>Intercept</td><td>-8.09***</td><td>-5.72***</td><td></td><td></td></tr><tr><td>BudgetConstraint</td><td>-3.69***</td><td>-1.84***</td><td></td><td></td></tr><tr><td>Demand</td><td>5.46***</td><td>3.62***</td><td></td><td></td></tr><tr><td>KOA</td><td>0.28*</td><td>-0.15</td><td></td><td></td></tr><tr><td rowspan="8">Forward-looking</td><td rowspan="4">Early bidders (E-F)</td><td>Intercept</td><td>-0.20</td><td>1.69***</td><td>7.18***</td><td></td></tr><tr><td>BudgetConstraint</td><td>-0.14</td><td>1.24***</td><td>3.33***</td><td></td></tr><tr><td>Demand</td><td>0.17</td><td>-1.43***</td><td>-4.57***</td><td></td></tr><tr><td>KOA</td><td>-0.20</td><td>-0.30**</td><td>-0.09</td><td></td></tr><tr><td rowspan="4">Opportunists (O-F)</td><td>Intercept</td><td>-1.94***</td><td>-0.02</td><td>5.78***</td><td>-1.50***</td></tr><tr><td>BudgetConstraint</td><td>-1.37***</td><td>0.06</td><td>1.96***</td><td>-1.07***</td></tr><tr><td>Demand</td><td>1.49***</td><td>-0.19</td><td>-3.85***</td><td>1.04***</td></tr><tr><td>KOA</td><td>0.20*</td><td>0.23*</td><td>0.53*</td><td>0.48***</td></tr></table>

\*\*\*p < 0.001; \*\*p < 0.01; \*p < 0.05

<table><tr><td colspan="3">Table 7. Summary of Hypothesis Test</td></tr><tr><td>H1a:</td><td>Bidders with high budget constraints are more likely to choose an early bidding strategy over opportunistic strategy.</td><td>H1a is supported</td></tr><tr><td>H1b:</td><td>Bidders with high budget constraints are more likely to choose a forward-looking, early bidding strategy over a conservative, early bidding strategy.</td><td>H1b is not supported</td></tr><tr><td>H2a:</td><td>Bidders are more likely to choose an opportunistic strategy over an early bidding strategy when they have large demand.</td><td>H2a is supported</td></tr><tr><td>H2b:</td><td>Bidders more likely to choose an analytical strategy over an early bidding strategy when they have large demand.</td><td>H2b is supported</td></tr><tr><td>H3a:</td><td>Bidders in the online channel are more likely to choose an opportunistic strategy over an early bidding strategy.</td><td>H3a is supported</td></tr><tr><td>H3b:</td><td>Bidders in the online channel are more likely to choose a forward-looking, opportunistic strategy over a conservative, opportunistic bidding strategy.</td><td>H3b is supported</td></tr></table>

H4: Opportunists perform better than others in minimizing the loss-of-surplus.

To test this hypothesis, we develop a hierarchical linear model (HLM) to examine the impact of bidders’ strategic choices on their winning prices. HLM is a popular approach to modeling hierarchically structured data where the lower-level units are nested within higher-level units (Bryk and Raudenbush, 1992). For example, in our case, each bidder had multiple winning bids during the four months (i.e., transactions and bidders are nested), and these bids are likely to be clustered. HLM can help to control for such clustering and produce unbiased estimates of the bidder-level effects (e.g., bidders strategic choices).<sup>20</sup>

Given the institutional characteristics of the DFA, we include three independent variables in the transaction level (i.e., Level 1): LotSize, MinPQ, and Supplier. LotSize refers to the lot size, or the total number of units available in the current auction. According to Mithas and Jones (2007), lot size has significant impact on auction prices. MinPQ denotes the required minimum purchase quantity in the current round. Anecdotal evidence from the DFA suggests that increasing the minimum purchase quantity in a given round can deter many small buyers from participating in the competition and thus affect the winning prices. Supplier is a vector of dummy variables that indicate the supplier of the products offered in the current auction. These dummy variables are used to capture the potential reputation effect (Koppius et al. 2004). In the bidder-level (i.e., Level 2), we include four dummy variables E-C, O-C, A-C, and E-F, which correspond to the bidding strategies characterized in Table 4. The baseline strategy is O-F, the forward-looking, opportunistic strategy.

In order to account for the unobservable confounding effects at market level, we normalized the winning prices on each day with respect to the minimum and maximum prices on that day: if the winning price in transaction j is $P _ { j }$ and the minimum and maximum prices on that day is $P _ { m i n }$ and $P _ { m a x } ,$ respectively, the normalized price is given by $( P _ { j } - P _ { m i n } ) / ( P _ { m a x }$ $- P _ { m i n } )$ Such a normalized price can be directly used as the measure of a bidder’s loss-of-surplus in a given transaction. The full model is specified in Equations (2) through (5).

$$
\begin{array}{l} \text {Level 1:} \hat {P} _ {j k} = \beta_ {0 k} + \beta_ {1 k} \text {LotSize} _ {j k} + \beta_ {2 k} \text {MinPQ} _ {j k} \\ \quad + \gamma \text {Supplier} _ {j} + \varepsilon_ {j k} \end{array}\tag{2}
$$

$$
\begin{array}{r l} \text { Level   2: } & \beta_ {0 k} = r _ {0 0} + r _ {0 1} E - C _ {k} + r _ {0 2} O - C _ {k} + r _ {0 3} A - C _ {k} \\ & + r _ {0 4} E - F _ {k} + u _ {0 k} \end{array}\tag{3}
$$

$$
\begin{array}{l} \beta_ {1 k} = r _ {1 0} + r _ {1 1} E - C _ {k} + r _ {1 2} O - C _ {k} + r _ {1 3} A - C _ {k} \\ + r _ {1 4} E - F _ {k} \end{array}\tag{4}
$$

$$
\begin{array}{l} \beta_ {2 k} = r _ {2 0} + r _ {2 1} E - C _ {k} + r _ {2 2} O - C _ {k} + r _ {2 3} A - C _ {k} \\ + r _ {2 4} E - F _ {k} \end{array}\tag{5}
$$

The dependent variable $\hat { P } _ { j k }$ in Equation (2) denotes the normalized winning price paid by bidder k in transaction j.

As the benchmark, we consider a simple linear model

$$
\hat {P} _ {j k} = \beta_ {0} + \beta_ {1} \text { LotSize } _ {j} + \beta_ {2} \text { MinQPQ } _ {j} + \gamma \text { Supplier } _ {j} + \varepsilon\tag{6}
$$

which does not account for the clustering of observations.

We use the maximum-likelihood (ML) method to estimate the coefficients in the above models. The results are summarized in Tables 8 and 9. The variables S5547, S79520, S80547, and S562450 refer to the supplier dummies.<sup>21</sup>

The first thing to note from Table 8 is that the opportunistic strategy yields a significantly lower price<sup>22</sup> than the analytical strategy and the early bidding strategy. Thus our hypothesis H4 is supported. We also find that both LotSize and MinPQ have a negative effect on price, although the magnitude of this effect is rather small.

Further, we find significant interaction effects between bidding strategies and the two auction design parameters. Specifically, our results suggest that the price paid by forward-looking opportunists (O-F) decreases at a faster rate than the price paid by conservative bidders (E-C, O-C) when LotSize increases. In addition, we can see that early bidders are more sensitive to the increase in MinPQ: the prices paid by these bidders decreases faster when MinPQ increases.

Both Table 8 and Table 9 indicate that there are significant reputation effects. For example, the normalized prices of products from Supplier 5547 and Supplier 80547 are higher than others. At first sight, the existence of such reputation effects might raise concerns about our cluster analysis, because

<table><tr><td>Variable</td><td>Coefficient</td><td>Standard Error</td><td>P-value</td></tr><tr><td>Intercept</td><td>0.3968</td><td>0.0125</td><td>0.0000***</td></tr><tr><td>E-C</td><td>0.0743</td><td>0.0181</td><td>0.0000***</td></tr><tr><td>O-C</td><td>-0.0417</td><td>0.0186</td><td>0.0248*</td></tr><tr><td>A-C</td><td>0.0586</td><td>0.0159</td><td>0.0002***</td></tr><tr><td>E-F</td><td>0.1038</td><td>0.0186</td><td>0.0000***</td></tr><tr><td>LotSize</td><td>-0.0005</td><td>0.0000</td><td>0.0000***</td></tr><tr><td>MinPQ</td><td>-0.0059</td><td>0.0031</td><td>0.0536</td></tr><tr><td>S5547</td><td>0.3788</td><td>0.0056</td><td>0.0000***</td></tr><tr><td>S79520</td><td>-0.4431</td><td>0.0066</td><td>0.0000***</td></tr><tr><td>S80547</td><td>0.4037</td><td>0.0078</td><td>0.0000***</td></tr><tr><td>S562450</td><td>-0.1791</td><td>0.0065</td><td>0.0000***</td></tr><tr><td>E-C: LotSize</td><td>0.0005</td><td>0.0001</td><td>0.0000***</td></tr><tr><td>O-C: LotSize</td><td>0.0003</td><td>0.0001</td><td>0.0187*</td></tr><tr><td>A-C: LotSize</td><td>0.0001</td><td>0.0001</td><td>0.2774</td></tr><tr><td>E-F: LotSize</td><td>0.0000</td><td>0.0001</td><td>0.9998</td></tr><tr><td>E-C: MinPQ</td><td>-0.0155</td><td>0.0055</td><td>0.0051**</td></tr><tr><td>O-C: MinPQ</td><td>0.0115</td><td>0.0048</td><td>0.0161*</td></tr><tr><td>A-C: MinPQ</td><td>-0.0088</td><td>0.0041</td><td>0.0330*</td></tr><tr><td>E-F: MinPQ</td><td>-0.0216</td><td>0.0060</td><td>0.0003***</td></tr></table>

<table><tr><td>Variables</td><td>Coefficient</td><td>Standard Error</td><td>P-value</td></tr><tr><td>Intercept</td><td>0.4507</td><td>0.0061</td><td>0.0000***</td></tr><tr><td>LotSize</td><td>-0.0003</td><td>0.0000</td><td>0.0000***</td></tr><tr><td>MinPQ</td><td>-0.0160</td><td>0.0014</td><td>0.0000***</td></tr><tr><td>S5547</td><td>0.3770</td><td>0.0057</td><td>0.0000***</td></tr><tr><td>S79520</td><td>-0.4417</td><td>0.0068</td><td>0.0000***</td></tr><tr><td>S80547</td><td>0.4068</td><td>0.0080</td><td>0.0000***</td></tr><tr><td>S562450</td><td>-0.1843</td><td>0.0066</td><td>0.0000***</td></tr></table>

if bidders do have preferences over suppliers, this might influence their entering decisions in an auction. However, since the daily auction schedule is randomized, it is highly unlikely that some suppliers’ products would always be auctioned earlier or later than others.

Finally, we compared the performance of the two models. The AIC and BIC values for the hierarchical model are much smaller (-5745, -5604) than the simple linear model (-5476, -5420), indicating that the former achieves a better model fit.

## Discussion

We develop a stable taxonomy of bidding behaviors in the DFA, a clear example of complex B2B markets. Although there are similarities in the empirical characterization of bidding strategies between the B2B and B2C contexts, some of the regularities observed in the B2C context do not carry over to the B2B context. For example, we do not observe any sip-and-dippers (Bapna et al. 2004). To some extent, this can be attributed to the differences in the auction mechanism: in an English auction, we can observe all of the placed bids (both winning and losing bids), whereas in the Dutch auction, only winning bids are revealed. However, given the sequential nature of these auctions, it is still surprising that bidders do not exhibit modified demand reduction (Goes et al. 2010) at auction level (i.e., purchasing a small amount in early rounds and a large amount in a later round). Also, we do not find intermittent strategies documented in Goes et al. (2012). In fact, the majority of the bidders (except for analyzers) tend to bid for only a short time, either at the beginning or toward the end of an auction day (see Table 4).

We examine the underlying drivers of the observed heterogeneity. Our empirical results show that bidders’ strategic choices can be explained by their budget constraints, demand, and channel adoption. Overall, we find that bidders with high budget constraints are more likely to choose an early bidding strategy, bidders with large demand have the tendency to choose an analytical or opportunistic strategy, and bidders using the online bidding channel are more likely to choose an opportunistic strategy. At the outset, this finding is consistent with the results documented in prior literature (e.g., Bapna et al. 2004, Goes et al. 2012). However, our analysis offers a higher level of granularity. In particular, to our knowledge, this is the first empirical study that examines bidders’ strategic behaviors in multichannel B2B auctions.

We further analyze the economic impact of different strategies. Our results suggest that opportunists outperform both analyzers and early bidders in surplus extraction. This differs from the findings from a previous study by Bapna et al. (2004) where participators, who are strategically equivalent to the analyzers in our case, perform best among non-agent bidders in surplus extraction. This difference can be attributed to the nature of auctions and the characteristics of bidders. Specifically, Bapna et al. (2004) examine the Yankee auctions where the market clears only once at the end of a prespecified time period. Therefore, the participators can always revise their bids by closely monitoring the market dynamics during an auction. In the case of the DFA, however, bidders do not know a priori when an auction will end. Besides, we have seen that analyzers are likely to have larger demand than other types of bidders. In most cases, fulfilling the orders from their customers is much more important than getting the products at the lowest possible price.

From the outcome analysis, we also find significant effects of auction design parameters. In particular, we have seen that both lot size and minimum purchase quantity have a negative effect on the winning price, and this effect is moderated by bidding strategies.

## Implications

The findings and results from the current study have important implications for theory and practice. From the theoretical perspective, the identification of the five distinctive strategies in the DFA challenges the conventional view that bidders strategies will converge as they gain experience from participating in the competition repeatedly. Thus it calls for a dynamic view in studying bidding behavior in a complex environment. Additionally, previous research by Goes et al. (2012) has shown that bidders in B2C sequential auctions are more likely to choose intermittent strategies as they gain experience. However, we did not find any bidder following these strategies while bidding in the DFA. This observed discrepancy in bidding strategies underscores the necessity of understanding the fundamental differences, especially in terms of bidders’ incentive structures, between B2B and B2C environments. In this sense, our explanatory model, which maps bidders’ choices of strategies to their business constraints and requirements, provides a useful starting point.

Our findings also shed new light on the declining price anomaly of sequential auctions<sup>23</sup> (McAfee and Vincent 1993; Van den Berg et al. 2001). Currently, the explanations to the declining price trend in sequential auctions can be cast into two broad categories. The first category consists of studies that examine bidder heterogeneity in terms of risk profiles (e.g., McAfee and Vincent 1993) or product heterogeneity (Engelbrecht-Wiggans, 1994) whereas the second category focuses on the informational effect, or learning, in sequential rounds (Jeitschko 1998). Our analysis empirically disentangles the two different effects, suggesting that both bidder heterogeneity and learning can affect the price path in sequential auctions. Specifically, our results suggest that early bidders are likely to be more risk averse and they would rather pay a risk premium to ensure the fulfillment of orders at the beginning of an auction. On the contrary, the opportunists exhibit a certain degree of gambling behavior: in order to acquire the products at the best price, they are willing to trade the opportunity to purchase in earlier rounds for more information about market conditions and opponents’ profiles.

From the managerial perspective, our results provide useful insights to auctioneers in their decision making in the DFA. The auctioneers in the DFA represent the growers. As such, their main objective is to achieve high revenues. Besides, it is also important that they achieve a quick turnaround since flowers are perishable goods. By controlling key auction parameters such as starting prices, minimum purchase quantities, and reserve prices, auctioneers can influence the dynamics of the auctions. Our taxonomy of bidder behavior can be viewed as a micro-segmentation of the market and thus is useful in facilitating the auctioneers to optimize the auction process (Bichler et al. 2010). For example, currently, the lot sizes are determined by the suppliers who have little information about the strategic characteristics of the bidders. Given the significant interaction effect between lot size and bidders strategies, auctioneers should tailor the decision of lot size to the composition of bidder population while taking into account the real-time market dynamics (Ketter et al. 2012). In addition, we have found that early bidders and analyzers as compared to opportunists are more sensitive to the change of minimum purchase quantity. Therefore, auctioneers should think of alternative strategies other than increasing the minimum purchase quantity to speed up the market process. In light of opportunists’ competitive advantage in surplus extraction and their channel usage patterns, auctioneers should also develop effective information revelation policies across different market channels. Finally, the separation of conservative strategies and forward-looking strategies along the day-level entering time (i.e., TOE-D) suggests that there is great potential to customize the daily auction schedule and further improve the total revenue.

## Limitations and Future Work

Our paper bears several limitations that, nevertheless, open up avenues for future research. For example, we do not take into account the potential screening effects when performing the cluster analysis. According to the results from the outcome analysis, if bidders’ entering decisions are conditional on their preferences over suppliers, we might need to adapt the current explanatory model for bidders’ strategic choices accordingly and the implications might be different. Further, we chose to analyze bidders’ strategies at day-level instead of auctionlevel because it helps us to better capture the B2B features of these auctions. However, this makes it difficult to analyze bidders’ strategic changes across different auctions on a given day. For example, we could not see how an analyzer’s strategies evolve. Nevertheless, given the nature of these auctions (i.e., high variation of auction length and only winning bids are visible), we think that the results from such sequence analysis of winning bids might be less useful than in the English type of online auctions.

Another potential weakness is that we have focused on the auctions of a specific type of product when examining bidders’ behavior. In reality, bidders might have to deal with constraints of product complementarity in their bidding decisions. Unfortunately, we do not have access to any data set that consists of transactions across different product groups. We plan to investigate these issues by computational simulations.

Currently, we are building a rich simulation platform, taking into account the strategic patterns of the bidder population and real-world market dynamics. Such a platform will allow us to experiment with alternative auction designs and different information revelation policies. The results from these experiments will provide useful implications to practitioners in B2B markets.

## Acknowledgments

We would like to thank the senior editor, Paulo Goes, for his guidance and support throughout the review process. We also thank the review team and seminar participants at Erasmus University, University of Minnesota, SCECR 2012, and CIST 2012 for their constructive comments and suggestions.

## References

Ariely, D., and Simonson, I. 2003. “Buying, Bidding, Playing or Competing? Value Assessment and Decision Dynamics in Online Auctions,” Journal of Consumer Psychology (13:1-2), pp. 113-123.

Ausubel, L. M., and Cramton, P. 2002. “Demand Reduction and Inefficiency in Multi-Unit Auctions,” Working Paper, Department of Economics, University of Maryland (ftp://cramton. umd.edu/papers1995-1999/98wp-demand-reduction.pdf).

Ba, S., and Pavlou, P. 2002. “Evidence of the Effect of Trust Building Technology in Electronic Markets: Price Premiums and Buyer Behavior,” MIS Quarterly (26:3), pp. 243-268.

Bajari, P., and Hortacsu, A. 2004. “Economic Insights from Internet Auctions,” Journal of Economic Literature (42:2), pp. 457-486.

Bakos, J. Y. 1997. “Reducing Buyer Search Costs: Implications for Electronic Marketplaces,” Management Science (43:12), pp. 1676-1692.

Bakos, J. Y., and Brynjolfsson, E. 1993. “Information Technology, Incentives, and the Optimal Number of Suppliers,” Journal of Management Information Systems (10:2), pp. 37-53.

Bapna, R., Chang, S., Goes, P., and Gupta, A. 2009. “Overlapping Online Auctions: Empirical Characterization of Bidder Strategies and Auction Prices,” MIS Quarterly (33:4), pp. 763-783.

Bapna, R., Goes, P., Gupta, A., and Jin, Y. 2004. “User Heterogeneity and its Impact on Electronic Auction Market Design: An Empirical Exploration,” MIS Quarterly (28:1), pp. 21-43.

Beggs, A., and Graddy, K. 1997. “Declining values and the Afternoon Effect: Evidence from Art Auctions,” The Rand Journal of Economics (28:3), pp. 544-565.

Benoit, J., and Krishna, V. 2001. “Multiple-Object Auctions with Budget Constrained Bidders,” The Review of Economic Studies (68:1), pp. 155-179.

Bichler, M., Gupta, A., and Ketter, W. 2010. “Research Commentary—Designing Smart Markets,” Information Systems Research (21:4), pp. 688-699.

Bryk, A. S., and Raudenbush, S. W. 1992. Hierarchical Linear Models: Applications and Data Analysis Methods, Newbury Park, CA: SAGE Publications.

Carare, O., and Rothkopf, M. 2005. “Slow Dutch Auctions,” Management Science (51:3), pp. 365-373.

Chakravarti, D., Greenleaf, E., Sinha, A., Cheema, A., Cox, J., Friedman, D., Ho, T., Isaac, R., Mitchell, A., Rapport, A., Rothkopf, M., Srivastava, J., and Zwick, R. 2002. “Auctions: Research Opportunities in Marketing,” Marketing Letters (13:3), pp. 281-296.

Che, Y., and Gale, J. 2000. “The Optimal Mechanism for Selling to a Budget-Cnstrained Buyer,” Journal of Economic Theory (92), pp. 198-233.

Devaraj, S., Fan, M., and Kohli, R. 2006. “Examination of Online Channel Preference: Using the Structure–Conduct–Outcome Framework,” Decision Support Systems (42:2), pp. 1089-1103.

Dewan, S., and Hsu, V. 2004. “Adverse Selection in Electronic Markets: Evidence from Online Stamp Auctions,” Journal of Industrial Economics (17:4), pp. 497-516.

Dholakia, U. M., and Sotysinski, K. 2001. “Coveted or Overlooked? The Psychology of Bidding for Comparable Listings in Digital Auctions,” Marketing Letters (12:3), pp. 225-237.

Engelbrecht-Wiggans, R. 1994. “Sequential Auctions of Stochastically Equivalent Objects,” Economics Letters (44:1), pp. 87-90.

Engelbrecht-Wiggans, R. 2000. “Empirical Contributions to the Theory of Auctions or Why Do Real Bidders Bid the Way They Do?,” notes prepared for the TOW Conference on Applied Research Concerning Auctions and Mechanism Design.

Ghose, A. 2009. “Internet Exchanges for Used Goods: An Empirical Analysis of Trade Patterns and Adverse Selection,” MIS Quarterly (33:2), pp. 263-291.

Goes, P., Karuga, G., and Tripathi, A. 2010. “Understanding Willingness-to-Pay Formation of Repeat Bidders in Sequential Online Auctions,” Information Systems Research (21:4), pp. 907-924.

Goes, P., Karuga, G., and Tripathi, A. 2012. “Bidding Behavior Evolution in Sequential Auctions: Characterization and Analysis,” MIS Quarterly (36:4), pp. 1021-1042.

Greene, W. 2008. Econometric Analysis (7<sup>th</sup> ed.), Upper Saddle River, NJ: Prentice Hall.

Herschlag, M., and Zwick, R. 2000. “Internet Auctions: A Popular and Professional Literature Review,” Quarterly Journal of Electronic Commerce (1:2), pp. 161-186.

Jeitschko, T. D. 1998. “Learning in Sequential Auctions,” Southern Economic Journal (65:1), pp. 98-112.

Jeitschko, T. D. 1999. “Equilibrium Price Paths in Sequential Auctions with Stochastic Supply,” Economic Letters (64), pp. 67-72.

Kambil, A., and van Heck, E. 1998. “Reengineering the Dutch Flower Auctions: A Framework for Analyzing Exchange Organizations,” Information System Research (9:1), pp. 1-19.

Kauffman, R. J., and Wood, C. A. 2006. “Doing Their Bidding: An Empirical Examination of Factors that Affect a Buyer’s Utility in Internet Auctions,” Information Technology and Management (7:3), pp. 171.190.

Ketter, W., Collins, J., Gini, M., Gupta, A., and Schrater, P. 2012. “Real-Time Tactical and Strategic Sales Management for Intelligent Agents Guided by Economic Regimes,” Information Systems Research (23:4), pp. 1263-1283.

Koehly, L. 2001. “Choosing the Optimal Number of Clusters in Kmeans Clustering,” a comment, Journal of Consumer Psychology (10:1-2), pp. 102-103.

Koppius, O. 2002. Information Architecture and Electronic Market Performance, Erasmus Research Institute of Management PhD Series, Erasmus University.

Koppius, O., van Heck, E., and Wolters, M. 2004. “The Importance of Product Representation Online: Empirical Results and Implications for Electronic Markets,” Decision Support Systems (38), pp. 161-169.

Kuruzovich, J., Viswanathan, S., Agarwal, R., Gosain, S., and Weitzman, S. 2008. “Marketspace or Marketplace? Online Information Search and Channel Outcomes in Auto Retailing,” Information Systems Research (19:2), pp. 182-201.

Laffont, J., and Robert, J. 1996. “Optimal Auctions with Financially Constrained Buyers,” Economics Letters (52), pp. 181-186.

List, J. A., and Lucking-Reiley, D. 2000. “Demand Reduction in Multi-Unit Auctions: Evidence from a Sports Card Field Experiment,” American Economic Review (90:4), pp. 961-972.

McAfee, R. P., and McMillan, J. 1987. “Auctions and Bidding,” Journal of Economic Literature (25:2), pp. 699-738.

McAfee, R. P., and Vincent, D. 1993. “The Declining Price Anomaly,” Journal of Economic Theory (60:1), pp. 191-212.

McFadden, D. 1973. “Conditional Logit Analysis of Qualitative Choice Behavior,” in Frontiers in Econometrics, P. Zarambka (ed.), New York: Academic Press, pp. 105-142.

Milgrom, P. 1989. “Auctions and Bidding: A Primer,” Journal of Economic Perspectives (3), pp. 3-22.

Milligan, G. W., and Cooper, M. C. 1985. “An Examination of Procedures for Determining the Number of Clusters in a Data Set,” Psychometrika (50), pp. 159-179.

Mithas, S., and Jones, J. 2007. “Do Auction Parameters Affect Buyer Surplus in E-Auctions for Procurement?” Production and Operations Management (16:4), pp. 455-470.

Myerson, R. B. 1981. “Optimal Auction Design,” Mathematics of Operations Research (6:1), pp. 58-73.

Overby, E., and Jap, S. D. 2009. “Electronic and Physical Market Channels: A Multi-Year Investigation in a Market for Products of Uncertain Quality,” Management Science (55:6), pp. 940-957.

Park, Y. H., and Bradlow, E. T. 2005. “An Integrated Model for Bidding Behavior in Internet Auctions: Whether, Who, When, and How Much,” Journal of Marketing Research (42:4), pp. 470-482.

Rothkopf, M. H., and Harstad, R. M. 1994. “Modeling Competitive Bidding: A Critical Essay,” Management Science (40:3), pp. 364-384.

Van den Berg, G. J., van Ours, J., and Pradhan, M. 2001. “The Declining Price Anomaly in Dutch Dutch Rose Auctions,” American Economic Review (91), pp. 1055-1062.

Weber, R. 1983. “Multi-Object Auctions,” in Auctions, Bidding, and Contracting: Uses and Theory, R. Engelbrecht-Wiggans, M. Shubik, and R. Stark (eds.), New York: New York University Press, pp. 165-191.

## About the Authors

Yixin Lu is an assistant professor in the Department of Information Systems and Technology Management at the School of Business, The George Washington University. She received her Ph.D. in Management, with a major in Information Systems, from the Rotterdam School of Management of Erasmus University. She has presented her work in leading conferences and workshops such as the Conference on Information Systems and Technology, the International Conference on Information Systems, Symposium on Statistical Challenges in eCommerce Research, and the Workshop on Information Technologies and Systems. Yixin’s current research seeks to leverage data and analytics to facilitate decision making in complex markets.

Alok Gupta is the Associate Dean for Faculty and Research at the Carlson School of Management, University of Minnesota. He is Curtis L. Carlson Schoolwide Chair in Information Management, and the former chair of the Information and Decision Sciences Department. His research has appeared in several information systems, economics, and computer science journals including Management Science, Information Systems Research, and MIS Quarterly. Alok was awarded the prestigious NSF CAREER Award for his research on dynamic pricing mechanisms on the Internet in 2001, and named an INFORMS Information Systems Society Distinguished Fellow in 2014. He served as a senior editor for

Information Systems Research from 2007–2013 and has been serving as an associate editor of Management Science since 2007.

Wolf Ketter is Professor of Next Generation Information Systems and section head of Business Information Management at the Department of Technology and Operations Management at the Rotterdam School of Management of Erasmus University. In addition, he is director of the Learning Agents Research Group at Erasmus (LARGE) and the Erasmus Center for Future Energy Business. Wolf is also the founder and chair of the Erasmus Forum for Future Energy Business. In 2010, he became president of the Association for Trading Agent Research (ATAR). ATAR organizes the annual Trading Agent Competition (TAC). Wolf is leading Power TAC, a new TAC challenge on energy retail markets. He has served as general chair or program chair of more than 20 international conferences and workshops. His research has been published in various top energy, information systems, and computer science journals such as Decision Sciences, Energy Economics, Information Systems Research, Machine Learning, and MIS Quarterly. He serves on the editorial boards of Information Systems Research and MIS Quarterly. In December 2012, he received the prestigious INFORMS Design Science Award, and in June 2013, he received the runner-up award for the best European Information Systems research paper of the year.

Eric van Heck is Professor of Information Management and Markets and Chairman of the Department of Technology & Operations Management at the Rotterdam School of Management of Erasmus University. His research concentrates on the role and impact of business architectures and digital platforms to tackle complex societal and business challenges. At the moment he is working on digital business and architecture, big data and analytics, digital work, and energy markets. His research is carried out in collaboration with innovative companies and universities in Brazil, China, Europe, Indonesia, and the United States.
