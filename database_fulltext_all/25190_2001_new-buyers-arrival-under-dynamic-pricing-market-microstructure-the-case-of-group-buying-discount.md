---
otero_id: 25190
otero_key: "4KS6W8TV"
title: "New Buyers' Arrival Under Dynamic Pricing Market Microstructure: The Case of Group-Buying Discounts on the Internet"
authors: "Robert J. Kauffman; Bin Wang"
year: "2001"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2001.11045687"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [York University Libraries] On: 05 March 2015, At: 03:05 Publisher: Routledge Informa Ltd Registered in England and Wales Registered Number: 1072954 Registered office: Mortimer House, 37-41 Mortimer Street, London W1T 3JH, UK

![](/api/attachments/4KS6W8TV/fulltext/images/69313f59772b30211b6668499c08355ffb95e4aed1424c11374ae7ac010b798c.jpg)

Journal of Management Information Systems

Publication details, including instructions for authors and subscription information: http://www.tandfonline.com/loi/mmis20

# New Buyers' Arrival Under Dynamic Pricing Market Microstructure: The Case of Group-Buying Discounts on the Internet

Robert J. Kauffman, Bin Wang Published online: 09 Jan 2015.

To cite this article: Robert J. Kauffman, Bin Wang (2001) New Buyers' Arrival Under Dynamic Pricing Market Microstructure: The Case of Group-Buying Discounts on the Internet, Journal of Management Information Systems, 18:2, 157-188

To link to this article: http://dx.doi.org/10.1080/07421222.2001.11045687

## PLEASE SCROLL DOWN FOR ARTICLE

Taylor & Francis makes every effort to ensure the accuracy of all the information (the “Content”) contained in the publications on our platform. However, Taylor & Francis, our agents, and our licensors make no representations or warranties whatsoever as to the accuracy, completeness, or suitability for any purpose of the Content. Any opinions and views expressed in this publication are the opinions and views of the authors, and are not the views of or endorsed by Taylor & Francis. The accuracy of the Content should not be relied upon and should be independently verified with primary sources of information. Taylor and Francis shall not be liable for any losses, actions, claims, proceedings, demands, costs, expenses, damages, and other liabilities whatsoever or howsoever caused arising directly or indirectly in connection with, in relation to or arising out of the use of the Content.

This article may be used for research, teaching, and private study purposes. Any substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or distribution in any form to anyone is expressly forbidden. Terms & Conditions of access and use can be found at http://www.tandfonline.com/page/ terms-and-conditions

# New Buyers’ Arrival Under Dynamic Pricing Market Microstructure: The Case of Group-Buying Discounts on the Internet

ROBERT J. KAUFFMAN AND BIN WANG

For biographical information on ROBERT J. KAUFFMAN, see the Special Section Introduction.

BIN WANG is a doctoral student in Information and Decision Sciences at the Carlson School of Management of the University of Minnesota. She has a Master of Science in Retail Management from Purdue University, and is a past graduate of Renmin University in Beijing, China. Her research interests focus on electronic commerce, the analysis of electronic marketplaces and the new business models of the Internet, and the applications of theory and methods from marketing science, strategic management, and economics.

ABSTRACT: Dynamic pricing mechanisms occur on the Internet when buyers and sell ers negotiate the final transaction price for the exchange of goods or services. These mechanisms are used in online auctions (e.g., eBay.com, uBid.com) and name-yourown-price (Priceline.com) formats, for example. The current research studies the dy namics of one instance of dynamic pricing—group-buying discounts—used by MobShop.com, whose products’selling prices drop as more buyers place their orders. We collect and analyze changes in the number of orders for MobShop-listed products over various periods of time, using an econometric model that reflects our understanding of bidder behavior in the presence of dynamic pricing and different levels of bidder participation. We find that the number of existing orders has a significant positive effect on new orders placed during each three-hour period, indicating the presence of a positive participation externality effect. We also find evidence for expectations of falling prices, a price drop effect. This occurs when the number of orders approaches the next price drop level and the price level for transacting will fall in the near future. The results also reveal a significant ending effect, as more orders were placed during the last three-hour period of the auction cycles. We also assess the efficacy of group-buying business models to shed light on the recent failures of many group-buying Web sites.

KEY WORDS AND PHRASES: bidding, dynamic pricing, electronic markets, group-buying discounts, Internet-based selling, market microstructure, online retailing, pricing mechanisms.

RECENT YEARS HAVE WITNESSED EXCEPTIONAL GROWTH in the number of online retailers and total consumer expenditures on the Internet. According to Forrester Research, a Cambridge, Massachusetts-based marketing research firm, U.S. consumer online spending will increase to \$71 billion in 2001, a 64 percent increase from the \$45 billion of 2000 [40]. And, even though online retail sales still only accounted for one percent of the total in 1999, more than \$184 billion will be spent by 49 million U.S. households who shop online, increasing the online portion to seven percent of total retail expenditure by 2004 [8]. Clearly, the market is poised for tremendous growth, and the stage is set for electronic commerce on the World Wide Web to play an even greater role in the overall retail economy.

According to Bakos [3], the main function of a market is to facilitate transactions between buyers and sellers based on its institutional infrastructure. Among the various functions of market intermediaries, Spulber [44] argues that pricing to match buyers and sellers is perhaps the most important one. In the traditional retail world, posted prices have been the dominant strategy, leaving buyers with only a take-it-orleave-it choice. However, this widely used pricing mechanism is not necessarily the optimal one. For example, Wang [48] compares posted-price selling with auctions. Under the independent private valuation assumption, Wang finds auctions to be optimal when auction selling costs are zero, or when the seller’s marginal revenue curve is steep. As a result, even if auctions were costly, as long as there is a wide dispersion of buyer valuations, auctions will still outperform posted-price selling.

The previous example shows the advantage of dynamic pricing mechanisms, in which buyers and sellers actively engage in the price discovery process. Because of electronic marketplaces’ability to attract a large numbers of buyers and sellers from different geographical areas and their lower operation costs, dynamic pricing mechanisms, such as auctions, are being used in an ever-broader fashion. Today, traditional dynamic pricing mechanisms serve as the core business models for many Internet-based electronic markets. They include eBay, Amazon.com, and Ubid.com, among many others. Indicative of its attractiveness to consumers in the Internet marketplace, the registered users of eBay increased to 22 million by the end of 2000, and almost 265 million items were listed on their site that year with about \$5.4 billion worth of completed transactions [12]. Other new approaches are also attracting consumers, however. They include dynamic pricing mechanisms such as the name-your-own-price approach of Priceline.com and bid solicitationfrom LiquidPrice.com. Another source predicts that the number of dynamic pricing-enabled transactions will approach 561 billion in 2004, accounting for about 40 percent of all Internet transactions, up from 14.5 percent in 1999 [1]. Clearly, this increase in consumer participation in the price-setting process is a bellwether of the future of Internet-based transaction-making [3, 23].

Recently, two online retailers—first Mercata.com in September 1998, and then Accompany.com (now MobShop.com) in October 1998—began to employ a new type of dynamic pricing model called group-buying discounts. With this approach, consumers can pool their purchase volume together—without any specific efforts made to coordinate their bids—to get a lower price, assisted by the market-making efforts of the online retailer itself. Mercata and MobShop’s innovative business models not only received favorable press reviews [1, 30], but also, once stimulated entry into the group-buying market by AOL and Yahoo! [30]. By spring 2000, the number of group-buying Web sites worldwide had increased to 12 [23]. However, starting from summer 2000, group-buying companies began to struggle for survival, and many would ultimately fail. The combined forces of competition from other online and offline retailers, declining market interest on the part of consumers, a slowing digital economy, and venture capitalists who were reluctant to invest more funds, forced four group-buying firms out of the market and another three to change their strategic focus to software licensing.

Since the group-buying discount-pricing mechanism is still a new phenomenon on the Internet, there have been no studies that have examined the performance of this market microstructure, and the nature of the bidder behavior that can be observed as the market operates. Research on consumer behavior under the group-buying market structure can help both academic researchers and industrial practitioners better understand this new kind of market intermediary, and the efficacy of the market mechanism that it provides to market participants.

The overall purpose of this paper is to study the operation of the group-buying discount market microstructure, and to understand its performance characteristics, in the broader context of declining market interest. We will examine consumers’ aggregate bidding behavior on the MobShop Web site, with reference to a conceptual model for expected bidder behaviors, which is motivated by theoretical perspectives from the study of auctions, consumer behavior, and network externality analysis.

Our primary research questions are:

 Can we build a model with which consumers’ aggregate bidding behavior can be predicted?

 How might the theory on network externalities inform us in our understanding of consumer behavior under the group-buying discount market structure? Specifically, how will the number of new orders placed be influenced by the num ber of existing orders?

 How can the concept of a “price threshold” and consumers’ expectations about future price help us to more accurately model the “price drop effect” that is observed on MobShop?

 As a business model that failed in many cases, how should we understand the efficacy of group-buying discounts? What were the factors behind the failure of the group-buying business model?

There are four primary findings that emerged from our empirical analysis using an econometric model of bidding arrivals, and our qualitative assessment of the groupbuying business models. First, there is a positive participation externality effect in the group-buying discount market microstructure: the number of existing orders has a significant and positive effect on the number of new orders placed during predefined periods of equal duration. Second, we find evidence for an expected price drop effect when the total number of orders approaches the required quantity of the next price tier. This is indicated by more new orders being placed during those periods. Third, our results also reveal a significant market ending effect, as is commonly observed in various auction market settings. In the case of MobShop, more orders appear to be placed during the final time period of the auction cycle. Fourth, we found that the frailty of the group-buying business models are relatively easily identified in terms of their lack of the key elements for sustainable competitive advantage.

## Literature

