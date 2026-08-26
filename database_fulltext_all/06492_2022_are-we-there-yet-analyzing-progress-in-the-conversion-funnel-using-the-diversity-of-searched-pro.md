---
otero_id: 6492
otero_key: "XHYVAPFY"
title: "Are We There Yet? Analyzing Progress in the Conversion Funnel Using the Diversity of Searched Products"
authors: "Anat Goldstein; Gal Oestreicher-Singer; Ohad Barzilay; Inbal Yahav"
year: "2022"
journal: "MIS Quarterly"
doi: "10.25300/misq/2022/15524"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# ARE WE THERE YET? ANALYZING PROGRESS IN THE CONVERSION FUNNEL USING THE DIVERSITY OF SEARCHED PRODUCTS<sup>1</sup>

Anat Goldstein Department of Industrial Engineering and Management, Ariel University ISRAEL {anatgo@ariel.ac.il}

Gal Oestreicher-Singer Coller School of Management, Tel-Aviv University, Ramat Aviv, Tel Aviv ISRAEL {galos@post.tau.ac.il}

Ohad Barzilay Similarweb, ISRAEL {ohadbr@gmail.com}

Inbal Yahav Coller School of Management, Tel-Aviv University, Ramat Aviv, Tel Aviv ISRAEL {inbalyahav@tauex.tau.ac.il}

The conversion funnel is a model describing the stages consumers go through in their journey toward a purchase. This journey often lasts several days to weeks and can include multiple visits to a seller’s website. A large body of literature has focused on using observable search patterns to identify consumers’ hidden purchasing stages and to estimate their likelihood of conversion. We propose a novel set of measures to better reveal the consumer’s hidden stage in the funnel. These measures are based on the diversity of the searches that a customer engages in while browsing an e-commerce website, and they include not only the number of different products that are searched for, but also measures that rely on unobserved similarities among products, captured in a product network (in which products are assumed to be “similar” if they are frequently co-searched). We operationalize and evaluate our proposed measures using a large-scale dataset from a medium-sized tourism website used for comparing and booking flights. We estimate a hidden Markov model to show that our proposed diversity measures are associated with progress in the funnel and consumers’ conversion likelihood. Specifically, we show that consumers go through different distinguishable stages (states) in their journey, characterized by different values of our proposed diversity measures. To demonstrate the managerial and business implications of our theory, we show that incorporating search-diversity measures into a baseline prediction model significantly improves the model’s performance in predicting purchase likelihood and churn.

Keywords: Conversion funnel, hidden Markov model, HMM, engagement, search diversity, online marketing, consumer research, tourism, online booking, e-commerce

## Introduction

The conversion funnel (also termed the buying funnel, purchasing funnel, and buying cycle) is a model describing the stages that consumers go through in their journey toward a purchase (Barry, 1987; Howard & Sheth, 1970; Vakratsas & Ambler, 1999). Several variants of the conversion funnel have been proposed, and most include four stages (Jansen & Schuster, 2011): (1) awareness, in which the consumer becomes aware of a need and wants to address this need with a product or a service; (2) research (or interest), in which the consumer becomes interested and engaged in informationseeking regarding products/services that can address the need; (3) decision (or desire), in which the consumer defines a set of options and enters a process of deciding among the options in the set; and finally; (4) purchase (or action), in which the consumer has decided to purchase a particular product/service and takes the next steps toward completing the purchase (e.g., price comparisons or convenience-of-purchase considerations) (Howard & Sheth, 1970; Jansen & Schuster, 2011; Lee & Seda, 2009). These stages may extend over days and even weeks (Bronnenberg et al., 2016; Wiesel et al., 2011). Research suggests that when targeting a specific customer, a seller might benefit from matching its sales and marketing tactics to the customer’s stage in the funnel (Lambrecht & Tucker, 2013). For example, display ads may be suitable for consumers in the awareness stage, whereas price discounts and retargeting may be suitable in the purchase stage (Nimetz, 2007). Moreover, a customer’s stage in the funnel is likely to be predictive of their conversion likelihood (Jansen & Schuster, 2011). For example, a customer in the decision stage, who has already identified several desirable products, may be more likely to make a purchase than a customer who has just become aware of the need for a product. Therefore, the capacity to identify where consumers are located along the conversion process is of practical value to retailers.

Clearly, it is not possible for a seller to directly observe consumers’ cognitive processes to map their progression through the conversion funnel. However, recent advancements in collecting and analyzing consumers’ online footprints have provided sellers with new opportunities that may enable them to approach this capacity. Indeed, a large body of literature has focused on using observable search patterns to identify a given consumer’s hidden stage of shopping and to estimate the likelihood of conversion. These observable patterns include search phrases, which are mapped to possibly relevant funnel stages (Jansen & Schuster, 2011), and engagement metrics such as the history of visits and purchases (Moe & Fader, 2004), visit duration, number of page-views, and types of pages browsed (Moe, 2003; Montgomery et al., 2004).

In this work, we add to this literature by focusing on a previously unexplored behavioral pattern that may be useful for estimating the customer’s progress in the conversion funnel on an e-commerce website: the diversity of searched products, that is, the extent to which the products searched for within a single visit are “different” from each other. The focus on searched-product diversity is motivated by prior works that suggest that consumers in different stages in the funnel engage in different types of searches, and, more broadly, by evidence from the consideration set literature (more details below).

The main goal of our research can be summarized as follows. We aim to establish whether the diversity of a user’s searched products during a visit to an e-commerce website is associated with that user’s progression in the conversion funnel, as well as with the user’s likelihood of making a purchase. To demonstrate the managerial and business implications of our research, we use search diversity to predict the user’s progression in the funnel, as reflected in conversion likelihood.

To achieve this goal, we develop several types of diversity measures. The first type of measure we propose is a straightforward measure reflecting the number of different products searched for within a visit to a website (Bronnenberg et al., 2016; Jang et al., 2007; Sirakaya & Woodside, 2005; Um & Crompton, 1990). Next, we develop a novel class of diversity measures that capture the latent dimensions of product similarity. These measures are extracted from a product network (Goldenberg et al., 2010; Oestreicher-Singer & Sundararajan, 2012), in which products are assumed to be connected if they are searched for one after the other during a single visit. In this case, products that are co-searched more frequently are considered to be more “similar” to one another (in other words, the “distance” between these products within the product network is smaller). Finally, we propose a class of dynamics-based diversity measures to capture the convergence of a potential customer toward a specific product over the course of a single visit (given that the user has performed multiple searches in that visit).

Our research context is the tourism industry—specifically, airline tickets. Airline tickets are often referred to as highinvolvement products (Sirakaya & Woodside, 2005), suggesting that information search plays an important role in the consumer’s decision process in our context (Gu et al., 2012; Spiggle & Sewall, 1987). We collected data from a medium-sized tourism website that serves as a platform for comparing flights and vacation packages offered by different travel agents. Our products are flights, which are characterized by their destinations and by their departure and return dates. Our dataset was collected over a period of four months and includes over 2.3 million flight searches that were conducted during more than 600,000 visits by more than 330,000 consumers (identified by user ID numbers).

Our findings establish a connection between each of the proposed diversity measures and user progression in the conversion funnel. First, using model-free analysis, we show that, in general, for each of our searched product-diversity measures, the diversity of the products a user searches for products tends to decrease as the visit number increases (potentially reflecting a more advanced position in the conversion funnel). Likewise, lower values of search diversity in a single visit are associated with a higher likelihood of making a purchase during that visit. Next, using a hidden Markov model (HMM), we show that it is possible to identify four distinct funnel stages (states) characterized by different distributions of diversity values. For example, the so-called research state is characterized by the highest diversity values, whereas the purchase state is characterized by the lowest diversity values.

To evaluate the capacity of visit-level diversity measures to predict a user’s eventual likelihood of conversion, we predicted users’ likelihood of booking a flight reservation. For this purpose, we first implemented our HMM to predict a consumer’s stage in the funnel, and we show that this information can be translated into a prediction of the consumer’s likelihood of booking a reservation, lending further support to the practical value of identifying consumers’ hidden funnel stages. We subsequently applied classification algorithms that are better suited for directly predicting purchase behavior in managerial settings (e.g., XGBoost and random forest). For each approach, we compared the results of a prediction model that includes our diversity measures to those of a baseline prediction model that includes standard engagement attributes such as the number of searches and visit duration as well as data on the consumer’s previous visits (Goldstein et al., 2016; Raphaeli et al., 2017). Across all approaches we consider, we show that a prediction model that incorporates the proposed diversity measures performs vastly better than the corresponding baseline model. Specifically, in predicting whether a website visit will lead to a flight-ticket reservation, we show that the incorporation of all diversity measures improves the baseline model’s recall and precision significantly (time-series cross-validation). The substantial improvements to the baseline model’s recall and precision imply that the search-diversity metrics we propose are able to more accurately identify converging consumers and thus can enable managers to improve targeted marketing efforts, e.g., by enabling them to avoid targeting users who would have made a purchase anyway, or to focus on targeting users who have the potential to converge toward a purchase but would benefit from an extra “nudge.” Put differently, the proposed diversity metrics allow for more efficient resource allocation and funnel-based targeting.

Our work makes three main contributions: First, we develop novel diversity measures and establish their relevance to the consumer purchasing funnel. Our findings regarding the capacity of searched-product diversity to be indicative of a consumer’s progression through the funnel are likely to be applicable to additional contexts—particularly highinvolvement products. Notably, the measures we propose do not require domain knowledge. In particular, our product-, network-, and dynamics-based measures rely on an induced product network, which “learns” product association from archival data of co-searches. Second, we show that the use of our diversity measures can significantly improve the capacity to predict whether a consumer will eventually make a purchase. Accordingly, our measures can support managers in allocating their targeting efforts. Third, we add to the growing literature on the business implications and the informative value of product networks. Product networks are based on aggregated consumer choices and are therefore influenced by (latent) tastes, interests, socioeconomic status, constraints, etc. Thus, it has been suggested that product-network-based inferences can provide a proxy for these unobserved factors and are therefore effective for estimating product affinity (Sundararajan et al., 2013). Our findings support this assertion. Furthermore, we propose a novel application to leverage this property.

The rest of this paper is organized as follows. In the following section, we review the various literature streams that guide our investigation, and we formulate our research questions. In the subsequent section, we describe the research context and data. In the fourth section, we describe our diversity measures and show how we derive them from the data. The fifth section provides an overview of our analysis procedures. Next, we present our results, showing the usefulness of the measures in revealing consumers’ hidden stages in the funnel and in predicting conversion. Finally, we discuss the implications of our results and provide conclusions.

## Theoretical Background and Research Questions

We draw on and add to three streams of literature. Our focus on search diversity and on the conversion funnel is motivated by a substantial body of research in IS and marketing that aims to estimate where consumers are located in the funnel, as well as by literature that focuses on consumers’ consideration sets (specifically, set size and set diversity). We ground the development of our diversity measures in the literature on product networks and their potential to reflect hidden product similarities. In what follows, we discuss these streams of literature. We then formally present our research questions.

## Clickstream Analysis and the Conversion Funnel

The conversion funnel model is a pivotal theory in the marketing literature (Barry, 1987; Howard & Sheth, 1970; Vakratsas & Ambler, 1999). It is also an important tool for making marketing decisions, which has been widely adopted by managers and marketing professionals for decades (Court et al., 2009; Lambrecht & Tucker, 2013; Lewis, 1985). Like most consumer behavior models, it relies on information processing theory (Bettman et al., 1998).

As elaborated above, different researchers have proposed different variants of the funnel framework, which typically include the following four stages: awareness (or attention), research (or interest), decision (or desire), and purchase (or action) (Jansen & Schuster, 2011). A customer’s stage in the funnel is likely to be predictive of the customer’s conversion likelihood, and therefore the capacity to identify where consumers are located along the conversion funnel is considered to be crucial to the effectiveness of targeted marketing efforts (Lambrecht & Tucker, 2013; Lewis, 1985; Netzer et al., 2008).

In traditional (offline) marketing settings (Abhishek et al., 2012), it is not straightforward to analyze the movement of a consumer down the funnel. However, internet-based and mobile technologies provide a window onto this process by creating new means of analyzing consumers’ consumption-related behavior. These technologies have driven a broad stream of literature that uses websites’ clickstream logs to analyze consumers’ behaviors, goals, and conversion probabilities based on various engagement measures, including visit duration (Bellman et al., 1999; Johnson et al., 2004), number of pages viewed and average page-view duration (Huang, 2009), and depth of search (Johnson et al., 2004). Engagement measures reflect consumers’ levels of involvement and interest while visiting a website (Pagani & Mirabello, 2011; Zhang et al., 2016) and have been identified as important characteristics of information processing while searching for and purchasing products (Cho et al., 2002; Jerath et al., 2014; Moe, 2003). Additionally, they have been shown to be positively correlated with various measures of purchasing behavior (Bellman et al., 1999; Lin et al., 2010; Olbrich & Holsing, 2011). Beyond examining engagement metrics, researchers have also analyzed browsing behavior and conversion likelihood according to movement patterns of consumers along pages during a visit (Clark et al., 2006; Montgomery et al., 2004; Ting et al., 2007; Ting et al., 2009), and consumers’ history of visits (Johnson et al., 2004; Moe, 2003).

Many of the studies that analyze clickstream data to derive information on consumption-related behavior focus on predicting conversion and overlook the process underlying the consumer’s conversion or churn, i.e., the consumer’s transitions between the latent stages of the funnel. Yet another stream of research uses such data to develop different types of insights—namely, to identify different visit goals of consumers (e.g., buying a particular product vs. windowshopping) and to characterize progress in the conversion funnel. For example, a study by Moe (2003) used cluster analysis of clickstream data to cluster consumers’ browsing behaviors into four types of visits (e.g., knowledge building and directed buying), which are characterized by different proportions of homepage views, product-page views, and category-page views. In a subsequent study, Moe and Fader (2004) used these visit types to develop a model that predicts consumers’ purchasing likelihood. The different visit goals identified by Moe (2003) may reflect different stages in the funnel; for example, knowledge building is likely to correspond to the research stage.

More closely related to our context, Jansen and Schuster (2011) used consumers’ search phrases as a means of identifying their locations along the conversion funnel. They manually mapped approximately 40,000 key phrases onto the four stages of the funnel on the basis of several criteria. The authors showed that the different classes of search phrases they had produced were indeed associated with different patterns of consumer behavior, suggesting that their approach had successfully captured the conversion funnel. Yet, the process of mapping key search phrases requires considerable effort and domain knowledge, such that it is not a very practical or generalizable approach for tracking consumer progression through the funnel.

Finally, several studies show that progress in the funnel is related to a converging decision-making process. For example, it has been shown that the consumer’s choice-set becomes smaller as the consumer approaches a conclusion (Bronnenberg et al., 2016; Jansen & Schuster, 2011; Sirakaya & Woodside, 2005; Um & Crompton, 1990). Moreover, as a consumer progresses in the funnel, the values of the searched-product attributes (for example, number of pixels in a digital camera) tend to converge toward their average (Bronnenberg et al., 2016).

The papers cited above identify or allude to links between various aspects of search behavior, consumers’ stages along the funnel, and/or their consumption behavior, and particularly their likelihood of conversion. Thus, those studies suggest that a focus on searched-product characteristics is likely to yield fruitful observations. We contribute to this literature by focusing on a previously unexplored aspect of search behavior—the diversity of searched products—and showing its suitability for characterizing consumers’ progress through the different stages of the conversion funnel.

## Consumers’ Consideration Sets, Convergence, and Search Diversity

Our focus on search diversity is also grounded in the literature on consumers’ consideration sets. Choice consideration studies suggest that a consumer’s decision task involves a set of product alternatives and a set of attributes describing each alternative (Bettman et al., 1998). Studies have shown that the choice task becomes more difficult for the consumers when they face greater complexity, which can manifest in large numbers of alternatives or attributes, uncertainty about the values of the attributes, or low similarity (i.e., fewer shared attributes) across alternative products (Bettman et al., 1998; Lleras et al., 2017). A consumer who faces a more difficult choice task due to a more complex choice set is less likely to exhibit progress in the conversion funnel. Yet studies have identified strategies that consumers use to overcome the difficulty and to reach a decision. For example, consumers who face complexity associated with large numbers of alternatives have been shown to first restrict their attention to a subset of products and then undertake a more detailed analysis of the attributes of this subset (Lleras et al., 2017). This behavior enables the consumer to progress through the conversion funnel (in this case, the consumer may be encouraged to move from researching a large number of alternatives to deciding between a small number of alternatives).

We suggest that the diversity of searched products can serve as another means of expressing the complexity of the choice task, which may reflect the likelihood of progressing (or not progressing) in the funnel. Our focus is not only on the diversity in terms of the number of alternatives searched for (as noted above, decreasing choice-set size has already been associated with progress in the funnel) but also on diversity in terms of the attributes of the products considered. Studies (e.g., Bettman et al., 1998; Chernev, 2003) have found that when the number of shared attributes between alternative products is smaller (i.e., products are less similar) it is more difficult for the consumer to reach a decision. Thus, we propose to measure the similarity between the different searched products. The larger this similarity is, the smaller the diversity is between these products. To estimate product similarity, we draw on previous research on product networks (Oestreicher-Singer & Sundararajan, 2012), i.e., a network in which products are nodes, and connections between products indicate a relationship between them, as elaborated in the following subsection.

