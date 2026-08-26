---
otero_id: 2492
otero_key: "5CK66C9A"
title: "Capturing the essence of word-of-mouth for social commerce: Assessing the quality of online e-commerce reviews by a semi-supervised approach"
authors: "Xiaolin Zheng; Shuai Zhu; Zhangxi Lin"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.06.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Capturing the essence of word-of-mouth for social commerce: Assessing the quality of online e-commerce reviews by a semi-supervised approach

Xiaolin Zheng <sup>a,</sup>⁎, Shuai Zhu <sup>a</sup>, Zhangxi Lin <sup>b,c</sup>

<sup>a</sup> College of Computer Science, Zhejiang University, No. 38, Zheda Road, Hangzhou 310027, China

<sup>b</sup> Center for Advanced Analytics and Business Intelligence, Texas Tech University, Lubbock, TX 79409-2101, USA

<sup>c</sup> Key Lab of Financial Intelligence and Financial Engineering, Southwestern University of Finance and Economics, Chengdu, Sichuan, 611130, China

## a r t i c l e i n f o

Article history: Received 28 April 2012 Received in revised form 28 April 2013 Accepted 9 June 2013 Available online 15 June 2013

Keywords: Online review Review quality Review mining Semi-supervised learning Social network

## a b s t r a c t

In e-commerce, online product reviews signi<sup>fi</sup>cantly in<sup>fl</sup>uence the purchase decisions of buyers and the marketing strategies employed by vendors. However, the abundance of reviews and their uneven quality make distinguishing between useful and useless reviews dif<sup>fi</sup>cult for potential customers, thereby diminishing the bene<sup>fi</sup>ts of online review systems. To address this problem, we develop a semi-supervised system called Online Review Quality Mining (ORQM). Embedded with independent component analysis and semi-supervised ensemble learning, ORQM exploits two opportunities: the improvement of classi<sup>fi</sup>cation performance through the use of a few labeled instances and numerous unlabeled instances, and the effectiveness of the social characteristics of e-commerce communities as identi<sup>fi</sup>ers of in<sup>fl</sup>uential reviewers who write high-quality reviews. Three complementary experiments on datasets from Amazon.com show that ORQM exhibits remarkably higher performance in classifying reviews of different quality levels than do other well-accepted state-of-the-art text mining methods. The high performance of ORQM is also consistent and stable even under limited availability of labeled instances, thereby outperforming other baseline methods. The experiments also reveal that (1) the social features of reviewers are important in deriving better classi<sup>fi</sup>cation results; (2) classi<sup>fi</sup>cation results are affected by product type given the different purchase habits of consumers; and (3) reviews are contingent on the inherent nature of products, such as whether they are search goods or experience goods, and digital products or physical products, through which purchase decisions are in<sup>fl</sup>uenced.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Empowered by cutting-edge social media, internet-based social communities have signi<sup>fi</sup>cantly contributed to the success of online businesses [1]. Current online retail commerce is characterized by many-to-many transactions, instead of the traditional one-to-one relationship between sellers and buyers, closely tying the parties involved in various social networks that center on a given product. That is, sellers form alliances through links to products for brand selling, buyers share shopping experiences in online virtual communities, and these two types of networks interact with each other, thereby generating positive propensity towards a more effective market. E-commerce oriented communities have thus far remained popular given that they are constantly updated with enriched features and services, enabling buyers to enjoy informative shopping facilities and retailers to build strong customer loyalty. Such communities have also considerably improved market ef<sup>fi</sup>ciency. All these advantages indicate the advent of social shopping and social commerce. The former is based primarily on word-of-mouth in electronic marketing, and the latter is referred to as the retail and referral network of individual sellers/shops for products sold online. Both are underpinned by advanced online social media.

E-commerce communities have given rise to a substantial volume of consumer-generated information, including online reviews of products or sellers, online transaction ratings, and scores on the different criteria provided by the electronic market. Such information exerts a huge in<sup>fl</sup>uence on the evolution of e-commerce. The in<sup>fl</sup>ux of user-generated contents re<sup>fl</sup>ects the wide acceptance of key Web 2.0 characteristics, such as user-centered design and information sharing. User-generated contents, typically product reviews, can be exploited through econometrics and data mining analysis [2]. With the help of a modi<sup>fi</sup>ed regression model, retailers can also predict the effectiveness of reviews in sales generation. Determining consumers' true opinions from reviews of existing product improvements or new product developments is helpful for manufacturers. Online review analysis can help retailers implement targeted marketing, sales prediction, and customer relationship management. From a consumers' perspective, effective and authentic reviews have become invaluable sources of shared opinions about products; these opinions have a guiding effect on purchase decisions.

The abundance of online reviews causes two problems: information overload and quality discrepancy. In particular, the quality of reviews dramatically varies, from very helpful to useless and even spam-like, diminishing the bene<sup>fi</sup>ts gained from online reviews. From a buyer's perspective, therefore, low-quality reviews pose dif<sup>fi</sup>- culties in comprehensively evaluating product quality. Speci<sup>fi</sup>cally, negative evaluations from credible reviewers tend to give rise to herd mentality [3]. In establishing market ef<sup>fi</sup>ciency and providing bene<sup>fi</sup>ts to retailers and consumers, the aforementioned issues make identifying true buyer opinions a critical yet challenging task.

To evaluate the quality of online reviews, researchers have devoted considerable effort to developing text analytics methods, including review quality classi<sup>fi</sup>cation [4,5] and spam detection [6]. These methods employ large-scale training datasets to build classi<sup>fi</sup>cation or prediction models, with data labeling as one of the major tasks in data pre-processing. However, manually labeling a large dataset incurs high costs, and is impractical when applied in industry given the diversity of reviews and the numerous factors that in<sup>fl</sup>uence product evaluations. In addition, a single model may exhibit unstable performance because of lack of generalizability. The major drawback of these methods is that they do not fully use the social characteristics of e-commerce communities, which are distinct attributes of advanced e-commerce. Thus far, many data mining techniques for knowledge discovery from online reviews have presented unstable or poor performance when applied to actual situations.

On the basis of the discussion above, we argue that the current imperfections in review quality classi<sup>fi</sup>cation, which is the preliminary task in further data analysis, can be recti<sup>fi</sup>ed by a semi-supervised classi<sup>fi</sup>cation approach [7]. This branch of machine learning has gained increasing popularity because of its practical value and versatile performance. The most critical advantage of semi-supervised classi<sup>fi</sup>cation is that it requires training datasets that contain only a few labeled instances but numerous unlabeled ones. The general idea of this method is to train a classi<sup>fi</sup>er from a dataset that contains both labeled and unlabeled records, instead of training one with only labeled records. Prior experiments show that, with a suf<sup>fi</sup>ciently accurate classi<sup>fi</sup>er, semi-supervised learning enables highly accurate classi<sup>fi</sup>cation [8]. Inspired by these outcomes, we design and implement the Online Review Quality Mining System (ORQM) based on the semi-supervised classi<sup>fi</sup>cation approach for review quality classi<sup>fi</sup>cation. ORQM is also reinforced with a Co-EM version of the ensemble selection method [7] to optimize the accuracy of classi<sup>fi</sup>cation and the independent component analysis (ICA)-based method for pre-processing mapped features. Speci<sup>fi</sup>cally, ORQM incorporates the comprehensive social features of reviewers, thereby enabling consumers to take advantage of potentially high-quality reviews from in<sup>fl</sup>uential evaluators. The experiments on Amazon.com review datasets, which contain the information on physical and digital products in four categories and on both search goods and experience goods, indicate:

1. The performance of ORQM is superior to that of the most popular supervised methods in terms of seven extensively applied metrics (accuracy (ACC), F-score, receiver operating characteristic curve (AUC), average precision (APR), root mean square error (RMSE), mean cross-entropy (MXE), and mean) [10]. Speci<sup>fi</sup>cally, ICA-based pre-processing further improves and stabilizes the performance of ORQM.

2. ORQM works more effectively than do baseline methods even under a very small number of labeled samples. Adding more labeled samples steadily improves the performance of the proposed system.

3. The social traits of reviewers are more helpful than other features in enhancing quality classi<sup>fi</sup>cation performance, which is also in<sup>fl</sup>uenced by product type. All the methods exhibit a higher performance in the IT product datasets than in the cultural product datasets.

The rest of the paper is organized as follows. Section 2 provides a background to quality mining and presents the literature review. Section 3 discusses the ORQM system. Section 4 describes the experiments on the Amazon.com online review datasets, including details on the performance evaluation, model validation, and feature selection. The conclusions and future research directions are presented in Section 5.

## 2. Related work

Knowledge discovery from online reviews (i.e., review mining) is an interdisciplinary research area that features econometric analysis, consumer psychological modeling, statistical linguistics, natural language processing, opinion mining, and machine learning [9]. It has received much attention from researchers in economics, management, behavioral science, psychology, computer science, and sociology.

In the early stage of review mining research, efforts were devoted to identifying the polarity of reviews (positive or negative) [10]. Particular attention was later paid to determining the in<sup>fl</sup>uence of product reviews on the purchase intentions of consumers from the perspectives of marketing and sociology. For example, Lee et al. [3] investigated the conformity effect of negative reviews on marketing. Econometrists and management experts studied the economic value of reviews and determined consumer needs. Ghose et al. [11] estimated the feature weights of reviews and predicted the sales <sup>fl</sup>uctuations in<sup>fl</sup>uenced by different features. Lee et al. [12] used a combination of association rule mining and graph analysis to accurately identify customer needs.

Despite the contributions of these studies, the robustness and reliability of their results are undermined by the insuf<sup>fi</sup>cient focus on review quality. Given the popularity of online review systems and the abundance of review information, review quality has emerged as an important research issue in social shopping and social commerce. User ratings generally demonstrate an unbalanced distribution [13], a bias further re<sup>fl</sup>ected as the effects of certain factors on project reviews [14]. Therefore, Pipino et al. [15] conducted subjective and objective assessments of data quality, in conjunction with three functional forms of objective metrics, to investigate distribution patterns. To enhance the ef<sup>fi</sup>ciency of this approach, researchers directed more focus toward feature selection for product quality assessments based on online reviews. Social features, such as trust features in social networks, improve the accuracy of predicting review quality [16]. Users constantly search for helpful reviews that enable them to more ef<sup>fi</sup>ciently and precisely make decisions, giving rise to the popularity of helpfulness ratings, an extended feature of online reviews [17]. Moghaddam et al. [18] suggested that rating the helpfulness of online reviews be personalized because utility is a subjective concept. Liu et al. [19] found that the helpfulness ratings assigned by regular users differ from those provided by sellers, who design speci<sup>fi</sup>c features for detecting helpful reviews on the basis of a retailers perspective. Other relevant studies emphasized the detection of spam reviews and untrustworthy members. Hu et al. [20] empirically found that review abuse occurs in Amazon.com and Barnes Noble, and Ku et al. [21] proposed a method for distinguishing members in opinion-sharing communities for products; the distinction is conducted on the basis of member reviews and trust networks [20].

