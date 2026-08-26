---
otero_id: 15082
otero_key: "2FPR9CPA"
title: "Information Processing on Online Review Platforms"
authors: "Michael Siering; Christian Janze"
year: "2019"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2019.1661094"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Processing on Online Review Platforms

Michael SieringMICHAEL SIERING & Christian JanzeCHRISTIAN JANZE

To cite this article: Michael SieringMICHAEL SIERING & Christian JanzeCHRISTIAN JANZE (2019) Information Processing on Online Review Platforms, Journal of Management Information Systems, 36:4, 1347-1377, DOI: 10.1080/07421222.2019.1661094

To link to this article: https://doi.org/10.1080/07421222.2019.1661094

![](/api/attachments/2FPR9CPA/fulltext/images/cd03984329a800f41d0e02822cceb67ec90c875213a0b328fcb99abf9d4bf014.jpg)

Published online: 09 Oct 2019.

![](/api/attachments/2FPR9CPA/fulltext/images/82cee6861147d0222f833ec231b7a6e024df5679714ec4bfcbef2e8a2d47519b.jpg)

Submit your article to this journal

![](/api/attachments/2FPR9CPA/fulltext/images/ca20a0c2d4da53b0766c818cc4aba90f827182eeb3c7274b996649ffb8a97b61.jpg)

View related articles

![](/api/attachments/2FPR9CPA/fulltext/images/459bc39deaf21a91d2ca4d90a41b5cf668d56d1fdc8509fb01ff91c0e0c31bd2.jpg)

View Crossmark data

# Information Processing on Online Review Platforms

MICHAEL SIERING AND CHRISTIAN JANZE\*

MICHAEL SIERING (siering@wiwi.uni-frankfurt.de) is a Postdoctoral Research Associate at Goethe University Frankfurt, Germany and a Business Consultant in the fields of digitalization and risk management. He holds a Doctoral degree from Goethe University Frankfurt and was a Visiting Scholar at Penn State University. His research studies decision support in electronic markets, with a focus on the analysis of user-generated content and applications in investment management, fraud detection, and social commerce. His work has been published in such journals as Journal of Management Information Systems, Information Systems Journal, Journal of Information Technology, and Decision Support Systems.

CHRISTIAN JANZE (christian.janze2@gmail.com) holds a Doctoral degree from Goethe University Frankfurt. His research focuses on user generated content and has appeared in such venues as Decision Support Systems and the Proceedings of the International Conference on Information Systems.

ABSTRACT: Online reviews represent an important decision aid for consumers. Therefore, the question of whether online reviews reflect the currently available information is of high importance. Nevertheless, previous research neglects information processing on online review platforms. We address this research gap and analyze whether restaurant health inspection results have an impact on the review generation process of online restaurant reviews. We find that while severe health inspection results lead to changes of online review star ratings, information processing depends on the current environment. We find indications for corrective actions after critical health inspections: on the one hand, the restaurant health score improves, which shows an increase in restaurant quality. On the other hand, we observe indications for an increased amount of fake reviews in case of poorly-graded restaurants. We contribute to theory by providing an understanding of the nature of information processing on online review platforms. For practitioners, our findings allow for an understanding of the dynamics of online review generation. Furthermore, we outline the importance of considering the risk of deceptive behavior.

KEY WORDS AND PHRASES: online reviews, online review platforms, restaurant inspections, efficient market hypothesis, adaptive market hypothesis, event study, online deception, user-generated content.

## Introduction

User-generated online reviews are an important decision aid within consumers’ purchase decision making processes [28, 59, 68]. Previous research provides insights regarding the determinants of the perceived helpfulness of online reviews and their impact on consumers’ purchase decisions [15, 48]. From an economic point of view, these findings call for an answer to the fundamental question of whether and to what extent online reviews reflect the current quality of a product or service and, therefore, whether online reviews reflect the currently available information. However, there is a research gap regarding information processing on online review platforms. Within this study, we investigate whether and how online reviews react to external events and whether corrective actions are performed by market participants.

To investigate information processing on online review platforms, we rely on restaurant health inspection data from three cities, that is, Las Vegas, Toronto, and Pittsburgh. In these cities, health authorities regularly visit local restaurants to inspect food safety and summarize their findings by means of sanitary inspection grades. The inspection result resembles information about aspects that are usually hidden from restaurant visitors, such as the cleanliness of the restaurant kitchen [24]. Restaurants are obliged to publicly display the grade received in their windows. Additionally, these grades are also available to consumers online, as they are published on websites which can also be accessed on mobile devices.

Previous research shows that restaurant health inspections affect consumer behavior: Food safety is an important driver of the decision to select a specific restaurant [14, 33, 62] and, consequently, in case of bad grades, restaurants suffer from a significant decrease in revenue [30, 33].

From a theoretical point of view, we adapted the Efficient Market Hypothesis from financial markets research in order to explain information processing mechanisms: At their core, the Efficient Market Hypothesis (EMH) by Fama [12] posits that market participants process new information published, trade accordingly, and that, consequently, stock prices react to such new relevant information. We adapt this explanatory framework for the processing of new health inspection grades and their impact on restaurant reviews: Because of the visibility and importance of health inspection results, we investigate whether newly published inspection results represent new and relevant information that is noticed by online reviewers and how these inspection results are reflected in online restaurant reviews posted on the online review platform Yelp (Research Question 1).

Furthermore, building upon the Adaptive Market Hypothesis (AMH) [42], we also investigate whether corrective actions are taken in response to these health inspections: Therefore, we examine whether restaurant quality is improved after the health inspection (Research Question 2a) or whether the degree of fake reviews increases that might mitigate potentially negative consequences (Research Question 2b). Finally, we also investigate the overall drivers of information processing on online review platforms (Research Question 3).

To evaluate our research questions, we utilize a sample of 40,834 restaurant reviews posted on Yelp around 2,126 non-overlapping restaurant health inspections of 1,570 restaurants. From a methodological perspective, we perform different event studies and a logistic regression analysis to investigate information processing mechanisms on online review platforms as well as a potential increase in restaurant quality or deceptive behavior. We utilize an approach based on natural language processing and machine learning to automatically identify fake reviews.

Our results show that critical restaurant health inspections represent new relevant information which is incorporated in online review star ratings. We also find indications for corrective actions performed by restaurant owners in the form of an increased restaurant quality after the inspection. Nevertheless, also the amount of fake reviews increases after critical health inspections for poorly-rated restaurants. Our study thus extends previous research in the field of online reviews by focusing on the, thus far, neglected aspect of information processing on online review platforms as well as the question whether corrective actions are performed after the publication of critical health inspections. From a practical perspective, our study is highly relevant for restaurant visitors, restaurant owners, and public authorities.

The remainder of this paper is structured as follows: the Theoretical Background and Research Hypotheses section provides the theoretical background regarding online reviews, health inspections, as well as information processing in order to develop our research questions. The Research Design and Data Set section presents the details of our research design including the data collection and transformation procedures. The Empirical Study section presents the results, which are discussed in the following section, whereas we also specifically focus on alternative explanations for the observed behavior such as reviewers’ behavioral biases. Finally, the last section concludes the study.

## Theoretical Background and Research Hypotheses

## Online Reviews

On social commerce platforms, consumers communicate with other potential consumers by means of online reviews to share their experiences and opinions about products and services [40]. Such online reviews are important decision aids within the purchase decision-making process: Previous research indicates that reviews published by other customers influence the decision to buy specific products [15, 20, 68] or to consume specific services [43, 58, 59, 64] and thus influence product growth and performance [7, 67]. Consequently, online reviews are not only important for consumers, but also for online retailers, as they help to acquire new and to retain existing customers.

Previous research in the field of online reviews has primarily focused on the questions whether online reviews influence specific phases of the purchase decision-making process and how they influence competition [10, 35], which factors make online reviews helpful [26, 48, 50, 57, 65] or credible [29], whether specific characteristics of online reviews change when online consumers gain in experience [18, 45] and which factors influence the review generation process [6, 9, 17, 61]. Analyzing the content of online reviews, existing studies show that online reviews focus on aspects related to product quality or to specific product characteristics [32, 41, 56] and that such product features influence the economic impact of online product reviews [4, 55].

However, previous research largely neglects information processing on online review platforms, i.e. the question to what extent online reviews reflect the current information available regarding a specific product or service. In particular, it has been neglected that specific events could have an influence on online reviews. Especially in the case of online restaurant reviews, results of health inspections can be expected to have an enormous impact on a visitors’ restaurant evaluation and can thus be assumed to influence a restaurant’s user rating as well. Consequently, we address this research gap by investigating information processing of critical restaurant health inspections on online review platforms.

## Restaurant Health Inspections

Restaurant health inspections are performed by governmental health departments to ensure compliance of restaurants with food safety regulations. During each inspection, different aspects related to food handling, food temperature, personal hygiene, facility, and equipment maintenance, as well as vermin control are investigated, and, in the case of violations, penalized by means of a bad restaurant health rating.

Typically, the restaurant health ratings are readily available to restaurant visitors: First, restaurant owners are obliged to publicly disclose their health inspection grades prominently in their restaurant windows. Second, health inspection results are publicly available online. Third, restaurant visitors can check the health grades via mobile apps. Customers can explicitly search for specific restaurants or for restaurants with a specific grade. Furthermore, consumers can display the detailed inspection results and focus on critical events.

Previous research underlines the importance of restaurant inspection results for consumers and restaurant owners as food safety is an essential driver for restaurant choice [24]. Next to personal evaluations of food safety, externally provided ratings of health authorities impact consumer perceptions. For example, previous research has found that especially bad hygiene ratings have a significant negative influence on restaurant revenue due to changed restaurant visitor behavior [14, 33, 62].

Apart from the economic consequences of health inspections, few studies focus on the relation of user-generated content and ratings resulting from health inspections. Previous studies focus on the question whether visible aspects of restaurant hygiene are discussed in online reviews and whether user-generated content allows for predicting a restaurant’s official health inspection score: [31] analyze online reviews and forecast the official health inspection rating by means of a text mining approach; and [54] utilize Twitter messages and text analysis techniques to generate health scores and provide indications that these generated health scores are correlated with the actual health rating. Finally, [23] analyze online reviews to identify foodborne illness and find that consumers share their experiences about such incidents. The authors, therefore, assume that online reviews might be used to identify deficiencies in food handling.

However, previous studies neglect the question whether health inspections also disclose invisible information which is otherwise hidden from restaurant visitors and whether online reviews also react to the event of such health inspections. Therefore, we address this research gap and investigate whether critical health inspection results represent new information, have an impact on a restaurant’s rating and whether this leads to corrective measures by market participants.

## Research Questions

In our study, we examine the nature of information processing mechanisms on online review platforms. Thereby, we investigate whether critical health inspection results represent new information, are processed and reflected in online reviews and whether this triggers corrective actions by market participants.

