---
otero_id: 8314
otero_key: "8A33EM35"
title: "How e-WOM and local competition drive local retailers' decisions about daily deal offerings"
authors: "Xue Bai; James R. Marsden; William T. Ross; Gang Wang"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.06.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# How e-WOM and local competition drive local retailers' decisions about daily deal offerings

Xue Bai <sup>a</sup>, James R. Marsden <sup>a</sup>, William T. Ross Jr <sup>b</sup>, Gang Wang <sup>c,</sup>⁎

<sup>a</sup> Operations and Information Management, School of Business, University of Connecticut. 2100 Hillside Road Unit 1041, Storrs, CT. 06269, United States

<sup>b</sup> Marketing, School of Business, University of Connecticut. 2100 Hillside Road Unit 1041, Storrs, CT. 06269, United States

Accounting and Management Information Systems Alfred Lerner College of Business and Economics University of Delaware, 42 Amstel Ave, Newark DE 19716 United States

## a r t i c l e i n f o

Article history: Received 29 May 2017 Accepted 20 June 2017 Available online xxxx

Keywords: Daily deals E-WOM Local competition Groupon Propensity score analysis

## a b s t r a c t

Local retailers considering offering daily deals must take into account possible impacts of both electronic-wordof-mouth (e-WOM) and local competition. However, how e-WOM, local competition, and their interactions affect local retailers' decisions to offer daily deals remains unclear. Here we examine these effects utilizing a data set that contains details of daily deals, online reviews, and local competition measures for restaurants in the Chicago area. With a propensity score matching (PSA) method, we show: 1) local retailers with high ratings and high number of reviews were more likely to initiate daily deals: 2) local retailers in an area with a low level of local competition were more likely to initiate daily deals; and 3) the strength and direction of the impact of e-WOM depend on the level of local competition. Our results enhance understanding of local retailers' decisions to offer daily deals and yield important implications related to daily deal sites.

© 2017 Elsevier B.V. All rights reserved.

## 1. Introduction

Daily deals integrate various elements including price promotion and e-couponing, and have become a popular marketing tool for local retailers including restaurants [44]. These vouchers for discounted products or services provided by local retailers, are listed and sold to consumers in the form of e-coupons on sites, such as Groupon, and LivingSocial [2,50]. Consumers who buy daily deals can consume the products or services within the specified duration of the coupon. These daily deal sites attract consumers by deep discounts and inform consumer purchasing decisions by providing additional information about local retailers, such as online reputation and locations. Compared with traditional marketing channels, such as a newspaper, local retailers pay no upfront costs or fees to offer a daily deal. Instead, the retailers share portions of the deal sales revenue with the sites [7]. Thus, the daily deal environment shifts the paradigm from a fee-for-promotion service to a revenue-sharing arrangement. Pioneered and led by Groupon, daily deals quickly became a multi-billion industry [33].

Despite the popularity of daily deals, prior studies on deal profitability are not in agreement on the value of such arrangements to retailers. Daily deals can benefit local retailers in several ways: short-term sales increases, the acquisition of new customers, and increased awareness among consumers in general [18,33]. However, the other side of the coin is that daily deals may also hurt local retailers' profits from intrafirm cannibalization and “deal-hunters” who never return [23,28]. The decision on whether to offer a daily deal remains a dilemma for many local retailers.

This study investigates local retailers' decisions to initiate daily deals. Daily deal sites explicitly integrate e-WOM (such as Yelp reviews) to influence consumers' decisions. Previous literature has shown the impact of e-WOM on consumer purchases and sales [10,14]. Local retailers also operate in a competitive landscape where a retailer's decision is very likely to be affected by other retailers' decisions and actions [9,11]. Daily deals represent an environment in which both e-WOM and local competition and their interactions may affect local retailers' decisions [32]. Prior studies have focused on either e-WOM or local competition, but not both individually or together with possible interaction effects. Thus, we address the following questions: 1) what impact do e-WOM and local competition, independently, have on local retailers' decisions whether to initiate a daily deal? and, 2) how does the interaction between e-WOM and local competition affect local retailers' decisions whether to initiate a daily deal?

To answer these questions, we collected a detailed data set of daily deals for restaurants in the Chicago area from Groupon, which includes data on 7008 restaurants over a three-year period. We developed two variables for e-WOM: Online Review Rating and Number of Online Reviews from Yelp, and two variables for local competition: Number of Restaurants Nearby from Yelp and Proportion of Restaurants Nearby that Have Used Groupon calculated from Yelp and Groupon data. We employed and extended propensity score analysis (PSA) to determine the causal relationships.

Our analysis yielded several interesting findings. Considering the effects of e-WOM and local competition independently, we found that restaurants with high online ratings were more likely to engage in initial daily deals. Similarly, restaurants with a high number of reviews, were more likely to run initial daily deals. In terms of local competition, restaurants in an area with a low level of nearby restaurants were more likely to initiate daily deals. Contrary to the local competition literature [11,16,40], restaurants were more likely to initiate daily deals if nearby competitors had not run one, suggesting that daily deals are viewed more as a means to create a competitive advantage than as competitive responses to the actions of other restaurants. When we considered local competition as a moderator, we found its significant impacts on the relationship between e-WOM and restaurants' decisions to initiate daily deals. Specifically, high online ratings had a positive impact on a restaurant's decision to offer an initial daily deal only when the restaurant is located in an area with a small number of nearby restaurants. A large set of online reviews for a restaurant yielded positive impact in an area with a small number of restaurants nearby but a negative impact in an area with a large number of restaurants nearby. High online ratings also had a positive impact on a restaurant's initial daily deal offering decision only if few nearby restaurants had offered daily deals.

To the best of our knowledge, this study is the first to examine local retailers' daily deal offering decisions affected by both e-WOM and local competition, and their interactions. The study complements previous literature by investigating the two types of factors together and uncovering significant and distinct impacts on daily deal decisions. Practically, our results shed light on the types of local retailers that are more likely to offer daily deals. The findings have important implications for daily deal sites to better allocate resources to target potential business customers.

## 2. Literature review and research gap

Three main fields of research relate to our study's focus: daily deals versus traditional coupons, e-WOM and firm promotion strategies, and local competition and firm promotion strategies. Our work is directed at filling the research gap since prior work does not consider both e-WOM and local competition impacts together let alone the interaction effects of the two.

## 2.1. Daily deals versus traditional coupons

As noted earlier, daily deals differ from traditional coupons because consumers must “pay to play” while local retailers pay no upfront costs but engage in a revenue sharing arrangement with a daily deal site [2,7]. Research into traditional coupons considers a very different market setting.

## 2.2. e-WOM and firm promotion strategies

Research of the impact of e-WOM on firm decisions includes Dellarocas's [12] and Gu and Ye's [21] assertions that retailers respond to consumers' e-WOM comments directly. Of particular relevance to our work, past authors have argued that e-WOM also affects firms' strategies related to price and coupon promotions. Kuksov and Xie [27] posited that retailers respond to e-WOM by offering discounts to early customers, whose reviews may influence subsequent potential customers. Feng et al. [19] argued that when consumers' expectations exceed reality, those consumers likely assigned harsh ratings, so retailers cut the prices to generate good online reviews initially, then subsequently increase the price. Using an analytical model, Kwark et al. [29] investigated the impact of e-WOM on the pricing decisions of different players (one retailer, two manufacturers) in a supply chain context. They argued that quality information from online reviews benefits manufacturers by mitigating pricing competition. Finally, Chen and Xie [8] offered a perspective that ties directly to our work. In their analytical analysis, it is more profitable for retailers to respond to thirdparty online reviews using promotions rather than pricing. However, both Kwark et al. and Chen and Xie's outcomes are theoretical conjecture since neither was empirically tested.

## 2.3. Local competition and firm promotion strategies

Local competition can influence the decisions retailers make. Also called spatial competition, the influence was formally modeled earlyon by Hotelling [25]. Through a highly simplified format, the Hotelling model theorized that if the transportation cost is small, the two firms engage in price competition. In another theoretical argument, Shaffer and Zhang [40] predicted that firms can poach consumers by offering coupon promotions, such that competing firms eroded their profits in a prisoner's dilemma scenario. Related empirical studies provided actual evidence of a negative impact of local competition on retailers' prices [11,45].

With a game-theoretic model, Shin and Sudhir [43] predicted that consumers' location information affects whether retailers should offer discounts to their own consumers or to competitors' consumers. Using a field experiment, Fong et al. [20] found that providing coupons to consumers near a competitor's location was effective in attracting more consumers and lessening profit cannibalization from existing consumers.

## 2.4. 2.4 summary of the research gap

Research on e-WOM and firm decisions has focused mainly on consumer purchase behavior and firm strategies in a monopoly market. A few studies [29,30] considered a competitive market using a theoretical model. However, competition in these theoretical frameworks was focused on price and did not include physical location as the current study does. In local competition literature, very few studies even mentioned e-WOM. Davis [11] explicitly omitted e-WOM to simplify the consumer choice process modeled. Moreover, instead of small, local, or weakly branded retailers, previous empirical studies of local competition tended to use data from national brands, such as Burger King and McDonald's [45].

Online services, including daily deals, enable local retailers to connect with online and networked consumers [48]. Local retailers must face both e-WOM and local competition - factors that might have both direct and interactive effects on retailers. We use the daily deal context to study these relationships to fill an existing research gap. We examine how local competition moderates the impact of e-WOM on local retailers' decisions whether to offer daily deals. However, because the location of a local retailer is a relatively fixed factor [15] and not easily affected by volatile factors such as e-WOM, we do not consider the moderating effect of e-WOM on local competition.