Most of these methods rely on large manually labeled training datasets, making them time consuming and less scalable. For example, Godfrey et al. [22]reported that human experts have to spend as many as 400 h transcribing an hour of conversational speech corpus. Furthermore, methods that rely solely on a single machine-learning model normally suffer from diminished generalizability and overlook social attributes.

Semi-supervised learning and ensemble learning are among the promising methods for overcoming these problems. Semi-supervised learning models are derived from traditional learning methods, including semi-supervised SVM [23], graph-based semi-supervised learning [24], and co-training [25]. Co-EM, a variant of co-training, has been extensively used in semi-supervised learning. In the co-training technique, an instance in a dataset has two views, each described by different feature sets with complementary information on the instance [23]. Two separate classi<sup>fi</sup>ers are trained using the labeled instances in each view, and the most con<sup>fi</sup>dent unlabeled instance is applied until all the instances are exhausted. Additionally, Co-EM [26] improves co-training by building a probability model that enables classi<sup>fi</sup>ers to teach each other, and leverages the EM algorithm to estimate parameters.

Semi-supervised learning markedly enhances the performance of a classi<sup>fi</sup>cation model while requiring considerably fewer labeled instances than does supervised learning; the unlabeled instances in a training dataset also contribute to classi<sup>fi</sup>cation or cluster modeling. Nonetheless, semi-supervised learning does not always yield good results [27]. To acquire the full bene<sup>fi</sup>ts of this approach, the co-training based method must typically comply with two assumptions [28]:

1. Each classi<sup>fi</sup>er trained on a corresponding view of instances performs suf<sup>fi</sup>ciently well when provided enough labeled instances.

2. Views are conditionally independent of one another given their class labels.

Assumption 1 ensures that each classi<sup>fi</sup>er provides another classi-<sup>fi</sup>er more accurately classi<sup>fi</sup>ed instances, and the second assumption guarantees that the newly added unlabeled instances are informative enough to update the classi<sup>fi</sup>cation model. If Assumption 2 were not held, selected instances would be highly similar, and therefore, less useful, eventually diminishing model performance.

Given the mandatory compliance with the two assumptions, some co-training based methods, such as Co-EM SVM [23] and Bayesian co-training [25], manually assign independent views, an approach that presents nongeneralizability and inaccuracy. The performance of SVM and Bayesian classi<sup>fi</sup>ers may not be suf<sup>fi</sup>ciently satisfactory for labeling unlabeled data. These drawbacks motivate our decision to embed the ORQM system with ICA [29] and use semi-supervised ensemble learning [30] to address the aforementioned problems.

## 3. Problem formalization

The extent of uselessness varies per case; useful and useless reviews are not clearly distinguished, challenging the implementation of ORQM. People may also have various criteria for product review quality, which depend on their roles in an e-commerce process, personal experiences or backgrounds, and product types. In a broad sense, therefore, the quality of an online review is subjective and context relevant. A helpful review likely possesses the following characteristics:

1. It provides as many appraisable contents as possible to encompass detailed descriptions of product features. For example, a helpful cell phone review tends to exhaustively describe product aspects, including operating system, display, battery duration, and weight. It also presents comprehensive personal experiences and opinions that do not echo other product descriptions or reviews;

2. It has few spelling and grammatical errors, as well as short sentences made up of familiar words or terms, and presents more relevant contents about a product;

3. The provider of a useful review tends to be active in reviewer communities and receives positive feedback from others. The review systems of leading e-commerce sites, such as Amazon.com, are actually social networks. The implicit and explicit feedbacks in such social networks represent the strength of the connection among the reviewers in these networks. Therefore, the average support number of a review is key to the quality of the review [18].

We de<sup>fi</sup>ne useless reviews as those containing spamming or low-quality contents [4]. Review spam is analogous to Web spam [31], through which spammers post malicious appraisals of speci<sup>fi</sup>c products to damage the reputation of these goods or mislead consumers. Although low-quality reviews are not products of malicious intent, they provide little information, and therefore, little additional value to consumers. Carelessly written reviews may contain numerous syntactic or grammatical mistakes and little personal empirical feedback. Shoppers are unlikely to refer to these reviews when making purchase decisions.

A review system is related to three entities: the items evaluated (products and services), the reviews of each item, and the communities to which reviewers/consumers belong. We denote these entities as I, R, and C, respectively. The demographics of the reviewers and their social network information form the social context of reviews. Consequently, we de<sup>fi</sup>ne the social feature of a review as follows:

De<sup>fi</sup>nition 1. For each review R, the social feature (SF) of R is denoted as $\mathrm { S F ( R ) } = < \mathsf { D } , \mathsf { S R } , \mathsf { C } >$ , which includes consumers (C), their social relationship (SR), and their demographics (D).

Traditional quality studies rely primarily on text-based features [15,32], which are de<sup>fi</sup>ned as follows:

De<sup>fi</sup>nition 2. Text-based features (TB) of a review (R) are de<sup>fi</sup>ned as $\mathrm { T B } ( \mathrm { R } ) = < \mathrm { I D } , \mathrm { C D } , \mathrm { R D } >$ , which includes intrinsic data quality, contextual data quality, and representational data quality [33].

A review R can be either labeled (L) or unlabeled (U). Each labeled review $r _ { i } \in L$ is assigned a numeric score $S _ { r _ { i } } ,$ which represents the true helpfulness degree of $r _ { i \cdot } \ \{ S _ { r _ { i } } \}$ can be collected from a feedback system available in many online social commerce platforms, such as the helpful voting system in Amazon.com, or manually labeled by annotators. In this paper, we adopt the former.

Consequently, the input raw data for ORQM can be denoted as $\{ \mathrm { L U U } , \{ \mathsf { S } _ { \mathrm { r _ { i } } } \} , \mathsf { S F } ( \bar { \mathsf { R } } ) , \mathsf { T B } ( \mathsf { R } ) \bar  \} .$ A classi<sup>fi</sup>cation function f is trained to esti-<sup>ð Þ ð Þ</sup>mate whether a review is helpful or useless (including spamming, replicating, or low quality reviews) using the following formula:

$$
f (R _ {i}) \rightarrow \left\{\begin{array}{c}\text { Useful,   ith   review   is   useful }\\\text { Spam|Duplicate|Low - quality,   otherwise }\end{array}\right.\tag{1}
$$

where $R : = \{ \cup R _ { i } , i = 1 , . . . , n . \}$ and $R _ { i }$ is the ith review. f maps the review feature space into the numerical quality value space. The continuous value of f can be further converted into the binary decision (helpful or useless discrimination) by ROC analysis using kappa statistics, which is measured by two annotators to determine a threshold $\theta . ^ { 1 }$ Previous studies focused on manipulating supervised learning models [34,32] to <sup>fi</sup>nd a quality predictor P on {L, TB(R)}. Our novel semi-supervised method, i.e., Co-EM ensemble learning, takes advantage of L, U, and SF to enhance P.

The three steps taken in verifying the effectiveness of our methods are discussed as follows. First, we select three typical supervised learning models and three typical semi-supervised models as baseline predictors, together with our model trained on {SF(R), TB(R)} to compare model performance. Then, we alter the input of each model by gradually increasing its input instance number. Finally, we investigate the manner by which quality predictor P is enhanced by the addition of an SF. In the succeeding section, we discuss the mechanism of our ORQM system.

## 4. The anatomy of ORQM

ORQM incorporates the social characteristics of reviewers to evaluate the quality of reviews with an extended Co-EM ensemble learning method. The ORQM system comprises three components: the system structure, the features of reviews extracted for data mining, and the principle of Co-EM ensemble learning with ICA-based data transformation. These components constitute the mechanism of ORQM.

As shown in Fig. 1 review mining in ORQM involves three stages accomplished by three subsystems: feature extraction, ICA, and Co-EM ensemble learning. The feature extraction subsystem pre-processes raw datasets to build a primitive feature space. The ICA subsystem converts the feature space into an appropriate form to optimize the performance of Co-EM ensemble learning. The Co-EM ensemble learning subsystem classi<sup>fi</sup>es online reviews into two classes in accordance with their characteristics.

In the ORQM work<sup>fl</sup>ow, the ICA subsystem transforms the original feature space into two mutually independent projection spaces. This transformation underpins the Co-EM ensemble learning subsystem, enabling the satisfaction of Assumption 2, as stated in Section 2. Moreover, the AdaBoost method in SVM [35] in the Co-EM ensemble learning subsystem manipulates the ensemble classi<sup>fi</sup>ers for Co-EM learning, enabling the satisfaction of Assumption 1. This way, ORQM can function in correspondence with the best performance of co-training based methods.

## 4.1. Feature extraction

The features extracted from online review corpuses contribute major information to review quality mining. In a study by Wang and Strong [33], a hierarchical text-based quality framework was constructed along three dimensions: intrinsic data quality, contextual data quality, and representational data quality. According to the authors [18], social features are speci<sup>fi</sup>cally important in online review quality mining because these attributes, which are used to quantify the social features of reviewers, are strongly associated with review quality. This relationship stems from the social contingence of the information sent by customers and retailers on social networks. On the basis of these considerations, we observe that reviewers with solid reputations post more high-quality reviews than do ordinary reviewers, an observation also con<sup>fi</sup>rmed in [36]. Thus, we claim that social features are effective components of review mining because they capture the social characteristics of reviewers and their relationships in social networks. We select six features from the social category (Table 1).

The rationale behind the selection of these social features lies in the fact that people with strong reputations in an e-commerce community tend to provide more in<sup>fl</sup>uential discussions, making their reviews more helpful [1,2]. The more detailed considerations for these features are discussed as follows. Historical ranking (f28) and recent ranking of reviewers (f27) show that reviewers with high ranks, more personal information, and more helpfulness votes, are expected to be high-quality review writers. Social commerce communities, such as Amazon.com, often rank reviewers in accordance with number of reviews, helpfulness rate, and total helpfulness votes received. Therefore we take advantage of current and historical rank to distin guish high-quality reviews.

A social network normally contains some hub nodes which have a high degree of centrality [37]; these nodes are recognized as opinion leaders, and hold highly regarded reputations and in<sup>fl</sup>uence in marketing. Studies also show that opinion leaders may deliver extra product information, in<sup>fl</sup>uence the product adoption process, and enlarge market size [38], making them suitable agents for viral marketing [39]. In our work, Top reviewer <sup>fl</sup>ag (f30) is used for representing the in<sup>fl</sup>uence of opinion leaders.

![](/api/attachments/5CK66C9A/fulltext/images/58aa8d5c8f4e56005ddc7fb5db19c91457eca3de075c7ccd8b6056763d847ed2.jpg)  
Fig. 1. ORQM structure

Total helpful votes (f29) that each reviewer receives are de<sup>fi</sup>ned as the degree of attention that a reviewer receives. To measure the extent of activity of reviewers in a community, we propose using Number of reviews posted by each reviewer (f31) and Number of disclosed demographics (f32), including number of friends, interests, and locations.

In addition to social features, text-based features in intrinsic, contextual, and accessible categories are carefully designed to capture the quality of reviews, following previous research. The extraction of these features is discussed in the experiment section. The descriptions of these features are provided in Appendix A. We use 32 features falling under four categories for review mining.

## 4.2. ICA-based data transformation

As a statistical method for separating a multivariate vector into additive subcomponents, ICA is widely used in statistics, signal processing (blind source separation), wavelet transform, and machine learning. It converts original multi-dimensional random vectors into statistically independent components [29]. In ORQM, ICA is a key step in transforming the original feature space into a conditional independence projection feature space, which makes our input for Co-EM ensemble learning more robust. A typical ICA problem is de-<sup>fi</sup>ned as follows.

De<sup>fi</sup>nition 3. $X = ( x _ { 1 } , x _ { 2 } , . . . , x _ { m } ) ^ { T }$ is an observed m-dimensional random vector, and $\boldsymbol { S } = ( s _ { 1 } , s _ { 2 } , . . . , s _ { n } ) ^ { T }$ is an n-dimensional component vector, the components of which are statistically mutually independent. The ICA problem is a linear transformation as follows:

$$
X = W S\tag{2}
$$

where $\mathsf { W }$ is an m × n static matrix for estimation, and the components of $s _ { i }$ must be as statistically independent from one another as possible [29].

ICA can be conducted with the help of mutual information, which measures W by minimizing mutual information among the features in X [29,40]:

$$
\operatorname{Min} _ {X} I (X) = - H (X) + \sum_ {i = 0} ^ {N - 1} H (X (i))\tag{3}
$$

where $X ( i )$ is the ith component of $X , I ( X )$ is the measure of mutual information for $X ,$ and $H ( X ( i ) )$ is the entropy of $X ( i )$

An approximate expression of $I ( X )$ can be obtained using the Edgeworth expansion [41] as follows:

$$
I (X) \approx C - \sum_ {i = 0} ^ {N - 1} \left(\frac {1}{1 2} \kappa_ {3} ^ {2} (X (i)) + \frac {1}{4 8} \kappa_ {4} ^ {2} (X (i)) + \frac {7}{4 8} \kappa_ {4} ^ {4} (X (i)) - \frac {1}{8} \kappa_ {3} ^ {2} (X (i)) \kappa_ {4} (X (i))\right)\tag{4}
$$

where κ denotes the cumulant of its corresponding random variable.

Table 1 Social features.

<table><tr><td>Variables</td><td>Description</td></tr><tr><td>NRR (f27)</td><td>Reviewer rank in the last few days</td></tr><tr><td>CRR (f28)</td><td>Historical reviewer rank</td></tr><tr><td>HV (f29)</td><td>Total helpfulness votes received</td></tr><tr><td>TP (f30)</td><td>Top reviewer flag, if the reviewer is of top type</td></tr><tr><td>NPI (f31)</td><td>Number of personal information items offered</td></tr><tr><td>TRN (f32)</td><td>Number of total posted reviews</td></tr></table>

The optimization problem can be solved by gradient descent. The t-step iteration is obtained as follows:

$$
\left\{ \begin{array}{l} W (t) = W (t - 1) + \mu (t) \Big (W ^ {- T} (t - 1) - E \Big (\phi (S) x ^ {T} \Big) \Big) \\ W (t) = W (t - 1) + \mu (t) \Big (I - E \Big [ \phi (S) S ^ {T} \Big ] W ^ {- T} (t - 1) \Big) \end{array} \right..\tag{5}
$$

After a statistically independent feature vector S is generated by ICA, it can be randomly split into two vectors. Two Co-EM ensemble classi<sup>fi</sup>ers can be trained by mutual reinforcement (the pseudo-code of the ICA algorithm can be found in Appendix B).

Finally, the values of the available features extracted from online reviews, denoted as V, are split into two disjoint sets $V _ { 1 }$ and $V _ { 2 } .$ Each instance can be represented as $\{ L \cup U , V _ { 1 } ( S F ( R ) \cup T B ( R ) )$ $V _ { 2 } ( S F ( R ) \cup T B ( R ) ) \}$ . Here, the second and third components are vectors over $V _ { 1 }$ and $V _ { 2 } ,$ respectively.

## 4.3. Co-EM ensemble learning

Co-training and Co-EM methods can use unlabeled data to enhance performance when these data are trained on independent views, but Co-EM requires a classi<sup>fi</sup>er to estimate class probability of instance. The Co-EM SVM method that we adopt is an extension of the general Co-EM method, reinforced by SVM for text mining [23]. We also improve Co-EM SVM by enhancing SVM with the ensemble approach.

Krogh [42] stated that an ensemble-enhanced model exhibits high generalization performance when the average error rate of component classi<sup>fi</sup>ers is low, and the extent of difference among the component classi<sup>fi</sup>ers is suf<sup>fi</sup>ciently large. To deliver versatile performance, therefore, diversity among component classi<sup>fi</sup>ers must be kept as high as possible when ORQM exploits unlabeled instances. To develop the Co-EM ensemble learning algorithm, three problems must be solved: constructing robust ensembles to satisfy the diversity requirement, estimating the class probability of unlabeled instances, and developing a learning algorithm that uses unlabeled instances.

To address the <sup>fi</sup>rst problem, we introduce the AdaBoost algorithm [35] into the SVM ensemble construction (AdaBoost \_ SVM). The proposed AdaBoost\_SVM obtains better generalization ability than SVM alone for imbalanced classi<sup>fi</sup>cation tasks [35], consequently producing high bene<sup>fi</sup>ts in quality classi<sup>fi</sup>cation problems, as the real quality distribution is extremely biased [13]. (AdaBoost \_ SVM) re-weighting the instances by <sup>fi</sup>rst assigning a training sample with a large weight δ and then decreasing this weight, so that SVM classi-<sup>fi</sup>ers initially perform poorly before acquiring stronger ability later on and keeps improving the classi<sup>fi</sup>cation performance. Controlling δ not only prevents (AdaBoost \_ SVM) from over<sup>fi</sup>tting, but also facilitates higher generalization performance.

To solve the second problem, we follow the principles of semi-supervised learning. Let us denote $U ^ { + }$ and $U ^ { - }$ as helpful and useless unlabeled reviews, respectively, and $L ^ { + }$ and $L ^ { - }$ as helpful and useless labeled reviews, respectively. The task is to estimate the class probability $\hat { P } ( y | x _ { i } ^ { * } ) , x _ { i } ^ { * } { \in } U , y =$ helpful for $U ^ { + }$ or useless for $U ^ { - }$ As $\begin{array} { r } { \hat { P } ( y | x _ { i } ^ { * } ) = \frac { \hat { P } ( x _ { i } ^ { * } | y ) \hat { P } ( y ) } { p ( x _ { i } ^ { * } ) } , } \end{array}$ , the prior probabilities $\hat { P } ( y )$ can be derived from $L ^ { + }$ and $\begin{array} { r } { L ^ { - } , \thinspace \thinspace \mathrm { e . g . } , \thinspace \thinspace P ( + ) = \frac { L ^ { + } } { L } . } \end{array}$ In each iteration, the unlabeled data are split into $U ^ { + }$ and $U ^ { - }$ with the ratio $\hat { P } ( y )$ and the unlabeled instance <sup>ð</sup>with the highest AS(x<sup>∗</sup>) appended to $L ^ { + }$ , where $A S ( { } ^ { \cdot } { } )$ denotes the AdaBoost\_SVM classi<sup>fi</sup>er.

If the decision function value is assumed normally distributed as $p ( A S ( X ) | y ) \sim N [ \mu , \sigma ^ { 2 } ]$ [43], according to the law of large numbers, μ and $\sigma ^ { 2 }$ for $U ^ { + }$ and $U ^ { - }$ can be estimated as the following, where $y \in$ {helpful,useless} and C is a constant:

$$
\mu_ {y} = \frac {C}{| U ^ {y} | + | L ^ {y} |} \left(| L | \sum_ {x \in L} A S (x) + | U | \sum_ {x \in U} A S (x)\right)\tag{6}
$$

$$
\sigma_ {y} ^ {2} = \frac {C}{\sqrt {| U ^ {y} | ^ {2} + | L ^ {y} | ^ {2}}} \left(\sum_ {x \in U, (x, y) \in L} \left(A S (x) - \mu_ {y}\right) ^ {2}\right).\tag{7}
$$

Finally, the class probabilities $\hat { P } ( y | x _ { i } ^ { * } )$ can be inferred from the Gaussian Maximum Likelihood of Eqs. (5) and (6) and prior probabilities $\hat { P } ( y )$

$$
\hat {p} \left(y | x _ {i} ^ {*}\right) = \frac {N \left[ \mu_ {y} , \sigma_ {y} ^ {2} \right] \left(A S (x _ {i} ^ {*})\right) P ^ {\wedge} \left(y\right)}{N \left[ \mu_ {y} , \sigma_ {y} ^ {2} \right] \left(A S (x _ {i} ^ {*})\right) P ^ {\wedge} \left(y\right) + N \left[ \mu_ {y} , \sigma_ {y} ^ {2} \right] \left(A S (x _ {i} ^ {*})\right) P ^ {\wedge} \left(\overline {{y}}\right)}.\tag{8}
$$

For the third problem, we designed a method for training ensembles based on labeled data, unlabeled data, and class probabilities $\hat { p } \left( y | x _ { i } ^ { * } \right)$ . In the simplest way, in each iteration of Co-EM ensemble learning, the ensemble $A S _ { i }$ examines each instance in U. If the number of component classi<sup>fi</sup>ers voting for some label exceeds a given threshold τ, then the unlabeled instances with their class probabilities $\hat { p } \left( y | x _ { i } ^ { * } \right)$ are placed in the labeled dataset L.

However, in some cases, the number of unlabeled instances added to the labeled dataset L can be very large or even equal to the size of U. In this case, when the learned model, especially in some initial iterations, has not fully satis<sup>fi</sup>ed the underlying normal distribution, then it may affect the performance by leveraging a large amount of automatically misclassi<sup>fi</sup>ed labeled data.

Thus, Nigam et al. [44] proposed that each unlabeled instance should be assigned a <sup>fi</sup>xed weight. Using a similar idea, in our model, the weight of an instance is given by the probabilistic con<sup>fi</sup>dence of an ensemble. By introducing the soft weight, it not only reduces the negative effect of large automatically labeled data but also makes the algorithm insensitive to τ.

Utilizing ensemble learning makes labeling the unlabeled instances much more accurate than using a single classi<sup>fi</sup>er, but the misclassi<sup>fi</sup>cation of unlabeled instances is unavoidable. Moreover, one of the disadvantages of the EM algorithm is that it tends to converge into the local optima. Thus, we added the slack variable $C _ { s }$ to each component SVM classi<sup>fi</sup>er of the ensemble following the smoothing strategy of TSVM [45].

The pseudo-code of Co-EM ensemble learning is available in Appendix C. The algorithm <sup>fi</sup>rst constructs two SVM ensembles and then transforms the original features into statistically independent feature subsets $V _ { 1 }$ and $V _ { 2 } .$ Then, it initializes two ensembles and trains two ensembles $E ^ { 1 }$ and $E ^ { 2 }$ on $V _ { 1 }$ and $V _ { 2 } ,$ respectively. The unlabeled data are split iteratively according to the estimated probability through mutual learning iteration. After convergence, the unlabeled data are used up. Finally, the trained classi<sup>fi</sup>ers for quality classi<sup>fi</sup>cation are obtained.

## 5. Experimental evaluation

## 5.1. Experiment design

## 5.1.1. Experiment scheme

We conduct three complementary experiments. The <sup>fi</sup>rst is designed to compare ORQM with several state-of-the-art supervised, semi-supervised, and unsupervised methods. The second experiment evaluates these models along the dimensions of different sample sizes and scenarios with/without ICA. The last experiment is intended to examine the effects of social features on ORQM.

These experiments match the three indispensable steps of review quality mining systems: review corpus shifting, pre-processing, and learning. Consequently, these tests adequately cover the dimensions of scope, depth, and factorial diversity in each sub-system in ORQM.

## 5.1.2. Dataset

We collect data from Amazon.com, one of the major representative sources of research data. The June 2006 dataset contains 5.8 million reviews posted by 2.14 million reviewers for 1.2 million products in four categories (Table 2). We select the four categories on the basis of size; categories that are too large or too small are excluded. The same dataset categories were also used by Jindal et al. [6]. These reviews cover both search products, such as DVD/VHS and mProducts (IT products such as computers,), and experience products, such as music and books. All reviews contain information about the review contents, product attributes, and reviewer attributes (Table 3).

Table 2  
Descriptions of Amazon.com review datasets.

<table><tr><td>Category</td><td>Reviews</td><td>Products</td><td>Reviewers</td></tr><tr><td>Music</td><td>1,327,456</td><td>221,432</td><td>503,884</td></tr><tr><td>Books</td><td>2,493,087</td><td>637,120</td><td>1,076,746</td></tr><tr><td>DVD/VHS</td><td>633,678</td><td>60,292</td><td>250,693</td></tr><tr><td>mProducts</td><td>228,422</td><td>36,692</td><td>165,608</td></tr><tr><td>All</td><td>5,838,032</td><td>1,195,133</td><td>2,146,048</td></tr></table>

## 5.1.3. Metrics

As previously stated, we apply accuracy (ACC), F-score, receiver operating characteristic curve (AUC), average precision (APR), root mean square error (RMSE), mean cross-entropy (MXE), and mean [46] in assessing the performance of ORQM in review quality mining. These metrics are commonly used in other models to measure the performance of such models; thus, they serve as standards for testing the performance of ORQM. Among the measures, ACC and F-score are threshold metrics that usually have a <sup>fi</sup>xed threshold; AUC and APR are order metrics; RMS and MXE are probability metrics; and mean calculates the average values of the other six metrics.

## 5.2. Data extraction and transformation

Two tasks are conducted in preparing pre-text mining data: feature extraction and transformation, which involve many technical details. The following are the approaches applied to extract or transform a number of important intrinsic features:

1. We use the latent Dirichlet allocation (LDA) method [47] for topic discovery, which is a utility implemented by LingPipe. Given the number of topics (i.e., Feature f2, the value of which is determined by applying Gibbs sampling in parameter estimation [48]), the LDA utility can decompose the term frequency vector of a document into a series of orthogonal vectors of term frequencies;

2. Using Bos method (f3) [9] as the basis, we train another dynamic language model to label each review as either subjective or objective, which then generates the statistics of subjective and objective sentences in reviews, including Feature subject (f7), Object (f8), and Ratio of subjective and objective reviews (f9, i.e. SOR).

Table 3  
Variables of the experiment dataset

<table><tr><td>Review dataset</td><td>Product dataset</td><td>Reviewer dataset</td></tr><tr><td>Reviewer id</td><td>Product id</td><td>Reviewer id</td></tr><tr><td>Product id</td><td>Product name</td><td>Reviewer name</td></tr><tr><td>Date</td><td>Brand</td><td>Rank</td></tr><tr><td>Helpful feedback number</td><td>Sales price</td><td>Top k</td></tr><tr><td>All feedback number</td><td>List price</td><td>Location</td></tr><tr><td>Rating</td><td>Product description</td><td>Birthday</td></tr><tr><td>Title</td><td></td><td>Total review number</td></tr><tr><td>Body</td><td></td><td>New reviewer rank</td></tr><tr><td></td><td></td><td>Classic reviewer rank</td></tr><tr><td></td><td></td><td>Total helpful votes</td></tr><tr><td></td><td></td><td>Total votes</td></tr></table>

3. We jointly use LDA [9] and the Inquirer dictionary <sup>2</sup> to construct two TF-IDF vectors includes Tf-idf vector of product feature words (f10) and Tf-idf vector of sentiment words (f11).

4. We derive f5, the degree of consistency indicates the deviation of a review from its rating, according to Eq. (5) as follows, where P denotes the polarity score and R is the product rating provided by a reviewer.

$$
\text { consistency } = \left\{ \begin{array}{l} 0, (R - 1) \times 2 0 <   P <   R \times 2 0 \\ \left\lfloor \frac {P - (R - 1) \times 2 0}{2 0} \right\rfloor , e l s e. \end{array} \right.\tag{9}
$$

5. With regard to Flesch reading ease score (f21), we adopted the approach by [49] to quantify the legibility of text using the following formula:

$$
\text { Score } = 2 0 6. 8 3 5 - (1. 0 1 5 \times A S L) - (8 4. 6 \times A S W)\tag{10}
$$

where ASL stands for average sentence length, and ASW stands for average syllable number per word.

6. The degree of consistency indicates the deviation of a review from its rating. We derived f5 according to Formula (5), where P denotes the polarity score, and R is the product rating provided by the reviewer. As $0 < P < 1 0 0$ and $1 < R < 5 ,$ , we adopt a linear scheme to map R into the range of 20 in P.

7. (6) Other derived features include a. Polarity feature (f3). It refers to the number of distinct product features of a review. It is built by the hierarchical classi<sup>fi</sup>cation method for sentiment analysis; b. Feature WR (f6). It is the ratio of nouns, verbs, adjectives, and adverbs in a review, a part-of-speech (POS) tagger is trained on Brown corpus.

These approaches are mainly processed through LingPipe<sup>3</sup> and Inquirer dictionary, and the ICA-based feature transformation algorithm is implemented by the MILCA<sup>4</sup> toolkit. The resultant outcomes are review feature vectors to be used for further analytical processes.

## 5.3. Experiment results and analysis

5.3.1. Evaluating the performance of different review mining models in terms of the seven metrics

We measure the Co-EM ensemble learning and baseline methods on the Amazon.com dataset using the 10-cross-validation. Our baseline methods incorporate supervised-learning models, including Random Forest, SVM, and Logistic Regression, semi-supervised models, including Co-EM SVM, Co-Training, Co-EM Bayesian and unsupervised one, namely, KNN clustering. These algorithms are implemented using the machine learning toolkit WEKA<sup>5</sup>. Two sets of 10,000 labeled reviews sampled from the dataset are used for training and testing, respectively. The experiment results are listed in Table 4, from which we obtain the following <sup>fi</sup>ndings.

Finding 1. Co-EM ensemble learning outperforms other methods in review quality classification measured with seven metrics in terms of datasets from four kinds of products.

Table 4 shows that under most of the metrics, the semi-supervised methods produce generally better results than do the supervised methods because the former use unlabeled data to improve performance. The results on the four distinguishable products show that Co-EM ensemble learning achieves remarkably higher performance on each metric than do the supervised methods, especially on ACC and AUC. Co-EM ensemble learning also enhances related semi-supervised learning, such as Co-EM SVM.

Finding 2. Review quality mining with nearly all algorithms, as previously itemized, performs well on the mProduct dataset but relatively underperforms on the music, book, and DVD/VHS datasets.

We attribute this outcome to the heterogeneity of reviews relevant to the nature of the products, in which herd mentality signi<sup>fi</sup>- cantly in<sup>fl</sup>uences virtual social relationships and the effects of online reviews [50,51].

mProducts are search products with tangible characteristics that can be described more objectively, whilst music and books are experience goods with more unstructured features, resulting in more subjective reviews. Thus, online search results for search goods have less depth (time per page) and higher breadth (total number of pages) than those for experience goods [20]. In this way, online reviews exert less in<sup>fl</sup>uence on consumer search and purchase behavior for search goods than for experience goods. If the reviews of search goods are meticulously written, the comments in the reviews can well match the expectation of a prospective consumer. From this perspective, such reviews are good predictors for product quality, and the responses on these reviews are accurate. As the features presented realistically re<sup>fl</sup>ect helpfulness, they in turn enhance the classi<sup>fi</sup>cation performance.

By contrast, the experiences of reviewers in experience goods, such as DVD, music and books, may not be directly adopted by others. Features in many reviews on experience goods for determining helpfulness could become deviational. This outcome eventually diminishes the perceived ability for prospective consumers to identify helpful reviews for their decisions [11]. Speci<sup>fi</sup>cally, models on the book dataset perform the worst, whereas models on the music dataset perform the best. We infer that books are the most experience-independent products, which also have minimum explicit features for quality assessment. Therefore, our experiment <sup>fi</sup>nding in this aspect is consistent with the previous discussion.

## 5.3.2. Testing the influence of labeled samples

The second experiment is designed to evaluate the effect of different training sizes on the performance. We manipulated ORQM to explore the effect of the training sample size and the effect of ICA on the performance of the system. The latter was done by comparing the performance of ORQM with a modi<sup>fi</sup>ed one without ICA. Based on, we obtained the following interesting <sup>fi</sup>ndings:

Finding 3. At different levels of available labeled samples, ORQM consistently outperforms other models on the AUC metric.

Fig. 2 shows that ORQM delivers the highest AUC performance even under extremely few labeled samples. ROC analysis (AUC) is designed to evaluate the classi<sup>fi</sup>cation task with varying class distributions, which are caused by different training samples. Hence, the observation on the AUC of these models is suitable. Supervised methods have poor performance under an excessively small labeled training dataset because of their incapability to use massive unlabeled data. As the number of labeled samples increases, ORQM and the other semi-supervised methods behave more stable than do supervised methods, fully demonstrating the power of semi-supervised learning when adequately conceived and con<sup>fi</sup>gured.

Table 4  
Results of the different algorithms on the Amazon.com datasets.

<table><tr><td rowspan="2">Category</td><td rowspan="2">Algorithm</td><td colspan="7">Metrics</td></tr><tr><td>ACC</td><td>F-score</td><td>AUC</td><td>APR</td><td>RMS</td><td>MXE</td><td>Mean</td></tr><tr><td rowspan="8">mProducts</td><td>Co-EM Ensemble</td><td>0.9915</td><td>0.9744</td><td>0.9969</td><td>0.9899</td><td>0.9807</td><td>0.9978</td><td>0.9885</td></tr><tr><td>Co-EM SVM</td><td>0.9609</td><td>0.874</td><td>0.981</td><td>0.9773</td><td>0.9319</td><td>0.9692</td><td>0.9491</td></tr><tr><td>Co-training</td><td>0.9699</td><td>0.8671</td><td>0.9608</td><td>0.9793</td><td>0.937</td><td>0.9704</td><td>0.9474</td></tr><tr><td>Co-EM Bayesian</td><td>0.9794</td><td>0.88</td><td>0.985</td><td>0.9821</td><td>0.935</td><td>0.9841</td><td>0.9576</td></tr><tr><td>Random forest</td><td>0.9129</td><td>0.852</td><td>0.977</td><td>0.963</td><td>0.929</td><td>0.9293</td><td>0.9272</td></tr><tr><td>LibSVM</td><td>0.9101</td><td>0.879</td><td>0.98</td><td>0.9603</td><td>0.9207</td><td>0.921</td><td>0.9285</td></tr><tr><td>Logic regression</td><td>0.8244</td><td>0.8156</td><td>0.89</td><td>0.8894</td><td>0.86</td><td>0.884</td><td>0.8606</td></tr><tr><td>KNN</td><td>0.7631</td><td>0.7583</td><td>0.7814</td><td>0.7745</td><td>0.7592</td><td>0.7702</td><td>0.7678</td></tr><tr><td rowspan="8">Music</td><td>Co-EM Ensemble</td><td>0.906</td><td>0.9</td><td>0.971</td><td>0.9435</td><td>0.9193</td><td>0.9214</td><td>0.9269</td></tr><tr><td>Co-EM SVM</td><td>0.883</td><td>0.849</td><td>0.944</td><td>0.9207</td><td>0.9005</td><td>0.9112</td><td>0.9014</td></tr><tr><td>Co-training</td><td>0.854</td><td>0.8374</td><td>0.9398</td><td>0.91</td><td>0.8866</td><td>0.9009</td><td>0.8881</td></tr><tr><td>Co-EM Bayesian</td><td>0.889</td><td>0.8672</td><td>0.952</td><td>0.9401</td><td>0.9017</td><td>0.912</td><td>0.9103</td></tr><tr><td>Random forest</td><td>0.876</td><td>0.849</td><td>0.94</td><td>0.9271</td><td>0.8871</td><td>0.9094</td><td>0.8981</td></tr><tr><td>LibSVM</td><td>0.835</td><td>0.808</td><td>0.9373</td><td>0.9331</td><td>0.9147</td><td>0.92</td><td>0.8914</td></tr><tr><td>Logic regression</td><td>0.701</td><td>0.6878</td><td>0.81</td><td>0.776</td><td>0.7193</td><td>0.72</td><td>0.7357</td></tr><tr><td>KNN</td><td>0.692</td><td>0.6749</td><td>0.7245</td><td>0.7137</td><td>0.6883</td><td>0.7059</td><td>0.6999</td></tr><tr><td rowspan="8">Books</td><td>Co-EM Ensemble</td><td>0.8879</td><td>0.8637</td><td>0.9492</td><td>0.9277</td><td>0.8973</td><td>0.9003</td><td>0.9044</td></tr><tr><td>Co-EM SVM</td><td>0.8491</td><td>0.8102</td><td>0.9223</td><td>0.9039</td><td>0.8651</td><td>0.8874</td><td>0.873</td></tr><tr><td>Co-training</td><td>0.8227</td><td>0.7972</td><td>0.9036</td><td>0.8741</td><td>0.8419</td><td>0.864</td><td>0.8506</td></tr><tr><td>Co-EM Bayesian</td><td>0.828</td><td>0.8097</td><td>0.8993</td><td>0.8793</td><td>0.8324</td><td>0.8542</td><td>0.8505</td></tr><tr><td>Random forest</td><td>0.8641</td><td>0.8479</td><td>0.9217</td><td>0.9115</td><td>0.8847</td><td>0.8994</td><td>0.8882</td></tr><tr><td>LibSVM</td><td>0.8041</td><td>0.7769</td><td>0.8974</td><td>0.8505</td><td>0.8211</td><td>0.8479</td><td>0.833</td></tr><tr><td>Logistic regression</td><td>0.6842</td><td>0.6659</td><td>0.7795</td><td>0.7359</td><td>0.6914</td><td>0.7126</td><td>0.7116</td></tr><tr><td>KNN</td><td>0.7144</td><td>0.6831</td><td>0.7292</td><td>0.7261</td><td>0.7014</td><td>0.7185</td><td>0.7121</td></tr><tr><td rowspan="8">DVD/VHS</td><td>Co-EM Ensemble</td><td>0.9019</td><td>0.8881</td><td>0.9599</td><td>0.9331</td><td>0.9097</td><td>0.9217</td><td>0.9191</td></tr><tr><td>Co-EM SVM</td><td>0.8541</td><td>0.8215</td><td>0.9117</td><td>0.8973</td><td>0.8676</td><td>0.8797</td><td>0.872</td></tr><tr><td>Co-training</td><td>0.8083</td><td>0.7768</td><td>0.8794</td><td>0.8411</td><td>0.8192</td><td>0.8215</td><td>0.8244</td></tr><tr><td>Co-EM Bayesian</td><td>0.8872</td><td>0.8769</td><td>0.9257</td><td>0.9193</td><td>0.8992</td><td>0.9137</td><td>0.9037</td></tr><tr><td>Random forest</td><td>0.7036</td><td>0.6875</td><td>0.7795</td><td>0.7437</td><td>0.7179</td><td>0.7338</td><td>0.7277</td></tr><tr><td>LibSVM</td><td>0.6473</td><td>0.6105</td><td>0.7705</td><td>0.7392</td><td>0.7075</td><td>0.7212</td><td>0.6994</td></tr><tr><td>Logistic regression</td><td>0.4741</td><td>0.4629</td><td>0.6038</td><td>0.5731</td><td>0.5059</td><td>0.5302</td><td>0.525</td></tr><tr><td>KNN</td><td>0.7241</td><td>0.6938</td><td>0.7381</td><td>0.7332</td><td>0.7119</td><td>0.7286</td><td>0.7216</td></tr></table>

Finding 4. ICA plays a critical role in ORQM.

The results from a comparison experiment without ICA show that, if the number of labeled samples were larger than a given threshold, the performance of ORQM would diminish upon training on some larger datasets. The decline in performance is due to the inappropriate pre-processing by randomly splitting features without ICA for Co-EM ensemble learning, where the independence assumption no longer holds. Thus, the ICA-based pre-processing increases and stabilizes the performance of ORQM.

## 5.3.3. Evaluating the effects of social features

The last experiment evaluates the effectiveness of social features in ORQM. The performances of ORQM measured in AUC and ACC are listed in Table 5 with different combinations of features. The following are the main <sup>fi</sup>ndings:

## Finding 5. Social features contribute the most to the performance of ORQM.

Social features implicitly take advantage of viral marketing (VM), which diffuses the opinion of products or ads through social networks in a self-replicating way analogous to the spread of viruses or computer viruses [52]. The mechanism of VM is in the cascade effect originated by in<sup>fl</sup>uencers [53], who have high social in<sup>fl</sup>uences and active social actions. Thus, the reviews of in<sup>fl</sup>uencers will likely change the minds and behaviors of consumers.

We <sup>fi</sup>nd that reviewers with a high reputation of high centrality are more likely to post high quality reviews. These opinion leaders also exert great in<sup>fl</sup>uence, namely, diffusion in the social network for marketing, which inevitably in<sup>fl</sup>uences the recognition degree of the quality of their online reviews [54,36]. Thus, consumers in the social commerce community are more likely to follow these opinion leaders. With more consent on their reviews, these opinion leaders are more likely to write more high quality reviews, forming a virtuous circle also known as positive psychology [55]. Thus, social features are strong indicators of review quality.

Finding 6. Next to social features, intrinsic features extracted from the reviews of search goods significantly influence the performance of ORQM.

This <sup>fi</sup>nding is inferred from the results of mProduct data mining in Table 5 but is not applicable to other product categories. This discrepancy is attributed to the nature of intrinsic features, which re<sup>fl</sup>ect review topics, product features, and sentiments, and make these qualities more suitable for products with clearly distinguishable features, such as search goods.

## 6. Conclusion and future work

The review quality problem in e-commerce communities has drawn considerable research attention, because the absence of an effective mechanism for review quality control casts doubt on the results studies on opinion mining, sentiment classi<sup>fi</sup>cation, and review summarization. Review quality mining that guarantees the dependability of the results of the aforementioned studies can provide a solid background for successive related research. Furthermore, placing these studies within a quality control structure yields more accurate results.

In this study, we present the ORQM system to conduct robust, practical, and high-performance review quality mining. The main distinguishing trait of ORQM is that it provides comprehensive functionalities to evaluate the quality of reviews, which not only cover text-based features, such as intrinsic, contextual, and accessible ones, but also creatively introduce social networks features in assessing the signi<sup>fi</sup>cance of online reviews. These social features can capture the social characteristics of reviewers and their relationship within the online business social network, and help to enhance the accuracy and performance of quality classi<sup>fi</sup>cation.

(a) mProduct  
![](/api/attachments/5CK66C9A/fulltext/images/ea141f1fe348583f5b506858eb1176e063a7ab7e7ad2968a17e5a7948f9dabff.jpg)

(b) Music  
![](/api/attachments/5CK66C9A/fulltext/images/73b0ae97d44acac9be80c76863d966ff86457112bdd391ed55a2a9e7ac363a30.jpg)

(c) Books  
![](/api/attachments/5CK66C9A/fulltext/images/bc51416ac1c4b38175741e3f831d61f25ace2ed8588044c69801b7db162c13d4.jpg)

(d) DVD/VHS  
![](/api/attachments/5CK66C9A/fulltext/images/40af9f177349c5d3b4d9075f4cb6e6f4aac9c1ae0112ba5b6e56a79cb1754216.jpg)  
Fig. 2. Algorithms comparison on mProducts, music, books and DVD/VHS of Amazon.com datasets using varied labeled samples

More important, from a technical aspect, we combine ensemble learning and Co-EM learning to enhance the performance of the system. Leveraging the Co-EM version of ensemble learning enables semi-supervised learning, which reduces the requirement of labeled samples, while resulting in more versatile performance compared with existing methods. In addition, ICA pre-processing ensures the robustness and stability of ORQM. These improvements are con-<sup>fi</sup>rmed or supported by three carefully designed experiments.

Table 5  
Results of the feature combinations for ORQM.

<table><tr><td colspan="4">Metrics</td></tr><tr><td>Dataset</td><td>Feature combination</td><td>ACC</td><td>AUC</td></tr><tr><td rowspan="8">mProduct</td><td>Intrinsic feature (1)</td><td>0.8415</td><td>0.8742</td></tr><tr><td>Contextual feature (2)</td><td>0.8766</td><td>0.8907</td></tr><tr><td>Accessibility feature (3)</td><td>0.9036</td><td>0.9328</td></tr><tr><td>Social feature (4)</td><td>0.9212</td><td>0.9391</td></tr><tr><td>(1) + (4)</td><td>0.9263</td><td>0.9471</td></tr><tr><td>(2) + (4)</td><td>0.9211</td><td>0.9457</td></tr><tr><td>(3) + (4)</td><td>0.9364</td><td>0.9572</td></tr><tr><td>(1) + (2) + (3) + (4)</td><td>0.9915</td><td>0.9969</td></tr><tr><td rowspan="8">Music</td><td>Intrinsic feature (1)</td><td>0.8201</td><td>0.8492</td></tr><tr><td>Contextual feature (2)</td><td>0.8679</td><td>0.8845</td></tr><tr><td>Accessibility feature (3)</td><td>0.8602</td><td>0.8798</td></tr><tr><td>Social feature (4)</td><td>0.8814</td><td>0.9132</td></tr><tr><td>(1) + (4)</td><td>0.8871</td><td>0.9265</td></tr><tr><td>(2) + (4)</td><td>0.8899</td><td>0.9395</td></tr><tr><td>(3) + (4)</td><td>0.8931</td><td>0.9463</td></tr><tr><td>(1) + (2) + (3) + (4)</td><td>0.906</td><td>0.971</td></tr><tr><td rowspan="8">Books</td><td>Intrinsic feature (1)</td><td>0.8126</td><td>0.8386</td></tr><tr><td>Contextual feature (2)</td><td>0.8204</td><td>0.8399</td></tr><tr><td>Accessibility feature (3)</td><td>0.8549</td><td>0.8736</td></tr><tr><td>Social feature (4)</td><td>0.8605</td><td>0.8994</td></tr><tr><td>(1) + (4)</td><td>0.8671</td><td>0.9197</td></tr><tr><td>(2) + (4)</td><td>0.8692</td><td>0.9225</td></tr><tr><td>(3) + (4)</td><td>0.8843</td><td>0.9339</td></tr><tr><td>(1) + (2) + (3) + (4)</td><td>0.8879</td><td>0.9492</td></tr><tr><td rowspan="8">DVD/VHS</td><td>Intrinsic feature (1)</td><td>0.8253</td><td>0.8446</td></tr><tr><td>Contextual feature (2)</td><td>0.8271</td><td>0.8495</td></tr><tr><td>Accessibility feature (3)</td><td>0.8566</td><td>0.8796</td></tr><tr><td>Social feature (4)</td><td>0.8792</td><td>0.8997</td></tr><tr><td>(1) + (4)</td><td>0.8894</td><td>0.9214</td></tr><tr><td>(2) + (4)</td><td>0.8831</td><td>0.9183</td></tr><tr><td>(3) + (4)</td><td>0.8902</td><td>0.9328</td></tr><tr><td>(1) + (2) + (3) + (4)</td><td>0.9019</td><td>0.9599</td></tr></table>

As a fundamental framework on review quality evaluation in e-commerce realm, ORQM should not only serve from the perspective of retailers, manufactures, but also bene<sup>fi</sup>t common online shopping consumers. On one hand, a promising opportunity is to use ORQM as a basis for examining the economic value of reviews. Highquality reviews re<sup>fl</sup>ect how people evaluate a product, which features satisfy their needs, and what types of products they prefer. For example, marketing practitioners can build personalized recommendation systems by incorporating ORQM to improve system performance; manufacturers can customize their products to more precisely <sup>fi</sup>t consumer needs; and retailers can adjust their advertising strategies to highlight preferred product features for sales promotions. On the other hand, conducting research from the perspective of consumers is also a worthwhile endeavor. Consumers rely heavily on highquality reviews in making purchase decisions. To save consumers effort in reading a large volume of product reviews, online stores, such as Amazon, provides the sentiment information, the frequency of review access, and the usefulness points of the review from other consumers. However, these utilities do not tell the quality of a review, while a poorly written or spamming review could sometimes be misleading. Therefore, a customer-oriented review search system or a review recommendation system can be valuable to social commerce, in which review quality mining is a vital component. In this way, we can regard ORQM as the fundamental work for building an online review <sup>fi</sup>ltering system in a social commerce environment, in which ORQM can serve as a quality control subsystem for <sup>fi</sup>ltering out useless reviews. Then online consumer can refer historical purchasing records and comments in an easier way, without distracted by tons of useless review information.

1: V = V = null;

Though researchers have presented plenty of creative proposals to move forward in review quality mining, there are still many challenges to be coped with in our future research agenda. Speci<sup>fi</sup>cally, people have different individual perspectives in the justi<sup>fi</sup>cation of a reviews quality. Their criteria of the review quality may vary between helpfulness and uselessness continuously. Thus, applying a uni<sup>fi</sup>ed model that can cope with diverse consumer tastes rooted in different purposes is in an urgent request. We expect the social network-based approach to be a potential solution to this challenge. A promising solution is crowdsourced clustering, a type of crowdsourcing method [56]. For example, given by delegating certain steps of the method to the public, the provision of user-friendly and adaptive quality estimations from different user types will become possible. In this context, even when social information becomes less available because of privacy concerns or other reasons, a social inference mechanism [57] can still be introduced to resolve the shortage of social characteristics.

## Acknowledgments

This work was supported in part by the National Key Technology RD Program (No. 2012BAH16F02), the National Natural Science Foundation of China (Grant No. 61003254 and 91218301), and the Fundamental Research Funds for the Central Universities, as well as Financial Service Innovation Team Development Project at Southwest University of Finance and Economics (2012).

## Appendix A. Features

## A.1. Intrinsic features

Intrinsic features are designated to capture the quality of reviews in their nature inherited in the lexical, syntactical, and semantic constitutions of the individual review. These reviews contain substantive information that may interest consumers. In accordance with this de<sup>fi</sup>nition, we selectively adopted four features previously proposed as intrinsic features and carefully added seven new ones (Table A.6). Among these features, feature polarity (f3) and consistency (f5) are introduced to detect spam reviews, as spammers tend to deviate from the normal practice.

## A.2. Contextual features

Contextual features in Table A.7 are proposed to evaluate the context of each review, as data quality must be aligned to a certain context [33]. Here, the context includes other reviews listed for the same product and editorial descriptions.

## A.3. Accessibility features

Accessibility features in Table A.8 measure the readability of a review. Consumers tend to read reviews that are neither too long and too complex nor too short. Reviews with a moderate amount of

## Table A.6

Intrinsic features.

<table><tr><td>Variables</td><td>Description</td><td>Notes</td></tr><tr><td>RL (f1)</td><td>Length of review</td><td></td></tr><tr><td>Topic (f2)</td><td>Topic number of review</td><td>New</td></tr><tr><td>Polarity (f3)</td><td>Polarity score of the review</td><td>New</td></tr><tr><td>Pfeatures (f4)</td><td>Product feature number in the review</td><td>New</td></tr><tr><td>Consistency (f5)</td><td>Consistency score by comparing f3 and rating</td><td>New</td></tr><tr><td>WR (f6)</td><td>Ratio of nouns, verbs, adjectives, and adverbs in the review</td><td></td></tr><tr><td>Subject (f7)</td><td>Subject sentence number and subject sentence ratio</td><td></td></tr><tr><td>Object (f8)</td><td>Object sentence number and object sentence ratio</td><td></td></tr><tr><td>SOR (f9)</td><td>Ratio of subject and object sentences</td><td>New</td></tr><tr><td>FTFIDF (f10)</td><td>Tf-idf vector of product feature words</td><td>New</td></tr><tr><td>STFIDF (f11)</td><td>Tf-idf vector of sentiment words</td><td>New</td></tr></table>

Table A.7  
Contextual features.

<table><tr><td>Variables</td><td>Description</td><td>Notes</td></tr><tr><td>Simi (f12)</td><td>Cosine similarity between review and product description</td><td></td></tr><tr><td>Dup (f13)</td><td>Cosine similarity between current and previous reviews posted</td><td>NEW</td></tr><tr><td>ED (f14)</td><td>Elapsed time after a review was posted</td><td></td></tr><tr><td>GS (f15)</td><td>Helpfulness score evaluated by helpfulness votes divided by total votes</td><td></td></tr><tr><td>Rat (f16)</td><td>Product rating</td><td></td></tr><tr><td>Div (f17)</td><td>Deviation between current rating and the average rating</td><td>NEW</td></tr></table>

Table A.8  
Accessibility features.

<table><tr><td>Variables</td><td>Description</td></tr><tr><td>SN (f18)</td><td>Sentence number of review</td></tr><tr><td>ASL (f19)</td><td>Average sentence length</td></tr><tr><td>ASW (f20)</td><td>Average number of syllables per word</td></tr><tr><td>FRE (f21)</td><td>Flesh Reading Ease score</td></tr><tr><td>FKG (f22)</td><td>Flesh Kincaid Grade score</td></tr><tr><td>SMOG (f23)</td><td>Years of education required</td></tr><tr><td>SE (f24)</td><td>Number of spelling errors</td></tr><tr><td>ALC (f25)</td><td>Average length of sentences</td></tr><tr><td>ALW (f26)</td><td>Average length of words</td></tr></table>

information, medium length, and elaborated presentations are more acceptable to consumers.

## Appendix B. Independent component analysis preprocessing

Please refer to Algorithm 1 for details.

Algorithm 1. $I C A ( D _ { L } , S e e d , T )$

Input:

Original n-dimensional vector $D _ { L } = \{ x _ { 1 } , x _ { 2 } , . . . , x _ { n } \} ;$

Seed: seed for random function;

T: Threshold for iteration.

Output:

Mutually statistical independent vectors $V _ { 1 } = \{ s _ { 1 1 } , s _ { 1 2 } , . . . , s _ { 1 k } \}$ and $V _ { 2 } = \{ s _ { 2 1 } , s _ { 2 2 } , . . . , s _ { 2 ( n - k ) } \}$

$$
\mathbf {2}: \text {   while   } | W (t) - W (t - 1) | <   T \text {   do   }
$$

$$
\mathbf {3}: W (t) = W (t - 1) + \mu (t) (W ^ {- T} (t - 1) - E (\phi (S) x ^ {T}));
$$

$$
\mathbf {4} \colon W (t) = W (t - 1) + \mu (t) (I - E [ \phi (S) S ^ {T} ] W ^ {- T} (t - 1));
$$

5: end while

$$
S = W ^ {- 1} D _ {L};
$$

7: for i = 1 to length(s) do

8: {V<sub>1</sub>,V<sub>2</sub>} = RandomSplit(S,Seed);

9: end for

10: return $V _ { 1 } , V _ { 2 } .$

## Appendix C. Co-EM ensemble learning algorithm

Please refer to Algorithms 2 and 3 for details. The Algorithm 2 describes the preprocessing step and Algorithm 3 shows the transformation and learning steps.

## Algorithm 2. Co - EM - Ensemble(D<sub>L</sub>,D<sub>U</sub>,C,T,Hi,Hc,MR,Seed,SI,SVMP,E, C<sub>S</sub>) part1

Input:

Labeled review feature vectors $D _ { L } ;$

Unlabeled review feature vectors $D _ { U } ;$

Hill climb iteration number $H _ { l } ;$

optimization metric $H _ { C } ;$

Ratio of models that will be randomly chosen from library in each iteration MR;

Seed of Random number generator Seed; Sort initialization SI; Pool of SVM with different kernel, etc. SVMP; Ensemble E; Smoothing factor $C _ { s } .$ Output: Trained function $C _ { e } ;$

1: $\begin{array} { r } { C _ { S } = \frac { 1 } { 2 } ; } \end{array}$

2: $\operatorname { f o r } i \stackrel { - } { = } 1$ to capacity(s) do

3: $\mathrm { i f ~ l e n g t h ( E ) } < = \mathrm { S I ~ t h e n }$

4: $E \gets E + S V M _ { i } ;$

5: ${ \mathrm { S o r t } } ( \mathbb { E } , \mathrm { H } _ { c } ( S V M _ { i } ) ) ;$

6: else

7: $\mathrm { i f } \ E _ { i \mathrm { ~ - ~ } 1 } < H c ( S V M _ { i } )$ then

8: $E _ { i } = E _ { i - 1 } + S V M _ { i } ;$

9: end if

10: end if

11: end for.

## Algorithm 3. Co - EM - Ensemble(D ,D ,C,T,Hi,Hc,MR,Seed,SI,SVMP,E, C ) part2

1: $I C A ( D _ { L } , D _ { U } )  \{ V _ { 1 } , V _ { 2 } \} ;$ 2: $R a n d o m ( S e e d )  K ;$ 3: $E ^ { 1 } = E ^ { 2 } = n u l l ;$ 4: $\mathrm { f o r } j = 1 t o H _ { i } \mathrm { d o }$ 5: $S V M _ { i } \gets R a n d o m S u b s e t _ { K } ( S V M P ) ;$ 6: $\mathrm { i f } \ H \bar { c } ( S V M _ { i } , V _ { 2 } ) > H c ( E ^ { 1 , 2 } , V _ { 2 } )$ the 7: $E ^ { 1 , 2 } \gets E ^ { 1 , 2 } + S V M _ { j } ;$ 8: else 9: return E<sup>1</sup>,E<sup>2</sup>; 10: end if 11: end for 12: $\hat { p } \left( y | x _ { i } ^ { \prime } \right) \gets D _ { L } ;$ 13: for k = 1toT do 14: for V = 1, 2 do 15: $D _ { U } ^ { + } = ( \hat { p } ( y = 1 ) * | D _ { U } | ) \{ D _ { U } \} ,$ 16: $D _ { U } ^ { - } = D _ { U } - D _ { U } ^ { + } ;$ 17: $\mu _ { + } , \mu _ { - } , \sigma _ { + } , \sigma _ { - }  D _ { L } , D _ { U } ;$ 18: $\forall x _ { k } ^ { * } \in D _ { U } , \hat { p } ( y \middle | x _ { k } ^ { \cdot } )  E _ { k - 1 ^ { \vee } } ;$ 19: $\{ V _ { \nu } \} \to E _ { K } ^ { \nu } { \sf w i t h } C _ { S } ;$ 20: end for 21: $C _ { S } = 2 C _ { S } ;$ 22: end for 23: return $\begin{array} { r } { \frac { 1 } { 2 } \Bigl ( E _ { T } ^ { 1 } + E _ { T } ^ { 2 } \Bigr ) \to C _ { e } . } \end{array}$

## References

[1] A. Stephen, O. Toubia, Deriving value from social commerce networks, Journal of Marketing Research 47 (2) (2009) 215–228.

[2] N. Archak, A. Ghose, P. Ipeirotis, Show me the money!: deriving the pricing power of product features by mining consumer reviews, Proceedings of the 13th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, 2011, pp. 56–65.

[3] J. Lee, D. Park, I. Han, The effect of negative online consumer reviews on product attitude: an information processing view, Electronic Commerce Research and Applications 7 (3) (2008) 341–352.

[4] J. Liu, Y. Cao, C. Lin, Y. Huang, M. Zhou, Low-quality product review detection in opinion summarization, Proceedings of the 2007 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning, ACL, 2007, pp. 334–342.

[5] X. Yu, Y. Liu, X. Huang, A. An, A quality-aware model for sales prediction using reviews, Proceedings of the 19th international conference on World wide web ACM, 2010, pp. 1217–1218.

[6] N. Jindal, B. Liu, E. Lim, Finding unusual review patterns using unexpected rules, Proceedings of the 19th ACM international conference on Information and knowledge management, ACM, 2010, pp. 1549–1552.

[7] A. Mantrach, N. Van Zeebroeck, P. Francq, M. Shimbo, H. Bersini, M. Saerens, Semi-supervised classi<sup>fi</sup>cation and betweenness computation on large, sparse, di rected graphs, Pattern Recognition 44 (6) (2011) 1212–1224.

[8] B. Kulis, S. Basu, I. Dhillon, R. Mooney, Semi-supervised graph clustering: a kernel approach, Machine Learning 74 (1) (2009) 1–22.

[9] B. Pang, L. Lee, Opinion mining and sentiment analysis, Foundations and Trends in Information Retrieval 2 (1–2) (2008) 1–135.

[10] B. Pang, L. Lee, A sentimental education: sentiment analysis using subjectivity summarization based on minimum cuts, Proceedings of the 42nd Annual Meeting on Association for Computational Linguistics, ACL, 2004, p. 271.

[11] A. Ghose, P. Ipeirotis, Estimating the helpfulness and economic impact of product reviews: mining text and reviewer characteristics, IEEE Transactions on Knowledge and Data Engineering 23 (10) (2011) 1498–1512.

[12] T. Lee, Needs-based analysis of online customer reviews, Proceedings of the Ninth International Conference on Electronic Commerce, vol. 258, ACM, 2007, pp. 311–318.

[13] N. Hu, J. Zhang, P. Pavlou, Overcoming the j-shaped distribution of product reviews, Communications of the ACM 52 (10) (2009) 144–147.

[14] A. Talwar, R. Jurca, B. Faltings, Understanding user behavior in online feedback reporting, Proceedings of the 8th ACM Conference on Electronic Commerce, ACM, 2007, pp. 134–142, (1250931).

[15] L. Pipino, Y. Lee, R. Wang, Data quality assessment, Communications of the ACM 45 (4) (2002) 211–218.

[16] H. Min, J. Park, Identifying helpful reviews based on customer's mentions about experiences, Expert Systems with Applications 39 (15) (2012) 11830–11838.

[17] Y. Lu, P. Tsaparas, A. Ntoulas, L. Polanyi, Exploiting social context for review quality prediction, Proceedings of the 19th International Conference on World wide Web, ACM, 2010, pp. 691–700.

[18] C. Au Yeung, T. Iwata, Strength of social in<sup>fl</sup>uence in trust networks in product review sites, Proceedings of the Fourth ACM International Conference on Web Search and Data Mining, ACM, 2011, pp. 495–504.

[19] S. Moghaddam, M. Jamali, M. Ester, Etf: extended tensor factorization model for personalizing prediction of review helpfulness, Proceedings of the <sup>fi</sup>fth ACM international conference on Web search and data mining, AČM 2012 pp. 163-172

[20] Y. Liu, J. Jin, P. Ji, J. Harding, R. Fung, Identifying helpful online reviews: a product designer's perspective, Computer-Aided Design 45 (2013) 180–194.

[21] N. Hu, L. Liu, V. Sambamurthy, Fraud detection in online consumer reviews, Decision Support Systems 50 (3) (2011) 614–626.

[22] J. Godfrey, E. Holliman, J. McDaniel, Switchboard: telephone speech corpus for research and development, Acoustics, Speech, and Signal Processing, 1992, ICASSP-92., 1992 IEEE International Conference on, vol. 1, 1992, pp. 517–520.

[23] U. Brefeld, T. Scheffer, Co-Em support vector learning, Proceedings of the Twenty-<sup>fi</sup>rst International Conference on Machine Learning, vol. 21, Association for Computing Machinery, 2004, pp. 121–128.

[24] R. Johnson, T. Zhang, Graph-based semi-supervised learning and spectral kernel design JEEE Transactions on Information Theory 54 (1) (2008) 275–288

[25] S. Yu, B. Krishnapuram, R. Rosales, R. Rao, Bayesian co-training, Journal of Machine Learning Research 12 (2011) 2649–2680.

[26] S. Bickel, T. Scheffer, Estimation of mixture models using Co-Em, 16th European Conference on Machine Learning, 2005, pp. 35–46.

[27] Y. Li, Z. Zhou, Towards making unlabeled data never hurt, Proceedings of the Twenty Eighth International Conference on Machine Learning, ACM, 2011, pp. 1081–1088.

[28] A. Blum, T. Mitchell, Combining labeled and unlabeled data with co-training, Proceedings of the11th Annual Conference on Computational Learning Theory, ACM, 1998, pp. 92–100.

[29] A. Hyvarinen, Independent Component Analysis by Minimization of Mutual Information, Helsinki University of Technology, 1997. , (City:).

[30] L. Shi, X. Ma, L. Xi, Q. Duan, J. Zhao, Rough set and ensemble learning based semi-supervised algorithm for text classi<sup>fi</sup>cation, Expert Systems with Applications 38 (5) (2011) 6300–6306

[31] E. Lim, V. Nguyen, N. Jindal, B. Liu, H. Lauw, Detecting product review spammers using rating behaviors, 19th International Conference on Information and Knowledge Management, ACM, 2010, pp. 939–948.

[32] Z. Zhang, B. Varadarajan, Utility scoring of product reviews, Proceedings of the 15th ACM International Conference on Information and Knowledge Management, ACM, 2006, pp. 51–57.

[33] R. Wang, D. Strong, Beyond accuracy: what data quality means to data consumers, Journal of Management Information Systems 12 (4) (1996) 5–33.

[34] S. Kim, P. Pantel, T. Chklovski, M. Pennacchiotti, Automatically assessing review helpfulness, Proceedings of the 2006 Conference on Empirical Methods in Natural Language Processing, Association for Computational Linguistics, 2006 pp 423–430

[35] X. Li, L. Wang, E. Sung, Adaboost with SVM-based component classi<sup>fi</sup>ers, Engineering Applications of Artificial Intelligence 21 (5) (2008) 785–795.

[36] P. Van Eck, W. Jager, P. Lee<sup>fl</sup>ang, Opinion leaders' role in innovation diffusion: a simulation study, Journal of Product Innovation Management 28 (2) (2011) 187-203.

[37] J. Goldenberg, S. Han, D. Lehmann, J. Hong, The role of hubs in the adoption processes, Journal of Marketing 73 (2) (2009) 1–13.

[38] S. Aral, D. Walker, Creating social contagion through viral product design: a randomized trial of peer in<sup>fl</sup>uence in networks, Management Science 57 (9) (2011) 1623–1639.

[39] W. Chen, C. Wang, Y. Wang, Scalable in<sup>fl</sup>uence maximization for prevalent viral marketing in large-scale social networks, 16th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, Association for Computing Machinery, 2010, pp. 1029–1038.

[40] H. Stogbauer, A. Kraskov, S. Astakhov, P. Grassberger, Least-dependent-component analysis based on mutual information, Physical Review E 70 (6) (2004) 066123.

[41] A. Papoulis, R. Probability, Probability, Random Variables and Stochastic Processes, vol. 3McGraw-hill, New York, 1991.

[42] A. Krogh, J. Vedelsby, et al., Neural network ensembles, cross validation, and active learning, Advances in Neural Information Processing Systems, 1995. 231–238.

[43] C. Chen, Y. Tseng, Quality evaluation of product reviews using an information quality framework, Decision Support Systems 50 (4) (2011) 755–768.

[44] K. Nigam, A. McCallum, S. Thrun, T. Mitchell, Text classi<sup>fi</sup>cation from labeled and unlabeled documents using EM, Machine Learning 39 (2) (2000) 103–134.

[45] X. Peng, A n-twin support vector machine (n-TSVM) classi<sup>fi</sup>er and its geometric algorithms, Information Sciences 180 (20) (2010) 3863–3875.

[46] R. Caruana, A. Niculescu-Mizil, Data mining in metric space: an empirical analysis of supervised learning performance criteria, Proceedings of the tenth ACM SIGKDD International conference on Knowledge Discovery and Data Mining, ACM; Association for Computing Machinery, 2004, pp. 69–78.

[47] I. Porteous, D. Newman, A. Ihler, A. Asuncion, P. Smyth, M. Welling, Fast collapsed Gibbs sampling for latent Dirichlet allocation, 4th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2008, pp. 569–577.

[48] S. Moghaddam, M. Ester, Ilda: interdependent lda model for learning latent aspects and their ratings from online product reviews, Proceedings of the 34th international ACM SIGIR conference on Research and development in Information Retrieval, ACM, 2011, pp. 665–674.

[49] W.H. DuBay, The Principles of Readability, Impact Information, 2004. , (City:).

[50] H. Bloom, The Global Brain: The Evolution of Mass Mind from the Big Bang to the 21st Century, John Wiley and Sons, New York, 2000. , (City:).

[51] C. McPhail, The Myth of the Madding Crowd, Aldine de gruyter, 1991.

[52] J. Leskovec, L. Adamic, B. Huberman, The dynamics of viral marketing, ACM Transactions on the Web (TWEB) 1 (1) (2007) 5.

[53] C. Kiss, M. Bichler, Identi<sup>fi</sup>cation of in<sup>fl</sup>uencers—measuring in<sup>fl</sup>uence in customer networks, Decision Support Systems 46 (1) (2008) 233–253.

[54] A. Shoham, A. Ruvio, Opinion leaders and followers: a replication and extension Psychology and Marketing 25 (3) (2008) 280–297

[55] C. Snyder, Positive Psychology: The Scienti<sup>fi</sup>c and Practical Explorations of Human Strengths, Sage, Thousand Oaks, CA, 2007. , (City:).

[56] R. Gomes, P. Welinder, A. Krause, P. Perona, Crowdclustering, Technical Report CNS-TR-2011.001, California Institute of Technology, Pasadena, CA, 2011.

[57] M. Bilenko, M. Richardson, Predictive client-side pro<sup>fi</sup>les for personalized advertising, 17th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, Association for Computing Machinery, 2011, pp. 413–421.

![](/api/attachments/5CK66C9A/fulltext/images/ebcf078c0bba32bdc68b70009de2e9cc94e71823fb024be588a812463e3b53b9.jpg)

![](/api/attachments/5CK66C9A/fulltext/images/2a9d83443b60d1552a0a7e77701dee0acd5edff5e1bac7f73eb46ddbebdd86f7.jpg)

Xiaolin Zheng is an associate professor in College of Computer Science in Zhejiang University, taking charge of Modern Service Innovation Lab as Director. His researches mainly focus on Data Mining for Social Network, electronic commerce, service computing and so on. He is a senior member of CCF (China Computer Federation), committee member in Service Computing of CCF, and committee member in Cloud Computing of CIC (China Institute of Communication), member of IEEE and ACM. He has received several awards as key member in the following prize: Second Class Prize for Outstanding Achievement Award of Colleges and universities Scienti<sup>fi</sup>c Research in 2010, IBM Outstanding Teachers Award in 2009, Excellent Scholar in First Alibaba Young Scholars Program in 2009.

Shuai Zhu is a student at Zhejiang University in China pursuing his M.S. degree in Computer Science. His current research interests include review mining, natural language processing, machine learning and computational advertising. He has received several awards and honors, including innovation awards of Tencent, Inc., school outstanding honor

![](/api/attachments/5CK66C9A/fulltext/images/107f776daa350dec232e44bd841aa792e10f523760da8f7b4ba5994429508068.jpg)

Dr. Zhangxi Lin is an associate professor at the Rawls College of Business Administration, and a co-director of Center for Advanced Analytics and Business Intelligence, at Texas Tech University. He received his <sup>fi</sup>rst master degree in computer science in 1982 from Tsinghua University, and another master degree in economics in 1996 from the University of Texas at Austin. He earned his Ph.D. degree in information systems in 1999 from the University of Texas at Austin. Zhangxi Lin's research interests include data communications business intelligence electronic commerce and knowledge-based system. In last ten years, he has published more than a hundred papers in internationally refereed journals and conferences. Zhangxi Lin is a member of Association of Information Systems, and INFORMS.
