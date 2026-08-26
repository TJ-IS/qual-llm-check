---
otero_id: 5090
otero_key: "7HZXRF8W"
title: "Overlapping Online Auctions: Empirical Characterization of Bidder Strategies and Auction Prices1"
authors: "Ravi Bapna; Seokjoo Andrew Chang; Paulo Goes; Alok Gupta"
year: "2009"
journal: "MIS Quarterly"
doi: "10.2307/20650326"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Overlapping Online Auctions: Empirical Characterization of Bidder Strategies and Auction Prices

Author(s): Ravi Bapna, Seokjoo Andrew Chang, Paulo Goes and Alok Gupta

Source: MIS Quarterly, Vol. 33, No. 4 (Dec., 2009), pp. 763-783

Published by: Management Information Systems Research Center, University of Minnesota

Stable URL: http://www.jstor.org/stable/20650326

Accessed: 20-02-2016 12:24 UTC

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# OVERLAPPING ONLINE AUCTIONS: EMPIRICAL CHARACTERIZATION OF BIDDER STRATEGIES AND AUCTION PRICES $^{1}$

By: Ravi Bapna
Department of Information and Decision Sciences
Carlson School of Management
University of Minnesota
321 19 $^{th}$ Avenue South
Minneapolis, MN 55455
U.S.A.
rbapna@umn.edu

Seokjoo Andrew Chang
School of Business
State University of New York at Albany
1400 Washington Avenue
Albany, NY 12222
U.S.A.
SChang@uamail.albany.edu

Paulo Goes
Department of Management Information Systems
Eller College of Management
University of Arizona
McClelland Hall 430
1130 East Helen Street
Tucson, AZ 85721
U.S.A.
pgoes@eller.arizona.edu

Alok Gupta
Department of Information and Decision Sciences
Carlson School of Management
University of Minnesota
321 19 $^{th}$ Avenue South
Minneapolis, MN 55455
U.S.A.
alok@umn.edu

## Abstract

Online auctions enable market-level interactions or interdependency of outcomes, which were not observed in physical auctions. One such set of interactions takes place when multiple auctions are conducted to sell identical items by an identical seller in an overlapping manner. This research focuses on overlapping auctions, their interactions, and the related impact on bidder behavior. We introduce the notion of auction “overlap” and examine the impact of market-level factors such as the price information revealed from prior auctions, degree of overlap, the auction format, and the overall market supply on a given auction’s price. Despite a competitive setting, we find that, ceteris paribus, English auctions, on average, extract roughly 8.6 percent more revenue per unit than multiunit uniform-price Dutch auctions. We discover that the overlapping auctions attract institutional bidders, who bid in a participatory manner across multiple auctions, and that such bidders exert a downward pressure on auction prices. We find that overlap of an auction with other competing auctions has a significant negative influence on prices, and information about following auctions has a stronger negative influence than information about prior closing auctions. By estimating the expected price difference, we provide practitioners, who have private knowledge of their internal holding costs, a benchmark that can be used in deciding between using overlapping single-unit English auctions and multiunit Dutch auctions.

Keywords: Online auctions, overlapping auctions, Dutch auctions, English auctions, bidding strategies, impact of information on pricing

## Introduction

Internet-based retailing has firmly established itself as a mainstream economic phenomenon, within which online auctions comprise a significant portion of economic activity. Online auctions facilitate web-based matching of buyers and sellers interested in trading in a wide variety of products. By seamlessly connecting traders that are physically apart, online auctions provide the requisite liquidity and thickness for effective dynamic pricing and allocation of goods. In the process, they create economic welfare for both buyers and sellers, with the buyer's surplus estimated to be close to 30 percent of a typical eBay transaction's value (Bapna et al. 2008). Not surprisingly, online auctions have been the focus of significant research initially in IS (Bapna et al. 2001, 2002, 2003a) and subsequently in Economics (for a detailed review, see Bajari and Hortascu 2004).

While much of the online auction research has taken as its unit of analysis a single auction, an interesting and understudied aspect of the current online auction landscape is that, often, multiple auctions are conducted to sell identical items by an identical seller in an overlapping manner. We use the term overlapping auctions to identify a market where there are multiple ongoing auctions for the identical item and these auctions share with each other a nonzero time interval. Overlapping auctions subsume simultaneous auctions as a special case, which have the identical opening time and closing time.

Further, we observe that online auctioneers also experiment with more than one auction format while carrying out a series of overlapping auctions. For instance, we repeatedly observed Mega Club (name changed) $^{2}$ to be using English auctions and Dutch $^{3}$ auctions to sell the identical items at the same point in time. Mega Club's English auctions are defined and run, for the most part, in a manner consistent with the popular and classical (Vickrey 1961) understanding of the term English auctions. In Mega Club, the English auction is a single-unit, ascending price auction in which the bidder with the highest bid wins the item and pays her bid, which is ostensibly an increment higher than the next highest bid. The slight departure from a traditional English auction comes from the technological affordability provided by the online environment. In Mega Club's English auctions, bidders have to use a bidding agent that ratchets up the bid in unit increments up to a pre-specified maximum by the bidder, with the bidder having the freedom to revise the maximum bid itself. This could presumably have implications on bidding behavior and monitoring costs, an issue we will cover in greater detail later in this paper. In a Mega Club's Dutch auction, multiple units, say $N$ , of identical items are offered, the top $N$ bidders win, and all the winners pay the same uniform amount equal to the lowest winning bid.

Figure 1 presents a stylized representation of our very general online auction setting that is characterized not just by a significant amount of overlap but also by the usage of two competing auction formats in the same time horizon. The figure captures the auction activity (start and end times) conducted during a span of 28 days by Mega Club. Each horizontal line represents the duration of an auction, and movement along the vertical dimension corresponds to later starting times. As is evident, during this time period identical items were sold using multiple overlapping English and Dutch auctions.

Much of our line of enquiry in this more general setting reflects the cumulative traditions of online auction research. In traditional auction environments, the allocation of goods, the winner determination, and the welfare of auctioneers and bidders have been studied for different formats of one-time single auctions. However, as pointed out, in today's online environment, buyers have easy access to bid in multiple auctions; prior auction price information is available and multiple auction formats are in use simultaneously. Bidders can easily locate multiple sources for the item they are seeking and can actually participate in multiple auctions by tracking the auctions themselves or by using software agents. In such a setting, we ask the following questions: Do the

![](/api/attachments/7HZXRF8W/fulltext/images/faa0709c5da0aff26eeb2d10a98a27d19492642bb516b7c212a68c3329cce73d.jpg)  
Figure 1. Stylized View of Multiple Overlapping Online Auction Market (MOOAM) for Identical Items in Mega Club

English and Dutch auction yield identical unit prices? Do we observe new forms of bidding behavior when we move the unit of analysis from the auction level to the market level? It is in the area of examining overlap that we push the online auction research agenda further. Does information spill over from a given auction into other overlapping auctions, and if so, what impact does this have on unit prices, controlling for other factors?

With respect to the issue of overlap, our work falls under the emerging theme of competing auctions, a phrase coined by Anwar et al. (2006). If bidders participate in multiple auctions as they are predicted to do (Peters and Severinov 2006), there is a distinct possibility of information spillovers from one auction to another, which in turn creates interesting interdependencies among multiple auctions. The theory around competing auctions draws on some of the early work on sequential auctions (Ashenfelter 1989) and some recent work on auctions with many traders (Peters and Severinov 2006). The latter predicts that for competing auctions, the final price of one auction is affected by the existence of other auctions, and that prices are expected to be uniform across competing auctions. While our setting of multiple auction types occurring in an overlapping fashion is more general than the simultaneous second-price auction setting of Peters and Severinov (2006), our empirical investigation is certainly similar in the spirit as their study. There has also been some limited amount of research that considers multiple mechanisms with a market-level view. For example, Engelbrecht-Wiggans and Weber (1979), Ashenfelter (1989), and McAfee (1993) examine concurrent or sequential auctions. These studies provide insights into how the information revealed from an auction influences other auctions and how the demand stream and risk attitude of bidders drive the prices of simultaneous or sequential auctions. However, these studies have not examined the case of overlapping auctions, where the auctions are not completely simultaneous or exactly sequential. In contrast to overlapping auctions, the sequential auction setting is characterized by uncertainty regarding if and when future auctions will occur. Relative to the overlapping auction scenario, the sequential auction scenario has greater uncertainty not only about supply (of future goods to be sold through future auctions), but also about demand as reflected in the overall level and nature of competition (for instance, in the mix of bidding strategies being used by the competing pool) with other bidders. This subtle but substantive informational difference can be expected to cause shifts in how bidders strategize and in how prices are formed. It should also be noted that in the overlapping setting, bidders in a given auction (henceforth referred to as a focal auction) have access to the outcomes of preceding overlapping auctions which can influence their willingness to pay in the focal auction. This is not possible in simultaneous auctions where only current prices in each of the simultaneously running auctions are available. Furthermore, the prior literature does not consider the case where the environment consists of multiple formats that coexist in the ecosystem. While overlapping auctions need not necessarily be in different formats in the marketplace we study, we observe all the possible cases: overlap between English and Dutch auctions, English and English auctions, and Dutch and Dutch auctions. To fully reflect this environment we introduce the notion of multiple overlapping online auction markets (MOOAM) and examine the impact of market-level factors such as the degree of overlap and the price information revealed from prior overlapping auctions on a given auction's price.

