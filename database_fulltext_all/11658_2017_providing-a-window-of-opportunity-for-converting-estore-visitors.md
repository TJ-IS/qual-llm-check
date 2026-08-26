---
otero_id: 11658
otero_key: "5HEGRBA6"
title: "Providing a Window of Opportunity for Converting eStore Visitors"
authors: "Amit Bhatnagar; Arun Sen; Atish P. Sinha"
year: "2017"
journal: "Information Systems Research"
doi: "10.1287/isre.2016.0655"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/5HEGRBA6/fulltext/images/437174c69ff0d13e24dc2749c3192bf977e174192d5b0a5760f41d05bf808a8d.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Research Note—Providing a Window of Opportunity for Converting eStore Visitors

Amit Bhatnagar, Arun Sen, Atish P. Sinha

To cite this article:

Amit Bhatnagar, Arun Sen, Atish P. Sinha (2016) Research Note—Providing a Window of Opportunity for Converting eStore Visitors. Information Systems Research

Published online in Articles in Advance 26 Sep 2016

http://dx.doi.org/10.1287/isre.2016.0655

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2016, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/5HEGRBA6/fulltext/images/b5e5e6d70b8ad30e210c91944d04fcadfad3403dcad5031110b62e6b28a2753a.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Research Note

# Providing a Window of Opportunity for Converting eStore Visitors

Amit Bhatnagar

Lubar School of Business, University of Wisconsin–Milwaukee, Milwaukee, Wisconsin 53201, amit@uwm.edu

Arun Sen

Department of Information and Operations Management, Mays Business School, Texas A&M University, College Station, Texas 77843, asen@mays.tamu.edu

Atish P. Sinha

Lubar School of Business, University of Wisconsin–Milwaukee, Milwaukee, Wisconsin 53201, sinha@uwm.edu

consumer typically visits an online store a few times before making a purchase decision, and on each visit spends some time browsing the store. The durations of these visits vary not only across consumers but also for a given consumer across multiple visits. We argue that the amount of time that a consumer spends on the first visit to a website depends on how she is drawn to the website. We find that the duration of the first visit is influenced by the advertising tool—banner ad or search engine—used to attract consumers to the website. The durations of subsequent visits are influenced by the durations of earlier visits. The search durations are also influenced by the visit day of the week and time of day. In this paper, we develop a multiple-spell competing risk model to capture the underlying stochastic process, chief elements of which are two interrelated processes: a duration process and a transition process. The multistate, multiple-spell model allows us to identify a window of opportunity, within which the purchase probability is higher than the exit probability. Online salespersons should target site visitors during this window of opportunity. The model, which is calibrated on clickstream data obtained from a major online vendor, can also be used to determine the bid price strategy for search engine ads.

Keywords: online information search; banner ad; search engine ad; competing risk model History: Il-Horn Hann, Senior Editor; Jeffrey Hu, Associate Editor. This paper was received on May 31, 2013, and was with the authors 8 months for 2 revisions. Published online in Articles in Advance September 26, 2016.

## 1. Introduction

Information search plays a key role in consumer decision making. To meet the increased demand for information, there has been a major surge in online initiatives by businesses, resulting in an exponential expansion of the information available on the Web. Competition on the Web has mounted, requiring firms to aggressively promote their websites to their target audience using different communication vehicles in online media, such as email, banners, paid sponsor search, etc. (Wu et al. 2005, Jiang and Benbasat 2007, Parboteeaah et al. 2009). The design of an online information system that effectively employs the different online communication vehicles requires an understanding of consumers’ information search behavior on the Web, especially how consumers respond to the various online communication vehicles (Kuruzovich et al. 2008, Hong et al. 2004, Zhang et al. 2006).

Most of the research studies involving information search behavior are concerned with the determinants of the depth of information search (Zhang et al. 2006). The research focus has been primarily on identifying the different determinants of the depth of information search—such as consumer-specific variables (Ratchford et al. 2003, 2007; Zhang et al. 2006), search cost, product characteristics (Zhang et al. 2006), etc., while the depth of information search has invariably been measured by the total amount of time spent in the entire search process.

For a major purchase, a consumer typically undertakes a number of trips to a store, and on each trip she spends time gathering information. Consumer search measures should ideally take into account the time spent on each separate trip. Traditionally, however, consumer search effort has been measured by the aggregate amount of time spent in the search process.

The existence of clickstream data enables one to study consumer search at the individual visit level (Johnson et al. 2004, Moe 2003, Moe and Fader 2004a, Bucklin and Sismeiro 2003). Consumers can exhibit different website visit patterns. Two individuals can visit an online store multiple times and spend the same aggregate time during the search process, but, at the individual visit level, display widely different behaviors. Such visit patterns result in a widely heterogeneous pattern of website visits.

In this study, we use clickstream data to study consumer search at the visit level. In particular, we examine the underlying factors that contribute to the heterogeneity in website visit dynamics. There could be different determinants of the durations of the first visit, second visit, etc., and the duration of one visit can influence the durations of subsequent visits. One of the factors influencing first visit duration could be the way a consumer arrives at the website. A number of different online advertising tools exist to draw a person to a website. While browsing an online news site, checking stock prices, etc., a person could be drawn by an attractive banner ad for an online business. Another person could go to a search engine and perform a keyword search.

In this paper, we empirically show that the advertising tool—banner ad or search engine—used to attract a consumer to the website plays a major role in determining the duration of the first visit to the website. We also argue that the durations of subsequent visits depend on the durations of previous visits— and, therefore, on the advertising tool—as well as on the time interval between visits. Finally, we examine whether visit durations are influenced by the landing page, the time of day, and the day of the week.

We present an empirical model to study the dynamics of consumer website visits. We develop a multiplespell competing risk model to capture the underlying stochastic process. The major elements of the model are two interrelated processes: a duration process and a transition process. We calibrate the model on clickstream data obtained from a major online vendor of computer and electronic products.

This study has important managerial implications for the design of online salesperson management systems. Our model provides the instantaneous transition probabilities from the search state into the two states of interest—purchase state and the leave and/or revisit state—enabling us to define a window of opportunity. Within this time window, the purchase probability is higher than the exit probability and, therefore, there is a higher likelihood of purchase conversion. This window of opportunity would allow an online salesperson to determine when to approach a site visitor. Also, if the number of site visitors exceeds the number of salespersons, an online salesperson needs to identify the visitor to approach first. Rather than approaching a visitor who came to the website first, he should approach the visitor who is nearing the end of her window of opportunity. The multistate, multiple-spell model that we develop allows us to identify the “window of opportunity.” The results of this study can also be used to determine the bid price strategy for search engine ads.

This paper is organized as follows. In the next section, we provide the background for our study. Section 3 describes the data, and Section 4 describes the development of our model. Section 5 presents the results. Sections 6 and 7 discuss two important managerial implications of our study. Section 8 concludes this paper and identifies future research directions.

## 2. Background