FOUR RESEARCH STREAMS ARE USEFUL IN INFORMING our exploration of the groupbuying discount approach to dynamic pricing on the Internet and laying the foundation for our theoretical treatment of this new market microstructure. We will first discuss prior work on auction, primarily from the Economics literature, and then we will turn to a discussion of relevant research from consumer behavior in Marketing Science. Next, we consider the role that participation externalities may play in influencing bidder behavior, motivated by recent research in Information Systems (IS) and Economics. We round out our coverage of the literature by examining impact of sustainable competitive advantage on company performance.

## Auction Theory

Economists have extensively studied auctions to understand their properties as a dy namic pricing market structure [e.g., 31, 33, 47]. This work has involved both analytical modeling and empirical testing approaches. The different auction mechanisms studied include the English auction (or ascending-bid auction), the Dutch auction (descending-bid auction), the first-price sealed-bid auction, and the Vickrey auction (second-price sealed-bid auction).

The rapid adoption in the Internet marketplace of online auctions has attracted IS researchers to the study of the application of various kinds of market microstructures, such as these auction formats we just described, in the new context of the Internet. Among the problems and issues that have been examined, developing a better understanding of bidder strategies and bidder behavior has become an especially important issue for study. For example, Bapna et al. [4] analyzed the strategies of online auction bidders and found there are different types of bidders, not all of whom always exhibit rational behavior in value maximization terms. The authors divided bidders into three categories: evaluators, participators, and opportunists. Evaluators are those who know clearly their true valuation of the good and submit high bids at the early stages of the auctions. Participators are bidders who follow the bidding closely and place ascending bids. Opportunists are driven by thoughts of getting bargains—they usually place the lowest possible bids toward the end of an auction. Their research clearly indicates the existence of bargain hunters in the electronic marketplace, which ties closely to the target market of group-buying business models and relates to the failure of many group-buying sites, as we will explain later in our assessment of group-buying business models.

Vakrat and Seidmann [46] found that the number of bidders—or bid density—in an auction is closely related to a number of factors. These include the duration of the auction, the minimum bid increment required, the quantity of items available and the average closing price. Their results suggest that information provided to bidders in online auctions is critical in their decision-making processes. In other research on coin auctions at eBay, Bajari and Hortacsu [2] find higher bidding intensities toward the end of the auctions. In addition, they measure the extent of the winner’s curse and find a 3.2 percent decrease in a bidder’s expected profits with each additional expected bidder. Their results also suggest bidders only enter those auctions that they are likely to win, and they make their decisions to participate based on an expected profit of \$3.20 or higher.

## Consumer Behavior

A second area of relevant research is consumer behavior in the Marketing Science literature. There, we find useful theories that enable us to better understand how bidders and potential buyers view price changes, how their expectations about future prices develop, and how their attitudes toward risk affect their behavior.

Bidder and buyer reactions to prices are especially worthwhile to consider in the context of group-buying discount electronic markets. When exposed to a physical stimulus from the external world, a person may not be able to detect it all of the time. Just as the weight of a feather falling on the hand of a person may not be felt, price changes can also act as stimuli that may or may not be responded to by potential buyers because they are too small. Even though Drakopoulos [9] does not use the term explicitly, he explains the main idea of price indifference thresholds, which refer to the minimum price changes required for consumers to detect the differences. By incorporating a threshold into a demand curve, he proposes that when a price change is smaller than some critical threshold, consumers will not detect the price change. As a result, there will be no impact on demand, though a price change has occurred. Change in demand will only occur when the price change is above the threshold. In our research, we will refer to the related term, price threshold, to indicate proximity in order quantity terms to the quantity-price combination that reflects a drop in price to the lower tier.

Research on consumer behavior has shown that other than the current price, consumers’ expectations about future price can also influence their purchasing behavior. Winer [52] incorporated expected future prices into a household durable purchasing probability model and found that it was significant for the purchasing decisions of color televisions. Krishna [28] conducted an experiment to test the impacts of consumer knowledge about future low price purchase opportunities. He found that consumers who receive announcements about near-term discount sales for large ticket-item purchases are more likely to hold off their purchases until the better prices appear than they would be otherwise.

In research on consumer attitudes related to risk taking, prospect theory emphasizes the context dependencies associated with human risk profiles [45]. In general, individuals’ attitudes toward risk appear to vary considerably across different situations in which buyer behavior can be observed. However, in their study of individual risk preferences, Dyer and Sarin [11] argue that individuals have a relative risk attitude that remains comparatively stable across different settings. According to this measure of individual risk preference, risk attitudes can be quantified along a continuum from risk-averse to risk-seeking. By suggesting a relatively stable risk preference ordering across different settings, the authors differentiate two key factors that help to explain what we observe: preference for the outcome and attitude toward risk. Specifically, when facing an uncertain outcome, a person makes a decision based on her trade-off between the value of the outcome and the risk associated with it, and this decision will be influenced by the individual’s attitude toward risk [39].

## Demand Externalities

The final relevant thread from the literature that will enable us to gain insight into the performance and mechanics of group-buying discounts is the network externalities literature. Network externalitiesoccur when the utility of using a technology increases as the network of adopters expands. They are often observed as being important driv ers of observed adoption behavior, as well as expectations in the market about future adoption, in studies of the diffusion of new technologies [20, 41]. Economides [13] distinguishes two types of networks. Two-way networks include telephone systems, fax machines, and e-mail, where it is possible to distinguish a “direction” of flow in a network, and where users on both ends of a connection can share in the benefits. In these instances, the externalities are direct and users enjoy a broader communication base as more and more people join a given network or adopt a specific technology. One-way networks occur when network components come together to form composite goods. Examples of one-way networks include paging networks and radio broadcasting. The components are the broadcast node and the receiver, in each case, and consumers exhibit demand only for the composite good. With this latter type of network, consumers usually cannot be identified with specific network nodes and the externali ties are indirect, even though they are clearly perceived in the marketplace. We argue later in the paper that group-buying electronic markets are one-way networks.

In both cases, network users derive higher utility from networks with positive externalities. Moreover, network externalities are known to increase an adopter’s willingness-to-pay. The overall effect is that the demand curve for a good or a service will shift, resulting in what are called demand externalities. However, demand externalities are not the same as price change-induced demand. Demand will increase in the presence of lower prices. Demand externalities take effect through the upward shift of demand curves, and the key driver for the increased demand is the higher utility a potential adopter perceives due to the large network size, which in turn results in higher willingness-to-pay. For demand increases due to price decreases, the result is just a simple movement along a demand curve.

Economists have developed a number of analytical models that lead us to an important conclusion for the present research. They typically state the finding in terms of installed base of users, that is, the number of users of product, a service, a software or hardware platform, a technical standard, and so on. Network externalities in the form of current installed base and expected installed base are important factors influencing a potential adopter’s decision to select a product [10]. Results from empirical testing of network externalities in a variety of applied contexts are generally supportive of this installed base theory.

For example, using hedonic price-regression models for computer spreadsheet market, Gandal [17] finds that software packages that were compatible with the Lotus platform at that time were associated with higher levels of consumers’ willingness-topay. Gandal interpreted this result as being indicative of the presence of network externalities. In another study of the spreadsheet software market, Brynjolfsson and Kemerer [6] use a hedonic value model and find that the prices of packaged software “suites” in the mid-1990s were positively related to their installed base of users. In a similar vein, Economides and Himmelberg [14] report that network externalities sped up adoption in the market for fax machines early in the 1990s. Kauffman et al. [26] also test network externality theory in electronic banking. Using a model that charac terizes expected durations of firm adoption of a network, the authors found that banking firms that have a higher expected effective network size tended to be earlier adopters.

Taken together, the perspective that emerges from this literature can inform our understanding of the performance of Web sites that provide group-buying discount auction markets. This is because the essence of the perceived success of such a market by participants who wish to buy the goods it sells is the installed base of bidding participants. Without their participation, there would be no critical mass of interest that would serve to drive prices to lower and lower levels, benefiting all participants in the process.

## Sustainable Competitive Advantage

The strategic management literature has long recognized the importance of competitive advantage on firm performance [e.g., 5, 36]. Competitive advantage, which results from a firm’s unique capabilities and resources according to Wernerfelt [51], enables it to deliver superior value to its customers at lower costs than its competitors. In order to obtain long-term profitability, however, competitive advantage has to be sustainable [36]. Barney [5] identifies four necessary conditions for a capability or resource to be a source of sustainable competitive advantage.

1. It has to be valuable.

2. It has to be rare among a firm’s competitors.

3. It has to be imperfectly imitable, which presents to a firm’s competitors with barriers to entry.

4. There should not be any strategically-equivalent substitutes available for this capability or resource.

Since competition, based only upon price, frequently lead to price wars and lower profitability, strategists such as Porter [37] and Slater [43] tend to emphasize a firm’s ability extracting price premiums by providing superior value to customers.

With intensified competition, lower barriers to entry, and higher buyer bargaining power, the Internet marketplace poses companies great challenges, according to Porter [37]. He argues that many DotComs targeted investors’ initial “blind faith” and lack of investing savvy to extract capital from the financial markets. The “gold rush” was on, and many naïve stock prospectors were drawn into the euphoria of a yet-toburst financial market bubble, expecting the halo effect of the DotCom marketplace to buoy the value of their e-commerce company investments. With the subsequent failure of many DotComs and a discernible diminution in the attractiveness of Internet-only business models, however, the focus has now shifted to long-term profitability and how these firms can achieve sustainable competitive advantage. Porter [37] posits that, instead of competing only on the price, the most successful DotComs should now begin to charge higher prices for the enhanced value they create for their customers. For Internet-based retailers, a loyal customer base and sustainable competitive advantage that can lead to long-term profitability become even more important, since switching costs are low on the Web and customer loyalty is somewhat diminished [38].

We now turn to a more in-depth discussion of the mechanics of group-buying discounts on the World Wide Web. As we reveal the features of a representative Internetbased group-buying Web site and discuss their implications relative to the four literatures that we have discussed, the basis for a conceptual model that can characterize observed bidder behavior and the performance of the market as a whole will become apparent.

## Research Context