Any theoretical consideration of auction ending price has to take into account the strategic behavior of the bidders. We are motivated to ask if the extant understanding of bidding strategies in online auctions, crafted in the context of individual auctions serving as the unit of analysis, needs to be expanded when one adopts a market-level viewpoint. In the competing auctions literature, Peters and Severinov (2006) show, in the context of competing (but not overlapping) second price auctions, that the equilibrium behavior for bidders is to bid the minimum required bid in the auction that has the current lowest ask. However, there is ample evidence now (summarized in Bapna et al. 2003b, 2004) that real-world online bidders use a wide variety of bidding strategies, and that such auction markets have multiple equilibria. Thus, it is natural to consider whether various forms of bidding behavior, as predicted by Peters and Severinov or other prior work (Bapna et al. 2004), emerge when bidders encounter MOOAM. Having information about multiple sources for identical goods expands the strategic space beyond a single auction to multiple auctions over a larger time horizon. As in Bapna et al. (2004), we use k-means clustering approach to classify bidders. While we replicate Bapna et al. at the individual auction level, we further extend the bidder classification to the market level by considering bidder behavior in multiple auctions of the same item.

In summary, the specific research questions we address are:

1. Do English and Dutch auctions yield equivalent unit prices in MOOAM?

2. Are there new forms on bidding behavior that are evident at the market level across a group of overlapping auctions?

3. What is the impact on unit price of overlap that an auction has with its preceding and following auctions, controlling for mechanism and bidder behavior?

We find that English auctions achieve significantly higher unit price than Dutch auctions, with a difference of approximately 8.6 percent on average. We discover the existence of institutional bidders, who bid large quantities across multiple auctions. In addition, an increase in proportion of bidders using active “participatory” $^{4}$ strategy increases the price in a given auction, while institutional bidding behavior across the auctions decreases the price. Finally, we find that the degree of overlap has a negative impact on the price, and the magnitude of the impact increases with the degree of overlap. We consider more detailed explanations and implications of these findings later in the paper.

In the next section we develop our conceptual model and operationalize variables for mechanism, market, and bidding behavior in the context of MOOAM. We then present our data and conduct some exploratory data analysis, followed by a presentation of our empirical results. We conclude with a discussion of managerial implications and future research,

## Theoretical Foundations and Conceptual Model

To understand the contextual setting that identifies the key competing theories for our research, it is important to understand the difference between sequential, simultaneous, and overlapping auctions. The main sequential auction result (Ashenfelter 1989) in the literature is that prices (of French wines and Australian wool) are observed to decline in subsequent auctions. The key simultaneous or competing auction result (Peters and Severinov 2006) is that when there are no bidding cost and when bidders share a common fixed buying horizon (or ending time), it is an equilibrium strategy for bidders to submit a bid on an auction with the lowest standing bid, and that, if the strategy is followed by all the bidders, prices are expected to be uniform across all auctions. We introduce the notion of an overlapping online auction market and examine whether these results need to be revisited in a more general setting.

In Ashenfelter's (1989) setting of wine auctions, the auctioneer, in anticipation of a price decline, uses a variety of strategies (smaller lots sizes initially followed by larger lot sizes later so bidders would perceive or rationalize the price decline as a quantity discount!) to “disguise this regularity.” This was primarily achieved by introducing uncertainty about future lots. In our overlapping web-based auction setting, with hyperlinks to the auctions for identical objects, this information uncertainty is significantly reduced, but not eliminated (in the extreme case, new information can arise in the non-overlapping period). Information about past and future closing auctions is readily shared, and an existing bidder pool gets split amongst competing auctions. At a very basic level, in contrast to sequential auctions, MOOAM is characterized by increased availability of supply (number of current units being sold through ongoing auctions) and demand (number of competing bidders at the market level) side information. It is also plausible that bidders can infer not just the level of competition, as measured by the number of competing bidders, but also the nature of competition, as exhibited in the bidding strategies of the individuals in the current mix. Thus, if the uncertainty or risk of future item availability is the explanation for price decline in sequential auctions, what can be expected when such uncertainty is reduced, as in the case with MOOAM?

![](/api/attachments/7HZXRF8W/fulltext/images/a1fe92a8e58e8991e464878b7225dc0e0e238669df91a6a16e96f7973b469404.jpg)  
Figure 2. Conceptual Model

At a high level, we postulate that price in a given auction is affected by three broad categories of variables: mechanism, market, and bidding behavior. Figure 2 presents our conceptual model.

The mechanism variable is operationalized by whether the type of auction is English or Dutch. We introduce three market-level variables that have not been studied in the prior literature. We operationalize the factor “preceding overlapping auctions” by a variable called overlap time preceding or OTP. This is measured as the total amount of time the focal auction shares with other auctions for identical goods, which close prior to it (see the Appendix A for formal mathematical definitions of this and all other variables). It captures the amount of time a bidder might be able to evaluate the bids and opportunities in other auctions. To operationalize the “factor following overlapping auctions,” we define overlap time following or OTF as the total amount of time the focal auction shares with other auctions that begin prior to the focal auction’s closure. The factor “market price bound” is operationalized as the lower bound of market price, labeled MinPB. It is calculated as lowest winning price among the previous overlapping auctions of the focal auction. Finally, we distinguish bidder behavior at the auction level and the market level. While more details on the operationalization of these two factors are presented in the next sections, it suffices to say that the auction level bidding behavior follows directly from Bapna et al. (2004), which considers bidders’ entry and exit times in an auction and the number of bid revisions they made as a three dimensional view of bidding strategy. In contrast, the market level view is a new contribution of this research, measuring the number of overlapping auctions in which a bidder participates, total quantity demanded, as well as the bidding intensity across auctions. In the next subsection, we develop hypotheses regarding the effect of these variables on prices of individual auctions.

## Effect of Auction Mechanism

One interesting aspect of MOOAM is concurrent use of both English and Dutch auctions to sell identical items. In such a setting, it is natural to ask what theory implies regarding the revenue equivalence of these two mechanisms, and subsequently explain what is observed empirically. The revenue equivalence theorem states that under the independent private values setting with risk-neutral bidders, all four primary auction mechanisms (English, Dutch, first price, and second price) yield the same expected revenue (Vickrey 1961). Note that in our setting we have to compare English auction with multiunit uniform price auction (labeled on the Internet and in some financial markets as Dutch auction). While there have been many tests of revenue equivalence in laboratory settings, the only known field test of this theory (Lucking-Reiley 1999) finds that the traditional Dutch auction (a descending open auction as pioneered in the Dutch flower markets) produces 30 percent higher revenues than the first-price auction format. Given that the overlapping auction market is characterized by a mix of two different types of auctions (English and multi-unit Dutch) in our study, it is important that we examine the impact of mechanism choice on the unit price of an item.

To theoretically analyze the prices of two auction formats, we trace back to the seminal work of Vickrey (1961). His results established revenue equivalence between the English and second-price sealed bid Vickrey auction, and further that truth-telling is a dominant strategy in second-price sealed bid settings. However, he also cautioned readers that the same truth-telling result does not apply in multiunit uniform price (or Dutch) settings.

In Dutch auctions, one potential cause for concern is demand reduction (see Ausubel and Cramton 1997; List and Lucking-Reiley 2000). This occurs when bidders have multiple unit demand (i.e., they want to buy more than one item). In such cases, Ausubel and Cramton (1997) show that bidders will have an incentive to lower their bids or “reduce their demand” for all but the first unit. This is because the likelihood of becoming the price setting bidder increases with the number of units desired and therefore bidders lower their bids. Vickrey also suggested that if bidders bid for one or more identical goods, the dominant strategy for each bidder is to submit a bid that is equal to his true valuation for the first good but they have an incentive to bid lower than their true valuation for subsequent goods. It is optimal for bidders, who bid on multiple units, to bid their average valuation if they cannot differentiate their bids for different units. Clearly, this induces a downward pressure on the expected revenue from uniform price multiple-unit auctions.

