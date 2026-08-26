---
otero_id: 1946
otero_key: "FAPPVVHC"
title: "Effectiveness of Location-Based Advertising and the Impact of Interface Design"
authors: "Dominik Molitor; Martin Spann; Anindya Ghose; Philipp Reichhart"
year: "2020"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2020.1759922"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Effectiveness of Location-Based Advertising and the Impact of Interface Design

Dominik Molitor , Martin Spann , Anindya Ghose & Philipp Reichhart

To cite this article: Dominik Molitor , Martin Spann , Anindya Ghose & Philipp Reichhart (2020) Effectiveness of Location-Based Advertising and the Impact of Interface Design, Journal of Management Information Systems, 37:2, 431-456, DOI: 10.1080/07421222.2020.1759922

To link to this article: https://doi.org/10.1080/07421222.2020.1759922

![](/api/attachments/FAPPVVHC/fulltext/images/eb56175e818475587f00ba2838cec70bae0b55473ef69ca0460ff3a631389f06.jpg)

View supplementary material

![](/api/attachments/FAPPVVHC/fulltext/images/a49b82fbb5680d7515b6b9d0e6106f5c0f30dddddfd880b31646212b2b1ad181.jpg)

Published online: 16 Jun 2020.

![](/api/attachments/FAPPVVHC/fulltext/images/cd7448ce54225f9cf08d6086897cd62614033a3180867eecf7763685cd7fb89f.jpg)

Submit your article to this journal

![](/api/attachments/FAPPVVHC/fulltext/images/cb2aca15d115eba7fee75740a85494be0bd0fec31f38e7ab5ee79a4966bd7af2.jpg)

Article views: 12

![](/api/attachments/FAPPVVHC/fulltext/images/4d8ef4a0f36893c0278752d57ad220c4a4538b03f29de7d0d0a5272b8ef6a6d4.jpg)

View related articles

![](/api/attachments/FAPPVVHC/fulltext/images/29e002e269c94816192e98dd679ba67232c68a7276a7aa8ea26597bddbf7bc46.jpg)

View Crossmark data

Check for updates

# E<sup>f</sup>ectiveness of Location-Based Advertising and the Impact of Interface Design

Dominik Molitor<sup>a</sup>, Martin Spann <sup>b</sup>, Anindya Ghose<sup>c</sup>, and Philipp Reichhart<sup>b</sup>

<sup>a</sup>Gabelli School of Business, Fordham University, New York, NY, USA; <sup>b</sup>Institute of Electronic Commerce and Digital Markets, Ludwig-Maximilians-Universität München, Munich, Germany; <sup>c</sup>Leonard N. Stern School of Business, New York University, New York, NY, USA

## ABSTRACT

O<sup>fl</sup>ine retailers increasingly use location-based coupons to target consumers in their vicinity in real-time. The rationale for the use of location-based coupons is that geographic proximity increases the relevance for consumers and, thus, the e<sup>f</sup>ectiveness of these campaigns. Two key interface-speci<sup>fi</sup>c aspects of location-based coupon applications that in<sup>fl</sup>uence their e<sup>f</sup>ectiveness are 1) the provision of distance information and 2) the distance-based ranking of coupons. The aim of this paper is to study and quantify the impact of these two key aspects of interface design on the e<sup>f</sup>ectiveness of locationbased coupons. We conduct a randomized <sup>fi</sup>eld experiment with 399,913 observations, including 3,499 di<sup>f</sup>erent coupon promotions o<sup>f</sup>ered by 3,930 di<sup>f</sup>erent stores located in 2,392 ZIP code areas in a large Western European country. Our results show that the most e<sup>f</sup>ective interface design for location-based coupons is based on a distance-based ranking. Furthermore, we <sup>fi</sup>nd signi<sup>fi</sup>cant di<sup>f</sup>erences in the impact of distance and display rank based on the interface design and the actual geographic location of users. Our results thus contribute to the understanding of consumers’ behavioral responses to location-based advertising and provide important implications for the interface-design of location-based advertising applications.

## KEYWORDS

Randomized <sup>fi</sup>eld experiment; mobile pull; mobile push; mobile analytics; behavioral e<sup>f</sup>ects; interface design; m-commerce; locationbased advertising; mobile advertising

## Introduction

Mobile advertising is the most important digital advertising channel based on ad spending, accounting for more than 75 percent of digital ad spending in the United States [32]. One of its key applications is location-based coupons. Functionally, location-based coupons can be either sent as a push noti<sup>fi</sup>cation to users without explicit request (i.e., mobile push) or provided based on explicit request (i.e., mobile pull) within speci<sup>fi</sup>c applications in which users can intentionally browse through available coupons [47].

Previous research has almost exclusively focused on investigating the users’ responses to mobile push coupons. For example, existing studies have analyzed the users’ intention to redeem coupons [15], the users’ probability of usage [33], and the e<sup>f</sup>ectiveness of mobile short message service (SMS) based [5, 16, 18] and app-based [24] push targeting strategies.<sup>1</sup> Unlike the existing studies analyzing coupons that are pushed on mobile devices, our study analyzes a location-based pull coupon application.

Speci<sup>fi</sup>cally, in addition to di<sup>f</sup>erences in the delivery mechanism, mobile pull di<sup>f</sup>ers from mobile push in three distinct categories: 1) the user’s perception, 2) the interaction with coupons/ads, and 3) the interface design. First, the di<sup>f</sup>erence in the users’ general perception is that mobile pull tends to be less often considered as spam [44] and less privacy intrusive [47]. For example, in European countries such as the United Kingdom, France, and Germany, as well as Canada, push noti<sup>fi</sup>cations require an additional opt-in, while the US requires an opt-out.<sup>2</sup> Second, from a behavioral perspective, mobile pull gives users more control over their interactions with the provider [47] and is based on di<sup>f</sup>erent motivations in their actions, allowing users to actively search for a product or service. The third key di<sup>f</sup>erentiator of mobile pull revolves around the interplay between the interface design, the organization of information, and the product discovery process. In the case of location-based coupons, users are typically presented with a variety of di<sup>f</sup>erent coupons, as well as the question of how to best organize these coupons.

From a theoretical perspective, the choice between di<sup>f</sup>erent coupon options in location-based pull advertising depends on the options’ presentation via the interface design, which is sometimes referred to as choice architecture [41]. Providers of location-based coupon applications are therefore able to make conscious decisions about how to display their coupons to users. Two key variables that may a<sup>f</sup>ect the relevance of displayed coupons are the ranking mechanism (i.e., distance-based vs. random) and the provision of distance information. In particular, the relevance of the ranking mechanism is guided by the distance to the o<sup>fl</sup>ine points-of-sale and the availability of distance information. The users’ choices are thereby in<sup>fl</sup>uenced by distance-speci<sup>fi</sup>c transportation costs [21] and ranking-related search costs [22]. The salience of actual distances to stores provides users with transparency about the required transportation costs. The ranking-related search costs are based on cognitive search e<sup>f</sup>orts that depend on the position of the coupon on the screen, which is driven by the need to <sup>fi</sup>t multiple coupons on the smartphones smaller screen sizes (compared with that of PCs or laptop computers) [6, 8, 19].

From a functional perspective, and similar to search engine advertising, location-based pull coupon providers can use distance-based rankings to present users with an ordered list of coupons that are sorted by relevance [9], allowing users to actively search for the preferred options. In this case, users are explicitly searching and asking for these coupons; hence, this scenario is referred to as pull.

Conversely, the concept of mobile push is more closely related to display advertising through which users are being targeted either depending on their browsing behavior (behavioral targeting) or through the context of the website (contextual targeting) [27]; the user’s proximity to a location is a key targeting factor in mobile push approaches [36]. In this case, users are not explicitly asking for these coupons, which are automatically pushed out to them (based on a variety of targeting criteria). In addition, most mobile push noti<sup>fi</sup>cations do not require a sophisticated interface design because they are standardized via the operating system (i.e., iOS or Android). Mobile push noti<sup>fi</sup>cations also rarely include more than one speci<sup>fi</sup>c coupon and, thus, do not require a ranking mechanism. Therefore, compared with location-based pull couponing, sending push noti<sup>fi</sup>cations to users is a very di<sup>f</sup>erent phenomenon. Thus, although previous research has focused on mobile push, a gap remains in the literature about the unique aspects of mobile (location-based) pull coupons with regard to the interplay between the users responses to coupons and the interface design that makes use of distance information and distance-based rankings. For <sup>fi</sup>rms, it is also important to learn about the behavioral aspects necessary to optimize the e<sup>f</sup>ectiveness of location-based coupon campaigns via the device’s interface.

The aim of this paper is to study and quantify the impact of an app’s interface-speci<sup>fi</sup>c choice architecture — via distance-based ranking and the provision of distance information — on the e<sup>f</sup>ectiveness of location-based coupons, by answering the following research questions:

Research Question 1 (RQ1): What is the most efective interface design for location-based pull coupons and how do users’ responses depend on their geographic location?

Research Question 2 (RQ2): How does the magnitude of distance and ranking efects difer depending on the interface design?

To address these research questions, we conduct a large-scale randomized <sup>fi</sup>eld experiment followed by a series of descriptive and model-based analyses. We employ model-free signi<sup>fi</sup>cance tests for the analyses of the <sup>fi</sup>rst research question on the interface-design speci<sup>fi</sup>c di<sup>f</sup>erences and location-speci<sup>fi</sup>c heterogeneity in users’ responses. The analysis of the second research question is based on a hierarchical Bayes model that is used to estimate the e<sup>f</sup>ects of distance and display rank, as well as their di<sup>f</sup>erences between interface designs (i.e., experimental treatment groups).

The setting of the paper is a popular location-based pull coupon smartphone application. The application provides a newsfeed-like list of coupons sorted in real time by their distance between the store and user. The distance is calculated by using data on the smartphones’ GPS locations. We employed a <sup>fi</sup>eld experiment to manipulate the application’s interface design. The <sup>fi</sup>eld experiment was conducted over 14 weeks (between November 2012 and February 2013). Our dataset consists of 399,913 observations from 4,364 unique users. The dataset also includes 3,499 di<sup>f</sup>erent coupons o<sup>f</sup>ered by 3,930 di<sup>f</sup>erent stores in 2,392 ZIP code areas in Germany. The available coupons can be classi<sup>fi</sup>ed as (1) discount coupons with a monetary discount and (2) promotion coupons without monetary discounts. The latter can be considered as advertising by informing users of a store’s existence [17]. In our model, for both types of coupons, we analyze the users’ responses as a function of interface design, distance, display rank, and discount depth as well as that of a broad array of additional covariates, such as time, product category, and previous usage behavior.

## Literature Review

Mobile couponing, as a subset of mobile advertising, is still a fairly new topic covered only by a few studies in previous literature. Table 1 shows a summary of the relevant prior studies.