As a theoretical lens for information processing on online review platforms, we rely on the EMH from financial market research: Information processing and information incorporation into stock prices are core questions researchers in the realm of financial markets are interested in. The EMH provides the theoretical foundations to explain the incorporation of new information into stock prices. The EMH is one of the most important foundations of contemporary theoretical and empirical research on financial markets. It postulates that “security prices always fully reflect available information” [12], ranging from the weak, semi-strong and strong form, depending on the information to be processed. According to the EMH, asset prices instantaneously react to relevant information, as market participants react to the new information and trade accordingly [5]. In information efficient markets, prices therefore fully reflect the information and expectations of all market participants [42].

We argue that online review platforms and online reviewers show similarities with regards to information processing: As in the case of market participants who are aware of new information and who trade accordingly, we assume that reviewers on online review platforms also take into account new information, that is, they consider this information when providing their product or service evaluation. Thus, online reviews should reflect the true quality of the service or product discussed.

We thus first investigate whether critical health inspections reveal new information which is incorporated within online reviews, as such health inspection results are very important for the selection of restaurants [24, 30]. In this case, the information revealed might be new since information such as the storage and handling of food in the kitchen area is typically not observable by restaurant visitors. Following the EMH, we investigate whether online reviews fully reflect all available information and therefore also fully reflect critical health inspection results. For instance, if severe health violations are found, it can be assumed that online review star ratings worsen once the results are published online, as bad hygiene ratings have a negative impact on the perceptions of the restaurant visitors [14, 33, 62]. Consequently, our first research question to be investigated is:

Research Question 1 (RQ1): Do critical restaurant health inspection results represent new information and how are critical restaurant health inspection results reflected in online restaurant reviews?

Beyond the EMH, the AMH [42] additionally considers evolutionary processes such as competition, reproduction, and natural selection due to social interactions and human behavior. AMH’s key tenet is that “survival is the only objective that matters” [42]. In previous financial research, it has been shown that “markets adapt to evolutionary selection pressures” [49]. In light of the very visible consequences of restaurant health inspection results (see Figure 1 for exemplary restaurant inspection grades displayed in restaurant windows) and the known impact of online reviews on sales figures, we assume that information processing and the resulting market reaction (i.e., changes in the online review star rating) depend on the goal of survival of the restaurant owner or related entities. As bad restaurant inspection results potentially damage the restaurant’s reputation and its economic raison d’être and therefore threaten its mere existence, we also investigate potential reactions to the critical inspection result.

There are two possible reactions towards critical restaurant health inspection results in order to ensure survival on the restaurant market: First, a restaurant owner could take corrective actions. In this case, the restaurant owner could increase restaurant quality by complying with food safety regulations to receive better restaurant health inspection results and, hence, more advantageous online reviews. Second, the restaurant owner or related entities being interested in the restaurant could try to mitigate the negative potential consequences of critical health inspection results. For instance, misleading fake reviews expressing false positive information related to the restaurant could be published. Therefore, we also examine the following research questions:

![](/api/attachments/2FPR9CPA/fulltext/images/e3a1f6ebd5c627882b7ad1aee0b8fffa381b1ec5c592e85dc4a8a95768007315.jpg)

![](/api/attachments/2FPR9CPA/fulltext/images/4f6b2b21b21299c4463c0f201aad100d3071e7180ee742bf9b0e45139498bebb.jpg)

![](/api/attachments/2FPR9CPA/fulltext/images/5bad0b09d8f306ada292ab0d51fe39e09307bdc1fa574c6f1bd6ee3b81f3f1ed.jpg)  
Figure 1. Exemplary Restaurant Inspection Results displayed in Restaurant Windows

Research Question 2a (RQ2a). Is restaurant quality increased in response to critical restaurant health inspection results?

Research Question 2b (RQ2b). Is an increased amount of fake reviews published in response to critical restaurant health inspection results?

Finally, having considered the impact of critical health inspections on online review platforms as well as the question of whether they cause corrective actions, we also investigate whether the specific reaction on the health inspection depends on the prior market environment by means of examining Research Question 3:

Research Question 3 (RQ3): What drives information processing on online review platforms?

Research Design and Data Set

Analyses Performed

To examine our research questions regarding the nature of information processing on online review platforms, we employ a three-step approach.

First, we investigate whether there is a reaction on critical restaurant health inspection results. Specifically, we conduct an event study to compare the mean star ratings prior and post to critical restaurant health inspections for both, the full sample of restaurants as well as sub-groups formed according to prior star ratings in order to investigate whether the critical health inspections represent new relevant information. To shed further light on information processing, we also focus on the directional change per star group.

Second, we study the two types of corrective actions employed to mitigate potential consequences of health inspection results to ensure the survival of the restaurant resulting from the AMH: In the first place, we look for indications of an actual improvement of the restaurant quality after critical health inspections. In the second place, we investigate potentially manipulative behavior by analyzing textual characteristics of the online reviews, reviewer characteristics of users contributing the online reviews as well as user feedback. Furthermore, we apply a machine learning approach to automatically identify fake reviews and conduct an additional event study.

Third, we explore the factors driving the observed reaction triggered by critical health inspections: We run a logistic regression to identify whether prior inspection-, review-, reviewer- and restaurant-specific factors influence information processing. Finally, we validate the impact of critical health inspections on restaurant visits. The following sections provide a detailed overview of our data collection efforts as well as our research methodology.

## Data Collection

For our study, we compiled three data sets covering restaurant health inspection results as well as the corresponding online restaurant reviews posted on Yelp, which represents a leading online platform for reviews on restaurants. Thereby, we focus on critical health inspections within the cities of Las Vegas, Toronto, and Pittsburgh. We define critical health inspections as health inspections with the worst grade except from immediate restaurant closure (if restaurant closure was included, we could not properly measure a change in star rating, as reviewers would not be able to actually visit the restaurant). Our data set covers 40,834 restaurant reviews posted on Yelp around 2,126 nonoverlapping restaurant health inspections of 1,570 restaurants posted from January 11, 2010 to December 12, 2018. Health inspections are defined as nonoverlapping if the time frame used for calculating the mean star rating prior and post to a health inspection (see the Variable Extraction section) does not overlap with the time frame used for calculating the mean star rating of another health inspection.

## Variable Extraction

From the datasets described in the previous section, we extract four variable categories to cover the inspection-specific, review-specific, reviewer-specific and restaurant-specific variables which are summarized in Table 1. In the following, the variable name suffix prior (Pr) indicates that a variable refers to the mean of a period of 60 days before the critical health inspection date, whereas post (Po) refers to the mean of a period of 60 days on and after the inspection date.

First, as inspection-specific variables, we calculate two metrics from the health inspection results based on the overall health score (HealthScore) received by a restaurant: HealthScCh0, HealthScCh1. These variables are related to three points in time, whereas $t _ { 0 }$ represents the health inspection under investigation, and $t _ { - 1 }$ and $t _ { 1 }$ represent the previous and next health inspection, respectively. HealthScCh0 is the change of the health score rating from $t _ { - 1 }$ to $t _ { 0 }$ in event time notation, and likewise, HealthScCh1 reflects the changes of the HealthScore from $t _ { 0 }$ to $t _ { 1 }$

Second, review-specific variables (averaged prior and post to the critical health inspection) are review depth, review sentiment, review deceptiveness as well as review usefulness. Review depth is represented by the word count of a review (MeanWCPr). The sentiment of the review is determined by the sentiment polarity (taking into account positive and negative word counts according to the General Inquirer Word lists and calculated as (positive – negative)/(positive + negative)) (MeanPolPr). Review deceptiveness is measured by means of a fake review classifier (MeanDecPr, see the section on the Publication of Fake Reviews) and review usefulness is measured by the useful votes received (MeanUsefulPr).

<table><tr><td colspan="3">Table 1. Variable Descriptions</td></tr><tr><td>Short Name</td><td>Full Name</td><td>Description</td></tr><tr><td>HealthScore</td><td>Health Score</td><td>Sum of violation points for inspection demerits of a given restaurant inspection (weight: 5 = significant, 3 = crucial, 1 = minor)</td></tr><tr><td>HealthScCh0</td><td>Health Score Change 0</td><td>Change of HealthScore from  $t_{-1}$  to  $t_0$ </td></tr><tr><td>HealthScCh1</td><td>Health Score Change 1</td><td>Change of HealthScore score from  $t_0$  to  $t_1$ </td></tr><tr><td>MeanWCPr/Po</td><td>Mean Word Count Prior/Post</td><td>Mean of review word count, prior/post</td></tr><tr><td>MeanPolPr/Po</td><td>Mean Polarity Prior/Post</td><td>Mean of review polarity, prior/post</td></tr><tr><td>MeanDecPr/Po</td><td>Mean Deceptive Prior/Post</td><td>Mean of binary variable containing 1 if a review is classified as fake and 0 otherwise, prior/post</td></tr><tr><td>MeanUsefulPr/Po</td><td>Mean Useful Prior/Post</td><td>Mean of review usefulness assessment, prior/post</td></tr><tr><td>MeanUStarsPr/Po</td><td>Mean User Star Rating Prior/Post</td><td>Mean of reviewer star rating assigned across the platform, prior/post</td></tr><tr><td>MeanUFriendsPr/Po</td><td>Mean User Friends Prior/Post</td><td>Mean of reviewer friends, prior/post</td></tr><tr><td>Star</td><td>Star Rating</td><td>Star rating of an online review, ranging from 1 (worst) to 5 (best)</td></tr><tr><td>MeanStarPr/Po</td><td>Mean Star Rating Prior/Post</td><td>Mean of review star rating, prior/post</td></tr><tr><td>StarDown</td><td>Star Down</td><td>Dummy Variable, 1 indicating a star rating decrease after a critical health inspection, 0 otherwise</td></tr><tr><td>RevsPr/Po</td><td>Reviews Prior/Post</td><td>Number of reviews per restaurant, prior/post</td></tr><tr><td>VisitsPr/Po</td><td>Visits Prior/Post</td><td>Number of restaurant check-ins prior/post</td></tr><tr><td colspan="3">Note: Prior (Pr) refers to a 60 day period before the health inspection date, whereas post (Po) refers to the 60 day period on and after the inspection date.</td></tr></table>

Third, we take into account reviewer-specific variables (averaged prior and post to the critical health inspection). Therefore, we consider the star rating assigned by the reviewer across the platform (MeanUStarsPr) as well as the reviewer’s number of friends (MeanUFriendsPr).

