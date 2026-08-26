---
otero_id: 920
otero_key: "45AJE4K3"
title: "Online and Offline Demand and Price Elasticities: Evidence from the Air Travel Industry"
authors: "Nelson Granados; Alok Gupta; Robert J. Kauffman"
year: "2012"
journal: "Information Systems Research"
doi: "10.1287/isre.1100.0312"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/45AJE4K3/fulltext/images/1a6cf0199332aab891818475dbdb8af94f46812cc72cab8a54c58d85ebf660c6.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Online and Offline Demand and Price Elasticities: Evidence from the Air Travel Industry

Nelson Granados, Alok Gupta, Robert J. Kauffman,

## To cite this article:

Nelson Granados, Alok Gupta, Robert J. Kauffman, (2012) Online and Offline Demand and Price Elasticities: Evidence from the Air Travel Industry. Information Systems Research 23(1):164-181. http://dx.doi.org/10.1287/isre.1100.0312

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2012, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/45AJE4K3/fulltext/images/9b51494558ab00e53fed80953ee4b7c0a13deddb00eafde2997cc6736bb4dc32.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Online and Offline Demand and Price Elasticities: Evidence from the Air Travel Industry

Nelson Granados

Graziadio School of Business and Management, Pepperdine University, Irvine, California 92612, nelson.granados@pepperdine.edu

Alok Gupta

Information and Decision Sciences, Carlson School of Management, University of Minnesota, Minneapolis, Minnesota 55455, alok@umn.edu

Robert J. Kauffman W. P. Carey School of Business, Arizona State University, Tempe, Arizona 85287, rkauffman@asu.edu

he Internet has brought consumers increased access to information to make purchase decisions. One of the expected consequences is an increase in the price elasticity of demand, or the percent change in demand caused by a percent change in price, because consumers are better able to compare offerings from multiple suppliers. In this paper, we analyze the impact of the Internet on demand, by comparing the demand functions in the Internet and traditional air travel channels. We use a data set that contains information for millions of records of airline ticket sales in both online and offline channels. The results suggest that consumer demand in the Internet channel is more price elastic for both transparent and opaque online travel agencies (OTAs), in part, because of more leisure travelers self-selecting the online channel, relative to business travelers. Yet, after controlling for this channel self-selection effect, we still find differences in price elasticity across channels. We find that the opaque OTAs are more price elastic than the transparent OTAs, which suggests that product information can mitigate the price pressures that arise from Internet-enabled price comparisons. We discuss the broader implications for multichannel pricing strategy and for the transparency-based design of online selling mechanisms.

Key words: air travel industry; economics of information systems; electronic markets; market transparency; mechanism design; multichannel strategy; price elasticity; online travel agencies; self-selection

History: Vallabh Sambamurthy, Senior Editor. This paper was received on June 1, 2008, and was with the authors 13 <sup>1</sup> months for 2 revisions. Published online in Articles in Advance April 8, 2011.

## 1. Introduction

Classic economic theory suggests that higher availability of information brings markets closer to perfect competition and full market efficiency. In particular, with the proliferation of electronic markets via the Internet, there has been an expectation that frictionless commerce will emerge, where perfect information to compare product offerings will lead to higher competition and a subsequent erosion of profits (Brynjolfsson and Smith 2000). Frictionless commerce has been hypothesized based on the following observations:

• Supply. Sellers engage in fierce price competition and lose their ability to price above marginal costs, leading to lower and less dispersed prices (Bakos 1997, Brynjolfsson and Smith 2000).

• Demand. Buyers enjoy lower search costs so they are able to make purchases that better fit their needs at a lower price (Bakos 1997), further fueling competition among suppliers.

For the last decade, academics have given a significant amount of attention to the supply-side effects, by analyzing the pricing actions of sellers, based on the massive amounts of price information that can be gathered from online sources. The results so far have been mixed. Some researchers have found analytical and empirical support for lower prices on the Internet relative to traditional channels (Brown and Goolsbee 2002, Brynjolfsson and Smith 2000, Degeratu et al. 2000, Lee 1998, Zettelmeyer 2000, Zettelmeyer et al. 2006) and lower price dispersion (Ghose and Yao 2010). Others, in turn, have found higher prices on the Internet (Bailey 1998, Lal and Sarvary 1999) and the existence of price dispersion (Chellappa et al. 2010, Ghose and Yao 2010), which contradicts the law of one price expected in the presence of perfect competition. Walter et al. (2006) argue that price dispersion exists because of the nature of e-retailers (multichannel versus pure play) and product characteristics. Therefore, there is some evidence that even in Internet-based markets, some of the frictions that mitigate head-on price-based competition will remain.

On the other hand, there is still much research to be done on the demand-side effects. One of the expected outcomes of the higher transparency in electronic markets is an increase in the price elasticity of demand, because of the increased availability of information about competitive offerings (Ghose and Yao 2010, Lynch and Ariely 2000, Smith 2002, Smith et al. 2001). Price elasticity comparisons across channels can inform the discussion on the impact on prices and price dispersion of the lower search costs for information in electronic markets. Theoretically, the higher the price elasticity, the lower will be the market price, and as prices converge to marginal cost, price dispersion will also decrease (Ghose and Yao 2010).

In this paper, we contribute to this line of research by estimating and comparing the air travel demand functions in the online and offline channels, using a data set with information for millions of airline tickets sold in the U.S. market. In our data, the offline channel represents phone-based or face-to-face reservations via traditional travel agencies and corporate travel departments while the online channel represents consumer-direct bookings via transparent online travel agencies (OTAs) such as Expedia and Travelocity, and opaque OTAs such as Hotwire and Priceline.com. We examine the following research questions:

• What are the differences in price elasticity of demand between the online and offline channels? What factors drive these differences?

• What are the implications for pricing, multichannel strategy, and information technology (IT) strategy?

Our empirical results provide a demand-side perspective on how the Internet channel impacts markets by bringing them closer to perfect information. This is one of the first studies that uses massive industry sales data to estimate price elasticities in the online and offline channels. The use of sales data provides a more direct estimate of price elasticity than that of a commonly used method in the literature based on sales rank (e.g., Brynjolfsson et al. 2003, Chevalier and Goolsbee 2003, Ellison and Ellison 2009, Ghose et al. 2006). In a nutshell, we find broad support for the notion that the Internet as a distribution channel is more price elastic than the offline channel, for both transparent and opaque OTAs. We were able to tease out the two major drivers of this higher elasticity online; namely, the informational effects on consumers and the disproportionate share of leisure travelers who book online. We find that the online channel is more price elastic even after controlling for customer heterogeneity across channels.

This analysis of the demand-side impacts of the Internet is not just relevant for the discussion of frictionless markets. There are also strategic consequences for firms. Our finding that the online channel is more elastic suggests that price discrimination across channels is bound to emerge, but it also explains why incumbents in many industries have been reluctant to penetrate the online channel aggressively, because of the consequent downward pressure on prices. We also find that opaque OTAs have very price-elastic demand, which suggests that opaqueness of information on product attributes and quality can lead to a very price-sensitive market. Therefore, product information is an important dimension to be considered in the design of selling mechanism, either to elicit lower price elasticity, or to attract less price-sensitive customers. More broadly, the results support our contention that firms must consider demand-side impacts in the design of their electronic selling mechanisms and as they price across channels. The winning players in electronic markets will use information strategically to develop transparency strategies, by considering the impact of information on consumer demand in the design of online selling mechanisms and pricing strategies (Granados et al. 2008).

The rest of the paper is organized as follows. In §2, we provide the theoretical background, hypotheses, and data. In §3, we present the econometric model of air travel demand, and the results of our analysis. In §4, we analyze and discuss our findings. Section 5 concludes with the implications for academics and practitioners, limitations of this research, and future research directions.

## 2. Hypotheses, Data, and Modeling Preliminaries

One of the predictions around the emergence of electronic markets is that price elasticity, the percent change in demand caused by a percent change in price, will be higher online than offline, because electronic markets enable consumers to search for information about competitive offerings at a lower cost (Smith et al. 2001, Alba et al. 1997). We will refer to this central hypothesis as the frictionless markets and price elasticity hypothesis (or FMPE hypothesis). Upon review of the literature in multiple disciplines, we find that there are nuances that need to be considered, so in this section, we first discuss the possible effects of increased availability of information on purchase decisions. We then develop hypotheses about the difference in price elasticities across channels and describe the data that was used to test the hypotheses, including some empirical modeling preliminaries.

## 2.1. The Impact on Demand of Better-Informed Consumers

Consumers will use market information to the extent that it is a valuable input in the purchase process. The effects on demand can be broken down into the impact on consumers’ sensitivity to price changes and on channel selection.

2.1.1. Price Information. Stigler (1961) suggests that in an environment of price dispersion, information about market prices allows consumers to find lower prices for a given product or horizontally differentiated substitutes. For example, Brynjolfsson and Smith (2000) found that prices for books and CDs were lower in the Internet channel as compared to conventional retailers. This higher ability to effectively compare prices for similar product offers should make consumers more price sensitive, because they have a larger consideration set to choose from, or a larger number of substitutes (Brons et al. 2002).

2.1.2. Product Information. Increased information about product characteristics and quality allows consumers to ascertain their valuation of a product with higher precision and find a product that better fits their needs (Akerlof 1970, Alba et al. 1997). Other things being equal, product information is likely to make consumers less price sensitive, as they focus their search on product characteristics and quality rather than on price (Gupta et al. 2004b). This assertion is founded on information integration theory (Anderson 1968, 1971; Degeratu et al. 2000), which suggests that consumers assign importance weights and values to available search attributes and then add them to make a purchase decision. The weights assigned are relative to the information available. Weights will not be assigned to information that is not available, so to the extent that product and brand information is not available, more weight will be placed on the price factor. On the flip side, if more product information is available, less weight will be placed on price.

2.1.3. Channel Selection. The relative information availability about product offers will also influence channel selection. Different service features and information levels lead to partially separable demand sets in the online and offline channels, or the existence of online-only shoppers and offline-only shoppers. Also, since lower search costs do not necessarily lead to more search activities (Gupta et al. 2004a, Johnson et al. 2004), some consumers may be locked-in to an online search process that has served them well in the past. This effect may be enhanced over time as consumers become more familiar and comfortable with their online search options.

The existence of single-channel shoppers can lead to a difference in the mix of customer segments across channels. Any difference in the mix of customers can, in turn, partially explain differences in cross-channel price elasticities. In the case of air travel, leisure travelers are likely to embrace the benefits of the online channel for search, because they have more flexibility in their travel requirements and are therefore willing to compare a more comprehensive set of alternatives (Clemons et al. 2002). On the other hand, many business travelers are locked into the offline channel because they place a high value on search time or simply prefer the added value of an experienced travel agent or corporate travel department. Others may not feel comfortable enough with computers to search for an airline ticket online. PhoCusWright (2004), a travel consulting and research firm, found that 45% of travelers were online-only shoppers. A similar study found that 42% of respondents were offline-only shoppers (Regan 2001). Gupta et al. (2004a) develop an analytical model and attribute this phenomenon to consumers’ risk attitudes, which are related to their price sensitivity.