The early studies on mobile coupons focused on survey-based approaches to analyze the consumers’ intention to redeem coupons (e.g., [15]), their usage probability (e.g., [33]), and the perceived e<sup>f</sup>ectiveness of di<sup>f</sup>erent targeting methods [44]. More recent literature has almost exclusively focused on mobile push approaches, often with a location component. For example, Andrews et al. [5] investigated how commuters in subways responded to push-based mobile ads. In a similar study, Ghose et al. [24] analyzed the di<sup>f</sup>erences between commuters and non-commuters in responses to mobile coupons. Luo et al. [36] used a <sup>fi</sup>eld experiment to estimate the impact of temporal and geographical distance — induced by mobile push noti<sup>fi</sup>cations — on the response to discounted movie tickets. In a related study, Fong et al. [20] investigated the response to mobile promotions for movie tickets targeted at consumers in the vicinity of a competing cinema, a strategy referred to as geo-conquesting. Dubé et al. [16] replicated this study and found that the returns to geo-conquesting were reduced when a competitor also implements a mobile targeting campaign. Fang et al. [18] analyzed whether mobile promotions that are triggered by geo-fences — promotions sent when a consumer enters a prede<sup>fi</sup>ned area around the promoting store — were more e<sup>f</sup>ective than those received without triggering by geo-fences. Danaher et al. [13] used observational data to analyze how mobile coupons — sent out to visitors of a mall — in<sup>fl</sup>uence the purchase behavior of these visitors and found temporal and in-mall location e<sup>f</sup>ects on coupon response. Li et al. [34] investigated the impact of weather and found that sunny weather increased the consumers’ response likelihood to push noti<sup>fi</sup>cations, while rainy weather decreased consumers’ response.

Comparison of this study to relevant prior research

<table><tr><td>Study</td><td>Coupon Model</td><td>Field Exp.</td><td>Distance Info</td><td>Ranking</td><td>Location-dependent Treatment</td><td>Product Categories</td><td>Spatial Scope</td></tr><tr><td>This Study</td><td>Pull</td><td>√</td><td>√</td><td>√</td><td>√</td><td>13</td><td>3,930 Stores; 2,392 ZIP code areas</td></tr><tr><td>Andrews et al. [5]</td><td>Push</td><td></td><td></td><td></td><td></td><td>2</td><td>1 City</td></tr><tr><td>Li et al. [34]</td><td>Push</td><td>√</td><td></td><td></td><td></td><td>1</td><td>344 Cities</td></tr><tr><td>Danaher et al. [13]</td><td>Push</td><td></td><td></td><td></td><td></td><td>4</td><td>38 Stores in 1 Mall, 1 City</td></tr><tr><td>Dubé et al. [16]</td><td>Push</td><td>√</td><td></td><td></td><td></td><td>1</td><td>2 Theaters, 1 City</td></tr><tr><td>Fang et al. [18]</td><td>Push</td><td>√</td><td></td><td></td><td>√</td><td>1</td><td>1 Theater in 1 Mall, 1 City</td></tr><tr><td>Fong et al. [20]</td><td>Push</td><td>√</td><td></td><td></td><td>√</td><td>1</td><td>1 Theater in 1 Mall, 1 City</td></tr><tr><td>Ghose et al. [24]</td><td>Push</td><td></td><td></td><td></td><td></td><td>1</td><td>1 City</td></tr><tr><td>Luo et al. [36]</td><td>Push</td><td>√</td><td></td><td></td><td>√</td><td>1</td><td>4 Theaters, 1 City</td></tr></table>

Notes: We did not include survey-based studies such as [15], [33], as well as [44] in this review.

In contrast to previous studies, we measure the e<sup>f</sup>ectiveness of a di<sup>f</sup>erent coupon delivery mechanism — location-based mobile pull — by using a large and novel randomized <sup>fi</sup>eld experiment that includes a great variety of product categories (13) and a great variety of stores and geographies (3,930 stores in 2,392 ZIP code areas). Unlike the previous literature, this approach allows us to investigate and vary the mechanism’s interface design. More speci<sup>fi</sup>cally, the interface design re<sup>fl</sup>ects the presence of multiple coupons, enabling us to implement rankings that are informed by distance. This approach contrasts with mobile push coupons that are usually standardized by the operating system’s message design and that rarely include more than one coupon.

## Theoretical Background

The implementation of mobile pull-based choice interfaces requires the consideration of speci<sup>fi</sup>c design mechanisms that govern the presentation of coupons on smartphones. Speci<sup>fi</sup>cally, a key aspect of mobile pull coupons is that users can proactively search and choose between a variety of available campaigns that are presented by mobile coupon providers [22]. As a result, the users’ choices strongly depend on the manner in which coupon-speci<sup>fi</sup>c information is being presented [31]. Thus, the app’s choice architecture can in<sup>fl</sup>uence the users’ decisions. This observation is why knowledge about the actual design of the interface-speci<sup>fi</sup>c choice architecture is also crucial for location-based pull coupon applications. The two main factors that inform the underlying choice architecture via the interface design are the availability of a ranking mechanism in combination with distance (location) information. We therefore discuss the theoretical background of both aspects based on previous studies on ranking and distance e<sup>f</sup>ects.

## Ranking E<sup>f</sup>ects

Previous studies in e-commerce have shown that consumers discover products mainly through the use of search engines (e.g., [23]). Most search engines use rankings to present their results to users [45]. Relevance-based rankings aim to reduce the search costs for consumers by allowing them to <sup>fi</sup>nd a product more quickly. Previous studies on the consumers’ search and choice behavior in the context of search engines have revealed strong ranking e<sup>f</sup>ects (e.g., [23]), which are manifested by a preference towards easily accessible (i.e., highly ranked) choice options. In particular, the literature on sponsored search advertising indicates that highly sorted options provide an economic bene<sup>fi</sup>t evidenced by the interplay between top-positioned search results and an increasing numbers of clicks and conversions [2, 25]. Higher-sorted coupons receive more attention by consumers because these coupons are often assumed to be more relevant [45], a phenomenon that is also denoted as the primacy e<sup>f</sup>ect [37].

It has been shown that the ranking e<sup>f</sup>ect is stronger for mobile users than for PC users, ostensibly due to the device-speci<sup>fi</sup>c display size [22]; to view information on smaller screens requires the user to exert comparably higher cognitive e<sup>f</sup>orts [6], sometimes also referred to as search costs. However, the e<sup>f</sup>ect of rankings on choice can be endogenous if, consistent with a standard practice of the search engines’ ranking algorithms, the consumers’ prior behavior is used to inform the ranking [25]. Therefore, it is important to use a randomized experiment to test the ranking e<sup>f</sup>ects.

In a location-based context, we contribute to these studies by using various ranking mechanisms to analyze the ranking e<sup>f</sup>ects. We treat the ranking mechanisms (in combination with distance) as a design option that informs our experimental design. We test the e<sup>f</sup>ectiveness of all ranking mechanisms by comparing the mean responses between di<sup>f</sup>erent treatment groups in a large-scale randomized <sup>fi</sup>eld experiment. The ranking e<sup>f</sup>ects, as an empirical outcome of our estimation model, are applicable to all treatment groups.

## Distance E<sup>f</sup>ects

The distance between the user and the coupon-related point of sale is a natural candidate to inform rankings for location-based applications. When combining distance and rankings, coupons o<sup>f</sup>ered from nearby stores should be perceived as more relevant and, accordingly, should be ranked higher. The impact of distance, for example, spatial proximity based on the consumers’ home location, on consumer behavior has been highlighted in existing studies involving the consumers’ choices related to o<sup>fl</sup>ine retail stores [7]. The results are unambiguous: increasing distances between consumers and o<sup>fl</sup>ine stores generally decrease the likelihood of a purchase. For example, Bell et al. [7] showed that the distance between households and stores negatively in<sup>fl</sup>uences the consumers’ shopping decisions.

Recent literature has studied the role of location and distance in mobile Internet usage. Ghose et al. [22] found that distance matters more for mobile Internet usage than it matters for Internet usage via PCs. Molitor et al. [38] investigated the impact of contextual factors (e.g., distance, geographical surroundings, weather) related to mobile device usage and found that distance has a negative impact on the consumers’ choice behavior. These results indicate that location matters for mobile shoppers [26]. The reason that distance might matter more for mobile device usage (compared with PC usage) is that mobile coupon applications are used as a ubiquitous information medium with the intention to bring consumers to physical stores.

The availability of distance information itself may also have di<sup>f</sup>erent implications. Information concerning distance to stores can be assumed to be a signal of the underlying transportation costs related to di<sup>f</sup>erent coupons or store options [21]. Increasing distance thus indicates higher transportation costs that decrease a store’s attractiveness (all else being equal). However, distance information can also help consumers reduce uncertainties about where to <sup>fi</sup>nd stores or products. When considering the relationship between saliency and transparency, the same coupon without distance information (low salience and transparency) might be preferred to the one with distance information (high salience and transparency), assuming that consumers have some knowledge of the location of the coupon-related store. This expectation can be explained by the fact that in the absence of distance information, consumers tend to miscalculate the actual distance to stores. The underlying theoretical explanation can be found in overcon<sup>fi</sup>dence [14].

Overcon<sup>fi</sup>dent consumers tend to overestimate their performance on particular tasks that require abilities, such as knowledge about store distances in their local environment, and, thus, underestimate how long it takes to reach the store (i.e., they are more optimistic about the required time). This underestimation is even valid for tasks that they were confronted with in the past. Similarly, individuals tend to underestimate the probability of negative events, such as the required time to <sup>fi</sup>nish a project or to travel to a store [10]. Therefore, the same coupon for the same store at the same location might be perceived as relatively less attractive if exact distance information is provided because the saliency of actual distances and thus the transparency of transportation costs reduce the risk of overcon<sup>fi</sup>dence. However, this phenomenon is only assumed to be valid in cases where consumers have some knowledge about the location of stores.

## Moderating the Role of Geography

Previous studies in psychology and economics have shown that the choice context matters to consumers (e.g., [40]). Similarly, the perceived value of a location-based coupon may depend on the actual geographic location where users open and access their mobile coupon application. On average, there are nearer choice options available for users located in urban areas than for users located in suburbs or even in more rural areas. This <sup>fi</sup>nding also implies that transportation costs should be higher for users in suburban or rural areas because the average distance to the next store o<sup>f</sup>ering coupons is relatively high. However, the average store travel distance can be perceived as a reference point. In case this reference point is already relatively high (e.g., larger distances due to a more rural home location), a marginal increase in distance is perceived to be less negative than is a similar marginal increase based on a relatively low reference point (e.g., smaller distances due to a home location close to urban areas). More remotely located — and geographically isolated — consumers can thus be assumed to be less sensitive to distances. This argument is supported by the results from prior research. Choi and Bell [12] found that consumers with high o<sup>fl</sup>ine shopping costs — due to geographical isolation in more rural areas — are less price sensitive. Hence, the geographic location presents a contextual reference point that has to be taken into account as it can lead to heterogeneous responses.

## Randomized Field Experiment