Fourth, we utilize individual star ratings expressed in a review (Star), to calculate the mean star rating (MeanStarPr). For each inspection and based on MeanStarPr, we determine the star group the inspection belongs to, i.e. a recoded version of the mean, with levels 1-2 (1 ≤ MeanStarPr < 2), 2-3 (2 ≤ MeanStarPr <3), 3-4 (3 ≤ MeanStarPr < 4) and 4-5 (=4 ≤ MeanStarPr ≤ 5). Additionally, we consider the binary variable StarDown which measures a decrease in star rating after the critical health inspection (1 = decrease, 0 = no decrease). Finally, we consider the mean number of online reviews (RevsPr), as well as the number of restaurant visits, measured by the number of check-ins reported on Yelp (VisitsPr).

## Empirical Study

## Information Processing of Restaurant Health Inspections

To examine the impact of health inspection results on online review star ratings and therefore to investigate the information processing mechanisms on online review platforms, we perform an event study. Event studies were introduced by [13] and are particularly useful to assess the information content of news [34]. In a financial context, researchers oftentimes examine the impact of specific events on the value of firms, that is, their free-float market capitalization [46]. Thereby, event studies are used to test the assumption of efficient capital markets [34]. There are countless phenomena analyzed utilizing event study methodology [2]. Examples include stock-splits [13], day patterns in trading [3], equity offerings and earnings management [52] as well as IT investments [27]. Event studies are also well-established in IS research (see for example [1, 11, 22, 63]).

While the typical event study is used to analyze the impact of events on stock prices, we apply event study methodology in a novel setting. We investigate the effects of restaurant health inspection results on star ratings of Yelp restaurant reviews by comparing the mean star ratings prior to and post to health inspections. Therefore, for each health inspection with a critical outcome and at least one review within 60 days before and after the inspection date, we calculate the mean star rating expressed in associated online reviews. We avoid confounding events by eliminating all overlapping restaurant inspections for each restaurant from the data set. We recoded dates within the Yelp and health inspection data sets in event time notation relative to the restaurant inspection date, where a negative (positive) integer represents the number of days prior (post) the event date.

Equation 1 shows how the mean star rating MeanStar is calculated. Let i denote the $i ^ { t h }$ health inspection out of m health inspections in the sample, r the $r ^ { t h }$ review about the restaurant of health inspection i and $n _ { i [ a , b ] }$ the number of reviews about the restaurant of health inspection i within a time period ranging from a to b and Star the star rating of a Yelp restaurant review.

$$
\text { MeanStar } = \frac {1}{m} \sum_ {i = 1} ^ {m} \frac {1}{n _ {i [ a , b ]}} \sum_ {r = 1} ^ {n _ {i [ a, b ]}} \text { Star } _ {i r}\tag{1}
$$

The mean star rating 60 days prior (Pr) and post (Po) to the 2,126 health inspections of the 1,570 restaurants in our sample is then given by Equation 2 and Equation 3 respectively.

$$
\text { MeanStarPr } = \frac {1}{2 1 2 6} \sum_ {i = 1} ^ {2 1 2 6} \frac {1}{n _ {i [ - 6 0 , - 1 ]}} \sum_ {r = 1} ^ {n _ {i [ - 6 0, - 1 ]}} \text { Star } _ {i r}\tag{2}
$$

$$
\text { MeanStarPo } = \frac {1}{2 1 2 6} \sum_ {i = 1} ^ {2 1 2 6} \frac {1}{n _ {i [ 0 , 6 0 ]}} \sum_ {r = 1} ^ {n _ {i [ 0, 6 0 ]}} \text { Star } _ {i r}\tag{3}
$$

As a robustness check, we repeat the event study with a shorter and a longer timewindow to include only online reviews 30 days or 90 days before and after the inspection date.

Table 2 presents the results of our event study regarding the impact of critical health inspections on online review star ratings posted on Yelp. In total, the analysis includes 20,618 user-generated online restaurant reviews prior to and 20,216 restaurant reviews post to restaurant health inspections. If health inspection results contain new relevant information, a change in the star rating should be observed.

Focusing on the consolidated sample covering all three cities, the percentage change of the mean star rating following a critical health inspection result is −1.27 percent and is significant at the 5 percent level.

Table 2. Impact of Health Inspections on Star Ratings – Consolidated Sample

<table><tr><td rowspan="2">Star Group</td><td rowspan="2">Mean StarPr</td><td rowspan="2">Mean StarPo</td><td rowspan="2">Change (percent)</td><td rowspan="2" colspan="2">P-Value</td><td colspan="2">Number of Posts</td></tr><tr><td>Prior</td><td>Post</td></tr><tr><td>Full</td><td>3.4899</td><td>3.4456</td><td>-1.27</td><td>0.0341</td><td>**</td><td>20,618</td><td>20,216</td></tr><tr><td>1-2</td><td>1.2005</td><td>2.6152</td><td>117.84</td><td>&lt;0.01</td><td>***</td><td>396</td><td>452</td></tr><tr><td>2-3</td><td>2.3959</td><td>2.8658</td><td>19.61</td><td>&lt;0.01</td><td>***</td><td>2,213</td><td>2,189</td></tr><tr><td>3-4</td><td>3.4082</td><td>3.4428</td><td>1.02</td><td>0.1294</td><td></td><td>8,265</td><td>7,600</td></tr><tr><td>4-5</td><td>4.3942</td><td>3.8215</td><td>-13.03</td><td>&lt;0.01</td><td>***</td><td>9,744</td><td>9,975</td></tr></table>

Note. $^ { * } p < 1 0$ percent. $\ast \ast _ { p } < 5$ percent. $\ast \ast \ast _ { p } < 1$ percent.

When taking a closer look at the star rating changes regarding specific star groups (depending on a restaurant’s mean star rating before the health inspection), we observe at a star group level that star ratings are significantly affected by restaurant health inspections. Consequently, health inspection results resemble new relevant information.

Interestingly, only in the case of inspections for restaurants with a prior star rating of 4-5 stars, star ratings react as assumed: critical health inspection results lead to a decrease of the mean star rating by 13.03 percent. In contrast, focusing on the other star groups, the mean star ratings increase by 117.84 percent, 19.61 percent, and 1.02 percent, respectively. All changes except from star group 3-4 are statistically significant at the 1 percent confidence level. We have also analyzed whether seasonal effects prevail regarding the impact of critical health inspections. Therefore, we have re-run our analysis for the different quarter years. Within this context, our results remain robust. Furthermore, we have re-run our analyses by only taking into account one health inspection per restaurant. Our results remain robust as well.

Furthermore, we also report the results for each city under investigation separately (see Table 3, Table 4, and Table 5). Here, we observe similar patterns related to the different cities. In total, the percentage change of online review star ratings for group 1-2, as well as 4-5 is higher in case of Toronto when compared to Las Vegas. Furthermore, the results are similar in the case of Pittsburgh as well, but the percentage changes have to be considered carefully as the number of critical health inspections in Pittsburgh is relatively small. In the following, we report the results of the pooled sample, as the results considering the different cities separately are comparable. Furthermore, since the amount of observations in case of Pittsburgh is quite small, we also evaluated our results without considering Pittsburgh. In this case, our results remain robust.

To gain additional insights into the nature of information processing mechanisms on online review platforms, we focus on the directional star change around the health inspection date (see Table 6).

Table 3. Impact of Health Inspections on Star Ratings – Las Vegas

<table><tr><td rowspan="2">Star Group</td><td rowspan="2">Mean StarPr</td><td rowspan="2">Mean StarPo</td><td rowspan="2">Change (Percent)</td><td rowspan="2" colspan="2">P-Value</td><td colspan="2">Number of Posts</td></tr><tr><td>Prior</td><td>Post</td></tr><tr><td>Full</td><td>3.5802</td><td>3.5158</td><td>-1.80</td><td>&lt;0.01</td><td>***</td><td>17,870</td><td>17,580</td></tr><tr><td>1-2</td><td>1.2289</td><td>2.4552</td><td>99.79</td><td>&lt;0.01</td><td>***</td><td>256</td><td>296</td></tr><tr><td>2-3</td><td>2.4130</td><td>2.9267</td><td>21.29</td><td>&lt;0.01</td><td>***</td><td>1,775</td><td>1,817</td></tr><tr><td>3-4</td><td>3.4487</td><td>3.4446</td><td>-0.12</td><td>0.5485</td><td></td><td>6,971</td><td>6,441</td></tr><tr><td>4-5</td><td>4.3860</td><td>3.9112</td><td>-10.83</td><td>&lt;0.01</td><td>***</td><td>8,868</td><td>9,026</td></tr></table>

Note. \*p < 10 percent. \*\*p < 5 percent. \*\*\*p < 1 percent.

Table 4. Impact of Health Inspections on Star Ratings – Toronto

<table><tr><td rowspan="2">Star Group</td><td rowspan="2">Mean StarPr</td><td rowspan="2">Mean StarPo</td><td rowspan="2">Change (Percent)</td><td rowspan="2" colspan="2">P-Value</td><td colspan="2">Number of Posts</td></tr><tr><td>Prior</td><td>Post</td></tr><tr><td>Full</td><td>3.2822</td><td>3.2795</td><td>-0.08</td><td>0.4795</td><td></td><td>2,699</td><td>2,583</td></tr><tr><td>1-2</td><td>1.1730</td><td>2.7809</td><td>137.08</td><td>&lt;0.01</td><td>***</td><td>138</td><td>152</td></tr><tr><td>2-3</td><td>2.3654</td><td>2.7475</td><td>16.15</td><td>&lt;0.01</td><td>***</td><td>436</td><td>369</td></tr><tr><td>3-4</td><td>3.3072</td><td>3.4227</td><td>3.49</td><td>0.0398</td><td>**</td><td>1,263</td><td>1,128</td></tr><tr><td>4-5</td><td>4.4178</td><td>3.5806</td><td>-18.95</td><td>&lt;0.01</td><td>***</td><td>862</td><td>934</td></tr></table>

Note. $^ { * } p < 1 0$ percent. $\ast \ast _ { p } < 5$ percent. $\ast \ast \ast _ { p } < 1$ percent.

Table 5 Impact of Health Inspections on Star Ratings – Pittsburgh

<table><tr><td rowspan="2">Star Group</td><td rowspan="2">Mean StarPr</td><td rowspan="2">Mean StarPo</td><td rowspan="2">Change (Percent)</td><td rowspan="2">P-Value</td><td colspan="2">Number of Posts</td></tr><tr><td>Prior</td><td>Post</td></tr><tr><td>Full</td><td>3.7351</td><td>3.8725</td><td>3.68</td><td>0.3561</td><td>49</td><td>53</td></tr><tr><td>1-2</td><td>1</td><td>3</td><td>200</td><td>-</td><td>2</td><td>4</td></tr><tr><td>2-3</td><td>2.5</td><td>4.3333</td><td>73.33</td><td>-</td><td>2</td><td>4</td></tr><tr><td>3-4</td><td>3.6389</td><td>4.3355</td><td>19.14</td><td>0.0182 **</td><td>31</td><td>31</td></tr><tr><td>4-5</td><td>4.3571</td><td>3.6667</td><td>-15.85</td><td>0.0801 *</td><td>14</td><td>15</td></tr></table>