IN THIS SECTION, WE FIRST WILL REVIEW the overall development of group-buying business models from 1998 to 2001, then we will focus our discussion on the specif ics of MobShop’s version of group-buying. This will effectively set the context for the empirical modeling and econometric analysis that will follow.

## The Rise and Fall of Group-Buying Business Models on the Internet

Volume discounts have been used widely in many offline buying clubs, such as CostCo and Sam’s Club. But bringing volume discounts to the Internet is a fairly recent phenomenon. The two DotCom pioneers of group-buying on the Internet—Mercata.com and MobShop.com—combined volume discounts with a popular and readily understood dynamic pricing mechanism, and launched group-buying Web sites in May 1999 and March 1999, respectively. By allowing retail buyers to aggregate their purchases and to obtain lower prices, the firms pioneering the group-buying business models tried to deliver “savings in numbers” to their customers.

Group-buying has been shown to be appealing to retail buyers in two respects. First, it is possible (though never certain) that the final price paid will be lower than the purchase price for the same items at other posted-price retailers, resulting in savings for the consumer. Second, group-buying gives buyers a “sneak peak” at the internals of volume discounting, and the feel that they are actually haggling with suppliers and wielding the power of aggregate purchasing [32]. Because of the lower price buyers can obtain as the size of the buyer group grows larger, consumers have the incentive to recruit other consumers, resulting in relatively lower customer acquisition cost for the retailer. Although other retailers emphasize the facilitation of searching for best prices and sale items that offer the right features, the group-buying Web sites provide tools for their customers to seek out other new customers, to add to the power-buying pools.

In their early stage of development, Mercata and MobShop were able to attract a significant market following. Mara [30], for example, reported that Mercata’s largest buying groups had more than 10,000 participants. MobShop, meanwhile, registered significant early successes. For example, using our data collection agent we observed MobShop accumulating 1,000 orders for the Palm V PDA in just one-and-one-half days in spring 2000. Mercata and MobShop’s initial success also motivated the entry of other group-buying firms into the electronic marketplace.

The twelve group-buying firms that were in operation by early 2000 were primarily based in the United States—just a couple operated in Europe. They included Mercata.com, Accompany.com (which later changed it name to MobShop.com, www.mobshop.com), actBIG.com (now Etrana.com, www.etrana.com), C-Tribe.com, DemandLine.com (www.demandline.com), OnlineChoice.com, PointSpeed.com, SHOP2gether (www.shop2gether.com), VolumeBuy.com (www.volumebuy.com), Zwirl.com (www.zwirl.com), and Let’s Buy It (www.letsbuyit.com) and CoShopper.com (www.coshopper.com) in Europe [23]. The products and services offered on these Web sites range from the sale of computer hardware, electronics, and office supplies, to offline retail gift certificates, vacation packages, telephone services, and electricity. Their customers included consumers, businesses, education market, and even government agencies.

Starting from summer 2000 and paralleling the slowing digital economy, groupbuying firms started to experience fierce competition, declining market interest, lower margins because of higher prices from their suppliers, and increasingly reluctant venture capitalists. Four companies—Mercata, C-Tribe, OnlineChoice, and PointSpeed— were forced out of the market, and another three—MobShop, actBIG, and Zwirl—changed their strategic emphasis to software licensing. Those that are still in existence are struggling to survive. For example, Europe-based Let’s Buy It filed for bankruptcy in December 2000, and was able to resume its operation in February 2001 after an additional round of successful funding [29]. However, the limited number of orders on their site reveals that the company faces a daunting task to ever achieve profitability.

## MobShop.com

When MobShop launched its beta Web site in March 1999, its founders were motivated by the idea of being a unique intermediary between consumers and businesses that could accumulate “collective bargaining power” for consumers. The basic business model, then, was to create an “e-shopping club.” Even though MobShop’s busi ness model was widely touted as being “innovative and pioneering,” a number of analysts also pointed out that the company faced the problem of consumer acceptance and achieving critical mass in buyer participation [27].

To answer the research questions we initially laid out in this article, it is appropriate for us to look closely at some of the details of this company’s group-buying market mechanism. We also need to identify the salient aspects that are likely to require special consideration in the development of a model that predicts bidder behavior. Before a product is put up for sale on MobShop’s Web site, fixed starting and ending times must be determined for the selling process. This is similar to what occurs in a call-market microstructure in the financial markets [15]. The period during which consumers can purchase the product on MobShop’s Web site is called an auction cycle. As the number of units sold in a MobShop auction cycle increases, the price of the product will drop according to a predetermined dynamic pricing strategy.

The most eye-catching feature of a MobShop auction cycle Web page was the price trajectory histogram. Figure 1 shows a typical price trajectory histogram that a consumer will see when she goes to MobShop to examine what is going on with an auction cycle for the sale of a product. This graphical display shows how the price decreases according to the number of units that will be sold, as well as the current price that has been achieved, based on the extent of bidder participation. In the case of the Olympus C-2020 Zoom digital camera that is offered for sale in Figure 1, there are five discrete price levels. The highest one is the manufacturer’s suggested retail price (MSRP) at \$829. Below MSRP is the starting price for the item on the MobShop Web site of \$615.95. As the number of orders received by the company changes in the range of 1 to 25, the price remains the same. However, when the number of orders reaches 26, this drives the price that everyone will pay down to the next lower tier at \$605.95. As the number of units sold further increases, the price will change according to the quantities specified in the x-axis of the graph, reaching a low point at \$575.95, if between 501 and 1,001 buyers choose to participate.

When the current price is higher than a buyer’s willingness-to-pay, she can also “Save a Spot” at a lower price level that indicates her reservation price. This way, the consumer will only be added into the buyer group when the total number of purchasers is large enough to drive the price down to her reservation price. The auction cycle continues until it reaches the ending time or a prespecified maximum number of selling units, whichever comes first. After the auction cycle closes, all buyers will be charged the same low final price even if some placed their orders earlier at higher price levels.

We observe a number of interesting aspects of MobShop’s market microstructure that deserve comment in advance of the specification of our predictive model for bidder behavior:

1. Bidder participation matters in aggregate. The extent of bidder participation drives the resulting price levels that are obtained in the market, and, as a result, bidder participation also will determine the welfare benefits that this virtual one-way network [13] can confer upon its users. Quite clearly, this is a network externality effect.

![](/api/attachments/4KS6W8TV/fulltext/images/d7263955c8b9f2c4cdef6db6f87d568f964c397fc01154fcc01620358bb2b04d.jpg)  
Figure 1. Price Trajectory Histogram of a Digital Camera Auction Cycle at MobShop.com

2. Bidders enter orders partly based on expected market outcomes. The extent of bidder participation, which we think of as the bid density for a given auction of a sale item, is also likely to be hard to predict. Bidders have no means to coordinate their bids at the various price levels. Nor is there any publicly available information about bidder-specific reservation prices. Nevertheless, one thing is clear: the lower that the price goes, the more bidders’reservation prices will have been reached or approached, resulting in a greater aggregate willingness in the marketplace to lodge new orders of the same item with MobShop.

3. Price thresholds may influence bid timing. In this context, bid timing or order timing will be an especially important consideration. The closer the market comes to reaching a price threshold, based on the quantity of orders, the greater the impetus will be for bidders whose reservation prices are at the next lower price tier to lodge their own orders.

## The Basic Model

WE NEXT OFFER A MORE FORMAL INTERPRETATION of the market microstructure that we observe at MobShop. The purpose of this discussion is to formulate the basis for a predictive model of bidder behavior, and to provide a means for assessing the performance of the market.

## Preliminary Modeling Considerations

Based on the preceding discussion of the theoretical literature and the MobShop market microstructure, we include the following considerations in the development of our model for bidder behavior:

 the extent to which bidder behavior is subject to demand externalities via the number of bids that are received over time at the MobShop Web site,

 the relationship between price thresholds and the manner in which demand is expressed through additional bids, and

 the impact of the prespecified closing time for bids to be made on a sale item at MobShop.

For the purposes of the present study, we pragmatically view each auction cycle as being divisible into equal-length time intervals of convenient duration. The auction formats that we will include are all four-day auctions. Because of the limited number of new orders received when one-hour intervals are used, we selected three-hour equal-length time intervals as our unit of analysis. Within these intervals of time, we can observe the number of new orders that are placed. In the discussion that follows, we will propose a model with which new orders that occur at a given point in time can be predicted. We now turn to those elements of a theory that can make such prediction possible in the context of group-buying electronic markets.

## Demand Externalities

Based on Economides’s [13] classification, the group-buying marketplace that MobShop offers on the Internet can be thought of as a one-way virtual network. Why is this the case? Because buyers in the group do not benefit directly from others in the same group. Instead, they benefit indirectly due to MobShop’s pricing policy: the participation of more buyers drives down the price for any buyer at the close of the market. Based on prior research on network externalities that we discussed earlier in this paper, we thus expect that the current group size, operationalized by the number of orders, will influence the purchasing decision of a potential buyer. However, unlike previously studied networks that had no specific time frames, the current groupbuying network only exists within the length of the auction cycles. As the end of the auction cycle approaches and potential buyers realize the limited possibility of network expansion, the influence of the current group size on their purchasing decisions may become limited. As a result, we expect to observe a nonlinear relationship between the current group size and the number of new orders placed. We can use the natural logarithm of the sum of the total units sold until period t – 1 and 1 to model this relationship.

## Price

The relationship between demand and price has been long recognized in the microeconomics literature. Even though different functional forms have been proposed for the demand-price relationship, there is a consensus that at the aggregate level demand for a product or brand decreases as the price increases under both monopoly and competitive settings [42]. As a result, we expect that there will be a higher demand when the price drops in the group-buying context. However, we remind the reader that this demand curve effect differs from demand externalities. The former is a movement along a single-demand curve. The latter emphasizes the role of expectations in decision-making and exists by the construction of the group-buying market microstructure. Demand externalities are realized through the upward shift of the demand curve due to potential adopters’higher willingness-to-pay. As a result, in the context of group-buying, a price effect is reflected in an increase in orders due to a price drop, while demand externalities are associated with the current group size. Thus, when the current group size increases, demand externalities capture the fact that potential buyers are more likely to place an order due to the expected larger final group size, even though the current price remains the same.