We further suggest that looking at the overall level of similarity between products that were searched for during a visit is not enough—the direction in which these similarities change over the course of the visit may also be indicative of progress in the funnel. For example, one consumer may start by searching for products that are very different from one another and then progressively search for more similar products, displaying a converging behavior, while another consumer may start with products that share many attributes and diverge to explore products that are different from one another. Intuitively, one might expect the latter consumer to be less likely than the former consumer to converge toward a purchase in his visit. Indeed, prior studies have shown that search dynamics, i.e., the ways in which search-behavior changes over time, are associated with conversion likelihood and progress in the funnel. These studies (e.g., Bronnenberg et al., 2016; Johnson et al., 2004) tend to look at the dynamics of the search process itself, considering changes in the number of searches and time spent on a searched item, across different visits of a user. Herein, we consider dynamics of searchedproduct diversity not only across visits but also within a single visit; that is, we measure changes in the extent to which products that the user searches for over the course of one visit resemble or differ from one another.

## Product Network Measures as Indicators of Product Similarity

Previous studies have used product networks in various contexts and for various purposes to describe similarities between products. One of the first types of product networks to be explicitly investigated as such captured connections (links) between content websites (i.e., the products in such a network are webpages that link to one another). This type of network has been used for analyzing numbers of blog readers (Mayzlin & Yoganarasimhan, 2012), estimating the quality of content as well as the profits of news websites (Dellarocas et al., 2013), and optimizing advertisement links (Katona & Sarvary, 2008). Another well-known type of product network captures relationships between product pages, linked by recommendations (i.e., a product page contains links to other product pages, selected on the basis of co-purchases or cosearches). Such networks have been used to estimate demand (Carmi et al., 2017; Dhar et al., 2012; Oestreicher-Singer & Sundararajan, 2010) and to estimate the true value of products (the value attributable not only to the revenue associated with a product but also to the revenue it generates by referring the user to additional products of interest) (Oestreicher-Singer & Sundararajan, 2012). Product networks have also been used to capture product comparisons for estimating product sales (Leem & Chun, 2014; Meiseberg, 2016; Zhang et al., 2013) and for capturing competition between products (Ringel & Skiera, 2016). Another stream of research uses product networks together with social networks and studies the effect of these combined networks on the efficiency and effectiveness of the exploration process (Goldenberg et al., 2012; Grange & Benbasat, 2013). Regardless of whether a product network is constructed on the basis of page links, copurchases, co-searches, or product comparisons, the associations between the products in that network are anchored in latent (unobserved) relationships among those products (Sundararajan et al., 2013).

We contribute to the product network literature by proposing a novel usage of the product network—namely, estimating a consumer’s progress in the conversion funnel. In particular, we use a product network that captures similarities between products based on whether many users searched for those products one after the other during a single visit. We hypothesize that the similarity measures provided by the product network also reveal the user’s latent considerations, and thus allow us to capture consumer convergence toward a decision.

## Research Questions

As noted above, the main goal of our research is to establish whether the diversity of a user’s searched products during an online visit can be related to the user’s position in the conversion funnel, as well as to the consumer’s likelihood of making a purchase during that visit. Accordingly, our core research questions are as follows:

RQ1a: How is the diversity of a consumer’s product searches in an e-commerce website associated with the consumer’s stage in the funnel?

RQ1b: Are lower (higher) levels of a consumer’s searchedproduct diversity in an e-commerce website associated with higher (lower) purchase likelihoods?

In addition, to show the managerial importance of our focus on diversity measures, we evaluate the capacity of visit-level diversity measures to predict a user’s eventual likelihood of conversion. Thus, our second research question is:

RQ2: Does the inclusion of consumers’ searched-product diversity measures in predictive models of conversion improve conversion prediction?

Clearly, in order to match a consumer’s position in the funnel to the diversity of their searched products, it is necessary to operationalize the concept of a funnel as well as the concept of diversity. To this end, we define a “funnel” as a set of website visits made by a single user with no more than 10 days between two consecutive visits. The choice of 10 days conforms to industry conventions and was made jointly with the tourism company whose data we use for this research. To operationalize searched-product diversity, we develop three classes of measures, as outlined above: measures based on the number of different products that a consumer looks for; measures derived from the product network (that is, the latent similarity between the products); and a measure based on diversity dynamics (that is, whether the diversity of a consumer’s searched products increases or decreases over time). These measures are discussed in detail in the Developing Diversity Measures section.

## Research Context and Data

This study is based on 3.5 months (September 2015- December 2015) of data collected from a medium-sized tourism website that serves as a platform for comparing and booking flights by different travel agents. The website had no recommendation system at the time of the study. In addition, no marketing campaigns were launched in the months before the study or during the time of the study.

Our dataset includes 2,379,834 searches for flights. Every search is characterized by the time of the search, the destination country and city, the departure and return dates, the average price of the searched flights, whether the search resulted in a flight reservation, and the reservation time (if present). In total, 1,482 unique cities and 160 unique countries were searched.

We aggregated searches and represented them at the visitgranularity level (where a visit, or session, was identified by a session ID). This aggregation resulted in a total of 611,308 visits conducted by 332,393 unique consumers (where each customer was identified by a user ID). Of the visits, 20,561 (3.3%) ended with a reservation. When a consumer made multiple visits to the site, we aggregated consecutive visits that were no more than 10 days apart into what we called a “funnel” for that consumer. This aggregation resulted in a total of 395,322 funnels. Table 1 presents descriptive statistics of several key attributes of the visits. Table 2 summarizes information on consumers’ funnels. In addition to the attributes in Table 1, each visit was characterized by the following (categorical) attributes:

• Start time: date and time of the visit

• Day of week: the day of the week in which the visit started

• Time of day: Whether the visit started during the morning, afternoon, evening, or night

• Flight season: the season (winter, spring, summer, or fall) of the first searched flight in the visit

• Cities: a list of the cities that appeared in the visit, presented in the order in which they were searched

• Countries: a similarly ordered list of the countries that appeared in the visit

• Flight dates: a list of the departure and return dates searched during the visit, presented in the order in which they were searched

Visit outcome: whether the visit ended with a reservation, ended with churn (i.e., the consumer did not revisit the website for at least ten days), or was followed by a subsequent visit.

<table><tr><td colspan="7">Table 1. Descriptive Statistics of Visit Attributes</td></tr><tr><td>Attribute</td><td>Description</td><td>Mean</td><td>SD</td><td>Median</td><td>Min</td><td>Max</td></tr><tr><td>Visit duration</td><td>The total duration of the visit (seconds) measured between the start times of the first search and the last search</td><td>522.08</td><td>877.7</td><td>207</td><td>1</td><td>23,094</td></tr><tr><td>Number of searches</td><td>The total number of searches conducted during the visit</td><td>3.92</td><td>4.62</td><td>3</td><td>1</td><td>200</td></tr><tr><td>Time-to-flight</td><td>The time from the visit start date to the first searched departure date (hours)</td><td>55.25</td><td>75</td><td>21.94</td><td>0.5</td><td>366.7</td></tr><tr><td>Average searched travel duration</td><td>The average travel duration searched in days</td><td>8.60</td><td>24.34</td><td>5</td><td>1</td><td>345.14</td></tr><tr><td>Previous visits</td><td>The number of previous visits of the consumer prior to the current visit</td><td>2.85</td><td>10</td><td>0</td><td>0</td><td>355</td></tr><tr><td>Searches in previous visit</td><td>Number of searches in the previous visit</td><td>3.17</td><td>4.00</td><td>2</td><td>0</td><td>200</td></tr><tr><td>Number of previous reservations</td><td>Number of previous reservations of the user</td><td>0.11</td><td>0.85</td><td>0</td><td>0</td><td>43</td></tr><tr><td>Average price</td><td>The average price of flights searched during the visit (for visits that include price data)</td><td>$519.40</td><td>$302</td><td>$448.09</td><td>$22.90</td><td>$9327</td></tr></table>

Note: The different analyses throughout this paper use different subsets of this dataset. Appendix F provides additional descriptive statistics for each subset and summarizes when each subset is used.

<table><tr><td colspan="2">Table 2. Descriptive Statistics of Funnels</td></tr><tr><td>Attribute</td><td>Value</td></tr><tr><td>Number of funnels</td><td>395,322</td></tr><tr><td>Number of funnels (percentage) that end with a reservation</td><td>20,561 (5.2%)</td></tr><tr><td>Number of visits in a funnel</td><td>Mean: 1.54 median: 1Min:1Max:78</td></tr><tr><td colspan="2">Multi-visit funnels (defined as funnels with at least three visits)</td></tr><tr><td>Number of multi-visit funnels</td><td>38,340</td></tr><tr><td>Number of visits</td><td>209,909</td></tr><tr><td>Number of visits (percentage among all multi-visit funnels) that end with a reservation</td><td>4,737 (2.3%)</td></tr><tr><td>Number of visits in funnel</td><td>Mean: 5.47Median: 4Min: 3Max: 78</td></tr></table>

\*Out of these visits, 126,330 visits include flight prices. Visits of funnels that do not include flight price data are excluded from analyses that use price-related variables

## Developing Diversity Measures

In our context of flight searches, the searched product—a flight—is characterized by the destination (city and country) and by the flight dates (departure and return dates). We propose three approaches for measuring diversity, each reflecting a different aspect of diversity: a count-based approach, a network-based approach, and a dynamics-based approach (where the latter approach accounts for changes in search diversity during a visit). In developing these diversity measures, we followed three guiding principles: First, the measures should be generalizable and applicable to contexts other than tourism. Second, they should not require domain knowledge (for example, in the tourism context, developing the measures should not require having prior knowledge about destinations). Third, the measures should be easy-touse in a production environment. For example, they should not be computationally intensive.

## Count-Based Measures

A straightforward means of measuring diversity is simply to count the number of different items the consumer has searched for. In that sense, a visit in which a user searches for Paris, Rome, and London could be considered more diverse than a visit in which a user searches for Paris three times. In our context, we define “different” in various ways. For example, a user can search for two different locations (e.g., London and Paris) or search for the same location but on two different dates. Hence, we take into account the following attributes:

• Number of unique searched cities

• Number of unique searched countries

• Number of unique flight dates (unique combinations of departure and return dates)

The advantage of this method is its simplicity. However, this count-based approach only considers whether products are identical or not; it does not account for the level of similarity between searched cities, countries, and flight dates.

## Network-Based Measures

In designing our network-based measures, we aimed to capture a nuanced indication of the level of similarity between different searches. The similarity between search dates is simple to measure—namely, as the number of days between two searched dates. However, the similarity between destinations (cities or countries) can be defined along a variety of dimensions: based on geographic distance, based on the type of destination (large city or beach resort, for example), or based on other nonintuitive, unobserved dimensions. Accordingly, to effectively capture all (intuitive and nonintuitive) dimensions of similarity, we relied on the use of a product network (Oestreicher-Singer & Sundararajan, 2012), i.e., a network in which products are nodes, and connections between products indicate frequent co-purchases or co-searches.

First, we constructed the network of “destinations” in our dataset. For robustness, we repeated the process twice, creating two different networks of destinations. In the first network, destinations were defined as cities, and in the second network, destinations were defined as countries. We defined any two destinations (cities or countries) as “connected” if they were searched for one after the other by a single user in a single visit. Specifically, given a graph populated by all cities (countries) that were searched for in our dataset, we created the connections among the cities (countries) as follows: For a given visit, we started with the first searched city (country). For each subsequent searched city (country), an edge was created between the preceding city (country) and the new one. The rationale behind this procedure was to capture the user’s associative processes as she considers product after product over the course of a visit. Each edge between two cities (countries) was assigned a weight, corresponding to the number of times the two cities (countries) were searched for one after the other in the data.

Figure 1 illustrates how the network was created. This figure corresponds to the process of constructing a network based on two sessions (visits) conducted by different users: visit #1 and visit #2. We began by constructing a network for visit #1, which contains the following search destinations (in the following order): Rome, Rome, Paris, London, and London. Based on this session we added to the network an edge from Rome to Paris and an edge from Paris to London. Thus far in our calculations, the weight of each edge is one, because in visit #1 each set of consecutive searches was carried out once (Figure 1a). Next, we proceeded to incorporate the data for visit #2, in which the user searched for Paris, London, London, Rome, Rome, and Seoul. Based on this sequence, we increased the weight from Paris to London by one (weight = 2), added an edge from London to Rome (weight = 1), and added an edge from Rome to Seoul (weight = 1). Updates are shown in red (Figure 1b). We note that the order in which the cities are searched for is important; that is, searching for Rome, Paris, and then Prague is different from searching for Prague, Rome, and then Paris. This is because the order of searches reflects the associativity or interchangeability of searched cities, as perceived by the consumer.

Using this process, we created two product networks—one for cities and one for countries—based on the data from all sessions. The networks are undirected; however, for robustness, we also developed directed networks in the same manner, which produced results similar to those obtained with the undirected networks (results available upon request).

Next, for each network, and for each pair of nodes (cities or countries) in the network, we calculated the network distance between those two nodes as the length of the shortest path between them. In our calculations, the “length” of an edge is defined as 1 divided by the weight of the edge.

![](/api/attachments/XHYVAPFY/fulltext/images/ada18f04ce37c3dcc1635fb5eb308c7c8e26273fb9d3b39fd365f4e25aa741ba.jpg)  
A: The network after visit #1

![](/api/attachments/XHYVAPFY/fulltext/images/3e47dfa1ed7abfb6bab9070a189de5d4dc1584aea843209f1546edc5bd7b73d1.jpg)  
B: The network after visit #2  
Note: (A) The network after visit #1, in which a consumer searched for cities in the following order: Rome, Rome, Paris, London, and London. (B) The network after visit #2, in which a consumer searched for cities in the following order: Paris, London, London, Rome, Rome, and Seoul.

## Figure 1. Development of the City Network

Thus, if two products are frequently co-searched for, the distance between them is smaller than the distance between two products that are rarely searched for together.<sup>2</sup> For example, in our dataset, Paris, and Rome were searched for together 1,963 times, whereas Paris and Nice were searched for together 238 times. Hence, in our product network, Paris is considered to be closer to Rome (distance of 1/1963 = 0.00051) than to Nice (the distance between Paris and Nice is 1/238 = 0.0042).

Then, for each website visit, we calculated the following measures:

Average city (country) distance from previous: For each city (country) searched for in the visit, we calculated its network distance from the previous city (country) searched for in that visit. We then summed up those distances and calculated their average.

Total unique cities (countries) distance: The sum of network distances between each unique city (country) in the visit and the first city (country) searched. For example, if the destinations the user searched for were “Paris, Paris, Rome, Rome, London,” we summed up the distances between Paris and Rome and between Paris and London. We calculated the distance to the first city (country) and not to the previous city (country) to reflect the idea that the destination that initiated the search is the destination that is most desirable to the consumer.

• Average date distance from previous: The average of the absolute differences between each searched departure date and its previous departure date in the visit plus the average of the absolute differences between each searched return date and its previous return date in the visit.

Total unique date distance from first: The sum of the absolute differences between each unique searched departure date and the first searched departure date in the visit plus the sum of the absolute differences between each unique searched return date and the first searched return date in the visit.

Notably, in contrast to the count-based measures, the network-based measures enable the diversity of a set of two or more products to be represented as a nuanced continuous variable, capturing the products’ unobserved similarities.

## Dynamics-Based Diversity Measures

Diversity values may change as the consumer progresses in the funnel. Specifically, decreasing or increasing diversity in the consideration set may be indicative of a consumer’s convergence toward a decision, or divergence away from one. Our clickstream data enable us to capture such changes within a single visit. To this end, we developed the following measures, which reflect changes (specifically, increases and decreases) in search diversity in the scope of a single visit:

Mean difference in city distances (/country distances /flightdate distances): The average distance differences between two pairs of consecutive searches (cities/countries/flight dates) during the visit. Note that this number can be either positive or negative (if overall there are more decreases). For example, if a consumer searched for “Paris, Nice, Paris, Rome,” then the corresponding distances in the city network are 0.0042 (Paris, Nice), 0.0042 (Nice, Paris), and 0.00051 (Paris, Rome). In this case, the mean difference in city distances is computed as:

$$
[ (0. 0 0 4 2 - 0. 0 0 4 2) + (0. 0 0 0 5 1 - 0. 0 0 4 2) ] / 2 = - 0. 0 0 1 8 5.
$$

It should be noted that measuring distance changes requires that the visit include at least three searches. For visits with fewer than three searches, we assigned a value of zero to each of the three dynamics-based measures.

## Methodology

In what follows, we elaborate on our empirical strategy. To investigate the relationships between search diversity measures, conversion likelihood, and stage in the funnel (RQ1), we first present model-free analysis followed by HMM analysis. Then, we incorporate our diversity measures into models for conversion prediction (an HMM-based model as well as models based on alternative classification algorithms), and we evaluate the models’ predictive performance (RQ2).

## Model-Free Analysis

To provide initial evidence to support the association between a consumer’s search diversity and their position in the funnel (RQ1a), we investigated the changes in the values of the different search-diversity measures along a given user’s “funnel.” As noted above, for the purpose of this analysis, a funnel is defined as a set of visits carried out by a single user, with no more than 10 days between two consecutive visits. Thus, we compared the values of the search-diversity measures corresponding to a user’s early visits with the values corresponding to the user’s later visits.

Further, to address RQ1b—the association between the consumer’s search diversity and their likelihood of conversion—we distinguish between website visits that ended with flight reservations and those that did not, and compare the mean values of search-diversity measures between the two groups of visits. Second, for each diversity measure, we investigate how different levels of the measure are associated with reservation likelihood. For robustness, we analyze RQ1b with survival (hazard) analysis in Appendix A.

## Hidden Markov Model

## Modeling Consumers’ Positions in the Conversion Funnel

In the marketing literature, HMMs serve as the canonical approach to model consumers’ progression through the hidden stages (states) of the conversion funnel based on their buying behavior (Abhishek et al., 2012; Ghose et al., 2017; Montgomery et al., 2004; Netzer et al., 2008; Todri et al., 2019). An HMM is a model of a Markov process, whose states are unobserved (latent), but can be inferred via their probability distribution over another set of observed signals (Rabiner, 1989; Rabiner & Juang, 1986). In presenting our model and results, we followed Todri et al. (2019), with the relevant changes.