Note. $^ { * } p < 1 0$ percent. $* * _ { p } < 5$ percent. $^ { * * * } p < 1$ percent.

Within the full sample, it is evident that critical health inspection results are reflected by worsening star ratings in only roughly half of the 2,126 cases. This changes dramatically when considering the sub-groups according to the star rating before the inspection. In the case of group 1-2, only 4.00 percent of critical health inspections are associated with worsening online review star ratings. The amount of worsening star ratings is rising for group 2-3 and 3-4. However, only in group 4-5, more than 50 percent of the critical health inspections are associated with worsening star ratings.

Table 6 Direction of Star Rating Change per Star Group

<table><tr><td rowspan="2">Star Group</td><td colspan="2">Star Rating Change</td><td rowspan="2"># Inspections</td></tr><tr><td>Worse</td><td>Better</td></tr><tr><td>Full</td><td>0.4774</td><td>0.5226</td><td>2,126</td></tr><tr><td>1-2</td><td>0.0400</td><td>0.9600</td><td>150</td></tr><tr><td>2-3</td><td>0.2979</td><td>0.7021</td><td>339</td></tr><tr><td>3-4</td><td>0.4569</td><td>0.5431</td><td>777</td></tr><tr><td>4-5</td><td>0.6430</td><td>0.3570</td><td>860</td></tr></table>

In summary, our empirical results from the event study indicate that health inspection results represent new and relevant information. Nevertheless, critical health inspection results lead to worsening online review star ratings only for restaurants with mean star ratings greater than 4 prior to the critical health inspection. In contrast, restaurants with mean star ratings prior to the inspection smaller than 4 yield different results: star ratings increase after critical health inspection results are published.

## Investigation of Corrective Actions

Based on the theoretical considerations of the AMH, we proceed to investigate measures to ensure survival in light of bad health inspection results. As previously discussed, restaurant owners can either increase restaurant quality or the number of fake reviews to mitigate the negative consequences of bad restaurant health inspection results. These two possibilities will be examined in the following.

## Increase in Restaurant Quality

In this section, we examine whether the quality of a restaurant improves after severe health inspection results in order to mitigate the negative consequences and to ensure survival. To do ${ \bf s o , }$ as already outlined, we define $t _ { O }$ as the health inspection date under investigation, $t _ { - I }$ as the previous and $t _ { I }$ as the next inspection date. We then calculate for each restaurant percentage changes in inspection demerit scores from $t _ { - I }$ to $t _ { O }$ (=HealthScCh0) and from $t _ { O }$ to $t _ { I }$ (=HealthScCh1). In order to assess star group-specific differences, we repeat this procedure for the full sample and each sub group (1-2, 2-3, 3-4, and 4-5 stars prior). Please note that we already removed confounding event dates from our analysis. Thus, it is impossible that the 60 day ranges overlap with another inspection date.

First, we validate whether critical health inspections actually lead to a worsening health score, i.e. to an increase of the number of inspection demerits from $t _ { - I }$ to $t _ { O } .$ The results of this analysis are reported in Table 7. Throughout all-star groups, we observe a significant change of the inspection demerits by more than 400 percent, which thus underlines the magnitude of the critical health inspection.

We assume that if corrective actions after a severe health inspection result are taken and restaurant quality is improved, this will also be noticed by the health authority during the next inspection. Consequently, the health authority will assign a better health score (i.e., lower inspection demerits) next time. Based on this reasoning, we actually consider the score change after the health inspection $( t _ { o }$ to $t _ { I } )$ under investigation. Thus, we can observe whether there is an actual increase in restaurant quality after the inspection.

The results of the analysis are shown in Table 8. Here, we find a significant increase in restaurant quality after critical health inspections, which is shown by reduced inspection demerits. This result is consistent for the different star groups. Please note that we repeated this analysis only including the reviews written 30 days before and within the 30 days after the health inspection, as well as considering a time period of 90 days. Our results remained robust.

Table 7. Changes of Inspection Demerits (t<sub>−1</sub> to $\mathbf { t } _ { 0 } )$

<table><tr><td rowspan="2">Star Group</td><td rowspan="2">Demerits  $t_{-1}$ </td><td rowspan="2">Demerits  $t_0$ </td><td rowspan="2">Change (Percent)</td><td rowspan="2" colspan="2">P-Value</td><td colspan="2">Number of Inspections</td></tr><tr><td>Prior</td><td>Post</td></tr><tr><td>Full</td><td>4.9889</td><td>26.0094</td><td>421.35</td><td>&lt;0.01</td><td>***</td><td>1801</td><td>1801</td></tr><tr><td>1-2</td><td>4.2462</td><td>22.3881</td><td>427.25</td><td>&lt;0.01</td><td>***</td><td>134</td><td>134</td></tr><tr><td>2-3</td><td>4.8547</td><td>25.2388</td><td>419.88</td><td>&lt;0.01</td><td>***</td><td>289</td><td>289</td></tr><tr><td>3-4</td><td>5.0861</td><td>26.3792</td><td>418.65</td><td>&lt;0.01</td><td>***</td><td>662</td><td>662</td></tr><tr><td>4-5</td><td>5.0922</td><td>26.6564</td><td>423.48</td><td>&lt;0.01</td><td>***</td><td>716</td><td>716</td></tr></table>

Note ${ \bf \ddot { \tau } } _ { p } < 1 0 $ percent. $\therefore p < 5$ percent. $^ { \ast \ast \ast } p < 1$ percent.

## Publication of Fake Reviews

In the following, we investigate whether the potentially negative consequences of health inspections lead to an increased number of fake reviews intended to shed a positive light on the specific restaurant. We do so in a multi-step process, examining the question from different angles and by employing different methodologies.

Therefore, we first consider textual characteristics of the online reviews contributed prior and post to critical health inspections and focus on their average number of words as well as their average emotiveness. Furthermore, we analyze the reviewers contributing the online reviews with a focus on their popularity, that is, their average number of friends as well as their general rating behavior represented by the average number of stars they assign on the platform. Additionally, we consider user feedback, by means of the amount of useful votes the reviews prior and post to critical health inspections receive. Finally, we also investigate the results of a fake review classifier enabling us to compare the fake review ratio prior and post to critical health inspections.

Table 8 Changes of Inspection Demerits $( \mathrm { t } _ { 0 }$ to $\mathbf { t } _ { 1 } )$

<table><tr><td rowspan="2">Star Group</td><td rowspan="2">Demerits  $t_{-1}$ </td><td rowspan="2">Demerits  $t_0$ </td><td rowspan="2">Change (Percent)</td><td rowspan="2" colspan="2">P-Value</td><td colspan="2">Number of Inspections</td></tr><tr><td>Prior</td><td>Post</td></tr><tr><td>Full</td><td>24.9956</td><td>9.0137</td><td>-63.94</td><td>&lt;0.01</td><td>***</td><td>2037</td><td>2037</td></tr><tr><td>1-2</td><td>21.5724</td><td>6.1586</td><td>-71.45</td><td>&lt;0.01</td><td>***</td><td>145</td><td>145</td></tr><tr><td>2-3</td><td>23.9179</td><td>7.9422</td><td>-66.79</td><td>&lt;0.01</td><td>***</td><td>329</td><td>329</td></tr><tr><td>3-4</td><td>25.4121</td><td>8.7638</td><td>-65.51</td><td>&lt;0.01</td><td>***</td><td>745</td><td>745</td></tr><tr><td>4-5</td><td>25.6565</td><td>10.1785</td><td>-60.33</td><td>&lt;0.01</td><td>***</td><td>818</td><td>818</td></tr></table>

Note ${ \bf \ddot { \tau } } _ { p } < 1 0 $ percent. $\therefore p < 5$ percent. $^ { \ast \ast \ast } p < 1$ percent.

Regarding the textual characteristics of online reviews, different studies in the field of deception detection focus on the depth of deceptive texts and provide a rationale that a reduced depth of a text is an indicator of deceptive behavior. Here, information manipulation theory [47] postulates that manipulators try to conceal or misrepresent information. Thus, the reticence of deceivers leads to a reduced length of writing [16]. Consequently, we also argue that deceptive market participants communicate by means of shorter messages than truth tellers [66]. Therefore, we conduct an additional event study focusing on the depth of the online reviews prior and post to critical health inspections.

Table 9 presents the results of the word count event study. For the full sample, a decrease by 0.36 percent in the mean word count can be observed, albeit it is of no statistical significance. The picture changes when looking at the different star groups. Here, statistically significant changes are evident. For example, the mean word count of observations within the star group 1-2 changed from 127.39 to 100.91 words (−20.79 percent). We observe that the changes of the mean word count at a star group level follow the same patterns like the mean star rating changes presented in Table 2.

Also, focusing on information manipulation theory, we assume that manipulators use a more positive language in order to whitewash restaurant quality. Considering the reviews’ average emotiveness (see Table 10), we observe that the higher the star group, the more positive the online reviews. Related to the impact of critical health inspections, we observe a significant decrease of review positivity by means of 4.77 percent for the full sample. Nevertheless, considering the percentage change for each star group separately, we also find indications for potential deceptive behavior, as the mean positivity in case of star group 1-2 increases by more than 470 percent, whereas the positivity of star groups 3-4 and 4-5 decreases.

Table 9. Impact of Health Inspections on Average Word Count

<table><tr><td rowspan="2">Star Group</td><td rowspan="2">Mean WCPr</td><td rowspan="2">Mean WCPo</td><td rowspan="2">Change (Percent)</td><td rowspan="2" colspan="2">P-Value</td><td colspan="2">Number of Posts</td></tr><tr><td>Prior</td><td>Post</td></tr><tr><td>Full</td><td>108.17</td><td>107.78</td><td>-0.36</td><td>0.4162</td><td></td><td>20,618</td><td>20,216</td></tr><tr><td>1-2</td><td>127.39</td><td>100.91</td><td>-20.79</td><td>&lt;0.01</td><td>***</td><td>396</td><td>452</td></tr><tr><td>2-3</td><td>121.98</td><td>110.27</td><td>-9.60</td><td>&lt;0.01</td><td>***</td><td>2,213</td><td>2,189</td></tr><tr><td>3-4</td><td>111.11</td><td>113.03</td><td>1.73</td><td>0.2256</td><td></td><td>8,265</td><td>7,600</td></tr><tr><td>4-5</td><td>96.71</td><td>103.28</td><td>6.79</td><td>&lt;0.01</td><td>***</td><td>9,744</td><td>9,975</td></tr></table>

Note. \*p < 10 percent. \*\*p < 5 percent. \*\*\*p < 1 percent.

