---
otero_id: 10826
otero_key: "XGK2GVCE"
title: "The influence of reviewer engagement characteristics on online review helpfulness: A text regression model"
authors: "Thomas L. Ngo-Ye; Atish P. Sinha"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.01.011"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The in<sup>fl</sup>uence of reviewer engagement characteristics on online review helpfulness: A text regression model<sup>☆</sup>

Thomas L. Ngo-Ye <sup>a,1</sup>, Atish P. Sinha <sup>b,</sup>⁎

<sup>a</sup> School of Business, Dalton State College, Dalton, GA 30720, United States

<sup>b</sup> Sheldon B. Lubar School of Business, University of Wisconsin-Milwaukee, Milwaukee, WI 53201–0742, United States

## a r t i c l e i n f o

Article history: Received 18 March 2013 Received in revised form 7 January 2014 Accepted 17 January 2014 Available online 25 January 2014

Keywords: Online review Text regression Vector space model Reviewer engagement characteristics RFM analysis

## a b s t r a c t

The era of Web 2.0 is witnessing the proliferation of online social media platforms, which develop new business models by leveraging user-generated content. One rapidly growing source of user-generated data is online reviews, which play a very important role in disseminating information, facilitating trust, and promoting commerce in the e-marketplace. In this paper, we develop and compare several text regression models for predicting the helpfulness of online reviews. In addition to using review words as predictors, we examine the in<sup>fl</sup>uence of reviewer engagement characteristics such as reputation, commitment, and current activity. We employ a reviewer's RFM (Recency, Frequency, Monetary Value) dimensions to characterize his/her overall engagement and investigate if the inclusion of those dimensions helps improve the prediction of online review helpfulness. Empirical <sup>fi</sup>ndings from text mining experiments conducted using reviews from Yelp and Amazon offer strong support to our thesis. We <sup>fi</sup>nd that both review text and reviewer engagement characteristics help predict review helpfulness. The hybrid approach of combining the textual features of bag-of-words model and RFM dimensions produces the best prediction results. Furthermore, our approach facilitates the estimation of the helpfulness of new reviews instantly, making it possible for social media platforms to dynamically adjust the presentation of those reviews on their websites.

© 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

In the era of Web 2.0, emerging online social media platforms build new business models based on their capabilities for leveraging usergenerated content. Online platforms collect, aggregate, process, and present user-contributed information, which has an important bearing on product preferences and company image [4]. Online social media afford consumers the opportunity to voice their opinions and learn from their peers on products and services of interest. This new channel of user-generated information greatly empowers the customers, who engage in the activities facilitated by the online platforms [52]. Online platforms employ and apply text mining algorithms, which can help unearth new knowledge about not only customer behavior, but also about customer attitude and sentiment.

While there are many forms of user-generated content, reviews still constitute the bulk of user-generated content [20]. Online customer reviews are “a type of product information created by users based on personal usage experience” ([5], p. 477) or “peer-generated product evaluations posted on company or third party websites” ([31], p. 186). They contain valuable information about a product or service. Studying online reviews can help manufacturers better understand consumer responses to their products and thereafter enhance their products [21]. Online reviews not only enhance consumer awareness, but also serve as a reliable source of information about the quality of the product or service of interest [22].

While most review opinion mining studies have concentrated on sentiment analysis (thumbs up or down) [23,37], the issue of review quality is often ignored, which leads to retrieving useless or even noisy documents [3]. Mudambi and Schuff [31] have stated that what makes customer reviews helpful is an important research question. Similarly, Cao et al. [2] have raised the research question as to why some reviews receive many usefulness votes while others receive few or no votes at all. Why some reviews are rated as helpful while others are not is therefore an important and interesting empirical question.

Major websites such as Amazon.com and Yelp.com provide a “Most Helpful First” option in sorting and presenting customer reviews. They usually ask a question like: “Was this review useful?” The customer reviews can then be ranked on the “usefulness” dimension based on the number of readers who voted “yes”. This community-based voting technique is called “social navigation” [12], which is widely used to help readers address the information overload problem, especially for products that have hundreds of online reviews. However, newly written reviews do not get suf<sup>fi</sup>cient time to accumulate helpfulness votes and, therefore, should not be ranked based on readers' votes [11,19]. Automatic helpfulness estimation methods could be employed to address this problem.

In general, predictive analytics involve constructing and evaluating models for the purpose of making empirical predictions [45]. We employ the predictive analytics approach for this study. More speci<sup>fi</sup>cally, we model the prediction of review helpfulness as a regression problem. The goal is to estimate or predict the value of review helpfulness. In websites such as Yelp.com, the helpfulness information is provided in the format of “y readers found the review useful” for existing reviews. For newly written reviews for which readers did not have suf<sup>fi</sup>cient time to provide ratings, our study provides an effective way to rate those reviews. This research can provide signi<sup>fi</sup>cant bene<sup>fi</sup>ts to social media platforms by helping them rate new online reviews instantly and adjust their presentation ef<sup>fi</sup>ciently. But to do that, we need to build a prediction model based on existing reviews whose helpfulness is known. We adopt the raw number of positive helpful votes of a review, or y in the example above, as the measure of helpfulness. The larger the number y, the more helpful the review appears to readers.

In this study, we propose a new hybrid model, which incorporates both the vector space model (VSM) representation of review text and a reviewer's engagement pro<sup>fi</sup>le. We address three important research questions in this study. We <sup>fi</sup>rst examine if the VSM representation of review text improves the prediction of review helpfulness over a baseline model. Second, we examine if the hybrid model is better than using VSM alone for the prediction of review usefulness. Third, we examine whether the hybrid model is better than using a reviewer's engagement pro<sup>fi</sup>le alone for predicting review helpfulness.

This research makes important contributions to the literature. First, we propose and empirically validate hybrid text regression models that incorporate both review textual features and reviewer engagement characteristics. Second, we creatively adapt the RFM (Recency, Frequency, and Monetary Value) analysis [29] to the domain of online social media and demonstrate that the hybrid approach with reviewers' RFM dimensions produces the best results, overall.

The paper is organized as follows. We <sup>fi</sup>rst survey the relevant literature on review helpfulness. Then we present the research model, followed by a description of the collected data and experiments. Next, we report the <sup>fi</sup>ndings from the experiments and discuss the implications of those <sup>fi</sup>ndings. Finally, we conclude the paper and identify future directions.

## 2. Literature review

Table 1 summarizes the main <sup>fi</sup>ndings of past studies on review helpfulness. Formulating it as a regression problem, some studies tried to rank the reviews based on helpfulness or utility. For example, with radial basis function (RBF) regression, reviewer's expertise, writing style, and timeliness of the review are identi<sup>fi</sup>ed as important factors for predicting the helpfulness of IMDB movie reviews [25,26]. Yu et al. [53] found that writing style, as re<sup>fl</sup>ected in part-of-speech tags, is effective in predicting movie review quality using support vector regression. Kim et al. [19] found that simple TF/IDF (Term Frequency/Inverse Document Frequency) weights of lemmatized unigrams, the length of the review, and product rating (number of stars) are the most important features in their Support Vector Machine (SVM) regression. Zhang and Varadarajan [55] found more sophisticated linguistic style cues (e.g., counts of words, sentences, wh-words such as which and where, and comparatives) to be the most effective. Ghose and Ipeirotis [9] found that the standard deviation of the sentence subjectivity scores and readability scores signi<sup>fi</sup>cantly in<sup>fl</sup>uence the helpfulness rank, and suggests that extreme reviews are the most helpful.

Chen and Tseng [3] found that high-quality reviews are those with in-depth comments on several product features, and are subjective as well. Cao et al. [2] also found that reviews with extreme opinions are more likely to be perceived as being more helpful. Moreover, semantic characteristics are more important than basic and stylistic features.

Taken together, these studies indicate that both the relevant key topics (substance) and subjective opinion are important for predicting review helpfulness.

In addition to review textual features, some reviewer characteristics have also been examined for review usefulness evaluation. Writer authority as a baseline feature was used in the classi<sup>fi</sup>cation models to predict the quality of user-generated documents [15]. Adopting the data quality framework proposed by Wang and Strong [49], Otterbacher [36] treated the reviewer's reputation as a dimension of intrinsic quality in a study of Amazon review helpfulness. The reviewer's reputation was measured by helpful votes received, total reviews written, “top reviewer” badge, and reviewer's rank in the community. The mean helpfulness of a reviewer's past reviews (a reputation feature) was found to be the strongest single predictor of the helpfulness of his/her current review [34,35].

In a recent empirical study aiming to understand what factors drive consumers to contribute in online platforms, reputation, sense of belonging, and enjoyment of helping other consumers were found to be signi<sup>fi</sup>cant motivations [6]. Identifying reputable online reviewers enables members to decide whose reviews they should trust [21].

In an empirical investigation of the impact of online reviews on product sales [17], the results showed that consumers not only pay attention to review ratings (number of stars), but also to the reviewer's reputation and reviewer exposure (how many reviews the reviewer has posted on the review website). Reviews written by reputable and voluminous reviewers are received more favorably by the market. To identify experts in online knowledge communities, a novel algorithm, ExpertRank, was recently proposed and tested [48]. The experimental results demonstrate that both document-based relevance and a member's authority in the knowledge community are important factors.