Because of reduced search costs on the Web, consumers who intend to purchase a product engage in extensive online search (Zhang et al. 2006). Prior research studies have examined consumer-specific differences in the use of the Internet as an information source. Klein and Ford (2003) focus on individual differences in the use of the Internet and substitution patterns across different information sources. Ratchford et al. (2003, 2007) show that younger and more educated consumers are more likely to use the Internet to gather information about automobiles, which has an impact on other sources of information.

Bhatnagar and Ghose (2004a) address the role of types of information, product categories, learning, and consumer characteristics (Bhatnagar and Ghose 2004b) on the depth and frequency of search. Park and Fader (2004) study Web browsing behavior across multiple websites; they use browsing behavior at one site to predict browsing behavior at another. Zhang et al. (2006) examine different determinants of consumer search, such as search costs, individual differences, and product characteristics. They find that lower search cost increases search depth, and that consumers who searched in greater depth in the previous session tend to search in greater depth during the current session.

Most of the research studies on online search behavior have conducted investigations at the aggregate level, i.e., they have studied search behavior accumulated across all visits. Yet consumers acquire information from a website in a series of visits (Moe and Fader 2004b). Bucklin and Sismeiro (2003) find that results obtained from aggregate-level site usage data are often misleading. In this study, we investigate visit behavior at the disaggregate level.

Only a few research studies so far have addressed the issue of studying consumer online search behavior at the disaggregated visit level. Johnson et al. (2003) argue that the cognitive costs of using a website decrease with experience. They find that visit duration decreases as the consumer makes more visits to the site. Bucklin and Sismeiro (2003) examine how visit depth and repeat visits influence the visitor’s browsing behavior and find that repeat visits have no effect on page-view durations. They find that visit durations remain the same with increasing frequency. We argue and empirically show that visit durations can increase, decrease, or remain the same with increasing frequency.

Montgomery et al. (2004) also use disaggregated clickstream data in their study. They employ the sequence of previous page viewings to predict the future path that a consumer would take as he navigates through an online retailer’s website. They use a dynamic multinomial probit model of Web browsing, which captures the consumer’s path information (category of previous page viewings), to predict his future navigation path and whether he will make a purchase or not. The authors find that the models that use memory of previous path information outperform the memoryless models by an order of magnitude in predicting paths and purchase conversion. Their study does not investigate the impact of different advertising tools on online search behavior; also, they do not predict visit durations.

Moe and Fader (2004a) find not only that frequent site visitors are more likely buyers but also that, in this group, those who have increasing visit rates are much more likely to purchase than those with decreasing visit rates. In a related study, Moe and Fader (2004b) find that purchase probabilities increase with the number of visits, but subsequent visits have diminishing effects as the customer makes more visits. While we are also interested in purchase probabilities, our focus is on a different set of covariates, such as how a visitor comes to the website, intervisit duration, duration of previous visit, landing page, day of the week, time of day, etc.

Only a few studies include more than one online media tool in their study. Danaher et al. (2010) use banner and other visual ads; essentially, the nature of tools examined is the same. Pauwels and Weiss (2008) include two different media tools, but they do not differentiate between them. De et al. (2010) examine the effects of information technology (IT) use on online sales. They measure IT use by analyzing an online retailer’s server log. The firm provides two tools on its website for facilitating sales: a search box and a recommendation engine. The search function examined by De et al. (2010) is provided through a search box that is internal to the retailer’s website. The recommendation system is also internal to the site. These tools, therefore, are not similar to the types of advertising tools we use in our study—search and banner ads—which are external to the retailer’s site.

Johnson et al. (2003) study the duration of site visits across multiple visits. They put forward the concept of consumer learning, wherein they propose that search costs associated with using a website decrease with experience with the website. As consumers visit a website repeatedly, they learn to use the website. Consequently, they need to spend less time per visit the more they visit the website. Evidence of consumer learning in the context of website search costs has also been found by a number of other researchers (e.g., Zauberman 2003). The amount of effort made in one visit decreases the extent of search needed for subsequent trips. We therefore test whether the duration of the first visit influences the duration of the second visit.

Memory decay with the passage of time is well known (Elliott and Anderson 1995, Gold et al. 2005). Chatterjee et al. (2003) find that under multiple exposures of ads, less frequent visitors are more likely to click on ads than more regular visitors. As the time interval between two visits increases, the amount of information obtained in the first visit and stored in the user’s memory that can be used in the second visit decreases due to memory decay. To explore this issue, we investigate if the time interval between the first two visits has any influence on the duration of the second visit.

Table 1 provides a summary of the related work and shows how our study is different. The columns of the table show (a) whether the online data examined was at the disaggregated visit level or not, (b) the online tools investigated in the study, (c) the determinants of search behavior, and (d) the dependent variables that were examined.

## 3. Data

We obtained clickstream data from a major global firm that serves almost every Fortune 100 company. The firm sells electronic products such as laptops, desktop computers, servers, printers, digital cameras, storage devices, etc., directly to consumers through its e-commerce sites in the United States and other countries. The firm provided us with a data set, which includes a random sample of 2,015 customers, along with all of the clickstream data collected for those customers during a month for computer products.

The firm records consumer interactions with its sites at several Web servers that it runs worldwide. These clickstream data include details about the visitors’ clicks as well as the Web server responses. A clickstream record captures interactions during an entire consumer visit or session; a visitor’s footprints may span several such records. The clickstream data collected by the firm include page request details, visit details, browser information, a unique visit identifier, and other information. Each visitor is identified by a unique global identifier, and each visit is identified separately. They also include the visit start time, visit end time, and the purchase flag.

Table 1 Summary of Related Work in Online Search

<table><tr><td>Research study</td><td>Disaggregated?</td><td>Online tools examined</td><td>Determinants</td><td>Dependent variables</td></tr><tr><td>Bucklin and Sismeiro (2003)</td><td>Yes</td><td>None</td><td>Visit depth, repeat visits</td><td>Stay/exit decision, page view duration</td></tr><tr><td>Johnson et al. (2003)</td><td>Yes</td><td>None</td><td>Number of visits</td><td>Visit duration, purchase probability</td></tr><tr><td>Johnson et al. (2004)</td><td>No</td><td>None</td><td>Baseline search propensity, experience product category, visit probability</td><td>Number of store visits, dynamics of search shopping activity</td></tr><tr><td>Moe (2003)</td><td>Yes</td><td>None</td><td>Number of pages, average time per page, page content, product variety measures, purchase transaction</td><td>Shopping categories</td></tr><tr><td>Moe and Fader (2004a)</td><td>Yes</td><td>None</td><td>Time, visit rate</td><td>Visit frequency, conversion rate</td></tr><tr><td>Moe and Fader (2004b)</td><td>Yes</td><td>None</td><td>Baseline purchase probability, number of visits</td><td>Purchase probability</td></tr><tr><td>Montgomery et al. (2004)</td><td>Yes</td><td>None</td><td>Sequence (category) of page viewings</td><td>Navigation path, purchase conversion</td></tr><tr><td>Pauwels and Weiss (2008)</td><td>No</td><td>Email, search engine</td><td>Referral</td><td>Subscription</td></tr><tr><td>Danaher et al. (2010)</td><td>No</td><td>Banner, other visual ads</td><td>Campaign duration, frequency capping level</td><td>Reach, average frequency of exposure</td></tr><tr><td>De et al. (2010)</td><td>Yes</td><td>Search function, recommendation system</td><td>Directed search usage, nondirected search usage, recommendation system usage</td><td>Sales of promoted/nonpromoted products</td></tr><tr><td>This study</td><td>Yes</td><td>Banner ad, search ad</td><td>Task switching, first visit duration, intervisit duration, day of week, time of day</td><td>First visit duration, second visit duration, purchase probability</td></tr></table>