In this section, we describe the location-based coupon application and the experimental design, report the summary statistics and provide comparisons between the experimental groups that allow us to measure the e<sup>f</sup>ectiveness of location-based mobile pull coupons.

## Location-Based Coupon Service

Our dataset stems from a location-based service provider that is part of one of the largest telecommunications companies in Europe (and the world). The provider runs a mobile application (available for iOS and Android devices) that presents context-sensitive information using the mobile devices’ GPS location. The core feature of the service is a list of store-speci<sup>fi</sup>c coupons sorted by their distances from the users’ geographic locations. After installing the application (which includes giving permission — on an opt-in basis — to track the smartphone’s location), users can start a session by actively opening the application, browsing, and obtaining information regarding coupons. The underlying search for coupons is conducted by scrolling up and down through the newsfeed-like list of coupons. At the time of the study, it was not possible to conduct a keyword or category search within the application.

The distance-based ranking of coupons contains short coupon pro<sup>fi</sup>les indicating the value of the coupon (the discount depth, if available), the distance to the store (presented in kilometers for distances greater than one kilometer; presented in meters for distances less than one kilometer), and brief information on the coupon. For example, a discount coupon might be described as “50 % O<sup>f</sup> Co<sup>f</sup>ee,” while a promotion coupon might instead be described as “Lunch for 10 € at Midtown Bar.” By clicking on the coupon pro<sup>fi</sup>le, users can respond to coupons. We use these clicks as a measure of the users’ revealed preferences toward the coupon, which can only be redeemed in participating o<sup>fl</sup>ine stores (or restaurants). The coupons are o<sup>f</sup>ered by a broad array of di<sup>f</sup>erent <sup>fi</sup>rms, such as retail stores, barbershops or restaurants, in various product categories.

This mobile application exhibits the key aspects of location-based pull advertising: coupons displayed with real-time distance information as an ordered list of coupons which are sorted by distance.<sup>4</sup> In general, distance-based rankings are an important design option for displaying content and ads with an explicit o<sup>fl</sup>ine component (e.g., Yelp, Foursquare, TripAdvisor, or Groupon).

## Experimental Design

In the <sup>fi</sup>eld experiment, we experimentally manipulated the two key aspects of locationbased pull coupons: the provision of distance information and the ranking mechanism. For a period of 14 weeks, the collaborating coupon provider agreed to randomly assign new users (who downloaded the focal application for the <sup>fi</sup>rst time) to four experimental groups. This approach ensured that only new users without prior experience with the design and mechanism of the application were included in the experiment.<sup>5</sup> These users were exclusively assigned to one treatment group (between-subjects experimental design).<sup>6</sup> The users also had no information about the existence of other treatment groups.

The ability to disentangle and test the impact of distance-based rankings and the provision of distance information was provided by a full factorial 2 x 2 design that yielded four experimental groups: “coupons sorted by distance, with distance information” (Group 1; this is the provider’s usual design); “randomly sorted coupons, with distance information” (Group 2); “coupons sorted by distance, without distance information” (Group 3); and “randomly sorted coupons, without distance information” (Group 4). Randomly sorted coupons hereby indicate that coupons in Groups 2 and 4 were randomly sorted within an interval of 50 km of a user’s location. In contrast, coupons in Groups 1 and 3 were sorted by distance in ascending order with the closest store displayed <sup>fi</sup>rst. Omitting distance information (Groups 3 and 4) induces uncertainty about actual distances but also makes transportation costs less salient; randomly sorted coupons instead of coupons sorted by distance decreases the relevancy of the ranking mechanism. Users may have basic knowledge about the approximate location of local stores. Therefore, random sorting (Group 4) can exhibit less relevance than can distance-based sorting (Group 3) even without distance information in both groups. Figure 1 depicts screenshots of all four treatment groups.

In total, 4,364 users participated in the <sup>fi</sup>eld experiment. Each participant was randomly assigned to one of the four treatment groups: 1,317 to Group 1, 1,011 to Group 2, 1,036 to Group 3, and 1,000 to Group 4.<sup>7</sup> The underlying randomization process was solved by a server-side allocation mechanism (i.e., participants did not have the ability to select into a particular treatment group for themselves). Furthermore, the server-side manipulation ensured that users remained in the same experimental group throughout the entire experiment.

## Data Description

Our dataset consists of 399,913 impressions (observations) based on the visits of 4,364 unique users in 30,779 sessions. Similar to impressions in online advertising, mobile impressions are based on the number of coupons displayed on the participants’ smartphones. Table 2 reports the summary statistics of all variables based on <sup>fi</sup>rst 25 coupons (ranks). Our focal variables are the distance to the o<sup>fl</sup>ine redemption point (measured in kilometers), the display rank, and the discount depth (measured as a relative discount). The variable coupon type denotes the coupons’ classi<sup>fi</sup>cation: the coupons are either classi<sup>fi</sup>ed as discount coupons with a monetary discount or promotion coupons without a monetary discount. The time-speci<sup>fi</sup>c e<sup>f</sup>ects are covered by the time of the day (morning, afternoon, evening, night), weekday (vs. weekend), and week. The coupon-speci<sup>fi</sup>c control variables include the product category (such as clubs, bars, and restaurants) and the expiration date (the number of days until a coupon expires). We also consider the number of impressions per session as a proxy for the users’ search depth/intensity as well as the number of previous clicks (before the current session) as an approximation of the users’ previous experience.

![](/api/attachments/FAPPVVHC/fulltext/images/1c4b498f2a64680f49a9c283ce73a012c48bd686fafc8cca24f90c31e1667b62.jpg)  
Screenshots of experimental design.

Summary statistics.

<table><tr><td>Variable</td><td>Mean</td><td>SD</td><td>Min</td><td>Max</td></tr><tr><td>Distance (in kilometers)</td><td>8.523</td><td>10.944</td><td>0</td><td>50</td></tr><tr><td>Display_Rank</td><td>10.465</td><td>6.876</td><td>1</td><td>25</td></tr><tr><td>Discount (relative)</td><td>0.054</td><td>0.207</td><td>0</td><td>1</td></tr><tr><td>Group $1^a$ </td><td>0.287</td><td>0.452</td><td>0</td><td>1</td></tr><tr><td>Group $2^a$ </td><td>0.241</td><td>0.428</td><td>0</td><td>1</td></tr><tr><td>Group $3^a$ </td><td>0.233</td><td>0.423</td><td>0</td><td>1</td></tr><tr><td>Group $4^a$ </td><td>0.239</td><td>0.426</td><td>0</td><td>1</td></tr><tr><td>Coupon_Type $^{a,b}$ </td><td>0.116</td><td>0.320</td><td>0</td><td>1</td></tr><tr><td>Impression_Session</td><td>14.180</td><td>6.844</td><td>1</td><td>25</td></tr><tr><td>Previous_Clicks</td><td>1.679</td><td>3.703</td><td>0</td><td>48</td></tr><tr><td>Expiration (in days)</td><td>148.012</td><td>160.329</td><td>0</td><td>624</td></tr><tr><td>Night (12am-5:59am) $^a$ </td><td>0.062</td><td>0.242</td><td>0</td><td>1</td></tr><tr><td>Morning (6am-11:59am) $^a$ </td><td>0.241</td><td>0.428</td><td>0</td><td>1</td></tr><tr><td>Afternoon (12pm-5:59pm) $^a$ </td><td>0.359</td><td>0.480</td><td>0</td><td>1</td></tr><tr><td>Evening (6pm-11:59pm) $^a$ </td><td>0.338</td><td>0.473</td><td>0</td><td>1</td></tr><tr><td>Weekday $^a$ </td><td>0.746</td><td>0.435</td><td>0</td><td>1</td></tr><tr><td>Barber $^a$ </td><td>0.024</td><td>0.154</td><td>0</td><td>1</td></tr><tr><td>Beauty &amp; Wellness $^a$ </td><td>0.063</td><td>0.244</td><td>0</td><td>1</td></tr><tr><td>Cafes $^a$ </td><td>0.039</td><td>0.193</td><td>0</td><td>1</td></tr><tr><td>Car $^a$ </td><td>0.005</td><td>0.068</td><td>0</td><td>1</td></tr><tr><td>Clubs &amp; Bars $^a$ </td><td>0.017</td><td>0.129</td><td>0</td><td>1</td></tr><tr><td>Education &amp; Culture $^a$ </td><td>0.126</td><td>0.332</td><td>0</td><td>1</td></tr><tr><td>Grocery $^a$ </td><td>0.101</td><td>0.301</td><td>0</td><td>1</td></tr><tr><td>Fashion &amp; Accessories $^a$ </td><td>0.066</td><td>0.249</td><td>0</td><td>1</td></tr><tr><td>Leisure &amp; Sport $^a$ </td><td>0.143</td><td>0.350</td><td>0</td><td>1</td></tr><tr><td>Living &amp; Home $^a$ </td><td>0.064</td><td>0.245</td><td>0</td><td>1</td></tr><tr><td>Multimedia $^a$ </td><td>0.151</td><td>0.358</td><td>0</td><td>1</td></tr><tr><td>Others $^a$ </td><td>0.033</td><td>0.178</td><td>0</td><td>1</td></tr><tr><td>Restaurant $^a$ </td><td>0.168</td><td>0.374</td><td>0</td><td>1</td></tr></table>

Notes: N = 399,913 impressions. <sup>a</sup>Dummy variable. <sup>b</sup>Baseline: Discount coupon  
(vs. promotion coupon).

![](/api/attachments/FAPPVVHC/fulltext/images/b1527a64854c31b174cbad96f78c1486a4a4ad37dd0967a411cb3ff89bc0798f.jpg)  
Coupon categories. Notes: Ordered by number of coupon impressions. Impressions: $\aleph =$ <sup>Figure 2.</sup>399,913, Clicks: N = 5,399.

The dataset includes 3,499 di<sup>f</sup>erent coupon promotions. The coupon promotions were o<sup>f</sup>ered by 3,930 di<sup>f</sup>erent stores shops located in 2,392 ZIP code areas. Figure 2 depicts all coupon-related product categories that were available and clicked; this pattern indicates some di<sup>f</sup>erences in preferences revealed by the users clicking on particular product categories.<sup>9</sup> However, as the relative distribution of categories is similar to that in other studies that make use of Groupon data from the United States [46], it permits us to make similar arguments about the categories’ generalizability.

## E<sup>f</sup>ects of Interface Design