Extant research has yet to establish the equilibrium bidding strategy in the MOOAM context. The closest one comes is Peters and Severinov (2006). In their analysis of second price auctions, and in the absence of bidding costs and infinite buying horizon, they find that bidders should look at the auction with the current lowest asking price, and bid the minimum bid increment there. If this equilibrium strategy is followed by all the bidders, if the market environment is viewed as being perfectly competitive, and if there is no demand reduction, then we can tentatively hypothesize that prices should be equal in both auction formats. However, recall that demand reduction deflates bids if there is multiunit demand and indeed multiunit bidding is allowed and observed (as we will show later). Given the lack of a firm theoretical footing, which we hope will be motivated by our exploratory empirical analysis, we cautiously posit a directionless hypothesis concerning the unit prices from Dutch and English auctions in MOOAM.

H1: In MOOAM, there is no significant difference between the unit prices of Dutch and English auctions.

Next we develop hypotheses about market-level factors that are likely to have an impact on auction prices.

## Effect of Market-Level Information

At the market level, we investigate how the overall market forces induced by the MOOAM structure influence the outcome of individual auctions. While most studies consider the auction mechanism as a single, independent and isolated environment, there is a body of literature that examines the interdependencies of multiple auctions. For example, Engelbrecht-Wiggans and Weber (1979) studied concurrent and sequential markets. They note that multiple simultaneous auctions are different from multiple independent auctions, when bidders have nonlinear utility functions. Only if the value of multiple items is simply the sum of those of individual objects does the independence assumption hold. McAfee (1993) proposed a multiple competing auction problem. He showed that, in equilibrium, auctioneers would use identical auctions with a reserve price equal to the cost. Peters and Severinov (1997) analyzed a similar setting. They argued that when there are multiple competing auctions, the demand and the number of bidders are endogenously determined by the mechanism factors offered by auctioneers. Ashenfelter (1989) observed in auctions of wine that when identical lots of the item are auctioned sequentially, the price decreased over time. McAfee and Vincent (1993) explained the declining price anomaly in sequential auctions in terms of the risk premium. For risk-averse bidders, the price of the previous auction involves the risk premium for subsequent auctions, which decreases the prices of later auctions. Engelbrecht-Wiggans and Kahn (1999) argued that the size of demand plays a crucial role in the prices of sequential auctions. Using the data from cattle auctions, they showed that the price declines in the sequential auctions as the demand reduces. Zeithammer (2006) noted that, if bidders know the availability of future auctions for identical goods, they decrease their bids in the current auction due to the positive expected opportunity cost of waiting.

In an overlapping setting, the existence of other sources for identical goods is, at least partially, common knowledge. Since bidders can easily get the information about the availability of multiple identical items from the website, the outcome of a given auction might be dependent on other auctions, and the overall demand and supply conditions in the market. Our market level variables are created to explicitly analyze the impact of the overlapped time with preceding and following overlapping auctions as well as the price information from previous auctions. A unique aspect of our data is that we observe different degrees of overlap, providing a perfect opportunity to study the impact of varying level of market information during an auction.

Below we construct the hypothesis related to the market level variables.

1. Information from preceding overlapping auctions provides a signal about prior prices that are not available in the case of simultaneous auctions, all of which end at the same time, and whose outcomes are uncertain until they are over. It may also be a surrogate for existing supply in the market; thus an increase in OTP may dilute the bidding pool for the focal auction. Further, given that OTP reflects prior information, it can only serve to truncate the high end of the valuation distribution. These factors combine to lead us to hypothesize

## H2a: Higher levels of OTP in a given auction will lower the realized price in that auction.

2. Information from following auctions gives certain supply side information that has been masked or obfuscated in the traditional sequential auctions literature (Ashenfelter 1989). It also creates an option value and causes bidders to bid less than their true valuation (Zeithammer 2006) because of the positive opportunity cost. Therefore, the higher the OTF, the lower the attention paid by a bidder to a given auction, resulting in fewer bids and lower prices. This leads us to hypothesize

## H2b: Higher levels of OTF in a given auction lower the price realized in that auction.

3. Since MnPB can be observed by the bidders, it may affect the price of the current auction. As this price creates a lower bound on prices, we hypothesize that

## H2c: The price realized in a given auction is positively correlated with observed lower bound on the market price.

We posit that the three market-level variables will explain a substantial amount of variance in prices observed in overlapping auctions. However, bidder behavior and characteristics are also important factors in explaining realized prices. While most of literature assumes that the number of bidders in an auction is exogenously determined, Levin and Smith (1994) argued that the number is stochastic and it is characterized by the seller's mechanism and other market factors. In the context of online auctions, with ease of search, we believe that the bidders' entry and bidding patterns are influenced not only by the given auction's parameters but also by the market level information that is accessible to them.

Following the recent literature in online bidder behavior, we compute, infer, and characterize some variables that capture bidder characteristics. We describe the motivation and process of construction of these variables in next subsection.

## Effect of Bidder Characteristics and Heterogeneity

One of the important contributions of online auction research to auction theory has been the exploration of observed heterogeneous bidders' strategies. In the traditional, face-to-face auction setting, it might have been reasonable to assume that bidders belonged to a homogenous, symmetric, risk-neutral group that adopted Bayesian-Nash equilibrium strategies. Thus the major strategic dimension in traditional auctions was the mapping between an individual's valuation and her bid. In the online environment, heterogeneous bidding behavior is observed due to an increase in the strategic space. This can be attributed to freer entry and exit as search technology makes it easy to find auctions and the emergence of bidding tools such as bidding agents (Bapna et al. 2008) and live updates of auction status. For instance, Easley and Tenorio (2004) presented a theoretical model that demonstrates, when there are nonnegative bidding costs associated with bidding, bidders may use jump bidding strategies instead of ratchet bidding (using participatory strategy). Bidders use the jump bidding strategies to signal their valuations to potential other bidders in the auction, and the size of the jump is related to the competitive condition of the auction. The timing and frequency of bids also play a crucial role in understanding the heterogeneity of real-world bidders' strategies (Bapna et al. 2004; Steinberg and Slavova 2005). We use a similar approach to characterize the different classes of bidders and how their behaviors differ in the two auction formats in our data. We then examine the impact of bidder behavior on the auction price. In addition to the auction specific analysis similar to Bapna et al. (2004) and Steinberg and Slavova (2005), we also consider the bidder behavior across many overlapping auctions in which bidders participate.

To characterize the bidders' heterogeneous entry and bidding behavior on two different levels—individual auction level and the entire market level—we conducted a segmentation analysis based on $k$ -means clustering (as in Bapna et al. 2004). (Refer to Appendix B for more details on this method.) We are motivated to conduct a market-level bidding strategy analysis based on the theoretical prediction of Peters and Severinov (2006). They predict that in a competing auction scenario, the equilibrium bidding behavior calls for bidding in multiple auctions. However, prior to analyzing whether certain subgroups of bidders bid more extensively across multiple auctions, we need to establish the individual auction level baseline of bidding behavior. At the individual auction level (as in Bapna et al. 2004), we deploy three variables, time of entry (TOE), time of exit (TOX) and number of bid revision (NOR). TOE is the time of the first bid and TOX is the time of the last bid of each bidder. At the market level we are interested in observing whether bidders bid across multiple overlapping auctions, the number of revisions they make, and their quantity demanded. To capture the entry and bidding behavior at the market level, we run a second cluster analysis with the following additional variables for each bidder: total number of auctions in which each bidder participated during our data collection period (NOA); average number of bid revisions made during the auctions in which they participated (NOR); and average quantity each bidder demanded in the auctions in which they participated (QNT). NOA captures the auction participation behavior at the market level. Bidders who participate in a large number of auctions tend to have high demand quantity, which can be captured by QNT. NOR is an indicator of how actively they bid in the auctions in which they participated.

Based on this characterization of the bidders, we introduce the following two variables that may have an impact on the price of an auction:

1. Percentage of participants in an auction (%Participator). Prior research (Bapna et al. 2004) on individual auction bidding strategies has noted the presence of participatory or pedestrian bidders, who keep bidding the minimum bid increment in a given auction. More participatory action creates faster movement of prices in an auction and creates a sense of urgency. Therefore, we hypothesize

H3a: A higher proportion of participants in an auction will result in higher prices in that auction.