## Price-Level Effect

In the group-buying situation, as the number of units sold increases within the same price-tier, the point of a price drop comes ever closer. However, consumers may not form the expectation of a price change until the number of orders needed to reach the next lower price level is smaller than some threshold. Moreover, as the price level span (i.e., distance in minimum required number of orders from one price tier to the next) increases, this threshold may also increase.

For example, let us look at Figure 1 again. At price level \$605.95, where the total number of units sold can range from 26 to 200, a consumer may start to form the perception that a price drop is very likely to occur when just 25 orders are needed to reach 201. At the \$595.95 level, however, where this price ranges over 300 orders (i.e., from 201 to 500 orders), the threshold for the same consumer to begin to form the expectation that a price drop will occur may be larger than 25. Obviously, there are fairly complex cognitive and perceptual aspects associated with this kind of market microstructure that deserve closer scrutiny.

Under group buying, when a buyer develops an expectation that the price will drop in the near future, we expect that her likelihood of purchasing the product will increase. However, her expectation of a price change itself will not be sufficient for the buyer to make the purchasing decision. Instead, her reservation price and attitude toward risk will also play important roles.

In the short run, because the price will only drop to the next lower price tier, a consumer will only be motivated to make a purchase when her reservation price is less than the current price, but greater than or equal to the next lower one. (We note that consumers having reservation prices higher than or equal to the current price are expected to have placed their orders already.) In this case, when the price drops to the next level, which is no greater than her reservation price, she will get a nonnegative surplus from this purchase. In the group-buying setting, when an individual perceives that the price is likely to drop to her reservation price or lower—and her purchase action can facilitate this process—she is more likely to place the order if she is riskseeking. On the contrary, a risk-averse person may wait until the price actually changes to make the purchase, even if she expected that the price would change.

As a result, we expect more orders to be placed right before and right after the price drop point. This may occur due to the purchases made by risk-seeking consumers before the price change, and by risk-averse buyers after the price change. Figure 2 shows the expected result of one price level.

## Cycle-Ending Effect

There are two sources of the cycle-ending effect. First, because buyers are able to place conditional bids at MobShop, it is possible that there will be a surge in the number of new orders if the price happens to decrease during this last auction period. This is essentially a “limit order” effect, where transactions will only be carried out conditional on some preset criteria [19]. These newly revealed orders would be added into the final buying group and result in a significantly higher number of orders placed during the last period than might otherwise be expected if no conditional orders were permitted.

A second alternative explanation for the auction cycle-ending effect is also worthy of discussion. When there is a time constraint imposed in a trading market, the market participants’behavior may be influenced both by the start time and by the end time of the trading session. In fact, it is possible that the auction-ending effect may be even more apparent in online auctions, where bidders bid more frequently near the end in order to win the auction, often paying too high a price. The empirical results of Bapna et al. [4] show that opportunists in auctions often select the strategy of bidding the lowest possible prices at the end of auctions. In addition, Bajari and Hortacsu’s [2] empirical test of eBay coin auctions also suggests higher bidding intensities at the end of the digital auctions. In the group-buying setting, when an auction cycle approaches its end, the ending price will become easier for participants to predict and consumers’ uncertainty should concomitantly decrease. Potential buyers, who have been waiting for the final price to become clearer, may make their purchase decision at that time. Moreover, MobShop’s e-mail reminder service, which notifies a potential buyer of the approaching end of an auction cycle, further creates the possibility of additional orders flowing in during the last auction period, since existing bidders who hope to acquire a sale item at a lower cost will have an increased monetary incentive to seek out other buying partners. As a result, we expect more new orders to occur when an auction cycle approaches its end.

## The Dependent Variables

The same set of independent variables is used to predict two different dependent variables. The first one is NewOrders , which is the number of new orders arriving during period t. However, many new orders placed just before a price drop occurs may be the result of previously-submitted limit orders that have accumulated. So using NewOrders as the dependent variable may artificially amplify the before-price drop effect. To correct for this problem, we use a second dependent variable NewOrders <sup>l</sup>, which eliminates the number of new orders due to conditional bidding using the “Save a Spot” feature. This gives us a more conservative estimate of the before-price drop effect.

![](/api/attachments/4KS6W8TV/fulltext/images/db248286ca03a2f65b41dd6cf6d640d1d706c11b032301429053c3c9aa6ca7c1.jpg)  
Figure 2. Expected Price-Level Effect. Note: $Q _ { i }$ and $Q _ { i + 1 }$ are the starting and ending total order quantities for price tier i. We expect more new orders right before and after price changes at $Q _ { i }$ and $Q _ { i + 1 }$ and fewer new orders in other periods.

## The Base Models

Based on our analysis in the previous sections, we specify our base model of bidder participation in terms of new orders received by MobShop in period t as

$$
\begin{array}{c} N e w O r d e r s _ {t} = f   [ \ln (O r d e r s _ {t - 1} + 1),   P r i c e _ {t - 1},   B e f o r e D r o p _ {t - 1}, A f t e r D r o p _ {t - 1}, \\ E n d _ {t}, T i m e o f D a y C o n t r o l s ], \end{array}
$$

and our base model of bidder participation in terms of new orders received by MobShop in period t after eliminating limit orders as

$$
\begin{array}{c} N e w O r d e r s _ {t} ^ {l} = f \left[ \ln (O r d e r s _ {t - 1} + 1), P r i c e _ {t - 1}, B e f o r e D r o p _ {t - 1}, A f t e r D r o p _ {t - 1}, \right. \\ E n d _ {t}, T i m e o f D a y C o n t r o l s ]. \end{array}
$$

The variables used in our empirical model are defined in Table 1. We will comment more fully on the specification of the Time-of-Day Controls dummy variables in the next section.

## Data Issues and Model Refinements

WE NEXT DISCUSS DATA COLLECTION FROM MobShop, and a number of data issues that led us to make refinements to our basic model.

## Data Collection from MobShop

A data-collecting agent, similar to the Electronic Data Retrieval Intelligent LexicaL Agent (eDRILL), proposed and tested by Kauffman et al. [25], was used to collect data from MobShop in March and April 2000. Automated data-collection techniques of this sort make it possible to conduct research and develop research designs that were hitherto impossible to implement, either due to costs, the availability of human data collection agents, or the overall volume of data to be collected [24]. The function of our data-collecting agent was primarily to monitor the MobShop Web site on an hourly basis, and to record the arrival of bids and other related auction cycle information for the sale of Olympus C-2020 Zoom Digital Cameras. Each auction cycle length was four days long and data were collected on an exploratory basis for seven different auction cycles. Table 2 summarizes the descriptive statistics for our data.

Table 1. Definitions of Model Variables

<table><tr><td>Variable</td><td>Definition</td></tr><tr><td colspan="2">Dependent Variables</td></tr><tr><td> $NewOrders_t$ </td><td>Number of new orders placed in period  $t$ </td></tr><tr><td> $NewOrders_i$ </td><td>Number of new orders placed in period  $t$  after eliminating limit orders</td></tr><tr><td colspan="2">Independent Variables</td></tr><tr><td> $ln(Orders_{t-1}+1)$ </td><td>Natural logarithm of the total number orders placed up to the end of period  $t-1$  plus 1</td></tr><tr><td> $Price_{t-1}$ </td><td>Price at the end of period  $t-1$ </td></tr><tr><td> $BeforeDrop_{t-1}$ </td><td>1, if percentage of orders needed to the next price tier at the end of period  $t-1 \leq 25\%$ , 0 otherwise</td></tr><tr><td> $AfterDrop_{t-1}$ </td><td>1, if percentage of orders needed to the next price tier at the end of period  $t-1 \geq 75\%$ , 0 otherwise</td></tr><tr><td> $End_t$ </td><td>1, if current period is the last one for the auction cycle, 0 otherwise</td></tr><tr><td>TimeofDay</td><td>The variables are as follows:</td></tr><tr><td>Control</td><td> $T_1 = 1, 12:00 \text{ A.M. to } 3:00 \text{ A.M.}$ </td></tr><tr><td>Dummy</td><td> $T_2 = 1, 6:00 \text{ A.M. to } 9:00 \text{ A.M.}$ </td></tr><tr><td>Variables</td><td> $T_3 = 1, 9:00 \text{ A.M. to } 12:00 \text{ P.M.}$ </td></tr><tr><td> $(T_1,...,T_7)$ </td><td> $T_4 = 1, 12:00 \text{ P.M. to } 3:00 \text{ P.M.}$  $T_5 = 1, 3:00 \text{ P.M. to } 6:00 \text{ P.M.}$  $T_6 = 1, 6:00 \text{ P.M. to } 9:00 \text{ P.M.}$  $T_7 = 1, 9:00 \text{ P.M. to } 12:00 \text{ A.M.}$ and 0 otherwise for all dummies. The time period 3:00 A.M. to 6:00 A.M. is the base case, when the least bidding activity occurs.</td></tr></table>

The starting time for the first period in each auction was the middle of the afternoon. Our data set contains 207 observations from the auction cycles in a three-hour period format (aggregating hourly observations), and 626 observations in the onehour format. The data-collecting agent used in this study failed to collect order number information from MobShop Web site for several time periods, so the number of observations in the two intervals do not conform to each other perfectly. Figure 3 illustrates the change in total number of orders in one cycle, and is suggestive of the emergence of greater interest among potential market participants, as the number of bidders increases and the remaining time to the close of the auction diminishes.

Table 2. Descriptive Statistics for the Bidding Data

<table><tr><td>Descriptive Category</td><td>Min</td><td>Max</td><td>Mean</td><td>Standard Deviation</td></tr><tr><td>Total number of orders, each cycle</td><td>96</td><td>324</td><td>170.4</td><td>81.0</td></tr><tr><td>Number new orders, 3-hour periods</td><td>0</td><td>79</td><td>5.7</td><td>8.5</td></tr><tr><td>Number of new orders per hour</td><td>0</td><td>38</td><td>1.9</td><td>3.3</td></tr></table>