Business travelers are less price sensitive because they are less flexible and often have more complex travel needs than leisure travelers. If leisure travelers are more price sensitive and they gravitate to the online channel, then this channel selection effect will lead to a higher observed price elasticity of demand online.

2.1.4. Summary. Overall, improvements in the availability of market information in the online channel decreases search costs, which can affect price elasticity of demand in three ways. Price comparison capabilities will make consumers more price sensitive in line with the FMPE hypothesis, product information will make consumers less price sensitive in line with information integration theory, and pricesensitive consumers will select a channel that offers easier comparison of product offerings and prices. Next, we hypothesize about the net result of these three effects in the air travel industry, for both the leisure and business travel segments.

## 2.2. Hypotheses

We formally define price elasticity as $\eta = \delta D / \delta P \cdot P / D ,$ or the percent change in demand D because of a percent change in price P . Demand decreases if price increases for normal goods such as travel, so  will be negative. If $| \eta | > 1 ,$ , demand is said to be elastic, because there is a higher than proportional increase in demand. $\mathrm { I f } \ | \eta | = 1$ , demand is unit elastic. If $| \eta | < 1$ demand is inelastic. We define $\eta _ { T } = \mathrm { p r i c e }$ elasticity of transparent OTAs, $\eta _ { O F F } = \mathrm { p r i c } \epsilon$ elasticity of the offline channel, and $\eta _ { O P } = { \mathrm { p r i c e } }$ elasticity of the opaque OTAs.

2.2.1. Offline vs. Transparent OTAs. The online travel channel allows consumers to search for airline tickets with detailed information regarding the itinerary and the associated price. Depending on the OTA, the number of priced itineraries for a search request can fluctuate. Travelocity, Expedia, and Orbitz—the industry leaders—display typically at least 50 search results per request. Instead, consumers typically receive just one or a handful of quotes from a travel agent or airline representative in the offline channel.

It is worth noting that the technological search capabilities of the online and offline travel channels are similar. Rather, what changes is the level of transparency of the interface with the customer. The travel industry has legacy systems and electronic market platforms for the distribution of airline tickets. Travel agencies and airlines use electronic reservation systems for phone-based and face-to-face interaction with travelers, which are integrated to sophisticated internal pricing and inventory management systems that airlines use to price each seat on a given flight. Transparent OTAs, such as Expedia and Travelocity, provide consumers direct access to the same information through an Internet-based user-friendly interface of this legacy distribution infrastructure. Through the online channel, travelers can browse numerous itineraries on their own. Offline travel agents and airline representatives, however, do not have the capability or the incentives to bring full transparency, because it is not possible by phone to relay all the possible information about the options in the same way an OTA does. Also, in an offline market, travel agencies and airlines have control of the information, so they have incentives to extract surplus from the consumer by not being fully transparent.

Transparent OTAs make comprehensive price comparisons possible, with detailed information about the airline carrier and the itinerary for each offer. These differences in price and product information have opposite effects on price elasticity. According to our central hypothesis, the FMPE hypothesis, price comparison capabilities will increase price elasticity, while information integration theory suggests that product information will decrease price elasticity. The FMPE hypothesis suggests that the net effect for commodity markets such as leisure travel will be higher price elasticity, so the higher price sensitivity because of price comparisons will prevail. This rationale leads to the following hypothesis.

Hypothesis 1A (The Leisure Segment Transparent OTA Price Elasticity Hypothesis) (H1A). <sub>In</sub> <sub>the</sub> leisure segment, transparent OTA demand is more price elastic than offline demand.

Information integration theory suggests that for differentiated markets, the impact of price comparison capability on price elasticity will not be as high as for commodity markets, because product attributes and brand will have more weight than price in the decision-making process (Degeratu et al. 2000). Brand can act as a surrogate for any missing product information, so the weight on price will not be as high as in markets that are commoditized, where brand matters less. Moreover, product information is likely to mitigate price elasticity in differentiated markets, because as consumers are better able to identify products that fit their needs, they will discard other options, effectively limiting the consideration set to the one or few offerings with the best fit. For example, in their experiments, Lynch and Ariely (2000) found that crossstore comparison had no effect on price sensitivity for premium wines. Similarly, Walter et al. (2006) found that the significant amount of price dispersion can be explained by the type of product, with specialized products having much less price dispersion as compared to commodities. Degeratu et al. (2000) compared the price sensitivity of consumers in grocery purchases and found that it was lower online. We hypothesize that the effect of product transparency will prevail in the business segment, so the net effect of transparent OTAs on business travel will be a reduction in price elasticity.

Hypothesis 1B (The Business Segment Transparent OTA Price Elasticity Hypothesis) (H1B). <sub>In</sub> <sub>the</sub> business segment, transparent OTA demand is less price elastic than offline demand.

Regarding channel selection, we find in our data that there is a higher share of business travel offline than online. This makes sense because business travelers are more time sensitive and likely to delegate the search task to an offline travel agency. In contrast, leisure travelers are more price sensitive, so they are more likely to value and use online search capabilities. The higher share of leisure travelers in the online channel will lead to a higher price elasticity of demand.

Based on the expected larger impact of price comparison on price elasticity and the higher share of leisure travelers online, we hypothesize that overall, air travel demand for transparent OTAs will be more price elastic than offline demand, which leads us to assert the following.

Hypothesis 1C (The Overall Offline vs. Transparent OTA Price Elasticity Hypothesis) (H1C). Overall, transparent OTA demand is more price elastic than offline demand, so that $| \eta _ { T } | > | \eta _ { O F F } |$

2.2.2. Offline vs. Opaque OTAs. As the OTA industry emerged in the 1990s, some players attempted opaque strategies to differentiate themselves from the transparent OTAs. Hotwire provides a price quote with no airline name or itinerary. Priceline.com has the patented name-your-own-price mechanism where consumers bid for a ticket with no prior information on market prices or product offerings, and they only receive final itinerary and airline carrier information when the booking is completed.

Offline agencies typically provide one or two price quotes over the phone or face to face, similar to the single price offer of an opaque site like Hotwire. On the other hand, offline travel agencies provide the airline and itinerary details while opaque sites conceal them. This difference in the product information is likely to drive the difference in price elasticity between these two channels. In line with information integration theory, we hypothesize that the lack of information about the airline carrier and the itinerary details will lead to a higher price elasticity for the opaque OTAs relative to the offline channel, as consumers turn their attention to price comparison shopping (Degeratu et al. 2000), and as they discount the value of an offer because of the lack of product information (Johnson and Levin 1985). This rationale leads to the following hypotheses.

Hypothesis 2A (The Leisure Segment Opaque OTA Price Elasticity Hypothesis) (H2A). <sub>In</sub> <sub>the</sub> leisure segment, opaque OTA demand is more price elastic than offline demand.

Hypothesis 2B (The Business Segment Opaque OTA Price Elasticity Hypothesis) (H2B). <sub>In</sub> <sub>the</sub> <sub>busi-</sub> ness segment, opaque OTA demand is more price elastic than offline demand.

Regarding channel selection, a low percentage of time-sensitive business travelers will book on the opaque channel. Indeed, in our data set, we find that 4% of business travelers who book online purchased through opaque OTAs. The consequent higher share of leisure travelers booking in the opaque channel should lead to a higher price elasticity relative to the offline channel. The magnitude of the channel selection effect is likely to be high, because very few business travelers are willing to forego information about the travel itinerary. We hypothesize as follows.

Hypothesis 2C (The Overall Offline vs. Online Opaque OTA Price Elasticity Hypothesis) (H2C). Opaque OTA demand is more price elastic than offline demand, so that $| \eta _ { O P } | > | \eta _ { O F F } |$

2.2.3. Transparent vs. Opaque OTAs. Transparent OTAs typically provide at least 50 priced offers with airline name and itinerary details. Instead, opaque OTAs provide at most one or two priced offerings, with no information on the airline carrier or the itinerary, so they offer less price comparison capabilities and less information about product attributes and quality. The FMPE hypothesis suggests that more product and price information leads to a net increase in price elasticity, so the opposite should happen when there is less product and price information: a net decrease in price elasticity. According to this inverse argument of the FMPE hypothesis, opaque OTAs should have lower price elasticity than transparent OTAs. We hypothesize that opaque OTA demand will be less price elastic because information is concealed about competitive offerings.

Hypothesis 3A (The Leisure Segment Opaque vs. Transparent OTA Price Elasticity Hypothesis) <sup>(H3A).</sup> In the leisure segment, opaque OTA demand is less price elastic than transparent OTA demand.

Hypothesis 3B (The Business Segment Opaque vs. Transparent OTA Price Elasticity Hypothesis) <sup>(H3B).</sup> In the business segment, opaque OTA demand is less price elastic than transparent OTA demand.

Regarding channel selection, there are very few business travelers in the opaque channel, while pricesensitive leisure travelers are more prone to use the opaque mechanisms. As the more price-sensitive leisure travelers gravitate to opaque OTAs, demand will be more price elastic.

Based on the above analysis of informational impacts and channel selection, the net effect is not straightforward. The lack of competitive offers in the opaque channel is likely to drive down price elasticity, while the self-selection of price-sensitive online customers into the opaque channel should have the opposite effect. We hypothesize that the channel selection effect will prevail, because of the low volume of business traffic in the opaque channel, so price elasticity in the opaque channel will be higher.

Hypothesis 3C (The Overall Opaque vs. Transparent OTA Price Elasticity Hypothesis) (H3C). Opaque OTA demand is more price elastic than transparent OTA demand, so that $| \eta _ { O P } | > | \eta _ { T } |$

## 2.3. Data

We analyzed price elasticities in the online and offline channels using a database of industry bookings sold by travel agencies through global distribution systems (GDSs) for travel between September 2003 and August 2004. The GDSs support electronic sales via the Internet, as well as sales via traditional travel agencies that provide the service through face-to-face or phone interactions. Excluded from this sample are airline direct sales, including frequent flyer award tickets, which are transacted directly through airline web portals or reservation offices. The database contains 2.21 million economy class bookings for travel between 47 different U.S. city pairs (i.e., origin and final destination cities), aggregated across airlines. We further aggregated bookings by city pair, channel, OTA type, market segment, and time of purchase. Bookings were classified as online if they were sold by an OTA, and offline otherwise. Within the online channel, an OTA was classified as transparent if the search results for the OTA included the airline name and itinerary (e.g., Orbitz, Travelocity, and Expedia), and opaque if they did not (e.g., Priceline.com’s nameyour-own-price mechanism and Hotwire’s opaque offers). The bookings were also classified based on whether the purpose of the trip was for business or leisure, and based on the weeks before departure when the booking was made.

Table 1 Descriptive Statistics