Table 10. Impact of Health Inspections on Average Emotiveness

<table><tr><td rowspan="2">Star Group</td><td rowspan="2">Mean PolPr</td><td rowspan="2">Mean PolPo</td><td rowspan="2">Change (Percent)</td><td rowspan="2" colspan="2">P-Value</td><td colspan="2">Number of Posts</td></tr><tr><td>Prior</td><td>Post</td></tr><tr><td>Full</td><td>0.2833</td><td>0.2698</td><td>-4.77</td><td>0.0160</td><td>**</td><td>20,618</td><td>20,216</td></tr><tr><td>1-2</td><td>0.0216</td><td>0.1236</td><td>472.22</td><td>&lt;0.01</td><td>***</td><td>396</td><td>452</td></tr><tr><td>2-3</td><td>0.1692</td><td>0.2191</td><td>29.49</td><td>&lt;0.01</td><td>***</td><td>2,213</td><td>2,189</td></tr><tr><td>3-4</td><td>0.2764</td><td>0.2655</td><td>-3.94</td><td>0.0960</td><td>*</td><td>8,265</td><td>7,600</td></tr><tr><td>4-5</td><td>0.3801</td><td>0.3191</td><td>-16.05</td><td>&lt;0.01</td><td>***</td><td>9,744</td><td>9,975</td></tr></table>

Note. \*p < 10 percent. \*\*p < 5 percent. \*\*\*p < 1 percent

Next, we consider the characteristics of users contributing online reviews prior and post to critical health inspections. We assume that the more trustworthy a user is, the more friends he has: if a reviewer provides fake reviews, other users get aware of this behavior and refrain from being connected to this reviewer. In contrast, if a user provides genuine reviews, other users get aware of the user and should prefer being connected to such a valuable part of the community.

Thus, we first focus on the average number of friends of the reviewers contributing online reviews (see Table 11). Considering the full sample, we observe a significant increase of the users’ number of friends by 76.66 percent after critical health inspections. Nevertheless, specifically in star group 1-2, we observe a decrease in the mean number of friends by 36.14 percent, albeit of no statistical significance. This provides further indications for the contribution of fake reviews in star group 1-2, as the users contributing these reviews are less central parts of the community.

Table 11. Impact of Health Inspections on Active Reviewers: Friends

<table><tr><td rowspan="2">Star Group</td><td rowspan="2">Mean UFriendsPr</td><td rowspan="2">Mean Ufriends Po</td><td rowspan="2">Change (Percent)</td><td rowspan="2" colspan="2">P-Value</td><td colspan="2">Number of Posts</td></tr><tr><td>Prior</td><td>Post</td></tr><tr><td>Full</td><td>1.9436</td><td>3.4336</td><td>76.66</td><td>&lt;0.01</td><td>***</td><td>20,618</td><td>20,216</td></tr><tr><td>1-2</td><td>2.0281</td><td>1.2951</td><td>-36.14</td><td>0.2089</td><td></td><td>396</td><td>452</td></tr><tr><td>2-3</td><td>1.3020</td><td>3.2003</td><td>145.80</td><td>0.1085</td><td></td><td>2,213</td><td>2,189</td></tr><tr><td>3-4</td><td>2.2436</td><td>4.4875</td><td>100.01</td><td>0.0494</td><td>**</td><td>8,265</td><td>7,600</td></tr><tr><td>4-5</td><td>1.9104</td><td>2.9451</td><td>54.16</td><td>0.0277</td><td>**</td><td>9,744</td><td>9,975</td></tr></table>

Note. $^ { * } p < 1 0$ percent. $\ast \ast _ { p } < 5$ percent. $\ast \ast \ast _ { p } < 1$ percent.

Focusing on the reviewers’ rating behavior, we assume that if users provide fake reviews, their star ratings are on average more positive since they try to positively portray a specific restaurant. Thus, we focus on the overall number of stars assigned by the reviewers taking into account their reviews on the platform.

The results are reported in Table 12. We do not observe any significant changes for the full sample. Focusing on the different star groups changes this picture. Related to star group 1-2, users contributing online reviews prior to critical health inspections assign a mean number of 2.8335 stars throughout the platform. The online reviewers assessing the restaurant after the critical health inspections are generally much more positive, as their average star rating on the platform is 21.19 percent higher, that is, 3.4338. In contrast, in case of star group 4-5, users contributing online reviews after critical health inspections are more negative, as their overall assigned number of stars on the platform decreases by 3.81 percent (statistically significant at a 1 percent level). Thus, this also provides indications for a potentially increased number of fake reviews after critical health inspections in case of star group 1-2.

Table 12. Impact of Health Inspections on Active Reviewers: Stars

<table><tr><td rowspan="2">Star Group</td><td rowspan="2">Mean UStarsPr</td><td rowspan="2">Mean UStarsPo</td><td rowspan="2">Change (Percent)</td><td rowspan="2" colspan="2">P-Value</td><td colspan="2">Number of Posts</td></tr><tr><td>Prior</td><td>Post</td></tr><tr><td>Full</td><td>3.6583</td><td>3.6587</td><td>0.01</td><td>0.4887</td><td></td><td>20,618</td><td>20,216</td></tr><tr><td>1-2</td><td>2.8335</td><td>3.4338</td><td>21.19</td><td>&lt;0.01</td><td>***</td><td>396</td><td>452</td></tr><tr><td>2-3</td><td>3.3772</td><td>3.4874</td><td>3.26</td><td>&lt;0.01</td><td>***</td><td>2,213</td><td>2,189</td></tr><tr><td>3-4</td><td>3.6604</td><td>3.6622</td><td>0.05</td><td>0.4600</td><td></td><td>8,265</td><td>7,600</td></tr><tr><td>4-5</td><td>3.9113</td><td>3.7623</td><td>-3.81</td><td>&lt;0.01</td><td>***</td><td>9,744</td><td>9,975</td></tr></table>

Note. $^ { * } p < 1 0$ percent. \*\*p < 5 percent. $\ast \ast \ast _ { \mathrm { p } } < 1$ percent.

Table 13. Impact of Health Inspections on Average Review Usefulness

<table><tr><td rowspan="2">Star Group</td><td rowspan="2">Mean UsefulPr</td><td rowspan="2">Mean UsefulPo</td><td rowspan="2">Change (Percent)</td><td rowspan="2">P-Value</td><td colspan="2">Number of Posts</td></tr><tr><td>Prior</td><td>Post</td></tr><tr><td>Full</td><td>1.1474</td><td>1.0760</td><td>-6.22</td><td>0.0412 **</td><td>20,618</td><td>20,216</td></tr><tr><td>1-2</td><td>0.9275</td><td>0.8748</td><td>-5.68</td><td>0.3700</td><td>396</td><td>452</td></tr><tr><td>2-3</td><td>1.2084</td><td>0.8922</td><td>-26.17</td><td>0.0011 **</td><td>2,213</td><td>2,189</td></tr><tr><td>3-4</td><td>1.1568</td><td>1.1496</td><td>-0.62</td><td>0.4547</td><td>8,265</td><td>7,600</td></tr><tr><td>4-5</td><td>1.1532</td><td>1.1169</td><td>-3.15</td><td>0.2980</td><td>9,744</td><td>9,975</td></tr></table>

Note. $^ { * } p < 1 0$ percent. \*\*p < 5 percent. $\ast \ast \ast _ { p } < 1$ percent.

Finally, we also focus on the question on how the online reviews are perceived by the other users of the online review platform (Table 13). Here, we assume that genuine online reviews are perceived to be more useful than fake reviews. We focus on the average number of usefulness votes a review receives. We observe a general decrease of 6.22 percent for the full sample. Considering the different star groups, we first observe that the average review usefulness depends on the star group, whereas the higher the star group, the higher the usefulness. Furthermore, we observe that the usefulness in case of star group 1-2 decreases (even below the original level), but this decrease is not statistically significant.

The observed results provide indications for the potentially misleading behavior to ensure survival by the publication of an increased number of fake reviews in star group 1-2. Specifically, the average word count of these reviews decreases, the average emotiveness increases, the reviewers’ average number of friends decreases, as well as their mean platform star rating increases. Finally, online reviews within this group are perceived to be less useful. In contrast, we do not observe such behavior in the case of restaurants with four or more stars. We repeated the event studies presented with a shorter time-window as well as a broader time window to include only online reviews 30 (90) days before and after the health inspection date. The results remained robust.

We now proceed to further investigate the potential publication of fake reviews. To do so, we conduct the following analysis: first, we train a machine learning classification approach to automatically distinguish between fake and non-fake reviews based on a labeled data sample. Subsequently, we utilize the developed model to classify the unlabeled Yelp online reviews used throughout this study. Second, we run another event study to examine whether the share of fake reviews changes in light of critical health inspection results.

Figure 2 outlines our four-step process model to automatically determine whether an online restaurant review is deceptive or not. Within the first three steps (i.e., preprocessing, learning, evaluation), we use a labeled dataset to train and evaluate different machine learning classification algorithms. The dataset includes a total of 200 deceptive and 200 non-deceptive online reviews of Chicago-based restaurants and was compiled by Li et al. [38]. Within the fourth step of our approach (prediction), we predict for each restaurant review within our Yelp data sample whether it is potentially deceptive or not.

Within the data preprocessing step, we transform each review’s description text within both, the labeled and unlabeled data samples to lowercase. Additionally, we remove numbers, stop words (list taken from 37), whitespaces, and punctuation. Thereafter, we conduct word stemming using Porter’s stemming algorithm [51]. Subsequently, we use the labeled data sample to calculate term-frequency inverse document frequency (Tf-Idf) matrices for our analysis. Within the learning step of our approach, we utilize the labeled and pre-processed data sample to train a Support

![](/api/attachments/2FPR9CPA/fulltext/images/ea392a455aadaccee9a72e5033b755004988464c26783e2575e1ea7c9339159e.jpg)  
Figure 2. Deception Detection Machine Learning Process.

Vector Machine classifier (SVM, see [8]). To allow for a comparison of our results to the findings of Li et al. [38], we employ stratified 10-fold cross-validation to calculate various evaluation metrics. The resulting SVM-based classifier has an accuracy of 83.38 percent (performance for class “fake review”: precision = 89.09 percent, recall = 76.35 percent; class “no fake review”: precision = 79.04 percent, recall = 90.50 percent). We use cost-based learning in order to train the classifier such that about 20 percent of all cases are classified as suspicious [19]. Please be aware that for other cost-settings, different levels of suspicious reviews result, but that the results of this study remain robust.

Table 14 presents the results of the event study based on the predicted deceptiveness of the online reviews within our sample. Most strikingly, our results indicate that the share of fake reviews increases related to the observations in star group 1-2. Here, we observe a statistically significant increase of 26.97 percent in fake reviews after critical health inspection results (which are contributed by reviewers with a lower number of friends as well as a higher average star rating across the platform). In case of the other star groups, we measure a slight reduction of the number of reviews classified as fake.