![](/api/attachments/4KS6W8TV/fulltext/images/64dc7655eed90bccb1cb961d38ddd011d423a66d119475c638070fd2155b26ed.jpg)  
Figure 3. Order Accumulation in an Auction Cycle (three-hour interval, four days)

## Defining the Unit of Analysis

Because of the limited number of arriving orders (1.9 mean bids) when observations are taken every hour, we were forced to aggregate the data. As a result we examined time intervals for observation of both one hour and three hours in our core data analysis. In the latter instance, we divided each of the four days of an auction into eight three-hour intervals. Because one day was divided in this manner, we used seven dummy variables, $T _ { \mathrm { 1 } } , \dots T _ { 7 }$ , to indicate the different times of day. We selected the period from 3:00 A.M. to 6:00 A.M. as the base case, and did not code it. We made this choice because we expect to see the least bidding activity occur during this period. As a result, only seven dummy variables are needed to represent all periods in the day.

Figure 4 shows the average number of new orders that occur during different times of day for the seven auction cycles using one-hour and three-hour intervals, as well as the per-hour average for the three-hour intervals. This figure shows the extent of the micro-seasonality in the number of new orders throughout different times of day. The most orders are placed during the first half of afternoon, followed by the latter part of the afternoon up until late at night. The hours before dawn and during the morning are the least active.

![](/api/attachments/4KS6W8TV/fulltext/images/ac99c9b29cc1bfb033a625e719327ac89e8ade05cdd5eee091810be4156881e5.jpg)  
Figure 4. Mean Orders by Times of Day (one- and three-hour intervals)

## Econometrics Issues

We next consider defects in the data that might make the use of ordinary least squares (OLS) regression problematic for our data analysis. We examine three kinds of defects: collinearity, the auction cycle effect, and autocorrelation.

Collinearity. Correlations between the independent variables exhibit no correlations in excess of 0.60, with the exception of $P r i c e _ { t - 1 }$ and $\boldsymbol { O r d e r s } _ { t - 1 }$ , which have a high negative correlation of –0.72. This high correlation is due to the pricing strategies employed by MobShop, where price is determined by number of orders. As a result, in order to eliminate this collinearity problem, we eliminated the variable, $P r i c e _ { t - 1 }$ from our analysis.

Auction Cycle Effect. Because the data used in the current study consist of timeseries observations from different auction cycles, they are panel data in nature. Since the auction cycles from which data for the current study were collected are just a sample of the ongoing auctions at MobShop, we use a random effects model for panel data, where $u _ { i }$ is the random disturbance for auction cycle i, $E [ u _ { i } ] = 0 , E [ u _ { i } ^ { 2 } ] = s _ { u } ^ { ~ 2 }$ and $E [ u _ { i } u _ { j } ] = 0 \mathrm { i f } i \neq j [ 1 8 ]$

Autocorrelation. A final consideration is the autocorrelation problem, which is apparent with the structure of our research setting. The first-order autoregressive disturbance is used to correct for the autocorrelation problem in the data set. Applying an AR(1) process for the error term, we obtain $\mathfrak { E } _ { i ^ { \flat } t } = \rho e _ { i , t - 1 } + \Pi _ { i , t }$ , where $E [ \boldsymbol { \eta } _ { \flat _ { t } } ] = 0$ $E [ \mathfrak { n } _ { t } { ^ 2 } ] = \mathbb { G } _ { \mathfrak { n } } ^ { 2 }$ , and $\mathrm { C o v } [ \mathfrak { h } _ { \mathfrak { p } _ { t } } , \mathfrak { N } _ { s } ] = 0 , \mathrm { i f } \ t \neq s \ [ 1 8 ]$ . Because the software agent failed to collect order-accumulation information for about one-third of the length of one auction cycle, this created gap in the time series. Thus, the observations from this auction cycle were deleted from further data analysis. A total of four observations were missing from the other six auction cycles. Using broadly accepted methods for handling missing data (discussed in [50]), we created a small number of observations for these periods by averaging the total number of orders before and after the missing periods. This approach is further justified by the fact that only one or two new orders were placed during the periods when the agent failed to collect order number information. As a result, the final data contains observations from six auction cycles with 190 observations in the three-hour format.

## The Revised Model for Estimation

Beginning with our base model, and then applying the various considerations (including dropping a variable due to collinearity) and transformations (for a random effects panel data model and autocorrelation), we obtain the following additive linear models, which include an intercept:

$$
\begin{array}{r l} & N e w O r d e r s _ {i, t} = \alpha_ {0} + \sum_ {j = 1} ^ {7} \gamma_ {j} T _ {i, j} + \beta_ {1} \ln (O r d e r s _ {i, t - 1} + 1) + \beta_ {2} E n d _ {i, t} \\ & \qquad + \beta_ {3} B e f o r e D r o p _ {i, t - 1} + \beta_ {4} A f t e r D r o p _ {i, t - 1} + u _ {i} + \rho \varepsilon_ {i, t - 1} + \eta_ {i, t} \end{array}
$$

and

$$
\begin{array}{r} N e w O r d e r s _ {i, t} ^ {l} = \alpha_ {0} ^ {l} + \sum_ {j = 1} ^ {7} \gamma_ {j} ^ {l} T _ {i, j} + \beta_ {1} ^ {l} \ln (O r d e r s _ {i, t - 1} + 1) + \beta_ {2} ^ {l} E n d _ {i, t} \\ + \beta_ {3} ^ {l} B e f o r e D r o p _ {i, t - 1} + \beta_ {4} ^ {l} A f t e r D r o p _ {i, t - 1} + u _ {i} ^ {l} + \rho^ {l} \varepsilon_ {i, t - 1} ^ {l} + \eta_ {i, t} ^ {l}. \end{array}
$$

In this expression, the subscript $i = \{ 1 , . . . , 6 \}$ denotes the six auction cycles, and $j =$ $\{ 1 , . . . , 7 \}$ is a counter for the time-of-day control dummy variables, and the $\beta \mathrm { s }$ are the model parameters to be estimated.

## Results

TABLE 3 SUMMARIZES THE MODEL RESULTS, including coefficient estimates, significance levels, and standard errors. Overall, our model has an $R ^ { 2 }$ of 50.3 percent and an adjusted $R ^ { 2 }$ of 47.1 percent for $N e w O r d e r s _ { i ^ { \prime } i } ,$ and an $R ^ { 2 }$ of 50.1 percent and an adjusted $R ^ { 2 }$ of 46.9 percent for $N e w O r d e r s _ { i ^ { \prime } t } ^ { l }$

## Main Effects

Let us first consider the main effects in our model. The coefficient estimates for $\ln ( O r d e r s _ { t - 1 } { + } 1 )$ and $E n d _ { t }$ are significant at the 0.01 level for both dependent variables, indicating the presence of significant bidding participation externalities and an auction ending effect. For new orders placed during period t, the coefficient estimate for $\ln ( O r d e r s _ { t - 1 } { + } 1 )$ is 2.227 with a standard deviation of 0.603 (and 2.121 with a standard deviation of 0.576 for new orders excluding limit orders). The coefficient estimate for the ending effect variable is 24.224 with a standard deviation of 2.350 (and 24.398 with a standard deviation of 2.297 for new orders excluding limit orders). This means that on average 24.224 (or 24.398) more orders were placed during the last time period than the previous ones. This is a huge increase since the average ending num ber of orders for the six cycles was 174.5 and the average number of orders for each three-hour period was just 5.7.

<sub>d</sub> <sub>by</sub> <sub>[York</sub> <sub>University</sub> <sub>Libraries]</sub> <sub>at</sub> <sub>03:05</sub> <sub>05</sub> M

<table><tr><td rowspan="2">Variable</td><td colspan="3"> $NewOrders_{i,t}$ </td><td colspan="3"> $NewOrders^{l}_{i,t}$ </td></tr><tr><td>Coefficient Estimate</td><td>Standard Deviation</td><td>T-Ratio Significance</td><td>Coefficient Estimate</td><td>Standard Deviation</td><td>T-Ratio (Significance)</td></tr><tr><td colspan="7">Main Effects Variables</td></tr><tr><td> $\alpha_0$ </td><td>-7.551</td><td>2.972</td><td>-2.540**</td><td>-7.066</td><td>2.889</td><td>-2.445**</td></tr><tr><td> $ln(Orders_{t-1}+1)$ </td><td>2.227</td><td>0.603</td><td>3.695***</td><td>2.121</td><td>0.576</td><td>3.681***</td></tr><tr><td> $End_t$ </td><td>24.224</td><td>2.350</td><td>10.307***</td><td>24.398</td><td>2.297</td><td>10.623***</td></tr><tr><td> $BeforeDrop_{t-1}$ </td><td>4.264</td><td>1.421</td><td>2.897***</td><td>2.961</td><td>1.377</td><td>2.151**</td></tr><tr><td> $AfterDrop_{t-1}$ </td><td>0.232</td><td>0.911</td><td>0.254</td><td>0.315</td><td>0.879</td><td>0.358</td></tr><tr><td colspan="7">Time-of-Day Control Dummy Variables</td></tr><tr><td> $T_1$ </td><td>4.851</td><td>1.329</td><td>3.651***</td><td>4.661</td><td>1.308</td><td>3.564***</td></tr><tr><td> $T_2$ </td><td>0.033</td><td>1.325</td><td>0.025</td><td>0.035</td><td>1.304</td><td>0.027</td></tr><tr><td> $T_3$ </td><td>2.139</td><td>1.430</td><td>1.495</td><td>2.140</td><td>1.398</td><td>1.530</td></tr><tr><td> $T_4$ </td><td>3.323</td><td>1.557</td><td>2.134**</td><td>3.484</td><td>1.519</td><td>2.293**</td></tr><tr><td> $T_5$ </td><td>3.658</td><td>1.574</td><td>2.324**</td><td>3.426</td><td>1.535</td><td>2.231**</td></tr><tr><td> $T_6$ </td><td>5.153</td><td>1.477</td><td>4.294***</td><td>4.629</td><td>1.441</td><td>3.214***</td></tr><tr><td> $T_7$ </td><td>6.170</td><td>1.437</td><td>4.682***</td><td>6.056</td><td>1.404</td><td>4.313***</td></tr><tr><td colspan="7">Transformed Error Term</td></tr><tr><td>ρ</td><td>0.160</td><td>—</td><td>—</td><td>0.144</td><td>—</td><td>—</td></tr><tr><td> $R^2$ </td><td>50.3%</td><td>—</td><td>—</td><td>50.1%</td><td>—</td><td>—</td></tr><tr><td>Adjusted  $R^2$ </td><td>47.1%</td><td>—</td><td>—</td><td>46.9%</td><td>—</td><td>—</td></tr><tr><td colspan="7">Significance levels: * = p &lt; 0.10; ** = p &lt; 0.05; *** = p &lt; 0.01</td></tr></table>