## 3. Hypotheses development

The conceptual model in Fig. 1 presents the direct impacts of e-WOM and local competition on local retailers' decisions about whether to initiate a daily deal $\mathrm { ( H } _ { 1 } \mathrm { - H } _ { 4 } )$ and the moderating roles of local competition factors $\left( \mathrm { H } _ { 5 \mathrm { a } } \mathrm { - H } _ { 6 \mathrm { b } } \right)$ . Because we test our hypotheses with restaurants daily deal offering data collected from Groupon, we use “restaurants” and “Groupon deals” in place of the terms “local retailers” and “daily deals” hereafter.

As shown in Fig. 1, we analyzed four factors (two elements of e-WOM and two elements of local competition). For each factor, we divided restaurants into three levels: top third, middle third, and bottom third. For example, for the “number of reviews” factor, we ordered the restaurants by the number of reviews they received, then sorted them into thirds. In all of our comparative analyses, we focus on comparing

X. Bai et al. / Decision Support Systems xxx (2017) xxx–xxx

![](/api/attachments/8A33EM35/fulltext/images/c37fbd01a32d45026ad05bc9125c23a9820b07c2fbe0dd3c00bb7326c930f7ba.jpg)  
Fig. 1. Conceptual model of restaurants' initial Groupon deal decision analysis.

the top third against the bottom third, ignoring the middle third,<sup>1</sup> in an effort to provide clear separation in the factors analyzed.

## 3.1. e-WOM Factors

We take online review ratings as representing the valence of e-WOM and the number of online reviews the volume of e-WOM [31]. As detailed in the following two sections, we studied both factors and their impact on restaurants' decisions to initiate Groupon deals.

## 3.1.1. Online review rating

Anderson and Magruder [1] argued that an online review rating indicates the retailer's online reputation with a high rating having a positive influence on consumer demand. In the context of Groupon deals, consumers pay for and buy the coupons, providing revenue for restaurants. Because consumers perceive highly rated restaurants as better, such restaurants can expect to sell more coupons and earn more revenue from a Groupon deal than do low rated restaurants [7].

Similar to traditional couponing, Groupon deals can help retailers attract new consumers and serve as promotion tools [18,47]. High ratings provide positive information about the quality of services and products being provided, so they should help restaurants attract more new consumers than low ratings do. In addition, some consumers do not just use the coupons but also write reviews and spread the retailer's reputation online [13,35]. Thus, highly rated restaurants can expect that, by using Groupon deals, their online reputation will be further enhanced and continue to help increase consumer demand in the future.

Although some might argue that highly rated restaurants do not need to engage in as much marketing as low rated restaurants, we follow most prior literature and conjecture that highly rated restaurants are more likely to initiate a Groupon deal than low rated restaurants because of the benefits they expect in the form of increased revenue, advertising, and online reputation. These arguments lead to the following hypothesis:

H . With other factors matched, restaurants with high online review ratings are more likely to initiate a Groupon deal than restaurants with low online review ratings.

## 3.1.2. Number of online reviews

As an indicator of popularity, a large number of online reviews may be a factor that increases consumer demand and sales [31]. Duan et al. [17] argued that restaurants with many online reviews appear more popular to consumers than those with few online reviews, so they should attract more consumers. Following this logic, restaurants with a large number of online reviews may be more likely to initiate a Groupon deal than those with a small number of online reviews. First, restaurants with more online reviews may expect to sell more coupons and earn more revenue, because the large number of reviews should have a positive impact on their sales [31,39]. Second, if more Groupon coupons are sold, a greater number of coupon users are available to write online reviews [35] which should increase the number of reviews (popularity) even further. This enhanced online popularity in turn should attract more future consumers. This leads to the following hypothesis:

H . With other factors matched, restaurants that have a high number of online reviews are more likely to initiate a Groupon deal than restaurants with a low number of online reviews.

## 3.2. Local competition factors

Competition in restaurant markets is highly localized [37] with restaurants competing heavily with other restaurants located in their local geographic area. We investigate two local competition factors: number of restaurants nearby and proportion of restaurants nearby that have used Groupon. The former factor reflects how many other restaurants are within a certain distance (e.g., half mile) from the focal restaurant. It indicates the overall competitive landscape of the local area. The latter factor is a measure of how many other restaurants nearby have run Groupon deals divided by the total number of nearby restaurants.

## 3.2.1. Number of restaurants nearby

Research in industrial organization topics demonstrated that market concentration, or the number of firms in a market, affects the degree of competition in that market [46]. Hannan [24] argued that a greater number of competitive firms results in a low level of market concentration, which invokes more intense competition than would occur in a market with just a few competing firms. Therefore, a restaurant in an area with a large number of restaurants nearby may be more likely to run Groupon deals to compete for consumers.

However, another stream of studies on spatial concentration suggested that in a local area geographic proximity increases overall demand [26]. Shen [41] argued that demand expands as the number of firms in a market grows. In our market, the presence of a group of restaurants in a more competitive area (e.g., the downtown area) may act as a popular consumer “destination”, because they provide more options from which consumers may choose. Wang et al. [49] investigated which factors influence the number of consumer visits, using restaurant data, and found that restaurants in close proximity to many other restaurants attracted more consumer visits than restaurants with fewer other restaurants nearby. We predict that restaurants with many restaurants nearby have a larger consumer base and more demand; therefore, they are less likely to need to initiate a Groupon deal to increase demand than are restaurants with just a few restaurants nearby. In summary,

$\mathbf { H } _ { 3 } .$ With other factors matched, restaurants that have many other restaurants nearby are less likely to initiate a Groupon deal than restaurants with few other restaurants nearby.

X. Bai et al. / Decision Support Systems xxx (2017) xxx–xxx

## 3.2.2. Proportion of restaurants nearby that have used Groupon

Previous theoretical work, such as that by Hotelling [25] and Shaffer and Zhang [40], indicated that firms engage in price competition that ultimately erodes profits. In an empirical study, Davis [11] demonstrated that price competition affects nearby, rather than distant, retailers. Duan and Mela [16] argued that consumers of retailers that are near each other in a local area are similar and drawn to similar offerings. Accordingly, we suggest that a restaurant is more likely to run a competing promotion for similar potential consumers if a high proportion of restaurants nearby have already run Groupon deals. As Gupta [22] found, short-term sales to new consumers brought in by coupon promotions mostly involve brand switchers, who by definition are prone to switch again. To reacquire brand switchers, a restaurant may feel compelled to run a defensive coupon promotion in response [40], especially if a high versus low proportion of restaurants nearby have run it.

$\mathbf { H } _ { 4 } .$ With other factors matched, restaurants that have a high proportion of restaurants nearby that have used Groupon are more likely to initiate a Groupon deal than restaurants with a low proportion of restaurants nearby that have used Groupon.

## 3.3. Moderating role of local competition factors

In addition to the direct impacts of e-WOM and local competition, we examine whether and how local competition might moderate the relationship between e-WOM and restaurants' decisions to initiate Groupon deals. Despite the lack of research into the interactions between e-WOM and local competition, we argue, in making deal decisions, local retailers take into account e-WOM, local competition, and these two factors in combination. Thus we develop hypotheses on the moderating effects of local competition on how e-WOM affects restaurants' initial Groupon deal decisions.

## 3.3.1. Moderating role of number of restaurants nearby

In addition to predicting that highly rated restaurants are more likely to initiate a Groupon deal because they expect both good revenues from the promotion and an advertising effect on customer patronage, we hypothesize that the number of restaurants nearby moderates this relationship. Spatial concentration theory [26,42] predicts that, for a given area, the number of restaurants correlates positively with the number of consumers frequenting the area. Restaurants with few restaurants nearby are likely to be more motivated to attract consumers who do not patronize the local area but would be willing to do so if given an incentive. Therefore, highly rated restaurants in an area with few restaurants nearby may have a greater incentive to initiate a Groupon deal than do restaurants in an area with a large number of restaurants nearby. We argue that with less consumers patronizing the area, a restaurant is more motivated to reach out to the new consumers.

We also have argued that the number of reviews is a measure of how popular a restaurant is. The number of restaurants nearby may moderate the relationship between the number of online reviews and the restaurant's decision to initiate a Groupon deal. Our argument is that restaurants with a high number of reviews and located in an area with few restaurants nearby, are more likely to attempt to reach new consumers and thus more likely to initiate a Groupon deal than restaurants with high number of reviews but located in an area with more restaurants nearby. Hence, we hypothesize:

$\mathbf { H } _ { 5 \mathbf { a } } .$ The number of restaurants nearby has a significant moderating effect on the relationship of a restaurant's online review ratings with that restaurant's decision to initiate a Groupon deal.

$\mathbf { H } _ { 5 \mathbf { b } } .$ The number of restaurants nearby has a significant moderating effect on the relationship of a restaurant's number of online reviews with that restaurant's decision to initiate a Groupon deal.

3.3.2. Moderating role of proportion of restaurants nearby that have used Groupon