<table><tr><td>Variable</td><td>Statistic</td><td>Leisure segment</td><td>Business segment</td></tr><tr><td rowspan="3">Quantity (passenger bookings)</td><td>Mean</td><td>392.68</td><td>121.42</td></tr><tr><td>St. dev.</td><td>1,318.67</td><td>679.08</td></tr><tr><td>Range</td><td>1 – 35,810</td><td>1 – 10,499</td></tr><tr><td rowspan="3">Price (one way, US$)</td><td>Mean</td><td>142.16</td><td>262.34</td></tr><tr><td>St. dev.</td><td>69.90</td><td>211.25</td></tr><tr><td>Range</td><td>15 – 409</td><td>88 – 1,863</td></tr></table>

Notes. N = 51160. This table contains the average of quantity and price for all city pairs and channels throughout the 20-week booking window by market segment.

Data were available for a booking window of 20 weeks prior to a flight’s departure. We further classified the tickets based on peak season (June, July, August, and December 15–January 15) or offpeak season. The number of peak season tickets sold reflect supply rather than demand patterns because of capacity constraints, so we excluded peak season observations from this study. These exclusions reduced the sample to 5,160 records with aggregate information for 1.32 million tickets. Table 1 presents descriptive statistics of this reduced data set by segment. The average price was lower for the leisure segment than for the business segment, as expected.

## 2.4. Demand Modeling Preliminaries

We consider the model DEMAND = f(Price, Channel, Controls), where DEMAND is estimated in terms of quantity sold, and Price is the industry wide average price in dollars of the tickets sold for a given city pair, channel, segment, and season. We next discuss the model’s variables (see Table 2).

2.4.1. Price. The variable PRICE captures market prices across channels, segments, and city pairs. It also captures prices throughout the booking period of a flight, which can fluctuate because of airlines’ dynamic pricing practices. Airlines set fare classes that are tied to advance purchase requirements, such that the closer in time to departure, the higher is the price of a fare class (see Figure 1). Inventory management systems further refine price discrimination by opening and closing fare classes for sale based on demand forecasts (Talluri and van Ryzin 2004). Ideally, these two are synchronized, such that seats for sale are allocated to travelers with a higher willingness to pay (e.g., business travelers) as the departure time approaches. However, forecasting algorithms may overestimate demand, so sometimes seats will be offered at a lower price close to departure, as inventory managers realize that the airplane will otherwise depart with empty seats. This practice has increased over time in response to macroeconomic shocks like the 2001–2002 global economic crisis and to lowcost carriers’ everyday low-price business models (Chellappa et al. 2010). Low-fare offers close to departure can be implemented through a price reduction of a fare class, or simply by opening inventory for sale to a low-fare class. Both pricing levels and inventory management policies are reflected in our PRICE variable, because the data captures posted prices for each week before departure. Therefore we explicitly capture the dynamic price changes for any given citypair across the booking period. This is a significant improvement compared to many airline demand studies that average out prices for the whole booking period (Brons et al. 2002, Oum et al. 1993).

2.4.2. Channel Dummy Variables. We include dummy variables TRANSP and OPAQUE for the transparent and opaque OTAs, respectively, to account for their fixed effects relative to offline demand (OFFLINE). These fixed effects include service-related differences across channels and the maturity of the Internet as a distribution channel for travel services.

2.4.3. Advance Purchase. A pervasive and wellrecognized difference between consumers is the urgency of purchase (Stigler 1964). This urgency of purchase and its impact on demand is captured in the variable ADVPURCH, which contains the weeks before departure when the ticket was purchased. This variable is not typically present in academic studies of air travel demand because of the difficulty in getting the detailed data, yet it is an important driver of demand variation. The closer to departure, the higher is the demand, as the sense of urgency increases. Therefore we should see a negative relationship between ADVPURCH and demand.

Table 2 Air Travel Demand Model Variables

<table><tr><td>Type</td><td>Variable</td><td>Definition</td></tr><tr><td>Dependent</td><td>QUANTITY</td><td>Tickets sold to represent DEMAND.</td></tr><tr><td rowspan="2">Main effects</td><td>PRICE</td><td>Average price paid in dollars.</td></tr><tr><td>CHANNEL</td><td>Dummy variables for offline, transparent, and opaque OTAs.</td></tr><tr><td rowspan="4">Control</td><td>ADVPURCH</td><td>Time of purchase in weeks before the flight&#x27;s departure.</td></tr><tr><td>SEGMENT</td><td>Dummy variable for business versus leisure travel.</td></tr><tr><td>CROSSPRICE</td><td>Price of the alternative channel.</td></tr><tr><td>ORIGIN</td><td>Dummy variables for each origin city.</td></tr></table>

Figure 1 Average Price of Fare Classes  
![](/api/attachments/45AJE4K3/fulltext/images/c2fee220bc47353fb434ce89860db78f6eb3d51433b36021d015ee4f89631c11.jpg)  
Notes. This figure shows the average fares for each fare class in the data set of this study. The higher the fare class, the higher is the average price.

Effects on demand because of dynamic pricing throughout the booking period are captured by the variable PRICE. In turn, ADVPURCH will capture variation in demand that cannot be attributed to these dynamic pricing effects. This is also a significant enhancement relative to existing studies on air travel demand, which do not account for the natural variation in demand because of the urgency of purchase.

2.4.4. Segment. We include a dummy variable SEGMENT for leisure versus business travel, based on segmentation techniques by the corporate sponsor of this study. We observe lower sales for business travel relative to leisure, considering the distribution of seats that airlines assign to business and leisure travelers. As far as we know, similar to advance purchases, our study is unique in being able to segment the business versus leisure segment because this information is typically not readily available and requires significant preprocessing of sales data.

2.4.5. Cross-Channel Prices. The variable CROS-SPRICE is the price of the alternative channel, so it captures cross-channel price effects. CROSSPRICE has an opposite effect on demand as compared to price, so its relationship with demand is usually positive.

2.4.6. Origin City Dummy Variables. We assigned dummy variables for the origin cities in our sample. Origin city dummies in the econometric model allow us to control for macroeconomic or regional drivers of demand that may differ across cities, such as regional economy, population, income levels, travel preferences, hub structure of the local airports, and business activity.

## 3. Empirical Model Specification and Results

We now present our econometric model of air travel demand, together with correlation, endogeneity, and heteroskedasticity diagnostics. We then present the results of our hypothesis tests related to the priceelasticity differences across channels.

3.1. The Log-Linear Air Travel Demand Model Airline demand models in the transportation literature typically use the linear and log-linear specifications (e.g., Bhadra 2003, Oum et al. 1993, among others). We tested these two specifications against our data to determine the one with the best fit. The loglinear specification is multiplicative as follows:

$$
\begin{array}{c} Q U A N T I T Y = e ^ {\beta_ {1}} \cdot P R I C E ^ {\eta} \cdot T R A N S P ^ {\beta_ {2}} \cdot O P A Q U E ^ {\beta_ {3}} \\ \cdot A D V P U R C H ^ {\beta_ {4}} \cdot S E G M E N T ^ {\beta_ {5}} \\ \cdot C R O S S P R I C E ^ {\beta_ {6}} \cdot \prod_ {j} O R I G I N _ {j} ^ {\sigma_ {j}} \cdot e ^ {\varepsilon}, \\ \forall j \neq \text {New York}. \end{array}\tag{1}
$$

In this model,  is the price elasticity of demand. $O R I G I N _ { j }$ represents dummy variables for each origin city j except the base case of New York. We excluded the OFFLINE dummy variable in the estimation and used it as another base case for comparison. The elasticities for ADVPURCH, SEGMENT, and CROSSPRICE are represented by $\beta _ { 4 } , \beta _ { 5 } ,$ , and $\beta _ { 6 }$ . The log transformation of Equation (1) is

ln QUANTITY

$$
\begin{array}{l} = \beta_ {1} + \eta \ln P R I C E + \beta_ {2} \ln T R A N S P \\ \quad + \beta_ {3} \ln O P A Q U E + \beta_ {4} \ln A D V P U R C H \\ \quad + \beta_ {5} \ln S E G M E N T + \beta_ {6} \ln C R O S S P R I C E \\ \quad + \sum_ {j} \sigma_ {j} \ln O R I G I N _ {j} + \varepsilon . \end{array}\tag{2}
$$

We estimated Equation (2) using ordinary least squares (OLS) regression, and found an appropriate fit with an adjusted-R<sup>2</sup> of 74.7%. In contrast, the linear model’s OLS regression had an adjusted-R<sup>2</sup> of 17.2%. Therefore we adopted the log-linear specification to test our hypotheses.

## 3.2. Model Diagnostics

3.2.1. Multicollinearity. See Table 3 for pairwise correlations. There is one correlation of concern between two of the regressors, PRICE and CROSSPRICE, which is 0.82. This correlation is likely because of the common practice of airlines to price homogeneously across channels through wholesale distribution via GDSs (Chellappa and Kumar 2005).

Table 3 Pairwise Correlations for the Empirical Model Variables

<table><tr><td>Variable</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>1. QUANTITY</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2. PRICE</td><td>0.29***</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3. ADVPURCH</td><td>-0.45***</td><td>-0.10***</td><td></td><td></td><td></td><td></td></tr><tr><td>4. SEGMENT</td><td>-0.51***</td><td>0.38***</td><td>0.00</td><td></td><td></td><td></td></tr><tr><td>5. CROSSPRICE</td><td>0.05*</td><td>0.82***</td><td>-0.15***</td><td>0.00</td><td></td><td></td></tr><tr><td>6. TRANSP</td><td>0.17***</td><td>0.10***</td><td>-0.00</td><td>0.00</td><td>0.23***</td><td></td></tr><tr><td>7. OPAQUE</td><td>-0.49***</td><td>-0.46***</td><td>0.00</td><td>0.00</td><td>-0.21***</td><td>-0.47***</td></tr></table>

Notes. Significance: $^ { * } = p < 0 . 1 0 ; ^ { * * } = p < 0 . 0 5 ; ^ { * * * } = p < 0 . 0 1$ . Correlations for ORIGIN dummy variables excluded for brevity; the highest correlation between ORIGIN dummies and any other variable was 0.37. The bold font points out the high (>0.80) pairwise correlation.

Further examination of this correlation led us to exclude the variable CROSSPRICE from the model for three reasons. First, the variance inflation factor of CROSSPRICE in the log-linear OLS regression was 22.03, which is above the threshold that is econometrically tolerable (Kennedy 1998). Second, when CROSSPRICE was included, the coefficient of ln PRICE was positive and that of ln CROSSPRICE was negative, which would wrongly suggest an upward sloping demand curve. Therefore the inclusion of this variable leads to inaccurate estimates of the variable of interest. Third, the correlation between CROSSPRICE and QUANTITY is low $( \sigma = 0 . 0 5 ,$ $p { = } 0 . 0 7 )$ , and the regression including CROSSPRICE only added 1.5% to the model fit $R ^ { \overset \vartriangle }$ statistic, compared to the regression without it. The rationale for this lack of explanatory power of CROSSPRICE may be that travelers seldom engage in cross-channel shopping.<sup>1</sup> This is because the cross-channel prices are relatively homogeneous in the U.S. air travel market (Chellappa and Kumar 2005, PhoCusWright 2004), in part, because U.S. airlines have gradually abolished online-only fares and promotions to bring order to the guerrilla pricing tactics that had started to impact the discipline of industry prices. Therefore, given the high risk of misspecification of the model and the low contribution of CROSSPRICE as an explanatory variable, we report results for a reduced model that excludes this variable in spite of its apparent prima facie relevance.

