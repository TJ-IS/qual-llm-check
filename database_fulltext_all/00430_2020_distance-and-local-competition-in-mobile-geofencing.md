---
otero_id: 430
otero_key: "XNXKEBW2"
title: "Distance and Local Competition in Mobile Geofencing"
authors: "Yi-Jen (Ian) Ho; Sanjeev Dewan; Yi-Chun (Chad) Ho"
year: "2020"
journal: "Information Systems Research"
doi: "10.1287/isre.2020.0953"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [156.62.3.11] On: 27 October 2020, At: 08:22 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

![](/api/attachments/XNXKEBW2/fulltext/images/fcc33030bf559b0b532624e6057a70d50c3b0f2461e7bfc283445674ee288835.jpg)

## Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Distance and Local Competition in Mobile Geofencing

Yi-Jen (Ian) Ho, Sanjeev Dewan, Yi-Chun (Chad) Ho

To cite this article:

Yi-Jen (Ian) Ho, Sanjeev Dewan, Yi-Chun (Chad) Ho (2020) Distance and Local Competition in Mobile Geofencing. Information Systems Research

Published online in Articles in Advance 22 Oct 2020

https://doi.org/10.1287/isre.2020.0953

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2020, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individual professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Distance and Local Competition in Mobile Geofencing

Yi-Jen (Ian) Ho,<sup>a</sup> Sanjeev Dewan,<sup>b</sup> Yi-Chun (Chad) Ho<sup>c,</sup>\*

<sup>a</sup> Smeal College of Business, Pennsylvania State University, University Park, Pennsylvania 16802; <sup>b</sup> Merage School of Business, University of California, Irvine, California 92697; <sup>c</sup> School of Business, George Washington University, Washington, District of Columbia 20052

Contact: ian.ho@psu.edu, https://orcid.org/0000-0002-2480-480X (Y-J(C)H); sdewan@uci.edu,

https://orcid.org/0000-0002-8768-8092 (SD); chadho@gwu.edu, https://orcid.org/0000-0003-0383-1216 (Y-C(C)H)

Received: Revised: August 19, 201<sub>Accepted:</sub> Published Online in Articles in Advance: October 22, 2020

https://doi.org/10.1287/isre.2020.0953

Copyright:

Abstract. This research studies the performance of geofencing, a practice where mobile users are targeted within a predefined virtual geographic boundary around an advertiser’s establishment. We argue the significance of distance (i.e., the mileage from a consumer to a focal establishment) and local competition (i.e., the number of alternatives in consumer vicinity) in ad responses. Drawing on the notion of the purchase funnel, we develop a twostage hierarchical Bayesian model to examine consumer click and conversion choices. A unique data set of geofencing ad impressions is collected from one of the largest locationbased marketing agencies in the United States. The results suggest that local competition matters in the click stage, whereas distance influences the propensity of conversion. Quantitatively, one additional competitor in the consumer vicinity zone lowers the clickthrough rate by 1.03%, whereas a 1-mile increase in distance results in a 17.64% decrease in the conversion rate. We also find a significant interactive effect, whereby a higher degree of local competition amplifies the negative impact of distance on the likelihood of conversions. Additionally, product differentiation ameliorates the effects of distance and local competition, whereas these effects are found to be more prominent during office working hours. This study discovers the stage-varying roles of distance and local competition along the customer journey and offers new directions for more effective location-based targeting

History: Param Singh, Senior Editor; Jianqing Chen, Associate Editor.

Keywords: location-based advertising • geofencing • mobile • purchase funnel • competition • hierarchical Bayes

## 1. Introduction

The ubiquity of global positioning system (GPS)- enabled devices continues to drive demand for location-based services, projected to reach \$86 billion by 2023 globally (Netscribes 2019). As users spend more time on mobile devices, advertising budgets are also migrating to the mobile platform. Industry observers estimated that location-targeted mobile ad spending in the United States alone is projected to grow from \$20 billion in 2018 to \$32 billion in 2021, which is a 21.1% compound annual growth rate during this period (BIA/Kelsey 2017). The typical milieu for such advertising is mobile apps that provide locationbased services, such as Yelp and Foursquare for local businesses and Uber and Lyft for ride-sharing services. The promise of location-based advertising is that it enables advertisers to target consumers at the right time and the right place when they are most responsive to the messaging. McKinsey Global Institute (2011) estimates that location-based services will account for \$100 billion in revenues for service providers and more than \$700 billion of value to end consumers. With the ability to exploit proximity and immediacy, location-based services are at the heart of online-to-offline (O2O) commerce, which has been recognized as a trillion-dollar opportunity (Inc 2016).

Given its economic significance, increased attention is being directed toward mobile location-based advertising (LBA), in both information systems (Fang et al. 2015) and marketing (Fong et al. 2015, Chen et al. 2017) literature. Much of the prior research has investigated the relationship between mobile coupon redemption and various contextual factors, such as geographical crowdedness (Andrews et al. 2016), timing (Luo et al. 2014), and specific consumer segments (commuters in Ghose et al. 2019b). Among all the factors, distance is the one that has drawn the most attention from researchers (Cho et al. 2011, Luo et al. 2014, Qiu et al. 2018, Molitor et al. 2020). The literature consistently suggests that the farther a targeted user is located relative to the focal establishment, the lower the likelihood of a positive response to targeting. Yet, geofencing campaigns in practice use an arbitrary geofence radius. In this regard, current geofencing practices account for neither the variation of the distances between consumers and establishments nor other location-specific factors, such as local competition.

Local competition is expected to play a significant role in affecting the performance of location-based advertising. Intuitively, the larger the number of alternatives available to a consumer, the lower the likelihood that the consumer will respond to a geo-targeting ad from the advertising establishment. In the economics literature, the intensity of competition is modeled as the number of competitors in a focal segment (Bresnahan and Reiss 1991, Danaher et al. 2008). Accordingly, we define local competition in terms of the number of similar establishments in the consumer’s vicinity. Our analysis of geofencing has two interrelated spheres of influence: (1) an establishment-specific geofence centered on a focal establishment, which determines the distance to a consumer and (2) a consumer-specific vicinity zone centered on a specific consumer’s location, which defines the level of local competition observed by the consumer with respect to a given advertiser. Currently, the practice of geofencing targets mobile devices purely based on whether they are inside or outside the geofence. With increasingly powerful real-time analytics capabilities, our analysis will demonstrate that advertisers would benefit from exploiting data on local competition, in conjunction with proximity (or distance) of the consumer in a geofence. Specifically, we address the following research questions: What are the direct and interactive impacts of distance and local competition on the performance of geofence advertising? How do these impacts vary across the click and conversion stages of the consumer journey?

To answer these questions, we have access to a unique data set of geofence advertising transactions from one of the largest location-based marketing agencies in the United States. Our data consist of all geofence campaigns run by the marketing agency in March 2017. In the context of mobile geofencing, consumers are exposed to in-app banner ads when they enter the targeted zone with location-based services enabled. We select one of the largest nationwide dining chains as the primary focus of our analysis, for two key reasons.<sup>1</sup> First, the restaurant industry, with annual revenues of around \$200 billion (Statista 2016), is one of the most active sectors in the arena of geofence advertising (BIA/Kelsey 2014). Restaurants lead other industries in using geofencing, allocating approximately 40% of their LBA budgets toward geofencing (Verve Mobile 2013). Second, consumers actively consider alternatives when deciding which restaurant to visit, as reflected in the widespread use of local review services, such as Yelp and Google Maps. Correspondingly, data on local competition are also available from such review sites, allowing us to measure local competition in a relatively precise manner. To calculate distance, we use location data consisting of latitude/longitude coordinates for both mobile devices and advertiser establishments. In sum, the prominence of the restaurant industry in geofence advertising, combined with the ready availability of distance and local competition data, makes restau rants an ideal industry segment to focus on.

Our research broadly examines the performance of geofence advertising, taking a relatively wider lens than prior work on location-based advertising in a number of dimensions (Table 1). First, prior research has looked at either click (Ghose et al. 2013) or conversion (Luo et al. 2014) outcomes—one or the other in isolation. In contrast, we examine both click and con version performance in a joint manner, albeit using proxy measures for conversion, as explained later. Second, prior work is based on specific contexts (mobile coupons as in Luo et al. 2014) or narrow geographic regions (a single city in China as in Fang et al. 2015), whereas we look at diverse geofencing campaigns targeted at an unrestricted cross section of users across the United States. Moreover, unlike some existing work that discretizes distance in a limited number of bins (within or beyond 500 m in Fang et al. 2015), we are able to observe and measure actual distance based on the latitude/longitude coordinates of both devices and advertising establishments. With respect to competition, researchers look at the effect of couponing in a setting of a pair of head-to-head competitors (Fang et al. 2015, Dubé et al. 2017), whereas we broadly consider the state of local competition in the vicinity zones of targeted consumers. Finally, whereas each of the prior studies is restricted to a particular publisher (i.e., short message service or a single app), the advertising impressions in our study are drawn from a vast network of mobile apps for both the Android and iOS platforms, providing more generalizable use cases in action.

Table 1. Related Literature of Location-Based Advertising

<table><tr><td>Reference</td><td>Outcome of interest</td><td>Targeting method</td><td>Proximity</td><td>Competition</td><td>Publisher(s)</td></tr><tr><td>This study</td><td>Click and conversion decisions</td><td>Geofencing</td><td>Actual distance</td><td>Availability of alternatives</td><td>Multiple apps</td></tr><tr><td>Ghose et al. 2013</td><td>Click decision</td><td>Not applicable</td><td>Approximated distance based on user home address</td><td>Not applicable</td><td>Microblogging</td></tr><tr><td>Luo et al. 2014 &amp; Fang et al. 2015</td><td>Coupon redemption</td><td>Geofencing</td><td>500-meter proximity of the focal location</td><td>Not applicable</td><td>SMS</td></tr><tr><td>Fong et al. 2015</td><td>Coupon redemption</td><td>Geo-conquesting</td><td>200-meter proximity of the focal, competitive and benchmark locations</td><td>A competing theatre</td><td>SMS</td></tr><tr><td>Dubé et al. 2017</td><td>Price elasticity</td><td>Geo-conquesting</td><td>500-meter proximity of the focal and competitive locations</td><td>A competing theatre</td><td>SMS</td></tr><tr><td>Andrews et al. 2016</td><td>Coupon redemption</td><td>Subway graphical targeting</td><td>Not applicable</td><td>Not applicable</td><td>SMS</td></tr><tr><td>Ghose et al. 2019a</td><td>Coupon redemption</td><td>Specific consumer segments</td><td>Not applicable</td><td>Not applicable</td><td>Focal transportation app</td></tr><tr><td>Molitor et al. 2020</td><td>Click decision</td><td>Focal app users</td><td>Actual distance</td><td>Not applicable</td><td>Focal local deal app</td></tr></table>

In terms of methodology, we implement a bivariate probit model in a hierarchical Bayes framework to quantify the effects of distance and local competition, along with their interaction on consumer responses to geofencing. We choose a bivariate probit specification because it enables us to jointly model two interdependent consumer decisions (i.e., click and conversion) in a two-stage process. Specifically, a consumer first decides whether to click on an ad impression displayed on her device; after clicking, she then decides whether to take further actions on the advertiser’s landing page. Furthermore, because an advertiser runs multiple geofencing campaigns in the same period of time, we exploit a hierarchical model specification to account for unobserved heterogeneity at the geofence level while controlling for publisher and device characteristics.

To summarize our main results, we find significant impacts of both distance and local competition on geofence advertising. Although the effect of distance, on the one hand, is not significant in the click stage, it is negative and significant in the conversion stage. Local competition, on the other hand, is a significant driver of clicks but has no measurable impact in the conversion stage. Quantitatively, one additional competitor in a consumer vicinity zone lowers the clickthrough rate by 1.03%, whereas the conversion rate decreases by 17.64% when the device is 1 mile farther away from the establishment, on average. Furthermore, we find a significant interactive effect between distance and local competition indicating that a higher level of local competition makes conversion rate more sensitive to distance. We show that these empirical regularities extend to other nationwide advertisers, including another dining chain, a general retailer, and a pharmacy.

We conduct a series of additional analyses for a more nuanced understanding of the role of distance and local competition. We show that the negative impact of distance on conversion is more salient in urban areas (compared with rural areas) and under bad weather conditions (e.g., raining or snowing), likely because of differences in transportation costs between the settings. We also investigate how product differentiation moderates the effect of competition. Different price ranges, cuisine types, and am biance experiences alleviate the negative impact in the click stage. Finally, we explore temporal effects and show that the impact of local competition is relatively stronger during office working hours and weekdays, perhaps because of the relatively higher opportunity cost of time during those periods.