To address the research problem of automatic helpfulness regression/classi<sup>fi</sup>cation, some studies concentrated on various textual and linguistic features (see Table 1). Other studies demonstrated that reviewer characteristics are relevant for review usefulness prediction, but none of them employed the lens of RFM to model reviewer characteristics. To the best of our knowledge, none of the prior studies has evaluated the predictive power of combining both textual features and reviewer engagement characteristics. While acknowledging the potential utility of textual features, we argue that reviewer engagement characteristics would also in<sup>fl</sup>uence readers' perception of review helpfulness. In this study, we develop a hybrid text regression model, which combines review textual features and reviewer engagement characteristics. Moreover, we empirically compare the predictive power of the proposed hybrid model with those of the textual features only model and the reviewer characteristics only model.

## 3. Conceptual model development and research questions

In this section, we <sup>fi</sup>rst review the work in VSM, and then describe RFM analysis and review its applications. We explain the application of RFM analysis to represent a reviewer's engagement pro<sup>fi</sup>le and make the argument that engagement is associated with review helpfulness. Next, we describe the development of the text regression models, and then elaborate on the speci<sup>fi</sup>c research questions addressed in this study.

## 3.1. Vector space model

In the literature on information retrieval [41,42] and text categorization [43], unstructured text is often represented by a vector space model (VSM). In VSM, the values of the elements are derived from event frequencies, such as the number of times a certain word appears in a particular document [47]. “The novelty of the VSM was to use frequencies in a corpus of text as a clue for discovering semantic information” ([47], p. 143). This fundamental insight can be expressed as the statistical semantics hypothesis: the statistical patterns of human word usage can be exploited to <sup>fi</sup>gure out what people write or talk about [47].

Summary of past studies on review helpfulness.

<table><tr><td>References</td><td>Review domain</td><td>Problem formulation</td><td>Findings</td></tr><tr><td>[19]</td><td>Amazon MP3 players and digital cameras</td><td>Readers&#x27; helpful vote ratio as ground truth, support sector regression with RBF kernel</td><td>Review length, product rating, and unigrams are the most useful features.</td></tr><tr><td>[54,55]</td><td>Amazon electronics, engineering books, and PG-13 movies</td><td>Readers&#x27; helpful vote ratio as ground truth, support vector regression with RBF kernel</td><td>Shallow syntactic features are most useful, subjectivity has limited influence, and lexical similarity to product description and editorial review plays a minor role.</td></tr><tr><td>[24]</td><td>Amazon digital cameras</td><td>Manual annotation based on author-defined quality as ground truth, support vector machines, binary classification</td><td>Informativeness features improve classification performance, readability has marginal effect and subjectiveness makes no contribution.</td></tr><tr><td>[9]</td><td>Amazon DVDs, audio and video players, videogames, computers, PDAs software, and digital cameras</td><td>Readers&#x27; helpful vote ratio as ground truth, log transformation of linear regression</td><td>Reviews that include a mixture of objective and subjective elements are considered helpful, readability is also relevant.</td></tr><tr><td>[15]</td><td>Amazon Electronics and answer messages from Question and Answer online forum</td><td>Manual annotation based on author-defined quality as ground truth, maximum entropy classification</td><td>Formality is most effective, subjectivity helps review corpus classification, readability makes no contribution.</td></tr><tr><td>[25,26]</td><td>IMDB movie</td><td>Readers&#x27; helpful vote ratio as ground truth, radial basis function (RBF) regression</td><td>Reviewer&#x27;s expertise, writing style, and timeliness of the review are important.</td></tr><tr><td>[36]</td><td>Amazon DVDs, Electronics, Music and Software</td><td>Readers&#x27; helpful vote ratio as ground truth, confirmatory factor analysis based on data quality framework [49]</td><td>Five quality dimensions are related to helpfulness scores. The five dimensions are relevancy, reputation, ease of understanding, believability, and objectivity.</td></tr><tr><td>[28]</td><td>Community review website Ciao UK, cellphones, beauty, and digital cameras</td><td>Linear regression to predict review quality</td><td>Using social contextual information such as authors&#x27; identities and social networks improves review quality prediction.</td></tr><tr><td>[34,35]</td><td>TripAdvisor hotel</td><td>Classification, helpful vs. non-helpful</td><td>Information gain feature selection shows reviewer reputation to be very significant. The mean helpfulness of a reviewer&#x27;s reviews is the strongest predictor of classification accuracy.</td></tr><tr><td>[31]</td><td>AmazonMP3 player, Music CD, PC video game, cell phone, digital camera and laser printer</td><td>Readers&#x27; helpful vote ratio as ground truth, linear regression model based on the paradigm of search and experience goods from information economics</td><td>Product type (search or experience goods) moderates the effect of product star rating on review helpfulness. Product type also moderates the effect of review length on review helpfulness.</td></tr><tr><td>[2]</td><td>CNETD Windows Enterprise Computing software programs</td><td>Whether a review receives at least one vote or not, ordinal logistic regression</td><td>Semantic characteristics are more influential than basic and stylistic features. Reviews with extreme opinions receive more helpfulness votes.</td></tr><tr><td>[3]</td><td>Amazon digital cameras and mp3 players</td><td>Manual annotation of review quality as ground truth, SVM classification</td><td>Employed an effective information quality framework to extract representative review features. High-quality reviews tend to be subjective and provide in-depth comments on a number of product features.</td></tr><tr><td>[11]</td><td>Amazon Audio and video players, digital cameras, and DVDs</td><td>Classification with random forest</td><td>The extent of subjectivity, informativeness, readability and linguistic correctness in reviews matters in influencing perceived usefulness. Reviews that have a mixture of objective and highly subjective sentences are rated more helpful.</td></tr><tr><td>[53]</td><td>IMDB movie</td><td>Readers&#x27; helpful vote ratio as ground truth, support vector regression with radial basis function (RBF) kernels</td><td>Employed shallow syntactical features (part-of-speech tag) to represent writing style for predicting review quality. Both review sentiment and review quality have a significant impact on predicting movie sales.</td></tr><tr><td>[32]</td><td>Amazon books</td><td>Readers&#x27; helpful votes as ground truth, support vector regression with linear kernel</td><td>Dimension reduction techniques enhance text regression performance for review helpfulness prediction.</td></tr></table>

The bag-of-words (BOW) model is a speci<sup>fi</sup>c type of vector space model. A document is represented as a bag of words. For example, the bag {t , t , t , t , t , t } can be represented as a vector x = (3,1,2), where the value of an element in the vector is the frequency of the corresponding word in the bag. To make the BOW representation of document more robust, a common practice is to <sup>fi</sup>lter out stopwords. Stopwords are common words, such as articles (e.g., “a”, “an”), conjunctions (e.g., “and”, “but”), and prepositions (e.g., “in”, “on”). Stopwords frequently appear in documents but they do not possess any real discriminating power. Removing the stopwords reduces unnecessary noise from the BOW model.

The frequencies of words in a document re<sup>fl</sup>ect what the document is about, or its topic and theme; they appear to capture an important aspect of text content. A plausible explanation is that the message a writer wants to express will probabilistically affect the writer's choice of words when writing the text [47].

One potential problem with using a BOW Full model, in which all the words in a text collection are used as predictors, is its high dimensionality (a very large numbers of variables — thousands or more), thereby necessitating feature selection [43]. The large dimensionality of the attribute space results in high computational costs and long training times. More importantly, it could lead to over<sup>fi</sup>tting for many learning algorithms. Dimension reduction techniques are therefore applied to address these problems [43]. Dimension reduction methods tend to signi<sup>fi</sup>cantly improve the performance of text regression models for predicting review helpfulness [32].

Correlation-based Feature Selection (CFS) has been shown to outperform other dimension reduction methods such as Entropy and Chisquare for Ovarian cancer classi<sup>fi</sup>cation [27]. Latent Semantic Analysis (LSA) has also been applied to extract semantic characteristics of review text [2]. Most conventional <sup>fi</sup>lter algorithms cannot handle dimension reduction for regression problems [13]. For example, traditional feature selection methods such as Chi-square, odds ratio, information gain, gain ratio, and mutual information cannot be applied to the regression problem. CFS has been shown to yield good performance results for regression [13,14]. We experimented with both CFS and LSA, and found that CFS consistently produced better results. We, therefore, report the results using CFS for dimension reduction and support vector regression (SVR) for predicting review helpfulness.

CFS evaluates subsets of the attributes. The basic rationale for CFS is that the desired attribute subset includes attributes that are highly correlated with the target variable but, at the same time, have low correlations among the attributes themselves [13]. High correlations between the subset attributes and the class variable indicate that the attributes are highly relevant. Lower correlations among the subset attributes imply that there is less redundancy in the subset. According to Hall [13], the “merit” or worth of a subset of attributes for predicting the target variable can be derived in the following manner. Suppose that an attribute subset S contains k predictors $\left\{ \mathrm { x } _ { 1 } , \mathrm { x } _ { 2 } , \mathrm { x } _ { 3 } , . . . , \mathrm { x } _ { \mathrm { k } } \right\}$ and the target variable is y. The average predictor–target correlation $\overline { { r _ { \mathrm { x y } } } }$ is de<sup>fi</sup>ned as:

$$
\overline {{r _ {\mathrm{xy}}}} = \frac {\sum_ {i = 1} ^ {k} c o r r (\mathrm{x} _ {i} , \mathrm{y})}{\mathrm{k}}.
$$