3.2.2. Heteroskedasticity. We performed a Breusch and Pagan (1979) Lagrange multiplier test for heteroskedasticity at the level of the model, against the fitted values of lnQUANTITY. We rejected the hypothesis of constant variance or homoskedasticity $( \dot { \chi } ^ { \bar { 2 } } = 1 7 7 . 4 7 , \ \mathrm { d . f . } = 1 , \ p < 0 . 0 1 )$ . We conclude that there is heteroskedasticity in the econometric model, although this test cannot diagnose exactly what its source is. One potential source of heteroskedasticity is PRICE. Demand in higher price ranges may exhibit higher variation because of the heterogeneity of consumers (both business and leisure travelers) at high prices. Based on the observation that PRICE might account for heteroskedasticity, we ran a second test by Goldfeld and Quandt (1965). We consider a known source of heteroskedasticity $( \mathrm { i . e . , \ v a r } [ \varepsilon _ { i } ] = \sigma _ { i } ^ { 2 } = \sigma _ { i } ^ { 2 } z _ { i } ,$ with $z _ { i } = P R I C E )$ . We were not able to reject the null hypothesis of homoskedasticity $( p < 0 . 1 7 )$ . To correct for other possible unknown sources of heteroskedasticity, we estimated the regressions using the Huber-White robust estimators of the standard error.

3.2.3. Endogeneity. In demand models, there is an inherent risk of endogenously generated prices, which can lead to misspecification of the empirical model because of a high correlation between prices and the residuals. This correlation between prices and the residuals can yield inconsistent estimators. In particular, in the air travel industry, there is simultaneity in the determination of demand and prices, because airline pricing managers set prices based on existing bookings and historical sales, yet sales are affected by prices.<sup>2</sup> We addressed this potential endogeneity problem by performing a two-stage least squares (2SLS) regression with instrumental variables for PRICE. We used the following cost-side instrumental variables, which are appropriate to solve endogeneity problems in demand models (Berry et al. 1995):

• STG\_LENGTH. An often-used predictor of price is stage length, a city-pair’s trip distance in air travel miles. This variable has been used in prior studies of airline performance, as noted by Duliba et al. (2001). The impact of stage length on prices is two-fold. First, it is directly related to variable costs such as fuel and crew expenses. Second, for shorter distances, air travel prices will be affected by prices of alternate modes of transportation such as trains and automobiles (Brons et al. 2002).

• MKT\_CONC. The degree of market concentration in a specific city pair influences market prices (Borenstein 1992). We measured market concentration at the city-pair level using the Herfindahl index, or the sum of squares of the market shares of the different airlines.

• HUB. Hub operations have been associated with higher prices in the industry (Chellappa et al. 2010), so we incorporate a HUB variable to indicate whether the city-pair origins and destinations are hubs of an airline. This variable also controls for the effect on price of multimarket competition (Gimeno 1999), whereby airlines set a foothold in a competitor’s hub to retaliate or to deter actions of the competitor in their own hub.

## 3.3. Results

We re-ran the air travel demand model without CROSSPRICE to control for multicollinearity, and as a 2SLS regression with instrumental variables for PRICE to control for endogenous prices. We report results with Huber-White robust standard errors to account for heteroskedasticity (see Table 4).

To test for endogeneity, we performed a generalized Hausman test for the null hypothesis that the OLS estimator is consistent, and the hypothesis was rejected $( \chi ^ { 2 } = 1 6 2 . 6 7 , ~ \mathrm { d . f . } = 1 4 , ~ p < 0 . { \dot { 0 } } { \dot { 0 } } 1 )$ . Thus we found that there is a risk of misspecification because of endogenously generated prices, and going forward we report and interpret the results using the estimates of the 2SLS regression.

The reduced 2SLS model has an adjusted-R<sup>2</sup> of 72.47%. The magnitudes and signs of the coefficients are as expected. The results suggest that overall, air travel demand is approximately unit elastic $( \eta = - 1 . 0 3 , \mathtt { S . E . } = 0 . 0 8 , p < 0 . 0 1 )$ . The dummy variables for the transparent and opaque OTAs are negative $( \beta _ { 2 } = - 1 . 9 5 , ^ { \circ } \mathrm { S . E . } = 0 . 0 6 , ^ { \circ } p < 0 . 0 1 , \beta _ { 3 } = - 4 . 4 \bar { 1 }$ $\mathrm { S . E . } = 0 . 0 9 , p < 0 . 0 1 )$ , which is in line with the actual lower share of online sales relative to offline sales during the 2003–2004 period.<sup>3</sup> The advance purchase variable has a negative relationship with demand $( \beta _ { 4 } = - 1 . 4 7 , \mathrm { S . E . } = \mathrm { } 0 . 0 3 , \mathrm { } p < 0 . 0 1 )$ , so the farther in time from departure, the lower will be the demand. This makes sense because airline seats are a perishable commodity, and thus demand will be higher closer to departure. The SEGMENT variable has a negative coefficient $( \beta _ { 5 } = - 2 . 0 5 , \mathrm { ~ S . E . } = 0 . 0 5 , \mathrm { ~ } p < 0 . 0 1 )$ , in line with the expectation that business demand is lower than leisure demand.

Table 4 Air Travel Demand Model: 2SLS and OLS Regressions

<table><tr><td rowspan="2">Variable</td><td colspan="3">2SLS reduced model</td><td colspan="3">OLS reduced model</td></tr><tr><td>Coefficient (robust SE)</td><td>t</td><td>p</td><td>Coefficient (robust SE)</td><td>t</td><td>p</td></tr><tr><td colspan="7">Main effects</td></tr><tr><td> $\eta$  (PRICE)</td><td>-1.03*** (0.08)</td><td>-12.67</td><td>0.001</td><td>-0.14*** (0.04)</td><td>-3.40</td><td>0.001</td></tr><tr><td> $\beta_1$  (CONSTANT)</td><td>14.11*** (0.46)</td><td>30.91</td><td>0.001</td><td>9.30*** (0.25)</td><td>36.96</td><td>0.001</td></tr><tr><td> $\beta_2$  (TRANSP)</td><td>-1.95*** (0.06)</td><td>-34.76</td><td>0.001</td><td>-1.56*** (0.05)</td><td>-34.35</td><td>0.001</td></tr><tr><td> $\beta_3$  (OPAQUE)</td><td>-4.41*** (0.09)</td><td>-48.57</td><td>0.001</td><td>-3.55*** (0.06)</td><td>-59.40</td><td>0.001</td></tr><tr><td colspan="7">Controls</td></tr><tr><td> $\beta_4$  (ADVPURCH)</td><td>-1.47*** (0.03)</td><td>-58.46</td><td>0.001</td><td>-1.36*** (0.02)</td><td>-59.40</td><td>0.001</td></tr><tr><td> $\beta_5$  (SEGMENT)</td><td>-2.05*** (0.05)</td><td>-38.92</td><td>0.001</td><td>-2.47*** (0.04)</td><td>-61.47</td><td>0.001</td></tr><tr><td> $\sigma_1$  (ORIGIN $_1$ )</td><td>0.35*** (0.11)</td><td>-3.34</td><td>0.001</td><td>-0.48*** (0.10)</td><td>-4.73</td><td>0.001</td></tr><tr><td> $\sigma_2$  (ORIGIN $_2$ )</td><td>0.77*** (0.12)</td><td>-6.43</td><td>0.001</td><td>-0.64*** (0.11)</td><td>-5.53</td><td>0.001</td></tr><tr><td> $\sigma_3$  (ORIGIN $_3$ )</td><td>-0.19** (0.09)</td><td>-2.05</td><td>0.040</td><td>-0.19** (0.09)</td><td>-2.19</td><td>0.029</td></tr><tr><td> $\sigma_4$  (ORIGIN $_4$ )</td><td>0.20* (0.11)</td><td>1.77</td><td>0.077</td><td>0.08*** (0.11)</td><td>0.71</td><td>0.479</td></tr><tr><td> $\sigma_5$  (ORIGIN $_5$ )</td><td>-0.75*** (0.11)</td><td>-6.88</td><td>0.001</td><td>-0.78*** (0.10)</td><td>-7.42</td><td>0.001</td></tr><tr><td> $\sigma_6$  (ORIGIN $_6$ )</td><td>0.07*** (0.09)</td><td>-0.80</td><td>0.421</td><td>-0.18** (0.09)</td><td>-2.09</td><td>0.037</td></tr><tr><td> $\sigma_7$  (ORIGIN $_7$ )</td><td>-0.04*** (0.11)</td><td>-0.34</td><td>0.733</td><td>-0.07*** (0.10)</td><td>-0.71</td><td>0.475</td></tr><tr><td> $\sigma_8$  (ORIGIN $_8$ )</td><td>0.03*** (0.11)</td><td>0.24</td><td>0.812</td><td>-0.07*** (0.11)</td><td>-0.69</td><td>0.490</td></tr><tr><td> $R^2$  (Adj.- $R^2$ )</td><td colspan="3">72.54% (72.47%)</td><td colspan="3">74.72% (74.66%%)</td></tr></table>

Notes. N = 51160. Models: OLS and 2SLS log-linear regressions with robust errors to handle heteroskedasticity. Reduced model excludes CROSSPRICE. Significance: $^ { * } = p < 0 . 1 0 , ^ { * * } = p < 0 . 0 5 , ^ { * * * } = p < 0 . 0 1$

## 3.4. Economy Class Price Elasticities: Business and Leisure Combined

To estimate price elasticity differences across channels econometrically, recall that in the log-linear model, we set the power of PRICE () as the price elasticity. We used the following econometric specification, in line with Granados et al. (2008), which breaks the power of price into the base elasticity for the transparent OTAs and its difference with respect to the elasticity of the offline travel agencies and opaque OTAs:

$$
\begin{array}{c} Q U A N T I T Y = e ^ {\beta_ {1}} \cdot P R I C E ^ {\eta_ {T} + \lambda_ {1} O F F L I N E + \lambda_ {2} O P A Q U E} \\ \cdot A D V P U R C H ^ {\beta_ {4}} \cdot S E G M E N T ^ {\beta_ {5}} \\ \cdot \prod_ {j} O R I G I N _ {j} ^ {\sigma_ {j}} \cdot e ^ {\varepsilon}. \end{array}\tag{3}
$$

