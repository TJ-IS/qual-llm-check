---
otero_id: 13018
otero_key: "JRCBMAQX"
title: "Hybrid collaborative filtering for high-involvement products: A solution to opinion sparsity and dynamics"
authors: "Cuiqing Jiang; Rui Duan; Hemant K. Jain; Shixi Liu; Kun Liang"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.09.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Hybrid collaborative filtering for high-involvement products: A solution to opinion sparsity and dynamics

Cuiqing Jiang <sup>a</sup>, Rui Duan <sup>a,</sup>⁎, Hemant K. Jain <sup>b</sup>, Shixi Liu <sup>a,c</sup>, Kun Liang <sup>a</sup>

<sup>a</sup> School of Management, Hefei University of Technology, No. 193, Tunxi Road, Hefei, Anhui 230009, PR China

<sup>b</sup> Sheldon B. Lubar School of Business, University of Wisconsin–Milwaukee, Milwaukee, WI 53201, United States

<sup>c</sup> School of Computer and Information Engineering, Chuzhou University, Chuzhou, Anhui 239000, PR China

## a r t i c l e i n f o

Article history: Received 28 June 2014 Received in revised form 21 July 2015 Accepted 2 September 2015 Available online 9 September 2015

Keywords: High-involvement products Hybrid collaborative filtering Sparsity problem Online opinion dynamics

## a b s t r a c t

High capital value goods that are purchased only after long and careful consideration, such as a car, truck, appliance (called high-involvement products) are increasingly being purchased online. For these products accurate recommendations are very important. Collaborative filtering (CF) is a commonly used approach for recommending products based on known preferences of similar users. Two challenges that limit the performance of CF in high-involvement products are the ratings' sparsity and dynamics. We use online reviews as an auxiliary information source and design a hybrid CF method to address the sparsity problem. Additionally, we consider the dynamics that may exist in online ratings and reviews. Specifically, we first investigate empirically the evolution of the ratings and reviews over time and sequence. The results show that there are both temporal and sequential dynamics in online ratings, and only temporal dynamics in online reviews. Next, considering these dynamics, we develop techniques to predict missing ratings based on online reviews and product similarities. The sparsity of the User–Item rating matrix is alleviated by filling these predicted ratings. The experiment, based on realworld datasets, demonstrates the superior performance of our recommendation approach for highinvolvement products.

© 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

As an approach to addressing the information overload problem [1], recommender systems (RS) provide personalized product recommendations to consumers based on their needs and interests [2]. RS are helpful in increasing sales, accelerating cross-sell opportunities and improving customer loyalty [3,4]. Collaborative filtering (CF) is a widely used recommendation technique. Although CF has been used in many large commercial sites, it suffers from two challenges: ratings' sparsity [5] and dynamics [6,7]. The former refers to the availability of fewer consumer ratings compared to the number of products and users, leading to a sparse User (U)–Item<sup>1</sup> (I) rating matrix. The latter refers to the fact that early and late adopters of a product have different perspectives on the same product, thus resulting in very different ratings. Both problems affect the calculation of similarities between products or users, and decrease the recommendation performance.

The high-involvement products are defined as high capital value goods that are purchased only after long and careful consideration, such as a car, truck, or appliance. Product involvement refers to a consumer's perceived importance of, and interest in, a product [8], which is a consumer-specific concept [9,10]. A product can also be classified as high or low-involvement based on some of its characteristics such as cost and complexity which contribute to consumer's involvement in the product [8]. Previous research [11,12] suggests that durable products with complex functionality, high price and long life generally have higher levels of consumer involvement in the purchase decision, since a wrong purchase decision leads to a high sunk cost. So, they are typically classified as high-involvement products. On the contrary, for consumable and low-cost products such as groceries, books and CDs, the consequences of making a wrong purchase decision are limited. Thus, consumers generally have low levels of involvement in those purchasing decisions. This simple and feasible way to identify the highinvolvement products has been widely accepted by researchers and practitioners [8,13,14]. Marketing research reveals that consumer information-search behaviors differ markedly between high and lowinvolvement products [8]. For the high-involvement products, consumers typically spend considerable time gathering information to make the right purchase decision. In such cases, accurate recommendations will generate higher consumer satisfaction.

The data sparsity problem described above is especially serious for high-involvement products. Consumers generally don't buy highinvolvement products often, and thus there are fewer purchasing, rating, and review details, for these products. Fig. 1 illustrates U–I rating matrix of high and low-involvement products. From this figure, we can see that a serious sparsity problem exists for high-involvement products (digital SLR cameras) compared with low-involvement products (shoes). In order to generate an accurate recommendation, we need to solve this sparsity problem.

![](/api/attachments/JRCBMAQX/fulltext/images/8fdb2d63a383297bc0edb989b311295d0d37140032b508547c0a3157361014ec.jpg)

![](/api/attachments/JRCBMAQX/fulltext/images/a80d5184783d8c9080cddddb7bb6f706ee3b353a98ffdf6dedbea315155e8f2f.jpg)  
Fig. 1. The User–Item rating matrix. Note: This figure is used to illustrate the difference in rating sparsity between high-involvement products (digital SLR cameras, shown on the left) and low-involvement products (shoes, shown on the right). We select 500 users (vertical axis) and 500 items (horizontal axis) for both types of products. Each box is a snapshot of the User– Item rating matrix and each point represents a rating. nz represents the number of ratings.

Improvements to CF that are helpful in addressing the sparsity problem include hybrid CF [15] that combines CF with other recommendation techniques like content-based filtering (CB) [16]. Online reviews can be used in RS as an auxiliary source [13], since they can help find microadvantages and disadvantages of product features including intangibles that the manufacturer may not mention in their official specifications, such as product quality, design, usability and robustness. These product features are generally hard to measure objectively based on product specifications, yet some important evaluation information about them can be gathered from consumers' reviews. Studies on low-involvement products have revealed the existence of rating<sup>2</sup> dynamics over both time and sequence order [17–20]. However, little research exists on the dynamics of consumers' sentiment in online reviews for high-involvement products.

To address the above research gaps, this paper develops reviewbased hybrid CF for high-involvement products that overcomes the data sparsity problem and considers dynamics of review. We first empirically investigate the evolution of online ratings and reviews over time (temporal dynamics) and sequence (sequential dynamics). The results show that there are both temporal and sequential dynamics in ratings, and only temporal dynamics in reviews of consumers' sentiment on product features. Based on the feature-level sentiment analysis of online reviews, we infer the qualities of product features and construct a dynamic rating matrix. We use this matrix to calculate the similarities between products and predict unknown user ratings. The predicted ratings are filled into the sparse U–I rating matrix so that more accurate recommendation results can be generated by the User-based CF algorithm. The contributions of this paper are: (1) from both ratings and reviews the temporal and sequential dynamics of online opinions are analyzed for high-involvement products; (2) a review-based hybrid CF is designed to overcome the rating sparsity problem of highinvolvement products; (3) the dynamics of online ratings and reviews are considered in the design of the recommendation method to avoid the possible biases.

The paper is organized as follows. In Section 2, we discuss related work on RS for high-involvement products, opinion dynamics and review-based RS. In Section 3, we detail our dataset and preprocessing of the dataset, including review quality filtering and feature-level sentiment analysis. In Section 4, based on the dataset we test the temporal and sequential dynamics of online ratings and reviews. In Section 5, we present our review-based hybrid CF recommendation method. The experiment conducted to evaluate and compare the performance of proposed recommendation approach to other commonly used approaches is presented in Section 6. The paper concludes with implications, limitations and directions for future research in Section 7.

## 2. Related work

Research in economics, marketing and MIS have shown the significant impact of online word of mouth (WOM) on market outcomes (market-level analysis) and consumer purchase decisions (individuallevel analysis) [21]. In the RS area, researchers employ online ratings as a main data source and online reviews as an important auxiliary source to design RS. Additionally, extant research has shown that posting of online WOM is a dynamic process and biases exist in this process. In this section, we first introduce the dynamics in the online WOM posting process and discuss drivers that motivates consumer to post their opinions. Then, we survey RS literature regarding high-involvement products, introduce the sparsity problem, and discuss review-based RS.

## 2.1. The dynamics of online opinions

Several research works have revealed that the average value of online ratings is characterized by a declining or increasing trend [17,18, 22], meaning that early vs. late adopters of a product have different perspectives on the same product. Godes and Silva [17] investigate the evolution of online ratings over time and sequence, and confirm the existence of both types of dynamic process. Two prevailing explanations for the dynamic WOM process have been provided. The first one, provided by Li and Hitt [18], identifies the process as a temporal dynamic one. Their explanation is based on the self-selection of purchase time, i.e., early adopters self-select the products they expect to like. The ratings will increase or decrease over time based on the self-selection bias. Brandes et al. [23] focus on the self-selection of review time after the purchase. They argue that consumer's decision to review or not to review a product is associated with an underlying utility, and the duration of the review latency period is a proxy of this utility. They propose that the selection biases can be corrected by using later reviews. We built on this idea to avoid the rating bias. The second explanation identifies the rating process as a sequential dynamic one. In this view, the existing reviews have an effect on a potential rater's decisions of whether to post and what to post. Moe and Trusov [22] found that (1) a higher average existing rating increases the likelihood of a one, two and three-star rating being posted; (2) the variance of ratings can generate dynamics that encourage subsequent WOM activity. In a follow-up research, Moe and Schweidel [20] identify the selection effect that influences the incidence decision and the adjustment effect that influences the evaluation behavior. Their studies show that (1) positive ratings increase posting incidence, whereas negative ratings discourage posting; (2) less frequent raters are more positive and likely to contribute to rating environment with lower opinion variance, whereas highly active posters are more negative in their evaluations and are more prone to post in an environment with a higher opinion variance. Wu and Huberman [19] present a theory to explain the motivation of consumers to post a review. They consider that opinion expression is costly and a person will only contribute if their gain from expressing an opinion is higher than their cost. They believe that people will derive more utility from the posting if they can influence the overall rating. That is to say, providing another 5-star review after one hundred people have done so may not be worth the cost of submitting a review.

Previous research on the dynamics of online WOM has two main limitations. (1) the analysis and explanation of the dynamics of online WOM are all based on an individual's overall numeric rating, ignoring the reviewer's opinions and sentiments regarding multiple features of the product which can be extracted from online review text; (2) the research and experiments have focused on low-involvement products, such as books [17–19], movies [24] and home products [20,22]. Few research studies have focused on the dynamic review posting process for high-involvement products.