The average predictor–predictor intercorrelation $\overline { { r _ { x x } } }$ is de<sup>fi</sup>ned as:

$$
\overline {{r _ {\mathrm{xx}}}} = \frac {\sum_ {i = 1} ^ {k} \sum_ {j = 1 , j \neq i} ^ {k} \operatorname{corr} \left(\mathrm{x} _ {i} , \mathrm{x} _ {j}\right)}{\mathrm{k} * (\mathrm{k} - 1)}.
$$

The merit of $S ,$ a subset of attributes, can be de<sup>fi</sup>ned as:

$$
\operatorname{Merit} _ {S} = \frac {\mathrm{k} * \overline {{r _ {x y}}}}{\sqrt [ 2 ]{\mathrm{k} + \mathrm{k} * (\mathrm{k} - 1) * \overline {{r _ {x x}}}}}.
$$

After estimating the correlation matrix from the dataset, the best-<sup>fi</sup>rst search strategy is often adopted for searching in the subset space. At each step, the best attribute is chosen and appended to the current best subset. If adding the new feature does not lead to any improvement, the search goes back to the next best unexplored subset and starts from there. In the best-<sup>fi</sup>rst search strategy, a common stopping criterion is controlling the level of backtracking allowed. When the exploration encounters a number of consecutive non-improving nodes and the number reaches a predetermined threshold, the search procedure is terminated. We refer to this procedure of CFS subset evaluation with best-<sup>fi</sup>rst search as CfsBF.

## 3.2. RFM analysis

RFM refers to Recency, Frequency, and Monetary Value of a customer's transactional history. The variables of RFM are measured by:

Recency: how long ago the customer made the last purchase Frequency: the frequency or total number of purchases by the customer

Monetary Value: the average amount of money the customer spent per transaction.

The three dimensions of RFM are used together as a whole to sort customers' transaction records and segment customers [18]. RFM analysis is an intuitive tool for maximizing purchase response rates of marketing campaigns in direct marketing [29]. While more sophisticated techniques have been reported in relatively newer studies (e.g., [40]), RFM analysis is still a widely practiced method in direct marketing. For targeted marketing and ef<sup>fi</sup>cient customer segmentation (pro-<sup>fi</sup>ling), a recent study has compared an RFM-based predictive model with classical data mining techniques and examined the tradeoffs [33]. RFM analysis has been used to estimate the importance of a customer based on his/her past purchasing behavior [44].

The principal rationale for RFM analysis is that a customer's past transaction behavior is a good predictor of his/her future behavior [7]. Customers who have recently made a purchase, who purchase frequently, and who have spent more money per transaction on average are often the best customers for the business. RFM is a convenient, yet powerful, behavioral analysis tool that helps marketers focus on those pro<sup>fi</sup>table customer segments [18]. RFM dimensions are the most commonly used indicators to gauge the propensity that a customer will make a purchase [46]. RFM analysis has been used to build customer value models that support management to respond promptly and effectively (see, for example, [1]).

## 3.3. Characterizing reviewer engagement using RFM analysis

We apply the principle of RFM analysis to the online review context, where a reviewer adds value to the review website by frequently writing good and timely reviews. We therefore broaden the scope of RFM analysis from monetary transactions to online reviews. In an online setting, a reviewer's RFM can describe his/her overall contributing behavior to the platform [20].

We derive RFM-like measures for reviewers to characterize the strength of their engagement in the online community. The number of days between a reviewer's current review and the immediate previous one is the measure of Recency. A simple proxy for Frequency is the number of reviews a reviewer has written and posted on the website before the current review. The Monetary Value can be estimated by the average number of helpfulness votes received by the reviewer across all the reviews he or she has written.

Reviews rated as useful tend to be written with relatively high level of effort and involvement on the part of a reviewer. Therefore, the review quality feedback (average number of helpful votes) can be viewed as an indicator of the intensity of the engagement. Moreover, the better the average quality of each contribution, the more reputable the reviewer is, because he or she consistently produces high quality reviews. The more frequently a reviewer posts reviews, the more committed the reviewer is with the online community. The more recently a reviewer posted a review, the more currently active is the reviewer. Using RFM analysis, therefore, we can identify valuable and good reviewers for the review website. Reviewers ranked on the high end of RFM dimensions are considered important by the online platform, because they are intensely engaged/reputable, committed, and currently active. Therefore, we can conceptualize RFM as a proxy for the overall strength of a reviewer's engagement in the online review community.

We argue that reviewers make important contributions to review websites by providing timely, frequent, and useful reviews. Highquality and timely reviews help a website attract more readers and generate more online advertisement revenue and/or increased product sales. We, therefore, draw an analogy between a reviewer and a customer. Review websites recognize the value of important reviewers and implement management strategies to facilitate online community building. To gauge a reviewer's importance with respect to the business of a review website, we argue that, just like a customer's RFM dimensions, the more recently the reviewer contributes, the more frequently he or she writes reviews, and the higher the quality of those contributed reviews, the more important will the reviewer be to the website.

Consistent with the behavior principle inherent in RFM analysis, a reviewer with better RFM scores may very likely produce a very useful review when he/she writes a new one. These good reviewers, in general, are more reputable, committed, and currently active. An intensely engaged or reputable reviewer is likely to make more effort in writing a good review. Moreover, a reputable reviewer may have more expertise in the topic area to be reviewed. A reputable reviewer may also happen to be a good writer or really concerned for other consumers [6]. A good reviewer establishes his/her online reputation and self-image through a history of contributing behavior. The feedback in terms of helpful votes received in the past may encourage a reviewer to continue the good work of reviewing so as to maintain and enhance one's existing reputation. Therefore, one can expect that new reviews written by good reviewers to be also very helpful.

## 3.4. Development of conceptual text regression models

Based on the literature on VSM, RFM analysis, and reviewer characteristics, we propose several conceptual text regression models (see Fig. 1). Consistent with the norm of evaluating models in predictive analytics, we compare the predictive accuracy (error) of competing models as well as the naïve model, which simply predicts the target variable in a new case as the overall average [45]. We start with the baseline ZeroR model, which does not make use of the text of online reviews or reviewer characteristics. The ZeroR model always predicts the value of the target variable in a new case as the majority class in the training data for classi<sup>fi</sup>cation problems, and as the mean value of the target variable in the training data for regression problems [51]. The ZeroR model has been used as a baseline for model comparison in both classi<sup>fi</sup>cation and regression problems [8,50]. Absent any other information about a review – such as review text content or a reviewer's characteristics – the ZeroR model provides the best possible estimate for its usefulness.

Next, we introduce VSM to represent review text. All the review words are used to create the BOW Full model. We then apply the CfsBF dimension reduction method to produce the Dimension Reduced BOW model (or BOW′, in short). Parallel to the development of the BOWbased model, we develop the RFM model, which captures only the reviewer's RFM characteristics.

We next develop a hybrid model, incorporating both review text and reviewer engagement characteristics. To operationalize the hybrid model, we integrate the textual features of the BOW′ model with the reviewer's RFM dimensions. We call this the BOW′ + RFM model. Table 2 summarizes the <sup>fi</sup>ve types of text regression models we investigate in this study.

## 3.5. Research questions

We next describe the proposed model comparisons (see Fig. 1) and elaborate on the research questions. In the context of online customer reviews, we argue that both review text content and reviewer engagement characteristics in<sup>fl</sup>uence review helpfulness. The content of review text and its manifested textual features are often found to be useful in predicting review helpfulness (see Table 1). In addition to review text, various reviewer-related constructs have been found relevant in review helpfulness prediction, including reviewer-related features [10], reviewer authority [15], reviewer expertise [25,26], reviewer reputation [17,34–36], reviewer identity and social network [28], and reviewer exposure [17]. Therefore, we argue that, to better estimate review helpfulness, we need to consider not only the content of review text, but also the information on reviewer characteristics. In this study, we adopt a novel approach by employing RFM analysis to represent a reviewer's engagement pro<sup>fi</sup>le and relate it to review helpfulness.

We use the VSM to exploit the recurring word patterns in the review text for capturing the essence of the review text. However, in online review analysis, not all words are equally important. Some keywords have particular signi<sup>fi</sup>cance as they correspond to the core of topic content, attitude, and sentiment, while others may only contribute to the noise factor. The reviews that we have collected for this study contain thousands of unique words (variables), which may contain a lot of irrelevant, redundant, and noisy information. Since the target variable is number of helpfulness votes, what we are addressing is a text regression problem, rather than a text categorization problem. To extract the core relevant text content and use that in developing text regression models, we employ a feature selection technique — CfsBF. We believe that the resulting

![](/api/attachments/XGK2GVCE/fulltext/images/f330b8598d3c1d44c083f21850ca415bbcd2fb579cb465a006a910feecff65bb.jpg)  
Fig. 1. Development of conceptual text regression models.

Table 2  
Conceptual models for predicting review helpfulness.