In addition to collecting clickstream data, the firm obtains promotional data from an advertising firm. The provider uses a promotional tool website to capture the data set generated by visitor’s visits from an affiliate to the company website and includes one record per visit. It includes information on the online promotional tool—banner or search terms—employed to attract the visitor to the site as well as the date and the time of landing. These data have a visit sequence number that specifies the sequence in which the visits took place.

We include the time of day as one of the independent variables to explain individual visit behavior. Most of the individuals in our data visit the website between 7:00 and 22:00 hours. We created a dummy variable called daytime, which was coded as 1 if the visit occurred between 7:00 and 22:00 hours and 0 otherwise. The second control variable was whether the visit took place on a weekday or weekend—it was coded as 1 if it was a weekday and 0 if it was a weekend or holiday. Descriptive statistics of the sample are provided in Table 2.

Table 2 Descriptive Statistics

<table><tr><td></td><td>First visit</td><td>Second visit</td></tr><tr><td>From banner ads</td><td>1,117</td><td>208</td></tr><tr><td>From search ad</td><td>898</td><td>119</td></tr><tr><td>During daytime (7:00–22:00 hours)</td><td>1,726</td><td>267</td></tr><tr><td>During nighttime (23:00–6:00 hours)</td><td>289</td><td>60</td></tr><tr><td>During weekday</td><td>1,474</td><td>238</td></tr><tr><td>During weekend</td><td>541</td><td>89</td></tr><tr><td>Total number of visitors</td><td>2,015</td><td>327</td></tr></table>

## 4. The Model

A typical consumer visits the website of an online retailer a number of times before deciding to purchase or not. The time spent browsing the website would vary not only across different visits for an individual but also across different individuals. Any visit would terminate with either the consumer making a purchase or deciding to take a break and come back for another information-seeking visit. A model should therefore incorporate these dynamics of the search process, namely, the amount of time spent at each visit, transition probability into multiple states at the end of each visit, and the relationship between different visits. We next describe a multistate, multiple-spell model that satisfies these requirements. The approach is somewhat similar to the hazard function methodology that has been used to study network adoption duration (Kauffman et al. 2000), interpurchase time (Chintagunta 1998), search duration (Bhatnagar and Ghose 2004a, b), etc.

The dependent variable of interest is the time $t _ { i }$ spent by an individual i on a visit to a website while searching for information in the prepurchase phase. Two important terms in competing risk methodology are survivor function and transition probability. The transition probability $H ( t _ { i } )$ is the instantaneous probability that an individual i transitions from the current state to another state at time $t _ { i } ,$ given that the individual remained in the current state till $t _ { i } ,$ and is defined as

$$
H (t _ {i}; Z _ {i}) = \lim _ {\Delta t \rightarrow 0} \frac {P (t _ {i} \leq T <   t _ {i} + \Delta t \mid T \geq t _ {i} , Z _ {i})}{\Delta t},\tag{1}
$$

and $Z _ { i }$ is the covariate vector associated with individual i and can shift the transition probability up or down. The survivor function $S ( t _ { i } ; Z _ { i } )$ is the probability that the time $T$ of an event for an individual i is at least as great as a value of $t _ { i } .$ . It can be shown that

$$
S (t _ {i}; Z _ {i}) = \exp \left(- \int_ {0} ^ {t _ {i}} H (x, Z _ {i}) d x\right),\tag{2}
$$

and the probability distribution function $f ( t _ { i } ; Z _ { i } ) =$ $H ( t _ { i } ; Z _ { i } ) \hat { S } ( t _ { i } ; Z _ { i } )$ (Kauffman et al. 2000).

## 4.1. Competing Risk Model

A visit to the website can end in two different ways. At the end of a visit, an individual can decide to purchase from the website or decide to take a break for some time and then come back for another visit. Therefore, an individual can transition from a search spell into one of the two states. Such models where a search state can end in one of multiple states are called competing risk models (Han and Hausman 1990, Wood et al. 1994). In such models, the transition probability of Equation (1) is modified to define a state-specific transition probability, $H _ { j } ( t _ { i } ; Z _ { i } )$ , where j is the state. Let state $j = 1$ represent the purchase state and $j = 2$ represent the leave and/or revisit state. The survivor function for individual i can be specified as

$$
S (t _ {i}; Z _ {i}) = \prod_ {j = 1} ^ {2} S _ {j} (t _ {i}; Z _ {i}),\tag{3}
$$

where $S _ { j } ( t _ { i } ; Z _ { i } )$ is the probability that individual i will survive transition to state j till time $t _ { i } .$ . Suppose there are n individuals in the sample and each individual is identified by data $( t _ { i } , \delta _ { i } ^ { j } , j _ { i } ; Z _ { i } )$ . Here, $\delta _ { i } ^ { j }$ is an indicator variable that is 1 if at time $t _ { i }$ consumer i transitions into state j and 0 otherwise. To ensure that an individual transitions into only one state, we impose the condition $\textstyle \sum _ { j } \delta _ { i } ^ { j } = 1$ . The likelihood function would be

$$
\Lambda = \prod_ {i = 1} ^ {n} \prod_ {j} S (t _ {i}; Z _ {i}) H _ {j} (t _ {i}; Z _ {i}) ^ {\delta_ {i} ^ {j}}\tag{4}
$$

(for details of the competing risk model, please see Hamerle 1989).

While mathematically one can have any number of states, conceptually, a website visitor can transition to only one of two states. Suppose an individual visits a website, stays at the website for some time, and then leaves. This visit can end with the individual transitioning into one of the following three states: purchase, leave and revisit the website after some time, or leave for good. To distinguish between the last two states with complete confidence, an observer will have to observe the visitor for his entire life. However, that is not feasible as all research studies have to stop observing their subjects at some point. A researcher cannot differentiate between a visitor who never returns and the one who returns but after the observation period. That is why the last two states need to be combined into one state. As there are only two possible transition states in our model, we impose the condition $\delta _ { i } ^ { 1 } = 1 - \delta _ { i } ^ { 2 }$

## 4.2. Multiple-Spell Competing Risk Model