Our research makes a number of contributions. First, we examine the role of local competition—an important yet underexplored influencer in the context of mobile advertising. Unlike prior location-based advertising research that focuses on the micro competition between two rival theaters (Fong et al. 2015, Dubé et al. 2017), we consider a measure of local competition at a more macro level—the number of alternatives near a consumer’s vicinity. We contribute to the literature by showing that local competition has not only a negative impact on consumer click responses, but also a moderating effect on distance. Second, we explicitly model consumer response in a two-stage process. This modeling effort allows us to discern the dissimilar effects of distance and local competition in the two yet interdependent (i.e., click and conversion) decisions along the customer journey. We extend the literature by demonstrating that the effects of distance and local competition manifest in different stages down the purchase funnel (Howard and Sheth 1969). Third, to the best of our knowledge, this research is the first attempt to empirically investigate geofencing using large-scale, nationwide campaigns. The data richness and broad empirical setting speak to the generalizability of our findings; the fine-grained data further enable us to generate deeper insights into locationbased advertising by exploring various contextual factors, such as location, time, and publisher type.

Our findings also lead to actionable recommendations for practitioners. Local competition in the consumer’s vicinity is critical while consistently neglected in the current practice of geofence advertising.<sup>2</sup> We highlight that distance and local competition should be taken into account in geofencing strategies, given their significant impact on consumer choices demonstrated in this research. It is worth noting that local competition should not be seen as an environmental characteristic of geofences; in fact, local competition is specific to each vicinity zone, varying with consumer locations. To improve geofencing performance, advertisers should not broadcast ads in geofences predefined with arbitrary radii; instead, they should decompose geofences and preferentially target consumers in less-competitive nano-zones. Advertisers may unlock the full potential of geofencing by proactively monitoring consumer locations and effectively delivering ads wherever they have fewer alternatives nearby. As real-time analytics capabilities improve, we envision a scenario where advertising strategies would account for contextual factors like device-level distance and local competition. Given pay per impression, our findings can help optimize the return on advertising spend from geofencing campaigns. In addition, the findings can guide advertisers to effectively use geofencing to promote consumer awareness of new establishment locations and products.

The rest of this paper is organized as follows. In Section 2, we review related literature in locationbased advertising and highlight the key differentiators of our work from prior research. Section 3 introduces the research context and our conceptual framework. Section 4 describes the data, and Section 5 specifies the empirical model. The results and additional analyses are presented in Sections 6 and 7. Section 8 concludes and provides directions for further research.

## 2. Literature Review and Research Framework

We start by reviewing relevant work on locationbased advertising in the literature of information systems and marketing. Then, we discuss the studies that examine the impacts of distance and local competition in LBA and differentiate our work from them.

## 2.1. Location-Based Advertising

The key to the success of mobile marketing is its ability to leverage both content and context, that is, targeting users at the right place and the right time with the right content (Kenny and Marshall 2000). Context can include factors such as geographical proximity, competitive landscape, medium types, surrounding environment, and consumer segments. Prior work has examined the role of various contextual factors in LBA performance, mainly using empirical approaches, as summarized in Table 1. For example, Luo et al. (2014) study mobile short message service (SMS) targeting in a field experiment incorporating both temporal effect (i.e., coupon expiration) and geographical effect (i.e., proximal locations). Andrews et al. (2016) further demonstrate that the performance of mobile targeting also depends on the physical environments of consumers, such as crowdedness. Moreover, Fong et al. (2015) investigate geo-conquesting, whereby a focal advertiser pushes ads to consumers near a specific competing establishment. Using a randomized field experiment, they find that offering deeper discounts in the competitor’s proximity leads to increased sales, whereas doing the same in the focal advertiser’s vicinity reduces the returns because of profit cannibalization. Fang et al. (2015) discover that a theater can further boost its sales by running geofencing with price promotions. In line with this finding, a discount effect also exists in local search advertising after controlling for the effects of ranking and distance (Molitor et al. 2020).

This study distinguishes itself from the related literature in the following three aspects. First, complementary to the previously mentioned research, we focus on two critical yet underexamined contextual factors in location-based advertising: distance and local competition. A novel contribution of our work is that we consider the intensity of local competition in the consumer vicinity zones while controlling for the actual distance between consumers and the focal establishment. The impact of local competition, to the best of our knowledge, has not yet been systemically studied in the LBA literature. Second, much of the prior research specifically looks into the effects of promotions delivered via a particular medium, such as SMS (Fang et al. 2015) or a specific app (Ghose et al. 2019b). We examine consumer response to locationbased ads in a more general setting—a vast network of mobile apps for both Android and iOS platforms. Third, in contrast to prior work that observes responses from consumers near one single establishment (Luo et al. 2014, Fang et al. 2015) or two competing stores (Fong et al. 2015, Dubé et al. 2017), we are able to obtain large-scale observations across multiple cities in the United States.

Next, we review literature that has examined distance and competition in the context of LBA, respectively, and differentiate our study from others.

## 2.2. Distance in Location-Based Advertising

It is well-known that transportation cost is a critical component of the direct costs of shopping behavior and influences where consumers choose to purchase products or services (Bell et al. 1998). Accordingly, distance naturally serves as one of the key determinants of location-based strategies (Curry 1978, Stahl 1982) and consumer utility (Hanson 1980, Mulligan 1983). With the recent growth of O2O commerce, there has been a renewed interest in the role of distance. For example, Forman et al. (2009) show that consumers are more likely to purchase books at physical stores than online retailers if the stores are geographically closer. Since then, a growing literature has studied the impacts of distance in mobile settings It is expected that the role of spatial proximity is more salient on mobile devices relative to desktop computers. Ghose et al. (2013) approximate the distance between consumers and stores using home addresses and find that consumers are more likely to click on microblogs by proximal advertisers on mobile devices as compared with personal computers.

With the growing adoption of location-based advertising, more attention has been directed to the effectiveness of proximity targeting. Fang et al. (2015) show that consumers who are within 500 m of a selected theater are more responsive to marketing messages than those who are not in the same geofencing range. In a similar setting, Luo et al. (2014) further classify consumers into near-, medium-, and fardistance groups, depending on how far they are from the focal theater. They conclude that neardistance mobile promotions result in a higher likelihood of redemption compared with far-distance mobile promotions. Along these lines, Fong et al. (2015) use 200 m for geofence configurations and construct the focal location (i.e., geofence centered at the focal theater) and the benchmark location (i.e., geofence centered at a location 2 km away from the focal theater). They find that promotions are more effective in the focal location than in the benchmark location. It should be clear that much of prior research operationalizes distance in discretized ranges (Luo et al. 2014). In contrast, we are able to account for the actual distance between an establishment and a consumer location, based on the precise latitude/longitude coordinates of each. To the best of our knowledge, this study is one of the first to quantify the economic impact of actual distances in location-based advertising.<sup>3</sup> We contribute to the literature by demonstrating the role of distance in conjunction with the impact of local competition, as we introduce next.

## 2.3. Local Competition in Location-Based Advertising

Competition plays a central role in economics and related domains (Tirole 1989) and has been studied in a variety of applications, such as product diversity (Dixit and Stiglitz 1977), network externality (Katz and Shapiro 1985), and promotions (Shaffer and Zhang 1995). More recently, scholars in information systems also extend this vast literature by examining the role of competition in, for example, online research intermedi aries (Weber and Zheng 2007), gamification (Santhanam et al. 2016), and mobile app demand (Ghose and Han 2014), among others. In the context of location-based advertising, existing work mainly studies price competition, a notion that is closer to Shaffer and Zhang (1995). Fong et al. (2015) study the effectiveness of geo-conquesting, whereby an advertiser attempts to steal business by pushing coupons to consumers near its competitor. They show that the focal theater can increase sales by offering deep mobile promotions in the proximity of the competing theater. In a similar head-to-head setting, Dubé et al. (2017) extend the findings by estimating the change in demand for movie tickets.<sup>4</sup>

The extant research primarily focuses on head-tohead or micro competition between two competing stores, ignoring the presence of nearby establishments that provide similar products or services. A potential limitation of this approach could be the negligence of other alternatives surrounding consumers. The marketing literature documents that when consumers are aware of an advertiser, the likelihood of choosing the advertiser would significantly increase (Andrews and Srinivasan 1995). As a result, one might expect the number of available alternatives to affect consumer choice. Following this rationale, we use our location data and measure local competition as the number of similar establishments in the vicinity of each individual consumer. Thus, local competition is a key contextual variable that varies with the location of every individual consumer, which has been largely ignored in prior research. It is worth highlighting that we can identify the effect of local competition by using the large variation in the number of alternatives across user vicinity zones and across campaigns.

Prior literature consistently suggests that distance and local competition both have a negative impact on location-based advertising. However, it remains unclear (1) whether these two contextual factors play different roles and (2) how the interact with each other, in a sequence of click and conversion decisions. Our research fills this research gap by developing a two-stage model of consumer decision making that emphasizes the roles of distance and local competition in the context of mobile geofencing. Before we further describe our empirical framework, it is useful to describe the industry context and geofencing phenomena that underlie our empirical analysis.

## 3. Research Context and Conceptual Framework

## 3.1. Research Context

The mobile advertising ecosystem consists of both supply-side players, including publishers (e.g., mobile apps) and exchanges, and demand-side players, including advertisers and marketing agencies. On the supply side, publishers provide mobile screen real estate for banner ad insertions. Exchanges consolidate ad slots supplied by multiple publishers and sell them in large batches. On the demand side, advertisers (e.g., restaurant chains) typically work with marketing agencies who acquire ad slot inventory on their behalf. In the context of geofence advertising, ads are inserted into apps on mobile devices based on geotargeting. Specifically, a given advertiser’s ad impression will be placed on a given user’s mobile device only when the following two conditions are both satisfied: (1) the user device is inside the geofence zone of a physical establishment and (2) an impression opportunity arises for the given device and app.

Let us unpack the series of events that lead to the placement of an ad impression in geofence advertising. Consider an advertiser running geofence advertising and a consumer using an app on her smart device with geolocation services enabled. The app provides an opportunity for ad insertions on the screen of the consumer’s device. Suppose that the advertiser sets a 5-mile geofence around a physical establishment. When a consumer steps into the geofence zone, an ad would be displayed only when the advertiser obtains the insertion opportunity. Given this unique context, the distance between the consumer and the advertiser for each impression would not be exactly 5 miles; instead, it varies depending on the timing of ad opportunities and consumer trajectory. As a result, this contextual nature generates a substantial variation in the distance measure, especially when we pool observations across hundreds of geofences nationwide.

Figure 1 illustrates this scenario. Consumer A is out of the geofence zone, so he will not receive a geofence ad. There is an ad opportunity on Consumer B’s device because she has a targeted app open, but she never sees an impression because she is also out of the geofence. Although Consumer C is located in the geofence zone, she is still not targeted because the screen is locked. Only Consumer D provides a viable ad insertion opportunity because her case meets the two criteria, that is, being located inside the geofence and having a targeted app open. This process provides sufficient variation in consumer-establishment distance, allowing us to quantify the effect of distance on advertising performance.

Figure 2 illustrates an ad impression from an advertiser displayed in an app and the corresponding landing page. The ad copy is basically a brand image, and when the ad is displayed, the user must first decide whether to click on it or not. If she clicks, the screen will be redirected to the advertiser’s landing page where the user can browse detailed information about the advertiser, products, and value propositions. At this point, the consumer needs to decide whether to convert or not. For the campaigns in our data set, the landing pages are not customized to users and do not provide real-time location-related information. Given the current practice of geofencing, it is difficult to observe actual conversions (i.e., actually purchasing goods or services in response to an ad). Nevertheless, we are able to observe in our data whether the user takes any follow-up actions on the landing page, including clicking on the “Place Order” button, looking up for the location, or clicking on a phone link. These follow-up actions are likely driven by a propensity to purchase and are highly correlated with actual purchases. Because all the advertisers included in our analysis are well-known nationwide brands, those follow-up actions are likely driven by a high propensity to purchase and thus are highly correlated with actual purchases. In prac tice, those secondary actions in the LBA industry are widely adopted by practitioners as proxies for conversions when actual purchase data are not available (Desaulniers 2016).

Figure 1. (Color online) Mobile Geofence Advertising  
![](/api/attachments/XNXKEBW2/fulltext/images/3c434317db3273c2aafbb214a03adecb15ec40401a7cb9dcaf5b72930c621224.jpg)