2. Percentage of institutional bidders (%Institutional). Theory predicts that equilibrium bidding behavior in competing auctions calls for bidding in multiple auctions (Peters and Severinov 2006). In addition, without any constraint on the number of items being bid upon, the literature on demand reduction suggests that multiunit auctions are likely to attract bidders desiring more than one unit of an item. We label such type of bidding behavior, if it exists, as institutional bidders. Based on demand reduction arguments and higher monitoring costs, we conjecture that institutional bidders will be looking for bargains, causing us to hypothesize

H3b: A higher proportion of institutional bidders in an auction will result in lower prices in that auction.

In the next section we describe our data set and present some insights from exploratory data analysis.

## Data Description and Exploratory Data Analysis

Our data was collected from the online auction site of Mega Club. In contrast to other online auction sites such as eBay, our data provides some key advantages to study the impact of overlapping auctions. Specifically, the data do not suffer from seller heterogeneity since there is only one seller in Mega Club auctions. We do not need to control for seller reputation or its unobserved heterogeneous effects. Therefore it creates a controlled environment to study the impact of mechanism, market, and bidder behavior on auction prices in MOOAM.

Using automated scripts, we downloaded auction information including current winner, current price, and remaining time every four minutes to construct a complete data set that includes opening and closing time, bid history, final winner(s), and winning price.

Figures 3 and 4 show the snapshots of an English auction and a Dutch auction for an identical item. Note that the seller also provided the links to the other overlapping auctions, which makes the interaction or interdependency of auctions in MOOAM easier from the bidders' perspective.

![](/api/attachments/7HZXRF8W/fulltext/images/76ff4701a67448b69fba8aa0c5f5d2bb8a05a3c520ed19ab84372640abec9281.jpg)  
Figure 3. Screenshot of an English Auction in Mega Club

![](/api/attachments/7HZXRF8W/fulltext/images/841e7219768de01fdc44bc88f5bedd2377d8f4a5a761e2dc1763313c71b6db2d.jpg)

Figure 4. Screenshot of a Dutch Auction in Mega Club

![](/api/attachments/7HZXRF8W/fulltext/images/d8e1de9753db64954f94773d86645b40aa00c602fa3143220a3e5ad19c9c3bd4.jpg)  
Figure 5. Overlapping Auctions for Item 787694 in Mega Club

![](/api/attachments/7HZXRF8W/fulltext/images/1a4f93fa4bfab6a38b24c15f1ec999aa19c0d5116a5c41d5c55155963cdc17e2.jpg)  
Figure 6. Overlapping Auctions for Item 359002 in Mega Club

<table><tr><td colspan="3">Table 1. The Three Items, Number of Auctions, and the Lot-Sizes</td></tr><tr><td></td><td>Number of Dutch Auctions (Lot Size)†</td><td>Number of English Auctions (Lot Size)</td></tr><tr><td>Item 846752</td><td>21 (3)</td><td>25 (1)</td></tr><tr><td>Item 787694</td><td>17 (2)</td><td>126 (1)</td></tr><tr><td>Item 359002</td><td>6 (3)</td><td>20 (1)</td></tr></table>

$^{\dagger}$ All Dutch auctions for Item 846752, Item 787694, and Item 359002 have the lot-size of 3, 2, and 3 respectively.

Table 2. Descriptive Statistics about Winning Price, Number of Bidders and Auction Duration

<table><tr><td></td><td>Objects</td><td>Mean</td><td>Median</td><td>St. Dev.</td><td>Skewness</td><td>Kurtosis</td></tr><tr><td rowspan="3">Winning price ($)</td><td>Item 846752</td><td>45.83</td><td>43.00</td><td>8.96</td><td>1.07</td><td>2.06</td></tr><tr><td>Item 787694</td><td>188.17</td><td>186.00</td><td>17.97</td><td>1.66</td><td>2.98</td></tr><tr><td>Item 359002</td><td>132.08</td><td>131.00</td><td>25.98</td><td>1.58</td><td>4.60</td></tr><tr><td rowspan="3">Number of Bidders</td><td>Item 846752</td><td>10.35</td><td>10.00</td><td>3.93</td><td>1.49</td><td>8.91</td></tr><tr><td>Item 787694</td><td>8.18</td><td>8.00</td><td>2.62</td><td>1.98</td><td>5.52</td></tr><tr><td>Item 359002</td><td>13.08</td><td>11.50</td><td>6.32</td><td>0.45</td><td>-1.64</td></tr><tr><td rowspan="3">Duration (hr.)</td><td>Item 846752</td><td>25.13</td><td>25.00</td><td>0.36</td><td>0.42</td><td>-0.05</td></tr><tr><td>Item 787694</td><td>22.68</td><td>23.67</td><td>15.46</td><td>0.92</td><td>1.34</td></tr><tr><td>Item 359002</td><td>13.03</td><td>10.08</td><td>8.17</td><td>0.87</td><td>-0.13</td></tr></table>

Figures 5 and 6 show some instances of MOOAM where multiple auctions for the same items were conducted in different manners. Note that unlike Figure 1, the auctions are not evenly distributed. Some auctions are stacked on one day, while some auctions are distributed across multiple days. Therefore, in these instances the degree of overlap among the various auctions for the same item varies significantly.

The items being sold in the Mega Club online auction site include a variety of computers, electronics, and home appliances. While items such as these are subject to declining prices over time, prices are unlikely to decline significantly during the time period of data collection (November–December). We also believe that any price declines caused by factors outside the model are likely to affect both English and Dutch auctions equally. Most of the items are auctioned in either English or Dutch auction format, but on occasion, both auction types are used simultaneously in one series of overlapping auctions for a given item. Table 1 provides a summary of the data we have used in this study. The data comes from 215 auctions for three items: a speaker package (item number 846752), a DVR system (item number 787694), and a home theater set (item number 359002). All three items were offered in MOOAM format using English and Dutch auction types during the period November 22, 2004, to December 18, 2004.

Our data reflects 3,723 bids by 1,986 bidders. Table 2 provides the descriptive statistics for winning price, number of bidders, and auction duration. An examination of these statistics reveals that item 787694 showed lower average number of bidders as compared to the other two items. However, this item was the most expensive among the three items and also had the highest number of auctions. Therefore, the data seem to support the broad microeconomic behavior of demand and supply.

## Mechanism Price Differences

A preliminary t-test for means using normalized prices $^{5}$ reveals that there is a significant difference in prices with English auctions yielding higher prices than the price of Dutch auctions.

Further investigation of the price patterns reveals interesting insights. Figure 7 indicates that the prices in English auctions have a significantly higher variance and more outliers as compared to Dutch auctions. Our conjecture is that this may be

<table><tr><td colspan="4">Table 3. Two-Sample T-Test for Price</td></tr><tr><td>Estimate for Difference</td><td>95% CI for Difference</td><td>t-value</td><td>p-value</td></tr><tr><td>16.46</td><td>(12.89, 20.04)</td><td>9.08</td><td>0.000</td></tr></table>

![](/api/attachments/7HZXRF8W/fulltext/images/7855c9ce267e711424d088005c43e9ad5757ebacea6107f0f42c4df1845cba1f.jpg)  
Auction Type (means are indicated by solid circles)

Figure 7. Boxplots of Price by Auction Type

due to the differences in technology usage: bidders can use a proxy-bidding agent for English auctions but they have to manually revise bids for Dutch auctions. Using the proxy-bidding system, bidders can simply enter the maximum they are willing to pay for the item, and then the automatic bidding agent increases the bid according to the auction progress. However, since bidding in Dutch auctions requires close monitoring and bidding costs, bidders behave much more conservatively, producing a smaller variance and fewer outliers.

A shortcoming $^{6}$ of the multiunit Dutch auction is that bidders with top valuations can make arbitrarily large bids to ensure that they win. To check whether such a behavior was taking place in the auctions that we observed, we also checked the highest bids in two auction types to see if bidders' bid value itself varies across the mechanism types.

Table 4 and Figure 8 indicate the highest bid in English auctions is significantly higher than that of Dutch auctions. Thus the possible bidding behavior of very high bids in multiunit

Dutch auctions to increase winning probability is not observed in our data.

Overall, it appears from the data that the auction mechanism seems to make a significant difference in prices. This is captured using a dummy variable in our model.

## Bidding Strategy Analysis