2.2. Recommender systems for high-involvement products and the sparsity problem

Previous research on RS is mainly concentrated on low-involvement products like movies, books, documents, TV programs, music and images [25]. In this paper, we focus on the RS for high-involvement products. As discussed in Section 1, for high-involvement products, since fewer ratings are available, researchers have focused on the sparsity problem [13]. Two categories of approaches have been proposed. The first one tries to improve the traditional memory-based CF. The representative methods in this category include model-based CF [6] and hybrid CF [15]. The second focuses on preference elicitation and decision-making, including critiquing-based RS [26] and utility-based RS [27].

A well-known technique in model-based CF for addressing the sparsity problem is matrix factorization (MF) [28]. MF is a type of latent factor model that tries to explain ratings by characterizing both items and users on fewer factors inferred from the limited number of available ratings [29]. Some representative works that use MF for high-involvement products include [30–33]. Hybrid CF such as [16] is found to be helpful to address the sparsity problem, in which external content information can be used to compute the user and product similarities. The common content is attribute information, such as users' gender, age, hobbies and products' specifications [6]. As an important source, online reviews have attracted the attention of researchers and some review-based RS have been designed. We will discuss them in detail in the next section.

Preference elicitation techniques progressively develop a model of user preferences by engaging users in some kind of “dialog” with the system [34]. Traditional preference elicitation methods include utility function elicitation [35] and analytic hierarchy process (AHP) [36]. However, as most users cannot clearly express their preferences in complex decision environments [37], researchers have begun to focus on the incremental preference elicitation [13], where a user's initial preference is acquired and then the hidden preferences are obtained by stimulating the user to participate in a conversation with the system. The representative application of preference elicitation in RS is critiquingbased RS [26] such as the Findme system [38] and the Dynamiccritiquing agent [39], both of which are designed for highinvolvement products. In addition to preference elicitation, some systems make recommendations based on the multi-attribute utility theory [35], which is called utility-based RS [27]. These systems model the user's preferences as a weighted sum of his (or her) preferences to different product attributes. The products with the highest utility scores are recommended to users [13]. The representative utility-based RS for high-involvement products include [27] and [40].

## 2.3. Review-based recommender systems

There is a growing interest in using online reviews for recommendation. There are two main approaches for designing review-based RS. One approach uses online reviews in recommendation as an external source of information to model the product or user profiles. Aciar et al. [41] were the first to use online reviews in RS. They use reviews to create a product model based on product features, and then recommendations are generated by considering the model and the preferences stated by the current buyer. Terzi et al. [42] use online reviews to model users. They present a hybrid RS which calculates user's similarities based on the content of user reviews. Esparza et al. [43] provide a recommendation method based on the real-time reviews from Twitter.com. They represent both users and products by the terms used in the associative reviews. An information retrieval method is then used to complete the recommendation. Another approach of review-based RS is to use customers' reviews to identify their preferences. Chen and Wang [13,44] attempt to recover each user's preferences by assigning weights to features based on his (or her) reviews. They identify the reviewerlevel preferences by a probabilistic regression model and the clusterlevel preferences by a clustering method based on the latent class regression model. For a target user, they find the cluster with the most relevant reviewers in terms of preference matching degree and their reviewed products, and then derive recommendation candidates. Liu [45] et al. analyze the consumers' reviews and develop two measures: concern and requirement to identify their preferences. They also model the products using online reviews. They make a recommendation based on users' preferences and the product model.

The previous research on review-based RS has two main limitations. (1) As Chen et al. state in [13], few researchers have used the featurelevel review opinions to recommend high-involvement products. Most recommended products, such as movies [5,43,46], books [43], restaurants [45,47] and hotels [48,49], are low-involvement. To the best of our knowledge, the review-based recommendations for high-involvement products include a RS designed by Aciar et al. [41] for cameras, a product-feature based ranking method presented by Zhang et al. [50] for cameras and televisions, and a users' preferences-based recommendation approach proposed by Chen and Wang [13,44] for cameras and laptops. (2) As far as we know, there is no review-based RS considering review dynamics, which may lead to biases in the recommendation results.

## 3. Reviews and ratings of high-involvement products

## 3.1. Dataset and review filtering

The product review data for this research comes from an online WOM website: Buzzillions.com. We selected digital SLR camera as the high-involvement product type to study opinion dynamics and to develop and validate our recommendation algorithm.<sup>3</sup> We crawled the web site to collect products and their reviews that satisfied the following two conditions: (1) the reviews were posted between January 1,

2011 and September 1, 2014, and (2) there were at least 50 reviews for the product. For each type of digital SLR camera that met the above conditions we collected the star rating (an integer number from 1 to 5), the review text, the posting date and the reviewer information. A total of 14,185 reviews and ratings on 103 types of digital SLR camera were collected.<sup>4</sup>

As expected, not all reviews are of high quality. Some reviews are too short to get enough information about product features, or are not easy to read because of spelling or syntax errors. Some reviews are written by reviewers who do not have an adequate understanding of the product. More seriously, some reviews contain fraudulent information. So, it is necessary to conduct a review filtering to remove as many low-quality reviews as possible. We conducted review filtering from two aspects: reviewer credibility and review quality. Buzzillions.com assigns different titles to reviewers based on their profile. For the camera dataset, the titles are: Pro Photographer, Semi-pro Photographer, Casual Photographer, Photo enthusiast and Null. We used these titles to represent reviewer credibility. The reviews from a professional photographer are generally more trustworthy than those from a casual photographer. For the camera dataset, we considered the reviews from Pro Photographer, Semi-pro Photographer, Casual Photographer and Photo enthusiast and excluded the reviews from reviewers without any titles.<sup>5</sup> Additionally, the Buzzillions.com site allows consumers to vote on the reviews by thump-up or thump-down. We can assume that reviews that get more thump-up are of better quality. So, we remove reviews that did not have any thump-up and reviews that had more thump-down. Another aspect of review quality is the readability of the review. Readability is defined as the ease of reading that improves the comprehension of textual materials [51]. We use five characteristics [52] to measure the readability of reviews: number of characters, number of syllables, number of spelling errors, average length of sentence, and SMOG index.<sup>6</sup> Table 1 summarizes the policies used for selecting products and the filtering methods used to remove low-quality reviews. Table 2 presents the detailed information about two datasets after review filtering.

## 3.2. Feature-level opinion mining

We used text mining techniques to identify product features and opinion words corresponding to these features in online reviews. We then grouped related features into topics. The relevant concepts are summarized in Table 3.

Hu and Liu [54] suggested that feature candidates can be collected by identifying the high-frequency nouns.<sup>7</sup> To further filter the feature candidates, we select some features of the product as seeds, and then compute the Point Mutual Information (PMI) value [55] between candidates and seeds. We use curt phrases related to the pros and cons of a product

$$
\text { Grade } = 1. 0 4 3 0 \sqrt {\text { number   of   polysyllables } \times \frac {3 0}{\text { number   of   sentences }}} + 3. 1 2 9 1.
$$

provided by Buzzillions.com as seeds since they may contain many feature words. The number of product features extracted is usually large. If we directly build a rating matrix from these features, the dimension of the matrix will be very high, which, on the one hand, causes complexity in processing and on the other hand leads to a sparse matrix. Additionally, many product features refer to the same aspect of the product. Taking the camera as an example, both running energy and power refer to the battery of the camera. So it is necessary to cluster related features of the product to reduce the dimension of the rating matrix. In this paper, latent Dirichlet allocation (LDA) algorithm [56] is used to cluster features into topics.<sup>8</sup>

To identify opinion words, we extract the words that have met a certain syntactic dependency relationship with the feature words.<sup>9</sup> For example, in a review: “this camera's appearance is very beautiful”, the word “beautiful” is extracted as an opinion word because it has an “nsubj” relation with the word “appearance”. Then, we need to determine opinion word's sentiment polarity and strength. We represent the opinion using five-point scale. A score of 3 means neutral sentiment, and a higher score represents higher positive sentiment strength. Here we adopt SentiWordNet [57] to assess an opinion word's sentiment polarity and strength. SentiWordNet can provide triple polarity scores for each opinion word o: positivity, negativity and objectivity, respectively denoted as: Pos(o), Neg(o) and Obj(o), satisfying the constraint:

$$
\operatorname{Pos} (o) + \operatorname{Neg} (o) + \operatorname{Obj} (o) = 1, 0 \leq \operatorname{Pos} (o), \operatorname{Neg} (o), \operatorname{Obj} (o) \leq 1.\tag{1}
$$

The triple polarity scores can be merged into a sentiment strength value S(o) by the following expression:

$$
S (o) = \operatorname{Neg} (o) \times R _ {\min} + \operatorname{Pos} (o) \times R _ {\max} + O b j (o) \times \frac {R _ {\max} + R _ {\min}}{2}\tag{2}
$$

where $R _ { m i n } = 1$ and $R _ { m a x } = 5$ are respectively the minimum and maximum value of sentiment strength. If there is a negative word before the sentiment word, the sentiment polarity will be reversed.

## 4. Opinion dynamics for high-involvement products

As described in Section 2.1, research on opinion dynamics is concentrated on two aspects: temporal and sequential, and the analysis of dynamics has generally focused on ratings and low-involvement products such as books and movies. We use the data set described above to analyze the temporal and sequential opinion dynamics for highinvolvement products. We first focus on the opinion dynamics at the rating level, and then based on the feature-level sentiment analysis, we analyze the dynamics at the review level

## 4.1. Dynamics of ratings

A rating is the overall evaluation a consumer gives to a product. Most previous studies [17,18,19,22] focusing on low-involvement products found a declining trend of ratings in terms of a temporal and/or a sequential process, and provided various explanations for this. As described in Godes and Silva [17], temporal and sequential dynamics are two different processes and have different implications. A sequential process would suggest that the previous ratings have an impact on an individual's rating, which is consistent with the theories and findings in [19,20,22]. On the other hand, a temporal process would suggest that the rating dynamics are determined by factors outside the rating environment, which is consistent with Li and Hitt's theory [18]. Godes and Silva's research [17] proves the existence of both processes. In this paper, we consider both temporal and sequential rating dynamics for high-involvement products. Specifically, we focus on the following variables for each review:

Product selection and review filtering policies.