Table 14. Impact of Health Inspections on Review Deceptiveness

<table><tr><td rowspan="2">Star Group</td><td rowspan="2">Mean DecPr</td><td rowspan="2">Mean DecPo</td><td rowspan="2">Change (Percent)</td><td rowspan="2">P-Value</td><td colspan="2">Number of Posts</td></tr><tr><td>Prior</td><td>Post</td></tr><tr><td>Full</td><td>0.2423</td><td>0.2357</td><td>-2.72</td><td>0.1944</td><td>20,618</td><td>20,216</td></tr><tr><td>1-2</td><td>0.1991</td><td>0.2528</td><td>26.97</td><td>0.0635 *</td><td>396</td><td>452</td></tr><tr><td>2-3</td><td>0.2669</td><td>0.2547</td><td>-4.57</td><td>0.2783</td><td>2,213</td><td>2,189</td></tr><tr><td>3-4</td><td>0.2450</td><td>0.2358</td><td>-3.76</td><td>0.2065</td><td>8,265</td><td>7,600</td></tr><tr><td>4-5</td><td>0.2376</td><td>0.2250</td><td>-5.30</td><td>0.1525</td><td>9,744</td><td>9,975</td></tr></table>

Note. \* p<10 percent, \*\* p<5 percent, \*\*\* p<1 percent.

To summarize, although the increase in average star rating after critical health inspections for star group 1-2 can be explained by an increase in restaurant quality, we also find indications for an increased publication of fake reviews within this star group. Consequently, restaurant owners or related market participants being interested in the restaurant follow a dual strategy after the publication of critical health inspections: on the one hand, they increase restaurant quality – but on the other hand, specifically for poorlyrated restaurants, they also try to portray the restaurant in a more positive light by the publication of an increased amount of suspicious fake reviews.

## Drivers of Information Processing

We further investigate whether information processing on online review platforms is driven by the environment. Specifically, we attempt to identify drivers that determine the changes in online review star ratings after critical health inspections. Therefore, we run a logistic regression with StarDown as the binary dependent variable. StarDown is defined as 1 if the mean star rating decreases after the critical health inspection. Otherwise, StarDown is defined as 0. Therefore, we consider inspection-, review, reviewer- and restaurant-specific aspects as independent variables which might influence StarDown. The formal representation of the logistic regression is presented in Equation 4. Table 15 presents the results of the logistic regression analysis.

$$
\begin{array}{l} \text { Prob } (\text { StarDown } = 1) = F \left(\beta^ {\prime} X\right) \\ = F \left( \begin{array}{l} \text { const } + \beta_ {1} \text { HealthScCh0 } + \beta_ {2} \text { MeanWCPr } + \beta_ {3} \text { MeanPolPr } \\ + \beta_ {4} \text { MeanDecPr } + \beta_ {5} \text { MeanUsefulPr } + \beta_ {6} \text { MeanUStarsPr } \\ + \beta_ {7} \text { MeanUFriendsPr } + \beta_ {8} \text { MeanStarPr } + \beta_ {9} \text { MeanRevsPr } \\ + \beta_ {1 0} \text { MeanVisitsPr } \end{array} \right) \end{array} \tag {4}
$$

where β0 is the parameter vector and X is the vector of regressors and F β0 X exp β0 X = 1 exp β0 X .

First, regarding inspection-specific aspects, we assume that the worse the health score change (i.e. the higher the number of inspection demerits observed), the higher the probability of a decrease in star rating. We actually find that the health score change has a positive influence on the decrease in star rating. Consequently, if the amount of inspection demerits increases, the probability of decrease in star rating is higher. This effect is statistically significant at the 10 percent confidence level and corresponds to the expectation that the worse the inspection result, the more pronounced the negative impact on the average star rating.

Second, focusing on review-specific aspects, we postulate that the more indications for fake reviews prior to the critical health inspection are present, the higher the probability that critical health inspections have a negative impact on the star rating, as the star rating before the inspection can be assumed to be exaggerated.

Table 15. Logistic Regression Results — Drivers of Decrease in Star Rating

<table><tr><td>Group</td><td>Independent Variable</td><td>Estimate</td><td>P-Value</td><td></td></tr><tr><td>Inspection-specific</td><td>HealthScCh0</td><td>0.0180</td><td>0.083</td><td>*</td></tr><tr><td rowspan="4">Review-specific</td><td>MeanWCPr</td><td>0.0008</td><td>0.426</td><td></td></tr><tr><td>MeanPolPr</td><td>-0.1504</td><td>0.622</td><td></td></tr><tr><td>MeanDecPr</td><td>0.4863</td><td>0.023</td><td>**</td></tr><tr><td>MeanUsefulPr</td><td>-0.0030</td><td>0.939</td><td></td></tr><tr><td rowspan="2">Reviewer-specific</td><td>MeanUStarsPr</td><td>0.2581</td><td>0.068</td><td>*</td></tr><tr><td>MeanUFriendsPr</td><td>0.0111</td><td>0.059</td><td>*</td></tr><tr><td rowspan="5">Restaurant-specific</td><td>MeanStarPr</td><td>0.9517</td><td>&lt;0.01</td><td>***</td></tr><tr><td>RevsPr</td><td>-0.0045</td><td>0.341</td><td></td></tr><tr><td>VisitsPr</td><td>0.0002</td><td>0.838</td><td></td></tr><tr><td>Intercept</td><td>-4.6029</td><td>&lt;0.01</td><td>***</td></tr><tr><td>McFadden&#x27;s Pseudo  $R^2$ </td><td>0.126</td><td></td><td></td></tr></table>

Note. $^ { * } p < 1 0$ percent. \*\*p < 5 percent. \*\*\*p < 1 percent.

Within our analysis, we find that the amount of fake reviews has a positive influence on the probability that the star rating decreases. This influence is statistically significant at the 5 percent level. An explanation is that in environments with a high number of fake reviews, a critical health inspection result is perceived as more surprising and more critically. Thus, it is translated into a lowering star rating. In contrast, we find no significant influence of prior number of words, prior sentiment as well as the prior number of useful votes received.

Third, related to reviewer-specific aspects, we assume that if a restaurant is covered by popular online reviewers, the probability of a star rating decrease is higher since these users can be assumed to be more experienced and objective. Within our analysis, we find a significant influence of both the reviewers’ mean number of friends as well as the reviewers’ mean star rating across the platform. In both cases, a higher number of friends as well as a more positive overall star rating increase the probability that a critical health inspection reduces the restaurant’s mean star rating. One explanation can be that highly-involved users are also more prone to provide a proper restaurant assessment in order to maintain a positive image within the community and thus incorporate critical health inspection results within their reviews.

Fourth, concerning restaurant-specific variables, we assume that restaurantaspects themselves have an impact on information processing. We find that a restaurant’s star rating before the critical health inspection is one of the main drivers of the star rating impact: The better the restaurant is perceived in terms of its prior rating, the more often a critical health inspection leads to a decline in star rating. The effect is significant at the 1 percent confidence level. In contrast, the number of online reviews as well as restaurant visits prior to the inspection has no significant influence.

Regarding the explanatory power of our model, we observe a McFadden’s Pseudo-R<sup>2</sup> of 0.126. The correlations between the variables are low and Variance Inflation Factors (VIFs) indicate that our model is not subject to multicollinearity (mean VIF = 1.55; highest VIF = 2.57).

To summarize, we find that information processing depends on the environment, whereas inspection-specific, review-specific, reviewer-specific and restaurant-specific aspects drive the change of online review star ratings. Whereas the impact of the health inspection result itself is quite obvious, the role of the reviewers covering a specific restaurant becomes clearer. Here, restaurants that are covered by reviewers who are highly-involved are more often accompanied by a star rating downgrade after critical health inspections than restaurants covered by less-involved reviewers.

## Impact on Restaurant Visits

Finally, we investigate the number of restaurant visits before and after critical health inspection results in order to shed further light on the impact of health inspections. At Yelp, users have the possibility to “check-in” via a mobile app when visiting a restaurant. Therefore, we use the number of check ins as a proxy for the amount of restaurant visits [21]. Based on previous research, we expect that restaurant visits should generally decrease after critical health inspections [14] or at least stay constant if restaurant quality recovers after the critical health inspection. In contrast, if a restaurant performs promotional campaigns in order to foster restaurant visits (for instance by means of gift coupons), we would expect an increase in restaurant visits.

Table 16 presents the results of the restaurant visit event study. In general, we find that the average number of restaurant visits depends on the star group, whereas the higher the star group, the higher the number of restaurant visits reported. We find that after a critical health inspection, the average number of restaurant visits decreases by up to 5 percent. For the full sample, this result is statistically significant. Considering the star groups, we observe that this is only significant for star group 3-4. Consequently, we do not observe a consistent significant decrease in restaurant visits, which might be driven by the fact that after a critical health inspection, restaurant quality nearly recovers to the original level prevailing before the critical health inspection (please also see section “Increase in Restaurant Quality”). Nevertheless, there is no increase in restaurant visits after the critical health inspection, which provides indications that no other strategies such as additional marketing campaigns are performed.

Table 16. Impact of Health Inspections on Restaurant Visits

<table><tr><td rowspan="2">Star Group</td><td rowspan="2">Mean VisitsPr</td><td rowspan="2">Mean VisitsPo</td><td rowspan="2">Change (Percent)</td><td rowspan="2" colspan="2">P-Value</td><td colspan="2">Number of Check-Ins</td></tr><tr><td>Prior</td><td>Post</td></tr><tr><td>Full</td><td>31.7970</td><td>30.9444</td><td>-2.68</td><td>0.0225</td><td>**</td><td>67,505</td><td>65,695</td></tr><tr><td>1-2</td><td>4.9933</td><td>4.7733</td><td>-4.41</td><td>0.3414</td><td></td><td>749</td><td>716</td></tr><tr><td>2-3</td><td>15.6903</td><td>15.4189</td><td>-1.73</td><td>0.2835</td><td></td><td>5,319</td><td>5,227</td></tr><tr><td>3-4</td><td>37.1587</td><td>35.1561</td><td>-5.39</td><td>&lt;0.01</td><td>***</td><td>28,798</td><td>27,246</td></tr><tr><td>4-5</td><td>37.9965</td><td>37.8417</td><td>-0.41</td><td>0.4202</td><td></td><td>32,639</td><td>32,506</td></tr></table>

Note. $^ { * } p < 1 0$ percent. $\ast \ast _ { p } < 5$ percent. $\ast \ast \ast _ { p } < 1$ percent.

## Discussion