Recall that at the individual auction level (as in Bapna et al. 2004), we deploy three variables: time of entry (TOE), time of exit (TOX), and number of bid revision (NOR). TOE is the time of the first bid and TOX is the time of the last bid of each bidder. These two variables represent timing and the duration of each bidder's auction participation characteristic. Based on the tie-breaking rule $^{7}$ in Mega Club, some bidders might want to enter early to take the advantage but some bidders tend to enter late to monitor the market and choose the best auction(s). In contrast to Bapna et al., we use the number of bid revisions to capture the bid frequency of each bidder. Since two auction formats have different bidding methods—one is automatic and the other is manual and the bidders can still revise their willingness to pay in English auctions—we believe the NOR is a more reasonable measure than the number of bids. We normalized TOE and TOX to the length of each auction so that the variables have the range [0, 1]. NOR is the actual numeric measure. Using a dissimilarity ratio analysis, we found that k=3 provides the most insightful clustering. The following tables show the three-means clustering results.

<table><tr><td colspan="4">Table 4. Two-Sample T-Test for the Highest Bid</td></tr><tr><td>Estimate for Difference</td><td>95% CI for Difference</td><td>t-value</td><td>p-value</td></tr><tr><td>8.87</td><td>(4.42, 13.32)</td><td>3.95</td><td>0.000</td></tr></table>

![](/api/attachments/7HZXRF8W/fulltext/images/da8151b9f16e21c1585379d2ff9636be73e1801a6ea7a609e43077d176c01f86.jpg)  
Figure 8. Boxplots of MaxBid by Auction Type

<table><tr><td colspan="4">Table 5. Cluster Centroids $^{\dagger}$  (Auction Level)</td></tr><tr><td>Cluster</td><td>TOE</td><td>TOX</td><td>NOR</td></tr><tr><td>Evaluator</td><td>0.213</td><td>0.231</td><td>1.111</td></tr><tr><td>Opportunist</td><td>0.828</td><td>0.829</td><td>1.041</td></tr><tr><td>Participator</td><td>0.623</td><td>0.838</td><td>2.765</td></tr></table>

$^{\dagger}$ Detailed comparison results for TOE, TOX, and NOR of three groups is provided in Appendix C.

We identify three groups of bidders using different entry and bidding strategies. Following the terminology of Bapna et al., we name the bidders who arrive early, make a single bid, and leave, evaluators. The bidders in the second group enter at near end of the auctions, place one bid, and exit. Those are labeled opportunists. Participants stay active for a longer time duration and make multiple bid revisions.

At the market level we are interested in observing whether bidders bid across multiple overlapping auctions, the number of revisions they make, and their quantity demanded. To capture the entry and bidding behavior at the market level, we run a second cluster analysis with the following additional variables for each bidder: total number of auctions in which each bidder participated during our data collection period (NOA), average number of bid revisions made during the auctions in which they participated (NOR), and average quantity each bidder demanded in the auctions in which they participated (QNT). NOA captures the auction participation

Institutional Bidders

<table><tr><td colspan="4">Table 6. Cluster Centroids $^{\dagger}$  (Market Level)</td></tr><tr><td>Cluster</td><td>NOA</td><td>NOR</td><td>QNT</td></tr><tr><td>Individual Bidders</td><td>1.990</td><td>1.354</td><td>1.012</td></tr><tr><td>Institutional Bidders</td><td>14.382</td><td>1.290</td><td>1.868</td></tr></table>

$^{\dagger}$ Detailed comparison results for NOA, NOR, and QNT of two groups is provided in Appendix D.

## Percentage of Auction Level Strategy Adopted by

![](/api/attachments/7HZXRF8W/fulltext/images/c767150bebc44c5e5d291df340013e79255b644421022c296bac4c36014e17ea.jpg)

![](/api/attachments/7HZXRF8W/fulltext/images/091abe9c4d57f53124be62cf5fec75fd025e99d8f53a3dbf25f3fe675f77ff72.jpg)  
Figure 9. Percentage of Participants Is Low in Both Institutional and Individual Clusters

behavior at the market level. Bidders who participate in a large number of auctions tend to have high demand quantity, which can be captured by QNT. NOR is an indicator of how actively they bid in the auctions in which they participated. Based on a dissimilarity ratio analysis, the best clustering occurs with k = 2. The classification resulted in two distinct groups that we identified as individual bidders and institutional bidders, as shown in Table 6.

In addition to the individual auction level strategies we characterize in MOOAM, our extension of bidder strategies at the market level captures the bidding and participation characteristics of multiple auctions. The group labeled as institutional bidders stands out. These bidders participate, on average, in 14 auctions and have a demand of, on average, 2 items.

As an exploratory step, we further investigated any potential linkages between individual auction level and market level bidder behavior. It is worth noting in Figure 9 that both institutional and individual bidders have a small portion of participants. Subsequently, we compared the winning prices of individual bidders and institutional bidders and found that institutional bidders pay less $^{8}$ than the individual bidders. We explore this in more detail in the next section.

## Results and Discussion

To test our hypotheses and analyze the specific impacts of mechanism, market, and bidder behavior factors as presented in the conceptual model of Figure 2, we examine a regression model presented in the equation below. The two dummy variables for product 1 (item 787694) and product 2 (item 359002) capture the product-specific variance for those products, respectively. The dependent variable used in the regression analysis is the normalized price of individual auction, which is calculated as the price premium in a given auction, over and above the lowest auction price for the particular product type Table 7 presents the result.

$$
\begin{array}{r l} \text {Price} _ {i} = & \beta_ {1} + \text {AuctionType} _ {i} + \beta_ {2} \cdot \text {Duration} _ {i} + \beta_ {3} \cdot \text {OTP} _ {i} + \beta_ {4} \cdot \\ & \text {OTF} _ {i} + \beta_ {5} \cdot \text {MinPB} _ {i} + \beta_ {6} \cdot \% \text {Participator} _ {i} + \beta_ {7} \cdot \\ & \% \text {Institutional} _ {i} + \beta_ {8} \cdot \text {Product1} _ {i} + \beta_ {9} \cdot \text {Product2} _ {i} + \varepsilon_ {i} \end{array}
$$

We have to be cautious in interpreting the results from the OLS regression because it is possible that the bidding strategy variables are endogenous. To test for this possibility, we deploy the Hausman test for endogeneity (see Woodridge 2001) by first regressing the two bidding strategy variables on all the exogenous market and mechanism level variables. Next, we predict the residuals from this regression, and regress the original price-premium of our earlier model with addition of the estimated residuals. The Hausman test reveals that while the \%Participators variable is not endogenous, the \%Institutional variable is endogenous (or the coefficient of the added residual is significant). We correct for this and perform 2SLS estimation using an innovative instrument PreSupp–FolSupp defined as follows:

<table><tr><td colspan="6">Table 7. Regression Results $^{\dagger}$ </td></tr><tr><td rowspan="2"></td><td></td><td colspan="2">OLS</td><td colspan="2">2SLS $^{\ddagger}$ </td></tr><tr><td>Price</td><td>Coef.</td><td>Std. Err.</td><td>Coef.</td><td>Std. Err.</td></tr><tr><td rowspan="12">MechanismMarketBidder BehaviorControl</td><td></td><td>15.241*</td><td>2.570</td><td>13.116*</td><td>3.031</td></tr><tr><td>OTP</td><td>-0.309*</td><td>0.118</td><td>-0.332*</td><td>0.123</td></tr><tr><td>OTF</td><td>-0.789*</td><td>0.152</td><td>-0.790*</td><td>0.155</td></tr><tr><td>MinPB</td><td>83.529*</td><td>12.227</td><td>75.182*</td><td>14.929</td></tr><tr><td>%Participator</td><td>40.448*</td><td>11.374</td><td>30.252**</td><td>15.416</td></tr><tr><td>%Institutional</td><td>-16.376**</td><td>6.454</td><td>-36.733***</td><td>20.287</td></tr><tr><td>Product1</td><td>10.927**</td><td>4.339</td><td>17.725**</td><td>7.648</td></tr><tr><td>Product2</td><td>21.829*</td><td>3.449</td><td>21.647*</td><td>3.572</td></tr><tr><td>Duration</td><td>11.611*</td><td>2.696</td><td>11.245*</td><td>2.645</td></tr><tr><td>Cons.</td><td>-52.556*</td><td>7.587</td><td>-43.829*</td><td>10.583</td></tr><tr><td rowspan="2"></td><td colspan="2">R-squared = 0.565</td><td colspan="2">R-squared = 0.544</td></tr><tr><td colspan="2">Adj R-squared = 0.546</td><td colspan="2">Adj R-squared = 0.524</td></tr></table>

