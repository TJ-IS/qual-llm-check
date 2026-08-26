---
otero_id: 1446
otero_key: "D95M2SQ5"
title: "The effect of user-controllable filters on the prediction of online hotel reviews"
authors: "Ya-Han Hu; Kuanchin Chen; Pei-Ju Lee"
year: "2017"
journal: "Information & Management"
doi: "10.1016/j.im.2016.12.009"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The effect of user-controllable <sup>fi</sup>lters on the prediction of online hotel reviews

Ya-Han Hu<sup>a</sup>, Kuanchin Chen<sup>b</sup>, Pei-Ju Lee<sup>c,</sup>\*

<sup>a</sup> Department of Information Management, National Chung Cheng University, Chiayi, 62102, Taiwan, ROC

<sup>b</sup> Department of Business Information Systems, Western Michigan University, 3344 Schneider Hall, Kalamazoo, MI 49008-5412, United States

<sup>c</sup> Department of Information Management, National Chung Cheng University, Chiayi, 62102, Taiwan, ROC

## A R T I C L E I N F O

Article history: Received 1 June 2016 Received in revised form 16 November 2016 Accepted 24 December 2016 Available online xxx

Keywords: Online hotel review Review helpfulness Sentiment analysis Review extremity Prediction Electronic word of mouth (eWOM)

## A B S T R A C T

Product reviews have gained much popularity in recent years. This study examines the theoretical foundation of review helpfulness and reports how the interactions among three user-controllable <sup>fi</sup>lters together with three groups of predictors affect review helpfulness. Reviews from TripAdvisor.com were analyzed against three analytical models. The results show that these groups of variables have a varying effect on different user-controllable <sup>fi</sup>lters. Review rating and number of words are key predictors of helpfulness across all three <sup>fi</sup>lters. The recency, frequency, and monetary (RFM) model has received a consistent support across all <sup>fi</sup>lters as well. Managerial implications are provided.

## 1. Introduction

© 2016 Elsevier B.V. All rights reserved.

With the rapid development of the Internet, online social media has become a popular platform for users to share their personal experiences. The shared information, termed user-generated content (UGC) in the academic literature, is the <sup>fi</sup>rst source of information for many people to make their decisions [1,2]. Of all types of UGC, online consumer reviews represent the majority for purchase decisions. Online review websites are a major channel of communication that provides valuable information to consumers [3,4]. These websites also tap into online reviews for the opportunity of promotions, customer service, and other revenue-generating activities [5]. Studies have shown that travel websites greatly in<sup>fl</sup>uence the tourism industry; 62% of travelers search the Internet for their upcoming travel activities and 43% of visitors read online reviews written by other travelers [6–9].

Although the growth in the volume of online hotel reviews is a welcomed trend for consumers, it also likely causes information overload for those who wish to meaningfully use it. Travelers must manually <sup>fi</sup>lter helpful reviews on travel websites, which considerably increases the search cost to locate hotel reviews helpful to meet their goals. This is the reason many product websites offer review helpfulness to help readers sort through a sea of reviews. Hotel reviews are not an exception. Most hotel review websites also provide some form of helpfulness indicators as well. Assessment of helpful reviews is, therefore, an important and essential task for consumers [10–12]. Review helpfulness typically refers to the total number or percentage of positive votes a product review has received; it represents a consumer’s analysis of how the review matches the expectations for the trip in mind [13].

Online tourism websites with more helpful reviews can provide more valuable information to potential customers. Therefore, the development of an automatic review evaluation system to identify high-quality reviews on tourism websites can both reduce the search time for a consumer to locate the desired information, and facilitate the creation of diversi<sup>fi</sup>ed services compared with those of the existing websites. Therefore, online review helpfulness has become a key variable of interest in the product review literature that spans across multiple disciplines.

Mudambi and Schuff [12] were among the <sup>fi</sup>rst to provide a theoretically grounded explanation of review helpfulness. They concluded with a model where the construct relationships vary between search goods and experience goods. Therefore, the requirements for a review to be considered helpful are not quite the same between the two types of goods. This is consistent with the literature where experience goods are de<sup>fi</sup>ned as goods that require consumers to sample or “experience” the product before formulating their own quality assessment, but quality assessment could be conducted for search goods before they are even purchased [14]. Similarly, readers of hotel reviews expect to learn from other people’s experience with the hotel, which makes hotels an experience good. Although Mudambi and Schuff’s model that predicts helpfulness with review rating, word count, and total votes are a great foundation model, it was not speci<sup>fi</sup>cally designed for experience goods or more speci<sup>fi</sup>cally for hotel reviews.

In fact, their theoretical basis of review helpfulness was information diagnosticity from Jiang and Benbasat [15] and others, which suggest that diagnosticity is highly desired when the salient product attributes are better assessed through experiences. Additionally, the accessibility–diagnosticity model indicates that “accessible information is not used as an input for judgement and choice when more diagnostic or probative information is available” ([16] Herr et al., 1991; p. 457). Therefore, factors in addition to review rating, word count, and total votes are also cues to enrich Mudambi and Schuff’s model for hotel reviews.

Moreover, studies of product reviews have traditionally focused on searching for an optimal set of predictors of review helpfulness, but neglecting the fact that even the predictors may interact with each other. For example, climate and seasonal shifts may affect tourism demand [17–21], which points to a possible interaction between travel season and geographic location of hotels. This is the reason several travel websites have offered <sup>fi</sup>lters of hotel reviews based on these characteristics. Because of the availability of these <sup>fi</sup>lters, the visibility of a review may be altered through the selection of a <sup>fi</sup>lter. In the end, it affects a review’s opportunity to be voted on for review helpfulness [11]. If interactions among predictor variables are not accommodated in a theoretical model for hotel reviews, the predictive power or even the accuracy of the model may be hampered.

Based on the above assessment, the present study is designed with the following objectives:

1. To enrich the theoretical model of Mudambi and Schuff with additional predictor variables from the relevant literature.

2. To provide empirical evidence of interaction effects for the common <sup>fi</sup>lters of hotel reviews (i.e., travel regions, travel seasons, and travel types on review helpfulness).

3. To improve the performance of review helpfulness prediction models by considering the above two objectives.

## 2. Related work

## 2.1. Factors affecting review helpfulness

Table 1 summarizes the predictors of review helpfulness from the literature. The predictors used in these studies can be divided into the following three categories: review quality (i.e., review content and review readability), review polarity (i.e., review sentiment and review subjectivity), and reviewer (i.e., reviewer characteristics and RFM (recency, frequency, and monetary) features). Such a classi<sup>fi</sup>cation is rooted in both the diagnosticity and electronic word-of-mouth (eWOM) literatures. For example, Wang et al.’s [49] <sup>fi</sup>nding of informant credibility supports that the characteristics of the information provider (i.e., product reviewer) are related to acceptance of a product. Similarly, Li et al. [50] also

Table 1  
Previous studies on review helpfulness.

<table><tr><td rowspan="2">Work</td><td rowspan="2">Data source</td><td rowspan="2">Search (S)/Experience (E) goods</td><td colspan="2">Review quality</td><td colspan="2">Review polarity</td><td colspan="2">Reviewer</td></tr><tr><td>Review content</td><td>Readability</td><td>Sentiment</td><td>Subjectivity</td><td>Reviewer characteristics</td><td>RFM</td></tr><tr><td>Kim et al. [22]</td><td>Amazon</td><td>S/E</td><td>✓</td><td></td><td>✓</td><td></td><td></td><td></td></tr><tr><td>Liu et al. [23]</td><td>Amazon</td><td>S</td><td>✓</td><td>✓</td><td>✓</td><td></td><td></td><td></td></tr><tr><td>Forman et al. [24]</td><td>Amazon</td><td>E</td><td>✓</td><td>✓</td><td></td><td>✓</td><td></td><td></td></tr><tr><td>Zhang [25]</td><td>Amazon</td><td>S/E</td><td>✓</td><td></td><td></td><td>✓</td><td></td><td></td></tr><tr><td>Liu et al. [26]</td><td>IMDB</td><td>E</td><td>✓</td><td></td><td></td><td></td><td>✓</td><td></td></tr><tr><td>Otterbacher [27]</td><td>Amazon</td><td>S/E</td><td>✓</td><td></td><td></td><td></td><td>✓</td><td></td></tr><tr><td>O&#x27;Mahony and Smyth [28]</td><td>TripAdvisor</td><td>E</td><td>✓</td><td></td><td></td><td></td><td>✓</td><td></td></tr><tr><td>Mudambi and Schuff [12]</td><td>Amazon</td><td>S/E</td><td>✓</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Chen and Tseng [29]</td><td>Amazon</td><td>S</td><td>✓</td><td></td><td>✓</td><td></td><td>✓</td><td></td></tr><tr><td>Ghose and Ipeirotis [30]</td><td>Amazon</td><td>S/E</td><td>✓</td><td>✓</td><td></td><td>✓</td><td>✓</td><td></td></tr><tr><td>Yu et al. [31]</td><td>IMDB</td><td>E</td><td>✓</td><td></td><td>✓</td><td></td><td></td><td></td></tr><tr><td>Ngo-Ye and Sinha [32]</td><td>Amazon</td><td>E</td><td>✓</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Liu et al. [33]</td><td>Amazon</td><td>S</td><td>✓</td><td></td><td>✓</td><td>✓</td><td></td><td></td></tr><tr><td>Dong et al. [34]</td><td>Amazon</td><td>S</td><td>✓</td><td>✓</td><td>✓</td><td></td><td></td><td></td></tr><tr><td>Ngo-Ye and Sinha [35]</td><td>Amazon/Yelp</td><td>E</td><td>✓</td><td></td><td></td><td></td><td></td><td>✓</td></tr><tr><td></td><td></td><td>E</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Hu et al. [36]</td><td>Amazon</td><td>E</td><td>✓</td><td></td><td>✓</td><td></td><td></td><td></td></tr><tr><td>Hwang et al. [37]</td><td>TripAdvisor</td><td>E</td><td>✓</td><td></td><td>✓</td><td></td><td></td><td></td></tr><tr><td>Yin et al. [38]</td><td>Yelp</td><td>E</td><td>✓</td><td></td><td></td><td></td><td>✓</td><td></td></tr><tr><td>Lee and Choeh [39]</td><td>Amazon</td><td>S</td><td>✓</td><td></td><td></td><td></td><td>✓</td><td></td></tr><tr><td>Martin and Pu [40]</td><td>Amazon/Yelp/TripAdvisor</td><td>S</td><td>✓</td><td>✓</td><td>✓</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>E</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>E</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Zhu et al. [41]</td><td>Yelp</td><td>E</td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td><td></td></tr><tr><td>Liu and Park [42]</td><td>Yelp</td><td>E</td><td></td><td>✓</td><td></td><td></td><td>✓</td><td></td></tr><tr><td>Weathers et al. [43]</td><td>Amazon</td><td>S/E</td><td>✓</td><td></td><td></td><td></td><td>✓</td><td></td></tr><tr><td>Huang et al. [44]</td><td>Amazon</td><td>S</td><td>✓</td><td></td><td></td><td></td><td>✓</td><td></td></tr><tr><td>Ahmad and Laroche [45]</td><td>Amazon</td><td>S</td><td>✓</td><td></td><td>✓</td><td></td><td></td><td></td></tr><tr><td>Chua and Banerjee [46]</td><td>Amazon</td><td>S/E</td><td>✓</td><td>✓</td><td></td><td></td><td></td><td></td></tr><tr><td>Fang et al. [47]</td><td>TripAdvisor</td><td>E</td><td>✓</td><td>✓</td><td>✓</td><td></td><td>✓</td><td></td></tr><tr><td>Hu and Chen [11]</td><td>TripAdvisor</td><td>E</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td></td></tr><tr><td>Qazi et al. [48]</td><td>TripAdvisor</td><td>E</td><td>✓</td><td></td><td>✓</td><td>✓</td><td>✓</td><td></td></tr></table>

Please cite this article in press as: Y.-H. Hu, et al., The effect of user-controllable <sup>fi</sup>lters on the prediction of online hotel reviews, Inf. Manage. (2017), http://dx.doi.org/10.1016/j.im.2016.12.009

indicate that source credibility, product review content, and authorship are key predictors for product review helpfulness.

Review quality directly affects review helpfulness; previous studies have explored the in<sup>fl</sup>uence of review content on review helpfulness from different aspects, including the length of the review, review structure, readability, and writing style. Moreover, sentiment analysis has become a popular research topic and is widely used in online review analysis. Sentiment analysis determines consumers’ sentiment polarity (i.e., positive, negative, or neutral sentiment) according to consumers’ reviews of products or service experiences. Many studies have also explored the relationship between sentiment strength and review helpfulness [12,51]. In addition, evidence suggests that reviewer characteristics (such as reviewer reputation) affect review helpfulness [27,48,52,53]. Details of individual categories of these predictors are presented in the following sections.

## 2.1.1. Review quality

A review with adequate readability is considered to be more helpful to users than a review that is dif<sup>fi</sup>cult to read and contains numerous typographical errors. However, although many reviewers are not concerned about spelling accuracy when writing online reviews, their spelling errors may cause dif<sup>fi</sup>culties when reading. Kim et al. [22] considered three types of features, namely term frequency–inverse document frequency (TF–IDF) scores, review length, and review readability, for explaining review helpfulness. Forman et al. [24] revealed that review readability has a positive effect on review helpfulness and that spelling errors have a negative effect on review helpfulness.

## 2.1.2. Review polarity

