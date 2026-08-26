---
otero_id: 5024
otero_key: "HF6HQ4MT"
title: "Disconfirmation Effect on Online Rating Behavior: A Structural Model"
authors: "Yi-Chun (Chad) Ho; Junjie Wu; Yong Tan"
year: "2017"
journal: "Information Systems Research"
doi: "10.1287/isre.2017.0694"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## rmationSystems Research

![](/api/attachments/HF6HQ4MT/fulltext/images/f43c5c623807655d5b7bee38d24fcfe0ba1475587990b11ecb82d7625f53d044.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Disconfirmation Effect on Online Rating Behavior: A Structural Model

Yi-Chun (Chad) Ho, Junjie Wu, Yong Tan

Yi-Chun (Chad) Ho, Junjie Wu, Yong Tan (2017) Disconfirmation Effect on Online Rating Behavior: A Structural Model. Information Systems Research

Published online in Articles in Advance 03 Jul 2017

https://doi.org/10.1287/isre.2017.0694

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2017, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/HF6HQ4MT/fulltext/images/2d35437bc5aad21619a7a85e11d213b4732509a1ecf964f80596cde5ab05729a.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Disconfirmation Efect on Online Rating Behavior: A Structural Model

Yi-Chun (Chad) Ho,<sup>a</sup> Junjie Wu,<sup>b,∗</sup> Yong Tan<sup>c,</sup> <sup>d</sup>

<sup>a</sup> School of Business, George Washington University, Washington, DC 20052; <sup>b</sup> School of Economics and Management, Beihang University, 100191 Beĳing, China; <sup>c</sup> Michael G. Foster School of Business, University of Washington, Seattle, Washington 98195; <sup>d</sup> School of Economics and Management, Tsinghua University, 100084 Beĳing, China

<sup>∗</sup> Corresponding author

Contact: chadho@gwu.edu (Y-C(C)H); wujj@buaa.edu.cn (JW); ytan@uw.edu (YT)

Received: October 25, 2014 Revised: February 6, 2016; September 23, 2016; October 31, 2016 Accepted: November 2, 2016 Published Online in Articles in Advance: July 3, 2017

https://doi.org/10.1287/isre.2017.0694

Copyright: © 2017 INFORMS

Abstract. This research studies the efect of disconfirmation—the discrepancy between the expected and experienced assessment of the same product—on the behavior of consumers leaving online product reviews. We propose a modeling framework in which an individual’s prepurchase expectation is shaped by (1) the product ratings she observes and (2) the perception of the review system she has at the time of the purchase. Upon product consumption, the individual obtains the postpurchase evaluation and encounters a certain level of disconfirmation. Drawing on the Bayesian learning framework, we model individual perception of the review system as a subjective attitude underlying how well the aggregate ratings match one’s own usage experience. A hierarchical Bayesian model is developed and estimated using a rich data set comprising complete purchasing and rating activities on an e-commerce website. Our results suggest that an individual’s decisions of whether to post a rating and what rating to post are afected by disconfirmation in two distinct manners. Specifically, an individual is more likely to leave a review when the magnitude of disconfirmation she encounters is larger. In addition, when the individual decides to review a product, the rating she chooses may not neutrally reflect her postpurchase evaluation; the direction of such a bias is in accordance with the sign of disconfirmation. We also observe several moderating efects: the disconfirmation efect on posting is attenuated by the time gap between purchase and receipt of the same product but accentuated by the dissension in product evaluations among peer consumers. A more granular examination reveals that infrequent raters are systematically more susceptible to disconfirmation than frequent posters. The insights from this research lead to actionable strategies for marketers and designers of recommender systems.

History: Sanjeev Dewan, Senior Editor; Bin Gu, Associate Editor.

Funding: Junjie Wu acknowledges the financial support from the National Science Foundation of China [Grants 71322104, 71531001, 71490723, and 71471009], National High Technology Research and Development Program of China [Grant SS2014AA012303], National Center for International Joint Research on E-Business Information Processing [Grant 2013B01035], and Fundamental Research Funds for the Central Universities. Yong Tan is supported in part by the National Science Foundation of China [Grant 71490723].

Keywords: disconfirmation • online reviews • rating bias • user-generated content • word of mouth • learning models • hierarchical Bayes • Bayesian estimation

## 1. Introduction

It has been well recognized that online customer reviews and ratings<sup>1</sup> have a substantial impact on consumer purchasing decisions. According to surveys, 82% of respondents agree that online reviews directly influence their decisions on what product to buy (MarketingCharts 2007), and over 75% of them consider recommendations from those who have experienced the product the most credible information source (Nielson 2007). By observing the usage experiences shared by peer consumers, prospective buyers can reduce product uncertainty and make more informed purchases, leading to higher satisfaction and lower merchandise return rates. As a result, the prevalence of online reviews enhances the information transparency and improves the eficiency of the digital marketplace.

There is growing evidence that companies intend to manipulate online customer reviews for targeted products and services (Gormley 2013). Some boost the image of their own brand or merchandise by posting deceptive positive evaluations, whereas others undermine those of the competitors’ by making up negative usage experiences, or both. Such unethical practices cast serious doubt on the trustworthiness of customer-reported ratings and jeopardize the credibility of the review system as perceived by consumers (Taylor 2014).

The objective of this research is to examine whether the behavior of consumers leaving online product reviews is afected by disconfirmation—the discrepancy between the prepurchase expectation and postpurchase evaluation of the same product. We propose a modeling framework for estimating and understanding the efect of disconfirmation on online rating behavior based on observational data. The proposed framework is novel in the following two aspects. First, we examine the online rating behavior by looking at the activities involved before and after a purchase. An online review platform is an information system that facilitates information exchange among its users. System users can be categorized into two groups based on how they interact with the system. The first type of user is the review reader (information receiver), who gathers information about peer consumers’ usage experience stored in various formats, such as numeric ratings, textual reviews, multimedia files, etc. After consuming the product herself, a review reader has an opportunity to become a review poster (information provider), the second role a user can play, by sharing her own assessment on the product. It has been shown that when making rating decisions, a focal individual tends to first observe the opinions expressed by others and then adjusts her own feedback accordingly (Moe and Schweidel 2012, Schlosser 2005). In terms of timing, prior research commonly assumes that the ratings posted by others will afect a focal individual’s rating decision only after a purchase, without considering an important fact that review posters are often review readers. Motivated by the dual role a review system user can play, we postulate that the influence of existing ratings may take place when the focal individual accesses the review information before the purchase.

The second novelty of this research is that we consider that individuals may not perceive the review system to be truly trustful. We consider that an individual holds a perception of the review system, a subjective attitude underlying how the rating signal of the system can predict one’s own usage experience. In particular, we model individual perception of the review system as two distinct yet interrelated components: system biasedness and system precision. Prior to the purchase, a consumer formulates the prepurchase expectation of the product based on the posted ratings, taking into account her own perception of the review system at the time. Upon product consumption, she obtains the postpurchase evaluation of the same product and encounters a certain level of disconfirmation. The realization of disconfirmation is then used by the consumer to update her perception toward the system over time. Such a consumer response is especially realistic after the outbreak of firms’ strategic manipulation in online rating environments.

Unlike prior work that study the formation of online ratings from a static point of view, this research examines consumer rating behavior from a dynamic perspective. We extend the Bayesian learning framework, flexibly allowing individual perception of the system to change over time and dynamically incorporating this time-variant component into raters’ decision-making process. The proposed model is applied to a unique data set consisting of consumer purchase histories and review entries on an e-commerce website. Utilizing these complete activity logs, we can discern whether a consumer left a review for the product she purchased earlier. In addition, the lengthy panel enables us to calibrate how consumer rating behavior changes over time under a dynamic learning mechanism.

This research also contributes to the broad literature on factors that encourage or discourage consumer rating behavior. Our estimation results show that an individual’s decision of whether to contribute a review and her decision of what rating number to give are both influenced by disconfirmation—the discrepancy between one’s expected and experienced quality of the same product. In particular, the relationship between posting propensity and disconfirmation is best described by a nonlinear U-shaped curve, meaning that a consumer’s marginal probability of posting increases as her postpurchase evaluation further deviates from the prepurchase expectation. Similar to consumers who use traditional channels (Anderson and Sullivan 1993), we find that online shoppers also factor in disconfirmation they encounter when giving product ratings. A further examination at the individual level reveals that occasional raters are more susceptible to disconfirmation when making the decision of whether to review a product. This finding has important managerial implications since the ratings posted by occasional raters appear to be more biased than those by frequent posters.

The rest of this paper is organized as follows. In Section 2, we review the relevant literature and diferentiate our work from others. Section 3 describes the data and provides a preliminary descriptive analysis on observed consumer rating decisions. Our empirical model is specified in detail in Section 4. Section 5 presents our estimation strategy, identification strategy, and model comparison. In Section 6, we present our estimation results and discuss the associated insights, followed by robustness checks and useful managerial implications for various practitioners. Concluding remarks and future research directions are provided in Section 7.

## 2. Relevant Literature

There is an emerging literature stream examining how existing reviews afect subsequent rating behavior after the consumption of a product. In a lab setting,

Schlosser (2005) observed self-presentational behavior in which a review poster strategically adjusted her product evaluation downward after observing negative opinions by others, perhaps to present herself as more intelligent. She also found that a rater would make her opinions more balanced when there was high dissension among opinions from the crowd. Li and Hitt (2008) argue that the predominant declining trend of book ratings is attributable to consumers’ self-selection bias, meaning that early buyers tend to have higher perceived quality, leading to better book ratings, than later buyers. Using reviews posted on the site of an online retailer of bath, fragrance, and home products, Moe and Schweidel (2012) show that rater behavior is influenced by the rating environments where they are exposed. In particular, consumers are subject to the selection efect, as they are more prone to share their experience when the existing ratings have high valance and high volume. In addition, Moe and Schweidel (2012) also find dissimilar adjustment efects among posters as activists are more negative and exhibit diferentiation behavior. On a social media– like review site, Lee et al. (2015) investigate any differential impact of prior ratings by strangers versus friends on a focal individual’s opinions. They conclude that friends’ opinions always induce herding, and the presence of social networking dampens the impact of opinions from the crowd. Although past researchers have shown that posted reviews can influence one’s product opinions after the purchase, many of them do not consider the impact of review information on the formulation of such opinions in the prepurchase stage. Our study attempts to fill this gap through the lens of the expectation–confirmation paradigm.

Disconfirmation, or, formally, expectation–disconfirmation theory (EDT) (Oliver 1977, 1980), has long been applied to studying satisfaction in both marketing and information systems literature. Much of the prior research has shown that overall satisfaction is afected by disconfirmation in diferent fields such as retailing (Anderson and Sullivan 1993), telecommunication (Bolton and Drew 1991), information technology usage (Bhattacherjee 2001), online travel agents (McKinney et al. 2002), and application service providers (Susarla et al. 2003). On the other hand, there is another literature stream that adopts EDT to better understand the role of disconfirmation on various postsale reactions. For example, disconfirmation has been demonstrated to have a significant impact on repurchase intentions (Anderson and Sullivan 1993), postsale complaints (Bearden and Teel 1983), continued use of information systems (Bhattacherjee 2001), and so on. This research contributes to the related literature in the following three aspects. First, whereas the relationship between disconfirmation and satisfaction has been well established, research to date has not explicitly examined the impact of disconfirmation on the consumer decision of whether or not to share such satisfaction. Second, by utilizing observational data, we are able to further explore factors that moderate the disconfirmation efect on posting. Third, unlike most prior work that study disconfirmation based on correlational techniques, this paper is, to our knowledge, one of the first few to model the influence of disconfirmation in a dynamic and structural way. By utilizing a hierarchical Bayes approach, we can identify and discern dissimilar levels of the disconfirmation efect across diferent types of individuals.

This work is also related to research that studies why individuals engage in postpurchase word of mouth (WOM). Using survey data, early researchers examined this question from a motivational point of view. Dichter (1966), in his seminal paper, suggests four motivations for traditional WOM communication: product, self-, other, and message involvement. Sundaram et al. (1998) expand the number of motivations behind WOM to eight and classify them into two main categories. They argue that altruism, product involvement, self-enhancement, and helping the company are four main factors leading to positive WOM, whereas consumers spread negative WOM usually for altruism, anxiety reduction, vengeance, and adviceseeking purposes. With a similar approach, Hennig-Thurau et al. (2004) identify a similar set of eight motivations—perform assistance, vent negative feelings, concern for others/altruism, extraversion, social benefits, economic incentives, help the company, and advice seeking—as the primary motivations for consumers sharing their usage experiences on the Internet. Although we attempt to answer a similar question from a diferent (nonmotivational) perspective, the disconfirmation efect identified in this paper can still be used to explain some, if not all, motivations such as anxiety/dissonance reduction, vengeance, and concerns for others/altruism.

An extensive literature using quantitative methods has also been developed to identify what drives consumers to share their product or service experiences in the absence of monetary reward mechanisms. Dellarocas et al. (2004) examine rating behavior on an electronic trading platform. They find that such voluntary behavior is driven by the expectation of reciprocal behavior, meaning that a trader evaluates her trading partner to solicit feedback from the other party. Shen et al. (2015) look at review posting behavior from a strategic perspective. Using book review data from online book sellers, they argue that online reviewers are more prone to rate popular but less crowded books to gain attention and to reduce competition for attention at the same time. They also conclude that reviewers with high reputation costs are more likely to adopt an imitation strategy by posting ratings conforming to the consensus of a community. Factors afecting the level of WOM have also been studied at the population level. Rather than taking the common conception of the level of WOM activity as a monotonic function of customer satisfaction, Anderson (1998) discovers that the relationship between them exhibits a U-shaped pattern—customers are more likely to engage in WOM when they are either extremely satisfied or dissatisfied with the product. Using data from a movie website, Dellarocas and Narayan (2006) also identify a similar association between observed rating density and perceived movie quality. Along these lines, Dellarocas et al. (2010) further suggest that moviegoers are more prone to post reviews for the most or least popular movies measured by box ofice revenue.

Research studying consumer rating behavior naturally leads to another stream of literature, which examines whether customer reviews can represent true product quality. This particular literature stream can be further classified into two categories, depending on whether publicly available reviews are entirely generated by consumers or partially manipulated by firms. Following the notion that online ratings are truthful, Hu et al. (2006) discuss whether the mean of posted ratings can represent true product quality. In particular, they develop an analytical model assuming that a consumer will post a review only when the level of her satisfaction is either above or below a “brag-andmoan” interval; she will otherwise be silent. Based on this assumption, they show that the average rating can serve as an unbiased signal if and only if two bounds of the interval are equal or symmetrically deviate from the true quality. On the other hand, Dellarocas (2006) assumes that the observed ratings may not be fully trustful and could be strategically boosted by firms. He demonstrates that inflated reviews are still informative since the firm producing high-quality products benefits the most through such manipulation.

In terms of research context and methodology, our work is most closely related to Moe and Schweidel (2012) (henceforth, MS). We develop our model based on MS, which, in turn, is a generalization of Ying et al. (2006), who first proposed that whether a product is rated should afect the analyst’s prediction of that rating. Despite some similarities, this paper differs from MS in many aspects. First, our focus is to study how quality disconfirmation and individual perception of the review system afect reviewposting decisions, while that of MS is to examine whether online raters will adjust their opinions according to opinions expressed by others. Second, we extend a dynamic learning framework, flexibly allowing an individual’s perception of the system to change over time and dynamically linking this perception to her rating decisions. By contrast, MS use a static model in which posting decisions are treated as independent and uncorrelated with each other. Finally, we are able to directly observe from our data set whether a consumer leaves a review for a product she purchased previously, whereas the purchase data are missing in MS. Our lengthy panel also allows us to construct a richer model to investigate why consumer rating behavior changes over time.

This paper attempts to close the gap in the online review literature by studying the relationship between posted reviews and subsequent ones from a diferent perspective. Specifically, we postulate that the impact of existing ratings may occur when an individual accesses review information for purchasing decisions (in the prepurchase stage), well before she faces the rating decisions (in the postpurchase stage). We also consider that individuals may perceive the review system not to be truly trustful, by modeling the evolution of individual perception of the review system over time and how such a perception afects one’s posting decisions in a dynamic fashion. While the perception of an information source has been examined in diferent applications such as how it determines the persuasiveness of communication (Chaiken 1980), the way in which individual perception impacts consumer interaction with information systems (as review readers and posters) still remains unstudied.

## 3. Data and Descriptive Analysis

The data for this study were provided by an online e-commerce website similar to Amazon. Per the information available on its home page, the site groups products into the following 10 major categories: electronics; computers and ofice supplies; home, kitchen, and tools; appliances; beauty and health; clothing, shoes, and bags; watches and jewelry; food; automotive; and books and music. The data set contains complete purchase histories and review entries made by 1,000 randomly selected individuals. The data well represent the purchasing and rating behavior of online shoppers typically observed on a mainstream e-commerce site.

The purchase record set consists of detailed order information such as the product name, price, shipping and handling time, and order placement date. The rating data set records customer-reported reviews in a typical format, including a review title, a review body, a submission date, and an overall product rating on a discrete five-star scale, with five being the best. The data span from March 2006 to November 2011. During this period of time, the site did not implement any marketing campaigns or system design that could have influenced consumer rating behavior. Submission of product reviews is voluntary and self-driven. To identify consumer rating behavior at the individual level, we exclude nonraters, who never left a review.<sup>2</sup> The resulting data set comprises 361 panelists who purchased 37,209 items and contributed 2,257 reviews.

Table 1. Descriptive Statistics of Main Variables

<table><tr><td>Notation</td><td>Description</td><td>Mean</td><td>Std. dev.</td><td>Min.</td><td>Max.</td></tr><tr><td> $y_{ijt}$ </td><td>A dummy indicating if a consumer leaves a product review</td><td>0.061</td><td>0.239</td><td>0</td><td>1</td></tr><tr><td> $z_{ijt}$ </td><td>Observed rating scores</td><td>3.826</td><td>1.200</td><td>1</td><td>5</td></tr><tr><td> $p_{ijt}$ </td><td>Product prices</td><td>50.208</td><td>200.170</td><td>0.440</td><td>13,674</td></tr><tr><td> $h_{ijt}$ </td><td>Shipping and handling time (days)</td><td>2.328</td><td>3.674</td><td>0</td><td>142</td></tr><tr><td> $\bar{R}_{ijt}$ </td><td>Valence of existing ratings</td><td>4.015</td><td>0.621</td><td>1</td><td>5</td></tr><tr><td> $Vol_{ijt}$ </td><td>Volume of existing ratings</td><td>58.357</td><td>186.776</td><td>2</td><td>3,587</td></tr><tr><td> $Var_{ijt}$ </td><td>Variance of existing ratings</td><td>0.817</td><td>0.652</td><td>0</td><td>4</td></tr></table>

A cross-check indicates that the 361 raters and remaining nonraters exhibit similar purchase behavior with respect to both revenue generation and items purchased.<sup>3</sup> In January 2016, we also collected the mean ratings for all products appearing in our data to supplement the main data.

Two aspects of our data set are unique. First, from the complete logs of purchasing and rating activities, we can observe whether a consumer left a review for the product she purchased earlier (posting versus lurking). Second, by leveraging the time stamps of all activities on the website, we are able to recover the rating information (characterized by the valence, volume, and variance of posted ratings) available to a consumer upon purchase. It is worth noting that our data were collected at the micro (individual) level. This nature distinguishes our work from others that commonly use review data at the aggregate (product) level.

Before introducing our empirical model, we briefly present a preliminary descriptive data analysis. Table 1 reports the descriptive statistics of variables from our final data set. At the population level, the review posting rate is around $6 \% ,$ , and the mean of all observed ratings is 3.83. The consumer rating behavior on the e-commerce website is presented in Figures 1 and 2. Figure 1 plots the frequency of five discrete ratings. The distribution roughly follows a J shape, which is commonly found across various rating platforms (McGlohon et al. 2010). This unique pattern is consistent with the results found by Anderson (1998), who argues that consumers are more prone to express opinions about products when their experiences are either terrific (represented by a high score of 4 or 5) or terrible (represented by a low score of 1 or 2). To understand the association between the rating by a focal consumer (a focal rating) and the mean of previously posted ratings by peer consumers, we calculate the observed “rating discrepancy” $( z _ { i j t } - \bar { R } _ { i j t } )$ for all rated occasions $( y _ { i j t } = 1 )$ . From Figure 2, we see that a majority of posted ratings do not deviate too much from the mean scores observed at the times of purchase. In particular, nearly two-thirds of them have an absolute rating discrepancy less than one. Yet, based on this data pattern, can we argue that online raters are more vocal when they concur with the consensus from the crowd? This is the main question we attempt to answer in this study.

Figure 1. Distribution of Posted Rating  
![](/api/attachments/HF6HQ4MT/fulltext/images/3e1f274144d1b6a45d518a6c1adbc8ffe8b7ba054aafc4a2ccccfab5e21c0eba.jpg)

Figure 2. Distribution of Rating Discrepancy  
![](/api/attachments/HF6HQ4MT/fulltext/images/b1905d149ec3a7d652cc977991cbdcf8755ce5d545f3a3761e826eed140a7714.jpg)

## 4. Model

We develop our empirical model to study the dynamics of consumer rating behavior at the individual level. The general modeling context is that individuals undergo the following five steps during the entire purchasing– rating process (Figure 3). Before a consumer purchases a product, she faces uncertainty about the product quality and formulates her prepurchase expectation based on the posted ratings she observes and the review system she perceives at that time (Step 1). Upon consumption, she obtains the postpurchase evaluation of the same product (Step 2) and experiences a certain level of disconfirmation (Step 3). She then uses this private information to update her own perception of the system (Step 4). With the realized disconfirmation

Figure 3. Conceptual Framework of the Online Rating Behavior  
![](/api/attachments/HF6HQ4MT/fulltext/images/3d13af153755ae1345330eb4f362b77b2add4df9c0e35baf2aa89b8bf928b85a.jpg)  
and her updated perception, the consumer faces two product-reviewing decisions, with the first decision being whether to leave a review and the second decision being what rating to leave (Step 5). The proposed model is presented in the following order: (1) formulation of disconfirmation; (2) updating of consumer perception of the review system; (3) consumer decisions of leaving product ratings; and (4) interdependence between the two rating decisions.

## 4.1. Formulation of Disconfirmation

Prepurchase Expectation. Consider an individual i who is about to purchase product j at occasion t. In our research context, the e-commerce website displays the aggregate statistics of customer self-reported ratings (e.g., the mean and the distribution) on the top of a product’s landing page, and we assume that prospective consumers access such information before making a purchase. In the prepurchase stage, the consumer formulates an expected assessment of the product as the true quality is uncertain to her. Following Rust et al. (1999), we view consumer expectation as a distribution that describes the likelihood of a given quality outcome being realized upon consumption. While the aggregate rating statistics provide objective information about quality, how the rating signal is interpreted by each individual could be subjective. To account for this heterogeneity, we assume that individual i’s prepurchase expectation, $\hat { Q } _ { i j t } ^ { }$ , for j at occasion t follows a normal distribution

$$
\hat {Q} _ {i j t} \sim N (\bar {R} _ {j t} - \delta_ {i, t - 1}, (\mathrm{T} _ {j t} \cdot \tau_ {i, t - 1}) ^ {- 1}),\tag{1}
$$

where $\bar { R } _ { j t }$ and $\mathrm { T } _ { j t }$ denote the mean and the precision of all ratings product j has received prior to the time of purchase, respectively.<sup>4</sup> These two pieces of information together characterize the rating signal for j available to individual i at occasion t. We model that consumer perception of the review system consists of two individual-specific parameters: system biasedness $( \delta _ { i \cdot } )$ and system precision $( \tau _ { i \cdot } )$ . The updating of such perception occurs when the disconfirmation is realized after the product consumption. It should be clear that one’s ex ante expectation, formulated right before the purchase, is influenced by the perception she has updated since the previous purchase occasion t <sup>−</sup> 1. The system biasedness $\delta _ { i \cdot }$ measures how biased the review system is perceived to be by individual i. When $\delta _ { i \cdot } = 0 ,$ , individual i perceives the system to be neutral and therefore believes that $\bar { R } _ { j t }$ provides an unbiased signal about the product quality. In this case, individual i formulates an expectation centered on ${ \bar { R } _ { j t } } .$ . The sign of $\delta _ { i }$ · indicates the direction of the perceived system biasedness. When $\delta _ { i \cdot } > 0 \ ( \delta _ { i \cdot } < 0 )$ , the individual believes that $\bar { R } _ { j t }$ overrepresents (underrepresents) the product quality; as a result, she will adjust the mean of her expectation downward (upward) to ofset the perceived biasedness. The system precision $\tau _ { i \cdot }$ · measures how precise the system is perceived to be by i. When $\tau _ { i t }$ is large (small), individual i perceives the review system to be precise (noisy) such that her expectation will be tightly (loosely) centered on its mean.

Postpurchase Evaluation. One of the most challenging modeling tasks is to model the baseline quality of the products. A convenient and widely accepted approach is to assume that the latent quality is drawn from a zero-mean normal distribution (Moe and Schweidel 2012). To better utilize the publicly available information, we first collect the long-term average rating, ${ \tilde { R } } _ { j } ,$ for all products. While we believe that ${ \tilde { R } } _ { j }$ has “some” information about the quality of product $j ,$ this rating signal may not necessarily reflect the overall evaluation among all consumers. For example, Hu et al. (2006) argue that the mean ratings could overreport (underreport) the true quality if consumers are more inclined to brag (moan) about the product when they are highly satisfied (disgruntled). To address this issue, we assume that the individual $i ,$ upon consumption of j, acquires her postpurchase evaluation

$$
Q _ {i j} = (\tilde {R} _ {j} + \bar {\omega} _ {j}) + \lambda_ {i 0},\tag{2}
$$

where $\varpi _ { j }$ is a product-level random efect and $\lambda _ { i 0 }$ is an individual-level random efect that allows for variation in product evaluation across individuals. We assume $\bar { \varpi _ { j } } \sim N ( \bar { \varpi } , \sigma _ { \varpi } ^ { 2 } )$ and model $\varpi _ { j }$ as the diference between ${ \tilde { R } } _ { j }$ and the latent quality in a random manner. In other words, if ${ \tilde { R } } _ { i }$ overrepresents (underrepresents) the true quality of product $j ,$ then the associated $\varpi _ { j }$ will be negative (positive). The mean parameter $\bar { \varpi }$ measures whether $\tilde { R } _ { j } ^ { \prime }$ s systematically deviate from the true quality, whereas the variance parameter $\sigma _ { \varpi } ^ { 2 }$ measures the degree of variation in such diferences.

Disconfirmation. Having developed consumer expectation and evaluation of the same product, we are now able to formally define the disconfirmation. We model disconfirmation as how far individual i’s ex post evaluation deviates from her ex ante expectation obtained from the same product

$$
\Delta Q _ {i j t} \equiv Q _ {i j} - \hat {Q} _ {i j t}.\tag{3}
$$

Plugging (1) and (2) into (3), we have

$$
\Delta Q _ {i j t} \sim N (\Delta \bar {Q} _ {i j t}, (\mathrm{T} _ {j t} \cdot \tau_ {i, t - 1}) ^ {- 1}),\tag{4}
$$

$$
\Delta \bar {Q} _ {i j t} = (\tilde {R} _ {j} + \varpi_ {j} + \lambda_ {i 0}) - (\bar {R} _ {j t} - \delta_ {i, t - 1}).\tag{5}
$$

When $\Delta \bar { Q } _ { i j t } > 0$ , we say that the consumer encounters a positive disconfirmation, meaning that her experienced product evaluation is greater than the expectation.

## 4.2. Updating of Individual Perception of the Review System

We explain how the individual perception of the system evolves over time. We assume that, before experiencing the product, individual i has prior beliefs of $\delta _ { i , t - 1 } \mid \tau _ { i , t - 1 }$ and $\tau _ { i , t - 1 } ,$ which jointly follow a normalgamma distribution<sup>5</sup>

$$
\delta_ {i, t - 1} \mid \tau_ {i, t - 1} \sim N (\bar {\delta} _ {i, t - 1}, (\gamma_ {i, t - 1} \cdot \tilde {\tau}) ^ {- 1}),\tag{6}
$$

$$
\tau_ {i, t - 1} \sim \Gamma (a _ {i, t - 1}, b _ {i, t - 1}),\tag{7}
$$

where $\gamma _ { i \cdot }$ is the precision parameter of a normal distribution, τ˜ is a time-invariant constant, $a _ { i \cdot }$ is the shape parameter, and $b _ { i \cdot }$ is the inverse scale parameter of a gamma distribution. After experiencing the product, the individual encounters a certain level of disconfirmation and uses this private information to update her perception of the system. As a result, such perception will dynamically change as she receives more disconfirmation signals over time. According to Bayes’ rule, individual $i ^ { \prime } \mathrm { s }$ posterior beliefs after receiving one disconfirmation signal are given by (DeGroot 1970)

$$
\delta_ {i t} \mid \tau_ {i t} \sim N (\bar {\delta} _ {i t}, (\gamma_ {i t} \cdot \tilde {\tau}) ^ {- 1}),\tag{8}
$$

$$
\tau_ {i t} \sim \Gamma (a _ {i t}, b _ {i t}),\tag{9}
$$

where

$$
\bar {\delta} _ {i t} = \bar {\delta} _ {i, t - 1} - D _ {j t} \cdot \frac {\mathrm{T} _ {j t}}{\mathrm{T} _ {j t} + \gamma_ {i , t - 1}} \cdot \Delta \bar {Q} _ {i j t},\tag{10}
$$

$$
\gamma_ {i t} = \gamma_ {i, t - 1} + D _ {j t},\tag{11}
$$

$$
a _ {i t} = a _ {i, t - 1} + D _ {j t} / 2,\tag{12}
$$

$$
b _ {i t} = b _ {i, t - 1} + D _ {j t} \cdot \frac {\mathrm{T} _ {j t} \cdot \gamma_ {i , t - 1} \cdot \Delta \bar {Q} _ {i j t} ^ {2}}{2 (\gamma_ {i , t - 1} + 1)},\tag{13}
$$

and $D _ { j t }$ is a dummy variable indicating whether there is at least one rating posted for j at occasion t. We further group all of the products into two major categories (experience versus search goods) and allow the belief updating mechanism to be category specific.

It is important at this time to point out how individual perception of the review system is updated. Consider a scenario where individual i has prior beliefs of $\delta _ { i , t - 1 } \mid \tau _ { i , t - 1 }$ and $\tau _ { i , t - 1 }$ . Suppose that she observes the rating signal for j and purchases $j$ during purchase occasion t. Upon product experience, she receives one disconfirmation signal, $\Delta \bar { Q _ { i j t } } ,$ and uses this private information to update her own beliefs. If there is no product rating available at the time of purchase $( \mathrm { i . e . , }$ $\mathbf { \dot { \boldsymbol { D } } } _ { j t } = 0 )$ , no belief updating will occur, and the beliefs will remain unchanged. If the rating signal is available $( \mathrm { i . e . , ~ } D _ { j t } = 1 )$ , she will update her beliefs in the system biasedness and precision jointly. According to Equation (10), the posterior mean $\bar { \delta } _ { i t }$ equals the prior mean minus the realized disconfirmation weighted by a fraction $\mathrm { T } _ { i t } / ( \mathrm { T } _ { i t } + \gamma _ { i , t - 1 } )$ . The rating signal precision $\mathrm { T } _ { i t }$ and the prior precision $\gamma _ { i , t - 1 }$ can be interpreted as the strength of the disconfirmation signal she has and the strength of the prior belief in system biasedness she holds, respectively. When $\mathrm { T } _ { i t }$ is large, individual i perceives the posted ratings to be more precise and therefore updates $\bar { \delta } _ { i t }$ by a relatively large amount, ceteris paribus. Similarly, the extent of updating of the scale parameter $b _ { i t }$ is increasing in the magnitude of the realized disconfirmation and the precision of the rating signal. When $\mathrm { T } _ { i t }$ is small, individual i anticipates the review signal to be noisy with a higher probability and therefore updates $b _ { i t }$ by a relatively small amount, ceteris paribus.

What remain unspecified are the initial belief parameters of each individual. The updating rule of the shape parameter indicates that the value of $a _ { i 0 }$ measures the richness of individual $i \prime \mathrm { s }$ initial learning experience. Since we can observe complete purchase histories for all individuals from our data set, we fix $a _ { i 0 }$ at a small number<sup>6</sup> (provided $a _ { i 0 } > 1 )$ because consumers have a very limited amount of learning experience with respect to system biasedness and precision until they receive the first disconfirmation signal. To allow for heterogeneity across individuals in their initial belief of system precision, we assume $b _ { i 0 } \sim N ( \bar { b } _ { 0 } , \sigma _ { b } ^ { 2 } )$ where $\bar { b } _ { 0 }$ and $\sigma _ { b } ^ { 2 }$ measure the mean efect and dispersion of $b _ { i 0 }$ across individuals, respectively. We further assume that $\delta _ { i 0 } = 0$ . This is reasonable because prior to the receipt of any disconfirmation signal, consumers may naturally perceive the review system to be unbiased, because of lack of purchase–consumption experience. Once they receive more disconfirmation signals, the perception of system biasedness will be updated depending on whether the perceived rating information inflates or underestimates ones’ own product assessment. Finally, we fix $\gamma _ { i 0 } = 0 . 1$ to reflect consumers having an uninformative initial belief of $\delta _ { i 0 } .$

## 4.3. Consumer Decisions to Leave Product Ratings

So far, we have presented a general model of how disconfirmation is derived, how the individual perception of the review system is updated, and how these two constructs are linked to each other. In this section, we discuss how we model consumers’ rating decisions.

Propensity Model. We model that a rater’s decision of whether to leave a product review is governed by latent posting propensity, which is specified as a function of (1) the disconfirmation she encounters, (2) the postpurchase evaluation she experiences, and (3) some other attributes such as intrinsic motivations and product price. Specifically, individual $i \prime \mathrm { s }$ propensity to post a review for product j associated with occasion $t , P r o p _ { i j t } ^ { * } ,$ is expressed as

$$
\begin{array}{r l} P r o p _ {i j t} ^ {*} = & P r o p _ {i j t} + \varepsilon_ {p, i j t} \\ & = \beta_ {i 1} + \beta_ {i 2} \Delta \bar {Q} _ {i j t} + \beta_ {i 3} \Delta \bar {Q} _ {i j t} ^ {2} + \beta_ {4} Q _ {i j t} + \beta_ {5} Q _ {i j t} ^ {2} \\ & \quad + \beta_ {6: 1 0} X _ {j t} + \beta_ {1 1: 1 5} (\Delta \bar {Q} _ {i j t} \times X _ {j t}) \\ & \quad + \beta_ {1 6: 2 0} (\Delta \bar {Q} _ {i j t} ^ {2} \times X _ {j t}) + \varepsilon_ {p, i j t}. \end{array}\tag{14}
$$

The individual-level parameter $\beta _ { i 1 }$ allows for variation in baseline propensity across reviewers. Under the random utility framework, $\beta _ { i 1 }$ can be interpreted as individual-specific net utility derived from posting a review online and can help control for rater heterogeneity in unobserved intrinsic motivations. The covariate $\Delta \bar { Q } _ { i j t }$ is the mean of disconfirmation given in (5), and $\dot { Q _ { i j t } }$ is the postpurchase evaluation given in (2). We also include quadratic terms for both constructs, $\Delta \bar { Q } _ { i j t } ^ { 2 }$ and $Q _ { i j t } ^ { 2 } ,$ to capture possible nonlinear relationships associated with $P r o p _ { i j t }$ . Parameters $\beta _ { i 2 }$ and $\beta _ { i 3 }$ together model the heterogeneous efect of disconfirmation on posting at the individual level. The control variables $\bar { \boldsymbol X } _ { j t }$ help us control for other factors that go beyond the individual level, such as product price, shipping and handling time, and the volume and variance of the previously posted ratings. We also include each individual’s purchase sequence number to control for a potential systematic shift in posting propensity over time. To further explore the factors that could moderate the disconfirmation efect, we allow both linear and quadratic terms of the disconfirmation construct to interact with $X _ { j t } .$ . Finally, since the outcome of the posting decision is binary (posting or lurking), we assume $\bar { \varepsilon _ { p , i j t } } \sim N ( 0 , 1 )$ such that the resulting propensity model has a binary probit specification

$$
\operatorname * {P r} (y _ {i j t} = 1) = \operatorname * {P r} (P r o p _ {i j t} ^ {*} > 0) = \Phi (P r o p _ {i j t}),\tag{15}
$$

where $y _ { i j t }$ is an occasion-specific dummy indicating whether a purchase leads to a review contribution.

We hypothesize the relationships between posting propensity and various independent variables and leave them as empirical questions. The parameters of our particular interest are $\beta _ { 1 }$ and $\beta _ { 2 }$ . The estimates of $\beta _ { 1 }$ and $\beta _ { 2 }$ together will inform us of the efect of disconfirmation on consumer participation in online WOM. In addition, it has been shown that online opinions are subject to a polar efect—consumers with extreme opinions tend to be more vocal (Anderson 1998, Dellarocas and Narayan 2006). From our model we will be able to verify whether our samples exhibit a similar polar efect based on the estimates of $\beta _ { 4 }$ and $\beta _ { 5 } .$

Evaluation Model. Now, suppose individual i has decided to leave a product rating for j. We assume that i’s decision of what score to give is governed by latent rating evaluation

$$
\begin{array}{r} E v a l _ {i j t} ^ {*} = E v a l _ {i j t} + \varepsilon_ {e, i j t} \\ = Q _ {i j t} + \lambda_ {1} \Delta \bar {Q} _ {i j t} + \lambda_ {2: 6} X _ {j t} + \varepsilon_ {e, i j t}, \end{array}\tag{16}
$$

where $\varepsilon _ { e , i j t }$ is a zero-mean random shock. Prior research has shown that a consumer’s overall satisfaction could be afected by the quality disconfirmation in of-line settings (Anderson and Sullivan 1993). Based on this theory, we model consumer rating evaluation as a linear combination of her experienced product quality, disconfirmation signal, and other control variables. Since rating evaluation is continuous, whereas the submitted ratings are discrete (1 to 5), we assume the relationship between them to follow

$$
z _ {i j t} = \left\{ \begin{array}{l l} 5 & \text {if} \kappa_ {4} <   E v a l _ {i j t} ^ {*} <   \kappa_ {5}, \\ 4 & \text {if} \kappa_ {3} <   E v a l _ {i j t} ^ {*} \leq \kappa_ {4}, \\ 3 & \text {if} \kappa_ {2} <   E v a l _ {i j t} ^ {*} \leq \kappa_ {3}, \\ 2 & \text {if} \kappa_ {1} <   E v a l _ {i j t} ^ {*} \leq \kappa_ {2}, \\ 1 & \text {if} \kappa_ {0} <   E v a l _ {i j t} ^ {*} \leq \kappa_ {1}, \end{array} \right.\tag{17}
$$

where $z _ { i j t }$ denotes the submitted rating scores, and $\kappa \cdot$ specifies the evaluation-rating translating cut points. For identification purposes, we set $\kappa _ { 0 } = - \infty , \ \kappa _ { 1 } = 0 .$ and $\kappa _ { 5 } = \infty$ (Koop et al. 2007), resulting in three cut points $\kappa _ { 2 } , \kappa _ { 3 }$ , and $\kappa _ { 4 }$ to be estimated.

## 4.4. Interdependence Between Two Rating Decisions

So far we have developed two separate models governing individual decisions of whether to post and what to rate. However, the covariance matrix of the equation system has not yet been clearly specified. Since $Q _ { i j t }$ enters two equations simultaneously, parameter estimates could be biased if the interdependence between two decisions is not properly specified. As a result, we assume two sets of error terms to follow a bivariate distribution

$$
\binom{\varepsilon_ {p}}{\varepsilon_ {e}} \sim B V N \biggl (\binom{0}{0}, \left( \begin{array}{c c} 1 & \rho \\ \rho & 1 \end{array} \right) \biggr).\tag{18}
$$

For identification purposes, we fix the standard deviations of $\varepsilon _ { p }$ and $\varepsilon _ { e }$ at 1 to obtain binary probit and ordered probit specifications, respectively. The parameter $\rho$ is the correlation coeficient to be estimated.<sup>7</sup> Given this covariance structure and the translating cut points defined in (17), the probability of observing a joint event of $y _ { i j t } = 1$ and $z _ { i j t } = s$ is given by

$$
\begin{array}{l} \operatorname * {P r} (y _ {i j t} = 1, z _ {i j t} = s) \\ = \left\{ \begin{array}{l} \Phi_ {2} (\infty , P r o p _ {i j t}, \rho) - \Phi_ {2} (\kappa_ {4} - E v a l _ {i j t}, P r o p _ {i j t}, \rho) \\ \quad s = 5, \\ \Phi_ {2} (\kappa_ {4} - E v a l _ {i j t}, P r o p _ {i j t}, \rho) - \Phi_ {2} (\kappa_ {3} - E v a l _ {i j t}, P r o p _ {i j t}, \rho) \\ \quad s = 4, \\ \Phi_ {2} (\kappa_ {3} - E v a l _ {i j t}, P r o p _ {i j t}, \rho) - \Phi_ {2} (\kappa_ {2} - E v a l _ {i j t}, P r o p _ {i j t}, \rho) \\ \quad s = 3, \\ \Phi_ {2} (\kappa_ {2} - E v a l _ {i j t}, P r o p _ {i j t}, \rho) - \Phi_ {2} (- E v a l _ {i j t}, P r o p _ {i j t}, \rho) \\ \quad s = 2, \\ \Phi_ {2} (- E v a l _ {i j t}, P r o p _ {i j t}, \rho) - \Phi_ {2} (- \infty , P r o p _ {i j t}, \rho) \\ \quad s = 1, \end{array} \right. \end{array}\tag{19}
$$

where $\Phi _ { 2 }$ denotes the standard bivariate normal cumulative distribution function. Our proposed model releases the independence assumption between two sets of observed outcomes $( y ^ { \prime } \mathbf { s }$ and $\bar { z } ^ { \prime } { \bf s } )$ ). The probability of observing $y _ { i j t } = 0 ( \mathrm { i . e . }$ ., lurking) can be expressed $\mathsf { a } \mathsf { \check { s } } ^ { 8 }$

$$
\operatorname * {P r} (y _ {i j t} = 0) = 1 - \Phi (P r o p _ {i j t}).\tag{20}
$$

Based on (19) and (20), the joint likelihood for observing individual i who makes m purchase occasions and posts n product ratings is given by

$$
\begin{array}{l} L _ {i} (y _ {i \cdot}, z _ {i \cdot}) \\ = \underbrace {\prod_ {t \in (y _ {i j t} = 0)} \operatorname* {P r} (y _ {i j t} = 0)} _ {m - n \text { terms}} \cdot \underbrace {\prod_ {t \in (y _ {i j t} = 1)} \operatorname* {P r} (y _ {i j t} = 1 , z _ {i j t} = s)} _ {n \text { terms}}, \end{array}\tag{21}
$$

and the likelihood of observing the entire decision set made by N individuals is $\begin{array} { r } { \prod _ { i = 1 } ^ { N } { \cal L } _ { i } ( y _ { i \cdot } , z _ { i \cdot } ) } \end{array}$

## 5. Estimation

For parameters that are subject to certain constraints, we apply the following transformation strategy. First, since the correlation coeficient $\rho$ takes value from <sup>[−</sup>1, 1<sup>]</sup> only, we estimate the inverse arctangent transformation of it, which maps the support <sup>[−</sup>1, 1<sup>]</sup> to a real line (Ying et al. 2006). Second, we estimate log $\left( \hat { b } _ { 0 } \right)$ instead of $\bar { b } _ { 0 }$ because the inverse scale parameter of a gamma distribution takes positive values only. Finally, we estimate the log of diference between two adjacent cutofs to ensure the magnitude of three cutofs to obey the desired order (i.e., $\kappa _ { 2 } < \kappa _ { 3 } < \kappa _ { 4 } )$ . For variables having a hyperdispersion property such as product price or order handling time, we take logarithm transformation. All variables are mean centered by subtracting their respective grand means to reduce the correlation between the estimated intercepts and slopes as well as to avoid potential multicollinearity in the propensity model.<sup>9</sup>

To estimate the proposed model, we use a hierarchical Bayes approach, which is convenient for the estimation of individual-specific parameters. Given the nature of the parameter hierarchy, the parameters in our model can be divided into two groups (Netzer et al. 2008): (1) “random-efect” parameters that vary across individuals (denoted by ${ \bar { \theta } } _ { i } )$ and (2) “fixed” parameters that do not vary across individuals (denoted by ψ<sup>)</sup>. We allow individual-specific parameters governing propensity intercept, product evaluation, and initial learning parameters to be correlated by assuming

$$
\theta_ {i} \sim \mathbf {M V N} (\bar {\theta}, \Sigma),\tag{22}
$$

where $\bar { \theta }$ denotes the mean efects that persist across individuals, and Σ denotes the covariance matrix of θ. As we do not have much prior knowledge about model parameters, we use a difuse multivariate normal distribution as the prior for the fixed parameters $\psi$ . Let $\xi _ { i }$ denote the individual-specific deviation from θ<sup>¯</sup>. Following (22), we can directly estimate those deviations using $\boldsymbol { \xi } _ { i } \sim \mathrm { M V N } ( \boldsymbol { 0 } , \boldsymbol { \Sigma } )$

A Markov Chain Monte Carlo (MCMC) procedure is developed to recursively draw parameters from the corresponding full conditional distributions using the following steps:

$$
\begin{array}{c} \xi_ {i} | Y _ {i}, Z _ {i}, \psi , \rho , \Sigma ; \\ \Sigma | \xi_ {i}; \\ \psi | Y, Z, \xi_ {i}, \rho ; \\ \rho | Y, Z, \psi , \xi_ {i}. \end{array}\tag{23}
$$

We adopt a random walk Metropolis–Hastings algorithm for steps where the conditional posterior distributions do not have a closed form. To improve the eficiency of the sampler, we use a two-step estimation approach. In the first step, we run a pilot MCMC sampler for 50,000 iterations and discard the first 10,000 draws as “burn-in” samples.<sup>10</sup> We calculate posterior means and the empirical covariance matrix based on the remaining 40,000 draws. In the second step, we run a separate MCMC sampler using the posterior means calculated in the previous step as the initial values and the empirical covariance matrix as the covariance parameters of the proposal distribution.<sup>11</sup> We run the MCMC sampler for 100,000 iterations and record every 10th draw only to mitigate the autocorrelation issue, which is an inevitable consequence of the MCMC simulation (Hof 2009). The adaptive chain converges immediately and explores the parameter space eficiently. To test convergence, we perform a Gelman and Rubin (1992) diagnostic by running three parallel chains with diferent initial values and random seeds. The potential scale reduction factors (PSRFs) are roughly 1.02 for all parameters, suggesting that the chains have converged to the target distributions.<sup>12</sup> We combine draws from three parallel chains, resulting in an efective sample size of at least 500 for each of the parameters.

## 5.1. Identification

We start the discussion on our identification strategy from the evaluation model. There are two common ways to identify an ordered probit model. The first approach is to estimate all four utility-rating cut points with no intercept. To identify the mean efect of the baseline evaluation, we adopt an alternative approach by holding one cut point as a constant $( \mathbf { i . e . } , \ \kappa _ { 1 } = 0 )$ and estimating the remaining three. Since \$¯ enters the evaluation model as an intercept coeficient, we do not need to explicitly estimate it as its identification is jointly achieved through the mean baseline evaluation. Given everything else is equal, the diference in the mean ratings among individuals helps us identify $\lambda _ { i 0 } .$ . Similarly, we can achieve the identification of the baseline propensity $\beta _ { i 1 }$ through the diference in the posting likelihood among individuals. In our learning framework, consumers first update their perception of the review system and then make a decision on rating scores. The dificulty is that we cannot identify ${ { \bar { a } } _ { 0 } }$ and $\bar { b } _ { 0 }$ simultaneously. Given that consumers have limited knowledge about how the review system can predict their own usage experience until the first disconfirmation signal is realized, we fix the richness of learning experience ${ { \bar { a } } _ { 0 } }$ at a small number (provided $\bar { a } _ { 0 } > 1 )$ such that $\bar { b } _ { 0 }$ is identifiable. Given everything else is equal, the variation in the change of posting behavior over time helps us identify the initial inverse scale parameter $b _ { i 0 } ,$ which determines the rate at which each individual learns about the system. Once $\bar { b } _ { 0 }$ is identified, the value of biasness parameter $\delta _ { i t }$ is determined and can be thought of as a constant c when it enters the propensity model. We can express the mean of the disconfirmation signal as $\Delta \bar { Q } _ { i j t } \bar { = } Q _ { i j t } - c .$ . Substituting $\Delta \bar { Q } _ { i j t } = Q _ { i j t } - c$ into the propensity model and collecting terms, we have $( \beta _ { 3 } + \beta _ { 5 } ) { \cal Q } _ { i j t } ^ { 2 } + ( \beta _ { 2 } + \beta _ { 4 } - 2 c \beta _ { 3 } ) { \cal Q } _ { i j t } -$ $\beta _ { 2 } c + \beta _ { 3 } c ^ { 2 }$ , with four identifiable parameters to be estimated.

Table 2. Model Fit and Comparison

<table><tr><td>Model feature</td><td>Full model</td><td>Model 1</td><td>Model 2</td><td>Model 3</td></tr><tr><td>Heterogeneity</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>Postpurchase evaluation</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>Disconfirmation</td><td>Yes</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Log-likelihood</td><td>-8,641.10</td><td>-9,013.46</td><td>-9,049.00</td><td>-10,792.41</td></tr><tr><td>DIC</td><td>18,139.35</td><td>18,538.86</td><td>18,609.83</td><td>21,604.44</td></tr><tr><td>ΔDIC w.r.t. full model</td><td></td><td>399.53</td><td>470.50</td><td>3,465.11</td></tr></table>

Note. A lower DIC is preferred.

## 5.2. Model Fit

To demonstrate the fit of our proposed model, we compare our full model with its three nested versions:

Model 1—a static, hierarchical model without disconfirmation constructs;

Model 2—a static, hierarchical model without postpurchase evaluation constructs;

Model 3—a static, nonhierarchical model without accounting for individual heterogeneity.

We compare the model performance based on the deviance information criterion (DIC), which is particularly useful in Bayesian model selection (Spiegelhalter et al. 2002). As Table 2 shows, our full model outperforms its three nested versions. The model performance becomes worse if we do not account for the efect of disconfirmation (Model 1) and the efect of postpurchase evaluation (Model 2). This result provides supportive evidence that it is desirable to incorporate the disconfirmation construct when modeling consumer online rating behavior. It is also worth noting that after we remove individual efects from our full model, the nonhierarchical model (Model 3) performs significantly worse, as indicated by a substantive increase in DIC. Such a sharp contrast suggests considerable heterogeneity across online users in their rating behavior and endorses the necessity of a richer, individual-level model like ours.

## 6. Results

Table 3 reports the posterior means of parameters specified in the propensity equation of the full model. Since the models are estimated using a Bayesian approach, we evaluate the significance levels of parameter estimates based on the highest posterior density (HPD) intervals. $\mathbf { A } \mathbf { n }$ HPD interval describes the information we have about the location of the true parameter after we have observed the data (Hof 2009). Parameter estimates are considered significant if a high percentage of the HPD interval does not contain zero.

Table 3. Estimation Results of the Propensity Model

<table><tr><td>Notation</td><td>Description</td><td>Posterior mean</td></tr><tr><td> $\beta_{i1}$ </td><td>Mean effect of baseline propensity</td><td>-2.0648***</td></tr><tr><td> $\beta_{i2}$ </td><td>Disconfirmation—linear ( $\Delta Q$ )</td><td>-0.0067*</td></tr><tr><td> $\beta_{i3}$ </td><td>Disconfirmation—quadratic ( $\Delta Q^{2}$ )</td><td>0.0428***</td></tr><tr><td> $\beta_{4}$ </td><td>Experienced quality—linear</td><td>-0.0084</td></tr><tr><td> $\beta_{5}$ </td><td>Experienced quality—quadratic</td><td>0.0485***</td></tr><tr><td> $\beta_{6}$ </td><td>Product price</td><td>0.2939***</td></tr><tr><td> $\beta_{7}$ </td><td>Shipping and handling time</td><td>-0.0399**</td></tr><tr><td> $\beta_{8}$ </td><td>Volume of posted ratings</td><td>0.0043</td></tr><tr><td> $\beta_{9}$ </td><td>Variance of posted ratings</td><td>0.0171**</td></tr><tr><td> $\beta_{10}$ </td><td>Purchase sequence number</td><td>-0.2791***</td></tr><tr><td> $\beta_{11}$ </td><td> $\Delta Q \times$ Product price</td><td>0.0173</td></tr><tr><td> $\beta_{12}$ </td><td> $\Delta Q \times$ Shipping and handling time</td><td>0.0312</td></tr><tr><td> $\beta_{13}$ </td><td> $\Delta Q \times$ Volume of posted ratings</td><td>-0.0090</td></tr><tr><td> $\beta_{14}$ </td><td> $\Delta Q \times$ Variance of posted ratings</td><td>0.0158</td></tr><tr><td> $\beta_{15}$ </td><td> $\Delta Q \times$ Purchase sequence number</td><td>0.0089</td></tr><tr><td> $\beta_{16}$ </td><td> $\Delta Q^{2} \times$ Product price</td><td>0.0053</td></tr><tr><td> $\beta_{17}$ </td><td> $\Delta Q^{2} \times$ Shipping and handling time</td><td>-0.0139**</td></tr><tr><td> $\beta_{18}$ </td><td> $\Delta Q^{2} \times$ Volume of posted ratings</td><td>0.0027</td></tr><tr><td> $\beta_{19}$ </td><td> $\Delta Q^{2} \times$ Variance of posted ratings</td><td>0.0076**</td></tr><tr><td> $\beta_{20}$ </td><td> $\Delta Q^{2} \times$ Purchase sequence number</td><td>0.0221***</td></tr></table>

<sup>∗</sup>90%, <sup>∗∗</sup>95%, <sup>∗∗∗</sup>99% of the HPD interval does not contain 0.

Our estimation results provide supportive evidence that consumers’ participation in leaving an online review ${ \mathrm { i } } \mathbf { s } ,$ at least partially, driven by the discrepancy between the expected and experienced assessments of the same product. The positive and significant $\beta _ { 3 }$ indicates that the relationship between posting propensity and disconfirmation is best described by a U-shaped curve, as depicted in Figure 4; that ${ \mathrm { i } } s ,$ the probability of an individual leaving a review increases as the postpurchase evaluation further deviates from the prepurchase expectation. On the other hand, an individual is more likely to demonstrate lurking when her product assessment is quite close to the expected quality. Moreover, the negative sign of $\beta _ { 2 }$ suggests that consumers’ posting decisions are impacted by the negative disconfirmation to a larger extent, ceteris paribus. The identified disconfirmation efect can be attributed to various motivations such as altruism and venting. An altruist may praise the product by submitting a score higher than the current mean level when she experiences positive disconfirmation. By contrast, if she encounters negative disconfirmation, she may warn peer consumers to be vigilant with the product by leaving a low rating. While prior works have documented several motives behind consumers engaging in WOM from a normative point of view (Hennig-Thurau et al. 2004, Sundaram et al. 1998), this research provides a positive, empirical validation and hence contributes to the literature by demonstrating that disconfirmation is one of the many factors that drive consumers to voluntarily engage in online WOM.

Figure 4. (Color online) The Efect of Disconfirmation on Posting Behavior  
![](/api/attachments/HF6HQ4MT/fulltext/images/a4b48eba16f5542e616ad5e938b910ee79898c37e56de90dfa9ef08afcb28d77.jpg)

From Table 3, we can see that consumers are likely to express their product opinions when they are either extremely satisfied or dissatisfied, as suggested by the positive and significant $\beta _ { 5 } .$ This finding echoes the polar efect of experiences on opinion sharing in both of-line settings (e.g., Anderson 1998) and online settings (e.g., Dellarocas and Narayan 2006). Our results also suggest that consumers are more interested in reviewing products with a higher price $\left( \beta _ { 6 } > 0 \right)$ and products that are delivered in a timely manner $( \beta _ { 7 } < 0 )$ . As to the impact of rating environments, the positive estimate of $\beta _ { 9 }$ informs us that dissentious rating environments induce active posting behavior from a focal rater. Finally, reviewers are less likely to post ratings for products purchased at a later time.

We can further uncover factors that moderate the disconfirmation efect on posting behavior by allowing the two disconfirmation constructs to interact with other control variables. Coeficient estimates for the 10 interaction terms can be respectively interpreted as how each of the control variables changes the location of the turning point $( \beta _ { 1 1 : 1 5 } )$ and the convexity $( \beta _ { 1 6 : 2 0 } )$ of the nonlinear relationship between posting and disconfirmation (see Figure 4). The results indicate three interesting findings. First, the disconfirmation efect attenuates as the duration from purchase to receipt of the same product extends further $( \beta _ { 1 7 } < 0 )$ . A plausible explanation is that an individual’s memory for her prepurchase expectation naturally fades over time. As a result, the individual’s rating propensity is less afected by disconfirmation as shipping and handling time increases. Second, the variance of posted ratings accentuates the impact of expectation–evaluation discrepancy on rating propensity $( \beta _ { 1 9 } > 0 )$ . In other words, the level of dissension among peer reviewers accentuates the impact of disconfirmation on review contribution.

Table 4. Estimation Results of Evaluation Model and Other Parameters

<table><tr><td>Notation</td><td>Description</td><td>Posterior mean</td></tr><tr><td> $\lambda_{i0}$ </td><td>Mean effect of baseline evaluation</td><td>-1.9865***</td></tr><tr><td> $\lambda_1$ </td><td>Disconfirmation—linear</td><td>0.0248*</td></tr><tr><td> $\lambda_2$ </td><td>Product price</td><td>0.0231</td></tr><tr><td> $\lambda_3$ </td><td>Shipping and handling time</td><td>-0.1057***</td></tr><tr><td> $\lambda_4$ </td><td>Volume of the posted ratings</td><td>-0.0128</td></tr><tr><td> $\lambda_5$ </td><td>Variance of the posted ratings</td><td>-0.0313*</td></tr><tr><td> $\lambda_6$ </td><td>Purchase sequence number</td><td>-0.0023</td></tr><tr><td> $\kappa_2$ </td><td>Cut point for s=2 and 3</td><td>0.4853</td></tr><tr><td> $\kappa_3$ </td><td>Cut point for s=3 and 4</td><td>1.4069</td></tr><tr><td> $\kappa_4$ </td><td>Cut point for s=4 and 5</td><td>2.4650</td></tr><tr><td> $\sigma_\omega$ </td><td>Random effect of quality discrepancy</td><td>0.0121</td></tr><tr><td> $b_{i0}$ </td><td>Mean effect of initial inverse scale parameter</td><td>5.8463</td></tr><tr><td> $\rho$ </td><td>Interdependency between two rating stages</td><td>0.0794</td></tr></table>

Note. Significance levels are reported for raw parameters (λ<sup>)</sup> only. <sup>∗</sup>90%, <sup>∗∗∗</sup>99% of the HPD interval does not contain 0.

Finally, online shoppers become more susceptible to the disconfirmation efect when they make more purchases over time $( \beta _ { 2 0 } > 0 )$ . To this point, our empirical findings on various moderating factors of disconfirmation can contribute to the literature stream on the expectation–disconfirmation paradigm.

The posterior means of parameters of the evaluation model are presented in Table 4. We see that disconfirmation has a positive impact on the rating decision, meaning that online consumers tend to factor their expectation into product experience. This finding echoes the bias disconfirmation has on experience identified in of-line settings (Anderson and Sullivan 1993). Shipping and handling time has a negative impact on the rating evaluation $( \lambda _ { 3 } < 0 )$ . This result provides evidence that online consumers tend to reflect their dissatisfaction at the e-commerce site in product ratings. Moreover, raters tend to be harsher in terms of giving online ratings when the opinions from peers are more dissentious. It is also worth noting that the coeficient estimate for product price is positive but insignificant. This result suggests that price in general serves as a weak proxy for perceived quality.

Figure 5. Distributions of Individual-Level Parameters  
(a) Distribution of $\beta _ { i 1 }$  
![](/api/attachments/HF6HQ4MT/fulltext/images/980581e9ee4df33298f65cc934d0c2ab790cbfb91f73cd64aa700efde4dd1999.jpg)

Table 5. Correlation Matrix

<table><tr><td></td><td> $\beta_{i1}$ </td><td> $\beta_{i2}$ </td><td> $\beta_{i3}$ </td></tr><tr><td> $\beta_{i1}$ </td><td>1.0000</td><td>-0.0532</td><td>-0.1102**</td></tr><tr><td> $\beta_{i2}$ </td><td></td><td>1.0000</td><td>0.0536</td></tr><tr><td> $\beta_{i3}$ </td><td></td><td></td><td>1.0000</td></tr></table>

<sup>∗∗</sup>95% of the HPD interval does not contain 0.

A scrutiny of the individual-level parameters reveals several insights at a more granular level. Figure 5 plots the distributions of the three rater-specific parameters of the propensity model. We observe large variations in the baseline posting propensity across consumers $( \beta _ { i 1 } ) .$ suggesting that individuals are quite diferent with respect to how each individual’s posting behavior is driven by various intrinsic motivations. Additionally, about 27% of reviewers are subject to the disconfirmation efect to a large extent $( \beta _ { i 3 } > 0 . 1 )$ . Table 5 presents the correlation matrix of the three individuallevel parameters. The negative correlation between $\beta _ { i 1 }$ and $\beta _ { i 3 }$ indicates that occasional raters are more susceptible to the disconfirmation efect than frequent posters. Such a systematic diference in posting behavior provides an important managerial implication— ratings posted by occasional raters may not objectively reflect their experienced quality because of the positive disconfirmation bias $( \lambda _ { 1 } > 0 )$

## 6.1. Robustness Checks

In this section, we perform three robustness checks by including additional variables and samples in our model. The consistent parameter estimates demonstrate the robustness of our results.

While the individual-specific baseline propensity $( \beta _ { i 1 } )$ can model an individual’s opportunity cost of leaving a review, we do not consider how the size of each individual’s consideration set for review (total number of products purchased) influences her posting decision. Since a consumer’s time for writing reviews is limited, it is reasonable to conjecture that a product is more likely to be reviewed when the consumer only purchases a few products over a certain time period than when she purchases many. To examine this impact, we construct a new variable based on the following rule. For each focal product j, we calculate the total number of products a customer has received and is about to receive within seven days before and after the date of receipt (j). We choose seven days for the time cutof because in our data an overwhelming majority of reviews are submitted within a week after receipt of the product. The estimation results are presented in the first column of Table 6, which reports estimation results from all three robustness checks introduced in Section 6.1. The new parameter estimates are not substantively diferent from those of the full model, suggesting the robustness of our results. The negative coeficient estimate for the new control variable confirms our intuition regarding the negative relationship between the likelihood of posting and the size of a rater’s consideration set for review. Finally, we find that our model remains robust if we use diferent time cutofs (within 3, 14, 21, and 28 days before and after the receipt date of j<sup>)</sup> in calculating the new variable.

(b) Distribution of $\beta _ { i 2 }$  
![](/api/attachments/HF6HQ4MT/fulltext/images/803f79970486e938052ffda9d5dec55700c89a051b44e5f374dff283ce4477ca.jpg)

(c) Distribution of $\beta _ { i 3 }$  
![](/api/attachments/HF6HQ4MT/fulltext/images/1bf4ac6cffea22e0bc411d07192940d2d922a890d106830ea43679426a481c84.jpg)

Table 6. Estimation Results from Robustness Checks

<table><tr><td>Variable descriptions</td><td>Robustness check 1</td><td>Robustness check 2</td><td>Robustness check 3</td></tr><tr><td colspan="4">Propensity Model</td></tr><tr><td>Mean effect of baseline propensity</td><td>-2.1543***</td><td>-1.8155***</td><td>-1.2405***</td></tr><tr><td>Disconfirmation—linear (ΔQ)</td><td>-0.0031</td><td>-0.0126</td><td>-0.0053</td></tr><tr><td>Disconfirmation—quadratic (ΔQ2)</td><td>0.0423***</td><td>0.0450***</td><td>0.0167***</td></tr><tr><td>Perceived system precision</td><td>-0.1909***</td><td>-0.1115***</td><td>-0.2387***</td></tr><tr><td>Experienced quality—linear</td><td>0.0110</td><td>0.0603</td><td>-0.0257</td></tr><tr><td>Experienced quality—quadratic</td><td>0.0493***</td><td>0.0546***</td><td>0.0346**</td></tr><tr><td>Product price</td><td>0.2452***</td><td>0.2125***</td><td>0.2112***</td></tr><tr><td>Shipping and handling time</td><td>-0.0155</td><td>-0.0336*</td><td>-0.0571**</td></tr><tr><td>Volume of posted ratings</td><td>-0.0033</td><td>-0.0029</td><td>-0.0068</td></tr><tr><td>Variance of posted ratings</td><td>0.0114</td><td>0.0117</td><td>0.0177*</td></tr><tr><td>Purchase sequence number</td><td>-0.2068***</td><td>-0.2517***</td><td>-0.1683***</td></tr><tr><td colspan="4">Evaluation Model</td></tr><tr><td>Mean effect of baseline evaluation</td><td>-1.9795***</td><td>-1.9480***</td><td>-2.4405***</td></tr><tr><td>Disconfirmation—linear</td><td>-0.0329*</td><td>-0.0290*</td><td>0.0429</td></tr><tr><td>Perceived system precision</td><td>-0.1170</td><td>0.1350</td><td>0.1945</td></tr><tr><td>Product price</td><td>0.0321</td><td>0.0297</td><td>-0.0022</td></tr><tr><td>Shipping and handling time</td><td>-0.1090***</td><td>-0.1035**</td><td>-0.1218***</td></tr><tr><td>Volume of posted ratings</td><td>-0.0130</td><td>-0.0143</td><td>-0.0280**</td></tr><tr><td>Variance of posted ratings</td><td>-0.0301*</td><td>-0.0301*</td><td>-0.0192</td></tr><tr><td>Purchase sequence number</td><td>-0.0449</td><td>-0.0502</td><td>-0.0864***</td></tr><tr><td>Total number of products received</td><td>-0.1982***</td><td>—</td><td>—</td></tr><tr><td>Category dummy (1 = experience goods)</td><td>—</td><td>-0.3842***</td><td>—</td></tr><tr><td>Number of individuals</td><td>361</td><td>361</td><td>1,000</td></tr><tr><td>Number of observations</td><td>37,209</td><td>37,209</td><td>97,199</td></tr></table>

<sup>∗</sup>90%, <sup>∗∗</sup>95%, <sup>∗∗∗</sup>99% of the HPD interval does not contain 0.

In our full model, we control for several observable characteristics beyond the individual level, such as product prices, shipping and handling time, and the characteristics of the rating environments. Consumer posting decisions may also be afected by other product-level attributes such as categories. For example, an individual may be more interested in reviewing a book than a utensil set. To investigate the potential dissimilar efects across various product types, we first categorize all products into experience goods and search goods by constructing a dummy variable (0 <sup></sup> search goods; 1 <sup></sup> experience goods) and include it in the propensity model. As we see from the second column of Table 6, the estimation results are still consistent after controlling for the product category. The coeficient estimate for the category dummy indicates that consumer posting propensity for experience goods is significantly lower than that for research goods. We also reconstruct the category dummy by following the e-commerce site’s own taxonomy. While we observe dissimilar efects on posting across various categories, the main results do not change substantively.

So far, we have excluded data points of nonraters for identification purposes. To further assess the robustness of our results, we add nonrater samples back in and estimate a nested model without the specification of any individual efect. The estimation results are reported in the third column of Table 6. While we observe minor changes in magnitude, the parameter estimates stay qualitatively the same after we include data points from nonraters. More importantly, after we remove various individual efects from our full model, the nested model performs significantly worse, as indicated by a substantive increase in DIC. Such a sharp contrast suggests considerable heterogeneity across online raters in their rating behavior and the necessity of a richer, individual-level model like ours.

## 6.2. Predictive Ability

To validate the estimation results, we evaluate the predictive ability of our full model with respect to posting and rating decisions of online consumers. We begin this section by discussing how we divide the data set for estimation into calibration and holdout samples. The most common approach used in prior research is to choose a time cutof such that the observations before and after the cutof constitute the calibration and validation samples, respectively (typically, 70% versus 30% of all data). However, a universal cutof for all users may reduce our sample size because it is likely that the identification condition of one review is violated for users who joined the site in a later period. To address this issue, we use the first 70% of observations of each individual to calibrate the model and use the remaining 30% for validation. In fact, such a holdout strategy makes more sense in our model because it allows us to gauge the dynamics of online rating behavior at the individual level. The validation results suggest that the prediction accuracy of the full model is 93.6% for posting decisions and 38.6% for rating decisions, respectively. It is worth noting that the prediction accuracy on rating decisions significantly improves compared with the model of Ying et al. (2006) in the context of movies (20.8%).

## 6.3. Managerial Implications and Discussions

This study provides important insights for managers of e-commerce sites, recommender system designers, and marketers who attempt to interfere with online WOM environments. Several actionable strategies are immediate from the findings from our empirical results. For example, we find that consumers are more prone to contribute reviews when they receive the products in a timely manner. A useful implication for managers is that they should speed up the order fulfillment process if the goal is to increase the volume of online WOM. Moreover, we also observe a negative impact of shipping and handling time on product evaluations. Managers of e-commerce sites should pay attention to maintaining good service because consumers will reflect their dissatisfaction with the site in product ratings, which, in turn, may lead to lower purchase intent from potential customers. Review system designers should take some proactive actions such as designing a review system that allows users to evaluate the service of the site and the product experience in separate items.

Designers of a recommender system can also benefit from the findings uncovered at the individual level. For example, we observe systematic diferences in rating behaviors between frequent raters and occasional posters. Since a frequent rater is more resistant to disconfirmation when making a decision of whether to post a review, the opinions they express are less subject to the disconfirmation bias and therefore are considered more objective than those of occasional posters. If the ultimate goal of a recommender system is to provide an unbiased signal about product quality, system designers should not believe “all reviews are created equal.” Instead, they should, to some extent, discount the ratings input by infrequent posters when utilizing the collective intelligence from the crowd.

Our estimation results can also be used to understand how review manipulations influence the subsequent rating entries. In what follows, we perform a simulation by considering a scenario where an ecommerce site sells a fictitious product with the true quality being equivalent to a rating of 3.5. Suppose the site is able to inflate the average rating to a targeted level through some manipulative tactics. Our objective here is to compare subsequent posted ratings when such manipulations are present versus absent in the prepurchase stage. We perform the simulation by following the procedure below.

1. We sample 100 individuals from the estimates of covariance matrix Σ. We assume that those 100 individuals purchase and consume the product with true quality being equivalent to 3.5 stars.

2. For each individual, we first simulate her posting decision under two cases: (1) when she observes a neutral mean rating of 3.5 and (2) when she observes a fake, inflated mean rating of 4.0, 4.5, or 5.0 prior to the purchase. For each individual who decides to post a rating, we simulate her decision of what rating to post.

3. We repeat Steps 1 and 2 for 5,000 iterations and average the two decisions across iterations.

As Table 7 shows, it is evident that consumers are more likely to share usage experience when the observed mean ratings overreport the true quality to a larger extent. More importantly, the means of subsequently posted ratings are much lower in the presence of fake reviews. Combined, our simulation results suggest that the unrealistic and high expectation led by inflated ratings may strongly induce more and negative reviews from consumers who experience negative disconfirmation. This finding has useful implications for marketers who attempt to influence user-generated product opinions through manipulative strategies. Although inflated ratings can deceptively elevate consumers’ prepurchase expectations and hence reap additional revenue in the short run, such a tactic may not be sustainable in the long run as more dissatisfied customers vent their frustrations for anxiety reduction or vengeance purposes. While the impact of textual reviews goes beyond the scope of this research, marketers should be vigilantly aware that the negative sentiments and abusive language expressed by disgruntled customers could cause even more serious damage to the firm in various aspects like sales revenue, brand image, and beyond.

Table 7. Efect of Inflated Ratings on Subsequent Rating Entries

<table><tr><td>Mean ratings observed before purchase</td><td>Subsequent posting rates (%)</td><td>Mean subsequent posted ratings</td></tr><tr><td>3.5</td><td>5.853</td><td>3.497</td></tr><tr><td>4.0</td><td>6.031</td><td>3.451</td></tr><tr><td>4.5</td><td>6.496</td><td>3.427</td></tr><tr><td>5.0</td><td>7.213</td><td>3.418</td></tr></table>

We conclude this section by conducting a simulation to better understand the underlying mechanism of online rating behavior. Given our estimation results, we “recover” the unobserved evaluation outcomes for all lurking occasions $( y _ { i j t } = 0 )$ . The simulation procedure is summarized as follows:

1. We compute the latent posting propensity per (14) and evaluation per (16) for all purchase occasions based on the posterior estimates.

2. Given the computed posting propensity, evaluation, and estimated cut points, we simulate the decisions of whether to rate per (15) and what to rate per (17).

3. We repeat Step 2 for 1,000 iterations and compute the average for the quantities of our interest across iterations.

4. To make sure the number of iterations is suficient, we repeat Steps 2 and 3 in three parallel processes with diferent random seeds. We compare simulated results and do not find any inconsistency across processes.

For interpretation purposes, we compute the posting rates, defined as the number of posting sessions divided by the number of total purchase occasions, and plot them against diferent levels of postpurchase evaluation (Figure 6(a)) and rating discrepancy (Figure 6(b)). We can see that the relationship between posting rate and discretized product evaluation is best characterized by a left-skewed U shape. Negative experiences (rated as 1 or 2) have a higher chance of being reported (7.44% and 6.10%, respectively), relative to neutral (5.88%) and positive evaluations (5.54% and 5.70%). It is evident that disappointed or disgruntled consumers are more vocal in expressing opinions about the product. The simulation results provide sharp insight into what drives consumers to leave online reviews, an insight that cannot be discovered from a simple descriptive analysis, as shown in Figures 1 and 2.

## 7. Conclusion

The primary objective of this paper was to study the efect disconfirmation has on consumer rating behavior in an online setting. The early research on online product reviews studied how customer-reported reviews can be related to market performance, whereas recent work focuses on the impact of posted ratings on subsequent ones from a social dynamics standpoint (Lee et al. 2015, Moe and Schweidel 2012, Shen et al. 2015). Our work contributes to the latter literature stream by proposing a novel framework in which the process of opinion formation starts even before the product is purchased and experienced. We also model how consumer perception of the review system evolves over time as a result of a series of disconfirmation signals. By integrating these two features in the individual decision-making process, we empirically test the hypothesized impact of disconfirmation on posting decisions.

Using a rich data set containing complete purchasing and rating activities at the individual level, we empirically show that the relationship between posting probability and disconfirmation is best described by a nonlinear U-shaped curve. We also observe several moderating factors: the disconfirmation efect is attenuated by the duration from purchase to receipt of the same product but accentuated by the dissension in product experience among peer consumers. A further examination of the results at a micro level reveals that occasional raters are more responsive to disconfirmation than frequent reviewers. This study provides several important insights into online rating behavior, providing useful managerial implications for both marketers and designers of recommender systems.

Figure 6. Dissimilar Efects of Diferent Measurements on Posting Behavior  
(a) Posting rate (%) vs. discretized evaluation  
![](/api/attachments/HF6HQ4MT/fulltext/images/0cdd01465cf3df4985b762d8b4620527f0d1ba94c966d494f43d44b677139da2.jpg)

(b) Posting rate (%) vs. rating discrepancy  
![](/api/attachments/HF6HQ4MT/fulltext/images/8780cc0c591112f6d1b1378743e873ae40db1a49ad9db1c4193ed9a9952adfae.jpg)

The main findings of this paper echoes prior research in some aspects but also provides new insights in others. On one hand, disconfirmation serves as one of the underlying drivers of why people engage in WOM, such as concern for others, anxiety/dissonance reduction, vengeance, etc. (Anderson 1998, Hennig-Thurau et al. 2004). The identified disconfirmation efect can also, at least partially, explain (1) the common U-shaped distribution of online ratings and (2) the declining trend of average ratings at the product level. On the other hand, we argue that the presence of the disconfirmation efect helps “correct” the valence of posted ratings to some extent. This proposition deviates somewhat from that of Hu et al. (2006), who proposed that the mean ratings under some conditions may provide biased information about product quality, an argument contingent on an explicit assumption that consumer posting decisions are triggered solely by the experienced quality.

This study has some data limitations and can be improved in the following directions. Clickstream data, particularly in the prepurchase stage, would allow us to enrich our econometric models in many diferent ways. For example, if the sitewide browsing history were available at the individual level, we would be able to observe each consumer’s consideration set and assess the role of existing ratings in consumer purchase decisions. We could also model how consumer perception of the review system influences individual decisions of which site to shop with if we had complete browsing records across various platforms at the individual level. Another promising direction for future research is to apply text mining techniques to extract the sentiments stored in the textual reviews and incorporate them into our econometric model. The synergy brought by the integration of diferent research techniques would allow us to provide a shaper insight into consumer online rating behavior.

## Acknowledgments

The authors thank the senior editor, the associate editor, and the anonymous reviewers for their constructive suggestions. The authors also thank Guodong Gao, Hossein Ghasemkhani, Yan Huang, Zhuoxin Li, Param Vir Singh, and participants at the 2013 INFORMS Conference on Information Systems Technology and research seminars at the Beĳing Institute of Technology, Dalian University of Technology, Fudan University, the George Washington University, the Hong Kong University of Science and Technology, Purdue University, Santa Clara University, the University of British Columbia, the University of International Business and Economics, the University of California, San Diego, the University of Maryland, the University of Texas at Austin, the University of Texas at Dallas, and Zhejiang Gongshang University for their helpful comments. Yong Tan is the Chang Jiang Scholar Visiting Chair Professor at Tsinghua University.

## Endnotes

<sup>1</sup> Following prior literature, we use reviews to refer to a general format of consumer evaluation and ratings to refer to numeric values indicating overall satisfaction.

<sup>2</sup> We model online rating behavior as individuals’ decision of whether to leave a rating in the postpurchase stage. As a result, we will not be able to identify any individual efect for nonraters because there is no variation in their posting decisions. In Section 6.1, we conduct a robustness check by estimating a nested model with no individual efect. The estimation results show that our hierarchical model significantly outperforms the nonhierarchical one, suggesting substantive heterogeneity among shoppers in rating behavior and the necessity for a microlevel model.

<sup>3</sup> The 361 raters account for 36.5% of all revenue generated and 33.4% of all items purchased by the 1,000 randomly selected users.

<sup>4</sup> According to a survey conducted by Lightspeed Research (Leggatt 2011), 72% of online shoppers expect to find customer reviews available on the website they are shopping at, while 47% seek them out on company websites and 43% seek them out on price comparison sites. Therefore, we assume that one’s expectation is primarily influenced by the mean ratings observed on the same site. The precision characterizes the level of disagreement among others. We use precision instead of variance because the former gives us a better expression of belief updating.

<sup>5</sup> In the context of Bayesian learning, disconfirmation defined here follows a normal model with unknown mean and unknown variance. The conjugate prior for this model is a normal-gamma joint distribution.

<sup>6</sup> The choice of $a _ { i 0 }$ is subjective. We estimate the proposed model with $a _ { i 0 }$ fixed at diferent values (2.5, 5, 10, and 20), and we do not observe notable changes for the estimated parameters. Given this result, we report the estimation results with $a _ { i 0 } = 5$ since it gives the best model fit.

<sup>7</sup> Alternatively, one can compute the inverse Mills ratio (IMR) from the propensity model and plug ρ <sup>·</sup> IMR into Equation (16).

<sup>8</sup> The marginal distribution of one series of bivariate normally distributed variables is simply a normal density.

<sup>9</sup> We calculate the variance inflation factor (VIF) for the covariates included in the propensity model, and the result shows no evidence of multicollinearity (VIF < 2).

<sup>10</sup> The choice of burn-in period is based on visual observation of the trace plot of MCMC draws. In fact, 25,000 is a conservative number since the chain appears to converge after the initial 5,000 iterations.

<sup>11</sup> The scale parameter of the proposal distribution is adaptively chosen such that the acceptance rate is around 23%, as suggested for high-dimensional vectors (Gelman et al. 2013).

<sup>12</sup> A series of MCMC draws are considered to achieve convergence as long as the PSRF is less than 1.2.

## References

Anderson EW (1998) Customer satisfaction and word of mouth. J. Service Res. 1(1):5–17.

Anderson EW, Sullivan MW (1993) The antecedents and consequences of customer satisfaction for firms. Marketing Sci. 12(2):125–143.

Bearden WO, Teel JE (1983) Selected determinants of consumer satisfaction and complaint reports. J. Marketing Res. 20(1):21–28.

Bhattacherjee A (2001) Understanding information systems continuance: An expectation-confirmation model. MIS Quart. 25(3): 351–370.

Bolton RN, Drew JH (1991) A multistage model of customers’ assessments of service quality and value. J. Consumer Res. 17(4): 375–384.

Chaiken S (1980) Heuristic versus systematic information processing and the use of source versus message cues in persuasion. J. Personality Soc. Psych. 39(5):752–766.

DeGroot MH (1970) Optimal Statistical Decisions, Vol. 82 (Wiley-Interscience, New York).

Dellarocas C (2006) Strategic manipulation of Internet opinion forums: Implications for consumers and firms. Management Sci. 52(10):1577–1593.

Dellarocas C, Narayan R (2006) A statistical measure of a population’s propensity to engage in post-purchase online word-ofmouth. Statist. Sci. 21(2):277–285.

Dellarocas C, Fan M, Wood C (2004) Self-interest, reciprocity, and participation in online reputation systems. Working paper, Boston University, Boston.

Dellarocas C, Gao G, Narayan R (2010) Are consumers more likely to contribute online reviews for hit or niche products? J. Management Inform. Systems 27(2):127–158.

Dichter E (1966) How word-of-mouth advertising works. Harvard Bus. Rev. 44(6):147–160.

Gelman A, Rubin DB (1992) Inference from iterative simulation using multiple sequences. Statist. Sci. 7(4):457–472.

Gelman A, Carlin JB, Stern HS, Dunson DB, Vehtari A, Rubin DB (2013) Bayesian Data Analysis, 3rd ed. (Chapman & Hall/CRC Press, Boca Raton, FL).

Gormley M (2013) NY attorney general cracks down on fake online reviews. NBC News (September 23), http://www.nbcnews.com/ tech/internet/ny-attorney-general-cracks-down-fake-online -reviews-f4B11235875.

Hennig-Thurau T, Gwinner KP, Walsh G, Gremler DD (2004) Electronic word-of-mouth via consumer-opinion platforms: What motivates consumers to articulate themselves on the Internet? J. Interactive Marketing 18(1):38–52.

Hof PD (2009) A First Course in Bayesian Statistical Methods (Springer, New York).

Hu N, Pavlou PA, Zhang J (2006) Can online reviews reveal a product’s true quality?: Empirical findings and analytical modeling of online word-of-mouth communication. Proc. 7th ACM Conf. Electronic Commerce (ACM, New York), 324–330.

Koop G, Poirier DJ, Tobias L (2007) Bayesian Econometric Methods <sup>(</sup>Econometric Exercises<sup>)</sup> (Cambridge University Press, New York).

Lee YJ, Hosanagar K, Tan Y (2015) Do I follow my friends or the crowd? Information cascades in online movie ratings. Management Sci. 61(9):2241–2258.

Leggatt H (2011) 24% of consumers turned of after two negative online reviews 2011. BizReport (April 13), http://www .bizreport.com/2011/04/27-of-consumers-turned-of-by-just-two -negative-online-revie.html.

Li X, Hitt LM (2008) Self-selection and information role of online product reviews. Inform. Systems Res. 19(4):456–474.

MarketingCharts (2007) Most consumers read and reply on online reviews; companies must adjust. (November 2). http:// www.marketingcharts.com/online/most-consumers-read-and -rely-on-online-reviews-companies-must-adjust-2234/.

McGlohon M, Glance N, Reiter Z (2010) Star quality: Aggregating reviews to rank products and merchants. Presentation, Internat. Conf. Weblogs Soc. Media, Washington, DC, 127–139.

McKinney V, Yoon K, Zahedi FM (2002) The measurement of web-customer satisfaction: An expectation and disconfirmation approach. Inform. Systems Res. 13(3):296–315.

Moe WW, Schweidel DA (2012) Online product opinions: Incidence, evaluation, and evolution. Marketing Sci. 31(3):372–386.

Netzer O, Lattin JM, Srinivasan V (2008) A hidden Markov model of customer relationship dynamics. Marketing Sci. 27(2):185–204.

Nielson (2007) Word-of-mouth the most powerful selling tool, http://nielsenmedia.co.nz/files/TrustinAdvertisingOct07.pdf.

Oliver RL (1977) Efect of expectation and disconfirmation on postexposure product evaluations: An alternative interpretation. J. Appl. Psych. 62(4):480–486.

Oliver RL (1980) A cognitive model of the antecedents and consequences of satisfaction decisions. J. Marketing Res. 17(4):460–469.

Rust RT, Inman JJ, Jia J, Zahorik A (1999) What you don’t know about customer-perceived quality: The role of customer expectation distributions. Marketing Sci. 18(1):77–92.

Schlosser AE (2005) Posting versus lurking: Communicating in a multiple audience context. J. Consumer Res. 32(2):260–265.

Shen W, Hu YJ, Ulmer JR (2015) Competing for attention: An empirical study of online reviewers’ strategic behavior. MIS Quart. 39(3):683–696.

Spiegelhalter DJ, Best NG, Carlin BP, Van Der Linde A (2002) Bayesian measures of model complexity and fit. J. Royal Statist. Soc.: Ser. B, Statist. Methodology 64(4):583–639.

Sundaram DS, Mitra K, Webster C (1998) Word-of-mouth communications: A motivational analysis. Adv. Consumer Res. 25(1): 527–531.

Susarla A, Barua A, Whinston AB (2003) Understanding the service component of application service provision: Empirical analysis of satisfaction with ASP services. MIS Quart. 27(1):91–123.

Taylor SJ (2014) Don’t fall for fake online reviews. U.S. News World Rep. (July 8), http://money.usnews.com/money/personalfinance/ articles/2014/07/08/dont-fall-for-fake-online-reviews.

Ying Y, Feinberg F, Wedel M (2006) Leveraging missing ratings to improve online recommendation systems. J. Marketing Res. 43(3):355–365.