<table><tr><td>Product selection policies</td><td colspan="4">The reviews of the product were posted between January 1, 2011 and Sept. 1, 2014The number of reviews for the product is not less than 50.</td></tr><tr><td rowspan="11">Review filtering criteria</td><td rowspan="5">Reviewer credibility</td><td rowspan="5">Reviewer titles</td><td>Pro photographer</td><td>✓</td></tr><tr><td>Semi-pro photographer</td><td>✓</td></tr><tr><td>Casual photographer</td><td>✓</td></tr><tr><td>Photo enthusiast</td><td>✓</td></tr><tr><td>Null</td><td>✘</td></tr><tr><td rowspan="6">Review quality</td><td>Helpfulness voting</td><td colspan="2">Remove reviews that did not have any thump-up and reviews that had more thump-down.</td></tr><tr><td rowspan="5">Review readability</td><td>Number of characters</td><td></td></tr><tr><td>Number of syllables</td><td></td></tr><tr><td>Number of spelling errors</td><td></td></tr><tr><td>Average length of sentence</td><td></td></tr><tr><td>SMOG index</td><td></td></tr></table>

Detailed information about two datasets.

<table><tr><td rowspan="2" colspan="2">Total number of products</td><td>Digital SLR camera</td><td>Laptop computers</td></tr><tr><td>103</td><td>124</td></tr><tr><td rowspan="8">Before filtering</td><td>Total reviews</td><td>14,185</td><td>11,395</td></tr><tr><td>Total users</td><td>11,507</td><td>9033</td></tr><tr><td>Average reviews per product</td><td>137.72 (st. d. = 140.32)</td><td>91.90 (st. d. = 94.47)</td></tr><tr><td>Average reviews per user</td><td>1.23 (st. d. = 1.68)</td><td>1.26 (st. d. = 1.74)</td></tr><tr><td>Average characters per review</td><td>419.45 (st. d. = 525.81)</td><td>360.49 (st. d. = 420.77)</td></tr><tr><td>Average syllables per review</td><td>131.42 (st. d. = 164.20)</td><td>96.62 (st. d. = 113.36)</td></tr><tr><td>Average spell errors per review</td><td>19.23 (st. d. = 24.45)</td><td>17.29 (st. d. = 20.90)</td></tr><tr><td>Average length of sentence</td><td>82.06 (st. d. = 55.98)</td><td>79.31 (st. d. = 70.77)</td></tr><tr><td rowspan="8">After filtering</td><td>Total reviews</td><td>10,221</td><td>8025</td></tr><tr><td>Total users</td><td>7887</td><td>6062</td></tr><tr><td>Average reviews per product</td><td>99.23 (st. d. = 100.72)</td><td>64.72 (st. d. = 69.38)</td></tr><tr><td>Average reviews per user</td><td>1.29 (st. d. = 1.53)</td><td>1.32 (st. d. = 1.57)</td></tr><tr><td>Average characters per review</td><td>500.49 (st. d. = 613.38)</td><td>470.94 (st. d. = 494.49)</td></tr><tr><td>Average syllables per review</td><td>186.59 (st. d. = 211.45)</td><td>156.43 (st. d. = 189.94)</td></tr><tr><td>Average spell errors per review</td><td>6.45 (st. d. = 5.47)</td><td>6.03 (st. d. = 6.48)</td></tr><tr><td>Average length of sentence</td><td>78.33 (st. d. = 80.73)</td><td>81.68 (st. d. = 77.74)</td></tr></table>

RATING number of stars assigned by the reviewer, from 1 to 5;

TPSENTI reviewer's sentiment on the topic of the product;

TIME number of days since the first review was posted for the product;

ORDER position of a review in the sequence of reviews for a given product.<sup>10</sup>

Fig. 2 graphically represents the rating data for all selected products (digital SLR camera) aggregated across TIME and ORDER. Although not the result of a formal model, from Fig. 2 we can see a clear increasing trend of the temporal and sequential dynamics of ratings, which is different from previous studies conducted on low-involvement products [17,22].

We used an ordered logit model to analyze the temporal and sequential dynamics. Specifically, we model the generation of ratings as a function of TIME and ORDER. Similar to Godes and Silva [17], we consider unobserved product-level heterogeneity via product fixed effects. However, different from their work, we do not consider reviewer-level heterogeneity based on the average rating provided by the reviewer, because for the high-involvement product, online rating is sparse and most reviewers only have a handful of ratings. Our ordered logit model is specified by Eq. (3).

$$
u _ {i j} = \beta_ {1} \cdot T I M E _ {i j} + \beta_ {2} \cdot O R D E R _ {i j} + \sum_ {j \in J} \delta_ {j} + \varepsilon_ {i j}\tag{3}
$$

where $u _ { i j }$ is reviewer i's latent evaluation for product j; $\delta _ { j }$ is the fixed effect for product j; $\varepsilon _ { i j }$ is the idiosyncratic errors following a logistic distribution. This model indicates that a reviewer's evaluation of a product can be explained by the product's vertical quality when the reviewer gives the rating and where the rating is located in the review queue. RATING is generated based on the reviewer's latent evaluation and a set of four estimated cutoff values μ , k ∈ {1, 2, 3, 4}