Sentiment analysis has become a popular research topic in recent years; many studies have been investigated on the relationship between sentiment strength and review helpfulness using different review data sets [51,54,55,56]. Hu et al. [36] explored the relationship between evaluation, sentiment, and sales amount through 4405 book reviews on Amazon.com; the results revealed that sentiment features affect the overall sales signi<sup>fi</sup>cantly. Mudambi and Schuff [12] analyzed 1587 reviews of consumer electronics on Amazon.com and reported that sentiment strength strongly affects review helpfulness, particularly for search goods. Ghose and Ipeirotis [30] learned from product reviews on Amazon.com that subjectivity, informativeness, readability, and linguistic correctness of reviews can signi<sup>fi</sup>cantly affect review helpfulness. They also reported that reviews containing a mix of subjective and objective statements were considered more helpful to users. The information-quality framework was used by Chen and Tseng [29] to evaluate the quality of product reviews. They concluded that high-quality reviews tend to be extremely subjective. Furthermore, Cao et al. [53] suggested that the stronger the sentiment polarity of reviews, the higher is the chance of them being considered helpful for consumers. In addition, semantic features are more critical than the basic stylistic characteristics. In semantic element selection, Kor<sup>fi</sup>atis et al. [57] demonstrated that the sentiment feature has a stronger in<sup>fl</sup>uence than the length of reviews. Chua and Banerjee [46] considered review helpfulness as a ratio of the number of helpful votes over the total number of votes; they de<sup>fi</sup>ned review sentiment as favorable or unfavorable and in<sup>fl</sup>uenced by review star ratings, which affect review helpfulness according to product type. Review star rating is positively related to more favorable reviews. Ahmad and Laroche [45] further divided the review sentiment into positive and negative; they con<sup>fi</sup>rmed that reviews using stronger sentiment words are considered to more greatly affect review helpfulness (i.e., positive or negative words have a positive or negative effect on review helpfulness) than reviews with vague or neutral words.

## 2.1.3. Reviewer

On most social media websites, reviewers’ personal information is available to users for reference. Previous studies have noted that consumers tend to believe the helpfulness of a review when travel websites incorporate the information of reviewer identity and personal characteristics in the review [42,52,58,13]. Accurately identifying reviewers with greater reputations is essential for consumers when deciding which review to believe. [13] Hu et al. suggested that consumers consider evaluation scores, reviewer reputation, and the number of past reviews of reviewers. Reviews written by reputed reviewers or by reviewers who have written extensive reviews on the social media websites are more prominent. Otterbacher [27] studied product reviews on Amazon.com and used the total votes, badge type, and website rankings of the reviewer to evaluate reviewer reputation.

Other studies have also revealed that the past average votes of the reviewer can be used to predict review helpfulness [47]. Qazi et al. [48] also addressed that the qualitative factors of reviewers, such as review type and cumulative helpfulness, are as equally critical as the quantitative factors, such as the number of concepts. Although the qualitative factor such as the length of the review has a diminishing effect on review helpfulness when the review length exceeds 144 characters, other qualitative factors remain in<sup>fl</sup>uential [44]. The combination of reviews and reviewers provides a more complete explanation of review helpfulness to consumers [42]. Weathers et al. [43] considered three factors—reviewer credibility, review diagnosticity, and product type—and concluded that review credibility refers to reviewer characteristics (e.g., trustworthiness and expertise) and review diagnosticity refers to review quality (e.g., uncertainty and equivocality).

Past studies have shown that gender and age affect how consumers react to online reviews. Females and younger people had higher intention to engage in eWOM. For example, the egeneration is immersed in technology growing up. The pervasiveness of personal technology has made them more open and comfortable to electronic communications. Moreover, there is also a gender difference in their interest in review content and preference over stylistic choices [58,59]. Therefore, the metadata such as gender and age of reviewers are also collected; these factors provide the background knowledge of reviewers that helps us to pro<sup>fi</sup>le these reviewers, and address the impact on population [27,60,61].

The RFM model is a valuable tool for measuring the values of customers, and it aims to predict consumers’ future purchasing according to their past transactions [62]. This model functions by combining the three indicators (i.e., recency, frequency, and monetary values) of consumers; these indicators describe reviewers who have recently made a transaction, purchase frequently, and, on average, spend more money. The RFM model combines the three indicators, groups consumers according to their behaviors, and provides different marketing strategies for distinct consumer groups [63,64]. This model has been widely used in direct marketing, such as in sending direct messages and emails.

Ngo-Ye and Sinha [32] were the <sup>fi</sup>rst to apply the RFM model to evaluate the effect of reviewer engagement on review helpfulness prediction. The authors collected reviews from Yelp.com and Amazon.com and considered both textual (i.e., bag-of-words method) and RFM features of the reviews. Their results con<sup>fi</sup>rmed that the variables in the RFM model provide a strong explanation of review helpfulness.

## 2.2. Previous studies on hotel review helpfulness

Although many studies have addressed online review helpfulness, few have focused on online hotel reviews. O’Mahony and

Smyth [28] collected reviews of Las Vegas and Chicago hotels on TripAdvisor.com. They de<sup>fi</sup>ned helpful reviews as those that received more than 75% positive feedback votes of all votes. They considered reviewer reputation, content, social, and sentiment features as independent variables (IVs). Their experimental results indicated that reviewer reputation is the predictor for classi<sup>fi</sup>ers to achieve favorable predictive ability.

Ghoses et al. [10] developed a hotel recommendation system that considered consumer heterogeneity, hotel characteristics, purchasing history, and online hotel reviews for hotel evaluation. Their results revealed that the readability and subjective features of hotel reviews can be used to predict review helpfulness effectively.

Hwang et al. [37] collected 3124 reviews of Taiwan hotels from TripAdvisor.com and divided the reviews into two categories (i.e., helpful/not helpful) according to two hotel managers. They considered three types of features—content, sentiment, and review quality—and applied three types of methods (i.e., TF–IDF, topic model-based latent Dirichlet allocation (LDA), and semantic-based LDA) in the selection of IVs. The results con<sup>fi</sup>rmed that the three content features are major predictors and the topic model-based LDA provided the most favorable performance in the predictive model.

Yin et al. [38] collected 16,269 reviews of 307 San Francisco hotels from Yelp.com. They de<sup>fi</sup>ned review helpfulness as the total number of helpful votes received by a review and determined the sentiment features by matching review contents with the sentiment lexicon (i.e., using the revised Dictionary of Affect in Language). In addition, their study considered other features, such as the review ratings, review length, reviewer characteristics, and hotel information in experimental evaluation. The results indicated that review sentiment, review length, and reviewer characteristic features can be critical factors in predicting review helpfulness.

Zhu et al. [41] also accumulated hotel reviews from Yelp.com and provided a de<sup>fi</sup>nition of review helpfulness identical to that of Yin et al. [38]. The main objective of Zhu et al. [41] was to investigate the relationship between reviewer credibility and review helpfulness and to examine the moderation effects of review extremity and hotel price. A total of 16,265 hotel reviews were collected. Two independent variables (i.e., reviewer expertise and online attractiveness) were selected, and several review and hotel features were used as control variables in their study. The results indicated that opinion leaders do not necessarily receive higher helpful votes; the effects of both reviewer expertise and online attractiveness were moderated by hotel price.

Hu and Chen [11] examined the interaction effects of star-class hotels and review ratings on review helpfulness prediction. They con<sup>fi</sup>rmed that users are likely to read the reviews when their review rating does not correspond with users’ expectations on star-class hotels and, therefore, the likelihood of these reviews being voted is increased. Hu and Chen [11] collected 349,582 reviews of 450 hotels in Orlando or Las Vegas from TripAdvisor. com and considered four types of features: review content, review sentiment, review author, and review visibility. The results revealed that review visibility has a strong effect on review helpfulness.

In summary, the abovementioned studies have shown that the review quality, review polarity, and reviewer characteristics are important factors to predict hotel review helpfulness, which also provide some evidences that review diagnosticity, review quality, and reviewer credibility signi<sup>fi</sup>cantly affect review helpfulness of experience goods. However, most of these studies overly focus on only locating the best set of predictors, neglecting a possibility for interaction among the predictors. Consequently, the predictive power of the resulting model may be inaccurate or biased. In addition, user-controllable <sup>fi</sup>lters (i.e., travel region, travel season, and travel type) may arti<sup>fi</sup>cially alter the visibility of reviews, thereby affecting their opportunities to be voted on for helpfulness. Such dynamics have received very little attention in the literature.

## 3. Research method

Fig. 1 illustrates the research process. The hotel reviews were collected from TripAdvisor.com. The preprocess procedures, including review length calculations, word and sentence segmentation, and part-of-speech (POS) tagging, were performed. A total of 39 features, including one dependent variable (DV) and 38 IVs,

![](/api/attachments/D95M2SQ5/fulltext/images/979a2b7597557ab38485b69414286ce482f01631fef45e1af3aa9a43474ec536.jpg)  
Fig. 1. Research process.

Please cite this article in press as: Y.-H. Hu, et al., The effect of user-controllable <sup>fi</sup>lters on the prediction of online hotel reviews, Inf. Manage. (2017), http://dx.doi.org/10.1016/j.im.2016.12.009

were considered. The DV was review helpfulness, which is de<sup>fi</sup>ned as follows:

$$
\text { Reviewhelpfulness } _ {i} = \frac {\text { HelpfulVotes } _ {i}}{\text { Elapsed } _ {\text { Month } _ {i}}}\tag{1}
$$

where HelpfulVotes is the number of votes the review i has received for its helpfulness, $\mathtt { E l a p s e d } _ { \mathrm { M o n t h } _ { i } }$ is the number of months since review i has been posted, that is, the difference between the date of review posted and the date the review was crawled. Usually, the longer a review has been posted, the more likely it will receive helpfulness votes. Dividing helpfulness votes by elapsed time will reduce the effect of systematic bias due to this abovereview longevity issue. Previous research [41] has also shown that elapsed time is related to review helpfulness.

The IVs were divided into the following categories: review quality, review polarity, and reviewer features. Three supervised learning techniques were used for developing prediction models, namely linear regression (LR), reduced error-pruning tree (REPtree), and random forest (RF).

## 3.1. Review collection and preprocessing

The present study collected complete sets of hotel reviews of <sup>fi</sup>ve famous travel destinations in the United States—New York City, Las Vegas, Chicago, Orlando, and Miami—from TripAdvisor.com. According to the data on the Travelers’ Choice of 2015 provided by TripAdvisor.com, the selected <sup>fi</sup>ve cities were voted by millions of travelers as the top <sup>fi</sup>ve most popular travel destinations in the United States; they were also listed as the top <sup>fi</sup>ve cities in the 2016U.S. Place Equity Index Resonance Report. The complete sets of hotel reviews of the <sup>fi</sup>ve cities were collected between June 1, 2012, and May 31, 2015. Before retrieving the features from the reviews, several data-<sup>fi</sup>ltering tasks were performed. First, to simplify the analysis, we collected reviews written only in English. Second, because this study investigated the interaction effects of review region, review season, and travel type on review helpfulness, the reviews without such information (i.e., missing data) were removed; the selected <sup>fi</sup>ve cities were also grouped according to three travel regions: north (New York City/Chicago), south (Miami/Orlando), and west (Las Vegas) regions. Consequently, the descriptive statistics of the selected hotel reviews of the <sup>fi</sup>ve cities are presented in Table 2.

The content of each review comprised review rating, review title, review content, reviewer information, number of helpful votes, and the date the review was posted. Before extracting review features from the review content, several preprocessing tasks were performed. First, we used Google’s spell-check function to rectify spelling errors in the collected reviews. We used Stanford CoreNLP for other preprocessing tasks such as word and sentence segmentation as well as POS tagging [65]. After segmentation, the POS tagging was assigned to each word according to the meaning of adjacent words in the same sentence; the tags included those for nouns (N), adjectives (JJ), or adverbs (RB).

Table 2  
Hotel review data sets from TripAdvisor.com.

<table><tr><td>Region</td><td>City</td><td># of Hotels</td><td># of Reviewers</td><td># of Reviews</td></tr><tr><td rowspan="2">North</td><td>New York City</td><td>401</td><td>200,313</td><td>227,931</td></tr><tr><td>Chicago</td><td>147</td><td>71,116</td><td>79,436</td></tr><tr><td rowspan="2">South</td><td>Miami</td><td>96</td><td>25,942</td><td>28,197</td></tr><tr><td>Orlando</td><td>301</td><td>125,783</td><td>147,179</td></tr><tr><td rowspan="2">West</td><td>Las Vegas</td><td>213</td><td>198,740</td><td>234,259</td></tr><tr><td>Total</td><td>1158</td><td>621,894</td><td>717,002</td></tr></table>

## 3.2. Selected review features

Table 3 details the investigated research variables and their de<sup>fi</sup>nitions. On the basis of previous studies on review helpfulness, this study considered three types of IVs: review quality, review polarity, and reviewer.

## 3.2.1. Review quality

The information contained in each review includes review rating, the date the review was posted, review title, reviewer information, and the number of helpful votes. We collected the overall ratings of hotels from every review (RATING), ranging from 1 (extremely negative) to 5 (extremely positive). To estimate the required education level for the reader to comprehend the review (i.e., content readability), we analyzed the total length and the average length of every review with different units in characters, syllables, words, and sentences. On the basis of the collected hotel reviews, variables associated with the review length were considered, which include the number of characters (LENGTH\_- CHAR), the number of syllables (LENGTH\_SYLL), the number of words (LENGTH\_WORD), the number of sentences (LENGTH\_- SENT), the average number of syllables per word (SYLL\_PER\_- WORD), and the average number of words per sentence (WORD\_PER\_SENT).