In this model, $\eta _ { T }$ is the price elasticity of the transparent ${ \mathrm { O T A s } } ,$ and it is the base elasticity. The parameter $\lambda _ { 1 }$ represents the difference between the price elasticity of the transparent OTAs and the offline channel, so $\eta _ { O F F } = \eta _ { T } + \lambda _ { 1 }$ . The parameter $\lambda _ { 2 }$ represents the difference between the price elasticity of the transparent OTAs and the opaque OTAs, so $\eta _ { O P } =$ $\eta _ { T } + \lambda _ { 2 } .$ . Taking the log transformation of Equation (3) leads to

$$
\begin{array}{r l} \ln Q U A N T I T Y & = \beta_ {1} + \eta_ {T} \ln P R I C E + \lambda_ {1} \ln P R I C E \\ & \cdot O F F L I N E + \lambda_ {2} \ln P R I C E \cdot O P A Q U E \\ & + \beta_ {4} \ln A D V P U R C H + \beta_ {5} \ln S E G M E N T \\ & + \sum_ {j} \sigma_ {j} \ln O R I G I N _ {j} + \varepsilon . \end{array} \tag {4}
$$

To estimate this model, we computed the new variables ln PRICE·OFFLINE and ln PRICE·OPAQUE, and included each one as a regressor in our estimations. The results are shown in Table 5. The 2SLS regression using this model has an adjusted-R<sup>2</sup> of 72.69%.

Table 5 Price Elasticities by Channel: Business and Leisure Combined

<table><tr><td>Variable</td><td>Coefficient (robust SE)</td><td>t</td><td>p</td></tr><tr><td colspan="4">• Main effects</td></tr><tr><td> $\eta_T$ </td><td>-1.11*** (0.08)</td><td>-13.39</td><td>0.001</td></tr><tr><td> $\lambda_1 (\eta_{OFF} - \eta_T)$ </td><td>0.38*** (0.01)</td><td>33.76</td><td>0.001</td></tr><tr><td> $\lambda_2 (\eta_{OP} - \eta_T)$ </td><td>-0.53*** (0.01)</td><td>-40.92</td><td>0.001</td></tr><tr><td> $\beta_1 (CONSTANT)$ </td><td>12.53*** (0.43)</td><td>29.27</td><td>0.001</td></tr><tr><td colspan="4">• Controls</td></tr><tr><td> $\beta_4 (ADVPURCH)$ </td><td>-1.46*** (0.03)</td><td>-58.47</td><td>0.001</td></tr><tr><td> $\beta_5 (SEGMENT)$ </td><td>-2.13*** (0.05)</td><td>-41.25</td><td>0.001</td></tr><tr><td> $R^2 (Adjusted-R^2)$ </td><td colspan="3">72.76% (72.69%)</td></tr></table>

Notes. N = 51160. 2SLS model estimation. Significance: $^ { * } = p < 0 . 1 0$ $^ { * * } = p < 0 . 0 5 , ^ { * * * } = p < 0 . 0 1$ . Other control variables omitted for brevity.

3.4.1. Transparent-Offline Comparison. The price elasticity for the transparent OTAs was found to be elastic at −1.11 $( \eta _ { T } = \bar { - 1 } . 1 1 , \mathrm { S . E . } = 0 . 0 8 , p < 0 . 0 1 )$ . The estimate of $\lambda _ { 1 }$ is $0 . 3 8 \ ( \lambda _ { 1 } = 0 . 3 8 , \mathrm { S . E . } = 0 . 0 1 , p < 0 . 0 1 )$ so the price elasticity estimate of the offline channel is $\eta _ { O F F } = \eta _ { T } + \lambda _ { 1 } = - 0 . 7 3$ . We find support for H1C. Demand for the transparent OTAs is more price elastic than that of the offline channel.

3.4.2. Opaque-Offline Comparison. The estimate of $\lambda _ { 2 }$ or the difference between the price elasticity of the opaque OTAs channel and the transparent OTAs $\mathrm { i s } - 0 . 5 3 \ : ( \lambda _ { 2 } = - 0 . 5 3 , \mathrm { S . E . } = 0 . 0 1 , p < 0 . 0 1 ) .$ , so the price elasticity of the opaque channel is $\eta _ { O P } = \eta _ { T } + \lambda _ { 2 } =$ −1064. The difference between the price elasticity of the opaque OTAs and the offline channel is $\eta _ { O P } -$ $\eta _ { O F F } = \lambda _ { 2 } - \lambda _ { 1 } = - 0 . 9 1$ . Therefore we find support for H2C, that the price elasticity of opaque OTAs is higher than that of the offline OTAs.

3.4.3. Transparent-Opaque Comparison. Since $\lambda _ { 2 } = - 0 . 5 3 ,$ the price elasticity of the opaque OTAs is higher than that of the transparent OTAs, so we find support for H3C. Opaque OTA demand is more price elastic than transparent OTA demand. See Figure 2 for a graphical representation of the results.

Figure 2 Price Elasticity Comparison Across Channels: Economy Class  
![](/api/attachments/45AJE4K3/fulltext/images/fda63e2349e2c37bcb7ab1c51dcd4654a0d0cb704691ed4faa2873f626584f84.jpg)  
Note. This graph depicts the relative price elasticities for the economy class cabin (business and leisure combined).

## 3.5. Price Elasticities by Segment

We performed price elasticity comparisons across channels by segment (see the results in Table 6). The results suggest that the directional differences in price elasticity across channels hold in relation to the Economy class cabin, with some nuances.

3.5.1. Transparent-Offline Comparison. We find support for H1A. The price elasticity of the transparent OTAs is higher than that of the offline channel for leisure travel (Leisure $\lambda _ { 1 } = 0 . 2 3 , \mathrm { S . E . } = 0 . 0 1 ,$ $p < 0 . 0 1 )$ . The price elasticity of the transparent OTAs is also higher than the offline channel for the business segment (Business $\lambda _ { 1 } = 0 . 5 5 , \mathrm { S . E . } = 0 . 0 4 , p < 0 . 0 1 )$ , so H1B was rejected. We not only find that the business segment is more price elastic online, but also the magnitude of the difference with respect to the offline channel is higher relative to that of the leisure segment. This finding is counter-intuitive, because we would expect the cross-channel difference in price elasticity to be lower for a differentiated market like business travel. We discuss this result further in the next section.

3.5.2. Opaque-Offline Comparison. The difference between the price elasticity of the opaque OTAs and the offline channel in the leisure segment is $\eta _ { O P } -$ $\eta _ { O F F } = \lambda _ { 2 } - \lambda _ { 1 } = - 0 . 9 5$ . The analogous result for the business segment is $\eta _ { O P } - \eta _ { O F F } = - 0 . 9 5$ . Therefore we find support for H2A and H2B. The demand for opaque OTAs is more price elastic than that of the offline channel in both the leisure and business segments by almost one elasticity point.

3.5.3. Transparent-Opaque Comparison. We find that the price elasticity of the opaque channel is higher than that of the transparent OTAs in both segments (Leisure $\lambda _ { 2 } = - 0 . 7 2 , \bar { \mathrm { S . E . } } = 0 . 0 1 , p < 0 . 0 1$ , and Business $\lambda _ { 2 } = - 0 . 4 0 , { \mathrm { S . E . } } = 0 . 0 4 , p < 0 . 0 1 )$ , so we reject H3A and H3B. Figure 3 depicts these results.

## 4. Analysis and Discussion

In the previous section, we estimated the demand functions of the online and offline air travel channels.

Table 6 Price Elasticities Comparison by Channel by Segment

<table><tr><td rowspan="2">Variable</td><td colspan="3">Leisure</td><td colspan="3">Business</td></tr><tr><td>Coefficient (robust SE)</td><td>t</td><td>P</td><td>Coefficient (robust SE)</td><td>T</td><td>P</td></tr><tr><td> $\eta_T$ </td><td>-1.56*** (0.07)</td><td>-12.87</td><td>0.001</td><td>-0.89*** (0.25)</td><td>-6.16</td><td>0.001</td></tr><tr><td> $\lambda_1 (\eta_{OFF} - \eta_T)$ </td><td>0.23*** (0.01)</td><td>21.78</td><td>0.001</td><td>0.55*** (0.04)</td><td>15.03</td><td>0.001</td></tr><tr><td> $\lambda_2 (\eta_{OP} - \eta_T)$ </td><td>-0.72*** (0.01)</td><td>-56.89</td><td>0.001</td><td>-0.40*** (0.04)</td><td>-10.45</td><td>0.001</td></tr><tr><td> $\beta_1 (CONSTANT)$ </td><td>11.26*** (0.34)</td><td>32.63</td><td>0.001</td><td>13.24*** (1.44)</td><td>9.17</td><td>0.001</td></tr><tr><td> $\beta_4 (ADVPURCH)$ </td><td>-1.30*** (0.04)</td><td>-35.04</td><td>0.001</td><td>-1.70*** (0.07)</td><td>-23.87</td><td>0.001</td></tr></table>

Notes. For each segment, N = 21580. 2SLS model estimation. Significance: $^ { * } = p < 0 . 1 0 , ^ { * * } = p < 0 . 0 5 , ^ { * * * } = p < 0 . 0 1$ . Other control variables omitted for brevity.

We found that the price elasticity is higher in the OTA channel than in the offline channel, for both transparent and opaque OTAs. Online demand is more price elastic than offline demand in both business and leisure segments. Within the online channel, opaque OTA demand is more price elastic than that of transparent OTAs. Table 7 summarizes these results.

## 4.1. The FMPE Hypothesis

One of the tenets of perfect competition is that consumers are more sensitive to price changes in markets with lower search costs, because they have more access to substitute offerings. The finding that the online channel is more price elastic than offline demand is consistent with the notion that less friction in the form of lower search costs will lead to higher price elasticity of demand, and hence more intense competition. Yet, based on the results, we contend that the price elasticity effect of the online channel is not straightforward. There are multiple forces at play, and the results of this study provide clues on the drivers of differences in price elasticity across channels, for both commodity and differentiated markets like leisure and business travel.

4.1.1. Commodity Markets: The Leisure Segment. In the leisure market, U.S. airlines struggle to stay profitable, one of the signs of the Bertrandlike competitive behavior that leads to marginal cost pricing. Compared to decades ago, domestic airlines have stripped their onboard economy class service of quality differentiators such as premium meals and amenities—and most recently, even peanuts and crackers.

Our findings suggest that in such commodity markets, the net effect of the ability to compare offerings online via transparent OTAs will be an increase in price elasticity, which may, in turn, exacerbate the commoditization of the product. Not surprisingly, airlines have been reluctant to aggressively penetrate the online market, and it was only after several independent OTAs gained significant share in the late 1990s that they decided to reintermediate the online channel (Chircu and Kauffman 2000, Granados et al. 2006). Travelers, on the other hand, take advantage of the Internet channel to shop for low prices. A study by comScore, Inc. (2006), an Internet research and consultancy firm, reported that in 2005, the OTA market reached more than \$40 billion in revenues, and price was the number one reason for consumers to return to a site to book air travel.