The proportion of restaurants nearby that have run a recent Groupon deal provides a measure of direct deal competition.<sup>2</sup> It also offers another potential moderating factor of the relationship between the e-WOM factors and restaurants' initial Groupon deal decisions. For example, when a higher proportion of restaurants nearby have already run Groupon deals, a restaurant may perceive that it faces a greater threat of the loss of consumers, because consumers are likely to respond to those promotions offered by competitors. Therefore, when a larger proportion of nearby restaurants have used Groupon, highly rated restaurants may have even an enhanced incentive to run a defensive promotion to maintain their existing consumers and entice new ones. They also may have less reason to fear negative promotion outcomes, because their high ratings protect them against the potential for poor results. Similarly, we argue that restaurants with more online reviews are more likely to initiate a Groupon deal to compete when their competitors already have initiated their own Groupon deals. We expect restaurants to do so in order to maintain their popularity, compared with their counterparts with a lower proportion of Groupon deal–using competitive restaurants nearby. We hypothesize:

$\mathbf { H } _ { 6 a ^ { * } }$ The proportion of restaurants nearby that have used Groupon has a significant moderating effect on the relationship of a restaurant's online review rating with that restaurant's decision to initiate a Groupon deal.

$\mathbf { H _ { 6 b } } .$ The proportion of restaurants nearby that have used Groupon has a significant moderating effect on the relationship of a restaurant's number of online reviews with that restaurant's decision to initiate a Groupon deal.

## 4. Variable descriptions and data collection processes

The following variables, with their formal names in italics, appear in our hypotheses and must be operationally defined: 1) online review ratings: Average Yelp Rating, 2) number of online reviews: Number of Yelp Reviews, 3) number of restaurants nearby: Number of Restaurants Nearby, and, 4) proportion of restaurants nearby that have used Groupon: Proportion of Restaurants Nearby that Have Used Groupon. Table 1 below provides a brief operational definition of each variable along with the relevant data source. The main sources for the data collection/construction for each variable were Groupon and Yelp.

## 4.1. Details of Groupon data collected

We collected data from Groupon's website on restaurant deals in the Chicago area from September 1, 2011, through March 31, 2013, though, as explained below, the completed data collection actually yielded information that spanned the period from December 7, 2008, to March 31, 2013. Each Groupon deal has a unique identifier that differentiates it from other deals. Even deals from the same restaurant use different deal identifiers. However, the unique identifiers did, in fact, follow patterns. For example, if “delux-grill” was the identifier for a restaurant's first promotion, “delux-grill-1” would be the identifier for the restaurant's second deal, and “delux-grill-2” would signal its third deal. Based on such patterns, we were able to identify restaurants that were returning and could locate their initial Groupon deal, many of which occurred well before September 1, 2011. To capture information on initial deals that occurred before September 1, 2011, we used three other sources detailed in Fig. 2.

Table 1  
Variable Descriptions/Definitions and Data Sources

<table><tr><td>Variables</td><td>Descriptions/definitions</td><td>Data sources</td></tr><tr><td>Groupon restaurants</td><td>Restaurants that ran an initial Groupon deal prior to the end of data collection, i.e. March 31, 2013.</td><td>Groupon</td></tr><tr><td>Non-Groupon restaurants</td><td>Restaurants that had not run Groupon deals prior to the end of data collection, i.e. March 31, 2013.</td><td>Identified from Groupon and Yelp</td></tr><tr><td>Average Yelp rating</td><td>Average of all Yelp ratings when a restaurant ran an initial Groupon. $^a$  This variable reflects the measure of online review ratings.</td><td>Yelp</td></tr><tr><td>Number of Yelp Reviews</td><td>Number of all Yelp reviews when a restaurant ran an initial Groupon. $^a$  This variable reflects the measure of the number of online reviews.</td><td>Yelp</td></tr><tr><td>Number of Restaurants Nearby</td><td>Number of competitors (other restaurants) within a half-mile of the focal restaurant.</td><td>Yelp</td></tr><tr><td>Proportion of Restaurants Nearby that Have Used Groupon</td><td>Number of a restaurant A&#x27;s competitors within a half-mile that have run a Groupon deal, before A ran an initial Groupon deal, divided by the Number of Restaurants Nearby. $^b$ </td><td>Calculated from Groupon and Yelp</td></tr></table>

<sup>a</sup> For non-Groupon restaurants, for which no date of initial Groupon deal was available, we determined the two e-WOM factors (Average Yelp Rating and Number of Yelp Reviews) on April 20, 2011, which is the median date on which Groupon restaurants ran the initial Groupon deals in our data set.  
<sup>b</sup> Nearby restaurants' promotion behaviors may influence the focal restaurant's promotion decisions mostly within a particular period. We operationalized this period by choosing 180 days before the restaurant ran its initial Groupon deal, because the median coupon duration (i.e., period when a buyer can use the coupon) is 180 days. As we discuss in the Section 5.4, our conclusions are not sensitive to our choice of 180 days.

First, we obtained a data set compiled by Byers et al. $[ 7 ] , ^ { 3 }$ which covered all Groupon deals between January 1 and July 31, 2011. Second, we collected Groupon deal links from Archive.org, which scanned Groupon's webpages and provided free access to the data. However, Archive.org only scanned Groupon data on randomly selected days each month. For restaurants in Chicago, Archive.org collected data for 23 days during 2009 and 118 days during 2010. Third, for the days not covered by Archive.org, we searched Groupon deal links through Google Custom Search. The search terms were the physical addresses or phone numbers of the restaurants in question. Our Archive.org and Google Custom Search together provided 1143 restaurant deals for 2010 or earlier in the Chicago area.

Thus, the overall Groupon restaurant deal data runs from December 7, 2008, to March 31, 2013. While we might have failed to capture some first-time deals before 2010, after that date we obtained every first deal for all later deals through use of the deal identifiers explained earlier.

Through Groupon's public API,<sup>4</sup> we obtained information about each deal, including the date the deal was issued, the discounted coupon price, and the quantity of coupons sold by the end of the promotion. We also obtained each restaurant's longitude, latitude, physical address, and zip code from Groupon's API. The longitude and latitude for each restaurant enabled us to determine Groupon usage by local competitors within a half-mile of its location.<sup>5</sup> For each restaurant at the time t of its initial promotion, we obtained the number of nearby restaurants that had run a Groupon deal within 180 days prior to t.

## 4.2. Yelp data details

Yelp provided the necessary operationalizations for our two e-WOM variables. We collected Yelp information for all restaurants in the Chicago area, then differentiated Groupon restaurants (restaurants having run a Groupon deal) from non-Groupon restaurants. For 58.2% of the Groupon restaurants, Groupon provided Yelp with information directly. For the remaining 41.8% of Groupon restaurants, we searched for the necessary Yelp information using phone numbers, business names, and physical addresses from the Groupon listings. This process yielded the information we needed for another 39.5% of the Groupon restaurants.

Overall, we matched 97.7% of Groupon restaurants with Yelp information specific to those restaurants. For each restaurant, we collected all of its individual reviews, with corresponding numeric ratings (1–5 points) and review dates. We then constructed an average of the individual Yelp ratings, the number of Yelp reviews, and the number of Yelp dollar signs (an indication of price level) for every restaurant on the specific day that it ran its initial Groupon deal.

We used the Yelp the information to identify each restaurant and the total number of restaurants within a certain distance (half-mile) of each restaurant using based on latitude and longitude to determine the Number of Restaurants Nearby values. Using this information and corresponding information from Groupon on which restaurants ran a Groupon deal and when, we constructed the Proportion of Restaurants Nearby that Have Used Groupon.

Finally, we collected demographic information (average household income and average age) from the 2010 U.S. Census by zip code and used these variables as controls.

## 5. Data analysis

## 5.1. Method

Because of our interest in identifying causal relationships among e-WOM, local competition, and restaurants' decisions to initiate a Groupon deal, we considered a variety of possible methods and settled on propensity score analysis (PSA), a quasi-experimental method for performing comparisons across matched pairs of observations, which in this paper are restaurants. To analyze the impact of each factor in turn, we pair the restaurants for similarity on all other e-WOM and local competition factors along with a set of control variables.

We made the final choice of the PSA approach over either laboratory or field experiments for several reasons. First, we were able to collect actual micro-level data for more than 7000 real restaurants engaging in Groupon deals. This use of real data supports comparisons of fairly large sets of matched pairs over long periods of time, in direct contrast with the limited observation sets over limited amounts of time that typically result from controlled laboratory experiments. Second, because we used real restaurants, our data reflect the actual decision making of a large number of real business owners, rather than the actions of participants in a laboratory setting.<sup>6</sup> Third, devising a field experiment generally requires the experimenter to limit the context to one or a few stimuli that may not be representative of the real environment or the factors considered by actual decision makers in that environment. Because we matched pairs of real deal offers from real restaurants purchased by real consumers, none of these limitations apply to our data and analysis. Finally, by matching pairs of restaurants that are equivalent on a number of characteristics but that differ in terms of one treatment, we have a mechanism for testing directly whether or not choosing to engage in daily deals is causally impacted by the factors we study.

![](/api/attachments/8A33EM35/fulltext/images/a89a0eaf50765fd91ee90931e0f50547538b9e6995cd7b55fd91cb94f72be917.jpg)  
Fig. 2. Data collection sources for Groupon restaurant deals.

## 5.2. Extended propensity score method

The PSA method identifies a variable (or combination of variables) for which a two-level separation is possible (e.g., low versus high, zero versus positive value). The set of observations then gets divided into two groups: a treatment group (presence of the treatment) and a control group (absence of the treatment). Using a structured search, corresponding members or matches are identified, one from the control group and one from the treatment group. The matches are such that the likelihood of each paired observations (one treatment, one nontreatment) being a member of the treatment group is “close” (within a specified ε). Given the observed values on all variables except for the variable of interest (treatment variable), the propensity score or likelihood that the paired observation from the control group would appear in the treatment group is very close to the propensity score for the matching observation that actually is in the treatment group (for details, see Mithas and Krishnan [34]). With this set of matched pairs, the analysis continues by examining the difference (or lack thereof) in the outcome variable of interest. The basic idea is to evaluate the differences in outcomes for two sets of observations that are matched on all but the variable being analyzed for a causal effect.