Some studies have indicated that readers’ reading abilities and speeds increase with an increase in review readability [30,40]. Content readability is estimated through various measurements; in most cases, researchers calculate content readability according to the corresponding education level. To prevent the bias of using a single measurement, we calculated a set of readability indices for each review, including the Automated Readability Index (ARI) [66], Coleman–Liau Index (CLI) [67], Flesch Reading Ease Scale (FRES) [68], Flesch–Kincaid Grade Level (FGL) [68], Gunning Fog Index (FOG) [69], and Simple Measure of Gobbledygook (SMOG) [70]. For more information on these readability indices, please refer to [11].

In addition to the aforementioned content features, the subjectivity of each review was also analyzed. This study adopted Opinion<sup>fi</sup>nder [71,72], one of the most widely used text-mining tools, to identify subjective sentences from texts automatically. Opinion<sup>fi</sup>nder uses a classi<sup>fi</sup>er trained with machine-learning methods. On the basis of the extracted sentences in reviews, subjective analysis can be performed. The results identify more subjects when the number of subjective sentences in the review is higher. The degree of subjectivity (SUBJECTIVITY) can be de<sup>fi</sup>ned as the ratio of the number of subjective sentences to the total number of sentences in the review (Eq. (2))

$$
\text {   SUBJECTIVITY   } = \frac {\text {   Sub   }}{\text {   Sentence   }}\tag{2}
$$

where Sub denotes the number of subjective sentences in the review and Sentence denotes the total number of sentences after punctuation.

## 3.2.2. Review sentiment

In addition to the subjectivity analysis, Opinion<sup>fi</sup>nder can also perform unsupervised sentiment analysis. The review texts were separated into sentences according to punctuation marks automatically. Each word was assigned a POS tag, such as nouns (N), adjectives (JJ), or adverbs (RB). Thereafter, polarity classi<sup>fi</sup>ers were used to identify the word polarity for each word. The types of review polarity were strong positive (STR\_POS), strong negative (STR\_NEG), strong sentiment (STR\_SENTI), weak sentiment (WEAK\_SENTI), weak positive (WEAK\_POS), and weak negative (WEAK\_NEG). This study calculated the scores of each type of word

6

Table 3 List of IVs.

Y.-H. Hu et al. / Information & Management xxx (2016) xxx–xxx

<table><tr><td>Variable category</td><td>Variable Name</td><td>Description</td><td>Type (value/range)</td></tr><tr><td rowspan="13">Review Quality</td><td>RATING</td><td>Review rating</td><td>Numeric (1-5)</td></tr><tr><td>LENGTH_CHAR</td><td>Number of characters</td><td>Numeric</td></tr><tr><td>LENGTH_SYLL</td><td>Number of syllables</td><td>Numeric</td></tr><tr><td>LENGTH_WORD</td><td>Number of words</td><td>Numeric</td></tr><tr><td>LENGTH_SENT</td><td>Number of sentences</td><td>Numeric</td></tr><tr><td>SYLL_PER_WORD</td><td>Average number of syllables per word</td><td>Numeric</td></tr><tr><td>WORD_PER_SENT</td><td>Average number of words per sentence</td><td>Numeric</td></tr><tr><td>ARI</td><td>Automated Readability Index</td><td>Numeric</td></tr><tr><td>CLI</td><td>Coleman-Liau Index</td><td>Numeric</td></tr><tr><td>FRES</td><td>Flesch Reading Ease Scale</td><td>Numeric</td></tr><tr><td>FGL</td><td>Flesch-Kincaid Grade Level</td><td>Numeric</td></tr><tr><td>FOG</td><td>Gunning Fog Index</td><td>Numeric</td></tr><tr><td>SMOG</td><td>Simple Measure of Gobbledygook</td><td>Numeric</td></tr><tr><td rowspan="15">Review polarity</td><td>SUBJECTIVITY</td><td>Number of subjective sentences/Number of sentences</td><td>Numeric</td></tr><tr><td>STR_POS</td><td>Strong positive score</td><td>Numeric</td></tr><tr><td>STR_NEG</td><td>Strong negative score</td><td>Numeric</td></tr><tr><td>WEAK_POS</td><td>Weak positive score</td><td>Numeric</td></tr><tr><td>WEAK_NEG</td><td>Weak negative score</td><td>Numeric</td></tr><tr><td>STR_SENTI</td><td>Strong sentiment score</td><td>Numeric</td></tr><tr><td>WEAK_SENTI</td><td>Weak sentiment score</td><td>Numeric</td></tr><tr><td>N_SENTI_SCORE</td><td>Overall sentiment score</td><td>Numeric</td></tr><tr><td>N_SENTI_CLASS</td><td>Unsupervised sentiment class</td><td>Nominal (Negative/Neutral/Positive)</td></tr><tr><td>S_SENTI_CLASS</td><td>Supervised sentiment class</td><td>Nominal (Negative/Neutral/Positive)</td></tr><tr><td>STANFORD_VERYNEG</td><td>Strong negative score calculated by Stanford CoreNLP</td><td>Numeric</td></tr><tr><td>STANFORD_NEG</td><td>Negative score calculated by Stanford CoreNLP</td><td>Numeric</td></tr><tr><td>STANFORD_NEUTRAL</td><td>Neutral score calculated by Stanford CoreNLP</td><td>Numeric</td></tr><tr><td>STANFORD_POS</td><td>Positive score calculated by Stanford CoreNLP</td><td>Numeric</td></tr><tr><td>STANFORD_VERYPOS</td><td>Strong positive score calculated by Stanford CoreNLP</td><td>Numeric</td></tr><tr><td rowspan="10">Reviewer</td><td>REVIEWER_LEVEL</td><td>Reviewer level</td><td>Nominal (NA/NewReviewer/Reviewer/Senior Reviewer/Contributor/Senior Contributor/TopContributor)</td></tr><tr><td>REVIEWER_SEX</td><td>Reviewer gender</td><td>Nominal (NA/Male/Female)</td></tr><tr><td>REVIEWER_AGE</td><td>Reviewer age</td><td>Nominal (NA/13-17 years old/18-24 years old/25-34 years old/35-49 years old/50-64 years old/above 65 years old)</td></tr><tr><td>JOIN_MONTHS</td><td>Number of months the reviewer has joined TripAdvisor.com</td><td>Numeric</td></tr><tr><td>NUM_PAST_REVIEW</td><td>Total number of past reviews</td><td>Numeric</td></tr><tr><td>NUM_PAST_HOTEL</td><td>Total number of hotels the reviewer has reviewed</td><td>Numeric</td></tr><tr><td>NUM_PAST_VOTE</td><td>Total number of past votes</td><td>Numeric</td></tr><tr><td>RECENCY</td><td>Recency score</td><td>Numeric</td></tr><tr><td>FREQUENCY</td><td>Frequency score</td><td>Numeric</td></tr><tr><td>MONETARY</td><td>Monetary score</td><td>Numeric</td></tr></table>

in every review and the IVs related to review sentiment, as follows:

Strongsubjpostivesentimentscor $\mathbf { \sigma } : ( \mathrm { S T R } _ { \mathrm { P O S } } ) = \frac { \mathbf { \sigma } \mathrm { S t r } _ { \mathrm { p o s } _ { i } } } { \mathbf { \sigma } \mathrm { S e n t i } _ { \mathrm { t o t } _ { i } } }$

ð<sup>3</sup>Þ

ð<sup>7</sup>Þ

Strongsubjnegativesentimentscore $( \mathrm { S T R } _ { \mathrm { N E G } } ) = \frac { \mathsf { s t r } _ { \mathrm { n e g } _ { i } } } { \mathsf { s e n t i } _ { \mathrm { t o t } _ { i } } }$

ð<sup>4</sup>Þ

Weaksubjpostivesentimentscore $\langle \mathrm { W E A K } _ { \mathrm { P O S } } \rangle = \frac { \mathsf { W e a k } _ { \mathrm { p o s } _ { i } } } { \mathsf { s e n t i } _ { \mathrm { t o t } _ { i } } }$

$$
\text { Weaksubjnegativesentimentscore } \left(\mathrm{WEAK} _ {\mathrm{NEG}}\right) = \frac {\text { weak } _ {\mathrm{neg} _ {i}}}{\text { senti } _ {\mathrm{tot} i}}
$$

$$
\text { S   t   r   o   n   g   s   u   b   j   s   e   n   t   i   m   e   n   t   s   c   o   r   e } \left(\mathrm{STR} _ {\text { S   E   N   T   I }}\right) = \frac {\left(\mathrm{str} _ {\text { p   o   s } _ {i}} + \mathrm{str} _ {\text { n   e   g } _ {i}}\right)}{\text { s   e   n   t   i } _ {\text { t   o   t } i}}\tag{8}
$$

ð<sup>5</sup>Þ