Figure 3 depicts the four experimental treatment groups’ average coupon click rates, which we use to address our <sup>fi</sup>rst research question. Altogether, 5,339 coupons were chosen, leading to an overall click rate of 1.35 percent on the impression-level.<sup>10</sup> The means of the aggregated click rates are signi<sup>fi</sup>cantly di<sup>f</sup>erent between treatment groups $( \chi ^ { 2 }$ $= 5 6 . 7 9 , \mathrm { p } < 0 . 0 1 )$ . The mean click rates in Groups 3 (1.53 percent) and 1 (1.42 percent) are higher than those in Groups 2 (1.27 percent) and 4 (1.16 percent). The di<sup>f</sup>erence between Groups 3 and 1 is signi<sup>fi</sup>cant $( \chi ^ { 2 } = 4 . 1 0 , \ : \mathrm { p } < 0 . 0 5 )$ , as is the di<sup>f</sup>erence Groups 1 and 3 $( \chi ^ { 2 } = 8 . 7 7 , \mathrm { p } < 0 . 0 1 )$ , between Groups 2 and $3 \ ( \chi ^ { 2 } = 2 2 . 7 1 , \mathfrak { p } < 0 . 0 1 )$ ), between Groups 2 and 4 $( \chi ^ { 2 } = 4 . 8 9 , \ : \mathrm { p } < 0 . 0 5 )$ , and between Groups 3 and 4 $( \chi ^ { 2 } = 4 8 . 1 0 , \ : \mathrm { p } < 0 . 0 1 )$ . This indicates that the most e<sup>f</sup>ective interface design for location-based coupons is based on a distance-based ranking. Comparing the click rates of our location-based coupons to those for mobile banner ads, with an average click rate of 0.33 percent [42], our pull-based setting yields a much higher percentage of choices and can thus be considered as rather high.<sup>11</sup>

The results are surprising in two aspects. First, even without distance information (Groups 3 and 4), randomly sorted coupons (Group 4) have lower click rates than coupons displayed in a distance-based ranking (Group 3). We interpret this result to indicate that users have at least a general sense of the stores’ location within a city. More than 77 percent of all participants in the experiment use the application within a range of up to 15 km, suggesting that most of the users’ activities can be attributed to one particular area or city. Put di<sup>f</sup>erently, when coupons are randomly sorted, this decreased relevancy is presumably detectable to users.<sup>12</sup> Second, the di<sup>f</sup>erences between Groups 1 and 3 indicate that the click rate is lower in cases in which distance information (sorted by distance) is shown than it is when distance information (sorted by distance) is not shown. This result may be cautiously interpreted to indicate that the less salient transportation costs led to an underestimation of the actual distance to stores in Group 3. The users hence seem to be contextually overcon<sup>fi</sup>dent, as predicted in the theory section. In addition, the average number of sessions per user is 7.05: 6.84 in Group 1, 7.29 in Group 2, 7.44 in Group 3, and 6.70 in Group 4 (F = 1.35, p > 0.1). This result shows that the attrition frequency (fewer repeat visits of the app) is not signi<sup>fi</sup>cantly higher in groups with a less relevant ranking mechanism, such as Group 4, which included random sorting and no distance information.

![](/api/attachments/FAPPVVHC/fulltext/images/065eaeba7b6c028fbe185eeb9c80d5e1eeba8b72d6c1c591c1970fe9251d0983.jpg)  
Comparison of click rates between treatment groups. Notes: N = 399,913. Margin of error: <sup>Figure 3.</sup>Group 1: 0.0014, Group 2: 0.0014, Group 3: 0.0016, Group 4: 0.0014.

Figure 4 shows more detailed between-group di<sup>f</sup>erences based on the click rate at the display rank level. These results shed further light on the stark contrast between distancebased rankings (Groups 1 and 3) and random rankings (Groups 2 and 4). If coupons are sorted by distance, there is a stronger di<sup>f</sup>erence between the click rates per display rank (resembling a discrete exponential distribution), indicating a stronger importance of the distance-based ranking. In contrast, if coupons are randomly sorted, the click rates per display rank are almost uniformly distributed. For Group 2, this <sup>fi</sup>nding can be explained by the availability of distance information as a key factor for coupon choice, which is then largely independent of the display rank. Even without distance information (Group 4), unlike the dominant negative role of display ranks in other studies, in our study, the rank order itself does not seem to be the users’ dominating choice heuristic [45]. This result indicates that the importance of distance and display rank depends on the choice context.

![](/api/attachments/FAPPVVHC/fulltext/images/166cb61d5d6491c3f9b4abd4360aede1295536a7ae319537affe2ff1e6f3cf43.jpg)  
Click rate by display rank and group. Notes: The x-axis indicates the <sup>fi</sup>rst ten display ranks for Groups 1-4.

![](/api/attachments/FAPPVVHC/fulltext/images/0f54d3186e579a57f012d01582e9e9f43de900571f7856db6a4c26d152d43d0b.jpg)  
Click rates by group and product category. Notes: A star on the respective product category <sup>Figure 5.</sup>indicates signi<sup>fi</sup>cant di<sup>f</sup>erences between groups within categories at 0.05 (p < 0.05). Speci<sup>fi</sup>cally, the di<sup>f</sup>erences in click rates between groups are signi<sup>fi</sup>cant for the following product categories: grocery, multimedia, cafes, beauty & wellness, leisure & sport, and living & home, as well as education & culture. The click rates rounded to one decimal place.

We also analyze the di<sup>f</sup>erences in click rates across groups and product categories, shown in Figure 5. The observed click pattern, indicating a higher click rate for Groups 1 and 3, also holds for many product categories. The di<sup>f</sup>erences between treatment groups are signi<sup>fi</sup>cant for the following categories: grocery, multimedia, cafes, beauty and wellness, leisure and sport, living and home as well as education and culture.

## E<sup>f</sup>ects of Interface Design and Location-Speci<sup>fi</sup>c Heterogeneity

In this section, we analyze how the geographic context a<sup>f</sup>ects the users’ coupon choices. Thus, we analyze our <sup>fi</sup>ndings by geographic locations and distinguish between the agglomeration of stores and users. This approach is a form of geographical segmentation, based on the users’ average real-time location relative to that of the stores [4, 29]. At the basic level, this approach assumes that geographic locations can be segmented by distancebased transportation costs [35], which are further presumed to be comparably similar within speci<sup>fi</sup>c geographic locations, such as city centers, as stores are mainly located in urban areas with higher store densities. Users in a trade area — as part of a speci<sup>fi</sup>c retail market agglomeration — are also assumed to shop at centrally located stores within that area. To this end, we divide the ordered distribution of mean distances to stores within the top 25 display ranks per session into three tertiles (with approximately 1/3 of all observations each) to approximate users in urban, suburban and rural areas, similar to the classi<sup>fi</sup>cation used in previous literature [39].

Figure 6 shows the click rates for each tertile and treatment group. The di<sup>f</sup>erences between groups are signi<sup>fi</sup>cant (Urban: $\chi ^ { 2 } = 1 4 . 0 6 .$ , p < 0.01; Suburban: $\bar { \chi } ^ { 2 } = \bar { 3 } 1 . 1 8 , \mathrm { p } < 0 . 0 1 ; \mathrm { R u r a l : } \chi ^ { 2 } =$ $5 0 . 7 6 , \mathrm { p } < 0 . 0 1 )$ . Tertile 1 includes all mean store distances between 0.01 and 2.71 km, and we refer to the users’ respective locations in this interval as “Urban” because proximate stores can mostly be found in densely populated areas (as is the case in most European cities). Tertile 2 includes all mean store distances between 2.72 and 8.68 km, and we refer to the users locations as “Suburban.” Tertile 3 includes all mean store distances between 8.69 and 50 km, and we refer to the users’ locations as “Rural.” We <sup>fi</sup>nd that treatment-speci<sup>fi</sup>c click rates di<sup>f</sup>er depending on the users’ geographical locations as indicated by the tertiles. Group 1, the default group, performs particularly ine<sup>f</sup>ectively in urban areas (Tertile 1, see Figure 6). Distance information in combination with distance-based rankings seems to be less informative if the di<sup>f</sup>erences between distances are rather small. This may be explained by better informed users as well as by more competition based on higher store densities in Tertile 1 (“Urban”). In contrast, close distances seem to be more informative if the coupons are sorted randomly (both in Groups 2 and 4) and/or if distance information is omitted (Groups 3 and 4). Figure 6 also shows that coupons in suburban (Tertile 2) and rural (Tertile 3) areas are more e<sup>f</sup>ective in treatment groups, such as Groups 1 and 3, which make use of distance-based rankings. The users’ sensitivity to distance thus seems to be context dependent. The results are consistent with the assumption that due to their higher average store travel distances, users in more remote locations tend to be more accepting of higher transportation costs. Users in more remote locations (rural vs. urban areas) thus appear to be comparably more inclined to respond to location-based coupons.

![](/api/attachments/FAPPVVHC/fulltext/images/7f464caa92a7dc10f4464614d3dc5bf47b04dc15d524671005ddb883492a0a14.jpg)  
Click rates by tertile (Top 25 ranks). Notes: $\mathsf { N } = 3 9 9 , 9 1 3 .$ . The order of the depicted groups is <sup>Figure 6.</sup>based on the experimental design – the adjacent Groups 1 and 3 are sorted by distance; conversely, Groups 2 and 4 are randomly sorted.

## Econometric Analysis

This section outlines our econometric model and describes the underlying estimation process.

## Model

We use a logit model to analyze the users’ coupon choices. Speci<sup>fi</sup>cally, the use of a hierarchical Bayesian logit model with mixed e<sup>f</sup>ects including Markov chain Monte Carlo (MCMC) methods enables us to control for the users’ individual-level heterogeneity [3]. The logit model in the hierarchical Bayes framework is based on the panel data approach introduced by Chib and Carlin [11]. In our model, a user is assumed to choose the utility-maximizing coupon option. Users reveal their coupon-speci<sup>fi</sup>c preferences by clicking on coupons. We model user i’s utility U as follows [43]:

$$
U _ {i j t} = \nu_ {i j t} + \varepsilon_ {i j t}\tag{1}
$$

$$
y _ {i j t} = 1 \text {   if   } U _ {i j t} > 0\tag{2}
$$

$$
y _ {i j t} = 0 \text {   if   } U _ {i j t} \leq 0\tag{3}
$$

The deterministic part of equation (1) is represented by $\nu _ { i j t }$ whereas the stochastic component is represented by $\varepsilon _ { i j t } .$ The stochastic part contains nonsystematic or random factors that a<sup>f</sup>ect the utility U. If users are browsing within the application, they choose a coupon only if the underlying utility U is greater than 0. Speci<sup>fi</sup>cally, the users’ direct responses are represented by the latent response variable $y _ { i j t } = 1$ if user i decides to choose coupon j at time t; otherwise, $y _ { i j t } = 0$

We model the users’ coupon choice probability as a function of user-speci<sup>fi</sup>c, couponspeci<sup>fi</sup>c, location-speci<sup>fi</sup>c, and time-speci<sup>fi</sup>c variables. We thereby aim to measure the impact of distance, display rank, and their treatment-speci<sup>fi</sup>c di<sup>f</sup>erences, based on the interactions between distance, rank and treatment groups on the users’ responses to coupons. We also account for the treatment groups, discount, coupon type (discount vs. promotion coupon), number of previous clicks, search depth (the number of impressions per session), product category, time of day, weekday or weekend, week, and coupon expiration. The number of previous clicks and the search depth are included in the model to control for the users’ experience as well as the usage intensity of the application. Controlling for the available product categories also helps us to account for categoryspeci<sup>fi</sup>c coupon preferences. Furthermore, the time of day, weekday, and week dummy variables allow us to control for time-speci<sup>fi</sup>c e<sup>f</sup>ects.<sup>13</sup> In our model, the probability of user i choosing coupon j at time t is given by the following mean function:

$$
P r _ {i j t} = \frac {\exp \left(v _ {i j t}\right)}{1 + \exp \left(v _ {i j t}\right)}\tag{4}
$$

with the underlying utility of user i based on a Bernoulli distributed logit link function [11]

$$
U _ {i j t} = X _ {i j t} \beta + W _ {i j t} b _ {i} + \varepsilon_ {i j t} w i t h v _ {i j t} = X _ {i j t} \beta + W _ {i j t} b _ {i}\tag{5}
$$

$$
b _ {i} \sim N _ {q} (0, D)\tag{6}
$$

where $X _ { i j t }$ is a matrix of right-hand side covariates, and $\beta$ is a vector of <sup>fi</sup>xed e<sup>f</sup>ects. Similarly, $W _ { i j t }$ is another matrix of right-hand side covariates, and $b _ { i }$ is a vector of individual-speci<sup>fi</sup>c random-e<sup>f</sup>ects: $b _ { i } \sim N _ { \mathrm { q } } ( 0 , D )$ and $\varepsilon _ { i j t }$ are error vectors that are independent and identically distributed based on a type I extreme value distribution.<sup>14</sup> The hierarchical speci<sup>fi</sup>cation of the mixed model in Equation (5) is completely denoted by the following prior distributions $\bar { D } ^ { - 1 } \sim \bar { W ( \nu _ { 0 } { } ^ { - 1 } R _ { o } , \nu _ { O } ) , \stackrel { - } { \sigma } } \sigma ^ { - 2 } \sim G ( \nu _ { o } / 2 , \delta _ { o } / 2 )$ and $\beta \sim N _ { p } ( \beta _ { o } , B _ { o } )$ where W denotes the Wishart distribution of the random e<sup>f</sup>ects-speci<sup>fi</sup>c precision matrix, G denotes the Gamma distribution of the conditional error vector, and N denotes the normal distribution of the <sup>fi</sup>xed-e<sup>f</sup>ects parameters. The mean of the Wishart prior is $R _ { O } ,$ whereas the Gamma prior mean is $\nu _ { o } / \delta _ { o }$ [11].

Based on the general formulation of our model in Equation (5), we can specify the random and <sup>fi</sup>xed-e<sup>f</sup>ects matrices by adding the full set of explanatory right-hand side covariates for $X _ { i j t }$ and $W _ { i j t }$ . We apply <sup>fi</sup>xed and random e<sup>f</sup>ects for distance, display rank, and discount depth, as we assume individual-level heterogeneity based on the users’ idiosyncratic preferences related to their responses to the experimental variation as well as discount depth. All the other variables are only estimated as <sup>fi</sup>xed e<sup>f</sup>ects.

## Estimation

We estimate our mixed-e<sup>f</sup>ects hierarchical Bayesian model by using Markov chain Monte Carlo methods with a Gibbs sampling algorithm from the posterior distribution. We run the Markov Chain for 25,000 iterations and use the last 20,000 iterations to calculate the posterior means and standard deviations and report the 95 percent posterior interval. To increase the estimation e<sup>fi</sup>ciency, we use a thinning parameter of 20 (i.e., keeping every $2 0 ^ { \mathrm { t h } }$ draw for the posterior distribution).

## Results

In this section, we present our estimation results and predict the click rates based on alternative coupon speci<sup>fi</sup>cations.

## Estimation Results

Table 3 presents the posterior means of our estimation results (based on top 25 display ranks).<sup>15</sup> Geographical distance has a signi<sup>fi</sup>cant negative impact on the probability of choosing coupons $( \beta = - 0 . 1 8 3 ; \ p < 0 . 0 5 )$ . Increasing distances between stores and the users’ realtime location are assumed to increase the underlying transportation costs, which has a negative impact on the users’ preferences toward these stores [7], as they have to travel to a store to make use of a chosen coupon.

Model results (Top 25 ranks).

<table><tr><td rowspan="2">Variables</td><td colspan="4">Full Model</td></tr><tr><td>Posterior Mean</td><td>S.D.</td><td colspan="2">95 % Posterior Interval</td></tr><tr><td>Intercept</td><td>-2.479*</td><td>0.212</td><td>-2.915</td><td>-2.082</td></tr><tr><td>Distance</td><td>-0.183*</td><td>0.057</td><td>-0.286</td><td>-0.069</td></tr><tr><td>Display_Rank</td><td>-0.354*</td><td>0.047</td><td>-0.451</td><td>-0.268</td></tr><tr><td>Discount</td><td>0.351*</td><td>0.119</td><td>0.103</td><td>0.561</td></tr><tr><td>Group $2^a$ </td><td>0.138</td><td>0.150</td><td>-0.154</td><td>0.432</td></tr><tr><td>Group $3^a$ </td><td>-0.049</td><td>0.147</td><td>-0.312</td><td>0.242</td></tr><tr><td>Group $4^a$ </td><td>-0.001</td><td>0.166</td><td>-0.331</td><td>0.308</td></tr><tr><td>Distance×Group $2^b$ </td><td>-0.330*</td><td>0.071</td><td>-0.464</td><td>-0.192</td></tr><tr><td>Distance×Group $3^b$ </td><td>-0.073</td><td>0.077</td><td>-0.220</td><td>0.082</td></tr><tr><td>Distance×Group $4^b$ </td><td>-0.276*</td><td>0.074</td><td>-0.415</td><td>-0.130</td></tr><tr><td>Rank×Group $2^b$ </td><td>0.239*</td><td>0.061</td><td>0.116</td><td>0.351</td></tr><tr><td>Rank×Group $3^b$ </td><td>0.098</td><td>0.061</td><td>-0.015</td><td>0.220</td></tr><tr><td>Rank×Group $4^b$ </td><td>0.225*</td><td>0.057</td><td>0.119</td><td>0.335</td></tr><tr><td>Coupon_Type $^c$ </td><td>-0.598*</td><td>0.085</td><td>-0.760</td><td>-0.424</td></tr><tr><td>Impression_Session</td><td>-0.657*</td><td>0.038</td><td>-0.732</td><td>-0.584</td></tr><tr><td>Previous_Clicks</td><td>-0.468*</td><td>0.033</td><td>-0.529</td><td>-0.398</td></tr><tr><td>Morning $^d$ </td><td>-0.146</td><td>0.093</td><td>-0.319</td><td>0.037</td></tr><tr><td>Afternoon $^d$ </td><td>-0.272*</td><td>0.097</td><td>-0.448</td><td>-0.087</td></tr><tr><td>Evening $^d$ </td><td>-0.133</td><td>0.090</td><td>-0.304</td><td>0.046</td></tr><tr><td>Expiration (in days)</td><td>-0.115*</td><td>0.012</td><td>-0.138</td><td>-0.093</td></tr><tr><td>Weekday</td><td>-0.173*</td><td>0.045</td><td>-0.262</td><td>-0.085</td></tr><tr><td>Beauty &amp; Wellness $^e$ </td><td>0.300*</td><td>0.118</td><td>0.061</td><td>0.501</td></tr><tr><td>Cafes $^e$ </td><td>0.550*</td><td>0.150</td><td>0.288</td><td>0.852</td></tr><tr><td>Care</td><td>0.466</td><td>0.239</td><td>-0.001</td><td>0.932</td></tr><tr><td>Clubs &amp; Bars $^e$ </td><td>0.442*</td><td>0.166</td><td>0.126</td><td>0.761</td></tr><tr><td>Education &amp; Culture $^e$ </td><td>-0.289*</td><td>0.138</td><td>-0.555</td><td>-0.031</td></tr><tr><td>Grocery $^e$ </td><td>0.781*</td><td>0.128</td><td>0.545</td><td>1.028</td></tr><tr><td>Fashion &amp; Accessories $^e$ </td><td>0.517*</td><td>0.137</td><td>0.273</td><td>0.789</td></tr><tr><td>Leisure &amp; Sport $^e$ </td><td>-0.029</td><td>0.130</td><td>-0.283</td><td>0.219</td></tr><tr><td>Living &amp; Home $^e$ </td><td>-0.242</td><td>0.150</td><td>-0.495</td><td>0.078</td></tr><tr><td>Multimedia $^e$ </td><td>0.705*</td><td>0.123</td><td>0.481</td><td>0.938</td></tr><tr><td>Restaurant $^e$ </td><td>0.746*</td><td>0.129</td><td>0.513</td><td>0.997</td></tr><tr><td>Others $^e$ </td><td>0.281*</td><td>0.146</td><td>0.021</td><td>0.563</td></tr><tr><td>N</td><td></td><td>399,913</td><td></td><td></td></tr><tr><td>Deviance</td><td></td><td>41,900</td><td></td><td></td></tr></table>

\* Signi<sup>fi</sup>cant at 0.05 (zero does not lie in the 95 % posterior interval); dependent variable: coupon choice. Notes: The variables Distance, Display\_Rank, Impression\_Session, Previous Clicks and Expiration are logtransformed. This also includes the interaction terms based on Distance and Display\_Rank. Time (weekly) dummies are included in the estimation. The term “Baseline” refers to the baseline variable of a speci<sup>fi</sup>c coe<sup>fi</sup>cient category. The estimated coe<sup>fi</sup>cients of each speci<sup>fi</sup>c category have to be interpreted in comparison to their baseline variable, indicating the comparative impact on coupon choice. <sup>a</sup>Baseline: Group1. <sup>b</sup>Baseline: Distance/Rank×Group1. <sup>c</sup>Baseline: Discount coupon (vs. promotion coupon). <sup>d</sup>Baseline: Night, <sup>(e)</sup> Baseline: Barbershops. The di<sup>f</sup>erence between the coe<sup>fi</sup>cients Distance × Group2 and Distance × Group4 are signi<sup>fi</sup>cantly di<sup>f</sup>erent from each other $( \mathrm { t } = 1 6 . 7 3 , \ \mathsf { p } < 0 . 0 1 )$ . As the coe<sup>fi</sup>cients are based on posterior distributions (described by the posterior mean and standard deviation) that are generated during the estimation process, this is done by comparing the posterior distributions of both coe<sup>fi</sup>cients.

Similarly, we <sup>fi</sup>nd that display rank has a negative impact on the users’ coupon response behavior $( \beta = - 0 . 3 5 4 ; \mathrm { ~ p ~ < ~ } 0 . 0 5 )$ . The further down a coupon is displayed (numerically increased display rank), the lower the probability of users choosing that coupon. Ghose et al. [22] found a comparable result, which was explained by an increased cognitive load — sometimes referred to as search costs — related to the screen size and requiring more scrolling to discover lower-ranked coupons.