We add a twist and create an extended propensity score analysis (EPSA) method that allows us to perform causal analysis on each of the continuous variables in our hypotheses. That is, prior uses of PSA have used binary treatment variables (e.g., drug treatment versus no drug treatment in medicine, MBA degree versus no MBA degree). The variables we analyze here are continuous or nearly continuous, such as Average Yelp Rating and Number of Yelp Reviews. Thus, we pursue our EPSA approach by dichotomizing the explanatory variables.

Table 2 below contains the range of values that we used to transform the variables of interest into binary variables with separation. We ordered the observations and assigned the bottom third of observed values to the $" 0 "$ or control group; those whose values were in the upper third of observed values entered the $" 1 "$ or treatment group. The middle third were not assigned. Thus, matched pairs involve elements from the lowest third and from the upper third; in treatment terms, the high category of values of a variable are considered as treatments for those variables. This division into treatment and control groups does not involve a direct binary split (e.g., drug versus no drug), but the basic approach is the same. Still, we note that our decision to base divisions on the bottom third (control) versus the upper third (treatment) is subjective in nature. To examine the validity of this decision, we also tested other possible splits, ranging from the bottom 20% versus top 20% to the bottom 40% versus top 40% (see Section 5.4.3). We found no significant changes and thus adopted the bottom third versus upper third splits for our EPSA.

Table 2 also contains variable levels and the number of observations for all of our treatment and control groups. For greater clarity, we use a running example for the variable Number of Yelp Reviews. For the initial decision about a Groupon deal (yes or no), we have 2338 observations in the control group, with a mean value of 2.59 and a standard deviation of 1.38, in contrast to 2335 observations in the treatment group, with a mean value of 102.48 and a standard deviation of 115.47.

## 5.3. Analysis and results

Our presentation of analysis and results follows the ordering of our hypotheses. We start with testing of the hypotheses related to the direct effects of e-WOM and local competition $\mathrm { ( H _ { 1 } \mathrm { - } H _ { 4 } ) }$ and following that by testing of hypotheses related to the moderating effects of local competition factors $\left( \mathrm { H } _ { 5 a } \mathrm { - H } _ { 6 \mathrm { b } } \right)$

## 5.3.1. Direct effects

The EPSA results are in Table 3. Consider the second row which is in bold font in Table 3. The EPSA involves comparison of 1345 matched pairs, each of which contains an observation from the control group (small Number of Yelp Reviews) and the treatment group (large Number of Yelp Reviews). The results reveal that restaurants in the high category of online review ratings are more likely to initiate a Groupon deal than restaurants in the low category of online review ratings, in support of H1. 11.7% of the treatment group restaurants in the matched pairs for the number of reviews decided to initiate a Groupon deal, whereas 7.5% of the control group restaurants did so. The difference is significant (at the 0.01 level using the Wilcoxon signed rank test) and supports $\mathrm { H } _ { 2 } .$ In addition, restaurants in the high category of number of restaurants nearby are less likely to initiate a Groupon deal than restaurants in the low category of number of restaurants nearby. Therefore, $\mathrm { H } _ { 3 }$ is supported.

However, we note that restaurants with a low proportion (actually 0), versus high proportion, of nearby competitors that previously ran Groupon deals are more likely to offer their own initial Groupon deal (13.7% versus 10.8%), in contrast with the prediction of $\mathrm { H } _ { 4 } .$ One explanation might be that if one local restaurant runs a Groupon deal, consumers notice and subsequently try nearby restaurants too, providing a positive spillover effect [42,48]. In contrast, if few or no restaurants nearby are using Groupon deals, the restaurant would not benefit from such a spillover effect and may be more likely to pursue its own Groupon deal.

## 5.3.2. Moderating effects

Next, we present the analysis of moderating effects of the Number of Restaurants Nearby (Tables 4 and 5) and Proportion of Restaurants Nearby that Have Used Groupon (Tables 6 and 7).

5.3.2.1. Moderating Effects - Number of Restaurants Nearby. Within the 1947 matched pairs used for the analysis of the Average Yelp Rating,

Variable levels and number of observations for control and treatment groups.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Initial Groupon deal decision</td></tr><tr><td>Control group</td><td>Treatment group</td></tr><tr><td rowspan="2">Average Yelp Rating</td><td>Mean (std. dev.)</td><td>2.70 (0.60)</td><td>4.27 (0.32)</td></tr><tr><td>N</td><td>2447</td><td>2336</td></tr><tr><td rowspan="2">Number of Yelp Reviewsa</td><td>Mean (std. dev.)</td><td>2.59 (1.38)</td><td>102.48 (115.47)</td></tr><tr><td>N</td><td>2338</td><td>2335</td></tr><tr><td rowspan="2">Number of Restaurants Nearby</td><td>Mean (std. dev.)</td><td>11.52 (5.31)</td><td>241.33 (199.00)</td></tr><tr><td>N</td><td>2441</td><td>2326</td></tr><tr><td rowspan="2">Proportion of Restaurants Nearby that Have Used Groupon</td><td>Mean (Std. Dev.)</td><td>0 (0)</td><td>0.05 (0.05)</td></tr><tr><td>N</td><td>3511b</td><td>2320b</td></tr></table>

Notes: N indicates the number of observations.  
<sup>a</sup> The row of Number of Yelp Reviews is in bold font and provides the information on our running example.  
<sup>b</sup> Due to the distribution of Proportion of Restaurants Nearby that Have Used Groupon, 0 is both the one-third division and the median. Thus, about 1000 more data items are assigned to the low level than the high level.

984 are in the category with a low Number of Restaurants Nearby and 963 are in the category with a high Number of Restaurants Nearby. We used this categorization to test $\mathrm { H } _ { 5 \mathrm { a } } ,$ which hypothesized that the number of restaurants nearby has a significant moderating effect on the relationship between a restaurant's online review rating and that restaurant's decision to initiate a Groupon deal. In Table 4, we see that highly rated restaurants in an area with a small Number of Restaurants Nearby are more likely to initiate a Groupon deal than low rated restaurants (10.9% versus 7.3%). However, when the Number of Restaurants Nearby is large, Average Yelp Rating did not have a statistically significant impact on restaurants' initial Groupon deal decisions. Therefore, $\mathrm { H } _ { 5 a }$ is supported. Restaurants in an area with a large Number of Restaurants Nearby can be expected to have a larger consumer base than restaurants with a small Number of Restaurants Nearby. Our results suggest that highly rated restaurants in an area with few restaurants nearby leverage Groupon deals as a promotion tool to reach new consumers outside their regular consumer base.

Of the 1345 matched pairs of the analysis of the Number of Yelp Reviews, 675 are in the category with a low Number of Restaurants Nearby, with 670 in the category with a high Number of Restaurants Nearby. We predicted that the number of restaurants nearby has a significant moderating effect on the relationship between the number of online reviews of a restaurant and that restaurant's decision to initiate a Groupon deal. As Table 5 shows, when the Number of Restaurants Nearby is small, restaurants with a larger number of reviews are more likely to initiate a Groupon deal than restaurants with a small number of reviews (14.5% versus 5.2%), consistent with the direct effect. However, when the Number of Restaurants Nearby is large, restaurants with a large number of reviews are less likely to initiate a Groupon deal than those with a small number of reviews (8.9% versus 10.0%), contrary to the direct effect. Therefore, we find support for $\mathrm { H } _ { 5 \mathrm { b . } }$ In an area with fewer restaurants nearby, Groupon deals function as a promotional tool for restaurants with a large number of reviews to reach new consumers. In an area with more restaurants nearby, Groupon deals are a competitive tool for restaurants with a small number of reviews to attract consumers who would not otherwise dine there without a discount.

5.3.2.2. Moderating Effect - Proportion of Restaurants Nearby that Have Used Groupon.. Table 6 shows that when the Proportion of Restaurants Nearby that Have Used Groupon is low, highly rated restaurants are more likely to initiate a Groupon deal than are low rated restaurants. However, when the Proportion of Restaurants Nearby that Have Used Groupon is high, online review ratings have no statistically significant impact on restaurants' initial Groupon deal decisions. Therefore, our prediction in $\mathrm { H } _ { 6 a }$ that the proportion of restaurants nearby that have used Groupon has a significant moderating effect on the relationship between a restaurant's online review rating and that restaurant's decision to initiate a Groupon deal was supported.

In $\mathrm { H } _ { 6 \mathrm { b } } ,$ , we proposed that the proportion of restaurants nearby that have used Groupon has a significant moderating effect on the relationship between the number of online reviews for a restaurant and that restaurant's decision to initiate a Groupon deal. From Table 7, we find that in both the high and low conditions for the Proportion of Restaurants Nearby that Have Used Groupon, restaurants with a high number of reviews were more likely to initiate a Groupon deal than those with a low number of reviews. However, in contrast with research that focuses solely on local competition, when the Proportion of Restaurants Nearby that Have Used Groupon is low, restaurants with a high number of reviews were more likely to initiate a Groupon deal. If few restaurants nearby are using Groupon deals, a restaurant cannot benefit from spillover effects [42,48] and thus may be more likely to pursue its own Groupon deal, leading to the observed support for H<sub>6b</sub>.