<table><tr><td>Model type</td><td>Predictor variables</td></tr><tr><td>ZeroR model</td><td>NA</td></tr><tr><td>BOW Full model</td><td>All the words from review text collection</td></tr><tr><td>Dimension Reduced BOW model (BOW&#x27;)</td><td>A subset of review words selected through applying CfsBF dimension reduction technique</td></tr><tr><td>RFM model</td><td>Reviewer&#x27;s RFM dimensions (Recency, Frequency, and Monetary Value)</td></tr><tr><td>BOW&#x27; + RFM model</td><td>CfsBF selected review words + reviewer&#x27;s RFM dimensions</td></tr></table>

BOW′ model captures only the relevant and necessary content of review text. Because review text content is expected to affect readers' rating of review helpfulness, we pose the following research question:

RQ1: Is the accuracy of the BOW′ model higher than that of the ZeroR model for predicting review helpfulness, i.e., is BOW′ N ZeroR?

In the context of online review community, a reviewer's RFM dimensions can be employed to characterize his/her overall engagement strength, because it captures the aspects of reputation, commitment, and current activity. Following the behavior principle inherent in RFM analysis, we expect reviewers with a proven track record to continue generating high-quality and well-received reviews. The reviewers' RFM dimensions would therefore provide useful cues on the helpfulness of the reviews they post. We expect that incorporating reviewer characteristics (RFM dimensions to represent a reviewer's engagement level) may enhance review helpfulness prediction accuracy beyond that of a model making use of only review text content. Hence, we examine the following research question:

RQ2: Is the accuracy of the BOW′ + RFM model higher than that of the BOW′ model alone for predicting review helpfulness, i.e., is BOW′ + RFM N BOW′?

While reviewers' RFM dimensions provide important signals of the reviewer's engagement, they only represent the general tendency of review usefulness based on the previous review records. Each individual new review, after all, has its own distinct idiosyncrasies that also contribute to the review helpfulness. We argue that adding selected key review words of BOW′ model to reviewer engagement characteristics model (reviewer RFM dimensions) would improve review usefulness prediction accuracy beyond that of a model making use of RFM dimensions only. Consequently, we examine the following research question:

RQ3: Is the accuracy of the BOW′ + RFM model higher than that of the RFM model alone for predicting review helpfulness, i.e., is BOW′ + RFM N RFM?

## 4. Methodology

## 4.1. Data collection

We collected data from two different sources: Amazon book reviews and Yelp restaurant reviews. We randomly selected ten books from Amazon and downloaded all the customer reviews for those books. We also acquired all the reviews for the 21 most-reviewed restaurants from the Yelp Dataset Challenge, 2013. Since reviews posted recently may not have had suf<sup>fi</sup>cient time to accumulate helpful votes, we removed the reviews written within two months before the data collection date.

After that, we had a pool of 584 Amazon book reviews and 7465 Yelp restaurant reviews.

## 4.1.1. RFM measures

We operationalize the Monetary Value dimension by using the average useful (helpful) votes a reviewer received for all his/her reviews, i.e.,

$$
\text { Monetary   Value } = \frac {\sum_ {i = 1} ^ {N} x _ {i} - x _ {\text { current }}}{N - 1}
$$

where N is the total number of reviews written by the reviewer $, x _ { i }$ is the number of useful votes for a review i written by the reviewer, and x<sub>current</sub> is the number of useful votes for the current review. The reason we use N − 1 is to remove the current review from the count. By removing the current review, we make sure that we are not using the votes for the current review in estimating its usefulness, which could otherwise bias the Monetary Value dimension, especially in situations when the reviewer does not have too many reviews.

For the Frequency dimension, we operationalize it as the number of previous reviews written by the same reviewer before the current review is posted. We count the number of reviews written up until the current review and use this number to represent Frequency. That is,

Frequency numberof reviewswrittenbeforethecurrentreview:

The Recency dimension is measured by the number of days between the posting date of the current review and that of the most recent review prior to the current review, i.e.,

Recency PostDate–lastPostDate:

Note that the larger the value of Recency, the less recent is the review.

## 4.2. Construction of instantiated models

We prepare the BOW model, where the predictor variables are the weights of words from a review text collection. We perform the following pre-processing procedures to generate the word lists (feature space) from review text (see Fig. 2). First, we tokenize the review text by removing all non-alphabetic characters. Then we apply the built-in English stopword list <sup>fi</sup>lter from RapidMiner 5.0 data mining tool [30] to remove common stopwords, which do not carry signi<sup>fi</sup>cant meaning. Next, we convert all the terms to lower case. Finally, we apply the popular Porter Stemmer algorithm [39] to stem English words. The algorithm applies an iterative, rule-based replacement of word suf<sup>fi</sup>xes to decrease the length of words.

For both Yelp and Amazon datasets, we experimented with all four index weighting schemes (Binary Occurrence, Term Occurrence, TF or Term Frequency, and TF/IDF) available in RapidMiner 5.0 to assign a term weight to each feature in the review text. In the binary occurrence scheme, a Boolean value of 0 or 1 is used to indicate absence or presence of a word in a document. In the Term Occurrence scheme, the raw word count in a document is used as the term weight. TF is similar to Term Occurrence, except that the raw word count is normalized by the document length. In the TF/IDF scheme, the word frequency in a document is transformed into:

$$
f _ {i, j} * \log \frac {\text { Number   of   Documents }}{\text { Number   of   Documents   with   word } i}
$$

where $f _ { i , j }$ is the frequency of word i in document j.

We apply the CfsBF dimension reduction technique to generate BOW′ models. We employ the Weka 3.6 data mining tool [51] for the dimension reduction task. Next, we add three dimensions of reviewers' RFM (Recency, Frequency, and Monetary Value) to the BOW′ models to generate the BOW′ + RFM models. Fig. 2 schematically captures the steps of the review helpfulness analysis process.

![](/api/attachments/XGK2GVCE/fulltext/images/ca9fc9f6ccdc07f39ba96bb2421e7b7f653fd9c8f12ba2bc1c226d3089c2ddcb.jpg)  
Fig. 2. Analyzing online customer review helpfulness using text regression

In summary, we have two ZeroR models, one for Yelp and one for Amazon. We also have two RFM only models, one for Yelp and one for Amazon. For BOW-based models, we have two sources of review (Yelp and Amazon). Within each review source, we have three conceptual types (BOW Full, BOW′ and BOW′ + RFM). For each of the BOWbased models, we experiment with four different types of index weighting schemes (Binary Occurrence, Term Occurrence, TF, and TF/ IDF), leading to:

2 ZeroR Models 2 RFM Models 2 Sourcesof Reviews

1BOW Full 1BOW′ 1BOW′ RFM

4 Index Weighting Schemes 2 2 2 3 4 28 models:

Therefore, we have a total of 28 instantiated models representing various conceptual types (see Table 3).

In Table 4, we summarize the operationalization of the predictor and target variables of various text regression models. The target variable for all the models is the number of useful/helpful votes. $\mathsf { W } _ { 1 } , \mathsf { W } _ { 2 } , . . . \mathsf { W } _ { N }$ refer to the weights of review words, where N is the total number of unique words in a review text collection. $\mathsf { W } _ { 1 } ^ { \prime } , \mathsf { W } _ { 2 } ^ { \prime } , . . . \mathsf { W } _ { p ^ { \prime } }$ refer to the weights of selected review words, where p is the size of the subset of unique words selected by CfsBF.

## 4.3. Experimental configuration

With the 28 instantiated text mining models identi<sup>fi</sup>ed above, we next design a text regression experiment to predict review helpfulness. Since support vector regression (SVR) has been shown to be effective in previous studies [19,54,55], we adopt the state-of-the-art support vector regression algorithm for this study. More speci<sup>fi</sup>cally, we apply Weka's SVR implementation — SMOreg with RBF kernel. In the default setting of SMOreg, all predictor variables are normalized before SVR is applied. The normalization scheme ensures that all predictor variables (review words and RFM dimensions) are on the same scale. Because the Amazon dataset is relatively small in size, we adopt 10-fold crossvalidation, which produces a relatively unbiased error estimate. Because the Yelp dataset is quite large, we randomly divide the sample into two parts: 60% for training and 40% for testing. To ensure robustness of the results, we perform 10 experimental runs [51]. Hence, we have 10 runs of the 10-fold cross-validation for the Amazon dataset and 10 runs of the 60%:40% split for the Yelp dataset. We use the average error rate across 10 runs as the overall performance measure.

## 4.3.1. Regression performance measures

We employ the following error-based measures to estimate regression performance: root relative squared error (RRSE), relative absolute

## Table 3

28 instantiated models.

<table><tr><td>Conceptual type</td><td>Index weighing</td><td>Yelp</td><td>Amazon</td></tr><tr><td>ZeroR model</td><td>NA</td><td>Y7465ZeroR</td><td>A584ZeroR</td></tr><tr><td>RFM model</td><td>NA</td><td>Y7465RFM</td><td>A584RFM</td></tr><tr><td rowspan="4">BOW Full model</td><td>BinaOccu</td><td>Y7465BinaOccu</td><td>A584BinaOccu</td></tr><tr><td>TermOccu</td><td>Y7465TermOccu</td><td>A584TermOccu</td></tr><tr><td>TermFreq</td><td>Y7465TermFreq</td><td>A584TermFreq</td></tr><tr><td>TFIDF</td><td>Y7465TFIDF</td><td>A584TFIDF</td></tr><tr><td rowspan="4">BOW&#x27; model</td><td>BinaOccu</td><td>Y7465BinaOccuCfsBF</td><td>A584BinaOccuCfsBF</td></tr><tr><td>TermOccu</td><td>Y7465TermOccuCfsBF</td><td>A584TermOccuCfsBF</td></tr><tr><td>TermFreq</td><td>Y7465TermFreqCfsBF</td><td>A584TermFreqCfsBF</td></tr><tr><td>TFIDF</td><td>Y7465TFIDFCfsBF</td><td>A584TFIDFCfsBF</td></tr><tr><td rowspan="4">BOW&#x27; + RFM model</td><td>BinaOccu</td><td>Y7465BinaOccuCfsBFRFM</td><td>A584BinaOccuCfsBFRFM</td></tr><tr><td>TermOccu</td><td>Y7465TermOccuCfsBFRFM</td><td>A584TermOccuCfsBFRFM</td></tr><tr><td>TermFreq</td><td>Y7465TermFreqCfsBFRFM</td><td>A584TermFreqCfsBFRFM</td></tr><tr><td>TFIDF</td><td>Y7465TFIDFCfsBFRFM</td><td>A584TFIDFCfsBFRFM</td></tr></table>

Table 4  
Operationalization of predictor variables and target variable for text regression models.

<table><tr><td>Model type</td><td>Predictor variables</td><td>Target variable</td></tr><tr><td>ZeroR model</td><td>NA</td><td>Number of useful votes</td></tr><tr><td>RFM model</td><td>Recency, Frequency, Monetary Value</td><td>Number of useful votes</td></tr><tr><td>BOW Full model</td><td> $W_1$ ,  $W_2$ , ...  $W_N$ </td><td>Number of useful votes</td></tr><tr><td>Dimension Reduced BOW model (BOW&#x27;)</td><td> $W_{1'}$ ,  $W_{2'}$ , ...  $W_p'$ </td><td>Number of useful votes</td></tr><tr><td>BOW&#x27; + RFM model</td><td> $W_{1'}$ ,  $W_{2'}$ , ...  $W_p'$ , Recency, Frequency, Monetary Value</td><td>Number of useful votes</td></tr></table>

error (RAE), root mean squared error (RMSE), and mean absolute error (MAE).

RMSE uses the square root of the average squared loss to measure regression error, i.e.,

$$
\mathrm{RMSE} = \sqrt [ 2 ]{\frac {\sum_ {i = 1} ^ {N} \left(y _ {i} - \hat {y} _ {i}\right) ^ {2}}{N}}.
$$

The default rule ZeroR model always predicts the mean of the target variable, calculated based on prior observations. The RMSE of ZeroR model is de<sup>fi</sup>ned as:

$$
\mathrm{RMSE} _ {\text { ZeroR }} = \sqrt [ 2 ]{\frac {\sum_ {i = 1} ^ {N} \left(y _ {i} - \overline {{y _ {i}}}\right) ^ {2}}{N}}.
$$

RRSE is a relative measure. It is the ratio of the algorithm's RMSE to the default rule's RMSE [8]. RRSE estimates how much better a learner is compared to the prior knowledge of the target class variable.

$$
\mathrm{RRSE} = \sqrt [ 2 ]{\frac {\sum_ {i = 1} ^ {N} (y _ {i} - \hat {y} _ {i}) ^ {2}}{\sum_ {i = 1} ^ {N} (y _ {i} - \overline {{y _ {i}}}) ^ {2}}}
$$

MAE, instead of using squared loss function as in RMSE, uses the absolute difference between the actual observation and the predicted target variable.

$$
\mathrm{MAE} = \frac {\sum_ {i = 1} ^ {N} | y _ {i} - \hat {y} _ {i} |}{N}
$$

The MAE of the ZeroR model is de<sup>fi</sup>ned as:

$$
\mathrm{MAE} _ {\text { ZeroR }} = \frac {\sum_ {i = 1} ^ {N} | y _ {i} - \overline {{y _ {i}}} |}{N}.
$$

Similarly, RAE is the ratio of the regression algorithm's MAE to the default rule's MAE. Hence, it is also a relative measure like RRSE.

$$
\mathrm{RAE} = \frac {\sum_ {i = 1} ^ {N} | y _ {i} - \hat {y} _ {i} |}{\sum_ {i = 1} ^ {N} | y _ {i} - \overline {{y _ {i}}} |}
$$

## 5. Text mining results

We next present the evaluation results of the 28 instantiated models using the regression performance measures discussed in the previous section. The combination of the control factors (review source, index weighting, and regression performance measure) produces unique scenarios for model comparison. Since error-based measures are used to gauge text regression performance, a smaller value indicates better performance. For each pairwise model comparison, we highlight the better performing model in bold. We also conduct paired t-tests and report if the differences are statistically signi<sup>fi</sup>cant.

For the baseline ZeroR model, because it does not make use of review text content, the index weighting schemes do not have any impact. Therefore, the performance result of ZeroR model is the same across the four index weighting schemes. Similarly, the index weighting schemes have no impact on the RFM model, because the RFM model does not involve review text content either.

First, we compare CfsBF reduced models (BOW′) with BOW Full models. We <sup>fi</sup>nd that for all the 16 scenarios in Yelp, the CfsBF feature selection technique always helps improve regression performance beyond the BOW Full models. Based on paired t-tests, we <sup>fi</sup>nd that in all 16 scenarios, the performance differences are highly signi<sup>fi</sup>cant (p b 0.001). Similarly, we <sup>fi</sup>nd that for all the 16 scenarios in Amazon, the CfsBF models signi<sup>fi</sup>cantly outperform the corresponding BOW Full models $\left( \mathsf { p } < 0 . 0 0 1 \right)$ . The results strongly indicate that only a selected subset of review words is important for predicting review helpfulness.

## 5.1. BOW′ vs. ZeroR

In research question RQ1, we are interested in examining whether adding the VSM would improve the usefulness prediction performance beyond the baseline ZeroR model. We report the results of the two models, the BOW′ (CfsBF) model and the ZeroR model, <sup>fi</sup>rst for Yelp in Table 5a and then for Amazon in Table 5b.

For all 16 scenarios for Yelp, BOW′ model performs signi<sup>fi</sup>cantly better than ZeroR (see Table 5a). Similarly, in all the 16 scenarios for Amazon, BOW′ model also signi<sup>fi</sup>cantly outperforms ZeroR (see Table 5b). Overall, the BOW′ model performs better than the ZeroR model for predicting review helpfulness. The results, taken as a whole, strongly support research question RQ1 in the positive, demonstrating the ef<sup>fi</sup>cacy of VSM for predicting review helpfulness.

$$
5. 2. B O W ^ {\prime} + R F M v s. B O W ^ {\prime}
$$

We <sup>fi</sup>rst compare BOW′ with RFM for the different scenarios. We <sup>fi</sup>nd that for all the 16 scenarios for Yelp, RFM models always perform better than BOW' models. However, for all the 16 scenarios for Amazon. BOW′ models always perform better than RFM models. The results suggest that, in general, RFM dimensions play a more prominent role in Yelp, while review words of BOW′ play a more salient role in Amazon. Thus, the relative ef<sup>fi</sup>cacies of the BOW′ model and the RFM model appear to be dependent on the context and nature of the review domain.

Research question RQ2 investigates whether adding the reviewer's three RFM dimensions to the BOW′ model would further enhance regression performance. To answer this question, we examine whether the hybrid approach of combining BOW′ and RFM dimensions is better than BOW′ alone. We compare BOW′ with BOW′ + RFM for the different scenarios and report the results, <sup>fi</sup>rst for Yelp in Table 6a and then for Amazon in Table 6b.

## Table 5a

Comparison of ZeroR models with BOW′ (CfsBF), Yelp reviews

<table><tr><td rowspan="2">Datasets</td><td colspan="2">MAE</td><td colspan="2">RMSE</td><td colspan="2">RAE</td><td colspan="2">RRSE</td></tr><tr><td>ZeroR</td><td>BOW&#x27;</td><td>ZeroR</td><td>BOW&#x27;</td><td>ZeroR</td><td>BOW&#x27;</td><td>ZeroR</td><td>BOW&#x27;</td></tr><tr><td>BinaOccu</td><td>1.61</td><td>1.35**</td><td>2.57</td><td>2.34**</td><td>100.00</td><td>84.26**</td><td>100.00</td><td>91.04**</td></tr><tr><td>TermOccu</td><td>1.61</td><td>1.35**</td><td>2.57</td><td>2.33**</td><td>100.00</td><td>84.17**</td><td>100.00</td><td>90.62**</td></tr><tr><td>TermFreq</td><td>1.61</td><td>1.37**</td><td>2.57</td><td>2.42**</td><td>100.00</td><td>85.16**</td><td>100.00</td><td>93.82**</td></tr><tr><td>TFIDF</td><td>1.61</td><td>1.37**</td><td>2.57</td><td>2.45**</td><td>100.00</td><td>85.24**</td><td>100.00</td><td>95.06**</td></tr></table>

## Table 5b

Comparison of ZeroR models with BOW′ (CfsBF), Amazon reviews.

<table><tr><td rowspan="2">Datasets</td><td colspan="2">MAE</td><td colspan="2">RMSE</td><td colspan="2">RAE</td><td colspan="2">RRSE</td></tr><tr><td>ZeroR</td><td>BOW&#x27;</td><td>ZeroR</td><td>BOW&#x27;</td><td>ZeroR</td><td>BOW&#x27;</td><td>ZeroR</td><td>BOW&#x27;</td></tr><tr><td>BinaOccu</td><td>5.76</td><td>4.19**</td><td>12.04</td><td>10.73**</td><td>100.00</td><td>71.43**</td><td>100.00</td><td>88.39**</td></tr><tr><td>TermOccu</td><td>5.76</td><td>4.19**</td><td>12.04</td><td>11.02**</td><td>100.00</td><td>71.22**</td><td>100.00</td><td>89.76**</td></tr><tr><td>TermFreq</td><td>5.76</td><td>4.39**</td><td>12.04</td><td>11.50**</td><td>100.00</td><td>74.57**</td><td>100.00</td><td>94.50**</td></tr><tr><td>TFIDF</td><td>5.76</td><td>4.41**</td><td>12.04</td><td>11.62**</td><td>100.00</td><td>74.89**</td><td>100.00</td><td>95.25**</td></tr></table>

\*\* p b 0.001.

## Table 6a

Comparison of BOW′ models with BOW′ + RFM, Yelp reviews.

<table><tr><td rowspan="2">Datasets</td><td colspan="2">MAE</td><td colspan="2">RMSE</td><td colspan="2">RAE</td><td colspan="2">RRSE</td></tr><tr><td>BOW&#x27;</td><td>BOW&#x27;+ RFM</td><td>BOW&#x27;</td><td>BOW&#x27;+ RFM</td><td>BOW&#x27;</td><td>BOW&#x27;+ RFM</td><td>BOW&#x27;</td><td>BOW&#x27;+ RFM</td></tr><tr><td>BinaOccu</td><td>1.35</td><td>1.15**</td><td>2.34</td><td>1.92**</td><td>84.26</td><td>71.72**</td><td>91.04</td><td>74.73**</td></tr><tr><td>TermOccu</td><td>1.35</td><td>1.14**</td><td>2.33</td><td>1.90**</td><td>84.17</td><td>71.14**</td><td>90.62</td><td>73.67**</td></tr><tr><td>TermFreq</td><td>1.37</td><td>1.15**</td><td>2.42</td><td>1.93**</td><td>85.16</td><td>71.41**</td><td>93.82</td><td>75.10**</td></tr><tr><td>TFIDF</td><td>1.37</td><td>1.15**</td><td>2.45</td><td>1.94**</td><td>85.24</td><td>71.36**</td><td>95.06</td><td>75.28**</td></tr></table>

\*\* p b 0.001.

## Table 6b

Comparison of BOW′ models with BOW′ + RFM, Amazon reviews.

<table><tr><td rowspan="2">Datasets</td><td colspan="2">MAE</td><td colspan="2">RMSE</td><td colspan="2">RAE</td><td colspan="2">RRSE</td></tr><tr><td>BOW&#x27;</td><td>BOW&#x27;+ RFM</td><td>BOW&#x27;</td><td>BOW&#x27;+ RFM</td><td>BOW&#x27;</td><td>BOW&#x27;+ RFM</td><td>BOW&#x27;</td><td>BOW&#x27;+ RFM</td></tr><tr><td>BinaOccu</td><td>4.19</td><td>4.17</td><td>10.73</td><td>10.72</td><td>71.43</td><td>71.11*</td><td>88.39</td><td>88.27</td></tr><tr><td>TermOccu</td><td>4.19</td><td>4.16**</td><td>11.02</td><td>11.00</td><td>71.22</td><td>70.65**</td><td>89.76</td><td>89.59</td></tr><tr><td>TermFreq</td><td>4.39</td><td>4.32**</td><td>11.50</td><td>11.43**</td><td>74.57</td><td>73.43**</td><td>94.50</td><td>93.75*</td></tr><tr><td>TFIDF</td><td>4.41</td><td>4.31**</td><td>11.62</td><td>11.49**</td><td>74.89</td><td>73.07**</td><td>95.25</td><td>94.01**</td></tr></table>

\*\* $\begin{array} { r } { \mathbf { p } < 0 . 0 0 1 . } \end{array}$

$$
\mathrm{p} <   0. 0 5.
$$

Comparison of RFM models with BOW′ + RFM, Yelp reviews

<table><tr><td rowspan="2">Datasets</td><td colspan="2">MAE</td><td colspan="2">RMSE</td><td colspan="2">RAE</td><td colspan="2">RRSE</td></tr><tr><td>RFM</td><td>BOW&#x27; + RFM</td><td>RFM</td><td>BOW&#x27; + RFM</td><td>RFM</td><td>BOW&#x27; + RFM</td><td>RFM</td><td>BOW&#x27; + RFM</td></tr><tr><td>BinaOccu</td><td>1.16</td><td>1.15**</td><td>2.01</td><td>1.92**</td><td>72.41</td><td>71.72**</td><td>78.07</td><td>74.73**</td></tr><tr><td>TermOccu</td><td>1.16</td><td>1.14**</td><td>2.01</td><td>1.90**</td><td>72.41</td><td>71.14**</td><td>78.07</td><td>73.67**</td></tr><tr><td>TermFreq</td><td>1.16</td><td>1.15**</td><td>2.01</td><td>1.93**</td><td>72.41</td><td>71.41**</td><td>78.07</td><td>75.10**</td></tr><tr><td>TFIDF</td><td>1.16</td><td>1.15**</td><td>2.01</td><td>1.94**</td><td>72.41</td><td>71.36**</td><td>78.07</td><td>75.28**</td></tr></table>

⁎⁎ p b 0.001.

## Table 7b

Comparison of RFM models with BOW′ + RFM, Amazon reviews.

<table><tr><td rowspan="2">Datasets</td><td colspan="2">MAE</td><td colspan="2">RMSE</td><td colspan="2">RAE</td><td colspan="2">RRSE</td></tr><tr><td>RFM</td><td>BOW&#x27; + RFM</td><td>RFM</td><td>BOW&#x27; + RFM</td><td>RFM</td><td>BOW&#x27; + RFM</td><td>RFM</td><td>BOW&#x27; + RFM</td></tr><tr><td>BinaOccu</td><td>4.50</td><td>4.17**</td><td>12.19</td><td>10.72**</td><td>76.38</td><td>71.11**</td><td>100.18</td><td>88.27**</td></tr><tr><td>TermOccu</td><td>4.50</td><td>4.16**</td><td>12.19</td><td>11.00**</td><td>76.38</td><td>70.65**</td><td>100.18</td><td>89.59**</td></tr><tr><td>TermFreq</td><td>4.50</td><td>4.32**</td><td>12.19</td><td>11.43**</td><td>76.38</td><td>73.43**</td><td>100.18</td><td>93.75**</td></tr><tr><td>TFIDF</td><td>4.50</td><td>4.31**</td><td>12.19</td><td>11.49**</td><td>76.38</td><td>73.07**</td><td>100.18</td><td>94.01**</td></tr></table>

⁎⁎ p b 0.001.

Based on the results shown in Tables 6a and 6b, we <sup>fi</sup>nd that for all the 32 scenarios for Yelp and Amazon – across all index weighting schemes and regression performance measures – BOW′ + RFM models always perform better than BOW′ only models. We conducted paired t-tests and found that in all the 16 scenarios of Yelp, the differences are statistically signi<sup>fi</sup>cant (see Table 6a). For Amazon, in 11 out of 16 cases, the BOW′ + RFM model is signi<sup>fi</sup>cantly better than the BOW′ model (see Table 6b). The results largely indicate that research question RQ2 is strongly supported in the positive. The hybrid model of BOW′ + RFM is superior to the BOW′ only model in predicting review helpfulness.

## 5.3. BOW′ + RFM vs. RFM

Research question RQ3 investigates whether adding the CfsBF selected review words to the RFM model would further improve regression performance. To address this question, we examine whether the hybrid approach of combining BOW′ and RFM dimensions is better than RFM alone. We compare RFM with BOW′ + RFM for the different scenarios and report the results, <sup>fi</sup>rst for Yelp in Table 7a and then for Amazon in Table 7b.

Based on the results shown in Tables 7a and 7b, we <sup>fi</sup>nd that for all the 32 scenarios for Yelp and Amazon – across all index weighting schemes and regression performance measures – the BOW′ + RFM models always perform better than the RFM only models. We conducted paired t-tests and found that in all the 16 scenarios of Yelp and all the 16 scenarios of Amazon, the differences are statistically signi<sup>fi</sup>cant. Research question RQ3, therefore, is strongly supported in the positive. The hybrid model of BOW′ + RFM is superior to the RFM model in predicting review helpfulness.

## 6. Discussion

The results of the study provide strong empirical support to our research questions. The <sup>fi</sup>ndings are consistent and robust across two review datasets (Yelp and Amazon), four index weighting schemes, and four regression performance measures. The most interesting <sup>fi</sup>nding is that incorporating a reviewer's RFM dimensions into the BOW' model produces the best predictive performance. In fact, the best models are all produced when the hybrid BOW′ + RFM approach is employed. Therefore, online social media platforms could build text mining models using a relatively small set of <sup>fi</sup>ltered words and enrich the models with the RFM dimensions of reviewers. We expect that our proposed hybrid model would be attractive to online platforms, which are interested in identifying useful new reviews promptly and presenting them sensibly.

RFM dimensions can be viewed as important reviewer characteristics, both from the online social media platform and the consumer's perspective. Our research con<sup>fi</sup>rms that a reviewer's RFM dimensions play a signi<sup>fi</sup>cant role in further improving the prediction of review helpfulness. The impact of RFM dimensions on review helpfulness is beyond the effect of review text content. Therefore, when estimating review helpfulness, we should take into account both the review text and the reviewer's RFM dimensions.

The implication for online platforms is that not only the textual content is important in predicting review helpfulness, but also that the reviewer's RFM dimensions matter. The <sup>fi</sup>ndings of this study should encourage review websites to automatically identify the most helpful reviews. By paying attention to both the review text and the reviewer's RFM dimensions, online platforms are more likely to spot helpful and in<sup>fl</sup>uential reviews, and can act promptly to position the most helpful reviews prominently on their websites. Featuring a reviewer's RFM information will not only bene<sup>fi</sup>t the readers by providing useful social navigation cues, but also encourage the reviewer to engage more actively and participate in online community building.

![](/api/attachments/XGK2GVCE/fulltext/images/387a9b7d65efc4e50877da7e1f20a89553425f78117f088fb186860294191c97.jpg)  
Fig. 3. Predicting new review helpfulness with trained model

In the era of Web 2.0, because of the interactive nature of the platform–user relationship and viral marketing, online platforms should pay close attention to the elites in the online community. Online platforms should be proactive with in<sup>fl</sup>uential reviewers and bloggers by cultivating positive online social relationships. RFM analysis is therefore not only applicable for modeling traditional purchase behavior, but also for modeling the strength of user's online engagement. As a reviewer contributes frequent and high-quality reviews to the website, he/she adds more value to the online platform.

## 7. Implications of <sup>fi</sup>ndings

Prior studies on review helpfulness have taken different perspectives and generated valuable, but diverse, and sometimes inconsistent, results. The central theme of our research is coming up with an effective approach to predict review helpfulness. The results from this empirical study indicate that both review textual features and reviewer characteristics are important in predicting review helpfulness.

This study demonstrates that the vector space model representation of review text does improve the prediction of review helpfulness. Moreover, this research reveals that reviewer engagement characteristics play an important role in further enhancing the estimation of review helpfulness. An important contribution of our study is in expanding the scope of RFM analysis from monetary transactions to modeling reviewers' online engagement. The empirical results demonstrate that the RFM analysis perspective is useful and signi<sup>fi</sup>cantly improves the prediction of review helpfulness.

This research has important managerial implications for review websites. Our research can bene<sup>fi</sup>t online platforms by helping them estimate the helpfulness of new reviews instantly. Thus, online platforms can quickly adjust the presentation of online reviews. For instance, when new restaurant reviews are posted on Yelp.com, a trained text regression model built using our approach can be applied to predict their usefulness. To predict the helpfulness of these new reviews, the SVR algorithm can be trained on existing reviews – which include review text, RFM dimensions, and helpfulness – and applied to the new incoming reviews to make predictions (see Fig. 3). Based on the predictions, an online platform such as Yelp.com can rank the new reviews instantly and feature the most helpful ones prominently on its website. Such actions would not only make the site more attractive to its readers, but also provide encouragement to those reviewers who invest their time and effort in writing effective reviews.

This study provides valuable insights into the factors that contribute to the prediction of review helpfulness. Overall, we <sup>fi</sup>nd that both reviewer engagement characteristics and review text are important in predicting review helpfulness. So online platforms should take a holistic view rather than focusing on review text alone. The reviewer's RFM measures could also be made readily available to the readers, so that those measures can serve as useful cues for identifying helpful reviews, and alleviate information overload.

Because a relatively small number of terms are key in predicting review helpfulness, online platforms can identify and pursue those key terms since they provide important clues to the core of the review text. From the <sup>fi</sup>ltered key terms, platforms can quickly glean knowledge on what aspects of products or services are important in reviewers' minds; what actions, actors, and entities are saliently involved; and what the prevailing sentiments are.

## 8. Conclusion and future directions

To the best of our knowledge, this study is the <sup>fi</sup>rst one to examine the role of reviewer's RFM dimensions in the context of online review helpfulness. One of the highlights of our research is the creative adaptation of RFM analysis to characterize the reviewer's online engagement. In the era of Web 2.0, online platforms are increasingly interested in monetizing user-generated content. Using RFM analysis, we presented a new perspective that would encourage online platforms to manage and cultivate online communities for promoting commerce. The results of our study reveal the insight that not only user-contributed content, but also that the RFM dimensions of an online community member are useful in estimating the helpfulness of the post.

Orthogonal to the research problem of review helpfulness, extant studies have examined the strategic manipulation of online reviews [16] and bias [38]. It would be interesting to investigate the interplay of these two aspects. Our current study can be further extended in several ways. First, we could examine the validity of our <sup>fi</sup>ndings in other review domains such as electronics and hotels. We expect the conclusion will hold because the methodology we developed is general and applicable to different types of reviews. Second, other indicators of reviewers' online engagement, such as the possession of various types of reviewer badges, may also be useful. We could consider combining review textual features with these new features. Third, reviewers' online social pro<sup>fi</sup>le, such as the number of friends in the community and the length of membership, may in<sup>fl</sup>uence review helpfulness evaluation, too. We may contemplate adding these social pro<sup>fi</sup>le features to the BOW′ model. Finally, we believe that the methodology presented in this paper can be applied to other domains. For example, it can be employed for evaluating the usefulness of answers in online discussion forums and identifying the most signi<sup>fi</sup>cant tweets for a company product or event.

## References

[1] R. Anderson-Lehman, H.J. Watson, B.H. Wixom, J.A. Hoffer, Continental airlines <sup>fl</sup>ies high with real-time business intelligence, MIS Quarterly Executive (3:4) (2004) 163–176.

[2] Q. Cao, W. Duan, Q. Gan, Exploring determinants of voting for the “helpfulness” of online user reviews: a text mining approach, Decision Support Systems (50) (2011) 511–521.

[3] C.C. Chen, Y.-D. Tseng, Quality evaluation of product reviews using an information quality framework, Decision Support Systems (50) (2011) 755–768.

[4] H. Chen, D. Zimbra, AI and Opinion Mining, IEEE Intelligent Systems (25:3) (2010) 74–76.

[5] Y. Chen, J. Xie, Online consumer review: word-of-mouth as a new element of marketing communication mix, Management Science (54:3) (2008) 477–491.

[6] C.M. Cheung, M.K. Lee, What drives consumers to spread electronic word of mouth in online consumer-opinion platforms, Decision Support Systems (53:1) (2012) 218–225.

[7] P.S. Fader, B.G. Hardie, K.L. Lee, RFM and CLV: using iso-value curves for customer base analysis, Journal of Marketing Research (XLII) (2005) 415–430.

[8] J. Gama, P. Brazdil, Characterization of classi<sup>fi</sup>cation algorithms, Proceedings of EPIA 95, Progress in Arti<sup>fi</sup>cial Intelligence; 7th Portuguese Conference on Arti<sup>fi</sup>cial Intelligence, LNAI, vol. 990, Springer-Verlag, Funchal, Madeira Island, Portugal, 1995, pp. 189–200.

[9] A. Ghose, P.G. Ipeirotis, Designing novel review ranking systems: predicting usefulness and impact of reviews, Proceedings of the International Conference on Electronic Commerce (ICEC), Minneapolis, Minnesota: ACM, 2007, pp. 1–7.

[10] A. Ghose, P.G. Ipeirotis, “Estimating the Socio-Economic Impact of Product Reviews: Mining Text and Reviewer Characteristics”, Working Paper, New York University, Stern School of Business, New York University, New York, 2008

[11] A. Ghose, P.G. Ipeirotis, Estimating the helpfulness and economic impact of product reviews: mining text and reviewer characteristics, IEEE Transactions on Knowledge and Data Engineering (23:10) (2011) 1498–1512.

[12] E. Gilbert, K. Karahalios, Understanding deja reviewers, CSCW 2010, ACM, Savannah, Georgia, USA, 2010. 225–228.

[13] M.A. Hall, Correlation-based feature selection for discrete and numeric class machine learning Proceedings of the Seventeenth International Conference on Machine Learning. 2000 pp. 359–366

[14] M.A. Hall, G. Holmes, Benchmarking attribute selection techniques for discrete class data mining, IEEE Transactions on Knowledge and Data Engineering (15:3) (2003) 1–16.

[15] L. Hoang, J.-T. Lee, Y.-I. Song, H.-C. Rim, A model for evaluating the quality of user-created documents, in: H. Li, T. Liu, W.-Y. Ma, T. Sakai, K.-F. Wong, G. Zhou (Eds.), AIRS 2008, LNCS 4993, Springer-Verlag, 2008, pp. 496–501.

[16] N. Hu, I. Bose, N.S. Koh, L. Liu, Manipulation of online reviews: an analysis of ratings, readability, and sentiments, Decision Support Systems (52:3) (2012) 674–684.

[17] N. Hu, L. Liu, J. Zhang, Do online reviews affect product sales? The role of reviewer characteristics and temporal effects in: P. Tallon I. Bardhan A. Gupta (Eds.). Information Technology and Management, 9:3 2008 pp. 201–214

[18] R. Kahan, Using database marketing techniques to enhance your one-to-one marketing initiatives, Journal of Consumer Marketing (15:5) (1998) 491–493.

[19] S.-M. Kim, P. Pantel, T. Chklovski, M. Pennacchiotti, Automatically assessing review helpfulness, Proceedings of the 2006 Conference on Empirical Methods in Natural Language Processing (EMNLP 2006), Association for Computational Linguistics, Sydney, Australia, 2006, pp. 423–430.

[20] D.M. Kroenke, Experiencing MIS, Third edition Prentice Hall, Upper Saddle River, New Jersey, 2012.

[21] Y.-C. Ku, C.-P. Wei, H.-W. Hsiao, To whom should I listen? Finding reputable reviewers in opinion-sharing communities, Decision Support Systems (53:3) (2012) 534–542.

[22] X. Li, L.M. Hitt, Self-selection and information role of online product reviews, in: A. Gupta (Ed.), Information Systems Research, 19:4, 2008, pp. 456–474.

[23] B. Liu, Sentiment analysis and subjectivity, in: N. Indurkhya, F.J. Damerau (Eds.), Handbook of Natural Language Processing2nd edition, 2010, pp. 1–38.

[24] J. Liu, Y. Cao, C.-Y. Lin, Y. Huang, M. Zhou, Low-quality product review detection in opinion summarization, Proceedings of the Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning (EMNLP-CoNLL), Prague: Association for Computational Linguistics, 2007, pp. 334–342.

[25] Y. Liu, X. Huang, A. An, X. Yu, Modeling and predicting the helpfulness of online reviews, 2008 Eighth IEEE International Conference on Data Mining, IEEE Computer Society, 2008, pp. 443–452.

[26] Y. Liu, X. Huang, A. An, X. Yu, HelpMeter: a nonlinear model for predicting the helpfulness of online reviews, 2008 IEEE/WIC/ACM International Conference on Web Intelligence and Intelligent Agent Technology, IEEE Computer Society, 2008, pp. 793–796.

[27] H. Liu, J. Li, L. Wong, A comparative study on feature selection and classi<sup>fi</sup>cation methods using gene expression pro<sup>fi</sup>les and proteomic patterns, Genome Informatics 13 (2002) 51–60.

[28] Y. Lu, P. Tsaparas, A. Ntoulas, L. Polanyi, Exploiting social context for review quality prediction, WWW 2010, ACM, Raleigh, North Carolina, USA, 2010. 691–700.

[29] C. Marcus, A practical yet meaningful approach to customer segmentation, Journal of Consumer Marketing (15:5) (1998) 494–504.

[30] I. Mierswa, M. Wurst, R. Klinkenberg, M. Scholz, T. Euler, YALE: rapid prototyping for complex data mining tasks, in: L. Ungar, M. Craven, D. Gunopulos, T. Eliassi-Rad (Eds.), Proceedings of the 12th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD-06), ACM, New York, NY, USA, 2006, pp. 935–940.

[31l. S.M. Mudambi D. Schuff What makes a helpful online review? A study of customer reviews On Amazon com in: C Saunders (Fd) MIS Ouarterly 34:1 2010 pp. 185–200.

[32] T.L. Ngo-Ye, A.P. Sinha, Analyzing online review helpfulness using a regressional reliefF-enhanced text mining method, ACM Transactions on Management, Information Systems (3:2) (2012) 10:1–10:20.

[33] D.L. Olson, B. Chae, Direct marketing decision support through predictive customer response modeling, Decision Support Systems (54:1) (2012) 443–451.

[34] M.P. O'Mahony, B. Smyth, Learning to recommend helpful hotel reviews, Recsys'09, ACM, New York, New York, USA, 2009. 305–308.

[35] M.P. O'Mahony, B. Smyth, A classi<sup>fi</sup>cation-based review recommender, in: M. Bramer (Ed.), Research and Development in Intelligent Systems XXVI, springer-Verlag London Limited London 2010 pp. 49–62

[36] J. Otterbacher, “Helpfulness” in online communities: a measure of message quality, CHI 2009 \~ Social Networking Sites. ACM. Boston, Massachusetts, USA. 2009. 955-964

[37] B. Pang L. Lee Opinion mining and sentiment analysis Foundations and Trends in Information Retrieval, vol. 2, 2008, pp. 1–135.

[38] S. Piramuthu, G. Kapoor, W. Zhou, S. Mauw, Input online review data and related bias in recommender systems, Decision Support Systems (53:3) (2012) 418–424.

[39] M.F. Porter, An algorithm for suf<sup>fi</sup>x stripping, Program (14:3) (1980) 130–137.

[40] W.J. Reinartz, V. Kumar, On the pro<sup>fi</sup>tability of long-life customers in a noncontractual setting: an empirical investigation and implications for marketing, Journal of Marketing (64:4) (2000) 17–35.

[41] G. Salton, C. Buckley, Term-weighting approaches in automatic text retrieval, Information Processing and Management (24:5) (1988) 513–523.

[42] G. Salton, A. Wong, C.S. Yang, A vector space model for automatic indexing, Communications of the ACM (18:11) (1975) 613–620.

[43] F. Sebastiani, Machine learning in automated text categorization, ACM Computing Surveys (34:1) (2002) 1–47.

[44] B. Shim, K. Choi, Y. Suh, CRM strategies for a small-size online shopping mall based on association rules and sequential patterns, Expert Systems with Applications (39:9) (2012) 7736–7742.

[45] G. Shmueli, O.R. Koppius, Predictive analytics in information systems research, MIS Quarterly (35:3) (2011) 553–572.

[46] G. Shmueli, N.R. Patel, P.C. Bruce, Data Mining for Business Intelligence: Concepts, Techniques, and Applications in Microsoft Of<sup>fi</sup>ce Excel with XLMiner, John Wiley & Sons, Inc., Hoboken, New Jersey, 2007.

[47] P.D. Turney, P. Pantel, From frequency to meaning: vector space models of semantics, Journal of Arti<sup>fi</sup>cial Intelligence Research (37) (2010) 141–188.

[48] G.A. Wang, J. Jiao, A.S. Abrahams, W. Fan, Z. Zhang, ExpertRank: a topic-aware expert <sup>fi</sup>nding algorithm for online knowledge communities, Decision Support Systems (54:3) (2013) 1442–1451.

[49] R.Y. Wang, D.M. Strong, Beyond accuracy: what data quality means to data consumers, Journal of Management Information Systems (12:4) (1996) 5–34.

[50] M. Ware, E. Frank, G. Holmes, M. Hall, I.H. Witten, Interactive machine learning: letting users build classi<sup>fi</sup>ers, International Journal Human-Computer Studies (55:3) (2001) 281–292.

[51] I.H. Witten, E. Frank, Data Mining: Practical Machine Learning Tools and Techniques, 2nd edition Morgan Kaufmann Publishers, San Francisco, 2005.

[52] N. Woodcock, A. Green, M. Starkey, Social CRM as a business strategy, Journal of Database Marketing & Customer Strategy Management (18:1) (2011) 50–64.

[53] X. Yu, Y. Liu, J.X. Huang, A. An, Mining online reviews for predicting sales performance: a case study in the movie domain, IEEE Transactions On Knowledge And Data Engineering (24:4) (2012) 720–734.

[54] Z. Zhang, Weighing stars: aggregating online product reviews for intelligent E-commerce applications, IEEE Intelligent Systems (September/October 2008) 42–49.

[55] Z. Zhang, B. Varadarajan, Utility scoring of product reviews, Proceedings of the ACM SIGIR Conference on Information and Knowledge Management (CIKM), ACM, Arlington, Virginia, 2006, pp. 51–57.

Thomas L. Ngo-Ye is an Assistant Professor of Management Information Systems at Dalton State College. He received his Ph.D. in Management Information Systems from the Lubar School of Business, University of Wisconsin-Milwaukee, in 2011. His research interests are in business intelligence and analytics data mining, text mining, sentiment analysis e-Commerce, and trust in information technology. His research has been published in ACM Transactions on MIS, International Journal of Intelligent Information Processing, and Is sues in Information Systems. He has also presented his research at premier IS conferences, including the International Conference on Information Systems (ICIS), Americas Conference on Information Systems (AMCIS), and Workshop on Information Technologies and Systems (WITS). He received the best research paper award at the BI Congress held in Orlando in 2012.

Atish P. Sinha is a Professor of Information Technology Management and a Business Advisory Council Research Fellow at the Sheldon B. Lubar School of Business, University of Wisconsin-Milwaukee, He earned his Ph.D. in business, with a concentration in Artificial Intelligence. from the University of Pittsburgh. His current research interests are in the areas of business intelligence and analytics, data mining, text mining, service-oriented computing, and healthcare informatics. His research has been published in several journals, including ACM Transactions on MIS; Communications of the ACM; Decision Support Systems; IEEE Transactions on Engineering Management; IEEE Transactions on Software Engineering; IEEE Transactions on Systems, Man, and Cybernetics; Information Systems Research; International Journal of Human-Computer Studies; Journal of the Association for Information Systems; and Journal of Management Information Systems. Professor Sinha is a member of ACM, AIS, and INFORMS. He served as the program co-chair of the 6th Design Science Research in Information Systems and Technology (DESRIST) conference, and as the co-chair of the 16th Workshop on Information Technologies and Systems (WITS).