Within this study, we investigate the nature of information processing on online review platforms. Building upon the EMH, we investigate whether online reviews reflect the available information (RQ1). We therefore examine whether critical health inspection results represent relevant information and are thus accompanied by changes in online review star ratings. Based on our event study presented in Table 2, we observe that critical health inspection results can be regarded as new relevant information. Our results show that there is a statistically significant impact of critical health inspection results on online review star ratings when considering the full sample of restaurant reviews, whereas the mean star rating decreases by −1.27 percent. We show that reactions to such information depend on the current environment. Within the results of our event study presented in Table 2 and Table 6, we show that in case of restaurants with high prior star ratings, critical health inspection results lead to a decrease in star ratings. However, in case of restaurants with low star ratings, this reaction is reversed, that is, following critical health inspection results, online review star ratings increase.

Furthermore, the AMH centers on survival as the most important objective of individuals. We therefore examine whether restaurant owners or other entities interested in restaurant survival perform corrective actions in order to mitigate the negative effects of critical health inspection results. Our study shows that critical health inspections trigger improvements in restaurant quality, a factor that can be directly influenced by the restaurant owner (RQ2a). Nevertheless, we also find indications for potentially deceptive behavior. More precisely, we find indications for the contribution of fake reviews in lower star groups (RQ2b). Within this context, a critical health inspection result could also have an impact on online reviewers usually contributing genuine reviews, as it is possible that these reviewers might refrain from visiting the restaurant thus further increasing the relative amount of fake reviews.

Focusing on the drivers of information processing (RQ3), we underline that the reaction is driven by the current environment. Next to the inspection result, we find that the reviewers covering a specific restaurant, but also restaurant quality itself drive the question of whether a critical health inspection leads to a decrease in star rating.

Finally, we observe that restaurant visits slightly decrease after critical health inspections. This can be explained by the fact that on the one hand, critical health inspections lead to a decrease in restaurant perception, specifically for star groups 4-5. On the other hand, the health score improves after the inspection. Thus, this is an explanation why there is no excessive decrease in the number of restaurant visits. Finally, since there is no overall increase in restaurant visits, other countermeasures, for instance in form of promotions, are rather unlikely.

When analyzing our results, we also evaluated different alternative explanations for the observed restaurant rating behavior. Previous research in the field of online reviews indicates that review contributors are prone to several biases when publishing their reviews. On the one hand, previous research has shown that a selfselection bias can prevail when early reviewers evaluate products or services more positively than later reviewers, as early reviewers might be more enthusiastic about the product or service [39]. Although such a behavior could also be assumed to prevail in the field of restaurant reviews, our results show that the self-selection bias cannot have a consistent influence in case of restaurant health inspections. As shown by our study, especially in the case of restaurants with a low star rating, star ratings increase and thus show that earlier reviewers are even more negative than later reviewers. More important, it is very unlikely that the information released by the health inspection is taken into account in the earlier online reviews as it is ordinarily hidden from restaurant visitors. Consequently, the self-selection bias is very unlikely to influence the information processing of restaurant health inspections. Self-selection could also prevail regarding restaurant visitor behavior: if negative inspection results are published, it could be assumed that potential restaurant visitors are scared because of the inspection results, do not visit the restaurant and thus do not leave any reviews. Nevertheless, as our results show, star ratings decrease in case of restaurants with a high star rating after critical inspection results. Although the mean star rating increases for restaurants with a low star rating, our analysis reveals that this is rather caused by potentially deceptive behavior instead of self-selection. In addition to that, the amount of online reviews before and after severe health inspection results remains slightly the same.

On the other hand, a stream of research reports on the disconfirmation bias when reviewers match their own product or service experience with the expectations evoked by online reviews [25, 60]. Here, reviewers are more likely to post a review (and are more likely to be biased regarding their evaluation) when their expectations are disconfirmed. At a first glance, this could be an explanation for the observed behavior when poorly rated restaurants receive star ratings which are higher than the previous mean star ratings, as a restaurant reviewer could be positively surprised about a restaurant.

Nevertheless, there are three major reasons why the disconfirmation bias is unlikely to cause the observed behavior. First, we show that the underlying event, i.e. the critical health inspection outcome, reveals information that was not publicly available before, such as unsatisfactory kitchen cleanliness. As a consequence, these results have not been discussed in prior online reviews. Furthermore, even after the health inspection, restaurant visitors cannot make an own assessment of kitchen cleanliness as they cannot investigate the kitchen on their own. Consequently, although these health inspection results can be assumed to have an influence on the reviewers’ expectations, these expectations cannot be (dis-)confirmed after a restaurant visit. Second, our results clearly show that especially in the case of poorly graded restaurants, the average word count of reviews after the critical health inspection decreases. In contrast, in case of disconfirmation of a reviewer’s expectations, it can rather be assumed that the word count would increase as reviewers justify why they do not agree with the previous opinion [60]. Third, previous research has also found that restaurants are more likely to publish fake reviews when their reputation is weak [44] as they influence restaurant visibility [36]. With this respect, our fake review detection model also provides indications for an increase in fake reviews.

We are aware that the analysis of information processing depends on the question of whether new information published is relevant for online reviewers. Luckily, the regulatory environment makes restaurant health inspection results publicly visible within the restaurant as well as the Internet. In addition, previous research shows that such health inspections reveal information that is usually hidden from restaurant visitors and thus influences restaurant image as well as sales [14, 33]. Furthermore, due to our event study design, we make sure that an influence of other unobserved factors on the results of the event study is unlikely: Next to fake review publication, we take into account an increase in restaurant quality as a driver of the reaction after the health inspection. As we take into account different short time spans for our event study, we reduce the risk that other unobserved factors have an influence. We conclude that health inspection results are visible, relevant and thus suitable to investigate information processing on online review platforms. Here, we also properly take into account other possible influences on the observed reaction and conclude that the critical health inspections provide new relevant information.

In addition, previous research attempted to use social media as a predictor for health inspection outcomes. We are aware of the possibility that health inspection results are driven by online reviews previously posted on online review platforms. However, our results also clearly show that critical health inspections have an impact on online reviews.

Finally, as we analyze restaurant reviews published on the platform Yelp, we are aware that health inspections are organized differently in other cities, which could influence information processing mechanisms. Nevertheless, we focus on three different cities in the United States (Las Vegas and Pittsburgh) and Canada (Toronto) in order to proxy for different cultures and cuisines. Furthermore, specifically Las Vegas attracts a large number of tourists, which rules out influences from single cultures and thus increases the robustness of our results.

## Conclusion

Online reviews are an important driver of purchase decisions as well as an important asset for online retailers. It is of high importance whether online reviews reflect the information available related to a specific product or service. Nevertheless, previous research neglects information processing on online review platforms and the subsequent product or service vendor reactions.

With this study, we contribute to the literature on online reviews by investigating whether critical health inspection results represent new information and whether they are reflected by restaurant reviews. Building upon the EMH, we show that critical health inspection results represent new information: While health inspection results are reflected in online reviews, the analysis of information processing mechanisms reveals an unexpected behavior. In many cases, critical health inspection results lead to increased star ratings. Referring to the AMH, we provide evidence for corrective actions employed to mitigate the potentially negative effects of critical health inspection results. Specifically, we show that restaurant owners or associated individuals try to ensure the survival of restaurants by improving restaurant quality, but also by contributing an increased amount of fake reviews. Additionally, we show that the reaction depends on the current environment. Finally, we rule out other influences like potential behavioral biases.

Our results are of high practical relevance for various stakeholders on online review platforms: Most importantly, our results show that market participants care about critical health inspections and that restaurant owners should be aware of the negative effects of critical health inspection results: In case of restaurants which are well-received by online reviewers and which exhibit a high star rating, critical health inspection results lead to a decrease of the star rating. This could result in lower sales figures. Therefore, restaurant owners should comply with health regulations to avoid bad inspection results. Furthermore, readers of online reviews should be aware of fake reviews — especially in case of poorly rated restaurants. Consequently, platform operators should implement appropriate detection techniques, for example, machine learning approaches as utilized in this study. From a regulatory perspective, financial markets are heavily regulated to protect market participants from deceptive behavior. To our knowledge, no such regulations exist in the realm of online review platforms. Because of the influence of online reviews on sales figures, regulatory authorities should put more emphasis on monitoring online review platforms and introduce specific regulations to deal with deceptive behavior of platform participants.

Acknowledgment: The authors thank the review team for providing very constructive feedback which has helped to significantly improve the manuscript throughout the review process.

## REFERENCES

1. Aggarwal, N; Dai, Q; and Walden, E.A. The more, the merrier? How the number of partners in a standard-setting initiative affects shareholder’s risk and return. MIS Quarterly, 35, 2 (2011), 445–462.

2. Ahern, K.R. Sample selection and event study estimation. Journal of Empirical Finance, 16, 3 (2009), 466–482.

3. Ajinkya, B.B. and Jain, P.C. The behavior of daily stock market trading volume. Journal of Accounting and Economics, 11, 4 (1989), 331–359.

4. Archak, N; Ghose, A; and Ipeirotis, P.G. Deriving the pricing power of product features by mining consumer reviews. Management Science, 57, 8 (2011), 1485–1509.

5. Charles, A; Darné, O; and Kim, J.H. Exchange-rate return predictability and the adaptive markets hypothesis: Evidence from major foreign exchange rates. Journal of International Money and Finance, 31, 6 (2012), 1607-1626.

6. Chen, H; Hu, Y.J; and Huang, S. Monetary Incentive and Stock Opinions on Social Media. Journal of Management Information Systems, 36, 2 (2019), 391–417.

7. Clemons, E.K; Gao, G.G; and Hitt, L.M. When online reviews meet hyperdifferentiation: A study of the craft beer industry. Journal of Management Information Systems, 23, 2 (2006), 149–171.

8. Cortes, C. and Vapnik, V. Support-vector networks. Machine Learning, 20, 3 (1995), 273–297.

9. Dellarocas, C; Gao, G; and Narayan, R. Are consumers more likely to contribute online reviews for hit or niche products? Journal of Management Information Systems, 27, 2 (2010), 127–158.

10. Dorner, V; Ivanova, O; and Scholz, M. Think Twice Before You Buy! How Recommendations Affect Three-Stage Purchase Decision Processes. ICIS 2013 Proceedings, 2013.

11. Dos Santos, Brian L; Zheng, Z; Mookerjee, V.S; and Chen, H. Are new IT-enabled investment opportunities diminishing for firms? Information Systems Research, 23, 2 (2012), 287–305.

12. Fama, E.F. Efficient Capital Markets: A Review of Theory and Empirical Work. The Journal of Finance, 25, 2 (1970), 383–417.

13. Fama, E.F; Fisher, L; Jensen, M.C; and Roll, R. The adjustment of stock prices to new information. International economic review, 10, 1 (1969), 1–21.

