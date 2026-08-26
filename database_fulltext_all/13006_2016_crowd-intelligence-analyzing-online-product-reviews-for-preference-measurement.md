---
otero_id: 13006
otero_key: "ZSE5RAQB"
title: "Crowd intelligence: Analyzing online product reviews for preference measurement"
authors: "Shengsheng Xiao; Chih-Ping Wei; Ming Dong"
year: "2016"
journal: "Information & Management"
doi: "10.1016/j.im.2015.09.010"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Title: Crowd intelligence: Analyzing online product reviews for preference measurement

Author: Shengsheng Xiao Chih-Ping Wei Ming Dong

![](/api/attachments/ZSE5RAQB/fulltext/images/42baf63a1f60fe49c0140883d6ee39ac94674bba5a52398d5f6ce50e563b87e0.jpg)

PII: S0378-7206(15)00108-1

DOI: http://dx.doi.org/doi:10.1016/j.im.2015.09.010

Reference: INFMAN 2847

To appear in: INFMAN

Received date: 21-10-2014

Revised date: 11-8-2015

Accepted date: 29-9-2015

Please cite this article as: S. Xiao, C.-P. Wei, M. Dong, Crowd intelligence: Analyzing online product reviews for preference measurement, Information and Management (2015), http://dx.doi.org/10.1016/j.im.2015.09.010

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Crowd Intelligence: Analyzing Online Product Reviews for Preference Measurement

Shengsheng Xiao<sup>1</sup>, Chih-Ping Wei<sup>2,\*</sup>, and Ming Dong<sup>3</sup>

1: Department of Operations Management

Antai College of Economics & Management

Shanghai Jiao Tong University

Shanghai 200052, China

Email: xiaoshengsheng@sjtu.edu.cn

2: Department of Information Management

National Taiwan University

Taipei, 10617, Taiwan

Email: cpwei@ntu.edu.tw

3: Department of Operations Management

Antai College of Economics & Management

Shanghai Jiao Tong University

Shanghai 200052, China

Email: mdong@sjtu.edu.cn

August 2015

Crowd Intelligence: Analyzing Online Product Reviews for Preference Measurement

## Abstract

The proliferation of opinion sharing platforms, especially product review websites, establishes open, convenient communication channels between customers but also produces a large, publicly accessible information resource for firms that seek to understand consumers’ perceptions and preferences. A key question here is how to measure aggregate consumer preferences from the opinions expressed in online product reviews (crowd intelligence) to facilitate product development or improvement. In response, we propose in this study a novel econometric preference measurement model (referred to as the modified ordered choice model, MOCM) to extract aggregate consumer preferences from online product reviews. Moreover, to categorize customer requirements on the basis of the aggregate consumer preferences estimated by the MOCM model, we extend the Kano model and propose a marginal effect-based Kano model (MEKM). For empirical evaluation purposes, we collect a data set that contains 2,425 online product reviews about mobile phones from a popular product review website, Epinions.com. Our empirical results suggest the superiority of the proposed MOCM model compared with three salient, existing econometric models for preference measurement and also demonstrate the utility of the proposed MEKM model.

Keywords: preference analysis and measurement; aggregate consumer preferences; crowd intelligence; online product reviews; user generated content; Kano model

## 1. Introduction

With the advances and rapid proliferation of Web 2.0 innovations, people increasingly use various online word-of-mouth (WOM) channels to share their consumption experiences with and preferences for a wide range of products. The resulting collection of online product reviews has become an important information source that consumers use to decide whether to purchase a product or which product to select. According to one recent report,<sup>1</sup> 77% of consumers read online product reviews before shopping, and 75% trust online product reviews more than personal recommendations. In addition, 81% of users indicate that they receive helpful advice from online product reviews. Online product reviews thus constitute a novel type of WOM online (commonly referred to as eWOM) (Chevalier & Mayzlin, 2006; Gu, Park, & Konana, 2012; Zhu & Zhang, 2010; Lee & Lee, 2009).

Compared with traditional WOM, online product reviews provide a more publicly accessible information source to understand consumer perceptions and preferences; traditionally, such data were difficult to collect on a large scale in the offline world. Because of this characteristic, substantial literature seeks to connect some measurable attributes of online product reviews (e.g., review valence, volume, product rating, product comparison) with consumers’ purchase behaviors (Lee & Lee, 2009; Phang, Zhang, & Sutanto, 2013), product sales (Chen & Xie, 2008; Forman, Ghose, & Wiesenfeld, 2008; Kuksov & Xie, 2010; Zhang, Guo, & Goes, 2013), firms’ economic outcomes (Archak, Ghose, & Ipeirotis, 2011) and operational strategies (Chen, Wang, & Xie, 2011; Chen & Xie, 2008; Kuksov & Xie, 2010; Netzer, Feldman, Goldenberg, & Fresko, 2012; Abrahams et al., 2013; Xu et al., 2011; He et al., 2015). Some prior studies also attempt to exploit this public information source and turn individual consumer opinions into aggregate consumer preference measures (i.e., a preference measurement model) that capture the effects of consumers’ sentiment toward product features on product ratings (Decker & Trusov, 2010; Ghose, Ipeirotis, & Li, 2012; Korfiatis & Poulos, 2013; Lee & Bradlow, 2011; Li et al., 2014).

Measuring such aggregate consumer preferences is critical to firms, because it can facilitate their planning and decision making pertaining to product improvement, new product development, pricing, market segmentation, positioning, and advertising (Ghose, Ipeirotis, & Sundararajan, 2007; Lee & Bradlow, 2007). Conjoint analysis has been the main quantitative preference measurement method since it was first introduced by Green & Rao (1971). As a result, preference measurement is often equated with conjoint analysis (Netzer et al., 2008). To conduct conjoint analysis, we need to collect consumers’ preferences through surveys or experiments, which require rigorous design and involve a proper procedure to ensure the quality of responses from respondents. There is no doubt that such data collection approach is time consuming and costly. In contrast, the availability of large-scale online product reviews offers the promise of an alternative means to measure aggregate consumer preferences. Compared with the traditional data collection approach for conjoint analysis, using online product reviews to support preference measurement has several advantages. First, online product reviews are publicly available and can be collected easily. Second, online product reviews are voluntarily produced by actual consumers (Decker & Trusov, 2010; Netzer et al., 2008) and do not depend on surveys or respondents. Prior studies have shown that consumer opinions expressed in online product reviews offer a good proxy for the overall WOM of the products being discussed and then become a new source of preference data (Archak et al., 2011; Decker & Trusov, 2010; Zhu & Zhang, 2010; Li et al., 2014). Thus, online product reviews represent a more representative preference dataset than those collected by surveys or experiments. Third, the size of online product reviews is generally large and they often cover diverse product features. Consequently, these online product reviews can be employed to construct more comprehensive preference measurement models than preference datasets collected through surveys or experiments. Considering these advantages, we focus on the use of online product reviews for preference measurement and investigate two pertinent research questions: (1) How can we effectively measure aggregate consumer preferences from online product reviews? and (2) How can we categorize customer requirements, on the basis of the estimated aggregate consumer preferences?

To address these research questions, we first establish a framework to extract, from online product reviews, the product features discussed and the reviewers’ sentiment orientations (like or dislike) toward them. To better explain reviewers’ rating behavior, we also collect additional information about the reviewers, including the total number of reviews written by each of them and the trust relations among them, for calibrating our preference measurement model. Next, we propose an econometric model, referred to as the modified ordered choice model (MOCM), to measure aggregate consumer preferences from online product reviews. This new model takes into consideration the heteroscedasticity of reviewers’ rating variance and allows reviewers to assign rating scores according to their own thresholds. Furthermore, to categorize customer requirements and support product design on the basis of the aggregate consumer preferences estimated by our proposed MOCM model, we extend the Kano model (Kano, Seraku, Takahashi, & Tsuji,1984; Janne & Timo, 1998; Chen & Chuang, 2008; Xu,Jiao, Yang, Helander, Khalid, & Opperud, 2009) and propose a marginal effect-based Kano model (MEKM). Finally, we empirically evaluate the effectiveness of our econometric preference measurement model (i.e., MOCM) and demonstrate the utility of our proposed MEKM model. Using a dataset collected from Epinions.com, we show that our proposed MOCM model outperforms existing models and the MEKM model provides a viable method for further categorizing and prioritizing customer requirements.

The remainder of the paper is organized as follows. Section 2 reviews the literature relevant to this study. We describe our preprocessing procedure for extracting product features and reviewers’ sentiment orientations from online product reviews and then depict our data coding scheme in Section 3. In Section 4, we detail our proposed econometric model (i.e., MOCM) for estimating aggregate consumer preferences from online product reviews. Section 5 depicts our proposed MEKM model for categorizing customer requirements, based on the aggregate consumer preferences estimated by MOCM. In Section 6, we report our empirical study, in which we use online product reviews from Epinions.com to evaluate the effectiveness of our proposed MOCM model and illustrate the utility of the proposed MEKM model. We conclude in Section 7 by highlighting our theoretical and practical contributions as well as some further research directions.

## 2. Literature Review

In this section, we review existing preference measurement methods and analyze their limitations to justify our research motivation. In addition, we summarize the Kano model, which provides the basis for our MEKM model.

## 2.1 Existing Preference Measurement Methods

In the past several decades, many methods have been developed to measure aggregate consumer preferences quantitatively. Depending on the data they use, existing preference measurement methods can be classified into three major approaches: survey-, behavior-, and online review–based.

Conjoint analysis was first introduced by Green & Rao (1971). Since its introduction, preference measurement is often linked to conjoint analysis (Netzer et al., 2008). One significant characteristic of conjoint analysis is that it depends strongly on survey data, collected through surveys or experiments. As a result, the survey-based approach mainly refers to those preference measurement methods that use conjoint analysis or its variants. Using consumers’ preference data collected from surveys or experiments, the survey-based approach typically relies on econometric and statistical methods to analyze these data and determine how people value the different features that constitute an individual product or service (Giesen et al., 2007; Halme & Kallio, 2011; Jiao et al., 2007; Sattler & Hensel-Börner, 2003; Toubia, De Jong, Stieger, & Füller, 2012).

The survey-based approach is formal and rigorous, but its data collection process is time consuming and costly. To overcome these challenges, some studies exploit the use of consumers’ behavioral data, collected from shopping environments, to infer aggregate consumer preferences. Different from the survey-based approach, the behavior-based approach uses the data about consumers’ behavior directly (e.g., items placed in shopping carts, items purchased, shopping paths), rather than preference data collected from surveys and experiments. For example, with point-of-sales data, Fader and Hardie (1996) employ a discrete choice model to measure consumer preferences for selected product features. In contrast, Hui, Fader, & Bradlow (2009) estimate aggregate consumer preferences from consumers’ purchases (i.e., transaction data) and their shopping paths (collected by RFID technology). Because the data about consumers’ behavior may have been collected already by retailers (e.g., consumers’ purchases) or can be acquired easily (e.g., with the support of some information technologies), the data collection cost of this approach tends to be far less than that of the survey-based approach.

Finally, the increasing availability and accessibility of online product reviews contributed by consumers have prompted some studies to investigate ways to measure aggregate consumer preferences from online product reviews. This online review-based approach leverages the large collection of existing, publicly available online product reviews and thus represents an appealing alternative. Archak, Ghose, and Ipeirotis (2007) propose a hedonic regression approach to analyze the strength and polarity of consumer review opinions. However, they did not consider opinion heterogeneity expressed in each review. In a follow-up study, they note that consumers’ preferences can be reflected by online product reviews but do not propose a detailed method to extract them (Ghose, Ipeirotis, & Sundararajan, 2007). Lee & Bradlow (2007) emphasize the importance of online product reviews for conjoint analyses in marketing and propose a text mining technique to extract the product features discussed in online product reviews, as well as consumers’ sentiment orientations toward these features. Li et al. (2014) develop a social intelligence mechanism to extract and consolidate the reviews expressed via social media and to derive insights to help firms make decisions on product portfolio design. Decker and Trusov (2010) propose three econometric models (i.e., Poisson regression, negative binominal regression, and latent class Poisson regression models) to measure aggregate consumer preferences from online product reviews about mobile phones.

Several online review-based preference measurement models have been proposed (Lee & Bradlow, 2007, 2011; Decker and Trusov, 2010). However, they incur several limitations. First, it may be not suitable to use counting models, such as Poisson regression, negative binominal regression, and latent class Poisson regression models, to assess reviewers’ rating behavior (i.e., measure aggregate consumer preferences).That is mainly because the ratings in online product reviews use an ordinal rather than interval scale, and counting models are not

#

designed to model ordinal scale data. Second, existing online review-based preference measurement methods consider review content only (i.e., textual comments and rating scores), without acknowledging that different reviewers have their own biases when giving rating scores, and their rating behaviors may be influenced by their personal characteristics (Li et al., 2011; Wang, Min, Huang, Li, & Wu, 2013). Therefore, to better explain reviewers’ rating behavior and improve the effectiveness of preference measurement, preference measurement models should take reviewer characteristics into consideration (Decker and Trusov,2010).

Following the stream of preference measurement literature, we propose in this study a modified ordered choice model (MOCM) to extract aggregate consumer preferences from online product reviews. Moreover, we incorporate some covariates from reviewer profiles into the proposed model, to improve the effectiveness of preference measurement.

## 2.2 Kano Model