The interactions between distance and treatment groups show that users’ sensitivity to distances becomes more negative when coupons are sorted randomly (i.e., Groups 2 and 4) than when the default distance-based ranking for coupons is employed (i.e.,

Group 1). This result suggests that distances to stores are an important driver of coupon response: randomly sorted coupons increase the negative impact of geographical distance. More precisely, for randomly sorted coupons, the distance e<sup>f</sup>ect is slightly more negative if the distance information is provided (Distance×Group2: $\beta = - 0 . 3 3 0 ; \mathrm { p } < 0 . 0 5 )$ but still signi<sup>fi</sup>cant without distance information (Distance×Group4: $\beta = - 0 . 2 7 6 ; \mathtt { p } < 0 . 0 5 )$ . These results re<sup>fl</sup>ect the descriptive results from Figure 4; the distance-based click rates in Groups 1 and 3 indicate substantial di<sup>f</sup>erences between ranks, whereas the random sorting-based click rates in Groups 2 and 4 are almost uniformly distributed, demonstrating less rank-speci<sup>fi</sup>c di<sup>f</sup>erences in click rates. One cautious explanation for this <sup>fi</sup>nding is that users are not just selecting top-ranked coupons; as re<sup>fl</sup>ected in the estimation results, the users care about the transportation costs based on the (more or less salient) distances to stores. For Group 2, this e<sup>f</sup>ect might be increased by the presence of distance-based contrast e<sup>f</sup>ects [40] between adjacent and randomly sorted coupons (i.e., 100 m vs. 1 km is a larger contrast than 100 m vs. 200 m).<sup>16</sup> Comparably closer store locations seem to be more attractive in this scenario. For Group 4, we also assume that users respond more positively to stores they recognize from their local environment once these stores appear in their coupon feed.

Further, the signi<sup>fi</sup>cant interactions between display rank and groups can be considered as the <sup>fl</sup>ipside of the distance-based interactions. Ranking e<sup>f</sup>ects are found to be weaker not only when coupons are not sorted by distance and distance information is available (Rank×Group2: $\beta = 0 . 2 3 9 ; \mathrm { p } < 0 . 0 5 )$ , but also when coupons are not sorted by distance and distance information is not available (Rank×Group4: $\beta = 0 . 2 2 5 , \mathtt { p } < 0 . 0 5 )$ . Hence, users are willing to choose lower ranked coupons (and incur higher search costs) if they stem from stores that are geographically close.

The group-speci<sup>fi</sup>c e<sup>f</sup>ects are not signi<sup>fi</sup>cant, given they are time invariant for individual users (i.e., each user remains in the same treatment group). However, the di<sup>f</sup>erences in variation between groups in terms of distance and display rank e<sup>f</sup>ects are captured by the interaction terms based on distance, display rank and treatment groups, as previously described.

Additionally, the discount depth has a positive and signi<sup>fi</sup>cant impact on the choice of discount coupons. However, promotion coupons without direct monetary impact seem to be generally preferred to discount coupons, as indicated by the negative e<sup>f</sup>ect of the coupon type variable. This <sup>fi</sup>nding may be explained by the presence of the coupons’ advertising e<sup>f</sup>ect [17], which informs users about the availability of (potentially) attractive products and stores.

We also control for the search depth via the number of impressions per session, number of previous clicks, time of day, weekday, and number of days before a coupon expires. The number of impressions per session has a signi<sup>fi</sup>cantly negative impact on the probability of choosing coupons. Similarly, the number of previous clicks — a proxy for usage experience — has a signi<sup>fi</sup>cantly negative impact on the users’ coupon choice probability.

Location-based coupons seem to be slightly more e<sup>f</sup>ective during the nighttime than during the morning, afternoon and evening. There are also signi<sup>fi</sup>cantly fewer coupon choices on weekdays versus weekends. Additionally, the fewer the number of days until a coupon expires is, the higher the probability that users will decide to choose that coupon.<sup>17</sup> This e<sup>f</sup>ect is consistent with the results of the previous studies on traditional coupon promotions [30] and can be explained by the fear of missing out.

Finally, the category-speci<sup>fi</sup>c di<sup>f</sup>erences in Table 3 indicate that users prefer coupons for the categories comprising beauty and wellness, cafes, clubs and bars, grocery, fashion and accessories, multimedia, restaurant and others than for the baseline category barbershops. Compared to the barbershop coupons, the education and culture category coupons signi<sup>fi</sup>cantly decrease the observed choice probability.

Please refer to the Online Supplemental Appendix for additional analyses as well as for robustness checks. The additional analyses focus on users’ heterogeneity regarding their usage intensity and di<sup>f</sup>erentiate between the coe<sup>fi</sup>cients of the top 15 percent of users and the rest of the user base. The robustness checks include analyses based on each user’s very <sup>fi</sup>rst login, treatment group-speci<sup>fi</sup>c results and controls for the appearance of o<sup>f</sup>ers on the <sup>fi</sup>rst screen/page of the app. Overall, our main variables — distance and display rank — remain qualitatively similar based on the sign and the statistical signi<sup>fi</sup>cance.

## Click Rate Predictions of Alternative Coupon Speci<sup>fi</sup>cations

Our model also allows us to predict the click rates based on alternative coupon speci<sup>fi</sup>cations.<sup>18</sup> This prediction is particularly valuable for coupon providers that have an interest in evaluating potential future coupon speci<sup>fi</sup>cations, including the discount depth, expiration date and product category. Overall, the predicted baseline click rate is 1.23 percent (for all groups). We <sup>fi</sup>nd that an increase of the discount depth to 50 percent (and holding everything else constant) increases the predicted click rate to 1.42 percent. Regarding product categories, we <sup>fi</sup>nd that for groceries, the predicted click rate increases to 1.70 percent, which is in stark contrast to categories, such as education and culture, yielding a predicted click rate of 0.61 percent.

Table 4 summarizes the main results of our analyses and research questions.

Summary of main results.

<table><tr><td>Research Question 1: Interface design, coupon effectiveness and location-specific heterogeneity</td></tr><tr><td>The most effective interface design includes coupons that are sorted by distance.The provision of distance information is less important when coupons are sorted by distance.Users are more likely to respond to location-based coupons in rural or suburban than urban areas.</td></tr><tr><td>Research Question 2: Magnitude of main and interface design effects</td></tr><tr><td>Main effects: Increased distances between users and stores and numerically increased display ranks on the mobile screen decrease the users&#x27; coupon choice probabilities.Interface design effects: When coupons are randomly sorted, the distance sensitivity is increased, while the display rank sensitivity is decreased.</td></tr></table>

## Concluding Discussion and Managerial Interpretation of the Results

In this paper, we quantify the impact of the interface-speci<sup>fi</sup>c choice architecture of a mobile application on the e<sup>f</sup>ectiveness of location-based pull coupons. We accomplish this goal by manipulating the core elements of the application’s interface design — the provision of distance information and distance-based ranking mechanisms — based on a randomized <sup>fi</sup>eld experiment.

Our experimental choice architecture is informed by previous information systems and marketing studies related to the context of ranking [23, 45] and distance e<sup>f</sup>ects [7, 38]. We extend prior studies on ranking and distance e<sup>f</sup>ects to the context of location-based pull coupons. Our main results are largely consistent with our theoretical expectations. However, we <sup>fi</sup>nd group-speci<sup>fi</sup>c di<sup>f</sup>erences based on the experimental interface design and location-speci<sup>fi</sup>c heterogeneities that deviate from previous studies.

The result of our <sup>fi</sup>rst research question shows coupons that are sorted by distance are the most e<sup>f</sup>ective interface design for location-based coupons, compared to randomly sorted coupons (Groups 1 and 3 vs. Groups 2 and 4). This <sup>fi</sup>nding is consistent with studies on relevance-based rankings [45]. However, the actual provision of distance information (Groups 1 and 3) tends to be less important, as users seem to be overcon<sup>fi</sup>dent [14] in the context of less salient transportation costs; and users’ overcon<sup>fi</sup>dence manifests itself in overestimating their knowledge about store distances when confronted with distance-based rankings without explicit distance information (Group 3). Our experiment thus shows that behavioral insights on overcon<sup>fi</sup>dence help explain how the interface design of an app can in<sup>fl</sup>uence individuals’ decisions, which can di<sup>f</sup>er from those based on existing utility-maximizing store-choice behavior [7].

Further, users in more remote locations (rural vs. urban areas) respond more favorably to location-based coupons. This phenomenon may be explained by the availability of more shopping alternatives in urban areas with higher store densities and a comparably higher tolerance to transportation costs in more remote locations.

In addition to the main results of negative distance and ranking e<sup>f</sup>ects, which are consistent with previous literature [22], the results of our second research question reveal deviations from the assumption of strictly negative distance and ranking e<sup>f</sup>ects [38, 22], indicating that the underlying search (via ranking) and transportation costs (via distance) are context dependent. More speci<sup>fi</sup>cally, ranking e<sup>f</sup>ects were found to be less negative if distance is not the main sorting mechanism (Groups 2 and 4). Similarly, the estimated distance e<sup>f</sup>ect is more negative when presented in the context of random rankings, a <sup>fi</sup>nding that is additionally related to the trade-o<sup>f</sup> contrast e<sup>f</sup>ect [40] that accounts for sorting-speci<sup>fi</sup>c discrepancies in distances that become more visible in this case (100 m vs. 1 km appears more striking than 100 m vs. 200 m). Distance hence seems to be more important for coupon choices compared to the display rank, indicating that distance-based transportation costs dominate ranking-based search costs when combined with random rankings.

To summarize, we extend the literature on ranking and distance e<sup>f</sup>ects by applying behavioral theories on overcon<sup>fi</sup>dence [14], trade-o<sup>f</sup> contrast heuristics, and contextdependent choices [40]. These <sup>fi</sup>ndings not only help to explain why user heterogeneity leads to deviations from previous literature but also enables <sup>fi</sup>rms to make more informed decisions as they manage location-based coupon campaigns.

## Managerial Implications

This study provides several implications for <sup>fi</sup>rms. First, our results indicate that location-based pull coupon providers can think about careful modi<sup>fi</sup>cations to a strict distance-based ranking. For example, providers could think about grouping coupons in distance buckets, such as 0–1 km and 1–2 km. Within a speci<sup>fi</sup>c bucket, providers can auction o<sup>f</sup> the speci<sup>fi</sup>c ranking slot, as done in search engine advertising campaigns, and achieve a higher click-through or impression-based price. Please note that such ranking mechanisms are very di<sup>f</sup>erent from the ranking currently applied by most coupon providers. Within distance buckets, a ranking that is not strictly based on distance should not substantially increase the disparity in the distances of the adjacent coupons. Thus, coupon providers might implement an auction mechanism to optimize the allocation of top-ranked promotions within distance buckets. Additionally, prices could di<sup>f</sup>er by the particular geographic area (e.g., urban areas vs. suburbs). In this case, real-time location information about actual usage frequencies can increase the value of area-speci<sup>fi</sup>c and ranking slots. The bidding competition would then not be based on particular coupons but instead would be based on speci<sup>fi</sup>c (highly frequented) areas.