$^{\dagger}$ Base product is item 846752.  
$^{\ddagger}$ Instrument variable is PreSupp–FolSupp  
\*Significant at 0.01 level. \*\*Significant at 0.05 level. \*\*\*Significant at 0.10 level.

Definition: PreSupp–FolSupp is the difference between the total number of objects that auctioned in all preceding overlapping auctions and the total number of objects auctioned in all following overlapping auctions (see Appendix A for a mathematical definition).

We choose the PreSupp–FolSupp as an instrument, because while the difference in supply is likely to affect the type of bidders that are drawn to the market, on its own, this variable is unlikely to have any direct linkage with the auction price. A key requirement of an instrument variable is that it influences the endogenous %Institutional variable but has no relationship with the dependent variable. In other words, the instrument variable provides for an exogenous source of variation in the independent variable %Institutional, thereby permitting us to get an unbiased estimate of the coefficients of the model under consideration using two-stage least squares (2SLS). From the regression table above we note that there is no qualitative change in the direction and statistical significance of the parameters estimated from the 2SLS; however, as desired, it removed the endogeneity bias from the actual values of the parameters. This improves the reliability and economic significance of our estimates.

The results indicate that we reject that hypothesis H1 which posits no significant difference between English and Dutch auctions. We find that, all else being constant, an English auction achieves a \$13 (8.6%) price premium over a Dutch auction. This empirical finding has to be viewed in light of the fact that no extant theoretical research definitively guides us to make a prediction about the Dutch auction price being lower than multiple competing English auctions. While Peters and Severinov (2006), albeit in a simpler setting, predict that the law of one price should prevail in competing auctions, the theory of order statistics and potential demand reduction suggests that Dutch auctions should yield lower unit prices. There are also differences in biddings costs associated with the two formats in our environment, an aspect we explore further later in this section. Based on earlier research, we use auction duration as a control variable in regression. Consistent with prior research (Bajari and Hortascu 2003), due to potentially finding more interested bidders, we find that auction duration control has a significant positive impact on the price of a given auction. We view this result as an early empirical finding that should motivate some new theoretical developments of equilibrium bidding and price formation for multiple overlapping auction markets.

With respect to the overlapping effect, we find support for both H2a and H2b that both preceding and following overlap have a significant negative impact on price and new inventory as reflected by OTF has almost twice the price deflating effect of previous overlap. We also find support for hypothesis H2c that the influence of market price signal, as reflected by lower bound of price in previous auctions MinPB, is positive. It appears that bidders pay close attention to price histories. Our results suggest that the price progress of other auctions plays a significant role as an external reference price for the bidders and bidders adjust their bidding strategy by considering previous lows as price bounds. Note that we do not consider the price histories of auctions that have closed prior to the focal auction's commencement and for which price histories are available (and sought). This may further influence the price of the focal auction. In that sense, our estimate of the MinPB coefficient is a conservative one. Overall, this result further strengthens our contention regarding the interdependency of price formation in overlapping auctions.

With respect to bidder behavior, the significant positive sign associated with the percentage of participants indicates support for hypothesis H3a. Active participation of bidders positively correlates with a given auction's price. This can be attributed to increased vigor and intensity of bidding. Contrary to Bapna et al. (2004), the percentage of evaluators does not have a significant impact on price in this generalized overlapping online auction setting. As Zeithammer (2006) argued, the bidders who jump around the auctions monitoring progress or waiting for other opportunities in the future would always bid less than the true valuation because of the positive opportunity cost. It can be expected that as the bidders stay in an auction for a long time, concentrating on the auction without spending the opportunity cost, they place higher bids and this is consistent with the positive sign of the participator ratio variable. Hypothesis H3b is also supported since percentage of institutional bidders is negatively correlated with the price premium. As we conjectured, the bidders in this group are experienced at participating in multiple auctions. Knowing that there are alternate auctions in which they can obtain identical items, they adjust their bids strategically looking for bargains. Note however, that while institutional bidders pay less if they win, their winning probability, as calculated by proportion of winners using a given strategy, is significantly lower than individual bidders (t-value (individual – institutional) = 5.88; p-value < 0.01). This is suggestive of a bargain hunting tendency on the part of the institutional bidders.

We further explore the possible explanations for the price difference between English and Dutch auctions by asking whether these auction formats attract a different mix of bidder profiles. Recall that in the Dutch auction, bidders have to bid manually, whereas in the English auction, they are required to use the proxy bidding agent. We conjecture that the difference in bidding method between English and Dutch auction incurs an auction progress monitoring cost and this is a possible (but not the only) explanation for the price difference. Those bidders that incur the higher monitoring costs in Dutch auctions are able to extract higher relative surplus (lower prices), as would be expected. If we were to consider more generally what would happen if both formats were manual or automatic, then a good place to start is to look at the distribution of bidding strategies as a function of the mechanism. We find, as shown in Figure 10, that there are no significant differences between English and Dutch auctions with respect to the mix of bidding strategies. However, we observe that only 19 percent of bidders are institutional in Dutch auctions as compared to 27 percent in English auctions. This is puzzling given that we established that institutional bidders pay significantly less than individuals. One potential explanation for why bidders keep going to the English auction mechanism can be the auction monitoring cost.

Note that participatory and institutional (monitoring cost intensive) behavior is exhibited in both English (automatic) and Dutch (manual) formats. This suggests that the price discrepancy between the formats is perhaps being driven more by demand reduction and it would be hard to eliminate this purely by equating the intensity of monitoring activity. Clearly, more research is needed to fully explain this phenomenon.

Overall, our results suggest that bidders in overlapping auctions use the signals presented by the market level information and use them in formulating their bids. We also uncover multi-auction strategic bid placement by institutional bidders. In addition, the format of auction makes a difference with English auctions producing higher prices than uniform price multiunit auctions. We elaborate on the managerial implications of these findings in the concluding section.

## Conclusions and Future Research

Using a data set collected from an online auction site, we investigated the revenue equivalence of two different mechanisms, the influence of market forces, and heterogeneous bidder behavior in MOOAM. Our paper builds on the emerging literature on competing auctions (Anwar et al. 2006; Peters and Severinov 2006; Zeithammer 2006). We consider a more general setting of overlapping auctions as opposed to previously studied sequential and simultaneous auctions. Extant research is yet to establish the equilibrium bidding strategy in the MOOAM context, and our empirical analysis motivates the need for future analytical and experimental work to robustly explain the equilibrium bidding strategies and price formation in such settings. While the sequential auction literature (Ashenfelter 1989) observes declining prices in a series of auctions of identical objects, the competing auction literature (Peters and Severinov 2006) predicts that prices can be expected to be uniform across auctions. Our market environment is further colored by the fact that the auctioneer appears to be experimenting with multiple auction formats and varying degrees of overlap to sell identical items.

![](/api/attachments/7HZXRF8W/fulltext/images/92d34d907fed8baab179398d47f6f6705b3c57735c82b5df785faa1fe24f25f0.jpg)

Percentage of Market Level Clusters in  
![](/api/attachments/7HZXRF8W/fulltext/images/96288d1b938018c88e7dd49e9041af306263ba0672dcdf12f03fa9abe87a7f65.jpg)

![](/api/attachments/7HZXRF8W/fulltext/images/403914222a7a4afb07f05b00b03bf921346090a3ec78b0af65639c2dbcc629c0.jpg)  
Figure 10. Bidders Strategies Do Not Vary Across the Auction Types

Our main results address the research questions we posited. We find that, ceteris paribus, English auctions extract roughly \$13 (8.6%) more per unit than multiunit uniform-price Dutch auctions. We find the existence of institutional bidders in the MOOAM environment, who exploit the environment by bidding in large number of auctions. Finally, we find that overlap of an auction with other competing auctions has a significant negative influence, and information about following auctions has a stronger negative influence than information about prior closing auctions. In addition to improving our theoretical understanding of how real-world online marketplaces operate, our results have practical managerial implications.

The consistent difference of about 8.6 percent (\$13 price difference for \$151 average price items) of the average transaction price between English and Dutch auctions has interesting implications for theory and practice. While theory (Ausubel and Cramton 1997) has predicted that demand reduction is to be expected in Dutch auctions, the actual quantification of its adverse impact in online auctions has been lacking. We believe that our research is the first to use a powerful counterfactual, namely the English auction, to quantify the dollar impact of using Dutch auctions. Interestingly, while such outcomes are predictable from the bidders' demand reduction angle, it is arguably at odds from the sellers' point of view. Given the higher lot size of Dutch auctions, it can also be argued that if sellers are repeatedly taking in different unit prices from the Dutch and English auction mechanisms, then these differences, controlling for everything else, can serve as useful estimates of holding costs in equilibrium. Alternatively, sellers with private information on their holding costs could use the estimated price discounts for the Dutch auction to calculate the optimal lot-size they want to use to dispose of their inventory, as well as by extension deciding on the optimal auction schedule that could contain a mix of Dutch and English auctions. We expect future research potential in looking closely at the profitability of seller strategies.