Our research also relates to the Kano model, a two-dimensional model first developed by Kano, Seraku, Takahashi, and Tsuji (1984). The Kano model classifies product features (attributes) into different categories (see Figure 1), according to the degree of fulfillment of the product feature and its effect on customer satisfaction (Kano et al., 1984; Janne & Timo, 1998; Chen & Chuang, 2008; Xu et al., 2009). Specifically,

1. Must-be (or basic) features: These product features are taken for granted when fulfilled, but if they are not fulfilled, customers become dissatisfied.

2. Performance (or one-dimensional) features: A product feature is considered as a performance feature if its fulfillment is positively associated with customer satisfaction.

3. Excitement (or attractive) features: Excitement features are the opposites of must-be features. That is, excitement features offer satisfaction when fulfilled but do not result in dissatisfaction if not fulfilled.

4. Indifferent features: When the degree of fulfillment of a product feature is either not associated or only marginally associated with customer satisfaction or customer dissatisfaction, this feature is referred to as an indifferent feature.

5. Reverse features: Reverse features imply that when the degree of fulfillment increases, customers become more dissatisfied.

![](/api/attachments/ZSE5RAQB/fulltext/images/2481f2356b579435a8715281c3a90873e5160b8c95ea40b617eecf83d951d99a.jpg)  
Figure 1: Classification of Features in the Kano Model

The Kano model is typically constructed on the basis of customer surveys, consisting of a set of question pairs. Each question pair pertains to a product feature and includes a functional form question, which captures customer responses if the product has this feature, and a dysfunctional form question to capture customer responses if the product does not have this feature. Customers’ responses to the question pair reveal their perceptions about that corresponding feature. The questionnaire is deployed to a number of customers, and the answers to each question pair is aligned with the Kano evaluation table (Berger et al., 1993). The classification of product features is then made on the basis of a statistical analysis of the survey results of all respondents.

As mentioned, the Kano model involves two dimensions: the degree of fulfillment of product features and the effect on customer satisfaction. However, aggregate consumer preferences measured by an online review-based preference measurement method cannot map directly to these two dimensions. Hence, in this study, we extend the Kano model by employing marginal effect information disclosed by the proposed MOCM model. Specifically, we follow the feature classification framework of the Kano model but use the marginal effect information derived from the MOCM model to quantify consumers’ satisfaction with different product features. To the best of our knowledge, this study is the first to combine the concept of the Kano model with a preference measurement model and thereby categorize product features.

## 3. Data Preprocessing Framework

In this section, we first depict the preprocessing procedure that we use to extract product features and reviewers’ sentiment orientations from online product reviews. We then discuss additional data (i.e., reviewer profiles) that our proposed preference measurement model requires. Finally, we describe our data coding scheme in detail.

#

## 3.1 Product Feature Extraction from Online Product Reviews

To understand why reviewers assign different rating scores to products, we should first extract product features discussed in these reviews and the reviewers’ sentiment orientations (positive or negative) toward these product features. Prior studies have developed various opinion mining methods for this purpose using natural language processing or text mining techniques (Cambria, Schuller, Xia, & Havasi, 2013; Dai et al., 2015; Hu & Liu, 2004; Popescu & Etzioni, 2007; Wei, Chen, Yang, & Yang, 2010; Xu, Cheng, Tan, Liu, & Shen, 2013; Yan et al., 2015). Because we aim to measure aggregate consumer preferences from online product reviews, developing a new product feature extraction method is not the main focus of our study; instead, we employ and extend existing methods to support our product feature extraction. Moreover, this study takes semi-structured reviews,<sup>2</sup> rather than free-text reviews, as inputs due to the following reasons. First, consumers explicitly express their sentiment orientations toward product features in semi-structured reviews (i.e., pro and con phrases are organized separately and directly convey reviewers’ sentiment orientations toward product features). As a result, given an online product review, we do not need to analyze the full text of the review to identify the sentiment orientations of the reviewer toward different product features. This will greatly improve the effectiveness and efficiency of the data preprocessing stage. Second, many studies reveal that the pro/con phrases in semi-structured reviews generally summarize the opinions expressed in the full text of the corresponding reviews (Branavan, Chen, Eisenstein, & Barzilay, 2009; Kim & Hovy, 2006). Therefore, using these semi-structured reviews should not lead to the loss of too much useful information, compared with using free-text reviews. Third, a semi-structured review is a popular format used by many online product review platforms (e.g., Epinions.com, 360buy.com, Taobao.com). Thus, the product feature extraction procedure developed and employed in this study can be applied to online product reviews collected from various platforms.

With a collection of semi-structured product reviews, our product feature extraction procedure consists of five steps (left column, Figure 2):

1) Partitioning, stemming and removing stop words. We start by splitting the pros and cons in each review into individual phrases, then reduce the inflected (or sometimes derived) words to their stems, bases, or root forms. Finally, we remove stop words and other meaningless words (e.g., “the,” “an,” “nothing else”) from the partitioned and stemmed pro/con phrases.

2) Extracting explicit features. Explicit product features can be found easily in the pro/con fields, but they often are accompanied by positive or negative adjectives that reiterate the reviewers’ sentiment orientations. Because we already know the reviewer’s sentiment orientation about a product feature, depending on whether it appears in the pro or con field, such positive or negative adjectives are not needed in subsequent analyses. Thus, we remove these adjectives to obtain explicit product features in this step. For example, reviewers may put “good touch screen” and “nice camera” in the pro field. In this case, “good” and “nice” are positive adjectives that recap the reviewers’ positive attitude toward these two product features. Thus, we remove “good” and “nice” and reduce “good touch screen” and “nice camera” to “touch screen” and “camera,” respectively.

3) Transforming implicit features. Reviewers might implicitly include product features in the pro/con fields. For example, “expensive” is an implicit product feature, corresponding to the explicit product feature “price.” In this step, we identify and transform all implicit features into explicit features. To ensure its accuracy, we perform this task manually.

4) Merging and grouping product features. People often use different terms to describe the same concept (or object) (Wei et al., 2007). To address this word mismatch problem, we merge terms in different reviews that refer to the same product feature and replace them with a standardized term for this feature. We employ a semi-automated method for the described merging and grouping task. Specifically, we first merge product features with a text mining package (i.e., IBM SPSS Text Analytics). Built on thousands of commonly used words and phrases, this package automatically calculates the similarity between product features and merges them according their similarities. Subsequently, we manually check the grouping results and make adjustments if needed.

5) Pruning infrequent product features. This step removes product features that are less frequent in the target collection of product reviews. For this study, we set a threshold of 10%; that is, we remove product features that occur in less than 10% of product reviews.

After the final step, we retain a list of extracted product features for each semi-structured product review in the target collection. An illustration of our product feature extraction procedure is in the right column of Figure 2. It is worth noting that, although we take semi-structured reviews as inputs, our study can easily be extended to handle free-text reviews. In this case, we can employ an existing opinion mining method for extracting product features from free-text reviews and identifying reviewers’ sentiment orientations toward these product features. Subsequently, we perform implicit feature transformation (step 3 in Figure 2), product feature grouping (step 4), and infrequent feature pruning (step 5) and thus conclude the product feature extraction procedure for free-text reviews.

![](/api/attachments/ZSE5RAQB/fulltext/images/2d8557107a1a12153ffda587b09c0ec9cae3a9e01c30a003351c0b18d86c55ea.jpg)  
Figure 2: Procedure of Product Feature Extraction and an Example<sup>3</sup>

## 3.2 Collection of Reviewer Profiles for Preference Measurement Purposes

In addition to extracting product features and identifying reviewers’ sentiment orientations from online product reviews, we also need to collect reviewer profiles, which help us to construct more covariates to explain reviewers’ rating behavior and improve the effectiveness of preference measurement. In a typical online product review platform, a reviewer profile contains the reviewer’s basic information (e.g., geographic and demographic information, nickname) and records his/her historical activities on this platform (e.g., total number of reviews written, trust relations with other reviewers). We are mainly interested in two types of information. First, we consider the total number of reviews written by each reviewer; compared with reviewers who have written fewer reviews, those who have published more usually are more experienced with expressing their preferences. Thus, the rating behavior of reviewers who have written more reviews should be different from that of reviewers who have written fewer reviews. Second, trust relations between reviewers likely disclose each reviewer’s overall position or reputation in this community. For our empirical study, we construct reviewers’ trust network and use the normalized PageRank value (Langville & Meyer, 2004; Monica, Marco, & Franco, 2005) of each reviewer to signify his or her overall position or reputation.

## 3.3 Data Coding Scheme

After our data preprocessing, we use the following scheme for data coding. Specifically, we use subscripts $k = 1 , 2 , 3 , . . . , K$ to index individual reviews; $l = 1 , 2 , 3 , . . . , L$ to denote product features mentioned in the reviews; i =1, 2, 3, …, I to represent reviewers; and s{pro, con} to represent the sentiment orientation of each extracted product feature in a

#

review (whether a feature is a pro or con in a review). We let $x _ { k , l , p + p , s } = 1$ , if product feature l is taken as a pro in review k (product feature l appears in the pro field of review k), and $x _ { k , l , p , p , p } = 0$ otherwise. Similarly, we let $x _ { k , l , \tt c o a } = 1$ if product feature l is taken as a

con in review k (product feature l appears in the con field of review k), and $x _ { k , l , r \in \mathsf { o r } } = 0$

otherwise. Product brand mentioned in review k is represented by $B _ { k } \left( B _ { \mathrm { k } } \right.$ is actually a dummy variable that serves as the brand-specific intercept and is incorporated to control brand effect), the total number of reviews written by reviewer i is represented by $n _ { i , }$ and the overall reputation of reviewer i (measured by the normalized PageRank value) is denoted by $t r _ { i }$

## 4. MOCM: A New Preference Measurement Model

Considering the ordinal scale of the rating scores in online product reviews, we do not intend to use the counting models employed by Decker and Trusov (2010) to explain reviewers’ rating behavior (instead, they serve as benchmark models for our empirical study). In this section, we first explain how the basic ordered choice model (BOCM) measures aggregate consumer preferences. Subsequently, we relax two assumptions of the BOCM model by taking the heterogeneity of each reviewer’s rating behavior into consideration to establish the modified ordered choice model (MOCM).

## 4.1 Basic Ordered Choice Model (BOCM)

The BOCM model is proposed by McKelvey and Zavoina (1975) for the analysis of categorical, non-quantitative choices, outcomes, and responses. Because of its capability to deal with ordinal data, we use this model as a basis to develop our preference measurement model. Specifically, the BOCM model assumes that the rating score given in online product review k is based on the following latent regression:

$$
y _ {k} ^ {*} = \beta^ {\prime} \cdot \left(\mathbf {x} _ {k, \text { pro }}, \mathbf {x} _ {k, \text { con }}, B _ {k}\right) + \varepsilon_ {k}\tag{3}
$$

Where $\Xi _ { k }$ is a random variable following a normal distribution. The continued latent variable, $F _ { k } ^ { \prime } ,$ is observed in discrete form through a censoring mechanism:

$$
\begin{array}{r l} y _ {k} & = 0 \text {   if   } - \infty <   y _ {k} ^ {*} \leq \mu_ {0} \\ & = 1 \text {   if   } \mu_ {0} <   y _ {k} ^ {*} \leq \mu_ {1} \\ & = 2 \text {   if   } \mu_ {1} <   y _ {k} ^ {*} \leq \mu_ {2} \\ & = \dots \end{array}\tag{4}
$$

$$
= J \text {   if   } \mu_ {J - 1} <   y _ {k} ^ {*} \leq + \infty
$$

$x _ { k , \cdots , p + r 0 }$ and $\pmb { \tilde { x } _ { k : , \pmb { \sigma } \mathbf { \tilde { u } } } }$ are vectors containing dummy variables. If we assume review k is written by reviewer i, then $x _ { k , \mu } = \mu _ { 0 }$ and $\sqrt { \pi } _ { k } , \ r \cdot \ o \mathbf { n }$ indicate the sentiment orientations of reviewer i toward all the extracted product features. More specifically, $x _ { \mathrm { k } , \mathrm { k } , \mathrm { p } \mathrm { p } \mathrm { r } \bar { \mathrm { p } } } = 1 ( x _ { \mathrm { k } , \mathrm { k } , \mathrm { p } \mathrm { r } \bar { \mathrm { p } } } \in x _ { \mathrm { k } , \mathrm { p } \mathrm { p } \mathrm { r } \bar { \mathrm { p } } } )$ means that product feature l in review k is regarded as a “pro” by reviewer i and $x _ { k , l , p + r , p } = 0$ denotes that reviewer i does not consider product feature l in review k a “pro.” The meaning of $x _ { k , l , \sigma , \sigma , \sigma }$ $x _ { k , l , \mu _ { r } \varrho }$ . In addition, $B _ { k }$ represents the brand name of the focal product discussed in review k. The outcome $y _ { k }$ refers to the observable rating score given in review k. The unknown marginal utilities , and unknown thresholds in Equation 4 must be estimated, using observable online product review samples (indexed by $k = 1 , . . . , K )$ . In the following section, we use $\yen 1$ to denote $x _ { k , \mu \mu }$ and $\pmb { \pi } _ { k _ { 1 } , \pmb { \pi } \oplus \mathbf { \equiv } }$ . The estimates in this model can be obtained with a maximum likelihood method. In the context of the BOCM model, the probability entering the log likelihood function is by Equation 5 (where is the cumulative distribution function (CDF) of the normal distribution):