Most of the research studies that have used competing risk models have dealt with single-spell data, i.e., time between two purchases, time between mailing of a catalog and consumer response, etc. However, in this case, we have multiple-spell data for each individual as some individuals visit a website a number of times before purchase and the time spent on each visit is of interest to the researchers. One solution would be to treat the different spells independently and estimate the effects of covariates on them separately. However, the different spells of an individual cannot be treated as independent, because the time spent on each visit is influenced by the time spent on previous visits. These different spells are generated by an underlying stochastic process that describes the individual Web visit behavior over time (Hamerle 1989). Suppose an individual i is in the kth spell; his previous history of the process until time $t _ { i } ^ { k }$ is represented by $Y _ { i } ^ { k }$ . Then the transition probability of Equation (1) is modified as

$$
\begin{array}{l}H _ {j} ^ {k} (t _ {i} ^ {k}; Z _ {i} ^ {k}, Y _ {i} ^ {k})\\= \lim _ {\Delta t \rightarrow 0} \frac {P (t _ {i} ^ {k} \leq T <   t _ {i} ^ {k} + \Delta t , J = j \mid T \geq t _ {i} ^ {k} , Z _ {i} ^ {k} , Y _ {i} ^ {k})}{\Delta t}.\end{array}\tag{5}
$$

The transition probability of spell k is now influenced not only by the covariates but also by the previous spells.

For multiple-spell data, an individual would be identified by data $( t _ { i } ^ { k } , \delta _ { i } ^ { k } , j _ { i } ^ { k } , \varepsilon _ { i } ^ { k } , Z _ { i } ^ { k } , Y _ { i } ^ { k } )$ 5. Here, $\varepsilon _ { i } ^ { k }$ is 1 if individual i experiences spell k and 0 otherwise. The indicator variable $\delta _ { i } ^ { k j }$ indicates how episode k ends; i.e., if episode k transitions into state j at the end of time $t _ { i } ^ { k }$ it is 1, otherwise 0. If episode k is not observed, then also $\delta _ { i } ^ { k j }$ is 0. The likelihood model for the multiple-spell competing risk model can be specified as

$$
\Lambda = \prod_ {i = 1} ^ {n} \prod_ {k} \prod_ {j} \bigl (S ^ {k} (t _ {i} ^ {k}; Z _ {i} ^ {k}, Y _ {i} ^ {k}) H _ {j _ {i} ^ {k}} ^ {k} (t _ {i} ^ {k}; Z _ {i} ^ {k}, Y _ {i} ^ {k}) ^ {\delta_ {i} ^ {k j}} \bigr) ^ {\varepsilon_ {i} ^ {k}}.\tag{6}
$$

In the above equation, $S ^ { k } ( t _ { i } ^ { k } ; Z _ { i } ^ { k } , Y _ { i } ^ { k } )$ is the probability of consumer i surviving in spell k until time $t _ { i } ^ { k } ,$ and $H _ { i ^ { k } } ^ { k } ( t _ { i } ^ { k } ; Z _ { i } ^ { k } , Y _ { i } ^ { k } )$ is the instantaneous probability of spell k transiting into state $j$ at time $t _ { i } ^ { k } .$ . In our case, $Y _ { i } ^ { k } = \{ t _ { i } ^ { k - 1 } , s _ { i } ^ { k } \}$ , where $t _ { i } ^ { k - 1 }$ is the duration of spell $k - 1$ and $s _ { i } ^ { k }$ is the time difference between the beginning of spell k and the ending of spell $k - 1$ . For the first spell, $Y _ { i } ^ { 1 } = \{ 0 , 0 \}$

The actual parametric form of the survivor and transition probabilities would depend on the shape of the underlying distribution of spell data, i.e., $f ( t _ { i } ; Z _ { i } )$ We do not know a priori the shape of the distribution of the duration variable. The standard practice is to assume some kind of distribution for the duration variable. After an individual enters a traditional store, her probability of purchasing should increase with the passage of time because she learns about the products available. However, after a certain time, the purchase probability should start declining. We expect the purchase probability to increase as time passes, but after some time, the purchase probability should start declining. Therefore, we need a distribution for spell data that accommodates increasing transition probabilities initially and declining probabilities after a point. Mathematically, the log-logistic distribution fulfills this requirement. For log-logistic distribution, the likelihood of Equation (6) would be specified as

$$
\Lambda_ {l} = \prod_ {i = 1} ^ {n} \prod_ {k} \prod_ {j = 1} ^ {2} \bigg (\frac {1}{1 + (\lambda_ {i j} ^ {k} t _ {i} ^ {k}) ^ {\sigma_ {j} ^ {k}}} \bigg (\frac {\lambda_ {i j} ^ {k} \sigma_ {j} ^ {k} (\lambda_ {i j} ^ {k} t _ {i} ^ {k}) ^ {\sigma_ {j} ^ {k} - 1}}{1 + (\lambda_ {i j} ^ {k} t _ {i} ^ {k}) ^ {\sigma_ {j} ^ {k}}} \bigg) ^ {\delta_ {i} ^ {k j}} \bigg) ^ {\varepsilon_ {i} ^ {k}},\tag{7}
$$

where $\lambda _ { i j } ^ { k } = \exp ( - \beta _ { j } ^ { k } X _ { i } ^ { k } ) , \beta _ { j } ^ { k }$ is a row vector of parameters, $X _ { i } ^ { k }$ is a column vector that has vectors $Z _ { i } ^ { k }$ and $Y _ { i } ^ { k }$ stacked on top of each other, and $\sigma _ { j } ^ { k }$ are scaling parameters. The log likelihood of Equation $( 7 )$ is maximized to estimate elements of $\beta _ { j } ^ { k }$ vectors. One $\beta$ vector would be estimated for each combination of spell k and transition state $j .$

We also test our assumption regarding the shape of the spell data against the following standard distributions:

Exponential:

$$
\Lambda_ {e} = \prod_ {i = 1} ^ {n} \prod_ {k} \prod_ {j = 1} ^ {2} \left(\exp (- \lambda_ {i j} ^ {k} t _ {i} ^ {k}) (\lambda_ {i j} ^ {k}) ^ {\delta_ {i} ^ {k j}}\right) ^ {\varepsilon_ {i} ^ {k}};\tag{8}
$$

Log-normal:

$$
\Lambda_ {n} = \prod_ {i = 1} ^ {n} \prod_ {k} \prod_ {j = 1} ^ {2} \left(\Phi (- \sigma_ {j} ^ {k} \log (\lambda_ {i j} ^ {k} t _ {i} ^ {k})) \right.
$$

$$
\cdot \bigg (\frac {\phi (- \sigma_ {j} ^ {k} \log (\lambda_ {i j} ^ {k} t _ {i} ^ {k}))}{\Phi (- \sigma_ {j} ^ {k} \log (\lambda_ {i j} ^ {k} t _ {i} ^ {k}))} \bigg) ^ {\delta_ {i} ^ {k j}} \bigg) ^ {\varepsilon_ {i} ^ {k}};\tag{9}
$$