Figure 2. (Color online) Illustrations of Geofencing Ads in an App and the Landing Page  
![](/api/attachments/XNXKEBW2/fulltext/images/3f58aee9603bcfbe9e8de7386d8081a8ed8341ca260be05866b541d4ef5aa28b.jpg)

## 3.2. Conversion Funnel Framework

Given the research context described previously, we now describe the conceptual framework that we deploy to study the consumer decision-making process in the context of mobile geofencing (Figure 3). In our empirical setting, the observed outcome variables are click and conversion choices at the impression level. As depicted in Figure 3, we examine the impact of distance, competition, and their interaction on click and conversion performance while controlling for other contextual characteristics at the device, publisher and geofence levels.

We draw on the concept of the purchase funnel that has been at the center of the marketing literature for decades (Howard and Sheth 1969). The purchase funnel, or more aptly the conversion funnel in our study, holds that consumers move toward a purchase in a series of phases, beginning with awareness to evaluation, and, ultimately, to conversion (Court et al. 2009; Srinivasan et al. 2010, 2016). This literature generally suggests that consumers will undergo two distinct phases on the rise of a purchase desire. In the awareness phase, a consumer becomes more aware of a brand when she is exposed to a marketing message placed by an advertiser. Subsequently, if the consumer is interested in the brand, she would add it to her consideration set and transition to the next phase. In the evaluation phase, the consumer assesses the relevant attributes of the product advertised and compares it against other alternatives in the set through an elimination process. Finally, the consumer would move to the conversion phase if the advertising product stands out from the set based on relevant attributes. This decision-making process is also described in the similar AIDA framework (attention, interest, desire, and action) favored by some in the marketing literature (Kotler and Armstrong 2011).

Figure 3. (Color online) Conceptual Framework  
![](/api/attachments/XNXKEBW2/fulltext/images/5c6d4e8147ed0a4c9a3ca3cee60ac8b79e70c5f85519e8ad3ffef5cee912aa66.jpg)

Figure 4. (Color online) Local Competition in the Consumer’s Vicinity  
![](/api/attachments/XNXKEBW2/fulltext/images/afcb6761ba38eeeee15a5dca86a5f20b5d5b641770b3963df58aac94e7960f04.jpg)

Grounded in information processing theory (Bettman 1979), the purchase funnel framework states that consumers perform distinct tasks by using different sets of information as they move down the funnel. This suggests that the role of the same information is likely to vary across different phases of the funnel. Consider a typical use case in our context: a consumer is located near an establishment of a focal advertiser and possesses some private information about the surrounding area. This private information helps the consumer infer some, albeit imperfect, knowledge about nearby businesses and accordingly form her consideration set. In the awareness phase, the consumer becomes more aware of the brand when she sees an ad impression on her mobile device. The ad copy in our case is basically a brand image, as illustrated in Figure 2. At this point (i.e., the click stage), the consumer faces a decision of whether to further engage with the advertiser, and a click action indicates a desire to include the brand in her consideration set. Prior research shows that the marginal utility gain of considering an extra option diminishes when the size of an existing consideration set is large (Ratchford 1980, Roberts and Lattin 1991). This suggests that the propensity to click on the ad should be lower in the presence of stronger local competition—embodied by a larger number of nearby competing alternatives in our conceptual framing. Therefore, we anticipate that local competition is likely to be diagnostic with respect to the click decision of a consumer. Because the main objective in the awareness phase is to form a consideration set for later evaluation, detailed attributes of an advertiser (e.g., distance in our conceptual framing) may play a little role at the click stage.

On clicking on an ad, the consumer transitions to the evaluation phase of the conversion funnel, which involves gaining detailed information about the alternatives in the consideration set and weighting the utility gain based on the relevant attributes. Such a process has been well recognized by research grounded in information processing theories (Payne 1976, Bettman 1979, Lussier and Olshavsky 1979, Gensch 1987). The consensus result states that when a consumer is faced with multiple alternatives, the optimal heuristic (with respect to economizing on cognitive effort) is to first eliminate alternatives, and then focus on the attributes of the remaining in order to make a choice. The elimination of alternatives is usually done using the attributes that are most relevant in a given circumstance. Because mobile geofencing embodies an O2O setting, it is reasonable to presume that offline transportation cost is likely to be a significant factor that affects consumer conversion decision. Based on the previous theoretical guidance, we anticipate that the negative effect of distance becomes more influential at the conversion stage. Accordingly, we conjecture that distance is likely to be diagnostic with respect to the conversion decision of a consumer. As the abstract information about local competition has already been used in forming the consideration set, it is likely to have no additional impact here.

Although we have discussed the main effects of distance and local competition, it remains unclear how the interaction between the two contextual fac tors affects the performance of geofencing. As discussed earlier, in the awareness phase, a consumer forms her consideration set using abstract information about the brand (i.e., advertiser), whereas in the evaluation phase, the same consumer assesses each alternative based on detailed attributes specific to the product (i.e., establishment). Thus, we conjecture that distance should have no moderating effect on local competition at the click stage. In contrast, as a consumer moves further down the funnel, she tends to be more deliberate in decision making and hence pays closer attention to contextual nuances. As a result, when a consumer has a larger consideration set, she may become even more fastidious in evaluating the attributes of each alternative. In our setting, a consumer may perceive traveling a certain distance as costlier when there are a larger number of alternatives available in her vicinity (conceptualized as stronger local competition in this study), ceteris paribus. Bearing these arguments in mind, we expect that the level of local competition is likely to intensify the negative effect of distance in the conversion stage.

## 4. Data and Descriptive Statistics

The data used for our research are provided by one of the leading marketing agencies specialized in locationbased advertising in the United States.<sup>5</sup> It runs locationbased campaigns on behalf of hundreds of advertisers, including nationwide restaurant chains, retailers, pharmacies, gas stations, and automobile dealers, among others. The data that we obtained from the agency cover more than a million impressions during the month of March 2017. It is important to point out that the advertising campaigns included in our data set correspond to pure geofence targeting and do not include campaigns using other types of targeting based on demographics or user trajectory (e.g., geo-cookie targeting). This allows us to focus on geofence advertising performance, without other confounding targeting activities.

Our data set captures impressions at the geofencedevice-app level (i.e., an impression is placed in an app banner on a user device, located within a particular geofence). Each observation in our data set contains various characteristics of the publisher, geofence, and user device. Publisher attributes include the type of app<sup>6</sup> (e.g., entertainment, social networking, gaming) and impression size in pixels. Geofence details cover the identity of advertiser and the latitude/ longitude coordinates of the center of the geofence (i.e., establishment location). User device characteristics consist of latitude/longitude coordinates, device manufacturer, and operating system. We use the Haversine formula<sup>7</sup> to compute the actual distances between devices and establishments.

To characterize the level of local competition in a consumer’s vicinity, we collect supplementary data from Yelp, one of the largest information aggregators for local businesses. Using Yelp Fusion Search API,<sup>8</sup> we search for local businesses providing services similar to our focal consumer within a 5-mile vicinity zone.<sup>9</sup> As illustrated in Figure 4, Consumer D, who receives a geofencing ad from the focal advertiser, has other alternatives in her proximity. Moreover, we use the Google Reverse Geocoding API<sup>10</sup> to translate the latitude/longitude coordinates of the establishment into the corresponding zip code. As control variables, we retrieve median income and population size at the level of ZIP code tabulation area (ZCTA) from American Community Survey data<sup>11</sup> (U.S. Census Bureau 2015). Our analysis focuses on one of the largest restaurant chains in the United States. We chose a nationwide restaurant chain as our focal advertiser for the reasons we discussed in the Introduction.

We initially obtain more than 10 million ad impressions across the United States for the restaurant chain in March 2017. In our data, mobile device locations come from multiple sources, including GPS coordinates, IP addresses, and antenna towers. Because the distance measure is one of the key variables of our research, we restrict our analysis to observations using GPS-based location, allowing us to measure distance in the most precise manner. The heavy computational burden of constructing our other key variable—local competition—necessitates a further reduction in our sample size.<sup>12</sup> Specifically, we use a random sampling procedure to restrict our final data set to roughly 210,000 impressions.<sup>13</sup> Figure 5 shows the geographic heat map of the impressions across the United States, indicating that the states of California Texas, Ohio, and Florida have the highest frequency of data in our data set, each accounting for more than 10% of the data. As the figure depicts, the resulting data shows great coverage across the entire nation. To ensure the resulting data set is not subject to sampling bias, we conduct a series of t-tests on variables against the data acquired from other sources. The results suggest no systematic difference between the two subsamples, suggesting the representativeness of the resulting data.

Figure 5. (Color online) Geographic Heat Map of Geofencing Impressions Across the United States  
![](/api/attachments/XNXKEBW2/fulltext/images/76a412e331d33ed5ed55f60aebfe2279e1a6ee9753797e31dd59af4c598633ec.jpg)

Table 2. Descriptive Statistics

<table><tr><td>Variable</td><td>Mean</td><td>Std. Dev.</td><td>Min</td><td>Max</td></tr><tr><td> $Click_{ij}$ </td><td>0.0136</td><td>0.1158</td><td>0</td><td>1</td></tr><tr><td> $Convert_{ij}$  (conditional on  $Click_{ij} = 1$ )</td><td>0.0251</td><td>0.1601</td><td>0</td><td>1</td></tr><tr><td> $Distance_{ij}$  (in miles)</td><td>2.6817</td><td>2.1081</td><td>0.0059</td><td>5.0000</td></tr><tr><td> $NoOfCompetitors_{ij}$ </td><td>108.09</td><td>124.83</td><td>1</td><td>379</td></tr><tr><td> $MedIncome_{i}$ </td><td>55,213</td><td>28,991</td><td>32,257</td><td>177,998</td></tr><tr><td> $Population_{i}$ </td><td>41,541</td><td>18,434</td><td>11,382</td><td>93,997</td></tr><tr><td> $iOS_{ij}$ </td><td>0.1824</td><td>0.3850</td><td>0</td><td>1</td></tr><tr><td> $LargeImp_{ij}$ </td><td>0.2166</td><td>0.4123</td><td>0</td><td>1</td></tr><tr><td> $CatEnt_{ij}$ </td><td>0.3982</td><td>0.4890</td><td>0</td><td>1</td></tr><tr><td> $CatSocial_{ij}$ </td><td>0.1054</td><td>0.3078</td><td>0</td><td>1</td></tr><tr><td> $CatGame_{ij}$ </td><td>0.3099</td><td>0.4627</td><td>0</td><td>1</td></tr><tr><td>N</td><td colspan="4">230,217</td></tr></table>

Note. The data are at the geofence-impression level, where the subscript i refers to geofence and j identifies impression.

## 4.1. Descriptive Statistics

Descriptive statistics for the key variables are reported in Table 2. The two dependent variables, $C l i c k _ { i j }$ and $C o n v e r t _ { i j }$ (both binary variables), refer to the click and conversion decisions on Impression j in Geofence i. Click has a mean of 0.0136, indicating that the overall click-through rate is 1.36% across all impressions. Conditional on a click $( \mathrm { i . e . , } C l i c k _ { i j } = 1 )$ , the conversion rate is 2.51%. Distance<sub>ij</sub> denotes the spatial distance between the user device and restaurant. The average distance is 2.68 miles, and its range is from 0.0059 to 5 miles across geofences. For the local competition measure, around 108 rival restaurants, on average, are located in the focal consumer vicinity zone.

MedIncome and Population serve as the extra controls for geofence zones at ZCTA level. In the data, the median household income and population size across geofences are around \$55,000 and 41,000 people, respectively. $i O S _ { i j }$ is a binary indicator and takes a value of 1 for an iOS device, and 0 otherwise. About 18.2% of the devices are iOS devices. As to publisher attributes, $L a r g e I m p _ { i j }$ is constructed as a dummy variable to indicate the size of impressions. In the data, the size is either 320 × 50 or 300 × 250 pixels, and the latter ones are defined as large impressions $( \mathrm { i . e . , ~ } L a r g e I m p _ { i j } = 1 ) ;$ 21.8% of impressions have large-image ads. To further distinguish types of apps, we categorize apps into four categories, including entertainment (e.g., music and movies), social networking, gaming, and others (e.g., utility and personal finance). These categories account for 39.8%, 10.6%, 31.0%, and 18.7% of the total observations, respectively.

We plot the relationships between the key variables of interest in Figure 6. On the one hand, Figure 6(a)