Second, dynamic coupon pricing could be applied in combination with geo-targeting and weighted by insights into the users’ heterogeneous sensitivities to distances, rankings and discounts. Our results help stores that engage in location-based couponing to quantify the impact of distance, display rank, and discount depth on coupon choice. Based on predicted click rates, stores who partner with coupon providers have multiple tools to leverage: the real-time distance between the user and the store, the rank of the coupon on the screen, and the actual discount. For example, if a store is 1 km away from a user relative to another competing store that is 0.5 km away, then the former can still incentivize the user to come to the store by increasing the discount relative to the latter store. Similarly, if stores displayed in positions 4 and 6 on a mobile screen are close competitors, then the store with the lower (worse, numerically lower) position can increase its attractiveness by increasing the discount relative to the store that is closer to the user (if these activities are relatively close to urban areas). Thus, there is room to implement dynamic pricing strategies based on the real-time distance between a user and the store and the rank of the coupon on the screen by additionally considering users’ sensitivities to those variables.

Third, our results on ranking e<sup>f</sup>ects for distance-based rankings are closely related to the smartphones’ limited screen sizes. Smartphone displays are several inches smaller than a laptop or PC display. This small size signi<sup>fi</sup>cantly reduces the number of coupons viewable on the screen. Thus, customizing or targeting advertisements becomes more critical on a smartphone. The advertisement’s position on the mobile screen and the distance between a user and the nearest store advertised produces an interesting set of three-way interactions for marketers to exploit. Thus, although many <sup>fi</sup>rms compete for attention via coupons, a mobile screen has only limited space. Therefore, the topmost slots of a mobile screen have greater value to <sup>fi</sup>rms and can be priced at a premium. The value of the topmost slots might also inform <sup>fi</sup>rms about potential modi<sup>fi</sup>cations of the application’s interface design, which could include the implementation of <sup>fi</sup>lter buttons that enable users to sort coupons by certain criteria, such as product categories, discount depth, or expiration dates, in addition to the default distance-based ranking criteria.

Finally, our results also deliver more general insights for <sup>fi</sup>rms. As mobile marketing becomes mainstream, <sup>fi</sup>rms struggle with the question of how to e<sup>f</sup>ectively measure the impact of their campaigns. Presumably, location information can help stores achieve higher response rates for their campaigns [1]. Most importantly, managers using location to localize promotions cannot only increase their campaigns’ return on investment (ROI) but also make those campaigns better tailored and easier to measure to enable a better customer experience.

## Limitations and Future Research

Our study provides multiple avenues for future research. For example, we have no information about o<sup>fl</sup>ine purchases that would enable us to validate the users’ actual coupon redemptions, which we approximate by individual-level coupon choices. O<sup>fl</sup>ine purchase data would also allow us to estimate the precise value of each user (e.g., by calculating the customer lifetime value) or to combine sales data with GPS data to gain further insights into the users’ conversion funnel. Additionally, our analyses are based on smartphone users who are interested in coupons. It might be interesting to compare our <sup>fi</sup>ndings with <sup>fi</sup>ndings related to PC users (e.g., based on IP tracking), who must <sup>fi</sup>nd deals on a website. It is possible that user behavior di<sup>f</sup>ers based on the channel accessing the service. In our <sup>fi</sup>eld experiment, we could not manipulate discount depth. However, we observe a wide variation of di<sup>f</sup>erent coupon categories/discounts and control for product category in our empirical analyses. Moreover, the <sup>fi</sup>eld experiment was conducted over 14 weeks. Here, it might be interesting to investigate long-term e<sup>f</sup>ects, such as user learning over time. Finally, our dataset does not allow us to experimentally di<sup>f</sup>erentiate, via randomized assignment, between the impact of retargeting based on repeated exposure of the same campaign and the impact of expiration dates. This area might be another interesting avenue for future research.

## Conclusions

O<sup>fl</sup>ine retailers increasingly use location-based coupons to target consumers in their vicinity in real-time. The rationale for the use of location-based coupons is that geographic proximity increases the relevance for consumers and, thus, the e<sup>f</sup>ectiveness of these campaigns. We focus on quantifying the most e<sup>f</sup>ective interface design for the presentation of location-based coupons. Our results show that the most e<sup>f</sup>ective interface design for location-based coupons is based on a distance-based ranking. We also <sup>fi</sup>nd signi<sup>fi</sup>cant di<sup>f</sup>erences in the impact of distance and display rank based on the interface design and the actual geographic location of users. In turn, we extend the literature on ranking and distance e<sup>f</sup>ects by applying behavioral theories on overcon<sup>fi</sup>dence, trade-o<sup>f</sup> contrast heuristics, and context-dependent choices.

To conclude, this paper paves the way for future research on pull coupons in the growing and important area of location-based advertising and mobile analytics. Although the speci<sup>fi</sup>c <sup>fi</sup>ndings of our randomized <sup>fi</sup>eld experiment may not generalize to every possible location-based advertising context, the results provide a critical baseline to inform <sup>fi</sup>rms and managers about the e<sup>f</sup>ects of location-based pull coupons. Our results thus contribute to the understanding of consumers’ behavioral responses to location-based advertising and provide important implications for the interface design of location-based advertising applications.

## Notes

1. Note that mobile push noti<sup>fi</sup>cations can be transmitted via SMS or app-based noti<sup>fi</sup>cations.

2. See, for example, http://www.lsoft.com/resources/optinlaws.asp.

3. The devices’ locations are only tracked when the login is initiated. Movements while using the app are not tracked.

4. The app does not apply any sort of coupon-speci<sup>fi</sup>c customization/personalization. Previous usage behavior neither informs the future selection nor the order of coupons. The default sorting logic is distance-based.

5. Please note that the descriptions in both app stores (Apple and Google Play) only promised coupons from stores nearby and did not provide any speci<sup>fi</sup>cs about the precise information provided (e.g., exact distance) or the type of sorting.

6. It is worth noting that experiments based on individual-level randomization are less prone to unobserved heterogeneity and endogeneity [28].

7. Non-systematic (server-side) technical issues caused the disparity in group sizes. We tested the integrity of our randomization procedure by using a logit model re<sup>fl</sup>ecting the <sup>fi</sup>rst login of each user. The non-experimental control variables were used to explain the users’ allocation to each of the two treatment variables (i.e., ranking by distance versus a randomly generated ranking and location information provided versus location information not provided). We found that none of the non-experimental variables explains this allocation, thus suggesting a clean randomization procedure.

8. The expiration date of each coupon is shown after clicking on the coupon pro<sup>fi</sup>le in the coupon feed.

9. The location-based coupon provider uses its sales force to recruit stores. To this end, the sales force does not prioritize speci<sup>fi</sup>c store categories, as the provider is aiming for a highly diverse selection of coupons.

10. The raw number of clicks and impressions for each group is as follows: in Group 1, there were 1,632 clicks and 114,668 impressions; in Group 2, there were 1,230 clicks and 96,571 impressions; in Group 3, there were 1,427 clicks and 93,224 impressions; and in Group 4, there were 1,110 clicks and 95,450 impressions. Of all the clicks, 46.32 percent can be attributed to the <sup>fi</sup>rst <sup>fi</sup>ve coupons (i.e., the <sup>fi</sup>rst screen).

11. In comparison, the session-level click rate is even higher, based on a mean of 16.38 percent.

12. In Group 3, all available coupons were sorted based on the actual distance between the user and all participating stores (e.g., if the user lives next to a participating retail store, this store would be ranked <sup>fi</sup>rst/very high in Group 3). However, if the same user were assigned to Group 4 instead, there would have been a high likelihood that this participating store (and other coupons from proximate stores) would not have shown up in the top results.

13. We log-transformed all non-categorical and non-percentage scaled variables (i.e., distance, display rank, impressions per session, previous clicks and coupon expiration), given their variance in scale (see Table 2).

14. The type I extreme value distribution, also known as the Gumbel distribution, closely resembles a normal distribution, which is often the preferred distribution to characterize random errors.

15. Note that the correlation between display rank and distance is 0.135. Our experimental design also allows us to disentangle the impact of display rank from that of distance. More speci<sup>fi</sup>cally, the rank and distance correlation varies between 0.054 (Group 4) and 0.220 (Group 3). But even in Groups 1 and 3, which are “sorted by distance,” this correlation is not straightforward due to the heterogeneous nature of user locations. We additionally estimated a random-e<sup>f</sup>ect logit model based on the same sample to estimate VIFs for distance (6.53) and display rank (7.21). Both approaches indicate that collinearity does not seem to be a critical issue in our models.

16. The distance-speci<sup>fi</sup>c di<sup>f</sup>erences between adjacently displayed coupons in the app (based on the session-level mean and median distances) are signi<sup>fi</sup>cantly higher in both groups with randomly sorted coupons: the median di<sup>f</sup>erence in distance is 3.55 times higher in Groups 2 and 4 than it is in Group 1 and 3.3 times higher in Groups 2 and 4 than it is in Group 3.

17. In order to di<sup>f</sup>erentiate between the impact of expiration dates and the impact of retargeting, the possibility that a user was exposed to a speci<sup>fi</sup>c coupon more than once, we investigate the correlation between expiration date and retargeting and also estimate a model that jointly accounts for both variables. We <sup>fi</sup>nd the correlation coe<sup>fi</sup>cient to be small and close to zero $( r = - 0 . 0 1 0 , p >$ 0.05) and the estimated expiration date coe<sup>fi</sup>cient robust to the inclusion of retargeting $( \beta _ { E x p i r a t i o n D a t e } = - 0 . 1 1 2 , p < 0 . 0 5 )$ . The most desired approach to di<sup>f</sup>erentiate between the impacts of both variables would be a randomized <sup>fi</sup>eld experiment (as future research). The design of this experiment could then consist of a treatment group that only includes expirable coupons that are displayed only once, another treatment group that allows for retargeting but only includes campaigns without expiration dates, and a third treatment group that combines both expirable, and retargeted campaigns; the latter situation would be similar to our current scenario.

18. The predicted click rates are based on the estimated log odds $\hat { y } _ { i j k t }$ followed by a non-linear transformation, exp $\left( \hat { y } _ { i j k t } \right) / 1 + \exp \left( \hat { y } _ { i j k t } \right)$ , which yields the predicted click rates.

## Acknowledgments

The authors gratefully acknowledge may helpful suggestions from Thomas Otter, the participants of the Statistical Challenges in eCommerce Research Symposium (SCECR) in Lisbon, the Marketing Science Conference in Istanbul, and the INFORMS Annual Meeting in Minneapolis. We are especially thankful to Boris Lücke for his support.

## ORCID

Martin Spann http://orcid.org/0000-0003-4645-3913

## References

1. AdAge. 3 mini case studies show how location data is moving marketing. http://adage.com/ article/print-edition/case-s/308190/(accessed on June 25, 2019).

2. Agarwal, A; Hosanagar, K; and Smith, M.D. Location, location, location: an analysis of pro<sup>fi</sup>tability of position in online advertising markets. Journal of Marketing Research, 48, 6 (2011), 1057–1073.