$$
\begin{array}{r l} \text { Weaksubjsentimentscore(WEAK} _ {\text { SENTI }} & = \frac {\left(\text { weak } _ {\text { pos } _ {i}} + \text { weak } _ {\text { neg } _ {i}}\right)}{\text { senti } _ {\text { tot } i}} \end{array}\tag{6}
$$

$$
\text { Overallsentimentscore } (N _ {\text { SENTI }} \text { SCORE })
$$

$$
= \left(\operatorname{str} _ {\text { pos } _ {i}} * 2 + \operatorname{weak} _ {\text { pos } _ {i}}\right) - \left(\operatorname{str} _ {\text { neg } _ {i}} * 2 + \operatorname{weak} _ {\text { neg } _ {i}}\right)\tag{9}
$$

where $\mathsf { s t r } _ { \mathsf { p o s } _ { i } }$ denotes the number of times strong positive words appeared in review i, $\mathsf { s t r } _ { \mathrm { n e g } _ { i } }$ denotes the number of times strong

Please cite this article in press as: Y.-H. Hu, et al., The effect of user-controllable <sup>fi</sup>lters on the prediction of online hotel reviews, Inf. Manage. (2017), http://dx.doi.org/10.1016/j.im.2016.12.009

negative words appeared, $\boldsymbol { \mathrm { w e a k } } _ { \mathrm { p o s } _ { i } }$ denotes the number of times weak positive words appeared, $\mathbf { w e a k } _ { \mathrm { n e g } _ { i } }$ denotes the number of times weak negative words appeared, and $\Pi _ { \mathrm { s e n t i } } S \mathrm { c o r e } _ { \mathrm { t o t } i }$ denotes the summation of $\mathsf { s t r \_ p o s } _ { i } ,$ str\_neg , weak\_pos , and weak\_neg .

This study also employed Stanford CoreNLP for supervised learning-based sentiment analysis. Previous studies have demonstrated that Stanford CoreNLP has high sentiment classi<sup>fi</sup>cation accuracy. Unlike the traditional bag-of-words model, this algorithm <sup>fi</sup>rst identi<sup>fi</sup>es the relationship between words through syntax analysis automatically and then obtains the results of the syntax tree. We used the Stanford Sentiment Treebank corpus, which contains 11,855 sentences and 215,154 short sentences.

The supervised sentiment variable of review i, denoted as S\_SENTI\_CLASS , was determined through the following process: the algorithm generated the <sup>fi</sup>ve sentiment categories through the aforementioned method and then calculated individual sentiment score according to the ratio of these <sup>fi</sup>ve categories of review i. The review was classi<sup>fi</sup>ed as positive if the result was greater than 0 (STANFORD\_VERYPOS and STANFORD\_POS), neutral if the result equaled 0 (STANFORD\_NEUTRAL), and negative if the result was less than 0 (STANFORD\_VERYNEG and STANFORD\_NEG).

## 3.2.3. Reviewer characteristics

This study considered the following reviewer features to evaluate review helpfulness, in addition to using text characteristics: the contribution of a reviewer to TripAdvisor.com (REVIE-WER\_LEVEL), the gender of the reviewer (REVIEWER\_SEX), the age of the reviewer (REVIEWER\_AGE), and the number of months between the date a review was posted by the reviewer and the date his or her account was registered (JOIN\_MONTHS). Reviews that the reviewer had posted in the past had a higher probability of obtaining more comments over time; furthermore, the reviewer who joined the social group earlier also had a higher potential of posting more reviews and receive more attention. Therefore, we traced reviewers’ characteristics at the moment when they posted the review according to reviews’ historical records. An example of a reviewer’s historical records is presented in Fig. 2. We collected reviewers’ previous review information, including the total number of past reviews (NUM\_PAST\_REVIEW), the total number of hotels the reviewer has reviewed (NUM\_PAST\_HOTEL), and the total number of past votes (NUM\_PAST\_VOTE).

Ngo-Ye and Sinha [32] applied RFM theory to online review research and described the overall contribution of a reviewer to the entire online social network. For the target reviewer, the following

![](/api/attachments/D95M2SQ5/fulltext/images/cc1f542b1cf5c011982fcf6b0f9a6d9c0f13647a6c799783e3425723abd0e1bd.jpg)

## Reviews

Recent Reviews FAQ

Reviews

· TripCollective Badge Collection

Explore the world! TripAdvisor has reviews and information on over 400,000 locations, including:

New York City

<table><tr><td>Date Posted</td><td>Title</td><td>Rating</td><td>Review Helpful?</td></tr><tr><td>June 15, 2015</td><td>New York City: OPEN LOOP New York: Expected better. Not enough stops and took forever to get from one place to the next.</td><td></td><td>1</td></tr><tr><td>June 15, 2015</td><td>New York City: Shake Shack: Great Burger and fast service!</td><td></td><td>0</td></tr><tr><td>June 15, 2015</td><td>New York City: Chevys Fresh Mex: Great food!</td><td></td><td>0</td></tr><tr><td>June 15, 2015</td><td>New York City: Staybridge Suites Times Square - New York City: Overall great stay</td><td></td><td>3</td></tr><tr><td>June 15, 2015</td><td>New York City: Capizzi: Very good little place</td><td></td><td>0</td></tr><tr><td>January 3, 2015</td><td>Hereford: Dakota&#x27;s Steak House: Disappointing every time.</td><td></td><td>0</td></tr><tr><td>September 16, 2014</td><td>Fredericksburg: Pasta Bella Restaurant &amp; Bkry: Great Little Place</td><td></td><td>0</td></tr><tr><td>September 16, 2014</td><td>Fredericksburg: Lincoln Street Wine Bar: Not so great service</td><td></td><td>0</td></tr><tr><td>August 5, 2014</td><td>Albuquerque: Saggio&#x27;s: A little pricey.. But glad I tried</td><td></td><td>0</td></tr><tr><td>February 23, 2014</td><td>Oklahoma City: Holiday Inn Oklahoma City Airport North: Won&#x27;t be back</td><td></td><td>2</td></tr><tr><td>February 23, 2014</td><td>Oklahoma City: Spaghetti Warehouse: Good food good price</td><td></td><td>0</td></tr><tr><td>February 22, 2014</td><td>Oklahoma City: Bricktown Brewery Restaurant: Never a disappointment!</td><td></td><td>0</td></tr><tr><td>February 12, 2014</td><td>Hereford: Joe&#x27;s Pizza &amp; pasta: Heaping Helping!</td><td></td><td>1</td></tr><tr><td>October 13, 2013</td><td>Santa Fe: Maria&#x27;s New Mexican Kitchen: Got to try the green chile stew!</td><td></td><td>0</td></tr><tr><td>October 13, 2013</td><td>Santa Fe: Del Charro Saloon: 17.00 for 2 margaritas!!</td><td></td><td>3</td></tr><tr><td>October 13, 2013</td><td>Chimayo: Casa Escondida Bed &amp; Breakfast: The peace and relaxation was here!</td><td></td><td>1</td></tr><tr><td>September 29, 2013</td><td>San Angelo: Cork and Pig Tavern: Gotta try the Slaw!!</td><td></td><td>1</td></tr><tr><td>August 17, 2013</td><td>Round Rock: Salt Lick BBQ: Finger lickin&#x27; good!</td><td></td><td>0</td></tr><tr><td>November 20, 2012</td><td>Santa Fe: Adobe Abode Bed and Breakfast Inn: Perfect!</td><td></td><td>0</td></tr><tr><td>November 20, 2012</td><td>Santa Fe: Agave Lounge: Great for date night.</td><td></td><td>12</td></tr><tr><td>November 20, 2012</td><td>Santa Fe: Cafe Pasqual&#x27;s: Definitely a tourist spot and they know it!</td><td></td><td>5</td></tr><tr><td>November 5, 2012</td><td>Oklahoma City: Pinkitzel: LOVE!~</td><td></td><td>0</td></tr><tr><td>November 5, 2012</td><td>Oklahoma City: Courtyard by Marriott Oklahoma City Downtown: Great Location</td><td></td><td>2</td></tr><tr><td>November 5, 2012</td><td>Oklahoma City: Bricktown Candy Co.: A Must Go!</td><td></td><td>2</td></tr></table>

Fig. 2. An example of a reviewer’s historical record.

Y.-H. Hu et al. / Information & Management xxx (2016) xxx–xxx

three RFM-related variables were considered: the date difference between the latest review and the previous review (RECENCY), the total number of reviews before the current review (FREQUENCY), and the total number of votes the reviewer had received in the past (MONETARY).

## 3.3. Investigated prediction techniques

We used Weka 3.6.14 data-mining software to construct the models [73]. Three prediction techniques were applied because of the characteristics of analysis—LR, REPTree, and RF. The LR is a widely used statistical method for modeling a dependent variable

Table 4  
Descriptive statistics for the reviews of the three regions.

<table><tr><td>Variable category</td><td>Variable Name</td><td>New York City/Chicago (NC) (n = 307,367) mean (std. dev.)</td><td>Miami/Orlando (MO) (n = 175,376) mean (std. dev.)</td><td>Las Vegas (LV) (n = 234,259) mean (std. dev.)</td></tr><tr><td rowspan="13">Review Quality</td><td>RATING</td><td>4.181 (1.012)</td><td>4.067 (1.113)</td><td>4.097 (1.078)</td></tr><tr><td>LENGTH_CHAR</td><td>589.813 (494.822)</td><td>686.307 (659.918)</td><td>611.765 (599.693)</td></tr><tr><td>LENGTH_SYLL</td><td>199.023 (165.939)</td><td>231.055 (220.144)</td><td>206.696 (200.744)</td></tr><tr><td>LENGTH_WORD</td><td>137.4 (117.86)</td><td>161.441 (157.642)</td><td>145.936 (144.516)</td></tr><tr><td>LENGTH_SENT</td><td>10.115 (8.463)</td><td>11.8 (11.067)</td><td>11.193 (11.256)</td></tr><tr><td>SYLL_PER_WORD</td><td>1.419 (0.111)</td><td>1.404 (0.111)</td><td>1.391 (0.114)</td></tr><tr><td>WORD_PER_SENT</td><td>15.255 (7.895)</td><td>15.704 (10.148)</td><td>15.254 (9.025)</td></tr><tr><td>ARI</td><td>6.316 (2.519)</td><td>6.191 (2.6)</td><td>5.734 (2.657)</td></tr><tr><td>CLI</td><td>9.499 (1.561)</td><td>9.266 (1.584)</td><td>8.929 (1.627)</td></tr><tr><td>FRES</td><td>71.322 (10.797)</td><td>72.207 (11.53)</td><td>73.737 (11.484)</td></tr><tr><td>FGL</td><td>6.932 (2.121)</td><td>6.824 (2.206)</td><td>6.531 (2.239)</td></tr><tr><td>FOG</td><td>9.555 (2.528)</td><td>9.466 (2.676)</td><td>9.294 (2.706)</td></tr><tr><td>SMOG</td><td>6.943 (1.616)</td><td>6.863 (1.684)</td><td>6.669 (1.682)</td></tr><tr><td rowspan="19">Review Polarity</td><td>SUBJECTIVITY</td><td>0.368 (0.254)</td><td>0.346 (0.252)</td><td>0.334 (0.256)</td></tr><tr><td>STR_POS</td><td>0.47 (0.187)</td><td>0.454 (0.192)</td><td>0.452 (0.197)</td></tr><tr><td>STR_NEG</td><td>0.109 (0.132)</td><td>0.13 (0.148)</td><td>0.13 (0.146)</td></tr><tr><td>WEAK_POS</td><td>0.334 (0.169)</td><td>0.335 (0.173)</td><td>0.335 (0.181)</td></tr><tr><td>WEAK_NEG</td><td>0.087 (0.098)</td><td>0.081 (0.097)</td><td>0.082 (0.1)</td></tr><tr><td>STR_SENTI</td><td>0.579 (0.172)</td><td>0.583 (0.175)</td><td>0.582 (0.183)</td></tr><tr><td>WEAK_SENTI</td><td>0.421 (0.172)</td><td>0.416 (0.175)</td><td>0.417 (0.183)</td></tr><tr><td>N_SENTI_SCORE</td><td>11.496 (9.561)</td><td>11.363 (10.758)</td><td>10.245 (9.643)</td></tr><tr><td>N_SENTI_CLASS</td><td>Negative: 16,125</td><td>Negative: 12,420</td><td>Negative: 16,412</td></tr><tr><td></td><td>Neutral: 5084</td><td>Neutral: 3514</td><td>Neutral: 5130</td></tr><tr><td></td><td>Positive: 286,158</td><td>Positive: 159,442</td><td>Positive: 212,717</td></tr><tr><td>S_SENTI_CLASS</td><td>Negative: 147,429</td><td>Negative: 97,725</td><td>Negative: 123,927</td></tr><tr><td></td><td>Neutral: 33,122</td><td>Neutral: 17,227</td><td>Neutral: 24,015</td></tr><tr><td></td><td>Positive: 126,816</td><td>Positive: 60,424</td><td>Positive: 86,317</td></tr><tr><td>STANFORD_VERYNEG</td><td>0.016 (0.064)</td><td>0.018 (0.073)</td><td>0.018 (0.072)</td></tr><tr><td>STANFORD_NEG</td><td>0.439 (0.238)</td><td>0.473 (0.24)</td><td>0.455 (0.247)</td></tr><tr><td>STANFORD_NEUTRAL</td><td>0.139 (0.145)</td><td>0.143 (0.145)</td><td>0.157 (0.153)</td></tr><tr><td>STANFORD_POS</td><td>0.361 (0.231)</td><td>0.329 (0.23)</td><td>0.331 (0.232)</td></tr><tr><td>STANFORD_VERYPOS</td><td>0.045 (0.1)</td><td>0.037 (0.091)</td><td>0.04 (0.097)</td></tr><tr><td rowspan="24">Reviewer</td><td>REVIEWER_LEVEL</td><td>N/A: 67,793</td><td>N/A: 40,746</td><td>N/A: 60,332</td></tr><tr><td></td><td>New Reviewer: 22,715</td><td>New Reviewer: 12,768</td><td>New Reviewer: 16,293</td></tr><tr><td></td><td>Reviewer: 34,046</td><td>Reviewer: 18,804</td><td>Reviewer: 23,898</td></tr><tr><td></td><td>Senior Reviewer: 58,648</td><td>Senior Reviewer: 32,352</td><td>Senior Reviewer: 41,952</td></tr><tr><td></td><td>Contributor: 48,789</td><td>Contributor: 27,398</td><td>Contributor: 35,793</td></tr><tr><td></td><td>Senior Contributor: 40,290</td><td>Senior Contributor: 22,671</td><td>Senior Contributor: 29,741</td></tr><tr><td></td><td>Top Contributor: 35,086</td><td>Top Contributor: 20,637</td><td>Top Contributor: 26,250</td></tr><tr><td>REVIEWER_SEX</td><td>N/A: 192,903</td><td>N/A: 110,780</td><td>N/A: 149,618</td></tr><tr><td></td><td>Male: 62,942</td><td>Male: 33,719</td><td>Male: 46,245</td></tr><tr><td></td><td>Female: 51,522</td><td>Female: 30,877</td><td>Female: 38,396</td></tr><tr><td>REVIEWER_AGE</td><td>N/A: 202,448</td><td>N/A: 115,777</td><td>N/A: 155,724</td></tr><tr><td></td><td>13-17 yrs: 70</td><td>13-17 yrs: 79</td><td>13-17 yrs: 55</td></tr><tr><td></td><td>18-24 yrs: 2878</td><td>18-24 yrs: 1,689</td><td>18-24 yrs: 2007</td></tr><tr><td></td><td>25-34 yrs: 21,877</td><td>25-34 yrs: 11,257</td><td>25-34 yrs: 17,418</td></tr><tr><td></td><td>35-49 yrs: 42,260</td><td>35-49 yrs: 27,036</td><td>35-49 yrs: 30,516</td></tr><tr><td></td><td>50-64 yrs: 32,059</td><td>50-64 yrs: 16,346</td><td>50-64 yrs: 24,132</td></tr><tr><td></td><td>&gt;65 yrs: 5775</td><td>&gt;65 yrs: 3192</td><td>&gt;65 yrs: 4407</td></tr><tr><td>JOIN_MONTHS</td><td>48.448 (33.635)</td><td>47.015 (33.819)</td><td>45.032 (33.859)</td></tr><tr><td>NUM_PAST_REVIEW</td><td>81.566 (433.494)</td><td>83.925 (387.312)</td><td>88.149 (453.818)</td></tr><tr><td>NUM_PAST_HOTEL</td><td>2.883 (2.305)</td><td>2.843 (2.304)</td><td>2.763 (2.31)</td></tr><tr><td>NUM_PAST_VOTE</td><td>22.958 (65.185)</td><td>23.988 (56.34)</td><td>22.341 (53.549)</td></tr><tr><td>RECENCY</td><td>487.615 (312.174)</td><td>481.384 (312.777)</td><td>476.956 (312.974)</td></tr><tr><td>FREQUENCY</td><td>0.339 (0.990)</td><td>0.394 (1.086)</td><td>0.367 (0.985)</td></tr><tr><td>MONETARY</td><td>0.313 (1.318)</td><td>0.525 (2.062)</td><td>0.454 (1.853)</td></tr><tr><td>DV</td><td>HELPFULNESS</td><td>0.147 (0.596)</td><td>0.258 (0.813)</td><td>0.213 (0.904)</td></tr></table>

Please cite this article in press as: Y.-H. Hu, et al., The effect of user-controllable <sup>fi</sup>lters on the prediction of online hotel reviews, Inf. Manage. (2017), http://dx.doi.org/10.1016/j.im.2016.12.009

according to a linear combination of one or more IVs. Considering the experimental results, researchers are recommended to use statistical modeling such as LR to strengthen the predictive capabilities of the model. REPTree is an extension of regression tree (RT) techniques with a hierarchical structure comprising branches and nodes. The internal node represents one of the selected IVs and its branches represent a subset of predictor values. The leaf node represents a set of instances satisfying a speci<sup>fi</sup>c set of decision rules in the tree. REPTree adopts the RT tree logic that creates multiple trees at each iteration and then selects the most favorable iteration as the representative. Therefore, REPTree is a fast decision tree (DT) learner, which constructs an RT by using information gain as the splitting criterion and shapes the tree using REP. Finally, the RF is an ensemble learning method developed by constructing multiple DTs [74]. In the training process, RF applies the bagging technique to bootstrap instances; a set of DTs is then constructed on the basis of each set of bootstrap instances with a subset of features. Thereafter, a random subset of features is selected. After the set of trees is constructed, a prediction regarding unseen samples can be generated by selecting the majority class of individual trees.

## 4. Analysis and results

## 4.1. Descriptive statistics of the collected reviews

The descriptive statistics of the hotel reviews of the three regions are displayed in Table 4, revealing that the average number of reviews per hotel was signi<sup>fi</sup>cantly different. Among the three travel regions, the south region received the most helpfulness votes per a review on average (0.258), followed by the west (0.213) and north (0.147) regions. The average review ratings in all three regions were relatively similar. With regard to the average review length, the south region ranked <sup>fi</sup>rst (11.8 sentences per review), followed by the west (11.193) and north (10.115) regions.

## 4.2. Baseline replication

The purpose of a baseline model is to replicate existing research for the possible re<sup>fi</sup>nement of existing theories. In Mudambi and Schuff [12], product reviews were analyzed for two categories of products—search goods and experience goods. Because hotels are experience goods, their results for experience goods are particularly relevant to the present study. Table 5 con<sup>fi</sup>rms that our results from a 10-fold cross-validation are relatively similar to those of Mudambi and Schuff, with rating being the strongest predictor of review helpfulness, followed by rating squared and then by word count.

The major difference is that the model <sup>fi</sup>t degrades signi<sup>fi</sup>cantly in our model $\scriptstyle ( R ^ { 2 } = 0 . 0 1 5 )$ versus that in Mudambi and Schuff [12] $\scriptstyle ( R ^ { 2 } = 0 . 3 6 1 )$ , indicating that the existing list of predictors from Mudambi and Schuff [12] may not be suf<sup>fi</sup>cient to explain the amount of variance for review helpfulness in the context of hotel reviews. This is consistent with the conclusion of other studies (e.g., [11], in which readers of hotel reviews tend to rely on additional cues to assess the quality or helpfulness of a hotel review. Therefore, the following sections are designed to reveal insights regarding predictors supported in the relevant literature as well as interactions among the major predictors.

Table 5 Baseline replication.

<table><tr><td></td><td>Coefficient</td><td>Std. Error</td><td>Standardized Coefficient</td><td>t-value</td><td>Sig.</td></tr><tr><td>(Constant)</td><td>0.671</td><td>0.008</td><td></td><td>84.766</td><td>0.000</td></tr><tr><td>Rating</td><td>-0.292</td><td>0.005</td><td>-0.406</td><td>-62.770</td><td>0.000</td></tr><tr><td> $Rating^2$ </td><td>0.037</td><td>0.001</td><td>0.359</td><td>55.480</td><td>0.000</td></tr><tr><td>Word count</td><td>0.000</td><td>0.000</td><td>0.079</td><td>66.489</td><td>0.000</td></tr></table>

R<sup>2</sup> = 0.015, correlation coef<sup>fi</sup>cient (CC) = 0.1216, mean absolute error (MAE) = 0.2574, root- mean-squared error (RMSE) = 0.7578.

## 4.3. Extensions to the existing model

## 4.3.1. Interaction effect

As travel websites offer options to <sup>fi</sup>lter reviews according to certain attributes, the probability of a review being available on the top (termed review visibility by Hu and Chen [11] in the search result is partially controlled by the <sup>fi</sup>lter the reader has chosen. Eventually, the reviews on the top have a greater chance of being voted as helpful. For TripAdvisor.com, <sup>fi</sup>lters are available for city, traveler type, language, and time of year. Because we focused on reviews written only in English, the remaining three <sup>fi</sup>lters were relevant to the present study.

In this section of the study, we examine the interactions among the aforementioned <sup>fi</sup>lters for their effects on review helpfulness. This area has not been explored in previous product review studies. The majority of related studies have focused on identifying the most favorable combination of predictors, thereby neglecting that predictors also interact with each other. Such interactions would affect the linear relationship between the predictors and the DV. Table 6 presents the interaction effects among travel region (TravelRegion), travel type (TravelType), and time of year (Time-OfYear) for travel. In the present study, we sampled the <sup>fi</sup>ve top cities into three geographical regions, namely north region (New York City/Chicago, NC), south region (Miami/Orlando, MO), and west region (Las Vegas, LV). To simplify the analysis, we categorized the reviews by two traveler types (i.e., TravelType = Business/Non-business, B/NB) and two periods (TimeOfYear = Summer–Fall/Winter–Spring, SF/WS). Consequently, we obtained a $3 \times 2 \times 2$ design.

Table 6 shows that all the three main effects were signi<sup>fi</sup>cant. The four interaction effects are also statistically signi<sup>fi</sup>cant, meaning that helpfulness varies among travel destination, types of travel, and the time of the year. As Fig. 3 shows, helpfulness of business travels peaked when the destination is in the southern geographic region. The slope of the two lines in Fig. 4 varies more between the northern and southern regions than between the southern and western regions. Helpfulness shown in Fig. 5 is more similar for Summer–Fall travels between business and nonbusiness travels than that for the Winter–Spring time.

## 4.3.2. Model building

A 10-fold cross-validation was applied to all of the experimental evaluations. To evaluate the model performance, the metrics of correlation coef<sup>fi</sup>cient (CC), mean absolute error (MAE), and rootmean-squared error (RMSE) were considered. CC describes the degree of the linear relationship between observed and simulated data. The CC ranged from 1 to 1 for a perfectly negative or positive interrelationship. The MAE measures the average value of the sample of the observed and simulated data; an MAE of zero suggests a perfect <sup>fi</sup>t or high accuracy. The RMSE measures the squared and averaged value of the sample of the observed and simulated data. Similar to the MAE, an RMSE of zero indicates a perfect <sup>fi</sup>t for the data; however, the RMSE value will be higher for greater sampling error because the values are squared. Both error measurements describe the variation in the observed and simulated data.

On the basis of the results in Section 4.3.1, the complete set of hotel reviews in each travel region was further divided into four subsets: business trip during Summer–Fall (SF-B), non-business trip during Summer–Fall (SF-NB), business trip during Winter–

Y.-H. Hu et al. / Information & Management xxx (2016) xxx–xxx

Table 6  
Interaction effects among city, traveler type, and time of year for travel Dependent variable: Review Helpfulness.

<table><tr><td>Source</td><td>Type III Sum of Squares</td><td>df</td><td>Mean Square</td><td>F</td><td>Sig.</td></tr><tr><td>Corrected Model</td><td>9436.162</td><td>11</td><td>857.833</td><td>1505.870</td><td>0.000</td></tr><tr><td>Intercept</td><td>12354.334</td><td>1</td><td>12354.334</td><td>21687.224</td><td>0.000</td></tr><tr><td>TravelRegion</td><td>421.718</td><td>2</td><td>210.859</td><td>370.149</td><td>0.000</td></tr><tr><td>TravelType</td><td>379.132</td><td>1</td><td>379.132</td><td>665.542</td><td>0.000</td></tr><tr><td>TimeOfYear</td><td>3293.759</td><td>1</td><td>3293.759</td><td>5781.979</td><td>0.000</td></tr><tr><td>TravelRegion * TravelType</td><td>171.979</td><td>2</td><td>85.989</td><td>150.949</td><td>0.000</td></tr><tr><td>TravelRegion * TimeOfYear</td><td>83.178</td><td>2</td><td>41.589</td><td>73.007</td><td>0.000</td></tr><tr><td>TravelType * TimeOfYear</td><td>86.861</td><td>1</td><td>86.861</td><td>152.478</td><td>0.000</td></tr><tr><td>TravelRegion * TravelType * TimeOfYear</td><td>32.892</td><td>2</td><td>16.446</td><td>28.870</td><td>0.000</td></tr><tr><td>Error</td><td>408440.195</td><td>716990</td><td>0.570</td><td></td><td></td></tr><tr><td>Total</td><td>445300.151</td><td>717002</td><td></td><td></td><td></td></tr><tr><td>Corrected Total</td><td>417876.357</td><td>717001</td><td></td><td></td><td></td></tr></table>

![](/api/attachments/D95M2SQ5/fulltext/images/e608371732e719ed7e246ea41aea708ad93e05d36d381eaa8902b8297a313849.jpg)  
Fig. 3. Interaction plot (TravelType by TravelRegion).

Spring (WS-B), and non-business trip during Winter–Spring (WS-NB).

The CC, MAE, and RMSE values for the 12 data sets for the classi<sup>fi</sup>cation of travel types were compared and are presented in Table 7. The CC values revealed that all three prediction techniques had weak-to-moderate linear relationships between observed and simulated data, and the samples were directly related. On average, the CC and RMSE performance indicators show that RF was the best model to predict helpfulness, followed by REPTree and LR. REPtree had the lowest MAE, followed by RF and LR, but there is no signi<sup>fi</sup>cant statistical difference between REPTree and RF on MAE. Therefore, judging by all three performance indicators, RF should be recommended as the most effective model among the three. It is worth noting that all the developed models in this study signi<sup>fi</sup>cantly outperform the baseline model (Table 5). This provides empirical evidence that additional variables extracted from review diagnosticity, reviewer credibility, and other aspects help to improve the predictive power of all three models.

Among the different regions, NC and LV tend to have a lower CC; however, NC-WS-B and LV-WS-B had a higher CC. A higher CC indicates that the predictors were adequately related to the outcome variables. The MAE and RMSE were extremely similar for all data sets. The MAE for B dominated the lower 50%; the MAEs for NC were relatively lower than those of MO and LV across all data sets. These results indicate adequate classi<sup>fi</sup>cation and low prediction errors for all data sets. In addition, the selected features can be used to increase the performance of review helpfulness prediction. The RMSE for B was also in the lower 50% range. In general, NC had lower RMSE of the prediction techniques. In addition to the NC being the region with a lower RMSE, NC-SF had the lowest MAE and RMSE. In addition to the lower end, LV had the highest MAE and RMSE. As evident from this evaluation, LV-WS-NB had a signi<sup>fi</sup>cantly higher RMSE among all data sets. Because the

![](/api/attachments/D95M2SQ5/fulltext/images/20ed82a7df9433ca7966f36efc34ad6b2db6de62f2939b0091d20a43fb0501d3.jpg)  
Fig. 4. Interaction plot (TimeOfYear by TravelRegion).

![](/api/attachments/D95M2SQ5/fulltext/images/9384bf74f7aa6f253f3dd3dcbe782fc175a14a519c8839ba6e9164e167a2354a.jpg)  
Fig. 5. Interaction plot (TravelType by TimeOfYear).

Table 7  
Experimental results of different prediction models using all features<sup>a</sup>.

<table><tr><td>Data set</td><td>TravelRegion</td><td>TimeOfYear</td><td>TravelType</td><td>Classifiers</td><td>CC</td><td>MAE</td><td>RMSE</td></tr><tr><td rowspan="3">NC-SF-B</td><td rowspan="3">NC</td><td rowspan="3">SF</td><td rowspan="3">B</td><td>LR</td><td>0.248</td><td>0.069</td><td>0.166</td></tr><tr><td>REPtree</td><td>0.369</td><td>0.059</td><td>0.160</td></tr><tr><td>RF</td><td>0.386</td><td>0.062</td><td>0.158</td></tr><tr><td rowspan="3">NC-SF-NB</td><td rowspan="3">NC</td><td rowspan="3">SF</td><td rowspan="3">NB</td><td>LR</td><td>0.240</td><td>0.085</td><td>0.237</td></tr><tr><td>REPtree</td><td>0.452</td><td>0.073</td><td>0.218</td></tr><tr><td>RF</td><td>0.482</td><td>0.074</td><td>0.214</td></tr><tr><td rowspan="3">NC-WS-B</td><td rowspan="3">NC</td><td rowspan="3">WS</td><td rowspan="3">B</td><td>LR</td><td>0.298</td><td>0.284</td><td>0.670</td></tr><tr><td>REPtree</td><td>0.405</td><td>0.226</td><td>0.646</td></tr><tr><td>RF</td><td>0.503</td><td>0.214</td><td>0.607</td></tr><tr><td rowspan="3">NC-WS-NB</td><td rowspan="3">NC</td><td rowspan="3">WS</td><td rowspan="3">NB</td><td>LR</td><td>0.297</td><td>0.329</td><td>0.799</td></tr><tr><td>REPtree</td><td>0.537</td><td>0.231</td><td>0.707</td></tr><tr><td>RF</td><td>0.550</td><td>0.238</td><td>0.700</td></tr><tr><td rowspan="3">MO-SF-B</td><td rowspan="3">MO</td><td rowspan="3">SF</td><td rowspan="3">B</td><td>LR</td><td>0.280</td><td>0.078</td><td>0.176</td></tr><tr><td>REPtree</td><td>0.356</td><td>0.070</td><td>0.172</td></tr><tr><td>RF</td><td>0.458</td><td>0.068</td><td>0.163</td></tr><tr><td rowspan="3">MO-SF-NB</td><td rowspan="3">MO</td><td rowspan="3">SF</td><td rowspan="3">NB</td><td>LR</td><td>0.297</td><td>0.143</td><td>0.386</td></tr><tr><td>REPtree</td><td>0.573</td><td>0.107</td><td>0.332</td></tr><tr><td>RF</td><td>0.629</td><td>0.108</td><td>0.316</td></tr><tr><td rowspan="3">MO-WS-B</td><td rowspan="3">MO</td><td rowspan="3">WS</td><td rowspan="3">B</td><td>LR</td><td>0.334</td><td>0.286</td><td>0.607</td></tr><tr><td>REPtree</td><td>0.520</td><td>0.203</td><td>0.553</td></tr><tr><td>RF</td><td>0.576</td><td>0.213</td><td>0.529</td></tr><tr><td rowspan="3">MO-WS-NB</td><td rowspan="3">MO</td><td rowspan="3">WS</td><td rowspan="3">NB</td><td>LR</td><td>0.391</td><td>0.493</td><td>1.024</td></tr><tr><td>REPtree</td><td>0.662</td><td>0.307</td><td>0.836</td></tr><tr><td>RF</td><td>0.683</td><td>0.318</td><td>0.816</td></tr><tr><td rowspan="3">LV-SF-B</td><td rowspan="3">LV</td><td rowspan="3">SF</td><td rowspan="3">B</td><td>LR</td><td>0.270</td><td>0.098</td><td>0.282</td></tr><tr><td>REPtree</td><td>0.480</td><td>0.084</td><td>0.262</td></tr><tr><td>RF</td><td>0.565</td><td>0.081</td><td>0.244</td></tr><tr><td rowspan="3">LV-SF-NB</td><td rowspan="3">LV</td><td rowspan="3">SF</td><td rowspan="3">NB</td><td>LR</td><td>0.201</td><td>0.106</td><td>0.399</td></tr><tr><td>REPtree</td><td>0.239</td><td>0.093</td><td>0.412</td></tr><tr><td>RF</td><td>0.527</td><td>0.084</td><td>0.348</td></tr><tr><td rowspan="3">LV-WS-B</td><td rowspan="3">LV</td><td rowspan="3">WS</td><td rowspan="3">B</td><td>LR</td><td>0.285</td><td>0.369</td><td>0.961</td></tr><tr><td>REPtree</td><td>0.438</td><td>0.255</td><td>0.928</td></tr><tr><td>RF</td><td>0.593</td><td>0.263</td><td>0.813</td></tr><tr><td rowspan="3">LV-WS-NB</td><td rowspan="3">LV</td><td rowspan="3">WS</td><td rowspan="3">NB</td><td>LR</td><td>0.301</td><td>0.456</td><td>1.166</td></tr><tr><td>REPtree</td><td>0.612</td><td>0.271</td><td>0.971</td></tr><tr><td>RF</td><td>0.627</td><td>0.289</td><td>0.956</td></tr><tr><td rowspan="3">Average</td><td></td><td></td><td></td><td>LR</td><td>0.287</td><td>0.233</td><td>0.573</td></tr><tr><td></td><td></td><td></td><td>REPtree</td><td>0.470</td><td>0.165</td><td>0.516</td></tr><tr><td></td><td></td><td></td><td>RF</td><td>0.548</td><td>0.167</td><td>0.489</td></tr></table>

<sup>a</sup> NC: north region (New York and Chicago), LV: west region (Las Vegas), MO: south region (Miami and Orland), SF: Summer–Fall, WS: Winter–Spring, B: business travel, NB: non-business travel.

RMSE had unequal weight toward errors, greater errors gained higher RMSEs, and the LV had greater variations across the samples.

## 4.3.3. Reduction of independent variables (IVs)

To further simplify the models, we conducted the correlationbased feature subset selection (CFS) technique to reduce the dimensionality of the data sets [75]. Speci<sup>fi</sup>cally, the CfsSubsetEval module with BestFirst search method in WEKA was used in our study. This method chooses a set of IVs that maximize their correlations with the DV, but minimize the correlation among them.

After applying the CFS method, the average number of IVs was reduced to 15.42, which is approximately two-<sup>fi</sup>fths of the original IVs. As shown in Table 8, after feature selection, RF has the highest average CC, MAE, and RMSE, followed by REPTree and LR. Compared with the results in Table 7, the total number of IVs is greatly reduced with the CFS method at the expense of a small reduction of performance measured as the average CC, MAE, and RMSE.

## 5. Discussion

The present study extends Mudambi and Schuff’s diagnosticity based theory to include predictors of product reviews from diagnosticity, eWOM, and UGC literatures. Mudambi and Schuff’s model was <sup>fi</sup>rst checked for its validity in the context of hotel reviews—a form of experience goods that is distinctively different from search goods. The predictors were also checked together with the interactions among user-controllable <sup>fi</sup>lters for their collective relationship with hotel review helpfulness. The extended formulation of predictors was tested in three models, namely LR, RF, and REPTree, to examine their predictability.

Table 8  
Experimental results of different prediction models using feature selection techniques<sup>a</sup>.

<table><tr><td>Data set</td><td>Travel Region</td><td>Time Of Year</td><td>Travel Type</td><td>Classifiers</td><td>CC</td><td>MAE</td><td>RMSE</td></tr><tr><td rowspan="3">NC-SF-B</td><td rowspan="3">NC</td><td rowspan="3">SF</td><td rowspan="3">B</td><td>LR</td><td>0.245</td><td>0.069</td><td>0.166</td></tr><tr><td>REPtree</td><td>0.334</td><td>0.066</td><td>0.162</td></tr><tr><td>RF</td><td>0.349</td><td>0.067</td><td>0.161</td></tr><tr><td rowspan="3">NC-SF-NB</td><td rowspan="3">NC</td><td rowspan="3">SF</td><td rowspan="3">NB</td><td>LR</td><td>0.238</td><td>0.085</td><td>0.238</td></tr><tr><td>REPtree</td><td>0.455</td><td>0.079</td><td>0.218</td></tr><tr><td>RF</td><td>0.447</td><td>0.081</td><td>0.220</td></tr><tr><td rowspan="3">NC-WS-B</td><td rowspan="3">NC</td><td rowspan="3">WS</td><td rowspan="3">B</td><td>LR</td><td>0.296</td><td>0.283</td><td>0.670</td></tr><tr><td>REPtree</td><td>0.390</td><td>0.228</td><td>0.649</td></tr><tr><td>RF</td><td>0.461</td><td>0.214</td><td>0.625</td></tr><tr><td rowspan="3">NC-WS-NB</td><td rowspan="3">NC</td><td rowspan="3">WS</td><td rowspan="3">NB</td><td>LR</td><td>0.294</td><td>0.328</td><td>0.800</td></tr><tr><td>REPtree</td><td>0.459</td><td>0.265</td><td>0.745</td></tr><tr><td>RF</td><td>0.473</td><td>0.268</td><td>0.739</td></tr><tr><td rowspan="3">MO-SF-B</td><td rowspan="3">MO</td><td rowspan="3">SF</td><td rowspan="3">B</td><td>LR</td><td>0.276</td><td>0.078</td><td>0.176</td></tr><tr><td>REPtree</td><td>0.287</td><td>0.071</td><td>0.184</td></tr><tr><td>RF</td><td>0.461</td><td>0.067</td><td>0.163</td></tr><tr><td rowspan="3">MO-SF-NB</td><td rowspan="3">MO</td><td rowspan="3">SF</td><td rowspan="3">NB</td><td>LR</td><td>0.290</td><td>0.143</td><td>0.387</td></tr><tr><td>REPtree</td><td>0.542</td><td>0.119</td><td>0.340</td></tr><tr><td>RF</td><td>0.581</td><td>0.121</td><td>0.330</td></tr><tr><td rowspan="3">MO-WS-B</td><td rowspan="3">MO</td><td rowspan="3">WS</td><td rowspan="3">B</td><td>LR</td><td>0.334</td><td>0.286</td><td>0.608</td></tr><tr><td>REPtree</td><td>0.439</td><td>0.239</td><td>0.582</td></tr><tr><td>RF</td><td>0.466</td><td>0.240</td><td>0.573</td></tr><tr><td rowspan="3">MO-WS-NB</td><td rowspan="3">MO</td><td rowspan="3">WS</td><td rowspan="3">NB</td><td>LR</td><td>0.388</td><td>0.493</td><td>1.025</td></tr><tr><td>REPtree</td><td>0.587</td><td>0.353</td><td>0.903</td></tr><tr><td>RF</td><td>0.597</td><td>0.357</td><td>0.898</td></tr><tr><td rowspan="3">LV-SF-B</td><td rowspan="3">LV</td><td rowspan="3">SF</td><td rowspan="3">B</td><td>LR</td><td>0.272</td><td>0.097</td><td>0.282</td></tr><tr><td>REPtree</td><td>0.451</td><td>0.089</td><td>0.266</td></tr><tr><td>RF</td><td>0.534</td><td>0.087</td><td>0.248</td></tr><tr><td rowspan="3">LV-SF-NB</td><td rowspan="3">LV</td><td rowspan="3">SF</td><td rowspan="3">NB</td><td>LR</td><td>0.200</td><td>0.106</td><td>0.399</td></tr><tr><td>REPtree</td><td>0.246</td><td>0.100</td><td>0.412</td></tr><tr><td>RF</td><td>0.562</td><td>0.092</td><td>0.338</td></tr><tr><td rowspan="3">LV-WS-B</td><td rowspan="3">LV</td><td rowspan="3">WS</td><td rowspan="3">B</td><td>LR</td><td>0.298</td><td>0.368</td><td>0.957</td></tr><tr><td>REPtree</td><td>0.433</td><td>0.284</td><td>0.920</td></tr><tr><td>RF</td><td>0.555</td><td>0.276</td><td>0.834</td></tr><tr><td rowspan="3">LV-WS-NB</td><td rowspan="3">LV</td><td rowspan="3">WS</td><td rowspan="3">NB</td><td>LR</td><td>0.300</td><td>0.455</td><td>1.167</td></tr><tr><td>REPtree</td><td>0.551</td><td>0.322</td><td>1.024</td></tr><tr><td>RF</td><td>0.564</td><td>0.325</td><td>1.012</td></tr><tr><td rowspan="3">Average</td><td></td><td></td><td></td><td>LR</td><td>0.286</td><td>0.233</td><td>0.573</td></tr><tr><td></td><td></td><td></td><td>REPtree</td><td>0.431</td><td>0.185</td><td>0.534</td></tr><tr><td></td><td></td><td></td><td>RF</td><td>0.504</td><td>0.183</td><td>0.512</td></tr></table>

<sup>a</sup> NC: north region (New York and Chicago), LV: west region (Las Vegas), MO: south region (Miami and Orland), SF: Summer–Fall, WS: Winter–Spring, B: business travel, NB: non-business travel.

Although the resulting performance metrics (CC, MAE, and RMSE) indicate that all three models outperform the baseline model of Mudambi and Schuff’s, we went a step further to also report the extent to which the set of predictors are applicable when user-controllable <sup>fi</sup>lters are in action. TripAdvisor.com provides four user-controllable <sup>fi</sup>lters, namely geographic location, type of travel, season of travel (i.e., TimeOfYear), and language. Since we are concerned with the English hotel reviews, our work focuses on only the <sup>fi</sup>rst three <sup>fi</sup>lters. As a result, we had three geographic regions, two travel types (B versus NB), and two travel seasons (SF versus WS). The combination divides the sample into 12 subsamples $( 3 \times 2 \times 2 )$

Table 9 summarizes critical IVs identi<sup>fi</sup>ed through the CFS method for the 12 subsamples individually. For review content features, our <sup>fi</sup>ndings show that the review rating (RATING) and the number of words in a review (LENGTH\_WORD) have strong effects on review helpfulness, which is consistent with existing studies [12,47]. In addition, although review readability has been exploited in past studies relating to review helpfulness [24,29,30,57], our work shows that review readability is not always valued by all travelers.

For review polarity features, both positive and negative sentiment score features displayed strong effects on review helpfulness in all subsamples. Research [29,76] has identi<sup>fi</sup>ed that sentiment adjectives can be widely identi<sup>fi</sup>ed in sentences expressing opinions. Positive opinions can provide consumers with favorable factors that they want to learn about regarding

Y.-H. Hu et al. / Information & Management xxx (2016) xxx–xxx

## Table 9

Crucial variables for each data set<sup>a</sup>.

<table><tr><td>NC-SF-B</td><td>NC-SF-NB</td><td>NC-WS-B</td><td>NC-WS-NB</td></tr><tr><td>RATING</td><td>RATING</td><td>RATING</td><td>RATING</td></tr><tr><td>LENGTH_WORD</td><td>LENGTH_WORD</td><td>LENGTH_WORD</td><td>LENGTH_SENT</td></tr><tr><td>SYLL_PER_WORD</td><td>WORD_PER_SENT</td><td>STR_POS</td><td>WORD_PER_SENT</td></tr><tr><td>CLI</td><td>STR_POS</td><td>STR_NEG</td><td>ARI</td></tr><tr><td>FRES</td><td>STR_NEG</td><td>WEAK_POS</td><td>CLI</td></tr><tr><td>STR_POS</td><td>WEAK_POS</td><td>WEAK_NEG</td><td>FOG</td></tr><tr><td>STR_NEG</td><td>STR_SENTI</td><td>STR_SENTI</td><td>STR_POS</td></tr><tr><td>WEAK_POS</td><td>N_SENTI_CLASS</td><td>WEAK_SENTI</td><td>STR_NEG</td></tr><tr><td>STR_SENTI</td><td>S_SENTI_CLASS</td><td>N_SENTI_CLASS</td><td>WEAK_POS</td></tr><tr><td>WEAK_SENTI</td><td>STANFORD_NEG</td><td>S_SENTI_CLASS</td><td>WEAK_NEG</td></tr><tr><td>N_SENTI_CLASS</td><td>STANFORD_POS</td><td>STANFORD_NEG</td><td>STR_SENTI</td></tr><tr><td>S_SENTI_CLASS</td><td>RECENTCY</td><td>STANFORD_POS</td><td>WEAK_SENTI</td></tr><tr><td>STANFORD_VERYNEG</td><td>MONETARY</td><td>STANFORD_VERYPOS</td><td>N_SENTI_CLASS</td></tr><tr><td>STANFORD_NEG</td><td></td><td>NUM_PAST_VOTE</td><td>S_SENTI_CLASS</td></tr><tr><td>STANFORD_POS</td><td></td><td>RECENTCY</td><td>STANFORD_VERYNEG</td></tr><tr><td>STANFORD_VERYPOS</td><td></td><td>MONETARY</td><td>STANFORD_NEG</td></tr><tr><td>RECENTCY</td><td></td><td></td><td>STANFORD_POS</td></tr><tr><td>FREQUENCY</td><td></td><td></td><td>STANFORD_VERYPOS</td></tr><tr><td>MONETARY</td><td></td><td></td><td>RECENTCY</td></tr><tr><td></td><td></td><td></td><td>MONETARY</td></tr></table>

<table><tr><td>LV-SF-B</td><td>LV-SF-NB</td><td>LV-WS-B</td><td>LV-WS-NB</td></tr><tr><td>RATING</td><td>RATING</td><td>RATING</td><td>RATING</td></tr><tr><td>LENGTH_WORD</td><td>LENGTH_WORD</td><td>LENGTH_WORD</td><td>LENGTH_WORD</td></tr><tr><td>LENGTH_SENT</td><td>WORD_PER_SENT</td><td>WORD_PER_SENT</td><td>STR_POS</td></tr><tr><td>SYLL_PER_WORD</td><td>FOG</td><td>CLI</td><td>STR_NEG</td></tr><tr><td>FRES</td><td>STR_POS</td><td>FRES</td><td>WEAK_POS</td></tr><tr><td>SMOG</td><td>STR_NEG</td><td>STR_POS</td><td>WEAK_NEG</td></tr><tr><td>STR_POS</td><td>WEAK_POS</td><td>STR_NEG</td><td>STR_SENTI</td></tr><tr><td>STR_NEG</td><td>WEAK_NEG</td><td>WEAK_POS</td><td>WEAK_SENTI</td></tr><tr><td>WEAK_POS</td><td>N_SENTI_CLASS</td><td>WEAK_NEG</td><td>N_SENTI_CLASS</td></tr><tr><td>WEAK_NEG</td><td>S_SENTI_CLASS</td><td>N_SENTI_CLASS</td><td>S_SENTI_CLASS</td></tr><tr><td>WEAK_SENTI</td><td>STANFORD_NEG</td><td>S_SENTI_CLASS</td><td>STANFORD_NEG</td></tr><tr><td>N_SENTI_CLASS</td><td>STANFORD_POS</td><td>STANFORD_NEG</td><td>STANFORD_POS</td></tr><tr><td>S_SENTI_CLASS</td><td>RECENTCY</td><td>STANFORD_POS</td><td>STANFORD_VERYPOS</td></tr><tr><td>STANFORD_VERYNEG</td><td>FREQUENCY</td><td>STANFORD_VERYPOS</td><td>RECENTCY</td></tr><tr><td>STANFORD_NEG</td><td>MONETARY</td><td>RECENTCY</td><td>FREQUENCY</td></tr><tr><td>STANFORD_POS</td><td></td><td>FREQUENCY</td><td>MONETARY</td></tr><tr><td>STANFORD_VERYPOS</td><td></td><td>MONETARY</td><td></td></tr><tr><td>NUM_PAST_HOTEL</td><td></td><td></td><td></td></tr><tr><td>RECENTCY</td><td></td><td></td><td></td></tr><tr><td>FREQUENCY</td><td></td><td></td><td></td></tr><tr><td>MONETARY</td><td></td><td></td><td></td></tr></table>

<sup>a</sup> NC: north region (New York and Chicago), LV: west region (Las Vegas), MO: south region (Miami and Orland), SF: Summer–Fall, WS: Winter–Spring, B: business travel, NB: non-business travel.

hotels, whereas negative opinions provide them with information concerning disadvantages and defects. Our <sup>fi</sup>ndings in this regard are fairly consistent with existing literature. The RFM model [32] also received a consistent support across all our data subsets with recency and monetary appearing in every one of the data subsets.

Prior studies indicate that reviewer characteristics concerning their past records and activity rates on travel websites were also related to review helpfulness [27,32,56]. In our study, the date difference between the latest review and the previous review (RECENCY) and the total number of votes the reviewer has received (MONETARY) are consistently the key aspects for all types of travel. Reviewer characteristics are gaining considerable attention for review helpfulness prediction. Our <sup>fi</sup>ndings help shed some light in

Please cite this article in press as: Y.-H. Hu, et al., The effect of user-controllable <sup>fi</sup>lters on the prediction of online hotel reviews, Inf. Manage. (2017), http://dx.doi.org/10.1016/j.im.2016.12.009

our understanding of how these features are related to hotel review helpfulness.

## 6. Conclusions

Travel websites have become an important source for travelers to plan their trips and share their own experiences. The collective review messages made available through a travel website are like a large database that makes the knowledge accessible to the general public. However, the exponential growth of the available review messages makes it dif<sup>fi</sup>cult for a reader to distill the information for the trip that he or she has in mind. Therefore, identifying helpful reviews accurately becomes an important issue. Added to the complexity is that most travel websites allow readers to <sup>fi</sup>lter review messages. In our case, TripAdvisor.com provides four <sup>fi</sup>lters, including geographic location, season of travel, type of travel, and language. These <sup>fi</sup>lters impose an arti<sup>fi</sup>cial selection of what reviews to show for a given search. As a result, not all reviews receive an equal opportunity to be visible and be voted on for helpfulness. This study collected hotel reviews from TripAdvisor. com to study review helpfulness and its predictors in three groups (namely review quality, review sentiment, and reviewer characteristics) in conjunction with the three <sup>fi</sup>lters mentioned above.

Our work contributes to the literature in three ways. First, this study is one of the <sup>fi</sup>rst to examine the interaction effects among geographic location, season of travel, and travel type. The majority of product review studies overly emphasize on optimizing the best combination of independent variables (IVs), while neglecting the fact that the IVs also interact with each other. If interactions are not taken into account, the true relationship between the selected IVs on review helpfulness may be biased, inaccurate, or even distorted. In the present study, the traditional optimizing approach is still followed, but variables were studied together with interaction effects. The results uncover additional insights that were not available before.

Second, we extended the review diagnosticity-based theory from Mudambi and Schuff [12] with the theoretical constructs from the eWOM and other literatures. Three categories of IVs (review polarity, review structure, and reviewer characteristics) adapted from multiple disciplines were tested in three models (LR, RF, and REPTree). All three models tested in the present study had shown large improvements over Mudambi and Schuff’s original model. As their model was constructed primarily based on variables representing review structure (e.g., review rating and review length), an extension into other relevant aspects of product review provides a better explanatory power to predict review helpfulness. This is consistent with the expectation that reviews for experience goods (such as hotels) need to provide a multifaceted view to meet the needs of the readers in order to receive helpfulness vote.

Third, by dividing the sample into subsamples based on <sup>fi</sup>lters controllable by users and showing strong variations across the subsamples, we were able to demonstrate that the generalizability of the traditional approach, which does not speci<sup>fi</sup>cally distinguish between possible groupings within the overall sample, may fall short for experience goods. This is an important theoretical implication because treating hotel reviews to be homogeneous across geographic locations, travel types, and travel season will likely obscure the true effect on the dependent variable. As a result, models generated for the overall sample will less likely have good predictive power than the individualized version that we provided in the present study. Additionally, by dividing samples based on user-controllable <sup>fi</sup>lters, we were able to shed some light on the boundaries for generalizability based on the individual combinations of user-controllable <sup>fi</sup>lters. For example, sentiment-related variables outweigh reviewer characteristics for business travelers when voting on review helpfulness. In other words, the generalizability of reviewer characteristics in the sample of business travelers may be weak. Table 5 summarizes the baseline models based on the parsimonious principle for model construction, which helps future researchers to expand on their theoretical directions.

Several practical implications may be derived from this study. First, we could construct a smart recommendation system that recommends useful reviews customized to travelers on travel websites. Travelers’ needs can be identi<sup>fi</sup>ed automatically through the search combination of TravelRegion, TravelType, and TimeOf-Year while they browse the travel websites. We predict that this smart recommendation system would provide reviews with higher helpful votes according to review quality, review polarity, and reviewer characteristics as well as the three previously mentioned search combinations. Such a system would conserve time that travelers spend on travel websites searching for helpful reviews for their trips and increase the usability of travel websites if they provide valuable information on the selected hotels. Second, indicators of review helpfulness may also be helpful to hotel managers; they can verify opinions in helpful reviews and subsequently strengthen the advantages and address weaknesses. The crucial advantage of using our proposed algorithm is that hotel managers may not necessarily read every review of their hotels; they may read only the reviews with higher helpful votes for their likely higher impact on sales. Third, we could construct a strategy that provides helpful reviews with higher rankings, thereby providing higher visibility. In general, reviews that have more votes are ranked higher. Such a mechanism disfavors recently published hotel reviews; these reviews will not be placed at the top because of their low rankings and cumulative votes, even if they re<sup>fl</sup>ect the latest hotel information. Without any <sup>fi</sup>ltering, hotel websites usually list the most recent reviews <sup>fi</sup>rst regardless of the quality of review; reviewers must invest extra time to <sup>fi</sup>lter useful information. Considering the aforementioned challenges, travel websites should not rank online reviews simply by publication date or score; rather, they should <sup>fi</sup>lter the most appropriate review of each hotel automatically to reduce the time spent <sup>fi</sup>ltering user information, thereby increasing the chances of users using their web services.

This study is not without limitations and there are still areas that future research may help continue to advance our understanding. First, although this study collected the complete set of reviews for <sup>fi</sup>ve cities from TripAdvisor.com, the reviews from other travel websites such as Hotel.com and Expedia.com were not considered. Since studying the complete set of reviews reduces sampling error compared to the traditional sampling approach, the representation of our sample from TripAdvisor.com may likely be similar to those of other sources of data. Future research may be conducted to con<sup>fi</sup>rm the difference. Second, cultural and societal variations are another area not studied in our research. Although there is a possible difference across cultural and societal norms, it is not readily accessible until the travel websites release traces of clues for a researcher to uncover the difference. Third, generally, reviews posted at an earlier time have a greater chance to be seen and voted on. However, more recent reviews are closer to the current reality, thus offering better realistic insights. Future studies may perform longitudinal observations to monitor how review helpfulness changes over time. It is also recommended to consider variables not studied in the present research. One such extension is to study variables concerning the nature of entertainment offerings and surrounding attractions of the city where a hotel resides. This is especially true when experience goods (such as hotels) are the subject of the study. The literature has been concerning variables relating to hotels, reviews, and reviewers, but very little attention has been paid on the effect of factors other than these three categories. Our work casts one of the early calls by showing that the effects of predictor variables vary between the three geographical regions. Further works in this direction will likely help advance our understanding in situational or nontraditional variables.

## Acknowledgments

This research was supported in part by the Ministry of Science and Technology of the Republic of China (grant numbers MOST 104-2410-H-194-070-MY3 and MOST104-2410-H-194-109). The authors would like to thank Mr. Kuan-Ting Lu for his support on data collection and data preprocessing.

## References

[1] L.J. Harrison-Walker, The measurement of word-of-mouth communication and an investigation of service quality and customer commitment as potential antecedents, J. Serv. Res. 4 (1) (2001) 60–75.

[2] Y. Yoon, M. Uysal, An examination of the effects of motivation and satisfaction on destination lovalty: a structural model Tour, Manage, 26 (2005) 45–56.

[3] C.M.K. Cheung, M.K.O. Lee, What drives consumers to spread electronic word of mouth in online consumer-opinion platforms, Decis. Support Syst. 53 (1) (2012) 218–225.

[4] A.S. Cantallops, F. Salvi, New consumer behavior: a review of research on eWOM and hotels, Int. J. Hosp. Manage. 36 (2014) 41–51.

[5] U. Gretzel, M. Sigala, Z. Xiang, C. Koo, Smart tourism: foundations and developments, Electron. Markets 25 (3) (2015) 179–188.

[6] I. Arsal, K.M. Woosnam, E.D. Baldwin, S.J. Backman, Residents as travel destination information providers: an online community perspective. I. Travel Res. 49 (4) (2010) 400–413.

[7] H. Xie, L. Miao, P.J. Kuo, B.Y. Lee, Consumers’ responses to ambivalent online hotel reviews: the role of perceived source credibility and pre-decisional disposition, Int. J. Hosp. Manage. 30 (2011) 178–183.

[8] H. Lee, A.R. Law, J. Murphy, Helpful reviewers in TripAdvisor: an online travel community, I. Travel Tour, Market, 28 (2011) 675–688.

[9] N. Yacouel, A. Fleischer, The role of cybermediaries in reputation building and price premiums in the online hotel market, J. Travel Res. 51 (2012) 219–226.

[10] A. Ghose, P.G. Ipeirotis, B. Li, Designing ranking systems for hotels on travel search engines by mining user-generated and crowdsourced content, Market. Sci. 31 (3) (2012) 493–520 (INFORMS.).

[11] Y.H. Hu, K. Chen, Predicting hotel review helpfulness: the impact of review visibility, and interaction between hotel stars and review ratings, Int. J. Inf. Manage 36 (6)(2016) 929–944

[12] S.M. Mudambi, D. Schuff, What makes a helpful online review? A study of customer reviews on Amazon.com, Manage. Inf. Syst. Q. 34 (1) (2010) 11.

[13] N. Hu, P. Pavlou, J. Zhang, Can online reviews reveal a product’s true quality? Empirical <sup>fi</sup>ndings and analytical modeling of online word-of-mouth communication, Proceedings of the 7th ACM Conference on Electronic Commerce, New York, USA, 2006.

[14] P. Nelson, Information and consumer behavior, J. Polit. Econ. 78 (1970) 311.

[15] Z. Jiang, I. Benbasat, Virtual product experience: effects of visual and functional control of products on perceived diagnosticity and <sup>fl</sup>ow in electronic shopping, J. Manage. Inf. Syst. 21 (3) (2004) 111–147.

[16] P.M. Herr, F.R. Kardes, J. Kim, Effects of word-of-mouth and product-attribute information on persuasion: an accessibility-diagnosticity perspective, J. Consum, Res, 17 (1991) 454–462.

[17] H. Song, G. Li, Tourism demand modelling and forecasting—a review of recent research, Tour. Manage. 29 (2) (2008) 203–220.

[18] S. Gössling, C.M. Hall, Uncertainties in predicting tourist <sup>fl</sup>ows under scenarios of climate change, Clim. Change 79 (3–4) (2006) 163–173.

[19] J. Rosselló-Nadal, How to evaluate the effects of climate change on tourism, Tour, Manage, 42 (2014) 334–340

[20] C. Goh, Exploring impact of climate on tourism demand, Ann. Tour. Res. 39 (4) (2012) 1859–1883

[21] H.Q. Zhang, N. Kulendran, The impact of climate variables on seasonal variation in Hong Kong inbound tourism demand, J. Travel Res. (2016), doi: http://dx.doi.org/10.1177/0047287515619692.

[22] S.-M. Kim, P. Pantel, T. Chklovski, M. Pennacchiotti, Automatically assessing review helpfulness, Proceedings of the 2006 Conference of Empirical Methods in Natural Language Processing, Sydney, Australia, 2006.

[23] J. Liu, Y. Cao, C.-Y. Lin, Y. Huang, M. Zhou, Low-quality product review detection in opinion summarization, Comput. Ling. (2007) 334–342.

[24] C. Forman, A. Ghose, B. Wiesenfeld, Examining the relationship between reviews and sales: the role of reviewer identity disclosure in electronic markets, Inf. Syst. Res. 19 (3) (2008) 291–313.

[25] Z. Zhang, Weighing stars: aggregating online product reviews for intelligent ecommerce applications, IEEE Intell. Syst. 23 (5) (2008) 42–49.

[26] Y. Liu, X. Huang, A. An, X. Yu, Modeling and predicting the helpfulness of online reviews, Proceedings IEEE International Conference on Data Mining, Pisa, Italy, 2008.

[27] J. Otterbacher, ‘Helpfulness’ in online communities: a measure of message quality, Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, ACM, 2009, pp. 955–964.

[28] M.P. O’Mahony, B. Smyth, A classi<sup>fi</sup>cation-based review recommender, Knowledge-Based Syst. 23 (4) (2010) 323–329.

[29] C.C. Chen, Y.-D. Tseng, Quality evaluation of product reviews using an information quality framework, Decis. Support Syst. 50 (4) (2011) 755–768.

[30] A. Ghose, P.G. Ipeirotis, Estimating the helpfulness and economic impact of product reviews: mining text and reviewer characteristics, IEEE Trans. Knowl. Data Eng. 23 (10) (2011) 1498–1512.

[31] X. Yu, Y. Liu, X. Huang, A. An, Mining online reviews for predicting sales performance: a case study in the movie domain, IEEE Trans. Knowl. Data Eng 24 (2012) 720–734.

[32] T.L. Ngo-Ye, A.P. Sinha, Analyzing online review helpfulness using a regressional relief-enhanced text mining method, ACM Trans. Manage. Inf. Syst. 3 (2) (2012) 10:1–10:20.

[33] Y. Liu, J. Jin, P. Ji, J.A. Harding, R.Y.K. Fung, Identifying helpful online reviews: a product designer’s perspective, Comp. Aided Des. 45 (2) (2013) 180–194.

[34] R. Dong, M. Schaal, M.P. O’Mahony, B. Smyth, Topic extraction from online reviews for classi<sup>fi</sup>cation and recommendation, Third International Joint Conference on Arti<sup>fi</sup>cial Intelligence, Beijing, China, 2013.

[35] T.L. Ngo-Ye, A.P. Sinha, The in<sup>fl</sup>uence of reviewer engagement characteristics on online review helpfulness: a text regression model, Decis. Support Syst. 61 (2014) 47–58.

[36] N. Hu, N.S. Koh, S.K. Reddy, Ratings lead you to the product, reviews help you clinch it?: the mediating role of online review sentiments on product sales, Decis. Support Syst. 57 (2014) 42–53.

[37] S.-Y. Hwang, C.-Y. Lai, J.-J. Jiang, S. Chang, The identi<sup>fi</sup>cation of noteworthy hotel reviews for hotel management, Paci<sup>fi</sup>c Asia J. Assoc. Inf. Syst. (2014).

[38] G. Yin, L. Wei, W. Xu, M. Chen, Exploring heuristic cues for consumer perceptions of online reviews helpfulness: the case of Yelp.com, Proceedings of the 2014 Paci<sup>fi</sup>c Asia Conference on Information Systems, Chengdu, China, 2014.

[39] S. Lee, J.Y. Choeh, Predicting the helpfulness of online reviews using multilayer perceptron neural networks, Expert Syst. Appl. 41 (2014) 3041–3046.

[40] L. Martin, P. Pu, Prediction of helpful reviews using emotions extraction, AAAI Conference on Arti<sup>fi</sup>cial Intelligence Twenty-Eighth AAAI Conference on Arti<sup>fi</sup>cial Intelligence, Quebec, Canada, 2014.

[41] L. Zhu, G. Yin, W. He, Is this opinion leader’s review useful? Peripheral cues for online review helpfulness, J. Electron. Comm. Res. 15 (4) (2014) 267–280

[42] Z. Liu, S. Park, What makes a useful online review?: Implication for travel product websites, Tour. Manage. 47 (2015) 140–151.

[43] D. Weathers, S.D. Swain, V. Grover, Can online product reviews be more helpful? Examining characteristics of information content by product type, Decis. Support Syst, 79 (2015) 12–23.

[44] A.H. Huang, K. Chen, D.C. Yen, T.P. Tran, A study of factors that contribute to online review helpfulness, Comp. Hum. Behav. 48 (2015) 17–27.

[45] S.N. Ahmad, M. Laroche, How do expressed emotions affect the helpfulness of a product review? Evidence from reviews using latent semantic analysis, Int. J. Electron. Comm. 20 (1) (2016) 76–111.

[46] A.Y. Chua, S. Banerjee, Helpfulness of user-generated reviews as a function of review sentiment: product type and information quality, Comp. Hum. Behav. 54 (2016) 547–554.

[47] B. Fang, Q. Ye, D. Kucukusta, R. Law, Analysis of the perceived value of online tourism reviews: in<sup>fl</sup>uence of readability and reviewer characteristics, Tour. Manage. 52 (2016) 498–506.

[48] A. Qazi, K.B.S. Syed, R.G. Raj, E. Cambria, M. Tahir, D. Alghazzawi, A conceptlevel approach to the analysis of online review helpfulness, Comput. Hum. Behav. 58 (2016) 75–81.

[49] X. Wang, H.H. Teo, K.K. Wei, Simultaneity and interactivity of the effects of communication elements on consumers'decision making in ewom systems, J. Electron. Comm. Res. 16 (3) (2015) 153.

[50] M. Li, L. Huang, C.H. Tan, K.K. Wei, Helpfulness of online product reviews as seen by consumers: source and content features, Int. J. Electron. Comm. 17 (4) (2013) 101–136.

[51] R.M. Schindler, B. Bickart, Perceived helpfulness of online consumer reviews: the role of message content and style, J. Consum. Behav. 11 (2012) 234–243.

[52] A.M. Weiss, N.H. Lurie, D.J. MacInnis, Listening to strangers: whose responses are valuable, how valuable are they, and why? J. Market. Res. 45 (2008) 425– 436.

[53] Q. Cao, W. Duan, Q. Gan, Exploring determinants of voting for the helpfulness of online user reviews: a text mining approach, Decis. Support Syst. 50 (2011) 511-521

[54] H. Chen, D. Zimbra, AI and opinion mining, IEEE Intell. Syst. 25 (2010) 74–76.

[55] S. Baccianella, A. Esuli, F. Sebastiani, SentiWordNet 3.0: an enhanced lexica resource for sentiment analysis and opinion mining, The International Conference on Language Resources and Evaluation Valletta Malta 2010

[56] Y. Pan, J.Q. Zhang, Born unequal: a study of the helpfulness of user-generated product reviews, J. Retailing 87 (2011) 598–612.

[57] N. Kor<sup>fi</sup>atis, E. García-Bariocanal, S. Sánchez-Alonso, Evaluating content quality and helpfulness of online product reviews: the interplay of review helpfulness ys, review content, Electron, Comm, Res, Appl, 11 (2012) 205–217

Y.-H. Hu et al. / Information & Management xxx (2016) xxx–xxx

[58] J. Otterbacher, Gender, writing and ranking in review forums: a case study of the IMDb, Knowl. Inf. Syst. 35 (3) (2013) 645–664.

[59] U. Gretzel, K.H. Yoo, Use and impact of online travel reviews, Inf. Commun. Technol. Tour. 2008 (2008) 35–46.

[60] F. Bronner, R. de Hoog, Vacationers and eWOM: who posts, and why, where, and what? J. Travel Res. 50 (1) (2011) 15–26.

[61] E. Parra-López, J. Bulchand-Gidumal, D. Gutiérrez-Taño, R. Díaz-Armas, Intentions to use social media in organizing and taking vacation trips, Comput. Hum. Behav. 27 (2) (2011) 640–654.

[62] P.S. Fader, B.G.S. Hardie, K.L. Lee, RFM and CLV: using iso-value curves for customer base analysis, J. Market. Res. 42 (4) (2005) 415–430.

[63] R. Kahan, Using database marketing techniques to enhance your one-to-one marketing initiatives, J. Cons. Market. 15 (1998) 491–493.

[64] C. Marcus, A practical yet meaningful approach to customer segmentation, J. Consum. Market. 15 (5) (1998) 494–504.

[65] C.D. Manning, M. Surdeanu, J. Bauer, J. Finkel, S.J. Bethard, D. McClosky, The natural language processing toolkit, Proceedings of 52nd Annual Meeting of the Association for Computational Linguistics: System Demonstrations, Baltimore, USA. 2014.

[66] E.A. Smith, J.P. Kincaid, Derivation and validation of the automated readability index for use with technical materials, Hum. Factors: J. Hum. Factors Ergon. Soc. 12 (5) (1970) 457–564.

[67] M. Coleman, T. Liau, A computer readability formula designed for machine scoring, J. Appl. Psychol. 60 (2) (1975) 283–284.

[68] J.P. Kincaid, Computer readability editing system, IEEE Trans. Prof. Commun. 24 (1) (1981) 38-42.

[69] R. Gunning, The fog index after twenty years, J. Bus. Commun. 6 (2) (1969) 3– 13.

[70] G.H. McLaughlin, SMOG grading: a new readability formula, J. Read. 12 (8) (1969) 639–646.

[71] E. Riloff, J. Wiebe, Learning extraction patterns for subjective expressions, Proceedings of the 2003 Conference on Empirical Methods in Natural Language Processing, Stroudsburg, USA, 2003.

[72] J. Wiebe, E. Riloff, Creating subjective and objective sentence classi<sup>fi</sup>ers from unannotated texts, Computational Linguistics and Intelligent Text Processing, Springer, Berlin Heidelberg, 2005, pp. 486–497.

[73] M. Hall, E. Frank, G. Holmes, B. Pfahringer, P. Reutemann, I.H. Witten, The WEKA data mining software, ACM SIGKDD Explor. Newsl. 11 (1) (2009) 10.

[74] T.K. Ho, Random decision forests, Proceedings of 3rd International Conference on Document Analysis and Recognition (vol, 1) Montreal Canada 1995.

[75] R. Diao, Q. Shen, Feature selection with harmony search, IEEE Trans. Syst. Man Cybern. Part B (Cybern.) 42 (6) (2012) 1509–1523.

[76] M. Hu, B. Liu, Mining and summarizing customer reviews, Proceedings of the Tenth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, 2004, pp. 168–177.

Ya-Han Hu is currently an Associate Professor of the Department of Information Management at the National Chung Cheng University, Taiwan. He received a PhD degree in Information Management from the National Central University of Taiwan in 2007. His current research interests include text mining and information retrieval, clinical decision support systems, and recommender systems. His research has appeared in Decision Support Systems, Journal of the American Society for Information Science and Technology, IEEE Transactions on Systems, Man, and Cybernetics, Arti<sup>fi</sup>cial Intelligence in Medicine, Applied Soft Computing, Computers in Human Behavior, Data & Knowledge Engineering, Expert Systems, Knowledge-Based Systems, Information Systems and e-Business Management, Journal of Information Science, Journal of Clinical Epidemiology, Methods of Information in Medicine, Online Information Review, and Journal of Systems and Software.

Kuanchin Chen is a Professor of Computer Information Systems at the Western Michigan University. Dr. Chen’s research interests include electronic business, social networking, project management, privacy & security, online behavioral issues, business analytics, and human–computer interactions. He has published articles in journals and other academic publication outlets, including Information Systems Journal, Decision Support Systems, Information & Management, IEEE Transactions on Systems, Man, and Cybernetics, Internet Research, Journal of Database Management, Communications of the Association for Information Systems, Electronic Commerce Research and Applications, Journal of Global Information Management, DATA BASE for Advances in Information Systems, Decision Sciences Journal of Innovative Education, and many others. Dr. Chen serves on the editoria review boards of several academic journals.

Pei-Ju Lee is currently an Assistant Professor of the Department of Information Management at the National Chung Cheng University, Taiwan. She received her PhD degree in Information Sciences from University of Pittsburgh in 2015. Her current research interests include information fusion, data mining, database management, human-computer interaction, and human factor