<sub>3.Resultsof</sub>M<sup>odelTe</sup>

The coefficient estimate for $B e f o r e D r o p _ { t - 1 }$ is significant at 0.01 level for $N e w O r d e r s _ { i } , \ l ,$ indicating bidders were more willing to bid when they perceived the price would drop shortly. When the new orders due to conditional biddings are excluded, the coefficient estimate for $B e f o r e D r o p _ { t - 1 }$ is significant at 0.05 level, which is a conservative estimate of the before-price change effect. Our estimates suggest that the number of orders placed right before the price change occurs results in an average increase in new orders of between 2.961 and 4.264 more than those placed in periods that were neither right before nor right after the price decrease. This is a big increase since the average number of orders placed in each period is just 5.7. Contrary to our hypothesis, however, the number of orders placed after a price drop is not significantly different from those placed in periods that occurred neither right before nor right after a price change.

## Control Variable Effects

Our coefficient estimates for the time-of-day control dummy variables are consistent for the regressions using either dependent variable and are of similar magnitude. Three of the time-of-day control dummy variables are significant at the 0.01 level and two are significant at 0.05 level, indicating significant micro-seasonality effects. The time periods from 6:00 A.M. to 9:00 A.M., and from 9:00 A.M. to 12:00 P.M. are not significantly different from the base case from 3:00 A.M. to 6:00 A.M. On average, MobShop received the highest number of orders from 9:00 P.M. to 12:00 A.M., about six more than those received during the 3:00 A.M. to 6:00 A.M. period. Two afternoon periods (12:00 P.M. to 3:00 P.M., and 3:00 P.M. to 6:00 P.M.), as well as a midnight period (12:00 A.M. to 3:00 A.M.) received three more orders than the base period. The early evening period received about five more orders than the base.

## Transformed Error Term

Recall that our revised regression models included an error term decomposition, r, to eliminate problems with autocorrelation. The coefficient estimate for r is 0.160 for the regression of new orders placed during each period and is 0.144 when limit orders are excluded. The positive sign of the parameter estimate conforms to the usually observed positive correlation between adjacent error terms in economic data [18]. It indicates that the error term at time t will be influenced by all the error terms in previous periods, with the most recent one having a direct marginal effect of 0.160 and 0.144, respectively.

## Discussion

THE OVERALL RESULTS GENERALLY CONFIRM our primary contention in this research—that new bidders’ arrivals are positively influenced by the number of orders already placed under the group-buying discount market structure. This is evidence of a positive network externality in this virtual marketplace. Specifically, as the natural logarithm of the number of total orders plus one increases by one, the number of new orders placed during each period increases by 2.227 (or 2.121 if limit orders are excluded). Our results also indicate the existence of a nonlinear relationship between the current group size and the number of new orders placed in the group-buying network with a time frame. As the buyer group size increases, potential bidders perceive a larger expected network size and are more willing to bid for the product, as a result. However, as the end of the auction cycles approaches, potential buyers realized the limited possibility of network expansion and their willingness to bid increases at a decreasing rate.

We also observe a significant before-price drop effect in the current study. When the percentage of orders needed to reach the next price drop is 25 percent or less, there is an average of 4.264 more orders per three-hour time period (or 2.961 if limit orders are excluded). This result lends support to our hypothesis that when the numbers of orders needed are small enough to be within a potential buyer’s perceived price threshold, the person will be more likely to act upon the expectation that the price will drop in the near future. This causes the buyer to be more willing to order. In our model, we use 25 percent as the cutoff point for the before-price drop dummy variable. This percentage is selected based on our consideration that a too large or too small cutoff point may not accurately capture the region that bidders generate the price drop expectations and, hence, mask the before-price drop effect.

The reader should note that we did not find a significant after-price drop effect, at least with the exploring data set that we acquired from the MobShop Web site in March and April 2000. Before we conclude there is no after-price drop effect, however, we think that additional consideration should be given to our data collection and coding methods. In the current study, the data were collected at MobShop every hour, and then coded for the purposes of the econometrics into three-hour intervals. It is possible, for example, that some price drops may have occurred within these threehour periods, and that some orders placed after the price drop were mixed with orders placed before the price change. As a result, we may have counted them as orders placed before the price change occurred, when they actually occurred afterward. So, a significant after-price drop effect may exist, but may be mixed with the before price change effect. Even though it is possible that smaller time intervals might have been used in our data collection to obtain a higher degree of separation of orders placed before and after price drops, this approach is questionable for two reasons.

 First, when the time interval gets very small and the number of orders arriving during each period approaches zero, it becomes very difficult, if not impossible, to test the existence of significant differences in order arrival during each period. This data collection granularity issue becomes a matter of practicality in our research design.

 Second, we were concerned that too-frequent data collection from MobShop’s Web site might result in their blocking our access to their site. For example, during spring 2000, when we were testing the power of our data-collecting agent by iterating the data collection monitoring process every five minutes, MobShop actually blocked our agent twice. However, at the time we chose not to communicate with the firm’s management to request permission to continue. Our view was that MobShop was publishing publicly-available data, and that so long as our agent conducted its investigation with a “responsible price following” demeanor, and did not create an operational burden on the firm’s server operations, we felt that it would be acceptable. (After all, we were not capturing data to assist a competing firm or to try to do material harm to MobShop’s server operations. Our purpose was simply to better understand the inner workings of group-buying dynamic pricing markets.)

We also obtained results from our analysis that show a significant auction ending effect, with an average of about 20 more orders placed during the last period than in previous periods. Previously we identified two possible sources for this ending effect—accumulated limit orders, and buyers’reduced price uncertainty or bidding strategy. In our regression using the new orders that exclude limit orders, we find that the ending effect is still significant with a coefficient estimate of 24.398. Since the limit order effect has been excluded in this regression, the only possible explanation is the reduced uncertainty and buyer strategy. This perspective can be further supported by an examination of the last bidding periods of the auction cycles. Specifically, there was no price drop during the last period in any of the seven auction cycles, indicating limit orders were not a possibility for the ending effect. When there is still enough time left for the auction cycle, some potential buyers may choose to wait. They will postpone placing an order until they know what the final price is likely to be. As the cycle approaches its end, potential buyers who do not want to miss this opportunity will decide to make a purchase, resulting in a significant ending effect.

## Limitations

AS AN EXPLORATORY STUDY TO UNDERSTAND the dynamics of group-buying business models, the current research still has many limitations. In addition to the variables included in our model, the following factors may also influence new order arrivals at MobShop, but are not included in our model:

 The price drops differ in magnitude and this may have impact on number of new orders placed.

 Because of the design of group-buying business models, the current price is inherently correlated with group size. Hence, we removed current price from our empirical models. Some cautions are in order in interpreting the results that pertain to demand externalities, as a result, since the effect of lower prices, which is different from demand externalities, may be woven in.

 Competing posted prices on other related Web sites can also influence the traffic flow and orders placed at MobShop. When the price at MobShop decreased to a lower tier than those that buyers could find at other sites, the new orders placed might be due to this lower comparative price, instead of the internal market dynamics of group-buying.

To further explore the potential limitations associate competing posted prices, we use price history information from three sources to estimate the possible omitted variable bias in our empirical models. Popular Photography, a monthly magazine that specializes in cameras, photographic equipment, and techniques, also publishes national advertisements for cameras, lenses, and other photography paraphernalia for hobbyists and professionals. In addition, we obtained assistance from staff members at Best Buy, a nationwide posted-price discounter that is headquartered in the Twin Cities of Minnesota, for acquiring data from weekly catalogs and newspaper inserts with price history data for cameras. Finally, we acquired additional indicative price history information from an Internet price comparison shopping site PriceSCAN.com (www.pricescan.com). This firm allows users to compare prices of the same product at multiple Web sites and provides price history of the products.

What kind of data did we collect to determine the strength of a possible omitted variable bias? We searched the advertisements in the March 2000 through June 2000 issues of Popular Photography for relevant sales price information on the Olympus C-2020 Zoom digital camera. We then recorded the maximum, minimum, average, and standard deviation of the prices in dollars found for each month. We report them in Table 4.

Our search of the weekly catalogues of Best Buy during March 2000 and Apri 2000 showed that during the two weeks from April 2 to April 8 and from April 16 to April 22, the same Olympus C-2020 Zoom digital camera was advertised at \$699.99. In addition, PriceScan.com provided a price history of the same Olympus digital camera sold on the Internet. (See Figure 5.) Compared to these three sources of pricing information, MobShop’s starting price of \$615.95 in the seven auction cycles during the period of March and April 2000 was either much lower than the posted prices we found, or toward the lower end of the prices that PriceScan.com reported. As a result, we believe the impact of competitive prices on the order arrival of the Olympus digital camera at MobShop was minimal during the period our observations were taken, even though we had guessed all along that posted-prices elsewhere might be lower. This apparently turned out not to be the case, based on the evidence that we have assembled.