Figure 3 Price Elasticities by Channel and Segment  
![](/api/attachments/45AJE4K3/fulltext/images/557a423571bc256d2a69762adaddcfe0dd7cec02ef5511602d91d65cf1cea683.jpg)

4.1.2. Differentiated Markets: The Business Segment. In the business segment, we find that transparent OTA demand is more price elastic than offline demand. Therefore our results are consistent with the frictionless markets hypothesis not just for commodity products like leisure travel, but also for differentiated markets like business travel. The higher price elasticity that we find online for business travel is in contrast with Degeratu et al. (2000) and Lynch and Ariely (2000), who found that price sensitivity was lower online for groceries and premium wines. These apparently contradictory findings can be reconciled in the following two ways:

• Gradually emerging impacts in differentiated markets. Perhaps over time, travelers have become experienced in searching, so they are able to better exploit the Internet to shop for lower prices, even when differentiation and brand matter. Therefore the expected effect of the Internet on price elasticity may be gradually emerging—rather than emerging abruptly—for differentiated markets, and that is why we see higher price elasticity in this study versus previous studies.

• Metasearch. The emergence of metasearch engines for travel such as Kayak (www.kayak.com) and Sidestep (www.sidestep.com) may be stripping air travel distributors of the possibility to obfuscate information even for business travelers. In contrast, in other industries where online price search engines are not as developed, firms are still in a position to conceal prices of competing alternatives. For example, Ellison and Ellison (2009) studied prices in an online search engine and found signs of obfuscation of consumer search by concealing shipping costs and forcing firm-by-firm product search. Oh and Lucas (2006) also found evidence that online vendors change pricing strategies frequently, making it difficult for consumers to learn their pricing strategies.

We also found that the elasticity differential of 0.55 between transparent OTAs and the offline channel in the business segment is higher in magnitude than the analogous 0.38 differential for the leisure segment. Yet, the impact on price elasticity of the online channel should theoretically be lower in differentiated markets like business travel than in commoditized markets like leisure travel. Because price information is less important to business travelers, an increase in the ability to compare competitive offerings should have a lower impact on price elasticity for the business segment. Moreover, business travelers are less concerned about booking the lowest price because the airline ticket is typically paid by the firm. Possible explanations for this counterintuitive result are as follows:

Table 7 Summary of Results: Relative Price Elasticities Across Channels and Segments

<table><tr><td>Segment</td><td>Hypotheses on relative price elasticities</td><td>Theoretical arguments</td><td>Empirical results</td></tr><tr><td rowspan="4">Business and leisure</td><td>Leisure H1A:  $|\eta_T| > |\eta_{OFF}|$ </td><td>FMPE hypothesis: More price comparison leads to higher elasticity in commodity markets.</td><td>Supported.  $\lambda_1 > 0$ </td></tr><tr><td>Business H1B:  $|\eta_T| < |\eta_{OFF}|$ </td><td>Information integration theory: More product information leads to lower elasticity in differentiated markets.</td><td>Rejected.  $\lambda_1 > 0$ </td></tr><tr><td>H2A, H2B:  $|\eta_{OP}| > |\eta_{OFF}|$ </td><td>Information integration theory (inverse): Less product information leads to higher elasticity.</td><td>Supported for business and leisure.  $\lambda_2 - \lambda_1 > 0$ </td></tr><tr><td>H3A, H3B:  $|\eta_T| > |\eta_{OP}|$ </td><td>FMPE hypothesis (inverse): Less price comparison leads to a lower elasticity.</td><td>Rejected for both business and leisure.  $\lambda_2 < 0$ </td></tr><tr><td rowspan="3">Total—economy class</td><td>H1C:  $|\eta_T| > |\eta_{OFF}|$ </td><td>FMPE hypothesis: More price comparison leads to higher elasticity.Channel selection: More leisure travelers buy online.</td><td>Supported.  $\lambda_1 > 0$ </td></tr><tr><td>H2C:  $|\eta_{OP}| > |\eta_{OFF}|$ </td><td>Information integration theory: More product information leads to lower elasticity.Channel selection: More leisure travelers buy opaque.</td><td>Supported.  $\lambda_2 - \lambda_1 > 0$ </td></tr><tr><td>H3C:  $|\eta_T| > |\eta_{OP}|$ </td><td>FMPE hypothesis (inverse): Less price comparison leads to a lower elasticity.Channel selection: More leisure travelers buy opaque.</td><td>Supported.  $\lambda_2 < 0$ </td></tr></table>

Note. FMPE hypothesis stands for frictionless markets price elasticity hypothesis.

• Higher and Lower Price Points Matter. Business travelers typically pay higher prices than leisure travelers, so some of them may be more sensitive to price comparison capabilities across channels. That is, for the same improvement in availability of market information across segments, the impact on price elasticity may be higher at higher price points if there is a limited budget. Such may be the case particularly for business travelers with a cap on spending and for business executives of small- and medium-sized firms.

• Offline Base Elasticity Estimates Are Lower. Business travelers are less likely to search actively in the offline channel than the leisure traveler, because they would rather use the time for other more valuable tasks. Therefore, the base elasticity in the offline channel is quite low for business travelers (i.e., very inelastic at −0.34). In contrast, leisure travelers spend more time shopping for lower prices, even in the offline channel, so the analogous base elasticity for the leisure segment is relatively higher (i.e., elastic at −1.33). With access to the online channel, business travelers are able to engage in very efficient search at a low cost, so they benefit more from the transparency of the online channel. Therefore you will see a higher magnitude in the increase of the price elasticity of the business segment, relative to the leisure segment.

• Online Price Elasticity Estimates May Be Understated. We tried to control for seat capacity constraints by using offpeak period data and by performing the analysis at the industry level. (In §5, we show how this approach reduces the risk of bias in our results.) Nevertheless, there may have been a shortage of supply that caused passenger spill mainly of leisure travelers. If this is the case, both online and offline price elasticity estimates in this study are downward biased, but this downward bias may be more evident in the online channel because of a disproportionate spill of leisure travelers who tried to book online but found no seats available.

• Managed Travel Services May Induce Higher Price Sensitivity. Corporate travel agencies and travel departments have dedicated resources and advanced search technologies to manage corporate travel arrangements. Included in their portfolio of tools are online search capabilities. Also, business travel is managed by expert staff that may have “tricks of the trade” to find lower prices. Therefore, better online resources and search expertise may induce higher sensitivity to prices as corporate travel managers are better able to find the best price for a given itinerary.

## 4.2. Opaqueness and the Inverse of the FMPE Hypothesis

If higher price comparison capabilities lead to a higher price elasticity of demand, a lower ability to compare products and prices should lead to a lower price elasticity. Based on this inverse statement of the FMPE hypothesis, because opaque OTAs make search costs higher, the result should be a lower price elasticity when controlling for the self-selection effect. Our results are not consistent with this argument, because we find that for both leisure and business segments, demand for opaque OTAs is more price elastic than transparent OTAs. Possible explanations are as follows:

• Discounting Product Value When Product Information Is Missing. The lack of relevant information on product characteristics and quality also can increase price elasticity to the point where it undermines the effect of price information. Consumers are likely to discount the value of an offer if the core product information is missing. Therefore the impact of the lack of information on the itinerary and the airline carrier may have a higher impact than the lack of price information, for a net increase in price elasticity.

• Additional Self-Selection May Also Influence Price Sensitivity. There may be further self-selection within the online channel not captured in our data. That is, more price-sensitive leisure travelers $( \mathrm { e . g . } ,$ , college students) may gravitate toward the opaque OTAs, which would explain the higher observed price elasticity of the opaque channel compared to the transparent OTAs.

## 4.3. Product Information and Information Integration Theory

Information integration theory suggests that more product information should decrease the importance that price or brand have on a purchase decision. Likewise, less product information should lead to a higher focus on price comparison, which will increase price elasticity. The main difference between opaque OTAs and offline agencies is the lack of product information, so travelers using opaque mechanisms will be relatively more sensitive to price changes. Our finding that opaque OTA demand is more price elastic than offline demand is consistent with this theoretical argument.

This result has strategic implications for opaque OTAs and other market players (Granados et al. 2010). Because opaque OTA demand is very price elastic, the opaque market price should be significantly lower than the retail price, in line with the degree of opaqueness. On the other hand, for transparent OTAs and other online players, this result underscores the importance of designing online mechanisms that emphasize information about product attributes. Otherwise, the lack of information about product attributes is likely to compound the negative effect of price information, leading to substantially price-elastic and competitive markets. For brick-and-mortar suppliers with an online presence, a sound multichannel strategy will include the design of online selling mechanisms that make product attributes transparent to the customer, which will mitigate the negative impact on demand of price comparison capabilities. They should also collaborate with intermediaries in the online channel to bring product attribute information to consumers in a transparent manner.

## 4.4. Channel Selection

Our results show that more price-sensitive leisure travelers gravitate to channels with lower search costs and higher price comparison capabilities. Part of the reason why we observe higher price elasticity online is the disproportionate set of leisure travelers who buy tickets in this channel. In contrast, a high proportion of business travelers book offline, perhaps because they prefer the convenience of an assisted purchase that satisfies their complex needs and their high value of time. This channel self-selection effect partially explains the higher price elasticity in the online channel for the economy class as a whole.

In our study, the channel selection effect increases the magnitude of the higher price elasticity observed online, because of the disproportionate share of leisure travelers who book online. To assess the extent to which channel self-selection affects our results, we compared the price elasticities for transparent OTAs and the offline channel with an aggregated data set for economy class that does not separate business and leisure records. This data are representative of many studies where there is no information to induce customer heterogeneity. The result based on this data set is an elasticity difference between transparent OTAs and the offline channel of $\lambda _ { 1 } = 0 . 4 9$ . In contrast, the result accounting for self-selection in our analysis is $\lambda _ { 1 } = 0 . 3 8$ . Therefore the self-selection effect roughly accounts for approximately 0.11 of the 0.49 elasticity differential or 22%. The remaining 0.38 elasticity points or 78% of the difference can be attributed to the channel-specific differences, including the product and price information provided. We may have not fully accounted for customer heterogeneity, so the mix of travelers may explain more than the 22% of the price elasticity differential across channels, but this is a step in the right direction relative to most air travel studies where customer heterogeneity is not accounted for.

## 5. Conclusions

We conclude with implications of our findings for academics and practitioners. We note challenges and insights for competitive strategy. We also discuss our contributions, limitations, and future research.

## 5.1. Theoretical and Methodological Contributions

5.1.1. Theoretical Contributions. We offer several empirical contributions related to price elasticity, market prices, price dispersion, and evidence of consumer self-selection.

Online Price Elasticity, Market Prices, and Price Dispersion. An increase in price elasticity is one of the four expected economic consequences of electronic markets, yet there has been little empirical evidence to support or reject this proposition. So far, academic research has focused mostly on price level and price dispersion comparisons across channels—two other expected impacts—because of the availability of price data on the Internet. In this paper, we used a data set that contains both sales and prices in online and offline channels. This is one of the first studies to provide comparable analysis of sales data in the online and offline channels. We have been able to test both the FMPE hypothesis in the context of price information availability and information integration theory in the context of product information availability. We find that, together, these theories are complementary in their ability to explain the impact of Internetenabled market transparency on demand.