$$
\operatorname{Prob} \left[ y _ {k} = j \mid \mathbf {x} _ {k, \cdot}, B _ {k} \right] = \left\{ \begin{array}{c} \Phi \left[ \mu_ {0} - \beta^ {\prime} \cdot \left(\mathbf {x} _ {k, \cdot}, B _ {k}\right) \right], \text {when} j = 0 \\ \Phi \left[ \mu_ {j} - \beta^ {\prime} \cdot \left(\mathbf {x} _ {k, \cdot}, B _ {k}\right) \right] - \Phi \left[ \mu_ {j - 1} - \beta^ {\prime} \cdot \left(\mathbf {x} _ {k, \cdot}, B _ {k}\right) \right], \text {when} 0 <   j <   J \\ 1 - \Phi \left[ \mu_ {j - 1} - \beta^ {\prime} \cdot \left(\mathbf {x} _ {k, \cdot}, B _ {k}\right) \right], \text {when} j = J \end{array} \right.\tag{5}
$$

## 4.2 Development of the Modified Ordered Choice Model (MOCM)

Although it is convenient to obtain estimates from the BOCM model, an issue for the estimation is the unobserved heterogeneity of each reviewer. Reviewers differ from one another, such that they express different opinions about the same products and assign different rating scores. If we reexamine the BOCM model, we will find two sources of individual heterogeneity: the random component $\sumint \limits _ { j }$ and the thresholds $\mu _ { j }$ , used by each reviewer. In the following subsections, we will discuss how to modify the BOCM model by taking these two heterogeneity patterns into consideration.

## 4.2.1 Heteroscedasticityof Rating Behavior

In the BOCM model, $\mathrm { V a r } [ \varepsilon _ { \mathrm { f } } | \boldsymbol { x } _ { \mathrm { f } } , \boldsymbol { B } _ { \mathrm { f } } ] = 1$ , so $\mathrm { V a r } [ { \bf { y } } _ { k } | { \bf x } _ { k _ { \mathrm { B } } } , { \bf B } _ { \mathrm { { z } } } ] = 1$ . It means that the rating variance is identical across different reviewers. Obviously, this is not a reasonable assumption. Intuitively, a reviewer who has written many reviews should be better expressing his or her opinions and assigning rating scores that are closer to products’ true ratings than a reviewer who has published only a few reviews. The rating variance from a more experienced reviewer then should differ from that of a less experienced reviewer. We first relax this homogeneous variance assumption by letting $\operatorname { V a r } [ \varepsilon _ { \mathrm { f } } | \mathbf { x } _ { \mathrm { f } } , \mathbf { \vec { B } } _ { \mathrm { \vec { \kappa } } } ]$ satisfy Equation 6 (assuming review k is written by reviewer i).

$$
\operatorname{Var} [ \varepsilon_ {k} | \pmb {x} _ {k, i}, B _ {k}, \pmb {w} _ {i} ] = (\sigma_ {k} ^ {i}) ^ {2}, \mathrm{where} (\sigma_ {k} ^ {i}) ^ {2} = \exp (\pmb {\gamma} ^ {\prime} \pmb {w} _ {i} + \nu)\tag{6}
$$

where $\mathbf { w _ { i } }$ is a vector of variables to explain reviewer $i \gamma _ { \mathrm { { S } } }$ rating variance (in our empirical study, we use the total number of reviews written by reviewer i to represent $\mathbf { u } \mathbf { \pmb { \nu } } _ { \mathbf { \pmb { \nu } } } )$ , and is the associated parameter set. Furthermore, $\mathbb { V } \left( \mathbb { V } ^ { \sim \mathbb { N } \left[ \mathbb { Q } , 1 \right] } \right)$ is a standard latent random variable for interpreting the unobservable part of the error term for rating variance. We use the exponential function, as widely used in prior literature (e.g., Eluru, Bhat, and Hensher, 2008; Greene & Hensher, 2010), to ensure the positivity of the parameterized $\sigma _ { k } ^ { i }$ . After considering heteroscedasticity, we can replace the conditional probability entering the log likelihood function by Equation 7:

$$
\operatorname{Prob} \left[ y _ {i} = j \mid x _ {k}, B _ {k}, w _ {i}, v \right] = \left\{ \begin{array}{c} \Phi \left[ \frac {\mu_ {1} - \beta^ {t} \cdot (x _ {k , i} , B _ {k})}{\sqrt {\exp (y ^ {t} w _ {1} + v)}} \right], \text {if} j = 0 \\ \Phi \left[ \frac {\mu_ {j} - \beta^ {t} (x _ {k , i} , B _ {k})}{\sqrt {\exp (y ^ {t} w _ {1} + v)}} \right] - \Phi \left[ \frac {\mu_ {j - 1} - \beta^ {t} (x _ {k , i} , B _ {k})}{\sqrt {\exp (y ^ {t} w _ {1} + v)}} \right], \text {if} 0 <   j <   J \\ 1 - \Phi \left[ \frac {\mu_ {j - 1} - \beta^ {t} (x _ {k , i} , B _ {k})}{\sqrt {\exp (y ^ {t} w _ {1} + v)}} \right], \text {if} j = J \end{array} \right.\tag{7}
$$

## 4.2.2 Different Thresholds for Different Reviewers

Another assumption in the BOCM model pertains to thresholds $\mu _ { j } ( j = 0 , \ 1 , \ 2 , \ . . . , \ J { - } 1 )$

assumed to be identical across different reviewers. In reality, different reviewers assign the rating scores, according to their own standards. As a result, these thresholds should take different values for different reviewers. We therefore model the reviewer-specific thresholds (Eluru et al. [2008] and Greene & Hensher [2010] use similar methods to solve different problems), as follows:

$$
\mu_ {i j} = \mu_ {i j - 1} + e ^ {\theta_ {j} + \delta_ {x _ {j}} + \eta} (j = 0, 1, 2, \dots , J - 1)\tag{8}
$$

#

As Equation 8 reveals, the thresholds used by different reviewers are no longer the same but instead depend on $\theta _ { j }$ (specific to the j-star rating score, but independent to reviewers), a parameter vector $z _ { i } ,$ and a latent variable . Moreover, $\theta _ { j }$ illustrates the fixed effect of a reviewer giving a j-star rating score $( j = 0 , \ 1 , \ 2 , \ . . . , \ J )$ . The variable vector $z _ { i }$ contains variables to capture reviewer-specific choices when they assign rating scores (in our empirical study, we use the overall reputation score of reviewer i, which is measured by the normalized PageRank value according to the reviewers’ trust network, to represent $z _ { i } )$ ; follows a normal distribution and serves to capture unobservable bias. It is worth noting that and in Equations 7 and 8 are independent. By using Equation 8, we ensure that $\mu _ { i , j }$ is always larger than $H _ { i , j - 1 }$

## 4.2.3 Our Proposed Modified Ordered Choice Model (MOCM)

By combining the aforementioned modifications, we establish the modified ordered choice model (MOCM) to explain reviewers’ rating behaviors. If we assume review k is posted by reviewer i, this model can be written as:

$$
y _ {k} ^ {*} = \beta^ {\prime} \cdot (x _ {k, 1}, B _ {k}) + \varepsilon_ {k}, \text { where   Var } [ \varepsilon_ {k} | x _ {k, 1}, B _ {k}, w _ {i} ] = (\sigma_ {k} ^ {i}) ^ {2}\tag{9}
$$

The continuous latent variable $y _ { k } ^ { * }$ is the observed rating score in discrete form, through a censoring mechanism:

$$
\begin{array}{r l} y _ {k} & = 0 \text {   if   } - \infty <   y _ {k} ^ {*} \leq \mu_ {i, 0} \\ & = 1 \text {   if   } \mu_ {i, 0} <   y _ {k} ^ {*} \leq \mu_ {i, 1} \\ & = 2 \text {   if   } \mu_ {i, 1} <   y _ {k} ^ {*} \leq \mu_ {i, 2} \\ & = \dots \\ & = J \text {   if   } \mu_ {i, j - 1} <   y _ {k} ^ {*} \leq + \infty \end{array}\tag{10}
$$

In Equations 9 and 10, $\begin{array} { r } { a _ { \tilde { \kappa } } ^ { i } = \exp ( \gamma ^ { i } w _ { i } + v ) \quad \mathrm { a n d } \quad \mu _ { i , j } = \ \mu _ { i , j - 1 } + e x p ( \theta _ { j } + \delta ^ { i } z _ { i } + \eta ) } \end{array}$

Estimates in the MOCM model can be obtained by the maximum simulated likelihood method. Now, the modified conditional probability entering the log likelihood function is replaced by:

$$
\operatorname{Prob} \left[ y _ {k} = j | \mathbf {x} _ {k, \cdot}, B _ {k}, w _ {i}, z _ {i}, v, \eta \right] = \left\{ \begin{array}{c} \Phi \left[ \frac {\mu_ {i , 0} - \beta^ {\prime} \cdot (\mathbf {x} _ {k , \cdot} , B _ {k})}{\sqrt {\exp (y ^ {\prime} w _ {1} + v)}} \right], \text {if} j = 0 \\ \Phi [ \frac {\mu_ {i , j} - \beta^ {\prime} \cdot (\mathbf {x} _ {k , \cdot} , B _ {k})}{\sqrt {\exp (y ^ {\prime} w _ {1} + v)}} ] - \Phi [ \frac {\mu_ {i , j - 1} - \beta^ {\prime} \cdot (\mathbf {x} _ {k , \cdot} , B _ {k})}{\sqrt {\exp (y ^ {\prime} w _ {1} + v)}} ], \text {if} 0 <   j <   J \\ 1 - \Phi \left[ \frac {\mu_ {i , j - 1} - \beta^ {\prime} \cdot (\mathbf {x} _ {k , \cdot} , B _ {k})}{\sqrt {\exp (y ^ {\prime} w _ {1} + v)}} \right], \text {if} j = J \end{array} \right.\tag{11}
$$

Because the term used in the log likelihood function is conditional on the unobservable variables and , the unconditional probability of Equation 11 can be written further as:

$$
\operatorname{Prob} \left[ y _ {k} = j | \boldsymbol {x} _ {k, \cdot}, B _ {k}, \boldsymbol {w} _ {j} Z _ {i} \right] = \left\{ \begin{array}{c} \int_ {v, \eta} \{\Phi [ \frac {\mu_ {0} - \beta^ {\prime} (\boldsymbol {x} _ {k , \cdot} , E _ {k})}{\sqrt {\exp (y ^ {\prime} w _ {1} + v)}} ] \} f (v) f (\eta) d v d \eta , i f j = 0 \\ \int_ {v, \eta} \{\Phi [ \frac {\mu_ {1} - \beta^ {\prime} (\boldsymbol {x} _ {k , \cdot} , E _ {k})}{\sqrt {\exp (y ^ {\prime} w _ {1} + v)}} ] - \Phi [ \frac {\mu_ {1 - 1} - \beta^ {\prime} (\boldsymbol {x} _ {k , \cdot} , E _ {k})}{\sqrt {\exp (y ^ {\prime} w _ {1} + v)}} ] \} f (v) f (\eta) d v d \eta , i f 0 <   j <   J \\ 1 - \int_ {v, \eta} \{\Phi [ \frac {\mu_ {1 - 1} - \beta^ {\prime} (\boldsymbol {x} _ {k , \cdot} , E _ {k})}{\sqrt {\exp (y ^ {\prime} w _ {1} + v)}} ] \} f (v) f (\eta) d v d \eta , i f j = J \end{array} \right.\tag{12}
$$

It is difficult to calculate this probability directly, because of the complexity of the integral operations in Equation 12. Therefore, we use a simulation method to compute Equation 12 and write the simulated log likelihood function as follows (where $v _ { i , m }$ and $\eta _ { i , m }$ are randomly drawn from a standard normal distribution in the m-th simulation, M is the total number of simulation runs, $0 < j < J ,$ and n is the total number of online product reviews): J

$$
\text { loglikely } (\boldsymbol {\beta}, \boldsymbol {\gamma}, \theta , \delta) = \sum_ {i = 1} ^ {n} \log \frac {1}{M} \sum_ {m = 1} ^ {M} \left\langle \Phi [ \frac {\mu_ {i , j} - \boldsymbol {\beta} ^ {\prime} \cdot (\mathbf {x} _ {k , y} , B _ {k})}{\sqrt {\exp (\mathbf {y} ^ {\prime} w _ {i} + v _ {i , m})}} ] - \Phi [ \frac {\mu_ {i , j - 1} - \boldsymbol {\beta} ^ {\prime} \cdot (\mathbf {x} _ {k , y} , B _ {k})}{\sqrt {\exp (\mathbf {y} ^ {\prime} w _ {i} + v _ {i , m})}} ] \right\rangle\tag{13}
$$

## 5. Development of Marginal Effect-Based Kano Model (MEKM)

After the parameter estimation for the MOCM model, we need to interpret the resultant MOCM model to derive useful product design or improvement guidelines. In this section, we first describe the notion of the marginal effects of product features in the MOCM model. Subsequently, we propose a marginal effect-based Kano model (MEKM) to categorize customer requirements on the basis of the consumer preferences estimated by the MOCM model.

## 5.1 Marginal Effects in the MOCM Model

Model interpretation is not straightforward for ordered choice models (Greene, Harris, Hollingsworth, & Weterings, 2014; Greene & Hensher, 2010). Because there is no natural conditional mean function in the MOCM model, the direct interpretation of the coefficients in

$\beta$ is ambiguous. To assign behavioral meaning to these estimated coefficients, we use the change of $[ \mathbf  \{ \mathcal { F } _ { k } = \mathbf { \vec { j } } \mathbf  | \mathbf { E } _ { k } , \mathbf { \vec { j } } _ { k } \mathbf  | \mathbf { \vec { r } _ { k } = \vec { k } } \mathbf  | \mathbf { \vec { r } _ { k } = \vec { k } } \mathbf  | \mathbf { \vec { r } _ { k } = \vec { k } } \mathbf  | \mathbf { \vec { r } _ { k } = \vec { k } } \mathbf  | \mathbf { \vec { r } _ { k } = \vec { k } } \mathbf  | \mathbf { \vec { r } _ { k } = \vec { k } } \mathbf  | \mathbf { \vec { r } _ { k } = \vec { k } } \mathbf  | \mathbf { \vec { r } _ { k } = \vec { k } } \mathbf  | \mathbf { \vec { r } _ { k } = \vec { k } } \mathbf  | \mathbf { \vec { r } _ { k } = \vec { k } } \mathbf  | \vec { r } _ { k } \mathbf { | \vec { r } _ { k } = \vec { k } } \mathbf  | \vec { r } _ { k } \mathbf { | \vec { r } _ { k } = \vec { k } } \mathbf  | \vec { r } _ { k } \mathbf { | \vec { r } _ { k } = \vec { k } } \mathbf  | \vec { r } _ { k } \mathbf { | \vec { r } _ { k } = \vec { k } } \mathbf  | \vec { r } _ { k } \mathbf { | \vec { r } _ { k } = \vec { k } } \mathbf  | \vec { r } _ { k } \mathbf { | \vec { r } _ { k } = \vec { k } } \mathbf  | \vec { r } _ { k } \mathbf { | \vec { r } _ { k } = \vec { k } } \mathbf  | \vec { r } _ { k } \mathbf { | \vec { r } _ { k } = \vec { k } } \mathbf  | \vec { r } _ { k } \mathbf { | \vec { r } _ { k } = \vec { k } } \mathbf  | \vec { r } _ { k } \mathbf  | \vec { r } _ { k } \mathbf { | \vec { r } _ { k } = \vec { k } } \mathbf  | \vec { r } _ { k } \mathbf  | \vec { r } _ { k } \mathbf { | \vec } _ { k } \mathbf  | \vec { r } _ { k } \mathbf  |$ , which is caused by the change of the explanatory variable $x _ { k , p } , ( x _ { k , p } , \in X _ { k , p } )$ , to compute the marginal effect:

$$
\frac {\partial \operatorname{Prob} \left[ y _ {k} = j \mid x _ {k , \cdot} , B _ {k} , w _ {k} , z _ {i} \right]}{\partial x _ {k , \cdot}} = \left[ f (\frac {\mu_ {i , j} - \beta^ {\prime} \cdot (x _ {k , \cdot} , B _ {k})}{\sqrt {\exp (y ^ {\prime} w _ {1} + v)}}) - f (\frac {\mu_ {i , j - 1} - \beta^ {\prime} \cdot (x _ {k , \cdot} , B _ {k})}{\sqrt {\exp (y ^ {\prime} w _ {1} + v)}}) \right] \beta\tag{14}
$$

If $x _ { k , i }$ is a dummy variable, its marginal effect can be computed by

$$
\operatorname{Prob} \left[ y _ {k} = j | \mathbf {x} _ {- k, \cdot}, B _ {k}, \mathbf {w} _ {j} z _ {i}; x _ {k, \cdot} = 1 \right] - \operatorname{Prob} \left[ y _ {k} = j | \mathbf {x} _ {- k, \cdot}, B _ {k}, \mathbf {w} _ {j} z _ {i}; x _ {k, \cdot} = 0 \right]\tag{15}
$$

where $x _ { 1 } , \ldots$ refers to a vector containing all the regressors in the model except $x _ { k _ { i } \cdot j }$

According to the data coding scheme described in Section 3.3, for product feature $l , x _ { k , \cdots }$ refers to $x _ { k , l , \mu , \mu , \nu , o }$ or $x _ { k , l , \theta , \mu \mu }$ . Both are dummy variables that indicate whether product feature l is a pro or a con in review k. The marginal effect calculated in Equation 15 is at the individual level. After analyzing all the collected reviews and deriving the average marginal effect across all reviewers in our dataset, we obtain the aggregate marginal effect (or marginal effect for short) of $x _ { 1 , l , \mu , \mu , \nu , \rho }$ or $\pmb { \chi } _ { \pmb { \imath } , \pmb { \imath } , \pmb { \imath } , \pmb { \imath } }$ for different rating scores. The marginal effect of $x _ { 1 , i , j , p , r , o }$ for rating score $j ,$ denoted $\mathrm { M } _ { l , \mathrm { p r o } , j }$ , means that if we improve feature l so that consumers will consider this feature a pro, the probability to give rating score j to the product will be changed by $| \mathbf { M } _ { l , \mathrm { p r o } , j } |$ (the change direction depends on the sign of ${ \bf M } _ { l , \mathrm { p r o } , j } )$ . We interpret the meaning of $\mathbf { M } _ { l , \mathrm { c o n } , j }$ (the marginal effect of $\pmb { \mathcal { T } } _ { \bullet , \pmb { l } , \pmb { \mathbb { E } } \pmb { \mathbb { O } } \pmb { \mathbb { \mathbf { n } } } }$ for rating score j) similarly: If we do not improve feature l so that consumers will become unsatisfied (i.e., considering this feature a con), the probability to give rating score $j$ to the product will be changed by $| \mathbf { M } _ { l , \mathrm { c o n } , j } |$ Because we have a total of J+1 rating levels (from 0 to J) in our model, we have J+1 marginal effect pairs for each product feature extracted from online product reviews. These marginal effect pairs reflect consumers’ satisfaction, at the product feature level.

## 5.2 Our Proposed Marginal Effect-Based Kano Model (MEKM)

To categorize customer requirements, we propose the MEKM model, based on the marginal effect pairs of product features derived from the MOCM model. The marginal effect pairs $( \mathrm { i } . \mathrm { e } . , \mathrm { M } _ { l , \mathrm { p r o } , j }$ and $\mathbf { M } _ { l , \mathrm { c o n } , j }$ for product feature l) are defined for each rating level j (from 0 to J), so they create too many marginal effect pairs. In response, we first combine the rating levels

#

into fewer rating groups and focus on two extremes only (i.e., low and high rating groups). We then calculate the average marginal effects for the two groups. When reviewers consider a product feature a con, it typically increases the chances that they assign low rating scores to the product. On the contrary, when reviewers become positive about a product feature (i.e., the product feature becomes a pro), it generally increases the chances that reviewers give high rating scores to that product. As a result, we concentrate on $\mathrm { M } _ { l , \mathrm { c o n , l o w } }$ and $\mathrm { M } _ { l , \mathrm { p r o } , \mathrm { h i g h } }$ only (i.e., exclude $\mathbf { M } _ { l , \mathrm { c o n , h i g h } }$ and $\mathrm { M } _ { l , \mathrm { p r o } , \mathrm { l o w } } )$ when developing our MEKM model.

For example, in a five-star rating scale, we can combine the 1 and 2 stars to constitute the low rating group, assign 3 to represent the medium group, and use 4 and 5 stars to denote the high group. Assume that $\mathrm { M } _ { l , \mathrm { p r o } , 1 } = 0 . 1 , \mathrm { M } _ { l , \mathrm { p r o } , 2 } = 0 . 2 , \mathrm { M } _ { l , \mathrm { p r o } , 3 } = 0 . 2 , \mathrm { M } _ { l , \mathrm { p r o } , 4 } = 0 . 1 , \mathrm { M } _ { l , \mathrm { p r o } , 5 } = 0 . 4$ $\mathrm { M } _ { l , \mathrm { c o n } , 1 } = 0 . 6 , \mathrm { M } _ { l , \mathrm { c o n } , 2 } = 0 . 1$ $\mathbf { M } _ { l , \mathrm { c o n } , 3 } = 0 . 1$ $\mathbf { M } _ { l , \mathrm { c o n } , 4 } = 0 . 1$ , and $\mathbf { M } _ { l , \mathrm { c o n } , 5 } = 0 . 1$ The average marginal effect of feature l for the low rating group when feature l is considered unsatisfactory (con) is $\mathbf { M } _ { l , \mathrm { c o n , l o w } } = 0 . 3 5$ (i.e., average of $\mathbf { M } _ { l , \mathrm { c o n } , 1 }$ and $\mathbf { M } _ { l , \mathrm { c o n } , 2 } )$ . That is, if we do not improve feature l and let consumers consider this feature unsatisfactory, the probability that consumers will give low rating scores (i.e., 1 and 2) to the product will increase by 0.35. The average marginal effect of feature l for the high rating group when feature l is considered satisfactory (pro) instead is $\mathbf { M } _ { l , \mathrm { p r o , h i g h } } = 0 . 2 5$ (i.e., average of $\mathrm { M } _ { l , \mathrm { p r o } , 4 }$ and $\mathbf { M } _ { l , \mathrm { p r o } , 5 } )$ . This average marginal effect indicates that if we improve feature l so that consumers are satisfied with this feature, the probability that consumers will give high rating scores (i.e., 4 and 5) to the product will increase by 0.25.

Following the general framework of the Kano model, we use $\mathrm { M } _ { l , \mathrm { c o n , l o w } }$ and $\mathrm { M } _ { l , \mathrm { p r o , h i g h } }$ to form a two-dimensional space in our proposed MEKM model, in which product features are divided into six categories according to the signs and values of the two marginal effects for each focal feature (the detailed classification conditions are in Table 1):

1. Must-be feature: If both $\mathrm { M } _ { l , \mathrm { p r o , h i g h } }$ and $\mathrm { M } _ { l , \mathrm { c o n , l o w } }$ are greater than 0, but $\mathbf { M } _ { l , \mathrm { p r o } , \mathrm { h i g h } } \ \ll$ (much less than) $\mathrm { M } _ { l , \mathrm { c o n , l o w } }$ , then feature l is a must-be feature. That is, $\mathbf { M } _ { l , \mathrm { c o n , l o w } } > 0$ indicates that if we do not improve feature l so that consumers are negative about this feature (i.e., considering this feature a con), the probability that consumers will give low rating scores increases. On the other hand, if we improve feature l so that consumers are positive about it, the probability to assign high rating scores increases $( \mathrm { i . e . , M } _ { l , \mathrm { p r o , h i g h } } > 0 )$ ; however, this increase is much less than the increase in the probability of giving low rating scores when consumers consider feature l unsatisfactory(i.e., $\mathbf { M } _ { l , \mathrm { p r o , h i g h } } \ll \mathbf { M } _ { l , \mathrm { c o n , l o w } } )$ .In this case, it is better to fulfill the customer requirements on product feature l.

2. Performance feature: If both $\mathrm { M } _ { l , \mathrm { p r o , h i g h } }$ and $\mathrm { M } _ { l , \mathrm { c o n , l o w } }$ are greater than 0 and the values of these two variables are similar, feature lis a performance feature. In other words, the fulfillment of customer requirements on this feature will result in customer satisfaction (i.e., $\mathbf { M } _ { l , \mathrm { p r o , h i g h } } > 0 )$ , whereas lack of fulfillment of will prompt customer dissatisfaction, with a similar magnitude $\mathrm { ( i . e . , M } _ { l , \mathrm { c o n , l o w } } > 0$ and $\mathbf { M } _ { l , \mathrm { p r o , h i g h } } \approx \mathbf { M } _ { l , \mathrm { c o n , l o w } } )$

3. Excitement feature: If both $\mathbf { M } _ { l , \mathrm { p r o , h i g h } }$ and $\mathrm { M } _ { l , \mathrm { c o n , l o w } }$ are greater than 0, but $\mathbf { M } _ { l , \mathrm { p r o , h i g h } } \gg$ $\mathrm { M } _ { l , \mathrm { c o n , l o w } ; }$ , feature l is an excitement feature. That is, the fulfillment of customer requirements on feature l will result in customer satisfaction $( { \mathrm { i . e . , ~ M } } _ { l , { \mathrm { p r o , h i g h } } } > 0 )$ , but the lack of fulfillment of customer requirements on feature l causes dissatisfaction (i.e.,

#

$\mathbf { M } _ { l , \mathrm { c o n , l o w } } > 0 )$ with a lesser degree compared to $\mathbf { M } _ { l , \mathrm { p r o , h i g h } } \left( \mathrm { i . e . , } \mathbf { M } _ { l , \mathrm { p r o , h i g h } } \right. \gg \mathbf { \ M } _ { l , \mathrm { c o n , l o w } } )$

4. Innovation-needed feature: If $\mathrm { M } _ { l , \mathrm { p r o , h i g h } }$ is less than 0, and $\mathrm { M } _ { l , \mathrm { c o n , l o w } }$ is greater than 0, feature l is an innovation-needed feature. That is because, in this case, whether we improve feature l or not, consumers will increase their probability to assign low rating scores $( \mathrm { i . e . , M } _ { l , \mathrm { c o n , l o w } } > 0 )$ and decrease their probability to offer high rating scores (i.e., $\mathbf { M } _ { l , \mathrm { p r o , h i g h } } < 0 )$ . In other words, consumers are not satisfied with the current design of feature l, so a revolutionary change in this feature l may be welcomed.

5. Reverse feature: If both $\mathbf { M } _ { l , \mathrm { p r o , h i g h } }$ and $\mathrm { M } _ { l , \mathrm { c o n , l o w } }$ are less than 0, then feature l is a reverse feature. This condition denotes that the fulfillment of feature l will result in customer dissatisfaction $( \mathrm { i . e . , ~ M _ { \mathit { l } , \mathrm { p r o , h i g h } } ~ < ~ 0 ) }$ , whereas leaving feature l unfulfilled will invoke customer satisfaction $( \mathrm { i . e . , M } _ { l , \mathrm { c o n , l o w } } < 0 )$

6. Divergent feature: If $\mathrm { M } _ { l , \mathrm { p r o , h i g h } }$ is greater than 0 but $\mathrm { M } _ { l , \mathrm { c o n , l o w } }$ is less than 0, feature l is a divergent feature. In this case, the fulfillment of feature l will result in customer satisfaction $( \mathrm { i . e . , M } _ { l , \mathrm { p r o , h i g h } } > 0 )$ , but so does its lack of fulfillment $( \mathrm { i . e . , M } _ { l , \mathrm { c o n , l o w } } < 0 )$ . That is, customers’ opinions about feature l are conflicting.

Table 1: Classification Conditions in the MEKM Model

<table><tr><td>Condition</td><td>Feature Category</td></tr><tr><td> $M_{l,pro,high} > 0$ ,  $M_{l,con,low} > 0$  and  $M_{l,pro,high} \ll M_{l,con,low}$ </td><td>Must-be feature</td></tr><tr><td> $M_{l,pro,high} > 0$ ,  $M_{l,con,low} > 0$  and  $M_{l,pro,high} \approx M_{l,con,low}$ </td><td>Performance feature</td></tr><tr><td> $M_{l,pro,high} > 0$ ,  $M_{l,con,low} > 0$  and  $M_{l,pro,high} \gg M_{l,con,low}$ </td><td>Excitement feature</td></tr><tr><td> $M_{l,pro,high} < 0$ ,  $M_{l,con,low} > 0$ </td><td>Innovation-needed feature</td></tr><tr><td> $M_{l,pro,high} < 0$ ,  $M_{l,con,low} < 0$ </td><td>Reverse feature</td></tr><tr><td> $M_{l,pro,high} > 0$ ,  $M_{l,con,low} < 0$ </td><td>Divergent feature</td></tr></table>

By using a two-dimensional graph in which the horizontal axis represents $\mathrm { M } _ { l , \mathrm { p r o , h i g h } }$ and the vertical axis denotes $\mathrm { M } _ { l , \mathrm { c o n } , \mathrm { l o w } } ,$ we can map these six product feature categories to six areas (Figure 3). The performance feature lies around the 45 degree dashed line $( \mathrm { i . e . , \ M _ { \mathit { l } , \mathrm { p r o , h i g h } } \approx }$ $\mathbf { M } _ { l , \mathrm { c o n , l o w } } )$ in the first quadrant (i.e., where $\mathbf { M } _ { l , \mathrm { p r o , h i g h } } > 0$ and $\mathbf { M } _ { l , \mathrm { c o n , l o w } } > 0 )$

![](/api/attachments/ZSE5RAQB/fulltext/images/0480e07958e9cc6808f45d3b655a6bc1be306974d502d153ca0f7bbfbe43ee64.jpg)  
Figure 3: Product Feature Classification in the Proposed MEKM Model

## 6. Empirical Study

In this section, we conduct an empirical study to evaluate the effectiveness of the proposed econometric preference measurement model (i.e., MOCM) and demonstrate the utility of our proposed MEKM model, using online product reviews collected from a popular product review website, Epinions.com. In the following, we describe our data collection and then some important evaluation results.

## 6.1 Data Collection and Preparation

We collected all product reviews about mobile phones posted on Epinions.com before November 2103, together with reviewer profiles. Each online product review included the title of the review, pro/con phrases, the detailed free-text review, the date that the review was posted, and the overall product rating (on a five-star scale). The reviewer profile consisted of the list of reviews this reviewer had written and his or her trust network (i.e., who trusts the focal reviewer and who is trusted by this reviewer). Because mobile phones typically invoke plentiful discussions online, we considered any phones with few online reviews are not well discussed, such that the opinions expressed in this limited set of reviews likely are not representative. Accordingly, we discarded brands that prompted no more than 55 reviews.<sup>4</sup> Finally, we obtained a dataset with 2,425 online product reviews, spanning 9 popular brands and 186 models in the mobile phone market.

Figure 4 illustrates the distribution of different rating scores in our dataset. This positively-skewed (J-shaped) distribution is consistent with the pattern commonly found on the online rating platforms (Dellarocas & Narayan, 2006; McGlohon et al., 2010). Table 2 shows some statistics of our dataset, including the number of reviews written by a reviewer, the number of members trusting a reviewer, and the number of members trusted by a reviewer.

![](/api/attachments/ZSE5RAQB/fulltext/images/eb173fbc88cd3dbabada3f5ec861d79f94a1e9c4738f40b8c5dcd0607e6b18fe.jpg)  
Figure 4: Distribution of Rating Scores in Our Dataset

Table 2: Statistics of Our Dataset

<table><tr><td></td><td>Number of reviews by a reviewer</td><td>Number of members trusting a reviewer</td><td>Number of members trusted by a reviewer</td></tr><tr><td>Min</td><td>1</td><td>0</td><td>0</td></tr><tr><td>Max</td><td>18</td><td>450</td><td>446</td></tr><tr><td>Average</td><td>1.084</td><td>8.183</td><td>7.832</td></tr><tr><td>Standard Deviation</td><td>0.5524</td><td>35.9755</td><td>34.5049</td></tr></table>

We extracted 25 features from the pro/con phrases across all product reviews in our dataset by using the product feature extraction procedure (denoted as the PFE procedure) described in Section 3.1. To assess the quality of these extracted product features, we conducted a validation experiment. In this experiment, we randomly drew two non-overlapped samples from our dataset, and each sample contained 100 product reviews. Subsequently, we recruited two graduate students from a business school, both with at least six years’ experience with mobile phone usage. Each coder was asked to examine one sample (i.e., 100 reviews) by assigning each pro and con mentioned in these reviews into the 25 product features identified by the PFE procedure. On the basis of these two samples, we compared the product features extracted by the PFE procedure with those manually assigned by the two coders. As Table 3 illustrates, their relative frequencies were comparable across all product features. The Pearson correlation coefficient was 0.98, suggesting the effectiveness of our PFE procedure. We also calculated the Cohen’s kappa coefficient for each product feature to measure the agreement between the two methods (i.e., PFE and manual assignment).<sup>5</sup> The average

Cohen’s kappa coefficient across the 25 product features was 0.8129, with a maximum of 1 (“battery”) and a minimum of 0.6468 (“reliability and quality”). The Cohen’s kappa coefficient indicated good agreement between the two methods, which also suggested the satisfactory effectiveness of our PFE procedure.

--- Insert Table 3 Here -- ---

Figure 5 shows the distributions of the 25 features in our dataset. The “Apps,” “design,” and “weight” features were more frequently considered pros rather than cons, whereas reviewers’ sentiments on “easy to use,” “price,” and “screen” features were quite balanced. In contrast, reviewers were more negative on the “battery,” “interface,” and “reliability” features.

![](/api/attachments/ZSE5RAQB/fulltext/images/384a7e97e95e59c200fdbed5f8803e67a94d14e29aae12a34920faba50b76296.jpg)  
Figure 5: Distribution of Features Discussed in the Pro and Con Fields of the Reviews

Subsequently, we used the trust relations between reviewers in our dataset to construct a trust network (Figure 6). We then employed the normalized PageRank value (Langville & Meyer, 2004) of each reviewer in this network to represent his or her position or reputation in the community. When calculating PageRank values, the damping factor was set as 0.85. We also normalized the total number of reviews written by each reviewer, using $( n _ { i } - \operatorname* { m i n } ( - ) ) / ( \operatorname* { m a x } ( - ) - \operatorname* { m i n } ( - ) )$ , where ${ \bf \delta n _ { i } }$ denotes the number of reviews written by reviewer $i ,$ and and refer to the minimum and maximum number of reviews written among all reviewers in the dataset, respectively.

![](/api/attachments/ZSE5RAQB/fulltext/images/0671393489b01d912380c27430e62f1d84844c03bb9bcb06b3e3097885ce841a.jpg)  
Figure 6: Trust Network of Reviewers

## 6.2 Model Estimation and Comparison

In this subsection, we use the collected dataset to estimate our econometric preference measurement model (i.e., MOCM). We also estimate aggregate consumer preferences using three prevalent models as the benchmarks for our proposed model: Poisson Regression Model (PRM), Negative Binomial Regression Model (NBRM), and Basic Ordered Choice Model (BOCM).

For both PRM and NBRM, we follow Decker and Trusov (2010) and employ the 25 product features extracted from online product reviews, in conjunction with reviewers’ sentiment orientations (pros or cons) toward the features, as the independent variables (i.e., a total of 50 independent variables) and the nine brand names as control variables. Furthermore, we assume that the rating score (i.e., the dependent variable) satisfies a Poisson distribution for the PRM model or a negative binominal distribution for the NBRM model. Accordingly, PRM and NBRM can be described by Equations 16 and 17, respectively:

$$
\operatorname{Prob} \left[ y _ {k} = j \mid \mathbf {x} _ {k, r}, B _ {k} \right] = \frac {\lambda^ {j}}{j !} \exp (- \lambda), \text {where} \lambda = \exp (\alpha + \beta^ {\prime} \cdot (\mathbf {x} _ {k, \text {pro}}, \mathbf {x} _ {k, \text {con}}, B _ {k}))\tag{16}
$$

$$
\operatorname{Prob} \left[ y _ {k} = j \mid \mathbf {x} _ {k,}, B _ {k} \right] = \binom {j + \tau - 1} {j} \frac {\lambda^ {j} \tau^ {\tau}}{(\lambda + \tau) ^ {j + \tau}}, \text { where } \tau > 0 \text { and } \lambda = \exp (\alpha + \beta^ {\prime} \cdot (\mathbf {x} _ {k, \text { pro }}, \mathbf {x} _ {k, \text { con }}, B _ {k}))\tag{17}
$$

In Equation 17, can be taken as the Gamma parameter in the distribution. All the parameters in Equations 16 and 17 are estimated using the maximum likelihood methods.

For the BOCM model (see Equations 3 and 4), though it uses the same independent and control variables as PRM and NBRM do, the dependent variable (the rating score) is modeled by a more reasonable ordinal model. Finally, in our proposed MOCM model, we extend the BOCM model to account for reviewers’ heterogeneity. The brand name and reviewer’s sentiment orientations towards each product feature are treated as explanatory variables (independent variables; Equation 9). To account for reviewer heterogeneity, we also consider

#

the number of reviews each reviewer has written (n ) after normalization and the normalized PageRank value of each reviewer $( t r _ { i } )$ . In our empirical study, the former is treated as an explanatory variable for Equation 6 and the latter is an explanatory variable in Equation 8. The parameters in the MOCM model are estimated by the maximum simulated likelihood method.

What should be noted here is that, we do not incorporate reviewer profile (i.e., $t r _ { i }$ and $n _ { i } )$ into the PRM and NBRM models when comparing the performance of different models. That is mainly because these two models are counting models and are usually designed to model interval scale data rather than ordinal scale data. Furthermore, unlike product features

$( \sum \limits _ { k _ { n } = \infty } ^ { \infty } \log _ { n } , \sum \limits _ { k _ { n } = \infty } ^ { \infty } \log _ { n } ( 0 ) )$ and product brand $( \theta _ { \tt H } )$ , individual reviewer profiles do not affect rating scores

directly. Instead, they generally influence rating scores indirectly through reviewers’ rating behavior. As a result, it is not reasonable to directly incorporate this information into PRM and NBRM. Incorporating reviewer profiles indirectly into PRM and NBRM and comparing their performance with our proposed MOCM model will be our future research work.

Table 4 illustrates the estimation results of the three benchmark models and our proposed MOCM model. According to Table 4, most product features with significant effects have the expected signs (i.e., pros with a positive sign and cons with a negative sign). The signs for the control variables (brands) are mostly consistent across the four models. Table 5 summarizes the comparison results for these four models. In this study, we use the log likelihood and Akaike Information Criterion (AIC) (Akaike, 1974) as the model evaluation criteria. The log likelihood is a criterion that measures the goodness of fit of a given statistical (or econometric) model, whereas AIC is a relative estimate of the information loss when the model is used to represent the “true” model that generates a given set of data. The information loss estimated by AIC takes into account the tradeoff between the goodness of fit and the complexity of the model. Given a set of candidate models, the model that minimizes the information loss (i.e., has the lowest AIC value) is considered the best model. The log likelihood measure may be biased towards a more complex model, but AIC does not because it also considers the model complexity. As Table 5 illustrates, among the four models examined, our proposed MOCM model attains the highest value in the log likelihood measure, but its AIC value is the lowest. Thus, in terms of log likelihood and AIC, our proposed MOCM model outperforms the extant three preference measurement models (i.e., PRM, NBRM, and BOCM).

---Insert Table 4 Here--

Table 5: Comparison of Different Models

<table><tr><td colspan="2"></td><td>PRM</td><td>NBRM</td><td>BOCM</td><td>MOCM</td></tr><tr><td rowspan="3">Property</td><td>Heterogeneity</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr><tr><td>Heteroscedasticity</td><td>-</td><td>-</td><td>No</td><td>Yes</td></tr><tr><td>Different Thresholds</td><td>-</td><td>-</td><td>No</td><td>Yes</td></tr><tr><td rowspan="2">Model Fitness</td><td>Log Likelihood</td><td>-4313.61</td><td>-4128.53</td><td>-2986.90</td><td>-2961.10</td></tr><tr><td>Akaike Information Criterion</td><td>8745.20</td><td>8375.06</td><td>6097.80</td><td>6066.20</td></tr></table>

However, a model with high explanatory power may be subject to potential predictive falsification (Shugan, 2009; Decker & Trusov, 2010). To test for this concern, we conduct 15 random and independent cross-validation experiments by using the holdout method to compare the hit rate of different models. Specifically, in each experiment, we first randomly divide the dataset into a calibration set (containing 90% of the dataset, i.e., 2,183 observations) and a prediction set (10% of the dataset, i.e., 242 observations). Subsequently, we use the calibration set to train a model and the prediction set to test its prediction effectiveness (measured by hit rate). We repeat this process 15 times and the overall performance of the model is the average of the 15 trials. Figure 7 shows the results of the 15 experiments for all models. As Figure 6 illustrates, our proposed MOCM model consistently outperforms the three benchmark models over the 15 trials, and the PRM model again represents the least effective model (measured by hit rate). The t-test (α = 0.05 and α = 0.1) between the proposed MOCM model and each benchmark model also supports our conclusion.

![](/api/attachments/ZSE5RAQB/fulltext/images/d3f3eaa0930c9b89044bad7d72acb654330a36f65056d03e7493b85884c0536d.jpg)  
Figure 7: Hit Rates of Different Models

We further perform a sensitivity analysis on the granularity of the rating scale (i.e., dependent variable). In the previous evaluations, the rating scale consists of 5 levels; with this experiment, we transform the scale into three levels (i.e., low, medium, and high) and examine whether our proposed MOCM model still performs better than the three benchmark models. The results show that the hit rate of each model improves. In addition, our proposed MOCM model still outperforms the other three models. Specifically, the hit rate of the MOCM model is 61.30%, which is greater than that for PRM (49.56%), NBRM (55.86%), or

BOCM (56.25%). This sensitivity analysis accordingly demonstrates the robustness of our proposed econometric preference measurement model (i.e., MOCM).

## 6.3 Categorization of Customer Requirements using MEKM

Using the MOCM model estimated in the previous section, we calculate, for each product feature, average marginal effect pairs for the high and low rating groups, then analyze the customer requirements using our proposed MEKM model. Figure 8 illustrates the results of the MEKM model, which maps the 25 product features onto a two-dimensional graph. Six product features are considered performance features: “navigation,” “multimedia,” “screen,” “Web browsing,” “camera,” and “voice.” “Reliability,” “text support”, and “easy to use” are labeled as must-be features; “price,” “weight,” “battery,” “OS (operating system),” “configuration,” “Wifi,” “speed,” and “new functions” are classified as excitement features. On the other hand, the divergent features include “service,” “design,” “Apps,” “software,” and “appearance,” whereas innovation-needed features encompass “accessory,” “display,” and “interface.” No product feature is classified as a reverse feature.

![](/api/attachments/ZSE5RAQB/fulltext/images/b0227f282f53c8e8c20c20cb80c3ce006e00569366cb80dfae44ef12fdf58391.jpg)  
Figure 8: Classification of Features of Mobile Phones using the MEKM Model

The managerial implications from the MEKM model can be derived as follows. Must-be features (“reliability,” “text support,” and “easy to use”) represent customers’ basic requirements for a mobile phone. Thus, all mobile phone companies must ensure that their mobile phones fulfill these basic requirements. Furthermore, the MEKM model can help mobile phone companies to develop their product design or improvement plans according to their competitive strategies.<sup>7</sup> For example, mobile phone companies with a cost leadership

#

strategy typically target a broad market rather than a narrow, niche market and make their efforts to reduce product costs to become low-cost producers in the industry. Because customer satisfaction is proportional to the level of fulfillment of performance features (i.e., “navigation,” “multimedia,” “screen,” “Web browsing,” “camera,” and “voice”), most mobile phones compete on the performance features. Thus, the market for mobile phones that focus on achieving performance features generally is a relatively broad segment. Mobile phone companies that pursue a cost leadership strategy therefore should compete on this market and develop cost-effective methods to fulfill these performance features.

Mobile phone companies with a differentiation strategy instead should focus on excitement features (“price,” “weight,” “battery,” “OS (operating system),” “configuration,” “Wifi,” “speed,” and “new functions”). Customers often can tolerate the current design of an excitement feature (even if their requirements are not completely fulfilled), but will be delighted when this feature is improved. Thus, excitement features offer a wide range of possibilities for differentiation. In addition, companies with a differentiation strategy can also concentrate on the divergent features (“service,” “design,” “Apps,” “software,” and “appearance”) and find ways to differentiate their products from competitors’ ones. Because consumer preferences for divergent features differ or even conflict, firms can attempt to group consumer preferences with respect to the divergent features and design different types of mobile phones to match those varying preferences and seek new market segments.

Finally, if mobile phone companies adopt an innovation strategy, they should pay more attention to innovation-needed features (“accessory,” “display,” and “interface”), because customers are not satisfied with their current designs. Thus, these product features call for innovative designs, and companies should target some or all of the innovation-needed features by designing mobile phones with revolutionary changes on the selected features.

## 7. Conclusions and Future Research Directions

Opinion sharing platforms provide open, convenient communication channels for sharing and gathering consumers’ experiences with and preferences for various products. Meanwhile, these online product reviews also represent unique and valuable information sources for firms to understand the preferences of their customers. In this study, we focus on how to measure aggregate consumer preferences from online product reviews and then categorize customer requirements for supporting product design/improvement decisions. Accordingly, we first establish a framework for semi-automatically extracting product features and reviewers’ sentiment orientations from online product reviews. We then propose an econometric preference measurement model, i.e., the modified ordered choice model (MOCM), to extract aggregate consumer preferences. Furthermore, to categorize customer requirements and support product design at the product feature level, we propose a marginal effect-based Kano model (MEKM) by extending the Kano model.

Our research contributions are three-fold. First, this study contributes to online product review research in information systems (IS) field. Most of IS literature on product reviews investigate how online product reviews affect product sales (Chen & Xie, 2008; Forman,

#

Ghose, & Wiesenfeld, 2008; Kuksov & Xie, 2010; Zhang, Guo, & Goes, 2013) or examine the antecedents of the helpfulness of product reviews (Mudambi & Schuff, 2010; Korfiatis, García-Bariocanal, & Sánchez-Alonso, 2012; Yin, Bond, & Zhang, 2014). Our current study extends the scope of IS research on online product reviews and propose effective and viable methods for converting a vast amount of data (i.e., online product reviews) into useful business intelligence (i.e., preference measurement).

Second, this study also contributes to the preference measurement literature by offering a more effective econometric model with a strong theoretical foundation to estimate aggregate consumer preferences from online product reviews. Traditionally, aggregate consumer preferences are estimated by means of conjoint analysis using preference data collected from surveys or experiments. However, such preference elicitation method is usually time consuming and costly. This study provides an econometric framework that turns online product reviews into aggregated consumer preferences. Specifically, we develop a modified ordered choice model (MOCM), which considers the heteroscedasticity of reviewers’ rating variance and allows reviewers to assign rating scores according to their own thresholds. Using a dataset collected from a popular product review website, Epinions.com, our empirical study shows that the proposed MOCM model outperforms the three benchmark models (i.e., PRM, NBRM, and BOCM).

Third, our study also contributes to the product design literature by proposing a marginal effect-based Kano model (MEKM) to categorize and prioritize customer requirements at the product feature level. The proposed MEKM model seamlessly integrates our proposed econometric preference measurement model and the traditional Kano model to analyze and visually portray the impact of product feature improvement on consumer satisfaction. Using our dataset, we empirically demonstrate the utility of the MEKM model.

Our research also has several practical implications. First, this study offers useful models (i.e., MOCM and MEKM) that managers and practitioners can use to extract and measure aggregate consumer preferences and categorize customer requirements from online product reviews. For example, product designers can employ our proposed MEKM model to comprehend customer requirements by categorizing product features into different categories, including must-be, performance, excitement, innovation-needed, divergent, and reverse features. Such understanding can facilitate product designers to derive product design or improvement plans according to their competitive strategies. Second, marketing managers can also exploit the categorization of product features for improving the effectiveness of their advertising decisions. For example, for firms with a differentiation strategy, their advertising should emphasize excitement and divergent features (if they have improved these features) rather than highlighting performance features.

Our study has some limitations that warrant additional research attention. First, in this study, we assume that all product reviews available on online product review platforms are contributed by honest reviewers and, thus, their reviews are not manipulated or fake. However, spam reviews can easily be found online. How to identify such untruthful reviews

#

is a growing research issue (Jindal & Liu, 2008; Mukherjee, Liu, & Glance, 2012). Combining our study with a good spam review detection method would constitute an important, interesting research direction. Second, our current study only focuses on semi-structured reviews. However, as we mentioned previously, our research can easily be extended to handle free-text reviews. Thus, to enhance the applicability of our proposed econometric framework, it is desirable to incorporate an existing opinion mining method or develop a new opinion mining method such that our proposed framework can also take free-text reviews as inputs. Third, a possible concern of our study stems from the representativeness of reviewers in online product review websites. It is commonly known that online reviewers may not be representative of the target population. Therefore, the appropriateness of using online product reviews to infer general consumer preferences depends on the representativeness of the reviewers and online product reviews included in the analysis. To lessen this concern, a possible direction for future research is to include reviews from multiple product review websites in order to reduce biases associated with individual websites. Alternatively, we can also collect the profiles of reviewers and adopt some statistical methods to control the possible self-selection problem in online review data. Finally, a promising future research direction is to add a temporal dimension to the current study. It will be interesting to develop an econometric model to capture the evolution of aggregate consumer preferences and then examine how aggregate consumer preferences evolve over time and how the evolution of consumer preferences influences product design or improvement decisions.

## Acknowledgments

This work was supported in part by the National Science Council of Taiwan under the grant NSC 100-2410-H-002-021-MY3 and by the Research Fund for the Doctoral Program of Higher Education of China (20120073110029), Inter discipline Foundation of Shanghai Jiao Tong University (No. 11JCZ02), National Natural Science Foundation of China (No. 71371123, 71131005), and Europe-China High Value Engineering Network (EC-HVEN: 295130).

## References

Abrahams, A.S., Jiao, J., Fan, W., Wang, G.A., & Zhang, Z. (2013). What’s buzzing in the blizzard of buzz? Automotive component isolation in social media postings. Decision Support Systems, 55(4), 871-882.

Akaike, H. (1974). A new look at the statistical model identification. IEEE Transactions on Automatic Control, 19(6), 716-723.

Archal, N., Ghose, A., & Ipeirotis, P.G. (2007). Show me the money!: Deriving the pricing power of product features by mining consumer reviews. Proceedings of the 13th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 56-65.

Archak, N., Ghose, A., & Ipeirotis, P.G. (2011). Deriving the pricing power of product features by mining consumer reviews. Management Science, 57(8), 1485-1509.

Berger, C., Blauth, R., Boger, D., Bolster, C., Burchill, G., DuMouchel, W., Pouliot, F., Richter, R., Rubinoff, A., Shen, D., Timko, M., & Walden, D., (1993). Kano's methods for understanding customer-defined quality. Center for Quality Management Journal, 2(4), 3-35.

Branavan, S., Chen, H., Eisenstein, J., & Barzilay, R. (2009). Learning document-level semantic properties from free-text annotations. Journal of Artificial Intelligence Research, 34(2), 569-603.

Cambria, E., Schuller, B., Xia, Y., & Havasi, C. (2013). New avenues in opinion mining and sentiment analysis. IEEE Intelligent Systems, 28(2), 15-21.

Chen, Y., Wang, Q., & Xie, J. (2011). Online social interactions: A natural experiment on word of mouth versus observational learning. Journal of Marketing Research, 48(2), 238-254.

Chen, Y. & Xie, J. (2008). Online consumer review: Word-of-mouth as a new element of marketing communication mix. Management Science, 54(3), 477-491.

Chen, C.C. & Chuang, M.C., (2008). Integrating the Kano model into a robust design approach to enhance customer satisfaction with product design. International Journal of Production Economics, 114(2), 667-681.

Chevalier, J.A. & Mayzlin, D. (2006). The effect of word of mouth on sales: Online book reviews. Journal of Marketing Research, 43(3), 345-354.

Decker, R. & Trusov, M. (2010). Estimating aggregate consumer preferences from online product reviews. International Journal of Research in Marketing, 27(4), 293-307.

Dellarocas, C. and Narayan, R. (2006). A statistical measure of a population’s propensity to engage in post-purchase online word-of-mouth. Statistical Science, 21(2), 277-285.

Dai, W., Han, D., Dai, Y., & Xu, D. (2015). Emotion recognition and affective computing on vocal social media. Information & Management (forthcoming).

Eluru, N., Bhat, C.R., & Hensher, D.A. (2008). A mixed generalized ordered response model for examining pedestrian and bicyclist injury severity level in traffic crashes. Accident Analysis & Prevention, 40(3), 1033-1054.

Fader, P.S. & Hardie, B.G. (1996). Modeling consumer choice among SKUs. Journal of Marketing Research, 33(4), 442-452.

Forman, C., Ghose, A., & Wiesenfeld, B. (2008). Examining the relationship between reviews and sales: The role of reviewer identity disclosure in electronic markets.Information Systems Research, 19(3), 291-313.

Ghose, A., Ipeirotis, P.G., & Li, B. (2012). Designing ranking systems for hotels on travel search engines by mining user-generated and crowdsourced content. Marketing Science, 31(3), 493-520.

Ghose, A., Ipeirotis, P.G., & Sundararajan, A. (2007). Opinion mining using econometrics: A case study on reputation systems. Proceedings of the 45th Annual Meeting of the Association of Computational Linguistics, 416-423.

Green, P.E. & Rao, V.R. (1971). Conjoint measurement for quantifying judgmental data. Journal of Marketing Research, 8(3), 355-363.

Greene, W., Harris, M.N., Hollingsworth, B., & Weterings, T.A. (2014). Heterogeneity in ordered choice models: A review with applications to self-assessed health. Journal of Economic Surveys, 28(1), 109-133.

Greene, W.H. & Hensher, D.A. (2010). Modeling Ordered Choices: A Primer: Cambridge University Press.

Gu, B., Park, J., & Konana, P. (2012). The impact of external word-of-mouth sources on retailer sales of high-involvement products. Information Systems Research, 23(1), 182-196.

Halme, M. & Kallio, M. (2011). Estimation methods for choice-based conjoint analysis of

consumer preferences. European Journal of Operational Research, 214(1), 160-167.

He, W., Wu, H., Yan, G., Akula, V., & Shen, J. (2015). A novel social media competitive analytics framework with sentiment benchmarks. Information & Management (forthcoming).

Hu, M. & Liu, B. (2004). Mining and summarizing customer reviews. Proceedings of the Tenth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 168-177.

Hui, S.K., Fader, P.S., & Bradlow, E.T. (2009). Path data in marketing: An integrative framework and prospectus for model building. Marketing Science, 28(2), 320-335.

Jindal, N. & Liu, B. (2008). Opinion spam and analysis. Proceedings of the 2008 International Conference on Web Search and Data Mining, 219-230.

Janne, H. & Timo, P., (1998). Sharpening logistics customer service strategy planning by applying Kano’s quality element classification. International Journal of Production Economics, 56/57, 253-260.

Kano, N., Seraku, N., Takahashi, F., & Tsuji, S. (1984). Attractive quality and must-be quality. The Journal of the Japanese Society for Quality Control, 14(2), 39-48.

Kim, S.M. & Hovy, E. (2006). Automatic identification of pro and con reasons in online reviews. Proceedings of the COLING/ACL on Main Conference Poster Sessions, 483-490.

Korfiatis, N. & Poulos, M. (2013). Using online consumer reviews as a source for demographic recommendations: A case study using online travel reviews. Expert Systems with Applications, 40(14), 5507-5515.

Korfiatis, N., García-Bariocanal, E., & Sánchez-Alonso, S. (2012). Evaluating content quality and helpfulness of online product reviews: The interplay of review helpfulness vs. review content. Electronic Commerce Research and Applications, 11(3), 205-217.

Kuksov, D. & Xie, Y. (2010). Pricing, frills, and customer ratings. Marketing Science, 29(5), 925-943.

Langville, A.N. & Meyer, C.D. (2004). Deeper inside PageRank, Internet Mathematics, 1(3), 335-380.

Lee, T.Y. & Bradlow, E.T. (2007). Automatic construction of conjoint attributes and levels from online customer reviews. Working paper, University of Pennsylvania, The Wharton Business School.

Lee, T.Y. & Bradlow, E.T. (2011). Automated marketing research using online customer reviews. Journal of Marketing Research, 48(5), 881-894.

Lee, J. & Lee, J.N. (2009). Understanding the product information inference process in electronic word-of-mouth: An objectivity–subjectivity dichotomy perspective. Information & Management, 46(5), 302-311.

Li, F., Liu, N., Jin, H., Zhao, K., Yang, Q., & Zhu, X. (2011). Incorporating reviewer and product information for review rating prediction. Proceedings of the Twenty-Second International Joint Conference on Artificial Intelligence, 3, 1820-1825.

Li, Y.M., Chen, H.M., Liou, J.H., & Lin, L.F. (2014). Creating social intelligence for product portfolio design. Decision Support Systems, 66, 123-134.

McKelvey, R.D. & Zavoina, W. (1975). A statistical model for the analysis of ordinal level dependent variables. Journal of Mathematical Sociology, 4(1), 103-120.

McGlohon, M., Glance, N., and Reiter, Z. (2010). Star quality: Aggregating reviews to rank

products and merchants. Proceedings of the Fourth International AAAI Conference on Weblogs and Social Media, 114-121.

Monica B., Marco G., &Franco S. (2005).Inside PageRank.ACM Transactions on Internet Technology, 5(1), 92-118.

Mudambi, S.M. & Schuff, D. (2010). What makes a helpful online review? A study of customer reviews on amazon.com. MIS Quarterly, 34(1), 185-200.

Mukherjee, A., Liu, B., & Glance, N. (2012). Spotting fake reviewer groups in consumer reviews. Proceedings of the 21st International Conference on World Wide Web, 191-200.

Netzer, O., Feldman, R., Goldenberg, J., & Fresko, M. (2012). Mine your own business: Market-structure surveillance through text mining. Marketing Science, 31(3), 521-543.

Netzer, O., Toubia, O., Bradlow, E.T., Dahan, E., Evgeniou, T., Feinberg, F.M., Feit, E.M., Hui, S.K., Johnson, J., Liechty, J.C., Orlin, J.B., & Rao, V.R. (2008). Beyond conjoint analysis: Advances in preference measurement. Marketing Letters, 19(3-4), 337-354.

Phang, C.W., Zhang, C., & Sutanto, J. (2013). The influence of user interaction and participation in social media on the consumption intention of niche products. Information & Management, 50(8), 661-672.

Porter, M. & Millar, C. (1985). How information gives you competitive advantage. Harvard Business Review, 63(4), 149-160.

Popescu, A.M. & Etzioni, O. (2007). Extracting product features and opinions from reviews. Chapter 2 in Natural Language Processing and Text Mining, Springer, 9-28.

Shugan, S.M. (2009). Commentary-relevancy is robust prediction, not alleged realism. Marketing Science, 28(5), 991-998.

Toubia, O., De Jong, M.G., Stieger, D., & Füller, J. (2012). Measuring consumer preferences using conjoint poker. Marketing Science, 31(1), 138-156.

Wang, B., Min, Y., Huang, Y., Li, X., & Wu, F. (2013). Review rating prediction based on the content and weighting strong social relation of reviewers. Proceedings of the 2013 International Workshop on Mining Unstructured Big Data using Natural Language Processing, 23-30.

Wei, C.P., Chen, Y.M., Yang, C.S., & Yang, C.C. (2010). Understanding what concerns consumers: a semantic approach to product feature extraction from consumer reviews. Information Systems and E-Business Management, 8(2), 149-167.

Wei, C.P., Hu, P., Tai, C.H., Huang, C.N., & Yang, C.S. (2007). Managing word mismatch problems in information retrieval: A topic-based query expansion approach. Journal of Management Information Systems, 24(3), 269-295.

Xu, Q., Jiao, R.J., Yang, X., Helander, M., Khalid, H.M., & Opperud, A. (2009). An analytical Kano model for customer need analysis. Design Studies, 30(1), 87-110.

Xu, K., Liao, S.S., Li, J., & Song, Y. (2011). Mining comparative opinions from customer reviews for Competitive Intelligence. Decision Support Systems, 50(4), 743-754.

Xu, X., Cheng, X., Tan, S., Liu, Y., & Shen, H. (2013). Aspect-level opinion mining of online customer reviews. Communications, China, 10(3), 25-41.

Yin, D., Bond, S., & Zhang, H. (2014). Anxious or angry? Effects of discrete emotions on the perceived helpfulness of online reviews. MIS Quarterly, 38(2), 539-560.

Yan, Z., Xing, M., Zhang, D., & Ma, B. (2015). EXPRS: An extended pagerank method for product feature extraction from online consumer reviews. Information & Management (forthcoming).

Zhang, Z., Guo, C., & Goes, P. (2013). Product comparison networks for competitive analysis of online word-of-mouth. ACM Transactions on Management Information Systems, 3(4), article 20.

Zhu, F. & Zhang, X. (2010). Impact of online consumer reviews on sales: The moderating role of product and consumer characteristics. Journal of Marketing, 74(2), 133-148.

##

Table 3: Result of the Validation Experiment

<table><tr><td>Feature</td><td>Description</td><td>Frequency (%)</td><td>Feature</td><td>Description</td><td>Frequency (%)</td></tr><tr><td>Apps</td><td>Apps and games</td><td> $8.25^{\dagger}(9.00^{\ddagger})$ </td><td>Multimedia</td><td>Multimedia/music and video</td><td>3.25 (4.00)</td></tr><tr><td>Battery</td><td>Durability, weight, and charging efficiency of battery</td><td>55.50 (55.50)</td><td>OS</td><td>Operation system and reliability</td><td>2.25 (3.75)</td></tr><tr><td>Camera</td><td>Camera and photo quality</td><td>17.75 (17.75)</td><td>Price</td><td>Price</td><td>8.75 (9.00)</td></tr><tr><td>Design</td><td>Design, quality, and material of outer casing</td><td>9.25 (11.25)</td><td>Reliability</td><td>Mobile phone&#x27;s reliability</td><td>24.75 (18.00)</td></tr><tr><td>Display</td><td>Display brightness and quality</td><td>4.75 (6.25)</td><td>Screen</td><td>Screen resolution and type</td><td>19.00 (19.25)</td></tr><tr><td>Easy to use</td><td>Easy to use</td><td>13.75 (16.50)</td><td>Appearance</td><td>Mobile phone&#x27;s size and shape</td><td>9.50 (11.50)</td></tr><tr><td>Navigation</td><td>GPS and navigation support</td><td>2.50 (2.75)</td><td>Software</td><td>Built-in software</td><td>5.00 (5.50)</td></tr><tr><td>Interface</td><td>Interface/inner equipment</td><td>16.25 (15.70)</td><td>Speed</td><td>Mobile phone&#x27;s response speed</td><td>10.25 (6.50)</td></tr><tr><td>Web browsing</td><td>Internet/web browsing</td><td>6.50 (4.75)</td><td>Voice</td><td>Voice quality and volume</td><td>8.75 (6.75)</td></tr><tr><td>Configuration</td><td>Memory/processor</td><td>6.25 (8.75)</td><td>Weight</td><td>Weight</td><td>5.25 (4.00)</td></tr><tr><td>Text support</td><td>Message/email/texting support</td><td>5.50 (5.75)</td><td>Wifi</td><td>Wifi support</td><td>1.75 (1.75)</td></tr><tr><td>Accessory</td><td>Mobile accessory</td><td>5.00 (3.25)</td><td>New functions</td><td>Video telephone, speech to text and other new functions</td><td>18.75 (19.50)</td></tr><tr><td>Service</td><td>After sales services</td><td>3.25 (7.75)</td><td></td><td></td><td></td></tr></table>

<sup>†</sup>Percentage of pros and cons in the two samples (i.e., 200 reviews) classified into this product feature by the product feature extraction procedure (Section 3.1).  
<sup>‡</sup>Percentage of pros and cons in the two samples classified into this product feature by the coders.

##

Table 4: Parameter Estimates of Different Empirical Models

<table><tr><td rowspan="2">Variable</td><td colspan="2">PRM</td><td colspan="2">NBRM</td><td colspan="2">BOCM</td><td colspan="2">MOCM</td></tr><tr><td>Estimate</td><td>Std. error</td><td>Estimate</td><td>Std. error</td><td>Estimate</td><td>Std. error</td><td>Estimate</td><td>Std. error</td></tr><tr><td>Intercept</td><td>1.346***</td><td>0.045</td><td>1.348***</td><td>0.046</td><td>1.533***</td><td>0.153</td><td>6.045***</td><td>0.886</td></tr><tr><td>Pro_Apps</td><td>0.042***</td><td>0.014</td><td>0.045***</td><td>0.016</td><td>0.170**</td><td>0.074</td><td>0.698*</td><td>0.407</td></tr><tr><td>Pro_Battery</td><td>0.043***</td><td>0.016</td><td>0.049***</td><td>0.017</td><td>0.177**</td><td>0.074</td><td>0.947**</td><td>0.396</td></tr><tr><td>Pro_Camera</td><td>0.034**</td><td>0.015</td><td>0.038**</td><td>0.019</td><td>0.146*</td><td>0.080</td><td>0.863*</td><td>0.464</td></tr><tr><td>Pro_Design</td><td>-0.021</td><td>0.016</td><td>-0.032</td><td>0.516</td><td>-0.108</td><td>0.072</td><td>-0.439</td><td>0.366</td></tr><tr><td>Pro_Display</td><td>-0.02</td><td>0.023</td><td>-0.023</td><td>0.123</td><td>-0.067</td><td>0.087</td><td>-0.265</td><td>0.391</td></tr><tr><td>Pro_Easy to use</td><td>0.076***</td><td>0.014</td><td>0.078***</td><td>0.019</td><td>0.231***</td><td>0.074</td><td>1.557***</td><td>0.488</td></tr><tr><td>Pro_New functions</td><td>0.075***</td><td>0.016</td><td>0.076***</td><td>0.021</td><td>0.297***</td><td>0.071</td><td>1.295***</td><td>0.387</td></tr><tr><td>Pro_Navigation</td><td>0.057**</td><td>0.023</td><td>0.061**</td><td>0.028</td><td>0.236**</td><td>0.117</td><td>1.094*</td><td>0.628</td></tr><tr><td>Pro_Interface</td><td>0.056***</td><td>0.019</td><td>0.060***</td><td>0.021</td><td>0.194***</td><td>0.074</td><td>0.882**</td><td>0.354</td></tr><tr><td>Pro_Web browsing</td><td>0.030*</td><td>0.017</td><td>0.032*</td><td>0.018</td><td>0.086</td><td>0.079</td><td>0.345</td><td>0.409</td></tr><tr><td>Pro_Configuration</td><td>0.0489***</td><td>0.019</td><td>0.053***</td><td>0.021</td><td>0.193**</td><td>0.093</td><td>1.289**</td><td>0.587</td></tr><tr><td>Pro_Text support</td><td>-0.009</td><td>0.022</td><td>-0.012</td><td>0.124</td><td>-0.062</td><td>0.085</td><td>-0.114</td><td>0.413</td></tr><tr><td>Pro_Accessary</td><td>-0.004</td><td>0.037</td><td>-0.006</td><td>0.069</td><td>-0.03</td><td>0.146</td><td>-0.191</td><td>0.726</td></tr><tr><td>Pro_Service</td><td>0.050</td><td>0.034</td><td>0.050</td><td>0.041</td><td>0.164</td><td>0.149</td><td>1.059</td><td>0.834</td></tr><tr><td>Pro_Multimedia</td><td>0.035**</td><td>0.017</td><td>0.035**</td><td>0.018</td><td>0.126</td><td>0.078</td><td>0.676*</td><td>0.411</td></tr><tr><td>Pro_OS</td><td>0.067***</td><td>0.019</td><td>0.071***</td><td>0.021</td><td>0.331***</td><td>0.113</td><td>1.340**</td><td>0.668</td></tr><tr><td>Pro_Price</td><td>-0.013</td><td>0.022</td><td>-0.013</td><td>0.029</td><td>-0.097</td><td>0.086</td><td>-0.451</td><td>0.421</td></tr><tr><td>Pro_Reliability</td><td>0.061***</td><td>0.016</td><td>0.068***</td><td>0.021</td><td>0.198***</td><td>0.073</td><td>0.930**</td><td>0.386</td></tr><tr><td>Pro_Screen</td><td>0.040**</td><td>0.017</td><td>0.040**</td><td>0.018</td><td>0.174**</td><td>0.077</td><td>0.861**</td><td>0.410</td></tr><tr><td>Pro_Appearance</td><td>0.036*</td><td>0.020</td><td>0.037*</td><td>0.021</td><td>0.168**</td><td>0.080</td><td>0.702*</td><td>0.399</td></tr><tr><td>Pro_Software</td><td>-0.001</td><td>0.019</td><td>-0.001</td><td>0.025</td><td>-0.016</td><td>0.084</td><td>0.142</td><td>0.424</td></tr></table>

##

<table><tr><td>Pro_Speed</td><td>0.106***</td><td>0.014</td><td>0.122***</td><td>0.019</td><td>0.491***</td><td>0.078</td><td>2.952***</td><td>0.641</td></tr><tr><td>Pro_Voice</td><td>0.015</td><td>0.018</td><td>0.015</td><td>0.018</td><td>0.065</td><td>0.077</td><td>0.431</td><td>0.376</td></tr><tr><td>Pro_Weight</td><td>0.043**</td><td>0.021</td><td>0.048**</td><td>0.023</td><td>0.189**</td><td>0.094</td><td>0.711</td><td>0.481</td></tr><tr><td>Pro_Wifi</td><td>0.087***</td><td>0.031</td><td>0.091***</td><td>0.034</td><td>0.358**</td><td>0.149</td><td>2.241**</td><td>0.945</td></tr><tr><td>Con_Apps</td><td>0.053***</td><td>0.020</td><td>0.079***</td><td>0.028</td><td>0.195*</td><td>0.111</td><td>1.142*</td><td>0.651</td></tr><tr><td>Con_battery</td><td>-0.035**</td><td>0.013</td><td>-0.037**</td><td>0.015</td><td>-0.210***</td><td>0.057</td><td>-0.889***</td><td>0.298</td></tr><tr><td>Con_Camera</td><td>0.022</td><td>0.017</td><td>0.022</td><td>0.048</td><td>0.022</td><td>0.077</td><td>0.454</td><td>0.417</td></tr><tr><td>Con_Design</td><td>-0.045</td><td>0.029</td><td>-0.045</td><td>0.069</td><td>-0.232**</td><td>0.103</td><td>-0.514</td><td>0.557</td></tr><tr><td>Con_Display</td><td>-0.031</td><td>0.060</td><td>-0.031</td><td>0.08</td><td>-0.311</td><td>0.309</td><td>-1.384</td><td>1.554</td></tr><tr><td>Con_Easyto use</td><td>-0.054***</td><td>0.021</td><td>-0.079***</td><td>0.029</td><td>-0.156**</td><td>0.070</td><td>-0.938***</td><td>0.327</td></tr><tr><td>Con_New functions</td><td>-0.058***</td><td>0.022</td><td>-0.083***</td><td>0.031</td><td>-0.240***</td><td>0.079</td><td>-1.360***</td><td>0.389</td></tr><tr><td>Con_Navigation</td><td>-0.087</td><td>0.066</td><td>-0.087</td><td>0.166</td><td>-0.278</td><td>0.207</td><td>-1.071</td><td>0.880</td></tr><tr><td>Con_Interface</td><td>-0.025</td><td>0.016</td><td>-0.025</td><td>0.086</td><td>-0.107*</td><td>0.061</td><td>-0.528*</td><td>0.285</td></tr><tr><td>Con_Web browsing</td><td>0.009</td><td>0.026</td><td>0.009</td><td>0.126</td><td>-0.029</td><td>0.113</td><td>-0.175</td><td>0.554</td></tr><tr><td>Con_Configuration</td><td>-0.003</td><td>0.023</td><td>-0.003</td><td>0.068</td><td>-0.070</td><td>0.104</td><td>-0.181</td><td>0.533</td></tr><tr><td>Con_Text support</td><td>-0.106***</td><td>0.033</td><td>-0.146***</td><td>0.038</td><td>-0.359***</td><td>0.117</td><td>-1.78***</td><td>0.577</td></tr><tr><td>Con_Accessary</td><td>0.021</td><td>0.028</td><td>0.023</td><td>0.126</td><td>0.111</td><td>0.134</td><td>0.547</td><td>0.657</td></tr><tr><td>Con_Service</td><td>0.022</td><td>0.025</td><td>0.024</td><td>0.167</td><td>0.110</td><td>0.106</td><td>0.308</td><td>0.488</td></tr><tr><td>Con_Multimedia</td><td>-0.007</td><td>0.026</td><td>-0.087</td><td>0.226</td><td>-0.031</td><td>0.117</td><td>-0.518</td><td>0.532</td></tr><tr><td>Con_OS</td><td>-0.033</td><td>0.040</td><td>-0.035</td><td>0.15</td><td>-0.149</td><td>0.152</td><td>-0.661</td><td>0.713</td></tr><tr><td>Con_Price</td><td>-0.004</td><td>0.020</td><td>-0.004</td><td>0.19</td><td>-0.019</td><td>0.092</td><td>-0.028</td><td>0.447</td></tr><tr><td>Con_Reliability</td><td>-0.091***</td><td>0.013</td><td>-0.121***</td><td>0.019</td><td>-0.365***</td><td>0.052</td><td>-1.799***</td><td>0.332</td></tr><tr><td>Con_Screen</td><td>-0.050***</td><td>0.017</td><td>-0.075***</td><td>0.021</td><td>-0.227***</td><td>0.068</td><td>-1.065***</td><td>0.357</td></tr><tr><td>Con_Apperance</td><td>0.049**</td><td>0.023</td><td>0.050**</td><td>0.024</td><td>0.186</td><td>0.132</td><td>0.986</td><td>0.860</td></tr><tr><td>Con_Software</td><td>-0.046</td><td>0.029</td><td>-0.043</td><td>0.031</td><td>-0.179*</td><td>0.100</td><td>-0.759*</td><td>0.452</td></tr><tr><td>Con_Speed</td><td>-0.121***</td><td>0.027</td><td>-0.141***</td><td>0.03</td><td>-0.471***</td><td>0.092</td><td>-1.778***</td><td>0.497</td></tr><tr><td>Con_Voice</td><td>-0.026</td><td>0.024</td><td>-0.026</td><td>0.037</td><td>-0.154*</td><td>0.091</td><td>-0.767*</td><td>0.437</td></tr><tr><td>Con_Weight</td><td>0.009</td><td>0.046</td><td>0.007</td><td>0.049</td><td>0.019</td><td>0.225</td><td>0.311</td><td>1.494</td></tr></table>

##

<table><tr><td>Con_Wifi</td><td>0.022</td><td>0.035</td><td>0.025</td><td>0.612</td><td>0.034</td><td>0.179</td><td>-0.108</td><td>0.896</td></tr><tr><td>Brand 1</td><td>0.074</td><td>0.046</td><td>0.094</td><td>0.546</td><td>0.435***</td><td>0.162</td><td>2.213***</td><td>0.772</td></tr><tr><td>Brand 2</td><td>-0.035</td><td>0.047</td><td>-0.043</td><td>0.147</td><td>-0.080</td><td>0.157</td><td>-0.285</td><td>0.667</td></tr><tr><td>Brand 3</td><td>-0.009</td><td>0.050</td><td>-0.009</td><td>0.15</td><td>0.002</td><td>0.182</td><td>-0.184</td><td>0.812</td></tr><tr><td>Brand 4</td><td>-0.111**</td><td>0.052</td><td>-0.113**</td><td>0.054</td><td>-0.358**</td><td>0.175</td><td>-1.490*</td><td>0.777</td></tr><tr><td>Brand 5</td><td>-0.213***</td><td>0.053</td><td>-0.263***</td><td>0.069</td><td>-0.613***</td><td>0.171</td><td>-2.506***</td><td>0.778</td></tr><tr><td>Brand 6</td><td>0.053</td><td>0.046</td><td>0.053</td><td>0.176</td><td>0.231</td><td>0.164</td><td>1.009</td><td>0.726</td></tr><tr><td>Brand 7</td><td>-0.018</td><td>0.057</td><td>-0.018</td><td>0.527</td><td>0.007</td><td>0.196</td><td>-0.070</td><td>0.827</td></tr><tr><td>Brand 8</td><td>0.064</td><td>0.045</td><td>0.074</td><td>0.845</td><td>0.241</td><td>0.160</td><td>1.308*</td><td>0.737</td></tr><tr><td>Brand 9</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>NORRW</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-0.014*</td><td>0.024</td></tr><tr><td>NORPR</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.040***</td><td>0.014</td></tr><tr><td>Log-Likelihood</td><td>-4313.61</td><td></td><td>-4128.53</td><td></td><td>-2986.90</td><td></td><td>-2961.10</td><td></td></tr><tr><td>Akaike Information Criterion</td><td>8745.20</td><td></td><td>8375.06</td><td></td><td>6097.80</td><td></td><td>6066.20</td><td></td></tr></table>

\*\*\*p<0.001; \*\*p<0.01; \*p<0.05.

#

Shengsheng Xiao is Ph.D. candidate in Antai College of Economics & Management, Shanghai Jiao Tong University. He received his Master degree in Management Information Systems from Shanghai University of Finance and Economics. His research deals with trust issues in social networks, and economics of user generated content.

![](/api/attachments/ZSE5RAQB/fulltext/images/8dd8d3eff968bb9163ad6d2ef1f3582810ee9897afd36c2af737378b91c19fe7.jpg)

Chih-Ping Wei received a BS in Management Science from the National Chiao-Tung University in Taiwan, R.O.C. in 1987 and an MS and a Ph.D. in Management Information Systems from the University of Arizona in 1991 and 1996. He is currently a professor of Department of Information Management at National Taiwan University, Taiwan, R.O.C. Prior to joining National Taiwan University in 2010, he was a professor at National Tsing Hua University and National Sun Yat-sen University in Taiwan and a visiting scholar at the University of Illinois at Urbana-Champaign (Fall 2001), the Chinese University of Hong Kong (Summer 2006 and 2007), and the University of Washington (Fall 2013). His papers have appeared in Journal of Management Information Systems (JMIS), European Journal of Information Systems, Decision Sciences, Decision Support Systems, IEEE Transactions on Engineering Management, IEEE Software, IEEE Intelligent Systems, IEEE Transactions on Systems, Man, and Cybernetics, IEEE Transactions on Information Technology in Biomedicine, Journal of the American Society for Information Science and Technology, Information Processing and Management, Journal of Database Management, and Journal of Organizational Computing and Electronic Commerce, etc. His current research interests include data analytics, text mining and information retrieval, knowledge management, patent analysis and intelligence, and health informatics. Chih-Ping Wei can be reached at the Department of Information Management, National Taiwan University, Taipei, Taiwan, R.O.C; cpwei@im.ntu.edu.tw.

Ming Dong is Professor in the Department of Operations Management, Antai College of Economics & Management, Shanghai Jiao Tong University. He received the M.S. and Ph.D. degrees from Tianjin University, Tianjin, China, respectively, all in mechanical engineering, and the Ph.D. degree in industrial engineering from Virginia Polytechnic Institute and State University. His research and teaching interests are in the areas of decision support, operations management and production optimization.