We use an HMM to capture the latent, cognitive stages (states) of the consumer’s journey through the conversion funnel, using clickstream-observable signals that capture the consumer’s search diversity during a visit. In other words, we decompose the diversity distributions according to the different stages in the funnel that are represented by different states of the HMM. We also take into account additional observable factors that may influence the consumer’s cognitive state (and thus their progression through the funnel).

In constructing the model, we considered all consumer funnels that include at least three visits (referred to as “multivisit funnels” in Table 2). This restriction allowed us to avoid short funnels that might be insufficient to capture the entire process of progression in the funnel. We assume that in each visit, the consumer resides in one of the four latent states of the funnel— awareness, research, decision, or purchase—and that at the end of the visit, the user may (or may not) transition to a different state. (We note that, as our unit of analysis is a visit, each visit is assumed to correspond to one state of the model; we do not attempt to identify transitions between cognitive states that take place within a single visit.)

Each funnel path is initiated the first time the consumer enters the website or when the consumer first enters the website after not entering it for more than 10 days. The funnel ends after the visit in which the consumer made a reservation or after the consumer churned, i.e., did not engage with the website for more than ten days. For each visit in the funnel, we calculated the different count-based, network-based, and dynamics-based measures. We emphasize that whereas these diversity values are observed, the consumer’s state in the funnel—awareness, research, decision, or purchase—is a latent, cognitive state, inferred statistically. Likewise, the decision to transition from one state to another is not observed; however, we assume that this decision may be influenced by certain factors that are observable in our data, which we measure for each visit. These factors include the prices of the flights that the consumer encounters during their visit (such that, for example, encountering a lower price than one has encountered previously may be expected to encourage the consumer to proceed to the next stage); as well as the time-to-flight, i.e., the amount of time between the current visit and the consumer’s target flight dates (where a shorter time-to-flight may indicate a more urgent search, thus encouraging the consumer to proceed to the next stage in the funnel).