Our results offer a future avenue for research to reconcile the apparently contradictory findings in the studies of online market prices and price dispersion, in the sense that price elasticity can drive prices in both directions (Ghose and Yao 2010). In this research, we have shown that it is not always the case that an increasingly frictionless market will lead to higher price elasticity of demand. Instead, it seems to depend on the type of information provided and on the degree to which heterogeneous consumers gravitate toward a channel because of the information provided. Depending on the specific information displayed and the impact of the channel selection effect, price elasticity online may be higher or lower than what is observed offline. If the impact of price comparison prevails, price elasticity will be higher. Otherwise, consumers may place higher weight on product characteristics and quality information, which may decrease price elasticity. Channel self-selection can drive price elasticity in both directions, depending on the segments of the market that gravitate to either channel. These demand-side effects on price elasticity suggest that market prices and price dispersion will not always be lower online, and it will depend, in part, on the net impact of the drivers of price elasticity that we have identified in this study.

Evidence of Self-Selection. Self-selection is an expected consequence of offering different levels of service quality across channels. In particular, based on the informational features of a channel, different types of consumers will have the propensity to transact in different channels. This is one of the first studies that offers empirical support for the presence of channel self-selection. We provide evidence that the mix of business and leisure travelers is different across channels, which partially explains the differences in price elasticities.

5.1.2. Methodological Contributions. Our analysis contributes to air travel demand research because we bring a level of detail not covered so far in the literature. Our contributions were made possible by our access to microdata on economy class bookings by channel, segment, and advance purchase, and to cost-side instrumental variables to solve endogeneity problems.

Demand Model with Sales Data. We have used sales data to estimate and compare price elasticities across channels, which is a more direct method than existing studies that approximate price elasticity using sales rank data from online retailers like Amazon (e.g., Brynjolfsson et al. 2003, Chevalier and Goolsbee 2003, Ellison and Ellison 2009, Ghose et al. 2006). Our analysis of massive sales data is also complementary to the results from experimental methods to estimate price elasticities, as in Lynch and Ariely (2000). They performed experiments to induce demand with transparency level as the treatment variable, while our study uses actual sales to estimate the demand function and the price elasticities.

The econometric method that we use in this study to analyze cross-channel price elasticities can also be used to compare price elasticities across multiple market dimensions (e.g., regional comparisons, citypair comparisons) and product attributes (e.g., price premium sensitivity for upgraded services). Airlines also can use elasticity estimates to make strategic pricing decisions and to design online selling mechanisms according to the expected price elasticity effects.

Customer Heterogeneity. The microdata that we used in our analysis are broken down by market segment with business versus leisure travelers, so we are able to control for customer heterogeneity in the demand model. We find that the different mix of business and leisure travelers in each channel affects the observed price elasticities, which corroborates the importance of accounting for customer heterogeneity to obtain unbiased price elasticity estimates (Bijmolt et al. 2005).

Advance Purchase. Most air travel demand studies use data that do not contain the date a ticket was booked. Yet, how far in advance an airline ticket is purchased is an important driver of demand in air travel. We address this in two ways. First, our data contain prices by weeks before departure, so we explicitly capture the different prices that arise because of pricing and inventory management tactics. Second, we include an advance purchase variable, ADVPURCH, as a regressor to control for demand variation because of the urgency of purchase, which is not accounted for by PRICE. This is an improvement compared to many airline demand studies that average out prices for the whole booking period and that do not account for the urgency of purchase (Brons et al. 2002, Oum et al. 1993).

Endogeneity of Prices in Demand Models. A common problem in demand estimation is the simultaneity of demand and prices. Demand is affected by prices, but in the airline industry prices are endogenously set by firms. This is because airline firms adjust their prices continuously based on dynamic evaluation of demand forecasts throughout the booking period. This endogeneity of prices can create a specification problem for our econometric model of travel demand by making the endogenous variable correlated with the model’s error terms. To solve for this, the econometric problems associated with endogeneity, we offer cost-side instruments that are appropriate in this setting. Cost data are private and closely guarded to most competitive firms, so it is typically difficult to obtain for research purposes. We used the HUB variable for each origin city and the STG\_LENGTH variable for each city-pair as cost-side instruments for the PRICE variable. Data on these instruments are publically available, so we offer them as cost-side instruments that are effective and accessible for future air travel demand studies.

## 5.2. Implications for Pricing, Multichannel Strategy, and IT Strategy

The findings of this study represent both managerial challenges and opportunities. Our validation that the online channel is more price elastic than the offline channel justifies the reluctance of many established firms to compete aggressively in the online channel upon the risk of eroding profits as markets come closer to perfect information. One possible strategic implication is for firms in commoditized markets to retrench and avoid penetrating the online channel aggressively. Alternatively, they will continue to adopt the well-accepted multichannel strategy to integrate the IT infrastructures across channels and create a seamless experience for the consumer. This approach of a seamless experience for the customer commonly includes setting homogeneous fares across online and offline channels.

5.2.1. Pricing and Multichannel Strategy. There is an opportunity to develop multichannel strategies that capitalize on the heterogeneity of demand across channels. However, firms may be reluctant to deviate from a strategy that is focused on seamless experience for the customer. So despite the rational inclination to price discriminate in online and offline channels given the higher price elasticity online, firms may be constrained by competitive inertia (Miller and Chen 1994) and the fear of innovation in pricing because of the risk of reciprocal threats from competitors (Gimeno 1999). In the air travel industry, for example, given the established homogenous prices in the online and offline channels, it will take perhaps a growing conviction of the profit-enhancing benefits of cross-channel price discrimination to fundamentally challenge the industry’s status quo. Airlines are constrained by decades of pricing practices structured around distribution via reservation systems. In addition, they may be reluctant to implement reasonable yet transformational pricing practices that reflect the heterogeneity of consumers across channels, lest competitors may retaliate with severe punishment in their home market.

A major challenge will be to strike a balance between the benefits of a homogeneous pricing structure and a seamless experience, and the benefits of price discrimination to take advantage of the heterogeneous cross-channel demand sets. One complication is that price discrimination across channels can backfire because of discontent by offline customers who pay higher prices, once they become aware that others are paying lower prices online. Fortunately, the higher cost of offline operations has allowed some firms to effectively justify and perform this price discrimination. For example, U.S. airlines typically charge a fee if bookings are made by phone through their reservations offices, and the fee is waived if the booking is made online. This is effectively a fixed price premium that is charged for offline bookings because of the incremental costs of face-to-face and phone interactions, and it is conveniently in line with the lower price elasticity that is observed offline. But there are probably many other unexplored opportunities. For example, airlines can innovate with inventory management techniques and systems to price discriminate across channels.

5.2.2. IT-Enabled Competitive Strategy. There are other possible strategies that can be adopted in addition to pricing strategies. Firms can also develop transparency strategies online given the numerous options they have to display or conceal information. These strategies involve the coordination between pricing, the transparency-based design of selling mechanisms, and the consequent IT infrastructure requirements. Based on an analytical model of the impact of transparency on demand, Granados et al. (2008) suggest that it is revenue maximizing to align prices with the transparency level of each online selling mechanism. Alternatively, transparency levels can be adjusted if the firm lacks the market power to set prices; such is the case of OTAs, which are subject to the market power that airlines have to set prices.

In addition, technology-enabled strategies can be adopted to confront the potential negative effects of higher price transparency. Suppliers and intermediaries can make IT investments to develop online selling mechanisms that increase product transparency and mitigate product uncertainty (Pavlou and Dimoka 2010). For example, Orbitz, an OTA launched by major airlines in 2001, used state-of-the-art technology to develop a transparent selling mechanism based on a matrix display that highlights product characteristics in addition to simple sorting of travel options based on price. Since then, most online travel intermediaries have entered into heavy competition in the transparency space (Granados et al. 2010), and even the opaque OTAs have implemented transparent selling mechanisms to compete in this dimension.

Similarly, Air Canada has developed a transparent pricing structure based on a customer-centric strategy, and it is investing in new and advanced Internet-based distribution platforms to implement an online à la carte interface that highlights the value of upgraded services. This is a bold move that is likely to offset the adverse effect of price transparency on price elasticity with the positive effect of a customer centric, product transparent pricing model. Air Canada so far implemented this strategy mostly in its portal, where it has the market power to do so. But it has been less successful in other channels like the OTAs and the offline channel, where there is more risk of retaliation and defection by competitors.

## 5.3. Limitations and Future Research

We offer three limitations to this present study that also represent opportunities for future research. First, because we have not explicitly measured and tested the product and price information in the online and offline channels, we can only claim consistency of our findings with the tenets of frictionless markets hypothesis and information integration theory. Nevertheless, we have controlled for other major factors that may account for this price elasticity differential across channels, including differences in the mix of customers segments. Further research is necessary to explicitly measure transparency levels across channels and online sites, and the corresponding impact on demand. Indeed, there is growing evidence that online markets are not completely frictionless, so there is a necessity beyond what we have done in this study to examine instances where market information will lead to different outcomes. It will be interesting to revisit the issues that we have studied at a much more detailed level of granularity to understand the impacts of different kinds of information on consumers. For example, along the lines of Lynch and Ariely (2000), who studied the different effects of product and price transparency in an experimental setting, more experimental studies of the impacts of changes to the information provided on individual online sites or across sites can provide valuable insights. Also, price elasticity comparisons between OTAs that have different user interfaces and transparency levels can bring new knowledge on this front.

Second, although we contend that the higher price elasticity online for air travel is likely to occur in other markets, more empirical studies in other contexts are necessary to verify this claim. We encourage others to verify our finding that the transparent online channel is more price elastic in both commodity and differentiated markets, and to reconcile the conflicting results across studies for differentiated markets. Moreover, new studies in other industries that examine the demand-side and supply-side effects of the Internet should lead to a more comprehensive view of market prices and price dispersion in the online channel.

Third, although we went beyond what most air travel demand studies have done to control for the airline inventory management policies that lead to dynamic pricing, there is another inventory management policy that we could not explicitly control for. Inventory managers close lower fare classes for sale when seat capacity cannot satisfy demand, which leads to what industry professionals refer to as passenger spill in the leisure segment. We partially controlled for such capacity constraints by performing our analysis with offpeak season data at the industry level. In the offpeak season, there is a lower probability of passenger spill. However, even in the offpeak season, it is still likely that seats were not available for sale by an airline in lower fare classes during some days in the booking period. Yet, even if an airline spilled a passenger, it is likely that the passenger would have been captured by another airline that had seats available during the same timeframe. As a result, the offpeak and industry-level features of our analysis mitigate the fact that we were not able to explicitly account for seat capacity constraints.