Weibull:

$$
\begin{array}{l} \Lambda_ {w} = \prod_ {i = 1} ^ {n} \prod_ {k} \prod_ {j = 1} ^ {2} \Bigl (\exp (- (\lambda_ {i j} ^ {k} t _ {i} ^ {k}) ^ {\sigma_ {j} ^ {k}}) \\ \qquad \cdot \bigl (\lambda_ {i j} ^ {k} \sigma_ {j} ^ {k} (\lambda_ {i j} ^ {k} t _ {i} ^ {k}) ^ {\sigma_ {j} ^ {k} - 1} \bigr) ^ {\delta_ {i} ^ {k j}} \Bigr) ^ {\varepsilon_ {i} ^ {k}}. \end{array}\tag{10}
$$

The above log-likelihoods are maximized with respect to the parameters and are used to find the parameter values.

We estimate all the four models of Equations (7)–(10) and compare them in terms of best fit to the data. We use the Akaike information criterion (AIC) and Bayesian information criterion (BIC) to compare the fit of the different models to the data.

## 5. Results

Out of the 2,015 visitors, very few visited three or more times. We estimated the model for the first two spells because the sample for the third visit is too small for model estimation purposes. Yet the general model that we developed in Section 4 can be estimated for any number of visits. Once the basic multiple-spell, competing risk model is specified, adding the number of states or number of spells (visits) is a straightforward mathematical exercise.

We estimated the four models of Equations (7)–(10) and determined the log-likelihood, AIC, and BIC values. The log-likelihood was the maximum and the AIC and $\mathrm { B I C } ^ { \cup }$ values were the least for the log-logistic distribution, implying that this distribution has the best fit to the spell data. For the rest of this paper, we will limit our discussion to the results of this estimation. The parameter estimates for the first spell are reported in Table 3, and those for the second spell are in Table 4.

First Visit. The parameter estimates from the first visit are reported in Table 4. The first visit can end in two different ways: a consumer can end up purchasing or decide to leave and return later to gather more information. There would be two transitionspecific probabilities that would measure the instantaneous probability of transitioning into the two different states. To interpret the lambda parameter, note that $\lambda _ { i j } ^ { k } = \exp ( - \beta _ { j } ^ { k } X _ { i } ^ { k } )$ . This indicates that as the beta parameter increases, lambda decreases. From

Table 3 Parameter Estimates for the First Visit

<table><tr><td>Covariates</td><td>Parameter</td><td>Standard error</td><td>t stats</td><td>p value</td></tr><tr><td colspan="5">Transition to leave and/or revisit state</td></tr><tr><td>Daytime (1 if daytime, 0 otherwise)</td><td>2.141</td><td>0.279</td><td>7.67</td><td>0.00</td></tr><tr><td>Weekday (1 if weekday, 0 otherwise)</td><td>0.219</td><td>0.085</td><td>2.58</td><td>0.00</td></tr><tr><td>Visit type (1 if banner ad, 0 if search engine)</td><td>-0.384</td><td>0.162</td><td>-2.37</td><td>0.00</td></tr><tr><td>Landing page type = Product</td><td>0.026</td><td>0.185</td><td>0.14</td><td>0.88</td></tr><tr><td>Landing page type = Product category</td><td>0.251</td><td>0.344</td><td>0.73</td><td>0.47</td></tr><tr><td>Landing page type = Information</td><td>0.933</td><td>0.440</td><td>2.12</td><td>0.03</td></tr><tr><td>Sigma</td><td>2.709</td><td>0.089</td><td>30.44</td><td>0.00</td></tr><tr><td colspan="5">Transition to purchase state</td></tr><tr><td>Daytime (1 if daytime, 0 otherwise)</td><td>2.179</td><td>0.131</td><td>16.63</td><td>0.00</td></tr><tr><td>Weekday (1 if weekday, 0 otherwise)</td><td>0.562</td><td>0.273</td><td>2.06</td><td>0.04</td></tr><tr><td>Visit type (1 if banner ad, 0 if search engine)</td><td>0.365</td><td>0.041</td><td>8.90</td><td>0.00</td></tr><tr><td>Landing page type = Product</td><td>0.259</td><td>0.144</td><td>1.80</td><td>0.07</td></tr><tr><td>Landing page type = Product category</td><td>0.153</td><td>0.194</td><td>0.79</td><td>0.43</td></tr><tr><td>Landing page type = Information</td><td>-0.332</td><td>0.163</td><td>-2.04</td><td>0.04</td></tr><tr><td>Sigma</td><td>1.192</td><td>0.244</td><td>4.89</td><td>0.00</td></tr></table>

Table 4 Parameter Estimates for the Second Visit

<table><tr><td>Covariates</td><td>Parameter</td><td>Standard error</td><td>t stats</td><td>p value</td></tr><tr><td colspan="5">Transition to leave and/or revisit state</td></tr><tr><td>First visit duration</td><td>0.137</td><td>0.031</td><td>4.42</td><td>0.00</td></tr><tr><td>Intervisit duration</td><td>0.140</td><td>0.187</td><td>0.75</td><td>0.45</td></tr><tr><td>Daytime (1 if daytime, 0 otherwise)</td><td>0.609</td><td>0.258</td><td>2.36</td><td>0.02</td></tr><tr><td>Weekday (1 if weekday, 0 otherwise)</td><td>-0.451</td><td>0.697</td><td>-0.65</td><td>0.52</td></tr><tr><td>Landing page type = Product</td><td>0.009</td><td>0.008</td><td>1.13</td><td>0.26</td></tr><tr><td>Landing page type = Product category</td><td>0.151</td><td>0.098</td><td>1.54</td><td>0.12</td></tr><tr><td>Landing page type = Information</td><td>2.551</td><td>0.896</td><td>2.85</td><td>0.00</td></tr><tr><td>Sigma</td><td>2.659</td><td>0.249</td><td>10.68</td><td>0.00</td></tr><tr><td colspan="5">Transition to purchase state</td></tr><tr><td>First visit duration</td><td>0.445</td><td>0.123</td><td>3.62</td><td>0.00</td></tr><tr><td>Intervisit duration</td><td>0.722</td><td>0.211</td><td>3.42</td><td>0.00</td></tr><tr><td>Daytime (1 if daytime, 0 otherwise)</td><td>0.923</td><td>0.166</td><td>5.56</td><td>0.00</td></tr><tr><td>Weekday (1 if weekday, 0 otherwise)</td><td>0.019</td><td>0.141</td><td>0.13</td><td>0.90</td></tr><tr><td>Landing page type = Product</td><td>0.928</td><td>0.663</td><td>1.40</td><td>0.16</td></tr><tr><td>Landing page type = Product category</td><td>0.064</td><td>0.326</td><td>0.20</td><td>0.84</td></tr><tr><td>Landing page type = Information</td><td>-0.119</td><td>0.297</td><td>-0.40</td><td>0.69</td></tr><tr><td>Sigma</td><td>1.113</td><td>0.051</td><td>21.82</td><td>0.00</td></tr></table>