## 5.3.3. 5.3.4 extended analysis of second Groupon deal decisions

We extended our analysis to restaurants' decisions to run a second Groupon deal. We defined Groupon Return Restaurants as those that ran a second promotion within 450 days of their first Groupon deal,<sup>7</sup> whereas Groupon One-Time Restaurants did not return within 450 days. We recalculated the Average Yelp Rating and Number of Yelp Reviews when a restaurant ran a second Groupon deal.<sup>8</sup> In addition to the four variables in the initial analysis, we included two variables that could affect restaurants' second Groupon deal decisions: Coupon Revenue from the First Promotion (i.e., quantity of coupons sold in the initial Groupon offering, multiplied by the price of the coupon for each restaurant) and Change in Average Yelp Rating (i.e., the value of Average Yelp Rating when a restaurant ran a second Groupon, minus that value when it ran the initial Groupon).

We applied the EPSA method to restaurants' decisions to run a second Groupon deal. This decision is relevant only for restaurants that already ran an initial Groupon deal, so the numbers of observations and matched pairs are much smaller than in the previous decision analysis (see Appendix A). Three variables (Average Yelp Rating, Number of Yelp Reviews, and Proportion of Restaurants Nearby that Have Used Groupon) have statistically significant impacts on restaurants' decisions to run a second Groupon deal. However, as we might expect, Coupon Revenue from the First Promotion has the strongest impact: High Coupon Revenue from the First Promotion increases the likelihood of running a second Groupon deal by 71.5% (from 25.3% to 43.4%). Therefore, the four variables that were important for the initial Groupon deal decision were less critical to restaurants' decisions to return.

X. Bai et al. / Decision Support Systems xxx (2017) xxx–xxx

Table 3  
Proportion of restaurants in matched pairs running an initial Groupon deal in control and treatment groups.

<table><tr><td></td><td>Control group</td><td>Treatment group</td><td>p-Values</td><td>Number of matched pairs</td><td>Hypotheses</td></tr><tr><td>Average Yelp rating</td><td>0.082</td><td>0.098**</td><td>0.038</td><td>1947</td><td> $H_1$  supported</td></tr><tr><td>Number of Yelp reviews</td><td>0.075</td><td>0.117***</td><td>&lt;0.001</td><td>1345</td><td> $H_2$  supported</td></tr><tr><td>Number of Restaurants Nearby</td><td>0.132***</td><td>0.054</td><td>&lt;0.001</td><td>869</td><td> $H_3$  supported</td></tr><tr><td>Proportion of Restaurants Nearby that Have Used Groupon</td><td>0.137***</td><td>0.108</td><td>&lt;0.001</td><td>1332</td><td> $H_4$  not supported (reverse is supported)</td></tr></table>

Notes: Significance levels determined by a Wilcoxon signed rank test.  
⁎⁎ Significant at b0.05.  
⁎⁎⁎ Significant at b0.01.

## 5.4. Sensitivity analysis and robustness checks

## 5.4.1. Sensitivity analysis

The EPSA method has limitations, particularly in terms of its stringent assumption that the differences between the treatment group and the control group can be fully captured by observable variables (i.e., strong ignorability assumption, Rosenbaum [38]). Because the conclusions may be sensitive to unobserved factors, we conducted sensitivity analyses.

Following Mithas and Krishnan [34], we defined Γ to indicate the log odds of the differential assignment to treatment due to unobserved factors. If there are no hidden factors, Γ equals 1. If potential hidden factors are underestimated, Γ is greater than 1. A larger Γ means a greater influence of potential unobservable factors on the assignment to the treatment group and the control group. If our conclusions hold when Γ is larger, we can be more confident in our results. We computed the value of Γ at which the hypothesis test results start to be insignificant (Appendix B). For almost all factors, we found significance at levels with relatively large values of Γ. The results suggest that the calculated importance of each factor does not appear to be an artifact of missing variables.

## 5.4.2. Different distances to local competitors

Local competitors are those within a designated distance from a local retailer. The distance applied to measure local competition in previous literature varies, including a radius of three-quarters of a mile for restaurants [4], 0.31 miles (half a kilometer) for hotels [32], and 0.06 mile (100 m) for coffee shops [5]. Noting these inconsistent measures, we considered three levels for the local competition variables (i.e., Number of Restaurants Nearby and Proportion of Restaurants Nearby that Have Used Groupon) in our sensitivity analysis: a quarter mile, a half mile (as in the main analysis), and one mile. The results for the alternative specifications are consistent (Appendix C).

## 5.4.3. Different quantiles to determine high versus low levels

We divided our data by assigning the top third of the data values to the treatment group and the bottom third to the control group. To address possible sensitivity to this particular data split method, we reran our analyses using a 20% split (bottom versus top 20%) and a 40% split (bottom versus top 40%). We found no significant differences in the results or conclusions.

## 5.4.4. Ethnic food categories

Our analysis above assumes that all other restaurants in a given area are the restaurant's local competitors. However, consumers also might consider, only restaurants in a specific ethnic category of food to be competitors (e.g., Mexican food). To investigate this issue, we reconstructed our two local competition factors (Number of Restaurants Nearby, Proportion of Restaurants Nearby that Have Used Groupon) according to the ethnic food categories, so that only restaurants offering the same type of food will be recognized as competitors. We ran the EPSA analysis using the new variables (Appendix D). The results were not sensitive to restrictions by ethnic food categories.

## 5.4.5. Online review ratings of nearby restaurants

Another factor that might affect a restaurant's decision to run a Groupon deal is competitors' online review ratings. To consider this issue, we constructed a new variable, Average of Competitors' Average Yelp Ratings, which is the average value of the Average Yelp Ratings across competitors within a half-mile distance. The analysis showed that a restaurant is more likely to initiate a Groupon deal when competitors have low versus high online ratings (Appendix E). That is, when competitors' online ratings are low, a restaurant is more likely to initiate a Groupon deal, perhaps with the expectation of getting both coupon revenue and acquiring new consumers who are dissatisfied with other competing restaurants. We tested our hypotheses while including the Average of Competitors' Average Yelp Ratings; the main conclusions still hold.

## 5.4.6. Different time intervals for competitors' initial Groupon deal decision

In our analysis, we used 180 days to operationalize the Proportion of Restaurants Nearby that Have Used Groupon for the initial Groupon deal decision. To check for possible sensitivity to this choice, we redid the analyses using 150 days and 210 days and found consistent results.

Table 4  
Moderating effect of Number of Restaurants Nearby on the effect of the average Yelp rating.

<table><tr><td rowspan="3"></td><td colspan="5">Main effect</td></tr><tr><td colspan="2">Average Yelp Rating</td><td rowspan="2" colspan="2">p-Values</td><td rowspan="2">Number of matched pairs</td></tr><tr><td>Low (control)</td><td>High (treatment)</td></tr><tr><td rowspan="4">Number of Restaurants Nearby</td><td>0.082</td><td>0.098**</td><td colspan="2">0.038</td><td>1947</td></tr><tr><td></td><td>Moderating effect</td><td colspan="2"></td><td></td></tr><tr><td></td><td colspan="2">Average Yelp Rating</td><td rowspan="2">p-Values</td><td rowspan="2">Number of matched pairs</td></tr><tr><td></td><td>Low (control)</td><td>High (treatment)</td></tr><tr><td rowspan="2">Number of Restaurants Nearby</td><td>Low</td><td>0.073</td><td>0.109***</td><td>0.006</td><td>984</td></tr><tr><td>High</td><td>0.090</td><td>0.087</td><td>0.812</td><td>963</td></tr></table>

Notes: Significance levels determined by a Wilcoxon signed rank test.  
⁎⁎ Significant at b0.05.  
⁎⁎⁎ Significant at b0.01.

Please cite this article as: X. Bai, et al., How e-WOM and local competition drive local retailers' decisions about daily deal offerings, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.06.003

Table 5  
Moderating Effect of Number of Restaurants Nearby on the effect of the Number of Yelp Reviews

<table><tr><td rowspan="3"></td><td colspan="5">Main effect</td></tr><tr><td colspan="3">Number of Yelp Reviews</td><td rowspan="2">p-Values</td><td rowspan="2">Number of matched pairs</td></tr><tr><td>Low (control)</td><td colspan="2">High (treatment)</td></tr><tr><td rowspan="4">Number of Restaurants Nearby</td><td>0.075</td><td colspan="2">0.117***</td><td>&lt;0.001</td><td>1345</td></tr><tr><td></td><td colspan="2">Moderating effect</td><td></td><td></td></tr><tr><td></td><td colspan="2">Number of Yelp Reviews</td><td rowspan="2">p-Values</td><td rowspan="2">Number of matched pairs</td></tr><tr><td></td><td>Low (control)</td><td>High (treatment)</td></tr><tr><td rowspan="2">Number of Restaurants Nearby</td><td>Low</td><td>0.052</td><td>0.145***</td><td>&lt;0.001</td><td>675</td></tr><tr><td>High</td><td>0.100**</td><td>0.089</td><td>0.011</td><td>670</td></tr></table>

Notes: Significance levels determined by a Wilcoxon signed rank test.  
⁎⁎ Significant at b0.05.  
⁎⁎⁎ Significant at b0.01.

## 5.4.7. Areas with tourist attractions