Nevertheless, there is still a chance of an industrylevel capacity constraint in the offpeak season for a given market, and in these cases, the number of bookings is a downward-biased measure of the real demand, which, in turn, will lead to an underestimation of the price elasticity of the leisure segment. However, industry-level seat constraints are the same across channels, so it is likely that the leisure price elasticity differentials are not going to be highly biased even in this scenario and the tests of our hypotheses on elasticity differentials should hold. Because the online channel has a higher share of leisure travelers, both the informational and channel selection impacts on price elasticity may be biased downward. The risk is that our price elasticity differentials are conservative, so our finding that the online channel is more price elastic is likely to hold.

## Acknowledgments

The authors thank V. Sambamurthy, Sanjeev Dewan, Ram Chellappa, Paul Gift, Rajiv Sabherwal, and T. S. Raghu. The authors also benefited from input by reviewers and participants at the 2009 Rensselaer Polytechnic Institute

Symposium on Digital Systems and Competition, the 2005 Workshop on IS and Economics, the 2007 INFORMS Annual Meeting, the University of Hawaii, the University of Alberta, and staff members from an anonymous sponsor, which provided the data for this research. Nelson Granados thanks Pepperdine University for sponsorship of this research through the Julian Virtue Professorship. Alok Gupta’s research is supported by the National Science Foundation (NSF) Grant IIS-0301239 but does not necessarily reflect the views of the NSF. Rob Kauffman thanks the Center for Advancing Business through Information Technology and the W. P. Carey Chair at Arizona State University. All errors of fact, opinion, and findings are the sole responsibility of the authors.

## References

Alba, J. W., J. Lynch, B. Weitz, C. Janiszewski, R. Lutz, A. Sawyer, S. Wood. 1997. Interactive home shopping: Consumer, retailer, and manufacturer incentives to participate in electronic marketplaces. J. Marketing 61(3) 38–53.

Akerlof, G. A. 1970. The market for lemons: Quality uncertainty and the market mechanism. Quart. J. Econom. 84(3) 488–500.

Anderson, N. H. 1968. A simple model for information integration. R. P. Abelson, E. Aronson, W. J. McGuire, T. M. Newcomb, M. J. Rosenberg, P. H. Tannenbaum, eds. Theories of Cognitive Consistency: A Sourcebook. Rand McNally, Chicago, 731–758.

Anderson, N. H. 1971. Integration theory and attitude change. Psych. Rev. 78 171–206.

Bailey, J. P. 1998. Intermediation and electronic markets: Aggregation and pricing in Internet commerce. Unpublished doctral dissertation, Technology, Management, and Policy, MIT, Cambridge, MA.

Bakos, J. Y. 1997. Reducing buyer search costs: Implications for electronic marketplaces. Management Sci. 43(12) 1676–1692.

Berry, S., J. Levinsohn, A. Pakes. 1995. Automobile prices in equilibrium. Econometrica 63(4) 841–890.

Bhadra, D. 2003. Demand for travel in the United States: Bottom-up econometric estimation and implications for forecasts by origin and destination city pairs. J. Air Transportation 8(2) 19–55.

Bijmolt, T. H. A., H. J. van Heerde, R. G. M. Pieters. 2005. New empirical generalizations on the determinants of price elasticity. J. Marketing Res. 42(2) 141–156.

Borenstein, S. 1992. The evolution of U.S. airline competition. J. Econom. Perspect. 6(2) 45–73.

Breusch, T., A. Pagan. 1979. A simple test for heteroskedasticity and random coefficient variation. Econometrica 47(5) 1287–1294.

Brons, M., E. Pels, P. Nijkamp, P. Rietveld. 2002. Price elasticities of demand for passenger air travel: A meta-analysis. J. Air Transport Management 8(1) 165–175.

Brown, J. R., A. Goolsbee. 2002. Does the Internet make markets more competitive? Evidence from the insurance industry. J. Political Econom. 110(4) 481–507.

Brynjolfsson, E., M. D. Smith. 2000. Frictionless commerce? A comparison of Internet and conventional retailers. Management Sci. 46(4) 563–585.

Brynjolfsson, E., Y. Hu, M. D. Smith. 2003. Consumer surplus in the digital economy: Estimating the value of increased customer variety at online booksellers. Management Sci. 49(11) 1580–1596.

Chellappa, R. K., R. Kumar. 2005. Examining the role of “free” product-augmenting online services in pricing and customer retention strategies. J. Management Inform. Systems 22(1) 355–377.

Chellappa, R. K., R. G. Sin, S. Siddarth. 2010. Price-formats as a source of price dispersion: A study of online and offline prices in the domestic U.S. airline markets. Inform. Systems Res. ePub ahead of print March 1, http://isr.journal.informs.org/ cgi/content/abstract/isre.1090.0264v1.

Chevalier, J., A. Goolsbee. 2003. Measuring prices and price competition online: Amazon.com and BarnesandNoble.com. Quant. Marketing Econom. 1(2) 203–222.

Chircu, A. M., R. J. Kauffman. 2000. Reintermediation strategies in business-to-business electronic commerce. Internat. J. Electronic Commerce 4(4) 7–42.

Clemons, E. K., I. Hann, L. M. Hitt. 2002. Price dispersion and differentiation in online travel: An empirical investigation. Management Sci. 48(4) 534–549.

comScore, Inc. 2010. Understanding consumers’ shopping and buying behavior at supplier and agency travel sites. Industry Report, Reston, VA, June 2006. Accessed April 18, 2010, www.comscorea.com.

Degeratu, A., A. Rangaswamy, J. Wu. 2000. Consumer choice behavior in online and traditional supermarkets: The effects of brand name, price, and other search attributes. Internat. J. Res. Marketing 17(1) 55–78.

Dimoka, A., P. Pavlou. 2010. Product uncertainty in online markets: Conceptualization, antecedents, and consequences. Working paper, SSRN. ssrn.com/abstract=1557862.

Duliba, K. A., R. J. Kauffman, H. C. Lucas. 2001. Appropriating value from computerized reservation systems ownership in the airline industry. Organ. Sci. 12(6) 702–728.

Ellison, G. D., S. F. Ellison. 2009. Search, obfuscation, and price elasticities on the Internet. Econometrica 77(2) 427–452.

eMarketer. 2005. High flying online travel segment gets down to business. (March 9). Newsletter, New York.

Ghose, A., Y. Yao. 2010. Using transaction prices to re-examine price dispersion in electronic markets. Inform. System Res. ePub ahead of print February 1, http://isr.journal.informs.org/ cgi/content/abstract/isre.1090.0252v1.

Ghose, A., M. D. Smith, R. Telang. 2006. Internet exchanges for used books: An empirical analysis of product cannibalization and welfare impact. Inform. Systems Res. 17(1) 3–19.

Gimeno, J. 1999. Reciprocal threats in multimarket rivalry: Staking out “spheres of influence” in the U.S. airline industry. Strategic Management J. 20(2) 101–128.

Goldfeld, S., R. Quandt. 1965. Some tests for homoscedasticity. J. Amer. Statist. Association 60(310) 539–547.

Granados, N. F., A. Gupta, R. J. Kauffman. 2006. The impact of IT on market information and transparency: A unified theoretical framework. J. Association Inform. Systems 7(3) 148–178.

Granados, N. F., A. Gupta, R. J. Kauffman. 2008. Designing online selling mechanisms: Online transparency and prices. Decision Support Systems 45(4) 729–745.

Granados, N. F., A. Gupta, R. J. Kauffman. 2010. Information transparency in business-to-consumer markets: Concepts, framework, and research agenda. Inform. Systems Res. 21(2) 207–226.

Gupta, A., B. Su, Z. Walter. 2004a. Risk profile and consumer shopping behavior in electronic and traditional channels. Decision Support Systems 38(3) 347–367.

Gupta, A., B. Su, Z. Walter. 2004b. An empirical study of consumer switching from traditional to electronic channel: A purchase decision process perspective. Internat. J. Electronic Commerce 8(3) 131–161.

Johnson, R. D., I. P. Levin. 1985. More than meets the eye: The effect of missing information on purchase evaluations. J. Consumer Res. 12(3) 169–177.

Johnson, E. J., W. W. Moe, P. S. Fader, S. Bellman, G. L. Lohse. 2004. On the depth and dynamics of online search behavior. Management Sci. 50(3) 299–308.

Kennedy, P. 1998. A Guide to Econometrics, 4th ed. MIT Press, Cambridge, MA, 205–217.

Lal, R., M. Sarvary. 1999. When and how is the Internet likely to decrease price competition? Marketing Sci. 18(4) 485–503.

Lee, H. G. 1998. Do electronic marketplaces lower the price of goods? Comm. ACM 41(12) 73–80.

Lynch, A., D. Ariely. 2000. Wine online: Search costs affect competition on price, quality, and distribution. Marketing Sci. 19(1) 83–103.

Miller, D., M. J. Chen. 1994. Sources and consequences of competitive inertia: A study of the U.S. airline industry. Admin. Sci. Quart. 39(1) 1–23.

Oh, W., H. C. Lucas, Jr. 2006. Information technology and pricing decisions: Price adjustments in online computer markets. MIS Quart. 30(3) 755–775.

Oum, T. H., A. Zhang, Y. Zhang. 1993. Inter-firm rivalry and firmspecific price elasticities in deregulated airline markets. Internat. J. Transport Econom. Policy 27(2) 171–192.

PhoCusWright. 2004. Number of U.S. online travel buyers up 17% in 2003. Press release, Sherman, CT (March 2). Accessed April 18, 2010, www.phocuswright.com.

Regan, K. 2001. Study: Economic slowdown aids online travel. E-Commerce Times (April 23). Accessed April 18, 2010, www .ecommercetimes.com/perl/story/9156.html.

Smith, M. D. 2002. The impact of shopbots on electronic markets. Marketing Sci. 30(4) 446–454.

Smith, M. D., J. Bailey, E. Brynjolfsson. 2001. Understanding digital markets: Review and assessment. Working Paper 4211-01, Sloan School of Management, MIT, Cambridge, MA.

Stigler, G. 1961. The economics of information. J. Political Econom. 69(3) 213–225.

Stigler, G. 1964. A theory of oligopoly. J. Political Econom. 72(1) 213–225.

Talluri, K. T., G. J. van Ryzin. 2004. The Theory and Practice of Revenue Management. Springer Science and Business Media, New York.

Villas-Boas, J. M., R. S. Winer. 1999. Endogeneity in brand choice models. Management Sci. 45(10) 1324–1338.

Walter, Z., A. Gupta, B. Su. 2006. The sources of on-line price dispersion across product types: An integrative view of on-line search costs and price premiums. Internat. J. Electronic Commerce 11(1) 37–62.

Zettelmeyer, F. 2000. Expanding to the Internet: Pricing and communications strategies when firms compete on multiple channels. J. Marketing Res. 37(3) 292–308.

Zettelmeyer, F., F. Scott Morton, J. Silva-Risso. 2006. How the Internet lowers prices: Evidence from matched survey and automobile transaction data. J. Marketing Res. 43(2) 168–181.