Our establishment of market level bidding strategies is a significant theoretical addition to Bapna et al.'s (2004) taxonomy of online bidding strategies. While Bapna et al. has been replicated at the individual auction level by Steinberg and Slavova (2005), using a data set from a later year, and by Zhong and Wu (2006) in business-to-business settings, other than this research, there has been no advance in taking the taxonomy to the market level. Practitioners can also benefit from a more nuanced understanding of market-level bidding strategies. In addition to the lot size, another significant difference between English and Dutch auctions—one that could account for some of the price difference—is the auction monitoring cost. Practitioners would do well to mitigate the significant negative influence of institutional bidders on auction prices by treating them differently, and perhaps even hosting specialized auctions with higher lot sizes for them. We believe that there is an interesting opportunity for technical IS researchers to lead the development of the next generation of bidding agents that cater to institutional bidders. Such agents would participate and bid optimally across multiple auctions and in the process go beyond the simple proxy bidding agents seen on eBay and Mega Club.

Finally, we believe that we have provided some impetus to the emerging theory on competing (Peters and Severinov 2006) and sequential(Ashenfelter 1989) auctions by empirically testing aspects of this in a more general setting. By conducting a fine-grained analysis of preceding overlap and following overlap, we show their differential impact. We demonstrate that the degree of preceding overlap and price information from previous auctions strongly influences the price of the focal auction. Information from preceding overlapping auctions gives a realized and certain signal about prior prices that are not available in the case of simultaneous auctions, all of which end at the same time, and whose outcomes are uncertain until they are over. Information from following auctions gives certain supply side information and creates an option value and causes bidders to bid less than their true valuation (Zeithammer 2006) because of the positive opportunity cost. To our knowledge, this unpacking of the impact of price and supply-side information has never been demonstrated in the literature and is a major contribution of this research. The degree of this impact is relevant to practitioners looking at making optimal seller entry and auction scheduling decisions in markets such as eBay and Mega Club. While posting of auction listings is not in eBay's control, it is fully controlled by Mega Club. Unless driven by a holding cost, it is not in the sellers' interest to commence their auctions while other competing auctions selling the identical goods are being conducted. Also, practitioners will do well to control the amount of information access they give about prior auction histories, much like expert auctioneers of French wine and Australian wool did in Ashenfelter's (1989) account of the declining price anomaly in sequential auctions. Clearly, the differential impact of price and supply-side information requires further study, including the optimization of this factor since preceding overlap in one auction is following overlap in another.

Based on our results, a fruitful avenue for future work is a generalized market design problem that optimizes the mechanism choice, auction duration, and degree of overlap of multiple auctions. Given that the amount of information transferred across the overlapping auctions is closely tied to the schedule of the auctions, the optimal strategy that determines the overall schedule by controlling the length of liquidation, degree of overlap, and associated operating costs can be investigated.

Our research also suggests that future research should pay closer attention to seller entry decisions in markets such as eBay. Should sellers list their products while other auctions are currently ongoing selling the identical or substitute items? How does seller reputation play a role in this? Should auctioneers limit or encourage cross-bidding activities across auctions?

## Acknowledgments

Alok Gupta's research is supported by NSF Career Grant #IIS-0301239, but does not necessarily reflect the views of the NSF. Ravi Bapna acknowledges the research support provided by the Srini Raju Centre for IT and the Networked Economy (SRITNE), Indian School of Business.

## References

Anwar, S., McMillan, R., and Zheng, M. 2006. “Bidding Behavior in Competing Auctions: Evidence from eBay,” European Economic Review (50:2), pp. 307-322.

Ashenfelter, O. 1989. “How Auctions Work for Wine and Art,” The Journal of Economic Perspectives (3:3), pp. 23-36.

Ausubel, L. M., and Cramton, P. 1997. “Demand Reduction and Inefficiency in Multi-Unit Auctions,” Working Paper, Department of Economics, University of Maryland.

Bajari, P., and Hortacsu, A. 2003. “The Winner’s Curse, Reserve Prices, and Endogenous Entry: Empirical Insights from eBay Auctions,” The Rand Journal of Economics (34:2), pp. 329-355.

Bajari, P., and Hortaçsu, A. 2004. “Economic Insights from Internet Auctions,” Journal of Economic Literature (42), pp. 457-486.

Bapna, R., Goes, P., and Gupta, A. 2001. “Online Auctions: Insights and Analysis,” Communications of the ACM (44), pp. 42-50.

Bapna, R., Goes, P., and Gupta, A. 2003a. "Analysis and Design of Business-to-Consumer Online Auctions," Management Science (49), pp. 85-101.

Bapna, R., Goes, P., and Gupta, A. 2003b. “Replicating Online Yankee Auctions to Analyze Auctioneers’ and Bidders’ Strategies,” Information Systems Research (14:3), pp. 244-268.

Bapna, R., Goes, P., Gupta, A., and Jin, Y. 2004. “User Heterogeneity and its Impact on Electronic Auction Market Design: An Empirical Exploration,” MIS Quarterly (28:1), pp. 21-43.

Bapna, R., Goes, P., Gupta, A., and Karuga, G. 2002. “Optimal Design of the Online Auction Channel: Analytical, Empirical and Computational Insights,” Decision Sciences (33), pp. 557-577.

Bapna, R., Jank, W., and Shmueli, G. 2008. “Consumer Surplus in Online Auctions,” Information Systems Research (19:4), pp. 400-416.

Easley, R. F., and Tenorio, R. 2004. “Jump Bidding Strategies in Internet Auctions,” Management Science (50:10), pp. 1407-1419.

Engelbrecht-Wiggans, R., and Weber, R. J. 1979. “An Example of a Multi-Object Auction Game,” Management Science (25:12), pp. 1272-1277.

Engelbrecht-Wiggans, R., and Kahn, C. M. 1999. “Calibration of a Model of Declining Prices in Cattle Auctions,” Quarterly Review of Economics and Finance (39:1), pp. 113-128.

Levin, D., and Smith, J. L. 1994. “Equilibrium in Auctions with Entry,” The American Economic Review (84:3), pp. 585-599.

List, J. A., and Lucking-Reiley, D. 2000. “Demand Reduction in Multiunit Auctions: Evidence from a Sports Card Field Experiment,” The American Economic Review (90:4), pp. 961-972.

Lucking-Reiley, D. 1999. “Using Field Experiments to Test Equivalence Between Auction Formats: Magic on the Internet,” American Economic Review (89:5), pp. 1063-1080.

Mcafee, R. P. 1993. “Mechanism Design by Competing Sellers,” Econometrica (61:6), pp. 1281-1312.

McAfee, R. P., and Vincent, D. 1993. “The Declining Price Anomaly,” Journal of Economic Theory (60:1), pp. 191-212.

Peters, M., and Severinov, S. 1997. “Competition Among Sellers Who Offer Auctions Instead of Prices,” Journal of Economic Theory (75:1), pp. 141-179.

Peters, M., and Severinov, S. 2006 “Internet Auctions with Many Traders,” Journal of Economic Theory (127:1), pp. 220-245.

Steinberg, R., and Slavova, M. 2005. “Empirical Investigation of Multidimensional Types in Yankee Auctions,” Working Paper, Judge Business School, University of Cambridge.

Vickrey, W. 1961. “Counterspeculations, Auctions, and Competitive Sealed Tenders,” Journal of Finance (16), pp. 8-37.

Woodridge, J. 2001. Econometric Analysis of Cross Section and Panel Data, Cambridge, MA: MIT Press.

Zeithammer, R. 2006. “Forward-Looking Bidding in Online Auctions,” Journal of Marketing Research (43:3), pp 462-476.

Zhong, F., and Wu, D. J. 2006. “E-Sourcing: Impact of Bidding Behavior and Non-Price Attributes,” in Proceedings of the 27 $^{th}$ International Conference on Information Systems, Milwaukee, WI, December 10-13, pp. 1979-1998.

## About the Authors