The Chicago area is a large metropolitan area with a significant tourism industry. The main tourist areas may attract consumers from outside of the zip code. To examine if tourist areas were key influences on our results, we redid our analyses after excluding restaurants from key zip codes linked to major Chicago tourist areas (i.e., Navy Pier, Rush Street, Old Town, Gold Coast, and Uptown). We found no significant shifts in the results or conclusions.

## 6. Discussion

## 6.1. Contributions: conceptual, methodological, and managerial

Our results provide several conceptual implications with respect to how e-WOM, local competition, and their interactions affect local retailers' decisions whether to offer daily deals (e.g., Groupon). Previous literature [31] has suggested two factors related to e-WOM: valence (positivity or negativity) and volume. We operationalized valence as the average numeric rating of the reviews of a restaurant and volume as the number of reviews. With respect to the valence, highly rated restaurants were more likely to initiate a Groupon deal, which suggests that decision makers and managers were attracted to the coupon revenues and also confident that their good ratings would continue. With respect to the volume, the greater the number of reviews for a restaurant, the more likely that restaurant was to initiate a Groupon deal. These results indicate that decisions about initial daily deals contrast with the results from earlier work on traditional couponing decisions [6,36].

We also considered two local competition factors: the number of restaurants nearby and the proportion of restaurants nearby that had used Groupon. The finding that restaurants in an area with few restaurants nearby were more likely to initiate a Groupon deal than were those in an area with a large number of restaurants nearby implied that restaurant managers initially regarded Groupon deals as a mechanism to draw in new consumers. Contrary to previous local competition literature [11,16,40], this study offers clear evidence that Groupon deals grant restaurant owners a way to create a competitive advantage by drawing in consumers and are not simply a response mechanism to deal with competitors' Groupon deals.

We investigate the moderating role of local competition on the impact of e-WOM on restaurants' daily deal offering decisions, which is rare in previous literature, and we find a negative moderating role for the number of restaurants nearby. That is, high online ratings had a positive impact on a restaurant's initial Groupon deal decision in an area with a small number of restaurants nearby but no statistically significant impact in an area with a large number of restaurants nearby. More online reviews also had a positive impact on a restaurant's initial Groupon deal decision in an area with a small number of restaurants nearby, versus a negative impact in an area with a large number of restaurants nearby. Thus, when there are few restaurants nearby, Groupon deals are a promotion tool that restaurants with high ratings and a large number of reviews use to reach new consumers. In an area with many restaurants nearby, Groupon deals are instead a competitive tool for restaurants with a small number of reviews, designed to attract more consumers.

With respect to the moderating role of Groupon usage by nearby restaurants, we found a negative moderating effect by the proportion of restaurants nearby that had used Groupon. High ratings had a positive impact on a restaurant's initial Groupon deal decision when no other nearby restaurants had used Groupon. Yet high ratings had no statistically significant impact when a certain proportion of restaurants nearby already had used Groupon. Similarly, when no nearby restaurants had used Groupon, restaurants with a large number of reviews have more incentive to initiate their own Groupon deal. Our results suggest that

## Table 6

Moderating Effect of Proportion of Restaurants Nearby that Have Used Groupon on the effect of the Average Yelp Rating.

<table><tr><td rowspan="3"></td><td colspan="4">Main effect</td></tr><tr><td colspan="2">Average Yelp Rating</td><td rowspan="2">p-Values</td><td rowspan="2">Number of matched pairs</td></tr><tr><td>Low (control)</td><td>High (treatment)</td></tr><tr><td>Proportion of Restaurants Nearby that Have Used Groupon</td><td>0.082</td><td>0.098**</td><td>0.038</td><td>1947</td></tr><tr><td rowspan="3"></td><td colspan="4">Moderating effect</td></tr><tr><td colspan="2">Average Yelp Rating</td><td rowspan="2">p-Values</td><td rowspan="2">Number of matched pairs</td></tr><tr><td>Low (control)</td><td>High (treatment)</td></tr><tr><td rowspan="2">Proportion of Restaurants Nearby that Have Used Groupon</td><td>Low</td><td>0.078</td><td>0.108***</td><td>0.012</td></tr><tr><td>High</td><td>0.086</td><td>0.084</td><td>0.861</td></tr></table>

Notes: Significance levels determined by a Wilcoxon signed rank test.  
⁎⁎ Significant at b0.05.  
⁎⁎⁎ Significant at b0.01.

Moderating Effect of Proportion of Restaurants Nearby that Have Used Groupon on the effect of the Number of Yelp Reviews.

<table><tr><td rowspan="3"></td><td colspan="5">Main effect</td></tr><tr><td colspan="3">Number of Yelp Reviews</td><td rowspan="2">p-Values</td><td rowspan="2">Number of matched pairs</td></tr><tr><td>Low (control)</td><td colspan="2">High (treatment)</td></tr><tr><td rowspan="4">Proportion of Restaurants Nearby that Have Used Groupon</td><td>0.075</td><td colspan="2">0.117***</td><td>&lt;0.001</td><td>1345</td></tr><tr><td></td><td colspan="2">Moderating effect</td><td></td><td></td></tr><tr><td></td><td colspan="2">Number of Yelp Reviews</td><td rowspan="2">p-Values</td><td rowspan="2">Number of matched pairs</td></tr><tr><td></td><td>Low (control)</td><td>High (treatment)</td></tr><tr><td rowspan="2">Proportion of Restaurants Nearby that Have Used Groupon</td><td>Low</td><td>0.080</td><td>0.150***</td><td>&lt;0.001</td><td>672</td></tr><tr><td>High</td><td>0.071</td><td>0.085**</td><td>0.031</td><td>673</td></tr></table>

Notes: Significance levels determined by a Wilcoxon signed rank test.  
⁎⁎ Significant at b0.05.  
⁎⁎⁎ Significant at b0.01.

when no other nearby restaurants have run a Groupon deal, restaurants do not benefit from a spillover effect [42,48], and a restaurant with high ratings and many reviews is more likely to pursue its own Groupon deal.

All of our results are based on comparisons across matched pairs of restaurants that were determined were statistically equivalent, except for the indicated treatment variable. Our EPSA paired comparison analysis extends standard PSA analysis in two ways. First, our propensity score matching entails the development of separate groupings of the treatment and control variable combinations, individually for each of the independent variables we want to test. Thus, we can test the causal relationship for each independent variable separately, rather than building an analysis of multiple variables that might mask each factor's true impacts. Second, we considered independent causal variables that are continuous. For each variable, we created the treatment versus control groups by dividing the observations into the bottom (control group) and top (treatment group) third. This approach is not cost-free though, in that it results in the loss of some potential pairs (middle third). On balance, we considered it important to ensure the paired restaurants were very different on the treatment variable under analysis.

These results provide useful managerial implications for daily deal sites. The daily deal site should target non-participating restaurants that are highly rated, heavily reviewed local retailers located in areas with a small number of other competitors or those in which no other competitors have run daily deals. Similarly, our results suggest that daily deal sites pursue local restaurants with a small number of online reviews in an area with many other competitors also are likely to initiate a daily deal. Therefore, daily deal sites, such as Groupon, might consider a redeployment of their resources to target business customers more likely to sign up.

## 6.2. Limitations and future research

Our empirical test uses EPSA, a quasi-experimental method that allows for an analysis of causation among the paired observations. However, there are costs of using this technique. First, EPSA can result in small numbers of paired observations for the causal tests raising issues common in bigger n versus smaller n discussions. Second, EPSA creates an omitted variable risk. We examine this issue through use of various sensitivity analyses, but the risk cannot be totally resolved. Third, EPSA requires acceptance of the risk that unpaired observations (observations not included in a PSA or EPSA analysis) differ inherently from paired observations. All of these concerns suggest that though our results are conceptually interesting, statistically significant, and empirically verified, further analyses using different approaches would be a worthwhile exercise.

Every sampling decision also involves trade-offs. Our need to create a data set that incorporated the full population of ratings data from Yelp, location data (geographical information) in Yelp, and daily deal data from Groupon necessitated our focus on one category (restaurants) and one location (Chicago). These choices clearly raise generalizability questions and suggest the need for different empirical analyses that prioritize broader category and location coverage.

## 6.3. Conclusion

We have introduced an extended propensity score analysis (EPSA) method to provide a causal analysis of the effects of e-WOM, local competition, and their interactions on local retailers' decisions to offer a daily deal. In terms of e-WOM, local retailers with high ratings and more reviews are more likely to initiate a daily deals. In terms of local competition, in an area with few retailers, local retailers are more likely to initiate a daily deal. Local retailers are also more likely to engage in initial daily deal if their competitors have not used daily deals previously. In an area with few retailers, daily deals offer a promotional tool for local retailers with high online ratings and many online reviews, whereas in an area with many retailers, daily deals constitute a competitive tool for local retailers with few online reviews. When no other nearby competitors have used daily deals, local competitors with a high rating and a large number of online reviews have a stronger incentive to initiate their daily deals. These results have important implications for understanding the effects of e-WOM, local competition, and their interactions on local retailers' daily deal offering decisions.

## Appendix A. Extended analysis of second Groupon deal decisions

## Table A.1

Variable levels and number of observations for control and treatment groups, second Groupon deal decision

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Second Groupon deal decision</td></tr><tr><td>Control group</td><td>Treatment group</td></tr><tr><td rowspan="2">Average Yelp Rating</td><td>Mean (Std. Dev.)</td><td>2.46 (0.51)</td><td>4.34 (0.30)</td></tr><tr><td>N</td><td>196</td><td>138</td></tr><tr><td rowspan="2">Number of Yelp Reviews</td><td>Mean (Std. Dev.)</td><td>3.49 (1.79)</td><td>42.28 (25.53)</td></tr><tr><td>N</td><td>246</td><td>221</td></tr></table>