The four states of the proposed HMM and the transitions between them are outlined in Figure 2 (The figure is inspired by the model presentation in Todri et al., (2019). The (observed) diversity values corresponding to the visits are represented in rectangles. As illustrated in the figure, our model does not impose assumptions a priori regarding the trajectory of the consumer’s journey, i.e., the order in which users transition from state to state. In particular, we do not assume that the user must progress sequentially through the stages of the funnel. Rather, the user can begin in any state, and can move to any state, including returning to “earlier” states. For example, a consumer in the decision state may become aware of an additional, unexplored, destination (or class of alternative destinations), and may then return to the research state to collect information about those alternatives. A consumer might also skip directly from the research state to the purchase state, without passing through the decision state.

Moreover, we do not make any assumptions regarding the diversity values that characterize each state. However, the conversion funnel literature suggests that we are likely to observe certain general patterns as follows. First, according to the literature, while in the awareness stage, consumers just become aware of the product and are expected to conduct only a few searches, consumers in the research stage collect information about a product type and compare the attributes of competing brands. In our context, consumers in the research state are collecting information on existing flights. We expect these consumers to compare a high number of destinations (cities/countries) and flight dates and expect high variety among them. Once the consumer has collected enough information, they can transition to the decision state, in which, according to the literature (Jang et al., 2007; Jansen & Schuster, 2011), the consumer reaches a subset of relevant products (for example, a consumer searching for a smartphone may narrow their choiceset to two or three models). In our context, we anticipate this state to be characterized by a decrease in the diversity of searches. In particular, compared with a visit in the research state, a visit in the decision state is expected to be characterized by smaller numbers of unique destinations and flight dates, closer (more similar) destinations and flight dates, and a stronger likelihood for convergence (rather than divergence) dynamics. A further decrease in diversity values is expected with the transition to the purchase state, in which, according to the literature, the customer conducts final decisions regarding the purchase (for example, a consumer searching for a smartphone might have selected a particular model and now decides on its color, shipping and payment methods). It is important to note that, despite the use of the label “purchase” to refer to this state, the literature does not assume that a purchase must occur in this state. Rather, it is a cognitive stage, in which the consumer has decided on a particular product or on a narrow set of versions of the product.

Table 3 shows an example of how these expected patterns might manifest in a particular user’s searches at different stages (states) of the funnel. In this example, in the research state, the consumer searches for three different cities at very different dates; in the decision state, the consumer seems to have chosen a destination and is now searching for different dates in October; and in the purchase state, the consumer is trying to make the final choice regarding the return date.<sup>3</sup>

Another (observed) characteristic that we measure for each visit is the visit outcome: that is, whether, following the visit, the consumer churned, made a reservation, or made another visit within the next 10 days. Any of the stages may lead to any of the three outcomes; for example, though we expect it to be more likely that a reservation would occur during the purchase state, a consumer may churn even if they are estimated to be in the purchase state. Information on visit outcome is left out of the HMM to enable us to use the HMM in a prediction mode, where search diversity is gradually revealed, yet its outcome (e.g., reservation or churn) is unknown.

## Model Formulation

We assume that each funnel f is a sequence of T<sub>f</sub> visits $( T _ { f } \geq 3 )$ conducted by a consumer, which ends either with a reservation or with churn. Funnel f is associated with two sequences: (1) a sequence of hidden states $S ( f ) .$ where each state corresponds to a single visit $t ~ \left( t ~ = ~ 1 , ~ \ldots ~ T _ { f } \right)$ in the funnel; $S ( f ) =$ $S _ { f 1 } , S _ { f 2 } , \dots , S _ { f _ { T _ { f } } }$ , where $S _ { f l }$ is the initial state for funnel f and $S _ { f t }$ ∈ {awareness, research, decision, purchase}; and (2) an observed signal sequence $O ( f ) = O _ { f 1 } , O _ { f 2 } , \dots , O _ { f T _ { f } }$ , where $O _ { \hbar }$ represents a multi-variate observed signal ${ \dot { O } } _ { \hbar } ^ { 1 ^ { \prime } } , . . , O _ { \hbar } ^ { \mathrm { { m } } }$ of count-based, network-based, and dynamics-based measures, that were recorded during visit $t ,$ as detailed in Table 4 below.

![](/api/attachments/XHYVAPFY/fulltext/images/f417a91056cc8a6067a395db23d4d3f2549861ff5d698e3c0e723da844b1fb19.jpg)

Figure 2. States of the HMM, Corresponding to the Latent Stages of the Funnel

<table><tr><td colspan="2">Table 3. Example of Search Behavior in Each State of the Funnel</td></tr><tr><td></td><td>Search query</td></tr><tr><td>Awareness state</td><td>Paris, Depart: Oct. 10 – Return: Oct. 15, Paris, Depart: Oct. 20 – Return: Oct. 25,</td></tr><tr><td>Research state</td><td>Paris, Depart: Oct. 10 – Return: Oct. 15, Rome, Depart: Oct. 10 – Return: Oct. 20, Paris, Depart: Nov. 05 – Return: Nov. 10, London, Oct. 3 – Return: Oct. 10</td></tr><tr><td>Decision state</td><td>Rome, Depart: Oct. 10 – Return: Oct. 15, Rome, Depart: Oct. 10 – Return: Oct. 17, Rome, Depart: Oct. 12 – Return: Oct. 17, Rome, Depart: Oct. 11 – Return: Oct. 15</td></tr><tr><td>Purchase state</td><td>Rome, Depart: Oct. 12 – Return: Oct. 17, Rome, Oct. 12 – Return: Oct. 18</td></tr></table>

<table><tr><td colspan="3">Table 4. Definition of State-Dependent Distributions of Observed Variables</td></tr><tr><td>Notation</td><td>Description of state-dependent observed diversity</td><td>Distribution family</td></tr><tr><td> $P(count1_{ft} = cd1 \mid S_{ft} = j)$ </td><td>Probability that the level of count1 (the first principal component of the count-based diversity measures) measured during visit t of funnel f was cd1, given that the consumer of funnel f is in state j, where cd1 ∈{low, medium, high}</td><td>Multinomial</td></tr><tr><td> $P(count2_{ft} = cd2 \mid S_{ft} = j)$ </td><td>Probability that the level of count2 (the second principal component of the count-based diversity measures) measured during visit t of funnel f was cd2, given that the consumer of funnel f is in state j, where cd2 ∈{low, medium, high}</td><td>Multinomial</td></tr><tr><td> $P(network1_{ft} = nd1 \mid S_{ft} = j)$ </td><td>Probability that the level of network1 (the first principal component of the network-based diversity measures) measured during visit t of funnel f was nd1, given that the consumer of funnel f is in state j, where nd1 ∈{low, medium, high}</td><td>Multinomial</td></tr><tr><td> $P(network2_{ft} = nd2 \mid S_{ft} = j)$ </td><td>Probability that the level of network2 (the first principal component of the network-based diversity measures) measuredduring visit t of funnel f was nd2, given that the consumer of funnel f is in state j, where nd2 ∈{low, medium, high}</td><td>Multinomial</td></tr><tr><td>P(dynamic1ft = dd1 | Sft = j)</td><td>Probability that the level of dynamic1 (the first principal component of the dynamics-based diversity measures) measured during visit t of funnel f was dd1, given that the consumer of funnel f is in state j, where dd1 ∈{converge, diverge}</td><td>Multinomial</td></tr><tr><td>P(dynamic2ft = dd2 | Sft = j)</td><td>Probability that the level of dynamic2 (the first principal component of the dynamics-based diversity measures) measured during visit t of funnel f was dd2, given that the consumer of funnel f is in state j, where dd2 ∈{converge, diverge}</td><td>Multinomial</td></tr></table>

The HMM is defined by a set of three parameters: $\lambda = ( \pi , A ,$ $B ) ,$ where π is the initial state distribution, A is the state transition probability distribution, and B is the observed signal-vector probability distribution (Visser & Speekenbrink, 2010).

In the HMM, the joint likelihood of the observed variates $O ( f )$ and latent states $S ( f )$ (assuming they are known), given a set of model parameters $\lambda ,$ can be written as (Visser & Speekenbrink, 2010):

$$
P (O (f), S (f) | \lambda) = \pi_ {S _ {f 1}} b _ {S _ {f 1}} \bigl (O _ {f 1} \bigr) \prod_ {t = 1} ^ {T - 1} a _ {S _ {f t} S _ {f t _ {+ 1}}} b _ {S _ {f t}} \bigl (O _ {f t + 1} \bigr),\tag{1}
$$

where

$1 . \pi _ { S _ { f 1 } }$ is the initial state probability, that is, the initial probability of being at state $S _ { f 1 }$ ;

$2 . b _ { S _ { f 1 } } ( O _ { f 1 } )$ is the state-dependent distribution of the first response $O _ { f 1 }$ ;

3. $a _ { i j } ( t ) = P ( S _ { t + I } { = } j | S _ { t } { = } i )$ is the probability of a transition from state i to state j. $a _ { i j } ( t )$ is an element of the transition matrix $\operatorname { A } ;$ 4. $b _ { S j } ( O _ { t } )$ is a vector of observation distributions $b _ { j } ^ { k } ( O _ { t } ) =$ $P ( O _ { t } ^ { k } | S _ { t } = j )$ , defining the conditional distribution of observations $O _ { t } ^ { k }$ associated with latent state $j , j = I , . . . , n ,$ and observed variable k, $k = I , . . . , m . \ b _ { i } ^ { k } ( O _ { t } )$ is an element of the observed response probability vector B.

The above Equation (1) presents the probability of a given observation sequence O(f) and a given state-sequence $S ( f )$ . To calculate the likelihood of all possible state-sequences, we sum the above equation over all possible state-sequences:

$$
\begin{array}{l} {L (O (f)) = P (O (f) | \lambda)} \\ {= \sum_ {a l l S (i)} \pi_ {S _ {f 1}} b _ {S _ {f 1}} (O _ {f 1}) \prod_ {t = 1} ^ {T - 1} a _ {S _ {f t} S _ {f t + 1}} b _ {S _ {f t}} (O _ {f t + 1})} \end{array}\tag{2}
$$

To find the maximum-likelihood estimates of the model parameters, we use the expectation-maximization (EM) algorithm<sup>4</sup>. In the EM algorithm, the HMM parameters are estimated by iteratively maximizing the expected loglikelihood of the parameters, given the observations (Visser, 2011).

Modeling State Transitions: The transition probability matrix A, in which each element $a _ { i j } ~ = ~ P ( S _ { t + I } { = } j | ~ S _ { t } { = } i )$ represents the probability to transition from state i to state j, is modeled as a baseline-category multinomial logistic model. Our model includes two covariates as transition predictors: deltaPrice and timeToFlight. The first covariate, deltaPrice, measures the difference between the average price of the flights searched for in the current visit and the average flight price of the previous visit. A negative value indicates a price decrease, which is expected to (positively) affect the consumer’s probability to transition to the next stage of the funnel. The second covariate, timeToFlight, is the duration of time between the visit start date and the first searched departure date (in hours). We expect lower values of timeto-flight to be associated with a higher likelihood of progressing to the next stage of the funnel.

Modeling Funnel Stages: Each state is characterized by the different measures of diversity: count-based, network-based, and dynamics-based. As detailed above, each class of diversity measures includes three elements: city, country, and flight date and, in some cases, a particular element corresponds to multiple related diversity measures (for example, we measured the average city distances and the total distance between unique cities). We observed high correlations between some of the elements. Accordingly, for each class of diversity measures, we used principal component analysis (PCA) to transform the element space into a new, orthogonal space (see, for example, Aggarwal et al., 2020; Argunsah & Cetin, 2010; Calinon & Billard, 2005). Notably, in doing so, we gained another benefit: PCA enabled us to obtain unified measures of diversity across the different elements (city, country, flight date). A detailed explanation of the PCA process is presented in Appendix B.

In each class of diversity measures, the first two principal components were found to capture most (over 70%) of the elements’ variance (see Tables B1-B3, Appendix B). We thus used those components as the observed signals in our four-state HMM. In what follows, we refer to the first two principal components of the count-based measures as count1 and count2, the network-based measures as network1 and network2, and the dynamics-based measures as dynamic1 and dynamic2.

While HMM handles common continuous distributions such as the Gaussian and gamma distributions, it does not handle (very) long-tailed distributions, such as those of city distance, flight-date distance and the corresponding PCA components. We thus decided to bin these variables into bins of equal sizes, and to use a multinomial distribution. The count-based and network-based variables were divided into three bins: high, medium, and low; and the dynamics-based variables were divided into two bins: diverge (increasing diversity) and converge (decreasing diversity).

To support the robustness of our binning approach, we reran our analyses using different binning cutoffs; the results were consistent with the main results presented below (for the sake of space, these results are not included in the paper but are available upon request).<sup>5</sup>

The state-based probability distributions, B, of our vector $O _ { \hat { \pi } }$ of observed variables = {count1<sub>ft</sub>, count2<sub>ft</sub>, network ${ \mathit { I } } _ { f t } ,$ network2<sub>ft</sub>, dynamic $\cdot I _ { f t } ,$ dynamic2<sub>ft</sub>,}, are formally described in Table 4. For example, for a given consumer with funnel f who is in visit t and is in state $j ,$ count1 is the distribution of the probability that the level of count1 (the first principal component derived from the count-based diversity measures) is low/medium/high.

The state-dependent probabilities of the multinomial response variables are modeled as follows:

$$
P (O _ {i t} ^ {k} | S _ {t} = j) = \frac {\mathrm{e} ^ {\beta_ {j} o _ {i} ^ {k}}}{1 + \sum_ {j} \mathrm{e} ^ {\beta_ {j} o _ {i} ^ {k}}}\tag{3}
$$

where $O ^ { k }$ is the $k ^ { \mathrm { { t h } } }$ variable of the m-variate observation vector $O , k { = } I , { \ldots } , m .$ , and $o ^ { k } { } _ { \mathit { f t } }$ is the observed value of $O ^ { k }$ at visit t in funne $\mid f .$

We use the proposed HMM to investigate whether our searched-product diversity measures are able to characterize the different stages of the funnel as described above. Specifically, we analyzed the different mean values of our diversity measures associated with each of the identified funnel stages.

## Using Diversity to Predict the Consumer’s Conversion

After showing the association between within-visit searchedproduct diversity and progress in the funnel, as well as the likelihood of purchase, we turn to RQ2 and demonstrate the managerial and business implications of our diversity measures. We investigate the capacity of the different diversity measures to contribute to predictions of consumers’ visit outcomes, using the fitted HMM. We note that we focus on the HMM (and the associated PCA-based diversity measures) to maintain consistency with our methodological approach to RQ1. Yet, for practical prediction purposes, it may be more straightforward to apply other types of prediction models, using the raw diversity measures (see the discussion of alternative models in the Robustness Checks section and in Appendix D).

## Target Variable

Given data from a single visit, we are interested in predicting the outcome of the visit and, specifically, whether searches of a given visit led to a reservation at the end of the visit or not (where a “no reservation” visit outcome refers to either churn or a subsequent visit).

Yet to be able to use the HMM to make such a prediction, it is first necessary to define how the information captured in the model is mapped to the prediction outcome. As mentioned above, our HMM captures four hidden states, representing four possible cognitive stages of the consumer: awareness, research, decision, and purchase. Theory suggests that conversion is most likely to occur in the purchase state. Indeed, as elaborated in the Results section, our analysis of the HMM reveals that users in the purchase state are most likely to book flight reservations than users in the other states. Thus, we define the prediction outcome (probability of conversion) as the probability of being in the purchase state.

As discussed below, we evaluate our predictions using the actual purchase behavior. For example, if a consumer in our test set is predicted by the HMM to be in the “purchase state” with the highest probability, we predict that this consumer will purchase. We then test our model using the actual purchase behavior, and if this consumer in fact purchased, the prediction is marked as “correct.”

## Baseline Variables

Before studying the predictive power of the proposed diversity measures, we need to construct a baseline model and define its attributes, based on established practice and existing literature.

Specifically, our baseline model includes all attributes presented in Table 1 as well as the categorical attributes that follow Table 1, namely: visit duration, number of searches, time to flight, median search duration, average searched travel duration, previous visits, searches in previous visit, number of previous reservations, start time, day of week, time of day, flight season, and average flight price.

To the baseline set of attributes of each visit, we also added network-related parameters derived from the destination networks (of cities and of countries): we calculated the average closeness, page-rank, transitivity and betweenness centrality of the cities searched during the visit. These measures represent the importance of destinations that are searched for during the visit and may also be indicative of the likelihood of conversion. They also ensure that the product-network-based diversity measures capture search diversity alone and are not confounded by factors related to specific destinations’ importance in the product network.

## Conversion Prediction Models

To predict the chances that a visit will lead to a reservation, we use three models: First, we used the HMM described in the previous section, which includes the count-based, networkbased, and dynamics-based diversity attributes (i.e., the diversity-based model). Second, to create a baseline model, we fitted an independent HMM, based on a set of baseline attributes (as defined in the previous subsection) that does not account for search diversity at all (i.e., the baseline model). Third, to observe the contribution of the network-related diversity attributes (i.e., network-based and dynamics-based) to the prediction performance, we also fitted an HMM that includes only the count-based measures (i.e., the count-based model).

To train and evaluate our models, we constructed training sets and test sets of visits corresponding to funnels that included at least three visits. As our dataset included time series of visits, we needed to control for possible data leakage, that is, to avoid the possibility that a model might be trained on data from later visits and then evaluated on earlier visits. To this end, we split the data such that the training set is composed of visits corresponding to funnels starting before the end of November 2015 (80% of the visits), and the test set is composed of visits corresponding to funnels starting at or after the end of November 2015 (20% of the visits).

We repeated our analysis for visits comprising at least n searches, for different values of n (n = 3, 4, 5, 6, 7). For each n, we train and evaluate the models only on data collected during the first n searches of each visit. For example, the variable number of unique searched cities was calculated based on the first n searches, that is, the number of unique cities searched for during the first n searches. This approach highlights the managerial value of our models: a manager can act in accordance with the expected result of a user’s visit (reserve versus churn/proceed) already after the n<sup>th</sup> search. Table 5 presents the dataset sizes of visits having at least n searches in funnels with at least three visits.

## Robustness Checks

Additional classification algorithms: To further establish the predictive value of our diversity measures, we also applied more traditional conversion classification algorithms, namely, XGBoost<sup>6</sup> and random forest.

In contrast to our HMM-based prediction models, which can be trained only on funnels that include at least three visits (to be able to capture state-transitioning, as explained above), XGBoost and random forest impose no constraints on the length of the funnel. Accordingly, in these analyses, we included visits of shorter funnels, leading to a larger dataset of 91,616 visits instead of 37,854 visits. Moreover, as in our HMM analysis, we repeated our XGBoost and random forest analyses using different numbers of observations. These analyses and their results are presented in Appendix D1. In these models—unlike in the HMM, which was explicitly designed to capture users’ stages in the funnel—we directly predicted purchase behavior and did not go through the intermediate step of predicting the user’s probability of being in the purchase stage of the funnel.

Dataset size: For robustness, to verify that adding additional observations (visits) to the dataset does not improve model performance, we analyzed the models’ performance when trained with growing numbers of funnels. In particular, we used 10%, 20%, 30%, …, 80%, and 90% of the funnels. We repeated this robustness analysis for the XGBoost and random forest models as well.

<table><tr><td colspan="2">Table 5. Number of Visits in the Dataset with at Least N Searches in Funnels with at Least 3 Visits</td></tr><tr><td>N</td><td>Dataset size</td></tr><tr><td>3</td><td>105,167</td></tr><tr><td>4</td><td>60,346</td></tr><tr><td>5</td><td>37,854</td></tr><tr><td>6</td><td>25,101</td></tr><tr><td>7</td><td>17,351</td></tr></table>

![](/api/attachments/XHYVAPFY/fulltext/images/eb9f06cb641b86c23092aff442faf61da7e1c9ba126db46df9ce89acada1b869.jpg)

![](/api/attachments/XHYVAPFY/fulltext/images/f12fe1b1296f8a0db3641cf98940b4f503bfe886c57cd72d782d4fbbac5b1a19.jpg)

![](/api/attachments/XHYVAPFY/fulltext/images/c6eaeea10ffd5937a49eedeff3d9c1c8f32ad87baecdbcceaa673c30d32543e7.jpg)

![](/api/attachments/XHYVAPFY/fulltext/images/6ebabbaf9878d0fb9083d3bd3818c4d5d099bb0bd3b8db104c2b34e37a603fb3.jpg)

![](/api/attachments/XHYVAPFY/fulltext/images/978215dab83828f2ed108c4f10ddf862ded68165dfc7bd7c04ef43012f369d64.jpg)

![](/api/attachments/XHYVAPFY/fulltext/images/446843ff4fb287bef6f45b7274261b77ecaa7f56fb5d4759cde1b87ee9171116.jpg)  
Note: (A-C) Count-based measures (number of unique cities $( \mathsf { A } ) ;$ countries (B); and flight dates (C) searched). (D-F) Network-based measures— average city (D), country (E), flight date (F) distances. All values were normalized to a 0-1 scale.

Figure 3. Diversity Values Along the Funnel’s Visits, for Funnels With 3, 4, 5, and 6 Visits

## Results

## Model-Free Analysis

The Relationship between Search Diversity and Progress in the Funnel (RQ1a)

Figure 3 depicts the values of the count-based and networkbased diversity measures in funnels with different numbers of visits (this presentation is less appropriate for the dynamicsbased measures, which are focused on within-visit rather than cross-visit behavior). Each diagram in Figure 3 shows, for a given diversity measure, the values corresponding to each visit in the funnel. Each diagram includes four lines—each one for funnels with a specific number of visits, namely three, four, five, and six visits.

As can be observed, for each search-diversity measure, the average value of the measure decreases as the visit number increases. If we assume that consumers (on average) are likely to progress through the funnel with each search visit (as explored in what follows), this observation suggests that search diversity decreases with the consumer’s progress in the funnel, not only from the perspective of the choice-set size (number of different destinations and dates) but also from the perspective of network distance among searched products.

## Diversity Values of Visits with and without Reservations (RQ1b)

We first compared the diversity values of visits that ended with a reservation (hereafter referred to as “buyers’ visits”) to the diversity values of visits that ended without a reservation (hereafter referred to as “nonbuyers’ visits”). The comparison was done while controlling for the number of searches performed during the visit because, naturally, consumers who perform more searches have the potential to exhibit higher diversity. Figure 4 presents the results of this comparison for the count- and network-based diversity measures.

These results suggest that buyers’ visits consistently exhibit a lower level of diversity than nonbuyers’ visits. Since the diversity measures were not normally distributed, we applied the Mann-Whitney U test (Mann & Whitney, 1947) to statistically compare the various measures across the different groups of visits. For the count-based attributes, whose values were exponentially distributed, we also performed t-test analysis on the logs of the values (which were normally distributed). The results show that the means of all measures differed significantly between buyers’ visits and nonbuyers’ visits.

Figure 5 presents the results of the comparison for the three dynamics-based measures (using a bar chart representation to accommodate both positive and negative values). This figure shows that buyers’ visits (in orange) tend to converge in terms of diversity, exhibiting negative values of the dynamics indices, whereas nonbuyers’ visits (in blue) tend to exhibit positive values (suggesting that these sessions diverge in terms of diversity of the consideration set) or less negative values (i.e., they converge more slowly) compared with buyers’ visits. Again, the differences are significant (according to the Mann-Whitney U test).

Put together, these results suggest that, on average, when the number of searches per visit is controlled for, buyers’ visits are characterized by lower search diversity values (compared with nonbuyers’ visits) for our proposed diversity measures.

## Linking Diversity to Conversion Rates (RQ1b)

In this section, we examine how the conversion rate (in the yaxis) in a given set of visits—i.e., the percentage of visits that ended in a reservation—behaves as a function of search diversity (x-axis) in those visits, for each of our diversity measures.

Count-Based diversity measures: Figure 6 shows the relationship between the number of unique cities (countries/flight dates) searched for in a single visit and the conversion rate (again controlling for the number of searches per visit). As can be observed, visits with higher diversity are associated with lower conversion rates.

Network-based diversity measures: Because the networkbased measures are continuous variables, for each diversity measure, we binned the visits into two quantiles of high and low values for that measure. We also grouped the dataset by the number of unique cities (or by country or flight date), which enabled us to control for the number of cities (or countries/flight dates) and focus on the level of similarity (i.e., diversity) among them. The results of this comparison are presented in Figure 7.

As shown in Figure 7, when we control for the number of unique cities (or countries/flight dates), visits manifesting high diversity values exhibit lower conversion rates compared with visits manifesting low diversity values. In each panel, all differences between high-diversity visits and low-diversity visits (corresponding to the same number of searches) are statistically significant (p < 0.01) except for two cases: visits with two cities (blue bars in Figure 7a) and visits with two countries (blue bars in Figure 7b).

Dynamics-based diversity measures: Next, we analyzed how conversion rate is associated with the mean difference in city (or country/flight date) distances during the visit. First, to control for the number of searches performed, we grouped visits by the number of searches. Then, within each group (that is, for each number of searches), we binned visits according to positive versus negative values of each diversity-based dynamics measure. Note that a positive value of Mean difference in city (or country/flight date) distance means that distances between searched products increased over the course of the visit (indicating divergence), whereas a negative value means that distances decreased (indicating convergence). We then measured the conversion rate of each bin. The results are presented in Figure 8. As shown in the figure, visits with negative values of mean distance differences among searches exhibited significantly higher conversion rates, as compared with visits with positive values of mean distance differences.

Survival analysis: To establish the statistical significance of the correlations between our search-diversity measures and the likelihood that a given funnel will end with a reservation (RQ1b), we used survival (hazard) analysis (where the reservation is the “hazard”) as well as competing risk analysis. The results of these analyses, reported in Appendix A, strengthen the above model-free findings on the negative relationship between diversity measures and conversion rate.

Figure 4. Means of the Count-based and Network-based Diversity Measures for Visits with/without Reservations, for Visits of Different Lengths (# of searches)

Note: (A-C) Count-based diversity measures (# unique cities (A), countries (B), and flight dates (C) searched). (D-F) Network-based diversity measures (total unique network distance)—cities (D), countries (E), flight dates (F). In each diagram, the x-axis depicts the number of searches included in a visit, and the Y-axis depicts the average diversity for visits with the corresponding number of searches. The blue line represents buyers’ visits; the orange line represents nonbuyers’ visits.  
![](/api/attachments/XHYVAPFY/fulltext/images/903cb5c040603103b22b7396bb3e01470c415b2347ee3840aceb526e82129d79.jpg)  
A

![](/api/attachments/XHYVAPFY/fulltext/images/d42c4688ea10af165b4fd75116ab1a5b8005fe92297f42d6e3f37833ac6372c7.jpg)  
B

![](/api/attachments/XHYVAPFY/fulltext/images/897d04fb037cb5a37e96c27eaabc6b78ea5b3545f3deda088969989f8fa21709.jpg)  
C

![](/api/attachments/XHYVAPFY/fulltext/images/b0ecf06a166328da5766b281a1dd24d014277bea58455b76b57825e453fdf44e.jpg)  
D

![](/api/attachments/XHYVAPFY/fulltext/images/03d6bcde996aa2bad754b55d5c0c6d659e11703b6791f632324de1048c48a01d.jpg)  
E

![](/api/attachments/XHYVAPFY/fulltext/images/5f0040d85b67f4c82fa036329fdbbb3fb539a45891d8fbf81c55f2bec417801c.jpg)  
F

## with reservation

no reservation  
![](/api/attachments/XHYVAPFY/fulltext/images/8f273cc3317d217e98d63991fd99466bda65fca4df7f0f3cbf0ec7b61085eede.jpg)

![](/api/attachments/XHYVAPFY/fulltext/images/22b422904c0c99f4b7596cbc62537d5fe3196637582b0291713bc3d72db33972.jpg)

![](/api/attachments/XHYVAPFY/fulltext/images/223fa4427c8e60d7437316a1f9b21cf3964a5e6d51f07eccd9afc6811aedabe8.jpg)  
no reservation  
Note: Mean (scaled by dividing in the maximum absolute value) distance differences for cities (A), countries (B), flight dates (C).

Figure 5. Means of the Dynamics-Based Diversity Attributes of Visits with/without Reservations, for Visits of Different Lengths (# of searches)

![](/api/attachments/XHYVAPFY/fulltext/images/cfed096367b19b220b8ee77ba4c1239b7efef1f0d679f666148c8c316fe5e92e.jpg)  
A

![](/api/attachments/XHYVAPFY/fulltext/images/d41e0c99e8c99d048f5b02dd510971e5c0a6f8fa55b6428f535d4ae7462af6dc.jpg)  
No. of unique countries  
B

![](/api/attachments/XHYVAPFY/fulltext/images/acac4af408807b8a13c70292def2f5fd0560dea3342781a5c120ae425bbac786.jpg)  
C  
Note: (A) number of unique cities, (B) number of unique countries, (C) number of unique flight dates. each line depicts the results for visits with a certain number of searches.

Figure 6. Conversion Rate (percentage of visits that ended in a reservation) as a Function of Count-Based Diversity Measures

![](/api/attachments/XHYVAPFY/fulltext/images/93e09fe9a8692b79fd96cd7a0d1afb7b62d2504ce098fe7e6b670f96a44863d4.jpg)  
A

![](/api/attachments/XHYVAPFY/fulltext/images/7aba6802f59143e0ae0b495e8f5c8c1f116238ab91594ef72193493d0be2b3d7.jpg)  
B

![](/api/attachments/XHYVAPFY/fulltext/images/712ed06a61e789ac53473798e11fa66275e73051b839a44ea068e0e680c5ec20.jpg)  
C  
Note: (A) city diversity levels (measure: Total unique cities distance); (B) country diversity levels (measure: Total unique countries distance); (C) flight date diversity levels (measure: Total unique date distance from first). Results are depicted for visits with different numbers of unique searched cities/countries/dates. For each diagram, the y-axis represents the conversation rate, and the x-axis represents the two diversity levels (low or high) for each number of unique cities (/countries /flight dates). Note that each color represents a different number of unique cities (/countries /flight-dates).

Figure 7. Conversion Rate (percentage of visits that ended in a reservation) as a Function of Network-Based Diversity Measures

![](/api/attachments/XHYVAPFY/fulltext/images/bed9462e00f115831b1f6ec12b7a599242f3cc76761028e2602cc236f2a9b8a7.jpg)  
A

![](/api/attachments/XHYVAPFY/fulltext/images/c2e4509158fb48dd27c58ce3de369fad3e8bcc7a30afa1def952010b77f8a094.jpg)  
B

![](/api/attachments/XHYVAPFY/fulltext/images/0aea37553dd6e4f66e0dcd820c1aa65f0fa44f44b3dfe04f54e7735d9973c906.jpg)  
C

\# searches per visit 34 56

Note: The y-axis represents the conversion rate; the x-axis represents distance differences bins (high (+) and low (-) differences for each number of searches). Different colors correspond to different numbers of searches per visit (3, 4, 5 or 6).

Figure 8. Conversion rate (percentage of visits that ended in a reservation) as a Function of Dynamics-Based Diversity Measures—i.e., Mean Difference in City (A), Country (B) Flight Date (C) Distances over the Visit

Table 6. State-Dependent Distributions of Observation Variables: Mean (standard error)

<table><tr><td>StateVariable</td><td></td><td>Awareness (S1)#visits = 11,447(23.4)</td><td>Research (S2)#visits = 63,027 (27)</td><td>Decision (S3)#visits = 31,360 (1.5)</td><td>Purchase (S4)#visits=20,496(4.7)</td></tr><tr><td rowspan="3">Count1</td><td>High</td><td>0.003 (1.7E-19)</td><td>0.675 (4E-17)</td><td>0.030 (0.0E+00)</td><td>0.000 (0.0E+00)</td></tr><tr><td>Medium</td><td>0.176 (1.1E-17)</td><td>0.325 (0E+00)</td><td>0.298 (0.0E+00)</td><td>0.015 (0.0E+00)</td></tr><tr><td>Low</td><td>0.820 (1.8E-04)</td><td>0.000 (0E+00)</td><td>0.672 (0.0E+00)</td><td>0.985 (0.0E+00)</td></tr><tr><td rowspan="3">Count2</td><td>High</td><td>0.131 (0.0E+00)</td><td>0.438 (0E+00)</td><td>0.293 (1.8E-04)</td><td>0.000 (0.0E+00)</td></tr><tr><td>Medium</td><td>0.454 (1.8E-04)</td><td>0.262 (0E+00)</td><td>0.707 (1.8E-04)</td><td>0.016 (1.8E-04)</td></tr><tr><td>Low</td><td>0.416 (1.8E-04)</td><td>0.300 (0E+00)</td><td>0.000 (0.0E+00)</td><td>0.984 (1.8E-04)</td></tr><tr><td rowspan="3">Network1</td><td>High</td><td>0.028 (0.0E+00)</td><td>0.372 (2E-17)</td><td>0.030 (0.0E+00)</td><td>0.000 (0.0E+00)</td></tr><tr><td>Medium</td><td>0.214 (0.0E+00)</td><td>0.621 (0E+00)</td><td>0.346 (1.8E-04)</td><td>0.000 (0.0E+00)</td></tr><tr><td>Low</td><td>0.758 (0.0E+00)</td><td>0.007 (0E+00)</td><td>0.625 (0.0E+00)</td><td>1.000 (0.0E+00)</td></tr><tr><td rowspan="3">Network2</td><td>High</td><td>0.107 (0.0E+00)</td><td>0.273 (0E+00)</td><td>0.159 (0.0E+00)</td><td>0.000 (0.0E+00)</td></tr><tr><td>Medium</td><td>0.462 (0.0E+00)</td><td>0.324 (0E+00)</td><td>0.841 (4.3E-17)</td><td>0.000 (0.0E+00)</td></tr><tr><td>Low</td><td>0.431 (1.8E-04)</td><td>0.403 (0E+00)</td><td>0.000 (0.0E+00)</td><td>1.000 (0.0E+00)</td></tr><tr><td rowspan="2">Dynamic1</td><td>Diverge</td><td>0.970 (4.3E-17)</td><td>0.658 (0E+00)</td><td>0.955 (0.0E+00)</td><td>1.000 (0.0E+00)</td></tr><tr><td>Converge</td><td>0.030 (0.0E+00)</td><td>0.342 (0E+00)</td><td>0.045 (2.7E-18)</td><td>0.000 (0.0E+00)</td></tr><tr><td rowspan="2">Dynamic2</td><td>Diverge</td><td>0.086 (5.4E-18)</td><td>0.349 (0E+00)</td><td>0.165 (0.0E+00)</td><td>0.000 (0.0E+00)</td></tr><tr><td>Converge</td><td>0.914 (0.0E+00)</td><td>0.651 (0E+00)</td><td>0.835 (0.0E+00)</td><td>1.000 (0.0E+00)</td></tr><tr><td rowspan="3">Visit outcome</td><td>Churn</td><td>0.000 (5.6E-08)</td><td>0.110 (2E-05)</td><td>0.145 (4.4E-06)</td><td>0.157 (1.1E-05)</td></tr><tr><td>Proceed</td><td>1.000 (1.6E-05)</td><td>0.876 (1E-05)</td><td>0.827 (2.7E-06)</td><td>0.778 (1.1E-05)</td></tr><tr><td>Reserve</td><td>0.000 (1.6E-05)</td><td>0.015 (7E-06)</td><td>0.029 (6.2E-06)</td><td>0.066 (2.2E-05)</td></tr></table>

Note: #visits = 126,330.

## Model-Free Analysis: Summary of Findings

The results of our model-free analysis thus far show that more advanced visits are associated with lower diversity measures, that visits that end in a purchase exhibit consistently lower diversity measures, and that lower diversity measures in a single visit are associated with a higher likelihood of conversion at the end of that visit. These results are consistent across all three types of diversity measures and provide preliminary empirical evidence regarding our initial research questions (RQ1a-b).

## Hidden Markov Model (RQ1a-b)

## The Relationships between Search Diversity, Funnel Stage, and Visit Outcome

We used a four-state HMM to study the relationships between different patterns of search diversity (described using our count-based, networked-based, and dynamicsbased measures; see the Modeling Funnel Stages section for the definitions of these measures for the purpose of HMM modeling) and the funnel stages, as well as the outcome of the visit (reservation, churn, another visit). To avoid local maxima and to calculate the statistical significance of the model, we fitted the HMM 10 times, using different seed numbers to initialize the model. The subset of the data used for this model is the set of multivisit funnels that contained price information. For robustness, we also fitted the HMM models to the entire set of multivisit funnels (that is, we included visits without price information, and thus the HMM did not include the deltaPrice transition variable) and reached similar results.

Table 6 describes the mean values and standard errors of the observed variables at each state of the HMM, computed based on the 10 repetitions. Comparing the mean diversity values of the different states, we found that the second state (S2) has the highest diversity values (highest count-based, network-based, and dynamics-based), corresponding to our expectations of the research stage. The fourth state (S4) is characterized by the lowest diversity levels, corresponding to our expectations of the purchase state.

Looking at the values of the visit outcome variable (churn/proceed/reserve), we can see that the likelihood of reservation increases as the consumer progresses between states. Specifically, the first state is characterized by the lowest likelihood of reservation, whereas the fourth state is characterized by the highest likelihood of reservation (7%), indicating that is indeed appropriate to classify the fourth state as the purchase stage.

To provide a more intuitive understanding of these results, Figures 9-11 depict the state-based distributions of the values of different (raw) diversity measures (count-based, network-based, and dynamics-based, respectively) and characterize the diversity patterns associated with each identified funnel stage. In Figure 9, for example, focusing on the number of unique cities (Panel A), we see that in almost all visits in the decision state or in the purchase state, the user searched for only one city, whereas all visits corresponding to the research state included multiple searched cities. Similarly, in Panel A of Figure 10, which depicts the state-based distributions of the city distance diversity levels,<sup>7</sup> we can see that almost all visits corresponding to the awareness, decision, or purchase states were characterized by low city distance levels, whereas in the research state, most visits (about 70%) were characterized by high city distance levels. Figure 11 reveals similar patterns, showing that the highest divergence rates are found in the research state (27% for city- and 30% for flight-date-based divergence). In the decision and purchase states, there is no city-related divergence at all, and the rates of flight-date-related divergence are substantially lower than those of the research state (12% and 21% respectively).

We found that about 48% of the funnels start in the awareness state and 52% of the funnels start in the research state. Our findings further reveal that consumers do not all progress through the funnel in a sequential manner (awareness → research → decision → purchase). Table 7 shows the transition matrix of our model at zero values of the covariates, conditional on having a subsequent visit (recall that in our model, a consumer can churn or make a reservation from any state). For example, for a visit in the awareness (S1) stage, the likelihood that the next visit will be in the same state is 0.1%, the likelihood that it will be in S2 (research) is 37.8%, the likelihood that it will be in S3 (decision) is 34.7%, and the likelihood that it will be in S3 (purchase) is 27.4%. These findings are in line with prior observations that one can move back and forth between stages of the funnel (Ghose et al., 2017; Netzer et al., 2008; Todri et al., 2019). Interestingly, the probability of returning to S1 (awareness) from all states is close to zero.

## The Role of Price and Time-to-Flight in the Transition between States

Figure 12 shows how the probability of transitioning from the awareness state changes as the value of deltaPrice changes. It shows that as the value of this variable becomes more negative—corresponding to higher price decreases—the probability of transitioning to the purchase state increases, whereas as the value becomes more positive (indicating price increases), the probability of transitioning to the research state increases. Interestingly, when the consumer resides in the research, decision and purchase states, deltaPrice has little effect (close to zero) on transition probability.

Figures 13-15 show how changes in the value of timeToFlight (normalized) affect the probability to transition from the awareness, decision, and purchase states respectively. These figures indicate that an increase in the timeToFlight is correlated with a slight decrease in the probability to transition to (or stay in) the purchase state, and with a slight increase in the probability to transition to the research state. In the research state, however, changes in timeToFlight are not associated with the transition probability. The full transition models (on which Figures 12-15 are based) are presented in Appendix C.

## Application: Using Diversity to Predict Consumers’ Progression in the Funnel (RQ2)

The above results show a negative relationship between searched-product diversity and progress in the funnel. In particular, when diversity values increase, the likelihood of being in the purchase stage (and hence the likelihood of a reservation) decreases. Based on the results thus far, in this section, we use the proposed diversity measures to predict a consumer’s conversion likelihood.

## Comparison of Prediction Performance of a Diversity-Based HMM versus a Baseline HMM

Table 8 presents the conversion prediction results of HMMs that were trained on the first five searches of a consumer’s visit (using visits having at least five searches), using a bootstrap procedure. Specifically, we trained 10 models; each one was trained on a randomly selected subset of 90% of the trainset and was tested on a randomly selected subset of 90% of the test-set. The table shows mean values and standard errors of different metrics (F1 score, Precision, Recall, AUC).

![](/api/attachments/XHYVAPFY/fulltext/images/c8c9fa837f631f6ec0900c035ccf5d21cc1f3cd3cdc4e3dceaf400a4fde2c2c4.jpg)  
A

![](/api/attachments/XHYVAPFY/fulltext/images/d5e341ec007bd98852bd8c75941be817ef034eafa4447fc100fb1ba8d45637e5.jpg)  
B  
Figure 9. State-Based Distribution of the Number of Unique Cities (A) and the Number of Unique Flight Dates (B)

![](/api/attachments/XHYVAPFY/fulltext/images/b1f8e8efab3be55f8f03ab44f9271f214be2e52ce5f8cee6e4d22b78bf30da8c.jpg)  
A

![](/api/attachments/XHYVAPFY/fulltext/images/6b6f1cd2a5be44545861aa50e2d4d7e10621d03874046dd8939e5d3ff84cfb2e.jpg)  
B  
Figure 10. State-Based Probabilities of the (network-based) City Distance Diversity Levels (A) and Flight-Date Distance Diversity Levels (B) within a Visit

![](/api/attachments/XHYVAPFY/fulltext/images/71191e4bda71779f724b9e5c2fc9cd850f2621c921c5c8bba54b8e24e57cc327.jpg)  
A

![](/api/attachments/XHYVAPFY/fulltext/images/891cd3370055aeee936efac98e1d6dbb46074d306058255900231f5e5fb30c22.jpg)  
B  
Figure 11. State-Based Probabilities of the Mean City (A) and Flight Date (B) Distance Increases (divergence) within a Visit

Table 7. Transition Matrix Describing the Probabilities of Transitioning Between Stages at Zero Values of the Covariates (standard errors)

<table><tr><td>From\To</td><td>S1: Awareness</td><td>S2: Research</td><td>S3: Decision</td><td>S4: Purchase</td></tr><tr><td>S1: Awareness</td><td>0.001</td><td>0.378</td><td>0.347</td><td>0.274</td></tr><tr><td>S2: Research</td><td>0.003</td><td>0.610</td><td>0.239</td><td>0.149</td></tr><tr><td>S3: Decision</td><td>0.001</td><td>0.321</td><td>0.486</td><td>0.193</td></tr><tr><td>S4: Purchase</td><td>0.001</td><td>0.315</td><td>0.264</td><td>0.419</td></tr></table>

![](/api/attachments/XHYVAPFY/fulltext/images/c140e9269a2e61e6b0d57191eeb81fab34fc71e60e4818e983a3511bdea6f26d.jpg)  
Figure 12. Probability to Transition from the Awareness State as a Function of the Average Price Difference (deltaPrice) between the Current and Previous Visits

![](/api/attachments/XHYVAPFY/fulltext/images/c5cd088856e62bb7f68d5bd8f5b9ae0888e5b9651992ab695983c7a90a193077.jpg)  
Note: As the time-to-flight increases, the probability to move to the purchase state decreases, and the probability to move to the research state increases.  
Figure 13. Probability to Transition from the Awareness State as a Function of the Normalized Time-to-Flight (timeToFlight)

![](/api/attachments/XHYVAPFY/fulltext/images/7edfd4083cb4f6cdd81e5a7b9c4da05fd4d6c0879e4b23b144313c2e308011b6.jpg)  
move to the research state increases.

Figure 14. Probability to Transition from The Decision State as A Function of the Normalized Time-To-Flight (timeToFlight)  
![](/api/attachments/XHYVAPFY/fulltext/images/b19b20550f4815f9c1c4a900b26eef142997603404263668904813e5c813ab99.jpg)  
Note: As the time-to-flight increases, the probability to stay at the purchase state decreases, and the probability to move to the research or decision states increases.  
Figure 15. Probability to Transition from The Purchase State as A Function of the Normalized Time-to-Flight (timeToFlight)

Table 8. Conversion-Prediction Performance Metrics (time-series cross-validation averages and standard error) for the Baseline HMM, Count-Based HMM, and the Diversity-Based HMM

<table><tr><td>Measure</td><td>Model 1: Baseline HMM</td><td>Model 2: Count-based HMM</td><td>Model 3: Diversity-based HMM</td></tr><tr><td>F1 score</td><td>0.055 (6.3E-03)</td><td>0.099 (9.5E-04)</td><td>0.124 (2.2E-03)</td></tr><tr><td>Precision</td><td>0.035 (4.4E-03)</td><td>0.061 (6.3E-04)</td><td>0.073 (2.2E-03)</td></tr><tr><td>Recall</td><td>0.136 (1.2E-02)</td><td>0.29 (2.2E-03)</td><td>0.422 (2.3E-02)</td></tr><tr><td>AUC</td><td>0.643 (1.2E-02)</td><td>0.697 (1.3E-03)</td><td>0.72 (4.1E-03)</td></tr></table>

Note: Models were trained on the first 5 searches of a consumer’s visit, using 37,854 visits having at least five searches

![](/api/attachments/XHYVAPFY/fulltext/images/c8e0d4344702595b2aa10acf7a6f9982370f047d2dd2a62c665460fb730a9c6a.jpg)  
Note: We present the standard errors of the time-series based on a bootstrap procedure in parentheses. We present the number of visits used in each analysis in square brackets.

Figure 16. F1-Score Values of HMM Prediction Models that Were Trained on the First 3, 4, 5, 6, and 7 Searches of Each Visit

Model 1 is the baseline model. It includes only the attributes mentioned in Table 1 (and the categorical attributes that follow it) and does not include any diversity measures. Model 2 is the count-based model and includes the count-based diversity measures. Model 3 is the diversity-based model and includes all the different diversity measures (count-based, network-based, and dynamics-based) and allows us to investigate the effect of the contribution of the networkrelated measures to the performance of the models. The models were compared across a series of established classification performance metrics: recall (sensitivity), precision (or positive predictive value), F1-score (the harmonic mean of precision and recall), and AUC (area under the ROC curve). For each metric, we present the mean and standard error of a time-series cross-validation, as detailed in the Methodology section.

As can be observed, the prediction performance of the diversity-based HMM (Model 3) is significantly better than that of the baseline HMM (Model 1) and better than that of the count-based HMM (Model 2). In particular, in the diversitybased HMM, the values of recall, precision, and F1-score are greater than those of the baseline model by factors of 3.1, 2.08, and 2.25, respectively, and also greater than those of the count-based model by factors of 1.45, 1.2, and 1.25, respectively.

We repeated this analysis while training the conversion prediction models on the first three, four, six, and seven searches. Results are in the same direction as the results above and are of similar magnitude. For brevity, we consolidated these results into one figure. Thus, Figure 16 presents the F1- score values of these baseline (blue) and diversity-based (green) models (standard errors in parentheses).

## Robustness Checks

Additional conversion classification algorithms: We further evaluated the predictive value of diversity measures using more traditional classification models: XGBoost and RF (which, unlike the HMM are applicable to funnels with fewer than three visits, as noted in the Additional Classification Algorithms section). The results are presented in Appendix D1. Like our HMM analysis, they reveal that the inclusion of diversity measures substantially improves the performance of a baseline model for conversion prediction. Specifically, recall increases by approximately 7% in the XGBoost models (8% in the RF models), and precision increases by 4% in the XGBoost models (3% in the RF models). It should also be noted that the baseline XGBoost/RF models achieve better results compared with the baseline HMM.

Finally, as elaborated in Appendix D1, we trained and evaluated the same classification models (XGBoost and RF), adding the HMM emission probabilities as predictor variables (on top of the baseline and diversity predictors). We found that those predictors did not improve the model performance.

Dataset Size: We analyzed the HMM and XGBoost models’ predictive performance for different trainset sizes. The results of this analysis are detailed in Appendix D2 and show that the performance of the models (AUC and F1-score) converges already when using about 80% of the data for the XGBoost models, and almost does not change for the HMMs when using 20% of the data or more. These findings suggest that our results hold regardless of the size of the dataset and that a larger dataset does not contribute to the baseline model in a way that enables it to outperform the diversity-based model.

## All Roads Lead to Rome (Robustness to Model Specification)

Our results show that progress to the “later” stages of the funnel is characterized by lower values of search diversity and that visits that culminate in reservations are characterized by lower diversity compared with visits that do not. In other words, there is a negative relationship between diversity values and progress in the funnel, as well as the likelihood of conversion. This relationship has been shown using multiple distinct and complementary approaches: model-free analyses, HMM, and, as elaborated in the Appendices, survival analysis, and even machine learning-based reservation prediction models. The different models we used are grounded in different assumptions. Accordingly, the fact that all models lead to the same conclusion strengthens our findings and suggests that they are valid regardless of specific assumptions.

## Discussion and Conclusion

Building upon the conversion funnel theory, coupled with research on consumers’ consideration sets, we examined whether the diversity of an online consumer’s searches can provide an indication, above and beyond standard engagement measures, regarding the consumer’s position in the conversion funnel and the likelihood of purchasing. We first developed three types of diversity measures (count-based, productnetwork-based, and dynamics-based) and showed that the search-diversity level of a given visit can be associated with the user’s current progress in the funnel and likelihood of conversion (RQ1). We then showed that our diversity measures are useful for predicting a user’s likelihood of conversion (RQ2).

To address RQ1, we presented model-free evidence and HMM analysis. In our model-free analysis, we showed that, on average, for all search-diversity measures, the diversity levels of a customer’s searches decrease with successive visits to the site (presumably reflecting progress in the funnel). This observation suggests that diversity is not constant but is rather a dynamic feature that changes over time.

Next, we showed that there is a negative relationship between the search-diversity level of a website visit (for all measures) and the likelihood that the user will make a purchase during that visit. For example, when controlling for the number of searches per visit, the mean diversity values are higher in visits that do not culminate in a reservation than in visits that do.

Then, we showed that the proposed diversity measures are useful for classifying visits into funnel stages. Specifically, we developed a four-state HMM—expected to correspond to the awareness, research, decision, and purchase stages of the funnel—and showed that the model states are indeed characterized by distinct patterns of search diversity. The patterns we observed were in line with our theoretical expectations. For example, the mean diversity values were highest in the second state of the HMM, representing the research stage, and lowest in the fourth state, representing the purchase stage.

To demonstrate the managerial and business implications of our theory and to address RQ2, we used our HMM to analyze the contributions of the different diversity measures to predict the likelihood of conversion. We compared the prediction performance of an HMM incorporating diversity measures to that of a baseline HMM incorporating well-known attributes of consumer engagement, including the number of searches, visit duration, and the number of previous visits (e.g., Bellman et al., 1999; Lin et al., 2010; Olbrich & Holsing, 2011; Johnson, 2004; Huang, 2009). We showed that the inclusion of all diversity measures significantly increased the recall, precision, and F1-score of the baseline model by factors of 3.1, 2.1, and 2.3, respectively. Additional analyses using more traditional classification models (XGBoost and random forest, see Appendix D) provide further robustness to the predictive value of our diversity measures. Compared with the HMM, which predicts conversion indirectly by predicting the consumer’s likelihood of being in the purchase state, the latter classification models constitute more straightforward (and accurate) conversion prediction tools that managers can easily implement in practice.

Our research offers several important contributions from both a theoretical perspective and a managerial perspective. First, we develop novel measures of search diversity and established (repeatedly using different models under different assumptions) that they can provide a window onto the consumer journey. The proposed measures are simple to use and, notably, do not require domain knowledge to capture the latent dimensions of product similarity. Rather, they rely on a product network in which the similarity between two products is defined according to the number of times they were searched for one after the other. Thus, it is straightforward to adapt the proposed measures to additional contexts, and particularly high-involvement products.

Second, we show that search diversity measures have the capacity to significantly improve predictions of a consumer’s likelihood of conversion, compared with a model based on standard engagement metrics. Accordingly, our diversity measures can support managers in identifying whom to target, potentially enabling them to avoid wasting resources on consumers who would have converted anyway or who are highly unlikely to convert. For a large online tourism company that spends hundreds of millions of dollars per year on targeting, the savings associated with even a slight improvement in targeting efficiency may be substantial. In Appendix E, we provide guidelines for implementing the proposed diversity measures and models in production.

Another contribution of our work, with both theoretical and managerial implications, relates to the relationship between consumer engagement and conversion likelihood. Specifically, previous studies have shown that common engagement measures, such as visit duration and number of pages viewed, are positively correlated with the likelihood of purchase (Olbrich & Holsing, 2011). Yet our results suggest that these measures should be interpreted in a nuanced manner: Specifically, visits that are more diverse, i.e., include more types of products (and can thus be considered to reflect high engagement), are in fact less likely to end with a purchase. This observation has important implications in practice: companies should not simply evaluate engagement levels without accounting for search diversity.

Finally, from a theoretical perspective, we add to the growing literature on the business implications and the informative value of product networks. As discussed above, it has been suggested that network inferences, which are based on aggregated consumer choices, can reveal latent (unobserved) relationships among products (Sundararajan et al., 2013). Our findings regarding the predictive potential of network-based searchdiversity measures seem to support this claim.

This paper is not without limitations. First, we focused on the tourism industry. While we expect our results to extend to other high-involvement products, further research is required for lowinvolvement products such as consumable products or products that are habitually purchased.

A second limitation is that our HMM analysis focused only on consumers who visited the website three times or more. It would be of interest to further develop our approach to map the funnel stages of consumers with fewer visits. Nevertheless, a key benefit of our diversity measures is in enabling managers to predict consumers’ conversion likelihood toward targeting various marketing activities. To this end, it is possible to use non-HMM prediction models—which can accommodate shorter funnels and whose predictive capacity may be superior to that of HMM, as elaborated in Appendix D (see also Appendix E for application guidelines). We further note that consumers with three visits or more are nevertheless interesting from a managerial perspective: Consumers who visit the website more frequently are effectively more engaged, providing the website with more opportunities to try to influence their final decision. Notably, our data show that more visits do not necessarily mean higher levels of conversion. In fact, although the consumers in our study visited the website at least three times, the conversion rate in our dataset is only 2.3%.

Third, our study did not distinguish between different types of consumers. Different consumers may demonstrate different search tendencies that manifest in different search-diversity patterns. For example, compared to a leisure traveler, a business traveler is likely to have a specific destination and flight date in mind, is less likely to be sensitive to price, and may thus be more likely to make a reservation. We suggest, however, that it is possible to interpret these different behavioral patterns as different levels of progress in the conversion funnel: the business traveler enters the funnel at the decision/purchase stage, whereas the leisure traveler is more likely to proceed sequentially through the stages.

Finally, the nature of our data did not enable us to examine certain additional variables that may be indicative of progress in the funnel, such as page type (category/product) and the textual content of consumers’ open search queries. Future research should investigate the respective roles of these measures and our proposed diversity measures in facilitating conversion prediction.

## Acknowledgments

We would like to thank the senior editor, the associate editor, and the three reviewers for their constructive and insightful comments and suggestions. Additionally, we would like to thank Karen Marron for her editorial assistance. This study benefitted from the generous support of the Amadeus@TAU lab, the Jeremy Coller Foundation, and the Henry Crown Institute of Business Research in Israel.

## References

Abhishek, V., Fader, P., & Hosanagar, K. (2012). The long road to online conversion: A model of multi-channel attribution. Available at https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=2158421.

Aggarwal, A., Alshehri, M., Kumar, M., Sharma, P., Alfarraj, O., & Deep, V. (2020). Principal component analysis, hidden Markov model, and artificial neural network inspired techniques to recognize faces. Concurrency and Computation: Practice and Experience, 33(9), Article 6157.

Argunsah, A. O., & Cetin, M. (2010). AR-PCA-HMM approach for sensorimotor task classification in EEG-based brain-computer interfaces. In Proceedings of <sup>t</sup>he 20th International Conference on Pattern Recognition (pp. 113-116).

Barry, T. E. (1987). The development of the hierarchy of effects: An historical perspective. Current Issues and Research in Advertising, 10(1-2), 251-295.

Bellman, S., Lohse, G. L., & Johnson, E. J. (1999). Predictors of online buying behavior. Communications of the ACM, 42(12), 32-38.

Benko, M., Härdle, W., & Kneip, A. (2009). Common functional principal components. The Annals of Statistics, 37(1), 1-34.

Bettman, J. R., Luce, M. F., & Payne, J. W. (1998). Constructive consumer choice processes. Journal of Consumer Research, 25(3), 187-217.

Bronnenberg, B. J., Kim, J. B., & Mela, C. F. (2016). Zooming in on choice: How do consumers search for cameras online? Marketing Science, 35(5), 693-712.

Calinon, S., & Billard, A. (2005). Recognition and reproduction of gestures using a probabilistic framework combining PCA, ICA and HMM. In Proceedings of <sup>t</sup>he 22nd international conference on Machine learning (pp. 105-112).

Carmi, E., Oestreicher-Singer, G., Stettner, U., & Sundararajan, A. (2017). Is Oprah contagious? The depth of diffusion of demand shocks in a product network. MIS Quarterly, 41(1), 207-221.

Chawla, N. V., Bowyer, K. W., Hall, L. O., & Kegelmeyer, W. P. (2002). SMOTE: Synthetic minority over-sampling technique. Journal of Artificial Intelligence Research, 16, 321-357.

Chernev, A. (2003). When more is less and less is more: the role of ideal point availability and assortment in consumer choice. Journal of Consumer Research, 30(2), 170-183.

Cho, Y.-H., Wang, Y., & Fesenmaier, D. R. (2002). Searching for experiences. Journal of Travel & Tourism Marketing, 12(4), 1- 17.

Clark, L., Ting, I. H., Kimble, C., Wright, P. C., & Kudenko, D. (2006). Combining ethnographic and clickstream data to identify user web browsing strategies. Information Research: An International Electronic Journal, 11(2), Article 249.

Court, D., Elzinga, D., Mulder, S., & Vetvik, O. J. (2009). The Consumer Decision Journey. McKinsey & Company. https://www.mckinsey.com/capabilities/growth-marketing-andsales/our-insights/the-consumer-decision-journey

Dellarocas, C., Katona, Z., & Rand, W. (2013). Media, aggregators, and the link economy: Strategic hyperlink formation in content networks. Management Science, 59(10), 2360-2379.

Dhar, V., Geva, T., Oestreicher-Singer, G., & Sundararajan, A. (2012). Prediction in economic networks: Using the implicit gestalt in product graphs. In Proceedings of the International Conference on Information Systems.

Ghose, A., Vir Singh, P., & Todri, V. (2017). Got annoyed? Examining the advertising effectiveness and annoyance dynamics. In Proceedings of the International Conference on Information Systems.

Goldenberg, J., Oestreicher-Singer, G., & Reichman, S. (2010). The quest for content: The integration of product networks and social networks in online content exploration. Proceedings of the International Conference on Information Systems

Goldenberg, J., Oestreicher-Singer, G., & Reichman, S. (2012). The quest for content: How user-generated links can facilitate online exploration. Journal of Marketing Research, 49(4), 452-468.

Goldstein, A., Raphaeli, O., & Reichman, S. (2016). Engagement, search goals and conversion: The different m-commerce path to conversion. In Proceedings of the International Conference on Information Systems.

Grange, C., & Benbasat, I. (2013). The value of social shopping networks for product search and the moderating role of network scope. In Proceedings of the International Conference on Information Systems.

Gu, B., Park, J., & Konana, P. (2012). Research note: The impact of external word-of-mouth sources on retailer sales of highinvolvement products. Information Systems Research, 23(1), 182-196.

Howard, J. A., & Sheth, J. N. (1970). The theory of buyer behavior. Journal of the American Statistical Association, 65(331), p. 1406-1407.

Huang, P. (2009). Searching for experience on the web: An empirical examination of consumer behavior for search and experience goods. Journal of Marketing, 73, 55-69.

Jang, H., Lee, S., Lee, S.-W., & Hong, S.-k. (2007). Expanding the individual choice-sets model to couples’ honeymoon destination selection process. Tourism Management, 28(5), 1299-1314.

Jansen, B. J., & Schuster, S. (2011). Bidding on the buying funnel for sponsored search and keyword advertising. Journal of Electronic Commerce Research, 12(1), 1-18.

Jerath, K., Ma, L., & Park, Y.-H. (2014). Consumer click behavior at a search engine: The role of keyword popularity. Journal of Marketing Research, 51(4), 480-486.

Johnson, E. J., Moe, W. W., Fader, P. S., Bellman, S., & Lohse, G. L. (2004). On the depth and dynamics of online search behavior. Management Science, 50(3), 299-308.

Katona, Z., & Sarvary, M. (2008). Network formation and the structure of the commercial world wide web. Marketing Science, 27(5), 764-778.

Lambrecht, A., & Tucker, C. (2013). When does retargeting work?: Information specificity in online advertising. Journal of Marketing Research, 50(5), 561-576.

Lee, K., & Seda, C. (2009). Search engine advertising: Buying your way to the top to increase sales. New Riders.

Leem, B., & Chun, H. (2014). An impact of online recommendation network on demand. Expert systems with applications, 41(4), 1723-1729.

Lewis, E. S. E. (1985). Financial advertising. Garland.

Lin, L., Hu, P. J.-H., Sheng, O. R. L., & Lee, J. (2010). Is stickiness profitable for electronic retailers? Communications of the ACM, 53(3), 132-136.

Lleras, J. S., Masatlioglu, Y., Nakajima, D., & Ozbay, E. Y. (2017). When more is less: Limited consideration. Journal of Economic Theory, 170, 70-85.

Mayzlin, D., & Yoganarasimhan, H. (2012). Link to success: How blogs build an audience by promoting rivals. Management Science, 58(9), 1651-1668.

Meiseberg, B. (2016). The effectiveness of e-tailers’ communication practices in stimulating sales of niche versus popular products. Journal of Retailing, 92(3), 319-332.

Moe, W. W. (2003). Buying, searching, or browsing: Differentiating between online shoppers using in-store navigational clickstream. Journal of Consumer Psychology, 13(1), 29-39.

Moe, W. W., & Fader, P. S. (2004). Dynamic conversion behavior at e-commerce sites. Management Science, 50(3), 326-335.

Montgomery, A. L., Li, S., Srinivasan, K., & Liechty, J. C. (2004). Modeling online browsing and path analysis using clickstream data. Marketing Science, 23(4), 579-595.

Netzer, O., Lattin, J. M., & v. Srinivasan 2008). A hidden Markov model of customer relationship dynamics. Marketing Science, 27(2), 185-204.

Nimetz, J. (2007). B2B marketing in 2007: The buying funnel vs. selling process. http://www.searchengineguide.com/jodynimetz/b2b-marketing-i-1.php.

Noordzij, M., Leffondré, K., van Stralen, K. J., Zoccali, C., Dekker, F. W., & Jager, K. J. (2013). When do we need competing risks methods for survival analysis in nephrology? Nephrology, dialysis, transplantation: official publication of the European Dialysis and Transplant Association—European Renal Association, 28(11), 2670-2677.

Oestreicher-Singer, G., & Sundararajan, A. (2010). Recommendation networks and the long tail of electronic commerce. Available at https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=1324064

Oestreicher-Singer, G., & Sundararajan, A. (2012). The visible hand? Demand effects of recommendation networks in electronic markets. Management Science, 58(11), 1963-1981.

Olbrich, R., & Holsing, C. (2011). Modeling consumer purchasing behavior in social shopping communities with clickstream data. International Journal of Electronic Commerce, 16(2), 15-40.

Pagani, M., & Mirabello, A. (2011). The influence of personal and social-interactive engagement in social TV web sites. International Journal of Electronic Commerce, 16(2), 41-68.

Rabiner, L., & Juang, B. (1986). An introduction to hidden Markov models. IEEE ASSP Magazine, 3(1), 4-16.

Rabiner, L. R. (1989). A tutorial on hidden Markov models and selected applications in speech recognition. In Proceedings of the IEEE, 77(2), 257-286.

Raphaeli, O., Goldstein, A., & Fink, L. (2017). Analyzing online consumer behavior in mobile and PC devices: A novel web usage mining approach. Electronic Commerce Research and Applications, 26, 1-12.

Ringel, D. M., & Skiera, B. (2016). Visualizing asymmetric competition among more than 1,000 products using big search data. Marketing Science, 35(3), 511-534.

Sirakaya, E., & Woodside, A. G. (2005). Building and testing theories of decision making by travellers. Tourism Management, 26(6), 815-832.

Spiggle, S., & Sewall, M. A. (1987). A choice sets model of retail selection. Journal of Marketing, 51(2), 97-111.

Sundararajan, A., Provost, F., Oestreicher-Singer, G., & Aral, S. (2013). Research commentary: Information in digital, economic, and social networks. Information Systems Research, 24(4), 883- 905.

Thomas, L., & Reyes, E. M. (2014). Tutorial: Survival estimation for Cox regression models with time-varying coefficients using SAS and R. Journal of Statistical Software, 61(Code Snippet 1), https://doi.org/10.18637/jss.v061.c01

Ting, I.-H., Clark, L., & Kimble, C. (2009). Identifying web navigation behaviour and patterns automatically from clickstream data. International Journal of Web Engineering and Technology, 5(4), 398-426.

Ting, I.-H., Clark, L., Kimble, C., Kudenko, D., & Wright, P. (2007). APD: A tool for identifying behavioural patterns automatically from clickstream data (pp. 66-73). Springer.

Todri, V., Ghose, A., & Vir Singh, P. (2019). Trade-offs in online advertising: Advertising effectiveness and annoyance dynamics across the purchase funnel. Information Systems Research (Forthcoming).

Um, S., & Crompton, J. L. (1990). Attitude determinants in tourism destination choice. Annals of Tourism Research, 17(3), 432-.

Vakratsas, D., & Ambler, T. (1999). How advertising works: What do we really know?” Journal of Marketing, 63(1), 26-43.

Visser, I. (2011). Seven things to remember about hidden Markov models: A tutorial on Markovian models for time series. Journal of Mathematical Psychology, 55(6), 403-415.

Visser, I., & Speekenbrink, M. (2010). depmixS4: An R package for hidden Markov models. Journal of Statistical Software, 36(7), https://doi.org/10.18637/jss.v036.i07

Wiesel, T., Pauwels, K., & Arts, J. (2011). Practice prize paper— Marketing’s profit impact: Quantifying online and off-line funnel progression. Marketing Science, 30(4), 604-611.

Zhang, Y., Li, B., Luo, X., & Wang, X. (2016). Modeling user engagement in mobile content consumption with tapstream data and field experiment. Available at https://doi.org/10.2139/ ssrn.2847634.

Zhang, Z., Guo, C., & Goes, P. (2013). Product comparison networks for competitive analysis of online word-of-mouth. ACM Transactions on Management Information Systems, 3(4), 1-22.

## About the Authors

Anat Goldstein is an assistant professor of knowledge and data engineering in the Department of Industrial Engineering and Management at Ariel University and a member of the Data Science and Artificial Intelligence Research Center. She holds a Ph.D. in information systems, an MBA, and a BA in computer science and economics all from Tel-Aviv University. Her research includes the development and application of data science and machine learning methods in the context of electronic-commerce, peer-to-peer platforms, medicine, and agriculture. Anat has published her work in numerous journals and conference proceedings.

Ohad Barzilay is a data science manager at Similarweb. After earning his Ph.D. in computer science, Ohad joined the department of information and technology management at the Coller School of Management at Tel Aviv University, where he studied the economics of digital platforms and electronic markets. Before joining academia, Ohad worked for some technology companies including Google, Jungo, VocalTec and BMC. He also served in the Israeli Chief Scientist Office on the committee for incubator and early-stage company funding, and on the scientific committee of the Blavatnik Interdisciplinary Center for Cyber Research.

Gal Oestreicher-Singer is The Mexico Professor of Information Systems and the associate dean of research at the Coller School of

Management at Tel Aviv University in Israel. She received her Ph.D. from the Stern School of Business at New York University. Her research focuses on the effects of social media, consumer engagement, and peer influence on electronic commerce outcomes, and on the effects of business models on electronic commerce. Her work has been published in the top journals in the fields of both Information Systems and Marketing. She currently serves as a senior editor at MIS Quarterly. She has also been the recipient of several prestigious grants and awards, most recently the ERC grant.

Inbal Yahav, a social scientist, is an assistant professor at Tel Aviv University Coller School of Management, Israel. Her main research interest lies in the areas of data science (DS), machine learning (ML), and natural language processing (NLP), with a focus on incorporating behavioral aspects into the ML and NLP algorithms. Dr. Yahav has presented her work at multiple conferences and has published papers in books and journals, including MIS Quarterly, Production and Operations Management, IEEE Transactions on Knowledge and Data Engineering, and Annals of Operations Research. She received her B.A. in computer science and her M.Sc in industrial engineering from the Israel Institute of Technology, and her Ph.D. in operations research and data mining from the University of Maryland, College Park in August 2010. Dr. Yahav is currently serving as an associate editor for the Informs Journal on Data Science and Decision Support Systems.

## Appendix A

## RQ1b Robustness Checks

To establish the statistical significance of the correlations between our search-diversity measures and the likelihood that a given funnel will end with a reservation (RQ1b), which are presented in the Model-Free Analysis section, we used survival (hazard) analysis as well as competing risk analysis. These analyses are presented in what follows.

## Survival Analysis

We used survival (hazard) analysis to connect the different diversity measures and the likelihood that a given funnel will end with a reservation (where the reservation is the “hazard”). The resulting model meets the proportional hazards assumption (p > 0.05), (Thomas & Reyes, 2014) Table A1 presents the Cox proportional hazard model. The coefficients of the diversity variables appear in bold.

In our context, a positive coefficient indicates that as the value of the variable increases, the reservation likelihood increases (and the time to reservation decreases). A negative coefficient indicates that the reservation likelihood decreases. Because the city and country measures are correlated, we only included the city and flight-date measures. As can be seen in Table A1 the coefficients of the count-based diversity measures (the top two variables) are significant and negative, thus supporting the results in Figure 6. For all the network-based diversity measures (third-fourth variables), the coefficients are significant and negative, thus supporting the results in Figure 4 (d-f) and in Figure 7. Finally, the results establish the connection between the dynamics-based diversity measures (fifth-sixth variables) and the reservation likelihood, and are in line with the results in Figure 8: the coefficients of city convergence and of date convergence are significant and negative. This means that single visits characterized by converging behavior (indicated by negative values) are more likely than nonconverging single visits (indicated by positive values) to culminate in a reservation. Put together, these findings strengthen our model-free findings on the negative relationship between diversity measures and reservation likelihood.

We also observe that the delta-price coefficient is significant and negative, meaning that when the price decreases within the visit (indicated by a negative delta-price value) the reservation likelihood increases.

Table A2 presents the results of the proportional hazards violation test. It shows that all p-values are higher than 0.05 and thus indicate that the proportional hazard assumption is not violated.  
Table A1. Time-Varying Cox Proportional Hazard Model

<table><tr><td></td><td>coef</td><td>exp(coef)</td><td>se(coef)</td><td>z</td><td>Pr(&gt;|z|)</td></tr><tr><td>No. of unique cities</td><td>-2.08E-01 ***</td><td>8.12E-01</td><td>1.99E-02</td><td>-10.431</td><td>&lt; 2e-16</td></tr><tr><td>No. of unique flight dates</td><td>-2.94E-02 ***</td><td>9.71E-01</td><td>9.89E-03</td><td>-2.975</td><td>0.002927</td></tr><tr><td>Avg. city distance from previous</td><td>-1.41E+01 ***</td><td>7.87E-07</td><td>2.63E+00</td><td>-5.337</td><td>9.47E-08</td></tr><tr><td>Avg. date distance from previous</td><td>-1.51E-02 ***</td><td>9.85E-01</td><td>1.55E-03</td><td>-9.733</td><td>&lt; 2e-16</td></tr><tr><td>Mean difference in city distances</td><td>-3.76E+01 ***</td><td>4.91E-17</td><td>7.72E+00</td><td>-4.867</td><td>1.14E-06</td></tr><tr><td>Mean difference in date distances</td><td>-1.26E-02 ***</td><td>9.88E-01</td><td>4.15E-03</td><td>-3.032</td><td>0.002433</td></tr><tr><td>Time to flight</td><td>-7.67E-02</td><td>9.26E-01</td><td>1.04E-01</td><td>-0.737</td><td>0.461005</td></tr><tr><td>Delta price</td><td>-2.92E-02 ***</td><td>1.00E+00</td><td>1.09E-04</td><td>-2.672</td><td>0.00753</td></tr><tr><td>Time of day: MORNING</td><td>-1.63E-01 ***</td><td>8.49E-01</td><td>4.77E-02</td><td>-3.427</td><td>0.000611</td></tr><tr><td>Time of day: NIGHT</td><td>-1.30E-01 **</td><td>8.78E-01</td><td>6.35E-02</td><td>-2.053</td><td>0.040074</td></tr><tr><td>Time of day: NOON</td><td>-3.91E-02</td><td>9.62E-01</td><td>4.47E-02</td><td>-0.874</td><td>0.382112</td></tr><tr><td>Avg. Travel Time</td><td>5.17E-03 ***</td><td>1.01E+00</td><td>9.23E-04</td><td>5.596</td><td>2.20E-08</td></tr><tr><td>Is Weekend</td><td>-5.82E-02</td><td>9.44E-01</td><td>4.19E-02</td><td>-1.388</td><td>0.165284</td></tr><tr><td>Session Duration</td><td>1.85E-04 ***</td><td>1.00E+00</td><td>3.14E-06</td><td>58.77</td><td>&lt; 2e-16</td></tr><tr><td>concordance</td><td colspan="5">0.771 (se = 0.005 )</td></tr><tr><td>Likelihood ratio test</td><td colspan="5">1757 ***</td></tr><tr><td>Wald test</td><td colspan="5">424.8***</td></tr><tr><td>Score (logrank) test</td><td colspan="5">6005 ***</td></tr><tr><td>Num. events</td><td colspan="5">3168</td></tr><tr><td>Num. obs.</td><td colspan="5">126330</td></tr></table>

Note: \*\*\*p < 0.01, \*\*p < 0.05, \*p < 0.1

<table><tr><td colspan="4">Table A2. Proportional Hazards Violation Test</td></tr><tr><td></td><td>Chi-squared</td><td>df</td><td>p</td></tr><tr><td>Time to flight</td><td>0.00171</td><td>1</td><td>0.967</td></tr><tr><td>Delta price</td><td>0.89633</td><td>1</td><td>0.344</td></tr><tr><td>Time of day</td><td>0.43495</td><td>3</td><td>0.933</td></tr><tr><td>Avg. Travel Time</td><td>0.04384</td><td>1</td><td>0.834</td></tr><tr><td>Is Weekend</td><td>0.02745</td><td>1</td><td>0.868</td></tr><tr><td>Session Duration</td><td>0.16689</td><td>1</td><td>0.683</td></tr><tr><td>No. of unique cities</td><td>1.01449</td><td>1</td><td>0.314</td></tr><tr><td>No. of unique flight dates</td><td>0.342</td><td>1</td><td>0.559</td></tr><tr><td>Avg city distance from previous</td><td>0.35176</td><td>1</td><td>0.553</td></tr><tr><td>Avg date distance from previous</td><td>2.81639</td><td>1</td><td>0.093</td></tr><tr><td>Mean difference in city distances</td><td>0.06196</td><td>1</td><td>0.803</td></tr><tr><td>Mean difference in date distances</td><td>2.72197</td><td>1</td><td>0.099</td></tr><tr><td>GLOBAL</td><td>6.49652</td><td>14</td><td>0.952</td></tr></table>

## Competing Risk Analysis

As a second robustness check, we ran a competing risk analysis (Noordzij et al., 2013). In this analysis, we assumed that a consumer continues to visit the website until one of two events occurs: a reservation or churn.

We analyzed the relationships between the different diversity measures and the probability of a reservation event while accounting for the competing event: churn. The relationships between the different diversity measures and the reservation event are summarized in Table A3. The results are in the same direction as the results of the Cox proportional hazard model: almost all diversity measures are negatively correlated with the probability of a reservation event, except for the number of city/date distance decreases, which is, as expected, positive. The only variable whose coefficient is positive, contrary to expectations, is the number of unique flight dates.

<table><tr><td colspan="6">Table A3. Competing Risk Analysis</td></tr><tr><td></td><td>coef</td><td>exp(coef)</td><td>se(coef)</td><td>z</td><td>p-value</td></tr><tr><td>No. of unique cities</td><td>-0.025</td><td>0.975</td><td>0.004</td><td>-5.640</td><td>0.000</td></tr><tr><td>No. of unique flight dates</td><td>0.011</td><td>1.010</td><td>0.001</td><td>10.170</td><td>0.000</td></tr><tr><td>Avg. city distance from previous</td><td>-3.650</td><td>0.026</td><td>1.834</td><td>-1.990</td><td>0.046</td></tr><tr><td>Avg. date distance from previous</td><td>-0.003</td><td>0.997</td><td>0.000</td><td>-8.970</td><td>0.000</td></tr><tr><td>Mean difference in city distances</td><td>-14.600</td><td>0.000</td><td>5.413</td><td>-2.700</td><td>0.007</td></tr><tr><td>Mean difference in date distances</td><td>-0.008</td><td>0.992</td><td>0.002</td><td>-3.640</td><td>0.000</td></tr></table>

## Appendix B

## Principal Component Analysis

In this appendix, we report the results of the PCA on the count-based (Table B1), network-based (Table B2) and dynamics-based (Table B3) measures. For each analysis, we report the proportion of variance captured by the first two components, and the loadings of the elements on the principal components. Note that we focus on the first two components, as they account for over 70% of the variance. Components 3 and above capture marginal proportions of the variance.

Interestingly, for all diversity dimensions (count based, network based, and dynamic), we consistently find that the first component of the PCA represents cases in which the country, city and date measures have the same sign; accordingly, we refer to this component as “overall diversity”. Similarly, the second component of all three outputs of the PCA represents cases in which country and city measures have the same sign, and date measures have the opposite sign. This component represents consumers who have made up their minds about the destination (city and country) but are still looking at a diverse set of dates, or vice versa. The rest of the components represent less frequent combinations of search diversity.

In the process of binning the PCA component values (as explained in the Modeling State Transitions section), in order to maintain the convention that positive diversity is related to “higher” values of the count-based and network-based variables, and to more “divergent” values of dynamics-based variables, we reversed the scale of our components (Benko et al., 2009).

<table><tr><td colspan="3">Table B1. Count-Based PCA Components, Variance Captured, and Loadings</td></tr><tr><td></td><td>PC1</td><td>PC2</td></tr><tr><td>Standard deviation</td><td>1.428</td><td>0.934</td></tr><tr><td>Proportion of Variance</td><td>0.680</td><td>0.291</td></tr><tr><td>Cumulative Proportion</td><td>0.680</td><td>0.971</td></tr><tr><td colspan="3">Loadings</td></tr><tr><td>No. of unique cities</td><td>-0.667</td><td>0.238</td></tr><tr><td>No. of unique countries</td><td>-0.668</td><td>0.228</td></tr><tr><td>No. of unique flight dates</td><td>-0.330</td><td>-0.944</td></tr></table>

<table><tr><td colspan="3">Table B2. Network-Based PCA Components, Variance Captured, and Loadings</td></tr><tr><td></td><td>PC1</td><td>PC2</td></tr><tr><td>Standard deviation</td><td>1.550</td><td>1.309</td></tr><tr><td>Proportion of Variance</td><td>0.400</td><td>0.306</td></tr><tr><td>Cumulative Proportion</td><td>0.400</td><td>0.706</td></tr><tr><td colspan="3">Loadings</td></tr><tr><td>Avg. city distance from previous</td><td>-0.474</td><td>0.066</td></tr><tr><td>Avg. country distance from previous</td><td>-0.468</td><td>0.066</td></tr><tr><td>Avg. date distance from previous</td><td>-0.118</td><td>-0.698</td></tr><tr><td>Total unique cities distance from first</td><td>-0.509</td><td>0.107</td></tr><tr><td>Total unique countries distance from first</td><td>-0.516</td><td>0.107</td></tr><tr><td>Total unique dates distance from first</td><td>-0.129</td><td>-0.694</td></tr></table>

<table><tr><td colspan="3">Table B3. Dynamics-Based PCA Components, Variance Captured, and Loadings</td></tr><tr><td></td><td>PC1</td><td>PC2</td></tr><tr><td>Standard deviation</td><td>1.211</td><td>0.993</td></tr><tr><td>Proportion of Variance</td><td>0.489</td><td>0.329</td></tr><tr><td>Cumulative Proportion</td><td>0.489</td><td>0.818</td></tr><tr><td colspan="3">Loadings</td></tr><tr><td>Mean difference in city distances</td><td>-0.698</td><td>0.111</td></tr><tr><td>Mean difference in country distances</td><td>-0.697</td><td>0.123</td></tr><tr><td>Mean difference in flight-date distances</td><td>-0.165</td><td>-0.986</td></tr></table>

## Appendix C

## Transition Models

Table C1 presents the transition coefficients. We report the coefficients of the state-dependent coefficients of the covariates (bootstrap means and standard errors). To compute the transition probabilities, we used the following equation:

$$
a _ {i j} = \frac {\exp (\beta_ {i j} ^ {0} + \beta_ {i j} ^ {1} t i m e T o F l i g h t + \beta_ {i j} ^ {2} d e l t a P r i c e)}{\sum_ {j = 1} ^ {4} \exp (\beta_ {i j} ^ {0} + \beta_ {i j} ^ {1} t i m e T o F l i g h t + \beta_ {i j} ^ {2} d e l t a P r i c e)}
$$

Note that the research state is used as the reference category.

<table><tr><td colspan="5">Table C1. State-Based Transition Probabilities</td></tr><tr><td colspan="5">Transition probabilities from the “awareness” state to all other states.</td></tr><tr><td>Coefficients:</td><td>Awareness</td><td>Research (reference category)</td><td>Decision</td><td>Purchase</td></tr><tr><td>(Intercept)</td><td>-9.631(0.04)</td><td>0</td><td>0.085(0.02)</td><td>-0.238(0.20)</td></tr><tr><td>timeToFlight</td><td>1.547(0.388)</td><td>0</td><td>-0.050(0.060)</td><td>-0.429(0.059)</td></tr><tr><td>deltaPrice (in 100$)</td><td>-0.231(0.004)</td><td>0</td><td>0.712(0.12)</td><td>1.105(0.16)</td></tr><tr><td>Probabilities at zero values of the covariates.</td><td>0(1.4E-05)</td><td>0.348 (1.2E-04)</td><td>0.378(0.065)</td><td>0.274(0.065)</td></tr><tr><td colspan="5">Transition probabilities from the “research” state to all other states.</td></tr><tr><td>Coefficients:</td><td>Awareness</td><td>Research (reference category)</td><td>Decision</td><td>Purchase</td></tr><tr><td>(Intercept)</td><td>-5.149(0.02)</td><td>0</td><td>-0.940(0.002)</td><td>-1.416(0.001)</td></tr><tr><td>timeToFlight</td><td>0.571(0.023)</td><td>0</td><td>-0.063(0.001)</td><td>-0.479(0.002)</td></tr><tr><td>deltaPrice (in $100)</td><td>0.023(3.3E-04)</td><td>0</td><td>-0.005(2.7E-05)</td><td>0.005(7.2E-05)</td></tr><tr><td>Probabilities at zero values of the covariates.</td><td>0.004(5.4E-04)</td><td>0.610 (1.9E-05)</td><td>0.238(1.1E-04)</td><td>0.148(4.4E-04)</td></tr><tr><td colspan="5">Transition probabilities from the “decision” state to all other states.</td></tr><tr><td>Coefficients:</td><td>Awareness</td><td>Research</td><td>Decision</td><td>Purchase</td></tr><tr><td>(Intercept)</td><td>-5.784(0.021)</td><td>0</td><td>0.420(0.001)</td><td>-0.504(0.001)</td></tr><tr><td>timeToFlight</td><td>2.495(0.215)</td><td>0</td><td>-0.458 (0.0004)</td><td>-0.802 (0.0003)</td></tr><tr><td>deltaPrice (in $100)</td><td>0.054(0.002)</td><td>0</td><td>0.010 (8.2E-05)</td><td>0.015(1.4E-04)</td></tr><tr><td>Probabilities at zero values of the covariates.</td><td>0.001(4.8E-04)</td><td>0.320 (5.7E-05)</td><td>0.486(7.2E-05)</td><td>0.193(5.0E-04)</td></tr><tr><td colspan="5">Transition probabilities from the “purchase” state to all other states.</td></tr><tr><td>Coefficients:</td><td>Awareness</td><td>Research</td><td>Decision</td><td>Purchase</td></tr><tr><td>(Intercept)</td><td>-5.914(0.150)</td><td>0</td><td>-0.172(2.3E-04)</td><td>0.289(8.0E-04)</td></tr><tr><td>timeToFlight</td><td>0.677(1.31)</td><td>0</td><td>-0.231(0.001)</td><td>-0.853(0.001)</td></tr><tr><td>deltaPrice (in $100)</td><td>0.017(0.003)</td><td>0</td><td>0.006(2.0E-04)</td><td>0.017(5.0E-04)</td></tr><tr><td>Probabilities at zero values of the covariates.</td><td>0.001(3.4E-04)</td><td>0.314 (8.1E-05)</td><td>0.265(2.4E-04)</td><td>0.420(9.3E-05)</td></tr></table>

## Appendix D

## Prediction Robustness Checks

## Additional Classification Algorithms

To further establish the predictive value of our diversity measures, beyond the results obtained with the HMM-based prediction model, we applied more traditional conversion classification algorithms, namely, XGBoost and Random Forest (RF).

As explained in the Methodology section, for the XGBoost and RF models, we are not limited by the length of the funnel and can include visits of shorter funnels as well, leading to a larger dataset. For example, for visits with at least five searches, we have 91,616 visits instead of 37,854 visits. To handle the imbalanced outcome classification in our dataset, we used the synthetic minority oversampling technique (SMOTE) (Chawla et al., 2002).

For each type of classification model (XGBoost and RF), we trained two models: The first includes the baseline attributes (see Table 1 and the categorical attributes that follow it<sup>8</sup>), and the second includes the baseline attributes as well as the diversity attributes (count-based, network-based, and dynamics-based). We further examined the effect of using the HMM’s emission probabilities as additional predictors on the models’ performance.

We examined two prediction approaches. In the first, we ignore the time component of the dataset (assuming time does not affect behavior, and there is no trend/ seasonality in the data). To establish the statistical significance of the results, we applied a bootstrap procedure, where we trained 20 models on randomly selected 90% of the dataset and tested them on the remaining 10% of the dataset. In the second approach, we examined a time-dependent model, which avoids the possibility that a model might be trained on data from later visits and then evaluated on earlier visits. That is, we used time-series analysis, where we trained our models on a growing window of visits (20%, 30%, …, 90%) and tested them on the subsequent visits (accounting for 10% of the dataset). Both approaches led to similar results.

Tables D1 and D2 present the reservation prediction results of XGBoost and RF models that were trained on the first five searches of a consumer’s visit (using visits having at least five searches). Each table includes three columns representing the three models (only baseline attribute, baseline + diversity attributes, and baseline + diversity+ emission probability attributes). The models were compared across a series of established classification performance metrics: AUC, recall, precision and F1-score. For each metric we present the mean and standard error of the repeating analyses. We observe that the inclusion of each type of diversity measure contributes to the performance of the prediction model (XGBoost and RF). In particular, when the diversity measures are included (Model 2), the values of recall and precision increase compared to the baseline model (Model 1) by about 6% and 4%, respectively, in the XGBoost model, and by about 8% and 3%, respectively, in the RF model. The emission probabilities from the HMM do not add value to the performance.

We repeated this analysis while training the conversion prediction models on the first three, four, five, six, and seven searches. Results are in the same direction as the results above, and are of similar magnitude. Figure D1 presents the F1-score values of these XGBoost (A) and RF (B) models (standard errors in parentheses). To verify that the superiority of the XGBoost models is not a result of the larger dataset, we also trained and evaluated the XGBoost models on a dataset including only visits that belong to long funnels, that is, to funnels of at least three visits. We show that in this case, too, the XGBoost models achieve substantially better prediction performance compared with the respective HMMs. The results are presented in Table D3.

Table D1. XGBoost Reservation-prediction Performance Metrics (bootstrap averages and standard errors) for the Different Prediction Models (#visits = 91,616)

<table><tr><td>Measure</td><td>Model 1: Baseline</td><td>Model 2: baseline + diversity</td><td>Model 3: baseline + diversity + emission</td></tr><tr><td>Recall</td><td>0.583 (3.1E-03)</td><td>0.649 (2.2E-03)</td><td>0.647 (2.5E-03)</td></tr><tr><td>Precision</td><td>0.197 (1.6E-03)</td><td>0.239 (1.8E-03)</td><td>0.239 (1.6E-03)</td></tr><tr><td>F1 score</td><td>0.295 (1.8E-03)</td><td>0.35 (2.0E-03)</td><td>0.349 (1.8E-03)</td></tr><tr><td>AUC</td><td>0.69 (1.1E-03)</td><td>0.718 (1.1E-03)</td><td>0.717 (1.1E-03)</td></tr></table>

Figure D1. F1-Score Values of Conversion Prediction Models that Were Trained on the First 3, 4, 5, 6, and 7 Searches of Each Visit of XGBoost Models (A) And RF Models (B)  
Table D2. Random Forest Reservation-prediction Performance Metrics (bootstrap averages and standard errors) For the Different Prediction Models (#visits = 91,616)

<table><tr><td>Measure</td><td>Model 1: Baseline</td><td>Model 2: baseline + diversity</td><td>Model 3: baseline + diversity + emission</td></tr><tr><td>Recall</td><td>0.62 (3.6E-03)</td><td>0.699 (2.5E-03)</td><td>0.703 (2.5E-03)</td></tr><tr><td>Precision</td><td>0.171 (1.3E-03)</td><td>0.207 (1.3E-03)</td><td>0.203 (1.3E-03)</td></tr><tr><td>F1 score</td><td>0.268 (1.6E-03)</td><td>0.319 (1.6E-03)</td><td>0.315 (1.6E-03)</td></tr><tr><td>AUC</td><td>0.795 (8.9E-04)</td><td>0.847 (8.9E-04)</td><td>0.845 (8.9E-04)</td></tr></table>

![](/api/attachments/XHYVAPFY/fulltext/images/b8ec1d9d34345a157861a88dc67a7d8ddb73f1ec6cb7147fdcfff54d49713f1b.jpg)  
A  
Note: We present the standard errors of time-series cross-validation in parentheses.

![](/api/attachments/XHYVAPFY/fulltext/images/4181ca8c2d2a8d5fdc9cbaed4a3b0e3e4c65308477bbc6cdce68854897f88eb4.jpg)

Table D3. XGBoost Reservation-Prediction Performance Metrics (bootstrap averages and standard errors) for the Different Prediction Models Trained on Visits of Long Funnels (with at least 3 visits)

<table><tr><td>Measure</td><td>Model 1: Baseline</td><td>Model 2: baseline + diversity</td><td>Model 3: baseline + diversity + emission</td></tr><tr><td>Recall</td><td>0.572 (3.1E-03)</td><td>0.62 (1.3E-03)</td><td>0.62 (1.8E-03)</td></tr><tr><td>Precision</td><td>0.186 (6.7E-04)</td><td>0.219 (8.9E-04)</td><td>0.219 (8.9E-04)</td></tr><tr><td>F1 score</td><td>0.281 (6.7E-04)</td><td>0.324 (2.0E-03)</td><td>0.324 (1.1E-03)</td></tr><tr><td>AUC</td><td>0.69 (8.9E-04)</td><td>0.71 (6.7E-04)</td><td>0.71 (8.9E-04)</td></tr></table>

Note: #visits= 37,854

## Dataset Size

## HMM with Different Dataset Sizes

To rule out the possibility that if additional observations had been used to train the baseline model, the model could achieve similar results to those achieved by the diversity-based models, we used different subsets (15%, 30%, 45%, 60%, 75%, and 100%) of the dataset (funnels) to train and test our models. For each dataset size, models were evaluated using bootstrap (10 samples of 90% of the training set).

The results are depicted in Figure D2 and show that performance, measured by F1-score, is similar for all trainset sizes for both model types, indicating that having additional data is not expected to improve our results.

![](/api/attachments/XHYVAPFY/fulltext/images/2de144f6567c94b5ba7536ab57650e372549ddf2c01da9c495d191889b4317bd.jpg)  
Note: The entire dataset (100%) had 37,854 visits. All models were evaluated (for each sample size) using bootstrapping (10 time resampling 90% of the funnels for training the model and testing it on the remaining 10%)

Figure D2. The performance in the F1-score of the Baseline (blue) and Diversity-Based (orange) HMMs as a Function of the Percentage of the Dataset Used for Training (15%, 30%, 45%, 60%, 75%, and 90%)

## XGBoost with Different Dataset Sizes

We repeated this analysis for the XGBoost models as well. Recall that for the HMM we used only visits of funnels with at least three visits, whereas for the XGBoost models we did not employ this constraint. Thus, the complete dataset included only visits with at least 5 searches, that is, 91,616 visits in total. We trained the prediction models using samples with different subsets of the dataset: 10%, 20%, 30%, …, 80%, and 90% of the visits. For each subset, models were evaluated using a bootstrap procedure (10 samples including 90% of the visits). The results are depicted in Figure D3 and show that performance, measured by F1-score (A) and AUC (B), begins to converge after using 80% of the data for both the baseline and diversity-based models. We further note that the performance differences across data sizes are not statistically significant (comparing the AUC and F1-score values of the different data sizes yields p > 0.05).

![](/api/attachments/XHYVAPFY/fulltext/images/c63c637087788e3a118f37f22bbfa4959a69c494b11cadebb2b4d204af386832.jpg)

![](/api/attachments/XHYVAPFY/fulltext/images/b8571b5ac0b9c1a4dc1c3ab4dc6ff7b22f0d7db243c4835616963d90de1b46ff.jpg)  
Note: The entire dataset (100%) had 91,616 visits. All models were evaluated (for each sample size) using a bootstrap procedure (10 samples of 90%).  
Figure D3. The Performance in F1-score (A) and AUC (B) of the Baseline (red) and Diversity-Based (blue) XGBoost Models as a Function of the Percentage of the Dataset Used for Training (10%, 20%, 30%, …, 80%, and 90%)

## Appendix E

## Application Guidelines

To apply the proposed measures in a production environment, the following steps should be followed:

Consumers’ search sequence logs should be used for developing a product network or several networks—each capturing a relevant attribute of the product (in our case—cities and countries, in a PC context these could be PC type (laptop, desktop), manufacturer (Dell, Asus, Lenovo…), CPU, hard drive type and so forth). The network should be developed based on consumers’ visits that were recorded over a period of several months in order to capture similarities between products. The network should be updated once in a while to capture trends and new products.

• Based on the product network(s), corresponding diversity measures should be defined that capture the count-based, network-based, and dynamics-based dimensions of each visit. In addition, these measures should be calculated based on the first n searches of the visit (n = three, four, five, six, or seven searches).

• Given the defined diversity measures, as well as additional baseline measures, conversion prediction models can be trained on existing data of the website. Once trained on existing data, the models can be deployed into production.

• In the production environment, whenever a consumer reaches three, four, five, six, or seven searches, diversity measures should be calculated on those searches and passed into the respective conversion prediction models in order to predict the likelihood that the visit will end with a conversion.

Given the prediction results, coupled with our insights on the probabilities to reside in different states, the website owner can decide whether and how to target the given consumer.

## Appendix F

## Datasets and Descriptive Statistics

As discussed in the Research Context and Data section, our raw dataset included 2,379,834 searches for flights. We aggregated searches and represented them at the visit-granularity level. This aggregation resulted in a total of 611,308 visits. When a consumer made multiple visits to the site, we aggregated consecutive visits that were no more than 10 days apart into what we called a “funnel” for that consumer. This aggregation resulted in a total of 395,322 funnels.

For different types of analyses, different subsets of the data were used. For the model-free analysis, we used the entire dataset (broken down differently for our analysis of each class of diversity measures, as explained in the main text). The descriptive statistics of the entire dataset are provided in Table 1 and in Table 2. For the explanatory HMM, we limited the analysis to funnels with at least three visits (referred to as “multivisit funnels” in Table 2). This dataset included 209,909 visits out of 611,308. Out of these visits, only 126,300 visits had price information. As our main HMM analyses incorporated price information, the results reported in Hidden Markov Model section are based on those 126,300 visits. Table F1 presents descriptive statistics of this dataset of 126,300 visits.

In the prediction models, we used the first n searches to predict the visit’s conversion. For example, for n = 4 we used the data from the first four searches to predict conversion. This limits us to data that include the cases with n searches. The dataset sizes are reported in Table 5.

Note that for prediction models that are not based on HMM, we do not need to limit the analysis to “multivisit funnels” (funnels with at least three visits), but only to funnel visits with at least n searches. For consistency, we run those models twice with two dataset sizes:

• The data for visits that include at least n searches (regardless of the number of visits per funnel)—these models’ results are presented in Table D1 and Table D2. Descriptive statistics of this dataset when n = 5 are provided in Table F2.

• The harsher limit of visits with at least n searches that are also part of “multivisit funnels” (results of these models appear in Table D3 and Table D4), which allows us to compare the models to the HMM model. Descriptive statistics of this dataset when n = 5 are provided in Table F3.

Table F1. Descriptive Statistics of Visit Attributes in Funnels with at Least 3 Visits, Including Price Information (in total: 126,330 Visits)

<table><tr><td>Attribute</td><td>Description</td><td>Mean</td><td>SD</td><td>Median</td><td>Min</td><td>Max</td></tr><tr><td>Visit duration</td><td>The total duration of the visit (seconds) measured between the start times of the first search and the last search</td><td>704.6</td><td>1059.9</td><td>298</td><td>1</td><td>23,094</td></tr><tr><td>Number of searches</td><td>The total number of searches conducted during the visit</td><td>4.65</td><td>4.51</td><td>3</td><td>2</td><td>130</td></tr><tr><td>Time-to-flight</td><td>The time from the visit start date to the first searched departure date (hours)</td><td>22.3</td><td>31.1</td><td>8.2</td><td>0.2</td><td>169.5</td></tr><tr><td>Average searched travel duration</td><td>The average travel duration searched in days</td><td>8.04</td><td>12.89</td><td>5</td><td>1</td><td>345.14</td></tr><tr><td>Previous visits</td><td>The number of previous visits of the consumer prior to the current visit</td><td>3.76</td><td>5.9</td><td>2</td><td>0</td><td>87</td></tr><tr><td>Searches in previous visit</td><td>Number of searches in the previous visit</td><td>3.22</td><td>4.56</td><td>2</td><td>0</td><td>200</td></tr><tr><td>No. of prev. reservations</td><td>Number of previous reservations of the user</td><td>0.21</td><td>1.23</td><td>0</td><td>0</td><td>43</td></tr><tr><td>Average price</td><td>The average price of flights searched during the visit</td><td>$519.4</td><td>$302</td><td>$448.09</td><td>$22.9</td><td>$9327</td></tr><tr><td colspan="7">Table F2. Descriptive Statistics of Visit Attributes of Visits with at Least 5 Searches (in total: 91,616 visits)</td></tr><tr><td>Attribute</td><td>Description</td><td>Mean</td><td>SD</td><td>Median</td><td>Min</td><td>Max</td></tr><tr><td>Visit duration</td><td>The total duration of the visit (seconds) measured between the start times of the first search and the last search</td><td>1302.96</td><td>1352.8</td><td>860</td><td>4</td><td>23,094</td></tr><tr><td>Number of searches</td><td>The total number of searches conducted during the visit</td><td>8.3</td><td>5.3</td><td>7</td><td>5</td><td>169</td></tr><tr><td>Time-to-flight</td><td>The time from the visit start date to the first searched departure date (hours)</td><td>22.7</td><td>31.3</td><td>8.19</td><td>0.2</td><td>153.8</td></tr><tr><td>Average searched travel duration</td><td>The average travel duration searched in days</td><td>8.25</td><td>13.22</td><td>5</td><td>1</td><td>345.14</td></tr><tr><td>Previous visits</td><td>The number of previous visits of the consumer prior to the current visit</td><td>2.57</td><td>6.5</td><td>0</td><td>0</td><td>250</td></tr><tr><td>Searches in previous visit</td><td>Number of searches in the previous visit</td><td>2.10</td><td>5.05</td><td>1</td><td>0</td><td>200</td></tr><tr><td>Number of previous reservations</td><td>Number of previous reservations of the user</td><td>0.15</td><td>1.16</td><td>0</td><td>0</td><td>43</td></tr><tr><td>Average price</td><td>The average price of flights searched during the visit</td><td>$536.8</td><td>$335.8</td><td>$460.8</td><td>$28.9</td><td>$7443</td></tr></table>

<table><tr><td colspan="7">Table F3. Descriptive Statistics of Visit Attributes of Visits with at Least 5 Searches in Multivisit Funnels (in total: 37,854 visits)</td></tr><tr><td>Attribute</td><td>Description</td><td>Mean</td><td>SD</td><td>Median</td><td>Min</td><td>Max</td></tr><tr><td>Visit duration</td><td>The total duration of the visit (seconds) measured between the start times of the first search and the last search</td><td>1420.55</td><td>1446.5</td><td>945</td><td>36</td><td>20,946</td></tr><tr><td>Number of searches</td><td>The total number of searches conducted during the visit</td><td>9.66</td><td>6.78</td><td>7</td><td>5</td><td>130</td></tr><tr><td>Time-to-flight</td><td>The time from the visit start date to the first searched departure date (hours)</td><td>24.1</td><td>33.5</td><td>7.5</td><td>0.2</td><td>134.37</td></tr><tr><td>Average searched travel duration</td><td>The average travel duration searched in days</td><td>8.45</td><td>12.40</td><td>5.47</td><td>1</td><td>301.2</td></tr><tr><td>Previous visits</td><td>The number of previous visits of the consumer prior to the current visit</td><td>2.95</td><td>3.94</td><td>2</td><td>0</td><td>39</td></tr><tr><td>Searches in previous visit</td><td>Number of searches in the previous visit</td><td>4.25</td><td>6.11</td><td>3</td><td>0</td><td>200</td></tr><tr><td>Number of previous reservations</td><td>Number of previous reservations of the user</td><td>0.25</td><td>1.56</td><td>0</td><td>0</td><td>44</td></tr><tr><td>Average price</td><td>The average price of flights searched during the visit</td><td>$536.8</td><td>$335.8</td><td>$460.8</td><td>$28.9</td><td>$7443</td></tr></table>