Two additional concerns must also be noted:

 The limited observations from seven auctions and one single product constrains the generalizability of our results. Our results would have been more robust had we designed the research to include longer observation period, as well as products from different categories and of high and low prices. However, the declin-

Table 4. Advertised Prices of Olympus C-2020 Zoom Digital Camera in Popular Photography

<table><tr><td>Months In 2000</td><td>Ads Listing Price</td><td>Maximum Price</td><td>Minimum Price</td><td>Mean Price</td><td>Standard Deviation of Price</td></tr><tr><td>March</td><td>5</td><td>$799.95</td><td>$737.00</td><td>$763.37</td><td>$33.42</td></tr><tr><td>April</td><td>5</td><td>$799.95</td><td>$707.00</td><td>$751.17</td><td>$46.25</td></tr><tr><td>May</td><td>4</td><td>$799.95</td><td>$649.95</td><td>$689.21</td><td>$73.90</td></tr><tr><td>June</td><td>6</td><td>$699.95</td><td>$599.99</td><td>$660.97</td><td>$37.65</td></tr></table>

## Olympus C-2020 Zoom

Mfg Part No: 225130

1600 × 1200 Ma× Resolution, 2110000 pixel Image Sensor, 3× Optical Zoom, LCD Display Movie Capture, SmartMedia Storage, built-in Flash

## Prices|Product Photo | Product Reviews

![](/api/attachments/4KS6W8TV/fulltext/images/b29ffeb330b8fc272c326de6d17fc31bb0017faea407526861ea93e746f8abf0.jpg)  
Figure 5. Price History of Olympus C-2020 Zoom Digital Camera at PriceSCAN.com (www.pricescan.com/digiphoto/graphs/graph113572.asp). Note: Interested readers can also obtain a similar price history graph of the same Olympus C-2020 Zoom digital camera at Nextag.com [35].

ing market for group-buying Web sites that began in summer 2000 actually forced MobShop to change its price levels and quantity cutoff points. This ultimately prevented us from obtaining more observations that would permit a comparison with prior period bidder behavior for the same group-buying setup.

 The “Save a Spot” feature implemented by MobShop deserves discussion. Consider the situation in which two individuals whose reservation prices are both less than the current price but no less than the next lower level price. Suppose that when they both bid they can drive the price down to the next level, but no change in price occurs if only one of them bids. Under this situation, [Bid, Bid] and [No Bid, No Bid] result in a Nash equilibrium [16]. When no coordination or information sharing is possible between the two, however, they will not always arrive at the Nash [Bid, Bid] decisions due to the risk of getting a negative payoff. The “Save a Spot” feature serves as a coordination mechanism in which the bidder can indicate her preferred action without the risk of getting a negative payoff. As a result, the effectiveness of the market is improved.

As mentioned earlier, group-buying business models motivate participating buyers to recruit others, which results in lower customer acquisition costs for the seller. MobShop did that, and it designed its Web site to implement conditional bidding to further improve market performance. And based on our price comparison results (for cameras, at least), MobShop seemed to be doing well in offering its customers lower prices than its competitors. But still, the DotCom marketplace still seemed to catch up with MobShop. Why couldn’t MobShop avoid the declining market interest, if their fundamentals were fairly good, and they enjoyed some advantage of being early to market? Why were they forced to redefine their business model to emphasize their new role as a software licensing vendor? We now turn to an assessment of groupbuying business models to attempt to put the answers to these questions in proper perspective.

## A Broader Assessment of Group-Buying Business Models in E-Commerce

LET’S FIRST CONSIDER THE “BIGGER PICTURE” in the group-buying DotCom market. In Table 5, we briefly chronicle the separate paths to success and failure that the various group-buying sites on the Internet have experienced. (For a more in-depth discussion of these mini-cases, the interested reader should see Kauffman and Wang [23]).

We identify four reasons as possible explanations for the initial growth and subsequent difficulties that many of these group-buying Web sites have experienced.

1. Many group-buying sites failed to achieve the critical mass that was necessary for them to compete with bricks-and-mortar and Internet-based discount retailers such as Walmart, Kmart, and Buy.com. Without enough buyers, groupbuying Web sites simply will not be able to offer sufficiently low prices, like the posted-price market leaders. So even though group-buying sites claimed they could provide savings to their customers, the reality was probably quite different. The limited volume of transactions that materialized on these sites prevented them from securing lower prices from their suppliers than could the nationwide discount posted-price retailers, which in turn prevents them from passing the savings on to their customers.

Table 5. The Success and Failure of Group-Buying Web Sites on the Internet

<table><tr><td>Web Site</td><td>Events Describing the Firm&#x27;s Path to Success and Failure</td></tr><tr><td>C-Tribe</td><td>Unique online group-buying of offline retail gift certificatesRedesigned Web site in June 2000 to allow for access through multiple channels such as Internet, telephone, and mobile devicesLoyalty program gave frequent buyers cash-back rewardsClosed sometime in late 2000</td></tr><tr><td>Let&#x27;s Buy It</td><td>A highly visible Web site in EuropeFiled for bankruptcy in December 2000 due to financial constraintsResumed operation in February 2001 after the infusion of additional fundingCurrently facing the problem of lack of critical mass market interest</td></tr><tr><td>Mercata</td><td>High profile startup backed by Microsoft cofounder Paul AllenOne of two early market leaders in group-buyingEarly involvement in retail and wholesale demand aggregationCeased operation in January 2001 due to a shortage of funding</td></tr><tr><td>MobShop</td><td>Increasing market interest during first half of 2000The second of two early innovators in group-buyingStarted to experience declining market following summer 2000Changed strategic focus to demand aggregation software licensing in January 2001</td></tr><tr><td>OnlineChoice</td><td>Uniquely positioned through offering of group-buying services for electricity, natural gas, telephone service, and so onAdvertised a customer base of 460,000 consumers and businesses in March 2001Folded by late April 2001</td></tr><tr><td>SHOP2gether</td><td>Group-buying services for small businesses on office furniture and equipment, travel, employee benefits, and corporate giftsRedirected its demand aggregation services toward education market in April 2000</td></tr><tr><td>VolumeBuy</td><td>Acted as a group-buying software vendor, in addition to providing a demand aggregation marketplace for consumersThree types of buying pools give buyers the flexibility of choosing formatBut requires buyer cognitive effort to understand benefits of participating in the different buying pools</td></tr></table>

2. There were low barriers to entry in the group-buying market, and this negatively affected sustainable competitive advantage. After Mercata and MobShop established the first two group-buying sites on the Internet, the number of group-buying firms rapidly swelled to twelve by early spring 2000. This reflected the presence of low barriers to entry due to a high propensity for imitation in the group-buying market. And this had the added negative effect of forcing the group-buying firms to compete not only with the traditional posted-pricing retailers, but also among themselves. As these firms learned, it would be very difficult to fight a head-on, winning battle with the largest and most powerful firms that have ever existed in the U.S. retail sales market.

3. Similar to Priceline.com, the group-buying firms were targeting the most pricesensitive consumers, who were poised to switch to other sellers with very little provocation. Because most of the group-buying Web sites tended to focus on a single dimension—price—instead of delivering a truly unique value proposition to their customers, their target market, by default, was bargain huntingconsumers. From prior research, bargain hunters are known to be less loyal than a retailer might desire. As a result, it was difficult for group-buying sites to build a loyal customer base. This put their potential for long-term profitability in jeopardy. Moreover, they were more easily squeezed when stronger players or new and inexperienced firms entered the market and made price the focal point of the competition.

4. Group-buying Web sites were subject to a structural “death spiral” of declin ing participation and viability, once the right circumstances occurred. Even the slightest shocks to the participation of members in a group-buying Web sites marketplace can have an adverse effect, as Clemons et al. [7] have shown can occur in other market settings. The intuition goes like this: Once a number of participants depart (for whatever reason, e.g., failure of the group-buying market to deliver sale items to customers in a timely manner, indications that the best prices are being offered at the site, other buying innovations that are occurring in the market at the same time), the extent of the critical mass of a group-buying marketplace will be diminished. This can only have the effect of reducing the willingness of the marginal market participant to stay in the market. Ultimately, the departure of some buyers will be evidenced by lower participation rates and bidding densities, leading to the departure of other marginal buyers in the buying pool, and ultimately leading to a “death spiral” that causes the group-buying model to cease being an effective mechanism to achieve sales. As the initial appeal of group-buying to buyers wears off and they learn more about the limited cost savings (if any) associated with group-buying, buyers will naturally turn their interest elsewhere.

The examples of group-buying business models that we have discussed illustrate the importance of examining electronic commerce initiatives in a broader context. Indeed, even though many observers have focused on the “revolution” associated with DotCom business models and the transformation of traditional business due to the emergence of the Internet, the real interest is now developing around the “evolution” of business strategy on the Internet. As we have seen in this article, the groupbuying firms of the Internet are no exception. Webmergers.com reports that more than 400 DotCom firms folded from January 2000 to April 2001 [49]. Webmergers’ president, Tim Miller, observes that for DotComs now it’s not a matter of how well these firms do what they have been doing, but how fast they can “morph” and begin to do something else that will enable them to achieve sustainable competitive advantage [34]. If we consider the group-buying context, such as we have in this article, it is clear that this interpretation is dead on target, in spite of the interesting innovations that we have seen to date.

## Conclusions

USING DATA COLLECTED FROM MobShop, the current study tested a model that predicts bidder participation and order arrivals in an electronic market that uses an innovative group-buying discount market microstructure, and provided an evaluation of group-buying business models. This research offers four contributions to what we know about the use of dynamic pricing market microstructures in sales auctions on the World Wide Web. They include:

1. Through this research, we now have a better understanding of the manner in which buyer bidding behavior occurs under a market microstructure with groupbuying discounts like MobShop’s.

2. We have obtained a better understanding of the complexities that are inherent in modeling even a simple phenomenon like bidder arrivals. We learned, for example, about the structure of the data, and the necessity of making various adjustments to support the estimation of a meaningful empirical model in this context.