14. Filion, K. and Powell, D.A. The use of restaurant inspection disclosure systems as a means of communicating food safety information. Journal of Foodservice, 20, 6 (2009), 287–297.

15. Forman, C; Ghose, A; and Wiesenfeld, B. Examining the Relationship Between Reviews and Sales: The Role of Reviewer Identity Disclosure in Electronic Markets. Information Systems Research, 19, 3 (2008), 291–313.

16. Fuller, C.M; Biros, D.P; Burgoon, J; and Nunamaker, J. An examination and validation of linguistic constructs for studying high-stakes deception. Group Decision and Negotiation, 22, 1 (2013), 117–134.

17. Gao, G.G; Greenwood, B.N; Agarwal, R; and McCullough, J.S. Vocal minority and silent majority: How do online ratings reflect population perceptions of quality?. MIS Quarterly 39, 3, (2015), 565–589.

18. Goes, P.B; Lin, M; and Yeung, C.-m.A. “Popularity effect” in user-generated content: evidence from online product reviews. Information Systems Research, 25, 2 (2014), 222–238.

19. Groth, S.S; Siering, M; and Gomber, P. How to enable automated trading engines to cope with news-related liquidity shocks? extracting signals from unstructured data. Decision Support Systems, 62 (2014), 32–42.

20. Gunaratne, J; Zalmanson, L; and Nov, O. The persuasive power of algorithmic and crowdsourced advice. Journal of Management Information Systems, 35, 4 (2018), 1092–1120.

21. Guo, J; Zhang, W; Fan, W; and Li, W. Combining geographical and social influences with deep learning for personalized point-of-interest recommendation. Journal of Management Information Systems, 35, 4 (2018), 1121–1153.

22. Han, K; Oh, W; Im, K.S; Oh, H; Pinsonneault, A; and Chang, R.M. Value cocreation and wealth spillover in open innovation alliances. MIS Quarterly, 36, 1 (2012), 291–325.

23. Harrison, C; Jorder, M; Stern, H; Stavinsky, F; Reddy, V; Hanson, H; Waechter, H; Lowe, L; Gravano, L; and Balter, S. Using online reviews by restaurant patrons to identify unreported cases of foodborne illness—New York City, 2012–2013. MMWR, 63, 20 (2014), 441–445.

24. Henson, S; Majowicz, S; Masakure, O; Sockett, P; Jones, A; Hart, R; Carr, D; and Knowles, L. Consumer assessment of the safety of restaurants: The role of inspection notices and other information cues. Journal of food safety, 26, 4 (2006), 275–301.

25. Ho, Y.-C; Wu, J; and Tan, Y. Disconfirmation effect on online rating behavior: A structural model. Information Systems Research, 28, 3 (2017), 626–642.

26. Huang, Y; Li, C; Wu, J; and Lin, Z. Online customer reviews and consumer evaluation: The role of review font. Big Data Commerce, 55, 4 (2018), 430–440.

27. Im, K.S; Dow, K.E; and Grover, V. A reexamination of IT investment and the market value of the firm—An event study methodology. Information Systems Research, 12, 1 (2001), 103–117.

28. Ivanov, A. and Sharman, R. Impact of user-generated internet content on hospital reputational dynamics. Journal of Management Information Systems, 35, 4 (2018), 1277–1300.

29. Jensen, M.L; Averbeck, J.M; Zhang, Z; and Wright, K.B. Credibility of anonymous online product reviews: A language expectancy perspective. Journal of Management Information Systems, 30, 1 (2013), 293–324.

30. Jin, G.Z. and Leslie, P. The effect of information on product quality: Evidence from restaurant hygiene grade cards. The Quarterly Journal of Economics, 118, 2 (2003), 409–451.

31. Kang, J.S; Kuznetsova, P; Luca, M; and Choi, Y. Where not to eat? Improving public policy by predicting hygiene inspections using online reviews. Proceedings 2013 Conference Empirical Methods Natural Language Process, 2013 (2013), 1443–1448.

32. Kim, S.M; Pantel, P; Chklovski, T; and Pennacchiotti, M. Automatically assessing review helpfulness. Proceedings of the 2006 Conference on Empirical Methods in Natural Language Processing, 2006, pp. 423–430.

33. Knight, A.J; Worosz, M.R; and Todd, E.C.D. Dining for safety: Consumer perceptions of food safety and eating out. Journal of Hospitality & Tourism Research, 33, 4 (2009), 471–486.

34. Konchitchki, Y. and O’Leary, D.E. Event study methodologies in information systems research. International Journal of Accounting Information Systems, 12, 2 (2011), 99–115.

35. Kwark, Y; Chen, J; and Raghunathan, S. Online product reviews: Implications for retailers and competing manufacturers. Information Systems Research, 25, 1 (2014), 93–110.

36. Lappas, T; Sabnis, G; and Valkanas, G. The impact of fake reviews on online visibility: A vulnerability assessment of the hotel industry. Information Systems Research, 27, 4 (2016), 940–961.

37. Lewis, D.D; Yang, Y; Rose, T.G; and Li, F. Rcv1: A new benchmark collection for text categorization research. Journal of Machine Learning Research, 5, Apr (2004), 361–397.

38. Li, J; Ott, M; Cardie, C; and Hovy, E.H. Towards a General rule for identifying deceptive opinion spam. ACL (2014), 1566–1567.

39. Li, X. and Hitt, L.M. Self-selection and information role of online product reviews. Information Systems Research, 19, 4 (2008), 456–474.

40. Liang, T.-P. and Turban, E. Introduction to the special issue social commerce: A research framework for social commerce. International Journal of Electronic Commerce, 16, 2 (2011), 5–13.

41. Liu, Y; Jiang, C; and Zhao, H. Using contextual features and multi-view ensemble learning in product defect identification from online discussion forums. Decision Support System: Directions for the Nest Decade, 105 (2018), 1–12.

42. Lo, A.W. The adaptive markets hypothesis. The Journal of Portfolio Management, 30, 5 (2004), 15–29.

43. Lu, X; Ba, S; Huang, L; and Feng, Y. Promotional marketing or word-of-mouth? Evidence from online restaurant reviews. Information Systems Research, 24, 3 (2013), 596–612.

44. Luca, M. and Zervas, G. Fake it till you make it: Reputation, competition, and Yelp review fraud. Management Science, 62, 12 (2016), 3412–3427.

45. Ma, X; Khansa, L; Deng, Y; and Kim, S.S. Impact of prior reviews on the subsequent review process in reputation systems. Journal of Management Information Systems, 30, 3 (2013), 279–310.

46. MacKinlay, A.C. Event Studies in economics and finance. Journal of Economic Literature, 35, 1 (1997), 13–39.

47. McCornack, S.A. Information manipulation theory. Comm. Monographs, 59, 1 (1992), 1–16.

48. Mudambi, S.M. and Schuff, D. What makes a helpful online review? A study of customer reviews on amazon.com. MIS Quarterly, 34, 1 (2010), 185–200.

49. Neely, C.J; Weller, P.A; and Ulrich, J.M. The adaptive markets hypothesis: Evidence from the foreign exchange market. Journal of Financial and Quantitative Analysis, 44, 2 (2009), 467–488.

50. Pentina, I; Bailey, A.A; and Zhang, L. Exploring effects of source similarity, message valence, and receiver regulatory focus on yelp review persuasiveness and purchase intentions. Journal of Marketing Communications, 24, 2 (2018), 125–145.

51. Porter, M.F. An algorithm for suffix stripping. Program, 14, 3 (1980), 211–218.

52. Rangan, S. Earnings management and the performance of seasoned equity offerings. Journal of Financial Economics, 50, 1 (1998), 101–122.

53. Raschka, S. Python Machine Learning. Birmingham, UK: Packt Publishing Ltd, 2015.

54. Sadilek, A; Brennan, S; Kautz, H; and Silenzio, V. nEmesis: Which restaurants should you avoid today? First AAAI Conference on Human Computing and Crowdsourcing, 2013.

55. Sahoo, N; Dellarocas, C; and Srinivasan, S. The Impact of online product reviews on product returns. Information Systems Research, 29, 3 (2018), 723–738.

56. Siering, M; Deokar, A.V; and Janze, C. Disentangling consumer recommendations: Explaining and predicting airline recommendations based on online reviews. Decision Support Systems, 107 (2018), 52–63.

57. Siering, M; Muntermann, J; and Rajagopalan, B. Explaining and predicting online review helpfulness: The role of content and reviewer-related signals. Decision Support Systems, 108 (2018), 1–12.

58. Sparks, B.A. and Browning, V. The impact of online reviews on hotel booking intentions and perception of trust. Tourism Management, 32, 6 (2011), 1310–1323.

59. Sparks, B.A; Perkins, H.E; and Buckley, R. Online travel reviews as persuasive communication: The effects of content type, source, and certification logos on consumer behavior. Tourism Management, 39 (2013), 1–9.

60. Talwar, A; Jurca, R; and Faltings, B. Understanding user behavior in online feedback reporting. Proc. 8th ACM Conference on Electron. Commer. (ACM), 2007, pp. 134–142.

61. Wang, C; Zhang, X; and Hann, I.-H. Socially nudged: A quasi-experimental study of friends’ social influence in online product ratings. Information Systems Research, 29, 3 (2018), 641-–655.

62. Worsfold, D. Consumer information on hygiene inspections of food premises. Journal of Foodservice, 17, 1 (2006), 23–31.

63. Yang, S.-B; Lim, J.-H; Oh, W; Animesh, A; and Pinsonneault, A. Research note— Using real options to investigate the market value of virtual world businesses. Information Systems Research, 23, 3–part–2 (2012), 1011–1029.

64. Ye, Q; Law, R; Gu, B; and Chen, W. The influence of user-generated content on traveler behavior: An empirical investigation on the effects of e-word-of-mouth to hotel online bookings. Computers in Human Behavior, 27, 2 (2011), 634–639.

65. Yin, D; Bond, S.D; and Zhang, H. Anxious or angry? Effects of discrete emotions on the perceived helpfulness of online reviews. MIS Quarterly, 38, 2 (2014), 539–560.

66. Zhou, L; Burgoon, J.K; Nunamaker, J.F; and Twitchell, D. Automating linguistics-based cues for detecting deception in text-based asynchronous computer-mediated communications. Group Decision and Negotiation, 13, 1 (2004), 81–106.

67. Zhou, S; Qiao, Z; Du, Q; Wang, G.A; Fan, W; and Yan, X. Measuring customer agility from online reviews using big data text analytics. Journal of Management Information Systems, 35, 2 (2018), 510–539.

68. Zhu, F. and Zhang, X. Impact of online consumer reviews on sales: the moderating role of product and consumer characteristics. Journal of Marketing, 74, 2 (2010), 133–148.