shows that there is no clear pattern between click performance and distance. On the other hand, we see that the impact of distance on conversion performance appears to be negative in Figure 6(b). Additionally, Figure 6(c) depicts a negative correlation between click-through rate and local competition, as represented by the number of other restaurants in the geofence. However, it is not clear whether local competition also lowers the propensity of conversion in Figure 6(d). A better understanding of the above relationships is the focus of our empirical analysis, as we discuss next.

## 5. Empirical Model and Estimation

We develop a hierarchical Bayes model to examine consumer responses in the context of mobile geofencing campaigns. Our modeling framework is that, on seeing an impression, a consumer first decides whether to click on the ad; if a click occurs, she then decides whether to convert. In the click stage, the observed consumer response $( \mathrm { i . e . , }$ , whether to click) on Impression j associated with the Geofence i is binary and can be coded as follows:

$$
\Upsilon_ {i j} ^ {c l c i k} = \left\{ \begin{array}{l l} 1, & \text { if   click; } \\ 0, & \text { otherwise. } \end{array} \right.
$$

Similarly, we use the following coding rule for the observed outcome (i.e., whether to convert) in the conversion stage:

$$
\Upsilon_ {i j} ^ {\text { convert }} = \left\{ \begin{array}{l l} 1, & \text { if   convert; } \\ 0, & \text { otherwise. } \end{array} \right.
$$

Figure 6. (Color online) Correlations Between Key Variables  
![](/api/attachments/XNXKEBW2/fulltext/images/ccefd593a78fca1300568becb55a332b6ff9c5bbc84d506abb99abe593c76df2.jpg)

(b)  
![](/api/attachments/XNXKEBW2/fulltext/images/736e59e746eedadeb78e6eddae647f916b11ae84173ae287768c9ce51921b85c.jpg)

Distance vs. Click-through Rate  
(c)  
![](/api/attachments/XNXKEBW2/fulltext/images/c255e82e0bab7868bcbf358cc8efa35e5ce4462a5f2eda14036be05155b37832.jpg)  
Competition vs. Click-through Rate

Distance vs. Conversion Rate  
(d)  
![](/api/attachments/XNXKEBW2/fulltext/images/b7af0a4dcdfd6644827d30c6487f337a3f38c2882b72be7ea0d0badef49107a4.jpg)  
Competition vs. Conversion Rate  
Notes. (a) Distance versus click-through rate. (b) Distance versus conversion rate. (c) Competition versus click-through rate. (d) Competition versus conversion rate.

## 5.1. Click Decision

Following random-utility theory, we specify consumer utility of clicking on Impression j associated with Geofence i as

$$
\begin{array}{r l} & U _ {i j} ^ {c l i c k} = U _ {i j} ^ {c l i c k ^ {*}} + \varepsilon_ {i j} \\ & \quad = \beta_ {i 0} + \beta_ {i 1} \mathrm{ln} (D i s t a n c e _ {i j}) + \beta_ {i 2} \mathrm{ln} (N u m C o m p e t i t o r s _ {i j}) \\ & \qquad + \beta_ {i 3} \mathrm{ln} (D i s t a n c e _ {i j}) ^ {*} \mathrm{ln} (N u m C o m p e t i t o r s _ {i j}) \\ & \qquad + \beta_ {4} \mathrm{ln} (M e d I n c o m e _ {i}) + \beta_ {5} \mathrm{ln} (P o p u l a t i o n _ {i}) \\ & \qquad + \beta_ {6} i O S _ {i j} + \beta_ {7} L a r g e I m p _ {i j} + \beta_ {8} C a t E n t _ {i j} \\ & \qquad + \beta_ {9} C a t S o c i a l _ {i j} + \beta_ {1 0} C a t G a m e _ {i j} + \varepsilon_ {i j}. \end{array}
$$

The two key independent variables, Distance and NoOfCompetitors , respectively, capture the distance (between the mobile device and the advertiser’s establishment) and the local competition (measured by the number of competitors within a five-mile consumer vicinity zone). We leverage the nature of the hierarchical model to quantify the effects of our interest at a more granular level for better control. This modeling approach accounts for unobserved heterogeneity across geofences. $\beta _ { i 0 }$ is the geofence-specific intercept which allows for variation in the baseline utility of clicks across geofences. $\beta _ { i 1 } , \beta _ { i 2 } ,$ , and $\beta _ { i 3 }$ are geofence-specific slope coefficients, which together model the heterogeneous effects of the key variables on the utility derived from clicking on an ad. We also control for characteristics at different levels such as the median income and population, operating systems of the devices, size of impressions, and publisher app categories. $\varepsilon _ { i j }$ is an idiosyncratic error term.

Assuming that $\varepsilon _ { i j }$ follows a standard normal distri bution, we have a standard binary probit specification:

$$
\operatorname * {P r} \left(\Upsilon_ {i j} ^ {\text {click}} = 1\right) = \operatorname * {P r} \left(U _ {i j} ^ {\text {click} ^ {*}} + \varepsilon_ {i j} > 0\right) = \Phi \left(U _ {i j} ^ {\text {click} ^ {*}}\right),
$$

where Φ denotes the cumulative density function (CDF) of a standard normal distribution. A consumer would click on the ad $( \mathrm { i . e . , ~ } Y _ { i j } ^ { c l i c k } = 1 )$ , if the latent utility of clicking $U _ { i j } ^ { c l i c k } > 0 ;$ the consumer would not click otherwise.

## 5.2. Conversion Decision

If a click occurs in the first stage, the consumer would be redirected to the advertiser’s landing page where she decides whether to take further actions. We specify the following utility function for consumers’ conversion decision, conditional on a click:

$$
\begin{array}{r l} & U _ {i j} ^ {c o n v e r t} = U _ {i j} ^ {c o n v e r t ^ {*}} + \zeta_ {i j} \\ & \quad = \gamma_ {i 0} + \gamma_ {i 1} \mathrm{ln} (D i s t a n c e _ {i j}) \\ & \qquad + \gamma_ {i 2} \mathrm{ln} (N u m C o m p e t i t o r s _ {i j}) \\ & \qquad + \gamma_ {i 3} \mathrm{ln} (D i s t a n c e _ {i j}) * \mathrm{ln} (N u m C o m p e t i t o r s _ {i j}) \\ & \qquad + \gamma_ {4} \mathrm{ln} (M e d I n c o m e _ {i}) + \gamma_ {5} \mathrm{ln} (P o p u l a t i o n _ {i}) \\ & \qquad + \gamma_ {6} i O S _ {i j} + \zeta_ {i j}. \end{array}
$$

Similarly, geofence-specific intercept coefficient $\gamma _ { i 0 }$ allows for variation in the baseline utility of conversion because of unobserved heterogeneity at the geofence level. $\gamma _ { i 1 } , \ \gamma _ { i 2 } ,$ , and $\gamma _ { i 3 }$ together model the heterogeneous effects of distance, competition, and their interaction term, respectively, on consumer utility from converting. We also add most of the control variables included in the click model. Because consumers in the conversion stage have landed on the advertiser’s landing pages, they are less likely to be affected by publisher characteristics. For this reason, we drop publishers’ app categories from the conversion model so as to achieve identification of our two-equation model.

We assume $\zeta _ { i j }$ follows a standard normal distribution, resulting in the following binary probit model with conditional probability:

$$
\begin{array}{c} \operatorname * {P r} \Big (\mathbf {Y} _ {i j} ^ {\text {convert}} = 1 \mid \mathbf {Y} _ {i j} ^ {\text {click}} = 1 \Big) = \operatorname * {P r} \Big (U _ {i j} ^ {\text {convert} ^ {*}} + \zeta_ {i j} > 0 \Big) \\ = \Phi \Big (U _ {i j} ^ {\text {convert} ^ {*}} \Big). \end{array}
$$

## 5.3. Interdependence between Click and Conversion Decisions

Although we have specified two separate equations for the two consumer choices, the interdependence between the two has not yet been formally discussed. It is reasonable to suspect that some unobserved factors, such as weather, may jointly influence both click and conversion decisions. Ignoring this potential interdependence could bias the estimation results. Accordingly, we flexibly allow the error terms in the click and conversion models to be correlated by assuming $\big ( \begin{array} { l } { \varepsilon _ { i j } } \\ { \zeta _ { i j } } \end{array} \big ) = \mathrm { B V N } \big ( \big ( \begin{array} { l } { 0 } \\ { 0 } \end{array} \big ) , \big ( \begin{array} { l l } { 1 } & { \rho } \\ { \rho } & { 1 } \end{array} \big ) \big )$ , where BVN denotes a bivariate normal distribution, and $\rho$ captures the correlation between the two sets of error terms. The standard deviations of $\varepsilon _ { i j }$ and $\zeta _ { i j }$ are fixed at 1 to obtain binary probit specifications, and the parameter $\rho$ is the correlation coefficient to be estimated.

We next specify the likelihood of observing the data, given the data generating process. Figure 7 shows three scenarios of consumer response in our two-stage model. Based on the covariance structure we have specified for the error terms, the joint probability of observing each of three possible events can be expressed as

Figure 7. (Color online) Consumer Click and Conversion Decisions  
![](/api/attachments/XNXKEBW2/fulltext/images/9fe434188cabe5936e729ee6e3d672e95ca0a6a795225ca445594419cd29fb9a.jpg)

1. Not clicking: $\mathrm { P r } ( Y _ { i j } ^ { C l i c k } = 0 ) = 1 - \Phi ( U _ { i j } ^ { C l i c k ^ { * } } ) ;$

2. Clicking, but not converting: $\mathrm { P r } ( Y _ { i j } ^ { C l i c k } = 1 )$ $\begin{array} { r } { { \cal Y } _ { i j } ^ { C o n v e r t } = 0 ) = \Phi _ { B V N } ( { \cal U } _ { i j } ^ { C l i c k ^ { * } } , - { \cal U } _ { i j } ^ { C o n v e r t ^ { * } } , \rho ) ; } \end{array}$

3. Clicking and converting: P $\cdot ( Y _ { i j } ^ { \dot { C } l i c k } = 1 , Y _ { i j } ^ { C o n v e r t } =$ $1 ) = \Phi _ { B V N } ^ { \smile } ( U _ { i j } ^ { C l i c k ^ { * } } , U _ { i j } ^ { C o n v e r t ^ { * } } , \rho ) ,$

where $\Phi _ { \mathrm { B V N } }$ denotes the CDF of a bivariate normal distribution. As a result, the joint likelihood of observing consumer click and conversion decisions from the entire data set can be expressed as

$$
\begin{array}{c} L \Big (\boldsymbol {y} _ {i j} ^ {c l i c k}, \boldsymbol {y} _ {i j} ^ {c o n v e r t} \Big) = \prod_ {j \in (\boldsymbol {y} _ {i j} ^ {c l i c k} = 0)} \operatorname * {P r} (\boldsymbol {y} _ {i j} ^ {c l i c k} = 0) ^ {*} \\ \prod_ {j \in (\boldsymbol {y} _ {i j} ^ {c o n v e r s i o n} = 0)} \operatorname * {P r} (\boldsymbol {y} _ {i j} ^ {c l i c k} = 1, \boldsymbol {y} _ {i j} ^ {c o n v e r s i o n} = 0) ^ {*} \\ \prod_ {j \in (\boldsymbol {y} _ {i j} ^ {c o n v e r s i o n} = 1)} \operatorname * {P r} (\boldsymbol {y} _ {i j} ^ {c l i c k} = 1, \boldsymbol {y} _ {i j} ^ {c o n v e r s i o n} = 1). \end{array}
$$

## 5.4. Estimation

Because our model has geofence-specific parameters, traditional estimation methods, such as maximum likelihood estimation, are inadequate because convergence is difficult, if not impossible, to achieve. As a result, we use a hierarchical Bayes approach to estimate the proposed model. Given the nature of parameter hierarchy, the parameters can be divided into two groups (Netzer et al. 2008), with (1) random-effect parameters that vary across geofences (denoted by $\theta _ { i } )$ and (2) fixed parameters that do not vary across geofences (denoted by Ψ). We allow for correlation among geofence-specific parameters by assuming

$$
\boldsymbol {\theta} _ {i} \sim \operatorname{MVN} (\bar {\boldsymbol {\theta}}, \boldsymbol {\Sigma}),
$$

where θ<sup>¯</sup> denotes the mean effects that persist across geofences and Σ denotes the covariance matrix of θ. We use a noninformative prior for the fixed parameter Ψ because researchers do not yet have a good understanding of consumer click and conversion be haviors in the context of geofence advertising.

We develop a Markov chain Monte Carlo (MCMC) procedure to recursively draw parameters from the corresponding full conditional distributions. The procedure has the following four steps:

$$
\begin{array}{c} \theta_ {i} | \Upsilon , \Psi , \rho , \Sigma ; \\ \Sigma | \theta_ {i}; \\ \Psi | \Upsilon , \rho , \theta_ {i}; \\ \rho | \Upsilon , \Psi , \theta_ {i}. \end{array}
$$

Because the conditional posterior distributions do not have a closed form for steps 1, 2, and 4, we adopt the random walk Metropolis-Hastings algorithm to search the parameter space. More specifically, a two-step estimation approach is used to improve the efficiency of the MCMC sampler. In the first step, we run a pilot MCMC for 50,000 iterations, and the first 10,000 draws are discarded as burn-in samples. We calculate posterior means and empirical covariance matrix based on the remaining 40,000 draws. In the second step, we run a separate MCMC using the posterior means calculated in the previous step as the initial values and the empirical covariance matrix as the covariance parameters for the random-walk proposal distribution. We run the MCMC sampler for 50,000 iterations and record only every 10th draw to mitigate the autocorrelation issue, an inevitable consequence of the MCMC simulation (Hoff 2009). The adaptive chain converges immediately and explores the parameter space efficiently. To test convergence, we perform the Gelman and Rubin diagnostic (Gelman and Rubin 1992) by running three parallel chains with different initial values and random seeds. The potential scale reduction factors (PSRFs) across all parameters are smaller than 1.09, much lower than the suggested threshold for the assessment of convergence (i.e., PSRF = 1.2). Draws from three parallel chains are consolidated and serve as the final draws for model results. The effective sample size is at least 600 for each parameter, which is more than sufficient for reliable Bayesian inference.

We also estimate two less-specified models with respect to heterogeneity and compare them against our full model. We specify model 1 as a model with geofencelevel intercept only $( \mathrm { i . e . , } \beta _ { i O }$ and $\gamma _ { i 0 } )$ and model 2 as a homogeneous model without accounting for any heterogeneity. Following Spiegelhalter et al. (2002), we evaluate the performance of the three estimated models based on deviance information criterion (DIC), a metric widely used for Bayesian model selection. From Table 3, we can see that our full model outperforms the two less-specified models, judging by a lower value of DIC. This result suggests that it is desirable to account for unobserved heterogeneity at the geofence level, as we are able to achieve in our hierarchical model.

## 6. Results

Our results for click and conversion responses to geofence advertising are presented in Table 4. In the click stage, the coefficient of distance is not statistically significant. The local competition variable is negative and significant. The coefficient estimate for the distance–competition interaction term suggests that these two factors do not jointly affect click responses. The coefficient of $i O S _ { i j }$ is insignificant, showing no systematic difference in the click performance between iOS and Android devices. ln MedIncome is insignificant, whereas ln Population is positive and significant. Considering the demographics of geofence zones, the click performance is better in more populated areas but not different across neighborhoods with different income levels. Large-size impressions are clicked less often by consumers. The coefficients for app categories suggest that entertainment and gaming apps garner a relatively higher click-through rate compared with social media or other apps. This could be driven by a natural match between dining businesses and consumer segments, such as millennials, interested in entertainment and gaming.

In the conversion stage, distance turns out to be significant. The negative sign shows that consumers are sensitive to distance when deciding whether convert after clicking an ad. Thus, distance matters only in the second stage but not in the first one, consistent with the research findings (Luo et al. 2014, Molitor et al. 2020), as well as the anecdotal evidence for the restaurant industry (YP Marketing Solutions 2012) and our theoretical arguments presented in Section 3.2. It is worth noting that competition is insignificant in the conversion stage. Moreover, the interaction between distance and the number of competitors is significant at the 0.01 level, showing that these two factors amplify each other. In other words, a consumer is less interested in the advertiser’s restaurant when it is farther from her and when there are more alternatives nearby. Regarding other control variables, consumers using Apple iOS devices appear to have lower propensity to convert, implying that the advertiser is not attractive to this specific consumer segment. Other demographics have no effect on the conversion rate. Finally, the posterior mean of $\rho$ falls in a reasonable range, suggesting there is a moderate level of interdependence between the two consumer decisions (Ho et al. 2017). The estimated coefficient is significant at 1% level, which validates the use of a two-stage specification like ours.

Table 3. Model Comparisons

<table><tr><td>Specifications</td><td>Full model</td><td>Model 1</td><td>Model 2</td></tr><tr><td>Geofence-specific intercept</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>Geofence-specific slopes</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>Log-likelihood</td><td>-30,716.3</td><td>-32,658.2</td><td>-37,195.8</td></tr><tr><td>Deviance Information Criterion (DIC)</td><td>63,454.3</td><td>66,512.1</td><td>74,481.4</td></tr><tr><td>ΔDIC with respect to full model</td><td></td><td>3,057.8</td><td>11,027.7</td></tr></table>

Notes. The full model allows for parameter heterogeneity at the geofence level. Model 1 has geofencelevel intercepts only, whereas Model 2 has all the variables but no heterogeneity.

Table 4. Effects of Distance and Local Competition in Geofencing

<table><tr><td></td><td>Click response</td><td>Conversion response</td></tr><tr><td>Intercept</td><td>-0.362***(0.124)</td><td>-0.988***(0.250)</td></tr><tr><td> $In(Distance_{ij})$ </td><td>-0.081(0.319)</td><td>-0.126***(0.036)</td></tr><tr><td> $In(NumCompetitors_{ij})$ </td><td>-0.518***(0.207)</td><td>0.017(0.012)</td></tr><tr><td> $In(Distance_{ij}) * In(NumCompetitors_{ij})$ </td><td>0.085(0.176)</td><td>-0.028***(0.005)</td></tr><tr><td> $In(MedIncome_{i})$ </td><td>-0.025(0.028)</td><td>-0.035(0.036)</td></tr><tr><td> $In(Population_{i})$ </td><td>0.037***(0.016)</td><td>-0.036(0.024)</td></tr><tr><td> $iOS_{ij}$ </td><td>0.135(0.107)</td><td>-0.233***(0.054)</td></tr><tr><td> $LargeImp_{ij}$ </td><td>-0.029(0.034)</td><td></td></tr><tr><td> $CatEnt_{ij}$ </td><td>0.082***(0.011)</td><td></td></tr><tr><td> $CatSocial_{ij}$ </td><td>-0.015(0.019)</td><td></td></tr><tr><td> $CatGame_{ij}$ </td><td>0.243***(0.066)</td><td></td></tr><tr><td>ρ</td><td></td><td>0.176***(0.067)</td></tr><tr><td>N</td><td></td><td>230,217</td></tr></table>

Note. Results from the bivariate probit model of Section 4.  
\*\*\*Significance at 1%.

Using the coefficient estimates in Table 4, we can quantify the economic significance of the variables of interest. Because interpreting the coefficients in a probit model is not as straightforward as in logit models, we have to derive the marginal effect of each variable of interest while fixing other variables at their mean levels. Quantitatively, having one more competitor in the consumer’s vicinity decreases clickthrough rate by a margin of 1.03%, ceteris paribus. On the contrary, distance has a negative impact on conversion rate, whereas competition does not. The estimation results indicate that the conversion rate would drop by a large margin of 17.64% if the consumer is 1 mile farther away from the focal advertiser establishment, all else equal. Entertainment and gaming apps are associated with a higher click-through rate, with margins of 23.47% and 85.23%, respectively. Finally, iOS consumers are less likely to take conversion actions than other device users by a margin of 25.49%.

Table 5. Correlation Matrix of Geofence-Specific Parameters

<table><tr><td></td><td> $\beta_{i0}$ </td><td> $\beta_{i1}$ </td><td> $\beta_{i2}$ </td><td> $\beta_{i3}$ </td></tr><tr><td> $\beta_{i0}$ </td><td>1</td><td></td><td></td><td></td></tr><tr><td> $\beta_{i1}$ </td><td>-0.106***</td><td>1</td><td></td><td></td></tr><tr><td> $\beta_{i2}$ </td><td>-0.080**</td><td>0.149***</td><td>1</td><td></td></tr><tr><td> $\beta_{i3}$ </td><td>0.025</td><td>-0.054</td><td>0.017</td><td>1</td></tr></table>

b. Correlations among the parameters of conversion response

<table><tr><td></td><td> $\gamma_{i0}$ </td><td> $\gamma_{i1}$ </td><td> $\gamma_{i2}$ </td><td> $\gamma_{i3}$ </td></tr><tr><td> $\gamma_{i0}$ </td><td>1</td><td></td><td></td><td></td></tr><tr><td> $\gamma_{i1}$ </td><td>-0.084</td><td>1</td><td></td><td></td></tr><tr><td> $\gamma_{i2}$ </td><td>-0.105**</td><td>0.120***</td><td>1</td><td></td></tr><tr><td> $\gamma_{i3}$ </td><td>-0.018</td><td>0.024</td><td>-0.026</td><td>1</td></tr></table>

\*\*\* and \*\* indicate 1% and 5% levels of significance, respectively.

An advantage of Bayesian inference is the ability to perform posterior analyses based on the draws obtained from our MCMC procedure. A closer examination of the microlevel parameters leads to some interesting findings. For the ease of presentation and interpretation, we separately report the correlation matrix from the two models. As shown in Panel A of Table 5, the correlations between the baseline utility from clicking and the effects of distance and competition are negative. This result suggests that, after controlling for the income and population of a given zone, consumers (aggregated at the geofence level) who are more likely to click on ads tend to be less sensitive to distance and competition. Albeit at different significance levels, a similar pattern is observed in the conversion stage (see Panel B). Moreover, we calculate the correlation between the baseline utility of clicking and converting to be corr $( \beta _ { 0 i } , \gamma _ { 0 i } ) { = } 0 . 1 6 3$ , significant at 0.01 level. The positive correlation indicates that, holding everything else equal, geofences that deliver good clickthrough performance tend to have higher conversion rates as well. This is empirically observed perhaps because consumers who reside in different geofence zones may demonstrate heterogeneous attitudes toward mobile ads for different reasons, such as distinct dining habits, dissimilar levels of proficiency in mobile technology, and the like.

We conduct a series of robustness checks to assure the stability and generalizability of our results. We look at three other nationwide advertisers, including a quick-service restaurant, a general retailer, and a pharmacy. The results are reported in Table 6. Although the magnitudes of coefficient estimates vary moderately across advertisers, the effects of distance and local competition and the moderation between the two continue to hold. These qualitatively consistent results help demonstrate the generalizability of our main findings. Also, we consider various consumer vicinity zones and an alternative measure of local competition based on the advertiser’s vicinity to demonstrate the robustness of our findings.<sup>14</sup>

## 7. Additional Analyses and Moderating Effects

In this section, we further explore other factors that could moderate the effects that we have identified. For distance, the comparison between urban and rural geofences is considered, along with weather

Table 6. Robustness Checks

<table><tr><td rowspan="2"></td><td colspan="2">Quick-Service restaurant</td><td colspan="2">General retailer</td><td colspan="2">Pharmacy</td></tr><tr><td>Click</td><td>Conversion</td><td>Click</td><td>Conversion</td><td>Click</td><td>Conversion</td></tr><tr><td>Intercept</td><td>-0.325***(0.130)</td><td>-1.259***(0.310)</td><td>-2.531***(0.406)</td><td>-1.636***(0.328)</td><td>-2.145***(0.872)</td><td>-1.191***(0.465)</td></tr><tr><td> $In(Distance_{ij})$ </td><td>-0.019(0.034)</td><td>-0.114***(0.051)</td><td>0.033(0.025)</td><td>-0.084***(0.029)</td><td>0.033(0.025)</td><td>-0.114***(0.035)</td></tr><tr><td> $In(NumCompetitors_{ij})$ </td><td>-0.493***(0.119)</td><td>0.022(0.019)</td><td>-0.189***(0.063)</td><td>0.038(0.024)</td><td>-0.232***(0.087)</td><td>0.016(0.021)</td></tr><tr><td> $In(Distance_{ij}) *In(NumCompetitors_{ij})$ </td><td>0.025(0.037)</td><td>-0.031***(0.012)</td><td>0.014(0.036)</td><td>-0.013***(0.004)</td><td>0.042(0.056)</td><td>-0.012***(0.004)</td></tr><tr><td> $In(MedIncome_{i})$ </td><td>-0.022**(0.011)</td><td>-0.045(0.036)</td><td>0.015(0.026)</td><td>0.021**(0.010)</td><td>0.026(0.024)</td><td>0.028**(0.015)</td></tr><tr><td> $In(Population_{i})$ </td><td>0.038**(0.018)</td><td>-0.025(0.020)</td><td>0.062***(0.021)</td><td>-0.033**(0.015)</td><td>0.087***(0.034)</td><td>-0.033***(0.014)</td></tr><tr><td> $iOS_{ij}$ </td><td>0.153(0.128)</td><td>-0.208***(0.092)</td><td>0.085(0.077)</td><td>-0.113(0.061)</td><td>0.055(0.046)</td><td>-0.084**(0.044)</td></tr><tr><td> $LargeImp_{ij}$ </td><td>-0.007(0.029)</td><td></td><td>-0.018(0.017)</td><td></td><td>-0.012(0.016)</td><td></td></tr><tr><td> $CatEnt_{ij}$ </td><td>0.021**(0.011)</td><td></td><td>0.038**(0.018)</td><td></td><td>0.053(0.021)</td><td></td></tr><tr><td> $CatSocial_{ij}$ </td><td>-0.008(0.017)</td><td></td><td>-0.023**(0.011)</td><td></td><td>-0.018(0.010)</td><td></td></tr><tr><td> $CatGame_{ij}$ </td><td>0.221**(0.071)</td><td></td><td>0.137***(0.051)</td><td></td><td>0.072***(0.031)</td><td></td></tr><tr><td> $\rho$ </td><td colspan="2">0.221***(0.090)</td><td colspan="2">0.153***(0.052)</td><td colspan="2">0.138***(0.049)</td></tr><tr><td>N</td><td colspan="2">254,089</td><td colspan="2">180,492</td><td colspan="2">108,443</td></tr></table>

\*\*\* and \*\* indicate 1% and 5% levels of significance, respectively.

Table 7. Effects of Environmental Conditions

<table><tr><td rowspan="2"></td><td colspan="2">Urban vs. rural</td><td colspan="2">Bad weather</td></tr><tr><td>Click</td><td>Conversion</td><td>Click</td><td>Conversion</td></tr><tr><td>Intercept</td><td>-0.352***(0.122)</td><td>-0.974***(0.249)</td><td>-0.328***(0.112)</td><td>-0.872***(0.175)</td></tr><tr><td> $In(Distance_{ij})$ </td><td>-0.081(0.316)</td><td>-0.122***(0.038)</td><td>-0.092(0.253)</td><td>-0.121***(0.032)</td></tr><tr><td> $In(NumCompetitors_{ij})$ </td><td>-0.514***(0.219)</td><td>0.016(0.012)</td><td>-0.386***(0.199)</td><td>0.035(0.028)</td></tr><tr><td> $Urban_i$ </td><td>-0.016***(0.002)</td><td>-0.038***(0.014)</td><td></td><td></td></tr><tr><td> $In(Distance_{ij}) * In(NumCompetitors_{ij})$ </td><td>0.088(0.170)</td><td>-0.026***(0.007)</td><td></td><td></td></tr><tr><td> $In(Distance_{ij}) * Urban_i$ </td><td>-0.006(0.033)</td><td>-0.010***(0.004)</td><td></td><td></td></tr><tr><td> $In(NumCompetitors_{ij}) * Urban_i$ </td><td>-0.015(0.044)</td><td>-0.027(0.082)</td><td></td><td></td></tr><tr><td> $In(Distance_{ij}) * In(NumCompetitors_{ij}) * Urban_i$ </td><td>-0.008(0.026)</td><td>-0.002(0.015)</td><td></td><td></td></tr><tr><td> $BadWeather_{ij}$ </td><td></td><td></td><td>-0.261***(0.024)</td><td>-0.159***(0.063)</td></tr><tr><td> $In(Distance_{ij}) * In(NumCompetitors_{ij})$ </td><td></td><td></td><td>0.035(0.170)</td><td>-0.015***(0.005)</td></tr><tr><td> $In(Distance_{ij}) * BadWeather_{ij}$ </td><td></td><td></td><td>0.111(0.074)</td><td>-0.154***(0.011)</td></tr><tr><td> $In(NumCompetitors_{ij}) * BadWeather_{ij}$ </td><td></td><td></td><td>0.087(0.089)</td><td>-0.048(0.064)</td></tr><tr><td> $In(MedIncome_i)$ </td><td>0.025(0.028)</td><td>-0.037(0.033)</td><td>-0.026(0.027)</td><td>-0.034(0.039)</td></tr><tr><td> $In(Population_i)$ </td><td>0.129(0.103)</td><td>-0.231***(0.054)</td><td>0.035***(0.016)</td><td>-0.021(0.018)</td></tr><tr><td> $iOS_{ij}$ </td><td>-0.039(0.072)</td><td></td><td>0.137(0.106)</td><td>-0.234***(0.055)</td></tr><tr><td> $LargeImp_{ij}$ </td><td>0.082***(0.011)</td><td></td><td>-0.027(0.039)</td><td></td></tr><tr><td> $CatEnt_{ij}$ </td><td>-0.014(0.019)</td><td></td><td>0.082***(0.010)</td><td></td></tr><tr><td> $CatSocial_{ij}$ </td><td>0.241***(0.065)</td><td></td><td>-0.018(0.026)</td><td></td></tr><tr><td> $CatGame_{ij}$ </td><td>0.174***(0.063)</td><td></td><td>0.242***(0.064)</td><td></td></tr><tr><td> $\rho$ </td><td colspan="2">0.174***(0.063)</td><td colspan="2">0.179***(0.056)</td></tr><tr><td>N</td><td colspan="4">230,217</td></tr></table>

\*\*\* and \*\* indicate 1% and 5% levels of significance, respectively.

conditions. For local competition, we investigate how its effect is moderated by product differentiation. Besides, we study time-of-day and day-of-week differences in distance and local competition effects.

## 7.1. Environmental Conditions

Transportation costs could vary in different environments. To generalize the effect of distance, we compare and contrast the geofence advertising performance between urban and rural areas because the traffic conditions are likely to be significantly different. Because of heavier traffic in urban areas, consumers typically incur higher transportation costs to travel the same distance in urban areas relative to rural ones. Following the urban-rural classification of the U.S. Census Bureau,<sup>15</sup> we construct a dummy variable Urban to indicate whether Geofence i is located in an urban area. The indicator is allowed to interact with the variables of interest, while Population is dropped as it has been used to distinguish urban areas from rural ones. Reported in the first panel of Table 7, the results not only validate our baseline results but generate some new insights. Consumers tend to be more sensitive to distance in urban areas, perhaps because traveling in such an area is perceived as costlier relative to rural areas. We also find that the location type of a geofence does not moderate the effect of local competition in the click stage. This suggests that the propensity to explore the advertiser is indifferent to the geographical areas, after controlling for local competition. Finally, the coefficient of the three-way interaction in the conversion stage is insignificant, suggesting that there is no systemic difference in moderation between local competition and distance across different geographical areas.

Besides traffic, weather could also have a significant impact on transportation costs. Because bad weather conditions could accentuate transportation costs, we construct BadWeather<sub>ij</sub> to capture whether it is raining or snowing at the time of an ad impression. We retrieve historical weather conditions using OpenWeather APIs<sup>16</sup> based on the timestamp and latitude/longitude coordinates of each observation. For a more general model, we interact BadWeather<sub>i</sub> with distance and local competition to quantify the moderating effects. As reported in the second panel of

Table 7, the estimation results show that bad weather conditions not only lower consumers’ overall willingness to click on geofencing ads but also intensify the negative effect of distance on conversion performance. This is likely because of the fact that transportation costs are higher when it is raining or snowing.

## 7.2. Product Differentiation

Prior research (Shaked and Sutton 1982, Hortaçsu and Syverson 2004) suggests that the less differentiated the products, the higher the intensity of competition. Following this theoretical guidance, we conjecture that the differentiation between an advertiser and its rivals alleviates the competition among them in geofence advertising. Using various restaurant characteristics collected from Yelp, we consider product differentiation in terms of price and product characteristics.

As Rosen (1974) theorizes, products can be differentiated through their prices. We use price ranges on Yelp to classify the local competitors into two groups, depending on whether the price range of a rival is the same as the advertiser’s. Because the price range of the chosen advertiser is labeled as inexpensive (i.e., one dollar sign), we calculate $N u m C o m p e t i t o r s _ { i j } ^ { s i m i }$ and $N u m C o m p e t i t o r s _ { i j } ^ { d i f f }$ to represent the number of rivals with one dollar sign and at least two dollar signs, respectively. The first panel of Table 8 shows how price ranges moderate the effect of local competition. The coefficients of $N u m C o m p e t i t o r s _ { i j } ^ { s i m i }$ and $N u m C o m p e t i t o r s _ { i j } ^ { d i f f }$ are both negative and significant, consistent with our results on local competition in the click stage. More importantly, the marginal effects of $\ln ( N u m C o m p e t i t o \ ' { s } _ { i j } ^ { s i m i } )$ is larger than that of $\ln ( N u m C o m p e t i t o r s _ { i j } ^ { d i f f } )$ , confirming that the effect of local competition diminishes as the degree of product differentiation increases. Quantitatively, having one more competitor with the same price range within the consumer proximal zone is associated with a 2.33% decrease in click-through rate, whereas click performance reduces by 2.03% if one more restaurant with a higher price range is present. Although most results remain qualitatively unchanged, it is worth noting that distance only moderates competition between restaurants that are less differentiated.

Table 8. Product Differentiation

<table><tr><td rowspan="2"></td><td colspan="2">Price range</td><td colspan="2">Cuisine type</td><td colspan="2">Ambience</td></tr><tr><td>Click</td><td>Conversion</td><td>Click</td><td>Conversion</td><td>Click</td><td>Conversion</td></tr><tr><td>Intercept</td><td>-0.358***(0.254)</td><td>-1.017***(0.337)</td><td>-0.360***(0.129)</td><td>-0.935***(0.242)</td><td>-0.360***(0.123)</td><td>-0.987***(0.242)</td></tr><tr><td> $In(Distance_{ij})$ </td><td>-0.013(0.039)</td><td>-0.118***(0.054)</td><td>-0.048(0.053)</td><td>-0.123***(0.039)</td><td>-0.023(0.046)</td><td>-0.121***(0.034)</td></tr><tr><td> $In(NumCompetitor_{ij}^{simi})$ </td><td>-0.718***(0.216)</td><td>0.020(0.014)</td><td>-0.638***(0.155)</td><td>0.027(0.068)</td><td>-0.783***(0.155)</td><td>0.023(0.025)</td></tr><tr><td> $In(NumCompetitor_{ij}^{diff})$ </td><td>-0.187***(0.060)</td><td>0.016(0.013)</td><td>-0.364***(0.120)</td><td>0.108(0.076)</td><td>-0.231***(0.029)</td><td>0.007(0.019)</td></tr><tr><td> $In(Distance_{ij}) * In(NumCompetitor_{ij}^{simi})$ </td><td>0.072(0.068)</td><td>-0.039***(0.014)</td><td>0.033(0.059)</td><td>-0.031***(0.012)</td><td>0.030(0.020)</td><td>-0.044***(0.016)</td></tr><tr><td> $In(Distance_{ij}) * In(NumCompetitor_{ij}^{diff})$ </td><td>0.034(0.022)</td><td>-0.008(0.013)</td><td>0.049(0.042)</td><td>-0.004***(0.001)</td><td>0.034(0.022)</td><td>-0.002(0.009)</td></tr><tr><td> $In(MedIncome_i)$ </td><td>-0.027(0.023)</td><td>-0.031(0.028)</td><td>-0.028(0.026)</td><td>-0.029(0.025)</td><td>-0.056(0.089)</td><td>-0.032(0.030)</td></tr><tr><td> $In(Population_i)$ </td><td>0.044**(0.018)</td><td>-0.026(0.023)</td><td>0.044***(0.018)</td><td>-0.038(0.022)</td><td>0.043***(0.017)</td><td>-0.031(0.029)</td></tr><tr><td> $iOS_{ij}$ </td><td>0.126(0.110)</td><td>-0.226***(0.051)</td><td>0.130(0.095)</td><td>-0.222***(0.053)</td><td>0.111(0.098)</td><td>-0.236***(0.062)</td></tr><tr><td> $LargeImp_{ij}$ </td><td>-0.028(0.033)</td><td></td><td>-0.028(0.033)</td><td></td><td>-0.025(0.034)</td><td></td></tr><tr><td> $CatGame_{ij}$ </td><td>0.075***(0.032)</td><td></td><td>0.081***(0.032)</td><td></td><td>0.080***(0.015)</td><td></td></tr><tr><td> $CatSocial_{ij}$ </td><td>-0.012(0.014)</td><td></td><td>-0.015(0.016)</td><td></td><td>-0.013(0.018)</td><td></td></tr><tr><td> $CatGame_{ij}$ </td><td>0.197***(0.080)</td><td></td><td>0.231***(0.062)</td><td></td><td>0.231***(0.057)</td><td></td></tr><tr><td> $\rho$ </td><td colspan="2">0.178***(0.070)</td><td colspan="2">0.174***(0.063)</td><td colspan="2">0.171***(0.069)</td></tr><tr><td>N</td><td colspan="2">230,217</td><td colspan="2">230,217</td><td colspan="2">230,217</td></tr></table>

\*\*\* and \*\* indicate 1% and 5% levels of significance, respectively.

We consider two additional dimensions of product differentiation, namely cuisine type and dining ambiance. Because the focal advertiser is an American food restaurant, we refer to $N u m C o m p e t i t o r _ { i j } ^ { s i m i }$ and $N u m C o m p e t i t o r _ { i j } ^ { d i f f }$ as the numbers of the restaurants that serve the same and different cuisine types, respectively. The estimation results are reported in the second panel of Table 8. Consistent with our earlier product differentiation analysis, we find that the stronger competition from other American restaurants generates stronger negative impacts on clickthrough performance. Last, we analyze the effect of dining ambience in a similar way. The focal advertiser provides a casual dining experience, so we code NumCompetitor<sup>simi</sup><sub>ij</sub> and $\begin{array} { r } { N u m C o m p e t i t o r _ { i j } ^ { d i f f } } \end{array}$ as the numbers of casual and classy dining establishments, respectively. The estimation results are reported in the third panel of Table 8, offering consistent insights into the impacts of product differentiation.

## 7.3. Temporal Effects

Temporal factors have been shown to affect the performance of LBA (Luo et al. 2014, Fong et al. 2015,

Table 9. Temporal Effects

<table><tr><td rowspan="2"></td><td colspan="2">Working hours</td><td colspan="2">Weekdays</td></tr><tr><td>Click</td><td>Conversion</td><td>Click</td><td>Conversion</td></tr><tr><td>Intercept</td><td>-0.191***(0.054)</td><td>-0.894***(0.269)</td><td>-0.286***(0.095)</td><td>-0.900***(0.229)</td></tr><tr><td> $\text{In}(Distance_{ij})$ </td><td>-0.007(0.031)</td><td>-0.101***(0.042)</td><td>-0.074(0.241)</td><td>-0.119***(0.035)</td></tr><tr><td> $\text{In}(NumCompetitors_{ij})$ </td><td>-0.513***(0.135)</td><td>0.009(0.010)</td><td>-0.436***(0.168)</td><td>0.013(0.007)</td></tr><tr><td> $Working_{ij}$ </td><td>-0.118***(0.022)</td><td>-0.094***(0.012)</td><td>-0.093***(0.030)</td><td>-0.062***(0.018)</td></tr><tr><td> $\text{In}(Distance_{ij}) * \text{In}(NumCompetitors_{ij})$ </td><td>0.021(0.028)</td><td>-0.016***(0.005)</td><td>0.076(0.134)</td><td>-0.015***(0.004)</td></tr><tr><td> $\text{In}(Distance_{ij}) * \text{Working}_{ij}$ </td><td>0.005(0.012)</td><td>-0.026***(0.012)</td><td>0.019(0.032)</td><td>-0.035***(0.009)</td></tr><tr><td> $\text{In}(NumCompetitors_{ij}) * \text{Working}_{ij}$ </td><td>-0.053***(0.019)</td><td>-0.007(0.006)</td><td>-0.037***(0.013)</td><td>-0.005(0.013)</td></tr><tr><td> $\text{In}(MedIncome_i)$ </td><td>-0.027(0.025)</td><td>-0.033(0.036)</td><td>-0.027(0.030)</td><td>-0.030(0.042)</td></tr><tr><td> $\text{In}(Population_i)$ </td><td>0.045***(0.015)</td><td>-0.034(0.020)</td><td>0.039***(0.012)</td><td>-0.029(0.030)</td></tr><tr><td> $iOS_{ij}$ </td><td>0.146(0.115)</td><td>-0.212***(0.085)</td><td>0.134(0.107)</td><td>-0.232***(0.053)</td></tr><tr><td> $Largelmp_{ij}$ </td><td>0.010(0.032)</td><td></td><td>-0.025(0.042)</td><td></td></tr><tr><td> $CatEnt_{ij}$ </td><td>0.067***(0.024)</td><td></td><td>0.081***(0.011)</td><td></td></tr><tr><td> $CatSocial_{ij}$ </td><td>-0.008(0.016)</td><td></td><td>-0.019(0.026)</td><td></td></tr><tr><td> $\rho$ </td><td></td><td>0.216***(0.065)</td><td></td><td>0.174***(0.065)</td></tr><tr><td>N</td><td></td><td></td><td></td><td></td></tr></table>

\*\*\* and \*\* indicate 1% and 5% level of significance, respectively.

Ghose et al. 2019b). Indeed, consumer purchase intent can vary across different periods of time. To be more specific, advertisements inserted at dining time are likely to result in higher click-through and conversion rates than those displayed at off-peak hours. To quantify these time effects, we construct a dummy variable, $W o r k i n g _ { i j } ,$ to indicate whether an impression was displayed during nondining hours. We define dining hours to include the time windows 11 a.m. to 1 p.m. and 6 p.m. to $8 { \mathrm { p . m . } } ^ { 1 7 }$ For example, if an impression is inserted at $3 \mathrm { p . m . } ,$ then we code $W o r k i n g _ { i j } { = } \dot { 1 } . \dot { 1 } 8$ In this analysis, we incorporate time effects into our models by adding $W o r k i n g _ { i j }$ and its interactions with distance and local competition. The results are reported in the first panel of Table 9. In both stages, the negative and significant coefficients of $W o r k i n g _ { i j }$ indicate that consumers are less interested in restaurant-related ads during nondining (working) hours. We find that time effects further intensify the impacts of competition in the click stage and those of distance in the conversion stage. One possible explanation could be that a consumer who is looking for restaurants during working hours may desire to choose a relatively convenient option; as a result, she could be more sensitive to the availability of dining alternatives nearby. Treating dining hours as benchmarks, we see that the clickthrough rate during working hours drops by a noticeable margin of 62.08%. Conditional on the occurrence of a click, mobile users are 31.71% less likely to take further actions in the conversion stage.

We further extend the temporal analysis to the horizon of week by comparing weekdays and weekends. Applying a similar procedure, we code a Working<sub>i</sub> dummy to indicate whether an ad is inserted on a weekday or a weekend. Table 9 summarizes the results, showing a similar pattern to the counterparts obtained in the time-of-day analysis. The results suggest that consumers are less likely to respond to geofencing ads on working days $( \mathrm { i . e . , }$ weekdays). Also, the negative impacts of distance and local competition are intensified when consumers have a tighter time constraint on searching and evaluating products. Overall, the time-of-day and day-of-week results are consistent with each other.

## 8. Conclusions

We examined the roles of distance (between an advertiser establishment and a consumer) and local competition (between the advertiser and its productmarket rivals in the consumer’s vicinity) on consumer response to mobile geofence advertising campaigns, a popular type of location-based advertising. We study the click and conversion decisions, based on a rich data set for a nationwide dining chain (and other restaurant and retail advertisers) from one of the largest location-based marketing agencies. Applying a hierarchical Bayes bivariate probit model to the highly granular data, we obtain a number of robust empirical regularities.

First, we find that click-through rate is negatively related to local competition (i.e., the number of alternatives nearby consumers) but not distance, whereas the conversion rate is influenced by distance rather than local competition. Quantitatively, having one additional competitor into the consumer’s vicinity decreases clickthrough rate by 1.03%. The conversion rate drops by 17.64% if the establishment is 1 mile further away from consumers. Second, we find similar results using the geofencing campaigns of other nationwide advertisers, including another restaurant chain, a general retailer, and a pharmacy. We also calculate local competition based on the advertiser’s vicinity to check the robustness of the findings.

We further consider the moderating effects of locations, weather conditions, product differentiation, and timing. First, we find that distance is more impactful in urban areas (than rural ones) and under bad weather conditions (e.g., rainy or snowy), perhaps because of higher transportation costs. Second, we show that product differentiation with respect to price ranges ameliorates the negative effects of both distance and local competition. Specifically, having one more nondifferentiated competitor (in the same price range) is associated with a 2.33% decrease in the click-through rate, whereas the click performance drops by 2.03% if one more differentiated competitor is added to the geofence. Different cuisine types and ambiance styles also help relieve the pressure of competition. Finally, we see significant time-of-day effects, whereby consumers are more sensitive to both distance and local competition during office working hours. This perhaps reflects the lower intensity of demand in working hours when click-through and conversion rates are 62.08% and 32.71% lower, respectively, compared with the corresponding levels observed in nonworking hours. A similar pattern maintains when the weekend effect is considered.

We precisely compute distance and quantify its impacts on location-based advertising. Our results on the importance of distance echo prior research (Ghose et al. 2013, Luo et al. 2014, Fang et al. 2015). These results are also consistent with anecdotal evidence from industry reports, where 70% of consumers use mobile devices to search and visit local stores within 5 miles (Google 2013, 2014). More notably, our results demonstrate the importance of local competition in consumer decision making in geofencing. Although prior research (Fong et al. 2015, Dubé et al. 2017) studies the effects of mobile promotions in geoconquesting, we focus on modeling the underlying mechanism of consumer choice. Our findings indicate that taking both consumer transportation costs and the severity of local competition together into consideration helps improve the performance of locationbased advertising. In addition, we examine local competition with product differentiation, and our results show that product differentiation moderates the competitive effect in geofence advertising. Last, we find that the click and conversion performance exhibit a sharp contrast across different times of a day and across different days in a week, suggesting that consumer responses to geofencing could systematically vary because of temporal factors.

These results are relevant to practitioners and have implications for the design of location-based strategies. Whereas advertisers in our data set used simple heuristics for geotargeting users (i.e., target all devices running particular apps within the geofence), one can conceive of richer strategies that take into account distance and local competition. Such strategies are becoming more feasible by the day, as more powerful real-time analytics capabilities are deployed for this purpose. In this regard, our results show distance and local competition have varying significance across decision stages: competition is critical for clickthrough, but distance is all-important at the time of conversion. Our results should help advertisers more precisely determine the size of geofence zones and provide managerial insights for dynamic geotargeting or location-based couponing, as applicable. For instance, advertisers are encouraged to decompose a macro-geofence of arbitrary radius into micro-geofences conditional on the intensity of local competition. Moreover, considering local competition would enable advertisers to be more cost-efficient at building brand awareness in the click stage, leading to more fruitful conversions downstream. This is particularly important for new brand advertisers, or for sellers of high-involvement products or services like car dealers or real estate agencies.

To further improve the performance of geofence advertising, advertisers should not only consider overall competition but recognize the importance of product differentiation as well. Highlighting differentiated products on ads may help alleviate the substitution effect from competing alternatives. For example, a restaurant advertiser could display seasonal menus in ads, rather than common everyday items, to enhance real and perceived differentiation. As to time-of-day effects, our results indicate that the effects of distance and competition are amplified during office working hours, further lowering the effectiveness of geofencing. Therefore, it is desirable for advertisers to reduce geofence radii and target smaller zones to compensate for the low click-through and conversion rates during less busy working hours. Finally, our robustness checks indicate that the results should be applicable to other O2O settings, such as general retailers (e.g., Walmart and Target), pharmacy (e.g., CVS and Walgreens), grocery stores (e.g., Whole Foods and Kroger), and other service providers like auto repair, hair salons, plumbers, and the like.

Turning to limitations, although we have a high level of granularity in the geofence data, we do not actually observe conversions. Instead, we operationalize conversions as the actions taken on landing pages, such as address look-up or phone calls. Although we cannot exactly calculate precise return on advertising spend of geofencing campaigns without data on sales, the findings are likely to be meaningful as long as sales are correlated with the user actions we do observe. Another limitation is that we analyze a limited set of advertiser types. Although these are the active adopters of geofencing, it would be useful for future work to examine other types of advertisers such as healthcare providers and other specialty service providers. Last, our data do not capture the trajectories of consumers (Ghose et al. 2019a), making it impossible to discern whether a consumer is approaching or withdrawing from the focal establishment. Our results show the mean effect of distance at the aggregate level, suggesting that the impact of consumer movements, if any, should have been averaged out in our model. As location-based services are advancing, we envision incorporating trajectory data to control for the impact of consumer movement (e.g., Ghose et al. 2019a). Despite these limitations, this study is one of the first to document robust empirical regularities with respect to distance and local competition in location-based advertising It also generates useful managerial implications on how the two critical factors affect consumer responses and profitable targeting strategies.

## Acknowledgments

The authors thank the senior editor, the associate editor, and three anonymous reviewers for constructive suggestions. The authors also thank participants at the 2016 Symposium on Statistical Challenges in Electronic Commerce and Research; the 2016 Workshop on Information Systems and Economics; the 2019 China Summer Workshop on Information Systems; and research seminars at National Taiwan University, Tai wan, for helpful comments.

## Endnotes

<sup>1</sup> Per our agreement with the marketing agency, we are unable to disclose the name of the dining chain.

<sup>2</sup> The conversations with the data provider confirm the lack of such a consideration, which motivates us to explore the role of local competition.

<sup>3</sup> The only exception we are aware of is Molitor et al. (2020), which focuses on coupon clicking when consumers proactively look for local deals provided by one single app (i.e., pull advertising). By contrast, we jointly examine click and conversion responses when ads are inserted in various apps (i.e., push advertising)

<sup>5</sup> The marketing agency shall remain unnamed in this study per our nondisclosure agreement.

<sup>6</sup> The categories of publishers are defined in OpenRTB API specification of Interactive Advertising Bureau (IAB), and publisher top categories are extracted to categorize publishers for the analysis.

<sup>7</sup> Haversine formula is discussed at https://en.wikipedia.org/wiki/ Haversine\_formula.

<sup>8</sup> Yelp Fusion API can be found at https://www.yelp.com/developers/ documentation/v3/business\_search.

<sup>9</sup> We also consider the radius of the consumer vicinity zone as either 1 or 3 miles for robustness analysis. The results for alternative vicinity zones are qualitatively similar.

<sup>10</sup> Google Reverse Geocoding API can be found at https://developers .google.com/maps/documentation/javascript/examples/geocoding -reverse.

<sup>11</sup> U.S. Census Bureau information can be found at https://www .census.gov/programs-surveys/acs/data.html.

<sup>12</sup> For every impression, we need to send a request to Yelp Fusion API while the daily limit of the API calls is only up to 5,000. We could scale the size of the data set out with more computation recourses if necessary.

<sup>13</sup> To ensure that the resulting data set is not subject to sampling bias, we conduct a series of t-tests to ensure the comparability between the sampled data and others acquired through non–GPS-based sources. The results of the balance checks are available on request.

<sup>14</sup> The results of the two robustness checks are available upon request.

<sup>15</sup> U.S. Census Urban and Rural Classification information can be found at https://www.census.gov/programs-surveys/geography/ guidance/geo-areas/urban-rural/2010-urban-rural.html.

<sup>16</sup> More information about OpenWeather APIs is available at https:// openweathermap.org/history.

<sup>17</sup> We also use different time windows (e.g., 10 a.m. to 2 p.m. and 5 p.m. to 9 p.m.). The results remain qualitatively the same.

<sup>18</sup> We only include impressions that occur between 11 a.m. and 10 p.m. in this analysis because of the common business hours of restaurants.

## References

Andrews M, Luo X, Fang Z, Ghose A (2016) Mobile ad effectiveness: Hyper-contextual targeting with crowdedness. Marketing Sci. 35(2):218–233.

Andrews R, Srinivasan TC (1995) Studying consideration effects in empirical choice models using scanner panel data. J. Marketing Res, 32(1):30–41

Bell D, Ho T, Tang C (1998) Determining where to shop: Fixed and variable costs of shopping. J. Marketing Res. 35(3):352–369.

Bettman JR (1979) An Information Processing Theory of Consumer Choice (Addison-Wesley, Boston, MA).

BIA/Kelsey (2014) Franchises spend nearly half of marketing budgets on digital. Accessed April 20, 2020, http://www.biakelsey.com/ research-data/current-research/getting-72-billion-biakelseys -mobile-ad-revenue-forecast/.

BIA/Kelsey (2017) Getting to \$72 billion: BIA/Kelsey’s mobile ad revenue forecast.

Bresnahan TF, Reiss PC (1991) Entry and competition in concentrated markets. J. Political Econom. 99(5):977–1009.

Chen Y, Li X, Sun M (2017) Competitive mobile geo targeting. Marketing Sci. 36(5):666–682.

Cho E, Myers SA, Leskovec J (2011) Friendship and mobility: User movement in location-based social networks. Proc. 17th ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining (Association for Computing Machinery, New York), 1082–1090.

Court D, Elzinga D, Mulder S, Vetvik OJ (2009) The consumer deci sion journey. McKinsey & Company, https://www.mckinsey.com business-functions/marketing-and-sales/our-insights/the -consumer-decision-journey#.

Curry L (1978) Demand in the spatial economy: II homo Stochasticus Geographic Anal. 10(4):309–344.

Danaher PJ, Bonfrer A, Dhar S (2008) The effect of competitive ad vertising interference on sales for packaged goods. J. Marketing Res. 45(2):211–225.

Desaulniers T (2016) A marketer’s guide to secondary conversion actions. Accessed April 20, 2020, https://www.mediapost.com publications/article/281845/a-marketers-guide-to-secondary -conversion-actions.html.

Dixit AK, Stiglitz JE (1977) Monopolistic competition and optimum product diversity. Amer. Econom. Rev. 67(3):297–308.

Dubé JP, Fang Z, Fong N, Luo X (2017) Competitive price targeting with smartphone coupons. Marketing Sci. 36(6):944–975.

Fang Z, Gu B, Luo X, Xu Y (2015) Contemporaneous and delayed sales impact of location-based mobile promotions. Inform. Systems Res. 26(3):552–564.

Fong NM, Fang Z, Luo X (2015) Geo-conquesting: Competitive locational targeting of mobile promotions. J. Marketing Res. 52(5):726–735.

Forman C, Ghose A, Goldfarb A (2009) Competition between local and electronic markets: How the benefit of buying online de pends on where you live. Management Sci. 55(1):47–57.

Gelman A, Rubin DB (1992) Inference from iterative simulation using multiple sequences. Statist. Sci. 7(4):457–472.

Gensch DH (1987) A two-stage disaggregate attribute choice model. Marketing Sci. 6(3):223–239

Ghose A, Han SP (2014) Estimating demand for mobile applications in the new economy. Management Sci. 60(6):1470–1488.

Ghose A, Goldfarb A, Han SP (2013) How is the mobile Internet different? Search costs and local activities. Inform. Systems Res. 24(3):613–631.

Ghose A, Li B, Liu S (2019a) Mobile targeting using customer tra jectory patterns. Management Sci. 65(11):5027–5049.

Ghose A, Kwon H, Lee D, Oh W (2019b) Seizing the commuting moment: Contextual targeting based on mobile transportation apps. Inform. Systems Res. 30(1):154–174.

Google (2013) Mobile path to purchase. Accessed April 20, 2020 https://www.thinkwithgoogle.com/advertising-channels/mobile -marketing/mobile-path-to-purchase-5-key-findings/.

Google (2014) Understanding consumers’ local search behavior. Accessed April 20, 2020, https://www.thinkwithgoogle.com advertising-channels/search/how-advertisers-can-extend-their -relevance-with-search-download/.

Hanson S (1980) Spatial diversification and multipurpose travel: Implications for choice theory. Geographic Anal. 12(3):245–257.

Ho YC, Wu J, Tan Y (2017) Disconfirmation effect on online rating behavior: A structural model. Inform. Systems Res. 28(3):626–642.

Hoff PD (2009) A First Course in Bayesian Statistical Methods (Springer Science & Business Media, New York).

Hortaçsu A, Syverson C (2004) Product differentiation, search costs, and competition in the mutual fund industry: A case study of S&P 500 index funds. Quart. J. Econom. 119(2):403–456.

Howard J, Sheth JN (1969) The Theory Buyer Behavior (Wiley, New York).

Inc (2016) Why O2O commerce is a trillion-dollar opportunity. Accessed April 20, 2020, https://www.inc.com/john-rampton/why-online -to-offline-commerce-is-a-trillion-dollar-opportunity.html.

Katz ML, Shapiro C (1985) Network externalities, competition, and compatibility. Amer. Econom. Rev. 75(3):424–440.

Kenny D, Marshall JF (2000) Contextual marketing: The real business of the Internet. Harvard Bus. Rev. 78(6):119–125.

Kotler P, Armstrong G (2011) Principles of Marketing (Prentice-Hall, Upper Saddle River, NJ).

Luo X, Andrews M, Fang Z, Phang CW (2014) Mobile targeting Management Sci. 60(7):1738–1756.

Lussier DA, Olshavsky RW (1979) Task complexity and contingent processing in brand choice. J. Consumer Res. 6(2):154–165.

McKinsey Global Institute (2011) Big data: The next frontier for innovation, competition, and productivity. Accessed April 20, 2020, https://www.mckinsey.com/business-functions/mckinsey-digital/ our-insights/big-data-the-next-frontier-for-innovation#.

Molitor D, Reichhart P, Spann M, Ghose A (2020) Effectiveness of location-based advertising and the impact of interface design. Working paper, Fordham University, New York.

Mulligan GF (1983) Consumer demand and multipurpose shopping behavior. Geographic Anal. 15(1):76–81.

Netscribes (2019) Global mobile location-based services market (2018-2023). Report, Netscribes, New York.

Netzer O, Lattin JM, Srinivasan V (2008) A hidden Markov model of customer relationship dynamics. Marketing Sci. 27(2):185–204.

Payne JW (1976) Task complexity and contingent Processing in de cision making: An information search and protocol analysis. Organ. Behav. Human Performance 16:366–387.

Qiu L, Shi Z, Whinston A (2018) Learning from your friends’ check ins: An empirical study of location-based social networks. Inform. Systems Res. 29(4):1044–1061.

Ratchford BT (1980) The value of information for selected appliances. J. Marketing Res. 17(1):14–25.

Roberts JH, Lattin JM (1991) Development and testing of a model of consideration set composition. J. Marketing Res. 28(4): 429–440.

Rosen S (1974) Hedonic prices and implicit markets: Product differentiation in pure competition. J. Political Econom. 82(1):34–55.

Santhanam R, Liu D, Shen WCM (2016) Research note—Gamification of technology-mediated training: Not all competitions are the same. Inform. Systems Res. 27(2):453–465.

Shaffer G, Zhang ZJ (1995) Competitive coupon targeting. Marketing Sci. 14(4):395–416.

Shaked A, Sutton J (1982) Relaxing price competition through product differentiation. Rev. Econom. Stud. 49(1):3–13.

Spiegelhalter DJ, Best NG, Carlin BP, Van Der Linde A (2002) Bayesian measures of model complexity and fit. J. Roy. Statist. Soc. Ser. B Statist. Methodology 64(4):583–639.

Srinivasan S, Rutz OJ, Pauwels K (2016) Paths to and off purchase: Quantifying the impact of traditional marketing and consume activity. J. Acad. Marketing Sci. 44(4):440–453.

Srinivasan S, Vanhuele M, Pauwels K (2010) Mind-set metrics in market response models: An integrative approach. J. Marketin Res. 47(4):672–684

Stahl K (1982) Location and spatial pricing theory with non-convex transportation cost schedules. Bell J. Econom. 13(2):575–582.

Statista (2016) Quick-service (fast food) restaurants in the U.S. Report, Statista, Hamburg, Germany.

U.S. Census Bureau (2015) 2011-2015 American Community Survey 5 year estimates. Accessed April 20, 2020, https://www.census.gov programs-surveys/acs/technical-documentation/table-and -geography-changes/2015/5-year.html.

Verve Mobile (2013) Location powered mobile advertising report. Accessed April 20, 2020, http://vervemobile.com/pdfs/LIR LIR\_full.pdf.

Weber TA, Zheng Z (2007) A model of search intermediaries and paid referrals. Inform. Systems Res. 18(4):414–436.

YP Marketing Solutions (2012) Local insights report, Q2 2012. Report, YP Intellectual Properties, Tucker, GA.

YP Marketing Solutions (2014) Mobile retargeting, optimization and hitting the ROI bullseye. Report, YP Intellectual Properties, Tucker, GA. http://national.yp.com/downloads/MMS \_Chicago.pdf.