3. We obtained preliminary evidence for the impact of participation externalities in an Internet-based electronic market. Although our results require refinement and expansion with more auctions and data to achieve broader generalizability, we nevertheless have shown the relevance of new theoretical perspectives from consumer behavior and Marketing Science, as well as from Economics, in this context.

4. We identified the sources that might have led to the failures of the business models of many group-buying sites.

IS and e-commerce researchers have been trying to explore the variety of business models in Internet-based selling [22]. As we attempted to understand the market dy namics and efficacy of group-buying business models, the current exploratory study illustrated one approach that can be taken to examine a specific type of business model. But it also became clear as we performed this research that the inner workings of the market microstructure of group-buying Web sites did not represent the keystone for their success or failure. In order to gain a more in-depth understanding of the recent developments in this area of the digital economy, and to relate it to other developments in e-commerce leading to the failure, acquisition, or merger of Internet companies, future research should take a more systematic approach to examine the evolution of DotCom strategies. We look forward to pursuing such issues in future research that is motivated by the present work.

Acknowledgments: The authors wish to thank Baba Prasad, Eric Clemons, Rajiv Dewan, Yu-Ming Wang, and Andrew Whinston, as well as five anonymous referees from the HICSS-34 and the Journal of Management Information Systems reviewing processes, for helpful suggestions and comments. Special thanks also are due to the participants in the Economics, Information Systems and Electronic Commerce Doctoral Seminar, held at the Carlson School of Management of the University of Minnesota during spring 2000, for comments on an earlier version of this research. The assistance of Mark Melville and Becky Porter at MobShop.com in San Francisco with interviews and data collection is also appreciated. An earlier version of this paper appeared in Proceedings of the 34th Hawaii Conference on Systems Science(Los Alamitos: IEEE Computer Society Press, 2001). All errors of fact or interpretation are solely the responsibility of the authors.

## REFERENCES

1. Andrews, W. The new laws of dynamic pricing. Internet World, 5, 35 (December 15, 1999), 27–34.

2. Bajari, P.L., and Hortacsu, A. Winner’s curse, reserve price, and endogenous entry: Empirical insights from eBay auctions. Working paper 00-004, Department of Economics, Stanford University, 2000.

3. Bakos, Y. The emerging role of electronic marketplaces on the Internet. Communications of the ACM, 41, 8 (August 1998), 35–42.

4. Bapna, R.; Goes, P.; and Gupta, A. A theoretical and empirical investigation of multiitem on-line auctions. Information Technology and Management, 1, 1–2 (2000), 1–23.

5. Barney, J.B. Firm resources and sustained competitive advantage. Journal of Management, 17, 1 (March 1991), 99–120.

6. Brynjolfsson, E., and Kemerer, C.F. Network externalities in microcomputer software: An econometric analysis of the spreadsheet market. Management Science, 42, 12 (December 1996), 1627–1647.

7. Clemons, E.K.; Croson, D.C.; and Weber, B.W. Market dominance as a precursor of a firm’s failure: Emerging technologies and the competitive advantage of new entrants. Journal of Management Information Systems, 13, 2 (Fall 1996), 59–68.

8. Corral, C.B. Clicks and mortar: Category leaders in cyberretailing. Discount Store News, 38, 23 (December 13, 1999), 10–13.

9. Drakopoulos, S.A. Psychological thresholds, demand and price rigidity. The Manchester School of Economic and Social Studies, 60, 2 (June 1992), 152–168.

10. Dybvig, P.H., and Spatt, C. Adoption externalities as public goods. Journal of Public Economics, 20, (March 1983), 231–247.

11. Dyer, J.S., and Sarin, R.K. Relative risk aversion. Management Science, 28, 8 (August 1982), 875–886.

12. eBay.com. Annual report, 2000, available at www.shareholder.com/ebay/annual/ 2000\_annual\_10K.pdf.

13. Economides, N. The economics of networks. International Journal of Industrial Organization, 14, 6 (October 1996), 673–699.

14. Economides, N., and Himmelberg, C. Critical mass and network size with application to the U.S. fax market. Discussion paper EC-95-11, Stern School of Business, New York University, New York, 1995.

15. Economides, N., and Schwartz, R.A. Electronic call market trading. Journal of Portfolio Management, 21, 3 (Spring 1995), 10–18.

16. Fudenberg, D., and Tirole, J. Game Theory. Cambridge, MA: MIT Press, 1991.

17. Gandal, N. Hedonic price indexes for spreadsheets and an empirical test for network externalities. Rand Journal of Economics, 25, 1 (Spring 1994), 160–170.

18. Greene, W.H. Econometric Analysis, 4th ed. Upper Saddle River, NJ: Prentice Hall, 2000.

19. Handa, P., and Scheartz, R.A. Limit order trading. The Journal of Finance, 51, 5 (December 1996), 1835–1861.

20. Katz, M., and Shapiro, C. Network externalities, competition, and compatibility. American Economic Review, 75, 3 (June 1985), 424–440.

21. Kauffman, R.J., and Riggins, F.J. Information systems and economics. Communications of the ACM, 41, 8 (August 1998), 32–34.

22. Kauffman, R.J., and Walden, E.A. Economics and electronic commerce: Survey and directions for research. International Journal of Electronic Commerce, 4, 5 (Summer 2001), 4–115.

23. Kauffman, R.J., and Wang, B. Bid together, buy together: On the efficacy of groupbuying business models in Internet-based selling. In P.B. Lowry, J.O. Cherrington, and R.R. Watson (eds.), Handbook of Electronic Commerce in Business and Society. Boca Raton, FL: CRC Press, 2002 (forthcoming).

24. Kauffman, R.J., and Wood, C.A. Data-collecting agents: Evaluating a research approach for the age of the Internet. Working paper, MIS Research Center, Carlson School of Management, University of Minnesota, Minneapolis, MN, May 2001.

25. Kauffman, R.J.; March, S.T.; and Wood, C.A. Design principles for long-lived Internet agents. International Journal of Intelligent Systems in Accounting, Finance and Management, 9, 12 (December 2000), 217–236.

26. Kauffman, R.J.; McAndrews, J.J.; and Wang, Y.M. Opening the black box of network externalities in network adoption. Information Systems Research, 11, 1 (March 2000), 61–82.

27. Kerstetter, J. Accompany has high hopes for a new business model. PC Week, 16, 17, April 26, 1999, p. 22.

28. Krishna, A. The effect of deal knowledge on consumer purchase behavior. Journal of Marketing Research, 31, 1 (February 1994), 76–91.

29. LetsBuyIt.com. LetsBuyIt.com back in control. Corporate press release, February 21, 2001, available at www.investor.letsbuyit.com/investor/en/news/press/00180/.

30. Mara, J. Good buys. Adweek, 41, 10 (March 6, 2000), 58–64.

31. McAfee, R.P., and McMillan, J. Auctions and bidding. Journal of Economic Literature, 25, 2 (June 1987), 699–738.

32. McHugh, J. Consumer collusion! Forbes, 164, 5 (September 6, 1999), 222–223.

33. Milgrom, P., and Weber, R.J. A theory of auctions and competitive bidding. Econometrica, 50, 5 (September 1982), 1089–1122.

34. Miller, T. Creative reconstruction: How DotComs are adapting to new market realities. Research report, Webmergers.com, June 2001.

35. Nextag.com. Olympus C-2020 zoom 1600x1200 8MB JPEG/TIFF digital camera 225130.

May 25, 2001, available at www.nextag.com/buyer/PriceHistory.jsp?product=7000668& channel=main&category=null.

36. Porter, M.E. Competitive Advantage: Creating and Sustaining Superior Performance. New York: Free Press, 1985.

37. Porter, M.E. Strategy and the Internet. Harvard Business Review, 79, 3 (March 2001), 63–78.

38. Reichheld, F.F.; Markey, R.G. Jr.; and Hopton, C. The loyalty effect: The relationship between loyalty and profits. European Business Journal, 12, 3 (Autumn 2000), 134–139.

39. Sarin, R.K., and Weber, M. Risk-value models. European Journal of Operational Research, 70, 2 (October 1993), 135–149.

40. Scheraga, D. A sales odyssey. Chain Store Age, 77, 1 (January 2001), 96–106.

41. Shy, O. Technology revolutions in the presence of network externalities. International Journal of Industrial Organization, 14, 6 (October 1996), 785–800.

42. Simon, H. Price Management. Amsterdam: North-Holland, 1989.

43. Slater, S.F. The challenge of sustaining competitive advantage. Industrial Marketing Management, 25, 1 (January 1996), 79–86.

44. Spulber, D.F. Market microstructure and intermediation. Journal of Economic Perspectives, 10, 3 (Summer 1996), 135–152.

45. Tversky, A., and Kahneman, D. Advances in prospect theory: Cumulative representation of uncertainty. Journal of Risk and Uncertainty, 5, 4 (October 1992), 297–323.

46. Vakrat, Y., and Seidmann, A. Implications of the bidders’process on the design of online auctions. In R. Sprague (ed.), Proceedings of the 33rd Hawaii International Conference on System Sciences. Los Alamitos, CA: IEEE Computer Society Press, CD-ROM, 2000.

47. Vickrey, W. Counterspeculation, auctions, and competitive sealed tenders. Journal of Fi nance, 16, 1 (March 1961), 8–37.

48. Wang, R. Auctions versus posted-price selling. American Economic Review, 83, 4 (September 1993), 838–851.

49. WebMergers.com. Shutdowns surge, M&A slumps in April. May 26, 2001, available at www.webmergers.com/editorial/article.php?id=17.

50. Weisberg, S. Applied Linear Regression, 2d ed. New York: John Wiley & Sons, 1985.

51. Wernerfelt, B. A resource-based view of the firm. Strategic Management Journal, 5, 2 (April/June 1984), 171–180.

52. Winer, R.S. A price vector model of demand for consumer durables: Preliminary developments. Marketing Science, 4, 1 (Winter 1985), 74–90.