Equation (7), we can see that as lambda decreases, the survivor probability increases. Therefore, as the beta parameter increases, the search duration goes up, and the instantaneous transition probability decreases.

We first discuss the parameter estimates for the transition probability for the “leave and/or revisit” state. The scale parameter is positive and significant. Since it is greater than 1, the transition rate is bell-shaped; i.e., it first increases and then decreases. The parameter for daytime is positive, which indicates that the survivor probability of consumers who visit during daytime is higher; i.e., consumers who visit during daytime stay longer than the consumers who visit during nighttime. Similarly, consumers who visit during the weekday spend more time on their first visit compared to consumers who visit over the weekend. This is different from traditional retailing, where most of the shopping is done over the weekend. Access to computers with faster Internet access at the workplace may be one reason why people search for longer durations during daytime and weekdays. Visitors who first land on an information page tend to stay longer compared to visitors who land first on the home page. Whether consumers land on a product page or a product category page has no effect on search duration.

Visit type is a dummy variable that is 1 if the visitor comes from a banner ad and 0 if the visitor comes from a search engine. The coefficient for visit type is negative, implying that individuals who visit the website from a banner ad are likely to search for lower durations on their first visit compared to those who visit the site via a search ad.

We next discuss the parameters for the transition probability of the “purchase” state. The scale parameter is again positive and significant. Furthermore, it is greater than 1, which informs us of a bell-shaped transition rate. The parameters for daytime and weekday are positive and significant. This implies that consumers are less likely to transition into the purchase stage during daytime and weekday. This is an interesting finding. Consumers prefer gathering information during the daytime and weekdays, but prefer purchasing during weekends and nighttime. Visitors who first land on an information page are more likely to purchase compared to visitors who first land on a product, product category or home page. The most interesting finding, based on the positive coefficient for visit type, is that consumers who visit the website by clicking on a banner ad are less likely to transition into the purchase state compared to those who visit the site through a search ad.

Second Visit. The parameter estimates for the second visit are reported in Table 4. The top panel has estimates for the transition probability associated with the transition to the leave and/or revisit state, and the lower panel has estimates for the transition probability associated with the transition to the purchase state. In addition to the control variables for the first visit, we have included the duration of the first visit and the time interval between the two visits as additional covariates.

We first discuss the transition probability associated with leaving and revisiting a third time. The parameter estimates are interpreted as in the first visit. The first visit duration increases the duration of a second visit. The transition probability to leave and/or revisit of a visitor is less during the daytime compared to nighttime. That implies that consumers are likely to search longer during the daytime compared to nighttime. Search durations on the second visit are not influenced by whether it is a weekday or not. Visitors search longer if the landing page is of an information type. The scale parameter is positive and significant. It is also greater than 1, indicating a bell-shaped transition rate.

We next discuss the parameter estimates from the probability of transitioning into the purchase state during the second visit. The probability of transitioning into the purchase state is less during daytime, indicating that consumers are less likely to buy during daytime. This is similar to the first visit. As the time between two trips increases, the probability of transitioning into the purchase state declines, that is, consumers are less likely to purchase, indicating perhaps a loss of interest. The scale parameter is positive and significant. It is also greater than 1, indicating a bellshaped transition rate. This indicates that the purchase probability initially increases as time passes, but after some time, the purchase probability declines.

## 6. Window of Opportunity

An important managerial implication of this study is that the results can be used to determine a window of opportunity during an online search session—the time period during which a customer is most likely to purchase. By plugging the estimated parameter values from Table 3 in Equation (7), one can determine the instantaneous transition probability of any individual into any state at any instant while searching. To illustrate, consider an individual who visits the site during the daytime on a weekday for the first time. Her probability of transitioning into different states at any instant would depend, in addition to weekday and daytime, on whether she came to the website via banner ads or search ads and the duration of the search spell at that instant. In Figure 1, we plot the instantaneous transition probabilities from the search state into the purchase state and the leave and/or revisit state at different points in the first spell.

We can see that the transition probability into the purchase state increases initially, reaches a peak, and then starts declining. Akin to how salespeople in brick and mortar stores approach customers visiting their stores and assist them with the sales process, many online retailers have live customer service representatives who approach site visitors by opening small chat windows on their screens (see Figure 2). Here, the challenge is when to approach the visitors: immediately when a visitor visits the website or after some time. It is not very profitable to approach a customer immediately after she comes to the website because, at this point, her purchase probability is increasing. However, after a point when the purchase probability starts declining, it would be the right time to approach the site visitor. It is therefore important to determine when the purchase probability reaches a maximum, because immediately after this, the purchase probability starts declining. In Figure 1, we represent this point by $t _ { A } .$ . If one knows the distribution of search duration, one can determine the instant at which the transition probability into any state would be the maximum. This can be determined by taking the first derivative of transition probability and equating it to 0. For loglogistic transition rate, one can show that the maximum transition probability would occur when

$$
\begin{array}{r} \frac {\partial}{\partial t _ {i} ^ {k}} \frac {\lambda_ {i j} ^ {k} \sigma_ {j} ^ {k} (\lambda_ {i j} ^ {k} t _ {i} ^ {k}) ^ {\sigma_ {j} ^ {k} - 1}}{1 + (\lambda_ {i j} ^ {k} t _ {i} ^ {k}) ^ {\sigma_ {j} ^ {k}}} = 0, \\ t _ {i A} ^ {k} = \frac {1}{\lambda_ {i j} ^ {k}} (\sigma_ {j} ^ {k} - 1) ^ {1 / \sigma_ {j} ^ {k}}. \end{array}
$$

Figure 1 (Color online) Instantaneous Transition Probabilities for First-Time Visitors Who Visit During a Weekday, Daytime, and Land at an Information Page  
![](/api/attachments/5HEGRBA6/fulltext/images/b2a9cd713b23a83380cd780544df649ad2c2ba29219a4f84b41b37a2d0671d2f.jpg)

Here, $t _ { i A } ^ { k }$ is the instant at which the purchase probability in spell k is at the maximum. By plugging in the estimated parameter values from Table 3, it can be shown that the transition probability of an individual who visits the website for the first time during the daytime on a weekday and lands at an information page would be a maximum at 4.01 minutes if she comes to the website from a banner ad, and 2.79 minutes if she comes after doing a keyword search and clicking on a search ad. Therefore, during the daytime on a weekday, the online customer service representative should approach a first-time online visitor after 4.01 minutes if she comes from a banner ad and after 2.79 minutes if she comes via a search ad.

Site visitors should be approached before their probability of purchasing becomes smaller than the probability of transitioning into the leave state. In Figure 1, we represent this point by $t _ { B } .$ . To determine $t _ { B } ,$ the following equation should be solved numerically:

$$
\frac {\lambda_ {i 1} ^ {k} \sigma_ {1} ^ {k} (\lambda_ {i 1} ^ {k} t _ {i B} ^ {k}) ^ {\sigma_ {1} ^ {k} - 1}}{1 + (\lambda_ {i 1} ^ {k} t _ {i B} ^ {k}) ^ {\sigma_ {1} ^ {k}}} = \frac {\lambda_ {i 2} ^ {k} \sigma_ {2} ^ {k} (\lambda_ {i 2} ^ {k} t _ {i B} ^ {k}) ^ {\sigma_ {2} ^ {k} - 1}}{1 + (\lambda_ {i 2} ^ {k} t _ {i B} ^ {k}) ^ {\sigma_ {2} ^ {k}}}.
$$

Figure 2 (Color online) An Online Chat Window  
![](/api/attachments/5HEGRBA6/fulltext/images/ec2302572b417391a975cc3ed45660b9cfeafdd1350b94442970550357a1db3c.jpg)

The time interval between $t _ { A }$ and $t _ { B }$ is the window of opportunity when a customer service representative should approach an online visitor and try to convert her. This window of opportunity would be different for different individuals based on the day and time of arrival, order of visit, as well as how they come to the website—via banner ads or search ads. Another challenge in the above context is how to allocate site visitors to customer service representatives if there are more visitors than representatives. Site visitors who seem to be reaching the end of their window of opportunity should be approached before others. As Figure 1 shows, the window of opportunity is smaller for visitors who come via banner ads compared to those who come through search ads. The customer service representative should approach banner ad visitors before search ad visitors.

## 7. Price Bidding Strategy for Search Ads

Another interesting managerial implication is that our study helps determine the bid price for search ads. For banner ads, the pricing of ads is determined by the publishing site, which determines the price for each clickthrough, and the online retailer then decides whether to accept that price. For search ads, it is the online retailer that decides what price it would pay for each clickthrough—the bid price. At a search engine, retailers input the search ad, keywords, and the amount that they would pay to the search engine for each customer who clicks on the search ad (Varian

2009). When a visitor to a search engine does a keyword search, the search engine displays ads of all firms that have placed a bid on this keyword, and it orders them in terms of their bid prices.

A retailer can improve the ranking of its search ad by increasing its bid price; however, that entails a higher budget outlay. Considerable research has been carried out in learning the optimum bidding strategy (Edelman and Schwartz 2010, Jerath et al. 2014, Varian 2009). The issue is further complicated by the fact that, similar to TV advertising rates that vary throughout the day/week, the pricing for banner/search ads should also vary throughout the day and week.

One strategy to determine the bid price is to compare the effectiveness of search ads with banner ads. Suppose the probability of purchasing of a visitor who comes to a site via a search ad is $P _ { s } ,$ and that of a visitor who comes via a banner ad is $P _ { b } .$ Assume the retailer is paying x dollars per click for its banner ad at a given publishing site. Then the maximum it should bid for a search ad should be $x P _ { s } / P _ { b }$ . The probabilities of purchase are the instantaneous transition probabilities. These probabilities would vary at different times of the week and day, and are obtained by inputing the parameter estimates from Table 3 into Equation (7). Once the transition probabilities are obtained, the multiplicative factor $( \bar { P _ { s } } / \bar { P _ { b } } )$ can be calculated (see Table 5). This table can be used to determine the maximum bid price for a search ad. For instance, if a firm is paying x dollars per click for its banner ad during the nighttime on a weekday, then it should bid a maximum of 1.258x dollars for a search ad during the same time period.

Table 5 Multiplicative Factor for Bid Price

<table><tr><td rowspan="2">Day of week/ Time of day</td><td colspan="2">Purchase probability</td><td rowspan="2">Multiplicative factor  $(P_s/P_b)$ </td></tr><tr><td>Banner ad  $(P_b)$ </td><td>Search ad  $(P_s)$ </td></tr><tr><td>Weekend nighttime</td><td>0.076</td><td>0.078</td><td>1.021</td></tr><tr><td>Weekend daytime</td><td>0.044</td><td>0.053</td><td>1.205</td></tr><tr><td>Weekday nighttime</td><td>0.031</td><td>0.039</td><td>1.258</td></tr><tr><td>Weekday daytime</td><td>0.072</td><td>0.075</td><td>1.042</td></tr></table>

## 8. Conclusions, Limitations, and

## Future Directions

In this study, we modeled the dynamic effects of an important variable—the online advertising tool a consumer uses to arrive at a site. We found that this variable influences online information search and purchase behavior not only for the first visit, but for subsequent visits as well. We also found that when a consumer leaves the site and returns later, the time interval between the two events affects consumer search behavior in the subsequent visit. Search durations are also found to be influenced by the time and the day of search.

Only a few studies in information systems (IS) have used the hazard function methodology (Kauffman et al. 2000, Lee and Raghu 2014, Oestreicher-Singer and Zalmanson 2013). All of them have used models that are both single state and single spell. In our study, we have used a multiple spell, multistate hazard model. Multistate hazard function models have not been used so far in the IS and marketing areas. We have not only used a multistate hazard model, but have extended it to include multiple spells. When single-spell models are applied to multiple-spell data, like the clickstream data used in this study, “much information about the underlying dynamic process is lost, and ignoring important aspects of this process may lead to false conclusions” (Hamerle 1989, p. 128).

An important methodological contribution of this study, therefore, is the multiple-spell competing risk model that is employed to capture multiple spells (repeat visits) for an online consumer, where each spell can transition to multiple states. Our model incorporates two interrelated processes, a duration process and a transition process, along with a set of covariates, for explaining online search and purchase behavior. We draw from theories of consumer learning and memory decay to explain why the duration of one visit could affect the durations of subsequent visits.

A major contribution of our work is to empirically show that consumers respond differently to the two online advertising tools: banner ad and search terms. We also found that the duration of the second visit is influenced by the duration of the first visit if the first visit resulted from a keyword search. These findings should be useful in choosing an appropriate mix of online advertising tools and also for evaluating their performance.

Another interesting finding is that while consumers are more likely to purchase during weekends, they tend to seek information during the daytime and on weekdays. This is very different from traditional retailing, where consumers do both activities over weekends. The Internet allows them to unbundle these two activities and perform them at different times. Advertising rates at major portals fluctuate throughout the day. This finding would suggest that the online advertising rates should be higher for weekdays and daytime, even though most of the purchasing takes place during the weekends.

The findings of this study have a very interesting managerial implication, namely, the window of opportunity. By knowing the instantaneous transition probabilities for any visitor, managers can plan appropriate strategies. The transition probability to the leave and/or revisit state is always higher for bannerad-induced visits compared to search-ad-induced visits. Since banner-ad-induced visitors are likely to quit earlier, the size of discounts offered to banner-directed visitors could be bigger than the discounts offered to visitors coming through search ads. Just before a visitor is likely to quit, the site can intervene to keep her searching longer by serving an attractive offer via a dynamic ad, which is similar to Web personalization (Tam and Ho 2006).