$$
R A T I N G _ {i j} = \left\{ \begin{array}{l l} 1 & \mu_ {i j} <   \mu_ {1} \\ k & \mu_ {i j} \in [ \mu_ {k - 1}, \mu_ {k}),   k \in \{2, 3, 4 \}. \\ 5 & \mu_ {i j} > \mu_ {4} \end{array} \right.\tag{4}
$$

The estimation results are presented in Table 4. From the results, we can see that there are both temporal and sequential dynamics in product ratings: RATING increases in both TIME and ORDER, each conditional on the other. This means that, holding the number of reviews constant, as the elapsed time since the first review was posted increases ratings also increase. Analogously, holding constant the elapsed time from the product's first review, as the number of reviews posted increases the posted rating increases. These results are different from previous studies on rating dynamics for low-involvement products, in which the ratings typically had a declining trend in the temporal and sequential processes.

Table 3  
Concepts used in the feature-level opinion mining.

<table><tr><td>Concepts</td><td>Definitions</td><td>Examples</td></tr><tr><td>Feature</td><td>A product contains components and has attributes, which respectively can have sub-components and sub-attributes. All the components and attributes of a product are collectively referred to as features.</td><td>The components of a camera such as lens, battery, viewfinder; and its attributes, such as brand, size, weight.</td></tr><tr><td>Topic</td><td>A topic describes an aspect of the product, usually containing several features, and can be represented as:  $p = (f_1, ..., f_l)$ , where  $p$  is the topic and  $f_k$  ( $k = 1, ..., l$ ) is the feature.</td><td>The topics of a cameras include hardware, performance, quality, service; the topic hardware contains features such as lens, viewfinder.</td></tr><tr><td>Opinion word</td><td>Opinion words are the words through which users express their positive or negative opinions. These words are usually used to describe some features of the product.</td><td>In a review that states “This mobile phone’s quality is very good” the phrase “very good” is an opinion phrase that describes the feature ‘quality’.</td></tr><tr><td>Feature-opinion-time triplet</td><td>A feature-opinion-time triplet consists of product features, the corresponding opinion word and the time when the evaluation was posted.</td><td>In the above example, &lt;quality, very good, t&gt; is an example of a feature-opinion-time triplet.</td></tr></table>

![](/api/attachments/JRCBMAQX/fulltext/images/b6950f65e22c116e64acaf7b64abec286df7392d75f5513c863d6b370ffd79e7.jpg)  
(a) RATING vs. TIME

![](/api/attachments/JRCBMAQX/fulltext/images/87896db47170f4e7f3cceb4c0419a203a2a1bbeb52d595181b1baf689ae60e0a.jpg)  
(b) RATING vs. TIME

![](/api/attachments/JRCBMAQX/fulltext/images/58ed4aba9f1a9cd683447f2637a685f784edf9bb642e1958e6b4cf56433e5828.jpg)  
(c) RATING vs. ORDER

![](/api/attachments/JRCBMAQX/fulltext/images/7faf19ff87716d45a6d721a85a96a5658ac166bcf644c128ed4a2bd2c381fd68.jpg)  
(d) RATING vs. ORDER  
Fig. 2. Temporal and sequential dynamics of average ratings

## We provide the following explanations for our results

(1) Temporal dynamics: Unlike previous research that focuses on low-involvement products, for high-involvement products, because of their high cost and high risk, consumers are typically sensitive to the product features. According to Li and Hitt's theory [18], in these cases, there is negative self-selection bias, i.e., the earlier consumers tend to give lower ratings. So there is an increasing trend in TIME.

(2) Sequential dynamics: Since the earlier ratings are typically lower, based on the theory proposed by Wu and Huberman [19], reviewers consider whether the impact of the review will outweigh the cost of posting it, so they prefer to submit only higher ratings.

## 4.2. Dynamics of reviews

In the last section, we analyzed opinion dynamics at the rating level and found an increasing trend in both temporal and sequential processes. In this section, we focus on opinion dynamics at the review level and analyze them to determine whether there are similar dynamics for consumers' sentiments on product topics.

Unlike online ratings, consumers' sentiments are not categorical variables, so we use a linear regression model with fix-effect product topic quality to estimate the dynamic effect

$$
T P S E N T I _ {i j} = \beta_ {1} \cdot T I M E _ {i j} + \beta_ {2} \cdot O R D E R _ {i j} + \sum_ {j \in J} \delta j + \varepsilon_ {i j}.\tag{5}
$$

We did the estimation on 32 product topics/subtopics. The results are provided in Table 5. From the results, we can see that (1) there are temporal dynamics in consumer sentiments, and there are few significant dynamics in the sequential process; (2) the features on which consumers have dynamic sentiments are ‘Hard-core’ and ‘Hardware’; (3) unlike the increasing trend of online ratings, consumers' sentiments on ‘Hard-core’ and ‘Hardware’ topics decline in the temporal process.

Table 4  
Estimation results of temporal and sequential dynamics of ratings for Camera.

<table><tr><td></td><td>Ordered logistic regression of RATINGS</td></tr><tr><td>Time</td><td>4.4948E-04***(9.8165E-05)</td></tr><tr><td>Order</td><td>3.7356E-04***(4.3025E-05)</td></tr><tr><td>AIC</td><td>199.85</td></tr><tr><td>RD</td><td>199.73</td></tr></table>

Notes: Standard errors are in parentheses. AIC: Akaike information criterion. RD: Residual deviance. \*\*\* p-Value b 0.001.

Table 5  
Estimation results of the temporal and sequential dynamics of consumers' sentiments for Camera.

<table><tr><td>Topics</td><td>Subtopics</td><td>Time</td><td>Order</td></tr><tr><td rowspan="3">Appearance</td><td>Body</td><td>-5.031E-05 (8.349E-05)</td><td>2.024E-05 (4.270E-05)</td></tr><tr><td>Color</td><td>-3.622E-04 (1.441E-04)*</td><td>1.326E-05 (7.120E-03).</td></tr><tr><td>Overall</td><td>4.697E-05 (1.014E-04)</td><td>2.500E-05 (4.618E-05)</td></tr><tr><td>Design</td><td>Design</td><td>2.479E-04 (2.813E-04)</td><td>-1.785E-04 (1.358E-04)</td></tr><tr><td rowspan="4">Hard-core</td><td>Lens</td><td>-3.018E-05 (7.019E-05).</td><td>4.287E-06 (3.306E-05)</td></tr><tr><td>Sensor</td><td>-4.403E-04 (1.485E-04)**</td><td>-1.748E-04 (7.490E-05)*</td></tr><tr><td>Shutter</td><td>-1.142E-04 (6.334E-05)*</td><td>-1.476E-05 (2.950E-05)</td></tr><tr><td>Viewfinder</td><td>-1.690E-04 (1.806E-04).</td><td>-1.988E-04 (1.056E-04).</td></tr><tr><td rowspan="5">Hardware</td><td>Accessory</td><td>-1.736E-04 (8.764E-04)</td><td>-6.393E-05 (4.289E-04)</td></tr><tr><td>Battery</td><td>-3.400E-04 (1.517E-04)**</td><td>2.485E-04 (7.258E-05)***</td></tr><tr><td>Button</td><td>-3.886E-04 (1.604E-04)**</td><td>1.259E-04 (8.176E-05)</td></tr><tr><td>Card slot</td><td>-4.462E-04 (1.708E-04)***</td><td>2.284E-04 (7.990E-05)**</td></tr><tr><td>Screen</td><td>-1.564E-04 (1.054E-04)**</td><td>-4.292E-05 (5.137E-05)</td></tr><tr><td rowspan="10">Performance</td><td>Control</td><td>-5.006E-05 (1.315E-04)</td><td>9.222E-05 (6.487E-05)</td></tr><tr><td>Customization</td><td>6.518E-04 (5.458E-04)</td><td>7.757E-04 (4.972E-04)</td></tr><tr><td>Durability</td><td>-6.123E-04 (3.871E-04)</td><td>4.808E-04 (1.744E-04)**</td></tr><tr><td>Ease of use</td><td>2.027E-05 (4.936E-05)</td><td>3.411E-05 (2.191E-05)</td></tr><tr><td>Ergonomics</td><td>2.593E-04 (4.443E-04)</td><td>1.654E-04 (2.069E-04)</td></tr><tr><td>Flexibility</td><td>-3.765E-05 (3.346E-04)</td><td>-1.104E-04 (1.541E-04)</td></tr><tr><td>Overall</td><td>5.589E-05 (5.421E-05)</td><td>-3.263E-05 (2.462E-05)</td></tr><tr><td>Portability</td><td>-1.819E-04 (1.590E-04)</td><td>4.677E-05 (7.952E-05)</td></tr><tr><td>Speed</td><td>-9.272E-05 (1.431E-04)</td><td>-1.559E-05 (6.743E-05)</td></tr><tr><td>User interface</td><td>1.512E-04 (3.562E-04)</td><td>-2.125E-04 (1.565E-04)</td></tr><tr><td rowspan="3">Picture and video</td><td>Audio</td><td>-8.941E-05 (4.361E-04)</td><td>1.567E-04 (1.910E-04)</td></tr><tr><td>Picture</td><td>4.315E-05 (3.487E-05)</td><td>-2.573E-05 (1.552E-05)</td></tr><tr><td>Video</td><td>-2.687E-06 (9.700E-05)</td><td>1.468E-05 (4.415E-05)</td></tr><tr><td>Price</td><td>Price</td><td>-1.960E-05 (8.536E-05)</td><td>6.090E-05 (3.933E-05)</td></tr><tr><td rowspan="5">Software</td><td>Exposure</td><td>2.523E-04 (2.190E-04)</td><td>3.580E-05 (1.051E-04)</td></tr><tr><td>Focus</td><td>-1.680E-04 (6.826E-05)*</td><td>8.206E-05 (3.190E-05)*</td></tr><tr><td>Iso</td><td>1.796E-04 (2.224E-04)</td><td>6.151E-05 (1.041E-04)</td></tr><tr><td>Shooting</td><td>-2.995E-05 (8.005E-05)</td><td>2.559E-05 (3.699E-05)</td></tr><tr><td>White balance</td><td>1.887E-04 (2.177E-04)</td><td>1.139E-04 (1.159E-04)</td></tr></table>

Note: Standard errors are in parentheses.  
<sup>.</sup> p b 0.1.  
$\mathsf { p } < 0 . 0 5 .$  
\*\* $\mathsf { p } < 0 . 0 1 .$  
\*\*\* $\begin{array} { r } { \mathsf { p } < 0 . 0 0 1 . } \end{array}$

We provide the following explanations for the results. (1) The temporal dynamics of consumers' sentiments on ‘Hard-core’ and ‘Hardware topics can be explained by the rapid change in hardware technologies in the electronics industry, which might have resulted in a declining trend in consumers' sentiments since better products might have become available as the technology improved. (2) The fact that consumers' sentiments related to most product features don't have significant dynamics whereas online ratings have clear dynamics can be explained by the fact that the overall rating is a single number and is easily influenced by the review environment, whereas writing online reviews needs a consumer to express his (or her) sentiments on specific product topics and their features. Generally speaking, a consumer only comments on the topics he (or she) is familiar with or is an expert on, so the reviewer does not get influenced by review time (temporal dynamics) and review environment (sequential dynamics).

## 5. Review-based hybrid collaborative filtering

In Section 4, based on the digital SLR camera dataset we found the existence of temporal and sequential dynamics of ratings and temporal dynamics of consumers' sentiments on product features. In this section, we present the design of a recommendation method that considers opinion dynamics and rating sparsity. The proposed Review-based Hybrid Collaborative Filtering (RHCF) method is illustrated in Fig. 3.

## 5.1. Dynamic item-topic rating matrix

In RHCF, we use online reviews to compute similarities between products; these similarities are then used to predict unobserved user ratings. Consider the topics, $\mathbf { P } = ( p _ { 1 } , . . . , p _ { \tau } )$ , which are extracted from online reviews. A model of the product is created based on its quality on the above topics. Thus, a product i can be represented as a vector

$$
\mathbf {i} = (r _ {1}, \dots , r _ {\tau}).\tag{6}
$$

Each element $r _ { g } ( g = 1 , . . . , \tau )$ of the above vector represent product i's quality on topic $p _ { g } .$ . We refer to it as product i's topic rating. Repeating this process for all n products we create the Item (I)-Topic (P) rating matrix

$$
R _ {I - P} = (\mathbf {i} _ {1}, \dots , \mathbf {i} _ {n}) = \left[ r _ {i p} \right] _ {n \times \tau} = \left[ \begin{array}{c c c} r _ {1 1} & \dots & r _ {1 \tau} \\ \vdots & \ddots & \vdots \\ r _ {n 1} & \dots & r _ {n \tau} \end{array} \right].\tag{7}
$$

The topic ratings are derived from the consumer's sentiment on product features. Intuitively speaking, if the polarity of the average of all users' sentiments on a feature is positive, then the feature is evaluated positively, and the higher the sentiment strength then the higher the rating. Consider a feature f of product i, if m users' sentiment values on this feature are $( s _ { 1 i f } , . . . , s _ { m i f } )$ , then we define the feature rating r as

$$
r _ {i f} = \frac {1}{m} \sum_ {j = 1} ^ {m} s _ {m i f}.\tag{8}
$$

![](/api/attachments/JRCBMAQX/fulltext/images/95814b35e4d7104668f12c5479a0877b6407979988d2ee7e52e49a8bf71be2e2.jpg)  
Fig. 3. The framework of Review-based Hybrid Collaborative Filtering (RHCF).

Since a topic is made up of several features, the topic rating can be computed by averaging the corresponding feature ratings. For a given topic p of product i, suppose there are μ features, namely $p =$ $( f _ { 1 } , . . . , f _ { \mu } )$ and the ratings corresponding to each feature $f _ { k } \ ( k =$ $1 , . . . , \mu )$ are $r _ { i f _ { k } }$ , then the topic rating $r _ { i p }$ is computed as

$$
r _ {i p} = \frac {1}{\mu} \sum_ {k = 1} ^ {\mu} r _ {i f _ {k}}.\tag{9}
$$

From Section 4, we know that there may be dynamics in a consumer's sentiment on product features. To avoid biases resulting from these dynamics, we divide the review period into several time intervals, and assume that, in a given time interval, consumers' sentiment is relatively stable. We then construct an I–P rating matrix for each of these intervals. Thus, the above I–P rating matrix $R _ { I } - P$ (see Eq. (7)) is expanded to a set of I–P rating matrices

$$
\{R _ {I - P} (t) | t = 1, \dots , T \}\tag{10}
$$

and

$$
R _ {I - P} (t) = (\mathbf {i} _ {1} (t),..., \mathbf {i} _ {n} (t)) = \left[ r _ {i p} (t) \right] _ {n \times \tau} = \left[ \begin{array}{c c c} r _ {1 1} (t) & \dots & r _ {1 \tau} (t) \\ \vdots & \ddots & \vdots \\ r _ {n 1} (t) & \dots & r _ {n \tau} (t) \end{array} \right].\tag{11}
$$

Using the dynamic I–P rating matrices constructed above, we calculate the similarity between product i and j by Pearson correlation coefficient considering the dynamics

$$
\operatorname{sim} ^ {I} (i, j) = \frac {\sum_ {t \in \mathbf {T}} \sum_ {p \in \mathbf {P}} \left[ r _ {i p} (t) - \overline {{r _ {i} (t)}} \right] \left[ r _ {j p} (t) - \overline {{r _ {j} (t)}} \right]}{\sqrt {\sum_ {t \in \mathbf {T}} \sum_ {p \in \mathbf {P}} \left[ r _ {i p} (t) - \overline {{r _ {t} (t)}} \right] ^ {2} \sum_ {t \in \mathbf {T}} \sum_ {p \in \mathbf {P}} \left[ r _ {j p} (t) - \overline {{r _ {j} (t)}} \right] ^ {2}}}\tag{12}
$$

where T is the time period of review; P is the topic set; $\overline { { r _ { i } ( t ) } }$ is the aver-<sup>ð</sup>age of topic ratings of the product i on all topics at time t.

We can then predict unobserved user ratings based on product similarities. However, prior to this, we cluster similar products. This allows us to predict a user rating based on the products that are in the same cluster as the predicted product, which can improve the accuracy of the prediction. We use the K-means clustering method to cluster similar products. The products in the same cluster are represented as $c l u s t e r ( i _ { 1 } , . . . , i _ { \boldsymbol \lambda } )$

## 5.2. The imputation of missing data in user–item rating matrix

In the U–I rating matrix, each user is represented by a row vector of user ratings, that is

$$
\mathbf {u} = (r _ {1}, \dots , r _ {n}).\tag{13}
$$

Then, the rating matrix can be represented as

$$
R _ {U - I} = (\mathbf {u} _ {1}, \dots , \mathbf {u} _ {m}) = [ r _ {u i} ] _ {m \times n} = \left[ \begin{array}{c c c} r _ {1 1} & \dots & r _ {1 n} \\ \vdots & \ddots & \vdots \\ r _ {m 1} & \dots & r _ {m n} \end{array} \right].\tag{14}
$$

From Section $^ { 4 , }$ we find that there is a significant increasing trend in ratings. Because of the sparseness of the U–I rating matrix, we cannot use the technique of dividing the rating matrix into several different rating matrices based on time intervals as was done in the case of reviews to avoid the rating dynamics. We adopt the findings of Brandes et al. in [23] to deal with this problem. They argue that rating bias can be corrected by using the later ratings as proxies for ratings that have not been submitted. So we choose a latency period l and only use the ratings posted after l to avoid rating dynamics. This can be intuitively seen from Fig. 2, where we can see that the average ratings approach a constant after a latency interval, and the dynamics become trivial.

Although this method addresses rating dynamics, it leads to another problem. As discussed before, the U–I rating matrix for the highinvolvement product is inherently sparse. If we ignore the ratings before latent period l, the sparsity problem becomes even more serious. To overcome the sparsity problem, we use the product similarity computed in Section 5.1. Using an approach based on item-based CF, we predict the missing user ratings from the existing ratings and product similarities. We then fill the predicted ratings into the U–I rating matrix to overcome the sparsity.

For a user, let us assume that, among the products rated by him (or her), there are λ products in the same cluster, that is, cluster $( i _ { 1 } , . . . , i _ { \lambda } )$ . If we further assume that this user has no rating for product i and this product is in the same cluster as the above λ products, then the user rating of $r _ { u i _ { s } }$ can be predicted as

$$
\hat {r} _ {u i _ {s}} = \frac {\sum_ {i _ {h} \in c l u s t e r (i _ {1} , \dots , i _ {\lambda})} r _ {u i _ {h}} \times s i m ^ {I} (i _ {h} , i _ {s})}{\sum_ {i _ {h} \in c l u s t e r (i _ {1} , \dots , i _ {\lambda})} s i m ^ {I} (i _ {h} , i _ {s})}\tag{15}
$$

where $s i m ^ { I } ( i _ { h } , i _ { s } )$ is the product similarity between product i<sub>h</sub> and $i _ { s } .$ We regard the above predicted user ratings based on product similarities as intermediate data and fill them in the U–I rating matrix to overcome the data sparsity. Finally, the user-based CF algorithm is used on the filled U–I rating matrix to generate the recommendation results.

As a summary, the Review-based Hybrid Collaborative Filtering (RHCF) algorithm proposed in this paper is shown in Algorithm 1.

Algorithm 1. Review-based Hybrid Collaborative Filtering (RHCF) algorithm.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: User set U, product set I, experiment time period T, User-Item rating matrix  $R_{U-I}$ , and the textual review set Rev.
Output: Top-N recommendation results set  $I_{N}$ .
Begin
1. For each review rev ∈ Rev
2. Extract feature-opinion-time triplets (f, o, t);
3. Add feature f into feature set F;
4. Compute opinion word o's sentiment value s(o);
5. end for
6. Perform topic cluster for feature set F;
7. Select a time interval t;
8. For each time  $t \in T$ 
9. For each product  $i \in I$ 
10. For each topic p ∈ P
11. For each feature  $f \in p$ 
12. Compute product i's rating on feature f at time t by Equation 8;
13. end for
14. Compute product i's rating on topic p at time t by Equation 9;
15. end for
16. end for
17. Construct an Item-Topic rating matrix;
18. end for
19. For each product  $i \in I$ 
20. For each product  $j \in I$ 
21. Compute the product similarity between i and j by Equation 12;
22. end for
23. end for
24. Cluster products using K-means algorithm by product similarities;
25. Select a latency period l;
26. For each  $r_{ui} \in R_{U-I}$ 
27. If  $r_{ui}$  is posted before l
28. Abandon  $r_{ui}$ ;
29. end if
30. If  $r_{ui}$  is null
31. Find the cluster of products that contains i;
32. Compute the predicted rating  $\hat{r}_{ui}$  by Equation 15 and fill  $\hat{r}_{ui}$  into  $R_{U-I}$ ;
33. end if
34. end if
35. Perform User-based CF on the filled  $R_{U-I}$  and choose the Top-N results.
End
</div>

## 6. Experimental study for the evaluation of recommendation method

We prepared two real-world datasets for evaluating the proposed recommendation method: the digital SLR camera dataset and the laptop computer dataset. Both datasets are crawled from Buzzillions.com and pre-processed using procedures described in Section 3.

## 6.1. Baseline methods and evaluation metrics

For the purpose of evaluating the proposed approach using an experimental study, we implemented following three recommendation approaches as baseline methods. The first two approaches are traditional memory-based CF methods that only consider online ratings; the last approach also considers reviews. However, none of the approaches considers rating and review dynamics.

1. User-based Collaborative Filtering (User CF): This method calculates the similarities between users in terms of ratings and recommends products to the target user based on the similar users' ratings.

2. Item-based Collaborative Filtering (Item CF): This method calculates the similarities between products instead of users in terms of ratings, and then recommends products to the target user based on his (her) previous ratings or purchases.

3. Content-based recommendation based on Real-time Web (RTWCB): This is a content-based recommendation approach proposed by Garcia et al. [43]. In this method, the online reviews are used as an indexing and retrieval source for product recommendation.

Specifically, users and products are represented by the terms used in their reviews.

To evaluate the performance of different recommendation methods, we divide the dataset into a training set and a test set. We adopt a predictive accuracy metric mean absolute error (MAE) to compare our method with the User CF and Item CF methods. MAE is defined as

$$
M A E = \frac {\sum_ {i = 1} ^ {N} | p _ {i} - r _ {i} |}{N}\tag{16}
$$

where $p _ { i }$ is the predicted rating for the product i, and r is the real rating. MAE measures the average absolute deviation between a predicted rating and the user's real rating. Since RTWCB creates a Top-N recommendation, we adopt classification accuracy metrics, precision, recall and F1, which are commonly used in the information retrieval field for evaluating this approach. The three measures are defined as

$$
\left\{ \begin{array}{l} P r e c i s i o n = \frac {| T \cap R |}{| R |} \\ \text { Recall } = \frac {| T \cap R |}{T} \\ F 1 = \frac {2 \times \text { Precision } \times \text { Recall }}{\text { Precision } + \text { Recall }} \end{array} \right.\tag{17}
$$

where T is the test dataset and R is the recommended products set. Here the test data set for each user is defined as the set of products for which the user has given a rating of more than three, since on a five-point scale more than three means the user is satisfied with the product.

Although the dataset is already sparse, to conservatively test the performance of our recommendation method in a sparser dataset we modify the dataset by excluding the reviewers who rated more than five products in the training dataset and refer to it as the new-user dataset. We can consider this modified data as a cold start problem, which represents the problem of starting RS with no reviews [58].

## 6.2. Results of experiment

In this section, we first show the recommendation results of our RHCF method. We identify the performance differences of RHCF at different settings. We also compare the recommendation results considering the dynamics of online WOM with those not considering the dynamics. We then present the comparison of our results with the results of three baseline methods: User CF, Item CF and RTWCB. In these comparisons, we consider both the sparsity problem and the cold start problem.

## 6.2.1. Evaluation of the dynamics of online WOM

Our recommendation method considers the dynamics of both online ratings and reviews by including two variants: time latency l for the former dynamics and time interval t for the latter. We first present in Table 6 and Fig. 4 the recommendation performance from testing the two variants, in comparison with not considering the dynamics of online WOM. For the values of l, we use 1 month and 1 quarter, whereas for the values of t, we use 1 month, 1 quarter and 1 year. For each combination of l and t, we conducted a five-fold cross-validation and computed the MAE for each fold. To do the cross-validation, we removed the reviewers who commented on fewer than five products from the training dataset. Then we split the reviews of the rest of the reviewers into five partitions, where four of them become the training dataset and one is test dataset.

From the results of the experiment, we can see that, for both datasets, the best recommendation performance is achieved at $t = 1$ quarter and l = 1 quarter. For the variant time interval t, we find that both small (1 month) and large (1 year) values will cause the recommendation performance to decrease. This is because when t is small, the review data becomes too sparse and we cannot get enough information to infer the product quality; when t is large, there are too few review dynamics to take into account. The situation is similar for the variant time latency l. From Table 6, we can also see that the recommendation performance considering the dynamics of online WOM is significantly better than the performance when dynamics is not considered.

Table 6  
Evaluations on different combinations of time interval t and time latency l.

<table><tr><td>Datasets</td><td>ID</td><td>Dynamics</td><td>MAE 1</td><td>MAE 2</td><td>MAE 3</td><td>MAE 4</td><td>MAE 5</td><td>Average MAE</td></tr><tr><td rowspan="7">Digital SLR Camera</td><td>1</td><td> $t = 1M, l = 1M$ </td><td>1.8452</td><td>1.8672</td><td>1.8663</td><td>1.8163</td><td>1.8155</td><td>1.8421</td></tr><tr><td> $2^{(1,3,4,7)}$ </td><td> $t = 1Q, l = 1M$ </td><td>1.2896</td><td>1.2498</td><td>1.2689</td><td>1.2891</td><td>1.2180</td><td>1.2631</td></tr><tr><td> $3^{(1,4,7)}$ </td><td> $t = 1Y, l = 1M$ </td><td>1.5068</td><td>1.5581</td><td>1.5969</td><td>1.5347</td><td>1.5893</td><td>1.5572</td></tr><tr><td> $4^{(1,7)}$ </td><td> $t = 1M, l = 1Q$ </td><td>1.6687</td><td>1.6371</td><td>1.6394</td><td>1.6743</td><td>1.6698</td><td>1.6579</td></tr><tr><td> $5^{(1,2,3,4,6,7)}$ </td><td> $t = 1Q, l = 1Q$ </td><td>0.9532</td><td>0.9951</td><td>0.9613</td><td>0.9570</td><td>0.9317</td><td>0.9597</td></tr><tr><td> $6^{(1,3,4,7)}$ </td><td> $t = 1Y, l = 1Q$ </td><td>1.2216</td><td>1.2652</td><td>1.2235</td><td>1.2711</td><td>1.2244</td><td>1.2412</td></tr><tr><td> $7^{(1)}$ </td><td>No dynamics</td><td>1.8413</td><td>1.7604</td><td>1.8123</td><td>1.8186</td><td>1.8149</td><td>1.8095</td></tr><tr><td rowspan="7">Laptop</td><td>1</td><td> $t = 1M, l = 1M$ </td><td>2.0815</td><td>2.0906</td><td>2.0127</td><td>2.0913</td><td>2.0632</td><td>2.0679</td></tr><tr><td> $2^{(1,3,4,7)}$ </td><td> $t = 1Q, l = 1M$ </td><td>1.4098</td><td>1.4278</td><td>1.4547</td><td>1.4958</td><td>1.4965</td><td>1.4569</td></tr><tr><td> $3^{(1,4,7)}$ </td><td> $t = 1Y, l = 1M$ </td><td>1.5158</td><td>1.5971</td><td>1.5957</td><td>1.5485</td><td>1.5800</td><td>1.5674</td></tr><tr><td> $4^{(1,7)}$ </td><td> $t = 1M, l = 1Q$ </td><td>1.7142</td><td>1.7422</td><td>1.7916</td><td>1.7792</td><td>1.7959</td><td>1.7646</td></tr><tr><td> $5^{(1,2,3,4,6,7)}$ </td><td> $t = 1Q, l = 1Q$ </td><td>1.0656</td><td>1.0036</td><td>1.0849</td><td>1.0934</td><td>1.0679</td><td>1.0631</td></tr><tr><td> $6^{(1,3,4,7)}$ </td><td> $t = 1Y, l = 1Q$ </td><td>1.3758</td><td>1.3743</td><td>1.3392</td><td>1.3655</td><td>1.3171</td><td>1.3544</td></tr><tr><td> $7^{(1)}$ </td><td>No dynamics</td><td>1.9706</td><td>1.9032</td><td>1.9277</td><td>1.9046</td><td>1.9097</td><td>1.9232</td></tr></table>

Note:  
1. M: month; Q: quarter; Y: year.  
2. The IDs in parentheses indicate the MAE at corresponding parameters is significantly higher (p b 0.05).  
3. In fact, for each combination of time interval t and time latency l, there is another important variant, number of nearest neighbor users K, to be determined. We tuned this variant for each combination of t and l, and got the following optimal numbers: in the digital SLR camera dataset, K = 35 for combination 1, K = 30 for combination 2, 4 and 5, K = 25 for combination 3, 6 and 7; in the laptop dataset, K = 25 for combination 1, 2 and $4 , \mathrm { K } = 3 0$ for combination 3 and 5, and K = 20 for combination 6 and 7.

![](/api/attachments/JRCBMAQX/fulltext/images/dfe908c1f93f5a034b87b364a7edebf04ebc067cc20ecb6f0757ee9671f4c180.jpg)  
Fig. 4. Evaluations on different combinations of time interval t and time latency l.

## 6.2.2. Comparison on the sparsity problem

In this section, we compare the RHCF method with three benchmark methods on both datasets. For comparison with User CF and Item CF, we use the MAE metric. As before, we conducted a five-fold cross-validation and computed the average MAE. The evaluation results are presented at Table 7 and Fig. 5. From the results, we can see that the proposed RHCF method has significantly lower MAE than Item and User CF, indicating a better recommendation performance. At the same time, comparing Item CF with User CF, the former has lower prediction errors, which indicates that Item CF is more effective than User CF in the sparsity environment.

Next, we compare RHCF with RTWCB on both datasets using classification accuracy metrics: precision, recall and F1 value. Since RTWCB produces Top-N recommendations, we rank the results generated by RHCF in terms of predicted ratings and choose the Top-N recommendation. To perform the evaluation, we compute the precision, recall and F1 value for different number of recommended products ranging from 5 to 30. The recommendation performance of the two methods is shown in Table 8 and Fig. 6. The results clearly indicate that, for two datasets of cameras and laptops, RHCF outperforms RTWCB on three accuracy

Comparison of RHCF with Item and User CF.

<table><tr><td>Datasets</td><td>ID</td><td>Methods</td><td>MAE 1</td><td>MAE 2</td><td>MAE 3</td><td>MAE 4</td><td>MAE 5</td><td>Average MAE</td></tr><tr><td>Digital</td><td> $1^{(2,3)}$ </td><td>RHCF</td><td>0.9532</td><td>0.9951</td><td>0.9613</td><td>0.9570</td><td>0.9317</td><td>0.9597</td></tr><tr><td>SLR</td><td> $2^{(3)}$ </td><td>Item CF</td><td>2.1899</td><td>2.1007</td><td>2.1014</td><td>2.1276</td><td>2.1936</td><td>2.1426</td></tr><tr><td>Camera</td><td>3</td><td>User CF</td><td>2.4448</td><td>2.4173</td><td>2.4128</td><td>2.4696</td><td>2.4713</td><td>2.4432</td></tr><tr><td>Laptop</td><td> $1^{(2,3)}$ </td><td>RHCF</td><td>1.0656</td><td>1.0036</td><td>1.0849</td><td>1.0934</td><td>1.0679</td><td>1.0631</td></tr><tr><td></td><td> $2^{(3)}$ </td><td>Item CF</td><td>2.2826</td><td>2.2538</td><td>2.2996</td><td>2.2078</td><td>2.2443</td><td>2.2576</td></tr><tr><td></td><td>3</td><td>User CF</td><td>2.5107</td><td>2.5962</td><td>2.5005</td><td>2.5775</td><td>2.5817</td><td>2.5533</td></tr></table>

Note:  
1. The IDs in parentheses indicate the MAE at corresponding parameters is significantly higher (p b 0.05).  
2. For Item CF and User CF, we also need to determine the number of nearest neighbor users K. We tuned this variant and got the optimal values: in the digital SLR camera dataset, K = 11 for Item CF and K = 25 for User CF: in the laptop dataset, K = 15 for Item CE and K = 20 for User CE

![](/api/attachments/JRCBMAQX/fulltext/images/11a2b28df9fa4c09a3a011f77e64e05d37e54fc60187dccccdb07ba66690d942.jpg)

![](/api/attachments/JRCBMAQX/fulltext/images/987743ed3c31d6ccb7b84c80d1953eb415b2d83fb88ea96665034ffaaa557849.jpg)  
Fig. 5. Comparison of RHCF with Item and User CF.

Table 8  
Comparison of RHCF with RTWCB

<table><tr><td rowspan="3">N</td><td colspan="6">Digital SLR camera</td><td colspan="6">Laptop camera</td></tr><tr><td colspan="3">RHCF</td><td colspan="3">RTWCB</td><td colspan="3">RHCF</td><td colspan="3">RTWCB</td></tr><tr><td>Precision</td><td>Recall</td><td>F1 value</td><td>Precision</td><td>Recall</td><td>F1 value</td><td>Precision</td><td>Recall</td><td>F1 value</td><td>Precision</td><td>Recall</td><td>F1 value</td></tr><tr><td>5</td><td>0.1995</td><td>0.4491</td><td>0.2763</td><td>0.1271</td><td>0.3137</td><td>0.1809</td><td>0.2147</td><td>0.4648</td><td>0.2937</td><td>0.1321</td><td>0.3243</td><td>0.1877</td></tr><tr><td>10</td><td>0.1174</td><td>0.5483</td><td>0.1934</td><td>0.0821</td><td>0.3977</td><td>0.1361</td><td>0.1401</td><td>0.5761</td><td>0.2254</td><td>0.0948</td><td>0.4163</td><td>0.1544</td></tr><tr><td>15</td><td>0.0692</td><td>0.6301</td><td>0.1247</td><td>0.0482</td><td>0.4639</td><td>0.0873</td><td>0.0734</td><td>0.6217</td><td>0.1313</td><td>0.0449</td><td>0.5754</td><td>0.0833</td></tr><tr><td>20</td><td>0.0528</td><td>0.7138</td><td>0.0983</td><td>0.0216</td><td>0.5736</td><td>0.0416</td><td>0.0539</td><td>0.7211</td><td>0.1003</td><td>0.0293</td><td>0.6482</td><td>0.0561</td></tr><tr><td>25</td><td>0.0381</td><td>0.7461</td><td>0.0725</td><td>0.0091</td><td>0.6681</td><td>0.0180</td><td>0.0409</td><td>0.7793</td><td>0.0777</td><td>0.0113</td><td>0.7015</td><td>0.0222</td></tr><tr><td>30</td><td>0.0301</td><td>0.7992</td><td>0.0580</td><td>0.0069</td><td>0.7153</td><td>0.0137</td><td>0.0287</td><td>0.8126</td><td>0.0554</td><td>0.0081</td><td>0.7541</td><td>0.0160</td></tr></table>

Note:

1. N is the number of recommended products.

measures at different recommendation-list sizes. From these results, we can see that the best recommendation performance appears at N = 5 for both recommendation methods and both datasets. The size of the test dataset is relatively small since for high-involvement products sufficient number of ratings are generally not available. Therefore, as the number of recommended products, N, increases, there is a larger decrease in rate of precision than the increase in rate of recall. As the harmonic mean of precision and recall, F1 is always maximum at N = 5.

## 6.2.3. Comparison on the cold start problem

To evaluate the performance of various recommendation methods for the cold start problem, we conducted the experiment using the new-user dataset. Since users in this dataset do not review more than five products, we cannot perform a five-fold cross-validation for RHCF, User CF and Item CF. We conducted the experiment using the entire data for both products and the results are presented in Table 9. From the results, we can clearly see that RHCF method outperforms the other two recommendation methods, Item CF and User CF, based on the new-user dataset. When comparing experimental results of new users and normal users, we see that recommendation accuracy for new users is commonly lower than those for normal users. However, we can further observe that the increase in MAE of the RHCF method is much lower than the other two approaches. This proves that RHCF is also helpful for the cold start problem.

Digital SLR Camera  
![](/api/attachments/JRCBMAQX/fulltext/images/9e19ca8a44a094e19b6051e18da59fd470720634039fbc77407b329a6d4f265c.jpg)

![](/api/attachments/JRCBMAQX/fulltext/images/449b664f49b2b16ec5c533075488f719ce63a3d48d5663a1dba416ed4fe55310.jpg)

Laptop Computer  
![](/api/attachments/JRCBMAQX/fulltext/images/f03ea7394f0fe1f63c18183eaf09c90e47c019a832bb5ba326fca7c7ae0866fb.jpg)

![](/api/attachments/JRCBMAQX/fulltext/images/b096fec04c15428ace7bc981c1ad948af8e7d688039bddfb07a2bf3d1244fd53.jpg)  
Fig. 6. Comparison of RHCF and RTWCB.

Table 9  
MAE for normal users and new users.

<table><tr><td>Dataset</td><td>Methods</td><td>Normal user</td><td>New user</td><td>MAE increase</td><td>Increase percentage</td></tr><tr><td rowspan="3">Digital SLR camera</td><td>RHCF</td><td>0.9597</td><td>1.1783</td><td>0.2186</td><td>22.78%</td></tr><tr><td>Item CF</td><td>2.1426</td><td>2.8294</td><td>0.6868</td><td>32.05%</td></tr><tr><td>User CF</td><td>2.4432</td><td>3.3862</td><td>0.9430</td><td>38.60%</td></tr><tr><td rowspan="3">Laptop</td><td>RHCF</td><td>1.0631</td><td>1.3633</td><td>0.3002</td><td>28.24%</td></tr><tr><td>Item CF</td><td>2.2576</td><td>2.9573</td><td>0.6997</td><td>30.99%</td></tr><tr><td>User CF</td><td>2.5533</td><td>3.4617</td><td>0.9084</td><td>35.58%</td></tr></table>

We now compare RHCF with RTWCB using the new-user dataset based on precision, recall and F1 values. As shown in previous findings, we directly test the recommendation performance at N = 5. The experimental results are detailed in Table 10. This table clearly shows that RHCF performs better than RTWCB for both datasets in precision, recall and F1. Comparing Table 10 with Table 8 we see that accuracy decrease (only in F1). From Table 11, we can see that the decrease in accuracy for the RHCF is lower than with RTWCB, which proves that the RHCF method is more efficient than RTWCB at the cold start problem.

## 7. Implications, limitations, and future research

Accurate recommendations on high-involvement products like cars, cameras, computers, and TVs to customers are very important since these products are increasingly being purchased on-line, have higher cost and carry significant risks to customers in the case of a wrong decision. Additionally, these products have longer life so customers have to live with their choice for a longer period. Because of these reasons, customers are much more careful in making purchase decisions for these products. Thus, online retailers are increasingly focusing on providing accurate recommendations for these kinds of products. However, most prevailing recommendation techniques such as collaborative filtering (CF) do not work well for high-involvement products. This is because of the sparsity of ratings available for these types of products resulting from relatively infrequent purchase of these products by consumers. Additionally, the ratings and reviews provided by consumers on these products significantly vary over time because of self-selection biases and the impact of existing ratings and reviews. In this paper, we first empirically verified the existence of opinion dynamics for highinvolvement products; then, we designed a recommendation approach that considered opinion dynamics and addressed the rating sparsity problem of high involvement products. Our approach achieved better performance than three baseline methods used for comparison. The findings of this research have several important implications for research and practice.

With respect to the implications for research, this paper addresses an important problem of recommendation system for high involvement products. As use of e-commerce expands, an increasing number of the complex high value products typically known as high-involvement products are being purchased online. However, research on recommender systems for these high-involvement products has been lacking. This paper addressed an important problem in the design of recommender systems for these products, namely the rating sparsity problem. Additionally, based on the data collected for two high-involvement products namely digital SLR camera and laptop computers we discovered opinion dynamics in online ratings and reviews. Thus, this research has important implications for researchers interested in opinion dynamics and recommendation systems. This research suggests that researcher consider product type as an important factor in developing RS. The empirical results described in Section 4 show that rating dynamics of high-involvement products have an opposite trend (increasing) compared to the previous research on low-involvement products (decreasing). We ascribe this phenomenon to consumers' sensitivity to high-involvement products, which results from high cost, complex functionality and durability of these products. Additionally, the dynamics in reviews are very different from those in ratings. Our findings show that there are both temporal and sequential dynamics in ratings. However, only temporal dynamics exist for some specific features (only ‘hard-core’ and ‘hardware’ topics in the camera dataset) in reviews. So we argue that, compared with online ratings, reviews are a little more objective and rational content source with fewer dynamic biases, and they more accurately reflect product feature quality. For researchers interested in RS, this paper shows that online reviews can be a reliable source to compute product similarities, which is helpful in addressing sparsity problem, and considering opinion dynamics so more accurate recommendation can be generated.

Table 10  
Experiment results of RHCE and RTWCB in new-user dataset

<table><tr><td rowspan="2">Dataset Algorithm</td><td colspan="3">Digital SLR camera</td><td colspan="3">Laptop</td></tr><tr><td>Precision</td><td>Recall</td><td>F1</td><td>Precision</td><td>Recall</td><td>F1</td></tr><tr><td>RHCF</td><td>0.1021</td><td>0.4012</td><td>0.1628</td><td>0.1295</td><td>0.4268</td><td>0.1987</td></tr><tr><td>RTWCB</td><td>0.0547</td><td>0.1073</td><td>0.0725</td><td>0.0501</td><td>0.1167</td><td>0.0701</td></tr></table>

Table 11  
F1 value for normal users and new users.

<table><tr><td>Dataset</td><td>Methods</td><td>Normal user</td><td>New user</td><td>F1 decrease</td><td>Decrease percentage</td></tr><tr><td rowspan="2">Digital SLR camera</td><td>RHCF</td><td>0.2763</td><td>0.1628</td><td>0.1135</td><td>41.08%</td></tr><tr><td>RTWCB</td><td>0.1809</td><td>0.0725</td><td>0.1084</td><td>59.95%</td></tr><tr><td rowspan="2">Laptop</td><td>RHCF</td><td>0.2937</td><td>0.1987</td><td>0.0950</td><td>32.35%</td></tr><tr><td>RTWCB</td><td>0.1877</td><td>0.0701</td><td>0.1176</td><td>62.66%</td></tr></table>

The implications of this research for practice are quite significant. With the growth of e-commerce, more and more high-involvement products are sold online. Accurate recommendation is a major differentiator of e-commerce from the brick and mortar stores and is also an important differentiator from other e-commerce sites. One of the important factors that contributed to the success of sites like Amazon.com, Netflix.com, and Hotels.com are their recommendation algorithms. This paper presents a practical way of deriving high quality recommendations for high-involvement products for which many ratings are not available and there is dynamism in the opinion. This paper addressed these two important problems and presented an approach that performed significantly better than the popularly used approaches. Furthermore, our method, RHCF, addresses the sparsity problem. Even if the recommendations are not for high-involvement products, as long as the rating sparsity exists, our method can be used.

However, the findings of this work have some limitations. We collected review and rating data from one review site: Buzzillions.com. Even though this is a popular review site, we cannot claim that reviews at other sites – especially sites that also sell products – will have the same characteristics. Second we validated our approach on highinvolvement products: digital SLR camera and laptop. However, the applicability to other types of products and especially complex services like insurance needs to be tested.

Future work needs to consider some products where the technol ogy is not changing very fast. Also the validity of the approach for services, especially high-end long-impact expensive services, needs to be tested. In addition, results needs to be validated with data collected from other review sites, especially sites like Amazon.com which are also involved in selling the products. Another fruitful area of research is to consider the impact of providing incentives to the reviewers. How incentives will impact the quality of a review and bias it may create will be an interesting areas to focus on. Lastly we need to close the loop which means to study the impact of recommendations provided based on the algorithm on the purchase behavior of customers. It will be very interesting to see how recommendations and the disclosure about how recommendations were derived impact the behavior of customers.

## Acknowledgments

This work was supported by the National Natural Science Foundation of China (Grant No. 71331002 and Grant No. 71571059), Specialized Research Fund for the Doctoral Program of the Ministry of Education (Grant No. 20120111110027) and Fund for Humanities and Social Science Fund Research Planning of the Ministry of Education (Grant No. 13YJA630037 and Grant No. 15YJA630010).

## References

[1] T.P. Liang, H.J. Lai, Y.C. Ku, Personalized content recommendation and user satisfaction: theoretical synthesis and empirical findings, Journal of Management Information Systems 23 (2007) 45–70.

[2] G. Adomavicius, A. Tuzhilin, Toward the next generation of recommender systems: a survey of the state-of-the-art and possible extensions, IEEE Transactions on Knowledge and Data Engineering 17 (2005) 734–749.

[3] D. Fleder, K. Hosanagar, Blockbuster culture's next rise or fall: the impact of recommender systems on sales diversity, Management Science 55 (2009) 697–712.

[4] T.P. Liang, H.Y. Chen, T. Du, E. Turban, Y. Li, Effect of personalization on the perceived usefulness of online customer services: a dual-core theory, Journal of Electronic Commerce Research 13 (2012) 275–288.

[5] Y. Moshfeghi, B. Piwowarski, J.M. Jose, Handling data sparsity in using emotion and semantic based features, Proceedings of the 34th international ACM SIGIR conference on Research and development in Information Retrieval, ACM 2011, pp. 625–634.

[6] Y. Shi, M. Larson, A. Hanjalic, Collaborative filtering beyond the user-item matrix: a survey of the state of the art and future challenges, ACM Computing Surveys (CSUR) 47 (2014) 3.

[7] Y. Koren, Collaborative filtering with temporal dynamics, Communications of the ACM 53 (4) (2010) 89–97.

[8] B. Gu, J. Park, P. Konana, Research note: the impact of external word-of-mouth sources on retailer sales of high-involvement products. Information Systems Research 23 (2012) 182 196.

[9] R.L. Celsi, J.C. Olson, The role of involvement in attention and comprehension processes, Journal of Consumer Research (1988) 210–224.

[10] J.L. Zaichkowsky, Measuring the involvement construct, Journal of Consumer Research (1985) 341–352.

[11] W.D. Hoyer, D.J. MacInnis, Consumer Behavior, Cengage Learning, 2008

[12] J.P. Peter, L.X. Tarpey Sr., A comparative analysis of three consumer decision strategies, Journal of Consumer Research (1975) 29–37.

[13] L. Chen, F. Wang, Preference-based clustering reviews for augmenting e-commerce recommendation, Knowledge-Based Systems 50 (2013) 44–59.

[14] M.Y. Kiang, Q. Ye, Y. Hao, M. Chen, Y. Li, A service-oriented analysis of online product classi cation methods, Decision Support Systems 52 (2011) 28 39.

[15] Y. Chen, M. Yu, A Hybrid Collaborative Filtering Algorithm Based on User–Item, 2010 International Conference on Computational and Information Sciences (ICCIS) IFFE 2010, pp. 618–621.

[16] P. Melville, R.J. Mooney, R. Nagarajan, Content-boosted collaborative filtering for improved recommendations, AAAI/IAAI (2002) 187–192.

[17] D. Godes, J.C. Silva, Sequential and temporal dynamics of online opinion, Marketing Science 31 (2012) 448–473.

[18] X. Li, L.M. Hitt, Self-selection and information role of online product reviews, Information Systems Research 19 (2008) 456–474.

[19] F. Wu, B.A. Huberman, How public opinion forms, Internet and Network Economics. , Springer, 2008 334–341.

[20] W.W. Moe, D.A. Schweidel, Online product opinions: incidence, evaluation, and evolution. Marketing Science 31. (2012) 372–386

[21] C.M. Cheung, D.R. Thadani, The impact of electronic word-of-mouth communication: a literature analysis and integrative model, Decision Support Systems 54 (2012) 461-470

[22] W.W. Moe, M. Trusov, The value of social dynamics in online product ratings forums, Journal of Marketing Research 48 (2011) 444–456.

[23] L. Brandes, D. Godes, D. Mayzlin, Controlling for self-selection bias in customer reviews Working Paper, 2013

[24] M. Sangkil, P.K. Bergey, D. Iacobucci, Dynamic effects among movie ratings, movie revenues, and viewer satisfaction, Journal of Marketing 74 (1) (2010) 108–121.

[25] D.H. Park, H.K. Kim, I.Y. Choi, J.K. Kim, A literature review and classification of recommender systems research, Expert Systems with Applications 39 (2012) 10059–10072.

[26] L. Chen, P. Pu, Critiquing-based recommenders: survey and emerging trends, User Modeling and User-Adapted Interaction 22 (2012) 125–150.

[27] S. Huang, Designing utility-based recommender systems for e-commerce: evaluation of preference-elicitation methods, Electronic Commerce Research and Applications 10 (2011) 398–407.

[28] Y. Koren, R. Bell, C. Volinsky, Matrix factorization techniques for recommender systems, Computer 42 (2009) 30–37.

[29] X. Su, T.M. Khoshgoftaar, A survey of collaborative filtering techniques, Advances in artificial intelligence (2009) 4.

[30] M. Jamali, M. Ester, A transitivity aware matrix factorization model for recommendation in social networks, IJCAI (2011) 2644–2649.

[31] H. Ma, D. Zhou, C. Liu, M.R. Lyu, I. King, Recommender systems with social regularization Proceedings of the fourth ACM international conference on Web search and data mining, ACM 2011, pp. 287–296.

[32] Š. Pero, T. Horváth, Opinion-driven matrix factorization for rating prediction, User Modeling, Adaptation, and Personalization. , Springer, 2013 1–13.

[33] J. Liu, C. Wu, W. Liu, Bayesian probabilistic matrix factorization with social relations and item contents for recommendation, Decision Support Systems 55 (2013) 838–850.

[34] L. Chen, P. Pu, Survey of preference elicitation methods, Ecole Politechnique Federale de Lausanne (EPFL) Technigual Report, Lausanne, Switzerland. 2004

[35] G.W. Torrance, Decisions with multiple objectives: preferences and value tradeoffs, Health Services Research 13 (1978) 328.

[36] T.L. Saaty, A scaling method for priorities in hierarchical structures, Journal of Mathematical Psychology 15 (1977) 234–281.

[37] P. Viappiani, B. Faltings, P. Pu, Preference-based search using example-critiquing with suggestions, Journal of Artificial Intelligence Research (JAIR) 27 (2006) 465–503.

[38] R.D. Burke, K.J. Hammond, B. Yound, The FindMe approach to assisted browsing, IEEE Expert 12 (1997) 32–40

[39] J. Reilly, K. McCarthy, L. McGinty, B. Smyth, Incremental critiquing, Knowledge-Based Systems 18 (2005) 143–151.

[40] M. Stolze, M. Ströbel, Dealing with learning in ecommerce product navigation and decision support: the teaching salesman problem, Proceedings of the Second Interdisciplinary World Congress on Mass Customization and Personalization, Citeseer, 2003.

[41] S. Aciar, D. Zhang, S. Simoff, J. Debenham, Informed recommender: basing recommendations on consumer product reviews, Intelligent Systems, IEEE 22 (2007) 39–47.

[42] M. Terzi, M.-A. Ferrario, J. Whittle, Free text in user reviews: their role in recommender systems, Workshop on Recommender Systems and the Social Web at the 5th ACM International Conference on Recommender Systems (RecSys' 11) 2011, pp. 45–48.

[43] S. Garcia Esparza, M.P. O'Mahony, B. Smyth, Mining the real-time web: a novel approach to product recommendation, Knowledge-Based Systems 29 (2012) 3–11.

[44] F. Wang, L. Chen, Recommendation based on mining product reviewers' preference similarity network, Proceedings of 6th SNAKDD workshop 2012, p. 166.

[45] H. Liu, J. He, T. Wang, W. Song, X. Du, Combining user preferences and user opinions for accurate recommendation, Electronic Commerce Research and Applications 12 (2013) 14–23.

[46] N. Jakob, S.H. Weber, M.C. Müller, I. Gurevych, Beyond the stars: exploiting free-text user reviews to improve the accuracy of movie recommendations. Proceedings of the 1st international CIKM workshop on Topic-sentiment analysis for mass opinion. ACM 2009, pp. 57–64

[47] G. Ganu, Y. Kakodkar, A. Marian, Improving the quality of predictions using textual information in online user reviews, Information Systems 38 (2013) 1–15.

[48] N. Hariri, Y. Zheng, B. Mobasher, R. Burke, Context-aware recommendation based on review mining, General Co-Chairs2011 27.

[49] A. Levi, O. Mokryn, C. Diot, N. Taft, Finding a needle in a haystack of reviews: cold start context-based hotel recommender system, Proceedings of the sixth ACM conference on Recommender systems, ACM 2012, pp. 115–122.

[50] K. Zhang, R. Narayanan, A. Choudhary, Voice of the customers: mining online customer reviews for product feature-based ranking, Proceedings of the 3rd conference on Online social networks, USENIX Association 2010, p. 11-11.

[51] N. Hu, I. Bose, N.S. Koh, et al., Manipulation of online reviews: an analysis of ratings, readability, and sentiments, Decision Support Systems 52 (3) (2012) 674–684.

[52] A. Ghose, P.G. Ipeirotis, B. Li, Designing ranking systems for hotels on travel search engines by mining user-generated and crowdsourced content, Marketing Science 31 (3) (2012) 493–520.

[53] S. White, The 2003 national assesement of adult literacy (NAAL). Technical Report NCES, Center for Education Statistics (NCES), Institute of Education Sciences, U.S. Department of Education, Washington, DC.

[54] M. Hu, B. Liu, Mining and summarizing customer reviews, Proceedings of the tenth ACM SIGKDD international conference on Knowledge discovery and data mining, ACM 2004, pp. 168–177.

[55] P.D. Turney, Thumbs up or thumbs down?: semantic orientation applied to unsupervised classification of reviews, Proceedings of the 40th annual meeting on association for computational linguistics, Association for Computational Linguistics 2002, pp. 417–424.

[56] D.M. Blei, A.Y. Ng, M.I. Jordan, Latent Dirichlet allocation, Journal of Machine Learning Research 3 (2003) 993–1022

[57] A. Esuli, F. Sebastiani, Sentiwordnet: a publicly available lexical resource for opinion mining, Proceedings of LREC 2006, pp. 417–422.

[58] Z. Huang, H. Chen, D. Zeng, Applying associative retrieval techniques to alleviate the sparsity problem in collaborative filtering, ACM Transactions on Information Systems (TOIS) 22 (2004) 116–142.

![](/api/attachments/JRCBMAQX/fulltext/images/4e9dcaf7919e43741325d92f8c81c9f678f9da850c25dde3ee9d7f6ab2d9d2d1.jpg)  
Dr. Cuiqing Jiang is a professor in School of Management, Hefei University of Technology. He received his PhD degree in 2007 from Hefei University of Technology. His research interests include Knowledge Management. Business Intelligence, Management Information Systems, and IT Project Management.

![](/api/attachments/JRCBMAQX/fulltext/images/ae64015ccbe4bf776e7fbd68a744cc20a3ff098ccbcf0eeff80490f284d39530.jpg)

Shixi Liu is a teacher in School of Computer and Information Engineering at Chuzhou University, and a doctoral student in School of Management at Hefei University of Technology. His research interests include online social networks and trust analysis.

![](/api/attachments/JRCBMAQX/fulltext/images/70dd482a2095344a329fcd4ed11c33a724d846ad6d59e9010bf52791e1424910.jpg)

Mr. Rui Duan is a doctoral student in School of Management at Hefei University of Technology. His research interests include online reviews analysis and recommendation systems.

![](/api/attachments/JRCBMAQX/fulltext/images/6e4b103bac63ebd8b3346ed36173031a68f1af87e9ffe8092cd93d44ddc93577.jpg)

Mr. Kun Liang is a doctoral student in School of Management at Hefei University of Technology. His research interests include social media analysis and business intelligence.

![](/api/attachments/JRCBMAQX/fulltext/images/ed9b249d3ac2baa85d8b7407ba21a34d551f827525d8819d41cea2a68f0d55ee.jpg)

Dr. Hemant K. Jain is a professor in Sheldon B. Lubar School of Business, University of Wisconsin–Milwaukee. He received his PhD degree from Lehigh University. His current interests include development of systems to support real time enterprises which have situational awareness, can quickly sense-and-respond to opportunities and threats, and can track-and-trace important items.