Ravi Bapna is an associate professor in the Department of Information and Decision Sciences at the Carlson School of Management, University of Minnesota, and the executive director of the Centre for Information Technology and the Networked Economy at Indian School of Business, Hyderabad, India. His research interests are in the areas of online auctions, e-market design, grid computing, and the economics of information systems. His research has been extensively published in a wide array of journals such as Management Science, Statistical Science, Information Systems Research, Journal of Retailing, MIS Quarterly, Decision Sciences, Communications of the ACM, Naval Research Logistics, Decision Support Systems, European Journal of Operational Research, and Information Technology and Management. He serves on the editorial board of the flagship journal MIS Quarterly, as well as for Production and Operations Management. He regularly serves on program committees of major international IS conferences and workshops, and was the cochair of the First International Symposium of Information Systems held at the Indian School of Business.

Seokjoo Andrew Chang is an assistant professor of Information Systems at the State University of New York, Albany. Dr. Chang received his Ph.D. in Information Systems from the University of Connecticut in 2006. His research interests are in the area of economics of information systems. His papers have been presented in major MIS conferences and workshops such as WISE and WITS.

Paulo Goes is the Salter Distinguished Professor in Technology and Management and head of Management Information Systems at the Eller College of Management, University of Arizona. His research interests are e-business, online auctions, confidentiality and security issues, database technology and management, networks, and data communications. Dr. Goes' articles have appeared in Information Systems Research, Management Science, Operations Research, MIS Quarterly, Communications of the ACM, Decision Sciences, INFORMS Journal on Computing, Information Technology and Management, IEEE Transactions on Communications, IEEE Transactions on Computers, and Decision Support Systems, among others. He holds both an M.S. and a Ph.D. in Computers and Information Systems from the University of Rochester (1987 and 1991). Dr. Goes is currently serving as a senior editor for Information Systems Research and as an associate editor for Management Science, Decision Sciences, and INFORMS Journal on Computing. He is a member of the editorial boards of Journal of Management Information Systems, Journal of Database Management, and Production and Operations Management. He was the cochair for WITS 2004.

Alok Gupta holds the Curtis L. Carlson Schoolwide Chair in Information Management and is chairman of Information and Decision Sciences Department at the Carlson School of Management. He received his Ph.D. in MSIS from The University of Texas at Austin in 1996. His research has been published in various top ranked information systems, economics, and computer science journals such as MIS Quarterly, Management Science, Information Systems Research, Communications of the ACM, Journal of MIS, Decision Sciences, Journal of Economic Dynamics and Control, Computational Economics, Decision Support Systems, IEEE Internet Computing, International Journal of Flexible Manufacturing Systems, European Journal of Operational Research, Information Technology and Management, and Journal of Organizational Computing and Electronic Commerce. He was rated among the top 20 IS researchers in the world based on his publication activity as reported in two studies published in 2006. He received the prestigious NSF CAREER award for his research in online auctions in 2001. Dr. Gupta serves on the editorial boards of several academic journals such as Management Science, Information systems Research, Journal of MIS, Decision Support Systems, and Brazilian Electronic Journal of Economics. He also holds the position of publisher of MIS Quarterly, the top rated journal in the field of MIS.

## Appendix A

## Notation, Definitions, and Description of Variables

$$
t _ {i} ^ {o}
$$

<table><tr><td colspan="2">Let  $t_i$  and  $t_j$  denote the opening and closing time of auction i where  $V \in I$  and  $P$  is a set of auctions under consideration. Then we can denote the duration of an auction i as  $d_i = t_i - t_j^o$ . Two auctions  $\{i, j\} \in I$  are said to overlap if  $d_i + d_j \geq \max[t_i, t_j'] - \min[t_i', t_j']$ . Further, if two auctions overlap and  $t_j' \leq t_i'$ , then auction j is a previous overlapping auction for auction i. Similarly, if  $t_j' \geq t_i'$ , then auction j is a following overlapping auction for auction i. Based on these basic relationships, we define the following market level variables:</td></tr><tr><td> $t_i^o$ </td><td>The opening time of auction i where  $i \in I$  and I is a set of auctions under consideration.</td></tr><tr><td> $t_i^e$ </td><td>The closing time of auction i where  $i \in I$ .</td></tr><tr><td>Durationi</td><td>Duration of auction i,  $t_i' - t_j^o$ .</td></tr><tr><td>Overlapping auctions</td><td>When  $d_i + d_j \geq \max[t_i', t_j'] - \min[t_i', t_j']$ , two auctions i and j overlap with each other.</td></tr><tr><td>Preceding overlapping auction</td><td>If two auctions i and j satisfy the overlapping conditions, say,  $d_i + d_j \geq \max[t_i', t_j'] - \min[t_i', t_j']$  and  $t_j' \leq t_i'$ , then auction j is a preceding overlapping auction for auction i.</td></tr><tr><td>Following overlapping auction</td><td>If two auctions i and j satisfy the overlapping conditions and  $t_j' > t_i'$ , then auction j is a following overlapping auction for auction i.</td></tr><tr><td> $OTP_i$ </td><td>The sum of the overlapping time with preceding overlapping auctions for auction i $\sum_{j} \{t_j^c - \max[t_i^o, t_j^o]\}$ where  $d_i + d_j \geq \max[t_i', t_j'] - \min[t_i', t_j']$  and  $t_j' \leq t_i'$  for all j ∈ I and j ≠ i.</td></tr><tr><td> $OTF_i$ </td><td>The sum of the overlapping time with following overlapping auctions for auction i $\sum_{j} \{t_i^c - \max(t_i^o, t_j^o)\}$ where  $d_i + d_j \geq \max[t_i', t_j'] - \min[t_i', t_j']$  and  $t_j' > t_i'$  for all j ∈ I and j ≠ i.</td></tr><tr><td>MinPBi</td><td>Lower bound of market pricemin[Pj] where Pj is the winning price of auction j, which satisfies  $d_i + d_j \geq$  and  $\max[t_i', t_j'] - \min[t_i', t_j']$  and  $t_j' \leq t_i'$  for all j ∈ I and j ≠ i.</td></tr><tr><td>PreSupp–FolSupp</td><td> $\sum_{j} n_j - \sum_{k} n_k$ , where  $n_j$  is the number of objects that are auctioned in any preceding overlapping auction j and  $n_k$  is the number of objects that are auctioned in any following overlapping auction k.</td></tr><tr><td>%Participator</td><td>As in Bapna et al. (2004), we classify the bidders into three disjoint groups: evaluators, opportunists and participants. We analyze how the proportion of the bidders with active participation strategy influences the auction price.</td></tr><tr><td>%Institutional</td><td>Classifying the bidders into two groups based on multi-auction participation behavior at the market level, we analyze how the proportion of the bidders with high demand influences the auction price.</td></tr></table>

## Appendix B

## K-Means Clustering

The k-means clustering algorithm partitions the data points into k disjoint subsets in which the sum of Euclidean distances between data points and the cluster centroid is minimized.

$$
M i n \sum_ {i = 1} ^ {k} \sum_ {n \notin S _ {i}} \left| x _ {n} - c e n t r o i d _ {i} \right| ^ {2}
$$

where i: cluster index

$S_{i}$ : a set of data points in cluster $i$

$x_{n}$ : a data point

centroid: centroid in cluster i

## Appendix C

Two Sample T-Tests for TOE, TOX, and NOR

<table><tr><td></td><td></td><td>Evaluator vs. Opportunist</td><td>Opportunist vs. Participator</td><td>Evaluator vs. Participator</td></tr><tr><td rowspan="2">TOE</td><td>T-Value</td><td>-83.250</td><td>14.840</td><td>-21.640</td></tr><tr><td>P-Value</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td rowspan="2">TOX</td><td>T-Value</td><td>-78.620</td><td>0.940</td><td>-48.480</td></tr><tr><td>P-Value</td><td>0.000</td><td>0.347</td><td>0.000</td></tr><tr><td rowspan="2">NOR</td><td>T-Value</td><td>1.890</td><td>-24.670</td><td>-24.170</td></tr><tr><td>P-Value</td><td>0.059</td><td>0.000</td><td>0.000</td></tr></table>

## Appendix D

## Two Sample T-Tests for NOA, NOR, and QNT

<table><tr><td></td><td></td><td>Individual Bidders vs. Institutional Bidders</td></tr><tr><td rowspan="2">NOA</td><td>T-Value</td><td>-3.330</td></tr><tr><td>P-Value</td><td>0.002</td></tr><tr><td rowspan="2">NOR</td><td>T-Value</td><td>0.680</td></tr><tr><td>P-Value</td><td>0.501</td></tr><tr><td rowspan="2">QNT</td><td>T-Value</td><td>-7.540</td></tr><tr><td>P-Value</td><td>0.000</td></tr></table>