Please cite this article as: X. Bai, et al., How e-WOM and local competition drive local retailers' decisions about daily deal offerings, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.06.003

Table A.1 (continued)

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Second Groupon deal decision</td></tr><tr><td>Control group</td><td>Treatment group</td></tr><tr><td rowspan="2">Number of Competitors Nearby</td><td>Mean (Std. Dev.)</td><td>9.31 (4.64)</td><td>197.70 (175.73)</td></tr><tr><td>N</td><td>242</td><td>229</td></tr><tr><td rowspan="2">Proportion of Restaurants Nearby that Have Used Groupon</td><td>Mean (Std. Dev.)</td><td>0 (0)</td><td>0.10 (0.12)</td></tr><tr><td>N</td><td>298</td><td>230</td></tr><tr><td rowspan="2">Coupon Revenue from the First Promotion</td><td>Mean (Std. Dev.)</td><td>4689.57 (1885.27)</td><td>32,966.00 (31,762.81)</td></tr><tr><td>N</td><td>232</td><td>227</td></tr><tr><td rowspan="2">Change in Average Yelp Rating</td><td>Mean (Std. Dev.)</td><td>-0.81 (0.51)</td><td>0.73 (0.48)</td></tr><tr><td>N</td><td>317</td><td>135</td></tr></table>

Notes: N indicates the number of observations.

## Table A.2

Proportion of restaurants in matched pairs running a second Groupon deal in control and treatment groups

<table><tr><td></td><td>Control group</td><td>Treatment group</td><td>p-Values</td><td>Number of matched pairs</td></tr><tr><td>Average Yelp Rating</td><td>0.377*</td><td>0.321</td><td>0.091</td><td>53</td></tr><tr><td>Number of Yelp Reviews</td><td>0.408</td><td>0.461**</td><td>0.035</td><td>76</td></tr><tr><td>Number of Restaurants Nearby</td><td>0.317</td><td>0.317</td><td>0.99</td><td>41</td></tr><tr><td>Proportion of Restaurants Nearby that Have Used Groupon</td><td>0.436***</td><td>0.390</td><td>0.002</td><td>172</td></tr><tr><td>Coupon Revenue from the First Promotion</td><td>0.253</td><td>0.434***</td><td>&lt;0.001</td><td>99</td></tr><tr><td>Change in Average Yelp Rating</td><td>0.361</td><td>0.421***</td><td>&lt;0.001</td><td>133</td></tr></table>

Notes: Significance levels determined by a Wilcoxon signed rank test.  
Significant at b0.1.  
⁎⁎ Significant at b0.05.  
⁎⁎⁎ Significant at b0.01.

## Appendix B. EPSA sensitivity analysis

Table B.1

Γ Values in Sensitivity Analysis.

<table><tr><td>Variables</td><td>Initial Groupon deal decision</td></tr><tr><td>Average Yelp Rating</td><td>1.1</td></tr><tr><td>Number of Yelp Reviews</td><td>34.0</td></tr><tr><td>Number of Competitors Nearby</td><td>41.4</td></tr><tr><td>Proportion of Restaurants Nearby that Have Used Groupon</td><td>23.7</td></tr></table>

## Appendix C. Different distances to determine nearby restaurants

## Table C.1

Proportion of restaurants in matched pairs running an initial Groupon deal in control and treatment groups.

<table><tr><td rowspan="2"></td><td colspan="4">Quarter mile distance</td></tr><tr><td>Control group</td><td>Treatment group</td><td>Number of matched pairs</td><td>Hypotheses</td></tr><tr><td>Average Yelp Rating</td><td>0.080</td><td>0.099**</td><td>1929</td><td>H1 supported</td></tr><tr><td>Number of Yelp Reviews</td><td>0.079</td><td>0.117***</td><td>1360</td><td>H2 supported</td></tr><tr><td>Number of Competitors Nearby</td><td>0.121***</td><td>0.076</td><td>1135</td><td>H3 supported</td></tr><tr><td>Proportion of Restaurants Nearby that Have Used Groupon</td><td>0.135***</td><td>0.102</td><td>1513</td><td>H4 not supported (reverse is supported)</td></tr><tr><td rowspan="2"></td><td colspan="4">One mile distance</td></tr><tr><td>Control group</td><td>Treatment group</td><td>Number of matched pairs</td><td>Hypotheses</td></tr><tr><td>Average Yelp Rating</td><td>0.089</td><td>0.099*</td><td>1940</td><td>H1 supported</td></tr><tr><td>Number of Yelp Reviews</td><td>0.072</td><td>0.125***</td><td>1295</td><td>H2 supported</td></tr><tr><td>Number of Competitors Nearby</td><td>0.128***</td><td>0.051</td><td>752</td><td>H3 supported</td></tr><tr><td>Proportion of Restaurants Nearby That Have Used Groupon</td><td>0.137***</td><td>0.105</td><td>1350</td><td>H4 not supported (reverse is supported)</td></tr></table>

Notes: Significance levels determined by a Wilcoxon signed rank test.  
⁎⁎ Significant at b0.05.  
⁎⁎⁎ Significant at b0.01.

Please cite this article as: X. Bai, et al., How e-WOM and local competition drive local retailers' decisions about daily deal offerings, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.06.003

## Appendix D. Ethnic food categories of restaurants

## Table D.1

Proportion of restaurants in matched pairs running an initial Groupon deal in control and treatment groups.

<table><tr><td></td><td>Control group</td><td>Treatment group</td><td>Number of matched pairs</td><td>Hypotheses</td></tr><tr><td>Average Yelp Rating</td><td>0.080</td><td>0.092***</td><td>1927</td><td>H1 supported</td></tr><tr><td>Number of Yelp Reviews</td><td>0.070</td><td>0.118***</td><td>1466</td><td>H2 supported</td></tr><tr><td>Number of Competitors Nearby</td><td>0.127***</td><td>0.054</td><td>1456</td><td>H3 supported</td></tr><tr><td>Proportion of Restaurants Nearby that Have Used Groupon</td><td>0.144***</td><td>0.094</td><td>501</td><td>H4 not supported (reverse is supported)</td></tr></table>

Notes: Significance levels determined by a Wilcoxon signed rank test.  
⁎ Significant at b0.1.  
\*\* Significant at b0.05.  
⁎⁎⁎ Significant at b0.01.

## Appendix E. Online review ratings of other restaurants nearby

## Table E.1

Proportion of restaurants in matched pairs running an initial Groupon deal in control and treatment groups.

<table><tr><td></td><td>Control group</td><td>Treatment group</td><td>Number of matched pairs</td><td>p-Values</td><td>Hypotheses</td></tr><tr><td>Average of Competitors&#x27; Average Yelp Ratings</td><td>0.127***</td><td>0.096</td><td>1748</td><td>0.003</td><td>-</td></tr><tr><td colspan="6">Hypotheses tests with Average of Competitors&#x27; Average Yelp Ratings</td></tr><tr><td>Average Yelp Rating</td><td>0.076</td><td>0.096**</td><td>1889</td><td>0.026</td><td>H1 supported</td></tr><tr><td>Number of Yelp Reviews</td><td>0.060</td><td>0.126***</td><td>1334</td><td>&lt;0.001</td><td>H2 supported</td></tr><tr><td>Number of Competitors Nearby</td><td>0.112***</td><td>0.049</td><td>858</td><td>&lt;0.001</td><td>H3 supported</td></tr><tr><td>Proportion of Restaurants Nearby that Have Used Groupon</td><td>0.117</td><td>0.109</td><td>1324</td><td>0.178</td><td>H4 not supported</td></tr></table>

Notes: Significance levels determined by a Wilcoxon signed rank test.  
⁎⁎ Significant at b0.05.  
⁎⁎⁎ Significant at b0.01.

## References

[1] M. Anderson, J. Magruder, Learning from the crowd: regression discontinuity estimates of the effects of an online review database, Econ. J. 122 (563) (2012) 957–989.

[2] X. Bai, J.R. Marsden, W.T. Ross Jr., G. Wang, Relationships among minimum requirements, Facebook likes, and Groupon deal outcomes, ACM Trans. Manag. Inf Syst. 6 (3) (2015) 1–28.

[3] R. Bapna, P. Goes, R. Gopal, J.R. Marsden, Moving from data-constrained to data-enabled research: experiences and challenges in collecting, validating and analyzing large-scale e-commerce data, Stat. Sci. (2006) 116–130.

[4] J. Blevins, A. Khwaja, N. Yang, Firm expansion, size spillovers and market dominance in retail chain dynamics, Manag. Sci. (2017) (forthcoming).

[5] B. Bollinger, P. Leslie, A. Sorensen, Calorie posting in chain restaurants, Am. Econ. J. Econ. Pol. 3 (1) (2011) 91–128.

[6] S. Borenstein, Price discrimination in free-entry markets, RAND J. Econ. 16 (3) (1985) 380–397.

[7] J.W. Byers, M. Mitzenmacher, G. Zervas, Daily deals: prediction, social diffusion, and reputational ramifications, Proceedings of the fifth ACM international conference on Web search and data mining 2012 pp. 543–552.

[8] Y. Chen, J. Xie, Third-party product review and firm marketing strategy, Mark. Sci. 24 (2)(2005) 218-240.