We know that as the interval between visits increases, the probability of purchase decreases. Therefore, retailers have an incentive to convert a visitor during the first visit. Even if a person leaves without purchasing, there should be a mechanism to lure her back as soon as possible. Through the use of cookies, websites can identify first-time visitors. A website can send these visitors attractive time-sensitive offers to bring them back to the website as quickly as possible. As in the first visit, the size of the offer should be greater for banner-directed consumers because they are less likely to buy even when they visit a second time.

This paper has several limitations that could be addressed in future research. First, we did not have any details of the product that was searched by site visitors; therefore, we could not examine the influence of product on search behavior. Second, the data set that we used does not include any details about the demographics of site visitors. Third, our data set, though comparable in size to those in other studies in the area, does not have a sufficiently large number of consumers visiting three or more times. Fourth, we do not have any data on actual salesperson intervention (the site does not do that presently). Ideally, one should test whether the use of the window of opportunity, which we have identified as the managerial implication of our study, can actually help the firm improve its revenues. Future researchers can collect these data to test whether the model predictions improve the performance of the firm.

We studied only two online advertising tools. There are a number of other advertising tools, such as Microsite, Commission Junction, email ads, etc., and future researchers could try to generalize the findings of our study across those additional tools.

## Acknowledgments

The authors thank the review team, including the senior editor and the associate editor, for their constructive feedback during the review process.

## References

Bhatnagar A, Ghose S (2004a) An analysis of frequency and duration of search on the Internet. J. Bus. 77(April):311–330.

Bhatnagar A, Ghose S (2004b) Online information search termination patterns across product categories and consumer demographics. J. Retailing 80(3):221–228.

Bucklin RE, Sismeiro C (2003) A model of Web site browsing behavior estimated on clickstream data. J. Marketing Res. 40(3): 249–267.

Chatterjee P, Hoffman DL, Novak TP (2003) Modeling the clickstream: Implications for web-based advertising efforts. Marketing Sci. 22(4):520–541.

Chintagunta PK (1998) Investigating purchase timing behavior in two related product categories. J. Marketing Res. 35(1): 43–53.

Danaher PJ, Lee J, Kerbache L (2010) Optimal Internet media selection. Marketing Sci. 29(2):336–347.

De P, Hu Y, Rahman MS (2010) Technology usage and online sales: An empirical study. Management Sci. 56(11):1930–1945.

Edelman B, Schwarz M (2010) Optimal auction design and equilibrium selection in sponsored search auctions. Amer. Econom. Rev. 100(2):597–602.

Elliott SW, Anderson JR (1995) Effect of memory decay on predictions from changing categories. J. Experiment. Psych. 21(4): 815–836.

Gold JM, Murray RF, Sekuler AB, Bennett PJ, Sekuler R (2005) Visual memory decay is deterministic. Psych. Sci. 16(10): 769–774.

Hamerle A (1989) Multiple-spell regression models for duration data. Appl. Statist. 38(1):127–138.

Han A, Hausman JA (1990) Flexible parametric estimation of duration and competing risk models. J. Appl. Econometrics 5(1): 1–28.

Hong W, Thong JYL, Tam KY (2004) Does animation attract online users’ attention? The effects of Flash on information search performance and perceptions. Inform. Systems Res. 15(1):60–86.

Jerath K, Ma L, Park YH (2014) Consumer click behavior at a search engine: The role of keyword popularity. J. Marketing Res. 51(4):480–486.

Jiang Z, Benbasat I (2007) Investigating the influence of the functional mechanisms of the online product presentations. Inform. Systems Res. 18(4):454–470.

Johnson EJ, Ballman S, Lohse J (2003) Cognitive lock-in and the power law of practice. J. Marketing 67(2):62–75.

Johnson EJ, Moe W, Fader P, Bellman S, Lohse J (2004) On the depth and dynamics of online search behavior. Management Sci. 50(3):299–308.

Kauffman RJ, McAndrews JJ, Wang YM (2000) Opening the “black box” of network externalities in network adoption. Inform. Systems Res. 11(1):61–82.

Klein LR, Ford GT (2003) Consumer search for information in the digital age: An empirical study of prepurchase search for automobiles. J. Interactive Marketing 17(3):29–49.

Kuruzovich J, Viswanathan S, Agarwal R, Gosain S, Weitzman S (2008) Marketspace or marketplace? Online information search and channel outcomes in auto retailing. Inform. Systems Res. 19(2):182–201.

Lee G, Raghu TS (2014) Determinants of mobile apps’ success: Evidence from the app store market. J. Management Inform. Systems 31(2):133–170.

Moe WW (2003) Buying, searching, or browsing: Differentiating between online shoppers using in-store navigational clickstream. J. Consumer Psych. 13(1–2):29–39.

Moe WW, Fader PS (2004a) Capturing evolving visit behavior in clickstream data. J. Interactive Marketing 18(1):5–19.

Moe WW, Fader PS (2004b) Dynamic conversion behavior at e-commerce sites. Management Sci. 50(3):326–336.

Montgomery AL, Li S, Srinivasan K, Liechty JC (2004) Modeling online browsing and path analysis using clickstream data. Marketing Sci. 23(4):579–595.

Oestreicher-Singer G, Zalmanson L (2013) Content or community? A digital business strategy for content providers in the social age. MIS Quart. 37(2):591–616.

Parboteeaah DV, Valacich JS, Wells JD (2009) The influence of website characteristics on a consumer’s urge to buy impulsively. Inform. Systems Res. 20(1):60–78.

Park YH, Fader PS (2004) Modeling browsing behavior at multiple websites. Marketing Sci. 23(3):280–303.

Pauwels K, Weiss A (2008) Moving from free to fee: How online firms market to change their business model successfully. J. Marketing 72(3):14–31.

Ratchford BT, Lee M-S, Talukdar D (2003) The impact of the Internet on information search for automobiles. J. Marketing Res. 40(2):193–209.

Ratchford BT, Talukdar D, Lee MS (2007) The impact of the Internet on consumers’ use of information sources for automobiles: A re-inquiry. J. Consumer Res. 34(1):111–119.

Tam KY, Ho SY (2006) Understanding the impact of Web personalization on user information processing and decision outcomes. MIS Quart. 30(4):865–890.

Varian HR (2009) Online ad auctions. Amer. Econom. Rev. 99(2): 430–434.

Wood JW, Holman DJ, Yashin AI, Peterson RJ, Weinstein M, Chang MC (1994) A multistate model of fecundability and sterility. Demography 31(3):403–426.

Wu J, Cook VJ, Strong EC (2005) A two-stage model of the promotional performance of pure online firms. Inform. Systems Res. 16(4):334–351.

Zauberman G (2003) The intertemporal dynamics of consumer lock-in. J. Consumer Res. 30(3):405–419.

Zhang J, Fang X, Sheng ORL (2006) Online consumer search depth: Theories and new findings. J. Management Inform. Systems 23(3): 71–95.
