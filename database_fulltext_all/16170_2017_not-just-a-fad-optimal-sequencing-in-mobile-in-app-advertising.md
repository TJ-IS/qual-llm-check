---
otero_id: 16170
otero_key: "Q8KRRBVX"
title: "Not Just a Fad: Optimal Sequencing in Mobile In-App Advertising"
authors: "Zhen Sun; Milind Dawande; Ganesh Janakiraman; Vijay Mookerjee"
year: "2017"
journal: "Information Systems Research"
doi: "10.1287/isre.2017.0697"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

![](/api/attachments/Q8KRRBVX/fulltext/images/9edd52560e2937f28b3629077c6bc19fcac915358916ebbea5420543c4226cff.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Not Just a Fad: Optimal Sequencing in Mobile In-App Advertising

http://orcid.org/0000-0001-5397-9521Zhen Sun, Milind Dawande, Ganesh Janakiraman, Vijay Mookerjee

To cite this article:

http://orcid.org/0000-0001-5397-9521Zhen Sun, Milind Dawande, Ganesh Janakiraman, Vijay Mookerjee (2017) Not Just a Fad: Optimal Sequencing in Mobile In-App Advertising. Information Systems Research

Published online in Articles in Advance 08 Jun 2017

https://doi.org/10.1287/isre.2017.0697

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2017, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/Q8KRRBVX/fulltext/images/35a9f45cb2557efb1d08acc9e60b42f353ab4a579a54fca9df60e78192e0447a.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Not Just a Fad: Optimal Sequencing in Mobile In-App Advertising

Zhen Sun,<sup>a</sup> Milind Dawande,<sup>b</sup> Ganesh Janakiraman,<sup>b</sup> Vijay Mookerjee<sup>b</sup>

<sup>a</sup> School of Business, George Washington University, Washington, DC 20052; <sup>b</sup> Naveen Jindal School of Management, University of Texas at Dallas, Richardson, Texas 75080

Contact: zhens@gwu.edu, http://orcid.org/0000-0001-5397-9521 (ZS); milind@utdallas.edu (MD); ganesh@utdallas.edu (GJ); vĳaym@utdallas.edu (VM)

Received: May 25, 2016 Revised: October 14, 2016; November 25, 2016 Accepted: November 25, 2016 Published Online in Articles in Advance: June 8, 2017

https://doi.org/10.1287/isre.2017.0697

Copyright: © 2017 INFORMS

Abstract. In this paper, we address the challenge faced by ad networks in managing the fading ads (or fads) shown to an end user during a session of a mobile application (app). A fad is an ad that disappears if the user does not interact with it for some length of time. The withdrawn ad could be replaced by another ad. The goal of the ad network is to determine the sequence of fads shown to the user in an ad space to maximize the expected revenue generated over the user’s app session. Mobile in-app advertising is uniquely suited for the sequencing of fads because user sessions are typically longer (than web sessions), and a single ad is displayed at any given point in time. We consider two factors that afect the probability of a click on an ad during a session: (i) the sojourn efect, the influence of the passage of time, and (ii) the exposure efect, the influence of the number of prior exposures of the ad to the user during that session. We provide simple and optimal policies for the ad-sequencing problem when either of these two efects dominates. For the general case in which both efects are significant, we ofer a provably near-optimal heuristic policy. The following two enhancements to the basic sequencing problem are also analyzed: (a) consideration of both click ads (which generate revenue for the ad network only through clicks) and display ads (which generate revenue only through exposures) and (b) the presence of a constraint imposed by the publisher (i.e., the owner of the app) that the expected revenue in each time slot exceeds a certain threshold.

History: Giri Kumar Tayi, Senior Editor; Xue Bai, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2017.0697.

Keywords: in-app ads • fading ads • sequencing under uncertainty • optimal policies

## 1. Introduction

The past decade has seen a remarkable growth in the use of advertising on online interactive media devices connected to the Internet and/or telephone networks, e.g., personal computers, tablets, mobile phones, etc. (Marketwire 2012, Lieberman 2013). In the online advertising space, a fast growing segment is advertising on mobile devices such as smartphones or tablets. The revenue of mobile advertising in the United States reached \$5.3 billion during the first six months of 2014, up from \$3 billion in the first six months of 2013 (Interactive Advertising Bureau 2014b). Revenues from ads running on smartphones and tablets were predicted to exceed those from newspaper, magazine, and radio ads for the first time in the United States in 2014 (Hof 2014). Globally, mobile advertising revenue hit \$19.3 billion in 2013, almost doubling from the previous year (Interactive Advertising Bureau 2014a).

The focus of the current study is on ads that are displayed on a mobile application (app), such as an app for weather, stocks, or a game. Among the sectors within mobile advertising, in-app advertising has grown the fastest, and spending on in-app ads is expected to reach \$17 billion by 2018 (Grant 2014). In addition to the end user of the mobile app, there are at least two other parties that are involved in the elements of mobile in-app advertising: (i) the advertiser, who provides ads created to promote products or services, and (ii) the publisher, or the owner of the mobile app. The advertiser and the publisher often interact with one another through their respective agents (Business Insider 2013). Advertisers (brands that generate demand for advertising space) are usually represented by demand-side agents (or ad agencies). Demand-side agents provide advertisers the access to a variety of publishers for the widespread exposure of their ads. Ad networks are responsible for the actual delivery of ads on mobile apps. Supply-side ad networks integrate with apps (publishers) that supply the space for ad display. These ad networks help monetize the space owned by publishers and earn revenue for them. Supply-side contracts (between ad networks and publishers) often operate on a revenue sharing basis, i.e., publishers get a proportion of the revenue generated from their ad space. Supply-side ad networks obtain ads from one or more ad agencies.<sup>1</sup>

Past research on managing ad campaigns (the related work is summarized in Section 2) has mainly focused on solving the problem of choosing the best set of ads to show a given online visitor for a particular visit. While the problem we consider in this study— one involving the sequencing of mobile in-app ads— is also relevant for other forms of mobile advertising (or even online advertising in general), mobile in-app advertising incorporates features that are especially applicable to our setting. Unlike the web, where showing multiple ads is quite common on a web page, the typical practice in in-app advertising is to show a single ad, usually at the bottom of the app. For example, in Google Adsense, the number of ads on a single screen should not exceed one on a mobile web page (Graham 2015). While the simultaneous display of multiple ads is not common, it is not unusual to encounter the practice of rotating over a set of ads (shown one at a time, in sequence). Ad rotation is possible using the software development kit (SDK) of a mobile app. For example, an app working with iAd could utilize a timer for rotating advertisements, with a minimum rendering time of 30 seconds (Graham 2015). For apps using mopubios-sdk, both ad rotation and ad refreshing are feasible (GitHub 2014).

Given these developments, a natural innovation in in-app advertising—to increase the performance of ads—is the concept of an optimal fading ad (or a fad). A fad is an ad that disappears if the end user does not interact with it for a certain length of time. The withdrawn ad could be replaced by another ad, a default ad for the app, or even a block of empty space if so desired. On the web, a concept similar to fads is currently being implemented by ad-rotator technology. An ad rotator is a program that controls the display sequence of a set of ads to a user. Such a program is usually run under the web browser (client side). In a client-side implementation, the set of ads to display is provided at the time of page loading. Then, the ad rotator rotates over the ads in a predetermined sequence. In a server-side implementation, the logic of ad rotation resides at the server. At predetermined times, a call is made to the server for the provision of an ad.

Mobile in-app advertising is a good candidate to benefit from ad sequencing because the duration of a single session on a typical app is usually much longer than the length of stay of a user on a typical web page. In one study, the average app session was found to be 4.2 minutes, compared to the average web session length of just under 1 minute (Newark-French 2011). According to the Adobe Digital Index report (Gesenhues 2013), the average app session for tablet users lasts 24 minutes, while the average smartphone app session runs 13 minutes. Another finding from this report is that both tablet and smartphone users spend more time on apps than browsing mobile websites. Furthermore, eMarketer (2014) reports that mobile users are far more likely to click on ads served in an app than via a mobile browser: the average clickthrough rate for in-app ads is nearly 2.8 times higher than that for placements on the mobile web, and the average revenue generated per thousand impressions for in-app ads is about 2.5 times that of mobile web ads. The other aspect that makes mobile in-app ad sequencing attractive is that a single ad is displayed at any given time. A sequencing problem in which a set of ads can be displayed at any given time is less amenable to the kind of analysis and structural results we obtain in this study. These features (significant duration of a session and display of a single ad at any given time) make mobile in-app advertising an ideal candidate for the optimal sequencing of ads during the session for which the app is used.

The basic setting of our analysis is as follows. We consider the problem—faced by a supply-side ad network—of scheduling the ads to be displayed in the ad space on a mobile app during a session of the app. The session ends when the user either exits the app or clicks on an ad.<sup>2</sup> The ad network generates advertising revenue only from a click on an ad. The goal of the ad network is to determine the sequence of ads to be shown in the ad space to maximize the expected revenue generated over a session of the app. We assume that time is divided into slots of equal length that is determined by industry practice as the minimum length of exposure of an ad. In theory, a slot can be arbitrarily small. In practice, a slot should allow for loading an ad and some minimum exposure (e.g., a slot can be no less than 30 seconds). The ad network chooses an ad at the beginning of each slot: a new ad could be chosen or the ad shown in the previous slot could be retained. Once an ad is chosen for a time slot, it is displayed for the entire duration of that slot. The exit of the user may occur for one of two reasons: (1) she “naturally” exits from the app without clicking on an ad or (2) she clicks on an ad, causing her to leave the app. The length of her natural stay is governed by the probability that she exits the app (without clicking on an ad) at the end of each time slot. Thus, the user engages with the app for a random number of slots. We consider two factors that afect the probability of a click on an ad: (i) the number of time slots for which the ad has already been displayed during the session (exposure efect) and (ii) the time elapsed before the user clicks on the ad (sojourn efect).

The models we analyze evolve progressively. We start by motivating and analyzing two important special cases, one in which the sojourn efect is dominant and the other in which the exposure efect is dominant. Subsequently, the analysis in Section 6 considers both these efects. In Sections 3–6, our assumption is that the (conditional) probability that the user naturally exits the app at the end of a time slot, given that she enters that time slot and does not click on an ad, is a constant. In Section $^ { 7 , }$ we allow this probability to be time dependent. Two additional enhancements are analyzed in Section 7: (i) the consideration of both click ads (that generate revenue for the ad network only through clicks) and display ads (that provide a fixed revenue for each exposure), and (ii) the scheduling of ads in the presence of the publisher-imposed restriction that the expected revenue in each time slot exceeds a certain threshold.

The need for fast and efective solutions to the ad-sequencing problems we study is highlighted by the combinatorial explosion in the number of feasible sequences. Assume, for example, that an app session is expected to last a maximum of 10 time slots and there are 30 ads available that can be potentially displayed. Even for this modest problem size, the number of possible ad sequences is $\dot { 3 } 0 ^ { 1 0 } \left( \approx 6 \times 1 0 ^ { 1 4 } \right)$ . Furthermore, this cardinality explodes dramatically as either the number of ads or the number of time slots increases. Thus, brute-force enumeration is ruled out, given that such a problem is typically required to be solved within hundreds of milliseconds. Our analysis in this paper proposes simple ad-sequencing rules: for the case in which either the sojourn efect or the exposure efect is dominant, we provide optimal solutions; for the general case in which both efects are significant, our solutions provide attractive performance guarantees.

## 2. Related Work

This paper is related to research in three areas: (1) campaign-level scheduling, (2) visit-level scheduling, and (3) click-probability prediction.

## 2.1. Campaign-Level Scheduling

The main focus of the literature on Internet ad campaign optimization is on the display of ads on diferent platforms (e.g., websites, smartphones, and Internetenabled game consoles) to optimize a certain objective (e.g., revenue and clicks) over a given planning horizon. Other than the consideration of the characteristics of the ads to be shown (e.g., size and location) and the issues associated with displaying a set of ads in the ad space, advertiser constraints based on ad saturation and competition are also considered in ad schedules (Turner et al. 2011b, Turner 2012). Mookerjee et al. (2012) study an optimization problem by jointly considering the publisher and the ad network. The goal of the ad network is to maximize the revenue while meeting or exceeding a click-through rate constraint specified by the publisher. Models of multistage decision making have been proposed for the management of Internet ad campaigns; these models are usually solvable through dynamic programming techniques (Baldacci et al. 2013, Hwang et al. 2013, Lai et al. 2010, Moallemi and Saglam 2013). In addition, there are a number of patents that measure the efectiveness of an Internet ad campaign (Harvey et al. 2010, Gerken 2008, Lindsay et al. 2010, Srinivasan and Shamos 2010). Moreover, there are other studies that examine a host of important microlevel issues in Internet advertising, such as the impact of ad position on profitability, targeting strategies (including privacy concerns), and wear-in/wear-out efects of Internet ads (Turner et al. 2011a, Chatterjee et al. 2003, Evans 2009, Goldfarb and Tucker 2011).

The problem we study in this paper is more specialized in that it focuses on the management of an ad campaign at the level of a single user’s app session. While solving the problem at the level of a single session, we incorporate some higher-level concerns that arise in managing the overall ad campaign (i.e., across users and over a longer planning horizon). One such aspect is the use of a filtering constraint, namely, an ad is shown only if it meets or exceeds a performance constraint. This constraint captures the publisher’s outside options, e.g., to display better ads from another ad network, display content and forego ad revenue, and so on.

## 2.2. Visit-Level Scheduling

There is a fairly large body of related work on the visitlevel scheduling of Internet ads. Dasgupta et al. (2009) introduce a storyboarding problem. In storyboarding, during the period a web user is on a website (visiting one or more web pages), a single advertiser controls a major ad position for some continuous time slots. The advertiser can then use these time slots to display different ads to showcase a range of products/services and build a linear story line. The goal of the publisher is to allocate multiple advertisers to the time slots of the user’s visit to maximize the total revenue under a cost-per-impression revenue model (i.e., the revenue is generated based on the exposure of ads). Dasgupta et al. (2009) propose a 7-competitive online algorithm for this problem. Albers and Passen (2013) present improved approximation algorithms for the problem. Kumar et al. (2007) provide heuristics for the problem of scheduling ads across multiple ad slots over a fixed time horizon to maximize the revenue from one web user for a website under a hybrid pricing model. The underlying optimization problem is solved as an ad-scheduling problem over the time horizon, subject to constraints that reflect the interests of advertisers (Dawande et al. 2003, 2005; Kumar et al. 2006). There are several important diferences between Kumar et al. (2007) and our paper. First, Kumar et al. (2007) studies advertising on a web page where multiple ads can be simultaneously shown to the user. Thus, the focus in Kumar et al. (2007) is on a fitting problem: at each slot there is some space available, and the challenge is to fit ads in such a way that an objective is optimized. Second, Kumar et al. (2007) only considers exposure efects, while our paper considers two efects—sojourn and exposure efects. Third, the reclick efect in Kumar et al. (2007) (i.e., a user clicking again on the same ad during a visit) does not apply to our problem. In our study, the mobile context presents clearly diferent challenges: only one ad can be shown at a time, and there is no reclick, since a click ends the impression as the user navigates away from the app. Fourth, in Kumar et al. (2007), the decision horizon is a fixed number of time slots. However, as mentioned above, our problem has to consider a random number of time slots since the visitor may leave the app or click on an ad in any time slot to end the problem. Finally, our problem context permits a much deeper analysis relative to Kumar et al. (2007); the technical contribution in Kumar et al. (2007) was in developing a heuristic whose performance was evaluated numerically. We provide optimal solutions in some cases, while in others we provide near-optimal solutions with an attractive performance guarantee.

In a typical stochastic sequencing problem, the objective is to order the processing of tasks (or jobs) to optimize some cost or revenue-related metric over a time horizon (which could be fixed and finite, or infinite). For instance, each task could incur a waiting cost that is a function of the time that task has to wait before being processed. The uncertainty could be, for example, in the processing times needed for the tasks. Two well-known examples are the appointment scheduling problem (see, e.g., Mak et al. 2015, Klassen and Yoogalingam 2009, Robinson and Chen 2003) and the stochastic traveling salesman problem (see, e.g., Cheong and White 2012, Chang et al. 2009). We note two key features that typically exist in such a setting: (i) each task contributes to the objective function via its processing cost or waiting cost, and (ii) the problem ends when all of the jobs are processed or when the time horizon ends. In our sequencing problem, on the other hand, the ad network gets revenue only when an ad is clicked on during a session. Moreover, a click ends the session, as the user navigates away from the app. Thus, only one ad contributes to the ad network’s objective. Also, the time horizon of our sequencing problem is random—the problem ends when the user either decides to navigate away from the app or clicks on an ad. In fact, the time horizon is a function of the sequencing policy itself. Consequently, uncertainty in our problem arises from two sources: the duration for which the user stays on the app and her clicking behavior.

## 2.3. Click-Probability Prediction

In both campaign-level and visit-level scheduling of ads, a basic input is the knowledge of the factors that afect user click behavior. By exploiting the substantial amount of literature in marketing on the prediction of a consumer’s choice over a set of discrete alternatives, techniques have been developed to predict consumer actions (clicks, conversions, etc.) associated with Internet ads. For example, Mookerjee et al. (2012) use logistic regression for predicting—in real time—a visitor’s probability of a click. The logit model is also used to infer consumer trends, e.g., how display ads influence consumers to make subsequent choices in consuming brand-specific content (Bucklin and Sismeiro 2009). In in-app advertising, predictions must be done quickly, thus restricting the number of independent variables that predictive models can incorporate. In our study, we use some structural properties of prediction work that has been done in previous research. Specifically, we use results pertaining to how the probability of a click changes with repeated exposures of an ad and with the time elapsed since the user initiated the app session.

## 3. The General Model

We consider the problem, faced by an ad network, of scheduling the ads to be displayed in an ad space of an app during a session of engagement with an end user. The session ends when the user either leaves the app or clicks on an ad.<sup>3</sup> In practice, clicking on an ad often causes the user to spend a significant amount of time outside the app; thus, assuming that the app session ends is more appropriate. For instance, after clicking on the ad, the user is often directed to another page that is controlled by the ad, where she may install another app, send an email, or place an order. Sometimes the ad has a “tap to call” feature. Interacting with such an ad initiates a phone call, such as placing an order for a pizza. In our ongoing work with the direct mobile-inapp platform Cidewalk (http://www.cidewalk.com), we observe that the user’s app session almost always ends if she engages with the ad.

The ad network generates advertising revenue only from a click on an ad. A generalization that considers both click ads (which generate revenue only if clicked) and display ads (which generate revenue only through exposures) is considered in Section 7. The goal of the ad network is to determine the sequence of ads to be shown in the ad space to maximize the expected revenue generated over the user’s session. We now discuss this problem in more detail and also introduce the relevant notation.

Assume that, during a user’s session, time is divided into slots of equal length that is predetermined by the ad network (e.g., 15 seconds). Consider a single ad space in which ads are displayed to this user. Let A denote the set of available ads. Once an ad is chosen for a time slot, it is displayed for the entire duration of the slot. The display of an ad for a time slot is referred to as an exposure of that ad. A new ad can potentially be chosen for exposure at the beginning of a new time slot. An ad can be displayed for multiple time slots (either contiguous or noncontiguous); $\mathrm { i . e . , }$ , it can have multiple exposures. The revenue per click of ad $a \in A$ is $\alpha _ { a }$

Throughout the session, the (conditional) probability that the user naturally exits the page at the end of a time slot, given that she enters that time slot and does not click on an ad, is $\lambda ;$ thus, the user stays on with probability $\bar { \lambda } = 1 - \lambda$ . This assumption on the user’s leaving probability is the same as that for the storyboarding problem. For ad $a \in A ,$ , let $p _ { a } ( k , t )$ denote the probability of a click on ad a when it is shown in time slot t and this is the kth exposure of that ad. Thus, the following two factors are assumed to afect this click probability:

• Exposure efect. The probability of a click on an ad during an exposure is influenced by the number of prior exposures of that ad. Unlike ads on a web page, mobile in-app ads are pushed to the end user, rather than pulled by her as a result of informationseeking search activity. Thus, from an end-user cognition perspective, in-app ads are similar to display or banner ads. Banner ads are subject to a phenomenon called banner burnout: the advertising efectiveness (in terms of banner click-through rate) reaches its maximum point at the first exposure and tends to decline rapidly with each additional exposure (Naik et al. 1998, Chatterjee et al. 2003, Braun and Moe 2013). Thus, the repetition of banner ads can lead to negative returns a lot earlier than that of other types of ads in online advertising. Because in-app ads are also pushed to the user (opening an app is analogous to opening a web page), we expect the exposure efect to be similar: the click-through rate can be expected to decline with each additional exposure. In the specific context of mobile ads, the typical time-to-click behavior (when repeatedly shown the same ad during a session) is consistent with the behavior for banner ads. Here, studies show that the chance of a click on a mobile ad drastically reduces after a certain length of time (Waber 2014).

• Sojourn efect. The probability of a click on an ad in a time slot may also be influenced by the number of the time slots the user has already spent on the app during the session. Again, one would typically expect the click probability to decrease with time: as the duration of a session increases, it is more likely that the user is not interested in clicking on an ad at all. The sojourn efect essentially captures a fact that has been known in the online advertising industry for quite sometime now: some users are clickers and others are not. Everything else held constant, a clicker is more likely to generate a click. For example, studies on online advertising on a web page found that a Google user that executes a search by pressing the “Search” button as opposed to pressing Enter is much more likely to click on an ad.

Table 1. Summary of Notations

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $A$ </td><td>The set of ads of the ad network</td></tr><tr><td> $a$ </td><td>An ad of the ad network,  $a \in A$ </td></tr><tr><td> $\alpha_{a}$ </td><td>The revenue per click of ad  $a$ </td></tr><tr><td> $t$ </td><td>A time slot in the schedule,  $t \in \{1,2,\ldots\}$ </td></tr><tr><td> $\lambda$ </td><td>The probability that the app user concludes her session at the end of a time slot, given that she enters that time slot and given that she does not click on an ad;  $\lambda > 0$ </td></tr><tr><td> $p_{a}(k,t)$ </td><td>The probability of a click on ad  $a$  when this ad is displayed in time slot  $t$  and it is the  $k$ th exposure of ad  $a$ </td></tr></table>

Similarly, bad spellers are often clickers. Thus, ad networks often profile users on the web as clickers versus nonclickers (Mookerjee et al. 2012). The sojourn efect is also based on the clicker/nonclicker phenomenon. As time passes in a session without a click, it is more likely that the user is someone who usually does not click on ads. Hence, the probability of a click can be expected to decrease with the duration of a session. The mathematical foundation of the sojourn efect is developed in Section 4 and Online Appendix B.

The notation introduced thus far is summarized in Table 1.

3.1. The Optimization Problem of the Ad Network For an arbitrary ad display sequence $\sigma ,$ let $\alpha _ { ( i ) } ^ { \sigma }$ and $p _ { ( i ) } ^ { \sigma }$ be the revenue per click and the probability of a click of the ad shown in time slot $i \in \{ \tilde { 1 } , 2 , \dots \}$ , respectively. Then, the expected revenue from the sequence σ is

$$
\mathbb {E} (\mathrm{Rev} ^ {\sigma}) = \sum_ {i} \alpha_ {(i)} ^ {\sigma} p _ {(i)} ^ {\sigma} \bar {\lambda} ^ {i - 1} \prod_ {j = 1} ^ {i - 1} (1 - p _ {(j)} ^ {\sigma}).
$$

In other words, the expected revenue from an ad display sequence is the summation of the expected revenue from each time slot. The expected revenue generated from a time slot, say, slot $i ,$ is the product of the expected revenue generated by the ad that is placed in the time slot $( \mathrm { i . e . , } \alpha _ { ( i ) } ^ { \sigma } p _ { ( i ) } ^ { \sigma } )$ and the probability of the user entering this time slot. The probability that the user enters time slot i is the product of (i) the probability of no click on an ad in any of the time slots before time slot i, i.e., $\begin{array} { r } { \prod _ { j = 1 } ^ { i - 1 } ( 1 - p _ { ( j ) } ^ { \sigma } ) _ { . } } \end{array}$ , and (ii) the probability of naturally staying in the app session and entering time slot $i , \mathrm { i . e . , } \bar { \lambda } ^ { i - 1 }$

Then, the optimization problem of the ad network is to find an ad display sequence that maximizes the above expected revenue; that is

$$
\max _ {\sigma} \{\mathbb {E} (\operatorname{Rev} ^ {\sigma}) \}.\tag{1}
$$

In Section $^ { 7 , }$ we will relax our assumptions in the following directions:

(i) The probability that the app user concludes her session at the end of time slot $t ,$ given that she enters that time slot and given that she does not click on an ad, is $\lambda _ { t } ,$ instead of a constant λ. In words, the natural exit probability of the user is time dependent.

(ii) In the above optimization problem, we assumed that the ad network generates revenue only from a click on an ad; i.e., the ads under consideration are all click ads. In addition to click ads, we consider display ads that, if shown, generate a fixed per-slot revenue for the ad network. Thus, showing a click ad in a time slot will not generate revenue for the ad network if the ad is not clicked on, while showing a display ad in the time slot brings the ad network a fixed amount of revenue.

(iii) We consider optimization problem (1) under a constraint (imposed by the owner of the app) that the conditional expected revenue in each time slot is above a specified threshold.

Until Section 7, however, we focus on the optimization problem (1) under the assumptions stated earlier in this section. We now discuss two relevant special cases that will be analyzed in Sections 4 and 5.

## 3.2. Two Special Cases

Two relevant special cases are as follows:

• The exposure efect is dominant and the sojourn efect is negligible. This is likely to occur when the session is on an app that users typically come to for a short time duration (e.g., an app providing weather information) and where ads are served using a retargeting technique. On one hand, since the duration of the session is short, the impact of time on the probability of a click on an ad is likely to be insignificant; in other words, the sojourn efect is negligible. On the other hand, retargeting allows ads to be served to users who have taken identifiable prior actions that are of interest to the advertisers, e.g., a recent download of a specific app (Sullivan 2014). Therefore, retargeting helps the ad network to display a sequence of ads about products and/or brands that the user is already knowledgeable about. Thus, the exposure efect is significant, since the displayed ads only play a “reminding role,” and the probability of a click is likely to reduce significantly with each additional exposure.

• The sojourn efect is dominant and the exposure efect is negligible. This situation is likely to occur when the app is content based—e.g., a news app or one that provides political commentaries—and the ads are not being served based on prior history about the user.<sup>4</sup> Rather, ads are likely to be served to match the content. Since the app is content based, the user is likely to get increasingly involved in the content as her session progresses. Consequently, the sojourn efect plays a significant role. In content-based ads, repeating an ad does not degrade its click probability as much as it does for a retargeted ad. This is because a user is not already primed about the context of a content-based ad. When the user is already primed (as in the case of a retargeted ad), if the first exposure (or first few exposures) does not generate a click, further exposures are much less likely to do so. Thus, content-based ads are likely to have a relatively weak exposure efect.

The special case of the sojourn efect being dominant is studied in Section 4, and that of the exposure efect being dominant in Section 5.

## 4. The Sojourn Decay

In this section, we consider the special case of the optimization problem (1) in which the exposure efect is ignored; that is, the probability of a click on an ad $a \in A$ at any time depends only on the characteristics of the ad and the amount of time the user has thus far spent in the app session. We first formalize the optimization problem for this special case and then provide an optimal policy.

## 4.1. The Model

Let $p _ { a } ( t ) = \delta _ { a } \beta ^ { t - 1 }$ denote the probability of a click on ad a when this ad is displayed in time slot t, where $\delta _ { a }$ is the probability of a click on ad a if it is shown in the first time slot of the app session, and $\beta \in ( 0 , 1 )$ is the sojourn decay factor, i.e., the probability of a click on an ad decreased by a factor of $\beta$ if the user stays for one more time slot. Note that the sojourn decay is not ad specific. To discuss the microfoundation of the sojourn efect, consider two types of visitors: clickers and nonclickers. Let p be the probability that a visitor belongs to the clicker type, and let 1<sup>−</sup> p be the probability that a visitor belongs to the nonclicker type. Given that a clicker (nonclicker) has arrived at a certain time slot, let a (respectively, ε) be the probability that she will click on an ad shown in that time slot. Of course, $a > \varepsilon$ . We can show that the probability of a click for an ad shown in time slot t, conditional on there being no click in the earlier t <sup>−</sup> 1 time slots, decreases with t; the detailed derivation is in Online Appendix B. Therefore, as the app session progresses, the probability of a click on an ad decreases. Recall from Section 3 that $\alpha _ { a }$ denotes the revenue per click of a click on ad $^ { a , }$ and $\lambda = 1 - \bar { \lambda }$ is the probability that the app user concludes her session at the end of time slot t given that she enters that time slot and given that she does not click on an ad.

For an ad sequence $\sigma ,$ let $\operatorname { R e v } ^ { \sigma } ( T )$ denote the revenue generated in the first T time slots, and let Rev<sup>σ</sup> denote the total revenue generated by $\sigma .$ Since the probability of a click on an ad decreases with the increase in the duration of the app session, for any $\nu > 0$ , we can find a large enough T that guarantees $\bar { \mathrm { R e v } } ^ { \sigma } ( t ) / \mathrm { R e v } ^ { \sigma } > 1 - \nu$ for any $t > T$ . Therefore, we assume that the probability of a click on an ad is zero after the user has stayed for a suficiently long duration in the session; that is, for a large enough value of $T , p _ { a } ( t ) = 0$ for any $t > T$ and any $a \in A$ . Thus, the ad network wants to determine an ad display sequence for the first T time slots of the session.

Let $\alpha _ { ( i ) } ^ { \sigma }$ and $p _ { ( i ) } ^ { \sigma }$ be, respectively, the revenue per click and the probability of a click of the ad shown in slot i of an ad display sequence $\sigma ; i = 1 , 2 , \dots , T$ . Using the expression for the expected revenue of a sequence developed in Section 3, the optimization problem of the ad network is

$$
\max _ {\sigma} \left\{\sum_ {i = 1} ^ {T} \alpha_ {(i)} ^ {\sigma} p _ {(i)} ^ {\sigma} \bar {\lambda} ^ {i - 1} \prod_ {j = 1} ^ {i - 1} (1 - p _ {(j)} ^ {\sigma}) \right\}.\tag{2}
$$

To gain intuition, let us first consider three special cases in which it is trivial to find an optimal ad display sequence.

• Consider $p _ { a } ( t ) = g ( t ) = \delta \beta ^ { t - 1 }$ for all $a \in A$ . This is the case in which the sojourn decay and the initial click probability are the same for all ads. Since the probability of a click on any ad is the same in this case, the optimal expected revenue is achieved by showing the ad with the highest revenue per click $( \mathrm { i . e . , \ a r g m a x _ { { a } } \{ \alpha _ { { a } } \} } )$ for the entire session.

• Consider $\lambda = 1$ . In this case, the user leaves the app naturally at the end of the first time slot. With only one time slot to display an ad, the optimum is achieved by displaying the ad with the highest expected revenue in the first time slot $( \mathrm { i . e . , }$ , arg ma $\mathfrak { c } _ { a } \{ \alpha _ { a } p _ { a } ( 1 ) \} )$ .

• Consider $\alpha _ { a } = \alpha$ for all $a \in A$ . Thus, the revenue per click is the same for all ads. It is easy to see that the only criterion that should be used to pick an ad to display is that of the probability of a click in the current time slot. The optimal expected revenue is achieved by the following display policy: In time slot $t ,$ display ad $a _ { t } ^ { * } = \arg \operatorname* { m a x } _ { a } \{ p _ { a } ( t ) \}$

In general, however, an optimal policy (i.e., the solution of problem (2)) uses a nontrivial criterion. Next, we obtain an optimal policy.

## 4.2. An Optimal Policy

Relative to the general problem (1) in Section 3, problem (2) ofers the following significant simplification: with only sojourn decay, the decision of which ad to display in time slot t after the app user has entered this time slot is not afected by the placements of ads in the slots before slot t. In other words, the ad selection decision in time slot t depends only on the value of t. Then, to select an ad for display in time slot $t ,$ we only need to consider the “forward” schedule from slots t through T. Therefore, the optimization problem (2) can be optimally solved by the following backward dynamic program (DP).

Let R<sup>(</sup>t<sup>)</sup> denote the optimal expected revenue after the user enters time slot t. In other words, $R ( t )$ is the optimal expected revenue generated over time slots t through T. Thus, the optimal ad display sequence is the one that generates expected revenue $R ( 1 )$ . Starting from the last time slot $T ,$ we have

$$
R (T) = \max _ {a} \{\alpha_ {a} p _ {a} (T) \}.
$$

This is intuitive since no revenue can be generated for the ad network after time slot T. Then, the DP recursion determines $R ( T - 1 ) , R ( T - 2 ) , \ldots , R ( 1 )$ in that order

$$
\begin{array}{c} R (t) = \max _ {a} \bigl \{\alpha_ {a} p _ {a} (t) + \bar {\lambda} (1 - p _ {a} (t)) R (t + 1) \bigr \}, \\ t \in \{1, 2, \ldots , T - 1 \}. \end{array}
$$

Thus, we have the following optimal policy:

Optimal Policy. In slot $t \in \{ 1 , 2 , \ldots , T \}$ , display ad

$$
a _ {t} ^ {*} = \underset {a} {\arg \max} \{\alpha_ {a} p _ {a} (t) + \bar {\lambda} (1 - p _ {a} (t)) R (t + 1) \},
$$

where $R ( T + 1 ) = 0 .$

Note that in the special case in which $\alpha _ { a } = \alpha$ for all $^ { a , }$ the optimal ad display sequence resulting from the above DP is the same as that discussed in Section 4.1: In time slot $t ,$ display ad $a _ { t } ^ { * } = \arg \operatorname* { m a x } _ { a } \{ p _ { a } ( t ) \}$

The DP above has time complexity $O ( | A | T )$ and can, therefore, be easily computed. Interestingly, in the optimal sequence above, the expected revenue in a slot may not decrease monotonically with time. We now present a simple illustrative example. Let $A = \{ 1 , 2 , 3 \} , \hat { T } = 3$ , and $\bar { \lambda } = \mathbf { \bar { 0 . 7 } }$ . Let $\beta = 0 . 8$ . The revenue per click $\alpha _ { i } , j = 1 , 2 , 3 ,$ and the click probabilities $p _ { j } ( t ) , j = 1 , 2 , 3 , t = 1 , 2 , 3 ,$ are shown in Table 2.

We use the standard backward approach to compute the solution of the DP. In time slot $t = 3 ,$ we have

$$
R (3) = \max \{\alpha_ {1} p _ {1} (3), \alpha_ {2} p _ {2} (3), \alpha_ {3} p _ {3} (3) \} = \alpha_ {2} p _ {2} (3) = 0. 1 1 2.
$$

Thus, ad 2 should be placed in time slot $t = 3 .$ . In time slot $t = 2$

$$
\begin{array}{l} R (2) = \max \left\{ \begin{array}{l} \alpha_ {1} p _ {1} (2) + \bar {\lambda} (1 - p _ {1} (2)) R (3), \\ \alpha_ {2} p _ {2} (2) + \bar {\lambda} (1 - p _ {2} (2)) R (3), \\ \alpha_ {3} p _ {3} (2) + \bar {\lambda} (1 - p _ {3} (2)) R (3) \end{array} \right\} \\ = \alpha_ {2} p _ {2} (2) + \bar {\lambda} (1 - p _ {2} (2)) R (3) \\ \approx 0. 1 9 6. \end{array}
$$

Thus, ad 2 should be displayed in time slot $t = 2 .$ . In time slot t <sup></sup> 1

$$
\begin{array}{r l} & R (1) = \max \left\{ \begin{array}{l} \alpha_ {1} p _ {1} (1) + \bar {\lambda} (1 - p _ {1} (1)) R (2), \\ \alpha_ {2} p _ {2} (1) + \bar {\lambda} (1 - p _ {2} (1)) R (2), \\ \alpha_ {3} p _ {3} (1) + \bar {\lambda} (1 - p _ {3} (1)) R (2) \end{array} \right\} \\ & \quad = \alpha_ {1} p _ {1} (1) + \bar {\lambda} (1 - p _ {1} (1)) R (2) \\ & \quad \approx 0. 2 6 6. \end{array}
$$

Thus, ad 1 should be placed in the first time slot. The optimal schedule is to display ad 1 in time slot 1 and ad 2 in time slots 2 and 3, and the expected revenue is about 0.266. Note that the expected revenue is nonmonotonic in time: the expected revenues in the three time slots are, in order, $\stackrel { \textstyle - } { \alpha _ { 1 } ^ { \dotsc } } p _ { 1 } ( 1 ) = 0 . 1 3 5 , \ \alpha _ { 2 } p _ { 2 } ( 2 ) = 0 . 1 4 .$ and $\alpha _ { 2 } p _ { 2 } ( 3 ) = 0 . 1 1 2$ , respectively.

Table 2. Parameters in the Illustrative Example in Section 4.2

<table><tr><td></td><td>t=1</td><td>t=2</td><td>t=3</td></tr><tr><td>Ad 1 ( $\alpha_{1}$ =2.7)</td><td> $p_{1}(1) = \delta_{1} = 0.05$ </td><td> $p_{1}(2) = 0.05 \times 0.8 = 0.04$ </td><td> $p_{1}(3) = 0.04 \times 0.8 = 0.032$ </td></tr><tr><td>Ad 2 ( $\alpha_{2}$ =0.5)</td><td> $p_{2}(1) = \delta_{2} = 0.35$ </td><td> $p_{2}(2) = 0.35 \times 0.8 = 0.28$ </td><td> $p_{2}(3) = 0.28 \times 0.8 = 0.224$ </td></tr><tr><td>Ad 3 ( $\alpha_{3}$ =0.1)</td><td> $p_{3}(1) = \delta_{3} = 0.20$ </td><td> $p_{3}(2) = 0.20 \times 0.8 = 0.16$ </td><td> $p_{3}(3) = 0.16 \times 0.8 = 0.128$ </td></tr></table>

The above example shows that, in general, no simple rule of thumb (e.g., giving preference to ads with more expected revenue first or giving preference to ads with more revenue per click) is guaranteed to always provide very good solutions. A key reason for this is that the sequencing of ads can change the efective length of time over which the expected revenue is realized. We now provide an example to illustrate this.

Consider $\beta = 0 . 9$ and that we have two advertisements: a and b. Suppose the revenue per click of ad a is $\alpha _ { a } = 0 . 2$ and $\delta _ { a } = \bar { 1 }$ . The revenue per click of ad b is $\alpha _ { b } = 0 . 3$ and $\delta _ { b } = 0 . 6$ . Let the user’s leaving probability in any time slot, given that she entered that time slot and given that she did not click on an ad, be $\lambda = 0 . 1$ Intuitively, since the sojourn efect is not ad specific $( \mathrm { i . e . , }$ the click probabilities of all of the ads are afected in the same manner), one would expect the policy of scheduling the ad with the higher expected revenue first to be optimal. However, this is not necessarily the case. In time slot 1, the expected revenues of the two ads are as follows: $r _ { a } = p _ { a } ( 1 ) \times \alpha _ { a } = 0 . 2$ and $r _ { b } = p _ { b } ( 1 ) \times$ $\alpha _ { b } = 0 . 6 \times 0 . 3 = 0 . 1 8$ . If we schedule the ad with the higher expected revenue (i.e., ad a) in time slot 1, then the expected revenue is 0.2, but the problem ends at the end of slot 1 (since the user surely clicks on the ad). On the other hand, by scheduling ad b in slot 1, we get a lower expected revenue in slot 1 (namely, 0.18), but the problem enters slot 2 with probability $\vec { \lambda } \times ( 1 - \delta _ { b } ) =$ $0 . 9 \dot { \times } 0 . 4 = 0 . 3 6$ . The expected revenue in slot 2 is $\bar { \lambda } \times$ $( 1 - \delta _ { b } ) \times p _ { a } ( 2 ) \times \alpha _ { a } = 0 . \hat { 9 } \times 0 . 4 \times 0 . 9 \times 0 . 2 = 0 . 0 6 4 8 .$ Thus, if we schedule ad b in slot 1 and ad a in slot 2, then the expected revenue over the first two time slots is $0 . 1 8 + \mathrm { \dot { 0 } } . 0 6 4 8 > 0 . 2$ . An important observation here is that the sequencing of ads changes the efective length of time over which the expected revenue is realized.

This example illustrates just one of the trade-ofs the above DP considers. In general, the optimal sequence of ads depends on the values of the various parameters, namely, the initial click probability and the revenue per click of each ad, the sojourn decay factor, and the user’s leaving probability.

## 5. The Exposure Decay

In this section, we consider the special case of the optimization problem (1) in which the sojourn efect is ignored; that is, the probability of a click on an ad $a \in A$ at any time depends only on the characteristics of the ad and the number of exposures of the ad thus far in the app session. We first formalize the optimization problem for this special case and then provide an optimal policy.

## 5.1. The Model

Let $p _ { a } ( k )$ denote the probability of a click on ad a during the kth exposure of this ad. We assume that ${ p _ { a } } ( k )$ is nonincreasing in k and, furthermore, that this probability is zero after ad a has been shown in a suficiently large number of time slots in the app session, that is, for ad $^ { a , }$ for a suficiently large integer $K _ { a } , p _ { a } ( k ) = 0$ for any $k > K _ { a }$ . Thus, it is suficient to consider policies in which ad a is shown in at most $K _ { a }$ time slots. With the number of available ads being $| A |$ , the ad network wants to determine an ad display sequence for the first $\begin{array} { r } { K = \sum _ { a = 1 } ^ { | A | } K _ { a } } \end{array}$ time slots. This is consistent with the practice in digital marketing of setting an ad frequency cap that limits the number of times an individual is exposed to an ad (ABC-Netmarketing 2013).

Let $k _ { a } ( t )$ denote the number of exposures of ad a before time slot t. Thus, $p _ { a } ( k _ { a } ( t ) + 1 )$ is the probability of a click on ad a if it is displayed in time slot t. For an ad display sequence $\sigma ,$ let $\alpha _ { ( i ) } ^ { \sigma }$ and $p _ { ( i ) } ^ { \sigma }$ be the revenue per click and the probability of a click, respectively, of the ad shown in slot $i , i = 1 , 2 , \dots , K$ . The optimization problem of the ad network is

$$
\max _ {\sigma} \left\{\sum_ {i = 1} ^ {K} \alpha_ {(i)} ^ {\sigma} p _ {(i)} ^ {\sigma} \bar {\lambda} ^ {i - 1} \prod_ {j = 1} ^ {i - 1} (1 - p _ {(j)} ^ {\sigma}) \right\}.\tag{3}
$$

## 5.2. An Optimal Policy

Unlike the sojourn decay model in Section 4, here the ad display sequence before time slot t is relevant to the ad selection decision in time slot t because this information afects the probability of a click on the ad displayed in time slot t. Nevertheless, the model in this section is simpler than the general problem (1) in Section 3.1 since time does not play a direct role. In other words, to know the probability of a click on an ad at any time, only the number of prior exposures of this ad is required. Let us consider the following policy; the intuition behind the policy is explained immediately thereafter.

Optimal Policy. In time slot t, display ad $a \in A$ with the highest value of the ratio

$$
\frac {\alpha_ {a} p _ {a} (k _ {a} (t) + 1)}{\lambda + \bar {\lambda} p _ {a} (k _ {a} (t) + 1)}.\tag{4}
$$

The numerator in the above ranking criterion, $\mathrm { i . e . , }$ $\alpha _ { a } p _ { a } ( k _ { a } ( t ) + 1 )$ , is the expected revenue from displaying ad a in time slot t. Displaying the ad with the highest value of this expected revenue would be an optimal decision if the current time slot were the last one. In other words, such a decision would be a myopic one that would disregard the impact on the expected revenue in the subsequent time slots in the case when the user does not click on the ad shown in the current slot and chooses to extend the app session beyond the current slot. The denominator in the ranking criterion, i.e., $\lambda + \bar { \lambda } p _ { a } ( k _ { a } ( t ) + 1 )$ , captures the efect of the current ad on the future expected revenue. Recall that λ is the (conditional) probability that the user naturally exits the page at the end of a time slot, given that she enters that time slot and does not click on an ad. Roughly, as λ gets closer to 1 $( \mathrm { i . e . , }$ the user is expected to stay in the app session only for a few slots), the optimal sequence gets closer to the one obtained by showing ads in the decreasing order of their expected revenues; that is, in a given time slot, the ads with higher expected revenue in that slot are preferred for display. On the other hand, as λ gets closer to 0, the optimal sequence gets closer to the one obtained by showing ads in decreasing order of their revenue per click. Also, as ads become similar to each other in terms of revenue per click, the optimal criterion moves toward one in which we choose the ad with the highest click probability in the current time slot.

To further understand the intuition behind our policy, we discuss three special cases as follows:

• Consider the special case in which $\lambda = 1$ , i.e., the user stays in the app session only for one slot. Thus, the efective length of the planning horizon is 1. In this case, it is clear that the optimal decision is to show the ad with the highest expected revenue, $\mathrm { i . e . , }$ the ad a with the highest value of $\alpha _ { a } p _ { a } ( 1 )$ . Note that when $\lambda = 1$ , our proposed optimal policy also makes the same decision since the denominator of the ratio criterion becomes one.

• Consider the special case in which $\lambda = \epsilon ,$ where  is a very small positive number $( \epsilon \ll 1 )$ . Here, the user’s exit from the session occurs almost always from clicking on an ad. Thus, intuition suggests that the ad with the highest revenue per click, say, $^ { a , }$ should be displayed for the maximum number $( K _ { a } )$ of time slots followed by the ad with the second-highest revenue per click, and so on. As $\lambda  0$ , our policy approaches that of ranking the ads based on $\alpha _ { a }$

• Consider the special case in which $\alpha _ { a } = \alpha$ for all $a \in A ;$ that ${ \mathrm { i } } \mathbf { s } ,$ all ads generate the same revenue per click. Here, intuition suggests that the only criterion one should use to pick an ad to display is that of the probability of a click in the current time slot. In this case, the criterion our policy uses is that of ranking the ads according to the values of $p _ { a } ( k _ { a } ( t ) + 1 ) /$ $( \stackrel { \sim } { \lambda } + \bar { \lambda } p _ { a } ( k _ { a } ( t ) + 1 ) ) = \stackrel { \sim } { 1 } / ( \lambda / ( p _ { a } ( k _ { a } ( t ) + 1 ) ) + \stackrel {  } { \bar { \lambda } } )$ , which is equivalent to ranking based on the values of the current click probabilities $p _ { a } ( k _ { a } ( t ) + 1 )$

The above three special cases highlight that ads should be ranked using a nontrivial criterion that incorporates the revenue per click, the click probabilities, and the user’s leaving probability. The following result establishes the optimality of the proposed policy.

## Theorem 1. Policy (4) is optimal for problem (3).

The proofs of all of the technical results are provided in Online Appendix A. As we observed for the sojourn decay model in Section 4, the expected revenue in a slot may not decrease monotonically with time in the optimal policy. We now illustrate this using a simple numerical example. Let $A = \{ 1 , 2 \} , \ K _ { 1 } = \breve { K _ { 2 } } = 2 ,$ , and $\lambda = 0 . 3$ . The values of the parameters $\alpha _ { j } , j = 1 , 2 ,$ and $p _ { j } ( k ) , j = 1 , 2 , k = 1 , 2 ,$ , are shown in Table 3.

With the number of ads being two and each of them generating revenue for two exposures, the ad network wants to decide an ad display sequence for the first four time slots $( \mathrm { i . e . , }$ slot $t \in \{ 1 , \dot { 2 } , 3 , 4 \dot  \} \}$ . In time slot $t = 1 .$ we pick the ad that corresponds to

$$
\begin{array}{l} \max \bigg \{\frac {\alpha_ {1} p _ {1} (1)}{\lambda + \bar {\lambda} p _ {1} (1)}, \frac {\alpha_ {2} p _ {2} (1)}{\lambda + \bar {\lambda} p _ {2} (1)} \bigg \} \\ = \max \bigg \{\frac {0 . 2 5}{0 . 3 + 0 . 7 \times 0 . 5}, \frac {0 . 3}{0 . 3 + 0 . 7 \times 0 . 3} \bigg \} \\ = \frac {0 . 3}{0 . 3 + 0 . 7 \times 0 . 3} = \frac {\alpha_ {2} p _ {2} (1)}{\lambda + \bar {\lambda} p _ {2} (1)}. \end{array}
$$

Thus, ad 2 should be placed in time slot $t = 1$ . In time slot $t = 2 ,$ we pick the ad corresponding to

$$
\begin{array}{r l} & {\max \bigg \{\frac {\alpha_ {1} p _ {1} (1)}{\lambda + \bar {\lambda} p _ {1} (1)}, \frac {\alpha_ {2} p _ {2} (2)}{\lambda + \bar {\lambda} p _ {2} (2)} \bigg \}} \\ & {\quad = \max \bigg \{\frac {0 . 2 5}{0 . 3 + 0 . 7 \times 0 . 5}, \frac {0 . 2}{0 . 3 + 0 . 7 \times 0 . 2} \bigg \}} \\ & {\quad = \frac {0 . 2}{0 . 3 + 0 . 7 \times 0 . 2} = \frac {\alpha_ {2} p _ {2} (2)}{\lambda + \bar {\lambda} p _ {2} (2)}.} \end{array}
$$

Table 3. Parameters in the Illustrative Example in Section 5.2

<table><tr><td></td><td> $k = 1$ </td><td> $k = 2$ </td></tr><tr><td>Ad 1 ( $\alpha_{1} = 0.5$ )</td><td> $p_{1}(1) = 0.5$ </td><td> $p_{1}(2) = 0.1$ </td></tr><tr><td>Ad 2 ( $\alpha_{2} = 1$ )</td><td> $p_{2}(1) = 0.3$ </td><td> $p_{2}(2) = 0.2$ </td></tr></table>

Thus, ad 2 should be placed in time slot $t = 2 .$ . In time slot $t = 3$ , we pick the ad corresponding to

$$
\max \left\{\frac {\alpha_ {1} p _ {1} (1)}{\lambda + \bar {\lambda} p _ {1} (1)}, \frac {\alpha_ {1} p _ {1} (2)}{\lambda + \bar {\lambda} p _ {1} (2)} \right\} = \frac {\alpha_ {1} p _ {1} (1)}{\lambda + \bar {\lambda} p _ {1} (1)}.
$$

Thus, ad 1 should be placed in time slot $t = 3 .$ . In time slot $t = 4 ,$ ad 1 should be displayed since $p _ { 2 } ( 3 ) = 0 .$ The optimal schedule is to show ad 2 in time slots 1 and 2, and ad 1 in time slots 3 and 4. The expected revenue is nonmonotonic in time: the expected revenues in time slots 1 through 4 are $\alpha _ { 2 } p _ { 2 } ( 1 ) = \hat { 0 . 3 } , \alpha _ { 2 } p _ { 2 } ( 2 ) = 0 . 2 ,$ $\alpha _ { 1 } p _ { 1 } ( 1 ) = 0 . 2 5$ , and $\bar { \alpha } _ { 1 } p _ { 1 } ( 2 ) = 0 . 0 5 ,$ respectively.

## 6. Incorporating Both Sojourn Decay and Exposure Decay

In this section, we consider the general model that was introduced in Section 3. Thus, the probability of a click on an ad in a time slot depends on both the number of prior exposures of that ad and the number of time slots the user has spent thus far in the app session. For the general model, we assume a functional form of this probability for analytical tractability. Let

$$
p _ {a} (k, t) = \delta_ {a} \beta^ {t - 1} \gamma^ {k - 1},
$$

where $( \mathrm { i } ) \ \delta _ { a }$ is the probability of a click on ad $a \in A$ if it was shown in the first time slot of the app session, $( \mathrm { i i } ) \beta \in ( 0 , 1 )$ captures the impact of sojourn (time) decay (specifically, the probability of a click on an ad decreases by a factor of $\beta$ if the user stays for one more time slot), and (iii) $\gamma \in ( 0 , 1 )$ captures the impact of exposure decay (in particular, the click probability of an ad decreases by a factor of $\gamma$ after each exposure of that ad). Thus, we have ad-specific initial click probabilities but assume that the decay efects of time and exposure are the same across ads.

As before, let $k _ { a } ( t )$ denote the number of time slots in which ad a has been shown prior to time slot t. Thus, $\delta _ { a } \beta ^ { t - 1 } \gamma ^ { k _ { a } ( t ) } \left( = \delta _ { a } \beta ^ { t - 1 } \gamma ^ { k _ { a } ( t ) + 1 - 1 } \right)$ denotes the probability of a click on ad a if it is shown in time slot t. For an arbitrary ad display sequence $\sigma ,$ , let $\alpha _ { ( i ) } ^ { \sigma }$ and $\delta _ { ( i ) } ^ { \sigma } \beta ^ { i - 1 } \gamma ^ { k _ { ( i ) } ^ { \sigma } ( i ) }$ be the revenue per click and the probability of a click, respectively, of the ad shown in slot i. Then, the revenue generated by sequence σ is

$$
\begin{array}{l} \mathbb {E} (\mathrm{Rev} ^ {\sigma}) = \sum_ {i} \alpha_ {(i)} ^ {\sigma} \delta_ {(i)} ^ {\sigma} \beta^ {i - 1} \gamma^ {k _ {(i)} ^ {\sigma} (i)} \bar {\lambda} ^ {i - 1} \\ \qquad \cdot \prod_ {j = 1} ^ {i - 1} \big (1 - \delta_ {(j)} ^ {\sigma} \beta^ {j - 1} \gamma^ {k _ {(j)} ^ {\sigma} (j)} \big). \end{array}\tag{5}
$$

Thus, the optimization problem of the ad network is

$$
\max _ {\sigma} \{\mathbb {E} (\operatorname{Rev} ^ {\sigma}) \}.\tag{6}
$$

## 6.1. A Heuristic Policy with a

Let $\delta _ { \mathrm { m i n } } = \operatorname* { m i n } _ { a } \delta _ { a }$ . We first derive the lower and upper bounds on the expected revenue defined in (5)

• Using that $\beta < 1$ , a lower bound on (5) is

$$
\begin{array}{c} \mathrm{LB} ^ {\sigma} = \sum_ {i} \alpha_ {(i)} ^ {\sigma} \delta_ {(i)} ^ {\sigma} \beta^ {i - 1} \gamma^ {k _ {(i)} ^ {\sigma} (i)} \bar {\lambda} ^ {i - 1} \prod_ {j = 1} ^ {i - 1} \bigl (1 - \delta_ {(j)} ^ {\sigma} \gamma^ {k _ {(j)} ^ {\sigma} (j)} \bigr) \\ = \sum_ {i} \alpha_ {(i)} ^ {\sigma} \delta_ {(i)} ^ {\sigma} \gamma^ {k _ {(i)} ^ {\sigma} (i)} (\beta \bar {\lambda}) ^ {i - 1} \prod_ {j = 1} ^ {i - 1} \bigl (1 - \delta_ {(j)} ^ {\sigma} \gamma^ {k _ {(j)} ^ {\sigma} (j)} \bigr). \end{array}
$$

• Using that $k _ { ( j ) } ^ { \sigma } ( j ) \leq j - 1$ and $\delta _ { a } \geq \operatorname* { m i n } _ { a } \delta _ { a } ,$ an upper bound on (5) is

$$
\mathrm{UB} ^ {\sigma} = \sum_ {i} \alpha_ {(i)} ^ {\sigma} \delta_ {(i)} ^ {\sigma} \beta^ {i - 1} \gamma^ {k _ {(i)} ^ {\sigma} (i)} \bar {\lambda} ^ {i - 1} \prod_ {j = 1} ^ {i - 1} (1 - \delta_ {\min} \beta^ {j - 1} \gamma^ {j - 1}).
$$

Thus, for an arbitrary ad display sequence $\sigma ,$ we have

$$
\mathrm{LB} ^ {\sigma} \leq \mathbb {E} (\operatorname{Rev} ^ {\sigma}) \leq \mathrm{UB} ^ {\sigma}.
$$

It is instructive to interpret the lower and upper bounds $\mathrm { L B } ^ { \sigma }$ and $\mathrm { U B } ^ { \sigma }$ . As we will see below, $\mathrm { L B } ^ { \sigma }$ corresponds to the expected revenue generated by sequence σ for the following “fictitious” problem: Let the probability of a click on ad a if it is shown in the first time slot of the user’s session be $\delta _ { a }$ . This probability only decays with exposure by a factor of γ. Let $k _ { a } ( t )$ denote the number of time slots ad a has been shown prior to time slot t. Thus, the probability of a click on an ad a in time slot t is $p _ { a } ( k _ { a } ( t ) { \dot { ) } } = \delta _ { a } \gamma ^ { k _ { a } ( t ) - 1 }$ . The revenue per click of ad a is $\alpha _ { a } ,$ and the probability that the app user concludes her session at the end of a time slot, given that she entered that time slot and given that she did not click on an ad, is $1 - \beta \bar { \lambda }$

Upper bound $\mathrm { U B } ^ { \sigma }$ corresponds to the expected revenue generated by sequence σ for the following “fictitious” problem: Let the probability of a click on ad a if it is shown in the first time slot of the user’s session be $\delta _ { \mathrm { m i n } }$ (thus, this probability is not ad specific). This probability decays with time by a factor of $\beta \gamma$ Thus, the probability of a click on ad a in time slot t is $p _ { a } ( t ) = \delta _ { \mathrm { m i n } } \bar { ( \beta \gamma ) } ^ { t - 1 }$ . Let $k _ { a } ( t )$ denote the number of time slots ad a has been shown prior to time slot t. The revenue per click of ad a when it is shown in time slot t is $\phi _ { a } = \dot { ( \alpha _ { a } \delta _ { a } / ( \delta _ { \operatorname* { m i n } } \gamma ^ { t - 1 } ) ) } \gamma ^ { k _ { a } ( t ) }$

Let $\dot { \phi _ { ( i ) } ^ { \sigma } } = \big ( \alpha _ { ( i ) } ^ { \sigma } \dot { \delta } _ { ( i ) } ^ { \sigma } / ( \delta _ { \operatorname* { m i n } } \gamma ^ { i - 1 } ) \big ) \gamma ^ { k _ { ( i ) } ^ { \sigma } ( i ) }$ be the revenue per click of the ad in time slot i of sequence $\sigma ,$ and let $p _ { ( i ) } ^ { \sigma } = \delta _ { \mathrm { m i n } } ( \beta \gamma ) ^ { i - 1 }$ be the probability of a click on the ad in time slot i of sequence σ. Then, the expected revenue of sequence σ is

$$
\begin{array}{l} \sum_ {i} \phi_ {(i)} ^ {\sigma} p _ {(i)} ^ {\sigma} \prod_ {j = 1} ^ {i - 1} (1 - p _ {(j)} ^ {\sigma}) \\ = \sum_ {i} \frac {\alpha_ {(i)} ^ {\sigma} \delta_ {(i)} ^ {\sigma}}{\delta_ {\min} \gamma^ {i - 1}} \gamma^ {k _ {(i)} ^ {\sigma} (i)} \delta_ {\min} (\beta \gamma) ^ {i - 1} \bar {\lambda} ^ {i - 1} \prod_ {j = 1} ^ {i - 1} (1 - \delta_ {\min} (\beta \gamma) ^ {j - 1}) \\ = \sum_ {i} \alpha_ {(i)} ^ {\sigma} \delta_ {(i)} ^ {\sigma} \beta^ {i - 1} \gamma^ {k _ {(i)} ^ {\sigma} (i)} \bar {\lambda} ^ {i - 1} \prod_ {j = 1} ^ {i - 1} (1 - \delta_ {\min} (\beta \gamma) ^ {j - 1}) = U B ^ {\sigma}. \end{array}
$$

We now explain our purpose in developing the lower and upper bounds. Let $\sigma _ { L }$ be a sequence that maximizes $\bar { \mathrm { L B } ^ { \sigma } }$ , and let $\sigma _ { U }$ be a sequence that maximizes UB<sup>σ</sup>. Let OPT be the optimal expected revenue to the ad network (i.e., the optimum value of problem (6)). Then, we have

$$
\mathrm{LB} ^ {\sigma_ {L}} \leq \mathbb {E} (\operatorname{Rev} ^ {\sigma_ {L}}) \leq \mathrm{OPT} \leq \mathrm{UB} ^ {\sigma_ {U}}.
$$

We will choose the sequence that maximizes $\mathrm { L B } ^ { \sigma }$ as our heuristic policy (Lemma 1). The upper bound $\mathrm { U B } ^ { \sigma _ { U } }$ will then be exploited to establish a performance guarantee on our heuristic policy (Lemma 2 and Theorem 2).

Lemma 1. The ad display sequence resulting from the $f o l -$ lowing policy maximizes the value of the lower bound $\dot { \mathrm { L B } } ^ { \sigma }$ on the expected revenue over the app session: In time slot $t ,$ display ad $a _ { t } = ( \alpha _ { a } \delta _ { a } \gamma ^ { k _ { a } ( t ) } ) / ( ( 1 - \ddot { \beta } \bar { \lambda } ) + \beta \bar { \lambda } \delta _ { a } \gamma ^ { k _ { a } ( t ) } )$

Lemma 2. The ad display sequence resulting from the following policy maximizes the value of the upper bound UB<sup>σ</sup> on the expected revenue over a session: In time slot t, display ad $a _ { t } = \mathrm { a r g m a x } _ { a } \{ \alpha _ { a } \delta _ { a } \gamma ^ { k _ { a } ( t ) } \}$

Note that

$$
\max _ {a} \{\alpha_ {a} \delta_ {a} \beta^ {t - 1} \gamma^ {k _ {a} (t)} \} = \beta^ {t - 1} \max _ {a} \{\alpha_ {a} \delta_ {a} \gamma^ {k _ {a} (t)} \}.
$$

Therefore,

$$
\underset {a} {\arg \max} \{\alpha_ {a} \delta_ {a} \beta^ {t - 1} \gamma^ {k _ {a} (t)} \} = \underset {a} {\arg \max} \{\alpha_ {a} \delta_ {a} \gamma^ {k _ {a} (t)} \}.
$$

Thus, the policy in Lemma 2 is the same as the following policy: In time slot $t ,$ display ad

$$
a _ {t} = \underset {a} {\arg \max} \{\alpha_ {a} \delta_ {a} \beta^ {t - 1} \gamma^ {k _ {a} (t)} \},
$$

i.e., the ad with the highest expected revenue in that time slot.

From Lemma 1, we have $\mathrm { L B } ^ { \sigma _ { L } } \geq \mathrm { L B } ^ { \sigma _ { U } }$ . Thus, the sequence $\sigma _ { L }$ ofers a tighter value of our lower bound on the optimal expected revenue compared to that ofered by the sequence $\sigma _ { U } \left( \mathrm { i . e . , L B } ^ { \sigma _ { U } } \leq \mathrm { L B } ^ { \hat { \sigma _ { L } } } \leq \mathbb { E } ( \mathrm { R e v } ^ { \sigma _ { L } } ) \leq \mathrm { O P T } \right)$ We therefore choose the sequence that maximizes LB<sup>σ</sup> as our heuristic policy.

Heuristic Policy. In time slot $t ,$ display ad

$$
a _ {t} = \arg \max _ {a} \left\{\frac {\alpha_ {a} \delta_ {a} \gamma^ {k _ {a} (t)}}{(1 - \beta \bar {\lambda}) + \beta \bar {\lambda} \delta_ {a} \gamma^ {k _ {a} (t)}} \right\}.
$$

Let $x = \bar { \lambda } ( 1 - \delta _ { a } \gamma ^ { k _ { a } ( t ) } ) < 1$ . Observe that

$$
\begin{array}{c} \frac {\alpha_ {a} \delta_ {a} \gamma^ {k _ {a} (t)}}{(1 - \beta \bar {\lambda}) + \beta \bar {\lambda} \delta_ {a} \gamma^ {k _ {a} (t)}} \\ = \alpha_ {a} \delta_ {a} \gamma^ {k _ {a} (t)} \frac {1}{1 - \beta x} \\ = \alpha_ {a} \delta_ {a} \gamma^ {k _ {a} (t)} (1 + \beta x + \beta^ {2} x ^ {2} + \dots). \end{array}\tag{7}
$$

We will use Equation (7) to intuitively understand the policy immediately after Corollary 1.

Let $\delta _ { \operatorname* { m a x } } = \operatorname* { m a x } _ { a } \{ \delta _ { a } \}$ . The following result establishes a worst-case performance guarantee for the heuristic policy.

Theorem 2. The heuristic policy is guaranteed to generate an expected revenue that is at least

$$
\max _ {T \in \{1, 2, \ldots \}} \left\{\frac {1 - (1 - \delta_ {\max}) ^ {T}}{\delta_ {\max} T} \cdot (1 - \bar {\lambda} ^ {T}) \right\}
$$

of the optimal expected revenue of problem (6).

The performance guarantee of our heuristic policy in Theorem 2 is attractive for realistic values of the parameters; e.g., if the leaving probability $\lambda \ge 0 . 5$ and the initial click probability $\delta _ { a } \leq 0 . 0 1$ for all ads $\ i \in A$ , then the performance guarantee can be shown to be at least 96%. The following result establishes this claim.

Corollary 1. $I f \lambda \ge 0 . 5 ( i . e . , \bar { \lambda } \le 0 . 5 )$ and $\delta _ { \mathrm { m a x } } \leq 0 . 0 1$ , then the performance guarantee of the above heuristic policy is at least 96% of the optimal expected revenue of problem (6).

We are now ready to summarize the insights gained in our analysis in Sections 4–6:

• A good rule of thumb to sequence in-app fads during a user’s visit is as follows: In each time slot, pick the ad with the highest expected revenue in that slot, adjusted by a factor that captures the efect of displaying that ad on the future expected revenue. When the exposure efect is dominant, the adjustment factor is determined by the expected revenue the ad would make if scheduled ad infinitum assuming that its current click probability remains unchanged. When the sojourn efect is dominant, the adjustment factor is calculated in a similar manner, but with an additional time discounting by the sojourn decay factor $\beta .$

• For scenarios in which the visitor is likely to visit the app for a short time duration (e.g., an app providing weather information), the policy of displaying ads in decreasing order of their expected revenues is near optimal; that is, in each time slot, the policy displays the ad that has the highest expected revenue in that slot.

• For scenarios in which the revenue per click is similar for all ads (e.g., ads for similar products), the policy of displaying ads in the decreasing order of their click probabilities is near optimal.

• For scenarios in which the initial probabilities of a click of all ads are similar and the exposure decay is negligible $( \mathrm { e . g . , }$ a news app in which contentappropriated ads are being served without prior history about the user), the policy of displaying ads in decreasing order of their revenues per click is near optimal.

• The sequencing of ads can influence the time horizon for which the user stays on the app. Thus, eforts to maximize revenue by making the visitor stay on the app for a longer duration (e.g., by improving content) should be in sync with the sequencing of ads. For instance, showing an attractive ad in the first time slot of a user’s visit can generate a click but lead to the visitor leaving the app, thus defeating eforts to make the visitor stay longer. In general, such an adsequencing decision does not maximize revenue for the ad network.

• In general, the expected revenue generated by an optimal ad-sequencing policy is nonmonotonic in time.

For practically reasonable values of the parameters— namely, the user’s probability of leaving the app (λ) and the maximum initial click probability $( \bar { \delta } _ { \operatorname* { m a x } } ) -$ Corollary 1 guarantees an attractive worst case lower bound on the expected revenue of the heuristic. Nevertheless, it is helpful to understand the actual performance of the heuristic and also examine its quality on a wider range of these parameters. We do this next via a computational study.

## 6.2. Computational Experience

In Section 6.2.1, we focus on assessing the quality of our heuristic with respect to changes in the user’s probability of leaving the app (λ) and the maximum initial click probability $( \delta _ { \mathrm { m a x } } )$ . In Section 6.2.2, we evaluate the heuristic with respect to changes in the sojourn decay factor (β) and the exposure decay factor $( \gamma )$

6.2.1. Impact of the Initial Click Probability and the Leaving Probability. The test bed is generated as follows. We consider nine possible values each for λ and $\delta _ { \mathrm { { m a x } } } \mathrm { { : } }$

$$
\bullet \quad \lambda \in \{0. 1, 0. 2, 0. 3, 0. 4, 0. 5, 0. 6, 0. 7, 0. 8, 0. 9 \};
$$

$\delta _ { \operatorname* { m a x } } \in \{ 0 . 0 0 2 , 0 . 0 0 4 , 0 . 0 0 6 , 0 . 0 0 8 , 0 . 0 1 , 0 . 0 2 , 0 . 0 5 ,$ 0.06, 0.08}.

For each combination of values of λ and $\delta _ { \mathrm { m a x } } ,$ 100 instances are generated by repeating the following process 100 times:

• The number of available ads is $2 5 \left( \mathrm { i . e . , } \left| A \right| = 2 5 \right)$

• The revenue per click $\alpha _ { a }$ of ad $a \in A$ is drawn from 10 <sup>×</sup> Beta<sup>(</sup>2, 198<sup>)</sup>. Thus, the mean revenue per click is $1 0 \times 2 / ( 2 + 1 9 8 ) = 0 . 1$

• For a given value of $\delta _ { \mathrm { m a x } } ,$ one of the 25 ads is randomly picked, say, ad ${ { a } _ { 0 } } ,$ and assigned this initial click probability. Then, for each remaining ad $a \in$ $A \backslash \{ a _ { 0 } \}$ , its initial click probability $\delta _ { a }$ is drawn from Uniform $[ 0 , \delta _ { \mathrm { m a x } } ]$

We consider three possible values for each of the two decay factors:

• Sojourn decay factor: $\beta \in \left\{ 0 . 1 , 0 . 5 , 0 . 9 \right\}$

• Exposure decay factor: $\gamma \in \{ 0 . 1 , 0 . 5 , 0 . 9 \}$

Thus, there are $3 \times 3 = 9$ combinations of $\beta$ and $\gamma .$ For each combination of λ and $\delta _ { \mathrm { m a x } } ,$ we therefore have a total of $9 \times 1 0 0 = 9 0 0$ instances, for a total of $9 0 0 \times 8 1 =$ $7 2 { , } 9 0 0$ instances in the test bed. Table 4 summarizes the performance of the heuristic on this test bed. The value in each cell of the table is the average ratio, over the corresponding 900 instances, of the expected revenue generated by the heuristic to an upper bound on the optimal expected revenue (i.e., max $\langle \mathrm { U B } ^ { \sigma } \} \rangle$ ). As can be seen from the table, under the conditions of Corollary 1, the actual expected revenue of our heuristic exceeds 99% of the optimum. For other values of the parameters, the performance of the heuristic is excellent, with the expected revenue exceeding 90% of the optimum.

The two plots in Figure 1 allow us to make two finer observations on the performance of the heuristic with respect to changes in the maximum initial click probability $\delta _ { \mathrm { m a x } }$ and the user’s leaving probability $\lambda ,$ respectively: (1) For a given value of $\lambda ,$ , the performance of the heuristic improves as $\delta _ { \mathrm { m a x } }$ decreases. (2) For a given value of $\delta _ { \mathrm { m a x } } ,$ the performance of the heuristic improves as λ increases.

6.2.2. Impact of the Sojourn Decay Factor and the Exposure Decay Factor. Here, our test bed considers the following wider ranges of the two decay factors:

• Sojourn decay factor: $\beta \in \{ 0 . 1 , 0 . 2 , 0 . 3 , 0 . 4 , 0 . 5 , 0 . 6 ,$ 0.7, 0.8, 0.9}.

• Exposure decay factor: $\gamma \in \{ 0 . 1 , 0 . 2 , 0 . 3 , 0 . 4 , 0 . 5 ,$ $0 . 6 , 0 . 7 , \dot { 0 } . 8 , 0 . 9 \}$

For each combination of the values of $\beta$ and $\gamma ,$ 100 instances are generated by repeating the following process 100 times:

• The number of available ads is $| A | = 2 5$

Table 4. Performance of Our Heuristic on a Wider Range of Parameters: λ and $\delta _ { \mathrm { m a x } }$

<table><tr><td rowspan="2"> $\delta_{\max }$ </td><td colspan="9">λ</td></tr><tr><td>0.1</td><td>0.2</td><td>0.3</td><td>0.4</td><td>0.5</td><td>0.6</td><td>0.7</td><td>0.8</td><td>0.9</td></tr><tr><td>0.002</td><td>0.9923</td><td>0.9981</td><td>0.9986</td><td>0.9989</td><td>0.9992</td><td>0.9994</td><td>0.9996</td><td>0.9998</td><td>0.9999</td></tr><tr><td>0.004</td><td>0.9896</td><td>0.9960</td><td>0.9969</td><td>0.9976</td><td>0.9982</td><td>0.9986</td><td>0.9990</td><td>0.9994</td><td>0.9997</td></tr><tr><td>0.006</td><td>0.9876</td><td>0.9945</td><td>0.9957</td><td>0.9967</td><td>0.9975</td><td>0.9981</td><td>0.9987</td><td>0.9992</td><td>0.9996</td></tr><tr><td>0.008</td><td>0.9847</td><td>0.9920</td><td>0.9938</td><td>0.9951</td><td>0.9963</td><td>0.9972</td><td>0.9981</td><td>0.9988</td><td>0.9994</td></tr><tr><td>0.01</td><td>0.9807</td><td>0.9892</td><td>0.9917</td><td>0.9936</td><td>0.9952</td><td>0.9964</td><td>0.9975</td><td>0.9985</td><td>0.9993</td></tr><tr><td>0.02</td><td>0.9722</td><td>0.9824</td><td>0.9863</td><td>0.9893</td><td>0.9918</td><td>0.9939</td><td>0.9958</td><td>0.9973</td><td>0.9987</td></tr><tr><td>0.05</td><td>0.9446</td><td>0.9619</td><td>0.9708</td><td>0.9776</td><td>0.9831</td><td>0.9876</td><td>0.9915</td><td>0.9947</td><td>0.9975</td></tr><tr><td>0.06</td><td>0.9259</td><td>0.9468</td><td>0.9585</td><td>0.9677</td><td>0.9753</td><td>0.9816</td><td>0.9871</td><td>0.9919</td><td>0.9961</td></tr><tr><td>0.08</td><td>0.9006</td><td>0.9244</td><td>0.9400</td><td>0.9527</td><td>0.9635</td><td>0.9727</td><td>0.9808</td><td>0.9880</td><td>0.9943</td></tr></table>

Figure 1. (Color online) Change in the Performance of the Heuristic with Respect to Changes in the Maximum Initial Click Probability $\delta _ { \mathrm { m a x } }$ and the User’s Leaving Probability λ  
![](/api/attachments/Q8KRRBVX/fulltext/images/1f1f5a1bfceefe416b32680ddfc3bccb36b19b72dcc797100cdfdeee29bb9418.jpg)

![](/api/attachments/Q8KRRBVX/fulltext/images/8d830cdc78d0e4c294b95d13003051524bbeb7661466a5500e5924c7bb8f9a9d.jpg)  
Note. The y-axes show the average ratio of the expected revenue generated by the heuristic to an upper bound on the optimal expected revenue.

• The revenue per click $\alpha _ { a }$ of ad $a \in A$ is drawn from 10 <sup>×</sup> Beta<sup>(</sup>2, 198<sup>)</sup>. Thus, the mean revenue per click is $1 0 \times 2 / ( 2 + 1 9 8 ) = 0 . 1$

• For a given value of $\delta _ { \mathrm { m a x } } ,$ one of the 25 ads is randomly picked, say, ad ${ a } _ { 0 } ,$ and assigned this initial click probability. Then, for each remaining ad $a \in$ $A \backslash \{ a _ { 0 } \}$ , its initial click probability $\delta _ { a }$ is drawn from $\mathrm { U n i f o r m } [ 0 , \delta _ { \mathrm { m a x } } ] .$

We allow three possible values for each of the following two parameters:

• The user’s probability of leaving the app: $\lambda \in \{ 0 . 1$ 0.5, 0.9<sup>}</sup>.

• The maximum initial click probability: $\delta _ { \mathrm { m a x } } \in$ <sup>{</sup>0.002, 0.01, 0.08<sup>}</sup>.

Thus, there are $3 \times 3 = 9$ combinations of $\lambda$ and $\delta _ { \mathrm { m a x } } .$ For each combination of $\beta$ and $\gamma ,$ we therefore have a total of $9 \times 1 0 0 = 9 0 0$ instances, giving us a total of $9 0 0 \times 8 1 = 7 2 { , } 9 0 0$ instances. Table 5 summarizes the performance of the heuristic on this test bed. The value in each cell of the table is the average ratio, over the corresponding 900 instances, of the expected revenue generated by the heuristic to an upper bound on the optimal expected revenue $\mathrm { ( i . e . , \ m a x _ { \sigma } \{ U B ^ { \sigma } \} ) }$ . As can be seen from the table, the performance of the heuristic is excellent, with the expected revenue exceeding 97% of the optimum.

Figure 2 depicts the performance of the heuristic with respect to changes in the sojourn decay factor (β) and the exposure decay factor $( \gamma )$ . We note two observations: (1) For a given value of $\gamma ,$ , the performance of the heuristic improves as $\beta$ decreases. (2) For a given value of $\beta ,$ the performance of the heuristic improves as $\gamma$ decreases.

Remark 1 (User Session Continues Even When an Ad is Clicked). Recall that in our analysis thus far, the app session can end in two ways: either the user naturally leaves the app session or she clicks on an ad. The analysis is significantly simpler if the user’s session ends only if she naturally leaves the session. In other words, clicking on an ad does not cause the session to end. Indeed, in this case, we can show that the following simple policy is optimal for each of the models in Sections 4–6: In time slot t, display the ad with the highest expected revenue in that time slot.

Table 5. Performance of Our Heuristic on a Wider Range of Decay Factors: $\beta$ and $\gamma$

<table><tr><td rowspan="2">β</td><td colspan="9">γ</td></tr><tr><td>0.1</td><td>0.2</td><td>0.3</td><td>0.4</td><td>0.5</td><td>0.6</td><td>0.7</td><td>0.8</td><td>0.9</td></tr><tr><td>0.1</td><td>0.9973</td><td>0.9973</td><td>0.9973</td><td>0.9973</td><td>0.9973</td><td>0.9973</td><td>0.9973</td><td>0.9972</td><td>0.9971</td></tr><tr><td>0.2</td><td>0.9963</td><td>0.9963</td><td>0.9963</td><td>0.9963</td><td>0.9963</td><td>0.9963</td><td>0.9962</td><td>0.9961</td><td>0.9959</td></tr><tr><td>0.3</td><td>0.9952</td><td>0.9952</td><td>0.9952</td><td>0.9952</td><td>0.9952</td><td>0.9951</td><td>0.9951</td><td>0.9949</td><td>0.9947</td></tr><tr><td>0.4</td><td>0.9940</td><td>0.9940</td><td>0.9940</td><td>0.9940</td><td>0.9940</td><td>0.9939</td><td>0.9938</td><td>0.9936</td><td>0.9933</td></tr><tr><td>0.5</td><td>0.9926</td><td>0.9926</td><td>0.9926</td><td>0.9926</td><td>0.9926</td><td>0.9925</td><td>0.9923</td><td>0.9920</td><td>0.9916</td></tr><tr><td>0.6</td><td>0.9909</td><td>0.9909</td><td>0.9909</td><td>0.9908</td><td>0.9908</td><td>0.9907</td><td>0.9905</td><td>0.9901</td><td>0.9895</td></tr><tr><td>0.7</td><td>0.9886</td><td>0.9886</td><td>0.9886</td><td>0.9886</td><td>0.9885</td><td>0.9883</td><td>0.9880</td><td>0.9876</td><td>0.9868</td></tr><tr><td>0.8</td><td>0.9853</td><td>0.9853</td><td>0.9853</td><td>0.9852</td><td>0.9851</td><td>0.9849</td><td>0.9845</td><td>0.9839</td><td>0.9827</td></tr><tr><td>0.9</td><td>0.9800</td><td>0.9800</td><td>0.9798</td><td>0.9794</td><td>0.9794</td><td>0.9790</td><td>0.9784</td><td>0.9774</td><td>0.9756</td></tr></table>

Figure 2. (Color online) Change in the Performance of the Heuristic with Respect to Changes in the Sojourn and Exposure Decay Factors  
![](/api/attachments/Q8KRRBVX/fulltext/images/967489a04a9b93137491617bde2e85b68b915ba9fce120f59917e09ac4704fc7.jpg)

![](/api/attachments/Q8KRRBVX/fulltext/images/9c55e31a18e7d18359f4d286f6db925afc019c1b7d2f38d66af973bbf7605eb5.jpg)  
Note. The y-axes show the average ratio of the expected revenue generated by the heuristic to an upper bound on the optimal expected revenue.

## 7. Extensions: Relaxing Our Assumptions

We now discuss three extensions of our analysis thus far. For each of these extensions, we develop a nearoptimal heuristic policy for the general model in Section 6 that incorporates both the sojourn decay and exposure decay.

• Extension 1. Our analysis thus far made the assumption that, given the user enters a certain time slot, the (conditional) probability of her natural exit (without clicking) from the app session is a constant, λ. This probability may itself change with time (Liu et al. 2010). To capture this situation, we consider slot-specific leaving probabilities $( \mathrm { i . e . , } \lambda _ { i }$ instead of λ). The analysis of this extension is in Section 7.1.

• Extension 2. Until now we only considered click ads, which generate revenue for the ad network through clicks. In the extension analyzed in Section 7.2, we also incorporate display ads, which generate revenue for the ad network only through exposures.

• Extension 3. Our models thus far have been formulated for the ad network, without any direct imposition from the publisher (i.e., owner of the app). It is possible that the publisher may have other sources of ads. Then, it is natural for the publisher to let the ad network manage its ad space only if the revenue received exceeds the utility from the other options the publisher may have. In other words, if the ads displayed by the ad network are not efective, it may be more beneficial for the publisher to choose from other options (e.g., ads for the “advertisement-free” version of the app). Motivated by this reason, Section 7.3 analyzes an extension that considers the following publisher-imposed constraint in our sequencing problem: the expected revenue in each time slot must be no less than a nonnegative threshold.

## 7.1. Slot-Specific Leaving Probability

Let $\lambda _ { t }$ denote the probability that the user naturally concludes her session at the end of time slot t given that she enters that time slot and given that she does not click on an ad. Thus, $\bar { \lambda } _ { t } = 1 - \lambda _ { t }$ denotes the probability that the user enters time slot $t + 1 .$ , given that she enters time slot t. With slot-specific leaving probabilities $\lambda _ { t } ,$ the optimization problem (6) in Section 6 gets modified as follows:

$$
\max _ {\sigma} \left\{\sum_ {i} \alpha_ {(i)} ^ {\sigma} \delta_ {(i)} ^ {\sigma} \beta^ {i - 1} \gamma^ {k _ {(i)} ^ {\sigma} (i)} \prod_ {j = 1} ^ {i - 1} \bar {\lambda} _ {j} \left(1 - \delta_ {(j)} ^ {\sigma} \beta^ {j - 1} \gamma^ {k _ {(j)} ^ {\sigma} (j)}\right) \right\}.\tag{8}
$$

We use the same policy as in Section 6.1 as our heuristic policy: In time slot $t \in \left\{ 1 , 2 , \ldots \right\}$ , display ad $a _ { t } = \arg \operatorname* { m a x } _ { a } \{ ( \alpha _ { a } \delta _ { a } \gamma ^ { k _ { a } ( t ) } ) / ( ( 1 - \beta \bar { \lambda } _ { t } ) + \beta \bar { \lambda } _ { t } \delta _ { a } \gamma ^ { k _ { a } ( \hat { t } ) } ) \}$

The result below establishes the worst-case performance of the heuristic policy under the following technical assumption: For any two ads a and $a ^ { \prime }$ and their respective numbers of exposures $k _ { a }$ and $k _ { a ^ { \prime } } ,$ , we have

$$
\frac {\alpha_ {a} \delta_ {a} \gamma^ {k _ {a} - 1}}{1 + (n - 1) \delta_ {a} \gamma^ {k _ {a} - 1}} \geq \frac {\alpha_ {a ^ {\prime}} \delta_ {a ^ {\prime}} \gamma^ {k _ {a ^ {\prime}} - 1}}{1 + (n - 1) \delta_ {a ^ {\prime}} \gamma^ {k _ {a ^ {\prime}} - 1}}
$$

(<sup>∗</sup>)

$$
\Longrightarrow \frac {\alpha_ {a} \delta_ {a} \gamma^ {k _ {a} - 1}}{1 - \beta \bar {\lambda} _ {t} + \beta \bar {\lambda} _ {t} \delta_ {a} \gamma^ {k _ {a} - 1}} \geq \frac {\alpha_ {a ^ {\prime}} \delta_ {a ^ {\prime}} \gamma^ {k _ {a ^ {\prime}} - 1}}{1 - \beta \bar {\lambda} _ {t} + \beta \bar {\lambda} _ {t} \delta_ {a ^ {\prime}} \gamma^ {k _ {a ^ {\prime}} - 1}},
$$

where n is the smallest integer that satisfies $1 - \beta \bar { \lambda _ { t } } >$ $1 / n$ for all $t \in \{ 1 , 2 , \ldots , T \}$

In words, the technical assumption (<sup>∗</sup>) implies that, given their numbers of exposures, the comparison of two ads based on the criterion in the heuristic policy does not change with the diferent values of $\bar { \lambda } _ { t } , t \doteq$ $1 , 2 , \ldots , T$ . It is easy to verify that this assumption is satisfied if the click probabilities are very small. Since this is indeed the case in practice, the assumption is innocuous.

Theorem 3. Assuming that $\bar { \lambda } _ { t }$ decreases with t and the condition (<sup>∗</sup>) holds, the heuristic policy above is guaranteed to generate an expected revenue that is at least

$$
\max _ {T \in \{1, 2, \dots \}} \left\{\frac {1 - (1 - \delta_ {\max}) ^ {T}}{\delta_ {\max} T} \cdot \left(1 - \prod_ {i = 1} ^ {T} \bar {\lambda} _ {i}\right) \right\}
$$

of the optimal expected revenue of problem (8).

As in Section $^ { 6 , }$ this performance guarantee remains attractive for realistic values of the parameters. The following corollary provides an example:

Corollary 2. Assume that $\bar { \lambda } _ { t }$ decreases with t and the condition (<sup>∗</sup>) holds. $I f \lambda _ { 1 } \ge 0 . 5$ and $\delta _ { \mathrm { m a x } } \leq 0 . 0 1$ , the performance guarantee of the sequence resulting from the heuristic policy is at least 96% of the optimal expected revenue of problem (8).

## 7.2. Incorporating Display Ads

In this section, we extend the optimization problem in Section 6 by allowing the presence of both click and display ads. Click ads generate revenue for the ad network only through clicks (under a cost-per-click model), while display ads generate revenue to the ad network only through exposures (i.e., under a cost-perimpression model). The purpose of display ads is to attract the visitor’s attention during the app session. For such ads, the event of a “click” is naturally replaced by the event of the user “noticing” the ad. Thus, while the probability of a click on a display ad is zero, the probability of the user noticing the ad is subject to the same two decays, namely, the number of time slots the visitor has stayed thus far and the number of exposures of the ad thus far. Let $\boldsymbol { e } _ { a } ( \boldsymbol { k } , t )$ denote the expected revenue per exposure of display ad a when it is shown in time slot t and it is the kth exposure of that ad. Then

$$
e _ {a} (k, t) = \rho_ {a} \beta^ {t - 1} \gamma^ {k - 1},
$$

where $( \mathrm { i } ) \rho _ { a }$ is the revenue per exposure of ad a if it was shown in the first time slot of the app session, (ii) β <sup>∈</sup> <sup>(</sup>0, 1<sup>)</sup> captures the impact of sojourn (time) decay, and (iii) $\gamma \in \bar { ( 0 , 1 ) }$ captures the impact of exposure decay.

To enable the use of a convenient and common notation for both click and display ads, define $e _ { a } ( k , t ) = 0$ if ad a is a click ad and $p _ { a } ( \bar { k } , t ) = 0$ if ad a is the display ad. Thus, given an ad display sequence $\sigma ,$ the expected revenue in time slot i is $\alpha _ { ( i ) } ^ { \sigma } p _ { ( i ) } ^ { \sigma } + e _ { ( i ) } ^ { \sigma } ,$ where $\alpha _ { ( i ) } ^ { \sigma } , p _ { ( i ) } ^ { \sigma } ,$ and $e _ { ( i ) } ^ { \sigma }$ are the revenue per click, click probability, and expected revenue per exposure, respectively, of the ad shown in time slot i. In the presence of both click and display ads, the optimization problem (6) in Section 6 becomes

$$
\begin{array}{c} \max _ {\sigma} \Bigg \{\sum_ {i} (\alpha_ {(i)} ^ {\sigma} \delta_ {(i)} ^ {\sigma} + \rho_ {(i)} ^ {\sigma}) \beta^ {i - 1} \gamma^ {k _ {(i)} ^ {\sigma} (i)} \bar {\lambda} ^ {i - 1} \\ \cdot \prod_ {j = 1} ^ {i - 1} (1 - \delta_ {(j)} ^ {\sigma} \beta^ {j - 1} \gamma^ {k _ {(j)} ^ {\sigma} (j)}) \Bigg \}. \end{array}\tag{9}
$$

Using an analysis similar to that in Section $^ { 6 , }$ we can derive the following lower and upper bounds on the expected revenue of an arbitrary ad sequence σ:

$$
\begin{array}{l} \mathrm{LB} ^ {\sigma} = \sum_ {i} (\alpha_ {(i)} ^ {\sigma} \delta_ {(i)} ^ {\sigma} + \rho_ {(i)} ^ {\sigma}) \gamma^ {k _ {(i)} ^ {\sigma} (i)} (\beta \bar {\lambda}) ^ {i - 1} \prod_ {j = 1} ^ {i - 1} (1 - \delta_ {(j)} ^ {\sigma} \gamma^ {k _ {(j)} ^ {\sigma} (j)}), \\ \mathrm{UB} ^ {\sigma} = \sum_ {i} (\alpha_ {(i)} ^ {\sigma} \delta_ {(i)} ^ {\sigma} + \rho_ {(i)} ^ {\sigma}) \gamma^ {k _ {(i)} ^ {\sigma} (i)} \beta^ {i - 1} \bar {\lambda} ^ {i - 1} \prod_ {j = 1} ^ {i - 1} (1 - \delta_ {\min} \beta^ {j - 1} \gamma^ {j - 1}), \end{array}
$$

where $\delta _ { \mathrm { m i n } } = \operatorname* { m i n } _ { a } \delta _ { a }$

As before, we use the following policy as the heuristic policy. The worst-case performance guarantee ofered by this policy is established in Theorem 4.

Heuristic Policy. In time slot $t ,$ show ad

$$
a _ {t} = \arg \max _ {a} \left\{\frac {(\alpha_ {a} \delta_ {a} + \rho_ {a}) \gamma^ {k _ {a} (t)}}{(1 - \beta \bar {\lambda}) + \beta \bar {\lambda} \delta_ {a} \gamma^ {k _ {a} (t)}} \right\}.
$$

Theorem 4. The sequence resulting from the above heuristic policy is guaranteed to generate an expected revenue that is at least

$$
\max _ {T \in \{1, 2, \ldots \}} \left\{\frac {1 - (1 - \delta_ {\max}) ^ {T}}{T \delta_ {\max}} \cdot (1 - \bar {\lambda} ^ {T}) \right\}
$$

of the optimal expected revenue of problem (9).

The performance guarantee is attractive for realistic values of the parameters. The following corollary provides an example:

Corollary 3. If $\lambda \ge 0 . 5 , \ \delta _ { \mathrm { m a x } } \le 0 . 0 1$ , and $\beta \ge 0 . 8 5$ , the performance guarantee of the sequence resulting from the heuristic policy is at least 74% of the optimal expected revenue of problem (9).

## 7.3. Publisher-Imposed Constraint on the Per-Slot Revenue

For a publisher (i.e., owner of the app), it is natural to let the ad network manage its ad space only if the revenue received exceeds the utility from the other options the publisher may have. For instance, a news app may want to promote content or display its own ads to promote subscriptions. Thus, if the ads displayed by the ad network are not efective, it may be more beneficial for the publisher to choose one of these options. Motivated by these reasons, we consider the following publisher-imposed constraint in our sequencing problem: The expected revenue in each time slot must be at least v, where v is an arbitrary nonnegative threshold.

The extreme case in which the constrained optimization problem is infeasible (i.e., the ad network has no ad with expected revenue v in the first time slot) is not of interest to us, since the ad-sequencing problem itself does not exist. Therefore, we assume that the ad network has at least one ad with expected revenue greater than or equal to v in the first time slot. The constrained version of the optimization problem (6) in Section 6 is

$$
\max _ {\sigma} \left\{\sum_ {i} \alpha_ {(i)} ^ {\sigma} \delta_ {(i)} ^ {\sigma} \beta^ {i - 1} \gamma^ {k _ {(i)} ^ {\sigma} (i)} \bar {\lambda} ^ {i - 1} \prod_ {j = 1} ^ {i - 1} (1 - \delta_ {(j)} ^ {\sigma} \beta^ {j - 1} \gamma^ {k _ {(j)} ^ {\sigma} (j)}) \right\}
$$

$$
\begin{array}{l l} \text { s.t. } & \alpha_ {(i)} ^ {\sigma} \delta_ {(i)} ^ {\sigma} \beta^ {i - 1} \gamma^ {k _ {(i)} ^ {\sigma} (i)} \geq v, \end{array}
$$

for all time slots i in which an ad is shown. (10)

Theorem $5$ establishes the worst-case performance guarantee of the following policy:

Heuristic Policy. In time slot $t \in \{ 1 , 2 , \dots , N \}$ , display the ad with

$$
\max _ {a} \{\alpha_ {a} \delta_ {a} \beta^ {t - 1} \gamma^ {k _ {a} (t)} \},
$$

where N is the largest integer that satisfies

$$
\max _ {a} \{\alpha_ {a} \delta_ {a} \beta^ {N - 1} \gamma^ {k _ {a} (N + 1)} \} \geq v.
$$

Theorem 5. The sequence resulting from the above heuristic policy generates an expected revenue that is at least a factor $\begin{array} { r } { \operatorname* { m a x } _ { T \in \{ 1 , 2 , \ldots , N \} } \{ ( ( 1 - ( 1 - \delta _ { \operatorname* { m a x } } ) ^ { T } ) / ( \delta _ { \operatorname* { m a x } } T ) ) \cdot ( 1 - \bar { \lambda } ^ { T } ) \} } \end{array}$ of the optimal expected revenue of problem (10).

Note that, with $\lambda > 0 . 5 ,$ the worst-case performance guarantee above is at least 50%.

Remark 2 (Estimation of Click Probabilities). Recall the discussion at the end of Section 3, where we provide specific settings in which the exposure efect (respectively, the sojourn efect) is dominant. In such settings, for an ad $^ { a , }$ the click probabilities $p _ { a } ( k )$ for diferent values of k (respectively, $p _ { a } ( t )$ for diferent values of t) can be directly estimated from user click data. In a setting where both the exposure and sojourn efects are significant, the click probabilities $p _ { a } ( k , t )$ for diferent values of k and t can be estimated using the existing ad rotator technology (see Section 1). An ad rotator allows us to display a given set of ads in any predetermined sequence. Thus, for a given time slot $t ,$ we can control the display sequence such that ad a is in its kth exposure in time slot $t , 1 \leq k \leq t$ . This allows us to estimate $p ( k , t )$ for a fixed $t ,$ for diferent values of k. Similarly, the kth exposure of ad $a$ can be controlled to occur in time slot t $( 1 \leq k \leq t )$ . Thus, for a fixed value of $k ,$ the probabilities $p _ { a } ( k , t )$ can be estimated for diferent values of t.

## 8. Concluding Remarks

This study was inspired by conversations with an online supply-side ad network that faced the problem presented in this paper. Essentially, given the extremely competitive nature of this landscape, such firms are continually exploring new ways to better monetize the in-app advertising space. In most cases, current monetization strategies do not explicitly consider time as a resource to be optimized. That is, once an ad is delivered in an ad space, the same ad is displayed for the entire duration of the user’s app session. Our study examines the monetization problem while explicitly managing time as a scarce resource. We model the user’s sojourn as random and optimize the sequence of ads shown to the user to maximize the expected revenue of the sequence. Our analysis reveals a good rule of thumb to sequence ads during a user’s visit: In each time slot, pick the ad with the highest expected revenue in that slot, adjusted by a factor that captures the efect of displaying that ad on the future expected revenue. The adjustment factor depends on the likelihood of the user’s continued stay on the app and on how the chance of a click on the ad is afected with elapsed time and with repeated exposures. In general, the expected revenue per time slot can increase or decrease over time, highlighting the nongreedy nature of the optimal solution. An important contribution of this study is that it exploits a user’s behavior in the app session to dynamically manage the sequence of ads over a session of random length.

For ad networks, the proper sequencing of ads during an app session ofers a fertile technique to improve revenue. One limitation of this study is that it did not consider the possibility that new ads could become available while a user’s session is in efect; that is, the sequence was designed in advance, assuming the set of available ads to be fixed. The availability of new ads could dynamically change the sequence of future ads once the new ads become available.

There are other challenging real-world aspects that may be included in future work. For instance, learning efects can be incorporated. The sequencing problem we addressed in this study could benefit from learning from historical events associated with a specific app–user–ad combination. Of the set of parameters that can be learned and updated, of special interest would be those associated with the click probability values associated with a specific ad, for an app–user combination. For example, if a user prefers travelrelated ads but is seen to usually ignore sports-related ads, this knowledge could be used to refine the clickprobability values associated with diferent genres of ads. Another useful generalization would be to consider more sophisticated payment contracts between the ad network and the publisher. In the sequencing models analyzed in the paper, the ad network obtains revenue from an ad when it is clicked on, and shares a percentage of this revenue with the publisher. Consider a contract where, in addition to this payment, the ad network has to pay the publisher a fixed amount, say, $c _ { a } ,$ if ad a is clicked on. For this setting, the analysis in our paper remains valid. However, for some other payment contracts—for example, one where the ad network pays the publisher for each exposure of an ad—the resulting sequencing problems are fundamentally diferent from the one analyzed in this paper.

## Endnotes

<sup>1</sup> Sometimes an ad network may represent the demand side of the ecosystem. Such an ad network works with ad agencies and integrates with an ad exchange to place ads in an in-app ad space that is auctioned of at the ad exchange. A demand-side ad network usually has no contract with the publisher. The current study considers a revenue optimization problem from the perspective of a supply-side ad network.

<sup>2</sup> We also analyze the case when clicking on an ad does not cause the session to end.

<sup>3</sup> It is also possible that clicking on an ad does not cause the session to end, i.e., the app session ends only if the user naturally leaves the app. The analysis is simpler in this case. See Remark 1 in Section 6 for a discussion.

<sup>4</sup> When a user of an app chooses to “opt out” of targeted advertising (also referred to as “interest-based” or “online-behavioral” advertising), the ad network may not be able to utilize her prior history to serve ads (Ha 2012).

## References

ABC-Netmarketing (2013) The digital marketing glossary: What is ad frequency capping definition? http://digitalmarketing -glossary.com/What-is-Ad-frequency-capping-definition.

Albers S, Passen A (2013) New online algorithms for story scheduling in web advertising. Fomin FV, Freivalds R, Kwiatkowska M, Peleg D, eds. Automata, Languages, and Programming, Lecture Notes Comput. Sci., Vol. 7966 (Springer, Berlin Heidelberg), 446–458.

Baldacci R, Mingozzi A, Roberti R, Wolfler Calvo R (2013) An exact algorithm for the two-echelon capacitated vehicle routing problem. Oper. Res. 61(2):298–314.

Braun M, Moe WW (2013) Online display advertising: Modeling the efects of multiple creatives and individual impression histories. Marketing Sci. 32(5):753–767.

Bucklin RE, Sismeiro C (2009) Click here for Internet insight: Advances in clickstream data analysis in marketing. J. Interactive Marketing 23(1):35–48.

Business Insider (2013) The mobile advertising ecosystem explained. (May 23), http://www.businessinsider.com/mobile -advertising-ecosystem-explained-2013-5.

Chang TS, Wan YW, Ooi WT (2009) A stochastic dynamic travelling salesman problem with hard time windows. Eur. J. Oper. Res. 198(3):748–759.

Chatterjee P, Hofman DL, Novak TP (2003) Modeling the clickstream: Implications for web-based advertising eforts. Marketing Sci. 22(4):520–541.

Cheong T, White CC (2012) Dynamic traveling salesman problem: Value of real-time trafic information. IEEE Trans. Intelligent Transportation Systems 13(2):619–630.

Dasgupta A, Ghosh A, Nazerzadeh H, Raghavan P (2009) Online story scheduling in web advertising. Mathieu C, ed. Proc. 20th Annual ACM-SIAM Sympos. Discrete Algorithms (SIAM, Philadelphia), 1275–1284.

Dawande M, Kumar S, Sriskandarajah C (2003) Performance bounds of algorithms for scheduling advertisements on a web page. J. Scheduling 6(4):373–394.

Dawande M, Kumar S, Sriskandarajah C (2005) Scheduling web advertisements: A note on the MINSPACE problem. J. Scheduling 8(1):97–106.

eMarketer (2014) Want successful mobile ads? (December 17), http:// www.emarketer.com/Article/Want-Successful-Mobile-Ads/ 1011708.

Evans DS (2009) The online advertising industry: Economics, evolution, and privacy. J. Econom. Perspect. 23(3):37–60.

Gerken DA (2008) System and method for selectively acquiring and targeting online advertising based on user IP address. U.S. Patent 7,376,714 B1 filed April 1, 2004, and issued May 20, 2008.

Gesenhues A (2013) Report: App session times run longer on tablets, but app usage is more frequent on smartphones. MarketingLand (November 7), http://marketingland.com/report-3-64362.

GitHub (2014) Banner integration for iOS. http://github.com/ mopub/mopub-ios-sdk/wiki/Banner-Integration-For-iOS.

Goldfarb A, Tucker C (2011) Online display advertising: Targeting and obtrusiveness. Marketing Sci. 30(3):389–404.

Graham K (2015) Common adsense violations on mobile. Monetize-More (June 5), http://www.monetizemore.com/blog/common -adsense-violations-on-mobile/.

Grant R (2014) In-app ads fastest growing sector of mobile advertising. VentureBeat (January 6), http://venturebeat.com/2014/01/ 06/in-app-ads-fastest-growing-sector-of-mobile-advertising/.

Ha A (2012) TRUSTe announces an opt-out system for mobile ads. TechCrunch (April 3), http://techcrunch.com/2012/04/03/ truste-mobile-ads/.

Harvey WM, Despain GL, Lieberman L, Canning BP, Bochman P (2010) Analyzing return on investment of advertising campaign by matching multiple data sources. U.S. Patent 7,729,940 B2 filed April 14, 2008, and issued June 1, 2010.

Hof R (2014) Mobile ad spending to blow past newspapers, magazines, radio this year. Forbes (July 2), http://www.forbes .com/sites/roberthof/2014/07/02/mobile-ad-spending-to-blow -past-newspapers-magazines-radio-this-year/.

Hwang H, Ahn H, Kaminsky P (2013) Basis paths and a polynomial algorithm for the multistage production-capacitated lot-sizing problem. Oper. Res. 61(2):469–482.

Interactive Advertising Bureau (2014a) Global mobile advertising revenue hits \$19.3 billion. http://www.iab.net/about\_the\_iab/ recent\_press\_releases/press\_release\_archive/press\_release/pr -081314.

Interactive Advertising Bureau (2014b) IAB Internet advertising revenue report. http://www.iab.net/media/file/IAB\_Internet \_Advertising\_Revenue\_Report\_HY\_2014\_PDF.pdf.

Klassen J, Yoogalingam R (2009) Improving performance in outpatient appointment services with a simulation optimization approach. Production Oper. Management 18(4):447–458.

Kumar S, Dawande M, Mookerjee VS (2007) Optimal scheduling and placement of Internet banner advertisements. IEEE Trans. Knowledge Data Engrg. 19(11):1571–1584.

Kumar S, Jacob VS, Sriskandarajah C (2006) Scheduling advertisements on a web page to maximize revenue. Eur. J. Oper. Res. 173(3):1067–1089.

Lai G, Margot F, Secomandi N (2010) An approximate dynamic programming approach to benchmark practice-based heuristics for natural gas storage valuation. Oper. Res. 58(3):564–582.

Lieberman D (2013) TV advertising is “surprisingly weak” due to Internet and economy: Analyst. Deadline (March 11), http:// www.deadline.com/2013/03/tv-advertising-weakness-economy -internet-analyst-report/.

Lindsay RT, Carriero T, Juan Y (2010) Measuring impact of online advertising campaigns. U.S. Patent 2010/0306043 A1 filed May 26, 2009, and issued December 2, 2010.

Liu C, White RW, Dumais S (2010) Understanding web browsing behaviors through Weibull analysis of dwell time. Chen HH, Efthimiadis EN, Savoy J, Crestani F, Marchand-Maillet S, eds. Proc. 33rd Annual Internat. ACM SIGIR Conf. Res. Development Inform. Retrieval (ACM, New York), 379–386.

Mak HY, Rong Y, Zhang J (2015) Appointment scheduling with limited distributional information. Management Sci. 61(2):316–334.

Marketwire (2012) Online advertising one of the fastest growing advertising segments. (February 15), http://finance.yahoo.com news/Online-Advertising-One-iw-991038561.html.

Moallemi CC, Saglam M (2013) OR forum—The cost of latency in high-frequency trading. Oper. Res. 61(5):1070–1086.

Mookerjee R, Kumar S, Mookerjee VS (2012) To show or not show: Using user profiling to manage Internet advertisement campaigns at Chitika. Interfaces 42(5):449–464.

Naik PA, Mantrala MK, Sawyer AG (1998) Planning media schedules in the presence of dynamic advertising quality. Marketing Sci. 17(3):214–235.

Newark-French C (2011) Mobile app inventory hungry enough to eat Internet display ad spend. (August 31), http://flurry

mobile.tumblr.com/post/113370456225/mobile-app-inventory -hungry-enough-to-eat-internet.

Robinson L, Chen R (2003) Scheduling doctors’ appointments: Optimal and empirically-based heuristic policies. IIE Trans. 35(3):295–307.

Srinivasan K, Shamos MI (2010) Determining the efectiveness of Internet advertising. U.S. Patent 7,747,465 B2 filed March 13, 2001, and issued June 29, 2010.

Sullivan M (2014) Retargeting is “where the puck is going” in mobile advertising. VentureBeat (November 13), http://venturebeat .com/2014/11/13/retargeting-is-where-the-puck-is-going-in -mobile-advertising/.

Turner J (2012) The planning of guaranteed targeted display advertising. Oper. Res. 60(1):18–33.

Turner J, Scheller-Wolf A, Tayur S (2011a) Location, location, location: An analysis of profitability of position in online advertising markets. J. Marketing Res. 48(6):1057–1073.

Turner J, Scheller-Wolf A, Tayur S (2011b) Scheduling of dynamic in-game advertising. Oper. Res. 59(1):1–16.

Waber A (2014) The shelf life of a mobile ad: Shorter than you may think. MarketingLand (July 23), http://marketingland.com/ shelf-life-mobile-ad-shorter-may-think-91495.