3. Allenby, G.M.; and Ginter, J.L. Using extremes to design products and segment markets. Journal of Marketing Research, 32, 4 (1995), 392–403.

4. Anderson, S.P.; and de Palma, A. Spatial price discrimination with heterogeneous products. The Review of Economic Studies, 55, 4 (1988), 573–592.

5. Andrews, M; Luo, X; Fang, Z; and Ghose, A. Mobile ad e<sup>f</sup>ectiveness: hyper-contextual targeting with crowdedness. Marketing Science, 35, 2 (2016), 218–233.

6. Bang, Y; Lee, D.-J; Han, K; Hwang, M; and Ahn, J.-H. Channel capabilities, product characteristics, and the impacts of mobile channel introduction. Journal of Management Information Systems, 30, 2 (2013), 101–126.

7. Bell, D.R; Ho, T.-H; and Tang, C.S. Determining where to shop: <sup>fi</sup>xed and variable costs of shopping. Journal of Marketing Research, 35, 3 (1998), 352–369.

8. Biocca, F; Owen, C; Tang, A; and Bohil, C. Attention issues in spatial information systems: directing mobile users’ visual attention using augmented reality. Journal of Management Information Systems, 23, 4 (2007), 163–184.

9. Bradlow, E.T.; and Schmittlein, D.C. The little engines that could: modeling the performance of World Wide Web search engines. Marketing Science, 19, 1 (2000), 43–62.

10. Buehler, R; Gri<sup>fi</sup>n, D; and Ross, M. Exploring the “planning fallacy”: why people underestimate their task completion times. Journal of Personality and Social Psychology, 67, 3 (1994), 366–381.

11. Chib, S.; and Carlin, B.P. On MCMC Sampling in hierarchical longitudinal models. Statistics and Computing, 9, 1 (1999), 17–26.

12. Choi, J.; and Bell, D.R. Preference minorities and the internet. Journal of Marketing Research, 48, 4 (2011), 670–682.

13. Danaher, P.J; Smith, M.S; Ranasinghe, K; and Danaher, T.S. Where, when and how long: factors that in<sup>fl</sup>uence the redemption of mobile phone coupons. Journal of Marketing Research, 52, 5 (2015), 710–725.

14. DellaVigna, S. Psychology and economics: evidence from the <sup>fi</sup>eld. Journal of Economic Literature, 47, 2 (2009), 315–372.

15. Dickinger, A.; and Kleijnen, M. Coupons going wireless: determinants of consumer intentions to redeem mobile coupons. Journal of Interactive Marketing, 22, 3 (2008), 23–39.

16. Dubé, J.-P; Fang, Z; Fong, N; and Luo, X. Competitive price targeting with smartphone coupons. Marketing Science, 36, 6 (2017), 944–975.

17. Edelman, B; Ja<sup>f</sup>e, S; and Kominers, S.D. To Groupon or not to Groupon: the pro<sup>fi</sup>tability of deep discounts. Marketing Letters, 27, 1 (2016), 39–53.

18. Fang, Z; Gu, B; Luo, X; and Xu, Y. Contemporaneous and delayed sales impact of location-based mobile promotions. Information Systems Research, 26, 3 (2015), 552–564.

19. Fang, X; Chan, S; Brzezinski, J; and Xu, S. Moderating e<sup>f</sup>ects of task type on wireless technology acceptance. Journal of Management Information Systems, 22, 3 (2006), 123–157.

20. Fong, N.M; Fang, Z; and Luo, X. Geo-conquesting: competitive locational targeting of mobile promotions. Journal of Marketing Research, 52, 5 (2015), 726–735.

21. Forman, C; Ghose, A; and Goldfarb, A. Competition between local and electronic markets: how the bene<sup>fi</sup>t of buying online depends on where you live. Management Science, 55, 1 (2009), 47–57.

22. Ghose, A; Goldfarb, A; and Han, S.P. How is the mobile internet di<sup>f</sup>erent? Search costs and local activities. Information Systems Research, 24, 3 (2013), 613–631.

23. Ghose, A; Ipeirotis, P.G; and Li, B. Examining the impact of ranking on consumer behavior and search engine revenue. Management Science, 60, 7 (2014), 1632–1654.

24. Ghose, A; Kwon, H.E; Lee, D; and Oh, W. Seizing the commuting moment: contextual targeting based on mobile transportation apps. Information Systems Research, 30, 1 (2019), 3–13.

25. Ghose, A.; and Yang, S. An empirical analysis of search engine advertising: sponsored search in electronic markets. Management Science, 55, 10 (2009), 1605–1622.

26. Goldfarb, A. The internet killed distance. Mobile computing brought it back. MIT Technology Review (2013). https://www.technologyreview.com/s/520796/the-internet-killed-distancemobile-computing-brought.

27. Goldfarb, A. What is di<sup>f</sup>erent about online advertising? Review of Industrial Organization, 44, 2 (2014), 115–129.

28. Goldfarb, A. and Tucker, C. Online display advertising: targeting and obtrusiveness. Marketing Science, 30, 3 (2011), 389–404.

29. Hu<sup>f</sup>, D.L. De<sup>fi</sup>ning and estimating a trading area. Journal of Marketing, 28, 3 (1964), 34–38.

30. Inman, J.J.; and McAlister, L. Do coupon expiration dates a<sup>f</sup>ect consumer behavior? Journal of Marketing Research, 31, 3 (1994), 423–428.

31. Johnson, E.J; Shu, S.B; Dellaert, Benedict G. C; Fox, C; Goldstein, D.G; Häubl, G; Larrick, R.P; Payne, J.W; Peters, E; Schkade, D; Wansink, B; and Weber, E.U. Beyond nudges: tools of a choice architecture. Marketing Letters, 23, 2 (2012), 487–504.

32. Koetsier, J. Mobile Advertising Will Drive 75% Of All Digital Ad Spend In 2018: here’s what’s changing. https://www.forbes.com/sites/johnkoetsier/2018/02/23/mobile-advertisingwill-drive-75-of-all-digital-ad-spend-in-2018-heres-whats-changing (accessed on June 25, 2019).

33. Kondo, F.N; Uwadaira, Y; and Nakahara, M. Stimulating customer response to promotions: the case of mobile phone coupons. Journal of Targeting, Measurement and Analysis for Marketing, 16, 1 (2007), 57–67.

34. Li, C; Luo, X; Zhang, C; and Wang, X. Sunny, rainy, and cloudy with a chance of mobile promotion e<sup>f</sup>ectiveness. Marketing Science, 36, 5 (2017), 762–779.

35. Li, H; Shen, Q; and Bart, Y. Local market characteristics and online-to-o<sup>fl</sup>ine commerce: an empirical analysis of Groupon. Management Science, 64, 4 (2018), 1860–1878.

36. Luo, X; Andrews, M; Fang, Z; and Phang, C.W. Mobile targeting. Management Science, 60, 7 (2014), 1738–1756.

37. Mantonakis, A; Rodero, P; Lesschaeve, I; and Hastie, R. Order in choice: e<sup>f</sup>ects of serial position on preferences. Psychological Science, 20, 11 (2009), 1309–1312.

38. Molitor, D; Reichhart, P; and Spann, M. Location-based advertising and contextual mobile targeting. In Proceedings of the Thirty Seventh International Conference on Information Systems, 2016, https://aisel.aisnet.org/icis2016/EBusiness/Presentations/14/.

39. Renski, H. New <sup>fi</sup>rm entry, survival, and growth in the United States: a comparison of urban, suburban, and rural areas. Journal of the American Planning Association, 75, 1 (2008), 60–77.

40. Simonson, I.; and Tversky, A. Choice in context: tradeo<sup>f</sup> contrast and extremeness aversion. Journal of Marketing Research, 29, 3 (1992), 281–295.

41. Thaler, R.H; Sunstein, C.R; and Balz, J.P. Choice architecture. Working paper. University of Chicago, 2010. http://ssrn.com/abstract=1583509.

42. The Financial Brand. Statistics & trends that will shape your digital marketing strategy. https://the<sup>fi</sup>nancialbrand.com/66080/trends-facts-digital-marketing-advertising/(accessed on June 25, 2019).

43. Train, K. Discrete Choice Methods with Simulation. New York: Cambridge University Press, 2003.

44. Unni, R.; and Harmon, R. Perceived e<sup>f</sup>ectiveness of push vs. pull mobile location based advertising. Journal of Interactive Advertising, 7, 2 (2007), 28–40.

45. Ursu, R.M. The power of rankings: quantifying the e<sup>f</sup>ect of rankings on online consumer search and purchase decisions. Marketing Science, 37, 4 (2018), 530–552.

46. Wu, J; Shi, M; and Hu, M. Threshold e<sup>f</sup>ects in online group buying. Management Science, 61, 9 (2015), 2025–2040.

47. Xu, H; Teo, H.-H; Tan, B.C.Y; and Agarwal, R. The role of push-pull technology in privacy calculus: the case of location-based services. Journal of Management Information Systems, 26, 3 (2009), 135–174.

## About the Authors

<sup>Dominik</sup> <sup>Molitor</sup> (dmolitor@fordham.edu) is an assistant professor of Information, Technology, and Operations at Fordham University’s Gabelli School of Business. His research interests include mobile and electronic commerce, digital marketing and search platforms. He has published in Decision Support Systems, PLOS ONE, the Journal of Business Economics, and proceedings, including those of the International Conference on Information Systems.

<sup>Martin Spann</sup> (spann@spann.de; corresponding author) is a professor of electronic commerce and digital markets at the Ludwig-Maximilians-Universität München, Germany. His research interests include e-commerce, mobile commerce, interactive pricing mechanisms, and social networks. He has published in Information Systems Research, MIS Quarterly, Management Science, Marketing Science, Journal of Marketing, and other journals.

<sup>Anindya</sup> <sup>Ghose</sup> (aghose@stern.nyu.edu) is the Heinz Riehl Chair Professor of Business at New York University’s Leonard N. Stern School of Business where he holds a joint appointment in the TOPS and Marketing departments. He is the Director of the Master of Science in Business Analytics program. His research seeks to measure and quantify three related issues: (1) the welfare impact of the Internet and mobile technologies on industries and markets transformed by its shared infrastructure, (2) the trade-o<sup>f</sup>s between data privacy concerns and the economic value accruing to consumers, and (3) the business impact of digital advertising and mobile marketing. He has published papers in Information Systems Research, MIS Quarterly, Management Science, Marketing Science, Statistical Science, and other journals.

<sup>Philipp</sup> <sup>Reichhart</sup> (lmu@philippreichhart.de) is an associated researcher at the Institute of Electronic Commerce and Digital Markets at the Ludwig-Maximilians-Universität München, Germany. His research interests include mobile commerce, consumer behavior, word of mouth and viral marketing. He has published in Journal of Interactive Marketing, Electronic Markets, International Journal of Electronic Business, and other journals.