[9] Y. Chen, X. Li, M. Sun, Competitive mobile targeting, Mark. Sci. (2017) (Forthcoming).

[10] J.A. Chevalier, D. Mayzlin, The effect of word of mouth on sales: online book reviews, J. Mark. Res. 43 (3) (2006) 345–354.

[11] P. Davis, Spatial competition in retail markets: movie theaters, RAND J. Econ. 37 (4) (2006) 964-982

[12] C. Dellarocas, Strategic manipulation of internet opinion forums: implications for consumers and rms, Manag. Sci. 52 (10) (2006) 1577 1593.

[13] C. Dellarocas, C.A. Wood, The sound of silence in online feedback: estimating trading risks in the presence of reporting bias, Manag. Sci. 54 (3) (2008) 460-476.

[14] V. Dhar, E.A. Chang, Does chatter matter? The impact of user-generated content on music sales, J. Interact. Mark. 23 (4) (2009) 300–307.

[15] N. Donthu, R.T. Rust, Note—estimating geographic customer densities using kernel density estimation, Mark. Sci. 8 (2) (1989) 191–203.

[16] J.A. Duan, C.F. Mela, The role of spatial demand on outlet location and pricing, J. Mark. Res. 46 (2) (2009) 260–278.

[17] W. Duan, B. Gu, A.B. Whinston, Do online reviews matter?—an empirical investigation of panel data, Decis. Support. Syst. 45 (4) (2008) 1007–1016.

[18] B. Edelman, S. Jaffe, S.D. Kominers, To groupon or not to groupon: the profitability of deep discounts, Mark. Lett. 27 (1) (2016) 39–53.

[19] J. Feng, X. Li, X.M. Zhang, Online Product Reviews-Triggered Dynamic Pricing: Theory and Evidence, 2016 (Working paper, available at SSRN: http://ssrn.com/abstract=2510470).

[20] N.M. Fong, Z. Fang, X. Luo, Geo-conquesting: competitive locational targeting of mobile promotions, I. Mark, Res, 52 (5) (2015) 726–735.

[21] B. Gu, Q. Ye, First step in social media: measuring the influence of online management responses on customer satisfaction, Prod. Oper. Manag. 23 (4) (2014) 570-582

[22] S. Gupta, Impact of sales promotions on when, what, and how much to buy, J. Mark. Res, 25(4)(1988) 342-355

[23] S. Gupta, R. Weaver, T. Keiningham, L. Williams, Are daily deals good for merchants, Harvard Business School Case, 9, 2012, pp. 513–559.

[24] T.H. Hannan, Market share inequality, the number of competitors, and the HHI: an examination of bank pricing, Rev. Ind. Organ. 12 (1) (1997) 23–35.

[25] H. Hotelling, Stability in competition, The Collected Economics Articles of Harold Hotelling, Springer, New York 1990, pp. 50–63.

[26] T. Klier, D.P. McMillen, Evolving agglomeration in the US auto supplier industry, J. Reg. Sci. 48 (1) (2008) 245–267.

[27] D. Kuksov, Y. Xie, Pricing, frills, and customer ratings, Mark. Sci. 29 (5) (2010) 925–943.

[28] V. Kumar, B. Rajan, Social coupons as a marketing strategy: a multifaceted perspective, J. Acad. Mark. Sci. 40 (1) (2012) 120–136.

[29] Y. Kwark, J. Chen, S. Raghunathan, Online product reviews: implications for retailers and competing manufacturers, Inf. Syst. Res. 25 (1) (2014) 93–110.

[30] X. Li, L.M. Hitt, Z.J. Zhang, Product reviews and competition in markets for repeat purchase products, J. Manag. Inf. Syst. 27 (4) (2011) 9–42.

[31] Y. Liu, Word of mouth for movies: its dynamics and impact on box office revenue, J. Mark. 70 (3) (2006) 74–89.

[32] D. Mayzlin, Y. Dover, J. Chevalier, Promotional reviews: an empirical investigation of online review manipulation. Am Econ Rev 104 (8) (2014) 2421–2455

[33] J. Mejia, A. Gopal, M. Trusov, Deal or no deal? Consumer expectations and competition in daily deals International Conference on Information Systems 2016.

[34] S. Mithas, M.S. Krishnan, From association to causation via a potential outcomes approach, Inf. Syst. Res. 20 (2) (2009) 295–313.

[35] W.W. Moe, D.A. Schweidel, Online product opinions: incidence, evaluation, and evolution, Mark, Sci, 31 (3) (2012) 372–386.

[36] C. Narasimhan, Competitive promotional strategies, J. Bus. (1988) 427–449.

[37] J. Pinkse, M.E. Slade, C. Brett, Spatial price competition: a semiparametric approach, Econometrica 70 (3) (2002) 1111–1153.

[38] P.R. Rosenbaum, Choice as an alternative to control in observational studies, Stat. Sci. (1999).259–278

[39] H. Rui, Y. Liu, A. Whinston, Whose and what chatter matters? The effect of tweets on movie sales. Decis, Support, Syst, 55 (4) (2013) 863–870

Please cite this article as: X. Bai, et al., How e-WOM and local competition drive local retailers' decisions about daily deal offerings, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.06.003

[40] G. Shaffer, Z.J. Zhang, Competitive coupon targeting, Mark. Sci. 14 (4) (1995) 395–416.

[41] Q. Shen, A dynamic model of entry and exit in a growing industry, Mark. Sci. 33 (5) (2014) 712–724.

[42] Q. Shen, P. Xiao, McDonald's and KFC in China: competitors or companions? Mark. Sci. 33 (2) (2014) 287–307.

[43] J. Shin, K. Sudhir, A customer management dilemma: when is it profitable to reward one's own customers? Mark. Sci. 29 (4) (2010) 671–689.

[44] Smith Brain Trust, Escaping the Groupon curse for restaurants, http://www.rhsmith. umd.edu/news/escaping-groupon-curse-restaurants 2015 (Accessed 17.05.27)

[45] R. Thomadsen, The effect of ownership structure on prices in geographically differentiated industries, RAND J. Econ. (2005) 908–929.

[46] J. Tirole, The Theory of Industrial Organization, MIT press, Cambridge, MA, 1988.

[47] P.R. Varadarajan, Consumer responses to small business coupon sales promotions, Am. J. Small Bus. 9 (2) (1984) 17–26.

[48] L. Wang, Essays on the Interface of Location-Based Services, consumers' Shopping Behavior and firms' Marketing StrategyDoctoral Dissertation Department of Operations and Information Management, University of Connecticut, 2014.

[49] L. Wang, R. Gopal, R. Shankar, J. Pancras, On the brink: predicting business failure with mobile location-based checkins, Decis. Support. Syst. 76 (2015) 3–13.

[50] J. Wu, M. Shi, M. Hu, Threshold effects in online group buying, Manag. Sci. 61 (9) (2014) 2025–2040.

Xue Bai is Associate Professor of Management Information Systems in the School of Business at University of Connecticut. She received her Ph.D. degree in Management Information Systems from Carnegie Mellon University. Her research interests include data mining, business analytics, and mathematical modeling, applied to online platforms and online social media. She has published in top management science and information systems journals including Management Science, Information Systems Research, INFORMS Journal on Computing, ACM Transactions on Management Information Systems, and Decision Support Systems. She is Associate Editor with Information Systems Research and Decision Support Systems. She has also served as special issue Associate Editor at MIS Quarterly and special issue Senior Editor at Production and Operations Management Society.

James R. Marsden is Board of Trustees Distinguished Professor at the Department of Operations and Information Management (OPIM) at the University of Connecticut. Dr. Marsden currently serves as Editor-in-Chief of Decision Support Systems and has a lengthy publication record in market innovation and analysis, economics of information, artificial intelligence, data analytics, and production theory. His research work has appeared in Journal of Management Information Systems, MIS Quarterly; Management Science, Journal of Law and Economics, American Economic Review, Journal of Economic Theory, Journal of Political Economy IEEE Transactions on Systems, Man, and Cybernetics; Decision Support Systems Statistical Science, Journal of Statistical Planning and Inference, and numerous other leading academic research journals. He received his A.B. from the University of Illinois, his M.S. and Ph.D. from Purdue University, and completed an NSF Post-doctoral Fellowship at the University of North Carolina - Chapel Hill. Also holding a J.D., Jim has been admitted to both the Kentucky Bar and the Connecticut Bar. He has held visiting positions at KU-Leuven, the University of Arizona, Purdue University and the University of York (England).

William T. Ross, Jr. is the Voya Financial Chair in Marketing at the University of Connecticut. He earned his Ph.D. in Business from Duke University. His research is in the areas of channel and brand management, and buyer decision-making. His publications have appeared in Journal of Consumer Research, Journal of Marketing, Journal of Marketing Research, Marketing Science, Management Science, and Journal of Retailing among others. He has taught at the undergraduate, MBA, EMBA, and doctoral level including courses in marketing management, marketing strategy, retailing, marketing research, consumer behavior, sales force management, business-to-business marketing, business ethics, and channels of distribution.

Gang Wang is an Assistant Professor of Management Information Systems at the University of Delaware. He received his Ph.D. degree in Operations and Information Management from the University of Connecticut. His research interests include social media, e-Business platforms, and firm strategies in e-Markets. His research has been published in ACM Transactions on Management Information Systems (TMIS). He has presented his work at confer ences like ICIS and INFORMS

Please cite this article as: X. Bai, et al., How e-WOM and local competition drive local retailers' decisions about daily deal offerings, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.06.003
